# scripts/yazilar/10_carpanlara_ayirma.py — Polinomlarda Carpanlara Ayirma (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "polinomlarda-carpanlara-ayirma",
    "baslik": "Polinomlarda Çarpanlara Ayırma",
    "aciklama": "Polinomlar nasıl çarpanlarına ayrılır? Ortak çarpan, gruplama, iki kare farkı, tam kare, küp özdeşlikleri, üç terimliler, kök deneme ve sadeleştirme; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "polinomlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "polinomlarda-carpanlara-ayirma",
    "kapak_alt": "Polinomlarda çarpanlara ayırma: renkli karoları bir dikdörtgen alan modeline yerleştiren iki öğrenci",
    "ozet": "Çarpanlara ayırma, bir polinomu daha basit polinomların çarpımı olarak yazmaktır. Denklem çözmenin, kesirli ifadeleri sadeleştirmenin ve polinomun köklerini bulmanın yolu buradan geçer. Bu yazıda ortak çarpan parantezini, gruplamayı, iki kare farkını, tam kare ve küp özdeşliklerini, ikinci dereceden üç terimlileri, değişken değiştirmeyi, terim ekleyip çıkarmayı, çarpan teoremiyle kök denemeyi, sadeleştirmeyi ve denklem çözmeyi çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Çarpanlara ayırma nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için polinomlarda çarpmayı, özdeşlikleri ve kalan teoremini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/polinomlar-konu-anlatimi/\">Polinomlar Konu Anlatımı</a> ve <a href=\"/blog/polinomlarda-kalan/\">Polinomlarda Kalan Bulma</a> yazılarına göz at."),
            "Bir polinomu, dereceleri daha küçük polinomların çarpımı olarak yazmaya <strong>çarpanlara ayırma</strong> denir. Çarpanlara ayırma, çarpma işleminin tersidir: çarpmada parantezler açılır, çarpanlara ayırmada parantezler geri kurulur.",
            "Kapaktaki öğrenciler bunu alan modeliyle yapıyor: $x^2+5x+6$ ifadesini oluşturan karolar, kenarları $x+2$ ve $x+3$ olan bir dikdörtgene diziliyor. Dikdörtgenin alanı kenarlarının çarpımı olduğu için $x^2+5x+6=(x+2)(x+3)$ yazılır.",
            hap("Çarpanlara ayırma, çarpmanın tersidir.",
                "Sonuç her zaman parantezler açılarak kontrol edilir."),
        ]},
        {"baslik": "Neden çarpanlara ayırırız?", "icerik": [
            "Çarpım biçimindeki bir ifade, toplam biçimindekinden çok daha fazla bilgi verir. Bir çarpımın sıfır olması için çarpanlardan birinin sıfır olması yeter; bu yüzden çarpanlara ayrılmış bir polinomun kökleri doğrudan okunur.",
            tablo(["Amaç", "Çarpanlara ayırmanın katkısı"], [
                ["Denklem çözmek", "Her çarpan ayrı ayrı sıfıra eşitlenir"],
                ["Kesirli ifadeyi sadeleştirmek", "Ortak çarpanlar sadeleşir"],
                ["Kökleri bulmak", "Çarpanlar kökleri gösterir"],
                ["İşaret incelemek", "Her çarpanın işareti ayrı incelenir"],
                ["Hızlı hesap yapmak", "Sayısal işlemler kısalır"],
            ]),
        ]},
        {"baslik": "Alan modeliyle çarpanlara ayırma", "icerik": [
            "Alan modeli, çarpanlara ayırmanın geometrik anlamını gösterir. Kenarı $x$ olan büyük kare $x^2$ yi, kenarları $x$ ve $1$ olan şerit $x$ i, kenarı $1$ olan küçük kare $1$ i temsil eder. Bir üç terimliye karşılık gelen karolar boşluksuz bir dikdörtgene dizilebiliyorsa dikdörtgenin kenarları ifadenin çarpanlarıdır.",
            ornek(
                "$x^2+5x+6$ ifadesi karolarla gösterilsin: bir büyük kare, beş şerit ve altı küçük kare.",
                "Karoları dikdörtgene dizip çarpanları bulalım.",
                "Büyük karenin bir yanına iki şerit, diğer yanına üç şerit konur; köşedeki boşluğu $2 \\cdot 3=6$ küçük kare doldurur.",
                "Dikdörtgenin kenarları $x+2$ ve $x+3$ tür: $x^2+5x+6=(x+2)(x+3)$."),
            "Model, iki sayı bulma yönteminin nedenini de açıklar: şeritler iki yana bölüştürülür ve toplamları $5$ tir; köşedeki küçük karelerin sayısı ise bu iki sayının çarpımıdır, yani $6$ dır.",
        ]},
        {"baslik": "Ortak çarpan parantezi", "icerik": [
            "Çarpanlara ayırmada ilk bakılacak şey, bütün terimlerde ortak olan bir çarpanın bulunup bulunmadığıdır. Ortak çarpan, katsayıların en büyük ortak böleni ile değişkenin en küçük kuvvetinin çarpımıdır.",
            ornek(
                "$6x^3-9x^2$ ifadesi verilsin.",
                "İfadeyi çarpanlarına ayıralım.",
                "Katsayıların en büyük ortak böleni $3$, değişkenin en küçük kuvveti $x^2$ dir.",
                "$6x^3-9x^2=3x^2(2x-3)$."),
            dikkat(
                "Ortak çarpan parantezini atlayıp doğrudan özdeşlik aramak.",
                "$2x^2-18$ ifadesinde önce $2$ ortak çarpandır: $2(x^2-9)=2(x-3)(x+3)$. Ortak çarpan alınmadan iki kare farkı görülmez ve ayırma yarım kalır."),
        ]},
        {"baslik": "Gruplama", "icerik": [
            "Terimlerin hepsinde ortak bir çarpan yoksa terimler ikişerli gruplara ayrılır. Her grupta ortak çarpan alındıktan sonra gruplar arasında ortak bir parantez ortaya çıkıyorsa ifade çarpanlarına ayrılmış olur.",
            ornek(
                "$x^3+2x^2+3x+6$ ifadesi verilsin.",
                "İfadeyi gruplayarak çarpanlarına ayıralım.",
                "İlk iki terimden $x^2$, son iki terimden $3$ ortak çarpan alınır: $x^2(x+2)+3(x+2)$.",
                "$x+2$ ortak paranteze alınır: $(x+2)(x^2+3)$."),
            "Gruplama her zaman ilk denemede işlemez. Ortak parantez çıkmıyorsa terimlerin sırası değiştirilip başka ikililer denenir; dört terimli ifadelerde üç farklı gruplama vardır ve bunlardan biri genellikle sonuç verir.",
        ]},
        {"baslik": "İki kare farkı", "icerik": [
            "İki karenin farkı, bu karelerin tabanlarının farkı ile toplamının çarpımıdır. En sık kullanılan özdeşliktir ve ifade içinde gizli olduğunda bile aranmalıdır:",
            "$$a^2-b^2=(a-b)(a+b)$$",
            ornek(
                "$x^2-25$, $4x^2-9$ ve $x^4-16$ ifadeleri verilsin.",
                "İfadeleri çarpanlarına ayıralım.",
                "$x^2-25=(x-5)(x+5)$ ve $4x^2-9=(2x-3)(2x+3)$.",
                "$x^4-16=(x^2-4)(x^2+4)=(x-2)(x+2)(x^2+4)$."),
            dikkat(
                "İki kare toplamını çarpanlarına ayırmaya çalışmak.",
                "$x^2+4$ gerçek sayılarda çarpanlarına ayrılmaz, çünkü $x^2+4$ hiçbir gerçek $x$ için sıfır olmaz. Bu yüzden $x^4-16$ nın son çarpanı $x^2+4$ olarak kalır."),
        ]},
        {"baslik": "Tam kare üç terimliler", "icerik": [
            "$a^2+2ab+b^2=(a+b)^2$ ve $a^2-2ab+b^2=(a-b)^2$ özdeşlikleri tersinden okunarak tam kare üç terimliler çarpanlarına ayrılır. Bir üç terimlinin tam kare olması için baştaki ve sondaki terimler kare, ortadaki terim de bunların tabanlarının çarpımının iki katı olmalıdır.",
            ornek(
                "$x^2+6x+9$ ve $4x^2-12x+9$ ifadeleri verilsin.",
                "İfadeleri çarpanlarına ayıralım.",
                "$x^2+6x+9$: kareler $x^2$ ve $9$; orta terim $2 \\cdot x \\cdot 3=6x$. Sonuç $(x+3)^2$.",
                "$4x^2-12x+9$: kareler $(2x)^2$ ve $3^2$; orta terim $2 \\cdot 2x \\cdot 3=12x$. Sonuç $(2x-3)^2$."),
        ]},
        {"baslik": "Küp toplamı ve farkı", "icerik": [
            "İki küpün toplamı ve farkı da çarpanlarına ayrılır. İkinci çarpan her iki durumda da üç terimlidir ve gerçek sayılarda daha fazla ayrılmaz:",
            "$$a^3-b^3=(a-b)(a^2+ab+b^2)$$",
            "$$a^3+b^3=(a+b)(a^2-ab+b^2)$$",
            ornek(
                "$x^3-27$ ve $8x^3+1$ ifadeleri verilsin.",
                "İfadeleri çarpanlarına ayıralım.",
                "$x^3-27=x^3-3^3=(x-3)(x^2+3x+9)$.",
                "$8x^3+1=(2x)^3+1^3=(2x+1)(4x^2-2x+1)$."),
            "İşaretleri hatırlamanın kısa yolu şudur: birinci çarpandaki işaret, ifadedeki işaretle aynıdır; ikinci çarpandaki orta terimin işareti bunun tersidir; son terim her zaman artıdır.",
        ]},
        {"baslik": "Tam küp", "icerik": [
            "$a^3+3a^2b+3ab^2+b^3=(a+b)^3$ ve $a^3-3a^2b+3ab^2-b^3=(a-b)^3$ özdeşlikleri de tersinden okunabilir. Dört terimli bir ifadenin katsayıları $1$, $3$, $3$, $1$ düzenini izliyorsa bir tam küp olabilir.",
            ornek(
                "$x^3+3x^2+3x+1$ ifadesi verilsin.",
                "İfadeyi çarpanlarına ayıralım.",
                "Katsayılar $1$, $3$, $3$, $1$ ve terimler $x$ ile $1$ in küp açılımına uyuyor.",
                "$x^3+3x^2+3x+1=(x+1)^3$."),
        ]},
        {"baslik": "x² + bx + c biçimindeki üç terimliler", "icerik": [
            "Baş katsayısı $1$ olan ikinci dereceden bir üç terimliyi çarpanlarına ayırmak için toplamı $b$, çarpımı $c$ olan iki sayı aranır. Bu sayılar $m$ ve $n$ ise $x^2+bx+c=(x+m)(x+n)$ olur.",
            ornek(
                "$x^2-5x+6$ ve $x^2+x-12$ ifadeleri verilsin.",
                "İfadeleri çarpanlarına ayıralım.",
                "$x^2-5x+6$: çarpımı $6$, toplamı $-5$ olan sayılar $-2$ ve $-3$ tür. Sonuç $(x-2)(x-3)$.",
                "$x^2+x-12$: çarpımı $-12$, toplamı $1$ olan sayılar $4$ ve $-3$ tür. Sonuç $(x+4)(x-3)$."),
            "Çarpım negatifse sayıların işaretleri farklıdır; toplamın işareti, mutlak değeri büyük olan sayının işaretidir. Çarpım pozitifse iki sayının işareti aynıdır ve toplamın işaretini taşır. Bu iki gözlem aranan sayıları hızla daraltır. Böyle iki tam sayı bulunamıyorsa üç terimli tam sayılarla ayrılmıyor olabilir; o zaman kökler ikinci dereceden denklem yöntemleriyle bulunur.",
        ]},
        {"baslik": "ax² + bx + c biçimindeki üç terimliler", "icerik": [
            "Baş katsayısı $1$ den farklıysa çapraz çarpım yöntemi kullanılır: $a$ katsayısı ve $c$ sabiti ikişer çarpana ayrılır; çaprazlama çarpımların toplamı $b$ yi veren düzen aranır.",
            ornek(
                "$2x^2+7x+3$ ifadesi verilsin.",
                "İfadeyi çarpanlarına ayıralım.",
                "$2x^2=2x \\cdot x$ ve $3=1 \\cdot 3$. Çapraz çarpımlar: $2x \\cdot 3+x \\cdot 1=7x$.",
                "Sonuç $(2x+1)(x+3)$."),
            ornek(
                "$6x^2-x-2$ ifadesi verilsin.",
                "İfadeyi çarpanlarına ayıralım.",
                "$6x^2=2x \\cdot 3x$ ve $-2=1 \\cdot (-2)$. Çapraz çarpımlar: $2x \\cdot (-2)+3x \\cdot 1=-x$.",
                "Sonuç $(2x+1)(3x-2)$."),
        ]},
        {"baslik": "Değişken değiştirme", "icerik": [
            "Bazı ifadeler ilk bakışta tanıdık görünmez ama bir parçası yeni bir değişkenle gösterilince bilinen bir biçime dönüşür. En sık karşılaşılan durum, yalnızca çift kuvvetleri olan dördüncü dereceden ifadelerdir.",
            ornek(
                "$x^4-5x^2+4$ ifadesi verilsin.",
                "İfadeyi çarpanlarına ayıralım.",
                "$x^2=t$ yazılır: $t^2-5t+4=(t-1)(t-4)$.",
                "Geri dönülür: $(x^2-1)(x^2-4)=(x-1)(x+1)(x-2)(x+2)$."),
        ]},
        {"baslik": "Terim ekleyip çıkarma", "icerik": [
            "Bazı ifadeler bir terim eklenip aynı terim çıkarılarak iki kare farkına dönüştürülür. Bu yöntem ilk bakışta çarpanlara ayrılmaz görünen ifadeleri çözer.",
            ornek(
                "$x^4+4$ ifadesi verilsin.",
                "İfadeyi çarpanlarına ayıralım.",
                "$4x^2$ eklenip çıkarılır: $x^4+4x^2+4-4x^2=(x^2+2)^2-(2x)^2$.",
                "İki kare farkı: $(x^2-2x+2)(x^2+2x+2)$."),
            "Bu örnekte $x^4+4$ iki kare toplamı olduğu hâlde çarpanlarına ayrılmıştır. Bunun nedeni, ifadenin gerçek köklerinin olmamasına rağmen ikinci dereceden gerçek çarpanlara ayrılabilmesidir; iki kare toplamı kuralı yalnızca $x^2+4$ gibi ikinci dereceden ifadeler için geçerlidir.",
        ]},
        {"baslik": "Çarpan teoremiyle kök denemek", "icerik": [
            "Özdeşliklerle ayrılamayan yüksek dereceli polinomlarda çarpan teoremi kullanılır: $P(a)=0$ ise $x-a$ bir çarpandır. Katsayıları tam sayı ve baş katsayısı $1$ olan bir polinomda tam sayı kökler sabit terimin bölenleri arasındadır.",
            ornek(
                "$P(x)=x^3-6x^2+11x-6$ polinomu verilsin.",
                "Polinomu çarpanlarına ayıralım.",
                "Sabit terim $-6$ nın bölenleri denenir: $P(1)=1-6+11-6=0$.",
                "$x-1$ bir çarpandır; bölüm $x^2-5x+6=(x-2)(x-3)$ tür.",
                "Sonuç $(x-1)(x-2)(x-3)$."),
            "Bir kök bulununca polinom o çarpana bölünür ve derecesi bir düşer. Bölüm ikinci dereceye inince üç terimli yöntemleri kullanılır. Denenecek sayıların sırası önemli değildir ama küçük bölenlerden başlamak hesabı kolaylaştırır; $1$ ve $-1$ en hızlı denenen adaylardır. Bölme için en kısa yol Horner yöntemidir; ayrıntısı <a href=\"/blog/polinomlarda-bolme/\">Polinomlarda Bölme İşlemi</a> yazısında.",
        ]},
        {"baslik": "Kesirli kök adayları", "icerik": [
            "Baş katsayı $1$ değilse kökler kesirli olabilir. Katsayıları tam sayı olan bir polinomun kesirli kökleri, sabit terimin bir böleninin baş katsayının bir bölenine bölümü biçimindedir. Bu kurala <strong>rasyonel kök teoremi</strong> denir ve denenecek adayların listesini verir.",
            ornek(
                "$P(x)=2x^3-3x^2-3x+2$ polinomu verilsin.",
                "Polinomu çarpanlarına ayıralım.",
                "Adaylar: $\\pm 1$, $\\pm 2$, $\\pm\\dfrac{1}{2}$. Denenince $P(2)=0$, $P(-1)=0$ ve $P(\\dfrac{1}{2})=0$ bulunur.",
                "Baş katsayı $2$ olduğu için sonuç $(x-2)(x+1)(2x-1)$ dir."),
        ]},
        {"baslik": "Dördüncü dereceden bir örnek", "icerik": [
            "Derece yükseldikçe kök deneme aynı biçimde sürdürülür: her bulunan kök bir çarpan verir ve polinomun derecesini bir düşürür.",
            ornek(
                "$P(x)=x^4-5x^3+5x^2+5x-6$ polinomu verilsin.",
                "Polinomu çarpanlarına ayıralım.",
                "$P(1)=1-5+5+5-6=0$ ve $P(-1)=1+5+5-5-6=0$.",
                "$P(2)=16-40+20+10-6=0$ ve $P(3)=81-135+45+15-6=0$.",
                "Dört kök bulundu; baş katsayı $1$ olduğu için $P(x)=(x-1)(x+1)(x-2)(x-3)$."),
            "Dördüncü dereceden bir polinomun en fazla dört gerçek kökü olabilir. Dört kök bulunduğunda çarpanlara ayırma tamamlanmıştır; bölme yapmaya bile gerek kalmaz.",
        ]},
        {"baslik": "Karışık örnekler", "icerik": [
            "Gerçek sorularda yöntemler çoğu zaman art arda kullanılır: önce ortak çarpan alınır, sonra kalan ifadeye bir özdeşlik ya da gruplama uygulanır.",
            ornek(
                "$2x^3-8x$, $x^3-x^2-4x+4$ ve $3x^2-12x+12$ ifadeleri verilsin.",
                "İfadeleri tamamen çarpanlarına ayıralım.",
                "$2x^3-8x=2x(x^2-4)=2x(x-2)(x+2)$.",
                "$x^3-x^2-4x+4=x^2(x-1)-4(x-1)=(x-1)(x-2)(x+2)$.",
                "$3x^2-12x+12=3(x^2-4x+4)=3(x-2)^2$."),
        ]},
        {"baslik": "Özdeşliklerle değer hesaplamak", "icerik": [
            "Özdeşlikler, değişkenlerin kendileri bilinmeden bazı ifadelerin değerini bulmayı da sağlar. En sık kullanılan bilgiler iki sayının toplamı ve çarpımıdır.",
            ornek(
                "$a+b=5$ ve $ab=6$ olsun.",
                "$a^2+b^2$ ve $a^3+b^3$ değerlerini bulalım.",
                "$a^2+b^2=(a+b)^2-2ab=25-12=13$.",
                "$a^3+b^3=(a+b)^3-3ab(a+b)=125-90=35$."),
            "Bu sonuçlar $a$ ve $b$ bulunarak da kontrol edilebilir: toplamı $5$, çarpımı $6$ olan sayılar $2$ ve $3$ tür; gerçekten $4+9=13$ ve $8+27=35$ tir.",
        ]},
        {"baslik": "Kesirli ifadeleri sadeleştirmek", "icerik": [
            "Pay ve payda çarpanlarına ayrılınca ortak çarpanlar sadeleşir. Sadeleşen çarpanı sıfır yapan değerler için ifade tanımsız olduğundan bu değerler ayrıca belirtilir.",
            ornek(
                "$\\dfrac{x^2-9}{x^2+5x+6}$ ifadesi verilsin.",
                "İfadeyi sadeleştirelim.",
                "Pay: $(x-3)(x+3)$. Payda: $(x+2)(x+3)$.",
                "Sadeleşince $\\dfrac{x-3}{x+2}$ bulunur; ifade $x=-3$ ve $x=-2$ için tanımsızdır."),
            dikkat(
                "Toplamdaki terimleri sadeleştirmek.",
                "$\\dfrac{x^2+3}{x+3}$ ifadesinde $3$ ler sadeleşmez. Yalnızca çarpanlar sadeleşir; bu yüzden önce pay ve payda çarpanlarına ayrılmalıdır."),
        ]},
        {"baslik": "Denklem çözmek", "icerik": [
            "Bir çarpım ancak çarpanlarından biri sıfırsa sıfırdır. Bu yüzden çarpanlarına ayrılmış bir denklemde her çarpan ayrı ayrı sıfıra eşitlenir.",
            ornek(
                "$x^3-x=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Ortak çarpan ve iki kare farkı: $x(x-1)(x+1)=0$.",
                "Çözüm kümesi $\\{-1, 0, 1\\}$."),
            dikkat(
                "Denklemin iki tarafını $x$ e bölmek.",
                "$x^3=x$ denkleminde iki taraf $x$ e bölünürse $x^2=1$ bulunur ve $x=0$ çözümü kaybolur. Bölmek yerine her şey bir tarafa toplanıp çarpanlara ayrılmalıdır."),
        ]},
        {"baslik": "Sayısal hesaplarda kısa yol", "icerik": [
            "Özdeşlikler yalnızca polinomlarda değil, sayılarla yapılan hesaplarda da işe yarar. Özellikle iki kare farkı, büyük sayıların karelerini hesaplamadan farkı bulmayı sağlar.",
            ornek(
                "$101^2-99^2$ işlemi verilsin.",
                "Sonucu hesaplayalım.",
                "İki kare farkı: $(101-99)(101+99)=2 \\cdot 200$.",
                "Sonuç $400$ dür."),
            ornek(
                "$98 \\cdot 102$ işlemi verilsin.",
                "Sonucu hesaplayalım.",
                "$(100-2)(100+2)=100^2-2^2$.",
                "Sonuç $10000-4=9996$."),
        ]},
        {"baslik": "Sonucu çarparak kontrol etmek", "icerik": [
            "Çarpanlara ayırmanın sonucu her zaman denetlenebilir: çarpanlar yeniden çarpılır ya da $x$ yerine basit bir sayı yazılarak iki tarafın değerleri karşılaştırılır. Sınavda tam çarpım zaman alıyorsa tek bir sayıyla yapılan kontrol çoğu hatayı yakalar.",
            ornek(
                "$6x^2-x-2=(2x+1)(3x-2)$ sonucu bulundu.",
                "Sonucu iki yolla kontrol edelim.",
                "Çarparak: $6x^2-4x+3x-2=6x^2-x-2$.",
                "$x=1$ yazarak: sol taraf $6-1-2=3$, sağ taraf $3 \\cdot 1=3$."),
        ]},
        {"baslik": "Hangi yöntem ne zaman?", "icerik": [
            "Çarpanlara ayırmada doğru yöntemi seçmek, ifadenin biçimine bakmakla başlar. Aşağıdaki sıra çoğu ifadede işe yarar:",
            tablo(["İfadenin biçimi", "Denenecek yöntem"], [
                ["Her terimde ortak çarpan var", "Ortak çarpan parantezi"],
                ["İki terim, ikisi de kare", "İki kare farkı"],
                ["İki terim, ikisi de küp", "Küp toplamı ya da farkı"],
                ["Üç terim", "Tam kare ya da iki sayı bulma"],
                ["Dört terim", "Gruplama ya da tam küp"],
                ["Yüksek derece", "Kök deneme ve bölme"],
            ]),
            "Her adımdan sonra elde edilen çarpanlara yeniden bakılmalıdır: bir çarpan hâlâ ayrılabiliyorsa işlem bitmemiştir. $x^4-16$ örneğinde ilk adımdan sonra $x^2-4$ çarpanı yeniden ayrılmıştı.",
        ]},
        {"baslik": "Sınavda çarpanlara ayırma", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) çarpanlara ayırma özdeşlikler, üç terimliler, kesirli ifadelerin sadeleştirilmesi ve sayısal kısa yollar biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) çarpan teoremiyle kök bulma, yüksek dereceli polinomların ayrılması ve denklem çözümü de sorulabilir."),
            "Sınavda sadeleştirme sorusu görünce ilk iş pay ve paydayı ayrı ayrı çarpanlarına ayırmaktır. Çoğu zaman pay ile paydada aynı çarpan belirir ve soru birkaç satırda biter. Sadeleşen çarpanı sıfır yapan değeri not etmeyi de unutma.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Ortak çarpanı almadan başlamak", "Önce ortak çarpan alınır"],
                ["$x^2+9$ u ayırmaya çalışmak", "Gerçek sayılarda ayrılmaz"],
                ["Küp açılımında işaret karıştırmak", "Son terim her zaman artıdır"],
                ["Toplamdaki terimleri sadeleştirmek", "Yalnız çarpanlar sadeleşir"],
                ["Denklemde $x$ e bölmek", "Kök kaybolur; çarpanlara ayrılır"],
                ["Bir çarpanı daha ayırmadan bırakmak", "Her çarpan yeniden incelenir"],
            ]),
            "Çarpanlara ayırmanın en güvenilir kontrolü, bulunan çarpanları yeniden çarpmaktır. Parantezler açıldığında başlangıçtaki ifade elde edilmiyorsa bir adımda hata vardır.",
        ]},
    ],
    "sss": [
        ("Çarpanlara ayırma nedir?",
         "Bir polinomu, dereceleri daha küçük polinomların çarpımı olarak yazmaktır. Çarpmanın tersidir."),
        ("Çarpanlara ayırmaya nereden başlanır?",
         "Önce bütün terimlerde ortak bir çarpan olup olmadığına bakılır. Sonra terim sayısına göre özdeşlikler ya da gruplama denenir."),
        ("İki kare farkı nedir?",
         "a kare eksi b kare, a eksi b ile a artı b nin çarpımına eşittir. x kare eksi 25 bu yolla x eksi 5 ile x artı 5 in çarpımı olarak yazılır."),
        ("x kare artı 4 çarpanlarına ayrılır mı?",
         "Gerçek sayılarda ayrılmaz, çünkü hiçbir gerçek x için sıfır olmaz. İkinci dereceden iki kare toplamları gerçek çarpanlara ayrılmaz."),
        ("Yüksek dereceli bir polinom nasıl çarpanlarına ayrılır?",
         "Sabit terimin bölenleri kök olarak denenir. Bulunan her kök bir çarpan verir ve polinom o çarpana bölünerek derecesi düşürülür."),
        ("Kesirli ifadeler nasıl sadeleştirilir?",
         "Pay ve payda çarpanlarına ayrılır, ortak çarpanlar sadeleştirilir. Toplamdaki terimler sadeleştirilemez."),
        ("Çarpanlara ayırmanın sonucu nasıl kontrol edilir?",
         "Bulunan çarpanlar yeniden çarpılır ya da x yerine basit bir sayı yazılarak iki tarafın değeri karşılaştırılır. İki taraf eşit değilse bir adımda hata vardır."),
        ("Gruplama ne zaman kullanılır?",
         "Dört terimli ve bütün terimlerde ortak çarpan olmayan ifadelerde kullanılır. Terimler ikişerli gruplanır ve gruplar arasında ortak bir parantez aranır."),
    ],
    "kontrol": [
        "Ortak çarpan parantezini kullanabiliyorum.",
        "Gruplama yöntemini uygulayabiliyorum.",
        "İki kare farkını tanıyıp kullanabiliyorum.",
        "Tam kare ve tam küp ifadeleri çarpanlarına ayırabiliyorum.",
        "Küp toplamı ve farkı özdeşliklerini kullanabiliyorum.",
        "Üç terimli ifadeleri çarpanlarına ayırabiliyorum.",
        "Değişken değiştirme ve terim ekleyip çıkarma yöntemlerini uygulayabiliyorum.",
        "Çarpan teoremiyle yüksek dereceli polinomları ayırabiliyorum.",
        "Kesirli ifadeleri çarpanlara ayırarak sadeleştirebiliyorum.",
        "Çarpanlara ayırarak denklem çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["polinomlar-konu-anlatimi", "polinomlarda-bolme", "polinomlarda-kalan"],
}
