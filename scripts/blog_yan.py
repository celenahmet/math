#!/usr/bin/env python3
# scripts/blog_yan.py — blogun sag blogu ve paylas alani (23.09.2026)
#
# Ahmet: "sagdakiler de gelistirilsin; sagda kategoriler vs olsun, en ustte
# uniconnectly reklam alani olsun sag blokta" + "en altta paylas butonu da
# olsun sayfayi paylasabilsin."
#
# Sag blok sirasi: UniConnectly tanitimi → Icindekiler → Kategoriler.
# Tanitim en uste konuyor cunku sayfa acildiginda gorunen tek sag oge o;
# icindekiler zaten kaydirma boyunca yapisik kaliyor.
import html

import blog_veri
import uniconnectly_blok as UC
from blog_ikon import ikon


def _k(s):
    return html.escape(str(s), quote=True)


def uc_karti(kampanya):
    """Dar sutuna sigan dikey tanitim karti. Magaza rozetleri yerine tek
    dugme; 260 px genislikte uc rozet okunmuyor. Reklam alaninda YILDIZSIZ
    logo kullanilir (ev kurali)."""
    adres = UC.ref("/", kampanya)
    return (
        '<aside class="bs-uc">'
        f'<a class="bs-uc-logo" href="{adres}" target="_blank" rel="noopener">'
        f'<img src="{UC.LOGO}" alt="UniConnectly" width="640" height="185" loading="lazy" decoding="async"></a>'
        "<p>Üniversite topluluklarını, etkinlikleri ve şirketleri tek uygulamada "
        "buluşturan ücretsiz kampüs platformu.</p>"
        f'<a class="bs-uc-dugme" href="{adres}" target="_blank" rel="noopener">Ücretsiz keşfet</a>'
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
