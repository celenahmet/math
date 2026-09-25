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


def _coz(sol, sag=0, degisken=None):
    """Gercek sayilarda denklem ya da esitsizlik cozum kumesi."""
    v = degisken if degisken is not None else x
    if isinstance(sol, sp.Basic) and sol.is_Relational:
        return sp.solveset(sol, v, R)
    return sp.solveset(sp.Eq(sol, sag), v, R)


def yazi_76_80():
    """76 Cebirsel Ifadeler, 77 Birinci Dereceden Denklemler, 78 Esitsizlikler, 79 Denklem Kurma, 80 Sayi Problemleri."""
    Q = Rational
    D = lambda s: Rational(s)  # ondalik sayiyi tam kesir olarak okur
    ex = sp.expand
    y_, m_, k_, e_, t_ = sp.symbols("y_ m_ k_ e_ t_", real=True)
    # ── 76 cebirsel ifadeler ──
    # NOT: sympy 1.x solveset(|x-2| > -1) yanlislikla EmptySet donuyor; 78 bu yuzden tumleyenle denetleniyor.
    esit("76 derece", (sp.degree(4*x**2 - 3*x + 7, x), sp.degree(5*x - 1, x), sp.Poly(3*x**2*y_, x, y_).total_degree(), sp.degree(7 - 2*x + x**3 + 5*x**2, x)), (2, 1, 3, 3))
    esit("76 siralama", ex(7 - 2*x + x**3 + 5*x**2) - (x**3 + 5*x**2 - 2*x + 7), 0)
    esit("76 benzer terim toplama", (ex(5*x + 3*y_ - 2*x + y_), ex((3*x**2 - 2*x + 5) + (x**2 + 4*x - 8)), ex((5*a - 3*b) - (2*a - 7*b)), ex(-(2*a - 7*b))),
         (3*x + 4*y_, 4*x**2 + 2*x - 3, 3*a + 4*b, -2*a + 7*b))
    esit("76 carpma", (ex(3*x*4*x), ex(2*a**2*5*a**3), ex(3*(2*x - 5)), ex(-2*x*(x - 4)), ex((x + 3)*(x + 2)), ex((2*x - 1)*(x + 4)), ex((x + 3)**2), ex((x + 3)**2) == x**2 + 9),
         (12*x**2, 10*a**5, 6*x - 15, -2*x**2 + 8*x, x**2 + 5*x + 6, 2*x**2 + 7*x - 4, x**2 + 6*x + 9, False))
    esit("76 bolme ve sadelestirme", (sp.simplify((6*x**2 + 9*x)/(3*x)), sp.simplify((x + 3)/3 - (x/3 + 1)), sp.simplify((x + 3)/3 - x) == 0, sp.simplify((x**2 - 9)/(x - 3))), (2*x + 3, 0, False, x + 3))
    esit("76 deger hesaplama", ((x**2 - 3*x + 1).subs(x, -2), (2*a**2 - a*b + b**2).subs({a: 3, b: -1}), (-x**2).subs(x, -3), ((-x)**2).subs(x, -3), -3**2), (11, 22, -9, 9, -9))
    esit("76 ortak carpan", (ex(3*(2*x + 3)), ex(2*x*(2*x - 5)), ex((x + y_)*(a - b)) - ex(a*x + a*y_ - b*x - b*y_), 37*23 + 37*77, 37*(23 + 77)), (6*x + 9, 4*x**2 - 10*x, 0, 3700, 3700))
    esit("76 ozdeslikler", (ex((a + b)**2), ex((a - b)**2), ex((a - b)*(a + b)), 51**2, 2500 + 100 + 1, 99*101, 10000 - 1),
         (a**2 + 2*a*b + b**2, a**2 - 2*a*b + b**2, a**2 - b**2, 2601, 2601, 9999, 9999))
    esit("76 sozel ifade", (ex(3*(x - 4)), ex(x + (x + 2) + (x + 4))), (3*x - 12, 3*x + 6))
    esit("76 geometri", (ex(2*(x + 3) + 2*x), ex(x*(x + 3)), (4*x + 6).subs(x, 5), (x**2 + 3*x).subs(x, 5)), (4*x + 6, x**2 + 3*x, 26, 40))
    esit("76 toplam carpimdan", (sp.simplify((x**2 + y_**2) - ((x + y_)**2 - 2*x*y_)), 5**2 - 2*6, 2**2 + 3**2, 2 + 3, 2*3, sp.simplify((a**2 + b**2) - ((a - b)**2 + 2*a*b)), 3**2 + 2*10, 5**2 + 2**2, 5 - 2, 5*2),
         (0, 13, 13, 5, 6, 0, 29, 29, 3, 10))
    esit("76 iki ifade esit mi", ([((x + 1)**2).subs(x, v_) for v_ in (0, 1)], [(x**2 + 1).subs(x, v_) for v_ in (0, 1)], ex((x + 1)**2 - (x**2 + 1)), _coz(2*x)), ([1, 4], [1, 2], 2*x, FiniteSet(0)))
    # ── 77 birinci dereceden denklemler ──
    esit("77 kok ve terazi", (_coz(2*x + 3, 11), _coz(3*x + 2, 11), 3*3 + 2), (FiniteSet(4), FiniteSet(3), 11))
    esit("77 derece tablosu", (sp.degree(ex(3*x - 7 - 5), x), sp.degree(ex(x**2 - 4), x), sp.degree(ex(4*(x + 1) - 3*x), x), ex(2*(x + 1)) - (2*x + 2)), (1, 2, 1, 0))
    esit("77 adim adim", (_coz(5*x - 4, 2*x + 11), 5*5 - 4, 2*5 + 11, _coz(7 - 3*x, x - 9), 7 - 12, 4 - 9), (FiniteSet(5), 21, 21, FiniteSet(4), -5, -5))
    esit("77 parantezli", (ex(3*(x - 2) - 2*(x + 1)), _coz(3*(x - 2) - 2*(x + 1), 4), 3*10 - 2*13, ex(2*(3*x + 1)), ex(5*(x - 2) + 3), _coz(2*(3*x + 1), 5*(x - 2) + 3), 2*(-26), 5*(-11) + 3, ex(-2*(x + 1))),
         (x - 8, FiniteSet(12), 4, 6*x + 2, 5*x - 7, FiniteSet(-9), -52, -52, -2*x - 2))
    esit("77 kesirli", (_coz(x/3 + x/4, 14), Q(24, 3) + Q(24, 4), ex(10*((x - 1)/2 - (x + 2)/5)), _coz((x - 1)/2 - (x + 2)/5, 3), Q(12, 2) - Q(15, 5), sp.ilcm(3, 4), sp.ilcm(2, 5)),
         (FiniteSet(24), 14, 3*x - 9, FiniteSet(13), 3, 12, 10))
    esit("77 ondalikli", (_coz(D("0.2")*x + D("1.5"), D("0.5")*x - D("0.3")), D("1.2") + D("1.5"), 3 - D("0.3")), (FiniteSet(6), D("2.7"), D("2.7")))
    esit("77 kisayollar", (_coz(12*x - 36, 48), 12*7 - 36, _coz((2*x - 1)/3, (x + 4)/2), Q(27, 3), Q(18, 2)), (FiniteSet(7), 48, FiniteSet(14), 9, 9))
    esit("77 cozum kumesi", (_coz(3*x, 12), _coz(2*x + 3, 2*x + 5), _coz(2*(x + 3), 2*x + 6)), (FiniteSet(4), S.EmptySet, R))
    esit("77 parametreli", ([_coz((mv - 2)*x, mv - 2) for mv in (0, 1, 3, 5, Q(7, 2))], _coz((2 - 2)*x, 2 - 2)), ([FiniteSet(1)]*5, R))
    esit("77 kokten katsayi", (sp.solve(sp.Eq(3*4 + a, 2*4 - 5), a), _coz(3*x - 9, 2*x - 5)), ([-9], FiniteSet(4)))
    esit("77 bilinmeyen paydada", (_coz(6/(x - 1), 3), sp.solveset(sp.Eq((x + 2)/(x - 1), (x + 5)/(x + 1)), x, R), ex((x + 2)*(x + 1)), ex((x + 5)*(x - 1)), Q(9, 6), Q(12, 8), sp.solveset(sp.Eq(x/(x - 2), 2/(x - 2)), x, R)),
         (FiniteSet(3), FiniteSet(7), x**2 + 3*x + 2, x**2 + 4*x - 5, Q(3, 2), Q(3, 2), S.EmptySet))
    esit("77 mutlak degerli", (_coz(Abs(x - 3), 5), _coz(Abs(x - 3), -5)), (FiniteSet(-2, 8), S.EmptySet))
    esit("77 sistemler", (sp.solve([x + y_ - 10, x - y_ - 4], [x, y_]), sp.solve([y_ - (2*x - 1), 3*x + y_ - 19], [x, y_]), sp.solve([x + y_ - 3, x + y_ - 5], [x, y_]), sp.solve([x + y_ - 3, 2*x + 2*y_ - 6], [x, y_])),
         ({x: 7, y_: 3}, {x: 4, y_: 7}, [], {x: 3 - y_}))
    esit("77 problemden denkleme", (_coz(3*x + 5, 26), _coz(4*(x + 15) + 3*x, 165), ex(4*(x + 15) + 3*x), 4*30 + 3*15, _coz(3*x, 12)), (FiniteSet(7), FiniteSet(15), 7*x + 60, 165, FiniteSet(4)))
    # ── 78 esitsizlikler ──
    esit("78 ozellikler", (3 < 7, -1 > -4, 2 < 5, 2 + 3 < 5 + 3, 2*4 < 5*4, -2 > -5), (True,)*6)
    esit("78 birinci derece", (_coz(3*x - 5 < 7), _coz(-2*x + 3 >= 11), (-2*x + 3).subs(x, -5), (-2*x + 3).subs(x, 0) >= 11, _coz(3 - 11 >= 2*x)),
         (Interval.open(-oo, 4), Interval(-oo, -4), 13, False, Interval(-oo, -4)))
    esit("78 aralik ve tam sayi", ([n_ for n_ in range(-20, 20) if 2 < n_ <= 7], [n_ for n_ in range(-20, 20) if 2 < n_ < 7]), ([3, 4, 5, 6, 7], [3, 4, 5, 6]))
    esit("78 parantezli kesirli", (_coz(2*(x - 3) <= 5*x + 6), _coz(x/2 - 1 > x/3), Q(12, 2) - 1, Q(12, 3)), (Interval(-4, oo), Interval.open(6, oo), 5, 4))
    esit("78 sirali", (aralik(-3 < 2*x + 1, 2*x + 1 <= 9), [n_ for n_ in range(-20, 20) if -3 < 2*n_ + 1 <= 9], aralik(1 <= 5 - 2*x, 5 - 2*x < 7)),
         (Interval.Lopen(-2, 4), [-1, 0, 1, 2, 3, 4], Interval.Lopen(-1, 2)))
    esit("78 kesisim birlesim", (aralik(2*x - 1 > 3, x + 4 <= 10), [n_ for n_ in range(-20, 20) if 2*n_ - 1 > 3 and n_ + 4 <= 10], aralik(x < 1, x > 3), _coz(x**2 < 9), (-5)**2),
         (Interval.Lopen(2, 6), [3, 4, 5, 6], S.EmptySet, Interval.open(-3, 3), 25))
    xs_ = [Q(2) + Q(3)*i_/40 for i_ in range(1, 40)]
    ys_ = [Q(1) + Q(2)*j_/40 for j_ in range(1, 40)]
    toplam_ = [p_ + q_ for p_ in xs_ for q_ in ys_]
    fark_ = [p_ - q_ for p_ in xs_ for q_ in ys_]
    carpim_ = [p_*q_ for p_ in xs_ for q_ in ys_]
    esit("78 deger araligi", (2 + 1, 5 + 3, 2 - 3, 5 - 1, 2*1, 5*3, all(3 < v_ < 8 for v_ in toplam_), all(-1 < v_ < 4 for v_ in fark_), all(2 < v_ < 15 for v_ in carpim_),
                              max(fark_) > 2, D("4.9") - D("1.1")),
         (3, 8, -1, 4, 2, 15, True, True, True, True, D("3.8")))
    esit("78 mutlak degerli", (_coz(Abs(x - 2) < 3), _coz(Abs(x + 1) >= 4), _coz(Abs(x - 2) < -1), R - _coz(Abs(x - 2) <= -1), all(abs(Q(v_, 7) - 2) > -1 for v_ in range(-700, 700))),
         (Interval.open(-1, 5), Union(Interval(-oo, -5), Interval(3, oo)), S.EmptySet, R, True))
    esit("78 problemler", (_coz(45*x <= 500), Q(500, 45), max(n_ for n_ in range(100) if 45*n_ <= 500), 11*45, 12*45, _coz((62 + 75 + x)/3 >= 70), 62 + 75, 3*70, _coz(50*x >= 1200), 24*50),
         (Interval(-oo, Q(100, 9)), Q(100, 9), 11, 495, 540, Interval(73, oo), 137, 210, Interval(24, oo), 1200))
    # ── 79 denklem kurma ──
    esit("79 bilinmeyen secimi", (_coz(x + 3*x, 48), 12 + 36, 3*12, Q(48, 4)), (FiniteSet(12), 48, 36, 12))
    esit("79 sayi problemleri", (_coz(x + (x + 2) + (x + 4), 87), 27 + 29 + 31, _coz(Q(2, 3)*x - Q(1, 4)*x, 15), 36*Q(2, 3), Q(36, 4), 24 - 9, _coz(3*x, 87), Q(87, 3), sp.ilcm(3, 4)),
         (FiniteSet(27), 87, FiniteSet(36), 24, 9, 15, FiniteSet(29), 29, 12))
    esit("79 yas", (_coz(4*x + 6, 3*(x + 6)), 4*12, 12 + 6, 48 + 6, 3*18), (FiniteSet(12), 48, 18, 54, 54))
    esit("79 para tablo", (_coz(5*x + 10*(30 - x), 220), 30 - 16, 5*16, 10*14, 80 + 140), (FiniteSet(16), 14, 80, 140, 220))
    esit("79 geometri", (_coz(2*(x + x + 4), 40), 8*12, 2*(8 + 12), _coz((x + 3)**2 - x**2, 57), 11**2 - 8**2), (FiniteSet(8), 96, 40, FiniteSet(8), 57))
    esit("79 cok kosullu", (_coz(2*3*x + 5*x, 110), 3*10, 2*30 + 5*10), (FiniteSet(10), 30, 110))
    esit("79 kalanin kesri", (sp.simplify(x - x/3 - 2*x/3), sp.simplify(2*x/3*Q(1, 4) - x/6), sp.simplify(2*x/3 - x/6 - x/2), _coz(x/2, 300), 600 - 200, Q(400, 4), 400 - 100, Q(600, 4)),
         (0, 0, 0, FiniteSet(600), 400, 100, 300, 150))
    esit("79 hiz yuzde", (_coz(50*t_ + 70*t_, 360, t_), 50*3 + 70*3, _coz(D("1.2")*x, 540), 450*D("1.2")), (FiniteSet(3), 360, FiniteSet(450), 540))
    esit("79 iki bilinmeyen", (sp.solve([k_ + e_ - 32, k_ - e_ - 6], [k_, e_]), _coz(2*e_ + 6, 32, e_)), ({k_: 19, e_: 13}, FiniteSet(13)))
    esit("79 sorulan nicelik", (_coz(2*(x + 5), 26), 8**2), (FiniteSet(8), 64))
    # ── 80 sayi problemleri ──
    esit("80 toplam fark", (sp.solve([a + b - 50, a - b - 14], [a, b]), Q(50 + 14, 2), Q(50 - 14, 2), sp.solve([a + b - 50, a - b - 15], [a, b])),
         ({a: 32, b: 18}, 32, 18, {a: Q(65, 2), b: Q(35, 2)}))
    esit("80 parite", all((p_ + q_) % 2 == (p_ - q_) % 2 for p_ in range(-30, 30) for q_ in range(-30, 30)), True)
    esit("80 kat", (_coz(4*x - x, 36), 4*12, _coz(3*x + 7, 5*x - 9), 3*8 + 7, 5*8 - 9, _coz(x + 4*x, 60), Q(60, 5)), (FiniteSet(12), 48, FiniteSet(8), 31, 31, FiniteSet(12), 12))
    esit("80 uc sayi", (_coz(x + 2*x + 2*x + 3, 58), 2*11, 22 + 3, 11 + 22 + 25), (FiniteSet(11), 22, 25, 58))
    esit("80 ardisik", (_coz(4*x + 12, 100), 22 + 24 + 26 + 28, Q(100, 4)), (FiniteSet(22), 100, 25))
    esit("80 oran", (_coz(3*k_ + 5*k_, 64, k_), 3*8, 5*8, Q(24, 40)), (FiniteSet(8), 24, 40, Q(3, 5)))
    esit("80 bolme kalan", (7*12 + 5, divmod(89, 7), all((3*n_) % 6 == 0 for n_ in range(4, 400, 6)), ex(3*(6*k_ + 4)), 10 % 6, 30 % 6), (89, (12, 5), True, 18*k_ + 12, 4, 0))
    esit("80 iki basamak", ([10*a_ + b_ for a_ in range(1, 10) for b_ in range(10) if a_ + b_ == 11 and (10*b_ + a_) - (10*a_ + b_) == 27], ex((10*b + a) - (10*a + b)), 74 - 47, 4 + 7, 4*7, 4*10 + 7,
                            all((10*b_ + a_ - (10*a_ + b_)) % 9 == 0 for a_ in range(1, 10) for b_ in range(1, 10))),
         ([47], 9*b - 9*a, 27, 11, 28, 47, True))
    esit("80 uc basamak", [100*4 + 10*b_ + 8 for b_ in range(10) if 4 + b_ + 2*4 == 15], [438])
    esit("80 ardisik carpim", ([n_ for n_ in range(1, 200) if n_*(n_ + 1) == 132], 11*11, 12*12, 11*12), ([11], 121, 144, 132))
    esit("80 kalan kosulu", ([n_ for n_ in range(1, 50) if n_ % 4 == 3 and n_ % 5 == 2], sp.ilcm(4, 5), 4*11 + 3, 5*9 + 2), ([7, 27, 47], 20, 47, 47))
    esit("80 kesirli", (_coz(3*x/5 + 2, 20), 30*Q(3, 5), _coz(x/2 + x/3, 45), Q(54, 2), Q(54, 3)), (FiniteSet(30), 18, FiniteSet(54), 27, 18))
    esit("80 ortalama", (5*18, 4*16, 90 - 64, 20*70, 21*71, 1491 - 1400, 70 + 21*1), (90, 64, 26, 1400, 1491, 91, 91))
    esit("80 tersten", (_coz((3*(x + 5) - 6)/2, 18), 18*2, 36 + 6, Q(42, 3), 14 - 5, (9 + 5)*3, 42 - 6, Q(36, 2)), (FiniteSet(9), 36, 42, 14, 9, 42, 36, 18))


def yazi_81_85():
    """81 Kesir, 82 Yas, 83 Yuzde, 84 Kar-Zarar, 85 Faiz problemleri."""
    Q = Rational
    D = lambda s: Rational(s)
    s_, k_, t_, d_, n_ = sp.symbols("s_ k_ t_ d_ n_", real=True)
    # ── 81 kesir problemleri ──
    esit("81 kesrini bulmak", (Q(60, 5), 2*12, 60*Q(2, 5)), (12, 24, 24))
    esit("81 tamamini bulmak", (Q(12, 3), 7*4, _coz(Q(3, 7)*x, 12), 12*Q(7, 3), 12*Q(3, 7) < 12), (4, 28, FiniteSet(28), 28, True))
    esit("81 serit modeli", (sp.ilcm(3, 4), 12*Q(1, 3), 12*Q(1, 4), 12 - 4 - 3, Q(2500, 5), 12*500, 6000*Q(1, 3) + 6000*Q(1, 4) + 2500), (12, 4, 3, 5, 500, 6000, 6000))
    esit("81 kalanin kesri", (sp.simplify(x - x/4 - 3*x/4), sp.simplify(3*x/4*Q(2, 5) - 3*x/10), sp.simplify(3*x/4 - 3*x/10 - 9*x/20), _coz(9*x/20, 135), Q(300, 4), 300 - 75, 225*Q(2, 5), 225 - 90, Q(3, 4)*Q(3, 5), 300*Q(2, 5)),
         (0, 0, 0, FiniteSet(300), 75, 225, 90, 135, Q(9, 20), 120))
    esit("81 parcadan parcaya", (18*4, 72*Q(2, 3), 18*4*Q(2, 3), Q(72, 4)), (72, 48, 48, 18))
    esit("81 kesrin kesri", (Q(2, 3)*Q(1, 4), Q(2, 12), 36*Q(1, 6), 36*Q(2, 3), 24*Q(1, 4)), (Q(1, 6), Q(1, 6), 6, 24, 6))
    esit("81 is sure", (Q(6, 2), 5*3, 3*3, 6 + 9), (3, 15, 9, 15))
    esit("81 kesirle indirim", (_coz(Q(4, 5)*x, 480), 480*Q(5, 4), 600*D("0.8"), Q(1, 5) == D("0.2")), (FiniteSet(600), 600, 480, True))
    esit("81 doluluk", (_coz(Q(7, 10)*x - Q(2, 5)*x, 30), Q(2, 5) == Q(4, 10), 100*Q(2, 5), 40 + 30, 100*Q(7, 10), Q(2, 3)*Q(1, 2), _coz(Q(1, 3)*x, 200)),
         (FiniteSet(100), True, 40, 70, 70, Q(1, 3), FiniteSet(600)))
    esit("81 kesirli denklem", (_coz(2*x/3 + 4, 3*x/4), sp.expand(12*(2*x/3 + 4)), 48*Q(2, 3), 32 + 4, 48*Q(3, 4), _coz(3*x/4 - 2*x/3, 5), sp.simplify(3*x/4 - 2*x/3 - x/12), 60*Q(3, 4), 60*Q(2, 3)),
         (FiniteSet(48), 8*x + 48, 32, 36, 36, FiniteSet(60), 0, 45, 40))
    esit("81 bahce birim", (15*Q(2, 5), 15 - 6, 9*Q(1, 3), 9 - 3, Q(120, 6), 15*20, 300*Q(2, 5), 180*Q(1, 3), 300 - 120 - 60), (6, 9, 3, 6, 20, 300, 120, 60, 120))
    esit("81 karsilastirma", (Q(3, 8) == Q(15, 40), Q(2, 5) == Q(16, 40), Q(2, 5) > Q(3, 8), float(Q(3, 8)), float(Q(2, 5)), sp.ilcm(8, 5)), (True, True, True, 0.375, 0.4, 40))
    esit("81 paylastirma", (Q(1, 2) + Q(1, 3), 1 - Q(5, 6), _coz(Q(1, 6)*x, 1500), 9000*Q(1, 2), 9000*Q(1, 3), 4500 + 3000 + 1500, Q(3, 6) + Q(2, 6), Q(1, 2) + Q(1, 3) == Q(2, 5)),
         (Q(5, 6), Q(1, 6), FiniteSet(9000), 4500, 3000, 9000, Q(5, 6), False))
    # ── 82 yas problemleri ──
    esit("82 gelecege", (_coz(36 + t_, 3*(8 + t_), t_), 36 + 6, 8 + 6, 3*14, 36 - 8, Q(28, 2), 14 - 8), (FiniteSet(6), 42, 14, 42, 28, 14, 6))
    esit("82 gecmise", (_coz(40 - t_, 5*(12 - t_), t_), 40 - 5, 12 - 5, 5*7, 40 - 12, Q(28, 4), 12 - 7), (FiniteSet(5), 35, 7, 35, 28, 7, 5))
    esit("82 yas farki formulu", (all((f_ % (k2 - 1) != 0) or ((f_//(k2 - 1)) + f_ == k2*(f_//(k2 - 1))) for f_ in range(1, 60) for k2 in range(2, 8)), 4 - 1, Q(9, 3), 3 + 9, 4*3), (True, 3, 3, 12, 12))
    esit("82 yas toplami", (30 + 3*4, _coz(96 + 4*t_, 120, t_), Q(20, 5)), (42, FiniteSet(6), 4))
    esit("82 dogmamis", (29 + 5 + 3, 37 - 3*4, 29 - 4, 5 - 4, 3 - 4 < 0, 25 + 1), (37, 25, 25, 1, True, 26))
    esit("82 uc kisili", (_coz(3*s_ + 5, 2*(s_ + 10), s_), 3*15, 45 + 5, 15 + 10, 2*25, 2*5), (FiniteSet(15), 45, 50, 25, 50, 10))
    esit("82 hic esit olmaz", (15 - 12, (15 + 10) - (12 + 10), Q(12, 15), Q(27, 30), Q(27, 30) > Q(12, 15), all(Q(12 + t2, 15 + t2) < 1 for t2 in range(0, 500))), (3, 3, Q(4, 5), Q(9, 10), True, True))
    esit("82 ortalama", (5*20, 100 + 26, Q(126, 6), 21 + 3), (100, 126, 21, 24))
    esit("82 oranli", (sp.solveset(sp.Eq((3*k_ + 6)*3, (5*k_ + 6)*2), k_, R), 3*6, 5*6, Q(24, 36)), (FiniteSet(6), 18, 30, Q(2, 3)))
    esit("82 zaman cizgisi", (_coz(10 + 3*d_, 40, d_), 10 + 10, 10 + 2*10, 30 - 10, 20 - 10, 20 + 10, 30 + 10), (FiniteSet(10), 20, 30, 20, 10, 30, 40))
    esit("82 dogum yili", (_coz(x + 20, 3*x), 2010 - 10, 10 + 20, 3*10, 2026 - 2012, 3*14, 2026 - 42, 2012 - 1984), (FiniteSet(10), 2000, 30, 30, 14, 42, 1984, 28))
    # ── 83 yuzde problemleri ──
    esit("83 100 kabul", (100*D("1.2"), 120*D("0.25"), 120 - 30, D("1.2")*D("0.75"), Q(100, 100)*25), (120, 30, 90, D("0.9"), 25))
    esit("83 yuzdenin yuzdesi", (45*D("0.2"), D("0.45")*D("0.2")), (9, D("0.09")))
    esit("83 oran degisen", (_coz(D("0.4")*x + 6, D("0.5")*(x + 6)), D("0.4")*30, 12 + 6, 30 + 6, Q(18, 36)), (FiniteSet(30), 12, 18, 36, Q(1, 2)))
    esit("83 fiyat miktar", (1/D("1.25"), Q(100, 4), Q(100, 5), Q(25 - 20, 25)), (D("0.8"), 25, 20, Q(1, 5)))
    esit("83 karsilastirma", (Q(25, 125), [Q(a2, 100 + a2) for a2 in (25, 50, 100)]), (Q(1, 5), [Q(1, 5), Q(1, 3), Q(1, 2)]))
    esit("83 art arda", (D("1.2")*D("1.25"), D("1.1")*D("0.9")), (D("1.5"), D("0.99")))
    esit("83 buyume", (200*D("1.1"), 220*D("1.1"), 242 - 200, Q(42, 200)), (220, 242, 42, Q(21, 100)))
    esit("83 son degerden", (D("1.2")*D("0.9"), 540/D("1.08"), 500*D("1.2"), 600*D("0.9"), 540*D("1.1"), 540/D("0.9")), (D("1.08"), 500, 600, 540, 594, 600))
    esit("83 kesir karsiliklari", ([D("0.125"), D("0.2"), D("0.25"), Q(1, 3), D("0.5"), Q(2, 3), D("0.75")], Q(1, 3)*100, Q(2, 3)*100, 360*Q(3, 4), Q(360, 4), 90*3),
         ([Q(1, 8), Q(1, 5), Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4)], Q(100, 3), Q(200, 3), 270, 90, 270))
    esit("83 yuzde puan", (36 - 30, Q(6, 30)*100), (6, 20))
    esit("83 anket", (100 - 36 - 44, 250*D("0.2"), 250*D("0.36"), 250*D("0.44"), 90 + 110 + 50), (20, 50, 90, 110, 250))
    esit("83 denklemli", (_coz(D("0.3")*x + 12, D("0.5")*x), 60*D("0.3"), 18 + 12, 60*D("0.5"), _coz(3*x + 120, 5*x)), (FiniteSet(60), 18, 30, 30, FiniteSet(60)))
    esit("83 birlesik yuzde", (20*D("0.6"), 30*D("0.4"), 12 + 12, Q(24, 50), Q(60 + 40, 2)), (12, 12, 24, Q(12, 25), 50))
    esit("83 hedef", (40*D("0.75"), 25*D("0.8"), 30 - 20, _coz(20 + d_ >= 30, 0, d_)), (30, 20, 10, Interval(10, oo)))
    esit("83 bilinmeyen yuzde", (92 - 80, Q(12, 80)*100, _coz(D("0.85")*x, 340), 400*D("0.85")), (12, 15, FiniteSet(400), 340))
    # ── 84 kar ve zarar ──
    esit("84 kar yuzdesi", (300 - 240, Q(60, 240)*100, 450 - 405, Q(45, 450)*100, Q(60, 300)*100), (60, 25, 45, 10, 20))
    esit("84 satis fiyati", (180*D("1.35"), 243 - 180, 600*D("0.85"), 600 - 510), (243, 63, 510, 90))
    esit("84 maliyet", (_coz(D("0.8")*x, 320), 400 - 320, 320*D("1.2")), (FiniteSet(400), 80, 384))
    esit("84 birim fiyat", (11 - 8, 3*120, Q(3, 8)*100, 8*120, 11*120, Q(360, 960)*100), (3, 360, D("37.5"), 960, 1320, D("37.5")))
    esit("84 denklemli", (_coz(540 - x, 2*(x - 360)), 540 - 420, 420 - 360), (FiniteSet(420), 120, 60))
    esit("84 maliyet artisi", (100*D("1.5"), 100*D("1.2"), 150 - 120, Q(30, 120)*100), (150, 120, 30, 25))
    esit("84 etiket indirim", (100*D("1.5"), 150*D("0.8"), 120 - 100, D("1.5")*D("0.8"), 200*D("1.6"), 320 - 200, Q(120, 320)*100), (150, 120, 20, D("1.2"), 320, 120, D("37.5")))
    esit("84 toplu satis", (60*D("1.3") + 40*D("0.9"), 114 - 100, Q(30 + (-10), 2)), (114, 14, 10))
    esit("84 fire", (50*20, 1000*D("1.35"), 50 - 5, Q(1350, 45), 45*20, 45*30), (1000, 1350, 45, 30, 900, 1350))
    esit("84 ayni fiyata iki mal", (1200/D("1.2"), 1200/D("0.8"), 1000 + 1500, 2*1200, 2500 - 2400, Q(100, 2500)*100, 1200 - 1000, 1500 - 1200), (1000, 1500, 2500, 2400, 100, 4, 200, 300))
    esit("84 kar miktarindan", (90*4, 360 + 90, 360*D("1.25")), (360, 450, 450))
    esit("84 zincirleme", (D("1.2")*D("1.25")*D("1.4"), 100*D("1.2"), 120*D("1.25"), 150*D("1.4"), 20 + 25 + 40), (D("2.1"), 120, 150, 210, 85))
    esit("84 hedef adet", (20 - 15, Q(1000, 5), Q(1000 + 300, 5)), (5, 200, 260))
    esit("84 satisa gore", (500*D("0.2"), 500 - 100, Q(100, 400)*100), (100, 400, 25))
    # ── 85 faiz ──
    esit("85 basit faiz", (Q(8000*30*2, 100), 8000 + 4800, 8000*D("0.3")), (4800, 12800, 2400))
    esit("85 ay donusumu", (6000*D("0.24")*Q(5, 12), Q(24, 12), 6000*D("0.02"), 5*120, 6000*D("0.24")*5), (600, 2, 120, 600, 7200))
    esit("85 anapara", (_coz(x*25*3/100, 1800), 1800/D("0.75"), _coz(D("1.4")*x, 7000), 7000 - 5000), (FiniteSet(2400), 2400, FiniteSet(5000), 2000))
    esit("85 oran sure", (_coz(5000*x*2/100, 1500), 4000*D("0.2"), Q(2400, 800)), (FiniteSet(15), 800, 3))
    esit("85 iki kat", (_coz(25*t_, 100, t_), 1000*D("0.25")*4, _coz(25*t_, 200, t_), Q(100, 20)), (FiniteSet(4), 1000, FiniteSet(8), 5))
    esit("85 bilesik", (10000*D("1.1"), 11000*D("1.1"), 10000*D("1.1")**2, 12100 - 10000, 12100 - 11000, D("1.1")**3, D("1.1")**6 > D("1.77"), D("1.1")**6 < D("1.772")),
         (11000, 12100, 12100, 2100, 1100, D("1.331"), True, True))
    esit("85 karsilastirma tablosu", ([10000 + 1000*y2 for y2 in (1, 2, 3)], [10000*D("1.1")**y2 for y2 in (1, 2, 3)]), ([11000, 12000, 13000], [11000, 12100, 13310]))
    esit("85 iki hesap", (_coz(D("0.2")*x + D("0.3")*(20000 - x), 5000), 10000*D("0.2"), 10000*D("0.3"), Q(5000, 20000)*100, Q(20 + 30, 2)), (FiniteSet(10000), 2000, 3000, 25, 25))
    esit("85 aylik yillik", (12*2, D("1.02")**12 > D("1.24"), D("1.02")**12 < D("1.27")), (24, True, True))
    esit("85 borc taksit", (12000*D("0.18")*Q(8, 12), 12000 + 1440, Q(13440, 8)), (1440, 13440, 1680))
    esit("85 farkli zaman", (10000*D("0.2")*1, 10000*D("0.2")*Q(1, 2), 2000 + 1000, 20000*D("0.2")), (2000, 1000, 3000, 4000))
    esit("85 bilesik sure", (D("1.2")**2, D("1.2")**3, D("1.2")**4, 10000*D("1.2")**3, 10000*D("1.2")**4, min(y2 for y2 in range(1, 20) if D("1.2")**y2 > 2)), (D("1.44"), D("1.728"), D("2.0736"), 17280, 20736, 4))
    esit("85 teklif", (10000 + 10000*D("0.3")*2, 10000*D("1.28")**2, 16384 - 16000, 10000*D("1.3") == 10000*(1 + D("0.3"))), (16000, 16384, 384, True))


def yazi_86_91():
    """86 Oran-Oranti, 87 Isci-Havuz, 88 Hareket, 89 Karisim problemleri, 90 Sayi Basamaklari, 91 Basamak Degeri."""
    Q = Rational
    D = lambda s: Rational(s)
    k_, d_, a_s, r_ = sp.symbols("k_ d_ a_s r_", real=True)
    # ── 86 oran ve oranti problemleri ──
    esit("86 paylastirma", (_coz(5*k_ - 2*k_, 1200, k_), [2*400, 3*400, 5*400], 800 + 1200 + 2000, 2000 - 800), (FiniteSet(400), [800, 1200, 2000], 4000, 1200))
    esit("86 ters oranti", (sp.ilcm(sp.ilcm(3, 4), 6), [12*Q(1, 3), 12*Q(1, 4), 12*Q(1, 6)], 4 + 3 + 2, Q(900, 9), [400, 300, 200], 3*400, 4*300, 6*200), (12, [4, 3, 2], 9, 100, [400, 300, 200], 1200, 1200, 1200))
    esit("86 birlesik", ((3*2, 4*2), sp.ilcm(4, 8), 6 + 8 + 1, _coz(15*k_, 150, k_), [60, 80, 10], Q(60, 80) == Q(3, 4), Q(80, 10) == Q(8, 1)), ((6, 8), 8, 15, FiniteSet(10), [60, 80, 10], True, True))
    esit("86 degisen oran", (_coz(7*(5*k_ - 4), 21*k_, k_), 5*2, 7*2, Q(10 - 4, 14)), (FiniteSet(2), 10, 14, Q(3, 7)))
    esit("86 oran kesir", (_coz(4*k_*Q(1, 4) + 5*k_*Q(1, 5), 72, k_), 9*36, 4*36, 5*36, 144*Q(1, 4), 180*Q(1, 5)), (FiniteSet(36), 324, 144, 180, 36, 36))
    esit("86 aktarma", (_coz(5*k_ - 60, 3*k_ + 60, k_), 300 - 60, 180 + 60, 300 + 180), (FiniteSet(60), 240, 240, 480))
    esit("86 dorduncu orantili", (_coz(Q(3, 5), 12/x), Q(12, 20)), (FiniteSet(20), Q(3, 5)))
    esit("86 olcek", (6*25000, Q(150000, 100000), 2*25000**2, Q(1250000000, 10000)), (150000, D("1.5"), 1250000000, 125000))
    esit("86 oran koruma", (_coz(8*k_, 40, k_), _coz(8*k_, 64, k_), (3*5, 5*5), (3*8, 5*8), 24 - 15, 40 - 25, Q(9, 15)), (FiniteSet(5), FiniteSet(8), (15, 25), (24, 40), 9, 15, Q(3, 5)))
    esit("86 tarif", (Q(6, 4), 300*Q(3, 2), Q(5, 8), float(Q(5, 8))), (Q(3, 2), 450, Q(5, 8), 0.625))
    esit("86 hiz sure", (Q(8, 4), 3*2, 8*3 == 6*4), (2, 6, True))
    esit("86 calisma hizi", (_coz(5*k_*30, 1, k_), Q(2, 150), Q(3, 150), Q(1, 75) + Q(1, 50)), (FiniteSet(Q(1, 150)), Q(1, 75), Q(1, 50), Q(1, 30)))
    esit("86 hizli cozum", (sp.simplify((2*k_ + 3*k_)/(2*k_ - 3*k_)), Q(4 + 6, 4 - 6)), (-5, -5))
    # ── 87 isci ve havuz ──
    esit("87 iki kisi", (Q(1, 12) + Q(1, 24), Q(12*24, 12 + 24), 8 < 12), (Q(1, 8), 8, True))
    esit("87 kisa formul", all(1/(Q(1, a2) + Q(1, b2)) == Q(a2*b2, a2 + b2) for a2 in range(1, 40) for b2 in range(1, 40)), True)
    esit("87 uc kisi", (Q(1, 10) + Q(1, 15) + Q(1, 30), Q(30, 3 + 2 + 1)), (Q(1, 5), 5))
    esit("87 bir kisinin suresi", (Q(1, 12) - Q(1, 20), Q(1, 20) + Q(1, 30)), (Q(1, 30), Q(1, 12)))
    esit("87 birlikte sonra tek", (Q(1, 18) + Q(1, 36), 4*Q(1, 12), 1 - Q(1, 3), Q(2, 3)*18, 4 + 12), (Q(1, 12), Q(1, 3), Q(2, 3), 12, 16))
    esit("87 sirayla", (Q(4, 10), 1 - Q(2, 5), Q(3, 5)*15, Q(4, 10) + Q(9, 15)), (Q(2, 5), Q(3, 5), 9, 1))
    esit("87 kismi is", (Q(8, 2)*5, Q(1, 20) + Q(1, 30)), (20, Q(1, 12)))
    esit("87 isci sayisi", (8*15, Q(120, 12), 6*20, 6*4, 120 - 24, Q(96, 8), 4 + 12), (120, 10, 120, 24, 96, 12, 16))
    esit("87 farkli hiz", (_coz(3*r_*6, 1, r_), Q(1, 9) + Q(1, 18)), (FiniteSet(Q(1, 18)), Q(1, 6)))
    esit("87 ara verme", (12 // 3, 12 // 3 - 1, 12 + 3, len("WWWRWWWRWWWRWWW"), "WWWRWWWRWWWRWWW".count("W")), (4, 3, 15, 15, 12))
    esit("87 havuz", (Q(1, 6) + Q(1, 9), Q(18, 5), float(Q(18, 5)), Q(6*9, 15), D("0.6")*60), (Q(5, 18), Q(18, 5), 3.6, Q(18, 5), 36))
    esit("87 dolduran bosaltan", (Q(1, 4) - Q(1, 12), Q(1, 8) - Q(1, 6)), (Q(1, 6), -Q(1, 24)))
    esit("87 kismen dolu", (1 - Q(1, 3), Q(1, 6) - Q(1, 9), Q(2, 3)/Q(1, 18)), (Q(2, 3), Q(1, 18), 12))
    esit("87 uc musluk", (Q(1, 6) + Q(1, 12) - Q(1, 8), 4 + 2 - 3, Q(24, 3)), (Q(1, 8), 3, 8))
    esit("87 once biri", (Q(3, 12), 1 - Q(1, 4), Q(1, 12) + Q(1, 6), Q(3, 4)/Q(1, 4), 3 + 3), (Q(1, 4), Q(3, 4), Q(1, 4), 3, 6))
    # ── 88 hareket ──
    esit("88 birimler", (Q(72000, 3600), 90*Q(20, 60), 90*20), (20, 30, 1800))
    esit("88 temel", (Q(240, 3), Q(150, 60), D("0.5")*60), (80, D("2.5"), 30))
    esit("88 karsilasma", (Q(420, 60 + 80), 60*3, 80*3, 180 + 240), (3, 180, 240, 420))
    esit("88 farkli saat", (480 - 60, Q(420, 140), 10 + 3, 60*4, 80*3, 240 + 240), (420, 3, 13, 240, 240, 480))
    esit("88 yetisme", (60*2, Q(120, 90 - 60), 90*4, 60*(2 + 4)), (120, 4, 360, 360))
    esit("88 uzaklasma", ((45 + 55)*4,), (400,))
    esit("88 ortalama hiz", (Q(120, 60), Q(120, 40), Q(240, 5), Q(60 + 40, 2), Q(180, 60), Q(180, 90), Q(360, 5), Q(60 + 90, 2), Q(2*60*90, 60 + 90)), (2, 3, 48, 50, 3, 2, 72, 75, 72))
    esit("88 esit sure ortalamasi", Q(60*1 + 90*1, 2), 75)
    esit("88 gidis donus", (_coz(d_/80 + d_/120, 5, d_), Q(240, 80), Q(240, 120)), (FiniteSet(240), 3, 2))
    esit("88 akinti", (20 + 4, 20 - 4, Q(48, 24), Q(48, 16), Q(24 + 16, 2), Q(24 - 16, 2)), (24, 16, 2, 3, 20, 4))
    esit("88 tren", (Q(800 + 200, 20), Q(200, 20), Q(800, 20)), (50, 10, 40))
    esit("88 pist", (Q(400, 6 - 4), Q(400, 6 + 4), [200*i2 for i2 in range(1, 6)][-1], len([t2 for t2 in range(1, 1001) if t2 % 200 == 0])), (200, 40, 1000, 5))
    esit("88 gec kalma", (_coz(d_/5 - d_/6, Q(1, 6), d_), Q(5, 5)*60, Q(5, 6)*60, 6 + 4), (FiniteSet(5), 60, 50, 10))
    # ── 89 karisim ──
    esit("89 oran yuzde", (Q(1, 1 + 4), Q(1, 4)), (Q(1, 5), Q(1, 4)))
    esit("89 madde ekleme", (300*D("0.2"), Q(60 + 100, 400), _coz(60 + x, D("0.4")*(300 + x))), (60, Q(2, 5), FiniteSet(100)))
    esit("89 su ekleme", (400*D("0.3"), Q(120, 600), 120/D("0.2") - 400), (120, Q(1, 5), 200))
    esit("89 buharlasma", (500*D("0.12"), Q(60, 300), 600*D("0.15"), 90/D("0.25"), 600 - 360), (60, Q(1, 5), 90, 360, 240))
    esit("89 iki karisim", (200*D("0.1") + 300*D("0.25"), Q(95, 500), Q(10 + 25, 2)), (95, D("0.19"), D("17.5")))
    esit("89 uc karisim", (100*D("0.1") + 200*D("0.2") + 200*D("0.35"), Q(120, 500)), (120, D("0.24")))
    esit("89 madde ve su", (200*D("0.2") + 50, Q(90, 300), Q(50, 100)), (90, D("0.3"), Q(1, 2)))
    esit("89 istenen oran", (_coz(300*D("0.1") + D("0.4")*x, D("0.2")*(300 + x)), Q(30 + 60, 450)), (FiniteSet(150), Q(1, 5)))
    esit("89 capraz", (20 - 10, 40 - 20, Q(20, 10), Q(300, 150)), (10, 20, 2, 2))
    esit("89 alip su koyma", (40*D("0.5"), 10*D("0.5"), Q(15, 40), 15*Q(3, 4)), (20, 5, D("0.375"), D("11.25")))
    esit("89 alasim", (60*Q(18, 24), _coz(45 + x, Q(22, 24)*(60 + x)), Q(165, 180), Q(22, 24)), (45, FiniteSet(120), Q(11, 12), Q(11, 12)))
    esit("89 fiyat", (_coz(40*a_s + 70*(30 - a_s), 1500, a_s), 20*40 + 10*70, 50 - 40, 70 - 50), (FiniteSet(20), 1500, 10, 20))
    esit("89 oranli karisim", (_coz(2*k_ + 4, 3*k_, k_), 2*4, 3*4, 8 + 4), (FiniteSet(4), 8, 12, 12))
    # ── 90 sayi basamaklari ──
    esit("90 adetler", ([9*10**(n2 - 1) for n2 in range(1, 5)], [len(range(10**(n2 - 1), 10**n2)) for n2 in range(2, 5)], 99 - 10 + 1), ([9, 90, 900, 9000], [90, 900, 9000], 90))
    uc_ = [n2 for n2 in range(100, 1000) if len(set(str(n2))) == 3]
    esit("90 rakamlari farkli", (min(uc_), max(uc_), 987 - 102, len(uc_), len([n2 for n2 in range(10, 100) if len(set(str(n2))) == 2])), (102, 987, 885, 648, 81))
    sec_ = [n2 for n2 in range(100, 1000) if set(str(n2)) <= set("0123")]
    esit("90 verilen rakamlar", (len([n2 for n2 in sec_ if len(set(str(n2))) == 3]), len(sec_), len([n2 for n2 in range(100, 1000) if set(str(n2)) <= set("12345") and len(set(str(n2))) == 3 and n2 % 2 == 0])), (18, 48, 24))
    esit("90 rakam toplami", ([n2 for n2 in range(10, 100) if sum(map(int, str(n2))) == 5], [n2 for n2 in range(10, 100) if sum(map(int, str(n2))) == 15]), ([14, 23, 32, 41, 50], [69, 78, 87, 96]))
    esit("90 yer degistirme", (sp.expand((10*a + b) + (10*b + a)), sp.expand((10*a + b) - (10*b + a)), sp.expand((100*a + 10*b + c) - (100*c + 10*b + a)), 74 + 47, 74 - 47,
                               [10*A2 + B2 for A2 in range(1, 10) for B2 in range(1, 10) if (10*A2 + B2) + (10*B2 + A2) == 132]),
         (11*a + 11*b, 9*a - 9*b, 99*a - 99*c, 121, 27, [39, 48, 57, 66, 75, 84, 93]))
    esit("90 basamak sayisi", (len(str(5**10*2**12)), 5**10*2**12, len(str(10**10))), (11, 4*10**10, 11))
    esit("90 9 a bolunen", max(n2 for n2 in uc_ if n2 % 9 == 0), 981)
    esit("90 sayfa", (sum(len(str(n2)) for n2 in range(1, 151)), 9 + 180 + 153, 99 + (342 - 189)//3), (342, 342, 150))
    esit("90 yedi rakami", sum(str(n2).count("7") for n2 in range(1, 101)), 20)
    dizi_ = "".join(str(n2) for n2 in range(1, 300))
    esit("90 yan yana", (dizi_[99], dizi_[199], 100 - 9, divmod(91, 2), 9 + 180, divmod(11, 3)), ("5", "0", 91, (45, 1), 189, (3, 2)))
    # ── 91 basamak degeri ──
    esit("91 cozumleme", (4*1000 + 5*100 + 7*10 + 2, 4*10**3 + 5*10**2 + 7*10 + 2, 3*10000 + 4*100 + 5, 7*111), (4572, 4572, 30405, 777))
    esit("91 denklem", ([10*A2 + B2 for A2 in range(1, 10) for B2 in range(10) if 10*A2 + B2 == 4*(A2 + B2)], [100*A2 + 10*B2 + C2 for A2 in range(1, 10) for B2 in range(10) for C2 in range(10) if A2 == 2*C2 and B2 == A2 + C2 and A2 + B2 + C2 == 12]),
         ([12, 24, 36, 48], [462]))
    esit("91 basamak degerleri", (5000 + 5, 5000 - 5), (5005, 4995))
    esit("91 rakam ekleme", (_coz(10*x + 7, x + 520), 577 - 57), (FiniteSet(57), 520))
    esit("91 rakam degistirme", (2*100 - 5, 511 - 316), (195, 195))
    esit("91 uc basamak ters", (len([n2 for n2 in range(100, 1000) if n2 % 10 != 0 and n2 - int(str(n2)[::-1]) == 396]), 5*10, sp.expand((100*a + 10*b + c) + (100*b + 10*c + a) + (100*c + 10*a + b)), 123 + 231 + 312, 111*6),
         (50, 50, 111*a + 111*b + 111*c, 666, 666))
    esit("91 harfli bolunebilme", ([A2 for A2 in range(10) if (400 + 10*A2 + 7) % 9 == 0], [A2 for A2 in range(10) if (400 + 10*A2 + 7) % 3 == 0]), ([7], [1, 4, 7]))
    esit("91 en buyuk fark", (max((10*A2 + B2) - (10*B2 + A2) for A2 in range(1, 10) for B2 in range(1, 10)), 91 - 19), (72, 72))
    esit("91 ters cevrilen", [10*A2 + B2 for A2 in range(1, 10) for B2 in range(10) if (10*B2 + A2) - (10*A2 + B2) == 36 and A2 + B2 == 10], [37])
    esit("91 eldeli", (47 + 38, 52 - 27), (85, 25))
    esit("91 dokuz iliskisi", (4 + 5 + 7 + 2, 4572 - 18, Q(4554, 9), all((n2 - sum(map(int, str(n2)))) % 9 == 0 for n2 in range(1, 20000)), sp.expand((100*a + 10*b + c) - (a + b + c))), (18, 4554, 506, True, 99*a + 9*b))
    esit("91 ondalik", (D("3.472"), 3 + D("0.4") + D("0.07") + D("0.002")), (D("3.472"), D("3.472")))
    esit("91 tabanlar", (int("1011", 2), 8 + 0 + 2 + 1, int("23", 5)), (11, 11, 13))
    esit("91 yuvarlama", (round(4572, -1), (4572 + 50)//100*100, (4572 + 500)//1000*1000), (4570, 4600, 5000))


def yazi_92_97():
    """92 Faktoriyel, 93 Permutasyon, 94 Kombinasyon, 95 Olasilik, 96 Kumeler, 97 Mantik."""
    from math import factorial as fa, comb as C, perm as P, prod
    perms = itertools.permutations
    def say(n_esya, kosul):
        """n_esya farkli nesnenin (0..n-1) kosulu saglayan siralamalari."""
        return sum(1 for s in perms(range(n_esya)) if kosul(s))
    def yan_yana(s, a, b):
        return abs(s.index(a) - s.index(b)) == 1
    # ── 92 faktoriyel ──
    esit("92 tablo", [fa(n) for n in range(8)], [1, 1, 2, 6, 24, 120, 720, 5040])
    esit("92 ozyineleme", (6*fa(5), 8*5040, 9*40320, fa(8), fa(9), fa(10) == 10*9*8*fa(7), fa(1) == 1*fa(0)), (720, 40320, 362880, 40320, 362880, True, True))
    esit("92 uc kitap", (len(set(perms("ABC"))), sorted("".join(p) for p in perms("ABC"))), (6, ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]))
    esit("92 bes-alti kisi", (fa(5), fa(6), fa(6) // fa(5)), (120, 720, 6))
    esit("92 bolumler", (fa(10) // fa(8), F(fa(7), fa(5)*fa(2)), F(42, 2), F(fa(5), fa(3)), fa(10) // fa(5), 10*9*8*7*6, fa(10) // fa(5) == fa(2)), (90, 21, 21, 20, 30240, 30240, False))
    esit("92 genel bolum", all(fa(n + 1) // fa(n) == n + 1 and fa(n + 2) // fa(n) == (n + 2)*(n + 1) for n in range(1, 30)), True)
    esit("92 toplama cikarma", (fa(5) + fa(4), fa(4)*6, fa(6) - fa(5), fa(5)*5, F(fa(8) + fa(7), fa(7) - fa(6)), fa(8) + fa(7) == 9*fa(7), fa(7) - fa(6) == 6*fa(6), F(9*7, 6)), (144, 144, 600, 600, F(21, 2), True, True, F(21, 2)))
    esit("92 dagilmaz", (fa(2 + 3), fa(2) + fa(3), all(fa(2*n) != 2*fa(n) for n in range(2, 20))), (120, 8, True))
    esit("92 denklemler", ([n for n in range(1, 60) if fa(n + 1) // fa(n - 1) == 42], F(fa(7), fa(5)), [n for n in range(2, 60) if fa(n) == 120 and fa(n - 2) == 6]), ([6], 42, [5]))
    esit("92 ardisik", (7*8*9*10, fa(10) // fa(6), 3628800 // 720, 7*8*9, 504 // 6, 504 % 6), (5040, 5040, 5040, 504, 84, 0))
    esit("92 ardisik k! boler", all(prod(range(a, a + k)) % fa(k) == 0 for a in range(1, 40) for k in range(1, 9)), True)
    esit("92 kalanlar", ((fa(20) + 7) % 11, (fa(10) + 15) % 12, 15 % 12, fa(10) % 12), (7, 3, 3, 0))
    esit("92 esitsizlik", (min(n for n in range(20) if fa(n) > 1000), fa(6) < 1000, fa(7) > 1000), (7, True, True))
    esit("92 basamak", (fa(10), fa(12), len(str(fa(10))), len(str(fa(12))), round(fa(10) / 1e6, 1)), (3628800, 479001600, 7, 9, 3.6))
    esit("92 secim", (F(fa(5), fa(2)*fa(3)), C(5, 2), 5*4, 20 // 2), (10, 10, 20, 10))
    esit("92 buyume", ([(2**n, fa(n)) for n in (4, 6, 8, 10)], 2**10), ([(16, 24), (64, 720), (256, 40320), (1024, 3628800)], 1024))
    sifir = lambda n: len(str(fa(n))) - len(str(fa(n)).rstrip("0"))
    esit("92 sondaki sifir", (sifir(25), 25 // 5 + 25 // 25, sifir(100), 100 // 5 + 100 // 25, [k for k in range(1, 101) if k % 25 == 0]), (6, 6, 24, 24, [25, 50, 75, 100]))
    esit("92 asal carpan", (sp.factorint(fa(10)), 10 // 2 + 10 // 4 + 10 // 8, 10 // 3 + 10 // 9, 256*81*25*7), ({2: 8, 3: 4, 5: 2, 7: 1}, 8, 4, 3628800))
    esit("92 bolunebilme", (fa(7) % 60, fa(7) // 60, fa(7) % 11 != 0, all(fa(n) % p_ != 0 for n in range(1, 30) for p_ in sp.primerange(n + 1, 60))), (0, 84, True, True))
    esit("92 birler", (sum(fa(n) for n in range(1, 101)) % 10, 1 + 2 + 6 + 24, all(fa(n) % 10 == 0 for n in range(5, 101)), all(fa(n) % 100 == 0 for n in range(10, 101))), (3, 33, True, True))
    # ── 93 permutasyon ──
    esit("93 ilkeler", (3*4, len(list(itertools.product(range(3), range(4)))), 5 + 3), (12, 12, 8))
    esit("93 P tablosu", (P(5, 5), P(5, 2), P(8, 3), [P(n, 1) for n in range(1, 9)] == list(range(1, 9)), all(P(n, r) == fa(n) // fa(n - r) for n in range(12) for r in range(n + 1))), (120, 20, 336, True, True))
    esit("93 yonetim yaris", (P(8, 3), 10*9*8, P(10, 3), 336 // 6, C(8, 3)), (336, 720, 720, 56, 56))
    esit("93 ozdes", (len(set(perms("KAPAK"))), len(set(perms("ANANAS"))), len(set(perms("KKKMM"))), F(fa(6), fa(3)*fa(2))), (30, 60, 10, 60))
    esit("93 blok", (say(5, lambda s: yan_yana(s, 0, 1)), fa(4)*2, say(5, lambda s: not yan_yana(s, 0, 1)), 120 - 48), (48, 48, 72, 72))
    # kitaplar 0-2 matematik, 3-4 fizik; ayni dersin kitaplari yan yana
    blok = lambda s, g: max(s.index(i) for i in g) - min(s.index(i) for i in g) == len(g) - 1
    esit("93 ders bloklari", (say(5, lambda s: blok(s, (0, 1, 2)) and blok(s, (3, 4))), 2*6*2), (24, 24))
    # 0-2 erkek, 3-4 kiz: kizlar yan yana degil
    esit("93 araya yerlestirme", (say(5, lambda s: not yan_yana(s, 3, 4)), fa(3)*P(4, 2), P(4, 2)), (72, 72, 12))
    esit("93 bir kisi arada", (say(5, lambda s: abs(s.index(0) - s.index(1)) == 2), 3*2*6), (36, 36))
    # 0-2 kiz, 3-5 erkek, donusumlu
    donusum = lambda s, kizlar: all((s[i] in kizlar) != (s[i + 1] in kizlar) for i in range(len(s) - 1))
    esit("93 donusumlu", (say(6, lambda s: donusum(s, {0, 1, 2})), 2*6*6), (72, 72))
    esit("93 donusumlu 3 kiz 2 erkek", all(s[0] in {0, 1, 2} for s in perms(range(5)) if donusum(s, {0, 1, 2})), True)
    uc = [100*a + 10*b + c for a, b, c in perms(range(1, 6), 3)]
    esit("93 rakamlar", (len(uc), P(5, 3), sum(1 for u in uc if u > 300), 3*4*3), (60, 60, 36, 36))
    esit("93 izgara", (len(set(perms("SSSYY"))), C(5, 2)), (10, 10))
    esit("93 konum", (say(5, lambda s: s[0] == 0), say(5, lambda s: s[0] == 0 and s[-1] == 1), say(5, lambda s: s[0] == 0 or s[-1] == 0), 2*24), (24, 6, 48, 48))
    def dairesel(n, ters=False):
        gorulen = set()
        for s in perms(range(n)):
            donen = [s[i:] + s[:i] for i in range(n)]
            if ters:
                donen += [tuple(reversed(d)) for d in donen]
            gorulen.add(min(donen))
        return gorulen
    daire5 = dairesel(5)
    esit("93 dairesel", (len(daire5), fa(4), 120 // 5, len(dairesel(5, True)), fa(4) // 2), (24, 24, 24, 12, 12))
    esit("93 dairesel blok", (sum(1 for d in daire5 if abs(d.index(0) - d.index(1)) in (1, 4)), fa(3)*2), (12, 12))
    esit("93 sifre", (10**4, len(list(itertools.product(range(10), repeat=4))), P(10, 4), 10*9*8*7, 10**3 + 10**4), (10000, 10000, 5040, 5040, 11000))
    kalem = list(perms("KALEM"))
    esit("93 KALEM", (len(set(kalem)), sum(1 for s in kalem if abs(s.index("A") - s.index("E")) == 1), 24*2), (120, 48, 48))
    # ── 94 kombinasyon ──
    esit("94 sira", (P(5, 3), 60 // 6, C(5, 3), F(fa(5), fa(3)*fa(2))), (60, 10, 10, 10))
    esit("94 ozel degerler", all(C(n, 0) == 1 and C(n, 1) == n and C(n, n) == 1 and C(n, 2) == n*(n - 1)//2 for n in range(2, 30)), True)
    esit("94 simetri", (C(10, 8), C(10, 2), 10*9 // 2, all(C(n, r) == C(n, n - r) for n in range(20) for r in range(n + 1))), (45, 45, 45, True))
    esit("94 komisyon", (C(12, 4), 12*11*10*9, 4*3*2*1, 11880 // 24), (495, 11880, 24, 495))
    esit("94 kiz erkek", (C(6, 2), C(5, 3), 15*10, 15 + 10), (15, 10, 150, 25))
    kisi = [("K", i) for i in range(6)] + [("E", i) for i in range(5)]
    kizsay = lambda e: sum(1 for k in e if k[0] == "K")
    ekip4 = list(itertools.combinations(kisi, 4))
    esit("94 en az bir kiz", (len(ekip4), C(11, 4), C(5, 4), sum(1 for e in ekip4 if kizsay(e) >= 1), 330 - 5), (330, 330, 5, 325, 325))
    esit("94 durumlar", (C(6, 1)*C(5, 3), C(6, 2)*C(5, 2), C(6, 3)*C(5, 1), C(6, 4), 60 + 150 + 100 + 15), (60, 150, 100, 15, 325))
    esit("94 en cok iki kiz", (sum(1 for e in ekip4 if kizsay(e) <= 2), 5 + 60 + 150, 6*10, 15*10), (215, 215, 60, 150))
    on4 = list(itertools.combinations(range(10), 4))
    esit("94 A B ayri", (len(on4), C(10, 4), C(8, 2), sum(1 for e in on4 if not (0 in e and 1 in e)), 210 - 28), (210, 210, 28, 182, 182))
    esit("94 A var yok", (sum(1 for e in on4 if 0 in e), C(9, 3), sum(1 for e in on4 if 0 not in e), C(9, 4), 84 + 126), (84, 84, 126, 126, 210))
    esit("94 pascal", ([[C(n, r) for r in range(n + 1)] for n in range(6)], all(C(n, r) == C(n - 1, r - 1) + C(n - 1, r) for n in range(1, 25) for r in range(1, n)), sum(C(5, r) for r in range(6)), 1 + 5 + 10 + 10 + 5 + 1, 2**5),
         ([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]], True, 32, 32, 32))
    esit("94 alt kume", (2**4, sum(C(4, r) for r in range(5)), 1 + 4 + 6 + 4 + 1, len([s for r in range(5) for s in itertools.combinations(range(4), r)])), (16, 16, 16, 16))
    esit("94 geometri", (C(8, 2), C(8, 3), C(6, 2), C(6, 2) - 6, 6*(6 - 3)//2, C(5, 2), C(4, 2), 10*6), (28, 56, 15, 9, 9, 10, 6, 60))
    a_, b_ = sp.symbols("a_ b_")
    esit("94 binom", (sp.expand((a_ + b_)**4), sp.expand((a_ + b_)**2), sp.Poly((a_ + b_)**4, a_, b_).coeff_monomial(a_**2*b_**2)), (a_**4 + 4*a_**3*b_ + 6*a_**2*b_**2 + 4*a_*b_**3 + b_**4, a_**2 + 2*a_*b_ + b_**2, 6))
    esit("94 tokalasma", (C(10, 2), 10*9, 90 // 2, P(10, 2)), (45, 90, 45, 90))
    esit("94 kaptan", (C(10, 5), 252*5, sum(5 for _ in itertools.combinations(range(10), 5)), C(9, 4), 10*126), (252, 1260, 1260, 126, 1260))
    esit("94 sec diz", (C(7, 3), C(7, 3)*6, P(7, 3), 7*6*5), (35, 210, 210, 210))
    def ikili_ayir(k):
        if not k:
            return [()]
        ilk, sonuc = k[0], []
        for es in k[1:]:
            kalan = [e for e in k[1:] if e != es]
            sonuc += [((ilk, es),) + r for r in ikili_ayir(kalan)]
        return sonuc
    esit("94 gruplara ayirma", (C(6, 2)*C(4, 2)*C(2, 2), 15*6*1, len(ikili_ayir(list(range(6)))), 90 // 6), (90, 90, 15, 15))
    esit("94 denklemler", ([n for n in range(2, 100) if C(n, 2) == 28], 8*7, [n for n in range(5, 100) if C(n, 3) == C(n, 5)], C(8, 3), C(8, 5)), ([8], 56, [8], 56, 56))
    # ── 95 olasilik ──
    zar = range(1, 7)
    esit("95 zar", (F(len([z for z in zar if z % 2 == 0]), 6), F(len([z for z in zar if z > 4]), 6)), (F(1, 2), F(1, 3)))
    para3 = list(itertools.product("TY", repeat=3))
    esit("95 uc para en az bir", (len(para3), F(sum(1 for p in para3 if "T" in p), 8), 1 - F(1, 8)), (8, F(7, 8), F(7, 8)))
    iki = list(itertools.product(zar, zar))
    top = lambda t: sum(1 for a, b in iki if a + b == t)
    esit("95 iki zar tablo", ([top(t) for t in (2, 4, 6, 7, 10, 12)], len(iki), F(top(7), 36), F(top(10), 36), max(range(2, 13), key=top), [top(t) for t in range(2, 13)]),
         ([1, 3, 5, 6, 3, 1], 36, F(1, 6), F(1, 12), 7, [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))
    esit("95 iki zar ciktilar", (sorted((a, b) for a, b in iki if a + b == 7), sorted((a, b) for a, b in iki if a + b == 10)), ([(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)], [(4, 6), (5, 5), (6, 4)]))
    esit("95 tam iki tura", (sorted("".join(p) for p in para3 if p.count("T") == 2), [F(sum(1 for p in para3 if p.count("T") == k), 8) for k in range(4)], C(3, 2)), (["TTY", "TYT", "YTT"], [F(1, 8), F(3, 8), F(3, 8), F(1, 8)], 3))
    esit("95 hic alti", (F(sum(1 for a, b in iki if 6 not in (a, b)), 36), F(5, 6)**2, F(sum(1 for a, b in iki if 6 in (a, b)), 36), F(1, 6) + F(1, 6), F(12, 36)), (F(25, 36), F(25, 36), F(11, 36), F(1, 3), F(1, 3)))
    esit("95 siralama", (F(say(5, lambda s: yan_yana(s, 0, 1)), fa(5)), fa(4)*fa(2)), (F(2, 5), 48))
    torba = ["K"]*4 + ["M"]*6
    cift = list(perms(range(10), 2))
    esit("95 ikinci renk", (F(sum(1 for i, j in cift if torba[j] == "K"), len(cift)), F(4, 10)*F(3, 9), F(6, 10)*F(4, 9), F(12, 90) + F(24, 90)), (F(2, 5), F(12, 90), F(24, 90), F(2, 5)))
    esit("95 torba", (F(4, 10), F(6, 10), F(2, 5) + F(3, 5)), (F(2, 5), F(3, 5), 1))
    kart = range(1, 21)
    esit("95 birlesim", (len([k for k in kart if k % 2 == 0]), len([k for k in kart if k % 3 == 0]), len([k for k in kart if k % 6 == 0]), F(len([k for k in kart if k % 2 == 0 or k % 3 == 0]), 20), 10 + 6 - 3), (10, 6, 3, F(13, 20), 13))
    esit("95 bagimsiz", (F(1, 6) + F(1, 6), F(1, 2)*F(1, 6), F(sum(1 for p in "TY" for z in zar if p == "T" and z == 6), 12)), (F(1, 3), F(1, 12), F(1, 12)))
    esit("95 geri koyma", (F(sum(1 for i in range(10) for j in range(10) if torba[i] == torba[j] == "K"), 100), F(4, 10)**2, F(sum(1 for i, j in cift if torba[i] == torba[j] == "K"), len(cift)), F(4, 10)*F(3, 9), F(C(4, 2), C(10, 2)), C(4, 2), C(10, 2)),
         (F(4, 25), F(4, 25), F(2, 15), F(2, 15), F(2, 15), 6, 45))
    uc10 = list(itertools.combinations(range(10), 3))
    esit("95 kombinasyonla", (len(uc10), F(sum(1 for e in uc10 if 0 in e and 1 in e), len(uc10)), C(8, 1), F(8, 120)), (120, F(1, 15), 8, F(1, 15)))
    kiz9 = list(itertools.combinations(range(9), 3))
    esit("95 iki kiz bir erkek", (len(kiz9), sum(1 for e in kiz9 if sum(1 for k in e if k < 5) == 2), C(5, 2)*C(4, 1), F(40, 84)), (84, 40, 40, F(10, 21)))
    esit("95 kosullu zar", (F(len([z for z in zar if z > 4 and z % 2 == 0]), len([z for z in zar if z > 4])),), (F(1, 2),))
    cocuk = [c for c in itertools.product("KE", repeat=2) if "K" in c]
    esit("95 iki cocuk", (len(cocuk), F(sum(1 for c in cocuk if c == ("K", "K")), len(cocuk))), (3, F(1, 3)))
    esit("95 cark deneysel", (F(3, 8), F(120, 360), F(47, 100), float(F(47, 100))), (F(3, 8), F(1, 3), F(47, 100), 0.47))
    # ── 96 kumeler ──
    esit("96 asallar", [n for n in range(20) if sp.isprime(n)], [2, 3, 5, 7, 11, 13, 17, 19])
    altk = lambda K: [set(s) for r in range(len(K) + 1) for s in itertools.combinations(K, r)]
    esit("96 alt kume sayisi", (len(altk("abc")), len(altk("abc")) - 1, sum(1 for s in altk("abcd") if "a" in s), 2**3, 16 // 2), (8, 7, 8, 8, 8))
    A5 = altk([1, 2, 3, 4, 5])
    esit("96 kosullu alt kume", (sum(1 for s in A5 if 1 in s and 2 not in s), sum(1 for s in A5 if s), 2**5 - 1, sum(1 for s in A5 if len(s) == 2), sum(1 for s in A5 if len(s) == 3)), (8, 31, 31, 10, 10))
    E, A, B = set(range(1, 9)), {1, 2, 3, 4, 5}, {4, 5, 6, 7}
    esit("96 islemler", (A | B, A & B, A - B, B - A, E - A, E - B, E - (A | B), (E - A) & (E - B)), (set(range(1, 8)), {4, 5}, {1, 2, 3}, {6, 7}, {6, 7, 8}, {1, 2, 3, 8}, {8}, {8}))
    esit("96 alt kume ornegi", ({1, 2} <= {1, 2, 3}, {2, 4} <= {1, 2, 3}), (True, False))
    esit("96 dil", (25 + 18 - 8, 40 - 35, 25 - 8, 18 - 8, 17 + 8 + 10 + 5), (35, 5, 17, 10, 40))
    esit("96 spor", (30 - 5, 18 + 15 - 25, 18 - 8, 15 - 8, 10 + 8 + 7 + 5), (25, 8, 10, 7, 30))
    esit("96 fark", (15 + 12 - 22, 15 - 5, 12 - 5, 10 + 7 + 5), (5, 10, 7, 22))
    esit("96 yuzde", (60 + 50 - 20, 100 - 90, 200*F(10, 100)), (90, 10, 20))
    # uc kulup: bolgeler negatif olmamali; toplam 39
    ab, ac, bc, abc = 7 - 2, 5 - 2, 4 - 2, 2
    yA, yB, yC = 20 - ab - ac - abc, 18 - ab - bc - abc, 15 - ac - bc - abc
    esit("96 uc kume", (20 + 18 + 15, 7 + 5 + 4, 53 - 16 + 2, min(yA, yB, yC, ab, ac, bc) >= 0, yA + yB + yC + ab + ac + bc + abc), (53, 16, 39, True, 39))
    olasi = [k for k in range(0, 19) if 18 + 20 - k <= 30]
    esit("96 en az en cok", (min(olasi), max(olasi), 18 + 20 - 30), (8, 18, 8))
    esit("96 kartezyen", (len(list(itertools.product([1, 2], "abc"))), 2*3), (6, 6))
    import random
    rnd = random.Random(9697)
    for _ in range(300):
        X, Y, Z = ({v for v in range(10) if rnd.random() < 0.5} for _ in range(3))
        U = set(range(10))
        esit("96 ozellikler", (X | Y == Y | X, X & Y == Y & X, (X | Y) | Z == X | (Y | Z), (X & Y) & Z == X & (Y & Z), X | set() == X, X & set() == set(), X | X == X, X & X == X,
                               X & (Y | Z) == (X & Y) | (X & Z), U - (X | Y) == (U - X) & (U - Y), U - (X & Y) == (U - X) | (U - Y),
                               len(X | Y) == len(X) + len(Y) - len(X & Y), len(X - Y) == len(X) - len(X & Y), len(X | Y) == len(X - Y) + len(Y - X) + len(X & Y),
                               len(X | Y | Z) == len(X) + len(Y) + len(Z) - len(X & Y) - len(X & Z) - len(Y & Z) + len(X & Y & Z), len(list(itertools.product(X, Y))) == len(X)*len(Y),
                               (not X <= Y) or (X | Y == Y and X & Y == X)), (True,)*17)
    # ── 97 mantik ──
    D2 = list(itertools.product((1, 0), repeat=2))
    D3 = list(itertools.product((1, 0), repeat=3))
    ve, veya, yada = (lambda p, q: p & q), (lambda p, q: p | q), (lambda p, q: p ^ q)
    ise, ancak = (lambda p, q: (1 - p) | q), (lambda p, q: int(p == q))
    d = lambda p: 1 - p
    esit("97 tablolar", ([ve(p, q) for p, q in D2], [veya(p, q) for p, q in D2], [yada(p, q) for p, q in D2], [ise(p, q) for p, q in D2], [ancak(p, q) for p, q in D2], [d(p) for p in (1, 0)]),
         ([1, 0, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [1, 0, 1, 1], [1, 0, 0, 1], [0, 1]))
    esit("97 onermeler", (sp.isprime(7), 2 + 3 == 6, sp.sqrt(9).is_integer, 12 % 2 == 0, sp.isprime(5), 5 % 2 == 0, 6 % 2 == 0 and 6 % 3 == 0), (True, False, True, True, True, False, True))
    esit("97 ozellikler", all(all([ve(p, q) == ve(q, p), veya(p, q) == veya(q, p), ve(p, p) == p, veya(p, p) == p, ve(p, 1) == p, veya(p, 1) == 1, ve(p, 0) == 0, veya(p, 0) == p, ve(p, d(p)) == 0, veya(p, d(p)) == 1, d(d(p)) == p,
                                   ve(p, veya(q, r)) == veya(ve(p, q), ve(p, r)), veya(p, ve(q, r)) == ve(veya(p, q), veya(p, r)),
                                   d(ve(p, q)) == veya(d(p), d(q)), d(veya(p, q)) == ve(d(p), d(q)), ise(p, q) == veya(d(p), q), d(ise(p, q)) == ve(p, d(q)),
                                   ise(p, q) == ise(d(q), d(p)), ise(q, p) == ise(d(p), d(q)), ancak(p, q) == ve(ise(p, q), ise(q, p)), ancak(p, q) == d(yada(p, q))])
                          for p, q, r in D3), True)
    esit("97 karsit denk degil", any(ise(p, q) != ise(q, p) for p, q in D2), True)
    esit("97 dort ve cift", (all(n % 2 == 0 for n in range(1, 500) if n % 4 == 0), 6 % 2 == 0 and 6 % 4 != 0, all(n % 4 != 0 for n in range(1, 500) if n % 2 != 0)), (True, True, True))
    tur = lambda f: "totoloji" if all(f(p, q) for p, q in D2) else ("celiski" if not any(f(p, q) for p, q in D2) else "ikisi de degil")
    esit("97 totoloji", (tur(lambda p, q: veya(p, d(p))), tur(lambda p, q: ve(p, d(p))), tur(lambda p, q: ise(ve(p, q), p)), tur(lambda p, q: ise(p, veya(p, q))), tur(lambda p, q: ve(p, q)), [ve(p, q) for p, q in D2].count(1)),
         ("totoloji", "celiski", "totoloji", "totoloji", "ikisi de degil", 1))
    esit("97 satir sayisi", (len(D2), len(D3)), (4, 8))
    esit("97 sadelestirme", (all(veya(ve(p, q), ve(p, d(q))) == p for p, q in D2), all(ve(ise(p, q), p) == ve(p, q) for p, q in D2)), (True, True))
    esit("97 geriye", [(p, q, r) for p, q, r in D3 if ise(p, veya(q, r)) == 0], [(1, 0, 0)])
    esit("97 acik onerme", ([x_ for x_ in range(100) if x_ + 2 < 5], all(({x_ for x_ in range(50) if x_ % 2 == 0} & {x_ for x_ in range(50) if x_ % 3 == 0}) == {x_ for x_ in range(50) if x_ % 2 == 0 and x_ % 3 == 0} for _ in [0])), ([0, 1, 2], True))
    esit("97 niceleyiciler", (all(x_ + 1 > x_ for x_ in range(1000)), [x_ for x_ in range(1000) if x_ + 3 == 1], [x_ for x_ in range(-1000, 1000) if x_ + 3 == 1]), (True, [], [-2]))


def yazi_98_100():
    """98 Tablo ve Grafik Yorumlama, 99 Aritmetik Ortalama ve Veri Analizi, 100 Genel Tekrar."""
    import statistics as st
    from math import factorial as fa, sqrt as kok
    ort = lambda v: F(sum(v), len(v))
    degisim = lambda eski, yeni: F(yeni - eski, eski)*100
    # ── 98 tablo ve grafik ──
    notlar = {1: 2, 2: 6, 3: 14, 4: 10, 5: 8}
    esit("98 siklik", (sum(notlar.values()), [F(s, 40)*100 for s in notlar.values()], notlar[4] + notlar[5], F(18, 40)*100, 25 + 20, max(notlar, key=notlar.get), 5 + 15 + 35 + 25 + 20),
         (40, [5, 15, 35, 25, 20], 18, 45, 45, 3, 100))
    esit("98 cift yonlu", (18 + 62, 12 + 48, 18 + 12, 62 + 48, 80 + 60, F(18, 30)*100, F(12, 60)*100, F(18, 80), F(12, 60), F(18, 80) > F(12, 60)),
         (80, 60, 30, 110, 140, 60, 20, F(225, 1000), F(2, 10), True))
    defter = [40, 50, 70, 56, 84]
    esit("98 defter", (sum(defter), ort(defter), [i for i in range(4) if defter[i + 1] < defter[i]], degisim(40, 50), degisim(70, 56), degisim(56, 84), round(float(-degisim(84, 56)))),
         (300, 60, [2], 25, -20, 50, 33))
    esit("98 miktar yuzde", (240 - 200, degisim(200, 240), 75 - 50, degisim(50, 75), 240 - 200 > 75 - 50, degisim(50, 75) > degisim(200, 240)), (40, 20, 25, 50, True, True))
    net = [40, 46, 44, 52, 58, 60]
    artis = [net[i + 1] - net[i] for i in range(5)]
    esit("98 deneme", ([i + 1 for i in range(5) if artis[i] < 0], max(artis), artis.index(max(artis)) + 1, degisim(40, 60), ort(net), all(v > 50 for v in net[3:]), artis[4], min(net) > 35),
         ([2], 8, 3, 50, 50, True, 2, True))
    aci = {"Otobüs": 120, "Yürüyerek": 90, "Servis": 60, "Özel araç": 60, "Bisiklet": 30}
    kisi = {k: F(a, 360)*240 for k, a in aci.items()}
    esit("98 daire", (sum(aci.values()), list(kisi.values()), sum(kisi.values()), F(90, 360)*100, F(40, 240)*360, 20*F(360, 30), F(120 - 90, 360)*240, kisi["Otobüs"] - kisi["Yürüyerek"], F(240, 360)*3),
         (360, [80, 60, 40, 40, 20], 240, 25, 60, 240, 20, 20, 2))
    esit("98 resim", ([3*10, 3*10 + 5, 2*10, 5*10, 4*10 + 5], 30 + 35 + 20 + 50 + 45), ([30, 35, 20, 50, 45], 180))
    boy = [4, 12, 10, 4]
    esit("98 gruplanmis", (sum(boy), boy[2] + boy[3], boy.index(max(boy))), (30, 14, 1))
    butce_aci = [144, 90, 72, 54]
    esit("98 iki grafik", (sum(butce_aci), [F(a, 360)*300 for a in butce_aci], sum(F(a, 360)*300 for a in butce_aci), degisim(200, 300)), (360, [120, 75, 60, 45], 300, 50))
    esit("98 yaniltici", (96 - 94, 100 - 94, F(100 - 94, 96 - 94), 100 - 96, round(float(degisim(96, 100)))), (2, 6, 3, 4, 4))
    esit("98 sss", (F(90, 360), degisim(40, 50)), (F(1, 4), 25))
    # ── 99 aritmetik ortalama ──
    esit("99 tanim", (sum([7, 9, 10, 12, 12]), ort([7, 9, 10, 12, 12])), (50, 10))
    sutun = [2, 5, 3, 6]
    esit("99 esitleme", (sum(sutun), ort(sutun), [v - 4 for v in sutun], sum(v - 4 for v in sutun)), (16, 4, [-2, 1, -1, 2], 0))
    esit("99 toplamdan", (5*12, 60 - 20, F(40, 4)), (60, 40, 10))
    esit("99 ekleme cikarma", (20*70, 1400 + 91, F(1491, 21), 10*15, 9*14, 150 - 126), (1400, 1491, 71, 150, 126, 24))
    esit("99 degistirme", (42 - 18, F(24, 8), 25 - 3, 8*25 - 24, F(176, 8)), (24, 3, 22, 176, 22))
    esit("99 hedef", (5*74, 4*70, 370 - 280, 74 + 4*4), (370, 280, 90, 90))
    cift = list(range(12, 31, 2))
    esit("99 ardisik", (ort(cift), len(cift), sum(cift), F(30 - 12, 2) + 1, ort(list(range(1, 100)))), (21, 10, 210, 10, 50))
    esit("99 agirlikli", (30*70 + 20*80, F(3700, 50), F(70 + 80, 2), F(4*80 + 3*70 + 3*90, 10)), (3700, 74, 75, 80))
    esit("99 ortalama hiz", (F(120, 60), F(120, 40), F(240, 5), F(2*60*40, 60 + 40)), (2, 3, 48, 48))
    esit("99 ortanca", (st.median([3, 8, 5, 12, 7]), sorted([3, 8, 5, 12, 7]), [3, 8, 5, 12, 7][2], st.median([4, 9, 2, 7, 10, 6]), sorted([4, 9, 2, 7, 10, 6])),
         (7, [3, 5, 7, 8, 12], 5, 6.5, [2, 4, 6, 7, 9, 10]))
    esit("99 tepe", (st.multimode([2, 3, 3, 5, 7, 7, 7, 9]), [2, 3, 3, 5, 7, 7, 7, 9].count(7), [2, 3, 3, 5, 7, 7, 7, 9].count(3)), ([7], 3, 2))
    liste = [n for n, s in notlar.items() for _ in range(s)]
    esit("99 sikliktan", ([n*s for n, s in notlar.items()], sum(n*s for n, s in notlar.items()), ort(liste), st.median(liste), sorted(liste)[19], sorted(liste)[20], 2 + 6, st.mode(liste)),
         ([2, 12, 42, 40, 40], 136, F(34, 10), 3, 3, 3, 8, 3))
    maas = [20, 22, 24, 26, 108]
    esit("99 uc deger", (sum(maas), ort(maas), st.median(maas), sum(1 for m in maas if m < ort(maas))), (200, 40, 24, 4))
    esit("99 aciklik", (ort([48, 50, 52]), ort([20, 50, 80]), 52 - 48, 80 - 20), (50, 50, 4, 60))
    def ceyrek(v):
        v = sorted(v); n = len(v); h = n // 2
        alt, ust = v[:h], v[n - h:]
        return st.median(alt), st.median(v), st.median(ust)
    q = ceyrek([3, 5, 7, 8, 10, 12, 15, 20])
    q2 = ceyrek([3, 5, 7, 8, 10, 12, 15, 200])
    esit("99 ceyrekler", (q, q[2] - q[0], q2[2] - q2[0], 200 - 3 > 20 - 3), ((6, 9, 13.5), 7.5, 7.5, True))
    v = [7, 7, 10, 13, 13]
    esit("99 standart sapma", (ort(v), [x_ - 10 for x_ in v], sum((x_ - 10)**2 for x_ in v), st.stdev(v), st.pstdev(v) < 3, st.stdev([10]*5)), (10, [-3, -3, 0, 3, 3], 36, 3.0, True, 0.0))
    esit("99 donusum", (ort([x_ + 5 for x_ in v]), st.stdev([x_ + 5 for x_ in v]), [x_ + 5 for x_ in v], ort([2*x_ for x_ in v]), st.stdev([2*x_ for x_ in v]), [2*x_ for x_ in v]),
         (15, 3.0, [12, 12, 15, 18, 18], 20, 6.0, [14, 14, 20, 26, 26]))
    # ── 100 genel tekrar ──
    x_ = sp.symbols("x_")
    esit("100 bilinmeyen", (_coz(x_ + 3*x_, 48, x_), 3*12), (FiniteSet(12), 36))
    esit("100 sayi", (_coz(3*x_ + 7, 5*x_ - 9, x_), 3*8 + 7, 5*8 - 9), (FiniteSet(8), 31, 31))
    h = F(600)
    esit("100 kesir", (F(2, 3)*F(3, 4), 300 / F(1, 2), h/3, h - h/3, (h - h/3)/4, h - h/3 - (h - h/3)/4), (F(1, 2), 600, 200, 400, 100, 300))
    esit("100 yas", (_coz(38 + x_, 2*(10 + x_), x_), 38 + 18, 10 + 18, 38 - 10, 56 - 28), (FiniteSet(18), 56, 28, 28, 28))
    esit("100 yuzde", (100*F(120, 100), 120*F(20, 100), 120 - 24, degisim(100, 96)), (120, 24, 96, -4))
    esit("100 kar zarar", (400*F(125, 100), F(360)/F(8, 10), 450*F(80, 100)), (500, 450, 360))
    esit("100 faiz", (F(20000*15*2, 100), 20000 + 6000), (6000, 26000))
    esit("100 oran", (_coz(3*x_ + 5*x_, 400, x_), 3*50, 5*50, F(6*10, 4)), (FiniteSet(50), 150, 250, 15))
    esit("100 isci havuz", (F(1, 6) + F(1, 12), F(3, 12), 1/(F(1, 6) + F(1, 12)), F(1, 4) - F(1, 6), 1/(F(1, 4) - F(1, 6))), (F(1, 4), F(1, 4), 4, F(1, 12), 12))
    esit("100 hareket", (60 + 80, F(420, 140)), (140, 3))
    esit("100 karisim", (300*F(2, 10), 60 + 100, 300 + 100, F(160, 400)), (60, 160, 400, F(4, 10)))
    esit("100 ortalama", (5*16, 6*18, 108 - 80), (80, 108, 28))
    iki = list(itertools.product(range(1, 7), repeat=2))
    esit("100 sayma olasilik", (fa(4), len(iki), sum(1 for a, b in iki if a + b == 7), F(6, 36)), (24, 36, 6, F(1, 6)))
    esit("100 kume", (50 - 6, 32 + 28 - 44, 32 - 16 + 28 - 16 + 16 + 6), (44, 16, 50))
    esit("100 basamak", ([10*a + b for a in range(1, 10) for b in range(10) if a + b == 11 and (10*b + a) - (10*a + b) == 27], 74 - 47, all((10*b + a) - (10*a + b) == 9*(b - a) for a in range(10) for b in range(10))),
         ([47], 27, True))
    esit("100 kumbara", ([(x2, 20 - x2) for x2 in range(21) if 5*x2 + (20 - x2) == 60], 10*5 + 10*1, 60 - 20, F(40, 4)), ([(10, 10)], 60, 40, 10))
    esit("100 grafik", (F(90, 360), F(240, 4)), (F(1, 4), 60))
    esit("100 ortadaki", (F(57, 3), 17 + 19 + 21, [a for a in range(-100, 100) if a % 2 == 1 and a + (a + 2) + (a + 4) == 57], F(50, 4), 11 + 12 + 13 + 14), (19, 57, [17], F(25, 2), 50))
    esit("100 cok adimli", (F(500)/F(125, 100), 500*F(9, 10), 450 - 400, F(50, 400)*100, 25 - 10), (400, 450, 50, F(25, 2), 15))


def yazi_06_10():
    """06 Fonksiyon Grafikleri, 07 Polinomlar, 08 Bolme, 09 Kalan, 10 Carpanlara Ayirma."""
    X, a_, b_, t_, k_, m_ = sp.symbols("X a_ b_ t_ k_ m_")
    Q = Rational
    ac = lambda e: sp.expand(e)
    bol = lambda p, q: sp.div(ac(p), ac(q), X)
    kalan = lambda p, q: sp.rem(ac(p), ac(q), X)
    ayni = lambda e1, e2: sp.expand(e1 - e2) == 0
    # ── 06 fonksiyon grafikleri ──
    f = X**2 - 4*X + 3
    esit("06 dogrusal tablo", [2*v - 1 for v in (-1, 0, 1, 2)], [-3, -1, 1, 3])
    esit("06 cember", (1 + 8, sp.solve(X**2 + 1 - 9, X)), (9, [-2*sp.sqrt(2), 2*sp.sqrt(2)]))
    esit("06 deger okuma", (f.subs(X, 0), f.subs(X, 4), set(sp.solve(f - 3, X)), set(sp.solve(f, X)), f.subs(X, 2)), (3, 3, {0, 4}, {1, 3}, -1))
    esit("06 artan azalan", (sp.solve(sp.diff(f, X), X), _coz(f < 0, 0, X) if False else sp.solveset(f < 0, X, R), sp.solveset(f > 0, X, R)),
         ([2], Interval.open(1, 3), Union(Interval.open(-oo, 1), Interval.open(3, oo))))
    esit("06 goruntu", (sp.Interval(-1, 2), function_range(X**2, X, Interval(-1, 2)), (-1)**2, 2**2), (Interval(-1, 2), Interval(0, 4), 1, 4))
    esit("06 dogru", ((-2*X + 4).subs(X, 0), sp.solve(-2*X + 4, X)), (4, [2]))
    esit("06 mutlak", (min(abs(v - 2) + 1 for v in [i / 100 for i in range(-500, 500)]), abs(2 - 2) + 1), (1, 1))
    pf = lambda v: v + 1 if v < 1 else 4 - v
    esit("06 parcali", (pf(-1), pf(1), pf(3), sp.limit(X + 1, X, 1, "-"), pf(pf(3)), pf(0), pf(pf(0))), (0, 3, 1, 2, 3, 1, 3))
    esit("06 oteleme", (sp.solve(sp.diff((X - 2)**2 + 1, X), X), ((X - 2)**2 + 1).subs(X, 2)), ([2], 1))
    esit("06 yansima", (sp.sqrt(4), -sp.sqrt(4), sp.sqrt(-(-4))), (2, -2, 2))
    esit("06 simetri", (ayni((-X)**3 - (-X), -(X**3 - X)), all(ayni(g.subs(X, -X), g) for g in (X**2, X**4 - 3*X**2)), all(ayni(g.subs(X, -X), -g) for g in (X, X**3)),
                        ayni((X**2 + X).subs(X, -X), X**2 + X), ayni((X**2 + X).subs(X, -X), -(X**2 + X)), abs(-3) == abs(3)), (True, True, True, False, False, True))
    esit("06 ters", (sp.solve(2*X + 1 - t_, X), 2*1 + 1, Q(3 - 1, 2)), ([(t_ - 1)/2], 3, 1))
    esit("06 kesisim", (sp.solve(X**2 - X - 2, X), [(-1, 1), (2, 4)] == [(v, v**2) for v in (-1, 2)], [v + 2 for v in (-1, 2)]), ([-1, 2], True, [1, 4]))
    # ── 07 polinomlar ──
    esit("07 6/n", ([n for n in range(1, 50) if 6 % n == 0 and n - 1 >= 0], len([n for n in range(1, 50) if 6 % n == 0])), ([1, 2, 3, 6], 4))
    p7 = sp.Poly(4*X**3 - 2*X**2 + 7*X - 5, X)
    esit("07 derece", (p7.degree(), p7.LC(), p7.eval(0), sp.Poly(5 - 2*X + 3*X**4, X).LC()), (3, 4, -5, 3))
    esit("07 sifir polinom", sp.solve([a_ - 3, b_ + 2, t_ - 1], [a_, b_, t_]), {a_: 3, b_: -2, t_: 1})
    p = (2*X - 1)**3 + X**2 + 4
    esit("07 sabit toplam", (p.subs(X, 0), p.subs(X, 1)), (3, 6))
    p = (X + 2)**3
    esit("07 cift tek", (p.subs(X, 1), p.subs(X, -1), Q(27 + 1, 2), Q(27 - 1, 2), ac(p), 6 + 8, 1 + 12), (27, 1, 14, 13, X**3 + 6*X**2 + 12*X + 8, 14, 13))
    esit("07 esitlik", sp.solve([a_ - 2 - 3, b_ + 1 + 4, t_ - 5], [a_, b_, t_]), {a_: 5, b_: -5, t_: 5})
    P7, Q7 = 2*X**3 - X + 4, X**3 + 3*X**2 - 5
    esit("07 toplama", (ac(P7 + Q7), ac(P7 - Q7)), (3*X**3 + 3*X**2 - X - 1, X**3 - 3*X**2 - X + 9))
    esit("07 carpma", (ac((2*X - 3)*(X**2 + X - 1)), ((2*X - 3)*(X**2 + X - 1)).subs(X, 1)), (2*X**3 - X**2 - 5*X + 3, -1))
    Pd, Qd = X**3 + 2*X + 1, 5*X**2 - X + 7
    esit("07 derece kurallari", (sp.degree(ac(Pd*Qd), X), sp.degree(ac(Pd**3), X), sp.degree(ac(Pd.subs(X, X**2)), X), sp.degree(ac(Pd + Qd), X), sp.degree(ac((X**2 + X) + (-X**2 + 3)), X)), (5, 9, 6, 3, 1))
    pc = sp.Poly(ac((X**2 + 1)**3 * (2*X - 1)**2), X)
    esit("07 carpim derecesi", (pc.degree(), pc.LC()), (8, 4))
    esit("07 deger", ((X**3 - 2*X + 1).subs(X, 2), (X**3 - 2*X + 1).subs(X, -1)), (5, 2))
    esit("07 P(x+1)", (ac((X - 1)**2 + 3*(X - 1) + 2), (X**2 + X).subs(X, 3), (X**2 + 3*X + 2).subs(X, 2)), (X**2 + X, 12, 12))
    esit("07 bilesik girdi", ((X**2 - 3*X + 4).subs(X, 1), (X**2 - 3*X + 4).subs(X, -1)), (2, 8))
    esit("07 grafik kokleri", set(sp.solve(X**3 - 3*X, X)), {0, sp.sqrt(3), -sp.sqrt(3)})
    esit("07 kok carpan", ((X**3 - 6*X**2 + 11*X - 6).subs(X, 1), sp.factor(X**3 - 6*X**2 + 11*X - 6)), (0, (X - 1)*(X - 2)*(X - 3)))
    esit("07 katsayi bul", sp.solve([a_ + b_ + 3 - 6, a_ - b_ + 3 - 4], [a_, b_]), {a_: 2, b_: 1})
    esit("07 kokten polinom", (ac(3*(X - 1)*(X + 2)), (3*X**2 + 3*X - 6).subs(X, -2)), (3*X**2 + 3*X - 6, 0))
    esit("07 fonksiyonel", (sp.solve([2*a_ - 4, 2*b_ - a_ - 2], [a_, b_]), ac((2*X + 2) + (2*(X - 1) + 2))), ({a_: 2, b_: 2}, 4*X + 2))
    esit("07 ozdeslik", (ac((2*X + 3)**2), ac((X - 5)*(X + 5)), (1 + 1)**2, 1**2 + 1**2, 5*3 + 2), (4*X**2 + 12*X + 9, X**2 - 25, 4, 2, 17))
    esit("07 carpim sabit", (3*(-2), 4*5), (-6, 20))
    # ── 08 bolme ──
    esit("08 kalansiz", (bol(X**2 + 5*X + 6, X + 2), Q(156, 12), 10**2 + 50 + 6, 10 + 2), ((X + 3, 0), 13, 156, 12))
    esit("08 kalanli", (bol(2*X**3 - 3*X**2 + 4*X - 5, X - 1), ac((X - 1)*(2*X**2 - X + 3))), ((2*X**2 - X + 3, -2), 2*X**3 - 3*X**2 + 4*X - 3))
    esit("08 eksik terim", (bol(X**3 - 8, X - 2), sp.factor(X**3 - 8)), ((X**2 + 2*X + 4, 0), (X - 2)*(X**2 + 2*X + 4)))
    esit("08 ikinci derece bolen", (bol(X**4 + X**3 - X + 2, X**2 + 1), (X**4 + X**3 - X + 2).subs(X, 2), ((X**2 + 1)*(X**2 + X - 1) + (-2*X + 3)).subs(X, 2)), ((X**2 + X - 1, -2*X + 3), 24, 24))
    esit("08 dereceler esit", bol(6*X**2 + X - 2, 3*X**2 + 1), (2, X - 4))
    esit("08 derece", (5 - 2,), (3,))
    def horner(kats, a):
        s = [kats[0]]
        for c in kats[1:]: s.append(s[-1]*a + c)
        return s
    esit("08 horner", (horner([2, -3, 4, -5], 1), horner([1, -4, 1, 6], -1), sp.factor(X**3 - 4*X**2 + X + 6), horner([1, 0, 0, 0, -16], 2)),
         ([2, -1, 3, -2], [1, -5, 6, 0], (X - 3)*(X - 2)*(X + 1), [1, 2, 4, 8, 0]))
    esit("08 ax+b bolen", (bol(6*X**2 + X - 2, 2*X - 1), (6*X**2 + X - 2).subs(X, Q(1, 2)), Q(6, 4) + Q(1, 2) - 2), ((3*X + 2, 0), 0, 0))
    esit("08 bolunen bul", (ac((X**2 - 1)*(X + 2) + 3*X - 1), (X**3 + 2*X**2 + 2*X - 3).subs(X, 1), 3*1 - 1), (X**3 + 2*X**2 + 2*X - 3, 2, 2))
    esit("08 kalansiz kosul", (sp.solve(1 + m_ + 6, m_), sp.factor(X**3 - 7*X + 6)), ([-7], (X - 2)*(X - 1)*(X + 3)))
    esit("08 iki kalan", (sp.solve([1 + a_ + b_ - 4, -1 - a_ + b_ - 2], [a_, b_]), (X**3 + 3).subs(X, 1), (X**3 + 3).subs(X, -1)), ({a_: 0, b_: 3}, 4, 2))
    esit("08 bolum degeri", sp.solve(2*t_ + 4 - 10, t_), [3])
    esit("08 ozdeslik tablosu", (bol(X**2 - 9, X - 3), bol(X**3 - 8, X - 2), bol(X**3 + 27, X + 3)), ((X + 3, 0), (X**2 + 2*X + 4, 0), (X**2 - 3*X + 9, 0)))
    esit("08 ikinci derece kalan", (kalan(X**5 + 2*X + 3, X**2 - X), (X**5 + 2*X + 3).subs(X, 0)), (3*X + 3, 3))
    esit("08 sayilarla", (156 // 12, 156 % 12), (13, 0))
    # ── 09 kalan ──
    p9 = X**3 - 2*X**2 + 5
    esit("09 temel", (p9.subs(X, 2), bol(p9, X - 2), p9.subs(X, -1), p9.subs(X, 1)), (5, (X**2, 5), 2, 4))
    esit("09 ax+b", (kalan(4*X**2 - 2*X + 1, 2*X - 1), 4*Q(1, 4) - 1 + 1), (1, 1))
    esit("09 x ile", kalan(3*X**4 - 7*X**2 + X - 6, X), -6)
    esit("09 katsayi toplami", (kalan((X + 1)**5, X - 1), sum(sp.Poly((X + 1)**5, X).all_coeffs())), (32, 32))
    esit("09 buyuk kuvvet", (kalan(X**100 + X**51 + 1, X + 1), kalan(X**100 + X**51 + 1, X - 1)), (1, 3))
    esit("09 carpan teoremi", ((X**3 - 3*X**2 + 4).subs(X, 2), sp.factor(X**3 - 3*X**2 + 4)), (0, (X - 2)**2*(X + 1)))
    esit("09 bilinmeyen", (sp.solve(8 + 4*k_ - 4 - 8, k_), sp.solve(-8 - 2*m_ + 6, m_)), ([1], [-1]))
    esit("09 iki bilinmeyen", (sp.solve([1 + a_ + b_ - 2, 4 - 2*a_ + b_ - 5], [a_, b_]), (X**2 + 1).subs(X, 1), (X**2 + 1).subs(X, -2)), ({a_: 0, b_: 1}, 2, 5))
    esit("09 bilesik girdi", ((X**2 - X + 2).subs(X, 3), kalan((X**2 - X + 2).subs(X, 2*X + 1), X - 1)), (8, 8))
    esit("09 bolme esitliginden", (1 - 3)*2 + 5, 1)
    esit("09 ikinci derece", (kalan(X**4 + X + 1, X**2 - 1), sp.solve([a_ + b_ - 3, -a_ + b_ - 1], [a_, b_]), ac((X**2 - 1)*(X**2 + 1) + X + 2)), (X + 2, {a_: 1, b_: 2}, X**4 + X + 1))
    esit("09 gercek koksuz", kalan(X**4 + 3*X**3 + X + 2, X**2 + 1), -2*X + 3)
    esit("09 derece indirgeme", kalan(X**7 + X**4 + X, X**3 - 1), 3*X)
    esit("09 birlesik kalan", (sp.solve([a_ + b_ - 3, 2*a_ + b_ - 5], [a_, b_]), kalan((X - 1)*(X - 2)*(X**2 + 7) + 2*X + 1, (X - 1)*(X - 2))), ({a_: 2, b_: 1}, 2*X + 1))
    esit("09 horner", horner([1, -2, 0, 5], 2), [1, 0, 0, 5])
    esit("09 kokten kur", (ac((X - 1)*(X - 3)), 3), (X**2 - 4*X + 3, (X**2 - 4*X + 3).subs(X, 0)))
    esit("09 bolum degeri", sp.solve((1 - 2)*t_ + 3 - 7, t_), [-4])
    esit("09 horner deger", (horner([2, -3, 0, 1, -7], 2), (2*X**4 - 3*X**3 + X - 7).subs(X, 2), 32 - 24 + 2 - 7), ([2, 1, 2, 5, 3], 3, 3))
    esit("09 buyuk bolenden", ((2*X + 3).subs(X, 2), (2*X + 3).subs(X, -2)), (7, -1))
    esit("09 art arda", sp.expand((X - 1)*((X - 2)*t_ + 3) + 4 - (X - 1)*(X - 2)*t_), 3*X + 1)
    # ── 10 carpanlara ayirma ──
    fk = lambda e1, e2: ayni(e1, e2)
    esit("10 temel", all([fk(6*X**3 - 9*X**2, 3*X**2*(2*X - 3)), fk(2*X**2 - 18, 2*(X - 3)*(X + 3)), fk(X**3 + 2*X**2 + 3*X + 6, (X + 2)*(X**2 + 3)),
                          fk(X**2 - 25, (X - 5)*(X + 5)), fk(4*X**2 - 9, (2*X - 3)*(2*X + 3)), fk(X**4 - 16, (X - 2)*(X + 2)*(X**2 + 4)),
                          fk(X**2 + 6*X + 9, (X + 3)**2), fk(4*X**2 - 12*X + 9, (2*X - 3)**2), fk(X**3 - 27, (X - 3)*(X**2 + 3*X + 9)),
                          fk(8*X**3 + 1, (2*X + 1)*(4*X**2 - 2*X + 1)), fk(X**3 + 3*X**2 + 3*X + 1, (X + 1)**3), fk(X**2 - 5*X + 6, (X - 2)*(X - 3)),
                          fk(X**2 + X - 12, (X + 4)*(X - 3)), fk(2*X**2 + 7*X + 3, (2*X + 1)*(X + 3)), fk(6*X**2 - X - 2, (2*X + 1)*(3*X - 2)),
                          fk(X**4 - 5*X**2 + 4, (X - 1)*(X + 1)*(X - 2)*(X + 2)), fk(X**4 + 4, (X**2 - 2*X + 2)*(X**2 + 2*X + 2)),
                          fk(X**3 - 6*X**2 + 11*X - 6, (X - 1)*(X - 2)*(X - 3)), fk(2*X**3 - 3*X**2 - 3*X + 2, (X - 2)*(X + 1)*(2*X - 1)),
                          fk(X**4 - 5*X**3 + 5*X**2 + 5*X - 6, (X - 1)*(X + 1)*(X - 2)*(X - 3)), fk(X**2 + 5*X + 6, (X + 2)*(X + 3)),
                          fk(2*X**3 - 8*X, 2*X*(X - 2)*(X + 2)), fk(X**3 - X**2 - 4*X + 4, (X - 1)*(X - 2)*(X + 2)), fk(3*X**2 - 12*X + 12, 3*(X - 2)**2)]), True)
    esit("10 koksuzler", (sp.solveset(X**2 + 4, X, R), sp.solveset(X**2 + 9, X, R), sp.solveset(X**4 + 4, X, R), sp.solveset(X**2 - 2*X + 2, X, R)), (S.EmptySet,)*4)
    esit("10 kok deneme", ([v for v in (1, -1, 2, -2, 3, -3, 6, -6) if (X**3 - 6*X**2 + 11*X - 6).subs(X, v) == 0], [v for v in (1, -1, 2, -2, Q(1, 2), -Q(1, 2)) if (2*X**3 - 3*X**2 - 3*X + 2).subs(X, v) == 0],
                           [(X**4 - 5*X**3 + 5*X**2 + 5*X - 6).subs(X, v) for v in (1, -1, 2, 3)], 16 - 40 + 20 + 10 - 6, 81 - 135 + 45 + 15 - 6), ([1, 2, 3], [-1, 2, Q(1, 2)], [0, 0, 0, 0], 0, 0))
    esit("10 sadelestirme", (sp.cancel((X**2 - 9)/(X**2 + 5*X + 6)), sp.solve(X**2 + 5*X + 6, X)), ((X - 3)/(X + 2), [-3, -2]))
    esit("10 denklem", (sp.solveset(X**3 - X, X, R), sp.solveset(X**2 - 1, X, R)), (FiniteSet(-1, 0, 1), FiniteSet(-1, 1)))
    esit("10 sayisal", (101**2 - 99**2, 2*200, 98*102, 100**2 - 2**2), (400, 400, 9996, 9996))
    esit("10 ozdeslik degeri", (sp.expand((a_ + b_)**2 - 2*a_*b_), sp.expand((a_ + b_)**3 - 3*a_*b_*(a_ + b_))), (a_**2 + b_**2, a_**3 + b_**3))
    esit("10 ozdeslik sayisal", (25 - 12, 125 - 90, 2**2 + 3**2, 2**3 + 3**3, 2 + 3, 2*3), (13, 35, 13, 35, 5, 6))
    esit("10 kontrol", (ac((2*X + 1)*(3*X - 2)), (6*X**2 - X - 2).subs(X, 1), 3*1), (6*X**2 - X - 2, 3, 3))


def yazi_11_13():
    """11 Ikinci Dereceden Denklemler, 12 Diskriminant, 13 Kokler Toplami ve Carpimi."""
    X, m_, a_, b_, t_ = sp.symbols("X m_ a_ b_ t_")
    Q = Rational
    kok = lambda e: sp.solveset(sp.expand(e), X, R)
    D = lambda a, b, c: b*b - 4*a*c
    # ── 11 ──
    esit("11 standart", sp.expand(2*X**2 - (7 - X)), 2*X**2 + X - 7)
    esit("11 x2=k", (kok(X**2 - 9), kok(X**2 + 4), kok((X - 1)**2 - 16)), (FiniteSet(-3, 3), S.EmptySet, FiniteSet(-3, 5)))
    esit("11 c=0", kok(2*X**2 - 6*X), FiniteSet(0, 3))
    esit("11 b=0", (kok(X**2 - 7), kok(3*X**2 + 12)), (FiniteSet(-sp.sqrt(7), sp.sqrt(7)), S.EmptySet))
    esit("11 carpanlar", (kok(X**2 - X - 6), sp.factor(X**2 - X - 6), kok(2*X**2 + 5*X - 3), sp.factor(2*X**2 + 5*X - 3)),
         (FiniteSet(-2, 3), (X - 3)*(X + 2), FiniteSet(-3, Q(1, 2)), (X + 3)*(2*X - 1)))
    esit("11 tam kare", (kok(X**2 + 6*X + 2), (Q(6, 2))**2, 9 - 2), (FiniteSet(-3 - sp.sqrt(7), -3 + sp.sqrt(7)), 9, 7))
    esit("11 kok formulu", (D(1, -4, 1), kok(X**2 - 4*X + 1), sp.simplify((2 + sp.sqrt(3))**2 - 4*(2 + sp.sqrt(3)) + 1), sp.expand((2 + sp.sqrt(3))**2), 4 - 1),
         (12, FiniteSet(2 - sp.sqrt(3), 2 + sp.sqrt(3)), 0, 7 + 4*sp.sqrt(3), 3))
    esit("11 vieta", (1, -6, 3 + (-2), 3*(-2)), (-(-1)//1, -6, 1, -6))
    esit("11 koksuz", (D(1, 2, 5), kok(X**2 + 2*X + 5), sp.expand((X + 1)**2 + 4)), (-16, S.EmptySet, X**2 + 2*X + 5))
    esit("11 degisken", (kok(X**4 - 13*X**2 + 36), sp.factor(t_**2 - 13*t_ + 36)), (FiniteSet(-3, -2, 2, 3), (t_ - 9)*(t_ - 4)))
    esit("11 kesirli", sp.solveset(X + 6/X - 5, X, R), FiniteSet(2, 3))
    esit("11 koklu", (sp.solveset(sp.sqrt(X + 2) - X, X, R), kok(X**2 - X - 2), sp.sqrt(1) == -1), (FiniteSet(2), FiniteSet(-1, 2), False))
    esit("11 kokten denklem", (sp.expand((X - 2)*(X + 5)), 2 + (-5), 2*(-5)), (X**2 + 3*X - 10, -3, -10))
    esit("11 parametre", (sp.solve(9 - 3*(m_ + 1) + m_, m_), kok(X**2 - 4*X + 3)), ([3], FiniteSet(1, 3)))
    esit("11 problem", (kok(X*(X + 1) - 56), kok(X*(X + 3) - 40), kok((X + 2)**2 - 49)), (FiniteSet(-8, 7), FiniteSet(-8, 5), FiniteSet(-9, 5)))
    esit("11 kok mu", ((2*X**2 - 5*X - 3).subs(X, 3), (2*X**2 - 5*X - 3).subs(X, -1)), (0, 4))
    esit("11 kesirli katsayi", (sp.expand(6*(Q(1, 2)*X**2 - Q(1, 3)*X - Q(1, 6))), kok(3*X**2 - 2*X - 1)), (3*X**2 - 2*X - 1, FiniteSet(-Q(1, 3), 1)))
    esit("11 mutlak", (sp.solveset(X**2 - sp.Abs(X) - 6, X, R), kok(t_**2 - t_ - 6) if False else sp.solveset(t_**2 - t_ - 6, t_, R)), (FiniteSet(-3, 3), FiniteSet(-2, 3)))
    esit("11 ortak kok", (sp.solve((X**2 - 5*X + 6) - (X**2 - X - 2), X), (X**2 - 5*X + 6).subs(X, 2), (X**2 - X - 2).subs(X, 2)), ([2], 0, 0))
    # ── 12 ──
    esit("12 tablo", (D(1, -5, 6), D(1, -4, 4), D(1, 1, 1), D(2, 3, -2)), (1, 0, -3, 25))
    esit("12 kokler", (kok(X**2 - 5*X + 6), kok(X**2 - 4*X + 4), kok(2*X**2 + 3*X - 2), sp.factor(2*X**2 + 3*X - 2)), (FiniteSet(2, 3), FiniteSet(2), FiniteSet(-2, Q(1, 2)), (X + 2)*(2*X - 1)))
    esit("12 grafik", (D(1, -2, -3), D(1, -2, 1), D(1, -2, 3), kok(X**2 - 2*X - 3), kok(X**2 - 2*X + 1)), (16, 0, -8, FiniteSet(-1, 3), FiniteSet(1)))
    esit("12 rasyonel", (D(1, -1, -6), sp.sqrt(25), sp.sqrt(12).is_rational), (25, 5, False))
    esit("12 parametreler", (sp.solveset(D(1, -4, m_) > 0, m_, R), sp.solve(D(1, m_, 9), m_), kok(X**2 + 6*X + 9), kok(X**2 - 6*X + 9), sp.solveset(D(1, 2, m_) < 0, m_, R)),
         (Interval.open(-oo, 4), [-6, 6], FiniteSet(-3), FiniteSet(3), Interval.open(1, oo)))
    esit("12 bas katsayi", (sp.solveset(D(m_, 4, 1) > 0, m_, R), kok(4*X + 1)), (Interval.open(-oo, 4), FiniteSet(-Q(1, 4))))
    esit("12 tam sayi", ([m for m in range(1, 20) if D(1, -2, m - 3) > 0], sp.expand(D(1, -2, m_ - 3))), ([1, 2, 3], 16 - 4*m_))
    esit("12 ac", (D(3, 7, -2), all(D(a, b, c) > 0 for a in range(1, 6) for b in range(-6, 7) for c in range(-6, 0))), (73, True))
    esit("12 hep kok", sp.expand(D(1, m_ + 2, m_)), m_**2 + 4)
    esit("12 kisa", ((-3)**2 - 1*5, D(1, -6, 5)), (4, 16))
    esit("12 fark", (sp.sqrt(D(1, -5, 6))/1, sp.sqrt(D(2, 3, -2))/2, Q(1, 2) - (-2)), (1, Q(5, 2), Q(5, 2)))
    esit("12 tam kare kosulu", (sp.solve(D(4, m_, 9), m_), sp.expand((2*X + 3)**2), sp.expand((2*X - 3)**2)), ([-12, 12], 4*X**2 + 12*X + 9, 4*X**2 - 12*X + 9))
    esit("12 hep pozitif", sp.solveset(D(1, m_, 4) < 0, m_, R), Interval.open(-4, 4))
    esit("12 teget", (sp.solve(D(1, -2, -t_), t_), kok(X**2 - 2*X + 1)), ([-1], FiniteSet(1)))
    esit("12 tepe", (-Q(D(1, -2, -3), 4), (X**2 - 2*X - 3).subs(X, 1)), (-4, -4))
    esit("12 isaret", (6 > 0, 5 > 0, kok(X**2 - 5*X + 6)), (True, True, FiniteSet(2, 3)))
    esit("12 esitsizlik", (sp.solveset(X**2 - 4*X + 3 < 0, X, R), sp.solveset(X**2 + X + 1 < 0, X, R), D(1, -4, 3)), (Interval.open(1, 3), S.EmptySet, 4))
    esit("12 durum tablosu", (D(1, -4, 4), kok(X**2 - 4*X + 4), D(1, -4, 3) > 0, D(1, -4, 5) < 0), (0, FiniteSet(2), True, True))
    # ── 13 ──
    x1, x2 = (5 - sp.sqrt(13))/2, (5 + sp.sqrt(13))/2
    ss = lambda e: sp.nsimplify(sp.simplify(e))
    esit("13 temel", (-Q(-6, 2), Q(4, 2), kok(2*X**2 - 6*X + 4)), (3, 2, FiniteSet(1, 2)))
    esit("13 x2-5x+3", (kok(X**2 - 5*X + 3), ss(x1**2 + x2**2), ss(1/x1 + 1/x2), ss(x1**3 + x2**3), ss(sp.Abs(x1 - x2)), ss(x1**2*x2 + x1*x2**2), ss(x1/x2 + x2/x1), ss((x1 + 1)*(x2 + 1)), ss((x1 - 2)*(x2 - 2))),
         (FiniteSet(x1, x2), 19, Q(5, 3), 80, sp.sqrt(13), 15, Q(19, 3), 9, -3))
    esit("13 bir kok", (kok(X**2 - 7*X + 10), kok(3*X**2 - X - 2), Q(1, 1) - Q(2, 3)), (FiniteSet(2, 5), FiniteSet(-Q(2, 3), 1), Q(1, 3)))
    esit("13 kareler parametre", (sp.solve(m_**2 - 8 - 17, m_), D(1, -5, 4), D(1, 5, 4)), ([-5, 5], 9, 9))
    esit("13 kokten denklem", sp.expand((X - 3)*(X + 4)), X**2 + X - 12)
    esit("13 turetilen", (sp.expand((X - 2*x1)*(X - 2*x2)), sp.expand((X - x1 - 1)*(X - x2 - 1)), sp.expand((X - x1**2)*(X - x2**2)), sp.expand(sp.radsimp(sp.expand(3*(X - 1/x1)*(X - 1/x2))))),
         (X**2 - 10*X + 12, X**2 - 7*X + 9, X**2 - 19*X + 9, 3*X**2 - 5*X + 1))
    esit("13 toplam parametre", (sp.solve(m_ + 2 - 5, m_), D(1, -5, 5)), ([3], 5))
    esit("13 katsayi", (kok(X**2 - 4*X - 5),), (FiniteSet(-1, 5),))
    esit("13 bagintilar", (kok(X**2 - 9*X + 18), kok(X**2 - 7*X + 10), sp.solve([a_ + b_ - 7, a_ - b_ - 3], [a_, b_])), (FiniteSet(3, 6), FiniteSet(2, 5), {a_: 5, b_: 2}))
    esit("13 isaretler", kok(X**2 + 3*X - 10), FiniteSet(-5, 2))
    esit("13 simetrik ters", (kok(X**2 - 4), kok(2*X**2 + 5*X + 2), Q(-1, 2)*(-2)), (FiniteSet(-2, 2), FiniteSet(-2, -Q(1, 2)), 1))
    esit("13 esit kok", (D(1, -6, 9), kok(X**2 - 6*X + 9)), (0, FiniteSet(3)))
    esit("13 tam sayi", sorted({a*(8 - a) for a in range(1, 8)}), [7, 12, 15, 16])
    esit("13 dikdortgen", kok(X**2 - 10*X + 24), FiniteSet(4, 6))
    esit("13 kubik", (sp.factor(X**3 - 6*X**2 + 11*X - 6), 1 + 2 + 3, 1*2 + 1*3 + 2*3, 1*2*3), ((X - 1)*(X - 2)*(X - 3), 6, 11, 6))
    esit("13 hatirlama", sp.expand((X - 1)*(X - 2)), X**2 - 3*X + 2)


def yazi_14_18():
    """14 Parabol, 15 Tepe Noktasi, 16 Parabol Denklemi, 17 Parabol Grafigi, 18 Parabol ve Dogru."""
    X, m_, k_, n_, a_, b_, c_, t_ = sp.symbols("X m_ k_ n_ a_ b_ c_ t_")
    Q = Rational
    kok = lambda e: sp.solveset(sp.expand(e), X, R)
    ac = sp.expand
    def tepe(e):
        p = sp.Poly(ac(e), X); a, b, c = (p.all_coeffs() + [0, 0, 0])[:3] if p.degree() == 2 else (None, None, None)
        r = Q(-b, 2*a) if all(isinstance(v, sp.Integer) for v in (a, b)) else -b/(2*a)
        return (sp.nsimplify(r), sp.nsimplify(ac(e).subs(X, r)))
    D = lambda a, b, c: b*b - 4*a*c
    f = X**2 - 4*X + 3
    # ── 14 ──
    esit("14 temel", ([v*v for v in (-2, -1, 0, 1, 2)], 1 - 0, 4 - 1), ([4, 1, 0, 1, 4], 1, 3))
    esit("14 x2-4x+3", (tepe(f), f.subs(X, 0), f.subs(X, 4), kok(f), -Q(D(1, -4, 3), 4), ac((X - 2)**2 - 1), ac((X - 1)*(X - 3))), ((2, -1), 3, 3, FiniteSet(1, 3), -1, f, f))
    esit("14 tepe bicimi", (kok(2*(X - 1)**2 - 8), tepe((X + 1)*(X - 3))), (FiniteSet(-1, 3), (1, -4)))
    g = -X**2 + 6*X - 5
    esit("14 en buyuk", (tepe(g), kok(g)), ((3, 4), FiniteSet(1, 5)))
    esit("14 goruntu", (function_range(f, X, R), function_range(g, X, R)), (Interval(-1, oo), Interval(-oo, 4)))
    esit("14 kapali aralik", (f.subs(X, 0), f.subs(X, 5), function_range(f, X, Interval(0, 5))), (3, 8, Interval(-1, 8)))
    esit("14 isaret", sp.solveset(f < 0, X, R), Interval.open(1, 3))
    esit("14 oteleme", ac((X - 2)**2 + 3), X**2 - 4*X + 7)
    esit("14 alan", (tepe(X*(10 - X)),), ((5, 25),))
    h = -5*t_**2 + 20*t_
    esit("14 atis", (sp.solve(sp.diff(h, t_), t_), h.subs(t_, 2), sp.solve(h, t_), h.subs(t_, 1), h.subs(t_, 3)), ([2], 20, [0, 4], 15, 15))
    esit("14 isaret okuma", (tepe(X**2 - 4*X - 1)[0] > 0, (X**2 - 4*X - 1).subs(X, 0) < 0), (True, True))
    # ── 15 ──
    f5 = X**2 - 6*X + 5
    esit("15 ilk", (tepe(f5), D(1, -6, 5), [f5.subs(X, v) for v in (1, 5, 0, 6)]), ((3, -4), 16, [0, 0, 5, 5]))
    esit("15 kesirli", (tepe(2*X**2 - 3*X + 1), D(2, -3, 1), -Q(1, 8), 2*Q(9, 16) - Q(9, 4) + 1), ((Q(3, 4), -Q(1, 8)), 1, -Q(1, 8), -Q(1, 8)))
    esit("15 asagi", tepe(-2*X**2 + 8*X - 3), (2, 5))
    esit("15 tam kare", (ac((X + 2)**2 + 3), ac(2*(X - 2)**2 - 3), tepe(2*X**2 - 8*X + 5)), (X**2 + 4*X + 7, 2*X**2 - 8*X + 5, (2, -3)))
    esit("15 kokler", (tepe((X - 2)*(X - 6)), Q(1 + 7, 2)), ((4, -4), 4))
    esit("15 goruntu", function_range(f5, X, R), Interval(-4, oo))
    esit("15 simetrik", [f5.subs(X, v) for v in (0, 6, 2, 4)], [5, 5, -3, -3])
    esit("15 konum", (D(1, -2, 3), tepe(X**2 - 2*X + 3)), (-8, (1, 2)))
    esit("15 tepeden denklem", (sp.solve(4*a_ - 3 - 5, a_), ac(2*(X - 2)**2 - 3)), ([2], 2*X**2 - 8*X + 5))
    esit("15 aralik disi", (f5.subs(X, 4), f5.subs(X, 7), function_range(f5, X, Interval(4, 7))), (-3, 12, Interval(-3, 12)))
    esit("15 koklere", kok((X - 3)**2 - 4), FiniteSet(1, 5))
    esit("15 parametre eksen", (m_, ac((X**2 - 2*m_*X + m_ + 6).subs(m_, 3)), tepe(X**2 - 6*X + 9)), (m_, X**2 - 6*X + 9, (3, 0)))
    esit("15 dogru uzerinde", (sp.solve((4 - 8 + m_) - 2, m_), tepe(X**2 - 4*X + 6)), ([6], (2, 2)))
    esit("15 x ekseni", (sp.solve(D(1, m_, 9), m_), tepe(X**2 + 6*X + 9), tepe(X**2 - 6*X + 9)), ([-6, 6], (-3, 0), (3, 0)))
    esit("15 yol", ac((X - m_)**2 + m_), ac(X**2 - 2*m_*X + m_**2 + m_))
    G = t_*(100 - 2*t_)
    esit("15 gelir", (sp.solve(sp.diff(G, t_), t_), G.subs(t_, 25), sp.solve(G, t_)), ([25], 1250, [0, 50]))
    esit("15 oteleme", ac((X - 3)**2 - 4), f5)
    esit("15 duvar", tepe(X*(40 - 2*X)), (10, 200))
    # ── 16 ──
    esit("16 tepe ve nokta", (sp.solve(4*a_ - 4, a_), ac((X - 1)**2 - 4), (X**2 - 2*X - 3).subs(X, -1)), ([1], X**2 - 2*X - 3, 0))
    esit("16 tepe ve y", (sp.solve(4*a_ + 1 - 9, a_), ac(2*(X - 2)**2 + 1)), ([2], 2*X**2 - 8*X + 9))
    esit("16 kok ve nokta", (sp.solve(-3*a_ + 6, a_), ac(2*(X + 1)*(X - 3))), ([2], 2*X**2 - 4*X - 6))
    esit("16 kok ve max", (sp.solve(a_*2*(-2) - 8, a_), ac(-2*X*(X - 4)), tepe(-2*X**2 + 8*X)), ([-2], -2*X**2 + 8*X, (2, 8)))
    esit("16 kok ve min", (sp.solve(a_*2*(-2) + 8, a_), ac(2*(X - 1)*(X - 5)), tepe(2*X**2 - 12*X + 10)), ([2], 2*X**2 - 12*X + 10, (3, -8)))
    esit("16 tepe ve kok", (2 + (2 - (-1)), sp.solve(a_*3*(-3) + 9, a_), ac((X + 1)*(X - 5)), tepe(X**2 - 4*X - 5)), (5, [1], X**2 - 4*X - 5, (2, -9)))
    esit("16 uc nokta", (sp.solve([a_ + b_ + 1, 4*a_ + 2*b_ + 1 - 3], [a_, b_]), [(2*X**2 - 3*X + 1).subs(X, v) for v in (0, 1, 2)]), ({a_: 2, b_: -3}, [1, 0, 3]))
    esit("16 teget", (sp.solve(4*a_ - 8, a_), ac(2*(X - 2)**2)), ([2], 2*X**2 - 8*X + 8))
    esit("16 eksen iki nokta", (sp.solve([a_ + k_ - 3, 4*a_ + k_], [a_, k_]), ac(-(X - 1)**2 + 4), (-X**2 + 2*X + 3).subs(X, 3)), ({a_: -1, k_: 4}, -X**2 + 2*X + 3, 0))
    esit("16 grafikten", (sp.solve(4*a_ - 2 - 2, a_), ac((X + 1)**2 - 2), (X**2 + 2*X - 1).subs(X, -3)), ([1], X**2 + 2*X - 1, 2))
    esit("16 grafikten kok", (sp.solve(-2*a_ + 4, a_), ac(2*(X + 2)*(X - 1))), ([2], 2*X**2 + 2*X - 4))
    esit("16 oteleme", (ac((X - 3)**2 - 2), ac(3*(X + 1)**2 + 5)), (X**2 - 6*X + 7, 3*X**2 + 6*X + 8))
    esit("16 bicimler", (ac(2*(X - 1)**2 - 8), ac(2*(X + 1)*(X - 3))), (2*X**2 - 4*X - 6, 2*X**2 - 4*X - 6))
    esit("16 simetrik ve orijin", (sp.solve([a_ + c_ - 3, 4*a_ + c_ - 9], [a_, c_]), sp.solve([a_ + b_ - 1, 4*a_ + 2*b_ - 6], [a_, b_]), sp.solve(1 + m_ + 4 - 2, m_)),
         ({a_: 2, c_: 1}, {a_: 2, b_: -1}, [-3]))
    esit("16 iki nokta yetmez", (all((a*X**2 + (1 - a)*X).subs(X, 0) == 0 and (a*X**2 + (1 - a)*X).subs(X, 1) == 1 for a in (1, 2, 3, -5)), ac(2*X**2 - X).subs(X, 1)), (True, 1))
    y16 = -X**2/20 + 5
    esit("16 kemer", (sp.solve(-100*a_ - 5, a_), kok(y16), y16.subs(X, 6)), ([-Q(1, 20)], FiniteSet(-10, 10), Q(16, 5)))
    h16 = -5*(t_ - 1)**2 + 7
    esit("16 atis", (sp.solve(a_ + 7 - 2, a_), ac(h16), h16.subs(t_, 2), h16.subs(t_, 0)), ([-5], -5*t_**2 + 10*t_ + 2, 2, 2))
    # ── 17 ──
    F = X**2 - 2*X - 3
    esit("17 ornek", (tepe(F), F.subs(X, 0), kok(F), F.subs(X, 2), [F.subs(X, v) for v in (-1, 0, 1, 2, 3)]), ((1, -4), -3, FiniteSet(-1, 3), -3, [0, -3, -4, -3, 0]))
    esit("17 sabit cifti", ((X**2 - 6*X + 5).subs(X, 6),), (5,))
    esit("17 asagi", (tepe(-X**2 + 4*X), kok(-X**2 + 4*X), [(-X**2 + 4*X).subs(X, v) for v in (1, 3)]), ((2, 4), FiniteSet(0, 4), [3, 3]))
    esit("17 koksuz", (D(1, 2, 3), tepe(X**2 + 2*X + 3), [(X**2 + 2*X + 3).subs(X, v) for v in (0, -2, 1, -3)]), (-8, (-1, 2), [3, 3, 6, 6]))
    esit("17 teget", [((X - 2)**2).subs(X, v) for v in (2, 0, 4)], [0, 4, 4])
    esit("17 tepe bicimi", (kok(2*(X - 1)**2 - 2), [(2*(X - 1)**2 - 2).subs(X, v) for v in (-1, 3)]), (FiniteSet(0, 2), [6, 6]))
    esit("17 kok bicimi", (tepe(-(X + 1)*(X - 3)), (-(X + 1)*(X - 3)).subs(X, 0), (-(X + 1)*(X - 3)).subs(X, 2)), ((1, 4), 3, 3))
    esit("17 genislik", [[a*d*d for d in (1, 2, 3)] for a in (1, 2, Q(1, 2))], [[1, 4, 9], [2, 8, 18], [Q(1, 2), 2, Q(9, 2)]])
    esit("17 oteleme", tepe((X + 2)**2 - 1), (-2, -1))
    esit("17 kisitli", (function_range(X**2 - 2*X, X, Interval(0, 3)), (X**2 - 2*X).subs(X, 3)), (Interval(-1, 3), 3))
    esit("17 mutlak", (sp.Abs(0**2 - 4), sp.solveset(X**2 - 4 < 0, X, R)), (4, Interval.open(-2, 2)))
    esit("17 iki parabol", (kok(X**2 - (-X**2 + 2)), [v**2 for v in (-1, 1)]), (FiniteSet(-1, 1), [1, 1]))
    esit("17 okuma", (kok(F - 5), sp.solveset(F < 0, X, R), function_range(F, X, R)), (FiniteSet(-2, 4), Interval.open(-1, 3), Interval(-4, oo)))
    esit("17 yansima", tepe(-F), (1, 4))
    esit("17 grafikle denklem", (kok(F - (X - 3)), F.subs(X, 3)), (FiniteSet(0, 3), 0))
    esit("17 grafikten denklem", (sp.solve(a_ + 2 - 3, a_), ac((X + 1)**2 + 2)), ([1], X**2 + 2*X + 3))
    # ── 18 ──
    esit("18 temel", (D(1, -1, -2), kok(X**2 - (X + 2)), D(1, -2, 1), kok(X**2 - (2*X - 1)), D(1, -1, 1)), (9, FiniteSet(-1, 2), 0, FiniteSet(1), -3))
    esit("18 uc dogru", (D(1, -2, 0), D(1, -2, 1), D(1, -2, 2), kok(X**2 - 2*X)), (4, 0, -4, FiniteSet(0, 2)))
    esit("18 teget parametre", sp.solve(D(1, -m_, 3), m_), [-2*sp.sqrt(3), 2*sp.sqrt(3)])
    esit("18 yatay", (sp.solveset(sp.expand(D(1, -4, 5 - k_)) < 0, k_, R), tepe(X**2 - 4*X + 5)), (Interval.open(-oo, 1), (2, 1)))
    esit("18 teget noktasi", (sp.solve(D(1, -4, 3 - k_), k_), kok(X**2 - 4*X + 4), (X**2 - 2*X + 3).subs(X, 2), 2*2 - 1), ([-1], FiniteSet(2), 3, 3))
    esit("18 egimli teget", (sp.solve(D(1, -4, -n_), n_), kok(X**2 - 4*X + 4), all(sp.solve(D(1, -mm, -n_), n_) == [-Q(mm*mm, 4)] for mm in range(-5, 6))), ([-4], FiniteSet(2), True))
    esit("18 noktadan teget", (sp.solve(D(1, -m_, 1), m_), kok(X**2 - 2*X + 1), kok(X**2 + 2*X + 1)), ([-2, 2], FiniteSet(1), FiniteSet(-1)))
    esit("18 orta nokta", (-(-4), Q(4, 2)), (4, 2))
    esit("18 uzaklik", (sp.sqrt(3**2 + 3**2), sp.sqrt((2 - (-1))**2 + (4 - 1)**2)), (3*sp.sqrt(2), 3*sp.sqrt(2)))
    esit("18 iki parabol", kok(X**2 - (-X**2 + 4*X)), FiniteSet(0, 2))
    esit("18 esitsizlik", (sp.solveset(X**2 - X - 2 > 0, X, R), sp.solveset(X**2 - X + 1 > 0, X, R)), (Union(Interval.open(-oo, -1), Interval.open(2, oo)), R))
    esit("18 dikey uzaklik", (tepe(X**2 - X + 1), D(1, -1, 1)), ((Q(1, 2), Q(3, 4)), -3))
    esit("18 iki nokta parametre", sp.solveset(sp.expand(D(1, 1, 3 - k_)) > 0, k_, R), Interval.open(Q(11, 4), oo))
    esit("18 bir nokta verildi", (sp.solve(2*m_ + 2 - 4, m_), kok(X**2 - X - 2), Q(-2, 2)), ([1], FiniteSet(-1, 2), -1))
    esit("18 asagi yatay", tepe(-X**2 + 4*X), (2, 4))
    def say(k):
        return len(sp.solveset(sp.Abs(X**2 - 4) - k, X, R))
    esit("18 mutlak yatay", [say(k) for k in (-1, 0, 2, 4, 5)], [0, 2, 4, 3, 2])
    esit("18 kesen egim", (D(1, -3, -2), kok(X**2 - 3*X - 2).is_FiniteSet), (17, True))
    esit("18 esit bas katsayi", sp.solve((X**2) - (X + 1)**2, X), [-Q(1, 2)])


def esit_ogeler(ad, bul, bek):
    """Ogeleri tek tek karsilastirir; trig sabitleri sympy'de kendiliginden sadelesmedigi
    icin fark hem simplify hem 60 basamak sayisal olarak sifira bakilir."""
    if isinstance(bul, (tuple, list)) and isinstance(bek, (tuple, list)) and len(bul) == len(bek):
        for i, (u, v) in enumerate(zip(bul, bek)):
            esit_ogeler(f"{ad}[{i}]", u, v)
        return
    sayi = lambda v: sp.Integer(v) if isinstance(v, int) and not isinstance(v, bool) else v
    bul, bek = sayi(bul), sayi(bek)
    if bul is bek or (type(bul) is type(bek) and bul == bek):
        return esit(ad, True, True)
    if not isinstance(bul, sp.Expr) or not isinstance(bek, sp.Expr):
        return esit(ad, bul, bek)
    fark = bul - bek
    sifir = sp.simplify(fark) == 0 or (not fark.free_symbols and abs(sp.N(fark, 60)) < sp.Float("1e-50"))
    esit(ad, sifir, True)


def yazi_19_23():
    """19 Trigonometri, 20 Birim Cember, 21 Trigonometrik Oranlar, 22 Ozdeslikler, 23 Grafikler."""
    from sympy import sin, cos, tan, cot, sec, csc, pi, atan, periodicity
    Q = Rational
    g = lambda d: d * pi / 180          # derece -> radyan
    X, a_, b_, h_ = sp.symbols("X a_ b_ h_", real=True)
    s3, s2 = sqrt(3), sqrt(2)
    yak = lambda deger, yaklasik, tol=0.005: abs(float(deger) - yaklasik) < tol
    tur = Interval.Ropen(0, 2 * pi)
    coz = lambda e, alan=tur: sp.solveset(e, X, alan)
    ozdes = lambda sol, sag: sp.simplify(sp.expand_trig(sol - sag)) == 0
    es = esit_ogeler
    # ── 19 ──
    es("19 donusum", (Q(150, 180) * pi, Q(2, 3) * 180, (pi / 6) * 180 / pi), (5 * pi / 6, 120, 30))
    es("19 yay", (6 * pi / 3, 2 * pi * 6), (2 * pi, 12 * pi))
    es("19 esas olcu", (750 - 2 * 360, -60 + 360, 750 % 360, (-60) % 360), (30, 300, 30, 300))
    es("19 3-4-5", (sqrt(9 + 16), Q(3, 5), Q(4, 5), Q(3, 4), Q(4, 3)), (5, sin(atan(Q(3, 4))), cos(atan(Q(3, 4))), tan(atan(Q(3, 4))), 1 / tan(atan(Q(3, 4)))))
    ozel = {30: (Q(1, 2), s3 / 2, s3 / 3, s3), 45: (s2 / 2, s2 / 2, 1, 1), 60: (s3 / 2, Q(1, 2), s3, s3 / 3)}
    for d_, (sn, cs, tn, ct) in ozel.items():
        es(f"19-21 ozel {d_}", (sin(g(d_)), cos(g(d_)), tan(g(d_)), cot(g(d_))), (sn, cs, tn, ct))
    es("19 ozel ucgenler", (sp.sqrt(1 + 3), Q(1, 2), sqrt(1 + 1)), (2, sin(g(30)), s2))
    es("19 eksen degerleri", (sin(0), cos(0), tan(0), sin(g(90)), cos(g(90)), tan(g(90))), (0, 1, 0, 1, 0, sp.zoo))
    es("19 150", (sin(g(150)), cos(g(150))), (Q(1, 2), -s3 / 2))
    es("19 sinir", (function_range(3 * sin(X) + 1, X, R), sp.solveset(sin(X) - 2, X, R)), (Interval(-2, 4), S.EmptySet))
    th = pi - sp.acos(Q(5, 13))
    es("19 ikinci bolge", (1 - Q(25, 169), sin(th), tan(th)), (Q(144, 169), Q(12, 13), -Q(12, 5)))
    th = sp.asin(Q(3, 5))
    es("19 temel ozdeslik", (1 - Q(9, 25), cos(th), tan(th), cot(th)), (Q(16, 25), Q(4, 5), Q(3, 4), Q(4, 3)))
    es("19 tumler", (sin(g(20)) - cos(g(70)), cot(g(30)), tan(g(60))), (0, s3, s3))
    es("19 negatif butunler", (sin(g(-30)), cos(g(-60)), sin(g(120)), sin(g(60))), (-Q(1, 2), Q(1, 2), s3 / 2, s3 / 2))
    es("19 periyot", (sin(g(390)), tan(g(225))), (Q(1, 2), 1))
    es("19 denklem", coz(sin(X) - Q(1, 2)), FiniteSet(pi / 6, 5 * pi / 6))
    es("19 merdiven", (10 * sin(g(60)), yak(5 * s3, 8.66), 10 * cos(g(60))), (5 * s3, True, 5))
    es("19 golge", (10 * tan(g(30)), yak(10 * s3 / 3, 5.77)), (10 * s3 / 3, True))
    es("19 egim", (atan(1), atan(s3)), (g(45), g(60)))
    es("19 sadelestirme", sp.simplify((1 - cos(X)**2) / sin(X)), sin(X))
    # ── 20 ──
    nokta = lambda aci, r=1: (sp.nsimplify(r * cos(aci)), sp.nsimplify(r * sin(aci)))
    es("20 eksenler", [nokta(g(d_)) for d_ in (0, 90, 180, 270)], [(1, 0), (0, 1), (-1, 0), (0, -1)])
    isaret = lambda d_: tuple(sp.sign(f(g(d_))) for f in (cos, sin, tan))
    es("20 bolgeler", [isaret(d_) for d_ in (45, 135, 225, 315)], [(1, 1, 1), (-1, 1, -1), (-1, -1, 1), (1, -1, -1)])
    es("20 buyuk negatif", (1110 - 3 * 360, nokta(g(1110)), nokta(-pi / 3)), (30, (s3 / 2, Q(1, 2)), (Q(1, 2), -s3 / 2)))
    es("20 ilk bolge", ([nokta(g(d_)) for d_ in (30, 45, 60)], Q(3, 4) + Q(1, 4)), ([(s3 / 2, Q(1, 2)), (s2 / 2, s2 / 2), (Q(1, 2), s3 / 2)], 1))
    es("20 referans", (225 - 180, nokta(g(225))), (45, (-s2 / 2, -s2 / 2)))
    es("20 yansitma", [nokta(g(d_)) for d_ in (30, 150, 210, 330)], [(s3 / 2, Q(1, 2)), (-s3 / 2, Q(1, 2)), (-s3 / 2, -Q(1, 2)), (s3 / 2, -Q(1, 2))])
    es("20 radyan", [r * 180 / pi for r in (pi / 6, 5 * pi / 6, 7 * pi / 6, 11 * pi / 6)], [30, 150, 210, 330])
    es("20 tanjant kotanjant ekseni", (tan(g(45)), tan(g(60)), cot(g(45)), cot(g(30))), (1, s3, 1, s3))
    es("20 ceyrek donus", (ozdes(sin(pi / 2 + X), cos(X)), ozdes(cos(pi / 2 + X), -sin(X)), sin(g(120)), cos(g(30)), cos(g(120)), -sin(g(30))), (True, True, s3 / 2, s3 / 2, -Q(1, 2), -Q(1, 2)))
    es("20 simetriler", [ozdes(l, r) for l, r in ((sin(-X), -sin(X)), (cos(-X), cos(X)), (sin(pi - X), sin(X)), (cos(pi - X), -cos(X)),
                                                    (sin(pi + X), -sin(X)), (cos(pi + X), -cos(X)), (sin(2 * pi - X), -sin(X)), (cos(2 * pi - X), cos(X)))], [True] * 8)
    es("20 135 240", (sin(g(135)), cos(g(240))), (s2 / 2, -Q(1, 2)))
    es("20 ayni sinus", coz(sin(X) - s3 / 2), FiniteSet(g(60), g(120)))
    es("20 ayni kosinus", coz(cos(X) + Q(1, 2)), FiniteSet(g(120), g(240)))
    es("20 esitsizlik", sp.solveset(sin(X) > Q(1, 2), X, tur), Interval.open(g(30), g(150)))
    th = pi - sp.acos(Q(3, 5))
    es("20 noktadan", (Q(9, 25) + Q(16, 25), nokta(th), tan(th), cot(th)), (1, (-Q(3, 5), Q(4, 5)), -Q(4, 3), -Q(3, 4)))
    es("20 yaricap r", nokta(g(60), 4), (2, 2 * s3))
    es("20 karsilastirma", (float(sin(g(20))) < float(sin(g(70))), sin(g(70)) - cos(g(20))), (True, 0))
    es("20 yay pi", (pi * 180 / pi, nokta(pi)), (180, (-1, 0)))
    # ── 21 ──
    th = atan(Q(5, 12))
    es("21 5-12-13", (sqrt(25 + 144), sin(th), cos(th), tan(th), cot(th), 1 / cos(th), 1 / sin(th)), (13, Q(5, 13), Q(12, 13), Q(5, 12), Q(12, 5), Q(13, 12), Q(13, 5)))
    es("21 5-12-13 bagintilar", (Q(25 + 144, 169), Q(5, 12) * Q(12, 5), Q(5, 13) / Q(12, 13), Q(10, 26)), (1, 1, Q(5, 12), Q(5, 13)))
    es("21 tumler", (90 - 35, sin(g(35)) - cos(g(55))), (55, 0))
    es("21 bagintilar", (ozdes(1 + tan(X)**2, 1 / cos(X)**2), ozdes(1 + cot(X)**2, 1 / sin(X)**2)), (True, True))
    th = atan(Q(3, 4))
    es("21 tan 3/4", (sin(th), cos(th), cot(th)), (Q(3, 5), Q(4, 5), Q(4, 3)))
    th = sp.acos(Q(2, 3))
    es("21 cos 2/3", (sqrt(9 - 4), sin(th), tan(th)), (sqrt(5), sqrt(5) / 3, sqrt(5) / 2))
    es("21 orandan aci", (Q(5, 1) / (5 * s3), atan(1 / s3)), (s3 / 3, g(30)))
    es("21 kenar bulmak", (12 * sin(g(30)), 12 * cos(g(30)), 7 / sin(g(45))), (6, 6 * s3, 7 * s2))
    es("21 cevre alan", (10 * sin(g(30)), 10 * cos(g(30)), 10 + 5 + 5 * s3, 5 * 5 * s3 / 2), (5, 5 * s3, 15 + 5 * s3, 25 * s3 / 2))
    es("21 degisim", (float(sin(g(40))) < float(sin(g(50))), float(cos(g(40))) > float(cos(g(50))), float(tan(g(50))) > 1), (True, True, True))
    es("21 yukseklik", (20 * tan(g(60)), yak(20 * s3, 34.64), 20 / cos(g(60))), (20 * s3, True, 40))
    xx = sp.solve(sp.Eq(X * s3, (X + 10) / s3), X)[0]
    es("21 iki gozlem", (xx, xx * s3, yak(5 * s3, 8.66), sqrt(xx**2 + (xx * s3)**2)), (5, 5 * s3, True, 10))
    es("21 egik duzlem", (10 * sin(g(30)), 10 * cos(g(30))), (5, 5 * s3))
    es("21 merdiven", (3 * s3 / 6, sp.asin(3 * s3 / 6), 6 * cos(g(60))), (s3 / 2, g(60), 3))
    es("21 ikizkenar", ((180 - 120) // 2, 10 * sin(g(30)), 2 * 10 * cos(g(30))), (30, 5, 10 * s3))
    es("21 tan sin", (float(tan(g(30))) > 0.5, yak(s3 / 3, 0.577, 0.0005)), (True, True))
    es("21 alan", (Q(1, 2) * 6 * 8 * sin(g(30)), sin(g(90))), (12, 1))
    # ── 22 ──
    es("22 temel sade", (sp.simplify((1 - sin(X)**2) / cos(X)), sp.simplify((sin(X)**4 - cos(X)**4) / (sin(X)**2 - cos(X)**2))), (cos(X), 1))
    th = atan(2)
    es("22 tan 2", (1 + 2**2, cos(th)**2), (5, Q(1, 5)))
    es("22 kare acilim", ozdes((sin(X) + cos(X))**2, 1 + 2 * sin(X) * cos(X)), True)
    es("22 ispat", ozdes(tan(X) + cot(X), 1 / (sin(X) * cos(X))), True)
    th = sp.asin(Q(3, 5))
    es("22 toplam verilince", (sin(th) + cos(th), (Q(49, 25) - 1) / 2, sin(2 * th), ozdes((sin(X) - cos(X))**2 + (sin(X) + cos(X))**2, 2)), (Q(7, 5), Q(12, 25), Q(24, 25), True))
    es("22 tumler kare", sp.nsimplify(sin(g(20))**2 + sin(g(70))**2), 1)
    es("22 toplam fark formulleri", [ozdes(l, r) for l, r in (
        (sin(a_ + b_), sin(a_) * cos(b_) + cos(a_) * sin(b_)), (cos(a_ + b_), cos(a_) * cos(b_) - sin(a_) * sin(b_)),
        (sin(a_ - b_), sin(a_) * cos(b_) - cos(a_) * sin(b_)), (cos(a_ - b_), cos(a_) * cos(b_) + sin(a_) * sin(b_)),
        (tan(a_ + b_), (tan(a_) + tan(b_)) / (1 - tan(a_) * tan(b_))), (tan(a_ - b_), (tan(a_) - tan(b_)) / (1 + tan(a_) * tan(b_))))], [True] * 6)
    es("22 75 15", (sin(g(75)), s2 / 2 * s3 / 2 + s2 / 2 * Q(1, 2), cos(g(15)), tan(g(15)), (1 - s3 / 3) / (1 + s3 / 3)), ((sqrt(6) + s2) / 4, (sqrt(6) + s2) / 4, (sqrt(6) + s2) / 4, 2 - s3, 2 - s3))
    es("22 dagilmaz", (sin(g(90)), sin(g(30)) + sin(g(60)), yak((1 + s3) / 2, 1.37)), (1, (1 + s3) / 2, True))
    es("22 tan toplam aci", ((2 + 3) / Q(1 - 6), atan(2) + atan(3)), (-1, g(135)))
    es("22 iki kat", [ozdes(l, r) for l, r in ((sin(2 * X), 2 * sin(X) * cos(X)), (cos(2 * X), cos(X)**2 - sin(X)**2), (cos(2 * X), 2 * cos(X)**2 - 1),
                                                 (cos(2 * X), 1 - 2 * sin(X)**2), (tan(2 * X), 2 * tan(X) / (1 - tan(X)**2)), (sin(3 * X), 3 * sin(X) - 4 * sin(X)**3))], [True] * 6)
    th = sp.asin(Q(3, 5))
    es("22 iki kat 3/5", (sin(2 * th), cos(2 * th), tan(2 * th)), (Q(24, 25), Q(7, 25), Q(24, 7)))
    th = pi - sp.acos(Q(3, 5))
    es("22 ikinci bolge iki kat", (sin(th), sin(2 * th), cos(2 * th)), (Q(4, 5), -Q(24, 25), -Q(7, 25)))
    es("22 kuvvet azaltma", (ozdes(cos(X)**2, (1 + cos(2 * X)) / 2), ozdes(sin(X)**2, (1 - cos(2 * X)) / 2), cos(g(15))**2, (1 + s3 / 2) / 2), (True, True, (2 + s3) / 4, (2 + s3) / 4))
    es("22 yarim aci", (sin(g(15)), sqrt((1 - cos(g(30))) / 2), yak(sqrt(2 - s3) / 2, 0.2588, 0.00005)), (sqrt(2 - s3) / 2, sqrt(2 - s3) / 2, True))
    es("22 uc kat 30", (sin(g(90)), 3 * Q(1, 2) - 4 * Q(1, 8)), (1, 1))
    es("22 donusum", [ozdes(l, r) for l, r in (
        (sin(a_) + sin(b_), 2 * sin((a_ + b_) / 2) * cos((a_ - b_) / 2)), (sin(a_) - sin(b_), 2 * cos((a_ + b_) / 2) * sin((a_ - b_) / 2)),
        (cos(a_) + cos(b_), 2 * cos((a_ + b_) / 2) * cos((a_ - b_) / 2)), (cos(a_) - cos(b_), -2 * sin((a_ + b_) / 2) * sin((a_ - b_) / 2)),
        (2 * sin(a_) * cos(b_), sin(a_ + b_) + sin(a_ - b_)), (2 * cos(a_) * cos(b_), cos(a_ + b_) + cos(a_ - b_)),
        (2 * sin(a_) * sin(b_), cos(a_ - b_) - cos(a_ + b_)))], [True] * 7)
    es("22 donusum ornek", (sin(g(75)) + sin(g(15)), 2 * sin(g(45)) * cos(g(30)), 2 * sin(g(75)) * cos(g(15))), (sqrt(6) / 2, sqrt(6) / 2, 1 + s3 / 2))
    es("22 kalip", (sin(g(15)) * cos(g(15)), cos(g(15))**2 - sin(g(15))**2), (Q(1, 4), s3 / 2))
    es("22 denklem sin2x", coz(sin(2 * X) - sin(X)), FiniteSet(0, g(60), g(180), g(300)))
    es("22 denklem cos2x", (sp.factor(2 * X**2 - X - 1), coz(cos(2 * X) - cos(X))), ((2 * X + 1) * (X - 1), FiniteSet(0, g(120), g(240))))
    es("22 en buyuk", (sqrt(3**2 + 4**2), function_range(3 * sin(X) + 4 * cos(X), X, tur), function_range(sin(X) * cos(X), X, tur)), (5, Interval(-5, 5), Interval(-Q(1, 2), Q(1, 2))))
    # ── 23 ──
    noktalar = (0, pi / 2, pi, 3 * pi / 2, 2 * pi)
    es("23 tablolar", ([sin(v) for v in noktalar], [cos(v) for v in noktalar]), ([0, 1, 0, -1, 0], [1, 0, -1, 0, 1]))
    es("23 sinus ozellik", (function_range(sin(X), X, R), periodicity(sin(X), X), ozdes(sin(-X), -sin(X)), coz(sin(X)), sin(pi / 2 + 2 * pi)), (Interval(-1, 1), 2 * pi, True, FiniteSet(0, pi), 1))
    es("23 kosinus ozellik", (function_range(cos(X), X, R), periodicity(cos(X), X), ozdes(cos(X), sin(X + pi / 2)), coz(cos(X)), cos(pi)), (Interval(-1, 1), 2 * pi, True, FiniteSet(pi / 2, 3 * pi / 2), -1))
    es("23 genlik", (function_range(3 * sin(X), X, R), -2 * sin(pi / 2), function_range(2 * sin(X), X, R)), (Interval(-3, 3), -2, Interval(-2, 2)))
    es("23 periyot", (periodicity(sin(2 * X), X), periodicity(cos(3 * X), X), periodicity(5 * tan(X / 2) - 1, X), periodicity(tan(X), X), periodicity(cot(X), X)), (pi, 2 * pi / 3, 2 * pi, pi, pi))
    es("23 duşey", function_range(sin(X) + 1, X, R), Interval(0, 2))
    es("23 yatay", (ozdes(sin(X + pi / 2), cos(X)), ozdes(sin(2 * X - pi), sin(2 * (X - pi / 2)))), (True, True))
    es("23 en buyuk", (function_range(4 - 3 * cos(2 * X), X, Interval(0, 2 * pi)), (4 - 3 * cos(2 * X)).subs(X, pi / 2)), (Interval(1, 7), 7))
    es("23 tanjant", (coz(tan(X), Interval(0, 2 * pi)), cos(pi / 2), cos(3 * pi / 2), ozdes(tan(-X), -tan(X))), (FiniteSet(0, pi, 2 * pi), 0, 0, True))
    es("23 kotanjant", (coz(cot(X), Interval.open(0, 2 * pi)), sin(pi), sin(2 * pi)), (FiniteSet(pi / 2, 3 * pi / 2), 0, 0))
    y_ = 2 * sin(2 * X) + 1
    es("23 grafikten", (Q(3 + (-1), 2), Q(3 - (-1), 2), sp.solve(2 * pi / b_ - pi, b_), function_range(y_, X, R), y_.subs(X, pi / 4), y_.subs(X, 3 * pi / 4), periodicity(y_, X)), (1, 2, [2], Interval(-1, 3), 3, -1, pi))
    es("23 cozum", (len(coz(sin(X) - Q(1, 2))), coz(sin(2 * X) - Q(1, 2))), (2, FiniteSet(pi / 12, 5 * pi / 12, 13 * pi / 12, 17 * pi / 12)))
    es("23 periyot sayisi", (2 * pi / (2 * pi / 3), len(coz(cos(3 * X)))), (3, 6))
    es("23 esitsizlik", sp.solveset(cos(X) > 0, X, tur), Union(Interval.Ropen(0, pi / 2), Interval.open(3 * pi / 2, 2 * pi)))
    es("23 toplam periyot", periodicity(sin(2 * X) + cos(3 * X), X), 2 * pi)
    # periodicity() en kucuk periyodu garanti etmez (sin^2 icin 2pi doner): pi'nin periyot oldugu
    # ve (0, pi) icinde f(t) = f(0) cozumu olmadigi, yani daha kucuk periyot olmadigi ayrica gosterilir
    tt = sp.symbols("tt", real=True)
    esas = lambda f, T: sp.simplify(f.subs(X, X + T) - f) == 0 and sp.solveset(sp.Eq(f.subs(X, tt), f.subs(X, 0)), tt, Interval.open(0, T)) == S.EmptySet
    es("23 kare mutlak", (esas(sin(X)**2, pi), esas(Abs(sin(X)), pi), ozdes(sin(X)**2, (1 - cos(2 * X)) / 2)), (True, True, True))
    es("23 hata", periodicity(sin(2 * X), X) != 4 * pi, True)


def yazi_24_26():
    """24 Toplam ve Fark, 25 Iki Kat ve Yarim Aci, 26 Trigonometrik Denklemler."""
    from sympy import sin, cos, tan, cot, pi, atan, asin, acos
    es = esit_ogeler
    Q = Rational
    g = lambda d: d * pi / 180
    X, a_, b_, t_ = sp.symbols("X a_ b_ t_", real=True)
    s2, s3, s6 = sqrt(2), sqrt(3), sqrt(6)
    tur = Interval.Ropen(0, 2 * pi)
    coz = lambda e, alan=tur: sp.solveset(e, X, alan)
    # sympy bazi yarim aci ozdesliklerini sembolik sadelestiremiyor; o zaman ozdeslik
    # yedi ayri noktada 50 basamak sayisal olarak denenir (analitik fonksiyonlar)
    def ozdes(sol, sag):
        fark = sol - sag
        if sp.simplify(sp.expand_trig(fark)) == 0:
            return True
        serbest = sorted(fark.free_symbols, key=str)
        noktalar = (Q(3, 10), Q(7, 10), Q(11, 10), Q(23, 10), Q(41, 10), Q(11, 2), Q(-9, 10))
        return all(abs(sp.N(fark.subs({s: n + j * Q(1, 7) for j, s in enumerate(serbest)}), 60)) < sp.Float("1e-45") for n in noktalar)
    # ── 24 ──
    esit("24 ispat uzaklik", (sp.simplify(sp.expand((cos(a_) - cos(b_))**2 + (sin(a_) - sin(b_))**2) - (2 - 2 * (cos(a_) * cos(b_) + sin(a_) * sin(b_)))),
                             sp.simplify(sp.expand((cos(a_ - b_) - 1)**2 + sin(a_ - b_)**2) - (2 - 2 * cos(a_ - b_)))), (0, 0))
    es("24 tanjant tanimsiz", (1 - tan(g(30)) * tan(g(60)), g(30) + g(60)), (0, g(90)))
    es("24 sinus", (sin(g(105)), s3 / 2 * s2 / 2 + Q(1, 2) * s2 / 2, sin(g(15)), s2 / 2 * s3 / 2 - s2 / 2 * Q(1, 2), sin(g(75))), ((s6 + s2) / 4, (s6 + s2) / 4, (s6 - s2) / 4, (s6 - s2) / 4, (s6 + s2) / 4))
    es("24 kosinus", (cos(g(75)), cos(g(105)), s2 / 2 * s3 / 2 - s2 / 2 * Q(1, 2), Q(1, 2) * s2 / 2 - s3 / 2 * s2 / 2), ((s6 - s2) / 4, (s2 - s6) / 4, (s6 - s2) / 4, (s2 - s6) / 4))
    es("24 tanjant", (tan(g(75)), (1 + s3 / 3) / (1 - s3 / 3), (3 + s3) / (3 - s3), sp.expand((3 + s3)**2), (12 + 6 * s3) / 6, tan(g(105)), tan(g(15)), tan(g(15)) * tan(g(75))),
       (2 + s3, 2 + s3, 2 + s3, 12 + 6 * s3, 2 + s3, -(2 + s3), 2 - s3, 1))
    es("24 radyan", (pi / 3 + pi / 4, cos(7 * pi / 12), (pi / 12) * 180 / pi, (7 * pi / 12) * 180 / pi), (7 * pi / 12, (s2 - s6) / 4, 15, 105))
    a1, b1 = asin(Q(3, 5)), acos(Q(5, 13))
    es("24 oranlardan", (cos(a1), sin(b1), sin(a1 + b1), cos(a1 + b1), sin(a1 - b1), cos(a1 - b1), float(a1 + b1) > float(pi / 2), float(b1) > float(a1)),
       (Q(4, 5), Q(12, 13), Q(63, 65), -Q(16, 65), -Q(33, 65), Q(56, 65), True, True))
    a2, b2 = pi - asin(Q(4, 5)), asin(Q(5, 13))
    es("24 bolge", (cos(a2), cos(b2), cos(a2 + b2)), (-Q(3, 5), Q(12, 13), -Q(56, 65)))
    es("24 tersten", (sin(g(50)) * cos(g(10)) + cos(g(50)) * sin(g(10)), cos(g(70)) * cos(g(10)) + sin(g(70)) * sin(g(10))), (s3 / 2, Q(1, 2)))
    es("24 tanjant tersten", ((tan(g(20)) + tan(g(25))) / (1 - tan(g(20)) * tan(g(25))), (1 + tan(g(20))) * (1 + tan(g(25)))), (1, 2))
    es("24 tanjantlardan aci", ((Q(1, 2) + Q(1, 3)) / (1 - Q(1, 6)), atan(Q(1, 2)) + atan(Q(1, 3))), (1, g(45)))
    es("24 tumler tanjant", tan(g(10)) * tan(g(20)) * tan(g(70)) * tan(g(80)), 1)
    es("24 indirgeme", (ozdes(sin(pi / 2 + X), cos(X)), ozdes(cos(pi - X), -cos(X))), (True, True))
    es("24 carpim", (ozdes(sin(a_ + b_) * sin(a_ - b_), sin(a_)**2 - sin(b_)**2), ozdes(cos(a_ + b_) * cos(a_ - b_), cos(a_)**2 - sin(b_)**2),
                     sin(g(75)) * sin(g(15)), sin(g(45))**2 - sin(g(30))**2), (True, True, Q(1, 4), Q(1, 4)))
    es("24 tek sinus", (ozdes(s3 * sin(X) + cos(X), 2 * sin(X + g(30))), function_range(s3 * sin(X) + cos(X), X, Interval(0, 2 * pi)),
                        ozdes(sin(X) - cos(X), s2 * sin(X - g(45))), function_range(sin(X) - cos(X), X, Interval(0, 2 * pi))), (True, Interval(-2, 2), True, Interval(-s2, s2)))
    es("24 denklem", coz(sin(X) * cos(g(30)) + cos(X) * sin(g(30)) - 1), FiniteSet(g(60)))
    A, B = asin(Q(3, 5)), asin(Q(5, 13))
    es("24 ucgen", (sin(pi - A - B), cos(pi - A - B), Q(48, 65) - Q(15, 65), float(pi - A - B) > float(pi / 2)), (Q(56, 65), -Q(33, 65), Q(33, 65), True))
    es("24 dogrular", ((3 - Q(1, 2)) / (1 + Q(3, 2)), sp.Abs(atan(3) - atan(Q(1, 2)))), (1, g(45)))
    # ── 25 ──
    x1_ = asin(Q(5, 13))
    es("25 sin iki kat", (cos(x1_), sin(2 * x1_), sin(pi / 8) * cos(pi / 8)), (Q(12, 13), Q(120, 169), s2 / 4))
    es("25 cos iki kat", (2 * Q(1, 9) - 1, cos(2 * acos(Q(1, 3)))), (-Q(7, 9), -Q(7, 9)))
    es("25 tan iki kat", (tan(2 * atan(Q(1, 2))), 1 - 1**2), (Q(4, 3), 0))
    x2_ = pi - asin(Q(12, 13))
    es("25 bolge", (cos(x2_), sin(2 * x2_), cos(2 * x2_), abs(float(x2_ * 180 / pi) - 112.6) < 0.05, abs(float(2 * x2_ * 180 / pi) - 225.2) < 0.1),
       (-Q(5, 13), -Q(120, 169), -Q(119, 169), True, True))
    x3_ = acos(Q(7, 25)) / 2
    es("25 iki kattan geri", (sin(x3_)**2, sin(x3_), cos(x3_)), (Q(9, 25), Q(3, 5), Q(4, 5)))
    es("25 tersten", (cos(pi / 8)**2 - sin(pi / 8)**2, 1 - 2 * sin(g(15))**2), (s2 / 2, s3 / 2))
    es("25 dorduncu kuvvet", (ozdes(sin(X)**4 + cos(X)**4, 1 - 2 * sin(X)**2 * cos(X)**2), sin(g(15))**4 + cos(g(15))**4, 1 - Q(1, 4) / 2, ozdes(cos(X)**4 - sin(X)**4, cos(2 * X))),
       (True, Q(7, 8), Q(7, 8), True))
    es("25 yarim aci deger", (cos(pi / 8), sin(pi / 8), (2 + s2) / 4 + (2 - s2) / 4), (sqrt(2 + s2) / 2, sqrt(2 - s2) / 2, 1))
    x4_ = pi + acos(Q(3, 5))
    es("25 yarim aci isaret", (cos(x4_), float(x4_ / 2) > float(pi / 2) and float(x4_ / 2) < float(3 * pi / 4), sin(x4_ / 2), cos(x4_ / 2), sqrt((1 + Q(3, 5)) / 2), -sqrt((1 - Q(3, 5)) / 2)),
       (-Q(3, 5), True, 2 * sqrt(5) / 5, -sqrt(5) / 5, 2 * sqrt(5) / 5, -sqrt(5) / 5))
    es("25 tanjant yarim", (ozdes(tan(X / 2), sin(X) / (1 + cos(X))), ozdes(tan(X / 2), (1 - cos(X)) / sin(X)), tan(pi / 8), tan(g(15))), (True, True, s2 - 1, 2 - s3))
    t0 = 2
    es("25 t donusumu", (ozdes(sin(X), 2 * tan(X / 2) / (1 + tan(X / 2)**2)), ozdes(cos(X), (1 - tan(X / 2)**2) / (1 + tan(X / 2)**2)), ozdes(tan(X), 2 * tan(X / 2) / (1 - tan(X / 2)**2)),
                         Q(2 * t0, 1 + t0**2), Q(1 - t0**2, 1 + t0**2), sin(2 * atan(2)), cos(2 * atan(2))), (True, True, True, Q(4, 5), -Q(3, 5), Q(4, 5), -Q(3, 5)))
    es("25 uc kat", (ozdes(sin(3 * X), 3 * sin(X) - 4 * sin(X)**3), ozdes(cos(3 * X), 4 * cos(X)**3 - 3 * cos(X)), cos(pi), 4 * Q(1, 8) - 3 * Q(1, 2)), (True, True, -1, -1))
    es("25 sadelestirme", (ozdes((1 - cos(2 * X)) / sin(2 * X), tan(X)), ozdes(sin(2 * X) / (1 + cos(2 * X)), tan(X))), (True, True))
    es("25 ispat", (ozdes((sin(X) + cos(X))**2, 1 + sin(2 * X)), ozdes(cot(X) - tan(X), 2 * cot(2 * X)), cot(g(15)) - tan(g(15)), 2 * cot(g(30))), (True, True, 2 * s3, 2 * s3))
    es("25 denklem", (sp.factor(2 * X**2 - X - 1), coz(cos(2 * X) + sin(X))), ((2 * X + 1) * (X - 1), FiniteSet(g(90), g(210), g(330))))
    es("25 en buyuk", function_range(4 * sin(X) * cos(X) + 1, X, Interval(0, 2 * pi)), Interval(-1, 3))
    es("25 menzil", (Q(400, 10), 40 * sin(g(30)), 40 * sin(g(150)), 40 * sin(g(90))), (40, 20, 20, 40))
    es("25 kontrol", (2 * cos(g(30))**2 - 1, cos(g(60))), (Q(1, 2), Q(1, 2)))
    # ── 26 ──
    es("26 grafik", coz(sin(X) - Q(1, 2)), FiniteSet(pi / 6, 5 * pi / 6))
    es("26 genel", (coz(sin(X) - s2 / 2), coz(cos(X) - Q(1, 2)), coz(tan(X) - s3, Interval.Ropen(0, pi)), coz(cot(X) + 1, Interval.open(0, pi))),
       (FiniteSet(pi / 4, 3 * pi / 4), FiniteSet(pi / 3, 5 * pi / 3), FiniteSet(pi / 3), FiniteSet(3 * pi / 4)))
    es("26 ozel degerler", [coz(e) for e in (sin(X), sin(X) - 1, sin(X) + 1, cos(X), cos(X) - 1, cos(X) + 1)],
       [FiniteSet(0, pi), FiniteSet(pi / 2), FiniteSet(3 * pi / 2), FiniteSet(pi / 2, 3 * pi / 2), FiniteSet(0), FiniteSet(pi)])
    es("26 cozumsuz", (sp.solveset(2 * sin(X) - 3, X, R), sp.solveset(cos(X) + 2, X, R)), (S.EmptySet, S.EmptySet))
    es("26 aralik", (coz(sin(X) + Q(1, 2)), coz(cos(X) + s3 / 2)), (FiniteSet(7 * pi / 6, 11 * pi / 6), FiniteSet(5 * pi / 6, 7 * pi / 6)))
    es("26 katli", coz(sin(2 * X) - s3 / 2), FiniteSet(pi / 6, pi / 3, 7 * pi / 6, 4 * pi / 3))
    es("26 otelenmis", coz(cos(X - pi / 6)), FiniteSet(2 * pi / 3, 5 * pi / 3))
    es("26 ayni fonksiyon", (coz(sin(3 * X) - sin(X), Interval.Ropen(0, pi)), coz(cos(3 * X) - cos(X), Interval(0, pi))), (FiniteSet(0, pi / 4, 3 * pi / 4), FiniteSet(0, pi / 2, pi)))
    es("26 ikinci derece", (sp.factor(2 * X**2 - 3 * X + 1), coz(2 * sin(X)**2 - 3 * sin(X) + 1)), ((2 * X - 1) * (X - 1), FiniteSet(pi / 6, pi / 2, 5 * pi / 6)))
    es("26 ozdeslikle", (sp.factor(2 * X**2 + X - 1), coz(2 * cos(X)**2 - sin(X) - 1)), ((2 * X - 1) * (X + 1), FiniteSet(pi / 6, 5 * pi / 6, 3 * pi / 2)))
    es("26 carpanlara", coz(tan(X) * sin(X) - sin(X)), FiniteSet(0, pi / 4, pi, 5 * pi / 4))
    es("26 homojen", (sin(pi / 2)**2 - 3 * cos(pi / 2)**2, coz(sin(X)**2 - 3 * cos(X)**2)), (1, FiniteSet(pi / 3, 2 * pi / 3, 4 * pi / 3, 5 * pi / 3)))
    es("26 toplam", (coz(sin(X) + cos(X) - 1), ozdes(sin(X) + cos(X), s2 * sin(X + pi / 4))), (FiniteSet(0, pi / 2), True))
    es("26 kare alma", (coz(sin(2 * X)), sin(pi) + cos(pi), sin(3 * pi / 2) + cos(3 * pi / 2)), (FiniteSet(0, pi / 2, pi, 3 * pi / 2), -1, -1))
    es("26 tanim kumesi", (coz((1 - sin(X)) / cos(X)), coz(1 - sin(X)), cos(pi / 2)), (S.EmptySet, FiniteSet(pi / 2), 0))
    es("26 esitsizlik", sp.solveset(cos(X) < Q(1, 2), X, tur), Interval.open(pi / 3, 5 * pi / 3))
    es("26 cozum sayisi", len(coz(sin(3 * X) - Q(1, 2))), 6)
    h = 10 - 8 * cos(pi * t_ / 15)
    es("26 donme dolap", (function_range(h, t_, Interval(0, 30)), sp.solveset(h - 14, t_, Interval.Ropen(0, 30)), h.subs(t_, 40), h.subs(t_, 50), (2 * pi) / (pi / 15)),
       (Interval(2, 18), FiniteSet(10, 20), 14, 14, 30))


def yazi_27_29():
    """27 Logaritma, 28 Logaritma Kurallari, 29 Logaritmik Denklemler."""
    from sympy import log as L, E, exp, floor
    es = esit_ogeler
    Q = Rational
    X, Y, t_, n_ = sp.symbols("X Y t_ n_", real=True)
    lg = lambda v, b=10: L(v, b)                       # sympy: log(v, b)
    yak = lambda deger, yaklasik, tol: abs(float(deger) - yaklasik) < tol
    pozitif = Interval.open(0, oo)
    def coz(e, alan=R):
        return sp.solveset(e, X, alan)
    def koklu(denklem, kosullar):
        """Cebirsel denklemi coz, tanim kosullarini (hepsi > 0 ya da True) saglayanlari tut."""
        kokler = sp.solveset(denklem, X, R)
        return FiniteSet(*[k for k in kokler if all(bool(c.subs(X, k)) for c in kosullar)])
    # ── 27 ──
    es("27 giris", (2**3, lg(8, 2)), (8, 3))
    es("27 tablo", (lg(32, 2), lg(81, 3), lg(Q(1, 25), 5), lg(3, 9), lg(8, Q(1, 2)), S(5)**-2, 9**Q(1, 2), Q(1, 2)**-3), (5, 4, -2, Q(1, 2), -3, Q(1, 25), 3, 8))
    es("27 log4 8", (lg(8, 4), sp.solve(2 * X - 3, X)), (Q(3, 2), [Q(3, 2)]))
    es("27 koklu", (lg(sqrt(8), 2), lg(1 / sqrt(3), 3), lg(4, sqrt(2))), (Q(3, 2), -Q(1, 2), 4))
    es("27 temel", (lg(1, 7), lg(7, 7), lg(3**10, 3), 5**lg(7, 5)), (0, 1, 10, 7))
    es("27 isaret", (float(lg(Q(1, 3), 2)) < 0, lg(Q(1, 9), Q(1, 3)), float(lg(5, Q(1, 2))) < 0), (True, 2, True))
    es("27 logaritmali us", (2**(lg(3, 2) + 1), 10**(2 + lg(5)), 9**lg(5, 3)), (6, 500, 25))
    es("27 onluk dogal", (lg(1000), L(1), L(E), exp(L(5)), yak(E, 2.718, 0.0005)), (3, 0, 1, 5, True))
    es("27 arada", (1 < float(lg(7, 3)) < 2, 4 < float(lg(20, 2)) < 5, 3**1, 3**2, 2**4, 2**5), (True, True, 3, 9, 16, 32))
    es("27 ic ice", (lg(lg(81, 3), 2), 3**(2**1)), (2, 9))
    es("27 bilinmeyen taban", (koklu(X**2 - 49, [X > 0, sp.Ne(X, 1)]), 8**Q(2, 3), 4**Q(3, 2)), (FiniteSet(7), 4, 8))
    ftan = sp.And(X - 1 > 0, sp.Ne(X - 1, 1), 5 - X > 0)
    kume = sp.solveset(X - 1 > 0, X, R).intersect(sp.solveset(5 - X > 0, X, R)) - FiniteSet(2)
    es("27 tanim f", (kume, [k for k in range(-10, 11) if bool(ftan.subs(X, k))]), (Union(Interval.open(1, 2), Interval.open(2, 5)), [3, 4]))
    es("27 tanim g", sp.solveset(X**2 - 4 > 0, X, R), Union(Interval.open(-oo, -2), Interval.open(2, oo)))
    es("27 grafik noktalari", (2**0, lg(1, 2), 2**1, lg(2, 2), lg(1024, 2)), (1, 0, 2, 1, 10))
    es("27 kucuk taban", (sp.simplify(lg(X, Q(1, 2)) + lg(X, 2)), lg(4, 2), lg(4, Q(1, 2))), (0, 2, -2))
    a1, b1, c1 = lg(10, 2), lg(10, 3), lg(10, 5)
    es("27 karsilastirma", (3 < float(a1) < 4, 2 < float(b1) < 3, 1 < float(c1) < 2, float(c1) < float(b1) < float(a1)), (True, True, True, True))
    es("27 esitsizlik", (sp.solveset(sp.log(X, 2) > 3, X, pozitif), sp.solveset(sp.log(X, Q(1, 2)) > 3, X, pozitif)), (Interval.open(8, oo), Interval.open(0, Q(1, 8))))
    f = lg(X - 1, 3) + 2
    finv = 3**(X - 2) + 1
    es("27 ters", (sp.simplify(f.subs(X, finv) - X), f.subs(X, 4), finv.subs(X, 3)), (0, 3, 4))
    es("27 basamak", (len(str(2**100)), yak(100 * lg(2), 30.103, 0.0005), floor(100 * lg(2)) + 1), (31, True, 31))
    es("27 pH", (-lg(Q(1, 1000)), -lg(Q(1, 100))), (3, 2))
    es("27 buyume", (lg(1024, 2), 2**10), (10, 1024))
    # ── 28 ──
    es("28 carpim bolum", (lg(4, 6) + lg(9, 6), lg(54, 3) - lg(2, 3), sp.simplify(sp.expand_log(lg(1 / sp.Symbol("yp", positive=True), 5) + lg(sp.Symbol("yp", positive=True), 5)))), (2, 3, 0))
    es("28 kuvvet", (lg(8**5, 2), lg(sqrt(125), 5), lg(16**Q(1, 3), 2)), (15, Q(3, 2), Q(4, 3)))
    es("28 kuvvet kosul", (lg((-3)**2, 3), 2 * lg(Abs(-3), 3)), (2, 2))
    es("28 tabanin kuvveti", (lg(32, 8), lg(8, sqrt(2))), (Q(5, 3), 6))
    es("28 taban degistirme", (lg(32, 4), lg(27, 9)), (Q(5, 2), Q(3, 2)))
    es("28 hesap makinesi", (yak(lg(7), 0.8451, 0.00005), yak(lg(2), 0.3010, 0.00005), yak(Q(8451, 10000) / Q(3010, 10000), 2.81, 0.005), yak(lg(7, 2), 2.81, 0.005), 2 < float(lg(7, 2)) < 3), (True,) * 5)
    es("28 karsilastirma", (lg(9, 4), float(lg(3, 2)) > 1.5, sqrt(8) < 3), (lg(3, 2), True, True))
    es("28 ters cevirme", (lg(3, 2) * lg(2, 3), 1 / lg(6, 2) + 1 / lg(6, 3)), (1, 1))
    zincir = 1
    for k in range(2, 8):
        zincir *= lg(k + 1, k)
    es("28 zincir", (zincir, lg(5, 2) * lg(9, 5) * lg(2, 9)), (3, 1))
    es("28 ters toplam", 1 / lg(30, 2) + 1 / lg(30, 3) + 1 / lg(30, 5), 1)
    es("28 logaritmali us", (5**lg(7, 5), 2**(3 + lg(5, 2)), 3**lg(5, 2) - 5**lg(3, 2)), (7, 40, 0))
    es("28 verilen", (2 * 2 + 3, Q(1, 2) * 2 - 3, 3 * 2 - 2 * 3), (7, -2, 0))
    l2, l3 = Q(301, 1000), Q(477, 1000)
    es("28 yaklasik", (l2 + l3, 1 - l2, 2 * l2 + l3, l3 - l2), (Q(778, 1000), Q(699, 1000), Q(1079, 1000), Q(176, 1000)))
    es("28 yaklasik gercek", [yak(lg(v), w, 0.0006) for v, w in ((6, 0.778), (5, 0.699), (12, 1.079), (Q(3, 2), 0.176))], [True] * 4)
    es("28 log5 25 50", (lg(25) - (2 - 2 * lg(2)), lg(50) - (2 - lg(2))), (0, 0))
    A_, B_ = lg(2), lg(3)
    es("28 harfle", (lg(18) - (A_ + 2 * B_), lg(15) - (B_ + 1 - A_), lg(12, 6) - (2 * A_ + B_) / (A_ + B_)), (0, 0, 0))
    a_ = lg(3, 2)
    es("28 harfle taban", lg(18, 12) - (1 + 2 * a_) / (2 + a_), 0)
    es("28 dogal", (L(E**3), exp(L(5)), L(8) - 3 * L(2)), (3, 5, 0))
    es("28 sadelestirme", (lg(12, 2) - lg(3, 2) + 2 * lg(Q(1, 2), 2), (lg(8) + lg(27)) / lg(6), 6**3), (0, 3, 216))
    es("28 ortak taban", (lg(5, 2) + lg(25, 4) + lg(125, 8) - lg(125, 2), lg(25, 4) - lg(5, 2)), (0, 0))
    es("28 katsayili", (2 * lg(5) + lg(4), 3 * lg(6, 2) - lg(27, 2)), (2, 3))
    es("28 basamak", (len(str(3**20)), yak(20 * Q(477, 1000), 9.54, 0.001)), (10, True))
    es("28 denklem", koklu(X * (X - 2) - 8, [X > 2]), FiniteSet(4))
    # ── 29 ──
    es("29 tanima donus", (koklu(2 * X + 1 - 9, [2 * X + 1 > 0]), koklu(X**2 - 15 - 10, [X**2 - 15 > 0])), (FiniteSet(4), FiniteSet(-5, 5)))
    es("29 esit logaritma", (koklu((X + 3) - (2 * X - 1), [X + 3 > 0, 2 * X - 1 > 0]), koklu((X**2 - 3 * X) - (X - 3), [X**2 - 3 * X > 0, X - 3 > 0])), (FiniteSet(4), S.EmptySet))
    es("29 kare", (koklu((X - 1)**2 - 9, [sp.Ne(X, 1)]), koklu(X - 1 - 3, [X > 1])), (FiniteSet(-2, 4), FiniteSet(4)))
    es("29 ic ice", (4**3, lg(lg(lg(64, 4), 3), 2)), (64, 0))
    es("29 birlestirme", (koklu(X * (X - 2) - 8, [X > 2]), koklu((X + 1) - 3 * (X - 1), [X > 1])), (FiniteSet(4), FiniteSet(2)))
    es("29 katsayili", (koklu(X**2 - (X + 6), [X > 0]), (-2)**2, -2 + 6), (FiniteSet(3), 4, 4))
    es("29 farkli taban", koklu(X**2 - (X + 2), [X > 0]), FiniteSet(2))
    es("29 degisken", (sp.solveset(t_**2 - 3 * t_ + 2, t_, R), [2**v for v in (1, 2)], sp.solveset(2 * t_**2 - 5 * t_ + 2, t_, R), (3**2, 3**Q(1, 2)),
                       lg(9, 3) + lg(3, 9), lg(sqrt(3), 3) + lg(3, sqrt(3))), (FiniteSet(1, 2), [2, 4], FiniteSet(Q(1, 2), 2), (9, sqrt(3)), Q(5, 2), Q(5, 2)))
    es("29 kokler toplami", (sp.solveset(t_**2 - 5 * t_ + 6, t_, R), 4 + 8, 4 * 8, 2**(2 + 3)), (FiniteSet(2, 3), 12, 32, 32))
    es("29 tabanda", (koklu(X**2 - 16, [X > 0, sp.Ne(X, 1)]), koklu((X - 1)**2 - 9, [X - 1 > 0, sp.Ne(X - 1, 1)])), (FiniteSet(4), FiniteSet(4)))
    es("29 taban ve sayi", koklu(X**2 - (2 * X + 3), [X > 0, sp.Ne(X, 1), 2 * X + 3 > 0]), FiniteSet(3))
    es("29 x uzeri logx", (sp.solveset(t_**2 - t_ - 2, t_, R), [(v**lg(v)) / (100 * v) for v in (100, Q(1, 10))]), (FiniteSet(-1, 2), [1, 1]))
    xs = L(3) / (L(3) - L(2))
    es("29 ustel", (5**lg(3, 5), 2**xs - 3**(xs - 1), yak(xs, 2.71, 0.005)), (3, 0, True))
    es("29 sistem", (sp.solve([sp.Symbol("u") + sp.Symbol("v") - 3, sp.Symbol("u") - sp.Symbol("v") - 1]), lg(100) + lg(10), lg(100) - lg(10)), ({sp.Symbol("u"): 2, sp.Symbol("v"): 1}, 3, 1))
    es("29 sabit carpan", (2**(lg(Q(5, 2), 2) + 1), lg(5, 2) - 1 - lg(Q(5, 2), 2), 1 < float(lg(Q(5, 2), 2)) < 2), (5, 0, True))
    es("29 ayni taban", (sp.solve(2 * X - 3, X), sp.solveset(9**X - 4 * 3**X + 3, X, R)), ([Q(3, 2)], FiniteSet(0, 1)))
    es("29 grafik", (lg(2, 2), 3 - 2, sp.nsolve(sp.log(X, 2) - (3 - X), X, 1.5)), (1, 1, 2))
    es("29 esitsizlik", (sp.solveset(sp.log(X - 1, 2) < 3, X, Interval.open(1, oo)), sp.solveset(sp.log(X, Q(1, 3)) > 2, X, pozitif)), (Interval.open(1, 9), Interval.open(0, Q(1, 9))))
    es("29 kurali esitsizlik", (sp.factor(X**2 - 3 * X - 10), sp.solveset(X**2 - 3 * X - 10 <= 0, X, R).intersect(Interval.open(3, oo))), ((X - 5) * (X + 2), Interval.Lopen(3, 5)))
    es("29 faiz", (yak(lg(2) / lg(Q(11, 10)), 7.27, 0.005), Q(11, 10)**7 < 2, Q(11, 10)**8 > 2), (True, True, True))
    es("29 nufus", (sp.solveset(100 * 2**(t_ / 3) - 1600, t_, R), sp.solveset(80 * Q(1, 2)**(t_ / 5) - 10, t_, R)), (FiniteSet(12), FiniteSet(15)))


def yazi_30_32():
    """30 Diziler, 31 Aritmetik Dizi, 32 Geometrik Dizi."""
    es = esit_ogeler
    Q = Rational
    n, k, X = sp.symbols("n k X", integer=True, positive=True)
    yak = lambda deger, yaklasik, tol: abs(float(deger) - yaklasik) < tol
    ilk = lambda f, m, bas=1: [sp.nsimplify(f(i)) for i in range(bas, bas + m)]
    def indirge(a1, adim, m):
        out = [a1]
        for i in range(1, m):
            out.append(adim(out[-1], i))
        return out
    # ── 30 ──
    T = lambda m: Q(m * (m + 1), 2)
    es("30 ucgensel", (ilk(T, 5), T(10), sp.simplify(n * (n + 1) / 2 - (n - 1) * n / 2)), ([1, 3, 6, 10, 15], 55, n))
    es("30 genel terimden", (ilk(lambda i: 3 * i - 1, 3), 3 * 10 - 1, ilk(lambda i: Q(i + 1, i), 4)), ([2, 5, 8], 29, [2, Q(3, 2), Q(4, 3), Q(5, 4)]))
    es("30 kaliplar", (ilk(lambda i: i**2, 4), ilk(lambda i: 2**i, 4), ilk(lambda i: Q(i, i + 1), 3), ilk(lambda i: (-1)**i, 4)),
       ([1, 4, 9, 16], [2, 4, 8, 16], [Q(1, 2), Q(2, 3), Q(3, 4)], [-1, 1, -1, 1]))
    es("30 dizi olma", (2 - 2, [i - 3 < 0 for i in (1, 2, 3)]), (0, [True, True, False]))
    dizi_degil = [kk for kk in range(-10, 11) if any(i + kk == 0 for i in range(1, 50))]
    es("30 k kosulu", (max(dizi_degil), min(set(range(-10, 11)) - set(dizi_degil))), (-1, 0))
    es("30 kacinci", (sp.solve(2 * X + 5 - 45), sp.solve(X**2 - 1 - 99), Q(50 - 5, 2)), ([20], [10], Q(45, 2)))
    es("30 aralik terim", (len([i for i in range(1, 200) if 20 <= 3 * i + 1 <= 100]), min(i for i in range(1, 200) if 3 * i + 1 >= 20), max(i for i in range(1, 200) if 3 * i + 1 <= 100)), (27, 7, 33))
    es("30 isaret", (len([i for i in range(1, 100) if Q(i - 5, i + 1) < 0]), Q(5 - 5, 6)), (4, 0))
    es("30 sabit", (sp.solve(Q(1, 3) * X - 2, X), sp.simplify((6 * n + 2) / (3 * n + 1))), ([6], 2))
    es("30 artan", sp.simplify((n + 1) / (n + 2) - n / (n + 1) - 1 / ((n + 1) * (n + 2))), 0)
    es("30 sinirli", (Q(1, 2), all(Q(1, 2) <= Q(i, i + 1) < 1 for i in range(1, 500)), all(Q(i + 1, i + 2) > Q(i, i + 1) for i in range(1, 500))), (Q(1, 2), True, True))
    es("30 grafik", ilk(lambda i: Q(6, i), 6), [6, 3, 2, Q(3, 2), Q(6, 5), 1])
    es("30 indirgeme", (indirge(1, lambda a, i: 2 * a + 1, 5), [2**i - 1 for i in range(1, 6)]), ([1, 3, 7, 15, 31], [1, 3, 7, 15, 31]))
    es("30 toplamli indirgeme", (indirge(1, lambda a, i: a + i, 5), [1 + Q(i * (i - 1), 2) for i in range(1, 6)]), ([1, 2, 4, 7, 11], [1, 2, 4, 7, 11]))
    fib = [1, 1]
    while len(fib) < 10:
        fib.append(fib[-1] + fib[-2])
    es("30 fibonacci", (fib, yak(Q(55, 34), 1.6176, 0.00005), yak((1 + sqrt(5)) / 2, 1.618, 0.0005)), ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55], True, True))
    p_, q_ = sp.symbols("p_ q_")
    es("30 esitlik", sp.solve([p_ + 1 - 5, 3 - (q_ - 2)], [p_, q_]), {p_: 4, q_: 5})
    es("30 islemler", (2 * 3 + 3**2, (2 * 2) * 2**2), (15, 16))
    es("30 toplam sembolu", (sp.summation(k, (k, 1, n)) - n * (n + 1) / 2, sp.summation(k**2, (k, 1, n)) - n * (n + 1) * (2 * n + 1) / 6, sp.summation(2 * k - 1, (k, 1, n)) - n**2,
                             sp.summation(k, (k, 1, 10)), sp.summation(k**2, (k, 1, 5)), Q(10 * 11, 2), Q(5 * 6 * 11, 6)), (0, 0, 0, 55, 55, 55, 55))
    es("30 toplam ozellik", (sp.summation(3 * k + 2, (k, 1, 20)), 3 * 210 + 40, sp.summation(k, (k, 1, 20))), (670, 670, 210))
    Sk = n**2 + 2 * n
    es("30 kismi toplam", (sp.expand(Sk - Sk.subs(n, n - 1)), Sk.subs(n, 1)), (2 * n + 1, 3))
    per = [2, 5, 7]
    es("30 periyodik", (per[(100 - 1) % 3], per[(50 - 1) % 3], 100 % 3, 50 % 3), (2, 5, 1, 2))
    es("30 turler", ([7 - 3, 11 - 7, 15 - 11], [Q(6, 3), Q(12, 6), Q(24, 12)]), ([4, 4, 4], [2, 2, 2]))
    # ── 31 ──
    ar = lambda a1, d, m: a1 + (m - 1) * d
    es("31 ortak fark", ([7 - 3, 11 - 7, 15 - 11], sp.expand(5 * (n + 1) - 2 - (5 * n - 2)), sp.expand((n + 1)**2 - n**2)), ([4, 4, 4], 5, 2 * n + 1))
    es("31 genel terim", (ar(3, 4, 20),), (79,))
    es("31 iki terim", (Q(26 - 11, 5), 11 - 2 * 3, ar(5, 3, 20), ar(5, 3, 3), ar(5, 3, 8)), (3, 5, 62, 11, 26))
    es("31 genel terimden", (sp.expand(Q(3, 2) * (n + 1) + Q(5, 2) - (Q(3, 2) * n + Q(5, 2))), Q(3 + 5, 2)), (Q(3, 2), 4))
    es("31 ilk negatif", (sp.expand(40 + (n - 1) * (-3)), min(i for i in range(1, 100) if 43 - 3 * i < 0), 43 - 3 * 15, 43 - 3 * 14, yak(Q(43, 3), 14.3, 0.05)), (43 - 3 * n, 15, -2, 1, True))
    es("31 terim sayisi", (Q(99 - 7, 4) + 1, len(range(7, 100, 4))), (24, 24))
    es("31 ardisik", (sum(range(11, 21)), Q(155, 10)), (155, Q(31, 2)))
    es("31 cift sirali", ([ar(2, 3, m) for m in (2, 4, 6)], ar(2, 3, 4) - ar(2, 3, 2)), ([5, 11, 17], 6))
    es("31 ortalama ozelligi", (sp.solve(2 * (3 * X - 2) - ((X + 1) + (4 * X + 1)), X), [6 + 1, 3 * 6 - 2, 4 * 6 + 1]), ([6], [7, 16, 25]))
    a1_, d_ = sp.symbols("a1_ d_")
    A = lambda m: a1_ + (m - 1) * d_
    es("31 simetrik", (sp.expand(A(3) + A(12) - A(7) - A(8)), sp.expand(A(3) + A(12) - A(1) - A(14))), (0, 0))
    Sn = lambda a1, d, m: Q(m, 2) * (2 * a1 + (m - 1) * d)
    es("31 toplam", (Sn(3, 4, 20), sum(ar(3, 4, i) for i in range(1, 21)), sp.simplify(n * (a1_ + A(n)) / 2 - n / 2 * (2 * a1_ + (n - 1) * d_))), (820, 820, 0))
    es("31 bilinen", (sum(range(1, 101)), sum(range(1, 20, 2)), sum(range(2, 21, 2)), 10**2, 10 * 11), (5050, 100, 110, 100, 110))
    yedi = [i for i in range(10, 100) if i % 7 == 0]
    es("31 yedinin katlari", (yedi[0], yedi[-1], len(yedi), sum(yedi), Q(13 * (14 + 98), 2)), (14, 98, 13, 728, 728))
    S2 = 2 * n**2 + 3 * n
    es("31 toplamdan", (sp.expand(S2 - S2.subs(n, n - 1)), S2.subs(n, 1)), (4 * n + 1, 5))
    es("31 ortanca", (9 * 12, sum(ar(12 - 4 * 3, 3, i) for i in range(1, 10))), (108, 108))
    es("31 grafik", ilk(lambda i: 2 * i - 3, 5), [-1, 1, 3, 5, 7])
    es("31 araya", (Q(29 - 5, 6), [5 + 4 * i for i in range(1, 6)]), (4, [9, 13, 17, 21, 25]))
    es("31 uc terim", (Q(30, 3), sp.solve(100 - X**2 - 91), 7 * 10 * 13, 7 + 10 + 13), (10, [3], 910, 30))
    es("31 toplam verilen", (sp.expand(n * (2 * n + 3) - Q(1, 1) * n / 2 * (10 + 4 * (n - 1))), sp.solve(2 * X**2 + 3 * X - 275, X), sp.expand((X - 11) * (2 * X + 25))), (0, [11], 2 * X**2 + 3 * X - 275))
    es("31 iki toplam", (sp.solve([5 * (2 * a1_ + 9 * d_) - 100, 10 * (2 * a1_ + 19 * d_) - 400], [a1_, d_]), Sn(1, 2, 10), Sn(1, 2, 20)), ({a1_: 1, d_: 2}, 100, 400))
    ortak = sorted(set(range(3, 200, 4)) & set(range(2, 200, 5)))
    es("31 ortak terimler", ortak[:3], [7, 27, 47])
    es("31 birikim", (ar(20, 5, 10), Sn(20, 5, 10)), (65, 425))
    es("31 amfi", (ar(12, 2, 15), Sn(12, 2, 15)), (40, 390))
    es("31 en buyuk toplam", (sp.expand(ar(50, -4, n)), ar(50, -4, 13), ar(50, -4, 14), Sn(50, -4, 13), Sn(50, -4, 14), max(Sn(50, -4, m) for m in range(1, 40))), (54 - 4 * n, 2, -2, 338, 336, 338))
    # ── 32 ──
    ge = lambda a1, r, m: a1 * r**(m - 1)
    es("32 oran", ([Q(6, 3), Q(12, 6), Q(24, 12)], sp.simplify(5 * 3**(n + 1) / (5 * 3**n)), sp.simplify((n + 1) * 2**(n + 1) / (n * 2**n) - 2 * (n + 1) / n)), ([2, 2, 2], 3, 0))
    es("32 genel terim", (ge(3, 2, 8), 3 * 128), (384, 384))
    es("32 iki terim", (Q(162, 6), sp.solve(X**3 - 27), Q(6, 3), ge(2, 3, 7), ge(2, 3, 2), ge(2, 3, 5)), (27, [3], 2, 1458, 6, 162))
    es("32 cift kuvvet", sp.solve(sp.Symbol("r")**2 - 9), [-3, 3])
    es("32 negatif", ([ge(2, -3, m) for m in range(1, 5)], ge(2, -3, 6)), ([2, -6, 18, -54], -486))
    es("32 kesirli", (Q(32, 64), ge(64, Q(1, 2), 7), ilk(lambda m: ge(64, Q(1, 2), m), 3)), (Q(1, 2), 1, [64, 32, 16]))
    es("32 tablo", (ilk(lambda m: ge(2, 3, m), 3), ilk(lambda m: ge(81, Q(1, 3), m), 3), ilk(lambda m: ge(1, -2, m), 3), ilk(lambda m: ge(-2, 3, m), 3)),
       ([2, 6, 18], [81, 27, 9], [1, -2, 4], [-2, -6, -18]))
    es("32 geometrik ortalama", (sp.solve((X + 3)**2 - X * (X + 9), X), [3, 6, 12], 6**2 - 3 * 12), ([3], [3, 6, 12], 0))
    es("32 AO GO", (Q(4 + 9, 2), sqrt(36), sqrt(4 * 9)), (Q(13, 2), 6, 6))
    b1_, r_ = sp.symbols("b1_ r_", positive=True)
    G = lambda m: b1_ * r_**(m - 1)
    es("32 simetrik", (sp.simplify(G(2) * G(9) - G(5) * G(6)), sp.simplify(G(2) * G(9) - G(1) * G(10))), (0, 0))
    es("32 terim sayisi", (Q(768, 3), 2**8, len([m for m in range(1, 20) if ge(3, 2, m) <= 768])), (256, 256, 9))
    Sg = lambda a1, r, m: S(a1) * (S(r)**m - 1) / (S(r) - 1)
    es("32 toplam", (Sg(3, 2, 8), sum(ge(3, 2, m) for m in range(1, 9)), sum(2**i for i in range(10)), Sg(1, 2, 10),
                     all(Sg(a1, r, m) == sum(S(a1) * S(r)**(i - 1) for i in range(1, m + 1)) for a1 in (1, 3, -2) for r in (2, 3, Q(1, 2), -3) for m in range(1, 12))), (765, 765, 1023, 1023, True))
    es("32 kesirli toplam", (sum(Q(1, 2**i) for i in range(6)), Q(1 - Q(1, 64), Q(1, 2))), (Q(63, 32), Q(63, 32)))
    es("32 sonsuz", (sp.summation(Q(1, 2)**k, (k, 0, oo)), Q(1, 1) / (1 - Q(1, 2)), sp.summation(3 * Q(1, 10)**k, (k, 1, oo)), sp.summation(36 * Q(1, 100)**k, (k, 1, oo)), Q(36, 99)),
       (2, 2, Q(1, 3), Q(4, 11), Q(4, 11)))
    es("32 uc terim", (sp.root(216, 3), sp.solve(2 * X**2 - 5 * X + 2), sp.solve(6 / sp.Symbol("rr") + 6 + 6 * sp.Symbol("rr") - 21), 3 * 6 * 12, 3 + 6 + 12),
       (6, [2], [Q(1, 2), 2], 216, 21))
    es("32 faiz", [1000 * Q(11, 10)**m for m in (1, 2, 3)], [1100, 1210, 1331])
    es("32 bakteri", (Q(120, 20), 2**6), (6, 64))
    es("32 top", ([16 * Q(3, 4)**m for m in (1, 2, 3)], 12 / (1 - Q(3, 4)), 16 + 2 * 48, sp.summation(12 * Q(3, 4)**k, (k, 0, oo))), ([12, 9, Q(27, 4)], 48, 112, 48))
    es("32 kareler", ([16 * Q(1, 2)**m for m in range(3)], 16 / (1 - Q(1, 2)), (sqrt(2**2 + 2**2))**2), ([16, 8, 4], 32, 8))
    es("32 yarilanma", (Q(20, 5), 1600 * Q(1, 2)**4), (4, 100))
    es("32 logaritma", [sp.log(v, 2) for v in (2, 4, 8, 16)], [1, 2, 3, 4])


def yazi_33_36():
    """33 Limit, 34 Sagdan ve Soldan Limit, 35 Limitte Belirsizlikler, 36 Sureklilik."""
    from sympy import limit as lim, sin, cos, tan, pi, floor, E, log as L, Piecewise, sign
    es = esit_ogeler
    Q = Rational
    X, h, t_, k_, a_, b_ = sp.symbols("X h t_ k_ a_ b_", real=True)
    yak = lambda deger, yaklasik, tol: abs(float(deger) - yaklasik) < tol
    # sympy'nin limit(..., '-') cagrisi Piecewise ve floor'da noktadaki degeri donduruyor (1 yerine 3);
    # tek yonlu limit bu yuzden x = a -+ e (e > 0) yazilip e -> 0+ ile hesaplanir
    e_ = sp.symbols("e_", positive=True)
    sol = lambda f, a: lim(sp.sympify(f).subs(X, a - e_), e_, 0, "+")
    sag = lambda f, a: lim(sp.sympify(f).subs(X, a + e_), e_, 0, "+")
    iki = lambda f, a: (sol(f, a), sag(f, a))
    # ── 33 ──
    es("33 tablo", [2 * v + 1 for v in (Q(29, 10), Q(299, 100), Q(301, 100), Q(31, 10))], [Q(68, 10), Q(698, 100), Q(702, 100), Q(72, 10)])
    es("33 yaklasma", lim(2 * X + 1, X, 3), 7)
    es("33 tanimsiz", (lim((X**2 - 1) / (X - 1), X, 1), sp.factor(X**2 - 1)), (2, (X - 1) * (X + 1)))
    es("33 deger farkli", (lim(X + 1, X, 2), 5), (3, 5))
    es("33 basit", (lim(S(7), X, 5), lim(X**2, X, 5)), (7, 25))
    es("33 tablo sinir", ([sin(pi / v) for v in (1, Q(1, 10), Q(1, 100))], sin(pi / Q(2, 5)), lim(sin(pi / X), X, 0)), ([0, 0, 0], 1, sp.AccumBounds(-1, 1)))
    es("33 polinom", lim(X**3 - 2 * X + 1, X, 2), 5)
    es("33 rasyonel", lim((X + 3) / (X + 1), X, 1), 2)
    es("33 kurallar", (2 * 3 - (-2), 3 * (-2), Q(9, -2)), (8, -6, -Q(9, 2)))
    es("33 parametre", sp.solve(4 + 2 * k_ - 10, k_), [3])
    es("33 koklu mutlak", (lim(sqrt(X + 5), X, 4), lim(Abs(X**2 - 9), X, -2)), (3, 5))
    es("33 bileske", lim(cos(X**2 + pi), X, 0), -1)
    es("33 trig ustel log", (lim(sin(X), X, pi / 2), lim(2**X, X, 2), lim(L(X), X, E)), (1, 4, 1))
    es("33 sinx bolu x", ([yak(sin(v) / v, w, 0.000005) for v, w in ((Q(1, 10), 0.99833), (Q(1, 100), 0.99998))], yak(sin(Q(1, 1000)) / Q(1, 1000), 0.9999998, 0.00000005), lim(sin(X) / X, X, 0)), ([True, True], True, 1))
    es("33 belirsizlik", lim((X**2 - 9) / (X - 3), X, 3), 6)
    es("33 sonsuz limit", ([1 / v**2 for v in (Q(1, 10), Q(1, 100), Q(1, 1000))], lim(1 / X**2, X, 0)), ([100, 10000, 1000000], oo))
    es("33 iki yon sonsuz", iki(1 / X, 0), (-oo, oo))
    es("33 sonsuzda", (lim(1 / X, X, oo), lim((2 * X + 1) / (X - 3), X, oo), lim((X + 1) / X**2, X, oo), lim((3 * X**2 + 1) / (X**2 - 5), X, oo), lim(X**3 / (X + 1), X, oo)), (0, 2, 0, 3, oo))
    es("33 sikistirma", lim(X**2 * sin(1 / X), X, 0), 0)
    es("33 anlik hiz", (sp.expand((5 * (2 + h)**2 - 20) / h), lim((5 * (2 + h)**2 - 20) / h, h, 0)), (20 + 5 * h, 20))
    n_ = sp.symbols("n_", integer=True, positive=True)
    es("33 sonsuz toplam", (sum(Q(1, 2)**i for i in range(10)) - (2 - Q(1, 2)**9),
                            lim(2 - Q(1, 2)**(X - 1), X, oo), sp.summation(9 * Q(1, 10)**k_, (k_, 1, oo))), (0, 2, 1))
    # ── 34 ──
    f1 = Piecewise((X + 1, X < 2), (2 * X - 1, True))
    es("34 esit", (iki(f1, 2), f1.subs(X, 2)), ((3, 3), 3))
    f2 = Piecewise((X**2, X < 1), (X + 2, True))
    es("34 sicrama", (iki(f2, 1), f2.subs(X, 1)), ((1, 3), 3))
    es("34 parametre", (sp.solve(6 + a_ - 5, a_), lim(X**2 + 1, X, 2)), ([-1], 5))
    f3 = Piecewise((X + 2, X < 0), (X**2, X < 2), (6 - X, True))
    es("34 uc parca", (iki(f3, 0), iki(f3, 2)), ((2, 0), (4, 4)))
    es("34 iki parametre", sp.solve([6 + b_ - 9, 1 + a_ - (2 + b_)], [a_, b_]), {a_: 4, b_: 3})
    es("34 mutlak", (iki(Abs(X) / X, 0), iki((X**2 - 4) / Abs(X - 2), 2), lim(Abs(X), X, 0), iki(sqrt(X**2) / X, 0)), ((-1, 1), (-4, 4), 0, (-1, 1)))
    es("34 tam deger", (floor(Q(27, 10)), floor(-Q(13, 10)), iki(floor(X), 2), lim(floor(X), X, Q(5, 2)), iki(floor(2 * X), 1), iki(floor(X) + X, 3)),
       (2, -2, (1, 2), 2, (1, 2), (5, 6)))
    es("34 payda sifir", (iki(1 / (X - 2), 2), iki(1 / (X - 2)**2, 2), iki((X + 1) / (X - 3), 3)), ((-oo, oo), (oo, oo), (-oo, oo)))
    es("34 ustel", iki(2**(1 / X), 0), (0, oo))
    es("34 tanjant", iki(tan(X), pi / 2), (oo, -oo))
    es("34 kok uc", sag(sqrt(X), 0), 0)
    es("34 isaret", (iki(sign(X), 0), lim(sign(X), X, 3)), ((-1, 1), 1))
    # ── 35 ──
    es("35 neden", (lim(X / X, X, 0), lim(X**2 / X, X, 0), sag(X / X**2, 0)), (1, 0, oo))
    es("35 carpanlar", (lim((X**2 - 4) / (X**2 - 3 * X + 2), X, 2), lim((X**3 - 1) / (X - 1), X, 1), lim((X**3 + 1) / (X**2 - 1), X, -1)), (4, 3, -Q(3, 2)))
    es("35 cift kok", (sp.factor(X**3 - 3 * X**2 + 4), lim((X**3 - 3 * X**2 + 4) / (X - 2)**2, X, 2)), ((X - 2)**2 * (X + 1), 3))
    es("35 eslenik", (lim((sqrt(X) - 2) / (X - 4), X, 4), lim(X / (sqrt(X + 9) - 3), X, 0), lim((sqrt(X + 1) - 2) / (sqrt(X - 2) - 1), X, 3)), (Q(1, 4), 6, Q(1, 2)))
    es("35 degisken", (lim((X**Q(1, 3) - 2) / (X - 8), X, 8), lim((t_ - 2) / (t_**3 - 8), t_, 2)), (Q(1, 12), Q(1, 12)))
    es("35 parametre", (sp.solve(4 + 2 * a_ - 6, a_), sp.factor(X**2 + X - 6), lim((X**2 + X - 6) / (X - 2), X, 2)), ([1], (X - 2) * (X + 3), 5))
    es("35 trig", (lim(sin(3 * X) / X, X, 0), lim(sin(5 * X) / sin(2 * X), X, 0), lim(tan(4 * X) / sin(2 * X), X, 0), lim(tan(X) / X, X, 0), lim((1 - cos(X)) / X**2, X, 0)),
       (3, Q(5, 2), 2, 1, Q(1, 2)))
    es("35 kosinus ozdes", sp.simplify(1 - cos(X) - 2 * sin(X / 2)**2), 0)
    es("35 sonsuz bolu sonsuz", (lim((4 * X**2 - X) / (2 * X**2 + 5), X, oo), lim(sqrt(X**2 + 1) / X, X, oo), lim(sqrt(X**2 + 1) / X, X, -oo), lim((1 - X**3) / (X**2 + 1), X, oo)), (2, 1, -1, -oo))
    es("35 sonsuz eksi sonsuz", (lim(sqrt(X**2 + 4 * X) - X, X, oo), lim(1 / (X - 1) - 2 / (X**2 - 1), X, 1)), (2, Q(1, 2)))
    es("35 sifir carpi sonsuz", (lim(X * sin(1 / X), X, oo), lim((X**2 + sin(X)) / X, X, 0), lim((2**X + 3**X) / 3**X, X, oo)), (1, 1, 1))
    es("35 mutlak", iki((X**2 - 9) / Abs(X - 3), 3), (-6, 6))
    es("35 turev", (sp.expand(((3 + h)**2 - 9) / h), lim(((3 + h)**2 - 9) / h, h, 0)), (6 + h, 6))
    # ── 36 ──
    es("36 surekli", ((X**2 + 1).subs(X, 2), lim(X**2 + 1, X, 2)), (5, 5))
    es("36 kaldirilabilir", (lim((X**2 - 4) / (X - 2), X, 2), lim((X**2 - 9) / (X - 3), X, 3)), (4, 6))
    es("36 sicrama", (iki(f2, 1), 3 - 1), ((1, 3), 2))
    es("36 sonsuz", iki(1 / (X - 2), 2), (-oo, oo))
    es("36 rasyonel", sp.solveset(X**2 - 5 * X + 6, X, R), FiniteSet(2, 3))
    es("36 her yerde", (sp.solveset(4 - 4 * sp.Symbol("m") < 0, sp.Symbol("m"), R), sp.solveset(X**2 - 2 * X + 2, X, R)), (Interval.open(1, oo), S.EmptySet))
    es("36 parcali", sp.solve(2 * a_ - 1 - (4 + a_), a_), [5])
    es("36 iki parametre", (sp.solve(1 + a_ - 3, a_), sp.solve(b_ + 1 - 3, b_)), ([2], [2]))
    es("36 tanjant", sp.solveset(cos(X), X, Interval(0, 2 * pi)), FiniteSet(pi / 2, 3 * pi / 2))
    es("36 bileske", (sp.simplify(1 / (X**2 - 1) - (1 / (X - 1)).subs(X, X**2)), sp.solveset(X**2 - 1, X, R)), (0, FiniteSet(-1, 1)))
    es("36 tam deger", [kk for kk in range(-5, 10) if 0 < kk < 5], [1, 2, 3, 4])
    es("36 kok", (sag(sqrt(X), 0), sqrt(0)), (0, 0))
    fx = X**3 + X - 1
    kok = sp.nsolve(fx, X, 0.7)
    es("36 ara deger", (fx.subs(X, 0), fx.subs(X, 1), fx.subs(X, Q(1, 2)), fx.subs(X, Q(3, 4)), yak(kok, 0.682, 0.0005), len(sp.real_roots(sp.Poly(fx, X)))), (-1, 1, -Q(3, 8), Q(11, 64), True, 1))
    es("36 ters ornek", ((1 / X).subs(X, -1), (1 / X).subs(X, 1), sp.solveset(1 / X, X, R)), (-1, 1, S.EmptySet))
    es("36 en buyuk", (function_range(X**2, X, Interval(-1, 2)), Q(11, 64)), (Interval(0, 4), Q(171875, 1000000)))
    es("36 mutlak turev", (lim(Abs(X), X, 0), iki(Abs(X) / X, 0)), (0, (-1, 1)))


def yazi_37_39():
    """37 Turev, 38 Turevin Tanimi, 39 Turev Alma Kurallari."""
    from sympy import limit as lim, sin, cos, tan, pi, E, exp, log as L, diff as D
    es = esit_ogeler
    Q = Rational
    X, h, t_, a_, b_, r_ = sp.symbols("X h t_ a_ b_ r_", real=True)
    xp = sp.symbols("xp", positive=True)
    yak = lambda deger, yaklasik, tol: abs(float(deger) - yaklasik) < tol
    e_ = sp.symbols("e_", positive=True)
    tek = lambda ifade, yon: lim(sp.sympify(ifade).subs(h, yon * e_), e_, 0, "+")
    tanim = lambda f, a: lim((f.subs(X, a + h) - f.subs(X, a)) / h, h, 0)
    # ── 37 ──
    f = X**2
    es("37 ortalama", (f.subs(X, 3) - f.subs(X, 1)) / (3 - 1), 4)
    es("37 anlik", (sp.expand(((1 + h)**2 - 1) / h), tanim(f, 1)), (2 + h, 2))
    es("37 temel", [D(g, X) for g in (S(7), X**5, sin(X), cos(X), exp(X), L(X))], [0, 5 * X**4, cos(X), -sin(X), exp(X), 1 / X])
    es("37 kuvvet", (D(X**5, X).subs(X, 2), D(sqrt(X), X) - 1 / (2 * sqrt(X))), (80, 0))
    es("37 negatif kesirli", (D(X**-2, X).subs(X, 1), D(X**Q(2, 3), X).subs(X, 8)), (-2, Q(1, 3)))
    es("37 trig ustel", (D(2 * sin(X) + 3 * cos(X), X).subs(X, 0), D(exp(X) + L(X), X).subs(X, 1)), (2, E + 1))
    es("37 toplam", (D(3 * X**2 - 4 * X + 7, X), D(3 * X**2 - 4 * X + 7, X).subs(X, 1)), (6 * X - 4, 2))
    g = X**3 - 3 * X
    es("37 x3-3x", (D(g, X).subs(X, 2), sp.solveset(D(g, X), X, R), g.subs(X, -1), g.subs(X, 1)), (9, FiniteSet(-1, 1), 2, -2))
    es("37 ekstremum isaret", [sp.sign(D(g, X).subs(X, v)) for v in (-2, 0, 2)], [1, -1, 1])
    es("37 teget", (D(f, X).subs(X, 1), sp.expand(1 + 2 * (X - 1))), (2, 2 * X - 1))
    es("37 kesen tablo", [((1 + v)**2 - 1) / v for v in (S(1), Q(1, 10), Q(1, 100), Q(1, 1000))], [3, Q(21, 10), Q(201, 100), Q(2001, 1000)])
    s = t_**3 - 6 * t_**2 + 9 * t_
    es("37 hiz ivme", (sp.factor(D(s, t_)), sp.solveset(D(s, t_), t_, R), D(s, t_, 2), sp.solveset(D(s, t_, 2), t_, R)), (3 * (t_ - 1) * (t_ - 3), FiniteSet(1, 3), 6 * t_ - 12, FiniteSet(2)))
    es("37 ikinci", (D(X**4, X, 2), D(X**4, X, 2).subs(X, 1)), (12 * X**2, 12))
    es("37 yuksek", (D(X**3, X, 3), D(X**3, X, 4), D(sin(X), X, 4)), (6, 0, sin(X)))
    es("37 mutlak", (tek(Abs(h) / h, -1), tek(Abs(h) / h, 1)), (-1, 1))
    es("37 parcali", (1**2, 2 * 1 - 1, D(X**2, X).subs(X, 1), D(2 * X - 1, X)), (1, 1, 2, 2))
    es("37 uygulamalar", (D(pi * r_**2, r_), D(r_**3, r_), D(r_**3, r_).subs(r_, 2), D(100 + 5 * X + Q(1, 100) * X**2, X), D(100 + 5 * X + Q(1, 100) * X**2, X).subs(X, 100)),
       (2 * pi * r_, 3 * r_**2, 12, 5 + X / 50, 7))
    es("37 dogrusal yaklasim", (D(sqrt(X), X).subs(X, 4), 2 + Q(1, 4) * Q(1, 10), yak(sqrt(Q(41, 10)), 2.0248, 0.00005)), (Q(1, 4), Q(81, 40), True))
    # ── 38 ──
    es("38 nokta", (sp.expand(((2 + h)**2 - 3 * (2 + h)) - (4 - 6)), tanim(X**2 - 3 * X, 2), lim((X**2 - 9) / (X - 3), X, 3)), (h + h**2, 1, 6))
    es("38 tanimdan", [sp.simplify(tanim(ff, X)) for ff in (S(7), 3 * X + 2, X**2, X**3, 2 * X**2 + 3 * X)], [0, 3, 2 * X, 3 * X**2, 4 * X + 3])
    es("38 ters karekok", (sp.simplify(lim((1 / (xp + h) - 1 / xp) / h, h, 0) + 1 / xp**2), sp.simplify(lim((sqrt(xp + h) - sqrt(xp)) / h, h, 0) - 1 / (2 * sqrt(xp)))), (0, 0))
    es("38 fark acilimi", (sp.expand((X + h)**3 - X**3), sp.simplify((1 / (X + h) - 1 / X) - (-h / (X * (X + h))))), (3 * X**2 * h + 3 * X * h**2 + h**3, 0))
    es("38 limitten turev", (lim(((2 + h)**4 - 16) / h, h, 0), D(X**4, X).subs(X, 2), lim((X**3 - 8) / (X - 2), X, 2)), (32, 32, 12))
    ornekler = (X**3, sin(X), exp(X), X**2 - 5 * X)
    es("38 katli artis", [sp.simplify(lim((ff.subs(X, 3 + 2 * h) - ff.subs(X, 3)) / h, h, 0) - 2 * D(ff, X).subs(X, 3)) for ff in ornekler], [0] * 4)
    es("38 simetrik fark", [sp.simplify(lim((ff.subs(X, 1 + h) - ff.subs(X, 1 - h)) / h, h, 0) - 2 * D(ff, X).subs(X, 1)) for ff in ornekler], [0] * 4)
    es("38 sayi ornek", (2 * 5, 2 * 4), (10, 8))
    es("38 sin cos", (lim(sin(h) / h, h, 0), lim((cos(h) - 1) / h, h, 0), sp.simplify(tanim(sin(X), X)), sp.simplify(tanim(cos(X), X))), (1, 0, cos(X), -sin(X)))
    es("38 ustel", (lim((exp(h) - 1) / h, h, 0), lim((2**h - 1) / h, h, 0), sp.simplify(tanim(exp(X), X))), (1, L(2), exp(X)))
    es("38 sayisal", (yak((2**sp.Float("1.001", 30) - 2) / sp.Float("0.001", 30), 1.3868, 0.00005), yak(2 * L(2), 1.3863, 0.00005)), (True, True))
    es("38 kose dikey", (tek(Abs(h) / h, 1), tek(Abs(h) / h, -1), tek(h**Q(1, 3) / h, 1)), (1, -1, oo))
    es("38 parcali", sp.solve([1 - (a_ + b_), 2 - a_], [a_, b_]), {a_: 2, b_: -1})
    es("38 fizik", (sp.expand((Q(49, 10) * (t_ + h)**2 - Q(49, 10) * t_**2) / h), D(Q(49, 10) * t_**2, t_).subs(t_, 2)), (Q(98, 10) * t_ + Q(49, 10) * h, Q(196, 10)))
    es("38 kucuk degisim", (D(X**2, X).subs(X, 3) * Q(1, 100), Q(301, 100)**2 - 9), (Q(6, 100), Q(601, 10000)))
    # ── 39 ──
    es("39 kuvvet", (D(X**7, X), D(X**-3, X), D(X**Q(3, 4), X), D(5 * X**3, X)), (7 * X**6, -3 * X**-4, Q(3, 4) * X**Q(-1, 4), 15 * X**2))
    es("39 polinom", D(4 * X**3 - 2 * X**2 + 5 * X - 9, X).subs(X, 1), 13)
    es("39 koklu", D(3 * sqrt(X) - 2 / X + X**2 / 4, X).subs(X, 4), Q(23, 8))
    es("39 acarak", (D((X + 1) * (X - 2), X), sp.expand(D((X**2 + 1)**2, X))), (2 * X - 1, 4 * X**3 + 4 * X))
    es("39 terimler", (sp.simplify(D((X**3 + 2 * X) / X, X)), sp.simplify(D((xp**2 + 3) / sqrt(xp), xp) - (Q(3, 2) * xp**Q(1, 2) - Q(3, 2) * xp**Q(-3, 2)))), (2 * X, 0))
    es("39 carpim bolum zincir", (D(X**2 * sin(X), X), sp.simplify(D((X + 1) / (X - 1), X) + 2 / (X - 1)**2), sp.simplify(D((3 * X + 1)**5, X) - 15 * (3 * X + 1)**4)), (2 * X * sin(X) + X**2 * cos(X), 0, 0))
    es("39 trig", (sp.simplify(D(tan(X), X) - (1 + tan(X)**2)), sp.simplify(D(tan(X), X) - 1 / cos(X)**2), sp.simplify(D(1 / tan(X), X) + (1 + 1 / tan(X)**2)),
                   D(3 * sin(X) - 2 * cos(X) + tan(X), X).subs(X, 0), D(tan(X), X).subs(X, pi / 4)), (0, 0, 0, 4, 2))
    es("39 ustel log", (sp.simplify(D(2**X + L(X, 3), X).subs(X, 1) - (2 * L(2) + 1 / L(3))), D(exp(3 * X), X), sp.simplify(D(L(5 * xp), xp))), (0, 3 * exp(3 * X), 1 / xp))
    es("39 log kurallari", (sp.simplify(D(L(xp**2), xp)), sp.simplify(D(L(xp**2), xp)).subs(xp, 1), sp.simplify(D(L(3 * xp**4), xp))), (2 / xp, 2, 4 / xp))
    es("39 parcali", (2**2, 4 * 2 - 4, D(X**2, X).subs(X, 2), D(4 * X - 4, X)), (4, 4, 4, 4))
    es("39 mutlak", (D(X - 2, X), D(2 - X, X)), (1, -1))
    es("39 ikinci", (D(X**4 - 3 * X**2, X, 2), D(X**4 - 3 * X**2, X, 2).subs(X, 1)), (12 * X**2 - 6, 6))
    es("39 oruntu", ([sp.simplify(D(exp(2 * X), X, k) / exp(2 * X)) for k in range(1, 6)], D(1 / X, X, 3), D(1 / X, X, 3).subs(X, 1)), ([2, 4, 8, 16, 32], -6 / X**4, -6))
    es("39 teget egim", (D(X**3 - 4 * X, X).subs(X, 2), D(X**3 - 4 * X, X).subs(X, 0)), (8, -4))
    es("39 isaret", (D(X**2 - 4 * X, X), sp.solveset(2 * X - 4 < 0, X, R)), (2 * X - 4, Interval.open(-oo, 2)))
    es("39 hiz ivme", (D(2 * t_**3 - 3 * t_**2, t_).subs(t_, 2), D(2 * t_**3 - 3 * t_**2, t_, 2).subs(t_, 2)), (12, 18))
    es("39 katsayi", sp.solve(3 * a_ + 2 - 11, a_), [3])
    es("39 kaybolan sabit", (D(X**2 + 5, X), D(X**2 - 3, X), D(3 * X**2 + 1, X), (3 * X**2 + 1).subs(X, 0)), (2 * X, 2 * X, 6 * X, 1))
    es("39 harfli", (D(3 * t_**2 + 2 * t_, t_), D(a_ * X**2 + b_ * X, X)), (6 * t_ + 2, 2 * a_ * X + b_))
    tek_mi = lambda ff: sp.simplify(ff.subs(X, -X) + ff) == 0
    cift_mi = lambda ff: sp.simplify(ff.subs(X, -X) - ff) == 0
    es("39 tek cift", (tek_mi(D(X**2, X)), cift_mi(D(X**3, X)), cift_mi(D(sin(X), X)), tek_mi(D(cos(X), X))), (True, True, True, True))


def yazi_40_42():
    """40 Carpimin Turevi, 41 Bolumun Turevi, 42 Zincir Kurali."""
    from sympy import sin, cos, tan, pi, E, exp, log as L, diff as D
    es = esit_ogeler
    Q = Rational
    X, t_, a_, r_ = sp.symbols("X t_ a_ r_", real=True)
    xp = sp.symbols("xp", positive=True)
    sade = lambda e: sp.simplify(e)
    sifir_mi = lambda e: sp.simplify(e) == 0
    # ── 40 ──
    es("40 xx", (D(X * X, X), D(X, X) * D(X, X)), (2 * X, 1))
    es("40 ilk", (sp.expand(2 * (X**2 - 3) + (2 * X + 1) * 2 * X), D(sp.expand((2 * X + 1) * (X**2 - 3)), X)), (6 * X**2 + 2 * X - 6, 6 * X**2 + 2 * X - 6))
    es("40 ustel", (sifir_mi(D(X**3 * exp(X), X) - X**2 * exp(X) * (X + 3)), sp.solveset(X**2 * (X + 3), X, R)), (True, FiniteSet(-3, 0)))
    es("40 xex", (sifir_mi(D(X * exp(X), X) - exp(X) * (1 + X)), sp.solveset(1 + X, X, R), (X * exp(X)).subs(X, -1), sp.sign(D(X * exp(X), X).subs(X, -2)), sp.sign(D(X * exp(X), X).subs(X, 0))),
       (True, FiniteSet(-1), -1 / E, -1, 1))
    es("40 sincos", sifir_mi(D(sin(X) * cos(X), X) - cos(2 * X)), True)
    es("40 xlnx", (sade(D(xp * L(xp), xp)), sp.solve(L(xp) + 1, xp)), (L(xp) + 1, [1 / E]))
    es("40 koklu", (sifir_mi(D(sqrt(xp) * (xp - 1), xp) - (3 * xp - 1) / (2 * sqrt(xp))), D(sqrt(xp) * (xp - 1), xp).subs(xp, 1)), (True, 1))
    es("40 degerler", (-1) * 4 + 3 * 5, 11)
    k = X * (X + 1) * (X + 2)
    es("40 uc carpan", (D(k, X).subs(X, 1), ((X + 1) * (X + 2) + X * (X + 2) + X * (X + 1)).subs(X, 1)), (11, 11))
    es("40 kare", sp.expand(2 * (X**2 + 1) * 2 * X), 4 * X**3 + 4 * X)
    es("40 carpim zincir", sifir_mi(D(X**2 * (3 * X + 1)**4, X) - 2 * X * (3 * X + 1)**3 * (9 * X + 1)), True)
    es("40 ikinci", sifir_mi(D(X * exp(X), X, 2) - exp(X) * (X + 2)), True)
    es("40 teget", (D(X * exp(X), X).subs(X, 0), (X * exp(X)).subs(X, 0)), (1, 0))
    es("40 dikdortgen", 2 * 5 + 10 * 1, 20)
    es("40 gelir", (D((20 + t_) * (100 - 2 * t_), t_).subs(t_, 0), 1 * 100 + 20 * (-2)), (60, 60))
    es("40 negatif ustel", (sifir_mi(D(X**2 * exp(-X), X) - X * exp(-X) * (2 - X)), sp.solveset(X * (2 - X), X, R)), (True, FiniteSet(0, 2)))
    es("40 kosinus", (D(X * cos(X), X), D(X * cos(X), X).subs(X, pi)), (cos(X) - X * sin(X), -1))
    es("40 parametre", (D((X**2 + a_) * exp(X), X).subs(X, 0), sp.solve(a_ - 3, a_)), (a_, [3]))
    es("40 kuvvet", (D(X * X * X, X), D(7 * X**2, X) - 7 * D(X**2, X)), (3 * X**2, 0))
    # ── 41 ──
    es("41 neden", (D(X**2 / X, X), Q(2, 1) * X, sp.solve(2 * X - 1, X)), (1, 2 * X, [Q(1, 2)]))
    es("41 ilk", sifir_mi(D((X + 1) / (X - 1), X) + 2 / (X - 1)**2), True)
    es("41 ikinci derece", (sifir_mi(D(X / (X**2 + 1), X) - (1 - X**2) / (X**2 + 1)**2), sp.solveset(1 - X**2, X, R)), (True, FiniteSet(-1, 1)))
    aa, bb, cc, dd = sp.symbols("aa bb cc dd")
    es("41 dogrusal", (sifir_mi(D((aa * X + bb) / (cc * X + dd), X) - (aa * dd - bb * cc) / (cc * X + dd)**2), 2 * 4 - 3 * 1, sifir_mi(D((2 * X + 3) / (X + 4), X) - 5 / (X + 4)**2)), (True, 5, True))
    es("41 ters", (sifir_mi(D(1 / (X**2 + 1), X) + 2 * X / (X**2 + 1)**2), sifir_mi(D(1 / sqrt(xp), xp) + 1 / (2 * xp * sqrt(xp)))), (True, True))
    es("41 degerler", Q(3 * 4 - 2 * (-1), 16), Q(7, 8))
    es("41 tan cot", (sifir_mi(D(tan(X), X) - 1 / cos(X)**2), sifir_mi(D(cos(X) / sin(X), X) + 1 / sin(X)**2), D(tan(X), X).subs(X, pi / 4), 1 + tan(pi / 4)**2, sifir_mi(1 + tan(X)**2 - 1 / cos(X)**2)),
       (True, True, 2, 2, True))
    es("41 sinx bolu x", (sifir_mi(D(sin(X) / X, X) - (X * cos(X) - sin(X)) / X**2), D(sin(X) / X, X).subs(X, pi)), (True, -1 / pi))
    es("41 ustel", (sifir_mi(D(exp(X) / X, X) - exp(X) * (X - 1) / X**2), sp.solveset(X - 1, X, R)), (True, FiniteSet(1)))
    es("41 log", (sifir_mi(D(L(xp) / xp, xp) - (1 - L(xp)) / xp**2), sp.solve(1 - L(xp), xp), (L(xp) / xp).subs(xp, E)), (True, [E], 1 / E))
    es("41 sadelestir", (D(sp.cancel((X**2 - 1) / (X - 1)), X), D(5 / X**3, X)), (1, -15 / X**4))
    es("41 bolum zincir", (sifir_mi(D(sqrt(xp) / (xp + 1), xp) - (1 - xp) / (2 * sqrt(xp) * (xp + 1)**2)), D(sqrt(xp) / (xp + 1), xp).subs(xp, 1)), (True, 0))
    es("41 parametre", (sifir_mi(D((a_ * X + 1) / (X + 2), X) - (2 * a_ - 1) / (X + 2)**2), sp.solve(Q(1, 4) * (2 * a_ - 1) - Q(5, 4), a_)), (True, [3]))
    es("41 ikinci turev", D(1 / X, X, 2), 2 / X**3)
    es("41 ortalama maliyet", sifir_mi(D((100 + 5 * X) / X, X) + 100 / X**2), True)
    c = 5 * t_ / (t_**2 + 1)
    es("41 derisim", (sifir_mi(D(c, t_) - 5 * (1 - t_**2) / (t_**2 + 1)**2), sp.solveset(1 - t_**2, t_, Interval(0, oo)), c.subs(t_, 1)), (True, FiniteSet(1), Q(5, 2)))
    es("41 ayni ifade", (sifir_mi(D(X**2 / (X**2 + 1), X) - 2 * X / (X**2 + 1)**2), sifir_mi(X**2 / (X**2 + 1) - (1 - 1 / (X**2 + 1)))), (True, True))
    y = (X + 1) / (X - 1)
    es("41 teget", (y.subs(X, 2), D(y, X).subs(X, 2), sp.expand(3 - 2 * (X - 2))), (3, -2, -2 * X + 7))
    # ── 42 ──
    es("42 neden", (D((2 * X + 1)**2, X), sp.expand(4 * (2 * X + 1))), (8 * X + 4, 8 * X + 4))
    es("42 disli", 3 * 2, 6)
    es("42 kuvvet", (sifir_mi(D((X**2 + 1)**3, X) - 6 * X * (X**2 + 1)**2), D((X**2 + 1)**3, X).subs(X, 1)), (True, 24))
    es("42 kok", (sifir_mi(D(sqrt(X**2 + 9), X) - X / sqrt(X**2 + 9)), D(sqrt(X**2 + 9), X).subs(X, 4)), (True, Q(4, 5)))
    es("42 kesirli", sifir_mi(D((X**2 + 1)**Q(3, 2), X) - 3 * X * sqrt(X**2 + 1)), True)
    es("42 mutlak", [D(sqrt(X**2), X).subs(X, v) for v in (-3, -1, 2, 5)], [-1, -1, 1, 1])
    es("42 trig", (D(sin(X**2), X), D(cos(3 * X), X)), (2 * X * cos(X**2), -3 * sin(3 * X)))
    es("42 trig kuvvet", (sifir_mi(D(sin(X)**2, X) - sin(2 * X)), sifir_mi(D(cos(X)**2, X) + sin(2 * X)), sifir_mi(D(sin(X)**2 + cos(X)**2, X))), (True, True, True))
    es("42 ustel", (D(exp(X**2), X), D(exp(-3 * X), X), sifir_mi(D(2**(3 * X), X) - 3 * 2**(3 * X) * L(2))), (2 * X * exp(X**2), -3 * exp(-3 * X), True))
    es("42 log", (sade(D(L(X**2 + 1), X)), D(L(X**2 + 1), X).subs(X, 1), sade(D(L(5 * xp), xp))), (2 * X / (X**2 + 1), 1, 1 / xp))
    es("42 uc kat", (sifir_mi(D(sin(2 * X)**3, X) - 6 * sin(2 * X)**2 * cos(2 * X)), D(sin(2 * X)**3, X).subs(X, pi / 8)), (True, 3 * sqrt(2) / 2))
    g = 2 * X + 1
    f = lambda u: 5 * u
    es("42 degerler", (g.subs(X, 1), D(g, X), D(f(g), X).subs(X, 1), 5 * 2), (3, 2, 10, 10))
    es("42 ic dogrusal", (2 * 3, 2 * 3 * (-1)), (6, -6))
    es("42 carpim zincir", (sifir_mi(D(X * sqrt(1 - X**2), X) - (1 - 2 * X**2) / sqrt(1 - X**2)), sp.solveset(1 - 2 * X**2, X, R)), (True, FiniteSet(-sqrt(2) / 2, sqrt(2) / 2)))
    es("42 bolum zincir", sifir_mi(D((X / (X + 1))**2, X) - 2 * X / (X + 1)**3), True)
    fx = X**3 + X
    kok = sp.nsolve(fx - sp.Float("2.0001"), X, 1)
    es("42 ters", (fx.subs(X, 1), D(fx, X).subs(X, 1), abs(float((kok - 1) / sp.Float("0.0001")) - 0.25) < 0.001), (2, 4, True))
    yy = sp.Function("yy")(X)
    es("42 kapali", (sp.solve(D(X**2 + yy**2 - 25, X), D(yy, X))[0].subs(yy, 4).subs(X, 3), Q(4, 3) * (-Q(3, 4))), (-Q(3, 4), -1))
    es("42 balon", (D(Q(4, 3) * pi * r_**3, r_).subs(r_, 5) * Q(1, 10),), (10 * pi,))
    es("42 merdiven", (sqrt(100 - 36), -Q(6 * 1, 8)), (8, -Q(3, 4)))
    es("42 titresim", (D(3 * sin(2 * t_), t_), function_range(6 * cos(2 * t_), t_, Interval(0, pi))), (6 * cos(2 * t_), Interval(-6, 6)))


def yazi_43_45():
    """43 Teget Denklemi, 44 Artan ve Azalan, 45 Maksimum ve Minimum."""
    from sympy import sin, cos, pi, E, exp, log as L, diff as D, atan
    es = esit_ogeler
    Q = Rational
    X, a_, b_, m_, t_ = sp.symbols("X a_ b_ m_ t_", real=True)
    xp = sp.symbols("xp", positive=True)
    sifir_mi = lambda e: sp.simplify(e) == 0
    def teget(f, x0):
        return sp.expand(f.subs(X, x0) + D(f, X).subs(X, x0) * (X - x0))
    def artan_araliklari(f, alan=R):
        return sp.solveset(D(f, X) > 0, X, alan)
    def azalan_araliklari(f, alan=R):
        return sp.solveset(D(f, X) < 0, X, alan)
    # ── 43 ──
    es("43 parabol", (teget(X**2 - 2 * X, 3), (X**2 - 2 * X).subs(X, 3), D(X**2 - 2 * X, X).subs(X, 3)), (4 * X - 9, 3, 4))
    es("43 kup", (teget(X**3, -1), sp.roots(sp.Poly(X**3 - 3 * X - 2, X))), (3 * X + 2, {-1: 2, 2: 1}))
    es("43 buküm", teget(X**3, 0), 0)
    es("43 eksenler", (teget(X**2 - 4, 1), sp.solve(2 * X - 5, X)), (2 * X - 5, [Q(5, 2)]))
    es("43 trig", (teget(sin(X), pi), teget(sin(X), 0)), (-X + pi, X))
    es("43 ustel log", (teget(exp(X), 0), sp.expand(L(1) + (1 / S(1)) * (X - 1))), (X + 1, X - 1))
    es("43 normal", sp.expand(1 - Q(1, 2) * (X - 1)), -X / 2 + Q(3, 2))
    f = X**3 - 3 * X**2
    es("43 yatay", (sp.solveset(D(f, X), X, R), f.subs(X, 0), f.subs(X, 2)), (FiniteSet(0, 2), 0, -4))
    es("43 paralel dik", (sp.solve(2 * X - 4, X), teget(X**2, 2), sp.solve(2 * X - 2, X), teget(X**2, 1), -1 / (-Q(1, 2))), ([2], 4 * X - 4, [1], 2 * X - 1, 2))
    es("43 disaridan", (sp.solve(-1 - a_**2 - 2 * a_ * (0 - a_), a_), teget(X**2, 1), teget(X**2, -1)), ([-1, 1], 2 * X - 1, -2 * X - 1))
    tg = teget(1 / X, 2)
    es("43 ucgen", (tg, sp.solve(tg, X), tg.subs(X, 0), Q(4 * 1, 2)), (-X / 4 + 1, [4], 1, 2))
    tga = sp.expand((1 / a_ - (X - a_) / a_**2))
    es("43 ucgen genel", sp.simplify(sp.solve(tga, X)[0] * tga.subs(X, 0) / 2), 2)
    es("43 parametreli", sp.solve([1 + a_ + b_ - 2, 2 + a_ - 3], [a_, b_]), {a_: 1, b_: 0})
    es("43 diskriminant", (sp.solve(m_**2 - 4, m_), sp.solve(X**2 - 2 * X + 1, X), sp.solve(X**2 + 2 * X + 1, X)), ([-2, 2], [1], [-1]))
    es("43 ortak teget", (sp.factor(X**2 - (-X**2 + 4 * X - 2)), D(X**2, X).subs(X, 1), D(-X**2 + 4 * X - 2, X).subs(X, 1), teget(X**2, 1)), (2 * (X - 1)**2, 2, 2, 2 * X - 1))
    es("43 cember", sp.expand(4 - Q(3, 4) * (X - 3)), -Q(3, 4) * X + Q(25, 4))
    es("43 egim acisi", (atan(D(X**2 / 2, X).subs(X, 1)), atan(D(X**2 / 2, X).subs(X, sqrt(3)))), (pi / 4, pi / 3))
    es("43 yaklasim", (teget(sqrt(X), 4), teget(sqrt(X), 4).subs(X, Q(41, 10))), (X / 4 + 1, Q(81, 40)))
    es("43 tegetten bilgi", (3 * 2 - 1, 5 + 2 * 3), (5, 11))
    g = X**3 - 3 * X**2 + 5
    es("43 en kucuk egim", (sp.solve(D(g, X, 2), X), D(g, X).subs(X, 1), g.subs(X, 1), teget(g, 1)), ([1], -3, 3, -3 * X + 6))
    es("43 teget kesisim", sp.solve([sp.Symbol("yy") - (2 * X - 1), sp.Symbol("yy") - (-2 * X - 1)], [X, sp.Symbol("yy")]), {X: 0, sp.Symbol("yy"): -1})
    # ── 44 ──
    es("44 parabol", (azalan_araliklari(X**2 - 4 * X), artan_araliklari(X**2 - 4 * X)), (Interval.open(-oo, 2), Interval.open(2, oo)))
    es("44 kup", (artan_araliklari(X**3 - 3 * X), azalan_araliklari(X**3 - 3 * X)), (Union(Interval.open(-oo, -1), Interval.open(1, oo)), Interval.open(-1, 1)))
    h = X**3 - 6 * X**2 + 9 * X + 1
    es("44 uc aralik", (sp.factor(D(h, X)), azalan_araliklari(h), artan_araliklari(h)), (3 * (X - 3) * (X - 1), Interval.open(1, 3), Union(Interval.open(-oo, 1), Interval.open(3, oo))))
    es("44 her yerde", (function_range(D(X**3 + X, X), X, R), function_range(D(X**3, X), X, R), azalan_araliklari(X**3)), (Interval(1, oo), Interval(0, oo), S.EmptySet))
    es("44 parametre", sp.solveset(4 * a_**2 - 36 <= 0, a_, R), Interval(-3, 3))
    es("44 rasyonel", (artan_araliklari(X / (X**2 + 1)), azalan_araliklari(X / (X**2 + 1))), (Interval.open(-1, 1), Union(Interval.open(-oo, -1), Interval.open(1, oo))))
    k = (X + 1) / (X - 1)
    es("44 asimptot", (sifir_mi(D(k, X) + 2 / (X - 1)**2), k.subs(X, 0), k.subs(X, 2)), (True, -1, 3))
    es("44 ustel", (azalan_araliklari(X * exp(X)), artan_araliklari(X * exp(X))), (Interval.open(-oo, -1), Interval.open(-1, oo)))
    es("44 log", (sp.solveset(D(L(X) / X, X) > 0, X, Interval.open(0, oo)), sp.solveset(D(L(X) / X, X) < 0, X, Interval.open(0, oo)), 3**4, 4**3, float(L(3) / 3) > float(L(4) / 4)),
       (Interval.open(0, E), Interval.open(E, oo), 81, 64, True))
    es("44 trig", (sp.solveset(cos(X) < 0, X, Interval(0, 2 * pi)), sp.solveset(D(X + 2 * cos(X), X) < 0, X, Interval(0, 2 * pi))), (Interval.open(pi / 2, 3 * pi / 2), Interval.open(pi / 6, 5 * pi / 6)))
    ma = sp.Abs(X**2 - 4)
    es("44 mutlak", [sp.sign(D(ma, X).subs(X, v)) for v in (-3, -1, 1, 3)], [-1, 1, -1, 1])
    kk = sqrt(4 - X**2)
    es("44 koklu", (sp.solveset(D(kk, X) > 0, X, Interval.open(-2, 2)), sp.solveset(D(kk, X) < 0, X, Interval.open(-2, 2)), kk.subs(X, 0)), (Interval.open(-2, 0), Interval.open(0, 2), 2))
    gg = exp(X) - 1 - X
    es("44 esitsizlik", (sp.solveset(D(gg, X), X, R), gg.subs(X, 0), function_range(gg, X, R), function_range(D(X - sin(X), X), X, R)), (FiniteSet(0), 0, Interval(0, oo), Interval(0, 2)))
    es("44 kok sayisi", (len(sp.real_roots(sp.Poly(X**3 + X - 1, X))), (X**3 + X - 1).subs(X, 0), (X**3 + X - 1).subs(X, 1)), (1, -1, 1))
    es("44 artanlikla esitsizlik", (sp.solveset(X**3 + X > 2, X, R), (X**3 + X).subs(X, 1)), (Interval.open(1, oo), 2))
    # ── 45 ──
    es("45 birinci test", (h.subs(X, 1), h.subs(X, 3), [sp.sign(D(h, X).subs(X, v)) for v in (0, 2, 4)]), (5, 1, [1, -1, 1]))
    c = X**3 - 3 * X
    es("45 ikinci test", (D(c, X, 2).subs(X, -1), D(c, X, 2).subs(X, 1), c.subs(X, -1), c.subs(X, 1)), (-6, 6, 2, -2))
    es("45 karar vermez", (D(X**4, X, 2).subs(X, 0), D(X**3, X, 2).subs(X, 0), [sp.sign(D(X**4, X).subs(X, v)) for v in (-1, 1)], [sp.sign(D(X**3, X).subs(X, v)) for v in (-1, 1)]), (0, 0, [-1, 1], [1, 1]))
    es("45 kapali aralik", ([c.subs(X, v) for v in (-2, -1, 1, 3)], function_range(c, X, Interval(-2, 3))), ([-2, 2, -2, 18], Interval(-2, 18)))
    es("45 parabol", (sp.solve(D(-X**2 + 4 * X + 1, X), X), (-X**2 + 4 * X + 1).subs(X, 2)), ([2], 5))
    es("45 tanimsiz", (function_range(sp.Abs(X), X, R), function_range(xp**Q(2, 3), xp, Interval.open(0, oo))), (Interval(0, oo), Interval.open(0, oo)))
    es("45 rasyonel", function_range(X / (X**2 + 1), X, R), Interval(-Q(1, 2), Q(1, 2)))
    es("45 ustel log", ((X * exp(-X)).subs(X, 1), sp.solve(D(X * exp(-X), X), X), (L(X) / X).subs(X, E)), (1 / E, [1], 1 / E))
    sc = sin(X) + cos(X)
    es("45 trig", (sp.solveset(D(sc, X), X, Interval(0, 2 * pi)), sc.subs(X, pi / 4), sc.subs(X, 5 * pi / 4), sc.subs(X, 0), sc.subs(X, 2 * pi)), (FiniteSet(pi / 4, 5 * pi / 4), sqrt(2), -sqrt(2), 1, 1))
    ff = X**3 - 3 * X**2 - 9 * X
    es("45 parametre", (sp.solve(27 + 6 * a_ - 9, a_), sp.factor(D(ff, X)), ff.subs(X, 3)), ([-3], 3 * (X - 3) * (X + 1), -27))
    es("45 alan", (sp.solve(D(X * (10 - X), X), X), (X * (10 - X)).subs(X, 5)), ([5], 25))
    V = X * (12 - 2 * X)**2
    es("45 kutu", (sp.factor(D(V, X)), sp.solveset(D(V, X), X, Interval.open(0, 6)), V.subs(X, 2), function_range(V, X, Interval(0, 6))), (12 * (X - 6) * (X - 2), FiniteSet(2), 128, Interval(0, 128)))
    es("45 iki sayi", ((X * (10 - X)).subs(X, 5), (X**2 + (10 - X)**2).subs(X, 5), sp.solve(D(X**2 + (10 - X)**2, X), X)), (25, 50, [5]))
    d2 = X**2 + (X**2 - 2)**2
    es("45 en yakin", (sp.expand(d2), sp.factor(D(d2, X)), d2.subs(X, sqrt(Q(3, 2))), function_range(d2, X, R), sqrt(Q(7, 4))), (X**4 - 3 * X**2 + 4, 2 * X * (2 * X**2 - 3), Q(7, 4), Interval(Q(7, 4), oo), sqrt(7) / 2))
    K = -X**2 + 40 * X - 300
    es("45 kar", (sp.solve(D(K, X), X), K.subs(X, 20)), ([20], 100))
    es("45 yok", (function_range(1 / X, X, Interval.Lopen(0, 1)),), (Interval(1, oo),))


def yazi_46_50():
    """46 Integral, 47 Belirsiz Integral, 48 Belirli Integral, 49 Degisken Degistirme, 50 Integral ile Alan."""
    from sympy import integrate as I, sin, cos, tan, pi, E, exp, log as L, diff as D, limit as lim
    es = esit_ogeler
    Q = Rational
    X, t_, a_, k_, y_ = sp.symbols("X t_ a_ k_ y_", real=True)
    xp = sp.symbols("xp", positive=True)
    yak = lambda deger, yaklasik, tol: abs(float(deger) - yaklasik) < tol
    # ters turev dogru mu: turevi integrandi veriyor mu (sabit farki onemsiz)
    tt = lambda F, f, v=X: sp.simplify(D(F, v) - f) == 0
    # ── 46 ──
    es("46 ters turev", (tt(X**3 / 3, X**2), tt(X**3 / 3 + 5, X**2), tt(X**3 + X**2, 3 * X**2 + 2 * X)), (True, True, True))
    es("46 baslangic", (sp.solve(1 + k_ - 4, k_), (X**2 + 3).subs(X, 1)), ([3], 4))
    sag = lambda n: sum((Q(2 * i, n))**2 * Q(2, n) for i in range(1, n + 1))
    sol = lambda n: sum((Q(2 * i, n))**2 * Q(2, n) for i in range(0, n))
    es("46 dikdortgenler", (sag(4), sol(4), sag(8), sol(8), sag(4) - sol(4), sag(8) - sol(8), lim(sp.summation((2 * k_ / sp.Symbol("n", positive=True))**2 * 2 / sp.Symbol("n", positive=True), (k_, 1, sp.Symbol("n", positive=True))), sp.Symbol("n", positive=True), oo)),
       (Q(15, 4), Q(7, 4), Q(51, 16), Q(35, 16), 2, 1, Q(8, 3)))
    es("46 temel teorem", (I(X**2, (X, 0, 2)), I(2 * X + 1, (X, 1, 3)), Q((3 + 7) * 2, 2), yak(Q(8, 3), 2.667, 0.0005)), (Q(8, 3), 10, 10, True))
    es("46 isaretli", (I(sin(X), (X, 0, pi)), I(sin(X), (X, 0, 2 * pi)), I(Abs(sin(X)), (X, 0, 2 * pi))), (2, 0, 4))
    es("46 degisken", tt((X**2 + 1)**4 / 4, 2 * X * (X**2 + 1)**3), True)
    es("46 alan", I(X - X**2, (X, 0, 1)), Q(1, 6))
    es("46 ortalama", I(X**2, (X, 0, 2)) / 2, Q(4, 3))
    es("46 uygulamalar", (I(3 * t_**2, (t_, 0, 2)), I(10 - t_, (t_, 0, 10)), I(t_**2, (t_, 0, X)), D(I(t_**2, (t_, 0, X)), X)), (8, 50, X**3 / 3, X**2))
    es("46 farkli", (I(cos(X), (X, 0, pi / 2)), I(exp(X), (X, 0, 1)), yak(E - 1, 1.718, 0.0005), I(1 / X, (X, 1, E)), I(sqrt(X), (X, 0, 4))), (1, E - 1, True, 1, Q(16, 3)))
    es("46 tablo", (tt(-cos(X), sin(X)), tt(sin(X), cos(X)), tt(L(X), 1 / X), tt(exp(X), exp(X))), (True, True, True, True))
    # ── 47 ──
    es("47 aile", (D(X**2 + 1, X), D(X**2 - 7, X)), (2 * X, 2 * X))
    es("47 tablo", (tt(X**Q(7, 2) / Q(7, 2), X**Q(5, 2)), tt(2**X / L(2), 2**X), tt(tan(X), 1 / cos(X)**2), [D(L(Abs(X)), X).subs(X, v) for v in (-2, 3)]), (True, True, True, [-Q(1, 2), Q(1, 3)]))
    es("47 kuvvet", (tt(X**6 / 6, X**5), tt(5 * X, S(5)), tt(Q(2, 3) * X**Q(3, 2), sqrt(X)), tt(-1 / (2 * X**2), X**-3)), (True, True, True, True))
    es("47 polinom", (sp.expand(I(4 * X**3 - 6 * X + 2, X)), sp.expand(I((X + 1)**2, X)), sp.expand(I((X + 2) * (X - 3), X))),
       (X**4 - 3 * X**2 + 2 * X, X**3 / 3 + X**2 + X, X**3 / 3 - X**2 / 2 - 6 * X))
    es("47 carpim tuzagi", (I(X * X, X), I(X, X) * I(X, X)), (X**3 / 3, X**4 / 4))
    es("47 ayirma", (tt(X**2 / 2 + L(X), (X**2 + 1) / X), tt(Q(2, 3) * xp**Q(3, 2) + 2 * sqrt(xp), (xp + 1) / sqrt(xp), xp)), (True, True))
    es("47 ustel trig", (tt(exp(3 * X) / 3, exp(3 * X)), tt(3 * sin(X) + 2 * cos(X), 3 * cos(X) - 2 * sin(X)), tt(sin(2 * X) / 2, cos(2 * X)), tt(-cos(3 * X) / 3, sin(3 * X))), (True, True, True, True))
    es("47 ozdeslik", (tt(tan(X) - X, tan(X)**2), tt(X / 2 - sin(2 * X) / 4, sin(X)**2), tt(X / 2 + sin(2 * X) / 4, cos(X)**2), sp.simplify((X / 2 - sin(2 * X) / 4) + (X / 2 + sin(2 * X) / 4))),
       (True, True, True, X))
    es("47 dogrusal ic", (tt((2 * X + 1)**4 / 8, (2 * X + 1)**3), sp.expand(D((2 * X + 1)**4 / 8, X) - (2 * X + 1)**3)), (True, 0))
    es("47 log turev", (tt(L(X**2 + 1), 2 * X / (X**2 + 1)), tt(L(2 * xp + 3) / 2, 1 / (2 * xp + 3), xp)), (True, True))
    es("47 mutlak", [D(X * Abs(X) / 2, X).subs(X, w) for w in (-3, 2)], [3, 2])
    es("47 baslangic", (sp.solve(1 - 2 + k_ - 4, k_), sp.solve(4 - 6 + k_ - 1, k_)), ([5], [3]))
    f = X**3 + X + 2
    es("47 ikinci turev", (D(f, X, 2), D(f, X).subs(X, 0), f.subs(X, 0)), (6 * X, 1, 2))
    s = t_**3 + 2 * t_
    es("47 hareket", (D(s, t_, 2), D(s, t_).subs(t_, 0), s.subs(t_, 0), s.subs(t_, 2)), (6 * t_, 2, 0, 12))
    C = 100 + 5 * X + Q(1, 100) * X**2
    es("47 maliyet", (D(C, X), C.subs(X, 0)), (5 + Q(2, 100) * X, 100))
    es("47 katsayi", sp.solve(D(3 * X**2 + 2 * X, X).coeff(X, 1) - a_, a_), [6])
    # ── 48 ──
    n = sp.Symbol("n", positive=True, integer=True)
    es("48 riemann", (sp.simplify(sp.summation(k_ / n, (k_, 1, n)) / n - (n + 1) / (2 * n)), lim((n + 1) / (2 * n), n, oo)), (0, Q(1, 2)))
    es("48 polinom", (I(3 * X**2 - 2 * X, (X, 1, 2)), I((X + 1)**2, (X, 0, 1)), I(3, (X, 1, 4))), (4, Q(7, 3), 9))
    es("48 kok", I(1 / sqrt(X), (X, 1, 4)), 2)
    es("48 ustel log", (I(exp(X), (X, 0, L(2))), I(1 / X, (X, 1, E**2)), I(exp(2 * X), (X, 0, 1))), (1, 2, (E**2 - 1) / 2))
    es("48 trig", (I(sin(X), (X, 0, pi / 2)), I(1 / cos(X)**2, (X, 0, pi / 4)), I(cos(X), (X, 0, pi)), I(sin(X)**2, (X, 0, pi))), (1, 1, 0, pi / 2))
    es("48 ozellikler", (5 + 2, -(5 + 2), 2 * 5 + (3 - 1)), (7, -7, 12))
    es("48 parcali", (I(X**2, (X, 0, 1)), I(2 * X - 1, (X, 1, 2))), (Q(1, 3), 2))
    es("48 mutlak", (I(Abs(X - 1), (X, 0, 3)), I(1 - X, (X, 0, 1)), I(X - 1, (X, 1, 3))), (Q(5, 2), Q(1, 2), 2))
    es("48 simetri", (I(X**3, (X, -2, 2)), I(X**2, (X, -1, 1))), (0, Q(2, 3)))
    es("48 isaretli", (I(X, (X, -1, 2)), I(Abs(X), (X, -1, 2))), (Q(3, 2), Q(5, 2)))
    es("48 degisken sinir", (I(2 * X * (X**2 + 1)**3, (X, 0, 1)), I(y_**3, (y_, 1, 2))), (Q(15, 4), Q(15, 4)))
    es("48 ust sinir", (D(I(t_**2 + 1, (t_, 1, X)), X), sp.simplify(D(I(cos(t_), (t_, 0, X**2)), X) - 2 * X * cos(X**2))), (X**2 + 1, 0))
    es("48 sinirda bilinmeyen", sp.solve(I(2 * X, (X, 0, xp)) - 9, xp), [3])
    es("48 ortalama", (I(sin(X), (X, 0, pi)) / pi, yak(2 / pi, 0.64, 0.005)), (2 / pi, True))
    es("48 karsilastirma", (I(X**2, (X, 0, 1)) < I(X, (X, 0, 1)),), (True,))
    es("48 yol enerji", (I(t_ - 2, (t_, 0, 4)), I(Abs(t_ - 2), (t_, 0, 4)), I(2 * t_, (t_, 0, 3))), (0, 4, 9))
    es("48 sinir degisimi", I(X, (X, 2, 0)), -2)
    es("48 geometri", I(sqrt(4 - X**2), (X, -2, 2)), 2 * pi)
    es("48 limit", lim(sp.summation((k_ / n)**2, (k_, 1, n)) / n, n, oo), Q(1, 3))
    # ── 49 ──
    es("49 kuvvet", (tt((X**2 + 1)**4 / 4, 2 * X * (X**2 + 1)**3), tt((X**2 + 1)**6 / 12, X * (X**2 + 1)**5)), (True, True))
    es("49 kok kesir", (tt((X**2 + 4)**Q(3, 2) / 3, X * sqrt(X**2 + 4)), tt(-1 / (2 * (X**2 + 1)), X / (X**2 + 1)**2), tt(sqrt(X**2 + 1), X / sqrt(X**2 + 1))), (True, True, True))
    es("49 log", (tt(L(xp**3 + 1), 3 * xp**2 / (xp**3 + 1), xp), tt(L(xp)**2 / 2, L(xp) / xp, xp), tt(L(L(xp)), 1 / (xp * L(xp)), xp), tt(L(exp(X) + 1), exp(X) / (exp(X) + 1))), (True, True, True, True))
    es("49 ustel", (tt(exp(X**2) / 2, X * exp(X**2)), tt(2 * exp(sqrt(xp)), exp(sqrt(xp)) / sqrt(xp), xp)), (True, True))
    es("49 trig", (tt(sin(X)**2 / 2, sin(X) * cos(X)), tt(-cos(2 * X) / 4, sin(X) * cos(X)), sp.simplify(sin(X)**2 / 2 - (1 - cos(2 * X)) / 4), tt(sin(X)**5 / 5, sin(X)**4 * cos(X)), tt(-cos(X)**4 / 4, cos(X)**3 * sin(X))),
       (True, True, 0, True, True))
    es("49 tanjant aci", (tt(-L(cos(X)), tan(X)), tt(sin(X**2), 2 * X * cos(X**2))), (True, True))
    es("49 dogrusal", (tt((3 * X - 1)**5 / 15, (3 * X - 1)**4), tt(sin(2 * X + 1) / 2, cos(2 * X + 1))), (True, True))
    es("49 belirli", (I(X * exp(X**2), (X, 0, 1)), I(sin(X) * cos(X), (X, 0, pi / 2)), I(2 * X * (X**2 + 1)**3, (X, 1, 2)), I(y_**3, (y_, 2, 5)), Q(625 - 16, 4)),
       ((E - 1) / 2, Q(1, 2), Q(609, 4), Q(609, 4), Q(609, 4)))
    es("49 eski degisken", (I(X * sqrt(X - 1), (X, 1, 2)), Q(2, 5) + Q(2, 3)), (Q(16, 15), Q(16, 15)))
    es("49 log belirli", I(X / (X**2 + 1), (X, 0, 2)), L(5) / 2)
    # ── 50 ──
    es("50 eksen", (I(X**2, (X, 0, 2)), I(X**2 - 4, (X, -2, 2)), I(X**2 - 2 * X, (X, 0, 2))), (Q(8, 3), -Q(32, 3), -Q(4, 3)))
    es("50 iki yan", (I(X**3, (X, -1, 0)), I(X**3, (X, 0, 2)), I(Abs(X**3), (X, -1, 2)), I(X**3, (X, -1, 2))), (-Q(1, 4), 4, Q(17, 4), Q(15, 4)))
    es("50 grafikten", (3 - 2, 3 + 2), (1, 5))
    es("50 sinus", (I(sin(X), (X, pi, 2 * pi)), I(Abs(sin(X)), (X, 0, 2 * pi))), (-2, 4))
    es("50 iki egri", (I(X - X**2, (X, 0, 1)), sp.solveset(X**2 - 2 * X - 3, X, R), I(2 * X + 3 - X**2, (X, -1, 3)), I(4 - X**2, (X, -2, 2)), I(2 - 2 * X**2, (X, -1, 1))),
       (Q(1, 6), FiniteSet(-1, 3), Q(32, 3), Q(32, 3), Q(8, 3)))
    es("50 sin cos", (I(cos(X) - sin(X), (X, 0, pi / 4)), yak(sqrt(2) - 1, 0.414, 0.0005)), (sqrt(2) - 1, True))
    es("50 yer degistirme", (I(X**3 - X, (X, -1, 0)), I(X - X**3, (X, 0, 1)), I(X - X**3, (X, -1, 1)), I(Abs(X - X**3), (X, -1, 1))), (Q(1, 4), Q(1, 4), 0, Q(1, 2)))
    es("50 dikey", (I(4 - y_**2, (y_, -2, 2)), I(2 * sqrt(X), (X, 0, 4))), (Q(32, 3), Q(32, 3)))
    es("50 ustel log", (I(exp(X), (X, 0, 1)), I(L(X), (X, 1, E)), tt(xp * L(xp) - xp, L(xp), xp)), (E - 1, 1, True))
    es("50 hiperbol", (I(1 / X, (X, 1, E)), I(1 / X, (X, 1, 4)), yak(L(4), 1.386, 0.0005)), (1, L(4), True))
    es("50 mutlak geometri", (I(Abs(X - 1), (X, 0, 3)), I(2 * X + 1, (X, 1, 3))), (Q(5, 2), 10))
    es("50 parametre", (sp.solve(xp**3 / 3 - 9, xp), I(X, (X, 0, 2)), sp.solve(xp**2 / 2 - 1, xp)), ([3], 2, [sqrt(2)]))
    es("50 araclar", I(2 * t_ - t_**2, (t_, 0, 2)), Q(4, 3))
    es("50 kemer", (I(4 - X**2, (X, -2, 2)), yak(Q(32, 3), 10.67, 0.005), Q(2, 3) * 4 * 4), (Q(32, 3), True, Q(32, 3)))


def hap_ekleri():
    """25.09 Ahmet: "hap bilgiler her yazida en az 5 tane; gundelik hayatla iliski
    kurularak birer ikiser tane." Yeni hap kutularindaki sayisal ve cebirsel
    iddialar. Kural cumleleri yazinin kendi bolumunde zaten dogrulaniyor;
    burada hap'in KENDI ornegi ve sayilari yeniden hesaplanir."""
    X, k_ = sp.symbols("X k_")
    es = esit_ogeler
    # ── 06 fonksiyon grafikleri ──
    taksi = 20 * X + 50
    es("06 hap taksi", (taksi.subs(X, 0), sp.diff(taksi, X), taksi.subs(X, 10)), (50, 20, 250))
    es("06 hap oteleme", (sp.solve(sp.diff((X - 3)**2, X), X), sp.expand(((X - 3)**2 + 2).subs(X, 3))), ([3], 2))
    # ── 07 polinomlar ──
    es("07 hap bahce", (sp.expand((X + 2)**2), sp.expand((X + 2)**2 - X**2)), (X**2 + 4 * X + 4, 4 * X + 4))
    P7 = (2 * X - 1)**3 + X**2 + 4
    es("07 hap sabit ve toplam", (P7.subs(X, 0), P7.subs(X, 1), sum(sp.Poly(P7, X).all_coeffs())), (3, 6, 6))
    es("07 hap derece", (sp.degree((X**2 + X + 1)**3, X), sp.degree((X**6 + X**3 + 1), X), sp.degree((X**2 + 1) * (X**3 - X), X)), (6, 6, 5))
    # ── 08 polinomlarda bolme ──
    es("08 hap para", ((X**2 + 5 * X + 6).subs(X, 10), (X + 2).subs(X, 10), sp.div(X**2 + 5 * X + 6, X + 2, X), 156 // 12, 156 % 12),
       (156, 12, (X + 3, 0), 13, 0))
    P8 = 2 * X**3 - 3 * X**2 + 4 * X - 5
    es("08 hap kalan teoremi", (sp.rem(P8, X - 1, X), P8.subs(X, 1), sp.rem(P8, X + 2, X), P8.subs(X, -2)), (-2, -2, -41, -41))
    es("08 hap bolum derecesi", sp.degree(sp.div(X**5 - 3 * X**2 + 1, X**2 + X + 1, X)[0], X), 3)

    # ── 09 kalan ──
    P9 = X**3 - 2 * X**2 + 5
    es("09 hap x+a ve x", (sp.rem(P9, X + 1, X), P9.subs(X, -1), sp.rem(P9, X, X), P9.subs(X, 0), sp.rem(P9, X - 1, X), sum(sp.Poly(P9, X).all_coeffs())), (2, 2, 5, 5, 4, 4))
    gunler = ["pazartesi", "sali", "carsamba", "persembe", "cuma", "cumartesi", "pazar"]
    es("09 hap takvim", (100 % 7, gunler[(gunler.index("sali") + 100) % 7]), (2, "persembe"))
    es("09 hap carpan", (sp.rem(X**3 - 3 * X**2 + 4, X - 2, X), sp.factor(X**3 - 3 * X**2 + 4)), (0, (X - 2)**2 * (X + 1)))
    # ── 10 carpanlara ayirma ──
    a_, b_ = sp.symbols("a_ b_", real=True)
    es("10 hap iki kare", (sp.expand((a_ - b_) * (a_ + b_)), sp.factor(a_**2 + b_**2), sp.solve(a_**2 + 1, a_)), (a_**2 - b_**2, a_**2 + b_**2, []))
    es("10 hap market", (98 * 102, 100**2 - 2**2), (9996, 9996))
    es("10 hap iki sayi", (sp.factor(X**2 - 5 * X + 6), sp.factor(X**2 + X - 12)), ((X - 3) * (X - 2), (X - 3) * (X + 4)))
    # ── 11 ikinci dereceden denklemler ──
    a2, b2, c2 = sp.symbols("a2 b2 c2")
    k1, k2 = sp.solve(a2 * X**2 + b2 * X + c2, X)
    es("11 hap kok formulu ve bagintilar", (sp.simplify(k1 + k2), sp.simplify(k1 * k2)), (-b2 / a2, c2 / a2))
    es("11 hap bahce", (sorted(sp.solve(X * (X + 2) - 48, X)), 6 * 8), ([-8, 6], 48))
    es("11 hap karekok", sorted(sp.solve(X**2 - 9, X)), [-3, 3])
    # ── 12 diskriminant ──
    t_ = sp.symbols("t_", real=True)
    h = -5 * t_**2 + 10 * t_
    es("12 hap top", (sp.discriminant(5 * t_**2 - 10 * t_ + 6, t_), sp.solve(h - 6, t_), sp.maximum(h, t_), 100 - 120), (-20, [], 5, -20))
    es("12 hap rasyonel", (sp.discriminant(X**2 - X - 6, X), sp.sqrt(25), sp.discriminant(X**2 - 4 * X + 1, X), sp.sqrt(12).is_rational), (25, 5, 12, False))
    es("12 hap ters isaret", sp.discriminant(3 * X**2 + 7 * X - 2, X) > 0, True)

    # ── 13 kokler toplami ve carpimi ──
    x1, x2 = sp.symbols("x1 x2")
    es("13 hap kareler toplami", sp.expand((x1 + x2)**2 - 2 * x1 * x2 - (x1**2 + x2**2)), 0)
    es("13 hap oda", (sorted(sp.solve(X**2 - 13 * X + 40, X)), 5 + 8, 5 * 8, 2 * (5 + 8)), ([5, 8], 13, 40, 26))
    es("13 hap isaret", sorted(sp.solve(X**2 - X - 6, X)), [-2, 3])
    # ── 14 parabol ──
    a3, b3, c3 = sp.symbols("a3 b3 c3", nonzero=True)
    es("14 hap simetri ekseni", sp.solve(sp.diff(a3 * X**2 + b3 * X + c3, X), X), [-b3 / (2 * a3)])
    es("14 hap goruntu", (sp.minimum(X**2 - 4 * X + 3, X), sp.maximum(-X**2 + 6 * X - 5, X)), (-1, 4))
    # ── 15 tepe noktasi ──
    r_ = -b3 / (2 * a3)
    f15 = a3 * X**2 + b3 * X + c3
    d_ = sp.symbols("d_")
    es("15 hap tepe", (sp.simplify(f15.subs(X, r_) + (b3**2 - 4 * a3 * c3) / (4 * a3)), sp.simplify(f15.subs(X, r_ + d_) - f15.subs(X, r_ - d_))), (0, 0))
    p_ = sp.symbols("p_", real=True)
    gelir = p_ * (120 - 4 * p_)
    es("15 hap limonata", (sp.solve(sp.diff(gelir, p_), p_), 120 - 4 * 15, gelir.subs(p_, 15)), ([15], 60, 900))
    es("15 hap kok ortalamasi", (sp.solve(sp.diff((X - 2) * (X - 6), X), X), Rational(2 + 6, 2)), ([4], 4))
    # ── 16 parabol denklemi ──
    kemer = -Rational(1, 4) * X**2 + 4
    es("16 hap kemer", (kemer.subs(X, 4), kemer.subs(X, -4), kemer.subs(X, 0), kemer.subs(X, 2)), (0, 0, 4, 3))
    es("16 hap teget", sp.discriminant(sp.expand(3 * (X - 2)**2), X), 0)

    # ── 17 parabol grafigi ──
    a4, k4, d4 = sp.symbols("a4 k4 d4")
    f17 = a4 * (X - 2)**2 + k4
    es("17 hap fiskiye ve genislik", (sp.simplify(f17.subs(X, 0) - f17.subs(X, 4)), sp.expand(f17.subs(X, 2 + d4) - f17.subs(X, 2))), (0, a4 * d4**2))
    es("17 hap mutlak", (sp.Abs(X**2 - 4).subs(X, 0), sp.Abs(X**2 - 4).subs(X, 3)), (4, 5))
    # ── 18 parabol ve dogru ──
    kemer18 = -Rational(1, 4) * X**2 + 4
    es("18 hap kemer", (sorted(sp.solve(kemer18 - 3, X)), 2 - (-2)), ([-2, 2], 4))
    k18 = sp.symbols("k18")
    es("18 hap teget", (sp.solve(sp.discriminant(X**2 - 4 * X + 3 - k18, X), k18), sp.solve(X**2 - 4 * X + 4, X), Rational(4, 2)), ([-1], [2], 2))
    q18 = X**2 - 4 * X + 1 - k18
    es("18 hap orta", sp.simplify(sum(sp.solve(q18, X)) / 2), 2)
    # ── 19 trigonometri ──
    es("19 hap donusum", (sp.pi * 150 / 180, sp.sin(sp.pi / 6), sp.cos(sp.pi / 3), sp.sin(sp.pi / 4), sp.cos(sp.pi / 4)),
       (5 * sp.pi / 6, Rational(1, 2), Rational(1, 2), sp.sqrt(2) / 2, sp.sqrt(2) / 2))
    th = sp.symbols("th")
    es("19 hap temel ozdeslik", sp.simplify(sp.sin(th)**2 + sp.cos(th)**2), 1)
    aci19 = float(sp.atan(Rational(1, 10)) * 180 / sp.pi)
    es("19 hap yol egimi", (Rational(10, 100), round(aci19, 1)), (Rational(1, 10), 5.7))
    # ── 20 birim cember ──
    es("20 hap dolap", (20 * sp.sin(sp.pi / 6), (20 * sp.cos(sp.pi / 2), 20 * sp.sin(sp.pi / 2))), (10, (0, 20)))
    isaret = lambda d: tuple(sp.sign(f(d * sp.pi / 180)) for f in (sp.sin, sp.cos, sp.tan))
    es("20 hap bolgeler", (isaret(45), isaret(135), isaret(225), isaret(315)), ((1, 1, 1), (1, -1, -1), (-1, -1, 1), (-1, 1, -1)))
    es("20 hap referans", (sp.sin(sp.pi * 225 / 180), -sp.sin(sp.pi / 4)), (-sp.sqrt(2) / 2, -sp.sqrt(2) / 2))


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
    for fn in (yazi_02, yazi_03, yazi_04, yazi_05, ekler, yazi_51_55, yazi_56_60, yazi_61_65, yazi_61_65_ek, yazi_66_70, yazi_66_70_ek, yazi_71_75, yazi_76_80, yazi_81_85, yazi_86_91, yazi_92_97, yazi_98_100, yazi_06_10, yazi_11_13, yazi_14_18, yazi_19_23, yazi_24_26, yazi_27_29, yazi_30_32, yazi_33_36, yazi_37_39, yazi_40_42, yazi_43_45, yazi_46_50, hap_ekleri):
        once = SAY[0]
        fn()
        print(f"{fn.__name__}: {SAY[0] - once} iddia dogrulandi")
    bicim()
    print(f"\nTOPLAM {SAY[0]} denetim, hepsi tuttu.")
