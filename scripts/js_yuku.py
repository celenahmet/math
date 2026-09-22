#!/usr/bin/env python3
# scripts/js_yuku.py — sayfa basina gereksiz tema betiklerini kaldirir (22.09.2026)
#
# OLCUM (canli mobil Lighthouse, /ss/kpss/): FCP 5,8 sn · LCP 7,8 sn.
# CSS zinciri kirildiktan SONRA engelleyici stil tasarrufu 0 ms'e dustu;
# geriye kalan yuk BETIKLERDE: tek bir icerik sayfasi ~1,05 MB ham JS
# indiriyordu. Icindekilerin cogu o sayfada hicbir sey yapmiyor.
#
# YONTEM: bir betik, karsiligi olan ISARET sayfanin govdesinde yoksa kaldirilir.
# Isaretler olculdu (sinif/oznitelik taramasi, 22.09):
#   owl-carousel/slick/maximage → yalniz index, indexcopy, cozum, video/*
#   class="timer"               → yalniz index, indexcopy
#   selectpicker, simplebar, parallax, isotope, countdown, wow → HICBIR sayfada yok
#
# GUVENLIK AGI: js/sayfa-duzeltmeleri.js icindeki sim blogu, kaldirilan
# eklentilerin adlarini bos fonksiyon olarak tanimlar. Boylece tema betigi
# (js/script.js) korumasiz cagri yapsa bile TypeError firlatmaz. Sim ONCE
# yuklenir; gercek eklenti varsa dokunulmaz.
#
# jQuery: 340 KB'lik kaynak surum yerine resmi kucultulmus surum
# (jquery-3.3.1.min.js, SRI sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=
# ile dogrulandi) kullanilir. Davranis ayni, 254 KB az.
#
# Kullanim: python3 scripts/js_yuku.py
import re, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
HARIC = ("arsiv", "okyanus", "temaindexler", "scripts")

# betik -> sayfada aranan isaret (None = her sayfadan kaldir)
KALDIR = {
    "timepicker.js": r'id="countdown"|datetimepicker|timepicker',
    "isotop.js": r'isotope|magnificPopup|popup-img',          # magnificPopup'i da tanimlar
    "bootstrap-select.min.js": r"selectpicker",
    "simplebar.js": r"data-simplebar|simplebar\"",
    "parallax.js": r'data-parallax|class="[^"]*parallax',
    "jquery-scrolltofixed-min.js": None,                       # sayfa-duzeltmeleri.js etkisiz kildi
    "wow.min.js": r'class="[^"]*\bwow\b',
    "slider.js": r"owl-carousel|owl-theme|slick-slider|maximage",
    "jquery.counterup.js": r'class="timer"',
}

def uygula():
    kaldirilan = {}
    jq = sayfa = 0
    for p in sorted(KOK.rglob("*.html")):
        if p.relative_to(KOK).parts[0] in HARIC:
            continue
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        t = s
        # govde: isaret aramasi betik etiketlerinin disinda yapilmali
        govde = re.sub(r"<script[^>]*>.*?</script>", "", s, flags=re.S)
        for ad, isaret in KALDIR.items():
            if isaret and re.search(isaret, govde):
                continue
            desen = re.compile(r"[ \t]*<script[^>]*src=\"/js/" + re.escape(ad) + r"(?:\?v=[0-9a-f]+)?\"[^>]*></script>\n?")
            t, k = desen.subn("", t)
            if k:
                kaldirilan[ad] = kaldirilan.get(ad, 0) + k
        y = t.replace('src="/js/jquery-3.3.1.js"', 'src="/js/jquery-3.3.1.min.js"')
        if y != t:
            jq += 1
        t = y
        if t != s:
            p.write_text(t, encoding="utf-8")
            sayfa += 1
    for ad, n in sorted(kaldirilan.items(), key=lambda x: -x[1]):
        kb = (KOK / "js" / ad).stat().st_size // 1024
        print(f"  - {ad:32s} {n:4d} sayfadan kaldirildi ({kb} KB)")
    print(f"jquery kucultulmus surume gecirildi: {jq} sayfa · toplam {sayfa} sayfa yazildi")

if __name__ == "__main__":
    uygula()
