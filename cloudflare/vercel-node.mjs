// Vercel Node fonksiyonlarini (req, res) Cloudflare Worker'da DEGISTIRMEDEN
// calistiran kopru (bote-web/cloudflare/worker.mjs ile ayni mantik, 18.11).
const MAX_BODY = 64 * 1024;

export function plain(status, text, extra = {}) {
  return new Response(text, { status, headers: { 'Content-Type': 'text/plain; charset=utf-8', 'Cache-Control': 'no-store', ...extra } });
}

export class NodeRes {
  constructor() { this.statusCode = 200; this.headers = new Headers(); this.body = null; this.finished = false; }
  setHeader(k, v) {
    if (Array.isArray(v)) { this.headers.delete(k); for (const x of v) this.headers.append(k, String(x)); }
    else this.headers.set(k, String(v));
    return this;
  }
  getHeader(k) { return this.headers.get(k) ?? undefined; }
  removeHeader(k) { this.headers.delete(k); }
  status(c) { this.statusCode = c; return this; }
  json(o) {
    if (!this.headers.has('content-type')) this.headers.set('Content-Type', 'application/json; charset=utf-8');
    return this.end(JSON.stringify(o));
  }
  send(b) {
    if (b !== null && typeof b === 'object') return this.json(b);
    return this.end(b);
  }
  end(b) { if (!this.finished) { this.body = b ?? null; this.finished = true; } return this; }
}

export async function nodeReq(request, url) {
  const headers = {};
  for (const [k, v] of request.headers) headers[k.toLowerCase()] = v;
  // Istemcinin gonderdigi adres basliklari GECERSIZ: Vercel bunlari kendisi
  // yaziyordu, burada Cloudflare'in olctugu adres yazilir (sinir atlatilamaz).
  const ip = request.headers.get('cf-connecting-ip') || '';
  headers['x-real-ip'] = ip;
  headers['x-forwarded-for'] = ip;
  const query = {};
  for (const [k, v] of url.searchParams) query[k] = k in query ? [].concat(query[k], v) : v;
  let body;
  if (request.method !== 'GET' && request.method !== 'HEAD') {
    if (Number(request.headers.get('content-length') || 0) > MAX_BODY) return { tooLarge: true };
    const text = await request.text();
    if (text.length > MAX_BODY) return { tooLarge: true };
    body = text;
    if ((headers['content-type'] || '').includes('application/json') && text) {
      try { body = JSON.parse(text); } catch { return { badJson: true }; }
    }
  }
  return { req: { method: request.method, url: url.pathname + url.search, headers, query, body, socket: { remoteAddress: ip } } };
}

function edgeTtl(h) {
  const v = h.get('vercel-cdn-cache-control') || '';
  let m = v.match(/max-age=(\d+)/);
  if (m) return Number(m[1]);
  m = (h.get('cache-control') || '').match(/s-maxage=(\d+)/);
  return m ? Number(m[1]) : 0;
}

// Vercel CDN'inde onbelleklenen GET yanitlari Cloudflare onbellegine konur.
export async function runVercelHandler(handler, request, ctx, url) {
  const cacheable = request.method === 'GET';
  const cache = caches.default;
  const key = new Request(url.toString(), { method: 'GET' });
  if (cacheable) {
    const hit = await cache.match(key);
    if (hit) return hit;
  }
  const r = await nodeReq(request, url);
  if (r.tooLarge) return plain(413, 'Payload Too Large');
  if (r.badJson) return plain(400, 'Invalid JSON');
  const res = new NodeRes();
  try {
    await handler(r.req, res);
  } catch (e) {
    console.error('api', url.pathname, e && e.message);
    return plain(500, 'Internal Server Error');
  }
  if (!res.finished) return plain(500, 'Internal Server Error');
  const h = res.headers;
  const ttl = edgeTtl(h);
  h.delete('vercel-cdn-cache-control');
  const out = new Response(request.method === 'HEAD' ? null : res.body, { status: res.statusCode, headers: h });
  if (cacheable && ttl > 0 && res.statusCode === 200 && !h.has('set-cookie')) {
    const copy = new Response(res.body, { status: 200, headers: new Headers(h) });
    copy.headers.set('Cache-Control', `public, max-age=${ttl}`);
    ctx.waitUntil(cache.put(key, copy));
  }
  return out;
}
