#!/usr/bin/env python3
# scripts/jsonld_uygula.py — yapilandirilmis veri (JSON-LD) ekler (22.09.2026)
#
# NEDEN: denetimde sitede HIC schema.org isareti yoktu. Iki ayri kazanim var:
#   1. Google zengin sonuc (SSS acilir listesi, kirinti yolu, etkinlik tarihi)
#   2. Dil modelleri sayfayi metinden tahmin etmek yerine VERIDEN okur
#      (llms.txt bunu tamamlar, yerine gecmez).
#
# GSC 22.09 gerekcesi:
#   · /ss/kpss/  19.052 tik, poz 8,9 → SSS + ItemList ile SERP alani buyur.
#   · /sinavlar/msu/ 31.850 gosterim, TO %0,16; "msü kaç gün kaldı" 13.788
#     gosterim → sinav gunu Event olarak isaretleniyor.
#
# KURAL: <title>, <h*> ve URL DEGISMEZ. Yalniz <head>'e script eklenir.
# Idempotent: "<!-- jsonld:bas -->" ... "<!-- jsonld:son -->" blogu.
#
# Kullanim: python3 scripts/jsonld_uygula.py
import json, re, sys, pathlib, html

KOK = pathlib.Path(__file__).resolve().parent.parent
ALAN = "https://ahmetcelen.com.tr"
BAS, SON = "<!-- jsonld:bas -->", "<!-- jsonld:son -->"
sys.path.insert(0, str(KOK / "scripts"))
import ss_veri  # noqa: E402

KISI = {
    "@type": "Person",
    "@id": ALAN + "/#kisi",
    "name": "Ahmet Çelen",
    "url": ALAN + "/hakkimizda/",
    "email": "ahmetcelen@hacettepe.edu.tr",
    "jobTitle": "Yazılım geliştirici",
    "alumniOf": {"@type": "CollegeOrUniversity", "name": "Hacettepe Üniversitesi"},
    "sameAs": [
        "https://www.youtube.com/channel/UCCXZwb5Y9Tphcv41jfgKI7w",
        "https://uniconnectly.com",
        "https://www.ahmetcelen.com",
    ],
}
SITE = {
    "@type": "WebSite",
    "@id": ALAN + "/#site",
    "url": ALAN + "/",
    "name": "Ahmet Çelen",
    "inLanguage": "tr-TR",
    "description": "Üniversite ve kamu sınavlarına hazırlananlar için ücretsiz matematik ders notları, denemeler, video çözümler ve ÖSYM çıkmış soru bağlantıları.",
    "publisher": {"@id": ALAN + "/#kisi"},
}

def kirinti(parcalar):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": ad, "item": ALAN + yol}
        for i, (ad, yol) in enumerate(parcalar)]}

def sss(cevaplar):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": s, "acceptedAnswer": {"@type": "Answer", "text": c}}
        for s, c in cevaplar]}

# ── /ss/* : cikmis sorular ────────────────────────────────────────────────
def ss_grafi(anahtar, v):
    yol = f"/ss/{anahtar}/"
    kisa, kartlar = v["kisa"], v["kartlar"]
    yillar = [k[0] for k in kartlar]
    liste = {"@type": "ItemList", "name": f"{kisa} çıkmış sorular (ÖSYM temel soru kitapçıkları)",
             "numberOfItems": len(kartlar), "itemListOrder": "https://schema.org/ItemListOrderAscending",
             "itemListElement": [
                 {"@type": "ListItem", "position": i + 1, "name": f"{y} {etiket}",
                  "url": url}
                 for i, (y, etiket, url) in enumerate(kartlar)]}
    sorular = [
        (f"{kisa} çıkmış sorular hangi yılları kapsıyor?",
         f"{min(yillar)}-{max(yillar)} arası {len(yillar)} yılın ÖSYM temel soru kitapçığı ve cevap anahtarı listelenir."),
        (f"{kisa} çıkmış sorular PDF ücretsiz mi?",
         "Evet. Bağlantıların tamamı ÖSYM'nin kendi belge sunucusundaki (dokuman.osym.gov.tr) ücretsiz PDF'lere gider; üyelik ya da ödeme istenmez."),
        ("PDF'ler bu sitede mi barındırılıyor?",
         "Hayır. Hiçbir ÖSYM belgesi burada yeniden yayımlanmaz; her bağlantı doğrudan ÖSYM'nin resmî adresine açılır."),
        (f"{kisa} cevap anahtarı da var mı?",
         "Evet. ÖSYM temel soru kitapçıkları cevap anahtarını da içerir; ayrı bir dosya aramanıza gerek yoktur."),
    ]
    return [liste, sss(sorular),
            kirinti([("Ana Sayfa", "/"), ("Çıkmış Sorular", "/ss/"), (kisa, yol)])]

# ── /sinavlar/* : geri sayim ──────────────────────────────────────────────
def js_sinavlar():
    js = (KOK / "sinavlar/js/sinav-takvimi.js").read_text(encoding="utf-8")
    govde = js[js.index("var SINAVLAR = {"):js.index("var SIRA")]
    d = {}
    for m in re.finditer(r"^\s{4}(\w+): \{(.*?)^\s{4}\},?$", govde, re.S | re.M):
        a, ic = m.group(1), m.group(2)
        al = lambda k: (re.search(r"%s: '([^']*)'" % k, ic) or [None, None])[1]
        d[a] = {"kisa": al("kisa"), "yol": al("yol"), "uzun": al("uzun"), "donem": al("donem"),
                "tarih": al("tarih"), "saat": al("saat"),
                "saatResmi": "saatResmi: true" in ic, "sonuc": al("sonuc")}
    return d

def sinav_grafi(a, s):
    yol = f"/sinavlar/{s['yol']}/"
    baslangic = f"{s['tarih']}T{s['saat']}:00+03:00"
    olay = {
        "@type": "Event",
        "name": s["donem"],
        "description": s["uzun"],
        "startDate": baslangic if s["saatResmi"] else s["tarih"],
        "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
        "eventStatus": "https://schema.org/EventScheduled",
        "location": {"@type": "Country", "name": "Türkiye"},
        "organizer": {"@type": "GovernmentOrganization", "name": "ÖSYM",
                      "url": "https://www.osym.gov.tr/"},
        "url": ALAN + yol,
        "isAccessibleForFree": True,
    }
    sorular = [
        (f"{s['kisa']} ne zaman yapılacak?",
         f"{s['donem']} sınavı {s['tarih'][8:10]}.{s['tarih'][5:7]}.{s['tarih'][:4]} tarihinde"
         + (f", saat {s['saat']}'te" if s["saatResmi"] else "") + " yapılır. Tarih ÖSYM'nin resmî sınav takviminden alınmıştır."),
        (f"{s['kisa']} sonuçları ne zaman açıklanacak?",
         f"ÖSYM takvimine göre sonuç açıklama tarihi {s['sonuc']}." if s.get("sonuc")
         else "ÖSYM sonuç tarihini takvimde yayımladığında bu sayfada gösterilir."),
        (f"{s['kisa']} çıkmış soruları nereden indirilir?",
         "Bu sitedeki çıkmış sorular sayfasından ÖSYM'nin resmî temel soru kitapçıklarına ulaşabilirsiniz."),
    ]
    return [olay, sss(sorular),
            kirinti([("Ana Sayfa", "/"), ("Sınav Geri Sayımları", "/sinavlar/"), (s["kisa"], yol)])]

def graf(nesneler):
    return {"@context": "https://schema.org", "@graph": [SITE, KISI] + nesneler}

def yaz(dosya, nesneler):
    p = KOK / dosya
    s = p.read_text(encoding="utf-8")
    blok = (BAS + '\n<script type="application/ld+json">'
            + json.dumps(graf(nesneler), ensure_ascii=False, separators=(",", ":"))
            + "</script>\n" + SON + "\n")
    if BAS in s and SON in s:
        a, b = s.index(BAS), s.index(SON) + len(SON) + 1
        t = s[:a] + blok + s[b:]
    else:
        t = s.replace("</head>", blok + "</head>", 1)
    if t != s:
        p.write_text(t, encoding="utf-8")
    return t != s

def uygula():
    n = 0
    for a in ss_veri.SIRA:
        n += yaz(f"ss/{a}/index.html", ss_grafi(a, ss_veri.SAYFALAR[a]))
    # /ss/ hub: tum sayfalarin listesi
    hub = {"@type": "ItemList", "name": "ÖSYM çıkmış sorular sayfaları",
           "itemListElement": [{"@type": "ListItem", "position": i + 1,
                                "name": f"{ss_veri.SAYFALAR[a]['kisa']} çıkmış sorular",
                                "item": f"{ALAN}/ss/{a}/"} for i, a in enumerate(ss_veri.SIRA)]}
    n += yaz("ss/index.html", [hub, kirinti([("Ana Sayfa", "/"), ("Çıkmış Sorular", "/ss/")])])

    sinavlar = js_sinavlar()
    for a, s in sinavlar.items():
        n += yaz(f"sinavlar/{s['yol']}/index.html", sinav_grafi(a, s))
    takvim = {"@type": "ItemList", "name": "2026 ÖSYM sınav takvimi geri sayımları",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": s["donem"],
                                   "item": f"{ALAN}/sinavlar/{s['yol']}/"}
                                  for i, s in enumerate(sinavlar.values())]}
    n += yaz("sinavlar/index.html", [takvim, kirinti([("Ana Sayfa", "/"), ("Sınav Geri Sayımları", "/sinavlar/")])])

    # Hakkimda / Iletisim / ana sayfa
    n += yaz("hakkimizda/index.html", [{"@type": "AboutPage", "url": ALAN + "/hakkimizda/", "mainEntity": {"@id": ALAN + "/#kisi"}},
                                       kirinti([("Ana Sayfa", "/"), ("Hakkımda", "/hakkimizda/")])])
    n += yaz("iletisim/index.html", [{"@type": "ContactPage", "url": ALAN + "/iletisim/", "mainEntity": {"@id": ALAN + "/#kisi"}},
                                     kirinti([("Ana Sayfa", "/"), ("İletişim", "/iletisim/")])])
    n += yaz("index.html", [{"@type": "CollectionPage", "url": ALAN + "/", "about": {"@id": ALAN + "/#kisi"}}])

    # /pdfnot/ : ders notu listesi
    s = (KOK / "pdfnot/index.html").read_text(encoding="utf-8")
    notlar = []
    for m in re.finditer(r'href="(/[^"]+\.pdf)"[^>]*>(.*?)</a>', s, re.S | re.I):
        ad = re.sub(r"<[^>]+>", " ", m.group(2))
        ad = html.unescape(re.sub(r"\s+", " ", ad)).strip()
        if ad and len(ad) < 120:
            notlar.append((ad, ALAN + m.group(1)))
    gorulen, temiz = set(), []
    for ad, u in notlar:
        if u in gorulen:
            continue
        gorulen.add(u)
        temiz.append({"@type": "ListItem", "position": len(temiz) + 1, "name": ad,
                      "item": {"@type": "DigitalDocument", "name": ad, "url": u,
                               "encodingFormat": "application/pdf", "inLanguage": "tr-TR",
                               "isAccessibleForFree": True, "author": {"@id": ALAN + "/#kisi"}}})
    n += yaz("pdfnot/index.html", [{"@type": "ItemList", "name": "Ücretsiz matematik ders notları (PDF)",
                                    "numberOfItems": len(temiz), "itemListElement": temiz},
                                   kirinti([("Ana Sayfa", "/"), ("Ders Notları", "/pdfnot/")])])
    print(f"jsonld: {n} sayfa guncellendi · pdfnot {len(temiz)} belge")

if __name__ == "__main__":
    uygula()
