"""Generate page-specific metadata after copying a shared HTML template."""
import json
import re

import jsonld_uygula as J
import seo_basliklari as S


def uygula(content, relative_path):
    path = S.KOK / relative_path
    url = S.yol_of(path)
    for name in ('seo', 'jsonld'):
        content = re.sub(r'<!-- ' + name + r':bas -->.*?<!-- ' + name + r':son -->\s*', '', content, flags=re.S)
    if url.startswith('/ss/') and url != '/ss/':
        key = url.strip('/').split('/')[1]
        data = J.ss_veri.SAYFALAR[key]
        years = [str(row[0]) for row in data['kartlar']]
        title = f"{data['kisa']} Çıkmış Sorular PDF ({min(years)}–{max(years)}) - ÖSYM"
        content = re.sub(r'<title>.*?</title>', lambda m: '<title>' + title + '</title>', content, count=1, flags=re.S)
        graph = J.ss_grafi(key, J.ss_veri.SAYFALAR[key])
    elif url.startswith('/sinavlar/') and url != '/sinavlar/':
        exam = next((s for s in J.js_sinavlar().values() if url == f"/sinavlar/{s['yol']}/"), None)
        graph = J.sinav_grafi(exam['yol'], exam) if exam else []
    else:
        name = 'Çıkmış Sorular' if url == '/ss/' else 'Sınav Geri Sayımları'
        graph = [{'@type': 'CollectionPage', 'url': S.ALAN + url, 'name': name}, J.kirinti([('Ana Sayfa', '/'), (name, url)])]
    metadata = S.blok(path, url, content)
    metadata += '<!-- jsonld:bas -->\n<script type="application/ld+json">'
    metadata += json.dumps(J.graf(graph), ensure_ascii=False, separators=(',', ':'))
    metadata += '</script>\n<!-- jsonld:son -->\n'
    return content.replace('</head>', metadata + '</head>', 1)


if __name__ == '__main__':
    for folder in ('ss', 'sinavlar'):
        for path in (S.KOK / folder).glob('*/index.html'):
            if '/tema/' not in str(path):
                old = path.read_text(encoding='utf-8')
                path.write_text(uygula(old, path.relative_to(S.KOK).as_posix()), encoding='utf-8')
        path = S.KOK / folder / 'index.html'
        path.write_text(uygula(path.read_text(encoding='utf-8'), f'{folder}/index.html'), encoding='utf-8')
