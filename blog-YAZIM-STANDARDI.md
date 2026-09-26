# Blog yazım standardı — ahmetcelen.com.tr/blog

Ahmet (23.09.2026): *"blogların yazma standartı olacak, matematiksel hata
olmayacak ve uzun olacak detaylı. hap bilgiler gibi böyle yenilikçi,
öğrenci yararına yapabilirsin."*

## 1. Matematiksel doğruluk — pazarlığa kapalı

- Her tanım, teorem ve formül yayımlanmadan önce **tek tek** doğrulanır.
- Bir ifade "genelde doğru" ise, hangi koşulda bozulduğu **yazılır**.
  Örnek: ters fonksiyon her fonksiyonda yoktur; birebir **ve** örten şart.
- Sayısal örneklerin sonucu hesaplanarak kontrol edilir; "yaklaşık şöyle"
  diye geçilmez.
- Sınav formatına ait bir iddia (soru sayısı, konu dağılımı) **ÖSYM'nin
  kendi belgesine** dayanır; kulaktan dolma dağılım yazılmaz.
- Emin olunmayan bilgi yazılmaz. Eksik bırakmak, yanlış yazmaktan iyidir.
- **Makine doğrulaması zorunlu** (Ahmet 23.09: *"matematiksel hata yapmayalım, kaynakta
  matematiksel olarak doğrulayalım"*). Yazıdaki her tanım/görüntü kümesi, ters fonksiyon,
  bileşke ve sayma sonucu `scripts/blog_dogrula.py` içinde bir satırdır: sympy ile sembolik ya
  da kaba kuvvetle (bütün fonksiyonlar tek tek sayılarak) yeniden hesaplanır. Yayından önce
  `.venv/bin/python scripts/blog_dogrula.py` çalışır; tek satır tutmazsa yayın yapılmaz.
  Betik biçimi de denetler: ≥ 2000 kelime, 10 kontrol maddesi, uzun tire yok, formül dışında ünlem yok.
- Sınav düzeyi anlatılırken **sıklık iddiası** ("çoğunlukla", "en çok", "sık sorulan") yazılmaz;
  ÖSYM dağılım yayımlamıyor. "Şu biçimde karşına çıkabilir" denir.

## 2. Uzunluk ve derinlik

- Konu **baştan sona** anlatılır: tanım → özel durumlar → işlemler →
  grafik → sınav → hata → özet. Yarım bırakılmaz.
- Hedef uzunluk: ana konu yazısı **en az 2000 kelime**. Kısa yazı, arama
  sonucunda da öğrenci gözünde de zayıf kalır.
- Her yeni kavram **önce sözle**, sonra **formülle**, sonra **örnekle**
  verilir. Üçü birden olmadan bölüm bitmez.

## 3. Öğrenci yararına kutular

| Kutu | Ne zaman |
|---|---|
| **Önce şunları bil** | Yazının başında; ön koşul konular |
| **Hap bilgi** | Ezberlenecek kural, formül, kısayol |
| **Dikkat** | Sınavda tuzak olan, sık yapılan hata |
| **Örnek** | Adım adım çözümlü örnek |
| **Sınavda nasıl çıkar** | TYT / AYT / ALES / KPSS ayrımı |
| **Kontrol listesi** | Yazının sonunda; öğrenci kendini sınar |

Kutu süs değildir: her biri gerçekten o işlevi görmeli. Bölüm başına
en fazla bir-iki kutu; sayfa kutu tarlasına dönmez.

### Hap bilgi özeti (zorunlu)

Sayfanın sonunda, kontrol listesinin hemen üstünde **"Hap bilgi özeti"**
bölümü bulunur. Bu bölüm **elle yazılmaz**: yazının içindeki bütün hap
bilgiler üretici tarafından toplanıp numaralı listeye dizilir.

Sonucu şudur: öğrenci yazıyı bitirdiğinde ya da sınavdan önce geri
döndüğünde, tüm konunun ezberlenecek kısmını tek ekranda görür.

Bu, hap bilgilerin yazıya **anlamlı dağıtılmasını** zorunlu kılar. Bir
bölümde hiç hap bilgi yoksa özet eksik kalır; on tane üst üste konursa
özet okunmaz olur. Her ana bölümde bir tane, en fazla iki tane.

**Sayı kuralı (26.09.2026, Ahmet):** her yazıda **en az 5** hap bilgi
bulunur. `blog_dogrula.py` içindeki `bicim()` bunu denetler; 5'in altı
derlemeyi kırmızıya düşürür. Beşi aynı bölüme yığılmaz, konunun farklı
bölümlerine dağıtılır.

**Gündelik hayat hapı (istenir, zorunlu değil):** yazıda bir iki tane hap,
konuyu gündelik bir durumla bağlar (market indirimi, taksi ücreti, tarif,
şifre sayısı gibi). `hap(..., gunluk=True)` ile yazılır, kutuda
"Gündelik hayatta" etiketiyle görünür. Sayılar gerçekçi ama **uydurma
gerçek bilgi** değil: kur, fiyat, nüfus gibi dış veriye dayanan iddia
yazılmaz; "tanesi 10 liradan" gibi varsayım olduğu belli örnek kullanılır.
Her sayısal iddia `hap_ekleri()` altında sympy ile doğrulanır.

⚠️ Hap bilgi kutusunun içine **tablo konmaz**; özet çıkarımını bozar.

### Kontrol listesi (zorunlu)

Yazının en sonunda, öğrencinin işaretleyebileceği bir kontrol listesi
bulunur. Maddeler "biliyorum" değil **"yapabiliyorum"** diliyle yazılır:
öğrenci kendini sınasın, kendine güven vermesin.

İşaretler yalnızca öğrencinin tarayıcısında saklanır; sunucuya hiçbir
şey gitmez, hesap istenmez.

### Paylaş alanı

Yazının sonunda paylaş alanı otomatik gelir. Üçüncü taraf paylaşım
betiği yüklenmez; tarayıcının kendi paylaşım penceresi kullanılır,
yoksa bağlantı panoya kopyalanır.

## 4. Formüller

- LaTeX alt kümesiyle yazılır (`$...$` satır içi, `$$...$$` blok),
  `scripts/matematik.py` MathML'e çevirir. Sayfaya JS/CSS inmez.
- **Ondalık sayı kaynakta NOKTA ile** yazılır (`2.5`), ekrana virgülle basılır (2,5).
  Virgül her zaman ayraçtır: `\{1,2,3\}`, `[2,5)`. (23.09'a kadar `1,2` ve `[2,5)` tek bir
  ondalık sayı gibi basılıyordu; `matematik.py` düzeltildi.)
- Formül **görsel olarak** değil, **metin olarak** yazılır: ekran
  okuyucu okur, arama motoru anlar, kopyalanabilir.

## 5. Dil

- Türkçe, sade, öğrenciye "sen" diye hitap eden ama samimiyetsiz olmayan.
- Teknik terim **herkes için** açıklanır: terimi ilk geçtiği yerde bir
  cümleyle tanımla.
- Uzun tire (—) kullanılmaz.
- **Formülden sonraki ek, formülün okunuşuna uyar** (24.09): ek ayrı yazılır (`$x$ in`) ve okunuşun son
  kelimesine göre seçilir. Kesir "paydada pay" okunur, son kelime PAYDIR: `$\dfrac{2}{5}$ nin` (beşte ikinin),
  `$\dfrac{1}{4}$ i` (dörtte biri), `$\dfrac{3}{8}$ tür` (sekizde üçtür). `scripts/ek_denetimi.py` bunu
  `blog_dogrula.py` içinde denetler; "de/da" bağlacı, "ya da" ve "su" bilinçli olarak dışarıda.
- İç mimariden (RPC, migration, dosya adı) ekranda söz edilmez.

## 6. Kaynaklar ve telif

**Kaynaklar yayımlanan sayfada GÖSTERİLMEZ** (Ahmet, 23.09). Yazı
verisinde tutulur ve `scripts/blog_kaynak_denetimi.py` ile iç rapora
yazılır: bir bilgi sorgulanırsa nereden geldiğini gösterebilelim.

- Kayda geçen kaynak **yalnız resmî** olur: MEB, ÖSYM, YÖK.
- Üçüncü taraf blog/haber atfı YOK.
- İç bağlantılar "Bunlar da ilgini çekebilir" bölümünde.

### Soru kullanımı — yasak

- Yazılarda **başka bir kurumun sorusu kullanılmaz.** MEB, ÖSYM ya da
  yayınevi sorularının metni alınmaz, uyarlanmaz.
- Bütün örnekler **özgün** yazılır.
- Kaynak yalnız tanım, kazanım ve müfredat çerçevesi için kullanılır;
  oradan da metin kopyalanmaz.
- ÖSYM belgeleri siteye yüklenmez, yalnız bağlantı verilir.

## 7. Değişmezler

- Yayımlanan `slug`, `<title>` ve `<h1>` **değiştirilmez**; arama
  birikimi oradan gelir. Düzeltme gerekiyorsa gövdeye yapılır.
- Güncelleme yapılınca `guncelleme` alanı doldurulur.

## 8. Arayüz metni üslubu

Ahmet (23.09): *"paylaş kısmını da 'bu yazı işine yaradıysa' yazmak
yerine daha uygun üslup tercih edelim."*

Sayfadaki düğme, başlık ve kısa açıklamalar **yalvarmaz, pazarlamaz**.

| Kaçın | Yerine |
|---|---|
| "Bu yazı işine yaradıysa paylaş" | "Bu yazıyı paylaş" |
| "Beğendiyseniz lütfen paylaşın" | "Paylaş" |
| "Harika bir kaynak!" | (hiç yazma) |
| "Hemen keşfet!" | "Keşfet" |

Kurallar:

- **Okurun yararını varsayma.** "İşine yaradıysa", "faydalandıysan" gibi
  ifadeler okura bir borç yükler.
- **Düz emir kipi yeter.** "Paylaş", "İndir", "Keşfet".
- **Ünlem yok.** Heyecanı metin değil içerik taşır.
- **Abartı sıfat yok.** "Harika", "muhteşem", "en iyi" yazılmaz.
- Uzun tire (—) kullanılmaz.

⚠️ Okura dönük metnin son hâli **Ahmet'in kararıdır**. Ajan varsayılan bir
metin koyar ve bunu açıkça söyler; Ahmet değiştirir.

## 9. Görsel ve SEO standardı

Ahmet (23.09): *"blog görselleri ve SEO anlamında kusursuz olmalı,
100 puan vermeli, görsellerde arama odaklı olmalı, alt etiketler vs her
şeyiyle birlikte."*

### Kapak görseli

| Kural | Değer |
|---|---|
| Biçim | **AVIF** |
| Ölçü | 1600 px (ana) + 800 px (dar ekran) |
| Dosya adı | Yazının slug'ı; `fonksiyonlar-konu-anlatimi.avif` |
| `srcset` + `sizes` | Zorunlu |
| `width` / `height` | Zorunlu (yerleşim kayması olmasın) |
| `fetchpriority` | Kapakta `high`, diğerlerinde `loading="lazy"` |

⚠️ **WebP kullanılmaz.** `vercel.json` `.webp` uzantısını medya sunucusuna
yönlendiriyor; depoya konan webp siteden servis edilmez. `.avif` o listede
değil (bkz. `scripts/blog_gorsel.py`).

### Alt metin

- Alt metin görselde **ne olduğunu** anlatır; anahtar kelime yığını değil.
- Konunun adı doğal biçimde geçer.
- Örnek: *"Fonksiyonlar konu anlatımı: giriş değerlerini çıkış değerlerine
  bağlayan eşleme şeması ve bir fonksiyon grafiği"*
- Süs görselinin alt metni **boş** bırakılır (`alt=""`), uydurma metin
  yazılmaz.

### Başlıkta ve görselde kişi adı yok (Ahmet, 24.09)

*"Ahmet Çelen yazınca çıkmasın; başlıklarda da Ahmet Çelen yazmasın, blog ana sayfası hariç.
Resim alt etiketleri de önemli, tüm yazılarda."* Blog bir portfolyo değil; alan adı zaten
ad aramasında öne çıkıyor. Blog görselleri **konu aramasında** çıkmalı.

- Yazı `<title>`, `og:title`, `twitter:title`: **yalnız konu başlığı** (" - Ahmet Çelen" eki yok).
  Tek istisna blog ana sayfası. 01-05'te ek yayından kaldırıldı (Ahmet'in açık kararı, "yayındaki
  title değişmez" kuralına bilinçli istisna).
- Açıklama, alt metin, JSON-LD `ImageObject` (`name`, `caption`) ve dosya adı: konu; kişi adı yok.
- Kapaklar görsel site haritasında (`image:loc`) kendi yazısına bağlı.
- Kişi adı yalnız yazar bilgisinde (JSON-LD `author`) ve site logosunda kalır.

### Sayfa başına zorunlu SEO

- Tek `<h1>`, bölümler `<h2>`
- `lang="tr"`, canonical, `meta description` (≤ 160 karakter)
- `og:title`, `og:description`, `og:image`, **`og:image:alt`**,
  `og:image:width`, `og:image:height`
- JSON-LD: `BlogPosting` (görsel **ImageObject** olarak; `wordCount`,
  `timeRequired`, `articleSection`, `keywords`), `BreadcrumbList`,
  soru varsa `FAQPage`
- Formüller MathML, yani **metin**: arama motoru okuyor
- Metinsiz bağlantı bırakılmaz; ikon bağlantısına `aria-label`

## 10. İfade ile açıklama ayrı satırda

Stajyer geri bildirimi (23.09), Ahmet onayladı: *"blog kısmını bu şekilde
revizeleri uyguladıktan sonra bitiriyoruz; bu formatta yazacağız."*

Bir kutunun içinde **veri / ifade / kural** ile **yorum / açıklama / soru**
aynı cümlede birleştirilmez. Her biri kendi satırında (kendi paragrafında)
durur. Göz önce veriyi, sonra ne yapılacağını ayrı ayrı görür.

| Yanlış | Doğru |
|---|---|
| "$s(A)=3$ ve $s(B)=4$ olsun. $A$ dan $B$ ye kaç fonksiyon tanımlanabilir?" | "$s(A)=3$ ve $s(B)=4$ olsun." ↵ "$A$ dan $B$ ye kaç fonksiyon tanımlanabilir?" |
| "Dikey doğru testi: fonksiyon mu? Yatay doğru testi: birebir mi? İkisini karıştırma." | "Dikey doğru testi: fonksiyon mu?" ↵ "Yatay doğru testi: birebir mi?" ↵ "İkisini karıştırma." |
| "Kök içi için $\geq 0$ yazılır. Bu ikisi sık karıştırılır." | "Kök içi için $\geq 0$ yazılır." ↵ "Bu ikisi sık karıştırılır." |

Uygulama: kutu yardımcıları (`hap`, `ornek`, `dikkat`, `onkosul`,
`sinavda`) her argümanı ayrı paragraf yapar. **Veri bir argüman, soru
ya da yorum ayrı argüman.**

Örnek kutusunda sıra her zaman: **verilenler → soru → çözüm adımları.**

### Dil düzeltmesi

"Bu yazıyı rahat okumak için" değil, **"Bu yazıyı daha rahat anlamak
için"**: amaç okumak değil anlamak.

## 11. Kontrol listesi tamamlanınca

On maddenin hepsi işaretlenince listenin altında yeşil bir tebrik satırı
çıkar: *"Tebrikler, bu konunun kontrol listesini tamamladın."* (metin
varsayılan; son hâli Ahmet'in).
