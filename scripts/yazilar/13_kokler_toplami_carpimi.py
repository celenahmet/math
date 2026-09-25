# scripts/yazilar/13_kokler_toplami_carpimi.py — Kokler Toplami ve Carpimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kokler-toplami-carpimi",
    "baslik": "Kökler Toplamı ve Kökler Çarpımı Nasıl Bulunur?",
    "aciklama": "Kökler toplamı ve çarpımı nasıl bulunur? Vieta bağıntıları, köklerin kareleri ve tersleri, kökleri verilen denklem, parametreler ve işaretler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "kokler-toplami-carpimi",
    "kapak_alt": "Kökler toplamı ve çarpımı: iki kök noktasını uzunluk ve dikdörtgen alan modelleriyle ilişkilendiren iki öğrenci",
    "ozet": "İkinci dereceden bir denklemin köklerini bulmadan onların toplamını ve çarpımını hesaplamak mümkündür: ikisi de doğrudan katsayılardan okunur. Bu bağıntılar, köklerle kurulan pek çok ifadeyi tek satırda hesaplamayı ve kökleri verilen denklemi hemen yazmayı sağlar. Bu yazıda kökler toplamı ve çarpımı formüllerini ve nedenlerini, köklerin kareleri, küpleri, tersleri ve farkıyla ilgili ifadeleri, kökleri verilen ya da türetilen denklemleri, parametreli soruları ve köklerin işaretlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kökler toplamı ve çarpımı formülleri", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için ikinci dereceden denklemleri ve kök formülünü biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/ikinci-dereceden-denklemler/\">İkinci Dereceden Denklemler Konu Anlatımı</a> yazısına göz at."),
            "$ax^2+bx+c=0$ denkleminin kökleri $x_1$ ve $x_2$ olsun. Köklerin toplamı ve çarpımı, kökler hiç bulunmadan katsayılardan hesaplanır. Bu eşitliklere, onları ilk kez sistemli biçimde kullanan matematikçinin adıyla <strong>Vieta bağıntıları</strong> denir:",
            tablo(["Bağıntı", "Formül"], [
                ["Kökler toplamı", "$x_1+x_2=-\\dfrac{b}{a}$"],
                ["Kökler çarpımı", "$x_1 \\cdot x_2=\\dfrac{c}{a}$"],
            ]),
            "Kapaktaki öğrenciler bu iki bağıntıyı somut modellerle gösteriyor: toplam iki uzunluğun art arda eklenmesiyle, çarpım ise kenarları bu iki uzunluk olan dikdörtgenin alanıyla canlanıyor.",
            hap("$x_1+x_2=-\\dfrac{b}{a}$ ve $x_1 \\cdot x_2=\\dfrac{c}{a}$",
                "Toplamda eksi işareti vardır, çarpımda yoktur."),
        ]},
        {"baslik": "Formüller neden doğrudur?", "icerik": [
            "Kökleri $x_1$ ve $x_2$ olan denklem, baş katsayı $a$ olmak üzere $a(x-x_1)(x-x_2)=0$ biçiminde yazılabilir. Parantezler açılınca aşağıdaki eşitlik elde edilir:",
            "$$a x^2-a(x_1+x_2)x+a x_1 x_2=ax^2+bx+c$$",
            "Aynı kuvvetlerin katsayıları eşitlenir: $x$ in katsayılarından $-a(x_1+x_2)=b$, sabit terimlerden $a x_1 x_2=c$ bulunur. İki formül de buradan doğrudan çıkar. Bu açıklama, formüllerin ezberlenmesi gereken kurallar değil, çarpanlara ayırmanın bir sonucu olduğunu gösterir.",
            "Aynı sonuç kök formülünden de elde edilir: $\\dfrac{-b+\\sqrt{\\Delta}}{2a}$ ile $\\dfrac{-b-\\sqrt{\\Delta}}{2a}$ toplanınca karekökler birbirini götürür ve $-\\dfrac{b}{a}$ kalır. Çarpılınca da iki kare farkı $b^2-\\Delta=4ac$ verir ve sonuç $\\dfrac{c}{a}$ olur.",
        ]},
        {"baslik": "Temel örnek", "icerik": [
            "Formülleri kullanmadan önce denklem standart biçime getirilir ve katsayılar işaretleriyle birlikte okunur. Eşitliğin iki tarafında terim varsa hepsi bir tarafa toplanmadan okunan katsayılar yanlış sonuç verir; bu yüzden ilk adım her zaman sağ tarafı sıfır yapmaktır.",
            ornek(
                "$2x^2-6x+4=0$ denklemi verilsin.",
                "Kökler toplamını ve çarpımını bulup kökleri bularak kontrol edelim.",
                "Toplam: $-\\dfrac{-6}{2}=3$. Çarpım: $\\dfrac{4}{2}=2$.",
                "Denklem $2(x-1)(x-2)=0$ olarak çarpanlarına ayrılır; kökler $1$ ve $2$ dir. Toplamları $3$, çarpımları $2$ dir."),
            dikkat(
                "Toplamda eksi işaretini unutmak.",
                "Kökler toplamı $-\\dfrac{b}{a}$ dir; $\\dfrac{b}{a}$ değil. Örnekte $\\dfrac{b}{a}=-3$ olurdu, bu da köklerin gerçek toplamının tersidir."),
        ]},
        {"baslik": "Bir kök biliniyorsa diğeri", "icerik": [
            "Köklerden biri biliniyorsa diğerini bulmak için denklemi çözmeye gerek yoktur. Toplam formülünden bilinen kök çıkarılır ya da çarpım formülü bilinen köke bölünür. İki yol da aynı sonucu verir ve biri diğerinin kontrolü olarak kullanılabilir.",
            ornek(
                "$x^2-7x+10=0$ denkleminin bir kökü $2$ dir.",
                "Diğer kökü bulalım.",
                "Toplamdan: $7-2=5$.",
                "Çarpımdan: $10:2=5$. İki yol aynı sonucu verir."),
            ornek(
                "$3x^2-x-2=0$ denkleminin bir kökü $1$ dir.",
                "Diğer kökü bulalım.",
                "Çarpım $\\dfrac{c}{a}=-\\dfrac{2}{3}$ dir ve bir kök $1$ dir.",
                "Diğer kök $-\\dfrac{2}{3}$ dir. Toplamdan kontrol: $1-\\dfrac{2}{3}=\\dfrac{1}{3}$ ve $-\\dfrac{b}{a}=\\dfrac{1}{3}$ dir."),
        ]},
        {"baslik": "Köklerin kareleri toplamı", "icerik": [
            "Köklerle kurulan ifadelerin çoğu toplam ve çarpım cinsinden yazılabilir. Bu yazıda kısaca $S=x_1+x_2$ ve $P=x_1 x_2$ gösterimleri kullanılacaktır. Karelerin toplamı için tam kare özdeşliğinden yararlanılır:",
            "$$x_1^2+x_2^2=S^2-2P$$",
            ornek(
                "$x^2-5x+3=0$ denkleminin kökleri $x_1$ ve $x_2$ olsun.",
                "$x_1^2+x_2^2$ değerini bulalım.",
                "$S=5$ ve $P=3$.",
                "$x_1^2+x_2^2=25-6=19$."),
            "Bu denklemin kökleri irrasyoneldir: $\\dfrac{5 \\pm \\sqrt{13}}{2}$. Kökleri bulup karelerini toplamak uzun bir işlemdir; formül ise sonucu tek satırda verir.",
            hap("Köklerin kareleri toplamı $S^2-2P$ olur.", "Bu değer $S^2$ ile karıştırılmamalıdır; aradaki fark $2P$ kadardır."),
        ]},
        {"baslik": "Köklerin terslerinin toplamı", "icerik": [
            "Köklerin terslerinin toplamı payda eşitlenerek toplam ve çarpım cinsinden yazılır:",
            "$$\\dfrac{1}{x_1}+\\dfrac{1}{x_2}=\\dfrac{x_1+x_2}{x_1 x_2}=\\dfrac{S}{P}$$",
            ornek(
                "$x^2-5x+3=0$ denklemi verilsin.",
                "Köklerin terslerinin toplamını bulalım.",
                "$\\dfrac{S}{P}=\\dfrac{5}{3}$."),
            "Bu formül yalnızca köklerden hiçbiri sıfır değilse, yani $P \\neq 0$ ise anlamlıdır. Sabit terimi sıfır olan bir denklemde köklerden biri $0$ dır ve tersi tanımsızdır.",
        ]},
        {"baslik": "Köklerin küpleri toplamı", "icerik": [
            "Küplerin toplamı, küp toplamı özdeşliğinden ya da tam küp açılımından toplam ve çarpım cinsinden yazılır:",
            "$$x_1^3+x_2^3=S^3-3PS$$",
            ornek(
                "$x^2-5x+3=0$ denklemi verilsin.",
                "Köklerin küpleri toplamını bulalım.",
                "$S^3=125$ ve $3PS=45$.",
                "$x_1^3+x_2^3=125-45=80$."),
            "Bu örnek, bağıntıların asıl gücünü gösterir: kökler irrasyonel olduğu hâlde küplerinin toplamı bir tam sayıdır. Kökleri bulup küplerini almak hem uzun sürer hem de hata yapma olasılığını artırır; toplam ve çarpımla yapılan hesap ise yalnızca birkaç çarpma işlemidir.",
        ]},
        {"baslik": "Kareler toplamından parametre bulmak", "icerik": [
            "Köklerle kurulan bir ifadenin değeri verilmişse ifade $S$ ve $P$ cinsinden yazılır ve parametre bu denklemden bulunur. Sonra bulunan değerler için köklerin gerçekten var olduğu diskriminantla denetlenir.",
            ornek(
                "$x^2-mx+4=0$ denkleminin kökleri için $x_1^2+x_2^2=17$ dir.",
                "$m$ yi bulalım.",
                "$S=m$ ve $P=4$: $m^2-8=17$, yani $m^2=25$ ve $m=\\pm 5$.",
                "İki değer için de $\\Delta=25-16=9>0$ dır; kökler gerçektir."),
        ]},
        {"baslik": "Kökler arasındaki fark", "icerik": [
            "Köklerin farkının karesi de toplam ve çarpımla yazılır: $(x_1-x_2)^2=S^2-4P$. Karekök alınınca kökler arasındaki uzaklık bulunur. Bu ifade, baş katsayısı $1$ olan denklemde diskriminanta eşittir.",
            ornek(
                "$x^2-5x+3=0$ denklemi verilsin.",
                "Kökler arasındaki farkın mutlak değerini bulalım.",
                "$S^2-4P=25-12=13$.",
                "$|x_1-x_2|=\\sqrt{13}$."),
        ]},
        {"baslik": "Diğer simetrik ifadeler", "icerik": [
            "Kökler yer değiştirdiğinde değişmeyen ifadelere simetrik ifade denir ve her simetrik ifade $S$ ile $P$ cinsinden yazılabilir. En sık karşılaşılanlar aşağıdadır:",
            tablo(["İfade", "$S$ ve $P$ ile", "$x^2-5x+3=0$ için"], [
                ["$x_1^2 x_2+x_1 x_2^2$", "$P \\cdot S$", "$15$"],
                ["$\\dfrac{x_1}{x_2}+\\dfrac{x_2}{x_1}$", "$\\dfrac{S^2-2P}{P}$", "$\\dfrac{19}{3}$"],
                ["$(x_1+1)(x_2+1)$", "$P+S+1$", "$9$"],
                ["$(x_1-2)(x_2-2)$", "$P-2S+4$", "$-3$"],
            ]),
            "Böyle bir ifadeyle karşılaşınca yapılacak iş, ifadeyi açıp içinde $x_1+x_2$ ve $x_1 x_2$ parçalarını aramaktır. Parantezli ifadeler açıldığında bu parçalar kendiliğinden ortaya çıkar. Simetrik olmayan bir ifade, örneğin yalnızca $x_1$ in karesi, bu yolla hesaplanamaz; o durumda kökleri bulmak gerekir.",
        ]},
        {"baslik": "Kökleri verilen denklemi yazmak", "icerik": [
            "Kökleri bilinen bir denklem, toplam ve çarpım kullanılarak doğrudan yazılır. Baş katsayısı $1$ olan denklem şudur:",
            "$$x^2-Sx+P=0$$",
            ornek(
                "Kökleri $3$ ve $-4$ olan denklem istensin.",
                "Denklemi yazalım.",
                "$S=-1$ ve $P=-12$.",
                "$x^2+x-12=0$. Kontrol: $(x-3)(x+4)=x^2+x-12$."),
            "Baş katsayısı $1$ olmayan bir denklem istenirse bu denklem istenen sayıyla çarpılır. Kökler değişmez, çünkü denklemin iki tarafını sıfırdan farklı bir sayıyla çarpmak çözüm kümesini etkilemez.",
            hap("Toplamı $S$, çarpımı $P$ olan iki sayı $x^2-Sx+P=0$ denkleminin kökleridir."),
        ]},
        {"baslik": "Kökleri türetilen denklem", "icerik": [
            "Bazı sorularda verilen denklemin köklerinden türetilen sayıları kök kabul eden yeni bir denklem istenir. Yeni köklerin toplamı ve çarpımı eski $S$ ve $P$ cinsinden hesaplanır.",
            ornek(
                "$x^2-5x+3=0$ denkleminin kökleri $x_1$ ve $x_2$ dir.",
                "Kökleri $2x_1$ ve $2x_2$ olan denklemi yazalım.",
                "Yeni toplam $2S=10$, yeni çarpım $4P=12$.",
                "$x^2-10x+12=0$."),
            ornek(
                "Aynı denklem verilsin.",
                "Kökleri $x_1+1$ ve $x_2+1$ olan denklemi yazalım.",
                "Yeni toplam $S+2=7$, yeni çarpım $P+S+1=9$.",
                "$x^2-7x+9=0$."),
        ]},
        {"baslik": "Köklerin kareleri kök olan denklem", "icerik": [
            "Kökleri $x_1^2$ ve $x_2^2$ olan denklemi yazmak için yeni köklerin toplamı ve çarpımı hesaplanır. Toplam, kareler toplamıdır; çarpım ise eski çarpımın karesidir.",
            ornek(
                "$x^2-5x+3=0$ denkleminin kökleri $x_1$ ve $x_2$ dir.",
                "Kökleri $x_1^2$ ve $x_2^2$ olan denklemi yazalım.",
                "Yeni toplam $S^2-2P=19$, yeni çarpım $P^2=9$.",
                "$x^2-19x+9=0$."),
        ]},
        {"baslik": "Köklerin tersleri kök olan denklem", "icerik": [
            "Kökleri $\\dfrac{1}{x_1}$ ve $\\dfrac{1}{x_2}$ olan denklemin katsayıları, ilk denklemin katsayılarının ters sırada yazılmasıyla elde edilir. Bunun nedeni, $x$ yerine $\\dfrac{1}{x}$ yazılıp paydadan kurtulunca katsayıların yer değiştirmesidir.",
            ornek(
                "$x^2-5x+3=0$ denklemi verilsin.",
                "Kökleri bu denklemin köklerinin tersleri olan denklemi yazalım.",
                "Yeni toplam $\\dfrac{S}{P}=\\dfrac{5}{3}$, yeni çarpım $\\dfrac{1}{P}=\\dfrac{1}{3}$.",
                "$x^2-\\dfrac{5}{3}x+\\dfrac{1}{3}=0$, yani $3x^2-5x+1=0$. Katsayılar $1$, $-5$, $3$ ün ters sırasıdır."),
        ]},
        {"baslik": "Toplam ve çarpımdan katsayı bulmak", "icerik": [
            "Denklemin katsayıları bilinmiyor ama kökler toplamı ve çarpımı biliniyorsa katsayılar doğrudan yazılır. Baş katsayı $1$ olduğunda $b$ toplamın ters işaretlisi, $c$ ise çarpımın kendisidir.",
            ornek(
                "$x^2+ax+b=0$ denkleminin kökler toplamı $4$, kökler çarpımı $-5$ tir.",
                "$a$ ve $b$ yi bulalım.",
                "$-a=4$, yani $a=-4$. $b=-5$.",
                "Denklem $x^2-4x-5=0$ dır; kökleri $5$ ve $-1$ dir."),
        ]},
        {"baslik": "Kökler toplamından parametre bulmak", "icerik": [
            "Denklemde bir parametre varsa ve kökler toplamı ya da çarpımı verilmişse formül parametre için doğrudan bir denklem verir.",
            ornek(
                "$x^2-(m+2)x+2m-1=0$ denkleminin kökler toplamı $5$ tir.",
                "$m$ yi bulalım.",
                "$S=m+2=5$, yani $m=3$.",
                "Denklem $x^2-5x+5=0$ olur. Diskriminantı $25-20=5>0$ olduğu için gerçekten iki gerçek kökü vardır."),
            dikkat(
                "Parametreyi bulduktan sonra köklerin varlığını denetlememek.",
                "Kökler toplamı formülü, kökler gerçek olmasa da cebirsel olarak çalışır. Soru gerçek kökler istiyorsa bulunan parametre için diskriminantın negatif olmadığı ayrıca kontrol edilmelidir."),
        ]},
        {"baslik": "Kökler arasında bir bağıntı verildiğinde", "icerik": [
            "Kökler arasında bir ilişki verilmişse bu ilişki toplam formülüyle birlikte kullanılarak kökler bulunur, sonra çarpım formülünden parametre hesaplanır.",
            ornek(
                "$x^2-9x+m=0$ denkleminin bir kökü diğerinin iki katıdır.",
                "Kökleri ve $m$ yi bulalım.",
                "Kökler $k$ ve $2k$ olsun: toplam $3k=9$, yani $k=3$. Kökler $3$ ve $6$ dır.",
                "$m=P=18$."),
            ornek(
                "$x^2-7x+m=0$ denkleminin kökleri arasındaki fark $3$ tür.",
                "$m$ yi bulalım.",
                "$x_1+x_2=7$ ve $x_1-x_2=3$; buradan $x_1=5$ ve $x_2=2$.",
                "$m=5 \\cdot 2=10$."),
        ]},
        {"baslik": "Eşit kökler", "icerik": [
            "Denklemin kökleri eşitse, yani çakışıksa, iki kök de toplamın yarısına eşittir ve çarpım bu değerin karesidir. Bu gözlem, diskriminantı sıfıra eşitlemenin yanında ikinci bir çözüm yolu verir.",
            ornek(
                "$x^2-6x+m=0$ denkleminin kökleri eşittir.",
                "$m$ yi bulalım.",
                "Toplam $6$ olduğu için iki kök de $3$ tür.",
                "$m=P=3 \\cdot 3=9$. Kontrol: $\\Delta=36-36=0$."),
        ]},
        {"baslik": "Tam sayı kökler", "icerik": [
            "Köklerin tam sayı olması istendiğinde toplam sabitse kökler, toplamı bu sayıya eşit olan tam sayı çiftleri arasından seçilir. Her çift bir çarpım, yani bir parametre değeri verir.",
            ornek(
                "$x^2-8x+m=0$ denkleminin kökleri pozitif tam sayılardır.",
                "$m$ nin alabileceği değerlerin sayısını bulalım.",
                "Toplamı $8$ olan pozitif tam sayı çiftleri: $1$ ile $7$, $2$ ile $6$, $3$ ile $5$, $4$ ile $4$.",
                "Çarpımlar $7$, $12$, $15$ ve $16$ dır; $m$ nin $4$ değeri vardır."),
        ]},
        {"baslik": "Köklerin işaretleri", "icerik": [
            "Kökler bulunmadan işaretleri de belirlenebilir. Çarpım, köklerin aynı mı ters mi işaretli olduğunu söyler; aynı işaretliyse toplam bu ortak işareti verir. Önce diskriminantla gerçek köklerin varlığı kontrol edilmelidir.",
            tablo(["Çarpım $P$", "Toplam $S$", "Kökler"], [
                ["Pozitif", "Pozitif", "İkisi de pozitif"],
                ["Pozitif", "Negatif", "İkisi de negatif"],
                ["Negatif", "Herhangi", "Ters işaretli"],
                ["Sıfır", "Herhangi", "Biri sıfır"],
            ]),
            ornek(
                "$x^2+3x-10=0$ denklemi verilsin.",
                "Köklerin işaretlerini bulalım.",
                "$P=-10<0$; kökler ters işaretlidir.",
                "$S=-3<0$ olduğu için negatif kökün mutlak değeri daha büyüktür. Gerçekten kökler $2$ ve $-5$ tir."),
            "İşaret tablosu yalnızca gerçek kökler için anlamlıdır. Çarpım ve toplam pozitif olsa bile diskriminant negatifse denklemin gerçek kökü yoktur; bu yüzden işaret sorularında ilk adım her zaman diskriminantı kontrol etmektir.",
            hap("Kökler çarpımı negatifse kökler ters işaretlidir.", "Çarpım pozitifse kökler aynı işaretlidir ve bu ortak işareti kökler toplamı belirler."),
        ]},
        {"baslik": "Simetrik ve ters kökler", "icerik": [
            "Köklerin birbirinin ters işaretlisi olması, yani $x_1=-x_2$ olması toplamın sıfır olması demektir; bu da $b=0$ koşulunu verir. Köklerin birbirinin çarpmaya göre tersi olması ise çarpımın $1$ olması, yani $c=a$ demektir.",
            ornek(
                "$x^2+(m-3)x-4=0$ denkleminin kökleri birbirinin ters işaretlisidir.",
                "$m$ yi ve kökleri bulalım.",
                "Toplam sıfır olmalıdır: $m-3=0$, yani $m=3$.",
                "Denklem $x^2-4=0$ olur; kökler $2$ ve $-2$ dir."),
            ornek(
                "$2x^2+5x+m=0$ denkleminin kökleri birbirinin çarpmaya göre tersidir.",
                "$m$ yi bulalım.",
                "Çarpım $1$ olmalıdır: $\\dfrac{m}{2}=1$, yani $m=2$.",
                "Denklem $2x^2+5x+2=0$ olur ve kökler $-\\dfrac{1}{2}$ ile $-2$ dir; çarpımları gerçekten $1$ dir."),
        ]},
        {"baslik": "Toplam ve çarpımdan iki sayı bulmak", "icerik": [
            "Toplamı ve çarpımı bilinen iki sayı, $x^2-Sx+P=0$ denkleminin kökleridir. Bu gözlem, uzunluk ve alan problemlerini doğrudan bir denkleme çevirir.",
            ornek(
                "Bir dikdörtgenin çevresi $20$ santimetre, alanı $24$ santimetrekaredir.",
                "Kenar uzunluklarını bulalım.",
                "Kenarların toplamı yarı çevredir: $10$. Çarpımları alandır: $24$.",
                "Kenarlar $x^2-10x+24=0$ denkleminin kökleridir: $(x-4)(x-6)=0$. Kenarlar $4$ ve $6$ santimetredir."),
            "Kapaktaki modelin söylediği de budur: iki uzunluğun art arda dizilmesi toplamı, bu uzunluklarla kurulan dikdörtgenin alanı çarpımı verir. İkisi birlikte bilindiğinde uzunlukların kendisi de bulunur.",
            hap("Çevresi $26$ metre, alanı $40$ metrekare olan dikdörtgen bir odanın kenarları, toplamı $13$ ve çarpımı $40$ olan iki sayıdır.", "Bu sayılar $x^2-13x+40=0$ denkleminin kökleri olan $5$ ve $8$ olur; oda $5$ metreye $8$ metredir.", gunluk=True),
        ]},
        {"baslik": "Üçüncü dereceden denklemlere uzantı", "icerik": [
            "Vieta bağıntıları daha yüksek dereceli denklemlerde de geçerlidir. $ax^3+bx^2+cx+d=0$ denkleminin kökleri $x_1$, $x_2$ ve $x_3$ ise:",
            tablo(["Bağıntı", "Formül"], [
                ["$x_1+x_2+x_3$", "$-\\dfrac{b}{a}$"],
                ["$x_1 x_2+x_1 x_3+x_2 x_3$", "$\\dfrac{c}{a}$"],
                ["$x_1 x_2 x_3$", "$-\\dfrac{d}{a}$"],
            ]),
            ornek(
                "$x^3-6x^2+11x-6=0$ denklemi verilsin.",
                "Bağıntıları hesaplayıp köklerle karşılaştıralım.",
                "Toplam $6$, ikili çarpımlar toplamı $11$, çarpım $6$.",
                "Kökler $1$, $2$ ve $3$ tür: $1+2+3=6$, $2+3+6=11$ ve $1 \\cdot 2 \\cdot 3=6$."),
        ]},
        {"baslik": "Formülleri doğru hatırlamanın yolu", "icerik": [
            "Kökler toplamı ve çarpımı formüllerinde en çok karıştırılan şey işaretlerdir. Bunları hatırlamanın güvenilir yolu, kökleri bilinen küçük bir denklemi zihinde açmaktır. Kökleri $1$ ve $2$ olan denklem $(x-1)(x-2)=x^2-3x+2=0$ dır.",
            "Bu denklemde köklerin toplamı $3$, çarpımı $2$ dir. Katsayılar ise $a=1$, $b=-3$, $c=2$ dir. Toplamın $3$ çıkması için $-\\dfrac{b}{a}$ yazılması gerektiği, çarpımın $2$ çıkması için ise $\\dfrac{c}{a}$ nin yeterli olduğu hemen görülür. Birkaç saniyelik bu deneme, formülü yanlış hatırlamaktan doğan hataların tamamını önler.",
        ]},
        {"baslik": "Sınavda kökler toplamı ve çarpımı", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kökler toplamı ve çarpımı, köklerin kareleri toplamı ve kökleri verilen denklemi yazma biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) kökleri türetilen denklemler, parametreli sorular, köklerin işaretleri ve üçüncü dereceden denklemlerde Vieta bağıntıları da sorulabilir."),
            "Soru köklerle kurulmuş bir ifade istiyorsa kökleri bulmaya çalışma. İfadeyi açıp toplam ve çarpım parçalarını bul; kökler irrasyonel olsa bile sonuç çoğu zaman tam sayı ya da basit bir kesir çıkar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Toplamı $\\dfrac{b}{a}$ almak", "Toplam $-\\dfrac{b}{a}$"],
                ["Çarpımı $-\\dfrac{c}{a}$ almak", "Çarpım $\\dfrac{c}{a}$"],
                ["Kareler toplamını $S^2$ sanmak", "$S^2-2P$"],
                ["Standart biçime getirmeden katsayı okumak", "Önce bir tarafa toplanır"],
                ["Parametre bulunca köklerin varlığına bakmamak", "Diskriminant denetlenir"],
                ["Üçüncü derecede çarpımın işaretini karıştırmak", "Çarpım $-\\dfrac{d}{a}$"],
            ]),
            "Bu hataların çoğu işaretlerle ilgilidir. Formülü doğru hatırlayıp hatırlamadığını denetlemenin en hızlı yolu, kökleri bilinen küçük bir denklemde, örneğin $(x-1)(x-2)=0$ da, formülü denemektir.",
        ]},
    ],
    "sss": [
        ("Kökler toplamı nasıl bulunur?",
         "ax kare artı bx artı c eşittir sıfır denkleminde kökler toplamı eksi b bölü a dır. Kökleri bulmaya gerek yoktur."),
        ("Kökler çarpımı nasıl bulunur?",
         "Kökler çarpımı c bölü a dır. Çarpım negatifse kökler ters işaretlidir."),
        ("Köklerin kareleri toplamı nasıl hesaplanır?",
         "Kökler toplamının karesinden kökler çarpımının iki katı çıkarılır. Toplamı 5, çarpımı 3 olan köklerin kareleri toplamı 19 dur."),
        ("Kökleri verilen denklem nasıl yazılır?",
         "Kökler toplamı ve çarpımı hesaplanır. Baş katsayısı 1 olan denklem x kare eksi toplam çarpı x artı çarpım eşittir sıfırdır."),
        ("Köklerin işaretleri kökleri bulmadan nasıl anlaşılır?",
         "Çarpım negatifse kökler ters işaretlidir. Çarpım pozitifse kökler aynı işaretlidir ve toplamın işareti bu ortak işareti verir."),
        ("Vieta bağıntıları üçüncü dereceden denklemlerde geçerli mi?",
         "Evet. Kökler toplamı eksi b bölü a, ikili çarpımlar toplamı c bölü a, kökler çarpımı eksi d bölü a dır."),
    ],
    "kontrol": [
        "Kökler toplamı ve çarpımı formüllerini yazabiliyorum.",
        "Formüllerin nereden geldiğini açıklayabiliyorum.",
        "Köklerin kareleri ve küpleri toplamını hesaplayabiliyorum.",
        "Köklerin terslerinin toplamını bulabiliyorum.",
        "Kökler arasındaki farkı hesaplayabiliyorum.",
        "Kökleri verilen denklemi yazabiliyorum.",
        "Kökleri türetilen yeni denklemi kurabiliyorum.",
        "Kökler arasındaki bağıntıdan parametre bulabiliyorum.",
        "Köklerin işaretlerini kökleri bulmadan belirleyebiliyorum.",
        "Vieta bağıntılarını üçüncü dereceden denklemlere uygulayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["ikinci-dereceden-denklemler", "diskriminant-delta", "parabol-konu-anlatimi"],
}
