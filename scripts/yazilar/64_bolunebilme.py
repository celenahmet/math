# scripts/yazilar/64_bolunebilme.py — Bolunebilme Kurallari (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "bolunebilme-kurallari-konu-anlatimi-pdf",
    "baslik": "Bölünebilme Kuralları Konu Anlatımı PDF",
    "aciklama": "Bölünebilme kuralları: 2, 3, 4, 5, 7, 8, 9, 10 ve 11 ile bölünebilme, kalan bulma, birleşik kurallar ve rakam bulma soruları; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "bolunebilme-kurallari-konu-anlatimi-pdf",
    "kapak_alt": "Bölünebilme kuralları: mavi bilyeleri ahşap kutulara eşit gruplar hâlinde dağıtan iki öğrenci",
    "ozet": "Bir sayının başka bir sayıya tam bölünüp bölünmediğini, bölme işlemini yapmadan anlamak mümkündür. Bölünebilme kuralları sayının son basamaklarına ya da rakamlarının toplamına bakarak bu kararı saniyeler içinde verdirir. Bu yazıda her kuralı nedeniyle birlikte veriyor, kuralları kalan bulmak için kullanmayı, birleşik sayılarla bölünebilmeyi, 7 ve 11 ile bölünebilmeyi ve bilinmeyen rakamı bulma sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Bölünebilme nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için bölme işlemini, basamak kavramını ve tek-çift sayıları biliyor olman yeterli.",
                "Çift sayılar ve $2$ ile bölünebilme için <a href=\"/blog/tek-ve-cift-sayilar/\">Tek ve Çift Sayılar</a> yazısına göz at."),
            "Bir $a$ doğal sayısı $b$ ye bölündüğünde bir bölüm ve bir kalan elde edilir. Bölme işleminin eşitliği şudur:",
            "$$a=b \\cdot q+r \\text{ ve } 0 \\leq r<b$$",
            "Burada $a$ bölünen, $b$ bölen, $q$ bölüm, $r$ kalandır. Kalan her zaman bölenden küçüktür. Kalan $0$ ise $a$, $b$ ye <strong>tam bölünür</strong>; başka bir deyişle $a$, $b$ nin bir katıdır.",
            "Bölünebilme kuralları, büyük bir sayıda bölme işlemini yapmadan kalanın $0$ olup olmadığını anlamanın kısa yollarıdır. Kuralların hepsi aynı fikre dayanır: basamak değerlerinin ($1$, $10$, $100$, $\\ldots$) bölene göre kalanları bilinirse, sayının kalanı da bilinir.",
            hap("$a=b \\cdot q+r$ ve $0 \\leq r<b$; kalan $0$ ise $a$, $b$ ye tam bölünür.",
                "Bölünebilme kuralları, bölme yapmadan kalanı bulmanın kısa yollarıdır."),
        ]},
        {"baslik": "Bölünebilmenin temel özellikleri", "icerik": [
            "Kuralların hepsi birkaç basit özelliğe dayanır. $a$, $b$ yi ve $c$ yi tam bölüyorsa:",
            "<ul><li>$a$, $b+c$ yi ve $b-c$ yi de tam böler.</li>"
            "<li>$a$, $b$ nin her katını da tam böler: $k \\cdot b$ gibi.</li></ul>",
            ornek(
                "$6$, $36$ yı ve $18$ i tam bölsün.",
                "$6$ nın $54$ ü ve $18$ i ($36-18$) böldüğünü gösterelim.",
                "$36+18=54$ ve $54=6 \\cdot 9$.",
                "$36-18=18$ ve $18=6 \\cdot 3$."),
            dikkat(
                "Bu özelliklerin tersi her zaman doğru değildir.",
                "$5$, $2+3=5$ toplamını böler ama ne $2$ yi ne $3$ ü böler. Toplamın bölünmesi, terimlerin tek tek bölündüğünü göstermez."),
        ]},
        {"baslik": "2, 5 ve 10 ile bölünebilme: son basamak", "icerik": [
            "$10$, hem $2$ ye hem $5$ e tam bölünür. Bu yüzden bir sayının onlar ve daha büyük basamaklarının toplamı her zaman $2$ ye ve $5$ e bölünür; karar yalnızca <strong>birler basamağına</strong> kalır.",
            tablo(["Bölen", "Kural", "Kalan"], [
                ["$2$", "Son basamak $0, 2, 4, 6, 8$", "Son basamağın $2$ ye bölümünden kalan"],
                ["$5$", "Son basamak $0$ ya da $5$", "Son basamağın $5$ e bölümünden kalan"],
                ["$10$", "Son basamak $0$", "Son basamağın kendisi"],
            ]),
            ornek(
                "$4837$ sayısı verilsin.",
                "$2$, $5$ ve $10$ a bölümünden kalanları bulalım.",
                "Son basamak $7$.",
                "$2$ ye bölümünden kalan $1$, $5$ e bölümünden kalan $2$, $10$ a bölümünden kalan $7$."),
        ]},
        {"baslik": "4 ve 8 ile bölünebilme: son basamaklar", "icerik": [
            "$100=4 \\cdot 25$ olduğu için yüzler ve daha büyük basamaklar $4$ e her zaman bölünür; karar <strong>son iki basamağa</strong> kalır. Aynı şekilde $1000=8 \\cdot 125$ olduğu için $8$ ile bölünebilmede <strong>son üç basamağa</strong> bakılır.",
            tablo(["Bölen", "Kural", "Kalan"], [
                ["$4$", "Son iki basamak $4$ ün katı", "Son iki basamağın kalanı"],
                ["$8$", "Son üç basamak $8$ in katı", "Son üç basamağın kalanı"],
            ]),
            ornek(
                "$1234567$ sayısı verilsin.",
                "$4$ e ve $8$ e bölümünden kalanları bulalım.",
                "$4$ için son iki basamak $67$: $67=4 \\cdot 16+3$, kalan $3$.",
                "$8$ için son üç basamak $567$: $567=8 \\cdot 70+7$, kalan $7$."),
            ornek(
                "Üç basamaklı $72a$ sayısı $4$ ile tam bölünsün.",
                "$a$ rakamının alabileceği değerleri bulalım.",
                "Son iki basamak $2a$ nın $4$ ün katı olması gerekir.",
                "$20$ ile $29$ arasında $4$ ün katları $20$, $24$ ve $28$ dir.",
                "$a$ nın değerleri $0$, $4$ ve $8$."),
            hap("$4$ ile bölünebilmede son iki basamağa, $8$ ile bölünebilmede son üç basamağa bakılır."),
        ]},
        {"baslik": "25 ve 125 ile bölünebilme", "icerik": [
            "Aynı basamak fikri $25$ ve $125$ için de işler. $100=4 \\cdot 25$ olduğu için $25$ ile bölünebilmede son iki basamağa bakılır: son iki basamak $00$, $25$, $50$ ya da $75$ ise sayı $25$ e tam bölünür. $1000=8 \\cdot 125$ olduğu için $125$ ile bölünebilmede son üç basamağa bakılır.",
            ornek(
                "$3375$ sayısı verilsin.",
                "$25$ ve $125$ ile tam bölünüp bölünmediğini bulalım.",
                "Son iki basamak $75$: sayı $25$ e tam bölünür.",
                "Son üç basamak $375=3 \\cdot 125$: sayı $125$ e de tam bölünür. Kontrol: $3375=125 \\cdot 27$."),
        ]},
        {"baslik": "3 ve 9 ile bölünebilme: rakamlar toplamı", "icerik": [
            "Bir sayı, rakamlarının toplamı $3$ e bölünüyorsa $3$ e, $9$ a bölünüyorsa $9$ a tam bölünür. Kalanlar için de aynı yol geçerlidir: sayının $3$ e ya da $9$ a bölümünden kalan, rakamları toplamının kalanına eşittir.",
            "<h3>Kural nereden geliyor?</h3>",
            "$10=9+1$, $100=99+1$, $1000=999+1$ olduğu için her basamak değeri, $9$ un bir katından $1$ fazladır. Örneğin:",
            "$$4527=4 \\cdot 1000+5 \\cdot 100+2 \\cdot 10+7=(4 \\cdot 999+5 \\cdot 99+2 \\cdot 9)+(4+5+2+7)$$",
            "Birinci parantez $9$ un, dolayısıyla $3$ ün katıdır. Sayının $9$ ve $3$ e göre kalanını ikinci parantez, yani rakamlar toplamı belirler. $4+5+2+7=18$ hem $3$ ün hem $9$ un katı olduğu için $4527$ ikisine de tam bölünür.",
            ornek(
                "$4528$ sayısı verilsin.",
                "$3$ e ve $9$ a bölümünden kalanları bulalım.",
                "Rakamlar toplamı: $4+5+2+8=19$.",
                "$19=3 \\cdot 6+1$: $3$ e bölümünden kalan $1$.",
                "$19=9 \\cdot 2+1$: $9$ a bölümünden kalan $1$."),
            dikkat(
                "$3$ e bölünen her sayı $9$ a bölünmez.",
                "$12$ nin rakamları toplamı $3$ tür: $12$, $3$ e bölünür ama $9$ a bölünmez. Tersi ise her zaman doğrudur: $9$ a bölünen sayı $3$ e de bölünür."),
            hap("Bir sayının $3$ e ya da $9$ a bölümünden kalan, rakamları toplamının kalanına eşittir."),
        ]},
        {"baslik": "11 ile bölünebilme", "icerik": [
            "$11$ ile bölünebilmede rakamlar <strong>sağdan başlayarak</strong> sırayla $+$, $-$, $+$, $-$ işaretleriyle toplanır. Bu toplam $11$ in katıysa (sıfır da dahil) sayı $11$ e tam bölünür. Toplamın $11$ e bölümünden kalan, sayının kalanına eşittir; toplam negatif çıkarsa $11$ eklenerek kalan bulunur.",
            "Kuralın nedeni: $10=11-1$ olduğu için $10$, $11$ e göre $-1$ gibi davranır; $100=99+1$ ise $+1$ gibi davranır. Basamak değerleri sırayla $+1$ ve $-1$ gibi davrandığı için işaretler sırayla değişir.",
            ornek(
                "$918082$ sayısı verilsin.",
                "$11$ ile tam bölünüp bölünmediğini bulalım.",
                "Sağdan başlayalım: $2-8+0-8+1-9=-22$.",
                "$-22$, $11$ in katıdır; sayı $11$ e tam bölünür. Kontrol: $918082=11 \\cdot 83462$."),
            ornek(
                "$1234$ sayısı verilsin.",
                "$11$ e bölümünden kalanı bulalım.",
                "Sağdan başlayalım: $4-3+2-1=2$.",
                "Kalan $2$ dir. Kontrol: $1234=11 \\cdot 112+2$."),
            ornek(
                "Dört basamaklı $5a38$ sayısı $11$ ile tam bölünsün.",
                "$a$ rakamını bulalım.",
                "Sağdan başlayalım: $8-3+a-5=a$.",
                "$a$ nın $11$ in katı olması gerekir; bir rakam için tek değer $a=0$.",
                "Sayı $5038$ dir. Kontrol: $5038=11 \\cdot 458$."),
        ]},
        {"baslik": "7 ile bölünebilme", "icerik": [
            "$7$ ile bölünebilme için kullanışlı bir yöntem şudur: sayının son basamağının iki katını, son basamak silinince kalan sayıdan çıkar. Sonuç $7$ nin katıysa (sıfır ya da negatif de olabilir) sayı $7$ ye tam bölünür. Sonuç hâlâ büyükse aynı işlem tekrarlanır.",
            "Yöntemin nedeni: sayı $10a+b$ biçimindeyse $a-2b$ ye bakılır. $10a+b$ nin $-2$ katı $-20a-2b$ dir ve $-20a=-21a+a$ olduğu için $-20a-2b$ ile $a-2b$ arasındaki fark $21a$, yani $7$ nin katıdır. Bu yüzden biri $7$ ye bölünüyorsa öteki de bölünür. $2$ ile $7$ aralarında asal olduğu için de $10a+b$ nin $7$ ye bölünmesi, $-2$ katının bölünmesiyle aynı şeydir.",
            ornek(
                "$343$ ve $3528$ sayıları verilsin.",
                "$7$ ile tam bölünüp bölünmediklerini bulalım.",
                "$343$: $34-2 \\cdot 3=28$ ve $28=7 \\cdot 4$; sayı $7$ ye bölünür.",
                "$3528$: $352-2 \\cdot 8=336$; tekrar: $33-2 \\cdot 6=21$ ve $21=7 \\cdot 3$; sayı $7$ ye bölünür."),
            dikkat(
                "Bu yöntem kalanı doğrudan vermez.",
                "Yöntem yalnızca tam bölünüp bölünmediğini söyler. Kalan gerekiyorsa bölme işlemi yapılır ya da sayının $7$ nin yakın bir katından farkına bakılır."),
        ]},
        {"baslik": "Birleşik sayılarla bölünebilme", "icerik": [
            "Bir sayının $6$, $12$, $15$ gibi bir sayıya bölünüp bölünmediğini anlamak için böleni <strong>aralarında asal</strong> çarpanlara ayırıp her çarpanın kuralını ayrı ayrı uygularsın. Aralarında asal, $1$ den başka ortak böleni olmayan sayılar demektir.",
            tablo(["Bölen", "Kontrol edilecek"], [
                ["$6$", "$2$ ve $3$"],
                ["$12$", "$3$ ve $4$"],
                ["$15$", "$3$ ve $5$"],
                ["$18$", "$2$ ve $9$"],
                ["$24$", "$3$ ve $8$"],
                ["$36$", "$4$ ve $9$"],
                ["$45$", "$5$ ve $9$"],
                ["$72$", "$8$ ve $9$"],
            ]),
            dikkat(
                "Çarpanlar aralarında asal olmalıdır.",
                "$12=2 \\cdot 6$ yazıp $2$ ve $6$ ile bölünebilmeye bakmak yanlıştır. $18$, hem $2$ ye hem $6$ ya bölünür ama $12$ ye bölünmez. Doğrusu $12$ için $3$ ve $4$ e bakmaktır."),
            ornek(
                "Beş basamaklı $4a73b$ sayısı $12$ ile tam bölünsün.",
                "Bu koşulu sağlayan kaç sayı olduğunu bulalım.",
                "$4$ ile bölünme: son iki basamak $3b$, $4$ ün katı olmalı. $32$ ve $36$ uygun: $b=2$ ya da $b=6$.",
                "$3$ ile bölünme: rakamlar toplamı $14+a+b$, $3$ ün katı olmalı.",
                "$b=2$ için $16+a$: $a$ değerleri $2$, $5$, $8$. $b=6$ için $20+a$: $a$ değerleri $1$, $4$, $7$.",
                "Toplam $6$ sayı vardır."),
            ornek(
                "Dört basamaklı $3a4b$ sayısı $5$ ile ve $9$ ile tam bölünsün.",
                "$a+b$ nin alabileceği değerleri bulalım.",
                "$5$ ile bölünme: $b=0$ ya da $b=5$.",
                "$b=0$ için rakamlar toplamı $7+a$; $9$ un katı olması için $a=2$.",
                "$b=5$ için rakamlar toplamı $12+a$; $9$ un katı olması için $a=6$.",
                "$a+b$ nin değerleri: $2+0=2$ ve $6+5=11$."),
            hap("$126$ öğrenci altışarlı gruplara eksiksiz ayrılabilir.", "$126$ çifttir ve rakamları toplamı $9$ olduğu için $3$ e de bölünür; $2$ ve $3$ e bölünen sayı $6$ ya bölünür ve $21$ grup oluşur.", gunluk=True),
        ]},
        {"baslik": "Kalan soruları", "icerik": [
            "Kalanlar toplama ve çarpmada birlikte hareket eder: bir sayı yerine onun kalanı kullanılabilir. Bu özellik, sayının kendisini bilmeden bir ifadenin kalanını bulmayı sağlar.",
            ornek(
                "$A$ nın $9$ a bölümünden kalan $5$ olsun.",
                "$2A+1$ in $9$ a bölümünden kalanı bulalım.",
                "$A$ yerine kalanı kullanalım: $2 \\cdot 5+1=11$.",
                "$11$ in $9$ a bölümünden kalan $2$ dir.",
                "Kontrol: $A=14$ için $2A+1=29$ ve $29=9 \\cdot 3+2$."),
            ornek(
                "$A$ nın $9$ a bölümünden kalan $5$, $B$ nin $9$ a bölümünden kalan $4$ olsun.",
                "$A \\cdot B$ nin $9$ a bölümünden kalanı bulalım.",
                "Kalanları çarpalım: $5 \\cdot 4=20$.",
                "$20=9 \\cdot 2+2$: kalan $2$.",
                "Kontrol: $A=14$, $B=13$ için $A \\cdot B=182$ ve $182=9 \\cdot 20+2$."),
            hap("Toplama ve çarpmada sayıların yerine kalanları kullanılabilir.",
                "Bulunan sonuç bölenden büyükse bir kez daha bölünerek kalan bulunur."),
        ]},
        {"baslik": "En büyük ve en küçük sayı soruları", "icerik": [
            "Bölünebilme kuralları, belirli bir koşulu sağlayan en büyük ya da en küçük sayıyı bulmak için de kullanılır. Yöntem, istenen yönde en uç sayıdan başlayıp kuralı sağlayana kadar rakamları ayarlamaktır.",
            ornek(
                "Dört basamaklı sayılar verilsin.",
                "$9$ ile tam bölünen en küçük dört basamaklı sayıyı bulalım.",
                "En küçük dört basamaklı sayı $1000$; rakamları toplamı $1$.",
                "Toplamın $9$ olması için $8$ eklemek gerekir: $1008$.",
                "Kontrol: $1008=9 \\cdot 112$."),
            ornek(
                "Rakamları birbirinden farklı dört basamaklı sayılar verilsin.",
                "Bunlardan $5$ ile tam bölünen en büyüğünü bulalım.",
                "Son basamak $0$ ya da $5$ olmalı. Baştaki basamakları olabildiğince büyük seçelim: $9$, $8$, $7$.",
                "Son basamak için $5$ ve $0$ uygun; büyük olan $9875$.",
                "Sayı $9875$ tir."),
            "<h3>Kalan ve bölenin bölenleri</h3>",
            "Bir sayının $12$ ye bölümünden kalan biliniyorsa, $12$ nin bölenlerine göre kalanlar da bilinir; çünkü $12$ nin katları $2$, $3$, $4$ ve $6$ nın da katıdır.",
            ornek(
                "$A$ nın $12$ ye bölümünden kalan $7$ olsun.",
                "$A$ nın $4$ e, $3$ e ve $6$ ya bölümünden kalanları bulalım.",
                "$A=12k+7$ biçimindedir ve $12k$ her birine tam bölünür; kalanı $7$ belirler.",
                "$7$ nin $4$ e bölümünden kalan $3$, $3$ e bölümünden kalan $1$, $6$ ya bölümünden kalan $1$."),
        ]},
        {"baslik": "Sınavda bölünebilme", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu bilinmeyen rakamı bulma, kalan bulma ve birleşik sayılarla bölünebilme biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde bölünebilme bilgisi sayısal akıl yürütme sorularında hızlı kontrol için de gerekebilir: bir sonucun bir sayıya bölünüp bölünmediğini hesap yapmadan anlamak gibi."),
            "Bölünebilme kuralları aynı zamanda asal çarpanlara ayırmanın da ilk adımıdır: bir sayıyı hangi küçük asallara böleceğini kurallar hemen gösterir. Bu bağlantı için <a href=\"/blog/asal-sayilar-ve-asal-carpanlara-ayirma/\">Asal Sayılar ve Asal Çarpanlara Ayırma</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$4$ için son basamağa bakmak", "Son iki basamak"],
                ["$8$ için son iki basamağa bakmak", "Son üç basamak"],
                ["$11$ de soldan başlamak", "Sağdan $+$ ile başla"],
                ["$12$ için $2$ ve $6$ ya bakmak", "$3$ ve $4$ e bak"],
                ["$3$ e bölüneni $9$ a da bölünür sanmak", "$12$, $9$ a bölünmez"],
                ["Kalanı bölenden büyük bırakmak", "Kalan bölenden küçüktür"],
            ]),
            "Bu hataların çoğu, kuralı nedeni olmadan ezberlemekten doğar. Her kuralın arkasındaki basamak değeri fikrini bilmek, hangi basamağa bakılacağını unutmayı önler: $4$ için $100$, $8$ için $1000$ bölene tam bölünen ilk basamak değeridir.",
        ]},
    ],
    "sss": [
        ("3 ile bölünebilme kuralı nedir?",
         "Rakamlarının toplamı 3 ün katı olan sayı 3 e tam bölünür. Sayının 3 e bölümünden kalan, rakamları toplamının 3 e bölümünden kalana eşittir."),
        ("4 ile bölünebilme kuralı nedir?",
         "Son iki basamağın oluşturduğu sayı 4 ün katıysa sayı 4 e tam bölünür. Çünkü 100, 4 e tam bölünür."),
        ("25 ile bölünebilme kuralı nedir?",
         "Son iki basamak 00, 25, 50 ya da 75 ise sayı 25 e tam bölünür. Çünkü 100, 25 e tam bölündüğü için karar yalnızca son iki basamağa kalır."),
        ("11 ile bölünebilme kuralı nasıl uygulanır?",
         "Rakamlar sağdan başlayarak sırayla artı ve eksi işaretleriyle toplanır. Sonuç 11 in katıysa, sıfır da dahil, sayı 11 e tam bölünür."),
        ("12 ile bölünebilme için neden 2 ve 6 ya bakılmaz?",
         "2 ile 6 aralarında asal değildir. Örneğin 18 hem 2 ye hem 6 ya bölünür ama 12 ye bölünmez. Doğrusu aralarında asal olan 3 ve 4 e bakmaktır."),
        ("7 ile bölünebilme nasıl anlaşılır?",
         "Son basamağın iki katı, son basamak silinince kalan sayıdan çıkarılır. Sonuç 7 nin katıysa sayı 7 ye tam bölünür."),
        ("Kalan en fazla kaç olabilir?",
         "Kalan her zaman bölenden küçüktür. Örneğin 9 a bölümde kalan 0 ile 8 arasında olabilir."),
    ],
    "kontrol": [
        "Bölme eşitliğini ve kalanın bölenden küçük olduğunu açıklayabiliyorum.",
        "$2$, $5$ ve $10$ ile bölünebilmede son basamağa bakabiliyorum.",
        "$4$ ve $8$ ile bölünebilmede son iki ve son üç basamağa bakabiliyorum.",
        "$3$ ve $9$ kuralının neden rakamlar toplamına dayandığını açıklayabiliyorum.",
        "$11$ ile bölünebilmede sağdan başlayarak işaretli toplam alabiliyorum.",
        "$7$ ile bölünebilmeyi son basamak yöntemiyle kontrol edebiliyorum.",
        "Birleşik bir sayıyı aralarında asal çarpanlara ayırıp kuralları birleştirebiliyorum.",
        "Bilinmeyen rakamı bölünebilme koşullarından bulabiliyorum.",
        "Bölünebilme kurallarıyla kalan bulabiliyorum.",
        "Toplama ve çarpmada sayıların yerine kalanları kullanabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["asal-sayilar-ve-asal-carpanlara-ayirma", "tek-ve-cift-sayilar", "ardisik-sayilar"],
}
