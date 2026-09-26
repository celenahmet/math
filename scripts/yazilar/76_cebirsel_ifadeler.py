# scripts/yazilar/76_cebirsel_ifadeler.py — Cebirsel Ifadeler (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "cebirsel-ifadeler-konu-anlatimi-pdf",
    "baslik": "Cebirsel İfadeler Konu Anlatımı PDF",
    "aciklama": "Cebirsel ifade nedir? Terim, katsayı, benzer terimler, toplama ve çarpma, parantez açma, değer hesaplama, ortak çarpan ve özdeşlikler; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "cebir",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "cebirsel-ifadeler-konu-anlatimi-pdf",
    "kapak_alt": "Cebirsel ifadeler: mavi ve kırmızı cebir karolarını türlerine göre gruplandıran iki öğrenci",
    "ozet": "Cebirsel ifade, sayıların yanında harflerin de kullanıldığı matematik ifadesidir. Harfler henüz bilinmeyen ya da değişebilen sayıların yerini tutar ve bir kuralı tek satırda anlatmayı sağlar. Bu yazıda cebirsel ifadenin parçalarını, benzer terimleri, toplama, çıkarma ve çarpmayı, parantez açmayı, bir ifadenin değerini hesaplamayı, ortak çarpan parantezine almayı, temel özdeşlikleri ve sözel ifadeleri cebirsel ifadeye çevirmeyi çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Cebirsel ifade nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi, işlem önceliğini ve üslü sayıları biliyor olman yeterli.",
                "İşlem sırası için <a href=\"/blog/islem-onceligi-nasil-yapilir/\">İşlem Önceliği Nasıl Yapılır?</a>, üsler için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısına göz at."),
            "İçinde en az bir harf bulunan ve sayılarla harflerin işlemlerle bağlandığı ifadelere <strong>cebirsel ifade</strong> denir. $3x+5$, $2a-b$ ve $x^2-4x+1$ birer cebirsel ifadedir. İfadedeki harflere <strong>değişken</strong> denir, çünkü yerlerine farklı sayılar yazılabilir. Harf taşımayan sayılar ise <strong>sabit</strong> olarak adlandırılır.",
            "Cebirsel ifadenin gücü, tek bir satırla sonsuz sayıda hesabı birden anlatabilmesidir. \"Tanesi $15$ lira olan kalemden kaç tane alınırsa alınsın ödenecek para\" cümlesi, $x$ kalem sayısı olmak üzere kısaca $15x$ diye yazılır.",
            tablo(["Sözel ifade", "Cebirsel ifade"], [
                ["Bir sayının $3$ katı", "$3x$"],
                ["Bir sayının $5$ fazlası", "$x+5$"],
                ["Bir sayının yarısı", "$\\dfrac{x}{2}$"],
                ["Bir sayının karesinin $1$ eksiği", "$x^2-1$"],
                ["Ardışık iki tam sayının toplamı", "$x+(x+1)$"],
            ]),
            "Cebirsel ifadede eşittir işareti yoktur. $3x+5=11$ gibi eşittir işareti içeren ve bilinmeyenin değerini bulmaya yarayan eşitliklere <strong>denklem</strong> denir; ayrıntısı <a href=\"/blog/birinci-dereceden-denklemler-konu-anlatimi-pdf/\">Birinci Dereceden Denklemler Konu Anlatımı PDF</a> yazısında.",
            hap("Cebirsel ifade, sayılar ve harflerin işlemlerle bağlandığı ifadedir; eşittir işareti taşımaz.",
                "Harfler değişken, harf taşımayan sayılar sabittir."),
        ]},
        {"baslik": "Terim, katsayı ve sabit terim", "icerik": [
            "Bir cebirsel ifade, toplama ve çıkarma işaretleriyle birbirinden ayrılan parçalardan oluşur. Bu parçaların her birine <strong>terim</strong> denir. Bir terimdeki sayı çarpanına <strong>katsayı</strong>, harf taşımayan terime de <strong>sabit terim</strong> denir.",
            ornek(
                "$4x^2-3x+7$ ifadesi verilsin.",
                "Terimlerini, katsayılarını ve sabit terimini bulalım.",
                "Terimler: $4x^2$, $-3x$ ve $7$. İfade üç terimlidir.",
                "$4x^2$ teriminin katsayısı $4$, $-3x$ teriminin katsayısı $-3$ tür.",
                "Sabit terim $7$ dir."),
            tablo(["Terim", "Katsayı", "Değişken kısmı"], [
                ["$5xy$", "$5$", "$xy$"],
                ["$-a^3$", "$-1$", "$a^3$"],
                ["$x$", "$1$", "$x$"],
                ["$\\dfrac{2}{3}m^2$", "$\\dfrac{2}{3}$", "$m^2$"],
            ]),
            "Değişkenin önünde sayı yazılmıyorsa katsayı $1$ dir: $x=1 \\cdot x$. Önünde yalnızca eksi işareti varsa katsayı $-1$ dir: $-a^3=-1 \\cdot a^3$.",
            dikkat(
                "İşaret, terimin bir parçasıdır.",
                "$4x^2-3x+7$ ifadesinde ikinci terim $3x$ değil, $-3x$ tir. Terimlerin yeri değiştirilirken işaret de terimle birlikte taşınır: $7+4x^2-3x$ aynı ifadedir."),
        ]},
        {"baslik": "Derece ve sıralama", "icerik": [
            "Tek değişkenli bir ifadede değişkenin en büyük üssüne ifadenin <strong>derecesi</strong> denir. $4x^2-3x+7$ ifadesinin derecesi $2$, $5x-1$ ifadesinin derecesi $1$ dir. Birden fazla değişkenli bir terimde ise terimin derecesi, değişkenlerin üslerinin toplamıdır: $3x^2y$ teriminin derecesi $2+1=3$ tür. Sıfırdan farklı bir sabit terimin derecesi ise $0$ kabul edilir, çünkü $7=7x^0$ olarak düşünülebilir.",
            "İfadeler genellikle değişkenin üssü büyükten küçüğe doğru sıralanarak yazılır. Bu yazım benzer terimleri görmeyi ve iki ifadeyi karşılaştırmayı kolaylaştırır.",
            ornek(
                "$7-2x+x^3+5x^2$ ifadesi verilsin.",
                "İfadeyi azalan kuvvetlere göre sıralayalım ve derecesini bulalım.",
                "En büyük üs $3$: $x^3$. Sonra $5x^2$, sonra $-2x$, en son sabit terim $7$.",
                "Sıralı yazım: $x^3+5x^2-2x+7$.",
                "İfadenin derecesi $3$ tür."),
        ]},
        {"baslik": "Benzer terimler", "icerik": [
            "Değişkenleri ve bu değişkenlerin üsleri tamamen aynı olan terimlere <strong>benzer terimler</strong> denir. Benzer terimler yalnızca katsayılarıyla ayrılır.",
            tablo(["Terimler", "Benzer mi?", "Neden"], [
                ["$3x$ ve $-5x$", "Evet", "İkisi de $x$"],
                ["$2x^2$ ve $7x^2$", "Evet", "İkisi de $x^2$"],
                ["$3x$ ve $3x^2$", "Hayır", "Üsler farklı"],
                ["$4xy$ ve $-yx$", "Evet", "$yx=xy$"],
                ["$2a$ ve $2b$", "Hayır", "Değişkenler farklı"],
            ]),
            "Katsayıların aynı olması terimleri benzer yapmaz; belirleyici olan değişken kısmıdır. $3x$ ile $3x^2$ aynı katsayıya sahiptir ama benzer değildir.",
            "<h3>Cebir karolarıyla düşünmek</h3>",
            "Benzer terim fikrini somutlaştırmanın bir yolu, cebir karolarıdır. Kenar uzunlukları $x$ ve $1$ olan uzun bir karo $x$ i, kenarı $1$ olan küçük bir kare $1$ i, kenarı $x$ olan büyük bir kare de $x^2$ yi temsil eder. Karoları türlerine göre gruplamak, benzer terimleri bir araya getirmekle aynıdır: iki uzun karo ile üç uzun karo birleşince beş uzun karo olur, ama uzun karolar ile küçük kareler tek bir türde birleşemez.",
            hap("Yalnız değişkenleri ve üsleri aynı olan terimler toplanıp çıkarılabilir; $3x$ ile $2y$ birleşmez."),
        ]},
        {"baslik": "Toplama ve çıkarma", "icerik": [
            "Cebirsel ifadelerde yalnızca benzer terimler toplanıp çıkarılabilir. Benzer terimler birleştirilirken katsayılar toplanır ya da çıkarılır, değişken kısmı aynen kalır: $2x+3x=5x$.",
            ornek(
                "$5x+3y-2x+y$ ifadesi verilsin.",
                "İfadeyi en sade biçimde yazalım.",
                "Benzer terimleri yan yana getirelim: $5x-2x+3y+y$.",
                "Katsayıları birleştirelim: $3x+4y$.",
                "$3x$ ile $4y$ benzer olmadığı için daha fazla birleştirilemez."),
            ornek(
                "$(3x^2-2x+5)+(x^2+4x-8)$ işlemi verilsin.",
                "Sonucu bulalım.",
                "$x^2$ li terimler: $3x^2+x^2=4x^2$.",
                "$x$ li terimler: $-2x+4x=2x$.",
                "Sabitler: $5-8=-3$. Sonuç: $4x^2+2x-3$."),
            "<h3>Eksi işaretli parantez</h3>",
            "Önünde eksi işareti bulunan bir parantez açılırken parantezin içindeki <strong>bütün terimlerin işareti değişir</strong>. Çünkü parantezin önündeki eksi, parantezi $-1$ ile çarpmak demektir.",
            ornek(
                "$(5a-3b)-(2a-7b)$ işlemi verilsin.",
                "Sonucu bulalım.",
                "İkinci parantezi açarken işaretler değişir: $5a-3b-2a+7b$.",
                "Benzer terimleri birleştirelim: $3a+4b$."),
            dikkat(
                "Eksi parantezde yalnız ilk terimin işaretini değiştirmek.",
                "$-(2a-7b)$ açılırken sonuç $-2a-7b$ değil, $-2a+7b$ dir. Eksi, parantezdeki her terime dağılır."),
        ]},
        {"baslik": "Çarpma", "icerik": [
            "Tek terimliler çarpılırken katsayılar kendi arasında, aynı değişkenler de kendi arasında çarpılır. Aynı tabanlı üslü ifadeler çarpılırken üsler toplanır: $3x \\cdot 4x=12x^2$ ve $2a^2 \\cdot 5a^3=10a^5$.",
            "<h3>Dağılma özelliği</h3>",
            "Bir terim bir parantezle çarpılırken parantezin içindeki <strong>her terimle ayrı ayrı</strong> çarpılır. Buna çarpmanın toplama ve çıkarma üzerine <strong>dağılma özelliği</strong> denir:",
            "$$a \\cdot (b+c)=a \\cdot b+a \\cdot c$$",
            ornek(
                "$3 \\cdot (2x-5)$ ve $-2x \\cdot (x-4)$ işlemleri verilsin.",
                "Parantezleri açalım.",
                "Birinci: $3 \\cdot 2x-3 \\cdot 5=6x-15$.",
                "İkinci: $-2x \\cdot x+(-2x) \\cdot (-4)=-2x^2+8x$."),
            "<h3>İki terimlinin iki terimliyle çarpımı</h3>",
            "İki parantez çarpılırken birinci parantezdeki her terim, ikinci parantezdeki her terimle çarpılır ve sonuçlar toplanır. Sonra benzer terimler birleştirilir.",
            ornek(
                "$(x+3) \\cdot (x+2)$ ve $(2x-1) \\cdot (x+4)$ çarpımları verilsin.",
                "Sonuçları bulalım.",
                "Birinci: $x^2+2x+3x+6=x^2+5x+6$.",
                "İkinci: $2x^2+8x-x-4=2x^2+7x-4$."),
            dikkat(
                "Bir toplamın karesini terimlerin kareleri sanmak.",
                "$(x+3)^2$ ifadesi $x^2+9$ değildir. Kare, ifadenin kendisiyle çarpımıdır: $(x+3) \\cdot (x+3)=x^2+6x+9$. Ortadaki $6x$ terimi çoğunlukla unutulan kısımdır."),
            hap("Tek terimliler çarpılırken katsayılar çarpılır, aynı tabanlı değişkenlerin üsleri toplanır: $2a^2 \\cdot 5a^3=10a^5$ olur."),
        ]},
        {"baslik": "Bölme ve sadeleştirme", "icerik": [
            "Bir ifade tek terimliye bölünürken payın her terimi ayrı ayrı bölünür. Payda sıfır olamayacağı için bölen terimin sıfırdan farklı olduğu kabul edilir.",
            ornek(
                "$\\dfrac{6x^2+9x}{3x}$ ifadesi verilsin; $x \\neq 0$.",
                "İfadeyi sadeleştirelim.",
                "Her terimi $3x$ e bölelim: $\\dfrac{6x^2}{3x}+\\dfrac{9x}{3x}$.",
                "Sonuç: $2x+3$."),
            dikkat(
                "Toplamın içindeki bir terimi sadeleştirmek.",
                "$\\dfrac{x+3}{3}$ ifadesinde $3$ ler birbirini götürmez; sonuç $x$ değildir. Doğrusu $\\dfrac{x}{3}+1$ dir. Sadeleştirme yalnızca payın ve paydanın <strong>çarpanları</strong> arasında yapılır."),
        ]},
        {"baslik": "Bir ifadenin değerini hesaplamak", "icerik": [
            "Bir cebirsel ifadenin değeri, değişkenlerin yerine verilen sayılar yazılarak bulunur. Yerine koyarken sayıyı <strong>parantez içine</strong> almak, özellikle negatif sayılarda işaret hatalarını önler.",
            ornek(
                "$x=-2$ için $x^2-3x+1$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "Yerine koyalım: $(-2)^2-3 \\cdot (-2)+1$.",
                "$4+6+1=11$."),
            ornek(
                "$a=3$ ve $b=-1$ için $2a^2-ab+b^2$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "Yerine koyalım: $2 \\cdot 3^2-3 \\cdot (-1)+(-1)^2$.",
                "$18+3+1=22$."),
            dikkat(
                "$-x^2$ ile $(-x)^2$ yi karıştırmak.",
                "$x=-3$ için $-x^2=-(-3)^2=-9$ dur; üs yalnızca $x$ e uygulanır, önündeki eksi sonradan gelir. $(-x)^2$ ise $9$ dur. Parantezsiz yazılan $-3^2$ de $-9$ a eşittir."),
        ]},
        {"baslik": "Ortak çarpan parantezine almak", "icerik": [
            "Dağılma özelliği tersten de kullanılabilir. İfadenin bütün terimlerinde ortak olan bir çarpan varsa bu çarpan parantezin dışına alınır. Bu işleme <strong>ortak çarpan parantezine alma</strong> denir ve çarpanlara ayırmanın ilk adımıdır.",
            ornek(
                "$6x+9$ ve $4x^2-10x$ ifadeleri verilsin.",
                "Ortak çarpan parantezine alalım.",
                "$6x+9$: katsayıların EBOB'u $3$; sonuç $3 \\cdot (2x+3)$.",
                "$4x^2-10x$: ortak çarpan $2x$; sonuç $2x \\cdot (2x-5)$.",
                "Kontrol için parantezleri geri açmak yeterlidir."),
            ornek(
                "$ax+ay-bx-by$ ifadesi verilsin.",
                "İfadeyi gruplayarak çarpanlarına ayıralım.",
                "İlk iki terimden $a$, son iki terimden $-b$ parantezine alalım: $a \\cdot (x+y)-b \\cdot (x+y)$.",
                "$x+y$ ortak çarpandır: $(x+y) \\cdot (a-b)$."),
            "Ortak çarpan fikri hesabı da kısaltır: $37 \\cdot 23+37 \\cdot 77=37 \\cdot (23+77)=37 \\cdot 100=3700$. Çarpanların ortak bölenleri için <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "İki ifade eşit mi?", "icerik": [
            "İki cebirsel ifadenin eşit olması, değişkene verilen <strong>her</strong> değer için aynı sonucu vermeleri demektir. Tek bir değerde aynı sonucu vermeleri yetmez; ama tek bir değerde farklı sonuç vermeleri, ifadelerin eşit olmadığını göstermeye yeter.",
            ornek(
                "$(x+1)^2$ ve $x^2+1$ ifadeleri verilsin.",
                "Bu iki ifadenin eşit olup olmadığını inceleyelim.",
                "$x=0$ için ikisi de $1$ verir; bu tek başına bir şey kanıtlamaz.",
                "$x=1$ için birincisi $4$, ikincisi $2$ verir. Sonuçlar farklı olduğu için ifadeler eşit değildir.",
                "Gerçekten $(x+1)^2=x^2+2x+1$ dir; aradaki fark $2x$ terimidir ve yalnızca $x=0$ iken sıfır olur."),
            "Bu yöntem, parantez açarken ya da sadeleştirirken yapılan hataları yakalamak için de kullanılabilir: işlemden önceki ve sonraki ifadeye aynı sayıyı verip sonuçları karşılaştırmak, hatayı hemen ortaya çıkarır.",
        ]},
        {"baslik": "Temel özdeşlikler", "icerik": [
            "Değişkenlere hangi sayı verilirse verilsin doğru olan eşitliklere <strong>özdeşlik</strong> denir. Aşağıdaki üç özdeşlik, iki terimlinin çarpımından doğrudan elde edilir ve çok sık kullanılır:",
            "$$(a+b)^2=a^2+2ab+b^2$$",
            "$$(a-b)^2=a^2-2ab+b^2$$",
            "$$a^2-b^2=(a-b) \\cdot (a+b)$$",
            "Üçüncüsüne <strong>iki kare farkı</strong> denir. Bu özdeşlikler hem ifadeleri sadeleştirmek hem de zihinden hesap yapmak için kullanılır.",
            ornek(
                "$51^2$ ve $99 \\cdot 101$ işlemleri verilsin.",
                "Özdeşliklerle zihinden hesaplayalım.",
                "$51^2=(50+1)^2=2500+100+1=2601$.",
                "$99 \\cdot 101=(100-1) \\cdot (100+1)=10000-1=9999$."),
            ornek(
                "$\\dfrac{x^2-9}{x-3}$ ifadesi verilsin; $x \\neq 3$.",
                "İfadeyi sadeleştirelim.",
                "Pay iki kare farkıdır: $x^2-9=(x-3) \\cdot (x+3)$.",
                "Ortak çarpan $x-3$ sadeleşir: sonuç $x+3$."),
            hap("$(a+b)^2=a^2+2ab+b^2$ olur; ortadaki $2ab$ terimi unutulmamalıdır."),
        ]},
        {"baslik": "Sözel ifadeyi cebirsel ifadeye çevirmek", "icerik": [
            "Problemlerin çoğunda ilk adım, cümleyi cebirsel ifadeye çevirmektir. Bilinmeyen niceliğe bir harf verilir ve cümle, işlemlerin sırasına dikkat edilerek yazılır.",
            ornek(
                "\"Bir sayının $3$ katının $4$ eksiği\" ve \"bir sayının $4$ eksiğinin $3$ katı\" ifadeleri verilsin.",
                "İkisini cebirsel olarak yazalım.",
                "Birinci: önce $3$ katı alınır, sonra $4$ çıkarılır: $3x-4$.",
                "İkinci: önce $4$ çıkarılır, sonra $3$ katı alınır: $3 \\cdot (x-4)=3x-12$.",
                "Aynı kelimeler farklı sırayla farklı ifadeler verir."),
            ornek(
                "Ardışık üç çift sayı verilsin.",
                "Bu sayıların toplamını cebirsel ifade olarak yazalım.",
                "En küçüğü $x$ olsun; diğerleri $x+2$ ve $x+4$ tür.",
                "Toplam: $x+(x+2)+(x+4)=3x+6$."),
            "Cebirsel ifade kurmak, denklem kurmanın yarısıdır. İfadenin bir değere eşit olduğu söylendiğinde bir denklem ortaya çıkar; bu adımın ayrıntısı <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısında.",
            hap("Aylık sabit ücreti $150$ lira, her ek gigabaytı $20$ lira olan bir telefon tarifesinde $x$ ek gigabaytın faturası $150+20x$ lira olur.", "$3$ ek gigabayt kullanan kişi $150+20 \\cdot 3=210$ lira öder.", gunluk=True),
        ]},
        {"baslik": "Geometride cebirsel ifadeler", "icerik": [
            "Kenar uzunlukları harfle verilen şekillerin çevresi ve alanı birer cebirsel ifadedir. Bu ifadeler, şeklin ölçüsü değiştikçe çevrenin ve alanın nasıl değiştiğini tek satırda gösterir.",
            ornek(
                "Kısa kenarı $x$, uzun kenarı $x+3$ santimetre olan bir dikdörtgen verilsin.",
                "Dikdörtgenin çevresini ve alanını cebirsel ifade olarak yazalım.",
                "Çevre: $2 \\cdot (x+3)+2 \\cdot x=2x+6+2x=4x+6$.",
                "Alan: $x \\cdot (x+3)=x^2+3x$.",
                "Örneğin $x=5$ için çevre $26$, alan $40$ olur."),
            "Kapaktaki cebir karoları bu fikrin somut hâlidir. $x^2+3x$ alanı, kenarı $x$ olan bir büyük kare ile üç uzun karodan oluşan bir dikdörtgen gibi dizilebilir. Karoların oluşturduğu dikdörtgenin kenarları $x$ ve $x+3$ tür; bu da $x^2+3x=x \\cdot (x+3)$ çarpanlara ayırmasının görsel karşılığıdır.",
        ]},
        {"baslik": "Toplam ve çarpımdan değer bulmak", "icerik": [
            "Bazı sorularda değişkenlerin kendisi değil, toplamları ya da çarpımları verilir. Bu durumda özdeşlikler, değişkenleri tek tek bulmadan istenen ifadeyi hesaplamayı sağlar.",
            ornek(
                "$x+y=5$ ve $x \\cdot y=6$ olsun.",
                "$x^2+y^2$ toplamını bulalım.",
                "$(x+y)^2=x^2+2xy+y^2$ özdeşliğinden $x^2+y^2=(x+y)^2-2xy$.",
                "Yerine koyalım: $5^2-2 \\cdot 6=25-12=13$."),
            ornek(
                "$a-b=3$ ve $a \\cdot b=10$ olsun.",
                "$a^2+b^2$ toplamını bulalım.",
                "$(a-b)^2=a^2-2ab+b^2$ özdeşliğinden $a^2+b^2=(a-b)^2+2ab$.",
                "Yerine koyalım: $3^2+2 \\cdot 10=9+20=29$."),
            "İlk örnekte $x$ ve $y$ sayıları $2$ ile $3$ tür ve gerçekten $4+9=13$ eder. Ama özdeşlik yolu, sayıları hiç bulmadan aynı sonuca ulaşır ve sayılar tam sayı olmadığında da işe yarar.",
        ]},
        {"baslik": "Sınavda cebirsel ifadeler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu benzer terimleri birleştirme, parantez açma, değer hesaplama, ortak çarpan parantezine alma ve özdeşliklerle sadeleştirme biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde cebirsel ifadeler, sayısal akıl yürütme ve problem sorularının içinde de gerekebilir."),
            "Uzun görünen bir ifadeyle karşılaştığında önce parantezleri açmak, sonra benzer terimleri gruplamak çoğu zaman ifadeyi birkaç terime indirir. Özdeşliklerle çözülecek sorularda ise ifadenin $a^2-b^2$ ya da $(a+b)^2$ kalıbına benzeyip benzemediğine bakmak gerekir. Seçenekli sorularda bulduğun sonucu, değişkene küçük bir sayı vererek soru ifadesiyle karşılaştırmak da hızlı ve güvenilir bir kontrol yoludur.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$3x+2y=5xy$ yazmak", "Benzer olmayan terimler birleşmez"],
                ["$-(x-3)=-x-3$", "$-(x-3)=-x+3$"],
                ["$(x+3)^2=x^2+9$", "$(x+3)^2=x^2+6x+9$"],
                ["$\\dfrac{x+3}{3}=x$", "$\\dfrac{x}{3}+1$"],
                ["$x=-3$ için $-x^2=9$", "$-x^2=-9$"],
                ["$2x \\cdot 3x=6x$", "$2x \\cdot 3x=6x^2$"],
            ]),
            "Bu hataların çoğu, işlemlerin neye uygulandığını gözden kaçırmaktan doğar. Eksi işaretinin, üssün ve sadeleştirmenin hangi terimleri kapsadığını her adımda kontrol etmek bu hataları önler.",
        ]},
    ],
    "sss": [
        ("Cebirsel ifade nedir?",
         "Sayıların ve harflerin toplama, çıkarma, çarpma ve bölme gibi işlemlerle bağlandığı ifadedir. Eşittir işareti taşımaz."),
        ("Terim ve katsayı nedir?",
         "Terim, ifadenin artı ve eksi işaretleriyle ayrılan her bir parçasıdır. Katsayı, bir terimdeki sayı çarpanıdır."),
        ("Benzer terim nedir?",
         "Değişkenleri ve üsleri tamamen aynı olan terimlerdir. Benzer terimler katsayıları toplanarak birleştirilir."),
        ("Cebirsel ifadeler nasıl toplanır?",
         "Parantezler açılır, benzer terimler yan yana getirilir ve katsayıları toplanır. Benzer olmayan terimler olduğu gibi kalır."),
        ("Dağılma özelliği nedir?",
         "Bir sayının ya da terimin bir parantezle çarpılırken parantezin içindeki her terimle ayrı ayrı çarpılmasıdır."),
        ("Cebirsel ifade ile denklem arasındaki fark nedir?",
         "Cebirsel ifadede eşittir işareti yoktur. Denklem ise bir cebirsel ifadenin bir değere ya da başka bir ifadeye eşit olduğunu söyler ve çözülerek bilinmeyen bulunur."),
        ("Cebirsel ifadenin derecesi nedir?",
         "Tek değişkenli bir ifadede değişkenin en büyük üssüdür. Örneğin dört iks kare eksi üç iks artı yedi ifadesinin derecesi ikidir."),
        ("Toplam ve çarpım verilince kareler toplamı nasıl bulunur?",
         "İki sayının kareleri toplamı, toplamlarının karesinden çarpımlarının iki katı çıkarılarak bulunur. Sayıları tek tek bulmaya gerek kalmaz."),
        ("İki ifadenin eşit olduğunu nasıl anlarım?",
         "Parantezleri açıp benzer terimleri birleştirerek iki ifadeyi aynı biçime getir. Aynı biçime geliyorlarsa eşittirler. Değişkene bir sayı verildiğinde farklı sonuç çıkıyorsa ifadeler eşit değildir."),
    ],
    "kontrol": [
        "Değişken, sabit, terim ve katsayı kavramlarını ayırt edebiliyorum.",
        "Bir ifadenin terimlerini işaretleriyle birlikte yazabiliyorum.",
        "Benzer terimleri tanıyıp birleştirebiliyorum.",
        "Eksi işaretli parantezi doğru açabiliyorum.",
        "Dağılma özelliğiyle parantezli çarpımları açabiliyorum.",
        "İki terimlileri çarpıp sonucu sadeleştirebiliyorum.",
        "Negatif sayıları parantez içinde yerine koyarak değer hesaplayabiliyorum.",
        "Ortak çarpanı parantez dışına alabiliyorum.",
        "Temel özdeşlikleri hesap ve sadeleştirmede kullanabiliyorum.",
        "Sözel bir ifadeyi doğru sırayla cebirsel ifadeye çevirebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birinci-dereceden-denklemler-konu-anlatimi-pdf", "uslu-sayilar-konu-anlatimi-pdf", "islem-onceligi-nasil-yapilir"],
}
