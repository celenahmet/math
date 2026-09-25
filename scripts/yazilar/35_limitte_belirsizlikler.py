# scripts/yazilar/35_limitte_belirsizlikler.py — Limitte Belirsizlikler (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "limitte-belirsizlikler",
    "baslik": "Limitte Belirsizlikler Nasıl Çözülür?",
    "aciklama": "Limitte belirsizlikler nasıl çözülür? Sıfır bölü sıfır, sonsuz bölü sonsuz, sonsuz eksi sonsuz; çarpanlara ayırma, eşlenik, trigonometrik limitler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "limitte-belirsizlikler",
    "kapak_alt": "Limitte belirsizlikler: birbirine dolanmış mavi ve yeşil şerit parçalarını ayırıp ışıklı hedefe giden düzgün yollara dönüştüren iki öğrenci",
    "ozet": "Limit hesaplarken yerine yazma bazen sıfır bölü sıfır ya da sonsuz bölü sonsuz gibi anlamsız görünen bir sonuç verir. Bu durumlara belirsizlik denir; limitin olmadığını değil, ifadenin sadeleştirilmesi gerektiğini gösterir. Bu yazıda belirsizlik türlerini ve neden belirsiz olduklarını, çarpanlara ayırma, eşlenikle çarpma ve değişken değiştirme yöntemlerini, limiti sonlu yapan parametreyi, temel trigonometrik limitleri, sonsuz bölü sonsuz, sonsuz eksi sonsuz ve sıfır çarpı sonsuz belirsizliklerini ve belirsiz olmayan durumları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Belirsizlik nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için limitin temel fikrini, tek yönlü limitleri ve çarpanlara ayırmayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/limit-konu-anlatimi/\">Limit Konu Anlatımı</a> ve <a href=\"/blog/polinomlarda-carpanlara-ayirma/\">Polinomlarda Çarpanlara Ayırma</a> yazılarına göz at."),
            "Bir limitte yerine yazma yapıldığında $\\dfrac{0}{0}$, $\\dfrac{\\infty}{\\infty}$ ya da $\\infty-\\infty$ gibi bir ifade çıkarsa sonuç hakkında hemen bir şey söylenemez. Bu tür ifadelere <strong>belirsizlik</strong> denir. Belirsizlik bir cevap değil, bir uyarıdır: ifade sadeleştirilmeden limit bulunamaz ve sonuç tahmin edilemez.",
            "Kapaktaki öğrenciler birbirine dolanmış şerit parçalarını ayırıp düzgün yollar hâline getiriyor; yollar sonunda ışıklı bir hedefe ulaşıyor. Belirsizlik çözmek de budur: karışık görünen ifade sadeleştirilir ve limitin gerçek değeri ortaya çıkar.",
        ]},
        {"baslik": "Belirsizlik türleri", "icerik": [
            "Lise matematiğinde karşılaşılan belirsizlikler ve ilk akla gelmesi gereken yöntemler şunlardır:",
            tablo(["Belirsizlik", "Nerede görülür?", "İlk yöntem"], [
                ["$\\dfrac{0}{0}$", "Pay ve payda aynı noktada sıfır", "Çarpanlara ayırma, eşlenik"],
                ["$\\dfrac{\\infty}{\\infty}$", "Sonsuzda rasyonel ifadeler", "En büyük kuvvete bölme"],
                ["$\\infty-\\infty$", "Köklü farklar, kesir farkları", "Eşlenik, payda eşitleme"],
                ["$0 \\cdot \\infty$", "Sıfıra giden ile büyüyen çarpım", "Kesre çevirme"],
            ]),
            "Bunların dışında $1^{\\infty}$, $0^0$ ve $\\infty^0$ biçiminde üstel belirsizlikler de vardır; bunlar genellikle logaritma ve türev yardımıyla çözülür.",
        ]},
        {"baslik": "Neden belirsiz?", "icerik": [
            "$\\dfrac{0}{0}$ biçimindeki bir limit, pay ve paydanın sıfıra hangi hızla gittiğine bağlı olarak her sonucu verebilir. Aşağıdaki üç limitin üçü de yerine yazınca $\\dfrac{0}{0}$ verir ama sonuçları tamamen farklıdır:",
            tablo(["Limit", "Sadeleşmiş hâli", "Sonuç"], [
                ["$\\lim_{x \\to 0}\\dfrac{x}{x}$", "$1$", "$1$"],
                ["$\\lim_{x \\to 0}\\dfrac{x^2}{x}$", "$x$", "$0$"],
                ["$\\lim_{x \\to 0^+}\\dfrac{x}{x^2}$", "$\\dfrac{1}{x}$", "$\\infty$"],
            ]),
            hap("Belirsizlik, limitin olmadığı anlamına gelmez.",
                "İfade sadeleştirilince limit bir sayı, sonsuz ya da yok çıkabilir."),
        ]},
        {"baslik": "Çarpanlara ayırma", "icerik": [
            "Rasyonel bir ifadede pay ve payda $x=a$ da sıfır oluyorsa ikisi de $(x-a)$ çarpanını içerir. Pay ve payda çarpanlarına ayrılır, ortak çarpan sadeleştirilir ve sonra yerine yazılır.",
            ornek(
                "$\\lim_{x \\to 2}\\dfrac{x^2-4}{x^2-3x+2}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay $(x-2)(x+2)$, payda $(x-2)(x-1)$ olarak ayrılır; $x-2$ sadeleşir.",
                "Limit $\\lim_{x \\to 2}\\dfrac{x+2}{x-1}=4$ olur."),
            "Sadeleştirme $x \\neq 2$ için yapılır. Limit $x=2$ nin kendisine değil yakın değerlerine baktığı için bu işlem limiti değiştirmez. Sadeleşmiş ifadenin grafiği, asıl fonksiyonun grafiğiyle $x=2$ deki boşluk dışında tamamen aynıdır; limit de bu boşluğun yüksekliğidir.",
        ]},
        {"baslik": "Özdeşliklerle çarpanlara ayırma", "icerik": [
            "Küp farkı, küp toplamı ve iki kare farkı gibi özdeşlikler belirsizlik sorularında çok sık kullanılır. $a^3-b^3=(a-b)(a^2+ab+b^2)$ ve $a^3+b^3=(a+b)(a^2-ab+b^2)$ özdeşlikleri özellikle önemlidir.",
            ornek(
                "$\\lim_{x \\to 1}\\dfrac{x^3-1}{x-1}$ ve $\\lim_{x \\to -1}\\dfrac{x^3+1}{x^2-1}$ limitleri verilsin.",
                "Limitleri bulalım.",
                "Birincide pay $(x-1)(x^2+x+1)$ olur; limit $1+1+1=3$ tür.",
                "İkincide pay $(x+1)(x^2-x+1)$, payda $(x+1)(x-1)$ olur; limit $\\dfrac{3}{-2}=-\\dfrac{3}{2}$ olur."),
        ]},
        {"baslik": "Çift kök ve bölme", "icerik": [
            "Payda $(x-a)^2$ gibi bir kare içeriyorsa payın da $a$ da çift katlı kökü olması gerekir. Pay polinom bölmesiyle $(x-a)$ ya iki kez bölünür ve sadeleştirme yapılır.",
            ornek(
                "$\\lim_{x \\to 2}\\dfrac{x^3-3x^2+4}{(x-2)^2}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay $x=2$ de sıfırdır ve bölme yapılınca $x^3-3x^2+4=(x-2)^2(x+1)$ bulunur.",
                "Sadeleşince limit $\\lim_{x \\to 2}(x+1)=3$ olur."),
            "Payın çarpanlara ayrılması için <a href=\"/blog/polinomlarda-bolme/\">Polinomlarda Bölme</a> yazısındaki bölme yöntemleri kullanılabilir.",
        ]},
        {"baslik": "Eşlenikle çarpma", "icerik": [
            "Karekök içeren ifadelerde belirsizlik çoğu zaman eşlenikle çarpılarak giderilir. $\\sqrt{a}-b$ ifadesinin eşleniği $\\sqrt{a}+b$ dir ve çarpımları $a-b^2$ olur; kök böylece ortadan kalkar.",
            ornek(
                "$\\lim_{x \\to 4}\\dfrac{\\sqrt{x}-2}{x-4}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay ve payda $\\sqrt{x}+2$ ile çarpılır: pay $x-4$ olur ve paydadaki $x-4$ ile sadeleşir.",
                "Limit $\\lim_{x \\to 4}\\dfrac{1}{\\sqrt{x}+2}=\\dfrac{1}{4}$ olur."),
            "Payda $x-4$ yerine $(\\sqrt{x}-2)(\\sqrt{x}+2)$ olarak da yazılabilir; bu, eşlenik yönteminin çarpanlara ayırma ile aynı fikre dayandığını gösterir.",
        ]},
        {"baslik": "Paydada kök", "icerik": [
            "Kök paydadaysa eşlenikle çarpma yine uygulanır; bu kez eşlenik paydadaki köke göre seçilir. Pay ve payda aynı ifadeyle çarpıldığı için kesrin değeri değişmez, yalnızca biçimi değişir.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{x}{\\sqrt{x+9}-3}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay ve payda $\\sqrt{x+9}+3$ ile çarpılır; payda $x+9-9=x$ olur ve paydaki $x$ ile sadeleşir.",
                "Limit $\\lim_{x \\to 0}(\\sqrt{x+9}+3)=6$ olur."),
        ]},
        {"baslik": "İki köklü ifade", "icerik": [
            "Hem payın hem paydanın içinde kök bulunuyorsa ikisi de kendi eşleniğiyle çarpılır. Böylece iki kök de ortadan kalkar ve ortak çarpan sadeleşir.",
            ornek(
                "$\\lim_{x \\to 3}\\dfrac{\\sqrt{x+1}-2}{\\sqrt{x-2}-1}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay $\\sqrt{x+1}+2$ ile çarpılınca $x-3$, payda $\\sqrt{x-2}+1$ ile çarpılınca yine $x-3$ olur; ifade $\\dfrac{\\sqrt{x-2}+1}{\\sqrt{x+1}+2}$ e dönüşür.",
                "Limit $\\dfrac{1+1}{2+2}=\\dfrac{1}{2}$ olur."),
        ]},
        {"baslik": "Değişken değiştirme", "icerik": [
            "Küpkök ya da daha yüksek dereceli kökler içeren ifadelerde kök yeni bir değişkenle gösterilir. Böylece ifade polinomlar arasında bir bölüme dönüşür ve çarpanlara ayırma uygulanır. Değişken değiştirilirken yaklaşılan noktanın da yeni değişkene göre yazılması unutulmamalıdır: $x$ $8$ e giderken $t$ $2$ ye gider.",
            ornek(
                "$\\lim_{x \\to 8}\\dfrac{\\sqrt[3]{x}-2}{x-8}$ limiti verilsin.",
                "Limiti bulalım.",
                "$t=\\sqrt[3]{x}$ yazılırsa $x=t^3$ olur ve $t$ $2$ ye yaklaşır: $\\dfrac{t-2}{t^3-8}=\\dfrac{1}{t^2+2t+4}$.",
                "Limit $\\dfrac{1}{4+4+4}=\\dfrac{1}{12}$ olur."),
        ]},
        {"baslik": "Limiti sonlu yapan parametre", "icerik": [
            "Payda sıfıra giderken limitin sonlu bir sayı olması için pay da sıfıra gitmek zorundadır. Aksi hâlde sıfırdan farklı bir sayı sıfıra bölünür ve limit sonsuz olur. Bu gözlem, bilinmeyen katsayıları bulmak için kullanılır.",
            ornek(
                "$\\lim_{x \\to 2}\\dfrac{x^2+ax-6}{x-2}$ limiti bir gerçek sayı olsun.",
                "$a$ yı ve limiti bulalım.",
                "Pay $x=2$ de sıfır olmalı: $4+2a-6=0$, yani $a=1$.",
                "Pay $x^2+x-6=(x-2)(x+3)$ olur; limit $2+3=5$ bulunur."),
        ]},
        {"baslik": "Temel trigonometrik limit", "icerik": [
            "Trigonometrik belirsizliklerin çoğu tek bir temel limite indirilir: $x$ radyan cinsinden sıfıra giderken $\\dfrac{\\sin x}{x}$ in limiti $1$ dir. Buradan tanjant için de aynı sonuç çıkar: $\\lim_{x \\to 0}\\dfrac{\\tan x}{x}=1$.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{\\sin 3x}{x}$ limiti verilsin.",
                "Limiti bulalım.",
                "İfade $3 \\cdot \\dfrac{\\sin 3x}{3x}$ biçiminde yazılır; $3x$ de sıfıra gider.",
                "Limit $3 \\cdot 1=3$ olur."),
            "Genel olarak $\\lim_{x \\to 0}\\dfrac{\\sin ax}{bx}=\\dfrac{a}{b}$ dır. Aynı kural tanjant için de geçerlidir ve sinüs ile tanjant birbirinin yerine kullanılabilir.",
        ]},
        {"baslik": "Sinüslerin oranı", "icerik": [
            "Pay ve paydada sinüs varsa her ikisi de kendi açısına bölünüp çarpılır. Böylece iki temel limit ve açıların oranı kalır.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{\\sin 5x}{\\sin 2x}$ limiti verilsin.",
                "Limiti bulalım.",
                "İfade $\\dfrac{\\sin 5x}{5x} \\cdot \\dfrac{2x}{\\sin 2x} \\cdot \\dfrac{5x}{2x}$ biçiminde yazılır.",
                "İlk iki çarpan $1$ e gider; limit $\\dfrac{5}{2}$ olur."),
        ]},
        {"baslik": "Tanjant ve sinüs birlikte", "icerik": [
            "Tanjant da sıfır yakınında sinüs gibi davrandığı için $\\dfrac{\\tan ax}{\\sin bx}$ biçimindeki bir limit de açıların oranına eşittir. Her iki fonksiyon kendi açısına bölünüp çarpılarak bu sonuç gösterilir.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{\\tan 4x}{\\sin 2x}$ limiti verilsin.",
                "Limiti bulalım.",
                "İfade $\\dfrac{\\tan 4x}{4x} \\cdot \\dfrac{2x}{\\sin 2x} \\cdot 2$ biçiminde yazılır.",
                "İlk iki çarpan $1$ e gider; limit $2$ olur."),
        ]},
        {"baslik": "Kosinüslü belirsizlik", "icerik": [
            "$1-\\cos x$ içeren ifadelerde iki kat açı formülü kullanılır: $1-\\cos x=2\\sin^2 \\dfrac{x}{2}$. Böylece ifade sinüslü bir ifadeye dönüşür ve temel limit uygulanır.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{1-\\cos x}{x^2}$ limiti verilsin.",
                "Limiti bulalım.",
                "İfade $\\dfrac{2\\sin^2 \\dfrac{x}{2}}{x^2}=\\dfrac{1}{2}\\left(\\dfrac{\\sin \\dfrac{x}{2}}{\\dfrac{x}{2}}\\right)^2$ olur.",
                "Parantez içi $1$ e gittiği için limit $\\dfrac{1}{2}$ olur."),
            "Kullanılan formülün ayrıntısı için <a href=\"/blog/iki-kat-yarim-aci/\">İki Kat Açı ve Yarım Açı Formülleri</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Polinom ve sinüs birlikte", "icerik": [
            "Payda $x$ varsa ve pay birden fazla terimden oluşuyorsa kesir terimlere ayrılır. Her terimin limiti ayrı hesaplanır; sinüslü terim için temel limit kullanılır.",
            ornek(
                "$\\lim_{x \\to 0}\\dfrac{x^2+\\sin x}{x}$ limiti verilsin.",
                "Limiti bulalım.",
                "Kesir $x+\\dfrac{\\sin x}{x}$ biçiminde iki parçaya ayrılır.",
                "Birinci parça $0$ a, ikincisi $1$ e gider; limit $1$ olur."),
        ]},
        {"baslik": "Belirsizlik ve mutlak değer", "icerik": [
            "Sadeleştirmeden sonra bile iki yönün sonucu farklı çıkabilir. Paydada mutlak değer varsa sıfır bölü sıfır belirsizliği çözülürken tek yönlü limitlere ayrı ayrı bakmak gerekir.",
            ornek(
                "$\\lim_{x \\to 3}\\dfrac{x^2-9}{|x-3|}$ limiti verilsin.",
                "Limiti inceleyelim.",
                "Sağdan yaklaşırken $|x-3|=x-3$ olduğundan ifade $x+3$ e, yani $6$ ya gider.",
                "Soldan yaklaşırken ifade $-(x+3)$ e, yani $-6$ ya gider; iki yön farklı olduğu için limit yoktur."),
        ]},
        {"baslik": "Sonsuz bölü sonsuz", "icerik": [
            "$x$ sonsuza giderken pay ve payda birlikte sınırsız büyüyorsa $\\dfrac{\\infty}{\\infty}$ belirsizliği vardır. Pay ve payda paydaki en büyük kuvvete bölünür; küçük kuvvetli terimler sıfıra gider.",
            ornek(
                "$\\lim_{x \\to \\infty}\\dfrac{4x^2-x}{2x^2+5}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay ve payda $x^2$ ye bölünür: $\\dfrac{4-\\dfrac{1}{x}}{2+\\dfrac{5}{x^2}}$.",
                "Kesirli terimler sıfıra gider; limit $\\dfrac{4}{2}=2$ olur."),
            "Genel kural derecelere bakmaktır: pay derecesi küçükse limit $0$, dereceler eşitse baş katsayılar oranı, pay derecesi büyükse sonsuzdur.",
        ]},
        {"baslik": "Eksi sonsuza giden bölüm", "icerik": [
            "Pay derecesi paydadan büyükse limit sonsuzdur, ama işareti baş katsayıların işaretine bağlıdır. Bu yüzden sonucu yazmadan önce en büyük dereceli terimlerin işaretlerine mutlaka bakılmalıdır. Baş katsayıların oranı negatifse ifade eksi sonsuza gider.",
            ornek(
                "$\\lim_{x \\to \\infty}\\dfrac{1-x^3}{x^2+1}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay ve payda $x^2$ ye bölünür: $\\dfrac{\\dfrac{1}{x^2}-x}{1+\\dfrac{1}{x^2}}$.",
                "Pay $-\\infty$ a, payda $1$ e gittiği için limit $-\\infty$ olur."),
        ]},
        {"baslik": "Köklü sonsuz bölü sonsuz", "icerik": [
            "Kök içindeki en büyük kuvvet dışarı çıkarılırken işarete dikkat etmek gerekir; çünkü $\\sqrt{x^2}=|x|$ tir. $x$ eksi sonsuza giderken $|x|=-x$ olduğundan sonuç işaret değiştirebilir.",
            ornek(
                "$\\lim_{x \\to \\infty}\\dfrac{\\sqrt{x^2+1}}{x}$ ve $\\lim_{x \\to -\\infty}\\dfrac{\\sqrt{x^2+1}}{x}$ limitleri verilsin.",
                "Limitleri bulalım.",
                "Pay $|x|\\sqrt{1+\\dfrac{1}{x^2}}$ olarak yazılır. Artı sonsuzda $|x|=x$ olduğundan limit $1$ olur.",
                "Eksi sonsuzda $|x|=-x$ olduğundan limit $-1$ olur."),
        ]},
        {"baslik": "Sonsuz eksi sonsuz", "icerik": [
            "İki terim birlikte sonsuza gidiyor ve aralarında fark alınıyorsa $\\infty-\\infty$ belirsizliği vardır. Köklü farklarda eşlenikle çarpılarak ifade bir bölüme çevrilir.",
            ornek(
                "$\\lim_{x \\to \\infty}\\left(\\sqrt{x^2+4x}-x\\right)$ limiti verilsin.",
                "Limiti bulalım.",
                "Eşlenikle çarpınca ifade $\\dfrac{4x}{\\sqrt{x^2+4x}+x}$ olur.",
                "Pay ve payda $x$ e bölünce $\\dfrac{4}{\\sqrt{1+\\dfrac{4}{x}}+1}$ elde edilir; limit $2$ olur."),
        ]},
        {"baslik": "Kesirlerin farkı", "icerik": [
            "İki kesrin paydaları aynı noktada sıfıra gidiyorsa her biri sonsuza gider ve farkları $\\infty-\\infty$ belirsizliği oluşturur. Paydalar eşitlenerek tek bir kesir elde edilir ve çoğu zaman $\\dfrac{0}{0}$ belirsizliğine dönüşür.",
            ornek(
                "$\\lim_{x \\to 1}\\left(\\dfrac{1}{x-1}-\\dfrac{2}{x^2-1}\\right)$ limiti verilsin.",
                "Limiti bulalım.",
                "Payda eşitlenince $\\dfrac{x+1-2}{x^2-1}=\\dfrac{x-1}{(x-1)(x+1)}=\\dfrac{1}{x+1}$ olur.",
                "Limit $\\dfrac{1}{2}$ olur."),
        ]},
        {"baslik": "Sıfır çarpı sonsuz", "icerik": [
            "Bir çarpanı sıfıra, diğeri sonsuza giden çarpımlar $0 \\cdot \\infty$ belirsizliği oluşturur. Çarpanlardan biri kesrin paydasına alınarak ifade $\\dfrac{0}{0}$ ya da $\\dfrac{\\infty}{\\infty}$ biçimine çevrilir.",
            ornek(
                "$\\lim_{x \\to \\infty} x\\sin \\dfrac{1}{x}$ limiti verilsin.",
                "Limiti bulalım.",
                "$t=\\dfrac{1}{x}$ yazılırsa $t$ sıfıra gider ve ifade $\\dfrac{\\sin t}{t}$ olur.",
                "Temel trigonometrik limitle sonuç $1$ olur."),
        ]},
        {"baslik": "Üstel ifadelerde sonsuz", "icerik": [
            "Üstel ifadelerde de $\\dfrac{\\infty}{\\infty}$ belirsizliği görülür. Bu durumda en hızlı büyüyen üstel terime bölünür; tabanı daha küçük olan kuvvetler bu bölümde sıfıra gider.",
            ornek(
                "$\\lim_{x \\to \\infty}\\dfrac{2^x+3^x}{3^x}$ limiti verilsin.",
                "Limiti bulalım.",
                "İfade $\\left(\\dfrac{2}{3}\\right)^x+1$ biçiminde yazılır.",
                "$\\dfrac{2}{3}$ nin kuvvetleri sıfıra gittiği için limit $1$ olur."),
        ]},
        {"baslik": "Belirsiz olmayan durumlar", "icerik": [
            "Her garip görünen ifade belirsizlik değildir. Aşağıdaki durumlarda sonuç doğrudan söylenebilir ve sadeleştirmeye gerek yoktur:",
            tablo(["İfade", "Sonuç"], [
                ["$\\dfrac{\\text{sıfırdan farklı sayı}}{0}$", "$\\pm\\infty$, işarete bakılır"],
                ["$\\dfrac{0}{\\text{sıfırdan farklı sayı}}$", "$0$"],
                ["$\\dfrac{\\text{sayı}}{\\infty}$", "$0$"],
                ["$\\infty+\\infty$", "$\\infty$"],
                ["$\\infty \\cdot \\infty$", "$\\infty$"],
            ]),
            "Sıfırdan farklı bir sayının sıfıra bölündüğü durumda tek yönlü limitlere bakılır. Ayrıntısı için <a href=\"/blog/sagdan-soldan-limit/\">Sağdan ve Soldan Limit Nasıl Bulunur?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Belirsizlik ve türev", "icerik": [
            "Türevin tanımı her zaman bir $\\dfrac{0}{0}$ belirsizliğidir: $h$ sıfıra giderken hem pay hem payda sıfıra gider. Bu yüzden türev hesabı, belirsizlik çözmenin sistemli bir biçimidir.",
            ornek(
                "$\\lim_{h \\to 0}\\dfrac{(3+h)^2-9}{h}$ limiti verilsin.",
                "Limiti bulalım.",
                "Pay açılınca $6h+h^2$ olur ve $h$ sadeleşir: $6+h$.",
                "Limit $6$ olur; bu sayı $x^2$ fonksiyonunun $3$ teki türevidir."),
            "Türev öğrenildikten sonra $\\dfrac{0}{0}$ ve $\\dfrac{\\infty}{\\infty}$ belirsizlikleri için pay ve paydanın türevlerini alan L'Hospital kuralı da kullanılabilir. Türevin tanımı <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Yöntem seçimi", "icerik": [
            tablo(["İfadede görülen", "Yöntem"], [
                ["Polinomlar bölümü, $\\dfrac{0}{0}$", "Çarpanlara ayır"],
                ["Karekök, $\\dfrac{0}{0}$", "Eşlenikle çarp"],
                ["Küpkök", "Değişken değiştir"],
                ["$\\sin$, $\\tan$, $x \\to 0$", "Temel trigonometrik limit"],
                ["$1-\\cos x$", "İki kat açı formülü"],
                ["$x \\to \\infty$, rasyonel", "En büyük kuvvete böl"],
                ["Köklü fark, $x \\to \\infty$", "Eşlenikle çarp"],
            ]),
            "Hangi yöntem seçilirse seçilsin amaç aynıdır: belirsizliğe yol açan ortak çarpanı ortaya çıkarıp sadeleştirmek ya da baskın terimi ayırmak.",
        ]},
        {"baslik": "Sınavda belirsizlikler", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) belirsizlikler; çarpanlara ayırma, eşlenikle çarpma, trigonometrik limitler, sonsuzda limit ve limiti sonlu yapan parametre biçiminde karşına çıkabilir.",
                "Parametre soruları özellikle sık sorulur."),
            "Her limit sorusunda önce yerine yaz. Sonuç belirsizse ifadenin türüne bakarak tablodaki yöntemi seç. Payda sıfıra giderken limitin sonlu olduğu söyleniyorsa payın da sıfır olması gerektiğini hemen bir denklem olarak yaz.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\dfrac{0}{0}$ çıkınca limit yok demek", "Önce sadeleştirilir"],
                ["$\\dfrac{0}{0}$ ı $1$ ya da $0$ saymak", "Sonuç ifadeye bağlı"],
                ["$\\infty-\\infty=0$ yazmak", "Eşlenik ya da payda eşitleme"],
                ["$\\sqrt{x^2}=x$ almak", "$\\sqrt{x^2}=|x|$"],
                ["$\\dfrac{\\sin 3x}{x}$ in limitini $1$ sanmak", "Limit $3$ tür"],
                ["Açıyı derece cinsinden kullanmak", "Temel limit radyan içindir"],
            ]),
            "Bu hataların ortak noktası, belirsiz bir ifadeye bir sayı gibi davranmaktır. Belirsizlik bir sonuç değil, işlemin henüz bitmediğini gösteren bir işarettir.",
        ]},
    ],
    "sss": [
        ("Limitte belirsizlik nedir?",
         "Yerine yazınca sıfır bölü sıfır, sonsuz bölü sonsuz ya da sonsuz eksi sonsuz gibi sonucu belli olmayan bir ifade çıkmasıdır."),
        ("0 bölü 0 belirsizliği nasıl çözülür?",
         "Polinomlarda çarpanlara ayrılır, köklü ifadelerde eşlenikle çarpılır, ortak çarpan sadeleştirildikten sonra yerine yazılır."),
        ("Eşlenikle çarpma ne zaman kullanılır?",
         "Pay ya da paydada karekök içeren bir fark varsa kullanılır. Kökün eşleniğiyle çarpınca kök ortadan kalkar."),
        ("sin 3x bölü x in sıfırdaki limiti kaçtır?",
         "sin ax bölü bx in sıfırdaki limiti a bölü b olduğu için sonuç 3 tür."),
        ("Sonsuz bölü sonsuz belirsizliği nasıl çözülür?",
         "Pay ve payda en büyük kuvvete bölünür. Rasyonel ifadelerde derecelere bakmak yeterlidir."),
        ("Limitin sonlu olması için pay neden sıfır olmalıdır?",
         "Payda sıfıra giderken pay sıfırdan farklı bir sayıya giderse kesir sınırsız büyür. Limitin sonlu olması için pay da sıfıra gitmelidir."),
        ("Belirsizlik çözüldükten sonra limit her zaman var mıdır?",
         "Hayır. Sadeleştirmeden sonra limit bir sayı çıkabileceği gibi sonsuz ya da soldan ve sağdan farklı da çıkabilir. Bu durumda limit yoktur."),
    ],
    "kontrol": [
        "Belirsizliğin ne olduğunu ve neden belirsiz olduğunu açıklayabiliyorum.",
        "Belirsizlik türlerini tanıyabiliyorum.",
        "Çarpanlara ayırarak sıfır bölü sıfır belirsizliğini çözebiliyorum.",
        "Eşlenikle çarpma yöntemini uygulayabiliyorum.",
        "Değişken değiştirme ile köklü limitleri hesaplayabiliyorum.",
        "Limiti sonlu yapan parametreyi bulabiliyorum.",
        "Temel trigonometrik limitleri kullanabiliyorum.",
        "Sonsuz bölü sonsuz belirsizliğini çözebiliyorum.",
        "Sonsuz eksi sonsuz ve sıfır çarpı sonsuz belirsizliklerini çözebiliyorum.",
        "Belirsiz olmayan durumları ayırt edebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["limit-konu-anlatimi", "sagdan-soldan-limit", "sureklilik-konu-anlatimi"],
}
