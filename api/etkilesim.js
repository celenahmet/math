// api/etkilesim.js — blog yazisinda "faydali mi", ifade, yorum ve geri bildirim (25.09.2026)
//
// Ayrinti ve guvenlik gerekcesi: api/_etkilesim.js basindaki not.
//
//   GET  ?yol=/blog/<slug>/   sayilar + onayli yorumlar (CDN'de 20 sn onbellek;
//                              cerez okunmaz, kisiye ozel hicbir sey donmez)
//   GET  ?meydan=1            is kaniti bulmacasi (onbelleksiz, depoya dokunmaz)
//   POST { yol, tur, ... , cozum }
//        tur=oy      deger: begeni | begenmeme | ""  (bos = geri al)
//        tur=ifade   deger: _ifadeler.json anahtari | ""
//        tur=yorum   rumuz, metin (onaydan sonra yayinlanir)
//        tur=geri    metin (yalniz bu yaziya "faydali degil" demis ziyaretci)
//
// Varsayilan RED: yalniz yayindaki yazi adresleri (_yazilar.json), yalniz
// ahmetcelen.com.tr kokeni, yalniz tanimli tur/deger. CORS basligi YOK.
const E = require("./_etkilesim.js");

// Oy ve ifade icin tek betik, ATOMIK: ayni cerezle es zamanli iki istek
// sayaci iki kez artiramaz (Redis betigi bolunmeden calisir).
// KEYS: secim hash'i, sayac hash'i, ag sayaci
// ARGV: ziyaretci, yeni deger ("" = geri al), ag siniri, ag suresi
const SECIM_BETIGI = `
local eski = redis.call('HGET', KEYS[1], ARGV[1])
if not eski then eski = '' end
local yeni = ARGV[2]
if eski == yeni then return {'ayni', eski} end
if eski == '' then
  local n = redis.call('INCR', KEYS[3])
  if n == 1 then redis.call('EXPIRE', KEYS[3], tonumber(ARGV[4])) end
  if n > tonumber(ARGV[3]) then return {'sinir', eski} end
end
if eski ~= '' then redis.call('HINCRBY', KEYS[2], eski, -1) end
if yeni == '' then
  redis.call('HDEL', KEYS[1], ARGV[1])
else
  redis.call('HSET', KEYS[1], ARGV[1], yeni)
  redis.call('HINCRBY', KEYS[2], yeni, 1)
end
return {'tamam', yeni}`;

function cift(ham) {
  // Upstash HGETALL'i duz dizi ([alan, deger, ...]) dondurur.
  const o = {};
  if (Array.isArray(ham)) for (let i = 0; i + 1 < ham.length; i += 2) o[ham[i]] = Number(ham[i + 1]) || 0;
  else if (ham && typeof ham === "object") for (const k of Object.keys(ham)) o[k] = Number(ham[k]) || 0;
  return o;
}

function sayac(ham) {
  const o = cift(ham);
  const ifade = {};
  for (const k of E.IFADELER) ifade[k] = Math.max(0, o["i:" + k] || 0);
  return { oy: { begeni: Math.max(0, o.begeni || 0), begenmeme: Math.max(0, o.begenmeme || 0) }, ifade };
}

function yorumlar(ham) {
  const l = [];
  for (const m of Array.isArray(ham) ? ham : []) {
    try {
      const y = JSON.parse(m);
      if (y && typeof y.metin === "string") l.push({ id: y.id, rumuz: y.rumuz, metin: y.metin, zaman: y.zaman });
    } catch (e) { /* bozuk kayit atlanir */ }
  }
  return l;
}

// Ad/rumuz: harf, rakam, bosluk ve . - _ ' ; yazarin adini baskasi kullanamaz.
const RUMUZ = /^[\p{L}\p{N} .'_-]{2,40}$/u;
const AYRILMIS = new Set(["ahmetcelen", "ahmetçelen", "yonetici", "yönetici", "admin", "moderator", "moderatör"]);
const ayrilmis = (r) => AYRILMIS.has(r.toLocaleLowerCase("tr-TR").replace(/[^\p{L}]/gu, ""));
const BAGLANTI = /https?:\/\/|www\./gi;

const kapali = (res, kod, hata) => { res.setHeader("Cache-Control", "no-store"); return res.status(kod).json({ hata }); };

module.exports = async (req, res) => {
  res.setHeader("X-Content-Type-Options", "nosniff");
  if (req.method === "GET" || req.method === "HEAD") return oku(req, res);
  if (req.method === "POST") return yaz(req, res);
  res.setHeader("Allow", "GET, HEAD, POST");
  return kapali(res, 405, "yontem");
};

async function oku(req, res) {
  const q = req.query || {};
  const g = E.gizli();
  if (q.meydan !== undefined) {
    if (!g || !E.depo()) return kapali(res, 503, "depo-yok");
    res.setHeader("Cache-Control", "no-store");
    return res.status(200).json(E.bulmaca(g));
  }
  const yol = String(q.yol || "");
  if (!E.YOL.test(yol) || !E.YAZILAR.has(yol)) return kapali(res, 400, "adres");
  const d = E.depo();
  // Gizli anahtar yoksa yazma kapali; okuma da acilmaz ki sayfa islemeyen
  // dugmeler gostermesin.
  if (!d || !g) return kapali(res, 503, "depo-yok");
  try {
    const [say, liste] = await E.boru(d, [["HGETALL", "etk:say:" + yol], ["ZRANGE", "etk:onayli:" + yol, "-200", "-1"]]);
    const y = yorumlar(liste);
    // Onbellek YALNIZ Vercel CDN'inde (20 sn). Tarayiciya stale-while-revalidate
    // verilirse sayfayi 60 sn icinde yenileyen okur ESKI yaniti gorur (25.09
    // uctan uca denemede yakalandi: onaylanan yorum yenilemede cikmadi).
    res.setHeader("Cache-Control", "no-cache");
    res.setHeader("Vercel-CDN-Cache-Control", "max-age=20, stale-while-revalidate=60");
    return res.status(200).json(Object.assign(sayac(say), { yorumlar: y }));
  } catch (e) {
    return kapali(res, 502, "depo");
  }
}

async function yaz(req, res) {
  res.setHeader("Cache-Control", "no-store");
  if (!E.kokenUygun(req)) return kapali(res, 403, "koken");
  const d = E.depo();
  const g = E.gizli();
  if (!d || !g) return kapali(res, 503, "depo-yok");
  const b = E.govde(req);
  if (!b) return kapali(res, 400, "govde");
  const yol = String(b.yol || "");
  if (!E.YOL.test(yol) || !E.YAZILAR.has(yol)) return kapali(res, 400, "adres");

  // ── girdi dogrulama (depoya gitmeden) ──
  const tur = b.tur;
  let deger = "", rumuz = "", metin = "";
  if (tur === "oy") {
    deger = b.deger;
    if (!["begeni", "begenmeme", ""].includes(deger)) return kapali(res, 400, "deger");
  } else if (tur === "ifade") {
    deger = b.deger;
    if (typeof deger !== "string" || (deger !== "" && !E.IFADELER.includes(deger))) return kapali(res, 400, "deger");
  } else if (tur === "yorum") {
    rumuz = E.temizMetin(b.rumuz, 2, 40);
    metin = E.temizMetin(b.metin, 3, 1500);
    if (!rumuz || !RUMUZ.test(rumuz) || ayrilmis(rumuz)) return kapali(res, 400, "rumuz");
    if (!metin) return kapali(res, 400, "metin");
    if ((metin.match(BAGLANTI) || []).length > 2) return kapali(res, 400, "baglanti");
  } else if (tur === "geri") {
    metin = E.temizMetin(b.metin, 3, 1000);
    if (!metin) return kapali(res, 400, "metin");
    if ((metin.match(BAGLANTI) || []).length > 2) return kapali(res, 400, "baglanti");
  } else {
    return kapali(res, 400, "tur");
  }
  if (!E.cozumGecerli(g, b.cozum)) return kapali(res, 400, "cozum");

  // Tuzak alan: insan gormez, bot doldurur. Bota basari gibi gorunur,
  // hicbir sey kaydedilmez (bot ogrenip alani atlamasin).
  if (tur === "yorum" && b.web !== undefined && b.web !== "") return res.status(200).json({ tamam: true });

  let vid = E.cerezOku(req, g);
  if (!vid) {
    if (tur === "geri") return kapali(res, 403, "once-oy");
    const c = E.cerezUret(g);
    vid = c.id;
    res.setHeader("Set-Cookie", c.baslik);
  }
  const ag = E.agOzeti(req, g);
  const simdi = Date.now();
  const dilim = Math.floor(simdi / 600000);

  try {
    const [pow, genel] = await E.boru(d, [
      ["SET", "etk:pow:" + b.cozum.meydan, "1", "NX", "EX", "900"],
      ["INCR", `etk:hiz:genel:${ag}:${dilim}`],
      ["EXPIRE", `etk:hiz:genel:${ag}:${dilim}`, "660"],
    ]);
    if (pow !== "OK") return kapali(res, 409, "cozum-kullanildi");
    if (Number(genel) > E.SINIR.GENEL) return kapali(res, 429, "hiz");

    if (tur === "oy" || tur === "ifade") {
      const secimK = (tur === "oy" ? "etk:oy:" : "etk:if:") + yol;
      const alan = tur === "ifade" && deger ? "i:" + deger : deger;
      const [sonuc, say] = await E.boru(d, [
        ["EVAL", SECIM_BETIGI, "3", secimK, "etk:say:" + yol, `etk:yeni:${tur}:${yol}:${ag}`,
          vid, alan, String(E.SINIR.YENI_OY), "86400"],
        ["HGETALL", "etk:say:" + yol],
      ]);
      const durum = sonuc[0];
      const secim = tur === "ifade" ? String(sonuc[1] || "").replace(/^i:/, "") : sonuc[1];
      const govdeS = Object.assign({ secim }, sayac(say));
      if (durum === "sinir") return res.status(429).json(Object.assign({ hata: "sinir" }, govdeS));
      return res.status(200).json(Object.assign({ tamam: true }, govdeS));
    }

    if (tur === "yorum") {
      const saat = Math.floor(simdi / 3600000);
      const [kisi, , agS, , bekleyen] = await E.boru(d, [
        ["INCR", `etk:hiz:yorum:${vid}:${dilim}`], ["EXPIRE", `etk:hiz:yorum:${vid}:${dilim}`, "660"],
        ["INCR", `etk:hiz:yorumag:${ag}:${saat}`], ["EXPIRE", `etk:hiz:yorumag:${ag}:${saat}`, "3660"],
        ["ZCARD", "etk:bekleyen"],
      ]);
      if (Number(kisi) > E.SINIR.YORUM_KISI || Number(agS) > E.SINIR.YORUM_AG) return kapali(res, 429, "hiz");
      if (Number(bekleyen) >= E.SINIR.BEKLEYEN_TAVAN) return kapali(res, 503, "kuyruk-dolu");
      const id = E.crypto.randomBytes(8).toString("hex");
      await E.boru(d, [
        ["HSET", "etk:yorum:" + id, "yol", yol, "rumuz", rumuz, "metin", metin, "zaman", String(simdi), "durum", "bekliyor"],
        ["ZADD", "etk:bekleyen", String(simdi), id],
      ]);
      return res.status(200).json({ tamam: true });
    }

    // tur === "geri": yalniz bu yaziya "faydali degil" demis ziyaretci yazar.
    const [oy, geriS, , toplam] = await E.boru(d, [
      ["HGET", "etk:oy:" + yol, vid],
      ["INCR", `etk:hiz:geri:${yol}:${vid}`], ["EXPIRE", `etk:hiz:geri:${yol}:${vid}`, "86400"],
      ["ZCARD", "etk:geriler"],
    ]);
    if (oy !== "begenmeme") return kapali(res, 403, "once-oy");
    if (Number(geriS) > E.SINIR.GERI_KISI) return kapali(res, 429, "hiz");
    if (Number(toplam) >= E.SINIR.GERI_TAVAN) return kapali(res, 503, "kuyruk-dolu");
    const id = E.crypto.randomBytes(8).toString("hex");
    await E.boru(d, [
      ["HSET", "etk:geri:" + id, "yol", yol, "metin", metin, "zaman", String(simdi)],
      ["ZADD", "etk:geriler", String(simdi), id],
    ]);
    return res.status(200).json({ tamam: true });
  } catch (e) {
    return kapali(res, 502, "depo");
  }
}
