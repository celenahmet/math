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
from blog_ikon import ikon            # noqa: E402
import blog_yan                      # noqa: E402
from matematik import satir as mm     # noqa: E402

ALAN = "https://ahmetcelen.com.tr"
TASLAK = "<!-- blog:taslak -->"
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
KAT = blog_veri.KAT_AD
_yt = (KOK / "css/blog-yazitipleri.css").read_text(encoding="utf-8")
ANA_FONT = re.search(r"webfont/(inter-latin-[0-9a-f]+\.woff2)", _yt).group(1)

MENU = [("Tüm Yazılar", "/blog/"), ("Konular", "/blog/#konular"),
        ("Sınavlar", "/blog/#sinavlar"), ("Ders Notları", "/pdfnot/"),
        ("Ana Site", "/")]


def k(s):
    return html.escape(str(s), quote=True)


def tr_tarih(iso):
    y, a, g = (int(x) for x in iso.split("-"))
    return f"{g} {AYLAR[a - 1]} {y}"


def _duz(metin):
    """Etiketleri siler. Once formul icindeki < ve > bosluga cevrilir: $x<2$
    gibi bir formul etiket basi sanilip bir sonraki > isaretine kadar olan
    METNI siliyordu (24.09 olculdu, kelime sayisi dusuk cikiyordu)."""
    metin = re.sub(r"\$[^$]*\$", lambda m: m.group(0).replace("<", " ").replace(">", " "), metin)
    return re.sub(r"<[^>]+>", " ", metin)


def kelime_sayisi(y):
    metin = " ".join([y["ozet"]] + [p for b in y["bolumler"] for p in b["icerik"]]
                     + [c for _, c in y.get("sss", [])] + list(y.get("kontrol", [])))
    return len(_duz(metin).split())


def okuma_dk(y):
    metin = " ".join([y["ozet"]] + [p for b in y["bolumler"] for p in b["icerik"]]
                     + [c for _, c in y.get("sss", [])])
    return max(1, round(len(_duz(metin).split()) / 190))


def kat_rozet(anahtar, sinif="bs-etiket"):
    """Kategori rozeti. Renk satir ici degisken olarak geciyor; her
    kategori kendi rengini tasisin diye (CSS'te altti kategori icin ayri
    kural yazmak yerine tek kural + degisken)."""
    return (f'<span class="{sinif}" style="--kat:{blog_veri.KAT_RENK.get(anahtar, "#1860f0")}">'
            + ikon(blog_veri.KAT_IKON.get(anahtar, "fonksiyonlar"))
            + k(KAT.get(anahtar, anahtar)) + "</span>")


def bolum_basligi(kimlik_, ikon_adi, metin):
    return f'<h2 id="{kimlik_}" class="bs-h2-ikon">{ikon(ikon_adi)}{k(metin)}</h2>\n'


def hap_ozeti(govde):
    """Yazidaki butun hap bilgileri sayfanin sonunda tek listede toplar.
    Ahmet (23.09): ogrenci yaziyi bitirince ya da sinav oncesi yalniz bu
    bolumu okusun. Ozet ELLE yazilmaz, kutulardan uretilir; boylece
    metin degisince ozet de kendiliginden degisir."""
    parcalar = re.findall(r'<div class="bs-hap-ic">(.*?)</div>', govde, re.S)
    if not parcalar:
        return "", ""
    liste = "".join(f"<li>{x}</li>" for x in parcalar)
    return (bolum_basligi("b-hap-ozet", "hap", "Hap bilgi özeti")
            + f'<ol class="bs-hap-ozet">{liste}</ol>\n',
            '<li><a href="#b-hap-ozet">Hap bilgi özeti</a></li>')


def kimlik(baslik):
    t = baslik.lower()
    for a, b in zip("çğıöşü", "cgiosu"):
        t = t.replace(a, b)
    return "b-" + (re.sub(r"[^a-z0-9]+", "-", t).strip("-") or "bolum")


# ── kabuk ────────────────────────────────────────────────────────────────
def kabuk(*, yol, title, desc, govde, jsonld, gorsel=None, onyukle=None, taslak=False, gorsel_alt=None):
    adres = ALAN + yol
    og = ALAN + (gorsel or "/blog/kapak/fonksiyonlar-konu-anlatimi.avif")
    menu = "".join(
        f'<a href="{u}"{" class=\"etkin\"" if u == "/blog/" and yol == "/blog/" else ""}>{k(a)}</a>'
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
{gorsel_alt or ""}
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
    <p><img class="bs-alt-logo" src="/blog/kapak/ahmet-celen-logo.avif" alt="" width="80" height="80" loading="lazy" decoding="async"><span>Üniversite ve kamu sınavlarına ücretsiz matematik kaynakları</span></p>
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
    _ozet, _ozet_toc = hap_ozeti(govde)
    ek += _ozet
    toc += _ozet_toc
    if y.get("sss"):
        ek += (bolum_basligi("b-sss", "sss", "Sık sorulanlar") + '<div class="bs-sss">'
               + "".join(f"<details><summary>{k(s)}</summary><p>{mm(c)}</p></details>"
                         for s, c in y["sss"]) + "</div>\n")
        toc += '<li><a href="#b-sss">Sık sorulanlar</a></li>'
    if y.get("kontrol"):
        # Tiklanabilir kontrol listesi (Ahmet 23.09). Isaretler tarayicida
        # saklanir (js/blog.js, localStorage); sunucuya hicbir sey gitmez.
        # JS calismazsa liste yine okunur kalir: kutular islevsiz ama
        # maddeler gorunur.
        n = len(y["kontrol"])
        maddeler = "".join(
            f'<li><label><input type="checkbox" data-i="{i}">'
            f'<span class="bs-kutu">{ikon("kontrol") if False else ""}</span>'
            f'<span class="bs-madde">{mm(m)}</span></label></li>'
            for i, m in enumerate(y["kontrol"]))
        ek += (bolum_basligi("b-kontrol", "kontrol", "Kontrol listesi")
               + f'<div class="bs-kontrol-sar" data-yazi="{k(y["slug"])}" data-toplam="{n}">'
               + '<div class="bs-kontrol-ust">'
               + f'<p class="bs-kontrol-durum"><strong>0</strong> / {n} tamamlandı</p>'
               + '<button type="button" class="bs-kontrol-sifirla" hidden>Sıfırla</button></div>'
               + '<div class="bs-kontrol-cubuk"><span style="width:0%"></span></div>'
               + f'<ul class="bs-kontrol">{maddeler}</ul>'
               # Hepsi isaretlenince gorunur (Ahmet 23.09: "10/10 olunca
               # tebrikler tarzi bir sey donebilir"). Metin varsayilan.
               + '<p class="bs-kontrol-tebrik" hidden>' + ikon("kontrol")
               + "Tebrikler, bu konunun kontrol listesini tamamladın.</p></div>\n")
        toc += '<li><a href="#b-kontrol">Kontrol listesi</a></li>'
    # ⚠️ KAYNAKLAR YAYINDA GOSTERILMIYOR (Ahmet, 23.09): "kaynaklar kismini
    # not alalim ama yayinda gostermeyelim, kendi icimizde denetim icin
    # kullanalim; MEB sorularini kullanmak yasak olabilir cunku."
    # Kaynaklar veride (scripts/yazilar/*.py) DURUYOR ve
    # scripts/blog_kaynak_denetimi.py ile ic rapora yaziliyor; sayfaya
    # basilmiyor. Rapor da .vercelignore ile yayin disinda.
    if digerleri:
        ek += (bolum_basligi("b-ilgili", "ilgili", "Bunlar da ilgini çekebilir") + '<div class="bs-ilgili">'
               + "".join(f'<a href="/blog/{k(d["slug"])}/">'
                         # Kapak (Ahmet 23.09: "onerilen yazilarda da gorseller gozuksun").
                         # Baglantinin adi basliktan geliyor; gorsel sus: alt="".
                         + (f'<img class="bs-ilgili-gorsel" src="/blog/kapak/{k(d["kapak"])}-800.avif" alt="" '
                            'width="800" height="450" loading="lazy" decoding="async">' if d.get("kapak") else "")
                         + f'<div class="bs-ilgili-ic">{kat_rozet(d["kategori"], "bs-etiket bs-etiket-mini")}'
                         f'<strong>{k(d["baslik"])}</strong>'
                         f'<span>{k(d["aciklama"])}</span></div></a>' for d in digerleri) + "</div>\n")

    toc_sayi = toc.count("<li>")
    guncel = (f' · Güncellendi <time datetime="{k(y["guncelleme"])}">{tr_tarih(y["guncelleme"])}</time>'
              if y.get("guncelleme") else "")
    rozet = "".join(f'<span class="bs-rozet">{k(s)}</span>' for s in y.get("sinavlar", []))
    kapak = ""
    if y.get("kapak"):
        # srcset: dar ekranda 1600 px'lik kapagi indirmenin anlami yok
        # (olculdu: 106 KB yerine 48 KB). `sizes` icerik sutunu genisligini
        # bildiriyor, yoksa tarayici 100vw varsayip buyugu seciyor.
        kapak = (f'<img class="bs-kapak" src="/blog/kapak/{k(y["kapak"])}.avif" '
                 f'srcset="/blog/kapak/{k(y["kapak"])}-800.avif 800w, /blog/kapak/{k(y["kapak"])}.avif 1600w" '
                 f'sizes="(max-width: 767px) 100vw, 720px" '
                 f'alt="{k(y.get("kapak_alt", y["baslik"]))}" width="1600" height="901" '
                 f'fetchpriority="high" decoding="async">')
    return f'''
<div class="kap bs-yazi-ust">
  <nav class="bs-kirinti" aria-label="Sayfa yolu">
    <a href="/">{ikon("ev")}<span>Ana Sayfa</span></a>{ikon("ok-sag")}
    <a href="/blog/">Blog</a>{ikon("ok-sag")}
    <a href="/blog/#{k(y["kategori"])}">{k(kat)}</a>
  </nav>
</div>
<div class="kap bs-duzen">
  <article class="bs-icerik">
    {kat_rozet(y["kategori"])}
    <h1 class="bs-baslik">{k(y["baslik"])}</h1>
    <p class="bs-kunye">{rozet}<span class="bs-kunye-oge">{ikon("saat")}{okuma_dk(y)} dakikalık okuma</span><span class="bs-kunye-oge bs-goruntulenme" data-yol="/blog/{k(y["slug"])}/" hidden>{ikon("goz")}<span class="bs-gor-sayi"></span> görüntülenme</span><span class="bs-kunye-oge"><time datetime="{k(y["tarih"])}">{tr_tarih(y["tarih"])}</time>{guncel}</span></p>
    {kapak}
    <p class="bs-ozet">{mm(k(y["ozet"]))}</p>
    <nav class="bs-toc bs-toc-ust" aria-label="İçindekiler">
      <p class="bs-yan-baslik">{ikon("liste")}İçindekiler<em>{toc_sayi} bölüm</em></p>
      <ol>{toc}</ol>
    </nav>
    <hr class="bs-ayrac">
{mm(govde)}{mm(ek)}
    {blog_yan.paylas(y["baslik"], "/blog/" + y["slug"] + "/")}
  </article>
  <aside class="bs-yan">
    {blog_yan.uc_karti("blog-" + y["slug"])}
    {blog_yan.kategori_blogu(y["kategori"])}
    {blog_yan.sinav_blogu(y.get("sinavlar"))}
    {blog_yan.yazi_listesi(y["slug"])}
    <nav class="bs-toc bs-toc-yan" aria-label="Okuma konumu" data-toplam="{toc_sayi}">
      <p class="bs-yan-baslik">Neredesin<em><span class="bs-konum">1</span> / {toc_sayi}</em></p>
      <div class="bs-toc-cubuk"><span style="width:0%"></span></div>
      <ol>{toc}</ol>
      <div class="bs-toc-gezinti">
        <button type="button" class="bs-toc-onceki" aria-label="Önceki bölüm">{ikon("ok-sol")}Önceki</button>
        <button type="button" class="bs-toc-sonraki" aria-label="Sonraki bölüm">Sonraki{ikon("ok-sag")}</button>
      </div>
      <div class="bs-toc-alt">
        <button type="button" class="bs-toc-hepsi" aria-expanded="false">Tüm bölümler</button>
        <button type="button" class="bs-toc-basa">{ikon("ok-yukari")}Başa dön</button>
      </div>
    </nav>
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
              + "".join(f'<button data-kat="{a}" aria-pressed="false" style="--kat:{r}">'
                        + ikon(i) + k(ad) + "</button>" for a, ad, i, r in kullanilan))
    def kapak_img(y, sizes, ilk=False):
        """Kart kapagi. Baslik baglantisi ayrica var; gorsel baglantisi ekran
        okuyucuda ve sekme sirasinda TEKRAR etmesin diye alt="" +
        aria-hidden + tabindex=-1 (sus gorseli kurali)."""
        if not y.get("kapak"):
            return ""
        kp = k(y["kapak"])
        return (f'<a class="bs-kart-gorsel" href="/blog/{k(y["slug"])}/" tabindex="-1" aria-hidden="true">'
                f'<img src="/blog/kapak/{kp}-800.avif" srcset="/blog/kapak/{kp}-800.avif 800w, /blog/kapak/{kp}.avif 1600w" '
                f'sizes="{sizes}" alt="" width="800" height="450" decoding="async"'
                + (' fetchpriority="high"' if ilk else ' loading="lazy"') + "></a>")

    def kart(y, i):
        # Ilk kart genis ekranda yatay "one cikan" kart (Ahmet 23.09: "blog ana
        # sayfasinin tasarimini resimlerle birlikte duzenleyelim").
        one = i == 0
        return f'''<article class="bs-kart{" bs-kart-one" if one else ""}" data-kat="{k(y["kategori"])}" data-sinav="{k(" ".join(str(x).lower() for x in y.get("sinavlar", [])))}" style="--kat:{blog_veri.KAT_RENK.get(y["kategori"], "#1860f0")}">
        {kapak_img(y, "(min-width: 900px) 620px, 100vw" if one else "(min-width: 900px) 380px, 100vw", ilk=one)}
        <div class="bs-kart-ic">
        {kat_rozet(y["kategori"])}
        <h2><a href="/blog/{k(y["slug"])}/">{k(y["baslik"])}</a></h2>
        <p>{k(y["aciklama"])}</p>
        <p class="bs-kunye">{"".join(f'<span class="bs-rozet">{k(s)}</span>' for s in y.get("sinavlar", []))}<time datetime="{k(y["tarih"])}">{tr_tarih(y["tarih"])}</time> · {okuma_dk(y)} dk</p>
        </div>
      </article>'''
    kartlar = "".join(kart(y, i) for i, y in enumerate(yazilar))
    sinav_suzgec = ('<button data-sinav="*" aria-pressed="true">Tüm sınavlar</button>'
                    + "".join(f'<button data-sinav="{a}" aria-pressed="false" style="--kat:{r}">'
                              + ikon("sinavda") + k(ad) + "</button>"
                              for a, ad, r in blog_veri.SINAVLAR))
    return f'''
<div class="kap bs-hero">
  <h1>Matematik Konu Anlatımı</h1>
  <p>Üniversite ve kamu sınavlarına hazırlananlar için baştan sona konu anlatımı, hap bilgiler ve çözümlü örnekler. Tamamı ücretsiz.</p>
</div>
<div class="kap">
  <div class="bs-suzgec-satir" id="konular"><span class="bs-suzgec-etiket">Konu</span><div class="bs-suzgec">{suzgec}</div></div>
  <div class="bs-suzgec-satir" id="sinavlar"><span class="bs-suzgec-etiket">Sınav</span><div class="bs-suzgec bs-suzgec-sinav">{sinav_suzgec}</div></div>
  <div class="bs-izgara">{kartlar}</div>
</div>
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
          "inLanguage": "tr-TR",
          "articleSection": KAT.get(y["kategori"], y["kategori"]),
          "keywords": ", ".join([y["baslik"]] + [str(x) for x in y.get("sinavlar", [])]),
          "wordCount": kelime_sayisi(y),
          # ISO 8601 sure: PT11M → 11 dakika
          "timeRequired": f"PT{okuma_dk(y)}M",
          # Gorsel KONUYA baglanir (name = konu basligi), kisiye degil (24.09).
          "image": ({"@type": "ImageObject",
                     "url": ALAN + f"/blog/kapak/{y['kapak']}.avif",
                     "contentUrl": ALAN + f"/blog/kapak/{y['kapak']}.avif",
                     "name": y["baslik"],
                     "width": 1600, "height": 901,
                     "caption": y.get("kapak_alt", y["baslik"])} if y.get("kapak") else None)},
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
            # Ahmet (24.09): "basliklarda Ahmet Celen yazmasin, blog ana sayfasi
            # haric; tum yazilarda." Yazi <title>'i YALNIZ konu basligi. 01-05'te
            # ek yayindan kalkti: Ahmet'in acik karari, "yayindaki title degismez"
            # kuralina bilincli istisna. "title_eki": True ancak Ahmet isterse.
            yol=f"/blog/{y['slug']}/", title=y["baslik"] + (" - Ahmet Çelen" if y.get("title_eki") else ""),
            desc=y["aciklama"], govde=yazi_govde(y, digerleri), jsonld=jsonld_yazi(y),
            gorsel=f"/blog/kapak/{y['kapak']}.avif" if y.get("kapak") else None,
            gorsel_alt=(f'<meta property="og:image:alt" content="{k(y.get("kapak_alt", y["baslik"]))}">'
                        '\n<meta property="og:image:width" content="1600">'
                        '\n<meta property="og:image:height" content="901">') if y.get("kapak") else None,
            onyukle=onyukle))
    n += yaz("blog/index.html", kabuk(
        yol="/blog/", title="Matematik Konu Anlatımı Blog - Ahmet Çelen",
        desc="TYT, AYT, ALES ve KPSS için baştan sona matematik konu anlatımı; hap bilgiler, çözümlü örnekler ve grafiklerle. Ücretsiz.",
        govde=hub_govde(yazilar), jsonld=jsonld_hub(yazilar), taslak=not yazilar))
    # api/goruntulenme.js yalniz bu listedeki adresleri kabul eder
    # (varsayilan red). Yazi eklenince liste de kendiliginden buyur.
    beyaz = json.dumps(sorted(f"/blog/{y['slug']}/" for y in yazilar), ensure_ascii=False, indent=1) + "\n"
    yaz("api/_yazilar.json", beyaz)
    print(f"blog: {len(yazilar)} yazi · {n} dosya yazildi"
          + ("" if yazilar else " · hub TASLAK (noindex)"))


if __name__ == "__main__":
    uygula()
