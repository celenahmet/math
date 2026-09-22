#!/usr/bin/env python3
# scripts/hakkimda_uygula.py — /hakkimizda/ sayfasinin govdesini uretir (22.09.2026)
#
# Ahmet: "hakkinda sayfasinin tasarimi komple yenilensin, modern olabilir."
# Sayfa iskeleti (bas/son) mevcut dosyadan alinir; <title> ve <h2> metni
# KORUNUR (SEO kurali: baslik/yol degismez). Yalniz govde ve meta aciklama
# yenilenir. Stil: css/duzeltmeler.css "hk-" blogu. Parilti/gradyan yok.
#
# Kullanim: python3 scripts/hakkimda_uygula.py   (ardindan scripts/css_surum.py)
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
DOSYA = KOK / "hakkimizda/index.html"
UC = "https://uniconnectly.com/?ref=ahmetcelen.com.tr&amp;utm_source=ahmetcelen.com.tr&amp;utm_medium=referral&amp;utm_campaign=hakkimda"
YOUTUBE = "https://www.youtube.com/channel/UCCXZwb5Y9Tphcv41jfgKI7w?sub_confirmation=1"
VIMEO = "https://vimeo.com/search?type=clip&amp;q=ahmet+celen"
ACIKLAMA = ("Ahmet Çelen: 2021'den beri ücretsiz matematik ders notları, denemeler, video çözümler "
            "ve ÖSYM çıkmış soru bağlantıları. UniConnectly kurucusu.")

# Sayi kaynaklari (uydurma yok): PDF sayisi pdfnot'taki .pdf baglantisi,
# cikmis soru sayfasi ss_veri.SIRA, geri sayim sinav-takvimi.js SINAVLAR.
sys.path.insert(0, str(KOK / "scripts"))
import ss_veri  # noqa: E402
PDF_SAYISI = len(set(re.findall(r'href="([^"]+\.pdf)"', (KOK / "pdfnot/index.html").read_text(encoding="utf-8"), re.I)))
SS_SAYISI = len(ss_veri.SIRA)
JS = (KOK / "sinavlar/js/sinav-takvimi.js").read_text(encoding="utf-8")
GS_SAYISI = len(re.findall(r"^\s{4}\w+: \{\s*$", JS[JS.index("var SINAVLAR"):JS.index("var SIRA")], re.M))

def ikon(ad):
    """Basit cizgi ikonlar (inline SVG, 24px). Dekor degil, kart etiketi."""
    yollar = {
        "belge": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M10 13h6M10 17h6"/>',
        "saat": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "pdf": '<path d="M4 19V6a2 2 0 0 1 2-2h5l2 2h5a2 2 0 0 1 2 2v11"/><path d="M2 19h20"/><path d="M9 11h6M9 14h4"/>',
        "video": '<rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/>',
        "posta": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        "balon": '<path d="M21 12a8 8 0 0 1-8 8H7l-4 3v-6a8 8 0 0 1 8-8h2a8 8 0 0 1 8 3z"/><path d="M9 11h6"/>',
        "elsikisma": '<path d="M9 7a3 3 0 1 0-3 3"/><path d="M18 10a3 3 0 1 0-3-3"/><path d="M3 20v-2a4 4 0 0 1 4-4h2"/><path d="M15 14h2a4 4 0 0 1 4 4v2"/><path d="M9 18l3-3 3 3"/>',
    }
    return (f'<svg class="hk-ikon" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" '
            f'stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{yollar[ad]}</svg>')

def kart(ad, baslik, metin, yol, etiket):
    return (f'\t\t\t\t<a class="hk-kart" href="{yol}">\n'
            f'\t\t\t\t\t<span class="hk-kart-ikon">{ikon(ad)}</span>\n'
            f'\t\t\t\t\t<span class="hk-kart-baslik">{baslik}</span>\n'
            f'\t\t\t\t\t<span class="hk-kart-metin">{metin}</span>\n'
            f'\t\t\t\t\t<span class="hk-kart-etiket">{etiket} <span class="uc-ok" aria-hidden="true">→</span></span>\n'
            f'\t\t\t\t</a>\n')

GOVDE = f'''	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-6 offset-xl-3 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">HAKKIMDA</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/">Ana Sayfa</a></li>
						    <li class="breadcrumb-item active" aria-current="page">Hakkımda</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- Hakkimda (scripts/hakkimda_uygula.py uretir) -->
	<section class="hk-sayfa">
		<div class="container">
			<div class="hk-hero">
				<div class="hk-hero-metin">
					<p class="hk-ust">Hacettepe Üniversitesi · Yazılım geliştirici · UniConnectly kurucusu</p>
					<h2>Ben Ahmet Çelen. 2021'den beri bu sitede üniversite ve kamu sınavlarına hazırlanan öğrenciler için ücretsiz matematik kaynakları yayımlıyorum.</h2>
					<p class="hk-giris">Ders notları, deneme sınavları ve video çözümlerinin tamamı ücretsizdir. Çıkmış sorular sayfalarında yalnızca ÖSYM'nin resmî kitapçıklarına bağlantı verilir; hiçbir doküman burada yeniden yayımlanmaz. Sınav geri sayımları ÖSYM'nin resmî takvimine göre güncellenir.</p>
					<div class="hk-dugmeler">
						<a class="uc-dugme uc-dugme-dolu" href="/ss/">Çıkmış sorular <span class="uc-ok" aria-hidden="true">→</span></a>
						<a class="uc-dugme uc-dugme-cerceve" href="/pdfnot/">Ders notları (PDF) <span class="uc-ok" aria-hidden="true">→</span></a>
					</div>
				</div>
				<figure class="hk-hero-gorsel">
					<img src="/images/about/3.jpg" width="615" height="500" alt="Kampüste birlikte ders çalışan öğrenciler" loading="lazy" decoding="async">
					<figcaption>2021'den beri · ücretsiz · reklam ağı yok</figcaption>
				</figure>
			</div>

			<ul class="hk-rakamlar" aria-label="Sitedeki içerik">
				<li><strong>620+</strong><span>yazdığım soru</span></li>
				<li><strong>{PDF_SAYISI}</strong><span>PDF ders notu</span></li>
				<li><strong>{SS_SAYISI}</strong><span>çıkmış soru sayfası</span></li>
				<li><strong>{GS_SAYISI}</strong><span>sınav geri sayımı</span></li>
			</ul>

			<h3 class="hk-bolum-baslik">Bu sitede ne var?</h3>
			<div class="hk-kartlar">
{kart("belge", "Çıkmış sorular", "TYT, AYT, MSÜ, DGS ve üç KPSS düzeyi için ÖSYM'nin resmî kitapçık bağlantıları; her bağlantı düzenli denetlenir.", "/ss/", "Sayfaya git")}{kart("saat", "Sınav geri sayımları", "ÖSYM takvimindeki her sınav için gün, saat, dakika; sonuç tarihleri ve kaynak bağlantısıyla.", "/sinavlar/", "Geri sayımlar")}{kart("pdf", "Ders notları", "Konu anlatımı ve soru bankası niteliğinde PDF fasiküller; logaritma, parabol, türev, integral ve daha fazlası.", "/pdfnot/", "PDF'leri gör")}{kart("video", "Video çözümler", "Notlardaki soruların adım adım video çözümleri; YouTube ve Vimeo'da.", "/video/", "Videolar")}			</div>

			<div class="hk-paneller">
				<div class="hk-panel">
					<h4>Neden ücretsiz?</h4>
					<p>Nitelikli sınav hazırlığının maddi imkâna bağlı olmaması gerektiğini düşünüyorum. Soruları kendim yazıyor, çözümlerini video olarak paylaşıyor ve ÖSYM'nin açık kaynaklarını tek yerde topluyorum. Sitede reklam ağı yok; yalnızca kendi geliştirdiğim öğrenci uygulaması UniConnectly'yi tanıtıyorum.</p>
				</div>
				<div class="hk-panel">
					<h4>Ne yapıyorum?</h4>
					<p>Hacettepe Üniversitesi'nde okudum; yazılım geliştiriciyim. Üniversite öğrencilerini, toplulukları ve şirketleri aynı uygulamada buluşturan <a href="{UC}" target="_blank" rel="noopener">UniConnectly</a>'nin kurucusu ve geliştiricisiyim. Diğer projelerim için <a href="https://www.ahmetcelen.com/projects" target="_blank" rel="noopener">ahmetcelen.com</a>.</p>
				</div>
			</div>

			<div class="hk-iletisim">
				<div class="hk-iletisim-metin">
					<h4>{ikon("posta")} İletişim</h4>
					<p>Görüş, öneri ve düzeltmeler için yazabilirsin. Kırık bağlantı ya da hatalı tarih görürsen haber ver; kaynağı kontrol edip düzeltirim.</p>
				</div>
				<div class="hk-baglantilar">
					<a class="hk-baglanti" href="mailto:ahmetcelen@hacettepe.edu.tr">ahmetcelen@hacettepe.edu.tr</a>
					<a class="hk-baglanti" href="mailto:bilgi@ahmetcelen.com.tr">bilgi@ahmetcelen.com.tr</a>
					<a class="hk-baglanti" href="{YOUTUBE}" target="_blank" rel="noopener noreferrer">YouTube</a>
					<a class="hk-baglanti" href="{VIMEO}" target="_blank" rel="noopener noreferrer">Vimeo</a>
					<a class="hk-baglanti" href="{UC}" target="_blank" rel="noopener">UniConnectly</a>
					<a class="hk-baglanti" href="https://www.ahmetcelen.com/projects" target="_blank" rel="noopener">ahmetcelen.com</a>
				</div>
			</div>
		</div>
	</section>
'''

def uygula():
    s = DOSYA.read_text(encoding="utf-8")
    a = s.index("\t<!-- Inner Page Breadcrumb -->")
    b = s.index('\t<section class="footer_one">')
    bas = s[:a]
    bas = re.sub(r'<meta name="description" content="[^"]*">',
                 f'<meta name="description" content="{ACIKLAMA}">', bas, count=1)
    assert "<title>Hakkımda - Ahmet Çelen</title>" in bas, "title degismis olmali degil"
    yeni = bas + GOVDE + s[b:]
    # CENTER gibi eski artiklar govdeyle birlikte gitti; iskelette kalmadigini dogrula
    assert "<CENTER>" not in yeni
    if yeni != s:
        DOSYA.write_text(yeni, encoding="utf-8")
    print(f"hakkimizda/index.html: {'yazildi' if yeni != s else 'ayni'} · PDF {PDF_SAYISI} · ss {SS_SAYISI} · gs {GS_SAYISI}")


if __name__ == "__main__":
    uygula()
