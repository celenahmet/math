# scripts/yazilar/71_ondalik_gosterim.py — Ondalik Gosterim (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "ondalik-gosterim-konu-anlatimi-pdf",
    "baslik": "Ondalık Gösterim Konu Anlatımı PDF",
    "aciklama": "Ondalık gösterim nedir? Basamak değerleri, kesir ve ondalık dönüşümü, dört işlem, 10 un kuvvetleriyle işlem, yuvarlama ve problemler; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "ondalik-gosterim-konu-anlatimi-pdf",
    "kapak_alt": "Ondalık gösterim: onluk bloklar, onda birlik şeritler ve yüzde birlik küplerle bir bütünü parçalara ayıran öğrenci",
    "ozet": "Ondalık gösterim, kesirleri onun kuvvetleri üzerinden yazmanın yoludur: onda bir, yüzde bir, binde bir. Para, uzunluk, ağırlık ve sınav puanları gibi günlük hayattaki ölçümlerin çoğu bu gösterimle yazılır. Bu yazıda ondalık sayıların basamak değerlerini, okunuşunu, kesirle arasındaki dönüşümü, karşılaştırmayı, dört işlemi, onun kuvvetleriyle hızlı çarpma ve bölmeyi, yuvarlamayı ve günlük problemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Ondalık gösterim nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için basamak değerini ve kesirleri biliyor olman yeterli.",
                "Kesirlerin temeli için <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a> yazısına göz at."),
            "Tam sayılarda her basamak, sağındakinin on katıdır: birler, onlar, yüzler, binler. Ondalık gösterim bu düzeni virgülün sağına doğru devam ettirir. Virgülün hemen sağındaki basamak bir bütünün <strong>onda biri</strong>, bir sonraki <strong>yüzde biri</strong>, bir sonraki <strong>binde biri</strong> kadardır. Her basamak, solundakinin onda biri olur.",
            "Türkiye'de tam kısım ile ondalık kısım arasına <strong>virgül</strong> konur: $3.472$ sayısı ekranda üç tam binde dört yüz yetmiş iki diye okunur. Bazı ülkelerde ve hesap makinelerinde bu ayırıcı olarak nokta kullanılır; anlam aynıdır.",
            tablo(["Basamak", "Değeri", "Kesir karşılığı"], [
                ["Birler", "$1$", "$1$"],
                ["Onda birler", "$0.1$", "$\\dfrac{1}{10}$"],
                ["Yüzde birler", "$0.01$", "$\\dfrac{1}{100}$"],
                ["Binde birler", "$0.001$", "$\\dfrac{1}{1000}$"],
            ]),
            hap("Virgülün sağındaki basamaklar sırayla onda bir, yüzde bir ve binde bir değerindedir.",
                "Her basamak solundakinin onda biri, sağındakinin on katıdır."),
        ]},
        {"baslik": "Ondalık sayıyı çözümlemek ve okumak", "icerik": [
            "Bir ondalık sayıyı basamak değerlerinin toplamı olarak yazmaya <strong>çözümleme</strong> denir. Çözümleme, her rakamın gerçekte ne kadarlık bir değeri gösterdiğini açıkça ortaya koyar.",
            ornek(
                "$3.472$ sayısı verilsin.",
                "Sayıyı çözümleyelim ve okuyalım.",
                "Rakamlar ve basamakları: $3$ birler, $4$ onda birler, $7$ yüzde birler, $2$ binde birler.",
                "Çözümleme: $3.472=3+\\dfrac{4}{10}+\\dfrac{7}{100}+\\dfrac{2}{1000}$.",
                "Okunuşu: üç tam binde dört yüz yetmiş iki. Son basamak binde birler olduğu için ondalık kısım \"binde\" diye okunur."),
            "Okurken ondalık kısmın son basamağının adı kullanılır: $0.7$ onda yedi, $0.07$ yüzde yedi, $0.007$ binde yedidir. Sondaki sıfırlar değeri değiştirmez: $0.5$, $0.50$ ve $0.500$ aynı sayıdır. Ama virgülün hemen sağındaki sıfırlar değeri değiştirir: $0.5$ ile $0.05$ çok farklıdır.",
            dikkat(
                "Sondaki sıfır değeri değiştirmez, aradaki sıfır değiştirir.",
                "$2.30=2.3$ tür, ama $2.03$ bambaşka bir sayıdır: iki tam yüzde üç."),
        ]},
        {"baslik": "Kesirden ondalık sayıya", "icerik": [
            "Bir kesri ondalık sayıya çevirmenin iki yolu vardır. Paydası $10$, $100$ ya da $1000$ yapılabiliyorsa kesir genişletilir; yapılamıyorsa pay paydaya bölünür.",
            ornek(
                "$\\dfrac{3}{25}$ ve $\\dfrac{7}{20}$ kesirleri verilsin.",
                "Genişleterek ondalık sayıya çevirelim.",
                "$\\dfrac{3}{25}=\\dfrac{12}{100}=0.12$.",
                "$\\dfrac{7}{20}=\\dfrac{35}{100}=0.35$."),
            ornek(
                "$\\dfrac{3}{8}$ kesri verilsin.",
                "Bölme yaparak ondalık sayıya çevirelim.",
                "$3:8$ işleminde $3$ ün yanına sıfırlar ekleyerek bölmeye devam edelim: $30:8=3$, kalan $6$; $60:8=7$, kalan $4$; $40:8=5$, kalan $0$.",
                "Sonuç: $\\dfrac{3}{8}=0.375$."),
            "Her kesir sonlu bir ondalık sayıya çevrilemez. En sade hâldeki kesrin paydasında $2$ ve $5$ ten başka bir asal çarpan varsa bölme hiç bitmez ve basamaklar bir düzen içinde tekrar eder: $\\dfrac{1}{3}=0.333\\ldots$ Bu sayıların nasıl yazıldığı ve kesre nasıl çevrildiği <a href=\"/blog/devirli-ondalik-sayilar-nasil-kesre-cevrilir/\">Devirli Ondalık Sayılar Nasıl Kesre Çevrilir?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Ondalık sayıdan kesre", "icerik": [
            "Sonlu bir ondalık sayı, virgülden sonraki basamak sayısı kadar sıfırı olan bir paydayla kesre çevrilir: bir basamak için $10$, iki basamak için $100$, üç basamak için $1000$. Sonra kesir sadeleştirilir.",
            ornek(
                "$0.35$ ve $2.125$ sayıları verilsin.",
                "İkisini de en sade kesir olarak yazalım.",
                "$0.35=\\dfrac{35}{100}$; pay ve payda $5$ e bölününce $\\dfrac{7}{20}$.",
                "$2.125=\\dfrac{2125}{1000}$; pay ve payda $125$ e bölününce $\\dfrac{17}{8}$.",
                "Kontrol: $17:8=2.125$."),
            hap("Kesirden ondalığa: paydayı onun kuvvetine genişlet ya da payı paydaya böl.",
                "Ondalıktan kesre: virgülden sonraki basamak kadar sıfırlı paydaya yaz, sonra sadeleştir."),
        ]},
        {"baslik": "Ondalık sayıları karşılaştırmak", "icerik": [
            "Ondalık sayılar karşılaştırılırken önce tam kısımlara bakılır. Tam kısımlar eşitse ondalık basamaklar soldan sağa sırayla karşılaştırılır; ilk farklı basamakta büyük rakamı olan sayı büyüktür. Basamak sayıları farklıysa sona sıfır eklemek karşılaştırmayı kolaylaştırır.",
            ornek(
                "$0.7$, $0.68$, $0.702$ ve $0.07$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Basamakları eşitleyelim: $0.700$, $0.680$, $0.702$, $0.070$.",
                "Onda birler basamakları: $7$, $6$, $7$, $0$. En küçük $0.070$, sonra $0.680$.",
                "$0.700$ ile $0.702$ binde birler basamağında ayrılır.",
                "Sıralama: $0.07<0.68<0.7<0.702$."),
            dikkat(
                "Basamak sayısı çok olan sayı büyük değildir.",
                "$0.68$ in iki, $0.7$ nin bir ondalık basamağı var; ama $0.7$ daha büyüktür. Ondalık sayılarda uzunluk değil, soldan başlayarak basamak değerleri belirleyicidir."),
            "Negatif ondalık sayıların ve farklı türden sayıların sıralanması için <a href=\"/blog/sayi-dogrusu-ve-sayilari-siralama/\">Sayı Doğrusu ve Sayıları Sıralama</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Toplama ve çıkarma", "icerik": [
            "Ondalık sayılar toplanırken ya da çıkarılırken <strong>virgüller alt alta</strong> gelecek biçimde yazılır. Böylece aynı basamaklar üst üste gelir: onda birler onda birlerin, yüzde birler yüzde birlerin altında. Eksik basamaklar sıfırla tamamlanır ve işlem tam sayılardaki gibi yapılır.",
            ornek(
                "$12.5+3.075$ ve $7-2.36$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "Birinci: $12.500+3.075=15.575$.",
                "İkinci: $7$ yi $7.00$ olarak yazalım: $7.00-2.36=4.64$."),
            dikkat(
                "Virgülleri hizalamadan toplama.",
                "$12.5+3.075$ işleminde sayılar sağa yaslanıp toplanırsa basamaklar kayar ve sonuç yanlış çıkar. Hizalanan şey sağ kenar değil, virgüldür."),
        ]},
        {"baslik": "Çarpma", "icerik": [
            "Ondalık sayılar çarpılırken önce virgüller yokmuş gibi tam sayılar çarpılır. Sonra çarpanlardaki ondalık basamak sayıları toplanır ve sonuçta sağdan o kadar basamak ayrılarak virgül konur.",
            "Kuralın nedeni kesirlerdedir: $2.4=\\dfrac{24}{10}$ ve $0.35=\\dfrac{35}{100}$ olduğu için çarpımları $\\dfrac{24 \\cdot 35}{10 \\cdot 100}=\\dfrac{840}{1000}$ tır. Paydadaki sıfırların sayısı, iki çarpandaki ondalık basamakların toplamıdır.",
            ornek(
                "$2.4 \\cdot 0.35$ çarpımı verilsin.",
                "Sonucu bulalım.",
                "Virgülsüz çarpalım: $24 \\cdot 35=840$.",
                "Ondalık basamaklar: $2.4$ te bir, $0.35$ te iki; toplam üç.",
                "Sağdan üç basamak ayıralım: $0.840=0.84$."),
            "<h3>10, 100 ve 1000 ile çarpmak</h3>",
            "Bir ondalık sayıyı $10$ ile çarpmak virgülü bir basamak sağa, $100$ ile çarpmak iki basamak sağa, $1000$ ile çarpmak üç basamak sağa kaydırır. Gerekirse sona sıfır eklenir: $3.472 \\cdot 100=347.2$ ve $0.5 \\cdot 1000=500$.",
            dikkat(
                "Çarpım her zaman büyümez.",
                "$1$ den küçük bir ondalık sayıyla çarpınca sonuç küçülür: $40 \\cdot 0.25=10$. Bu, kesirlerde $1$ den küçük bir kesirle çarpmanın ondalık karşılığıdır."),
            hap("Ondalık sayılar önce tam sayılar gibi çarpılır.", "Sonra çarpanlardaki ondalık basamak sayılarının toplamı kadar basamak sağdan ayrılır ve virgül konur."),
        ]},
        {"baslik": "Bölme", "icerik": [
            "Bölen bir ondalık sayıysa, bölen ve bölünen aynı anda $10$, $100$ ya da $1000$ ile çarpılarak bölen tam sayı yapılır. Bu, bir kesrin payını ve paydasını aynı sayıyla genişletmek gibidir ve bölümü değiştirmez.",
            ornek(
                "$7.2:0.4$ ve $0.63:0.009$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "Birinci: ikisini $10$ ile çarpalım: $72:4=18$.",
                "İkinci: ikisini $1000$ ile çarpalım: $630:9=70$."),
            "Bölen tam sayıysa bölme olduğu gibi yapılır ve bölümdeki virgül, bölünendeki virgülün hizasına konur: $9.6:4=2.4$.",
            "<h3>10, 100 ve 1000 ile bölmek</h3>",
            "$10$ a bölmek virgülü bir basamak sola, $100$ e bölmek iki basamak sola, $1000$ e bölmek üç basamak sola kaydırır. Gerekirse başa sıfır eklenir: $45.6:100=0.456$ ve $7:1000=0.007$.",
            hap("Çarpmada ondalık basamak sayıları toplanır; bölmede bölen tam sayı yapılır.",
                "Onun kuvvetleriyle çarpmak virgülü sağa, bölmek sola kaydırır."),
        ]},
        {"baslik": "Yuvarlama", "icerik": [
            "Bir ondalık sayıyı belirli bir basamağa yuvarlamak için o basamağın hemen sağındaki rakama bakılır. Bu rakam $5$ ya da daha büyükse yuvarlanan basamak bir artırılır; $5$ ten küçükse aynen bırakılır. Sağdaki basamakların hepsi atılır.",
            ornek(
                "$3.46$ ve $2.749$ sayıları verilsin.",
                "Birincisini onda birler, ikincisini yüzde birler basamağına yuvarlayalım.",
                "$3.46$: onda birler basamağı $4$, sağındaki rakam $6$; $6 \\geq 5$ olduğu için $3.5$.",
                "$2.749$: yüzde birler basamağı $4$, sağındaki rakam $9$; sonuç $2.75$."),
            ornek(
                "$4.96$ sayısı verilsin.",
                "Onda birler basamağına yuvarlayalım.",
                "Onda birler basamağı $9$, sağındaki rakam $6$; $9$ bir artınca $10$ olur.",
                "Bu yüzden birler basamağına bir aktarılır: sonuç $5.0$."),
            dikkat(
                "Yuvarlama tek adımda yapılır, zincirleme yapılmaz.",
                "$2.449$ sayısını onda birlere yuvarlarken yalnızca sağdaki ilk rakama, yani $4$ e bakılır: sonuç $2.4$ tür. Önce yüzde birlere $2.45$, sonra onda birlere $2.5$ diye iki adımda yuvarlamak yanlış sonuç verir."),
        ]},
        {"baslik": "Tahminle hesap", "icerik": [
            "Ondalık sayılarla yapılan uzun bir işlemin sonucunu önceden kabaca tahmin etmek, virgülün yanlış yere konduğu hataları yakalamanın en kolay yoludur. Her sayı en yakın tam sayıya yuvarlanır ve tahmin hesaplanır.",
            ornek(
                "$4.98 \\cdot 3.02$ çarpımı verilsin.",
                "Önce tahmin edelim, sonra hesaplayalım.",
                "Tahmin: $5 \\cdot 3=15$.",
                "Hesap: $498 \\cdot 302=150396$; dört ondalık basamak: $15.0396$.",
                "Sonuç tahmine çok yakın; virgül doğru yerde."),
            "Virgül yanlışlıkla bir basamak kaysaydı sonuç $1.50396$ ya da $150.396$ gibi tahminden çok uzak çıkardı ve hata hemen fark edilirdi.",
        ]},
        {"baslik": "Günlük hayatta ondalık sayılar", "icerik": [
            "Para, ölçü ve puan hesaplarının çoğu ondalık sayılarla yapılır. Bu tür sorularda birimi sonuçla birlikte yazmak anlamı netleştirir.",
            ornek(
                "Tanesi $4.75$ lira olan kalemden $3$ tane alınıp $20$ lira veriliyor.",
                "Kaç lira para üstü alınır?",
                "Tutar: $3 \\cdot 4.75=14.25$ lira.",
                "Para üstü: $20-14.25=5.75$ lira."),
            ornek(
                "Bir öğrencinin üç sınav notu $7.5$, $8.25$ ve $6.75$ olsun.",
                "Bu notların ortalamasını bulalım.",
                "Toplam: $7.5+8.25+6.75=22.5$.",
                "Ortalama: $22.5:3=7.5$."),
        ]},
        {"baslik": "Ondalık sayılar sayı doğrusunda", "icerik": [
            "$0$ ile $1$ arasını on eşit parçaya bölersek her parça $0.1$ uzunluğunda olur ve işaretler sırayla $0.1$, $0.2$, $0.3$ diye $0.9$ a kadar gider. $0.1$ ile $0.2$ arasını da on eşit parçaya bölersek $0.11$, $0.12$ diye $0.19$ a kadar giden yeni işaretler elde ederiz. Bu bölme hiç bitmeden sürdürülebilir. Bu yüzden iki farklı ondalık sayı arasında her zaman başka ondalık sayılar bulunur.",
            ornek(
                "$2.3$ ve $2.4$ sayıları verilsin.",
                "Bu iki sayı arasında iki ondalık basamaklı kaç sayı olduğunu bulalım.",
                "Basamakları eşitleyelim: $2.30$ ve $2.40$.",
                "Aradaki iki ondalık basamaklı sayılar $2.31$, $2.32$ diye $2.39$ a kadar gider; toplam $9$ tane.",
                "Üç ondalık basamağa izin verilirse $2.301$ den $2.399$ a kadar $99$ tane sayı vardır. Basamak sayısı arttıkça aradaki sayılar da çoğalır."),
            ornek(
                "$\\dfrac{3}{4}$ ve $0.7$ sayıları verilsin.",
                "Hangisinin sayı doğrusunda daha sağda olduğunu bulalım.",
                "Kesri ondalık sayıya çevirelim: $\\dfrac{3}{4}=\\dfrac{75}{100}=0.75$.",
                "Basamakları eşitleyelim: $0.75$ ve $0.70$. Yüzde birler basamağında $5>0$ olduğu için $0.75>0.7$.",
                "Sayı doğrusunda büyük olan sayı daha sağdadır; bu yüzden $\\dfrac{3}{4}$ daha sağda yer alır."),
            "Bir kesir ile bir ondalık sayıyı karşılaştırmanın en kolay yolu ikisini aynı gösterime getirmektir. Kesir sonlu bir ondalık sayıya kolayca çevrilebiliyorsa ondalık gösterim, çevrilemiyorsa kesir gösterimi tercih edilir.",
        ]},
        {"baslik": "Kesir, ondalık ve yüzde", "icerik": [
            "Yüzde, paydası $100$ olan bir kesrin başka bir yazılışıdır: $\\%35=\\dfrac{35}{100}=0.35$. Bu yüzden ondalık sayıdan yüzdeye geçmek için sayıyı $100$ ile çarpmak, yani virgülü iki basamak sağa kaydırmak yeterlidir. Yüzdeden ondalık sayıya geçerken de virgül iki basamak sola kaydırılır: $\\%7=0.07$.",
            tablo(["Kesir", "Ondalık", "Yüzde"], [
                ["$\\dfrac{1}{2}$", "$0.5$", "$\\%50$"],
                ["$\\dfrac{1}{4}$", "$0.25$", "$\\%25$"],
                ["$\\dfrac{3}{4}$", "$0.75$", "$\\%75$"],
                ["$\\dfrac{1}{5}$", "$0.2$", "$\\%20$"],
                ["$\\dfrac{2}{5}$", "$0.4$", "$\\%40$"],
                ["$\\dfrac{1}{8}$", "$0.125$", "$\\%12.5$"],
                ["$\\dfrac{1}{10}$", "$0.1$", "$\\%10$"],
                ["$\\dfrac{1}{20}$", "$0.05$", "$\\%5$"],
                ["$\\dfrac{1}{25}$", "$0.04$", "$\\%4$"],
            ]),
            "Bu eşlikleri akılda tutmak, hem ondalık sayılarla hem de yüzdelerle yapılan hesaplarda zaman kazandırır. Örneğin $0.25$ ile çarpmak $4$ e bölmekle, $0.125$ ile çarpmak $8$ e bölmekle aynıdır: $36 \\cdot 0.25=36:4=9$. Yüzde hesaplarının ayrıntısı <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Birim dönüşümlerinde ondalık sayılar", "icerik": [
            "Metrik birimler birbirine onun kuvvetleriyle bağlıdır: $1$ metre $100$ santimetre, $1$ kilometre $1000$ metre, $1$ kilogram $1000$ gram, $1$ litre $1000$ mililitredir. Bu yüzden bir birimden ötekine geçmek, virgülü kaydırmaktan ibarettir. Büyük birimden küçük birime geçerken sayı büyür ve virgül sağa kayar; küçük birimden büyük birime geçerken sayı küçülür ve virgül sola kayar.",
            ornek(
                "$2.5$ kilometre, $1.75$ kilogram ve $350$ santimetre verilsin.",
                "Sırasıyla metreye, grama ve metreye çevirelim.",
                "$2.5 \\cdot 1000=2500$ metre.",
                "$1.75 \\cdot 1000=1750$ gram.",
                "$350:100=3.5$ metre."),
            ornek(
                "$3.2$ metrelik bir ip, her biri $0.4$ metre olan parçalara ayrılıyor.",
                "Kaç parça elde edildiğini bulalım.",
                "Parça sayısı $3.2:0.4$ tür.",
                "İkisini $10$ ile çarpalım: $32:4=8$.",
                "Sonuç: $8$ parça."),
            dikkat(
                "Farklı birimlerle işlem yapmak.",
                "$1.2$ metre ile $45$ santimetre toplanırken önce ikisi aynı birime çevrilmelidir: $1.2+0.45=1.65$ metre. Birim çevrilmeden yapılan $1.2+45$ işleminin anlamı yoktur."),
            hap("Market tartısında $1.25$ kilogram gelen peynir $1250$ gramdır.", "Kilogramdan grama geçerken virgül üç basamak sağa kayar, çünkü $1$ kilogram $1000$ gramdır.", gunluk=True),
        ]},
        {"baslik": "Karışık işlemler", "icerik": [
            "Birden fazla işlem içeren ondalık ifadelerde tam sayılardaki işlem önceliği aynen geçerlidir: önce parantez içi, sonra soldan sağa çarpma ve bölme, en son soldan sağa toplama ve çıkarma. Ayrıntısı için <a href=\"/blog/islem-onceligi-nasil-yapilir/\">İşlem Önceliği Nasıl Yapılır?</a> yazısına bakabilirsin.",
            ornek(
                "$0.5 \\cdot (3.2-1.8)+0.36:0.12$ işlemi verilsin.",
                "Sonucu bulalım.",
                "Parantez içi: $3.2-1.8=1.4$.",
                "Çarpma: $0.5 \\cdot 1.4=0.7$.",
                "Bölme: $0.36:0.12=36:12=3$.",
                "Toplama: $0.7+3=3.7$."),
            ornek(
                "$\\dfrac{0.25 \\cdot 0.8}{0.02}$ işlemi verilsin.",
                "Ondalık sayıları kesre çevirerek hesaplayalım.",
                "$0.25=\\dfrac{1}{4}$ olduğu için pay $\\dfrac{1}{4} \\cdot 0.8=0.2$ olur.",
                "Bölme: $0.2:0.02=20:2=10$.",
                "Sonuç: $10$."),
            "İkinci örnekte $0.25$ i kesre çevirmek, üç basamaklı bir çarpma yapmaktan kurtardı. Sınavda karşılaşılan ondalık işlemlerin çoğunda sayılar bu tür kolaylıklara izin verecek biçimde seçilir.",
        ]},
        {"baslik": "Sınavda ondalık gösterim", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu ondalık sayılarla dört işlem, kesir ve ondalık dönüşümü, sıralama ve yuvarlama biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde ondalık sayılar para, ortalama ve yüzde hesaplarının içinde de gerekebilir."),
            "Karmaşık görünen ondalık işlemlerde ondalık sayıları kesre çevirmek çoğu hesabı kısaltır: $0.25$ yerine $\\dfrac{1}{4}$, $0.125$ yerine $\\dfrac{1}{8}$ yazmak, çarpma ve bölmeyi sadeleştirmeyle çözmeyi sağlar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$0.7<0.68$ sanmak", "$0.7>0.68$"],
                ["Toplamada sağa yaslamak", "Virgülleri hizala"],
                ["Çarpmada virgülü yanlış yere koymak", "Ondalık basamakları topla"],
                ["$2.03=2.3$ sanmak", "Aradaki sıfır değeri değiştirir"],
                ["Zincirleme yuvarlamak", "Tek adımda yuvarla"],
                ["$\\dfrac{1}{3}$ i sonlu yazmak", "$0.333\\ldots$ devirlidir"],
            ]),
            "Bu hataların çoğu, ondalık basamakların değerini unutmaktan doğar. Her rakamın onda bir, yüzde bir ya da binde bir değerinde olduğunu akılda tutmak ve sonucu tahminle kontrol etmek bu hataları önler.",
        ]},
    ],
    "sss": [
        ("Ondalık gösterim nedir?",
         "Kesirlerin onda bir, yüzde bir ve binde bir gibi basamak değerleriyle yazılmasıdır. Tam kısım ile ondalık kısım arasına virgül konur."),
        ("Ondalık sayı nasıl okunur?",
         "Önce tam kısım okunur, sonra ondalık kısım son basamağın adıyla okunur. Örneğin üç tam binde dört yüz yetmiş iki."),
        ("Kesir ondalık sayıya nasıl çevrilir?",
         "Payda onun bir kuvvetine genişletilebiliyorsa genişletilir; genişletilemiyorsa pay paydaya bölünür."),
        ("Ondalık sayılarda çarpma nasıl yapılır?",
         "Virgüller yokmuş gibi çarpılır, sonra çarpanlardaki ondalık basamak sayıları toplanır ve sonuçta sağdan o kadar basamak ayrılır."),
        ("Ondalık sayıya bölerken ne yapılır?",
         "Bölen ve bölünen aynı anda 10, 100 ya da 1000 ile çarpılarak bölen tam sayı yapılır. Bu işlem sonucu değiştirmez."),
        ("Yuvarlama nasıl yapılır?",
         "Yuvarlanacak basamağın sağındaki rakam 5 ya da daha büyükse basamak bir artırılır, küçükse aynen bırakılır. Sağdaki basamaklar atılır."),
        ("Her kesir ondalık sayıya çevrilebilir mi?",
         "Evet. En sade hâldeki kesrin paydasında yalnızca 2 ve 5 çarpanları varsa sonlu bir ondalık sayı, başka bir asal çarpan varsa devirli bir ondalık sayı elde edilir."),
        ("Ondalık sayı yüzdeye nasıl çevrilir?",
         "Sayı 100 ile çarpılır, yani virgül iki basamak sağa kaydırılır ve önüne yüzde işareti konur. Yüzdeden ondalığa geçerken virgül iki basamak sola kaydırılır."),
    ],
    "kontrol": [
        "Ondalık basamakların değerlerini sayabiliyorum.",
        "Bir ondalık sayıyı çözümleyip doğru okuyabiliyorum.",
        "Sondaki ve aradaki sıfırın farkını açıklayabiliyorum.",
        "Kesirleri genişleterek ya da bölerek ondalık sayıya çevirebiliyorum.",
        "Sonlu ondalık sayıları en sade kesir olarak yazabiliyorum.",
        "Ondalık sayıları basamak basamak karşılaştırıp sıralayabiliyorum.",
        "Virgülleri hizalayarak toplama ve çıkarma yapabiliyorum.",
        "Ondalık sayılarda çarpma ve bölmeyi doğru yapabiliyorum.",
        "Onun kuvvetleriyle çarparken ve bölerken virgülü doğru kaydırabiliyorum.",
        "Bir ondalık sayıyı istenen basamağa tek adımda yuvarlayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["devirli-ondalik-sayilar-nasil-kesre-cevrilir", "kesirler-konu-anlatimi-pdf", "yuzdeler-konu-anlatimi-pdf"],
}
