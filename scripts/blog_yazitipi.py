#!/usr/bin/env python3
# scripts/blog_yazitipi.py — Google Fonts'u kendi sunucumuza alir (22.09.2026)
#
# NEDEN: yazi tipleri fonts.googleapis.com'dan CSS, fonts.gstatic.com'dan
# dosya olarak geliyordu. Mobilde bu IKI AYRI kaynak demek: her biri icin
# DNS + TCP + TLS (~3 gidis-donus, olculen RTT 190 ms). Ustelik font
# istekleri CSS inmeden BASLAYAMIYOR. Kendi alan adimizdan verince bu
# el sikismalar tamamen kalkar ve dosya on yuklenebilir.
#
# KAPSAM: yalniz `latin` ve `latin-ext` altkumeleri. Turkce harflerin
# (ı, İ, ş, ğ, ç, ö, ü) tamami bu ikisinde; kiril/yunan/vietnam altkumeleri
# indirilmiyordu zaten, dosya olarak da tutulmuyor.
#
# Lisans: Inter ve Outfit SIL Open Font License; kendi sunucudan
# yayimlamak serbest.
#
# Kullanim: .venv/bin/python scripts/blog_yazitipi.py   (fontTools gerekir)   (tek seferlik; fontlar
# depoda duruyor, tekrar calistirmak gerekmez)
import hashlib, io, re, pathlib, urllib.request

# Blogun GERCEKTEN kullandigi karakterler. Google'in latin-ext altkumesi
# 85 KB (Inter): Vietnamca, Baltik, bircok aksan... hicbiri bu sitede
# gecmiyor. Alt kumeye indirince yalniz Turkce ek harfler kaliyor.
# Formuller MathML ile diziliyor ve KENDI yazi tipini kullaniyor, bu
# yuzden matematik sembolleri buraya girmez.
KARAKTERLER = (
    "".join(chr(c) for c in range(0x20, 0x7F))
    + "çÇğĞıİöÖşŞüÜâÂîÎûÛ"
    + "\u00a0\u2018\u2019\u201c\u201d\u2013\u2014\u2026\u00b7"
    + "\u00b0\u00d7\u2192\u2197\u2713\u20ba%&@"
)


def altkumele(veri, aralik):
    """woff2'yi KARAKTERLER ile sinirlar; bos kalirsa None doner."""
    from fontTools import subset
    from fontTools.ttLib import TTFont
    f = TTFont(io.BytesIO(veri), fontNumber=0)
    kapsam = set()
    for tablo in f["cmap"].tables:
        kapsam |= set(tablo.cmap)
    istenen = {ord(c) for c in KARAKTERLER} & kapsam
    if not istenen:
        return None
    o = subset.Options()
    o.layout_features = ["kern", "liga", "calt", "ccmp", "locl"]
    o.drop_tables += ["DSIG"]
    o.notdef_outline = True
    s_ = subset.Subsetter(options=o)
    s_.populate(unicodes=istenen)
    s_.subset(f)
    f.flavor = "woff2"
    tampon = io.BytesIO()
    f.save(tampon)
    return tampon.getvalue()


KOK = pathlib.Path(__file__).resolve().parent.parent
HEDEF_DIZIN = KOK / "fonts/webfont"
# Blog kabugu ana temadan AYRI: Ahmet "blog tasarimi komple farkli olacak,
# uniconnectly web sitesi gibi modern" dedi. UniConnectly Inter (govde) +
# Outfit (baslik) kullaniyor (22.09'da olculdu); ayni ikili aliniyor.
ADRES = ("https://fonts.googleapis.com/css?family=Inter:400,500,600,700"
         "|Outfit:600,700&display=swap")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")
# latin ve latin-ext altkumelerinin ayirt edici aralilari
LATIN = "U+0000-00FF"
LATIN_EXT = "U+0100-02BA"

def indir(u):
    r = urllib.request.Request(u, headers={"User-Agent": UA})
    with urllib.request.urlopen(r, timeout=30) as f:
        return f.read()

def uygula():
    HEDEF_DIZIN.mkdir(parents=True, exist_ok=True)
    css = indir(ADRES).decode("utf-8")
    bloklar = re.findall(r"@font-face\s*\{[^}]*\}", css)
    cikti, n, gorulen = [], 0, {}
    for b in bloklar:
        ar = re.search(r"unicode-range:\s*([^;]+);", b)
        if not ar or not (LATIN in ar.group(1) or LATIN_EXT in ar.group(1)):
            continue
        u = re.search(r"url\((https://[^)]+\.woff2)\)", b)
        aile = re.search(r"font-family:\s*'([^']+)'", b).group(1)
        agirlik = re.search(r"font-weight:\s*(\d+)", b).group(1)
        altkume = "latin" if LATIN in ar.group(1) else "latinext"
        veri = indir(u.group(1))
        # TEKILLESTIRME ALT KUMELEMEDEN ONCE yapilir: Google degisken yazi
        # tipinde 400/500/600/700 icin AYNI dosyayi veriyor, ama alt kumeleme
        # her seferinde bayt bayt ayni ciktiyi uretmiyor. Once indirilenin
        # ozetine bakilir, sonra bir kez alt kumelenir.
        ozet = hashlib.sha256(veri).hexdigest()[:8]
        # Nunito DEGISKEN yazi tipi: Google 400/500/600/700 icin AYNI dosyayi
        # veriyor (olculdu, dort dosyanin ozeti ayni). Icerik ozetine gore
        # tekillestirip tek @font-face'te agirlik ARALIGI bildiriyoruz;
        # aksi halde ayni 38 KB dort kez depoda duruyordu.
        anahtar = (aile, altkume, ozet)
        if anahtar in gorulen:
            gorulen[anahtar][1].append(int(agirlik))
            continue
        kucuk = altkumele(veri, ar.group(1))
        if kucuk is None:
            continue                      # bu altkumede kullandigimiz harf yok
        ad = f"{aile.lower().replace(' ', '-')}-{altkume}-{hashlib.sha256(kucuk).hexdigest()[:8]}.woff2"
        (HEDEF_DIZIN / ad).write_bytes(kucuk)
        n += 1
        gorulen[anahtar] = (ad, [int(agirlik)], ar.group(1).strip(), aile)
    for ad, agirliklar, aralik, aile in gorulen.values():
        a = (str(agirliklar[0]) if len(agirliklar) == 1
             else f"{min(agirliklar)} {max(agirliklar)}")
        cikti.append(
            "@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
            "font-display:swap;src:url('/fonts/webfont/%s') format('woff2');"
            "unicode-range:%s}" % (aile, a, ad, aralik))
    (KOK / "css/blog-yazitipleri.css").write_text(
        "/* Uretici: scripts/blog_yazitipi.py — ELLE DUZENLEME */\n"
        + "\n".join(cikti) + "\n", encoding="utf-8")
    toplam = sum(p.stat().st_size for p in HEDEF_DIZIN.glob("*.woff2"))
    print(f"blog yazi tipi: {n} dosya · {toplam//1024} KB · css/blog-yazitipleri.css yazildi")

if __name__ == "__main__":
    uygula()
