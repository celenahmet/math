# scripts/yazilar/30_diziler.py — Diziler Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "diziler-konu-anlatimi",
    "baslik": "Diziler Konu Anlatımı",
    "aciklama": "Dizi nedir? Genel terim, dizi olma koşulu, sabit, artan ve azalan diziler, indirgemeli diziler, toplam sembolü ve kısmi toplamlar; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "logaritma",
    "sinavlar": ["AYT"],
    "kapak": "diziler-konu-anlatimi",
    "kapak_alt": "Diziler konu anlatımı: bölmelere sırayla artan renkli üçgen desenlerini yerleştirip sonraki terimi tamamlayan iki öğrenci",
    "ozet": "Dizi, belirli bir kurala göre sıralanmış sayıların listesidir ve matematikte pozitif tam sayılar üzerinde tanımlı bir fonksiyon olarak ele alınır. Örüntüleri tanımak, bir sonraki terimi tahmin etmek ve uzun toplamları hesaplamak dizilerle yapılır. Bu yazıda dizinin tanımını, genel terimi, bir ifadenin dizi olma koşulunu, sonlu ve sonsuz dizileri, sabit, artan ve azalan dizileri, indirgemeli dizileri ve Fibonacci dizisini, dizilerde eşitlik ve işlemleri, toplam sembolünü, kısmi toplamdan genel terime geçişi ve periyodik dizileri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Dizi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için fonksiyon kavramını ve temel cebirsel işlemleri biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/fonksiyonlar-konu-anlatimi/\">Fonksiyonlar Konu Anlatımı</a> yazısına göz at."),
            "Belirli bir kurala göre sıralanmış sayılara <strong>dizi</strong> denir. $2, 4, 6, 8, \\ldots$ çift sayılar dizisidir; $1, 4, 9, 16, \\ldots$ ise kare sayılar dizisidir. Dizideki her sayıya bir <strong>terim</strong> denir ve terimlerin sırası önemlidir.",
            "Kapaktaki öğrenciler bölmelere $1$, $3$, $6$ ve $10$ üçgenden oluşan desenler yerleştirmiş ve boş kalan beşinci bölmeyi dolduruyor. Her desen bir öncekine yeni bir sıra eklenerek oluşuyor; beşinci desende $15$ üçgen olacak. Bu sayılara üçgensel sayılar denir ve dizilerin temel sorusunu gösterirler: kural bulunursa sıradaki terim bilinir.",
        ]},
        {"baslik": "Dizi bir fonksiyondur", "icerik": [
            "Matematikte dizi, tanım kümesi pozitif tam sayılar olan bir fonksiyon olarak tanımlanır. Fonksiyon her sıra numarasına bir sayı karşılık getirir: birinci terim $a_1$, ikinci terim $a_2$, $n$ inci terim $a_n$ ile gösterilir.",
            "$a_n$ ifadesine dizinin <strong>genel terimi</strong> denir. Genel terim biliniyorsa dizinin istenen her terimi $n$ yerine sıra numarası yazılarak hesaplanır. Dizi $(a_n)$ biçiminde gösterilir.",
            hap("Dizi, pozitif tam sayılardan gerçek sayılara bir fonksiyondur.",
                "$a_n$, $n$ inci sıradaki terimi verir."),
        ]},
        {"baslik": "Genel terimden terim bulmak", "icerik": [
            "Genel terimi verilen bir dizinin terimleri, $n$ yerine $1$, $2$, $3$ gibi sıra numaraları yazılarak bulunur.",
            ornek(
                "$a_n=3n-1$ dizisi verilsin.",
                "İlk üç terimi ve onuncu terimi bulalım.",
                "$a_1=2$, $a_2=5$ ve $a_3=8$ olur.",
                "$a_{10}=3 \\cdot 10-1=29$ bulunur."),
            ornek(
                "$b_n=\\dfrac{n+1}{n}$ dizisi verilsin.",
                "İlk dört terimi bulalım.",
                "$b_1=2$, $b_2=\\dfrac{3}{2}$ olur.",
                "$b_3=\\dfrac{4}{3}$ ve $b_4=\\dfrac{5}{4}$ olur."),
        ]},
        {"baslik": "Terimlerden genel terim bulmak", "icerik": [
            "Tersine, ilk birkaç terimi verilen bir dizinin genel terimi, terimlerin sıra numarasıyla ilişkisi aranarak bulunur. Kare, küp, ikinin kuvvetleri ve kesirler en sık görülen kalıplardır:",
            tablo(["Terimler", "Genel terim"], [
                ["$1, 4, 9, 16, \\ldots$", "$a_n=n^2$"],
                ["$2, 4, 8, 16, \\ldots$", "$a_n=2^n$"],
                ["$\\dfrac{1}{2}, \\dfrac{2}{3}, \\dfrac{3}{4}, \\ldots$", "$a_n=\\dfrac{n}{n+1}$"],
                ["$-1, 1, -1, 1, \\ldots$", "$a_n=(-1)^n$"],
            ]),
            "Birkaç terim tek bir kuralı kesin olarak belirlemez; farklı kurallar aynı ilk terimleri üretebilir. Bu yüzden sınav sorularında genellikle en basit kural beklenir ve seçeneklerle kontrol edilir.",
        ]},
        {"baslik": "Dizi olma koşulu", "icerik": [
            "Bir ifadenin dizi belirtmesi için her pozitif tam sayıda tanımlı olması gerekir. Paydası bir pozitif tam sayıda sıfır olan ya da kök içi bir pozitif tam sayıda negatif olan ifadeler dizi değildir.",
            ornek(
                "$a_n=\\dfrac{n+3}{n-2}$ ve $b_n=\\sqrt{n-3}$ ifadeleri verilsin.",
                "Dizi olup olmadıklarını inceleyelim.",
                "$a_2$ de payda sıfır olur; $a_n$ bir dizi değildir.",
                "$b_1$ ve $b_2$ de kök içi negatif olur; $b_n$ de bir dizi değildir."),
            ornek(
                "$c_n=\\dfrac{2n+1}{n+k}$ ifadesi verilsin.",
                "Bu ifadenin dizi olmadığı en büyük $k$ tam sayısını bulalım.",
                "Payda $n=-k$ için sıfır olur; bunun bir pozitif tam sayı olması için $k$ negatif bir tam sayı olmalıdır.",
                "$k \\le -1$ olduğunda ifade dizi değildir; en büyük böyle $k$ değeri $-1$ dir."),
        ]},
        {"baslik": "Kaçıncı terim?", "icerik": [
            "Bir sayının dizinin kaçıncı terimi olduğu, genel terim bu sayıya eşitlenerek bulunur. Çözüm pozitif bir tam sayı çıkmazsa sayı dizinin terimi değildir.",
            ornek(
                "$a_n=2n+5$ ve $b_n=n^2-1$ dizileri verilsin.",
                "$45$ in $a_n$ nin, $99$ un $b_n$ nin kaçıncı terimi olduğunu bulalım.",
                "$2n+5=45$ ise $n=20$; $45$, $a_n$ nin yirminci terimidir.",
                "$n^2-1=99$ ise $n^2=100$ ve $n=10$; $99$, $b_n$ nin onuncu terimidir."),
            "Aynı yolla $50$ nin $a_n$ nin terimi olmadığı görülür: $2n+5=50$ denkleminden $n=22.5$ çıkar ve bu bir tam sayı değildir.",
            hap("Bir sayının kaçıncı terim olduğu, genel terim o sayıya eşitlenerek bulunur.", "Çözüm pozitif bir tam sayı değilse sayı dizinin terimi değildir."),
        ]},
        {"baslik": "Belirli aralıktaki terim sayısı", "icerik": [
            "Bir dizinin iki sayı arasında kalan terimlerinin sayısı, genel terim için iki eşitsizlik yazılarak bulunur. Eşitsizlikleri sağlayan pozitif tam sayılar sayılır.",
            ornek(
                "$a_n=3n+1$ dizisi verilsin.",
                "$20$ ile $100$ arasında, sınırlar dahil, kaç terim olduğunu bulalım.",
                "$3n+1 \\ge 20$ ise $n \\ge 7$; $3n+1 \\le 100$ ise $n \\le 33$ olur.",
                "$n$ nin $7$ den $33$ e kadar aldığı değerler sayılır: $33-7+1=27$ terim vardır."),
        ]},
        {"baslik": "Terimlerin işareti", "icerik": [
            "Genel terimi kesirli olan dizilerde terimlerin işareti pay ve paydanın işaretine bağlıdır. Payda her pozitif tam sayıda pozitifse işareti pay belirler.",
            ornek(
                "$a_n=\\dfrac{n-5}{n+1}$ dizisi verilsin.",
                "Dizinin kaç negatif terimi olduğunu bulalım.",
                "Payda her zaman pozitiftir; terim $n<5$ iken negatif, $n=5$ iken sıfır, $n>5$ iken pozitiftir.",
                "Negatif terimler $a_1$, $a_2$, $a_3$ ve $a_4$ tür; dizinin dört negatif terimi vardır."),
        ]},
        {"baslik": "Sonlu ve sonsuz diziler", "icerik": [
            "Terim sayısı belirli bir sayıyla sınırlı olan dizilere <strong>sonlu dizi</strong>, terimleri sonsuza kadar devam eden dizilere <strong>sonsuz dizi</strong> denir. Bir yılın aylarındaki gün sayıları sonlu bir dizidir; pozitif tek sayılar ise sonsuz bir dizidir.",
            "Okul matematiğinde dizi denince çoğunlukla sonsuz diziler kastedilir. Sonlu dizilerde ise son terim ve terim sayısı önem kazanır; aritmetik ve geometrik dizilerin toplam formülleri de ilk $n$ terimi, yani sonlu bir parçayı toplar.",
        ]},
        {"baslik": "Sabit dizi", "icerik": [
            "Bütün terimleri birbirine eşit olan diziye <strong>sabit dizi</strong> denir. $a_n=7$ bir sabit dizidir. Genel terimi kesirli olan bir dizinin sabit olması için pay ve paydadaki katsayıların orantılı olması gerekir.",
            ornek(
                "$a_n=\\dfrac{kn+2}{3n+1}$ dizisi sabit dizi olsun.",
                "$k$ değerini ve dizinin terimini bulalım.",
                "Katsayılar orantılı olmalıdır: $\\dfrac{k}{3}=\\dfrac{2}{1}$, yani $k=6$.",
                "Dizi $a_n=\\dfrac{6n+2}{3n+1}=2$ olur; her terim $2$ dir."),
        ]},
        {"baslik": "Artan ve azalan diziler", "icerik": [
            "Her terimi bir öncekinden büyük olan diziye <strong>artan dizi</strong>, küçük olana <strong>azalan dizi</strong> denir. Bunu anlamanın en kısa yolu ardışık iki terimin farkına bakmaktır: $a_{n+1}-a_n$ her $n$ için pozitifse dizi artan, negatifse azalandır.",
            ornek(
                "$a_n=\\dfrac{n}{n+1}$ dizisi verilsin.",
                "Dizinin artan mı azalan mı olduğunu bulalım.",
                "$a_{n+1}-a_n=\\dfrac{n+1}{n+2}-\\dfrac{n}{n+1}=\\dfrac{1}{(n+1)(n+2)}$ olur.",
                "Fark her $n$ için pozitif olduğundan dizi artandır."),
            "Bazı diziler ne artan ne azalandır. $a_n=(-1)^n$ dizisinin terimleri $-1$ ve $1$ arasında gidip gelir; bu yüzden bu dizi monoton değildir.",
            hap("$a_{n+1}-a_n$ her $n$ için pozitifse dizi artan, negatifse azalandır."),
        ]},
        {"baslik": "Sınırlı diziler", "icerik": [
            "Terimlerinin hepsi belirli iki sayı arasında kalan dizilere <strong>sınırlı dizi</strong> denir. Artan bir dizinin en küçük terimi ilk terimidir; terimleri bir sayıya yaklaşıyorsa o sayı da bir üst sınırdır.",
            ornek(
                "$a_n=\\dfrac{n}{n+1}$ dizisi verilsin.",
                "Dizinin terimlerinin hangi aralıkta kaldığını bulalım.",
                "Dizi artandır; en küçük terimi $a_1=\\dfrac{1}{2}$ dir.",
                "Her terimde pay paydadan küçük olduğundan terimler $1$ den küçüktür: $\\dfrac{1}{2} \\le a_n<1$ olur."),
        ]},
        {"baslik": "Dizinin grafiği", "icerik": [
            "Dizi bir fonksiyon olduğu için grafiği çizilebilir. Ancak tanım kümesi yalnızca pozitif tam sayılar olduğundan grafik birleşik bir eğri değil, ayrık noktalardan oluşur.",
            koordinat_grafik("a_n = 6/n dizisinin ilk altı terimi", [], (-0.5, 7), (-0.5, 7), adim=1,
                             noktalar=[(1, 6, "", True), (2, 3, "", True), (3, 2, "", True), (4, 1.5, "", True), (5, 1.2, "", True), (6, 1, "", True)]),
            "Grafikteki noktalar $a_n=\\dfrac{6}{n}$ dizisinin ilk altı terimidir: $6$, $3$, $2$, $1.5$, $1.2$ ve $1$. Noktalar sağa doğru alçalıyor; dizi azalandır ve terimleri sıfıra yaklaşır ama hiçbir zaman sıfır olmaz.",
        ]},
        {"baslik": "İndirgemeli diziler", "icerik": [
            "Bazı dizilerde her terim, bir önceki terim ya da terimler kullanılarak tanımlanır. Bu tür dizilere <strong>indirgemeli dizi</strong> denir. İndirgemeli bir dizinin tanımlanması için ilk terimin ya da ilk birkaç terimin verilmesi gerekir.",
            ornek(
                "$a_1=1$ ve $a_{n+1}=2a_n+1$ dizisi verilsin.",
                "İlk beş terimi bulalım ve bir kural arayalım.",
                "$a_2=3$, $a_3=7$, $a_4=15$ ve $a_5=31$ olur.",
                "Terimler ikinin kuvvetlerinin bir eksiğidir: $a_n=2^n-1$."),
        ]},
        {"baslik": "Toplamla tanımlanan indirgeme", "icerik": [
            "İndirgeme bağıntısında her adımda farklı bir sayı eklenebilir. Bu durumda terimler yazılarak eklenen sayıların bir toplam oluşturduğu görülür ve genel terim toplam formülüyle bulunur.",
            ornek(
                "$a_1=1$ ve $a_{n+1}=a_n+n$ dizisi verilsin.",
                "İlk beş terimi ve genel terimi bulalım.",
                "Terimler $1$, $2$, $4$, $7$ ve $11$ olur; her adımda eklenen sayı bir artar.",
                "$a_n=1+(1+2+\\cdots+(n-1))=1+\\dfrac{n(n-1)}{2}$ bulunur; $n=5$ için $11$ çıkar."),
        ]},
        {"baslik": "Fibonacci dizisi", "icerik": [
            "En ünlü indirgemeli dizi Fibonacci dizisidir. İlk iki terimi $1$ dir ve her terim kendinden önceki iki terimin toplamıdır: $a_{n+2}=a_{n+1}+a_n$.",
            tablo(["$n$", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], [
                ["$a_n$", "1", "1", "2", "3", "5", "8", "13", "21", "34", "55"],
            ]),
            "Fibonacci dizisinde ardışık iki terimin oranı giderek altın oran denen $\\dfrac{1+\\sqrt{5}}{2}$ sayısına, yani yaklaşık $1.618$ e yaklaşır. Örneğin $\\dfrac{55}{34}$ yaklaşık $1.6176$ dır.",
        ]},
        {"baslik": "Dizilerde eşitlik", "icerik": [
            "İki dizinin eşit olması için bütün karşılıklı terimlerinin eşit olması gerekir: her $n$ için $a_n=b_n$. Genel terimler $n$ ye göre birer ifadeyse bu, aynı dereceli terimlerin katsayılarının eşit olması demektir.",
            ornek(
                "$a_n=(p+1)n+3$ ve $b_n=5n+q-2$ dizileri eşit olsun.",
                "$p$ ve $q$ yu bulalım.",
                "$n$ nin katsayıları eşitlenir: $p+1=5$, yani $p=4$.",
                "Sabit terimler eşitlenir: $3=q-2$, yani $q=5$."),
        ]},
        {"baslik": "Dizilerde işlemler", "icerik": [
            "İki dizi terim terim toplanabilir, çıkarılabilir, çarpılabilir ve sıfır terimi olmayan bir diziye bölünebilir. Sonuç yine bir dizidir: $(a_n+b_n)$, $(a_n \\cdot b_n)$ gibi.",
            ornek(
                "$a_n=2n$ ve $b_n=n^2$ dizileri verilsin.",
                "$(a_n+b_n)$ dizisinin üçüncü terimini ve $(a_n \\cdot b_n)$ dizisinin ikinci terimini bulalım.",
                "$a_3+b_3=6+9=15$ olur.",
                "$a_2 \\cdot b_2=4 \\cdot 4=16$ olur."),
        ]},
        {"baslik": "Toplam sembolü", "icerik": [
            "Bir dizinin art arda gelen terimlerinin toplamı kısaca $\\sum$ sembolüyle yazılır. $\\sum_{k=1}^{n} a_k$ ifadesi, $k$ yı $1$ den $n$ ye kadar değiştirerek $a_k$ terimlerinin toplanacağını söyler.",
            tablo(["Toplam", "Formül"], [
                ["$\\sum_{k=1}^{n} k$", "$\\dfrac{n(n+1)}{2}$"],
                ["$\\sum_{k=1}^{n} k^2$", "$\\dfrac{n(n+1)(2n+1)}{6}$"],
                ["$\\sum_{k=1}^{n} (2k-1)$", "$n^2$"],
            ]),
            ornek(
                "$\\sum_{k=1}^{10} k$ ve $\\sum_{k=1}^{5} k^2$ toplamları verilsin.",
                "Değerlerini bulalım.",
                "Birincisi $\\dfrac{10 \\cdot 11}{2}=55$ olur.",
                "İkincisi $\\dfrac{5 \\cdot 6 \\cdot 11}{6}=55$ olur; iki toplam aynı çıkar."),
        ]},
        {"baslik": "Toplam sembolünün özellikleri", "icerik": [
            "Toplam sembolü toplama ve sabitle çarpmaya dağılır. Sabit bir sayının $n$ kez toplamı $n$ ile çarpımıdır:",
            tablo(["Özellik", "Formül"], [
                ["Toplama dağılma", "$\\sum (a_k+b_k)=\\sum a_k+\\sum b_k$"],
                ["Sabitle çarpma", "$\\sum c \\cdot a_k=c\\sum a_k$"],
                ["Sabitin toplamı", "$\\sum_{k=1}^{n} c=n \\cdot c$"],
            ]),
            ornek(
                "$\\sum_{k=1}^{20} (3k+2)$ toplamı verilsin.",
                "Değerini bulalım.",
                "$3\\sum_{k=1}^{20} k+\\sum_{k=1}^{20} 2=3 \\cdot 210+40$ olur.",
                "Sonuç $670$ tir."),
        ]},
        {"baslik": "Kısmi toplamdan genel terim", "icerik": [
            "Dizinin ilk $n$ teriminin toplamına $n$ inci kısmi toplam denir ve $S_n$ ile gösterilir. $S_n$ biliniyorsa genel terim iki ardışık kısmi toplamın farkıdır: $a_n=S_n-S_{n-1}$. İlk terim ise doğrudan $a_1=S_1$ dir.",
            ornek(
                "Bir dizinin ilk $n$ teriminin toplamı $S_n=n^2+2n$ olsun.",
                "Genel terimi bulalım.",
                "$a_n=(n^2+2n)-((n-1)^2+2(n-1))=2n+1$ olur.",
                "Kontrol: $a_1=S_1=3$ ve formülden $2 \\cdot 1+1=3$; formül ilk terim için de geçerlidir."),
            hap("$a_n=S_n-S_{n-1}$ olur; ilk terim ise doğrudan $a_1=S_1$ ile bulunur."),
        ]},
        {"baslik": "Periyodik diziler", "icerik": [
            "Terimleri belirli aralıklarla tekrar eden dizilere periyodik dizi denir. Böyle bir dizinin çok ileri bir terimi, sıra numarasının periyoda bölümünden kalana bakılarak bulunur.",
            ornek(
                "Bir dizide $a_1=2$, $a_2=5$, $a_3=7$ ve her $n$ için $a_{n+3}=a_n$ olsun.",
                "$a_{100}$ terimini bulalım.",
                "Dizi üç terimde bir tekrar eder; $100$ ün $3$ e bölümünden kalan $1$ dir.",
                "Bu yüzden $a_{100}=a_1=2$ olur."),            "Aynı yolla $50$ nin $3$ e bölümünden kalan $2$ olduğundan $a_{50}=a_2=5$ bulunur. Kalan $0$ olduğunda ise terim, periyodun son terimi olan $a_3$ e eşittir.",
        ]},
        {"baslik": "Üçgensel sayılar", "icerik": [
            "Kapaktaki desenler üçgensel sayılar dizisini oluşturur. $n$ inci desende $1$ den $n$ ye kadar sıralar vardır; bu yüzden terim, ilk $n$ pozitif tam sayının toplamıdır:",
            "$$T_n=\\dfrac{n(n+1)}{2}$$",
            ornek(
                "Üçgensel sayılar dizisi verilsin.",
                "Beşinci ve onuncu terimi bulalım.",
                "$T_5=\\dfrac{5 \\cdot 6}{2}=15$ olur; kapaktaki boş bölmeye $15$ üçgen gelir.",
                "$T_{10}=\\dfrac{10 \\cdot 11}{2}=55$ olur."),
            "Ardışık iki üçgensel sayının farkı sıra numarasına eşittir: $T_n-T_{n-1}=n$. Yani her yeni desen bir öncekine $n$ üçgenlik bir sıra eklenerek oluşur.",
            hap("Bowlingde lobutlar üçgen biçiminde dizilir.", "Dört sıralık dizilişte $1+2+3+4=10$ lobut vardır; bu sayı dördüncü üçgensel sayı olan $T_4=10$ değeridir.", gunluk=True),
        ]},
        {"baslik": "Aritmetik ve geometrik diziler", "icerik": [
            "En sık kullanılan iki dizi türü, her adımda aynı sayının eklendiği aritmetik diziler ile her adımda aynı sayıyla çarpılan geometrik dizilerdir. $3, 7, 11, 15, \\ldots$ aritmetik, $3, 6, 12, 24, \\ldots$ ise geometrik bir dizidir.",
            "Bu iki dizi türünün genel terimleri, toplam formülleri ve uygulamaları ayrı yazılarda ayrıntılı olarak anlatılıyor: <a href=\"/blog/aritmetik-dizi/\">Aritmetik Dizi Konu Anlatımı</a> ve <a href=\"/blog/geometrik-dizi/\">Geometrik Dizi Konu Anlatımı</a>.",
        ]},
        {"baslik": "Sınavda diziler", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) diziler; genel terimden terim bulma, dizi olma koşulu, sabit dizi, artan ve azalan dizi, indirgemeli diziler ve toplam sembolü biçiminde karşına çıkabilir.",
                "Aritmetik ve geometrik diziler bu konunun devamıdır ve en çok soru bu iki türden gelir."),
            "Dizi sorusunda önce genel terimin ne olduğunu belirle. Terimler verilmişse sıra numarasıyla ilişkiyi ara; indirgemeli bir tanım varsa ilk birkaç terimi yazıp bir kural görmeye çalış.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$a_{n+1}$ i $a_n+1$ sanmak", "$n$ yerine $n+1$ yazılır"],
                ["Dizi olma koşulunda yalnız $n=1$ i denemek", "Her pozitif tam sayı denenir"],
                ["Kaçıncı terim sorusunda kesirli $n$ kabul etmek", "$n$ pozitif tam sayı olmalı"],
                ["$a_n=S_n-S_{n-1}$ formülünü $n=1$ için kullanmak", "$a_1=S_1$"],
                ["Toplam sembolünde sabiti bir kez saymak", "Sabit $n$ kez toplanır"],
                ["Birkaç terimden kesin kural çıkarmak", "En basit kural beklenir"],
            ]),
            "Özellikle $a_{n+1}$ ile $a_n+1$ farkı çok sık karıştırılır. $a_n=n^2$ için $a_{n+1}=(n+1)^2$ dir; $a_n+1$ ise $n^2+1$ dir ve bu ikisi farklıdır.",
        ]},
    ],
    "sss": [
        ("Dizi nedir?",
         "Belirli bir kurala göre sıralanmış sayılardır. Matematikte dizi, tanım kümesi pozitif tam sayılar olan bir fonksiyondur."),
        ("Genel terim nedir?",
         "Dizinin n inci terimini veren ifadedir ve a n ile gösterilir. n yerine sıra numarası yazılarak istenen terim bulunur."),
        ("Bir ifadenin dizi olup olmadığı nasıl anlaşılır?",
         "İfade her pozitif tam sayı için tanımlı olmalıdır. Paydayı sıfır yapan ya da kök içini negatif yapan bir pozitif tam sayı varsa ifade dizi değildir."),
        ("Artan dizi nasıl anlaşılır?",
         "Ardışık iki terimin farkı a n+1 eksi a n her n için pozitifse dizi artandır, negatifse azalandır."),
        ("İndirgemeli dizi nedir?",
         "Her terimi bir önceki terim ya da terimler yardımıyla tanımlanan dizidir. Fibonacci dizisi en bilinen örnektir."),
        ("Kısmi toplamdan genel terim nasıl bulunur?",
         "Genel terim ardışık iki kısmi toplamın farkıdır: a n eşittir S n eksi S n-1. İlk terim ise S 1 e eşittir."),
    ],
    "kontrol": [
        "Dizinin pozitif tam sayılarda tanımlı bir fonksiyon olduğunu açıklayabiliyorum.",
        "Genel terimden istenen terimi bulabiliyorum.",
        "Terimlerden genel terimi tahmin edebiliyorum.",
        "Bir ifadenin dizi olup olmadığını belirleyebiliyorum.",
        "Bir sayının dizinin kaçıncı terimi olduğunu bulabiliyorum.",
        "Sabit, artan ve azalan dizileri tanıyabiliyorum.",
        "İndirgemeli dizilerin terimlerini hesaplayabiliyorum.",
        "Dizilerde eşitlik ve işlemleri kullanabiliyorum.",
        "Toplam sembolünü ve özelliklerini kullanabiliyorum.",
        "Kısmi toplamdan genel terimi bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["aritmetik-dizi", "geometrik-dizi", "fonksiyonlar-konu-anlatimi"],
}
