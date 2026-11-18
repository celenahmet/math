// Cloudflare Workers yayini icin .cf-dist/ uretir (Vercel'den tasima, 18.11).
// Dosyalar: depodaki izli dosyalar - .vercelignore - gelistirme dosyalari -
// Vercel'de parametreli yonlendirmenin onune gectigi dosyalar (or. *.php).
// Sabit yonlendirmeler _redirects'e, basliklar _headers'a; geri kalan kurallari
// worker.mjs vercel.json'dan kendisi uygular. Cevrilemeyen kural derlemeyi durdurur.
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import path from 'node:path';
import { compile, isParam, statusOf } from './vercel-rules.mjs';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const OUT = path.join(ROOT, '.cf-dist');
const fail = (m) => { console.error('build: STOP ' + m); process.exit(1); };

const vercel = JSON.parse(fs.readFileSync(path.join(ROOT, 'vercel.json'), 'utf8'));
for (const k of Object.keys(vercel)) if (!['$schema', 'trailingSlash', 'regions', 'redirects', 'rewrites', 'headers'].includes(k)) fail('vercel.json bilinmeyen alan: ' + k);
if (vercel.trailingSlash !== true || vercel.cleanUrls) fail('trailingSlash/cleanUrls degisti, worker.mjs yeniden gozden gecirilmeli');
for (const r of vercel.redirects) if (r.has || r.missing) fail('kosullu yonlendirme: ' + r.source);
const paramRedirects = vercel.redirects.filter((r) => isParam(r.source)).map((r) => compile(r.source));
for (const r of vercel.rewrites || []) compile(r.source);

const git = (...a) => execFileSync('git', a, { cwd: ROOT, maxBuffer: 1 << 28 }).toString('utf8').split('\0').filter(Boolean);
const tracked = git('ls-files', '-z');
const ignored = new Set(git('ls-files', '-z', '-ci', '--exclude-from=.vercelignore'));
const DEV = /^(api\/|cloudflare\/|vercel\.json$|wrangler\.jsonc$|package(-lock)?\.json$|\.(?!well-known\/)[^/]+)/;

fs.rmSync(OUT, { recursive: true, force: true });
let n = 0, bytes = 0, shadowed = 0;
for (const f of tracked) {
  if (ignored.has(f) || DEV.test(f)) continue;
  if (paramRedirects.some((re) => re.test('/' + f))) { shadowed++; continue; }
  const src = path.join(ROOT, f);
  const st = fs.statSync(src, { throwIfNoEntry: false });
  if (!st || !st.isFile()) continue;
  if (st.size > 25 * 1024 * 1024) fail('25 MiB ustu dosya: ' + f);
  fs.mkdirSync(path.dirname(path.join(OUT, f)), { recursive: true });
  fs.copyFileSync(src, path.join(OUT, f));
  n++; bytes += st.size;
}
if (n > 19000) fail('dosya sayisi Free sinirina yakin: ' + n);
if (!fs.existsSync(path.join(OUT, '404.html'))) fail('404.html yok');

// Sabit yonlendirmeler: sira korunur (hepsi sabit, joker yok).
const red = vercel.redirects.filter((r) => !isParam(r.source)).map((r) => {
  if (r.destination.startsWith('http://')) fail('http hedefi: ' + r.source);
  return `${r.source} ${r.destination} ${statusOf(r)}`;
});
if (red.length > 1900) fail('_redirects sinira yakin');
fs.writeFileSync(path.join(OUT, '_redirects'), red.join('\n') + '\n');

function hpaths(src) {
  let s = src.replace(/\(\.\*\)/g, '*').replace(/\\\./g, '.');
  const alt = s.match(/\(([^()]+)\)/);
  const list = alt ? alt[1].split('|').map((a) => s.replace(alt[0], a)) : [s];
  for (const p of list) if (/[()\\|?+^$[\]{}:]/.test(p)) fail('cevrilemeyen baslik kurali: ' + src);
  return list;
}
const blocks = [['/*', [['Strict-Transport-Security', 'max-age=63072000'], ['Access-Control-Allow-Origin', '*']]]];
for (const h of vercel.headers || []) for (const p of hpaths(h.source)) {
  const hs = h.headers.map((x) => [x.key, x.value]);
  const prev = blocks.find((b) => b[0] === p);
  if (prev) prev[1].push(...hs); else blocks.push([p, hs]);
}
const seen = new Set(), lines = [];
for (const [p, hs] of blocks) {
  lines.push(p);
  for (const [k, v] of hs) {
    if (seen.has(k.toLowerCase()) && p !== '/*') lines.push(`  ! ${k}`);
    lines.push(`  ${k}: ${v}`);
  }
  for (const [k] of hs) seen.add(k.toLowerCase());
}
if (blocks.length > 95) fail('_headers sinira yakin');
fs.writeFileSync(path.join(OUT, '_headers'), lines.join('\n') + '\n');
console.log(`build: ${n} dosya, ${(bytes / 1048576).toFixed(1)} MB, yonlendirmenin golgeledigi ${shadowed} dosya disarida, ${red.length} sabit yonlendirme, ${blocks.length} baslik kurali`);
