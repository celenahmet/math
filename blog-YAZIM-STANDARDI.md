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
- Formül **görsel olarak** değil, **metin olarak** yazılır: ekran
  okuyucu okur, arama motoru anlar, kopyalanabilir.

## 5. Dil

- Türkçe, sade, öğrenciye "sen" diye hitap eden ama samimiyetsiz olmayan.
- Teknik terim **herkes için** açıklanır: terimi ilk geçtiği yerde bir
  cümleyle tanımla.
- Uzun tire (—) kullanılmaz.
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
