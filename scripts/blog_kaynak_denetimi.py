#!/usr/bin/env python3
# scripts/blog_kaynak_denetimi.py — blog kaynaklarinin IC denetim raporu
# (23.09.2026)
#
# Ahmet: "kaynaklar kismini not alalim ama yayinda gostermeyelim, kendi
# icimizde denetim icin kullanalim; MEB sorularini kullanmak yasak olabilir
# cunku."
#
# Kaynaklar yazi verisinde (scripts/yazilar/*.py) DURUYOR ama sayfaya
# BASILMIYOR. Bu betik onlari tek bir ic rapora topluyor ve her adresin
# hala ayakta olup olmadigini olcuyor.
#
# ⚠️ Rapor YAYINA CIKMAZ: .vercelignore `*.md` ve `scripts/` dizinini
# yayindan cikariyor (23.09'da eklendi; oncesinde scripts/ herkese acikti).
#
# Kullanim: python3 scripts/blog_kaynak_denetimi.py [--baglanti]
#   --baglanti  adreslere HTTP istegi atip durum kodunu yazar (yavas)
import datetime, pathlib, subprocess, sys

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import blog_veri  # noqa: E402

DENETLE = "--baglanti" in sys.argv
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36")


def durum(url):
    if not DENETLE:
        return "—"
    try:
        r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
                            "-L", "--max-time", "20", "-A", UA, url],
                           capture_output=True, text=True, timeout=30)
        return r.stdout.strip() or "?"
    except Exception:
        return "?"


def uret():
    y = sorted(blog_veri.YAZILAR, key=lambda x: x["tarih"])
    s = ["# Blog kaynak denetimi (İÇ BELGE — yayına çıkmaz)", ""]
    s.append(f"Üretim: `scripts/blog_kaynak_denetimi.py` · {datetime.date.today().isoformat()}")
    s += ["", "## Neden bu belge var", "",
          "Kaynaklar **yayımlanan sayfada gösterilmiyor** (Ahmet, 23.09). Yine de",
          "her yazının hangi kaynağa dayandığı kayıt altında olmalı: bir bilgi",
          "sorgulanırsa nereden geldiğini gösterebilelim.", "",
          "## Telif kuralı", "",
          "- Yazılarda **başka bir kurumun sorusu kullanılmaz**. MEB, ÖSYM ya da",
          "  yayınevi sorularının metni alınmaz, uyarlanmaz.",
          "- Örnekler **özgün** yazılır. Şu ana kadarki yazılarda dışarıdan",
          "  alınmış tek bir soru yoktur.",
          "- Kaynak yalnız **tanım, kazanım ve müfredat çerçevesi** için",
          "  kullanılır; oradan da metin kopyalanmaz.",
          "- ÖSYM belgeleri siteye **yüklenmez**, yalnız bağlantı verilir",
          "  (bu kural `/ss/` sayfalarında zaten uygulanıyor).", ""]
    s += ["## Yazı başına kaynaklar", ""]
    for x in y:
        s.append(f"### {x['baslik']}")
        s.append("")
        s.append(f"- Adres: `/blog/{x['slug']}/` · Tarih: {x['tarih']}"
                 + (" · **TASLAK**" if x.get("taslak") else ""))
        kaynaklar = x.get("kaynaklar") or []
        if not kaynaklar:
            s.append("- ⚠️ Kaynak kaydı YOK")
        for ad, url in kaynaklar:
            s.append(f"- {ad} — <{url}> · durum: {durum(url)}")
        s.append("")
    yol = KOK / "blog-KAYNAK-DENETIMI.md"
    yol.write_text("\n".join(s) + "\n", encoding="utf-8")
    n = sum(len(x.get("kaynaklar") or []) for x in y)
    print(f"{yol.name}: {len(y)} yazi · {n} kaynak"
          + (" · baglantilar denetlendi" if DENETLE else " (baglanti denetimi icin --baglanti)"))


if __name__ == "__main__":
    uret()
