# scripts/yazilar/58_ardisik_sayilar.py — Ardisik Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "ardisik-sayilar",
    "baslik": "Ardışık Sayılar",
    "aciklama": "Ardışık sayılar nedir? Terim sayısı, ardışık sayıların toplamı, kareler ve küpler toplamı, çarpımda bölünebilme ve problemler; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "ardisik-sayilar",
    "kapak_alt": "Ardışık sayılar: ahşap tabla üzerinde eşit adımlarla yükselen bloklar ve eşit aralıklarla dizilmiş mavi toplarla çalışan öğrenci",
    "ozet": "Ardışık sayılar, belirli bir adımla düzenli olarak artan sayılardır ve sayı problemlerinde kullanılan temel araçlardan biridir. Bu yazıda ardışık sayıları harfle yazmayı, bir dizide kaç terim olduğunu bulmayı, ardışık sayıların toplamını tek bir formülle hesaplamayı, kareler ve küpler toplamını, ardışık sayıların çarpımındaki bölünebilme özelliklerini ve klasik ardışık sayı problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Ardışık sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için tam sayıları ve tek-çift sayı kavramını biliyor olman yeterli.",
                "Tek ve çift sayıların özellikleri için <a href=\"/blog/tek-ve-cift-sayilar/\">Tek ve Çift Sayılar</a> yazısına göz at."),
            "Belirli bir kurala göre <strong>eşit adımlarla</strong> artan sayılara ardışık sayılar denir. En yaygın olanı ardışık tam sayılardır: her sayı bir öncekinden $1$ fazladır. $4, 5, 6, 7$ ya da $-2, -1, 0, 1$ bu türden dizilerdir. Negatif sayılar ve sıfır da ardışık dizilerde yer alabilir.",
            "Adımın $1$ olması gerekmez. Ardışık çift sayılarda ve ardışık tek sayılarda adım $2$ dir: $6, 8, 10$ ve $11, 13, 15$ gibi. Ardışık $5$ in katlarında adım $5$ tir: $15, 20, 25$ gibi. Hangi adım seçilirse seçilsin, ardışık bir dizide komşu iki terimin farkı hep aynıdır.",
            hap("Ardışık sayılarda komşu iki terimin farkı sabittir; bu farka <strong>artış miktarı</strong> ya da adım denir.",
                "Ardışık tam sayılarda adım $1$, ardışık tek ve ardışık çift sayılarda adım $2$ dir."),
        ]},
        {"baslik": "Ardışık sayıları harfle yazmak", "icerik": [
            "Problemlerde ardışık sayılar genellikle bilinmez. Onları tek bir harfle ifade etmek, soruyu tek bilinmeyenli bir denkleme çevirir:",
            tablo(["Tür", "Genel yazım", "Adım"], [
                ["Ardışık tam sayılar", "$n, n+1, n+2, \\ldots$", "$1$"],
                ["Ardışık çift sayılar", "$2n, 2n+2, 2n+4, \\ldots$", "$2$"],
                ["Ardışık tek sayılar", "$2n+1, 2n+3, 2n+5, \\ldots$", "$2$"],
                ["Ardışık $k$ nın katları", "$kn, kn+k, kn+2k, \\ldots$", "$k$"],
            ]),
            "Terim sayısı tek olduğunda ortadaki terimi $x$ almak işlemi kısaltır. Üç ardışık tam sayı $x-1$, $x$, $x+1$ olarak yazılırsa toplamları doğrudan $3x$ olur; artılar ve eksiler birbirini götürür. Beş ardışık çift sayı da $x-4$, $x-2$, $x$, $x+2$, $x+4$ olarak yazılabilir ve toplamları $5x$ olur.",
            dikkat(
                "Ardışık tek sayıları $x$, $x+1$, $x+2$ diye yazmak yanlıştır.",
                "$x$ tek ise $x+1$ çifttir. Ardışık tek sayılar da ardışık çift sayılar da $x$, $x+2$, $x+4$ biçiminde yazılır; $x$ in tek mi çift mi olduğunu sorudaki bilgi belirler."),
        ]},
        {"baslik": "Terim sayısı nasıl bulunur?", "icerik": [
            "Ardışık bir dizide kaç terim olduğunu saymak için hepsini yazmak gerekmez. İlk terim, son terim ve adım biliniyorsa şu formül yeter:",
            "$$\\text{Terim sayısı}=\\dfrac{\\text{Son terim}-\\text{İlk terim}}{\\text{Adım}}+1$$",
            "Sondaki $+1$ in nedeni basittir. $3$ ten $7$ ye kadar olan tam sayılar $3, 4, 5, 6, 7$ dir. Aradaki fark $7-3=4$ adım eder, ama sayı sayısı $5$ tir: dört adım, beş durak demektir. Bir çitin direklerini sayarken de aynı durum vardır; $4$ aralık için $5$ direk gerekir.",
            ornek(
                "$7$ den $91$ e kadar olan tek sayılar verilsin.",
                "Bu dizide kaç terim vardır?",
                "İlk terim $7$, son terim $91$, adım $2$.",
                "Formülü uygulayalım: $\\dfrac{91-7}{2}+1=42+1$.",
                "Dizide $43$ terim vardır."),
            ornek(
                "$15$ ile $120$ arasındaki, $15$ ve $120$ dahil, $5$ in katları verilsin.",
                "Kaç tane olduklarını bulalım.",
                "İlk terim $15$, son terim $120$, adım $5$.",
                "$\\dfrac{120-15}{5}+1=21+1=22$.",
                "$22$ tane $5$ in katı vardır."),
            ornek(
                "İki basamaklı doğal sayılar verilsin.",
                "Bunlardan kaç tanesi $3$ ile tam bölünür?",
                "$3$ ile bölünen en küçük iki basamaklı sayı $12$, en büyüğü $99$.",
                "Adım $3$ olan bu dizide terim sayısı: $\\dfrac{99-12}{3}+1=29+1$.",
                "$30$ tane iki basamaklı sayı $3$ ile tam bölünür."),
            dikkat(
                "Soruda \"arasında\" ile \"dahil\" ifadelerine dikkat et.",
                "$10$ ile $20$ arasındaki tam sayılar $11, 12, \\ldots, 19$ dur ve $9$ tanedir. Uç değerler dahil edilirse $10$ ve $20$ de sayılır ve $11$ tane olur."),
            hap("Bir kitabın $23$ ile $58$ numaralı sayfaları arasında, bu iki sayfa dahil, $58-23+1=36$ sayfa vardır.", "Sondaki $1$, ilk sayfanın da sayılması içindir.", gunluk=True),
        ]},
        {"baslik": "Kaçıncı terim?", "icerik": [
            "Terim sayısı formülü tersinden de kullanılır. İlk terimi ve adımı bilinen bir dizide herhangi bir terimi bulmak için ilk terime adım, terimin sırasından bir eksik kadar eklenir:",
            "$$n \\text{. terim}=\\text{İlk terim}+(n-1) \\cdot \\text{Adım}$$",
            "Burada da $n-1$ in sebebi aynıdır: birinci terimden $n$ inci terime gitmek için $n-1$ adım atılır.",
            ornek(
                "$5, 9, 13, 17, \\ldots$ dizisi verilsin.",
                "Dizinin $20$ nci terimini ve $101$ in kaçıncı terim olduğunu bulalım.",
                "İlk terim $5$, adım $4$. Yirminci terim: $5+19 \\cdot 4=5+76=81$.",
                "$101$ in sırası için terim sayısı formülünü kullanalım: $\\dfrac{101-5}{4}+1=24+1=25$.",
                "Yirminci terim $81$, $101$ ise $25$ inci terimdir."),
            "Adım negatif de olabilir; bu durumda dizi azalır. $100$ den başlayıp geriye doğru yedişer sayıldığını düşünelim: $100, 93, 86, \\ldots$ Bu dizide $2$ nin kaçıncı terim olduğunu bulmak için farkı adımın büyüklüğüne bölmek yeter: $\\dfrac{100-2}{7}+1=14+1=15$. Yani $2$, on beşinci terimdir.",
            dikkat(
                "Bir sayının dizide olup olmadığını kontrol etmeden sırasını hesaplama.",
                "$5, 9, 13, \\ldots$ dizisinde $50$ var mı? $\\dfrac{50-5}{4}$ tam sayı çıkmaz; bu yüzden $50$ bu dizinin terimi değildir. Bölme tam çıkmıyorsa sayı dizide yoktur."),
        ]},
        {"baslik": "Ardışık sayıların toplamı", "icerik": [
            "$1$ den $100$ e kadar olan sayıların toplamını tek tek toplamak uzun sürer. Matematikçi Gauss'a atfedilen yöntemde ilk ve son terimler eşleştirilir: $1+100=101$, $2+99=101$, $3+98=101$ ve bu böyle devam eder. $100$ sayı, $50$ çift oluşturur ve her çiftin toplamı $101$ dir:",
            "$$1+2+3+\\cdots+100=50 \\cdot 101=5050$$",
            "Aynı fikir her ardışık diziye uygulanır. İlk terimle son terimin toplamı, baştan ikinci ile sondan ikincinin toplamına eşittir ve bu eşitlik dizinin ortasına kadar sürer. Bu yüzden:",
            "$$\\text{Toplam}=\\dfrac{(\\text{İlk terim}+\\text{Son terim}) \\cdot \\text{Terim sayısı}}{2}$$",
            ornek(
                "$21+23+25+\\cdots+59$ toplamı verilsin.",
                "Toplamın değerini bulalım.",
                "Önce terim sayısı: $\\dfrac{59-21}{2}+1=19+1=20$.",
                "Formülü uygulayalım: $\\dfrac{(21+59) \\cdot 20}{2}=\\dfrac{80 \\cdot 20}{2}$.",
                "Toplam $800$ dür."),
            "<h3>Özel toplamlar</h3>",
            "Genel formülden elde edilen üç özel toplam, sorularda çok zaman kazandırır:",
            tablo(["Toplam", "Sonuç"], [
                ["$1+2+3+\\cdots+n$", "$\\dfrac{n(n+1)}{2}$"],
                ["$2+4+6+\\cdots+2n$", "$n(n+1)$"],
                ["$1+3+5+\\cdots+(2n-1)$", "$n^2$"],
            ]),
            "Burada $n$ her zaman <strong>terim sayısıdır</strong>. Çift sayılar toplamında son terim $2n$, tek sayılar toplamında son terim $2n-1$ olduğu için $n$ yi son terimden hesaplamak gerekir.",
            ornek(
                "Üç toplam verilsin: $1+2+\\cdots+40$, $2+4+\\cdots+60$ ve $1+3+\\cdots+49$.",
                "Üçünün değerini bulalım.",
                "Birincide $n=40$: $\\dfrac{40 \\cdot 41}{2}=820$.",
                "İkincide son terim $60=2n$, yani $n=30$: $30 \\cdot 31=930$.",
                "Üçüncüde son terim $49=2n-1$, yani $n=25$: $25^2=625$."),
            hap("Ardışık bir dizinin toplamı, ilk ve son terimin ortalaması ile terim sayısının çarpımıdır.",
                "Özel toplamlarda $n$ terim sayısıdır; son terimle karıştırma."),
        ]},
        {"baslik": "Aradan başlayan toplamlar", "icerik": [
            "Toplam $1$ den başlamıyorsa iki yol vardır: genel formülü doğrudan kullanmak ya da büyük toplamdan küçük toplamı çıkarmak. İkinci yol, özel toplam formüllerini ezbere bilenler için hızlıdır.",
            ornek(
                "$11+12+13+\\cdots+30$ toplamı verilsin.",
                "Toplamı iki yoldan bulalım.",
                "Çıkarma yoluyla: $1$ den $30$ a kadar toplam $\\dfrac{30 \\cdot 31}{2}=465$, $1$ den $10$ a kadar toplam $55$.",
                "Aranan toplam $465-55=410$.",
                "Genel formülle: terim sayısı $20$, toplam $\\dfrac{(11+30) \\cdot 20}{2}=410$. İki yol aynı sonucu verir."),
            ornek(
                "$40+42+44+\\cdots+80$ toplamı verilsin.",
                "Toplamı bulalım.",
                "Terim sayısı: $\\dfrac{80-40}{2}+1=21$.",
                "Toplam: $\\dfrac{(40+80) \\cdot 21}{2}=60 \\cdot 21=1260$.",
                "Kontrol: toplam $2 \\cdot (20+21+\\cdots+40)$ olarak da yazılabilir ve $2 \\cdot (820-190)=1260$ bulunur."),
            dikkat(
                "Çıkarma yolunda çıkarılan toplamın son terimine dikkat et.",
                "$11$ den başlayan bir toplam için $1$ den $10$ a kadar olan toplam çıkarılır; $11$ e kadar olan değil. Yoksa $11$ de yanlışlıkla çıkarılmış olur."),
        ]},
        {"baslik": "Ortalama ve ortadaki terim", "icerik": [
            "Ardışık bir dizinin ortalaması, ilk ve son terimin ortalamasına eşittir. Terim sayısı tekse bu ortalama tam ortadaki terimdir. Bu özellik, toplamı verilen ardışık sayıları bulmanın en kısa yoludur: toplamı terim sayısına bölersen ortayı bulursun.",
            ornek(
                "Beş ardışık tam sayının toplamı $115$ olsun.",
                "Bu sayılardan en büyüğü kaçtır?",
                "Ortalama $115:5=23$; terim sayısı tek olduğu için ortadaki sayı $23$ tür.",
                "Sayılar: $21, 22, 23, 24, 25$.",
                "En büyüğü $25$ tir."),
            ornek(
                "Dört ardışık çift sayının toplamı $100$ olsun.",
                "Bu sayıları bulalım.",
                "Ortalama $100:4=25$. Terim sayısı çift olduğu için ortada bir terim yoktur; $25$, ortadaki iki terimin tam ortasıdır.",
                "$25$ in iki yanındaki ardışık çift sayılar $24$ ve $26$.",
                "Sayılar: $22, 24, 26, 28$. Kontrol: toplamları $100$."),
            ornek(
                "Üç ardışık tek sayının toplamı $81$ olsun.",
                "En büyük sayı kaçtır?",
                "Sayıları $x-2$, $x$, $x+2$ olarak yazalım; toplam $3x=81$.",
                "$x=27$; sayılar $25, 27, 29$.",
                "En büyüğü $29$ dur."),
            hap("Ardışık sayıların ortalaması ilk ve son terimin ortalamasıdır.", "Toplam, terim sayısı ile bu ortalamanın çarpımıdır."),
        ]},
        {"baslik": "Kareler ve küpler toplamı", "icerik": [
            "Ardışık sayıların kareleri ve küpleri ardışık dizi değildir; çünkü komşu terimlerin farkı sabit kalmaz. Bu yüzden onların toplamı için ayrı formüller kullanılır:",
            tablo(["Toplam", "Sonuç"], [
                ["$1^2+2^2+\\cdots+n^2$", "$\\dfrac{n(n+1)(2n+1)}{6}$"],
                ["$1^3+2^3+\\cdots+n^3$", "$\\dfrac{n^2(n+1)^2}{4}$"],
            ]),
            "Küpler toplamının sonucu dikkat çekicidir: $\\dfrac{n^2(n+1)^2}{4}$, $1+2+\\cdots+n$ toplamının karesidir. Yani ilk $n$ sayının küplerinin toplamı, bu sayıların toplamının karesine eşittir.",
            ornek(
                "$1^2+2^2+\\cdots+10^2$ toplamı verilsin.",
                "Değerini bulalım.",
                "$n=10$ için formül: $\\dfrac{10 \\cdot 11 \\cdot 21}{6}=\\dfrac{2310}{6}$.",
                "Toplam $385$ tir."),
            ornek(
                "$1^3+2^3+3^3+4^3+5^3$ toplamı verilsin.",
                "Değerini iki yoldan bulalım.",
                "Formülle: $1+2+3+4+5=15$ ve $15^2=225$.",
                "Tek tek toplayarak: $1+8+27+64+125=225$.",
                "İki yol aynı sonucu verir: $225$."),
            ornek(
                "$6^2+7^2+8^2+9^2+10^2$ toplamı verilsin.",
                "Değerini bulalım.",
                "$1^2+\\cdots+10^2=385$ ve $1^2+\\cdots+5^2=\\dfrac{5 \\cdot 6 \\cdot 11}{6}=55$.",
                "Aranan toplam $385-55=330$.",
                "Kontrol: $36+49+64+81+100=330$."),
        ]},
        {"baslik": "Ardışık sayıların çarpımı ve bölünebilme", "icerik": [
            "Ardışık tam sayıların çarpımı bazı sayılara her zaman tam bölünür. Bunun sebebi, ardışık dizilerde belirli katların kaçınılmaz olarak yer almasıdır:",
            "<ul><li><strong>İki ardışık tam sayı:</strong> biri mutlaka çifttir, bu yüzden çarpımları çifttir.</li>"
            "<li><strong>Üç ardışık tam sayı:</strong> biri mutlaka $3$ ün katı, en az biri çifttir; çarpımları $6$ ya tam bölünür.</li>"
            "<li><strong>İki ardışık çift sayı:</strong> $2n(2n+2)=4n(n+1)$ ve $n(n+1)$ çift olduğu için çarpımları $8$ e tam bölünür.</li></ul>",
            "Genel kural şudur: $k$ ardışık tam sayının çarpımı $k!$ ile tam bölünür. Dört ardışık tam sayının çarpımı $4!=24$ e, beş ardışık tam sayının çarpımı $5!=120$ ye tam bölünür.",
            ornek(
                "$5 \\cdot 6 \\cdot 7$ ve $12 \\cdot 13 \\cdot 14 \\cdot 15$ çarpımları verilsin.",
                "Kuralı kontrol edelim.",
                "$5 \\cdot 6 \\cdot 7=210$ ve $210=6 \\cdot 35$: $6$ ya tam bölünüyor.",
                "$12 \\cdot 13 \\cdot 14 \\cdot 15=32760$ ve $32760=24 \\cdot 1365$: $24$ e tam bölünüyor."),
            ornek(
                "Dört ardışık tam sayının çarpımına $1$ eklensin.",
                "Sonucun bir tam kare olduğunu gösterelim.",
                "Örnekler: $1 \\cdot 2 \\cdot 3 \\cdot 4+1=25=5^2$ ve $2 \\cdot 3 \\cdot 4 \\cdot 5+1=121=11^2$.",
                "Genel olarak $n(n+3)=n^2+3n$ ve $(n+1)(n+2)=n^2+3n+2$ dir.",
                "$t=n^2+3n$ dersek çarpım artı bir $t(t+2)+1=t^2+2t+1=(t+1)^2$ olur; yani $(n^2+3n+1)^2$."),
        ]},
        {"baslik": "Ardışık sayı problemleri", "icerik": [
            "Ardışık sayı problemlerinde yol hep aynıdır: sayıları tek bir harfle yaz, verilen bilgiyi denkleme çevir, denklemi çöz ve sonucu kontrol et.",
            ornek(
                "Ardışık iki doğal sayının kareleri farkı $37$ olsun.",
                "Bu sayıları bulalım.",
                "Sayılar $n$ ve $n+1$ olsun: $(n+1)^2-n^2=2n+1$.",
                "$2n+1=37$ ise $n=18$.",
                "Sayılar $18$ ve $19$. Kontrol: $361-324=37$."),
            ornek(
                "Bir kitabın sayfaları $1$ den $150$ ye kadar numaralandırılsın.",
                "Numaralandırmada toplam kaç rakam kullanılır?",
                "Tek basamaklı sayfalar $1$ ile $9$ arası: $9$ sayfa, $9$ rakam.",
                "İki basamaklılar $10$ ile $99$ arası: $90$ sayfa, $90 \\cdot 2=180$ rakam.",
                "Üç basamaklılar $100$ ile $150$ arası: $51$ sayfa, $51 \\cdot 3=153$ rakam.",
                "Toplam: $9+180+153=342$ rakam."),
            ornek(
                "Açık bir kitapta karşılıklı iki sayfanın numaraları toplamı $245$ olsun.",
                "Sayfa numaralarını bulalım.",
                "Karşılıklı sayfalar ardışıktır: $n$ ve $n+1$.",
                "$2n+1=245$ ise $n=122$.",
                "Sayfalar $122$ ve $123$ tür."),
            hap("Önce sayıları harfle yaz, sonra denklemi kur; bulduğun sayıları mutlaka soruya geri koyarak kontrol et.",
                "Terim sayısı tekse ortadaki terimi $x$ almak denklemi kısaltır."),
        ]},
        {"baslik": "Sınavda ardışık sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu terim sayısı, ardışık sayıların toplamı, toplamı verilen sayıları bulma ve sayfa numarası gibi problemler biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde ardışık sayı bilgisi sayısal akıl yürütme sorularının içinde de karşına çıkabilir: ortalamadan terim bulma ya da iki toplamın farkını hesaplama gibi."),
            "Bu konuda hız, formülleri ezberlemekten çok onların nereden geldiğini bilmekten gelir. Terim sayısı formülündeki $+1$ i ve toplam formülündeki eşleştirme fikrini anladıysan, hatırlamadığın bir formülü birkaç saniyede yeniden kurabilirsin.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Terim sayısında $+1$ i unutmak", "$\\dfrac{\\text{Son}-\\text{İlk}}{\\text{Adım}}+1$"],
                ["Ardışık tekleri $x$, $x+1$ yazmak", "$x$, $x+2$"],
                ["Özel toplamda $n$ yi son terim sanmak", "$n$ terim sayısıdır"],
                ["Aradan başlayan toplamda fazla terim çıkarmak", "Bir önceki terime kadar çıkar"],
                ["Karelerin toplamını ardışık dizi sanmak", "Ayrı formül kullanılır"],
                ["\"Arasında\" ile \"dahil\" ifadesini karıştırmak", "Uç değerleri kontrol et"],
            ]),
            "Bu hataların çoğu, formülü nereden geldiğini bilmeden kullanmaktan doğar. Şüphede kaldığında küçük bir örnek üzerinde, örneğin $1$ den $5$ e kadar olan sayılarla, formülü denemek hatayı hemen ortaya çıkarır.",
        ]},
    ],
    "sss": [
        ("Ardışık sayı ne demektir?",
         "Eşit adımlarla artan sayılardır. Ardışık tam sayılarda adım 1, ardışık tek ve çift sayılarda adım 2 dir."),
        ("Terim sayısı formülünde neden 1 eklenir?",
         "Son terimden ilk terimi çıkarıp adıma bölmek aradaki adım sayısını verir. Dizinin terim sayısı adım sayısından bir fazladır; 4 adım, 5 terim demektir."),
        ("1 den 100 e kadar olan sayıların toplamı kaçtır?",
         "5050 dir. İlk ve son terimler eşleştirilince 50 çift oluşur ve her çiftin toplamı 101 dir."),
        ("Ardışık tek sayıların toplamı nasıl bulunur?",
         "1 den başlayan ilk n tek sayının toplamı n nin karesidir. Örneğin 1 den 49 a kadar olan 25 tek sayının toplamı 625 tir."),
        ("Toplamı verilen ardışık sayılar nasıl bulunur?",
         "Toplam terim sayısına bölünerek ortalama bulunur. Terim sayısı tekse bu ortalama ortadaki sayıdır, sonra komşu terimler yazılır."),
        ("Üç ardışık tam sayının çarpımı neden 6 ya bölünür?",
         "Üç ardışık tam sayıdan biri mutlaka 3 ün katıdır ve en az biri çifttir. Bu yüzden çarpım hem 2 ye hem 3 e, yani 6 ya tam bölünür."),
    ],
    "kontrol": [
        "Ardışık tam, tek ve çift sayıları harfle yazabiliyorum.",
        "Terim sayısı tek olduğunda ortadaki terimi $x$ alarak denklemi kısaltabiliyorum.",
        "İlk terim, son terim ve adımla terim sayısını bulabiliyorum.",
        "\"Arasında\" ile \"dahil\" farkını terim sayısına yansıtabiliyorum.",
        "Ardışık bir dizinin toplamını ilk ve son terimle hesaplayabiliyorum.",
        "Tek ve çift sayıların özel toplam formüllerinde $n$ yi doğru belirleyebiliyorum.",
        "Aradan başlayan bir toplamı iki yoldan bulabiliyorum.",
        "Toplamı verilen ardışık sayıları ortalama yardımıyla bulabiliyorum.",
        "Kareler ve küpler toplamını formülle hesaplayabiliyorum.",
        "Ardışık sayıların çarpımının hangi sayılara bölündüğünü açıklayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["tek-ve-cift-sayilar", "temel-kavramlar-konu-anlatimi-pdf", "sayi-dogrusu-ve-sayilari-siralama"],
}
