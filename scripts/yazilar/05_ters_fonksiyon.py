# scripts/yazilar/05_ters_fonksiyon.py — besinci blog yazisi (23.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "ters-fonksiyon",
    "baslik": "Ters Fonksiyon Nasıl Bulunur?",
    "aciklama": "Ters fonksiyon nedir, ne zaman vardır, nasıl bulunur? Doğrusal, kesirli, köklü ve üslü fonksiyonların tersi, özellikler ve grafik; çözümlü örneklerle.",
    "tarih": "2026-09-23",
    "guncelleme": None,
    "kategori": "fonksiyonlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "ters-fonksiyon",
    "kapak_alt": "Ters fonksiyon nasıl bulunur: katlanmış origami kâğıdını adım adım açarak başlangıçtaki düz kâğıda geri döndüren iki öğrenci",
    "ozet": "Bir fonksiyon girdiyi çıktıya götürür; ters fonksiyon ise çıktıdan yola çıkıp girdiye geri döner. Katlanmış bir kâğıdı katları tersten açarak eski hâline getirmek gibi. Bu yazıda ters fonksiyonun ne zaman var olduğunu, adım adım nasıl bulunduğunu, kesirli, köklü ve üslü fonksiyonlarda nelere dikkat edileceğini, tersi bulmadan değer hesaplamayı ve grafikteki simetriyi ele alıyoruz.",
    "bolumler": [
        {"baslik": "Ters fonksiyon nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birebir ve örten fonksiyon kavramlarını, bileşke fonksiyonu ve denklemde bir bilinmeyeni yalnız bırakmayı biliyor olman yeterli.",
                "Bu kavramlar yeni geliyorsa önce <a href=\"/blog/birebir-orten-fonksiyon/\">Birebir ve Örten Fonksiyon Nedir?</a> ve <a href=\"/blog/bileske-fonksiyon/\">Bileşke Fonksiyon Konu Anlatımı</a> yazılarına göz at."),
            "Bir kâğıdı önce ikiye, sonra köşesinden katladığını düşün. Başlangıçtaki düz kâğıda dönmek için katları <strong>ters sırayla</strong> açarsın: önce son katı, sonra ilkini. Ters fonksiyon da budur: fonksiyonun yaptığını geri alır.",
            "Matematikte şöyle yazılır: $f:A \\to B$ birebir ve örten bir fonksiyon olsun. $f(a)=b$ ise $f^{-1}(b)=a$ dır. $f^{-1}$ fonksiyonu $B$ den $A$ ya gider ve \"$f$ nin tersi\" diye okunur.",
            "$$f(a)=b \\Leftrightarrow f^{-1}(b)=a$$",
            hap("$f(a)=b$ ise $f^{-1}(b)=a$ dır: ters fonksiyon çıktıdan girdiye döner.",
                "$f:A \\to B$ ise $f^{-1}:B \\to A$ dır; tanım ve değer kümeleri yer değiştirir."),
            dikkat(
                "$f^{-1}(x)$ ile $\\dfrac{1}{f(x)}$ aynı şey değildir.",
                "Buradaki $-1$ bir üs değil, ters fonksiyon işaretidir."),
        ]},
        {"baslik": "Ters fonksiyon ne zaman vardır?", "icerik": [
            "Geri dönebilmek için iki şey gerekir. Her çıktının <strong>tek bir</strong> girdiden gelmesi gerekir, yoksa geri dönerken hangi girdiye gideceğimizi bilemeyiz. Bu birebirliktir. Değer kümesindeki <strong>her</strong> elemanın bir girdiden gelmesi de gerekir, yoksa boşta kalan eleman hiçbir yere dönemez. Bu da örtenliktir.",
            hap("$f^{-1}$ in fonksiyon olarak var olması için $f$ nin birebir <strong>ve</strong> örten olması gerekir ve yeter.",
                "Ters fonksiyon aramaya başlamadan önce bu şartı kontrol et."),
            ornek(
                "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=x^2$ olsun.",
                "$f$ nin tersi var mıdır?",
                "$f(-3)=f(3)=9$ olduğu için $f$ birebir değildir. Geri dönerken $9$ dan hem $-3$ e hem $3$ e gitmek gerekirdi.",
                "Ayrıca negatif sayılara hiç ok gelmez; $f$ örten de değildir.",
                "Bu hâliyle $f$ nin tersi yoktur."),
            "Tanım ve değer kümesi uygun biçimde daraltılırsa aynı kuralın tersi olabilir. $f:[0,\\infty) \\to [0,\\infty)$, $f(x)=x^2$ birebir ve örtendir; tersi $f^{-1}(x)=\\sqrt{x}$ tir. Karekök fonksiyonunun yalnızca negatif olmayan değeri vermesinin sebebi budur.",
        ]},
        {"baslik": "Adım adım ters fonksiyon bulma", "icerik": [
            "Kural verilmiş bir fonksiyonun tersini bulmak için üç adım yeter:",
            "<ol><li>$y=f(x)$ yaz.</li><li>Denklemi $x$ i yalnız bırakacak biçimde çöz.</li><li>$x$ ile $y$ nin yerini değiştir.</li></ol>",
            "Üçüncü adımın sebebi şudur: ikinci adımın sonunda elinde $x=f^{-1}(y)$ biçiminde bir eşitlik vardır. Fonksiyonların değişkenini $x$ ile yazmak alışkanlık olduğu için harfler değiştirilir.",
            ornek(
                "$f(x)=4x-7$ olsun.",
                "$f^{-1}(x)$ i bulalım.",
                "$y=4x-7$ yazalım.",
                "$x$ i yalnız bırakalım: $4x=y+7$ ve $x=\\dfrac{y+7}{4}$.",
                "Harfleri değiştirelim: $f^{-1}(x)=\\dfrac{x+7}{4}$.",
                "Kontrol: $f(2)=8-7=1$ ve $f^{-1}(1)=\\dfrac{1+7}{4}=2$. Başladığımız yere döndük."),
            "Doğrusal fonksiyonlar için bu işlemin genel sonucu doğrudan kullanılabilir:",
            "$$f(x)=ax+b \\ (a \\neq 0) \\Rightarrow f^{-1}(x)=\\frac{x-b}{a}$$",
            "Bunu \"ters işlem, ters sıra\" diye hatırlayabilirsin. $f$ önce $a$ ile çarpar, sonra $b$ ekler. $f^{-1}$ önce $b$ çıkarır, sonra $a$ ya böler.",
            hap("Ters fonksiyonu bulduktan sonra bir sayıyla kontrol et: $f(a)=b$ ise $f^{-1}(b)=a$ çıkmalı.",
                "Doğrusal fonksiyonda $f(x)=ax+b$ ise $f^{-1}(x)=\\dfrac{x-b}{a}$."),
        ]},
        {"baslik": "Kesirli fonksiyonun tersi", "icerik": [
            "$f(x)=\\dfrac{ax+b}{cx+d}$ biçimindeki fonksiyonlarda adımlar aynıdır ama cebir biraz daha uzundur.",
            ornek(
                "$f(x)=\\dfrac{3x-2}{x+4}$ olsun.",
                "$f^{-1}(x)$ i bulalım.",
                "$y=\\dfrac{3x-2}{x+4}$ yazıp paydayı karşıya atalım: $y(x+4)=3x-2$.",
                "Dağıtalım: $xy+4y=3x-2$.",
                "$x$ li terimleri bir tarafta toplayalım: $xy-3x=-4y-2$, yani $x(y-3)=-4y-2$.",
                "$x=\\dfrac{-4y-2}{y-3}$.",
                "Harfleri değiştirelim: $f^{-1}(x)=\\dfrac{-4x-2}{x-3}$.",
                "Kontrol: $f(0)=-\\dfrac{2}{4}=-\\dfrac{1}{2}$ ve $f^{-1}\\left(-\\dfrac{1}{2}\\right)=\\dfrac{2-2}{-\\frac{1}{2}-3}=0$."),
            "Bu işlemi genel harflerle yaparsak akılda kalıcı bir kalıp çıkar:",
            "$$f(x)=\\frac{ax+b}{cx+d} \\Rightarrow f^{-1}(x)=\\frac{-dx+b}{cx-a}$$",
            "Kalıbı hatırlamanın yolu: $a$ ile $d$ <strong>yer değiştirir</strong> ve ikisinin de <strong>işareti değişir</strong>; $b$ ile $c$ olduğu yerde kalır. Kalıp $ad-bc \\neq 0$ için geçerlidir; $ad-bc=0$ ise fonksiyon sabittir ve tersi yoktur.",
            hap("$f(x)=\\dfrac{ax+b}{cx+d}$ ise $f^{-1}(x)=\\dfrac{-dx+b}{cx-a}$ dir.",
                "$a$ ile $d$ yer ve işaret değiştirir, $b$ ile $c$ kalır."),
            dikkat(
                "$a+d=0$ ise kalıp fonksiyonun kendisini verir; böyle bir fonksiyon <strong>kendi tersidir</strong>.",
                "Örneğin $f(x)=\\dfrac{x+4}{2x-1}$ için $a=1$ ve $d=-1$ dir. Kalıp $f^{-1}(x)=\\dfrac{x+4}{2x-1}$ verir, yani $f^{-1}=f$ dir."),
        ]},
        {"baslik": "Tersin tanım ve görüntü kümesi", "icerik": [
            "$f:A \\to B$ birebir örtense $f^{-1}:B \\to A$ dır. Yani tersin tanım kümesi $f$ nin görüntü kümesidir; tersin görüntü kümesi de $f$ nin tanım kümesidir. Bu bilgi hem kontrol hem kısayol olarak işe yarar.",
            ornek(
                "$f(x)=\\dfrac{3x-2}{x+4}$ ve $f^{-1}(x)=\\dfrac{-4x-2}{x-3}$ olsun.",
                "İki fonksiyonun tanım ve görüntü kümelerini karşılaştıralım.",
                "$f$ nin tanım kümesi $\\mathbb{R}-\\{-4\\}$ tür. Görüntü kümesi $\\mathbb{R}-\\{3\\}$ tür, çünkü pay ile paydadaki $x$ katsayılarının oranı $\\dfrac{3}{1}=3$ tür.",
                "$f^{-1}$ in tanım kümesi $\\mathbb{R}-\\{3\\}$ tür. Görüntü kümesi $\\mathbb{R}-\\{-4\\}$ tür, çünkü bu kez oran $\\dfrac{-4}{1}=-4$ tür.",
                "İki küme yer değiştirdi."),
            "Bu ilişkiyi tersine de kullanabilirsin: bir fonksiyonun görüntü kümesini bulmakta zorlanıyorsan, tersini bulup tersin tanım kümesine bakabilirsin.",
            ornek(
                "$f:[-1,\\infty) \\to (-\\infty,3]$, $f(x)=3-\\sqrt{x+1}$ olsun.",
                "$f^{-1}$ i tanım kümesiyle birlikte bulalım.",
                "$y=3-\\sqrt{x+1}$ yazalım. Kök negatif olmadığı için $y \\leq 3$ tür.",
                "$\\sqrt{x+1}=3-y$. İki tarafın karesini alalım: $x+1=(3-y)^2$.",
                "$x=(3-y)^2-1$.",
                "Harfleri değiştirelim: $f^{-1}:(-\\infty,3] \\to [-1,\\infty)$, $f^{-1}(x)=(3-x)^2-1$.",
                "Kontrol: $f(8)=3-3=0$ ve $f^{-1}(0)=9-1=8$."),
        ]},
        {"baslik": "Köklü, ikinci dereceden ve üslü fonksiyonlar", "icerik": [
            "Bu fonksiyonlarda üç adım yine aynıdır. Fark, <strong>tanım ve değer kümelerinin</strong> tersin kuralına eklenmesi gerekmesidir. Küme yazılmazsa bulunan kural başka bir fonksiyonu anlatır.",
            ornek(
                "$f:[2,\\infty) \\to [1,\\infty)$, $f(x)=\\sqrt{x-2}+1$ olsun.",
                "$f^{-1}(x)$ i bulalım.",
                "$y=\\sqrt{x-2}+1$ yazalım. Burada $y \\geq 1$ dir.",
                "$y-1=\\sqrt{x-2}$. İki tarafın karesini alalım: $(y-1)^2=x-2$.",
                "$x=(y-1)^2+2$.",
                "Harfleri değiştirelim: $f^{-1}:[1,\\infty) \\to [2,\\infty)$, $f^{-1}(x)=(x-1)^2+2$.",
                "Kontrol: $f(6)=\\sqrt{4}+1=3$ ve $f^{-1}(3)=4+2=6$."),
            dikkat(
                "Tersin tanım kümesini yazmayı unutma.",
                "$(x-1)^2+2$ kuralı $\\mathbb{R}$ üzerinde birebir değildir. Bu kural ancak $x \\geq 1$ ile birlikte $f$ nin tersidir; tanım kümesi, $f$ nin görüntü kümesi olan $[1,\\infty)$ dur."),
            "İkinci dereceden bir fonksiyon, tepe noktasından başlayan bir aralıkta birebirdir. O aralıkta tam kareye tamamlama tersini kolayca verir.",
            ornek(
                "$f:[1,\\infty) \\to [-3,\\infty)$, $f(x)=x^2-2x-2$ olsun.",
                "$f^{-1}(x)$ i bulalım.",
                "Tam kareye tamamlayalım: $x^2-2x-2=(x-1)^2-3$. Yani $y=(x-1)^2-3$.",
                "$(x-1)^2=y+3$. Burada $x \\geq 1$ olduğu için $x-1 \\geq 0$ dır ve karekökün yalnız pozitif değeri alınır: $x-1=\\sqrt{y+3}$.",
                "$x=1+\\sqrt{y+3}$ ve $f^{-1}(x)=1+\\sqrt{x+3}$.",
                "Kontrol: $f(3)=9-6-2=1$ ve $f^{-1}(1)=1+\\sqrt{4}=3$."),
            "Üslü fonksiyonun tersi logaritmadır. $f:\\mathbb{R} \\to (3,\\infty)$, $f(x)=2^{x-1}+3$ için $y-3=2^{x-1}$ ve $x-1=\\log_{2}(y-3)$ bulunur. Öyleyse $f^{-1}(x)=\\log_{2}(x-3)+1$ dir. Kontrol: $f(3)=4+3=7$ ve $f^{-1}(7)=\\log_{2} 4+1=3$.",
            hap("Köklü ve ikinci dereceden fonksiyonun tersinde tanım kümesi kuralın bir parçasıdır.",
                "$f^{-1}$ in tanım kümesi $f$ nin görüntü kümesidir."),
        ]},
        {"baslik": "Tersi bulmadan değer hesaplama", "icerik": [
            "Yalnızca $f^{-1}(a)$ gibi tek bir değer isteniyorsa tersin kuralını bulmak şart değildir. $f^{-1}(a)=b$ demek $f(b)=a$ demektir. Yani $f(x)=a$ denklemini çözmek yeter.",
            ornek(
                "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=x^3+2x+1$ olsun. Bu fonksiyon artandır; birebir ve örtendir.",
                "$f^{-1}(4)$ kaçtır?",
                "$f^{-1}(4)=b$ ise $f(b)=4$ tür: $b^3+2b+1=4$, yani $b^3+2b-3=0$.",
                "$b=1$ denendiğinde $1+2-3=0$ sağlanır.",
                "$f$ birebir olduğu için başka çözüm yoktur. $f^{-1}(4)=1$ dir."),
            "Bu fonksiyonun tersini kural olarak yazmak kolay değildir, ama değer sorusu birkaç satırda çözüldü. Soruda $f^{-1}$ görünce ilk iş olarak tersin kuralını bulmaya kalkma; istenen şeyin bir değer mi yoksa kural mı olduğuna bak.",
            hap("$f^{-1}(a)=b \\Leftrightarrow f(b)=a$.",
                "Tek bir değer isteniyorsa $f(x)=a$ denklemini çöz; tersin kuralına gerek yok."),
        ]},
        {"baslik": "Değer sorularında farklı kalıplar", "icerik": [
            "Değer soruları farklı biçimlerde gelebilir. Hepsinin çözümü aynı eşdeğerliğe dayanır: $f^{-1}(a)=b \\Leftrightarrow f(b)=a$.",
            ornek(
                "$f^{-1}(x)=\\dfrac{x+1}{3}$ olsun.",
                "$f(5)$ kaçtır?",
                "$f(5)=b$ diyelim. Bu, $f^{-1}(b)=5$ demektir.",
                "$\\dfrac{b+1}{3}=5$ ve $b=14$.",
                "$f(5)=14$ tür. Kontrol: $f$ yi bulursak $f(x)=3x-1$ ve $f(5)=14$."),
            ornek(
                "$f(2x-1)=3x+2$ olsun.",
                "$f^{-1}(8)$ kaçtır?",
                "$f^{-1}(8)=b$ ise $f(b)=8$ dir. Verilen eşitlikte sağ tarafı $8$ yapan $x$ i bulalım: $3x+2=8$ ve $x=2$.",
                "Bu $x$ için parantezin içi $2x-1=3$ tür. Yani $f(3)=8$.",
                "$f^{-1}(8)=3$ tür."),
            dikkat(
                "İkinci örnekte cevap $x=2$ değil, parantezin içi olan $3$ tür.",
                "$f^{-1}(8)$, $f$ ye hangi sayı verilince $8$ çıktığını sorar; $f$ ye verilen sayı parantezin içidir."),
            "Bileşke ile birlikte gelen değer sorularında da sıra aynıdır: içten dışa. $f(x)=2x+3$ ve $g(x)=x^2$ ise $(f^{-1} \\circ g)(3)=f^{-1}(9)$ olur. $f(b)=9$ denkleminden $2b+3=9$ ve $b=3$ bulunur; sonuç $3$ tür.",
            hap("Santigrattan Fahrenhayta çeviren $f(C)=1.8C+32$ fonksiyonunun tersi $f^{-1}(F)=\\dfrac{F-32}{1.8}$ olur.", "Yurt dışındaki bir hava durumunda görülen $77$ derece Fahrenhayt, $\\dfrac{77-32}{1.8}=25$ derece santigrattır.", gunluk=True),
        ]},
        {"baslik": "Ters fonksiyonun özellikleri", "icerik": [
            "<ul>"
            "<li>$(f^{-1} \\circ f)(x)=x$ ve $(f \\circ f^{-1})(x)=x$. Fonksiyon ile tersi birbirini götürür.</li>"
            "<li>$(f^{-1})^{-1}=f$. Tersin tersi fonksiyonun kendisidir.</li>"
            "<li>$(f \\circ g)^{-1}=g^{-1} \\circ f^{-1}$. Bileşkenin tersinde sıra döner.</li>"
            "</ul>",
            ornek(
                "$f(x)=2x+1$ ve $g(x)=x-3$ olsun.",
                "$(f \\circ g)^{-1}$ i iki yoldan bulup karşılaştıralım.",
                "Birinci yol: $(f \\circ g)(x)=2(x-3)+1=2x-5$. Tersi $\\dfrac{x+5}{2}$ tir.",
                "İkinci yol: $f^{-1}(x)=\\dfrac{x-1}{2}$ ve $g^{-1}(x)=x+3$. $g^{-1}(f^{-1}(x))=\\dfrac{x-1}{2}+3=\\dfrac{x+5}{2}$.",
                "İki yol aynı sonucu verdi."),
            "Bu özellikler bileşke sorularında bir fonksiyonu yalnız bırakmak için kullanılır. Bir eşitliğin iki tarafına da <strong>soldan</strong> $f^{-1}$ uygulamak, $f$ yi ortadan kaldırır.",
            ornek(
                "$f(x)=2x-3$ ve $(f \\circ g)(x)=4x+1$ olsun.",
                "$g(x)$ i bulalım.",
                "$f(g(x))=4x+1$ eşitliğinin iki tarafına $f^{-1}$ uygulayalım: $g(x)=f^{-1}(4x+1)$.",
                "$f^{-1}(x)=\\dfrac{x+3}{2}$ olduğu için $g(x)=\\dfrac{4x+1+3}{2}=2x+2$.",
                "Kontrol: $f(2x+2)=2(2x+2)-3=4x+1$."),
        ]},
        {"baslik": "Kendi tersi olan fonksiyonlar", "icerik": [
            "Bazı fonksiyonlar kendi tersidir: $f^{-1}=f$. Bu, fonksiyonu iki kez uygulamanın her sayıyı yerine getirmesi demektir: $(f \\circ f)(x)=x$.",
            "<ul><li>$f(x)=-x$ için $f(f(x))=-(-x)=x$.</li>"
            "<li>$f(x)=5-x$ için $f(f(x))=5-(5-x)=x$.</li>"
            "<li>$f(x)=\\dfrac{1}{x}$ için ($x \\neq 0$) $f(f(x))=\\dfrac{1}{\\frac{1}{x}}=x$.</li>"
            "<li>$f(x)=\\dfrac{ax+b}{cx+d}$ biçiminde olup $a+d=0$ olan kesirli fonksiyonlar ($ad-bc \\neq 0$ şartıyla).</li></ul>",
            "Kendi tersi olan bir fonksiyonun grafiği $y=x$ doğrusuna göre kendisiyle simetriktir. Bunun sebebini bir sonraki bölümdeki simetri kuralı açıklıyor.",
            hap("$f$ kendi tersiyse $(f \\circ f)(x)=x$ tir.",
                "Kesirli fonksiyonda bunun işareti $a+d=0$ olmasıdır."),
        ]},
        {"baslik": "Grafikte ters fonksiyon", "icerik": [
            "$(a,b)$ noktası $f$ nin grafiğindeyse $f(a)=b$ dir; bu da $f^{-1}(b)=a$, yani $(b,a)$ noktasının $f^{-1}$ in grafiğinde olması demektir. $(a,b)$ ile $(b,a)$ noktaları $y=x$ doğrusuna göre simetriktir.",
            hap("$f$ ile $f^{-1}$ in grafikleri $y=x$ doğrusuna göre simetriktir.",
                "$f^{-1}$ in grafiğini çizmek için $f$ nin grafiğini $y=x$ doğrusuna göre yansıtman yeter."),
            "Bu simetriden önemli bir sonuç çıkar: $f$ ile $f^{-1}$ in grafikleri nerede kesişir? $f$ artan bir fonksiyonsa kesişim noktaları $y=x$ doğrusu üzerindedir. Yani $f(x)=f^{-1}(x)$ yerine daha kolay olan $f(x)=x$ denklemini çözmek yeter.",
            ornek(
                "$f(x)=2x-3$ olsun.",
                "$f$ ile $f^{-1}$ in grafiklerinin kesişim noktasını bulalım.",
                "$f$ artan olduğu için $f(x)=x$ denklemini çözeriz: $2x-3=x$ ve $x=3$.",
                "Kesişim noktası $(3,3)$ tür.",
                "Kontrol: $f^{-1}(x)=\\dfrac{x+3}{2}$ ve $f^{-1}(3)=3$. Nokta iki grafikte de var."),
            "Grafikten değer okumak da aynı simetriye dayanır. $f$ nin grafiği $(2,5)$ noktasından geçiyorsa $f(2)=5$ tir ve buradan hiç hesap yapmadan $f^{-1}(5)=2$ bulunur. Ayrıca $f$ artansa tersi de artandır, azalansa tersi de azalandır; yansıtma bu özelliği değiştirmez.",
            dikkat(
                "Bu kısayol yalnızca <strong>artan</strong> fonksiyonlarda güvenlidir.",
                "$f(x)=-x^3$ azalandır ve tersi $f^{-1}(x)=-\\sqrt[3]{x}$ tir. $f(1)=-1$ ve $f^{-1}(1)=-1$ olduğu için $(1,-1)$ noktası iki grafikte de vardır, ama $y=x$ doğrusu üzerinde değildir."),
        ]},
        {"baslik": "Sınavda ters fonksiyon", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) ters fonksiyon doğrusal bir fonksiyonla karşına çıkabilir: $f^{-1}(x)$ kuralı ya da $f^{-1}(a)$ gibi tek bir değer istenir. Değer sorusunda tersi bulmadan $f(x)=a$ denklemini çözmek zaman kazandırır.",
                "İleri düzeyde (<strong>AYT</strong>) kesirli, köklü ve üslü fonksiyonların tersi, $(f \\circ g)^{-1}$ ile işlem, ters fonksiyonun tanım kümesi ve grafikteki simetri öne çıkar."),
            "Soruyu okurken kendine üç şey sor. İstenen bir <strong>kural</strong> mı, bir <strong>değer</strong> mi? Fonksiyon gerçekten birebir ve örten mi? Tersin tanım kümesi yazılması gereken bir durum var mı? Bu üç soru birçok hatayı baştan önler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$f^{-1}(x)=\\dfrac{1}{f(x)}$ sanmak", "$-1$ üs değil, ters işareti"],
                ["Her fonksiyonun tersi var sanmak", "Birebir ve örten olmalı"],
                ["Harfleri değiştirmeyi unutmak", "Son adımda $x$ ile $y$ yer değiştirir"],
                ["Köklü fonksiyonun tersinde kümeyi yazmamak", "$f^{-1}$ in tanım kümesi $f$ nin görüntü kümesi"],
                ["Kesirli kalıpta $b$ ile $c$ yi değiştirmek", "Yalnız $a$ ile $d$ yer ve işaret değiştirir"],
                ["$(f \\circ g)^{-1}=f^{-1} \\circ g^{-1}$ yazmak", "Sıra döner: $g^{-1} \\circ f^{-1}$"],
                ["Değer sorusunda önce tersin kuralını aramak", "$f(x)=a$ denklemini çöz"],
                ["Her fonksiyonda $f=f^{-1}$ kesişimini $y=x$ te aramak", "Yalnız artan fonksiyonda güvenli"],
            ]),
            "Bu tabloyu bir kez gözden geçirmek bile işe yarar, ama asıl koruma her sorunun sonunda bir sayıyla kontrol yapmaktır: $f(a)=b$ ise $f^{-1}(b)=a$ çıkıyor mu?",
        ]},
    ],
    "sss": [
        ("Ters fonksiyon nedir?",
         "Bir fonksiyonun yaptığını geri alan fonksiyondur. f fonksiyonu a yı b ye götürüyorsa, ters fonksiyon b yi a ya geri götürür."),
        ("Her fonksiyonun tersi var mıdır?",
         "Hayır. Bir fonksiyonun tersinin olması için birebir ve örten olması gerekir. Örneğin gerçel sayılarda tanımlı kare fonksiyonunun tersi yoktur; tanım ve değer kümesi negatif olmayan sayılarla sınırlanırsa tersi karekök fonksiyonu olur."),
        ("Ters fonksiyon nasıl bulunur?",
         "Üç adımda bulunur. Önce y eşittir f(x) yazılır. Sonra denklem x yalnız kalacak biçimde çözülür. Son olarak x ile y nin yeri değiştirilir."),
        ("Kesirli fonksiyonun tersi için kısa yol var mı?",
         "Var. Pay ax artı b, payda cx artı d ise tersin payı eksi dx artı b, paydası cx eksi a olur. Yani a ile d yer değiştirir ve işaretleri değişir, b ile c yerinde kalır."),
        ("f üzeri eksi bir ile bir bölü f aynı şey midir?",
         "Hayır. f üzeri eksi bir ters fonksiyonu gösterir, buradaki eksi bir bir üs değildir. Bir bölü f ise fonksiyonun değerinin çarpmaya göre tersidir ve genellikle ters fonksiyondan farklıdır."),
        ("Bir fonksiyon ile tersinin grafikleri arasında nasıl bir ilişki vardır?",
         "İki grafik y eşittir x doğrusuna göre simetriktir. Fonksiyonun grafiğindeki her (a, b) noktası, tersinin grafiğinde (b, a) noktası olarak yer alır."),
        ("Ters fonksiyonun tanım kümesi nasıl bulunur?",
         "Ters fonksiyonun tanım kümesi, fonksiyonun görüntü kümesidir. Önce fonksiyonun hangi değerleri aldığı bulunur; ters fonksiyon tam olarak bu değerlerde tanımlıdır. Köklü ve ikinci dereceden fonksiyonlarda bu küme tersin kuralıyla birlikte yazılmalıdır."),
    ],
    "kontrol": [
        "Bir fonksiyonun tersinin olup olmadığını birebirlik ve örtenlikle gerekçelendirebiliyorum.",
        "Tersi olmayan bir fonksiyonun tanım ve değer kümesini daraltarak tersini tanımlayabiliyorum.",
        "Ters fonksiyonu üç adımda bulup bir sayıyla kontrol ediyorum.",
        "Doğrusal fonksiyonun tersini $\\dfrac{x-b}{a}$ kalıbıyla doğrudan yazabiliyorum.",
        "$\\dfrac{ax+b}{cx+d}$ türü fonksiyonun tersini kalıpla bulabiliyor, kendi tersi olan fonksiyonu tanıyorum.",
        "Köklü ve ikinci dereceden fonksiyonun tersini tanım kümesiyle birlikte yazıyorum.",
        "$f^{-1}(a)$ değerini tersi bulmadan $f(x)=a$ denklemiyle hesaplayabiliyorum.",
        "$(f \\circ g)^{-1}=g^{-1} \\circ f^{-1}$ özelliğini bir örnekle doğrulayabiliyorum.",
        "Bileşke eşitliğinde $f^{-1}$ uygulayarak içteki fonksiyonu bulabiliyorum.",
        "$f$ ile $f^{-1}$ in grafiklerinin $y=x$ e göre simetrik olduğunu ve kesişim kısayolunun sınırını biliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birebir-orten-fonksiyon", "bileske-fonksiyon", "tanim-deger-goruntu-kumeleri"],
}
