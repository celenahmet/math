#!/usr/bin/env python3
# scripts/sinav_sayfa_uygula.py — /sinavlar/* geri sayim sayfalarina TEK
# kaynaktan (sinavlar/js/sinav-takvimi.js) sinava ozel meta aciklama, ortak
# baglanti satiri ve tutarli alt bilgi basar. Baslik (<title>), <h2> ve
# dosya yollarina DOKUNMAZ (arama trafigi oturmus, Ahmet 21.09).
#
# Neden: 9 sayfada meta aciklama ayni ve geneldi ("...ogrenmek icin
# tiklayin!"); GSC'de /sinavlar/msu 1.779 gosterim / 6 tik. Alt bilgi 2021/2022
# karisik, bazi sayfada ders notu baglantisi var bazinda yok, Google fontlari
# http:// ile (https sayfada engellenir), <head> disinda basibos <meta>.
#
# Tarih degisince (ÖSYM 2027 takvimi) once sinav-takvimi.js guncellenir,
# sonra bu betik yeniden kosulur; aciklama "yapildi / kac gun kaldi"
# durumunu kosuldugu gune gore yazar.
#
# Kullanim: python3 scripts/sinav_sayfa_uygula.py [--kuru]
import re, sys, pathlib, datetime, html

KOK = pathlib.Path(__file__).resolve().parent.parent
KURU = "--kuru" in sys.argv
JS = (KOK / "sinavlar/js/sinav-takvimi.js").read_text(encoding="utf-8")
BUGUN = datetime.date.today()
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]

# Yonelme eki (Turkce): "MSÜ'ye kaç gün kaldı", "ALES/3'e kaç gün kaldı".
YONELME = {"msu": "MSÜ'ye", "ales1": "ALES/1'e", "tyt": "TYT'ye", "ayt": "AYT'ye",
           "dgs": "DGS'ye", "ales2": "ALES/2'ye", "kpssa": "KPSS'ye", "ales3": "ALES/3'e"}
# Sayfaya en yakin cikmis sorular sayfasi (ALES icin yok → TYT).
CIKMIS = {"msu": "/ss/msu/", "tyt": "/ss/tyt/", "ayt": "/ss/ayt/", "dgs": "/ss/dgs/", "kpssa": "/ss/kpss/"}

def js_sinavlar():
    govde = JS[JS.index("var SINAVLAR = {"):JS.index("var SIRA")]
    out = {}
    for m in re.finditer(r"\n\s{4}(\w+): \{(.*?)\n\s{4}\}", govde, re.S):
        anahtar, ic = m.group(1), m.group(2)
        alan = dict(re.findall(r"(\w+): '([^']*)'", ic))
        out[anahtar] = alan
    return out

def tr_tarih(iso):            # 2026-03-01 → 1 Mart 2026
    y, a, g = (int(x) for x in iso.split("-"))
    return f"{g} {AYLAR[a-1]} {y}"

def tr_tarih_nokta(s):        # 24.03.2026 → 24 Mart 2026
    g, a, y = (int(x) for x in s.split("."))
    return f"{g} {AYLAR[a-1]} {y}"

def aciklama(anahtar, s, hub=False):
    gecti = datetime.date.fromisoformat(s["tarih"]) <= BUGUN
    kisa, yon = s["kisa"], YONELME[anahtar]
    yil = s["tarih"][:4]
    # Uzun donem adi (KPSS: "...Genel Yetenek-Genel Kultur") 160 karakteri asar.
    donem = s["donem"] if len(s["donem"]) <= 28 else f"{yil}-{s['uzun'].split(' (')[0]}"
    if hub:
        return (f"{kisa} {yil} sınavı {tr_tarih(s['tarih'])}'da {'yapıldı' if gecti else 'yapılacak'}. "
                f"{yon} kaç gün kaldı geri sayımı ve AYT, MSÜ, DGS, KPSS, ALES sınav tarihleri "
                f"(ÖSYM resmî takvimi).")
    if gecti:
        return (f"{donem} sınavı {tr_tarih(s['tarih'])}'da yapıldı"
                + (f", sonuç {tr_tarih_nokta(s['sonuc'])}" if s.get("sonuc") else "")
                + f". {int(yil)+1} {kisa} tarihi ÖSYM takvimiyle burada; {yon} kaç gün kaldı geri sayımı.")
    return (f"{donem} sınavı {tr_tarih(s['tarih'])}'da. {yon} kaç gün kaldı? Canlı geri sayım"
            + (f", sonuç tarihi {tr_tarih_nokta(s['sonuc'])}" if s.get("sonuc") else "")
            + ". Tarihler ÖSYM resmî sınav takviminden.")

def baglantilar(anahtar):
    return ('<nav class="sinav-baglantilar">'
            '<a href="/">Ana Sayfa</a> · '
            f'<a href="{CIKMIS.get(anahtar, "/ss/tyt/")}">Çıkmış Sorular</a> · '
            '<a href="/pdfnot/">Ders Notları (PDF)</a> · '
            '<a href="/video/">Video Çözümler</a> · '
            '<a href="/sinavlar/">Tüm Geri Sayımlar</a>'
            '</nav>')

ALT_BILGI = ('<footer class="fade-down">\n'
             '                <p>Not : Sınavı koordine eden ÖSYM tarihi değiştirebilir.</p>\n'
             '                <h3>Ahmet Çelen © 2021</h3>\n'
             '            </footer>')

def uygula(yol, anahtar, hub=False):
    p = KOK / yol
    s = p.read_text(encoding="utf-8")
    e = s
    s = re.sub(r'^<meta http-equiv="content-type"[^>]*>\n\n?', "", s, count=1, flags=re.M)
    s = s.replace("http://fonts.googleapis.com", "https://fonts.googleapis.com")
    metin = aciklama(anahtar, SINAVLAR[anahtar], hub)
    assert len(metin) <= 160, (yol, len(metin), metin)
    desc = metin.replace("&", "&amp;").replace('"', "&quot;")
    s = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', s, count=1)
    # sayim kutusu ile "Count Down end" arasindaki karisik blok → tek blok
    s = re.sub(r"(</ul>\s*</section>).*?(<!-- Count Down end here -->)",
               lambda m: m.group(1) + '\n            <div id="diger-sinavlar"></div>\n            '
                         + baglantilar(anahtar) + "\n            " + m.group(2), s, count=1, flags=re.S)
    s = re.sub(r"<footer class=\"fade-down\">.*?</footer>", ALT_BILGI, s, count=1, flags=re.S)
    if s != e and not KURU:
        p.write_text(s, encoding="utf-8")
    print(f"{yol}: {'degisti' if s != e else 'ayni'} · {len(metin)} kr · {metin}")

SINAVLAR = js_sinavlar()
assert set(SINAVLAR) == set(YONELME), set(SINAVLAR) ^ set(YONELME)
for anahtar in SINAVLAR:
    uygula(f"sinavlar/{anahtar}/index.html", anahtar)
uygula("sinavlar/index.html", "tyt", hub=True)
