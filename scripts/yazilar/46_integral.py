# scripts/yazilar/46_integral.py — Integral Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402


def _sag_basamak(x):
    """[0, 2] araliginda 4 esit dikdortgenin sag uc yuksekligi (x^2 icin)."""
    if x < 0 or x >= 2:
        return None
    k = math.floor(x / 0.5) + 1
    return (k * 0.5) ** 2


YAZI = {
    "slug": "integral-konu-anlatimi",
    "baslik": "İntegral Konu Anlatımı",
    "aciklama": "İntegral nedir? Ters türev, belirsiz integral, dikdörtgenlerle alan, belirli integral, temel teorem, işaretli alan ve uygulamalar; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "integral-konu-anlatimi",
    "kapak_alt": "İntegral konu anlatımı: eğrinin altına ince mavi çubukları yan yana dizerek alanı dolduran iki öğrenci",
    "ozet": "İntegral, iki temel sorunun cevabıdır: türevi bilinen bir fonksiyonun kendisini bulmak ve bir eğrinin altında kalan alanı hesaplamak. Analizin temel teoremi bu iki sorunun aynı işlemle çözüldüğünü gösterir. Bu yazıda ters türev ve belirsiz integral kavramını, temel integral kurallarını, integral sabitinin anlamını, alanın dikdörtgenlerle yaklaşık hesaplanmasını, belirli integrali ve temel teoremi, işaretli alanı, belirli integralin özelliklerini, değişken değiştirmeye ve alan hesabına girişi, ortalama değeri ve hızdan yol, akıştan miktar gibi uygulamaları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "İntegral nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için türev kurallarını ve limit kavramını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> ve <a href=\"/blog/limit-konu-anlatimi/\">Limit Konu Anlatımı</a> yazılarına göz at."),
            "Türev bir fonksiyonun bir noktada ne kadar hızlı değiştiğini söyler. İntegral ise bunun tersini yapar: değişim hızı bilinen bir niceliğin toplam değişimini bulur. Hızdan alınan yol, akış hızından biriken su, üretim hızından toplam üretim hep integral sorularıdır.",
            "Kapaktaki öğrenciler bir eğrinin altına ince çubukları yan yana diziyor; her çubuğun yüksekliği eğrinin o noktadaki değerine eşit. Çubuklar inceldikçe eğrinin altındaki alan daha iyi doluyor. İntegral, sonsuz sayıda sonsuz ince çubuğun toplamıdır ve bu yazı bu fikri adım adım kuruyor.",
        ]},
        {"baslik": "İki soru, tek cevap", "icerik": [
            "İntegral konusu ilk bakışta birbirinden çok farklı iki soruyla başlar. Birincisi cebirseldir: türevi verilen bir fonksiyonun kendisi nedir? İkincisi geometriktir: bir eğrinin altında kalan bölgenin alanı nedir?",
            "Analizin temel teoremi bu iki sorunun aynı araçla çözüldüğünü gösterir. Alanı hesaplamak için türevi o fonksiyon olan başka bir fonksiyon bulunur ve iki uçtaki değerleri çıkarılır. Bu keşif, türev ile integrali birbirinin tersi olan iki işlem hâline getirir.",
            hap("İntegral, türevin tersidir ve alanı hesaplar.",
                "Temel teorem bu iki anlamı birbirine bağlar."),
        ]},
        {"baslik": "Ters türev", "icerik": [
            "Türevi $f$ olan bir $F$ fonksiyonuna $f$ nin <strong>ters türevi</strong> denir: $F'(x)=f(x)$. Ters türev bulmak, türev kurallarını tersten okumaktır.",
            ornek(
                "$f(x)=x^2$ fonksiyonu verilsin.",
                "Bir ters türevini bulalım.",
                "Türevi $x^2$ olan fonksiyon aranır; $x^3$ ün türevi $3x^2$ olduğundan $\\dfrac{x^3}{3}$ ün türevi $x^2$ dir.",
                "$F(x)=\\dfrac{x^3}{3}$ bir ters türevdir; $\\dfrac{x^3}{3}+5$ de bir ters türevdir."),
            "Bir fonksiyonun tek bir ters türevi yoktur: bir ters türeve herhangi bir sabit eklenirse türev değişmez. Bu yüzden ters türevler bir sabit farkıyla belirlenir.",
        ]},
        {"baslik": "Belirsiz integral", "icerik": [
            "Bir fonksiyonun bütün ters türevlerinin ailesine belirsiz integral denir. Aile, integral sabitiyle tek bir ifadede toplanır ve şöyle yazılır:",
            "$$\\int f(x)\\,dx=F(x)+C$$",
            "Buradaki $\\int$ işareti integral işareti, $f(x)$ integrali alınan fonksiyon, $dx$ ise değişkenin $x$ olduğunu gösteren ektir. $C$ ye integral sabiti denir ve herhangi bir gerçek sayı olabilir. Belirsiz integralin ayrıntıları için <a href=\"/blog/belirsiz-integral/\">Belirsiz İntegral Konu Anlatımı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Temel integral kuralları", "icerik": [
            "Temel integral kuralları, temel türev kurallarının tersten yazılmasından ibarettir. Her kural, sağ tarafın türevi alınarak doğrulanabilir:",
            tablo(["İntegral", "Sonuç"], [
                ["$\\int x^n\\,dx$", "$\\dfrac{x^{n+1}}{n+1}+C$, $n \\neq -1$"],
                ["$\\int \\dfrac{1}{x}\\,dx$", "$\\ln|x|+C$"],
                ["$\\int e^x\\,dx$", "$e^x+C$"],
                ["$\\int \\sin x\\,dx$", "$-\\cos x+C$"],
                ["$\\int \\cos x\\,dx$", "$\\sin x+C$"],
            ]),
            "Kuvvet kuralında üs bir artırılır ve yeni üsse bölünür. Üs $-1$ olduğunda bu kural sıfıra bölmeye yol açacağı için $\\dfrac{1}{x}$ in integrali ayrı bir kuralla, doğal logaritmayla verilir.",
        ]},
        {"baslik": "Sonucu türevle denetlemek", "icerik": [
            "İntegral almak türev almaktan daha zordur; çünkü her fonksiyonun ters türevi kolayca yazılamaz. Buna karşın bulunan sonucun doğruluğu her zaman kolayca denetlenir: sonucun türevi alınır ve integrali alınan fonksiyonla karşılaştırılır.",
            "Örneğin $\\int \\cos x\\,dx=\\sin x+C$ sonucunun türevi $\\cos x$ tir ve doğrudur. $\\int \\sin x\\,dx$ için $\\cos x$ yazılırsa türevi $-\\sin x$ çıkar ve işaretin yanlış olduğu hemen görülür. Bu yüzden sinüsün integrali $-\\cos x+C$ dir.",
        ]},
        {"baslik": "Toplam ve sabitle çarpım", "icerik": [
            "Türevde olduğu gibi integralde de toplamın integrali integrallerin toplamıdır ve sabit çarpan integralin dışına çıkar. Bu yüzden polinomların integrali terim terim alınır.",
            ornek(
                "$\\int (3x^2+2x)\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "Terim terim: $3 \\cdot \\dfrac{x^3}{3}+2 \\cdot \\dfrac{x^2}{2}$ olur.",
                "Sonuç $x^3+x^2+C$ dir; türevi alınınca $3x^2+2x$ geri gelir."),
            "Sonucun türevini alıp integrali alınan fonksiyona ulaşmak, integral hesabını denetlemenin en güvenilir yoludur.",
        ]},
        {"baslik": "İntegral sabitinin anlamı", "icerik": [
            "İntegral sabiti, ters türevler ailesinden hangisinin istendiğini belirler. Bir noktadaki değer verilirse sabit bulunur ve ailenin tek bir üyesi seçilir. Bu tür sorulara başlangıç değer problemi denir.",
            ornek(
                "$F'(x)=2x$ ve $F(1)=4$ olsun.",
                "$F$ fonksiyonunu bulalım.",
                "$F(x)=x^2+C$ olur; $F(1)=1+C=4$ ise $C=3$.",
                "$F(x)=x^2+3$ bulunur."),
            "Geometrik olarak ters türevlerin grafikleri birbirinin dikey kaydırılmış kopyalarıdır. Verilen nokta, bu kopyalardan hangisinin o noktadan geçtiğini seçer.",
        ]},
        {"baslik": "Alan problemi", "icerik": [
            "Kenarları doğru parçası olan üçgen, dikdörtgen ve yamuk gibi bölgelerin alanı formüllerle bulunur. Bir kenarı eğri olan bölgenin alanı ise dikdörtgenlerle yaklaşık hesaplanır: bölge ince şeritlere ayrılır ve her şerit bir dikdörtgenle değiştirilir.",
            koordinat_grafik("y = x² altındaki alanın dört dikdörtgenle yaklaşımı", [("y = x²", lambda x: x * x), ("sağ uç dikdörtgenleri", _sag_basamak)],
                             (-0.5, 2.5), (-0.5, 6), adim=0.5, etiket_adim=1, dikeyler=[0.5, 1, 1.5, 2]),
            ornek(
                "$y=x^2$ eğrisinin altında, $[0, 2]$ aralığındaki bölge verilsin.",
                "Alanı dört eşit genişlikte dikdörtgenle yaklaşık hesaplayalım.",
                "Genişlik $0.5$ tir. Sağ uç yükseklikleri $0.25$, $1$, $2.25$ ve $4$ tür: toplam $0.5 \\cdot 7.5=3.75$ olur.",
                "Sol uç yükseklikleri $0$, $0.25$, $1$, $2.25$ tir: toplam $0.5 \\cdot 3.5=1.75$ olur. Gerçek alan bu iki sayı arasındadır."),
        ]},
        {"baslik": "Dikdörtgen sayısını artırmak", "icerik": [
            "Dikdörtgenler inceldikçe eğrinin altındaki bölgeye daha iyi uyar ve iki yaklaşım birbirine yaklaşır. Dikdörtgen sayısı sonsuza götürüldüğünde toplamların ortak limiti gerçek alanı verir.",
            tablo(["Dikdörtgen sayısı", "Sol uç toplamı", "Sağ uç toplamı"], [
                ["$4$", "$1.75$", "$3.75$"],
                ["$8$", "$2.1875$", "$3.1875$"],
                ["Sonsuz", "$\\dfrac{8}{3}$", "$\\dfrac{8}{3}$"],
            ]),
            "Tablodaki iki sütun ortadaki $\\dfrac{8}{3} \\approx 2.667$ değerine iki yandan yaklaşıyor. Her adımda iki toplam arasındaki fark yarıya iniyor; dikdörtgen sayısı iki katına çıktıkça yaklaşım iki kat iyileşiyor.",
        ]},
        {"baslik": "Toplam sembolüyle yazım", "icerik": [
            "Dikdörtgen toplamı toplam sembolüyle kısaca yazılır. $[a, b]$ aralığı $n$ eşit parçaya bölünürse her parçanın genişliği $\\Delta x=\\dfrac{b-a}{n}$ olur ve toplam $\\sum_{k=1}^{n} f(x_k)\\,\\Delta x$ biçimini alır; burada $x_k$ her parçadan seçilen bir noktadır.",
            "İntegral işareti $\\int$ aslında uzatılmış bir S harfidir ve toplamı hatırlatır; $dx$ ise sonsuz küçük genişliği temsil eder. Böylece $\\int_a^b f(x)\\,dx$ yazımı, sonsuz sayıda yüksekliği $f(x)$, genişliği $dx$ olan şeridin toplamı olarak okunabilir.",
        ]},
        {"baslik": "Belirli integral", "icerik": [
            "Dikdörtgen toplamlarının limitine $f$ nin $a$ dan $b$ ye <strong>belirli integrali</strong> denir ve şöyle yazılır:",
            "$$\\int_a^b f(x)\\,dx$$",
            "$a$ ve $b$ ye integralin alt ve üst sınırları denir. Belirsiz integral bir fonksiyon ailesi verirken belirli integral tek bir sayı verir. Fonksiyon aralıkta pozitifse bu sayı, eğrinin altında ve yatay eksenin üstünde kalan bölgenin alanıdır.",
        ]},
        {"baslik": "Analizin temel teoremi", "icerik": [
            "Belirli integrali dikdörtgen toplamlarıyla hesaplamak uzundur ve her fonksiyon için ayrı bir limit gerektirir. Temel teorem kısa yolu verir: $F$, $f$ nin herhangi bir ters türeviyse",
            "$$\\int_a^b f(x)\\,dx=F(b)-F(a)$$",
            ornek(
                "$\\int_0^2 x^2\\,dx$ integrali verilsin.",
                "Temel teoremle hesaplayalım.",
                "Ters türev $F(x)=\\dfrac{x^3}{3}$ tür.",
                "$F(2)-F(0)=\\dfrac{8}{3}-0=\\dfrac{8}{3}$ bulunur; dikdörtgenlerin yaklaştığı değerle aynıdır."),
            "Belirli integralde integral sabiti $C$ yazılmaz; çünkü $F(b)+C$ den $F(a)+C$ çıkarılınca sabit sadeleşir. Hangi ters türev seçilirse seçilsin sonuç aynıdır.",
        ]},
        {"baslik": "Temel teoremle ikinci örnek", "icerik": [
            "Temel teoremin verdiği sonucu, alanı geometriyle bilinen bir bölgede denetlemek teoremin gücünü gösterir. Doğrusal bir fonksiyonun altındaki bölge bir yamuktur ve alanı formülle de bulunabilir.",
            ornek(
                "$\\int_1^3 (2x+1)\\,dx$ integrali verilsin.",
                "İntegrali hesaplayıp geometriyle karşılaştıralım.",
                "$F(x)=x^2+x$ olduğundan $F(3)-F(1)=12-2=10$ olur.",
                "Bölge paralel kenarları $3$ ve $7$, yüksekliği $2$ olan bir yamuktur; alanı $\\dfrac{(3+7) \\cdot 2}{2}=10$ dur."),
        ]},
        {"baslik": "Farklı fonksiyonlarla belirli integral", "icerik": [
            "Temel teorem her fonksiyon ailesinde aynı biçimde uygulanır: ters türev bulunur, üst sınırdaki değerden alt sınırdaki değer çıkarılır. Aşağıdaki üç integral, üç farklı temel kuralı kullanır.",
            ornek(
                "$\\int_0^{\\pi/2}\\cos x\\,dx$, $\\int_0^1 e^x\\,dx$ ve $\\int_1^e \\dfrac{1}{x}\\,dx$ integralleri verilsin.",
                "Üç integrali hesaplayalım.",
                "Birincisi $\\sin \\dfrac{\\pi}{2}-\\sin 0=1$, ikincisi $e-1$, yaklaşık $1.718$ olur.",
                "Üçüncüsü $\\ln e-\\ln 1=1$ olur."),
        ]},
        {"baslik": "Kökün belirli integrali", "icerik": [
            "Kök içeren fonksiyonlar önce kesirli üslü yazılır, sonra kuvvet kuralı uygulanır. Sınırlar yerine yazılırken kesirli üslerin hesaplanması için sınırların tam kare ya da tam küp seçilmesi işi kolaylaştırır.",
            ornek(
                "$\\int_0^4 \\sqrt{x}\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$\\sqrt{x}=x^{1/2}$ nin ters türevi $\\dfrac{2}{3}x^{3/2}$ dir.",
                "$\\dfrac{2}{3} \\cdot 4^{3/2}=\\dfrac{2}{3} \\cdot 8=\\dfrac{16}{3}$ bulunur."),
        ]},
        {"baslik": "İşaretli alan", "icerik": [
            "Fonksiyon yatay eksenin altına indiğinde dikdörtgenlerin yükseklikleri negatif olur ve belirli integral o bölgeyi negatif sayar. Bu yüzden belirli integral bir alan değil, işaretli bir alandır: eksenin üstü artı, altı eksi katkı yapar.",
            ornek(
                "$\\int_0^{\\pi}\\sin x\\,dx$ ve $\\int_0^{2\\pi}\\sin x\\,dx$ integralleri verilsin.",
                "İki integrali hesaplayalım.",
                "Ters türev $-\\cos x$ tir: birincisi $-\\cos \\pi+\\cos 0=2$ olur.",
                "İkincisi $-\\cos 2\\pi+\\cos 0=0$ olur; eksenin üstündeki ve altındaki alanlar birbirini götürür."),
            "Gerçek alan isteniyorsa eksenin altında kalan parçalar ayrı hesaplanıp mutlak değerleri toplanır. $[0, 2\\pi]$ aralığında sinüsün grafiğiyle eksen arasındaki gerçek alan $4$ tür.",
        ]},
        {"baslik": "Belirli integralin özellikleri", "icerik": [
            "Belirli integral, alanın doğal özelliklerini taşır ve bu özellikler sezgiyle de kolayca anlaşılır. Bu özellikler hesapları kısaltır ve integralin sınırlarıyla oynamayı sağlar:",
            tablo(["Özellik", "Formül"], [
                ["Eşit sınır", "$\\int_a^a f(x)\\,dx=0$"],
                ["Sınırları değiştirme", "$\\int_a^b f=-\\int_b^a f$"],
                ["Aralık bölme", "$\\int_a^b f+\\int_b^c f=\\int_a^c f$"],
                ["Doğrusallık", "$\\int_a^b (kf+g)=k\\int_a^b f+\\int_a^b g$"],
            ]),
            "Ayrıntılı örnekler için <a href=\"/blog/belirli-integral/\">Belirli İntegral Konu Anlatımı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Değişken değiştirmeye giriş", "icerik": [
            "Bazı integrallerde integrali alınan fonksiyon, bir iç fonksiyon ile onun türevinin çarpımı biçimindedir; bu yapı fark edilirse integral kolaylaşır. Bu durumda iç fonksiyona yeni bir ad verilir ve integral basit bir kuvvet integraline dönüşür. Bu yöntem, zincir kuralının tersidir.",
            ornek(
                "$\\int 2x(x^2+1)^3\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+1$ denirse $du=2x\\,dx$ olur ve integral $\\int u^3\\,du=\\dfrac{u^4}{4}+C$ ye dönüşür.",
                "Sonuç $\\dfrac{(x^2+1)^4}{4}+C$ olur."),
            "Yöntemin ayrıntıları <a href=\"/blog/degisken-degistirme/\">İntegralde Değişken Değiştirme Yöntemi</a> yazısında.",
        ]},
        {"baslik": "Alan hesabına giriş", "icerik": [
            "İki eğri arasında kalan alan, her apsiste üstteki eğriden alttakinin çıkarılıp bu farkın integralinin alınmasıyla bulunur. Önce eğrilerin kesişim noktaları, yani integralin sınırları belirlenir.",
            ornek(
                "$y=x$ doğrusu ile $y=x^2$ eğrisi arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "Eğriler $x=0$ ve $x=1$ de kesişir; bu aralıkta doğru eğrinin üstündedir.",
                "Alan $\\int_0^1 (x-x^2)\\,dx=\\dfrac{1}{2}-\\dfrac{1}{3}=\\dfrac{1}{6}$ bulunur."),
            "Alan hesabının bütün durumları <a href=\"/blog/integral-alan-hesaplama/\">İntegral ile Alan Hesaplama</a> yazısında ele alınıyor.",
        ]},
        {"baslik": "Ortalama değer", "icerik": [
            "Bir fonksiyonun bir aralıktaki ortalama değeri, belirli integralinin aralık uzunluğuna bölümüdür. Bu, aynı tabana ve aynı alana sahip dikdörtgenin yüksekliğidir; eğrinin altındaki alanı düzleyip dikdörtgene çevirmek gibi düşünülebilir.",
            ornek(
                "$f(x)=x^2$ fonksiyonu $[0, 2]$ aralığında verilsin.",
                "Ortalama değerini bulalım.",
                "$\\int_0^2 x^2\\,dx=\\dfrac{8}{3}$ ve aralık uzunluğu $2$ dir.",
                "Ortalama değer $\\dfrac{8}{3} \\cdot \\dfrac{1}{2}=\\dfrac{4}{3}$ olur."),
        ]},
        {"baslik": "Uygulama: hızdan yol", "icerik": [
            "Hız, konumun türevidir; bu yüzden hızın integrali konumdaki değişimi, yani alınan yolu verir. Hız sabitse yol hız ile sürenin çarpımıdır; hız değişiyorsa integral gerekir. Hız zaman grafiğinin altındaki alan, alınan yolu gösterir.",
            ornek(
                "Bir aracın hızı $v(t)=3t^2$ metre bölü saniye olsun.",
                "İlk iki saniyede alınan yolu bulalım.",
                "Yol $\\int_0^2 3t^2\\,dt$ dir; ters türev $t^3$ tür.",
                "Yol $2^3-0=8$ metre olur."),
        ]},
        {"baslik": "Uygulama: akıştan miktar", "icerik": [
            "Bir depoya giren suyun akış hızı zamanla değişiyor ve sabit kalmıyorsa, belirli bir sürede biriken su miktarı akış hızının integralidir. Aynı fikir üretim hızından toplam üretimi, tüketim hızından toplam tüketimi bulmakta da kullanılır.",
            ornek(
                "Bir depoya dakikada $r(t)=10-t$ litre su akıyor; $t$ dakika cinsindendir.",
                "İlk on dakikada depoya giren suyu bulalım.",
                "Miktar $\\int_0^{10}(10-t)\\,dt=\\left[10t-\\dfrac{t^2}{2}\\right]_0^{10}$ olur.",
                "$100-50=50$ litre su girer."),
        ]},
        {"baslik": "Türev ve integral birbirinin tersi", "icerik": [
            "Temel teoremin ikinci biçimi, üst sınırı değişken olan bir integralin türevinin integrali alınan fonksiyon olduğunu söyler: $\\dfrac{d}{dx}\\int_a^x f(t)\\,dt=f(x)$. Yani önce integral, sonra türev almak fonksiyonu geri verir.",
            ornek(
                "$G(x)=\\int_0^x t^2\\,dt$ fonksiyonu verilsin.",
                "$G'(x)$ i iki yoldan bulalım.",
                "Önce integrali hesaplayalım: $G(x)=\\dfrac{x^3}{3}$ ve $G'(x)=x^2$ olur.",
                "Temel teoremle de doğrudan $G'(x)=x^2$ bulunur."),
        ]},
        {"baslik": "İntegral konularının haritası", "icerik": [
            "İntegral konusu birbirine bağlı adımlardan oluşur ve her adım bir öncekinin üzerine kurulur. Önerilen çalışma sırası şöyledir:",
            tablo(["Adım", "Konu"], [
                ["1", "<a href=\"/blog/belirsiz-integral/\">Belirsiz integral</a>"],
                ["2", "<a href=\"/blog/degisken-degistirme/\">Değişken değiştirme</a>"],
                ["3", "<a href=\"/blog/belirli-integral/\">Belirli integral</a>"],
                ["4", "<a href=\"/blog/integral-alan-hesaplama/\">İntegral ile alan hesaplama</a>"],
            ]),
        ]},
        {"baslik": "Sınavda integral", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) integral; belirsiz integral kuralları, başlangıç değerli sorular, belirli integral hesabı, değişken değiştirme ve alan hesabı biçiminde karşına çıkabilir.",
                "Temel teoremin ikinci biçimi ve işaretli alan da sık sorulur."),
            "İntegral sorusunda sonucu her zaman türev alarak denetle. Belirli integralde sınırları doğru sırayla yerleştir: önce üst sınırdaki değer, sonra alt sınırdaki değer. Alan isteniyorsa eksenin altında kalan parçaları ayrı hesapla.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Belirsiz integralde $C$ yi unutmak", "$+C$ eklenir"],
                ["$\\int x^n\\,dx=x^{n+1}$", "$\\dfrac{x^{n+1}}{n+1}$"],
                ["$\\int \\dfrac{1}{x}\\,dx$ için kuvvet kuralı", "$\\ln|x|+C$"],
                ["$\\int \\sin x\\,dx=\\cos x$", "$-\\cos x+C$"],
                ["$F(a)-F(b)$ yazmak", "$F(b)-F(a)$"],
                ["İşaretli alanı gerçek alan sanmak", "Eksenin altı ayrı hesaplanır"],
            ]),
            "Bu hataların çoğu, sonucun türevi alınarak hemen yakalanır. Türev alındığında integrali alınan fonksiyon geri gelmiyorsa hesapta bir hata vardır.",
        ]},
    ],
    "sss": [
        ("İntegral nedir?",
         "Türevin tersi olan işlemdir. Türevi bilinen fonksiyonun kendisini bulur ve bir eğrinin altında kalan alanı hesaplar."),
        ("Belirsiz ve belirli integral arasındaki fark nedir?",
         "Belirsiz integral bir fonksiyon ailesidir ve integral sabiti içerir. Belirli integral iki sınır arasında hesaplanan tek bir sayıdır."),
        ("İntegral sabiti C neden yazılır?",
         "Bir sabitin türevi sıfır olduğu için türevi aynı olan sonsuz sayıda fonksiyon vardır. C bu fonksiyonların hepsini temsil eder."),
        ("Analizin temel teoremi nedir?",
         "a dan b ye belirli integral, ters türevin b deki değerinden a daki değerinin çıkarılmasıyla bulunur."),
        ("x kare nin 0 dan 2 ye integrali kaçtır?",
         "Ters türev x küp bölü 3 olduğundan sonuç 8 bölü 3 tür."),
        ("Belirli integral negatif çıkabilir mi?",
         "Evet. Fonksiyon yatay eksenin altındaysa o bölge negatif sayılır; belirli integral işaretli alandır."),
        ("Sinüsün integrali nedir?",
         "Eksi kosinüs artı C dir. Sonucun türevi alınınca sinüs geri geldiği için doğrudur."),
        ("Alan dikdörtgenlerle nasıl hesaplanır?",
         "Aralık eşit parçalara bölünür ve her parçada yüksekliği fonksiyon değeri olan bir dikdörtgen çizilir. Parça sayısı arttıkça dikdörtgenlerin toplam alanı gerçek alana yaklaşır."),
        ("Ortalama değer nedir?",
         "Bir fonksiyonun bir aralıktaki ortalama değeri, belirli integralinin aralık uzunluğuna bölümüdür. x karenin 0 ile 2 arasındaki ortalama değeri 4 bölü 3 tür."),
    ],
    "kontrol": [
        "Ters türev ve belirsiz integral kavramlarını açıklayabiliyorum.",
        "Temel integral kurallarını uygulayabiliyorum.",
        "İntegral sabitini başlangıç değerinden bulabiliyorum.",
        "Alanı dikdörtgen toplamlarıyla yaklaşık hesaplayabiliyorum.",
        "Belirli integralin anlamını açıklayabiliyorum.",
        "Temel teoremle belirli integral hesaplayabiliyorum.",
        "İşaretli alan ile gerçek alanı ayırt edebiliyorum.",
        "Belirli integralin özelliklerini kullanabiliyorum.",
        "Basit değişken değiştirme ve alan sorularını çözebiliyorum.",
        "Hızdan yol ve akıştan miktar problemlerini integralle çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["belirsiz-integral", "belirli-integral", "turev-konu-anlatimi"],
}
