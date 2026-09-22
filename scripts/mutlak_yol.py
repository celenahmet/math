#!/usr/bin/env python3
# scripts/mutlak_yol.py — alt dizindeki sayfalarda goreli varlik yollarini
# mutlak yapar (22.09.2026).
#
# BULGU: /dokumanlar/** ve /cozumler/denemeler/ altindaki 14 sayfa CSS/JS/gorseli
# GORELI yolla cagiriyordu: href="css/style.css" → /dokumanlar/ayt/bio/css/style.css
# → canlida 404 (dogrulandi). Yani bu sayfalar tarayicida TAMAMEN STILSIZ ve
# betiksiz aciliyordu; menu, geri sayim, mobil uyum hicbiri calismiyordu.
# Arama motoru icin de "mobile-friendly degil" sinyali uretiyorlardi.
#
# Kok dizindeki sayfalarda goreli yol zaten dogru cozuluyor; bu betik yalniz
# ALT DIZIN sayfalarina dokunur.
#
# Kullanim: python3 scripts/mutlak_yol.py
import re, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
HARIC = ("arsiv", "okyanus", "temaindexler", "scripts")
DESEN = re.compile(r'((?:href|src)=")(css/|js/|images/)')

n = t = 0
for p in sorted(KOK.rglob("*.html")):
    par = p.relative_to(KOK).parts
    if par[0] in HARIC or len(par) == 1:      # kok dizin: goreli yol zaten dogru
        continue
    try:
        s = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    y, k = DESEN.subn(lambda m: m.group(1) + "/" + m.group(2), s)
    if k:
        p.write_text(y, encoding="utf-8")
        n += 1
        t += k
print(f"mutlak yol: {n} sayfa, {t} baglanti duzeltildi")
