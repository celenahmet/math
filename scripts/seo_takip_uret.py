"""Create reviewable URL inspection lists from the audited exports."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
audit = json.loads((ROOT / 'scripts/seo-audit-2026-10-13.json').read_text())
out = ROOT / 'seo-2026-10-13'
out.mkdir(exist_ok=True)
export = next(v for k, v in audit['exports'].items() if 'Validation' in k)
urls = [row[0] for row in export['rows'] if '/blog/' in row[0]]
(out / 'blog-dizine-ekleme-adresleri.txt').write_text('\n'.join(urls) + '\n')
lines = ['# SEO incelemesi — 13 Ekim 2026', '',
         'Canlı denetim: 538 adres, 526 HTTP 200 ve 12 HTTP 404. Bu sayılar düzeltmelerden önceki ölçümdür.', '',
         '## Uygulanan düzeltmeler', '',
         '- 19 çıkmış soru ve geri sayım sayfasındaki KPSS canonical/OG/JSON-LD kopyası düzeltildi. Üreticiler artık sayfaya özel metadata üretir.',
         '- Çıkmış soru başlıkları listedeki gerçek yıl aralığını gösterir.',
         '- Karşılığı bulunan eski blog, ders notu ve sınav adreslerine kalıcı HTTP yönlendirmeleri eklendi.',
         '- sitemap-blog.xml: 100 yazı ve blog merkezi. robots.txt üzerinden duyurulur; Search Console’a ayrıca gönderilebilir.',
         '- Sitemap lastmod artık yazının gerçek yayın/güncelleme tarihidir; her üretimde bugün yapılmaz. Noindex ve başka canonical taşıyan sayfalar haritaya alınmaz.',
         '- Eski /yt/ PDF adreslerinin indeks engelini kaldırmak için ana alan adında index, follow yanıt başlığı eklendi; medya alanının davranışı ayrı kalır.', '',
         '## Raporların anlamı', '',
         '- 256 noindex URL: 154 belge doğrulama, 97 PDF/indirme, 2 eski blog, 1 eski PDF, 1 ders notu yönlendirmesi, 1 Telegram yönlendirmesi.',
         '- 149 keşfedilmiş URL: 39 blog, 94 video, 11 QR, 2 çıkmış sorular, 1 kitap, 1 parabol, 1 QR alternatifi.',
         '- 39 blogun hepsi canlıda 200, kendi canonical adresi ve index etiketiyle erişilebilir. 1970-01-01 ihracat değeri gerçek yayın/tarama tarihi olarak yorumlanmadı.',
         '- 100 yazının blog iç bağlantılarında eksik yerel hedef bulunmadı.',
         '- 6 eski 403 adresinin tümü güncel denetimde 200 döndü. Eski rapor tek başına bugünkü erişim engelini kanıtlamıyor.', '',
         '## Search Console’da yapılacaklar', '',
         '1. Site haritaları alanına https://ahmetcelen.com.tr/sitemap-blog.xml ekle.',
         '2. Aşağıdaki bloglar için URL Denetimi → Canlı URL’yi test et → Dizine eklenmesini iste. Günlük kota çıkarsa kalanları sonraki günlerde gönder.',
         '3. /ss/tyt/, /ss/ayt/, /ss/msu/ ve /sinavlar/msu/ için kullanıcı canonical adresini ve canlı yanıtı kontrol et; yeniden tarama iste.',
         '4. Son 3 ay Performans raporunun Sayfalar/Sorgular sekmelerini dışa aktar. 22 Eylül dosyası 20 Eylül 2025–20 Eylül 2026 dönemini kapsıyor; yeni blogların etkisini göstermiyor.',
         '5. 7–14 gün sonra blog gösterimleri, taranan URL sayısı ve Google’ın seçtiği canonical adresleri yeniden incele. İndeksleme ve tıklama garanti edilmez.', '',
         '## İçeriği geri kazanılması gereken eski 404 adresleri', '',
         'Aşağıdaki konuların eşdeğer güncel yazısı bulunmadığı için alakasız bir sayfaya topluca yönlendirilmedi. Eski WordPress yedeği veya özgün içerik gerekir.', '',
         '- /blog/index.php/2020/07/10/soygazlar-asalgazlar/',
         '- /blog/index.php/2020/07/28/kaynak-rehberim/',
         '- /blog/index.php/2021/02/24/karmasik-sayilar/',
         '- /blog/index.php/2021/08/06/tyt-mat-deneme/',
         '- /blog/index.php/tag/cemberin-analitigi/',
         '- /blog/index.php/tag/ters-trigonometrik-fonksiyonlarin-turevi/',
         '- /deneme/aytmat/ (eski sayfa yayın kapsamı dışında; özgün hedefi geri kazandırılmalı)', '',
         '## Öncelikli blog URL listesi', '']
lines += [f'- {url}' for url in urls]
(out / 'inceleme.md').write_text('\n'.join(lines) + '\n')
print(out)
