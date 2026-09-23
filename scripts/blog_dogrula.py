#!/usr/bin/env python3
# scripts/blog_dogrula.py — blog yazilarindaki matematiksel iddialarin
# makine dogrulamasi (23.09.2026)
#
# Ahmet: "yazilar cok onemli, matematiksel hata yapmayalim; kaynakta
# matematiksel olarak dogrulayalim." Bu betik yazilardaki her tanim
# kumesi, goruntu kumesi, ters fonksiyon, bileske ve sayma sonucunu
# sympy ile SEMBOLIK ya da kaba kuvvetle (butun fonksiyonlari tek tek
# sayarak) yeniden hesaplar. Yazida bir sayi degisirse buradaki satir da
# degismeli; tutmazsa betik HATA verir, yayin yapilmaz.
#
# Ayrica her yazi icin bicim denetimi: >= 2000 kelime, 10 kontrol
# maddesi, uzun tire yok, formul disinda unlem yok, aciklama <= 160.
#
# Calistirma (sympy yalniz .venv'de):  .venv/bin/python scripts/blog_dogrula.py
import itertools, re, sys, pathlib
from fractions import Fraction as F

import sympy as sp
from sympy import S, Interval, Union, FiniteSet, oo, sqrt, log, Abs, Rational
from sympy.calculus.util import continuous_domain, function_range

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))

x, y, t, a, b, c, d, x1, x2 = sp.symbols("x y t a b c d x1 x2", real=True)
R = S.Reals
SAY = [0]


def esit(ad, bulunan, beklenen):
    SAY[0] += 1
    if isinstance(bulunan, sp.Basic) and isinstance(beklenen, sp.Basic) and not isinstance(bulunan, sp.Set):
        tamam = sp.simplify(bulunan - beklenen) == 0
    else:
        tamam = bulunan == beklenen
    if not tamam:
        raise AssertionError(f"TUTMADI: {ad}\n  bulunan : {bulunan}\n  beklenen: {beklenen}")


def tanim(ifade):
    return continuous_domain(ifade, x, R)


def goruntu(ifade, alan=R):
    return function_range(ifade, x, alan)


def aralik(*esitsizlikler):
    """Esitsizliklerin ortak cozum kumesi (her biri ayri cozulur, kesisim alinir)."""
    kume = R
    for e in esitsizlikler:
        kume = kume.intersect(sp.solveset(e, x, R))
    return kume


def fonksiyonlar(A, B):
    """A dan B ye butun fonksiyonlar (sozluk olarak)."""
    for secim in itertools.product(B, repeat=len(A)):
        yield dict(zip(A, secim))


def orten_sayisi(m, n):
    return sum(1 for f in fonksiyonlar(range(m), range(n)) if set(f.values()) == set(range(n)))


# ── 02 Tanim, deger ve goruntu kumeleri ─────────────────────────────────
def yazi_02():
    esit("02 x^2 goruntu {-1,0,1,2}", {v * v for v in (-1, 0, 1, 2)}, {0, 1, 4})
    esit("02 g=x^2 [0,3] goruntu", goruntu(x**2, Interval(0, 3)), Interval(0, 9))
    esit("02 f=x^2 R goruntu", goruntu(x**2), Interval(0, oo))
    esit("02 (2x+1)/(x^2-9)", tanim((2*x + 1) / (x**2 - 9)), R - FiniteSet(-3, 3))
    esit("02 sqrt(6-2x)+1/(x+1)", tanim(sqrt(6 - 2*x) + 1 / (x + 1)),
         Union(Interval.open(-oo, -1), Interval.Lopen(-1, 3)))
    esit("02 5/sqrt(x+4)", tanim(5 / sqrt(x + 4)), Interval.open(-4, oo))
    esit("02 sqrt(x^2-5x+6)", tanim(sqrt(x**2 - 5*x + 6)), Union(Interval(-oo, 2), Interval(3, oo)))
    esit("02 carpanlar", sp.factor(x**2 - 5*x + 6), (x - 2) * (x - 3))
    esit("02 x=2.5 carpim", F(1, 2) * F(-1, 2), F(-1, 4))
    esit("02 sqrt((x-1)/(x+3))", tanim(sqrt((x - 1) / (x + 3))),
         Union(Interval.open(-oo, -3), Interval(1, oo)))
    esit("02 log_{x-1}(5-x)", tanim(log(5 - x) / log(x - 1)),
         Union(Interval.open(1, 2), Interval.open(2, 5)))
    # sympy kup kokun tanim kumesini cikaramiyor (NotImplementedError); iki parca:
    # kup kok negatif sayida gercel (sart koymaz), sart yalniz icerideki 1/x ten.
    esit("02 kupkok negatifte gercel", sp.real_root(-8, 3), -2)
    esit("02 kupkok(1/x) sart 1/x ten", tanim(1 / x), R - FiniteSet(0))
    esit("02 sqrt(x^2)=|x|", sp.sqrt(x**2), Abs(x))
    # f(ax+b) kaydirmalari: parantez ici [1,7] -> x araligi
    esit("02 f(2x-1), Tf=[1,7]", aralik(2*x - 1 >= 1, 2*x - 1 <= 7), Interval(1, 4))
    esit("02 f(3-x) T=[0,5] -> Tf", goruntu(3 - x, Interval(0, 5)), Interval(-2, 3))
    k1 = aralik(x + 3 >= 0, x + 3 <= 5)
    k2 = aralik(1 - x >= 0, 1 - x <= 5)
    esit("02 f(x+3) parcasi", k1, Interval(-3, 2))
    esit("02 f(1-x) parcasi", k2, Interval(-4, 1))
    esit("02 kesisim", k1.intersect(k2), Interval(-3, 1))
    esit("02 f(x^2), Tf=[-2,6]", aralik(x**2 >= -2, x**2 <= 6), Interval(-sqrt(6), sqrt(6)))
    esit("02 x+1 {1,2,3}", {v + 1 for v in (1, 2, 3)}, {2, 3, 4})
    esit("02 x^2+1 {-2..2}", {v * v + 1 for v in range(-2, 3)}, {1, 2, 5})
    esit("02 3x-2 [-1,4]", goruntu(3*x - 2, Interval(-1, 4)), Interval(-5, 10))
    esit("02 5-2x [0,3)", goruntu(5 - 2*x, Interval.Ropen(0, 3)), Interval.Lopen(-1, 5))
    p = x**2 - 4*x + 7
    esit("02 tepe apsisi", -(-4) / sp.Integer(2), 2)
    esit("02 tepe degeri", p.subs(x, 2), 3)
    esit("02 tam kare", sp.expand((x - 2)**2 + 3), sp.expand(p))
    esit("02 parabol R", goruntu(p), Interval(3, oo))
    esit("02 parabol [0,5]", goruntu(p, Interval(0, 5)), Interval(3, 12))
    esit("02 parabol yalniz uclar yanlis", {p.subs(x, 0), p.subs(x, 5)}, {7, 12})
    esit("02 parabol [3,6]", goruntu(p, Interval(3, 6)), Interval(4, 19))
    q = (2*x + 1) / (x - 3)
    esit("02 kesirli goruntu", goruntu(q, R - FiniteSet(3)), R - FiniteSet(2))
    esit("02 y cozumu", sp.solve(sp.Eq(y, q), x), [(3*y + 1) / (y - 2)])
    esit("02 x=3 imkansiz", sp.solve(sp.Eq((3*y + 1) / (y - 2), 3), y), [])
    esit("02 y=2 -> 0=7", sp.expand(2 * (x - 3) - (2*x + 1)), -7)
    esit("02 ad-bc=0 sabit", sp.cancel((2*x + 4) / (x + 2)), 2)
    esit("02 kalip a/c", goruntu((5*x - 1) / (2*x + 3), R - FiniteSet(Rational(-3, 2))), R - FiniteSet(Rational(5, 2)))
    esit("02 sqrt(x-1)+2", goruntu(sqrt(x - 1) + 2, Interval(1, oo)), Interval(2, oo))
    esit("02 3-|x+2|", goruntu(3 - Abs(x + 2)), Interval(-oo, 3))
    esit("02 2^x+1", goruntu(2**x + 1), Interval.open(1, oo))
    esit("02 sqrt(9-x^2) T", tanim(sqrt(9 - x**2)), Interval(-3, 3))
    esit("02 sqrt(9-x^2) G", goruntu(sqrt(9 - x**2), Interval(-3, 3)), Interval(0, 3))
    ters = (3*x + 1) / (x - 2)
    esit("02 ters dogru", sp.simplify(q.subs(x, ters)), x)
    esit("02 tersin goruntusu", goruntu(ters, R - FiniteSet(2)), R - FiniteSet(3))
    esit("02 grafik birlesim", Union(Interval(1, 5), Interval.Lopen(-2, 5)), Interval.Lopen(-2, 5))
    A, B = [1, 2, 3], ["a", "b", "c", "d"]
    boy = {}
    for f in fonksiyonlar(A, B):
        boy[len(set(f.values()))] = boy.get(len(set(f.values())), 0) + 1
    esit("02 goruntu 1/2/3 elemanli", boy, {1: 4, 2: 36, 3: 24})
    esit("02 toplam 4^3", sum(boy.values()), 64)
    esit("02 binom(4,2)*6", sp.binomial(4, 2) * (2**3 - 2), 36)
    esit("02 f(1)=a", sum(1 for f in fonksiyonlar(A, B) if f[1] == "a"), 16)
    for m in range(1, 7):
        esit(f"02 2^m-2 (m={m})", orten_sayisi(m, 2), 2**m - 2)


# ── 03 Birebir ve orten ─────────────────────────────────────────────────
def yazi_03():
    q = lambda v: (2*v + 1) / (v - 3)
    fark = sp.factor(sp.together(q(x1) - q(x2)))
    esit("03 kesirli birebir: fark = -7(x1-x2)/..", sp.simplify(fark * (x1 - 3) * (x2 - 3) / (x1 - x2)), -7)
    esit("03 icler disler", sp.expand((2*x1 + 1)*(x2 - 3) - (2*x2 + 1)*(x1 - 3)), 7*x2 - 7*x1)
    h = lambda v: v**2 - 2*v
    esit("03 x^2-2x carpan", sp.factor(h(x1) - h(x2)), (x1 - x2) * (x1 + x2 - 2))
    esit("03 f(0)=f(2)=0", (h(0), h(2)), (0, 0))
    esit("03 x^2 y=4 kesisim", set(sp.solve(x**2 - 4, x)), {-2, 2})
    esit("03 |x| y=3", sp.solveset(Abs(x) - 3, x, R), FiniteSet(-3, 3))
    esit("03 1/x: f(-1)<f(1)", (F(1, -1), F(1, 1)), (F(-1), F(1)))
    esit("03 x^2+1 goruntu", goruntu(x**2 + 1), Interval(1, oo))
    esit("03 3x-5 orten", sp.simplify(3 * ((y + 5) / 3) - 5), y)
    esit("03 Z->Z 2x cozum 1.5", sp.solve(2*x - 3, x), [Rational(3, 2)])
    esit("03 Z->Z 2x tekler bos", any(2*n == k for n in range(-50, 51) for k in (-3, -1, 1, 3)), False)
    g = sp.Piecewise((3*x, x >= 0), (x, True))
    esit("03 2x+|x| parcali", sp.piecewise_fold(2*x + Abs(x)).rewrite(sp.Piecewise).equals(g) or
         all((2*v + abs(v)) == (3*v if v >= 0 else v) for v in range(-20, 21)), True)
    esit("03 2x+|x| goruntu", Union(goruntu(3*x, Interval(0, oo)), goruntu(x, Interval.open(-oo, 0))), R)
    esit("03 a=2", sp.expand(((a - 2)*x**2 + 3*x + 1).subs(a, 2)), 3*x + 1)
    esit("03 [2,oo) tepe", -(-4) / sp.Integer(2 * 1), 2)
    esit("03 k=-3", goruntu(x**2 - 4*x + 1, Interval(2, oo)), Interval(-3, oo))
    esit("03 orten 4->3 kaba kuvvet", orten_sayisi(4, 3), 36)
    esit("03 orten 4->3 formul", 3**4 - 3 * 2**4 + 3, 36)
    for m in range(1, 6):
        for n in range(1, 5):
            ie = sum((-1)**k * sp.binomial(n, k) * (n - k)**m for k in range(n + 1))
            esit(f"03 icerme-disarma m={m} n={n}", ie, orten_sayisi(m, n))
            birebir = sum(1 for f in fonksiyonlar(range(m), range(n)) if len(set(f.values())) == m)
            esit(f"03 birebir sayisi m={m} n={n}", birebir,
                 sp.factorial(n) / sp.factorial(n - m) if m <= n else 0)
    for n in range(1, 6):
        fs = list(fonksiyonlar(range(n), range(n)))
        bb = {i for i, f in enumerate(fs) if len(set(f.values())) == n}
        ot = {i for i, f in enumerate(fs) if set(f.values()) == set(range(n))}
        esit(f"03 esit sonlu: birebir=orten n={n}", bb, ot)
        esit(f"03 n! n={n}", len(bb), sp.factorial(n))
    esit("03 icine 3->3", 27 - 6, 21)
    # tablo: R -> R
    esit("03 x^3 goruntu", goruntu(x**3), R)
    # sympy 1.14 hatasi: function_range(2**x) bos kume donduruyor (2**x+1 dogru).
    # Esdegeri e^(x ln2) ile hesaplatilir.
    esit("03 2^x goruntu", goruntu(sp.exp(x * sp.log(2))), Interval.open(0, oo))
    esit("03 |x| goruntu", goruntu(Abs(x)), Interval(0, oo))
    esit("03 x^2 goruntu", goruntu(x**2), Interval(0, oo))
    esit("03 x^3 artan", sp.solveset(sp.diff(x**3, x) < 0, x, R), S.EmptySet)
    esit("03 log2 = 2^x tersi", sp.simplify(sp.log(2**x, 2)), x)


# ── 04 Bileske ──────────────────────────────────────────────────────────
def yazi_04():
    f = lambda v: v**2 + 1
    g = lambda v: 2*v - 3
    esit("04 (fog)(2)", f(g(2)), 2)
    esit("04 (gof)(2)", g(f(2)), 7)
    esit("04 (fof)(1)", f(f(1)), 5)
    esit("04 fog kural", sp.expand(f(g(x))), 4*x**2 - 12*x + 10)
    esit("04 gof kural", sp.expand(g(f(x))), 2*x**2 - 1)
    G = {1: 2, 2: 3, 3: 1}
    Fn = {1: 2, 2: 2, 3: 1}
    esit("04 tablo fog", {k: Fn[G[k]] for k in G}, {1: 2, 2: 1, 3: 2})
    esit("04 tablo gof", {k: G[Fn[k]] for k in Fn}, {1: 3, 2: 3, 3: 2})
    esit("04 sqrt(x-4)", tanim(sqrt(x - 4)), Interval(4, oo))
    esit("04 sqrt(x)-4", tanim(sqrt(x) - 4), Interval(0, oo))
    # 1/(1/x): ic fonksiyonun tanim kumesi de aranir
    ic = tanim(1 / x)
    esit("04 1/(1/x) tanim", ic.intersect(sp.imageset(sp.Lambda(x, 1 / x), ic)), R - FiniteSet(0))
    esit("04 x+2, x+5 degisme", sp.expand((x + 5) + 2 - ((x + 2) + 5)), 0)
    esit("04 g=2x^2-3", sp.solve(sp.Eq(2*y + 5, 4*x**2 - 1), y), [2*x**2 - 3])
    esit("04 g kontrol", sp.expand(2*(2*x**2 - 3) + 5), 4*x**2 - 1)
    for gg in (x + 1, -x - 1, Abs(x + 1)):
        esit(f"04 g^2=(x+1)^2 icin {gg}", sp.simplify(gg**2 - (x + 1)**2), 0)
    ff = sp.expand((4*x + 7).subs(x, (t - 1) / 2))
    esit("04 f(2x+1)=4x+7 -> f(t)", ff, 2*t + 5)
    esit("04 4x+7 = 2(2x+1)+5", sp.expand(2*(2*x + 1) + 5), 4*x + 7)
    esit("04 f(9)", (4*x + 7).subs(x, sp.solve(2*x + 1 - 9, x)[0]), 23)
    esit("04 f(9) dogrudan", 2*9 + 5, 23)
    esit("04 f(x+1)=x^2+3x", sp.expand((x**2 + 3*x).subs(x, t - 1)), t**2 + t - 2)
    esit("04 f(x+1) kontrol", sp.expand((x + 1)**2 + (x + 1) - 2), x**2 + 3*x)
    fp = lambda v: v + 1 if v < 2 else v * v
    gp = lambda v: 3 - v
    esit("04 parcali", (fp(gp(0)), gp(fp(1)), fp(fp(1))), (9, 1, 4))
    fd = lambda v: 1 / (1 - v)
    esit("04 dongu", (fd(F(2)), fd(F(-1)), fd(F(1, 2))), (F(-1), F(1, 2), F(2)))
    esit("04 fof", sp.simplify(fd(fd(x))), (x - 1) / x)
    esit("04 fofof", sp.simplify(fd(fd(fd(x)))), x)
    esit("04 2026 bolme", divmod(2026, 3), (675, 1))
    v = F(2)
    for _ in range(2026):
        v = fd(v)
    esit("04 2026 kez", v, F(-1))


# ── 05 Ters fonksiyon ───────────────────────────────────────────────────
def ters_mi(fx, gx, f_alan, g_alan):
    """g, f nin tersi mi? f nin tanim kumesinden her s icin g(f(s))=s ve
    g ninkinden her s icin f(g(s))=s. Sembolik tek esitlik YETMEZ: koklu
    ve ikinci dereceden fonksiyonda ters kural yalniz kisitli kumede
    gecerli (orn. g(f(x))=1+|x-1| ancak x>=1 icin x e esit)."""
    return (all(sp.simplify(gx.subs(x, fx.subs(x, s)) - s) == 0 for s in f_alan) and
            all(sp.simplify(fx.subs(x, gx.subs(x, s)) - s) == 0 for s in g_alan))


def yazi_05():
    esit("05 x^2: f(-3)=f(3)=9", ((-3)**2, 3**2), (9, 9))
    esit("05 sqrt tersi [0,oo)", ters_mi(x**2, sqrt(x), [0, 1, 4, Rational(9, 4), 7], [0, 1, 2, 4, Rational(9, 4)]), True)
    esit("05 4x-7 tersi", ters_mi(4*x - 7, (x + 7) / 4, [0, 2, -5, Rational(7, 3)], [0, 1, -5, Rational(7, 3)]), True)
    esit("05 4x-7 kontrol", ((4*2 - 7), F(1 + 7, 4)), (1, F(2)))
    esit("05 ax+b genel", sp.simplify((a*x + b).subs(x, (x - b) / a)), x)
    esit("05 (3x-2)/(x+4) tersi", ters_mi((3*x - 2) / (x + 4), (-4*x - 2) / (x - 3), [0, 1, 5, -3], [0, 1, 5, Rational(-1, 2)]), True)
    esit("05 f(0)", F(-2, 4), F(-1, 2))
    esit("05 f^-1(-1/2)", ((-4*x - 2) / (x - 3)).subs(x, Rational(-1, 2)), 0)
    fg = (a*x + b) / (c*x + d)
    tg = (-d*x + b) / (c*x - a)
    esit("05 kesirli kalip genel", sp.simplify(fg.subs(x, tg) - x), 0)
    esit("05 kendi tersi (x+4)/(2x-1)", sp.simplify(((x + 4) / (2*x - 1)).subs(x, (x + 4) / (2*x - 1))), x)
    esit("05 a+d=0 genel", sp.simplify(tg.subs(d, -a) - fg.subs(d, -a)), 0)
    f1 = sqrt(x - 2) + 1
    esit("05 sqrt(x-2)+1 goruntu", goruntu(f1, Interval(2, oo)), Interval(1, oo))
    esit("05 sqrt tersi", ters_mi(f1, (x - 1)**2 + 2, [2, 3, 6, 11, Rational(9, 4)], [1, 2, 3, Rational(5, 2)]), True)
    esit("05 f(6), f^-1(3)", (f1.subs(x, 6), ((x - 1)**2 + 2).subs(x, 3)), (3, 6))
    # yazidaki uyari: kisit disinda kural ters DEGIL: g(0)=3, f(3)=2 (0 degil)
    esit("05 f(g(0)) kisit disi", f1.subs(x, ((x - 1)**2 + 2).subs(x, 0)), 2)
    esit("05 (x-1)^2+2 R de birebir degil", ((x - 1)**2 + 2).subs(x, 0) == ((x - 1)**2 + 2).subs(x, 2), True)
    p = x**2 - 2*x - 2
    esit("05 tam kare", sp.expand((x - 1)**2 - 3), p)
    esit("05 [1,oo) goruntu", goruntu(p, Interval(1, oo)), Interval(-3, oo))
    esit("05 parabol tersi", ters_mi(p, 1 + sqrt(x + 3), [1, 3, 4, Rational(5, 2)], [-3, 1, 6, Rational(-11, 4)]), True)
    esit("05 f(3), f^-1(1)", (p.subs(x, 3), (1 + sqrt(x + 3)).subs(x, 1)), (1, 3))
    e = 2**(x - 1) + 3
    esit("05 ussel goruntu", goruntu(e), Interval.open(3, oo))
    esit("05 ussel tersi", ters_mi(e, sp.log(x - 3, 2) + 1, [0, 1, 3, -2], [4, 7, 11, Rational(7, 2)]), True)
    esit("05 f(3), f^-1(7)", (e.subs(x, 3), sp.simplify((sp.log(x - 3, 2) + 1).subs(x, 7))), (7, 3))
    k = x**3 + 2*x + 1
    esit("05 kubik artan", sp.solveset(sp.diff(k, x) <= 0, x, R), S.EmptySet)
    esit("05 kubik orten", goruntu(k), R)
    esit("05 f^-1(4)", sp.solveset(k - 4, x, R), FiniteSet(1))
    esit("05 (f o g)^-1 birinci yol", sp.expand((2*x + 1).subs(x, x - 3)), 2*x - 5)
    esit("05 2x-5 tersi", ters_mi(2*x - 5, (x + 5) / 2, [0, 1, 7], [0, 1, 7]), True)
    esit("05 g^-1(f^-1(x))", sp.simplify(((x - 1) / 2) + 3), (x + 5) / 2)
    esit("05 g=f^-1(4x+1)", sp.expand(((x + 3) / 2).subs(x, 4*x + 1)), 2*x + 2)
    esit("05 g kontrol", sp.expand(2*(2*x + 2) - 3), 4*x + 1)
    esit("05 2x-3 kesisim", sp.solve(2*x - 3 - x, x), [3])
    esit("05 2x-3 tersi 3 te", ((x + 3) / 2).subs(x, 3), 3)
    ku = lambda v: -sp.real_root(v, 3)
    esit("05 -x^3 tersi", all(sp.simplify(ku(-(s**3)) - s) == 0 for s in (-2, -1, 0, 1, 3)), True)
    esit("05 (1,-1) ikisinde", (-(1**3), ku(1)), (-1, -1))
    # artan fonksiyonda f ile f^-1 kesisimi y=x uzerinde: ornek tarama
    for fx, gx in ((2*x - 3, (x + 3) / 2), (x**3, sp.real_root(x, 3))):
        kes = sp.solveset(fx - gx, x, R)
        esit(f"05 artan kesisim y=x ({fx})", all(sp.simplify(fx.subs(x, r) - r) == 0 for r in kes), True)


# ── 03/04/05 ek bolumler (ikinci tur) ────────────────────────────────────
def ekler():
    p3 = x**2 - 4*x + 3
    esit("03 tepe (2,-1)", (-(-4) / sp.Integer(2), p3.subs(x, 2)), (2, -1))
    esit("03 y=3 kesisim", sp.solveset(p3 - 3, x, R), FiniteSet(0, 4))
    esit("03 y=-2 kesmez", sp.solveset(p3 + 2, x, R), S.EmptySet)
    esit("03 [2,oo) goruntu", goruntu(p3, Interval(2, oo)), Interval(-1, oo))
    esit("03 [2,oo) artan", sp.solveset(sp.diff(p3, x) <= 0, x, Interval.open(2, oo)), S.EmptySet)
    esit("03 parcali 1. goruntu", goruntu(x + 1, Interval.open(-oo, 0)), Interval.open(-oo, 1))
    esit("03 parcali 2. goruntu", goruntu(x**2, Interval(0, oo)), Interval(0, oo))
    esit("03 parcali birlesim", Union(Interval.open(-oo, 1), Interval(0, oo)), R)
    esit("03 parcali cakisma", Interval.open(-oo, 1).intersect(Interval(0, oo)), Interval.Ropen(0, 1))
    esit("03 f(-0.5)=f(sqrt0.5)", (Rational(-1, 2) + 1, sqrt(Rational(1, 2))**2), (Rational(1, 2), Rational(1, 2)))
    esit("04 1/(x^2-1) tanim", tanim(1 / (x**2 - 1)), R - FiniteSet(-1, 1))
    esit("04 sqrt(3x+1) ayrim", sqrt(x).subs(x, 3*x + 1), sqrt(3*x + 1))
    esit("04 (x^2+1)^3 ayrim 1", (x**3).subs(x, x**2 + 1), (x**2 + 1)**3)
    esit("04 (x^2+1)^3 ayrim 2", ((x + 1)**3).subs(x, x**2), (x**2 + 1)**3)
    f = lambda v: 2*v + 1
    g = lambda v: v**2
    esit("04 fog=gof kokler", sp.solveset(f(g(x)) - g(f(x)), x, R), FiniteSet(0, -2))
    esit("04 x=-2 kontrol", (f(g(-2)), g(f(-2))), (9, 9))
    esit("04 fofof x+3", ((x + 3).subs(x, x + 3)).subs(x, x + 3), x + 9)
    esit("04 x+9=20", sp.solve(x + 9 - 20, x), [11])
    esit("04 sss carpim", sp.expand((x + 1) * (2*x)), 2*x**2 + 2*x)
    esit("04 sss bileske", (x + 1).subs(x, 2*x), 2*x + 1)
    q = (3*x - 2) / (x + 4)
    qt = (-4*x - 2) / (x - 3)
    esit("05 f tanim", tanim(q), R - FiniteSet(-4))
    esit("05 f goruntu", goruntu(q, R - FiniteSet(-4)), R - FiniteSet(3))
    esit("05 f^-1 tanim", tanim(qt), R - FiniteSet(3))
    esit("05 f^-1 goruntu", goruntu(qt, R - FiniteSet(3)), R - FiniteSet(-4))
    esit("05 f^-1=(x+1)/3 -> f", ters_mi(3*x - 1, (x + 1) / 3, [0, 5, -2], [0, 14, 2]), True)
    esit("05 f(5)", sp.solve((y + 1) / 3 - 5, y), [14])
    fb = sp.expand((3*x + 2).subs(x, (t + 1) / 2))
    esit("05 f(2x-1)=3x+2 -> f(3)", fb.subs(t, 3), 8)
    esit("05 3x+2=8", sp.solve(3*x + 2 - 8, x), [2])
    esit("05 f^-1(9), f=2x+3", sp.solve(2*y + 3 - 9, y), [3])
    for kf in (-x, 5 - x, 1 / x):
        esit(f"05 kendi tersi {kf}", sp.simplify(kf.subs(x, kf)), x)
    k3 = 3 - sqrt(x + 1)
    esit("05 3-sqrt(x+1) goruntu", goruntu(k3, Interval(-1, oo)), Interval(-oo, 3))
    esit("05 3-sqrt(x+1) tersi", ters_mi(k3, (3 - x)**2 - 1, [-1, 0, 3, 8], [3, 0, -1, Rational(5, 2)]), True)
    esit("05 f(8), f^-1(0)", (k3.subs(x, 8), ((3 - x)**2 - 1).subs(x, 0)), (0, 8))
    esit("05 artan f -> artan f^-1", sp.diff((x + 3) / 2, x) > 0, True)

# ── bicim denetimi ─────────────────────────────────────────────────────
def bicim():
    import blog_veri
    from blog_uygula import kelime_sayisi
    for Y in blog_veri.YAZILAR:
        no = Y["slug"]
        metin = " ".join([Y["ozet"], Y["aciklama"], Y["baslik"]] + [b["baslik"] for b in Y["bolumler"]]
                         + [p for b in Y["bolumler"] for p in b["icerik"]]
                         + [s + " " + c for s, c in Y.get("sss", [])] + list(Y.get("kontrol", [])))
        esit(f"{no} uzun tire yok", "—" in metin, False)
        esit(f"{no} formul disinda unlem yok", "!" in re.sub(r"\$[^$]*\$", "", metin), False)
        esit(f"{no} $ dengeli", metin.count("$") % 2, 0)
        esit(f"{no} aciklama <= 160", len(Y["aciklama"]) <= 160, True)
        esit(f"{no} kontrol 10", len(Y["kontrol"]), 10)
        esit(f"{no} >= 2000 kelime", kelime_sayisi(Y) >= 2000, True)
        print(f"  {no:34s} {kelime_sayisi(Y):5d} kelime · {len(Y['bolumler']):2d} bolum · "
              f"{metin.count('bs-hap-ic'):2d} hap · aciklama {len(Y['aciklama'])}")


if __name__ == "__main__":
    for fn in (yazi_02, yazi_03, yazi_04, yazi_05, ekler):
        once = SAY[0]
        fn()
        print(f"{fn.__name__}: {SAY[0] - once} iddia dogrulandi")
    bicim()
    print(f"\nTOPLAM {SAY[0]} denetim, hepsi tuttu.")
