#!/usr/bin/env node
// scripts/pdf_yazdir.mjs — HTML'i Chrome ile A4 PDF'e basar (28.09.2026)
//
// Kullanim: node scripts/pdf_yazdir.mjs <isler.json>
//   isler.json: [{ "sayfa": "/.pdf-yapim/ac-010.html", "cikti": "/mutlak/yol.pdf",
//                  "ust": "<div></div>", "alt": "<div>...</div>" }]
//
// Neden Chrome: formuller MathML; tarayici yerel diziyor, PDF'e de ayni
// dizgi gidiyor (KaTeX/MathJax gerekmez). Page.printToPDF alt bilgi
// sablonunu (sayfa no / toplam), etiketli PDF'i ve bolum yer imlerini veriyor.
// Bagimlilik yok: Node 22'nin fetch ve WebSocket'i + depo kokunu sunan
// kucuk bir statik sunucu (yazi tipleri ve kapaklar /fonts, /blog/kapak'tan).
import { spawn } from 'node:child_process';
import fs from 'node:fs';
import http from 'node:http';
import os from 'node:os';
import path from 'node:path';

const KOK = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const CHROME = process.env.CHROME_YOLU || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const TUR = { '.html': 'text/html; charset=utf-8', '.css': 'text/css', '.woff2': 'font/woff2',
  '.avif': 'image/avif', '.png': 'image/png', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.jpg': 'image/jpeg' };

const isler = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));

// Yalniz depo kokunun ALTINDAKI dosyalari sunar (yol kacisi yok), yalniz 127.0.0.1.
const sunucu = http.createServer((istek, yanit) => {
  const yol = path.normalize(path.join(KOK, decodeURIComponent(new URL(istek.url, 'http://x').pathname)));
  if (!yol.startsWith(KOK + path.sep) || !fs.existsSync(yol) || fs.statSync(yol).isDirectory()) {
    yanit.writeHead(404); return yanit.end();
  }
  yanit.writeHead(200, { 'Content-Type': TUR[path.extname(yol)] || 'application/octet-stream' });
  fs.createReadStream(yol).pipe(yanit);
});
await new Promise((r) => sunucu.listen(0, '127.0.0.1', r));
const taban = `http://127.0.0.1:${sunucu.address().port}`;

const profil = fs.mkdtempSync(path.join(os.tmpdir(), 'pdf-chrome-'));
const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--no-first-run', '--no-default-browser-check',
  '--remote-debugging-port=0', `--user-data-dir=${profil}`, 'about:blank'], { stdio: 'ignore' });
let port;
for (let i = 0; i < 100 && !port; i++) {
  await new Promise((r) => setTimeout(r, 100));
  try { port = fs.readFileSync(path.join(profil, 'DevToolsActivePort'), 'utf8').split('\n')[0]; } catch {}
}
if (!port) throw new Error('Chrome acilmadi');
const hedef = (await (await fetch(`http://127.0.0.1:${port}/json/list`)).json()).find((t) => t.type === 'page');
const ws = new WebSocket(hedef.webSocketDebuggerUrl);
await new Promise((r) => ws.addEventListener('open', r));
let sira = 0; const bekleyen = new Map(); const olaylar = [];
ws.addEventListener('message', (e) => {
  const m = JSON.parse(e.data);
  if (m.id && bekleyen.has(m.id)) { const [ok, red] = bekleyen.get(m.id); bekleyen.delete(m.id); m.error ? red(new Error(m.error.message)) : ok(m.result); }
  else if (m.method) olaylar.push(m.method);
});
const gonder = (method, params = {}) => new Promise((ok, red) => { const i = ++sira; bekleyen.set(i, [ok, red]); ws.send(JSON.stringify({ id: i, method, params })); });
await gonder('Page.enable'); await gonder('Runtime.enable');

const sonuc = [];
try {
  for (const is of isler) {
    olaylar.length = 0;
    await gonder('Page.navigate', { url: taban + is.sayfa });
    for (let i = 0; i < 200 && !olaylar.includes('Page.loadEventFired'); i++) await new Promise((r) => setTimeout(r, 50));
    // Yazi tipleri ve gorseller hazir olmadan basilirsa yedek yazi tipi PDF'e girer.
    const hazir = await gonder('Runtime.evaluate', { awaitPromise: true, returnByValue: true, expression:
      `(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.complete?0:new Promise(r=>{i.onload=i.onerror=r})));
        return {kirik:[...document.images].filter(i=>!i.naturalWidth).map(i=>i.src), yazitipi:[...document.fonts].filter(f=>f.status==='error').map(f=>f.family)}})()` });
    const h = hazir.result.value;
    if (h.kirik.length || h.yazitipi.length) throw new Error(`${is.sayfa}: eksik varlik ${JSON.stringify(h)}`);
    // Sabit yukseklikli sayfalar (ilk bilgi sayfasi, son tanitim sayfasi) tasarsa
    // Chrome sessizce yeni sayfa acar (28.09: etiket eklenince 12 → 13 sayfa).
    // Tasma varsa basim DURUR; metin ya da duzen kisaltilir.
    const tasma = await gonder('Runtime.evaluate', { returnByValue: true, expression:
      `[...document.querySelectorAll('.p-bilgi-sayfasi,.p-tanitim-sayfasi')].filter(e=>e.scrollHeight>e.clientHeight+1).map(e=>e.className+' '+e.scrollHeight+'>'+e.clientHeight)` });
    if (tasma.result.value.length) throw new Error(`${is.sayfa}: sabit sayfa tasiyor ${JSON.stringify(tasma.result.value)}`);
    const pdf = await gonder('Page.printToPDF', {
      paperWidth: 8.2677, paperHeight: 11.6929, preferCSSPageSize: true, printBackground: true,
      marginTop: 0.59, marginBottom: 0.67, marginLeft: 0.63, marginRight: 0.63,
      displayHeaderFooter: true, headerTemplate: is.ust || '<div></div>', footerTemplate: is.alt || '<div></div>',
      generateTaggedPDF: true, generateDocumentOutline: true,
    });
    fs.mkdirSync(path.dirname(is.cikti), { recursive: true });
    fs.writeFileSync(is.cikti, Buffer.from(pdf.data, 'base64'));
    sonuc.push({ cikti: is.cikti, bayt: fs.statSync(is.cikti).size });
    process.stdout.write(`  basildi ${path.basename(is.cikti)}\n`);
  }
} finally {
  ws.close(); sunucu.close();
  // Chrome kapanmadan profil silinirse klasore yazmaya devam ediyor (ENOTEMPTY).
  const kapandi = new Promise((r) => chrome.once('exit', r));
  chrome.kill();
  await Promise.race([kapandi, new Promise((r) => setTimeout(r, 5000))]);
  try { fs.rmSync(profil, { recursive: true, force: true, maxRetries: 5, retryDelay: 200 }); } catch {}
}
console.log(JSON.stringify(sonuc));
