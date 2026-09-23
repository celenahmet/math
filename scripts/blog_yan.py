#!/usr/bin/env python3
# scripts/blog_yan.py — blogun sag blogu ve paylas alani (23.09.2026)
#
# Ahmet: "sagdakiler de gelistirilsin; sagda kategoriler vs olsun, en ustte
# uniconnectly reklam alani olsun sag blokta" + "en altta paylas butonu da
# olsun sayfayi paylasabilsin."
#
# Sag blok sirasi (23.09 gece): UniConnectly tanitimi (+ 3 magaza rozeti) →
# Kategoriler → Sinavlar → En populer / En yeni → Neredesin (icindekiler).
# Tanitim en uste konuyor cunku sayfa acildiginda gorunen tek sag oge o;
# icindekiler zaten kaydirma boyunca yapisik kaliyor.
import html

import blog_veri
import uniconnectly_blok as UC
from blog_ikon import ikon


def _k(s):
    return html.escape(str(s), quote=True)


# Rozet altindaki erisilebilir ad: Turkce ek okunusa gore (Store'dan,
# Play'den, AppGallery'den). Adres ve gorsel UC.MAGAZALAR'dan (tek kaynak).
_MAGAZA_EK = {"App Store": "App Store'dan indir", "Google Play": "Google Play'den indir",
              "AppGallery": "AppGallery'den indir"}
_ROZET_EN = {"App Store": 241, "Google Play": 269, "AppGallery": 266}  # PNG, 80 px yukseklik


def uc_karti(kampanya):
    """Dar sutuna sigan dikey tanitim karti. Reklam alaninda YILDIZSIZ logo
    kullanilir (ev kurali).

    Magaza rozetleri (Ahmet 23.09: "altina uc magaza butonu koyalim, CTA
    olarak"): once tek dugme vardi, cunku 260 px'te uc rozet YAN YANA
    okunmuyordu. Simdi ana dugmenin ALTINDA, tek satirda esit yukseklikte;
    Play adresi kampanya etiketini (referrer) tasiyor."""
    adres = UC.ref("/", kampanya)
    rozetler = "".join(
        f'<a href="{_k(u.format(kampanya=kampanya))}" target="_blank" rel="noopener">'
        f'<img src="{g}" alt="{_k(_MAGAZA_EK.get(e, e))}" width="{_ROZET_EN.get(e, 240)}" height="80" '
        'loading="lazy" decoding="async"></a>'
        for e, g, u in UC.MAGAZALAR)
    return (
        '<aside class="bs-uc">'
        f'<a class="bs-uc-logo" href="{adres}" target="_blank" rel="noopener">'
        f'<img src="{UC.LOGO}" alt="UniConnectly" width="640" height="185" loading="lazy" decoding="async"></a>'
        "<p>Üniversite topluluklarını, etkinlikleri ve şirketleri tek uygulamada "
        "buluşturan ücretsiz kampüs platformu.</p>"
        f'<a class="bs-uc-dugme" href="{adres}" target="_blank" rel="noopener">Ücretsiz keşfet</a>'
        f'<div class="bs-uc-magazalar">{rozetler}</div>'
        "</aside>")


def kategori_blogu(etkin=None):
    """Kategori listesi. Baglantilar /blog/#<anahtar> adresine gider;
    js/blog.js hub'da adres parcasini okuyup suzgeci uyguluyor.

    ⚠️ Henuz yazisi OLMAYAN kategori baglanti YAPILMAZ: hub'da o suzgec
    dugmesi bulunmadigi icin baglanti hicbir sey yapmazdi. Soluk metin
    olarak duruyor, boylece yol haritasi gorunur kaliyor."""
    sayilar = {}
    for y in blog_veri.yayinda():
        sayilar[y["kategori"]] = sayilar.get(y["kategori"], 0) + 1
    ogeler = []
    for a, ad, i, r in blog_veri.KATEGORILER:
        n = sayilar.get(a, 0)
        if not n:
            ogeler.append('<li><span class="bs-bos-kat">' + ikon(i)
                          + f"<span>{_k(ad)}</span><em>yakında</em></span></li>")
            continue
        sinif = ' class="etkin"' if a == etkin else ""
        ogeler.append(f'<li><a href="/blog/#{a}"{sinif} style="--kat:{r}">'
                      + ikon(i) + f"<span>{_k(ad)}</span><em>{n}</em></a></li>")
    return ('<nav class="bs-kategori-blok" aria-label="Kategoriler">'
            '<p class="bs-yan-baslik">Kategoriler</p><ul>' + "".join(ogeler) + "</ul></nav>")


def sinav_blogu(etkinler=None):
    """Sinav blogu. Baglantilar /blog/#sinav-<anahtar> adresine gidiyor ve
    hub'da sinav suzgecini gercekten uyguluyor."""
    etkinler = [str(x).lower() for x in (etkinler or [])]
    sayilar = {}
    for y in blog_veri.yayinda():
        for sv in y.get("sinavlar", []):
            k2 = str(sv).lower()
            sayilar[k2] = sayilar.get(k2, 0) + 1
    ogeler = []
    for a, ad, r in blog_veri.SINAVLAR:
        n = sayilar.get(a, 0)
        if not n:
            ogeler.append('<li><span class="bs-bos-kat">' + ikon("sinavda")
                          + f"<span>{_k(ad)}</span><em>yakında</em></span></li>")
            continue
        sinif = ' class="etkin"' if a in etkinler else ""
        ogeler.append(f'<li><a href="/blog/#sinav-{a}"{sinif} style="--kat:{r}">'
                      + ikon("sinavda") + f"<span>{_k(ad)}</span><em>{n}</em></a></li>")
    return ('<nav class="bs-kategori-blok bs-sinav-blok" aria-label="Sınavlar">'
            '<p class="bs-yan-baslik">Sınavlar</p><ul>' + "".join(ogeler) + "</ul></nav>")


def yazi_listesi(etkin=None, adet=5):
    """"En popüler / En yeni" blogu (Ahmet 23.09: "sag blokta en populer
    yazilar olsun, 5 tane gozuksun; en populer ve en yeni diye
    degistirilebilsin").

    · "En yeni" SUNUCUDA uretilir; JS olmadan da calisir. Ayni gunde
      yayinlananlarda dosya numarasi buyuk olan daha yenidir.
    · "En popüler" icin yayindaki BUTUN yazilar gizli olarak basilir;
      js/blog.js /api/populer/ yanitina gore siralayip ilk 5'i acar ve
      sekmeyi gorunur yapar. Depo bagli degilse ya da hic sayim yoksa
      sekme GIZLI kalir: uydurma siralama gosterilmez.
    · Istemcide innerHTML YOK: yalniz var olan ogeler yeniden dizilir."""
    yazilar = list(enumerate(blog_veri.yayinda()))
    yeniler = [y for _, y in sorted(yazilar, key=lambda iy: (iy[1]["tarih"], iy[0]), reverse=True)]

    def oge(y, gizli=False):
        simdiki = ' aria-current="page"' if y["slug"] == etkin else ""
        return (f'<li data-yol="/blog/{_k(y["slug"])}/"{" hidden" if gizli else ""}>'
                f'<a href="/blog/{_k(y["slug"])}/"{simdiki} '
                f'style="--kat:{blog_veri.KAT_RENK.get(y["kategori"], "#1860f0")}">'
                f'<span>{_k(y["baslik"])}</span></a></li>')

    return ('<nav class="bs-yazilar-blok" aria-label="Öne çıkan yazılar">'
            '<div class="bs-yazilar-sekme">'
            '<button type="button" data-sekme="populer" aria-pressed="false" hidden>En popüler</button>'
            '<button type="button" data-sekme="yeni" aria-pressed="true">En yeni</button></div>'
            '<ol class="bs-yazilar" data-panel="yeni">'
            + "".join(oge(y) for y in yeniler[:adet]) + "</ol>"
            f'<ol class="bs-yazilar" data-panel="populer" data-adet="{adet}" hidden>'
            + "".join(oge(y, gizli=True) for y in yeniler) + "</ol></nav>")


def paylas(baslik, yol):
    """Paylas alani. Once tarayicinin KENDI paylasim penceresi denenir
    (navigator.share; mobilde WhatsApp/Instagram dahil her sey cikar).
    Desteklenmiyorsa js/blog.js baglantiyi panoya kopyalar. Ucuncu taraf
    paylasim betigi YUKLENMEZ: her biri izleme cerezi tasiyor."""
    return (
        '<div class="bs-paylas" data-baslik="' + _k(baslik) + '" data-yol="' + _k(yol) + '">'
        "<p>Bu yazıyı paylaş</p>"
        '<div class="bs-paylas-dugmeler">'
        '<button type="button" class="bs-paylas-ana">' + ikon("paylas") + "Paylaş</button>"
        '<button type="button" class="bs-paylas-kopya">' + ikon("baglanti") + "Bağlantıyı kopyala</button>"
        '<a class="bs-paylas-whatsapp" target="_blank" rel="noopener" href="#">' + ikon("whatsapp") + "WhatsApp</a>"
        '<a class="bs-paylas-x" target="_blank" rel="noopener" href="#">' + ikon("x") + "X</a>"
        # ⚠️ Instagram web uzerinden BAGLANTI PAYLASIMINI DESTEKLEMIYOR:
        # X'in intent adresi gibi bir adresi yok. Bu yuzden dugme baglantiyi
        # panoya kopyalayip kullaniciya hikayesine yapistirmasini soyluyor.
        # Mobilde zaten sistem paylasim penceresinde (Paylas dugmesi)
        # Instagram cikiyor.
        '<button type="button" class="bs-paylas-instagram">' + ikon("instagram") + "Instagram</button>"
        "</div></div>")
