# scripts/yazilar/48_belirli_integral.py — Belirli Integral Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "belirli-integral",
    "baslik": "Belirli İntegral Konu Anlatımı",
    "aciklama": "Belirli integral nedir, nasıl hesaplanır? Temel teorem, özellikler, parçalı ve mutlak değerli integraller, simetri, işaretli alan, sınır türevi; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "belirli-integral",
    "kapak_alt": "Belirli integral: iki sınır direği arasında eğrinin altındaki bölgeyi şeritlerle dolduran iki öğrenci",
    "ozet": "Belirli integral, bir fonksiyonun iki sınır arasındaki toplam etkisini tek bir sayıyla veren işlemdir; fonksiyon pozitifken eğrinin altındaki alana eşittir. Analizin temel teoremi sayesinde ters türevin iki sınırdaki değerlerinin farkıyla hesaplanır. Bu yazıda belirli integralin tanımını ve gösterimini, temel teoremi, polinom, kök, üstel, logaritmik ve trigonometrik fonksiyonların belirli integralini, belirli integralin özelliklerini, parçalı ve mutlak değerli integralleri, tek ve çift fonksiyonlarda simetriyi, işaretli alanı, sınırlarla değişken değiştirmeyi, üst sınırı değişken integralin türevini ve yer değiştirme ile toplam yol gibi uygulamaları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Belirli integral nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için belirsiz integral kurallarını ve integralin temel fikrini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/belirsiz-integral/\">Belirsiz İntegral Konu Anlatımı</a> ve <a href=\"/blog/integral-konu-anlatimi/\">İntegral Konu Anlatımı</a> yazılarına göz at."),
            "Belirsiz integral sonsuz sayıda fonksiyondan oluşan bir aile verir. <strong>Belirli integral</strong> ise iki sınır arasında hesaplanan tek bir sayıdır ve $\\int_a^b f(x)\\,dx$ biçiminde yazılır. $a$ alt sınır, $b$ üst sınırdır. Fonksiyon bu aralıkta pozitifse belirli integral, eğrinin altında ve yatay eksenin üstünde kalan bölgenin alanına eşittir.",
            "Kapaktaki öğrenciler iki sınır direği arasında kalan bölgeyi eğrinin altına kadar şeritlerle dolduruyor. Direklerin dışındaki bölge hesaba katılmıyor. Belirli integral, direkler arasındaki bu şeritlerin toplam alanıdır ve şeritler inceldikçe tam değere ulaşılır.",
        ]},
        {"baslik": "Belirsiz ve belirli integral farkı", "icerik": [
            "İki kavram aynı işareti kullanır ama farklı şeyler verir. Belirsiz integral $\\int f(x)\\,dx$ bir fonksiyon ailesidir ve sonucunda $+C$ bulunur. Belirli integral $\\int_a^b f(x)\\,dx$ ise sınırları olan tek bir sayıdır.",
            "Aralarındaki bağ temel teoremdir: belirli integrali hesaplamak için belirsiz integralden bir üye seçilir ve iki sınırdaki değerleri çıkarılır. Hangi üyenin seçildiği önemli değildir; çünkü sabitler çıkarma işleminde birbirini götürür.",
        ]},
        {"baslik": "Tanım: dikdörtgen toplamlarının limiti", "icerik": [
            "$[a, b]$ aralığı $n$ eşit parçaya bölünür ve her parçada yüksekliği fonksiyon değeri olan bir dikdörtgen çizilir. Dikdörtgenlerin alanları toplamı $\\sum_{k=1}^{n} f(x_k)\\,\\Delta x$ tir. Parça sayısı sonsuza giderken bu toplamın limiti belirli integrali verir.",
            ornek(
                "$f(x)=x$ fonksiyonu $[0, 1]$ aralığında verilsin.",
                "Sağ uç toplamlarının limitini bulalım.",
                "$n$ parçada sağ uç toplamı $\\dfrac{1}{n}\\left(\\dfrac{1}{n}+\\dfrac{2}{n}+\\cdots+\\dfrac{n}{n}\\right)=\\dfrac{n+1}{2n}$ olur.",
                "$n$ sonsuza giderken limit $\\dfrac{1}{2}$ dir; bu, dik kenarları $1$ olan üçgenin alanıdır."),
            "Tanım, belirli integralin bir alan olduğunu açıklar ama hesap için uzundur; her fonksiyon için ayrı bir toplam formülü ve limit gerekir. Pratikte temel teorem kullanılır ve tanım yalnızca kavramı anlamak için akılda tutulur.",
        ]},
        {"baslik": "Analizin temel teoremi", "icerik": [
            "$f$ fonksiyonu $[a, b]$ aralığında sürekli ve $F$ onun bir ters türevi olsun. Belirli integral, ters türevin üst sınırdaki değerinden alt sınırdaki değerinin çıkarılmasıyla bulunur:",
            "$$\\int_a^b f(x)\\,dx=F(b)-F(a)$$",
            "Hesapta ara adım genellikle köşeli parantezle gösterilir: $\\left[F(x)\\right]_a^b=F(b)-F(a)$. Belirli integralde integral sabiti yazılmaz; iki değerin farkı alınırken sabit sadeleşir.",
            hap("Önce ters türev, sonra üst sınır eksi alt sınır.",
                "Belirli integralin sonucu bir sayıdır, $C$ yazılmaz."),
        ]},
        {"baslik": "Temel teoremin sezgisi", "icerik": [
            "Temel teorem neden doğrudur? $F$ nin türevi $f$ olduğu için $f$, $F$ nin değişim hızıdır. Bir niceliğin değişim hızı bir aralık boyunca toplanırsa, niceliğin o aralıktaki toplam değişimi elde edilir. Bu toplam değişim de $F(b)-F(a)$ dır.",
            "Günlük bir örnekle: bir aracın hızı her an biliniyorsa, hızların küçük zaman aralıklarıyla çarpılıp toplanması alınan yolu verir. Aynı yol, kilometre sayacının başlangıç ve bitişteki değerlerinin farkıdır. Temel teorem, bu iki hesabın her zaman aynı sonucu verdiğini söyler.",
        ]},
        {"baslik": "Sabit fonksiyonun integrali", "icerik": [
            "Sabit bir fonksiyonun grafiği yatay bir doğrudur ve iki sınır arasında altında kalan bölge bir dikdörtgendir. Belirli integral bu dikdörtgenin alanını, yani yükseklik ile genişliğin çarpımını verir.",
            ornek(
                "$\\int_1^4 3\\,dx$ integrali verilsin.",
                "İntegrali iki yoldan hesaplayalım.",
                "Temel teoremle $\\left[3x\\right]_1^4=12-3=9$ olur.",
                "Geometriyle yüksekliği $3$, genişliği $3$ olan dikdörtgenin alanı $9$ dur."),
        ]},
        {"baslik": "Polinomların belirli integrali", "icerik": [
            "Polinomlarda ters türev terim terim bulunur, sonra iki sınır ayrı ayrı yerine yazılır ve farkları alınır. Sınırlardan biri sıfır olduğunda o kısmın değeri çoğu zaman sıfır çıkar ve hesap kısalır.",
            ornek(
                "$\\int_1^2 (3x^2-2x)\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "Ters türev $x^3-x^2$ dir: $\\left[x^3-x^2\\right]_1^2=(8-4)-(1-1)$.",
                "Sonuç $4$ tür."),
            ornek(
                "$\\int_0^1 (x+1)^2\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "Ters türev $\\dfrac{(x+1)^3}{3}$ tür: $\\dfrac{8}{3}-\\dfrac{1}{3}$.",
                "Sonuç $\\dfrac{7}{3}$ olur."),
        ]},
        {"baslik": "Kök ve kesir içeren integraller", "icerik": [
            "Kök ve paydada $x$ bulunan terimler önce üslü biçimde yazılır, ters türev bulunur ve sınırlar yerine konur. Sınırların tam kare olması hesabı kolaylaştırır.",
            ornek(
                "$\\int_1^4 \\dfrac{1}{\\sqrt{x}}\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$x^{-1/2}$ nin ters türevi $2\\sqrt{x}$ tir: $\\left[2\\sqrt{x}\\right]_1^4=4-2$.",
                "Sonuç $2$ dir."),
        ]},
        {"baslik": "Üstel ve logaritmik integraller", "icerik": [
            "Üstel ve logaritmik fonksiyonlarda sınırlar çoğu zaman $\\ln 2$ ya da $e$ gibi seçilir; böylece ters türevin değerleri basit sayılar çıkar.",
            ornek(
                "$\\int_0^{\\ln 2} e^x\\,dx$ ve $\\int_1^{e^2}\\dfrac{1}{x}\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "Birincisi $e^{\\ln 2}-e^0=2-1=1$ olur.",
                "İkincisi $\\ln e^2-\\ln 1=2$ olur."),
            "Üssünde katsayı bulunan fonksiyonlarda katsayı bölen olarak gelir: $\\int_0^1 e^{2x}\\,dx=\\dfrac{e^2-1}{2}$ dir.",
        ]},
        {"baslik": "Trigonometrik integraller", "icerik": [
            "Trigonometrik belirli integrallerde sınırlar genellikle radyan cinsinden özel açılardır. Ters türev bulunduktan sonra özel açıların sinüs, kosinüs ve tanjant değerleri kullanılır.",
            ornek(
                "$\\int_0^{\\pi/2}\\sin x\\,dx$ ve $\\int_0^{\\pi/4}\\dfrac{1}{\\cos^2 x}\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "Birincisi $-\\cos \\dfrac{\\pi}{2}+\\cos 0=1$ olur.",
                "İkincisi $\\tan \\dfrac{\\pi}{4}-\\tan 0=1$ olur."),
            "Kosinüsün $[0, \\pi]$ aralığındaki integrali ise $\\sin \\pi-\\sin 0=0$ dır; aralığın ilk yarısındaki pozitif alan, ikinci yarısındaki negatif alanla tam olarak dengelenir.",
        ]},
        {"baslik": "Kare trigonometrik integral", "icerik": [
            "Sinüs karesi gibi ifadelerin belirli integrali kuvvet azaltma formülüyle alınır. Sınırlar bir periyodun katıysa trigonometrik terim çoğu zaman sıfıra gider ve sonuç basit çıkar.",
            ornek(
                "$\\int_0^{\\pi}\\sin^2 x\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$\\sin^2 x=\\dfrac{1-\\cos 2x}{2}$ olduğundan ters türev $\\dfrac{x}{2}-\\dfrac{\\sin 2x}{4}$ tir.",
                "Sınırlar yerine yazılınca $\\dfrac{\\pi}{2}-0=\\dfrac{\\pi}{2}$ bulunur."),
        ]},
        {"baslik": "Geometriyle hesaplanan integral", "icerik": [
            "Ters türevi kolayca bulunamayan ya da hiç bulunamayan bazı integraller, grafiğin bilinen bir geometrik şekil olduğu fark edilerek hesaplanır. Yarım çember bunun en bilinen örneğidir.",
            ornek(
                "$\\int_{-2}^{2}\\sqrt{4-x^2}\\,dx$ integrali verilsin.",
                "İntegrali geometriyle bulalım.",
                "$y=\\sqrt{4-x^2}$ nin grafiği yarıçapı $2$ olan çemberin üst yarısıdır.",
                "İntegral yarım dairenin alanıdır: $\\dfrac{\\pi \\cdot 2^2}{2}=2\\pi$ olur."),
        ]},
        {"baslik": "Belirli integralin özellikleri", "icerik": [
            "Belirli integralin özellikleri, alanın ve toplamanın doğal özelliklerinden gelir ve ezberlenmesi kolaydır. Bu özellikler hesapları kısaltır ve sınırlarla ilgili soruların temelini oluşturur:",
            tablo(["Özellik", "Formül"], [
                ["Eşit sınırlar", "$\\int_a^a f(x)\\,dx=0$"],
                ["Sınırların yer değiştirmesi", "$\\int_b^a f=-\\int_a^b f$"],
                ["Aralığın bölünmesi", "$\\int_a^b f+\\int_b^c f=\\int_a^c f$"],
                ["Sabitle çarpım", "$\\int_a^b kf=k\\int_a^b f$"],
                ["Toplam", "$\\int_a^b (f+g)=\\int_a^b f+\\int_a^b g$"],
            ]),
            "Aralığın bölünmesi özelliği, $b$ noktası $a$ ile $c$ arasında olmasa da geçerlidir. Bu, işaretli alanın ve sınırların yer değiştirmesi kuralının doğal sonucudur.",
            hap("$\\int_a^b f(x)\\,dx=-\\int_b^a f(x)\\,dx$ olur.", "$\\int_a^b f(x)\\,dx+\\int_b^c f(x)\\,dx=\\int_a^c f(x)\\,dx$ olur."),
        ]},
        {"baslik": "Özelliklerle hesap", "icerik": [
            "Fonksiyonun kendisi verilmeden yalnızca bazı integral değerleri verildiğinde, istenen integral özelliklerle bulunur. Bu sorularda fonksiyonu bulmaya çalışmak gereksizdir; özellikler tek başına yeterlidir.",
            ornek(
                "$\\int_1^3 f(x)\\,dx=5$ ve $\\int_3^6 f(x)\\,dx=2$ olsun.",
                "$\\int_1^6 f$, $\\int_6^1 f$ ve $\\int_1^3 (2f(x)+1)\\,dx$ değerlerini bulalım.",
                "Aralık birleşimiyle $\\int_1^6 f=7$, sınırların yer değiştirmesiyle $\\int_6^1 f=-7$ olur.",
                "Doğrusallıkla $2 \\cdot 5+\\int_1^3 1\\,dx=10+2=12$ olur."),
        ]},
        {"baslik": "Sınırların yer değiştirmesi", "icerik": [
            "Alt sınır üst sınırdan büyük olduğunda da temel teorem aynı biçimde uygulanır; sonuç, sınırları doğru sırada olan integralin ters işaretlisi çıkar. Bu, soldan sağa değil sağdan sola toplamanın işaretinin ters olması demektir.",
            ornek(
                "$\\int_2^0 x\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$\\left[\\dfrac{x^2}{2}\\right]_2^0=0-2=-2$ olur.",
                "Sonuç, $\\int_0^2 x\\,dx=2$ nin ters işaretlisidir."),
        ]},
        {"baslik": "Parçalı fonksiyonların integrali", "icerik": [
            "Parçalı bir fonksiyonun integrali alınırken aralık, kuralın değiştiği kritik noktalardan bölünür. Her parçada o parçanın kuralıyla integral alınır ve sonuçlar toplanır.",
            ornek(
                "$x<1$ için $f(x)=x^2$, $x \\ge 1$ için $f(x)=2x-1$ olsun.",
                "$\\int_0^2 f(x)\\,dx$ integralini bulalım.",
                "$\\int_0^1 x^2\\,dx=\\dfrac{1}{3}$ ve $\\int_1^2 (2x-1)\\,dx=\\left[x^2-x\\right]_1^2=2$ olur.",
                "Toplam $\\dfrac{1}{3}+2=\\dfrac{7}{3}$ bulunur."),
        ]},
        {"baslik": "Mutlak değerli integraller", "icerik": [
            "Mutlak değerli bir fonksiyonun integralinde önce içteki ifadenin sıfır olduğu, yani işaret değiştirdiği nokta bulunur. Aralık bu noktadan bölünür ve her parçada mutlak değer uygun işaretle açılır.",
            ornek(
                "$\\int_0^3 |x-1|\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$[0, 1]$ de $|x-1|=1-x$, $[1, 3]$ te $|x-1|=x-1$ olur; integraller $\\dfrac{1}{2}$ ve $2$ dir.",
                "Sonuç $\\dfrac{5}{2}$ olur; grafikte bu, iki üçgenin alanları toplamıdır."),
        ]},
        {"baslik": "Tek ve çift fonksiyonlarda simetri", "icerik": [
            "Simetrik bir aralıkta, yani $[-a, a]$ aralığında integral alınırken fonksiyonun simetrisi işi çok kısaltır ve çoğu zaman hesabı tamamen ortadan kaldırır. Tek bir fonksiyonun grafiği orijine göre simetrik olduğu için pozitif ve negatif alanlar birbirini götürür; çift bir fonksiyonda ise iki yarının integrali eşittir.",
            tablo(["Fonksiyon", "Simetrik aralıkta integral"], [
                ["Tek: $f(-x)=-f(x)$", "$\\int_{-a}^{a} f=0$"],
                ["Çift: $f(-x)=f(x)$", "$\\int_{-a}^{a} f=2\\int_0^a f$"],
            ]),
            ornek(
                "$\\int_{-2}^{2} x^3\\,dx$ ve $\\int_{-1}^{1} x^2\\,dx$ integralleri verilsin.",
                "Simetriyle hesaplayalım.",
                "$x^3$ tek olduğundan birincisi $0$ dır.",
                "$x^2$ çift olduğundan ikincisi $2\\int_0^1 x^2\\,dx=\\dfrac{2}{3}$ olur."),
            hap("Tek bir fonksiyonun $[-a, a]$ aralığındaki integrali $0$ olur.", "Çift bir fonksiyonda bu integral, $[0, a]$ aralığındaki integralin iki katıdır."),
        ]},
        {"baslik": "İşaretli alan ve gerçek alan", "icerik": [
            "Fonksiyonun negatif olduğu aralıklarda belirli integral negatif katkı yapar. Bu yüzden belirli integral bir alan değil, işaretli alandır. Gerçek alan isteniyorsa fonksiyonun işaret değiştirdiği noktalardan aralık bölünür ve her parçanın mutlak değeri alınır.",
            ornek(
                "$f(x)=x$ fonksiyonu $[-1, 2]$ aralığında verilsin.",
                "Belirli integrali ve grafikle eksen arasındaki gerçek alanı bulalım.",
                "$\\int_{-1}^{2} x\\,dx=\\dfrac{4}{2}-\\dfrac{1}{2}=\\dfrac{3}{2}$ olur.",
                "Gerçek alan $\\left|\\int_{-1}^{0} x\\,dx\\right|+\\int_0^2 x\\,dx=\\dfrac{1}{2}+2=\\dfrac{5}{2}$ olur."),
            "Alan hesabının bütün durumları <a href=\"/blog/integral-alan-hesaplama/\">İntegral ile Alan Hesaplama</a> yazısında.",
        ]},
        {"baslik": "Sınırlarla değişken değiştirme", "icerik": [
            "Belirli integralde değişken değiştirildiğinde sınırlar da yeni değişkene göre yeniden yazılır; eski sınırlar yeni değişken için anlamsızdır. Böylece sonuç eski değişkene geri dönmeden hesaplanır.",
            ornek(
                "$\\int_0^1 2x(x^2+1)^3\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+1$ ve $du=2x\\,dx$ olur; $x=0$ için $u=1$, $x=1$ için $u=2$ dir.",
                "İntegral $\\int_1^2 u^3\\,du=\\dfrac{16-1}{4}=\\dfrac{15}{4}$ olur."),
            "Yöntemin ayrıntıları için <a href=\"/blog/degisken-degistirme/\">İntegralde Değişken Değiştirme Yöntemi</a> yazısına bakabilirsin.",
            hap("Belirli integralde değişken değiştirilince sınırlar da yeni değişkene göre yeniden yazılır."),
        ]},
        {"baslik": "Üst sınırı değişken integral", "icerik": [
            "Üst sınırı $x$ olan bir integral, sınır değiştikçe değeri de değiştiği için $x$ in bir fonksiyonudur. Temel teoremin ikinci biçimine göre bu fonksiyonun türevi, integrali alınan fonksiyonun üst sınırdaki değeridir: $\\dfrac{d}{dx}\\int_a^x f(t)\\,dt=f(x)$.",
            ornek(
                "$G(x)=\\int_1^x (t^2+1)\\,dt$ ve $H(x)=\\int_0^{x^2}\\cos t\\,dt$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$G'(x)=x^2+1$ olur.",
                "Üst sınır $x^2$ olduğundan zincir kuralıyla $H'(x)=\\cos(x^2) \\cdot 2x$ olur."),
        ]},
        {"baslik": "Limiti integrale çevirmek", "icerik": [
            "Tanım tersten de kullanılabilir: bazı uzun toplamların limiti, bir belirli integral olarak tanınır ve kolayca hesaplanır. Toplam $\\dfrac{1}{n}\\sum f\\left(\\dfrac{k}{n}\\right)$ biçimindeyse limit, $f$ nin $[0, 1]$ aralığındaki integralidir.",
            ornek(
                "$\\lim_{n \\to \\infty}\\dfrac{1}{n}\\sum_{k=1}^{n}\\left(\\dfrac{k}{n}\\right)^2$ limiti verilsin.",
                "Limiti bulalım.",
                "Toplam, $f(x)=x^2$ için $[0, 1]$ aralığındaki sağ uç toplamıdır.",
                "Limit $\\int_0^1 x^2\\,dx=\\dfrac{1}{3}$ olur."),
        ]},
        {"baslik": "Sınırda bilinmeyen", "icerik": [
            "Belirli integralin değeri verilip sınırlardan biri bilinmeyen olarak sorulabilir. Ters türev sınırlarla hesaplanır ve verilen değere eşitlenir; ortaya çıkan denklem çözülür.",
            ornek(
                "$k>0$ ve $\\int_0^k 2x\\,dx=9$ olsun.",
                "$k$ yı bulalım.",
                "$\\left[x^2\\right]_0^k=k^2$ olduğundan $k^2=9$ olur.",
                "$k>0$ olduğundan $k=3$ bulunur."),
        ]},
        {"baslik": "Ortalama değer", "icerik": [
            "Bir fonksiyonun $[a, b]$ aralığındaki ortalama değeri $\\dfrac{1}{b-a}\\int_a^b f(x)\\,dx$ tir. Geometrik olarak bu, eğrinin altındaki alanla aynı alana sahip, tabanı aralık olan dikdörtgenin yüksekliğidir.",
            ornek(
                "$f(x)=\\sin x$ fonksiyonu $[0, \\pi]$ aralığında verilsin.",
                "Ortalama değerini bulalım.",
                "$\\int_0^{\\pi}\\sin x\\,dx=2$ dir.",
                "Ortalama değer $\\dfrac{2}{\\pi}$, yaklaşık $0.64$ olur."),
        ]},
        {"baslik": "İntegralleri karşılaştırmak", "icerik": [
            "Bir aralıkta bir fonksiyon diğerinden hep küçükse, o aralıktaki integrali de küçüktür. Bu özellik, integrali hesaplamadan karşılaştırma yapmayı sağlar.",
            ornek(
                "$[0, 1]$ aralığında $x^2$ ile $x$ fonksiyonları verilsin.",
                "İntegrallerini karşılaştıralım.",
                "Bu aralıkta $x^2 \\le x$ olduğundan $\\int_0^1 x^2\\,dx \\le \\int_0^1 x\\,dx$ olmalıdır.",
                "Gerçekten $\\dfrac{1}{3}<\\dfrac{1}{2}$ dir."),
        ]},
        {"baslik": "Uygulama: yer değiştirme ve toplam yol", "icerik": [
            "Hızın belirli integrali başlangıç ve bitiş konumları arasındaki farkı, yani yer değiştirmeyi verir; hareket yönü değişiyorsa ileri ve geri hareketler birbirini götürür. Toplam yol ise hızın mutlak değerinin integralidir.",
            ornek(
                "Bir cismin hızı $v(t)=t-2$ metre bölü saniye olsun.",
                "$[0, 4]$ aralığında yer değiştirmeyi ve toplam yolu bulalım.",
                "Yer değiştirme $\\int_0^4 (t-2)\\,dt=\\left[\\dfrac{t^2}{2}-2t\\right]_0^4=0$ olur; cisim başladığı yere döner.",
                "Toplam yol $\\int_0^4 |t-2|\\,dt=2+2=4$ metre olur."),
        ]},
        {"baslik": "Uygulama: enerji", "icerik": [
            "Güç, enerjinin zamana göre değişim hızıdır ve birimi kilovattır; bu yüzden gücün zamana göre integrali harcanan ya da üretilen enerjiyi verir. Elektrik faturalarındaki kilovatsaat birimi de bu integralin sonucudur.",
            ornek(
                "Bir cihazın gücü $P(t)=2t$ kilovat olsun; $t$ saat cinsindendir.",
                "İlk üç saatte harcanan enerjiyi bulalım.",
                "Enerji $\\int_0^3 2t\\,dt=\\left[t^2\\right]_0^3$ olur.",
                "Harcanan enerji $9$ kilovatsaattir."),
            hap("Gücü $2$ kilovat olan bir ısıtıcı $3$ saat çalışırsa harcanan enerji $2 \\cdot 3=6$ kilovatsaat olur.", "Bu değer, güç zaman grafiğinin altındaki alanı, yani gücün zamana göre integralini gösterir.", gunluk=True),
        ]},
        {"baslik": "Sınavda belirli integral", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) belirli integral; temel teoremle hesap, özelliklerle hesap, parçalı ve mutlak değerli integraller, simetri, sınırda bilinmeyen ve üst sınırı değişken integralin türevi biçiminde karşına çıkabilir.",
                "Alan soruları da belirli integralin doğrudan uygulamasıdır."),
            "Sınırları yerleştirirken her zaman önce üst sınırı yaz. Simetrik aralık görüyorsan önce fonksiyonun tek ya da çift olup olmadığına bak; tek fonksiyonlarda sonuç hesap yapmadan sıfırdır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$F(a)-F(b)$ yazmak", "$F(b)-F(a)$"],
                ["Belirli integrale $+C$ eklemek", "Sonuç bir sayıdır"],
                ["Mutlak değeri açmadan integral almak", "Aralık bölünür"],
                ["Değişken değiştirip sınırları değiştirmemek", "Sınırlar da dönüştürülür"],
                ["İşaretli alanı gerçek alan sanmak", "Negatif parçalar ayrı alınır"],
                ["$\\int_0^{x^2}$ türevinde zinciri unutmak", "$f(x^2) \\cdot 2x$"],
            ]),
            "Bu hataların çoğu dikkat eksikliğinden doğar. Hesaptan sonra sonucun işaretini grafikle karşılaştırmak iyi bir denetimdir: fonksiyon aralıkta pozitifse integral de pozitif olmalıdır.",
        ]},
    ],
    "sss": [
        ("Belirli integral nedir?",
         "Bir fonksiyonun iki sınır arasındaki integralidir ve tek bir sayı verir. Fonksiyon pozitifken eğrinin altındaki alana eşittir."),
        ("Belirli integral nasıl hesaplanır?",
         "Ters türev bulunur, üst sınırdaki değerinden alt sınırdaki değeri çıkarılır. Bu, analizin temel teoremidir."),
        ("Belirli integralde C neden yazılmaz?",
         "Üst ve alt sınırdaki değerler çıkarılırken integral sabiti sadeleşir."),
        ("Tek fonksiyonun simetrik aralıkta integrali kaçtır?",
         "Sıfırdır. Orijine göre simetrik grafikte pozitif ve negatif alanlar birbirini götürür."),
        ("Mutlak değerli belirli integral nasıl alınır?",
         "İçteki ifadenin işaret değiştirdiği nokta bulunur, aralık bölünür ve her parçada mutlak değer uygun işaretle açılır."),
        ("Üst sınırı x olan integralin türevi nedir?",
         "İntegrali alınan fonksiyonun x teki değeridir. Üst sınır x yerine bir fonksiyonsa zincir kuralı gereği o fonksiyonun türeviyle çarpılır."),
        ("Belirli integral ile alan aynı şey midir?",
         "Fonksiyon aralıkta pozitifse aynıdır. Fonksiyon yatay eksenin altına iniyorsa belirli integral o bölgeyi negatif sayar; gerçek alan için parçalar ayrı alınır."),
        ("Belirli integralde sınırlar yer değiştirirse ne olur?",
         "Sonucun işareti değişir: b den a ya integral, a dan b ye integralin ters işaretlisidir."),
        ("Parçalı fonksiyonun belirli integrali nasıl alınır?",
         "Aralık, kuralın değiştiği noktalardan bölünür; her parçada o parçanın kuralıyla integral alınır ve sonuçlar toplanır."),
    ],
    "kontrol": [
        "Belirli integralin dikdörtgen toplamlarının limiti olduğunu açıklayabiliyorum.",
        "Temel teoremle belirli integral hesaplayabiliyorum.",
        "Polinom, kök, üstel, logaritmik ve trigonometrik integralleri hesaplayabiliyorum.",
        "Belirli integralin özelliklerini kullanabiliyorum.",
        "Parçalı ve mutlak değerli fonksiyonların integralini alabiliyorum.",
        "Tek ve çift fonksiyonlarda simetriyi kullanabiliyorum.",
        "İşaretli alan ile gerçek alanı ayırt edebiliyorum.",
        "Sınırlarla değişken değiştirebiliyorum.",
        "Üst sınırı değişken integralin türevini bulabiliyorum.",
        "Yer değiştirme, toplam yol ve enerji problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["belirsiz-integral", "integral-alan-hesaplama", "degisken-degistirme"],
}
