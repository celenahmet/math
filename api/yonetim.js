// api/yonetim.js — blog yorum onayi ve geri bildirim okuma (25.09.2026)
//
// Ahmet (25.09): "dislike isaretlerse mesaj birakma gelsin, bu mesajlari
// bizde gorebilelim" + "yorum icerigi onaydan sonra gelir".
//
//   GET                         bekleyen yorumlar, son onaylilar, geri bildirimler, yazi ozeti
//   POST { islem, id }          onayla | sil (yorum) | geri-sil (geri bildirim)
//
// YETKI: "Authorization: Bearer <YONETIM_ANAHTARI>". Anahtar Vercel ortam
// degiskeninde; sayfada ya da depoda YOK. Yoksa ya da kisaysa uc KAPALI.
// Karsilastirma sabit sureli; yanlis anahtar ayni agdan 15 dk'da 20 kez
// denenince 429. Yanitlar onbelleksiz ve dizinlenmez.
const E = require("./_etkilesim.js");

const ID = /^[0-9a-f]{16}$/;
const kapali = (res, kod, hata) => res.status(kod).json({ hata });

function nesne(ham) {
  const o = {};
  if (Array.isArray(ham)) for (let i = 0; i + 1 < ham.length; i += 2) o[ham[i]] = ham[i + 1];
  else if (ham && typeof ham === "object") Object.assign(o, ham);
  return o;
}

async function yetkili(req, res, d, g) {
  const anahtar = process.env.YONETIM_ANAHTARI || "";
  if (anahtar.length < 32) { kapali(res, 503, "yapilandirma"); return false; }
  const h = String((req.headers && req.headers.authorization) || "");
  const verilen = h.startsWith("Bearer ") ? h.slice(7) : "";
  if (verilen && E.esit(verilen, anahtar)) return true;
  const ag = E.agOzeti(req, g);
  const k = `etk:hiz:yonetim:${ag}:${Math.floor(Date.now() / 900000)}`;
  try {
    const [n] = await E.boru(d, [["INCR", k], ["EXPIRE", k, "960"]]);
    if (Number(n) > E.SINIR.YONETIM_HATA) { kapali(res, 429, "hiz"); return false; }
  } catch (e) { /* sayac yazilamasa da yetki verilmez */ }
  kapali(res, 401, "yetki");
  return false;
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("X-Robots-Tag", "noindex, nofollow");
  if (req.method !== "GET" && req.method !== "POST") {
    res.setHeader("Allow", "GET, POST");
    return kapali(res, 405, "yontem");
  }
  const d = E.depo();
  const g = E.gizli();
  if (!d || !g) return kapali(res, 503, "depo-yok");
  if (!(await yetkili(req, res, d, g))) return;

  try {
    if (req.method === "GET") return await liste(res, d);
    const b = E.govde(req);
    if (!b || !ID.test(String(b.id || ""))) return kapali(res, 400, "id");
    const id = b.id;
    if (b.islem === "onayla" || b.islem === "sil") {
      const [ham] = await E.boru(d, [["HGETALL", "etk:yorum:" + id]]);
      const y = nesne(ham);
      if (!y.yol) return kapali(res, 404, "yok");
      if (b.islem === "onayla") {
        if (y.durum !== "bekliyor") return kapali(res, 409, "durum");
        const uye = JSON.stringify({ id, rumuz: y.rumuz, metin: y.metin, zaman: Number(y.zaman) });
        await E.boru(d, [
          ["ZADD", "etk:onayli:" + y.yol, String(y.zaman), uye],
          ["ZADD", "etk:onaylilar", String(y.zaman), id],
          ["HSET", "etk:yorum:" + id, "durum", "onayli", "uye", uye],
          ["ZREM", "etk:bekleyen", id],
        ]);
        return res.status(200).json({ tamam: true });
      }
      const k = [["ZREM", "etk:bekleyen", id], ["ZREM", "etk:onaylilar", id], ["DEL", "etk:yorum:" + id]];
      if (y.uye) k.unshift(["ZREM", "etk:onayli:" + y.yol, y.uye]);
      await E.boru(d, k);
      return res.status(200).json({ tamam: true });
    }
    if (b.islem === "geri-sil") {
      await E.boru(d, [["ZREM", "etk:geriler", id], ["DEL", "etk:geri:" + id]]);
      return res.status(200).json({ tamam: true });
    }
    return kapali(res, 400, "islem");
  } catch (e) {
    return kapali(res, 502, "depo");
  }
};

async function liste(res, d) {
  const [bekleyenId, onayliId, geriId] = await E.boru(d, [
    ["ZRANGE", "etk:bekleyen", "0", "199"],
    ["ZRANGE", "etk:onaylilar", "-100", "-1"],
    ["ZRANGE", "etk:geriler", "-200", "-1"],
  ]);
  const yollar = [...E.YAZILAR];
  const komut = [
    ...bekleyenId.map((id) => ["HGETALL", "etk:yorum:" + id]),
    ...onayliId.map((id) => ["HGETALL", "etk:yorum:" + id]),
    ...geriId.map((id) => ["HGETALL", "etk:geri:" + id]),
    ...yollar.map((y) => ["HGETALL", "etk:say:" + y]),
    ...yollar.map((y) => ["ZCARD", "etk:onayli:" + y]),
  ];
  const r = komut.length ? await E.boru(d, komut) : [];
  let i = 0;
  const al = (idler) => idler.map((id) => Object.assign({ id }, nesne(r[i++]))).filter((x) => x.yol);
  const bekleyen = al(bekleyenId);
  const onayli = al(onayliId).reverse();
  const geri = al(geriId).reverse();
  const sayilar = yollar.map(() => nesne(r[i++]));
  const yorumSay = yollar.map(() => Number(r[i++]) || 0);
  const ozet = yollar.map((yol, j) => {
    const s = sayilar[j];
    const ifade = {};
    for (const k of E.IFADELER) ifade[k] = Math.max(0, Number(s["i:" + k]) || 0);
    return { yol, begeni: Math.max(0, Number(s.begeni) || 0), begenmeme: Math.max(0, Number(s.begenmeme) || 0), ifade, yorum: yorumSay[j] };
  }).filter((x) => x.begeni || x.begenmeme || x.yorum || Object.values(x.ifade).some(Boolean));
  const temiz = (x) => ({ id: x.id, yol: x.yol, rumuz: x.rumuz, metin: x.metin, zaman: Number(x.zaman) || 0 });
  return res.status(200).json({
    bekleyen: bekleyen.map(temiz),
    onayli: onayli.map(temiz),
    geri: geri.map((x) => ({ id: x.id, yol: x.yol, metin: x.metin, zaman: Number(x.zaman) || 0 })),
    ozet,
    ifadeler: require("./_ifadeler.json"),   // [anahtar, emoji, ad]: sayfa ikinci liste tutmasin
  });
}
