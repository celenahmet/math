# scripts/yazilar/91_basamak_degeri.py — Basamak Degeri ve Cozumleme (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "basamak-degeri-ve-cozumleme",
    "baslik": "Basamak Değeri ve Çözümleme",
    "aciklama": "Basamak değeri ve sayı değeri nedir? Çözümleme, harfli sayılar, rakam ekleme ve değiştirme, rakamlar toplamı ile 9 ilişkisi ve tabanlar; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "basamak-degeri-ve-cozumleme",
    "kapak_alt": "Basamak değeri ve çözümleme: yüzlük kareleri, onluk çubukları ve birlik küpleri ayrı kutulara yerleştiren öğrenci",
    "ozet": "Aynı rakam farklı basamaklarda farklı değerler taşır: yedi rakamı birler basamağında yedi, onlar basamağında yetmiş, yüzler basamağında yedi yüz demektir. Bu fikir onluk sayı sisteminin temelidir ve rakamlarla ilgili bütün soruların çözüm anahtarıdır. Bu yazıda basamak değeri ile sayı değerini, çözümlemeyi, harflerle yazılan sayıları, bir sayıya rakam eklemeyi ve rakam değiştirmeyi, bir sayı ile rakamlarının toplamı arasındaki dokuz ilişkisini ve farklı tabanlardaki sayıları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Sayı değeri ve basamak değeri", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için basamak adlarını ve onun kuvvetlerini biliyor olman yeterli.",
                "Basamak adları için <a href=\"/blog/sayi-basamaklari-konu-anlatimi-pdf/\">Sayı Basamakları Konu Anlatımı PDF</a> yazısına göz at."),
            "Bir rakamın kendi değerine <strong>sayı değeri</strong>, bulunduğu basamak nedeniyle aldığı değere <strong>basamak değeri</strong> denir. Sayı değeri basamaktan bağımsızdır; basamak değeri ise rakamın bulunduğu basamağın değeriyle çarpımıdır. Aynı rakam bir sayıda birden fazla kez geçebilir ve her seferinde farklı bir basamak değeri alır.",
            ornek(
                "$4572$ sayısı verilsin.",
                "Her rakamın sayı değerini ve basamak değerini bulalım.",
                "$4$: sayı değeri $4$, binler basamağında olduğu için basamak değeri $4000$.",
                "$5$: sayı değeri $5$, basamak değeri $500$. $7$: sayı değeri $7$, basamak değeri $70$.",
                "$2$: sayı değeri $2$, basamak değeri $2$. Birler basamağında sayı değeri ile basamak değeri aynıdır."),
            tablo(["Rakam", "Basamak", "Sayı değeri", "Basamak değeri"], [
                ["$4$", "Binler", "$4$", "$4000$"],
                ["$5$", "Yüzler", "$5$", "$500$"],
                ["$7$", "Onlar", "$7$", "$70$"],
                ["$2$", "Birler", "$2$", "$2$"],
            ]),
            hap("Sayı değeri rakamın kendisidir; basamak değeri bulunduğu basamağa göre değişir.",
                "Basamak değeri, rakam ile basamağın değerinin çarpımıdır."),
        ]},
        {"baslik": "Çözümleme", "icerik": [
            "Bir sayıyı rakamlarının basamak değerlerinin toplamı olarak yazmaya <strong>çözümleme</strong> denir. Çözümleme, sayının yapısını açıkça gösterir ve rakamlarla ilgili soruları denkleme çevirmeyi sağlar. Bu yazıdaki soruların neredeyse hepsi, ilk adımda sayıyı çözümlemekle başlar.",
            "$$4572=4 \\cdot 1000+5 \\cdot 100+7 \\cdot 10+2$$",
            "Aynı çözümleme onun kuvvetleriyle de yazılabilir: $4572=4 \\cdot 10^3+5 \\cdot 10^2+7 \\cdot 10+2$. Her basamak bir öncekinin $10$ katı olduğu için bu sisteme <strong>onluk sistem</strong> denir.",
            ornek(
                "$30\\,405$ sayısı verilsin.",
                "Sayıyı çözümleyelim.",
                "Rakamlar ve basamaklar: $3$ on binler, $0$ binler, $4$ yüzler, $0$ onlar, $5$ birler.",
                "Çözümleme: $30\\,405=3 \\cdot 10000+4 \\cdot 100+5$.",
                "Basamak değeri $0$ olan terimler yazılmayabilir ama o basamakların varlığı sayının değerini belirler."),
            dikkat(
                "Aradaki sıfırları görmezden gelmek.",
                "$30\\,405$ sayısındaki sıfırlar yazılmasa sayı $345$ olurdu. Sıfır kendi başına bir değer taşımaz ama diğer rakamları doğru basamakta tutar."),
        ]},
        {"baslik": "Harflerle yazılan sayılar", "icerik": [
            "Rakamları harflerle gösterilen sayılar çözümlenerek cebirsel ifadeye çevrilir. $AB$ yazılışı $A$ ile $B$ nin çarpımı değil, onlar basamağı $A$, birler basamağı $B$ olan iki basamaklı sayıdır.",
            tablo(["Sayı", "Çözümlenmiş hâli"], [
                ["$AB$", "$10A+B$"],
                ["$ABC$", "$100A+10B+C$"],
                ["$ABCD$", "$1000A+100B+10C+D$"],
                ["$AAA$", "$111A$"],
            ]),
            "Son satır sık kullanılan bir kalıptır: bütün rakamları aynı olan üç basamaklı bir sayı, o rakamın $111$ katıdır. Örneğin $777=7 \\cdot 111$ dir.",
            dikkat(
                "Harfli sayıyı çarpım sanmak.",
                "$AB$ yazılışı $A \\cdot B$ değildir. $A=4$ ve $B=7$ için $AB$ sayısı $47$ dir, $28$ değil."),
        ]},
        {"baslik": "Çözümlemeyle denklem kurmak", "icerik": [
            "Rakamları arasındaki bir ilişkisi verilen sayılar, çözümlenerek denkleme çevrilir. Rakamların $0$ ile $9$ arasında tam sayı olduğu ve en soldaki rakamın $0$ olamayacağı çözüm aşamasında kullanılır.",
            ornek(
                "İki basamaklı bir $AB$ sayısı, rakamları toplamının $4$ katına eşittir.",
                "Bu koşulu sağlayan sayıları bulalım.",
                "Denklem: $10A+B=4(A+B)$, yani $10A+B=4A+4B$ ve $6A=3B$. Buradan $B=2A$.",
                "$B$ bir rakam olduğu için $2A \\leq 9$, yani $A$ en fazla $4$ tür.",
                "Sayılar: $12$, $24$, $36$ ve $48$. Kontrol: $48=4 \\cdot 12$ ve $4+8=12$."),
            ornek(
                "Üç basamaklı bir $ABC$ sayısında $A=2C$ ve $B=A+C$ dir. Sayının rakamları toplamı $12$ dir.",
                "Sayıyı bulalım.",
                "$A=2C$ ve $B=3C$ yazalım: $A+B+C=2C+3C+C=6C=12$.",
                "$C=2$, $A=4$, $B=6$. Sayı $462$ dir. Kontrol: $4=2 \\cdot 2$, $6=4+2$ ve $4+6+2=12$."),
        ]},
        {"baslik": "Basamak değerleri toplamı ve farkı", "icerik": [
            "Bir rakam bir sayıda birden fazla kez geçiyorsa her birinin basamak değeri ayrı ayrı hesaplanır. Soruda bu değerlerin toplamı ya da farkı istenebilir.",
            ornek(
                "$5125$ sayısı verilsin.",
                "$5$ rakamlarının basamak değerleri toplamını ve farkını bulalım.",
                "Binler basamağındaki $5$ in basamak değeri $5000$, birler basamağındaki $5$ inki $5$ tir.",
                "Toplam: $5000+5=5005$.",
                "Fark: $5000-5=4995$."),
            "Aynı rakamın sayı değerleri ise her zaman aynıdır: iki $5$ in sayı değerleri farkı $0$ dır. Sorunun sayı değerini mi basamak değerini mi istediğine dikkat etmek gerekir.",
        ]},
        {"baslik": "Bir sayıya rakam eklemek", "icerik": [
            "Bir sayının sağına bir rakam yazmak, sayıyı $10$ ile çarpıp o rakamı eklemek demektir. Soluna bir rakam yazmak ise sayıya o rakamın yeni basamaktaki değerini eklemektir.",
            tablo(["İşlem", "Sonuç"], [
                ["$x$ in sağına $5$ yazmak", "$10x+5$"],
                ["İki basamaklı $x$ in soluna $3$ yazmak", "$300+x$"],
                ["$x$ in sağına iki sıfır yazmak", "$100x$"],
            ]),
            ornek(
                "İki basamaklı bir sayının sağına $7$ yazılınca sayı $520$ artıyor.",
                "Sayıyı bulalım.",
                "Sayı $x$ olsun. Yeni sayı $10x+7$: $10x+7=x+520$.",
                "$9x=513$, yani $x=57$.",
                "Kontrol: $577-57=520$."),
        ]},
        {"baslik": "Bir rakamı değiştirmek", "icerik": [
            "Bir sayının bir rakamı değiştirildiğinde sayı, o rakamdaki değişimin basamak değeri kadar değişir. Onlar basamağındaki rakam $3$ artırılırsa sayı $30$, yüzler basamağındaki rakam $2$ azaltılırsa sayı $200$ değişir.",
            ornek(
                "Üç basamaklı bir sayının yüzler basamağındaki rakam $2$ artırılıyor, birler basamağındaki rakam $5$ azaltılıyor.",
                "Sayının nasıl değiştiğini bulalım.",
                "Yüzler basamağındaki artış: $2 \\cdot 100=200$.",
                "Birler basamağındaki azalış: $5 \\cdot 1=5$.",
                "Sayı $200-5=195$ artar. Örneğin $316$ sayısı bu iki değişiklikle $511$ olur ve $511-316=195$."),
            "Bu tür sorularda sayının kendisini bilmeye gerek yoktur; yalnızca değişimlerin basamak değerleri toplanır. Rakam değişiminin mümkün olması için yeni rakamların da $0$ ile $9$ arasında kalması gerekir. Örneğin birler basamağı $3$ olan bir sayıda bu rakam $5$ azaltılamaz.",
        ]},
        {"baslik": "Üç basamaklı sayılarda rakamların yer değiştirmesi", "icerik": [
            "Üç basamaklı $ABC$ sayısı ile rakamlarının sırası ters çevrilmiş $CBA$ sayısının farkı çözümlemeyle hesaplanır: $(100A+10B+C)-(100C+10B+A)=99A-99C$, yani $99(A-C)$ dir. Ortadaki rakam farkta hiç rol oynamaz.",
            ornek(
                "$ABC$ ve $CBA$ üç basamaklı sayılar olmak üzere $ABC-CBA=396$ olsun.",
                "$A-C$ farkını ve bu koşulu sağlayan kaç $ABC$ sayısı olduğunu bulalım.",
                "$99(A-C)=396$, yani $A-C=4$.",
                "$CBA$ üç basamaklı olduğu için $C$ en az $1$ dir. $A=C+4$ olduğundan $C$ için $1$ den $5$ e kadar $5$ değer vardır.",
                "$B$ için $10$ değer vardır. Toplam $5 \\cdot 10=50$ sayı."),
            "<h3>Döngüsel toplam</h3>",
            "Rakamları döngüsel olarak kaydırılan üç sayının toplamı da sade bir sonuç verir: $ABC+BCA+CAB=111(A+B+C)$. Örneğin $123+231+312=666$ ve $666=111 \\cdot 6$ dır.",
        ]},
        {"baslik": "Harfli sayılarda bölünebilme", "icerik": [
            "Bir rakamı harfle verilen sayının belirli bir sayıya bölünmesi isteniyorsa, bölünebilme kuralı çözümlenmiş ifadeye ya da rakamlar toplamına uygulanır.",
            ornek(
                "$4A7$ üç basamaklı bir sayıdır.",
                "Sayının $9$ a ve $3$ e bölünmesi için $A$ nın alabileceği değerleri bulalım.",
                "Rakamlar toplamı: $4+A+7=11+A$.",
                "$9$ a bölünme: $11+A$ nın $9$ un katı olması gerekir. $A$ bir rakam olduğundan $11+A=18$ ve $A=7$.",
                "$3$ e bölünme: $11+A$ değeri $12$, $15$ ya da $18$ olabilir; $A$ için $1$, $4$ ve $7$ değerleri bulunur."),
        ]},
        {"baslik": "En büyük ve en küçük değer soruları", "icerik": [
            "Çözümlenmiş bir ifadenin en büyük ya da en küçük değeri sorulduğunda, ifadedeki harflere rakam kısıtları içinde en uygun değerler verilir.",
            ornek(
                "$AB$ ve $BA$ iki basamaklı sayılar olsun.",
                "$AB-BA$ farkının alabileceği en büyük değeri bulalım.",
                "$AB-BA=9(A-B)$. Farkın en büyük olması için $A-B$ en büyük olmalıdır.",
                "$BA$ iki basamaklı olduğu için $B$ en az $1$ dir. $A=9$ ve $B=1$ seçilir: $A-B=8$.",
                "En büyük fark $9 \\cdot 8=72$ dir. Kontrol: $91-19=72$."),
        ]},
        {"baslik": "Rakamları ters çevrilen sayı problemi", "icerik": [
            "Bir sayının rakamlarının yeri değiştirilince ne kadar arttığı ya da azaldığı ve rakamların toplamı birlikte verildiğinde, iki bilgi iki denkleme dönüşür.",
            ornek(
                "İki basamaklı bir sayının rakamlarının yeri değiştirilince sayı $36$ artıyor. Sayının rakamları toplamı $10$ dur.",
                "Sayıyı bulalım.",
                "Sayı $AB$, yeni sayı $BA$ olsun: $(10B+A)-(10A+B)=9(B-A)=36$, yani $B-A=4$.",
                "$A+B=10$ ve $B-A=4$: $B=7$, $A=3$.",
                "Sayı $37$ dir. Kontrol: $73-37=36$ ve $3+7=10$."),
        ]},
        {"baslik": "Yuvarlama ve basamak değeri", "icerik": [
            "Bir sayıyı belirli bir basamağa yuvarlamak, o basamaktan sağdaki rakamları sıfırlamak ve gerekirse o basamağı bir artırmaktır. Karar, yuvarlanan basamağın hemen sağındaki rakama göre verilir: bu rakam $5$ ya da daha büyükse basamak bir artar.",
            ornek(
                "$4572$ sayısı verilsin.",
                "Sayıyı onlar, yüzler ve binler basamağına yuvarlayalım.",
                "Onlara: sağdaki rakam $2$, $5$ ten küçük; sonuç $4570$.",
                "Yüzlere: sağdaki rakam $7$, $5$ ten büyük; sonuç $4600$.",
                "Binlere: sağdaki rakam $5$; sonuç $5000$."),
            "Yuvarlama, sayının yaklaşık değerini verir ve tahmin yaparken kullanılır. Yuvarlanan basamağın basamak değeri, yapılan hatanın en fazla ne kadar olabileceğini de gösterir: yüzlere yuvarlanan bir sayı gerçek değerinden en fazla $50$ uzaktadır.",
        ]},
        {"baslik": "Onluk sistemin mantığı ve eldeli işlemler", "icerik": [
            "Onluk sistemde her basamaktaki $10$ birim, bir üst basamakta $1$ birim eder: $10$ birlik bir onluk, $10$ onluk bir yüzlük, $10$ yüzlük bir binliktir. Kapaktaki birlik küpler, onluk çubuklar ve yüzlük kareler bu düzeni somut olarak gösterir.",
            "Toplamada bir basamakta $10$ ya da daha fazla birim oluşursa $10$ u bir üst basamağa <strong>elde</strong> olarak aktarılır. Çıkarmada bir basamakta yeterli birim yoksa üst basamaktan bir birim <strong>bozulur</strong> ve $10$ birim olarak alınır.",
            ornek(
                "$47+38$ ve $52-27$ işlemleri verilsin.",
                "Basamak mantığıyla sonuçları bulalım.",
                "Toplama: birler $7+8=15$; $10$ u bir onluk olarak ele alınır, birlerde $5$ kalır. Onlar $4+3+1=8$. Sonuç $85$.",
                "Çıkarma: birlerde $2$ den $7$ çıkmaz; bir onluk bozulur ve birler $12$ olur. $12-7=5$, onlar $4-2=2$. Sonuç $25$."),
        ]},
        {"baslik": "Sayı ile rakamları toplamı arasındaki ilişki", "icerik": [
            "Bir sayıdan rakamlarının toplamı çıkarıldığında sonuç her zaman $9$ un katıdır. Nedeni çözümlemede gizlidir: $10-1=9$, $100-1=99$, $1000-1=999$ sayılarının hepsi $9$ un katıdır.",
            ornek(
                "$4572$ sayısı verilsin.",
                "Sayı ile rakamları toplamının farkını bulalım ve $9$ a bölünüp bölünmediğine bakalım.",
                "Rakamlar toplamı: $4+5+7+2=18$.",
                "Fark: $4572-18=4554$.",
                "$4554=9 \\cdot 506$; fark $9$ un katıdır."),
            "Genel olarak $ABC-(A+B+C)=99A+9B$ dir ve bu ifade $9$ un katıdır. Bu yüzden bir sayı $9$ a bölündüğünde verdiği kalan, rakamları toplamının $9$ a bölümünden kalana eşittir. $9$ a bölünebilme kuralının nedeni budur. Kuralların ayrıntısı <a href=\"/blog/bolunebilme-kurallari-konu-anlatimi-pdf/\">Bölünebilme Kuralları Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Ondalık sayılarda basamak değeri", "icerik": [
            "Basamak değeri fikri virgülün sağına doğru da devam eder. Virgülün hemen sağındaki basamak onda birler, sonraki yüzde birler, sonraki binde birler basamağıdır. Her basamak yine solundakinin onda biri kadardır.",
            ornek(
                "$3.472$ sayısı verilsin.",
                "$4$, $7$ ve $2$ rakamlarının basamak değerlerini bulalım.",
                "$4$ onda birler basamağında: $0.4$.",
                "$7$ yüzde birler basamağında: $0.07$. $2$ binde birler basamağında: $0.002$.",
                "Çözümleme: $3.472=3+0.4+0.07+0.002$."),
            "Ondalık sayıların ayrıntısı <a href=\"/blog/ondalik-gosterim-konu-anlatimi-pdf/\">Ondalık Gösterim Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Farklı tabanlarda sayılar", "icerik": [
            "Onluk sistemde her basamak bir öncekinin $10$ katıdır. Aynı fikir başka sayılarla da kurulabilir: ikilik sistemde her basamak bir öncekinin $2$ katıdır ve yalnızca $0$ ile $1$ rakamları kullanılır. Bilgisayarlar bilgiyi bu sistemle saklar.",
            ornek(
                "İkilik tabanda yazılmış $1011_2$ sayısı ile beşlik tabanda yazılmış $23_5$ sayısı verilsin.",
                "Bu sayıları onluk tabanda yazalım.",
                "$1011_2=1 \\cdot 2^3+0 \\cdot 2^2+1 \\cdot 2+1=8+0+2+1=11$.",
                "$23_5=2 \\cdot 5+3=13$."),
            "Farklı tabanlar, basamak değerinin onluk sisteme özgü olmadığını gösterir: taban ne olursa olsun, bir rakamın değeri rakam ile bulunduğu basamağın değerinin çarpımıdır. Onluk sistemin günlük hayatta kullanılması, ellerimizde on parmak olmasıyla ilişkilendirilir.",
        ]},
        {"baslik": "Sınavda basamak değeri ve çözümleme", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu harfli sayıların çözümlenmesi, rakamlar arasındaki ilişkilerden sayı bulma, rakam ekleme ve değiştirme soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de rakamlarla ilgili sayı problemlerinin temelini çözümleme oluşturur."),
            "Rakamları harflerle verilen bir soruda ilk adım her zaman çözümlemedir. Denklem kurulduktan sonra rakamların $0$ ile $9$ arasında tam sayı olduğu ve en soldaki rakamın $0$ olamayacağı kısıtları uygulanır. Bu kısıtlar çoğu zaman sonsuz çözümü birkaç sayıya indirir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$AB$ yi $A \\cdot B$ sanmak", "$AB=10A+B$"],
                ["Sayı değeri ile basamak değerini karıştırmak", "Basamak değeri, rakam çarpı basamak"],
                ["Aradaki sıfırları yok saymak", "Sıfır basamağı tutar"],
                ["Sağa rakam yazmayı toplama sanmak", "$x$ in sağına $5$: $10x+5$"],
                ["Rakam kısıtlarını unutmak", "Rakam $0$ ile $9$ arasında"],
                ["En soldaki rakama $0$ vermek", "En soldaki rakam $0$ olamaz"],
            ]),
            "Bu hataların çoğu, bir rakamın konumunun değerini belirlediğini unutmaktan doğar. Her harfli sayıyı ilk iş olarak çözümlemek, hataların büyük bölümünü baştan önler.",
        ]},
    ],
    "sss": [
        ("Sayı değeri ile basamak değeri arasındaki fark nedir?",
         "Sayı değeri rakamın kendi değeridir ve basamaktan bağımsızdır. Basamak değeri ise rakamın bulunduğu basamağın değeriyle çarpımıdır."),
        ("Çözümleme nedir?",
         "Bir sayıyı rakamlarının basamak değerlerinin toplamı olarak yazmaktır. Örneğin 4572, 4 çarpı 1000 artı 5 çarpı 100 artı 7 çarpı 10 artı 2 dir."),
        ("AB sayısı nasıl çözümlenir?",
         "Onlar basamağı A, birler basamağı B olan iki basamaklı sayı 10A artı B olarak yazılır. AB, A ile B nin çarpımı değildir."),
        ("Bir sayının sağına rakam yazılınca ne olur?",
         "Sayı 10 ile çarpılır ve yazılan rakam eklenir. 57 nin sağına 7 yazılınca 577 olur, yani 10 çarpı 57 artı 7."),
        ("Bir sayıdan rakamları toplamı çıkarılınca neden 9 un katı çıkar?",
         "Çünkü her basamağın değeri ile 1 arasındaki fark, yani 9, 99, 999 gibi sayılar, 9 un katıdır. Bu yüzden 9 a bölünebilme kuralı rakamlar toplamına bakar."),
        ("İkilik tabandaki bir sayı onluk tabana nasıl çevrilir?",
         "Her rakam, bulunduğu basamağa karşılık gelen 2 nin kuvvetiyle çarpılır ve sonuçlar toplanır. 1011 ikilik sayısı onluk tabanda 11 dir."),
        ("ABC ile CBA sayılarının farkı neden 99 un katıdır?",
         "Çözümlendiğinde fark 99A eksi 99C olur. Ortadaki rakam iki sayıda da aynı basamakta olduğu için farkta yok olur."),
        ("Bir rakamın basamak değerleri farkı nasıl bulunur?",
         "Rakamın geçtiği her basamaktaki değeri ayrı ayrı yazılır ve çıkarılır. 5125 sayısındaki iki 5 in basamak değerleri farkı 5000 eksi 5, yani 4995 tir."),
        ("Bir sayı yüzlere nasıl yuvarlanır?",
         "Onlar basamağındaki rakama bakılır. Bu rakam 5 ya da daha büyükse yüzler basamağı bir artırılır, sonra onlar ve birler basamakları sıfır yapılır."),
    ],
    "kontrol": [
        "Sayı değeri ile basamak değerini ayırt edebiliyorum.",
        "Bir sayıyı basamak değerleriyle çözümleyebiliyorum.",
        "Sayıyı onun kuvvetleriyle çözümleyebiliyorum.",
        "Aradaki sıfırların sayının değerindeki rolünü açıklayabiliyorum.",
        "Harflerle yazılan sayıları cebirsel ifadeye çevirebiliyorum.",
        "Rakamlar arasındaki ilişkilerden sayı bulabiliyorum.",
        "Bir sayıya rakam eklenince oluşan sayıyı yazabiliyorum.",
        "Bir rakam değişince sayının ne kadar değiştiğini hesaplayabiliyorum.",
        "Sayı ile rakamları toplamı arasındaki 9 ilişkisini açıklayabiliyorum.",
        "İkilik ve beşlik tabandaki sayıları onluk tabana çevirebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["sayi-basamaklari-konu-anlatimi-pdf", "bolunebilme-kurallari-konu-anlatimi-pdf", "ondalik-gosterim-konu-anlatimi-pdf"],
}
