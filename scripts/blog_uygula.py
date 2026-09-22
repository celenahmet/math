#!/usr/bin/env python3
# scripts/blog_uygula.py — /blog/ ve /blog/<slug>/ sayfalarini uretir
# (22.09.2026)
#
# Ahmet: "uniconnectly'deki gibi blog sayfasi kuracagiz." UniConnectly
# blogunun yapisi ornek alindi (22.09'da okundu): yazi listesi + kategori
# suzgeci; yazi sayfasinda icindekiler → bolumler → sik sorulanlar →
# kontrol listesi → ozet → kaynaklar → ilgili yazilar. TASARIM bu sitenin
# kendi temasi (Edumy); UniConnectly'nin gorunumu kopyalanmaz.
#
# Iskelet ss/kpss/index.html'den alinir (sinav_sayfa_uygula.py ile ayni
# yontem): <head> + ust menu + mobil menu bas tarafta, alt bilgi + betikler
# son tarafta; arasina yazi govdesi konur.
#
# ⚠️ HENUZ YAZI YOKKEN: hub sayfasi "<!-- blog:taslak -->" isareti tasir.
# Bu isareti tasiyan sayfa sitemap'e GIRMEZ ve robots meta'si "noindex"
# olur (scripts/sitemap_uret.py + scripts/seo_basliklari.py). Boylece bos
# bir sayfa aramaya dusmez ama adres canlida gorulebilir.
#
# Calistirma sirasi (yazi ekledikten sonra):
#   python3 scripts/blog_uygula.py
#   python3 scripts/seo_basliklari.py
#   python3 scripts/sitemap_uret.py
#   python3 scripts/arama_uygula.py
#   python3 scripts/css_surum.py
import html, json, re, sys, pathlib, datetime

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import blog_veri  # noqa: E402
import uniconnectly_blok  # noqa: E402

ALAN = "https://ahmetcelen.com.tr"
TASLAK = "<!-- blog:taslak -->"
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
KAT = dict(blog_veri.KATEGORILER)

ISKELET = (KOK / "ss/kpss/index.html").read_text(encoding="utf-8")
BAS = ISKELET[:ISKELET.index("\t<!-- Inner Page Breadcrumb -->")]
SON = ISKELET[ISKELET.index('\t<section class="footer_one">'):]
assert '<link rel="stylesheet" href="/css/duzeltmeler.css' in BAS and "</body>" in SON


def k(s):
    return html.escape(str(s), quote=True)


def tr_tarih(iso):
    y, a, g = (int(x) for x in iso.split("-"))
    return f"{g} {AYLAR[a - 1]} {y}"


def okuma_dk(y):
    kelime = len(re.sub(r"<[^>]+>", " ", " ".join(
        [y["ozet"]] + [p for b in y["bolumler"] for p in b["icerik"]]
        + [c for _, c in y.get("sss", [])])).split())
    return max(1, round(kelime / 200))


def kimlik(baslik):
    """H2 metninden ic baglanti kimligi (icindekiler icin)."""
    t = baslik.lower()
    for a, b in zip("çğıöşü", "cgiosu"):
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9]+", "-", t).strip("-")
    return "b-" + (t or "bolum")


# ── yazi sayfasi ─────────────────────────────────────────────────────────
def yazi_govde(y, digerleri):
    kat = KAT.get(y["kategori"], y["kategori"])
    bolumler = y["bolumler"]
    icindekiler = "".join(
        f'<li><a href="#{kimlik(b["baslik"])}">{k(b["baslik"])}</a></li>' for b in bolumler)
    govde = "".join(
        f'<h2 id="{kimlik(b["baslik"])}" class="blog-h2">{k(b["baslik"])}</h2>\n'
        + "\n".join(b["icerik"]) + "\n" for b in bolumler)

    sss = ""
    if y.get("sss"):
        sss = ('<h2 id="b-sss" class="blog-h2">Sık sorulanlar</h2>\n<div class="blog-sss">'
               + "".join(f"<details><summary>{k(s)}</summary><p>{k(c)}</p></details>"
                         for s, c in y["sss"]) + "</div>\n")
    kontrol = ""
    if y.get("kontrol"):
        kontrol = ('<h2 id="b-kontrol" class="blog-h2">Kontrol listesi</h2>\n<ul class="blog-kontrol">'
                   + "".join(f"<li>{k(m)}</li>" for m in y["kontrol"]) + "</ul>\n")
    kaynaklar = ""
    if y.get("kaynaklar"):
        # Kaynaklar YALNIZ resmi kaynaga gider; ic baglanti buraya konmaz.
        kaynaklar = ('<h2 id="b-kaynaklar" class="blog-h2">Kaynaklar</h2>\n<ul class="blog-kaynaklar">'
                     + "".join(f'<li><a href="{k(u)}" target="_blank" rel="noopener noreferrer">{k(a)}</a></li>'
                               for a, u in y["kaynaklar"]) + "</ul>\n")
    ilgili = ""
    if digerleri:
        ilgili = ('<h2 class="blog-h2">Bunlar da ilgini çekebilir</h2>\n<div class="blog-ilgili">'
                  + "".join(f'<a href="/blog/{k(d["slug"])}/"><strong>{k(d["baslik"])}</strong>'
                            f'<span>{k(d["aciklama"])}</span></a>' for d in digerleri) + "</div>\n")

    guncel = (f' · Güncellendi: <time datetime="{k(y["guncelleme"])}">{tr_tarih(y["guncelleme"])}</time>'
              if y.get("guncelleme") else "")
    return f'''
	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-8 offset-xl-2 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">Blog</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/blog/">Blog</a></li>
						    <li class="breadcrumb-item active" aria-current="page">{k(kat)}</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- scripts/blog_uygula.py uretir; icerik scripts/blog_veri.py -->
	<section class="blog-sayfa">
		<div class="container">
			<article class="blog-yazi">
				<h1 class="blog-baslik">{k(y["baslik"])}</h1>
				<p class="blog-kunye"><span class="blog-kat">{k(kat)}</span>
					<time datetime="{k(y["tarih"])}">{tr_tarih(y["tarih"])}</time>{guncel}
					· {okuma_dk(y)} dakikalık okuma</p>
				<p class="blog-ozet">{k(y["ozet"])}</p>
				<nav class="blog-icindekiler" aria-label="İçindekiler">
					<p>İçindekiler</p>
					<ol>{icindekiler}</ol>
				</nav>
{govde}{sss}{kontrol}{kaynaklar}{ilgili}
			</article>
		</div>
	</section>
''' + uniconnectly_blok.blok(f"blog-{y['slug']}", "kampus")


# ── hub ──────────────────────────────────────────────────────────────────
def hub_govde(yazilar):
    if yazilar:
        kartlar = "".join(
            f'''<article class="blog-kart">
					<span class="blog-kat">{k(KAT.get(y["kategori"], y["kategori"]))}</span>
					<h3><a href="/blog/{k(y["slug"])}/">{k(y["baslik"])}</a></h3>
					<p>{k(y["aciklama"])}</p>
					<p class="blog-kunye"><time datetime="{k(y["tarih"])}">{tr_tarih(y["tarih"])}</time> · {okuma_dk(y)} dk</p>
				</article>''' for y in yazilar)
        liste = f'<div class="blog-liste">{kartlar}</div>'
        kullanilan = [x for x in blog_veri.KATEGORILER if any(y["kategori"] == x[0] for y in yazilar)]
        kategoriler = ('<div class="blog-kategoriler">'
                       + "".join(f'<span>{k(ad)}</span>' for _, ad in kullanilan) + "</div>")
    else:
        # Bos durum metni GECICI: ilk yazi gelince kalkar. Sayfa bu haldeyken
        # "<!-- blog:taslak -->" tasidigi icin aramaya dusmez.
        liste = '<p class="blog-bos">İlk yazı hazırlanıyor.</p>'
        kategoriler = ""
    return f'''
	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-8 offset-xl-2 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">Blog</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/">Ana Sayfa</a></li>
						    <li class="breadcrumb-item active" aria-current="page">Blog</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- scripts/blog_uygula.py uretir; icerik scripts/blog_veri.py -->
	<section class="blog-sayfa">
		<div class="container">
			<div class="main-title">
				<h2 class="mt0">Blog</h2>
			</div>
			{kategoriler}
			{liste}
		</div>
	</section>
''' + uniconnectly_blok.blok("blog-hub", "kampus")


# ── JSON-LD ──────────────────────────────────────────────────────────────
KISI = {"@type": "Person", "@id": ALAN + "/#kisi", "name": "Ahmet Çelen", "url": ALAN + "/hakkimizda/"}


def jsonld_yazi(y):
    yol = f"{ALAN}/blog/{y['slug']}/"
    g = [{
        "@type": "BlogPosting", "headline": y["baslik"], "description": y["aciklama"],
        "url": yol, "mainEntityOfPage": yol, "inLanguage": "tr-TR",
        "datePublished": y["tarih"],
        "dateModified": y.get("guncelleme") or y["tarih"],
        "author": {"@id": ALAN + "/#kisi"}, "publisher": {"@id": ALAN + "/#kisi"},
        "isAccessibleForFree": True,
    }, KISI, {
        "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": ALAN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": ALAN + "/blog/"},
            {"@type": "ListItem", "position": 3, "name": y["baslik"], "item": yol}]}]
    if y.get("sss"):
        g.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": s,
             "acceptedAnswer": {"@type": "Answer", "text": c}} for s, c in y["sss"]]})
    return {"@context": "https://schema.org", "@graph": g}


def jsonld_hub(yazilar):
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "Blog", "@id": ALAN + "/blog/", "url": ALAN + "/blog/", "name": "Ahmet Çelen Blog",
         "inLanguage": "tr-TR", "author": {"@id": ALAN + "/#kisi"},
         "blogPost": [{"@type": "BlogPosting", "headline": y["baslik"],
                       "url": f"{ALAN}/blog/{y['slug']}/", "datePublished": y["tarih"]} for y in yazilar]},
        KISI,
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": ALAN + "/"},
            {"@type": "ListItem", "position": 2, "name": "Blog", "item": ALAN + "/blog/"}]}]}


# ── yazma ────────────────────────────────────────────────────────────────
def yaz(yol, title, desc, keywords, govde, veri, taslak=False):
    bas = BAS
    bas = re.sub(r"<title>.*?</title>", lambda m: f"<title>{title}</title>", bas, count=1, flags=re.S)
    bas = re.sub(r'<meta name="keywords" content="[^"]*">',
                 lambda m: f'<meta name="keywords" content="{k(keywords)}">', bas, count=1)
    bas = re.sub(r'<meta name="description" content="[^"]*">',
                 lambda m: f'<meta name="description" content="{k(desc)}">', bas, count=1)
    bas = bas.replace('<html dir="ltr" lang="en">', '<html dir="ltr" lang="tr">')
    # Iskeletten gelen JSON-LD blogu bu sayfaya ait DEGIL; kendi grafigimizle degistir.
    blok = ('<!-- jsonld:bas -->\n<script type="application/ld+json">'
            + json.dumps(veri, ensure_ascii=False, separators=(",", ":"))
            + "</script>\n<!-- jsonld:son -->\n")
    if "<!-- jsonld:bas -->" in bas:
        a = bas.index("<!-- jsonld:bas -->")
        b = bas.index("<!-- jsonld:son -->") + len("<!-- jsonld:son -->") + 1
        bas = bas[:a] + blok + bas[b:]
    else:
        bas = bas.replace("</head>", blok + "</head>", 1)
    if taslak:
        bas = bas.replace("</head>", TASLAK + "\n</head>", 1)

    son = SON if "uniconnectly-blok.js" in SON else SON.replace(
        '<script type="text/javascript" src="/js/script.js"></script>',
        '<script type="text/javascript" src="/js/script.js"></script>\n<script src="/js/uniconnectly-blok.js"></script>')
    p = KOK / yol
    eski = p.read_text(encoding="utf-8") if p.exists() else ""
    yeni = bas + govde + son
    if yeni != eski:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(yeni, encoding="utf-8")
    return yeni != eski


def uygula():
    yazilar = sorted(blog_veri.yayinda(), key=lambda y: y["tarih"], reverse=True)
    for y in yazilar:
        assert len(y["aciklama"]) <= 160, (y["slug"], len(y["aciklama"]))
    n = 0
    for y in yazilar:
        digerleri = [d for d in yazilar if d["slug"] != y["slug"]][:3]
        n += yaz(f"blog/{y['slug']}/index.html",
                 f"{y['baslik']} - Ahmet Çelen", y["aciklama"],
                 f"{KAT.get(y['kategori'], y['kategori'])}, blog, ahmet çelen",
                 yazi_govde(y, digerleri), jsonld_yazi(y))
    n += yaz("blog/index.html", "Blog - Ahmet Çelen",
             "Sınavlar, çalışma yöntemi ve matematik üzerine yazılar.",
             "blog, sınav, matematik, çalışma yöntemi",
             hub_govde(yazilar), jsonld_hub(yazilar), taslak=not yazilar)
    durum = "TASLAK (noindex, sitemap disi)" if not yazilar else "yayinda"
    print(f"blog: {len(yazilar)} yazi · hub {durum} · {n} dosya yazildi")


if __name__ == "__main__":
    uygula()
