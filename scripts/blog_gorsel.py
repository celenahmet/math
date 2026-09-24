#!/usr/bin/env python3
# scripts/blog_gorsel.py — blog kapaklarini AVIF'e cevirir (23.09.2026)
#
# ⚠️ NEDEN AVIF, NEDEN WEBP DEGIL: vercel.json'daki ilk yonlendirme
# `.webp` DAHIL bir uzanti listesini medya.ahmetcelen.com.tr'ye 307 ile
# gonderiyor. Yani depoya konan bir .webp SITEDEN SERVIS EDILMEZ, medya
# sunucusuna gider; oraya yukleme erisimi ajanda yok. `.avif` o listede
# DEGIL, dogrudan Vercel'den servis ediliyor. Ustelik AVIF daha kucuk.
# Yonlendirme listesine ileride avif eklenirse bu kapaklar kirilir --
# eklenmeden once buraya bakilmali.
#
# Kaynak: blog-gorselleri/NN-slug.png (1672x941, ~2 MB)
# Cikti : blog/kapak/<slug>.avif (1600 px) + <slug>-800.avif (kart icin)
#
# Kullanim: python3 scripts/blog_gorsel.py <kaynak.png> <slug>
import pathlib, subprocess, sys

KOK = pathlib.Path(__file__).resolve().parent.parent
HEDEF = KOK / "blog/kapak"

def cevir(kaynak, slug, olculer=((1600, ""), (800, "-800"), (240, "-240"))):
    HEDEF.mkdir(parents=True, exist_ok=True)
    cikti = []
    # -240: sag bloktaki "Populer / En yeni" kucuk resmi (72 px, 2x ekran).
    # 800 px'lik kapagi orada kullanmak sayfa basina ~240 KB fazladan inis demekti.
    for en, ek in olculer:
        ara = HEDEF / f"_{slug}{ek}.png"
        son = HEDEF / f"{slug}{ek}.avif"
        subprocess.run(["sips", "-Z", str(en), str(kaynak), "--out", str(ara)],
                       check=True, capture_output=True)
        # -q 62: kapak fotografi icin gozle ayirt edilemeyen kalite;
        # -s 6 hiz/oran dengesi (0 en yavas, 10 en hizli).
        subprocess.run(["avifenc", "-q", "62", "-s", "6", str(ara), str(son)],
                       check=True, capture_output=True)
        ara.unlink()
        cikti.append((son, son.stat().st_size))
    return cikti

if __name__ == "__main__":
    # --kucuk: yalniz -240 uretir (var olan kapaklara dokunmaz)
    kaynak, slug = sys.argv[1], sys.argv[2]
    ham = pathlib.Path(kaynak).stat().st_size
    olc = ((240, "-240"),) if "--kucuk" in sys.argv[3:] else ((1600, ""), (800, "-800"), (240, "-240"))
    for yol, boyut in cevir(kaynak, slug, olc):
        print(f"{yol.relative_to(KOK)}  {boyut//1024} KB  (kaynak {ham//1024} KB)")
