#!/usr/bin/env python3
# scripts/menu_uygula.py — ust menuyu (masaustu + mobil) TEK kaynaktan
# butun sayfalara basar.
#
# Neden: menu 23 sayfada ayri ayri gomulu; her degisiklik 23 dosyaya elle
# yaziliyordu ve sayfalar birbirinden ayrismisti. Artik menu asagidaki MENU
# listesinde tanimlanir, bu betik iki menuyu (masaustu `#respMenu`, mobil
# `nav#menu`) uretip sayfalara yerlestirir.
#
# Kullanim:
#   python3 scripts/menu_uygula.py            # uygular
#   python3 scripts/menu_uygula.py --kuru     # ne degisecegini yazar, yazmaz
#
# Kurallar:
# - Baglantilar GORELI (/yol): site hangi alan adinda yayindaysa oraya gider.
# - Olmayan sayfaya baglanti verilmez (denemeler/, anketler, telegramhome,
#   redirect/socialmedia bu sitede yok → menuden cikarildi).
# - Sponsor ve Ozel Ders sayfalari kaldirildi (Ahmet, 21.09).
import re, sys, pathlib, html

KOK = pathlib.Path(__file__).resolve().parent.parent
KURU = "--kuru" in sys.argv

def yt(q):
    return "https://www.youtube.com/results?search_query=" + q

# (etiket, href, alt_ogeler | None, yeni_sekme)
MENU = [
    ("Ana Sayfa", "/", None, False),
    ("Ders Notları", "/pdfnot/", [
        ("TYT Matematik Deneme", "/yt/tytmat.pdf", None, True),
        ("AYT Matematik Deneme", "/yt/aytmat.pdf", None, True),
        ("DGS Matematik Deneme", "/yt/dgsmat.pdf", None, True),
        # kpssmat.pdf / alesmat.pdf: eski menude vardi, dosya hicbir yerde yok
        # (repo + medya sunucusu tarandi, 21.09) → 404 vermesin diye cikarildi.
        ("TYT Son Prova", "/yt/2021denemeler/tytmatsonprova.pdf", None, True),
        ("AYT Son Prova", "/yt/2021denemeler/aytmatsonprova.pdf", None, True),
        ("Parabol Fasikülü", "/pdf/parabol.pdf", None, True),
        ("Tüm Notlar (Google Drive)",
         "https://drive.google.com/drive/folders/1rjDxAuM4c1mmqp_X-BTmfoJCCFFlahcU?usp=sharing", None, True),
    ], False),
    ("Videolar", "/video/", [
        ("YouTube Kanalı", "/youtube/", None, False),
        ("Konu Anlatımları", "/video/konu.html", None, False),
        ("Parabol Fasikülü Çözümleri", "/video/parabol.html", None, False),
        ("Rehberlik", yt("ahmet+%C3%A7elen+rehberlik"), None, True),
        ("TYT", yt("ahmet+%C3%A7elen+tyt"), None, True),
        ("AYT", yt("ahmet+%C3%A7elen+ayt"), None, True),
        ("DGS", yt("ahmet+%C3%A7elen+dgs"), None, True),
        ("KPSS", yt("ahmet+%C3%A7elen+kpss"), None, True),
        ("Konulara Göre", yt("ahmet+%C3%A7elen+matematik"), [
            ("Problemler", yt("ahmet+%C3%A7elen+problemler"), None, True),
            ("Mantık", yt("ahmet+%C3%A7elen+mant%C4%B1k"), None, True),
            ("Mutlak Değer", yt("ahmet+%C3%A7elen+mutlak+de%C4%9Fer"), None, True),
            ("Üslü ve Köklü Sayılar", yt("ahmet+%C3%A7elen+%C3%BCsl%C3%BC+ve+k%C3%B6kl%C3%BC+say%C4%B1lar"), None, True),
            ("Polinomlar", yt("ahmet+%C3%A7elen+polinomlar"), None, True),
            ("Parabol", yt("ahmet+%C3%A7elen+parabol"), None, True),
            ("İkinci Dereceden Denklemler", yt("ahmet+%C3%A7elen+ikinci+dereceden+denklemler"), None, True),
            ("Eşitsizlikler", yt("ahmet+%C3%A7elen+e%C5%9Fitsizlikler"), None, True),
            ("Trigonometri", yt("ahmet+%C3%A7elen+trigonometri"), None, True),
            ("Logaritma", yt("ahmet+%C3%A7elen+logaritma"), None, True),
            ("Diziler", yt("ahmet+%C3%A7elen+diziler"), None, True),
            ("Limit", yt("ahmet+%C3%A7elen+limit"), None, True),
            ("Türev", yt("ahmet+%C3%A7elen+t%C3%BCrev"), None, True),
            ("İntegral", yt("ahmet+%C3%A7elen+integral"), None, True),
            ("Analitik Geometri", yt("ahmet+%C3%A7elen+analitik+geometri"), None, True),
        ], True),
    ], False),
    # "Sınavlar" = Çıkmış Sorular + Sınavlara Geri Sayım (Ahmet, 21.09).
    # ADRESLER SABIT: /ss/* ve /sinavlar/* arama trafiginde onde, oturmus
    # sayfalar; yalniz menu etiketleri degisti.
    ("Sınavlar", "/sinavlar/", [
        ("Çıkmış Sorular", "/ss/tyt/", [
            ("TYT Çıkmış Sorular", "/ss/tyt/", None, False),
            ("AYT Çıkmış Sorular", "/ss/ayt/", None, False),
            ("MSÜ Çıkmış Sorular", "/ss/msu/", None, False),
            ("DGS Çıkmış Sorular", "/ss/dgs/", None, False),
            ("KPSS Çıkmış Sorular", "/ss/kpss/", None, False),
        ], False),
        ("Sınavlara Geri Sayım", "/sinavlar/", [
            ("Tüm Sınavlar", "/sinavlar/", None, False),
            ("TYT Geri Sayım", "/sinavlar/tyt/", None, False),
            ("AYT Geri Sayım", "/sinavlar/ayt/", None, False),
            ("MSÜ Geri Sayım", "/sinavlar/msu/", None, False),
            ("DGS Geri Sayım", "/sinavlar/dgs/", None, False),
            ("KPSS Geri Sayım", "/sinavlar/kpssa/", None, False),
            ("ALES/1 Geri Sayım", "/sinavlar/ales1/", None, False),
            ("ALES/2 Geri Sayım", "/sinavlar/ales2/", None, False),
            ("ALES/3 Geri Sayım", "/sinavlar/ales3/", None, False),
        ], False),
    ], False),
    ("İletişim", "/iletisim/", [
        ("Hakkımda", "/hakkimizda/", None, False),
        ("İletişim", "/iletisim/", None, False),
        ("Soru Çözüm Grubu", "/sorucozumgrubu/", None, False),
    ], False),
]

def a(etiket, href, yeni_sekme, sinif=None):
    ek = ' target="_blank" rel="noopener noreferrer"' if yeni_sekme else ""
    ek += f' class="{sinif}"' if sinif else ""
    return f'<a href="{html.escape(href, quote=True)}"{ek}>'

def masaustu(ogeler, seviye=0):
    pad = "\t\t    " + "    " * seviye
    out = []
    for etiket, href, alt, ys in ogeler:
        if seviye == 0:
            out.append(f'{pad}<li>')
            out.append(f'{pad}    {a(etiket, href, ys)}<span class="title">{html.escape(etiket)}</span></a>')
        else:
            out.append(f'{pad}<li>{a(etiket, href, ys)}{html.escape(etiket)}</a>' + ("" if alt else "</li>"))
        if alt:
            out.append(f'{pad}    <ul>')
            out.extend(masaustu(alt, seviye + 1))
            out.append(f'{pad}    </ul>')
            out.append(f'{pad}</li>')
        elif seviye == 0:
            out.append(f'{pad}</li>')
    return out

def mobil(ogeler, seviye=0):
    pad = "\t\t\t" + "\t" * seviye
    out = []
    for etiket, href, alt, ys in ogeler:
        if alt:
            out.append(f'{pad}<li><span>{html.escape(etiket)}</span>')
            out.append(f'{pad}\t<ul>')
            # Ust maddenin kendi sayfasi alt listede zaten varsa ikinci kez yazma.
            if href not in {h for _, h, _, _ in alt}:
                out.append(f'{pad}\t\t<li>{a(etiket, href, ys)}{html.escape(etiket)} sayfası</a></li>')
            out.extend(mobil(alt, seviye + 1))
            out.append(f'{pad}\t</ul>')
            out.append(f'{pad}</li>')
        else:
            out.append(f'{pad}<li>{a(etiket, href, ys)}{html.escape(etiket)}</a></li>')
    return out

MASAUSTU_HTML = (
    '<ul id="respMenu" class="ace-responsive-menu" data-menu-style="horizontal">\n'
    + "\n".join(masaustu(MENU)) + "\n\t\t    </ul></nav>"
)
MOBIL_HTML = (
    '<nav id="menu" class="stylehome1">\n\t\t\t<ul>\n'
    + "\n".join(mobil(MENU)) + "\n\t\t\t</ul>\n\t\t</nav>"
)

RE_MASAUSTU = re.compile(r'<ul id="respMenu".*?</nav>', re.S)
RE_MOBIL = re.compile(r'<nav id="menu" class="stylehome1">.*?</nav>', re.S)
RE_LOGO_BOS = re.compile(r'<a href="#" class="navbar_brand')

def sayfalar():
    for p in KOK.rglob("*.html"):
        rel = p.relative_to(KOK).as_posix()
        if rel.startswith(("temaindexler/", "okyanus/")) or "/tema/" in rel or "/errors/" in rel:
            continue
        yield p

degisen = 0
for p in sayfalar():
    s0 = p.read_text(encoding="utf-8", errors="surrogateescape")
    if 'id="respMenu"' not in s0:
        continue
    s = s0
    notlar = []
    if RE_MASAUSTU.search(s):
        s = RE_MASAUSTU.sub(lambda m: MASAUSTU_HTML, s, count=1); notlar.append("masaustu")
    if RE_MOBIL.search(s):
        s = RE_MOBIL.sub(lambda m: MOBIL_HTML, s, count=1); notlar.append("mobil")
    if RE_LOGO_BOS.search(s):
        s = RE_LOGO_BOS.sub('<a href="/" class="navbar_brand', s); notlar.append("logo→/")
    if s != s0:
        degisen += 1
        print(f"{'KURU ' if KURU else ''}{p.relative_to(KOK)}: {', '.join(notlar)}")
        if not KURU:
            p.write_text(s, encoding="utf-8", errors="surrogateescape")
print(f"\n{degisen} sayfa {'degisecek' if KURU else 'guncellendi'}.")
