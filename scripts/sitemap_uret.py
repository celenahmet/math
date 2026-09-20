#!/usr/bin/env python3
# scripts/sitemap_uret.py — yalnizca GERCEK icerik sayfalarindan sitemap.xml
# uretir. Tema demolari, hata sayfalari, yonlendirme sayfalari, test/kopya
# dosyalar ve .vercelignore ile yayindan cikan klasorler DAHIL EDILMEZ.
#
# Kullanim: python3 scripts/sitemap_uret.py
import pathlib, datetime, re

KOK = pathlib.Path(__file__).resolve().parent.parent
ALAN = "https://ahmetcelen.com.tr"

HARIC_ON_EK = (
    "temaindexler/", "okyanus/", "arsiv/", "sıcak/", "parabol/test1/",
    "video/eskiler/", "video/ucgen/eskiler/", "video/demo/", "video/ucgen/demo/",
    "scripts/", "css/", "js/", "fonts/", "images/", "error_docs/",
    "aytmat/", "cozumler/", "deneme/", "dersnot/",
)
HARIC_AD = {"cozum.html", "indexcopy.html", "index1.html", "GET.html", "404.html", "403.html"}
HARIC_PARCA = ("/tema/", "/errors/", "/bakim/", "/error/", "/httpdocs/", "/css/", "/js/", "/images/")
HARIC_DESEN = re.compile(r"^google[0-9a-f]+\.html$|^_")  # site dogrulama + gecici test dosyalari

def yonlendirme_mi(p):
    try:
        bas = p.read_text(encoding="utf-8", errors="ignore")[:1500].lower()
    except OSError:
        return True
    return 'http-equiv="refresh"' in bas or "yonlendiriliyor" in bas or "404 not found" in bas

urls = []
for p in sorted(KOK.rglob("*.html")):
    r = p.relative_to(KOK).as_posix()
    if r.startswith(HARIC_ON_EK) or p.name in HARIC_AD or HARIC_DESEN.match(p.name):
        continue
    if any(x in "/" + r for x in HARIC_PARCA) or yonlendirme_mi(p):
        continue
    if p.name == "index.html":
        yol = "/" if p.parent == KOK else "/" + p.parent.relative_to(KOK).as_posix() + "/"
    else:
        yol = "/" + r
    urls.append(yol)

urls = sorted(set(urls), key=lambda u: (u.count("/"), u))
bugun = datetime.date.today().isoformat()
xml = ['<?xml version="1.0" encoding="UTF-8"?>',
       '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
xml += [f"  <url><loc>{ALAN}{u}</loc><lastmod>{bugun}</lastmod></url>" for u in urls]
xml.append("</urlset>")
(KOK / "sitemap.xml").write_text("\n".join(xml) + "\n", encoding="utf-8")
print(f"{len(urls)} adres yazildi → sitemap.xml")
