#!/usr/bin/env python3
# scripts/css_zinciri.py — style.css'teki @import zincirini kirar (22.09.2026)
#
# BULGU (mobil Lighthouse 62, FCP 5,3 sn / LCP 7,6 sn):
# css/style.css (285 KB) dosyasinin BASINDA 14 adet `@import url(...)` vardi.
# @import zincirli istektir: tarayici once style.css'i indirip AYRISTIRMAK
# zorunda, ancak ondan sonra bu 14 dosyayi kesfedip istiyor. Yani kritik yol
# iki kat derin; 3G'de saniyelerce bos ekran.
#
# AYNI ZINCIR GORSEL ARIZA DA URETIYORDU (Ahmet 22.09, ekran goruntusu):
# acilir menuyu gizleyen kural `.ace-responsive-menu li ul { display:none }`
# ace-responsive-menu.css icinde ve o dosya zincirin 5. halkasi. Gelene kadar
# "Ders Notlari" alt menusu SAYFANIN USTUNDE ACIK duruyordu; menu JS'i
# calisincaya dek basligi ~265 px sisirip icerigi asagi itiyordu.
#
# COZUM: @import'lar style.css'ten cikarilir, her sayfanin <head>'ine
# style.css linkinden HEMEN ONCE gercek <link> etiketi olarak, AYNI SIRADA
# yazilir. Boylece:
#   · 14 dosya style.css ile PARALEL iner (zincir yok)
#   · belge sirasi korundugu icin kaskad (oncelik) aynen kalir
#   · alt menu ilk boyamadan once gizlenir → parlama ve kayma biter
#
# Kullanilmayan/kritik olmayanlar `media="print" onload` ile ertelenir:
# olculdu (sinif taramasi) → jquery-ui, font-awesome-animation,
# magnific-popup, timecounter sitede HIC kullanilmiyor; bootstrap-select,
# simplebar, progressbar, animate ilk ekranda yok.
#
# font-awesome.min.css ve flaticon.css bu listede YOK: onlar zaten
# scripts/seo_basliklari.py tarafindan ertelenmis olarak ekleniyor.
#
# Idempotent: "<!-- cssz:bas -->" ... "<!-- cssz:son -->".
# Kullanim: python3 scripts/css_zinciri.py
import re, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
BAS, SON = "<!-- cssz:bas -->", "<!-- cssz:son -->"

# (dosya, bloklayici_mi) — SIRA style.css'teki @import sirasinin AYNISI.
# Sira degismez: kaskad belge sirasina gore cozulur.
# 22.09 ikinci tur: adlar "-az" surumlerine gecti (scripts/css_azalt.py).
# megadropdown.css listeden CIKTI: budama sonrasi 0 bayt kaldi, sitede
# tek bir secicisi bile kullanilmiyor.
# 22.09 ucuncu tur: ertelenmis 8 dosya TAMAMEN cikti (163 KB bos indirme).
# Gerekce: onlari besleyen betikler de kaldirildi (scripts/js_yuku.py), yani
# sinifi calisma aninda ekleyecek kod artik yok ve govdede de gecmiyorlar:
#   jquery-ui (jquery-ui.js hic yuklenmiyordu) · font-awesome-animation (faa-*
#   yok) · bootstrap-select (selectpicker yok) · simplebar · progressbar
#   (.circlechart yok) · animate (class="wow" yok, wow.min.js kaldirildi) ·
#   magnific-popup (isotop.js kaldirildi) · timecounter (timepicker.js kaldirildi)
# megadropdown.css da cikti: budama sonrasi 0 bayt.
DOSYALAR = [
    ("menu-az.css", True),                     # baslik/mobil menu — ilk ekran
    ("ace-responsive-menu-az.css", True),      # alt menuyu gizler — SART
    ("slider-az.css", True),                   # ana sayfa hero slider — ilk ekran
]

def blok(girinti):
    sat = [BAS]
    for ad, bloklayici in DOSYALAR:
        if bloklayici:
            sat.append(f'<link rel="stylesheet" href="/css/{ad}">')
        else:
            sat.append(f'<link rel="stylesheet" href="/css/{ad}" media="print" onload="this.media=\'all\'">')
    ertelenen = "".join(f'<link rel="stylesheet" href="/css/{ad}">' for ad, b in DOSYALAR if not b)
    if ertelenen:
        sat.append(f"<noscript>{ertelenen}</noscript>")
    sat.append(SON)
    return "\n".join(girinti + x for x in sat) + "\n"

def style_css_ayikla():
    p = KOK / "css/style.css"
    s = p.read_text(encoding="utf-8")
    adlar = [ad for ad, _ in DOSYALAR] + ["font-awesome.min.css", "flaticon.css"]
    y, n = s, 0
    for ad in adlar:
        y, k = re.subn(r"@import url\(" + re.escape(ad) + r"\);\n", "", y)
        n += k
    if n == 0:
        return                                  # zaten temizlenmis (idempotent)
    assert n == len(adlar), f"style.css'te {n}/{len(adlar)} @import bulundu"
    y = y.replace("/* CSS Document */\n",
                  "/* CSS Document */\n"
                  "/* 22.09.2026: 14 @import KALDIRILDI (zincirli istek; mobil FCP 5,3 sn).\n"
                  "   Ayni dosyalar her sayfanin <head>'inde, bu dosyadan ONCE ve ayni\n"
                  "   sirada <link> ile paralel yukleniyor. Kaynak: scripts/css_zinciri.py */\n", 1)
    p.write_text(y, encoding="utf-8")
    print(f"style.css: {n} @import kaldirildi")

HEDEF = re.compile(r'^([ \t]*)<link rel="stylesheet" href="/css/style-az\.css(?:\?v=[0-9a-f]+)?">$', re.M)

def uygula():
    style_css_ayikla()
    n = 0
    for p in sorted(KOK.rglob("*.html")):
        if p.relative_to(KOK).parts[0] in ("arsiv", "okyanus", "temaindexler", "scripts"):
            continue
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        m = HEDEF.search(s)
        if not m:
            continue
        b = blok(m.group(1))
        if BAS in s and SON in s:
            a, c = s.index(BAS), s.index(SON) + len(SON) + 1
            t = s[:a] + b.lstrip() + s[c:]
        else:
            t = s[:m.start()] + b + s[m.start():]
        if t != s:
            p.write_text(t, encoding="utf-8")
            n += 1
    print(f"css zinciri: {n} sayfaya paralel <link> blogu yazildi")

if __name__ == "__main__":
    uygula()
