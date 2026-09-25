# scripts/yazilar/24_trigonometrik_toplam_fark.py — Trigonometrik Toplam ve Fark Formulleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "trigonometrik-toplam-fark",
    "baslik": "Trigonometrik Toplam ve Fark Formülleri",
    "aciklama": "Trigonometrik toplam ve fark formülleri nedir, nereden gelir? İspat, özel olmayan açıların değeri, formülü tersten tanıma, üçgen ve doğrular arası açı; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "trigonometrik-toplam-fark",
    "kapak_alt": "Trigonometrik toplam ve fark formülleri: mavi ve kırmızı açı dilimlerini ahşap diskler üzerinde birleştirip ayıran iki öğrenci",
    "ozet": "Trigonometrik toplam ve fark formülleri, iki açının toplamının ya da farkının sinüs, kosinüs ve tanjantını açıların kendi değerleriyle hesaplamayı sağlar. Bu formüller sayesinde 15, 75 ya da 105 derece gibi özel olmayan açıların tam değeri bulunur. Bu yazıda formüllerin birim çemberden ispatını, diğer formüllerin türetilmesini, değer hesaplamayı, bölgesi verilen açılarla çalışmayı, formülü tersten tanımayı, özdeşlik ispatlarını, üçgende ve iki doğru arasındaki açıda kullanımı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Toplam ve fark formülleri ne işe yarar?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için özel açıların değerlerini, birim çemberi ve temel özdeşliği biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/birim-cember/\">Birim Çember Konu Anlatımı</a> ve <a href=\"/blog/trigonometrik-ozdeslikler-formuller/\">Trigonometrik Özdeşlikler ve Formüller</a> yazılarına göz at."),
            "Özel açılar olan $30^\\circ$, $45^\\circ$ ve $60^\\circ$ nin değerleri ezbere bilinir. Peki $75^\\circ$ ya da $15^\\circ$ gibi açılar? Bu açılar özel açıların toplamı ya da farkı olarak yazılabilir: $75^\\circ=45^\\circ+30^\\circ$ ve $15^\\circ=45^\\circ-30^\\circ$. Toplam ve fark formülleri, bu yazılışı değer hesabına dönüştüren araçlardır.",
            "Kapaktaki öğrenciler mavi ve kırmızı iki açı dilimini ahşap bir disk üzerinde yan yana koyarak birleştiriyor, sonra birini diğerinden çıkararak ayırıyor. Formüller tam olarak bu iki işlemin trigonometrik karşılığıdır: birleşen açının değeri, parçaların değerlerinden hesaplanır.",
        ]},
        {"baslik": "Formüllerin listesi", "icerik": [
            "Altı formül üç çift hâlinde öğrenilir. Her çiftte toplam ve fark formülü yalnızca işaretlerle ayrılır:",
            tablo(["Formül", "Açılımı"], [
                ["$\\sin(a+b)$", "$\\sin a \\cos b+\\cos a \\sin b$"],
                ["$\\sin(a-b)$", "$\\sin a \\cos b-\\cos a \\sin b$"],
                ["$\\cos(a+b)$", "$\\cos a \\cos b-\\sin a \\sin b$"],
                ["$\\cos(a-b)$", "$\\cos a \\cos b+\\sin a \\sin b$"],
                ["$\\tan(a+b)$", "$\\dfrac{\\tan a+\\tan b}{1-\\tan a \\tan b}$"],
                ["$\\tan(a-b)$", "$\\dfrac{\\tan a-\\tan b}{1+\\tan a \\tan b}$"],
            ]),
            hap("Sinüste işaret korunur: toplamda artı, farkta eksi.",
                "Kosinüste işaret ters döner: toplamda eksi, farkta artı."),
        ]},
        {"baslik": "Kosinüs fark formülünün ispatı", "icerik": [
            "Formüllerin hepsi tek bir formülden türetilebilir: kosinüs fark formülü. Birim çember üzerinde $P(\\cos a, \\sin a)$ ve $Q(\\cos b, \\sin b)$ noktalarını düşün. Bu iki nokta arasındaki merkez açısı $a-b$ dir.",
            "İki nokta arasındaki uzaklığın karesi koordinatlarla hesaplanırsa $(\\cos a-\\cos b)^2+(\\sin a-\\sin b)^2$ bulunur. Açılıp temel özdeşlik kullanılınca bu ifade $2-2(\\cos a \\cos b+\\sin a \\sin b)$ olur.",
            "Şimdi çemberi, $Q$ noktası $(1, 0)$ a gelecek biçimde döndürelim. Uzaklık değişmez; $P$ ise $(\\cos(a-b), \\sin(a-b))$ noktasına gelir. Bu kez uzaklığın karesi $2-2\\cos(a-b)$ çıkar. İki sonuç eşitlenince formül elde edilir:",
            "$$\\cos(a-b)=\\cos a \\cos b+\\sin a \\sin b$$",
        ]},
        {"baslik": "Diğer formüllerin türetilmesi", "icerik": [
            "Kosinüs fark formülünde $b$ yerine $-b$ yazılırsa, kosinüsün çift ve sinüsün tek fonksiyon olması sayesinde $\\cos(a+b)=\\cos a \\cos b-\\sin a \\sin b$ elde edilir.",
            "Sinüs için tümler açı kuralı kullanılır: $\\sin(a+b)=\\cos\\left(90^\\circ-(a+b)\\right)=\\cos\\left((90^\\circ-a)-b\\right)$. Bu ifadeye kosinüs fark formülü uygulanınca $\\sin a \\cos b+\\cos a \\sin b$ çıkar. Sinüs fark formülü de yine $b$ yerine $-b$ yazılarak bulunur.",
            "Bu türetme zinciri, altı formülü ayrı ayrı ezberlemek yerine tek bir fikirden kurmayı sağlar. Sınavda bir işaret akla takılırsa zincirin bir halkasını yeniden yapmak birkaç saniye sürer.",
        ]},
        {"baslik": "Tanjant formülünün türetilmesi", "icerik": [
            "Tanjant toplam formülü, sinüs ve kosinüs toplam formüllerinin oranından gelir. $\\tan(a+b)=\\dfrac{\\sin a \\cos b+\\cos a \\sin b}{\\cos a \\cos b-\\sin a \\sin b}$ kesrinin payı ve paydası $\\cos a \\cos b$ ye bölünür.",
            "Paydaki iki terim $\\tan a$ ve $\\tan b$ ye, paydadaki terimler ise $1$ ve $\\tan a \\tan b$ ye dönüşür. Sonuç $\\dfrac{\\tan a+\\tan b}{1-\\tan a \\tan b}$ formülüdür. Payda sıfır olduğunda, yani $\\tan a \\tan b=1$ iken toplam açının tanjantı tanımsızdır; bu durumda $a+b$ açısı $90^\\circ$ nin tek katıdır.",
        ]},
        {"baslik": "Özel olmayan açıların sinüsü", "icerik": [
            "Özel olmayan bir açının sinüsünü bulmak için açı, iki özel açının toplamı ya da farkı olarak yazılır. Genellikle $30^\\circ$, $45^\\circ$, $60^\\circ$ ve $90^\\circ$ açılarından ikisi yeterlidir.",
            ornek(
                "$\\sin 105^\\circ$ ve $\\sin 15^\\circ$ değerleri istensin.",
                "Toplam ve fark formülleriyle bulalım.",
                "$\\sin 105^\\circ=\\sin(60^\\circ+45^\\circ)=\\dfrac{\\sqrt{3}}{2} \\cdot \\dfrac{\\sqrt{2}}{2}+\\dfrac{1}{2} \\cdot \\dfrac{\\sqrt{2}}{2}=\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$.",
                "$\\sin 15^\\circ=\\sin(45^\\circ-30^\\circ)=\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2}-\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{1}{2}=\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$."),
            "$\\sin 105^\\circ$ ile $\\sin 75^\\circ$ aynı çıkar; çünkü iki açı bütünlerdir ve bütünler açıların sinüsleri eşittir.",
        ]},
        {"baslik": "Özel olmayan açıların kosinüsü", "icerik": [
            "Kosinüs hesabında formüldeki işaretin ters döndüğünü unutmamak gerekir. Toplam açının kosinüsünde iki çarpım arasına eksi, fark açısının kosinüsünde artı gelir.",
            ornek(
                "$\\cos 75^\\circ$ ve $\\cos 105^\\circ$ değerleri istensin.",
                "Toplam formülüyle bulalım.",
                "$\\cos 75^\\circ=\\cos(45^\\circ+30^\\circ)=\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2}-\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{1}{2}=\\dfrac{\\sqrt{6}-\\sqrt{2}}{4}$.",
                "$\\cos 105^\\circ=\\cos(60^\\circ+45^\\circ)=\\dfrac{1}{2} \\cdot \\dfrac{\\sqrt{2}}{2}-\\dfrac{\\sqrt{3}}{2} \\cdot \\dfrac{\\sqrt{2}}{2}=\\dfrac{\\sqrt{2}-\\sqrt{6}}{4}$."),
            "$\\cos 105^\\circ$ negatif çıktı; bu beklenen bir sonuçtur, çünkü $105^\\circ$ ikinci bölgededir ve orada kosinüs negatiftir. Sonucun işaretini bölgeyle karşılaştırmak hesabı denetlemenin en hızlı yoludur.",
        ]},
        {"baslik": "Özel olmayan açıların tanjantı", "icerik": [
            "Tanjant hesabında karekökler paydada kalır; sonuç genellikle payda eşleniğiyle genişletilerek sadeleştirilir.",
            ornek(
                "$\\tan 75^\\circ$ değeri istensin.",
                "Tanjant toplam formülüyle bulalım.",
                "$\\tan 75^\\circ=\\dfrac{\\tan 45^\\circ+\\tan 30^\\circ}{1-\\tan 45^\\circ \\tan 30^\\circ}=\\dfrac{1+\\dfrac{\\sqrt{3}}{3}}{1-\\dfrac{\\sqrt{3}}{3}}=\\dfrac{3+\\sqrt{3}}{3-\\sqrt{3}}$.",
                "Eşlenikle genişletilince $\\dfrac{(3+\\sqrt{3})^2}{9-3}=\\dfrac{12+6\\sqrt{3}}{6}=2+\\sqrt{3}$ olur."),
            "$\\tan 105^\\circ$ ise $-(2+\\sqrt{3})$ tür; çünkü $105^\\circ$ ile $75^\\circ$ bütünlerdir ve bütünler açıların tanjantları ters işaretlidir. $\\tan 15^\\circ$ ise $2-\\sqrt{3}$ tür ve $\\tan 75^\\circ$ ile çarpımı $1$ dir; iki açı tümler olduğu için bu da beklenen sonuçtur.",
        ]},
        {"baslik": "Radyanla verilen açılar", "icerik": [
            "Açı radyanla verildiğinde de aynı yol izlenir. $\\dfrac{\\pi}{12}$ radyan $15^\\circ$ ye, $\\dfrac{7\\pi}{12}$ radyan ise $105^\\circ$ ye karşılık gelir. Radyanlı yazımda özel açılar $\\dfrac{\\pi}{6}$, $\\dfrac{\\pi}{4}$ ve $\\dfrac{\\pi}{3}$ dir.",
            ornek(
                "$\\cos \\dfrac{7\\pi}{12}$ değeri istensin.",
                "Değeri bulalım.",
                "$\\dfrac{7\\pi}{12}=\\dfrac{\\pi}{3}+\\dfrac{\\pi}{4}$ olarak yazılır.",
                "$\\cos \\dfrac{\\pi}{3} \\cos \\dfrac{\\pi}{4}-\\sin \\dfrac{\\pi}{3} \\sin \\dfrac{\\pi}{4}=\\dfrac{\\sqrt{2}-\\sqrt{6}}{4}$ olur."),
        ]},
        {"baslik": "Verilen oranlardan hesap", "icerik": [
            "Sorularda açılar çoğu zaman doğrudan verilmez; bunun yerine birer trigonometrik oranları verilir. Bu durumda önce her açının eksik oranı temel özdeşlikle ya da bir dik üçgenle bulunur, sonra formül uygulanır.",
            ornek(
                "$a$ ve $b$ dar açılar, $\\sin a=\\dfrac{3}{5}$ ve $\\cos b=\\dfrac{5}{13}$ olsun.",
                "$\\sin(a+b)$ ve $\\cos(a+b)$ değerlerini bulalım.",
                "Eksik oranlar: $\\cos a=\\dfrac{4}{5}$ ve $\\sin b=\\dfrac{12}{13}$. $\\sin(a+b)=\\dfrac{3}{5} \\cdot \\dfrac{5}{13}+\\dfrac{4}{5} \\cdot \\dfrac{12}{13}=\\dfrac{63}{65}$.",
                "$\\cos(a+b)=\\dfrac{4}{5} \\cdot \\dfrac{5}{13}-\\dfrac{3}{5} \\cdot \\dfrac{12}{13}=-\\dfrac{16}{65}$ olur."),
            "Kosinüsün negatif çıkması, $a+b$ toplamının $90^\\circ$ den büyük olduğunu gösterir. Aynı veriyle $\\sin(a-b)=-\\dfrac{33}{65}$ ve $\\cos(a-b)=\\dfrac{56}{65}$ bulunur; sinüsün negatif olması da $b$ nin $a$ dan büyük olduğunu anlatır.",
        ]},
        {"baslik": "Bölgesi verilen açılar", "icerik": [
            "Açılardan biri ikinci, üçüncü ya da dördüncü bölgedeyse eksik oranın işareti bölgeden seçilir. Karekök alınırken işaret atlanırsa formül doğru uygulansa bile sonuç yanlış çıkar.",
            ornek(
                "$a$ ikinci bölgede ve $\\sin a=\\dfrac{4}{5}$; $b$ dar açı ve $\\sin b=\\dfrac{5}{13}$ olsun.",
                "$\\cos(a+b)$ değerini bulalım.",
                "İkinci bölgede kosinüs negatiftir: $\\cos a=-\\dfrac{3}{5}$. Ayrıca $\\cos b=\\dfrac{12}{13}$.",
                "$\\cos(a+b)=\\left(-\\dfrac{3}{5}\\right) \\cdot \\dfrac{12}{13}-\\dfrac{4}{5} \\cdot \\dfrac{5}{13}=-\\dfrac{56}{65}$ olur."),
        ]},
        {"baslik": "Formülü tersten tanımak", "icerik": [
            "Sınav sorularının önemli bir kısmında formül açılmış hâlde verilir ve toplu hâline getirilmesi beklenir. $\\sin x \\cos y+\\cos x \\sin y$ biçimini gören öğrenci bunun $\\sin(x+y)$ olduğunu tanımalıdır.",
            ornek(
                "$\\sin 50^\\circ \\cos 10^\\circ+\\cos 50^\\circ \\sin 10^\\circ$ ve $\\cos 70^\\circ \\cos 10^\\circ+\\sin 70^\\circ \\sin 10^\\circ$ ifadeleri verilsin.",
                "İfadelerin değerini bulalım.",
                "Birincisi sinüs toplam formülüdür: $\\sin(50^\\circ+10^\\circ)=\\sin 60^\\circ=\\dfrac{\\sqrt{3}}{2}$.",
                "İkincisi kosinüs fark formülüdür: $\\cos(70^\\circ-10^\\circ)=\\cos 60^\\circ=\\dfrac{1}{2}$."),
            "Tanımanın ipucu çarpımların düzenidir: sinüs formüllerinde her çarpımda bir sinüs ve bir kosinüs bulunur; kosinüs formüllerinde ise çarpımlardan biri iki kosinüsten, diğeri iki sinüsten oluşur.",
        ]},
        {"baslik": "Tanjant formülünü tersten tanımak", "icerik": [
            "Tanjant toplam formülünün biçimi de tanınmalıdır: payda iki tanjantın toplamı, paydada $1$ eksi aynı tanjantların çarpımı varsa ifade toplam açının tanjantıdır.",
            ornek(
                "$\\dfrac{\\tan 20^\\circ+\\tan 25^\\circ}{1-\\tan 20^\\circ \\tan 25^\\circ}$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "İfade $\\tan(20^\\circ+25^\\circ)$ biçimindedir.",
                "$\\tan 45^\\circ=1$ olur."),
            "Bu sonuçtan ilginç bir kural çıkar: toplamı $45^\\circ$ olan iki açı için $(1+\\tan a)(1+\\tan b)=2$ dir. Formüldeki eşitlik $\\tan a+\\tan b=1-\\tan a \\tan b$ biçiminde yazılıp iki tarafa $1+\\tan a \\tan b$ eklenince bu çarpım elde edilir. Örneğin $(1+\\tan 20^\\circ)(1+\\tan 25^\\circ)=2$ olur.",
        ]},
        {"baslik": "Tanjantlardan açı bulmak", "icerik": [
            "İki açının tanjantı biliniyorsa toplamlarının tanjantı hesaplanır ve sonuç bir özel açıya karşılık geliyorsa toplam açı bulunur. Açıların aralığı mutlaka hesaba katılmalıdır.",
            ornek(
                "$a$ ve $b$ dar açılar, $\\tan a=\\dfrac{1}{2}$ ve $\\tan b=\\dfrac{1}{3}$ olsun.",
                "$a+b$ toplamını bulalım.",
                "$\\tan(a+b)=\\dfrac{\\dfrac{1}{2}+\\dfrac{1}{3}}{1-\\dfrac{1}{6}}=\\dfrac{\\dfrac{5}{6}}{\\dfrac{5}{6}}=1$.",
                "İki dar açının toplamı $0^\\circ$ ile $180^\\circ$ arasındadır ve tanjantı $1$ olan tek açı $45^\\circ$ dir."),
        ]},
        {"baslik": "Tümler açılarda tanjant çarpımı", "icerik": [
            "Toplamı $90^\\circ$ olan iki açının toplamının tanjantı tanımsızdır. Formülde paydanın sıfır olması gerektiği için $1-\\tan a \\tan b=0$, yani $\\tan a \\tan b=1$ olur. Bu sonuç, tümler açıların tanjantlarının birbirinin çarpmaya göre tersi olduğunu söyler.",
            ornek(
                "$\\tan 10^\\circ \\cdot \\tan 20^\\circ \\cdot \\tan 70^\\circ \\cdot \\tan 80^\\circ$ çarpımı verilsin.",
                "Çarpımın değerini bulalım.",
                "Çarpanlar tümler çiftler hâlinde gruplanır: $(\\tan 10^\\circ \\tan 80^\\circ)(\\tan 20^\\circ \\tan 70^\\circ)$.",
                "Her parantez $1$ e eşittir; çarpım $1$ olur."),
        ]},
        {"baslik": "Bütünler ve tümler kuralları", "icerik": [
            "Birim çemberden bilinen indirgeme kuralları aslında toplam ve fark formüllerinin özel hâlleridir. Açılardan biri $90^\\circ$ ya da $180^\\circ$ olduğunda sinüs ve kosinüsü $0$ ya da $\\pm 1$ olduğu için formülün bir terimi düşer.",
            ornek(
                "$\\sin(90^\\circ+x)$ ve $\\cos(180^\\circ-x)$ ifadeleri verilsin.",
                "Formüllerle sadeleştirelim.",
                "$\\sin(90^\\circ+x)=\\sin 90^\\circ \\cos x+\\cos 90^\\circ \\sin x=\\cos x$.",
                "$\\cos(180^\\circ-x)=\\cos 180^\\circ \\cos x+\\sin 180^\\circ \\sin x=-\\cos x$."),
        ]},
        {"baslik": "Toplam ve farkın çarpımı", "icerik": [
            "Toplam ve fark formülleri birlikte kullanılınca kısa ve kullanışlı özdeşlikler ortaya çıkar. Bunlardan en bilineni, sinüs toplamı ile sinüs farkının çarpımıdır.",
            ornek(
                "$\\sin(a+b) \\cdot \\sin(a-b)=\\sin^2 a-\\sin^2 b$ eşitliği verilsin.",
                "Eşitliğin özdeşlik olduğunu gösterelim.",
                "Sol taraf iki kare farkı biçimindedir: $\\sin^2 a \\cos^2 b-\\cos^2 a \\sin^2 b$.",
                "$\\cos^2 b=1-\\sin^2 b$ ve $\\cos^2 a=1-\\sin^2 a$ yazılınca çarpımlı terimler sadeleşir ve $\\sin^2 a-\\sin^2 b$ kalır."),
            "Benzer yolla $\\cos(a+b) \\cdot \\cos(a-b)=\\cos^2 a-\\sin^2 b$ özdeşliği de gösterilir. Örneğin $\\sin 75^\\circ \\sin 15^\\circ=\\sin^2 45^\\circ-\\sin^2 30^\\circ=\\dfrac{1}{2}-\\dfrac{1}{4}=\\dfrac{1}{4}$ olur.",
        ]},
        {"baslik": "İki terimi tek sinüse çevirmek", "icerik": [
            "$a\\sin x+b\\cos x$ biçimindeki bir ifade, sinüs toplam formülü tersten okunarak tek bir sinüs olarak yazılabilir. Önce ifade $\\sqrt{a^2+b^2}$ parantezine alınır, sonra katsayılar bir açının kosinüsü ve sinüsü olarak tanınır.",
            ornek(
                "$\\sqrt{3}\\sin x+\\cos x$ ifadesi verilsin.",
                "İfadeyi tek bir sinüs olarak yazalım.",
                "$\\sqrt{3+1}=2$: ifade $2\\left(\\dfrac{\\sqrt{3}}{2}\\sin x+\\dfrac{1}{2}\\cos x\\right)$ olur.",
                "$\\dfrac{\\sqrt{3}}{2}=\\cos 30^\\circ$ ve $\\dfrac{1}{2}=\\sin 30^\\circ$ olduğundan ifade $2\\sin(x+30^\\circ)$ olur."),
            "Bu yazılış ifadenin alabileceği değerleri de hemen gösterir: sinüs $-1$ ile $1$ arasında kaldığı için $\\sqrt{3}\\sin x+\\cos x$ en fazla $2$, en az $-2$ olur.",
        ]},
        {"baslik": "Fark biçimini tek sinüse çevirmek", "icerik": [
            "Katsayılardan biri negatif olduğunda aynı yöntem sinüs fark formülüyle uygulanır. Katsayıların karelerinin toplamının karekökü parantez dışına alınır ve içeride kalan sayılar bir özel açının kosinüsü ve sinüsü olarak okunur.",
            ornek(
                "$\\sin x-\\cos x$ ifadesi verilsin.",
                "İfadeyi tek bir sinüs olarak yazalım ve değer aralığını bulalım.",
                "$\\sqrt{1+1}=\\sqrt{2}$: ifade $\\sqrt{2}\\left(\\dfrac{\\sqrt{2}}{2}\\sin x-\\dfrac{\\sqrt{2}}{2}\\cos x\\right)$ olur.",
                "$\\dfrac{\\sqrt{2}}{2}=\\cos 45^\\circ=\\sin 45^\\circ$ olduğundan ifade $\\sqrt{2}\\sin(x-45^\\circ)$ olur ve $-\\sqrt{2}$ ile $\\sqrt{2}$ arasında değer alır."),
        ]},
        {"baslik": "Formülle denklem çözmek", "icerik": [
            "Denklemde açılmış bir toplam formülü görülüyorsa önce toplu hâle getirilir; sonra tek bir trigonometrik denklem çözülür.",
            ornek(
                "$[0^\\circ, 360^\\circ)$ aralığında $\\sin x \\cos 30^\\circ+\\cos x \\sin 30^\\circ=1$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Sol taraf $\\sin(x+30^\\circ)$ tir; denklem $\\sin(x+30^\\circ)=1$ olur.",
                "$x+30^\\circ=90^\\circ$, yani $x=60^\\circ$ bulunur."),
            "Trigonometrik denklem çözme yöntemlerinin tamamı için <a href=\"/blog/trigonometrik-denklemler/\">Trigonometrik Denklemler Nasıl Çözülür?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Üçgende toplam formülü", "icerik": [
            "Bir üçgenin iç açıları toplamı $180^\\circ$ olduğu için $C=180^\\circ-(A+B)$ dir. Bütünler açı kuralıyla $\\sin C=\\sin(A+B)$ ve $\\cos C=-\\cos(A+B)$ olur. Böylece iki açının oranları bilinen bir üçgende üçüncü açının oranları toplam formülüyle bulunur.",
            ornek(
                "Bir üçgende $A$ ve $B$ dar açılar, $\\sin A=\\dfrac{3}{5}$ ve $\\sin B=\\dfrac{5}{13}$ olsun.",
                "$\\sin C$ ve $\\cos C$ değerlerini bulalım.",
                "$\\cos A=\\dfrac{4}{5}$, $\\cos B=\\dfrac{12}{13}$. $\\sin C=\\sin(A+B)=\\dfrac{3}{5} \\cdot \\dfrac{12}{13}+\\dfrac{4}{5} \\cdot \\dfrac{5}{13}=\\dfrac{56}{65}$.",
                "$\\cos C=-\\cos(A+B)=-\\left(\\dfrac{48}{65}-\\dfrac{15}{65}\\right)=-\\dfrac{33}{65}$; $C$ geniş açıdır."),
        ]},
        {"baslik": "İki doğru arasındaki açı", "icerik": [
            "Eğimi $m$ olan bir doğru yatay eksenle tanjantı $m$ olan bir açı yapar. İki doğru arasındaki açı bu iki açının farkıdır; tanjant fark formülüyle arada kalan dar açının tanjantı bulunur:",
            "$$\\tan \\theta=\\left|\\dfrac{m_1-m_2}{1+m_1 m_2}\\right|$$",
            ornek(
                "Eğimleri $3$ ve $\\dfrac{1}{2}$ olan iki doğru verilsin.",
                "Doğrular arasındaki dar açıyı bulalım.",
                "$\\tan \\theta=\\left|\\dfrac{3-\\dfrac{1}{2}}{1+\\dfrac{3}{2}}\\right|=\\dfrac{\\dfrac{5}{2}}{\\dfrac{5}{2}}=1$.",
                "Doğrular arasındaki dar açı $45^\\circ$ dir."),
            "Paydanın sıfır olduğu durum, yani $m_1 m_2=-1$ olması, doğruların dik kesiştiğini gösterir. Analitik geometrideki diklik koşulu bu formülün doğal bir sonucudur.",
        ]},
        {"baslik": "Sınavda toplam ve fark formülleri", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) toplam ve fark formülleri; özel olmayan açıların değeri, oranları verilen açılarla hesap, açılmış formülü tanıma ve tanjantlardan açı bulma biçiminde karşına çıkabilir.",
                "Formül çoğu zaman tek başına değil, bir sadeleştirme ya da denklem sorusunun içinde bir adım olarak kullanılır."),
            "Soruda iki farklı açı ve çarpımlar görüyorsan önce toplam ya da fark formülünü tersten tanımayı dene. Açılar $15^\\circ$, $75^\\circ$ ya da $105^\\circ$ gibi özel açıların toplamı veya farkıysa formülü düz uygulamak doğrudan sonuca götürür.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\sin(a+b)=\\sin a+\\sin b$", "Toplam formülü kullanılır"],
                ["$\\cos(a+b)$ de artı işareti", "Kosinüs toplamında eksi"],
                ["$\\cos(a-b)$ de eksi işareti", "Kosinüs farkında artı"],
                ["Tanjant paydasında işareti karıştırmak", "Toplamda $1-$, farkta $1+$"],
                ["Eksik oranın işaretini bölgeden seçmemek", "Bölgeye göre işaret"],
                ["Tanjanttan açı bulurken aralığı unutmak", "Açıların aralığı kontrol edilir"],
            ]),
            "Formüldeki işaretten emin olmadığında $a=b=45^\\circ$ gibi basit bir değerle kontrol et. $\\cos 90^\\circ=0$ olması gerektiği için $\\cos(45^\\circ+45^\\circ)$ açılımındaki işaretin eksi olduğu hemen görülür.",
        ]},
    ],
    "sss": [
        ("Sinüs toplam formülü nedir?",
         "sin(a + b), sin a çarpı cos b artı cos a çarpı sin b ye eşittir. Fark formülünde artı yerine eksi gelir."),
        ("Kosinüs toplam formülünde neden eksi var?",
         "Formül birim çemberdeki iki nokta arasındaki uzaklıktan türetilir ve sonuçta cos a cos b eksi sin a sin b çıkar. a ve b 45 derece alınarak cos 90 derecenin 0 olduğu kontrol edilebilir."),
        ("sin 15 derece kaçtır?",
         "sin 15 derece, sin(45 eksi 30) olarak yazılır ve kök 6 eksi kök 2 bölü 4 bulunur."),
        ("tan 75 derece kaçtır?",
         "Tanjant toplam formülüyle 2 artı kök 3 bulunur."),
        ("Toplam formülü tersten nasıl tanınır?",
         "Her çarpımda bir sinüs ve bir kosinüs varsa sinüs formülü, çarpımlardan biri iki kosinüs diğeri iki sinüsse kosinüs formülüdür."),
        ("İki doğru arasındaki açı nasıl bulunur?",
         "Eğimler m1 ve m2 ise dar açının tanjantı, m1 eksi m2 nin 1 artı m1 çarpı m2 ye bölümünün mutlak değeridir."),
    ],
    "kontrol": [
        "Altı toplam ve fark formülünü yazabiliyorum.",
        "Kosinüs fark formülünün birim çemberden ispatını açıklayabiliyorum.",
        "Diğer formülleri kosinüs fark formülünden türetebiliyorum.",
        "Özel olmayan açıların sinüs, kosinüs ve tanjantını hesaplayabiliyorum.",
        "Oranları verilen açılarla toplam ve fark değerlerini bulabiliyorum.",
        "Eksik oranın işaretini bölgeden seçebiliyorum.",
        "Açılmış formülü tanıyıp toplu hâle getirebiliyorum.",
        "Tanjantları verilen açıların toplamını bulabiliyorum.",
        "İki terimli ifadeyi tek bir sinüs olarak yazabiliyorum.",
        "Formülleri üçgende ve iki doğru arasındaki açıda kullanabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["trigonometrik-ozdeslikler-formuller", "iki-kat-yarim-aci", "trigonometrik-denklemler"],
}
