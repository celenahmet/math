# scripts/yazilar/33_limit.py — Limit Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "limit-konu-anlatimi",
    "baslik": "Limit Konu Anlatımı",
    "aciklama": "Limit nedir? Yaklaşma fikri, limit ile fonksiyon değeri farkı, limit kuralları, polinom ve rasyonel limitler, sonsuzda limit ve anlık hız; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "limit-konu-anlatimi",
    "kapak_alt": "Limit konu anlatımı: ahşap ray üzerinde giderek küçülen aralıklarla ışıklı hedefe yaklaşan mavi bilyeleri dizen öğrenci",
    "ozet": "Limit, bir fonksiyonun değişkeni belirli bir sayıya yaklaşırken değerlerinin neye yaklaştığını söyleyen kavramdır. Fonksiyonun o noktadaki değerinden bağımsızdır ve türev ile integralin temelini oluşturur. Bu yazıda yaklaşma fikrini ve limit gösterimini, limit ile fonksiyon değeri arasındaki farkı, limitin var olma koşulunu, polinom, rasyonel, köklü ve trigonometrik fonksiyonlarda limit hesabını, limit kurallarını, belirsizliklere girişi, sonsuz limitleri ve sonsuzda limiti, sıkıştırma fikrini ve anlık hız uygulamasını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Limit nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için fonksiyon kavramını ve fonksiyon grafiklerini okumayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/fonksiyonlar-konu-anlatimi/\">Fonksiyonlar Konu Anlatımı</a> ve <a href=\"/blog/fonksiyon-grafikleri/\">Fonksiyon Grafikleri Nasıl Çizilir ve Yorumlanır?</a> yazılarına göz at."),
            "Bir fonksiyonun değişkeni belirli bir sayıya giderek yaklaşırken fonksiyonun değerleri de belirli bir sayıya yaklaşıyorsa, bu sayıya fonksiyonun o noktadaki <strong>limiti</strong> denir. Limit, fonksiyonun o noktada ne olduğunu değil, o noktaya yaklaşırken nereye gittiğini anlatır.",
            "Kapaktaki öğrenci bilyeleri bir ray üzerinde ışıklı bir hedefe doğru diziyor; bilyeler arasındaki aralıklar hedefe yaklaştıkça küçülüyor. Hiçbir bilye hedefin tam üstünde durmuyor, ama bilyelerin nereye yöneldiği açıkça görülüyor. Limit tam olarak bu yönelimin adıdır. Bu fikir türev ve integral konularının da başlangıç noktasıdır.",
        ]},
        {"baslik": "Yaklaşma fikri", "icerik": [
            "$f(x)=2x+1$ fonksiyonunu ele alalım ve $x$ i $3$ e hem küçük hem büyük değerlerden yaklaştıralım. Fonksiyon değerleri tabloda görüldüğü gibi $7$ ye yaklaşır:",
            tablo(["$x$", "$2.9$", "$2.99$", "$3.01$", "$3.1$"], [
                ["$f(x)$", "$6.8$", "$6.98$", "$7.02$", "$7.2$"],
            ]),
            "$x$ i $3$ e ne kadar yaklaştırırsak $f(x)$ de $7$ ye o kadar yaklaşır. Bu durum $x$ in $3$ e yaklaşırken $f(x)$ in limitinin $7$ olduğu biçiminde ifade edilir. Bu örnekte limit, fonksiyonun $3$ teki değerine de eşittir; ama bu her zaman böyle değildir.",
        ]},
        {"baslik": "Limitin gösterimi", "icerik": [
            "$x$ değişkeni $a$ sayısına yaklaşırken $f(x)$ değerleri $L$ sayısına yaklaşıyorsa bu durum şöyle yazılır:",
            "$$\\lim_{x \\to a} f(x)=L$$",
            "İfade, $x$ in $a$ ya yaklaşırken $f(x)$ in limiti $L$ dir diye okunur. Önceki örnek için $\\lim_{x \\to 3}(2x+1)=7$ yazılır. Yaklaşmada $x$ hiçbir zaman $a$ ya eşit olmaz; yalnızca istenildiği kadar yakın değerler alır.",
            hap("Limit, fonksiyonun bir noktaya yaklaşırken yöneldiği değerdir.",
                "Fonksiyonun o noktadaki değeriyle aynı olmak zorunda değildir."),
        ]},
        {"baslik": "Tanımsız noktada limit", "icerik": [
            "$f(x)=\\dfrac{x^2-1}{x-1}$ fonksiyonu $x=1$ de tanımsızdır; çünkü payda sıfır olur. Ama $x \\neq 1$ için pay $(x-1)(x+1)$ olarak çarpanlara ayrılır ve fonksiyon $x+1$ e eşittir. Bu yüzden grafik, $(1, 2)$ noktasında bir boşluk bulunan bir doğrudur.",
            koordinat_grafik("y = (x² - 1)/(x - 1) grafiği", [("", lambda x: x + 1 if abs(x - 1) > 1e-9 else None)], (-2, 4), (-1.5, 5), adim=1,
                             noktalar=[(1, 2, "", False)]),
            "Fonksiyon $1$ de tanımlı olmasa da $x$ $1$ e yaklaşırken değerler $2$ ye yaklaşır: $\\lim_{x \\to 1}\\dfrac{x^2-1}{x-1}=2$. Grafikteki boş daire, fonksiyonun o noktada değeri olmadığını ama limitinin var olduğunu gösterir.",
        ]},
        {"baslik": "Limit ile fonksiyon değeri farklı olabilir", "icerik": [
            "Fonksiyon bir noktada tanımlı olsa bile oradaki değeri limitten farklı olabilir. Limit yalnızca yakın noktalara bakar; noktanın kendisini hesaba katmaz. Bu yüzden bir noktadaki değeri değiştirmek o noktadaki limiti değiştirmez.",
            koordinat_grafik("Parçalı tanımlı f fonksiyonu", [("", lambda x: x + 1 if abs(x - 2) > 1e-9 else None)], (-1.5, 4.5), (-1, 6), adim=1,
                             noktalar=[(2, 3, "", False), (2, 5, "", True)]),
            ornek(
                "$x \\neq 2$ için $f(x)=x+1$ ve $f(2)=5$ olsun.",
                "$\\lim_{x \\to 2} f(x)$ ve $f(2)$ yi karşılaştıralım.",
                "$x$ $2$ ye yaklaşırken $f(x)=x+1$ değerleri $3$ e yaklaşır: limit $3$ tür.",
                "Fonksiyonun değeri ise $f(2)=5$ tir; limit ile değer farklıdır."),
        ]},
        {"baslik": "Limitin var olma koşulu", "icerik": [
            "Bir noktaya iki yönden yaklaşılabilir: soldan, yani küçük değerlerden ve sağdan, yani büyük değerlerden. Limitin var olması için iki yönden yaklaşırken fonksiyonun aynı sayıya yönelmesi gerekir:",
            "$$\\lim_{x \\to a^-} f(x)=\\lim_{x \\to a^+} f(x)=L$$",
            "Soldan ve sağdan limitler farklıysa limit yoktur. Bu durum özellikle parçalı fonksiyonlarda, mutlak değerli ifadelerde ve tam değer fonksiyonunda görülür. Ayrıntılı örnekler için <a href=\"/blog/sagdan-soldan-limit/\">Sağdan ve Soldan Limit Nasıl Bulunur?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "En basit iki limit", "icerik": [
            "Bütün limit hesaplarının dayandığı iki temel sonuç vardır. Sabit bir fonksiyonun limiti her noktada o sabittir: $\\lim_{x \\to a} c=c$. Birim fonksiyonun limiti ise yaklaşılan sayının kendisidir: $\\lim_{x \\to a} x=a$.",
            "Limit kuralları bu iki sonuçla birleştirilince polinomların limitinin neden yerine yazmayla bulunduğu anlaşılır. Örneğin $\\lim_{x \\to 5} 7=7$ ve $\\lim_{x \\to 5} x^2=5 \\cdot 5=25$ olur; her polinom bu tür terimlerin toplamıdır.",
        ]},
        {"baslik": "Tablo ile tahminin sınırı", "icerik": [
            "Değer tablosu limiti sezmek için yararlıdır, ama tek başına kanıt değildir. Seçilen noktalar yanıltıcı olabilir ve tablo yanlış bir sonuç düşündürebilir.",
            ornek(
                "$f(x)=\\sin \\dfrac{\\pi}{x}$ fonksiyonu verilsin.",
                "$x=1$, $0.1$ ve $0.01$ değerlerine bakıp limiti tahmin etmenin neden yanıltıcı olduğunu görelim.",
                "Bu noktalarda $\\sin \\pi$, $\\sin 10\\pi$ ve $\\sin 100\\pi$ hesaplanır; üçü de $0$ dır ve limit $0$ gibi görünür.",
                "Oysa $x=\\dfrac{2}{5}$ için $\\sin \\dfrac{5\\pi}{2}=1$ olur; fonksiyon sıfıra yakın her aralıkta $-1$ ile $1$ arasında salınır ve limiti yoktur."),
        ]},
        {"baslik": "Polinomlarda limit", "icerik": [
            "Polinom fonksiyonların grafiğinde boşluk ya da sıçrama yoktur; grafik kalem kâğıttan kaldırılmadan çizilebilir ve her gerçek sayıda tanımlıdır. Bu yüzden bir polinomun herhangi bir noktadaki limiti, o noktadaki değerine eşittir ve $x$ yerine sayı yazılarak bulunur.",
            ornek(
                "$\\lim_{x \\to 2}(x^3-2x+1)$ limiti verilsin.",
                "Limiti bulalım.",
                "Polinom olduğu için $x$ yerine $2$ yazılır: $8-4+1$.",
                "Limit $5$ tir."),
        ]},
        {"baslik": "Rasyonel fonksiyonlarda limit", "icerik": [
            "İki polinomun bölümü olan rasyonel fonksiyonlarda, payda limitin alındığı noktada sıfır değilse limit yine doğrudan yerine yazmayla bulunur. Payda sıfır oluyorsa önce ifadenin sadeleştirilmesi gerekir.",
            ornek(
                "$\\lim_{x \\to 1}\\dfrac{x+3}{x+1}$ limiti verilsin.",
                "Limiti bulalım.",
                "Payda $x=1$ için $2$ olur, sıfır değildir.",
                "Limit $\\dfrac{1+3}{1+1}=2$ olur."),
        ]},
        {"baslik": "Limit kuralları", "icerik": [
            "Limitleri var olan fonksiyonların toplamının, farkının, çarpımının ve bölümünün limiti, limitlerin toplamı, farkı, çarpımı ve bölümüdür. Bölümde paydanın limiti sıfırdan farklı olmalıdır:",
            tablo(["Kural", "Formül"], [
                ["Toplam ve fark", "$\\lim(f \\pm g)=\\lim f \\pm \\lim g$"],
                ["Sabitle çarpma", "$\\lim(c \\cdot f)=c \\cdot \\lim f$"],
                ["Çarpım", "$\\lim(f \\cdot g)=\\lim f \\cdot \\lim g$"],
                ["Bölüm", "$\\lim \\dfrac{f}{g}=\\dfrac{\\lim f}{\\lim g}$, $\\lim g \\neq 0$"],
                ["Kuvvet", "$\\lim f^n=(\\lim f)^n$"],
            ]),
            ornek(
                "$\\lim_{x \\to a} f(x)=3$ ve $\\lim_{x \\to a} g(x)=-2$ olsun.",
                "$\\lim(2f-g)$, $\\lim(f \\cdot g)$ ve $\\lim \\dfrac{f^2}{g}$ limitlerini bulalım.",
                "$\\lim(2f-g)=6-(-2)=8$ ve $\\lim(f \\cdot g)=3 \\cdot (-2)=-6$ olur.",
                "$\\lim \\dfrac{f^2}{g}=\\dfrac{9}{-2}=-\\dfrac{9}{2}$ olur."),
        ]},
        {"baslik": "Parametreli limit", "icerik": [
            "Limit değeri verilen bir ifadede bilinmeyen bir katsayı bulunabilir. Limit yerine yazmayla hesaplanıyorsa sonuç verilen değere eşitlenir ve parametre için bir denklem çözülür.",
            ornek(
                "$\\lim_{x \\to 2}(x^2+kx)=10$ olsun.",
                "$k$ değerini bulalım.",
                "Polinom olduğu için limit $4+2k$ olur.",
                "$4+2k=10$ denkleminden $k=3$ bulunur."),
        ]},
        {"baslik": "Bileşke fonksiyonda limit", "icerik": [
            "Dıştaki fonksiyon kesintisizse bileşke fonksiyonun limiti, içteki limitin dıştaki fonksiyona yazılmasıyla bulunur: $\\lim f(g(x))=f(\\lim g(x))$.",
            ornek(
                "$\\lim_{x \\to 0}\\cos(x^2+\\pi)$ limiti verilsin.",
                "Limiti bulalım.",
                "İçteki ifade $\\pi$ ye yaklaşır.",
                "Kosinüs kesintisiz olduğu için limit $\\cos \\pi=-1$ olur."),
        ]},
        {"baslik": "Köklü ve mutlak değerli ifadeler", "icerik": [
            "Kök ve mutlak değer, içlerindeki ifadenin limitine uygulanabilir. Kök içindeki ifadenin limiti pozitif olduğu sürece limit, kök içindeki limitin köküdür; mutlak değerde ise içteki limitin mutlak değeri alınır.",
            ornek(
                "$\\lim_{x \\to 4}\\sqrt{x+5}$ ve $\\lim_{x \\to -2}|x^2-9|$ limitleri verilsin.",
                "Limitleri bulalım.",
                "Birincide kök içi $9$ a yaklaşır; limit $\\sqrt{9}=3$ olur.",
                "İkincide içteki ifade $4-9=-5$ e yaklaşır; limit $|-5|=5$ olur."),
        ]},
        {"baslik": "Trigonometrik, üstel ve logaritmik limitler", "icerik": [
            "Sinüs, kosinüs, üstel ve logaritma fonksiyonları tanım kümelerinin her noktasında kesintisizdir. Bu yüzden tanım kümesindeki bir noktada limitleri, o noktadaki değerlerine eşittir.",
            ornek(
                "$\\lim_{x \\to \\pi/2}\\sin x$, $\\lim_{x \\to 2} 2^x$ ve $\\lim_{x \\to e}\\ln x$ limitleri verilsin.",
                "Limitleri bulalım.",
                "$\\sin \\dfrac{\\pi}{2}=1$ ve $2^2=4$ olur.",
                "$\\ln e=1$ olur; üç limit de fonksiyon değerine eşittir."),
        ]},
        {"baslik": "Ünlü bir limit", "icerik": [
            "$\\dfrac{\\sin x}{x}$ ifadesi $x=0$ da tanımsızdır; pay ve payda birlikte sıfıra gider. Yine de $x$ radyan cinsinden sıfıra yaklaşırken değerler $1$ e yaklaşır:",
            tablo(["$x$", "$0.1$", "$0.01$", "$0.001$"], [
                ["$\\dfrac{\\sin x}{x}$", "$0.99833$", "$0.99998$", "$0.9999998$"],
            ]),
            "Bu sonuç $\\lim_{x \\to 0}\\dfrac{\\sin x}{x}=1$ biçiminde yazılır. Küçük açılarda $\\sin x$ değerinin $x$ e çok yakın olduğunu söyler ve sinüsün türevinin hesaplanmasında temel rol oynar.",
        ]},
        {"baslik": "Belirsizliklere giriş", "icerik": [
            "Yerine yazma sonucunda $\\dfrac{0}{0}$ gibi bir ifade çıkarsa limit hakkında hemen bir şey söylenemez; bu duruma belirsizlik denir. Belirsizlik, limitin olmadığı anlamına gelmez; ifadenin sadeleştirilmesi gerektiğini gösterir.",
            ornek(
                "$\\lim_{x \\to 3}\\dfrac{x^2-9}{x-3}$ limiti verilsin.",
                "Limiti bulalım.",
                "Yerine yazınca $\\dfrac{0}{0}$ çıkar. Pay $(x-3)(x+3)$ olarak çarpanlara ayrılır ve $x-3$ sadeleşir.",
                "Limit $\\lim_{x \\to 3}(x+3)=6$ olur."),
            "Çarpanlara ayırma, eşlenikle çarpma ve diğer yöntemler için <a href=\"/blog/limitte-belirsizlikler/\">Limitte Belirsizlikler Nasıl Çözülür?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sonsuz limitler", "icerik": [
            "Bazı fonksiyonlar bir noktaya yaklaşırken sınırsız büyür. $f(x)=\\dfrac{1}{x^2}$ fonksiyonunda $x$ sıfıra yaklaştıkça $x^2$ çok küçük pozitif değerler alır ve kesir sınırsız büyür.",
            tablo(["$x$", "$\\pm 0.1$", "$\\pm 0.01$", "$\\pm 0.001$"], [
                ["$\\dfrac{1}{x^2}$", "$100$", "$10000$", "$1000000$"],
            ]),
            "Bu durum $\\lim_{x \\to 0}\\dfrac{1}{x^2}=\\infty$ biçiminde yazılır. Sonsuz bir sayı değildir; bu yazım, limitin gerçek bir sayı olarak var olmadığını ve değerlerin sınırsız büyüdüğünü anlatır. Grafikte bu nokta dikey bir asimptota karşılık gelir.",
        ]},
        {"baslik": "İki yönden farklı sonsuzlar", "icerik": [
            "Bazı fonksiyonlar bir noktanın iki yanında farklı yönlere sınırsız gider. $f(x)=\\dfrac{1}{x}$ fonksiyonunda $x$ sıfıra sağdan yaklaşırken değerler sınırsız büyür, soldan yaklaşırken ise sınırsız küçülür.",
            "Bu durumda $\\lim_{x \\to 0^+}\\dfrac{1}{x}=\\infty$ ve $\\lim_{x \\to 0^-}\\dfrac{1}{x}=-\\infty$ yazılır. İki yönün sonucu farklı olduğu için $\\lim_{x \\to 0}\\dfrac{1}{x}$ limitinden söz edilemez; buna karşın $\\dfrac{1}{x^2}$ de iki yön de aynı yöne gittiği için sonsuz limit yazımı kullanılabilir.",
        ]},
        {"baslik": "Sonsuzda limit", "icerik": [
            "Değişken sınırsız büyürken fonksiyonun neye yaklaştığı da bir limit sorusudur ve $x \\to \\infty$ ile gösterilir. $\\dfrac{1}{x}$ ifadesi $x$ büyüdükçe sıfıra yaklaşır: $\\lim_{x \\to \\infty}\\dfrac{1}{x}=0$.",
            ornek(
                "$\\lim_{x \\to \\infty}\\dfrac{2x+1}{x-3}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay ve payda $x$ e bölünür: $\\dfrac{2+\\dfrac{1}{x}}{1-\\dfrac{3}{x}}$.",
                "$\\dfrac{1}{x}$ ve $\\dfrac{3}{x}$ sıfıra gittiği için limit $2$ olur."),
        ]},
        {"baslik": "Derece karşılaştırması", "icerik": [
            "Sonsuzda rasyonel fonksiyonların limiti, pay ve paydanın derecelerine bakılarak hemen söylenir. En yüksek dereceli terimler baskın olduğu için diğer terimler sonucu değiştirmez:",
            tablo(["Durum", "Limit", "Örnek"], [
                ["Pay derecesi küçük", "$0$", "$\\lim_{x \\to \\infty}\\dfrac{x+1}{x^2}=0$"],
                ["Dereceler eşit", "Baş katsayılar oranı", "$\\lim_{x \\to \\infty}\\dfrac{3x^2+1}{x^2-5}=3$"],
                ["Pay derecesi büyük", "$\\pm\\infty$", "$\\lim_{x \\to \\infty}\\dfrac{x^3}{x+1}=\\infty$"],
            ]),
            "Yatay asimptot kavramı da buradan gelir: dereceler eşitse grafik, baş katsayılar oranı olan yatay doğruya yaklaşır.",
        ]},
        {"baslik": "Sıkıştırma fikri", "icerik": [
            "Doğrudan hesaplanamayan bir limit, limitleri aynı olan iki fonksiyon arasına sıkıştırılarak bulunabilir. Bu yönteme sıkıştırma ya da sandviç teoremi denir ve özellikle salınan fonksiyonlarda işe yarar. Alttaki ve üstteki fonksiyon aynı sayıya gidiyorsa aradaki fonksiyon da o sayıya gitmek zorundadır.",
            ornek(
                "$\\lim_{x \\to 0} x^2 \\sin \\dfrac{1}{x}$ limiti verilsin.",
                "Limiti bulalım.",
                "Sinüs $-1$ ile $1$ arasında kaldığı için $-x^2 \\le x^2 \\sin \\dfrac{1}{x} \\le x^2$ olur.",
                "İki sınır da sıfıra gittiği için limit $0$ olur."),
        ]},
        {"baslik": "Uygulama: anlık hız", "icerik": [
            "Limitin en önemli uygulamalarından biri anlık hızdır. Ortalama hız, alınan yolun geçen süreye bölümüdür; süre aralığı sıfıra yaklaştırıldığında ortalama hızın limiti anlık hızı verir.",
            ornek(
                "Serbest düşen bir cismin $t$ saniyede aldığı yol yaklaşık $s(t)=5t^2$ metre olsun.",
                "$t=2$ anındaki anlık hızı bulalım.",
                "$2$ ile $2+h$ arasındaki ortalama hız $\\dfrac{5(2+h)^2-20}{h}=20+5h$ olur.",
                "$h$ sıfıra yaklaşırken ortalama hız $20$ ye yaklaşır; anlık hız $20$ metre bölü saniyedir."),
            "Bu hesap aslında türevin tanımıdır. Türevin limitle nasıl tanımlandığı <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> yazısında ayrıntılı olarak anlatılıyor.",
        ]},
        {"baslik": "Uygulama: sonsuz toplamlar", "icerik": [
            "Sonsuz toplamlar da limitle tanımlanır. $1+\\dfrac{1}{2}+\\dfrac{1}{4}+\\cdots$ toplamının ilk $n$ teriminin toplamı $2-\\dfrac{1}{2^{n-1}}$ dir. $n$ sonsuza giderken ikinci terim sıfıra yaklaştığı için toplamın limiti $2$ olur.",
            "Aynı fikir devirli ondalık sayılarda da vardır: $0.999\\ldots$ sayısı $\\dfrac{9}{10}+\\dfrac{9}{100}+\\cdots$ toplamının limitidir ve tam olarak $1$ e eşittir. Sonsuz geometrik toplamların ayrıntısı için <a href=\"/blog/geometrik-dizi/\">Geometrik Dizi Konu Anlatımı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Limit ve süreklilik", "icerik": [
            "Bir noktada limit var ve fonksiyonun o noktadaki değerine eşitse fonksiyon o noktada süreklidir; grafiği o noktada kopmaz. Polinomlar, sinüs ve kosinüs ile üstel fonksiyonlar her yerde süreklidir; bu yüzden limitleri yerine yazmayla bulunur.",
            "Tanımsız nokta örneğindeki fonksiyon $x=1$ de sürekli değildir, çünkü o noktada tanımlı değildir. Parçalı örnekte ise limit $3$, değer $5$ olduğu için süreksizlik vardır. Sürekliliğin türleri ve koşulları <a href=\"/blog/sureklilik-konu-anlatimi/\">Süreklilik Konu Anlatımı</a> yazısında.",
        ]},
        {"baslik": "Sınavda limit", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) limit; grafikten limit okuma, polinom ve rasyonel limitler, limit kuralları, belirsizlikler, sağdan ve soldan limit ve sonsuzda limit biçiminde karşına çıkabilir.",
                "Limit, türev ve integral sorularının da temelini oluşturur."),
            "Limit sorusuna her zaman yerine yazarak başla. Sonuç bir sayıysa ve payda sıfır değilse limit odur. Sıfır bölü sıfır çıkarsa sadeleştirmeye, sayı bölü sıfır çıkarsa sağdan ve soldan limite bakmaya geç.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Limiti her zaman $f(a)$ sanmak", "Limit yakın değerlere bakar"],
                ["Fonksiyon tanımsızsa limit yok demek", "Limit yine var olabilir"],
                ["$\\dfrac{0}{0}$ çıkınca limit yok demek", "Önce sadeleştirilir"],
                ["$\\infty$ u bir sayı gibi kullanmak", "Sınırsız büyümeyi anlatır"],
                ["Soldan ve sağdan limiti kontrol etmemek", "İkisi eşit olmalı"],
                ["Bölüm kuralını paydanın limiti sıfırken uygulamak", "Payda limiti sıfır olmamalı"],
            ]),
            "Bu hataların çoğu limit ile fonksiyon değerini aynı şey sanmaktan doğar. Limitin sorusu her zaman aynıdır: noktaya yaklaşırken fonksiyon nereye gidiyor?",
        ]},
    ],
    "sss": [
        ("Limit nedir?",
         "Bir fonksiyonun değişkeni belirli bir sayıya yaklaşırken fonksiyon değerlerinin yaklaştığı sayıdır."),
        ("Limit ile fonksiyon değeri aynı mıdır?",
         "Her zaman değil. Fonksiyon o noktada tanımsız olabilir ya da değeri limitten farklı olabilir; limit yalnızca yakın noktalara bakar."),
        ("Limitin var olması için ne gerekir?",
         "Soldan ve sağdan limitlerin var olması ve birbirine eşit olması gerekir."),
        ("0 bölü 0 çıkarsa limit yok mu demektir?",
         "Hayır. Bu bir belirsizliktir; ifade çarpanlara ayırma ya da eşlenikle çarpma gibi yöntemlerle sadeleştirilir."),
        ("Sonsuzda limit nasıl bulunur?",
         "Rasyonel fonksiyonlarda pay ve paydanın derecelerine bakılır. Dereceler eşitse limit baş katsayıların oranıdır."),
        ("sin x bölü x in limiti kaçtır?",
         "x radyan cinsinden sıfıra yaklaşırken sin x bölü x in limiti 1 dir."),
        ("Polinomun limiti nasıl bulunur?",
         "Polinomların grafiğinde boşluk ya da sıçrama olmadığı için limit, x yerine yaklaşılan sayının yazılmasıyla bulunur."),
        ("1 bölü x in sıfırdaki limiti var mıdır?",
         "Yoktur. Sağdan yaklaşırken değerler sınırsız büyür, soldan yaklaşırken sınırsız küçülür; iki yönün sonucu farklıdır."),
    ],
    "kontrol": [
        "Limitin yaklaşma fikrini açıklayabiliyorum.",
        "Limit gösterimini okuyup yazabiliyorum.",
        "Limit ile fonksiyon değeri arasındaki farkı açıklayabiliyorum.",
        "Limitin var olma koşulunu söyleyebiliyorum.",
        "Polinom ve rasyonel fonksiyonların limitini bulabiliyorum.",
        "Limit kurallarını kullanabiliyorum.",
        "Köklü, mutlak değerli ve trigonometrik ifadelerin limitini hesaplayabiliyorum.",
        "Belirsizliği tanıyıp basit durumlarda sadeleştirebiliyorum.",
        "Sonsuz limitleri ve sonsuzda limiti yorumlayabiliyorum.",
        "Anlık hızı limitle hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["sagdan-soldan-limit", "limitte-belirsizlikler", "sureklilik-konu-anlatimi"],
}
