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
LOGO = SITE + "/brand/light-logo-yildizsiz.webp"  # yildizsiz (Ahmet 22.09: reklam alanlarinda hep bu)
MAGAZALAR = [  # (etiket, rozet gorseli, adres)
    ("App Store", SITE + "/brand/imza/app-store.png", "https://apps.apple.com/tr/app/uniconnectly/id6784849124"),
    ("Google Play", SITE + "/brand/imza/google-play.png",
     "https://play.google.com/store/apps/details?id=com.uniconnectly.app&referrer=utm_source%3Dahmetcelen.com.tr%26utm_medium%3Dreferral%26utm_campaign%3D{kampanya}"),
    ("AppGallery", SITE + "/brand/imza/appgallery.png", "https://appgallery.huawei.com/app/C118677033"),
]
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

# Kitleye gore faydalar. Her madde uygulamada VAR olan bir ozelliktir (22.09
# dogrulama: portfoy mig 237, event_checkins, sertifika bayragi, company_jobs,
# kampus elcisi mig 102-112, podyum, organizer_web_visibility, uye karti
# indirimleri, Bilime Destek). Olmayan ozellik yazilmaz.
FAYDALAR = {
    "ogrenci": ("Öğrenciye ne kazandırır?", [
        ("Dijital portföy", '<span class="uc-mono">uniconnectly.com/@kullanıcıadı</span> adresiyle herkese açık paylaş; CV\'ne ve LinkedIn\'e sertifika doğrulama bağlantısı olarak ekle. <a class="uc-ornek" href="{ORNEK_OGRENCI}" target="_blank" rel="noopener" title="Örnek portföy: @nursena">Örneği gör: @nursena</a>'),
        ("Doğrulanabilir katılım", "QR ile giriş yaptığın etkinlikler portföyünde doğrulanmış listelenir"),
        ("Sertifikalar", "Platformda verilen sertifikalar doğrulanmış işaretli, edu.tr e-postan onaylı"),
        ("Anlık fırsatlar", "Staj, iş ve burs duyuruları akışına düşer; şirket ilanlarına uygulamadan başvur"),
        ("Topluluklar ve etkinlikler", "Üniversitendeki toplulukları ve takvimi tek ekranda gör, başvurulu etkinliklere katıl"),
        ("Üye kartı indirimleri", "Takip ettiğin toplulukların anlaşmalı işletme indirimlerinden yararlan"),
    ]),
    "topluluk": ("Topluluğa ne kazandırır?", [
        ("Ücretsiz web sitesi", '<span class="uc-mono">uniconnectly.com/@topluluk</span>: etkinlikler, duyurular ve yönetim kurulu herkese açık, Google\'da bulunur. <a class="uc-ornek" href="{ORNEK_TOPLULUK}" target="_blank" rel="noopener" title="Örnek topluluk sayfası: @uludag_emt">Örneği gör: @uludag_emt</a>'),
        ("Podyum ile sponsor bulma", "Etkinliğini yayınlamadan önce hazırlık aşamasında şirketlere sun, sponsor ve iş birliği görüşmesini uygulamada yürüt"),
        ("İş birliği ortamı", "Şirketler ve diğer topluluklarla mesajlaşma, ortak etkinlik ve sponsorluk iletişimi tek kanalda"),
        ("QR ile katılım takibi", "Kapıda QR okut, katılımcı istatistiklerini ve geçmiş etkinlik raporlarını gör"),
        ("Başvurulu etkinlik ve bilet", "Başvuru al, onayla, görevli üye ata; harici biletli etkinliklerde kapı yönetimi"),
        ("Üye kartı fırsatları", "Üyelerine özel anlaşmalı işletme indirimleri tanımla"),
    ]),
    "sirket": ("Şirkete ne kazandırır?", [
        ("Kampüs elçisi programı", "Üniversitelere elçi ilanı aç, başvuruları değerlendir, her kampüste elçi ekibi kur"),
        ("Markanı kampüse taşı", "Etkinlik ve sponsorluk fırsatlarını Podyum'da gör, topluluklarla doğrudan görüş"),
        ("Staj ve iş ilanları", "İlanların öğrenci akışında ve İş İlanları bölümünde görünür, başvurular uygulamadan gelir"),
        ("İş birliği fırsatları", "Topluluklarla mesajlaş, ortak etkinlik ve marka iş birliklerini tek yerden yönet"),
        ("Etki ölçümü", "Markanın kampüslerdeki toplulaştırılmış, anonim etkileşim raporu"),
    ]),
    "akademik": ("Akademisyene ne kazandırır?", [
        ("Bilime Destek", "Anket ve araştırma çağrını UniConnectly ağındaki doğru öğrenci kitlesine ulaştır, katılımcı topla"),
        ("Etkinlik ve seminer duyurusu", "Bölüm topluluklarıyla seminer, atölye ve konferans duyurularını öğrencilere ulaştır"),
        ("Öğrenci topluluklarına erişim", "Danışmanı olduğun topluluğun etkinlik takvimi ve katılım verileri tek ekranda"),
        ("Blog ile anlık fırsat takibi", "Hibe, araştırma programı, burs ve etkinlik çağrılarını UniConnectly blogundan takipte kal"),
    ]),
}

ORNEK_OGRENCI = SITE + "/@nursena"      # Ahmet 22.09: ornek kisisel portfoy
ORNEK_TOPLULUK = SITE + "/@uludag_emt"  # Ahmet 22.09: ornek topluluk sayfasi

def fayda_panelleri():
    out = []
    for i, (anahtar, (baslik, maddeler)) in enumerate(FAYDALAR.items()):
        li = "\n".join(f'\t\t\t\t\t\t\t<li><strong>{b}</strong><span>{a.replace("{ORNEK_OGRENCI}", ORNEK_OGRENCI).replace("{ORNEK_TOPLULUK}", ORNEK_TOPLULUK)}</span></li>' for b, a in maddeler)
        out.append(f'\t\t\t\t\t<div class="uc-panel" data-uc-panel="{anahtar}" role="tabpanel"{"" if i == 0 else " hidden"}>\n'
                   f'\t\t\t\t\t\t<h4>{baslik}</h4>\n\t\t\t\t\t\t<ul class="uc-faydalar">\n{li}\n\t\t\t\t\t\t</ul>\n\t\t\t\t\t</div>')
    return "\n".join(out)

def magaza_rozetleri(kampanya):
    return "\n".join(
        f'\t\t\t\t\t\t<a class="uc-magaza" href="{u.format(kampanya=kampanya)}" target="_blank" rel="noopener" aria-label="{e}\'dan indir">'
        f'<img src="{g}" alt="{e}" loading="lazy" decoding="async" height="40"></a>'
        for e, g, u in MAGAZALAR)

def blok(kampanya):
    """kampanya: utm_campaign degeri (ss-kpss, sinavlar-ales3 gibi)."""
    kartlar = "\n".join(yazi_karti(s, b, e, kampanya) for s, b, e in SABIT_YAZILAR)
    rozetler = magaza_rozetleri(kampanya)
    FAYDA_PANELLERI = fayda_panelleri()
    return f'''
	<!-- UniConnectly tanitim + blog (scripts/uniconnectly_blok.py) -->
	<section class="uc-blok" data-kampanya="{kampanya}">
		<div class="container">
			<div class="uc-tanitim">
				<div class="uc-tanitim-metin">
					<a class="uc-logo" href="{ref("/", kampanya)}" target="_blank" rel="noopener"><img src="{LOGO}" alt="UniConnectly" width="640" height="185" loading="lazy" decoding="async"></a>
					<span class="uc-etiket">Öğrenciler için ücretsiz</span>
					<h3>Sınavdan sonra kampüs hayatı başlıyor</h3>
					<p>UniConnectly, üniversite öğrencilerini toplulukları, etkinlikleri ve şirketlerle aynı uygulamada buluşturur. Üniversitendeki toplulukları keşfeder, etkinliklere QR ile katılır, katıldıklarını ve sertifikalarını dijital portföyünde herkese açık paylaşırsın.</p>
					<div class="uc-rakamlar">
						<div><strong>234</strong><span>üniversite</span></div>
						<div><strong>Ücretsiz</strong><span>öğrenciler ve topluluklar için</span></div>
						<div><strong>3</strong><span>mağazada yayında</span></div>
					</div>
					<div class="uc-dugmeler">
						<a class="btn btn-thm" href="{ref("/", kampanya)}" target="_blank" rel="noopener">UniConnectly'yi keşfet</a>
						<a class="uc-ikincil" href="{ref("/blog", kampanya)}" target="_blank" rel="noopener">Tüm blog yazıları</a>
					</div>
					<div class="uc-magazalar">
{rozetler}
					</div>
				</div>
				<div class="uc-tanitim-liste">
					<div class="uc-sekmeler" role="tablist" aria-label="Kime ne kazandırır?">
						<button type="button" class="uc-sekme uc-sekme-acik" role="tab" aria-selected="true" data-uc-sekme="ogrenci">Öğrenciler</button>
						<button type="button" class="uc-sekme" role="tab" aria-selected="false" data-uc-sekme="topluluk">Topluluklar</button>
						<button type="button" class="uc-sekme" role="tab" aria-selected="false" data-uc-sekme="sirket">Şirketler</button>
						<button type="button" class="uc-sekme" role="tab" aria-selected="false" data-uc-sekme="akademik">Akademisyenler</button>
					</div>
{FAYDA_PANELLERI}
				</div>
			</div>

			<div class="uc-baslik-satiri">
				<h3 class="uc-alt-baslik" id="uc-yazi-baslik">Öğrenciler için rehberler</h3>
				<div class="uc-kategoriler" id="uc-kategoriler" role="tablist" aria-label="Blog kategorileri">
					<button type="button" class="uc-kategori uc-kategori-acik" data-uc-kategori="seckiler" aria-selected="true">Seçkiler</button>
				</div>
			</div>
			<div class="uc-yazilar" id="uc-yazilar" data-uc-seckiler>
{kartlar}
			</div>
			<p class="uc-tumu" id="uc-tumu" hidden><a href="{ref("/blog", kampanya)}" target="_blank" rel="noopener">Tümünü gör</a></p>

			<div id="uc-en-yeniler-kutu" hidden>
				<h3 class="uc-alt-baslik">En yeniler</h3>
				<div class="uc-yazilar uc-yeniler" id="uc-en-yeniler"></div>
			</div>

			<div class="uc-kapanis">
				<a class="uc-kapanis-baglanti" href="{ref("/", kampanya)}" target="_blank" rel="noopener">
					<img src="{LOGO}" alt="UniConnectly" width="640" height="185" loading="lazy" decoding="async">
					<h3>Öğrenciler, etkinlikler, topluluklar, şirketler: hepsi bir arada!</h3>
					<p>Toplulukları keşfet, etkinliklere QR ile katıl, dijital portföyünü herkese açık paylaş. Öğrenciler için ücretsiz.</p>
				</a>
				<div class="uc-magazalar uc-magazalar-orta">
{rozetler}
				</div>
				<a class="uc-ikincil" href="{ref("/", kampanya)}" target="_blank" rel="noopener">uniconnectly.com</a>
			</div>
		</div>
	</section>
'''
