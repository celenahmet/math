// api/populer.js — blogun en cok okunan yazilari (23.09.2026)
//
// Ahmet: "sag blokta en populer yazilar olsun, 5 tane gozuksun; en populer
// ve en yeni diye degistirilebilsin."
//
// Sayilar api/goruntulenme.js'nin yazdigi "gor:<yol>" anahtarlarindan
// OKUNUR; bu uc nokta hicbir sey yazmaz.
//
// GUVENLIK (api/goruntulenme.js ile ayni ilkeler):
//  · Istemciden GIRDI ALINMAZ: okunan anahtarlar yalniz yayindaki yazilarin
//    listesinden (_yazilar.json) uretilir. Sorgu parametreleri yok sayilir.
//  · Yalniz GET (ve HEAD). Yazma yolu yok.
//  · Kapali hata: depo yoksa 503, depo hatasinda 502; istemci "En populer"
//    sekmesini GIZLER, uydurma siralama gosterilmez.
//  · Anahtar yalniz sunucuda; CORS basligi yok; hata mesaji ic ayrinti
//    sizdirmaz. Kisisel veri yok: yanit yalniz yol + sayi.
//  · CDN onbellegi 5 dk: her ziyaret Redis'e gitmez (ucretsiz katman).
const YAZILAR = require("./_yazilar.json");
const EN_COK = 5;

function depo() {
  const e = process.env;
  if (e.KV_REST_API_URL && e.KV_REST_API_TOKEN) return { url: e.KV_REST_API_URL, token: e.KV_REST_API_TOKEN };
  if (e.UPSTASH_REDIS_REST_URL && e.UPSTASH_REDIS_REST_TOKEN) return { url: e.UPSTASH_REDIS_REST_URL, token: e.UPSTASH_REDIS_REST_TOKEN };
  for (const k of Object.keys(e)) {
    const m = k.match(/^(.*)_REST_API_URL$/);
    if (m && e[m[1] + "_REST_API_TOKEN"]) return { url: e[k], token: e[m[1] + "_REST_API_TOKEN"] };
  }
  return null;
}

module.exports = async (req, res) => {
  res.setHeader("X-Content-Type-Options", "nosniff");
  if (req.method !== "GET" && req.method !== "HEAD") {
    res.setHeader("Allow", "GET, HEAD");
    res.setHeader("Cache-Control", "no-store");
    return res.status(405).json({ hata: "yontem" });
  }
  const d = depo();
  if (!d) {
    res.setHeader("Cache-Control", "no-store");
    return res.status(503).json({ hata: "depo-yok" });
  }
  try {
    const yollar = YAZILAR.slice();
    const r = await fetch(d.url, {
      method: "POST",
      headers: { Authorization: `Bearer ${d.token}`, "Content-Type": "application/json" },
      body: JSON.stringify(["MGET"].concat(yollar.map((y) => "gor:" + y))),
    });
    if (!r.ok) throw new Error("depo " + r.status);
    const sonuc = (await r.json()).result;
    if (!Array.isArray(sonuc) || sonuc.length !== yollar.length) throw new Error("bicim");
    const liste = yollar
      .map((yol, i) => ({ yol, sayi: Number(sonuc[i]) || 0 }))
      .filter((x) => x.sayi > 0 && Number.isSafeInteger(x.sayi))
      .sort((a, b) => b.sayi - a.sayi || (a.yol < b.yol ? -1 : 1))
      .slice(0, EN_COK);
    res.setHeader("Cache-Control", "public, max-age=0, s-maxage=300, stale-while-revalidate=600");
    return res.status(200).json({ yazilar: liste });
  } catch (e) {
    res.setHeader("Cache-Control", "no-store");
    return res.status(502).json({ hata: "depo" });
  }
};
