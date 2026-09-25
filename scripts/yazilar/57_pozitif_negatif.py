# scripts/yazilar/57_pozitif_negatif.py — Pozitif ve Negatif Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "pozitif-ve-negatif-sayilar",
    "baslik": "Pozitif ve Negatif Sayılar",
    "aciklama": "Pozitif ve negatif sayılar nedir? İşaret kuralları, negatif tabanlı kuvvetler, işaret problemleri, eşitsizlikte yön değişimi ve sıralama; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "pozitif-ve-negatif-sayilar",
    "kapak_alt": "Pozitif ve negatif sayılar: sıfırın iki yanına kırmızı ve mavi bilyeleri dizerek denge ve yön fikrini gösteren iki öğrenci",
    "ozet": "Sıfırın iki yanında iki ayrı dünya var: pozitif sayılar ve negatif sayılar. Borç ile alacak, sıfırın altı ile üstü, deniz seviyesinin altı ile üstü hep bu iki yönü anlatır. Bu yazıda pozitif ve negatif sayıları tanımlıyor, dört işlemde ve kuvvetlerde işaret kurallarını gerekçeleriyle veriyor, sayıların kendisini bilmeden bir ifadenin işaretini bulmayı, eşitsizlikte yön değişimini ve aralıklara göre sıralamayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Pozitif ve negatif sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için tam sayıları, dört işlemi ve sayı doğrusunu biliyor olman yeterli.",
                "Tam sayılarda dört işlemin temelleri için <a href=\"/blog/dogal-sayilar-ve-tam-sayilar/\">Doğal Sayılar ve Tam Sayılar</a> yazısına göz at."),
            "Sıfırdan büyük sayılara <strong>pozitif</strong>, sıfırdan küçük sayılara <strong>negatif</strong> sayı denir. Sayı doğrusunda pozitif sayılar sıfırın sağında, negatif sayılar solunda yer alır. <strong>Sıfır</strong> ne pozitif ne negatiftir; iki bölgeyi ayıran noktadır.",
            "Pozitif sayıların önündeki $+$ işareti genellikle yazılmaz: $+5$ ile $5$ aynı sayıdır. Negatif sayılarda ise $-$ işareti sayının parçasıdır ve yazılmak zorundadır.",
            "Sayı doğrusunda sıfıra eşit uzaklıktaki iki sayıya <strong>zıt sayılar</strong> denir: $5$ ile $-5$ gibi. Zıt sayıların toplamı sıfırdır. Bir sayının önüne eksi koymak, onu zıttına çevirmek demektir; bu yüzden $-(-5)=5$ olur.",
            hap("Pozitif sayılar sıfırın sağında, negatif sayılar solundadır; sıfır ne pozitif ne negatiftir.",
                "Bir sayının zıttı, önüne eksi konarak bulunur ve $-(-a)=a$ dır."),
        ]},
        {"baslik": "Günlük hayatta negatif sayılar", "icerik": [
            "Negatif sayılar soyut bir fikir değildir; günlük hayatta bir yönün tersini anlatmak için sürekli kullanılır:",
            "<ul><li><strong>Sıcaklık:</strong> sıfırın altındaki sıcaklıklar negatif sayıyla gösterilir: $-7$ derece gibi.</li>"
            "<li><strong>Yükseklik:</strong> deniz seviyesinin altındaki noktalar negatif yükseklikle ifade edilir.</li>"
            "<li><strong>Bakiye:</strong> hesaptaki borç negatif, alacak pozitif sayıyla düşünülebilir.</li>"
            "<li><strong>Kat numaraları:</strong> zemin katın altındaki bodrum katlar bazı binalarda eksiyle numaralandırılır.</li>"
            "<li><strong>Averaj:</strong> bir takımın yediği gol attığı golden fazlaysa averajı negatiftir.</li></ul>",
            ornek(
                "Bir şehirde sabah sıcaklık $-7$ derece, öğleden sonra $5$ derece olsun.",
                "Sıcaklık kaç derece artmıştır?",
                "Artış, son değerden ilk değerin çıkarılmasıyla bulunur: $5-(-7)$.",
                "Negatif bir sayıyı çıkarmak, pozitifini eklemektir: $5+7=12$.",
                "Sıcaklık $12$ derece artmıştır. Sayı doğrusunda $-7$ den $5$ e giden yol da $12$ birimdir."),
            ornek(
                "Bir dalgıç deniz seviyesinin $12$ metre altında, bir martı ise deniz seviyesinin $30$ metre üstünde olsun.",
                "Aralarındaki yükseklik farkı kaç metredir?",
                "Deniz seviyesini $0$ kabul edelim: dalgıcın konumu $-12$, martınınki $30$.",
                "Fark, büyük değerden küçük değerin çıkarılmasıyla bulunur: $30-(-12)=30+12$.",
                "Aralarındaki fark $42$ metredir."),
            hap("Gündüz sıcaklığı $5$ derece, gece sıcaklığı $-3$ derece olan bir günde sıcaklık farkı $5-(-3)=8$ derece olur.", "Negatif bir sayıyı çıkarmak, onun mutlak değerini eklemek demektir.", gunluk=True),
        ]},
        {"baslik": "Toplama ve çıkarmada işaret", "icerik": [
            "Toplamada iki durum vardır. <strong>Aynı işaretli</strong> sayılar toplanırken mutlak değerler toplanır ve ortak işaret sonuca yazılır. <strong>Farklı işaretli</strong> sayılar toplanırken büyük mutlak değerden küçüğü çıkarılır ve mutlak değeri büyük olanın işareti sonuca yazılır.",
            "Çıkarma için ayrı bir kural gerekmez: bir sayıyı çıkarmak, zıttını eklemektir. $a-b=a+(-b)$ olduğu için her çıkarma bir toplamaya dönüşür.",
            "Toplamayı sayı doğrusunda hareket olarak düşünmek de işe yarar: pozitif bir sayı eklemek sağa, negatif bir sayı eklemek sola gitmektir. $-3+5$ işleminde $-3$ ten başlayıp $5$ birim sağa gidersin ve $2$ ye ulaşırsın. $2-6$ işleminde ise $2$ den başlayıp $6$ birim sola gidersin ve $-4$ e ulaşırsın.",
            ornek(
                "$-8+13-(-4)-9$ işlemi verilsin.",
                "Sonucu adım adım bulalım.",
                "Çıkarmaları toplamaya çevirelim: $-8+13+4+(-9)$.",
                "Pozitifleri toplayalım: $13+4=17$. Negatifleri toplayalım: $-8+(-9)=-17$.",
                "Sonuç: $17+(-17)=0$."),
            hap("Uzun toplamlarda pozitifleri ve negatifleri <strong>ayrı ayrı</strong> topla, sonra ikisini birleştir.",
                "Çıkarma, zıt sayıyı eklemektir: $a-(-b)=a+b$."),
        ]},
        {"baslik": "Çarpma ve bölmede işaret", "icerik": [
            "Çarpma ve bölmede mutlak değerler çarpılır ya da bölünür, işaret ise tek bir kuralla bulunur: <strong>aynı işaretliler pozitif, farklı işaretliler negatif</strong> verir.",
            tablo(["İşaretler", "Sonuç"], [
                ["$(+) \\cdot (+)$", "Pozitif"],
                ["$(-) \\cdot (-)$", "Pozitif"],
                ["$(+) \\cdot (-)$", "Negatif"],
            ]),
            "Birden fazla çarpan olduğunda işaretleri tek tek çarpmak yerine <strong>negatif çarpanları saymak</strong> yeter: negatif çarpan sayısı çiftse çarpım pozitif, tekse negatiftir. Çarpanlardan biri sıfırsa çarpım sıfırdır ve işareti yoktur.",
            ornek(
                "$(-2) \\cdot (-3) \\cdot (-4) \\cdot 5$ çarpımı verilsin.",
                "Sonucun işaretini ve değerini bulalım.",
                "Negatif çarpan sayısı $3$; tek olduğu için sonuç negatiftir.",
                "Mutlak değerlerin çarpımı: $2 \\cdot 3 \\cdot 4 \\cdot 5=120$.",
                "Sonuç: $-120$."),
            "<h3>Eksi çarpı eksi neden artıdır?</h3>",
            "Bu kural ezberlenecek bir anlaşma değil, dağılma özelliğinin sonucudur. $a$ ve $b$ pozitif sayılar olsun. Bir sayının zıttıyla toplamı sıfır olduğu için $b+(-b)=0$ dır ve her sayının sıfırla çarpımı sıfırdır:",
            "$$(-a) \\cdot (b+(-b))=0$$",
            "Sol tarafı dağıtalım: $(-a) \\cdot b+(-a) \\cdot (-b)=0$. Farklı işaretli iki sayının çarpımı negatif olduğu için $(-a) \\cdot b=-ab$ dir. Öyleyse $-ab+(-a) \\cdot (-b)=0$ olur ve $(-a) \\cdot (-b)$, $-ab$ nin zıttı olmak zorundadır: $(-a) \\cdot (-b)=ab$.",
            "<h3>Bölmede ve kesirlerde işaret</h3>",
            "Bölme de aynı kurala uyar: $(-24):(-6)=4$ ve $(-24):6=-4$. Kesirlerde eksi işareti paya, paydaya ya da kesrin önüne yazılabilir; üçü de aynı sayıyı gösterir: $\\dfrac{-3}{4}=\\dfrac{3}{-4}=-\\dfrac{3}{4}$. Pay ve paydanın ikisi de negatifse kesir pozitiftir: $\\dfrac{-3}{-4}=\\dfrac{3}{4}$.",
        ]},
        {"baslik": "Kuvvetlerde işaret", "icerik": [
            "Kuvvet tekrarlı çarpma olduğu için aynı kural geçerlidir. Negatif bir sayının çift kuvveti pozitif, tek kuvveti negatiftir. Özellikle $-1$ tabanını akılda tut: $(-1)^{\\text{çift}}=1$ ve $(-1)^{\\text{tek}}=-1$.",
            dikkat(
                "$(-2)^4$ ile $-2^4$ farklıdır.",
                "$(-2)^4=16$ dır: parantez, eksinin de kuvvete girdiğini gösterir.",
                "$-2^4=-16$ dır: önce $2^4=16$ hesaplanır, sonra başına eksi konur. İşlem önceliğinde kuvvet, eksiden önce gelir."),
            ornek(
                "$(-2)^3+(-2)^2-(-2)^1$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Her kuvveti ayrı hesaplayalım: $(-2)^3=-8$, $(-2)^2=4$, $(-2)^1=-2$.",
                "Yerine yazalım: $-8+4-(-2)=-8+4+2$.",
                "Sonuç: $-2$."),
            ornek(
                "$(-1)^{2026}-(-1)^{2025}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "$2026$ çift olduğu için $(-1)^{2026}=1$.",
                "$2025$ tek olduğu için $(-1)^{2025}=-1$.",
                "Sonuç: $1-(-1)=2$."),
            ornek(
                "$-3^2+(-3)^2-2 \\cdot (-3)$ ifadesi verilsin.",
                "Değerini bulalım.",
                "$-3^2=-9$: kuvvet yalnızca $3$ e uygulanır, eksi sonra gelir.",
                "$(-3)^2=9$ ve $2 \\cdot (-3)=-6$.",
                "Yerine yazalım: $-9+9-(-6)=0+6=6$."),
        ]},
        {"baslik": "İşaret tablosu yöntemi", "icerik": [
            "Bazı sorularda sayıların kendisi verilmez, yalnızca işaretleri verilir ve bir ifadenin işareti sorulur. Bunun için her çarpanın işaretini ayrı ayrı bulup çarpma kuralını uygularsın. Kuvvetlerde çift kuvvetin her zaman pozitif, tek kuvvetin tabanla aynı işaretli olduğunu unutma.",
            ornek(
                "$a<0$, $b>0$ ve $c<0$ olsun.",
                "$\\dfrac{a^3 \\cdot b^2}{c}$ ifadesinin işaretini bulalım.",
                "$a^3$: negatif sayının tek kuvveti, negatif.",
                "$b^2$: pozitif.",
                "Pay negatif ile pozitifin çarpımı, yani negatif; payda $c$ negatif.",
                "Negatifin negatife bölümü pozitif: ifade pozitiftir.",
                "Kontrol: $a=-1$, $b=2$, $c=-4$ için $\\dfrac{(-1) \\cdot 4}{-4}=1$."),
            hap("Bir ifadenin işaretini bulmak için her çarpanın işaretini ayrı yaz, sonra negatifleri say.",
                "Çift kuvvet her zaman pozitif (taban sıfır değilse), tek kuvvet tabanla aynı işaretlidir."),
        ]},
        {"baslik": "İşaret problemleri", "icerik": [
            "Bir adım daha ileri: bazen ifadelerin işareti verilir ve sayıların işareti sorulur. Burada kuralı tersinden kullanırsın.",
            ornek(
                "$a$ ve $b$ sıfırdan farklı sayılar, $a \\cdot b>0$ ve $a+b<0$ olsun.",
                "$a$ ve $b$ nin işaretini bulalım.",
                "$a \\cdot b>0$ ise ikisi aynı işaretlidir.",
                "İkisi de pozitif olsaydı toplamları pozitif olurdu. Oysa $a+b<0$.",
                "Öyleyse ikisi de negatiftir."),
            ornek(
                "$a$ ve $b$ sıfırdan farklı sayılar, $a \\cdot b<0$ ve $a<b$ olsun.",
                "$a$ ve $b$ nin işaretini bulalım.",
                "$a \\cdot b<0$ ise ikisi farklı işaretlidir.",
                "Farklı işaretli iki sayıdan küçük olan negatif, büyük olan pozitiftir.",
                "$a<b$ olduğundan $a<0<b$."),
            ornek(
                "$a$ ve $b$ sıfırdan farklı sayılar ve $a^2 \\cdot b<0$ olsun.",
                "$b$ nin işareti nedir?",
                "$a \\neq 0$ olduğu için $a^2$ her zaman pozitiftir.",
                "Pozitif bir sayıyla çarpım negatif çıkıyorsa $b$ negatiftir.",
                "$a$ nın işareti hakkında ise hiçbir şey söylenemez."),
            ornek(
                "$a>0$, $a \\cdot b<0$ ve $b \\cdot c>0$ olsun.",
                "$b$, $c$ ve $a-c$ nin işaretini bulalım.",
                "$a>0$ ve $a \\cdot b<0$ ise $b$, $a$ ile farklı işaretlidir: $b<0$.",
                "$b \\cdot c>0$ ise $c$, $b$ ile aynı işaretlidir: $c<0$.",
                "Pozitif bir sayıdan negatif bir sayı çıkarmak, pozitif bir sayı eklemektir: $a-c>0$.",
                "Kontrol: $a=2$, $b=-1$, $c=-3$ için $a \\cdot b=-2$, $b \\cdot c=3$ ve $a-c=5$."),
            dikkat(
                "Toplamın işareti yalnızca işaretlerden her zaman bulunamaz.",
                "$a<0<b$ ise $a+b$ nin işareti mutlak değerlere bağlıdır: $-5+3<0$ ama $-2+3>0$. Böyle bir durumda \"belirlenemez\" cevabını görmek gerekir."),
        ]},
        {"baslik": "Negatif sayılarda eşitsizlik", "icerik": [
            "Eşitsizliklerde negatif sayılarla işlem yaparken bir kural hayati önem taşır: eşitsizliğin iki tarafı <strong>negatif bir sayıyla çarpılır ya da bölünürse eşitsizliğin yönü değişir</strong>.",
            "Örneğin $2<5$ doğrudur. İki tarafı $-1$ ile çarparsak $-2$ ve $-5$ elde ederiz ve sayı doğrusunda $-2$, $-5$ in sağındadır: $-2>-5$.",
            hap("Eşitsizliğin iki tarafı negatif bir sayıyla çarpılır ya da bölünürse yön değişir.",
                "Pozitif bir sayıyla çarpma ya da bölme yönü değiştirmez."),
            ornek(
                "$-2x+3>7$ eşitsizliği verilsin.",
                "$x$ in hangi değerleri için sağlandığını bulalım.",
                "İki taraftan $3$ çıkaralım: $-2x>4$.",
                "İki tarafı $-2$ ye bölelim; negatif bir sayıya böldüğümüz için yön değişir: $x<-2$.",
                "Kontrol: $x=-3$ için $-2 \\cdot (-3)+3=9$ ve $9>7$ sağlanır; $x=0$ için $3>7$ sağlanmaz."),
            "<h3>Terslerin sıralaması</h3>",
            "Aynı işaretli iki sayının terslerinde sıralama ters döner. İki negatif sayı için: $x<y<0$ ise $\\dfrac{1}{x}>\\dfrac{1}{y}$ dir.",
            ornek(
                "$-4$ ve $-2$ sayıları verilsin; $-4<-2$.",
                "$\\dfrac{1}{-4}$ ile $\\dfrac{1}{-2}$ i karşılaştıralım.",
                "$\\dfrac{1}{-4}=-0.25$ ve $\\dfrac{1}{-2}=-0.5$.",
                "$-0.25$, $-0.5$ ten büyüktür.",
                "Yani $-4<-2$ iken $-\\dfrac{1}{4}>-\\dfrac{1}{2}$: tersler alınınca sıralama ters döndü."),
        ]},
        {"baslik": "Negatif aralıklarda sıralama", "icerik": [
            "Klasik bir soru tipi, bir sayının belirli bir aralıkta olduğu bilindiğinde $x$, $x^2$, $x^3$ ve $\\dfrac{1}{x}$ gibi ifadelerin sıralanmasıdır. Negatif sayılarda iki aralık özellikle önemli:",
            tablo(["Aralık", "Sıralama"], [
                ["$-1<x<0$", "$\\dfrac{1}{x}<x<x^3<x^2$"],
                ["$x<-1$", "$x^3<x<\\dfrac{1}{x}<x^2$"],
            ]),
            "İki durumda da $x^2$ pozitif olduğu için en büyüktür; diğer üçü negatiftir. Farkı yaratan, $x$ in mutlak değerinin $1$ den küçük ya da büyük olmasıdır: mutlak değeri $1$ den küçük bir sayının kuvveti alındıkça mutlak değeri küçülür, $1$ den büyük bir sayınınki büyür.",
            ornek(
                "$x=-\\dfrac{1}{2}$ olsun.",
                "$x$, $x^2$, $x^3$ ve $\\dfrac{1}{x}$ i sıralayalım.",
                "Hesaplayalım: $x=-0.5$, $x^2=0.25$, $x^3=-0.125$, $\\dfrac{1}{x}=-2$.",
                "Küçükten büyüğe: $-2<-0.5<-0.125<0.25$.",
                "Yani $\\dfrac{1}{x}<x<x^3<x^2$; tablodaki birinci satırla aynı."),
            ornek(
                "$x=-2$ olsun.",
                "Aynı ifadeleri sıralayalım.",
                "Hesaplayalım: $x=-2$, $x^2=4$, $x^3=-8$, $\\dfrac{1}{x}=-0.5$.",
                "Küçükten büyüğe: $-8<-2<-0.5<4$.",
                "Yani $x^3<x<\\dfrac{1}{x}<x^2$; tablodaki ikinci satırla aynı."),
            dikkat(
                "Sıralama sorularında tek bir sayı denemek tabloyu hatırlamanın iyi bir yoludur, ama aralığın içinden bir sayı seçmeye dikkat et.",
                "$-1$ gibi sınır değerler eşitlik üretir: $x=-1$ için $x=x^3=\\dfrac{1}{x}=-1$ olur ve sıralama bozulur."),
        ]},
        {"baslik": "Mutlak değerle bağlantı", "icerik": [
            "Negatif sayılarla çalışırken \"sayının büyüklüğü\" ile \"sayının kendisi\" karıştırılabilir. $-9$ ile $-2$ den büyük olan $-2$ dir, ama $-9$ sıfırdan daha uzaktadır. Sıfıra olan bu uzaklığa <strong>mutlak değer</strong> denir ve işaretten bağımsız olarak büyüklüğü ölçer: $|-9|=9$, $|-2|=2$.",
            "Sayı doğrusunda iki sayı arasındaki uzaklık da mutlak değerle bulunur: $-9$ ile $-2$ arasındaki uzaklık $|-2-(-9)|=|7|=7$ birimdir. İki sıcaklık ya da iki yükseklik arasındaki farkı işaretten bağımsız ölçmenin temeli bu fikirdir.",
            "İki negatif sayıdan mutlak değeri büyük olanın daha küçük olmasının sebebi budur. Mutlak değerin ayrıntılı anlatımı için <a href=\"/blog/mutlak-deger-konu-anlatimi-pdf/\">Mutlak Değer Konu Anlatımı PDF</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sınavda pozitif ve negatif sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu işaret problemleri, negatif tabanlı kuvvetler, işlem önceliği ve aralıklara göre sıralama biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde işaret bilgisi bir problemin içinde de karşına çıkabilir: sıcaklık farkı, borç-alacak hesabı ya da bir ifadenin kesinlikle pozitif olup olmadığı gibi."),
            ornek(
                "Bir şehirde beş günün en düşük sıcaklıkları $-4$, $-1$, $2$, $0$ ve $-7$ derece olsun.",
                "Bu beş günün ortalama en düşük sıcaklığını bulalım.",
                "Önce toplayalım: pozitifler $2$, negatifler $-4-1-7=-12$; sıfır toplamı değiştirmez.",
                "Toplam: $2+(-12)=-10$.",
                "Ortalama, toplamın gün sayısına bölümüdür: $(-10):5=-2$ derece."),
            "İşaret sorularında en güvenli yol, her adımda işareti ayrı yazmaktır. Sonucu kontrol etmek için verilen koşullara uyan küçük sayılar seçip ifadeyi hesaplamak da hızlı bir doğrulama sağlar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$0$ ı pozitif saymak", "$0$ işaretsizdir"],
                ["$-2^4=16$ yazmak", "$-2^4=-16$"],
                ["Negatifle çarpınca yönü korumak", "Yön değişir"],
                ["$-2x>4$ ten $x>-2$ bulmak", "$x<-2$"],
                ["$-9>-2$ sanmak", "$-9<-2$"],
                ["Toplamın işaretini hep belirlenebilir sanmak", "Mutlak değere bağlı"],
                ["Sınır değerle sıralama denemek", "Aralığın içinden sayı seç"],
            ]),
            "Bu hataların ortak noktası eksi işaretinin nereye ait olduğunu karıştırmaktır. Eksi bir sayının parçası mı, bir işlem mi, yoksa bir kuvvetin dışında mı? Her adımda bunu açıkça yazmak hataların çoğunu önler.",
        ]},
    ],
    "sss": [
        ("Sıfır pozitif mi negatif mi?",
         "Sıfır ne pozitif ne negatiftir. Sayı doğrusunda pozitif ve negatif sayıları ayıran noktadır."),
        ("Eksi ile eksinin çarpımı neden artıdır?",
         "Bir sayıyı negatif bir sayıyla çarpmak, onu sıfıra göre ters yöne çevirmek demektir. Negatif bir sayı ters yöne çevrilince pozitif olur."),
        ("Kesirde eksi işareti nereye yazılır?",
         "Paya, paydaya ya da kesrin önüne yazılabilir; üçü de aynı sayıyı gösterir. Pay ve payda ikisi birden negatifse kesir pozitiftir."),
        ("Negatif bir sayının kuvveti ne zaman pozitif olur?",
         "Üs çift olduğunda. Negatif bir sayının çift kuvveti pozitif, tek kuvveti negatiftir."),
        ("İki negatif sayıdan hangisi büyüktür?",
         "Sıfıra daha yakın olan, yani mutlak değeri küçük olan büyüktür. Örneğin eksi 2, eksi 9 dan büyüktür."),
        ("Eşitsizlikte negatif sayıyla çarpınca ne olur?",
         "Eşitsizliğin yönü değişir. Örneğin 2 küçüktür 5 doğruysa, iki taraf eksi 1 ile çarpılınca eksi 2 büyüktür eksi 5 olur."),
        ("Eksi 1 ile 0 arasındaki bir sayının karesi neden kendisinden büyüktür?",
         "Çünkü negatif sayının karesi pozitiftir ve her pozitif sayı her negatif sayıdan büyüktür."),
    ],
    "kontrol": [
        "Pozitif, negatif ve sıfırı sayı doğrusu üzerinde açıklayabiliyorum.",
        "Günlük hayattan negatif sayı kullanılan örnekler verebiliyorum.",
        "Uzun bir toplamda pozitifleri ve negatifleri ayrı toplayarak sonuca ulaşabiliyorum.",
        "Çok çarpanlı bir çarpımın işaretini negatif çarpanları sayarak bulabiliyorum.",
        "$(-2)^4$ ile $-2^4$ ün farkını açıklayabiliyorum.",
        "Yalnızca işaretleri verilen sayılarla bir ifadenin işaretini bulabiliyorum.",
        "Verilen işaret bilgilerinden sayıların işaretini çıkarabiliyorum.",
        "Eşitsizliği negatif sayıyla çarparken yönü çevirmeyi unutmuyorum.",
        "$-1<x<0$ ve $x<-1$ aralıklarında $x$, $x^2$, $x^3$ ve $\\dfrac{1}{x}$ i sıralayabiliyorum.",
        "İki negatif sayıyı ve terslerini doğru karşılaştırabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["tek-ve-cift-sayilar", "sayi-dogrusu-ve-sayilari-siralama", "mutlak-deger-konu-anlatimi-pdf"],
}
