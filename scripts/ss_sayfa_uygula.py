#!/usr/bin/env python3
# scripts/ss_sayfa_uygula.py — /ss/* cikmis sorular sayfalarini TEK veriden
# (scripts/ss_veri.py) ve ana temanin iskeletinden (ss/kpss/index.html'in
# <head>/ust menu/alt bilgisi) uretir; /ss/ ana sayfasini da yazar.
#
# 22.09.2026 (Ahmet): tasarim yenileme, kirik ÖSYM baglantilari, guncel
# yillar, dis baglantilar yeni sekmede, altta UniConnectly kutusu.
#
# DEGISMEYENLER (arama trafigi; /ss/kpss/ sitenin %95'i): mevcut sayfalarda
# <title>, meta keywords/description, <h3> ve giris paragrafi DOSYADAN OKUNUR
# ve aynen korunur; dosya yollari ayni. Yeni sayfalar (kpss-onlisans,
# kpss-ortaogretim) icin metinler ss_veri.py'de.
#
# Kullanim: python3 scripts/ss_sayfa_uygula.py [--kuru]
import re, sys, pathlib, html, datetime
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import ss_veri, uniconnectly_blok

KOK = pathlib.Path(__file__).resolve().parent.parent
KURU = "--kuru" in sys.argv
ISKELET = (KOK / "ss/kpss/index.html").read_text(encoding="utf-8")
BAS = ISKELET[:ISKELET.index("\t<!-- Inner Page Breadcrumb -->")]
SON = ISKELET[ISKELET.index('\t<section class="footer_one">'):]
assert '<link rel="stylesheet" href="/css/duzeltmeler.css' in BAS and "</body>" in SON
BUGUN = datetime.date.today().isoformat()

def mevcut(yol):
    p = KOK / yol
    if not p.exists():
        return {}
    s = p.read_text(encoding="utf-8")
    al = lambda r: (re.search(r, s, re.S) or [None, None])[1]
    giris = al(r'<div class="main-title text-center">\s*<h3[^>]*>.*?</h3>\s*<p>(.*?)</p>')
    return {
        "title": al(r"<title>(.*?)</title>"),
        "keywords": al(r'<meta name="keywords" content="([^"]*)">'),
        "description": al(r'<meta name="description" content="([^"]*)">'),
        "h3": al(r'<h3 class="mt0">(.*?)</h3>'),
        "giris": re.sub(r"\s+", " ", giris).strip() if giris else None,
    }

# Eski tasarimdaki kart gorseli; Ahmet 22.09: "hepsi ayni olsun".
KART_GORSELI = "/images/ss-kart.webp"  # tema gorseli (images/background/8.jpg kirpik); 22.09 vectorstock hotlink kaldirildi

def kart(yil, etiket, url):
    return (f'\t\t\t\t<a class="cs-kart cs-kart-gorsel" style="background-image:url({KART_GORSELI})" href="{url}" target="_blank" rel="noopener">\n'
            f'\t\t\t\t\t<span class="cs-kart-yil">{yil}</span>\n'
            f'\t\t\t\t\t<span class="cs-kart-ad">{html.escape(etiket)}</span>\n'
            f'\t\t\t\t\t<span class="cs-kart-dugme">PDF (ÖSYM)</span>\n'
            f'\t\t\t\t</a>')

def diger(secili):
    out = []
    for a in ss_veri.SIRA:
        v = ss_veri.SAYFALAR[a]
        y = v["kartlar"]
        out.append(f'\t\t\t\t<a href="/ss/{a}/"{" class=\"cs-secili\"" if a == secili else ""}>{v["kisa"]} Çıkmış Sorular<span>{y[0][0]} - {y[-1][0]}</span></a>')
    out.append('\t\t\t\t<a href="/sinavlar/">Sınav Geri Sayımları<span>Tüm sınavlar</span></a>')
    return "\n".join(out)

def govde(anahtar, v, m):
    kartlar = v["kartlar"]
    h3 = m.get("h3") or v["h3"]
    giris = m.get("giris") or v["giris"]
    tam = sum(1 for _, e, _ in kartlar if "%10" not in e)
    return f'''
	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-6 offset-xl-3 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">{v["kisa"]}</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/ss/">Çıkmış Sorular</a></li>
						    <li class="breadcrumb-item active" aria-current="page">{kartlar[0][0]} - {kartlar[-1][0]}</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Cikmis sorular (scripts/ss_sayfa_uygula.py uretir; veri scripts/ss_veri.py) -->
	<section class="cs-sayfa">
		<div class="container">
			<div class="main-title text-center">
				<h3 class="mt0">{h3}</h3>
				<p>{giris}</p>
			</div>
			<div class="cs-ozet">
				<span class="gs-cip"><strong>{len(kartlar)}</strong> yıl</span>
				<span class="gs-cip">{kartlar[0][0]} - {kartlar[-1][0]}</span>
				<span class="gs-cip">Kaynak: <a href="https://www.osym.gov.tr/" target="_blank" rel="noopener">ÖSYM</a></span>
				<span class="gs-cip"><a href="/sinavlar/{v["geri_sayim"]}/">{v["kisa"]} sınavına kaç gün kaldı?</a></span>
			</div>
			<div class="cs-liste">
{chr(10).join(kart(*k) for k in kartlar)}
			</div>
			<p class="cs-not">Bu soruların tüm hakları ÖSYM'ye aittir. Bağlantılar ÖSYM'nin resmî sitesine (dokuman.osym.gov.tr) yönlendirilmiştir; PDF'ler yeni sekmede açılır.{" 2019'dan itibaren ÖSYM soruların %10'unu 'temel soru kitapçığı' olarak yayımlar." if tam < len(kartlar) else ""} Bu sayfa {BUGUN[8:10]}.{BUGUN[5:7]}.{BUGUN[:4]} tarihinde güncellendi.</p>

			<h3 class="gs-alt-baslik">Diğer çıkmış sorular</h3>
			<div class="cs-diger">
{diger(anahtar)}
			</div>
		</div>
	</section>
''' + uniconnectly_blok.blok(f"ss-{anahtar}", "kariyer" if anahtar.startswith("kpss") else "kampus")

def hub():
    kartlar = []
    for a in ss_veri.SIRA:
        v = ss_veri.SAYFALAR[a]; y = v["kartlar"]
        kartlar.append(f'\t\t\t\t<a class="cs-kart" href="/ss/{a}/">\n\t\t\t\t\t<span class="cs-kart-yil" style="font-size:24px">{v["kisa"]}</span>\n'
                       f'\t\t\t\t\t<span class="cs-kart-ad">{len(y)} yıl · {y[0][0]} - {y[-1][0]} · ÖSYM PDF</span>\n'
                       f'\t\t\t\t\t<span class="cs-kart-dugme" style="color:#192675">Çıkmış sorular</span>\n\t\t\t\t</a>')
    return f'''
	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-6 offset-xl-3 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">Çıkmış Sorular ve Sınavlar</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/">Ana Sayfa</a></li>
						    <li class="breadcrumb-item active" aria-current="page">Sınavlar</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>

	<section class="cs-sayfa">
		<div class="container">
			<div class="main-title text-center">
				<h3 class="mt0">Çıkmış Sorular</h3>
				<p>TYT, AYT, MSÜ, DGS ve KPSS için ÖSYM'nin yayımladığı resmî soru kitapçıkları. PDF'ler ÖSYM'nin sitesinden açılır; burada barındırılmaz.</p>
			</div>
			<div class="cs-liste">
{chr(10).join(kartlar)}
			</div>

			<h3 class="gs-alt-baslik" style="margin-top:36px">Sınavlar ve Geri Sayımlar</h3>
			<p class="cs-not" style="text-align:left;margin:0 0 16px">ÖSYM takvimindeki sınavlara kaç gün kaldığını canlı takip et: <a href="/sinavlar/">tüm geri sayımlar</a>.</p>
			<div class="cs-diger">
				<a href="/sinavlar/">Tüm Sınavlar<span>Sıradaki sınav ve takvim</span></a>
				<a href="/sinavlar/kpss-onlisans/">KPSS Ön Lisans<span>04.10.2026</span></a>
				<a href="/sinavlar/kpss-ortaogretim/">KPSS Ortaöğretim<span>25.10.2026</span></a>
				<a href="/sinavlar/ales3/">ALES/3<span>29.11.2026</span></a>
				<a href="/sinavlar/tyt/">TYT<span>2027 takvimi bekleniyor</span></a>
				<a href="/sinavlar/ayt/">AYT<span>2027 takvimi bekleniyor</span></a>
				<a href="/sinavlar/msu/">MSÜ<span>2027 takvimi bekleniyor</span></a>
				<a href="/sinavlar/kpssa/">KPSS Lisans<span>2027 takvimi bekleniyor</span></a>
			</div>
		</div>
	</section>
''' + uniconnectly_blok.blok("ss-genel")

def yaz(yol, title, keywords, description, govde_html):
    bas = BAS
    bas = re.sub(r"<title>.*?</title>", lambda m: f"<title>{title}</title>", bas, count=1, flags=re.S)
    bas = re.sub(r'<meta name="keywords" content="[^"]*">', lambda m: f'<meta name="keywords" content="{keywords}">', bas, count=1)
    bas = re.sub(r'<meta name="description" content="[^"]*">', lambda m: f'<meta name="description" content="{description}">', bas, count=1)
    bas = bas.replace('<html dir="ltr" lang="en">', '<html dir="ltr" lang="tr">')
    son = SON if "uniconnectly-blok.js" in SON else SON.replace(
        '<script type="text/javascript" src="/js/script.js"></script>',
        '<script type="text/javascript" src="/js/script.js"></script>\n<script src="/js/uniconnectly-blok.js"></script>')
    yeni = bas + govde_html + son
    p = KOK / yol
    eski = p.read_text(encoding="utf-8") if p.exists() else ""
    if not KURU and yeni != eski:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(yeni, encoding="utf-8")
    print(f"{yol}: {'ayni' if yeni == eski else 'yazildi'} · {title[:50]}")

for a in ss_veri.SIRA:
    v = ss_veri.SAYFALAR[a]
    m = mevcut(f"ss/{a}/index.html")
    title = m.get("title") or v["baslik_yeni"]
    keywords = m.get("keywords") or v["anahtar_kelime_yeni"]
    desc = m.get("description") or v["aciklama_yeni"].replace('"', "&quot;")
    assert (m.get("h3") or v.get("h3")) and (m.get("giris") or v.get("giris")), a
    yaz(f"ss/{a}/index.html", title, keywords, desc, govde(a, v, m))

yaz("ss/index.html", "Çıkmış Sorular ve Sınav Geri Sayımları - ÖSYM PDF",
    "çıkmış sorular, tyt çıkmış sorular, ayt çıkmış sorular, kpss çıkmış sorular, dgs çıkmış sorular, msü çıkmış sorular, sınava kaç gün kaldı",
    "TYT, AYT, MSÜ, DGS, KPSS Lisans, Ön Lisans ve Ortaöğretim çıkmış sorular (ÖSYM resmî PDF) ve sınavlara kaç gün kaldı geri sayımları tek sayfada.",
    hub())
