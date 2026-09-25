# scripts/yazilar/44_artan_azalan.py — Turevde Artan ve Azalan Fonksiyonlar (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "artan-azalan-fonksiyonlar",
    "baslik": "Türevde Artan ve Azalan Fonksiyonlar",
    "aciklama": "Türevle artan ve azalan aralıklar nasıl bulunur? Türevin işareti, işaret tablosu, her yerde artanlık, kesirli fonksiyonlar ve eşitsizlik ispatı; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "artan-azalan-fonksiyonlar",
    "kapak_alt": "Türevde artan ve azalan fonksiyonlar: dalgalı yolun yükselen ve alçalan bölümlerine farklı renkte boncuklar dizen iki öğrenci",
    "ozet": "Bir fonksiyonun hangi aralıklarda arttığı ve hangi aralıklarda azaldığı türevinin işaretinden okunur: türev pozitifse fonksiyon artar, negatifse azalır. Bu yöntem grafiği çizmeden fonksiyonun davranışını ortaya çıkarır. Bu yazıda artan ve azalan fonksiyonun tanımını, türevle ilişkisini, işaret tablosu yöntemini, polinom, rasyonel, üstel, logaritmik ve trigonometrik fonksiyonlarda artan ve azalan aralıkları, her yerde artan olma koşulunu ve parametreli soruları, türevin sıfır olduğu ama fonksiyonun artmaya devam ettiği durumları, türevle eşitsizlik ispatını, kök sayısını ve birebirliği çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Artan ve azalan ne demek?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için türev kurallarını ve işaret tablosu yapmayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> ve <a href=\"/blog/esitsizlikler-konu-anlatimi-pdf/\">Eşitsizlikler Konu Anlatımı</a> yazılarına göz at."),
            "Bir aralıkta $x$ büyüdükçe fonksiyonun değeri de büyüyorsa fonksiyon o aralıkta <strong>artandır</strong>; $x$ büyüdükçe değer küçülüyorsa <strong>azalandır</strong>. Kesin tanım şöyledir: aralıktaki her $x_1<x_2$ için $f(x_1)<f(x_2)$ oluyorsa fonksiyon artan, $f(x_1)>f(x_2)$ oluyorsa azalandır.",
            "Kapaktaki öğrenciler dalgalı bir yolun yükselen bölümlerine bir renkte, alçalan bölümlerine başka renkte boncuklar diziyor. Grafiğin soldan sağa yükseldiği yerler artan, alçaldığı yerler azalan aralıklardır. Bu yazı, bu aralıkları grafiği çizmeden türevle bulmayı anlatıyor.",
        ]},
        {"baslik": "Türevle ilişki", "icerik": [
            "Türev, grafiğin her noktasındaki teğetin eğimidir. Grafik yükselirken teğetler sağa doğru yukarı eğiktir ve eğimleri pozitiftir; grafik alçalırken teğetler aşağı eğiktir ve eğimleri negatiftir. Bu gözlem şu kurala dönüşür:",
            tablo(["Aralıkta türev", "Fonksiyon"], [
                ["$f'(x)>0$", "Artan"],
                ["$f'(x)<0$", "Azalan"],
                ["$f'(x)=0$", "Sabit"],
            ]),
            hap("Türevin işareti, fonksiyonun yönünü gösterir.",
                "Pozitif türev yükselen, negatif türev alçalan grafik demektir."),
        ]},
        {"baslik": "İşaret tablosu yöntemi", "icerik": [
            "Artan ve azalan aralıklar her fonksiyonda aynı dört adımda bulunur. Yöntem, türevin işaretinin yalnızca türevin sıfır olduğu ya da tanımsız olduğu noktalarda değişebilmesine dayanır:",
            tablo(["Adım", "İşlem"], [
                ["1", "Fonksiyonun tanım kümesini belirle"],
                ["2", "Türevi al ve çarpanlarına ayır"],
                ["3", "Türevin sıfır ve tanımsız olduğu noktaları bul"],
                ["4", "Bu noktaların arasındaki her aralıkta türevin işaretine bak"],
            ]),
            "Her aralıkta türevin işareti sabit olduğu için aralıktan tek bir sayı seçip türevde denemek yeterlidir. Çarpanlarına ayrılmış türevde işaret, çarpanların işaretlerinden de okunabilir.",
            hap("Türevin işareti yalnızca türevin sıfır ya da tanımsız olduğu noktalarda değişebilir; bu noktalar işaret tablosuna yazılır."),
        ]},
        {"baslik": "Parabolde artan ve azalan", "icerik": [
            "İkinci dereceden fonksiyonlarda türev birinci derecedendir ve tek bir noktada sıfır olur. Bu nokta parabolün tepe noktasının apsisidir ve fonksiyon yalnızca burada yön değiştirir.",
            ornek(
                "$f(x)=x^2-4x$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=2x-4$ tür ve $x=2$ de sıfır olur; $x<2$ için negatif, $x>2$ için pozitiftir.",
                "Fonksiyon $(-\\infty, 2)$ aralığında azalan, $(2, \\infty)$ aralığında artandır."),
            "Sonuç parabol bilgisiyle uyumludur: kolları yukarı bakan parabol tepe noktasına kadar iner, sonra yükselir. Parabolün ayrıntıları için <a href=\"/blog/parabol-grafigi/\">Parabol Grafiği</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Üçüncü dereceden fonksiyon", "icerik": [
            "Üçüncü dereceden bir fonksiyonun türevi ikinci derecedendir ve genellikle iki noktada sıfır olur. Böylece grafik üç aralığa bölünür.",
            koordinat_grafik("y = x³ - 3x grafiği", [("", lambda x: x ** 3 - 3 * x)], (-2.5, 2.5), (-3, 3), adim=1,
                             noktalar=[(-1, 2, "", True), (1, -2, "", True)], dikeyler=[-1, 1]),
            ornek(
                "$f(x)=x^3-3x$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=3x^2-3=3(x-1)(x+1)$ dir; türev $-1$ ve $1$ de sıfır olur.",
                "Türev $x<-1$ ve $x>1$ için pozitif, $-1<x<1$ için negatiftir: fonksiyon $(-\\infty, -1)$ ve $(1, \\infty)$ da artan, $(-1, 1)$ de azalandır."),
            "Grafikte kesikli çizgiler türevin sıfır olduğu noktaları gösterir. Grafik bu çizgiler arasında alçalır, dışında yükselir; işaretlenen iki nokta grafiğin tepe ve çukur noktalarıdır.",
        ]},
        {"baslik": "Üç aralıklı bir örnek daha", "icerik": [
            "Türevin kökleri tam sayı olduğunda işaret tablosu çok hızlı yapılır ve hesap makinesine gerek kalmaz. Türev çarpanlarına ayrıldıktan sonra her aralıktan bir sayı denenir.",
            ornek(
                "$f(x)=x^3-6x^2+9x+1$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=3x^2-12x+9=3(x-1)(x-3)$ tür.",
                "Fonksiyon $(-\\infty, 1)$ de artan, $(1, 3)$ te azalan, $(3, \\infty)$ da yeniden artandır."),
        ]},
        {"baslik": "Her yerde artan fonksiyon", "icerik": [
            "Türevi her gerçek sayıda pozitif olan fonksiyon her yerde artandır. Bu fonksiyonların grafiği hiçbir yerde alçalmaz ve yatay eksene paralel bir doğru grafiği en fazla bir kez keser.",
            ornek(
                "$f(x)=x^3+x$ fonksiyonu verilsin.",
                "Fonksiyonun her yerde artan olduğunu gösterelim.",
                "$f'(x)=3x^2+1$ olur.",
                "$3x^2 \\ge 0$ olduğu için $f'(x) \\ge 1>0$ dır; fonksiyon her yerde artandır."),
        ]},
        {"baslik": "Türevin sıfır olduğu ama artan", "icerik": [
            "Türevin bir noktada sıfır olması, fonksiyonun orada yön değiştirdiği anlamına gelmez. Türev sıfır olduğu noktanın iki yanında aynı işareti taşıyorsa fonksiyon aynı yönde devam eder.",
            ornek(
                "$f(x)=x^3$ fonksiyonu verilsin.",
                "Fonksiyonun artan olup olmadığını inceleyelim.",
                "$f'(x)=3x^2$ dir; türev $x=0$ da sıfır, diğer bütün noktalarda pozitiftir.",
                "Türev sıfırın iki yanında pozitif olduğu için fonksiyon her yerde artandır."),
            "Bu yüzden artanlık için tam kural şöyledir: türev bir aralıkta sıfır ya da pozitifse ve yalnızca tek tek noktalarda sıfır oluyorsa fonksiyon o aralıkta artandır.",
            hap("Türevin bir noktada sıfır olması yön değişimi demek değildir; noktanın iki yanındaki işaret karşılaştırılır."),
        ]},
        {"baslik": "Her yerde artan olma koşulu", "icerik": [
            "Parametreli bir fonksiyonun her yerde artan olması için türevinin hiçbir yerde negatif olmaması gerekir. Türev ikinci dereceden bir ifadeyse bu, baş katsayının pozitif ve diskriminantın sıfır ya da negatif olması demektir.",
            ornek(
                "$f(x)=x^3+ax^2+3x$ fonksiyonu verilsin.",
                "Fonksiyonun her yerde artan olması için $a$ nın alabileceği değerleri bulalım.",
                "$f'(x)=3x^2+2ax+3$ tür; her yerde negatif olmaması için $\\Delta=4a^2-36 \\le 0$ olmalıdır.",
                "$a^2 \\le 9$, yani $-3 \\le a \\le 3$ bulunur."),
            "Diskriminantın sıfır olduğu uç değerlerde türev tek bir noktada sıfır olur; önceki bölümde görüldüğü gibi bu, artanlığı bozmaz.",
        ]},
        {"baslik": "Rasyonel fonksiyon", "icerik": [
            "Rasyonel fonksiyonlarda türevin paydası kare olduğu için pozitiftir ve işareti yalnızca pay belirler. Tanım kümesi dışındaki noktalar da işaret tablosuna eklenir.",
            ornek(
                "$f(x)=\\dfrac{x}{x^2+1}$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=\\dfrac{1-x^2}{(x^2+1)^2}$ olur; pay $-1$ ve $1$ de sıfırdır.",
                "Fonksiyon $(-1, 1)$ de artan, $(-\\infty, -1)$ ve $(1, \\infty)$ da azalandır."),
        ]},
        {"baslik": "Asimptot ve aralıkların birleşimi", "icerik": [
            "Tanım kümesi parçalıysa artanlık ve azalanlık her parçada ayrı ayrı söylenir. Parçaların birleşimi üzerinde aynı sonuç geçerli olmayabilir.",
            ornek(
                "$f(x)=\\dfrac{x+1}{x-1}$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları inceleyelim.",
                "$f'(x)=-\\dfrac{2}{(x-1)^2}<0$ dır; fonksiyon $(-\\infty, 1)$ ve $(1, \\infty)$ aralıklarının her birinde azalandır.",
                "Ama birleşim üzerinde azalan değildir: $0<2$ olduğu hâlde $f(0)=-1<f(2)=3$ tür."),
            dikkat(
                "Kesikli aralıklarda birleşim yazıp fonksiyonun orada azalan olduğunu söylemek.",
                "Azalanlık tek bir aralık üzerinde tanımlanır. Asimptotun iki yanındaki aralıklar ayrı ayrı yazılmalıdır."),
        ]},
        {"baslik": "Mutlak değerli fonksiyon", "icerik": [
            "Mutlak değerli fonksiyonlarda türev, içteki ifadenin sıfır olduğu noktalarda tanımsız olabilir. Bu noktalar da işaret tablosuna kritik nokta olarak eklenir; fonksiyon bu köşelerde de yön değiştirebilir.",
            ornek(
                "$f(x)=|x^2-4|$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$|x|>2$ iken $f(x)=x^2-4$ ve $f'(x)=2x$; $|x|<2$ iken $f(x)=4-x^2$ ve $f'(x)=-2x$ olur. Kritik noktalar $-2$, $0$ ve $2$ dir.",
                "Fonksiyon $(-\\infty, -2)$ de azalan, $(-2, 0)$ da artan, $(0, 2)$ de azalan, $(2, \\infty)$ da artandır."),
        ]},
        {"baslik": "Köklü fonksiyon", "icerik": [
            "Köklü fonksiyonlarda tanım kümesi kök içinin negatif olmadığı değerlerle sınırlıdır. İşaret tablosu yalnızca bu kapalı aralıkta yapılır.",
            ornek(
                "$f(x)=\\sqrt{4-x^2}$ fonksiyonu verilsin, $-2 \\le x \\le 2$.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=-\\dfrac{x}{\\sqrt{4-x^2}}$ olur; pay $x=0$ da sıfırdır.",
                "Fonksiyon $[-2, 0]$ da artan, $[0, 2]$ de azalandır; grafiği yarım çemberdir ve en yüksek noktası $(0, 2)$ dir."),
        ]},
        {"baslik": "Üstel fonksiyonlu örnek", "icerik": [
            "Üstel fonksiyon her zaman pozitif olduğu için türevde ortak çarpan olarak çıktığında işarete hiçbir şekilde etki etmez. İşaret yalnızca kalan çarpandan okunur.",
            ornek(
                "$f(x)=x e^x$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=e^x(1+x)$ olur; işaret yalnızca $1+x$ e bağlıdır.",
                "Fonksiyon $(-\\infty, -1)$ de azalan, $(-1, \\infty)$ da artandır."),
        ]},
        {"baslik": "Logaritmik fonksiyonlu örnek", "icerik": [
            "Logaritmalı fonksiyonlarda tanım kümesi pozitif sayılarla sınırlıdır. İşaret tablosu yalnızca bu küme üzerinde yapılır ve sıfırın solu tabloya hiç yazılmaz.",
            ornek(
                "$f(x)=\\dfrac{\\ln x}{x}$ fonksiyonu verilsin, $x>0$.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=\\dfrac{1-\\ln x}{x^2}$ olur; pay $x=e$ de sıfırdır.",
                "Fonksiyon $(0, e)$ de artan, $(e, \\infty)$ da azalandır."),
            "Bu sonuç ilginç bir karşılaştırmayı mümkün kılar: fonksiyon $e$ den sonra azaldığı için $\\dfrac{\\ln 3}{3}>\\dfrac{\\ln 4}{4}$ tür; buradan $4^3>3^4$ değil, $3^4>4^3$ olduğu çıkar ve gerçekten $81>64$ tür.",
        ]},
        {"baslik": "Trigonometrik fonksiyonlar", "icerik": [
            "Trigonometrik fonksiyonlarda türevin sıfır olduğu noktalar periyodik olarak ve sonsuz kez tekrar eder. Bu yüzden inceleme genellikle bir periyotluk aralıkta yapılır.",
            ornek(
                "$[0, 2\\pi]$ aralığında $f(x)=\\sin x$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f'(x)=\\cos x$ tir ve $\\dfrac{\\pi}{2}$ ile $\\dfrac{3\\pi}{2}$ de sıfır olur.",
                "Sinüs $\\left[0, \\dfrac{\\pi}{2}\\right]$ ve $\\left[\\dfrac{3\\pi}{2}, 2\\pi\\right]$ da artan, $\\left[\\dfrac{\\pi}{2}, \\dfrac{3\\pi}{2}\\right]$ de azalandır."),
            ornek(
                "$[0, 2\\pi]$ aralığında $f(x)=x+2\\cos x$ fonksiyonu verilsin.",
                "Azalan olduğu aralığı bulalım.",
                "$f'(x)=1-2\\sin x$ tir; $\\sin x=\\dfrac{1}{2}$ için $x=\\dfrac{\\pi}{6}$ ya da $\\dfrac{5\\pi}{6}$ olur.",
                "Türev bu iki nokta arasında negatiftir; fonksiyon $\\left(\\dfrac{\\pi}{6}, \\dfrac{5\\pi}{6}\\right)$ aralığında azalandır."),
        ]},
        {"baslik": "Grafikten türevin işaretini okumak", "icerik": [
            "Fonksiyonun grafiği verilmişse türevin işareti doğrudan okunur: grafiğin yükseldiği aralıklarda türev pozitif, alçaldığı aralıklarda negatif, tepe ve çukur noktalarında sıfırdır.",
            "Tersine, türevin grafiği verilmişse fonksiyonun davranışı okunur. Türev grafiğinin yatay eksenin üstünde kaldığı aralıklarda fonksiyon artan, altında kaldığı aralıklarda azalandır. Türev grafiğinin ekseni kestiği noktalar fonksiyonun yön değiştirebileceği yerlerdir. Bu iki okuma yönü sınavlarda sık sorulur ve birbirine karıştırılmamalıdır.",
        ]},
        {"baslik": "Türevle eşitsizlik ispatı", "icerik": [
            "Artanlık, iki ifade arasındaki bir eşitsizliği ispatlamak için güçlü bir araçtır. İki ifadenin farkı bir fonksiyon olarak yazılır, türevinden davranışı incelenir ve en küçük değerinin sıfır olduğu gösterilir.",
            ornek(
                "Her $x$ için $e^x \\ge 1+x$ eşitsizliği verilsin.",
                "Eşitsizliği türevle ispatlayalım.",
                "$g(x)=e^x-1-x$ olsun; $g'(x)=e^x-1$ dir ve $x<0$ için negatif, $x>0$ için pozitiftir.",
                "$g$ sıfıra kadar azalır, sonra artar; en küçük değeri $g(0)=0$ dır. Bu yüzden her $x$ için $g(x) \\ge 0$ olur."),
            ornek(
                "Pozitif $x$ ler için $x>\\sin x$ eşitsizliği verilsin.",
                "Eşitsizliği türevle ispatlayalım.",
                "$g(x)=x-\\sin x$ için $g'(x)=1-\\cos x \\ge 0$ dır ve türev yalnızca tek tek noktalarda sıfırdır.",
                "$g$ artandır ve $g(0)=0$ olduğundan pozitif $x$ ler için $g(x)>0$, yani $x>\\sin x$ olur."),
        ]},
        {"baslik": "Artanlıkla eşitsizlik çözmek", "icerik": [
            "Artan bir fonksiyonda büyük girdi büyük çıktı verir. Bu yüzden $f$ artansa $f(a)<f(b)$ eşitsizliği $a<b$ eşitsizliğine denktir. Böylece çözülmesi zor görünen bazı eşitsizlikler kolayca çözülür.",
            ornek(
                "$x^3+x>2$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "$f(x)=x^3+x$ her yerde artandır ve $f(1)=2$ dir.",
                "Eşitsizlik $f(x)>f(1)$ biçimindedir; artanlık nedeniyle $x>1$ bulunur."),
        ]},
        {"baslik": "Kök sayısı", "icerik": [
            "Bir aralıkta artan ya da azalan bir fonksiyon o aralıkta her değeri en fazla bir kez alır. Bu yüzden artanlık, bir denklemin kaç kökü olduğunu belirlemeye yardım eder.",
            ornek(
                "$x^3+x-1=0$ denklemi verilsin.",
                "Denklemin kaç gerçek kökü olduğunu bulalım.",
                "$f(x)=x^3+x-1$ in türevi $3x^2+1>0$ olduğundan fonksiyon her yerde artandır; bu yüzden en fazla bir kökü vardır.",
                "$f(0)=-1<0$ ve $f(1)=1>0$ olduğundan bir kök vardır; denklemin tam olarak bir gerçek kökü bulunur."),
            hap("Bir aralıkta artan ya da azalan bir fonksiyon o aralıkta her değeri en fazla bir kez alır."),
        ]},
        {"baslik": "Artanlık ve birebirlik", "icerik": [
            "Bir aralıkta artan ya da azalan bir fonksiyon o aralıkta birebirdir: farklı $x$ ler farklı değerler verir. Birebir fonksiyonların tersi tanımlıdır; bu yüzden türevin işareti, bir fonksiyonun tersinin olup olmadığını da gösterir.",
            "Örneğin $x^3+x$ her yerde artan olduğu için bütün gerçek sayılarda tersi vardır, ama bu tersin formülünü yazmak kolay değildir. $x^2$ ise her yerde birebir değildir; ancak $[0, \\infty)$ aralığına kısıtlandığında artan olur ve tersi $\\sqrt{x}$ tir. Ters fonksiyon kavramı için <a href=\"/blog/ters-fonksiyon/\">Ters Fonksiyon</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Günlük hayatta artan ve azalan", "icerik": [
            "Bir aracın konumunun türevi hızıdır. Hız pozitifken araç ileri gider ve konum artar, negatifken geri gider ve konum azalır. Hızın sıfır olduğu anlar aracın durup yön değiştirebileceği anlardır.",
            "Bir işletmenin kârı da benzer biçimde incelenir: kâr fonksiyonunun türevi pozitif olduğu sürece üretimi artırmak kârı artırır. Türev negatife döndüğünde üretimi artırmak kârı azaltmaya başlar. Bu dönüm noktası, kârın en yüksek olduğu üretim miktarıdır ve <a href=\"/blog/maksimum-minimum/\">Türevde Maksimum ve Minimum Nasıl Bulunur?</a> yazısının konusudur.",
            hap("Bir fırının günlük kârı $x$ tepsi pişirildiğinde $K(x)=-x^2+40x-300$ lira olsun.", "$K'(x)=-2x+40$ olduğu için $20$ tepsiye kadar her ek tepsi kârı artırır, $20$ tepsiden sonra azaltır.", gunluk=True),
        ]},
        {"baslik": "Sınavda artan ve azalan", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) bu konu; artan ve azalan aralıkları bulma, her yerde artan olma koşulu, türev grafiğinden fonksiyon davranışı okuma ve parametreli sorular biçiminde karşına çıkabilir.",
                "Maksimum ve minimum soruları da aynı işaret tablosuna dayanır."),
            "Türevi mutlaka çarpanlarına ayır; işaret tablosu ancak böyle hatasız yapılır. Parametreli her yerde artanlık sorusunda türev ikinci dereceden çıkıyorsa diskriminant koşulunu yaz, eşitlik durumunu da dahil etmeyi unutma.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Fonksiyonun işaretine bakmak", "Türevin işaretine bakılır"],
                ["Türev sıfırsa yön değişir sanmak", "İki yandaki işaret karşılaştırılır"],
                ["Tanım kümesini unutmak", "İşaret tablosu tanım kümesinde yapılır"],
                ["Asimptotun iki yanını birleştirmek", "Aralıklar ayrı yazılır"],
                ["Her yerde artanlıkta $\\Delta<0$ yazmak", "$\\Delta \\le 0$"],
                ["Türev grafiğini fonksiyon grafiği gibi okumak", "Türevin işaretine bakılır"],
            ]),
            "En sık hata fonksiyonun kendisinin pozitif olmasını artanlıkla karıştırmaktır. Negatif değerler alan bir fonksiyon da artan olabilir; önemli olan değerin kendisi değil, değişimin yönüdür.",
        ]},
    ],
    "sss": [
        ("Artan fonksiyon nedir?",
         "Bir aralıkta x büyüdükçe değeri de büyüyen fonksiyondur. Aralıktaki her x1 küçüktür x2 için f(x1) küçüktür f(x2) olur."),
        ("Artan ve azalan aralıklar türevle nasıl bulunur?",
         "Türev alınır, sıfır ve tanımsız olduğu noktalar bulunur ve bu noktalar arasındaki aralıklarda türevin işaretine bakılır. Pozitif türev artan, negatif türev azalan demektir."),
        ("Türev sıfır olursa fonksiyon yön değiştirir mi?",
         "Her zaman değil. x küp fonksiyonunda türev sıfırda sıfırdır ama iki yanında pozitif olduğu için fonksiyon artmaya devam eder."),
        ("Bir fonksiyonun her yerde artan olması için ne gerekir?",
         "Türevin hiçbir yerde negatif olmaması gerekir. Türev ikinci dereceden bir ifadeyse baş katsayı pozitif, diskriminant sıfır ya da negatif olmalıdır."),
        ("1 bölü x azalan bir fonksiyon mudur?",
         "Eksi sonsuzdan sıfıra ve sıfırdan artı sonsuza kadar olan aralıkların her birinde azalandır, ama bu iki aralığın birleşiminde azalan değildir."),
        ("Artan fonksiyonun tersi var mıdır?",
         "Evet. Bir aralıkta artan fonksiyon o aralıkta birebirdir ve tersi tanımlıdır."),
        ("Türev grafiğinden fonksiyonun artan olduğu yer nasıl okunur?",
         "Türev grafiğinin yatay eksenin üstünde kaldığı aralıklarda fonksiyon artan, altında kaldığı aralıklarda azalandır."),
    ],
    "kontrol": [
        "Artan ve azalan fonksiyonu tanımlayabiliyorum.",
        "Türevin işaretiyle fonksiyonun yönü arasındaki ilişkiyi açıklayabiliyorum.",
        "İşaret tablosu yöntemiyle artan ve azalan aralıkları bulabiliyorum.",
        "Polinom fonksiyonların artan ve azalan aralıklarını bulabiliyorum.",
        "Rasyonel, üstel ve logaritmik fonksiyonları inceleyebiliyorum.",
        "Trigonometrik fonksiyonların artan ve azalan aralıklarını bulabiliyorum.",
        "Her yerde artan olma koşulunu parametreli sorularda kullanabiliyorum.",
        "Türevin sıfır olduğu ama yön değişmeyen durumları tanıyabiliyorum.",
        "Türevle eşitsizlik ispatlayabiliyorum.",
        "Artanlıkla kök sayısını ve birebirliği belirleyebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["maksimum-minimum", "teget-denklemi", "turev-konu-anlatimi"],
}
