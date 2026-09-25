# scripts/yazilar/45_maksimum_minimum.py — Turevde Maksimum ve Minimum (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "maksimum-minimum",
    "baslik": "Türevde Maksimum ve Minimum Nasıl Bulunur?",
    "aciklama": "Türevle maksimum ve minimum nasıl bulunur? Kritik nokta, birinci ve ikinci türev testi, kapalı aralıkta mutlak ekstremum ve optimizasyon problemleri; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "maksimum-minimum",
    "kapak_alt": "Türevde maksimum ve minimum: dalgalı eğrinin en yüksek ve en düşük noktalarını ışıklı işaretçilerle gösteren öğrenci",
    "ozet": "Bir fonksiyonun en büyük ve en küçük değerleri, türevin sıfır olduğu ya da tanımsız olduğu kritik noktalarda ve aralığın uçlarında aranır. Türevin işaret değiştirmesi ya da ikinci türevin işareti, bir kritik noktanın tepe mi çukur mu olduğunu söyler. Bu yazıda yerel ve mutlak ekstremum kavramlarını, kritik noktaları, birinci ve ikinci türev testlerini, kapalı aralıkta mutlak en büyük ve en küçük değeri, türevin tanımsız olduğu kritik noktaları, rasyonel, üstel, logaritmik ve trigonometrik örnekleri, parametreli soruları ve en büyük alan, kutu, en yakın nokta ve kâr gibi optimizasyon problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Maksimum ve minimum nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için türev kurallarını ve artan azalan aralıkları bulmayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/artan-azalan-fonksiyonlar/\">Türevde Artan ve Azalan Fonksiyonlar</a> ve <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> yazılarına göz at."),
            "Bir fonksiyonun grafiğindeki tepe noktaları maksimum, çukur noktaları minimum noktalarıdır. İkisine birlikte <strong>ekstremum</strong> denir. En yüksek kâr, en az malzeme, en kısa süre gibi soruların hepsi bir fonksiyonun maksimum ya da minimum değerini bulmaya dayanır.",
            "Kapaktaki öğrenci dalgalı bir eğrinin en yüksek ve en düşük noktalarına ışıklı işaretçiler yerleştiriyor. Eğrinin bu noktalarda bir an için yatay olduğuna dikkat et: yükselen yol burada alçalmaya, alçalan yol yükselmeye başlıyor. Türevle ekstremum bulmanın temel fikri tam olarak budur ve bütün yöntemler buradan çıkar.",
        ]},
        {"baslik": "Yerel ve mutlak ekstremum", "icerik": [
            "Bir noktadaki değer, o noktanın yakınındaki bütün değerlerden büyükse orada <strong>yerel maksimum</strong>, küçükse <strong>yerel minimum</strong> vardır. Değer bütün tanım kümesindeki en büyük ya da en küçük değerse buna <strong>mutlak</strong> maksimum ya da minimum denir.",
            tablo(["Kavram", "Karşılaştırma"], [
                ["Yerel maksimum", "Yakın noktalardan büyük"],
                ["Yerel minimum", "Yakın noktalardan küçük"],
                ["Mutlak maksimum", "Bütün noktalardan büyük ya da eşit"],
                ["Mutlak minimum", "Bütün noktalardan küçük ya da eşit"],
            ]),
            "Bir fonksiyonun birden çok yerel maksimumu olabilir ve bir yerel minimum, başka bir yerel maksimumdan büyük olabilir. Mutlak değerler ise tektir; ancak her fonksiyonun mutlak maksimumu ya da minimumu olmayabilir.",
        ]},
        {"baslik": "Kritik noktalar", "icerik": [
            "Türevli bir fonksiyonun yerel ekstremum noktasında teğet yataydır; yani türev sıfırdır. Türevin tanımsız olduğu köşe noktaları da ekstremum olabilir. Türevin sıfır ya da tanımsız olduğu noktalara <strong>kritik nokta</strong> denir.",
            hap("Yerel ekstremumlar yalnızca kritik noktalarda olabilir.",
                "Ama her kritik nokta ekstremum değildir; test gerekir."),
            "Örneğin $x^3$ ün türevi sıfırda sıfırdır, yani sıfır bir kritik noktadır; ama fonksiyon orada artmaya devam eder ve ekstremum yoktur. Bu yüzden kritik noktalar bulunduktan sonra her biri bir testle incelenir.",
        ]},
        {"baslik": "Birinci türev testi", "icerik": [
            "Kritik noktanın iki yanında türevin işaretine bakılır. Türev artıdan eksiye geçiyorsa fonksiyon önce artıp sonra azalır ve o noktada yerel maksimum vardır; eksiden artıya geçiyorsa yerel minimum vardır. İşaret değişmiyorsa ekstremum yoktur.",
            tablo(["Türevin işaret değişimi", "Sonuç"], [
                ["Artıdan eksiye", "Yerel maksimum"],
                ["Eksiden artıya", "Yerel minimum"],
                ["Değişmiyor", "Ekstremum yok"],
            ]),
            hap("Türev artıdan eksiye geçiyorsa yerel maksimum, eksiden artıya geçiyorsa yerel minimum vardır.", "Türevin işareti değişmiyorsa o noktada ekstremum yoktur."),
        ]},
        {"baslik": "Birinci türev testiyle örnek", "icerik": [
            "Birinci türev testi, artan ve azalan aralıkları bulmak için yapılan işaret tablosunun doğrudan devamıdır. Tablo yapıldığında ekstremumlar da okunmuş olur.",
            koordinat_grafik("y = x³ - 6x² + 9x + 1 grafiği", [("", lambda x: x ** 3 - 6 * x ** 2 + 9 * x + 1)], (-0.5, 4.5), (-1, 6), adim=1,
                             noktalar=[(1, 5, "", True), (3, 1, "", True)]),
            ornek(
                "$f(x)=x^3-6x^2+9x+1$ fonksiyonu verilsin.",
                "Yerel ekstremum noktalarını bulalım.",
                "$f'(x)=3(x-1)(x-3)$; türev $x=1$ de artıdan eksiye, $x=3$ te eksiden artıya geçer.",
                "$x=1$ de yerel maksimum $f(1)=5$, $x=3$ te yerel minimum $f(3)=1$ vardır."),
        ]},
        {"baslik": "İkinci türev testi", "icerik": [
            "Türevin sıfır olduğu bir noktada ikinci türevin işareti grafiğin bükülme yönünü söyler. İkinci türev negatifse grafik aşağı doğru bükülüdür ve nokta bir tepedir; pozitifse yukarı doğru bükülüdür ve nokta bir çukurdur.",
            tablo(["$f'(a)=0$ iken", "Sonuç"], [
                ["$f''(a)<0$", "Yerel maksimum"],
                ["$f''(a)>0$", "Yerel minimum"],
                ["$f''(a)=0$", "Test karar vermez"],
            ]),
            ornek(
                "$f(x)=x^3-3x$ fonksiyonu verilsin.",
                "Kritik noktaları ikinci türev testiyle inceleyelim.",
                "$f'(x)=3x^2-3$ ten kritik noktalar $-1$ ve $1$ dir; $f''(x)=6x$ tir.",
                "$f''(-1)=-6<0$ olduğundan $x=-1$ de maksimum $2$, $f''(1)=6>0$ olduğundan $x=1$ de minimum $-2$ vardır."),
            hap("$f'(a)=0$ iken $f''(a)<0$ ise yerel maksimum, $f''(a)>0$ ise yerel minimum vardır."),
        ]},
        {"baslik": "İkinci türev karar vermezse", "icerik": [
            "İkinci türevin de sıfır olduğu noktalarda test sonuç vermez; o zaman birinci türev testine dönülür. Bu durumda nokta maksimum da, minimum da, hiçbiri de olabilir.",
            ornek(
                "$f(x)=x^4$ ve $g(x)=x^3$ fonksiyonları $x=0$ da verilsin.",
                "İkinci türev testinin neden karar veremediğini görelim.",
                "İki fonksiyonun da birinci ve ikinci türevi sıfırda sıfırdır.",
                "$x^4$ ün türevi $4x^3$ sıfırda eksiden artıya geçer ve minimum vardır; $x^3$ ün türevi $3x^2$ ise işaret değiştirmez ve ekstremum yoktur."),
        ]},
        {"baslik": "Kapalı aralıkta mutlak ekstremum", "icerik": [
            "Kapalı bir aralıkta sürekli olan fonksiyon, mutlak en büyük ve en küçük değerini mutlaka alır. Bu değerler ya kritik noktalarda ya da aralığın uçlarındadır. Bu yüzden yöntem basittir: aralıktaki kritik noktalarda ve iki uçta fonksiyon değerleri hesaplanır, en büyüğü ve en küçüğü seçilir.",
            ornek(
                "$f(x)=x^3-3x$ fonksiyonu $[-2, 3]$ aralığında verilsin.",
                "Mutlak en büyük ve en küçük değeri bulalım.",
                "Kritik noktalar $-1$ ve $1$ dir. Değerler: $f(-2)=-2$, $f(-1)=2$, $f(1)=-2$, $f(3)=18$.",
                "Mutlak en büyük değer $18$ dir ve $x=3$ te alınır; mutlak en küçük değer $-2$ dir ve $x=-2$ ile $x=1$ de alınır."),
            dikkat(
                "Kapalı aralıkta yalnızca kritik noktalara bakmak.",
                "Örnekte en büyük değer bir uç noktada çıktı; yerel maksimum olan $f(-1)=2$ ise mutlak maksimum değildir. Uç noktalar her zaman hesaba katılmalıdır."),
            hap("Kapalı aralıkta mutlak ekstremumlar ya kritik noktalarda ya da aralığın uçlarındadır; hepsinde değer hesaplanıp karşılaştırılır."),
        ]},
        {"baslik": "Parabolün tepesi", "icerik": [
            "İkinci dereceden fonksiyonlarda tek bir kritik nokta vardır ve bu nokta parabolün tepe noktasıdır. Baş katsayı negatifse tepe bir maksimum, pozitifse minimumdur.",
            ornek(
                "$f(x)=-x^2+4x+1$ fonksiyonu verilsin.",
                "En büyük değeri bulalım.",
                "$f'(x)=-2x+4=0$ ise $x=2$ olur; $f''(x)=-2<0$ dır.",
                "En büyük değer $f(2)=5$ tir."),
            "Sonuç parabolün tepe noktası formülüyle de bulunur: $r=-\\dfrac{b}{2a}=2$. Ayrıntılar için <a href=\"/blog/parabol-tepe-noktasi/\">Parabolün Tepe Noktası</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Türevin tanımsız olduğu kritik nokta", "icerik": [
            "Köşe ya da sivri uç yapan grafiklerde türev tanımsızdır ama bu noktalar ekstremum olabilir. Bu yüzden kritik noktalar aranırken türevin tanımsız olduğu yerler de listeye eklenir.",
            ornek(
                "$f(x)=|x|$ ve $g(x)=x^{2/3}$ fonksiyonları $x=0$ da verilsin.",
                "Sıfırda ekstremum olup olmadığını inceleyelim.",
                "$|x|$ in türevi sıfırın solunda $-1$, sağında $1$ dir; türev tanımsızdır ama eksiden artıya geçer.",
                "$g'(x)=\\dfrac{2}{3}x^{-1/3}$ sıfırda tanımsızdır ve yine eksiden artıya geçer; iki fonksiyonun da sıfırda minimumu vardır ve değeri $0$ dır."),
        ]},
        {"baslik": "Rasyonel fonksiyonda ekstremum", "icerik": [
            "Rasyonel fonksiyonlarda türevin işaretini pay belirlediği için kritik noktalar payın kökleridir. Payda sıfır olmuyorsa tanımsız nokta da yoktur.",
            ornek(
                "$f(x)=\\dfrac{x}{x^2+1}$ fonksiyonu verilsin.",
                "Ekstremum değerlerini bulalım.",
                "$f'(x)=\\dfrac{1-x^2}{(x^2+1)^2}$ dir; türev $-1$ de eksiden artıya, $1$ de artıdan eksiye geçer.",
                "Minimum $f(-1)=-\\dfrac{1}{2}$, maksimum $f(1)=\\dfrac{1}{2}$ dir; bunlar aynı zamanda mutlak değerlerdir."),
        ]},
        {"baslik": "Üstel fonksiyonda ekstremum", "icerik": [
            "Üstel fonksiyon içeren ifadelerde türev genellikle üstel bir çarpan ile polinom gibi basit bir çarpanın çarpımıdır. Üstel çarpan hiç sıfır olmadığı için kritik nokta yalnızca diğer çarpandan gelir.",
            ornek(
                "$f(x)=x e^{-x}$ fonksiyonu verilsin.",
                "En büyük değeri bulalım.",
                "$f'(x)=e^{-x}(1-x)$ tir; türev $x=1$ de artıdan eksiye geçer.",
                "En büyük değer $f(1)=\\dfrac{1}{e}$ dir."),
        ]},
        {"baslik": "Logaritmik fonksiyonda ekstremum", "icerik": [
            "Logaritmalı fonksiyonlar yalnızca pozitif sayılarda tanımlıdır. Kritik noktalar bu aralıkta aranır ve sonuçta sık sık $e$ sayısı ortaya çıkar.",
            ornek(
                "$f(x)=\\dfrac{\\ln x}{x}$ fonksiyonu verilsin, $x>0$.",
                "En büyük değeri bulalım.",
                "$f'(x)=\\dfrac{1-\\ln x}{x^2}$ tir; türev $x=e$ de artıdan eksiye geçer.",
                "En büyük değer $f(e)=\\dfrac{1}{e}$ dir."),
        ]},
        {"baslik": "Trigonometrik fonksiyonda ekstremum", "icerik": [
            "Trigonometrik fonksiyonlarda kritik noktalar periyodik olarak tekrar eder. İnceleme bir periyotluk aralıkta yapılır ve uç noktalar da hesaba katılır.",
            ornek(
                "$f(x)=\\sin x+\\cos x$ fonksiyonu $[0, 2\\pi]$ aralığında verilsin.",
                "En büyük ve en küçük değeri bulalım.",
                "$f'(x)=\\cos x-\\sin x=0$ ise $\\tan x=1$, yani $x=\\dfrac{\\pi}{4}$ ya da $\\dfrac{5\\pi}{4}$ olur.",
                "$f\\left(\\dfrac{\\pi}{4}\\right)=\\sqrt{2}$ en büyük, $f\\left(\\dfrac{5\\pi}{4}\\right)=-\\sqrt{2}$ en küçük değerdir; uçlarda değer $1$ dir."),
        ]},
        {"baslik": "Parametreli ekstremum", "icerik": [
            "Bir fonksiyonun belirli bir noktada ekstremumu olduğu verilirse, o noktada türev sıfır olmalıdır. Bu koşul bilinmeyen katsayı için bir denklem verir.",
            ornek(
                "$f(x)=x^3+ax^2-9x$ fonksiyonunun $x=3$ te ekstremumu olsun.",
                "$a$ yı ve ekstremumun türünü bulalım.",
                "$f'(3)=27+6a-9=0$ ise $a=-3$ olur; $f'(x)=3x^2-6x-9=3(x-3)(x+1)$.",
                "Türev $x=3$ te eksiden artıya geçtiği için bu nokta yerel minimumdur ve $f(3)=-27$ dir."),
        ]},
        {"baslik": "Türev grafiğinden ekstremum okumak", "icerik": [
            "Bazı sorularda fonksiyonun değil türevinin grafiği verilir. Bu durumda türev grafiğinin yatay ekseni kestiği noktalar kritik noktalardır. Türev grafiği ekseni yukarıdan aşağı kesiyorsa türev artıdan eksiye geçer ve fonksiyonun orada yerel maksimumu vardır; aşağıdan yukarı kesiyorsa yerel minimum vardır.",
            "Türev grafiği ekseni kesmeden yalnızca dokunuyorsa işaret değişmez ve ekstremum yoktur. Bu okuma, türev grafiğini fonksiyon grafiği sanma hatasından kaçınmayı gerektirir: türev grafiğinin tepe noktası, fonksiyonun tepe noktası değildir.",
        ]},
        {"baslik": "Optimizasyonun adımları", "icerik": [
            "Günlük hayattaki en büyük ya da en küçük değer problemlerine optimizasyon denir. Bu problemler her zaman aynı adımlarla çözülür:",
            tablo(["Adım", "İşlem"], [
                ["1", "Enbüyüklenecek ya da enküçüklenecek niceliği belirle"],
                ["2", "Bu niceliği tek bir değişkenin fonksiyonu olarak yaz"],
                ["3", "Değişkenin anlamlı olduğu aralığı belirle"],
                ["4", "Kritik noktaları bul ve test et"],
                ["5", "Uç noktaları da kontrol edip sonucu yorumla"],
            ]),
            "En zor adım ikincisidir: problemde birden çok değişken varsa verilen bir koşul yardımıyla hepsi tek bir değişkene indirgenir.",
        ]},
        {"baslik": "En büyük alan", "icerik": [
            "Çevresi sabit olan dikdörtgenler arasında alanı en büyük olan karedir. Bu klasik sonuç türevle kolayca gösterilir ve bahçe çiti, çerçeve gibi problemlerin temelidir.",
            ornek(
                "Çevresi $20$ cm olan dikdörtgenler verilsin.",
                "Alanı en büyük olan dikdörtgeni bulalım.",
                "Bir kenar $x$ ise diğer kenar $10-x$ olur; alan $A(x)=x(10-x)=10x-x^2$ dir ve $0<x<10$.",
                "$A'(x)=10-2x=0$ ise $x=5$ tir; dikdörtgen bir karedir ve en büyük alan $25$ santimetrekaredir."),
        ]},
        {"baslik": "Açık kutu problemi", "icerik": [
            "Kare bir kartonun köşelerinden eşit kareler kesilip kenarlar kaldırılarak üstü açık bir kutu yapılır. Kesilen karelerin boyutu kutunun hacmini belirler ve hacmi en büyük yapan boyut türevle bulunur.",
            ornek(
                "Kenarı $12$ cm olan kare bir kartonun köşelerinden kenarı $x$ olan kareler kesiliyor.",
                "Kutunun hacmini en büyük yapan $x$ i ve en büyük hacmi bulalım.",
                "Hacim $V(x)=x(12-2x)^2$ dir ve $0<x<6$; türev $V'(x)=(12-2x)(12-6x)$ olur ve aralıkta yalnızca $x=2$ de sıfırdır.",
                "Türev $x=2$ de artıdan eksiye geçer; en büyük hacim $V(2)=2 \\cdot 64=128$ santimetreküptür."),
            hap("Kenarı $30$ santimetre olan kare bir kartonun köşelerinden $5$ santimetrelik kareler kesilip kenarlar kaldırılırsa üstü açık kutunun hacmi en büyük olur.", "Kutunun tabanı $20$ santimetrelik bir kare, yüksekliği $5$ santimetre olur ve hacmi $20 \\cdot 20 \\cdot 5=2000$ santimetreküp olur.", gunluk=True),
        ]},
        {"baslik": "Toplamı sabit iki sayı", "icerik": [
            "Toplamı sabit iki pozitif sayının çarpımı, sayılar eşitken en büyüktür; kareleri toplamı ise sayılar eşitken en küçüktür. İki sonuç da tek değişkenli bir fonksiyonun türeviyle gösterilir.",
            ornek(
                "Toplamı $10$ olan iki pozitif sayı verilsin.",
                "Çarpımın en büyük, kareleri toplamının en küçük değerini bulalım.",
                "Sayılar $x$ ve $10-x$ olsun. Çarpım $10x-x^2$, türevi $10-2x$; en büyük çarpım $x=5$ te $25$ olur.",
                "Kareler toplamı $x^2+(10-x)^2$, türevi $4x-20$; en küçük değer yine $x=5$ te $50$ olur."),
        ]},
        {"baslik": "Eğriye en yakın nokta", "icerik": [
            "Bir noktanın bir eğriye en yakın noktası, uzaklığın karesini enküçükleyerek bulunur. Uzaklığın kendisi yerine karesiyle çalışmak kökten kurtarır ve aynı noktayı verir.",
            ornek(
                "$y=x^2$ parabolü ve $(0, 2)$ noktası verilsin.",
                "Parabolün bu noktaya en yakın noktalarını ve en kısa uzaklığı bulalım.",
                "Uzaklığın karesi $d^2=x^2+(x^2-2)^2=x^4-3x^2+4$ tür; türevi $4x^3-6x=2x(2x^2-3)$ olur.",
                "$x^2=\\dfrac{3}{2}$ için $d^2=\\dfrac{7}{4}$ en küçüktür; en kısa uzaklık $\\dfrac{\\sqrt{7}}{2}$ dir."),
        ]},
        {"baslik": "Kâr maksimizasyonu", "icerik": [
            "Kâr, gelir ile maliyetin farkıdır ve üretim miktarına bağlı bir fonksiyondur. Kâr fonksiyonunun türevi sıfır olduğu üretim miktarında, bir birim daha üretmenin getirdiği ek gelir ile ek maliyet eşitlenir; kâr bu noktada en büyüktür.",
            ornek(
                "Bir ürünün kâr fonksiyonu $K(x)=-x^2+40x-300$ bin TL olsun; $x$ üretim miktarıdır.",
                "Kârı en büyük yapan üretim miktarını ve en büyük kârı bulalım.",
                "$K'(x)=-2x+40=0$ ise $x=20$ olur; $K''(x)=-2<0$ dır.",
                "En büyük kâr $K(20)=100$ bin TL dir."),
        ]},
        {"baslik": "Mutlak ekstremumun olmadığı durumlar", "icerik": [
            "Açık ya da sınırsız aralıklarda fonksiyonun mutlak maksimumu ya da minimumu olmayabilir. $x^3$ fonksiyonu bütün gerçek sayılarda sınırsız büyür ve küçülür; hiçbir mutlak ekstremumu yoktur.",
            "$\\dfrac{1}{x}$ fonksiyonu $(0, 1]$ aralığında süreklidir ama aralık kapalı olmadığı için sıfıra yaklaşırken sınırsız büyür ve en büyük değeri yoktur; en küçük değeri ise $x=1$ de $1$ dir. Bu yüzden optimizasyon problemlerinde değişkenin aralığı mutlaka yazılmalı ve uçlardaki davranış incelenmelidir.",
        ]},
        {"baslik": "Sınavda maksimum ve minimum", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) ekstremum soruları; yerel ekstremum noktaları, kapalı aralıkta en büyük ve en küçük değer, parametreli ekstremum ve optimizasyon problemleri biçiminde karşına çıkabilir.",
                "Optimizasyon soruları genellikle alan, hacim, uzaklık ve kâr üzerine kurulur."),
            "Kapalı aralık sorusunda uçları unutma; yerel maksimum her zaman mutlak maksimum değildir. Optimizasyon sorusunda önce niceliği tek değişkenle yaz, değişkenin aralığını belirle, sonra türev al.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Her kritik noktayı ekstremum saymak", "İşaret değişimi gerekir"],
                ["Kapalı aralıkta uçları unutmak", "Uçlar da hesaplanır"],
                ["Türevin tanımsız olduğu noktaları atlamak", "Onlar da kritik noktadır"],
                ["$f''=0$ iken ekstremum yok demek", "Birinci türev testine dönülür"],
                ["Ekstremum noktası ile değerini karıştırmak", "Nokta $x$, değer $f(x)$"],
                ["Optimizasyonda aralığı yazmamak", "Değişkenin anlamlı aralığı belirlenir"],
            ]),
            "Sonucu her zaman yorumla: bir kutunun kenarı negatif, bir dikdörtgenin kenarı sıfır çıkamaz. Anlamsız çıkan kritik noktalar, problemin koşullarıyla elenir.",
        ]},
    ],
    "sss": [
        ("Kritik nokta nedir?",
         "Türevin sıfır olduğu ya da tanımsız olduğu noktadır. Yerel ekstremumlar yalnızca bu noktalarda olabilir."),
        ("Birinci türev testi nedir?",
         "Kritik noktanın iki yanında türevin işaretine bakılır. Artıdan eksiye geçiş yerel maksimum, eksiden artıya geçiş yerel minimum demektir."),
        ("İkinci türev testi nedir?",
         "Türevin sıfır olduğu noktada ikinci türev negatifse yerel maksimum, pozitifse yerel minimum vardır. İkinci türev sıfırsa test karar vermez."),
        ("Kapalı aralıkta en büyük değer nasıl bulunur?",
         "Aralıktaki kritik noktalarda ve iki uç noktada fonksiyon değerleri hesaplanır; en büyüğü mutlak maksimumdur."),
        ("Çevresi sabit dikdörtgenlerden hangisinin alanı en büyüktür?",
         "Karenin. Çevresi 20 olan dikdörtgenler arasında en büyük alan kenarı 5 olan karenindir ve 25 tir."),
        ("Her kritik nokta ekstremum mudur?",
         "Hayır. x küp fonksiyonunda sıfır kritik noktadır ama türev işaret değiştirmediği için ekstremum yoktur."),
        ("Optimizasyon problemi nasıl çözülür?",
         "Enbüyüklenecek ya da enküçüklenecek nicelik tek değişkenli bir fonksiyon olarak yazılır, değişkenin aralığı belirlenir, kritik noktalar bulunur ve uçlarla birlikte karşılaştırılır."),
    ],
    "kontrol": [
        "Yerel ve mutlak ekstremum kavramlarını ayırt edebiliyorum.",
        "Kritik noktaları bulabiliyorum.",
        "Birinci türev testini uygulayabiliyorum.",
        "İkinci türev testini ve sınırını biliyorum.",
        "Kapalı aralıkta mutlak en büyük ve en küçük değeri bulabiliyorum.",
        "Türevin tanımsız olduğu kritik noktaları inceleyebiliyorum.",
        "Rasyonel, üstel, logaritmik ve trigonometrik fonksiyonlarda ekstremum bulabiliyorum.",
        "Parametreli ekstremum sorularını çözebiliyorum.",
        "Optimizasyon problemlerini tek değişkenli fonksiyona indirgeyebiliyorum.",
        "Alan, hacim, uzaklık ve kâr problemlerini türevle çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["artan-azalan-fonksiyonlar", "teget-denklemi", "turev-konu-anlatimi"],
}
