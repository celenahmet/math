# ahmetcelen.com.tr — 22.09.2026 toplu yayın listesi (Ahmet'in sohbetteki tüm istekleri)

Kural: başlık (`<title>`), H1/H3 ve dosya yolları DEĞİŞMEZ · ÖSYM PDF'leri sunucumuzda barındırılmaz, ÖSYM'ye bağlanır · dış bağlantılar yeni sekmede.

- [x] KPSS lisans: 2020-2026 ÖSYM kitapçıkları, kırık 2008/2011 çıktı (d93b7ed)
- [ ] `/ss/kpss-onlisans/` ve `/ss/kpss-ortaogretim/` yeni sayfalar (aynı format; 2018-2024 ÖSYM %10 kitapçıkları; 2026 sınavı 04.10 / 25.10)
- [ ] `/ss/tyt`, `/ss/ayt`: kırık 2019-2021 → resmi 2020-2026 bağlantılar · `/ss/msu`: 2022-2026 eklenir · `/ss/dgs`: kırık 2008-2012, 2018 çıkar; 2026 eklenir (2021-2025 ÖSYM sayfası bulunamadı, aranacak)
- [ ] `/ss/*` tasarım yenileme (tek üretici, tema iskeleti), tüm dış bağlantılar `target=_blank`
- [ ] `/ss/` ana sayfa: Çıkmış Sorular + Sınavlar ve Geri Sayımlar (şu an 404); menü "Sınavlar" → `/ss/`
- [ ] Sitenin kendi 404 sayfası (`404.html`), Vercel'in siyah sayfası değil
- [ ] UniConnectly bloğu (çıkmış sorular + geri sayım sayfalarının altı): somut öğrenci faydası, `?ref=ahmetcelen.com.tr` + UTM, 8 sabit yazı + "En yeniler" 4 (uniconnectly.com/blog-feed.json, CORS)
- [ ] uniconnectly-web: `blog-feed.json` üretimi (build) + CORS başlığı
- [ ] Geri sayım: KPSS Ön Lisans (04.10.2026 10:15) ve KPSS Ortaöğretim (25.10.2026) eklenir (ÖSYM takvimi 22.09'da okundu)
- [ ] IBAN içeren bağlantılar/metinler kaldırılır (`pdfnot/`, `books/problemler/`)
- [ ] Hakkımda içeriği profesyonel metinle yenilenir (Ahmet onayı)
- [ ] `/pdfnot/` içeriği revize
- [ ] Alt bilgi: Vimeo → `https://vimeo.com/search?type=clip&q=ahmet+celen`; YouTube bağlantısı doğrulanır; hepsi yeni sekme
- [ ] 3. seviye menü sığmıyor → iki sütun, üst hizalı (d93b7ed'de gitti; canlıda doğrula)
- [ ] sitemap yeniden üretilir, push, canlı doğrulama, DEVIR_NOTU
