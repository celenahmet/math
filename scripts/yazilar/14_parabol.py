# scripts/yazilar/14_parabol.py — Parabol Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "parabol-konu-anlatimi",
    "baslik": "Parabol Konu Anlatımı",
    "aciklama": "Parabol nedir? Kolların yönü, simetri ekseni, tepe noktası, eksen kesişimleri, üç denklem biçimi, en büyük ve en küçük değer ve problemler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["AYT"],
    "kapak": "parabol-konu-anlatimi",
    "kapak_alt": "Parabol: köprü kemeri, su yayı ve çanak anten gibi parabol biçimlerini karşılaştıran iki öğrenci",
    "ozet": "Parabol, ikinci dereceden bir fonksiyonun grafiğidir ve matematiğin en tanıdık eğrilerinden biridir: fırlatılan bir topun izlediği yol, bir fıskiyeden çıkan su ve bir çanak antenin kesiti bu biçimdedir. Bu yazıda parabolün tanımını, baş katsayının kolların yönüne ve genişliğine etkisini, simetri eksenini, tepe noktasını, eksen kesişimlerini, parabol denkleminin üç biçimini, en büyük ve en küçük değeri, görüntü kümesini, artan ve azalan aralıkları ve parabolle çözülen problemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Parabol nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için ikinci dereceden denklemleri ve fonksiyon grafiklerini biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/ikinci-dereceden-denklemler/\">İkinci Dereceden Denklemler Konu Anlatımı</a> ve <a href=\"/blog/fonksiyon-grafikleri/\">Fonksiyon Grafikleri Nasıl Çizilir ve Yorumlanır?</a> yazılarına göz at."),
            "$a$, $b$ ve $c$ gerçek sayılar ve $a \\neq 0$ olmak üzere $f(x)=ax^2+bx+c$ biçimindeki fonksiyonlara <strong>ikinci dereceden fonksiyon</strong>, bu fonksiyonların grafiklerine de <strong>parabol</strong> denir. Parabol, bir simetri eksenine göre iki yanı birbirinin aynası olan, bir tepe noktasından iki kola ayrılan bir eğridir.",
            "$a \\neq 0$ koşulu tanımın temelidir. $a$ sıfır olursa $x^2$ li terim kaybolur, fonksiyon birinci dereceden olur ve grafiği bir doğruya dönüşür. Bu yüzden parabol sorularında baş katsayı parametreliyse sıfırdan farklı olduğu ayrıca yazılmalıdır.",
            hap("Parabol, $y=ax^2+bx+c$ ve $a \\neq 0$ fonksiyonunun grafiğidir.",
                "Her parabolün bir tepe noktası ve bir simetri ekseni vardır."),
        ]},
        {"baslik": "Günlük hayatta parabol", "icerik": [
            "Parabol yalnızca kâğıt üzerinde bir eğri değildir. Hava direnci ihmal edildiğinde eğik fırlatılan bir cismin izlediği yol bir paraboldür, çünkü yatayda sabit hızla ilerlerken dikeyde yer çekimiyle düzgün biçimde yavaşlar ve sonra hızlanır; bu yüzden basketbol topunun yayı ya da bir fıskiyeden çıkan suyun izi parabol biçimindedir.",
            "Çanak antenler ve bazı el fenerlerinin yansıtıcıları da parabol kesitlidir. Parabolün eksenine paralel gelen ışınlar yansıyınca tek bir noktada, odak noktasında toplanır. Kapaktaki öğrencilerin karşılaştırdığı köprü kemeri, su yayı ve çanak anten, aynı matematiksel eğrinin farklı kullanımlarıdır. Hepsinde ortak olan, eğrinin tek bir eksene göre simetrik olması ve bir tepe noktasından iki kola ayrılmasıdır.",
        ]},
        {"baslik": "Temel parabol: y = x²", "icerik": [
            "En basit parabol $y=x^2$ dir. Değer tablosu kurulunca parabolün simetrisi hemen görülür: $x$ ile $-x$ aynı $y$ değerini verir.",
            tablo(["$x$", "$-2$", "$-1$", "$0$", "$1$", "$2$"], [
                ["$y=x^2$", "$4$", "$1$", "$0$", "$1$", "$4$"],
            ]),
            koordinat_grafik("Temel parabol y = x²", [("y = x²", lambda x: x * x)], (-3, 3), (-1, 5),
                             noktalar=[(-2, 4, "(−2, 4)", True), (-1, 1, "", True), (0, 0, "(0, 0)", True), (1, 1, "", True), (2, 4, "(2, 4)", True)]),
            "Bu parabolün tepe noktası başlangıç noktasıdır, simetri ekseni $y$ eksenidir ve kolları yukarı bakar. Diğer bütün paraboller bu eğrinin ötelenmesi, uzatılması ya da ters çevrilmesiyle elde edilir. Tablodaki değerler, eğrinin tepe noktasından uzaklaştıkça giderek daha hızlı yükseldiğini de gösterir: $x$ bir birim arttığında $y$ önce $1$, sonra $3$ birim artar.",
        ]},
        {"baslik": "Baş katsayının etkisi", "icerik": [
            "Baş katsayı $a$ parabolün hem yönünü hem genişliğini belirler. $a$ pozitifse kollar yukarı, negatifse aşağı bakar. $a$ nın mutlak değeri büyüdükçe parabol daralır, küçüldükçe genişler.",
            koordinat_grafik("Baş katsayının etkisi: y = x², y = 2x², y = x²/2 ve y = −x²",
                             [("y = x²", lambda x: x * x), ("y = 2x²", lambda x: 2 * x * x), ("y = x²/2", lambda x: x * x / 2), ("y = −x²", lambda x: -x * x)],
                             (-3, 3), (-4, 5)),
            tablo(["$a$", "Kolların yönü", "Genişlik"], [
                ["$a>0$", "Yukarı", "$|a|$ büyüdükçe dar"],
                ["$a<0$", "Aşağı", "$|a|$ büyüdükçe dar"],
            ]),
            dikkat(
                "Negatif baş katsayıyı yalnızca konum değişikliği sanmak.",
                "$y=-x^2$ parabolü $y=x^2$ nin aşağı kaydırılmışı değil, $x$ eksenine göre yansımasıdır. Kollar aşağı döner ve tepe noktası artık en büyük değer olur."),
        ]},
        {"baslik": "Simetri ekseni", "icerik": [
            "Her parabol, tepe noktasından geçen dikey bir doğruya göre simetriktir. Bu doğruya <strong>simetri ekseni</strong> denir ve denklemi şudur:",
            "$$x=-\\dfrac{b}{2a}$$",
            "Simetri ekseni, köklerin tam ortasından geçer; çünkü kökler toplamı $-\\dfrac{b}{a}$ dir ve bunun yarısı $-\\dfrac{b}{2a}$ dir. Daha genel olarak, parabolde aynı yükseklikteki iki noktanın yatay konumlarının ortalaması her zaman simetri eksenini verir.",
            ornek(
                "$y=x^2-4x+3$ parabolü verilsin.",
                "Simetri eksenini bulup simetrik iki noktayı gösterelim.",
                "$x=-\\dfrac{-4}{2}=2$.",
                "$x=0$ ve $x=4$ simetri eksenine eşit uzaklıktadır ve iki noktada da $y=3$ tür."),
        ]},
        {"baslik": "Tepe noktası", "icerik": [
            "Parabolün simetri ekseni üzerindeki noktasına <strong>tepe noktası</strong> denir. Tepe noktasının yatay koordinatı simetri eksenidir, dikey koordinatı ise fonksiyonun o noktadaki değeridir:",
            "$$r=-\\dfrac{b}{2a}$$",
            "$$k=f(r)$$",
            ornek(
                "$y=x^2-4x+3$ parabolü verilsin.",
                "Tepe noktasını bulalım.",
                "$r=2$ ve $k=4-8+3=-1$.",
                "Tepe noktası $T(2, -1)$ dir."),
            "Tepe noktasının dikey koordinatı $k=-\\dfrac{\\Delta}{4a}$ formülüyle de bulunur. Bu örnekte $\\Delta=16-12=4$ ve $k=-\\dfrac{4}{4}=-1$ dir. Ayrıntısı <a href=\"/blog/parabol-tepe-noktasi/\">Parabolün Tepe Noktası Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Eksenleri kestiği noktalar", "icerik": [
            "Parabolün $y$ eksenini kestiği nokta $(0, c)$ dir, çünkü $x=0$ yazılınca geriye yalnızca sabit terim kalır. $x$ eksenini kestiği noktalar ise $ax^2+bx+c=0$ denkleminin kökleridir.",
            ornek(
                "$y=x^2-4x+3$ parabolü verilsin.",
                "Eksenleri kestiği noktaları bulalım.",
                "$y$ ekseni: $(0, 3)$.",
                "$x$ ekseni: $x^2-4x+3=0$, yani $(x-1)(x-3)=0$; noktalar $(1, 0)$ ve $(3, 0)$."),
            koordinat_grafik("y = x² − 4x + 3 parabolü: tepe noktası, simetri ekseni ve eksen kesişimleri", [("y = x² − 4x + 3", lambda x: x * x - 4 * x + 3)], (-1, 5), (-2, 5),
                             dikeyler=[2], noktalar=[(2, -1, "T(2, −1)", True), (1, 0, "(1, 0)", True), (3, 0, "(3, 0)", True), (0, 3, "(0, 3)", True), (4, 3, "(4, 3)", True)]),
            "$x$ eksenini kaç noktada kestiği diskriminantla belirlenir: pozitifse iki, sıfırsa bir, negatifse hiç. Ayrıntısı <a href=\"/blog/diskriminant-delta/\">Diskriminant Nedir? Delta Nasıl Hesaplanır?</a> yazısında.",
        ]},
        {"baslik": "Parabol denkleminin üç biçimi", "icerik": [
            "Aynı parabol üç farklı biçimde yazılabilir ve her biçim parabolün farklı bir özelliğini doğrudan gösterir. Soru hangi bilgiyi veriyorsa ona uygun biçimle başlamak, çözümü kısaltır.",
            tablo(["Biçim", "Denklem", "Doğrudan okunan"], [
                ["Genel biçim", "$y=ax^2+bx+c$", "$y$ ekseni kesişimi $c$"],
                ["Tepe noktası biçimi", "$y=a(x-r)^2+k$", "Tepe noktası $(r, k)$"],
                ["Kök biçimi", "$y=a(x-x_1)(x-x_2)$", "Kökler $x_1$ ve $x_2$"],
            ]),
            ornek(
                "$y=x^2-4x+3$ parabolü verilsin.",
                "Parabolü üç biçimde yazalım.",
                "Genel biçim: $y=x^2-4x+3$.",
                "Tepe noktası biçimi: $y=(x-2)^2-1$. Kök biçimi: $y=(x-1)(x-3)$."),
            "Parabol denklemini verilen bilgilerden kurmanın ayrıntısı <a href=\"/blog/parabol-denklemi/\">Parabol Denklemi Nasıl Yazılır?</a> yazısında.",
        ]},
        {"baslik": "Tepe noktası biçiminden okumak", "icerik": [
            "Denklem $y=a(x-r)^2+k$ biçiminde verilmişse tepe noktası hesap yapmadan okunur. Parantez içindeki işarete dikkat edilmelidir: $(x-r)$ ifadesinde tepe noktasının yatay koordinatı $r$ dir, $-r$ değil.",
            ornek(
                "$y=2(x-1)^2-8$ parabolü verilsin.",
                "Tepe noktasını ve kökleri bulalım.",
                "Tepe noktası $(1, -8)$ dir; $a=2>0$ olduğu için bu bir en küçük değerdir.",
                "Kökler: $2(x-1)^2=8$, yani $(x-1)^2=4$ ve $x=3$ ya da $x=-1$."),
        ]},
        {"baslik": "Kök biçiminden okumak", "icerik": [
            "Denklem çarpanlarına ayrılmış biçimdeyse kökler doğrudan okunur. Simetri ekseni köklerin ortalamasıdır; tepe noktası da bu değerin denklemde yerine yazılmasıyla bulunur.",
            ornek(
                "$y=(x+1)(x-3)$ parabolü verilsin.",
                "Kökleri, simetri eksenini ve tepe noktasını bulalım.",
                "Kökler $-1$ ve $3$ tür.",
                "Simetri ekseni $x=\\dfrac{-1+3}{2}=1$; tepe noktası $(1, 2 \\cdot (-2))=(1, -4)$ tür."),
        ]},
        {"baslik": "En büyük ve en küçük değer", "icerik": [
            "Kolları yukarı bakan bir parabol tepe noktasında en küçük değerini alır ve en büyük değeri yoktur. Kolları aşağı bakan bir parabol ise tepe noktasında en büyük değerini alır ve en küçük değeri yoktur.",
            ornek(
                "$y=-x^2+6x-5$ parabolü verilsin.",
                "En büyük değerini bulalım.",
                "$a=-1<0$; kollar aşağı bakar. $r=-\\dfrac{6}{-2}=3$.",
                "$k=-9+18-5=4$. En büyük değer $4$ tür ve $x=3$ te alınır."),
            koordinat_grafik("y = −x² + 6x − 5 parabolü tepe noktasında en büyük değerini alır", [("y = −x² + 6x − 5", lambda x: -x * x + 6 * x - 5)], (-1, 7), (-3, 5),
                             dikeyler=[3], noktalar=[(3, 4, "T(3, 4)", True), (1, 0, "(1, 0)", True), (5, 0, "(5, 0)", True)]),
        ]},
        {"baslik": "Görüntü kümesi", "icerik": [
            "Tanım kümesi bütün gerçek sayılar olan bir parabolün görüntü kümesi, tepe noktasının dikey koordinatından başlar. Kollar yukarı bakıyorsa görüntü kümesi $[k, \\infty)$, aşağı bakıyorsa $(-\\infty, k]$ aralığıdır.",
            ornek(
                "$y=x^2-4x+3$ ve $y=-x^2+6x-5$ fonksiyonları verilsin.",
                "Görüntü kümelerini bulalım.",
                "Birinci parabolün tepesi $(2, -1)$ ve kolları yukarıdır: görüntü kümesi $[-1, \\infty)$.",
                "İkinci parabolün tepesi $(3, 4)$ ve kolları aşağıdır: görüntü kümesi $(-\\infty, 4]$."),
        ]},
        {"baslik": "Artan ve azalan aralıklar", "icerik": [
            "Parabol, simetri ekseninin bir yanında artan, öteki yanında azalandır. Kollar yukarı bakıyorsa fonksiyon tepe noktasına kadar azalır, sonra artar. Kollar aşağı bakıyorsa önce artar, sonra azalır.",
            ornek(
                "$y=x^2-4x+3$ parabolü verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "Simetri ekseni $x=2$ ve kollar yukarıdır.",
                "Fonksiyon $(-\\infty, 2]$ aralığında azalan, $[2, \\infty)$ aralığında artandır."),
        ]},
        {"baslik": "Kapalı aralıkta en büyük ve en küçük değer", "icerik": [
            "Tanım kümesi kapalı bir aralıkla sınırlandırıldığında en büyük ve en küçük değer aralığın uçlarında ya da tepe noktasında alınır. Tepe noktası aralığın içindeyse o da hesaba katılır; dışındaysa yalnızca uçlara bakılır.",
            ornek(
                "$[0, 5]$ aralığında $f(x)=x^2-4x+3$ fonksiyonu verilsin.",
                "En büyük ve en küçük değerleri bulalım.",
                "Tepe noktası $x=2$ aralığın içindedir: $f(2)=-1$.",
                "Uçlar: $f(0)=3$ ve $f(5)=25-20+3=8$.",
                "En küçük değer $-1$, en büyük değer $8$ dir."),
            dikkat(
                "Kapalı aralıkta yalnızca uçlara bakmak.",
                "Uçlardaki değerler $3$ ve $8$ dir; yalnızca bunlara bakılsaydı en küçük değer yanlış olarak $3$ bulunurdu. Tepe noktası aralığın içinde olduğunda en küçük ya da en büyük değer oradadır."),
        ]},
        {"baslik": "Parabolün işareti", "icerik": [
            "Parabolün $x$ ekseninin üstünde kaldığı yerlerde fonksiyon pozitif, altında kaldığı yerlerde negatiftir. Kökler, işaretin değişebileceği noktalardır. Kolları yukarı bakan ve iki kökü olan bir parabol kökler arasında negatif, dışında pozitiftir.",
            ornek(
                "$y=x^2-4x+3$ parabolü verilsin.",
                "Fonksiyonun negatif olduğu aralığı bulalım.",
                "Kökler $1$ ve $3$, kollar yukarı.",
                "Fonksiyon $(1, 3)$ aralığında negatiftir."),
            "Bu işaret incelemesi ikinci dereceden eşitsizliklerin çözümünün temelidir. Ayrıntısı <a href=\"/blog/esitsizlikler-konu-anlatimi-pdf/\">Eşitsizlikler Konu Anlatımı PDF</a> yazısında.",
        ]},
        {"baslik": "Parabolün ötelenmesi", "icerik": [
            "Tepe noktası biçimi, parabolün $y=ax^2$ nin ötelenmiş hâli olduğunu gösterir: $y=a(x-r)^2+k$ parabolü, $y=ax^2$ parabolünün $r$ birim yatay ve $k$ birim dikey ötelenmesidir. Parabolün biçimi değişmez, yalnızca yeri değişir. Bu yüzden baş katsayı ötelemeden etkilenmez; ötelenen parabolün kolları aynı yöne bakar ve aynı genişliktedir.",
            ornek(
                "$y=x^2$ parabolü $2$ birim sağa ve $3$ birim yukarı ötelensin.",
                "Yeni parabolün denklemini yazalım.",
                "Tepe noktası $(0, 0)$ dan $(2, 3)$ e taşınır.",
                "$y=(x-2)^2+3=x^2-4x+7$."),
        ]},
        {"baslik": "En büyük alan problemi", "icerik": [
            "Parabolün tepe noktası, en büyük ya da en küçük değer isteyen problemlerin çözüm aracıdır. Problem bir ikinci dereceden fonksiyona dönüştürülür ve tepe noktası bulunur.",
            ornek(
                "Çevresi $20$ metre olan dikdörtgenlerin alanı inceleniyor.",
                "En büyük alanı ve bu alanı veren kenarları bulalım.",
                "Bir kenar $x$ ise diğer kenar $10-x$ tir; alan $A(x)=x(10-x)=-x^2+10x$.",
                "Tepe noktası $x=5$; alan $A(5)=25$. En büyük alan $25$ metrekaredir ve dikdörtgen bir karedir."),
        ]},
        {"baslik": "Atış problemi", "icerik": [
            "Yukarı doğru atılan bir cismin yüksekliği, hava direnci ihmal edildiğinde zamanın ikinci dereceden bir fonksiyonudur. Tepe noktası en yüksek noktayı, kökler de cismin yerde olduğu anları verir.",
            ornek(
                "Bir topun $t$ saniye sonraki yüksekliği metre cinsinden $h(t)=-5t^2+20t$ ile veriliyor.",
                "Topun ulaştığı en büyük yüksekliği ve yere düştüğü anı bulalım.",
                "Tepe noktası: $t=-\\dfrac{20}{-10}=2$ ve $h(2)=-20+40=20$. En büyük yükseklik $20$ metredir.",
                "Yere düşüş: $-5t^2+20t=0$, yani $t=0$ ya da $t=4$. Top $4$ saniye sonra yere düşer."),
            "Simetri burada da görülür: top en yüksek noktaya $2$ saniyede çıkar ve oradan yere yine $2$ saniyede iner. Aynı yükseklikten çıkış ve iniş anları da simetriktir; örneğin top $15$ metre yüksekliğe $1$. saniyede çıkarken ulaşır ve $3$. saniyede inerken yeniden oradadır.",
        ]},
        {"baslik": "Grafikten katsayıların işaretini okumak", "icerik": [
            "Denklemi verilmeyen bir parabolün grafiğinden katsayıların işaretleri okunabilir. Her katsayı parabolün farklı bir özelliğine bağlıdır ve üçü ayrı ayrı belirlenir.",
            tablo(["Katsayı", "Grafikte bakılan yer", "Kural"], [
                ["$a$", "Kolların yönü", "Yukarı ise pozitif, aşağı ise negatif"],
                ["$c$", "$y$ ekseni kesişimi", "Eksenin üstünde pozitif, altında negatif"],
                ["$b$", "Simetri ekseninin yeri", "$a$ ile $r$ aynı işaretliyse $b$ negatif"],
            ]),
            ornek(
                "Kolları yukarı bakan, tepe noktası $y$ ekseninin sağında olan ve $y$ eksenini eksenin altında kesen bir parabol verilsin.",
                "$a$, $b$ ve $c$ nin işaretlerini bulalım.",
                "Kollar yukarı: $a>0$. $y$ ekseni kesişimi negatif: $c<0$.",
                "Simetri ekseni $r=-\\dfrac{b}{2a}$ pozitiftir ve $a>0$ olduğu için $b<0$ dır. Örneğin $y=x^2-4x-1$ bu parabole uyar."),
            "$b$ nin kuralı simetri ekseni formülünden gelir: $r$ ile $a$ aynı işaretliyse $-\\dfrac{b}{2a}$ nin pozitif çıkması için $b$ negatif olmalıdır. Simetri ekseni $y$ ekseninin üzerindeyse $b=0$ dır.",
        ]},
        {"baslik": "Parabol ve doğru", "icerik": [
            "Bir parabol ile bir doğrunun ortak noktaları, iki denklemin eşitlenmesiyle bulunur. Ortaya çıkan ikinci dereceden denklemin diskriminantı, doğrunun parabolü iki noktada kestiğini, parabole teğet olduğunu ya da parabolü hiç kesmediğini söyler.",
            "Ayrıntısı <a href=\"/blog/parabol-ve-dogru/\">Parabol ve Doğrunun Birbirine Göre Durumları</a> yazısında, grafiğin adım adım çizimi de <a href=\"/blog/parabol-grafigi/\">Parabol Grafiği Nasıl Çizilir?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sınavda parabol", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) parabol; tepe noktası, simetri ekseni, eksen kesişimleri, denklem yazma, en büyük ve en küçük değer, görüntü kümesi ve parabol ile doğrunun durumları biçiminde karşına çıkabilir.",
                "Grafiği verilen bir parabolden katsayıların işaretlerini ya da denklemi bulmak da sık kullanılan bir soru biçimidir."),
            "Parabol sorularında ilk iş tepe noktasını bulmaktır. Tepe noktası bilindiğinde simetri ekseni, en büyük ya da en küçük değer, görüntü kümesi ve artan azalan aralıklar hemen okunur; sorunun çoğu bu tek noktadan çözülür.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Simetri eksenini $\\dfrac{b}{2a}$ almak", "$x=-\\dfrac{b}{2a}$"],
                ["$y=(x-2)^2$ nin tepesini $(-2, 0)$ sanmak", "Tepe $(2, 0)$"],
                ["Negatif $a$ da tepeyi en küçük değer sanmak", "$a<0$ ise en büyük değer"],
                ["Kapalı aralıkta tepe noktasını unutmak", "Tepe aralıktaysa hesaba katılır"],
                ["Baş katsayı parametreliyken $a \\neq 0$ ı unutmak", "Parabol için $a \\neq 0$"],
                ["$y$ ekseni kesişimini kökle karıştırmak", "$y$ ekseni kesişimi $(0, c)$"],
            ]),
            "Bu hataların çoğu, işaretlerin ve parantezlerin aceleyle okunmasından doğar. Tepe noktasını bulduktan sonra onu denklemde yerine yazıp doğru değeri verdiğini kontrol etmek, hataların büyük bölümünü yakalar.",
        ]},
    ],
    "sss": [
        ("Parabol nedir?",
         "a sıfırdan farklı olmak üzere y eşittir ax kare artı bx artı c fonksiyonunun grafiğidir. Bir tepe noktası ve bir simetri ekseni vardır."),
        ("Parabolün kollarının yönü neye bağlıdır?",
         "Baş katsayının işaretine bağlıdır. a pozitifse kollar yukarı, negatifse aşağı bakar."),
        ("Simetri ekseni nasıl bulunur?",
         "x eşittir eksi b bölü 2a doğrusudur. Köklerin tam ortasından geçer."),
        ("Tepe noktası nasıl bulunur?",
         "Yatay koordinat eksi b bölü 2a dır; dikey koordinat bu değerin fonksiyonda yerine yazılmasıyla bulunur."),
        ("Parabolün en büyük değeri ne zaman vardır?",
         "Kollar aşağı bakıyorsa, yani a negatifse tepe noktasında en büyük değer vardır. Kollar yukarı bakıyorsa en büyük değer yoktur."),
        ("Parabolün görüntü kümesi nasıl bulunur?",
         "Tepe noktasının dikey koordinatı k olmak üzere kollar yukarıysa k dan sonsuza, aşağıysa eksi sonsuzdan k ya kadar olan aralıktır."),
        ("Grafikten b katsayısının işareti nasıl bulunur?",
         "Simetri ekseninin yerine bakılır. a ile simetri ekseninin yatay konumu aynı işaretliyse b negatif, ters işaretliyse b pozitiftir."),
    ],
    "kontrol": [
        "Parabolün tanımını ve a ≠ 0 koşulunu açıklayabiliyorum.",
        "Baş katsayının kolların yönüne ve genişliğine etkisini biliyorum.",
        "Simetri eksenini bulabiliyorum.",
        "Tepe noktasını hesaplayabiliyorum.",
        "Parabolün eksenleri kestiği noktaları bulabiliyorum.",
        "Parabol denklemini üç biçimde yazabiliyorum.",
        "En büyük ya da en küçük değeri bulabiliyorum.",
        "Görüntü kümesini ve artan azalan aralıkları belirleyebiliyorum.",
        "Kapalı aralıkta en büyük ve en küçük değeri bulabiliyorum.",
        "En büyük alan ve atış problemlerini parabolle çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["parabol-tepe-noktasi", "parabol-grafigi", "ikinci-dereceden-denklemler"],
}
