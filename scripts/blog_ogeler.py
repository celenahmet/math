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
    bas = "".join(f"<th>{html.escape(str(b))}</th>" for b in basliklar)
    gov = "".join("<tr>" + "".join(f"<td>{h}</td>" for h in s) + "</tr>" for s in satirlar)
    return f'<div class="bs-tablo"><table><thead><tr>{bas}</tr></thead><tbody>{gov}</tbody></table></div>'
