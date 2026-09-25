# scripts/yazilar/43_teget_denklemi.py — Turevde Teget Denklemi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "teget-denklemi",
    "baslik": "Türevde Teğet Denklemi Nasıl Bulunur?",
    "aciklama": "Teğet denklemi nasıl bulunur? Eğim ve türev, nokta eğim formülü, normal doğru, yatay teğet, paralel teğet, dışarıdaki noktadan teğet; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "teget-denklemi",
    "kapak_alt": "Türevde teğet denklemi: ahşap eğriye tek noktada dokunan düz çubuğu ve eğim gönyesini yerleştiren öğrenci",
    "ozet": "Bir eğrinin bir noktadaki teğeti, eğriye o noktada dokunan ve eğrinin o noktadaki yönünü veren doğrudur. Teğetin eğimi fonksiyonun o noktadaki türevine eşit olduğu için teğet denklemi türevle kolayca yazılır. Bu yazıda teğetin anlamını, nokta eğim formülünü ve teğet yazmanın adımlarını, polinom, trigonometrik, üstel ve logaritmik eğrilerde teğeti, normal doğruyu, yatay teğetleri, eğimi verilen ya da bir doğruya paralel veya dik teğetleri, dışarıdaki bir noktadan çizilen teğetleri, teğetin eksenlerle oluşturduğu üçgeni, parametreli sorular ve ortak teğeti çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Teğet nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için türev kurallarını ve doğru denklemini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> ve <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> yazılarına göz at."),
            "Bir eğrinin bir noktasındaki teğeti, eğriye o noktada dokunan ve o noktanın yakınında eğriye en çok benzeyen doğrudur; eğriye çok yakından bakıldığında eğri ile teğet neredeyse ayırt edilemez. Eğri üzerindeki iki noktadan geçen kesen, noktalardan biri diğerine yaklaştıkça teğete dönüşür. Teğet eğriyi başka noktalarda kesebilir; önemli olan, dokunma noktasında eğrinin yönünü taşımasıdır.",
            "Kapaktaki öğrenci ahşap bir eğrinin üzerine düz bir çubuk yerleştiriyor; çubuk eğriye yalnızca bir noktada dokunuyor. Yanındaki gönye ise çubuğun eğimini ölçüyor. Teğet denklemi yazmak, bu çubuğun konumunu ve eğimini tek bir doğru denklemiyle ifade etmektir.",
        ]},
        {"baslik": "Teğetin eğimi türevdir", "icerik": [
            "Türevin geometrik anlamı teğetin eğimidir. $f$ fonksiyonunun grafiğine $x_0$ apsisli noktada çizilen teğetin eğimi $m=f'(x_0)$ dır. Bu tek bilgi, teğet denklemini yazmak için gereken her şeyin yarısını verir; diğer yarısı dokunma noktasının kendisidir.",
            hap("Teğetin eğimi, dokunma noktasındaki türev değeridir.",
                "Teğet, dokunma noktasından geçer ve bu eğime sahiptir."),
        ]},
        {"baslik": "Nokta eğim formülü", "icerik": [
            "Bir noktası $(x_0, y_0)$ ve eğimi $m$ olan doğrunun denklemi nokta eğim formülüyle yazılır:",
            "$$y-y_0=m(x-x_0)$$",
            "Teğet için $y_0=f(x_0)$ ve $m=f'(x_0)$ alınır. Böylece teğet denklemi $y-f(x_0)=f'(x_0)(x-x_0)$ olur. Denklem istenirse $y=mx+n$ biçimine getirilir; bu biçimde $n$ teğetin dikey ekseni kestiği noktayı gösterir.",
        ]},
        {"baslik": "Teğet yazmanın adımları", "icerik": [
            "Teğet denklemi her zaman aynı dört adımda yazılır. Adımların sırası her eğri için aynıdır ve her birinde tek bir hesap yapılır:",
            tablo(["Adım", "İşlem"], [
                ["1", "Dokunma noktasının apsisini $x_0$ belirle"],
                ["2", "Ordinatı hesapla: $y_0=f(x_0)$"],
                ["3", "Eğimi hesapla: $m=f'(x_0)$"],
                ["4", "$y-y_0=m(x-x_0)$ denklemini yaz ve düzenle"],
            ]),
            "En sık hata ikinci ve üçüncü adımları karıştırmaktır: ordinat fonksiyonun kendisinden, eğim ise türevden hesaplanır.",
        ]},
        {"baslik": "Polinom eğrisinde teğet", "icerik": [
            "İlk örnekte adımlar bir parabole uygulanıyor. Grafikte eğri ve teğet birlikte görülüyor; teğet eğriye yalnızca dokunma noktasında değiyor ve parabolün tamamı teğetin üst tarafında kalıyor. Bu, kolları yukarı bakan her parabolün her teğeti için geçerlidir.",
            koordinat_grafik("y = x² - 2x eğrisi ve x = 3 teki teğeti", [("y = x² - 2x", lambda x: x * x - 2 * x), ("teğet: y = 4x - 9", lambda x: 4 * x - 9)],
                             (-1.5, 5), (-2, 8), adim=1, noktalar=[(3, 3, "", True)]),
            ornek(
                "$f(x)=x^2-2x$ eğrisi ve $x_0=3$ verilsin.",
                "Teğet denklemini bulalım.",
                "$y_0=f(3)=3$ ve $f'(x)=2x-2$ olduğundan $m=f'(3)=4$ olur.",
                "$y-3=4(x-3)$, yani $y=4x-9$ bulunur."),
        ]},
        {"baslik": "Küp eğrisinde teğet", "icerik": [
            "Adımlar üçüncü dereceden eğrilerde de aynıdır. Negatif apsisli noktalarda işaretlere dikkat etmek yeterlidir; özellikle tek kuvvetlerde negatif sayının işareti korunur.",
            ornek(
                "$f(x)=x^3$ eğrisi ve $x_0=-1$ verilsin.",
                "Teğet denklemini bulalım.",
                "$y_0=(-1)^3=-1$ ve $f'(x)=3x^2$ olduğundan $m=3$ olur.",
                "$y+1=3(x+1)$, yani $y=3x+2$ bulunur."),
            "Bu teğet eğriyi dokunma noktası dışında bir kez daha keser: $x^3=3x+2$ denkleminin kökleri $-1$ ve $2$ dir. Teğetin eğriyi başka bir yerde kesmesi, onun teğet olmasına engel değildir.",
        ]},
        {"baslik": "Teğet eğriyi keser mi?", "icerik": [
            "Günlük dilde teğet, bir eğriye dokunup geçen ama onu kesmeyen doğru gibi düşünülür. Matematikte ise teğet, dokunma noktasında eğriyle aynı eğime sahip doğrudur ve eğriyi o noktada bile kesebilir.",
            "$y=x^3$ eğrisinin başlangıç noktasındaki teğeti $y=0$ doğrusudur; çünkü türev $3x^2$ sıfırda sıfırdır. Eğri bu noktada teğetin bir yanından öbür yanına geçer: negatif $x$ için teğetin altında, pozitif $x$ için üstündedir. Eğrinin bükülme yönünü değiştirdiği bu tür noktalara büküm noktası denir.",
        ]},
        {"baslik": "Teğetin eksenleri kestiği noktalar", "icerik": [
            "Teğet denklemi bulunduktan sonra $y=0$ yazılarak yatay ekseni, $x=0$ yazılarak dikey ekseni kestiği noktalar bulunur. Bu noktalar, teğetle ilgili alan ve uzunluk sorularının başlangıcıdır.",
            ornek(
                "$y=x^2-4$ eğrisi ve $x_0=1$ verilsin.",
                "Teğetin eksenleri kestiği noktaları bulalım.",
                "$y_0=-3$ ve $m=2$ olduğundan teğet $y=2x-5$ olur.",
                "Teğet dikey ekseni $(0, -5)$ te, yatay ekseni $\\left(\\dfrac{5}{2}, 0\\right)$ da keser."),
        ]},
        {"baslik": "Trigonometrik eğride teğet", "icerik": [
            "Trigonometrik eğrilerde apsis genellikle radyan cinsinden verilir. Değer ve türev hesaplanırken özel açıların değerleri kullanılır ve türev formülleri yalnızca radyan için geçerlidir.",
            ornek(
                "$f(x)=\\sin x$ eğrisi ve $x_0=\\pi$ verilsin.",
                "Teğet denklemini bulalım.",
                "$y_0=\\sin \\pi=0$ ve $m=\\cos \\pi=-1$ olur.",
                "$y-0=-1(x-\\pi)$, yani $y=-x+\\pi$ bulunur."),
            "Sinüs eğrisi başlangıç noktasında ise $y=x$ doğrusuna teğettir; çünkü $\\sin 0=0$ ve $\\cos 0=1$ dir. Küçük açılarda $\\sin x$ değerinin $x$ e yakın olmasının geometrik nedeni budur.",
        ]},
        {"baslik": "Üstel ve logaritmik eğrilerde teğet", "icerik": [
            "Üstel ve logaritmik eğriler birbirinin tersi olduğu için teğetleri de birbirinin yansımasıdır. İki eğrinin en sık sorulan teğetleri özel noktalardadır.",
            ornek(
                "$y=e^x$ eğrisi $x_0=0$ da, $y=\\ln x$ eğrisi $x_0=1$ de verilsin.",
                "İki teğet denklemini bulalım.",
                "$e^0=1$ ve türev $e^0=1$ olduğundan birinci teğet $y=x+1$ olur.",
                "$\\ln 1=0$ ve türev $\\dfrac{1}{1}=1$ olduğundan ikinci teğet $y=x-1$ olur."),
            "İki teğet birbirine paraleldir ve $y=x$ doğrusuna göre birbirinin yansımasıdır; bu, üstel ve logaritma fonksiyonlarının birbirinin tersi olmasından gelir.",
        ]},
        {"baslik": "Normal doğru", "icerik": [
            "Bir eğriye dokunma noktasında teğete dik olan doğruya <strong>normal doğru</strong> denir. Dik iki doğrunun eğimleri çarpımı $-1$ olduğu için normalin eğimi $-\\dfrac{1}{m}$ dir.",
            ornek(
                "$y=x^2$ eğrisi ve $(1, 1)$ noktası verilsin.",
                "Bu noktadaki normal doğrunun denklemini bulalım.",
                "Teğetin eğimi $2$ olduğundan normalin eğimi $-\\dfrac{1}{2}$ dir.",
                "$y-1=-\\dfrac{1}{2}(x-1)$, yani $y=-\\dfrac{1}{2}x+\\dfrac{3}{2}$ bulunur."),
            "Teğet yataysa normal dikey olur ve denklemi $x=x_0$ dır. Bu durumda eğim formülü kullanılamaz; dikey doğrunun eğimi tanımsızdır.",
        ]},
        {"baslik": "Yatay teğetler", "icerik": [
            "Türevin sıfır olduğu noktalarda teğet yataydır ve denklemi $y=y_0$ biçimindedir; eğim sıfır olduğu için nokta eğim formülünde $x$ li terim kaybolur. Bu noktalar grafiğin tepe ve çukur noktalarının adaylarıdır.",
            ornek(
                "$f(x)=x^3-3x^2$ eğrisi verilsin.",
                "Yatay teğetlerin denklemlerini bulalım.",
                "$f'(x)=3x^2-6x=3x(x-2)=0$ ise $x=0$ ya da $x=2$ olur.",
                "$f(0)=0$ ve $f(2)=-4$ olduğundan yatay teğetler $y=0$ ve $y=-4$ tür."),
        ]},
        {"baslik": "Eğimi verilen teğet", "icerik": [
            "Bazı sorularda dokunma noktası değil teğetin eğimi verilir ya da teğetin bir doğruya paralel olması istenir. Bu durumda işlem ters yönde yürür: önce eğimden dokunma noktası bulunur. Paralel doğruların eğimleri eşit olduğu için türev verilen eğime eşitlenir ve dokunma noktası bulunur.",
            ornek(
                "$y=x^2$ eğrisine çizilen ve $y=4x+1$ doğrusuna paralel olan teğet istensin.",
                "Teğet denklemini bulalım.",
                "Eğim $4$ olmalı: $2x=4$, yani $x_0=2$ ve $y_0=4$ olur.",
                "$y-4=4(x-2)$, yani $y=4x-4$ bulunur."),
        ]},
        {"baslik": "Bir doğruya dik teğet", "icerik": [
            "Teğetin bir doğruya dik olması isteniyorsa önce o doğrunun eğiminin negatif tersi alınır; bu değer teğetin eğimidir. Sonra türev bu eğime eşitlenir.",
            ornek(
                "$y=x^2$ eğrisine çizilen ve $y=-\\dfrac{1}{2}x+3$ doğrusuna dik olan teğet istensin.",
                "Teğet denklemini bulalım.",
                "Doğrunun eğimi $-\\dfrac{1}{2}$ olduğundan teğetin eğimi $2$ dir; $2x=2$ ise $x_0=1$ ve $y_0=1$.",
                "$y-1=2(x-1)$, yani $y=2x-1$ bulunur."),
        ]},
        {"baslik": "Dışarıdaki noktadan teğet", "icerik": [
            "Eğri üzerinde olmayan bir noktadan eğriye teğet çizilecekse dokunma noktası bilinmez. Dokunma noktası $(a, f(a))$ olarak alınır, bu noktadaki teğet genel olarak yazılır ve verilen noktadan geçmesi istenir.",
            ornek(
                "$(0, -1)$ noktasından $y=x^2$ eğrisine çizilen teğetler istensin.",
                "Teğet denklemlerini bulalım.",
                "$(a, a^2)$ deki teğet $y-a^2=2a(x-a)$ dır; $(0, -1)$ yazılınca $-1-a^2=-2a^2$, yani $a^2=1$ olur.",
                "$a=1$ için $y=2x-1$, $a=-1$ için $y=-2x-1$ bulunur."),
            "Dışarıdaki bir noktadan bir parabole genellikle iki teğet çizilir. Nokta parabolün içinde, yani kolları arasında kalan bölgedeyse hiç teğet çizilemez.",
        ]},
        {"baslik": "Teğetin eksenlerle oluşturduğu üçgen", "icerik": [
            "Teğet doğrusunun koordinat eksenlerini kestiği noktalar bulunarak teğetin eksenlerle oluşturduğu üçgenin alanı hesaplanabilir. Bu tür sorular teğet denkleminin yorumlanmasını ister.",
            ornek(
                "$y=\\dfrac{1}{x}$ eğrisi ve $x_0=2$ verilsin.",
                "Teğetin eksenlerle oluşturduğu üçgenin alanını bulalım.",
                "$y_0=\\dfrac{1}{2}$ ve $m=-\\dfrac{1}{4}$ olur; teğet $y=-\\dfrac{1}{4}x+1$ dir. Eksenleri $(4, 0)$ ve $(0, 1)$ noktalarında keser.",
                "Alan $\\dfrac{4 \\cdot 1}{2}=2$ birimkare olur."),
            "İlginç bir özellik: $y=\\dfrac{1}{x}$ eğrisinin birinci bölgedeki her teğeti, eksenlerle alanı tam $2$ olan bir üçgen oluşturur. Dokunma noktası değişse de alan değişmez.",
        ]},
        {"baslik": "Teğetten fonksiyon bilgisi okumak", "icerik": [
            "Bir eğrinin belirli bir noktadaki teğet denklemi verilmişse, o noktadaki fonksiyon değeri ve türev değeri doğrudan okunur. Bu bilgiler başka fonksiyonların türevini hesaplamak için kullanılabilir.",
            ornek(
                "$y=f(x)$ eğrisinin $x=2$ deki teğeti $y=3x-1$ olsun ve $g(x)=x f(x)$ tanımlansın.",
                "$g'(2)$ değerini bulalım.",
                "Teğetten $f(2)=3 \\cdot 2-1=5$ ve $f'(2)=3$ okunur.",
                "Çarpım kuralıyla $g'(2)=f(2)+2f'(2)=5+6=11$ bulunur."),
        ]},
        {"baslik": "Eğimi en küçük olan teğet", "icerik": [
            "Teğet eğimi $x_0$ a bağlı bir fonksiyondur: $m(x_0)=f'(x_0)$. Eğimin en küçük ya da en büyük olduğu nokta, bu eğim fonksiyonunun türevi sıfırlanarak bulunur.",
            ornek(
                "$y=x^3-3x^2+5$ eğrisi verilsin.",
                "Eğimi en küçük olan teğetin denklemini bulalım.",
                "Eğim $m=3x^2-6x$ tir; bu parabol $x=1$ de en küçük değeri olan $-3$ ü alır.",
                "Dokunma noktası $(1, 3)$ tür; teğet $y-3=-3(x-1)$, yani $y=-3x+6$ olur."),
        ]},
        {"baslik": "İki teğetin kesişimi", "icerik": [
            "Aynı eğriye farklı noktalarda çizilen iki teğet genellikle bir noktada kesişir. Kesişim noktası iki teğet denklemi birlikte çözülerek bulunur.",
            ornek(
                "$y=x^2$ eğrisine $x=1$ ve $x=-1$ noktalarında çizilen teğetler verilsin.",
                "Teğetlerin kesişim noktasını bulalım.",
                "Teğetler $y=2x-1$ ve $y=-2x-1$ dir.",
                "$2x-1=-2x-1$ ise $x=0$ ve $y=-1$ olur; teğetler $(0, -1)$ de kesişir."),
            "Bu sonuç, dışarıdaki noktadan teğet örneğinin tersidir: $(0, -1)$ noktasından çizilen iki teğet, eğriye tam olarak bu iki noktada dokunur.",
        ]},
        {"baslik": "Parametreli teğet soruları", "icerik": [
            "Bir eğrinin verilen bir doğruya belirli bir noktada teğet olması iki ayrı koşul verir ve bu koşullar birbirinden bağımsızdır: eğri o noktadan geçer ve eğimi doğrunun eğimine eşittir. Bu iki koşul iki bilinmeyeni bulmaya yeter.",
            ornek(
                "$f(x)=x^2+ax+b$ eğrisi $x=1$ noktasında $y=3x-1$ doğrusuna teğet olsun.",
                "$a$ ve $b$ yi bulalım.",
                "Nokta koşulu: $f(1)=3 \\cdot 1-1=2$, yani $1+a+b=2$. Eğim koşulu: $f'(1)=2+a=3$, yani $a=1$.",
                "Buradan $b=0$ bulunur; eğri $y=x^2+x$ olur."),
        ]},
        {"baslik": "Diskriminant ile teğetlik", "icerik": [
            "Bir doğrunun bir parabole teğet olması, ortak nokta denkleminin tek çözümü olması demektir. Bu yüzden bazı sorular türev kullanılmadan diskriminantla da çözülür.",
            ornek(
                "$y=mx$ doğrusu $y=x^2+1$ parabolüne teğet olsun.",
                "$m$ değerlerini bulalım.",
                "Ortak nokta denklemi $x^2-mx+1=0$ dır; teğetlik için $\\Delta=m^2-4=0$ olmalıdır.",
                "$m=2$ ya da $m=-2$ bulunur; dokunma noktaları $(1, 2)$ ve $(-1, 2)$ dir."),
            "Bu yöntemin ayrıntısı için <a href=\"/blog/parabol-ve-dogru/\">Parabol ve Doğru</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "İki eğrinin ortak teğeti", "icerik": [
            "İki eğri bir noktada birbirine dokunuyorsa o noktada ortak bir teğetleri vardır. Bunun için iki koşul gerekir: eğriler o noktada aynı değeri alır ve türevleri eşittir.",
            ornek(
                "$y=x^2$ ve $y=-x^2+4x-2$ eğrileri verilsin.",
                "Eğrilerin birbirine dokunduğu noktayı ve ortak teğeti bulalım.",
                "Ortak nokta: $x^2=-x^2+4x-2$, yani $2(x-1)^2=0$ ve $x=1$. İki eğrinin türevleri $x=1$ de $2$ ve $-2+4=2$ dir.",
                "Eğriler $(1, 1)$ de dokunur ve ortak teğet $y=2x-1$ olur."),
        ]},
        {"baslik": "Kapalı eğride teğet", "icerik": [
            "Çember gibi $y=f(x)$ biçiminde yazılmayan eğrilerde eğim kapalı türevle bulunur. Sonra aynı nokta eğim formülü kullanılır. Çemberde sonuç ayrıca geometriyle de denetlenebilir; teğet her zaman yarıçapa diktir.",
            ornek(
                "$x^2+y^2=25$ çemberi ve $(3, 4)$ noktası verilsin.",
                "Teğet denklemini bulalım.",
                "Kapalı türevden $y'=-\\dfrac{x}{y}$ ve bu noktada $m=-\\dfrac{3}{4}$ olur.",
                "$y-4=-\\dfrac{3}{4}(x-3)$, yani $y=-\\dfrac{3}{4}x+\\dfrac{25}{4}$ bulunur."),
            "Kapalı türevin ayrıntısı için <a href=\"/blog/zincir-kurali/\">Bileşke Fonksiyonun Türevi: Zincir Kuralı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Teğetin eğim açısı", "icerik": [
            "Bir doğrunun eğimi, yatay eksenle yaptığı açının tanjantıdır: $m=\\tan \\theta$. Bu yüzden teğetin yatay eksenle yaptığı açı türevden bulunur.",
            ornek(
                "$y=\\dfrac{x^2}{2}$ eğrisi verilsin.",
                "$x=1$ ve $x=\\sqrt{3}$ noktalarındaki teğetlerin yatay eksenle yaptığı açıları bulalım.",
                "$y'=x$ olduğundan eğimler $1$ ve $\\sqrt{3}$ tür.",
                "$\\tan \\theta=1$ için açı $45^\\circ$, $\\tan \\theta=\\sqrt{3}$ için $60^\\circ$ olur."),
        ]},
        {"baslik": "Teğetle yaklaşık hesap", "icerik": [
            "Teğet doğrusu dokunma noktasının yakınında eğriye çok yakın olduğu için hesaplaması zor değerler teğetle yaklaşık bulunabilir; hesap makinesi olmadan kök ve üs değerleri böyle tahmin edilir. Buna doğrusal yaklaşım denir.",
            ornek(
                "$y=\\sqrt{x}$ eğrisi ve $x_0=4$ verilsin.",
                "Teğeti yazıp $\\sqrt{4.1}$ değerini yaklaşık bulalım.",
                "$y_0=2$ ve $m=\\dfrac{1}{4}$ olduğundan teğet $y=\\dfrac{1}{4}x+1$ olur.",
                "$x=4.1$ için teğet $2.025$ verir; gerçek değer yaklaşık $2.0248$ dir."),
        ]},
        {"baslik": "Sınavda teğet denklemi", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) teğet soruları; bir noktadaki teğet, normal doğru, eğimi verilen ya da bir doğruya paralel teğet, teğetin eksenleri kestiği noktalar ve parametreli teğet biçiminde karşına çıkabilir.",
                "Teğet soruları çoğu zaman türev değeri ile fonksiyon değerinin birlikte kullanılmasını ister."),
            "Soruda teğet denklemi verilip fonksiyon hakkında bir şey soruluyorsa şunu hatırla: teğetin eğimi $f'(x_0)$, teğetin dokunma noktasındaki değeri $f(x_0)$ dır. Bu iki bilgi çoğu soruyu tek başına çözer.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Ordinatı türevden hesaplamak", "$y_0=f(x_0)$"],
                ["Eğimi fonksiyondan hesaplamak", "$m=f'(x_0)$"],
                ["Eğim olarak türev fonksiyonunu yazmak", "Türev $x_0$ da hesaplanır"],
                ["Normalin eğimini $-m$ almak", "$-\\dfrac{1}{m}$"],
                ["Dışarıdaki noktayı dokunma noktası sanmak", "Dokunma noktası $(a, f(a))$ alınır"],
                ["Teğetin eğriyi başka yerde kesmeyeceğini sanmak", "Kesebilir"],
            ]),
            "Teğet denklemi yazdıktan sonra iki kontrol yap: doğru dokunma noktasından geçiyor mu ve eğimi türev değerine eşit mi? İki kontrol de tutuyorsa denklem doğrudur.",
        ]},
    ],
    "sss": [
        ("Teğet denklemi nasıl bulunur?",
         "Dokunma noktasının ordinatı fonksiyondan, eğimi türevden hesaplanır ve y eksi y0 eşittir m çarpı x eksi x0 formülüyle doğru yazılır."),
        ("Teğetin eğimi nedir?",
         "Dokunma noktasındaki türev değeridir: m eşittir f üssü x0."),
        ("Normal doğru nedir?",
         "Dokunma noktasında teğete dik olan doğrudur. Eğimi teğet eğiminin negatif tersidir."),
        ("Yatay teğet nerede olur?",
         "Türevin sıfır olduğu noktalarda. Bu noktalarda teğet denklemi y eşittir fonksiyonun o noktadaki değeri biçimindedir."),
        ("Bir doğruya paralel teğet nasıl bulunur?",
         "Türev, doğrunun eğimine eşitlenir ve dokunma noktası bulunur; sonra teğet denklemi yazılır."),
        ("Dışarıdaki bir noktadan teğet nasıl çizilir?",
         "Dokunma noktası (a, f(a)) alınır, bu noktadaki teğet yazılır ve verilen noktadan geçmesi istenerek a bulunur."),
        ("Teğet eğriyi kesebilir mi?",
         "Evet. Teğet, dokunma noktasında eğriyle aynı eğime sahip doğrudur; eğriyi başka noktalarda, hatta büküm noktalarında dokunma noktasının kendisinde de kesebilir."),
        ("Teğet denklemi verilirse fonksiyon hakkında ne öğrenilir?",
         "Dokunma noktasındaki fonksiyon değeri teğetin o noktadaki değerinden, türev değeri ise teğetin eğiminden okunur."),
    ],
    "kontrol": [
        "Teğetin geometrik anlamını açıklayabiliyorum.",
        "Teğetin eğiminin türev olduğunu biliyorum.",
        "Nokta eğim formülüyle teğet denklemi yazabiliyorum.",
        "Polinom, trigonometrik, üstel ve logaritmik eğrilerde teğet bulabiliyorum.",
        "Normal doğrunun denklemini yazabiliyorum.",
        "Yatay teğetleri bulabiliyorum.",
        "Eğimi verilen, paralel ya da dik teğeti bulabiliyorum.",
        "Dışarıdaki bir noktadan çizilen teğetleri bulabiliyorum.",
        "Teğetin eksenlerle oluşturduğu üçgenin alanını hesaplayabiliyorum.",
        "Parametreli teğet ve ortak teğet sorularını çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["turev-alma-kurallari", "artan-azalan-fonksiyonlar", "parabol-ve-dogru"],
}
