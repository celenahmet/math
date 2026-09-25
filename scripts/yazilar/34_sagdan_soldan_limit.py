# scripts/yazilar/34_sagdan_soldan_limit.py — Sagdan ve Soldan Limit (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "sagdan-soldan-limit",
    "baslik": "Sağdan ve Soldan Limit Nasıl Bulunur?",
    "aciklama": "Sağdan ve soldan limit nasıl bulunur? Parçalı fonksiyonlar, mutlak değer, tam değer, payda sıfır olan kesirler, üstel ifadeler ve grafikten okuma; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "sagdan-soldan-limit",
    "kapak_alt": "Sağdan ve soldan limit: ortadaki ışıklı hedefe soldan mavi, sağdan kırmızı bilyelerle yaklaşan iki öğrenci",
    "ozet": "Bir noktaya iki yönden yaklaşılabilir: o sayıdan küçük değerlerden ya da büyük değerlerden. Bu iki yaklaşmanın sonuçlarına soldan ve sağdan limit denir ve limitin var olup olmadığı bu iki değerin karşılaştırılmasıyla anlaşılır. Bu yazıda tek yönlü limitlerin tanımını ve gösterimini, parçalı fonksiyonlarda limit hesabını, limiti var yapan parametreyi bulmayı, mutlak değerli ifadeleri, tam değer fonksiyonunu, paydası sıfır olan kesirlerde işaret incelemesini, üstel ve trigonometrik örnekleri, tanım kümesinin uç noktalarını ve grafikten limit okumayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "İki yönden yaklaşma", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için limitin temel fikrini ve parçalı fonksiyonları biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/limit-konu-anlatimi/\">Limit Konu Anlatımı</a> yazısına göz at."),
            "Sayı doğrusunda bir $a$ noktasına iki yönden yaklaşılabilir. Soldan yaklaşırken $x$ değerleri $a$ dan küçüktür, sağdan yaklaşırken büyüktür. İki yönden yaklaşırken fonksiyonun yöneldiği değerler farklı olabilir; bu yüzden her yön ayrı hesaplanır.",
            "Kapaktaki öğrencilerden biri mavi bilyeleri hedefe soldan, diğeri kırmızı bilyeleri sağdan yaklaştırıyor. İki dizi aynı hedefe ulaşıyorsa limit vardır; farklı noktalara yöneliyorsa limit yoktur. Bu yazının bütün soruları bu karşılaştırmaya dayanır ve her örnekte önce iki yön ayrı ayrı hesaplanır.",
        ]},
        {"baslik": "Soldan ve sağdan limit", "icerik": [
            "$x$, $a$ dan küçük değerlerle $a$ ya yaklaşırken $f(x)$ in yöneldiği değere <strong>soldan limit</strong>, büyük değerlerle yaklaşırken yöneldiği değere <strong>sağdan limit</strong> denir:",
            tablo(["Yön", "Gösterim", "Anlamı"], [
                ["Soldan", "$\\lim_{x \\to a^-} f(x)$", "$x<a$ iken yaklaşma"],
                ["Sağdan", "$\\lim_{x \\to a^+} f(x)$", "$x>a$ iken yaklaşma"],
            ]),
            "Sayının üstündeki eksi işareti soldan, artı işareti sağdan yaklaşmayı gösterir. Bu işaretler sayının negatif ya da pozitif olduğunu değil, yaklaşma yönünü anlatır: $x \\to 2^-$ ifadesi $1.9$, $1.99$, $1.999$ gibi değerleri düşündürür.",
        ]},
        {"baslik": "Limitin var olma koşulu", "icerik": [
            "Bir noktada limitin var olması için soldan ve sağdan limitlerin ikisinin de var olması ve birbirine eşit olması gerekir:",
            "$$\\lim_{x \\to a} f(x)=L \\Leftrightarrow \\lim_{x \\to a^-} f(x)=\\lim_{x \\to a^+} f(x)=L$$",
            hap("Soldan limit ile sağdan limit eşitse limit vardır ve bu ortak değerdir.",
                "Farklıysa ya da biri yoksa limit yoktur."),
            "Fonksiyonun $a$ noktasındaki değeri bu koşulda yer almaz. Fonksiyon $a$ da tanımsız olsa ya da farklı bir değer alsa bile iki yönün sonucu eşitse limit vardır.",
        ]},
        {"baslik": "Parçalı fonksiyonda eşit limitler", "icerik": [
            "Parçalı fonksiyonlarda kuralın değiştiği noktaya kritik nokta denir. Bu noktada iki yön ayrı parçalardan hesaplanır: soldan limit için sol taraftaki kural, sağdan limit için sağ taraftaki kural kullanılır.",
            koordinat_grafik("Kırık doğru biçimindeki parçalı fonksiyon", [("x < 2 için y = x + 1", lambda x: x + 1 if x < 2 else None), ("x ≥ 2 için y = 2x - 1", lambda x: 2 * x - 1 if x >= 2 else None)],
                             (-1, 4.5), (-1, 8), adim=1, noktalar=[(2, 3, "", True)]),
            ornek(
                "$x<2$ için $f(x)=x+1$, $x \\ge 2$ için $f(x)=2x-1$ olsun.",
                "$x=2$ deki limiti bulalım.",
                "Soldan limit: $\\lim_{x \\to 2^-}(x+1)=3$. Sağdan limit: $\\lim_{x \\to 2^+}(2x-1)=3$.",
                "İki değer eşit olduğu için $\\lim_{x \\to 2} f(x)=3$ olur."),
        ]},
        {"baslik": "Parçalı fonksiyonda sıçrama", "icerik": [
            "İki parçanın uçları aynı yüksekliğe gelmiyorsa grafikte bir sıçrama oluşur. Bu durumda soldan ve sağdan limitler farklıdır ve limit yoktur.",
            koordinat_grafik("Sıçramalı parçalı fonksiyon", [("x < 1 için y = x²", lambda x: x * x if x < 1 else None), ("x ≥ 1 için y = x + 2", lambda x: x + 2 if x >= 1 else None)],
                             (-2, 4), (-1, 7), adim=1, noktalar=[(1, 1, "", False), (1, 3, "", True)]),
            ornek(
                "$x<1$ için $f(x)=x^2$, $x \\ge 1$ için $f(x)=x+2$ olsun.",
                "$x=1$ deki limiti inceleyelim.",
                "Soldan limit $1^2=1$, sağdan limit $1+2=3$ olur.",
                "İki değer farklı olduğu için $\\lim_{x \\to 1} f(x)$ yoktur; fonksiyonun değeri ise $f(1)=3$ tür."),
            "Grafikteki boş daire, sol parçanın ulaşamadığı $(1, 1)$ noktasını, dolu daire ise fonksiyonun gerçekten aldığı $(1, 3)$ değerini gösterir.",
        ]},
        {"baslik": "Limiti var yapan parametre", "icerik": [
            "Parçalı fonksiyonun kurallarından birinde bilinmeyen bir katsayı varsa, limitin var olması için iki yönün sonuçları eşitlenir ve katsayı bulunur.",
            ornek(
                "$x<2$ için $f(x)=3x+a$, $x \\ge 2$ için $f(x)=x^2+1$ olsun.",
                "$\\lim_{x \\to 2} f(x)$ in var olması için $a$ yı bulalım.",
                "Soldan limit $6+a$, sağdan limit $5$ tir.",
                "$6+a=5$ olmalı; $a=-1$ bulunur ve limit $5$ olur."),
        ]},
        {"baslik": "Üç parçalı fonksiyon", "icerik": [
            "Parçalı bir fonksiyonun birden fazla kritik noktası olabilir. Her kritik noktada yalnızca o noktanın iki yanındaki parçalar kullanılır; diğer parçaların o noktadaki limitle ilgisi yoktur.",
            ornek(
                "$x<0$ için $f(x)=x+2$, $0 \\le x<2$ için $f(x)=x^2$, $x \\ge 2$ için $f(x)=6-x$ olsun.",
                "$x=0$ ve $x=2$ noktalarındaki limitleri inceleyelim.",
                "$x=0$ da soldan limit $2$, sağdan limit $0$ dır; limit yoktur.",
                "$x=2$ de soldan limit $4$, sağdan limit $6-2=4$ tür; limit $4$ olur."),
        ]},
        {"baslik": "İki parametreli parçalı fonksiyon", "icerik": [
            "İki kritik noktası olan bir parçalı fonksiyonda iki bilinmeyen varsa, her noktada limitin var olma koşulu bir denklem verir. İki denklem birlikte çözülür.",
            ornek(
                "$x<1$ için $f(x)=x+a$, $1 \\le x<3$ için $f(x)=2x+b$, $x \\ge 3$ için $f(x)=x^2$ olsun ve iki noktada da limit var olsun.",
                "$a$ ve $b$ yi bulalım.",
                "$x=3$ te $6+b=9$ olmalı, yani $b=3$.",
                "$x=1$ de $1+a=2+b=5$ olmalı, yani $a=4$ bulunur."),
        ]},
        {"baslik": "Mutlak değerli ifadeler", "icerik": [
            "Mutlak değer, içindeki ifadenin işaretine göre farklı kurallarla açılır. İçi sıfır yapan noktada mutlak değer iki farklı ifadeye dönüştüğü için soldan ve sağdan limitler ayrı hesaplanır.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{|x|}{x}$ limiti verilsin.",
                "Limiti inceleyelim.",
                "$x>0$ iken $|x|=x$ olduğundan kesir $1$ dir; sağdan limit $1$ olur. $x<0$ iken $|x|=-x$ olduğundan kesir $-1$ dir; soldan limit $-1$ olur.",
                "İki değer farklı olduğu için limit yoktur."),
            ornek(
                "$\\lim_{x \\to 2}\\dfrac{x^2-4}{|x-2|}$ limiti verilsin.",
                "Soldan ve sağdan limitleri bulalım.",
                "$x>2$ iken kesir $x+2$ ye eşittir; sağdan limit $4$ olur.",
                "$x<2$ iken kesir $-(x+2)$ ye eşittir; soldan limit $-4$ olur ve limit yoktur."),
        ]},
        {"baslik": "Karekök ve mutlak değer", "icerik": [
            "Bir ifadenin karesinin karekökü, ifadenin kendisi değil mutlak değeridir: $\\sqrt{x^2}=|x|$. Bu eşitlik gözden kaçırılırsa tek yönlü limitlerden biri yanlış hesaplanır.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{\\sqrt{x^2}}{x}$ limiti verilsin.",
                "Soldan ve sağdan limitleri bulalım.",
                "Pay $|x|$ e eşittir; sağdan yaklaşırken kesir $1$ olur.",
                "Soldan yaklaşırken kesir $-1$ olur; iki yön farklı olduğu için limit yoktur."),
        ]},
        {"baslik": "Tam değer fonksiyonu", "icerik": [
            "Tam değer fonksiyonu $\\lfloor x \\rfloor$, bir sayıdan büyük olmayan en büyük tam sayıyı verir: $\\lfloor 2.7 \\rfloor=2$, $\\lfloor -1.3 \\rfloor=-2$. Grafiği basamaklıdır ve her tam sayıda bir birim sıçrar.",
            ornek(
                "$\\lfloor x \\rfloor$ fonksiyonu verilsin.",
                "$x=2$ ve $x=2.5$ noktalarındaki limitleri inceleyelim.",
                "$x$ $2$ ye soldan yaklaşırken değer $1$, sağdan yaklaşırken $2$ dir; $x=2$ de limit yoktur.",
                "$2.5$ in yakınında fonksiyon sabit $2$ dir; $x=2.5$ te limit $2$ olur."),
            "Tam değerin içinde bir ifade varsa önce ifadenin hangi yönden hangi tam sayıya yaklaştığına bakılır. Örneğin $x$ $1$ e soldan yaklaşırken $2x$ $2$ ye soldan yaklaşır ve $\\lfloor 2x \\rfloor$ in soldan limiti $1$, sağdan limiti $2$ olur.",
        ]},
        {"baslik": "Mutlak değerin kendisi", "icerik": [
            "Mutlak değer içeren her ifadenin kritik noktada limiti yoktur. $|x|$ fonksiyonunun kendisi sıfırda kırılır ama kopmaz: soldan yaklaşırken $-x$, sağdan yaklaşırken $x$ değerleri sıfıra gider.",
            "Bu yüzden $\\lim_{x \\to 0}|x|=0$ dır. Limitin yok olduğu $\\dfrac{|x|}{x}$ örneğinde sorun mutlak değer değil, onun sıfıra giden $x$ e bölünmesidir. Mutlak değerli bir ifadeyle karşılaşınca iki yönü hesaplamak, sonucun hangisi olduğunu hemen gösterir.",
        ]},
        {"baslik": "Tam değerli toplam", "icerik": [
            "Tam değer bir toplamın içinde yer alıyorsa yalnızca tam değerli terim yöne göre değişir; diğer terimler her iki yönde aynı sayıya gider.",
            ornek(
                "$\\lim_{x \\to 3}(\\lfloor x \\rfloor+x)$ limiti verilsin.",
                "Soldan ve sağdan limitleri bulalım.",
                "Soldan yaklaşırken $\\lfloor x \\rfloor=2$ olduğundan limit $2+3=5$ olur.",
                "Sağdan yaklaşırken $\\lfloor x \\rfloor=3$ olduğundan limit $3+3=6$ olur; limit yoktur."),
        ]},
        {"baslik": "Paydası sıfır olan kesirler", "icerik": [
            "Yerine yazınca sıfırdan farklı bir sayının sıfıra bölümü çıkıyorsa kesir sınırsız büyür ya da küçülür. Hangisinin olduğu, paydanın o yönden pozitif mi negatif mi olduğuna bakılarak belirlenir.",
            ornek(
                "$\\lim_{x \\to 2}\\dfrac{1}{x-2}$ limiti verilsin.",
                "Soldan ve sağdan limitleri bulalım.",
                "Sağdan yaklaşırken payda küçük pozitif sayılardır; kesir $+\\infty$ a gider.",
                "Soldan yaklaşırken payda küçük negatif sayılardır; kesir $-\\infty$ a gider. İki yön farklı olduğu için limit yoktur."),
            "Payda kare olduğunda durum değişir: $\\dfrac{1}{(x-2)^2}$ ifadesinde payda iki yönden de pozitiftir ve iki tek yönlü limit de $+\\infty$ olur.",
        ]},
        {"baslik": "İşaret incelemesi", "icerik": [
            "Pay ve paydadaki çarpanların işaretleri tek tek belirlenerek kesrin işareti bulunur. Bu yöntem, payda sıfıra giderken sonsuzun işaretini hatasız verir.",
            ornek(
                "$\\lim_{x \\to 3^+}\\dfrac{x+1}{x-3}$ ve $\\lim_{x \\to 3^-}\\dfrac{x+1}{x-3}$ limitleri verilsin.",
                "Limitleri bulalım.",
                "Pay $4$ e yaklaşır ve pozitiftir. Sağdan payda pozitif, soldan negatiftir.",
                "Sağdan limit $+\\infty$, soldan limit $-\\infty$ olur."),
        ]},
        {"baslik": "Üstel ifadelerde tek yönlü limit", "icerik": [
            "Üssünde $\\dfrac{1}{x}$ gibi bir ifade bulunan üstel fonksiyonlarda üssün sonsuza mı eksi sonsuza mı gittiği yöne bağlıdır. Bu yüzden iki yönün sonucu çok farklı olabilir.",
            ornek(
                "$\\lim_{x \\to 0} 2^{1/x}$ limiti verilsin.",
                "Soldan ve sağdan limitleri bulalım.",
                "Sağdan yaklaşırken üs $+\\infty$ a gider ve ifade sınırsız büyür.",
                "Soldan yaklaşırken üs $-\\infty$ a gider ve ifade $0$ a yaklaşır. İki yön farklı olduğu için limit yoktur."),
        ]},
        {"baslik": "Trigonometrik örnek", "icerik": [
            "Tanjant fonksiyonu kosinüsün sıfır olduğu noktalarda tanımsızdır ve bu noktaların iki yanında ters yönlere gider. $\\dfrac{\\pi}{2}$ nin solunda sinüs ve kosinüs pozitif olduğu için tanjant $+\\infty$ a, sağında kosinüs negatif olduğu için $-\\infty$ a gider.",
            ornek(
                "$\\tan x$ fonksiyonu verilsin.",
                "$x=\\dfrac{\\pi}{2}$ deki tek yönlü limitleri bulalım.",
                "$\\lim_{x \\to \\pi/2^-}\\tan x=+\\infty$ olur.",
                "$\\lim_{x \\to \\pi/2^+}\\tan x=-\\infty$ olur; tanjantın grafiğindeki dikey asimptotun iki yanı budur."),
        ]},
        {"baslik": "Tanım kümesinin uç noktası", "icerik": [
            "Fonksiyon bir noktanın yalnızca bir yanında tanımlıysa o noktada yalnızca tek yönlü limitten söz edilir. $\\sqrt{x}$ fonksiyonu negatif sayılarda tanımsız olduğu için $x=0$ da yalnızca sağdan yaklaşılabilir.",
            "Bu durumda $\\lim_{x \\to 0^+}\\sqrt{x}=0$ yazılır. Lise matematiğinde tanım kümesinin uç noktasındaki limit genellikle bu tek yönlü limit olarak kabul edilir; soruda aksi belirtilmedikçe bu yaklaşım kullanılır.",
        ]},
        {"baslik": "Grafikten tek yönlü limit okumak", "icerik": [
            "Grafik verildiğinde soldan limit için grafiğin noktanın sol yanından geldiği yükseklik, sağdan limit için sağ yanından geldiği yükseklik okunur. Dolu ve boş daireler limit değil, fonksiyonun o noktadaki değeri hakkında bilgi verir.",
            tablo(["Grafikte görülen", "Soldan limit", "Sağdan limit", "Limit"], [
                ["Kesintisiz geçiş", "$L$", "$L$", "$L$"],
                ["Boşluk", "$L$", "$L$", "$L$"],
                ["Sıçrama", "$L_1$", "$L_2$", "Yok"],
                ["Dikey asimptot", "$\\pm\\infty$", "$\\pm\\infty$", "Sonlu değer yok"],
            ]),
            "Sıçramalı örnekteki grafikte sol parça $1$ yüksekliğine, sağ parça $3$ yüksekliğine gelir. Fonksiyonun değeri dolu daireden $3$ olarak okunur, ama limit yoktur.",
        ]},
        {"baslik": "İşaret fonksiyonu", "icerik": [
            "İşaret fonksiyonu pozitif sayılara $1$, negatif sayılara $-1$, sıfıra $0$ karşılık getirir. Sıfırda iki yönden farklı değerlere gittiği için bu noktada limiti yoktur.",
            ornek(
                "İşaret fonksiyonu verilsin.",
                "$x=0$ ve $x=3$ noktalarındaki limitleri inceleyelim.",
                "Sıfırda soldan limit $-1$, sağdan limit $1$ dir; limit yoktur.",
                "$3$ ün yakınında fonksiyon sabit $1$ dir; limit $1$ olur."),
        ]},
        {"baslik": "Uygulama: kademeli ücret", "icerik": [
            "Günlük hayattaki kademeli ücretler tek yönlü limitlerin somut bir örneğidir. Ücret belirli eşiklerde birden değişir; eşiğin iki yanındaki ücretler farklıdır. Otopark, kargo ve elektrik tarifeleri bu tür basamaklı fonksiyonlarla anlatılır ve grafikleri tam değer fonksiyonunun grafiğine benzer.",
            ornek(
                "Bir kargo firması $1$ kilograma kadar olan paketler için $30$ TL, $1$ kilogramı aşan paketler için $45$ TL alıyor.",
                "Ücret fonksiyonunun $1$ kilogramdaki tek yönlü limitlerini bulalım.",
                "Ağırlık $1$ e soldan yaklaşırken ücret $30$ TL dir.",
                "Sağdan yaklaşırken ücret $45$ TL dir; iki yön farklı olduğu için eşikte limit yoktur."),
        ]},
        {"baslik": "Tek yönlü limit ve süreklilik", "icerik": [
            "Bir fonksiyonun bir noktada sürekli olması için soldan limit, sağdan limit ve fonksiyonun değeri üçünün de eşit olması gerekir. Tek yönlü limitler, sürekliliği incelemenin en temel aracıdır.",
            "Eşit limitli örnekte soldan ve sağdan limit $3$ tür ve $f(2)=2 \\cdot 2-1=3$ olduğu için fonksiyon $2$ de süreklidir. Sıçramalı örnekte ise limit bile olmadığı için fonksiyon $1$ de sürekli değildir. Ayrıntılar için <a href=\"/blog/sureklilik-konu-anlatimi/\">Süreklilik Konu Anlatımı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sınavda sağdan ve soldan limit", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) tek yönlü limitler; grafikten limit okuma, parçalı fonksiyonlar, mutlak değer ve tam değer içeren ifadeler ve limiti var yapan parametre biçiminde karşına çıkabilir.",
                "Süreklilik soruları da çoğu zaman tek yönlü limitlerle çözülür."),
            "Parçalı, mutlak değerli ya da tam değerli bir ifade görüyorsan kritik noktada limiti hemen iki yöne ayır. Her yön için ifadeyi sadeleştirip ayrı hesapla, sonra karşılaştır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Sağdan limit için sol parçanın kuralını kullanmak", "Her yön kendi parçasından"],
                ["Limiti fonksiyonun değerinden okumak", "Dolu daire limit değildir"],
                ["$x \\to 2^-$ yi negatif sayı sanmak", "Eksi yalnızca yönü gösterir"],
                ["$|x|/x$ in limitini $1$ sanmak", "Soldan $-1$, sağdan $1$"],
                ["Tam değerde iki yönü aynı almak", "Tam sayılarda sıçrama var"],
                ["Payda sıfırken işareti incelememek", "Her yönde işaret ayrı"],
            ]),
            "Bu hataların hepsi tek bir alışkanlıkla önlenir: kritik noktada her zaman iki yönü ayrı ayrı yaz. Sayı doğrusu üzerinde noktanın solunu ve sağını çizip her bölgedeki kuralı not etmek bu alışkanlığı kolaylaştırır.",
        ]},
    ],
    "sss": [
        ("Soldan limit nedir?",
         "x, a dan küçük değerlerle a ya yaklaşırken fonksiyonun yöneldiği değerdir ve x a eksi ye giderken limit olarak yazılır."),
        ("Limitin var olması için ne gerekir?",
         "Soldan ve sağdan limitlerin ikisinin de var olması ve birbirine eşit olması gerekir. Fonksiyonun o noktadaki değeri bu koşulda yer almaz."),
        ("Parçalı fonksiyonda limit nasıl bulunur?",
         "Kuralın değiştiği noktada soldan limit sol parçanın kuralıyla, sağdan limit sağ parçanın kuralıyla hesaplanır ve karşılaştırılır."),
        ("Mutlak değerin sıfırdaki limiti var mıdır?",
         "Mutlak x in sıfırdaki limiti vardır ve 0 dır. Ama mutlak x bölü x in sıfırdaki limiti yoktur; soldan -1, sağdan 1 dir."),
        ("Tam değer fonksiyonunun tam sayılarda limiti var mıdır?",
         "Yoktur. Tam sayılarda soldan limit bir eksik tam sayı, sağdan limit o tam sayının kendisidir."),
        ("1 bölü x eksi 2 nin 2 deki limiti nedir?",
         "Soldan eksi sonsuz, sağdan artı sonsuzdur. İki yön farklı olduğu için limit yoktur."),
        ("x 2 ye soldan yaklaşıyor ne demektir?",
         "x in 2 den küçük değerlerle, örneğin 1.9, 1.99, 1.999 gibi sayılarla 2 ye yaklaşması demektir. Üstteki eksi işareti yönü gösterir, sayının negatif olduğunu değil."),
    ],
    "kontrol": [
        "Soldan ve sağdan limitin anlamını açıklayabiliyorum.",
        "Tek yönlü limit gösterimini doğru okuyup yazabiliyorum.",
        "Limitin var olma koşulunu uygulayabiliyorum.",
        "Parçalı fonksiyonlarda iki yönü ayrı hesaplayabiliyorum.",
        "Limiti var yapan parametreyi bulabiliyorum.",
        "Mutlak değerli ifadelerin tek yönlü limitlerini hesaplayabiliyorum.",
        "Tam değer ve işaret fonksiyonunun limitlerini inceleyebiliyorum.",
        "Paydası sıfıra giden kesirlerde işaret incelemesi yapabiliyorum.",
        "Üstel ve trigonometrik ifadelerde tek yönlü limitleri bulabiliyorum.",
        "Grafikten soldan ve sağdan limitleri okuyabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["limit-konu-anlatimi", "limitte-belirsizlikler", "sureklilik-konu-anlatimi"],
}
