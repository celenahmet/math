#!/usr/bin/env python3
# scripts/css_surum.py — css/duzeltmeler.css baglantisina icerik ozetinden
# turetilen surum eki (?v=...) yazar.
#
# Neden: vercel.json CSS'i 7 gun onbellekliyor (max-age=604800). Dosya
# degisince tarayici eski CSS'i gostermeye devam ediyordu (Ahmet 21.09'da
# menuyu hala eski hizada gordu). Adres degisince onbellek anahtari da
# degisir; uzun onbellek korunur, guncelleme aninda gorunur.
#
# Kullanim: python3 scripts/css_surum.py   (duzeltmeler.css degisince kos)
import hashlib, pathlib, re

KOK = pathlib.Path(__file__).resolve().parent.parent
CSS = KOK / "css" / "duzeltmeler.css"
ozet = hashlib.sha256(CSS.read_bytes()).hexdigest()[:8]
desen = re.compile(r'href="/css/duzeltmeler\.css(?:\?v=[0-9a-f]+)?"')
yeni = f'href="/css/duzeltmeler.css?v={ozet}"'

sayac = 0
for p in KOK.rglob("*.html"):
    if "scripts" in p.parts:
        continue
    s = p.read_text(encoding="utf-8", errors="surrogateescape")
    y, n = desen.subn(yeni, s)
    if n and y != s:
        p.write_text(y, encoding="utf-8", errors="surrogateescape")
        sayac += 1
print(f"v={ozet} → {sayac} sayfa guncellendi")
