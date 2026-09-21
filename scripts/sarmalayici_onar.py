#!/usr/bin/env python3
# scripts/sarmalayici_onar.py — mobil menunun (nav#menu) ardindaki iki fazla
# </div> sayfanin .wrapper'ini erken kapatiyordu. mmenu acilinca yalniz
# .wrapper (mm-page) kaydirildigindan, disarida kalan icerik tablet/telefonda
# menunun saginda BEYAZ alan olarak gorunuyordu (Ahmet, 22.09 iPad goruntusu).
# Bir kez kosulur; sonuc her sayfada div yigini ile dogrulanir.
import re, pathlib
KOK = pathlib.Path(__file__).resolve().parent.parent
DESEN = re.compile(r"(\t\t</nav>\n\t</div>\n)</div>\n</div>\n")

def yigin(s):
    st, fazla = [], 0
    for m in re.finditer(r"<div\b[^>]*>|</div>", s):
        if m.group(0).startswith("</"):
            if st: st.pop()
            else: fazla += 1
        else: st.append(1)
    return len(st), fazla

n = 0
for p in KOK.rglob("*.html"):
    r = p.as_posix()
    if r.startswith(("temaindexler/", "okyanus/", "arsiv/")) or "/tema/" in r: continue
    s = p.read_text(encoding="utf-8", errors="surrogateescape")
    y, k = DESEN.subn(r"\1", s, count=1)
    if k:
        acik, fazla = yigin(y)
        durum = "dengeli" if (acik, fazla) == (0, 0) else f"acik={acik} fazla={fazla}"
        p.write_text(y, encoding="utf-8", errors="surrogateescape"); n += 1
        if durum != "dengeli": print(f"  {r}: {durum}")
print(f"{n} sayfa onarildi")
