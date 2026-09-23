#!/usr/bin/env python3
# scripts/blog_veri.py — blog yazilarini toplar (23.09.2026)
#
# Her yazi scripts/yazilar/ altinda KENDI dosyasinda durur ve bir `YAZI`
# sozlugu disa verir. Elli konuluk yol haritasi tek dosyaya sigmaz; bu
# yuzden yazi basina bir dosya. Sira dosya adindaki numaradan gelir.
#
# ALAN SOZLUGU
#   slug        : /blog/<slug>/ — YAYINLANDIKTAN SONRA DEGISTIRILMEZ
#   baslik      : <h1> ve <title> govdesi
#   aciklama    : meta description (<= 160 karakter)
#   tarih       : ISO yayin tarihi · guncelleme: ISO ya da None
#   kategori    : KATEGORILER anahtari
#   sinavlar    : ["TYT","AYT","ALES","KPSS"] — hangi sinavda cikar
#   kapak       : blog/kapak/<kapak>.avif  (scripts/blog_gorsel.py uretir)
#   kapak_alt   : gorselin alt metni
#   ozet        : giris paragrafi (duz metin)
#   bolumler    : [{"baslik": "H2", "icerik": [html ya da duz paragraf]}]
#   sss         : [(soru, cevap)] — sayfada ve JSON-LD FAQPage'te
#   kontrol     : ["kontrol listesi maddesi"]
#   kaynaklar   : [(ad, url)] — YALNIZ RESMI kaynak, ic baglanti YOK
#   ilgili      : ["baska-yazinin-slugu"] (bos birakilirsa tarihe gore)
#   taslak      : True ise sayfa uretilmez
import importlib.util, pathlib, re

KOK = pathlib.Path(__file__).resolve().parent.parent

# (anahtar, ad, ikon adi, renk). Renk her kategoriye AYRI bir kimlik verir;
# Ahmet: "kategorileri de iyi ayirmaliyiz, bunlara da ikonlu yapalim."
# Renkler marka mavisiyle ayni doygunluk bandindan secildi; dekoratif
# gradyan ya da parilti YOK.
KATEGORILER = [
    ("fonksiyonlar", "Fonksiyonlar", "fonksiyonlar", "#1860f0"),
    ("polinomlar", "Polinomlar", "polinomlar", "#0f766e"),
    ("denklemler", "Denklem ve Parabol", "denklemler", "#6d28d9"),
    ("trigonometri", "Trigonometri", "trigonometri", "#c2410c"),
    ("logaritma", "Logaritma ve Diziler", "logaritma", "#15803d"),
    ("analiz", "Limit, Türev, İntegral", "analiz", "#be123c"),
]
KAT_AD = {a: ad for a, ad, _, _ in KATEGORILER}
KAT_IKON = {a: i for a, _, i, _ in KATEGORILER}
KAT_RENK = {a: r for a, _, _, r in KATEGORILER}

# Sinav ekseni. Ayni konu uc sinavda farkli derinlikte soruluyor; ogrenci
# hangi sinava calisiyorsa oradan girsin diye kategoriden AYRI bir eksen.
# (Ahmet 23.09: "sagda kategoriler ve sinavlar diye ayri bloklar olsun".)
SINAVLAR = [
    ("tyt", "TYT", "#1860f0"),
    ("ayt", "AYT", "#6d28d9"),
    ("ales", "ALES", "#0f766e"),
    ("kpss", "KPSS", "#c2410c"),
]
SINAV_AD = {a: ad for a, ad, _ in SINAVLAR}
SINAV_RENK = {a: r for a, _, r in SINAVLAR}

def _yukle():
    out = []
    for p in sorted((KOK / "scripts/yazilar").glob("[0-9]*.py")):
        ad = "blog_yazi_" + p.stem
        spec = importlib.util.spec_from_file_location(ad, p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        if hasattr(m, "YAZI"):
            out.append(m.YAZI)
    return out

YAZILAR = _yukle()

def yayinda():
    return [y for y in YAZILAR if not y.get("taslak")]
