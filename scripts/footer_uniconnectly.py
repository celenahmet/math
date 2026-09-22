#!/usr/bin/env python3
# scripts/footer_uniconnectly.py — alt bilgiye UniConnectly magaza baglantilari
# ekler (22.09.2026).
#
# Ahmet: "footer'a uniconnectly magaza linklerini koyabiliriz uygun olacak
# sekilde." Yer: alt bilgideki "Mobil" sutununun altina, kendi "Yakinda!"
# kutularini bozmadan. Koyu zemin oldugu icin yildizsiz KOYU logo kullanilir
# (kural: tanitim alaninda yildizsiz logo).
#
# Baglantilar ref + utm tasir; trafik Umami'de "footer" kampanyasi olarak
# ayrisir (uniconnectly_blok.py ile ayni desen).
#
# Idempotent: "<!-- ucfooter:bas -->" ... "<!-- ucfooter:son -->".
# Kullanim: python3 scripts/footer_uniconnectly.py
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
from uniconnectly_blok import MAGAZALAR, LOGO_KOYU, ref  # noqa: E402

BAS, SON = "<!-- ucfooter:bas -->", "<!-- ucfooter:son -->"
KAMPANYA = "footer"

rozetler = "\n".join(
    f'\t\t\t\t\t\t\t<a href="{adres.replace("{kampanya}", KAMPANYA)}" target="_blank" rel="noopener">'
    f'<img src="{gorsel}" alt="{ad}" width="120" height="36" loading="lazy" decoding="async"></a>'
    for ad, gorsel, adres in MAGAZALAR)

BLOK = f'''{BAS}
\t\t\t\t\t<div class="uc-footer">
\t\t\t\t\t\t<a class="uc-footer-logo" href="{ref("/", KAMPANYA)}" target="_blank" rel="noopener">
\t\t\t\t\t\t\t<img src="{LOGO_KOYU}" alt="UniConnectly" width="150" height="43" loading="lazy" decoding="async">
\t\t\t\t\t\t</a>
\t\t\t\t\t\t<p>Öğrenciler, etkinlikler, topluluklar, şirketler: hepsi bir arada. Ücretsiz.</p>
\t\t\t\t\t\t<div class="uc-footer-magazalar">
{rozetler}
\t\t\t\t\t\t</div>
\t\t\t\t\t</div>
{SON}'''

def uygula():
    # "Mobil" basliginin hemen altina ekle.
    # 22.09: eskiden capa app_grid ("Yakinda!" kutulari) idi; o blok
    # scripts/footer_yakinda_kaldir.py ile kaldirildi, capa basliga tasindi.
    desen = re.compile(r'(<h4>Mobil</h4>\n)')
    n = 0
    for p in sorted(KOK.rglob("*.html")):
        r = p.relative_to(KOK).as_posix()
        if r.startswith(("arsiv/", "okyanus/", "temaindexler/", "scripts/")):
            continue
        try:
            s = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "<h4>Mobil</h4>" not in s:
            continue
        if BAS in s and SON in s:
            a, b = s.index(BAS), s.index(SON) + len(SON)
            t = s[:a] + BLOK + s[b:]
        else:
            m = desen.search(s)
            if not m:
                continue
            t = s[:m.end(1)] + BLOK + "\n" + s[m.end(1):]
        if t != s:
            p.write_text(t, encoding="utf-8")
            n += 1
    print(f"footer UniConnectly blogu: {n} sayfa")

if __name__ == "__main__":
    uygula()
