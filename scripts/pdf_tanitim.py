#!/usr/bin/env python3
# scripts/pdf_tanitim.py — cikmis sorular ve geri sayim sayfalarinda PDF merkezi
# ic tanitimi (28.09.2026)
#
# Ahmet (28.09): "genel olarak SEO odakli trafik alan sayfalar, cikmis sorular ve
# kalan gunler; bu PDF ders notu kismina kesin reklam verelim, kendi icimizde."
# Sayfanin sinavina uyan (blog etiketi) ilk 6 PDF + merkeze baglanti. Veri
# pdf/kayit.json (yalniz YAYINDA surumler). Baslik/H1/H3'lere dokunulmaz; blok
# ek bolum olarak girer. Stil: css/duzeltmeler.css blok 29.
# ⚠️ Okura donuk metin VARSAYILAN; son hali Ahmet'in.
import html

import pdf_veri as V

k = lambda s: html.escape(str(s), quote=True)   # noqa: E731

# sayfa anahtari → blog yazisi sinav etiketleri
ESLEME = {
    "tyt": ["TYT"], "ayt": ["AYT"], "msu": ["TYT"], "dgs": ["ALES", "TYT"],
    "kpss": ["KPSS"], "kpssa": ["KPSS"], "kpss-onlisans": ["KPSS"], "kpss-ortaogretim": ["KPSS"],
    "ales1": ["ALES"], "ales2": ["ALES"], "ales3": ["ALES"],
}


def blok(anahtar, sinav_adi, adet=6):
    etiketler = ESLEME.get(anahtar)
    kayit = V.oku()
    secim = []
    for kd, b in sorted(kayit["belgeler"].items(), key=lambda x: x[1]["no"]):
        yayinda = [s for s in b["surumler"] if V.yayinda_mi(s)]
        if not yayinda:
            continue
        y = dict(V.yazilar()).get(b["no"], {})
        if etiketler and not set(etiketler) & set(y.get("sinavlar", [])):
            continue
        secim.append((kd, b, yayinda[-1]))
    if not secim:
        return ""
    toplam = len(secim)
    # Once aramada hedeflenen "... Konu Anlatimi PDF" yazilari, sonra numara sirasi.
    secim.sort(key=lambda x: (0 if "PDF" in x[1]["baslik"] else 1, x[1]["no"]))
    kartlar = "\n".join(
        f'\t\t\t\t<a class="pdf-tanitim-kart" href="{V.indirme_yolu(b["slug"])}">'
        f'<span class="pdf-tanitim-kod">{k(kd)}</span>'
        f'<span class="pdf-tanitim-ad">{k(V.pdf_adi(b["baslik"]))}</span>'
        f'<span class="pdf-tanitim-kunye">{s["sayfa"]} sayfa · Sürüm {k(s["surum"])} · ücretsiz</span></a>'
        for kd, b, s in secim[:adet])
    ara = f"#ara={etiketler[0].lower()}" if etiketler else ""
    ad = f"{sinav_adi} matematiğinde" if sinav_adi else "Sınavlarda"
    return f'''
			<!-- PDF merkezi ic tanitimi (scripts/pdf_tanitim.py) -->
			<div class="pdf-tanitim" id="pdf-tanitim">
				<div class="pdf-tanitim-bas">
					<h3 class="gs-alt-baslik">Ücretsiz konu anlatımı PDF'leri</h3>
					<p>{k(ad)} çıkan konuların anlatımı, hap bilgiler ve çözümlü örneklerle PDF olarak. Her belge sürümlü ve QR kodla doğrulanabilir; tamamen ücretsiz.</p>
				</div>
				<div class="pdf-tanitim-liste">
{kartlar}
				</div>
				<a class="pdf-tanitim-dugme" href="/pdf/{ara}">PDF Merkezi: {toplam} konunun tamamı →</a>
			</div>
'''
