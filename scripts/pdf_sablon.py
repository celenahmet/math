#!/usr/bin/env python3
# scripts/pdf_sablon.py — blog PDF'inin yazdirma sablonu (A4 dikey) (28.09.2026)
#
# Ahmet (28.09): "tasarim A4 dikey; ilk sayfada genel bir tanitim alani ve
# 'bu belgeyi kullanmadan veya paylasmadan once guncelliginden emin olunuz'
# diye bir kontrol kismi, orada sistemsel bilgileri gosteririz; sayfanin en
# sol altinda ve altinda sitenin tanitimi."
#
# Sayfa duzeni:
#   1. sayfa  bilgi sayfasi: marka, konu, ozet, kapak gorseli, belge bilgileri,
#             guncellik kontrolu + QR, site tanitimi
#   2. sayfa+ icindekiler ve icerik (bolumler, hap ozeti, SSS, kontrol listesi)
#   son       "bu belge hakkinda" (surum gecmisi PDF'te DEGIL, sitede: Ahmet
#             28.09 "surum kismi burada degil webde yayinlansa daha mantikli")
#   son sayfa yarisi site tanitimi, yarisi UniConnectly (Ahmet 28.09)
#   her sayfa alt bilgi: solda web ikonu + "ahmetcelen.com.tr - Egitime Bir
#             Tik Katki", sagda kod · surum · sayfa
#
# ⚠️ Okura donuk metinler VARSAYILAN; son hali Ahmet'in (hitap metni kurali).
# Sablon, CSS ya da alt bilgi degisince pdf_veri.SABLON'u 1 artir.
import html

import segno

import pdf_veri as V

k = lambda s: html.escape(str(s), quote=True)   # noqa: E731

# ── okura donuk metinler (VARSAYILAN; Ahmet 28.09 revizyonu islendi) ─────
# Ahmet: "guncellik kontrolu kisminda 'belge tamamen ucretsizdir, size satmaya
# calisanlara taviz gostermeyiniz' tarzi not"; "100 konu diye israr etmeye
# gerek yok"; alt bilgi "ahmetcelen.com.tr - Egitime Bir Tik Katki", alan
# adinin onunde web ikonu. Belge metinleri resmi hitap (-iniz), anlatim
# blogdaki gibi.
SLOGAN = "Eğitime Bir Tık Katkı"
GUNCELLIK = ("Bu belgeyi kullanmadan veya paylaşmadan önce güncelliğinden emin olunuz. "
             "QR kodu okutun ya da adrese girin: elinizdeki sürümün güncel olup olmadığını ve "
             "sonradan düzeltilen bir hata bulunup bulunmadığını gösterir.")
UCRETSIZ = "Bu belge tamamen ücretsizdir. Size satmaya çalışanlara itibar etmeyiniz."
GUNCELLIK_ALT = "Hatalar düzeltildikçe yeni sürüm yayımlanır; bütün değişiklikler sitede sürüm geçmişinde listelenir."
TANITIM = ("Konu anlatımları ve PDF'leri, TYT, AYT, MSÜ, DGS ve KPSS çıkmış soruları, "
           "sınav geri sayımları ve video çözümler. Tamamı ücretsiz.")
SITE_GIRIS = ("Üniversite ve kamu sınavlarına hazırlananlar için ücretsiz matematik kaynakları. "
              "Bu belgenin güncel hâli ve çok daha fazlası sitede.")
SITE_BOLUMLER = [  # (ikon, baslik, aciklama, yol)
    ("liste", "Konu anlatımları", "Baştan sona anlatım, hap bilgiler ve çözümlü örnekler", "/blog/"),
    ("pdf", "PDF merkezi", "Her konunun güncel PDF'i, sürüm geçmişi ve belge doğrulama", "/pdf/"),
    ("sinavda", "Çıkmış sorular", "TYT, AYT, MSÜ, DGS ve KPSS çıkmış soruları", "/ss/"),
    ("saat", "Sınav geri sayımları", "ÖSYM takvimine göre sınavlara kalan süre", "/sinavlar/"),
    ("goz", "Video çözümler", "Konu anlatımı ve soru çözüm videoları", "/video/"),
    ("kontrol", "Belge doğrulama", "Elinizdeki PDF'in güncel ve değiştirilmemiş olduğunu denetleyin", "/d/"),
]


# Son sayfa "Diger yapimlarimiz" (Ahmet 28.09): "Veterito: Hayvanseverlerin sosyal
# medyasi, Veteriner Akilli Klinik Yonetim Uygulamasi; bote.web.tr: Egitim Fakultesi
# ve ogretmenlik dusunenler icin; ucretsiz veriyoruz, bu yapimlari degerlendirip
# bize destek olabilirsiniz; pazarlama %70 agirlikta. UniConnectly alanini kucultme."
DIGER_GIRIS = ("Bu belgeyi ücretsiz hazırlıyoruz. Diğer yapımlarımızı da keşfedin; "
               "kullanmanız ve çevrenizle paylaşmanız bizim için en büyük destek.")
DIGER = [  # (logo dosyasi, ad, kalin metin, devam, adres, gorunen adres)
    ("bote.png", "BÖTE", "Eğitim fakültesi ve öğretmenlik düşünenler için:",
     "bölüm rehberleri, öğretmenlik mesleği ve eğitim teknolojileri üzerine kaynaklı yazılar.",
     "https://bote.web.tr/", "bote.web.tr"),
    ("veterito.png", "Veterito", "Hayvanseverlerin sosyal medyası",
     "ve veteriner akıllı klinik yönetim uygulaması.",
     "https://veterito.com/", "veterito.com"),
]


def _globe(boyut=9, renk="#1860f0"):
    """Alan adinin onundeki web ikonu (Ahmet 28.09). Cizgi ikon, dolgu yok."""
    return (f'<svg width="{boyut}" height="{boyut}" viewBox="0 0 24 24" fill="none" stroke="{renk}" '
            'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" '
            'style="vertical-align:-1px;margin-right:3px">'
            '<circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19"/>'
            '<path d="M12 2.5c2.6 2.6 4 6 4 9.5s-1.4 6.9-4 9.5c-2.6-2.6-4-6-4-9.5s1.4-6.9 4-9.5z"/></svg>')


def qr_svg(adres):
    # Hata duzeltme M (yuzde 15): fotokopide ya da ekranda kucuk lekeye dayanir.
    # Kenar bosluğu 4 modul (standart sessiz bolge); boyut CSS'ten.
    return segno.make(adres, error="m", micro=False).svg_inline(
        scale=1, border=4, dark="#0d2560", light="#ffffff", omitsize=True)


CSS = """
@page { size: A4; margin: 15mm 16mm 17mm 16mm; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
:root { --mor:#1860f0; --mor-koyu:#1250d0; --mor-acik:#eaf1fe; --murekkep:#0d2560;
  --govde:#334155; --soluk:#64748b; --cizgi:#e2e8f0; --cizgi-acik:#f1f5f9; --yuzey:#fff; }
* { box-sizing: border-box; }
body { margin: 0; font: 400 10.4pt/1.58 Inter, system-ui, sans-serif; color: var(--govde); }
h1, h2, h3, .p-kutu-baslik, .p-marka { font-family: Outfit, Inter, sans-serif; color: var(--murekkep); }
a { color: var(--mor-koyu); text-decoration: underline; text-decoration-thickness: .5pt; text-underline-offset: 2pt; }
strong { color: var(--murekkep); font-weight: 600; }
.bs-ikon { width: 1.05em; height: 1.05em; flex: none; vertical-align: -.15em; }

/* 1. sayfa */
.p-bilgi-sayfasi { height: 265mm; display: flex; flex-direction: column; break-after: page; }
.p-marka { display: flex; align-items: center; gap: 8pt; padding-bottom: 8pt;
  border-bottom: 1pt solid var(--cizgi); font-size: 11pt; font-weight: 700; }
.p-marka img { width: 26pt; height: auto; }
.p-marka em { font-style: normal; font-weight: 600; color: var(--soluk); font-size: 9.5pt; }
.p-marka .p-site { margin-left: auto; color: var(--mor); font-size: 10pt; }
.p-rozetler { display: flex; flex-wrap: wrap; gap: 5pt; margin: 14pt 0 6pt; }
.p-etiket { display: inline-flex; align-items: center; gap: 4pt; padding: 2pt 8pt 2pt 6pt; border-radius: 99pt;
  font: 600 8.5pt Inter, sans-serif; color: var(--kat); background: color-mix(in srgb, var(--kat) 9%, #fff);
  border: .6pt solid color-mix(in srgb, var(--kat) 25%, #fff); }
.p-rozet { padding: 2pt 7pt; border-radius: 4pt; background: var(--cizgi-acik); color: var(--soluk);
  font: 600 8.5pt Inter, sans-serif; }
h1 { font-size: 25pt; line-height: 1.12; margin: 2pt 0 8pt; letter-spacing: -.01em; }
.p-ozet { margin: 0 0 10pt; font-size: 10.6pt; }
.p-kapak { display: block; width: 100%; aspect-ratio: 1600 / 901; flex: 0 1 auto; min-height: 0;
  object-fit: contain; border-radius: 6pt; border: .6pt solid var(--cizgi); background: #f5f8ff; }
.p-alt-blok { margin-top: auto; }
.p-bilgi { display: grid; grid-template-columns: 1fr 1.25fr 30mm; gap: 10pt; margin-top: 10pt;
  padding: 10pt 12pt; border: 1pt solid #dbe6fb; background: #f5f8ff; border-radius: 6pt; }
.p-kutu-baslik { margin: 0 0 5pt; font-size: 8.5pt; font-weight: 700; text-transform: uppercase;
  letter-spacing: .06em; color: var(--murekkep); }
.p-kunye dl { display: grid; grid-template-columns: auto 1fr; gap: 1.5pt 8pt; margin: 0; font-size: 8.6pt; }
.p-kunye dt { color: var(--soluk); }
.p-kunye dd { margin: 0; color: var(--murekkep); font-weight: 600; }
.p-kunye dd.p-iz { font-family: ui-monospace, Menlo, monospace; font-weight: 500; letter-spacing: .02em; }
.p-guncellik p { margin: 0 0 4pt; font-size: 8.6pt; line-height: 1.45; }
.p-guncellik .p-adres { font-weight: 700; color: var(--mor-koyu); font-size: 9pt; word-break: break-all; }
.p-guncellik .p-kucuk { color: var(--soluk); font-size: 7.8pt; }
.p-qr svg { display: block; width: 30mm; height: 30mm; }
.p-qr span { display: block; margin-top: 2pt; text-align: center; font-size: 7pt; color: var(--soluk); }
.p-tanitim { display: flex; align-items: center; gap: 10pt; margin-top: 8pt; padding: 9pt 12pt;
  border-radius: 6pt; background: var(--murekkep); color: #dbe6fb; font-size: 8.8pt; line-height: 1.45; }
.p-tanitim b { color: #fff; font-family: Outfit, Inter, sans-serif; font-size: 11pt; white-space: nowrap; }

/* icindekiler */
.p-icindekiler { border: 1pt solid var(--cizgi); border-radius: 6pt; padding: 10pt 14pt; margin-bottom: 12pt;
  break-inside: avoid; }
.p-icindekiler ol { margin: 0; padding-left: 16pt; columns: 2; column-gap: 18pt; font-size: 9.2pt; }
.p-icindekiler li { margin: 0 0 2pt; break-inside: avoid; }
.p-icindekiler a { color: var(--govde); text-decoration: none; }

/* icerik */
h2 { font-size: 14.5pt; line-height: 1.25; margin: 16pt 0 6pt; break-after: avoid; }
h2.bs-h2-ikon { display: flex; align-items: center; gap: 6pt; }
h2 .bs-ikon { width: 15pt; height: 15pt; color: var(--mor); }
h3 { font-size: 12pt; margin: 12pt 0 4pt; break-after: avoid; }
p { margin: 0 0 7pt; orphans: 3; widows: 3; }
ul, ol { margin: 0 0 8pt; padding-left: 16pt; }
li { margin-bottom: 3pt; }
.bs-hap, .bs-dikkat, .bs-ornek, .bs-onkosul, .bs-sinavda {
  border-radius: 5pt; padding: 8pt 11pt; margin: 9pt 0; border: .8pt solid var(--cizgi); background: var(--yuzey);
  break-inside: avoid; }
.bs-hap { border-left: 2.5pt solid var(--mor); background: var(--mor-acik); border-color: #e0e7ff; }
.bs-dikkat { border-left: 2.5pt solid #d97706; background: #fffbeb; border-color: #fde68a; }
.bs-ornek { border-left: 2.5pt solid #0f766e; background: #f0fdfa; border-color: #99f6e4; }
.bs-onkosul { border-left: 2.5pt solid #7c3aed; background: #f5f3ff; border-color: #e4dcfd; }
.bs-sinavda { border-left: 2.5pt solid #0d2560; background: #f5f8ff; border-color: #dbe6fb; }
.bs-hap > b, .bs-dikkat > b, .bs-ornek > b, .bs-onkosul > b, .bs-sinavda > b {
  display: flex; align-items: center; gap: 5pt; font: 600 8.3pt Outfit, Inter, sans-serif;
  text-transform: uppercase; letter-spacing: .05em; margin-bottom: 3pt; }
.bs-hap > b { color: var(--mor-koyu); } .bs-dikkat > b { color: #b45309; } .bs-ornek > b { color: #0f766e; }
.bs-onkosul > b { color: #6d28d9; } .bs-sinavda > b { color: #0d2560; }
.bs-hap p:last-child, .bs-dikkat p:last-child, .bs-ornek p:last-child,
.bs-onkosul p:last-child, .bs-sinavda p:last-child { margin-bottom: 0; }
.bs-gunluk { display: inline-block; margin: 0 0 4pt; padding: 1pt 7pt; border-radius: 99pt;
  background: #ccfbf1; color: #0f766e; font: 600 7.8pt Inter, sans-serif; }
math.mtml { font-family: "Latin Modern Math", "STIX Two Math", "Cambria Math", serif; font-size: 1.08em; }
.mtml-blok { margin: 8pt 0; padding: 7pt 10pt; border: .8pt solid var(--cizgi); border-radius: 5pt;
  text-align: center; break-inside: avoid; }
.mtml-blok math { font-size: 1.18em; }
.bs-tablo { margin: 9pt 0; break-inside: avoid; }
.bs-tablo table { width: 100%; border-collapse: collapse; font-size: 9pt; }
.bs-tablo th, .bs-tablo td { border: .6pt solid var(--cizgi); padding: 4pt 7pt; text-align: left; vertical-align: top; }
.bs-tablo th { background: var(--cizgi-acik); color: var(--murekkep); font-weight: 600; }
.bs-grafik { margin: 9pt 0; padding: 8pt 8pt 6pt; border: .8pt solid var(--cizgi); border-radius: 5pt; break-inside: avoid; }
.bs-grafik svg { display: block; width: 100%; max-width: 120mm; height: auto; margin: 0 auto; }
.bs-grafik text { fill: var(--soluk); font: 500 14px Inter, sans-serif; }
.bs-grafik .g-deger { fill: var(--murekkep); font-weight: 700; }
.bs-grafik .g-izgara { stroke: var(--cizgi); stroke-width: 1; }
.bs-grafik .g-eksen { stroke: var(--soluk); stroke-width: 1.5; }
.bs-grafik .g-sutun { fill: var(--mor); }
.bs-grafik .g-cizgi { fill: none; stroke: var(--mor); stroke-width: 3; stroke-linejoin: round; }
.bs-grafik .g-nokta { fill: #fff; stroke: var(--mor); stroke-width: 3; }
.bs-grafik .g-dilim { stroke: #fff; stroke-width: 2; }
.bs-grafik figcaption { margin-top: 4pt; text-align: center; font-size: 8.5pt; color: var(--soluk); }
.bs-grafik .g-kucuk { font-size: 12px; paint-order: stroke; stroke: #fff; stroke-width: 3px; }
.bs-grafik .g-egri { fill: none; stroke-width: 3; stroke-linejoin: round; stroke-linecap: round; }
.bs-grafik .g-nokta-dolu { fill: var(--murekkep); }
.bs-grafik .g-lejant-zemin { fill: #fff; opacity: .9; stroke: var(--cizgi); }
.bs-grafik .g-yardimci { stroke: var(--soluk); stroke-width: 1.5; stroke-dasharray: 5 4; }
.bs-grafik .g-lejant { fill: var(--murekkep); font-weight: 600; paint-order: stroke; stroke: #fff; stroke-width: 4px; }
.bs-hap-ozet { counter-reset: hapoz; list-style: none; padding-left: 0; }
.bs-hap-ozet > li { counter-increment: hapoz; position: relative; padding: 6pt 9pt 6pt 30pt; margin-bottom: 4pt;
  background: var(--mor-acik); border: .6pt solid #dbe6fb; border-radius: 5pt; break-inside: avoid; }
.bs-hap-ozet > li::before { content: counter(hapoz); position: absolute; left: 8pt; top: 6pt; width: 14pt; height: 14pt;
  border-radius: 50%; background: var(--mor); color: #fff; font: 600 7.5pt/14pt Inter, sans-serif; text-align: center; }
.bs-hap-ozet > li > p:last-child { margin-bottom: 0; }
.p-sss { padding: 6pt 10pt; margin-bottom: 5pt; border: .6pt solid var(--cizgi); border-radius: 5pt; break-inside: avoid; }
.p-sss p { margin: 0; } .p-sss .p-soru { font-weight: 600; color: var(--murekkep); margin-bottom: 2pt; }
.p-kontrol { list-style: none; padding-left: 0; }
.p-kontrol li { position: relative; padding: 3pt 0 3pt 18pt; border-bottom: .5pt dashed var(--cizgi); break-inside: avoid; }
.p-kontrol li::before { content: ""; position: absolute; left: 1pt; top: 5pt; width: 9pt; height: 9pt;
  border: 1pt solid var(--soluk); border-radius: 2pt; }

/* son bolumler */
.p-son { margin-top: 14pt; padding: 10pt 12pt; border: 1pt solid #dbe6fb; background: #f5f8ff; border-radius: 6pt;
  font-size: 8.8pt; break-inside: avoid; }
.p-son p { margin: 0 0 4pt; } .p-son p:last-child { margin: 0; color: var(--soluk); }
.p-ucretsiz { margin-top: 5pt !important; padding: 4pt 7pt; border-radius: 4pt; background: #fff;
  border: .8pt solid #bfd3fb; color: var(--murekkep); font-weight: 600; font-size: 8.3pt !important; }

/* son sayfa: site + UniConnectly tanitimi */
.p-tanitim-sayfasi { break-before: page; height: 265mm; display: flex; flex-direction: column; gap: 8pt; }
.p-yarim { flex: 0 0 auto; border-radius: 8pt; padding: 14pt 16pt; display: flex; flex-direction: column; }
.p-uc-yari { flex: 1 1 auto; }
.p-site-bas { display: flex; gap: 12pt; align-items: flex-start; }
.p-site-bas > div:first-child { flex: 1; }
.p-site-qr { flex: none; text-align: center; font: 600 7.5pt Inter, sans-serif; color: var(--mor-koyu); }
.p-site-qr svg { display: block; width: 21mm; height: 21mm; margin-bottom: 1pt; }
.p-kartlar-3 { grid-template-columns: 1fr 1fr 1fr !important; gap: 6pt !important; }
.p-kartlar-3 .p-kart { padding: 6pt 8pt; }
.p-kartlar-3 .p-kart span { font-size: 7.8pt; }
.p-diger { flex: 0 0 auto; border-radius: 8pt; padding: 12pt 14pt; background: var(--murekkep); color: #cbd5e1; }
.p-diger-bas { margin: 0 0 8pt; font-size: 8.6pt; line-height: 1.45; }
.p-diger-bas b { display: block; color: #fff; font: 700 12pt Outfit, Inter, sans-serif; margin-bottom: 2pt; }
.p-diger-kartlar { display: grid; grid-template-columns: 1fr 1fr; gap: 8pt; }
.p-diger-kart { display: flex; flex-direction: column; gap: 5pt; padding: 9pt 11pt; border-radius: 6pt;
  background: rgba(255,255,255,.07); border: .6pt solid rgba(255,255,255,.16); color: #cbd5e1; text-decoration: none; }
.p-diger-kart img { height: 20pt; width: auto; align-self: flex-start; }
.p-diger-kart p { margin: 0; font-size: 8.4pt; line-height: 1.42; }
.p-diger-kart p b { color: #fff; font-weight: 600; }
.p-diger-kart em { font-style: normal; font: 700 9pt Inter, sans-serif; color: #93c5fd; }
.p-yarim h2 { margin: 0 0 4pt; font-size: 17pt; display: flex; align-items: center; gap: 6pt; }
.p-yarim h2 small { font: 600 11pt Outfit, Inter, sans-serif; color: var(--soluk); }
.p-yarim > p { margin: 0 0 10pt; }
.p-site-yari { background: #f5f8ff; border: 1pt solid #dbe6fb; }
.p-kartlar { display: grid; grid-template-columns: 1fr 1fr; gap: 7pt; }
.p-kart { display: flex; gap: 7pt; padding: 7pt 9pt; background: #fff; border: .8pt solid #dbe6fb; border-radius: 6pt;
  text-decoration: none; color: var(--govde); }
.p-kart .bs-ikon { width: 14pt; height: 14pt; color: var(--mor); margin-top: 1pt; }
.p-kart b { display: block; color: var(--murekkep); font: 600 9.6pt Outfit, Inter, sans-serif; }
.p-kart span { display: block; font-size: 8.2pt; line-height: 1.4; }
.p-kart em { display: block; font-style: normal; font-size: 7.6pt; color: var(--mor-koyu); margin-top: 1pt; }
.p-yarim-alt { margin-top: auto; display: flex; align-items: center; gap: 10pt; padding-top: 10pt; }
.p-yarim-alt svg { width: 24mm; height: 24mm; flex: none; }
.p-yarim-alt p { margin: 0; font-size: 8.8pt; }
.p-yarim-alt strong { font-size: 10pt; }
.p-uc-yari { background: #fff; border: 1pt solid var(--cizgi); }
.p-uc-logo { height: 26pt; width: auto; align-self: flex-start; margin-bottom: 6pt; }
.p-faydalar { list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 6pt 12pt; }
.p-faydalar li { margin: 0; padding-left: 10pt; position: relative; font-size: 8.4pt; line-height: 1.4; }
.p-faydalar li::before { content: ""; position: absolute; left: 0; top: 4pt; width: 4pt; height: 4pt; border-radius: 50%;
  background: var(--mor); }
.p-faydalar b { display: block; color: var(--murekkep); font-size: 9pt; }
.p-rozetler-uc { display: flex; gap: 6pt; margin-top: 6pt; }
.p-rozetler-uc img { height: 22pt; width: auto; }
"""


def alt_bilgi(kod, surum):
    """Chrome'un alt bilgi sablonu (her sayfanin alt kenar boslugu). Web yazi
    tipi burada yuklenmez; sistem yazi tipi kullanilir. Yazi boyu acikca
    verilmezse Chrome cok kucuk basar."""
    return (
        '<div style="width:100%;margin:0 16mm;display:flex;justify-content:space-between;align-items:center;'
        'font-family:\'Helvetica Neue\',Helvetica,Arial,sans-serif;font-size:7.5px;color:#64748b;'
        '-webkit-print-color-adjust:exact;border-top:.5px solid #e2e8f0;padding-top:5px">'
        f'<span>{_globe()}<b style="color:#1860f0;font-size:8px">ahmetcelen.com.tr</b> - {k(SLOGAN)}</span>'
        f'<span>{k(kod)} · Sürüm {k(surum)} · Sayfa <span class="pageNumber"></span> / <span class="totalPages"></span></span>'
        '</div>')


def ust_bilgi():
    return "<div></div>"


def _duz(metin):
    import re
    return re.sub(r"<[^>]+>", "", metin).replace("{ORNEK_OGRENCI}", "").strip()


def son_sayfa(kd):
    """Son sayfa: ustte site, altta UniConnectly (Ahmet 28.09: "pdf'in en sonunda
    matematik blog sitemiz tanitilir, neler yapar; yari sayfasinda UniConnectly").
    UniConnectly metinleri uniconnectly_blok'taki DOGRULANMIS ogrenci faydalari
    (uygulamada olmayan ozellik yazilmaz); baglanti ref/UTM'li, kampanya = belge kodu."""
    import blog_uygula as B
    import uniconnectly_blok as UC
    kartlar = "".join(
        f'<a class="p-kart" href="{V.ALAN}{yol}">{B.ikon(ikon)}<div><b>{k(b)}</b><span>{k(a)}</span>'
        f'<em>ahmetcelen.com.tr{yol}</em></div></a>'
        for ikon, b, a, yol in SITE_BOLUMLER)
    site_qr = V.ALAN + "/pdf/"
    uc_adres = UC.ref("/", "pdf-" + kd.lower()).replace("utm_medium=referral", "utm_medium=pdf")
    faydalar = UC.FAYDALAR["ogrenci"][1]
    faydalar_html = "".join(f"<li><b>{k(b)}</b>{k(_duz(a).split(';')[0])}</li>" for b, a in faydalar)
    rozetler = "".join(f'<img src="/.pdf-yapim/uc/{e.lower().replace(" ", "-")}.png" alt="{k(e)}">'
                       for e, _, _ in UC.MAGAZALAR)
    diger = "".join(
        f'<a class="p-diger-kart" href="{k(adres)}?utm_source=ahmetcelen.com.tr&amp;utm_medium=pdf&amp;utm_campaign={kd.lower()}">'
        f'<img src="/.pdf-yapim/diger/{logo}" alt="{k(ad)}"><p><b>{k(kalin)}</b> {k(devam)}</p><em>{k(gorunen)}</em></a>'
        for logo, ad, kalin, devam, adres, gorunen in DIGER)
    return f'''<section class="p-tanitim-sayfasi">
  <div class="p-yarim p-site-yari">
    <div class="p-site-bas">
      <div><h2>{_globe(18)}ahmetcelen.com.tr <small>- {k(SLOGAN)}</small></h2>
      <p>{k(SITE_GIRIS)}</p></div>
      <a class="p-site-qr" href="{site_qr}">{qr_svg(site_qr)}PDF merkezi</a>
    </div>
    <div class="p-kartlar p-kartlar-3">{kartlar}</div>
  </div>
  <div class="p-yarim p-uc-yari">
    <img class="p-uc-logo" src="/.pdf-yapim/uc/logo.webp" alt="UniConnectly">
    <p>Üniversite topluluklarını, etkinlikleri ve şirketleri tek uygulamada buluşturan ücretsiz kampüs platformu.</p>
    <ul class="p-faydalar">{faydalar_html}</ul>
    <div class="p-yarim-alt">{qr_svg(uc_adres)}<p><strong>Ücretsiz keşfet</strong><br>QR kodu okutun ya da <a href="{k(uc_adres)}">uniconnectly.com</a> adresine girin.
      <span class="p-rozetler-uc">{rozetler}</span></p></div>
  </div>
  <div class="p-diger">
    <p class="p-diger-bas"><b>Diğer yapımlarımız</b>{k(DIGER_GIRIS)}</p>
    <div class="p-diger-kartlar">{diger}</div>
  </div>
</section>'''


def belge(no, y, s):
    """Yazdirilacak tam HTML. `s`: basilan surum kaydi."""
    import blog_uygula as B
    import blog_veri
    kd = V.kod(no)
    dogrula = V.ALAN + V.dogrulama_yolu(kd, s["surum"])
    dogrula_kisa = dogrula.replace("https://", "")
    kat_renk = blog_veri.KAT_RENK.get(y["kategori"], "#1860f0")
    etiket = (f'<span class="p-etiket" style="--kat:{kat_renk}">'
              + B.ikon(blog_veri.KAT_IKON.get(y["kategori"], "fonksiyonlar"))
              + k(B.KAT.get(y["kategori"], y["kategori"])) + "</span>")
    rozetler = etiket + "".join(f'<span class="p-rozet">{k(x)}</span>' for x in y.get("sinavlar", []))
    # Kapak JPEG olarak gomulur (pdf_uret.kapak_jpg): AVIF'i Chrome PDF'e
    # sikistirmasiz (FlateDecode) yaziyordu, 12 sayfalik belge 3,1 MB oldu.
    kapak = (f'<img class="p-kapak" src="/.pdf-yapim/kapak/{k(y["kapak"])}.jpg" alt="{k(y.get("kapak_alt", ""))}">'
             if y.get("kapak") else '<div class="p-kapak" style="background:#f5f8ff"></div>')
    toc = "".join(f'<li><a href="#{k(i)}">{k(b)}</a></li>' for i, b in V.bolumler(y))
    gecmis_adres = V.ALAN + V.dogrulama_yolu(kd)
    return f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<title>{k(y["baslik"])} · {kd} Sürüm {k(s["surum"])}</title>
<link rel="stylesheet" href="/css/blog-yazitipleri.css">
<style>{CSS}</style>
</head>
<body>
<section class="p-bilgi-sayfasi">
  <header class="p-marka"><img src="/blog/kapak/ac-monogram.avif" alt=""><span>Ahmet Çelen</span><em>Matematik Konu Anlatımı</em><span class="p-site">{_globe(10)}ahmetcelen.com.tr</span></header>
  <div class="p-rozetler">{rozetler}</div>
  <h1>{k(y["baslik"])}</h1>
  <p class="p-ozet">{B.mm(k(y["ozet"]))}</p>
  {kapak}
  <div class="p-alt-blok">
  <div class="p-bilgi">
    <div class="p-kunye">
      <p class="p-kutu-baslik">Belge bilgileri</p>
      <dl>
        <dt>Belge kodu</dt><dd>{kd}</dd>
        <dt>Yazı no</dt><dd>{no}</dd>
        <dt>Sürüm</dt><dd>{k(s["surum"])}</dd>
        <dt>Sürüm tarihi</dt><dd>{V.tr_tarih(s["tarih"])}</dd>
        <dt>İçerik izi</dt><dd class="p-iz">{V.parmak_izi(s["icerik"])}</dd>
        <dt>Yayımlayan</dt><dd>ahmetcelen.com.tr</dd>
      </dl>
    </div>
    <div class="p-guncellik">
      <p class="p-kutu-baslik">Güncellik kontrolü</p>
      <p>{k(GUNCELLIK)}</p>
      <p class="p-adres"><a href="{k(dogrula)}">{k(dogrula_kisa)}</a></p>
      <p class="p-kucuk">{k(GUNCELLIK_ALT)}</p>
      <p class="p-ucretsiz">{k(UCRETSIZ)}</p>
    </div>
    <div class="p-qr"><a href="{k(dogrula)}">{qr_svg(dogrula)}</a><span>Güncelliği kontrol et</span></div>
  </div>
  <aside class="p-tanitim"><b>{_globe(12, "#ffffff")}ahmetcelen.com.tr</b><span>{k(TANITIM)}</span></aside>
  </div>
</section>
<nav class="p-icindekiler" aria-label="İçindekiler">
  <p class="p-kutu-baslik">İçindekiler</p>
  <ol>{toc}</ol>
</nav>
<main>
{V.govde(y)}
</main>
<section class="p-son">
  <p><strong>Bu belge hakkında.</strong> Bu PDF, ahmetcelen.com.tr'deki <a href="{V.ALAN}/blog/{k(y["slug"])}/">{k(y["baslik"])}</a> yazısının {kd} kodlu belgesinin {k(s["surum"])} sürümüdür.</p>
  <p>Sürüm geçmişi ve değişiklikler: <a href="{k(gecmis_adres)}">{k(gecmis_adres.replace("https://", ""))}</a>. Güncel sürümü ve bütün konuların PDF'lerini <a href="{V.ALAN}/pdf/">ahmetcelen.com.tr/pdf/</a> adresinde bulabilirsiniz. Elinizdeki dosyanın bizim yayımladığımız sürümle birebir aynı olup olmadığını <a href="{V.ALAN}/d/">ahmetcelen.com.tr/d/</a> adresinde denetleyebilirsiniz; dosya cihazınızdan dışarı gönderilmez.</p>
  <p>© {s["tarih"][:4]} ahmetcelen.com.tr · {k(SLOGAN)}</p>
</section>
{son_sayfa(kd)}
</body>
</html>
'''
