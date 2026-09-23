#!/usr/bin/env python3
# scripts/blog_uygula.py — /blog/ ve /blog/<slug>/ sayfalarini uretir
# (23.09.2026)
#
# Ahmet: "blog tasarimi komple farkli olacak; ana sayfadaki tasarim eski,
# oturmus diye bozmadim; blog UniConnectly web sitesi gibi modern olacak."
#
# Bu yuzden blog sayfalari ana temanin (Edumy) HICBIR varligini yuklemez:
# Bootstrap yok, jQuery yok, tema betikleri yok, style-az.css yok. Sayfa
# css/blog.css + iki yazi tipi + js/blog.js ile ayakta; arama ana siteyle
# ORTAK (js/arama.js), yalniz derisi farkli.
#
# Formuller MathML: scripts/matematik.py LaTeX alt kumesini cevirir,
# tarayici yerel dizer. KaTeX/MathJax yuklenmez (100-300 KB tasarruf).
#
# Kapaklar AVIF ve DEPODA: vercel.json `.webp`yi medya sunucusuna
# yonlendiriyor, `.avif`i yonlendirmiyor (bkz. scripts/blog_gorsel.py).
#
# seo_basliklari.py bu sayfalara DOKUNMAZ; head'i bu betik yazar.
#
# Calistirma sirasi:
#   python3 scripts/blog_uygula.py
#   python3 scripts/sitemap_uret.py
#   python3 scripts/arama_uygula.py
#   python3 scripts/css_surum.py
import html, json, re, sys, pathlib, datetime

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import blog_veri                      # noqa: E402
from matematik import satir as mm     # noqa: E402

ALAN = "https://ahmetcelen.com.tr"
TASLAK = "<!-- blog:taslak -->"
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
KAT = dict(blog_veri.KATEGORILER)
_yt = (KOK / "css/blog-yazitipleri.css").read_text(encoding="utf-8")
ANA_FONT = re.search(r"webfont/(inter-latin-[0-9a-f]+\.woff2)", _yt).group(1)

MENU = [("Ana Sayfa", "/"), ("Ders Notları", "/pdfnot/"), ("Videolar", "/video/"),
        ("Sınavlar", "/sinavlar/"), ("Çıkmış Sorular", "/ss/"), ("Blog", "/blog/")]


def k(s):
    return html.escape(str(s), quote=True)


def tr_tarih(iso):
    y, a, g = (int(x) for x in iso.split("-"))
    return f"{g} {AYLAR[a - 1]} {y}"


def okuma_dk(y):
    metin = " ".join([y["ozet"]] + [p for b in y["bolumler"] for p in b["icerik"]]
                     + [c for _, c in y.get("sss", [])])
    return max(1, round(len(re.sub(r"<[^>]+>", " ", metin).split()) / 190))


def kimlik(baslik):
    t = baslik.lower()
    for a, b in zip("çğıöşü", "cgiosu"):
        t = t.replace(a, b)
    return "b-" + (re.sub(r"[^a-z0-9]+", "-", t).strip("-") or "bolum")


# ── kabuk ────────────────────────────────────────────────────────────────
def kabuk(*, yol, title, desc, govde, jsonld, gorsel=None, onyukle=None, taslak=False):
    adres = ALAN + yol
    og = ALAN + (gorsel or "/blog/kapak/fonksiyonlar-konu-anlatimi.avif")
    menu = "".join(
        f'<a href="{u}"{" class=\"etkin\"" if u == "/blog/" else ""}>{k(a)}</a>'
        for a, u in MENU)
    robots = ("noindex, follow" if taslak else
              "index, follow, max-snippet:-1, max-image-preview:large")
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{k(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{adres}">
<link rel="icon" href="/images/favicon.ico" sizes="128x128">
<link rel="preload" as="font" type="font/woff2" href="/fonts/webfont/{ANA_FONT}" crossorigin>
<link rel="stylesheet" href="/css/blog-yazitipleri.css">
<link rel="stylesheet" href="/css/blog.css">
{onyukle or ""}
<meta property="og:type" content="{'article' if gorsel else 'website'}">
<meta property="og:site_name" content="Ahmet Çelen">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{k(desc)}">
<meta property="og:url" content="{adres}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:image" content="{og}">
<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False, separators=(",", ":"))}</script>
{TASLAK if taslak else ""}
</head>
<body>
<div class="bs-ilerleme" id="ilerleme"></div>
<header class="bs-ust">
  <div class="kap">
    <a class="bs-logo" href="/blog/" aria-label="Ahmet Çelen Blog">
      <img src="/blog/kapak/ac-monogram.avif" alt="" width="34" height="26" decoding="async">
      <span>Ahmet Çelen</span>
    </a>
    <nav class="bs-menu">{menu}
      <button type="button" class="bs-ara" id="search-button" aria-label="Sitede ara">Ara <kbd>/</kbd></button>
    </nav>
  </div>
</header>
<main>
{govde}
</main>
<footer class="bs-alt">
  <div class="kap">
    <p><img class="bs-alt-logo" src="/blog/kapak/ahmet-celen-logo.avif" alt="Ahmet Çelen" width="80" height="80" loading="lazy" decoding="async"><br>Üniversite ve kamu sınavlarına ücretsiz matematik kaynakları</p>
    <nav><a href="/pdfnot/">Ders Notları</a><a href="/video/">Video Çözümler</a><a href="/ss/">Çıkmış Sorular</a><a href="/sinavlar/">Geri Sayımlar</a><a href="/hakkimizda/">Hakkımda</a><a href="/iletisim/">İletişim</a></nav>
  </div>
</footer>
<div class="mk-fullscreen-search-overlay" id="mk-search-overlay">
  <a href="#" class="mk-fullscreen-close" id="mk-fullscreen-close-button" aria-label="Kapat">✕</a>
  <div id="mk-fullscreen-search-wrapper">
    <form method="get" id="mk-fullscreen-searchform" role="search">
      <input type="text" id="mk-fullscreen-search-input" placeholder="Sitede ara…" aria-label="Sitede ara" autocomplete="off">
    </form>
  </div>
</div>
<script src="/js/arama.js"></script>
<script src="/js/blog.js"></script>
</body>
</html>
'''


# ── yazi ─────────────────────────────────────────────────────────────────
def yazi_govde(y, digerleri):
    kat = KAT.get(y["kategori"], y["kategori"])
    toc = "".join(f'<li><a href="#{kimlik(b["baslik"])}">{k(b["baslik"])}</a></li>'
                  for b in y["bolumler"])
    govde = ""
    for b in y["bolumler"]:
        icerik = "\n".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in b["icerik"])
        govde += (f'<h2 id="{kimlik(b["baslik"])}">{k(b["baslik"])}</h2>\n' + icerik + "\n")

    ek = ""
    if y.get("sss"):
        ek += ('<h2 id="b-sss">Sık sorulanlar</h2>\n<div class="bs-sss">'
               + "".join(f"<details><summary>{k(s)}</summary><p>{mm(c)}</p></details>"
                         for s, c in y["sss"]) + "</div>\n")
        toc += '<li><a href="#b-sss">Sık sorulanlar</a></li>'
    if y.get("kontrol"):
        ek += ('<h2 id="b-kontrol">Kontrol listesi</h2>\n<ul class="bs-kontrol">'
               + "".join(f"<li>{mm(m)}</li>" for m in y["kontrol"]) + "</ul>\n")
        toc += '<li><a href="#b-kontrol">Kontrol listesi</a></li>'
    if y.get("kaynaklar"):
        ek += ('<h2 id="b-kaynaklar">Kaynaklar</h2>\n<ul class="bs-kaynaklar">'
               + "".join(f'<li><a href="{k(u)}" target="_blank" rel="noopener noreferrer">{k(a)}</a></li>'
                         for a, u in y["kaynaklar"]) + "</ul>\n")
    if digerleri:
        ek += ('<h2>Bunlar da ilgini çekebilir</h2>\n<div class="bs-ilgili">'
               + "".join(f'<a href="/blog/{k(d["slug"])}/"><strong>{k(d["baslik"])}</strong>'
                         f'<span>{k(d["aciklama"])}</span></a>' for d in digerleri) + "</div>\n")

    guncel = (f' · Güncellendi <time datetime="{k(y["guncelleme"])}">{tr_tarih(y["guncelleme"])}</time>'
              if y.get("guncelleme") else "")
    rozet = "".join(f'<span class="bs-rozet">{k(s)}</span>' for s in y.get("sinavlar", []))
    kapak = ""
    if y.get("kapak"):
        kapak = (f'<img class="bs-kapak" src="/blog/kapak/{k(y["kapak"])}.avif" '
                 f'alt="{k(y.get("kapak_alt", y["baslik"]))}" width="1600" height="901" '
                 f'fetchpriority="high" decoding="async">')
    return f'''
<div class="kap bs-yazi-ust">
  <p class="bs-kirinti"><a href="/">Ana Sayfa</a> / <a href="/blog/">Blog</a> / {k(kat)}</p>
</div>
<div class="kap bs-duzen">
  <article class="bs-icerik">
    <span class="bs-etiket">{k(kat)}</span>
    <h1 class="bs-baslik">{k(y["baslik"])}</h1>
    <p class="bs-kunye">{rozet}<time datetime="{k(y["tarih"])}">{tr_tarih(y["tarih"])}</time>{guncel} · {okuma_dk(y)} dakikalık okuma</p>
    {kapak}
    <p class="bs-ozet">{mm(k(y["ozet"]))}</p>
    <hr class="bs-ayrac">
{mm(govde)}{mm(ek)}
  </article>
  <aside class="bs-yan">
    <nav class="bs-toc" aria-label="İçindekiler"><p>İçindekiler</p><ol>{toc}</ol></nav>
  </aside>
</div>
'''


# ── hub ──────────────────────────────────────────────────────────────────
def hub_govde(yazilar):
    if not yazilar:
        return ('<div class="kap bs-hero"><h1>Blog</h1>'
                '<p class="bs-bos">İlk yazı hazırlanıyor.</p></div>')
    kullanilan = [x for x in blog_veri.KATEGORILER if any(y["kategori"] == x[0] for y in yazilar)]
    suzgec = ('<button data-kat="*" aria-pressed="true">Tümü</button>'
              + "".join(f'<button data-kat="{a}" aria-pressed="false">{k(ad)}</button>'
                        for a, ad in kullanilan))
    kartlar = "".join(f'''<article class="bs-kart" data-kat="{k(y["kategori"])}">
        <span class="bs-etiket">{k(KAT.get(y["kategori"], y["kategori"]))}</span>
        <h2><a href="/blog/{k(y["slug"])}/">{k(y["baslik"])}</a></h2>
        <p>{k(y["aciklama"])}</p>
        <p class="bs-kunye">{"".join(f'<span class="bs-rozet">{k(s)}</span>' for s in y.get("sinavlar", []))}<time datetime="{k(y["tarih"])}">{tr_tarih(y["tarih"])}</time> · {okuma_dk(y)} dk</p>
      </article>''' for y in yazilar)
    return f'''
<div class="kap bs-hero">
  <h1>Matematik Konu Anlatımı</h1>
  <p>Üniversite ve kamu sınavlarına hazırlananlar için baştan sona konu anlatımı, hap bilgiler ve çözümlü örnekler. Tamamı ücretsiz.</p>
</div>
<div class="kap"><div class="bs-suzgec">{suzgec}</div><div class="bs-izgara">{kartlar}</div></div>
'''


# ── JSON-LD ──────────────────────────────────────────────────────────────
KISI = {"@type": "Person", "@id": ALAN + "/#kisi", "name": "Ahmet Çelen", "url": ALAN + "/hakkimizda/"}


def jsonld_yazi(y):
    yol = f"{ALAN}/blog/{y['slug']}/"
    g = [{"@type": "BlogPosting", "headline": y["baslik"], "description": y["aciklama"],
          "url": yol, "mainEntityOfPage": yol, "inLanguage": "tr-TR",
          "datePublished": y["tarih"], "dateModified": y.get("guncelleme") or y["tarih"],
          "author": {"@id": ALAN + "/#kisi"}, "publisher": {"@id": ALAN + "/#kisi"},
          "isAccessibleForFree": True,
          "image": ALAN + f"/blog/kapak/{y['kapak']}.avif" if y.get("kapak") else None},
         KISI,
         {"@type": "BreadcrumbList", "itemListElement": [
             {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": ALAN + "/"},
             {"@type": "ListItem", "position": 2, "name": "Blog", "item": ALAN + "/blog/"},
             {"@type": "ListItem", "position": 3, "name": y["baslik"], "item": yol}]}]
    g[0] = {a: b for a, b in g[0].items() if b is not None}
    if y.get("sss"):
        g.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": s,
             "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"\$[^$]*\$", "…", c)}}
            for s, c in y["sss"]]})
    return {"@context": "https://schema.org", "@graph": g}


def jsonld_hub(yazilar):
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": ALAN + "/blog/", "url": ALAN + "/blog/",
         "name": "Ahmet Çelen Blog · Matematik Konu Anlatımı", "inLanguage": "tr-TR",
         "author": {"@id": ALAN + "/#kisi"},
         "blogPost": [{"@type": "BlogPosting", "headline": y["baslik"],
                       "url": f"{ALAN}/blog/{y['slug']}/", "datePublished": y["tarih"]}
                      for y in yazilar]},
        KISI,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": ALAN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": ALAN + "/blog/"}]}]}


def yaz(yol_dosya, icerik):
    p = KOK / yol_dosya
    eski = p.read_text(encoding="utf-8") if p.exists() else ""
    if icerik != eski:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(icerik, encoding="utf-8")
    return icerik != eski


def uygula():
    yazilar = sorted(blog_veri.yayinda(), key=lambda y: y["tarih"], reverse=True)
    for y in yazilar:
        assert len(y["aciklama"]) <= 160, (y["slug"], len(y["aciklama"]))
    n = 0
    for y in yazilar:
        secili = [d for d in yazilar if d["slug"] in (y.get("ilgili") or [])]
        digerleri = (secili or [d for d in yazilar if d["slug"] != y["slug"]])[:3]
        onyukle = (f'<link rel="preload" as="image" href="/blog/kapak/{y["kapak"]}.avif" fetchpriority="high">'
                   if y.get("kapak") else None)
        n += yaz(f"blog/{y['slug']}/index.html", kabuk(
            yol=f"/blog/{y['slug']}/", title=f"{y['baslik']} - Ahmet Çelen",
            desc=y["aciklama"], govde=yazi_govde(y, digerleri), jsonld=jsonld_yazi(y),
            gorsel=f"/blog/kapak/{y['kapak']}.avif" if y.get("kapak") else None,
            onyukle=onyukle))
    n += yaz("blog/index.html", kabuk(
        yol="/blog/", title="Matematik Konu Anlatımı Blog - Ahmet Çelen",
        desc="TYT, AYT, ALES ve KPSS için baştan sona matematik konu anlatımı; hap bilgiler, çözümlü örnekler ve grafiklerle. Ücretsiz.",
        govde=hub_govde(yazilar), jsonld=jsonld_hub(yazilar), taslak=not yazilar))
    print(f"blog: {len(yazilar)} yazi · {n} dosya yazildi"
          + ("" if yazilar else " · hub TASLAK (noindex)"))


if __name__ == "__main__":
    uygula()
