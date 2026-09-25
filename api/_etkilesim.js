// api/_etkilesim.js — blog etkilesiminin ORTAK cekirdegi (25.09.2026)
//
// Ahmet (25.09): "yazi faydali oldu mu begen, dislike (gercek sayilar
// tutulsun), dislike isaretlerse mesaj birakma gelsin, bu mesajlari biz
// gorebilelim. Yorum: ad soyad ya da rumuz, onaydan sonra gelir. 5 emojili
// ifade. Sayfayi yenileyip emoji birakamayacak; oturum acmadigi halde spam
// korumasi ust duzey olacak."
//
// Alt cizgiyle basladigi icin Vercel bunu fonksiyon olarak YAYINLAMAZ;
// yalniz api/etkilesim.js ve api/yonetim.js tarafindan require edilir.
//
// ── SPAM KORUMASI: uc katman, hicbiri tek basina yetmez ─────────────────
// Oturum acmayan ziyaretcide %100 koruma YOKTUR (cerezi silen, IP degistiren,
// bilgisayar basinda sabirla bekleyen kisi her zaman bir oy daha verebilir).
// Hedef: tekrari ZAHMETLI ve PAHALI yapmak, gercek sayiyi korumak.
//  1) Is kaniti (proof of work): her yazma istegi sunucunun imzaladigi,
//     10 dk gecerli, TEK KULLANIMLIK bir bulmacanin cozumunu tasir.
//     Tarayici ~0,5 sn hesaplar (okur fark etmez); bot icin her oy CPU
//     bedeli demek. Imza sunucuda, cozum tek kullanimlik (Redis SET NX).
//  2) Ziyaretci cerezi: sunucunun HMAC ile imzaladigi rastgele kimlik
//     (HttpOnly, Secure, SameSite=Lax, yalniz /api/). Ayni kimlik ayni
//     yaziya tek oy + tek ifade verir; yenilemek bir sey degistirmez.
//     Cerez YALNIZ ilk etkilesimde verilir: yalniz okuyana cerez yok.
//  3) Ag siniri: ayni IP'den (IPv6'da /64) bir yaziya gunde en cok
//     YENI_OY_SINIRI yeni oy/ifade. Cerezi silen ya da gizli sekme acan
//     burada durur. Bedeli: ayni agdaki (yurt, kampus) okurlar bu siniri
//     paylasir; bilincli denge.
// Genel hiz siniri, yorum/mesaj siniri ve kuyruk tavanlari ek katmandir.
//
// ── KISISEL VERI (toplanmayan veri en guvenli veridir) ──────────────────
//  · IP SAKLANMAZ. Sinir anahtari IP'nin gunluk degisen HMAC ozeti; en cok
//    24 saat yasar, ertesi gun ayni IP baska ozet verir (gunler arasi
//    baglanamaz).
//  · Ziyaretci kimligi rastgeledir, kisiyle baglantisi yoktur.
//  · Yorumda yalniz okurun yazdigi ad/rumuz ve metin tutulur; e-posta YOK.
//  · Hata mesaji ic ayrinti sizdirmaz.
const crypto = require("crypto");

const YAZILAR = new Set(require("./_yazilar.json"));
const IFADELER = require("./_ifadeler.json").map((x) => x[0]);
const YOL = /^\/blog\/[a-z0-9-]{1,80}\/$/;
const KOKENLER = new Set(["https://ahmetcelen.com.tr", "https://www.ahmetcelen.com.tr"]);

const SINIR = {
  YENI_OY: 5,              // ayni ag + ayni yazi + 24 saat: yeni oy (ve ayrica yeni ifade)
  GENEL: 60,               // ayni ag, 10 dk: toplam yazma istegi
  YORUM_KISI: 3,           // ayni ziyaretci, 10 dk
  YORUM_AG: 10,            // ayni ag, 1 saat
  GERI_KISI: 3,            // ayni ziyaretci + ayni yazi, 24 saat
  BEKLEYEN_TAVAN: 500,     // onay bekleyen yorum kuyrugu (depolama tuketme saldirisi)
  GERI_TAVAN: 2000,        // okunmamis geri bildirim kuyrugu
  YONETIM_HATA: 20,        // ayni ag, 15 dk: yanlis yonetim anahtari
};
// Is kaniti zorlugu: 0..UST arasi gizli bir sayi; tarayici ortalama UST/2
// SHA-256 hesaplar. 50.000 ile telefonda ~0,3-1 sn (olculecek, istemci
// cozumu arka planda onceden hazirlar).
const POW_UST = 50000;
const POW_SURE_SN = 600;

function depo() {
  // api/goruntulenme.js ile AYNI arama sirasi (panelde onek degisirse diye).
  const e = process.env;
  if (e.KV_REST_API_URL && e.KV_REST_API_TOKEN) return { url: e.KV_REST_API_URL, token: e.KV_REST_API_TOKEN };
  if (e.UPSTASH_REDIS_REST_URL && e.UPSTASH_REDIS_REST_TOKEN) return { url: e.UPSTASH_REDIS_REST_URL, token: e.UPSTASH_REDIS_REST_TOKEN };
  for (const k of Object.keys(e)) {
    const m = k.match(/^(.*)_REST_API_URL$/);
    if (m && e[m[1] + "_REST_API_TOKEN"]) return { url: e[k], token: e[m[1] + "_REST_API_TOKEN"] };
  }
  return null;
}

// Gizli anahtar yoksa ya da kisaysa ozellik KAPALI (kapali hata): imzasiz
// cerez ve bulmaca, korumasiz sayac demek.
function gizli() {
  const g = process.env.ETKILESIM_GIZLI || "";
  return g.length >= 32 ? g : null;
}

async function boru(d, komutlar) {
  const r = await fetch(d.url.replace(/\/+$/, "") + "/pipeline", {
    method: "POST",
    headers: { Authorization: `Bearer ${d.token}`, "Content-Type": "application/json" },
    body: JSON.stringify(komutlar),
  });
  if (!r.ok) throw new Error("depo " + r.status);
  const j = await r.json();
  return j.map((x) => {
    if (x && x.error) throw new Error("depo komut");
    return x.result;
  });
}

const hmac = (g, metin) => crypto.createHmac("sha256", g).update(metin).digest();
const b64 = (buf) => buf.toString("base64url");
const sha256hex = (metin) => crypto.createHash("sha256").update(metin).digest("hex");

function esit(a, b) {
  // Sabit sureli karsilastirma; uzunluk farki da sizmasin diye once ozet.
  const x = crypto.createHash("sha256").update(String(a)).digest();
  const y = crypto.createHash("sha256").update(String(b)).digest();
  return crypto.timingSafeEqual(x, y);
}

// ── is kaniti ───────────────────────────────────────────────────────────
function bulmaca(g, simdi = Date.now()) {
  const son = Math.floor(simdi / 1000) + POW_SURE_SN;
  const tuz = crypto.randomBytes(12).toString("hex") + "?s=" + son;
  const sayi = crypto.randomInt(0, POW_UST + 1);
  const meydan = sha256hex(tuz + sayi);
  return { algoritma: "SHA-256", tuz, meydan, ust: POW_UST, imza: b64(hmac(g, "pow:" + meydan)) };
}

// Imza, sure ve cozum denetlenir; TEK KULLANIM depo tarafinda (SET NX).
function cozumGecerli(g, c, simdi = Date.now()) {
  if (!c || typeof c !== "object") return false;
  const { tuz, meydan, imza, sayi } = c;
  if (typeof tuz !== "string" || typeof meydan !== "string" || typeof imza !== "string") return false;
  if (!/^[0-9a-f]{24}\?s=\d{10}$/.test(tuz) || !/^[0-9a-f]{64}$/.test(meydan)) return false;
  if (!Number.isInteger(sayi) || sayi < 0 || sayi > POW_UST) return false;
  if (!esit(imza, b64(hmac(g, "pow:" + meydan)))) return false;
  if (Number(tuz.slice(tuz.indexOf("?s=") + 3)) * 1000 < simdi) return false;
  return sha256hex(tuz + sayi) === meydan;
}

// ── ziyaretci cerezi ────────────────────────────────────────────────────
const CEREZ = "etk";
function cerezOku(req, g) {
  const ham = String((req.headers && req.headers.cookie) || "");
  const m = ham.match(/(?:^|;\s*)etk=([A-Za-z0-9_-]{22})\.([A-Za-z0-9_-]{22})(?:;|$)/);
  if (!m) return null;
  return esit(m[2], b64(hmac(g, "ziyaretci:" + m[1])).slice(0, 22)) ? m[1] : null;
}
function cerezUret(g) {
  const id = b64(crypto.randomBytes(16));
  const deger = id + "." + b64(hmac(g, "ziyaretci:" + id)).slice(0, 22);
  return { id, baslik: `${CEREZ}=${deger}; Path=/api/; Max-Age=31536000; HttpOnly; Secure; SameSite=Lax` };
}

// ── ag ozeti ────────────────────────────────────────────────────────────
function ip(req) {
  const h = req.headers || {};
  // Vercel x-real-ip ve x-forwarded-for'u KENDISI yazar (istemcinin
  // gonderdigini ezer); ilk deger gercek istemci adresidir.
  const ham = String(h["x-real-ip"] || String(h["x-forwarded-for"] || "").split(",")[0] || (req.socket && req.socket.remoteAddress) || "").trim();
  if (ham.includes(":")) return ham.split(":").slice(0, 4).join(":");   // IPv6 /64
  return ham || "bilinmiyor";
}
function agOzeti(req, g, simdi = Date.now()) {
  const gun = new Date(simdi).toISOString().slice(0, 10);
  return b64(hmac(g, "ag:" + gun + ":" + ip(req))).slice(0, 16);
}

function kokenUygun(req) {
  const o = String((req.headers && req.headers.origin) || "");
  return KOKENLER.has(o);
}

function govde(req) {
  let b = req.body;
  if (typeof b === "string") {
    if (b.length > 8000) return null;
    try { b = JSON.parse(b); } catch (e) { return null; }
  }
  return b && typeof b === "object" && !Array.isArray(b) ? b : null;
}

// Kontrol karakterleri atilir, satir sonu korunur, bos satirlar ikiye iner.
function temizMetin(m, en, boy) {
  if (typeof m !== "string") return null;
  const t = m.replace(/\r\n?/g, "\n").replace(/[\u0000-\u0009\u000B-\u001F\u007F​-‏‪-‮⁦-⁩]/g, "")
    .replace(/\n{3,}/g, "\n\n").trim();
  return t.length >= en && t.length <= boy ? t : null;
}

module.exports = {
  crypto, YAZILAR, IFADELER, YOL, SINIR, POW_UST, CEREZ,
  depo, gizli, boru, esit, bulmaca, cozumGecerli, cerezOku, cerezUret, agOzeti, kokenUygun, govde, temizMetin,
};
