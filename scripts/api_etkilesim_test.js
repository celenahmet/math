// scripts/api_etkilesim_test.js — api/etkilesim.js + api/yonetim.js icin
// mutlu yol + SALDIRGAN testler (25.09.2026).
//
// Taklit degil GERCEK Redis: Lua betigi (atomik oy) ancak gercek depoda
// sinanir. Upstash'in REST arayuzunu taklit eden yerel vekil gerekir:
//   docker network create etk-test
//   docker run -d --rm --name etk-redis --network etk-test redis:7-alpine
//   docker run -d --rm --name etk-srh --network etk-test -p 8079:80 \
//     -e SRH_MODE=env -e SRH_TOKEN=yerel-test-token \
//     -e SRH_CONNECTION_STRING=redis://etk-redis:6379 hiett/serverless-redis-http
// Calistirma: node scripts/api_etkilesim_test.js
//
// ⚠️ Her test grubu depoyu SIFIRLAR (FLUSHDB). Canli depoya asla baglanmasin
// diye adres localhost degilse test HIC calismaz.
const assert = require("assert");
const crypto = require("crypto");
const path = require("path");

const DEPO = process.env.ETK_TEST_DEPO || "http://localhost:8079";
const TOKEN = process.env.ETK_TEST_TOKEN || "yerel-test-token";
if (!/^http:\/\/(localhost|127\.0\.0\.1):\d+$/.test(DEPO)) {
  console.error("DUR: test deposu yerel degil (" + DEPO + "). FLUSHDB canli veriyi silerdi.");
  process.exit(2);
}
for (const k of Object.keys(process.env)) if (/REST_API|UPSTASH|ETKILESIM|YONETIM/.test(k)) delete process.env[k];
const ENV = {
  KV_REST_API_URL: DEPO, KV_REST_API_TOKEN: TOKEN,
  ETKILESIM_GIZLI: "t".repeat(40) + "-yerel-test-gizli",
  YONETIM_ANAHTARI: "y".repeat(40) + "-yerel-yonetim",
};
Object.assign(process.env, ENV);

const API = path.join(__dirname, "../api");
const etk = require(path.join(API, "etkilesim.js"));
const yon = require(path.join(API, "yonetim.js"));
const YAZILAR = require(path.join(API, "_yazilar.json"));
const IFADELER = require(path.join(API, "_ifadeler.json")).map((x) => x[0]);
const YOL = YAZILAR[0], YOL2 = YAZILAR[1];
const KOKEN = "https://ahmetcelen.com.tr";

async function redis(...k) {
  const r = await fetch(DEPO, { method: "POST", headers: { Authorization: "Bearer " + TOKEN, "Content-Type": "application/json" }, body: JSON.stringify(k) });
  return (await r.json()).result;
}
const sifirla = () => redis("FLUSHDB");

function yanit() {
  const r = { kod: 0, govde: null, baslik: {} };
  r.setHeader = (k, v) => { r.baslik[k.toLowerCase()] = v; };
  r.status = (k) => { r.kod = k; return r; };
  r.json = (g) => { r.govde = g; return r; };
  return r;
}
async function cagir(fn, { method = "GET", query = {}, headers = {}, body, ip = "203.0.113.7" } = {}) {
  const res = yanit();
  await fn({ method, query, headers: Object.assign({ "x-real-ip": ip }, headers), body, socket: {} }, res);
  return res;
}

// Tarayicinin yaptigini yapar: bulmacayi al, sayiyi bul.
async function coz() {
  const r = await cagir(etk, { query: { meydan: "1" } });
  assert.strictEqual(r.kod, 200);
  const { tuz, meydan, imza, ust } = r.govde;
  for (let n = 0; n <= ust; n++) {
    if (crypto.createHash("sha256").update(tuz + n).digest("hex") === meydan) return { tuz, meydan, imza, sayi: n };
  }
  throw new Error("cozum yok");
}
const cerezDegeri = (res) => {
  const c = res.baslik["set-cookie"];
  return c ? c.split(";")[0] : null;
};
async function gonder(body, { cerez, ip, koken = KOKEN, cozum } = {}) {
  const b = Object.assign({ yol: YOL }, body);
  if (!("cozum" in body)) b.cozum = cozum || (await coz());
  const headers = { origin: koken };
  if (cerez) headers.cookie = cerez;
  return cagir(etk, { method: "POST", headers, body: b, ip });
}
const okuSayac = async (yol = YOL) => (await cagir(etk, { query: { yol } })).govde;
const YETKI = { authorization: "Bearer " + ENV.YONETIM_ANAHTARI };

let n = 0;
const test = async (ad, fn) => { await sifirla(); await fn(); n++; console.log("ok  " + ad); };

(async () => {
  // ── yapilandirma ve kapali hata ──
  await test("depo yoksa GET ve POST 503, yonetim 503", async () => {
    const eski = process.env.KV_REST_API_URL;
    delete process.env.KV_REST_API_URL;
    assert.strictEqual((await cagir(etk, { query: { yol: YOL } })).kod, 503);
    assert.strictEqual((await cagir(etk, { query: { meydan: "1" } })).kod, 503);
    assert.strictEqual((await cagir(etk, { method: "POST", headers: { origin: KOKEN }, body: {} })).kod, 503);
    assert.strictEqual((await cagir(yon, { headers: YETKI })).kod, 503);
    process.env.KV_REST_API_URL = eski;
  });
  await test("gizli anahtar yok ya da kisa: ozellik kapali (503)", async () => {
    const eski = process.env.ETKILESIM_GIZLI;
    process.env.ETKILESIM_GIZLI = "kisa";
    assert.strictEqual((await cagir(etk, { query: { yol: YOL } })).kod, 503);
    assert.strictEqual((await cagir(etk, { query: { meydan: "1" } })).kod, 503);
    process.env.ETKILESIM_GIZLI = eski;
  });
  await test("yonetim anahtari kisa: yonetim kapali (503), dogru anahtarla bile", async () => {
    const eski = process.env.YONETIM_ANAHTARI;
    process.env.YONETIM_ANAHTARI = "kisa-anahtar";
    assert.strictEqual((await cagir(yon, { headers: { authorization: "Bearer kisa-anahtar" } })).kod, 503);
    process.env.YONETIM_ANAHTARI = eski;
  });

  // ── okuma ──
  await test("GET bos yazi: sifir sayilar, bos yorum, CDN onbellegi, cerez YOK", async () => {
    const r = await cagir(etk, { query: { yol: YOL } });
    assert.strictEqual(r.kod, 200);
    assert.deepStrictEqual(r.govde.oy, { begeni: 0, begenmeme: 0 });
    assert.deepStrictEqual(Object.keys(r.govde.ifade), IFADELER);
    assert.deepStrictEqual(r.govde.yorumlar, []);
    assert.strictEqual(r.baslik["cache-control"], "no-cache", "tarayici her seferinde dogrular");
    assert.match(r.baslik["vercel-cdn-cache-control"], /max-age=20/);
    assert.strictEqual(r.baslik["set-cookie"], undefined);
  });
  await test("GET yayinda olmayan / bicimsiz adres 400", async () => {
    for (const yol of ["/blog/yok-boyle-yazi/", "/blog/../api/", "/", "", "/blog/Limit/"]) {
      assert.strictEqual((await cagir(etk, { query: { yol } })).kod, 400, yol);
    }
  });
  await test("bulmaca onbelleksiz, her seferinde farkli", async () => {
    const a = await cagir(etk, { query: { meydan: "1" } }), b = await cagir(etk, { query: { meydan: "1" } });
    assert.strictEqual(a.baslik["cache-control"], "no-store");
    assert.notStrictEqual(a.govde.meydan, b.govde.meydan);
  });
  await test("PUT/DELETE 405", async () => {
    assert.strictEqual((await cagir(etk, { method: "PUT" })).kod, 405);
    assert.strictEqual((await cagir(yon, { method: "DELETE", headers: YETKI })).kod, 405);
  });

  // ── oy: mutlu yol ──
  await test("oy: begeni -> cerez verilir, sayac 1; ayni cerezle tekrar -> hala 1", async () => {
    const r = await gonder({ tur: "oy", deger: "begeni" });
    assert.strictEqual(r.kod, 200);
    assert.strictEqual(r.govde.secim, "begeni");
    assert.strictEqual(r.govde.oy.begeni, 1);
    const c = cerezDegeri(r);
    assert.ok(c && /^etk=/.test(c));
    assert.match(r.baslik["set-cookie"], /HttpOnly/);
    assert.match(r.baslik["set-cookie"], /Secure/);
    assert.match(r.baslik["set-cookie"], /SameSite=Lax/);
    assert.match(r.baslik["set-cookie"], /Path=\/api\//);
    const r2 = await gonder({ tur: "oy", deger: "begeni" }, { cerez: c });
    assert.strictEqual(r2.kod, 200);
    assert.strictEqual(r2.govde.oy.begeni, 1);
    assert.strictEqual(r2.baslik["set-cookie"], undefined, "gecerli cerezde yeni cerez verilmez");
    assert.strictEqual((await okuSayac()).oy.begeni, 1);
  });
  await test("oy: fikir degistirme ve geri alma sayaci dogru tasir", async () => {
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begeni" }));
    let r = await gonder({ tur: "oy", deger: "begenmeme" }, { cerez: c });
    assert.deepStrictEqual(r.govde.oy, { begeni: 0, begenmeme: 1 });
    r = await gonder({ tur: "oy", deger: "" }, { cerez: c });
    assert.deepStrictEqual(r.govde.oy, { begeni: 0, begenmeme: 0 });
    assert.strictEqual(r.govde.secim, "");
  });
  await test("oy: yazilar birbirinden bagimsiz", async () => {
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begeni" }));
    await gonder({ yol: YOL2, tur: "oy", deger: "begenmeme" }, { cerez: c });
    assert.strictEqual((await okuSayac(YOL)).oy.begeni, 1);
    assert.strictEqual((await okuSayac(YOL2)).oy.begenmeme, 1);
  });

  // ── ifade ──
  await test("ifade: tek secim, degistirme tasir, oydan bagimsiz", async () => {
    const c = cerezDegeri(await gonder({ tur: "ifade", deger: IFADELER[0] }));
    let s = await okuSayac();
    assert.strictEqual(s.ifade[IFADELER[0]], 1);
    const r = await gonder({ tur: "ifade", deger: IFADELER[2] }, { cerez: c });
    assert.strictEqual(r.govde.secim, IFADELER[2]);
    assert.strictEqual(r.govde.ifade[IFADELER[0]], 0);
    assert.strictEqual(r.govde.ifade[IFADELER[2]], 1);
    await gonder({ tur: "oy", deger: "begeni" }, { cerez: c });
    s = await okuSayac();
    assert.strictEqual(s.oy.begeni, 1);
    assert.strictEqual(s.ifade[IFADELER[2]], 1);
  });

  // ── saldirgan: girdi ──
  await test("koken yok / yabanci koken 403, depoya dokunmaz", async () => {
    for (const koken of ["", "https://kotu.example", "https://ahmetcelen.com.tr.kotu.example", "http://ahmetcelen.com.tr"]) {
      const r = await cagir(etk, { method: "POST", headers: koken ? { origin: koken } : {}, body: { yol: YOL, tur: "oy", deger: "begeni" } });
      assert.strictEqual(r.kod, 403, koken);
    }
    assert.strictEqual(await redis("DBSIZE"), 0);
  });
  await test("gecersiz tur / deger / ifade / nesne deger 400", async () => {
    const cozum = await coz();
    for (const b of [{ tur: "sil" }, { tur: "oy", deger: "super" }, { tur: "oy", deger: { $gt: "" } },
      { tur: "ifade", deger: "yildiz" }, { tur: "ifade", deger: ["sevdim"] }, { tur: "oy" }]) {
      assert.strictEqual((await gonder(Object.assign({ cozum }, b))).kod, 400, JSON.stringify(b));
    }
  });
  await test("govde bozuk / dizi / dev 400", async () => {
    for (const body of ["{bozuk", "[1,2]", JSON.stringify({ tur: "x".repeat(9000) })]) {
      assert.strictEqual((await cagir(etk, { method: "POST", headers: { origin: KOKEN }, body })).kod, 400);
    }
  });

  // ── saldirgan: is kaniti ──
  await test("cozum yok / yanlis sayi / sahte imza / kurcalanmis tuz 400", async () => {
    const c = await coz();
    const kotu = [undefined, null, "x", Object.assign({}, c, { sayi: (c.sayi + 1) % 50001 }),
      Object.assign({}, c, { imza: "A".repeat(43) }), Object.assign({}, c, { sayi: -1 }), Object.assign({}, c, { sayi: 1.5 }),
      Object.assign({}, c, { tuz: c.tuz.replace(/\?s=\d+/, "?s=9999999999") })];
    for (const cozum of kotu) {
      assert.strictEqual((await gonder({ tur: "oy", deger: "begeni", cozum })).kod, 400, JSON.stringify(cozum));
    }
    assert.strictEqual((await okuSayac()).oy.begeni, 0);
  });
  await test("suresi gecmis cozum 400", async () => {
    const E = require(path.join(API, "_etkilesim.js"));
    const b = E.bulmaca(ENV.ETKILESIM_GIZLI, Date.now() - 11 * 60 * 1000);
    let sayi = 0;
    while (crypto.createHash("sha256").update(b.tuz + sayi).digest("hex") !== b.meydan) sayi++;
    const r = await gonder({ tur: "oy", deger: "begeni", cozum: { tuz: b.tuz, meydan: b.meydan, imza: b.imza, sayi } });
    assert.strictEqual(r.kod, 400);
  });
  await test("ayni cozum ikinci kez kullanilamaz (409)", async () => {
    const cozum = await coz();
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni", cozum })).kod, 200);
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni", cozum })).kod, 409);
    assert.strictEqual((await okuSayac()).oy.begeni, 1);
  });

  // ── saldirgan: cerez ve ag ──
  await test("sahte cerez tanınmaz: yeni kimlik verilir (eskisi ezilemez)", async () => {
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begeni" }));
    const sahte = c.slice(0, -3) + (c.endsWith("AAA") ? "BBB" : "AAA");
    const r = await gonder({ tur: "oy", deger: "begenmeme" }, { cerez: sahte });
    assert.ok(cerezDegeri(r) && cerezDegeri(r) !== c);
    assert.deepStrictEqual((await okuSayac()).oy, { begeni: 1, begenmeme: 1 });
  });
  await test("cerez silip tekrar: ayni agdan bir yaziya gunde en cok 5 yeni oy (6. 429), baska ag gecer", async () => {
    for (let i = 0; i < 5; i++) assert.strictEqual((await gonder({ tur: "oy", deger: "begeni" })).kod, 200);
    const r = await gonder({ tur: "oy", deger: "begeni" });
    assert.strictEqual(r.kod, 429);
    assert.strictEqual(r.govde.hata, "sinir");
    assert.strictEqual(r.govde.oy.begeni, 5);
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni" }, { ip: "198.51.100.9" })).kod, 200);
    assert.strictEqual((await gonder({ yol: YOL2, tur: "oy", deger: "begeni" })).kod, 200, "sinir yazi basina");
    assert.strictEqual((await okuSayac()).oy.begeni, 6);
  });
  await test("sinir dolunca mevcut oy degistirilebilir (yeni oy degil)", async () => {
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begeni" }));
    for (let i = 0; i < 4; i++) await gonder({ tur: "oy", deger: "begeni" });
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni" })).kod, 429);
    assert.strictEqual((await gonder({ tur: "oy", deger: "begenmeme" }, { cerez: c })).kod, 200);
  });
  await test("IPv6: ayni /64 icindeki farkli adresler ayni ag sayilir", async () => {
    for (let i = 0; i < 5; i++) await gonder({ tur: "oy", deger: "begeni" }, { ip: `2001:db8:1:2::${i + 1}` });
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni" }, { ip: "2001:db8:1:2::ff" })).kod, 429);
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni" }, { ip: "2001:db8:1:3::1" })).kod, 200);
  });
  await test("ATOMIKLIK: ayni cerezle es zamanli 8 ilk oy -> sayac tam 1", async () => {
    const ilk = await gonder({ tur: "ifade", deger: IFADELER[1] });
    const c = cerezDegeri(ilk);
    await sifirla();
    const cozumler = [];
    for (let i = 0; i < 8; i++) cozumler.push(await coz());
    const r = await Promise.all(cozumler.map((cozum) => gonder({ tur: "oy", deger: "begeni", cozum }, { cerez: c })));
    assert.ok(r.every((x) => x.kod === 200));
    assert.strictEqual((await okuSayac()).oy.begeni, 1);
  });
  await test("genel hiz siniri: ayni agdan 10 dk'da 60 ustu yazma 429", async () => {
    await redis("SET", "x", "1");
    const E = require(path.join(API, "_etkilesim.js"));
    const ag = E.agOzeti({ headers: { "x-real-ip": "203.0.113.7" } }, ENV.ETKILESIM_GIZLI);
    await redis("SET", `etk:hiz:genel:${ag}:${Math.floor(Date.now() / 600000)}`, "60");
    assert.strictEqual((await gonder({ tur: "oy", deger: "begeni" })).kod, 429);
  });

  // ── yorum ──
  await test("yorum: onaya duser, onaydan once GORUNMEZ, onaylaninca gorunur", async () => {
    const r = await gonder({ tur: "yorum", rumuz: "Deniz K.", metin: "Limit anlatimi cok acikti.\n\n\n\nTesekkurler", web: "" });
    assert.strictEqual(r.kod, 200);
    assert.deepStrictEqual((await okuSayac()).yorumlar, []);
    const l = await cagir(yon, { headers: YETKI });
    assert.strictEqual(l.kod, 200);
    assert.strictEqual(l.govde.bekleyen.length, 1);
    const y = l.govde.bekleyen[0];
    assert.strictEqual(y.metin, "Limit anlatimi cok acikti.\n\nTesekkurler", "bos satirlar ikiye iner");
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "onayla", id: y.id } })).kod, 200);
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "onayla", id: y.id } })).kod, 409);
    const s = await okuSayac();
    assert.strictEqual(s.yorumlar.length, 1);
    assert.strictEqual(s.yorumlar[0].rumuz, "Deniz K.");
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "sil", id: y.id } })).kod, 200);
    assert.deepStrictEqual((await okuSayac()).yorumlar, []);
    assert.strictEqual((await cagir(yon, { headers: YETKI })).govde.onayli.length, 0);
  });
  await test("yorum: betik iceren metin DEGISMEDEN saklanir (sayfa textContent ile basar)", async () => {
    const kotu = "<img src=x onerror=alert(1)><script>alert(2)</script>";
    await gonder({ tur: "yorum", rumuz: "Test", metin: kotu });
    const y = (await cagir(yon, { headers: YETKI })).govde.bekleyen[0];
    assert.strictEqual(y.metin, kotu);
  });
  await test("yorum: tuzak alan dolu -> 200 ama HICBIR SEY kaydedilmez", async () => {
    const r = await gonder({ tur: "yorum", rumuz: "Bot", metin: "ucuz takipci", web: "http://spam.example" });
    assert.strictEqual(r.kod, 200);
    assert.strictEqual((await cagir(yon, { headers: YETKI })).govde.bekleyen.length, 0);
  });
  await test("yorum: gecersiz rumuz / metin / ayrilmis ad / cok baglanti 400", async () => {
    const cozum = await coz();
    const kotu = [{ rumuz: "", metin: "merhaba" }, { rumuz: "a", metin: "merhaba" }, { rumuz: "x".repeat(41), metin: "merhaba" },
      { rumuz: "<b>ad</b>", metin: "merhaba" }, { rumuz: "Ahmet Çelen", metin: "merhaba" }, { rumuz: "ahmet celen", metin: "merhaba" },
      { rumuz: "Yönetici", metin: "merhaba" }, { rumuz: "Deniz", metin: "ab" }, { rumuz: "Deniz", metin: "x".repeat(1501) },
      { rumuz: "Deniz", metin: "http://a.example http://b.example www.c.example" }, { rumuz: 5, metin: "merhaba" }];
    for (const b of kotu) assert.strictEqual((await gonder(Object.assign({ tur: "yorum", cozum }, b))).kod, 400, JSON.stringify(b));
  });
  await test("yorum: ayni kisi 10 dk'da 3'ten fazla yazamaz (429)", async () => {
    const c = cerezDegeri(await gonder({ tur: "yorum", rumuz: "Deniz", metin: "birinci" }));
    assert.strictEqual((await gonder({ tur: "yorum", rumuz: "Deniz", metin: "ikinci" }, { cerez: c })).kod, 200);
    assert.strictEqual((await gonder({ tur: "yorum", rumuz: "Deniz", metin: "ucuncu" }, { cerez: c })).kod, 200);
    assert.strictEqual((await gonder({ tur: "yorum", rumuz: "Deniz", metin: "dorduncu" }, { cerez: c })).kod, 429);
  });
  await test("yorum: kuyruk tavanda 503 (depolama tuketme)", async () => {
    const k = [];
    for (let i = 0; i < 500; i++) k.push(String(i), "id" + i);
    await redis("ZADD", "etk:bekleyen", ...k);
    assert.strictEqual((await gonder({ tur: "yorum", rumuz: "Deniz", metin: "merhaba" })).kod, 503);
  });

  // ── geri bildirim ──
  await test("geri: yalniz 'faydali degil' diyen yazabilir; cerezsiz 403", async () => {
    assert.strictEqual((await gonder({ tur: "geri", metin: "ornek eksik" })).kod, 403);
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begeni" }));
    assert.strictEqual((await gonder({ tur: "geri", metin: "ornek eksik" }, { cerez: c })).kod, 403);
    await gonder({ tur: "oy", deger: "begenmeme" }, { cerez: c });
    assert.strictEqual((await gonder({ yol: YOL2, tur: "geri", metin: "ornek eksik" }, { cerez: c })).kod, 403, "baska yazi");
    assert.strictEqual((await gonder({ tur: "geri", metin: "ornek eksik" }, { cerez: c })).kod, 200);
    const l = (await cagir(yon, { headers: YETKI })).govde;
    assert.strictEqual(l.geri.length, 1);
    assert.strictEqual(l.geri[0].yol, YOL);
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "geri-sil", id: l.geri[0].id } })).kod, 200);
    assert.strictEqual((await cagir(yon, { headers: YETKI })).govde.geri.length, 0);
  });
  await test("geri: kisi + yazi basina gunde 3", async () => {
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begenmeme" }));
    for (let i = 0; i < 3; i++) assert.strictEqual((await gonder({ tur: "geri", metin: "mesaj " + i }, { cerez: c })).kod, 200);
    assert.strictEqual((await gonder({ tur: "geri", metin: "mesaj 4" }, { cerez: c })).kod, 429);
  });

  // ── yonetim ──
  await test("yonetim: anahtarsiz / yanlis / Bearer'siz 401, noindex, onbelleksiz", async () => {
    for (const h of [{}, { authorization: "Bearer yanlis" }, { authorization: ENV.YONETIM_ANAHTARI }, { authorization: "Bearer " + ENV.YONETIM_ANAHTARI + "x" }]) {
      const r = await cagir(yon, { headers: h });
      assert.strictEqual(r.kod, 401, JSON.stringify(h));
      assert.strictEqual(r.baslik["cache-control"], "no-store");
      assert.match(r.baslik["x-robots-tag"], /noindex/);
    }
  });
  await test("yonetim: kaba kuvvet 20 yanlistan sonra 429, dogru anahtar baska agdan calisir", async () => {
    for (let i = 0; i < 20; i++) assert.strictEqual((await cagir(yon, { headers: { authorization: "Bearer yanlis" + i } })).kod, 401);
    assert.strictEqual((await cagir(yon, { headers: { authorization: "Bearer yanlis" } })).kod, 429);
    assert.strictEqual((await cagir(yon, { headers: YETKI, ip: "198.51.100.20" })).kod, 200);
  });
  await test("yonetim: bicimsiz id / bilinmeyen islem / olmayan kayit", async () => {
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "onayla", id: "../x" } })).kod, 400);
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "hepsini-sil", id: "0123456789abcdef" } })).kod, 400);
    assert.strictEqual((await cagir(yon, { method: "POST", headers: YETKI, body: { islem: "onayla", id: "0123456789abcdef" } })).kod, 404);
  });
  await test("yonetim ozeti: yalniz etkilesim alan yazilar, dogru sayilar", async () => {
    const c = cerezDegeri(await gonder({ tur: "oy", deger: "begeni" }));
    await gonder({ tur: "ifade", deger: IFADELER[4] }, { cerez: c });
    const o = (await cagir(yon, { headers: YETKI })).govde.ozet;
    assert.strictEqual(o.length, 1);
    assert.strictEqual(o[0].yol, YOL);
    assert.strictEqual(o[0].begeni, 1);
    assert.strictEqual(o[0].ifade[IFADELER[4]], 1);
  });

  // ── kisisel veri ──
  await test("depoda IP ya da ham ziyaretci cerezi DURMAZ", async () => {
    const r = await gonder({ tur: "oy", deger: "begeni" }, { ip: "203.0.113.77" });
    await gonder({ tur: "yorum", rumuz: "Deniz", metin: "merhaba" }, { cerez: cerezDegeri(r), ip: "203.0.113.77" });
    const anahtarlar = await redis("KEYS", "*");
    const hepsi = [];
    for (const k of anahtarlar) {
      const t = await redis("TYPE", k);
      hepsi.push(k);
      if (t === "hash") hepsi.push(...(await redis("HGETALL", k)));
      else if (t === "string") hepsi.push(String(await redis("GET", k)));
      else if (t === "zset") hepsi.push(...(await redis("ZRANGE", k, "0", "-1")));
    }
    const dok = hepsi.join("\n");
    assert.ok(!dok.includes("203.0.113.77"), "IP depoda");
    assert.ok(!dok.includes(cerezDegeri(r).split(".")[1]), "cerez imzasi depoda");
    for (const k of anahtarlar) {
      if (/^etk:(hiz|yeni):/.test(k)) assert.ok((await redis("TTL", k)) > 0, "sureli olmali: " + k);
    }
  });

  console.log(`\n${n} test gecti.`);
})().catch((e) => { console.error("HATA:", e && e.stack || e); process.exit(1); });
