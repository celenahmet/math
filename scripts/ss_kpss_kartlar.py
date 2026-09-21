#!/usr/bin/env python3
# scripts/ss_kpss_kartlar.py — /ss/kpss/ sayfasindaki yil kartlarini TEK
# listeden uretir. Baslik (<title>), <h3> ve dosya yolu DEGISMEZ.
#
# Kural (Ahmet, 21.09): ÖSYM PDF'leri ASLA kendi sunucumuzda barindirilmaz,
# yalnizca ÖSYM'nin resmi adresine (dokuman.osym.gov.tr) baglanti verilir.
# Her baglanti eklenmeden once curl ile dogrulanmistir (application/pdf).
#
# 21.09 degisiklikleri: 2020 "Henuz hazir degil" (href=#) ve kirik 2008/2011
# baglantilari (ÖSYM arsivinde 404, resmi kaynak bulunamadi) kaldirildi;
# 2020-2026 ÖSYM %10 kitapciklari eklendi. GSC: "kpss son 10 yilin cikmis
# sorulari pdf" 6.859 gosterim / poz. 9,8 iken sayfa 2019'da bitiyordu.
#
# Kullanim: python3 scripts/ss_kpss_kartlar.py
import re, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
SAYFA = KOK / "ss/kpss/index.html"

# (yil, etiket eki, ÖSYM PDF)  — %10: ÖSYM 2019'dan beri sorularin %10'unu yayimliyor
KARTLAR = [
    (2009, "", "https://dokuman.osym.gov.tr/pdfdokuman/2009/KPSS/Lisans/2009kpsscsgenyetgenkul2.pdf"),
    (2010, "", "https://dokuman.osym.gov.tr/pdfdokuman/2010/KPSS/Lisans/2010kpsscsgenyetgenkul.pdf"),
    (2012, "", "https://dokuman.osym.gov.tr/pdfdokuman/2012/KPSS/Lisans/KPSS1_2012_CS_GYGK.pdf"),
    (2013, "", "https://dokuman.osym.gov.tr/pdfdokuman/2013/KPSS1/CS.pdf"),
    (2014, "", "https://dokuman.osym.gov.tr/pdfdokuman/2014/KPSS/SINAVSORULARI/2014KPSSALANCSGKGY.pdf"),
    (2015, "", "https://dokuman.osym.gov.tr/pdfdokuman/2015/KPSS/SINAVSORULARI/2015KPSSALANGKGY.pdf"),
    (2016, "", "https://dokuman.osym.gov.tr/pdfdokuman/2016/KPSS/2016KPSSGenelYetenekGenelKultur.pdf"),
    (2017, "", "https://dokuman.osym.gov.tr/pdfdokuman/2017/KPSS/SINAVSORULARI/2017KPSSALANGKGY.pdf"),
    (2018, "", "https://dokuman.osym.gov.tr/pdfdokuman/2018/KPSS/SINAVSORULARI/2018KPSSALANGKGY12112019.pdf"),
    (2019, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2019/KPSS/gy-gk16072019.pdf"),
    (2020, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2020/KPSS/gy-gk14092020.pdf"),
    (2021, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2021/KPSS/gy_gk_01082021.pdf"),
    (2022, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2022/KPSS/LISANS/kpss_lisans_gygk_18092022.pdf"),
    (2023, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2023/KPSS/LISANS/gygk_23072023nfy.pdf"),
    (2024, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2024/KPSS/LISANS/GYGK14072024.pdf"),
    (2025, " - %10", "https://dokuman.osym.gov.tr/pdfdokuman/2025/KPSS/GY-GK/gygk_07092025lsy.pdf"),
    (2026, " - %10", "https://dokuman.osym.gov.tr/web/2026/9/2026-kpss-lisansgenel-yetenek-genel-kultur-temel-soru-kitapcigi-ve-cevap-anahtari-10-9dh155-06125847.pdf"),
]
GORSELLER = ["https://cdn1.vectorstock.com/i/1000x1000/07/75/a-school-stationery-border-vector-23750775.jpg",
             "/images/courses/2.jpg", "/images/courses/3.jpg", "/images/courses/4.jpg"]

def kart(i, yil, ek, url):
    return (f'\t\t\t\t<div class="col-sm-6 col-lg-3">\n'
            f'\t\t\t\t\t<div class="img_hvr_box" style="background-image: url({GORSELLER[i % 4]});">\n'
            f'\t\t\t\t\t\t<div class="overlay">\n'
            f'\t\t\t\t\t\t\t<div class="details">\n'
            f'\t\t\t\t\t\t\t\t<h5>{yil} KPSS LİSANS{ek}</h5>\n'
            f'\t\t\t\t\t\t\t\t<p><a style="color:#FFFF00;" href="{url}" target="_blank" rel="noopener">PDF Dosyası için tıkla</a></p>\n'
            f'\t\t\t\t\t\t\t</div>\n\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n')

satirlar = []
for b in range(0, len(KARTLAR), 4):
    satirlar.append('\t\t\t<div class="row">\n' + "".join(kart(i, *k) for i, k in enumerate(KARTLAR[b:b+4])) + '\t\t\t</div>\n')
yeni_blok = "".join(satirlar)

s = SAYFA.read_text(encoding="utf-8")
a = s.index('\t\t\t<div class="row">', s.index("<h3 class=\"mt0\">Kamu Personeli"))   # ilk kart satiri
a = s.index('\t\t\t<div class="row">', a + 1) if 'col-lg-6 offset-lg-3' in s[a:a+200] else a
b = s.index('<h3 class="text-center">Bu soruların')
b = s.rindex("\n", 0, b) + 1
s = s[:a] + yeni_blok + "\t\t\t" + s[b:].lstrip("\t")
s = s.replace('aria-current="page">2008 - 2020<', 'aria-current="page">2009 - 2026<')
SAYFA.write_text(s, encoding="utf-8")
print(f"{len(KARTLAR)} kart, {len(satirlar)} satir yazildi")
