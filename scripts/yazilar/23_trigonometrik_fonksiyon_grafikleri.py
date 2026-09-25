# scripts/yazilar/23_trigonometrik_fonksiyon_grafikleri.py — Trigonometrik Fonksiyonlarin Grafikleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

PI_ISARET = [(math.pi / 2, "π/2"), (math.pi, "π"), (3 * math.pi / 2, "3π/2"), (2 * math.pi, "2π")]
CEYREK_ISARET = [(math.pi / 4, "π/4"), (math.pi / 2, "π/2"), (3 * math.pi / 4, "3π/4"), (math.pi, "π")]


def _tan(x):
    return None if abs(math.cos(x)) < 1e-9 else math.tan(x)


def _cot(x):
    return None if abs(math.sin(x)) < 1e-9 else math.cos(x) / math.sin(x)


YAZI = {
    "slug": "trigonometrik-fonksiyon-grafikleri",
    "baslik": "Trigonometrik Fonksiyonların Grafikleri",
    "aciklama": "Sinüs, kosinüs, tanjant ve kotanjant grafikleri nasıl çizilir? Periyot, genlik, öteleme, grafikten denklem okuma ve grafikle çözüm; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "trigonometrik-fonksiyon-grafikleri",
    "kapak_alt": "Trigonometrik fonksiyonların grafikleri: dönen çarkların renkli dalga izlerine dönüştüğü düzeneği inceleyen iki öğrenci",
    "ozet": "Trigonometrik fonksiyonların grafikleri, birim çember üzerinde dönen bir noktanın hareketinin zamana yayılmış hâlidir. Sinüs ve kosinüs grafikleri dalga biçimindedir, tanjant ve kotanjant grafikleri ise dikey asimptotlarla bölünmüş dallardan oluşur. Bu yazıda periyodik fonksiyon kavramını, dört temel grafiği, genlik, periyot ve öteleme dönüşümlerini, genel biçimin en büyük ve en küçük değerini, grafikten denklem okumayı ve grafik yardımıyla denklem ve eşitsizlik çözmeyi çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Birim çemberden grafiğe", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birim çemberi, radyanı ve özel açıların trigonometrik değerlerini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/birim-cember/\">Birim Çember Konu Anlatımı</a> ve <a href=\"/blog/trigonometri-konu-anlatimi/\">Trigonometri Konu Anlatımı</a> yazılarına göz at."),
            "Birim çember üzerinde sabit hızla dönen bir nokta düşün. Noktanın yüksekliği sinüsü, yatay konumu kosinüsü verir. Dönme açısını yatay eksene, yüksekliği dikey eksene yazarsan bir dalga elde edersin; bu dalga sinüs fonksiyonunun grafiğidir.",
            "Kapaktaki düzenek bu fikri görselleştiriyor: dönen çarkların uçlarına bağlı kalemler, kâğıt ilerledikçe renkli dalgalar çiziyor. Çarkın büyüklüğü dalganın yüksekliğini, dönme hızı ise dalgaların ne sıklıkla tekrar ettiğini belirliyor. Bu iki özellik, grafiklerde genlik ve periyot olarak karşımıza çıkacak.",
        ]},
        {"baslik": "Periyodik fonksiyon", "icerik": [
            "Bir fonksiyonun değerleri belirli aralıklarla aynen tekrar ediyorsa bu fonksiyon <strong>periyodiktir</strong>. Her $x$ için $f(x+T)=f(x)$ eşitliğini sağlayan en küçük pozitif $T$ sayısına fonksiyonun <strong>esas periyodu</strong> denir.",
            "Birim çemberde bir tam tur $2\\pi$ radyan olduğu için sinüs ve kosinüsün değerleri her $2\\pi$ de bir tekrar eder. Tanjant ve kotanjant ise yarım turda, yani her $\\pi$ de bir tekrar eder. Bu yüzden bir periyotluk grafiği çizmek, tüm grafiği çizmek demektir: aynı parça sağa ve sola kopyalanır.",
            hap("Periyodik fonksiyonda aynı parça sonsuza kadar tekrar eder.",
                "Bir periyotluk parçayı çizmek, grafiğin tamamını bilmek demektir."),
        ]},
        {"baslik": "Sinüs grafiği", "icerik": [
            "$y=\\sin x$ grafiğini çizmek için bir periyot boyunca birkaç önemli noktanın değeri hesaplanır ve noktalar düzgün bir dalgayla birleştirilir. Çeyrek tur aralıklarla alınan beş nokta dalganın iskeletini verir:",
            tablo(["$x$", "$0$", "$\\dfrac{\\pi}{2}$", "$\\pi$", "$\\dfrac{3\\pi}{2}$", "$2\\pi$"], [
                ["$\\sin x$", "$0$", "$1$", "$0$", "$-1$", "$0$"],
            ]),
            koordinat_grafik("y = sin x grafiği", [("", math.sin)], (-0.5, 7), (-1.5, 1.5), adim=0.5, etiket_adim=1, x_isaretler=PI_ISARET,
                             noktalar=[(0, 0, "", True), (math.pi / 2, 1, "", True), (math.pi, 0, "", True), (3 * math.pi / 2, -1, "", True), (2 * math.pi, 0, "", True)]),
            "Grafik başlangıç noktasından geçer, $\\dfrac{\\pi}{2}$ de en yüksek değeri olan $1$ e ulaşır, $\\pi$ de yeniden sıfıra iner, $\\dfrac{3\\pi}{2}$ de en düşük değeri olan $-1$ e iner ve $2\\pi$ de başladığı yüksekliğe döner.",
        ]},
        {"baslik": "Sinüs grafiğinin özellikleri", "icerik": [
            "Sinüs fonksiyonu tüm gerçek sayılarda tanımlıdır ve yalnızca $-1$ ile $1$ arasındaki değerleri alır. Grafik orijine göre simetriktir; çünkü her $x$ için $\\sin(-x)=-\\sin x$ olur. Bu özelliğe sahip fonksiyonlara tek fonksiyon denir.",
            tablo(["Özellik", "$y=\\sin x$"], [
                ["Tanım kümesi", "Tüm gerçek sayılar"],
                ["Görüntü kümesi", "$[-1, 1]$"],
                ["Esas periyot", "$2\\pi$"],
                ["Simetri", "Orijine göre (tek fonksiyon)"],
                ["Sıfırları", "$x=k\\pi$"],
                ["En büyük değer", "$1$, $x=\\dfrac{\\pi}{2}+2k\\pi$ iken"],
            ]),
            "Tablodaki $k$ herhangi bir tam sayıyı gösterir. Sıfırların $\\pi$ aralıklarla dizilmesi, grafiğin yatay ekseni her yarım turda bir kestiğini anlatır.",
        ]},
        {"baslik": "Kosinüs grafiği", "icerik": [
            "$y=\\cos x$ grafiği de aynı yolla çizilir. Kosinüs başlangıçta en yüksek değerindedir, bu yüzden dalga $1$ den başlar:",
            tablo(["$x$", "$0$", "$\\dfrac{\\pi}{2}$", "$\\pi$", "$\\dfrac{3\\pi}{2}$", "$2\\pi$"], [
                ["$\\cos x$", "$1$", "$0$", "$-1$", "$0$", "$1$"],
            ]),
            koordinat_grafik("y = cos x grafiği", [("", math.cos)], (-0.5, 7), (-1.5, 1.5), adim=0.5, etiket_adim=1, x_isaretler=PI_ISARET,
                             noktalar=[(0, 1, "", True), (math.pi / 2, 0, "", True), (math.pi, -1, "", True), (3 * math.pi / 2, 0, "", True), (2 * math.pi, 1, "", True)]),
            "İki grafik aynı dalgadır; kosinüs grafiği, sinüs grafiğinin $\\dfrac{\\pi}{2}$ kadar sola kaydırılmış hâlidir. Bu yüzden her $x$ için $\\cos x=\\sin\\left(x+\\dfrac{\\pi}{2}\\right)$ eşitliği doğrudur.",
        ]},
        {"baslik": "Kosinüs grafiğinin özellikleri", "icerik": [
            "Kosinüs fonksiyonu da tüm gerçek sayılarda tanımlıdır, görüntü kümesi yine $[-1, 1]$ aralığıdır ve esas periyodu $2\\pi$ dir. Farkı simetride görülür: her $x$ için $\\cos(-x)=\\cos x$ olduğundan grafik dikey eksene göre simetriktir. Bu özelliğe sahip fonksiyonlara çift fonksiyon denir.",
            "Kosinüsün sıfırları $x=\\dfrac{\\pi}{2}+k\\pi$ noktalarıdır; en büyük değer olan $1$ e $x=2k\\pi$ noktalarında, en küçük değer olan $-1$ e ise $x=\\pi+2k\\pi$ noktalarında ulaşılır. Sinüs ve kosinüsün en yüksek noktaları arasında her zaman çeyrek periyotluk, yani $\\dfrac{\\pi}{2}$ lik bir kayma vardır.",
        ]},
        {"baslik": "Genlik", "icerik": [
            "$y=a\\sin x$ fonksiyonunda $a$ katsayısı dalganın yüksekliğini değiştirir. Bu yüksekliğe <strong>genlik</strong> denir ve $|a|$ ile ölçülür. Grafik dikey yönde $|a|$ kat uzar; periyot ve sıfırlar değişmez.",
            koordinat_grafik("y = sin x ve y = 2 sin x grafikleri", [("y = sin x", math.sin), ("y = 2 sin x", lambda x: 2 * math.sin(x))], (-0.5, 7), (-2.5, 3.5), adim=0.5, etiket_adim=1, x_isaretler=PI_ISARET),
            ornek(
                "$y=3\\sin x$ fonksiyonu verilsin.",
                "Genliği ve görüntü kümesini bulalım.",
                "Genlik $|3|=3$ tür.",
                "Fonksiyon $-3$ ile $3$ arasındaki değerleri alır: görüntü kümesi $[-3, 3]$ aralığıdır."),
            "Katsayı negatifse genlik yine pozitif alınır; negatif işaret yalnızca grafiği yatay eksene göre ters çevirir. $y=-2\\sin x$ grafiği, $\\dfrac{\\pi}{2}$ de $1$ e çıkmak yerine $-2$ ye iner.",
            hap("$y=a\\sin x$ fonksiyonunda genlik $|a|$ olur; periyot ve sıfırlar değişmez."),
        ]},
        {"baslik": "Periyodun değişmesi", "icerik": [
            "$y=\\sin(bx)$ fonksiyonunda $b$ katsayısı dalganın sıklığını değiştirir. $b$ büyüdükçe nokta çember üzerinde daha hızlı döner ve dalgalar sıklaşır. Yeni periyot $\\dfrac{2\\pi}{|b|}$ formülüyle bulunur.",
            koordinat_grafik("y = sin x ve y = sin 2x grafikleri", [("y = sin x", math.sin), ("y = sin 2x", lambda x: math.sin(2 * x))], (-0.5, 7), (-1.5, 2.2), adim=0.5, etiket_adim=1, x_isaretler=PI_ISARET),
            "Grafikte $y=\\sin 2x$ dalgası, $y=\\sin x$ in bir tur attığı aralıkta iki tur atar; periyodu $\\dfrac{2\\pi}{2}=\\pi$ dir. Genlik ise değişmemiştir: iki dalga da $-1$ ile $1$ arasında kalır.",
            ornek(
                "$y=\\cos 3x$ fonksiyonu verilsin.",
                "Esas periyodu bulalım.",
                "Periyot $\\dfrac{2\\pi}{|b|}$ formülüyle bulunur, burada $b=3$.",
                "Esas periyot $\\dfrac{2\\pi}{3}$ dir."),
            hap("$y=\\sin(bx)$ ve $y=\\cos(bx)$ fonksiyonlarının periyodu $\\dfrac{2\\pi}{|b|}$ olur."),
        ]},
        {"baslik": "Periyot formülleri", "icerik": [
            "Dört temel fonksiyonun periyot formülleri aşağıda bir araya getirilmiştir. Sinüs ve kosinüs için pay $2\\pi$, tanjant ve kotanjant için $\\pi$ alınır. Formülde yalnızca $x$ in katsayısı etkilidir; genlik, düşey öteleme ya da yatay öteleme periyodu değiştirmez.",
            tablo(["Fonksiyon", "Esas periyot"], [
                ["$y=a\\sin(bx+c)+d$", "$\\dfrac{2\\pi}{|b|}$"],
                ["$y=a\\cos(bx+c)+d$", "$\\dfrac{2\\pi}{|b|}$"],
                ["$y=a\\tan(bx+c)+d$", "$\\dfrac{\\pi}{|b|}$"],
                ["$y=a\\cot(bx+c)+d$", "$\\dfrac{\\pi}{|b|}$"],
            ]),
            ornek(
                "$y=5\\tan\\left(\\dfrac{x}{2}\\right)-1$ fonksiyonu verilsin.",
                "Esas periyodu bulalım.",
                "$x$ in katsayısı $\\dfrac{1}{2}$ dir; tanjant için pay $\\pi$ alınır.",
                "Periyot $\\dfrac{\\pi}{1/2}=2\\pi$ olur."),
        ]},
        {"baslik": "Düşey öteleme", "icerik": [
            "$y=\\sin x+d$ fonksiyonunda grafik $d$ birim yukarı kayar; $d$ negatifse aşağı kayar. Dalganın biçimi, genliği ve periyodu değişmez, yalnızca denge çizgisi yatay eksenden $y=d$ doğrusuna taşınır.",
            koordinat_grafik("y = sin x ve y = sin x + 1 grafikleri", [("y = sin x", math.sin), ("y = sin x + 1", lambda x: math.sin(x) + 1)], (-0.5, 7), (-1.5, 3), adim=0.5, etiket_adim=1, x_isaretler=PI_ISARET,
                             yataylar=[1]),
            "Grafikte kesikli çizgi, yeni dalganın denge çizgisi olan $y=1$ doğrusudur. $y=\\sin x+1$ fonksiyonu $0$ ile $2$ arasındaki değerleri alır; görüntü kümesi $[0, 2]$ aralığıdır.",
        ]},
        {"baslik": "Yatay öteleme", "icerik": [
            "$y=\\sin(x-c)$ fonksiyonunda grafik $c$ birim sağa kayar; parantezin içindeki işaret artıysa kayma sola doğrudur. Bu yön ilk bakışta ters gibi görünür: $x-c$ ifadesinin sıfır olması için $x$ in $c$ kadar büyük olması gerekir, bu yüzden dalganın başlangıç noktası sağa taşınır.",
            ornek(
                "$y=\\sin\\left(x+\\dfrac{\\pi}{2}\\right)$ fonksiyonu verilsin.",
                "Grafiğin hangi bilinen grafiğe dönüştüğünü bulalım.",
                "Parantez içindeki artı işaret, grafiğin $\\dfrac{\\pi}{2}$ kadar sola kaydığını gösterir.",
                "Sinüs grafiği $\\dfrac{\\pi}{2}$ sola kayınca kosinüs grafiği elde edilir: fonksiyon $y=\\cos x$ olur."),
            "Katsayılı durumlarda önce parantez içi $b\\left(x+\\dfrac{c}{b}\\right)$ biçimine getirilir. $y=\\sin(2x-\\pi)$ fonksiyonunda kayma $\\pi$ değil, $\\dfrac{\\pi}{2}$ kadar sağa doğrudur.",
            hap("$y=\\sin(x-c)$ grafiği $c$ birim sağa, $y=\\sin(x+c)$ grafiği $c$ birim sola kayar."),
        ]},
        {"baslik": "Genel biçim", "icerik": [
            "Tüm dönüşümler bir araya getirilince genel biçim $y=a\\sin(bx+c)+d$ olur. Bu biçimde her harfin görevi ayrıdır: $a$ genliği, $b$ periyodu, $c$ yatay kaymayı, $d$ ise denge çizgisini belirler.",
            tablo(["Harf", "Etkisi", "Formül"], [
                ["$a$", "Genlik", "$|a|$"],
                ["$b$", "Periyot", "$\\dfrac{2\\pi}{|b|}$"],
                ["$c$", "Yatay kayma", "$-\\dfrac{c}{b}$"],
                ["$d$", "Denge çizgisi", "$y=d$"],
            ]),
            "Görüntü kümesi yalnızca $a$ ve $d$ ye bağlıdır: fonksiyon $d-|a|$ ile $d+|a|$ arasındaki tüm değerleri alır.",
            hap("Yarıçapı $20$ metre, merkezi yerden $22$ metre yüksekte olan ve $10$ dakikada bir tur atan dönme dolapta kabinin yüksekliği $h(t)=22-20\\cos \\dfrac{\\pi t}{5}$ metre olur.", "Kabin en alçakta $2$, en yüksekte $42$ metrededir ve her $10$ dakikada bir aynı yüksekliğe döner.", gunluk=True),
        ]},
        {"baslik": "En büyük ve en küçük değer", "icerik": [
            "Genel biçimdeki bir fonksiyonun en büyük ve en küçük değeri, sinüs ya da kosinüsün $-1$ ile $1$ arasında kalmasından bulunur. Önce trigonometrik kısmın aralığı yazılır, sonra katsayılar ve sabit adım adım uygulanır.",
            ornek(
                "$y=4-3\\cos 2x$ fonksiyonu verilsin.",
                "En büyük ve en küçük değeri bulalım.",
                "$-1 \\le \\cos 2x \\le 1$ olduğundan $-3 \\le -3\\cos 2x \\le 3$ olur.",
                "Dört eklenince $1 \\le y \\le 7$ elde edilir: en küçük değer $1$, en büyük değer $7$ dir."),
            "En büyük değer $\\cos 2x=-1$ iken alınır; yani negatif katsayı yüzünden kosinüsün en küçük olduğu yerde fonksiyon en büyük olur. İşaretin bu etkisi sık yapılan bir hatanın kaynağıdır.",
        ]},
        {"baslik": "Tanjant grafiği", "icerik": [
            "$y=\\tan x$ fonksiyonu kosinüsün sıfır olduğu yerlerde tanımsızdır. Bu noktalarda grafiğin yaklaştığı ama hiç kesmediği dikey doğrulara <strong>asimptot</strong> denir. Grafik her iki asimptot arasında aşağıdan yukarıya sürekli artan bir dal çizer.",
            koordinat_grafik("y = tan x grafiği", [("", _tan)], (-0.5, 7), (-4, 4), adim=1, x_isaretler=PI_ISARET,
                             dikeyler=[math.pi / 2, 3 * math.pi / 2], noktalar=[(0, 0, "", True), (math.pi, 0, "", True), (2 * math.pi, 0, "", True)]),
            "Kesikli çizgiler $x=\\dfrac{\\pi}{2}$ ve $x=\\dfrac{3\\pi}{2}$ asimptotlarıdır. Grafik $0$, $\\pi$ ve $2\\pi$ noktalarında yatay ekseni keser ve her dal bir öncekinin $\\pi$ kadar sağa kaydırılmış kopyasıdır.",
        ]},
        {"baslik": "Tanjant grafiğinin özellikleri", "icerik": [
            "Tanjantın değerleri sınırsızdır: görüntü kümesi tüm gerçek sayılardır. Buna karşın tanım kümesinden $x=\\dfrac{\\pi}{2}+k\\pi$ noktaları çıkarılır. Esas periyot $\\pi$ dir ve grafik orijine göre simetriktir; tanjant da sinüs gibi tek bir fonksiyondur.",
            tablo(["Özellik", "$y=\\tan x$", "$y=\\cot x$"], [
                ["Tanımsız olduğu yerler", "$x=\\dfrac{\\pi}{2}+k\\pi$", "$x=k\\pi$"],
                ["Görüntü kümesi", "Tüm gerçek sayılar", "Tüm gerçek sayılar"],
                ["Esas periyot", "$\\pi$", "$\\pi$"],
                ["Her dalda", "Artan", "Azalan"],
                ["Sıfırları", "$x=k\\pi$", "$x=\\dfrac{\\pi}{2}+k\\pi$"],
            ]),
        ]},
        {"baslik": "Kotanjant grafiği", "icerik": [
            "$y=\\cot x$ fonksiyonu sinüsün sıfır olduğu yerlerde tanımsızdır; asimptotları $x=k\\pi$ doğrularıdır. Tanjanttan farklı olarak her dalda yukarıdan aşağıya sürekli azalır.",
            koordinat_grafik("y = cot x grafiği", [("", lambda x: _cot(x) if x > 0 else None)], (-0.5, 7), (-4, 4), adim=1, x_isaretler=PI_ISARET,
                             dikeyler=[math.pi, 2 * math.pi], noktalar=[(math.pi / 2, 0, "", True), (3 * math.pi / 2, 0, "", True)]),
            "Grafikte dikey eksen, $x=\\pi$ ve $x=2\\pi$ doğruları asimptotlardır. Kotanjant yatay ekseni dalların tam ortasında, $\\dfrac{\\pi}{2}$ ve $\\dfrac{3\\pi}{2}$ noktalarında keser.",
        ]},
        {"baslik": "Grafikten denklem okumak", "icerik": [
            "Grafiği verilen bir fonksiyonun denklemini bulmak için genel biçimdeki harfler sırayla okunur. En yüksek ve en düşük değerin ortalaması denge çizgisini, farkının yarısı genliği, art arda iki tepe arasındaki uzaklık ise periyodu verir.",
            koordinat_grafik("Denklemi bulunacak grafik", [("", lambda x: 2 * math.sin(2 * x) + 1)], (-0.3, 3.6), (-1.5, 3.5), adim=0.5, etiket_adim=1, x_isaretler=CEYREK_ISARET,
                             yataylar=[1], noktalar=[(math.pi / 4, 3, "", True), (3 * math.pi / 4, -1, "", True)]),
            ornek(
                "Grafikteki fonksiyon $y=a\\sin(bx)+d$ biçiminde, en yüksek değeri $3$, en düşük değeri $-1$ ve periyodu $\\pi$ dir.",
                "Denklemi bulalım.",
                "Denge çizgisi $d=\\dfrac{3+(-1)}{2}=1$, genlik $a=\\dfrac{3-(-1)}{2}=2$ dir.",
                "Periyottan $\\dfrac{2\\pi}{b}=\\pi$, yani $b=2$. Fonksiyon $y=2\\sin 2x+1$ olur."),
        ]},
        {"baslik": "Grafikle denklem çözmek", "icerik": [
            "Bir trigonometrik denklemin belirli bir aralıktaki çözüm sayısı, grafik ile yatay bir doğrunun kesişim sayısına eşittir. Örneğin $\\sin x=\\dfrac{1}{2}$ denkleminin $[0, 2\\pi)$ aralığında iki çözümü vardır; çünkü sinüs dalgası bu aralıkta $y=\\dfrac{1}{2}$ doğrusunu iki kez keser.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin 2x=\\dfrac{1}{2}$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$y=\\sin 2x$ bu aralıkta iki tam dalga çizer; her dalga $y=\\dfrac{1}{2}$ doğrusunu iki kez keser, toplam dört çözüm beklenir.",
                "$2x=\\dfrac{\\pi}{6}, \\dfrac{5\\pi}{6}, \\dfrac{13\\pi}{6}, \\dfrac{17\\pi}{6}$ olduğundan çözümler $\\dfrac{\\pi}{12}$, $\\dfrac{5\\pi}{12}$, $\\dfrac{13\\pi}{12}$ ve $\\dfrac{17\\pi}{12}$ olur."),
        ]},
        {"baslik": "Periyot sayısıyla çözüm saymak", "icerik": [
            "Çözümleri tek tek bulmadan yalnızca kaç tane olduğu sorulduğunda periyot sayısı kullanılır. Aralık uzunluğu periyoda bölünür; her tam periyotta sinüs ve kosinüs dalgası yatay eksenle iki kez, $-1$ ile $1$ arasındaki her yatay doğruyla da iki kez kesişir.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\cos 3x=0$ denklemi verilsin.",
                "Çözüm sayısını bulalım.",
                "$\\cos 3x$ in periyodu $\\dfrac{2\\pi}{3}$ olduğundan aralık tam üç periyot içerir.",
                "Her periyotta iki sıfır vardır; denklemin bu aralıkta altı çözümü olur."),
        ]},
        {"baslik": "Grafikle eşitsizlik çözmek", "icerik": [
            "Grafik, bir trigonometrik ifadenin hangi aralıklarda pozitif ya da negatif olduğunu bir bakışta gösterir. Eşitsizlik çözerken önce eşitlik durumundaki noktalar bulunur, sonra grafiğin bu noktalar arasında yatay eksenin üstünde mi altında mı kaldığına bakılır.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\cos x>0$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "Kosinüs $\\dfrac{\\pi}{2}$ ve $\\dfrac{3\\pi}{2}$ noktalarında sıfırdır; grafik bu iki nokta arasında eksenin altında kalır.",
                "Çözüm kümesi $\\left[0, \\dfrac{\\pi}{2}\\right) \\cup \\left(\\dfrac{3\\pi}{2}, 2\\pi\\right)$ olur."),
        ]},
        {"baslik": "Toplam fonksiyonun periyodu", "icerik": [
            "İki periyodik fonksiyonun toplamının periyodu, iki periyodun en küçük ortak katıdır. Toplam fonksiyon, iki parçanın da aynı anda başa döndüğü ilk anda kendini tekrar etmeye başlar.",
            ornek(
                "$f(x)=\\sin 2x+\\cos 3x$ fonksiyonu verilsin.",
                "Esas periyodu bulalım.",
                "$\\sin 2x$ in periyodu $\\pi$, $\\cos 3x$ in periyodu $\\dfrac{2\\pi}{3}$ dir.",
                "İki periyodun en küçük ortak katı $2\\pi$ dir; toplam fonksiyonun esas periyodu $2\\pi$ olur."),
        ]},
        {"baslik": "Kare ve mutlak değer", "icerik": [
            "Sinüsün karesi ya da mutlak değeri alınınca negatif kısımlar pozitife döner ve dalganın yarısı diğer yarısının kopyası hâline gelir. Bu yüzden periyot yarıya iner.",
            ornek(
                "$y=\\sin^2 x$ ve $y=|\\sin x|$ fonksiyonları verilsin.",
                "Esas periyotlarını bulalım.",
                "Kuvvet azaltma formülüyle $\\sin^2 x=\\dfrac{1-\\cos 2x}{2}$; buradaki $\\cos 2x$ in periyodu $\\pi$ dir.",
                "$|\\sin x|$ grafiğinde de negatif yarım dalga yukarı katlanır. İki fonksiyonun esas periyodu da $\\pi$ olur."),
            "Kuvvet azaltma formülünün ayrıntısı için <a href=\"/blog/trigonometrik-ozdeslikler-formuller/\">Trigonometrik Özdeşlikler ve Formüller</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Dört grafiğin karşılaştırması", "icerik": [
            "Dört temel fonksiyonun grafikleri iki aileye ayrılır. Sinüs ve kosinüs sürekli, sınırlı ve dalga biçimindedir; tanjant ve kotanjant ise asimptotlarla bölünmüş, sınırsız dallardan oluşur.",
            tablo(["Fonksiyon", "Görüntü kümesi", "Periyot", "Simetri"], [
                ["$\\sin x$", "$[-1, 1]$", "$2\\pi$", "Tek"],
                ["$\\cos x$", "$[-1, 1]$", "$2\\pi$", "Çift"],
                ["$\\tan x$", "Tüm gerçek sayılar", "$\\pi$", "Tek"],
                ["$\\cot x$", "Tüm gerçek sayılar", "$\\pi$", "Tek"],
            ]),
        ]},
        {"baslik": "Sınavda grafikler", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) trigonometrik grafikler; periyot bulma, en büyük ve en küçük değer, grafikten denklem okuma ve çözüm sayısı biçiminde karşına çıkabilir.",
                "Periyot soruları en sık görülen türdür ve genellikle tek satırda çözülür."),
            "Grafik sorularında önce periyodu ve denge çizgisini belirle, sonra genliği oku. Çözüm sayısı soruluyorsa aralığın kaç periyot içerdiğini hesaplamak, grafiği çizmeden cevaba ulaştırır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\sin 2x$ in periyodunu $4\\pi$ bulmak", "Periyot $\\dfrac{2\\pi}{2}=\\pi$"],
                ["Tanjant periyodunda $2\\pi$ kullanmak", "Tanjant ve kotanjantta pay $\\pi$"],
                ["$\\sin(x-c)$ yi sola kaydırmak", "Eksi işaret sağa kaydırır"],
                ["Negatif katsayıda genliği negatif almak", "Genlik $|a|$"],
                ["Düşey ötelemenin periyodu değiştirdiğini sanmak", "Periyot yalnız $b$ ye bağlı"],
                ["Tanjantın asimptotlarını $k\\pi$ sanmak", "Asimptotlar $\\dfrac{\\pi}{2}+k\\pi$"],
            ]),
            "Bu hataların çoğu, formülü grafikle ilişkilendirmeden ezberlemekten doğar. Şüpheye düşüldüğünde birkaç noktanın değerini hesaplayıp kaba bir grafik çizmek, doğru cevabı hızlıca gösterir.",
        ]},
    ],
    "sss": [
        ("Sinüs fonksiyonunun periyodu nedir?",
         "y = sin x fonksiyonunun esas periyodu 2 pi dir. y = sin(bx) biçiminde ise periyot 2 pi bölü mutlak b olur."),
        ("Tanjant grafiğinde asimptot nedir?",
         "Grafiğin yaklaştığı ama hiç kesmediği dikey doğrudur. Tanjantın asimptotları kosinüsün sıfır olduğu pi bölü 2 artı k pi noktalarındadır."),
        ("Genlik nedir?",
         "Dalganın denge çizgisinden en yüksek noktasına olan uzaklığıdır. y = a sin x fonksiyonunda genlik a nın mutlak değeridir."),
        ("Sinüs ve kosinüs grafikleri arasındaki fark nedir?",
         "İki grafik aynı dalgadır. Kosinüs grafiği, sinüs grafiğinin pi bölü 2 kadar sola kaydırılmış hâlidir."),
        ("Trigonometrik fonksiyonun en büyük değeri nasıl bulunur?",
         "Sinüs ya da kosinüsün eksi 1 ile 1 arasında kalmasından yola çıkılır; katsayı ve sabit terim bu aralığa sırayla uygulanır."),
        ("İki trigonometrik fonksiyonun toplamının periyodu nasıl bulunur?",
         "Her birinin periyodu ayrı bulunur ve iki periyodun en küçük ortak katı alınır."),
    ],
    "kontrol": [
        "Periyodik fonksiyonu ve esas periyodu açıklayabiliyorum.",
        "Sinüs ve kosinüs grafiklerini önemli noktalarıyla çizebiliyorum.",
        "Sinüs ve kosinüs grafiklerinin özelliklerini karşılaştırabiliyorum.",
        "Genliği ve görüntü kümesini bulabiliyorum.",
        "Katsayıdan esas periyodu hesaplayabiliyorum.",
        "Düşey ve yatay ötelemeyi grafikte gösterebiliyorum.",
        "Genel biçimin en büyük ve en küçük değerini bulabiliyorum.",
        "Tanjant ve kotanjant grafiklerini asimptotlarıyla çizebiliyorum.",
        "Grafiği verilen fonksiyonun denklemini okuyabiliyorum.",
        "Grafik yardımıyla denklem ve eşitsizlik çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birim-cember", "trigonometrik-ozdeslikler-formuller", "trigonometri-konu-anlatimi"],
}
