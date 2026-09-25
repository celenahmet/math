# scripts/yazilar/42_zincir_kurali.py — Bileske Fonksiyonun Turevi: Zincir Kurali (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "zincir-kurali",
    "baslik": "Bileşke Fonksiyonun Türevi: Zincir Kuralı",
    "aciklama": "Zincir kuralı nedir? Bileşke fonksiyonun türevi, iç ve dış fonksiyon, kuvvet, kök, üstel, logaritmik ve trigonometrik zincirler, ilişkili oranlar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "zincir-kurali",
    "kapak_alt": "Bileşke fonksiyonun türevi: büyük çarkın küçük dişliyi, onun da kaydırıcıyı hareket ettirdiği düzeneği çeviren öğrenci",
    "ozet": "Zincir kuralı, iç içe yerleştirilmiş fonksiyonların, yani bileşke fonksiyonların türevini verir: dıştaki fonksiyonun türevi içteki ifadede hesaplanır ve içteki fonksiyonun türeviyle çarpılır. Türev alınan fonksiyonların çoğu bileşke olduğu için en sık kullanılan kurallardan biridir. Bu yazıda kuralın mantığını ve dişli benzetmesini, iç ve dış fonksiyonu belirlemeyi, kuvvet, kök, trigonometrik, üstel ve logaritmik zincirleri, üç katlı bileşkeleri, değerleri verilen fonksiyonlarla hesabı, zincirin çarpım ve bölüm kurallarıyla birlikte kullanımını, ters fonksiyonun türevini, kapalı türevi ve ilişkili oran problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Zincir kuralı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için bileşke fonksiyonu ve temel türev kurallarını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/bileske-fonksiyon/\">Bileşke Fonksiyon</a> ve <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> yazılarına göz at."),
            "$(3x+1)^5$, $\\sin(x^2)$ ya da $e^{2x}$ gibi fonksiyonlarda bir fonksiyonun içine başka bir fonksiyon yerleştirilmiştir. Bu tür fonksiyonlara bileşke fonksiyon denir ve türevleri <strong>zincir kuralı</strong> ile alınır. Kural adını, türevlerin birbirine zincir halkaları gibi eklenmesinden alır.",
            "Kapaktaki öğrenci büyük bir çarkı çeviriyor; çark küçük bir dişliyi, dişli de bir kaydırıcıyı hareket ettiriyor. Kaydırıcının hızı, çarkın hızına iki aktarma oranı üzerinden bağlıdır. Zincir kuralı bu aktarma oranlarının birbiriyle çarpılmasından ibarettir.",
        ]},
        {"baslik": "Neden özel bir kural gerekir?", "icerik": [
            "Bileşke bir fonksiyonun türevini, içteki ifadeyi tek bir değişken gibi görerek almak yanlış sonuç verir. Hatayı açılabilen basit bir örnekle görmek mümkündür.",
            ornek(
                "$h(x)=(2x+1)^2$ fonksiyonu verilsin.",
                "Türevini açarak bulalım ve yanlış yöntemle karşılaştıralım.",
                "Açarak: $h(x)=4x^2+4x+1$ ve $h'(x)=8x+4=4(2x+1)$ olur.",
                "İçteki ifadeyi değişken sayarak bulunan $2(2x+1)$ sonucu yarı yarıya eksiktir; eksik olan çarpan, içteki ifadenin türevi olan $2$ dir."),
            "Zincir kuralı bu eksik çarpanı sistemli olarak ekler. İçteki ifade $x$ ten daha hızlı ya da daha yavaş değişiyorsa, dıştaki fonksiyonun değişim hızı bu oranla çarpılmalıdır. Örnekte içteki ifade $x$ in iki katı hızla değiştiği için türev de iki katına çıkar.",
        ]},
        {"baslik": "Zincir kuralı", "icerik": [
            "$f$ ve $g$ türevli olsun. $f(g(x))$ bileşkesinin türevi, dıştaki fonksiyonun türevinin içteki ifadede hesaplanıp içteki fonksiyonun türeviyle çarpılmasıdır:",
            "$$\\left(f(g(x))\\right)'=f'(g(x)) \\cdot g'(x)$$",
            "İçteki ifade $u=g(x)$ ve dıştaki $y=f(u)$ yazılırsa aynı kural oran gösterimiyle çok akılda kalıcı bir biçim alır: $\\dfrac{dy}{dx}=\\dfrac{dy}{du} \\cdot \\dfrac{du}{dx}$. Sanki $du$ ler sadeleşiyormuş gibi görünür; bu görünüm kuralı hatırlamayı kolaylaştırır.",
            hap("Dışın türevi, içi değiştirmeden; sonra içteki fonksiyonun türeviyle çarp.",
                "İçteki ifade dıştaki türevin içinde aynen kalır."),
        ]},
        {"baslik": "Kural nereden gelir?", "icerik": [
            "$x$ küçük bir $\\Delta x$ kadar değişince içteki $u=g(x)$ ifadesi $\\Delta u$ kadar, dıştaki $y=f(u)$ ise $\\Delta y$ kadar değişir. Bu değişimlerin oranı cebirsel olarak şöyle yazılabilir: $\\dfrac{\\Delta y}{\\Delta x}=\\dfrac{\\Delta y}{\\Delta u} \\cdot \\dfrac{\\Delta u}{\\Delta x}$.",
            "$\\Delta x$ sıfıra giderken $\\Delta u$ da sıfıra gider; çünkü türevli olan $g$ süreklidir. Böylece iki oran sırasıyla $f'(u)$ ya ve $g'(x)$ e yaklaşır ve zincir kuralı elde edilir. Kesin ispatta $\\Delta u$ nun sıfır olduğu durumlar ayrıca ele alınır, ama fikir bu kadar basittir.",
        ]},
        {"baslik": "Dişli benzetmesi", "icerik": [
            "Birinci dişli ikinciyi üç kat hızlı, ikinci dişli de üçüncüyü iki kat hızlı döndürüyorsa, üçüncü dişli birinciden altı kat hızlı döner. Aktarma oranları toplanmaz, çarpılır.",
            "Zincir kuralında da durum aynıdır: $\\dfrac{du}{dx}$ içteki fonksiyonun $x$ e göre aktarma oranı, $\\dfrac{dy}{du}$ ise dıştaki fonksiyonun $u$ ya göre aktarma oranıdır. Toplam oran bu ikisinin çarpımıdır. Kapaktaki çark, dişli ve kaydırıcı üçlüsü tam olarak böyle çalışır.",
            hap("Bisikletin ön dişlisi $48$, arka dişlisi $16$ dişliyse pedalın her turunda arka tekerlek $3$ kez döner, çünkü $\\dfrac{48}{16}=3$ olur.", "İç içe geçen değişim oranları toplanmaz, çarpılır; zincir kuralı da bunu söyler.", gunluk=True),
        ]},
        {"baslik": "İç ve dış fonksiyonu belirlemek", "icerik": [
            "Zincir kuralının ilk adımı, fonksiyonda en son yapılan işlemi bulmaktır. $x$ e bir değer verildiğinde en son uygulanan işlem dış fonksiyon, ondan önce yapılan hesap ise iç fonksiyondur:",
            tablo(["Fonksiyon", "Dış", "İç"], [
                ["$(3x+1)^5$", "$u^5$", "$3x+1$"],
                ["$\\sin(x^2)$", "$\\sin u$", "$x^2$"],
                ["$e^{2x}$", "$e^u$", "$2x$"],
                ["$\\ln(x^2+1)$", "$\\ln u$", "$x^2+1$"],
                ["$\\sqrt{1-x^2}$", "$\\sqrt{u}$", "$1-x^2$"],
            ]),
            "Dikkat edilmesi gereken bir fark vardır: $\\sin(x^2)$ de dış fonksiyon sinüstür, $\\sin^2 x$ te ise dış fonksiyon karedir ve iç fonksiyon sinüstür. Yazımdaki küçük fark türevi tamamen değiştirir.",
        ]},
        {"baslik": "Kuvvet zinciri", "icerik": [
            "En sık karşılaşılan zincir, bir ifadenin kuvvetidir. Kuvvet kuralı dış fonksiyona uygulanır, sonra içteki ifadenin türeviyle çarpılır: $\\left(g(x)^n\\right)'=n g(x)^{n-1} \\cdot g'(x)$.",
            ornek(
                "$h(x)=(x^2+1)^3$ fonksiyonu verilsin.",
                "Türevini ve $h'(1)$ değerini bulalım.",
                "$h'(x)=3(x^2+1)^2 \\cdot 2x=6x(x^2+1)^2$ olur.",
                "$h'(1)=6 \\cdot 1 \\cdot 4=24$ bulunur."),
            "Aynı türev açarak da bulunabilirdi, ama kuvvet büyüdükçe açmak çok uzar. $(x^2+1)^{20}$ gibi bir ifadede zincir kuralı tek satırlık bir sonuç verir.",
            hap("$\\left(g(x)^n\\right)'=n g(x)^{n-1} \\cdot g'(x)$ olur."),
        ]},
        {"baslik": "Kök zinciri", "icerik": [
            "Karekök, üssü bir bölü iki olan bir kuvvet olduğu için zincir kuralı aynı biçimde işler: $\\left(\\sqrt{g(x)}\\right)'=\\dfrac{g'(x)}{2\\sqrt{g(x)}}$. İçteki ifadenin türevi paya, kökün kendisi paydaya gelir.",
            ornek(
                "$h(x)=\\sqrt{x^2+9}$ fonksiyonu verilsin.",
                "Türevini ve $h'(4)$ değerini bulalım.",
                "$h'(x)=\\dfrac{2x}{2\\sqrt{x^2+9}}=\\dfrac{x}{\\sqrt{x^2+9}}$ olur.",
                "$h'(4)=\\dfrac{4}{\\sqrt{25}}=\\dfrac{4}{5}$ bulunur."),
        ]},
        {"baslik": "Kesirli kuvvetler", "icerik": [
            "Kök ile kuvvetin birleştiği ifadeler kesirli üslü yazılınca kuvvet zinciri doğrudan uygulanır. Sonuç, kök içeren sade bir ifadeye dönüştürülür.",
            ornek(
                "$h(x)=(x^2+1)^{3/2}$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "$h'(x)=\\dfrac{3}{2}(x^2+1)^{1/2} \\cdot 2x$ olur.",
                "Sadeleşince $h'(x)=3x\\sqrt{x^2+1}$ bulunur."),
        ]},
        {"baslik": "Mutlak değer ve zincir", "icerik": [
            "Mutlak değer fonksiyonu $|x|=\\sqrt{x^2}$ biçiminde yazılabilir. Bu yazım, zincir kuralıyla mutlak değerin türevini tek bir formülle vermeyi sağlar.",
            ornek(
                "$h(x)=\\sqrt{x^2}$ fonksiyonu verilsin, $x \\neq 0$.",
                "Türevini zincir kuralıyla bulalım.",
                "$h'(x)=\\dfrac{2x}{2\\sqrt{x^2}}=\\dfrac{x}{|x|}$ olur.",
                "Türev pozitif $x$ için $1$, negatif $x$ için $-1$ dir; sıfırda tanımsızdır ve bu, $|x|$ in köşesine karşılık gelir."),
        ]},
        {"baslik": "Trigonometrik zincir", "icerik": [
            "Trigonometrik fonksiyonların içinde $x$ ten farklı bir ifade varsa türevde bu ifadenin türevi çarpan olarak ortaya çıkar. İçteki ifade trigonometrik fonksiyonun içinde değişmeden kalır; yalnızca sinüs kosinüse, kosinüs eksi sinüse dönüşür.",
            ornek(
                "$h(x)=\\sin(x^2)$ ve $k(x)=\\cos 3x$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$h'(x)=\\cos(x^2) \\cdot 2x=2x\\cos(x^2)$ olur.",
                "$k'(x)=-\\sin 3x \\cdot 3=-3\\sin 3x$ olur."),
        ]},
        {"baslik": "Trigonometrik fonksiyonun kuvveti", "icerik": [
            "$\\sin^2 x$ gibi ifadelerde dış fonksiyon kuvvettir; bu yazım aslında $(\\sin x)^2$ anlamına gelir. Önce kuvvet kuralı uygulanır, sonra içteki trigonometrik fonksiyonun türeviyle çarpılır.",
            ornek(
                "$h(x)=\\sin^2 x$ fonksiyonu verilsin.",
                "Türevini bulup sadeleştirelim.",
                "$h'(x)=2\\sin x \\cdot \\cos x$ olur.",
                "İki kat açı formülüyle $h'(x)=\\sin 2x$ bulunur."),
            "Aynı yolla $\\cos^2 x$ in türevi $-2\\cos x \\sin x=-\\sin 2x$ tir. İki türevin toplamı sıfırdır; bu, $\\sin^2 x+\\cos^2 x=1$ özdeşliğinin türevinin sıfır olmasıyla tutarlıdır.",
        ]},
        {"baslik": "Üstel zincir", "icerik": [
            "$e^{g(x)}$ in türevi kendisi ile içteki ifadenin türevinin çarpımıdır: $\\left(e^{g(x)}\\right)'=e^{g(x)} \\cdot g'(x)$. Üstel fonksiyon türevde aynen kalır, yanına içteki türev gelir.",
            ornek(
                "$h(x)=e^{x^2}$ ve $k(x)=e^{-3x}$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$h'(x)=2x e^{x^2}$ olur.",
                "$k'(x)=-3e^{-3x}$ olur; negatif katsayı, fonksiyonun azaldığını gösterir."),
            "Tabanı $e$ olmayan üstel fonksiyonlarda doğal logaritma da çarpan olarak eklenir: $\\left(a^{g(x)}\\right)'=a^{g(x)} \\ln a \\cdot g'(x)$. Örneğin $2^{3x}$ in türevi $3 \\cdot 2^{3x}\\ln 2$ dir.",
            hap("$\\left(e^{g(x)}\\right)'=e^{g(x)} \\cdot g'(x)$ olur; üstel ifade türevde aynen kalır."),
        ]},
        {"baslik": "Logaritmik zincir", "icerik": [
            "$\\ln g(x)$ in türevi, içteki ifadenin türevinin kendisine bölümüdür: $\\left(\\ln g(x)\\right)'=\\dfrac{g'(x)}{g(x)}$. Bu kalıba logaritmik türev denir ve çok sık kullanılır.",
            ornek(
                "$h(x)=\\ln(x^2+1)$ fonksiyonu verilsin.",
                "Türevini ve $h'(1)$ değerini bulalım.",
                "$h'(x)=\\dfrac{2x}{x^2+1}$ olur.",
                "$h'(1)=\\dfrac{2}{2}=1$ bulunur."),
            "Logaritmik türevin bir sonucu şudur: $\\ln(kx)$ in türevi $\\dfrac{k}{kx}=\\dfrac{1}{x}$ dir; içteki sabit katsayı sadeleşir. Bu, $\\ln(kx)=\\ln k+\\ln x$ eşitliğiyle de tutarlıdır.",
            hap("$\\left(\\ln g(x)\\right)'=\\dfrac{g'(x)}{g(x)}$ olur."),
        ]},
        {"baslik": "Üç katlı zincir", "icerik": [
            "Bazı fonksiyonlarda üç ya da daha fazla fonksiyon iç içedir. Zincir kuralı dıştan içe doğru her katta bir kez uygulanır ve bütün türevler çarpılır. Kat sayısı kadar çarpan olur; bir katı atlamak, sonucu o katın türevi kadar yanlış yapar.",
            ornek(
                "$h(x)=\\sin^3(2x)$ fonksiyonu verilsin.",
                "Türevini ve $h'\\left(\\dfrac{\\pi}{8}\\right)$ değerini bulalım.",
                "Katlar dıştan içe kuvvet, sinüs ve $2x$ tir: $h'(x)=3\\sin^2(2x) \\cdot \\cos(2x) \\cdot 2=6\\sin^2(2x)\\cos(2x)$.",
                "$x=\\dfrac{\\pi}{8}$ de $2x=\\dfrac{\\pi}{4}$ olur; $h'=6 \\cdot \\dfrac{1}{2} \\cdot \\dfrac{\\sqrt{2}}{2}=\\dfrac{3\\sqrt{2}}{2}$ bulunur."),
        ]},
        {"baslik": "Titreşimde iç katsayı", "icerik": [
            "Periyodik hareketlerde konum çoğu zaman $A\\sin(\\omega t)$ biçimindedir. Zincir kuralı gereği hızda $\\omega$ çarpanı ortaya çıkar; bu yüzden daha hızlı titreşen bir cisim, aynı genlikte daha büyük hızlara ulaşır.",
            ornek(
                "Bir yayın ucundaki cismin konumu $y(t)=3\\sin 2t$ santimetre olsun.",
                "Hız fonksiyonunu ve en büyük hızı bulalım.",
                "$v(t)=3\\cos 2t \\cdot 2=6\\cos 2t$ olur.",
                "Kosinüs en fazla $1$ olduğundan en büyük hız $6$ santimetre bölü saniyedir."),
        ]},
        {"baslik": "Değerleri verilen bileşke", "icerik": [
            "Fonksiyonların kendileri yerine bazı değerleri verilmişse zincir kuralı bu değerlerle uygulanır. Önce içteki fonksiyonun değeri bulunur, sonra dıştaki türev o değerde hesaplanır.",
            ornek(
                "$g(1)=3$, $g'(1)=2$ ve $f'(3)=5$ olsun.",
                "$(f \\circ g)'(1)$ değerini bulalım.",
                "$(f \\circ g)'(1)=f'(g(1)) \\cdot g'(1)=f'(3) \\cdot 2$ olur.",
                "Sonuç $5 \\cdot 2=10$ dur."),
            dikkat(
                "Dıştaki türevi $f'(1)$ olarak almak.",
                "Dıştaki türev, $x$ te değil içteki fonksiyonun değerinde, yani $g(1)=3$ te hesaplanır. Soruda $f'(1)$ verilmiş olsa bile bu değer kullanılmaz."),
        ]},
        {"baslik": "İçi doğrusal bileşke", "icerik": [
            "İçteki ifade $2x$, $x^2$ gibi basit bir ifade olduğunda da aynı kural geçerlidir: $\\left(f(2x)\\right)'=2f'(2x)$ ve $\\left(f(x^2)\\right)'=2x f'(x^2)$.",
            ornek(
                "$f'(4)=3$ ve $f'(9)=-1$ olsun.",
                "$f(2x)$ in $x=2$ deki ve $f(x^2)$ nin $x=3$ teki türevini bulalım.",
                "$f(2x)$ için türev $2f'(2x)$ tir; $x=2$ de $2f'(4)=6$ olur.",
                "$f(x^2)$ için türev $2x f'(x^2)$ dir; $x=3$ te $6f'(9)=-6$ olur."),
        ]},
        {"baslik": "Zincir ve çarpım birlikte", "icerik": [
            "Çarpanlardan biri bileşke fonksiyonsa çarpım kuralı uygulanırken o çarpanın türevi zincir kuralıyla alınır. Sonuç genellikle ortak payda ya da ortak çarpanla sadeleştirilir.",
            ornek(
                "$h(x)=x\\sqrt{1-x^2}$ fonksiyonu verilsin.",
                "Türevini bulup sadeleştirelim.",
                "$h'(x)=\\sqrt{1-x^2}+x \\cdot \\dfrac{-2x}{2\\sqrt{1-x^2}}=\\sqrt{1-x^2}-\\dfrac{x^2}{\\sqrt{1-x^2}}$ olur.",
                "Ortak paydayla $h'(x)=\\dfrac{1-2x^2}{\\sqrt{1-x^2}}$ bulunur; türev $x=\\pm\\dfrac{\\sqrt{2}}{2}$ de sıfırdır."),
        ]},
        {"baslik": "Zincir ve bölüm birlikte", "icerik": [
            "Bir bölümün kuvveti gibi ifadelerde önce dıştaki kuvvet için zincir kuralı, sonra içteki bölüm için bölüm kuralı uygulanır.",
            ornek(
                "$h(x)=\\left(\\dfrac{x}{x+1}\\right)^2$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "Dış türev $2\\left(\\dfrac{x}{x+1}\\right)$, içteki bölümün türevi $\\dfrac{1}{(x+1)^2}$ olur.",
                "$h'(x)=\\dfrac{2x}{(x+1)^3}$ bulunur."),
            "Bölüm kuralının ayrıntısı için <a href=\"/blog/bolumun-turevi/\">Bölümün Türevi Nasıl Alınır?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Ters fonksiyonun türevi", "icerik": [
            "Zincir kuralı ters fonksiyonun türevini de verir. $f(f^{-1}(x))=x$ eşitliğinin iki tarafının türevi alınırsa $f'(f^{-1}(x)) \\cdot (f^{-1})'(x)=1$ olur. Buradan ters fonksiyonun türevi, fonksiyonun türevinin tersidir:",
            "$$(f^{-1})'(x)=\\dfrac{1}{f'(f^{-1}(x))}$$",
            ornek(
                "$f(x)=x^3+x$ fonksiyonu verilsin.",
                "$(f^{-1})'(2)$ değerini bulalım.",
                "$f(1)=2$ olduğundan $f^{-1}(2)=1$ dir; $f'(x)=3x^2+1$ ve $f'(1)=4$ olur.",
                "$(f^{-1})'(2)=\\dfrac{1}{4}$ bulunur."),
            "Bu yolla ters fonksiyonun formülünü bulmadan türevi hesaplanır. Ters fonksiyon kavramı için <a href=\"/blog/ters-fonksiyon/\">Ters Fonksiyon</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kapalı türev", "icerik": [
            "Bazı eğriler $y=f(x)$ biçiminde değil, $x$ ve $y$ yi birlikte içeren bir denklemle verilir. Bu durumda denklemin iki tarafının türevi alınır ve $y$ içeren her terimde zincir kuralı gereği $y'$ çarpanı eklenir.",
            ornek(
                "$x^2+y^2=25$ çemberi verilsin.",
                "$(3, 4)$ noktasındaki teğetin eğimini bulalım.",
                "Türev alınınca $2x+2y \\cdot y'=0$, yani $y'=-\\dfrac{x}{y}$ olur.",
                "$(3, 4)$ noktasında eğim $-\\dfrac{3}{4}$ bulunur."),
            "Sonuç geometriyle de uyumludur: çemberin teğeti yarıçapa diktir. Yarıçapın eğimi $\\dfrac{4}{3}$ olduğundan teğetin eğimi $-\\dfrac{3}{4}$ tür.",
        ]},
        {"baslik": "İlişkili oranlar: şişen balon", "icerik": [
            "Zamanla değişen ve birbirine bağlı iki niceliğin değişim hızları zincir kuralıyla ilişkilendirilir. Bir niceliğin hızı biliniyorsa diğerininki hesaplanır. Bu tür sorulara ilişkili oran problemleri denir.",
            ornek(
                "Küre biçimli bir balonun yarıçapı saniyede $0.1$ cm artıyor.",
                "Yarıçap $5$ cm olduğunda hacmin artış hızını bulalım.",
                "$V=\\dfrac{4}{3}\\pi r^3$ olduğundan $\\dfrac{dV}{dt}=4\\pi r^2 \\cdot \\dfrac{dr}{dt}$ olur.",
                "$4\\pi \\cdot 25 \\cdot 0.1=10\\pi$ santimetreküp bölü saniye bulunur."),
            "Aynı yarıçap artışı, balon büyüdükçe hacmi daha hızlı artırır; çünkü hız $r^2$ ile orantılıdır.",
        ]},
        {"baslik": "İlişkili oranlar: kayan merdiven", "icerik": [
            "Duvara dayalı bir merdivenin alt ucu duvardan uzaklaştıkça üst ucu aşağı kayar ve iki hız birbirine bağlıdır. Merdivenin boyu sabit olduğu için iki uç arasındaki ilişki Pisagor bağıntısıyla verilir ve zincir kuralıyla iki hız bağlanır.",
            ornek(
                "$10$ m uzunluğundaki merdivenin alt ucu duvardan saniyede $1$ m uzaklaşıyor.",
                "Alt uç duvardan $6$ m uzaktayken üst ucun kayma hızını bulalım.",
                "$x^2+y^2=100$ ve $x=6$ iken $y=8$ dir; türev alınınca $2x x'+2y y'=0$ olur.",
                "$y'=-\\dfrac{x x'}{y}=-\\dfrac{6}{8}=-\\dfrac{3}{4}$ m bölü saniye bulunur; üst uç aşağı kaymaktadır."),
        ]},
        {"baslik": "Zincirin adımları", "icerik": [
            "Karmaşık bir bileşkede işlemi sistemli yürütmek hataları önler ve hiçbir katın atlanmamasını sağlar. Aşağıdaki adımlar her zincir problemi için kullanılabilir:",
            tablo(["Adım", "İşlem"], [
                ["1", "En son yapılan işlemi, yani dış fonksiyonu bul"],
                ["2", "Dış fonksiyonun türevini al, içi aynen bırak"],
                ["3", "İçteki fonksiyonun türevini al"],
                ["4", "İç de bileşkeyse aynı adımları tekrarla"],
                ["5", "Bütün türevleri çarp ve sadeleştir"],
            ]),
        ]},
        {"baslik": "Sınavda zincir kuralı", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) zincir kuralı; kuvvet, kök, üstel, logaritmik ve trigonometrik bileşkelerin türevi, değerleri verilen fonksiyonlarla bileşke türevi ve ters fonksiyonun türevi biçiminde karşına çıkabilir.",
                "Zincir kuralı, teğet, ekstremum ve ilişkili oran sorularının da içinde yer alır."),
            "Bileşke sorusunda önce içteki fonksiyonun değerini hesapla, sonra dıştaki türevi o değerde bul. $(f \\circ g)'(a)$ sorularındaki en sık hata, dıştaki türevi $a$ da hesaplamaktır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["İçteki türevi unutmak", "$f'(g(x)) \\cdot g'(x)$"],
                ["$(f \\circ g)'(a)=f'(a)g'(a)$", "$f'(g(a))g'(a)$"],
                ["$(e^{3x})'=e^{3x}$", "$3e^{3x}$"],
                ["$(\\sin 2x)'=\\cos 2x$", "$2\\cos 2x$"],
                ["$\\sin^2 x$ ile $\\sin(x^2)$ yi karıştırmak", "Dış fonksiyonlar farklı"],
                ["Kapalı türevde $y$ nin yanına $y'$ koymamak", "Zincir kuralı gereği eklenir"],
            ]),
            "En yaygın hata içteki türevi unutmaktır. Bir türev aldıktan sonra içteki ifadenin türevinin $1$ olup olmadığına bakmak bu hatayı önler; yalnızca iç ifade $x$ ise çarpan $1$ dir.",
        ]},
    ],
    "sss": [
        ("Zincir kuralı nedir?",
         "Bileşke fonksiyonun türevini veren kuraldır: dıştaki fonksiyonun türevi içteki ifadede hesaplanır ve içteki fonksiyonun türeviyle çarpılır."),
        ("(3x + 1) üzeri 5 in türevi nedir?",
         "Zincir kuralıyla 5(3x + 1) üzeri 4 çarpı 3, yani 15(3x + 1) üzeri 4 tür."),
        ("e üzeri x kare nin türevi nedir?",
         "2x çarpı e üzeri x kare dir. Üstel fonksiyon aynen kalır, yanına içteki ifadenin türevi gelir."),
        ("ln g(x) in türevi nedir?",
         "g üssü x bölü g(x) tir. Bu kalıba logaritmik türev denir."),
        ("sin kare x ile sin(x kare) nin türevleri aynı mı?",
         "Hayır. sin kare x in türevi sin 2x, sin(x kare) nin türevi 2x cos(x kare) dir; dış fonksiyonlar farklıdır."),
        ("Ters fonksiyonun türevi nasıl bulunur?",
         "Ters fonksiyonun bir noktadaki türevi, fonksiyonun karşılık gelen noktadaki türevinin çarpmaya göre tersidir."),
        ("Kapalı türev nedir?",
         "x ve y yi birlikte içeren bir denklemin iki tarafının türevi alınır. y li her terimde zincir kuralı gereği y üssü çarpanı eklenir ve y üssü yalnız bırakılır."),
        ("İlişkili oran problemi nasıl çözülür?",
         "Nicelikler arasındaki bağıntı yazılır, iki tarafın zamana göre türevi alınır ve bilinen hız yerine konarak istenen hız bulunur."),
    ],
    "kontrol": [
        "Bileşke fonksiyonda iç ve dış fonksiyonu belirleyebiliyorum.",
        "Zincir kuralını her iki gösterimle yazabiliyorum.",
        "Kuvvet ve kök zincirlerinin türevini alabiliyorum.",
        "Trigonometrik zincirleri ve trigonometrik kuvvetleri türevleyebiliyorum.",
        "Üstel ve logaritmik zincirlerin türevini bulabiliyorum.",
        "Üç katlı bileşkelerde zinciri sırayla uygulayabiliyorum.",
        "Değerleri verilen fonksiyonlarla bileşke türevini hesaplayabiliyorum.",
        "Zinciri çarpım ve bölüm kurallarıyla birlikte kullanabiliyorum.",
        "Ters fonksiyonun türevini ve kapalı türevi bulabiliyorum.",
        "İlişkili oran problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["turev-alma-kurallari", "carpimin-turevi", "bileske-fonksiyon"],
}
