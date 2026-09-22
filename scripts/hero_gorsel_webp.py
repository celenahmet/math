#!/usr/bin/env python3
# scripts/hero_gorsel_webp.py — ana sayfa hero ve bolum arka planlarini
# WebP'ye cevirir (22.09.2026).
#
# OLCUM (canli mobil Lighthouse, ana sayfa): toplam transfer 1889 KB,
# LCP 12,3 sn. En agir kalem TEK BIR DOSYA: images/background/2.jpg = 1092 KB
# (1920x960, kotu sikistirilmis JPEG). Hero slaytlari da JPEG.
#
# WebP karsiliklari (kalite 78, ayni olcu):
#   images/background/2.jpg  1092 → 89 KB
#   images/home/1.jpg         160 → 95 KB
#   images/home/2.jpg         125 → 71 KB
#   images/home/3.jpg         115 → 58 KB
#
# Dosyalar MEDYA SUNUCUSUNA yuklenir (vercel.json /images/* adresini
# medya.ahmetcelen.com.tr'ye 307 ile yonlendiriyor), depoda da durur.
# Bu betik yalniz REFERANSLARI cevirir.
#
# Kullanim: python3 scripts/hero_gorsel_webp.py
import re, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
HARIC = ("arsiv", "okyanus", "temaindexler", "scripts")
GORSELLER = ["home/1", "home/2", "home/3", "background/2"]

def uygula():
    n = t = 0
    for p in sorted(KOK.rglob("*.html")):
        if p.relative_to(KOK).parts[0] in HARIC:
            continue
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        y = s
        for g in GORSELLER:
            # hem goreli (url(images/...)) hem mutlak (url(/images/...)) yazim
            y = re.sub(r"url\(/?images/" + re.escape(g) + r"\.jpg\)",
                       f"url(/images/{g}.webp)", y)
        if y != s:
            p.write_text(y, encoding="utf-8")
            n += 1
            t += sum(y.count(f"/images/{g}.webp") for g in GORSELLER)
    print(f"hero gorselleri WebP'ye cevrildi: {n} sayfa, {t} referans")

if __name__ == "__main__":
    uygula()
