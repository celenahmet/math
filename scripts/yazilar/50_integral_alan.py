# scripts/yazilar/50_integral_alan.py — Integral ile Alan Hesaplama (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "integral-alan-hesaplama",
    "baslik": "İntegral ile Alan Hesaplama",
    "aciklama": "İntegral ile alan nasıl hesaplanır? Eğri ile eksen arası, eksenin altı, iki eğri arası, kesişim noktaları, dikey eksene göre alan; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "integral-alan-hesaplama",
    "kapak_alt": "İntegral ile alan hesaplama: iki eğri arasında kalan bölgeyi küçük mavi karolarla dolduran iki öğrenci",
    "ozet": "Belirli integralin en önemli uygulaması, kenarları eğri olan bölgelerin alanını hesaplamaktır. Bir eğri ile yatay eksen arasındaki alan, eğrinin eksenin altına indiği parçalar ayrı alınarak; iki eğri arasındaki alan ise üstteki eğriden alttakinin çıkarılmasıyla bulunur. Bu yazıda eğri ile eksen arasındaki alanı, eksenin altında kalan ve eksenin iki yanına yayılan bölgeleri, iki eğri arasındaki alanı ve kesişim noktalarının bulunmasını, eğrilerin yer değiştirdiği durumları, dikey eksene göre alanı, üstel, logaritmik ve trigonometrik eğrileri, parametreli alan sorularını ve hız ile kemer gibi uygulamaları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Alan ve integral", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için belirli integrali hesaplamayı ve eğrilerin kesişim noktalarını bulmayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/belirli-integral/\">Belirli İntegral Konu Anlatımı</a> ve <a href=\"/blog/integral-konu-anlatimi/\">İntegral Konu Anlatımı</a> yazılarına göz at."),
            "Üçgen, dikdörtgen ve daire gibi tanıdık şekillerin alanları formüllerle bulunur. Kenarlarından biri eğri olan bölgelerin alanı ise belirli integralle hesaplanır. Fonksiyon aralıkta pozitifken belirli integral, eğrinin altında ve yatay eksenin üstünde kalan bölgenin alanına eşittir.",
            "Kapaktaki öğrenciler iki eğri arasında kalan bölgeyi küçük karolarla dolduruyor. Karoların sayısı ve boyutu bölgenin alanını verir; karolar küçüldükçe hesap daha kesinleşir. İntegral, bu karolaşmanın sonsuz incelikteki hâlidir ve alanı tam olarak verir.",
        ]},
        {"baslik": "Eğri ile yatay eksen arasındaki alan", "icerik": [
            "Fonksiyon $[a, b]$ aralığının hiçbir noktasında negatif değer almıyorsa, eğri ile yatay eksen arasındaki alan doğrudan belirli integraldir: $A=\\int_a^b f(x)\\,dx$.",
            ornek(
                "$y=x^2$ eğrisi, yatay eksen ve $x=2$ doğrusu arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "Eğri $[0, 2]$ aralığında negatif değildir: $A=\\int_0^2 x^2\\,dx$.",
                "$A=\\dfrac{8}{3}$ birimkare bulunur."),
            hap("Fonksiyon pozitifse alan, belirli integraldir.",
                "Negatif parçalarda integralin mutlak değeri alınır."),
        ]},
        {"baslik": "Eksenin altında kalan alan", "icerik": [
            "Fonksiyon aralıkta negatifse belirli integral negatif çıkar; alan, integralin mutlak değeridir. Alan hiçbir zaman negatif olmaz; negatif işaret yalnızca bölgenin eksenin altında olduğunu gösterir.",
            ornek(
                "$y=x^2-4$ eğrisi ile yatay eksen arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "Eğri ekseni $x=-2$ ve $x=2$ de keser ve bu aralıkta eksenin altındadır: $\\int_{-2}^{2}(x^2-4)\\,dx=-\\dfrac{32}{3}$.",
                "Alan $\\dfrac{32}{3}$ birimkare olur."),
            hap("Eksenin altında kalan bölgenin alanı, belirli integralin mutlak değeridir; alan hiçbir zaman negatif olmaz."),
        ]},
        {"baslik": "Eksenin iki yanına yayılan bölge", "icerik": [
            "Eğri aralığın bir kısmında eksenin üstünde, bir kısmında altındaysa belirli integral iki parçanın farkını verir, toplamını değil. Alan için aralık, eğrinin ekseni kestiği noktalardan bölünür ve her parçanın mutlak değeri toplanır.",
            ornek(
                "$y=x^3$ eğrisi ile yatay eksen arasında $[-1, 2]$ aralığındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "Eğri $x=0$ da ekseni keser: $\\int_{-1}^{0} x^3\\,dx=-\\dfrac{1}{4}$ ve $\\int_0^2 x^3\\,dx=4$ olur.",
                "Alan $\\dfrac{1}{4}+4=\\dfrac{17}{4}$ birimkare olur; oysa belirli integral $\\dfrac{15}{4}$ verir."),
            dikkat(
                "Eksenin iki yanına yayılan bölgede tek bir belirli integral almak.",
                "Tek integral pozitif ve negatif parçaları birbirinden çıkarır ve alanı olduğundan küçük gösterir. Önce eğrinin ekseni kestiği noktalar bulunmalıdır."),
        ]},
        {"baslik": "Eksenin altındaki parabol parçası", "icerik": [
            "Kolları yukarı bakan bir parabol iki gerçek kökü arasında yatay eksenin altında kalır. Bu parçanın alanı, iki kök arasındaki integralin mutlak değeridir.",
            ornek(
                "$y=x^2-2x$ parabolü ile yatay eksen arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "Kökler $0$ ve $2$ dir; $\\int_0^2 (x^2-2x)\\,dx=\\dfrac{8}{3}-4=-\\dfrac{4}{3}$ olur.",
                "Alan $\\dfrac{4}{3}$ birimkaredir."),
        ]},
        {"baslik": "Grafikten alan okumak", "icerik": [
            "Bazı sorularda eğri ile eksen arasındaki alanlar grafik üzerinde sayı olarak verilir ve fonksiyonun formülü hiç verilmeden belirli integralin değeri sorulur. Bu durumda eksenin üstündeki alanlar artı, altındakiler eksi işaretle toplanır.",
            ornek(
                "Bir $f$ fonksiyonunun grafiği ile eksen arasında $[0, 3]$ te eksenin üstünde $3$, $[3, 5]$ te eksenin altında $2$ birimkarelik alan olsun.",
                "$\\int_0^5 f(x)\\,dx$ değerini ve toplam alanı bulalım.",
                "Belirli integral $3-2=1$ olur.",
                "Toplam alan ise $3+2=5$ birimkaredir."),
        ]},
        {"baslik": "Sinüs eğrisinin altındaki alan", "icerik": [
            "Trigonometrik eğriler periyodik olarak eksenin üstüne ve altına geçer ve her yarım periyotta işaret değiştirir. Bu yüzden bir tam periyot boyunca belirli integral sıfır çıkabilir, ama alan sıfır değildir.",
            ornek(
                "$y=\\sin x$ eğrisi ile yatay eksen arasında $[0, 2\\pi]$ aralığındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "$\\int_0^{\\pi}\\sin x\\,dx=2$ ve $\\int_{\\pi}^{2\\pi}\\sin x\\,dx=-2$ dir.",
                "Alan $2+2=4$ birimkare olur; belirli integral ise $0$ dır."),
        ]},
        {"baslik": "İki eğri arasındaki alan", "icerik": [
            "İki eğri arasında kalan bölgenin alanı, her apsiste üstteki eğriden alttakinin çıkarılıp bu farkın integralinin alınmasıyla bulunur. Eksenin nerede olduğu önemli değildir; fark her zaman iki eğri arasındaki dikey uzaklıktır:",
            "$$A=\\int_a^b \\left(f_{\\text{üst}}(x)-f_{\\text{alt}}(x)\\right)dx$$",
            koordinat_grafik("y = x ve y = x² eğrileri", [("y = x", lambda x: x), ("y = x²", lambda x: x * x)], (-0.5, 1.6), (-0.3, 1.6), adim=0.25, etiket_adim=0.5,
                             noktalar=[(0, 0, "", True), (1, 1, "", True)]),
            ornek(
                "$y=x$ doğrusu ile $y=x^2$ eğrisi arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "Eğriler $x=0$ ve $x=1$ de kesişir; bu aralıkta doğru üsttedir.",
                "$A=\\int_0^1 (x-x^2)\\,dx=\\dfrac{1}{2}-\\dfrac{1}{3}=\\dfrac{1}{6}$ birimkare olur."),
            hap("İki eğri arasındaki alan $\\int_a^b \\left(f(x)-g(x)\\right)\\,dx$ olur; burada $f$ üstteki, $g$ alttaki eğridir."),
        ]},
        {"baslik": "Neden üst eksi alt?", "icerik": [
            "İki eğri arasındaki alanda eksenin konumu önemsizdir. Bunun nedeni şudur: iki eğri birlikte aynı miktar yukarı ya da aşağı kaydırılırsa aralarındaki bölge değişmez ve üst eksi alt farkı da aynı kalır. Bu yüzden eğrilerden biri ya da ikisi eksenin altında olsa bile formül değişmez.",
            "Geometrik olarak her apsiste üst eğri ile alt eğri arasındaki dikey uzaklık, bölgeyi oluşturan ince şeridin yüksekliğidir. Bu yüksekliklerin integrali bölgenin alanını verir. Üst ve alt yer değiştirirse fark negatif olur; bu, eğrilerin kesiştiğini ve aralığın bölünmesi gerektiğini gösterir.",
        ]},
        {"baslik": "Kesişim noktalarını bulmak", "icerik": [
            "İki eğri arasındaki kapalı bölgenin sağ ve sol sınırları, eğrilerin kesişim noktalarıdır. Bu noktalar iki fonksiyon eşitlenerek bulunur; sonra aralıktan bir sayı seçilerek hangi eğrinin üstte olduğu belirlenir.",
            ornek(
                "$y=x^2$ eğrisi ile $y=2x+3$ doğrusu arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "$x^2=2x+3$ ise $(x-3)(x+1)=0$, yani $x=-1$ ve $x=3$; aralıkta doğru üsttedir.",
                "$A=\\int_{-1}^{3}(2x+3-x^2)\\,dx=\\dfrac{32}{3}$ birimkare olur."),
            hap("Kapalı bölgenin sınırları eğrilerin kesişim noktalarıdır.", "Hangi eğrinin üstte olduğu, aralıktan bir sayı seçilerek belirlenir."),
        ]},
        {"baslik": "Parabol ile yatay doğru", "icerik": [
            "Yukarı açılan bir parabol ile onu kesen yatay bir doğru, parabolün içinde kapalı bir bölge oluşturur. Doğru üstte, parabol alttadır.",
            ornek(
                "$y=x^2$ parabolü ile $y=4$ doğrusu arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "$x^2=4$ ise $x=\\pm 2$ olur; $A=\\int_{-2}^{2}(4-x^2)\\,dx$.",
                "$A=\\dfrac{32}{3}$ birimkare bulunur."),
        ]},
        {"baslik": "Sinüs ve kosinüs arasındaki alan", "icerik": [
            "Trigonometrik eğriler arasındaki alanlarda kesişim noktaları özel açılarda olur. $[0, \\dfrac{\\pi}{4}]$ aralığında kosinüs sinüsün üstündedir; iki eğri $\\dfrac{\\pi}{4}$ de kesişir.",
            ornek(
                "$y=\\sin x$ ve $y=\\cos x$ eğrileri ile dikey eksen arasında $\\left[0, \\dfrac{\\pi}{4}\\right]$ aralığındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "$A=\\int_0^{\\pi/4}(\\cos x-\\sin x)\\,dx=\\left[\\sin x+\\cos x\\right]_0^{\\pi/4}$ olur.",
                "$\\sqrt{2}-1$, yaklaşık $0.414$ birimkare bulunur."),
        ]},
        {"baslik": "İki parabol arasındaki alan", "icerik": [
            "Biri yukarı, diğeri aşağı açılan iki parabol genellikle kapalı bir bölge oluşturur. Bölge dikey eksene göre simetrikse yarısı hesaplanıp iki katı alınır ve hesap kısalır.",
            ornek(
                "$y=x^2$ ve $y=2-x^2$ parabolleri arasındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "$x^2=2-x^2$ ise $x=\\pm 1$ olur; aralıkta $2-x^2$ üsttedir ve fark $2-2x^2$ dir.",
                "$A=\\int_{-1}^{1}(2-2x^2)\\,dx=2\\int_0^1 (2-2x^2)\\,dx=\\dfrac{8}{3}$ birimkare olur."),
        ]},
        {"baslik": "Eğrilerin yer değiştirmesi", "icerik": [
            "İki eğri birden fazla noktada kesişiyorsa her kesişim noktasında üstteki eğri değişebilir ve bölge birden fazla parçadan oluşur. Bu durumda aralık kesişim noktalarından bölünür ve her parçada ayrı bir integral alınır.",
            ornek(
                "$y=x^3$ ve $y=x$ eğrileri arasında kalan bölge verilsin.",
                "Toplam alanı bulalım.",
                "Eğriler $x=-1$, $0$ ve $1$ de kesişir. $[-1, 0]$ da $x^3$, $[0, 1]$ de $x$ üsttedir.",
                "Her iki parçanın alanı $\\dfrac{1}{4}$ dir; toplam alan $\\dfrac{1}{2}$ birimkare olur."),
            "Tek bir integral $\\int_{-1}^{1}(x-x^3)\\,dx$ alınsaydı iki parça birbirini götürür ve sonuç $0$ çıkardı. Simetrik görünen bölgelerde bu tuzağa özellikle dikkat etmek gerekir.",
        ]},
        {"baslik": "Dikey eksene göre alan", "icerik": [
            "Bazı bölgelerde eğriler $x$ in $y$ ye bağlı fonksiyonları olarak daha kolay yazılır; özellikle yana açılan paraboller böyledir. Bu durumda integral $y$ ye göre alınır: sağdaki eğriden soldaki çıkarılır ve alt ile üst $y$ sınırları arasında integral alınır.",
            ornek(
                "$x=y^2$ eğrisi ile $x=4$ doğrusu arasındaki bölge verilsin.",
                "Bölgenin alanını $y$ ye göre integralle bulalım.",
                "Eğri ile doğru $y=-2$ ve $y=2$ de kesişir; doğru sağdadır: $A=\\int_{-2}^{2}(4-y^2)\\,dy$.",
                "$A=16-\\dfrac{16}{3}=\\dfrac{32}{3}$ birimkare olur."),
            "Aynı bölge $x$ e göre de hesaplanabilir; bu kez üst sınır $\\sqrt{x}$, alt sınır $-\\sqrt{x}$ olur ve $\\int_0^4 2\\sqrt{x}\\,dx$ yine $\\dfrac{32}{3}$ verir. Hangi değişkenin daha kolay olduğu bölgenin biçimine bağlıdır.",
        ]},
        {"baslik": "Üstel ve logaritmik eğriler", "icerik": [
            "Üstel eğriler her zaman yatay eksenin üstündedir; bu yüzden altlarındaki alan doğrudan belirli integraldir ve mutlak değer gerekmez. Logaritma eğrisi ise $x=1$ de ekseni keser ve bu noktanın sağında pozitiftir.",
            ornek(
                "$y=e^x$ eğrisi ile yatay eksen arasında $[0, 1]$ aralığındaki bölge ve $y=\\ln x$ eğrisi altında $[1, e]$ aralığındaki bölge verilsin.",
                "İki alanı bulalım.",
                "Birinci alan $\\int_0^1 e^x\\,dx=e-1$, yaklaşık $1.718$ birimkaredir.",
                "$\\ln x$ in bir ters türevi $x\\ln x-x$ tir; ikinci alan $(e-e)-(0-1)=1$ birimkare olur."),
            "İkinci örnekteki ters türev, türev alınarak doğrulanır: $(x\\ln x-x)'=\\ln x+1-1=\\ln x$ tir.",
        ]},
        {"baslik": "Hiperbolün altındaki alan", "icerik": [
            "$y=\\dfrac{1}{x}$ eğrisinin altındaki alan, pozitif $x$ ler için doğal logaritmayla verilir. Bu, doğal logaritmanın geometrik tanımıdır: $1$ den $t$ ye kadar olan alan $\\ln t$ dir.",
            ornek(
                "$y=\\dfrac{1}{x}$ eğrisi ile yatay eksen arasında $[1, e]$ ve $[1, 4]$ aralıklarındaki bölgeler verilsin.",
                "Alanları bulalım.",
                "Birincisi $\\ln e-\\ln 1=1$ birimkaredir.",
                "İkincisi $\\ln 4$, yaklaşık $1.386$ birimkaredir."),
        ]},
        {"baslik": "Mutlak değerli eğri", "icerik": [
            "Mutlak değerli bir fonksiyon hiçbir zaman negatif olmadığı için grafiği hep eksenin üstündedir ve altındaki alan belirli integrale eşittir. Hesap için aralık, mutlak değerin içinin sıfır olduğu noktadan bölünür.",
            ornek(
                "$y=|x-1|$ eğrisi ile yatay eksen arasında $[0, 3]$ aralığındaki bölge verilsin.",
                "Bölgenin alanını bulalım.",
                "$\\int_0^1 (1-x)\\,dx=\\dfrac{1}{2}$ ve $\\int_1^3 (x-1)\\,dx=2$ olur.",
                "Alan $\\dfrac{5}{2}$ birimkaredir; bu, iki üçgenin alanları toplamıdır."),
        ]},
        {"baslik": "Geometriyle karşılaştırma", "icerik": [
            "Doğrularla sınırlanan bölgelerde integral ile geometri her zaman aynı sonucu vermelidir. Bu karşılaştırma, integral yönteminin güvenilirliğini gösterir ve hesap hatalarını yakalamaya yarar.",
            ornek(
                "$y=2x+1$ doğrusu, yatay eksen, $x=1$ ve $x=3$ doğruları arasındaki bölge verilsin.",
                "Alanı iki yoldan bulalım.",
                "İntegralle $\\int_1^3 (2x+1)\\,dx=\\left[x^2+x\\right]_1^3=10$ olur.",
                "Bölge paralel kenarları $3$ ve $7$, yüksekliği $2$ olan bir yamuktur; alanı $10$ dur."),
        ]},
        {"baslik": "Parametreli alan soruları", "icerik": [
            "Alanın değeri verilip bölgeyi sınırlayan bir sayı sorulabilir. Alan integralle sınır cinsinden yazılır ve verilen değere eşitlenir; ortaya çıkan denklemden sınır bulunur ve koşulu sağlamayan kökler atılır.",
            ornek(
                "$y=x^2$ eğrisi, yatay eksen ve $x=k$ doğrusu arasındaki bölgenin alanı $9$ birimkare olsun, $k>0$.",
                "$k$ yı bulalım.",
                "Alan $\\int_0^k x^2\\,dx=\\dfrac{k^3}{3}$ tür.",
                "$\\dfrac{k^3}{3}=9$ ise $k^3=27$ ve $k=3$ bulunur."),
            ornek(
                "$y=x$ doğrusu altında $[0, 2]$ aralığındaki bölge verilsin.",
                "Bu alanı iki eşit parçaya bölen $x=a$ doğrusunu bulalım.",
                "Toplam alan $\\int_0^2 x\\,dx=2$ dir; $\\int_0^a x\\,dx=1$ olmalıdır.",
                "$\\dfrac{a^2}{2}=1$ ise $a=\\sqrt{2}$ bulunur."),
        ]},
        {"baslik": "Uygulama: iki aracın mesafe farkı", "icerik": [
            "Hız zaman grafiğinin altındaki alan, o süre boyunca alınan toplam yoldur. İki aracın hız grafikleri arasındaki alan ise aynı sürede aldıkları yolların farkını verir.",
            ornek(
                "Aynı noktadan aynı anda çıkan iki aracın hızları $v_1(t)=2t$ ve $v_2(t)=t^2$ olsun.",
                "İlk iki saniyenin sonunda araçlar arasındaki mesafeyi bulalım.",
                "$[0, 2]$ aralığında $2t \\ge t^2$ olduğundan birinci araç öndedir: $\\int_0^2 (2t-t^2)\\,dt$.",
                "$4-\\dfrac{8}{3}=\\dfrac{4}{3}$ birim bulunur."),
        ]},
        {"baslik": "Uygulama: parabol biçimli kemer", "icerik": [
            "Köprü ve kapı kemerlerinin birçoğu parabol biçimindedir; parabol, yükü kemer boyunca dengeli dağıtır. Kemerin altındaki açıklığın alanı, parabolün yatay eksenin üstünde kalan kısmının integraliyle bulunur.",
            ornek(
                "Bir kemer $y=4-x^2$ parabolüyle modelleniyor; birimler metredir.",
                "Kemerin altındaki açıklığın alanını bulalım.",
                "Parabol yatay ekseni $x=\\pm 2$ de keser: $A=\\int_{-2}^{2}(4-x^2)\\,dx$.",
                "$A=\\dfrac{32}{3}$, yaklaşık $10.67$ metrekaredir."),
            "Bu alan, kemerin içine yerleştirilebilecek en büyük dikdörtgenden de, kemeri çevreleyen dikdörtgenden de farklıdır; çevreleyen dikdörtgenin alanının tam üçte ikisidir.",
            hap("Altı düz, üstü $y=1-x^2$ metre biçiminde kemerli bir pencerenin camı $x=-1$ ile $x=1$ arasındadır.", "Camın alanı $\\int_{-1}^{1}(1-x^2)\\,dx=\\dfrac{4}{3}$ metrekare olur.", gunluk=True),
        ]},
        {"baslik": "Alan hesabının adımları", "icerik": [
            "Alan sorularında aşağıdaki adımlar sırayla izlenirse hata olasılığı çok azalır ve hiçbir parça atlanmaz:",
            tablo(["Adım", "İşlem"], [
                ["1", "Bölgeyi kabaca çiz"],
                ["2", "Kesişim ve eksen kesim noktalarını bul"],
                ["3", "Her parçada hangi eğrinin üstte olduğunu belirle"],
                ["4", "Her parça için üst eksi alt integralini kur"],
                ["5", "İntegralleri hesapla ve topla"],
            ]),
            "Kaba bir çizim çoğu hatayı daha başlamadan önler: hangi eğrinin üstte olduğu ve bölgenin kaç parçadan oluştuğu çizimden hemen görülür.",
        ]},
        {"baslik": "Sınavda alan hesabı", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) alan soruları; eğri ile eksen arası, iki eğri arası, parabol ile doğru arası, parametreli alan ve grafikten alan okuma biçiminde karşına çıkabilir.",
                "Bazı sorularda alanlar verilir ve belirli integralin değeri istenir; bu durumda eksenin altındaki alanlar eksi işaretle alınır."),
            "Soruda grafik verilmişse alanları doğrudan integral değerlerine çevir: eksenin üstü artı, altı eksi. Grafik verilmemişse önce kesişim noktalarını bul ve kaba bir çizim yap.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Negatif integrali alan saymak", "Mutlak değer alınır"],
                ["Eksenin iki yanında tek integral", "Aralık bölünür"],
                ["Alt eksi üst almak", "Üst eksi alt"],
                ["Kesişim noktalarını bulmadan sınır seçmek", "Sınırlar kesişimlerdir"],
                ["Eğriler yer değiştirince tek integral", "Her parça ayrı"],
                ["Alanı negatif yazmak", "Alan her zaman pozitiftir"],
            ]),
            "Alan hesabının sonunda sonucu bir tahminle karşılaştır: bölge yaklaşık hangi dikdörtgenin içine sığıyor? Sonuç o dikdörtgenin alanından büyükse ya da negatifse bir yerde hata vardır.",
        ]},
    ],
    "sss": [
        ("Eğri ile eksen arasındaki alan nasıl bulunur?",
         "Fonksiyon aralıkta pozitifse alan belirli integraldir. Eksenin altına inen parçalarda integralin mutlak değeri alınır."),
        ("İki eğri arasındaki alan nasıl bulunur?",
         "Eğrilerin kesişim noktaları bulunur, her aralıkta üstteki eğriden alttaki çıkarılır ve bu farkın integrali alınır."),
        ("Belirli integral ile alan neden farklı çıkabilir?",
         "Belirli integral eksenin altındaki bölgeyi negatif sayar. Alan ise her parçayı pozitif sayar."),
        ("y = x ile y = x kare arasındaki alan kaçtır?",
         "Eğriler 0 ve 1 de kesişir; alan x eksi x karenin 0 dan 1 e integralidir ve 1 bölü 6 dır."),
        ("Sinüs eğrisinin bir periyot boyunca altındaki alan kaçtır?",
         "0 ile 2 pi arasında alan 4 birimkaredir; belirli integral ise 0 dır."),
        ("Dikey eksene göre alan ne zaman kullanılır?",
         "Eğriler x in y ye bağlı fonksiyonları olarak daha kolay yazılıyorsa integral y ye göre alınır: sağdaki eğriden soldaki çıkarılır."),
        ("Parabol ile doğru arasındaki alan nasıl bulunur?",
         "Parabol ile doğru eşitlenerek kesişim noktaları bulunur. Bu noktalar arasında doğru üstteyse doğru eksi parabolün integrali alınır."),
        ("Alan neden negatif olamaz?",
         "Alan bir büyüklüktür ve her zaman pozitiftir. Belirli integral negatif çıkıyorsa bölge eksenin altındadır ve alan için mutlak değer alınır."),
        ("Eğriler aralıkta yer değiştirirse ne yapılır?",
         "Aralık kesişim noktalarından bölünür; her parçada hangi eğri üstteyse ondan alttaki çıkarılır ve parçaların alanları toplanır."),
    ],
    "kontrol": [
        "Eğri ile yatay eksen arasındaki alanı hesaplayabiliyorum.",
        "Eksenin altında kalan bölgenin alanını bulabiliyorum.",
        "Eksenin iki yanına yayılan bölgeyi parçalara ayırabiliyorum.",
        "İki eğri arasındaki alanı üst eksi alt integraliyle bulabiliyorum.",
        "Kesişim noktalarını bulup integralin sınırlarını belirleyebiliyorum.",
        "Eğrilerin yer değiştirdiği durumları ayrı hesaplayabiliyorum.",
        "Dikey eksene göre alan hesaplayabiliyorum.",
        "Üstel, logaritmik ve trigonometrik eğrilerin altındaki alanı bulabiliyorum.",
        "Parametreli alan sorularını çözebiliyorum.",
        "Alan hesabını hız ve kemer gibi uygulamalarda kullanabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["belirli-integral", "integral-konu-anlatimi", "parabol-grafigi"],
}
