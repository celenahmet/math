# scripts/yazilar/72_devirli_ondalik.py — Devirli Ondalik Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "devirli-ondalik-sayilar-nasil-kesre-cevrilir",
    "baslik": "Devirli Ondalık Sayılar Nasıl Kesre Çevrilir?",
    "aciklama": "Devirli ondalık sayı nedir, neden oluşur, kesre nasıl çevrilir? Kuralın ispatı, 0,999 un 1 e eşitliği, devrin uzunluğu ve işlemler; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "devirli-ondalik-sayilar-nasil-kesre-cevrilir",
    "kapak_alt": "Devirli ondalık sayılar: tekrar eden mavi ve kırmızı desenli ahşap parçaları yeniden düzenleyen iki öğrenci",
    "ozet": "Üçte bir ondalık sayıya çevrilmek istendiğinde bölme hiç bitmez: sıfır virgül üç üç üç diye sonsuza kadar sürer. Bu tür sayılara devirli ondalık sayı denir ve her biri aslında bir kesirdir. Bu yazıda devirli sayıların neden oluştuğunu, nasıl gösterildiğini, kesre çevirme kuralını ve bu kuralın neden doğru olduğunu, sıfır virgül dokuz dokuzun neden bire eşit olduğunu, devrin uzunluğunu ve devirli sayılarla işlemi çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Devirli ondalık sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için ondalık gösterimi ve kesirleri biliyor olman yeterli.",
                "Ondalık gösterimin temeli için <a href=\"/blog/ondalik-gosterim-konu-anlatimi-pdf/\">Ondalık Gösterim Konu Anlatımı PDF</a> yazısına göz at."),
            "Bazı kesirler bölünürken bölme işlemi bir noktada biter: $\\dfrac{3}{8}=0.375$. Bazılarında ise bölme hiç bitmez ve ondalık kısımdaki bir rakam ya da rakam grubu sonsuza kadar aynı sırayla tekrar eder. Bu sayılara <strong>devirli ondalık sayı</strong>, tekrar eden rakam grubuna da <strong>devreden</strong> denir.",
            "Devreden kısım, üzerine çizgi çekilerek gösterilir. Böylece sonsuz bir yazım tek satıra sığar:",
            tablo(["Kesir", "Açık yazım", "Devirli gösterim"], [
                ["$\\dfrac{1}{3}$", "$0.333\\ldots$", "$0.\\overline{3}$"],
                ["$\\dfrac{4}{11}$", "$0.3636\\ldots$", "$0.\\overline{36}$"],
                ["$\\dfrac{1}{6}$", "$0.1666\\ldots$", "$0.1\\overline{6}$"],
                ["$\\dfrac{1}{7}$", "$0.142857142857\\ldots$", "$0.\\overline{142857}$"],
            ]),
            "Üçüncü satırda $1$ rakamı tekrar etmez, yalnızca $6$ tekrar eder. Tekrar etmeyen bu kısma <strong>devretmeyen</strong> kısım denir ve çizginin dışında kalır.",
            hap("Devirli ondalık sayıda tekrar eden rakam grubu devredendir ve üzerine çizgi çekilir.",
                "Virgülden sonra tekrar etmeyen rakamlar devretmeyen kısımdır ve çizginin dışında kalır."),
        ]},
        {"baslik": "Devir neden oluşur?", "icerik": [
            "Bir kesri ondalık sayıya çevirirken uzun bölme yapılır. Her adımda bir kalan elde edilir ve bu kalan her zaman bölenden küçüktür. Örneğin $7$ ye bölerken kalan yalnızca $0, 1, 2, 3, 4, 5$ ya da $6$ olabilir.",
            "Kalan $0$ olursa bölme biter ve ondalık sayı sonludur. Kalan hiç $0$ olmazsa, sınırlı sayıda kalan olduğu için bir süre sonra daha önce görülmüş bir kalan mutlaka yeniden ortaya çıkar. O andan itibaren bölme adımları aynı sırayla tekrar eder ve basamaklar da tekrar eder. Devrin nedeni budur.",
            ornek(
                "$\\dfrac{1}{7}$ kesri verilsin.",
                "Uzun bölmede kalanları izleyelim.",
                "Kalanlar sırayla $3, 2, 6, 4, 5, 1$ olur; bölüm basamakları $1, 4, 2, 8, 5, 7$ dir.",
                "Altıncı adımda kalan yeniden $1$ oluyor; yani bölmeye başladığımız duruma dönüyoruz.",
                "Sonuç: $\\dfrac{1}{7}=0.\\overline{142857}$. Devreden $6$ basamaklıdır."),
            "Bu akıl yürütme bir sonuç daha verir: paydası $q$ olan bir kesirde devreden en fazla $q-1$ basamaklı olabilir, çünkü sıfır dışında en fazla $q-1$ farklı kalan vardır.",
            "<h3>Hangi kesirler devirlidir?</h3>",
            "En sade hâldeki bir kesrin paydasında $2$ ve $5$ ten başka asal çarpan yoksa ondalık gösterimi sonludur; varsa devirlidir. Bunun nedeni, sonlu ondalık sayıların paydasının $10$ un bir kuvveti olmasıdır ve $10=2 \\cdot 5$ tir.",
            ornek(
                "$\\dfrac{7}{40}$, $\\dfrac{7}{30}$ ve $\\dfrac{3}{12}$ kesirleri verilsin.",
                "Hangilerinin sonlu, hangilerinin devirli olduğunu bulalım.",
                "$40=2^3 \\cdot 5$: yalnız $2$ ve $5$ var, sonlu: $\\dfrac{7}{40}=0.175$.",
                "$30=2 \\cdot 3 \\cdot 5$: paydada $3$ var, devirli: $\\dfrac{7}{30}=0.2\\overline{3}$.",
                "$\\dfrac{3}{12}$ önce sadeleştirilir: $\\dfrac{1}{4}$. Payda $4=2^2$, sonlu: $0.25$."),
            dikkat(
                "Karar vermeden önce kesri sadeleştir.",
                "$\\dfrac{3}{12}$ ün paydasında $3$ görünür ama bu $3$ payla sadeleşir. Sadeleştirmeden karar verilirse sonlu bir kesir yanlışlıkla devirli sanılır."),
            hap("Bir pizza $3$ kişiye eşit bölününce herkese $\\dfrac{1}{3}=0.333\\ldots$ pizza düşer.", "Hesap makinesinin gösterdiği $0.3333333$, bu sonsuz devrin ekrana sığan kısmıdır.", gunluk=True),
        ]},
        {"baslik": "Devirli sayıyı kesre çevirme kuralı", "icerik": [
            "Bir devirli ondalık sayıyı kesre çevirmek için şu kural kullanılır:",
            "<ul><li><strong>Pay:</strong> virgül yokmuş gibi yazılan sayının tamamından, devretmeyen kısmın çıkarılmasıyla bulunur.</li>"
            "<li><strong>Payda:</strong> devreden basamak sayısı kadar $9$, onun sağına da virgülden sonraki devretmeyen basamak sayısı kadar $0$ yazılarak bulunur.</li></ul>",
            ornek(
                "$0.\\overline{3}$ ve $0.\\overline{36}$ sayıları verilsin.",
                "Kesre çevirelim.",
                "$0.\\overline{3}$: pay $3-0=3$, payda bir devreden basamak için $9$: $\\dfrac{3}{9}=\\dfrac{1}{3}$.",
                "$0.\\overline{36}$: pay $36-0=36$, payda iki devreden basamak için $99$: $\\dfrac{36}{99}=\\dfrac{4}{11}$."),
            ornek(
                "$0.1\\overline{6}$ sayısı verilsin.",
                "Kesre çevirelim.",
                "Sayının tamamı virgülsüz $16$, devretmeyen kısım $1$: pay $16-1=15$.",
                "Bir devreden basamak için bir $9$, bir devretmeyen ondalık basamak için bir $0$: payda $90$.",
                "Sonuç: $\\dfrac{15}{90}=\\dfrac{1}{6}$."),
            ornek(
                "$2.\\overline{45}$ ve $1.2\\overline{34}$ sayıları verilsin.",
                "Kesre çevirelim.",
                "$2.\\overline{45}$: pay $245-2=243$, payda $99$: $\\dfrac{243}{99}=\\dfrac{27}{11}$.",
                "$1.2\\overline{34}$: pay $1234-12=1222$, payda iki $9$ ve bir $0$: $990$.",
                "$\\dfrac{1222}{990}=\\dfrac{611}{495}$."),
            dikkat(
                "Paydadaki sıfırlar, virgülden sonraki devretmeyen basamaklar içindir.",
                "Tam kısım paydaya sıfır eklemez. $2.\\overline{45}$ te virgülden sonra devretmeyen basamak olmadığı için payda yalnızca $99$ dur, $990$ değil."),
            hap("Pay, virgül yokmuş gibi yazılan sayıdan devretmeyen kısım çıkarılarak bulunur.", "Paydaya devreden basamak sayısı kadar $9$, onun sağına devretmeyen ondalık basamak sayısı kadar $0$ yazılır."),
        ]},
        {"baslik": "Kural neden doğru?", "icerik": [
            "Kural ezber değildir; onun kuvvetleriyle çarpıp çıkarma fikrinden gelir. Amaç, devreden kısmı birbirini götürecek biçimde iki sayı elde etmektir.",
            ornek(
                "$x=0.\\overline{36}$ olsun.",
                "$x$ i kesir olarak bulalım.",
                "Devreden iki basamaklı olduğu için $100$ ile çarpalım: $100x=36.\\overline{36}$.",
                "İki eşitliği taraf tarafa çıkaralım; sonsuz devreden kısımlar birbirini götürür: $100x-x=36$.",
                "$99x=36$, yani $x=\\dfrac{36}{99}=\\dfrac{4}{11}$."),
            ornek(
                "$x=0.1\\overline{6}$ olsun.",
                "$x$ i kesir olarak bulalım.",
                "Devretmeyen kısmı virgülün soluna almak için $10$ ile çarpalım: $10x=1.\\overline{6}$.",
                "Bir devreden basamağı da sola almak için $100$ ile çarpalım: $100x=16.\\overline{6}$.",
                "Çıkaralım: $100x-10x=16-1$, yani $90x=15$ ve $x=\\dfrac{15}{90}=\\dfrac{1}{6}$."),
            "İkinci örnekte paydanın $90$, payın $16-1$ olduğuna dikkat et. Kuraldaki \"sayının tamamı eksi devretmeyen kısım\" ve \"dokuzlar ve sıfırlar\" ifadeleri tam olarak bu çıkarmanın sonucudur.",
        ]},
        {"baslik": "Sıfır virgül dokuz dokuz neden bire eşittir?", "icerik": [
            "Kural $0.\\overline{9}$ sayısına uygulanınca şaşırtıcı bir sonuç çıkar: pay $9$, payda $9$ ve $\\dfrac{9}{9}=1$. Yani $0.999\\ldots$ ile $1$ aynı sayıdır.",
            "Bu sonuç başka yollarla da görülebilir. $\\dfrac{1}{3}=0.\\overline{3}$ eşitliğinin iki tarafı $3$ ile çarpılırsa $1=0.\\overline{9}$ elde edilir. Ya da $x=0.\\overline{9}$ için $10x=9.\\overline{9}$ ve $10x-x=9$ yazılır; buradan $9x=9$ ve $x=1$ bulunur.",
            "Sezgiye ters gelmesinin nedeni, sonsuz sayıda dokuzun \"bir türlü bire ulaşamayan\" bir süreç gibi düşünülmesidir. Oysa $0.\\overline{9}$ bir süreç değil, tek bir sayıdır. İki sayı farklı olsaydı aralarına başka bir sayı sığardı; $0.\\overline{9}$ ile $1$ arasında ise hiçbir sayı yoktur.",
            ornek(
                "$2.4\\overline{9}$ sayısı verilsin.",
                "Sayıyı kurala göre kesre çevirelim.",
                "Pay: $249-24=225$. Payda: bir $9$ ve bir $0$: $90$.",
                "$\\dfrac{225}{90}=\\dfrac{5}{2}=2.5$. Yani $2.4\\overline{9}=2.5$ tir."),
            dikkat(
                "Sonu $9$ devreden her sayı sonlu bir ondalık sayıya eşittir.",
                "Bu yüzden devirli gösterimde devredenin $9$ olması genellikle tercih edilmez; aynı sayı sonlu biçimde yazılır."),
            hap("$0.\\overline{9}=1$ olur; $0.999\\ldots$ ile $1$ aynı sayıdır."),
        ]},
        {"baslik": "Devrin uzunluğu", "icerik": [
            "Devreden kısmın kaç basamaklı olduğu paydaya bağlıdır ve bazen şaşırtıcı biçimde uzun olabilir. Aşağıdaki birim kesirlerde devrin uzunluğu görülüyor:",
            tablo(["Kesir", "Ondalık gösterim", "Devrin uzunluğu"], [
                ["$\\dfrac{1}{3}$", "$0.\\overline{3}$", "$1$"],
                ["$\\dfrac{1}{11}$", "$0.\\overline{09}$", "$2$"],
                ["$\\dfrac{1}{37}$", "$0.\\overline{027}$", "$3$"],
                ["$\\dfrac{1}{7}$", "$0.\\overline{142857}$", "$6$"],
                ["$\\dfrac{1}{13}$", "$0.\\overline{076923}$", "$6$"],
            ]),
            "$\\dfrac{1}{7}$ de devrin uzunluğu $6$ dır ve bu, $7-1$ ile, yani mümkün olan en büyük uzunlukla aynıdır. $\\dfrac{1}{13}$ de ise devir $6$ basamaklıdır, $12$ değil; üst sınır her zaman dolmaz.",
            ornek(
                "$\\dfrac{1}{7}=0.\\overline{142857}$ verilsin.",
                "Virgülden sonraki $100$ üncü basamağı bulalım.",
                "Devir $6$ basamaklı; $100$ ün $6$ ya bölümünden kalan $4$.",
                "Kalan $4$ olduğu için $100$ üncü basamak, devrin dördüncü basamağıdır: $8$."),
        ]},
        {"baslik": "Devirli sayılarla işlem", "icerik": [
            "Devirli sayılar toplanırken, çıkarılırken, çarpılırken ya da bölünürken en güvenli yol önce hepsini kesre çevirmektir. Sonsuz basamaklarla doğrudan işlem yapmak hem zor hem hataya açıktır.",
            ornek(
                "$0.\\overline{3}+0.\\overline{6}$ ve $0.\\overline{1}+0.\\overline{2}$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "Birinci: $\\dfrac{3}{9}+\\dfrac{6}{9}=\\dfrac{9}{9}=1$.",
                "İkinci: $\\dfrac{1}{9}+\\dfrac{2}{9}=\\dfrac{3}{9}=\\dfrac{1}{3}$."),
            ornek(
                "$0.1\\overline{6} \\cdot 6$ ve $0.\\overline{36}:0.\\overline{12}$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "Birinci: $0.1\\overline{6}=\\dfrac{1}{6}$; $\\dfrac{1}{6} \\cdot 6=1$.",
                "İkinci: $\\dfrac{36}{99}:\\dfrac{12}{99}=\\dfrac{36}{12}=3$."),
            hap("Devirli sayılarla işlem yapmadan önce hepsini kesre çevir.",
                "Aynı paydada kesirler çıkıyorsa ($9$, $99$ gibi) işlem çok kısalır."),
        ]},
        {"baslik": "Devirli sayıları sıralamak", "icerik": [
            "Devirli sayılar karşılaştırılırken devreden kısım birkaç kez açık yazılır ve basamaklar soldan sağa karşılaştırılır. Kesre çevirmek de her zaman güvenilir bir yoldur.",
            ornek(
                "$0.33$, $0.\\overline{3}$ ve $0.3\\overline{4}$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Açık yazalım: $0.3300\\ldots$, $0.3333\\ldots$, $0.3444\\ldots$",
                "Yüzde birler basamağında $3$, $3$, $4$; binde birlerde ilk ikisi $0$ ve $3$.",
                "Sıralama: $0.33<0.\\overline{3}<0.3\\overline{4}$."),
            dikkat(
                "$0.\\overline{3}$ ile $0.33$ aynı sayı değildir.",
                "$0.33$ sonludur ve $\\dfrac{33}{100}$ e eşittir; $0.\\overline{3}$ ise $\\dfrac{1}{3}$ dir. Aradaki fark $\\dfrac{1}{300}$ dir."),
        ]},
        {"baslik": "Paydayı dokuzlara tamamlamak", "icerik": [
            "Paydası $9$, $99$ ya da $999$ olan kesirler doğrudan devirli sayıya çevrilebilir, çünkü $\\dfrac{1}{9}=0.\\overline{1}$, $\\dfrac{1}{99}=0.\\overline{01}$ ve $\\dfrac{1}{999}=0.\\overline{001}$ dir. Pay, paydadaki dokuzların sayısı kadar basamakla yazılırsa devreden doğrudan pay olur: $\\dfrac{7}{9}=0.\\overline{7}$, $\\dfrac{23}{99}=0.\\overline{23}$ ve $\\dfrac{123}{999}=0.\\overline{123}$.",
            "Bu gözlem kuralın tersini de verir. Bir kesrin paydası uygun bir sayıyla genişletilerek $9$, $99$ ya da $999$ yapılabiliyorsa devreden hiç bölme yapmadan okunur.",
            ornek(
                "$\\dfrac{5}{11}$ ve $\\dfrac{2}{27}$ kesirleri verilsin.",
                "Paydaları dokuzlara tamamlayarak devirli sayıya çevirelim.",
                "$11 \\cdot 9=99$ olduğu için $\\dfrac{5}{11}=\\dfrac{45}{99}=0.\\overline{45}$.",
                "$27 \\cdot 37=999$ olduğu için $\\dfrac{2}{27}=\\dfrac{74}{999}=0.\\overline{074}$.",
                "İkinci sonuçta pay üç basamakla yazılmalıdır: devreden $74$ değil, $074$ olarak okunur."),
            dikkat(
                "Payı eksik basamakla yazmak.",
                "$\\dfrac{7}{99}=0.\\overline{07}$ dir. Bunu $0.\\overline{7}$ diye yazmak yanlıştır, çünkü $0.\\overline{7}=\\dfrac{7}{9}$ dir ve bu sayı $\\dfrac{7}{99}$ nin on bir katıdır."),
        ]},
        {"baslik": "Bilinmeyen rakamlı sorular", "icerik": [
            "Devreden kısmı harfle verilen sorularda kural aynen işler. Tek basamaklı bir $a$ rakamı için $0.\\overline{a}=\\dfrac{a}{9}$ olur. İki basamaklı devredende ise $ab$ iki basamaklı sayıyı gösterdiği için $0.\\overline{ab}=\\dfrac{10a+b}{99}$ yazılır.",
            ornek(
                "$a$ bir rakam ve $0.\\overline{a}+0.\\overline{3}=0.\\overline{8}$ olsun.",
                "$a$ rakamını bulalım.",
                "Kesre çevirelim: $\\dfrac{a}{9}+\\dfrac{3}{9}=\\dfrac{8}{9}$.",
                "Paydalar eşit olduğu için paylar da eşit olmalıdır: $a+3=8$, yani $a=5$.",
                "Kontrol: $0.\\overline{5}+0.\\overline{3}=\\dfrac{8}{9}=0.\\overline{8}$."),
            ornek(
                "$a$ ve $b$ sıfırdan farklı rakamlar ve $0.\\overline{ab}+0.\\overline{ba}=1$ olsun.",
                "$a+b$ toplamını bulalım.",
                "Kesre çevirelim: $0.\\overline{ab}=\\dfrac{10a+b}{99}$ ve $0.\\overline{ba}=\\dfrac{10b+a}{99}$.",
                "Toplam: $\\dfrac{11a+11b}{99}=\\dfrac{a+b}{9}$.",
                "Bu toplam $1$ e eşit olduğu için $a+b=9$.",
                "Örneğin $a=2$ ve $b=7$ için $0.\\overline{27}+0.\\overline{72}=\\dfrac{99}{99}=1$."),
            "Bu tür sorularda önce her devirli sayıyı harflerle kesre çevirmek, sonra paydaları eşitleyip payları karşılaştırmak yeterlidir. Harflerin rakam olduğunu, yani $0$ ile $9$ arasında tam sayı olduğunu unutmamak gerekir.",
        ]},
        {"baslik": "Devirli sayıları yuvarlamak", "icerik": [
            "Devirli bir sayı yuvarlanırken devreden kısım gerektiği kadar açık yazılır, sonra sıradan yuvarlama kuralı uygulanır: yuvarlanacak basamağın sağındaki rakam $5$ ya da daha büyükse basamak bir artırılır.",
            ornek(
                "$0.\\overline{6}$ ve $1.\\overline{27}$ sayıları verilsin.",
                "Birincisini yüzde birler, ikincisini onda birler basamağına yuvarlayalım.",
                "$0.\\overline{6}=0.666\\ldots$ Yüzde birler basamağı $6$, sağındaki rakam $6$; sonuç $0.67$.",
                "$1.\\overline{27}=1.2727\\ldots$ Onda birler basamağı $2$, sağındaki rakam $7$; sonuç $1.3$."),
            "Hesap makinesi bir devirli sayıyı ekrana sığdırabildiği kadar basamakla gösterir. Bu yüzden ekrandaki sonuç devirli sayının kendisi değil, yaklaşık bir değeridir. $\\dfrac{2}{3}$ nin tam değeri $0.\\overline{6}$ dır; ekranda görülen sonlu sayı bu değere yalnızca yakındır.",
            dikkat(
                "Yuvarlanmış değerle işleme devam etmek.",
                "$\\dfrac{1}{3}$ yerine $0.33$ alınıp $3$ ile çarpılırsa $0.99$ bulunur; oysa doğru sonuç $1$ dir. Ara adımlarda kesir ya da devirli gösterimi korumak ve yuvarlamayı en sona bırakmak gerekir."),
        ]},
        {"baslik": "Sonucu bölmeyle kontrol etmek", "icerik": [
            "Kuralla bulunan kesrin doğru olup olmadığını anlamanın en sağlam yolu, payı paydaya bölüp aynı devirli sayının çıktığını görmektir. Bölmede bir kalan yeniden ortaya çıktığı anda devir başlamış demektir; bu yüzden birkaç adım yeterlidir.",
            ornek(
                "Kuralla $1.2\\overline{34}=\\dfrac{611}{495}$ bulunmuştu.",
                "Bu sonucu uzun bölmeyle kontrol edelim.",
                "$611:495$ işleminde bölüm $1$, kalan $116$.",
                "$1160:495$ işleminde bölüm $2$, kalan $170$.",
                "$1700:495$ işleminde bölüm $3$, kalan $215$; $2150:495$ işleminde bölüm $4$, kalan yeniden $170$.",
                "Kalan $170$ tekrar ettiği için $3$ ve $4$ basamakları sonsuza kadar tekrar eder: $1.2343434\\ldots=1.2\\overline{34}$. Sonuç doğru."),
            "Kontrol sırasında devrin nereden başladığı da görülür: kalan $170$ ilk kez ikinci adımda ortaya çıktı ve ondan sonraki basamaklar tekrar etti. Devretmeyen $2$ basamağı ise tekrar eden kalanlardan önce geldiği için çizginin dışında kalır.",
        ]},
        {"baslik": "Sınavda devirli ondalık sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu devirli sayıyı kesre çevirme, devirli sayılarla işlem, sıralama ve devirdeki belirli bir basamağı bulma biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde devirli sayılar, işlem sorularında kesre çevrilerek sadeleştirilecek ifadeler olarak da gerekebilir."),
            "Devirli sayı içeren bir işlemle karşılaştığında ilk adım, her devirli sayıyı kuralla kesre çevirmektir. Bu adımdan sonra soru, sıradan bir kesir işlemine dönüşür. Kesrin rasyonel sayılarla bağlantısı için <a href=\"/blog/rasyonel-sayilar-konu-anlatimi-pdf/\">Rasyonel Sayılar Konu Anlatımı PDF</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Paydaya tam kısım için sıfır eklemek", "Yalnız devretmeyen ondalık basamaklar"],
                ["Payda devretmeyen kısmı çıkarmamak", "Tamamı eksi devretmeyen"],
                ["$0.\\overline{9}<1$ sanmak", "$0.\\overline{9}=1$"],
                ["$0.\\overline{3}=0.33$ yazmak", "$0.\\overline{3}=\\dfrac{1}{3}$"],
                ["Sadeleştirmeden devirli demek", "Önce en sade hâle getir"],
                ["Devirli sayılarla doğrudan işlem", "Önce kesre çevir"],
            ]),
            "Bu hataların çoğu, kuralı nereden geldiğini bilmeden uygulamaktan doğar. Emin olmadığında sayıyı $x$ olarak adlandırıp onun kuvvetleriyle çarpma yöntemini kullanmak her zaman doğru sonucu verir.",
        ]},
    ],
    "sss": [
        ("Devirli ondalık sayı nedir?",
         "Virgülden sonraki bir rakam ya da rakam grubunun sonsuza kadar aynı sırayla tekrar ettiği ondalık sayıdır. Tekrar eden kısmın üzerine çizgi çekilir."),
        ("Devirli ondalık sayı kesre nasıl çevrilir?",
         "Pay, sayının virgülsüz tamamından devretmeyen kısmın çıkarılmasıyla bulunur. Payda, devreden basamak sayısı kadar 9 ve virgülden sonraki devretmeyen basamak sayısı kadar 0 yazılarak bulunur."),
        ("0,999 devirli neden 1 e eşittir?",
         "Kural uygulandığında dokuzda dokuz, yani 1 bulunur. Ayrıca üçte birin üç katı hem 1 hem de 0,999 devirli olduğu için ikisi aynı sayıdır."),
        ("Hangi kesirler devirli ondalık sayı verir?",
         "En sade hâldeki kesrin paydasında 2 ve 5 ten başka asal çarpan varsa ondalık gösterim devirlidir. Paydada yalnız 2 ve 5 varsa gösterim sonludur."),
        ("Devrin uzunluğu en fazla kaç olabilir?",
         "Paydası q olan bir kesirde devreden en fazla q eksi 1 basamaklı olabilir. Örneğin yedide birde devir 6 basamaklıdır."),
        ("Devirli sayılar rasyonel midir?",
         "Evet. Her devirli ondalık sayı iki tam sayının oranı olarak yazılabildiği için rasyoneldir."),
        ("Devirli sayı nasıl yuvarlanır?",
         "Devreden kısım birkaç kez açık yazılır. Sonra yuvarlanacak basamağın sağındaki rakama bakılarak sıradan yuvarlama kuralı uygulanır."),
        ("Paydası 99 olan kesir nasıl devirli yazılır?",
         "Pay iki basamakla yazılır ve devreden olarak alınır. Örneğin doksan dokuzda yedi, devredeni 07 olan sayıdır; doksan dokuzda yirmi üç ise devredeni 23 olan sayıdır."),
        ("Kuralla bulduğum kesri nasıl kontrol ederim?",
         "Payı paydaya uzun bölmeyle böl. Bir kalan yeniden ortaya çıktığında devir başlamıştır. Elde edilen basamaklar başlangıçtaki devirli sayıyla aynıysa bulduğun kesir doğrudur; farklıysa pay ya da paydada bir basamak hatası vardır."),
        ("Devirli sayılar hesap makinesinde neden farklı görünür?",
         "Hesap makinesi yalnızca ekrana sığan kadar basamak gösterir ve sonuncuyu yuvarlayabilir. Bu yüzden ekrandaki değer devirli sayının kendisi değil, ona yakın bir sonlu sayıdır."),
    ],
    "kontrol": [
        "Devreden ve devretmeyen kısmı ayırt edip doğru gösterebiliyorum.",
        "Devrin neden oluştuğunu uzun bölmedeki kalanlarla açıklayabiliyorum.",
        "Bir kesrin sonlu mu devirli mi olduğunu paydasından anlayabiliyorum.",
        "Devirli sayıyı kuralla kesre çevirebiliyorum.",
        "Paydadaki dokuzların ve sıfırların nereden geldiğini açıklayabiliyorum.",
        "Kuralın doğruluğunu onun kuvvetleriyle çarparak gösterebiliyorum.",
        "$0.\\overline{9}=1$ eşitliğini açıklayabiliyorum.",
        "Devirdeki belirli bir basamağı kalan yardımıyla bulabiliyorum.",
        "Devirli sayılarla işlemi kesre çevirerek yapabiliyorum.",
        "Devirli ve sonlu ondalık sayıları sıralayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["ondalik-gosterim-konu-anlatimi-pdf", "rasyonel-sayilar-konu-anlatimi-pdf", "kesirler-konu-anlatimi-pdf"],
}
