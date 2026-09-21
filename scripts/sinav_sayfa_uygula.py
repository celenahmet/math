#!/usr/bin/env python3
# scripts/sinav_sayfa_uygula.py — /sinavlar/* geri sayim sayfalarini TEK
# kaynaktan (sinavlar/js/sinav-takvimi.js) ve ana temanin iskeletinden
# (ss/kpss/index.html: <head>, ust menu, alt bilgi) uretir.
#
# 21.09.2026 (Ahmet): "tasarimlari cok kotu" → eski "coming soon" sablonu
# (tema/webajans, knob halkalari, jQuery) birakildi; sayfalar ana temanin
# basligi/menusu/alt bilgisiyle, sade kutu sayac + tum sinavlar kart listesi
# olarak yeniden yazildi. Genel sayfa (/sinavlar/) siradaki sinavi one
# cikarir, tum sinavlara yonlendirir.
#
# DEGISMEYENLER (arama trafigi): <title> mevcut sayfadan okunur ve aynen
# korunur; sinav sayfalarinda <h2> metni ("MSÜ Geri Sayım") aynen korunur;
# dosya yollari ayni. Yalniz genel sayfanin <h2>'si "Sınav Geri Sayımları"
# (Ahmet: genel sayfa tum sinavlara yonlendirsin).
#
# Meta aciklama sinava ozel ve kosuldugu gune gore "yapildi / kac gun kaldi"
# yazar; ÖSYM 2027 takvimi gelince once JS, sonra bu betik kosulur.
#
# Kullanim: python3 scripts/sinav_sayfa_uygula.py [--kuru]
import re, sys, pathlib, datetime
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import uniconnectly_blok

KOK = pathlib.Path(__file__).resolve().parent.parent
KURU = "--kuru" in sys.argv
JS = (KOK / "sinavlar/js/sinav-takvimi.js").read_text(encoding="utf-8")
ISKELET = (KOK / "ss/kpss/index.html").read_text(encoding="utf-8")
BUGUN = datetime.date.today()
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
YONELME = {"msu": "MSÜ'ye", "ales1": "ALES/1'e", "tyt": "TYT'ye", "ayt": "AYT'ye",
           "dgs": "DGS'ye", "ales2": "ALES/2'ye", "kpssa": "KPSS'ye", "ales3": "ALES/3'e",
           "kpssonlisans": "KPSS Ön Lisans'a", "kpssorta": "KPSS Ortaöğretim'e"}
CIKMIS = {"msu": ("MSÜ Çıkmış Sorular", "/ss/msu/"), "tyt": ("TYT Çıkmış Sorular", "/ss/tyt/"),
          "ayt": ("AYT Çıkmış Sorular", "/ss/ayt/"), "dgs": ("DGS Çıkmış Sorular", "/ss/dgs/"),
          "kpssa": ("KPSS Lisans Çıkmış Sorular PDF", "/ss/kpss/"),
          "kpssonlisans": ("KPSS Ön Lisans Çıkmış Sorular PDF", "/ss/kpss-onlisans/"),
          "kpssorta": ("KPSS Ortaöğretim Çıkmış Sorular PDF", "/ss/kpss-ortaogretim/")}
GENEL_CIKMIS = ("Çıkmış Sorular (TYT, AYT, MSÜ, DGS, KPSS)", "/ss/")
H2_GENEL = "Sınav Geri Sayımları"

def js_sinavlar():
    govde = JS[JS.index("var SINAVLAR = {"):JS.index("var SIRA")]
    out = {}
    for m in re.finditer(r"\n\s{4}(\w+): \{(.*?)\n\s{4}\}", govde, re.S):
        out[m.group(1)] = dict(re.findall(r"(\w+): '([^']*)'", m.group(2)))
    sira = re.findall(r"'(\w+)'", JS[JS.index("var SIRA = ["):JS.index("]", JS.index("var SIRA = ["))])
    kaynak_tarihi = re.search(r"KAYNAK_TARIHI = '([^']+)'", JS).group(1)
    return out, sira, kaynak_tarihi

SINAVLAR, SIRA, KAYNAK_TARIHI = js_sinavlar()
assert set(SINAVLAR) == set(YONELME) == set(SIRA), "JS ile betik anahtarlari uyusmuyor"

def gecti(s): return datetime.date.fromisoformat(s["tarih"]) <= BUGUN
def tr_tarih(iso):
    y, a, g = (int(x) for x in iso.split("-")); return f"{g} {AYLAR[a-1]} {y}"
def tr_tarih_nokta(s):
    g, a, y = (int(x) for x in s.split(".")); return f"{g} {AYLAR[a-1]} {y}"
def nokta(iso):
    y, a, g = iso.split("-"); return f"{g}.{a}.{y}"
def siradaki():
    for a in SIRA:
        if not gecti(SINAVLAR[a]): return a
    return None

def aciklama(anahtar):
    s = SINAVLAR[anahtar]; kisa, yon = s["kisa"], YONELME[anahtar]; yil = s["tarih"][:4]
    donem = s["donem"] if len(s["donem"]) <= 28 else f"{yil}-{s['uzun'].split(' (')[0]}"
    if gecti(s):
        return (f"{donem} sınavı {tr_tarih(s['tarih'])}'da yapıldı"
                + (f", sonuç {tr_tarih_nokta(s['sonuc'])}" if s.get("sonuc") else "")
                + f". {int(yil)+1} {kisa} tarihi ÖSYM takvimiyle burada; {yon} kaç gün kaldı geri sayımı.")
    return (f"{donem} sınavı {tr_tarih(s['tarih'])}'da. {yon} kaç gün kaldı? Canlı geri sayım"
            + (f", sonuç tarihi {tr_tarih_nokta(s['sonuc'])}" if s.get("sonuc") else "")
            + ". Tarihler ÖSYM resmî sınav takviminden.")

def aciklama_genel():
    sn = siradaki()
    ilk = (f"Sıradaki sınav {SINAVLAR[sn]['kisa']}, {tr_tarih(SINAVLAR[sn]['tarih'])}. " if sn else "")
    return (ilk + "TYT, AYT, MSÜ, DGS, KPSS ve ALES sınavlarına kaç gün kaldı? "
            "ÖSYM takvimine göre canlı geri sayım ve sonuç tarihleri.")

def kartlar(secili):
    out = []
    for a in SIRA:
        s = SINAVLAR[a]
        out.append(
            f'      <a class="gs-kart" data-sinav="{a}" href="/sinavlar/{s["yol"]}/">\n'
            f'        <span class="gs-kart-kisa">{s["kisa"]}</span>\n'
            f'        <span class="gs-kart-uzun">{s["uzun"].split(" (", 1)[1].rstrip(")") if " (" in s["uzun"] else s["donem"]}</span>\n'
            f'        <span class="gs-kart-tarih">{nokta(s["tarih"])}</span>\n'
            f'        <span class="gs-rozet">{"Tamamlandı" if gecti(s) else "Yaklaşıyor"}</span>\n'
            f'      </a>')
    return "\n".join(out)

def baglantilar(anahtar):
    ad, yol = CIKMIS.get(anahtar, GENEL_CIKMIS)
    return (f'      <a class="gs-baglanti" href="{yol}"><strong>{ad}</strong><span>ÖSYM PDF bağlantıları</span></a>\n'
            '      <a class="gs-baglanti" href="/pdfnot/"><strong>Ders Notları (PDF)</strong><span>Deneme ve fasiküller</span></a>\n'
            '      <a class="gs-baglanti" href="/video/"><strong>Video Çözümler</strong><span>Konu anlatımı ve soru çözümü</span></a>')

def govde(anahtar):
    genel = anahtar == "tumu"
    s = None if genel else SINAVLAR[anahtar]
    ust = H2_GENEL if genel else s["kisa"]
    kirinti = "ÖSYM sınav takvimi" if genel else s["donem"]
    h2 = H2_GENEL if genel else H2[anahtar]
    return f'''
	<!-- Inner Page Breadcrumb -->
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-6 offset-xl-3 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">{ust}</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/sinavlar/">Sınav Geri Sayımları</a></li>
						    <li class="breadcrumb-item active" aria-current="page">{kirinti}</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Geri sayim (scripts/sinav_sayfa_uygula.py uretir; veri sinavlar/js/sinav-takvimi.js) -->
	<section class="gs-sayfa">
		<div class="container">
			<div class="main-title text-center gs-baslik">
				<h2 class="mt0">{h2}</h2>
				{'<p id="gs-one-cikan" class="gs-one-cikan"></p>' if genel else ''}
				<p id="gs-durum" class="gs-durum"></p>
			</div>
			<div id="gs-sayac" class="gs-sayac" hidden>
				<div class="gs-kutu"><span class="gs-sayi" id="gs-gun">0</span><span class="gs-etiket">Gün</span></div>
				<div class="gs-kutu"><span class="gs-sayi" id="gs-saat">00</span><span class="gs-etiket">Saat</span></div>
				<div class="gs-kutu"><span class="gs-sayi" id="gs-dk">00</span><span class="gs-etiket">Dakika</span></div>
				<div class="gs-kutu"><span class="gs-sayi" id="gs-sn">00</span><span class="gs-etiket">Saniye</span></div>
			</div>
			<div id="gs-bilgi" class="gs-bilgi"></div>

			<h3 class="gs-alt-baslik">Tüm sınavlar</h3>
			<div class="gs-liste">
{kartlar(anahtar)}
			</div>

			<h3 class="gs-alt-baslik">Çalışma kaynakları</h3>
			<div class="gs-baglantilar">
{baglantilar(anahtar)}
			</div>
			<p id="gs-kaynak" class="gs-kaynak"></p>
		</div>
	</section>
''' + uniconnectly_blok.blok("sinavlar-genel" if genel else f"sinavlar-{anahtar}")

# --- iskelet parcalari (ss/kpss/index.html) ---
BAS = ISKELET[:ISKELET.index("\t<!-- Inner Page Breadcrumb -->")]
SON = ISKELET[ISKELET.index('\t<section class="footer_one">'):]
assert '<link rel="stylesheet" href="/css/duzeltmeler.css' in BAS and "</body>" in SON

def sayfa(anahtar, yol):
    p = KOK / yol
    eski = p.read_text(encoding="utf-8") if p.exists() else ""
    tm = re.search(r"<title>(.*?)</title>", eski, re.S)
    kisa = H2_GENEL if anahtar == "tumu" else SINAVLAR[anahtar]["kisa"]
    title = tm.group(1) if tm else f"{kisa} Sınavına Kaç Gün Kaldı? - {kisa} Geri Sayım"   # mevcut KORUNUR
    keywords = re.search(r'<meta name="keywords" content="([^"]*)">', eski)
    keywords = keywords.group(1) if keywords else "sınav tarihleri, kaç gün kaldı, geri sayım"
    metin = aciklama_genel() if anahtar == "tumu" else aciklama(anahtar)
    assert len(metin) <= 165, (yol, len(metin), metin)
    desc = metin.replace("&", "&amp;").replace('"', "&quot;")
    bas = BAS
    bas = re.sub(r"<title>.*?</title>", lambda m: f"<title>{title}</title>", bas, count=1, flags=re.S)
    bas = re.sub(r'<meta name="keywords" content="[^"]*">', lambda m: f'<meta name="keywords" content="{keywords}">', bas, count=1)
    bas = re.sub(r'<meta name="description" content="[^"]*">', lambda m: f'<meta name="description" content="{desc}">', bas, count=1)
    bas = bas.replace('<html dir="ltr" lang="en">', '<html dir="ltr" lang="tr">')
    son = SON if "uniconnectly-blok.js" in SON else SON.replace(
        '<script type="text/javascript" src="/js/script.js"></script>',
        '<script type="text/javascript" src="/js/script.js"></script>\n<script src="/js/uniconnectly-blok.js"></script>')
    son = son.replace('<script src="/js/uniconnectly-blok.js"></script>',
                      '<script src="/js/uniconnectly-blok.js"></script>\n'
                      '<script src="/sinavlar/js/sinav-takvimi.js"></script>\n'
                      f"<script>sinavGeriSayim('{anahtar}');</script>")
    yeni = bas + govde(anahtar) + son
    if not KURU and yeni != eski:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(yeni, encoding="utf-8")
    print(f"{yol}: {'ayni' if yeni == eski else 'yazildi'} · title: {title[:45]} · {len(metin)} kr")

# Mevcut <h2> metinleri (korunur): dosyadan okunur, yoksa "<KISA> Geri Sayım".
H2 = {}
for a in SINAVLAR:
    dosya = KOK / f"sinavlar/{SINAVLAR[a]['yol']}/index.html"
    eski = dosya.read_text(encoding="utf-8") if dosya.exists() else ""
    m = re.search(r"<h2[^>]*>(.*?)</h2>", eski, re.S)
    H2[a] = m.group(1).strip() if m else f"{SINAVLAR[a]['kisa']} Geri Sayım"

for a in SIRA:
    sayfa(a, f"sinavlar/{SINAVLAR[a]['yol']}/index.html")
sayfa("tumu", "sinavlar/index.html")
