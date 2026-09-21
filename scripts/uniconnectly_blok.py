#!/usr/bin/env python3
# scripts/uniconnectly_blok.py — cikmis sorular ve geri sayim sayfalarinin
# altina konan UniConnectly tanitim + blog kutusu (TEK kaynak; ss_sayfa_uygula
# ve sinav_sayfa_uygula bunu cagirir).
#
# Ahmet (22.09): "ogrenciye somut faydasi anlatilir, referans linki paylasilir,
# en altta blog: sabit 8 yazi + 'En yeniler' 4 yazi; UniConnectly'ye organik
# trafik". Baglantilar ?ref=ahmetcelen.com.tr + UTM ile isaretli (Umami'de
# kaynak/kampanya olarak gorunur). "En yeniler" tarayicida
# https://uniconnectly.com/blog-feed.json'dan okunur (js/uniconnectly-blok.js);
# akis gelmezse bolum gizli kalir, sayfa bozulmaz.
#
# Metin: olgusal, abarti yok. Metni Ahmet degistirmek isterse yalniz burasi.
import html

SITE = "https://uniconnectly.com"
SABIT_YAZILAR = [
    ("edu-tr-mail-ogrenci-firsatlari", "Edu.tr Mailiyle Ücretsiz Neler Alınabilir? Öğrenci Fırsatları", "Fırsat"),
    ("google-ai-plus-ogrenci-ucretsiz", "Google AI Plus Öğrencilere 1 Yıl Ücretsiz: Nasıl Alınır?", "Fırsat"),
    ("microsoft-365-ogrenci-ucretsiz", "Microsoft 365 Öğrencilere Ücretsiz mi? Office 365 A1 Rehberi", "Fırsat"),
    ("github-student-developer-pack", "GitHub Student Developer Pack Nedir? Ücretsiz Copilot ve Pro", "Fırsat"),
    ("2026-2027-burs-veren-kurumlar", "2026-2027 Burs Veren Kurumlar: Tutarlar ve Son Başvuru Tarihleri", "Burs"),
    ("universite-tercihi-dikkat-edilecekler", "Üniversite Tercihi Yaparken Dikkat Edilmesi Gerekenler", "Rehber"),
    ("universiteye-baslayanlar-ilk-ay", "Üniversiteye Yeni Başlayanlar İçin İlk Ay Rehberi", "Rehber"),
    ("kulube-katilmak-neden-onemli", "Üniversite Kulüplerine Katılmak Neden Önemli?", "Kampüs"),
]

def ref(yol, kampanya):
    ayrac = "&" if "?" in yol else "?"
    return (f"{SITE}{yol}{ayrac}ref=ahmetcelen.com.tr&utm_source=ahmetcelen.com.tr"
            f"&utm_medium=referral&utm_campaign={kampanya}")

def yazi_karti(slug, baslik, etiket, kampanya):
    return (f'        <a class="uc-yazi" href="{ref("/blog/" + slug, kampanya)}" target="_blank" rel="noopener">\n'
            f'          <img src="{SITE}/assets/blog/{slug}.webp" alt="" loading="lazy" decoding="async" width="600" height="400">\n'
            f'          <span class="uc-yazi-etiket">{etiket}</span>\n'
            f'          <span class="uc-yazi-baslik">{html.escape(baslik)}</span>\n'
            f'        </a>')

def blok(kampanya):
    """kampanya: utm_campaign degeri (ss-kpss, sinavlar-ales3 gibi)."""
    kartlar = "\n".join(yazi_karti(s, b, e, kampanya) for s, b, e in SABIT_YAZILAR)
    return f'''
	<!-- UniConnectly tanitim + blog (scripts/uniconnectly_blok.py) -->
	<section class="uc-blok" data-kampanya="{kampanya}">
		<div class="container">
			<div class="uc-tanitim">
				<div class="uc-tanitim-metin">
					<span class="uc-etiket">UniConnectly · öğrenciler için ücretsiz</span>
					<h3>Sınavdan sonra kampüs hayatı başlıyor</h3>
					<p>UniConnectly, üniversite öğrencilerini toplulukları, etkinlikleri ve şirketlerle aynı uygulamada buluşturur. Üniversitendeki toplulukları keşfeder, etkinliklere QR ile katılır, burs ve öğrenci fırsatlarını tek yerden takip edersin.</p>
					<ul class="uc-faydalar">
						<li>Üniversitendeki toplulukları ve etkinlik takvimini tek ekranda gör</li>
						<li>Burs, staj ve ücretsiz öğrenci araçları rehberleri</li>
						<li>Etkinliklere QR ile hızlı giriş, katıldıkların kaydedilir</li>
						<li>App Store, Google Play ve AppGallery'de yayında</li>
					</ul>
					<div class="uc-dugmeler">
						<a class="btn btn-thm" href="{ref("/", kampanya)}" target="_blank" rel="noopener">UniConnectly'yi keşfet</a>
						<a class="uc-ikincil" href="{ref("/blog", kampanya)}" target="_blank" rel="noopener">Tüm blog yazıları</a>
					</div>
				</div>
			</div>

			<h3 class="uc-alt-baslik">Öğrenciler için rehberler</h3>
			<div class="uc-yazilar">
{kartlar}
			</div>

			<div id="uc-en-yeniler-kutu" hidden>
				<h3 class="uc-alt-baslik">En yeniler</h3>
				<div class="uc-yazilar uc-yeniler" id="uc-en-yeniler"></div>
			</div>
		</div>
	</section>
'''
