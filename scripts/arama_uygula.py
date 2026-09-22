#!/usr/bin/env python3
# scripts/arama_uygula.py — site ici arama (22.09.2026)
#
# NEDEN: sayfadaki buyutec dugmesi CALISMIYORDU. Olculdu (canli, 22.09):
#   · masaustunde dugme HIC YOK — `#search-button` sayfada bulunmuyor,
#     yalnizca acilamayan bir katman (#mk-search-overlay) duruyordu.
#   · mobilde dugme katmani aciyor ama form `action` tasimiyor, girdilerin
#     `name`'i yok → yazip gonderince sayfa kendini yeniliyor, sonuc yok.
#
# COZUM: site statik (Vercel), sunucu tarafi arama yok. Bu betik sayfalardan
# bir DIZIN uretir (arama.json); js/arama.js dizini ilk acilista indirip
# tarayicida arar. Ucuncu taraf servis yok, ek istek yok (dizin yalnizca
# kullanici aramayi acinca iniyor), gizlilik disariya sizmiyor.
#
# KURAL: <title>, <h*> ve URL'lere DOKUNULMAZ (SEO). Bu betik yalniz
# arama dugmesini ve betik etiketini ekler.
#
# Idempotent: "<!-- arama:bas -->" ... "<!-- arama:son -->" bloklari.
# Kullanim: python3 scripts/arama_uygula.py
import json, re, sys, html, pathlib, datetime

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
from sitemap_uret import HARIC_ON_EK, HARIC_AD, HARIC_PARCA, HARIC_DESEN, yonlendirme_mi  # noqa: E402
import ss_veri  # noqa: E402
from jsonld_uygula import js_sinavlar  # noqa: E402

BAS, SON = "<!-- arama:bas -->", "<!-- arama:son -->"
BBAS, BSON = "<!-- aramabetik:bas -->", "<!-- aramabetik:son -->"

# Menunun SON maddesi olarak eklenir. Tema JS'i de `#search-button`e
# baglaniyor; js/arama.js zaten kendi dinleyicisini kuruyor, cift baglanma
# zararsiz (ikisi de ayni sinifi ekliyor).
DUGME = (
    '<li class="arama-madde">'
    '<a href="#" id="search-button" class="arama-tetik" aria-label="Sitede ara" title="Sitede ara">'
    '<span class="title"><i class="flaticon-magnifying-glass" aria-hidden="true"></i></span>'
    '</a></li>'
)

def metin(x):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", x))).strip()

def sayfalar():
    for p in sorted(KOK.rglob("*.html")):
        r = p.relative_to(KOK).as_posix()
        if r.startswith(HARIC_ON_EK) or p.name in HARIC_AD or HARIC_DESEN.match(p.name):
            continue
        if any(x in "/" + r for x in HARIC_PARCA) or yonlendirme_mi(p):
            continue
        yield p

def yol_of(p):
    r = p.relative_to(KOK).as_posix()
    if p.name == "index.html":
        return "/" if p.parent == KOK else "/" + p.parent.relative_to(KOK).as_posix() + "/"
    return "/" + r

# ── dizin ────────────────────────────────────────────────────────────────
def dizin():
    kayitlar, indeks = [], {}

    def ekle(baslik, adres, tur, anahtar="", aciklama="", agirlik=0):
        """Ayni ADRES icin ikinci kayit ACMAZ, mevcut kaydi zenginlestirir.

        Olculdu: /sinavlar/kpssa/ hem "Sayfa" hem "Sinav geri sayimi" olarak
        iki kez listeleniyordu; /pdf/parabol.pdf iki farkli baglanti metniyle
        iki kez cikiyordu. Kullanici icin ayni hedef iki satir demek.
        """
        if not baslik:
            return
        var = indeks.get(adres)
        if var is not None:
            ek = " ".join(x for x in (var.get("k", ""), baslik, anahtar) if x)
            var["k"] = ek[:400]
            if not var.get("d") and aciklama:
                var["d"] = aciklama[:160]
            if agirlik > var.get("w", 0):
                var["w"] = agirlik
            return
        k = {"b": baslik, "a": adres, "t": tur}
        if anahtar:
            k["k"] = anahtar
        if aciklama:
            k["d"] = aciklama[:160]
        if agirlik:
            k["w"] = agirlik
        indeks[adres] = k
        kayitlar.append(k)

    # 1) icerik sayfalari
    for p in sayfalar():
        s = p.read_text(encoding="utf-8", errors="ignore")
        yol = yol_of(p)
        tm = re.search(r"<title>(.*?)</title>", s, re.S)
        baslik = metin(tm.group(1)) if tm else ""
        baslik = re.sub(r"\s*[-–|]\s*(Ahmet\s*Çelen|Ahmetcelen\.com\.tr|Ahmet Celen).*$", "", baslik, flags=re.I).strip()
        dm = re.search(r'<meta name="description" content="([^"]*)"', s)
        aciklama = html.unescape(dm.group(1)).strip() if dm else ""
        if yol.startswith("/video/") and yol != "/video/":
            hm = re.search(r"<h3[^>]*>(.*?)</h3>", s, re.S)
            soru = metin(hm.group(1)) if hm else ""
            ad = pathlib.Path(yol).stem
            grup = "Parabol Fasikülü" if ad.startswith("parabol") else "Video"
            baslik = f"{grup} — {soru}" if soru else (baslik or ad)
            ekle(baslik, yol, "Video çözüm", anahtar=ad, agirlik=-2)
            continue
        if not baslik:
            continue
        # ana basliklar ek anahtar kelime olsun
        basliklar = " ".join(metin(x) for x in re.findall(r"<h[12][^>]*>(.*?)</h[12]>", s, re.S)[:4])
        # Agirlik sirasi OLCUMLE belirlendi: "kpss" aramasinda /ss/kpss/
        # sayfasi 35 adet tek tek OSYM yil kaydinin ALTINDA kaliyordu.
        # Bir SAYFA neredeyse her zaman tek bir belgeden daha iyi cevaptir.
        ekle(baslik, yol, "Sayfa", anahtar=basliklar, aciklama=aciklama,
             agirlik=8 if yol == "/" else (6 if yol.count("/") <= 2 else 5))

    # 2) cikmis sorular: her yil ayri kayit, dogrudan OSYM belgesine
    #    (OSYM PDF'leri burada BARINDIRILMAZ, yalnizca baglanti verilir)
    for a in ss_veri.SIRA:
        v = ss_veri.SAYFALAR[a]
        for yil, etiket, url in v["kartlar"]:
            ekle(f"{v['kisa']} {yil} — {etiket}", url, "Çıkmış soru (ÖSYM)",
                 anahtar=f"{a} {v['kisa']} {yil} cikmis sorular pdf cevap anahtari")

    # 3) sinav geri sayimlari
    for s in js_sinavlar().values():
        t = s["tarih"]
        ekle(f"{s['donem']} geri sayım", f"/sinavlar/{s['yol']}/", "Sınav geri sayımı",
             anahtar=f"{s['kisa']} {s['uzun']} ne zaman kac gun kaldi sinav takvimi {t[:4]}",
             aciklama=f"{t[8:10]}.{t[5:7]}.{t[:4]}" + (f" · saat {s['saat']}" if s["saatResmi"] else ""),
             agirlik=4)

    # 4) ders notu PDF'leri
    for kaynak in ("pdfnot/index.html", "video/index.html"):
        p = KOK / kaynak
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8", errors="ignore")
        for m in re.finditer(r'href="(/(?:yt|pdf)/[^"]+\.pdf)"[^>]*>(.*?)</a>', s, re.S | re.I):
            ad = metin(m.group(2))
            if ad and len(ad) < 120:
                ekle(ad, m.group(1), "Ders notu (PDF)", anahtar="pdf fasikul deneme not", agirlik=3)

    # 5) menudeki YouTube konu baglantilari: sitede PDF'i olmayan konular
    #    (orn. integral) yalnizca burada gecer; arama bos donmesin.
    ana = (KOK / "index.html").read_text(encoding="utf-8", errors="ignore")
    for m in re.finditer(r'href="(https://www\.youtube\.com/results\?search_query=[^"]+)"[^>]*>(.*?)</a>', ana, re.S):
        ad = metin(m.group(2))
        if ad and len(ad) < 60:
            ekle(f"{ad} videoları (YouTube)", m.group(1), "Video (YouTube)",
                 anahtar=f"{ad} video konu anlatimi izle", agirlik=2)

    kayitlar.sort(key=lambda k: (-k.get("w", 0), k["b"]))
    return kayitlar

# ── sayfalara baglama ────────────────────────────────────────────────────
def uygula():
    kayitlar = dizin()
    (KOK / "arama.json").write_text(
        json.dumps({"g": datetime.date.today().isoformat(), "s": kayitlar},
                   ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    dugme_n = betik_n = 0
    for p in sayfalar():
        s = p.read_text(encoding="utf-8", errors="ignore")
        t = s
        # a) masaustu arama dugmesi: #respMenu'nun SON maddesi
        if "respMenu" in t:
            blok = BAS + DUGME + SON
            if BAS in t and SON in t:
                a, b = t.index(BAS), t.index(SON) + len(SON)
                t = t[:a] + blok + t[b:]
            else:
                m = re.search(r'(<ul id="respMenu"[^>]*>)(.*?)(</ul>\s*</nav>)', t, re.S)
                if m:
                    t = t[:m.end(2)] + blok + t[m.end(2):]
        # b) betik: tema betiginden SONRA
        if "js/script.js" in t and BBAS not in t:
            t = t.replace('<script type="text/javascript" src="/js/script.js"></script>',
                          '<script type="text/javascript" src="/js/script.js"></script>\n'
                          + BBAS + '\n<script src="/js/arama.js"></script>\n' + BSON, 1)
        if t != s:
            p.write_text(t, encoding="utf-8")
        # sayac DEGISENI degil, MEVCUT durumu bildirir (ikinci calistirmada
        # hicbir sey degismez; "0 sayfa" yaniltici olurdu)
        if BAS in t:
            dugme_n += 1
        if BBAS in t:
            betik_n += 1
    print(f"arama.json: {len(kayitlar)} kayit · dugme {dugme_n} sayfa · betik {betik_n} sayfa")

if __name__ == "__main__":
    uygula()
