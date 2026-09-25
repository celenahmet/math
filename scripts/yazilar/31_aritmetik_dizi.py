# scripts/yazilar/31_aritmetik_dizi.py — Aritmetik Dizi Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "aritmetik-dizi",
    "baslik": "Aritmetik Dizi Konu Anlatımı",
    "aciklama": "Aritmetik dizi nedir? Ortak fark, genel terim, terim sayısı, aritmetik ortalama, simetrik terimler, ilk n terim toplamı ve günlük hayat problemleri; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "logaritma",
    "sinavlar": ["AYT"],
    "kapak": "aritmetik-dizi",
    "kapak_alt": "Aritmetik dizi: her basamağı bir öncekinden aynı miktarda yüksek mavi blok merdivene yeşil küpler ekleyen öğrenci",
    "ozet": "Aritmetik dizi, ardışık iki teriminin farkı hep aynı olan dizidir. Her adımda aynı miktar eklendiği için terimleri eşit aralıklarla ilerler ve grafiği bir doğru üzerinde dizilir. Bu yazıda aritmetik dizinin tanımını ve ortak farkı, genel terim formülünü, iki terimi verilen diziyi, terim sayısını, aritmetik ortalama özelliğini, simetrik terimleri, ilk n terim toplamı formüllerini, toplamdan genel terime geçişi, araya terim yerleştirmeyi ve birikim, amfi ve en büyük toplam gibi günlük hayat problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Aritmetik dizi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dizi, genel terim ve toplam sembolü kavramlarını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/diziler-konu-anlatimi/\">Diziler Konu Anlatımı</a> yazısına göz at."),
            "Ardışık iki terimi arasındaki fark her zaman aynı olan dizilere <strong>aritmetik dizi</strong> denir. Bu sabit farka <strong>ortak fark</strong> denir ve $d$ ile gösterilir. $3, 7, 11, 15, \\ldots$ dizisinde her terim bir öncekinden $4$ fazladır; ortak fark $d=4$ tür.",
            "Kapaktaki öğrenci her basamağı bir öncekinden aynı miktarda yüksek olan bir merdivene küpler ekliyor. Basamaklar eşit aralıklarla yükseldiği için merdivenin yükseklikleri bir aritmetik dizi oluşturur. Aritmetik dizinin bütün özellikleri bu eşit adım fikrinden gelir.",
        ]},
        {"baslik": "Aritmetik dizi olma koşulu", "icerik": [
            "Bir dizinin aritmetik olup olmadığını anlamak için ardışık terimlerin farkına bakılır. Fark her $n$ için aynı sabitse dizi aritmetiktir: $a_{n+1}-a_n=d$.",
            ornek(
                "$a_n=5n-2$ ve $b_n=n^2$ dizileri verilsin.",
                "Hangisinin aritmetik dizi olduğunu bulalım.",
                "$a_{n+1}-a_n=5(n+1)-2-(5n-2)=5$; fark sabittir, $a_n$ aritmetiktir ve $d=5$ tir.",
                "$b_{n+1}-b_n=2n+1$; fark $n$ ye bağlıdır, $b_n$ aritmetik değildir."),
            hap("Genel terimi $n$ ye göre birinci dereceden olan her dizi aritmetiktir.",
                "$n$ nin katsayısı ortak farka eşittir."),
        ]},
        {"baslik": "Genel terim formülü", "icerik": [
            "Birinci terimden $n$ inci terime ulaşmak için ortak fark $n-1$ kez eklenir. Bu yüzden aritmetik dizinin genel terimi şöyledir:",
            "$$a_n=a_1+(n-1)d$$",
            ornek(
                "$a_1=3$ ve $d=4$ olan aritmetik dizi verilsin.",
                "Yirminci terimi bulalım.",
                "$a_{20}=3+19 \\cdot 4$ olur.",
                "Sonuç $79$ dur."),
            "Formül, herhangi iki terim arasındaki ilişkiye de genellenir: $a_n=a_k+(n-k)d$. İki terimin sıra numaraları arasındaki fark kadar ortak fark eklenir ya da çıkarılır. Örneğin $a_5$ biliniyorsa $a_{12}$ ye ulaşmak için ortak fark yedi kez eklenir; ilk terimi bulmaya gerek kalmaz.",
        ]},
        {"baslik": "İki terimi verilen dizi", "icerik": [
            "Bir aritmetik dizinin iki terimi biliniyorsa ortak fark ve ilk terim bulunur. İki terimin farkı, sıra numaraları farkı kadar ortak farka eşittir.",
            ornek(
                "Bir aritmetik dizide $a_3=11$ ve $a_8=26$ olsun.",
                "Ortak farkı, ilk terimi ve yirminci terimi bulalım.",
                "$a_8-a_3=5d=15$, yani $d=3$ olur; $a_1=a_3-2d=5$.",
                "$a_{20}=5+19 \\cdot 3=62$ bulunur."),
        ]},
        {"baslik": "Genel terimden ortak fark", "icerik": [
            "Genel terimi verilen bir aritmetik dizinin ortak farkı, $n$ nin katsayısından doğrudan okunur. Genel terim kesirli olsa bile bu kural geçerlidir; ilk terim ise $n=1$ yazılarak bulunur.",
            ornek(
                "$a_n=\\dfrac{3n+5}{2}$ dizisi verilsin.",
                "Ortak farkı ve ilk terimi bulalım.",
                "Genel terim $\\dfrac{3}{2}n+\\dfrac{5}{2}$ biçimindedir; ortak fark $\\dfrac{3}{2}$ tür.",
                "İlk terim $a_1=\\dfrac{3+5}{2}=4$ olur."),
        ]},
        {"baslik": "İlk negatif terim", "icerik": [
            "Azalan bir aritmetik dizinin kaçıncı teriminin ilk kez negatif olduğu, genel terim sıfırdan küçük yapılarak bulunur. Eşitsizliği sağlayan en küçük pozitif tam sayı aranan sıra numarasıdır.",
            ornek(
                "$40, 37, 34, \\ldots$ dizisi verilsin.",
                "İlk negatif terimi bulalım.",
                "$a_n=40+(n-1)(-3)=43-3n$ olur; $43-3n<0$ ise $n>14.3$.",
                "İlk negatif terim on beşinci terimdir: $a_{15}=-2$."),
        ]},
        {"baslik": "Terim sayısı", "icerik": [
            "İlk ve son terimi ile ortak farkı bilinen sonlu bir aritmetik dizinin terim sayısı şu formülle bulunur:",
            "$$\\text{Terim sayısı}=\\dfrac{\\text{Son terim}-\\text{İlk terim}}{d}+1$$",
            ornek(
                "$7, 11, 15, \\ldots, 99$ dizisi verilsin.",
                "Dizinin kaç terimi olduğunu bulalım.",
                "Ortak fark $4$ tür: $\\dfrac{99-7}{4}+1$ hesaplanır.",
                "$23+1=24$ terim vardır."),
            "Formüldeki $+1$ unutulursa sonuç bir eksik çıkar. Bunun nedeni, iki uç arasındaki adım sayısının terim sayısından bir az olmasıdır; tıpkı bir çitte direk sayısının aralık sayısından bir fazla olması gibi.",
        ]},
        {"baslik": "Ardışık sayılar", "icerik": [
            "Ardışık tam sayılar ortak farkı $1$, ardışık çift ya da tek sayılar ortak farkı $2$ olan aritmetik dizilerdir. Bu yüzden ardışık sayıların toplamı, terim sayısı ile ortalamanın çarpımıdır.",
            ornek(
                "Ardışık $10$ tam sayının toplamı $155$ olsun.",
                "Bu sayıları bulalım.",
                "Ortalama $\\dfrac{155}{10}=15.5$ tir; bu değer beşinci ve altıncı sayının tam ortasıdır.",
                "Beşinci sayı $15$, altıncı sayı $16$ olduğundan sayılar $11$ den $20$ ye kadardır."),
            "Ardışık sayı problemlerinin daha fazla örneği için <a href=\"/blog/ardisik-sayilar/\">Ardışık Sayılar</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Çift sıralı terimler", "icerik": [
            "Bir aritmetik diziden düzenli aralıklarla seçilen terimler de aritmetik dizi oluşturur. Örneğin yalnızca çift sıralı terimler alınırsa her adımda iki terim atlandığı için yeni ortak fark $2d$ olur.",
            ornek(
                "$a_1=2$ ve $d=3$ olan aritmetik dizi verilsin.",
                "$a_2$, $a_4$, $a_6$, $\\ldots$ terimlerinden oluşan dizinin ilk üç terimini ve ortak farkını bulalım.",
                "$a_2=5$, $a_4=11$ ve $a_6=17$ olur.",
                "Yeni dizinin ortak farkı $6$ dır, yani $2d$ ye eşittir."),
        ]},
        {"baslik": "Aritmetik ortalama özelliği", "icerik": [
            "Aritmetik dizide her terim, kendisine komşu iki terimin aritmetik ortalamasıdır: $a_n=\\dfrac{a_{n-1}+a_{n+1}}{2}$. Bu yüzden $a$, $b$, $c$ sayılarının aritmetik dizi oluşturması için $2b=a+c$ olmalıdır.",
            ornek(
                "$x+1$, $3x-2$ ve $4x+1$ sayıları bu sırayla bir aritmetik dizinin ardışık terimleri olsun.",
                "$x$ i ve terimleri bulalım.",
                "$2(3x-2)=(x+1)+(4x+1)$, yani $6x-4=5x+2$ ve $x=6$ olur.",
                "Terimler $7$, $16$ ve $25$ tir; ortak fark $9$ dur."),
        ]},
        {"baslik": "Simetrik terimler", "icerik": [
            "Aritmetik dizide sıra numaralarının toplamı eşit olan terim çiftlerinin toplamları da eşittir: $p+q=r+s$ ise $a_p+a_q=a_r+a_s$ olur. Bu özellik, ortak farkı ve ilk terimi bulmadan birçok soruyu çözer.",
            ornek(
                "Bir aritmetik dizide $a_3+a_{12}=40$ olsun.",
                "$a_7+a_8$ ve $a_1+a_{14}$ toplamlarını bulalım.",
                "$3+12=7+8=15$ olduğundan $a_7+a_8=40$ olur.",
                "$1+14=15$ olduğundan $a_1+a_{14}=40$ olur."),
        ]},
        {"baslik": "İlk n terimin toplamı", "icerik": [
            "Aritmetik dizinin ilk $n$ teriminin toplamı, terimler baştan ve sondan eşleştirilerek bulunur. Her çiftin toplamı $a_1+a_n$ dir ve $\\dfrac{n}{2}$ çift vardır:",
            "$$S_n=\\dfrac{n(a_1+a_n)}{2}$$",
            "Son terim yerine genel terim formülü yazılırsa toplam yalnızca ilk terim ve ortak farkla ifade edilir:",
            "$$S_n=\\dfrac{n}{2}\\left(2a_1+(n-1)d\\right)$$",
        ]},
        {"baslik": "Toplam formülünün kullanımı", "icerik": [
            "Son terim biliniyorsa birinci formül, bilinmiyorsa ikinci formül kullanılır. İki formül de aynı sonucu verir; seçim yalnızca hesabı kısaltmak içindir.",
            ornek(
                "$3, 7, 11, \\ldots$ dizisi verilsin.",
                "İlk $20$ terimin toplamını bulalım.",
                "$a_1=3$ ve $d=4$ olduğundan $S_{20}=\\dfrac{20}{2}(2 \\cdot 3+19 \\cdot 4)$ olur.",
                "$10 \\cdot 82=820$ bulunur."),
        ]},
        {"baslik": "Bilinen toplamlar", "icerik": [
            "Bazı toplamlar o kadar sık kullanılır ki formülleri ayrıca bilinir. Hepsi aritmetik dizi toplam formülünün özel hâlleridir:",
            tablo(["Toplam", "Formül", "Örnek"], [
                ["$1+2+\\cdots+n$", "$\\dfrac{n(n+1)}{2}$", "$1+2+\\cdots+100=5050$"],
                ["$1+3+\\cdots+(2n-1)$", "$n^2$", "İlk $10$ tek sayı: $100$"],
                ["$2+4+\\cdots+2n$", "$n(n+1)$", "İlk $10$ çift sayı: $110$"],
            ]),
            ornek(
                "İki basamaklı sayılardan $7$ ile tam bölünenler verilsin.",
                "Bu sayıların toplamını bulalım.",
                "Sayılar $14, 21, \\ldots, 98$ dir; terim sayısı $\\dfrac{98-14}{7}+1=13$ olur.",
                "Toplam $\\dfrac{13(14+98)}{2}=728$ bulunur."),
        ]},
        {"baslik": "Toplamı verilen dizide terim sayısı", "icerik": [
            "İlk terimi, ortak farkı ve toplamı bilinen bir dizinin kaç terimden oluştuğu, toplam formülü $n$ ye göre ikinci dereceden bir denklem olarak çözülerek bulunur. Negatif ya da kesirli kök atılır.",
            ornek(
                "$5+9+13+\\cdots$ toplamı $275$ olsun.",
                "Toplamda kaç terim olduğunu bulalım.",
                "$S_n=\\dfrac{n}{2}(10+4(n-1))=n(2n+3)$ olur; $2n^2+3n-275=0$ denklemi yazılır.",
                "$(n-11)(2n+25)=0$ olduğundan $n=11$ terim vardır."),
        ]},
        {"baslik": "İki toplamdan dizi bulmak", "icerik": [
            "Aynı dizinin iki farklı kısmi toplamı biliniyorsa, toplam formülü iki kez yazılarak ilk terim ve ortak fark için iki denklem elde edilir.",
            ornek(
                "Bir aritmetik dizide $S_{10}=100$ ve $S_{20}=400$ olsun.",
                "İlk terimi ve ortak farkı bulalım.",
                "$5(2a_1+9d)=100$ ve $10(2a_1+19d)=400$ olur; buradan $2a_1+9d=20$ ve $2a_1+19d=40$.",
                "Çıkarınca $10d=20$, yani $d=2$ ve $a_1=1$ bulunur; dizi tek sayılar dizisidir."),
        ]},
        {"baslik": "İki dizinin ortak terimleri", "icerik": [
            "İki aritmetik dizinin ortak terimleri de bir aritmetik dizi oluşturur. Bu yeni dizinin ortak farkı, iki ortak farkın en küçük ortak katıdır; ilk ortak terim ise terimler yazılarak bulunur.",
            ornek(
                "$3, 7, 11, \\ldots$ ve $2, 7, 12, \\ldots$ dizileri verilsin.",
                "Ortak terimlerden oluşan dizinin ilk üç terimini bulalım.",
                "İlk ortak terim $7$ dir; ortak farklar $4$ ve $5$ olduğundan yeni ortak fark $20$ dir.",
                "Ortak terimler $7$, $27$ ve $47$ olur."),
        ]},
        {"baslik": "Toplamdan genel terim", "icerik": [
            "Aritmetik dizinin kısmi toplamı $n$ ye göre ikinci dereceden ve sabit terimi olmayan bir ifadedir: $S_n=An^2+Bn$. Tersine, kısmi toplamı bu biçimde olan her dizi aritmetiktir ve ortak farkı $2A$ dır.",
            ornek(
                "Bir dizinin ilk $n$ teriminin toplamı $S_n=2n^2+3n$ olsun.",
                "Genel terimi ve ortak farkı bulalım.",
                "$a_n=S_n-S_{n-1}=2n^2+3n-2(n-1)^2-3(n-1)=4n+1$ olur.",
                "Dizi aritmetiktir, $d=4$ ve $a_1=5$ tir; gerçekten $S_1=5$ tir."),
        ]},
        {"baslik": "Ortanca terim ve toplam", "icerik": [
            "Tek sayıda terimi olan bir aritmetik dizide ortadaki terim, bütün terimlerin aritmetik ortalamasıdır. Bu yüzden toplam, terim sayısı ile ortanca terimin çarpımına eşittir.",
            ornek(
                "Dokuz terimli bir aritmetik dizinin ortanca terimi $12$ olsun.",
                "Terimlerin toplamını bulalım.",
                "Ortanca terim beşinci terimdir ve ortalamaya eşittir.",
                "Toplam $9 \\cdot 12=108$ olur."),
        ]},
        {"baslik": "Aritmetik dizinin grafiği", "icerik": [
            "Aritmetik dizinin genel terimi $n$ ye göre birinci dereceden olduğu için terimleri bir doğru üzerinde dizilir. Doğrunun eğimi ortak farka eşittir.",
            koordinat_grafik("a_n = 2n - 3 dizisinin terimleri ve y = 2x - 3 doğrusu", [("y = 2x - 3", lambda x: 2 * x - 3)], (-0.5, 6.5), (-3, 9), adim=1,
                             noktalar=[(1, -1, "", True), (2, 1, "", True), (3, 3, "", True), (4, 5, "", True), (5, 7, "", True)]),
            "Grafikteki noktalar $a_n=2n-3$ dizisinin ilk beş terimidir: $-1$, $1$, $3$, $5$ ve $7$. Dizi yalnızca bu noktalardan oluşur; doğru, noktaların aynı doğru üzerinde dizildiğini göstermek için çizilmiştir.",
        ]},
        {"baslik": "Artan, azalan ve sabit", "icerik": [
            "Aritmetik dizinin davranışını ortak farkın işareti belirler. Ortak fark pozitifse dizi artan, negatifse azalan, sıfırsa sabittir.",
            tablo(["Ortak fark", "Dizi", "Örnek"], [
                ["$d>0$", "Artan", "$2, 5, 8, 11, \\ldots$"],
                ["$d<0$", "Azalan", "$20, 17, 14, 11, \\ldots$"],
                ["$d=0$", "Sabit", "$6, 6, 6, 6, \\ldots$"],
            ]),
        ]},
        {"baslik": "Araya terim yerleştirme", "icerik": [
            "İki sayı arasına belirli sayıda terim yerleştirerek bir aritmetik dizi oluşturulabilir. Araya $k$ terim girerse toplam terim sayısı $k+2$ olur ve iki uç arasında $k+1$ adım bulunur.",
            ornek(
                "$5$ ile $29$ arasına $5$ terim yerleştirilerek bir aritmetik dizi oluşturulsun.",
                "Yerleştirilen terimleri bulalım.",
                "Adım sayısı $6$ dır: $d=\\dfrac{29-5}{6}=4$ olur.",
                "Yerleştirilen terimler $9$, $13$, $17$, $21$ ve $25$ tir."),
        ]},
        {"baslik": "Üç terim problemi", "icerik": [
            "Aritmetik dizi oluşturan üç sayı sorulduğunda terimleri $a-d$, $a$ ve $a+d$ olarak almak hesabı çok kısaltır; çünkü toplamda ortak fark sadeleşir.",
            ornek(
                "Aritmetik dizi oluşturan üç sayının toplamı $30$, çarpımı $910$ olsun.",
                "Sayıları bulalım.",
                "Toplamdan $3a=30$, yani $a=10$. Çarpımdan $(10-d) \\cdot 10 \\cdot (10+d)=910$, yani $100-d^2=91$ ve $d=\\pm 3$.",
                "Sayılar $7$, $10$ ve $13$ olur."),
        ]},
        {"baslik": "Problem: birikim", "icerik": [
            "Her dönem aynı miktarda artan ödeme ya da birikimler aritmetik dizi oluşturur. Belirli bir dönemdeki tutar genel terimle, toplam birikim ise toplam formülüyle bulunur.",
            ornek(
                "Bir öğrenci ilk hafta $20$ TL biriktiriyor ve her hafta bir önceki haftadan $5$ TL fazla biriktiriyor.",
                "Onuncu haftada biriktirdiği tutarı ve on haftalık toplamı bulalım.",
                "$a_{10}=20+9 \\cdot 5=65$ TL olur.",
                "$S_{10}=\\dfrac{10(20+65)}{2}=425$ TL olur."),
        ]},
        {"baslik": "Problem: amfi koltukları", "icerik": [
            "Sıraları geriye doğru genişleyen salonlar, basamaklı yapılar ve üst üste dizilmiş borular gibi geometrik düzenler de aritmetik dizilerle modellenir.",
            ornek(
                "Bir amfinin ilk sırasında $12$ koltuk var ve her sırada bir önceki sıradan $2$ koltuk fazla bulunuyor. Amfide $15$ sıra var.",
                "Son sıradaki koltuk sayısını ve toplam koltuk sayısını bulalım.",
                "Son sıra: $a_{15}=12+14 \\cdot 2=40$ koltuk.",
                "Toplam: $S_{15}=\\dfrac{15(12+40)}{2}=390$ koltuk."),
        ]},
        {"baslik": "En büyük toplam", "icerik": [
            "Azalan bir aritmetik dizide terimler bir noktadan sonra negatif olur. Negatif terimler eklendikçe toplam küçüleceği için toplam, son pozitif terime kadar alındığında en büyük değerine ulaşır.",
            ornek(
                "$50, 46, 42, \\ldots$ dizisi verilsin.",
                "İlk kaç terimin toplamının en büyük olduğunu ve bu toplamı bulalım.",
                "$a_n=54-4n$ olur; $a_{13}=2>0$ ve $a_{14}=-2<0$ dır.",
                "Toplam ilk $13$ terimde en büyüktür: $S_{13}=\\dfrac{13(50+2)}{2}=338$."),
            "On dördüncü terimden itibaren her yeni terim negatif olduğu için toplamı azaltır; örneğin $S_{14}=338-2=336$ olur.",
        ]},
        {"baslik": "Formüllerin özeti", "icerik": [
            tablo(["Kavram", "Formül"], [
                ["Ortak fark", "$d=a_{n+1}-a_n$"],
                ["Genel terim", "$a_n=a_1+(n-1)d$"],
                ["İki terim arası", "$a_n=a_k+(n-k)d$"],
                ["Terim sayısı", "$\\dfrac{\\text{Son}-\\text{İlk}}{d}+1$"],
                ["Ortalama özelliği", "$2a_n=a_{n-1}+a_{n+1}$"],
                ["Toplam", "$S_n=\\dfrac{n(a_1+a_n)}{2}$"],
            ]),
            "Formüllerin hepsi tek bir fikre dayanır: her adımda aynı sayı eklenir. Bir formül akla gelmediğinde ilk birkaç terimi yazıp adımları saymak doğru sonuca götürür.",
        ]},
        {"baslik": "Sınavda aritmetik dizi", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) aritmetik diziler; genel terim, iki terimi verilen dizi, simetrik terimler, toplam formülü ve günlük hayat problemleri biçiminde karşına çıkabilir.",
                "Temel düzeyde (<strong>TYT</strong>) ise ardışık sayılar ve örüntü soruları aynı fikre dayanır."),
            "Soruda iki terim verilmişse önce sıra numaraları farkını kullanarak ortak farkı bul. Terimlerin toplamı soruluyorsa simetrik terim özelliğine bak; çoğu zaman ilk terimi bulmaya bile gerek kalmaz.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$a_n=a_1+nd$ yazmak", "$a_n=a_1+(n-1)d$"],
                ["Terim sayısında $+1$ i unutmak", "$\\dfrac{\\text{Son}-\\text{İlk}}{d}+1$"],
                ["Araya $k$ terimde $k$ adım almak", "$k+1$ adım vardır"],
                ["$a_p+a_q$ yu $a_{p+q}$ sanmak", "Simetrik terim özelliği kullanılır"],
                ["Toplamı $n \\cdot a_n$ almak", "$S_n=\\dfrac{n(a_1+a_n)}{2}$"],
                ["$b_n=n^2$ gibi dizileri aritmetik sanmak", "Fark sabit olmalı"],
            ]),
            "Bu hataların çoğu adım sayısı ile terim sayısını karıştırmaktan doğar. Birinci terimden $n$ inci terime giderken $n-1$ adım atılır; bu tek gözlem genel terim ve terim sayısı formüllerinin ikisini de açıklar.",
        ]},
    ],
    "sss": [
        ("Aritmetik dizi nedir?",
         "Ardışık iki terimi arasındaki farkın hep aynı olduğu dizidir. Bu sabit farka ortak fark denir."),
        ("Aritmetik dizinin genel terimi nedir?",
         "a n eşittir a 1 artı n eksi 1 çarpı d dir. İlk terime ortak fark n eksi 1 kez eklenir."),
        ("Aritmetik dizide ilk n terimin toplamı nasıl bulunur?",
         "İlk terim ile son terim toplanır, terim sayısıyla çarpılır ve ikiye bölünür: S n eşittir n çarpı a 1 artı a n bölü 2."),
        ("Terim sayısı nasıl bulunur?",
         "Son terimden ilk terim çıkarılır, ortak farka bölünür ve 1 eklenir."),
        ("1 den 100 e kadar sayıların toplamı kaçtır?",
         "Toplam 100 çarpı 101 bölü 2, yani 5050 dir."),
        ("Aritmetik ortalama özelliği nedir?",
         "Aritmetik dizide her terim, komşu iki terimin ortalamasıdır. a, b, c aritmetik dizi oluşturuyorsa 2b eşittir a artı c dir."),
        ("Aritmetik dizide simetrik terim özelliği nedir?",
         "Sıra numaralarının toplamı eşit olan terim çiftlerinin toplamları da eşittir. Örneğin a 3 artı a 12, a 7 artı a 8 e eşittir; çünkü iki çiftte de sıra numaraları toplamı 15 tir."),
    ],
    "kontrol": [
        "Aritmetik diziyi ve ortak farkı tanımlayabiliyorum.",
        "Bir dizinin aritmetik olup olmadığını belirleyebiliyorum.",
        "Genel terim formülüyle istenen terimi bulabiliyorum.",
        "İki terimi verilen dizinin ortak farkını ve ilk terimini bulabiliyorum.",
        "Sonlu bir aritmetik dizinin terim sayısını hesaplayabiliyorum.",
        "Aritmetik ortalama ve simetrik terim özelliklerini kullanabiliyorum.",
        "İlk n terimin toplamını iki formülle de hesaplayabiliyorum.",
        "Kısmi toplamdan genel terimi ve ortak farkı bulabiliyorum.",
        "İki sayı arasına terim yerleştirebiliyorum.",
        "Birikim, amfi ve en büyük toplam problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["diziler-konu-anlatimi", "geometrik-dizi", "ardisik-sayilar"],
}
