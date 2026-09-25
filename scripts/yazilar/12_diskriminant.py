# scripts/yazilar/12_diskriminant.py — Diskriminant (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "diskriminant-delta",
    "baslik": "Diskriminant Nedir? Delta Nasıl Hesaplanır?",
    "aciklama": "Diskriminant nedir, delta nasıl hesaplanır? Kök sayısı, çakışık kök, rasyonel kök, parametreli sorular, grafik yorumu ve her x için pozitiflik koşulu; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "diskriminant-delta",
    "kapak_alt": "Diskriminant: yatay çizgiyi iki kez kesen, bir kez değen ve hiç kesmeyen üç parabol panelini inceleyen iki öğrenci",
    "ozet": "Diskriminant, ikinci dereceden bir denklemin köklerini bulmadan kaç gerçek kökü olduğunu söyleyen sayıdır. Tek bir hesapla denklemin iki farklı kökü mü, tek kökü mü olduğu ya da hiç gerçek kökü olmadığı anlaşılır. Bu yazıda diskriminantın tanımını ve hesabını, üç durumun anlamını, grafik yorumunu, köklerin rasyonel olup olmadığını, parametreli soruları, kökler arasındaki farkı, tam kare koşulunu ve bir ifadenin her zaman pozitif olma koşulunu çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Diskriminant nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için ikinci dereceden denklemleri ve kök formülünü biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/ikinci-dereceden-denklemler/\">İkinci Dereceden Denklemler Konu Anlatımı</a> yazısına göz at."),
            "$ax^2+bx+c=0$ denkleminde $b^2-4ac$ sayısına <strong>diskriminant</strong> denir ve Yunan harfi delta ile, yani $\\Delta$ ile gösterilir. Kelime, Latince ayırt etmek anlamındaki bir kökten gelir: diskriminant, denklemin hangi durumda olduğunu ayırt eder.",
            "$$\\Delta=b^2-4ac$$",
            "Kök formülünde diskriminant karekökün içinde yer alır: $x=\\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$. Karekökün içindeki sayının işareti, formülün iki mi, bir mi yoksa hiç gerçek sonuç mu vereceğini belirler.",
            hap("$\\Delta=b^2-4ac$",
                "Diskriminantın işareti gerçek kök sayısını belirler."),
        ]},
        {"baslik": "Diskriminant nasıl hesaplanır?", "icerik": [
            "Hesaba başlamadan önce denklem $ax^2+bx+c=0$ biçimine getirilir ve katsayılar işaretleriyle birlikte okunur. Sonra $b$ nin karesinden $4ac$ çıkarılır.",
            tablo(["Denklem", "$a$, $b$, $c$", "$\\Delta$"], [
                ["$x^2-5x+6=0$", "$1$, $-5$, $6$", "$25-24=1$"],
                ["$x^2-4x+4=0$", "$1$, $-4$, $4$", "$16-16=0$"],
                ["$x^2+x+1=0$", "$1$, $1$, $1$", "$1-4=-3$"],
                ["$2x^2+3x-2=0$", "$2$, $3$, $-2$", "$9+16=25$"],
            ]),
            dikkat(
                "$b$ negatifken karesini negatif almak.",
                "$b=-5$ ise $b^2=25$ tir, $-25$ değil. Kare her zaman negatif olmayan bir sayı verir; bu yüzden $b^2$ yazarken katsayıyı parantez içinde almak işaret hatasını önler."),
            "Hesaptan sonra kısa bir akıl kontrolü de yapılabilir: $a$ ile $c$ ters işaretliyse diskriminant mutlaka pozitif çıkmalıdır. Bu kontrol, işaret hatalarının büyük bölümünü hemen yakalar.",
        ]},
        {"baslik": "Δ > 0: iki farklı gerçek kök", "icerik": [
            "Diskriminant pozitifse kök formülündeki karekök pozitif bir sayıdır; artı ve eksi işaretleri iki farklı sonuç verir. Denklemin iki farklı gerçek kökü vardır.",
            ornek(
                "$x^2-5x+6=0$ denklemi verilsin.",
                "Diskriminantı bulup kökleri hesaplayalım.",
                "$\\Delta=25-24=1>0$; iki farklı kök vardır.",
                "$x=\\dfrac{5 \\pm 1}{2}$; kökler $3$ ve $2$ dir."),
        ]},
        {"baslik": "Diskriminantla kökleri bulmak", "icerik": [
            "Diskriminant yalnızca kök sayısını söylemez; hesaplandıktan sonra kök formülüne yerleştirilerek kökleri de verir. Diskriminantı önce ayrı hesaplamak, formülün karekök kısmını sadeleştirir ve işlem hatalarını azaltır.",
            ornek(
                "$2x^2+3x-2=0$ denklemi verilsin.",
                "Diskriminantı bulup kökleri hesaplayalım.",
                "$\\Delta=9+16=25$ ve $\\sqrt{\\Delta}=5$.",
                "$x=\\dfrac{-3 \\pm 5}{4}$; kökler $\\dfrac{1}{2}$ ve $-2$ dir."),
            "Diskriminant bir tam kare çıktığı için kökler rasyoneldir ve denklem aslında $(2x-1)(x+2)=0$ biçiminde çarpanlarına da ayrılabilirdi. Diskriminantın tam kare olması, çarpanlara ayırmanın mümkün olduğunun bir işaretidir.",
        ]},
        {"baslik": "Δ = 0: çakışık kök", "icerik": [
            "Diskriminant sıfırsa karekök sıfırdır ve artı ile eksi aynı sonucu verir. Denklemin iki eşit kökü vardır; bu köke <strong>çakışık kök</strong> ya da çift kat kök denir ve değeri $-\\dfrac{b}{2a}$ dir.",
            ornek(
                "$x^2-4x+4=0$ denklemi verilsin.",
                "Diskriminantı bulup kökü hesaplayalım.",
                "$\\Delta=16-16=0$; çakışık kök vardır.",
                "$x=\\dfrac{4}{2}=2$. Gerçekten $x^2-4x+4=(x-2)^2$ dir."),
            "Diskriminantın sıfır olması, ifadenin bir tam kare olması demektir. Bu yüzden diskriminant, bir ifadenin tam kare olup olmadığını anlamanın da en hızlı yoludur.",
        ]},
        {"baslik": "Δ < 0: gerçek kök yok", "icerik": [
            "Diskriminant negatifse karekök gerçek sayılarda alınamaz ve denklemin gerçek kökü yoktur. Çözüm kümesi gerçek sayılarda boş kümedir. Bu, denklemin hiç çözümü olmadığı anlamına gelmez; ileride karmaşık sayılarla bu denklemlerin de kökleri bulunur, ama gerçek sayılar içinde kök yoktur.",
            ornek(
                "$x^2+x+1=0$ denklemi verilsin.",
                "Denklemin gerçek kökü olup olmadığını inceleyelim.",
                "$\\Delta=1-4=-3<0$.",
                "Gerçek kök yoktur; çözüm kümesi boştur."),
            dikkat(
                "Diskriminant negatifken kök formülüne devam etmek.",
                "$\\sqrt{-3}$ gerçek bir sayı değildir. Diskriminant negatif çıktığında hesap orada durur; bulunacak gerçek bir kök yoktur."),
        ]},
        {"baslik": "Üç durumun özeti", "icerik": [
            "Diskriminantın üç durumu, hem cebirsel hem grafik anlamıyla birlikte aşağıdaki tabloda özetlenmiştir.",
            tablo(["Durum", "Kökler", "Parabol ve x ekseni"], [
                ["$\\Delta>0$", "İki farklı gerçek kök", "İki noktada keser"],
                ["$\\Delta=0$", "Çakışık kök", "Bir noktada teğet"],
                ["$\\Delta<0$", "Gerçek kök yok", "Kesmez"],
            ]),
        ]},
        {"baslik": "Grafik yorumu", "icerik": [
            "$ax^2+bx+c=0$ denkleminin kökleri, $y=ax^2+bx+c$ parabolünün $x$ eksenini kestiği noktalardır. Diskriminant bu yüzden parabolün $x$ ekseniyle ilişkisini de söyler. Kapaktaki üç panel bu üç durumu yan yana gösterir.",
            koordinat_grafik("Aynı biçimli üç parabol: Δ = 16, Δ = 0 ve Δ = −8",
                             [("y = x² − 2x − 3 (Δ = 16)", lambda x: x * x - 2 * x - 3), ("y = x² − 2x + 1 (Δ = 0)", lambda x: x * x - 2 * x + 1),
                              ("y = x² − 2x + 3 (Δ = −8)", lambda x: x * x - 2 * x + 3)],
                             (-3, 5), (-5, 7), noktalar=[(-1, 0, "", True), (3, 0, "", True), (1, 0, "", True)]),
            "Üç parabolün biçimi aynıdır; yalnızca yükseklikleri farklıdır. En alçaktaki ekseni iki noktada keser, ortadaki eksene tek noktada değer, en yüksekteki ekseni hiç kesmez. Sabit terim büyüdükçe parabol yukarı kayar ve diskriminant küçülür.",
        ]},
        {"baslik": "Köklerin rasyonel olup olmadığı", "icerik": [
            "Katsayılar tam sayıysa ve diskriminant bir tam kare sayıysa karekök tam sayı çıkar ve kökler rasyoneldir. Diskriminant pozitif ama tam kare değilse kökler irrasyoneldir.",
            ornek(
                "$x^2-x-6=0$ ve $x^2-4x+1=0$ denklemleri verilsin.",
                "Köklerin rasyonel olup olmadığını inceleyelim.",
                "$x^2-x-6=0$ için $\\Delta=1+24=25=5^2$; kökler rasyoneldir: $3$ ve $-2$.",
                "$x^2-4x+1=0$ için $\\Delta=16-4=12$; tam kare değildir, kökler $2 \\pm \\sqrt{3}$ irrasyoneldir."),
            "Bu gözlem, çarpanlara ayırmaya ne zaman güvenileceğini de gösterir: diskriminant tam kare değilse denklem tam sayılarla çarpanlarına ayrılamaz ve kök formülüne geçmek gerekir.",
        ]},
        {"baslik": "İki farklı kök için parametre", "icerik": [
            "Denklemde bir parametre varsa kök sayısıyla ilgili koşul diskriminant üzerinden bir eşitsizliğe dönüşür. İki farklı gerçek kök için $\\Delta>0$ yazılır ve parametre bulunur.",
            ornek(
                "$x^2-4x+m=0$ denkleminin iki farklı gerçek kökü vardır.",
                "$m$ nin alabileceği değerleri bulalım.",
                "$\\Delta=16-4m>0$.",
                "$m<4$."),
        ]},
        {"baslik": "Çakışık kök için parametre", "icerik": [
            "Çakışık kök koşulu $\\Delta=0$ bir denklem verir. Parametrenin karesi geçiyorsa çoğu zaman iki değer bulunur ve ikisi de koşulu sağlar.",
            ornek(
                "$x^2+mx+9=0$ denkleminin çakışık kökü vardır.",
                "$m$ yi ve çakışık kökü bulalım.",
                "$\\Delta=m^2-36=0$, yani $m=6$ ya da $m=-6$.",
                "$m=6$ için kök $-3$, $m=-6$ için kök $3$ tür."),
        ]},
        {"baslik": "Parametrenin tam sayı değerleri", "icerik": [
            "Parametre sorularında bazen yalnızca belirli türden değerler istenir: pozitif tam sayılar, doğal sayılar ya da belirli bir aralıktaki tam sayılar. Önce diskriminant koşulu çözülür, sonra istenen türdeki değerler sayılır.",
            ornek(
                "$x^2-2x+m-3=0$ denkleminin iki farklı gerçek kökü vardır.",
                "$m$ nin alabileceği pozitif tam sayı değerlerinin sayısını bulalım.",
                "$\\Delta=4-4(m-3)=16-4m>0$, yani $m<4$.",
                "Pozitif tam sayı değerleri $1$, $2$ ve $3$ tür; $3$ değer vardır."),
        ]},
        {"baslik": "Kök olmaması için parametre", "icerik": [
            "Denklemin gerçek kökü olmaması için $\\Delta<0$ yazılır. Bu koşul, parabolün $x$ eksenini hiç kesmemesi demektir.",
            ornek(
                "$x^2+2x+m=0$ denkleminin gerçek kökü yoktur.",
                "$m$ nin alabileceği değerleri bulalım.",
                "$\\Delta=4-4m<0$.",
                "$m>1$."),
        ]},
        {"baslik": "Parametreye göre bütün durumlar", "icerik": [
            "Tek bir parametreli denklemde üç durumun hepsi birlikte incelenebilir. Diskriminant parametreye bağlı bir ifade olarak yazılır ve işaretinin değiştiği değer bulunur; bu değer, iki kök ile kökün olmadığı durumları ayıran sınırdır.",
            tablo(["$x^2-4x+m=0$ için", "$\\Delta=16-4m$", "Sonuç"], [
                ["$m<4$", "Pozitif", "İki farklı gerçek kök"],
                ["$m=4$", "Sıfır", "Çakışık kök: $2$"],
                ["$m>4$", "Negatif", "Gerçek kök yok"],
            ]),
            "Tablo, parabolün yukarı kaydıkça ekseni önce iki noktada kestiğini, sonra teğet olduğunu, en sonunda da hiç kesmediğini sayılarla gösterir. $m$ burada sabit terimdir ve parabolün yüksekliğini belirler.",
        ]},
        {"baslik": "Baş katsayıda parametre", "icerik": [
            "Parametre $x^2$ nin katsayısındaysa önce denklemin gerçekten ikinci dereceden olması, yani baş katsayının sıfırdan farklı olması gerekir. Bu koşul unutulursa yanlış bir değer cevaba karışır.",
            ornek(
                "$mx^2+4x+1=0$ denkleminin iki farklı gerçek kökü vardır.",
                "$m$ nin alabileceği değerleri bulalım.",
                "İkinci dereceden olması için $m \\neq 0$.",
                "$\\Delta=16-4m>0$, yani $m<4$. Sonuç: $m<4$ ve $m \\neq 0$."),
            dikkat(
                "$m=0$ durumunu elememek.",
                "$m=0$ için denklem $4x+1=0$ olur; birinci dereceden bu denklemin tek kökü vardır. İki farklı kök istendiği için $m=0$ cevaptan çıkarılmalıdır."),
        ]},
        {"baslik": "a ile c ters işaretliyse", "icerik": [
            "$a$ ile $c$ ters işaretliyse $ac$ negatiftir ve $-4ac$ pozitif olur. $b^2$ de negatif olmadığı için diskriminant kesinlikle pozitiftir; denklemin her zaman iki farklı gerçek kökü vardır.",
            ornek(
                "$3x^2+7x-2=0$ denklemi verilsin.",
                "Kök sayısını hesap yapmadan belirleyelim.",
                "$a=3$ ve $c=-2$ ters işaretlidir; $ac<0$.",
                "Diskriminant pozitiftir: $49+24=73$. İki farklı gerçek kök vardır."),
        ]},
        {"baslik": "Her zaman kökü olan denklem", "icerik": [
            "Parametreli bir denklemin diskriminantı parametre ne olursa olsun pozitif çıkabilir. Bunu göstermek için diskriminant bir kare artı pozitif bir sayı biçimine getirilir.",
            ornek(
                "$x^2+(m+2)x+m=0$ denklemi verilsin.",
                "Her $m$ için iki farklı gerçek kökü olduğunu gösterelim.",
                "$\\Delta=(m+2)^2-4m=m^2+4m+4-4m=m^2+4$.",
                "$m^2 \\geq 0$ olduğu için $\\Delta \\geq 4>0$ dır; denklemin her zaman iki farklı gerçek kökü vardır."),
        ]},
        {"baslik": "b çiftken kısa diskriminant", "icerik": [
            "$b=2b'$ yazılabiliyorsa $\\Delta=4(b'^2-ac)$ olur. Bu durumda işaret incelemesi için $\\Delta'=b'^2-ac$ hesaplamak yeterlidir; $\\Delta$ ile aynı işarete sahiptir ama daha küçük sayılarla çalışır.",
            ornek(
                "$x^2-6x+5=0$ denklemi verilsin.",
                "Kısa diskriminantla kök sayısını bulalım.",
                "$b=-6$ olduğu için $b'=-3$ tür. $\\Delta'=9-5=4>0$.",
                "İki farklı kök vardır. Tam diskriminant $\\Delta=4 \\cdot 4=16$ dır."),
        ]},
        {"baslik": "Diskriminant ve tepe noktası", "icerik": [
            "Diskriminant, parabolün tepe noktasının yüksekliğiyle de bağlantılıdır. $y=ax^2+bx+c$ parabolünün tepe noktasının ikinci koordinatı $-\\dfrac{\\Delta}{4a}$ dır. Bu bağlantı, diskriminantın grafik anlamını sayılarla gösterir.",
            ornek(
                "$y=x^2-2x-3$ parabolü verilsin.",
                "Tepe noktasının ikinci koordinatını diskriminanttan bulalım.",
                "$\\Delta=4+12=16$.",
                "Tepe noktasının ikinci koordinatı $-\\dfrac{16}{4}=-4$ tür. Tepe noktası $(1, -4)$ tür."),
            "$a>0$ iken diskriminant pozitifse tepe noktası eksenin altındadır ve parabol ekseni keser; diskriminant negatifse tepe noktası eksenin üstündedir ve parabol ekseni kesmez. Tepe noktasının ayrıntısı <a href=\"/blog/parabol-tepe-noktasi/\">Parabolün Tepe Noktası Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Diskriminant yetmediğinde", "icerik": [
            "Diskriminant köklerin sayısını söyler ama işaretlerini söylemez. Köklerin pozitif mi negatif mi olduğunu anlamak için kökler toplamı ve çarpımı da gerekir: çarpım pozitifse kökler aynı işaretlidir, toplamın işareti de bu ortak işareti verir.",
            ornek(
                "$x^2-5x+6=0$ denklemi verilsin.",
                "Köklerin işaretini kökleri bulmadan belirleyelim.",
                "$\\Delta=1>0$; iki farklı gerçek kök vardır.",
                "Çarpım $6>0$, toplam $5>0$; iki kök de pozitiftir. Gerçekten kökler $2$ ve $3$ tür."),
            "Ayrıntısı <a href=\"/blog/kokler-toplami-carpimi/\">Kökler Toplamı ve Kökler Çarpımı Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Kökler arasındaki fark", "icerik": [
            "Kök formülündeki iki kök yalnızca $\\pm\\sqrt{\\Delta}$ kısmında ayrılır. Bu yüzden iki kök arasındaki uzaklık diskriminanttan doğrudan bulunur:",
            "$$|x_1-x_2|=\\dfrac{\\sqrt{\\Delta}}{|a|}$$",
            ornek(
                "$x^2-5x+6=0$ ve $2x^2+3x-2=0$ denklemleri verilsin.",
                "Kökler arasındaki farkı bulalım.",
                "Birinci denklem: $\\dfrac{\\sqrt{1}}{1}=1$. Kökler $2$ ve $3$ olduğu için doğrudur.",
                "İkinci denklem: $\\dfrac{\\sqrt{25}}{2}=\\dfrac{5}{2}$. Kökler $\\dfrac{1}{2}$ ve $-2$ dir; fark gerçekten $\\dfrac{5}{2}$ tir."),
        ]},
        {"baslik": "Tam kare olma koşulu", "icerik": [
            "Bir üç terimlinin bir tam kare olması, karşılık gelen denklemin çakışık köklü olması demektir. Bu yüzden tam kare koşulu $\\Delta=0$ ile bulunur.",
            ornek(
                "$4x^2+mx+9$ ifadesi bir tam karedir.",
                "$m$ yi bulalım.",
                "$\\Delta=m^2-4 \\cdot 4 \\cdot 9=m^2-144=0$.",
                "$m=12$ ya da $m=-12$. Gerçekten $(2x+3)^2=4x^2+12x+9$ ve $(2x-3)^2=4x^2-12x+9$ dur."),
        ]},
        {"baslik": "Her x için pozitif olma koşulu", "icerik": [
            "$ax^2+bx+c$ ifadesinin her gerçek $x$ için pozitif olması, parabolün tamamen $x$ ekseninin üstünde kalması demektir. Bunun için parabolün kolları yukarı bakmalı ve ekseni hiç kesmemelidir: $a>0$ ve $\\Delta<0$.",
            ornek(
                "$x^2+mx+4$ ifadesi her gerçek $x$ için pozitiftir.",
                "$m$ nin alabileceği değerleri bulalım.",
                "$a=1>0$ koşulu sağlanır. $\\Delta=m^2-16<0$ olmalıdır.",
                "$-4<m<4$."),
            "Her $x$ için negatif olma koşulu ise bunun tersidir: kollar aşağı bakmalı ve parabol ekseni kesmemelidir, yani $a<0$ ve $\\Delta<0$.",
        ]},
        {"baslik": "Eşitsizliklerle bağlantı", "icerik": [
            "Diskriminant, ikinci dereceden eşitsizliklerin çözümünde de ilk bakılacak şeydir. Kökler varsa ifade kökler arasında bir işaret, dışında ters işaret alır. Kök yoksa ifade her yerde baş katsayının işaretini taşır.",
            ornek(
                "$x^2-4x+3<0$ ve $x^2+x+1<0$ eşitsizlikleri verilsin.",
                "Çözüm kümelerini bulalım.",
                "Birinci için $\\Delta=4>0$, kökler $1$ ve $3$ tür; ifade kökler arasında negatiftir: çözüm $(1, 3)$ aralığıdır.",
                "İkinci için $\\Delta=-3<0$ ve $a=1>0$; ifade her yerde pozitiftir, bu yüzden çözüm kümesi boştur."),
            "Eşitsizliklerin ayrıntısı <a href=\"/blog/esitsizlikler-konu-anlatimi-pdf/\">Eşitsizlikler Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Parabol ile doğrunun kesişimi", "icerik": [
            "Bir parabol ile bir doğrunun kaç noktada kesiştiği de diskriminantla bulunur: iki denklem eşitlenir, ortaya çıkan ikinci dereceden denklemin diskriminantına bakılır.",
            ornek(
                "$y=x^2$ parabolü ile $y=2x+k$ doğrusu verilsin.",
                "Doğrunun parabole teğet olması için $k$ yı bulalım.",
                "$x^2=2x+k$, yani $x^2-2x-k=0$. $\\Delta=4+4k$.",
                "Teğetlik için $\\Delta=0$: $k=-1$. Teğet noktası $x=1$, $y=1$ dir."),
            "Ayrıntısı <a href=\"/blog/parabol-ve-dogru/\">Parabol ve Doğrunun Birbirine Göre Durumları</a> yazısında.",
        ]},
        {"baslik": "Sınavda diskriminant", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) diskriminant kök sayısını bulma ve basit parametre soruları biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) çakışık kök, her $x$ için pozitiflik, parabol ile doğrunun kesişimi ve baş katsayıda parametre bulunan sorular da sorulabilir."),
            "Diskriminant sorusunda önce koşulun hangi eşitsizliğe karşılık geldiğini yaz: iki farklı kök için büyüktür, çakışık kök için eşittir, kök olmaması için küçüktür. Parametre baş katsayıdaysa baş katsayının sıfır olmaması koşulunu da eklemeyi unutma.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$b^2$ yi negatif almak", "$b^2$ her zaman negatif değildir"],
                ["Standart biçime getirmeden katsayı okumak", "Önce her şey bir tarafa toplanır"],
                ["Baş katsayı parametreliyken $a \\neq 0$ ı unutmak", "Baş katsayı sıfır olamaz"],
                ["$\\Delta<0$ iken kök formülüne devam etmek", "Gerçek kök yoktur"],
                ["$\\Delta=0$ ı kök yok sanmak", "Çakışık tek kök vardır"],
                ["Her $x$ için pozitiflikte $a>0$ ı unutmak", "$a>0$ ve $\\Delta<0$ birlikte"],
            ]),
            "Bu hataların çoğu, koşulları tek tek yazmadan doğrudan hesaba girişmekten doğar. Önce hangi koşulların gerektiğini alt alta yazmak, özellikle parametreli sorularda cevaba yanlış bir değerin karışmasını önler.",
        ]},
    ],
    "sss": [
        ("Diskriminant nedir?",
         "ax kare artı bx artı c eşittir sıfır denkleminde b kare eksi 4ac sayısıdır. Delta ile gösterilir ve denklemin gerçek kök sayısını belirler."),
        ("Delta sıfırsa ne olur?",
         "Denklemin iki eşit kökü, yani çakışık bir kökü vardır. Bu kök eksi b bölü 2a dır ve ifade bir tam karedir."),
        ("Delta negatifse ne olur?",
         "Denklemin gerçek kökü yoktur. Parabol x eksenini hiç kesmez."),
        ("Köklerin rasyonel olduğu nasıl anlaşılır?",
         "Katsayılar tam sayıysa ve diskriminant bir tam kareyse kökler rasyoneldir. Tam kare değilse kökler irrasyoneldir."),
        ("Bir ifade her x için ne zaman pozitiftir?",
         "Baş katsayı pozitif ve diskriminant negatifse ifade her gerçek x için pozitiftir. Parabol tamamen x ekseninin üstünde kalır."),
        ("Kökler arasındaki fark nasıl bulunur?",
         "Diskriminantın karekökü baş katsayının mutlak değerine bölünür. Kökler 2 ve 3 olan denklemde bu fark 1 dir."),
        ("Baş katsayı parametreliyse neye dikkat edilir?",
         "Denklemin ikinci dereceden kalması için baş katsayının sıfırdan farklı olması gerekir. Bu koşul diskriminant koşuluyla birlikte yazılır."),
    ],
    "kontrol": [
        "Diskriminantı katsayılardan hesaplayabiliyorum.",
        "Diskriminantın işaretinden kök sayısını söyleyebiliyorum.",
        "Çakışık kökü bulabiliyorum.",
        "Diskriminantı parabolün x ekseniyle ilişkisi olarak yorumlayabiliyorum.",
        "Köklerin rasyonel olup olmadığını belirleyebiliyorum.",
        "Kök sayısı koşulundan parametre bulabiliyorum.",
        "Baş katsayıda parametre olduğunda a ≠ 0 koşulunu ekleyebiliyorum.",
        "Kısa diskriminantı kullanabiliyorum.",
        "Tam kare koşulunu diskriminantla kurabiliyorum.",
        "Her x için pozitiflik koşulunu yazabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["ikinci-dereceden-denklemler", "kokler-toplami-carpimi", "parabol-ve-dogru"],
}
