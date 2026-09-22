#!/usr/bin/env python3
# scripts/seo_basliklari.py — her icerik sayfasina canonical + og + twitter +
# robots meta ekler (22.09.2026).
#
# NEDEN: denetimde sitede HIC canonical, og:* ya da twitter:card yoktu.
#   · canonical yoklugu: GSC'de `/ss/tyt` ve `/ss/tyt/` AYRI sayfa olarak
#     raporlaniyordu (31 + 20 gosterim) — sinyal bolunuyor.
#   · `max-snippet:-1, max-image-preview:large` Google'in daha uzun ozet ve
#     buyuk gorsel gostermesine izin verir; TO'yu dogrudan etkiler.
#     (GSC 22.09: /sinavlar/msu/ 31.850 gosterim, TO %0,16.)
#   · og/twitter yalniz sosyal degil; dil modelleri de sayfayi bu alanlardan
#     ozetliyor.
#
# KURAL: <title>, <h1>/<h2> ve URL'lere DOKUNULMAZ. Bu betik yalniz <head>
# icine meta ekler; mevcut meta'lari (keywords/description) korur.
#
# Idempotent: blok "<!-- seo:bas -->" ile "<!-- seo:son -->" arasinda tutulur,
# her calistirmada yeniden yazilir.
#
# Kullanim: python3 scripts/seo_basliklari.py [--kuru]
import re, sys, pathlib, html

KOK = pathlib.Path(__file__).resolve().parent.parent
ALAN = "https://ahmetcelen.com.tr"
KURU = "--kuru" in sys.argv
BAS, SON = "<!-- seo:bas -->", "<!-- seo:son -->"

# sitemap_uret.py ile AYNI kapsam: sitemap'e giren sayfa seo basligini da alir.
sys.path.insert(0, str(KOK / "scripts"))
from sitemap_uret import HARIC_ON_EK, HARIC_AD, HARIC_PARCA, HARIC_DESEN, yonlendirme_mi  # noqa: E402

# Sayfaya ozel paylasim gorseli; yoksa site geneli.
OG_GORSEL = {
    "/ss/": "/images/ss-kart.webp",
}
OG_VARSAYILAN = "/images/about/3.jpg"

def yol_of(p):
    r = p.relative_to(KOK).as_posix()
    if p.name == "index.html":
        return "/" if p.parent == KOK else "/" + p.parent.relative_to(KOK).as_posix() + "/"
    return "/" + r

def sayfalar():
    for p in sorted(KOK.rglob("*.html")):
        r = p.relative_to(KOK).as_posix()
        if r.startswith(HARIC_ON_EK) or p.name in HARIC_AD or HARIC_DESEN.match(p.name):
            continue
        if any(x in "/" + r for x in HARIC_PARCA) or yonlendirme_mi(p):
            continue
        yield p

def gorsel_of(yol):
    for on, g in OG_GORSEL.items():
        if yol.startswith(on):
            return g
    return OG_VARSAYILAN

def blok(p, yol):
    s = p.read_text(encoding="utf-8")
    tm = re.search(r"<title>(.*?)</title>", s, re.S)
    title = html.escape(re.sub(r"\s+", " ", tm.group(1)).strip(), quote=True) if tm else "Ahmet Çelen"
    dm = re.search(r'<meta name="description" content="([^"]*)"', s)
    desc = dm.group(1).strip() if dm else ""
    adres = ALAN + yol
    g = ALAN + gorsel_of(yol)
    satirlar = [
        BAS,
        # Font: style.css'teki @import kaldirildi (zincirleme istek). Burada
        # paralel yuklenir; display=swap metnin fontu beklemesini onler.
        '<link rel="preconnect" href="https://fonts.googleapis.com">',
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>',
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:400,500,600,700|Open+Sans&display=swap" media="print" onload="this.media=\'all\'">',
        '<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Nunito:400,500,600,700|Open+Sans&display=swap"></noscript>',
        # LCP ogesi her ic sayfada ayni: baslik bandinin arka plan gorseli.
        '<link rel="preload" as="image" href="/images/background/inner-pagebg.webp" fetchpriority="high" media="(min-width: 992px)">',
        '<link rel="preload" as="image" href="/images/background/inner-pagebg-960.webp" fetchpriority="high" media="(max-width: 991px)">',
        # Ikon fontlari kritik degil: render'i bloklamadan yuklensinler.
        '<link rel="preload" as="style" href="/css/font-awesome.min.css" onload="this.rel=\'stylesheet\'">',
        '<link rel="preload" as="style" href="/css/flaticon.css" onload="this.rel=\'stylesheet\'">',
        f'<link rel="canonical" href="{adres}">',
        # Uzun ozet + buyuk gorsel izni (TO). Varsayilan snippet 155-160 karakterde kesiliyor.
        '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">',
        '<meta property="og:type" content="website">',
        '<meta property="og:site_name" content="Ahmet Çelen">',
        '<meta property="og:locale" content="tr_TR">',
        f'<meta property="og:title" content="{title}">',
    ]
    if desc:
        satirlar.append(f'<meta property="og:description" content="{desc}">')
    satirlar += [
        f'<meta property="og:url" content="{adres}">',
        f'<meta property="og:image" content="{g}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{title}">',
    ]
    if desc:
        satirlar.append(f'<meta name="twitter:description" content="{desc}">')
    satirlar += [f'<meta name="twitter:image" content="{g}">', SON]
    return "\n".join(satirlar) + "\n"

def uygula():
    yazilan = atlanan = 0
    for p in sayfalar():
        s = p.read_text(encoding="utf-8")
        if "</head>" not in s:
            atlanan += 1
            continue
        yeni_blok = blok(p, yol_of(p))
        if BAS in s and SON in s:
            a, b = s.index(BAS), s.index(SON) + len(SON) + 1
            t = s[:a] + yeni_blok + s[b:]
        else:
            t = s.replace("</head>", yeni_blok + "</head>", 1)
        if t != s and not KURU:
            p.write_text(t, encoding="utf-8")
            yazilan += 1
        elif t != s:
            yazilan += 1
    print(f"seo basliklari: {yazilan} sayfa yazildi, {atlanan} atlandi (</head> yok)")

if __name__ == "__main__":
    uygula()
