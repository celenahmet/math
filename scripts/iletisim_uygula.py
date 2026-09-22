#!/usr/bin/env python3
# scripts/iletisim_uygula.py — /iletisim/ sayfasinin govdesini uretir (22.09.2026)
#
# Ahmet: "bu iletisim sayfasinin da biraz yenilenmeye ihtiyaci var."
# Metinler AHMET'IN kendi cumleleri; yalnizca duzene sokuldu, yeniden
# YAZILMADI (kural: hitap/karsilama metnini ajan yazmaz). <title> korunur.
# Stil: css/duzeltmeler.css "hk-" blogu (Hakkimda ile ayni dil) + "il-" ekleri.
#
# Ayrica head'deki bozuk kapanis (`<` ... `/head>`) onarilir: sayfada
# "< /head>" metni gorunuyordu.
#
# Kullanim: python3 scripts/iletisim_uygula.py   (ardindan scripts/css_surum.py)
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
DOSYA = KOK / "iletisim/index.html"
sys.path.insert(0, str(KOK / "scripts"))
from hakkimda_uygula import ikon  # noqa: E402  (ayni ikon seti)

POSTA = "ahmetcelen@hacettepe.edu.tr"
UC = "https://uniconnectly.com/?ref=ahmetcelen.com.tr&amp;utm_source=ahmetcelen.com.tr&amp;utm_medium=referral&amp;utm_campaign=iletisim"
YOUTUBE = "https://www.youtube.com/channel/UCCXZwb5Y9Tphcv41jfgKI7w?sub_confirmation=1"
VIMEO = "https://vimeo.com/search?type=clip&amp;q=ahmet+celen"
ACIKLAMA = ("Ahmet Çelen iletişim: ders notlarındaki hata bildirimi, öneri, iş birliği ve telif "
            f"başvuruları için {POSTA}.")

# Ahmet'in kendi cumleleri (eski sayfadan, degistirilmedi).
SEBEPLER = [
    ("belge", "Hata bildirimi", "Yayımladığımız belgelerde yazım, soru, mantık hataları ve eksik kısımlar için ulaşabilirsiniz."),
    ("balon", "Öneri ve görüş", "İstekleriniz, öneri ve görüşlerinizi bildirebilirsiniz."),
    ("elsikisma", "İş birliği", "Sponsorluk veya işbirliği için ulaşabilirsiniz."),
    ("saat", "Tanışma", "Sohbet ve tanışma amaçlı ulaşabilirsiniz :)"),
]
TELIF = ("Herhangi bir ticari gelirimiz yok fakat yayımladığımız bir içerik telif haklarınızı ihlal ettiğini "
         "düşünüyorsanız bildirebilirsiniz. Eğer telif haklarınızı ihlal ediyorsa o bölümü kaldırıp tekrar "
         "dokümanı güncelleriz.")

def sebep(ad, baslik, metin):
    return (f'\t\t\t\t<li class="hk-kart il-sebep">\n'
            f'\t\t\t\t\t<span class="hk-kart-ikon">{ikon(ad)}</span>\n'
            f'\t\t\t\t\t<span class="hk-kart-baslik">{baslik}</span>\n'
            f'\t\t\t\t\t<span class="hk-kart-metin">{metin}</span>\n'
            f'\t\t\t\t</li>\n')

GOVDE = f'''	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-6 offset-xl-3 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">İLETİŞİM</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/">Ana Sayfa</a></li>
						    <li class="breadcrumb-item active" aria-current="page">İletişim</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!-- Iletisim (scripts/iletisim_uygula.py uretir) -->
	<section class="hk-sayfa">
		<div class="container">
			<div class="il-ust">
				<div class="il-ust-metin">
					<p class="hk-ust">İletişim</p>
					<h2>Hata bildirimi, öneri ya da iş birliği: yazabilirsiniz.</h2>
					<p class="hk-giris">Aşağıdaki adrese yazmanız yeterli. Kırık bağlantı, hatalı tarih ya da soru hatası bildirirseniz kaynağı kontrol edip düzeltirim.</p>
				</div>
				<div class="il-kart">
					<span class="il-kart-etiket">{ikon("posta")} E-posta</span>
					<a class="il-adres" href="mailto:{POSTA}">{POSTA}</a>
					<div class="hk-baglantilar il-kanallar">
						<a class="hk-baglanti" href="{YOUTUBE}" target="_blank" rel="noopener noreferrer">YouTube</a>
						<a class="hk-baglanti" href="{VIMEO}" target="_blank" rel="noopener noreferrer">Vimeo</a>
						<a class="hk-baglanti" href="{UC}" target="_blank" rel="noopener">UniConnectly</a>
					</div>
				</div>
			</div>

			<h3 class="hk-bolum-baslik">Ne için yazabilirsiniz?</h3>
			<ul class="hk-kartlar il-sebepler">
{"".join(sebep(*s) for s in SEBEPLER)}			</ul>

			<div class="hk-paneller il-paneller">
				<div class="hk-panel">
					<h4>Telif bildirimi</h4>
					<p>{TELIF}</p>
				</div>
				<div class="hk-panel">
					<h4>Aradığınız burada olabilir</h4>
					<p>Ders notları için <a href="/pdfnot/">PDF sayfası</a>, çıkmış sorular için <a href="/ss/">ÖSYM bağlantıları</a>, sınav tarihleri için <a href="/sinavlar/">geri sayımlar</a>. Hakkımda bilgisi: <a href="/hakkimizda/">Hakkımda</a>.</p>
				</div>
			</div>
		</div>
	</section>
'''

s = DOSYA.read_text(encoding="utf-8")
# 1) head onarimi: "<\n  <link ..." ve "/head>" → duzgun kapanis
s = s.replace('<  <link rel="stylesheet" href="/css/font-awesome.min.css">', '  <link rel="stylesheet" href="/css/font-awesome.min.css">')
s = re.sub(r"^/head>$", "</head>", s, count=1, flags=re.M)
a = s.index("\t<!-- Inner Page Breadcrumb -->")
b = s.index('\t<section class="footer_one">')
bas = re.sub(r'<meta name="description" content="[^"]*">',
             f'<meta name="description" content="{ACIKLAMA}">', s[:a], count=1)
assert "<title>İletişim - Ahmet Çelen</title>" in bas
yeni = bas + GOVDE + s[b:]
assert "<CENTER>" not in yeni and "/head>\n<body>" not in yeni.replace("</head>", "")
eski = DOSYA.read_text(encoding="utf-8")
if yeni != eski:
    DOSYA.write_text(yeni, encoding="utf-8")
print(f"iletisim/index.html: {'yazildi' if yeni != eski else 'ayni'}")
