# scripts/yazilar/86_oran_oranti_problemleri.py — Oran ve Oranti Problemleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "oran-ve-oranti-problemleri",
    "baslik": "Oran ve Orantı Problemleri",
    "aciklama": "Oran ve orantı problemleri nasıl çözülür? k yöntemi, paylaştırma, ters orantılı paylaşım, birleşik oran, değişen oran, ölçek, tarif ve hız soruları; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "oran-ve-oranti-problemleri",
    "kapak_alt": "Oran ve orantı problemleri: farklı sayıda mavi ve kırmızı küplerle ölçekli kuleler kuran iki öğrenci",
    "ozet": "Oran ve orantı problemleri, büyüklükler arasındaki ilişkinin bir oranla verildiği sorulardır. Bu soruların neredeyse tamamı tek bir fikirle çözülür: oranda yer alan her büyüklük ortak bir sayının katı olarak yazılır ve sorudaki ikinci bilgi bu ortak sayıyı verir. Bu yazıda k yöntemini, paylaştırma ve ters orantılı paylaştırmayı, birleşik oranları, değişen oranları, ölçek, tarif ve hız sorularını, çalışma hızlarının oranını ve orantı özellikleriyle hızlı çözümü çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Oran problemlerinin ortak anahtarı: k yöntemi", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için oranı, orantıyı ve içler dışlar çarpımını biliyor olman yeterli.",
                "Temeller için <a href=\"/blog/oran-ve-oranti-konu-anlatimi-pdf/\">Oran ve Orantı Konu Anlatımı PDF</a> ve <a href=\"/blog/dogru-oranti-ve-ters-oranti/\">Doğru Orantı ve Ters Orantı</a> yazılarına göz at."),
            "İki ya da daha fazla büyüklüğün oranı verildiğinde, bu büyüklüklerin kendisi değil yalnızca birbirine göre büyüklükleri bilinir. $a:b=2:3$ demek, $a$ nın $2$ parça, $b$ nin $3$ parça olduğunu söyler; bir parçanın değeri ise henüz bilinmez. Bu bilinmeyen parça değerine $k$ denir ve büyüklükler $a=2k$, $b=3k$ biçiminde yazılır.",
            "Sorudaki ikinci bilgi, yani toplam, fark ya da büyüklüklerden birinin değeri, $k$ yı verir. $k$ bulunduğunda bütün büyüklükler hesaplanır. Oran problemlerinin çok büyük bölümü bu iki adımla çözülür. Aşağıdaki bölümlerde farklı soru türlerinin bu iki adıma nasıl indirgendiği gösteriliyor.",
            hap("Oranda her büyüklüğü ortak bir $k$ nın katı olarak yaz.",
                "İkinci bilgiyle $k$ yı bul, sonra istenen büyüklüğü hesapla."),
        ]},
        {"baslik": "Paylaştırma problemleri", "icerik": [
            "Bir miktar verilen oranlarda paylaştırılırken oran sayılarının toplamı parça sayısını verir. Toplam miktar parça sayısına bölünerek bir parçanın değeri bulunur. Toplam yerine fark verildiğinde de aynı mantık işler; bu kez fark, oran sayılarının farkı kadar parçaya karşılık gelir.",
            ornek(
                "Üç kardeş bir miktar parayı $2:3:5$ oranında paylaşıyor. En büyük pay, en küçük paydan $1200$ lira fazla.",
                "Her kardeşin payını ve toplam parayı bulalım.",
                "Paylar $2k$, $3k$ ve $5k$ olsun. En büyük ile en küçük arasındaki fark: $5k-2k=3k=1200$.",
                "$k=400$. Kardeşlerin payları sırasıyla $800$, $1200$ ve $2000$ liradır.",
                "Toplam para: $800+1200+2000=4000$ lira. Kontrol: $2000-800=1200$."),
            dikkat(
                "Farkı toplam gibi kullanmak.",
                "$1200$ lira toplam değil, iki payın farkıdır. $10k=1200$ yazmak, farkı bütün paranın yerine koymaktır. Fark, oran sayılarının farkına eşitlenir: $3k=1200$."),
        ]},
        {"baslik": "Ters orantılı paylaştırma", "icerik": [
            "\"Yaşlarıyla ters orantılı\" ya da \"harcadıkları süreyle ters orantılı\" gibi ifadelerde paylar verilen sayıların <strong>terslerine</strong> göre dağıtılır. Terslerin oranını tam sayılara çevirmek için oran, paydaların EKOK'u ile çarpılır.",
            ornek(
                "$900$ lira, yaşları $3$, $4$ ve $6$ olan üç çocuk arasında yaşlarıyla ters orantılı olarak paylaştırılıyor.",
                "Her çocuğun payını bulalım.",
                "Paylar $\\dfrac{1}{3}:\\dfrac{1}{4}:\\dfrac{1}{6}$ oranındadır. Paydaların EKOK'u $12$; oranı $12$ ile çarpalım: $4:3:2$.",
                "Toplam parça: $4+3+2=9$. Bir parça: $900:9=100$ lira.",
                "Paylar: $400$, $300$ ve $200$ lira. En küçük çocuk en büyük payı alır. Kontrol: payların yaşlarla çarpımı hep aynıdır; $3 \\cdot 400=4 \\cdot 300=6 \\cdot 200=1200$."),
            dikkat(
                "Ters orantıyı doğru orantı gibi paylaştırmak.",
                "Yaşlara doğrudan $3:4:6$ oranında dağıtmak en büyük payı en büyük çocuğa verir; ters orantıda ise durum tam tersidir. Ters orantılı paylaştırmada önce sayıların tersleri alınır."),
        ]},
        {"baslik": "Birleşik oranlarla kurulan problemler", "icerik": [
            "Üç büyüklük ikişer ikişer oranlarla verildiğinde önce ortak büyüklük eşitlenerek tek bir birleşik oran yazılır. Sonra bu oran üzerinden $k$ yöntemi uygulanır.",
            ornek(
                "Bir kulüp gezisinde kızların erkeklere oranı $3:4$, erkeklerin öğretmenlere oranı $8:1$ dir. Gezide toplam $150$ kişi var.",
                "Kız, erkek ve öğretmen sayılarını bulalım.",
                "Ortak büyüklük erkekler: birinci oranda $4$, ikincide $8$. Birinci oranı $2$ ile genişletelim: $6:8$.",
                "Birleşik oran: kız, erkek ve öğretmen sayıları $6:8:1$ oranındadır. Toplam parça: $15$.",
                "$15k=150$, yani $k=10$. Kız $60$, erkek $80$, öğretmen $10$ kişi."),
            "Ortak büyüklüğü eşitlemek için iki oranı, ortak terimlerin EKOK'una ulaşacak biçimde genişletmek yeterlidir. Burada $4$ ile $8$ in EKOK'u $8$ dir. Ortak terimi eşitlemeden iki oranı yan yana yazmak, örneğin $3:4:1$ gibi, erkeklerin iki farklı sayıyla gösterilmesine yol açar ve yanlış sonuç verir.",
        ]},
        {"baslik": "Oranı değişen gruplar", "icerik": [
            "Bir gruba kişi eklenip çıkarıldığında oran değişir. Başlangıçtaki sayılar $k$ ile yazılır, değişiklik eklenir ve yeni oran bir orantı olarak kurulur.",
            ornek(
                "Bir sınıfta kızların erkeklere oranı $5:7$ dir. Sınıftan $4$ kız öğrenci ayrılınca oran $3:7$ oluyor.",
                "Başlangıçtaki kız ve erkek sayılarını bulalım.",
                "Kızlar $5k$, erkekler $7k$ olsun. $4$ kız ayrılınca: $\\dfrac{5k-4}{7k}=\\dfrac{3}{7}$.",
                "İçler dışlar çarpımı: $7(5k-4)=21k$, yani $35k-28=21k$ ve $14k=28$.",
                "$k=2$. Başlangıçta $10$ kız ve $14$ erkek vardı. Kontrol: $6:14=3:7$."),
            "Bu sorularda değişmeyen grup, çözümün en güvenilir dayanağıdır. Burada erkek sayısı değişmedi; oranın paydası da bu yüzden $7k$ olarak kaldı.",
        ]},
        {"baslik": "Oran ve kesir birlikte", "icerik": [
            "Bazı sorularda önce iki grubun oranı, sonra her grubun içindeki bir kesir verilir. Gruplar $k$ ile yazılır ve kesirler bu ifadelere uygulanır.",
            ornek(
                "Bir okulda kızların erkeklere oranı $4:5$ tir. Kızların dörtte biri, erkeklerin beşte biri gözlük kullanıyor ve okulda $72$ gözlüklü öğrenci var.",
                "Okuldaki öğrenci sayısını bulalım.",
                "Kızlar $4k$, erkekler $5k$ olsun. Gözlüklü kızlar $4k$ nın dörtte biri, yani $k$; gözlüklü erkekler $5k$ nın beşte biri, yani yine $k$ dır.",
                "Toplam gözlüklü: $k+k=2k=72$, yani $k=36$.",
                "Okulda $4 \\cdot 36+5 \\cdot 36=9 \\cdot 36=324$ öğrenci var. Kontrol: $144$ kızın dörtte biri $36$, $180$ erkeğin beşte biri $36$."),
            "Oran sayılarının kesirlerin paydalarıyla uyumlu seçilmesi, bu tür soruları çok kısaltır. Burada $4k$ nın dörtte biri ve $5k$ nın beşte biri doğrudan $k$ ya eşit çıktı.",
        ]},
        {"baslik": "Aktarma ile değişen oran", "icerik": [
            "İki kişi ya da iki kap arasında bir miktar aktarıldığında birinin kaybı ötekinin kazancıdır. Toplam değişmez ama oran değişir. Başlangıç miktarları $k$ ile yazılır ve aktarılan miktar birinden çıkarılıp ötekine eklenir.",
            ornek(
                "İki kasadaki paraların oranı $5:3$ tür. Birinci kasadan ikinciye $60$ lira aktarılınca iki kasadaki para eşit oluyor.",
                "Başlangıçta her kasada ne kadar para olduğunu bulalım.",
                "Paralar $5k$ ve $3k$ olsun. Aktarmadan sonra: $5k-60=3k+60$.",
                "$2k=120$, yani $k=60$. Kasalarda $300$ ve $180$ lira vardı.",
                "Kontrol: aktarmadan sonra ikisinde de $240$ lira olur; toplam $480$ lira değişmemiştir."),
            dikkat(
                "Aktarılan miktarı yalnızca bir tarafa yazmak.",
                "$5k-60=3k$ gibi bir kurulum, aktarılan paranın ikinci kasaya eklenmesini unutmaktır. Aktarmada bir tarafın azalması, öteki tarafın aynı miktarda artması demektir."),
        ]},
        {"baslik": "Dördüncü orantılı", "icerik": [
            "Üç sayı verilip bunlarla orantı kuran dördüncü sayı sorulduğunda, $\\dfrac{a}{b}=\\dfrac{c}{x}$ orantısı yazılır ve içler dışlar çarpımıyla $x$ bulunur. Bu $x$ sayısına $a$, $b$ ve $c$ nin <strong>dördüncü orantılısı</strong> denir.",
            ornek(
                "$3$, $5$ ve $12$ sayıları verilsin.",
                "Bu sayıların dördüncü orantılısını bulalım.",
                "Orantı: $\\dfrac{3}{5}=\\dfrac{12}{x}$.",
                "İçler dışlar çarpımı: $3x=60$, yani $x=20$.",
                "Kontrol: $\\dfrac{3}{5}=\\dfrac{12}{20}$."),
            "Günlük hayattaki \"üç bilinenden dördüncüyü bulma\" soruları bu kalıba girer: $3$ defter $5$ liraysa $12$ defter kaç liradır sorusunun cevabı da $20$ liradır.",
        ]},
        {"baslik": "Ölçek ve harita problemleri", "icerik": [
            "Harita ve planlarda ölçek, çizimdeki uzunluğun gerçek uzunluğa oranıdır. Ölçek $1:n$ ise gerçek uzunluk, çizimdeki uzunluğun $n$ katıdır. Alanlar ise ölçeğin karesiyle büyür.",
            ornek(
                "Ölçeği $1:25000$ olan bir haritada iki nokta arası $6$ santimetredir.",
                "Gerçek uzaklığı kilometre olarak bulalım.",
                "Gerçek uzunluk: $6 \\cdot 25000=150000$ santimetre.",
                "$1$ kilometre $100000$ santimetre olduğu için uzaklık $1.5$ kilometredir."),
            ornek(
                "Aynı haritada bir parkın alanı $2$ santimetrekare olarak görünüyor.",
                "Parkın gerçek alanını metrekare olarak bulalım.",
                "Alan, ölçeğin karesiyle büyür: $2 \\cdot 25000^2=1250000000$ santimetrekare.",
                "$1$ metrekare $10000$ santimetrekaredir: $1250000000:10000=125000$ metrekare."),
            dikkat(
                "Alanı ölçekle bir kez çarpmak.",
                "Harita üzerindeki alan yalnızca $25000$ ile çarpılırsa sonuç $25000$ kat küçük çıkar. Uzunluk iki yönde de $25000$ kat büyüdüğü için alan $25000^2$ katına çıkar."),
        ]},
        {"baslik": "Tarif ve karışım ölçekleme", "icerik": [
            "Bir tarifteki malzemeler kişi sayısıyla doğru orantılıdır. Tarif büyütülürken ya da küçültülürken bütün malzemeler aynı oranla çarpılır; bu oran, yeni kişi sayısının eski kişi sayısına bölümüdür. Malzemelerden yalnızca birini artırmak, tarifin kendi içindeki oranları bozar ve sonuç değişir.",
            ornek(
                "$4$ kişilik bir tarifte $300$ gram un kullanılıyor.",
                "Aynı tarif $6$ kişi için kaç gram un gerektirir, bulalım.",
                "Ölçekleme oranı: $\\dfrac{6}{4}=\\dfrac{3}{2}$.",
                "Un: $300 \\cdot \\dfrac{3}{2}=450$ gram."),
            ornek(
                "Bir karışımda A maddesinin B maddesine oranı $3:5$ tir.",
                "B maddesinin karışımdaki yüzdesini bulalım.",
                "Karışımın tamamı $3+5=8$ parçadır; B bunun $5$ parçasıdır.",
                "B nin payı: $\\dfrac{5}{8}=0.625$, yani yüzde $62.5$."),
        ]},
        {"baslik": "Oranı koruyarak büyütmek", "icerik": [
            "Bir karışımın ya da grubun oranı korunarak toplam miktar değiştirilmek istendiğinde, yeni miktarlar aynı oranla yeniden hesaplanır. Eklenmesi gereken miktar, yeni ve eski değerlerin farkıdır.",
            ornek(
                "Toplam $40$ kilogramlık bir karışımda A maddesinin B maddesine oranı $3:5$ tir. Oran korunarak karışım $64$ kilograma çıkarılacak.",
                "Her maddeden ne kadar eklenmesi gerektiğini bulalım.",
                "Eski karışım: $8k=40$, yani $k=5$; A $15$, B $25$ kilogram.",
                "Yeni karışım: $8k=64$, yani $k=8$; A $24$, B $40$ kilogram.",
                "Eklenecek: A dan $9$, B den $15$ kilogram. Eklenen miktarlar da $9:15=3:5$ oranındadır."),
            "Son satır genel bir kuralı gösterir: oranı korumak için eklenen miktarların da aynı oranda olması gerekir. Yalnızca bir maddeden eklemek oranı her zaman bozar.",
        ]},
        {"baslik": "Hız ve süre oranları", "icerik": [
            "Aynı yol gidilirken hız ile süre ters orantılıdır. İki aracın hızlarının oranı verildiğinde süreleri bu oranın tersiyle orantılı olur.",
            ornek(
                "İki aracın hızlarının oranı $3:4$ tür. Birinci araç bir yolu $8$ saatte alıyor.",
                "İkinci aracın aynı yolu kaç saatte alacağını bulalım.",
                "Süreler hızların tersiyle orantılıdır: süreler oranı $4:3$ tür.",
                "Birinci aracın süresi $4$ parça ve $8$ saat ise bir parça $2$ saattir.",
                "İkinci aracın süresi $3$ parça, yani $6$ saattir."),
            "Hareket problemlerinin ayrıntısı <a href=\"/blog/hareket-problemleri-konu-anlatimi-pdf/\">Hareket Problemleri Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Çalışma hızlarının oranı", "icerik": [
            "İki kişinin çalışma hızlarının oranı verildiğinde, bir günde yaptıkları iş miktarları da aynı orandadır. Hızlar $k$ ile yazılır ve birlikte yaptıkları iş, işin tamamına eşitlenir. İşin tamamı $1$ birim kabul edilir; böylece her işçinin bir günde yaptığı iş, işin kesri olarak yazılır ve tek başına bitirme süresi bu kesrin tersidir.",
            ornek(
                "İki işçinin çalışma hızlarının oranı $2:3$ tür ve ikisi birlikte bir işi $30$ günde bitiriyor.",
                "Her birinin işi tek başına kaç günde bitireceğini bulalım.",
                "Bir günde yaptıkları işler $2k$ ve $3k$ olsun. Birlikte bir günde $5k$ iş yaparlar ve $30$ günde işin tamamını bitirirler: $5k \\cdot 30=1$.",
                "$k=\\dfrac{1}{150}$. Birinci işçi bir günde işin $\\dfrac{2}{150}=\\dfrac{1}{75}$ kadarını, ikinci işçi $\\dfrac{3}{150}=\\dfrac{1}{50}$ kadarını yapar.",
                "Birinci işçi işi tek başına $75$ günde, ikinci işçi $50$ günde bitirir."),
            "İşçi ve havuz problemlerinin ayrıntısı <a href=\"/blog/isci-ve-havuz-problemleri-konu-anlatimi-pdf/\">İşçi ve Havuz Problemleri Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Orantı özellikleriyle hızlı çözüm", "icerik": [
            "Yalnızca oranı verilen iki sayının toplamı, farkı ya da başka bir birleşimi soruluyorsa sayıların kendisini bulmaya gerek yoktur. Sayılar $k$ ile yazılır ve $k$ sadeleşir.",
            ornek(
                "$\\dfrac{a}{b}=\\dfrac{2}{3}$ olsun.",
                "$\\dfrac{a+b}{a-b}$ ifadesinin değerini bulalım.",
                "$a=2k$ ve $b=3k$ yazalım.",
                "$\\dfrac{2k+3k}{2k-3k}=\\dfrac{5k}{-k}=-5$."),
            "Sonuç $k$ dan bağımsızdır; yani oranı $2:3$ olan her sayı çifti için aynı değer çıkar. Bu yüzden bu tür sorularda sayıları bulmaya çalışmak gereksiz zaman kaybıdır. $a=4$ ve $b=6$ için de $\\dfrac{10}{-2}=-5$ bulunur.",
        ]},
        {"baslik": "Sınavda oran ve orantı problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) oran ve orantı problemleri paylaştırma, ters orantılı paylaştırma, birleşik oran, değişen oran ve ölçek soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde oran bilgisi karışım, hız ve iş sorularının da temelini oluşturur."),
            "Bir oran sorusunda ilk adım, oranı $k$ ile yazmaktır. İkinci adım, sorudaki bilginin toplam mı, fark mı, yoksa tek bir büyüklüğün değeri mi olduğunu belirlemektir. Bu ayrım yapıldığında denklem genellikle tek satırda kurulur. Bulunan değerleri oranın kendisine yeniden bölmek de kısa bir kontroldür: sonuç verilen orana eşit çıkmalıdır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Farkı toplam gibi kullanmak", "Fark, oran sayılarının farkına eşitlenir"],
                ["Ters orantıyı doğru orantı gibi paylaştırmak", "Önce sayıların terslerini al"],
                ["Birleşik oranda ortak terimi eşitlememek", "Ortak terimi EKOK ile eşitle"],
                ["Ölçekte alanı bir kez çarpmak", "Alan ölçeğin karesiyle büyür"],
                ["Hız oranını süre oranı sanmak", "Süreler hızların tersiyle orantılı"],
                ["Oranı parçanın bütüne oranı sanmak", "Oran sayılarını toplayarak bütünü bul"],
            ]),
            "Bu hataların çoğu, oranın neyi neyle karşılaştırdığını gözden kaçırmaktan doğar. Oranı yazarken her sayının hangi büyüklüğe ait olduğunu yanına not etmek, hataların çoğunu kurulum aşamasında önler.",
        ]},
    ],
    "sss": [
        ("Oran problemleri nasıl çözülür?",
         "Oranda yer alan her büyüklük ortak bir k nın katı olarak yazılır. Sorudaki toplam, fark ya da tek bir değer kullanılarak k bulunur ve istenen büyüklük hesaplanır."),
        ("Ters orantılı paylaştırma nasıl yapılır?",
         "Verilen sayıların tersleri alınır ve paydaların EKOK'u ile çarpılarak tam sayılı bir orana çevrilir. Miktar bu orana göre paylaştırılır."),
        ("Birleşik oran nasıl kurulur?",
         "İki oranda ortak olan büyüklük, EKOK kullanılarak iki oranda da aynı sayıya getirilir. Böylece üç büyüklük tek bir oranla yazılır."),
        ("Haritada alan nasıl hesaplanır?",
         "Alan, ölçeğin karesiyle büyür. Harita üzerindeki alan ölçek sayısının karesiyle çarpılır ve istenen birime çevrilir."),
        ("Hızların oranından süre nasıl bulunur?",
         "Aynı yol gidiliyorsa süreler hızların tersiyle orantılıdır. Hızlar 3 e 4 oranındaysa süreler 4 e 3 oranındadır."),
        ("Oranı verilen sayıların toplamı ve farkıyla kurulan ifade nasıl hesaplanır?",
         "Sayılar k ile yazılır ve ifadede k sadeleşir. Sonuç, oranı aynı olan bütün sayı çiftleri için aynıdır."),
        ("Aktarma sorularında oran nasıl kurulur?",
         "Başlangıç miktarları k ile yazılır. Aktarılan miktar bir taraftan çıkarılıp öteki tarafa eklenir ve yeni oran bir orantı olarak kurulur; toplam değişmez."),
        ("Dördüncü orantılı nedir?",
         "Verilen üç sayıyla orantı kuran dördüncü sayıdır. a bölü b, c bölü x e eşit yazılır ve içler dışlar çarpımıyla x bulunur."),
        ("Bir karışımın oranı korunarak nasıl büyütülür?",
         "Yeni toplam miktar aynı oranla paylaştırılır ve her maddenin yeni miktarından eskisi çıkarılır. Eklenen miktarlar da aynı oranda olmalıdır."),
    ],
    "kontrol": [
        "Oranları ortak bir k ile yazabiliyorum.",
        "Toplamı ya da farkı verilen paylaştırma sorularını çözebiliyorum.",
        "Ters orantılı paylaştırmada terslerin oranını tam sayılara çevirebiliyorum.",
        "İkişer ikişer verilen oranları birleşik orana dönüştürebiliyorum.",
        "Oranı değişen grup sorularını orantı kurarak çözebiliyorum.",
        "Ölçekten gerçek uzunluğu ve gerçek alanı bulabiliyorum.",
        "Bir tarifi kişi sayısına göre ölçekleyebiliyorum.",
        "Hız oranından süre oranına geçebiliyorum.",
        "Çalışma hızlarının oranından tek başına bitirme sürelerini bulabiliyorum.",
        "Oranı verilen sayılarla kurulan ifadeleri k sadeleştirerek hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["oran-ve-oranti-konu-anlatimi-pdf", "dogru-oranti-ve-ters-oranti", "isci-ve-havuz-problemleri-konu-anlatimi-pdf"],
}
