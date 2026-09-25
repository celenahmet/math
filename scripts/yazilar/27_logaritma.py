# scripts/yazilar/27_logaritma.py — Logaritma Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402


def _log(taban, alt=None):
    return lambda x: math.log(x, taban) if x > 0 and (alt is None or x >= alt) else None


YAZI = {
    "slug": "logaritma-konu-anlatimi",
    "baslik": "Logaritma Konu Anlatımı",
    "aciklama": "Logaritma nedir? Üslü ifadeden logaritmaya geçiş, tanım koşulları, temel değerler, onluk ve doğal logaritma, logaritma grafiği ve uygulamalar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "logaritma",
    "sinavlar": ["AYT"],
    "kapak": "logaritma-konu-anlatimi",
    "kapak_alt": "Logaritma konu anlatımı: katlanarak yükselen ahşap blok kulelerini şeffaf bir kemerle eşit adımlı basamaklara dönüştüren öğrenci",
    "ozet": "Logaritma, bir sayının belirli bir tabanın kaçıncı kuvveti olduğunu söyleyen işlemdir ve üs almanın tersidir. Katlanarak büyüyen nicelikleri eşit adımlarla ölçmeyi sağladığı için fen bilimlerinden finansa kadar pek çok alanda kullanılır. Bu yazıda üslü ifadeden logaritmaya geçişi, logaritmanın tanımını ve tanımlı olma koşullarını, temel değerleri, onluk ve doğal logaritmayı, tanım kümesi sorularını, logaritma fonksiyonunun grafiğini ve özelliklerini, logaritmalı sayıları karşılaştırmayı, basamak sayısı hesabını ve günlük hayattan uygulamaları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Logaritma nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için üslü sayıları ve ters fonksiyon kavramını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı</a> ve <a href=\"/blog/ters-fonksiyon/\">Ters Fonksiyon</a> yazılarına göz at."),
            "Üslü sayılarda taban ve üs verilir, sonuç hesaplanır: $2^3=8$. Logaritma ise ters soruyu sorar: $2$ nin kaçıncı kuvveti $8$ eder? Cevap $3$ tür ve bu durum $\\log_2 8=3$ biçiminde yazılır. Kısacası logaritma, bir üssü bulma işlemidir.",
            "Kapaktaki öğrenci her adımda iki katına çıkan blok kulelerini şeffaf bir kemerin altından geçirerek eşit adımlarla yükselen küçük basamaklara çeviriyor. Logaritmanın yaptığı iş budur: katlanarak büyüyen değerleri, kaç adımda büyüdüklerini gösteren eşit aralıklı sayılara dönüştürür.",
        ]},
        {"baslik": "Logaritmanın tanımı", "icerik": [
            "$a$ pozitif ve $1$ den farklı bir sayı, $b$ pozitif bir sayı olmak üzere $a^x=b$ eşitliğini sağlayan $x$ sayısına $b$ nin $a$ tabanına göre logaritması denir:",
            "$$a^x=b \\Leftrightarrow \\log_a b=x$$",
            "Bu eşdeğerlik, logaritma sorularının neredeyse tamamında kullanılır. Bir logaritmanın değerini bulmak için ifade üslü biçime çevrilir; üslü bir denklemi çözmek için ise logaritma biçimine geçilir.",
            hap("Logaritma bir üstür.",
                "$\\log_a b$ sorusu, $a$ nın kaçıncı kuvvetinin $b$ ettiğini sorar."),
        ]},
        {"baslik": "Tanımlı olma koşulları", "icerik": [
            "Logaritmanın tanımlı olması için hem tabana hem de logaritması alınan sayıya koşullar konur. Her koşulun bir nedeni vardır:",
            tablo(["Koşul", "Neden?"], [
                ["Taban pozitif: $a>0$", "Negatif tabanın kesirli kuvvetleri gerçek sayı olmayabilir"],
                ["Taban $1$ den farklı: $a \\neq 1$", "$1$ in her kuvveti $1$ dir; başka sayıya ulaşılamaz"],
                ["Sayı pozitif: $b>0$", "Pozitif tabanın her kuvveti pozitiftir"],
            ]),
            "Bu yüzden $\\log_2(-8)$, $\\log_2 0$ ya da $\\log_1 5$ gibi ifadeler tanımsızdır. Logaritma içeren her soruda, hesaba başlamadan önce bu üç koşul kontrol edilmelidir.",
        ]},
        {"baslik": "Logaritma değeri hesaplamak", "icerik": [
            "Logaritmanın değerini bulmak için sayı, tabanın bir kuvveti olarak yazılır. Sayı tabanın kesirli ya da negatif kuvvetiyse üs kuralları kullanılır:",
            tablo(["İfade", "Üslü yazım", "Değer"], [
                ["$\\log_2 32$", "$2^5=32$", "$5$"],
                ["$\\log_3 81$", "$3^4=81$", "$4$"],
                ["$\\log_5 \\dfrac{1}{25}$", "$5^{-2}=\\dfrac{1}{25}$", "$-2$"],
                ["$\\log_9 3$", "$9^{1/2}=3$", "$\\dfrac{1}{2}$"],
                ["$\\log_{1/2} 8$", "$\\left(\\dfrac{1}{2}\\right)^{-3}=8$", "$-3$"],
            ]),
            ornek(
                "$\\log_4 8$ ifadesi verilsin.",
                "Değerini bulalım.",
                "$4^x=8$ yazılır; iki taraf $2$ tabanına çevrilir: $2^{2x}=2^3$.",
                "$2x=3$, yani $\\log_4 8=\\dfrac{3}{2}$ olur."),
        ]},
        {"baslik": "Köklü ve kesirli sayıların logaritması", "icerik": [
            "Kök ve kesir içeren sayılar önce üslü biçimde yazılır: $\\sqrt{a}=a^{1/2}$ ve $\\dfrac{1}{a}=a^{-1}$. Taban köklü olduğunda da aynı yol izlenir; taban ve sayı ortak bir asal tabana çevrilir, sonra üsler eşitlenir.",
            ornek(
                "$\\log_2 \\sqrt{8}$, $\\log_3 \\dfrac{1}{\\sqrt{3}}$ ve $\\log_{\\sqrt{2}} 4$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$\\sqrt{8}=2^{3/2}$ olduğundan birincisi $\\dfrac{3}{2}$ olur; $\\dfrac{1}{\\sqrt{3}}=3^{-1/2}$ olduğundan ikincisi $-\\dfrac{1}{2}$ olur.",
                "$(\\sqrt{2})^x=4$ ise $2^{x/2}=2^2$, yani $x=4$ olur."),
        ]},
        {"baslik": "Temel değerler", "icerik": [
            "Tanımdan doğrudan çıkan dört eşitlik, logaritma hesaplarının en sık kullanılan araçlarıdır:",
            tablo(["Eşitlik", "Neden?"], [
                ["$\\log_a 1=0$", "$a^0=1$"],
                ["$\\log_a a=1$", "$a^1=a$"],
                ["$\\log_a a^x=x$", "Tanımın kendisi"],
                ["$a^{\\log_a b}=b$", "Üs, tabanın $b$ yi veren kuvvetidir"],
            ]),
            "Son iki eşitlik, logaritma ile üs almanın birbirinin tersi olduğunu gösterir: biri diğerinin yaptığını geri alır. Örneğin $5^{\\log_5 7}=7$ ve $\\log_3 3^{10}=10$ olur.",
            hap("$\\log_a 1=0$ ve $\\log_a a=1$ olur.", "$a^{\\log_a b}=b$ eşitliği, logaritma ile üs almanın birbirinin tersi olduğunu gösterir."),
        ]},
        {"baslik": "Logaritmanın işareti", "icerik": [
            "Bir logaritmanın pozitif mi negatif mi olduğu, hesaplamadan önce taban ve sayının $1$ e göre konumundan anlaşılır. Taban ve sayı $1$ in aynı tarafındaysa logaritma pozitif, farklı taraflarındaysa negatiftir.",
            tablo(["Taban", "Sayı", "İşaret"], [
                ["$a>1$", "$b>1$", "Pozitif"],
                ["$a>1$", "$0<b<1$", "Negatif"],
                ["$0<a<1$", "$0<b<1$", "Pozitif"],
                ["$0<a<1$", "$b>1$", "Negatif"],
            ]),
            "Örneğin $\\log_2 \\dfrac{1}{3}$ negatiftir, $\\log_{1/3} \\dfrac{1}{9}=2$ pozitiftir ve $\\log_{1/2} 5$ negatiftir. Karşılaştırma sorularında önce işaretlere bakmak, sayıları çoğu zaman hesap yapmadan gruplara ayırır.",
            hap("Taban ve sayı $1$ in aynı tarafındaysa logaritma pozitif, farklı taraflarındaysa negatiftir."),
        ]},
        {"baslik": "Logaritmalı üsler", "icerik": [
            "Üssünde logaritma bulunan ifadelerde $a^{\\log_a b}=b$ eşitliği kullanılır. Üs bir toplam ise önce üs kuralıyla parçalara ayrılır; taban logaritmanın tabanının kuvvetiyse önce ortak tabana çevrilir.",
            ornek(
                "$2^{\\log_2 3+1}$, $10^{2+\\log 5}$ ve $9^{\\log_3 5}$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$2^{\\log_2 3} \\cdot 2^1=3 \\cdot 2=6$ ve $10^2 \\cdot 10^{\\log 5}=100 \\cdot 5=500$ olur.",
                "$9^{\\log_3 5}=(3^2)^{\\log_3 5}=(3^{\\log_3 5})^2=5^2=25$ olur."),
        ]},
        {"baslik": "Onluk ve doğal logaritma", "icerik": [
            "İki taban o kadar sık kullanılır ki kendilerine özel yazımları vardır. Tabanı $10$ olan logaritmaya <strong>onluk logaritma</strong> denir ve taban yazılmaz: $\\log 1000=3$. Tabanı $e$ sayısı olan logaritmaya <strong>doğal logaritma</strong> denir ve $\\ln$ ile gösterilir.",
            "$e$ sayısı yaklaşık $2.718$ olan irrasyonel bir sayıdır ve sürekli büyüme hesaplarında, türev ve integral konularında doğal olarak ortaya çıkar. Doğal logaritmada da temel değerler geçerlidir: $\\ln 1=0$, $\\ln e=1$ ve $e^{\\ln 5}=5$.",
            tablo(["Yazım", "Anlamı"], [
                ["$\\log x$", "$\\log_{10} x$"],
                ["$\\ln x$", "$\\log_e x$"],
            ]),
        ]},
        {"baslik": "Üslü denklemden logaritmaya", "icerik": [
            "Bir üslü denklemde bilinmeyen üsteyse ve iki taraf aynı tabana getirilemiyorsa çözüm logaritma ile yazılır. Sonuç bir tam sayı değildir, ama hangi iki tam sayı arasında olduğu kolayca bulunur.",
            ornek(
                "$3^x=7$ denklemi verilsin.",
                "Çözümü yazalım ve hangi tam sayılar arasında olduğunu bulalım.",
                "Tanımdan $x=\\log_3 7$ olur.",
                "$3^1=3<7<9=3^2$ olduğundan $x$, $1$ ile $2$ arasındadır."),
            ornek(
                "$\\log_2 20$ ifadesi verilsin.",
                "Değerin hangi iki ardışık tam sayı arasında olduğunu bulalım.",
                "$2^4=16$ ve $2^5=32$ dir.",
                "$16<20<32$ olduğundan $\\log_2 20$, $4$ ile $5$ arasındadır."),
        ]},
        {"baslik": "İç içe logaritma", "icerik": [
            "İç içe logaritmalar içten dışa doğru hesaplanır. Her adımda elde edilen sayı bir sonraki logaritmanın içine yazılır.",
            ornek(
                "$\\log_2(\\log_3 81)$ ifadesi verilsin.",
                "Değerini bulalım.",
                "İçteki logaritma: $\\log_3 81=4$.",
                "Dıştaki logaritma: $\\log_2 4=2$ olur."),
            ornek(
                "$\\log_2(\\log_3 x)=1$ olsun.",
                "$x$ i bulalım.",
                "Dıştan içe tanım uygulanır: $\\log_3 x=2^1=2$.",
                "Buradan $x=3^2=9$ olur."),
        ]},
        {"baslik": "Tabanı bilinmeyen logaritma", "icerik": [
            "Tabanda bilinmeyen varsa ifade yine üslü biçime çevrilir. Bulunan değerlerden tabanın pozitif ve $1$ den farklı olma koşulunu sağlamayanlar atılır.",
            ornek(
                "$\\log_x 49=2$ ve $\\log_y 8=\\dfrac{3}{2}$ eşitlikleri verilsin.",
                "$x$ ve $y$ yi bulalım.",
                "$x^2=49$ olduğundan $x=7$ ya da $x=-7$; taban pozitif olmalı, $x=7$ olur.",
                "$y^{3/2}=8$ ise $y=8^{2/3}=4$ olur."),
        ]},
        {"baslik": "Tanım kümesi", "icerik": [
            "Logaritmalı bir fonksiyonun tanım kümesi bulunurken tabanın pozitif ve $1$ den farklı, logaritması alınan ifadenin ise pozitif olması istenir. Bu koşulların ortak çözümü tanım kümesini verir.",
            ornek(
                "$f(x)=\\log_{x-1}(5-x)$ fonksiyonu verilsin.",
                "Tanım kümesini ve bu kümedeki tam sayıları bulalım.",
                "$x-1>0$ ve $x-1 \\neq 1$ koşullarından $x>1$ ve $x \\neq 2$; $5-x>0$ koşulundan $x<5$.",
                "Tanım kümesi $(1, 2) \\cup (2, 5)$ olur; içindeki tam sayılar $3$ ve $4$ tür."),
            ornek(
                "$g(x)=\\log(x^2-4)$ fonksiyonu verilsin.",
                "Tanım kümesini bulalım.",
                "$x^2-4>0$ olmalıdır, yani $(x-2)(x+2)>0$.",
                "Tanım kümesi $(-\\infty, -2) \\cup (2, \\infty)$ olur."),
            hap("Tanım kümesi için taban pozitif ve $1$ den farklı, logaritması alınan ifade pozitif olmalıdır."),
        ]},
        {"baslik": "Logaritma fonksiyonunun grafiği", "icerik": [
            "$f(x)=\\log_a x$ fonksiyonu, $g(x)=a^x$ üstel fonksiyonunun tersidir. Ters fonksiyonların grafikleri $y=x$ doğrusuna göre simetrik olduğundan logaritma grafiği, üstel grafiğin bu doğruya göre yansımasıdır.",
            koordinat_grafik("y = 2ˣ ve y = log2 x grafikleri", [("y = 2ˣ", lambda x: 2 ** x), ("y = log2 x", _log(2)), ("y = x", lambda x: x)],
                             (-3, 5), (-3, 5), adim=1, noktalar=[(1, 0, "", True), (0, 1, "", True), (2, 1, "", True), (1, 2, "", True)]),
            "Grafikte üstel eğri $(0, 1)$ noktasından, logaritma eğrisi ise onun yansıması olan $(1, 0)$ noktasından geçer. Aynı şekilde $(1, 2)$ noktası $(2, 1)$ noktasına yansır: $2^1=2$ ve $\\log_2 2=1$.",
        ]},
        {"baslik": "Grafiğin özellikleri", "icerik": [
            "Logaritma fonksiyonunun grafiği tabanın değerine göre iki biçimde olur, ama bazı özellikler her iki durumda da aynıdır:",
            tablo(["Özellik", "$y=\\log_a x$"], [
                ["Tanım kümesi", "$(0, \\infty)$"],
                ["Görüntü kümesi", "Tüm gerçek sayılar"],
                ["Geçtiği nokta", "$(1, 0)$"],
                ["Asimptot", "Dikey eksen, $x=0$"],
                ["$a>1$ iken", "Artan"],
                ["$0<a<1$ iken", "Azalan"],
            ]),
            "Grafik dikey eksene sonsuz yaklaşır ama onu hiç kesmez; çünkü $0$ ve negatif sayıların logaritması tanımsızdır. Buna karşın grafik sağa doğru sınırsız yükselir, ama bu yükseliş çok yavaştır: $\\log_2 x$ in $10$ a ulaşması için $x$ in $1024$ olması gerekir. Bu yavaş büyüme, logaritmanın çok büyük sayıları küçük ve kolay yönetilen değerlere çevirmesinin temel nedenidir.",
        ]},
        {"baslik": "Tabanı 1 den küçük logaritma", "icerik": [
            "Taban $0$ ile $1$ arasındaysa logaritma fonksiyonu azalandır. $\\log_{1/2} x=-\\log_2 x$ olduğu için bu grafik, $\\log_2 x$ grafiğinin yatay eksene göre yansımasıdır.",
            koordinat_grafik("y = log2 x ve y = log1/2 x grafikleri", [("y = log2 x", _log(2, 0.125)), ("y = log1/2 x", _log(0.5, 0.125))],
                             (-1, 8), (-4, 4.5), adim=1, noktalar=[(1, 0, "", True), (4, 2, "", True), (4, -2, "", True)]),
            "İki grafik $(1, 0)$ noktasında kesişir. $x=4$ için biri $2$, diğeri $-2$ değerini alır: $\\log_2 4=2$ ve $\\log_{1/2} 4=-2$.",
        ]},
        {"baslik": "Logaritmalı sayıları karşılaştırmak", "icerik": [
            "Taban $1$ den büyükse logaritma artan olduğu için büyük sayının logaritması da büyüktür. Aynı sayının farklı tabanlardaki logaritmaları karşılaştırılırken ise tersine bir durum vardır: taban büyüdükçe aynı sayıya ulaşmak için daha küçük bir üs yeter.",
            ornek(
                "$a=\\log_2 10$, $b=\\log_3 10$ ve $c=\\log_5 10$ sayıları verilsin.",
                "Sayıları sıralayalım.",
                "$2^3=8<10<16=2^4$, $3^2=9<10<27=3^3$ ve $5^1=5<10<25=5^2$ olduğundan $a$, $3$ ile $4$; $b$, $2$ ile $3$; $c$, $1$ ile $2$ arasındadır.",
                "Sıralama $c<b<a$ olur."),
        ]},
        {"baslik": "Logaritmalı eşitsizliklere giriş", "icerik": [
            "Logaritma fonksiyonunun artan ya da azalan olması, eşitsizlik çözerken yönü belirler. Taban $1$ den büyükse eşitsizliğin yönü korunur, taban $0$ ile $1$ arasındaysa yön değişir. Her durumda logaritması alınan ifadenin pozitif olması ayrıca istenir.",
            ornek(
                "$\\log_2 x>3$ ve $\\log_{1/2} x>3$ eşitsizlikleri verilsin.",
                "Çözüm kümelerini bulalım.",
                "Birincide taban $1$ den büyüktür: $x>2^3=8$.",
                "İkincide taban $1$ den küçüktür, yön değişir: $x<\\dfrac{1}{8}$; pozitiflik koşuluyla çözüm $0<x<\\dfrac{1}{8}$ olur."),
        ]},
        {"baslik": "Logaritma fonksiyonunun tersi", "icerik": [
            "Logaritmalı bir fonksiyonun tersi, $y$ yalnız bırakılıp logaritma üslü biçime çevrilerek bulunur. Tersine, üstel bir fonksiyonun tersi logaritmalı bir fonksiyondur.",
            ornek(
                "$f(x)=\\log_3(x-1)+2$ fonksiyonu verilsin.",
                "Ters fonksiyonu bulalım.",
                "$y=\\log_3(x-1)+2$ ise $y-2=\\log_3(x-1)$, yani $x-1=3^{y-2}$.",
                "Değişkenler yer değiştirince $f^{-1}(x)=3^{x-2}+1$ olur."),
            "Kontrol için $f(4)=\\log_3 3+2=3$ ve $f^{-1}(3)=3^1+1=4$ hesaplanabilir; fonksiyon ile tersi birbirini geri alır.",
        ]},
        {"baslik": "Kuralların önizlemesi", "icerik": [
            "Logaritma üs almanın tersi olduğu için üs kuralları logaritmada yeni kurallara dönüşür. Çarpımın logaritması toplam, bölümün logaritması fark, kuvvetin logaritması ise çarpım olur:",
            tablo(["Üs kuralı", "Logaritma kuralı"], [
                ["$a^m \\cdot a^n=a^{m+n}$", "$\\log_a(xy)=\\log_a x+\\log_a y$"],
                ["$\\dfrac{a^m}{a^n}=a^{m-n}$", "$\\log_a \\dfrac{x}{y}=\\log_a x-\\log_a y$"],
                ["$(a^m)^n=a^{mn}$", "$\\log_a x^n=n\\log_a x$"],
            ]),
            "Bu kuralların ispatı, taban değiştirme formülü ve çok sayıda örnek <a href=\"/blog/logaritma-kurallari-formulleri/\">Logaritma Kuralları ve Formülleri</a> yazısında.",
        ]},
        {"baslik": "Basamak sayısı", "icerik": [
            "Onluk logaritma, büyük bir sayının kaç basamaklı olduğunu hesaplamadan bulmayı sağlar. $n$ basamaklı bir pozitif tam sayı $10^{n-1}$ ile $10^n$ arasındadır; bu yüzden logaritmasının tam kısmı $n-1$ dir. Basamak sayısı, logaritmanın tam kısmının bir fazlasıdır.",
            ornek(
                "$\\log 2 \\approx 0.30103$ olduğu biliniyor.",
                "$2^{100}$ sayısının kaç basamaklı olduğunu bulalım.",
                "$\\log 2^{100}=100\\log 2 \\approx 30.103$ olur.",
                "Tam kısım $30$ olduğundan sayı $31$ basamaklıdır."),
        ]},
        {"baslik": "Uygulama: pH değeri", "icerik": [
            "Kimyada bir çözeltinin asitliği pH ile ölçülür ve $\\text{pH}=-\\log[\\text{H}^+]$ formülüyle hesaplanır; burada $[\\text{H}^+]$ hidrojen iyonu derişimidir. Derişim $10$ kat artınca pH yalnızca $1$ azalır; logaritma, çok geniş bir aralığa yayılan derişimleri $0$ ile $14$ arasındaki kullanışlı bir ölçeğe sıkıştırır.",
            ornek(
                "Bir çözeltide $[\\text{H}^+]=10^{-3}$ mol bölü litre olsun.",
                "pH değerini ve derişim $10$ katına çıkarsa yeni pH değerini bulalım.",
                "$\\text{pH}=-\\log 10^{-3}=3$ olur.",
                "Derişim $10^{-2}$ olursa $\\text{pH}=2$ olur; pH $1$ azalmıştır."),
        ]},
        {"baslik": "Uygulama: katlanarak büyüme", "icerik": [
            "Her adımda sabit bir katla büyüyen bir niceliğin belirli bir değere kaç adımda ulaşacağı logaritma ile bulunur. Bakteri üremesi, bileşik faiz ve bilgisayar biliminde ikili arama bu türden sorulardır.",
            ornek(
                "Bir bakteri kolonisi her saat iki katına çıkıyor.",
                "Kolonin başlangıçtakinin $1024$ katına kaç saatte ulaşacağını bulalım.",
                "$2^t=1024$ denklemi yazılır; $t=\\log_2 1024$.",
                "$2^{10}=1024$ olduğundan $t=10$ saat bulunur."),
            "Aynı fikir ikili aramada da görülür: sıralı $1024$ elemanlı bir listede her adımda aranan aralık yarıya indiği için en fazla $10$ adımda sonuca ulaşılır. Logaritma, bu yüzden bilgisayar biliminde algoritmaların hızını ölçmede de temel bir araçtır.",
            hap("Her gün iki katına çıkan bir paylaşım bir kişiden başlayıp $1000$ kişiyi onuncu günde geçer: $2^9=512$ ve $2^{10}=1024$ olur.", "Bu gün sayısı, $\\log_2 1000$ değerinin yukarı yuvarlanmasıdır.", gunluk=True),
        ]},
        {"baslik": "Sınavda logaritma", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) logaritma; değer hesaplama, tanım kümesi, iç içe logaritma, karşılaştırma, grafik ve ters fonksiyon biçiminde karşına çıkabilir.",
                "Logaritma kuralları ve logaritmalı denklemler bu konunun devamıdır ve sık sorulur."),
            "Logaritma sorusuna başlarken önce tanım koşullarını yaz, sonra ifadeyi üslü biçime çevir. Değer hesaplarında sayıyı tabanın kuvveti olarak yazmak, karşılaştırma sorularında ise değerleri iki ardışık tam sayı arasına yerleştirmek çoğu zaman yeterlidir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\log_2 8=4$ sanmak", "$2^3=8$, değer $3$"],
                ["Negatif sayının logaritmasını almak", "Sayı pozitif olmalı"],
                ["Tabanı $1$ almak", "Taban $1$ den farklı olmalı"],
                ["Tanım kümesinde tabanı unutmak", "Taban da koşul verir"],
                ["$0<a<1$ iken eşitsizlik yönünü korumak", "Yön değişir"],
                ["$\\log 0=0$ yazmak", "$\\log 0$ tanımsızdır"],
            ]),
            "Hataların çoğu logaritmanın bir üs olduğunu unutmaktan doğar. Şüpheye düştüğünde ifadeyi $a^x=b$ biçimine çevirip denetlemek doğru sonucu hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Logaritma nedir?",
         "Bir sayının belirli bir tabanın kaçıncı kuvveti olduğunu söyleyen işlemdir. log2 8 eşittir 3 çünkü 2 nin küpü 8 dir."),
        ("Logaritmada taban neden 1 olamaz?",
         "1 in her kuvveti 1 olduğu için 1 tabanıyla başka bir sayıya ulaşılamaz. Bu yüzden taban pozitif ve 1 den farklı olmalıdır."),
        ("Negatif sayının logaritması alınır mı?",
         "Hayır. Pozitif bir tabanın her kuvveti pozitif olduğu için logaritması alınan sayı pozitif olmalıdır."),
        ("log ve ln arasındaki fark nedir?",
         "log onluk logaritmadır, tabanı 10 dur. ln doğal logaritmadır, tabanı yaklaşık 2.718 olan e sayısıdır."),
        ("Logaritma fonksiyonunun grafiği hangi noktadan geçer?",
         "Her tabanda logaritma grafiği (1, 0) noktasından geçer; çünkü her tabanın sıfırıncı kuvveti 1 dir."),
        ("Bir sayının basamak sayısı logaritma ile nasıl bulunur?",
         "Sayının onluk logaritmasının tam kısmına 1 eklenir. Örneğin 2 üzeri 100 sayısı 31 basamaklıdır."),
        ("log 1000 kaçtır?",
         "10 un küpü 1000 olduğu için log 1000 eşittir 3 tür. Onluk logaritmada 10 un kuvvetlerinin logaritması doğrudan üs olarak okunur."),
        ("Logaritma fonksiyonu artan mıdır?",
         "Taban 1 den büyükse artan, taban 0 ile 1 arasındaysa azalandır. Bu durum logaritmalı eşitsizliklerde yönün korunup korunmayacağını belirler."),
    ],
    "kontrol": [
        "Logaritmanın üs almanın tersi olduğunu açıklayabiliyorum.",
        "Üslü ifade ile logaritma arasında geçiş yapabiliyorum.",
        "Tanımlı olma koşullarını ve nedenlerini söyleyebiliyorum.",
        "Logaritma değerlerini tabanın kuvvetiyle hesaplayabiliyorum.",
        "Temel değerleri, onluk ve doğal logaritmayı kullanabiliyorum.",
        "Logaritmalı fonksiyonların tanım kümesini bulabiliyorum.",
        "Logaritma fonksiyonunun grafiğini ve özelliklerini açıklayabiliyorum.",
        "Logaritmalı sayıları karşılaştırabiliyorum.",
        "Logaritmalı fonksiyonun tersini bulabiliyorum.",
        "Basamak sayısı ve büyüme problemlerini logaritma ile çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["logaritma-kurallari-formulleri", "logaritmik-denklemler", "uslu-sayilar-konu-anlatimi-pdf"],
}
