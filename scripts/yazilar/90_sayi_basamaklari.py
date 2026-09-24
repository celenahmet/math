# scripts/yazilar/90_sayi_basamaklari.py — Sayi Basamaklari (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "sayi-basamaklari-konu-anlatimi-pdf",
    "baslik": "Sayı Basamakları Konu Anlatımı PDF",
    "aciklama": "Sayı basamakları konu anlatımı: rakam ve sayı, basamak adları, n basamaklı sayıların adedi, rakamları farklı sayılar, rakam toplamı ve sayfa numarası soruları.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "sayi-basamaklari-konu-anlatimi-pdf",
    "kapak_alt": "Sayı basamakları: birlik küpler, onluk çubuklar ve yüzlük karelerle basamakları modelleyen iki öğrenci",
    "ozet": "Sayılar on rakamla yazılır ve her rakamın değeri bulunduğu basamağa göre değişir. Sayı basamakları konusu, bu düzenin sonuçlarını inceler: belirli sayıda basamağı olan kaç sayı vardır, rakamları farklı sayılar nasıl sayılır, verilen rakamlarla hangi sayılar yazılabilir, rakamların yeri değişince sayı nasıl değişir ve bir kitabın sayfalarını numaralamak için kaç rakam gerekir. Bu yazıda bu soruların hepsini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Rakam ve sayı", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için doğal sayıları ve basit sayma işlemini biliyor olman yeterli.",
                "Sayı kümeleri için <a href=\"/blog/dogal-sayilar-ve-tam-sayilar/\">Doğal Sayılar ve Tam Sayılar</a> yazısına göz at."),
            "Sayıları yazmak için kullanılan on sembole <strong>rakam</strong> denir: $0$, $1$, $2$, $3$, $4$, $5$, $6$, $7$, $8$ ve $9$. <strong>Sayı</strong> ise bu rakamlarla yazılan ve bir çokluk belirten ifadedir. Her rakam aynı zamanda tek basamaklı bir sayıdır, ama her sayı bir rakam değildir: $47$ bir sayıdır ve iki rakamdan oluşur.",
            "Rakamlar arasındaki en önemli ayrım $0$ ile ilgilidir. $0$ bir sayının başına yazılamaz: $047$ üç basamaklı bir sayı değil, $47$ sayısıdır. Bu yüzden sayma sorularında en soldaki basamağa $0$ gelemeyeceği her zaman ayrıca hesaba katılır.",
            hap("On rakam vardır: $0$ dan $9$ a kadar.",
                "En soldaki basamak $0$ olamaz."),
        ]},
        {"baslik": "Basamak adları", "icerik": [
            "Bir sayının rakamlarının her biri bir basamakta durur. Basamaklar sağdan sola doğru birler, onlar, yüzler, binler, on binler, yüz binler diye adlandırılır. Okumayı kolaylaştırmak için basamaklar sağdan sola üçer üçer gruplanır; bu gruplara <strong>bölük</strong> denir.",
            tablo(["Bölük", "Basamaklar"], [
                ["Birler bölüğü", "Birler, onlar, yüzler"],
                ["Binler bölüğü", "Binler, on binler, yüz binler"],
                ["Milyonlar bölüğü", "Milyonlar, on milyonlar, yüz milyonlar"],
            ]),
            "Örneğin $4\\,572\\,309$ sayısında $9$ birler, $0$ onlar, $3$ yüzler, $2$ binler, $7$ on binler, $5$ yüz binler, $4$ milyonlar basamağındadır. Bir rakamın bulunduğu basamağa göre aldığı değer <a href=\"/blog/basamak-degeri-ve-cozumleme/\">Basamak Değeri ve Çözümleme</a> yazısında ayrıntılı olarak anlatılıyor.",
        ]},
        {"baslik": "Belirli basamak sayısındaki sayıların adedi", "icerik": [
            "Ardışık tam sayıların sayısı, son sayıdan ilk sayının çıkarılıp $1$ eklenmesiyle bulunur. Bu kural, belirli basamak sayısına sahip sayıları saymak için kullanılır.",
            tablo(["Basamak sayısı", "En küçük", "En büyük", "Adet"], [
                ["$1$", "$1$", "$9$", "$9$"],
                ["$2$", "$10$", "$99$", "$90$"],
                ["$3$", "$100$", "$999$", "$900$"],
                ["$4$", "$1000$", "$9999$", "$9000$"],
            ]),
            "Tablodaki düzen genel bir kural verir: $n$ basamaklı doğal sayıların sayısı $9 \\cdot 10^{n-1}$ dir. En soldaki basamak için $9$ seçenek vardır, çünkü $0$ gelemez; diğer her basamak için $10$ seçenek vardır.",
            ornek(
                "İki basamaklı sayılar verilsin.",
                "Kaç tane olduklarını iki yolla bulalım.",
                "Birinci yol: $99-10+1=90$.",
                "İkinci yol: onlar basamağına $9$, birler basamağına $10$ rakam gelebilir: $9 \\cdot 10=90$."),
            dikkat(
                "Ardışık sayıları sayarken $1$ eklemeyi unutmak.",
                "$10$ dan $99$ a kadar olan sayıların sayısı $99-10=89$ değil, $90$ dır. Hem ilk hem son sayı sayıldığı için fark $1$ artırılır."),
        ]},
        {"baslik": "En büyük ve en küçük sayılar", "icerik": [
            "$n$ basamaklı en küçük sayı $1$ ile başlayıp $0$ larla devam eder: $10^{n-1}$. En büyük sayı ise bütün basamakları $9$ olan sayıdır: $10^n-1$. Rakamların farklı olması istendiğinde ise en küçük ve en büyük sayılar değişir.",
            ornek(
                "Rakamları birbirinden farklı üç basamaklı sayılar verilsin.",
                "Bu sayıların en küçüğünü ve en büyüğünü bulalım.",
                "En küçük: yüzler basamağına en küçük sıfırdan farklı rakam $1$, sonra en küçük kullanılmamış rakamlar $0$ ve $2$ gelir: $102$.",
                "En büyük: büyükten küçüğe $9$, $8$, $7$: $987$.",
                "Farkları: $987-102=885$. Rakamların farklı olma koşulu olmasaydı en küçük $100$, en büyük $999$ olurdu."),
            dikkat(
                "En küçük sayıya $0$ ile başlamak.",
                "Rakamları farklı en küçük üç basamaklı sayı $012$ değildir, çünkü $012$ aslında iki basamaklı $12$ sayısıdır. En soldaki basamağa $0$ dan farklı en küçük rakam, yani $1$ gelir."),
        ]},
        {"baslik": "Rakamları farklı sayıları saymak", "icerik": [
            "Rakamları birbirinden farklı sayılar sayılırken basamaklar tek tek doldurulur ve her basamak için kullanılabilecek rakam sayısı çarpılır. En soldaki basamaktan başlamak, $0$ kısıtını doğru uygulamayı sağlar.",
            ornek(
                "Rakamları birbirinden farklı üç basamaklı sayılar verilsin.",
                "Bu sayıların kaç tane olduğunu bulalım.",
                "Yüzler basamağı: $0$ gelemez, $9$ seçenek.",
                "Onlar basamağı: yüzlerde kullanılan rakam gelemez ama $0$ gelebilir, $9$ seçenek.",
                "Birler basamağı: kullanılan iki rakam gelemez, $8$ seçenek. Toplam: $9 \\cdot 9 \\cdot 8=648$."),
            "Aynı mantıkla rakamları farklı iki basamaklı sayılar $9 \\cdot 9=81$ tanedir. Bu sayma yöntemine <strong>çarpma ilkesi</strong> denir ve permütasyon konusunun temelidir.",
        ]},
        {"baslik": "Verilen rakamlarla sayı yazmak", "icerik": [
            "Yalnızca belirli rakamların kullanılabildiği sorularda aynı çarpma ilkesi uygulanır. Rakamların tekrar edip edemeyeceği ve $0$ ın rakamlar arasında olup olmadığı sonucu değiştirir.",
            ornek(
                "$0$, $1$, $2$ ve $3$ rakamları kullanılarak üç basamaklı sayılar yazılacak.",
                "Rakamlar farklı olduğunda ve rakamlar tekrar edebildiğinde kaç sayı yazılabileceğini bulalım.",
                "Rakamlar farklıysa: yüzler için $3$ seçenek ($0$ gelemez), onlar için $3$, birler için $2$ seçenek: $3 \\cdot 3 \\cdot 2=18$.",
                "Rakamlar tekrar edebiliyorsa: yüzler için $3$, onlar ve birler için $4$ er seçenek: $3 \\cdot 4 \\cdot 4=48$."),
            "<h3>Çift ya da tek sayı yazmak</h3>",
            "Sayının çift ya da tek olması isteniyorsa önce birler basamağı doldurulur, çünkü kısıt oradadır. Sonra diğer basamaklar kalan rakamlarla doldurulur.",
            ornek(
                "$1$, $2$, $3$, $4$ ve $5$ rakamları kullanılarak rakamları farklı üç basamaklı çift sayılar yazılacak.",
                "Kaç sayı yazılabileceğini bulalım.",
                "Birler basamağı çift olmalı: $2$ ya da $4$; $2$ seçenek.",
                "Yüzler basamağı: kalan $4$ rakamdan biri; onlar basamağı: kalan $3$ rakamdan biri.",
                "Toplam: $2 \\cdot 4 \\cdot 3=24$ sayı."),
        ]},
        {"baslik": "Rakamları toplamı verilen sayılar", "icerik": [
            "Rakamlarının toplamı belirli bir sayı olan sayılar, basamaklara gelebilecek rakamlar tek tek denenerek sayılır. En soldaki basamağın $0$ olamayacağı ve her rakamın en fazla $9$ olabileceği unutulmamalıdır.",
            ornek(
                "Rakamları toplamı $5$ olan iki basamaklı sayılar verilsin.",
                "Bu sayıları bulalım.",
                "Onlar basamağı $a$, birler basamağı $b$ olsun: $a+b=5$ ve $a \\geq 1$.",
                "$a$ için $1$, $2$, $3$, $4$, $5$ değerleri mümkün; $b$ sırasıyla $4$, $3$, $2$, $1$, $0$ olur.",
                "Sayılar: $14$, $23$, $32$, $41$ ve $50$; toplam $5$ tane."),
            ornek(
                "Rakamları toplamı $15$ olan iki basamaklı sayılar verilsin.",
                "Bu sayıların kaç tane olduğunu bulalım.",
                "$a+b=15$ ve her rakam en fazla $9$ olduğu için $a$ en az $6$ olmalıdır.",
                "$a$ için $6$, $7$, $8$, $9$ değerleri mümkün: $69$, $78$, $87$, $96$; toplam $4$ tane."),
        ]},
        {"baslik": "Rakamların yeri değişince", "icerik": [
            "İki basamaklı $AB$ sayısının değeri $10A+B$, rakamlarının yeri değişince oluşan $BA$ sayısının değeri $10B+A$ dır. Bu iki sayının toplamı ve farkı çok sade ifadeler verir:",
            tablo(["İşlem", "Sonuç"], [
                ["$AB+BA$", "$11(A+B)$"],
                ["$AB-BA$", "$9(A-B)$"],
                ["$ABC-CBA$", "$99(A-C)$"],
            ]),
            "Bu yüzden iki basamaklı bir sayı ile rakamlarının yeri değişmiş hâlinin toplamı her zaman $11$ in, farkı ise her zaman $9$ un katıdır. Örneğin $74+47=121=11 \\cdot 11$ ve $74-47=27=9 \\cdot 3$ tür.",
            ornek(
                "$AB$ ve $BA$ iki basamaklı sayılar olmak üzere $AB+BA=132$ olsun.",
                "$A+B$ toplamını ve bu koşulu sağlayan $AB$ sayılarının sayısını bulalım.",
                "$11(A+B)=132$, yani $A+B=12$.",
                "$A$ ve $B$ sıfırdan farklı rakamlar olmalı: $A$ için $3$ ten $9$ a kadar değerler mümkün.",
                "Sayılar: $39$, $48$, $57$, $66$, $75$, $84$, $93$; toplam $7$ tane."),
        ]},
        {"baslik": "Büyük sayıların basamak sayısı", "icerik": [
            "Bir sayının kaç basamaklı olduğu, onun kuvvetleriyle karşılaştırılarak bulunur. $10^n$ sayısı $1$ ve arkasından $n$ tane $0$ dan oluştuğu için $n+1$ basamaklıdır. Üslü ifadelerde bu kural, ifadeyi $10$ un kuvveti içeren bir biçime getirerek kullanılır.",
            ornek(
                "$5^{10} \\cdot 2^{12}$ sayısı verilsin.",
                "Bu sayının kaç basamaklı olduğunu bulalım.",
                "$2^{12}=2^{10} \\cdot 2^2$ yazalım: $5^{10} \\cdot 2^{10} \\cdot 4=10^{10} \\cdot 4$.",
                "Sayı $4$ ün arkasına $10$ tane $0$ yazılarak elde edilir.",
                "Sayı $11$ basamaklıdır."),
            "Üslü sayıların ayrıntısı <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısında anlatılıyor. Bu tür sorularda $2$ ve $5$ in kuvvetlerini eşleştirerek $10$ un kuvvetini oluşturmak en kısa yoldur.",
        ]},
        {"baslik": "Rakamlar ve bölünebilme", "icerik": [
            "Bazı bölünebilme kuralları doğrudan rakamlara bakar: bir sayı, rakamlarının toplamı $3$ e bölünüyorsa $3$ e, $9$ a bölünüyorsa $9$ a bölünür. Bu kurallar, rakamlarla ilgili sayma ve bulma sorularında sık kullanılır.",
            ornek(
                "Rakamları birbirinden farklı üç basamaklı sayılar verilsin.",
                "Bunlardan $9$ a bölünen en büyüğünü bulalım.",
                "Rakamlar toplamı $9$ un katı olmalı: $9$, $18$ ya da $27$. Toplamın $27$ olması için üç rakamın da $9$ olması gerekir, bu da farklılık koşuluna aykırıdır.",
                "En büyük sayı için yüzler basamağına $9$, onlar basamağına $8$ yazalım: $9+8+c=18$ ise $c=1$.",
                "Aranan sayı $981$ dir."),
            "Bölünebilme kurallarının ayrıntısı <a href=\"/blog/bolunebilme-kurallari-konu-anlatimi-pdf/\">Bölünebilme Kuralları Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sayfa numaralamak için gereken rakamlar", "icerik": [
            "Bir kitabın sayfaları numaralanırken tek basamaklı sayfa numaraları birer, iki basamaklılar ikişer, üç basamaklılar üçer rakam kullanır. Toplam rakam sayısı, her gruptaki sayfa sayısı ile basamak sayısının çarpımlarının toplamıdır.",
            ornek(
                "Bir kitabın sayfaları $1$ den $150$ ye kadar numaralanıyor.",
                "Kaç rakam kullanıldığını bulalım.",
                "Tek basamaklı sayfalar: $1$ den $9$ a, $9$ sayfa; $9$ rakam.",
                "İki basamaklı sayfalar: $10$ dan $99$ a, $90$ sayfa; $180$ rakam.",
                "Üç basamaklı sayfalar: $100$ den $150$ ye, $51$ sayfa; $153$ rakam. Toplam: $9+180+153=342$ rakam."),
            "Soru tersine de sorulabilir: $342$ rakamla numaralanan bir kitabın kaç sayfa olduğu sorulursa, önce tek ve iki basamaklı sayfaların kullandığı $189$ rakam çıkarılır. Kalan $153$ rakam üçer üçer kullanıldığı için $51$ üç basamaklı sayfa vardır; son sayfa $99+51=150$ dir.",
        ]},
        {"baslik": "Bir rakamın kaç kez kullanıldığı", "icerik": [
            "Belirli bir rakamın bir aralıktaki sayılarda kaç kez yazıldığı sorulduğunda her basamak ayrı ayrı sayılır: rakam birler basamağında kaç kez, onlar basamağında kaç kez geçiyor? İki sayım toplandığında aynı sayıda iki kez geçen rakamlar da doğru sayılmış olur.",
            ornek(
                "$1$ den $100$ e kadar olan sayılar yazılıyor.",
                "$7$ rakamının kaç kez kullanıldığını bulalım.",
                "Birler basamağında: $7$, $17$, $27$ diye $97$ ye kadar $10$ kez.",
                "Onlar basamağında: $70$ ten $79$ a kadar $10$ kez.",
                "Toplam: $20$ kez. $77$ sayısında $7$ iki kez yazılır ve iki sayımda da ayrı ayrı sayılmıştır."),
        ]},
        {"baslik": "Yan yana yazılan sayılarda basamak bulmak", "icerik": [
            "Sayılar $1$ den başlayarak yan yana yazıldığında $123456789101112\\ldots$ biçiminde uzun bir rakam dizisi oluşur. Bu dizinin belirli bir sıradaki rakamı, rakamlar basamak sayısına göre gruplara ayrılarak bulunur: önce tek basamaklılar, sonra iki basamaklılar, sonra üç basamaklılar.",
            ornek(
                "Doğal sayılar $1$ den başlayarak yan yana yazılıyor.",
                "Oluşan dizinin $100$ üncü rakamını bulalım.",
                "İlk $9$ rakam tek basamaklı sayılardan gelir. Geriye $100-9=91$ rakam kalır.",
                "İki basamaklı sayılar ikişer rakam kullanır: $91=2 \\cdot 45+1$. Yani $10$ dan başlayan $45$ sayı, $10$ dan $54$ e kadar, tam olarak yazılır ve $99$ uncu rakama ulaşılır.",
                "$100$ üncü rakam bir sonraki sayı olan $55$ in ilk rakamıdır: $5$."),
            "Aynı yöntemle $200$ üncü rakam da bulunur. Tek ve iki basamaklı sayılar birlikte $9+180=189$ rakam kullanır; geriye $11$ rakam kalır. Üç basamaklı sayılar üçer rakam kullandığı için $11=3 \\cdot 3+2$ dir: $100$, $101$ ve $102$ tam olarak yazılır ve $103$ ün ikinci rakamına gelinir. $200$ üncü rakam $0$ dır.",
        ]},
        {"baslik": "Sınavda sayı basamakları", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) sayı basamakları rakamları farklı sayılar, verilen rakamlarla sayı yazma, rakam toplamı ve rakamların yer değiştirmesi soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde sayfa numarası ve rakam sayma soruları da sık görülür."),
            "Sayma sorularında en güvenli yol, basamakları tek tek doldurmak ve her adımda kaç seçenek kaldığını yazmaktır. Kısıtlı basamaktan başlamak, yani en soldaki basamaktan ya da tek ve çift koşulu varsa birler basamağından başlamak, hataları büyük ölçüde önler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["En soldaki basamağa $0$ koymak", "En solda $0$ olamaz"],
                ["Ardışık sayıları sayarken $1$ eklememek", "Son eksi ilk artı $1$"],
                ["Rakamları farklı sayıda tekrarı saymak", "Kullanılan rakam tekrar gelmez"],
                ["Çift sayı yazarken birler basamağını sonra doldurmak", "Önce kısıtlı basamak"],
                ["Rakamın en fazla $9$ olabileceğini unutmak", "Her rakam $0$ ile $9$ arasında"],
                ["$77$ deki iki $7$ yi bir kez saymak", "Her basamak ayrı sayılır"],
            ]),
            "Bu hataların çoğu, basamakların kısıtlarını gözden kaçırmaktan doğar. Her basamağın hangi rakamları alabileceğini yazmak ve sonuçları küçük bir örnekle denemek, sayma sorularındaki hataları büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("Rakam ile sayı arasındaki fark nedir?",
         "Rakam, sayıları yazmak için kullanılan on sembolden biridir. Sayı ise rakamlarla yazılan ve bir çokluk belirten ifadedir; her rakam tek basamaklı bir sayıdır."),
        ("Kaç tane üç basamaklı sayı vardır?",
         "100 den 999 a kadar 900 tane üç basamaklı sayı vardır. Genel olarak n basamaklı sayıların sayısı 9 çarpı 10 un n eksi birinci kuvvetidir."),
        ("Rakamları farklı kaç tane üç basamaklı sayı vardır?",
         "Yüzler basamağına 9, onlar basamağına 9, birler basamağına 8 rakam gelebilir. Toplam 648 sayı vardır."),
        ("Rakamları farklı en küçük üç basamaklı sayı kaçtır?",
         "102 dir. En soldaki basamağa 0 gelemediği için 1 yazılır, sonra kullanılmamış en küçük rakamlar 0 ve 2 gelir."),
        ("İki basamaklı bir sayı ile rakamlarının yeri değişmiş hâlinin toplamı neden 11 in katıdır?",
         "Çünkü on A artı B ile on B artı A nın toplamı 11 çarpı A artı B dir. Farkları ise 9 çarpı A eksi B olduğu için her zaman 9 un katıdır."),
        ("Bir kitabın sayfalarını numaralamak için kaç rakam gerekir?",
         "Tek, iki ve üç basamaklı sayfalar ayrı ayrı sayılır ve basamak sayılarıyla çarpılıp toplanır. 150 sayfalık bir kitap için 342 rakam gerekir."),
        ("Bir üslü ifadenin kaç basamaklı olduğu nasıl bulunur?",
         "İfade, bir sayı ile 10 un bir kuvvetinin çarpımı biçimine getirilir. 10 un n inci kuvveti n artı bir basamaklıdır; önündeki sayının basamak sayısı da buna göre eklenir."),
        ("Rakamları farklı ve 9 a bölünen en büyük üç basamaklı sayı kaçtır?",
         "981 dir. Rakamlar toplamı 9 un katı olmalıdır; 27 için üç rakam da 9 olacağından toplam 18 seçilir ve en büyük rakamlar sırayla yazılır."),
    ],
    "kontrol": [
        "Rakam ile sayı arasındaki farkı açıklayabiliyorum.",
        "Basamak ve bölük adlarını doğru kullanabiliyorum.",
        "Belirli basamak sayısındaki sayıların adedini bulabiliyorum.",
        "Rakamları farklı en küçük ve en büyük sayıları yazabiliyorum.",
        "Rakamları farklı sayıları çarpma ilkesiyle sayabiliyorum.",
        "Verilen rakamlarla yazılabilecek sayıları sayabiliyorum.",
        "Çift ya da tek sayı koşulunda önce birler basamağını doldurabiliyorum.",
        "Rakamları toplamı verilen sayıları bulabiliyorum.",
        "Rakamların yeri değişince oluşan toplam ve farkı hesaplayabiliyorum.",
        "Sayfa numarası ve rakam sayma sorularını çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["basamak-degeri-ve-cozumleme", "dogal-sayilar-ve-tam-sayilar", "sayi-problemleri-konu-anlatimi-pdf"],
}
