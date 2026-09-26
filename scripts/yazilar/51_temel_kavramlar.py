# scripts/yazilar/51_temel_kavramlar.py — Temel Kavramlar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "temel-kavramlar-konu-anlatimi-pdf",
    "baslik": "Temel Kavramlar Konu Anlatımı PDF",
    "aciklama": "Rakam ve sayı, tek ve çift sayılar, pozitif ve negatif sayılar, ardışık sayılar, asal sayılar, faktöriyel ve basamak kavramı; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "temel-kavramlar-konu-anlatimi-pdf",
    "kapak_alt": "Temel kavramlar konu anlatımı: ahşap ray üzerinde küçükten büyüğe sıralanan toplar ve bir terazi ile karşılaştırma yapan iki öğrenci",
    "ozet": "Sayı problemleri, bölünebilme, EBOB ve EKOK, denklemler ve olasılık; hepsi aynı küçük kavram setinin üzerine kurulur. Rakam ile sayının farkı, tek ve çift sayıların davranışı, işaret kuralları, ardışık sayılar, asal sayılar, faktöriyel ve basamak kavramı. Bu yazıda bu kavramları tek tek tanımlıyor, her birinin sınavda işe yarayan kurallarını çözümlü örneklerle veriyoruz.",
    "bolumler": [
        {"baslik": "Temel kavramlar nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi ve çarpım tablosunu biliyor olman yeterli.",
                "Sayı kümeleri ayrıntılı olarak <a href=\"/blog/sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf/\">Sayılar ve Sayı Kümeleri Konu Anlatımı PDF</a> yazısında anlatılıyor."),
            "Temel kavramlar, matematiğin geri kalanında sürekli kullanılan küçük tanımlar ve kurallardır. Tek başına çok basit görünürler; zorluk, bir soruda birkaçının aynı anda kullanılmasından çıkar. Örneğin \"ardışık üç tek sayının toplamı\" diye başlayan bir soruda hem ardışıklık hem de tek sayı kavramı birlikte çalışır.",
            "Bu yazıda sırasıyla şunları ele alıyoruz: rakam ve sayı, sayı çeşitleri, tek ve çift sayılar, pozitif ve negatif sayılar, ardışık sayılar, asal sayılar, faktöriyel ve basamak kavramı.",
            hap("Temel kavram sorularında önce <strong>hangi kavramların</strong> kullanıldığını ayır: tek mi çift mi, pozitif mi negatif mi, ardışık mı, asal mı.",
                "Kavramı doğru adlandırmak, kuralın yarısını çözmektir."),
        ]},
        {"baslik": "Rakam ve sayı", "icerik": [
            "<strong>Rakam</strong>, sayıları yazmak için kullandığımız sembollerdir. Onluk sistemde on rakam vardır: $0, 1, 2, 3, 4, 5, 6, 7, 8, 9$. <strong>Sayı</strong> ise rakamlarla yazılan ve bir çokluk ya da değer belirten ifadedir: $7$, $48$, $305$ gibi.",
            "Her rakam aynı zamanda tek basamaklı bir sayıdır, ama her sayı bir rakam değildir. $48$ bir sayıdır; $4$ ve $8$ rakamlarıyla yazılmıştır.",
            "Çok basamaklı bir sayının en başına $0$ yazılmaz. Bu yüzden en küçük üç basamaklı sayı $100$ dür. Soruda \"rakamları farklı\" deniyorsa aynı rakam iki kez kullanılamaz.",
            ornek(
                "Rakamları birbirinden farklı üç basamaklı sayıları düşünelim.",
                "Bunların en büyüğü ile en küçüğünün toplamı kaçtır?",
                "En büyük için baştan büyük rakamları yazarız: $987$.",
                "En küçük için başa sıfır olmayan en küçük rakamı, sonra kalan en küçük rakamları yazarız: $102$.",
                "Toplam: $987+102=1089$."),
            ornek(
                "Rakamları birbirinden farklı iki basamaklı sayıları sayalım.",
                "Kaç tane vardır?",
                "Onlar basamağı için $0$ olamayacağı için $9$ seçenek vardır.",
                "Birler basamağı için $0$ dahil $10$ rakamdan onlar basamağında kullanılanı çıkarırız: $9$ seçenek.",
                "Toplam: $9 \\cdot 9=81$ sayı."),
            dikkat(
                "En küçük üç basamaklı sayı $100$ dür, ama rakamları farklı en küçük üç basamaklı sayı $102$ dir.",
                "Soruda \"rakamları farklı\" ifadesinin olup olmadığına mutlaka bak."),
            hap("Telefon numarası ya da okul numarası aslında bir sayı değil, rakamlardan oluşan bir koddur: başındaki $0$ atılamaz ve bu kodlarla toplama yapılmaz.", gunluk=True),
        ]},
        {"baslik": "Sayı çeşitleri kısaca", "icerik": [
            "Temel kavramlarda kullanılan sayı kümeleri şunlardır:",
            "<ul><li><strong>Sayma sayıları:</strong> $\\{1,2,3,\\ldots\\}$. Nesneleri saymak için kullandığımız sayılar.</li>"
            "<li><strong>Doğal sayılar</strong> $\\mathbb{N}$: $\\{0,1,2,3,\\ldots\\}$. Sayma sayılarına $0$ eklenmiş hâli.</li>"
            "<li><strong>Tam sayılar</strong> $\\mathbb{Z}$: $\\{\\ldots,-2,-1,0,1,2,\\ldots\\}$. Doğal sayılara negatifleri eklenmiş hâli.</li>"
            "<li><strong>Rasyonel sayılar</strong> $\\mathbb{Q}$: $\\dfrac{a}{b}$ biçiminde yazılabilen sayılar ($a$ ve $b$ tam sayı, $b \\neq 0$).</li>"
            "<li><strong>Gerçek sayılar</strong> $\\mathbb{R}$: sayı doğrusundaki bütün noktalar.</li></ul>",
            "Soruda \"$a$ bir tam sayıdır\" ile \"$a$ bir doğal sayıdır\" arasındaki fark cevabı değiştirebilir. Tam sayı negatif olabilir, doğal sayı olamaz.",
            hap("Sayma sayıları $1$ den, doğal sayılar $0$ dan başlar.",
                "Soruda hangi kümeden söz edildiğini cevaba geçmeden önce not et."),
        ]},
        {"baslik": "Tek ve çift sayılar", "icerik": [
            "$2$ ile tam bölünebilen tam sayılara <strong>çift sayı</strong>, bölünemeyenlere <strong>tek sayı</strong> denir. $k$ bir tam sayı olmak üzere çift sayılar $2k$, tek sayılar $2k+1$ biçiminde yazılır.",
            "Bu tanım negatif sayıları da kapsar: $-4$ çift, $-3$ tektir. $0$ da çift sayıdır, çünkü $0=2 \\cdot 0$ dır.",
            "Tek ve çift sayıların toplama, çıkarma ve çarpmadaki davranışı sabittir. $\\text{T}$ tek, $\\text{Ç}$ çift sayıyı göstersin:",
            tablo(["İşlem", "Sonuç"], [
                ["$\\text{T} \\pm \\text{T}$", "Çift"],
                ["$\\text{T} \\pm \\text{Ç}$", "Tek"],
                ["$\\text{Ç} \\pm \\text{Ç}$", "Çift"],
                ["$\\text{T} \\cdot \\text{T}$", "Tek"],
                ["$\\text{T} \\cdot \\text{Ç}$", "Çift"],
                ["$\\text{Ç} \\cdot \\text{Ç}$", "Çift"],
            ]),
            "Kuvvetlerde de durum basittir: $n$ bir pozitif tam sayıysa tek sayının her kuvveti tek, çift sayının her kuvveti çifttir.",
            hap("Bir çarpımda <strong>en az bir çift</strong> çarpan varsa çarpım çifttir.",
                "Toplamda ise tek sayıların <strong>adedine</strong> bakılır: tek sayıda tek terim varsa toplam tektir."),
            ornek(
                "$a$ ve $b$ tam sayılar ve $3a+2b$ tek olsun.",
                "$a$ ve $b$ hakkında ne söylenebilir?",
                "$2b$ her zaman çifttir, çünkü $2$ ile çarpılmıştır.",
                "Çift bir sayıya eklendiğinde sonucun tek çıkması için $3a$ tek olmalıdır.",
                "$3$ tek olduğu için $3a$ ancak $a$ tekse tektir. Öyleyse $a$ tektir.",
                "$b$ hakkında hiçbir şey söylenemez; tek de olabilir çift de."),
            dikkat(
                "Bölme işleminin sonucu için tek ya da çift kuralı yoktur.",
                "$12 \\div 4=3$ tektir, $12 \\div 6=2$ çifttir. İkisinde de bölünen çift sayıdır."),
        ]},
        {"baslik": "Pozitif ve negatif sayılar", "icerik": [
            "Sıfırdan büyük sayılara <strong>pozitif</strong>, sıfırdan küçük sayılara <strong>negatif</strong> sayı denir. $0$ ne pozitif ne negatiftir.",
            "Çarpma ve bölmede işaret kuralı şudur: aynı işaretli iki sayının çarpımı ya da bölümü pozitif, farklı işaretli iki sayınınki negatiftir.",
            "Kuvvet alırken bu kural tekrar tekrar uygulanır. Negatif bir sayı çift sayıda kez çarpılırsa işaretler ikişer ikişer birbirini götürür ve sonuç pozitif olur. Tek sayıda kez çarpılırsa bir eksi artar ve sonuç negatif olur.",
            hap("Negatif bir sayının çift kuvveti pozitif, tek kuvveti negatiftir.",
                "Örneğin $(-2)^4=16$ ve $(-2)^3=-8$."),
            dikkat(
                "$(-2)^4$ ile $-2^4$ aynı şey değildir.",
                "$(-2)^4=16$ dır: parantez, eksinin de kuvvete girdiğini söyler.",
                "$-2^4=-16$ dır: önce $2^4=16$ hesaplanır, sonra başına eksi konur."),
            ornek(
                "$a<0<b$ olsun.",
                "$a \\cdot b$, $a^2 \\cdot b$, $a^3$ ve $b-a$ ifadelerinin işaretini bulalım.",
                "$a \\cdot b$: farklı işaretli iki sayının çarpımı, negatif.",
                "$a^2 \\cdot b$: $a^2$ pozitiftir, pozitif ile pozitifin çarpımı pozitif.",
                "$a^3$: negatif sayının tek kuvveti, negatif.",
                "$b-a$: $b-a=b+(-a)$ ve iki terim de pozitif, sonuç pozitif.",
                "Kontrol için $a=-2$ ve $b=3$ alalım: $a \\cdot b=-6$, $a^2 \\cdot b=12$, $a^3=-8$, $b-a=5$."),
        ]},
        {"baslik": "Ardışık sayılar", "icerik": [
            "Belirli bir kurala göre art arda gelen sayılara <strong>ardışık sayılar</strong> denir. Başlıcaları şunlardır:",
            "<ul><li>Ardışık tam sayılar: $n$, $n+1$, $n+2$, ...</li><li>Ardışık çift sayılar: $2n$, $2n+2$, $2n+4$, ...</li><li>Ardışık tek sayılar: $2n+1$, $2n+3$, $2n+5$, ...</li></ul>",
            "Aralarındaki fark sabit olan sayı dizilerinde iki soru sık sorulur: kaç terim var ve toplamları kaç? İkisinin de kısa bir cevabı vardır.",
            "$$\\text{Terim sayısı}=\\frac{\\text{son}-\\text{ilk}}{\\text{artış}}+1$$",
            "$$\\text{Toplam}=\\frac{\\text{ilk}+\\text{son}}{2} \\cdot \\text{terim sayısı}$$",
            "Toplam formülünün mantığı şudur: ilk terimle son terim, ikinci terimle sondan ikinci terim ve bu şekilde eşleşen bütün çiftlerin toplamı aynıdır. Bu yüzden toplam, ortalama ile terim sayısının çarpımıdır.",
            ornek(
                "$12+14+16+\\cdots+40$ toplamı verilsin.",
                "Bu toplam kaçtır?",
                "Terim sayısı: $\\dfrac{40-12}{2}+1=14+1=15$.",
                "Toplam: $\\dfrac{12+40}{2} \\cdot 15=26 \\cdot 15=390$."),
            hap("$1+2+\\cdots+n=\\dfrac{n(n+1)}{2}$ ve $1+3+5+\\cdots+(2n-1)=n^2$.",
                "Örneğin $1+2+\\cdots+20=210$ ve ilk $10$ tek sayının toplamı $1+3+\\cdots+19=100$ dür."),
            ornek(
                "Ardışık üç tek sayının toplamı $87$ olsun.",
                "Bu sayıları bulalım.",
                "Ardışık üç sayının toplamı, ortadaki sayının üç katıdır; çünkü ortancanın bir eksiği ile bir fazlası birbirini dengeler.",
                "Ortanca: $87 \\div 3=29$.",
                "Sayılar $27$, $29$ ve $31$ dir. Kontrol: $27+29+31=87$."),
            "Ardışık sayıların tek ve çift davranışı da işe yarar. Ardışık iki tam sayıdan biri mutlaka çifttir; bu yüzden $n(n+1)$ çarpımı her zaman çifttir. Ardışık üç tam sayıdan biri de mutlaka $3$ ün katıdır.",
        ]},
        {"baslik": "Asal sayılar", "icerik": [
            "$1$ den büyük olup yalnızca $1$ e ve kendisine bölünebilen doğal sayılara <strong>asal sayı</strong> denir. $30$ dan küçük asal sayılar şunlardır:",
            "$$2, 3, 5, 7, 11, 13, 17, 19, 23, 29$$",
            "Bu listeden iki önemli sonuç çıkar. $1$ asal değildir, çünkü tanım $1$ den büyük olmayı şart koşar. $2$ ise tek çift asal sayıdır; ondan büyük her çift sayı $2$ ye bölündüğü için asal olamaz.",
            hap("En küçük asal sayı $2$ dir ve $2$ tek çift asal sayıdır.",
                "$1$ asal değildir."),
            "İki sayının $1$ den başka ortak böleni yoksa bu sayılara <strong>aralarında asal</strong> denir. Bunun için sayıların kendilerinin asal olması gerekmez. $8$ ve $15$ asal değildir, ama ortak bölenleri yalnızca $1$ olduğu için aralarında asaldır.",
            ornek(
                "İki asal sayının toplamı $25$ olsun.",
                "Bu iki sayının çarpımı kaçtır?",
                "$25$ tek sayıdır. İki sayının toplamının tek çıkması için biri tek, biri çift olmalıdır.",
                "Çift olan asal sayı yalnızca $2$ dir. Öteki sayı $25-2=23$ tür ve $23$ asaldır.",
                "Çarpım: $2 \\cdot 23=46$."),
            dikkat(
                "\"Aralarında asal\" iki sayı arasındaki bir ilişkidir, sayıların kendisinin asal olduğunu söylemez.",
                "Tersine, iki farklı asal sayı her zaman aralarında asaldır."),
        ]},
        {"baslik": "Faktöriyel", "icerik": [
            "$1$ den $n$ ye kadar olan doğal sayıların çarpımına <strong>$n$ faktöriyel</strong> denir ve $n!$ ile gösterilir:",
            "$$n!=1 \\cdot 2 \\cdot 3 \\cdots n$$",
            "Tanım gereği $0!=1$ ve $1!=1$ dir. İlk birkaç değer: $2!=2$, $3!=6$, $4!=24$, $5!=120$, $6!=720$.",
            "Faktöriyel sorularında temel araç tek bir eşitliktir: $n!=n \\cdot (n-1)!$. Büyük faktöriyeli küçüğe kadar açıp sadeleştirirsin. Böylece çok büyük sayıları hiç hesaplamadan sadeleştirebilirsin.",
            ornek(
                "$\\dfrac{7!}{5!}$ ve $5!+6!$ ifadelerini hesaplayalım.",
                "Her birinin değeri kaçtır?",
                "$7!=7 \\cdot 6 \\cdot 5!$ olduğu için $\\dfrac{7!}{5!}=7 \\cdot 6=42$.",
                "$6!=6 \\cdot 5!$ olduğu için $5!+6!=5! \\cdot (1+6)=120 \\cdot 7=840$."),
            hap("$n!=n \\cdot (n-1)!$ eşitliği sadeleştirmenin anahtarıdır.",
                "$0!=1$ dir."),
            dikkat(
                "Faktöriyel toplamaya dağılmaz: $(a+b)!$ ile $a!+b!$ farklıdır.",
                "Örneğin $2!+3!=8$ ama $5!=120$."),
            "<h3>Faktöriyelin sonundaki sıfırlar</h3>",
            "Bir sayının sonundaki her sıfır bir $10$ çarpanından, her $10$ da bir $2$ ile bir $5$ çarpanından gelir. $n!$ içinde $2$ çarpanı her zaman $5$ ten fazladır; bu yüzden sondaki sıfır sayısı $5$ çarpanlarının sayısına eşittir. $25$ gibi $5$ in kuvvetleri birden fazla $5$ çarpanı taşıdığı için onlar ayrıca sayılır.",
            ornek(
                "$25!$ sayısı verilsin.",
                "Bu sayının sonunda kaç sıfır vardır?",
                "$5$ in katları: $25 \\div 5=5$ tane ($5$, $10$, $15$, $20$, $25$).",
                "$25$ in katları bir $5$ daha taşır: $25 \\div 25=1$ tane.",
                "Toplam $5$ çarpanı: $5+1=6$. $25!$ sayısının sonunda $6$ sıfır vardır."),
        ]},
        {"baslik": "Basamak kavramı ve çözümleme", "icerik": [
            "Bir sayıdaki her rakamın bulunduğu yere göre bir değeri vardır. $347$ sayısında $4$ ün <strong>sayı değeri</strong> $4$, <strong>basamak değeri</strong> ise $40$ tır. Basamak değeri, rakamın bulunduğu basamağın değeriyle çarpımıdır.",
            "Rakamları harfle verilen sayılar üstü çizili yazılır: $\\overline{ab}$ iki basamaklı, $\\overline{abc}$ üç basamaklı bir sayıdır. Burada $ab$ bir çarpım değil, yan yana yazılmış iki rakamdır. Bu sayıları basamak değerleriyle açıp yazmaya <strong>çözümleme</strong> denir:",
            "$$\\overline{ab}=10a+b$$",
            "$$\\overline{abc}=100a+10b+c$$",
            hap("$\\overline{ab}=10a+b$ ve $\\overline{abc}=100a+10b+c$.",
                "Rakamları yer değiştiren sayılarda: $\\overline{ab}+\\overline{ba}=11(a+b)$ ve $\\overline{ab}-\\overline{ba}=9(a-b)$."),
            ornek(
                "$\\overline{ab}$ ve $\\overline{ba}$ iki basamaklı sayılar ve $\\overline{ab}-\\overline{ba}=27$ olsun.",
                "Bu koşulu sağlayan kaç tane $\\overline{ab}$ sayısı vardır?",
                "Çözümleyelim: $(10a+b)-(10b+a)=9a-9b=9(a-b)$.",
                "$9(a-b)=27$ ise $a-b=3$.",
                "$\\overline{ba}$ de iki basamaklı olduğu için $b \\geq 1$ olmalı. $b$ en az $1$, $a$ en fazla $9$ olabilir.",
                "Sayılar $41$, $52$, $63$, $74$, $85$, $96$ dır; toplam $6$ tane. Kontrol: $41-14=27$."),
        ]},
        {"baslik": "Sınavda temel kavramlar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu kavramlar tek başına değil, bir problemin içinde de gelebilir: rakamları farklı sayılar, tek ve çift sayıların toplamı, işaret soruları ve ardışık sayı toplamları bu türdendir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde aynı kavramlar kısa işlem sorularında karşına çıkabilir. Faktöriyel sadeleştirme, basamak çözümleme ve asal sayı özellikleri bu soruların temelidir."),
            "Bu konuda hız kazandıran şey ezber değil, kavramı doğru adlandırmaktır. Soruyu okurken \"burada hangi küme, hangi kural?\" diye sorarsan işlem kısa kalır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$1$ i asal saymak", "Asal sayılar $2$ den başlar"],
                ["$0$ ı tek ya da işaretli saymak", "$0$ çifttir, işaretsizdir"],
                ["$-2^4$ ile $(-2)^4$ ü aynı sanmak", "$-16$ ve $16$"],
                ["$0!=0$ yazmak", "$0!=1$"],
                ["$\\overline{ab}$ yi $a \\cdot b$ sanmak", "$\\overline{ab}=10a+b$"],
                ["Bölmede tek/çift kuralı aramak", "Bölme için kural yoktur"],
                ["Terim sayısında $+1$ i unutmak", "$\\dfrac{\\text{son}-\\text{ilk}}{\\text{artış}}+1$"],
            ]),
            "Bu hataların çoğu tanımın küçük bir ayrıntısını atlamaktan kaynaklanır: sıfırın durumu, birin asal olmaması, parantezin yeri. Tanımları ayrıntısıyla bir kez yazmak bu hataları büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("Rakam ile sayı arasındaki fark nedir?",
         "Rakam, sayıları yazmak için kullanılan sembollerdir ve onluk sistemde 0 dan 9 a kadar on tanedir. Sayı ise rakamlarla yazılan ve bir değer belirten ifadedir. Her rakam tek basamaklı bir sayıdır ama her sayı rakam değildir."),
        ("Sıfır çift sayı mıdır?",
         "Evet. Sıfır 2 ile tam bölünür, bu yüzden çift sayıdır. Ayrıca ne pozitif ne negatiftir."),
        ("1 asal sayı mıdır?",
         "Hayır. Asal sayı tanımı 1 den büyük olmayı şart koşar. En küçük asal sayı 2 dir ve 2 tek çift asal sayıdır."),
        ("Aralarında asal ne demektir?",
         "İki sayının 1 den başka ortak böleni yoksa bu sayılara aralarında asal denir. Sayıların kendilerinin asal olması gerekmez; örneğin 8 ile 15 aralarında asaldır."),
        ("Sıfır faktöriyel neden 1 dir?",
         "Tanım gereği 0 faktöriyel 1 kabul edilir. Bu kabul, n faktöriyelin n çarpı (n eksi 1) faktöriyel eşitliğinin n eşittir 1 için de geçerli olmasını sağlar."),
        ("Ardışık sayıların toplamı nasıl bulunur?",
         "Aralarındaki fark sabitse önce terim sayısı bulunur: son terimden ilk terim çıkarılır, artışa bölünür ve 1 eklenir. Toplam ise ilk ve son terimin ortalamasının terim sayısıyla çarpımıdır."),
        ("Faktöriyelin sonunda kaç sıfır olduğu nasıl bulunur?",
         "Sondaki her sıfır bir 2 ile bir 5 çarpanından gelir ve faktöriyelde 5 çarpanı daha azdır. Bu yüzden 5 çarpanları sayılır: sayı 5 e, 25 e, 125 e bölünür ve bölümlerin tam kısımları toplanır. Örneğin 25 faktöriyelin sonunda 6 sıfır vardır."),
    ],
    "kontrol": [
        "Rakam ile sayının farkını bir örnekle açıklayabiliyorum.",
        "Rakamları farklı en büyük ve en küçük sayıları yazabiliyorum.",
        "Tek ve çift sayıların toplama ve çarpmadaki sonucunu tabloya bakmadan söyleyebiliyorum.",
        "Bir ifadeden bir değişkenin tek mi çift mi olduğunu gerekçesiyle çıkarabiliyorum.",
        "$-2^4$ ile $(-2)^4$ ün farkını açıklayabiliyorum.",
        "Verilen işaret bilgisinden bir ifadenin işaretini bulabiliyorum.",
        "Ardışık bir dizinin terim sayısını ve toplamını formülle hesaplayabiliyorum.",
        "$30$ dan küçük asal sayıları sayabiliyor, $1$ in neden asal olmadığını biliyorum.",
        "Faktöriyelli bir ifadeyi $n!=n \\cdot (n-1)!$ ile sadeleştirebiliyorum.",
        "$\\overline{ab}$ biçimindeki bir sayıyı çözümleyip denklem kurabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf", "dogal-sayilar-ve-tam-sayilar", "rasyonel-sayilar-konu-anlatimi-pdf"],
}
