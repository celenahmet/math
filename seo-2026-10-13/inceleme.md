# SEO incelemesi — 13 Ekim 2026

Canlı denetim: 538 adres, 526 HTTP 200 ve 12 HTTP 404. Bu sayılar düzeltmelerden önceki ölçümdür.

## Uygulanan düzeltmeler

- 19 çıkmış soru ve geri sayım sayfasındaki KPSS canonical/OG/JSON-LD kopyası düzeltildi. Üreticiler artık sayfaya özel metadata üretir.
- Çıkmış soru başlıkları listedeki gerçek yıl aralığını gösterir.
- Karşılığı bulunan eski blog, ders notu ve sınav adreslerine kalıcı HTTP yönlendirmeleri eklendi.
- sitemap-blog.xml: 100 yazı ve blog merkezi. robots.txt üzerinden duyurulur; Search Console’a ayrıca gönderilebilir.
- Sitemap lastmod artık yazının gerçek yayın/güncelleme tarihidir; her üretimde bugün yapılmaz. Noindex ve başka canonical taşıyan sayfalar haritaya alınmaz.
- Eski /yt/ PDF adreslerinin indeks engelini kaldırmak için ana alan adında index, follow yanıt başlığı eklendi; medya alanının davranışı ayrı kalır.

## Raporların anlamı

- 256 noindex URL: 154 belge doğrulama, 97 PDF/indirme, 2 eski blog, 1 eski PDF, 1 ders notu yönlendirmesi, 1 Telegram yönlendirmesi.
- 149 keşfedilmiş URL: 39 blog, 94 video, 11 QR, 2 çıkmış sorular, 1 kitap, 1 parabol, 1 QR alternatifi.
- 39 blogun hepsi canlıda 200, kendi canonical adresi ve index etiketiyle erişilebilir. 1970-01-01 ihracat değeri gerçek yayın/tarama tarihi olarak yorumlanmadı.
- 100 yazının blog iç bağlantılarında eksik yerel hedef bulunmadı.
- 6 eski 403 adresinin tümü güncel denetimde 200 döndü. Eski rapor tek başına bugünkü erişim engelini kanıtlamıyor.

## Search Console’da yapılacaklar

1. Site haritaları alanına https://ahmetcelen.com.tr/sitemap-blog.xml ekle.
2. Blog URL’lerini tek tek göndermek zorunlu değildir. Ana sitemap zaten bütün blog yazılarını içerir; Google sitemap ve HTML iç bağlantılar üzerinden otomatik keşfedebilir. URL Denetimi yalnızca örnek sayfalarda teşhis için kullanılabilir.
3. /ss/tyt/, /ss/ayt/, /ss/msu/ ve /sinavlar/msu/ için kullanıcı canonical adresini ve canlı yanıtı kontrol et; yeniden tarama iste.
4. Son 3 ay Performans raporunun Sayfalar/Sorgular sekmelerini dışa aktar. 22 Eylül dosyası 20 Eylül 2025–20 Eylül 2026 dönemini kapsıyor; yeni blogların etkisini göstermiyor.
5. 7–14 gün sonra blog gösterimleri, taranan URL sayısı ve Google’ın seçtiği canonical adresleri yeniden incele. İndeksleme ve tıklama garanti edilmez.

## İçeriği geri kazanılması gereken eski 404 adresleri

Aşağıdaki konuların eşdeğer güncel yazısı bulunmadığı için alakasız bir sayfaya topluca yönlendirilmedi. Eski WordPress yedeği veya özgün içerik gerekir.

- /blog/index.php/2020/07/10/soygazlar-asalgazlar/
- /blog/index.php/2020/07/28/kaynak-rehberim/
- /blog/index.php/2021/02/24/karmasik-sayilar/
- /blog/index.php/2021/08/06/tyt-mat-deneme/
- /blog/index.php/tag/cemberin-analitigi/
- /blog/index.php/tag/ters-trigonometrik-fonksiyonlarin-turevi/
- /deneme/aytmat/ (eski sayfa yayın kapsamı dışında; özgün hedefi geri kazandırılmalı)

## Öncelikli blog URL listesi

- https://ahmetcelen.com.tr/blog/asal-sayilar-ve-asal-carpanlara-ayirma/
- https://ahmetcelen.com.tr/blog/birim-cember/
- https://ahmetcelen.com.tr/blog/birinci-dereceden-denklemler-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/devirli-ondalik-sayilar-nasil-kesre-cevrilir/
- https://ahmetcelen.com.tr/blog/diskriminant-delta/
- https://ahmetcelen.com.tr/blog/ebob-ve-ekok-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/esitsizlikler-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/faktoriyel-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/hareket-problemleri-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/isci-ve-havuz-problemleri-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/islem-onceligi-nasil-yapilir/
- https://ahmetcelen.com.tr/blog/kar-ve-zarar-problemleri-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/karisim-problemleri-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/kesirler-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/kesirlerde-carpma-ve-bolme/
- https://ahmetcelen.com.tr/blog/kokler-toplami-carpimi/
- https://ahmetcelen.com.tr/blog/koklu-sayilar-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/kumeler-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/mantik-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/olasilik-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/ondalik-gosterim-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/oran-ve-oranti-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/parabol-denklemi/
- https://ahmetcelen.com.tr/blog/parabol-tepe-noktasi/
- https://ahmetcelen.com.tr/blog/permutasyon-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/polinomlar-konu-anlatimi/
- https://ahmetcelen.com.tr/blog/polinomlarda-bolme/
- https://ahmetcelen.com.tr/blog/polinomlarda-carpanlara-ayirma/
- https://ahmetcelen.com.tr/blog/polinomlarda-kalan/
- https://ahmetcelen.com.tr/blog/pozitif-ve-negatif-sayilar/
- https://ahmetcelen.com.tr/blog/rasyonel-sayilar-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/sayi-dogrusu-ve-sayilari-siralama/
- https://ahmetcelen.com.tr/blog/sayi-problemleri-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/tablo-ve-grafik-yorumlama/
- https://ahmetcelen.com.tr/blog/tek-ve-cift-sayilar/
- https://ahmetcelen.com.tr/blog/turevin-tanimi/
- https://ahmetcelen.com.tr/blog/uslu-sayilar-konu-anlatimi-pdf/
- https://ahmetcelen.com.tr/blog/yuzdeler-konu-anlatimi-pdf/

## Canlı yayın doğrulaması

- TYT sayfası canonical ve OG URL olarak kendi adresini döndürüyor.
- Karmaşık Sayılar PDF’si HTTP 200 ve X-Robots-Tag: index, follow döndürüyor.
- Search Console istekleri hesap erişimi olmadığı için gönderilmedi; URL listesi kullanıcı tarafından gönderilmek üzere hazır.
- Eski /blog/logaritma/ adresi 308 ile yeni logaritma yazısına yönleniyor.
- sitemap-blog.xml HTTP 200 application/xml olarak erişilebilir.
