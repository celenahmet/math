#!/usr/bin/env python3
# scripts/css_azalt.py — tema stil dosyalarini sitede GECEN seciciyle
# sinirlar (22.09.2026).
#
# OLCUM (canli mobil, /ss/kpss/): ikon ve betik budamasindan sonra geriye
# kalan en buyuk engelleyici yuk CSS. style.css 285 KB, bootstrap.min.css
# 155 KB; ikisi de "Edumy LMS" temasinin TAM dagitimi — kurs listesi, magaza,
# panel, takvim, forum ekranlari sitede yok ama kurallari iniyor.
#
# YONTEM (PurgeCSS mantigi): bir secici, icindeki TUM sinif/kimlik adlari
# sitede geciyorsa korunur. Gecmeyen tek bir ad bile varsa secici atilir;
# secicilerin hepsi atilirsa kural silinir. Sinif/kimlik icermeyen seciciler
# (body, a:hover, [data-x]) her zaman korunur — ucuz ve risksiz.
#
# "Geciyor" kumesi GENIS tutulur, cunku sinifi CSS'e degil calisma anina
# borclu olanlar var:
#   · HTML'deki class/id degerleri
#   · JS dosyalarindaki METIN sabitleri (mmenu 'mm-opened', tema 'menu-active',
#     'stricky-fixed' gibi sinifları calisma aninda ekliyor)
# Bu yuzden tarama kaynaklari HTML *ve* JS. Bir sinif ikisinde de yoksa
# gercekten kullanilmiyordur.
#
# Cikti AYRI dosyaya yazilir (css/<ad>-az.css); orijinal durur, geri donus
# tek satir. @font-face, @keyframes ve @media korunur (@media icerigi suzulur).
#
# Kullanim: python3 scripts/css_azalt.py [--kuru]
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
HARIC = ("arsiv", "okyanus", "temaindexler", "scripts")
KURU = "--kuru" in sys.argv

HEDEFLER = ["css/bootstrap.min.css", "css/style.css", "css/responsive.css",
            "css/menu.css", "css/ace-responsive-menu.css", "css/megadropdown.css",
            "css/slider.css"]

# ── kullanilan adlar ──────────────────────────────────────────────────────
# Etkilesimle olusan siniflar DOM dokumune de girmez (mobil menu ancak
# dokununca kuruluyor). Bu on ekler kosulsuz korunur.
KORUNAN_ON_EK = ("mm-", "mm_", "sub-menu", "menu-active", "stricky", "slick-",
                 "animated", "collaps", "show", "open", "active", "disabled",
                 "selected", "hover", "focus", "owl-")

# DOM dokumu: sayfalar tarayicida CALISTIKTAN SONRA serilestirilir. Owl
# carousel gibi eklentiler sinifi (owl-stage, owl-item) calisma aninda
# uretiyor; statik HTML taramasi bunlari goremedigi icin ilk turda ana
# sayfanin tamami budanmisti. Dokum klasoru varsa taramaya dahil edilir.
DOM_KLASORU = pathlib.Path("/private/tmp/claude-501") if False else None


def kullanilan_adlar(dom_klasoru=None):
    sinif, kimlik = set(), set()
    kaynaklar = list(KOK.rglob("*.html"))
    if dom_klasoru:
        kaynaklar += sorted(pathlib.Path(dom_klasoru).glob("*.html"))
    for p in kaynaklar:
        try:
            if p.relative_to(KOK).parts[0] in HARIC:
                continue
        except ValueError:
            pass                                  # DOM dokumu: KOK disinda
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for m in re.finditer(r'class="([^"]*)"', s):
            sinif.update(m.group(1).split())
        for m in re.finditer(r'id="([^"]*)"', s):
            kimlik.update(m.group(1).split())
    # JS: metin sabitlerindeki her ad aday kabul edilir (genis taraf)
    for p in KOK.rglob("*.js"):
        if p.relative_to(KOK).parts[0] in HARIC:
            continue
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for m in re.finditer(r"""['"]([^'"\n]{1,120})['"]""", s):
            for t in re.findall(r"[A-Za-z][A-Za-z0-9_-]{1,}", m.group(1)):
                sinif.add(t)
                kimlik.add(t)
    return sinif, kimlik

# ── kucuk CSS ayristirici (metin ve yorum farkindaligi ile) ───────────────
def dugumler(s, bas=0, bit=None):
    """[(tur, on_metin, govde_baslangic, govde_bitis)] dondurur."""
    bit = len(s) if bit is None else bit
    cikti, i, on = [], bas, bas
    while i < bit:
        c = s[i]
        if c == "/" and s[i:i + 2] == "/*":
            j = s.find("*/", i + 2)
            i = bit if j < 0 else j + 2
            continue
        if c in "\"'":
            j = i + 1
            while j < bit and s[j] != c:
                j += 2 if s[j] == "\\" else 1
            i = j + 1
            continue
        if c == "}":
            # BASIBOS kapanis. css/style.css'te bir fazla "}" var (2256 "{",
            # 2257 "}"); tarayici toparliyor, duz ayristirici KAYIYOR ve bundan
            # sonraki her kural yanlis yerde kaliyordu ("display: flex;}" gibi
            # bildirim parcalari ciktiya sizmisti). Atla, sirayi bozma.
            i += 1
            on = i
            continue
        if c == ";":
            cikti.append(("ifade", s[on:i + 1], None, None))
            i += 1
            on = i
            continue
        if c == "{":
            derinlik, j = 1, i + 1
            while j < bit and derinlik:
                k = s[j]
                if k == "/" and s[j:j + 2] == "/*":
                    j = s.find("*/", j + 2)
                    j = bit if j < 0 else j + 2
                    continue
                if k in "\"'":
                    m = j + 1
                    while m < bit and s[m] != k:
                        m += 2 if s[m] == "\\" else 1
                    j = m + 1
                    continue
                derinlik += 1 if k == "{" else (-1 if k == "}" else 0)
                j += 1
            cikti.append(("blok", s[on:i], i + 1, j - 1))
            i = j
            on = i
            continue
        i += 1
    if s[on:bit].strip():
        cikti.append(("ifade", s[on:bit], None, None))
    return cikti

def secici_parcala(sec):
    """Virgulle ayir, ama parantez icindeki virgule dokunma (:not(a,b))."""
    parca, derinlik, son = [], 0, 0
    for i, c in enumerate(sec):
        if c == "(":
            derinlik += 1
        elif c == ")":
            derinlik -= 1
        elif c == "," and derinlik == 0:
            parca.append(sec[son:i])
            son = i + 1
    parca.append(sec[son:])
    return [p.strip() for p in parca if p.strip()]

AD = re.compile(r"([.#])(-?[A-Za-z_][A-Za-z0-9_-]*)")
YORUM = re.compile(r"/\*.*?\*/", re.S)

def secici_gecerli(sec, sinif, kimlik):
    for isaret, ad in AD.findall(sec):
        if ad.startswith(KORUNAN_ON_EK):
            continue
        if isaret == "." and ad not in sinif:
            return False
        if isaret == "#" and ad not in kimlik:
            return False
    return True

KORUNAN_AT = ("@font-face", "@keyframes", "@-webkit-keyframes", "@-moz-keyframes",
              "@-o-keyframes", "@page", "@charset", "@import", "@namespace",
              "@counter-style", "@viewport", "@-ms-viewport", "@property")

def suz(s, bas, bit, sinif, kimlik):
    cikti = []
    for tur, on, gb, gs in dugumler(s, bas, bit):
        if tur == "ifade":
            g = on.strip()
            # Yalniz at-kuralini gecir (@charset/@import). Govdeden sizan
            # bildirim parcasi ("display: flex;") CSS'i gecersiz kilar.
            if g.startswith("@"):
                cikti.append(g)
            continue
        # Secici onunden YORUMLARI at. Yoksa virgulle bolme yorumun icine
        # girip onu ortadan kesiyor: "/*== Fonts Size,Font Weights ==*/.fz11"
        # → ".fz11" atilinca geriye KAPANMAMIS "/*== Fonts Size" kaliyor ve
        # o noktadan sonraki ~20 kurali yutuyordu (.p0, .pt25, .mt20 ...).
        on_t = YORUM.sub(" ", on).strip()
        if on_t.startswith("@"):
            ad = on_t.split()[0].split("(")[0].lower()
            if ad.startswith(KORUNAN_AT):
                cikti.append(on_t + "{" + s[gb:gs] + "}")
                continue
            ic = suz(s, gb, gs, sinif, kimlik)          # @media / @supports
            if ic.strip():
                cikti.append(on_t + "{" + ic + "}")
            continue
        kalan = [x for x in secici_parcala(on_t) if secici_gecerli(x, sinif, kimlik)]
        if kalan and s[gb:gs].strip():
            cikti.append(",".join(kalan) + "{" + s[gb:gs].strip() + "}")
    return "".join(cikti)

def uygula(dom_klasoru=None):
    sinif, kimlik = kullanilan_adlar(dom_klasoru)
    print(f"taranan ad: {len(sinif)} sinif · {len(kimlik)} kimlik")
    toplam_e = toplam_y = 0
    for yol in HEDEFLER:
        p = KOK / yol
        s = p.read_text(encoding="utf-8")
        y = suz(s, 0, len(s), sinif, kimlik)
        hedef = KOK / yol.replace(".min.css", ".css").replace(".css", "-az.css")
        if not KURU:
            if y.strip():
                hedef.write_text(y, encoding="utf-8")
            else:
                hedef.unlink(missing_ok=True)   # bos cikti: dosya hic olusmasin
        toplam_e += len(s)
        toplam_y += len(y)
        print(f"  {yol:34s} {len(s)//1024:4d} KB → {len(y)//1024:4d} KB   {hedef.name}")
    print(f"TOPLAM {toplam_e//1024} KB → {toplam_y//1024} KB")

if __name__ == "__main__":
    dk = None
    for a in sys.argv[1:]:
        if a.startswith("--dom="):
            dk = a.split("=", 1)[1]
    uygula(dk)
