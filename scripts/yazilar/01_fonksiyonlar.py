# scripts/yazilar/01_fonksiyonlar.py — ilk blog yazisi (23.09.2026)
# Standart: blog-YAZIM-STANDARDI.md
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "fonksiyonlar-konu-anlatimi",
    "baslik": "Fonksiyonlar Konu Anlatımı",
    "aciklama": "Fonksiyon nedir, tanım ve görüntü kümesi, birebir ve örten fonksiyonlar, bileşke ve ters fonksiyon: baştan sona konu anlatımı.",
    "tarih": "2026-09-23",
    "guncelleme": None,
    "kategori": "fonksiyonlar",
    "sinavlar": ["TYT", "AYT", "ALES", "KPSS"],
    "kapak": "fonksiyonlar-konu-anlatimi",
    "kapak_alt": "Fonksiyonlar konu anlatımı: giriş değerlerini çıkış değerlerine bağlayan eşleme şeması ve bir fonksiyon grafiği",
    "ozet": "Fonksiyon, matematiğin geri kalanının üzerine kurulduğu fikirdir. Parabol da türev de integral de bir fonksiyonun davranışını konuşur. Bu yazıda fonksiyonu sıfırdan kuruyoruz: bir eşlemenin ne zaman fonksiyon olduğundan başlayıp tanım kümesine, fonksiyon çeşitlerine, bileşkeye, ters fonksiyona ve grafik okumaya kadar gidiyoruz.",
    "bolumler": [
        {"baslik": "Fonksiyon nedir?", "icerik": [
            onkosul(
                "Bu yazıyı rahat okumak için küme kavramını (eleman, alt küme, kesişim) ve koordinat düzleminde nokta işaretlemeyi biliyor olman yeterli. Denklem çözmeyi biliyorsan ters fonksiyon bölümü de kolay gelir."),
            "Bir fonksiyonu anlamanın en kolay yolu onu bir <strong>makine</strong> gibi düşünmektir. Makineye bir değer verirsin, makine sana tek bir değer döndürür. Aynı değeri tekrar verdiğinde yine aynı cevabı alırsın; makine keyfine göre bazen şunu bazen bunu vermez.",
            "Matematikte bu fikir şöyle yazılır: $A$ ve $B$ iki boş olmayan küme olsun. $A$ kümesinin <strong>her</strong> elemanını, $B$ kümesinin <strong>bir ve yalnız bir</strong> elemanına eşleyen kurala $A$ dan $B$ ye fonksiyon denir ve $f:A \\to B$ yazılır.",
            "Tanımın içinde iki ayrı şart saklı ve sınavda sorulan da genellikle bu iki şart:",
            "<ul><li><strong>Açıkta eleman kalmaz.</strong> $A$ kümesinde eşleşmemiş tek bir eleman bile varsa bu bir fonksiyon değildir.</li><li><strong>Bir elemanın iki görüntüsü olmaz.</strong> $A$ daki bir eleman $B$ deki iki farklı elemana birden gidiyorsa yine fonksiyon değildir.</li></ul>",
            "Tersi serbesttir: $B$ tarafında açıkta eleman kalabilir, $B$ deki bir elemana $A$ dan birden fazla ok gelebilir. Bunların ikisi de fonksiyonluğu bozmaz.",
            hap("Fonksiyon olma şartı yalnızca <strong>çıkış tarafında</strong> aranır: her $x$ in tam bir $f(x)$ i olacak. Giriş tarafında ne olduğu fonksiyonluğu bozmaz."),
            dikkat(
                "Türkçede \"her elemanın bir görüntüsü var\" cümlesi kulağa \"en az bir\" gibi geliyor. Matematikte burada kastedilen <strong>tam olarak bir</strong> tanedir. $f(2)=5$ ve $f(2)=7$ aynı anda olamaz."),
        ]},
        {"baslik": "Tanım kümesi, değer kümesi, görüntü kümesi", "icerik": [
            "$f:A \\to B$ fonksiyonunda üç küme konuşuruz ve üçünü karıştırmak sınavda en pahalı hatalardan biridir.",
            "<ul><li><strong>Tanım kümesi</strong> $A$: fonksiyona verebileceğimiz değerler.</li><li><strong>Değer kümesi</strong> $B$: çıkışın içinden seçildiği küme.</li><li><strong>Görüntü kümesi</strong> $f(A)$: çıkışta <em>gerçekten kullanılan</em> değerler.</li></ul>",
            "Görüntü kümesi her zaman değer kümesinin alt kümesidir: $f(A) \\subseteq B$. Eşit olmak zorunda değildir.",
            ornek(
                "$A=\\{1,2,3\\}$, $B=\\{a,b,c,d\\}$ ve $f(1)=a$, $f(2)=b$, $f(3)=a$ olsun.",
                "Tanım kümesi $\\{1,2,3\\}$, değer kümesi $\\{a,b,c,d\\}$, görüntü kümesi ise yalnızca $\\{a,b\\}$ dir. Çünkü $c$ ve $d$ ye hiç ok gitmemiştir.",
                "$a$ ya iki ok gitmesi bir sorun değildir; fonksiyonluk bozulmaz."),
            "<h3>Gerçel sayılarda en geniş tanım kümesi</h3>",
            "Sınavda \"$f$ fonksiyonunun en geniş tanım kümesi nedir?\" diye sorulduğunda, ifadeyi tanımsız yapan durumları eleriz. Üç klasik kısıt vardır:",
            tablo(["Yapı", "Kısıt"], [
                ["Payda", "Payda $\\neq 0$"],
                ["Çift dereceden kök", "Kök içi $\\geq 0$"],
                ["Logaritma", "İçi $> 0$, taban $>0$ ve $\\neq 1$"],
            ]),
            "Tek dereceden kökte (küp kök gibi) kısıt yoktur; negatif sayının küp kökü tanımlıdır.",
            ornek(
                "$f(x)=\\dfrac{\\sqrt{x-2}}{x-5}$ fonksiyonunun en geniş tanım kümesini bulalım.",
                "Kök içi sıfır ya da pozitif olmalı: $x-2 \\geq 0 \\Rightarrow x \\geq 2$.",
                "Payda sıfır olmamalı: $x-5 \\neq 0 \\Rightarrow x \\neq 5$.",
                "İkisi birlikte: tanım kümesi $[2,5) \\cup (5,\\infty)$ dur."),
            dikkat(
                "Kök içi için $> 0$ değil $\\geq 0$ yazılır; $\\sqrt{0}=0$ tanımlıdır. Payda içinse eşitlik yasaktır. Bu ikisi sık karıştırılır."),
        ]},
        {"baslik": "Bir eşleme ne zaman fonksiyon değildir?", "icerik": [
            "Şema olarak verilen bir eşlemede iki şeye bakarsın: açıkta kalan eleman var mı, çift ok çıkan eleman var mı. Grafikte ise aynı kontrolün adı <strong>dikey doğru testi</strong>dir.",
            "Grafiğin üzerinden geçen her dikey doğru, grafiği <strong>en fazla bir</strong> noktada kesiyorsa bu bir fonksiyon grafiğidir. İki noktada kesiyorsa aynı $x$ e iki farklı $y$ düşüyor demektir ve fonksiyon değildir.",
            hap("<strong>Dikey doğru testi:</strong> fonksiyon mu? <br><strong>Yatay doğru testi:</strong> birebir mi? İkisini karıştırma."),
            "Örneğin merkezi orijinde olan bir çember, $y$ ekseni yönünde iki değer ürettiği için fonksiyon grafiği değildir. Ama çemberin yalnız üst yarısı fonksiyondur.",
        ]},
        {"baslik": "Fonksiyon çeşitleri: birebir, örten, içine", "icerik": [
            "<h3>Birebir fonksiyon</h3>",
            "Farklı girişler farklı çıkışlar veriyorsa fonksiyon <strong>birebir</strong>dir. Simgeyle: $x_1 \\neq x_2 \\Rightarrow f(x_1) \\neq f(x_2)$.",
            "Sınavda bunu genelde ters yönden kullanmak daha kolaydır: $f(x_1)=f(x_2)$ olduğunu varsay, buradan $x_1=x_2$ çıkıyorsa fonksiyon birebirdir.",
            ornek(
                "$f(x)=3x-5$ birebir midir?",
                "$f(x_1)=f(x_2)$ diyelim: $3x_1-5 = 3x_2-5$.",
                "Her iki tarafa $5$ ekleyip $3$ e bölersek $x_1=x_2$ bulunur. Öyleyse $f$ birebirdir."),
            "<h3>Örten fonksiyon</h3>",
            "Değer kümesinde açıkta eleman kalmıyorsa, yani $f(A)=B$ ise fonksiyon <strong>örten</strong>dir. Açıkta eleman kalıyorsa fonksiyon <strong>içine</strong>dir.",
            "Dikkat edilecek nokta şu: örtenlik fonksiyonun kuralına değil, <strong>hangi değer kümesiyle</strong> verildiğine de bağlıdır. Aynı kural farklı değer kümesiyle örten olabilir de olmayabilir de.",
            ornek(
                "$f(x)=x^2$ kuralını iki ayrı biçimde ele alalım.",
                "$f:\\mathbb{R} \\to \\mathbb{R}$ olarak verilirse örten değildir; hiçbir gerçel sayının karesi negatif olamayacağı için $-4$ gibi değerler açıkta kalır.",
                "$f:\\mathbb{R} \\to [0,\\infty)$ olarak verilirse örtendir, çünkü her negatif olmayan sayı bir karedir."),
            "<h3>Birebir örten fonksiyon</h3>",
            "Hem birebir hem örten olan fonksiyona <strong>birebir örten</strong> denir. Bu, iki küme arasında tam bir eşleşme kurulduğu anlamına gelir: her girişin bir çıkışı, her çıkışın da tek bir girişi vardır. Ters fonksiyonun var olabilmesi için gereken şart tam olarak budur.",
            sinavda(
                "Birebir ve örten kavramları <strong>TYT</strong> de çoğunlukla şema üzerinden, \"aşağıdakilerden hangisi birebir örtendir?\" biçiminde sorulur. <strong>AYT</strong> de ise ters fonksiyonun var olup olmadığını tartışmak için kullanılır. <strong>ALES ve KPSS</strong> de doğrudan bu terimler nadiren geçer; oralarda fonksiyon daha çok işlem ve bileşke olarak karşına çıkar."),
            "<h3>Fonksiyon sayısı soruları</h3>",
            "$s(A)=m$ ve $s(B)=n$ olmak üzere $A$ dan $B$ ye tanımlanabilecek fonksiyonları saymak klasik bir soru tipidir.",
            tablo(["Aranan", "Sayısı", "Koşul"], [
                ["Tüm fonksiyonlar", "$n^m$", "&ndash;"],
                ["Birebir fonksiyonlar", "$\\dfrac{n!}{(n-m)!}$", "$m \\leq n$"],
                ["Sabit fonksiyonlar", "$n$", "&ndash;"],
                ["Birebir örten fonksiyonlar", "$n!$", "$m=n$"],
            ]),
            "Mantığı şudur: $A$ nın her elemanı için $B$ den bağımsız bir seçim yaparız, bu yüzden $n \\cdot n \\cdots n = n^m$ olur. Birebirde ise seçilen her eleman havuzdan düşer: $n(n-1)(n-2)\\cdots$ diye gider.",
            ornek(
                "$s(A)=3$ ve $s(B)=4$ olsun. $A$ dan $B$ ye kaç fonksiyon tanımlanabilir, bunların kaçı birebirdir?",
                "Tüm fonksiyonlar: $4^3 = 64$.",
                "Birebir olanlar: ilk eleman için $4$, ikinci için $3$, üçüncü için $2$ seçenek kalır; $4 \\cdot 3 \\cdot 2 = 24$.",
                "Bu $24$ sayısı $\\dfrac{4!}{(4-3)!} = \\dfrac{24}{1}$ ile de bulunur."),
            "Örten fonksiyon sayısı için doğrudan bir çarpım yoktur; içerme-dışarma ilkesi kullanılır:",
            "$$\\sum_{k=0}^{n} (-1)^k \\binom{n}{k} (n-k)^m$$",
            "Bu formül sınavda nadiren gerekir; küçük kümelerde örtenleri doğrudan saymak genellikle daha hızlıdır. Örneğin $s(A)=3$, $s(B)=2$ için tüm fonksiyonlar $2^3=8$, bunlardan ikisi sabit olduğu için örtenler $8-2=6$ tanedir.",
            hap("$A$ dan $B$ ye fonksiyon sayısı $n^m$ dir; <strong>üs tanım kümesinin eleman sayısıdır</strong>. Hangi sayının üste çıkacağı en sık yapılan karışıklıktır."),
        ]},
        {"baslik": "Özel fonksiyonlar", "icerik": [
            "<ul>"
            "<li><strong>Sabit fonksiyon:</strong> $f(x)=c$. Grafiği $x$ eksenine paralel bir doğrudur. Birebir değildir (tanım kümesinde birden fazla eleman varsa).</li>"
            "<li><strong>Birim (özdeşlik) fonksiyon:</strong> $I(x)=x$. Her değeri kendisine eşler, grafiği $y=x$ doğrusudur. Bileşkede etkisiz elemandır.</li>"
            "<li><strong>Doğrusal fonksiyon:</strong> $f(x)=ax+b$ ve $a \\neq 0$. $\\mathbb{R}$ dan $\\mathbb{R}$ ya tanımlı olduğunda hem birebir hem örtendir.</li>"
            "<li><strong>Mutlak değer fonksiyonu:</strong> $f(x)=|x|$. $x \\geq 0$ için $x$, $x < 0$ için $-x$ değerini alır.</li>"
            "<li><strong>Parçalı fonksiyon:</strong> tanım kümesinin farklı aralıklarında farklı kuralla tanımlanan fonksiyon.</li>"
            "</ul>",
            dikkat(
                "$f(x)=|x|$ fonksiyonu $\\mathbb{R} \\to \\mathbb{R}$ olarak <strong>birebir değildir</strong>: $f(-3)=f(3)=3$. Bu yüzden tersi de yoktur. Mutlak değerin tersini almaya çalışmak sık görülen bir hatadır."),
            ornek(
                "Parçalı bir örnek alalım: $x \\geq 0$ için $f(x)=x^2$, $x<0$ için $f(x)=-x$ olsun.",
                "$f(3)$ için $3 \\geq 0$ olduğundan birinci kural geçerlidir: $f(3)=9$.",
                "$f(-4)$ için $-4 < 0$ olduğundan ikinci kural geçerlidir: $f(-4)=4$.",
                "Parçalı fonksiyonda önce <strong>hangi aralıkta</strong> olduğuna bakılır, sonra o aralığın kuralı uygulanır."),
        ]},
        {"baslik": "İki fonksiyon ne zaman eşittir?", "icerik": [
            "İki fonksiyonun eşit sayılması için kurallarının aynı görünmesi yetmez. $f=g$ diyebilmek için iki şart birden gerekir:",
            "<ul><li>Tanım kümeleri aynı olmalı.</li><li>Tanım kümesindeki <strong>her</strong> $x$ için $f(x)=g(x)$ olmalı.</li></ul>",
            ornek(
                "$f(x)=\\dfrac{x^2-1}{x-1}$ ve $g(x)=x+1$ fonksiyonları eşit midir?",
                "Sadeleştirince $f(x)$ de $x+1$ gibi görünür, ama $f$ in tanım kümesinde $x=1$ <strong>yoktur</strong>; payda sıfır olur.",
                "$g$ ise $x=1$ için tanımlıdır ve $g(1)=2$ değerini alır.",
                "Tanım kümeleri farklı olduğu için bu iki fonksiyon eşit değildir. Ancak $x \\neq 1$ için değerleri aynıdır."),
            dikkat(
                "Sadeleştirme tanım kümesini değiştirmez. Bir ifadeyi sadeleştirdiğinde, sadeleşen çarpanın sıfır yaptığı değer tanım kümesinden çıkmış olarak kalır. Bu, limit ve süreklilik konularında karşına tekrar çıkacak."),
        ]},
        {"baslik": "Fonksiyonlarda dört işlem", "icerik": [
            "İki fonksiyon toplanabilir, çıkarılabilir, çarpılabilir ve bölünebilir. Kural beklendiği gibidir:",
            "$$(f+g)(x) = f(x)+g(x)$$",
            "$$(f \\cdot g)(x) = f(x) \\cdot g(x)$$",
            "$$\\left(\\frac{f}{g}\\right)(x) = \\frac{f(x)}{g(x)}$$",
            "Asıl dikkat edilecek yer sonuçların <strong>tanım kümesi</strong>dir. Toplam, fark ve çarpımda yeni tanım kümesi iki fonksiyonun tanım kümelerinin kesişimidir. Bölmede buna bir şart daha eklenir: $g(x) \\neq 0$.",
            hap("$f+g$, $f-g$ ve $f \\cdot g$ için tanım kümesi $A_f \\cap A_g$ dir. $\\dfrac{f}{g}$ için ayrıca $g(x) \\neq 0$ şartı aranır."),
        ]},
        {"baslik": "Bileşke fonksiyon", "icerik": [
            "İki makineyi arka arkaya bağladığını düşün: birinin çıkışı ötekinin girişi olsun. Bu birleşime <strong>bileşke</strong> denir.",
            "$$(f \\circ g)(x) = f(g(x))$$",
            "Okunuşu \"f bileşke g\" dir ve <strong>içteki önce çalışır</strong>. Yani $g$ uygulanır, çıkan sonuç $f$ e verilir. Yazılış sırası ile işlem sırasının ters olması, bu konudaki en yaygın karışıklıktır.",
            ornek(
                "$f(x)=2x+1$ ve $g(x)=x^2$ olsun.",
                "$(f \\circ g)(3) = f(g(3)) = f(9) = 2 \\cdot 9 + 1 = 19$.",
                "$(g \\circ f)(3) = g(f(3)) = g(7) = 7^2 = 49$.",
                "Görüldüğü gibi sonuçlar farklı; sıra önemlidir."),
            "<h3>Bileşkenin özellikleri</h3>",
            "<ul>"
            "<li><strong>Değişme özelliği yoktur:</strong> genel olarak $f \\circ g \\neq g \\circ f$.</li>"
            "<li><strong>Birleşme özelliği vardır:</strong> $(f \\circ g) \\circ h = f \\circ (g \\circ h)$.</li>"
            "<li><strong>Birim fonksiyon etkisizdir:</strong> $f \\circ I = I \\circ f = f$.</li>"
            "</ul>",
            dikkat(
                "$f \\circ g \\neq g \\circ f$ olması <strong>her zaman farklı</strong> demek değildir; bazı özel fonksiyonlarda eşit olabilirler. Doğru ifade şudur: genel olarak eşit olmak zorunda değillerdir."),
            ornek(
                "$f(x)=3x-2$ ve $(f \\circ g)(x) = 6x+4$ ise $g(x)$ nedir?",
                "$f(g(x)) = 3 \\cdot g(x) - 2$ olduğunu biliyoruz.",
                "Öyleyse $3 \\cdot g(x) - 2 = 6x+4$ yazarız.",
                "$3 \\cdot g(x) = 6x+6$ ve buradan $g(x) = 2x+2$ bulunur."),
        ]},
        {"baslik": "Ters fonksiyon", "icerik": [
            "Ters fonksiyon, makineyi geriye çalıştırmaktır: çıkıştan girişe dönmek. $f(a)=b$ ise $f^{-1}(b)=a$ olur.",
            "Ama her fonksiyonun tersi yoktur. Geriye dönebilmek için iki şey gerekir: her çıkışın <strong>bir</strong> girişten gelmesi (birebirlik) ve <strong>her</strong> çıkışın kullanılmış olması (örtenlik).",
            hap("Bir fonksiyonun tersi <strong>ancak ve ancak</strong> birebir ve örtense vardır. Bu şart sağlanmıyorsa $f^{-1}$ diye bir fonksiyon yoktur."),
            "<h3>Ters fonksiyon nasıl bulunur?</h3>",
            "<ol><li>$y=f(x)$ yaz.</li><li>Denklemi $x$ i yalnız bırakacak biçimde çöz.</li><li>$x$ ile $y$ yi yer değiştir.</li></ol>",
            ornek(
                "$f(x)=3x-5$ fonksiyonunun tersini bulalım.",
                "$y=3x-5$ yazarız.",
                "$x$ i çekeriz: $3x = y+5$ ve $x = \\dfrac{y+5}{3}$.",
                "$x$ ile $y$ yi değiştiririz: $f^{-1}(x) = \\dfrac{x+5}{3}$.",
                "Kontrol edelim: $f(4) = 3 \\cdot 4 - 5 = 7$ ve $f^{-1}(7) = \\dfrac{7+5}{3} = 4$. Başladığımız yere döndük."),
            "Doğrusal fonksiyonlar için doğrudan kullanılabilecek bir sonuç da vardır: $f(x)=ax+b$ ve $a \\neq 0$ ise",
            "$$f^{-1}(x) = \\frac{x-b}{a}$$",
            "<h3>Ters fonksiyonun özellikleri</h3>",
            "<ul>"
            "<li>$f \\circ f^{-1} = f^{-1} \\circ f = I$ &nbsp;(birim fonksiyon)</li>"
            "<li>$(f^{-1})^{-1} = f$</li>"
            "<li>$(f \\circ g)^{-1} = g^{-1} \\circ f^{-1}$ &nbsp;(sıra ters döner)</li>"
            "<li>$f$ nin grafiği ile $f^{-1}$ in grafiği $y=x$ doğrusuna göre simetriktir.</li>"
            "</ul>",
            dikkat(
                "$f^{-1}(x)$ ile $\\dfrac{1}{f(x)}$ aynı şey <strong>değildir</strong>. Buradaki $-1$ bir üs değil, ters fonksiyon işaretidir. $f(x)=3x-5$ için $f^{-1}(x)=\\dfrac{x+5}{3}$ tür, $\\dfrac{1}{3x-5}$ değil."),
            hap("$(f \\circ g)^{-1} = g^{-1} \\circ f^{-1}$ sırasını hatırlamak için giyinme sırasını düşün: önce çorap sonra ayakkabı giyilir; çıkarırken önce ayakkabı çıkar. Ters alınca sıra tersine döner."),
        ]},
        {"baslik": "Grafikten fonksiyon okuma", "icerik": [
            "Bir fonksiyon grafiğinden şunları doğrudan okuyabilirsin:",
            "<ul>"
            "<li><strong>$f(a)$ değeri:</strong> $x=a$ noktasından yukarı çık, grafiği kestiği noktanın $y$ değeri $f(a)$ dır.</li>"
            "<li><strong>Kökler:</strong> grafiğin $x$ eksenini kestiği noktalar $f(x)=0$ denkleminin çözümleridir.</li>"
            "<li><strong>$y$ kesişimi:</strong> grafiğin $y$ eksenini kestiği nokta $f(0)$ değeridir.</li>"
            "<li><strong>Tanım kümesi:</strong> grafiğin $x$ ekseni üzerinde kapladığı aralık.</li>"
            "<li><strong>Görüntü kümesi:</strong> grafiğin $y$ ekseni üzerinde kapladığı aralık.</li>"
            "</ul>",
            ornek(
                "Bir $f$ fonksiyonunun grafiği $(-2,0)$, $(0,3)$ ve $(4,0)$ noktalarından geçiyor olsun.",
                "$f(0)=3$ tür; grafiğin $y$ eksenini kestiği yer budur.",
                "$f(x)=0$ denkleminin çözümleri $x=-2$ ve $x=4$ tür; bunlar grafiğin $x$ eksenini kestiği noktalardır.",
                "Bu üç bilgi, fonksiyonun kuralını bilmeden de bir sürü soruyu çözmeye yeter."),
            sinavda(
                "Grafik okuma soruları <strong>TYT</strong> de doğrudan \"$f(2)$ kaçtır?\" biçiminde gelir. <strong>AYT</strong> de grafik genellikle bileşke ile birleştirilir: grafikten $g(1)$ okunur, sonra $f(g(1))$ istenir. <strong>ALES ve KPSS</strong> de grafik yerine tablo verilmesi daha yaygındır; mantık aynıdır, okuma biçimi değişir."),
            "Ters fonksiyonun grafiğini çizmek istiyorsan yeni bir hesap yapmana gerek yok: $f$ nin grafiğini $y=x$ doğrusuna göre yansıtman yeterlidir. Bunun sebebi basittir; $(a,b)$ noktası $f$ üzerindeyse $(b,a)$ noktası $f^{-1}$ üzerindedir ve bu iki nokta $y=x$ e göre simetriktir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$f^{-1}(x) = \\dfrac{1}{f(x)}$ sanmak", "$-1$ üs değil, ters fonksiyon işareti"],
                ["Görüntü kümesini değer kümesiyle bir tutmak", "$f(A) \\subseteq B$, eşit olmak zorunda değil"],
                ["$f \\circ g = g \\circ f$ sanmak", "Genel olarak eşit değildir"],
                ["Bileşkede dıştakini önce uygulamak", "İçteki önce çalışır: $f(g(x))$"],
                ["$|x|$ in tersini aramak", "Birebir olmadığı için tersi yoktur"],
                ["Kök içine $>0$ yazmak", "Çift dereceden kökte $\\geq 0$"],
                ["Fonksiyon sayısında üssü şaşırmak", "Tanım kümesinin eleman sayısı üste çıkar"],
            ]),
            "Bu yedi satırın altısı tanımı yanlış hatırlamaktan değil, <strong>tanımı hiç okumadan işleme geçmekten</strong> kaynaklanır. Soruya başlamadan önce \"hangi küme tanım, hangisi değer kümesi?\" diye sormak çoğu hatayı baştan keser.",
        ]},
    ],
    "sss": [
        ("Her bağıntı fonksiyon mudur?",
         "Hayır. Fonksiyon, bağıntının özel bir hâlidir. Bir bağıntının fonksiyon olabilmesi için tanım kümesindeki her elemanın tam olarak bir görüntüsü olması gerekir."),
        ("Bir fonksiyonun tersi her zaman var mıdır?",
         "Hayır. Ters fonksiyonun var olması için fonksiyonun hem birebir hem örten olması gerekir. Örneğin gerçel sayılarda tanımlı mutlak değer fonksiyonunun tersi yoktur."),
        ("f bileşke g ile g bileşke f aynı şey midir?",
         "Genel olarak değildir. Bileşkede sıra önemlidir; bazı özel fonksiyonlarda eşit olabilirler ama bu bir kural değildir."),
        ("Görüntü kümesi ile değer kümesi arasındaki fark nedir?",
         "Değer kümesi, çıkışın seçildiği bütün kümedir. Görüntü kümesi ise bu kümenin gerçekten kullanılan kısmıdır. Görüntü kümesi her zaman değer kümesinin alt kümesidir."),
        ("En geniş tanım kümesi nasıl bulunur?",
         "İfadeyi tanımsız yapan durumlar elenir: payda sıfır olamaz, çift dereceden kökün içi negatif olamaz, logaritmanın içi pozitif olmalıdır. Kalan değerler en geniş tanım kümesini verir."),
        ("Fonksiyon sayısı sorularında hangi sayı üste çıkar?",
         "Tanım kümesinin eleman sayısı üste çıkar. Tanım kümesinde m, değer kümesinde n eleman varsa fonksiyon sayısı n üzeri m dir."),
    ],
    "kontrol": [
        "Bir şemaya bakıp fonksiyon olup olmadığını iki şartla gerekçelendirebiliyorum.",
        "Tanım, değer ve görüntü kümesini bir örnek üzerinde ayrı ayrı gösterebiliyorum.",
        "Paydalı ve köklü bir ifadenin en geniş tanım kümesini bulabiliyorum.",
        "Dikey doğru testi ile yatay doğru testinin neyi sınadığını karıştırmıyorum.",
        "Birebir olduğunu $f(x_1)=f(x_2) \\Rightarrow x_1=x_2$ yoluyla gösterebiliyorum.",
        "Aynı kuralın değer kümesine göre örten olup olmadığının değişebileceğini biliyorum.",
        "$(f \\circ g)(x)$ hesaplarken içteki fonksiyonu önce uyguluyorum.",
        "Verilen $f$ ve $f \\circ g$ den $g$ yi çekebiliyorum.",
        "Ters fonksiyonu üç adımda bulup sonucu geri yerine koyarak kontrol ediyorum.",
        "$f^{-1}(x)$ ile $\\dfrac{1}{f(x)}$ i karıştırmıyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": [],
}
