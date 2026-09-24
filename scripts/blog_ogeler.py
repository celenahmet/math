#!/usr/bin/env python3
# scripts/blog_ogeler.py — yazi govdesinde kullanilan kutular (23.09.2026)
#
# Ahmet: "konu anlatimini bastan sona ne varsa HAP BILGILERLE birlikte
# verecegiz." Hap bilgi, dikkat ve ornek kutulari yaziyi tarayarak okuyan
# ogrenci icin capa noktasi; her biri css/blog.css'te ayri bir kutu.
#
# Formuller $...$ (satir ici) ve $$...$$ (blok) ile yazilir;
# scripts/matematik.py bunlari MathML'e cevirir (sayfaya JS/CSS inmez).
import html

from blog_ikon import ikon


def _ic(parcalar):
    return "".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in parcalar)


def hap(*parcalar):
    """Ezberlenecek kural, formul ya da kisayol.

    Ic govde ayri bir sarmalayiciya aliniyor: scripts/blog_uygula.py
    sayfanin sonunda butun hap bilgileri toplayip "Hap bilgi ozeti"
    bolumunu URETIYOR (Ahmet 23.09). Bu yuzden hap kutusunun icine
    TABLO KONMAZ; tablo da <div> oldugu icin ozet cikarimini bozar.
    """
    ic = _ic(parcalar)
    assert "<div" not in ic, "hap() icine div (orn. tablo) konmaz; ozet cikarimi bozulur"
    return ('<div class="bs-hap"><b>' + ikon("hap") + "Hap bilgi" + "</b>"
            + '<div class="bs-hap-ic">' + ic + "</div></div>")


def dikkat(*parcalar):
    """Sinavda tuzak olan, sik yapilan hata."""
    return '<div class="bs-dikkat"><b>' + ikon("dikkat") + "Dikkat" + '</b>' + _ic(parcalar) + "</div>"


def ornek(*parcalar):
    """Cozumlu ornek."""
    return '<div class="bs-ornek"><b>' + ikon("ornek") + "Örnek" + '</b>' + _ic(parcalar) + "</div>"


def onkosul(*parcalar):
    """Yaziya baslamadan once bilinmesi gerekenler. Ogrenci konuya hazir mi
    olmadan giriyorsa once oraya donsun diye yazinin BASINA konur."""
    return '<div class="bs-onkosul"><b>' + ikon("onkosul") + "Önce şunları bil" + '</b>' + _ic(parcalar) + "</div>"


def sinavda(*parcalar):
    """Konunun sinavda hangi bicimde sorulduğu. Ahmet: kitle YKS + ALES/KPSS;
    ayni konu uc sinavda farkli derinlikte soruluyor, ogrenci hangisine
    calistigini bilerek okusun."""
    return '<div class="bs-sinavda"><b>' + ikon("sinavda") + "Sınavda nasıl çıkar" + '</b>' + _ic(parcalar) + "</div>"


def tablo(basliklar, satirlar):
    """Dar ekranda yatay kayan tablo. Hucreler KISA tutulur; uzun aciklama
    tablonun altina yazilir (blog yazim kurali)."""
    # quote=False: baslik ogenin ICINDE, tirnak kacisi gerekmez; $p'$ gibi formuller &#x27; olup bozuluyordu (25.09)
    bas = "".join(f"<th>{html.escape(str(b), quote=False)}</th>" for b in basliklar)
    gov = "".join("<tr>" + "".join(f"<td>{h}</td>" for h in s) + "</tr>" for s in satirlar)
    return f'<div class="bs-tablo"><table><thead><tr>{bas}</tr></thead><tbody>{gov}</tbody></table></div>'


# ── grafikler (25.09) ─────────────────────────────────────────────────────
# Tablo ve grafik yorumlama yazisi grafiksiz anlatilamaz. Satir ici SVG:
# sayfaya JS/kutuphane inmez, olcek viewBox ile ekrana uyar. Renkler
# css/blog.css'teki .bs-grafik siniflarindan gelir. Etiket metni kelime
# sayisina girmez (blog_uygula._duz <svg> blogunu siler); okunabilir veri
# aria-label'da da var.
GRAFIK_RENK = ["#1860f0", "#f97316", "#0d9488", "#a21caf", "#eab308", "#64748b"]


def _sayi(v):
    """Grafik etiketi: Turkce ondalik virgul, gereksiz sifir yok."""
    return f"{v:g}".replace(".", ",")


def _cerceve(baslik, gen, yuk, govde, veri_metni):
    etiket = html.escape(f"{baslik}. {veri_metni}", quote=True)
    return (f'<figure class="bs-grafik"><svg viewBox="0 0 {gen} {yuk}" role="img" aria-label="{etiket}">'
            f'{govde}</svg><figcaption>{html.escape(baslik, quote=False)}</figcaption></figure>')


def _eksen(etiketler, degerler, y_bas, y_son, adim, gen, yuk, sol=52, sag=12, ust=26, alt=40):
    """Ortak eksen: yatay izgara + sol sayi etiketleri. (x_merkez, y) doner."""
    n = len(degerler)
    cizim_y = yuk - ust - alt
    yx = lambda v: yuk - alt - (v - y_bas) / (y_son - y_bas) * cizim_y
    parca = []
    v = y_bas
    while v <= y_son + 1e-9:
        y = yx(v)
        parca.append(f'<line class="g-izgara" x1="{sol}" y1="{y:.1f}" x2="{gen - sag}" y2="{y:.1f}"/>'
                     f'<text x="{sol - 8}" y="{y + 5:.1f}" text-anchor="end">{_sayi(v)}</text>')
        v += adim
    dilim = (gen - sol - sag) / n
    merkez = [sol + dilim * (i + .5) for i in range(n)]
    for xm, e in zip(merkez, etiketler):
        parca.append(f'<text x="{xm:.1f}" y="{yuk - alt + 24}" text-anchor="middle">{html.escape(e)}</text>')
    parca.append(f'<line class="g-eksen" x1="{sol}" y1="{yuk - alt}" x2="{gen - sag}" y2="{yuk - alt}"/>')
    return "".join(parca), merkez, dilim, yx


def sutun_grafik(baslik, etiketler, degerler, y_son, adim, y_bas=0):
    """Sutun grafigi. y_bas > 0 ise eksen sifirdan baslamaz (yaniltici olcek ornegi)."""
    gen, yuk = 480, 280
    eksen, merkez, dilim, yx = _eksen(etiketler, degerler, y_bas, y_son, adim, gen, yuk)
    gs = dilim * .56
    sutun = "".join(
        f'<rect class="g-sutun" x="{xm - gs / 2:.1f}" y="{yx(v):.1f}" width="{gs:.1f}" height="{yx(y_bas) - yx(v):.1f}" rx="3"/>'
        f'<text class="g-deger" x="{xm:.1f}" y="{yx(v) - 7:.1f}" text-anchor="middle">{_sayi(v)}</text>'
        for xm, v in zip(merkez, degerler))
    return _cerceve(baslik, gen, yuk, eksen + sutun,
                    ", ".join(f"{e}: {_sayi(v)}" for e, v in zip(etiketler, degerler)))


def cizgi_grafik(baslik, etiketler, degerler, y_son, adim, y_bas=0):
    """Cizgi grafigi: zaman icindeki degisim."""
    gen, yuk = 480, 280
    eksen, merkez, _, yx = _eksen(etiketler, degerler, y_bas, y_son, adim, gen, yuk)
    noktalar = " ".join(f"{xm:.1f},{yx(v):.1f}" for xm, v in zip(merkez, degerler))
    govde = eksen + f'<polyline class="g-cizgi" points="{noktalar}"/>' + "".join(
        f'<circle class="g-nokta" cx="{xm:.1f}" cy="{yx(v):.1f}" r="5"/>'
        f'<text class="g-deger" x="{xm:.1f}" y="{yx(v) - 12:.1f}" text-anchor="middle">{_sayi(v)}</text>'
        for xm, v in zip(merkez, degerler))
    return _cerceve(baslik, gen, yuk, govde,
                    ", ".join(f"{e}: {_sayi(v)}" for e, v in zip(etiketler, degerler)))


def daire_grafik(baslik, dilimler):
    """Daire grafigi. dilimler: [(gosterilecek_etiket, merkez_acisi_derece)];
    acilar toplami 360 olmali."""
    import math
    assert abs(sum(a for _, a in dilimler) - 360) < 1e-9, "daire grafigi: acilar toplami 360 degil"
    gen, yuk = 480, 250
    cx, cy, r = 118, 125, 104
    bas = -90.0
    parca = []
    for i, (_, aci) in enumerate(dilimler):
        son = bas + aci
        x1, y1 = cx + r * math.cos(math.radians(bas)), cy + r * math.sin(math.radians(bas))
        x2, y2 = cx + r * math.cos(math.radians(son)), cy + r * math.sin(math.radians(son))
        buyuk = 1 if aci > 180 else 0
        parca.append(f'<path d="M{cx},{cy} L{x1:.1f},{y1:.1f} A{r},{r} 0 {buyuk} 1 {x2:.1f},{y2:.1f} Z" '
                     f'fill="{GRAFIK_RENK[i % len(GRAFIK_RENK)]}" class="g-dilim"/>')
        bas = son
    ly = yuk / 2 - (len(dilimler) - 1) * 15
    for i, (etiket, _) in enumerate(dilimler):
        y = ly + i * 30
        parca.append(f'<rect x="262" y="{y - 11:.1f}" width="14" height="14" rx="3" fill="{GRAFIK_RENK[i % len(GRAFIK_RENK)]}"/>'
                     f'<text x="284" y="{y + 1:.1f}">{html.escape(etiket)}</text>')
    return _cerceve(baslik, gen, yuk, "".join(parca), ", ".join(e for e, _ in dilimler))
