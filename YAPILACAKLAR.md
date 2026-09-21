# ahmetcelen.com.tr — 22.09.2026 toplu yayın listesi (Ahmet'in sohbetteki tüm istekleri)

Kural: başlık (`<title>`), H1/H3 ve dosya yolları DEĞİŞMEZ · ÖSYM PDF'leri sunucumuzda barındırılmaz, ÖSYM'ye bağlanır · dış bağlantılar yeni sekmede.

- [x] KPSS lisans: 2020-2026 ÖSYM kitapçıkları, kırık 2008/2011 çıktı (d93b7ed)
- [x] `/ss/kpss-onlisans/` ve `/ss/kpss-ortaogretim/` yeni sayfalar (aynı format; 2018-2024 ÖSYM %10 kitapçıkları; 2026 sınavı 04.10 / 25.10)
- [x] `/ss/tyt`, `/ss/ayt`: 2020-2026 resmi bağlantılar (2019 bulunamadı) · `/ss/msu`: 2022-2026 · `/ss/dgs`: 2021, 2025, 2026 eklendi; kırık 2008-2012/2018 çıktı · AÇIK: DGS 2022-2024 ve TYT/AYT 2019 ÖSYM sayfası bulunamadı
- [x] `/ss/*` tasarım yenileme (tek üretici, tema iskeleti), tüm dış bağlantılar `target=_blank`
- [x] `/ss/` ana sayfa: Çıkmış Sorular + Sınavlar ve Geri Sayımlar (şu an 404); menü "Sınavlar" → `/ss/`
- [x] Sitenin kendi 404 sayfası (`404.html`), Vercel'in siyah sayfası değil
- [x] UniConnectly bloğu (çıkmış sorular + geri sayım sayfalarının altı): somut öğrenci faydası, `?ref=ahmetcelen.com.tr` + UTM, 8 sabit yazı + "En yeniler" 4 (uniconnectly.com/blog-feed.json, CORS)
- [x] uniconnectly-web: `blog-feed.json` üretimi (build) + CORS başlığı
- [x] Geri sayım: KPSS Ön Lisans (04.10.2026 10:15) ve KPSS Ortaöğretim (25.10.2026) eklenir (ÖSYM takvimi 22.09'da okundu)
- [x] IBAN içeren bağlantılar/metinler kaldırılır (`pdfnot/`, `books/problemler/`)
- [x] Hakkımda içeriği yenilendi (metin taslak: Ahmet göz atsın)
- [x] `/pdfnot/` içeriği revize
- [x] Alt bilgi: Vimeo → `https://vimeo.com/search?type=clip&q=ahmet+celen`; YouTube bağlantısı doğrulanır; hepsi yeni sekme
- [x] 3. seviye menü sığmıyor → iki sütun, üst hizalı (d93b7ed'de gitti; canlıda doğrula)
- [x] sitemap yeniden üretilir, push, canlı doğrulama, DEVIR_NOTU


Yayın: cc80324 (22.09). Canlı doğrulandı: /ss/, 7 çıkmış soru sayfası, 10 geri sayım, 404, pdfnot, hakkımda.
