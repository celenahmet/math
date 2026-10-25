#!/usr/bin/env python3
# scripts/paketle.py — tema sayfalarinin 10 CSS'ini tek dosyada (css/tema.css),
# 9 hazir JS kutuphanesini tek dosyada (js/tema-vendor.js) birlestirir ve
# sayfalardaki baglantilari bu iki dosyaya cevirir (25.10.2026).
#
# Neden: Vercel Hobby'nin aylik 1M CDN istek kotasi %93'e geldi (kayan 30 gun);
# bayt degil ISTEK SAYISI olculuyor. Tema sayfasi (/ss/kpss/ sitenin trafiginin
# cogu) acilista 10 CSS + 13 JS istiyordu. Paketle 10 CSS -> 1, 9 JS -> 1.
#
# Kurallar:
# - Sira AYNEN korunur (basamakli stil sirasi = sayfadaki baglanti sirasi).
#   Bir sayfada tema CSS'leri bu sirada degilse ya da araya baska bir stil
#   girmisse o sayfaya DOKUNULMAZ ve adi yazilir.
# - JS yalniz ardisik ve ayni sirada duruyorsa birlestirilir; sayfaya ozel
#   betikler (sayfa-duzeltmeleri, script.js, arama, uniconnectly-blok...) ayri
#   kalir: biri hata verirse digerleri calismaya devam etsin.
# - Paketler her calistirmada kaynak dosyalardan YENIDEN uretilir; paketi elle
#   duzenleme. css_surum.py bu betigi ilk is cagirir, yani bilinen akis
#   ("degisiklikten sonra python3 scripts/css_surum.py") paketi de tazeler.
# - Islem tekrar edilebilir: zaten paketli sayfa degismez.
import pathlib, re

KOK = pathlib.Path(__file__).resolve().parent.parent
TEMA_CSS = ["css/bootstrap-az.css", "css/menu-az.css", "css/ace-responsive-menu-az.css", "css/slider-az.css",
            "css/style-az.css", "css/responsive-az.css", "css/duzeltmeler.css", "css/yazitipleri.css",
            "css/font-awesome-az.css", "css/flaticon-az.css"]
TEMA_JS = ["js/jquery-3.3.1.min.js", "js/jquery-migrate-3.0.0.min.js", "js/popper.min.js", "js/bootstrap.min.js",
           "js/jquery.mmenu.all.js", "js/ace-responsive-menu.js", "js/snackbar.min.js", "js/scrollto.js",
           "js/progressbar.js"]
PAKET_CSS, PAKET_JS = "css/tema.css", "js/tema-vendor.js"
BASLIK = "/* URETILMIS DOSYA: elle duzenleme. Kaynak: scripts/paketle.py ({}) */\n"

LINK = re.compile(r'<link\b[^>]*>', re.I)
HREF = re.compile(r'href="/([^"?]+)(?:\?[^"]*)?"')
STIL_ETIKETI = re.compile(r'<style\b|<link\b[^>]*rel="(?:stylesheet|preload)"[^>]*as="style"|<link\b[^>]*rel="stylesheet"', re.I)


def paketleri_uret():
    css = BASLIK.format(", ".join(TEMA_CSS))
    for yol in TEMA_CSS:
        css += f"\n/* --- {yol} --- */\n" + (KOK / yol).read_text(encoding="utf-8")
    (KOK / PAKET_CSS).write_text(css, encoding="utf-8")
    js = BASLIK.format(", ".join(TEMA_JS))
    for yol in TEMA_JS:
        govde = (KOK / yol).read_text(encoding="utf-8")
        govde = re.sub(r'^\s*//[#@] sourceMappingURL=.*$', '', govde, flags=re.M)  # haritalar yok, 404 istegi olmasin
        js += f"\n/* --- {yol} --- */\n" + govde + "\n;\n"
    (KOK / PAKET_JS).write_text(js, encoding="utf-8")


def css_cevir(s):
    """Tema CSS baglantilarini tek pakete cevirir; uymayan sayfada None doner."""
    eslesen = []  # (bas, son, yol)
    for m in LINK.finditer(s):
        h = HREF.search(m.group(0))
        if h and h.group(1) in TEMA_CSS and re.search(r'rel="(stylesheet|preload)"', m.group(0)):
            eslesen.append((m.start(), m.end(), h.group(1)))
    if [e[2] for e in eslesen] != TEMA_CSS:
        return None
    bas, son = eslesen[0][0], eslesen[-1][1]
    # Araya tema disi bir stil girmisse sira degisir: dokunma.
    ara = s[bas:son]
    for e in eslesen:
        ara = ara.replace(s[e[0]:e[1]], "", 1)
    if STIL_ETIKETI.search(ara):
        return None
    parcalar, onceki = [], 0
    for i, (b, e, _) in enumerate(eslesen):
        parcalar.append(s[onceki:b])
        if i == 0:
            parcalar.append(f'<link rel="stylesheet" href="/{PAKET_CSS}">')
        onceki = e
    parcalar.append(s[onceki:])
    return "".join(parcalar)


JS_DIZI = re.compile(r''.join(
    r'<script\b[^>]*src="/' + re.escape(y) + r'(?:\?[^"]*)?"[^>]*>\s*</script>' + (r'\s*' if i < len(TEMA_JS) - 1 else '')
    for i, y in enumerate(TEMA_JS)), re.I)


def js_cevir(s):
    m = JS_DIZI.search(s)
    if not m:
        return None
    return s[:m.start()] + f'<script src="/{PAKET_JS}"></script>' + s[m.end():]


def calistir(sessiz=False):
    paketleri_uret()
    css_n = js_n = 0
    atlanan = []
    for p in KOK.rglob("*.html"):
        if "scripts" in p.parts or "arsiv" in p.parts or ".git" in p.parts:
            continue
        s = p.read_text(encoding="utf-8", errors="surrogateescape")
        y = s
        if any(f'href="/{c}' in y for c in TEMA_CSS):
            c = css_cevir(y)
            if c is None:
                if "css/bootstrap-az.css" in y:
                    atlanan.append(str(p.relative_to(KOK)))
            else:
                y, css_n = c, css_n + 1
        j = js_cevir(y)
        if j is not None:
            y, js_n = j, js_n + 1
        if y != s:
            p.write_text(y, encoding="utf-8", errors="surrogateescape")
    if not sessiz:
        print(f"paketle: {PAKET_CSS} ({len(TEMA_CSS)} dosya) {css_n} sayfa · {PAKET_JS} ({len(TEMA_JS)} dosya) {js_n} sayfa"
              + (f" · sirasi uymayan {len(atlanan)} sayfa dokunulmadi" if atlanan else ""))
    return atlanan


if __name__ == "__main__":
    for a in calistir():
        print("  dokunulmadi:", a)
