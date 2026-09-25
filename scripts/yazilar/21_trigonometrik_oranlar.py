# scripts/yazilar/21_trigonometrik_oranlar.py — Trigonometrik Oranlar (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "trigonometrik-oranlar",
    "baslik": "Trigonometrik Oranlar: Sinüs, Kosinüs, Tanjant ve Kotanjant",
    "aciklama": "Sinüs, kosinüs, tanjant ve kotanjant nedir? Dik üçgende oranlar, bir orandan diğerleri, özel açılar, kenar bulma, yükseklik problemi ve alan; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "trigonometrik-oranlar",
    "kapak_alt": "Trigonometrik oranlar: dönen bir kol ve renkli dik üçgen kenarlarıyla sinüs ve kosinüs ilişkisini inceleyen iki öğrenci",
    "ozet": "Sinüs, kosinüs, tanjant ve kotanjant, bir dik üçgenin kenarları arasındaki oranlardır ve yalnızca açıya bağlıdır: üçgen büyüse de küçülse de aynı açı için oranlar değişmez. Bu yazıda dik üçgende kenar adlarını, dört temel oranı ve sekant ile kosekantı, oranlar arasındaki bağıntıları, bir orandan diğerlerini bulmayı, özel açıları, kenar ve hipotenüs hesabını, oranların açıya göre değişimini, yükseklik ve eğik düzlem problemlerini ve üçgenin alan formülünü çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Dik üçgende kenar adları", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dik üçgeni, Pisagor bağıntısını ve açı ölçülerini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/trigonometri-konu-anlatimi/\">Trigonometri Konu Anlatımı</a> yazısına göz at."),
            "Bir dik üçgende dik açının karşısındaki en uzun kenara <strong>hipotenüs</strong> denir. Dar açılardan biri $\\alpha$ seçildiğinde, bu açının karşısındaki kenar <strong>karşı dik kenar</strong>, açının bir kolunu oluşturan diğer dik kenar ise <strong>komşu dik kenar</strong> olur.",
            "Kenar adları seçilen açıya göre değişir. Aynı üçgende diğer dar açı seçilirse karşı ve komşu kenarlar yer değiştirir; hipotenüs ise her zaman aynıdır. Kapaktaki öğrencilerin renkli çubuklarla kurduğu üçgende mavi kol hipotenüsü, kırmızı ve yeşil çubuklar da iki dik kenarı temsil ediyor.",
            hap("Hipotenüs dik açının karşısındadır ve en uzun kenardır.",
                "Karşı ve komşu kenar, seçilen açıya göre belirlenir."),
        ]},
        {"baslik": "Sinüs", "icerik": [
            "Bir dar açının <strong>sinüsü</strong>, karşı dik kenarın hipotenüse oranıdır ve $\\sin \\alpha$ ile gösterilir. Hipotenüs en uzun kenar olduğu için bu oran $0$ ile $1$ arasındadır; karşı kenar hipotenüse ne kadar yakınsa sinüs de $1$ e o kadar yaklaşır.",
            "$$\\sin \\alpha=\\dfrac{\\text{karşı dik kenar}}{\\text{hipotenüs}}$$",
            ornek(
                "Dik kenarları $5$ ve $12$ olan bir dik üçgende $5$ birimlik kenarın karşısındaki açı $\\alpha$ olsun.",
                "$\\sin \\alpha$ yı bulalım.",
                "Hipotenüs: $\\sqrt{25+144}=13$.",
                "$\\sin \\alpha=\\dfrac{5}{13}$."),
        ]},
        {"baslik": "Kosinüs", "icerik": [
            "Bir dar açının <strong>kosinüsü</strong>, komşu dik kenarın hipotenüse oranıdır ve $\\cos \\alpha$ ile gösterilir. Sinüs gibi kosinüs de dar açılarda $0$ ile $1$ arasındadır.",
            "$$\\cos \\alpha=\\dfrac{\\text{komşu dik kenar}}{\\text{hipotenüs}}$$",
            ornek(
                "Aynı $5$, $12$, $13$ üçgeni verilsin.",
                "$\\cos \\alpha$ yı bulalım.",
                "$\\alpha$ nın komşu dik kenarı $12$ dir.",
                "$\\cos \\alpha=\\dfrac{12}{13}$."),
            "Sinüs ve kosinüs birlikte temel özdeşliği sağlar: $(\\dfrac{5}{13})^2+(\\dfrac{12}{13})^2=\\dfrac{25+144}{169}=1$. Bu eşitlik, Pisagor bağıntısının hipotenüsün karesine bölünmüş hâlidir.",
        ]},
        {"baslik": "Tanjant", "icerik": [
            "Bir dar açının <strong>tanjantı</strong>, karşı dik kenarın komşu dik kenara oranıdır ve $\\tan \\alpha$ ile gösterilir. Tanjant hipotenüse bağlı olmadığı için $1$ den büyük de olabilir. Karşı kenar komşu kenardan uzunsa, yani açı $45^\\circ$ den büyükse tanjant $1$ i aşar.",
            "$$\\tan \\alpha=\\dfrac{\\text{karşı dik kenar}}{\\text{komşu dik kenar}}$$",
            ornek(
                "Aynı üçgen verilsin.",
                "$\\tan \\alpha$ yı bulalım ve sinüs ile kosinüsle ilişkisini gösterelim.",
                "$\\tan \\alpha=\\dfrac{5}{12}$.",
                "$\\dfrac{\\sin \\alpha}{\\cos \\alpha}=\\dfrac{5}{13}:\\dfrac{12}{13}=\\dfrac{5}{12}$; tanjant, sinüsün kosinüse bölümüdür."),
            hap("Tanjant, karşı dik kenarın komşu dik kenara oranıdır.", "Hipotenüse bağlı olmadığı için $1$ den büyük olabilir: açı $45^\\circ$ den büyükse tanjant $1$ i aşar."),
        ]},
        {"baslik": "Kotanjant", "icerik": [
            "Bir dar açının <strong>kotanjantı</strong>, komşu dik kenarın karşı dik kenara oranıdır ve $\\cot \\alpha$ ile gösterilir. Tanjantın çarpmaya göre tersidir; bu yüzden ikisinin çarpımı her zaman $1$ dir.",
            "$$\\cot \\alpha=\\dfrac{\\text{komşu dik kenar}}{\\text{karşı dik kenar}}$$",
            ornek(
                "Aynı üçgen verilsin.",
                "$\\cot \\alpha$ yı bulalım.",
                "$\\cot \\alpha=\\dfrac{12}{5}$.",
                "$\\tan \\alpha \\cdot \\cot \\alpha=\\dfrac{5}{12} \\cdot \\dfrac{12}{5}=1$."),
        ]},
        {"baslik": "Sekant ve kosekant", "icerik": [
            "Kosinüs ve sinüsün çarpmaya göre terslerine de ayrı adlar verilir: <strong>sekant</strong> kosinüsün, <strong>kosekant</strong> sinüsün tersidir. Bu iki oran bazı özdeşliklerde ve ileri konularda karşına çıkar.",
            tablo(["Oran", "Tanım", "$5$, $12$, $13$ üçgeninde"], [
                ["$\\sec \\alpha$", "$\\dfrac{1}{\\cos \\alpha}$", "$\\dfrac{13}{12}$"],
                ["$\\csc \\alpha$", "$\\dfrac{1}{\\sin \\alpha}$", "$\\dfrac{13}{5}$"],
            ]),
        ]},
        {"baslik": "Oranlar yalnızca açıya bağlıdır", "icerik": [
            "Aynı açılı iki dik üçgen benzerdir; kenarları orantılıdır. Bu yüzden oranlar üçgenin büyüklüğüne değil, yalnızca açıya bağlıdır. Kenarları $5$, $12$, $13$ olan üçgen ile kenarları $10$, $24$, $26$ olan üçgende aynı açının sinüsü $\\dfrac{5}{13}=\\dfrac{10}{26}$ dur.",
            "Trigonometrik oranların bir açının fonksiyonu olarak tanımlanabilmesi bu gözleme dayanır. Açı sabit kaldıkça oran değişmez; açı değiştikçe oran da değişir. Bu yüzden bir oran bilindiğinde, o orana uyan herhangi bir dik üçgen çizilerek hesap yapılabilir; hangi büyüklükte çizildiğinin önemi yoktur.",
            hap("Aynı açılı dik üçgenler benzer olduğu için trigonometrik oranlar üçgenin büyüklüğüne değil, yalnızca açıya bağlıdır."),
        ]},
        {"baslik": "Tümler açılarda oranlar", "icerik": [
            "Bir dik üçgenin iki dar açısı tümlerdir: toplamları $90^\\circ$ dir. Bir açının karşı kenarı öteki açının komşu kenarı olduğu için bir açının sinüsü, tümlerinin kosinüsüne eşittir; tanjant ile kotanjant da aynı biçimde yer değiştirir.",
            tablo(["$\\alpha+\\beta=90^\\circ$ ise", ""], [
                ["$\\sin \\alpha$", "$\\cos \\beta$"],
                ["$\\tan \\alpha$", "$\\cot \\beta$"],
            ]),
            ornek(
                "$\\sin 35^\\circ=\\cos x$ eşitliği verilsin ve $x$ dar açı olsun.",
                "$x$ i bulalım.",
                "Tümler açılarda sinüs ile kosinüs eşittir.",
                "$x=90^\\circ-35^\\circ=55^\\circ$."),
            hap("$\\alpha+\\beta=90^\\circ$ ise $\\sin \\alpha=\\cos \\beta$ ve $\\tan \\alpha=\\cot \\beta$ olur."),
        ]},
        {"baslik": "Oranlar arasındaki bağıntılar", "icerik": [
            "Dört oran birbirinden bağımsız değildir; biri bilindiğinde diğerleri bulunur. Bu bağlantıyı sağlayan temel eşitlikler şunlardır:",
            tablo(["Bağıntı", "Açıklama"], [
                ["$\\sin^2 \\alpha+\\cos^2 \\alpha=1$", "Pisagor bağıntısından"],
                ["$\\tan \\alpha=\\dfrac{\\sin \\alpha}{\\cos \\alpha}$", "Tanjantın tanımından"],
                ["$\\tan \\alpha \\cdot \\cot \\alpha=1$", "Ters oranlar"],
                ["$1+\\tan^2 \\alpha=\\dfrac{1}{\\cos^2 \\alpha}$", "Temel özdeşlik $\\cos^2$ ye bölünür"],
            ]),
            "Bu bağıntıların ayrıntısı ve daha fazlası <a href=\"/blog/trigonometrik-ozdeslikler-formuller/\">Trigonometrik Özdeşlikler ve Formüller</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Bir orandan diğerlerini bulmak", "icerik": [
            "Bir oran verildiğinde en pratik yol, o orana uyan bir dik üçgen çizmektir. Oranın payı ve paydası iki kenar olarak alınır, üçüncü kenar Pisagor bağıntısıyla bulunur ve diğer oranlar üçgenden okunur.",
            ornek(
                "$\\alpha$ dar açı ve $\\tan \\alpha=\\dfrac{3}{4}$ olsun.",
                "Diğer oranları bulalım.",
                "Karşı kenar $3$, komşu kenar $4$ alınır; hipotenüs $5$ tir.",
                "$\\sin \\alpha=\\dfrac{3}{5}$, $\\cos \\alpha=\\dfrac{4}{5}$, $\\cot \\alpha=\\dfrac{4}{3}$."),
            ornek(
                "$\\alpha$ dar açı ve $\\cos \\alpha=\\dfrac{2}{3}$ olsun.",
                "$\\sin \\alpha$ ve $\\tan \\alpha$ yı bulalım.",
                "Komşu kenar $2$, hipotenüs $3$; karşı kenar $\\sqrt{9-4}=\\sqrt{5}$.",
                "$\\sin \\alpha=\\dfrac{\\sqrt{5}}{3}$ ve $\\tan \\alpha=\\dfrac{\\sqrt{5}}{2}$."),
        ]},
        {"baslik": "Özel açılar", "icerik": [
            "$30^\\circ$, $45^\\circ$ ve $60^\\circ$ açılarının oranları iki özel üçgenden bulunur. Kenarları $1$, $\\sqrt{3}$, $2$ olan üçgenin açıları $30^\\circ$, $60^\\circ$, $90^\\circ$; kenarları $1$, $1$, $\\sqrt{2}$ olan üçgenin açıları $45^\\circ$, $45^\\circ$, $90^\\circ$ dir.",
            tablo(["Açı", "$\\sin$", "$\\cos$", "$\\tan$", "$\\cot$"], [
                ["$30^\\circ$", "$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{\\sqrt{3}}{3}$", "$\\sqrt{3}$"],
                ["$45^\\circ$", "$\\dfrac{\\sqrt{2}}{2}$", "$\\dfrac{\\sqrt{2}}{2}$", "$1$", "$1$"],
                ["$60^\\circ$", "$\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{1}{2}$", "$\\sqrt{3}$", "$\\dfrac{\\sqrt{3}}{3}$"],
            ]),
            dikkat(
                "$30^\\circ$ ile $60^\\circ$ nin değerlerini karıştırmak.",
                "Küçük açının karşısındaki kenar da küçüktür. $30^\\circ$ nin karşısındaki kenar en kısa kenardır, bu yüzden $\\sin 30^\\circ$ küçük değer olan $\\dfrac{1}{2}$ dir; $\\sin 60^\\circ$ ise daha büyük olan $\\dfrac{\\sqrt{3}}{2}$ tür."),
        ]},
        {"baslik": "Orandan açıyı bulmak", "icerik": [
            "Bir oranın değeri özel açılardan birine karşılık geliyorsa açı doğrudan bulunur. Bu, kenar uzunlukları verilen bir dik üçgenin açılarını bulmanın da yoludur: önce bir oran hesaplanır, sonra tabloya bakılır.",
            ornek(
                "Bir dik üçgende dik kenarlar $5$ ve $5\\sqrt{3}$ tür.",
                "Kısa kenarın karşısındaki açıyı bulalım.",
                "$\\tan \\alpha=\\dfrac{5}{5\\sqrt{3}}=\\dfrac{1}{\\sqrt{3}}=\\dfrac{\\sqrt{3}}{3}$.",
                "Tanjantı $\\dfrac{\\sqrt{3}}{3}$ olan dar açı $30^\\circ$ dir; diğer dar açı $60^\\circ$ dir."),
        ]},
        {"baslik": "Kenar bulmak", "icerik": [
            "Bir açı ve bir kenar bilindiğinde diğer kenarlar oranlarla bulunur. Hangi oranın kullanılacağı, bilinen ve istenen kenarların açıya göre konumuna bağlıdır: hipotenüs ve karşı kenar varsa sinüs, hipotenüs ve komşu kenar varsa kosinüs, iki dik kenar varsa tanjant kullanılır.",
            ornek(
                "Hipotenüsü $12$ olan bir dik üçgende bir açı $30^\\circ$ dir.",
                "Dik kenarları bulalım.",
                "Karşı kenar: $12 \\cdot \\sin 30^\\circ=6$.",
                "Komşu kenar: $12 \\cdot \\cos 30^\\circ=6\\sqrt{3}$."),
            ornek(
                "Bir dik üçgende $45^\\circ$ lik açının karşısındaki kenar $7$ dir.",
                "Hipotenüsü bulalım.",
                "$\\sin 45^\\circ=\\dfrac{7}{h}$, yani $h=\\dfrac{7}{\\dfrac{\\sqrt{2}}{2}}$.",
                "$h=7\\sqrt{2}$."),
        ]},
        {"baslik": "Çevre ve alan hesabı", "icerik": [
            "Bir dik üçgenin hipotenüsü ve bir açısı bilindiğinde bütün kenarlar bulunur; buradan çevre ve alan da hesaplanır. Bu tür sorularda önce iki dik kenar sinüs ve kosinüsle bulunur.",
            ornek(
                "Hipotenüsü $10$ olan bir dik üçgende bir açı $30^\\circ$ dir.",
                "Üçgenin çevresini ve alanını bulalım.",
                "Dik kenarlar: $10 \\cdot \\sin 30^\\circ=5$ ve $10 \\cdot \\cos 30^\\circ=5\\sqrt{3}$.",
                "Çevre: $15+5\\sqrt{3}$. Alan: $\\dfrac{5 \\cdot 5\\sqrt{3}}{2}=\\dfrac{25\\sqrt{3}}{2}$."),
        ]},
        {"baslik": "Oranların açıya göre değişimi", "icerik": [
            "Dar açı $0^\\circ$ den $90^\\circ$ ye doğru büyürken karşı kenar uzar, komşu kenar kısalır. Bu yüzden sinüs ve tanjant artar, kosinüs ve kotanjant azalır.",
            tablo(["Oran", "$0^\\circ$ de", "$90^\\circ$ de", "Açı büyürken"], [
                ["$\\sin$", "$0$", "$1$", "Artar"],
                ["$\\cos$", "$1$", "$0$", "Azalır"],
                ["$\\tan$", "$0$", "Tanımsız", "Artar"],
            ]),
            ornek(
                "$\\sin 40^\\circ$ ile $\\sin 50^\\circ$, $\\cos 40^\\circ$ ile $\\cos 50^\\circ$ ve $\\tan 50^\\circ$ ile $1$ karşılaştırılsın.",
                "Hesap yapmadan karşılaştıralım.",
                "Sinüs artan olduğu için $\\sin 40^\\circ<\\sin 50^\\circ$; kosinüs azalan olduğu için $\\cos 40^\\circ>\\cos 50^\\circ$.",
                "$\\tan 45^\\circ=1$ ve tanjant artan olduğu için $\\tan 50^\\circ>1$."),
        ]},
        {"baslik": "Yükseklik açısı problemi", "icerik": [
            "Yerdeki bir noktadan bir cismin tepesine bakıldığında bakış doğrusunun yerle yaptığı açıya <strong>yükseklik açısı</strong> denir. Cisme olan uzaklık ve yükseklik açısı biliniyorsa yükseklik tanjantla bulunur.",
            ornek(
                "Bir binaya $20$ metre uzaktan bakıldığında yükseklik açısı $60^\\circ$ dir.",
                "Binanın yüksekliğini bulalım.",
                "$\\tan 60^\\circ=\\dfrac{h}{20}$.",
                "$h=20\\sqrt{3}$, yaklaşık $34.64$ metre."),
            "Aynı durumda bina ile gözlemci arasındaki bakış doğrusunun uzunluğu da bulunabilir: hipotenüs $\\dfrac{20}{\\cos 60^\\circ}=40$ metredir.",
        ]},
        {"baslik": "İki gözlem noktası", "icerik": [
            "Klasik bir problemde bir cismin tepesine aynı doğrultudaki iki noktadan bakılır. İki yükseklik açısı ve noktalar arasındaki uzaklık biliniyorsa, iki dik üçgen için tanjant eşitlikleri yazılır ve ortak yükseklik bulunur.",
            ornek(
                "Bir kulenin tepesine, aralarında $10$ metre bulunan iki noktadan $60^\\circ$ ve $30^\\circ$ lik açılarla bakılıyor. Yakın nokta ile kule arasındaki uzaklık $x$ olsun.",
                "Kulenin yüksekliğini bulalım.",
                "Yakın noktadan: $h=x\\tan 60^\\circ=x\\sqrt{3}$. Uzak noktadan: $h=(x+10)\\tan 30^\\circ=\\dfrac{x+10}{\\sqrt{3}}$.",
                "Eşitlenir: $3x=x+10$, yani $x=5$. Yükseklik $h=5\\sqrt{3}$, yaklaşık $8.66$ metredir."),
            "Sonuç ilginç bir özellik de gösterir: uzak noktadaki $30^\\circ$ lik açı ile yakın noktadaki $60^\\circ$ lik açı arasında oluşan üçgen ikizkenardır. Bu yüzden yakın noktadan kulenin tepesine olan uzaklık da $10$ metredir.",
        ]},
        {"baslik": "Eğik düzlem", "icerik": [
            "Rampalar, merdivenler ve eğik düzlemler günlük hayatta en sık karşılaşılan dik üçgenlerdir ve hepsi aynı yapıdadır: rampanın uzunluğu hipotenüs, ulaştığı yükseklik karşı dik kenar, yatay uzunluğu komşu dik kenardır.",
            ornek(
                "Uzunluğu $10$ metre olan bir rampa yerle $30^\\circ$ açı yapıyor.",
                "Rampanın ulaştığı yüksekliği ve yatay uzunluğunu bulalım.",
                "Yükseklik: $10 \\cdot \\sin 30^\\circ=5$ metre.",
                "Yatay uzunluk: $10 \\cdot \\cos 30^\\circ=5\\sqrt{3}$, yaklaşık $8.66$ metre."),
            hap("Bir rampanın eğimi, yerle yaptığı açının tanjantıdır: yükselme bölü yatay uzunluk.", "$50$ santimetre yükselip yatayda $6$ metre ilerleyen bir tekerlekli sandalye rampasının eğimi $\\dfrac{0.5}{6}$, yani yaklaşık $0.083$ olur.", gunluk=True),
        ]},
        {"baslik": "Merdivenin açısı", "icerik": [
            "Bazı problemlerde kenarlar verilir ve açı istenir. Bu durumda uygun oran hesaplanır ve değerin hangi açıya karşılık geldiğine bakılır.",
            ornek(
                "$6$ metrelik bir merdiven duvara dayandığında duvarda $3\\sqrt{3}$ metre yüksekliğe ulaşıyor.",
                "Merdivenin yerle yaptığı açıyı ve duvardan uzaklığını bulalım.",
                "$\\sin \\alpha=\\dfrac{3\\sqrt{3}}{6}=\\dfrac{\\sqrt{3}}{2}$; açı $60^\\circ$ dir.",
                "Uzaklık: $6 \\cdot \\cos 60^\\circ=3$ metre."),
        ]},
        {"baslik": "İkizkenar üçgende yükseklik", "icerik": [
            "Dik üçgen içermeyen üçgenlerde de trigonometrik oranlar kullanılır: uygun bir yükseklik çizilerek üçgen iki dik üçgene ayrılır ve her birinde oranlar ayrı ayrı uygulanır. İkizkenar üçgende tepeden inen yükseklik tabanı ikiye böler.",
            ornek(
                "Eşit kenarları $10$ ve tepe açısı $120^\\circ$ olan bir ikizkenar üçgen verilsin.",
                "Yüksekliği ve taban uzunluğunu bulalım.",
                "Taban açıları $30^\\circ$ dir; yükseklik $10 \\cdot \\sin 30^\\circ=5$.",
                "Tabanın yarısı $10 \\cdot \\cos 30^\\circ=5\\sqrt{3}$; taban $10\\sqrt{3}$ tür."),
        ]},
        {"baslik": "Tanjant ile sinüsün karşılaştırılması", "icerik": [
            "Dar bir açı için tanjant her zaman sinüsten büyüktür. Bunun nedeni, $\\tan \\alpha=\\dfrac{\\sin \\alpha}{\\cos \\alpha}$ olması ve dar açılarda kosinüsün $1$ den küçük olmasıdır: bir sayıyı $1$ den küçük pozitif bir sayıya bölmek onu büyütür.",
            ornek(
                "$30^\\circ$ açısı verilsin.",
                "Sinüs ve tanjantı karşılaştıralım.",
                "$\\sin 30^\\circ=\\dfrac{1}{2}=0.5$.",
                "$\\tan 30^\\circ=\\dfrac{\\sqrt{3}}{3}$, yaklaşık $0.577$; tanjant daha büyüktür."),
        ]},
        {"baslik": "Üçgenin alanı", "icerik": [
            "İki kenarı ve aralarındaki açı bilinen bir üçgenin alanı sinüsle bulunur. Kenarlardan biri taban kabul edilirse yükseklik, diğer kenarın açının sinüsüyle çarpımıdır:",
            "$$\\text{Alan}=\\dfrac{1}{2} a b \\sin C$$",
            ornek(
                "İki kenarı $6$ ve $8$ olan, bu kenarlar arasındaki açısı $30^\\circ$ olan bir üçgen verilsin.",
                "Alanını bulalım.",
                "$\\text{Alan}=\\dfrac{1}{2} \\cdot 6 \\cdot 8 \\cdot \\dfrac{1}{2}$.",
                "Alan $12$ birimkaredir."),
            "Açı $90^\\circ$ olduğunda $\\sin 90^\\circ=1$ olur ve formül bildik dik üçgen alanına döner. Bu, formülün tutarlılığı için iyi bir kontroldür. Açı $90^\\circ$ den uzaklaştıkça sinüs küçülür ve aynı iki kenarla kurulan üçgenin alanı da küçülür; en büyük alan kenarlar dik olduğunda elde edilir.",
        ]},
        {"baslik": "Sınavda trigonometrik oranlar", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) trigonometrik oranlar; bir orandan diğerlerini bulma, özel açılar, kenar ve hipotenüs hesabı, tümler açılar ve oranların karşılaştırılması biçiminde karşına çıkabilir.",
                "Geometri sorularında da dik üçgende kenar bulma, yükseklik ve alan hesabı için sık kullanılır."),
            "Oran sorularında bir dik üçgen çizmek neredeyse her zaman en kısa yoldur. Verilen oranı kenarlara yaz, üçüncü kenarı Pisagor ile bul ve istenen oranı üçgenden oku. Açının bölgesi sorulmuyorsa ve açı dar ise bütün oranlar pozitiftir. Açı geniş olduğunda ise oranların işaretleri birim çemberden belirlenir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Karşı ve komşu kenarı karıştırmak", "Kenarlar açıya göre belirlenir"],
                ["Sinüsü karşı bölü komşu almak", "Sinüs karşı bölü hipotenüs"],
                ["$\\sin 30^\\circ$ yi $\\dfrac{\\sqrt{3}}{2}$ almak", "$\\sin 30^\\circ=\\dfrac{1}{2}$"],
                ["Tanjantın $1$ den büyük olamayacağını sanmak", "Tanjant her pozitif değeri alabilir"],
                ["Kotanjantı sinüsün tersi sanmak", "Kotanjant tanjantın tersidir"],
                ["Alan formülünde açıyı kenarların arasından almamak", "Açı iki kenarın arasındaki açıdır"],
            ]),
            "Bu hataların çoğu, çizim yapmadan formül hatırlamaya çalışmaktan doğar. Üçgeni çizip açıyı işaretlemek ve kenarları açıya göre adlandırmak, bütün tanımları doğru uygulamanın en güvenli yoludur.",
        ]},
    ],
    "sss": [
        ("Sinüs nedir?",
         "Dik üçgende bir dar açının karşısındaki dik kenarın hipotenüse oranıdır. Dar açılar için 0 ile 1 arasındadır."),
        ("Kosinüs nedir?",
         "Dik üçgende bir dar açının komşu dik kenarının hipotenüse oranıdır."),
        ("Tanjant ile kotanjant arasındaki ilişki nedir?",
         "Tanjant karşı kenarın komşu kenara, kotanjant komşu kenarın karşı kenara oranıdır. Biri ötekinin tersidir ve çarpımları 1 dir."),
        ("Bir orandan diğerleri nasıl bulunur?",
         "Orana uyan bir dik üçgen çizilir, üçüncü kenar Pisagor bağıntısıyla bulunur ve diğer oranlar üçgenden okunur."),
        ("Tümler açılarda oranlar nasıl ilişkilidir?",
         "Toplamları 90 derece olan iki açıdan birinin sinüsü diğerinin kosinüsüne, birinin tanjantı diğerinin kotanjantına eşittir."),
        ("İki kenarı ve aradaki açısı bilinen üçgenin alanı nasıl bulunur?",
         "İki kenarın çarpımının yarısı, aradaki açının sinüsüyle çarpılır."),
        ("Sekant ve kosekant nedir?",
         "Sekant kosinüsün, kosekant sinüsün çarpmaya göre tersidir. Dik kenarları 5 ve 12 olan üçgende sekant 13 bölü 12 dir."),
        ("Tanjant 1 den büyük olabilir mi?",
         "Evet. Tanjant iki dik kenarın oranıdır ve açı 45 dereceden büyükse karşı kenar komşu kenardan uzun olduğu için 1 i aşar."),
    ],
    "kontrol": [
        "Dik üçgende hipotenüs, karşı ve komşu kenarları ayırt edebiliyorum.",
        "Sinüs, kosinüs, tanjant ve kotanjantı tanımlayabiliyorum.",
        "Sekant ve kosekantın ne olduğunu biliyorum.",
        "Oranların yalnızca açıya bağlı olduğunu açıklayabiliyorum.",
        "Tümler açılardaki ilişkileri kullanabiliyorum.",
        "Bir orandan diğerlerini dik üçgen çizerek bulabiliyorum.",
        "Özel açıların oranlarını ve nereden geldiklerini biliyorum.",
        "Bir açı ve bir kenardan diğer kenarları bulabiliyorum.",
        "Oranları açıya göre karşılaştırabiliyorum.",
        "Yükseklik, eğik düzlem ve alan problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["trigonometri-konu-anlatimi", "birim-cember", "trigonometrik-ozdeslikler-formuller"],
}
