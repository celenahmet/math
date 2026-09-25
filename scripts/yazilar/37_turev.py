# scripts/yazilar/37_turev.py — Turev Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "turev-konu-anlatimi",
    "baslik": "Türev Konu Anlatımı",
    "aciklama": "Türev nedir? Ortalama ve anlık değişim hızı, teğetin eğimi, temel türevler, türev kuralları, ikinci türev, hız ve ivme, türevlenebilirlik; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "turev-konu-anlatimi",
    "kapak_alt": "Türev konu anlatımı: dalgalı mavi eğri üzerinde farklı noktalara yerleştirilmiş eğim çubuklarını inceleyen öğrenci",
    "ozet": "Türev, bir fonksiyonun bir noktadaki anlık değişim hızıdır ve geometrik olarak grafiğin o noktadaki teğetinin eğimine eşittir. Hız, büyüme, maliyet ve eğim gibi değişim içeren her kavramın matematiksel dilidir. Bu yazıda ortalama değişim hızından anlık değişim hızına geçişi, türevin gösterimlerini ve geometrik anlamını, temel fonksiyonların türevlerini, türev kurallarının özetini, yatay teğetleri, hız ve ivmeyi, ikinci türevi, türevlenebilirlik koşulunu, parçalı fonksiyonlarda türevi ve alan, maliyet gibi uygulamaları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Türev nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için limiti, sürekliliği ve doğrunun eğimini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/limit-konu-anlatimi/\">Limit Konu Anlatımı</a> ve <a href=\"/blog/sureklilik-konu-anlatimi/\">Süreklilik Konu Anlatımı</a> yazılarına göz at."),
            "Bir otomobilin hız göstergesi o andaki hızı gösterir; bir saat boyunca alınan yolun süreye bölümü ise ortalama hızdır. <strong>Türev</strong>, bu anlık hız fikrinin matematikteki karşılığıdır: bir fonksiyonun bir noktada ne kadar hızlı değiştiğini ölçer.",
            "Kapaktaki öğrenci dalgalı bir eğrinin farklı noktalarına küçük düz çubuklar yerleştiriyor. Eğrinin dik yükseldiği yerde çubuk dik, düzleştiği yerde yatay, alçaldığı yerde ters yöne eğik duruyor. Her çubuğun eğimi, eğrinin o noktadaki türevidir. Bu yazı türevin ne olduğunu, nasıl hesaplandığını ve nerelerde kullanıldığını bir bütün olarak anlatıyor.",
        ]},
        {"baslik": "Ortalama değişim hızı", "icerik": [
            "Bir fonksiyonun $[a, b]$ aralığındaki ortalama değişim hızı, değerdeki değişimin aralık uzunluğuna bölümüdür. Geometrik olarak bu sayı, grafiğin $a$ ve $b$ deki noktalarını birleştiren kesenin eğimidir:",
            "$$\\dfrac{f(b)-f(a)}{b-a}$$",
            ornek(
                "$f(x)=x^2$ fonksiyonu verilsin.",
                "$[1, 3]$ aralığındaki ortalama değişim hızını bulalım.",
                "$f(3)=9$ ve $f(1)=1$ olur.",
                "Ortalama değişim hızı $\\dfrac{9-1}{3-1}=4$ olur."),
        ]},
        {"baslik": "Anlık değişim hızı", "icerik": [
            "Aralık daraltıldıkça ortalama değişim hızı bir noktadaki değişimi daha iyi temsil eder. Aralığın uzunluğu $h$ sıfıra yaklaştırılınca ortalama hızın limiti anlık değişim hızını, yani türevi verir.",
            ornek(
                "$f(x)=x^2$ fonksiyonu verilsin.",
                "$x=1$ deki anlık değişim hızını bulalım.",
                "$[1, 1+h]$ aralığında ortalama hız $\\dfrac{(1+h)^2-1}{h}=2+h$ olur.",
                "$h$ sıfıra yaklaşırken bu değer $2$ ye yaklaşır; $f$ nin $1$ deki türevi $2$ dir."),
            hap("Türev, aralık sıfıra daralırken ortalama değişim hızının limitidir.",
                "Geometrik olarak teğetin eğimi, fiziksel olarak anlık hızdır."),
        ]},
        {"baslik": "Kesenden teğete: sayısal görünüm", "icerik": [
            "Kesenin teğete dönüşmesi sayılarla da izlenebilir. $f(x)=x^2$ için $1$ ile $1+h$ arasındaki kesenin eğimi $2+h$ dir; $h$ küçüldükçe eğim $2$ ye yaklaşır:",
            tablo(["$h$", "$1$", "$0.1$", "$0.01$", "$0.001$"], [
                ["Kesenin eğimi", "$3$", "$2.1$", "$2.01$", "$2.001$"],
            ]),
            "Tablodaki değerler hiçbir zaman tam olarak $2$ olmaz, ama $2$ ye istenildiği kadar yaklaşır. Türev bu yaklaşılan değerdir; limit kavramının türevin temelinde olmasının nedeni budur.",
        ]},
        {"baslik": "Türevin birimi", "icerik": [
            "Türev bir oran olduğu için birimi, fonksiyonun biriminin değişkenin birimine bölümüdür. Konum metre, zaman saniye ise hız metre bölü saniyedir; maliyet TL, üretim adet ise marjinal maliyet TL bölü adettir.",
            "Birimi yazmak, uygulama sorularında türevin ne anlattığını doğru yorumlamayı sağlar. Örneğin bir deponun su hacminin zamana göre türevi $-5$ litre bölü dakika ise depo dakikada $5$ litre boşalmaktadır; eksi işaret azalmayı gösterir.",
        ]},
        {"baslik": "Türevin tanımı", "icerik": [
            "Yukarıdaki fikir genel olarak şöyle yazılır. Limit varsa $f$, $a$ noktasında türevlidir ve bu limite $f$ nin $a$ daki türevi denir:",
            "$$f'(a)=\\lim_{h \\to 0}\\dfrac{f(a+h)-f(a)}{h}$$",
            "Tanımdaki kesir her zaman $\\dfrac{0}{0}$ belirsizliği verir; türev hesabı bu belirsizliği çözmektir. Tanımla türev almanın ayrıntıları ve örnekleri <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Türevin gösterimleri", "icerik": [
            "Türev için farklı alanlarda farklı gösterimler kullanılır. Hepsi aynı kavramı anlatır:",
            tablo(["Gösterim", "Okunuşu", "Nerede kullanılır?"], [
                ["$f'(x)$", "f üssü x", "Fonksiyon dilinde"],
                ["$y'$", "y üssü", "Denklem dilinde"],
                ["$\\dfrac{dy}{dx}$", "dy bölü dx", "Değişim oranı vurgusu"],
            ]),
            "$\\dfrac{dy}{dx}$ gösterimi türevin bir oran olduğunu hatırlatır: $y$ deki çok küçük değişimin $x$ teki çok küçük değişime oranı. Özellikle zincir kuralında ve uygulama problemlerinde bu gösterim işi kolaylaştırır.",
        ]},
        {"baslik": "Geometrik anlam: teğetin eğimi", "icerik": [
            "Bir eğri üzerindeki iki noktadan geçen kesen, noktalardan biri diğerine yaklaştırıldıkça o noktadaki teğete dönüşür. Kesenin eğimi ortalama değişim hızı, teğetin eğimi ise türevdir.",
            koordinat_grafik("y = x² eğrisi ve (1, 1) noktasındaki teğeti", [("y = x²", lambda x: x * x), ("teğet: y = 2x - 1", lambda x: 2 * x - 1)],
                             (-2, 3), (-2, 5), adim=1, noktalar=[(1, 1, "", True)]),
            "Grafikte $y=x^2$ eğrisine $(1, 1)$ noktasında teğet olan doğru çizilmiştir. Doğrunun eğimi $2$ dir; bu da fonksiyonun $1$ deki türevidir. Teğet, eğriye o noktanın yakınında en iyi uyan doğrudur.",
        ]},
        {"baslik": "Temel türevler", "icerik": [
            "Türev tanımından elde edilen temel sonuçlar bir tabloda toplanır. Türev kuralları bu tabloyla birleştirilerek hemen her fonksiyonun türevi alınır:",
            tablo(["Fonksiyon", "Türevi"], [
                ["$c$ (sabit)", "$0$"],
                ["$x^n$", "$n x^{n-1}$"],
                ["$\\sin x$", "$\\cos x$"],
                ["$\\cos x$", "$-\\sin x$"],
                ["$e^x$", "$e^x$"],
                ["$\\ln x$", "$\\dfrac{1}{x}$"],
            ]),
            "Sabitin türevinin sıfır olması, sabit bir fonksiyonun hiç değişmemesinden gelir; grafiği yatay bir doğrudur ve eğimi sıfırdır.",
        ]},
        {"baslik": "Kuvvet kuralı", "icerik": [
            "$x^n$ biçimindeki fonksiyonların türevi, üs katsayı olarak öne alınıp üs bir azaltılarak bulunur. Kural kesirli ve negatif üsler için de geçerlidir; bu yüzden kökler ve kesirler önce üslü biçime çevrilir.",
            ornek(
                "$f(x)=x^5$ ve $g(x)=\\sqrt{x}$ fonksiyonları verilsin.",
                "Türevlerini ve $f'(2)$ değerini bulalım.",
                "$f'(x)=5x^4$ olur; $f'(2)=5 \\cdot 16=80$.",
                "$g(x)=x^{1/2}$ olduğundan $g'(x)=\\dfrac{1}{2}x^{-1/2}=\\dfrac{1}{2\\sqrt{x}}$ olur."),
        ]},
        {"baslik": "Negatif ve kesirli üsler", "icerik": [
            "Paydada $x$ bulunan ifadeler negatif üslü, kökler ise kesirli üslü yazılınca kuvvet kuralı doğrudan uygulanır. Türev alındıktan sonra sonuç istenirse yeniden kesir ya da kök biçimine çevrilir.",
            ornek(
                "$f(x)=\\dfrac{1}{x^2}$ ve $g(x)=\\sqrt[3]{x^2}$ fonksiyonları verilsin.",
                "$f'(1)$ ve $g'(8)$ değerlerini bulalım.",
                "$f(x)=x^{-2}$ olduğundan $f'(x)=-2x^{-3}$ ve $f'(1)=-2$ olur.",
                "$g(x)=x^{2/3}$ olduğundan $g'(x)=\\dfrac{2}{3}x^{-1/3}$ ve $g'(8)=\\dfrac{2}{3} \\cdot \\dfrac{1}{2}=\\dfrac{1}{3}$ olur."),
        ]},
        {"baslik": "Trigonometrik, üstel ve logaritmik türevler", "icerik": [
            "Temel türev tablosu toplam ve sabitle çarpım kurallarıyla birleştirilince trigonometrik, üstel ve logaritmik ifadelerin türevleri de terim terim alınır.",
            ornek(
                "$f(x)=2\\sin x+3\\cos x$ ve $g(x)=e^x+\\ln x$ fonksiyonları verilsin.",
                "$f'(0)$ ve $g'(1)$ değerlerini bulalım.",
                "$f'(x)=2\\cos x-3\\sin x$ olduğundan $f'(0)=2$ olur.",
                "$g'(x)=e^x+\\dfrac{1}{x}$ olduğundan $g'(1)=e+1$ olur."),
        ]},
        {"baslik": "Toplam ve sabitle çarpım", "icerik": [
            "Toplamın türevi türevlerin toplamıdır ve sabit bir katsayı türevin dışına çıkar. Bu iki kural sayesinde polinomların türevi terim terim alınır.",
            ornek(
                "$f(x)=3x^2-4x+7$ fonksiyonu verilsin.",
                "Türevini ve $f'(1)$ değerini bulalım.",
                "Terim terim türev alınır: $f'(x)=6x-4$.",
                "$f'(1)=2$ olur."),
            "Kuralların tamamı ve daha karmaşık örnekler için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Çarpım, bölüm ve zincir", "icerik": [
            "Çarpım, bölüm ve bileşke fonksiyonların türevleri için ayrı kurallar vardır. Bu kurallar, türevin toplam gibi kolayca dağılmadığını gösterir: çarpımın türevi türevlerin çarpımı değildir.",
            tablo(["Kural", "Formül", "Ayrıntı"], [
                ["Çarpım", "$(fg)'=f'g+fg'$", "<a href=\"/blog/carpimin-turevi/\">Çarpımın Türevi</a>"],
                ["Bölüm", "$\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f'g-fg'}{g^2}$", "<a href=\"/blog/bolumun-turevi/\">Bölümün Türevi</a>"],
                ["Zincir", "$(f(g(x)))'=f'(g(x)) \\cdot g'(x)$", "<a href=\"/blog/zincir-kurali/\">Zincir Kuralı</a>"],
            ]),
        ]},
        {"baslik": "Bir noktadaki türev değeri", "icerik": [
            "Bir noktadaki türev değeri, önce türev fonksiyonu bulunup sonra noktanın yerine yazılmasıyla hesaplanır. Bu değer, o noktadaki teğetin eğimi ve fonksiyonun o andaki değişim hızıdır.",
            ornek(
                "$f(x)=x^3-3x$ fonksiyonu verilsin.",
                "$f'(2)$ değerini bulalım.",
                "$f'(x)=3x^2-3$ olur.",
                "$f'(2)=12-3=9$ bulunur; fonksiyon $x=2$ de hızla artmaktadır."),
        ]},
        {"baslik": "Teğet doğrusunun denklemi", "icerik": [
            "Türev, teğetin eğimini verdiği için teğet doğrusunun denklemi doğrudan yazılır: $(a, f(a))$ noktasından geçen ve eğimi $f'(a)$ olan doğru $y-f(a)=f'(a)(x-a)$ dır.",
            ornek(
                "$f(x)=x^2$ eğrisi ve $(1, 1)$ noktası verilsin.",
                "Teğet denklemini bulalım.",
                "Eğim $f'(1)=2$ dir.",
                "Teğet $y-1=2(x-1)$, yani $y=2x-1$ olur; grafikteki doğru budur."),
            "Teğet ve normal denklemleri için daha fazla örnek <a href=\"/blog/teget-denklemi/\">Türevde Teğet Denklemi Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Yatay teğet", "icerik": [
            "Türevin sıfır olduğu noktalarda teğet yataydır. Bu noktalar, grafiğin tepe ve çukur noktalarının adaylarıdır ve türevin en önemli uygulamalarının başlangıcıdır. Türevi sıfır yapan noktalara kritik nokta ya da durağan nokta denir; fonksiyon bu noktalarda bir an için ne artar ne azalır.",
            ornek(
                "$f(x)=x^3-3x$ fonksiyonu verilsin.",
                "Teğetin yatay olduğu noktaları bulalım.",
                "$f'(x)=3x^2-3=0$ ise $x^2=1$ olur.",
                "Teğet $x=-1$ ve $x=1$ de yataydır; bu noktalar $(-1, 2)$ ve $(1, -2)$ dir."),
        ]},
        {"baslik": "Artan, azalan ve ekstremum", "icerik": [
            "Türevin işareti fonksiyonun davranışını söyler: türev pozitifse fonksiyon artar, negatifse azalır. Türevin işaret değiştirdiği yerlerde fonksiyon yerel en büyük ya da en küçük değerini alır.",
            tablo(["Türev", "Fonksiyon"], [
                ["$f'(x)>0$", "Artan"],
                ["$f'(x)<0$", "Azalan"],
                ["$f'$ artıdan eksiye geçer", "Yerel maksimum"],
                ["$f'$ eksiden artıya geçer", "Yerel minimum"],
            ]),
            "$x^3-3x$ örneğinde türev $x=-1$ de artıdan eksiye, $x=1$ de eksiden artıya geçer; bu yüzden $x=-1$ de yerel maksimum, $x=1$ de yerel minimum vardır. Ayrıntılar <a href=\"/blog/artan-azalan-fonksiyonlar/\">Türevde Artan ve Azalan Fonksiyonlar</a> ve <a href=\"/blog/maksimum-minimum/\">Türevde Maksimum ve Minimum Nasıl Bulunur?</a> yazılarında.",
        ]},
        {"baslik": "Hız ve ivme", "icerik": [
            "Konumun zamana göre türevi hızı, hızın zamana göre türevi ivmeyi verir. Türevin fizikteki en doğrudan uygulaması budur. Hızın işareti hareketin yönünü, sıfır olduğu anlar ise cismin durup yön değiştirebileceği anları gösterir.",
            ornek(
                "Bir cismin konumu $s(t)=t^3-6t^2+9t$ metre olsun.",
                "Cismin durduğu anları ve ivmenin sıfır olduğu anı bulalım.",
                "Hız $v(t)=3t^2-12t+9=3(t-1)(t-3)$ tür; cisim $t=1$ ve $t=3$ saniyelerde durur.",
                "İvme $a(t)=6t-12$ dir ve $t=2$ saniyede sıfır olur."),
        ]},
        {"baslik": "İkinci türev", "icerik": [
            "Türevin türevine ikinci türev denir ve $f''(x)$ ile gösterilir. İkinci türev, değişim hızının kendisinin nasıl değiştiğini ölçer; hareket probleminde ivmeye karşılık gelir.",
            ornek(
                "$f(x)=x^4$ fonksiyonu verilsin.",
                "İkinci türevi ve $f''(1)$ değerini bulalım.",
                "$f'(x)=4x^3$ ve $f''(x)=12x^2$ olur.",
                "$f''(1)=12$ bulunur."),
            "İkinci türevin işareti grafiğin eğriliğini de gösterir: pozitifse grafik yukarı doğru bükülür, negatifse aşağı doğru bükülür.",
        ]},
        {"baslik": "Yüksek mertebeden türevler", "icerik": [
            "Türev alma işlemi tekrarlanabilir: üçüncü türev $f^{(3)}$, dördüncü türev ise $f^{(4)}$ ile gösterilir. Polinomlarda her türev derecenin bir azalmasına yol açtığı için yeterince türev alınınca sonuç sıfır olur.",
            ornek(
                "$f(x)=x^3$ ve $g(x)=\\sin x$ fonksiyonları verilsin.",
                "$f^{(3)}(x)$ ve $g$ nin dördüncü türevini bulalım.",
                "$f'(x)=3x^2$, $f''(x)=6x$ ve $f^{(3)}(x)=6$ olur; dördüncü türev $0$ dır.",
                "Sinüsün türevleri $\\cos x$, $-\\sin x$, $-\\cos x$ ve $\\sin x$ olur; dördüncü türev fonksiyonun kendisine döner."),
        ]},
        {"baslik": "Türevlenebilirlik", "icerik": [
            "Her sürekli fonksiyon türevli değildir. Grafiğin köşe yaptığı, dikey teğetinin olduğu ya da koptuğu noktalarda türev yoktur. $|x|$ fonksiyonu sıfırda süreklidir ama köşe yapar: soldan eğim $-1$, sağdan eğim $1$ dir.",
            tablo(["Durum", "Sürekli mi?", "Türevli mi?"], [
                ["Pürüzsüz eğri", "Evet", "Evet"],
                ["Köşe, örneğin $|x|$ te $0$", "Evet", "Hayır"],
                ["Sıçrama ya da boşluk", "Hayır", "Hayır"],
            ]),
            hap("Türevli olan her fonksiyon süreklidir.",
                "Sürekli olan her fonksiyon türevli değildir."),
        ]},
        {"baslik": "Parçalı fonksiyonda türev", "icerik": [
            "Parçalı bir fonksiyonun kritik noktada türevli olması için önce orada sürekli olması, sonra soldan ve sağdan türevlerin eşit olması gerekir. Her yönün türevi kendi parçasından hesaplanır.",
            ornek(
                "$x<1$ için $f(x)=x^2$, $x \\ge 1$ için $f(x)=2x-1$ olsun.",
                "$x=1$ de türevli olup olmadığını inceleyelim.",
                "Süreklilik: soldan $1$, sağdan $2 \\cdot 1-1=1$; fonksiyon süreklidir.",
                "Soldan türev $2x$ ten $2$, sağdan türev $2$ dir; eşit oldukları için $f'(1)=2$ vardır."),
        ]},
        {"baslik": "Uygulama: dairenin alanı", "icerik": [
            "Türev, bir niceliğin başka bir niceliğe göre değişim oranıdır. Dairenin alanı yarıçapa bağlıdır ve alanın yarıçapa göre türevi ilginç bir sonuç verir.",
            ornek(
                "Dairenin alanı $A(r)=\\pi r^2$ olsun.",
                "Alanın yarıçapa göre türevini bulalım.",
                "$A'(r)=2\\pi r$ olur.",
                "Bu, dairenin çevresidir: yarıçap çok az artınca alana çevre uzunluğunda ince bir şerit eklenir."),
        ]},
        {"baslik": "Uygulama: küpün hacmi", "icerik": [
            "Bir küpün hacmi kenar uzunluğuna bağlıdır: $V(a)=a^3$. Hacmin kenara göre türevi, kenar çok az uzatıldığında hacmin ne hızla arttığını gösterir.",
            ornek(
                "Kenarı $a$ olan bir küp verilsin.",
                "Hacmin kenara göre değişim hızını ve $a=2$ deki değerini bulalım.",
                "$V'(a)=3a^2$ olur; bu, küpün yüzey alanının yarısıdır.",
                "$a=2$ için değişim hızı $12$ birimküp bölü birimdir."),
        ]},
        {"baslik": "Uygulama: doğrusal yaklaşım", "icerik": [
            "Teğet doğrusu, eğriye dokunduğu noktanın yakınında eğriye çok yakındır. Bu yüzden hesaplaması zor değerler teğet yardımıyla yaklaşık bulunabilir: $f(x) \\approx f(a)+f'(a)(x-a)$.",
            ornek(
                "$\\sqrt{4.1}$ değeri istensin.",
                "Doğrusal yaklaşımla bulalım.",
                "$f(x)=\\sqrt{x}$ için $f(4)=2$ ve $f'(4)=\\dfrac{1}{4}$ dir.",
                "$\\sqrt{4.1} \\approx 2+\\dfrac{1}{4} \\cdot 0.1=2.025$ olur; gerçek değer yaklaşık $2.0248$ dir."),
        ]},
        {"baslik": "Uygulama: marjinal maliyet", "icerik": [
            "Ekonomide maliyetin üretim miktarına göre türevine marjinal maliyet denir. Bir birim daha üretmenin yaklaşık ek maliyetini verir.",
            ornek(
                "$x$ birim üretimin maliyeti $C(x)=100+5x+0.01x^2$ TL olsun.",
                "$100$ birim üretimdeki marjinal maliyeti bulalım.",
                "$C'(x)=5+0.02x$ olur.",
                "$C'(100)=7$ TL bulunur; yüz birinci birimin ek maliyeti yaklaşık $7$ TL dir."),
        ]},
        {"baslik": "Türev konularının haritası", "icerik": [
            "Türev konusu birbirine bağlı birkaç adımdan oluşur ve her adım bir öncekine dayanır. Önerilen çalışma sırası şöyledir:",
            tablo(["Adım", "Konu"], [
                ["1", "<a href=\"/blog/turevin-tanimi/\">Türevin tanımı</a>"],
                ["2", "<a href=\"/blog/turev-alma-kurallari/\">Türev alma kuralları</a>"],
                ["3", "<a href=\"/blog/carpimin-turevi/\">Çarpımın</a> ve <a href=\"/blog/bolumun-turevi/\">bölümün türevi</a>"],
                ["4", "<a href=\"/blog/zincir-kurali/\">Zincir kuralı</a>"],
                ["5", "<a href=\"/blog/teget-denklemi/\">Teğet denklemi</a>"],
                ["6", "<a href=\"/blog/artan-azalan-fonksiyonlar/\">Artan ve azalan fonksiyonlar</a>"],
                ["7", "<a href=\"/blog/maksimum-minimum/\">Maksimum ve minimum</a>"],
            ]),
        ]},
        {"baslik": "Sınavda türev", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) türev; türev alma, bir noktadaki türev değeri, teğet denklemi, artan ve azalan aralıklar, ekstremum noktaları, optimizasyon ve hız ivme problemleri biçiminde karşına çıkabilir.",
                "Türev, AYT matematiğinde en çok soru gelen konulardan biridir."),
            "Türev sorusunda önce ne istendiğini belirle: bir sayı mı, bir doğru mu, bir aralık mı? Türev değeri istenirse türevi alıp yerine yaz; teğet istenirse eğimi türevden, noktayı fonksiyondan bul; aralık istenirse türevin işaret tablosunu yap.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$(x^n)'=x^{n-1}$ yazmak", "$(x^n)'=nx^{n-1}$"],
                ["Sabitin türevini sabit sanmak", "Sabitin türevi $0$"],
                ["$(fg)'=f'g'$ yazmak", "$(fg)'=f'g+fg'$"],
                ["$f'(a)$ yerine $f(a)$ yı eğim almak", "Eğim türevdir"],
                ["Sürekli fonksiyonu her yerde türevli sanmak", "Köşelerde türev yok"],
                ["$\\sqrt{x}$ i üslü yazmadan türev almak", "$x^{1/2}$ olarak yazılır"],
            ]),
            "Türev hatalarının çoğu kuralı bir sayıyla denemeden uygulamaktan doğar. Şüpheye düşüldüğünde türevi tanımla ya da basit bir fonksiyonla kontrol etmek doğru kuralı hatırlatır.",
        ]},
    ],
    "sss": [
        ("Türev nedir?",
         "Bir fonksiyonun bir noktadaki anlık değişim hızıdır. Geometrik olarak grafiğin o noktadaki teğetinin eğimidir."),
        ("Türev nasıl hesaplanır?",
         "Tanım olarak f(a + h) eksi f(a) bölü h ifadesinin h sıfıra giderken limitidir. Pratikte temel türevler ve türev kurallarıyla hesaplanır."),
        ("x üzeri n in türevi nedir?",
         "n çarpı x üzeri n eksi 1 dir. Örneğin x üzeri 5 in türevi 5 x üzeri 4 tür."),
        ("Türev sıfır olursa ne anlama gelir?",
         "O noktada teğet yataydır. Bu noktalar fonksiyonun yerel maksimum ya da minimum noktalarının adaylarıdır."),
        ("Her sürekli fonksiyon türevli midir?",
         "Hayır. Mutlak değer fonksiyonu sıfırda süreklidir ama köşe yaptığı için türevi yoktur. Buna karşın türevli her fonksiyon süreklidir."),
        ("İkinci türev ne işe yarar?",
         "Değişim hızının değişimini ölçer. Harekette ivmeyi verir, grafikte eğriliğin yönünü gösterir."),
        ("Türevin birimi nedir?",
         "Fonksiyonun biriminin değişkenin birimine bölümüdür. Konumun zamana göre türevi olan hızın birimi metre bölü saniyedir."),
    ],
    "kontrol": [
        "Ortalama ve anlık değişim hızını ayırt edebiliyorum.",
        "Türevin limitle tanımını açıklayabiliyorum.",
        "Türevin gösterimlerini tanıyıp kullanabiliyorum.",
        "Türevin teğetin eğimi olduğunu açıklayabiliyorum.",
        "Temel fonksiyonların türevlerini biliyorum.",
        "Kuvvet, toplam ve sabitle çarpım kurallarını uygulayabiliyorum.",
        "Bir noktadaki türev değerini ve teğet denklemini bulabiliyorum.",
        "Hız, ivme ve ikinci türevi hesaplayabiliyorum.",
        "Türevlenebilirlik ile süreklilik arasındaki ilişkiyi açıklayabiliyorum.",
        "Türevi alan ve maliyet gibi uygulamalarda kullanabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["turevin-tanimi", "turev-alma-kurallari", "limit-konu-anlatimi"],
}
