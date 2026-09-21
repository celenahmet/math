#!/usr/bin/env python3
# scripts/hata_sayfasi.py — sitenin kendi 404 sayfasini (404.html) ana
# temanin iskeletiyle uretir. Vercel statik dagitimda kok dizindeki
# 404.html'i 404 durum koduyla sunar; boylece Vercel'in siyah "This page
# doesn't exist" sayfasi gorunmez (Ahmet, 22.09).
# Kullanim: python3 scripts/hata_sayfasi.py  (menu/alt bilgi degisince koş)
import re, pathlib
KOK = pathlib.Path(__file__).resolve().parent.parent
ISKELET = (KOK / "ss/kpss/index.html").read_text(encoding="utf-8")
BAS = ISKELET[:ISKELET.index("\t<!-- Inner Page Breadcrumb -->")]
SON = ISKELET[ISKELET.index('\t<section class="footer_one">'):]
SON = re.sub(r'\n<script src="/js/uniconnectly-blok\.js[^"]*"></script>', "", SON)
bas = re.sub(r"<title>.*?</title>", "<title>Sayfa bulunamadı - Ahmet Çelen</title>", BAS, count=1, flags=re.S)
bas = re.sub(r'<meta name="keywords" content="[^"]*">', "", bas, count=1)
bas = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="robots" content="noindex, follow">', bas, count=1)
bas = bas.replace('<html dir="ltr" lang="en">', '<html dir="ltr" lang="tr">')
govde = '''
	<section class="inner_page_breadcrumb">
		<div class="container">
			<div class="row">
				<div class="col-xl-6 offset-xl-3 text-center">
					<div class="breadcrumb_content">
						<h4 class="breadcrumb_title">404</h4>
						<ol class="breadcrumb">
						    <li class="breadcrumb-item"><a href="/">Ana Sayfa</a></li>
						    <li class="breadcrumb-item active" aria-current="page">Sayfa bulunamadı</li>
						</ol>
					</div>
				</div>
			</div>
		</div>
	</section>
	<section class="cs-sayfa">
		<div class="container">
			<div class="main-title text-center">
				<h3 class="mt0">Aradığın sayfa burada değil</h3>
				<p>Adres taşınmış ya da hiç var olmamış olabilir. Aşağıdan devam edebilirsin.</p>
			</div>
			<div class="cs-diger" style="max-width:900px;margin:0 auto">
				<a href="/">Ana Sayfa<span>Ders notları ve videolar</span></a>
				<a href="/ss/">Çıkmış Sorular<span>TYT, AYT, MSÜ, DGS, KPSS</span></a>
				<a href="/sinavlar/">Sınav Geri Sayımları<span>ÖSYM takvimi</span></a>
				<a href="/pdfnot/">Ders Notları (PDF)<span>Deneme ve fasiküller</span></a>
			</div>
		</div>
	</section>
'''
(KOK / "404.html").write_text(bas + govde + SON, encoding="utf-8")
print("404.html yazildi")
