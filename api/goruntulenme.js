// api/goruntulenme.js — blog yazisi goruntulenme sayaci (23.09.2026)
//
// Ahmet: "goruntulenme sayacini vercelde tutsak bilgilerini daha iyi olur."
//
// DEPOLAMA: Vercel panelinden baglanan "Upstash for Redis" (Marketplace,
// ucretsiz katman). Baglaninca Vercel ortam degiskenlerini KENDISI ekler
// (KV_REST_API_URL / KV_REST_API_TOKEN; eski adlandirma UPSTASH_REDIS_REST_*
// da okunur). Bagimlilik YOK: Upstash'in REST arayuzune dogrudan fetch.
//
// GUVENLIK (backend/cyber-security anayasasi):
//  · Varsayilan RED: yalniz YAYINDA olan yazilarin adresi kabul edilir
//    (_yazilar.json, scripts/blog_uygula.py uretir). Baska her adres 400.
//  · Anahtar YALNIZ sunucuda; istemciye hicbir kimlik bilgisi gitmez.
//  · Kapali hata: depolama yoksa 503 doner, istemci sayaci GIZLER --
//    uydurma sayi gosterilmez.
//  · Kisisel veri TOPLANMAZ: IP, cerez, kullanici kimligi saklanmiyor.
//    Bedeli: sayac bilincli sisirilebilir (tekrar ziyaret istemcide gunde
//    bire indiriliyor, sunucuda denetlenmiyor). Bir goruntulenme sayaci
//    icin kabul edildi; "toplanmayan veri en guvenli veridir".
//  · Hata mesaji ic ayrinti sizdirmaz.
//  · CORS basligi YOK: yalniz ayni kokenden cagrilir.
const YAZILAR = new Set(require("./_yazilar.json"));
const YOL = /^\/blog\/[a-z0-9-]{1,80}\/$/;

function depo() {
  const url = process.env.KV_REST_API_URL || process.env.UPSTASH_REDIS_REST_URL;
  const token = process.env.KV_REST_API_TOKEN || process.env.UPSTASH_REDIS_REST_TOKEN;
  return url && token ? { url, token } : null;
}

async function komut(d, dizi) {
  const r = await fetch(d.url, {
    method: "POST",
    headers: { Authorization: `Bearer ${d.token}`, "Content-Type": "application/json" },
    body: JSON.stringify(dizi),
  });
  if (!r.ok) throw new Error("depo " + r.status);
  return (await r.json()).result;
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Content-Type-Options", "nosniff");
  if (req.method !== "GET" && req.method !== "POST") {
    res.setHeader("Allow", "GET, POST");
    return res.status(405).json({ hata: "yontem" });
  }
  const yol = String((req.query && req.query.yol) || "");
  if (!YOL.test(yol) || !YAZILAR.has(yol)) {
    return res.status(400).json({ hata: "adres" });
  }
  const d = depo();
  if (!d) return res.status(503).json({ hata: "depo-yok" });
  const anahtar = "gor:" + yol;
  try {
    const sayi = req.method === "POST"
      ? await komut(d, ["INCR", anahtar])
      : Number(await komut(d, ["GET", anahtar])) || 0;
    return res.status(200).json({ sayi: Number(sayi) || 0 });
  } catch (e) {
    return res.status(502).json({ hata: "depo" });
  }
};
