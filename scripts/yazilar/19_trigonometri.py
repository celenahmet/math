# scripts/yazilar/19_trigonometri.py — Trigonometri Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

PI_ISARET = [(math.pi / 2, "π/2"), (math.pi, "π"), (3 * math.pi / 2, "3π/2"), (2 * math.pi, "2π")]

YAZI = {
    "slug": "trigonometri-konu-anlatimi",
    "baslik": "Trigonometri Konu Anlatımı",
    "aciklama": "Trigonometri nedir? Derece ve radyan, esas ölçü, dik üçgende oranlar, özel açılar, bölgelere göre işaretler, temel özdeşlik, periyot ve grafikler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "trigonometri-konu-anlatimi",
    "kapak_alt": "Trigonometri: dönen bir kolun dik üçgen izdüşümlerini ve oluşan dalga izini gösteren düzenek üzerinde çalışan iki öğrenci",
    "ozet": "Trigonometri, açılar ile uzunluklar arasındaki ilişkiyi inceleyen matematik dalıdır. Bir dik üçgenin kenar oranlarıyla başlar, birim çemberle bütün açılara genişler ve dönen bir hareketin ürettiği dalgaları tanımlar. Bu yazıda açı ölçü birimlerini, derece ve radyan dönüşümünü, esas ölçüyü, dik üçgende sinüs, kosinüs, tanjant ve kotanjantı, özel açıların değerlerini, bölgelere göre işaretleri, temel özdeşliği, tümler açıları, periyodu ve grafikleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Trigonometri nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dik üçgeni, Pisagor bağıntısını ve fonksiyon kavramını biliyor olman yeterli.",
                "Fonksiyonlar için <a href=\"/blog/fonksiyonlar-konu-anlatimi/\">Fonksiyonlar Konu Anlatımı</a> yazısına göz at."),
            "Trigonometri sözcüğü Yunanca üçgen ve ölçme anlamındaki iki kelimeden gelir. Başlangıçta bir üçgenin açılarından kenar uzunluklarını hesaplamak için geliştirilmiştir: bir ağacın boyunu gölgesinden ya da bir nehrin genişliğini karşı kıyıdaki bir noktaya bakış açısından bulmak gibi.",
            "Bugün trigonometri çok daha geniş bir alanı kapsar. Kapaktaki düzenek bunu özetliyor: çember üzerinde dönen bir kolun yatay ve dikey izdüşümleri, zaman içinde çizildiğinde bir dalga oluşturur. Ses, ışık ve alternatif akım gibi tekrar eden bütün olaylar bu dalgalarla anlatılır.",
            hap("Trigonometri, açılar ile uzunluklar arasındaki ilişkiyi inceler.",
                "Dik üçgenle başlar, birim çemberle bütün açılara genişler."),
        ]},
        {"baslik": "Açı ölçü birimleri", "icerik": [
            "Açılar iki birimle ölçülür. <strong>Derece</strong>, tam dönüşün $360$ eşit parçasından biridir. <strong>Radyan</strong> ise çemberde yarıçap uzunluğundaki bir yayı gören merkez açıdır. Tam dönüş $360^\\circ$ ya da $2\\pi$ radyandır; bu yüzden $180^\\circ=\\pi$ radyandır.",
            tablo(["Derece", "$30^\\circ$", "$45^\\circ$", "$60^\\circ$", "$90^\\circ$", "$180^\\circ$", "$360^\\circ$"], [
                ["Radyan", "$\\dfrac{\\pi}{6}$", "$\\dfrac{\\pi}{4}$", "$\\dfrac{\\pi}{3}$", "$\\dfrac{\\pi}{2}$", "$\\pi$", "$2\\pi$"],
            ]),
            "Radyan, matematikte doğal olan birimdir: yay uzunluğu yarıçap ile radyan cinsinden açının çarpımıdır. Bu yüzden ileri konularda, özellikle türev ve integralde, açılar hep radyanla ölçülür.",
        ]},
        {"baslik": "Derece ve radyan dönüşümü", "icerik": [
            "Derece ile radyan arasındaki dönüşüm, $180^\\circ=\\pi$ eşitliğinden gelen bir orantıyla yapılır. Derece cinsinden ölçü $D$, radyan cinsinden ölçü $R$ ise:",
            "$$\\dfrac{D}{180}=\\dfrac{R}{\\pi}$$",
            ornek(
                "$150^\\circ$ ve $\\dfrac{2\\pi}{3}$ radyan verilsin.",
                "Birincisini radyana, ikincisini dereceye çevirelim.",
                "$R=\\dfrac{150}{180}\\pi=\\dfrac{5\\pi}{6}$.",
                "$D=\\dfrac{2}{3} \\cdot 180=120^\\circ$."),
            dikkat(
                "Radyanı derece gibi yazmak.",
                "$\\dfrac{\\pi}{6}$ bir radyan ölçüsüdür ve $30^\\circ$ ye eşittir. $\\pi$ nin sayısal değeri yaklaşık $3.14$ tür; bu yüzden $\\pi$ radyan yaklaşık $3.14$ radyan, yani $180^\\circ$ dir. Radyanı dereceyle karıştırmamak için birim her zaman açıkça düşünülmelidir."),
        ]},
        {"baslik": "Yay uzunluğu ve radyan", "icerik": [
            "Radyanın asıl kullanışlılığı yay uzunluğu hesabında görülür. Yarıçapı $r$ olan bir çemberde radyan cinsinden $\\theta$ açısının gördüğü yayın uzunluğu $l=r \\cdot \\theta$ dır. Derece kullanılsaydı formüle $\\dfrac{\\pi}{180}$ çarpanı eklenmesi gerekirdi.",
            ornek(
                "Yarıçapı $6$ santimetre olan bir çemberde $\\dfrac{\\pi}{3}$ radyanlık merkez açı verilsin.",
                "Açının gördüğü yayın uzunluğunu bulalım.",
                "$l=6 \\cdot \\dfrac{\\pi}{3}=2\\pi$ santimetre.",
                "Bu uzunluk çevrenin, yani $12\\pi$ nin altıda biridir; açı da tam dönüşün altıda biridir."),
        ]},
        {"baslik": "Yönlü açı ve esas ölçü", "icerik": [
            "Trigonometride açılar yönlüdür: saat yönünün tersine dönüş pozitif, saat yönünde dönüş negatif kabul edilir. Tam dönüş eklenip çıkarıldığında kol aynı yere geldiği için bir açının $0^\\circ$ ile $360^\\circ$ arasındaki eş değerine <strong>esas ölçü</strong> denir.",
            ornek(
                "$750^\\circ$ ve $-60^\\circ$ açıları verilsin.",
                "Esas ölçülerini bulalım.",
                "$750^\\circ-2 \\cdot 360^\\circ=30^\\circ$.",
                "$-60^\\circ+360^\\circ=300^\\circ$."),
            "Esas ölçüsü aynı olan açıların bütün trigonometrik değerleri de aynıdır, çünkü kolları aynı yerdedir. Bu yüzden büyük açıların değerleri hesaplanırken önce esas ölçü bulunur. Radyan cinsinden verilen açılarda da aynı yol izlenir; bu kez eklenip çıkarılan tam dönüş $2\\pi$ dir.",
        ]},
        {"baslik": "Dik üçgende trigonometrik oranlar", "icerik": [
            "Bir dik üçgende dar açılardan biri $\\alpha$ olsun. Bu açının karşısındaki kenara karşı dik kenar, yanındaki dik kenara komşu dik kenar, dik açının karşısındaki en uzun kenara hipotenüs denir. Dört temel oran şöyle tanımlanır:",
            tablo(["Oran", "Tanım"], [
                ["$\\sin \\alpha$", "Karşı dik kenar / hipotenüs"],
                ["$\\cos \\alpha$", "Komşu dik kenar / hipotenüs"],
                ["$\\tan \\alpha$", "Karşı dik kenar / komşu dik kenar"],
                ["$\\cot \\alpha$", "Komşu dik kenar / karşı dik kenar"],
            ]),
            ornek(
                "Dik kenarları $3$ ve $4$ olan bir dik üçgende $3$ birimlik kenarın karşısındaki açı $\\alpha$ olsun.",
                "Dört oranı bulalım.",
                "Hipotenüs: $\\sqrt{9+16}=5$.",
                "$\\sin \\alpha=\\dfrac{3}{5}$, $\\cos \\alpha=\\dfrac{4}{5}$, $\\tan \\alpha=\\dfrac{3}{4}$, $\\cot \\alpha=\\dfrac{4}{3}$."),
            "Oranların ayrıntısı <a href=\"/blog/trigonometrik-oranlar/\">Trigonometrik Oranlar: Sinüs, Kosinüs, Tanjant ve Kotanjant</a> yazısında.",
        ]},
        {"baslik": "Özel açıların değerleri", "icerik": [
            "$30^\\circ$, $45^\\circ$ ve $60^\\circ$ açılarının trigonometrik değerleri çok sık kullanılır ve ezberlenir. Bu değerler iki özel üçgenden elde edilir.",
            tablo(["Açı", "$\\sin$", "$\\cos$", "$\\tan$"], [
                ["$30^\\circ$", "$\\dfrac{1}{2}$", "$\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{\\sqrt{3}}{3}$"],
                ["$45^\\circ$", "$\\dfrac{\\sqrt{2}}{2}$", "$\\dfrac{\\sqrt{2}}{2}$", "$1$"],
                ["$60^\\circ$", "$\\dfrac{\\sqrt{3}}{2}$", "$\\dfrac{1}{2}$", "$\\sqrt{3}$"],
            ]),
            "Kenarı $2$ olan bir eşkenar üçgen ortadan ikiye bölünürse açıları $30^\\circ$, $60^\\circ$ ve $90^\\circ$ olan, kenarları $1$, $\\sqrt{3}$ ve $2$ olan bir dik üçgen elde edilir. Dik kenarları $1$ olan ikizkenar dik üçgenin hipotenüsü ise $\\sqrt{2}$ dir ve açıları $45^\\circ$ dir. Tablodaki bütün değerler bu iki üçgenden okunur. Tabloyu ezberlemek yerine bu iki üçgeni zihinde çizmek, unutulan bir değeri birkaç saniyede yeniden bulmayı sağlar.",
        ]},
        {"baslik": "0 ve 90 derecede değerler", "icerik": [
            "Özel açılar tablosu $0^\\circ$ ve $90^\\circ$ değerleriyle tamamlanır. Birim çemberde $0^\\circ$ noktası $(1, 0)$, $90^\\circ$ noktası $(0, 1)$ dir; kosinüs yatay, sinüs dikey koordinat olduğu için değerler doğrudan okunur.",
            tablo(["Açı", "$\\sin$", "$\\cos$", "$\\tan$"], [
                ["$0^\\circ$", "$0$", "$1$", "$0$"],
                ["$90^\\circ$", "$1$", "$0$", "Tanımsız"],
            ]),
            "$\\tan 90^\\circ$ tanımsızdır, çünkü tanjant sinüsün kosinüse bölümüdür ve $\\cos 90^\\circ=0$ dır. Grafikte bu durum, tanjant eğrisinin $90^\\circ$ yaklaştıkça sınırsız büyümesi olarak görülür.",
        ]},
        {"baslik": "Birim çembere geçiş", "icerik": [
            "Dik üçgen tanımı yalnızca $0^\\circ$ ile $90^\\circ$ arasındaki açılar için geçerlidir. Bütün açılar için merkezi başlangıç noktası, yarıçapı $1$ olan <strong>birim çember</strong> kullanılır. Pozitif $x$ ekseninden başlayarak $\\theta$ kadar dönen yarıçapın ucundaki noktanın koordinatları $(\\cos \\theta, \\sin \\theta)$ dir.",
            "Bu tanım dar açılar için dik üçgen tanımıyla aynı sonucu verir, çünkü hipotenüs $1$ olunca sinüs karşı kenarın, kosinüs komşu kenarın uzunluğuna eşit olur. Ayrıntısı <a href=\"/blog/birim-cember/\">Birim Çember Konu Anlatımı</a> yazısında.",
        ]},
        {"baslik": "Bölgelere göre işaretler", "icerik": [
            "Birim çemberdeki noktanın koordinatları bölgeye göre işaret değiştirdiği için trigonometrik değerlerin işaretleri de bölgeye bağlıdır. Sinüs noktanın yüksekliği, kosinüs yatay konumu olduğu için işaretler doğrudan koordinatlardan okunur.",
            tablo(["Bölge", "Açı aralığı", "Pozitif olanlar"], [
                ["I", "$0^\\circ$ ile $90^\\circ$", "Hepsi"],
                ["II", "$90^\\circ$ ile $180^\\circ$", "$\\sin$"],
                ["III", "$180^\\circ$ ile $270^\\circ$", "$\\tan$ ve $\\cot$"],
                ["IV", "$270^\\circ$ ile $360^\\circ$", "$\\cos$"],
            ]),
            ornek(
                "$\\sin 150^\\circ$ ve $\\cos 150^\\circ$ değerleri istensin.",
                "İşaretlerini ve değerlerini bulalım.",
                "$150^\\circ$ ikinci bölgededir; sinüs pozitif, kosinüs negatiftir.",
                "$150^\\circ$ nin $180^\\circ$ ye uzaklığı $30^\\circ$ dir: $\\sin 150^\\circ=\\dfrac{1}{2}$ ve $\\cos 150^\\circ=-\\dfrac{\\sqrt{3}}{2}$."),
        ]},
        {"baslik": "Değerlerin sınırları", "icerik": [
            "Birim çemberdeki noktanın koordinatları $-1$ ile $1$ arasında olduğu için sinüs ve kosinüs hiçbir zaman bu aralığın dışına çıkmaz. Bu sınır, bazı denklemlerin çözümsüz olduğunu hemen gösterir ve trigonometrik ifadelerin alabileceği değerleri belirler.",
            ornek(
                "$\\sin x=2$ denklemi ve $3\\sin x+1$ ifadesi verilsin.",
                "Denklemin çözümü olup olmadığını ve ifadenin alabileceği değerleri bulalım.",
                "Sinüs en fazla $1$ olabileceği için $\\sin x=2$ denkleminin çözümü yoktur.",
                "$-1 \\leq \\sin x \\leq 1$ ise $-2 \\leq 3\\sin x+1 \\leq 4$ tür; ifade $-2$ ile $4$ arasındaki değerleri alır."),
        ]},
        {"baslik": "İkinci bölgede bir orandan diğerlerine", "icerik": [
            "Temel özdeşlik bir oranın karesini verir; kökün işareti ise açının bölgesinden belirlenir. Bölge bilgisi olmadan sonuç iki olasılıklı kalır, bu yüzden sorular bölgeyi mutlaka belirtir.",
            ornek(
                "$\\cos \\theta=-\\dfrac{5}{13}$ ve $\\theta$ ikinci bölgede olsun.",
                "$\\sin \\theta$ ve $\\tan \\theta$ değerlerini bulalım.",
                "$\\sin^2 \\theta=1-\\dfrac{25}{169}=\\dfrac{144}{169}$; ikinci bölgede sinüs pozitif: $\\sin \\theta=\\dfrac{12}{13}$.",
                "$\\tan \\theta=\\dfrac{12}{13}:(-\\dfrac{5}{13})=-\\dfrac{12}{5}$."),
        ]},
        {"baslik": "Temel özdeşlik", "icerik": [
            "Birim çemberdeki nokta $x^2+y^2=1$ denklemini sağladığı için her açı için şu eşitlik doğrudur. Bu, trigonometrinin en temel özdeşliğidir ve Pisagor bağıntısının trigonometrik biçimidir:",
            "$$\\sin^2 \\theta+\\cos^2 \\theta=1$$",
            ornek(
                "$\\sin \\theta=\\dfrac{3}{5}$ ve $\\theta$ birinci bölgede olsun.",
                "Diğer oranları bulalım.",
                "$\\cos^2 \\theta=1-\\dfrac{9}{25}=\\dfrac{16}{25}$; birinci bölgede kosinüs pozitif olduğu için $\\cos \\theta=\\dfrac{4}{5}$.",
                "$\\tan \\theta=\\dfrac{3}{4}$ ve $\\cot \\theta=\\dfrac{4}{3}$."),
            "Tanjant ve kotanjant da sinüs ve kosinüs cinsinden yazılır: $\\tan \\theta=\\dfrac{\\sin \\theta}{\\cos \\theta}$ ve $\\cot \\theta=\\dfrac{\\cos \\theta}{\\sin \\theta}$. Bu yüzden $\\tan \\theta \\cdot \\cot \\theta=1$ dir. Özdeşliklerin ayrıntısı <a href=\"/blog/trigonometrik-ozdeslikler-formuller/\">Trigonometrik Özdeşlikler ve Formüller</a> yazısında.",
        ]},
        {"baslik": "Tümler açılar", "icerik": [
            "Toplamları $90^\\circ$ olan açılara tümler açılar denir. Bir dik üçgende iki dar açı tümlerdir ve birinin karşı kenarı ötekinin komşu kenarıdır. Bu yüzden bir açının sinüsü, tümlerinin kosinüsüne eşittir:",
            "$$\\sin(90^\\circ-x)=\\cos x$$",
            ornek(
                "$\\sin 20^\\circ$ ile $\\cos 70^\\circ$ karşılaştırılsın.",
                "İki değerin ilişkisini bulalım.",
                "$20^\\circ+70^\\circ=90^\\circ$; açılar tümlerdir.",
                "$\\sin 20^\\circ=\\cos 70^\\circ$ tir."),
            "Kosinüs adındaki \"ko\" öneki de buradan gelir: kosinüs, tümler açının sinüsüdür. Kotanjant da aynı biçimde tümler açının tanjantıdır. Örneğin $\\cot 30^\\circ=\\tan 60^\\circ=\\sqrt{3}$ tür.",
        ]},
        {"baslik": "Negatif açılar ve bütünler açılar", "icerik": [
            "Negatif bir açı, pozitif açının $x$ eksenine göre yansımasıdır: nokta aynı yatay konumda kalır, yüksekliği işaret değiştirir. Bu yüzden $\\cos(-x)=\\cos x$ ve $\\sin(-x)=-\\sin x$ tir. Toplamları $180^\\circ$ olan bütünler açılarda ise nokta $y$ eksenine göre yansır: $\\sin(180^\\circ-x)=\\sin x$ ve $\\cos(180^\\circ-x)=-\\cos x$ tir.",
            ornek(
                "$\\sin(-30^\\circ)$, $\\cos(-60^\\circ)$ ve $\\sin 120^\\circ$ değerleri istensin.",
                "Değerleri bulalım.",
                "$\\sin(-30^\\circ)=-\\sin 30^\\circ=-\\dfrac{1}{2}$ ve $\\cos(-60^\\circ)=\\cos 60^\\circ=\\dfrac{1}{2}$.",
                "$\\sin 120^\\circ=\\sin 60^\\circ=\\dfrac{\\sqrt{3}}{2}$."),
        ]},
        {"baslik": "Periyot", "icerik": [
            "Birim çemberde bir tam dönüş sonra nokta aynı yere geldiği için sinüs ve kosinüsün değerleri her $360^\\circ$ de bir tekrar eder. Tanjant ve kotanjant ise her $180^\\circ$ de bir tekrar eder, çünkü yarım dönüşte noktanın iki koordinatı birlikte işaret değiştirir ve oranları aynı kalır.",
            tablo(["Fonksiyon", "Periyot"], [
                ["$\\sin$ ve $\\cos$", "$360^\\circ$ ya da $2\\pi$"],
                ["$\\tan$ ve $\\cot$", "$180^\\circ$ ya da $\\pi$"],
            ]),
            ornek(
                "$\\sin 390^\\circ$ ve $\\tan 225^\\circ$ değerleri istensin.",
                "Değerleri bulalım.",
                "$\\sin 390^\\circ=\\sin 30^\\circ=\\dfrac{1}{2}$.",
                "$\\tan 225^\\circ=\\tan 45^\\circ=1$."),
        ]},
        {"baslik": "Grafikler", "icerik": [
            "Sinüs ve kosinüs fonksiyonlarının grafikleri, $-1$ ile $1$ arasında salınan dalgalardır. Sinüs grafiği başlangıç noktasından başlar; kosinüs grafiği ise aynı dalganın $\\dfrac{\\pi}{2}$ kadar sola kaydırılmış hâlidir.",
            koordinat_grafik("y = sin x ve y = cos x grafikleri", [("y = sin x", math.sin), ("y = cos x", math.cos)], (-0.5, 7), (-1.5, 2), adim=0.5, x_isaretler=PI_ISARET,
                             noktalar=[(math.pi / 2, 1, "", True), (0, 1, "", True), (math.pi, 0, "", True)]),
            "Grafikler, kapaktaki düzeneğin çizdiği dalganın matematiksel karşılığıdır: dönen kolun yüksekliği sinüsü, yatay konumu kosinüsü verir. Ayrıntısı <a href=\"/blog/trigonometrik-fonksiyon-grafikleri/\">Trigonometrik Fonksiyonların Grafikleri</a> yazısında.",
        ]},
        {"baslik": "Basit bir trigonometrik denklem", "icerik": [
            "Trigonometrik denklemlerde bilinmeyen bir açıdır ve çözüm, verilen değeri üreten açıları aramaktır. Periyodiklik yüzünden bu denklemlerin genellikle sonsuz çözümü vardır; bu yüzden çözümler çoğu zaman belirli bir aralıkta istenir.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin x=\\dfrac{1}{2}$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "Sinüsü $\\dfrac{1}{2}$ olan açılardan biri $\\dfrac{\\pi}{6}$ dir.",
                "Sinüs ikinci bölgede de pozitiftir: $\\pi-\\dfrac{\\pi}{6}=\\dfrac{5\\pi}{6}$. Çözümler $\\dfrac{\\pi}{6}$ ve $\\dfrac{5\\pi}{6}$ dir."),
        ]},
        {"baslik": "Dik üçgen uygulaması", "icerik": [
            "Trigonometrinin en eski kullanımı, doğrudan ölçülemeyen uzunlukları bir açı ve bir uzunluk yardımıyla hesaplamaktır. Hangi oranın kullanılacağı, bilinen ve istenen kenarların açıya göre konumuna bağlıdır.",
            ornek(
                "$10$ metrelik bir merdiven duvara, yerle $60^\\circ$ açı yapacak biçimde dayanmış.",
                "Merdivenin duvarda ulaştığı yüksekliği ve duvardan uzaklığını bulalım.",
                "Yükseklik karşı dik kenardır: $10 \\cdot \\sin 60^\\circ=5\\sqrt{3}$, yaklaşık $8.66$ metre.",
                "Uzaklık komşu dik kenardır: $10 \\cdot \\cos 60^\\circ=5$ metre."),
        ]},
        {"baslik": "Gölgeden yükseklik", "icerik": [
            "Trigonometrinin klasik kullanımlarından biri, bir cismin yüksekliğini gölgesinden bulmaktır. Güneş ışınlarının yerle yaptığı açı ve gölgenin uzunluğu biliniyorsa yükseklik tanjantla hesaplanır, çünkü yükseklik karşı dik kenar, gölge komşu dik kenardır.",
            ornek(
                "Bir ağacın gölgesi $10$ metre ve güneş ışınları yerle $30^\\circ$ açı yapıyor.",
                "Ağacın boyunu bulalım.",
                "$\\tan 30^\\circ=\\dfrac{h}{10}$.",
                "$h=10 \\cdot \\dfrac{\\sqrt{3}}{3}=\\dfrac{10\\sqrt{3}}{3}$, yaklaşık $5.77$ metre."),
        ]},
        {"baslik": "Sadeleştirmede temel özdeşlik", "icerik": [
            "Temel özdeşlik yalnızca değer bulmak için değil, ifadeleri sadeleştirmek için de kullanılır. $1-\\cos^2 x$ ifadesi $\\sin^2 x$ olarak, $1-\\sin^2 x$ ifadesi de $\\cos^2 x$ olarak yazılabilir.",
            ornek(
                "$\\dfrac{1-\\cos^2 x}{\\sin x}$ ifadesi verilsin, $\\sin x \\neq 0$.",
                "İfadeyi sadeleştirelim.",
                "Pay $\\sin^2 x$ olarak yazılır.",
                "$\\dfrac{\\sin^2 x}{\\sin x}=\\sin x$."),
        ]},
        {"baslik": "Eğim ve tanjant", "icerik": [
            "Bir doğrunun eğimi, $x$ ekseniyle yaptığı açının tanjantına eşittir. Eğim, yatayda bir birim ilerlerken dikeyde ne kadar yükselindiğini gösterir; bu da karşı kenarın komşu kenara oranıdır.",
            ornek(
                "$y=x$ ve $y=\\sqrt{3}x$ doğruları verilsin.",
                "$x$ ekseniyle yaptıkları açıları bulalım.",
                "$y=x$ doğrusunun eğimi $1$ dir ve $\\tan 45^\\circ=1$ olduğu için açı $45^\\circ$ dir.",
                "$y=\\sqrt{3}x$ doğrusunun eğimi $\\sqrt{3}$ tür ve açı $60^\\circ$ dir."),
        ]},
        {"baslik": "Sınavda trigonometri", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) trigonometri; derece ve radyan dönüşümü, esas ölçü, özel açıların değerleri, bölgelere göre işaretler, özdeşlikler, denklemler ve grafikler biçiminde karşına çıkabilir.",
                "Dik üçgende oranlar ve özel açılar, geometri sorularının içinde de sık kullanılır."),
            "Trigonometri sorularında ilk adım açıyı esas ölçüye indirmek ve hangi bölgede olduğunu belirlemektir. Bölge işareti, özel açı değeri ise sayısal büyüklüğü verir; ikisi birleştirildiğinde değer bulunur.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\pi$ yi $180$ sayısı sanmak", "$\\pi$ radyan $180^\\circ$ ye eşittir"],
                ["Sinüsü komşu kenarla kurmak", "Sinüs karşı kenar bölü hipotenüs"],
                ["İkinci bölgede kosinüsü pozitif almak", "İkinci bölgede yalnız sinüs pozitif"],
                ["$\\sin^2 \\theta$ yı $\\sin(\\theta^2)$ sanmak", "$(\\sin \\theta)^2$ demektir"],
                ["Tanjantın periyodunu $360^\\circ$ almak", "Tanjantın periyodu $180^\\circ$"],
                ["Denklemde yalnız bir çözüm yazmak", "Aralıktaki bütün çözümler yazılır"],
            ]),
            "Bu hataların çoğu, birim çember düşünülmeden ezbere çalışılmasından doğar. Her değerin birim çemberdeki bir noktanın koordinatı olduğu akılda tutulursa işaretler ve periyotlar kendiliğinden anlaşılır.",
        ]},
    ],
    "sss": [
        ("Trigonometri nedir?",
         "Açılar ile uzunluklar arasındaki ilişkiyi inceleyen matematik dalıdır. Dik üçgenin kenar oranlarıyla başlar ve birim çemberle bütün açılara genişler."),
        ("Radyan nedir?",
         "Yarıçap uzunluğundaki bir yayı gören merkez açıdır. 180 derece pi radyana eşittir."),
        ("Sinüs ve kosinüs nasıl tanımlanır?",
         "Dik üçgende sinüs karşı dik kenarın hipotenüse, kosinüs komşu dik kenarın hipotenüse oranıdır. Birim çemberde ise noktanın dikey ve yatay koordinatlarıdır."),
        ("Esas ölçü nedir?",
         "Bir açının 0 ile 360 derece arasındaki eş değeridir. Tam dönüşler eklenip çıkarılarak bulunur."),
        ("Sinüs kare artı kosinüs kare neden 1 dir?",
         "Birim çemberdeki nokta x kare artı y kare eşittir 1 denklemini sağlar ve bu noktanın koordinatları kosinüs ve sinüstür."),
        ("Tanjantın periyodu neden 180 derecedir?",
         "Yarım dönüşte noktanın iki koordinatı birlikte işaret değiştirir ve oranları aynı kalır. Bu yüzden tanjant her 180 derecede bir tekrar eder."),
        ("Sinüs ve kosinüs hangi değerleri alabilir?",
         "Birim çemberdeki noktanın koordinatları olduğu için her zaman eksi 1 ile 1 arasındadır. Bu yüzden sinüs x eşittir 2 gibi denklemlerin çözümü yoktur."),
    ],
    "kontrol": [
        "Derece ve radyan arasında dönüşüm yapabiliyorum.",
        "Bir açının esas ölçüsünü bulabiliyorum.",
        "Dik üçgende dört trigonometrik oranı yazabiliyorum.",
        "Özel açıların değerlerini ve nereden geldiklerini biliyorum.",
        "Birim çemberde noktanın koordinatlarını açıyla ilişkilendirebiliyorum.",
        "Bölgelere göre işaretleri belirleyebiliyorum.",
        "Temel özdeşliği kullanarak bir orandan diğerlerini bulabiliyorum.",
        "Tümler açıların ilişkisini kullanabiliyorum.",
        "Periyotları kullanarak büyük açıların değerlerini bulabiliyorum.",
        "Basit trigonometrik denklemleri ve dik üçgen problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birim-cember", "trigonometrik-oranlar", "trigonometrik-ozdeslikler-formuller"],
}
