#!/usr/bin/env python3
# scripts/footer_yakinda_kaldir.py — alt bilgideki "Yakinda!" kutularini
# kaldirir (22.09.2026).
#
# Ahmet: "footerda mobil yaziyo ya, yakinda kisimlarini kaldiralim."
# Tema alt bilgisinde "Mobil" sutununun altinda iki adet tiklanmayan dugme
# vardi: App Store / Yakinda! ve Google Play / Yakinda!. Site icin mobil
# uygulama yok; bos vaat duruyordu. UniConnectly rozetleri (gercek magaza
# baglantilari) KALIR — onlar ayri blok (ucfooter:bas ... ucfooter:son).
#
# Idempotent: app_grid blogu yoksa dosyaya dokunulmaz.
# Kullanim: python3 scripts/footer_yakinda_kaldir.py
import re, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
HARIC = ("arsiv", "okyanus", "temaindexler", "scripts")
# <div class="app_grid"> ... </div> — icinde iki <button>, ic ice div yok.
DESEN = re.compile(r"[ \t]*<div class=\"app_grid\">.*?</div>\n", re.S)

def uygula():
    n = 0
    for p in sorted(KOK.rglob("*.html")):
        if p.relative_to(KOK).parts[0] in HARIC:
            continue
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        t, k = DESEN.subn("", s)
        if k:
            assert "Yakında!" not in t or "app_grid" in t, "beklenmeyen kalinti"
            p.write_text(t, encoding="utf-8")
            n += 1
    print(f"alt bilgi 'Yakinda!' kutulari: {n} sayfadan kaldirildi")

if __name__ == "__main__":
    uygula()
