"""Read-only audit of Search Console exports, sitemap and live responses."""
import concurrent.futures, collections, json, pathlib, re, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import openpyxl

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPORTS = pathlib.Path('/Users/ahmetcelen/Downloads/edakapusuz')
OUT = ROOT / 'scripts/seo-audit-2026-10-13.json'
BASE = 'https://ahmetcelen.com.tr'

def fetch(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; SiteAudit/1.0)'})
        with urllib.request.urlopen(req, timeout=25) as r:
            body = r.read().decode('utf-8', errors='replace') if 'text' in r.headers.get('Content-Type', '') or url.endswith('.xml') else ''
            canonical = re.findall(r'<link[^>]*rel=[\"\']canonical[\"\'][^>]*href=[\"\']([^\"\']+)', body, re.I)
            robots = re.findall(r'<meta[^>]*name=[\"\']robots[\"\'][^>]*content=[\"\']([^\"\']+)', body, re.I)
            return dict(url=url, final=r.url, status=r.status, canonical=canonical, robots=robots,
                        xrobots=r.headers.get('X-Robots-Tag'), title=re.findall(r'<title>(.*?)</title>', body, re.S),
                        links=re.findall(r'<a\b[^>]*href=[\"\']([^\"\']+)', body, re.I), bytes=len(body), body=body if url.endswith(('.xml', '.txt')) else '')
    except urllib.error.HTTPError as e:
        return dict(url=url,status=e.code, final=e.url)
    except Exception as e:
        return dict(url=url,status=0,error=str(e))

def run():
    exports = {}
    for p in REPORTS.glob('*ahmetcelen*Coverage*.xlsx'):
        w = openpyxl.load_workbook(p, data_only=True)
        exports[p.name] = {'meta': list(w['Meta Veri'].values), 'rows': [[str(v) if v is not None else None for v in row] for row in list(w['Tablo'].values)[1:]]}
    sitemap = fetch(BASE + '/sitemap.xml')
    urls = set(re.findall(r'<loc>(.*?)</loc>', sitemap.get('body','')))
    for data in exports.values():
        urls.update(row[0] for row in data['rows'])
    urls.update([BASE+'/', BASE+'/robots.txt', BASE+'/blog/',BASE+'/blog/logaritma/',BASE+'/blog/parabol-konu-anlatimli-pdf/'])
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(fetch, sorted(urls)))
    OUT.write_text(json.dumps(dict(exports=exports, sitemap=sitemap, results=results),ensure_ascii=False,indent=2))
    print('Saved', OUT)
    print('HTTP', dict(collections.Counter(r['status'] for r in results)))
    for r in results:
        if r['status'] != 200 or ('noindex' in ' '.join(r.get('robots',[])) and r['url'] in sitemap.get('body','')):
            print(r['status'],r['url'],r.get('final'),r.get('robots'))

if __name__ == '__main__':
    run()
