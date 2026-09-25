#!/usr/bin/env python3
# scripts/css_surum.py — kendi CSS/JS dosyalarimizin baglantilarina icerik
# ozetinden turetilen surum eki (?v=...) yazar.
#
# Neden: vercel.json CSS/JS'i 7 gun onbellekliyor (max-age=604800). Dosya
# degisince tarayici eski surumu gostermeye devam ediyordu (21.09: Ahmet
# menuyu eski hizada gordu; 22.09: geri sayim JS'i eski surumle calismadi,
# "Yaklasiyor" rozeti sabit kaldi). Adres degisince onbellek anahtari da
# degisir; uzun onbellek korunur, guncelleme aninda gorunur.
#
# Kullanim: python3 scripts/css_surum.py   (listedeki dosya degisince kos;
# uretici betikler zaten cagiriyor)
import hashlib, pathlib, re

KOK = pathlib.Path(__file__).resolve().parent.parent
# 22.09: css/style.css listeye eklendi — icindeki 14 @import kaldirildi
# (scripts/css_zinciri.py). Surum eki olmasa donen ziyaretcide 7 gun boyunca
# ESKI style.css kalir, 14 dosya hem @import hem <link> ile iki kez inerdi.
VARLIKLAR = ["css/duzeltmeler.css", "css/style-az.css", "css/font-awesome-az.css",
              "css/flaticon-az.css", "sinavlar/js/sinav-takvimi.js",
              "js/uniconnectly-blok.js", "js/sayfa-duzeltmeleri.js", "js/arama.js", "css/blog.css", "js/blog.js", "js/etkilesim.js"]

def ozet(yol):
    p = KOK / yol
    return hashlib.sha256(p.read_bytes()).hexdigest()[:8] if p.exists() else None

kurallar = []
for yol in VARLIKLAR:
    o = ozet(yol)
    if not o:
        continue
    desen = re.compile(r'(href|src)="/' + re.escape(yol) + r'(?:\?v=[0-9a-f]+)?"')
    kurallar.append((desen, yol, o))

sayac = 0
for p in KOK.rglob("*.html"):
    if "scripts" in p.parts:
        continue
    s = p.read_text(encoding="utf-8", errors="surrogateescape")
    y = s
    for desen, yol, o in kurallar:
        y = desen.sub(lambda m, yol=yol, o=o: f'{m.group(1)}="/{yol}?v={o}"', y)
    if y != s:
        p.write_text(y, encoding="utf-8", errors="surrogateescape")
        sayac += 1
print(" · ".join(f"{yol} v={o}" for _, yol, o in kurallar) + f" → {sayac} sayfa guncellendi")
