#!/usr/bin/env python3
# scripts/ss_veri.py — /ss/* cikmis sorular sayfalarinin TEK veri kaynagi.
#
# KURAL (Ahmet, 21-22.09): ÖSYM PDF'leri ASLA kendi sunucumuzda barindirilmaz;
# yalnizca ÖSYM'nin resmi adresine (dokuman.osym.gov.tr) baglanti verilir.
# Buradaki her baglanti eklenmeden once curl ile dogrulanmistir
# (application/pdf). Bulunamayan yillar YAZILMAZ (tahmin yok):
#   TYT/AYT 2019 · DGS 2008-2012, 2018, 2022-2024 · KPSS Lisans 2008, 2011
#   · KPSS On Lisans/Ortaogretim 2026 (sinav henuz yapilmadi).
#
# Alanlar: yol (klasor), kisa, baslik_yeni (yalniz YENI sayfalarda kullanilir;
# mevcut sayfanin <title>'i dosyadan okunur ve KORUNUR), h3 (yeni sayfalar
# icin; mevcutta dosyadan okunur), aciklama_yeni, anahtar_kelime_yeni,
# geri_sayim (sinavlar/ altindaki klasor), kartlar [(yil, etiket, url)].
D = "https://dokuman.osym.gov.tr/pdfdokuman/"

SAYFALAR = {
    "kpss": {
        "kisa": "KPSS", "geri_sayim": "kpssa",
        "kartlar": [
            (2009, "KPSS Lisans", D + "2009/KPSS/Lisans/2009kpsscsgenyetgenkul2.pdf"),
            (2010, "KPSS Lisans", D + "2010/KPSS/Lisans/2010kpsscsgenyetgenkul.pdf"),
            (2012, "KPSS Lisans", D + "2012/KPSS/Lisans/KPSS1_2012_CS_GYGK.pdf"),
            (2013, "KPSS Lisans", D + "2013/KPSS1/CS.pdf"),
            (2014, "KPSS Lisans", D + "2014/KPSS/SINAVSORULARI/2014KPSSALANCSGKGY.pdf"),
            (2015, "KPSS Lisans", D + "2015/KPSS/SINAVSORULARI/2015KPSSALANGKGY.pdf"),
            (2016, "KPSS Lisans", D + "2016/KPSS/2016KPSSGenelYetenekGenelKultur.pdf"),
            (2017, "KPSS Lisans", D + "2017/KPSS/SINAVSORULARI/2017KPSSALANGKGY.pdf"),
            (2018, "KPSS Lisans", D + "2018/KPSS/SINAVSORULARI/2018KPSSALANGKGY12112019.pdf"),
            (2019, "KPSS Lisans · %10 kitapçık", D + "2019/KPSS/gy-gk16072019.pdf"),
            (2020, "KPSS Lisans · %10 kitapçık", D + "2020/KPSS/gy-gk14092020.pdf"),
            (2021, "KPSS Lisans · %10 kitapçık", D + "2021/KPSS/gy_gk_01082021.pdf"),
            (2022, "KPSS Lisans · %10 kitapçık", D + "2022/KPSS/LISANS/kpss_lisans_gygk_18092022.pdf"),
            (2023, "KPSS Lisans · %10 kitapçık", D + "2023/KPSS/LISANS/gygk_23072023nfy.pdf"),
            (2024, "KPSS Lisans · %10 kitapçık", D + "2024/KPSS/LISANS/GYGK14072024.pdf"),
            (2025, "KPSS Lisans · %10 kitapçık", D + "2025/KPSS/GY-GK/gygk_07092025lsy.pdf"),
            (2026, "KPSS Lisans · %10 kitapçık", "https://dokuman.osym.gov.tr/web/2026/9/2026-kpss-lisansgenel-yetenek-genel-kultur-temel-soru-kitapcigi-ve-cevap-anahtari-10-9dh155-06125847.pdf"),
        ],
    },
    "kpss-onlisans": {
        "kisa": "KPSS Ön Lisans", "geri_sayim": "kpss-onlisans",
        "baslik_yeni": "KPSS Ön Lisans Çıkmış Sorular PDF - ÖSYM",
        "h3": "KPSS Ön Lisans Çıkmış Sorular",
        "giris": "KPSS Ön Lisans, iki yıllık ön lisans mezunlarının kamu kurumlarına atanması için ÖSYM tarafından çift yıllarda yapılır; Genel Yetenek ve Genel Kültür testlerinden oluşur. Aşağıdaki kitapçıklar ÖSYM'nin yayımladığı resmî temel soru kitapçıklarıdır (2018'den itibaren %10'luk örnek kitapçık).",
        "aciklama_yeni": "KPSS Ön Lisans çıkmış sorular PDF: 2014-2024 ÖSYM temel soru kitapçıkları ve cevap anahtarları, resmî ÖSYM bağlantılarıyla. 2026 KPSS Ön Lisans 4 Ekim'de.",
        "anahtar_kelime_yeni": "kpss ön lisans çıkmış sorular, kpss önlisans çıkmış sorular pdf, kpss ön lisans soruları, ösym kpss önlisans",
        "kartlar": [
            (2014, "KPSS Ön Lisans", D + "2014/KPSS/SINAVSORULARI/2014KPSSOnlisans.pdf"),
            (2018, "KPSS Ön Lisans · %10 kitapçık", D + "2018/KPSS/ONL/internetkitapcik06112018.pdf"),
            (2020, "KPSS Ön Lisans · %10 kitapçık", D + "2020/KPSS/ONL/internetkitap26102020.pdf"),
            (2022, "KPSS Ön Lisans · %10 kitapçık", D + "2022/KPSS/ONL/internetk09102022.pdf"),
            (2024, "KPSS Ön Lisans · %10 kitapçık", D + "2024/KPSS/ONL/kitapcik01092024.pdf"),
        ],
    },
    "kpss-ortaogretim": {
        "kisa": "KPSS Ortaöğretim", "geri_sayim": "kpss-ortaogretim",
        "baslik_yeni": "KPSS Ortaöğretim Çıkmış Sorular PDF - ÖSYM",
        "h3": "KPSS Ortaöğretim Çıkmış Sorular",
        "giris": "KPSS Ortaöğretim, lise mezunlarının kamu kurumlarına atanması için ÖSYM tarafından çift yıllarda yapılır; Genel Yetenek ve Genel Kültür testlerinden oluşur. Aşağıdaki kitapçıklar ÖSYM'nin yayımladığı resmî temel soru kitapçıklarıdır (2018'den itibaren %10'luk örnek kitapçık).",
        "aciklama_yeni": "KPSS Ortaöğretim (lise) çıkmış sorular PDF: 2016-2024 ÖSYM temel soru kitapçıkları ve cevap anahtarları, resmî ÖSYM bağlantılarıyla. 2026 KPSS Ortaöğretim 25 Ekim'de.",
        "anahtar_kelime_yeni": "kpss ortaöğretim çıkmış sorular, kpss lise çıkmış sorular pdf, kpss ortaöğretim soruları, ösym kpss ortaöğretim",
        "kartlar": [
            (2016, "KPSS Ortaöğretim", D + "2016/KPSSORTON/2016KPSSOrtaogretimDuzeyiTemel20112016.pdf"),
            (2018, "KPSS Ortaöğretim · %10 kitapçık", D + "2018/KPSSORTOGR/TemelSoruKitapcik09102018.pdf"),
            (2020, "KPSS Ortaöğretim · %10 kitapçık", D + "2020/KPSS/ORTAOGRET%C4%B0M/temelsorukitapcik_23112020.pdf"),
            (2022, "KPSS Ortaöğretim · %10 kitapçık", D + "2022/KPSS/ORTAOGRETIM/tsk06112022.pdf"),
            (2024, "KPSS Ortaöğretim · %10 kitapçık", D + "2024/KPSS/ORTAOGRETIM/tsk15092024.pdf"),
        ],
    },
    "tyt": {
        "kisa": "TYT", "geri_sayim": "tyt",
        "kartlar": [
            (2018, "TYT · tam kitapçık", D + "2018/YKS/TYT_01072018.pdf"),
            (2020, "TYT · temel soru kitapçığı", D + "2020/YKS/TSK/tyt_yks_2020.pdf"),
            (2021, "TYT · temel soru kitapçığı", D + "2021/YKS/TSK/tyt_yks_2021.pdf"),
            (2022, "TYT · temel soru kitapçığı", D + "2022/YKS/TSK/yks_2022_tyt.pdf"),
            (2023, "TYT · temel soru kitapçığı", D + "2023/YKS/TSK/yks_tyt_2023_kitapcik_T23ky.pdf"),
            (2024, "TYT · temel soru kitapçığı", D + "2024/YKS/TSK/yks_tyt_2024_kitapcik_T24kt.pdf"),
            (2025, "TYT · temel soru kitapçığı", D + "2025/YKS/TSK/yks_tyt_2025_kitapcik_d250.pdf"),
            (2026, "TYT · temel soru kitapçığı", D + "2026/YKS/TSK/yks_tyt_2026_kitapcik_d350.pdf"),
        ],
    },
    "ayt": {
        "kisa": "AYT", "geri_sayim": "ayt",
        "kartlar": [
            (2018, "AYT · tam kitapçık", D + "2018/YKS/AYT_01072018.pdf"),
            (2020, "AYT · temel soru kitapçığı", D + "2020/YKS/TSK/ayt_yks_2020.pdf"),
            (2021, "AYT · temel soru kitapçığı", D + "2021/YKS/TSK/ayt_yks_2021.pdf"),
            (2022, "AYT · temel soru kitapçığı", D + "2022/YKS/TSK/yks_2022_ayt.pdf"),
            (2023, "AYT · temel soru kitapçığı", D + "2023/YKS/TSK/yks_ayt_2023_kitapcik_g5A2H.pdf"),
            (2024, "AYT · temel soru kitapçığı", D + "2024/YKS/TSK/yks_ayt_2024_kitapcik_ts85k.pdf"),
            (2025, "AYT · temel soru kitapçığı", D + "2025/YKS/TSK/yks_ayt_2025_kitapcik_st12.pdf"),
            (2026, "AYT · temel soru kitapçığı", D + "2026/YKS/TSK/yks_ayt_2026_kitapcik_kt12.pdf"),
        ],
    },
    "msu": {
        "kisa": "MSÜ", "geri_sayim": "msu",
        "kartlar": [
            (2018, "MSÜ · tam kitapçık", D + "2018/MSU/CS/MSUCikmissorular24072018.pdf"),
            (2019, "MSÜ · %10 kitapçık", D + "2019/MSU/internetkitapcigi07042019.pdf"),
            (2020, "MSÜ · %10 kitapçık", D + "2020/MSU/internetkitapcik14062020.pdf"),
            (2021, "MSÜ · %10 kitapçık", D + "2021/MSU/kitapcik_04042021.pdf"),
            (2022, "MSÜ · %10 kitapçık", D + "2022/MSU/internetkitapcik27032022.pdf"),
            (2023, "MSÜ · %10 kitapçık", D + "2023/MSU/tsk_02042023.pdf"),
            (2024, "MSÜ · %10 kitapçık", D + "2024/MSU/tsk03032024.pdf"),
            (2025, "MSÜ · %10 kitapçık", D + "2025/MSU/tsk23022025.pdf"),
            (2026, "MSÜ · %10 kitapçık", D + "2026/MSU/msu_tskbd0103026.pdf"),
        ],
    },
    "dgs": {
        "kisa": "DGS", "geri_sayim": "dgs",
        "kartlar": [
            (2013, "DGS", D + "2013/DGS/DGS_internet%20kitap%C3%A7%C4%B1%C4%9F%C4%B1.pdf"),
            (2014, "DGS", D + "2014/DGS/2014_Dgs_Soru_Kitapciklari.pdf"),
            (2015, "DGS", D + "2015/DGS/2015_Dgs_Soru_Kitapciklari.pdf"),
            (2016, "DGS", D + "2016/DGS/2016_Dgs_Soru_Kitapciklari.pdf"),
            (2017, "DGS", D + "2017/DGS/2017_Dgs_Soru_Kitapciklari.pdf"),
            (2019, "DGS · %10 kitapçık", D + "2019/DGS/dgskitapcik30062019.pdf"),
            (2020, "DGS · %10 kitapçık", D + "2020/DGS/kitapcik10082020.pdf"),
            (2021, "DGS · %10 kitapçık", D + "2021/DGS/CS/2021_DGS_sorular.pdf"),
            (2025, "DGS · %10 kitapçık", D + "2025/DGS/tintkitapcik_20072025.pdf"),
            (2026, "DGS · %10 kitapçık", D + "2026/DGS/TSK/intkitapcik_td19072026.pdf"),
        ],
    },
}
SIRA = ["tyt", "ayt", "msu", "dgs", "kpss", "kpss-onlisans", "kpss-ortaogretim"]
