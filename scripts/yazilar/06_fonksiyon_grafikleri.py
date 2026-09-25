# scripts/yazilar/06_fonksiyon_grafikleri.py — Fonksiyon Grafikleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "fonksiyon-grafikleri",
    "baslik": "Fonksiyon Grafikleri Nasıl Çizilir ve Yorumlanır?",
    "aciklama": "Fonksiyon grafiği nasıl çizilir ve okunur? Dikey doğru testi, eksen kesişimleri, artan ve azalan aralıklar, öteleme, yansıma, simetri ve kesişim; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "fonksiyonlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "fonksiyon-grafikleri",
    "kapak_alt": "Fonksiyon grafikleri: koordinat ızgaralı bir tahtaya noktalar yerleştirip eğri çizen ve dikey bir cetvelle inceleyen iki öğrenci",
    "ozet": "Bir fonksiyonun grafiği, fonksiyonun bütün davranışını tek bir resimde gösterir: hangi değerleri aldığı, nerede arttığı, nerede sıfır olduğu ve başka bir fonksiyonla nerede kesiştiği bir bakışta görülür. Bu yazıda koordinat düzlemini, nokta nokta grafik çizmeyi, dikey doğru testini, grafikten tanım ve görüntü kümesi okumayı, eksen kesişimlerini, artan ve azalan aralıkları, temel fonksiyonların grafiklerini, öteleme ve yansımayı, simetriyi ve iki grafiğin kesişimini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Fonksiyon grafiği nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için fonksiyon kavramını, tanım ve görüntü kümesini biliyor olman yeterli.",
                "Temel kavramlar için <a href=\"/blog/fonksiyonlar-konu-anlatimi/\">Fonksiyonlar Konu Anlatımı</a> ve <a href=\"/blog/tanim-deger-goruntu-kumeleri/\">Tanım, Değer ve Görüntü Kümeleri</a> yazılarına göz at."),
            "Bir $f$ fonksiyonunun tanım kümesindeki her $x$ için $(x, f(x))$ noktası koordinat düzleminde işaretlenirse bu noktaların oluşturduğu şekle $f$ fonksiyonunun <strong>grafiği</strong> denir. Grafik, fonksiyonun bir tablo ya da formülle anlatılan davranışını görünür hâle getirir.",
            "Grafik üzerindeki her nokta bir girdi ile ona karşılık gelen çıktıyı birlikte taşır: noktanın yatay konumu girdiyi, dikey konumu çıktıyı gösterir. Kapaktaki öğrencilerin tahtaya çaktığı her çivi böyle bir noktadır; çiviler birleştirildiğinde eğri ortaya çıkar.",
            hap("Grafik, $(x, f(x))$ noktalarının kümesidir.",
                "Yatay konum girdi, dikey konum çıktıdır."),
        ]},
        {"baslik": "Koordinat düzlemi", "icerik": [
            "Koordinat düzlemi, birbirine dik iki sayı doğrusundan oluşur. Yatay doğruya $x$ ekseni, dikey doğruya $y$ ekseni, kesiştikleri noktaya da başlangıç noktası denir. Her nokta $(a, b)$ biçiminde bir sıralı ikiliyle gösterilir: $a$ yatay, $b$ dikey konumdur.",
            "Eksenler düzlemi dört bölgeye ayırır. Bölgeler sağ üstten başlayıp saat yönünün tersine numaralanır ve her bölgede koordinatların işaretleri bellidir.",
            tablo(["Bölge", "$x$ in işareti", "$y$ nin işareti", "Örnek nokta"], [
                ["I. bölge", "$+$", "$+$", "$(2, 3)$"],
                ["II. bölge", "$-$", "$+$", "$(-2, 3)$"],
                ["III. bölge", "$-$", "$-$", "$(-2, -3)$"],
                ["IV. bölge", "$+$", "$-$", "$(2, -3)$"],
            ]),
            "Eksenler üzerindeki noktalar hiçbir bölgeye ait değildir. Örneğin $(0, 5)$ noktası $y$ ekseni üzerinde, $(4, 0)$ noktası $x$ ekseni üzerindedir.",
        ]},
        {"baslik": "Nokta nokta grafik çizmek", "icerik": [
            "Bir fonksiyonun grafiğini çizmenin en temel yolu, birkaç $x$ değeri seçip karşılık gelen $f(x)$ değerlerini hesaplamak, bulunan noktaları işaretlemek ve bu noktaları fonksiyonun davranışına uygun biçimde birleştirmektir.",
            ornek(
                "$f(x)=2x-1$ fonksiyonu verilsin.",
                "Değer tablosu kurup grafiği çizelim.",
                "$x=-1$ için $f(-1)=-3$; $x=0$ için $f(0)=-1$; $x=1$ için $f(1)=1$; $x=2$ için $f(2)=3$.",
                "Noktalar: $(-1, -3)$, $(0, -1)$, $(1, 1)$, $(2, 3)$. Hepsi aynı doğru üzerindedir."),
            koordinat_grafik("f(x) = 2x − 1 fonksiyonunun grafiği", [("y = 2x − 1", lambda x: 2 * x - 1)], (-3, 4), (-4, 4),
                             noktalar=[(-1, -3, "(−1, −3)", True), (0, -1, "(0, −1)", True), (1, 1, "(1, 1)", True), (2, 3, "(2, 3)", True)]),
            "Doğrusal bir fonksiyon için iki nokta yeterlidir, çünkü iki noktadan tek bir doğru geçer. Eğri grafiklerde ise ne kadar çok nokta seçilirse eğrinin biçimi o kadar doğru görünür; özellikle eğrinin yön değiştirdiği yerlerin çevresinde nokta seçmek gerekir.",
        ]},
        {"baslik": "Dikey doğru testi", "icerik": [
            "Her grafik bir fonksiyon grafiği değildir. Fonksiyonda her girdinin tek bir çıktısı olduğu için grafiği hiçbir dikey doğru birden fazla noktada kesemez. Bu ölçüte <strong>dikey doğru testi</strong> denir: dikey doğrulardan biri bile eğriyi iki noktada kesiyorsa eğri bir fonksiyon grafiği değildir.",
            ornek(
                "Merkezi başlangıç noktası, yarıçapı $3$ olan çember verilsin.",
                "Çemberin bir fonksiyon grafiği olup olmadığını inceleyelim.",
                "$x=1$ dikey doğrusu çemberi iki noktada keser: $y=\\sqrt{8}$ ve $y=-\\sqrt{8}$.",
                "Bir girdiye iki çıktı karşılık geldiği için çember bir fonksiyon grafiği değildir."),
            koordinat_grafik("Çember dikey doğru testini geçemez: x = 1 doğrusu iki noktada keser",
                             [("üst yarı", lambda x: math.sqrt(9 - x * x) if abs(x) <= 3 else None),
                              ("alt yarı", lambda x: -math.sqrt(9 - x * x) if abs(x) <= 3 else None)],
                             (-4, 4), (-4, 4), dikeyler=[1], noktalar=[(1, math.sqrt(8), "", True), (1, -math.sqrt(8), "", True)]),
            "Çemberin üst yarısı tek başına bir fonksiyon grafiğidir, alt yarısı da öyle. Kapaktaki öğrencinin elindeki dikey cetvel bu testi uygular: cetvel eğri boyunca kaydırılır ve her konumda eğriye en fazla bir kez değip değmediğine bakılır.",
            hap("Hiçbir dikey doğru eğriyi birden fazla noktada kesmiyorsa eğri bir fonksiyon grafiğidir."),
        ]},
        {"baslik": "Grafikten değer okumak", "icerik": [
            "Grafik verildiğinde $f(a)$ değeri şöyle okunur: $x$ ekseninde $a$ noktasından dikey olarak grafiğe gidilir, grafiğe değilen noktanın yüksekliği $f(a)$ dır. Tersine, $f(x)=b$ denkleminin çözümleri için $y=b$ yatay doğrusunun grafiği kestiği noktaların yatay konumlarına bakılır.",
            ornek(
                "$f(x)=x^2-4x+3$ fonksiyonunun grafiği verilsin.",
                "$f(0)$ ve $f(4)$ değerlerini ve $f(x)=3$ denkleminin çözümlerini bulalım.",
                "$f(0)=3$ ve $f(4)=16-16+3=3$.",
                "$f(x)=3$ için $x^2-4x=0$, yani $x(x-4)=0$. Çözümler $x=0$ ve $x=4$ tür; $y=3$ doğrusu grafiği bu iki noktada keser."),
            koordinat_grafik("f(x) = x² − 4x + 3 fonksiyonunun grafiği ve y = 3 doğrusu", [("y = x² − 4x + 3", lambda x: x * x - 4 * x + 3)], (-1, 5), (-2, 5),
                             yataylar=[3], noktalar=[(0, 3, "(0, 3)", True), (4, 3, "(4, 3)", True), (1, 0, "(1, 0)", True), (3, 0, "(3, 0)", True), (2, -1, "(2, −1)", True)]),
        ]},
        {"baslik": "Eksen kesişimleri", "icerik": [
            "Grafiğin $y$ eksenini kestiği nokta $(0, f(0))$ dır ve her fonksiyon grafiği $y$ eksenini en fazla bir kez keser. Grafiğin $x$ eksenini kestiği noktalar ise $f(x)=0$ denkleminin çözümleridir; bu değerlere fonksiyonun <strong>sıfırları</strong> ya da kökleri denir.",
            ornek(
                "$f(x)=x^2-4x+3$ fonksiyonu verilsin.",
                "Grafiğin eksenleri kestiği noktaları bulalım.",
                "$y$ ekseni: $f(0)=3$; nokta $(0, 3)$.",
                "$x$ ekseni: $x^2-4x+3=0$, yani $(x-1)(x-3)=0$. Noktalar $(1, 0)$ ve $(3, 0)$."),
            "Eksen kesişimleri grafiği çizmeye başlamak için en kolay bulunan noktalardır. Grafiğin çizilmesi istenen sorularda önce bu noktaları bulmak, eğriyi doğru yere yerleştirmeyi kolaylaştırır.",
            hap("$y$ eksenini kestiği noktayı bulmak için $x=0$ yazılır.", "$x$ eksenini kestiği noktalar $f(x)=0$ denkleminin çözümleridir."),
        ]},
        {"baslik": "Grafikten tanım ve görüntü kümesi", "icerik": [
            "Grafiğin $x$ eksenine dik izdüşümü tanım kümesini, $y$ eksenine dik izdüşümü görüntü kümesini verir. Başka bir deyişle, grafiğin yatayda kapladığı aralık tanım kümesi, dikeyde kapladığı aralık görüntü kümesidir.",
            ornek(
                "$[-1, 2]$ aralığında tanımlı $f(x)=x^2$ fonksiyonu verilsin.",
                "Görüntü kümesini grafikten bulalım.",
                "Grafik $x=0$ noktasında en alçak değeri alır: $f(0)=0$.",
                "En yüksek değer aralığın sağ ucundadır: $f(2)=4$. Sol uçtaki değer $f(-1)=1$ dir.",
                "Görüntü kümesi $[0, 4]$ tür."),
            dikkat(
                "Görüntü kümesini uç noktalardaki değerlerden bulmak.",
                "Uç noktalarda $f(-1)=1$ ve $f(2)=4$ bulunur, ama görüntü kümesi $[1, 4]$ değildir. Grafik aralığın içinde $0$ a kadar iner; en küçük ve en büyük değer grafiğin tamamına bakılarak bulunur."),
        ]},
        {"baslik": "Artan ve azalan aralıklar", "icerik": [
            "Soldan sağa ilerlerken grafik yükseliyorsa fonksiyon o aralıkta <strong>artandır</strong>, alçalıyorsa <strong>azalandır</strong>. Artandan azalana ya da azalandan artana geçilen noktalarda fonksiyon yerel en büyük ya da en küçük değerini alır.",
            ornek(
                "$f(x)=x^2-4x+3$ fonksiyonunun grafiği verilsin.",
                "Artan ve azalan olduğu aralıkları ve en küçük değerini bulalım.",
                "Grafik $x=2$ noktasına kadar alçalır, sonra yükselir.",
                "Fonksiyon $(-\\infty, 2]$ aralığında azalan, $[2, \\infty)$ aralığında artandır.",
                "En küçük değer $f(2)=-1$ dir."),
            "Artan bir fonksiyonda büyük girdi büyük çıktı verir: $a<b$ ise $f(a)<f(b)$ dir. Azalan bir fonksiyonda ise büyük girdi küçük çıktı verir. Bu tanımlar, bir fonksiyonun grafiği olmadan da artan ya da azalan olduğunu göstermek için kullanılır.",
        ]},
        {"baslik": "Pozitif ve negatif olduğu aralıklar", "icerik": [
            "Grafik $x$ ekseninin üstündeyse fonksiyonun değerleri pozitif, altındaysa negatiftir. Bu yüzden $f(x)>0$ ya da $f(x)<0$ biçimindeki eşitsizlikler grafikten doğrudan okunur: sıfırlar işaret değişiminin olabileceği yerleri ayırır.",
            ornek(
                "$f(x)=x^2-4x+3$ fonksiyonu verilsin.",
                "$f(x)<0$ eşitsizliğinin çözüm kümesini bulalım.",
                "Sıfırlar $x=1$ ve $x=3$ tür.",
                "Grafik bu iki nokta arasında $x$ ekseninin altındadır: çözüm kümesi $(1, 3)$ tür.",
                "$x<1$ ya da $x>3$ için ise $f(x)>0$ dır."),
        ]},
        {"baslik": "Doğrusal fonksiyonun grafiği", "icerik": [
            "$f(x)=ax+b$ biçimindeki fonksiyonların grafiği bir doğrudur. $a$ sayısı doğrunun <strong>eğimidir</strong>: $x$ bir birim arttığında $y$ nin ne kadar değiştiğini gösterir. $b$ sayısı ise doğrunun $y$ eksenini kestiği noktanın yüksekliğidir.",
            ornek(
                "$f(x)=-2x+4$ fonksiyonu verilsin.",
                "Grafiğin eksen kesişimlerini ve eğimini bulalım.",
                "$y$ ekseni: $f(0)=4$; nokta $(0, 4)$.",
                "$x$ ekseni: $-2x+4=0$, yani $x=2$; nokta $(2, 0)$.",
                "Eğim $-2$ dir: $x$ bir artınca $y$ iki azalır; fonksiyon azalandır."),
            "Eğim pozitifse doğru soldan sağa yükselir ve fonksiyon artandır; eğim negatifse doğru alçalır ve fonksiyon azalandır. Eğim sıfırsa doğru yataydır: bu bir <strong>sabit fonksiyondur</strong> ve $y=3$ gibi yazılır. $f(x)=x$ ise <strong>birim fonksiyondur</strong>; grafiği başlangıç noktasından geçen ve eksenler arasındaki açıyı ikiye bölen doğrudur.",
            hap("Açılış ücreti $50$ TL, kilometre ücreti $20$ TL olan bir taksinin ücreti $f(x)=20x+50$ doğrusudur.", "Doğrunun $y$ eksenini kestiği yer açılış ücretini, eğimi kilometre başına ücreti gösterir: $10$ kilometrelik yol $250$ TL tutar.", gunluk=True),
        ]},
        {"baslik": "Mutlak değer fonksiyonunun grafiği", "icerik": [
            "$f(x)=|x|$ fonksiyonunun grafiği, $x \\geq 0$ için $y=x$ doğrusu, $x<0$ için $y=-x$ doğrusundan oluşur ve V biçimindedir. En alçak noktası başlangıç noktasıdır.",
            koordinat_grafik("y = |x| ve y = |x − 2| + 1 grafikleri", [("y = |x|", abs), ("y = |x − 2| + 1", lambda x: abs(x - 2) + 1)], (-4, 5), (-1, 5),
                             noktalar=[(0, 0, "", True), (2, 1, "(2, 1)", True)]),
            ornek(
                "$f(x)=|x-2|+1$ fonksiyonu verilsin.",
                "Grafiğin köşe noktasını ve en küçük değeri bulalım.",
                "Mutlak değerin içi $x=2$ de sıfır olur; köşe noktası $(2, 1)$ dir.",
                "Mutlak değer negatif olamayacağı için en küçük değer $1$ dir ve $x=2$ de alınır."),
            "Mutlak değerin ayrıntısı <a href=\"/blog/mutlak-deger-konu-anlatimi-pdf/\">Mutlak Değer Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Parçalı fonksiyonların grafiği", "icerik": [
            "Tanım kümesinin farklı bölümlerinde farklı kurallarla tanımlanan fonksiyonlara <strong>parçalı fonksiyon</strong> denir. Grafiği çizilirken her parça yalnızca kendi aralığında çizilir. Aralığın ucu fonksiyona dâhilse o uca dolu, dâhil değilse boş daire konur.",
            ornek(
                "$x<1$ için $f(x)=x+1$, $x \\geq 1$ için $f(x)=4-x$ olarak tanımlanan fonksiyon verilsin.",
                "Grafiği çizip $f(-1)$, $f(1)$ ve $f(3)$ değerlerini bulalım.",
                "$f(-1)=-1+1=0$. $x=1$ ikinci parçaya aittir: $f(1)=4-1=3$.",
                "$f(3)=4-3=1$.",
                "Birinci parça $x=1$ e yaklaşırken $2$ ye yaklaşır ama bu değeri almaz; o noktaya boş daire konur."),
            koordinat_grafik("Parçalı fonksiyon: x < 1 için x + 1, x ≥ 1 için 4 − x",
                             [("y = x + 1 (x < 1)", lambda x: x + 1 if x < 1 else None), ("y = 4 − x (x ≥ 1)", lambda x: 4 - x if x >= 1 else None)],
                             (-3, 5), (-2, 4), noktalar=[(1, 2, "", False), (1, 3, "(1, 3)", True)]),
        ]},
        {"baslik": "Grafiklerin ötelenmesi", "icerik": [
            "Bir fonksiyonun grafiği bilinirken ona benzeyen fonksiyonların grafikleri yeniden çizilmeden bulunabilir. $k$ pozitif olmak üzere:",
            tablo(["Fonksiyon", "Grafiğe etkisi"], [
                ["$y=f(x)+k$", "$k$ birim yukarı"],
                ["$y=f(x)-k$", "$k$ birim aşağı"],
                ["$y=f(x-k)$", "$k$ birim sağa"],
                ["$y=f(x+k)$", "$k$ birim sola"],
            ]),
            ornek(
                "$y=x^2$ grafiği biliniyor.",
                "$y=(x-2)^2+1$ grafiğinin en alçak noktasını bulalım.",
                "$y=x^2$ nin en alçak noktası $(0, 0)$ dır.",
                "Grafik $2$ birim sağa ve $1$ birim yukarı ötelenir: en alçak nokta $(2, 1)$ olur."),
            koordinat_grafik("y = x² grafiğinin 2 birim sağa, 1 birim yukarı ötelenmesi", [("y = x²", lambda x: x * x), ("y = (x − 2)² + 1", lambda x: (x - 2) ** 2 + 1)],
                             (-3, 5), (-1, 6), noktalar=[(0, 0, "", True), (2, 1, "(2, 1)", True)]),
            dikkat(
                "Parantez içindeki ötelemenin yönünü ters almak.",
                "$y=f(x-2)$ grafiği sola değil sağa kayar. Eski grafikte $x=0$ noktasında olan değer, yeni grafikte $x-2=0$, yani $x=2$ noktasında görülür."),
            hap("$y=f(x-k)$ grafiği $k$ birim sağa, $y=f(x)+k$ grafiği $k$ birim yukarı kayar.", "Parantezin içindeki değişiklik yatay, dışındaki değişiklik dikey kaydırmadır."),
        ]},
        {"baslik": "Yansımalar", "icerik": [
            "Bir grafiğin eksenlere göre yansıması da kuraldan doğrudan okunur. $y=-f(x)$ grafiği, $y=f(x)$ grafiğinin $x$ eksenine göre yansımasıdır: her noktanın yüksekliği işaret değiştirir. $y=f(-x)$ grafiği ise $y$ eksenine göre yansımadır: her nokta yatayda karşı tarafa geçer.",
            ornek(
                "$f(x)=\\sqrt{x}$ fonksiyonunun grafiği $(4, 2)$ noktasından geçiyor.",
                "$y=-\\sqrt{x}$ ve $y=\\sqrt{-x}$ grafiklerinde bu noktanın karşılıklarını bulalım.",
                "$x$ eksenine göre yansıma: $(4, -2)$.",
                "$y$ eksenine göre yansıma: $(-4, 2)$. Gerçekten $\\sqrt{-(-4)}=\\sqrt{4}=2$."),
            koordinat_grafik("y = √x grafiği ve eksenlere göre yansımaları",
                             [("y = √x", lambda x: math.sqrt(x) if x >= 0 else None), ("y = −√x", lambda x: -math.sqrt(x) if x >= 0 else None),
                              ("y = √(−x)", lambda x: math.sqrt(-x) if x <= 0 else None)],
                             (-5, 5), (-3, 5), noktalar=[(4, 2, "(4, 2)", True), (4, -2, "(4, −2)", True), (-4, 2, "(−4, 2)", True)]),
        ]},
        {"baslik": "Simetri: tek ve çift fonksiyonlar", "icerik": [
            "Her $x$ için $f(-x)=f(x)$ oluyorsa $f$ <strong>çift fonksiyondur</strong> ve grafiği $y$ eksenine göre simetriktir. Her $x$ için $f(-x)=-f(x)$ oluyorsa $f$ <strong>tek fonksiyondur</strong> ve grafiği başlangıç noktasına göre simetriktir.",
            tablo(["Fonksiyon", "Tür", "Simetri"], [
                ["$x^2$, $|x|$, $x^4-3x^2$", "Çift", "$y$ eksenine göre"],
                ["$x$, $x^3$, $x^3-x$", "Tek", "Başlangıç noktasına göre"],
                ["$x^2+x$", "Ne tek ne çift", "Yok"],
            ]),
            ornek(
                "$f(x)=x^3-x$ fonksiyonu verilsin.",
                "Fonksiyonun tek mi çift mi olduğunu bulalım.",
                "$f(-x)=(-x)^3-(-x)=-x^3+x$.",
                "$-f(x)=-x^3+x$ olduğu için $f(-x)=-f(x)$ tir; fonksiyon tektir."),
            "Simetri, grafiğin yalnızca yarısını çizip diğer yarısını yansıtarak tamamlamayı sağlar. Çift fonksiyonda $x \\geq 0$ kısmı $y$ eksenine göre, tek fonksiyonda başlangıç noktasına göre yansıtılır.",
        ]},
        {"baslik": "Ters fonksiyonun grafiği", "icerik": [
            "Birebir ve örten bir fonksiyonun tersinin grafiği, fonksiyonun grafiğinin $y=x$ doğrusuna göre yansımasıdır. Grafikte $(a, b)$ noktası varsa ters fonksiyonun grafiğinde $(b, a)$ noktası vardır.",
            ornek(
                "$f(x)=2x+1$ fonksiyonu verilsin.",
                "Ters fonksiyonu bulup iki grafiğin simetrisini inceleyelim.",
                "$y=2x+1$ den $x=\\dfrac{y-1}{2}$; yani $f^{-1}(x)=\\dfrac{x-1}{2}$.",
                "$f(1)=3$ olduğu için $(1, 3)$ noktası $f$ nin grafiğindedir; $f^{-1}(3)=1$ olduğu için $(3, 1)$ noktası tersinin grafiğindedir."),
            koordinat_grafik("f(x) = 2x + 1 ile tersinin grafikleri y = x doğrusuna göre simetriktir",
                             [("y = 2x + 1", lambda x: 2 * x + 1), ("y = (x − 1)/2", lambda x: (x - 1) / 2), ("y = x", lambda x: x)],
                             (-3, 5), (-3, 5), noktalar=[(1, 3, "(1, 3)", True), (3, 1, "(3, 1)", True)]),
            "Ters fonksiyonun ayrıntısı <a href=\"/blog/ters-fonksiyon/\">Ters Fonksiyon Nasıl Bulunur?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "İki grafiğin kesişimi", "icerik": [
            "İki fonksiyonun grafiklerinin kesiştiği noktalarda iki fonksiyon aynı değeri alır. Bu yüzden kesişim noktalarının yatay konumları $f(x)=g(x)$ denkleminin çözümleridir; kesişim noktası sayısı da bu denklemin çözüm sayısına eşittir.",
            ornek(
                "$f(x)=x^2$ ve $g(x)=x+2$ fonksiyonları verilsin.",
                "Grafiklerin kesişim noktalarını bulalım.",
                "$x^2=x+2$, yani $x^2-x-2=0$ ve $(x-2)(x+1)=0$.",
                "$x=2$ için $y=4$; $x=-1$ için $y=1$. Kesişim noktaları $(-1, 1)$ ve $(2, 4)$ tür."),
            koordinat_grafik("y = x² ile y = x + 2 grafiklerinin kesişimi", [("y = x²", lambda x: x * x), ("y = x + 2", lambda x: x + 2)],
                             (-3, 4), (-1, 6), noktalar=[(-1, 1, "(−1, 1)", True), (2, 4, "(2, 4)", True)]),
            "Tersine, bir denklemin kaç çözümü olduğu da grafiklerle bulunabilir: denklemin iki tarafı iki ayrı fonksiyon gibi çizilir ve kesişim noktaları sayılır. Cebirsel çözümü zor olan denklemlerde bu yöntem, en azından çözüm sayısını hızla verir.",
        ]},
        {"baslik": "Grafikten bileşke değer okumak", "icerik": [
            "Grafik verilen bir fonksiyonda $f(f(a))$ gibi bileşke değerler içten dışa doğru okunur: önce $f(a)$ grafikten bulunur, sonra bulunan değer yeni girdi olarak kullanılır.",
            ornek(
                "Yukarıdaki parçalı fonksiyon verilsin: $x<1$ için $f(x)=x+1$, $x \\geq 1$ için $f(x)=4-x$.",
                "$f(f(3))$ ve $f(f(0))$ değerlerini bulalım.",
                "$f(3)=1$ ve $f(1)=3$; yani $f(f(3))=3$.",
                "$f(0)=1$ ve $f(1)=3$; yani $f(f(0))=3$."),
            "Bileşkenin ayrıntısı <a href=\"/blog/bileske-fonksiyon/\">Bileşke Fonksiyon Konu Anlatımı</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sınavda fonksiyon grafikleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) grafik soruları grafikten değer okuma, eksen kesişimleri ve basit grafik yorumlama biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) öteleme, yansıma, parçalı fonksiyonlar, simetri, bileşke ve ters fonksiyonun grafiği de sorulabilir."),
            "Grafik sorularında önce eksenlerin ölçeğine ve grafiğin üzerindeki özel noktalara bak: eksen kesişimleri, en yüksek ve en alçak noktalar, dolu ve boş daireler. Sorunun büyük bölümü bu noktalarla çözülür; geri kalan kısım soldan sağa okunan artma ve azalma bilgisidir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Her eğriyi fonksiyon grafiği sanmak", "Dikey doğru testi uygulanır"],
                ["$y=f(x-2)$ yi sola kaydırmak", "Grafik $2$ birim sağa kayar"],
                ["Görüntü kümesini uç değerlerden bulmak", "Grafiğin tamamına bakılır"],
                ["Boş daireyi değer sanmak", "Boş dairedeki değer alınmaz"],
                ["Kesişim noktasının yalnız $x$ ini yazmak", "Nokta $(x, y)$ olarak yazılır"],
                ["Artanlığı sağdan sola okumak", "Grafik soldan sağa okunur"],
            ]),
            "Bu hataların çoğu grafiğe acele bakmaktan doğar. Grafiği her zaman soldan sağa oku, özel noktaları işaretle ve bir kuralı uygulamadan önce birkaç noktada yerine koyarak kontrol et.",
        ]},
    ],
    "sss": [
        ("Fonksiyon grafiği nedir?",
         "Tanım kümesindeki her x için (x, f(x)) noktalarının koordinat düzleminde oluşturduğu şekildir. Yatay konum girdiyi, dikey konum çıktıyı gösterir."),
        ("Bir grafiğin fonksiyon grafiği olup olmadığı nasıl anlaşılır?",
         "Dikey doğru testi uygulanır. Hiçbir dikey doğru grafiği birden fazla noktada kesmiyorsa grafik bir fonksiyona aittir."),
        ("Grafiğin x eksenini kestiği noktalar nasıl bulunur?",
         "f(x) = 0 denklemi çözülür. Bulunan değerler fonksiyonun sıfırlarıdır ve grafik x eksenini bu noktalarda keser."),
        ("Grafikten görüntü kümesi nasıl bulunur?",
         "Grafiğin y eksenine izdüşümüne bakılır. Grafiğin dikeyde kapladığı aralık görüntü kümesidir; yalnız uç noktalara bakmak yetmez."),
        ("f(x − 2) grafiği hangi yöne kayar?",
         "Sağa kayar. Eski grafikte x = 0 da görülen değer, yeni grafikte x = 2 de görülür."),
        ("Ters fonksiyonun grafiği nasıl çizilir?",
         "Fonksiyonun grafiği y = x doğrusuna göre yansıtılır. Grafikteki her (a, b) noktası ters fonksiyonun grafiğinde (b, a) noktası olur."),
    ],
    "kontrol": [
        "Koordinat düzleminde noktaları ve bölgeleri tanıyabiliyorum.",
        "Değer tablosuyla bir fonksiyonun grafiğini çizebiliyorum.",
        "Dikey doğru testini uygulayabiliyorum.",
        "Grafikten fonksiyon değeri ve denklem çözümü okuyabiliyorum.",
        "Grafiğin eksen kesişimlerini bulabiliyorum.",
        "Grafikten tanım kümesini, görüntü kümesini ve artan azalan aralıkları bulabiliyorum.",
        "Doğrusal, mutlak değer ve parçalı fonksiyonların grafiklerini çizebiliyorum.",
        "Öteleme ve yansımaları grafiğe uygulayabiliyorum.",
        "Tek ve çift fonksiyonların simetrisini kullanabiliyorum.",
        "İki grafiğin kesişim noktalarını bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["fonksiyonlar-konu-anlatimi", "ters-fonksiyon", "mutlak-deger-konu-anlatimi-pdf"],
}
