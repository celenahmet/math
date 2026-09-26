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
- [ ] **Ahmet:** Vercel → math → Storage → Upstash for Redis (ücretsiz, bölge Frankfurt) → projeye bağla (Production) → yeniden dağıt. Bağlanana kadar sayaç, popüler sekmesi ve yazı sonu etkileşimi (faydalı mı, ifade, yorum) gizli (503). **Tek bağlantı üçünü birden açar.**
- [x] 02-05 yazıldı (23.09): Tanım, Değer ve Görüntü Kümeleri (3439 kelime) · Birebir ve Örten Fonksiyon Nedir? (2122) · Bileşke Fonksiyon Konu Anlatımı (2015) · Ters Fonksiyon Nasıl Bulunur? (2007). Kapaklar: 03 ve 04 için `-v2` (01 de v2 idi, piksel karşılaştırmasıyla ölçüldü)
- [x] `scripts/blog_dogrula.py`: 261 matematiksel ve biçim denetimi, hepsi tuttu (sympy `.venv`'de)
- [x] `matematik.py`: `{1,2,3}` ve `[2,5)` içindeki virgül ondalık sanılıyordu; işaret eksisi `{ − 1` diye aralıklı basılıyordu. İkisi düzeldi, 01 de yeniden üretildi
- [x] Sağ blok: UniConnectly kartının altına 3 mağaza rozeti (App Store, Google Play, AppGallery; adresler `uniconnectly_blok.MAGAZALAR`)
- [x] Sağ blok: "En popüler / En yeni" (5 yazı). Popüler sırası `api/populer.js` (salt okuma, MGET, CDN 5 dk, 12 test `scripts/api_populer_test.js`). **Upstash bağlanana kadar popüler sekmesi gizli**, yalnız "En yeni" görünür
- [x] Hub kartları kapaklı (ilk kart geniş ekranda yatay öne çıkan), "Bunlar da ilgini çekebilir" kartları kapaklı
- [x] 24.09: 51-55 yazıldı (Temel Kavramlar ve Sayılar kategorisi; hepsi ≥ 2000 kelime, `blog_dogrula.py` 12932 denetim tuttu). PDF başlıklı yazılarda PDF şimdilik YOK (Ahmet'in kararı)
- [x] 24.09 SEO: yazı başlıklarında "Ahmet Çelen" yok (hub hariç, 01-05 dahil); kapaklar görsel site haritasında; ImageObject name = konu; altbilgi logosu alt=""
- [x] Sağ blok "Popüler / En yeni": solda küçük kapak (-240.avif), sağda başlık + tarih
- [x] 24.09: 56-60 yazıldı ve yayında (tek-çift, pozitif-negatif, ardışık, sayı doğrusu, mutlak değer; hepsi ≥ 2000 kelime, `blog_dogrula.py` toplam 13061 denetim tuttu)
- [x] 24.09: 61-65 yayında (üslü, köklü, işlem önceliği, bölünebilme, asal); 51-60 metinlerinden sınav sıklık iddiaları temizlendi; `blog_dogrula.py` 13193 denetim tuttu
- [x] 24.09: 66-70 yayında (EBOB-EKOK, kesirler, sıralama, toplama-çıkarma, çarpma-bölme); `scripts/ek_denetimi.py` eklendi (formül sonrası ek, okunuşa göre), 01-70 arasında 83 yanlış ek düzeltildi; 13329 denetim
- [x] 24.09: 71-75 yayında (ondalık gösterim, devirli ondalık, yüzdeler, oran-orantı, doğru-ters orantı); `yazi_71_75` 13445 denetim
- [x] 24.09: 76-80 yayında (cebirsel ifadeler, 1. derece denklemler, eşitsizlikler, denklem kurma, sayı problemleri); `yazi_76_80` 13539 denetim. Ahmet'in kategori kararı: Temel Cebir (76-79), Problemler (80-89), Sayma ve Olasılık (92-95), Kümeler ve Mantık (96-97), Veri ve Grafik (98-99); `blog_veri.KATEGORILER` + `blog_ikon`
- [x] 06-50 TAMAM (Ahmet 25.09: "math da yazılmayan blogları yazalım"). 25.09: 06-10 yayında (fonksiyon grafikleri, polinomlar, bölme, kalan, çarpanlara ayırma; `yazi_06_10` 14378 denetim; `blog_ogeler.koordinat_grafik` koordinat düzleminde SVG fonksiyon grafiği). 25.09: 11-13 yayında (ikinci dereceden denklemler, diskriminant, kökler toplamı ve çarpımı; `yazi_11_13`, toplam 14452 denetim; `blog_uygula` yayında olmayan yazıya giden iç bağlantıyı düz metin basıyor ve build'de ! satırıyla yazıyor). 25.09: 14-18 yayında (parabol, tepe noktası, parabol denklemi, parabol grafiği, parabol ve doğru; `yazi_14_18`, toplam 14567 denetim). 25.09: 19-23 yayında (trigonometri, birim çember, trigonometrik oranlar, özdeşlikler ve formüller, trigonometrik fonksiyon grafikleri; `yazi_19_23`, toplam 14923 denetim; trig sabitleri sympy'de kendiliğinden sadeleşmediği için `yazi_19_23` içindeki `es()` öğe öğe simplify + 60 basamak sayısal karşılaştırıyor; `periodicity()` en küçük periyodu garanti etmiyor, sin² için 2π dönüyor, esas periyot ayrıca gösteriliyor). 25.09: 24-26 yayında (toplam ve fark, iki kat ve yarım açı, trigonometrik denklemler; `yazi_24_26`, toplam 15104 denetim; `esit_ogeler` artık modül düzeyinde ortak). Not: 24-50 kapakları 24.09'dan beri `blog-gorselleri/` içinde (47-49 için `-logo-v2` sürümü kullanılır); "kapak yok" notu yanlıştı. 25.09: 27-29 yayında (logaritma, logaritma kuralları, logaritmik denklemler; `yazi_27_29`, toplam 15307 denetim; doğrulayıcı 28'de 0.8451/0.3010 için yazılan 2.807 yuvarlamasını yakaladı, 2.81 yapıldı). 25.09: 30-32 yayında (diziler, aritmetik dizi, geometrik dizi; `yazi_30_32`, toplam 15614 denetim). 25.09: 33-36 yayında (limit, sağdan ve soldan limit, limitte belirsizlikler, süreklilik; `yazi_33_36`, toplam 15808 denetim; sympy `limit(f, x, a, '-')` Piecewise ve floor'da noktadaki değeri döndürüyor, tek yönlü limit x = a ∓ e ile hesaplanıyor; `matematik.py`'ye \lfloor \rfloor \lceil \rceil eklendi; 33, 35, 36 dan /blog/turevin-tanimi/ bağlantısı 38 yayına girince kendiliğinden açılır). 25.09: 37-39 yayında (türev, türevin tanımı, türev alma kuralları; `yazi_37_39`, toplam 15980 denetim; 37 ve 39 dan 40-45 e giden bağlantılar o yazılar yayına girince açılır). 25.09: 40-42 yayında (çarpımın türevi, bölümün türevi, zincir kuralı; `yazi_40_42`, toplam 16120 denetim). 25.09: 43-45 yayında (teğet denklemi, artan ve azalan, maksimum ve minimum; `yazi_43_45`, toplam 16286 denetim; türev serisi 37-45 tamam). 25.09: 46-50 yayında (integral konu anlatımı, belirsiz integral, belirli integral, değişken değiştirme, integral ile alan; `yazi_46_50`, toplam 16506 denetim). 06-100 SERİSİ TAMAM, 100 yazı yayında. 51-100 TAMAM. 25.09: 98-100 yayında (tablo ve grafik yorumlama, aritmetik ortalama ve veri analizi, genel tekrar; `yazi_98_100` 14266 denetim; `blog_ogeler` sutun/cizgi/daire_grafik satır içi SVG, JS yok, etiketler kelime sayısına girmez; `blog_veri` dosyaları sayısal sıralıyor, 100_ artık 51_ den önce gelmiyor). 25.09: 92-97 yayında (faktöriyel, permütasyon, kombinasyon, olasılık, kümeler, mantık; `yazi_92_97` 14198 denetim; `matematik.py`'ye \wedge \vee \veebar eklendi; `tablo()` başlığı artık tırnak kaçırmıyor, `$p'$` başlıkta bozuluyordu). 25.09: 86-91 yayında (oran-orantı, işçi-havuz, hareket, karışım problemleri, sayı basamakları, basamak değeri; 13760 denetim; 90-91 kategori: sayilar). 25.09: 81-85 yayında (kesir, yaş, yüzde, kâr-zarar, faiz problemleri; 13640 denetim). Not: `matematik.py` \quad / \qquad tanımıyor; sympy `solveset(|x-2| > -1)` yanlışlıkla boş küme veriyor (tümleyenle denetle)
- [x] (eski) Sıradaki yazılar: `blog-gorselleri/` 06-50 (brief'teki konu sırası); her yazının iddiaları `blog_dogrula.py`'ye eklenir
- [ ] Boş durum ve arayüz metinleri (tebrik, "Bu yazıyı paylaş") Ahmet onayı bekliyor
- [x] 25.09 hub süzgeci: `.bs-kart{display:flex}` tarayıcının `[hidden]` kuralını eziyordu, kartlar gizlenmiyordu (Ahmet: "kategorilendirme çalışmıyor") → `.bs-kart[hidden]{display:none!important}`. "Dengesiz yerleşme": `.bs-hero` kapın yan boşluğunu sıfırlıyordu (başlık süzgeçten 20px solda, 1180px altında kenara yapışık) + süzgeç düğmeleri 6/6/1 → satır içi dengeleme betiği (5/4/4, ilk boyamadan önce, CLS yok) + öne çıkan kart görseli soldan hizalı (kapak yazısı kırpılmıyor). Boş sonuç satırı eklendi (metin varsayılan).
- [x] 25.09 yazı sonu etkileşimi (Ahmet: faydalı mı + gerçek sayı, "hayır"da mesaj, 5 ifade, onaylı yorum, üst düzey spam koruması). `api/etkilesim.js` + `api/yonetim.js` + ortak `api/_etkilesim.js`, ifade listesi tek kaynak `api/_ifadeler.json`, istemci `js/etkilesim.js`, yönetim sayfası `/yonetim/` (noindex, site haritası ve arama dışı). Spam: iş kanıtı (imzalı, 10 dk, tek kullanımlık) + HMAC imzalı HttpOnly çerez + aynı ağdan yazı başına günde 5 yeni oy + genel/yorum/mesaj hız sınırları + kuyruk tavanları; oy atomik (Redis Lua). IP saklanmaz (günlük değişen HMAC özeti, ≤24 sa). 36 test gerçek Redis'e karşı (`scripts/api_etkilesim_test.js`, SRH vekili) + tarayıcıda uçtan uca (CDP). Vercel ortamı: `ETKILESIM_GIZLI`, `YONETIM_ANAHTARI` eklendi; anahtarın kopyası `~/.ahmetcelen_yonetim_anahtari` (600). Önbellek yalnız Vercel CDN'de (`Vercel-CDN-Cache-Control`); tarayıcıya stale-while-revalidate verilince onaylı yorum yenilemede çıkmıyordu.
- [ ] **Ahmet:** yazı sonu metinleri varsayılan: "Evet/Hayır", "Neyi eksik buldun?", "Henüz yorum yok.", form notu, `js/etkilesim.js` başındaki `METIN` (sınır, hata, gönderildi). İfade seti (❤️ 💡 🤯 🤔 😅) `api/_ifadeler.json`'da; yayına girip sayı birikmeden değişmeli (anahtar değişirse sayılar kaybolur). Hub'daki "Bu seçimde henüz yazı yok." de varsayılan.
- [x] 26.09 hap bilgi kuralı (Ahmet: "her yazıda en az 5 tane", gündelik hayatla bir iki tane istenir): 100 yazının hepsi ≥5 hap, her birinde 1 gündelik hayat hapı (`hap(..., gunluk=True)`, "Gündelik hayatta" etiketi). Eklenen her sayısal iddia `hap_ekleri()` altında doğrulandı (509 iddia). `bicim()` artık 5'in altını kırmızıya düşürüyor; kural `blog-YAZIM-STANDARDI.md`'de.
