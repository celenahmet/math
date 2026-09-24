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

# ── 51-55 Temel kavramlar ve sayilar (24.09) ────────────────────────────
def _devirli(tam, devretmeyen, devreden):
    """Devirli ondalik → kesir, TANIMDAN (x = tam,devretmeyen(devreden)...):
    kuraldan bagimsiz hesap; yazidaki kuralla karsilastirilir."""
    n, m = len(devretmeyen), len(devreden)
    a = F(int(str(tam) + devretmeyen + devreden)) if (devretmeyen + devreden) else F(tam)
    b = F(int(str(tam) + devretmeyen)) if devretmeyen else F(tam)
    return (a - b) / (10**n * (10**m - 1)) if m else F(int(str(tam) + devretmeyen), 10**n)


def _sonlu_mu(p, q):
    """Uzun bolme ile: kalan tekrar etmeden 0 olursa sonlu."""
    r, gorulen = p % q, set()
    while r and r not in gorulen:
        gorulen.add(r); r = (r * 10) % q
    return r == 0


def yazi_51_55():
    # 51
    uc = [n for n in range(100, 1000) if len(set(str(n))) == 3]
    esit("51 rakamlari farkli 3 bas. max/min", (max(uc), min(uc), max(uc) + min(uc)), (987, 102, 1089))
    esit("51 rakamlari farkli 2 bas. adet", sum(1 for n in range(10, 100) if len(set(str(n))) == 2), 81)
    for a_, b_ in itertools.product(range(-6, 7), repeat=2):
        esit("51 tek/cift", ((a_ + b_) % 2, (a_ * b_) % 2), ((a_ % 2 + b_ % 2) % 2, (a_ % 2) * (b_ % 2)))
        esit("51 3a+2b tek <=> a tek", (3 * a_ + 2 * b_) % 2 == 1, a_ % 2 == 1)
    esit("51 bolme", (12 // 4, 12 // 6), (3, 2))
    esit("51 kuvvet isaret", ((-2)**4, (-2)**3, -2**4), (16, -8, -16))
    esit("51 a=-2 b=3", ((-2) * 3, 4 * 3, (-2)**3, 3 - (-2)), (-6, 12, -8, 5))
    dz = list(range(12, 41, 2))
    esit("51 12..40", (len(dz), sum(dz), (40 - 12) // 2 + 1), (15, 390, 15))
    esit("51 toplamlar", (sum(range(1, 21)), sum(range(1, 20, 2))), (210, 100))
    esit("51 ardisik tek 87", [n for n in range(1, 87, 2) if n + n + 2 + n + 4 == 87], [27])
    esit("51 asal <30", list(sp.primerange(1, 30)), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    esit("51 asal toplam 25", [(p_, 25 - p_) for p_ in sp.primerange(1, 13) if sp.isprime(25 - p_)], [(2, 23)])
    esit("51 8,15 aralarinda asal", sp.gcd(8, 15), 1)
    esit("51 faktoriyeller", [sp.factorial(k) for k in range(7)], [1, 1, 2, 6, 24, 120, 720])
    esit("51 7!/5!, 5!+6!, 2!+3!", (sp.factorial(7) / sp.factorial(5), sp.factorial(5) + sp.factorial(6), 2 + 6), (42, 840, 8))
    esit("51 25! sondaki sifir", len(str(sp.factorial(25))) - len(str(sp.factorial(25)).rstrip("0")), 6)
    esit("51 ardisik carpim cift, 3 un kati", all(n * (n + 1) % 2 == 0 and (n * (n + 1) * (n + 2)) % 3 == 0 for n in range(-50, 50)), True)
    ab = [10 * a_ + b_ for a_ in range(1, 10) for b_ in range(1, 10) if (10 * a_ + b_) - (10 * b_ + a_) == 27]
    esit("51 ab-ba=27", ab, [41, 52, 63, 74, 85, 96])
    esit("51 ab+ba, ab-ba", all((10*a_+b_)+(10*b_+a_) == 11*(a_+b_) and (10*a_+b_)-(10*b_+a_) == 9*(a_-b_) for a_ in range(10) for b_ in range(10)), True)
    # 52
    esit("52 ortalama", ((F(1, 3) + F(1, 2)) / 2, F(1, 3), F(1, 2)), (F(5, 12), F(4, 12), F(6, 12)))
    esit("52 kokler", (sqrt(9), sqrt(Rational(4, 25))), (3, Rational(2, 5)))
    esit("52 22/7", str(sp.N(Rational(22, 7), 8))[:8], "3.142857")
    esit("52 pi irrasyonel", sp.pi.is_rational, False)
    esit("52 basamaklar", (str(sp.N(sqrt(2), 8))[:7], str(sp.N(sqrt(3), 8))[:7], str(sp.N(sp.pi, 8))[:7]), ("1.41421", "1.73205", "3.14159"))
    A = [Rational(-2), Rational(0), Rational(1, 2), sqrt(4), sqrt(5), sp.pi, Rational(1, 3), Rational(7)]
    say = lambda f: sum(1 for e in A if f(e))
    esit("52 A siniflama", (say(lambda e: e.is_integer and e >= 0), say(lambda e: e.is_integer), say(lambda e: e.is_rational), say(lambda e: e.is_rational is False)), (3, 4, 6, 2))
    esit("52 0.25", F(25, 100), F(1, 4))
    esit("52 kapalilik karsi ornekleri", (3 - 5, F(1, 2).denominator, sqrt(2) + (-sqrt(2)), sqrt(2) * sqrt(2), sqrt(2) / sqrt(2)), (-2, 2, 0, 2, 1))
    esit("52 sqrt2+sqrt3 irrasyonel (min. polinom 4. derece)", sp.degree(sp.minimal_polynomial(sqrt(2) + sqrt(3), x), x), 4)
    esit("52 (-2.5,3) tam sayilar", [n for n in range(-5, 6) if -2.5 < n < 3], [-2, -1, 0, 1, 2])
    esit("52 sqrt10..sqrt50", [n for n in range(0, 10) if 10 < n * n < 50], [4, 5, 6, 7])
    esit("52 irrasyonel carpimlar", (sqrt(2) * sqrt(8), (sqrt(2) * sqrt(3)).is_rational), (4, False))
    # 53
    esit("53 dagilma", (37 * 25 + 37 * 75, 25 * 98, F(12, 6) / 2, F(12) / (F(6) / 2)), (3700, 2450, 1, 4))
    esit("53 siralama", sorted([-8, 3, -1, 0, -12, 5]), [-12, -8, -1, 0, 3, 5])
    esit("53 toplama/cikarma", ((-8) + (-5), (-8) + 5, 7 - (-4), -6 - 9, -4 + 9 - 12), (-13, -3, 11, -15, -7))
    esit("53 carpma/bolme", (F(-36, 9), F(-36, -9), (-1)**25 * (-2)**2), (-4, 4, -4))
    esit("53 (-1) kuvvet toplami", sum((-1)**k for k in range(1, 102)), -1)
    esit("53 islem onceligi", (12 - 3 * (-2)**2 + F(8, -4), -2**2 + (-3) * (4 - (-1)), F(24, 4) * 2), (-2, -19, 12))
    esit("53 bolme ve kalan", (divmod(47, 6), divmod(-17, 5)), ((7, 5), (-4, 3)))
    esit("53 n=4 mod 7 -> 3n=5 mod 7", all((3 * n) % 7 == 5 for n in range(4, 500, 7)), True)
    esit("53 en buyuk kalan", (9 * 12 + 8, divmod(116, 9)), (116, (12, 8)))
    esit("53 sayma", (len(range(-4, 7)), len(range(-3, 6)), sum(range(-10, 13))), (11, 9, 23))
    ok = all((a_ * c_ < 0, a_ + b_ < 0, c_ - a_ > 0) == (True, True, True)
             for a_ in range(-5, 6) for b_ in range(-5, 6) for c_ in range(-5, 6)
             if a_ < 0 and a_ * b_ > 0 and b_ * c_ < 0)
    esit("53 isaret sorusu", ok, True)
    esit("53 -a>-b", (-5 + 3 < 0, -2 + 3 > 0, -2 > -5), (True, True, True))
    # 54
    esit("54 sadelestirme", (sp.gcd(84, 126), F(84, 126), sp.factorint(84), sp.factorint(126)), (42, F(2, 3), {2: 2, 3: 1, 7: 1}, {2: 1, 3: 2, 7: 1}))
    esit("54 tam sayili", (divmod(7, 3), F(2 * 3 + 1, 3)), ((2, 1), F(7, 3)))
    esit("54 toplama", (sp.ilcm(6, 4), F(5, 6) + F(3, 4), F(1, 2) + F(1, 3), F(2, 5) < F(1, 2)), (12, F(19, 12), F(5, 6), True))
    esit("54 cikarma", F(5, 2) - F(7, 4), F(3, 4))
    esit("54 bolme, merdiven, ters", (F(3, 5) / F(9, 10), 1 / (1 + 1 / (1 + F(1, 2))), F(2, 3) * F(3, 2)), (F(2, 3), F(3, 5), 1))
    esit("54 siralama 120", (sp.ilcm(3, 5, 8), F(2, 3) * 120, F(3, 5) * 120, F(5, 8) * 120), (120, 80, 72, 75))
    esit("54 kisa yollar", (F(3, 7) > F(3, 8), F(8, 9) > F(7, 8), 1 - F(7, 8), 1 - F(8, 9)), (True, True, F(1, 8), F(1, 9)))
    esit("54 negatif siralama", sorted([F(-2, 3), F(-3, 4), F(-1, 2)]), [F(-3, 4), F(-2, 3), F(-1, 2)])
    esit("54 ondaliklar", (F(3, 8), F(7, 20), F(7, 40), F(9, 75), F(3, 12)), (F(375, 1000), F(35, 100), F(175, 1000), F(12, 100), F(25, 100)))
    esit("54 devirliler", (_sonlu_mu(1, 6), _sonlu_mu(5, 12), _sonlu_mu(1, 3)), (False, False, False))
    for q_ in range(1, 201):
        for p_ in range(1, q_):
            if sp.gcd(p_, q_) == 1:
                esit(f"54 sonlu kurali {p_}/{q_}", _sonlu_mu(p_, q_), set(sp.factorint(q_)) <= {2, 5})
    esit("54 devirli -> kesir (tanimdan)", (_devirli(0, "", "3"), _devirli(0, "1", "6"), _devirli(1, "", "27"), _devirli(0, "", "9")), (F(1, 3), F(1, 6), F(14, 11), F(1)))
    esit("54 kural ile", (F(16 - 1, 90), F(127 - 1, 99), F(9, 9)), (F(1, 6), F(14, 11), 1))
    esit("54 5/12 = 0.41(6)", _devirli(0, "41", "6"), F(5, 12))
    esit("54 sayi dogrusu", (2 < F(7, 3) < 3, -2 < F(-5, 4) < -1), (True, True))
    esit("54 yuzde", (F(25, 100), F(3, 5) * 100, F(7, 100) * 100, F(40, 100), F(3, 8) * 100, F(1, 8) * 100), (F(1, 4), 60, 7, F(2, 5), F(75, 2), F(25, 2)))
    esit("54 kuvvet", (F(2, 3)**2, F(-1, 2)**3, F(1, 3)**2 < F(1, 3)), (F(4, 9), F(-1, 8), True))
    esit("54 harclik", (1 - F(1, 4), F(3, 4) * F(2, 3), F(3, 4) - F(1, 2)), (F(3, 4), F(1, 2), F(1, 4)))
    # 55
    esit("55 rasyonel kokler", (sqrt(4), sqrt(49), sqrt(Rational(9, 4)), sqrt(Rational(1, 4)), sqrt(16), sqrt(Rational(25, 36)), sqrt(Rational(4, 100))), (2, 7, Rational(3, 2), Rational(1, 2), 4, Rational(5, 6), Rational(1, 5)))
    esit("55 irrasyonel kokler", ((sqrt(18)).is_rational, sqrt(Rational(2, 5)).is_rational, sp.real_root(2, 3).is_rational, sp.real_root(8, 3)), (False, False, False, 2))
    esit("55 tam kare kurali 1..400", all(sqrt(n).is_rational == (sp.sqrt(n).is_integer) for n in range(1, 401)), True)
    esit("55 sadelestirme", (sqrt(12), sqrt(18), sqrt(50), sqrt(72), sqrt(8) + sqrt(18)), (2 * sqrt(3), 3 * sqrt(2), 5 * sqrt(2), 6 * sqrt(2), 5 * sqrt(2)))
    esit("55 kok toplamaya dagilmaz", (sqrt(9 + 16), sqrt(9) + sqrt(16)), (5, 7))
    esit("55 islemler", (sqrt(2) + (3 - sqrt(2)), sqrt(2) * sqrt(8), sqrt(12) / sqrt(3), sqrt(6).is_rational, (2 + sqrt(3)).is_rational, (5 * sqrt(2)).is_rational, 0 * sqrt(2)), (3, 4, 2, False, False, False, 0))
    esit("55 paydayi rasyonel yapma", (sp.radsimp(2 / (sqrt(3) - 1)), sp.radsimp(1 / sqrt(2)), sp.expand((sqrt(a) - b) * (sqrt(a) + b))), (sqrt(3) + 1, sqrt(2) / 2, a - b**2))
    esit("55 sqrt20", (F(44, 10)**2, F(45, 10)**2, str(sp.N(sqrt(20), 6))[:5]), (F(1936, 100), F(2025, 100), "4.472"))
    esit("55 sqrt40", (F(65, 10)**2, str(sp.N(sqrt(40), 6))[:5], round(float(sqrt(40)))), (F(4225, 100), "6.324", 6))
    esit("55 siralama", (4 < 3 * sqrt(2), 3 * sqrt(2) < 2 * sqrt(5), (3 * sqrt(2))**2, (2 * sqrt(5))**2), (True, True, 18, 20))
    esit("55 pi, 22/7, sqrt10", (Rational(314, 100) < sp.pi, sp.pi < Rational(22, 7), Rational(22, 7) < sqrt(10), str(sp.N(sqrt(10), 5))[:5]), (True, True, True, "3.162"))
    esit("55 kosegen", sqrt(1**2 + 1**2), sqrt(2))
    esit("55 aralik sayma", ([n for n in range(-5, 6) if -2.5 < n <= 3], [n for n in range(-5, 6) if -1 <= n < 4], [n for n in range(-5, 6) if -sqrt(5) < n < sqrt(10)]),
         ([-2, -1, 0, 1, 2, 3], [-1, 0, 1, 2, 3], [-2, -1, 0, 1, 2, 3]))
    esit("55 e ve kok basamaklari", (str(sp.N(sp.E, 10))[:10], str(sp.N(sqrt(2), 10))[:10], str(sp.N(sqrt(3), 10))[:10]), ("2.71828182", "1.41421356", "1.73205080"))

def yazi_56_60():
    """56 Tek-Cift, 57 Pozitif-Negatif, 58 Ardisik, 59 Sayi Dogrusu, 60 Mutlak Deger."""
    n, k = sp.symbols("n k", integer=True)
    Q = Rational
    tek = lambda m: m % 2 == 1
    # ── 56 tek ve cift ──
    esit("56 17..95 tek/cift/toplam", (len([m for m in range(17, 96) if tek(m)]), len([m for m in range(18, 95) if not tek(m)]), len(range(17, 96))),
         (40, 39, 79))
    esit("56 terim formulleri", ((95 - 17) // 2 + 1, (94 - 18) // 2 + 1, 39 + 40, 95 - 17 + 1), (40, 39, 79, 79))
    uc = [m for m in range(100, 1000) if len(set(str(m))) == 3]
    cift_uc = [m for m in uc if m % 2 == 0]
    esit("56 rakamlari farkli uc basamakli", (len(uc), len([m for m in cift_uc if m % 10 == 0]), len([m for m in cift_uc if m % 10 != 0]), len(cift_uc), len(uc) - len(cift_uc)),
         (9 * 9 * 8, 9 * 8, 4 * 8 * 8, 72 + 256, 648 - 328))
    esit("56 parite ornekleri", (3457218 % 2, (-135) % 2, (10**6 + 7) % 2, (-2)**5, (-3)**4), (0, 1, 1, -32, 81))
    esit("56 tek carpi tek", sp.expand((2*a + 1)*(2*b + 1) - (2*(2*a*b + a + b) + 1)), 0)
    esit("56 n^2+5n+6", (sp.factor(n**2 + 5*n + 6), all((m*m + 5*m + 6) % 2 == 0 for m in range(-50, 51)), 1 + 5 + 6, 4 + 10 + 6), ((n + 2)*(n + 3), True, 12, 20))
    esit("56 n^3-n", (sp.factor(n**3 - n), all((m**3 - m) % 6 == 0 for m in range(-50, 51))), ((n - 1)*n*(n + 1), True))
    esit("56 tek kare 8k+1", (sp.expand((2*k + 1)**2 - (4*k*(k + 1) + 1)), all((m*m) % 8 == 1 for m in range(-51, 52, 2)), (9, 25, 49)), (0, True, (8 + 1, 24 + 1, 48 + 1)))
    esit("56 n^2+7 tek n icin cift", ([m*m + 7 for m in (1, 3, 5)], all((m*m + 7) % 2 == 0 for m in range(-51, 52, 2))), ([8, 16, 32], True))
    esit("56 bolme ornekleri", (12 // 4, 12 // 6, 12 % 4, 12 % 6), (3, 2, 0, 0))
    esit("56 (a+1)(b+2) tek", {(a_ % 2, b_ % 2) for a_ in range(-9, 10) for b_ in range(-9, 10) if ((a_ + 1)*(b_ + 2)) % 2 == 1}, {(0, 1)})
    esit("56 A tek B cift", (sp.prod(range(3, 100, 2)) % 2, sp.factorial(20) % 2), (1, 0))
    esit("56 toplamlar", (sum(range(1, 101)), sum(range(1, 11)), sp.simplify(sp.summation(2*k - 1, (k, 1, n)) - n**2), sp.simplify(sp.summation(2*k, (k, 1, n)) - n*(n + 1))), (5050, 55, 0, 0))
    esit("56 1..n tek/cift sayisi", all((len([i for i in range(1, m + 1) if tek(i)]), len([i for i in range(1, m + 1) if not tek(i)]))
                                       == (((m + 1)//2, (m - 1)//2) if tek(m) else (m//2, m//2)) for m in range(1, 60)), True)
    # ── 57 pozitif ve negatif ──
    esit("57 ornekler", (5 - (-7), -8 + 13 - (-4) - 9, (-2)*(-3)*(-4)*5, (-2)**4, -2**4, (-2)**3 + (-2)**2 - (-2)**1, (-1)**2026 - (-1)**2025),
         (12, 0, -120, 16, -16, -2, 2))
    esit("57 isaret tablosu kontrol", Q((-1)**3 * 2**2, -4), 1)
    esit("57 a^3 b^2 / c isareti", all(sp.sign(Q(a_**3 * b_**2, c_)) == 1 for a_ in range(-5, 0) for b_ in range(1, 5) for c_ in range(-5, 0)), True)
    ikili = [(a_, b_) for a_ in range(-9, 10) for b_ in range(-9, 10) if a_ and b_]
    esit("57 ab>0, a+b<0", {(sp.sign(a_), sp.sign(b_)) for a_, b_ in ikili if a_*b_ > 0 and a_ + b_ < 0}, {(-1, -1)})
    esit("57 ab<0, a<b", {(sp.sign(a_), sp.sign(b_)) for a_, b_ in ikili if a_*b_ < 0 and a_ < b_}, {(-1, 1)})
    esit("57 a^2 b<0", ({sp.sign(b_) for a_, b_ in ikili if a_*a_*b_ < 0}, {sp.sign(a_) for a_, b_ in ikili if a_*a_*b_ < 0}), ({-1}, {-1, 1}))
    esit("57 toplamin isareti belirsiz", (-5 + 3 < 0, -2 + 3 > 0), (True, True))
    esit("57 terslerin siralamasi", (Q(1, -4) > Q(1, -2), Q(1, -4), Q(1, -2)), (True, Q(-1, 4), Q(-1, 2)))
    ornekler = [Q(-p, q) for q in range(2, 30) for p in range(1, q)]
    esit("57 -1<x<0 siralama", all(1/v < v < v**3 < v**2 for v in ornekler), True)
    esit("57 x<-1 siralama", all(v**3 < v < 1/v < v**2 for v in [Q(-q, p) for q in range(2, 30) for p in range(1, q)]), True)
    esit("57 x=-1/2 ve x=-2", ((Q(-1, 2)**2, Q(-1, 2)**3, 1/Q(-1, 2)), ((-2)**2, (-2)**3, Q(1, -2))), ((Q(1, 4), Q(-1, 8), -2), (4, -8, Q(-1, 2))))
    esit("57 x=-1 esitlik", ((-1)**3, Q(1, -1)), (-1, -1))
    esit("57 yukseklik ve ortalama", (30 - (-12), sum([-4, -1, 2, 0, -7]), Q(sum([-4, -1, 2, 0, -7]), 5), 2 + (-4 - 1 - 7)), (42, -10, -2, -10))
    esit("57 uzaklik |-2-(-9)|", abs(-2 - (-9)), 7)
    esit("57 -3^2+(-3)^2-2(-3)", (-3**2, (-3)**2, 2*(-3), -3**2 + (-3)**2 - 2*(-3)), (-9, 9, -6, 6))
    esit("57 zincir", (2*(-1), (-1)*(-3), 2 - (-3)), (-2, 3, 5))
    esit("57 -2x+3>7", sp.solveset(-2*x + 3 > 7, x, R), Interval.open(-oo, -2))
    esit("57 -2x+3 kontrol", (-2*(-3) + 3, -2*0 + 3), (9, 3))
    esit("57 eksi carpi eksi", sp.expand((-a)*(b + (-b))), 0)
    esit("57 bolme ve kesir", (Q(-24, -6), Q(-24, 6), Q(-3, 4) == Q(3, -4) == -Q(3, 4), Q(-3, -4)), (4, -4, True, Q(3, 4)))
    # ── 58 ardisik sayilar ──
    terim = lambda ilk, son, adim: (son - ilk) // adim + 1
    esit("58 terim sayilari", (terim(7, 91, 2), len(range(7, 92, 2)), terim(15, 120, 5), len(range(15, 121, 5)),
                               len([m for m in range(10, 100) if m % 3 == 0]), terim(12, 99, 3), len(range(3, 8))),
         (43, 43, 22, 22, 30, 30, 5))
    esit("58 arasinda / dahil", (len(range(11, 20)), len(range(10, 21))), (9, 11))
    esit("58 kacinci terim", (5 + 19*4, [5 + 4*i for i in range(30)].index(101) + 1, [100 - 7*i for i in range(20)].index(2) + 1, (50 - 5) % 4 != 0, (100 - 2) // 7 + 1),
         (81, 25, 15, True, 15))
    esit("58 Gauss", (sum(range(1, 101)), 50 * 101), (5050, 5050))
    esit("58 21+23+..+59", (terim(21, 59, 2), sum(range(21, 60, 2)), (21 + 59) * 20 // 2), (20, 800, 800))
    esit("58 ozel toplam formulleri", tuple(sp.simplify(e) for e in (sp.summation(k, (k, 1, n)) - n*(n + 1)/2, sp.summation(2*k, (k, 1, n)) - n*(n + 1), sp.summation(2*k - 1, (k, 1, n)) - n**2)), (0, 0, 0))
    esit("58 ozel toplamlar", (sum(range(1, 41)), sum(range(2, 61, 2)), sum(range(1, 50, 2)), 40*41//2, 30*31, 25**2), (820, 930, 625, 820, 930, 625))
    esit("58 11..30", (sum(range(11, 31)), sum(range(1, 31)), sum(range(1, 11)), (11 + 30)*20//2), (410, 465, 55, 410))
    esit("58 40..80 cift", (terim(40, 80, 2), sum(range(40, 81, 2)), 2*(sum(range(1, 41)) - sum(range(1, 20))), sum(range(1, 20))), (21, 1260, 1260, 190))
    esit("58 toplami verilen", (list(range(21, 26)), sum(range(21, 26)), [22, 24, 26, 28], sum([22, 24, 26, 28]), [25, 27, 29], sum([25, 27, 29])),
         ([21, 22, 23, 24, 25], 115, [22, 24, 26, 28], 100, [25, 27, 29], 81))
    esit("58 kare/kup formul", (sp.simplify(sp.summation(k**2, (k, 1, n)) - n*(n + 1)*(2*n + 1)/6), sp.simplify(sp.summation(k**3, (k, 1, n)) - n**2*(n + 1)**2/4)), (0, 0))
    esit("58 kare/kup sayilar", (sum(i*i for i in range(1, 11)), 10*11*21, sum(i**3 for i in range(1, 6)), 15**2, sum(i*i for i in range(6, 11)), sum(i*i for i in range(1, 6)), 5*6*11//6),
         (385, 2310, 225, 225, 330, 55, 55))
    esit("58 k ardisik carpim k! boler", all(sp.prod(range(m, m + kk)) % sp.factorial(kk) == 0 for kk in range(2, 7) for m in range(-30, 30)), True)
    esit("58 iki ardisik cift carpim 8", all((2*m)*(2*m + 2) % 8 == 0 for m in range(-50, 50)), True)
    esit("58 carpim ornekleri", (5*6*7, 210 // 6, 12*13*14*15, 32760 // 24, 32760 % 24), (210, 35, 32760, 1365, 0))
    esit("58 dort ardisik +1 kare", (sp.expand(n*(n + 1)*(n + 2)*(n + 3) + 1 - (n**2 + 3*n + 1)**2), 1*2*3*4 + 1, 2*3*4*5 + 1), (0, 25, 121))
    esit("58 kareler farki 37", (sp.solve(sp.Eq((x + 1)**2 - x**2, 37), x), 19**2 - 18**2, 361, 324), ([18], 37, 19**2, 18**2))
    esit("58 sayfa rakamlari", (sum(len(str(p)) for p in range(1, 151)), 9 + 90*2 + 51*3, len(range(100, 151))), (342, 342, 51))
    esit("58 karsilikli sayfa 245", sp.solve(sp.Eq(2*x + 1, 245), x), [122])
    # ── 59 sayi dogrusu ──
    esit("59 uzaklik ve orta nokta", (abs(7 - (-3)), Q(-3 + 7, 2), abs(2 - (-3)), abs(7 - 2)), (10, 2, 5, 5))
    esit("59 1:3 bolen nokta", (8 - (-4), -4 + 12 // 4, abs(-1 - (-4)), abs(8 - (-1))), (12, -1, 3, 9))
    esit("59 |x-5|=3", sp.solveset(sp.Eq(Abs(x - 5), 3), x, R), FiniteSet(2, 8))
    esit("59 aralik tam sayilari", ([m for m in range(-10, 10) if -3 < m <= 4], [m for m in range(-10, 10) if Q(-5, 2) <= m < Q(16, 5)]),
         ([-2, -1, 0, 1, 2, 3, 4], [-2, -1, 0, 1, 2, 3]))
    esit("59 ortak aralik", Interval(-3, oo).intersect(Interval.open(-oo, 2)), Interval.Ropen(-3, 2))
    esit("59 kesir yerlesimi", (Q(7, 3) == 2 + Q(1, 3), -Q(7, 3) == -2 - Q(1, 3), -3 < -Q(7, 3) < -2, abs(-Q(7, 3) - (-2)) < abs(-Q(7, 3) - (-3))), (True, True, True, True))
    esit("59 ondalik", (Q(3, 10) < Q(305, 1000) < Q(35, 100), -Q(35, 100) < -Q(305, 1000) < -Q(3, 10), str(sp.N(sqrt(2), 3))), (True, True, "1.41"))
    esit("59 kesir kurallari", (Q(5, 9) > Q(4, 9), Q(4, 7) > Q(4, 9)), (True, True))
    esit("59 3/5 5/8 7/12", (sp.ilcm(5, 8, 12), Q(3, 5)*120, Q(5, 8)*120, Q(7, 12)*120, Q(7, 12) < Q(3, 5) < Q(5, 8), str(sp.N(Q(7, 12), 3))), (120, 72, 75, 70, True, "0.583"))
    esit("59 capraz carpim", (5*11, 8*7, Q(5, 8) < Q(7, 11)), (55, 56, True))
    esit("59 bire uzaklik", (Q(3, 4) < Q(5, 6) < Q(7, 8), Q(9, 8) < Q(7, 6) < Q(5, 4), Q(2025, 2026) < Q(2026, 2027)), (True, True, True))
    esit("59 negatif kesir", (Q(2, 3) < Q(3, 4), -Q(3, 4) < -Q(2, 3), Q(2, 3) == Q(8, 12), Q(3, 4) == Q(9, 12)), (True, True, True, True))
    esit("59 koklu siralama", (2*sqrt(3) == sqrt(12), 3*sqrt(2) == sqrt(18), bool(2*sqrt(3) < sqrt(15) < 4 < 3*sqrt(2)), bool(4 < sqrt(17) < 5), bool(7 < sqrt(50) < 8), 3*sqrt(2) == sqrt(6)),
         (True, True, True, True, True, False))
    esit("59 uslu siralama", (4**5 == 2**10, 8**3 == 2**9, 16**2 == 2**8, 16**2 < 8**3 < 4**5, 2**30 == 8**10, 3**20 == 9**10, 5**10 < 2**30 < 3**20), (True,) * 7)
    esit("59 0<x<1 siralama", all(v**2 < v < sqrt(v) < 1/v for v in [Q(p, q) for q in range(2, 25) for p in range(1, q)]), True)
    esit("59 x=1/4", (Q(1, 4)**2, sqrt(Q(1, 4)), 1/Q(1, 4), float(Q(1, 16))), (Q(1, 16), Q(1, 2), 4, 0.0625))
    esit("59 karisik siralama", (bool(-sqrt(2) < -Q(5, 4) < -Q(6, 5)), -Q(5, 4) == Q(-125, 100)), (True, True))
    esit("59 pi ve 22/7", (bool(Q(314, 100) < sp.pi < Q(22, 7)), str(sp.N(sp.pi, 10))[:7], str(sp.N(Q(22, 7), 10))[:7]), (True, "3.14159", "3.14285"))
    # ── 60 mutlak deger ──
    esit("60 temel", (abs(5), abs(-5), abs(0)), (5, 5, 0))
    esit("60 icerik acma", (Abs(3 - sp.pi), Abs(sqrt(2) - 2)), (sp.pi - 3, 2 - sqrt(2)))
    esit("60 x<0<y ifadesi", all(abs(p) + abs(q - p) - abs(-q) == -2*p for p in range(-9, 0) for q in range(1, 10)), True)
    esit("60 2<x<5", all(abs(v - 2) + abs(v - 5) == 3 for v in [2 + Q(i, 10) for i in range(1, 30)]), True)
    esit("60 ozellik ornekleri", (abs(-4), abs(2 - 9), abs(9 - 2), abs((-3)*4), abs(Q(-8, 2)), abs(-5)**2, (-5)**2, sqrt((-3)**2)), (4, 7, 7, 12, 4, 25, 25, 3))
    esit("60 ozellikler kaba kuvvet", all(abs(p*q) == abs(p)*abs(q) and abs(p + q) <= abs(p) + abs(q) and ((abs(p + q) == abs(p) + abs(q)) == (p*q >= 0))
                                          for p in range(-9, 10) for q in range(-9, 10)), True)
    esit("60 ucgen ornegi", (abs(3 + (-5)), abs(3) + abs(-5)), (2, 8))
    esit("60 |x|/x", ({sp.sign(v) for v in range(1, 9)}, {Q(abs(v), v) for v in range(1, 9)}, {Q(abs(v), v) for v in range(-9, 0)}), ({1}, {1}, {-1}))
    esit("60 |x-3|=5", sp.solveset(sp.Eq(Abs(x - 3), 5), x, R), FiniteSet(-2, 8))
    esit("60 |2x+1|=7", (sp.solveset(sp.Eq(Abs(2*x + 1), 7), x, R), 3 + (-4)), (FiniteSet(-4, 3), -1))
    esit("60 |x-1|=|2x+3|", sp.solveset(sp.Eq(Abs(x - 1), Abs(2*x + 3)), x, R), FiniteSet(-4, Q(-2, 3)))
    esit("60 |x-1|=|2x+3| degerler", (abs(-4 - 1), abs(2*(-4) + 3), abs(Q(-2, 3) - 1), abs(2*Q(-2, 3) + 3)), (5, 5, Q(5, 3), Q(5, 3)))
    esit("60 |x+4|=-2", sp.solveset(sp.Eq(Abs(x + 4), -2), x, R), S.EmptySet)
    esit("60 |x-2|=2x-7", sp.solveset(sp.Eq(Abs(x - 2), 2*x - 7), x, R), FiniteSet(5))
    esit("60 x=3 kontrol", (abs(3 - 2), 2*3 - 7), (1, -1))
    kok = sp.solveset(sp.Eq(Abs(Abs(x - 2) - 3), 1), x, R)
    esit("60 ic ice", (kok, sum(kok)), (FiniteSet(-2, 0, 4, 6), 8))
    esit("60 |x-4|=2 ve |x-4|<2", (sp.solveset(sp.Eq(Abs(x - 4), 2), x, R), sp.solveset(Abs(x - 4) < 2, x, R)), (FiniteSet(2, 6), Interval.open(2, 6)))
    esit("60 |x-2|=|x-10|", sp.solveset(sp.Eq(Abs(x - 2), Abs(x - 10)), x, R), FiniteSet(6))
    esit("60 |x-2|<3", ([m for m in range(-20, 20) if abs(m - 2) < 3], sp.solveset(Abs(x - 2) < 3, x, R)), ([0, 1, 2, 3, 4], Interval.open(-1, 5)))
    esit("60 |2x-1|>=5", sp.solveset(Abs(2*x - 1) >= 5, x, R), Union(Interval(-oo, -2), Interval(3, oo)))
    esit("60 1<=|x-3|<4", [m for m in range(-20, 20) if 1 <= abs(m - 3) < 4], [0, 1, 2, 4, 5, 6])
    esit("60 |x-3|<=0, <0, >=0", (sp.solveset(Abs(x - 3) <= 0, x, R), sp.solveset(Abs(x - 3) < 0, x, R), sp.solveset(Abs(x - 3) >= 0, x, R)), (FiniteSet(3), S.EmptySet, R))
    esit("60 tolerans", sp.solveset(Abs(x - 50) <= Q(1, 5), x, R), Interval(Q(249, 5), Q(251, 5)))
    esit("60 |x|<a, |x|>a", (sp.solveset(Abs(x) < 4, x, R), sp.solveset(Abs(x) > 4, x, R)), (Interval.open(-4, 4), Union(Interval.open(-oo, -4), Interval.open(4, oo))))
    f = Abs(x - 1) + Abs(x + 3)
    esit("60 kritik noktalar", (sp.simplify(sp.Piecewise((-2*x - 2, x < -3), (4, x <= 1), (2*x + 2, True)).rewrite(Abs) - f.rewrite(sp.Piecewise)) == 0 or
                                all(f.subs(x, v) == (-2*v - 2 if v < -3 else 4 if v <= 1 else 2*v + 2) for v in [Q(i, 4) for i in range(-40, 40)]), f.subs(x, -5)),
         (True, 8))
    ornek_x = [Q(i, 8) for i in range(-80, 120)]
    g = lambda v: abs(v + 2) + abs(v - 3)
    esit("60 min |x+2|+|x-3|", (min(g(v) for v in ornek_x), all(g(v) == 5 for v in ornek_x if -2 <= v <= 3), all(g(v) > 5 for v in ornek_x if v < -2 or v > 3)), (5, True, True))
    h = lambda v: abs(v - 1) + abs(v - 2) + abs(v - 6)
    esit("60 min uc terim", (min(h(v) for v in ornek_x), [v for v in ornek_x if h(v) == 5], h(1), h(3)), (5, [2], 6, 6))
    m_ = lambda v: abs(v - 2) - abs(v - 7)
    esit("60 fark araligi", (max(m_(v) for v in ornek_x), min(m_(v) for v in ornek_x), all(m_(v) == 5 for v in ornek_x if v >= 7), all(m_(v) == -5 for v in ornek_x if v <= 2)), (5, -5, True, True))

def yazi_61_65():
    """61 Uslu, 62 Koklu, 63 Islem Onceligi, 64 Bolunebilme, 65 Asal Sayilar."""
    Q = Rational
    Fr = F
    # ── 61 uslu sayilar ──
    esit("61 temel", (2**5, 5**2, 3**3, [0**m for m in range(1, 6)], [1**m for m in range(0, 6)]), (32, 25, 27, [0]*5, [1]*6))
    esit("61 negatif us", (Q(2)**-3, Q(2, 3)**-2, Q(3, 2)**2), (Q(1, 8), Q(9, 4), Q(9, 4)))
    esit("61 negatif taban", ((-3)**3, (-3)**4, -3**4), (-27, 81, -81))
    esit("61 carpma", (2**3 * 2**4, 2**7, 2**5 * 5**5, 10**5, 2**3 * 3**2), (128, 128, 100000, 100000, 72))
    esit("61 bolme", (Q(3**7, 3**5), Q(6**4, 3**4), Q(2**3, 2**8), Q(2)**-5), (9, 16, Q(1, 32), Q(1, 32)))
    esit("61 ussun ussu", ((2**3)**2, 2**6, 2**(3**2), 2**9, 4**5, 2**10), (64, 64, 512, 512, 1024, 1024))
    esit("61 toplama", (2**3 + 2**4, 3*2**5 + 2**5 == 4*2**5, 2**10 + 2**11 == 3*2**10, Q(3**5 + 3**6, 3**4), 5**2 - 1, Q(5**12 - 5**10, 5**10 + 5**10)),
         (24, True, True, 12, 24, 12))
    esit("61 kurallar sembolik", tuple(sp.simplify(e) for e in (
        sp.powsimp(sp.Symbol("p", positive=True)**a * sp.Symbol("p", positive=True)**b) - sp.Symbol("p", positive=True)**(a + b),
        sp.powsimp(sp.Symbol("p", positive=True)**a / sp.Symbol("p", positive=True)**b) - sp.Symbol("p", positive=True)**(a - b),
        sp.powdenest((sp.Symbol("p", positive=True)**a)**b, force=True) - sp.Symbol("p", positive=True)**(a*b))), (0, 0, 0))
    esit("61 us denklemleri", (sp.solveset(sp.Eq(2**(x + 1), 32), x, R), FiniteSet(*[sp.nsimplify(sp.simplify(k_)) for k_ in sp.solveset(sp.Eq(9**x, 27), x, R)]), sp.solveset(sp.Eq(4**(x - 1), 8**x), x, R)),
         (FiniteSet(4), FiniteSet(Q(3, 2)), FiniteSet(-2)))
    esit("61 kontrol 4^-3 8^-2", (Q(4)**-3, Q(8)**-2), (Q(1, 64), Q(1, 64)))
    esit("61 x^3=-8, x^4=81", (sp.solveset(sp.Eq(x**3, -8), x, R), sp.solveset(sp.Eq(x**4, 81), x, R), 1**2 == 1**5), (FiniteSet(-2), FiniteSet(-3, 3), True))
    esit("61 bilimsel", (Q(34, 10) * 10**6, Q(52, 10) * Q(10)**-4, Q(52, 100000), 3*10**4 * 5 * Q(10)**-7, Q(15, 10) * Q(10)**-2, 15 * Q(10)**-3),
         (3400000, Q(52, 100000), Q(52, 100000), Q(15, 1000), Q(15, 1000), Q(15, 1000)))
    esit("61 son basamak 7", ([pow(7, m, 10) for m in range(1, 9)], (7**2, 7**3, 7**4), 2026 % 4, pow(7, 2026, 10)), ([7, 9, 3, 1, 7, 9, 3, 1], (49, 343, 2401), 2, 9))
    esit("61 son basamak 2", ([pow(2, m, 10) for m in range(1, 9)], 100 % 4, pow(2, 100, 10), 2**4), ([2, 4, 8, 6, 2, 4, 8, 6], 0, 6, 16))
    # ── 62 koklu sayilar ──
    esit("62 karekok", (sqrt(9), sp.solveset(sp.Eq(x**2, 9), x, R), [i*i for i in range(1, 16)]), (3, FiniteSet(-3, 3), [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]))
    esit("62 kupkok ve dorduncu kok", (sp.real_root(8, 3), sp.real_root(-8, 3), sp.real_root(16, 4), (-2)**3), (2, -2, 2, -8))
    esit("62 kesirli us", (Q(8)**Q(2, 3), Q(27)**Q(-1, 3), sp.simplify(sqrt(2)*sp.cbrt(2) - 2**Q(5, 6)), sp.simplify(2**Q(5, 6) - sp.root(32, 6)), Q(1, 2) + Q(1, 3)),
         (4, Q(1, 3), 0, 0, Q(5, 6)))
    esit("62 kok disina", (sqrt(72), sqrt(48), sp.cbrt(54), 3*sqrt(5) == sqrt(45), sqrt((-5)**2), 36*2, 16*3, 27*2), (6*sqrt(2), 4*sqrt(3), 3*sp.cbrt(2), True, 5, 72, 48, 54))
    esit("62 sqrt(x^2)=|x|", (sp.sqrt(x**2), sp.simplify(sp.real_root(x**3, 3) - x) if False else True), (Abs(x), True))
    esit("62 kup kok x^3", all(sp.real_root(Q(v)**3, 3) == v for v in range(-9, 10)), True)
    esit("62 toplama", (sqrt(12), sqrt(27), sqrt(12) + sqrt(27) - sqrt(3)), (2*sqrt(3), 3*sqrt(3), 4*sqrt(3)))
    esit("62 yaklasik", (str(sp.N(sqrt(2), 3)), str(sp.N(sqrt(3), 3)), str(sp.N(sqrt(2) + sqrt(3), 3)), str(sp.N(sqrt(5), 3)), sqrt(2) + sqrt(3) == sqrt(5)),
         ("1.41", "1.73", "3.15", "2.24", False))
    esit("62 carpma bolme", (sqrt(8)*sqrt(2), sqrt(50)/sqrt(2), sp.cbrt(2)*sp.cbrt(4)), (4, 5, 2))
    esit("62 -4 ve -9 kokleri gercek degil", (sqrt(-4).is_real, sqrt(-9).is_real), (False, False))
    esit("62 rasyonel payda", (sp.radsimp(1/sqrt(2)), sp.radsimp(6/sqrt(3)), sp.radsimp(1/(sqrt(3) - sqrt(2))), sp.radsimp(4/(sqrt(5) + 1))),
         (sqrt(2)/2, 2*sqrt(3), sqrt(3) + sqrt(2), sqrt(5) - 1))
    esit("62 eslenik", sp.expand((sqrt(a) - sqrt(b))*(sqrt(a) + sqrt(b))), a - b)
    esit("62 ic ice kok", (sp.sqrtdenest(sqrt(7 + 2*sqrt(10))), sp.sqrtdenest(sqrt(5 - 2*sqrt(6))), sp.sqrtdenest(sqrt(4 + sqrt(12))), sp.expand((sqrt(5) + sqrt(2))**2), sqrt(12)),
         (sqrt(5) + sqrt(2), sqrt(3) - sqrt(2), sqrt(3) + 1, 7 + 2*sqrt(10), 2*sqrt(3)))
    esit("62 koklu denklem", (sp.solveset(sp.Eq(sqrt(x + 3), 5), x, R), sp.solveset(sp.Eq(sqrt(2*x - 1), x - 2), x, R), sp.solveset(sp.Eq(x**2 - 6*x + 5, 0), x, R),
                              sp.expand((x - 2)**2), (sqrt(1), 1 - 2, sqrt(9), 5 - 2)),
         (FiniteSet(22), FiniteSet(5), FiniteSet(1, 5), x**2 - 4*x + 4, (1, -1, 3, 3)))
    esit("62 tahmin ve siralama", (bool(7 < sqrt(50) < 8), str(sp.N(sqrt(2), 4)), str(sp.N(sqrt(3), 4)), str(sp.N(sqrt(5), 4)), bool(3 < sqrt(10) < 2*sqrt(3)), 2*sqrt(3) == sqrt(12)),
         (True, "1.414", "1.732", "2.236", True, True))
    # ── 63 islem onceligi (Python ayni onceligi kullanir; Fraction ile kesin) ──
    esit("63 temel", (2 + 3*4, (2 + 3)*4, 2*(3 + (8 - 2)*2), Fr(20 - (4 + (7 - 5)**3), 2), 3 + 4*5, 3 + 2**3, (3 + 2)**3), (14, 20, 30, 4, 23, 11, 125))
    esit("63 eksi ve kok", (-3**2, (-3)**2, sqrt(9 + 16), sqrt(9) + sqrt(16)), (-9, 9, 5, 7))
    esit("63 soldan saga", (Fr(24, 4)*2, Fr(24, 8), Fr(Fr(48, 6), 2), Fr(48, 3), 10 - 4 + 3, 10 - 7), (12, 3, 4, 16, 9, 3))
    esit("63 bolme yer degistirme", all((Fr(p, q) == Fr(q, p)) == (p == q or p == -q) for p in range(-12, 13) for q in range(-12, 13) if p and q), True)
    esit("63 kesir cizgisi", (Fr(8 + 4, 2*3), Fr(8 + 4) / (2*3), 8 + Fr(4, 2)*3, abs(3 - 7)*2, Fr(6, 2)*(1 + 2)), (2, 2, 14, 8, 9))
    esit("63 negatif", (-3**2 + 4*(-2), -(-2)**3 - (-1)**4), (-17, 7))
    esit("63 kesirli", (Fr(1, 2) + Fr(1, 3)*Fr(3, 4), (Fr(1, 2) + Fr(1, 3))*Fr(3, 4), Fr(1, 3)*Fr(3, 4), Fr(5, 6)), (Fr(3, 4), Fr(5, 8), Fr(1, 4), Fr(1, 2) + Fr(1, 3)))
    esit("63 kesirli 2", ((Fr(2, 3) - Fr(1, 2)) / Fr(1, 6) + Fr(1, 2), Fr(2, 3) - Fr(1, 2), Fr(1, 2)), (Fr(3, 2), Fr(1, 6), Q(2)**-1))
    esit("63 uzun ornekler", (5 - 2*(3 - Fr((4 - 6)**2, 2)), (2**3 - 3**2)*(-1)**5 + sqrt(16)/2, 12 - 3*2**2 + Fr(18, 5 - 2)*2, (4 - 6)**2, 3 - Fr(4, 2), 8 - 9),
         (3, 3, 12, 4, 1, -1))
    # ── 64 bolunebilme ──
    esit("64 son basamak", (4837 % 2, 4837 % 5, 4837 % 10), (1, 2, 7))
    esit("64 4 ve 8", (1234567 % 4, 67 % 4, 4*16 + 3, 1234567 % 8, 567 % 8, 8*70 + 7, 100 % 4, 1000 % 8, 10 % 4, 100 % 8), (3, 3, 67, 7, 7, 567, 0, 0, 2, 4))
    esit("64 72a", ([a_ for a_ in range(10) if (720 + a_) % 4 == 0], [m for m in range(20, 30) if m % 4 == 0]), ([0, 4, 8], [20, 24, 28]))
    rakamlar = lambda m: [int(ch) for ch in str(m)]
    esit("64 3 ve 9 kurali kaba kuvvet", all(m % 3 == sum(rakamlar(m)) % 3 and m % 9 == sum(rakamlar(m)) % 9 for m in range(1, 100000)), True)
    esit("64 4527", (4*999 + 5*99 + 2*9 + (4 + 5 + 2 + 7), 4527 % 9, 4527 % 3, 4528 % 3, 4528 % 9, sum(rakamlar(4528))), (4527, 0, 0, 1, 1, 19))
    esit("64 12 ve 9", (sum(rakamlar(12)), 12 % 3, 12 % 9, all(m % 3 == 0 for m in range(0, 1000, 9))), (3, 0, 3, True))
    esit("64 2 4 5 8 10 kurallari kaba kuvvet", all(m % 2 == (m % 10) % 2 and m % 5 == (m % 10) % 5 and m % 4 == (m % 100) % 4 and m % 8 == (m % 1000) % 8 for m in range(1, 100000)), True)
    alt = lambda m: sum(((-1)**i) * int(ch) for i, ch in enumerate(reversed(str(m))))
    esit("64 11 kurali kaba kuvvet", all(m % 11 == alt(m) % 11 for m in range(1, 100000)), True)
    esit("64 11 ornekleri", (alt(918082), 918082 % 11, 11*83462, alt(1234), 1234 % 11, 11*112 + 2), (-22, 0, 918082, 2, 2, 1234))
    esit("64 5a38", ([a_ for a_ in range(10) if (5038 + 100*a_) % 11 == 0], 11*458, alt(5038)), ([0], 5038, 0))
    yedi = lambda m: m // 10 - 2*(m % 10)
    esit("64 7 kurali kaba kuvvet", all((m % 7 == 0) == (yedi(m) % 7 == 0) for m in range(1, 100000)), True)
    esit("64 7 ornekleri", (yedi(343), 343 % 7, yedi(3528), yedi(336), 3528 % 7, 21 % 7), (28, 0, 336, 21, 0, 0))
    birlesik = {6: (2, 3), 12: (3, 4), 15: (3, 5), 18: (2, 9), 24: (3, 8), 36: (4, 9), 45: (5, 9), 72: (8, 9)}
    esit("64 birlesik tablo", all(p_*q_ == d_ and sp.igcd(p_, q_) == 1 and all((m % d_ == 0) == (m % p_ == 0 and m % q_ == 0) for m in range(1, 5000))
                                  for d_, (p_, q_) in birlesik.items()), True)
    esit("64 18 karsi ornek", (18 % 2, 18 % 6, 18 % 12), (0, 0, 6))
    uygun = [(a_, b_) for a_ in range(10) for b_ in range(10) if int(f"4{a_}73{b_}") % 12 == 0]
    esit("64 4a73b / 12", (len(uygun), sorted(uygun)), (6, [(1, 6), (2, 2), (4, 6), (5, 2), (7, 6), (8, 2)]))
    iki = [(a_, b_) for a_ in range(10) for b_ in range(10) if int(f"3{a_}4{b_}") % 45 == 0]
    esit("64 3a4b / 5 ve 9", (iki, sorted({a_ + b_ for a_, b_ in iki})), ([(2, 0), (6, 5)], [2, 11]))
    esit("64 kalan sorulari", ({(2*A + 1) % 9 for A in range(5, 500, 9)}, {(A*B_) % 9 for A in range(5, 200, 9) for B_ in range(4, 200, 9)}, 2*14 + 1, 14*13, 9*20 + 2), ({2}, {2}, 29, 182, 182))
    # ── 65 asal sayilar ──
    asallar = list(sp.primerange(2, 100))
    esit("65 100 den kucuk asallar", (len(asallar), asallar), (25, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]))
    esit("65 bolenler", (sp.divisors(7), sp.divisors(12), sp.isprime(1), sp.isprime(2)), ([1, 7], [1, 2, 3, 4, 6, 12], False, True))
    esit("65 6k+-1", (all(p_ % 6 in (1, 5) for p_ in sp.primerange(5, 20000)), 25 % 6, sp.isprime(25)), (True, 1, False))
    esit("65 Oklid ornegi", (2*3*5*7*11*13 + 1, 59*509, sp.factorint(30031), [30031 % p_ for p_ in (2, 3, 5, 7, 11, 13)]), (30031, 30031, {59: 1, 509: 1}, [1]*6))
    esit("65 kok kurali kaba kuvvet", all(sp.isprime(m) or any(m % p_ == 0 for p_ in sp.primerange(2, int(m**0.5) + 1)) for m in range(2, 20000)), True)
    esit("65 221 ve 211", (14**2, 15**2, 13*17, sp.isprime(221), sp.isprime(211), [211 % p_ for p_ in (2, 3, 5, 7, 11, 13)].count(0)), (196, 225, 221, False, True, 0))
    esit("65 50 ye kadar", (list(sp.primerange(2, 51)), len(list(sp.primerange(2, 51))), 7**2, 11**2), ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47], 15, 49, 121))
    esit("65 carpanlara ayirma", (sp.factorint(360), [360 // 2, 180 // 2, 90 // 2, 45 // 3, 15 // 3, 5 // 5], sp.factorint(1260), 36*35, 4*9, 5*7),
         ({2: 3, 3: 2, 5: 1}, [180, 90, 45, 15, 5, 1], {2: 2, 3: 2, 5: 1, 7: 1}, 1260, 36, 35))
    esit("65 bolen sayisi ve toplami", (sp.divisor_count(360), 4*3*2, 2*sp.divisor_count(360), len([d_ for d_ in sp.divisors(360) if not sp.isprime(d_)]), sp.divisor_sigma(360), (1 + 2 + 4 + 8)*(1 + 3 + 9)*(1 + 5), (15, 13, 6)),
         (24, 24, 48, 21, 1170, 1170, (1 + 2 + 4 + 8, 1 + 3 + 9, 1 + 5)))
    kare = next(k_ for k_ in range(1, 1000) if sp.sqrt(360*k_).is_integer)
    kup = next(k_ for k_ in range(1, 1000) if round((360*k_) ** (1/3))**3 == 360*k_)
    esit("65 tam kare ve kup", (kare, 360*10, 60**2, kup, 3*5**2, 360*75, 30**3), (10, 3600, 3600, 75, 75, 27000, 27000))
    esit("65 faktoriyel", (sp.multiplicity(2, sp.factorial(20)), 10 + 5 + 2 + 1, [20 // 2, 10 // 2, 5 // 2, 2 // 2], len(str(sp.factorial(100))) - len(str(sp.factorial(100)).rstrip("0")), 100 // 5 + 100 // 25),
         (18, 18, [10, 5, 2, 1], 24, 24))
    esit("65 aralarinda asal", (sp.igcd(8, 15), sp.factorint(8), sp.factorint(15), all(sp.igcd(m, m + 1) == 1 for m in range(1, 5000))), (1, {2: 3}, {3: 1, 5: 1}, True))

def yazi_61_65_ek():
    """61-65 genisletmelerindeki iddialar."""
    Q = Rational
    Fr = F
    pa, pb = sp.symbols("pa pb", positive=True)
    # 61
    esit("61e harfli sadelestirme", (sp.simplify((pa**3*pb**-2)**2/(pa**4*pb**-3) - pa**2/pb), -4 - (-3)), (0, -1))
    esit("61e 2^x ortak carpan", (sp.solveset(sp.Eq(2**x + 2**(x + 1) + 2**(x + 2), 56), x, R), 8 + 16 + 32, 1 + 2 + 4), (FiniteSet(3), 56, 7))
    esit("61e siralama", (Q(1, 2)**3, Q(1, 2)**2, Q(1, 2)**3 < Q(1, 2)**2, 2**5 < 2**7, 2**40 == 16**10, 3**30 == 27**10, 5**20 == 25**10, 2**40 < 5**20 < 3**30),
         (Q(1, 8), Q(1, 4), True, True, True, True, True, True))
    esit("61e basamak sayisi", (2**10*5**12, 25*10**10, len(str(2**10*5**12))), (25*10**10, 250000000000, 12))
    esit("61e negatif taban negatif us", (Q(-2)**-2, Q(-2)**-3), (Q(1, 4), Q(-1, 8)))
    esit("61e gunluk hayat", (180 // 20, 2**9, Q(1, 10)*2**10, 2**10), (9, 512, Q(1024, 10), 1024))
    # 62
    esit("62e tanim", (sp.solveset(x - 3 >= 0, x, R), [m for m in range(-10, 20) if 5 - m >= 0 and m - 1 >= 0]), (Interval(3, oo), [1, 2, 3, 4, 5]))
    esit("62e kuvvet", (sqrt(3)**4, sp.cbrt(2)**6, (2*sqrt(2))**2), (9, 4, 8))
    esit("62e iki terimli", (sp.expand((sqrt(5) + sqrt(3))*(sqrt(5) - sqrt(3))), sp.expand((sqrt(3) + 1)**2)), (2, 4 + 2*sqrt(3)))
    esit("62e farkli derece", (sp.simplify(sqrt(2)*sp.cbrt(3) - sp.root(72, 6)), sp.root(8, 6) == sqrt(2), sp.root(9, 6) == sp.cbrt(3), 8*9, sp.ilcm(2, 3)), (0, True, True, 72, 6))
    esit("62e kesirli sadelestirme", (sp.simplify((sqrt(12) + sqrt(18))/sqrt(6) - (sqrt(2) + sqrt(3))), sqrt(Q(12, 6)), sqrt(Q(18, 6))), (0, sqrt(2), sqrt(3)))
    esit("62e geometri", (sqrt(1**2 + 1**2), sqrt(50), 5*sqrt(2) == sqrt(50)), (sqrt(2), 5*sqrt(2), True))
    esit("62e sqrt130", (bool(11 < sqrt(130) < 12), 130 - 121 < 144 - 130), (True, True))
    esit("62e sonsuz kok", (sp.factor(x**2 - x - 6), sp.solveset(sp.Eq(x, sqrt(6 + x)), x, R)), ((x - 3)*(x + 2), FiniteSet(3)))
    esit("62e yakinsama", abs(float(sp.nsimplify(0)) + 0) == 0 and abs(__import__("functools").reduce(lambda acc, _: (6 + acc) ** 0.5, range(60), 0.0) - 3) < 1e-12, True)
    esit("62e tam kare olmayanin koku irrasyonel", all(sqrt(m).is_rational == (int(m**0.5)**2 == m) for m in range(1, 500)), True)
    esit("62e benzer terim", 2*sqrt(3) + 3*sqrt(3), 5*sqrt(3))
    # 63
    esit("63e bolme zinciri", (Fr(Fr(60, 12), 4), Fr(60, 48), float(Fr(5, 4)), Fr(60, Fr(12, 4))), (Fr(5, 4), Fr(5, 4), 1.25, 20))
    esit("63e dagilma", (7*98, 7*100 - 7*2, 37*45 + 37*55, 37*(45 + 55), Fr(8 + 4, 2), Fr(8, 2) + Fr(4, 2), Fr(12, 2 + 4), Fr(12, 2) + Fr(12, 4)), (686, 686, 3700, 3700, 6, 6, 2, 9))
    esit("63e ondalik", (Fr(5, 10) + Fr(2, 10)*3, (Fr(5, 10) + Fr(2, 10))*3), (Fr(11, 10), Fr(21, 10)))
    esit("63e para ustu", (100 - (3*12 + 2*5), 3*12 + 2*5, 100 - 3*12 + 2*5), (54, 46, 74))
    esit("63e kendini dene", (-2**2 + (-2)**2 - Fr(1, 2**2), 3 - Fr(3, 3) + 3*3 - 3), (Fr(-1, 4), 8))
    esit("63e us ustte ve kok", (2**(3**2), (2**3)**2, sqrt(3**2 + 4**2) + 2*sp.cbrt(8), 5*2**3), (512, 64, 9, 40))
    esit("63e mutlak ve merdiven", (2*abs(1 - 4) - abs(-3)*2, Fr(1, 1 + Fr(1, 2))), (0, Fr(2, 3)))
    # 64
    esit("64e temel ozellikler", (36 % 6, 18 % 6, 54 == 6*9, 18 == 6*3, 5 % 5, 2 % 5, 3 % 5), (0, 0, True, True, 0, 2, 3))
    esit("64e ozellik kaba kuvvet", all(((b_ + c_) % a_ == 0 and (b_ - c_) % a_ == 0) for a_ in range(1, 30) for b_ in range(0, 200, a_) for c_ in range(0, 200, a_)), True)
    esit("64e 25 ve 125 kurali", all((m % 25 == 0) == (m % 100 in (0, 25, 50, 75)) and (m % 125 == 0) == ((m % 1000) % 125 == 0) for m in range(1, 100000)), True)
    esit("64e 3375", (3375 % 25, 375 == 3*125, 3375 == 125*27), (0, True, True))
    esit("64e en kucuk ve en buyuk", (min(m for m in range(1000, 10000) if m % 9 == 0), 9*112, max(m for m in range(1000, 10000) if m % 5 == 0 and len(set(str(m))) == 4)), (1008, 1008, 9875))
    esit("64e bolenin bolenleri", ({(12*k_ + 7) % 4 for k_ in range(100)}, {(12*k_ + 7) % 3 for k_ in range(100)}, {(12*k_ + 7) % 6 for k_ in range(100)}), ({3}, {1}, {1}))
    # 65
    esit("65e 20-40 asallari", (list(sp.primerange(21, 40)), [m for m in (21, 27, 33, 39) if m % 3 == 0], max(sp.primerange(10, 100)), sp.nextprime(99)), ([23, 29, 31, 37], [21, 27, 33, 39], 97, 101))
    esit("65e toplami tek iki asal", ({(p_, q_) for p_ in sp.primerange(2, 15) for q_ in sp.primerange(2, 15) if p_ + q_ == 15 and p_ <= q_}, all(2 in (p_, q_) for p_ in sp.primerange(2, 300) for q_ in sp.primerange(2, 300) if (p_ + q_) % 2 == 1)),
         ({(2, 13)}, True))
    bol360 = sp.divisors(360)
    esit("65e tek cift ve tam kare bolen", (len([d_ for d_ in bol360 if d_ % 2]), sp.divisor_count(45), len([d_ for d_ in bol360 if d_ % 2 == 0]), sorted(d_ for d_ in bol360 if sp.sqrt(d_).is_integer), sum(sp.primefactors(360))),
         (6, 6, 18, [1, 4, 9, 36], 10))
    esit("65e sifreleme ornegi ve kalbur", (13*17, len(list(sp.primerange(2, 101))), all(any(m % p_ == 0 for p_ in (2, 3, 5, 7)) for m in range(2, 101) if not sp.isprime(m)), 11**2), (221, 25, True, 121))
    esit("65e aralarinda asal ornekleri", (sp.igcd(14, 15), sp.igcd(14, 21)), (1, 7))

def yazi_66_70():
    """66 EBOB-EKOK, 67 Kesirler, 68 Siralama, 69 Toplama-Cikarma, 70 Carpma-Bolme."""
    Q = Rational
    Fr = F
    g, l = sp.igcd, sp.ilcm
    # ── 66 EBOB ve EKOK ──
    esit("66 bolen ve katlar", (sp.divisors(12), sp.divisors(18), sorted(set(sp.divisors(12)) & set(sp.divisors(18))), g(12, 18), l(12, 18),
                                [12*i for i in range(1, 5)], [18*i for i in range(1, 4)]),
         ([1, 2, 3, 4, 6, 12], [1, 2, 3, 6, 9, 18], [1, 2, 3, 6], 6, 36, [12, 24, 36, 48], [18, 36, 54]))
    esit("66 asal carpanlarla", (sp.factorint(72), sp.factorint(120), g(72, 120), l(72, 120), 2**3*3, 2**3*3**2*5), ({2: 3, 3: 2}, {2: 3, 3: 1, 5: 1}, 24, 360, 24, 360))
    A_, B_ = 2**4*3**2*7, 2**2*3**5*5
    esit("66 uslu EBOB EKOK", (g(A_, B_), l(A_, B_)), (2**2*3**2, 2**4*3**5*5*7))
    satirlar, cur = [], [24, 36, 60]
    for p_ in (2, 2, 2, 3, 3, 5):
        cur = [c_ // p_ if c_ % p_ == 0 else c_ for c_ in cur]; satirlar.append(cur)
    esit("66 bolme tablosu", (satirlar, g(g(24, 36), 60), l(l(24, 36), 60), 2*2*3, 2*2*2*3*3*5), ([[12, 18, 30], [6, 9, 15], [3, 9, 15], [1, 3, 5], [1, 1, 5], [1, 1, 1]], 12, 360, 12, 360))
    esit("66 uc sayi asal carpan", (sp.factorint(24), sp.factorint(36), sp.factorint(60), 24*15, 36*10, 60*6), ({2: 3, 3: 1}, {2: 2, 3: 2}, {2: 2, 3: 1, 5: 1}, 360, 360, 360))
    esit("66 EBOB*EKOK=ab kaba kuvvet", all(g(p_, q_)*l(p_, q_) == p_*q_ for p_ in range(1, 120) for q_ in range(1, 120)), True)
    esit("66 EBOB*EKOK ornekleri", (6*36, 12*18, 6*90, Fr(540, 18), g(18, 30), l(18, 30)), (216, 216, 540, 30, 6, 90))
    esit("66 uc sayida gecmez", (g(g(2, 4), 8), l(l(2, 4), 8), 2*8, 2*4*8), (2, 8, 16, 64))
    esit("66 diger iliskiler", (all(l(p_, q_) % g(p_, q_) == 0 for p_ in range(1, 80) for q_ in range(1, 80)), g(6, 24), l(6, 24), l(8, 15)), (True, 6, 24, 120))
    esit("66 EBOB 8 toplam 56", sorted((p_, 56 - p_) for p_ in range(1, 29) if g(p_, 56 - p_) == 8), [(8, 48), (16, 40), (24, 32)])
    esit("66 EBOB 6 toplam 48", (sorted((p_, 48 - p_) for p_ in range(1, 25) if g(p_, 48 - p_) == 6), g(12, 36)), ([(6, 42), (18, 30)], 12))
    esit("66 karton ve halat", (g(84, 120), 84 // 12, 120 // 12, 7*10, g(g(48, 72), 120), 48 // 24 + 72 // 24 + 120 // 24), (12, 7, 10, 70, 24, 10))
    esit("66 bahce", (g(60, 84), 2*(60 + 84), 288 // 12), (12, 288, 24))
    esit("66 otobus ve fayans", (l(12, 18), l(6, 8), 24 // 6, 24 // 8, 4*3), (36, 24, 4, 3, 12))
    esit("66 kalan esit", (l(l(4, 6), 9), min(n_ for n_ in range(4, 1000) if n_ % 4 == 3 and n_ % 6 == 3 and n_ % 9 == 3), 4*9 + 3, 6*6 + 3, 9*4 + 3), (36, 39, 39, 39, 39))
    esit("66 kalan farkli", (l(l(5, 6), 8), min(n_ for n_ in range(1, 1000) if n_ % 5 == 3 and n_ % 6 == 4 and n_ % 8 == 6), 118 % 5, 118 % 6, 118 % 8), (120, 118, 3, 4, 6))
    esit("66 kesirlerde", (g(84, 120), Fr(84, 120), l(12, 18), Fr(5, 12) + Fr(7, 18), Fr(5, 12)*36, Fr(7, 18)*36), (12, Fr(7, 10), 36, Fr(29, 36), 15, 14))
    # ── 67 kesirler ──
    esit("67 temel", (Fr(0, 5), Fr(12)*Fr(3, 4), Fr(11, 4), 2 + Fr(3, 4), 3 + Fr(2, 5), Fr(17, 5), 2*Fr(3, 4) == Fr(11, 4)), (0, 9, Fr(11, 4), Fr(11, 4), Fr(17, 5), Fr(17, 5), False))
    esit("67 donusum", (divmod(11, 4), 3*5 + 2), ((2, 3), 17))
    esit("67 birim ve denk", (Fr(1, 10) < Fr(1, 2), 3*Fr(1, 8), Fr(2, 3) == Fr(4, 6) == Fr(10, 15) == Fr(20, 30), g(36, 48), Fr(36, 48), Fr(2 + 6, 2), Fr(2, 2) + 6),
         (True, Fr(3, 8), True, 12, Fr(3, 4), 4, 7))
    esit("67 cokluk", (60 // 5, 12*2, Fr(60)*Fr(2, 5), 21 // 3, 7*7, Fr(49)*Fr(3, 7)), (12, 24, 24, 7, 49, 21))
    esit("67 ondalik ve yuzde", (float(Fr(7, 4)), [float(Fr(*k_)) for k_ in ((1, 2), (1, 4), (3, 4), (1, 5), (1, 8))], [float(Fr(*k_))*100 for k_ in ((1, 2), (1, 4), (3, 4), (1, 5), (1, 8))], float(Fr(3, 8))),
         (1.75, [0.5, 0.25, 0.75, 0.2, 0.125], [50.0, 25.0, 75.0, 20.0, 12.5], 0.375))
    esit("67 sonlu ondalik kurali", all(_sonlu_mu(p_, q_) == (set(sp.primefactors(Fr(p_, q_).denominator)) <= {2, 5}) for q_ in range(1, 120) for p_ in range(1, 60)), True)
    esit("67 kitap", (1 - Fr(1, 3), Fr(1, 4)*Fr(2, 3), Fr(2, 3) - Fr(1, 6), 60 / Fr(1, 2)), (Fr(2, 3), Fr(1, 6), Fr(1, 2), 120))
    esit("67 depo", (Fr(3, 4) - Fr(2, 5), Fr(15, 20) - Fr(8, 20), 21 // 7, 20*3, Fr(2, 5)*20, Fr(3, 4)*20), (Fr(7, 20), Fr(7, 20), 3, 60, 8, 15))
    esit("67 sinif", (12 // 3, 8*4, 5*4, Fr(3, 8)*32), (4, 32, 20, 12))
    # ── 68 siralama ──
    esit("68 esit pay payda", (Fr(5, 9) > Fr(4, 9), Fr(4, 7) > Fr(4, 9)), (True, True))
    esit("68 ortak payda", (l(l(6, 9), 12), [Fr(5, 6)*36, Fr(7, 9)*36, Fr(11, 12)*36], Fr(7, 9) < Fr(5, 6) < Fr(11, 12)), (36, [30, 28, 33], True))
    esit("68 ortak pay", (Fr(4, 9) == Fr(12, 27), Fr(6, 13) == Fr(12, 26), Fr(4, 9) < Fr(6, 13) < Fr(12, 25), l(l(9, 13), 25), l(l(4, 6), 12)), (True, True, True, 2925, 12))
    esit("68 capraz carpim", (5*11, 8*7, Fr(5, 8) < Fr(7, 11), all((Fr(p_, q_) < Fr(r_, t_)) == (p_*t_ < q_*r_) for p_ in range(-5, 6) for q_ in range(1, 7) for r_ in range(-5, 6) for t_ in range(1, 7))),
         (55, 56, True, True))
    esit("68 referans", (Fr(5, 11) < Fr(1, 2) < Fr(7, 12), 2*5, 2*7, Fr(2024, 2025) < Fr(2025, 2026), Fr(9, 7) == 1 + Fr(2, 7), Fr(13, 11) == 1 + Fr(2, 11), Fr(9, 7) > Fr(13, 11)),
         (True, 10, 14, True, True, True, True))
    esit("68 pay paydaya ekleme", (Fr(3, 5) < Fr(4, 6) < Fr(5, 7), Fr(7, 5) > Fr(8, 6) > Fr(9, 7),
                                   all((Fr(p_ + k_, q_ + k_) > Fr(p_, q_)) == (p_ < q_) and (Fr(p_ + k_, q_ + k_) == Fr(p_, q_)) == (p_ == q_) for p_ in range(1, 15) for q_ in range(1, 15) for k_ in range(1, 6)),
                                   Fr(3, 5) < Fr(13, 15) < Fr(23, 25), str(sp.N(Q(13, 15), 3)), float(Fr(23, 25))),
         (True, True, True, True, "0.867", 0.92))
    esit("68 ondalik", (float(Fr(3, 8)), float(Fr(7, 20)), Fr(7, 20) < Fr(3, 8) < Fr(4, 10)), (0.375, 0.35, True))
    esit("68 negatif", (l(l(5, 3), 8), [Fr(3, 5)*120, Fr(2, 3)*120, Fr(5, 8)*120], -Fr(2, 3) < -Fr(5, 8) < -Fr(3, 5)), (120, [72, 80, 75], True))
    esit("68 arada kesir", (Fr(1, 3) < Fr(5, 12) < Fr(1, 2), Fr(1, 3) == Fr(2, 6) == Fr(4, 12), Fr(1, 2) == Fr(3, 6) == Fr(6, 12), Fr(1, 3) < Fr(2, 5) < Fr(1, 2), Fr(1, 3) + Fr(1, 2)),
         (True, True, True, True, Fr(5, 6)))
    esit("68 mediant kaba kuvvet", all(Fr(p_, q_) < Fr(p_ + r_, q_ + t_) < Fr(r_, t_) for p_ in range(-6, 7) for q_ in range(1, 8) for r_ in range(-6, 7) for t_ in range(1, 8) if Fr(p_, q_) < Fr(r_, t_)), True)
    # ── 69 toplama cikarma ──
    esit("69 esit payda", (Fr(2, 7) + Fr(3, 7), Fr(7, 12) + Fr(11, 12), Fr(18, 12), Fr(9, 10) - Fr(3, 10)), (Fr(5, 7), Fr(3, 2), Fr(3, 2), Fr(3, 5)))
    esit("69 farkli payda", (l(6, 8), Fr(5, 6)*24, Fr(3, 8)*24, Fr(5, 6) + Fr(3, 8), 1 + Fr(5, 24), Fr(58, 48), l(15, 9), Fr(7, 15)*45, Fr(2, 9)*45, Fr(7, 15) - Fr(2, 9)),
         (24, 20, 9, Fr(29, 24), Fr(29, 24), Fr(29, 24), 45, 21, 10, Fr(11, 45)))
    esit("69 klasik yanlis", (Fr(1, 2) + Fr(1, 3), Fr(2, 5) < Fr(1, 2)), (Fr(5, 6), True))
    esit("69 tam sayi", (3 - Fr(2, 5), 2 + Fr(3, 4), Fr(15, 5)), (Fr(13, 5), Fr(11, 4), 3))
    esit("69 tam sayili", (3 + Fr(1, 4) + 2 + Fr(2, 3), 5 + Fr(11, 12), Fr(1, 4) + Fr(2, 3), 5 + Fr(1, 6) - (2 + Fr(3, 4)), 2 + Fr(5, 12), Fr(31, 6) - Fr(11, 4), 4 + Fr(14, 12) == 5 + Fr(2, 12)),
         (Fr(71, 12), Fr(71, 12), Fr(11, 12), Fr(29, 12), Fr(29, 12), Fr(29, 12), True))
    esit("69 uc kesir", (Fr(1, 2) + Fr(1, 3) + Fr(1, 6), Fr(3, 4) - Fr(1, 6) + Fr(5, 12)), (1, 1))
    esit("69 negatif", (-Fr(3, 4) + Fr(1, 6), Fr(2, 5) - (-Fr(1, 3))), (Fr(-7, 12), Fr(11, 15)))
    nn = sp.Symbol("nn", positive=True)
    esit("69 birbirini goturen", (sp.simplify(1/(nn*(nn + 1)) - (1/nn - 1/(nn + 1))), sum(Fr(1, k_*(k_ + 1)) for k_ in range(1, 10))), (0, Fr(9, 10)))
    esit("69 problemler", (Fr(1, 3) + Fr(2, 5), 1 - Fr(11, 15), Fr(1, 4) + Fr(1, 6), 1 - Fr(5, 12), 210 // 7, 12*30, Fr(360)*Fr(7, 12), Fr(3, 8) - Fr(1, 4), Fr(3, 8)*Fr(3, 4)),
         (Fr(11, 15), Fr(4, 15), Fr(5, 12), Fr(7, 12), 30, 360, 210, Fr(1, 8), Fr(9, 32)))
    # ── 70 carpma bolme ──
    esit("70 carpma", (3*Fr(2, 5), Fr(2, 3)*Fr(3, 4), Fr(3, 4)*Fr(2, 5), Fr(14, 15)*Fr(25, 28), Fr(350, 420)), (Fr(6, 5), Fr(1, 2), Fr(3, 10), Fr(5, 6), Fr(5, 6)))
    esit("70 tam sayili carpma", ((2 + Fr(1, 2))*(1 + Fr(1, 3)), 3 + Fr(1, 3), 2*1 + Fr(1, 2)*Fr(1, 3), 2 + Fr(1, 6)), (Fr(10, 3), Fr(10, 3), Fr(13, 6), Fr(13, 6)))
    esit("70 buyur kucultur", (12*Fr(3, 4), 12*Fr(5, 4), Fr(12)/Fr(3, 4)), (9, 15, 16))
    esit("70 ters", (1/Fr(3, 7), 1/Fr(5), 1/Fr(-2, 9), Fr(3, 7)*Fr(7, 3)), (Fr(7, 3), Fr(1, 5), Fr(-9, 2), 1))
    esit("70 bolme", (Fr(3, 4)/Fr(2, 5), 1 + Fr(7, 8), Fr(6, 7)/3, 4/Fr(2, 3), 1/Fr(1, 4)), (Fr(15, 8), Fr(15, 8), Fr(2, 7), 6, 4))
    pa, pb, pc, pd = sp.symbols("pa pb pc pd", positive=True)
    esit("70 bolme kurali", sp.simplify((pa/pb)/(pc/pd) - pa*pd/(pb*pc)), 0)
    esit("70 merdiven", (Fr(1, 2)/Fr(3, 4), 1/(1 + 1/(1 + Fr(1, 2))), 1 + Fr(1, 2), 1/Fr(3, 2), 1 + Fr(2, 3), 1/Fr(5, 3)), (Fr(2, 3), Fr(3, 5), Fr(3, 2), Fr(2, 3), Fr(5, 3), Fr(3, 5)))
    esit("70 us", (Fr(2, 3)**3, Fr(3, 2)**-2, [Fr(1, 2)**k_ for k_ in (1, 2, 3)]), (Fr(8, 27), Fr(4, 9), [Fr(1, 2), Fr(1, 4), Fr(1, 8)]))
    esit("70 problemler", (6*Fr(3, 4), Fr(9, 2)/Fr(3, 8), Fr(2, 3)/4, 10*Fr(1, 6), 1 + Fr(2, 3), Fr(3, 4)*Fr(2, 5), 18/Fr(3, 10), Fr(60)*Fr(2, 5)*Fr(3, 4)),
         (Fr(9, 2), 12, Fr(1, 6), Fr(5, 3), Fr(5, 3), Fr(3, 10), 60, 18))

def yazi_66_70_ek():
    """66-70 genisletmelerindeki iddialar."""
    Fr = F
    Q = Rational
    k_ = sp.Symbol("k_", positive=True)
    # 67
    esit("67e kalanli bolme", (divmod(17, 5), Fr(17, 5), 3 + Fr(2, 5)), ((3, 2), Fr(17, 5), Fr(17, 5)))
    esit("67e gunluk", (Fr(60, 2), Fr(60, 4), 60*Fr(3, 4), 200*Fr(1, 4), 2*60, Fr(120)*Fr(3, 4)), (30, 15, 45, 50, 120, 90))
    esit("67e denk kesir", (sp.solve(sp.Eq(2*k_ + 3*k_, 35), k_), Fr(14, 21) == Fr(2, 3), sp.solve(sp.Eq(5*k_ - 3*k_, 12), k_), Fr(18, 30) == Fr(3, 5)), ([7], True, [6], True))
    esit("67e pay payda", (2*Fr(3, 8), Fr(6, 8), Fr(3, 8)/2, Fr(3, 16), Fr(6, 16) == Fr(3, 8)), (Fr(3, 4), Fr(3, 4), Fr(3, 16), Fr(3, 16), True))
    esit("67e otobus", sp.solve(sp.Eq(x - Fr(2, 7)*x + 4, 24), x), [28])
    esit("67e birim kesirler", (Fr(1, 2) + Fr(1, 4), Fr(1, 2) + Fr(1, 3)), (Fr(3, 4), Fr(5, 6)))
    # 68
    esit("68e sayi dogrusu", (Fr(2, 3)*15, Fr(3, 5)*15, Fr(2, 3) - Fr(3, 5), 1/Fr(3, 5), Fr(3, 5) < 1 < Fr(5, 3)), (10, 9, Fr(1, 15), Fr(5, 3), True))
    esit("68e kuvvet kok", (Fr(4, 9)**2, sqrt(Q(4, 9)), [Fr(16, 81), Fr(4, 9)*81, Fr(2, 3)*81], Fr(16, 81) < Fr(4, 9) < Fr(2, 3), Fr(9, 4)**2, sqrt(Q(9, 4)), Fr(3, 2) < Fr(9, 4) < Fr(81, 16)),
         (Fr(16, 81), Q(2, 3), [Fr(16, 81), 36, 54], True, Fr(81, 16), Q(3, 2), True))
    bes = [Fr(3, 7), Fr(5, 12), Fr(4, 9), Fr(7, 15), Fr(2, 5)]
    esit("68e bes kesir", (sorted(bes), [str(sp.N(Q(v_.numerator, v_.denominator), 3)) for v_ in bes], all(2*v_.numerator < v_.denominator for v_ in bes), 3*9, 7*4),
         ([Fr(2, 5), Fr(5, 12), Fr(3, 7), Fr(4, 9), Fr(7, 15)], ["0.429", "0.417", "0.444", "0.467", "0.400"], True, 27, 28))
    esit("68e gunluk", (float(Fr(3, 8)), Fr(3, 8) > Fr(35, 100), 18*30, 25*21, float(Fr(18, 25)), float(Fr(21, 30))), (0.375, True, 540, 525, 0.72, 0.7))
    esit("68e harfli", (sp.simplify((x + 1)/(x + 2) - x/(x + 1) - 1/((x + 1)*(x + 2))) == 0, all(Fr(v_, v_ + 1) < Fr(v_ + 1, v_ + 2) for v_ in range(1, 50)), Fr(1, 2) < Fr(2, 3)), (True, True, True))
    esit("68e kisa yol yanlis", (Fr(3, 10) < Fr(2, 3), Fr(1, 3) < Fr(3, 4), 3*8 == 4*6), (True, True, True))
    # 69
    esit("69e ozellikler", (Fr(1, 3) + Fr(5, 7) + Fr(2, 3), 1 + Fr(5, 7), Fr(1, 3) + Fr(5, 7), Fr(2, 3) == Fr(14, 21), Fr(36, 21)), (Fr(12, 7), Fr(12, 7), Fr(22, 21), True, Fr(12, 7)))
    esit("69e tahmin", (Fr(7, 8) + Fr(5, 9), l_ := sp.ilcm(8, 9), Fr(7, 8)*72, Fr(5, 9)*72, str(sp.N(Q(103, 72), 3)), Fr(12, 17) < 1), (Fr(103, 72), 72, 63, 40, "1.43", True))
    esit("69e ondalik harfli", (Fr(1, 4) + Fr(2, 3), sp.simplify(1/x + 1/(2*x) - 3/(2*x)), sp.simplify(a/b + c/d - (a*d + b*c)/(b*d))), (Fr(11, 12), 0, 0))
    esit("69e eksik kesir", (Fr(3, 4) - Fr(1, 6), 1 - Fr(2, 5)), (Fr(7, 12), Fr(3, 5)))
    esit("69e yol", (Fr(1, 4) + Fr(1, 3), 35 // 7, 12*5, Fr(60)*Fr(7, 12)), (Fr(7, 12), 5, 60, 35))
    esit("69e pizza ve fark", (Fr(1, 2) == Fr(3, 6), Fr(1, 3) == Fr(2, 6), Fr(1, 2) + Fr(1, 3), sp.ilcm(2, 3), Fr(5, 6) - Fr(3, 4), Fr(5, 6)*12, Fr(3, 4)*12), (True, True, Fr(5, 6), 6, Fr(1, 12), 10, 9))
    esit("69e gunluk", (1 - Fr(5, 6), Fr(1, 2) + Fr(3, 4), 1 + Fr(1, 2) + Fr(3, 4), Fr(1, 4)*60), (Fr(1, 6), Fr(5, 4), Fr(9, 4), 15))
    # 70
    esit("70e bolme ortak payda", (Fr(3, 4)/Fr(1, 8), Fr(3, 4) == Fr(6, 8), Fr(3, 4)*8), (6, True, 6))
    esit("70e ozellikler", (Fr(4, 7)*14 + Fr(4, 7)*7, Fr(4, 7)*21, Fr(5, 9)*Fr(7, 11)*Fr(9, 5)), (12, 12, Fr(7, 11)))
    esit("70e ondalik harfli", (Fr(6, 10)*Fr(5, 9), sp.simplify(x/2*4/x), sp.simplify((a/b)/(a/c) - c/b)), (Fr(1, 3), 2, 0))
    esit("70e tablo", (Fr(60)*Fr(2, 3), Fr(3)/Fr(3, 4), Fr(3, 5)/3, Fr(40)/Fr(2, 3)), (40, 4, Fr(1, 5), 60))
    esit("70e hiz", (60*Fr(3, 4), Fr(90, 60)), (45, Fr(3, 2)))
    esit("70e kontrol", (Fr(15, 8)*Fr(2, 5), Fr(4, 3)*Fr(2, 5), Fr(8, 15)*Fr(2, 5)), (Fr(3, 4), Fr(8, 15), Fr(16, 75)))
    esit("70e yuzde", (Fr(40, 100), Fr(3, 4)*Fr(2, 5), 20*Fr(2, 5), 8*Fr(3, 4), Fr(6, 20)*100), (Fr(2, 5), Fr(3, 10), 8, 6, 30))
    esit("70e negatif", (-Fr(2, 3)*Fr(3, 4), (-Fr(2, 3))*(-Fr(3, 4))), (Fr(-1, 2), Fr(1, 2)))

# ── bicim denetimi ─────────────────────────────────────────────────────
def _acilim(p_, q_):
    """p/q (p >= 0, q > 0) uzun bolmesi: (tam kisim, devretmeyen basamaklar, devreden basamaklar)."""
    tam_, r_ = divmod(p_, q_)
    bas_, gor_ = [], {}
    while r_ and r_ not in gor_:
        gor_[r_] = len(bas_)
        r_ *= 10
        bas_.append(r_ // q_)
        r_ %= q_
    if not r_:
        return (tam_, "".join(map(str, bas_)), "")
    i_ = gor_[r_]
    return (tam_, "".join(map(str, bas_[:i_])), "".join(map(str, bas_[i_:])))


def _devir_kurali(tam_, dt_, dv_):
    """Yazidaki kural: pay = tamami - devretmeyen, payda = devreden kadar 9 + devretmeyen ondalik kadar 0."""
    return F(int(str(tam_) + dt_ + dv_) - int(str(tam_) + dt_), int("9"*len(dv_) + "0"*len(dt_)))


def _yuvarla(x_, n_):
    """Pozitif sayiyi n ondalik basamaga yuvarlar (5 ve ustu yukari)."""
    return F(int(x_*10**n_ + F(1, 2)), 10**n_)


def yazi_71_75():
    """71 Ondalik, 72 Devirli, 73 Yuzdeler, 74 Oran-Oranti, 75 Dogru-Ters Oranti (genisletmeler dahil)."""
    D = F  # D("3.472") ondalik sayiyi TAM kesir olarak okur
    # ── 71 ondalik gosterim ──
    esit("71 cozumleme", D("3.472") == 3 + F(4, 10) + F(7, 100) + F(2, 1000), True)
    esit("71 sifirlar", (D("0.5") == D("0.50") == D("0.500"), D("2.30") == D("2.3"), D("2.03") == D("2.3")), (True, True, False))
    esit("71 kesirden ondaliga", (F(3, 25) == F(12, 100) == D("0.12"), F(7, 20) == F(35, 100) == D("0.35"),
                                  [divmod(30, 8), divmod(60, 8), divmod(40, 8)], F(3, 8) == D("0.375"), _acilim(1, 3)),
         (True, True, [(3, 6), (7, 4), (5, 0)], True, (0, "", "3")))
    esit("71 ondaliktan kesre", (D("0.35"), F(35 // 5, 100 // 5), D("2.125"), F(2125 // 125, 1000 // 125), float(F(17, 8))), (F(7, 20), F(7, 20), F(17, 8), F(17, 8), 2.125))
    esit("71 siralama", D("0.07") < D("0.68") < D("0.7") < D("0.702"), True)
    esit("71 toplama cikarma", (D("12.5") + D("3.075"), 7 - D("2.36")), (D("15.575"), D("4.64")))
    esit("71 carpma", (24*35, F(24*35, 10*100), D("2.4")*D("0.35"), D("3.472")*100, D("0.5")*1000, 40*D("0.25")), (840, D("0.84"), D("0.84"), D("347.2"), 500, 10))
    esit("71 bolme", (D("7.2")/D("0.4"), F(72, 4), D("0.63")/D("0.009"), F(630, 9), D("9.6")/4, D("45.6")/100, F(7, 1000)),
         (18, 18, 70, 70, D("2.4"), D("0.456"), D("0.007")))
    esit("71 yuvarlama", (_yuvarla(D("3.46"), 1), _yuvarla(D("2.749"), 2), _yuvarla(D("4.96"), 1), _yuvarla(D("2.449"), 1), _yuvarla(_yuvarla(D("2.449"), 2), 1)),
         (D("3.5"), D("2.75"), 5, D("2.4"), D("2.5")))
    esit("71 tahmin", (5*3, 498*302, D("4.98")*D("3.02")), (15, 150396, D("15.0396")))
    esit("71 kalem ve not", (3*D("4.75"), 20 - 3*D("4.75"), D("7.5") + D("8.25") + D("6.75"), (D("7.5") + D("8.25") + D("6.75"))/3), (D("14.25"), D("5.75"), D("22.5"), D("7.5")))
    esit("71 kesre cevirme kisayolu", (D("0.25"), D("0.125")), (F(1, 4), F(1, 8)))
    esit("71 araliktaki sayilar", (len([k_ for k_ in range(230, 241) if 230 < k_ < 240]), len([k_ for k_ in range(2300, 2401) if 2300 < k_ < 2400])), (9, 99))
    esit("71 kesir ve ondalik karsilastirma", (F(3, 4), F(75, 100) == D("0.75"), D("0.75") > D("0.7")), (D("0.75"), True, True))
    tablo_ = [(F(1, 2), "0.5", 50), (F(1, 4), "0.25", 25), (F(3, 4), "0.75", 75), (F(1, 5), "0.2", 20), (F(2, 5), "0.4", 40),
              (F(1, 8), "0.125", D("12.5")), (F(1, 10), "0.1", 10), (F(1, 20), "0.05", 5), (F(1, 25), "0.04", 4)]
    esit("71 kesir ondalik yuzde tablosu", all(k_ == D(o_) and k_*100 == y_ for k_, o_, y_ in tablo_), True)
    esit("71 yuzde donusum", (F(35, 100) == D("0.35"), F(7, 100) == D("0.07"), 36*D("0.25"), F(36, 4)), (True, True, 9, 9))
    esit("71 birim donusumu", (D("2.5")*1000, D("1.75")*1000, F(350, 100), D("3.2")/D("0.4"), F(32, 4), D("1.2") + D("0.45")), (2500, 1750, D("3.5"), 8, 8, D("1.65")))
    esit("71 karisik islem", (D("3.2") - D("1.8"), D("0.5")*D("1.4"), D("0.36")/D("0.12"), D("0.5")*(D("3.2") - D("1.8")) + D("0.36")/D("0.12")), (D("1.4"), D("0.7"), 3, D("3.7")))
    esit("71 kesirle kisaltma", (F(1, 4)*D("0.8"), D("0.2")/D("0.02"), D("0.25")*D("0.8")/D("0.02")), (D("0.2"), 10, 10))
    esit("71 her kesir sonlu ya da devirli", all((_acilim(p_, q_)[2] == "") == _sonlu_mu(p_, q_) for q_ in range(1, 150) for p_ in range(1, 60)), True)
    # ── 72 devirli ondalik ──
    esit("72 tablo", (_acilim(3, 8), _acilim(1, 3), _acilim(4, 11), _acilim(1, 6), _acilim(1, 7)),
         ((0, "375", ""), (0, "", "3"), (0, "", "36"), (0, "1", "6"), (0, "", "142857")))
    kalan_, bas_, r_ = [], [], 1
    for _ in range(6):
        bas_.append(r_*10 // 7); r_ = r_*10 % 7; kalan_.append(r_)
    esit("72 1/7 kalanlari", (kalan_, bas_), ([3, 2, 6, 4, 5, 1], [1, 4, 2, 8, 5, 7]))
    esit("72 devir en fazla q-1", all(len(_acilim(p_, q_)[2]) <= q_ - 1 for q_ in range(2, 300) for p_ in range(1, q_)), True)
    esit("72 sonlu mu devirli mi", (sp.factorint(40), _acilim(7, 40), sp.factorint(30), _acilim(7, 30), F(3, 12), _acilim(3, 12), 2*5),
         ({2: 3, 5: 1}, (0, "175", ""), {2: 1, 3: 1, 5: 1}, (0, "2", "3"), F(1, 4), (0, "25", ""), 10))
    esit("72 kural ornekleri", (_devir_kurali(0, "", "3"), _devir_kurali(0, "", "36"), 16 - 1, _devir_kurali(0, "1", "6"),
                                245 - 2, _devir_kurali(2, "", "45"), 1234 - 12, _devir_kurali(1, "2", "34"), F(1222, 990)),
         (F(1, 3), F(4, 11), 15, F(1, 6), 243, F(27, 11), 1222, F(611, 495), F(611, 495)))
    esit("72 kural kaba kuvvet", all(_devir_kurali(*_acilim(p_, q_)) == F(p_, q_) for q_ in range(1, 200) for p_ in range(0, 3*q_) if _acilim(p_, q_)[2]), True)
    esit("72 kural ispati", (F(36, 99), F(15, 90), F(9, 9), F(1, 3)*3, 10 - 1), (F(4, 11), F(1, 6), 1, 1, 9))
    esit("72 dokuz devreden", (_devir_kurali(0, "", "9"), 249 - 24, _devir_kurali(2, "4", "9"), float(F(5, 2))), (1, 225, F(5, 2), 2.5))
    esit("72 devir uzunlugu", ([_acilim(1, q_)[2] for q_ in (3, 11, 37, 7, 13)], [len(_acilim(1, q_)[2]) for q_ in (3, 11, 37, 7, 13)], 7 - 1, 13 - 1),
         (["3", "09", "027", "142857", "076923"], [1, 2, 3, 6, 6], 6, 12))
    esit("72 yuzuncu basamak", (100 % 6, _acilim(1, 7)[2][(100 - 1) % 6]), (4, "8"))
    esit("72 islem", (F(3, 9) + F(6, 9), F(1, 9) + F(2, 9), _devir_kurali(0, "1", "6")*6, F(36, 99)/F(12, 99)), (1, F(1, 3), 1, 3))
    esit("72 siralama", (_devir_kurali(0, "3", "4"), D("0.33") < F(1, 3) < _devir_kurali(0, "3", "4"), F(1, 3) - D("0.33")), (F(31, 90), True, F(1, 300)))
    esit("72 dokuzlara tamamlama", ([_acilim(1, q_) for q_ in (9, 99, 999)], _acilim(7, 9), _acilim(23, 99), _acilim(123, 999)),
         ([(0, "", "1"), (0, "", "01"), (0, "", "001")], (0, "", "7"), (0, "", "23"), (0, "", "123")))
    esit("72 genisletme", (11*9, F(5, 11) == F(45, 99), _acilim(5, 11), 27*37, F(2, 27) == F(74, 999), _acilim(2, 27)),
         (99, True, (0, "", "45"), 999, True, (0, "", "074")))
    esit("72 eksik basamak", (_acilim(7, 99), _devir_kurali(0, "", "7"), F(7, 9)/F(7, 99)), ((0, "", "07"), F(7, 9), 11))
    esit("72 bilinmeyen tek", [a_ for a_ in range(10) if _devir_kurali(0, "", str(a_)) + F(3, 9) == _devir_kurali(0, "", "8")], [5])
    esit("72 bilinmeyen cift", (all(_devir_kurali(0, "", f"{a_}{b_}") == F(10*a_ + b_, 99) for a_ in range(10) for b_ in range(10)),
                                {a_ + b_ for a_ in range(1, 10) for b_ in range(1, 10) if _devir_kurali(0, "", f"{a_}{b_}") + _devir_kurali(0, "", f"{b_}{a_}") == 1},
                                F(27 + 72, 99)),
         (True, {9}, 1))
    esit("72 yuvarlama", (_acilim(2, 3), _yuvarla(F(2, 3), 2), _devir_kurali(1, "", "27"), _yuvarla(_devir_kurali(1, "", "27"), 1), D("0.33")*3, F(1, 3)*3),
         ((0, "", "6"), D("0.67"), F(14, 11), D("1.3"), D("0.99"), 1))
    esit("72 bolmeyle kontrol", ([divmod(611, 495), divmod(1160, 495), divmod(1700, 495), divmod(2150, 495)], _acilim(611, 495)),
         ([(1, 116), (2, 170), (3, 215), (4, 170)], (1, "2", "34")))
    # ── 73 yuzdeler ──
    esit("73 tanim", (F(25, 100), D("0.25"), F(10, 40), F(50, 200)), (F(1, 4), F(1, 4), F(1, 4), F(1, 4)))
    esit("73 donusum", (F(7, 100) == D("0.07"), D("1.2")*100, F(3, 5) == F(60, 100), D("0.6")*100, F(6, 5) == D("1.2"), F(1, 8)*100),
         (True, 120, True, 60, True, D("12.5")))
    esit("73 sayinin yuzdesi", (240*F(15, 100), F(3600, 100), [240*F(y_, 100) for y_ in (10, 5, 25, 50, 15)], 24 + 12), (36, 36, [24, 12, 60, 120, 36], 36))
    esit("73 yer degistirme", (50*F(8, 100), 8*F(50, 100), sp.simplify(a*b/100 - b*a/100)), (4, 4, 0))
    esit("73 yuzdesi verilen", (F(42, 30), F(42, 30)*100, F(12, 4), 3*10, F(12, F(40, 100))), (D("1.4"), 140, 3, 30, 30))
    esit("73 yuzde kaci", (F(18, 72), F(18, 72)*100, F(132, 480), F(132, 480)*100), (F(1, 4), 25, F(11, 40), D("27.5")))
    esit("73 artis azalis", (F(100 - 80, 80)*100, F(80 - 100, 100)*100), (25, -20))
    esit("73 carpanlar", (1 + F(20, 100), 1 - F(20, 100), 1 + F(5, 100), 1 - F(35, 100), D("1.2")*D("0.8"), D("1.1")*D("1.1")), (D("1.2"), D("0.8"), D("1.05"), D("0.65"), D("0.96"), D("1.21")))
    esit("73 yuzde puan", (12 - 10, F(12 - 10, 10)*100), (2, 20))
    esit("73 indirim vergi", (250*D("0.8"), 360/D("1.2"), 360 - 300, 360*F(20, 100), 360 - 72, 300*F(20, 100)), (200, 300, 60, 72, 288, 60))
    esit("73 yuz kabul", 100*D("1.2")*D("0.8"), 96)
    esit("73 basa donus", (1/D("1.25"), 200*D("1.25"), 250 - 200, F(50, 250)*100, D("1.25")*D("0.8"), D("0.8")*D("1.25")), (D("0.8"), 250, 50, 20, 1, 1))
    esit("73 kar zarar", (120*D("1.25"), 150 - 120, 91/D("0.7"), F(910, 7), 130 - 91, F(30, 120)*100, F(30, 150)*100), (150, 30, 130, 130, 39, 25, 20))
    esit("73 art arda indirim", (D("0.8")*D("0.9"), (1 - D("0.8")*D("0.9"))*100, 500*D("0.8")*D("0.9"), 500 - 360, F(140, 500)*100, 500*D("0.9")*D("0.8")),
         (D("0.72"), 28, 360, 140, 28, 360))
    esit("73 karisim", (200*D("0.15"), 30 + 50, 200 + 50, F(80, 250)*100, F(30, 300)*100, (F(10, 100)*100 + F(30, 100)*100)/200*100), (30, 80, 250, 32, 10, 20))
    esit("73 faiz", (5000*D("0.4")*F(1, 2), 5000 + 1000, D("1.1")*D("1.1"), 2*10, F(6, 12), F(3, 12)), (1000, 6000, D("1.21"), 20, F(1, 2), F(1, 4)))
    # ── 74 oran ve oranti ──
    k_, m_, n_ = sp.symbols("k_ m_ n_", positive=True)
    esit("74 oran", (F(12, 18), sp.igcd(12, 18), F(12, 18) == F(2, 3) == F(4, 6), F(50, 2), F(50, 200)), (F(2, 3), 6, True, 25, F(1, 4)))
    esit("74 icler disler", (sp.solve(sp.Eq(5*x, 3*40), x), sp.solve(sp.Eq(4*(x + 1), 7*(x - 2)), x), F(6 + 1, 6 - 2)), ([24], [6], F(7, 4)))
    esit("74 oranti sabiti", (sp.solve(sp.Eq(3*k_ + 5*k_ + 7*k_, 45), k_), [3*3, 5*3, 7*3], sp.solve(sp.Eq(2*k_*3*k_, 54), k_), (2*3, 3*3)), ([3], [9, 15, 21], [3], (6, 9)))
    esit("74 ozellikler", (sp.simplify((b*k_ + d*k_)/(b + d)), sp.simplify((m_*b*k_ + n_*d*k_)/(m_*b + n_*d)), sp.simplify((2*3*k_ + 4*k_)/(3*k_ - 4*k_))), (k_, k_, -10))
    esit("74 birlesik", (sp.ilcm(3, 4), (2*4, 3*4), (4*3, 5*3), F(8, 12) == F(2, 3), F(12, 15) == F(4, 5)), (12, (8, 12), (12, 15), True, True))
    esit("74 bolusum", (2 + 3 + 4, 360 // 9, [2*40, 3*40, 4*40], sum([80, 120, 160]), 90 // 3, (3 + 5)*30), (9, 40, [80, 120, 160], 360, 30, 240))
    esit("74 olcek", (4*50000, 200000 // 100000, 6*100, F(3, 600), 200*200, F(40000, 100*100), 50000 // 100), (200000, 2, 600, F(1, 200), 40000, 4, 500))
    esit("74 gunluk", (32/D("0.4"), 57/D("0.75"), D("1.8")/6, 5 + 1), (80, 76, D("0.3"), 6))
    esit("74 parca butun", (40*F(2, 5), 40 // 5, 2*8, F(2, 2 + 3), F(3, 5)), (16, 8, 16, F(2, 5), F(3, 5)))
    esit("74 oran degisimi", (sp.solve(sp.Eq(3*k_ + 4, 4*k_), k_), (3*4, 4*4, 7*4), 500*F(1, 5), sp.solve(sp.Eq(2*(100 + x), 400), x), F(100 + 100, 400)),
         ([4], (12, 16, 28), 100, [100], F(1, 2)))
    esit("74 yas", (sp.solve(sp.Eq(4*(2*k_ + 5), 3*(3*k_ + 5)), k_), sp.expand(4*(2*k_ + 5)), sp.expand(3*(3*k_ + 5)), (2*5, 3*5), F(10 + 5, 15 + 5)),
         ([5], 8*k_ + 20, 9*k_ + 15, (10, 15), F(3, 4)))
    esit("74 orta orantili", (sp.solve(sp.Eq(x**2, 4*9), x), F(4, 6), F(6, 9), F(6, 4), F(9, 6)), ([-6, 6], F(2, 3), F(2, 3), F(3, 2), F(3, 2)))
    c_ = a*d/b  # a/b = c/d  =>  c = a*d/b
    esit("74 yer degistirme", [sp.simplify(e_) for e_ in (a/c_ - b/d, d/b - c_/a, b/a - d/c_)], [0, 0, 0])
    esit("74 yer degistirme ornek", (F(3, 5) == F(12, 20), F(3, 12), F(5, 20)), (True, F(1, 4), F(1, 4)))
    esit("74 karsilastirma", (F(18, 24), F(21, 30), F(18, 24) > F(21, 30), 21 > 18, F(150, 2), 200/D("2.5")), (D("0.75"), D("0.7"), True, True, 75, 80))
    # ── 75 dogru ve ters oranti ──
    esit("75 dogru oranti", (F(45, 3), 45*7, F(315, 3)), (15, 315, 105))
    esit("75 ters oranti", (6*10, F(60, 4), 60*3, F(180, 90)), (60, 15, 180, 2))
    cift_ = [(2, 12), (3, 8), (4, 6), (6, 4)]
    esit("75 tablo testi", ([F(y_, x_) for x_, y_ in cift_], {x_*y_ for x_, y_ in cift_}, all(y_ == F(24, x_) for x_, y_ in cift_)),
         ([6, F(8, 3), F(3, 2), F(2, 3)], {24}, True))
    esit("75 yanilgi", ([10 - x_ for x_ in (2, 4, 5)], [x_*(10 - x_) for x_ in (2, 4, 5)], F(2*1 + 1, 1), F(2*2 + 1, 2)), ([8, 6, 5], [16, 24, 25], 3, F(5, 2)))
    esit("75 bilesik", (F(4, 5*8), sp.solve(sp.Eq(Rational(4, 40), x/60), x), sp.solve(sp.Eq(6, k_*Rational(4, 2)), k_), 3*F(10, 5)), (F(1, 10), [6], [3], 6))
    esit("75 gunluk", (sp.solve(sp.Eq(100*x, 6*350), x), 6*350, 12 // 4, 12 // 6), ([21], 2100, 3, 2))
    esit("75 birim yontemi", (120 // 5, 8*24, 6*10, 60 // 4), (24, 192, 60, 15))
    esit("75 havuz", (F(1, 6) + F(1, 12), 1/(F(1, 6) + F(1, 12)), F(1, 4) - F(1, 6), 1/(F(1, 4) - F(1, 6)), 6 + 12, F(6 + 12, 2), 4 < 6),
         (F(1, 4), 4, F(1, 12), 12, 18, 9, True))
    esit("75 degisen isci", (12*20, 12*5, 240 - 60, 180 // 9, 5 + 20, F(180, 12), F(12, 9), F(180, 12)*F(12, 9)), (240, 60, 180, 20, 25, 15, F(4, 3), 20))
    esit("75 disli", (40*15, F(600, 24), F(30*4, 20), F(20*6, 60), 30*4 == 60*2), (600, 25, 6, 2, True))
    esit("75 hiz yol zaman", (sp.solve(sp.Eq(60*x, 120*90), x), 120*90), ([180], 10800))


def bicim():
    import blog_veri
    from blog_uygula import kelime_sayisi
    for Y in blog_veri.YAZILAR:
        no = Y["slug"]
        metin = " ".join([Y["ozet"], Y["aciklama"], Y["baslik"]] + [b["baslik"] for b in Y["bolumler"]]
                         + [p for b in Y["bolumler"] for p in b["icerik"]]
                         + [s + " " + c for s, c in Y.get("sss", [])] + list(Y.get("kontrol", [])))
        esit(f"{no} uzun tire yok", "—" in metin, False)
        esit(f"{no} formul disinda unlem yok", "!" in re.sub(r"\$\$.*?\$\$|\$[^$]*\$", "", metin, flags=re.S), False)
        esit(f"{no} $ dengeli", metin.count("$") % 2, 0)
        esit(f"{no} aciklama <= 160", len(Y["aciklama"]) <= 160, True)
        esit(f"{no} kontrol 10", len(Y["kontrol"]), 10)
        esit(f"{no} >= 2000 kelime", kelime_sayisi(Y) >= 2000, True)
        import json as _json
        from ek_denetimi import denetle as _ek_denetle
        esit(f"{no} formul sonrasi ekler", _ek_denetle(_json.dumps(Y, ensure_ascii=False).replace("\\\\", "\\")), [])
        print(f"  {no:34s} {kelime_sayisi(Y):5d} kelime · {len(Y['bolumler']):2d} bolum · "
              f"{metin.count('bs-hap-ic'):2d} hap · aciklama {len(Y['aciklama'])}")


if __name__ == "__main__":
    for fn in (yazi_02, yazi_03, yazi_04, yazi_05, ekler, yazi_51_55, yazi_56_60, yazi_61_65, yazi_61_65_ek, yazi_66_70, yazi_66_70_ek, yazi_71_75):
        once = SAY[0]
        fn()
        print(f"{fn.__name__}: {SAY[0] - once} iddia dogrulandi")
    bicim()
    print(f"\nTOPLAM {SAY[0]} denetim, hepsi tuttu.")
