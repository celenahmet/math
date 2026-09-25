# scripts/yazilar/39_turev_alma_kurallari.py — Turev Alma Kurallari (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "turev-alma-kurallari",
    "baslik": "Türev Alma Kuralları",
    "aciklama": "Türev alma kuralları nelerdir? Sabit, kuvvet, toplam, çarpım, bölüm ve zincir kuralı; trigonometrik, üstel ve logaritmik türevler, ikinci türev; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "turev-alma-kurallari",
    "kapak_alt": "Türev alma kuralları: yan yana dizilmiş farklı eğri ve dişli mekanizmalarını karşılaştıran iki öğrenci",
    "ozet": "Türev alma kuralları, türevi her seferinde limitle hesaplamadan bulmayı sağlayan hazır sonuçlardır. Sabit, kuvvet, toplam ve sabitle çarpım kurallarıyla polinomların, çarpım, bölüm ve zincir kurallarıyla daha karmaşık fonksiyonların türevi alınır. Bu yazıda temel kuralları, kök ve kesirleri üslü biçime çevirerek türev almayı, açarak ve terimlere ayırarak sadeleştirmeyi, çarpım, bölüm ve zincir kurallarının özetini, trigonometrik, üstel ve logaritmik fonksiyonların türevlerini, parçalı ve mutlak değerli fonksiyonları, ikinci ve daha yüksek mertebeden türevleri ve kural seçimini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kurallar neden gerekli?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için türevin tanımını ve üslü sayıları biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> ve <a href=\"/blog/turev-konu-anlatimi/\">Türev Konu Anlatımı</a> yazılarına göz at."),
            "Türevin tanımı her fonksiyon için geçerlidir, ama her seferinde limit hesaplamak uzun ve hataya açıktır. Tanım bir kez genel olarak uygulanır ve sonuçlar kurallar hâline getirilir. Böylece $x^7$ ya da $\\sin x \\cdot e^x$ gibi fonksiyonların türevi birkaç satırda bulunur.",
            "Kapaktaki öğrenciler yan yana dizilmiş farklı mekanizmaları inceliyor: tek bir eğri, iki eğrinin birleşimi, kesişen iki kol ve birbirini döndüren dişliler. Her mekanizma ayrı bir türev kuralına karşılık geliyor: tek fonksiyon, toplam, çarpım ve bileşke.",
        ]},
        {"baslik": "Sabit kuralı", "icerik": [
            "Sabit bir fonksiyonun grafiği yatay bir doğrudur ve eğimi her yerde sıfırdır. Değer hiç değişmediği için değişim hızı da yoktur. Bu yüzden sabitin türevi sıfırdır:",
            "$$(c)'=0$$",
            "Örneğin $f(x)=7$, $g(x)=-3$ ve $h(x)=\\pi$ fonksiyonlarının türevleri sıfırdır. $\\pi$ ya da $e$ gibi sayılar da sabittir; içlerinde harf görünmesi onları değişken yapmaz.",
        ]},
        {"baslik": "Kuvvet kuralı", "icerik": [
            "Kuvvet kuralı en sık kullanılan türev kuralıdır. Üs katsayı olarak öne alınır ve üs bir azaltılır. Kural, türevin tanımında $(x+h)^n$ açılımından gelir ve yalnızca değişkenin tabanda olduğu durumlarda geçerlidir:",
            "$$(x^n)'=n x^{n-1}$$",
            ornek(
                "$f(x)=x^7$, $g(x)=x^{-3}$ ve $h(x)=x^{3/4}$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$f'(x)=7x^6$ ve $g'(x)=-3x^{-4}$ olur.",
                "$h'(x)=\\dfrac{3}{4}x^{-1/4}$ olur; kural her gerçek üs için geçerlidir."),
        ]},
        {"baslik": "Sabitle çarpım kuralı", "icerik": [
            "Bir fonksiyon sabit bir sayıyla çarpılmışsa sabit türevin dışında kalır ve sonuç aynı sabitle çarpılır. Grafik dikey yönde uzadığında eğimler de aynı oranda büyür:",
            "$$(c \\cdot f(x))'=c \\cdot f'(x)$$",
            "Örneğin $5x^3$ ün türevi $5 \\cdot 3x^2=15x^2$ dir. Sabit toplama değil çarpma olarak bulunduğu için kaybolmaz; toplamda bulunan bir sabit ise sabit kuralı gereği türevde sıfır olur.",
        ]},
        {"baslik": "Toplam ve fark kuralı", "icerik": [
            "Toplamın ya da farkın türevi, terimlerin türevlerinin toplamı ya da farkıdır. Bu kural sayesinde uzun ifadelerin türevi terim terim alınır:",
            "$$(f \\pm g)'=f' \\pm g'$$",
            ornek(
                "$f(x)=4x^3-2x^2+5x-9$ fonksiyonu verilsin.",
                "Türevini ve $f'(1)$ değerini bulalım.",
                "Terim terim: $f'(x)=12x^2-4x+5$ olur.",
                "$f'(1)=12-4+5=13$ bulunur."),
        ]},
        {"baslik": "Kuralların kaynağı", "icerik": [
            "Toplam ve sabitle çarpım kuralları doğrudan türevin tanımından çıkar. $f+g$ için tanımdaki fark $\\left(f(x+h)-f(x)\\right)+\\left(g(x+h)-g(x)\\right)$ biçiminde iki parçaya ayrılır; $h$ ye bölünüp limit alınınca iki türevin toplamı kalır.",
            "Sabitle çarpımda ise $c$ bütün farkın ortak çarpanıdır ve limitin dışına çıkar. Limit kuralları türev kurallarına bu şekilde taşınır; bu yüzden türevin toplam ve sabit çarpan üzerinde doğrusal davrandığı söylenir.",
        ]},
        {"baslik": "Kaybolan sabit", "icerik": [
            "Toplamdaki bir sabit türevde sıfır olduğu için yalnızca sabitleri farklı olan fonksiyonların türevleri aynıdır. $x^2+5$ ile $x^2-3$ fonksiyonlarının ikisinin de türevi $2x$ tir; grafikleri birbirinin dikey kaydırılmış kopyasıdır ve her apsiste eğimleri eşittir.",
            "Bu gözlem, türevden fonksiyona geri dönerken bir sabitin belirsiz kalmasının nedenidir. Örneğin türevi $6x$ ve $f(0)=1$ olan fonksiyon $f(x)=3x^2+1$ dir; koşul verilmeseydi sabit bulunamazdı. Bu geri dönüş işlemi integral konusunun başlangıcıdır.",
        ]},
        {"baslik": "Farklı değişkenler ve harfli katsayılar", "icerik": [
            "Türev hangi değişkene göre alınıyorsa yalnızca o harf değişken kabul edilir; diğer harfler sabit gibi davranır. Zamana bağlı fonksiyonlarda değişken genellikle $t$ dir.",
            ornek(
                "$s(t)=3t^2+2t$ ve $f(x)=ax^2+bx$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$s'(t)=6t+2$ olur.",
                "$a$ ve $b$ sabit kabul edilir: $f'(x)=2ax+b$ olur."),
        ]},
        {"baslik": "Türevden katsayı bulmak", "icerik": [
            "Bir noktadaki türev değeri verilmişse bilinmeyen katsayı, türev alınıp o nokta yerine yazılarak bulunur. Bu tür sorular türev kurallarının ters yönde kullanımıdır.",
            ornek(
                "$f(x)=ax^3+2x$ ve $f'(1)=11$ olsun.",
                "$a$ yı bulalım.",
                "$f'(x)=3ax^2+2$ olduğundan $f'(1)=3a+2$ olur.",
                "$3a+2=11$ denkleminden $a=3$ bulunur."),
        ]},
        {"baslik": "Kök ve kesirleri üslü yazmak", "icerik": [
            "Kök ve paydada $x$ bulunan terimler kuvvet kuralına uymaz gibi görünür. Önce üslü biçime çevrilirlerse kural doğrudan uygulanır: $\\sqrt{x}=x^{1/2}$ ve $\\dfrac{1}{x^n}=x^{-n}$.",
            ornek(
                "$f(x)=3\\sqrt{x}-\\dfrac{2}{x}+\\dfrac{x^2}{4}$ fonksiyonu verilsin.",
                "Türevini ve $f'(4)$ değerini bulalım.",
                "$f(x)=3x^{1/2}-2x^{-1}+\\dfrac{1}{4}x^2$ olduğundan $f'(x)=\\dfrac{3}{2\\sqrt{x}}+\\dfrac{2}{x^2}+\\dfrac{x}{2}$ olur.",
                "$f'(4)=\\dfrac{3}{4}+\\dfrac{1}{8}+2=\\dfrac{23}{8}$ bulunur."),
        ]},
        {"baslik": "Açarak türev almak", "icerik": [
            "Çarpım biçimindeki basit ifadeler önce açılırsa türev kuvvet ve toplam kurallarıyla alınır. Bu yol, çarpım kuralına gerek bırakmaz ve çoğu zaman daha az hata üretir. Açılımı uzun süren yüksek kuvvetlerde ise zincir kuralı daha hızlıdır.",
            ornek(
                "$f(x)=(x+1)(x-2)$ ve $g(x)=(x^2+1)^2$ fonksiyonları verilsin.",
                "Türevlerini açarak bulalım.",
                "$f(x)=x^2-x-2$ olduğundan $f'(x)=2x-1$ olur.",
                "$g(x)=x^4+2x^2+1$ olduğundan $g'(x)=4x^3+4x$ olur."),
        ]},
        {"baslik": "Terimlere ayırarak türev almak", "icerik": [
            "Payı birden fazla terimli, paydası tek terimli bir kesir, terimlere ayrılarak sadeleştirilir. Bölüm kuralına gerek kalmadan her terim ayrı türevlenir. Payda birden fazla terimliyse bu yol işlemez ve bölüm kuralı gerekir.",
            ornek(
                "$f(x)=\\dfrac{x^3+2x}{x}$ ve $g(x)=\\dfrac{x^2+3}{\\sqrt{x}}$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$f(x)=x^2+2$ olduğundan $f'(x)=2x$ olur.",
                "$g(x)=x^{3/2}+3x^{-1/2}$ olduğundan $g'(x)=\\dfrac{3}{2}x^{1/2}-\\dfrac{3}{2}x^{-3/2}$ olur."),
        ]},
        {"baslik": "Çarpım kuralı", "icerik": [
            "İki fonksiyonun çarpımının türevi, türevlerin çarpımı değildir; bu kural türevin en çok karıştırılan yeridir. Birinci fonksiyonun türevi ikinciyle, birinci fonksiyon ikincinin türeviyle çarpılır ve toplanır:",
            "$$(f \\cdot g)'=f' \\cdot g+f \\cdot g'$$",
            ornek(
                "$h(x)=x^2 \\sin x$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "$f=x^2$ ve $g=\\sin x$ alınır: $f'=2x$ ve $g'=\\cos x$.",
                "$h'(x)=2x\\sin x+x^2\\cos x$ olur."),
            "Çarpım kuralının ispatı ve daha fazla örnek için <a href=\"/blog/carpimin-turevi/\">Çarpımın Türevi Nasıl Alınır?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Bölüm kuralı", "icerik": [
            "İki fonksiyonun bölümünün türevi için payın türevi paydayla çarpılır, pay paydanın türeviyle çarpılır, bu iki çarpımın farkı paydanın karesine bölünür:",
            "$$\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f' g-f g'}{g^2}$$",
            ornek(
                "$h(x)=\\dfrac{x+1}{x-1}$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "$h'(x)=\\dfrac{1 \\cdot (x-1)-(x+1) \\cdot 1}{(x-1)^2}$ olur.",
                "Pay $-2$ ye sadeleşir: $h'(x)=\\dfrac{-2}{(x-1)^2}$."),
            "Paydaki sıra önemlidir; ayrıntılar <a href=\"/blog/bolumun-turevi/\">Bölümün Türevi Nasıl Alınır?</a> yazısında.",
        ]},
        {"baslik": "Zincir kuralı", "icerik": [
            "Bir fonksiyonun içine başka bir fonksiyon yerleştirilmişse, dıştaki fonksiyonun türevi içteki ifadede hesaplanır ve içteki fonksiyonun türeviyle çarpılır:",
            "$$(f(g(x)))'=f'(g(x)) \\cdot g'(x)$$",
            ornek(
                "$h(x)=(3x+1)^5$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "Dıştaki fonksiyonun türevi $5(3x+1)^4$, içtekinin türevi $3$ tür.",
                "$h'(x)=15(3x+1)^4$ olur."),
            "Zincir kuralının mantığı ve çok katlı bileşkeler için <a href=\"/blog/zincir-kurali/\">Bileşke Fonksiyonun Türevi: Zincir Kuralı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Trigonometrik fonksiyonların türevleri", "icerik": [
            "Sinüs ve kosinüsün türevleri tanımdan, tanjant ve kotanjantınkiler bölüm kuralından bulunur. Açılar radyan cinsindendir:",
            tablo(["Fonksiyon", "Türevi"], [
                ["$\\sin x$", "$\\cos x$"],
                ["$\\cos x$", "$-\\sin x$"],
                ["$\\tan x$", "$1+\\tan^2 x=\\dfrac{1}{\\cos^2 x}$"],
                ["$\\cot x$", "$-(1+\\cot^2 x)=-\\dfrac{1}{\\sin^2 x}$"],
            ]),
            ornek(
                "$f(x)=3\\sin x-2\\cos x+\\tan x$ fonksiyonu verilsin.",
                "$f'(0)$ değerini bulalım.",
                "$f'(x)=3\\cos x+2\\sin x+1+\\tan^2 x$ olur.",
                "$f'(0)=3+0+1+0=4$ bulunur."),
        ]},
        {"baslik": "Tanjantın türevi nereden gelir?", "icerik": [
            "Tanjant, sinüsün kosinüse bölümü olduğu için türevi bölüm kuralıyla bulunur. Payda kosinüsün türevi, paydada sinüsün türevi yer alır ve temel özdeşlik sonucu sadeleştirir.",
            ornek(
                "$\\tan x=\\dfrac{\\sin x}{\\cos x}$ yazılsın.",
                "Türevini bulalım ve $x=\\dfrac{\\pi}{4}$ teki değerini hesaplayalım.",
                "$\\dfrac{\\cos x \\cdot \\cos x-\\sin x \\cdot (-\\sin x)}{\\cos^2 x}=\\dfrac{1}{\\cos^2 x}$ olur.",
                "$\\cos \\dfrac{\\pi}{4}=\\dfrac{\\sqrt{2}}{2}$ olduğundan türev $\\dfrac{1}{1/2}=2$ olur."),
        ]},
        {"baslik": "Üstel ve logaritmik türevler", "icerik": [
            "Üstel ve logaritmik fonksiyonların türevleri tabanın $e$ olup olmamasına göre ayrılır. Taban $e$ değilse doğal logaritma bir çarpan olarak ortaya çıkar:",
            tablo(["Fonksiyon", "Türevi"], [
                ["$e^x$", "$e^x$"],
                ["$a^x$", "$a^x \\ln a$"],
                ["$\\ln x$", "$\\dfrac{1}{x}$"],
                ["$\\log_a x$", "$\\dfrac{1}{x \\ln a}$"],
            ]),
            ornek(
                "$f(x)=2^x+\\log_3 x$ fonksiyonu verilsin.",
                "$f'(1)$ değerini bulalım.",
                "$f'(x)=2^x \\ln 2+\\dfrac{1}{x \\ln 3}$ olur.",
                "$f'(1)=2\\ln 2+\\dfrac{1}{\\ln 3}$ bulunur."),
        ]},
        {"baslik": "Logaritma kurallarıyla sadeleştirme", "icerik": [
            "Logaritmalı fonksiyonlarda türev almadan önce logaritma kuralları uygulanırsa işlem kısalır. Kuvvet kuralı üssü öne indirir, çarpım kuralı logaritmayı toplamlara ayırır.",
            ornek(
                "$f(x)=\\ln x^2$ ve $g(x)=\\ln(3x^4)$ fonksiyonları verilsin, $x>0$.",
                "Türevlerini ve $f'(1)$ değerini bulalım.",
                "$f(x)=2\\ln x$ olduğundan $f'(x)=\\dfrac{2}{x}$ ve $f'(1)=2$ olur.",
                "$g(x)=\\ln 3+4\\ln x$ olduğundan $g'(x)=\\dfrac{4}{x}$ olur."),
        ]},
        {"baslik": "Üstelde katsayılı üs", "icerik": [
            "Üssü $kx$ olan üstel fonksiyonlarda zincir kuralı gereği türevde $k$ çarpanı ortaya çıkar: $(e^{kx})'=k e^{kx}$. Logaritmada ise içteki katsayı sadeleşir: $(\\ln kx)'=\\dfrac{k}{kx}=\\dfrac{1}{x}$.",
            ornek(
                "$f(x)=e^{3x}$ ve $g(x)=\\ln 5x$ fonksiyonları verilsin.",
                "Türevlerini bulalım.",
                "$f'(x)=3e^{3x}$ olur.",
                "$g'(x)=\\dfrac{1}{x}$ olur; çünkü $\\ln 5x=\\ln 5+\\ln x$ ve $\\ln 5$ sabittir."),
        ]},
        {"baslik": "Parçalı fonksiyonların türevi", "icerik": [
            "Parçalı fonksiyonun türevi her parçada o parçanın kuralıyla alınır. Kritik noktalarda ise süreklilik ve iki yönün türevlerinin eşitliği ayrıca kontrol edilir.",
            ornek(
                "$x<2$ için $f(x)=x^2$, $x \\ge 2$ için $f(x)=4x-4$ olsun.",
                "Türev fonksiyonunu bulalım.",
                "$x<2$ için $f'(x)=2x$, $x>2$ için $f'(x)=4$ olur.",
                "$x=2$ de fonksiyon süreklidir ($4=4$) ve iki yönün türevi $4$ tür; bu yüzden $f'(2)=4$ vardır."),
        ]},
        {"baslik": "Mutlak değerli fonksiyonlar", "icerik": [
            "Mutlak değerli bir fonksiyon, içinin işaretine göre iki parçalı fonksiyon olarak yazılır; içi pozitifken olduğu gibi, negatifken eksiyle çarpılarak alınır. İçi sıfır yapan nokta dışında türev bu parçalardan alınır; o noktada genellikle bir köşe vardır ve türev yoktur.",
            ornek(
                "$f(x)=|x-2|$ fonksiyonu verilsin.",
                "$f'(5)$ ve $f'(0)$ değerlerini bulalım.",
                "$x>2$ iken $f(x)=x-2$ olduğundan $f'(5)=1$ olur.",
                "$x<2$ iken $f(x)=2-x$ olduğundan $f'(0)=-1$ olur; $x=2$ de türev yoktur."),
        ]},
        {"baslik": "Türevin işareti ve grafik", "icerik": [
            "Türev kuralları yalnızca bir sayı üretmez; türevin işareti grafiğin nerede yükselip nerede alçaldığını da söyler. Türev pozitifken grafik yükselir, negatifken alçalır, sıfır olduğunda ise yatay bir teğet vardır.",
            ornek(
                "$f(x)=x^2-4x$ fonksiyonu verilsin.",
                "Türevin işaretini inceleyelim.",
                "$f'(x)=2x-4$ olur; $x<2$ için negatif, $x>2$ için pozitiftir.",
                "Fonksiyon $x=2$ ye kadar azalır, sonra artar; $x=2$ parabolün tepe noktasının apsisidir."),
            "Bu yorumun ayrıntısı için <a href=\"/blog/artan-azalan-fonksiyonlar/\">Türevde Artan ve Azalan Fonksiyonlar</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Hız ve ivme hesabı", "icerik": [
            "Konum fonksiyonuna türev kuralları bir kez uygulanınca hız, iki kez uygulanınca ivme bulunur. Kurallar sayesinde bu hesap limit kullanmadan birkaç satırda yapılır.",
            ornek(
                "Bir cismin konumu $s(t)=2t^3-3t^2$ metre olsun.",
                "$t=2$ saniyedeki hızı ve ivmeyi bulalım.",
                "$v(t)=6t^2-6t$ olduğundan $v(2)=12$ metre bölü saniye olur.",
                "$a(t)=12t-6$ olduğundan $a(2)=18$ metre bölü saniye kare olur."),
        ]},
        {"baslik": "İkinci türev", "icerik": [
            "Türev kuralları art arda uygulanarak ikinci türev bulunur. İkinci türev, birinci türevin değişim hızıdır; grafiğin bükülme yönünü ve hareketteki ivmeyi verir.",
            ornek(
                "$f(x)=x^4-3x^2$ fonksiyonu verilsin.",
                "$f''(x)$ ve $f''(1)$ değerlerini bulalım.",
                "$f'(x)=4x^3-6x$ ve $f''(x)=12x^2-6$ olur.",
                "$f''(1)=6$ bulunur."),
        ]},
        {"baslik": "Yüksek mertebeden türevlerde örüntü", "icerik": [
            "Bazı fonksiyonlarda art arda alınan türevler bir örüntü oluşturur ve her adımda benzer bir çarpan eklenir. Örüntü bulunursa istenen mertebedeki türev tek tek hesaplanmadan yazılabilir.",
            ornek(
                "$f(x)=e^{2x}$ ve $g(x)=\\dfrac{1}{x}$ fonksiyonları verilsin.",
                "$f$ nin $n$ inci türevini ve $g'''(1)$ değerini bulalım.",
                "Her türevde $2$ çarpanı gelir: $f^{(n)}(x)=2^n e^{2x}$.",
                "$g'(x)=-x^{-2}$, $g''(x)=2x^{-3}$ ve $g'''(x)=-6x^{-4}$ olur; $g'''(1)=-6$."),
        ]},
        {"baslik": "Türevle teğet eğimi", "icerik": [
            "Türev kuralları, bir eğrinin herhangi bir noktadaki teğet eğimini hızla bulmayı sağlar; limitle tek tek hesaplamaya gerek kalmaz. Türev fonksiyonu bir kez bulunur, sonra istenen apsis yerine yazılır.",
            ornek(
                "$y=x^3-4x$ eğrisi verilsin.",
                "$x=2$ ve $x=0$ noktalarındaki teğet eğimlerini bulalım.",
                "$y'=3x^2-4$ olur.",
                "$x=2$ de eğim $8$, $x=0$ da eğim $-4$ bulunur."),
            "Eğimden teğet doğrusunun denklemine geçiş <a href=\"/blog/teget-denklemi/\">Türevde Teğet Denklemi Nasıl Bulunur?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Tek ve çift fonksiyonların türevi", "icerik": [
            "Türev alma, fonksiyonun simetrisini de değiştirir. Çift bir fonksiyonun türevi tektir, tek bir fonksiyonun türevi ise çifttir. $x^2$ çifttir ve türevi $2x$ tektir; $x^3$ tektir ve türevi $3x^2$ çifttir.",
            "Aynı durum trigonometrik fonksiyonlarda da görülür: sinüs tektir ve türevi olan kosinüs çifttir; kosinüs çifttir ve türevi olan $-\\sin x$ tektir. Bu özellik, bir türev sonucunu hızlıca denetlemenin yollarından biridir.",
        ]},
        {"baslik": "Kural seçimi", "icerik": [
            "Bir fonksiyonun türevini almadan önce yapısına bakmak doğru kuralı seçtirir. Aşağıdaki tablo en sık karşılaşılan yapıları özetler:",
            tablo(["Fonksiyonun yapısı", "Kullanılacak kural"], [
                ["Terimlerin toplamı", "Toplam kuralı, terim terim"],
                ["Kök ya da $\\dfrac{1}{x^n}$", "Üslü yazıp kuvvet kuralı"],
                ["Açılabilen çarpım", "Açıp terim terim"],
                ["Açılması zor çarpım", "Çarpım kuralı"],
                ["Paydası çok terimli kesir", "Bölüm kuralı"],
                ["İç içe fonksiyon", "Zincir kuralı"],
            ]),
            "Birçok fonksiyonda birden fazla kural birlikte kullanılır. Örneğin $x^2 e^{3x}$ için önce çarpım kuralı, $e^{3x}$ in türevinde ise zincir kuralı gerekir.",
        ]},
        {"baslik": "Kuralların özeti", "icerik": [
            tablo(["Kural", "Formül"], [
                ["Sabit", "$(c)'=0$"],
                ["Kuvvet", "$(x^n)'=nx^{n-1}$"],
                ["Sabitle çarpım", "$(cf)'=cf'$"],
                ["Toplam", "$(f+g)'=f'+g'$"],
                ["Çarpım", "$(fg)'=f'g+fg'$"],
                ["Bölüm", "$\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f'g-fg'}{g^2}$"],
                ["Zincir", "$(f(g(x)))'=f'(g(x))g'(x)$"],
            ]),
            "Tablodaki kuralların hepsi türevin tanımından ispatlanır. Bir kural akla gelmediğinde basit bir fonksiyonla, örneğin $x \\cdot x=x^2$ ile denemek doğru biçimi hatırlatır.",
        ]},
        {"baslik": "Sınavda türev kuralları", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) türev kuralları; bir noktadaki türev değeri, çarpım ve bölümün türevi, zincir kuralı, trigonometrik, üstel ve logaritmik türevler ve ikinci türev biçiminde karşına çıkabilir.",
                "Türevin diğer bütün uygulamaları bu kurallara dayanır."),
            "Soruda yalnızca bir noktadaki türev değeri isteniyorsa türev fonksiyonunu tamamen sadeleştirmeye gerek yoktur; türevi alıp sayıyı erkenden yerine yazmak zaman kazandırır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$(x^n)'=x^{n-1}$", "$(x^n)'=nx^{n-1}$"],
                ["$(fg)'=f'g'$", "$(fg)'=f'g+fg'$"],
                ["$\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f'}{g'}$", "Bölüm kuralı kullanılır"],
                ["$(e^{3x})'=e^{3x}$", "$3e^{3x}$"],
                ["$(2^x)'=x \\cdot 2^{x-1}$", "$2^x \\ln 2$"],
                ["$(\\cos x)'=\\sin x$", "$-\\sin x$"],
            ]),
            "Üstel fonksiyonu kuvvet fonksiyonu gibi türevlemek sık yapılan bir hatadır: $x^2$ de değişken tabanda, $2^x$ te üstedir. Kuvvet kuralı yalnızca değişkenin tabanda olduğu durumlar içindir.",
        ]},
    ],
    "sss": [
        ("Türev alma kuralları nelerdir?",
         "Sabit, kuvvet, sabitle çarpım, toplam, çarpım, bölüm ve zincir kurallarıdır. Bunlara trigonometrik, üstel ve logaritmik fonksiyonların türev tablosu eklenir."),
        ("Kuvvet kuralı nedir?",
         "x üzeri n in türevi n çarpı x üzeri n eksi 1 dir. Kural kesirli ve negatif üsler için de geçerlidir."),
        ("Karekökün türevi nasıl alınır?",
         "Karekök x, x üzeri 1 bölü 2 olarak yazılır. Türevi 1 bölü 2 kök x olur."),
        ("2 üzeri x in türevi nedir?",
         "2 üzeri x çarpı ln 2 dir. Kuvvet kuralı burada kullanılamaz, çünkü değişken üstedir."),
        ("tan x in türevi nedir?",
         "1 artı tan kare x ya da 1 bölü cos kare x tir."),
        ("Çarpımın türevi türevlerin çarpımı mıdır?",
         "Hayır. f çarpı g nin türevi f üssü çarpı g artı f çarpı g üssüdür."),
        ("e üzeri 3x in türevi nedir?",
         "Zincir kuralı gereği üsteki katsayı öne gelir: e üzeri 3x in türevi 3 e üzeri 3x tir."),
        ("ln x in türevi nedir?",
         "ln x in türevi 1 bölü x tir. Tabanı a olan logaritmada türev 1 bölü x ln a olur."),
    ],
    "kontrol": [
        "Sabit, kuvvet ve sabitle çarpım kurallarını uygulayabiliyorum.",
        "Toplam ve fark kuralıyla polinomların türevini alabiliyorum.",
        "Kök ve kesirleri üslü yazıp türev alabiliyorum.",
        "Açarak ya da terimlere ayırarak türev alabiliyorum.",
        "Çarpım ve bölüm kurallarını kullanabiliyorum.",
        "Zincir kuralını basit bileşkelerde uygulayabiliyorum.",
        "Trigonometrik fonksiyonların türevlerini biliyorum.",
        "Üstel ve logaritmik fonksiyonların türevlerini alabiliyorum.",
        "Parçalı ve mutlak değerli fonksiyonların türevini inceleyebiliyorum.",
        "İkinci ve daha yüksek mertebeden türevleri hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["turevin-tanimi", "carpimin-turevi", "zincir-kurali"],
}
