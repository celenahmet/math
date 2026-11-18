// ahmetcelen.com.tr Cloudflare Worker (Vercel'den tasima, 18.11).
// html_handling "none": var olan dosya (css, js, .html, xml) Worker'a ugramadan
// sunulur. Bulunamayan her istek buraya gelir ve vercel.json'un Vercel'deki
// sirasi uygulanir: api, parametreli yonlendirme, sonda egik cizgi (308),
// klasor index.html, yeniden yazma (PDF medya sunucusundan), 404.
import vercel from '../vercel.json';
import { compile, fill, isParam, statusOf } from './vercel-rules.mjs';
import { runVercelHandler, plain } from './vercel-node.mjs';
import populer from '../api/populer.js';
import goruntulenme from '../api/goruntulenme.js';
import etkilesim from '../api/etkilesim.js';
import yonetim from '../api/yonetim.js';

const API = { populer, goruntulenme, etkilesim, yonetim };
const REDIRECTS = vercel.redirects.filter((r) => isParam(r.source)).map((r) => ({ re: compile(r.source), dest: r.destination, status: statusOf(r) }));
const REWRITES = (vercel.rewrites || []).map((r) => ({ re: compile(r.source), dest: r.destination }));
const HEADER_RULES = vercel.headers.map((h) => ({ re: compile(h.source), headers: h.headers }));
const HSTS = 'max-age=63072000';

// Worker'in urettigi yanitlara vercel.json basliklari (statik dosyalara _headers).
function withHeaders(res, path, { cors = false } = {}) {
  const out = new Response(res.body, res);
  for (const rule of HEADER_RULES) if (rule.re.test(path)) for (const { key, value } of rule.headers) out.headers.set(key, value);
  out.headers.set('Strict-Transport-Security', HSTS);
  if (cors) out.headers.set('Access-Control-Allow-Origin', '*');
  return out;
}

function redirect(location, status, path) {
  return withHeaders(new Response(null, { status, headers: { Location: location } }), path);
}

async function notFound(env, url, request, path) {
  const page = await env.ASSETS.fetch(new Request(url.origin + '/404.html', { method: request.method === 'HEAD' ? 'HEAD' : 'GET' }));
  return withHeaders(new Response(page.body, { status: 404, headers: page.headers }), path);
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const p = url.pathname;

    // 1) API: Vercel /api/x -> 308 /api/x/, /api/x/ ve /api/x.js calisir
    const api = p.match(/^\/api\/([a-z]+)(\/|\.js)?$/);
    if (api && API[api[1]]) {
      if (!api[2]) return redirect(url.origin + p + '/' + url.search, 308, p);
      return withHeaders(await runVercelHandler(API[api[1]], request, ctx, url), p);
    }
    if (p.startsWith('/api/')) return notFound(env, url, request, p);

    // 2) Parametreli yonlendirmeler (Vercel'de dosyadan once)
    for (const r of REDIRECTS) {
      const m = r.re.exec(p);
      if (m) return redirect(fill(r.dest, m.groups) + url.search, r.status, p);
    }

    // 3) trailingSlash: true -> uzantisiz adrese egik cizgi (308)
    const last = p.slice(p.lastIndexOf('/') + 1);
    if (last && !last.includes('.')) return redirect(url.origin + p + '/' + url.search, 308, p);

    // 4) Klasor: index.html
    if (p.endsWith('/')) {
      const idx = await env.ASSETS.fetch(new Request(url.origin + p + 'index.html', { method: request.method === 'HEAD' ? 'HEAD' : 'GET', headers: request.headers }));
      if (idx.status === 200 || idx.status === 304) return idx;
    }

    // 5) Yeniden yazma (dosya yoksa)
    for (const r of REWRITES) {
      const m = r.re.exec(p);
      if (!m) continue;
      const dest = fill(r.dest, m.groups);
      if (dest.startsWith('https://')) {
        if (request.method !== 'GET' && request.method !== 'HEAD') return plain(405, 'Method Not Allowed', { Allow: 'GET, HEAD' });
        const pass = new Headers();
        for (const k of ['range', 'if-none-match', 'if-modified-since', 'accept-encoding']) if (request.headers.has(k)) pass.set(k, request.headers.get(k));
        const up = await fetch(dest + url.search, { method: request.method, headers: pass, redirect: 'manual' });
        const h = new Headers(up.headers);
        h.delete('set-cookie');
        return withHeaders(new Response(up.body, { status: up.status, headers: h }), p, { cors: true });
      }
      const inner = await env.ASSETS.fetch(new Request(url.origin + dest, { method: request.method === 'HEAD' ? 'HEAD' : 'GET' }));
      if (inner.status === 200) return inner;
    }

    return notFound(env, url, request, p);
  },
};
