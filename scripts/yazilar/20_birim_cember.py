# scripts/yazilar/20_birim_cember.py — Birim Cember (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

_UST = lambda x: math.sqrt(1 - x * x) if abs(x) <= 1 else None
_ALT = lambda x: -math.sqrt(1 - x * x) if abs(x) <= 1 else None
_C30 = math.sqrt(3) / 2

YAZI = {
    "slug": "birim-cember",
    "baslik": "Birim Çember Konu Anlatımı",
    "aciklama": "Birim çember nedir? Noktanın koordinatları, bölgeler ve işaretler, özel açılar, referans açı, tanjant ekseni, simetriler ve aynı değeri veren açılar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "birim-cember",
    "kapak_alt": "Birim çember: dört renkli bölgeye ayrılmış bir çemberde dönen yarıçapı ve izdüşüm çubuklarını gösteren iki öğrenci",
    "ozet": "Birim çember, trigonometriyi dik üçgenin sınırlarından kurtarıp bütün açılara genişleten araçtır. Merkezi başlangıç noktası, yarıçapı bir olan bu çemberde her açıya bir nokta karşılık gelir ve noktanın koordinatları o açının kosinüsü ve sinüsüdür. Bu yazıda birim çemberin tanımını, eksen noktalarını, dört bölgeyi ve işaretleri, özel açıların noktalarını, referans açıyla diğer bölgelere geçişi, tanjant eksenini, simetrileri, aynı sinüs ya da kosinüsü veren açıları ve noktadan oran bulmayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Birim çember nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dik üçgende trigonometrik oranları ve koordinat düzlemini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/trigonometri-konu-anlatimi/\">Trigonometri Konu Anlatımı</a> yazısına göz at."),
            "Merkezi başlangıç noktası, yarıçapı $1$ birim olan çembere <strong>birim çember</strong> denir. Çember üzerindeki her nokta başlangıç noktasına $1$ birim uzaklıkta olduğu için Pisagor bağıntısından birim çemberin denklemi elde edilir:",
            "$$x^2+y^2=1$$",
            "Kapaktaki öğrencilerin kullandığı çember dört renkli bölgeye ayrılmış; merkezden çıkan döner bir yarıçap ve bu yarıçapın ucundan eksenlere inen iki çubuk var. Bu çubuklar, trigonometrinin iki temel değerini, yani kosinüs ve sinüsü, uzunluk olarak gösterir.",
            hap("Birim çember: merkez $(0, 0)$, yarıçap $1$, denklem $x^2+y^2=1$.",
                "Çember üzerindeki her nokta $(\\cos \\theta, \\sin \\theta)$ biçimindedir."),
        ]},
        {"baslik": "Çember üzerindeki nokta", "icerik": [
            "Pozitif $x$ ekseninden başlayıp saat yönünün tersine $\\theta$ kadar dönen yarıçapın ucundaki noktaya $P$ denirse, $P$ nin yatay koordinatı $\\cos \\theta$, dikey koordinatı $\\sin \\theta$ dır. Bu, bütün açılar için sinüs ve kosinüsün genel tanımıdır.",
            koordinat_grafik("Birim çemberde 30 derecelik açıya karşılık gelen nokta", [("x² + y² = 1", _UST), ("", _ALT), ("yarıçap", lambda x: math.tan(math.pi / 6) * x if 0 <= x <= _C30 else None)],
                             (-1.5, 1.5), (-1.5, 1.5), adim=0.5, dikeyler=[_C30], yataylar=[0.5],
                             noktalar=[(_C30, 0.5, "P(√3/2, 1/2)", True), (_C30, 0, "", True), (0, 0.5, "", True)]),
            "Dar açılarda bu tanım dik üçgen tanımıyla aynı sonucu verir. $P$ den $x$ eksenine inen dikme bir dik üçgen oluşturur; hipotenüs yarıçaptır ve uzunluğu $1$ dir. Hipotenüs $1$ olunca karşı kenar sinüse, komşu kenar kosinüse eşit olur.",
        ]},
        {"baslik": "Neden yarıçap 1?", "icerik": [
            "Yarıçapın $1$ seçilmesi hesabı büyük ölçüde sadeleştirir. Dik üçgende sinüs karşı kenarın hipotenüse bölümüdür; hipotenüs $1$ olunca bölme işlemi ortadan kalkar ve sinüs doğrudan bir uzunluk olur. Başka bir yarıçapla çalışılsaydı her değer yarıçapa bölünmek zorunda kalırdı.",
            "Bu seçim, trigonometrik değerlerin neden $-1$ ile $1$ arasında kaldığını da açıklar: çember üzerindeki bir noktanın koordinatları yarıçaptan büyük olamaz. Sinüs ve kosinüs için $-1 \\leq \\sin \\theta \\leq 1$ ve $-1 \\leq \\cos \\theta \\leq 1$ sınırları buradan gelir.",
        ]},
        {"baslik": "Eksenlerle kesişim noktaları", "icerik": [
            "Birim çember eksenleri dört noktada keser. Bu noktalar $0^\\circ$, $90^\\circ$, $180^\\circ$ ve $270^\\circ$ açılarına karşılık gelir ve değerleri doğrudan okunur.",
            tablo(["Açı", "Nokta", "$\\cos$", "$\\sin$"], [
                ["$0^\\circ$", "$(1, 0)$", "$1$", "$0$"],
                ["$90^\\circ$", "$(0, 1)$", "$0$", "$1$"],
                ["$180^\\circ$", "$(-1, 0)$", "$-1$", "$0$"],
                ["$270^\\circ$", "$(0, -1)$", "$0$", "$-1$"],
            ]),
            "Bu dört değer, sinüs ve kosinüsün en büyük ve en küçük değerlerini de gösterir: sinüs en büyük değeri $1$ i $90^\\circ$ de, en küçük değeri $-1$ i $270^\\circ$ de alır.",
        ]},
        {"baslik": "Dört bölge ve işaretler", "icerik": [
            "Eksenler çemberi dört bölgeye ayırır ve her bölgede noktanın koordinatlarının işaretleri bellidir. Kapaktaki dört renk bu bölgeleri gösterir. Tanjant, sinüsün kosinüse bölümü olduğu için iki koordinat aynı işaretliyse pozitif, farklıysa negatiftir.",
            tablo(["Bölge", "$\\cos$", "$\\sin$", "$\\tan$"], [
                ["I", "$+$", "$+$", "$+$"],
                ["II", "$-$", "$+$", "$-$"],
                ["III", "$-$", "$-$", "$+$"],
                ["IV", "$+$", "$-$", "$-$"],
            ]),
            dikkat(
                "İşaretleri ezberlemeye çalışıp karıştırmak.",
                "İşaret tablosunu ezberlemek gerekmez: kosinüs sağda pozitif, solda negatif; sinüs yukarıda pozitif, aşağıda negatiftir. Noktanın bulunduğu bölgeye bakmak her işareti doğrudan verir."),
            "Kotanjant da tanjantla aynı işarete sahiptir, çünkü biri ötekinin çarpmaya göre tersidir. Bu yüzden tablo tanjant için doğruysa kotanjant için de doğrudur.",
        ]},
        {"baslik": "İşaretlerden bölgeyi bulmak", "icerik": [
            "İşaret tablosu tersinden de okunur: iki değerin işareti biliniyorsa açının bölgesi tek olarak belirlenir. Sorularda açının bölgesi çoğu zaman doğrudan verilmez, bu yolla bulunur.",
            ornek(
                "$\\sin \\theta>0$ ve $\\cos \\theta<0$ ile $\\tan \\theta>0$ ve $\\sin \\theta<0$ durumları verilsin.",
                "Her durumda açının bölgesini bulalım.",
                "Sinüs pozitif ve kosinüs negatifse nokta yukarıda ve soldadır: ikinci bölge.",
                "Tanjant pozitif ve sinüs negatifse kosinüs de negatiftir; nokta aşağıda ve soldadır: üçüncü bölge."),
        ]},
        {"baslik": "Büyük ve negatif açılar", "icerik": [
            "$360^\\circ$ den büyük açılarda önce tam dönüşler çıkarılır ve esas ölçü bulunur; negatif açılarda ise tam dönüş eklenir. Esas ölçü bulunduktan sonra nokta her zamanki gibi okunur.",
            ornek(
                "$1110^\\circ$ ve $-\\dfrac{\\pi}{3}$ açıları verilsin.",
                "Birim çemberdeki noktalarını bulalım.",
                "$1110^\\circ-3 \\cdot 360^\\circ=30^\\circ$; nokta $(\\dfrac{\\sqrt{3}}{2}, \\dfrac{1}{2})$ dir.",
                "$-\\dfrac{\\pi}{3}$ saat yönünde $60^\\circ$ dönüştür ve dördüncü bölgededir; nokta $(\\dfrac{1}{2}, -\\dfrac{\\sqrt{3}}{2})$ olur."),
        ]},
        {"baslik": "Birinci bölgedeki özel noktalar", "icerik": [
            "$30^\\circ$, $45^\\circ$ ve $60^\\circ$ açılarına karşılık gelen noktalar, özel açıların değerlerinden okunur. Bu noktalar birinci bölgededir ve bütün diğer bölgelerdeki özel noktalar bunların yansımasıdır.",
            tablo(["Açı", "Nokta"], [
                ["$30^\\circ$", "$(\\dfrac{\\sqrt{3}}{2}, \\dfrac{1}{2})$"],
                ["$45^\\circ$", "$(\\dfrac{\\sqrt{2}}{2}, \\dfrac{\\sqrt{2}}{2})$"],
                ["$60^\\circ$", "$(\\dfrac{1}{2}, \\dfrac{\\sqrt{3}}{2})$"],
            ]),
            "Her noktanın gerçekten çember üzerinde olduğu denklemle kontrol edilebilir: $(\\dfrac{\\sqrt{3}}{2})^2+(\\dfrac{1}{2})^2=\\dfrac{3}{4}+\\dfrac{1}{4}=1$.",
        ]},
        {"baslik": "Referans açı", "icerik": [
            "Bir açının kolunun $x$ ekseniyle yaptığı dar açıya o açının <strong>referans açısı</strong> denir. Bir açının trigonometrik değerlerinin mutlak değeri, referans açısının değerlerine eşittir; işaret ise bölgeden gelir.",
            tablo(["Bölge", "Referans açı"], [
                ["II", "$180^\\circ-\\theta$"],
                ["III", "$\\theta-180^\\circ$"],
                ["IV", "$360^\\circ-\\theta$"],
            ]),
            ornek(
                "$225^\\circ$ açısı verilsin.",
                "Birim çemberdeki noktasını bulalım.",
                "Açı üçüncü bölgededir ve referans açısı $225^\\circ-180^\\circ=45^\\circ$ dir.",
                "Üçüncü bölgede iki koordinat da negatiftir: nokta $(-\\dfrac{\\sqrt{2}}{2}, -\\dfrac{\\sqrt{2}}{2})$ dir."),
        ]},
        {"baslik": "Diğer bölgelere yansıtma", "icerik": [
            "Referans açısı $30^\\circ$ olan dört açı, birim çemberde birbirinin yansıması olan dört nokta verir. Koordinatların mutlak değerleri aynıdır; yalnızca işaretler bölgeye göre değişir.",
            tablo(["Açı", "Bölge", "Nokta"], [
                ["$30^\\circ$", "I", "$(\\dfrac{\\sqrt{3}}{2}, \\dfrac{1}{2})$"],
                ["$150^\\circ$", "II", "$(-\\dfrac{\\sqrt{3}}{2}, \\dfrac{1}{2})$"],
                ["$210^\\circ$", "III", "$(-\\dfrac{\\sqrt{3}}{2}, -\\dfrac{1}{2})$"],
                ["$330^\\circ$", "IV", "$(\\dfrac{\\sqrt{3}}{2}, -\\dfrac{1}{2})$"],
            ]),
            "Aynı düzen $45^\\circ$ ve $60^\\circ$ için de geçerlidir. Böylece birim çemberdeki on altı özel nokta, birinci bölgedeki üç nokta ile eksenlerdeki dört noktadan türetilir. Bu yüzden birim çemberi öğrenmek, aslında üç noktayı ve yansıtma kuralını öğrenmektir.",
        ]},
        {"baslik": "Radyanla konumlar", "icerik": [
            "Birim çemberdeki noktalar radyanla da adlandırılır. $\\pi$ radyan yarım dönüş olduğu için radyan cinsinden açıların bölgesi $\\pi$ ye göre konumlarından anlaşılır: $\\dfrac{\\pi}{2}$ den küçükse birinci, $\\pi$ den küçükse ikinci bölgededir.",
            tablo(["Radyan", "Derece", "Bölge"], [
                ["$\\dfrac{\\pi}{6}$", "$30^\\circ$", "I"],
                ["$\\dfrac{5\\pi}{6}$", "$150^\\circ$", "II"],
                ["$\\dfrac{7\\pi}{6}$", "$210^\\circ$", "III"],
                ["$\\dfrac{11\\pi}{6}$", "$330^\\circ$", "IV"],
            ]),
            "Paydaları $6$ olan bu açılar, $\\pi$ nin altıda birinin katlarıdır ve hepsinin referans açısı $\\dfrac{\\pi}{6}$, yani $30^\\circ$ dir. Bu düzeni görmek, radyanla verilen soruları derece çevirmeden çözmeyi sağlar.",
        ]},
        {"baslik": "Tanjant ekseni", "icerik": [
            "Tanjantın da birim çemberde geometrik bir karşılığı vardır. Çembere $(1, 0)$ noktasında teğet olan $x=1$ doğrusuna <strong>tanjant ekseni</strong> denir. Açının kolu uzatılınca bu doğruyu kestiği noktanın yüksekliği $\\tan \\theta$ dır.",
            ornek(
                "$45^\\circ$ ve $60^\\circ$ açıları verilsin.",
                "Kolların tanjant eksenini kestiği noktaları bulalım.",
                "$\\tan 45^\\circ=1$; kol $x=1$ doğrusunu $(1, 1)$ de keser.",
                "$\\tan 60^\\circ=\\sqrt{3}$; kol $(1, \\sqrt{3})$ te keser."),
            "Açı $90^\\circ$ ye yaklaştıkça kol dikleşir ve tanjant eksenini giderek daha yüksekte keser; $90^\\circ$ de kol eksene paralel olur ve hiç kesmez. $\\tan 90^\\circ$ nin tanımsız olmasının geometrik nedeni budur.",
        ]},
        {"baslik": "Kotanjant ekseni", "icerik": [
            "Kotanjantın da benzer bir geometrik karşılığı vardır. Çembere $(0, 1)$ noktasında teğet olan $y=1$ doğrusuna <strong>kotanjant ekseni</strong> denir. Açının kolu uzatılınca bu doğruyu kestiği noktanın yatay koordinatı $\\cot \\theta$ dır.",
            ornek(
                "$45^\\circ$ ve $30^\\circ$ açıları verilsin.",
                "Kolların kotanjant eksenini kestiği noktaları bulalım.",
                "$\\cot 45^\\circ=1$; kol $y=1$ doğrusunu $(1, 1)$ de keser.",
                "$\\cot 30^\\circ=\\sqrt{3}$; kol $(\\sqrt{3}, 1)$ de keser."),
        ]},
        {"baslik": "Çeyrek dönüş eklemek", "icerik": [
            "Bir açıya $90^\\circ$ eklenince nokta çeyrek dönüş ilerler ve koordinatlar yer değiştirir. Bu yüzden $\\sin(90^\\circ+\\theta)=\\cos \\theta$ ve $\\cos(90^\\circ+\\theta)=-\\sin \\theta$ dır.",
            ornek(
                "$\\sin 120^\\circ$ ve $\\cos 120^\\circ$ değerleri istensin.",
                "Çeyrek dönüş kuralıyla bulalım.",
                "$120^\\circ=90^\\circ+30^\\circ$.",
                "$\\sin 120^\\circ=\\cos 30^\\circ=\\dfrac{\\sqrt{3}}{2}$ ve $\\cos 120^\\circ=-\\sin 30^\\circ=-\\dfrac{1}{2}$."),
        ]},
        {"baslik": "Simetriler", "icerik": [
            "Birim çemberdeki yansımalar, farklı açıların değerleri arasındaki ilişkileri verir. Aşağıdaki eşitlikler, noktaların eksenlere ya da başlangıç noktasına göre simetrisinden gelir.",
            tablo(["Açı", "$\\sin$", "$\\cos$", "Simetri"], [
                ["$-\\theta$", "$-\\sin \\theta$", "$\\cos \\theta$", "$x$ eksenine göre"],
                ["$180^\\circ-\\theta$", "$\\sin \\theta$", "$-\\cos \\theta$", "$y$ eksenine göre"],
                ["$180^\\circ+\\theta$", "$-\\sin \\theta$", "$-\\cos \\theta$", "Başlangıç noktasına göre"],
                ["$360^\\circ-\\theta$", "$-\\sin \\theta$", "$\\cos \\theta$", "$x$ eksenine göre"],
            ]),
            ornek(
                "$\\sin 135^\\circ$ ve $\\cos 240^\\circ$ değerleri istensin.",
                "Simetrilerle bulalım.",
                "$\\sin 135^\\circ=\\sin(180^\\circ-45^\\circ)=\\sin 45^\\circ=\\dfrac{\\sqrt{2}}{2}$.",
                "$\\cos 240^\\circ=\\cos(180^\\circ+60^\\circ)=-\\cos 60^\\circ=-\\dfrac{1}{2}$."),
        ]},
        {"baslik": "Aynı sinüse sahip açılar", "icerik": [
            "Birim çemberde aynı yükseklikteki iki nokta, yani yatay bir doğrunun çemberi kestiği iki nokta, aynı sinüse sahiptir. Bu noktalar $y$ eksenine göre simetriktir; bu yüzden $\\theta$ ile $180^\\circ-\\theta$ aynı sinüsü verir.",
            ornek(
                "$0^\\circ$ ile $360^\\circ$ arasında $\\sin \\theta=\\dfrac{\\sqrt{3}}{2}$ eşitliği verilsin.",
                "Açıları bulalım.",
                "Birinci bölgede $\\theta=60^\\circ$.",
                "Yüksekliği aynı olan ikinci nokta: $180^\\circ-60^\\circ=120^\\circ$."),
        ]},
        {"baslik": "Aynı kosinüse sahip açılar", "icerik": [
            "Aynı yatay konumdaki iki nokta aynı kosinüse sahiptir ve bu noktalar $x$ eksenine göre birbirinin tam simetriğidir. Bu yüzden $\\theta$ ile $360^\\circ-\\theta$ aynı kosinüsü verir.",
            ornek(
                "$0^\\circ$ ile $360^\\circ$ arasında $\\cos \\theta=-\\dfrac{1}{2}$ eşitliği verilsin.",
                "Açıları bulalım.",
                "Kosinüs negatif olduğu için noktalar ikinci ve üçüncü bölgededir; referans açı $60^\\circ$ dir.",
                "Açılar $180^\\circ-60^\\circ=120^\\circ$ ve $180^\\circ+60^\\circ=240^\\circ$ dir."),
        ]},
        {"baslik": "Birim çemberle eşitsizlik", "icerik": [
            "Trigonometrik eşitsizlikler birim çemberde bir yay olarak görünür ve bu yay, cebirsel bir işlem yapmadan çözüm aralığını gösterir. Örneğin sinüsün belirli bir değerden büyük olduğu açılar, çemberin o yüksekliğin üstünde kalan yayına karşılık gelir.",
            ornek(
                "$0^\\circ$ ile $360^\\circ$ arasında $\\sin \\theta>\\dfrac{1}{2}$ eşitsizliği verilsin.",
                "Çözüm aralığını bulalım.",
                "Sinüsün $\\dfrac{1}{2}$ olduğu açılar $30^\\circ$ ve $150^\\circ$ dir.",
                "Yükseklik bu iki nokta arasındaki yayda $\\dfrac{1}{2}$ den büyüktür: $30^\\circ<\\theta<150^\\circ$."),
        ]},
        {"baslik": "Noktadan oranlar", "icerik": [
            "Birim çember üzerindeki bir nokta verildiğinde açının bütün trigonometrik değerleri okunur: kosinüs yatay, sinüs dikey koordinattır; tanjant ve kotanjant bunların oranlarıdır.",
            ornek(
                "Birim çember üzerinde $P(-\\dfrac{3}{5}, \\dfrac{4}{5})$ noktası verilsin.",
                "Noktaya karşılık gelen açının bölgesini ve oranlarını bulalım.",
                "Kontrol: $\\dfrac{9}{25}+\\dfrac{16}{25}=1$; nokta çember üzerindedir ve ikinci bölgededir.",
                "$\\cos \\theta=-\\dfrac{3}{5}$, $\\sin \\theta=\\dfrac{4}{5}$, $\\tan \\theta=-\\dfrac{4}{3}$, $\\cot \\theta=-\\dfrac{3}{4}$."),
        ]},
        {"baslik": "Yarıçapı r olan çember", "icerik": [
            "Birim çemberdeki fikir her çembere genellenir: merkezi başlangıç noktası, yarıçapı $r$ olan bir çemberde $\\theta$ açısına karşılık gelen nokta $(r\\cos \\theta, r\\sin \\theta)$ dır. Birim çember, $r=1$ olan özel durumdur. Bu genelleme, dönen bir tekerleğin üzerindeki bir noktanın konumunu ya da bir saat kolunun ucunun yerini hesaplamak için kullanılır.",
            ornek(
                "Yarıçapı $4$ olan bir çemberde $60^\\circ$ lik açıya karşılık gelen nokta istensin.",
                "Noktanın koordinatlarını bulalım.",
                "$x=4\\cos 60^\\circ=2$.",
                "$y=4\\sin 60^\\circ=2\\sqrt{3}$. Nokta $(2, 2\\sqrt{3})$ tür."),
        ]},
        {"baslik": "Değerleri karşılaştırmak", "icerik": [
            "Birim çember, trigonometrik değerleri hesaplamadan karşılaştırmayı sağlar. Birinci bölgede açı büyüdükçe nokta yükselir ve sola kayar: sinüs artar, kosinüs azalır. Bu yüzden birinci bölgede açıları karşılaştırmak, değerleri karşılaştırmak için yeterlidir.",
            ornek(
                "$\\sin 20^\\circ$, $\\sin 70^\\circ$ ve $\\cos 20^\\circ$ değerleri verilsin.",
                "Değerleri karşılaştıralım.",
                "Birinci bölgede sinüs artan olduğu için $\\sin 20^\\circ<\\sin 70^\\circ$ dir.",
                "Tümler açılardan $\\cos 20^\\circ=\\sin 70^\\circ$ tir. Sıralama: $\\sin 20^\\circ<\\sin 70^\\circ=\\cos 20^\\circ$."),
        ]},
        {"baslik": "Yay uzunluğu ve açı", "icerik": [
            "Birim çemberde radyanın anlamı en açık biçimde görülür: yarıçap $1$ olduğu için radyan cinsinden açı, açının gördüğü yayın uzunluğuna eşittir. Tam dönüşün yay uzunluğu çemberin çevresi olan $2\\pi$ dir ve bu yüzden tam dönüş $2\\pi$ radyandır.",
            ornek(
                "Birim çemberde $(1, 0)$ noktasından başlayıp çember üzerinde $\\pi$ birim yol alan bir nokta verilsin.",
                "Noktanın vardığı yeri bulalım.",
                "Yay uzunluğu $\\pi$ olduğu için açı $\\pi$ radyan, yani $180^\\circ$ dir.",
                "Nokta $(-1, 0)$ noktasına varır; bu yarım dönüştür."),
        ]},
        {"baslik": "Birim çemberden grafiğe", "icerik": [
            "Birim çemberde dönen noktanın yüksekliği açıya göre çizilirse sinüs grafiği, yatay konumu çizilirse kosinüs grafiği elde edilir. Nokta $0^\\circ$ dan $90^\\circ$ ye giderken yükselir, $180^\\circ$ ye kadar iner, $270^\\circ$ de en alçak noktaya varır ve $360^\\circ$ de başladığı yere döner.",
            "Bu hareket, sinüs grafiğinin neden $-1$ ile $1$ arasında salındığını ve neden her $360^\\circ$ de bir tekrar ettiğini açıklar. Grafiklerin ayrıntısı <a href=\"/blog/trigonometrik-fonksiyon-grafikleri/\">Trigonometrik Fonksiyonların Grafikleri</a> yazısında.",
        ]},
        {"baslik": "Sınavda birim çember", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) birim çember; bölgelere göre işaretler, referans açıyla değer bulma, simetriler, aynı değeri veren açılar ve değer karşılaştırma biçiminde karşına çıkabilir.",
                "Trigonometrik denklem ve eşitsizlik soruları da çoğu zaman birim çember üzerinde düşünülerek çözülür."),
            "Birim çember sorularında açıyı çember üzerinde kabaca işaretlemek her zaman işe yarar. Noktanın hangi bölgede olduğu ve referans açısı bir kez görülünce işaret ve değer aynı anda belirlenir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Noktayı $(\\sin \\theta, \\cos \\theta)$ yazmak", "$(\\cos \\theta, \\sin \\theta)$"],
                ["Açıyı saat yönünde ölçmek", "Pozitif yön saat yönünün tersidir"],
                ["Referans açıyı $y$ eksenine göre almak", "Referans açı $x$ ekseniyle yapılan açıdır"],
                ["Aynı sinüsü veren tek açı yazmak", "$\\theta$ ve $180^\\circ-\\theta$"],
                ["Aynı kosinüsü veren açıları $180^\\circ-\\theta$ almak", "$\\theta$ ve $360^\\circ-\\theta$"],
                ["$\\tan 90^\\circ$ yi sonsuz sayı sanmak", "Tanımsızdır"],
            ]),
            "Bu hataların çoğu, çember çizilmeden ezbere işlem yapmaktan doğar. Küçük bir çember çizip noktayı işaretlemek, koordinatların hangisinin sinüs hangisinin kosinüs olduğunu ve işaretlerini bir bakışta gösterir.",
        ]},
    ],
    "sss": [
        ("Birim çember nedir?",
         "Merkezi başlangıç noktası, yarıçapı 1 olan çemberdir. Denklemi x kare artı y kare eşittir 1 dir."),
        ("Birim çemberde sinüs ve kosinüs nedir?",
         "Açıya karşılık gelen noktanın dikey koordinatı sinüs, yatay koordinatı kosinüstür."),
        ("Referans açı nedir?",
         "Açının kolunun x ekseniyle yaptığı dar açıdır. Değerlerin mutlak değeri referans açıdan, işaret bölgeden gelir."),
        ("Tanjant ekseni nedir?",
         "Birim çembere (1, 0) noktasında teğet olan x eşittir 1 doğrusudur. Açının kolunun bu doğruyu kestiği noktanın yüksekliği tanjanttır."),
        ("Hangi açılar aynı sinüsü verir?",
         "Açı teta ve 180 eksi teta aynı sinüsü verir, çünkü bu noktalar aynı yüksekliktedir."),
        ("Neden tanjant 90 derecede tanımsızdır?",
         "90 derecede kosinüs sıfırdır ve tanjant sinüsün kosinüse bölümüdür. Geometrik olarak açının kolu tanjant eksenine paraleldir ve onu kesmez."),
        ("Birim çemberde radyan ne anlama gelir?",
         "Yarıçap 1 olduğu için radyan cinsinden açı, açının gördüğü yayın uzunluğuna eşittir. Tam dönüşün yay uzunluğu 2 pi dir."),
        ("Bir açının bölgesi işaretlerden nasıl bulunur?",
         "Sinüsün işareti noktanın yukarıda mı aşağıda mı, kosinüsün işareti sağda mı solda mı olduğunu söyler. İkisi birlikte bölgeyi belirler."),
    ],
    "kontrol": [
        "Birim çemberin tanımını ve denklemini yazabiliyorum.",
        "Açıya karşılık gelen noktayı kosinüs ve sinüsle ifade edebiliyorum.",
        "Eksen noktalarındaki değerleri biliyorum.",
        "Bölgelere göre işaretleri belirleyebiliyorum.",
        "Birinci bölgedeki özel noktaları yazabiliyorum.",
        "Referans açıyla diğer bölgelerdeki noktaları bulabiliyorum.",
        "Tanjant eksenini yorumlayabiliyorum.",
        "Simetrilerle değer bulabiliyorum.",
        "Aynı sinüs ya da kosinüsü veren açıları bulabiliyorum.",
        "Çember üzerindeki bir noktadan bütün oranları okuyabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["trigonometri-konu-anlatimi", "trigonometrik-oranlar", "trigonometrik-fonksiyon-grafikleri"],
}
