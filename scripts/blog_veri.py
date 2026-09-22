#!/usr/bin/env python3
# scripts/blog_veri.py — blog yazilarinin TEK kaynagi (22.09.2026)
#
# Ahmet (22.09): "uniconnectly'deki gibi blog sayfasi kuracagiz, bloglari
# yazacagiz; blog kurulunca icerigini bahsederim." Bu dosya iskeleti tutar,
# ICERIK Ahmet'ten gelir — ajan kendi basina yazi uretmez.
#
# Sayfalar scripts/blog_uygula.py ile uretilir. Bir yazi eklemek = asagidaki
# YAZILAR listesine bir sozluk eklemek; baska hicbir dosyaya dokunulmaz.
#
# ALAN SOZLUGU
#   slug        : adres parcasi (/blog/<slug>/). SONRADAN DEGISTIRILMEZ —
#                 yayinlanmis adres aramada birikir (bkz. SEO kurali).
#   baslik      : yazinin <h1>'i ve <title>'inin govdesi
#   aciklama    : meta description (<= 160 karakter)
#   tarih       : ISO yayin tarihi (2026-09-22)
#   guncelleme  : ISO ya da None
#   kategori    : KATEGORILER icinden biri
#   ozet        : giris paragrafi (duz metin)
#   bolumler    : [{"baslik": "H2 metni", "icerik": ["<p>…</p>", "<ul>…</ul>"]}]
#   sss         : [("soru", "cevap")] — hem sayfada hem JSON-LD FAQPage'te
#   kontrol     : ["kontrol listesi maddesi", …]  (bos birakilabilir)
#   kaynaklar   : [("ad", "https://…")] — YALNIZ RESMI KAYNAK.
#                 Ucuncu taraf blog/haber atfi YOK; ic baglanti da YOK
#                 (ic baglantilar "Bunlar da ilgini cekebilir" bolumunde).
#   taslak      : True ise sayfa uretilmez (yayindan once bekletmek icin)
#
# Kullanim: python3 scripts/blog_uygula.py

KATEGORILER = [
    ("sinav", "Sınav"),
    ("calisma", "Çalışma Yöntemi"),
    ("matematik", "Matematik"),
    ("tercih", "Tercih ve Başvuru"),
]

YAZILAR = [
    # Ornek kalip (silinmedi, KOPYALANIR):
    # {
    #     "slug": "ornek-yazi",
    #     "baslik": "Örnek Yazı Başlığı",
    #     "aciklama": "Arama sonucunda görünecek bir cümlelik özet.",
    #     "tarih": "2026-09-22",
    #     "guncelleme": None,
    #     "kategori": "sinav",
    #     "ozet": "Yazının ilk paragrafı.",
    #     "bolumler": [
    #         {"baslik": "İlk bölüm", "icerik": ["<p>Metin.</p>"]},
    #     ],
    #     "sss": [("Soru?", "Cevap.")],
    #     "kontrol": ["Madde"],
    #     "kaynaklar": [("ÖSYM Sınav Takvimi", "https://www.osym.gov.tr/Sayfa/SinavTakvimi/...")],
    # },
]

def yayinda():
    return [y for y in YAZILAR if not y.get("taslak")]
