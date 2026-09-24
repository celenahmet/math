# scripts/yazilar/65_asal_sayilar.py — Asal Sayilar ve Asal Carpanlara Ayirma (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "asal-sayilar-ve-asal-carpanlara-ayirma",
    "baslik": "Asal Sayılar ve Asal Çarpanlara Ayırma",
    "aciklama": "Asal sayılar nedir? Asallık testi, Eratosthenes kalburu, asal çarpanlara ayırma, bölen sayısı ve toplamı, faktöriyelde asal çarpan; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "asal-sayilar-ve-asal-carpanlara-ayirma",
    "kapak_alt": "Asal sayılar ve asal çarpanlara ayırma: ahşap bloklarla çarpan ağacı kuran iki öğrenci",
    "ozet": "Asal sayılar, doğal sayıların yapı taşlarıdır: 1 den büyük her doğal sayı, asal sayıların çarpımı olarak tek bir biçimde yazılabilir. Bu yazıda asal sayıyı tanımlıyor, bir sayının asal olup olmadığını hızlıca anlamayı, Eratosthenes kalburunu, asal çarpanlara ayırmanın iki yolunu, bölen sayısı ve bölenler toplamı formüllerini, tam kare ve tam küp yapmayı ve faktöriyelde asal çarpan saymayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Asal sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için bölme işlemini, üslü sayıları ve bölünebilme kurallarını biliyor olman yeterli.",
                "Bölünebilme kuralları için <a href=\"/blog/bolunebilme-kurallari-konu-anlatimi-pdf/\">Bölünebilme Kuralları Konu Anlatımı PDF</a> yazısına göz at."),
            "$1$ den büyük olup $1$ ve kendisinden başka pozitif böleni olmayan doğal sayılara <strong>asal sayı</strong> denir. Örneğin $7$ nin pozitif bölenleri yalnızca $1$ ve $7$ dir; bu yüzden $7$ asaldır. $12$ ise $2$, $3$, $4$ ve $6$ ya da bölünür; asal değildir.",
            "$1$ den büyük olup asal olmayan sayılara <strong>bileşik sayı</strong> denir. $0$ ve $1$ ne asal ne bileşiktir.",
            "$100$ den küçük $25$ asal sayı vardır:",
            "$$2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97$$",
            dikkat(
                "$1$ asal sayı değildir.",
                "$1$ in yalnızca bir pozitif böleni vardır. Asal sayının tam olarak iki pozitif böleni olmalıdır: $1$ ve kendisi.",
                "$1$ asal sayılsaydı, aşağıda göreceğimiz asal çarpanlara ayırmanın tekliği bozulurdu: $6=2 \\cdot 3=1 \\cdot 2 \\cdot 3$ gibi sonsuz farklı yazım ortaya çıkardı."),
            hap("Asal sayının tam olarak iki pozitif böleni vardır: $1$ ve kendisi.",
                "$2$ tek çift asal sayıdır; $1$ asal değildir."),
        ]},
        {"baslik": "Asal sayıların özellikleri", "icerik": [
            "<ul><li><strong>$2$ tek çift asaldır.</strong> $2$ den büyük her çift sayı $2$ ye bölündüğü için asal olamaz.</li>"
            "<li><strong>$2$ ve $3$ ten sonraki asallar $6k-1$ ya da $6k+1$ biçimindedir.</strong> Diğer biçimler ($6k$, $6k+2$, $6k+3$, $6k+4$) $2$ ye ya da $3$ e bölünür.</li>"
            "<li><strong>Asal sayılar sonsuz tanedir.</strong> Bunun kanıtı aşağıda.</li></ul>",
            dikkat(
                "$6k \\pm 1$ biçimi asal olmanın yeterli koşulu değildir.",
                "$25=6 \\cdot 4+1$ bu biçimdedir ama $25=5 \\cdot 5$ olduğu için asal değildir. Biçim yalnızca adayları daraltır."),
            "<h3>Asal sayılar neden bitmez?</h3>",
            "Asal sayıların sonlu sayıda olduğunu varsayalım ve hepsini çarpıp $1$ ekleyelim. Elde edilen sayı listedeki hiçbir asala tam bölünmez; çünkü her birine bölümünden kalan $1$ dir. Oysa $1$ den büyük her sayının en az bir asal böleni vardır. Bu asal bölen listede olmadığına göre liste eksiktir. Demek ki asal sayılar sonsuz tanedir. Bu kanıt Öklid'e atfedilir.",
            dikkat(
                "Kanıttaki sayının kendisi asal olmak zorunda değildir.",
                "$2 \\cdot 3 \\cdot 5 \\cdot 7 \\cdot 11 \\cdot 13+1=30031$ dir ve $30031=59 \\cdot 509$ dur. Kanıt yalnızca listede olmayan bir asal bölenin varlığını gösterir."),
        ]},
        {"baslik": "Asal sayılarla sayma soruları", "icerik": [
            "Asal sayı listesini bilmek, aralıktaki asalları sayma sorularını hızlandırır. Listeyi ezberlemek yerine kök kuralıyla tek tek kontrol etmek de mümkündür.",
            ornek(
                "$20$ ile $40$ arasındaki doğal sayılar verilsin.",
                "Bu aralıktaki asal sayıları bulalım.",
                "Çift sayılar ve $5$ ile biten sayılar elenir. Kalanlar: $21, 23, 27, 29, 31, 33, 37, 39$.",
                "$21$, $27$, $33$ ve $39$, $3$ e bölünür.",
                "Asallar: $23, 29, 31, 37$; toplam $4$ tane."),
            "İki basamaklı en büyük asal sayı $97$, üç basamaklı en küçük asal sayı $101$ dir.",
            "<h3>İki asalın toplamı tekse</h3>",
            "İki tek sayının toplamı çifttir. Bu yüzden toplamı tek olan iki asaldan biri mutlaka çift asal, yani $2$ olmalıdır. Örneğin toplamı $15$ olan iki asal sayı $2$ ve $13$ tür.",
        ]},
        {"baslik": "Bir sayı asal mı? Kök kuralı", "icerik": [
            "Bir $n$ sayısının asal olup olmadığını anlamak için $n$ ye kadar bütün sayılara bölmek gerekmez. Karekökü $\\sqrt{n}$ den küçük ya da ona eşit asallara bölmek yeter. Bunların hiçbiri $n$ yi bölmüyorsa $n$ asaldır.",
            "Nedeni şudur: $n=a \\cdot b$ ve $a \\leq b$ ise $a \\cdot a \\leq a \\cdot b=n$, yani $a \\leq \\sqrt{n}$ dir. Bileşik bir sayının mutlaka $\\sqrt{n}$ den büyük olmayan bir böleni, dolayısıyla böyle bir asal böleni vardır.",
            ornek(
                "$221$ ve $211$ sayıları verilsin.",
                "Asal olup olmadıklarını bulalım.",
                "$14^2=196$ ve $15^2=225$ olduğu için iki sayının da karekökü $14$ ile $15$ arasındadır. Denenecek asallar: $2, 3, 5, 7, 11, 13$.",
                "$221$: $13$ e bölünür, $221=13 \\cdot 17$. Asal değildir.",
                "$211$: $2, 3, 5, 7, 11, 13$ ün hiçbirine bölünmez. Asaldır."),
        ]},
        {"baslik": "Eratosthenes kalburu", "icerik": [
            "Belirli bir sayıya kadar olan bütün asalları bulmanın eski ve düzenli bir yolu, Eratosthenes kalburudur. $50$ ye kadar olan asallar için:",
            "<ol><li>$2$ den $50$ ye kadar olan sayıları yaz.</li>"
            "<li>$2$ yi asal olarak işaretle ve $2$ nin kendisinden büyük bütün katlarını sil.</li>"
            "<li>Silinmemiş ilk sayı $3$; onu işaretle ve katlarını sil.</li>"
            "<li>Aynı işlemi $5$ ve $7$ için yap.</li>"
            "<li>$7^2=49 \\leq 50$ ama $11^2=121>50$ olduğu için burada durabilirsin. Silinmeden kalan bütün sayılar asaldır.</li></ol>",
            "Sonuçta $50$ ye kadar $15$ asal kalır: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47$. Kalburun durma noktası da kök kuralından gelir: $\\sqrt{50}$ den büyük bir asalın $50$ ye kadar olan ve kendisinden büyük katları, daha küçük bir asalın katı olarak zaten silinmiştir. Aynı yöntem $100$ e kadar uygulanırsa yine $2$, $3$, $5$ ve $7$ nin katlarını silmek yeter, çünkü $11^2=121>100$ dür; geriye $25$ asal kalır.",
        ]},
        {"baslik": "Asal çarpanlara ayırma", "icerik": [
            "Bir sayıyı asal sayıların çarpımı olarak yazmaya <strong>asal çarpanlara ayırma</strong> denir. <strong>Aritmetiğin temel teoremine</strong> göre $1$ den büyük her doğal sayı asal çarpanlarına ayrılabilir ve bu ayrılış, çarpanların sırası dışında tektir.",
            "<h3>Bölme merdiveni</h3>",
            "Sayı, bölünebildiği en küçük asaldan başlayarak tekrar tekrar bölünür; bölüm $1$ olunca durulur. Kullanılan bölenler asal çarpanlardır.",
            ornek(
                "$360$ sayısı verilsin.",
                "Asal çarpanlarına ayıralım.",
                "$360:2=180$, $180:2=90$, $90:2=45$.",
                "$45:3=15$, $15:3=5$.",
                "$5:5=1$.",
                "Sonuç: $360=2^3 \\cdot 3^2 \\cdot 5$."),
            "<h3>Çarpan ağacı</h3>",
            "Sayı herhangi iki çarpana ayrılır; asal olmayan her dal yeniden ayrılır. Hangi çarpanlarla başlanırsa başlansın, sonunda aynı asallara ulaşılır.",
            ornek(
                "$1260$ sayısı verilsin.",
                "Çarpan ağacıyla asal çarpanlarına ayıralım.",
                "$1260=36 \\cdot 35$.",
                "$36=4 \\cdot 9=2^2 \\cdot 3^2$ ve $35=5 \\cdot 7$.",
                "Sonuç: $1260=2^2 \\cdot 3^2 \\cdot 5 \\cdot 7$."),
            hap("Asal çarpanlara ayırma, sıralama dışında tektir.",
                "Bölme merdiveninde en küçük asaldan başla; bölüm $1$ olunca dur."),
        ]},
        {"baslik": "Bölen sayısı ve bölenler toplamı", "icerik": [
            "Asal çarpanlara ayrılmış bir sayının kaç böleni olduğu, bölenleri tek tek yazmadan bulunur. $n=p^a \\cdot q^b \\cdot r^c$ ise $n$ nin her pozitif böleni $p^x \\cdot q^y \\cdot r^z$ biçimindedir ve $x$ için $a+1$, $y$ için $b+1$, $z$ için $c+1$ seçenek vardır:",
            "$$\\text{Pozitif bölen sayısı}=(a+1)(b+1)(c+1)$$",
            ornek(
                "$360=2^3 \\cdot 3^2 \\cdot 5$ verilsin.",
                "Pozitif bölen sayısını, tam sayı bölen sayısını ve asal olmayan pozitif bölen sayısını bulalım.",
                "Pozitif bölen sayısı: $(3+1)(2+1)(1+1)=4 \\cdot 3 \\cdot 2=24$.",
                "Her pozitif bölenin bir de negatifi vardır: tam sayı bölen sayısı $2 \\cdot 24=48$.",
                "Asal bölenler $2$, $3$ ve $5$; asal olmayan pozitif bölen sayısı $24-3=21$."),
            "Pozitif bölenlerin toplamı da benzer bir çarpımla bulunur: her asalın $0$ dan kendi üssüne kadar olan kuvvetleri toplanır ve bu toplamlar çarpılır.",
            ornek(
                "$360=2^3 \\cdot 3^2 \\cdot 5$ verilsin.",
                "Pozitif bölenlerinin toplamını bulalım.",
                "$2$ için: $1+2+4+8=15$. $3$ için: $1+3+9=13$. $5$ için: $1+5=6$.",
                "Toplam: $15 \\cdot 13 \\cdot 6=1170$."),
            hap("$n=p^a \\cdot q^b \\cdot r^c$ ise pozitif bölen sayısı $(a+1)(b+1)(c+1)$ dir.",
                "Tam sayı bölen sayısı, pozitif bölen sayısının iki katıdır."),
            dikkat(
                "Bölen sayısı formülü, sayı asal çarpanlarına tam ayrılmadan uygulanmaz.",
                "$360=4 \\cdot 90$ gibi asal olmayan çarpanlarla formül uygulanırsa yanlış sonuç çıkar. Önce bütün çarpanlar asal olmalıdır."),
        ]},
        {"baslik": "Tek bölenler ve tam kare bölenler", "icerik": [
            "Bölen sayısı formülü, belirli türden bölenleri saymak için de uyarlanır. Tek bölenler, $2$ nin kuvvetini içermeyen bölenlerdir; tam kare bölenler ise her asalın üssü çift olan bölenlerdir.",
            ornek(
                "$360=2^3 \\cdot 3^2 \\cdot 5$ verilsin.",
                "Tek ve çift pozitif bölenlerin sayısını bulalım.",
                "Tek bölenlerde $2$ nin üssü $0$ olmalı; geriye $3^2 \\cdot 5=45$ in bölenleri kalır: $(2+1)(1+1)=6$ tane.",
                "Çift bölen sayısı: $24-6=18$."),
            ornek(
                "Aynı $360$ sayısı verilsin.",
                "Tam kare olan pozitif bölenlerinin sayısını bulalım.",
                "Üsler çift olmalı: $2$ için $0$ ya da $2$, $3$ için $0$ ya da $2$, $5$ için yalnızca $0$.",
                "Seçenek sayısı: $2 \\cdot 2 \\cdot 1=4$. Bu bölenler $1$, $4$, $9$ ve $36$ dır."),
            "Farklı asal çarpanları sorulduğunda üslere bakılmaz: $360$ ın farklı asal çarpanları $2$, $3$ ve $5$ tir; toplamları $10$ dur.",
        ]},
        {"baslik": "Tam kare ve tam küp yapmak", "icerik": [
            "Bir sayı, asal çarpanlarının bütün üsleri çiftse <strong>tam karedir</strong>; bütün üsleri $3$ ün katıysa <strong>tam küptür</strong>. Bir sayıyı tam kare ya da tam küp yapmak için eksik üsler tamamlanır.",
            ornek(
                "$360=2^3 \\cdot 3^2 \\cdot 5$ verilsin.",
                "$360$ ı tam kare yapmak için çarpılması gereken en küçük doğal sayıyı bulalım.",
                "Tek üslü çarpanlar: $2^3$ ve $5^1$. Her birini bir kez daha çarparsak üsler çift olur.",
                "Gereken sayı $2 \\cdot 5=10$.",
                "Kontrol: $360 \\cdot 10=3600=60^2$."),
            ornek(
                "Aynı $360$ sayısı verilsin.",
                "Tam küp yapmak için çarpılması gereken en küçük doğal sayıyı bulalım.",
                "Üsler $3$ ün katı olmalı: $2^3$ tamam, $3^2$ için bir $3$, $5^1$ için iki $5$ eksik.",
                "Gereken sayı $3 \\cdot 5^2=75$.",
                "Kontrol: $360 \\cdot 75=27000=30^3$."),
        ]},
        {"baslik": "Faktöriyelde asal çarpan", "icerik": [
            "$n!$, $1$ den $n$ ye kadar olan doğal sayıların çarpımıdır. Bir $p$ asalının $n!$ içinde kaçıncı kuvvetle bulunduğunu bulmak için $n$ art arda $p$ ye bölünür ve bölümlerin tam kısımları toplanır. Her bölüm, $p$ nin, $p^2$ nin, $p^3$ ün katlarının sayısını verir.",
            ornek(
                "$20!$ verilsin.",
                "$20!$ içinde $2$ nin üssünü bulalım.",
                "$20:2=10$, $10:2=5$, $5:2=2$ (tam kısım), $2:2=1$.",
                "Toplam: $10+5+2+1=18$. Yani $20!$, $2^{18}$ e bölünür ama $2^{19}$ a bölünmez."),
            ornek(
                "$100!$ verilsin.",
                "$100!$ sayısının sonunda kaç sıfır olduğunu bulalım.",
                "Sondaki her sıfır bir $10=2 \\cdot 5$ çarpanından gelir. $2$ ler $5$ lerden fazla olduğu için $5$ leri saymak yeter.",
                "$100:5=20$ ve $20:5=4$.",
                "Toplam $20+4=24$; $100!$ sayısının sonunda $24$ sıfır vardır."),
        ]},
        {"baslik": "Aralarında asal sayılar", "icerik": [
            "Ortak asal çarpanı olmayan, yani $1$ den başka ortak pozitif böleni bulunmayan sayılara <strong>aralarında asal</strong> denir. Bu sayıların kendilerinin asal olması gerekmez.",
            ornek(
                "$8$ ve $15$ sayıları verilsin.",
                "Aralarında asal olup olmadıklarını bulalım.",
                "$8=2^3$ ve $15=3 \\cdot 5$; ortak asal çarpan yok.",
                "İkisi de asal değildir ama aralarında asaldır."),
            "Ardışık iki doğal sayı her zaman aralarında asaldır; çünkü ikisini birden bölen bir sayı, farkları olan $1$ i de bölmek zorundadır. Örneğin $14$ ile $15$ ardışıktır ve aralarında asaldır; $14$ ile $21$ ise ortak bölenleri $7$ olduğu için aralarında asal değildir. Aralarında asallık, EBOB ve EKOK konusunun ve birleşik sayılarla bölünebilmenin temelidir.",
        ]},
        {"baslik": "Günlük hayatta asal sayılar", "icerik": [
            "Asal sayılar yalnızca ders konusu değildir. İnternette kullanılan bazı şifreleme yöntemleri, iki büyük asal sayıyı çarpmanın kolay, ama çarpımı yeniden asal çarpanlarına ayırmanın çok zor olmasına dayanır. Küçük sayılarda asal çarpanlara ayırma saniyeler sürer; yüzlerce basamaklı sayılarda ise bilinen yöntemlerle çok uzun zaman alır.",
            "Bu fark, çarpmanın ve çarpanlara ayırmanın aynı zorlukta olmadığını gösterir: $13 \\cdot 17=221$ işlemi bir adımda yapılır, ama $221$ in çarpanlarını bulmak için kök kuralıyla asalları tek tek denemek gerekir.",
        ]},
        {"baslik": "Sınavda asal sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu asal çarpanlara ayırma, bölen sayısı, tam kare ve tam küp yapma ve faktöriyelin sonundaki sıfırlar biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde asal sayı bilgisi sayı problemlerinde, bir sayının hangi çarpanlardan oluştuğunu görmek için de gerekebilir."),
            "Asal çarpanlara ayırma, sayılarla ilgili birçok konunun ortak başlangıç noktasıdır: bölünebilme, bölen sayısı, EBOB ve EKOK, tam kare ve köklü sayıları sadeleştirme. Sayıyı asallarına ayırdığında, bu soruların hepsinde aynı tablo üzerinden ilerlersin.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$1$ i asal saymak", "$1$ asal değildir"],
                ["$2$ yi tek sayı sanmak", "$2$ çift ve asaldır"],
                ["$6k \\pm 1$ olanı asal sanmak", "$25$ asal değildir"],
                ["Asal olmayan çarpanla bölen saymak", "Önce asallara ayır"],
                ["Tam sayı bölenlerde negatifleri unutmak", "Pozitif bölenlerin iki katı"],
                ["Sondaki sıfırlarda $2$ leri saymak", "$5$ leri say"],
            ]),
            "Bu hatalar, tanımın ayrıntısını atlamaktan doğar: asal sayının tam olarak iki pozitif böleni vardır ve formüllerin hepsi sayının asal çarpanlarına tam ayrılmış olmasını gerektirir.",
        ]},
    ],
    "sss": [
        ("1 asal sayı mıdır?",
         "Hayır. Asal sayının tam olarak iki pozitif böleni olmalıdır; 1 in yalnızca bir pozitif böleni vardır."),
        ("En küçük asal sayı kaçtır?",
         "2 dir. 2 aynı zamanda tek çift asal sayıdır."),
        ("100 den küçük kaç asal sayı vardır?",
         "25 asal sayı vardır. En büyüğü 97 dir."),
        ("Bir sayının asal olup olmadığı nasıl anlaşılır?",
         "Sayının karekökünden küçük ya da ona eşit asallara bölünüp bölünmediğine bakılır. Hiçbirine bölünmüyorsa sayı asaldır."),
        ("Pozitif bölen sayısı nasıl bulunur?",
         "Sayı asal çarpanlarına ayrılır, her asalın üssüne 1 eklenir ve bu sayılar çarpılır. Örneğin 360 ın 24 pozitif böleni vardır."),
        ("Asal çarpanlara ayırma neden tektir?",
         "Aritmetiğin temel teoremine göre 1 den büyük her doğal sayının asal çarpanlarına ayrılışı, çarpanların sırası dışında tektir. Hangi yolla başlanırsa başlansın aynı asallara ve aynı üslere ulaşılır."),
        ("Aralarında asal ne demektir?",
         "1 den başka ortak pozitif böleni olmayan sayılar demektir. 8 ve 15 gibi, sayıların kendilerinin asal olması gerekmez."),
    ],
    "kontrol": [
        "Asal sayıyı iki pozitif bölen koşuluyla tanımlayabiliyorum.",
        "$1$ in neden asal olmadığını açıklayabiliyorum.",
        "$100$ den küçük asal sayıları sayabiliyorum.",
        "Bir sayının asallığını kök kuralıyla kontrol edebiliyorum.",
        "Eratosthenes kalburunu uygulayabiliyorum.",
        "Bir sayıyı bölme merdiveni ve çarpan ağacıyla asal çarpanlarına ayırabiliyorum.",
        "Pozitif ve tam sayı bölen sayısını formülle bulabiliyorum.",
        "Bir sayıyı tam kare ya da tam küp yapan en küçük çarpanı bulabiliyorum.",
        "Faktöriyelde bir asalın üssünü ve sondaki sıfır sayısını bulabiliyorum.",
        "Aralarında asal sayılara örnek verebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["bolunebilme-kurallari-konu-anlatimi-pdf", "uslu-sayilar-konu-anlatimi-pdf", "temel-kavramlar-konu-anlatimi-pdf"],
}
