# scripts/yazilar/66_ebob_ekok.py — EBOB ve EKOK (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "ebob-ve-ekok-konu-anlatimi-pdf",
    "baslik": "EBOB ve EKOK Konu Anlatımı PDF",
    "aciklama": "EBOB ve EKOK nedir? Asal çarpanlarla ve bölme yöntemiyle bulma, EBOB ile EKOK çarpımı, parçalama, buluşma ve kalan problemleri; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "ebob-ve-ekok-konu-anlatimi-pdf",
    "kapak_alt": "EBOB ve EKOK: renkli boncukları düzenli aralıklarla çubuklara dizerek ortak katları gösteren iki öğrenci",
    "ozet": "EBOB ve EKOK, iki ya da daha fazla sayının ortak yanlarını ölçer: EBOB hepsini tam bölen en büyük sayıyı, EKOK hepsinin tam böldüğü en küçük pozitif sayıyı verir. Bir alanı eş karelere bölmek, farklı aralıklarla gelen otobüslerin ne zaman birlikte kalkacağını bulmak ya da kesirleri ortak paydaya getirmek bu iki kavramla çözülür. Bu yazıda EBOB ve EKOK'u tanımlıyor, üç farklı yolla hesaplıyor, aralarındaki ilişkiyi gösteriyor ve problem türlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Ortak bölen ve ortak kat", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için bölünebilme kurallarını ve asal çarpanlara ayırmayı biliyor olman yeterli.",
                "Asal çarpanlara ayırma için <a href=\"/blog/asal-sayilar-ve-asal-carpanlara-ayirma/\">Asal Sayılar ve Asal Çarpanlara Ayırma</a> yazısına göz at."),
            "Bir sayıyı tam bölen pozitif sayılara o sayının <strong>bölenleri</strong>, sayının pozitif tam sayılarla çarpımlarına da <strong>katları</strong> denir. $12$ nin bölenleri $1, 2, 3, 4, 6, 12$ dir; katları ise $12, 24, 36, 48, \\ldots$ diye sonsuza kadar gider.",
            "İki sayının ikisini birden bölen sayılara <strong>ortak bölen</strong>, ikisinin de katı olan sayılara <strong>ortak kat</strong> denir. Ortak bölenlerin en büyüğüne <strong>EBOB</strong> (en büyük ortak bölen), pozitif ortak katların en küçüğüne <strong>EKOK</strong> (en küçük ortak kat) denir.",
            ornek(
                "$12$ ve $18$ sayıları verilsin.",
                "EBOB ve EKOK değerlerini listeleyerek bulalım.",
                "$12$ nin bölenleri: $1, 2, 3, 4, 6, 12$. $18$ in bölenleri: $1, 2, 3, 6, 9, 18$.",
                "Ortak bölenler: $1, 2, 3, 6$. En büyüğü: $\\text{EBOB}(12, 18)=6$.",
                "$12$ nin katları: $12, 24, 36, 48, \\ldots$ $18$ in katları: $18, 36, 54, \\ldots$",
                "İlk ortak kat: $\\text{EKOK}(12, 18)=36$."),
            hap("EBOB, sayıların hepsini tam bölen en büyük sayıdır; EKOK, sayıların hepsinin tam böldüğü en küçük pozitif sayıdır.",
                "EBOB sayılardan büyük olamaz, EKOK sayılardan küçük olamaz."),
        ]},
        {"baslik": "Asal çarpanlarla EBOB ve EKOK", "icerik": [
            "Listeleme yöntemi küçük sayılarda işe yarar ama büyük sayılarda uzun sürer. Asıl yöntem, sayıları asal çarpanlarına ayırmaktır. Her sayı asallarının kuvvetleri olarak yazıldıktan sonra:",
            "<ul><li><strong>EBOB:</strong> yalnızca <strong>ortak</strong> asallar alınır, her birinin <strong>en küçük</strong> üssüyle.</li>"
            "<li><strong>EKOK:</strong> <strong>bütün</strong> asallar alınır, her birinin <strong>en büyük</strong> üssüyle.</li></ul>",
            "Nedeni şudur: EBOB iki sayıyı da bölmek zorunda olduğu için bir asaldan en fazla küçük üs kadar içerebilir. EKOK ise iki sayının katı olmak zorunda olduğu için her asaldan en az büyük üs kadar içermelidir.",
            ornek(
                "$72$ ve $120$ sayıları verilsin.",
                "Asal çarpanlarla EBOB ve EKOK bulalım.",
                "$72=2^3 \\cdot 3^2$ ve $120=2^3 \\cdot 3 \\cdot 5$.",
                "EBOB: ortak asallar $2$ ve $3$; en küçük üslerle $2^3 \\cdot 3=24$.",
                "EKOK: bütün asallar $2$, $3$, $5$; en büyük üslerle $2^3 \\cdot 3^2 \\cdot 5=360$."),
            ornek(
                "$2^4 \\cdot 3^2 \\cdot 7$ ve $2^2 \\cdot 3^5 \\cdot 5$ sayıları verilsin.",
                "EBOB ve EKOK değerlerini üslü biçimde yazalım.",
                "EBOB: ortak asallar $2$ ve $3$: $2^2 \\cdot 3^2$.",
                "EKOK: bütün asallar: $2^4 \\cdot 3^5 \\cdot 5 \\cdot 7$."),
            dikkat(
                "EBOB'a yalnızca bir sayıda bulunan asal girmez.",
                "Yukarıdaki örnekte $5$ yalnızca ikinci sayıda, $7$ yalnızca birinci sayıda var. İkisi de EBOB'a girmez ama ikisi de EKOK'a girer."),
            hap("EBOB için yalnız ortak asallar küçük üsleriyle alınır.", "EKOK için bütün asallar büyük üsleriyle alınır."),
        ]},
        {"baslik": "Bölme yöntemi: ortak bölme tablosu", "icerik": [
            "Sayılar yan yana yazılır ve en küçük asaldan başlayarak bölünür. Bir asal, sayılardan en az birini bölüyorsa kullanılır; bölünemeyen sayı aynen aşağı indirilir. Bütün sayılar $1$ olunca durulur.",
            "<ul><li><strong>EKOK:</strong> kullanılan bütün bölenlerin çarpımıdır.</li>"
            "<li><strong>EBOB:</strong> yalnızca sayıların <strong>hepsini aynı anda</strong> bölen bölenlerin çarpımıdır.</li></ul>",
            ornek(
                "$24$, $36$ ve $60$ sayıları verilsin.",
                "Bölme yöntemiyle EBOB ve EKOK bulalım.",
                "$2$ ile bölelim: $12, 18, 30$. Üç sayı da bölündü.",
                "Yine $2$ ile: $6, 9, 15$. Üç sayı da bölündü.",
                "Yine $2$ ile: $3, 9, 15$. Yalnızca $6$ bölündü, diğerleri aynen indi.",
                "$3$ ile: $1, 3, 5$. Üç sayı da bölündü. Yine $3$ ile: $1, 1, 5$. Son olarak $5$ ile: $1, 1, 1$.",
                "EKOK, bütün bölenlerin çarpımıdır: $2 \\cdot 2 \\cdot 2 \\cdot 3 \\cdot 3 \\cdot 5=360$.",
                "EBOB, üç sayının birlikte bölündüğü adımların çarpımıdır: $2 \\cdot 2 \\cdot 3=12$."),
            "Bu yöntemde en kolay hata, hepsini aynı anda bölen adımları doğru işaretlememektir. Bu yüzden üç sayılı durumlarda asal çarpan yöntemi daha güvenlidir. Aynı sayıları asal çarpanlarıyla çözelim:",
            ornek(
                "$24=2^3 \\cdot 3$, $36=2^2 \\cdot 3^2$ ve $60=2^2 \\cdot 3 \\cdot 5$ verilsin.",
                "EBOB ve EKOK bulalım.",
                "EBOB: ortak asallar $2$ ve $3$; en küçük üsler: $2^2 \\cdot 3=12$.",
                "EKOK: $2^3 \\cdot 3^2 \\cdot 5=360$.",
                "Kontrol: $12$, üç sayıyı da böler; $360$ ise üçünün de katıdır: $360=24 \\cdot 15=36 \\cdot 10=60 \\cdot 6$."),
            dikkat(
                "Bölme tablosunda EBOB için yalnızca bütün sayıların birlikte bölündüğü satırlar sayılır.",
                "$24$, $36$ ve $60$ için ilk iki bölme adımında ($2$ ve $2$) üç sayı da çift olduğu için ikisi de EBOB'a girer; sonra $3$ ile üçü birden bölünür. Böylece $2 \\cdot 2 \\cdot 3=12$ bulunur."),
        ]},
        {"baslik": "EBOB ile EKOK arasındaki ilişki", "icerik": [
            "İki pozitif tam sayı için çok kullanışlı bir eşitlik vardır:",
            "$$\\text{EBOB}(a, b) \\cdot \\text{EKOK}(a, b)=a \\cdot b$$",
            "Nedeni asal çarpanlardadır: her asal için EBOB küçük üssü, EKOK büyük üssü alır. İki üssün toplamı, o asalın $a$ ve $b$ deki üslerinin toplamına eşittir. Bu yüzden EBOB ile EKOK'un çarpımı, $a$ ile $b$ nin çarpımıyla aynı asal çarpanlara sahiptir.",
            ornek(
                "$12$ ve $18$ verilsin.",
                "Eşitliği kontrol edelim.",
                "$\\text{EBOB} \\cdot \\text{EKOK}=6 \\cdot 36=216$.",
                "$12 \\cdot 18=216$. Eşitlik sağlanır."),
            ornek(
                "İki sayının EBOB'u $6$, EKOK'u $90$ ve sayılardan biri $18$ olsun.",
                "Diğer sayıyı bulalım.",
                "Eşitliği kullanalım: $6 \\cdot 90=18 \\cdot b$.",
                "$b=\\dfrac{540}{18}=30$.",
                "Kontrol: $\\text{EBOB}(18, 30)=6$ ve $\\text{EKOK}(18, 30)=90$."),
            dikkat(
                "Bu eşitlik yalnızca iki sayı için geçerlidir.",
                "$2$, $4$ ve $8$ için EBOB $2$, EKOK $8$ dir; çarpımları $16$ olur. Ama $2 \\cdot 4 \\cdot 8=64$ tür. Üç ya da daha fazla sayıda eşitlik kullanılmaz."),
            "<h3>Başka ilişkiler</h3>",
            "<ul><li>EBOB, EKOK'u her zaman tam böler.</li>"
            "<li>$a$, $b$ yi tam bölüyorsa EBOB $a$, EKOK $b$ dir. Örneğin $\\text{EBOB}(6, 24)=6$ ve $\\text{EKOK}(6, 24)=24$.</li>"
            "<li>EBOB'u $1$ olan sayılara <strong>aralarında asal</strong> denir; bu durumda EKOK sayıların çarpımıdır: $\\text{EKOK}(8, 15)=120$.</li></ul>",
            hap("İki pozitif sayı için $\\text{EBOB}(a, b) \\cdot \\text{EKOK}(a, b)=a \\cdot b$ olur.", "Bu eşitlik yalnız iki sayı için geçerlidir."),
        ]},
        {"baslik": "EBOB'u verilen sayılar", "icerik": [
            "EBOB'u $d$ olan iki sayı $d \\cdot x$ ve $d \\cdot y$ biçiminde yazılır ve $x$ ile $y$ aralarında asal olmak zorundadır. Ortak bir çarpanları olsaydı EBOB $d$ den büyük çıkardı.",
            ornek(
                "EBOB'u $8$, toplamı $56$ olan iki pozitif tam sayı aransın.",
                "Bu sayı çiftlerini bulalım.",
                "Sayılar $8x$ ve $8y$ olsun; $8x+8y=56$ ise $x+y=7$.",
                "$x$ ile $y$ aralarında asal olmalı: $(1, 6)$, $(2, 5)$, $(3, 4)$ çiftlerinin hepsi uygun.",
                "Sayı çiftleri: $8$ ile $48$, $16$ ile $40$, $24$ ile $32$."),
            dikkat(
                "$x$ ile $y$ nin aralarında asal olma koşulunu atlama.",
                "EBOB'u $6$, toplamı $48$ olan sayılarda $x+y=8$ olur. $(2, 6)$ çifti bu toplamı sağlar ama $\\text{EBOB}(12, 36)=12$ dir, $6$ değil. Bu yüzden $(2, 6)$ elenir; uygun çiftler $(1, 7)$ ve $(3, 5)$ tir."),
        ]},
        {"baslik": "EBOB problemleri: parçalama", "icerik": [
            "Bir bütünü <strong>en büyük</strong> eş parçalara ayırma, farklı miktarları <strong>en büyük</strong> eşit gruplara bölme ya da <strong>en az</strong> sayıda parça elde etme soruları EBOB ile çözülür. Parça büyüdükçe parça sayısı azalır; en büyük ortak parça, en az parça sayısını verir.",
            ornek(
                "Boyutları $84$ santimetre ve $120$ santimetre olan dikdörtgen bir karton, hiç artmayacak biçimde eş karelere bölünecek.",
                "Kareler olabildiğince büyük olursa bir karenin kenarı ve kare sayısı ne olur?",
                "Kare kenarı iki kenarı da tam bölmeli ve en büyük olmalı: $\\text{EBOB}(84, 120)=12$ santimetre.",
                "Bir kenara $84:12=7$, diğerine $120:12=10$ kare sığar.",
                "Kare sayısı: $7 \\cdot 10=70$."),
            ornek(
                "Uzunlukları $48$, $72$ ve $120$ metre olan üç halat, hiç artmayacak biçimde eşit uzunlukta parçalara kesilecek.",
                "Parçalar en uzun olursa kaç parça elde edilir?",
                "Parça uzunluğu: $\\text{EBOB}(48, 72, 120)=24$ metre.",
                "Parça sayıları: $48:24=2$, $72:24=3$, $120:24=5$.",
                "Toplam $2+3+5=10$ parça elde edilir."),
            ornek(
                "Kenarları $60$ metre ve $84$ metre olan dikdörtgen bir bahçenin çevresine, köşelere de gelecek biçimde, eşit aralıklarla ağaç dikilecek.",
                "En az kaç ağaç gerekir?",
                "Aralık iki kenarı da tam bölmeli ve en az ağaç için en büyük olmalı: $\\text{EBOB}(60, 84)=12$ metre.",
                "Çevre: $2 \\cdot (60+84)=288$ metre.",
                "Kapalı bir çevrede ağaç sayısı aralık sayısına eşittir: $288:12=24$ ağaç."),
            dikkat(
                "Açık ve kapalı yolda ağaç sayısı farklıdır.",
                "Kapalı bir çevrede ağaç sayısı aralık sayısına eşittir. Düz ve açık bir yolun iki ucuna da ağaç dikilirse ağaç sayısı aralık sayısından $1$ fazladır."),
            hap("Bayramda $48$ çikolata ve $36$ lokum hiç artmadan en çok $12$ çocuğa eşit paylaştırılır, çünkü $\\text{EBOB}(48, 36)=12$ olur.", "Her çocuk $4$ çikolata ve $3$ lokum alır.", gunluk=True),
        ]},
        {"baslik": "EKOK problemleri: buluşma ve birleştirme", "icerik": [
            "Farklı aralıklarla tekrar eden olayların <strong>ilk kez birlikte</strong> gerçekleşmesi, küçük parçalardan <strong>en küçük</strong> bütünü oluşturma ve verilen sayıların hepsine bölünen <strong>en küçük</strong> sayıyı bulma soruları EKOK ile çözülür.",
            ornek(
                "Bir duraktan iki otobüs saat 09.00'da birlikte kalkıyor. Biri $12$ dakikada bir, diğeri $18$ dakikada bir kalkıyor.",
                "İki otobüs bir sonraki sefer ne zaman birlikte kalkar?",
                "Birlikte kalkış için geçen süre iki aralığın da katı olmalı ve en küçük olmalı: $\\text{EKOK}(12, 18)=36$ dakika.",
                "Bir sonraki birlikte kalkış saat 09.36'dadır."),
            ornek(
                "Boyutları $6$ santimetre ve $8$ santimetre olan dikdörtgen fayanslar aynı yönde yan yana ve alt alta dizilerek bir kare oluşturulacak.",
                "Oluşturulabilecek en küçük karenin kenarı ve gereken fayans sayısı nedir?",
                "Karenin kenarı hem $6$ nın hem $8$ in katı olmalı: $\\text{EKOK}(6, 8)=24$ santimetre.",
                "Bir kenara $24:6=4$, diğerine $24:8=3$ fayans gelir.",
                "Fayans sayısı: $4 \\cdot 3=12$."),
            hap("\"En büyük parça\", \"en az parça\" ifadeleri EBOB'u; \"ilk kez birlikte\", \"en küçük bütün\" ifadeleri EKOK'u gösterir.",
                "Parçalama EBOB, birleştirme EKOK sorusudur."),
        ]},
        {"baslik": "EKOK ile kalan problemleri", "icerik": [
            "Bir sayının birkaç sayıya bölümünden kalanlar verilip sayı sorulduğunda iki durum ayrılır.",
            "<h3>Kalanlar eşitse</h3>",
            "Sayı, bölenlerin hepsine bölündüğünde aynı $r$ kalanını veriyorsa sayıdan $r$ çıkarılınca bölenlerin hepsine tam bölünür. Yani sayı, EKOK'un bir katının $r$ fazlasıdır.",
            ornek(
                "$4$, $6$ ve $9$ a bölündüğünde her seferinde $3$ kalanını veren doğal sayılar aransın.",
                "Bu sayılardan $3$ ten büyük olan en küçüğünü bulalım.",
                "Sayı $\\text{EKOK}(4, 6, 9) \\cdot k+3$ biçimindedir; $\\text{EKOK}(4, 6, 9)=36$.",
                "$k=1$ için $36+3=39$.",
                "Kontrol: $39=4 \\cdot 9+3=6 \\cdot 6+3=9 \\cdot 4+3$."),
            "<h3>Kalanlar bölenden hep aynı kadar eksikse</h3>",
            "Kalanlar farklıysa bölen ile kalan arasındaki farklara bakılır. Farklar eşitse sayıya bu fark eklenince bölenlerin hepsine tam bölünür.",
            ornek(
                "Bir doğal sayının $5$ e bölümünden kalan $3$, $6$ ya bölümünden kalan $4$, $8$ e bölümünden kalan $6$ olsun.",
                "Bu koşulları sağlayan en küçük doğal sayıyı bulalım.",
                "Her durumda kalan, bölenden $2$ eksik: $5-3=6-4=8-6=2$.",
                "Sayıya $2$ eklenirse üç bölene de tam bölünür: sayı $\\text{EKOK}(5, 6, 8) \\cdot k-2$ biçimindedir.",
                "$\\text{EKOK}(5, 6, 8)=120$; en küçük sayı $120-2=118$.",
                "Kontrol: $118$ in $5$ e bölümünden kalan $3$, $6$ ya bölümünden kalan $4$, $8$ e bölümünden kalan $6$."),
        ]},
        {"baslik": "Kesirlerde EBOB ve EKOK", "icerik": [
            "EBOB ve EKOK'un günlük bir kullanımı kesirlerdedir. Bir kesri en sade hâline getirmek için pay ve payda EBOB'larına bölünür. Farklı paydalı kesirleri toplarken ya da karşılaştırırken ortak payda olarak paydaların EKOK'u kullanılır; bu, sayıları olabildiğince küçük tutar.",
            ornek(
                "$\\dfrac{84}{120}$ kesri ile $\\dfrac{5}{12}+\\dfrac{7}{18}$ toplamı verilsin.",
                "Kesri sadeleştirelim ve toplamı ortak paydayla bulalım.",
                "$\\text{EBOB}(84, 120)=12$: $\\dfrac{84}{120}=\\dfrac{7}{10}$.",
                "$\\text{EKOK}(12, 18)=36$: $\\dfrac{15}{36}+\\dfrac{14}{36}=\\dfrac{29}{36}$."),
            "Kesirlerle işlemlerin ayrıntısı için <a href=\"/blog/kesirlerde-toplama-ve-cikarma/\">Kesirlerde Toplama ve Çıkarma</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sınavda EBOB ve EKOK", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu parçalama, buluşma, ağaç dikme, fayans döşeme ve kalan problemleri biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde EBOB ve EKOK bilgisi sayısal akıl yürütme sorularında, özellikle tekrar eden olayların zamanlamasında da gerekebilir."),
            "Problemde ilk yapılacak iş, sorunun EBOB mu EKOK mu istediğine karar vermektir. Cevabın verilen sayılardan küçük mü büyük mü olması gerektiğini düşünmek yardımcı olur: parça, bütünden küçüktür; ortak buluşma zamanı ise aralıklardan büyüktür. Bu kısa kontrol, yanlış kavramı seçmeyi büyük ölçüde önler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["EBOB'a ortak olmayan asalı almak", "Yalnız ortak asallar"],
                ["EBOB'da büyük üssü almak", "Küçük üs"],
                ["EKOK'ta küçük üssü almak", "Büyük üs"],
                ["Üç sayıda $a \\cdot b=\\text{EBOB} \\cdot \\text{EKOK}$ kullanmak", "Yalnız iki sayıda"],
                ["Kapalı çevrede ağaç sayısına $1$ eklemek", "Aralık sayısı kadar"],
                ["Parçalama sorusunda EKOK almak", "Parçalama EBOB"],
            ]),
            "Bu hataların ortak noktası, iki kavramın tanımını karıştırmaktır. EBOB bölen olduğu için sayılardan büyük çıkamaz; EKOK kat olduğu için sayılardan küçük çıkamaz. Bulduğun sonucu bu iki cümleyle kontrol etmek hatayı hemen gösterir.",
        ]},
    ],
    "sss": [
        ("EBOB ne demektir?",
         "En büyük ortak bölen demektir. Verilen sayıların hepsini tam bölen pozitif sayıların en büyüğüdür."),
        ("EKOK ne demektir?",
         "En küçük ortak kat demektir. Verilen sayıların hepsinin tam böldüğü pozitif sayıların en küçüğüdür."),
        ("EBOB ve EKOK asal çarpanlarla nasıl bulunur?",
         "EBOB için yalnızca ortak asallar en küçük üsleriyle, EKOK için bütün asallar en büyük üsleriyle çarpılır."),
        ("EBOB çarpı EKOK neye eşittir?",
         "İki pozitif tam sayı için sayıların çarpımına eşittir. Üç ya da daha fazla sayı için bu eşitlik geçerli değildir."),
        ("Bir problemin EBOB mu EKOK mu olduğu nasıl anlaşılır?",
         "Bir bütünü en büyük eş parçalara ayırma soruları EBOB, farklı aralıklarla tekrar eden olayların birlikte gerçekleşmesi ya da en küçük bütünü oluşturma soruları EKOK ile çözülür."),
        ("Aralarında asal sayıların EKOK'u nedir?",
         "EBOB'ları 1 olduğu için EKOK'ları sayıların çarpımıdır. Örneğin 8 ile 15 in EKOK'u 120 dir."),
    ],
    "kontrol": [
        "Bölen, kat, ortak bölen ve ortak kat kavramlarını ayırt edebiliyorum.",
        "Küçük sayılarda EBOB ve EKOK'u listeleyerek bulabiliyorum.",
        "Asal çarpanlarla EBOB için küçük, EKOK için büyük üsleri seçebiliyorum.",
        "Bölme tablosunda EBOB'a hangi bölenlerin girdiğini doğru işaretleyebiliyorum.",
        "İki sayı için EBOB çarpı EKOK eşitliğini kullanabiliyorum.",
        "EBOB'u verilen sayıları $d \\cdot x$ ve $d \\cdot y$ biçiminde yazabiliyorum.",
        "Parçalama ve ağaç dikme sorularını EBOB ile çözebiliyorum.",
        "Buluşma ve fayans sorularını EKOK ile çözebiliyorum.",
        "Kalanı verilen sayıları EKOK yardımıyla bulabiliyorum.",
        "Kesirleri EBOB ile sadeleştirip EKOK ile ortak paydaya getirebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["asal-sayilar-ve-asal-carpanlara-ayirma", "bolunebilme-kurallari-konu-anlatimi-pdf", "kesirlerde-toplama-ve-cikarma"],
}
