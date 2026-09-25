# scripts/yazilar/28_logaritma_kurallari.py — Logaritma Kurallari ve Formulleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "logaritma-kurallari-formulleri",
    "baslik": "Logaritma Kuralları ve Formülleri",
    "aciklama": "Logaritma kuralları nelerdir? Çarpım, bölüm ve kuvvet kuralı, taban değiştirme, zincir kuralı, logaritmalı üsler ve harfle verilen değerler; ispatlı ve çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "logaritma",
    "sinavlar": ["AYT"],
    "kapak": "logaritma-kurallari-formulleri",
    "kapak_alt": "Logaritma kuralları ve formülleri: mavi ve kırmızı blok gruplarını birleştirip ayıran ve tekrar düzenleriyle dizen iki öğrenci",
    "ozet": "Logaritma kuralları, çarpma ve bölme gibi zor işlemleri toplama ve çıkarmaya, kuvvet almayı ise çarpmaya dönüştürür. Bu kurallar üs kurallarının logaritma dilindeki karşılığıdır ve logaritmalı her ifadenin sadeleştirilmesinde kullanılır. Bu yazıda çarpım, bölüm ve kuvvet kurallarını ispatlarıyla, tabanın kuvveti kuralını, taban değiştirme formülünü, ters çevirme ve zincir kurallarını, logaritmalı üsleri, yaklaşık değerlerle hesaplamayı, harfle verilen logaritmalarla çalışmayı ve sık yapılan hataları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kurallar neden gerekli?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için logaritmanın tanımını ve üs kurallarını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/logaritma-konu-anlatimi/\">Logaritma Konu Anlatımı</a> ve <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı</a> yazılarına göz at."),
            "$\\log_6 4+\\log_6 9$ ifadesindeki iki logaritmanın hiçbiri tam sayı değildir, ama toplamları $2$ dir. Bunu görmek için logaritma kuralları gerekir. Kurallar, farklı görünen logaritmaları birleştirmeyi, ayırmayı ve tek bir değere indirmeyi sağlar.",
            "Kapaktaki öğrenciler mavi ve kırmızı blok gruplarını birleştiriyor, ayırıyor ve aynı gruptan birkaç tane yan yana diziyor. Bu üç hareket, logaritmanın çarpım, bölüm ve kuvvet kurallarına karşılık geliyor. Diğer bütün formüller bu üç temel kuralın birleşimidir.",
        ]},
        {"baslik": "Üs kurallarından logaritma kurallarına", "icerik": [
            "Logaritma bir üs olduğu için logaritma kuralları üs kurallarından gelir. Aynı tabanlı kuvvetler çarpılırken üsler toplanır; bu yüzden çarpımın logaritması, logaritmaların toplamıdır. Bölmede üsler çıkarılır; kuvvetin kuvvetinde ise üsler çarpılır.",
            tablo(["Üs kuralı", "Logaritma kuralı"], [
                ["$a^m \\cdot a^n=a^{m+n}$", "$\\log_a(xy)=\\log_a x+\\log_a y$"],
                ["$\\dfrac{a^m}{a^n}=a^{m-n}$", "$\\log_a \\dfrac{x}{y}=\\log_a x-\\log_a y$"],
                ["$(a^m)^n=a^{mn}$", "$\\log_a x^n=n\\log_a x$"],
            ]),
            "Kuralların hepsinde $x$ ve $y$ pozitif, taban ise pozitif ve $1$ den farklıdır. Bu koşullar unutulursa kurallar yanlış sonuç verebilir.",
        ]},
        {"baslik": "Çarpım kuralı", "icerik": [
            "$\\log_a x=m$ ve $\\log_a y=n$ olsun. Tanımdan $x=a^m$ ve $y=a^n$ olur. Çarpım $xy=a^{m+n}$ olduğundan $\\log_a(xy)=m+n$ bulunur. Böylece çarpımın logaritması logaritmaların toplamına eşittir:",
            "$$\\log_a(xy)=\\log_a x+\\log_a y$$",
            ornek(
                "$\\log_6 4+\\log_6 9$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Çarpım kuralıyla ifade $\\log_6(4 \\cdot 9)=\\log_6 36$ olur.",
                "$6^2=36$ olduğundan sonuç $2$ dir."),
        ]},
        {"baslik": "Bölüm kuralı", "icerik": [
            "Aynı yolla bölümün logaritması logaritmaların farkıdır. $\\dfrac{x}{y}=a^{m-n}$ olduğundan:",
            "$$\\log_a \\dfrac{x}{y}=\\log_a x-\\log_a y$$",
            ornek(
                "$\\log_3 54-\\log_3 2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Bölüm kuralıyla ifade $\\log_3 \\dfrac{54}{2}=\\log_3 27$ olur.",
                "$3^3=27$ olduğundan sonuç $3$ tür."),
            "Bölüm kuralının özel bir durumu $\\log_a \\dfrac{1}{x}=-\\log_a x$ eşitliğidir; çünkü $\\log_a 1=0$ dır. Bir sayının tersinin logaritması, logaritmasının ters işaretlisidir.",
        ]},
        {"baslik": "Kuvvet kuralı", "icerik": [
            "$x=a^m$ ise $x^n=a^{mn}$ olur. Bu yüzden bir kuvvetin logaritmasında üs, logaritmanın önüne katsayı olarak iner:",
            "$$\\log_a x^n=n\\log_a x$$",
            ornek(
                "$\\log_2 8^5$ ve $\\log_5 \\sqrt{125}$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$\\log_2 8^5=5\\log_2 8=5 \\cdot 3=15$ olur.",
                "$\\log_5 \\sqrt{125}=\\dfrac{1}{2}\\log_5 125=\\dfrac{1}{2} \\cdot 3=\\dfrac{3}{2}$ olur."),
            "Kökler de kesirli üs olarak yazılıp aynı kurala uyar: $\\log_2 \\sqrt[3]{16}=\\dfrac{1}{3}\\log_2 16=\\dfrac{4}{3}$ olur.",
        ]},
        {"baslik": "Kuvvet kuralında tanım koşulu", "icerik": [
            "Kuvvet kuralı yalnızca logaritması alınan sayı pozitifken doğrudan uygulanabilir. Çift kuvvetlerde bu koşula özellikle dikkat etmek gerekir: $x^2$ her $x \\neq 0$ için pozitiftir ama $x$ negatif olabilir.",
            ornek(
                "$x=-3$ için $\\log_3 x^2$ ifadesi verilsin.",
                "Kuvvet kuralının nasıl uygulanacağını inceleyelim.",
                "$\\log_3(-3)^2=\\log_3 9=2$ olur; ama $2\\log_3(-3)$ tanımsızdır.",
                "Doğru yazım $\\log_a x^2=2\\log_a |x|$ tir; burada $2\\log_3 3=2$ bulunur."),
            "Bu ayrım özellikle logaritmalı denklemlerde önemlidir: $\\log x^2$ yerine $2\\log x$ yazmak negatif çözümleri siler.",
        ]},
        {"baslik": "Tabanın kuvveti", "icerik": [
            "Taban da bir kuvvet olarak yazılabiliyorsa tabandaki üs logaritmanın önüne bölen olarak iner. Sayıdaki ve tabandaki üsler birlikte şu kuralı verir:",
            "$$\\log_{a^m} b^n=\\dfrac{n}{m}\\log_a b$$",
            ornek(
                "$\\log_8 32$ ve $\\log_{\\sqrt{2}} 8$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$\\log_{2^3} 2^5=\\dfrac{5}{3}\\log_2 2=\\dfrac{5}{3}$ olur.",
                "$\\log_{2^{1/2}} 2^3=\\dfrac{3}{1/2}=6$ olur."),
        ]},
        {"baslik": "Taban değiştirme formülü", "icerik": [
            "Farklı tabanlı logaritmalar ortak bir tabana çevrilerek karşılaştırılır ya da hesaplanır. Taban değiştirme formülü, her logaritmayı istenen bir $c$ tabanındaki iki logaritmanın bölümü olarak yazar:",
            "$$\\log_a b=\\dfrac{\\log_c b}{\\log_c a}$$",
            "İspatı kısadır: $\\log_a b=x$ ise $a^x=b$ dir. İki tarafın $c$ tabanında logaritması alınınca kuvvet kuralıyla $x\\log_c a=\\log_c b$ olur ve $x$ yalnız bırakılır.",
            ornek(
                "$\\log_4 32$ ve $\\log_9 27$ ifadeleri verilsin.",
                "Taban değiştirmeyle bulalım.",
                "$\\log_4 32=\\dfrac{\\log_2 32}{\\log_2 4}=\\dfrac{5}{2}$ olur.",
                "$\\log_9 27=\\dfrac{\\log_3 27}{\\log_3 9}=\\dfrac{3}{2}$ olur."),
        ]},
        {"baslik": "Kurallarla karşılaştırma", "icerik": [
            "Farklı görünen iki logaritmanın eşit olup olmadığı ya da hangisinin büyük olduğu kurallarla anlaşılır. Tabanın kuvveti kuralı, birçok ifadeyi aynı tabana indirerek karşılaştırmayı hesapsız hâle getirir.",
            ornek(
                "$\\log_4 9$ ile $\\log_2 3$, sonra $\\log_2 3$ ile $\\dfrac{3}{2}$ karşılaştırılsın.",
                "Hangisinin büyük olduğunu bulalım.",
                "$\\log_4 9=\\log_{2^2} 3^2=\\log_2 3$ olduğundan ilk iki sayı eşittir.",
                "$\\dfrac{3}{2}=\\log_2 2^{3/2}=\\log_2 \\sqrt{8}$ ve $\\sqrt{8}<\\sqrt{9}=3$ olduğundan $\\log_2 3$ daha büyüktür."),
        ]},
        {"baslik": "Hesap makinesiyle logaritma", "icerik": [
            "Hesap makineleri genellikle yalnızca onluk ve doğal logaritmayı hesaplar. Başka tabanlı bir logaritma, taban değiştirme formülüyle bu iki tabandan birine çevrilir.",
            ornek(
                "$\\log 7 \\approx 0.8451$ ve $\\log 2 \\approx 0.3010$ değerleri verilsin.",
                "$\\log_2 7$ değerini yaklaşık olarak bulalım.",
                "$\\log_2 7=\\dfrac{\\log 7}{\\log 2} \\approx \\dfrac{0.8451}{0.3010}$ olur.",
                "Sonuç yaklaşık $2.81$ dir; gerçekten $2^2=4<7<8=2^3$ olduğundan değer $2$ ile $3$ arasındadır."),
        ]},
        {"baslik": "Ters çevirme kuralı", "icerik": [
            "Taban değiştirme formülünde $c=b$ alınırsa pay $1$ olur ve bir logaritmanın tabanı ile sayısı yer değiştirince değerin çarpmaya göre tersi elde edilir:",
            "$$\\log_a b=\\dfrac{1}{\\log_b a}$$",
            ornek(
                "$\\log_2 3 \\cdot \\log_3 2$ ve $\\dfrac{1}{\\log_2 6}+\\dfrac{1}{\\log_3 6}$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "Birincisi $\\log_2 3 \\cdot \\dfrac{1}{\\log_2 3}=1$ olur.",
                "İkincisi $\\log_6 2+\\log_6 3=\\log_6 6=1$ olur."),
        ]},
        {"baslik": "Ters çevirmeyle toplam", "icerik": [
            "Paydasında logaritma bulunan kesirler ters çevirme kuralıyla aynı tabanlı logaritmalara dönüşür. Böylece kesirler toplamı tek bir logaritmada birleşir.",
            ornek(
                "$\\dfrac{1}{\\log_2 30}+\\dfrac{1}{\\log_3 30}+\\dfrac{1}{\\log_5 30}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Her kesir ters çevrilir: $\\log_{30} 2+\\log_{30} 3+\\log_{30} 5$.",
                "Çarpım kuralıyla $\\log_{30}(2 \\cdot 3 \\cdot 5)=\\log_{30} 30=1$ olur."),
        ]},
        {"baslik": "Zincir kuralı", "icerik": [
            "Birinin sayısı diğerinin tabanı olan logaritmalar çarpılınca aradaki sayı sadeleşir. Taban değiştirme formülüyle her çarpan bir bölüm olarak yazılırsa paylar ve paydalar birbirini götürür:",
            "$$\\log_a b \\cdot \\log_b c=\\log_a c$$",
            ornek(
                "$\\log_2 3 \\cdot \\log_3 4 \\cdot \\log_4 5 \\cdot \\log_5 6 \\cdot \\log_6 7 \\cdot \\log_7 8$ çarpımı verilsin.",
                "Değerini bulalım.",
                "Zincir kuralı art arda uygulanınca aradaki bütün sayılar sadeleşir ve $\\log_2 8$ kalır.",
                "Sonuç $3$ tür."),
        ]},
        {"baslik": "Kapanan zincir", "icerik": [
            "Zincirin son sayısı ilk tabana eşitse, yani zincir başladığı yere dönüyorsa çarpım her zaman $1$ dir: $\\log_a b \\cdot \\log_b c \\cdot \\log_c a=\\log_a a=1$. Bu kural, tabanları ve sayıları döngü oluşturan çarpımları tek adımda hesaplatır.",
            ornek(
                "$\\log_2 5 \\cdot \\log_5 9 \\cdot \\log_9 2$ çarpımı verilsin.",
                "Değerini bulalım.",
                "Zincir kuralıyla ilk iki çarpan $\\log_2 9$ olur; bu da $\\log_9 2$ ile çarpılınca $\\log_2 2$ kalır.",
                "Sonuç $1$ dir."),
        ]},
        {"baslik": "Logaritmaları verilen sayılarla işlem", "icerik": [
            "İki sayının aynı tabandaki logaritmaları biliniyorsa, bu sayılardan kurulan çarpım, bölüm ve kuvvetlerin logaritmaları kurallarla doğrudan hesaplanır. Sayıların kendilerini bulmaya gerek kalmaz.",
            ornek(
                "$\\log_a x=2$ ve $\\log_a y=3$ olsun.",
                "$\\log_a(x^2 y)$, $\\log_a \\dfrac{\\sqrt{x}}{y}$ ve $\\log_a \\dfrac{x^3}{y^2}$ değerlerini bulalım.",
                "$\\log_a(x^2 y)=2 \\cdot 2+3=7$ ve $\\log_a \\dfrac{\\sqrt{x}}{y}=\\dfrac{1}{2} \\cdot 2-3=-2$ olur.",
                "$\\log_a \\dfrac{x^3}{y^2}=3 \\cdot 2-2 \\cdot 3=0$ olur; bu da $x^3=y^2$ olduğunu gösterir."),
        ]},
        {"baslik": "Logaritmalı üsler", "icerik": [
            "$a^{\\log_a b}=b$ eşitliği, üssünde logaritma bulunan ifadeleri sadeleştirir. Üs bir toplamsa önce üs kuralıyla parçalanır.",
            ornek(
                "$5^{\\log_5 7}$ ve $2^{3+\\log_2 5}$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "Birincisi doğrudan $7$ olur.",
                "İkincisi $2^3 \\cdot 2^{\\log_2 5}=8 \\cdot 5=40$ olur."),
            "Daha ileri bir kural da vardır: $a^{\\log_b c}=c^{\\log_b a}$ eşitliği her uygun $a$, $b$ ve $c$ için doğrudur. İki tarafın $b$ tabanında logaritması alınınca ikisi de $\\log_b a \\cdot \\log_b c$ olur. Örneğin $3^{\\log_2 5}=5^{\\log_2 3}$ tür.",
        ]},
        {"baslik": "Yaklaşık değerlerle hesap", "icerik": [
            "$\\log 2 \\approx 0.301$ ve $\\log 3 \\approx 0.477$ değerleri bilinirse birçok sayının onluk logaritması kurallarla bulunur. Sayı $2$, $3$ ve $10$ un çarpımları ve bölümleri olarak yazılır:",
            tablo(["Sayı", "Yazılış", "Yaklaşık logaritma"], [
                ["$6$", "$2 \\cdot 3$", "$0.778$"],
                ["$5$", "$\\dfrac{10}{2}$", "$0.699$"],
                ["$12$", "$2^2 \\cdot 3$", "$1.079$"],
                ["$1.5$", "$\\dfrac{3}{2}$", "$0.176$"],
            ]),
            "$\\log 5=\\log 10-\\log 2=1-\\log 2$ eşitliği özellikle kullanışlıdır; $5$ in logaritması doğrudan $2$ ninkinden elde edilir. Aynı yolla $\\log 25=2-2\\log 2$ ve $\\log 50=2-\\log 2$ yazılabilir.",
        ]},
        {"baslik": "Harfle verilen logaritmalar", "icerik": [
            "Sınav sorularında logaritmalar çoğu zaman harfle verilir ve başka bir logaritmanın bu harfler cinsinden yazılması istenir. Yöntem aynıdır: sayı, logaritması bilinen sayıların çarpımına ve bölümüne ayrılır.",
            ornek(
                "$\\log 2=a$ ve $\\log 3=b$ olsun.",
                "$\\log 18$ ve $\\log 15$ ifadelerini $a$ ve $b$ cinsinden yazalım.",
                "$18=2 \\cdot 3^2$ olduğundan $\\log 18=a+2b$ olur.",
                "$15=\\dfrac{3 \\cdot 10}{2}$ olduğundan $\\log 15=b+1-a$ olur."),
            ornek(
                "Yine $\\log 2=a$ ve $\\log 3=b$ olsun.",
                "$\\log_6 12$ ifadesini $a$ ve $b$ cinsinden yazalım.",
                "Taban değiştirme: $\\log_6 12=\\dfrac{\\log 12}{\\log 6}$.",
                "$\\log 12=2a+b$ ve $\\log 6=a+b$ olduğundan sonuç $\\dfrac{2a+b}{a+b}$ olur."),
        ]},
        {"baslik": "Harfle verilen tabanda logaritma", "icerik": [
            "Bazen tek bir logaritma harfle verilir ve başka tabanlı bir logaritma istenir. Bu durumda verilen logaritmanın tabanı ortak taban seçilir ve istenen ifade taban değiştirmeyle bu tabana çevrilir.",
            ornek(
                "$\\log_2 3=a$ olsun.",
                "$\\log_{12} 18$ ifadesini $a$ cinsinden yazalım.",
                "Taban $2$ ye çevrilir: $\\log_{12} 18=\\dfrac{\\log_2 18}{\\log_2 12}$.",
                "$\\log_2 18=1+2a$ ve $\\log_2 12=2+a$ olduğundan sonuç $\\dfrac{1+2a}{2+a}$ olur."),
        ]},
        {"baslik": "Kurallarla basamak sayısı", "icerik": [
            "Kuvvet kuralı, büyük bir kuvvetin kaç basamaklı olduğunu bulmayı kolaylaştırır. Kuvvetin onluk logaritması, üs ile tabanın logaritmasının çarpımıdır; basamak sayısı bu değerin tam kısmının bir fazlasıdır.",
            ornek(
                "$\\log 3 \\approx 0.477$ olduğu biliniyor.",
                "$3^{20}$ sayısının kaç basamaklı olduğunu bulalım.",
                "$\\log 3^{20}=20\\log 3 \\approx 9.54$ olur.",
                "Tam kısım $9$ olduğundan sayı $10$ basamaklıdır."),
        ]},
        {"baslik": "Doğal logaritmada kurallar", "icerik": [
            "Doğal logaritma da bir logaritma olduğu için bütün kurallar onda da geçerlidir. $\\ln$ ile yazılan ifadelerde tabanın $e$ olduğu unutulmamalıdır: $\\ln e=1$ ve $e^{\\ln x}=x$.",
            ornek(
                "$\\ln e^3$, $e^{\\ln 5}$ ve $\\ln 8-3\\ln 2$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$\\ln e^3=3$ ve $e^{\\ln 5}=5$ olur.",
                "$\\ln 8=\\ln 2^3=3\\ln 2$ olduğundan üçüncüsü $0$ olur."),
        ]},
        {"baslik": "Birden fazla kuralla sadeleştirme", "icerik": [
            "Uzun ifadelerde kurallar sırayla uygulanır: önce katsayılar kuvvet kuralıyla sayının üssüne taşınır, sonra toplamlar çarpım, farklar bölüm olarak birleştirilir. Tek bir logaritmaya inen ifade kolayca hesaplanır.",
            ornek(
                "$\\log_2 12-\\log_2 3+2\\log_2 \\dfrac{1}{2}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Katsayı üsse taşınır: $2\\log_2 \\dfrac{1}{2}=\\log_2 \\dfrac{1}{4}$.",
                "İfade $\\log_2 \\left(\\dfrac{12}{3} \\cdot \\dfrac{1}{4}\\right)=\\log_2 1=0$ olur."),
            ornek(
                "$\\dfrac{\\log 8+\\log 27}{\\log 6}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Pay $\\log 216=\\log 6^3=3\\log 6$ olur.",
                "Sonuç $\\dfrac{3\\log 6}{\\log 6}=3$ olur."),
        ]},
        {"baslik": "Katsayılı ifadeyi tek logaritmaya indirmek", "icerik": [
            "Katsayılı logaritmalar toplanırken ya da çıkarılırken önce her katsayı kuvvet kuralıyla sayının üssüne taşınır. Katsayı kalmadığında toplama ve çıkarma çarpım ve bölüm kurallarıyla tek bir logaritmada birleşir.",
            ornek(
                "$2\\log 5+\\log 4$ ve $3\\log_2 6-\\log_2 27$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "Birincisi $\\log 25+\\log 4=\\log 100=2$ olur.",
                "İkincisi $\\log_2 216-\\log_2 27=\\log_2 8=3$ olur."),
        ]},
        {"baslik": "Ortak tabana getirme", "icerik": [
            "Farklı tabanlı logaritmalar toplanacaksa önce aynı tabana getirilir. Tabanlar aynı asal sayının kuvvetleriyse tabanın kuvveti kuralı işlemi kısaltır.",
            ornek(
                "$\\log_2 5+\\log_4 25+\\log_8 125$ ifadesi verilsin.",
                "İfadeyi tek bir logaritma olarak yazalım.",
                "$\\log_4 25=\\log_{2^2} 5^2=\\log_2 5$ ve $\\log_8 125=\\log_{2^3} 5^3=\\log_2 5$ olur.",
                "Toplam $3\\log_2 5=\\log_2 125$ olur."),
        ]},
        {"baslik": "Kurallarla denkleme giriş", "icerik": [
            "Logaritma kuralları denklem çözerken de kullanılır: birden fazla logaritma tek bir logaritmada toplanır, sonra tanım uygulanır. Bulunan köklerin tanım koşullarını sağlayıp sağlamadığı mutlaka kontrol edilmelidir.",
            ornek(
                "$\\log_2 x+\\log_2(x-2)=3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Çarpım kuralıyla $\\log_2(x(x-2))=3$, yani $x^2-2x=8$ ve $(x-4)(x+2)=0$.",
                "$x=-2$ logaritmayı tanımsız yaptığı için atılır; çözüm $x=4$ tür."),
            "Denklem çözme yöntemlerinin tamamı için <a href=\"/blog/logaritmik-denklemler/\">Logaritmik Denklemler Nasıl Çözülür?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kuralların özeti", "icerik": [
            tablo(["Kural", "Formül"], [
                ["Çarpım", "$\\log_a(xy)=\\log_a x+\\log_a y$"],
                ["Bölüm", "$\\log_a \\dfrac{x}{y}=\\log_a x-\\log_a y$"],
                ["Kuvvet", "$\\log_a x^n=n\\log_a x$"],
                ["Tabanın kuvveti", "$\\log_{a^m} b^n=\\dfrac{n}{m}\\log_a b$"],
                ["Taban değiştirme", "$\\log_a b=\\dfrac{\\log_c b}{\\log_c a}$"],
                ["Ters çevirme", "$\\log_a b \\cdot \\log_b a=1$"],
                ["Zincir", "$\\log_a b \\cdot \\log_b c=\\log_a c$"],
                ["Logaritmalı üs", "$a^{\\log_a b}=b$"],
            ]),
            "Tablodaki her kural, logaritmanın bir üs olduğu gerçeğinden türetilebilir. Bir kural akla gelmediğinde ifadeyi üslü biçime çevirip üs kurallarını uygulamak her zaman işe yarar.",
        ]},
        {"baslik": "Sınavda logaritma kuralları", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) logaritma kuralları; ifade sadeleştirme, harfle verilen logaritmalar, taban değiştirme, zincir kuralı ve logaritmalı üsler biçiminde karşına çıkabilir.",
                "Kurallar logaritmalı denklem ve eşitsizlik sorularının da ilk adımıdır."),
            "Sadeleştirme sorusunda önce bütün katsayıları üsse taşı, sonra toplamları ve farkları tek bir logaritmada birleştir. Farklı tabanlar varsa ortak tabana getirmeyi, harfle verilen sorularda ise sayıyı asal çarpanlarına ayırmayı dene.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\log(x+y)=\\log x+\\log y$", "Toplamın logaritması için kural yok"],
                ["$\\log x \\cdot \\log y=\\log(xy)$", "Çarpımın logaritması toplamdır"],
                ["$\\dfrac{\\log x}{\\log y}=\\log \\dfrac{x}{y}$", "Bölüm taban değiştirmedir"],
                ["$(\\log x)^2=2\\log x$", "Kuvvet kuralı yalnız $\\log x^2$ için"],
                ["Tabanın kuvvetinde üssü çarpmak", "Tabandaki üs bölen olur"],
                ["Denklemde tanım koşulunu kontrol etmemek", "Kökler denenir"],
            ]),
            "Bu hataların çoğu kuralların yönünü karıştırmaktan doğar. Kural, logaritmanın içindeki işlemi dışarıdaki başka bir işleme çevirir; içeride toplama varsa hiçbir kural uygulanamaz.",
        ]},
    ],
    "sss": [
        ("Logaritmada çarpım kuralı nedir?",
         "Çarpımın logaritması logaritmaların toplamıdır: log a tabanında xy eşittir log a x artı log a y."),
        ("Logaritmada kuvvet kuralı nedir?",
         "Bir kuvvetin logaritmasında üs, logaritmanın önüne katsayı olarak iner: log a x üzeri n eşittir n çarpı log a x."),
        ("Taban değiştirme formülü nedir?",
         "log a b, istenen bir c tabanında log c b nin log c a ya bölümüne eşittir. Hesap makinesiyle farklı tabanlı logaritma bu formülle hesaplanır."),
        ("log(x + y) nasıl açılır?",
         "Toplamın logaritması için bir kural yoktur. log(x + y), log x artı log y ye eşit değildir."),
        ("log 5 kaçtır?",
         "log 5 eşittir 1 eksi log 2 dir. log 2 yaklaşık 0.301 olduğundan log 5 yaklaşık 0.699 olur."),
        ("Zincir kuralı nedir?",
         "Birinin sayısı diğerinin tabanı olan logaritmalar çarpılınca aradaki sayı sadeleşir: log a b çarpı log b c eşittir log a c."),
        ("Logaritma kuralları nereden gelir?",
         "Logaritma bir üs olduğu için kurallar üs kurallarından gelir. Kuvvetler çarpılırken üsler toplandığı için çarpımın logaritması logaritmaların toplamıdır; bölme ve kuvvet kuralları da aynı yolla elde edilir."),
    ],
    "kontrol": [
        "Logaritma kurallarının üs kurallarından geldiğini açıklayabiliyorum.",
        "Çarpım ve bölüm kurallarını kullanabiliyorum.",
        "Kuvvet kuralını kökler dahil uygulayabiliyorum.",
        "Tabanın kuvveti kuralını kullanabiliyorum.",
        "Taban değiştirme formülünü ispatlayıp kullanabiliyorum.",
        "Ters çevirme ve zincir kurallarını uygulayabiliyorum.",
        "Logaritmalı üsleri sadeleştirebiliyorum.",
        "Yaklaşık değerlerle ve harfle verilen logaritmalarla hesap yapabiliyorum.",
        "Birden fazla kuralla uzun ifadeleri sadeleştirebiliyorum.",
        "Sık yapılan hataları tanıyıp kaçınabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["logaritma-konu-anlatimi", "logaritmik-denklemler", "uslu-sayilar-konu-anlatimi-pdf"],
}
