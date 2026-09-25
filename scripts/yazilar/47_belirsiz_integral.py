# scripts/yazilar/47_belirsiz_integral.py — Belirsiz Integral Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "belirsiz-integral",
    "baslik": "Belirsiz İntegral Konu Anlatımı",
    "aciklama": "Belirsiz integral nedir? Ters türev, integral sabiti, temel kurallar, açarak ve ayırarak integral, trigonometrik ve üstel integraller, başlangıç değeri.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "belirsiz-integral",
    "kapak_alt": "Belirsiz integral: aynı biçimdeki mavi eğrilerin farklı yüksekliklerde çizildiği şeffaf levhaları dizen öğrenci",
    "ozet": "Belirsiz integral, türevi verilen bir fonksiyonun bütün ters türevlerinin ailesidir ve bir integral sabitiyle yazılır. Türev kurallarının tersten okunmasıyla hesaplanır ve sonucun türevi alınarak her zaman denetlenebilir. Bu yazıda ters türev kavramını, integral sabitinin geometrik anlamını, temel integral kurallarını, kuvvet kuralını kök ve kesirlerle kullanmayı, açarak ve terimlere ayırarak integral almayı, üstel ve trigonometrik integralleri, özdeşliklerle integrali, başlangıç değer problemlerini, ikinci türevden fonksiyon bulmayı ve hareket ile maliyet uygulamalarını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Belirsiz integral nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için türev kurallarını ve integralin temel fikrini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/integral-konu-anlatimi/\">İntegral Konu Anlatımı</a> ve <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> yazılarına göz at."),
            "Türevi $f$ olan her $F$ fonksiyonuna $f$ nin ters türevi denir. Bir fonksiyonun bütün ters türevlerinin oluşturduğu aileye <strong>belirsiz integral</strong> denir ve $\\int f(x)\\,dx=F(x)+C$ biçiminde yazılır. Belirsiz denmesinin nedeni, sonucun tek bir fonksiyon değil, bir sabit kadar farklı fonksiyonlardan oluşan bir aile olmasıdır.",
            "Kapaktaki öğrenci aynı biçimdeki mavi eğrilerin farklı yüksekliklerde çizildiği şeffaf levhaları yan yana diziyor. Levhalardaki eğrilerin hepsi aynı eğime sahip; yalnızca yükseklikleri farklı. Belirsiz integral de tam olarak bu eğri ailesini verir.",
        ]},
        {"baslik": "Ters türev ve türevin ilişkisi", "icerik": [
            "Belirsiz integral, türev işleminin tersidir. Bir fonksiyonun integrali alınıp sonra türevi alınırsa fonksiyonun kendisi geri gelir: $\\dfrac{d}{dx}\\int f(x)\\,dx=f(x)$. Tersine, bir fonksiyonun türevi alınıp sonra integrali alınırsa fonksiyon bir sabit farkıyla geri gelir: $\\int f'(x)\\,dx=f(x)+C$.",
            "Bu iki eşitlik, belirsiz integrali hesaplamanın ve denetlemenin anahtarıdır. Her integral kuralı bir türev kuralından gelir ve her integral sonucu türev alınarak doğrulanır.",
            hap("İntegralin sonucu, türevi alınınca integrali alınan fonksiyonu vermelidir.",
                "Bu denetim her soruda birkaç saniyede yapılabilir."),
        ]},
        {"baslik": "İntegral sabiti", "icerik": [
            "Bir sabitin türevi sıfır olduğu için $x^2$, $x^2+1$ ve $x^2-7$ fonksiyonlarının türevleri aynıdır: $2x$. Bu yüzden $2x$ in ters türevi tek değildir; hepsi $x^2+C$ biçimindedir. $C$ ye <strong>integral sabiti</strong> denir.",
            koordinat_grafik("2x in ters türevlerinden üçü: y = x² + 2, y = x² ve y = x² - 2", [("", lambda x: x * x + 2), ("", lambda x: x * x), ("", lambda x: x * x - 2)],
                             (-3, 3), (-3, 7), adim=1, noktalar=[(0, 2, "", True), (0, 0, "", True), (0, -2, "", True)]),
            "Grafikteki üç eğri yukarıdan aşağıya $y=x^2+2$, $y=x^2$ ve $y=x^2-2$ dir; birbirinin dikey kaydırılmış kopyasıdırlar ve aynı apsiste eğimleri eşittir. Kapaktaki şeffaf levhalar bu eğri ailesinin fiziksel bir modelidir. Bir koşul verilmedikçe aileden hangi eğrinin istendiği bilinemez; bu yüzden sonuca her zaman $+C$ eklenir.",
            hap("Belirsiz integralde $+C$ yazılır; çünkü yalnız sabit terimleri farklı fonksiyonların türevleri aynıdır."),
        ]},
        {"baslik": "İntegral neden türevden zordur?", "icerik": [
            "Türev almak mekanik bir işlemdir: toplam, çarpım, bölüm ve zincir kurallarıyla her temel fonksiyonun türevi bulunur. İntegralde ise çarpım ve bölüm için genel bir kural yoktur. Bu yüzden integral almak, çoğu zaman fonksiyonu tanıdık bir biçime getirmeyi gerektirir.",
            "Hatta bazı fonksiyonların ters türevi temel fonksiyonlarla hiç yazılamaz; $e^{x^2}$ bunun ünlü bir örneğidir. Lise matematiğinde karşılaşılan integraller ise hep tablodaki kurallara, açmaya, ayırmaya, özdeşliklere ya da değişken değiştirmeye indirgenebilecek biçimde seçilir.",
        ]},
        {"baslik": "Temel integral kuralları", "icerik": [
            "Temel türev tablosu sağdan sola, yani tersten okunarak temel integral tablosu elde edilir. Her satırın doğruluğu sağ tarafın türevi alınarak görülür:",
            tablo(["İntegral", "Sonuç"], [
                ["$\\int k\\,dx$", "$kx+C$"],
                ["$\\int x^n\\,dx$", "$\\dfrac{x^{n+1}}{n+1}+C$, $n \\neq -1$"],
                ["$\\int \\dfrac{1}{x}\\,dx$", "$\\ln|x|+C$"],
                ["$\\int e^x\\,dx$", "$e^x+C$"],
                ["$\\int a^x\\,dx$", "$\\dfrac{a^x}{\\ln a}+C$"],
                ["$\\int \\sin x\\,dx$", "$-\\cos x+C$"],
                ["$\\int \\cos x\\,dx$", "$\\sin x+C$"],
                ["$\\int \\dfrac{1}{\\cos^2 x}\\,dx$", "$\\tan x+C$"],
            ]),
            "Tablodaki $\\ln|x|$ yazımındaki mutlak değer, negatif $x$ ler için de sonucun tanımlı olmasını sağlar; türevi her iki durumda da $\\dfrac{1}{x}$ dir.",
        ]},
        {"baslik": "Kuvvet kuralı", "icerik": [
            "Kuvvet kuralında üs bir artırılır ve yeni üsse bölünür. Kural, türevdeki kuvvet kuralının tam tersidir: türevde üs öne iner ve bir azalır, integralde bir artar ve paydaya gider. Sonucun türevi alınınca paydadaki sayı öne inen üsle sadeleşir ve başlangıçtaki fonksiyon geri gelir.",
            ornek(
                "$\\int x^5\\,dx$ ve $\\int 5\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "$\\int x^5\\,dx=\\dfrac{x^6}{6}+C$ olur.",
                "$\\int 5\\,dx=5x+C$ olur; sabitin integrali, sabit ile değişkenin çarpımıdır."),
        ]},
        {"baslik": "Kök ve kesirlerle kuvvet kuralı", "icerik": [
            "Kök ve paydada $x$ içeren terimler önce üslü biçime çevrilir: $\\sqrt{x}=x^{1/2}$, $\\dfrac{1}{x^3}=x^{-3}$. Sonra kuvvet kuralı uygulanır ve sonuç isteniyorsa yeniden kök ya da kesir olarak yazılır.",
            ornek(
                "$\\int \\sqrt{x}\\,dx$ ve $\\int \\dfrac{1}{x^3}\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "$\\int x^{1/2}\\,dx=\\dfrac{x^{3/2}}{3/2}=\\dfrac{2}{3}x\\sqrt{x}+C$ olur.",
                "$\\int x^{-3}\\,dx=\\dfrac{x^{-2}}{-2}=-\\dfrac{1}{2x^2}+C$ olur."),
            "Negatif üslerde kural yalnızca üs $-1$ olduğunda işlemez; o durumda sonuç doğal logaritmadır. $x^{-3}$ gibi diğer negatif üslerde kural sorunsuz uygulanır.",
        ]},
        {"baslik": "Toplam ve sabitle çarpım", "icerik": [
            "Toplamın integrali integrallerin toplamıdır ve sabit çarpan integralin dışına çıkar. Bu yüzden polinomların integrali terim terim alınır ve her terime kuvvet kuralı uygulanır. Terimlerin integral sabitleri tek bir $C$ de toplanır.",
            ornek(
                "$\\int (4x^3-6x+2)\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "Terim terim: $4 \\cdot \\dfrac{x^4}{4}-6 \\cdot \\dfrac{x^2}{2}+2x$ olur.",
                "Sonuç $x^4-3x^2+2x+C$ dir; türevi $4x^3-6x+2$ verir."),
        ]},
        {"baslik": "Açarak integral almak", "icerik": [
            "Çarpımın integrali için çarpım kuralına benzer basit bir kural yoktur. Bu yüzden çarpım biçimindeki polinomlar önce açılır, sonra terim terim integral alınır. Açılım uzunsa ve çarpanlardan biri diğerinin türeviyse değişken değiştirme daha kısa yoldur.",
            ornek(
                "$\\int (x+1)^2\\,dx$ ve $\\int (x+2)(x-3)\\,dx$ integralleri verilsin.",
                "İntegralleri açarak hesaplayalım.",
                "$(x+1)^2=x^2+2x+1$ olduğundan birincisi $\\dfrac{x^3}{3}+x^2+x+C$ olur.",
                "$(x+2)(x-3)=x^2-x-6$ olduğundan ikincisi $\\dfrac{x^3}{3}-\\dfrac{x^2}{2}-6x+C$ olur."),
            dikkat(
                "Çarpımın integralini integrallerin çarpımı olarak almak.",
                "$\\int x \\cdot x\\,dx=\\dfrac{x^3}{3}+C$ dir; oysa $\\int x\\,dx \\cdot \\int x\\,dx$ hesabı $\\dfrac{x^4}{4}$ verir. Çarpım önce açılmalıdır."),
        ]},
        {"baslik": "Terimlere ayırarak integral almak", "icerik": [
            "Paydası tek terimli kesirler terimlere ayrılır; payın her terimi paydaya ayrı ayrı bölünür, sadeleştirilir ve integrali alınır. Payda $x$ olduğunda terimlerden biri $\\dfrac{1}{x}$ e dönüşebilir ve doğal logaritma ortaya çıkar.",
            ornek(
                "$\\int \\dfrac{x^2+1}{x}\\,dx$ ve $\\int \\dfrac{x+1}{\\sqrt{x}}\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "Birincisi $\\int \\left(x+\\dfrac{1}{x}\\right)dx=\\dfrac{x^2}{2}+\\ln|x|+C$ olur.",
                "İkincisi $\\int (x^{1/2}+x^{-1/2})\\,dx=\\dfrac{2}{3}x^{3/2}+2\\sqrt{x}+C$ olur."),
        ]},
        {"baslik": "Üstel integraller", "icerik": [
            "$e^x$ in integrali, türevinde olduğu gibi kendisidir. Tabanı başka bir sayı olan üstel fonksiyonlarda ise türevde çarpan olarak gelen doğal logaritma, integralde bölen olarak gelir. Üssünde katsayı bulunan fonksiyonlarda da katsayı bölen olur.",
            ornek(
                "$\\int 2^x\\,dx$ ve $\\int e^{3x}\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "$\\int 2^x\\,dx=\\dfrac{2^x}{\\ln 2}+C$ olur.",
                "$\\int e^{3x}\\,dx=\\dfrac{e^{3x}}{3}+C$ olur; türevi $e^{3x}$ verir."),
        ]},
        {"baslik": "Trigonometrik integraller", "icerik": [
            "Sinüsün integrali eksi kosinüs, kosinüsün integrali ise sinüstür. İşaret, türev tablosundaki işaretin tersinden gelir ve en sık hata yapılan yer burasıdır.",
            ornek(
                "$\\int (3\\cos x-2\\sin x)\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$3\\int \\cos x\\,dx=3\\sin x$ ve $-2\\int \\sin x\\,dx=2\\cos x$ olur.",
                "Sonuç $3\\sin x+2\\cos x+C$ dir."),
            "İçinde katsayılı açı bulunan trigonometrik fonksiyonlarda katsayı bölen olarak gelir: $\\int \\cos 2x\\,dx=\\dfrac{\\sin 2x}{2}+C$ ve $\\int \\sin 3x\\,dx=-\\dfrac{\\cos 3x}{3}+C$ dir.",
            hap("$\\int \\sin x\\,dx=-\\cos x+C$ ve $\\int \\cos x\\,dx=\\sin x+C$ olur."),
        ]},
        {"baslik": "Özdeşliklerle integral", "icerik": [
            "Doğrudan tabloda bulunmayan trigonometrik integraller, trigonometrik özdeşliklerle tablodaki biçimlere çevrilir. $1+\\tan^2 x=\\dfrac{1}{\\cos^2 x}$ özdeşliği ve kuvvet azaltma formülleri en sık kullanılanlardır.",
            ornek(
                "$\\int \\tan^2 x\\,dx$ ve $\\int \\sin^2 x\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "$\\tan^2 x=\\dfrac{1}{\\cos^2 x}-1$ olduğundan birincisi $\\tan x-x+C$ olur.",
                "$\\sin^2 x=\\dfrac{1-\\cos 2x}{2}$ olduğundan ikincisi $\\dfrac{x}{2}-\\dfrac{\\sin 2x}{4}+C$ olur."),
            "Kuvvet azaltma formülü için <a href=\"/blog/iki-kat-yarim-aci/\">İki Kat Açı ve Yarım Açı Formülleri</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Doğrusal iç fonksiyon", "icerik": [
            "İçteki ifade $ax+b$ biçiminde doğrusal olduğunda integral kolayca ve tek adımda alınır: dıştaki fonksiyonun integrali yazılır ve $a$ ya bölünür. Bu, zincir kuralının tersidir; türevde gelen $a$ çarpanı integralde bölen olur.",
            ornek(
                "$\\int (2x+1)^3\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "Dış fonksiyonun integrali $\\dfrac{(2x+1)^4}{4}$ tür; iç fonksiyonun katsayısı $2$ ye bölünür.",
                "Sonuç $\\dfrac{(2x+1)^4}{8}+C$ dir; türevi $\\dfrac{4(2x+1)^3 \\cdot 2}{8}=(2x+1)^3$ verir."),
            "İç fonksiyon doğrusal değilse bu kısa yol işlemez; o zaman değişken değiştirme yöntemi kullanılır. Ayrıntılar <a href=\"/blog/degisken-degistirme/\">İntegralde Değişken Değiştirme Yöntemi</a> yazısında.",
            hap("İçteki ifade $ax+b$ biçimindeyse dıştaki fonksiyonun integrali yazılır ve $a$ ya bölünür."),
        ]},
        {"baslik": "Paydada doğrusal ifade", "icerik": [
            "Paydası doğrusal bir ifade olan kesirlerin integrali doğal logaritma verir. Paydadaki $x$ in katsayısı, doğrusal iç fonksiyon kuralı gereği bölen olarak gelir.",
            ornek(
                "$\\int \\dfrac{1}{2x+3}\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$\\int \\dfrac{1}{u}\\,du=\\ln|u|$ kalıbı kullanılır ve iç fonksiyonun katsayısı $2$ ye bölünür.",
                "Sonuç $\\dfrac{1}{2}\\ln|2x+3|+C$ dir."),
        ]},
        {"baslik": "Kosinüs karesi ve karelerin toplamı", "icerik": [
            "Sinüs karesinde olduğu gibi kosinüs karesinin integrali de kuvvet azaltma formülüyle alınır: $\\cos^2 x=\\dfrac{1+\\cos 2x}{2}$. İki sonucu toplamak, bulunan formülleri denetlemenin güzel bir yoludur.",
            ornek(
                "$\\int \\cos^2 x\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım ve sinüs karesinin integraliyle toplayalım.",
                "$\\int \\dfrac{1+\\cos 2x}{2}\\,dx=\\dfrac{x}{2}+\\dfrac{\\sin 2x}{4}+C$ olur.",
                "Sinüs karesinin integraliyle toplanınca $x+C$ kalır; bu, $\\sin^2 x+\\cos^2 x=1$ in integralidir."),
        ]},
        {"baslik": "Mutlak değerli integral", "icerik": [
            "Mutlak değerli fonksiyonların integrali, içteki ifadenin işaretine göre parçalara ayrılarak alınır. $|x|$ için tek bir formül de yazılabilir: $\\int |x|\\,dx=\\dfrac{x|x|}{2}+C$.",
            "Bu formülün doğruluğu türevle görülür: $x>0$ için ifade $\\dfrac{x^2}{2}$ dir ve türevi $x$ tir; $x<0$ için ifade $-\\dfrac{x^2}{2}$ dir ve türevi $-x$ tir. İki durumda da türev $|x|$ e eşittir.",
        ]},
        {"baslik": "Logaritmik türevin tersi", "icerik": [
            "Payı, paydasının türevine eşit olan kesirlerin integrali paydanın doğal logaritmasıdır: $\\int \\dfrac{f'(x)}{f(x)}\\,dx=\\ln|f(x)|+C$. Bu kalıp, logaritmik türevin tersten okunmasıdır.",
            ornek(
                "$\\int \\dfrac{2x}{x^2+1}\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "Pay, paydanın türevidir: $(x^2+1)'=2x$.",
                "Sonuç $\\ln(x^2+1)+C$ dir; payda her zaman pozitif olduğu için mutlak değere gerek yoktur."),
        ]},
        {"baslik": "Başlangıç değer problemi", "icerik": [
            "Türevi ve bir noktadaki değeri verilen fonksiyon tek olarak belirlenir; çünkü verilen nokta ailenin yalnızca bir üyesinden geçer. Önce belirsiz integral alınır, sonra verilen noktadaki değer yerine yazılarak integral sabiti bulunur.",
            ornek(
                "$F'(x)=3x^2-2$ ve $F(1)=4$ olsun.",
                "$F(x)$ fonksiyonunu bulalım.",
                "$F(x)=x^3-2x+C$ olur; $F(1)=1-2+C=4$ ise $C=5$.",
                "$F(x)=x^3-2x+5$ bulunur."),
        ]},
        {"baslik": "Eğimi verilen eğri", "icerik": [
            "Bir eğrinin her noktasındaki teğet eğimi bir fonksiyon olarak verilmişse, eğim fonksiyonunun integrali eğrinin denklemini bir sabit farkıyla verir. Eğrinin geçtiği bir nokta bilinirse sabit bulunur.",
            ornek(
                "Bir eğrinin her $x$ teki teğet eğimi $2x-3$ ve eğri $(2, 1)$ noktasından geçiyor.",
                "Eğrinin denklemini bulalım.",
                "$y=\\int (2x-3)\\,dx=x^2-3x+C$ olur; $(2, 1)$ yazılınca $1=4-6+C$, yani $C=3$.",
                "Eğri $y=x^2-3x+3$ tür."),
        ]},
        {"baslik": "İkinci türevden fonksiyon", "icerik": [
            "İkinci türev verildiğinde integral art arda iki kez alınır ve iki ayrı sabit ortaya çıkar. İki sabitin bulunması için iki koşul gerekir; genellikle bir noktadaki fonksiyon değeri ve türev değeri verilir.",
            ornek(
                "$f''(x)=6x$, $f'(0)=1$ ve $f(0)=2$ olsun.",
                "$f(x)$ fonksiyonunu bulalım.",
                "$f'(x)=3x^2+C_1$ ve $f'(0)=1$ olduğundan $C_1=1$ olur.",
                "$f(x)=x^3+x+C_2$ ve $f(0)=2$ olduğundan $f(x)=x^3+x+2$ bulunur."),
        ]},
        {"baslik": "Uygulama: ivmeden konuma", "icerik": [
            "Fizikte ivmenin integrali hızı, hızın integrali de konumu verir; türevdeki sıra tersine işler. İki integralin sabitleri başlangıç hızı ve başlangıç konumudur.",
            ornek(
                "Bir cismin ivmesi $a(t)=6t$, başlangıç hızı $2$ ve başlangıç konumu $0$ olsun.",
                "Konum fonksiyonunu ve $t=2$ deki konumu bulalım.",
                "$v(t)=3t^2+2$ ve $s(t)=t^3+2t$ olur.",
                "$s(2)=8+4=12$ birim bulunur."),
            "Sabit ivmeli harekette aynı yol, fizikten bilinen $s=v_0 t+\\dfrac{1}{2}at^2$ formülünü verir; bu formül aslında iki kez integral almanın sonucudur.",
            hap("Duraktan kalkan bir metro sabit $2$ metre bölü saniye kare ivmeyle hızlanırsa hızı $v(t)=2t$, aldığı yol $s(t)=t^2$ metre olur.", "Metro kalkıştan $10$ saniye sonra $100$ metre ilerlemiş olur.", gunluk=True),
        ]},
        {"baslik": "Uygulama: marjinal maliyetten maliyet", "icerik": [
            "Ekonomide marjinal maliyet, toplam maliyetin üretim miktarına göre türevidir. Marjinal maliyet ve sabit maliyet biliniyorsa toplam maliyet integralle bulunur; integral sabiti hiç üretim yapılmadığındaki sabit maliyettir.",
            ornek(
                "Marjinal maliyet $C'(x)=5+0.02x$ TL ve sabit maliyet $100$ TL olsun.",
                "Toplam maliyet fonksiyonunu bulalım.",
                "$C(x)=5x+0.01x^2+K$ olur; $C(0)=100$ olduğundan $K=100$.",
                "$C(x)=100+5x+0.01x^2$ bulunur."),
        ]},
        {"baslik": "Katsayı bulma soruları", "icerik": [
            "Bazı sorularda integralin sonucu verilir ve integrali alınan fonksiyondaki bilinmeyen bir katsayı istenir. Bu durumda sonucun türevi alınıp katsayılar karşılaştırılır.",
            ornek(
                "$\\int (ax+2)\\,dx=3x^2+2x+C$ olsun.",
                "$a$ yı bulalım.",
                "Sağ tarafın türevi $6x+2$ dir; bu, integrali alınan fonksiyona eşit olmalıdır.",
                "$ax+2=6x+2$ olduğundan $a=6$ bulunur."),
        ]},
        {"baslik": "Grafikle ters türev", "icerik": [
            "Bir fonksiyonun grafiği verilmişse ters türevinin davranışı yorumlanabilir. Fonksiyon pozitif olduğu aralıklarda ters türev artar, negatif olduğu aralıklarda azalır; fonksiyonun işaret değiştirdiği noktalar ters türevin tepe ve çukur noktalarıdır.",
            "Örneğin $f(x)=2x$ negatif $x$ ler için negatif, pozitif $x$ ler için pozitiftir. Bu yüzden ters türevi olan $x^2+C$ eğrileri sıfıra kadar azalır, sonra artar ve hepsinin en küçük değeri $x=0$ dadır. Bu yorum, türev ile fonksiyon arasındaki ilişkinin integral yönünden okunmasıdır.",
        ]},
        {"baslik": "Kuralların özeti", "icerik": [
            tablo(["Durum", "Yöntem"], [
                ["Polinom", "Terim terim kuvvet kuralı"],
                ["Kök ya da $\\dfrac{1}{x^n}$", "Üslü yazıp kuvvet kuralı"],
                ["Açılabilen çarpım", "Açıp terim terim"],
                ["Paydası tek terimli kesir", "Terimlere ayır"],
                ["İçi doğrusal bileşke", "İntegral al, katsayıya böl"],
                ["$\\dfrac{f'}{f}$ biçimi", "$\\ln|f|+C$"],
                ["$\\tan^2 x$, $\\sin^2 x$", "Özdeşlikle dönüştür"],
            ]),
            "Hiçbiri uymuyorsa değişken değiştirme yöntemi denenir. Hangi yol seçilirse seçilsin sonuç, türev alınarak denetlenmelidir.",
        ]},
        {"baslik": "Sınavda belirsiz integral", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) belirsiz integral; temel kurallar, başlangıç değer problemleri, eğimi verilen eğri, ikinci türevden fonksiyon ve basit trigonometrik ve üstel integraller biçiminde karşına çıkabilir.",
                "Belirsiz integral, belirli integral ve alan sorularının ilk adımıdır."),
            "Seçenekli sorularda integrali hesaplamak yerine seçeneklerin türevini almak çoğu zaman daha hızlıdır. Türevi integrali alınan fonksiyonu veren seçenek doğru cevaptır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$+C$ yi unutmak", "Belirsiz integralde $C$ yazılır"],
                ["$\\int x^n\\,dx=x^{n+1}$", "$\\dfrac{x^{n+1}}{n+1}+C$"],
                ["$\\int \\dfrac{1}{x}\\,dx$ e kuvvet kuralı", "$\\ln|x|+C$"],
                ["$\\int \\sin x\\,dx=\\cos x$", "$-\\cos x+C$"],
                ["$\\int e^{3x}\\,dx=e^{3x}$", "$\\dfrac{e^{3x}}{3}+C$"],
                ["Çarpımın integralini çarpım sanmak", "Önce açılır"],
            ]),
            "Bu hataların hepsi türev denetimiyle yakalanır. Sonucun türevini almak, integral sorularında en güvenilir kontroldür.",
        ]},
    ],
    "sss": [
        ("Belirsiz integral nedir?",
         "Bir fonksiyonun bütün ters türevlerinin ailesidir ve integral sabiti C ile yazılır."),
        ("İntegral sabiti C neden eklenir?",
         "Sabitin türevi sıfır olduğu için türevi aynı olan sonsuz sayıda fonksiyon vardır. C bu fonksiyonların hepsini temsil eder."),
        ("x üzeri n in integrali nedir?",
         "n eksi 1 den farklıysa x üzeri n artı 1 bölü n artı 1 artı C dir. n eşittir eksi 1 ise sonuç ln mutlak x artı C dir."),
        ("Sinüsün integrali nedir?",
         "Eksi kosinüs artı C dir. Kosinüsün integrali ise sinüs artı C dir."),
        ("e üzeri 3x in integrali nedir?",
         "e üzeri 3x bölü 3 artı C dir; üsteki katsayı bölen olarak gelir."),
        ("İntegral sonucu nasıl denetlenir?",
         "Sonucun türevi alınır. Türev, integrali alınan fonksiyona eşitse sonuç doğrudur."),
        ("Çarpımın integrali nasıl alınır?",
         "Çarpım için genel bir integral kuralı yoktur. Polinom çarpımları açılır; diğer durumlarda değişken değiştirme gibi yöntemler kullanılır."),
        ("Başlangıç değer problemi nedir?",
         "Türevi ve bir noktadaki değeri verilen fonksiyonu bulma problemidir. Belirsiz integral alınır ve verilen değerle integral sabiti bulunur."),
        ("tan kare x in integrali nedir?",
         "tan kare x, 1 bölü cos kare x eksi 1 olarak yazılır. İntegrali tan x eksi x artı C dir."),
        ("1 bölü x in integrali nedir?",
         "ln mutlak x artı C dir. Kuvvet kuralı bu durumda sıfıra bölme gerektirdiği için ayrı bir kural kullanılır."),
    ],
    "kontrol": [
        "Ters türev ve belirsiz integral kavramlarını açıklayabiliyorum.",
        "İntegral sabitinin geometrik anlamını açıklayabiliyorum.",
        "Temel integral tablosunu kullanabiliyorum.",
        "Kuvvet kuralını kök ve kesirlerle uygulayabiliyorum.",
        "Açarak ve terimlere ayırarak integral alabiliyorum.",
        "Üstel ve trigonometrik integralleri hesaplayabiliyorum.",
        "Özdeşliklerle trigonometrik integralleri dönüştürebiliyorum.",
        "İçi doğrusal bileşkelerin ve f üssü bölü f kalıbının integralini alabiliyorum.",
        "Başlangıç değer problemlerini ve eğimi verilen eğri sorularını çözebiliyorum.",
        "İkinci türevden fonksiyonu ve ivmeden konumu bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["integral-konu-anlatimi", "degisken-degistirme", "belirli-integral"],
}
