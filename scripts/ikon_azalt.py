#!/usr/bin/env python3
# scripts/ikon_azalt.py — ikon yazi tiplerini ve CSS'lerini kullanilanla
# sinirlar (22.09.2026).
#
# OLCUM (canli mobil, /ss/kpss/): fontawesome-webfont.woff2 75 KB + Flaticon
# 22 KB iniyordu; o sayfada FontAwesome'dan kullanilan ikon sayisi BIR
# (fa-times). Tema 700'den fazla ikonun tamamini tasiyordu.
#
# YAPILAN:
#   1. CSS'ten `.fa-x:before{content:"\fxxx"}` kurallarindan YALNIZ sitede
#      gecenler korunur (geri kalani silinir).
#   2. Yazi tipi, korunan ikonlarin kod noktalarina gore altkumeye indirilir
#      (fontTools). eot/ttf/svg kaynaklari da atilir; woff2 her yerde var.
#   3. Ciktilar YENI dosyalara yazilir (css/*-az.css, fonts/*-az.woff2);
#      orijinaller elden gecirilmez, geri donus kolay olsun.
#
# Ikon adlari HTML *ve* JS dosyalarindan toplanir: uniconnectly-blok.js gibi
# betikler ikon sinifini calisma aninda basiyor, taramaya girmezse ikon kaybolur.
#
# Kullanim: <venv>/bin/python scripts/ikon_azalt.py
import re, pathlib, sys

KOK = pathlib.Path(__file__).resolve().parent.parent
HARIC = ("arsiv", "okyanus", "temaindexler", "scripts")

def kullanilan(on_ek):
    bulunan = set()
    for uzanti in ("*.html", "*.js"):
        for p in KOK.rglob(uzanti):
            if p.relative_to(KOK).parts[0] in HARIC:
                continue
            try:
                s = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            bulunan.update(re.findall(r"\b" + on_ek + r"[a-z0-9-]+", s))
    return bulunan

def azalt(css_ad, on_ek, font_ad, yeni_css, yeni_font, font_ailesi):
    from fontTools import subset
    s = (KOK / css_ad).read_text(encoding="utf-8")
    # Kural blogu: secici listesi + govde. FA4 kucultulmus CSS takma adlari
    # GRUPLAR (".fa-close:before,.fa-remove:before,.fa-times:before{...}"),
    # Flaticon ise govdeye noktali virgul koyar. Ikisini de yakalamak icin
    # blok blok ayristirilir; tek-secicili desen 10 ikonu kacirmisti.
    blok = re.compile(r"([^{}]+)\{([^{}]*)\}")
    kod = re.compile(r"content\s*:\s*[\"']\\([0-9a-fA-F]+)[\"']")
    secici = re.compile(r"\.(" + on_ek + r"[a-z0-9-]+):+before")
    kullanim = kullanilan(on_ek)
    tum, kul, kodlar, silinecek = set(), set(), set(), []
    for m in blok.finditer(s):
        adlar = set(secici.findall(m.group(1)))
        c = kod.search(m.group(2))
        if not adlar or not c:
            continue
        tum |= adlar
        if adlar & kullanim:
            kul |= adlar & kullanim
            kodlar.add(int(c.group(1), 16))
        else:
            silinecek.append(m.span())
    assert kul, f"{css_ad}: kullanilan ikon bulunamadi"
    parca, son = [], 0
    for a, b in silinecek:
        parca.append(s[son:a]); son = b
    parca.append(s[son:])
    y = "".join(parca)
    # @font-face kaynaklarini tek woff2'ye indir
    y = re.sub(r"src:\s*url\([^;]*?\);", f"src:url('/{yeni_font}') format('woff2');", y, count=1, flags=re.S)
    (KOK / yeni_css).write_text(y, encoding="utf-8")

    kodlar = sorted(kodlar)
    se = subset.Subsetter(subset.Options(layout_features=[], notdef_outline=True,
                                         drop_tables=["FFTM"], ignore_missing_glyphs=True))
    font = subset.load_font(str(KOK / font_ad), subset.Options(flavor="woff2"))
    se.populate(unicodes=kodlar)
    se.subset(font)
    subset.save_font(font, str(KOK / yeni_font), subset.Options(flavor="woff2", with_zopfli=False))
    eski_f = (KOK / font_ad).stat().st_size
    yeni_f = (KOK / yeni_font).stat().st_size
    print(f"{font_ailesi}: {len(kul)}/{len(tum)} ikon · yazi tipi {eski_f//1024} KB → {yeni_f//1024} KB"
          f" · css {len(s)//1024} KB → {len(y)//1024} KB")
    return sorted(kul)

if __name__ == "__main__":
    azalt("css/font-awesome.min.css", "fa-", "fonts/fontawesome-webfont3e6e.woff2",
          "css/font-awesome-az.css", "fonts/fontawesome-az.woff2", "FontAwesome")
    azalt("css/flaticon.css", "flaticon-", "fonts/Flaticon.woff2",
          "css/flaticon-az.css", "fonts/Flaticon-az.woff2", "Flaticon")
