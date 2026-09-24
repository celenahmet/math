# scripts/yazilar/78_esitsizlikler.py — Esitsizlikler (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "esitsizlikler-konu-anlatimi-pdf",
    "baslik": "Eşitsizlikler Konu Anlatımı PDF",
    "aciklama": "Eşitsizlik nedir, nasıl çözülür? İşaretler, negatif sayıyla çarpma, aralık gösterimi, sıralı ve mutlak değerli eşitsizlikler, değer aralığı; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "cebir",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "esitsizlikler-konu-anlatimi-pdf",
    "kapak_alt": "Eşitsizlikler: bir yana eğilmiş teraziyle ve boncuklu sayı çubuğuyla büyüklük ilişkilerini inceleyen iki öğrenci",
    "ozet": "Eşitsizlik, iki ifadeden birinin diğerinden büyük ya da küçük olduğunu söyler. Denklemin genellikle tek bir çözümü varken eşitsizliğin çözümü çoğu zaman bir aralıktır: bir sayıdan küçük bütün sayılar gibi. Bütçe sınırı, geçme notu, hız sınırı ve kapasite gibi günlük kısıtların hepsi eşitsizlikle anlatılır. Bu yazıda eşitsizlik işaretlerini, eşitsizliğin özelliklerini, negatif sayıyla çarpınca yönün neden değiştiğini, aralık gösterimini, sıralı ve mutlak değerli eşitsizlikleri ve değer aralığı sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Eşitsizlik nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birinci dereceden denklem çözmeyi ve sayı doğrusunu biliyor olman yeterli.",
                "Denklemler için <a href=\"/blog/birinci-dereceden-denklemler-konu-anlatimi-pdf/\">Birinci Dereceden Denklemler Konu Anlatımı PDF</a>, sıralama için <a href=\"/blog/sayi-dogrusu-ve-sayilari-siralama/\">Sayı Doğrusu ve Sayıları Sıralama</a> yazısına göz at."),
            "İki ifadenin büyüklük ilişkisini gösteren bağıntılara <strong>eşitsizlik</strong> denir. Dört eşitsizlik işareti vardır:",
            tablo(["İşaret", "Okunuşu", "Örnek"], [
                ["$<$", "küçüktür", "$3<7$"],
                ["$>$", "büyüktür", "$-1>-4$"],
                ["$\\leq$", "küçük ya da eşittir", "$x \\leq 5$"],
                ["$\\geq$", "büyük ya da eşittir", "$x \\geq -2$"],
            ]),
            "İşaretin açık tarafı her zaman büyük olana bakar. $x<5$ eşitsizliği \"$x$, $5$ ten küçüktür\" diye okunur ve $5$ ten küçük bütün sayılar bu eşitsizliği sağlar: $4$, $0$, $-3$, $4.99$ gibi. Denklemin çözümü çoğunlukla tek bir sayıyken eşitsizliğin çözümü genellikle sonsuz sayıda sayıdan oluşan bir <strong>aralıktır</strong>.",
            hap("Eşitsizlik iki ifadenin büyüklük ilişkisini gösterir: $<$, $>$, $\\leq$, $\\geq$.",
                "Eşitsizliğin çözümü genellikle bir aralıktır."),
        ]},
        {"baslik": "Eşitsizliğin özellikleri", "icerik": [
            "Eşitsizlikler de denklemler gibi iki tarafa aynı işlem uygulanarak çözülür. Ama bir farkla: bazı işlemler eşitsizliğin yönünü değiştirir.",
            tablo(["İşlem", "Yön", "Örnek"], [
                ["İki tarafa aynı sayıyı eklemek ya da çıkarmak", "Değişmez", "$2<5$ ise $2+3<5+3$"],
                ["İki tarafı pozitif bir sayıyla çarpmak ya da bölmek", "Değişmez", "$2<5$ ise $2 \\cdot 4<5 \\cdot 4$"],
                ["İki tarafı negatif bir sayıyla çarpmak ya da bölmek", "Değişir", "$2<5$ ise $-2>-5$"],
            ]),
            "<h3>Negatif sayıyla çarpınca yön neden değişir?</h3>",
            "Sayı doğrusunda $2$, $5$ in solundadır. İki sayıyı $-1$ ile çarpmak, onları sıfıra göre aynalamak demektir: $-2$ sıfırın hemen solunda, $-5$ ise daha solda kalır. Aynalama sıralamayı tersine çevirdiği için $2<5$ iken $-2>-5$ olur. Bu yüzden eşitsizliğin iki tarafı negatif bir sayıyla çarpılır ya da bölünürse işaret ters çevrilir.",
            hap("Negatif bir sayıyla çarpma ya da bölme eşitsizliğin yönünü ters çevirir.",
                "Toplama, çıkarma ve pozitif sayıyla çarpma yönü değiştirmez."),
            dikkat(
                "Bilinmeyenin işaretini bilmeden onunla çarpmak.",
                "$x$ in pozitif mi negatif mi olduğu bilinmiyorsa eşitsizliğin iki tarafı $x$ ile çarpılamaz ya da $x$ e bölünemez; yön değişip değişmeyeceği belli değildir."),
        ]},
        {"baslik": "Birinci dereceden eşitsizlikleri çözmek", "icerik": [
            "Birinci dereceden bir eşitsizlik, denklem gibi adım adım çözülür: bilinmeyenler bir tarafa, sabitler diğer tarafa toplanır ve iki taraf bilinmeyenin katsayısına bölünür. Katsayı negatifse son adımda yön değişir.",
            ornek(
                "$3x-5<7$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "İki tarafa $5$ ekleyelim: $3x<12$.",
                "İki tarafı pozitif $3$ e bölelim; yön değişmez: $x<4$.",
                "Kontrol için aralıktan bir değer seçelim: $x=0$ için $-5<7$ doğrudur."),
            ornek(
                "$-2x+3 \\geq 11$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "İki taraftan $3$ çıkaralım: $-2x \\geq 8$.",
                "İki tarafı negatif $-2$ ye bölelim; yön değişir: $x \\leq -4$.",
                "Kontrol: $x=-5$ için $10+3=13 \\geq 11$ doğrudur; $x=0$ için $3 \\geq 11$ yanlıştır."),
            "İkinci örnekte bilinmeyenleri sağ tarafta toplamak da mümkündü: $3-11 \\geq 2x$, yani $-8 \\geq 2x$ ve $-4 \\geq x$. Bu yol negatif sayıya bölmeyi hiç gerektirmez ve aynı sonucu verir.",
        ]},
        {"baslik": "Denklem ile eşitsizlik arasındaki farklar", "icerik": [
            "Eşitsizlik çözerken denklemdeki adımların neredeyse hepsi aynen kullanılır. Farklar az ama önemlidir:",
            tablo(["", "Denklem", "Eşitsizlik"], [
                ["Çözüm", "Genellikle tek sayı", "Genellikle bir aralık"],
                ["Negatif sayıyla çarpma", "Eşitlik bozulmaz", "Yön ters döner"],
                ["İki tarafı taraf tarafa çıkarma", "Yapılabilir", "Yapılamaz"],
                ["Kontrol", "Kökü yerine koy", "Aralığın içinden ve dışından birer değer dene"],
            ]),
            "Son satır özellikle önemlidir. Bir denklemin kökünü kontrol etmek için tek bir değer yeter; eşitsizlikte ise hem aralığın içinden bir değerin eşitsizliği sağladığını hem de dışından bir değerin sağlamadığını görmek, yönün doğru olduğunu gösterir.",
        ]},
        {"baslik": "Aralık gösterimi ve sayı doğrusu", "icerik": [
            "Eşitsizliğin çözüm kümesi, sayı doğrusunda bir parça olarak gösterilir ve <strong>aralık gösterimiyle</strong> yazılır. Uç nokta çözüme dahilse <strong>köşeli parantez</strong> ve sayı doğrusunda içi dolu nokta, dahil değilse <strong>normal parantez</strong> ve içi boş nokta kullanılır. Sonsuzluk bir sayı olmadığı için $\\infty$ yanına her zaman normal parantez gelir.",
            tablo(["Eşitsizlik", "Aralık", "Uç noktalar"], [
                ["$x<4$", "$(-\\infty, 4)$", "$4$ dahil değil"],
                ["$x \\leq -4$", "$(-\\infty, -4]$", "$-4$ dahil"],
                ["$x \\geq 1$", "$[1, \\infty)$", "$1$ dahil"],
                ["$2<x \\leq 7$", "$(2, 7]$", "$2$ dahil değil, $7$ dahil"],
            ]),
            ornek(
                "$2<x \\leq 7$ eşitsizliği verilsin.",
                "Bu eşitsizliği sağlayan tam sayıları bulalım.",
                "$2$ dahil değil, $7$ dahil.",
                "Tam sayılar: $3$, $4$, $5$, $6$ ve $7$; toplam $5$ tane."),
            dikkat(
                "Uç noktanın dahil olup olmadığını gözden kaçırmak.",
                "Tam sayı sayma sorularında sonuç çoğu zaman uç noktaya bağlıdır. $2<x<7$ olsaydı $7$ dahil olmaz ve $4$ tam sayı kalırdı."),
        ]},
        {"baslik": "Parantezli ve kesirli eşitsizlikler", "icerik": [
            "Parantezli ve kesirli eşitsizlikler de denklemlerdeki gibi sadeleştirilir. Kesirleri yok etmek için iki taraf paydaların EKOK'u ile çarpılır; EKOK pozitif olduğu için yön değişmez.",
            ornek(
                "$2(x-3) \\leq 5x+6$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "Parantezi açalım: $2x-6 \\leq 5x+6$.",
                "Bilinmeyenleri sağa toplayalım: $-6-6 \\leq 5x-2x$, yani $-12 \\leq 3x$.",
                "$-4 \\leq x$, yani $x \\geq -4$."),
            ornek(
                "$\\dfrac{x}{2}-1>\\dfrac{x}{3}$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "Paydaların EKOK'u $6$. İki tarafı $6$ ile çarpalım: $3x-6>2x$.",
                "$x>6$.",
                "Kontrol: $x=12$ için sol taraf $6-1=5$, sağ taraf $4$; $5>4$ doğrudur."),
        ]},
        {"baslik": "Sıralı eşitsizlikler", "icerik": [
            "$-3<2x+1 \\leq 9$ gibi iki işaret içeren eşitsizliklere <strong>sıralı</strong> ya da <strong>çift taraflı</strong> eşitsizlik denir. Bu eşitsizliklerde işlem, üç tarafa birden uygulanır.",
            ornek(
                "$-3<2x+1 \\leq 9$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim ve tam sayı çözümleri sayalım.",
                "Üç taraftan $1$ çıkaralım: $-4<2x \\leq 8$.",
                "Üç tarafı $2$ ye bölelim: $-2<x \\leq 4$.",
                "Tam sayılar: $-1$, $0$, $1$, $2$, $3$ ve $4$; toplam $6$ tane."),
            ornek(
                "$1 \\leq 5-2x<7$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "Üç taraftan $5$ çıkaralım: $-4 \\leq -2x<2$.",
                "Üç tarafı $-2$ ye bölelim; iki işaret de döner: $2 \\geq x>-1$.",
                "Küçükten büyüğe yazalım: $-1<x \\leq 2$."),
            dikkat(
                "Negatif sayıya bölerken yalnız bir işareti çevirmek.",
                "Sıralı eşitsizlikte negatif bir sayıya bölünürse <strong>iki işaret de</strong> ters döner. Sonucu küçükten büyüğe yeniden yazmak okumayı kolaylaştırır."),
        ]},
        {"baslik": "İki koşul birlikte: kesişim ve birleşim", "icerik": [
            "Bazı sorularda bilinmeyen iki koşulu birden sağlamalıdır. \"ve\" bağlacıyla verilen koşulların çözümü, iki aralığın <strong>kesişimidir</strong>; \"ya da\" ile verilenlerin çözümü ise <strong>birleşimidir</strong>.",
            ornek(
                "$2x-1>3$ ve $x+4 \\leq 10$ koşulları verilsin.",
                "İki koşulu birlikte sağlayan tam sayıları bulalım.",
                "Birinci koşul: $2x>4$, yani $x>2$.",
                "İkinci koşul: $x \\leq 6$.",
                "Kesişim: $2<x \\leq 6$, yani $(2, 6]$. Tam sayılar $3$, $4$, $5$ ve $6$; toplam $4$ tane."),
            "İki aralığı sayı doğrusunda üst üste çizmek, kesişimi ve birleşimi görmenin en güvenli yoludur. Kesişim iki çizginin üst üste geldiği kısım, birleşim ise çizgilerden en az birinin bulunduğu kısımdır. Kesişim boş kalabilir: $x<1$ ve $x>3$ koşullarını birlikte sağlayan hiçbir sayı yoktur.",
            dikkat(
                "Kareli eşitsizliği birinci dereceden gibi çözmek.",
                "$x^2<9$ eşitsizliğinin çözümü $x<3$ değildir; $x=-5$ için $x^2=25$ olur ve eşitsizlik sağlanmaz. Doğru çözüm $-3<x<3$ tür. Bu tür eşitsizlikler, mutlak değerdeki uzaklık fikriyle ya da ikinci dereceden eşitsizlik yöntemleriyle çözülür."),
        ]},
        {"baslik": "Eşitsizliklerde toplama ve değer aralığı", "icerik": [
            "Aynı yönlü iki eşitsizlik taraf tarafa toplanabilir: $a<b$ ve $c<d$ ise $a+c<b+d$ dir. Ama taraf tarafa <strong>çıkarma yapılamaz</strong>. İki değişkenin farkının aralığı, en küçük değerden en büyük değer çıkarılarak ve tersi yapılarak bulunur.",
            ornek(
                "$2<x<5$ ve $1<y<3$ olsun.",
                "$x+y$, $x-y$ ve $x \\cdot y$ ifadelerinin aralıklarını bulalım.",
                "Toplam: taraf tarafa toplayalım: $3<x+y<8$.",
                "Fark: en küçük fark $2-3=-1$, en büyük fark $5-1=4$; yani $-1<x-y<4$.",
                "Çarpım: $x$ ve $y$ pozitif olduğu için uçlar çarpılır: $2<x \\cdot y<15$."),
            dikkat(
                "Farkın aralığını uçları çıkararak bulmak.",
                "$2<x<5$ ve $1<y<3$ eşitsizliklerini taraf tarafa çıkarıp $1<x-y<2$ demek yanlıştır. Örneğin $x=4.9$ ve $y=1.1$ için $x-y=3.8$ olur ve bu değer $2$ den büyüktür."),
            "Çarpımda uçları doğrudan çarpmak yalnızca bütün değerler pozitifken güvenlidir. Negatif değerler işe karıştığında dört uç çarpımın hepsi hesaplanır ve en küçüğü ile en büyüğü seçilir.",
        ]},
        {"baslik": "Mutlak değerli eşitsizlikler", "icerik": [
            "$|x-a|$, sayı doğrusunda $x$ ile $a$ arasındaki uzaklıktır. Bu yüzden mutlak değerli eşitsizlikler uzaklık diliyle kolayca okunur:",
            "<ul><li>$|x-a|<r$: $x$, $a$ ya $r$ den daha yakındır; yani $a-r<x<a+r$.</li>"
            "<li>$|x-a|>r$: $x$, $a$ dan $r$ den daha uzaktır; yani $x<a-r$ ya da $x>a+r$.</li></ul>",
            ornek(
                "$|x-2|<3$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "Sıralı eşitsizliğe çevirelim: $-3<x-2<3$.",
                "Üç tarafa $2$ ekleyelim: $-1<x<5$."),
            ornek(
                "$|x+1| \\geq 4$ eşitsizliği verilsin.",
                "Eşitsizliği çözelim.",
                "Birinci durum: $x+1 \\geq 4$, yani $x \\geq 3$.",
                "İkinci durum: $x+1 \\leq -4$, yani $x \\leq -5$.",
                "Çözüm kümesi: $(-\\infty, -5] \\cup [3, \\infty)$."),
            "Sağ taraf negatifse durum özeldir: mutlak değer hiçbir zaman negatif olmadığı için $|x-2|<-1$ eşitsizliğini sağlayan sayı yoktur, $|x-2|>-1$ eşitsizliği ise her gerçek sayı için doğrudur.",
            "Mutlak değerin ayrıntısı <a href=\"/blog/mutlak-deger-konu-anlatimi-pdf/\">Mutlak Değer Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Problemden eşitsizliğe", "icerik": [
            "\"En az\", \"en fazla\", \"aşmamak\", \"geçmek\" gibi ifadeler bir eşitsizlik kurulacağını gösterir. \"En az\" $\\geq$, \"en fazla\" ve \"aşmamak\" $\\leq$ işaretine karşılık gelir.",
            ornek(
                "Bir öğrencinin $500$ lirası var ve tanesi $45$ lira olan kitaplardan almak istiyor.",
                "En fazla kaç kitap alabileceğini bulalım.",
                "Kitap sayısı $x$ olsun: $45x \\leq 500$.",
                "$x \\leq \\dfrac{500}{45}$, yani $x \\leq 11.1\\ldots$",
                "Kitap sayısı tam sayı olduğu için en fazla $11$ kitap alabilir. Kontrol: $11 \\cdot 45=495$, $12 \\cdot 45=540$."),
            ornek(
                "Bir öğrencinin iki sınav notu $62$ ve $75$ tir; üç sınavın ortalaması en az $70$ olursa dersi geçecek.",
                "Üçüncü sınavdan en az kaç alması gerektiğini bulalım.",
                "Üçüncü not $x$ olsun: $\\dfrac{62+75+x}{3} \\geq 70$.",
                "İki tarafı $3$ ile çarpalım: $137+x \\geq 210$.",
                "$x \\geq 73$; en az $73$ alması gerekir."),
            ornek(
                "Bir öğrenci topluluğu bir etkinlik için $1200$ liraya salon kiralıyor ve biletleri $50$ liradan satacak.",
                "Zarar etmemek için en az kaç bilet satılması gerektiğini bulalım.",
                "Satılan bilet sayısı $x$ olsun. Gelir, salon ücretinden az olmamalı: $50x \\geq 1200$.",
                "$x \\geq 24$; en az $24$ bilet satılmalıdır.",
                "Kontrol: $24 \\cdot 50=1200$ lira; gelir gideri tam karşılar."),
            "Bu tür sorularda sonucun tam sayı olması gerekip gerekmediğine dikkat etmek gerekir. Kişi, kitap ya da bilet sayısı tam sayıdır; bu yüzden \"en az\" sorularında çözüm yukarı, \"en fazla\" sorularında aşağı doğru en yakın tam sayıya tamamlanır.",
        ]},
        {"baslik": "Sınavda eşitsizlikler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu birinci dereceden ve sıralı eşitsizlikler, tam sayı çözümleri sayma, değer aralığı ve mutlak değerli eşitsizlikler biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde eşitsizlikler, \"en az\" ve \"en fazla\" içeren problemlerde ve sayısal akıl yürütmede de gerekebilir."),
            "Seçenekli sorularda çözüm aralığından bir değer ve aralığın dışından bir değer seçip ilk eşitsizlikte denemek, yönün doğru olup olmadığını birkaç saniyede gösterir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Negatife bölünce yönü çevirmemek", "$-2x \\geq 8$ ise $x \\leq -4$"],
                ["Sıralıda yalnız bir işareti çevirmek", "İki işaret de döner"],
                ["Eşitsizlikleri taraf tarafa çıkarmak", "Uçları çapraz çıkar"],
                ["$\\infty$ yanına köşeli parantez koymak", "$[1, \\infty)$"],
                ["Uç noktayı yanlış saymak", "$<$ dahil etmez, $\\leq$ eder"],
                ["$x$ in işaretini bilmeden $x$ ile çarpmak", "Önce işaretini belirle"],
            ]),
            "Bu hataların çoğu, yönü değiştiren tek işlemin negatif sayıyla çarpma ve bölme olduğunu unutmaktan doğar. Her adımda \"bu işlem yönü değiştirir mi?\" diye sormak ve sonucu aralıktan seçilen bir sayıyla denemek bu hataları önler.",
        ]},
    ],
    "sss": [
        ("Eşitsizlik nedir?",
         "İki ifadenin büyüklük ilişkisini gösteren bağıntıdır. Küçüktür, büyüktür, küçük eşittir ve büyük eşittir işaretleriyle yazılır."),
        ("Eşitsizlikte yön ne zaman değişir?",
         "İki taraf negatif bir sayıyla çarpıldığında ya da negatif bir sayıya bölündüğünde yön ters çevrilir. Toplama, çıkarma ve pozitif sayıyla çarpma yönü değiştirmez."),
        ("Aralık gösteriminde köşeli ve normal parantez farkı nedir?",
         "Köşeli parantez uç noktanın çözüme dahil olduğunu, normal parantez dahil olmadığını gösterir. Sonsuzluğun yanında her zaman normal parantez kullanılır."),
        ("Sıralı eşitsizlik nasıl çözülür?",
         "Her işlem üç tarafa birden uygulanır. Negatif bir sayıyla çarpılır ya da bölünürse iki işaret de ters döner."),
        ("İki eşitsizlik taraf tarafa çıkarılabilir mi?",
         "Hayır. Aynı yönlü eşitsizlikler toplanabilir ama çıkarılamaz. Farkın aralığı, bir değişkenin uçlarından diğerinin uçları çapraz çıkarılarak bulunur."),
        ("Mutlak değerli eşitsizlik nasıl çözülür?",
         "Küçüktür biçimindeki eşitsizlik tek bir sıralı eşitsizliğe, büyüktür biçimindeki ise iki ayrı eşitsizliğe ayrılır ve çözümler birleştirilir."),
        ("Ve ile ya da bağlaçlarının farkı nedir?",
         "Ve ile verilen iki koşulu aynı anda sağlayan sayılar aranır; çözüm iki aralığın kesişimidir. Ya da ile verilen koşullarda en az birini sağlamak yeter; çözüm birleşimdir."),
        ("En az ve en fazla ifadeleri hangi işarete karşılık gelir?",
         "En az ifadesi büyük ya da eşittir, en fazla ve aşmamak ifadeleri küçük ya da eşittir işaretine karşılık gelir. Fazla ve geçmek ise eşitliği içermeyen büyüktür işaretiyle yazılır."),
    ],
    "kontrol": [
        "Dört eşitsizlik işaretini doğru okuyup yazabiliyorum.",
        "Hangi işlemlerin yönü değiştirdiğini açıklayabiliyorum.",
        "Negatif sayıyla çarpınca yönün neden döndüğünü sayı doğrusuyla gösterebiliyorum.",
        "Birinci dereceden eşitsizlikleri çözebiliyorum.",
        "Çözüm kümesini aralık gösterimiyle ve sayı doğrusunda gösterebiliyorum.",
        "Uç noktaları doğru dahil ederek tam sayı çözümleri sayabiliyorum.",
        "Sıralı eşitsizliklerde üç tarafa birden işlem yapabiliyorum.",
        "İki değişkenin toplamının ve farkının aralığını bulabiliyorum.",
        "Mutlak değerli eşitsizlikleri uzaklık diliyle çözebiliyorum.",
        "\"En az\" ve \"en fazla\" içeren problemleri eşitsizlikle kurabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birinci-dereceden-denklemler-konu-anlatimi-pdf", "mutlak-deger-konu-anlatimi-pdf", "sayi-dogrusu-ve-sayilari-siralama"],
}
