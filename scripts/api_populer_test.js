// scripts/api_populer_test.js — api/populer.js icin mutlu yol + saldirgan
// testler (23.09.2026). Ag yok: fetch ve ortam degiskenleri taklit edilir.
// Calistirma: node scripts/api_populer_test.js
const assert = require("assert");
const path = require("path");
const YAZILAR = require("../api/_yazilar.json");
const IS = path.join(__dirname, "../api/populer.js");

function yanit() {
  const r = { kod: 0, govde: null, baslik: {} };
  r.setHeader = (k, v) => { r.baslik[k.toLowerCase()] = v; };
  r.status = (k) => { r.kod = k; return r; };
  r.json = (g) => { r.govde = g; return r; };
  return r;
}

async function cagir(req, { env = {}, depo } = {}) {
  for (const k of Object.keys(process.env)) if (/REST_API|UPSTASH/.test(k)) delete process.env[k];
  Object.assign(process.env, env);
  const istekler = [];
  global.fetch = async (url, opt) => {
    istekler.push({ url, opt });
    if (typeof depo === "function") return depo(url, opt);
    return { ok: true, json: async () => ({ result: depo }) };
  };
  delete require.cache[IS];
  const res = yanit();
  await require(IS)(Object.assign({ method: "GET", query: {} }, req), res);
  return { res, istekler };
}

const ENV = { KV_REST_API_URL: "https://depo.example", KV_REST_API_TOKEN: "GIZLI-TOKEN-123" };
let n = 0;
const test = async (ad, fn) => { await fn(); n++; console.log("ok  " + ad); };

(async () => {
  await test("POST reddedilir (405, Allow)", async () => {
    const { res, istekler } = await cagir({ method: "POST" }, { env: ENV, depo: [] });
    assert.strictEqual(res.kod, 405);
    assert.strictEqual(res.baslik["allow"], "GET, HEAD");
    assert.strictEqual(istekler.length, 0);
  });
  await test("DELETE reddedilir", async () => {
    const { res } = await cagir({ method: "DELETE" }, { env: ENV, depo: [] });
    assert.strictEqual(res.kod, 405);
  });
  await test("depo yoksa 503, onbelleksiz", async () => {
    const { res, istekler } = await cagir({}, {});
    assert.strictEqual(res.kod, 503);
    assert.strictEqual(res.baslik["cache-control"], "no-store");
    assert.strictEqual(istekler.length, 0);
  });
  await test("siralama, ilk 5, sifirlar elenir, CDN onbellegi", async () => {
    const sayilar = YAZILAR.map((_, i) => String(i * 10));  // ilk yazi 0
    const { res } = await cagir({}, { env: ENV, depo: sayilar });
    assert.strictEqual(res.kod, 200);
    const l = res.govde.yazilar;
    assert.ok(l.length <= 5 && l.length === Math.min(5, YAZILAR.length - 1));
    for (let i = 1; i < l.length; i++) assert.ok(l[i - 1].sayi >= l[i].sayi);
    assert.ok(l.every((x) => x.sayi > 0 && YAZILAR.includes(x.yol)));
    assert.match(res.baslik["cache-control"], /s-maxage=300/);
  });
  await test("sorgu parametresi anahtara GIRMEZ (enjeksiyon)", async () => {
    const { istekler } = await cagir({ query: { yol: "../../x", anahtar: "FLUSHALL" } }, { env: ENV, depo: YAZILAR.map(() => "1") });
    const govde = JSON.parse(istekler[0].opt.body);
    assert.strictEqual(govde[0], "MGET");
    assert.deepStrictEqual(govde.slice(1), YAZILAR.map((y) => "gor:" + y));
    assert.ok(!istekler[0].opt.body.includes("FLUSHALL") && !istekler[0].opt.body.includes("../"));
  });
  await test("token yalniz yetki basliginda, yanitta yok", async () => {
    const { res, istekler } = await cagir({}, { env: ENV, depo: YAZILAR.map(() => "3") });
    assert.strictEqual(istekler[0].opt.headers.Authorization, "Bearer GIZLI-TOKEN-123");
    assert.ok(!JSON.stringify(res.govde).includes("GIZLI"));
  });
  await test("bozuk degerler elenir (metin, negatif, tasma)", async () => {
    const bozuk = ["abc", "-5", "1e400", "7", null].concat(YAZILAR.slice(5).map(() => null)).slice(0, YAZILAR.length);
    const { res } = await cagir({}, { env: ENV, depo: bozuk });
    assert.strictEqual(res.kod, 200);
    assert.ok(res.govde.yazilar.every((x) => Number.isSafeInteger(x.sayi) && x.sayi > 0));
  });
  await test("depo hata kodu → 502, ic ayrinti sizmaz", async () => {
    const { res } = await cagir({}, { env: ENV, depo: async () => ({ ok: false, status: 401, json: async () => ({}) }) });
    assert.strictEqual(res.kod, 502);
    assert.deepStrictEqual(res.govde, { hata: "depo" });
    assert.strictEqual(res.baslik["cache-control"], "no-store");
  });
  await test("depo ag hatasi → 502", async () => {
    const { res } = await cagir({}, { env: ENV, depo: async () => { throw new Error("ECONNRESET 10.0.0.1"); } });
    assert.strictEqual(res.kod, 502);
    assert.ok(!JSON.stringify(res.govde).includes("10.0.0.1"));
  });
  await test("uzunluk tutmayan sonuc → 502", async () => {
    const { res } = await cagir({}, { env: ENV, depo: ["1"] });
    assert.strictEqual(YAZILAR.length > 1, true);
    assert.strictEqual(res.kod, 502);
  });
  await test("onekli ortam degiskeni de okunur", async () => {
    const { res } = await cagir({}, { env: { BLOG_REST_API_URL: "https://d", BLOG_REST_API_TOKEN: "t" }, depo: YAZILAR.map(() => "2") });
    assert.strictEqual(res.kod, 200);
  });
  await test("HEAD izinli", async () => {
    const { res } = await cagir({ method: "HEAD" }, { env: ENV, depo: YAZILAR.map(() => "1") });
    assert.strictEqual(res.kod, 200);
  });
  console.log(`\n${n} test gecti.`);
})().catch((e) => { console.error("BASARISIZ:", e.message); process.exit(1); });
