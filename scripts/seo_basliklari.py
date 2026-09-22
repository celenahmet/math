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

# On yuklenecek yazi tipi: govde fontu Nunito'nun latin altkumesi.
# Adi icerik ozeti tasir; css/yazitipleri.css'ten okunur ki elle guncelleme
# gerekmesin.
_yt = (KOK / "css/yazitipleri.css").read_text(encoding="utf-8")
ANA_FONT = re.search(r"webfont/(nunito-latin-[0-9a-f]+\.woff2)", _yt).group(1)

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
    hero = "home1-mainslider" in s
    satirlar = [
        BAS,
        # Yazi tipleri 22.09'da KENDI SUNUCUMUZA alindi
        # (scripts/yazitipi_yerel.py). Once fonts.googleapis.com'dan CSS,
        # fonts.gstatic.com'dan dosya geliyordu: mobilde iki ayri kaynak icin
        # DNS + TCP + TLS ve font istegi CSS inmeden baslayamiyordu.
        # Dosya adi icerik ozeti tasidigi icin surum eki gerekmez.
        f'<link rel="preload" as="font" type="font/woff2" href="/fonts/webfont/{ANA_FONT}" crossorigin>',
        '<link rel="stylesheet" href="/css/yazitipleri.css">',
        # LCP ogesi sayfa tipine gore degisir; yanlis gorseli on yuklemek
        # hem bos yere bant genisligi harcar hem GERCEK LCP'yi geciktirir.
        # 22.09: ana sayfa ve /video/ hero slayti kullaniyor, ic sayfalar
        # baslik bandinin arka planini.
    ] + (
        ['<link rel="preload" as="image" href="/images/home/1.webp" fetchpriority="high">']
        if hero else [
        '<link rel="preload" as="image" href="/images/background/inner-pagebg.webp" fetchpriority="high" media="(min-width: 992px)">',
        '<link rel="preload" as="image" href="/images/background/inner-pagebg-960.webp" fetchpriority="high" media="(max-width: 991px)">',
    ]) + [
        # Ikon fontlari kritik degil: render'i bloklamadan yuklensinler.
        # 22.09: -az surumleri yalniz sitede GECEN ikonlari tasir
        # (scripts/ikon_azalt.py): 131 KB → 10 KB.
        '<link rel="preload" as="style" href="/css/font-awesome-az.css" onload="this.rel=\'stylesheet\'">',
        '<link rel="preload" as="style" href="/css/flaticon-az.css" onload="this.rel=\'stylesheet\'">',
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
