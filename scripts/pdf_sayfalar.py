#!/usr/bin/env python3
# scripts/pdf_sayfalar.py — PDF merkezi, indirme ve dogrulama sayfalari (28.09.2026)
#
# Ahmet (28.09):
#   · "PDF'leri indirirken 10 sn bekletecegiz; 10 saniye dolduktan sonra indirme
#     butonu cikacak; o 10 sn'de UniConnectly reklami cikaracagiz. Her yazida."
#   · "PDF merkezi olacak", "webde aramali ve tum PDF'lerin bir arada oldugu"
#   · "QR okutunca guncel diye yesil renkli animasyonlar, eger degilse de
#     guncele yonlendirme olsun; her turlu ikisinde de guncel listelere
#     bakabilirsiniz"
#   · "duyurular tarzi bir sey olur, gecmiste neler, hangi belgeler degisti,
#     uptime gibi sergilenir"
#
# Uretilen sayfalar (veri: pdf/kayit.json, YALNIZ yuklenmis surumler):
#   /pdf/                 merkez: arama, butun belgeler, duyurular, dogrulama
#   /pdf/<slug>/          indirme: 10 sn bekleme + UniConnectly, surum gecmisi  (noindex)
#   /d/                   belge dogrulama: kod ya da dosya                      (noindex)
#   /d/<kod>/             belgenin surumleri ve durumlari                        (noindex)
#   /d/<kod>/<surum>/     QR hedefi: guncel (yesil) / eski / hata duzeltildi     (noindex)
# noindex sayfalar blog_uygula.kabuk(taslak=True) ile basilir: robots noindex +
# "blog:taslak" isareti, boylece sitemap ve site ici aramaya girmez.
#
# Dosyalar medya.ahmetcelen.com.tr'den iner (Vercel trafigi harcanmaz); medya
# zaten X-Robots-Tag: noindex veriyor, PDF'ler Google'da ayrica listelenmez.
# ⚠️ Okura donuk metinler VARSAYILAN; son hali Ahmet'in.
import datetime, html, json, shutil, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import pdf_veri as V                  # noqa: E402
import blog_uygula as B               # noqa: E402
import blog_veri                      # noqa: E402
import uniconnectly_blok as UC        # noqa: E402
from blog_ikon import ikon            # noqa: E402

k = B.k
BEKLEME = 10          # saniye
DUYURU_GUN = 90       # "uptime" seridi

DURUM = {  # (sinif, baslik)
    "guncel": ("guncel", "Güncel"),
    "eski": ("eski", "Daha yeni sürüm var"),
    "hata": ("hata", "Hata düzeltildi"),
}


def boyut(b):
    mb = b / 1048576
    return (f"{mb:.1f}".replace(".", ",") + " MB") if mb >= 1 else f"{round(b / 1024)} KB"


def yayindaki(belge):
    return [s for s in belge["surumler"] if V.yayinda_mi(s)]


def _rozet(tur):
    return f'<span class="pdf-tur pdf-tur-{k(tur)}">{k(V.TURLER[tur])}</span>'


# ── ortak parcalar ───────────────────────────────────────────────────────
def uc_reklam(kampanya):
    """Bekleme ekranindaki UniConnectly tanitimi. Metinler uniconnectly_blok'taki
    DOGRULANMIS ogrenci faydalari; baglantilar ref/UTM'li, yildizsiz logo."""
    adres = UC.ref("/", kampanya)
    faydalar = "".join(
        f"<li><b>{k(b)}</b><span>{k(V_duz(a))}</span></li>"
        for b, a in UC.FAYDALAR["ogrenci"][1][:4])
    rozetler = "".join(
        f'<a href="{k(u.format(kampanya=kampanya))}" target="_blank" rel="noopener">'
        f'<img src="{g}" alt="{k(e)}" height="40" loading="lazy" decoding="async"></a>'
        for e, g, u in UC.MAGAZALAR)
    # Etiket (Ahmet 28.09): "tanitim degil de diger yapimlarimiz; is birligi de
    # degil, kendi urunumuz, ona gore yazalim."
    return (f'<aside class="pdf-uc" aria-label="Diğer yapımlarımızdan: UniConnectly">'
            f'<span class="pdf-uc-etiket">Diğer yapımlarımızdan</span>'
            f'<a class="pdf-uc-logo" href="{k(adres)}" target="_blank" rel="noopener">'
            f'<img src="{UC.LOGO}" alt="UniConnectly" width="640" height="185" decoding="async"></a>'
            '<p class="pdf-uc-giris">Üniversite topluluklarını, etkinlikleri ve şirketleri tek uygulamada buluşturan ücretsiz kampüs platformu.</p>'
            f'<ul class="pdf-uc-faydalar">{faydalar}</ul>'
            f'<div class="pdf-uc-alt"><a class="bs-dugme-ana" href="{k(adres)}" target="_blank" rel="noopener">Ücretsiz keşfet</a>'
            f'<div class="pdf-uc-magaza">{rozetler}</div></div></aside>')


def V_duz(a):
    import re
    a = re.sub(r"<a\b.*?</a>", "", a)
    return re.sub(r"<[^>]+>", "", a).split(";")[0].strip()


def dosya_denetimi():
    """Tarayicida SHA-256; dosya cihazdan cikmaz (js/pdf.js)."""
    return ('<section class="pdf-dosya" data-pdf-dosya>'
            f'<h2 class="bs-h2-ikon">{ikon("kontrol")}Elinizdeki dosyayı doğrulayın</h2>'
            '<p>PDF dosyasını seçin; bizim yayımladığımız bir sürümle <strong>birebir aynı</strong> olup olmadığını ve güncelliğini gösterelim. '
            'Denetim tarayıcınızda yapılır, dosya cihazınızdan dışarı gönderilmez.</p>'
            '<label class="pdf-dosya-sec"><input type="file" accept="application/pdf,.pdf" data-pdf-dosya-girdi>'
            '<span>PDF dosyası seçin ya da buraya bırakın</span></label>'
            '<div class="pdf-dosya-sonuc" role="status" aria-live="polite" hidden></div>'
            '<noscript><p>Dosya denetimi için tarayıcıda JavaScript açık olmalı.</p></noscript>'
            '</section>')


def duyurular(kayit, bugun, en_cok=30):
    """Uptime tarzi serit + gun gun degisiklik listesi. Ayni gun ayni turde cok
    kayit varsa (ilk yayin gibi) tek satirda toplanir, ayrinti acilir."""
    olaylar = {}
    for kd, b in kayit["belgeler"].items():
        for s in yayindaki(b):
            olaylar.setdefault(s["tarih"], []).append((kd, b, s))
    ilk_gun = min(olaylar) if olaylar else bugun.isoformat()
    serit = []
    for i in range(DUYURU_GUN - 1, -1, -1):
        gun = bugun - datetime.timedelta(days=i)
        g = gun.isoformat()
        o = olaylar.get(g, [])
        if g < ilk_gun:
            sinif, aciklama = "once", "Henüz yayın yok"
        elif any(s["tur"] == "hata" for _, _, s in o):
            sinif, aciklama = "hata", f"{sum(s['tur'] == 'hata' for _, _, s in o)} hata düzeltmesi"
        elif o:
            sinif, aciklama = "surum", f"{len(o)} yeni sürüm"
        else:
            sinif, aciklama = "sorunsuz", "Değişiklik yok"
        serit.append(f'<span class="pdf-gun pdf-gun-{sinif}" title="{V.tr_tarih(g)}: {aciklama}"></span>')
    hata_sayisi = sum(s["tur"] == "hata" for g, o in olaylar.items()
                      if g >= (bugun - datetime.timedelta(days=DUYURU_GUN - 1)).isoformat() for _, _, s in o)
    toplam = len(kayit["belgeler"])
    liste = []
    for g in sorted(olaylar, reverse=True)[:en_cok]:
        turler = {}
        for kd, b, s in sorted(olaylar[g], key=lambda x: x[0]):
            turler.setdefault(s["tur"], []).append((kd, b, s))
        for tur, ogeler in turler.items():
            if len(ogeler) > 5:
                ic = "".join(f'<li><a href="{V.dogrulama_yolu(kd)}">{k(kd)}</a> {k(b["baslik"])} · Sürüm {k(s["surum"])}</li>'
                             for kd, b, s in ogeler)
                liste.append(f'<li class="pdf-duyuru"><time datetime="{g}">{V.tr_tarih(g)}</time>{_rozet(tur)}'
                             f'<details><summary>{len(ogeler)} belge · {k(ogeler[0][2]["not"])}</summary><ul>{ic}</ul></details></li>')
            else:
                for kd, b, s in ogeler:
                    liste.append(f'<li class="pdf-duyuru"><time datetime="{g}">{V.tr_tarih(g)}</time>{_rozet(tur)}'
                                 f'<div><a href="{V.dogrulama_yolu(kd)}">{k(kd)} · {k(b["baslik"])}</a> · Sürüm {k(s["surum"])}'
                                 f'<p>{k(s["not"])}</p></div></li>')
    return (f'<section class="pdf-duyurular" id="duyurular">'
            f'<h2 class="bs-h2-ikon">{ikon("saat")}Duyurular ve değişiklikler</h2>'
            f'<div class="pdf-durum-ozet"><span class="pdf-nokta"></span><strong>{toplam} belge yayında</strong>'
            f'<span>Son {DUYURU_GUN} günde {hata_sayisi} hata düzeltmesi</span></div>'
            f'<div class="pdf-serit" role="img" aria-label="Son {DUYURU_GUN} günün değişiklik şeridi">{"".join(serit)}</div>'
            f'<div class="pdf-serit-alt"><span>{DUYURU_GUN} gün önce</span><span class="pdf-lejant">'
            '<i class="pdf-gun-sorunsuz"></i>Değişiklik yok <i class="pdf-gun-surum"></i>Yeni sürüm '
            '<i class="pdf-gun-hata"></i>Hata düzeltmesi</span><span>Bugün</span></div>'
            f'<ol class="pdf-duyuru-liste">{"".join(liste[:en_cok])}</ol>'
            + (f'<p class="pdf-tum-degisiklik"><a href="/d/#duyurular">Bütün değişiklikler</a></p>' if en_cok < 30 else "")
            + '</section>')


def gecmis_tablosu(b):
    satir = "".join(
        f'<tr><td><strong>{k(s["surum"])}</strong></td><td>{V.tr_tarih(s["tarih"])}</td><td>{_rozet(s["tur"])}</td>'
        f'<td>{k(s["not"])}</td><td><a href="{V.dogrulama_yolu(V.kod(b["no"]), s["surum"])}">Durum</a></td></tr>'
        for s in reversed(yayindaki(b)))
    return ('<div class="bs-tablo"><table><thead><tr><th>Sürüm</th><th>Tarih</th><th>Tür</th><th>Değişiklik</th><th></th></tr></thead>'
            f'<tbody>{satir}</tbody></table></div>')


# ── /pdf/ ────────────────────────────────────────────────────────────────
def merkez(kayit, yazilar, bugun):
    satirlar = []
    for anahtar, ad, ik, renk in blog_veri.KATEGORILER:
        belgeler = [(kd, b) for kd, b in kayit["belgeler"].items() if b["kategori"] == anahtar and yayindaki(b)]
        if not belgeler:
            continue
        ogeler = []
        for kd, b in sorted(belgeler, key=lambda x: x[1]["no"]):
            s = yayindaki(b)[-1]
            y = yazilar[b["no"]]
            aranan = " ".join([kd, kd.replace("-", ""), str(b["no"]), b["baslik"], ad] + [str(x) for x in y.get("sinavlar", [])])
            ogeler.append(
                f'<li class="pdf-satir" data-ara="{k(aranan.lower())}">'
                f'<span class="pdf-kod">{k(kd)}</span>'
                f'<div class="pdf-satir-ic"><a class="pdf-satir-baslik" href="{V.indirme_yolu(b["slug"])}">{k(b["baslik"])}</a>'
                f'<span class="pdf-satir-kunye">Sürüm {k(s["surum"])} · {s["sayfa"]} sayfa · {boyut(s["bayt"])}</span></div>'
                f'<div class="pdf-satir-eylem"><a class="bs-dugme-ana" href="{V.indirme_yolu(b["slug"])}">{ikon("indir")}İndir</a>'
                f'<a class="bs-dugme-ikincil" href="{V.dogrulama_yolu(kd)}">Doğrula</a></div></li>')
        satirlar.append(f'<section class="pdf-grup" style="--kat:{renk}"><h2 class="bs-h2-ikon">{ikon(ik)}{k(ad)}</h2>'
                        f'<ol class="pdf-liste">{"".join(ogeler)}</ol></section>')
    toplam = sum(1 for b in kayit["belgeler"].values() if yayindaki(b))
    govde = f'''
<div class="kap bs-hero pdf-hero">
  <h1>PDF Merkezi</h1>
  <p>Bütün konu anlatımlarının ücretsiz PDF'leri. Her belgenin bir kodu ve sürümü var: bir hata düzeltildiğinde yeni sürüm yayımlanır, değişiklik aşağıda duyurulur. Elinizdeki belgenin güncel olup olmadığını QR kodla ya da dosyayla doğrulayabilirsiniz.</p>
</div>
<div class="kap pdf-merkez">
  {duyurular(kayit, bugun, en_cok=5)}
  <div class="pdf-ara">
    <label for="pdf-ara-girdi" class="sr-only">PDF ara</label>
    <input id="pdf-ara-girdi" type="search" placeholder="Konu, belge kodu ya da sınav ara (EBOB, AC-066, KPSS)" autocomplete="off" data-pdf-ara>
    <span class="pdf-ara-sayi" data-pdf-sayi aria-live="polite">{toplam} belge</span>
  </div>
  <p class="pdf-bos" data-pdf-bos hidden>Bu aramayla eşleşen belge yok.</p>
  {"".join(satirlar)}
  <section class="pdf-kodla">
    <h2 class="bs-h2-ikon">{ikon("kontrol")}Belge doğrulama</h2>
    <p>Her PDF'in ilk sayfasında bir QR kod ve belge kodu (örneğin AC-066) bulunur. QR kodu okutun ya da <a href="/d/">belge doğrulama</a> sayfasında kodu girin veya dosyanın kendisini denetleyin.</p>
  </section>
</div>
'''
    return B.kabuk(yol="/pdf/", title="PDF Merkezi: Matematik Konu Anlatımı PDF'leri",
                   desc="Bütün matematik konu anlatımlarının ücretsiz PDF'leri. Her belgenin kodu ve sürümü var; güncelliğini QR kodla ya da dosyayla doğrulayın.",
                   govde=govde, jsonld=_jsonld_merkez(kayit), ek_betik='<script src="/js/pdf.js" defer></script>')


def _jsonld_merkez(kayit):
    ogeler = [{"@type": "ListItem", "position": i + 1, "url": V.ALAN + V.indirme_yolu(b["slug"]), "name": b["baslik"]}
              for i, b in enumerate(sorted((b for b in kayit["belgeler"].values() if yayindaki(b)), key=lambda b: b["no"]))]
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": V.ALAN + "/pdf/", "url": V.ALAN + "/pdf/", "name": "PDF Merkezi",
         "inLanguage": "tr-TR", "isAccessibleForFree": True,
         "publisher": {"@type": "Organization", "name": "ahmetcelen.com.tr", "url": V.ALAN + "/"},
         "mainEntity": {"@type": "ItemList", "numberOfItems": len(ogeler), "itemListElement": ogeler}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Ana Sayfa", "item": V.ALAN + "/"},
            {"@type": "ListItem", "position": 2, "name": "PDF Merkezi", "item": V.ALAN + "/pdf/"}]}]}


def _kirinti(*ogeler):
    parca = f'<a href="/">{ikon("ev")}<span>Ana Sayfa</span></a>'
    for ad, yol in ogeler:
        parca += ikon("ok-sag") + (f'<a href="{yol}">{k(ad)}</a>' if yol else f'<span>{k(ad)}</span>')
    return f'<div class="kap bs-yazi-ust"><nav class="bs-kirinti" aria-label="Sayfa yolu">{parca}</nav></div>'


def _noindex_jsonld(ad, yol):
    return {"@context": "https://schema.org", "@type": "WebPage", "name": ad, "url": V.ALAN + yol, "inLanguage": "tr-TR"}


# ── /pdf/<slug>/ ─────────────────────────────────────────────────────────
def indirme(kd, b, y):
    s = yayindaki(b)[-1]
    adres = V.medya_adresi(s["dosya"])
    kapak = (f'<img class="pdf-kapak" src="/blog/kapak/{k(y["kapak"])}-800.avif" alt="" width="800" height="450" decoding="async">'
             if y.get("kapak") else "")
    govde = f'''{_kirinti(("PDF Merkezi", "/pdf/"), (b["baslik"], None))}
<div class="kap pdf-indirme">
  <div class="pdf-belge">
    {kapak}
    <p class="pdf-ust-etiket">PDF · {k(kd)} · Sürüm {k(s["surum"])}</p>
    <h1>{k(b["baslik"])}</h1>
    <dl class="pdf-kunye">
      <dt>Belge kodu</dt><dd>{k(kd)}</dd>
      <dt>Sürüm</dt><dd>{k(s["surum"])} · {V.tr_tarih(s["tarih"])}</dd>
      <dt>Sayfa</dt><dd>{s["sayfa"]} sayfa, A4</dd>
      <dt>Boyut</dt><dd>{boyut(s["bayt"])}</dd>
      <dt>Yayımlayan</dt><dd>ahmetcelen.com.tr</dd>
    </dl>
    <p class="pdf-ucretsiz">Bu belge tamamen ücretsizdir. Size satmaya çalışanlara itibar etmeyiniz.</p>
    <p class="pdf-baglantilar"><a href="/blog/{k(y["slug"])}/">Yazıyı sitede oku</a><a href="{V.dogrulama_yolu(kd)}">Belgeyi doğrula</a><a href="/pdf/">Bütün PDF'ler</a></p>
  </div>
  <div class="pdf-bekleme" data-pdf-bekle="{BEKLEME}">
    <div class="pdf-sayac-kutu">
      <div class="pdf-sayac" aria-hidden="true"><svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="19"/><circle class="pdf-sayac-ilerle" cx="22" cy="22" r="19"/></svg><span data-pdf-kalan>{BEKLEME}</span></div>
      <p class="pdf-bekle-metin" data-pdf-bekle-metin aria-live="polite">PDF'iniz hazırlanıyor. İndirme bağlantısı <strong>{BEKLEME} saniye</strong> içinde açılacak.</p>
      <a class="bs-dugme-ana pdf-indir" href="{k(adres)}" data-pdf-indir rel="nofollow">{ikon("indir")}PDF'i indir ({boyut(s["bayt"])})</a>
    </div>
    {uc_reklam("pdf-indir-" + kd.lower())}
  </div>
  <section class="pdf-gecmis">
    <h2 class="bs-h2-ikon">{ikon("liste")}Sürüm geçmişi</h2>
    {gecmis_tablosu(b)}
  </section>
</div>
'''
    return B.kabuk(yol=V.indirme_yolu(b["slug"]), title=f"{b['baslik']} PDF İndir",
                   desc=f"{b['baslik']}: ücretsiz PDF, {kd} Sürüm {s['surum']}, {s['sayfa']} sayfa.",
                   govde=govde, jsonld=_noindex_jsonld(b["baslik"] + " PDF", V.indirme_yolu(b["slug"])),
                   gorsel=f"/blog/kapak/{y['kapak']}.avif" if y.get("kapak") else None,
                   taslak=True, ek_betik='<script src="/js/pdf.js" defer></script>')


# ── /d/ ──────────────────────────────────────────────────────────────────
def dogrulama_merkezi(kayit, bugun):
    govde = f'''{_kirinti(("PDF Merkezi", "/pdf/"), ("Belge doğrulama", None))}
<div class="kap pdf-dogrula">
  <h1>Belge doğrulama</h1>
  <p class="pdf-giris">ahmetcelen.com.tr'nin yayımladığı her PDF'in ilk sayfasında bir belge kodu (örneğin AC-066), sürüm numarası ve QR kod bulunur. QR kodu okutun, kodu aşağıya yazın ya da dosyanın kendisini denetleyin.</p>
  <form class="pdf-kod-form" data-pdf-kod-form>
    <label for="pdf-kod">Belge kodu</label>
    <input id="pdf-kod" name="kod" placeholder="AC-066" autocomplete="off" required>
    <button type="submit" class="bs-dugme-ana">Göster</button>
    <p class="pdf-kod-sonuc" role="status" aria-live="polite" data-pdf-kod-sonuc></p>
  </form>
  {dosya_denetimi()}
  {duyurular(kayit, bugun)}
  <p class="pdf-liste-bag"><a class="bs-dugme-ikincil" href="/pdf/">Güncel listeler: PDF Merkezi</a></p>
</div>
'''
    return B.kabuk(yol="/d/", title="Belge Doğrulama · PDF Merkezi", desc="ahmetcelen.com.tr PDF'lerinin güncelliğini ve özgünlüğünü doğrulayın.",
                   govde=govde, jsonld=_noindex_jsonld("Belge doğrulama", "/d/"), taslak=True,
                   ek_betik='<script src="/js/pdf.js" defer></script>')


def belge_sayfasi(kd, b):
    s = yayindaki(b)[-1]
    govde = f'''{_kirinti(("PDF Merkezi", "/pdf/"), ("Belge doğrulama", "/d/"), (kd, None))}
<div class="kap pdf-dogrula">
  <p class="pdf-ust-etiket">{k(kd)} · Yazı {b["no"]}</p>
  <h1>{k(b["baslik"])}</h1>
  <div class="pdf-sonuc pdf-sonuc-guncel pdf-sonuc-kucuk">
    <div><strong>Güncel sürüm: {k(s["surum"])}</strong><span>{V.tr_tarih(s["tarih"])} · {s["sayfa"]} sayfa · içerik izi {V.parmak_izi(s["icerik"])}</span></div>
    <a class="bs-dugme-ana" href="{V.indirme_yolu(b["slug"])}">{ikon("indir")}Güncel sürümü indir</a>
  </div>
  <section class="pdf-gecmis"><h2 class="bs-h2-ikon">{ikon("liste")}Sürüm geçmişi</h2>{gecmis_tablosu(b)}</section>
  {dosya_denetimi()}
  <p class="pdf-liste-bag"><a href="/blog/{k(b["slug"])}/">Yazıyı sitede oku</a> · <a href="/pdf/">Güncel listeler: PDF Merkezi</a></p>
</div>
'''
    return B.kabuk(yol=V.dogrulama_yolu(kd), title=f"{kd} · {b['baslik']} · Belge doğrulama",
                   desc=f"{kd} {b['baslik']} PDF'inin sürümleri ve güncelliği.", govde=govde,
                   jsonld=_noindex_jsonld(kd, V.dogrulama_yolu(kd)), taslak=True, ek_betik='<script src="/js/pdf.js" defer></script>')


def surum_sayfasi(kd, b, s):
    """QR hedefi. Guncelse yesil animasyon; degilse guncele yonlendirme (8 sn,
    iptal edilebilir) ve aradaki degisiklikler. Her iki durumda da PDF merkezi."""
    d = V.durum(b, s)
    son = yayindaki(b)[-1]
    sonraki = [x for x in yayindaki(b) if x["surum"] != s["surum"] and
               yayindaki(b).index(x) > yayindaki(b).index(s)]
    if d == "guncel":
        simge = ('<svg class="pdf-onay" viewBox="0 0 52 52" aria-hidden="true"><circle class="pdf-onay-daire" cx="26" cy="26" r="24"/>'
                 '<path class="pdf-onay-isaret" d="M15 27l7.5 7.5L38 19"/></svg>')
        baslik = "Bu belge güncel"
        metin = f"{k(kd)} · Sürüm {k(s['surum'])} en son sürümdür. Güvenle kullanabilir ve paylaşabilirsiniz."
        eylem = (f'<a class="bs-dugme-ana" href="/blog/{k(b["slug"])}/">Yazıyı sitede oku</a>'
                 '<a class="bs-dugme-ikincil" href="/pdf/">Güncel listeler: PDF Merkezi</a>')
        yonlendir = ""
    else:
        simge = ('<svg class="pdf-uyari" viewBox="0 0 52 52" aria-hidden="true"><circle cx="26" cy="26" r="24"/>'
                 '<path d="M26 14v15"/><path d="M26 37h.01"/></svg>')
        baslik = "Bu sürümde düzeltilmiş bir hata var" if d == "hata" else "Bu belgenin daha yeni bir sürümü var"
        metin = (f"Elinizdeki {k(kd)} · Sürüm {k(s['surum'])}. Güncel sürüm {k(son['surum'])} ({V.tr_tarih(son['tarih'])}). "
                 + ("Bu sürümden sonra bir hata düzeltildi; lütfen güncel sürümü kullanın ve paylaşın." if d == "hata"
                    else "Güncel sürümü kullanmanızı öneririz."))
        eylem = (f'<a class="bs-dugme-ana" href="{V.indirme_yolu(b["slug"])}" data-pdf-yonlendir>{ikon("indir")}Güncel sürümü indir ({k(son["surum"])})</a>'
                 '<a class="bs-dugme-ikincil" href="/pdf/">Güncel listeler: PDF Merkezi</a>')
        yonlendir = ('<p class="pdf-yonlendir" data-pdf-yonlendir-metin hidden>Güncel sürümün sayfasına <strong data-pdf-yonlendir-kalan>8</strong> saniye içinde '
                     'yönlendirileceksiniz. <button type="button" class="pdf-kal" data-pdf-kal>Burada kal</button></p>')
    degisiklikler = ""
    if sonraki:
        degisiklikler = ('<section class="pdf-gecmis"><h2 class="bs-h2-ikon">' + ikon("liste") + 'Bu sürümden sonraki değişiklikler</h2><ul class="pdf-degisiklik">'
                         + "".join(f'<li><strong>{k(x["surum"])}</strong> · {V.tr_tarih(x["tarih"])} {_rozet(x["tur"])}<p>{k(x["not"])}</p></li>' for x in sonraki)
                         + "</ul></section>")
    sinif = DURUM[d][0]
    govde = f'''{_kirinti(("PDF Merkezi", "/pdf/"), ("Belge doğrulama", "/d/"), (kd, V.dogrulama_yolu(kd)), ("Sürüm " + s["surum"], None))}
<div class="kap pdf-dogrula">
  <div class="pdf-sonuc pdf-sonuc-{sinif}">
    {simge}
    <div class="pdf-sonuc-ic">
      <p class="pdf-ust-etiket">{k(kd)} · {k(b["baslik"])}</p>
      <h1>{baslik}</h1>
      <p>{metin}</p>
      {yonlendir}
      <div class="pdf-eylem">{eylem}</div>
    </div>
  </div>
  <dl class="pdf-kunye pdf-kunye-yatay">
    <dt>Belge kodu</dt><dd>{k(kd)}</dd>
    <dt>Sürüm</dt><dd>{k(s["surum"])} · {V.tr_tarih(s["tarih"])}</dd>
    <dt>İçerik izi</dt><dd>{V.parmak_izi(s["icerik"])}</dd>
    <dt>Yayımlayan</dt><dd>ahmetcelen.com.tr</dd>
  </dl>
  <p class="pdf-iz-not">İçerik izi, PDF'in ilk sayfasındaki "Belge bilgileri" kutusunda yazan izle aynı olmalıdır.</p>
  {degisiklikler}
  {dosya_denetimi()}
</div>
'''
    return B.kabuk(yol=V.dogrulama_yolu(kd, s["surum"]), title=f"{kd} Sürüm {s['surum']} · {DURUM[d][1]}",
                   desc=f"{kd} {b['baslik']} PDF'i, Sürüm {s['surum']}: {DURUM[d][1].lower()}.", govde=govde,
                   jsonld=_noindex_jsonld(f"{kd} Sürüm {s['surum']}", V.dogrulama_yolu(kd, s["surum"])), taslak=True,
                   ek_betik='<script src="/js/pdf.js" defer></script>')


def uygula():
    kayit = V.oku()
    yazilar = dict(V.yazilar())
    bugun = datetime.date.today()
    n = 0
    # Yayindan kalkan adresler temizlenir; /pdf/ altinda YALNIZ bizim urettiklerimiz
    # (index.html'li slug klasorleri) silinir, eski sayfalar (parabol) korunur.
    hedef_slug = {b["slug"] for b in kayit["belgeler"].values() if yayindaki(b)}
    for p in (KOK / "pdf").iterdir():
        if p.is_dir() and p.name not in V.AYRILMIS and p.name not in hedef_slug and (p / "index.html").exists() \
                and "blog:taslak" in (p / "index.html").read_text(encoding="utf-8", errors="ignore"):
            shutil.rmtree(p)
    n += B.yaz("pdf/index.html", merkez(kayit, yazilar, bugun))
    n += B.yaz("d/index.html", dogrulama_merkezi(kayit, bugun))
    for kd, b in kayit["belgeler"].items():
        if not yayindaki(b):
            continue
        n += B.yaz(f"pdf/{b['slug']}/index.html", indirme(kd, b, yazilar[b["no"]]))
        n += B.yaz(f"d/{V.kod_yol(kd)}/index.html", belge_sayfasi(kd, b))
        for s in yayindaki(b):
            n += B.yaz(f"d/{V.kod_yol(kd)}/{V.surum_yol(s['surum'])}/index.html", surum_sayfasi(kd, b, s))
    print(f"pdf sayfalari: {sum(1 for b in kayit['belgeler'].values() if yayindaki(b))} belge · {n} dosya yazildi")


if __name__ == "__main__":
    uygula()
