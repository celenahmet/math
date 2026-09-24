# scripts/ek_denetimi.py — formul sonrasi Turkce ek denetimi (24.09.2026)
#
# Yazilarda formulden sonra gelen ek ayri yazilir: "$x$ in", "$\\dfrac{2}{5}$ i".
# Ek, formulun OKUNUSUNUN son kelimesine uymali (unlu uyumu, unsuz benzesmesi,
# kaynastirma harfi). Kesir "paydada pay" okunur ("besde iki"): son kelime
# PAYIN okunusudur. 24.09 taramasinda 51-70 arasinda 80'den fazla yanlis ek
# bulundu ("$\\dfrac{2}{5}$ in" yerine "nin", "$\\dfrac{1}{4}$ u" yerine "i").
#
# Bilincli olarak DENETLENMEYENLER (yanlis alarm):
#   "de/da" -- baglac da olabilir ("$f(x)$ de ... gibi gorunur")
#   "ya"    -- "ya da" baglaci
#   "su"    -- "su bardagi" gibi ad
#   q, f    -- harf okunusu tartismali (ku/ku, fe/f)
#   "inci"  -- "n'inci" yerlesik yazimi
# blog_dogrula.py bicim() icinden cagrilir; tutmazsa yayin yapilmaz.
import re


BIRLER = ["sıfır", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
ONLAR = {1: "on", 2: "yirmi", 3: "otuz", 4: "kırk", 5: "elli", 6: "altmış", 7: "yetmiş", 8: "seksen", 9: "doksan"}
HARF = {"a": "a", "b": "be", "c": "ce", "d": "de", "e": "e", "f": "fe", "g": "ge", "h": "he", "k": "ka", "m": "me",
        "n": "ne", "p": "pe", "q": "kü", "r": "re", "s": "se", "t": "te", "x": "iks", "y": "ye", "z": "ze",
        "A": "a", "B": "be", "C": "ce", "D": "de", "P": "pe", "Q": "kü", "R": "re", "S": "se", "I": "ı"}

def sayi_son(n):
    n = abs(int(n))
    if n == 0: return "sıfır"
    if n % 10: return BIRLER[n % 10]
    if n % 100: return ONLAR[(n % 100) // 10]
    if n % 1000: return "yüz"
    if n % 10**6: return "bin"
    if n % 10**9: return "milyon"
    return "milyar"

def son_kelime(ifade):
    s = ifade.strip()
    s = re.sub(r"\\(left|right)", "", s)
    s = s.rstrip(" ")
    # sondaki kapanis isaretleri
    while s and s[-1] in ")]|":
        s = s[:-1].rstrip()
    if s.endswith("\\}"): s = s[:-2]
    if s.endswith("\\ldots") or s.endswith("\\cdots"): return None
    # sondaki faktoriyel: 5! "bes faktoriyel" okunur (25.09: "$5!$ ten" yakalanamiyordu)
    if s.endswith("!"): return "faktöriyel"
    # sondaki us: ^2 kare, ^3 kup, ^{...} ya da ^n
    m = re.search(r"\^(\{([^{}]*)\}|(\w))$", s)
    if m:
        us = m.group(2) if m.group(2) is not None else m.group(3)
        taban = s[:m.start()]
        if us in ("2",) and not re.search(r"\d$", taban.rstrip(")")): return "kare"
        if us in ("3",) and not re.search(r"\d$", taban.rstrip(")")): return "küp"
        return son_kelime(us)
    # sondaki kesir: \dfrac{p}{q} -> pay
    m = re.search(r"\\d?frac\{((?:[^{}]|\{[^{}]*\})*)\}\{((?:[^{}]|\{[^{}]*\})*)\}$", s)
    if m:
        return son_kelime(m.group(1))
    if s.endswith("}"):
        # \sqrt{...} ya da \text{...}
        m = re.search(r"\\sqrt(\[\d\])?\{((?:[^{}]|\{[^{}]*\})*)\}$", s)
        if m: return son_kelime(m.group(2))
        m = re.search(r"\\text\{([^{}]*)\}$", s)
        if m: return m.group(1).split()[-1].lower() if m.group(1).split() else None
        return None
    if s.endswith("\\pi"): return "pi"
    if s.endswith("\\infty"): return "sonsuz"
    m = re.search(r"(\d+)\.(\d+)$", s)
    if m: return sayi_son(m.group(2))
    m = re.search(r"(\d+)$", s)
    if m: return sayi_son(m.group(1))
    m = re.search(r"([A-Za-z])$", s)
    if m and not re.search(r"\\[A-Za-z]+$", s): return HARF.get(m.group(1))
    return None

UNLU = "aıoueiöü"
def son_unlu(k):
    for ch in reversed(k):
        if ch in UNLU: return ch
    return None

def h4(v): return {"a": "ı", "ı": "ı", "o": "u", "u": "u", "e": "i", "i": "i", "ö": "ü", "ü": "ü"}[v]
def h2(v): return "a" if v in "aıou" else "e"
SERT = set("çfhkpsşt")

def beklenen(kelime, ek):
    v = son_unlu(kelime); son = kelime[-1]; unlu_son = son in UNLU; sert = son in SERT
    H4, H2 = h4(v), h2(v)
    d = "t" if sert else "d"
    adaylar = {
        "gen": ("n" if unlu_son else "") + H4 + "n",
        "belirtme": (("y" if unlu_son else "") + H4, ("s" if unlu_son else "") + H4),
        "yonelme": ("y" if unlu_son else "") + H2,
        "bulunma": d + H2,
        "ayrilma": d + H2 + "n",
        "ek_eylem": d + H4 + "r",
        "lik": "l" + H4 + "k",
        "sira": ("n" if unlu_son else H4 + "n") + {"ı": "cı", "i": "ci", "u": "cu", "ü": "cü"}[H4],
        "iyelik_belirtme": (("s" if unlu_son else "") + H4 + "n" + H4,),
        "iyelik_gen": (("s" if unlu_son else "") + H4 + "n" + H4 + "n",),
        "iyelik_yonelme": (("s" if unlu_son else "") + H4 + "n" + H2,),
        "iyelik_bulunma": (("s" if unlu_son else "") + H4 + "nd" + H2,),
        "iyelik_ayrilma": (("s" if unlu_son else "") + H4 + "nd" + H2 + "n",),
        "iyelik_ek_eylem": (("s" if unlu_son else "") + H4 + "d" + H4 + "r",),
    }
    return adaylar

def sinif(ek):
    if re.fullmatch(r"n?[ıiuü]n", ek): return "gen"
    if re.fullmatch(r"[ys]?[ıiuü]", ek): return "belirtme"
    if re.fullmatch(r"y?[ae]", ek): return "yonelme"
    if re.fullmatch(r"[dt][ae]", ek): return "bulunma"
    if re.fullmatch(r"[dt][ae]n", ek): return "ayrilma"
    if re.fullmatch(r"[dt][ıiuü]r", ek): return "ek_eylem"
    if re.fullmatch(r"l[ıiuü]k", ek): return "lik"
    if re.fullmatch(r"(n|[ıiuü]n)c[ıiuü]", ek): return "sira"
    if re.fullmatch(r"s?[ıiuü]n[ıiuü]", ek): return "iyelik_belirtme"
    if re.fullmatch(r"s?[ıiuü]n[ıiuü]n", ek): return "iyelik_gen"
    if re.fullmatch(r"s?[ıiuü]n[ae]", ek): return "iyelik_yonelme"
    if re.fullmatch(r"s?[ıiuü]nd[ae]", ek): return "iyelik_bulunma"
    if re.fullmatch(r"s?[ıiuü]nd[ae]n", ek): return "iyelik_ayrilma"
    if re.fullmatch(r"s?[ıiuü]d[ıiuü]r", ek): return "iyelik_ek_eylem"
    return None

def denetle(metin):
    sorunlar = []
    for m in re.finditer(r"(?<!\$)\$([^$]+)\$ ([a-zçğıöşü]+)(?=[\s.,;:!?\"')<]|$)", metin):
        ifade, ek = m.group(1), m.group(2)
        sonrasi = metin[m.end():m.end()+4]
        if ek == "ya" and sonrasi.startswith(" da"): continue
        if ek in ("inci",) : continue
        if re.search(r"(^|[^\\a-zA-Z])[qf]$", ifade.strip().rstrip(")")) or ifade.strip() in ("q", "f"): continue
        s = sinif(ek)
        if not s: continue
        if ek in ("de", "da", "su"):
            continue
        k = son_kelime(ifade)
        if not k: continue
        ad = beklenen(k, ek)[s]
        kabul = ad if isinstance(ad, tuple) else (ad,)
        if ek not in kabul:
            sorunlar.append((ifade, ek, k, "/".join(kabul)))
    return sorunlar
