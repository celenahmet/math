#!/usr/bin/env python3
# scripts/matematik.py — LaTeX alt kumesi → MathML (23.09.2026)
#
# NEDEN KENDI DONUSTURUCU: blog yazilari matematik konu anlatimi olacak,
# yani her sayfada onlarca formul var. Secenekler:
#   · KaTeX/MathJax → sayfaya ~100-300 KB JS+CSS+font iner. Performans
#     turunda ana sayfayi 1889 KB'den 602 KB'ye indirdik; bunu geri vermeyiz.
#   · Elle MathML yazmak → cok ayrintili, yazi yazmayi imkansiz kilar.
#   · latex2mathml paketi → `pip install` PEP 668 yuzunden kapali, ayrica
#     uretim makinesine bagimlilik ekler.
# Cozum: ihtiyac duydugumuz LaTeX alt kumesini burada cevirip MathML
# BASIYORUZ. MathML'i tarayici yerel olarak dizer: ek istek YOK.
#
# KAPSAM (sinav matematigi icin yeterli): ^ _ \frac \sqrt \sqrt[n]
# \lim \sum \prod \int \log \ln \sin \cos \tan \cot \text \left \right
# \circ \dfrac \mathbb{R}
# Yunan harfleri, karsilastirma ve islem isaretleri, |mutlak deger|.
# Kapsam disi bir komut gelirse SESSIZCE GECILMEZ — hata firlatilir ki
# yaziya bozuk formul girmesin.
#
# Kullanim: mm(r"\frac{a^2-b^2}{a-b}")  → <math>…</math>
#           satir(metin)  → metindeki $…$ ve $$…$$ parcalarini cevirir
import re

YUNAN = {
    "alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ε",
    "theta": "θ", "lambda": "λ", "mu": "μ", "pi": "π", "sigma": "σ",
    "phi": "φ", "omega": "ω", "Delta": "Δ", "Sigma": "Σ", "Omega": "Ω",
}
ISARET = {
    "times": "×", "cdot": "·", "div": "÷", "pm": "±", "mp": "∓",
    "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "ne": "≠", "neq": "≠",
    "approx": "≈", "equiv": "≡", "to": "→", "Rightarrow": "⇒",
    "Leftrightarrow": "⇔", "in": "∈", "notin": "∉", "subset": "⊂",
    "cup": "∪", "cap": "∩", "emptyset": "∅", "infty": "∞",
    "forall": "∀", "exists": "∃", "angle": "∠", "triangle": "△",
    "perp": "⊥", "parallel": "∥", "degree": "°", "ldots": "…", "cdots": "⋯",
    "circ": "∘", "subseteq": "⊆", "supseteq": "⊇", "Leftarrow": "⇐",
    "leftrightarrow": "↔", "mapsto": "↦", "setminus": "\\", "prime": "′",
}
# Cift cizgili kume simgeleri: \mathbb{R} gibi yazilir ama tek bir harf gibi
# davranir; grup ayristirmasina girmeden dogrudan karsiligi basilir.
KUMELER = {"R": "ℝ", "N": "ℕ", "Z": "ℤ", "Q": "ℚ", "C": "ℂ"}
FONKSIYON = ["sin", "cos", "tan", "cot", "sec", "csc", "log", "ln",
             "arcsin", "arccos", "arctan", "max", "min", "ebob", "ekok"]
BUYUK = {"sum": "∑", "prod": "∏", "int": "∫", "lim": "lim"}

# Sayi jetonu: ondalik ayirac KAYNAKTA NOKTA ile yazilir (2.5), ekrana
# virgulle basilir (2,5). Virgul HER ZAMAN ayractir. Eskiden [.,] ikisi de
# ondalik sayiliyordu: {1,2,3} icindeki "1,2" ve [2,5) araligi tek bir
# ondalik sayi (<mn>2,5</mn>) olarak basiliyordu (23.09 olculdu).
_JETON = re.compile(r"""
    \\text\{[^{}]*\} |
    \\[A-Za-z]+ | \\[{}|,\ ] | \d+(?:\.\d+)? | [A-Za-z] |
    \^ | _ | \{ | \} | \( | \) | \[ | \] | \| |
    [+\-=<>/!,.:;'] | \s+
""", re.X)


def _jetonla(s):
    i, out = 0, []
    while i < len(s):
        m = _JETON.match(s, i)
        if not m:
            raise ValueError(f"matematik: cozulemeyen karakter {s[i]!r} → {s!r}")
        j = m.group(0)
        i = m.end()
        if j.strip():
            out.append(j)
    return out


def _atom(j, jetonlar, k):
    """Tek bir atomu MathML'e cevirir; (mathml, sonraki_indis) doner."""
    if j == "{":
        parca, k = _dizi(jetonlar, k, "}")
        return ("<mrow>" + parca + "</mrow>", k)
    if j.startswith("\\text{"):
        # Jetonlayici \text{...} parcasini BUTUN olarak veriyor; harf harf
        # ayrilirsa MathML her harfi ayri <mi> yapip aralarini aciyor.
        # Bas/son bosluk HTML'de yutulur; bolunmez bosluga cevrilir
        # (yoksa "2^{x+1} olsun" bitisik cikiyor).
        ic = _kacir(j[6:-1]).replace(" ", "\u00a0")
        return (f"<mtext>{ic}</mtext>", k)
    if j.startswith("\\"):
        ad = j[1:]
        if ad == "mathbb":
            if k < len(jetonlar) and jetonlar[k] == "{":
                harf = jetonlar[k + 1] if k + 1 < len(jetonlar) else ""
                if harf in KUMELER and k + 2 < len(jetonlar) and jetonlar[k + 2] == "}":
                    return (f"<mi>{KUMELER[harf]}</mi>", k + 3)
            raise ValueError("matematik: \\mathbb yalnizca R N Z Q C alir")
        if ad == "binom":
            # Kombinasyon: cizgisiz kesir + esneyen parantez
            a, k = _grup(jetonlar, k)
            b, k = _grup(jetonlar, k)
            return ('<mrow><mo stretchy="true">(</mo>'
                    f'<mfrac linethickness="0">{a}{b}</mfrac>'
                    '<mo stretchy="true">)</mo></mrow>', k)
        if ad in ("frac", "dfrac", "tfrac"):
            a, k = _grup(jetonlar, k)
            b, k = _grup(jetonlar, k)
            return (f"<mfrac>{a}{b}</mfrac>", k)
        if ad == "sqrt":
            if k < len(jetonlar) and jetonlar[k] == "[":
                derece, k = _dizi(jetonlar, k + 1, "]")
                a, k = _grup(jetonlar, k)
                return (f"<mroot>{a}<mrow>{derece}</mrow></mroot>", k)
            a, k = _grup(jetonlar, k)
            return (f"<msqrt>{a}</msqrt>", k)
        if ad in ("left", "right"):
            if k < len(jetonlar):
                p = jetonlar[k]
                if p == "\\|":
                    p = "|"
                return (f'<mo stretchy="true">{_kacir(p)}</mo>', k + 1)
            return ("", k)
        if ad in BUYUK:
            return (f'<mo movablelimits="false">{BUYUK[ad]}</mo>', k)
        if ad in FONKSIYON:
            return (f"<mi>{ad}</mi>", k)
        if ad in YUNAN:
            return (f"<mi>{YUNAN[ad]}</mi>", k)
        if ad in ISARET:
            return (f"<mo>{ISARET[ad]}</mo>", k)
        if j == "\\ ":
            return ('<mspace width="0.3em"/>', k)
        if j in ("\\{", "\\}"):
            return (f"<mo>{j[1]}</mo>", k)
        if j == "\\,":
            return ('<mspace width="0.17em"/>', k)
        raise ValueError(f"matematik: bilinmeyen komut \\{ad}")
    if j[0].isdigit():
        return (f"<mn>{j.replace('.', ',')}</mn>", k)
    if j.isalpha():
        return (f"<mi>{j}</mi>", k)
    if j == "-":
        return ("<mo>\u2212</mo>", k)          # tire degil GERCEK eksi
    if j in "()[]":
        # Sade parantez icerige gore BUYUMESIN; yalniz \left( \right) esner.
        return (f'<mo stretchy="false">{j}</mo>', k)
    return (f"<mo>{_kacir(j)}</mo>", k)


def _kacir(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _grup(jetonlar, k):
    if k >= len(jetonlar):
        raise ValueError("matematik: eksik grup")
    if jetonlar[k] == "{":
        ic, k = _dizi(jetonlar, k + 1, "}")
        return ("<mrow>" + ic + "</mrow>", k)
    parca, k = _atom(jetonlar[k], jetonlar, k + 1)
    return (parca, k)


def _duzmetin(jetonlar, k):
    """\\text{...} icindeki jetonlari duz metin olarak birlestirir."""
    if k >= len(jetonlar) or jetonlar[k] != "{":
        raise ValueError("matematik: \\text{...} bekleniyordu")
    k += 1
    parcalar = []
    derinlik = 1
    while k < len(jetonlar):
        j = jetonlar[k]
        if j == "{":
            derinlik += 1
        elif j == "}":
            derinlik -= 1
            if derinlik == 0:
                return (_kacir(" ".join(parcalar)), k + 1)
        parcalar.append(j)
        k += 1
    raise ValueError("matematik: \\text{...} kapanmadi")


_KAPAYAN = {")", "]", "}", "|", "\u2032", "!"}


def _acan_isaret(mathml):
    """Onceki parca bir isaret mi ve ardindan gelen eksi, isaret eksisi mi?
    Kapayan ayrac ya da sayi/harf sonrasi eksi cikarmadir."""
    m = re.fullmatch(r"<mo[^>]*>(.*?)</mo>", mathml)
    return bool(m) and m.group(1) not in _KAPAYAN


def _dizi(jetonlar, k, bitis=None):
    out = []
    while k < len(jetonlar):
        j = jetonlar[k]
        if bitis and j == bitis:
            return ("".join(out), k + 1)
        if j in ("^", "_"):
            if not out:
                raise ValueError("matematik: ^ ya da _ once bir atom ister")
            taban = out.pop()
            ust, k2 = _grup(jetonlar, k + 1)
            # alt ve ust birlikte mi?
            if k2 < len(jetonlar) and jetonlar[k2] in ("^", "_") and jetonlar[k2] != j:
                digeri, k2 = _grup(jetonlar, k2 + 1)
                alt, ustu = (ust, digeri) if j == "_" else (digeri, ust)
                etiket = "munderover" if 'movablelimits="false"' in taban else "msubsup"
                out.append(f"<{etiket}>{taban}{alt}{ustu}</{etiket}>")
            else:
                if 'movablelimits="false"' in taban:
                    etiket = "munder" if j == "_" else "mover"
                else:
                    etiket = "msub" if j == "_" else "msup"
                out.append(f"<{etiket}>{taban}{ust}</{etiket}>")
            k = k2
            continue
        parca, k = _atom(j, jetonlar, k + 1)
        if j == "-" and (not out or _acan_isaret(out[-1])):
            # Isaret eksisi: "{-1", "f(-1)", "=-3", "^{-1}". Varsayilan <mo>
            # ikili islem boslugu alip "{ − 1" gibi basiliyordu (23.09 olculdu);
            # prefix bicimi bosluksuz dizer.
            parca = '<mo form="prefix">\u2212</mo>'
        out.append(parca)
    if bitis:
        raise ValueError(f"matematik: {bitis} kapanmadi")
    return ("".join(out), k)


def mm(latex, blok=False):
    """LaTeX alt kumesini MathML'e cevirir."""
    govde, _ = _dizi(_jetonla(latex), 0)
    d = ' display="block"' if blok else ""
    etiket = latex.replace('"', "'")
    return (f'<math xmlns="http://www.w3.org/1998/Math/MathML"{d} '
            f'class="mtml"><mrow>{govde}</mrow></math>')


_SATIR = re.compile(r"\$\$(.+?)\$\$|\$(.+?)\$", re.S)


def satir(metin):
    """Metindeki $...$ (satir ici) ve $$...$$ (blok) formullerini cevirir."""
    def d(m):
        if m.group(1) is not None:
            return '<div class="mtml-blok">' + mm(m.group(1).strip(), blok=True) + "</div>"
        return mm(m.group(2).strip())
    return _SATIR.sub(d, metin)


if __name__ == "__main__":
    ornekler = [
        r"a^2+b^2=c^2",
        r"\frac{a^2-b^2}{a-b}=a+b",
        r"\sqrt[3]{27}=3",
        r"\lim_{x \to 0} \frac{\sin x}{x} = 1",
        r"\sum_{i=1}^{n} i = \frac{n(n+1)}{2}",
        r"x_{1,2} = \frac{-b \pm \sqrt{b^2-4ac}}{2a}",
        r"\log_a b \cdot \log_b c = \log_a c",
        r"\left| x-3 \right| \le 5",
        r"\int_0^1 x^2 \, dx = \frac{1}{3}",
        r"f(x) = 2^{x+1} \text{ olsun}",
    ]
    for o in ornekler:
        c = mm(o)
        assert c.startswith("<math") and c.endswith("</math>"), o
        print(f"OK  {o[:46]:48s} {len(c):4d} bayt")
    print(f"\n{len(ornekler)} ornek cevrildi, hata yok.")
