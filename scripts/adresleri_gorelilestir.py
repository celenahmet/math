#!/usr/bin/env python3
# scripts/adresleri_gorelilestir.py — `https://ahmetcelen.com.tr/...` mutlak
# adreslerini goreli `/...` yapar; site hangi alan adinda yayindaysa
# baglantilar oraya gider (Vercel on izleme adresi dahil).
#
# DOKUNULMAYANLAR (SEO):
# - <link rel="canonical"> ve og:url satirlari (mutlak kalmali)
# - sitemap.xml, robots.txt
#
# Kullanim: python3 scripts/adresleri_gorelilestir.py [--kuru]
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
KURU = "--kuru" in sys.argv
UZANTILAR = {".html", ".htm", ".css", ".js", ".php"}

# Sirasi onemli: once ozel bicimler, sonra genel.
DONUSUMLER = [
    (re.compile(r'https?://(?:www\.)?ahmetcelen\.com\.tr\?=home'), '/'),
    (re.compile(r'(["\'(])https?://(?:www\.)?ahmetcelen\.com\.tr/'), r'\1/'),
    (re.compile(r'(["\'(])https?://(?:www\.)?ahmetcelen\.com\.tr(["\')])'), r'\1/\2'),
]
KORU = re.compile(r'rel="canonical"|property="og:url"|name="twitter:url"', re.I)

dosya_sayisi = 0; degisim_sayisi = 0
for p in KOK.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in UZANTILAR:
        continue
    rel = p.relative_to(KOK).as_posix()
    if rel.startswith(("scripts/", "node_modules/", ".git/")):
        continue
    try:
        s0 = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        s0 = p.read_text(encoding="utf-8", errors="surrogateescape")
    if "ahmetcelen.com.tr" not in s0:
        continue
    satirlar = s0.split("\n")
    yeni = []; n = 0
    for sat in satirlar:
        if KORU.search(sat):
            yeni.append(sat); continue
        s = sat
        for rx, yerine in DONUSUMLER:
            s, k = rx.subn(yerine, s); n += k
        yeni.append(s)
    if n:
        dosya_sayisi += 1; degisim_sayisi += n
        if not KURU:
            p.write_text("\n".join(yeni), encoding="utf-8", errors="surrogateescape")
print(f"{'KURU: ' if KURU else ''}{dosya_sayisi} dosyada {degisim_sayisi} adres goreli yapildi.")
kalan = 0
for p in KOK.rglob("*.html"):
    t = p.read_text(encoding="utf-8", errors="surrogateescape")
    for sat in t.split("\n"):
        if "ahmetcelen.com.tr" in sat and not KORU.search(sat):
            kalan += 1
print(f"canonical/og:url disinda kalan mutlak adres satiri: {kalan}")
