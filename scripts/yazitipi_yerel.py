#!/usr/bin/env python3
# scripts/yazitipi_yerel.py — Google Fonts'u kendi sunucumuza alir (22.09.2026)
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
# Lisans: Nunito ve Open Sans SIL Open Font License; kendi sunucudan
# yayimlamak serbest.
#
# Kullanim: python3 scripts/yazitipi_yerel.py   (tek seferlik; fontlar
# depoda duruyor, tekrar calistirmak gerekmez)
import hashlib, re, pathlib, urllib.request

KOK = pathlib.Path(__file__).resolve().parent.parent
HEDEF_DIZIN = KOK / "fonts/webfont"
ADRES = ("https://fonts.googleapis.com/css?family=Nunito:400,500,600,700"
         "|Open+Sans&display=swap")
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
        ozet = hashlib.sha256(veri).hexdigest()[:8]
        # Nunito DEGISKEN yazi tipi: Google 400/500/600/700 icin AYNI dosyayi
        # veriyor (olculdu, dort dosyanin ozeti ayni). Icerik ozetine gore
        # tekillestirip tek @font-face'te agirlik ARALIGI bildiriyoruz;
        # aksi halde ayni 38 KB dort kez depoda duruyordu.
        anahtar = (aile, altkume, ozet)
        if anahtar in gorulen:
            gorulen[anahtar][1].append(int(agirlik))
            continue
        ad = f"{aile.lower().replace(' ', '-')}-{altkume}-{ozet}.woff2"
        (HEDEF_DIZIN / ad).write_bytes(veri)
        n += 1
        gorulen[anahtar] = (ad, [int(agirlik)], ar.group(1).strip(), aile)
    for ad, agirliklar, aralik, aile in gorulen.values():
        a = (str(agirliklar[0]) if len(agirliklar) == 1
             else f"{min(agirliklar)} {max(agirliklar)}")
        cikti.append(
            "@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
            "font-display:swap;src:url('/fonts/webfont/%s') format('woff2');"
            "unicode-range:%s}" % (aile, a, ad, aralik))
    (KOK / "css/yazitipleri.css").write_text(
        "/* Uretici: scripts/yazitipi_yerel.py — ELLE DUZENLEME */\n"
        + "\n".join(cikti) + "\n", encoding="utf-8")
    toplam = sum(p.stat().st_size for p in HEDEF_DIZIN.glob("*.woff2"))
    print(f"yazi tipi: {n} dosya · {toplam//1024} KB · css/yazitipleri.css yazildi")

if __name__ == "__main__":
    uygula()
