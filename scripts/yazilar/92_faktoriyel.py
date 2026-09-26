# scripts/yazilar/92_faktoriyel.py — Faktoriyel (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "faktoriyel-konu-anlatimi-pdf",
    "baslik": "Faktöriyel Konu Anlatımı PDF",
    "aciklama": "Faktöriyel nedir? Sıfır faktöriyel, sıralama ile bağlantı, sadeleştirme, faktöriyelli denklemler, sondaki sıfırlar, asal çarpanlar ve birler basamağı; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "sayma",
    "sinavlar": ["TYT", "AYT", "ALES", "KPSS"],
    "kapak": "faktoriyel-konu-anlatimi-pdf",
    "kapak_alt": "Faktöriyel: dallanan ahşap bir ağaç modeli üzerinde toplarla azalan seçimleri inceleyen iki öğrenci",
    "ozet": "Faktöriyel, bir sayıdan başlayıp bire kadar bütün pozitif tam sayıların çarpımıdır. İlk bakışta sıradan bir çarpım gibi görünse de sayma problemlerinin temel taşıdır: farklı nesnelerin kaç farklı sırada dizilebileceğini doğrudan verir. Bu yazıda faktöriyelin tanımını, sıfır faktöriyelin neden bire eşit olduğunu, sıralama ile bağlantısını, faktöriyelli ifadeleri sadeleştirmeyi, faktöriyelli denklemleri, faktöriyelin sonundaki sıfırları, asal çarpanlarını ve birler basamağı sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Faktöriyel nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için çarpma işlemini ve asal çarpanlara ayırmayı biliyor olman yeterli.",
                "Asal çarpanlar için <a href=\"/blog/asal-sayilar-ve-asal-carpanlara-ayirma/\">Asal Sayılar ve Asal Çarpanlara Ayırma</a> yazısına göz at."),
            "$n$ pozitif bir tam sayı olmak üzere $1$ den $n$ ye kadar bütün pozitif tam sayıların çarpımına <strong>$n$ faktöriyel</strong> denir ve $n!$ ile gösterilir:",
            "$$n!=1 \\cdot 2 \\cdot 3 \\cdots n$$",
            "Ayrıca $0!=1$ olarak tanımlanır. Ünlem işareti burada bir vurgu değil, faktöriyel işlemidir. İlk birkaç faktöriyelin değerleri şöyledir:",
            tablo(["$n$", "$n!$"], [
                ["$0$", "$1$"],
                ["$1$", "$1$"],
                ["$2$", "$2$"],
                ["$3$", "$6$"],
                ["$4$", "$24$"],
                ["$5$", "$120$"],
                ["$6$", "$720$"],
                ["$7$", "$5040$"],
            ]),
            hap("$n!$, $1$ den $n$ ye kadar bütün pozitif tam sayıların çarpımıdır.",
                "$0!=1$ ve $1!=1$ dir."),
        ]},
        {"baslik": "Özyinelemeli tanım", "icerik": [
            "Her faktöriyel bir öncekinden kolayca elde edilir: $n!=n \\cdot (n-1)!$. Örneğin $6!=6 \\cdot 5!=6 \\cdot 120=720$ dir. Bu özellik, büyük faktöriyelleri hesaplarken ve faktöriyelli ifadeleri sadeleştirirken en çok kullanılan araçtır. Bir faktöriyeli bilen, bir sonrakini tek bir çarpmayla bulur; baştan bütün çarpımı yeniden yapmaya gerek yoktur.",
            ornek(
                "$7!=5040$ olduğu biliniyor.",
                "$8!$ ve $9!$ değerlerini bulalım.",
                "$8!=8 \\cdot 7!=8 \\cdot 5040=40320$.",
                "$9!=9 \\cdot 8!=9 \\cdot 40320=362880$."),
            "Özyinelemeli tanım, faktöriyeli daha küçük bir faktöriyel cinsinden yazmayı sağlar: $10!=10 \\cdot 9 \\cdot 8 \\cdot 7!$ gibi. Bu açılım, iki faktöriyelin bölümü sorulduğunda ortak kısmı sadeleştirmenin anahtarıdır.",
        ]},
        {"baslik": "Sıfır faktöriyel neden bire eşittir?", "icerik": [
            "$0!=1$ ilk bakışta tuhaf görünür, çünkü çarpılacak hiçbir sayı yoktur. Ama bu tanım keyfî bir seçim değildir; iki güçlü gerekçesi vardır ve ikisi de aynı sonuca götürür.",
            "Birincisi özyinelemeli tanımdır. $n!=n \\cdot (n-1)!$ eşitliğinde $n=1$ yazılırsa $1!=1 \\cdot 0!$ elde edilir. $1!=1$ olduğu için $0!$ in $1$ olması gerekir.",
            "İkincisi saymadır. $n!$, $n$ farklı nesnenin kaç farklı sırada dizilebileceğini verir. Hiç nesne yokken yapılabilecek tek bir dizilim vardır: hiçbir şey yapmamak. Bu yüzden $0$ nesnenin dizilim sayısı $1$ dir.",
            dikkat(
                "$0!$ i sıfır sanmak.",
                "$0!=0$ değil, $0!=1$ dir. Bu hata, faktöriyelli ifadelerde sıfıra bölme gibi yanlış sonuçlara ve sayma sorularında sıfır sonucuna yol açar."),
        ]},
        {"baslik": "Faktöriyel ve sıralama", "icerik": [
            "Faktöriyelin en önemli anlamı saymadır: $n$ farklı nesne bir sıraya $n!$ farklı biçimde dizilebilir. Birinci sıraya $n$ nesneden biri, ikinci sıraya kalan $n-1$ nesneden biri gelir ve bu böyle devam eder. Seçenek sayıları çarpılınca $n \\cdot (n-1) \\cdots 1=n!$ bulunur.",
            ornek(
                "Üç farklı kitap, A, B ve C bir rafa dizilecek.",
                "Kaç farklı dizilim olduğunu bulalım ve dizilimleri yazalım.",
                "Birinci sıraya $3$, ikinciye $2$, üçüncüye $1$ kitap gelebilir: $3 \\cdot 2 \\cdot 1=3!=6$.",
                "Dizilimler: ABC, ACB, BAC, BCA, CAB ve CBA."),
            "Kapaktaki dallanan ağaç modeli bu düşünceyi gösterir: ilk seçimde $n$ dal, her dalda bir sonraki seçim için bir eksik dal açılır. Ağacın uçlarındaki yolların sayısı $n!$ dir.",
            ornek(
                "Beş kişi bir sıraya dizilecek.",
                "Kaç farklı sıralama olduğunu bulalım.",
                "$5!=120$ farklı sıralama vardır. Grup altı kişi olsaydı sıralama sayısı altı katına çıkıp $6!=720$ olurdu."),
            "Sıralama fikrinin genişletilmiş hâli <a href=\"/blog/permutasyon-konu-anlatimi-pdf/\">Permütasyon Konu Anlatımı PDF</a> yazısında anlatılıyor.",
            hap("Fotoğraf için yan yana duran $4$ arkadaş $4!=24$ farklı biçimde sıralanabilir.", "Gruba bir kişi daha katılınca sıralamalar $5$ katına çıkar ve $120$ olur.", gunluk=True),
        ]},
        {"baslik": "Faktöriyelli ifadeleri sadeleştirmek", "icerik": [
            "İki faktöriyelin bölümünde büyük olan faktöriyel küçük olana kadar açılır ve ortak kısım sadeleştirilir. Büyük faktöriyelleri tam olarak hesaplamaya gerek kalmaz.",
            ornek(
                "$\\dfrac{10!}{8!}$ ve $\\dfrac{7!}{5! \\cdot 2!}$ ifadeleri verilsin.",
                "İfadelerin değerini bulalım.",
                "$\\dfrac{10!}{8!}=\\dfrac{10 \\cdot 9 \\cdot 8!}{8!}=10 \\cdot 9=90$.",
                "$\\dfrac{7!}{5! \\cdot 2!}=\\dfrac{7 \\cdot 6 \\cdot 5!}{5! \\cdot 2}=\\dfrac{42}{2}=21$."),
            ornek(
                "$n$ pozitif bir tam sayı olsun.",
                "$\\dfrac{(n+1)!}{n!}$ ve $\\dfrac{(n+2)!}{n!}$ ifadelerini sadeleştirelim.",
                "$\\dfrac{(n+1)!}{n!}=\\dfrac{(n+1) \\cdot n!}{n!}=n+1$.",
                "$\\dfrac{(n+2)!}{n!}=(n+2)(n+1)$. Örneğin $n=3$ için $\\dfrac{5!}{3!}=5 \\cdot 4=20$ bulunur."),
            dikkat(
                "Faktöriyelleri sayı gibi sadeleştirmek.",
                "$\\dfrac{10!}{5!}$ ifadesi $2!$ değildir. Faktöriyeller bölünürken sayılar değil çarpımlar sadeleşir: $\\dfrac{10!}{5!}=10 \\cdot 9 \\cdot 8 \\cdot 7 \\cdot 6=30240$."),
            hap("Bölümde büyük faktöriyel küçük olana kadar açılır: $\\dfrac{10!}{7!}=10 \\cdot 9 \\cdot 8$ olur."),
        ]},
        {"baslik": "Faktöriyelli toplama ve çıkarma", "icerik": [
            "Faktöriyeller toplanırken ya da çıkarılırken en küçük faktöriyel ortak çarpan olarak paranteze alınır. Böylece büyük sayılarla uğraşmadan sonuç bulunur.",
            ornek(
                "$5!+4!$ ve $6!-5!$ işlemleri verilsin.",
                "Ortak çarpan parantezine alarak hesaplayalım.",
                "$5!+4!=5 \\cdot 4!+4!=4! \\cdot (5+1)=24 \\cdot 6=144$.",
                "$6!-5!=6 \\cdot 5!-5!=5! \\cdot (6-1)=120 \\cdot 5=600$."),
            ornek(
                "$\\dfrac{8!+7!}{7!-6!}$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "Pay: $8!+7!=7! \\cdot (8+1)=9 \\cdot 7!$. Payda: $7!-6!=6! \\cdot (7-1)=6 \\cdot 6!$.",
                "$\\dfrac{9 \\cdot 7!}{6 \\cdot 6!}=\\dfrac{9 \\cdot 7}{6}=\\dfrac{63}{6}=\\dfrac{21}{2}$."),
            dikkat(
                "$(a+b)!$ ifadesini $a!+b!$ sanmak.",
                "$(2+3)!=5!=120$ iken $2!+3!=2+6=8$ dir. Faktöriyel toplama üzerine dağılmaz. Benzer biçimde $(2n)!$ ifadesi $2 \\cdot n!$ e eşit değildir."),
        ]},
        {"baslik": "Faktöriyelli denklemler", "icerik": [
            "Bilinmeyen faktöriyelin içindeyse önce bölümler sadeleştirilir ve denklem sıradan bir denkleme dönüştürülür. Bulunan değerin faktöriyelin tanımlı olduğu doğal sayılardan olması gerekir.",
            ornek(
                "$\\dfrac{(n+1)!}{(n-1)!}=42$ denklemi verilsin.",
                "$n$ yi bulalım.",
                "$\\dfrac{(n+1)!}{(n-1)!}=(n+1) \\cdot n$.",
                "$(n+1) \\cdot n=42$. Ardışık iki sayının çarpımı $42$ ise sayılar $6$ ve $7$ dir: $n=6$.",
                "Kontrol: $\\dfrac{7!}{5!}=7 \\cdot 6=42$."),
            ornek(
                "$n!=120$ ve $(n-2)!=6$ bilgileri verilsin.",
                "$n$ yi bulalım.",
                "Tablodan $5!=120$ olduğu için $n=5$.",
                "Kontrol: $(5-2)!=3!=6$."),
        ]},
        {"baslik": "Ardışık sayıların çarpımı", "icerik": [
            "Ardışık sayıların çarpımı iki faktöriyelin bölümü olarak yazılabilir. $7 \\cdot 8 \\cdot 9 \\cdot 10$ çarpımı, $10!$ in $6!$ e bölümüdür, çünkü $10!$ içindeki $1$ den $6$ ya kadar olan çarpanlar sadeleşir.",
            ornek(
                "$7 \\cdot 8 \\cdot 9 \\cdot 10$ çarpımı verilsin.",
                "Bu çarpımı faktöriyellerle yazalım ve değerini bulalım.",
                "$7 \\cdot 8 \\cdot 9 \\cdot 10=\\dfrac{10!}{6!}$.",
                "Değer: $\\dfrac{3628800}{720}=5040$."),
            "Bu yazımdan önemli bir sonuç çıkar: art arda gelen $k$ tam sayının çarpımı her zaman $k!$ e bölünür. Örneğin $7 \\cdot 8 \\cdot 9=504$ çarpımı $3!=6$ ya bölünür: $504:6=84$. Bu sonucun nedeni, bölümün bir kombinasyon sayısına, yani bir tam sayıya eşit olmasıdır.",
        ]},
        {"baslik": "Faktöriyelle kalan soruları", "icerik": [
            "Büyük bir faktöriyel, kendisinden küçük ya da eşit bütün sayılara ve bunların birçok çarpımına tam bölünür. Bu yüzden faktöriyel içeren bir toplamın kalanı, çoğu zaman yalnızca faktöriyel olmayan terime bağlıdır.",
            ornek(
                "$20!+7$ sayısı verilsin.",
                "Bu sayının $11$ e bölümünden kalanı bulalım.",
                "$20!$ içinde $11$ çarpanı vardır; $20!$, $11$ e tam bölünür.",
                "Kalan, $7$ nin $11$ e bölümünden kalandır: $7$."),
            ornek(
                "$10!+15$ sayısı verilsin.",
                "Bu sayının $12$ ye bölümünden kalanı bulalım.",
                "$12=3 \\cdot 4$ ve $10!$ içinde $3$ ile $4$ çarpanları vardır; $10!$, $12$ ye tam bölünür.",
                "Kalan, $15$ in $12$ ye bölümünden kalandır: $3$."),
        ]},
        {"baslik": "Faktöriyelli eşitsizlikler", "icerik": [
            "Faktöriyelle kurulan eşitsizliklerde faktöriyeller sırayla hesaplanır ve koşulu ilk sağlayan değer bulunur. Faktöriyel sürekli arttığı için bir değer koşulu sağlıyorsa ondan büyük bütün değerler de sağlar.",
            ornek(
                "$n!>1000$ eşitsizliği verilsin.",
                "Bu eşitsizliği sağlayan en küçük doğal sayıyı bulalım.",
                "$6!=720$ ve $720<1000$; koşul sağlanmaz.",
                "$7!=5040$ ve $5040>1000$; koşul sağlanır.",
                "En küçük değer $n=7$ dir."),
            "Faktöriyelin basamak sayısı da aynı yolla bulunur: $10!=3628800$ yedi basamaklı, $12!=479001600$ dokuz basamaklıdır. Basamak sayısı faktöriyel büyüdükçe giderek daha hızlı artar.",
        ]},
        {"baslik": "Faktöriyelden seçim sayısına", "icerik": [
            "Faktöriyel yalnızca sıralamayı değil, seçimleri saymayı da sağlar. $n$ nesneden sırası önemli olmadan $r$ tanesini seçmenin kaç yolu olduğu, faktöriyellerle şöyle yazılır:",
            "$$\\dfrac{n!}{r! \\cdot (n-r)!}$$",
            ornek(
                "Beş kişilik bir gruptan iki kişilik bir ekip seçilecek.",
                "Kaç farklı ekip seçilebileceğini bulalım.",
                "Seçim sayısı: $\\dfrac{5!}{2! \\cdot 3!}=\\dfrac{120}{2 \\cdot 6}=10$.",
                "Aynı sonuç sıralama üzerinden de bulunur: iki kişiyi sırayla seçmenin $5 \\cdot 4=20$ yolu vardır, ama her ekip $2!=2$ kez sayılmıştır; $20:2=10$."),
            "Bu ifadenin neden böyle olduğu ve nasıl kullanıldığı <a href=\"/blog/kombinasyon-konu-anlatimi-pdf/\">Kombinasyon Konu Anlatımı PDF</a> yazısında ayrıntılı olarak anlatılıyor.",
        ]},
        {"baslik": "Faktöriyelin büyüme hızı", "icerik": [
            "Faktöriyel çok hızlı büyür ve bu büyüme sayma sorularının sonuçlarını da doğrudan etkiler. $10!$ yaklaşık $3.6$ milyondur; $2^{10}$ ise yalnızca $1024$ tür. Her adımda çarpılan sayı da büyüdüğü için faktöriyel, üstel büyümeyi bile kısa sürede geride bırakır.",
            tablo(["$n$", "$2^n$", "$n!$"], [
                ["$4$", "$16$", "$24$"],
                ["$6$", "$64$", "$720$"],
                ["$8$", "$256$", "$40320$"],
                ["$10$", "$1024$", "$3628800$"],
            ]),
            "Bu hız, sayma sorularında sonuçların neden çok büyük çıkabildiğini açıklar. $10$ kişilik bir grubun bir sıraya kaç farklı biçimde dizilebileceği sorusunun cevabı $3628800$ dür.",
        ]},
        {"baslik": "Faktöriyelin sonundaki sıfırlar", "icerik": [
            "Bir sayının sonundaki her sıfır, bir $10$ çarpanından, yani bir $2$ ile bir $5$ in çarpımından gelir. $n!$ içinde $2$ çarpanları $5$ çarpanlarından her zaman daha fazladır; bu yüzden sondaki sıfır sayısı, $n!$ içindeki $5$ çarpanlarının sayısıdır.",
            "$5$ çarpanları şöyle sayılır: $n$, $5$ e bölünür ve bölüm yazılır; bu bölüm yeniden $5$ e bölünür ve bu işlem bölüm $0$ olana kadar sürer. Bulunan bölümler toplanır.",
            ornek(
                "$25!$ ve $100!$ sayıları verilsin.",
                "Sonlarında kaç sıfır olduğunu bulalım.",
                "$25!$: $25:5=5$, $5:5=1$. Toplam $5+1=6$ sıfır.",
                "$100!$: $100:5=20$, $20:5=4$. Toplam $20+4=24$ sıfır."),
            dikkat(
                "Yalnızca $5$ in katlarını saymak.",
                "$25$, $50$, $75$ ve $100$ gibi sayılar iki tane $5$ çarpanı taşır. Bu yüzden $100!$ in sonundaki sıfır sayısı $20$ değil, $24$ tür. İkinci bölme adımı bu fazladan çarpanları sayar."),
            hap("Bir faktöriyelin sonundaki sıfır sayısı, içindeki $5$ çarpanlarının sayısına eşittir.", "Örneğin $25$ faktöriyelin sonunda $5+1=6$ sıfır vardır."),
        ]},
        {"baslik": "Faktöriyelin asal çarpanları", "icerik": [
            "Aynı yöntem herhangi bir asal sayı için kullanılır: $n!$ içindeki $p$ asal çarpanlarının sayısı, $n$ nin $p$ ye art arda bölünmesiyle bulunan bölümlerin toplamıdır.",
            ornek(
                "$10!$ sayısı verilsin.",
                "$10!$ i asal çarpanlarına ayıralım.",
                "$2$ nin kuvveti: $10:2=5$, $5:2=2$, $2:2=1$; toplam $8$.",
                "$3$ ün kuvveti: $10:3=3$, $3:3=1$; toplam $4$. $5$ in kuvveti: $2$. $7$ nin kuvveti: $1$.",
                "$10!=2^8 \\cdot 3^4 \\cdot 5^2 \\cdot 7$. Kontrol: $256 \\cdot 81 \\cdot 25 \\cdot 7=3628800$."),
            "Asal çarpanların ayrıntısı <a href=\"/blog/asal-sayilar-ve-asal-carpanlara-ayirma/\">Asal Sayılar ve Asal Çarpanlara Ayırma</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Faktöriyel ve bölünebilme", "icerik": [
            "$n!$, $1$ den $n$ ye kadar bütün sayıları çarpan olarak içerdiği için bu sayıların her birine tam bölünür. Ayrıca bu sayıların çarpımından oluşan birçok sayıya da bölünür.",
            ornek(
                "$7!$ sayısı verilsin.",
                "$7!$ in $60$ a ve $11$ e bölünüp bölünmediğini bulalım.",
                "$60=3 \\cdot 4 \\cdot 5$ ve bu çarpanların hepsi $7!$ in içinde vardır; $7!$, $60$ a bölünür: $5040:60=84$.",
                "$11$ asal bir sayıdır ve $7$ den büyüktür; $7!$ içinde $11$ çarpanı yoktur, bu yüzden $7!$, $11$ e bölünmez."),
            "Genel olarak $p$ asal sayısı $n$ den büyükse $n!$ sayısı $p$ ye bölünmez. Nedeni şudur: asal bir sayı bir çarpımı ancak çarpanlarından birini bölüyorsa böler ve $n!$ in bütün çarpanları $p$ den küçüktür. Bu gözlem, faktöriyelli ifadelerin kalan sorularında sık kullanılır.",
        ]},
        {"baslik": "Faktöriyellerin birler basamağı", "icerik": [
            "$5!=120$ olduğu için $5!$ ve daha büyük bütün faktöriyeller $10$ un katıdır ve $0$ ile biter. Bu yüzden faktöriyel toplamlarının birler basamağını yalnızca ilk dört terim belirler. Aynı fikirle, $10!$ ve sonrasının son iki basamağının $00$ olduğu da görülür, çünkü bu faktöriyeller $100$ ün katıdır.",
            ornek(
                "$1!+2!+3!+\\cdots+100!$ toplamı verilsin.",
                "Bu toplamın birler basamağını bulalım.",
                "$5!$ den itibaren her terim $0$ ile biter ve birler basamağını etkilemez.",
                "İlk dört terimin toplamı: $1+2+6+24=33$.",
                "Toplamın birler basamağı $3$ tür."),
            hap("$5!$ ve daha büyük bütün faktöriyellerin birler basamağı $0$ olur."),
        ]},
        {"baslik": "Sınavda faktöriyel", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) faktöriyel sadeleştirme, faktöriyelli işlemler ve sıralama soruları biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) faktöriyel permütasyon, kombinasyon ve olasılık sorularının içinde kullanılır; <strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de sayma sorularında gerekir."),
            "Faktöriyelli bir ifadeyle karşılaştığında önce en küçük faktöriyeli bul ve diğerlerini onun cinsinden yaz. Bu tek adım, bölme, toplama ve çıkarma sorularının neredeyse hepsini birkaç satıra indirir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$0!=0$", "$0!=1$"],
                ["$\\dfrac{10!}{5!}=2!$", "$10 \\cdot 9 \\cdot 8 \\cdot 7 \\cdot 6$"],
                ["$(a+b)!=a!+b!$", "Faktöriyel toplamaya dağılmaz"],
                ["$(2n)!=2 \\cdot n!$", "$(2n)!$ çok daha büyüktür"],
                ["Sondaki sıfırlarda yalnız ilk bölmeyi yapmak", "$25$ in katları fazladan $5$ verir"],
                ["$5!$ den büyük faktöriyelin birler basamağını hesaplamak", "Hepsi $0$ ile biter"],
            ]),
            "Bu hataların çoğu, faktöriyeli sıradan bir sayı gibi düşünmekten doğar. Faktöriyel bir çarpımdır; onu açarak yazmak ve ortak kısımları çarpım olarak sadeleştirmek hataları büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("Faktöriyel nedir?",
         "Bir pozitif tam sayıdan bire kadar bütün pozitif tam sayıların çarpımıdır. Örneğin 5 faktöriyel, 1 çarpı 2 çarpı 3 çarpı 4 çarpı 5, yani 120 dir."),
        ("Sıfır faktöriyel neden 1 dir?",
         "Özyinelemeli tanımda 1 faktöriyel, 1 çarpı 0 faktöriyel olarak yazılır ve 1 faktöriyel 1 olduğu için 0 faktöriyel de 1 olmalıdır. Ayrıca hiç nesne yokken tek bir dizilim vardır."),
        ("Faktöriyel sayma ile nasıl ilişkilidir?",
         "n farklı nesne bir sıraya n faktöriyel farklı biçimde dizilebilir. Örneğin üç farklı kitap bir rafa 6 farklı biçimde dizilir."),
        ("İki faktöriyelin bölümü nasıl hesaplanır?",
         "Büyük faktöriyel küçük olana kadar açılır ve ortak kısım sadeleştirilir. 10 faktöriyelin 8 faktöriyele bölümü 10 çarpı 9, yani 90 dır."),
        ("Bir faktöriyelin sonunda kaç sıfır vardır?",
         "Sayının 5 e art arda bölünmesiyle bulunan bölümler toplanır. 100 faktöriyelin sonunda 20 artı 4, yani 24 sıfır vardır."),
        ("Faktöriyel toplamlarının birler basamağı nasıl bulunur?",
         "5 faktöriyelden itibaren bütün faktöriyeller 0 ile bittiği için yalnızca ilk dört terimin toplamının birler basamağına bakılır."),
        ("Faktöriyel içeren bir toplamın kalanı nasıl bulunur?",
         "Faktöriyel, bölen sayının bütün asal çarpanlarını içeriyorsa tam bölünür ve kalan yalnızca faktöriyel olmayan terime bağlı kalır. 20 faktöriyel artı 7 nin 11 e bölümünden kalan 7 dir."),
        ("Ardışık sayıların çarpımı neden faktöriyele bölünür?",
         "Art arda gelen k sayının çarpımı, iki faktöriyelin bölümü olarak yazılabilir ve k faktöriyele bölündüğünde bir kombinasyon sayısı, yani bir tam sayı verir."),
        ("Faktöriyel seçim sorularında nasıl kullanılır?",
         "n nesneden r tanesini sıra gözetmeden seçmenin yolu, n faktöriyelin r faktöriyel ile n eksi r faktöriyelin çarpımına bölümüdür. Beş kişiden iki kişilik ekip 10 farklı biçimde seçilir."),
    ],
    "kontrol": [
        "Faktöriyelin tanımını yazabiliyorum.",
        "Sıfır faktöriyelin neden bire eşit olduğunu açıklayabiliyorum.",
        "Özyinelemeli tanımla faktöriyelleri hesaplayabiliyorum.",
        "Faktöriyelin sıralama sayısını verdiğini açıklayabiliyorum.",
        "İki faktöriyelin bölümünü sadeleştirebiliyorum.",
        "Faktöriyelli toplama ve çıkarmada ortak çarpanı paranteze alabiliyorum.",
        "Faktöriyelli denklemleri çözebiliyorum.",
        "Bir faktöriyelin sonundaki sıfır sayısını bulabiliyorum.",
        "Bir faktöriyeli asal çarpanlarına ayırabiliyorum.",
        "Faktöriyel toplamlarının birler basamağını bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["permutasyon-konu-anlatimi-pdf", "kombinasyon-konu-anlatimi-pdf", "asal-sayilar-ve-asal-carpanlara-ayirma"],
}
