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

# 23.09.2026 — Blog (ahmetcelen.com.tr/blog)

Kurallar: `blog-YAZIM-STANDARDI.md` (11 bölüm) · kaynaklar iç rapor `blog-KAYNAK-DENETIMI.md` (yayında gösterilmez) · kapaklar AVIF (webp medya sunucusuna yönleniyor).

- [x] Kendi modern kabuğu (tema yok, jQuery/Bootstrap yok) · palet kapaktan ölçüldü · AÇ monogram kilidi
- [x] Formüller MathML (`scripts/matematik.py`), sayfaya JS/CSS inmez
- [x] İlk yazı: Fonksiyonlar Konu Anlatımı (2213 kelime, 26 kutu, 6 SSS, 10 madde kontrol listesi)
- [x] Kutular: önce şunları bil (mor) · hap bilgi · dikkat · örnek · sınavda nasıl çıkar; hap bilgi özeti otomatik
- [x] Tıklanabilir kontrol listesi + 10/10 tebrik (localStorage, sunucuya veri gitmez)
- [x] Sağ blok: UniConnectly → Kategoriler (sayılı, boşlar "yakında") → Sınavlar → akıllı okuma konumu (5'li pencere, önceki/sonraki, tüm bölümler, başa dön)
- [x] İçindekiler yazının başında (iki sütun) · kırıntı yolu ikonlu · okuma süresi ikonu
- [x] Hub: Konu + Sınav iki eksenli süzgeç, `/blog/#analiz` `/blog/#sinav-kpss` çapaları
- [x] Blog menüsü (Tüm Yazılar · Konular · Sınavlar · Ders Notları · Ana Site)
- [x] Paylaş: sistem paylaşımı + kopyala + WhatsApp + X + Instagram (Instagram web paylaşımını desteklemiyor → kopyalar)
- [x] Görsel SEO: srcset, og:image:alt/boyut, JSON-LD ImageObject + wordCount + timeRequired
- [x] Stajyer notları: ifade ile açıklama/soru ayrı satırda (21 yer) · standarda bölüm 10
- [x] GÜVENLİK: `scripts/` ve `*.md` yayındaydı (200) → `.vercelignore`, şimdi 404
- [x] Görüntülenme sayacı: `api/goruntulenme.js` canlı, 15 test (adversarial dahil) geçti
- [ ] **Ahmet:** Vercel → math → Storage → Upstash for Redis → projeye bağla → yeniden dağıt. Bağlanana kadar sayaç gizli (503).
- [ ] Sıradaki yazılar: `blog-gorselleri/` 02-50 (brief'teki konu sırası)
- [ ] Boş durum ve arayüz metinleri (tebrik, "Bu yazıyı paylaş") Ahmet onayı bekliyor
