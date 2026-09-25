# scripts/yazilar/59_sayi_dogrusu.py — Sayi Dogrusu ve Sayilari Siralama (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "sayi-dogrusu-ve-sayilari-siralama",
    "baslik": "Sayı Doğrusu ve Sayıları Sıralama",
    "aciklama": "Sayı doğrusu nedir? Uzaklık ve orta nokta, aralıklar, ondalık sayıları, kesirleri, köklü ve üslü sayıları sıralama yöntemleri; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "sayi-dogrusu-ve-sayilari-siralama",
    "kapak_alt": "Sayı doğrusu ve sayıları sıralama: ahşap ray üzerine soldan sağa büyüyen renkli toplar yerleştiren iki öğrenci",
    "ozet": "Sayıları karşılaştırmanın en sağlam yolu, onları bir doğru üzerinde görmektir. Sayı doğrusunda sağdaki sayı her zaman büyüktür; bu basit kural tam sayılardan kesirlere, köklü sayılardan üslü sayılara kadar her sıralama sorusunun temelidir. Bu yazıda sayı doğrusunu kuruyor, iki nokta arasındaki uzaklığı ve orta noktayı buluyor, aralıkları gösteriyor ve ondalık sayıları, kesirleri, köklü ve üslü sayıları sıralamanın yöntemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Sayı doğrusu nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için tam sayıları, kesirleri ve pozitif-negatif sayı kavramını biliyor olman yeterli.",
                "İşaret kuralları ve negatif sayılar için <a href=\"/blog/pozitif-ve-negatif-sayilar/\">Pozitif ve Negatif Sayılar</a> yazısına göz at."),
            "Sayı doğrusu, sayıları bir doğru üzerinde noktalarla gösterme yoludur. Kurmak için üç şey gerekir: <strong>başlangıç noktası</strong> olarak seçilen ve $0$ ile gösterilen bir nokta, <strong>birim uzunluk</strong> olarak seçilen sabit bir uzunluk ve bir <strong>yön</strong>. Genellikle sağ yön pozitif seçilir; $0$ ın sağında $1, 2, 3, \\ldots$ solunda $-1, -2, -3, \\ldots$ birer birim aralıkla dizilir.",
            "Sayı doğrusundaki her nokta tek bir gerçek sayıya, her gerçek sayı da tek bir noktaya karşılık gelir. Yalnızca tam sayılar değil, $\\dfrac{3}{4}$ gibi kesirler ve $\\sqrt{2}$ gibi irrasyonel sayılar da doğru üzerinde bir yer kaplar. Gerçek sayıların doğruyu boşluksuz doldurması hakkında <a href=\"/blog/irrasyonel-sayilar-ve-gercek-sayilar/\">İrrasyonel Sayılar ve Gerçek Sayılar</a> yazısına bakabilirsin.",
            hap("Sayı doğrusunda sağdaki sayı soldakinden her zaman büyüktür.",
                "Her gerçek sayı doğru üzerinde tek bir noktaya karşılık gelir."),
        ]},
        {"baslik": "Sayı doğrusuna sayı yerleştirmek", "icerik": [
            "Tam sayılar birim çizgilerin tam üzerindedir. Kesirleri yerleştirmek için birim aralık paydadaki sayı kadar eşit parçaya bölünür ve pay kadar parça sayılır.",
            ornek(
                "$\\dfrac{3}{4}$ ve $\\dfrac{7}{3}$ sayıları verilsin.",
                "Sayı doğrusunda yerlerini bulalım.",
                "$\\dfrac{3}{4}$: $0$ ile $1$ arası $4$ eşit parçaya bölünür; $0$ dan sağa $3$ parça sayılır.",
                "$\\dfrac{7}{3}=2+\\dfrac{1}{3}$: $2$ ile $3$ arası $3$ eşit parçaya bölünür; $2$ den sağa $1$ parça sayılır."),
            "Ondalık ve irrasyonel sayılar için önce hangi iki tam sayı arasında olduklarına bakılır. $-1.5$, $-2$ ile $-1$ in tam ortasındadır. $\\sqrt{2}$ ise yaklaşık $1.41$ olduğu için $1$ ile $2$ arasında, $1.5$ in biraz solundadır.",
            dikkat(
                "Negatif kesirleri yerleştirirken yön ters çalışır.",
                "$-\\dfrac{7}{3}=-2-\\dfrac{1}{3}$ dir: $-2$ den <strong>sola</strong> doğru $1$ parça sayılır. Sayı $-2$ ile $-3$ arasındadır, $-2$ ye daha yakındır."),
        ]},
        {"baslik": "İki nokta arasındaki uzaklık ve orta nokta", "icerik": [
            "Sayı doğrusunda $a$ ve $b$ noktaları arasındaki uzaklık, büyük sayıdan küçüğün çıkarılmasıyla bulunur. Hangisinin büyük olduğunu düşünmek istemiyorsan farkın mutlak değerini al: uzaklık $|a-b|$ dir. İki noktanın tam ortasındaki nokta ise iki sayının ortalamasıdır: $\\dfrac{a+b}{2}$.",
            ornek(
                "Sayı doğrusunda $A=-3$ ve $B=7$ noktaları verilsin.",
                "$A$ ile $B$ arasındaki uzaklığı ve orta noktayı bulalım.",
                "Uzaklık: $|7-(-3)|=|10|=10$ birim.",
                "Orta nokta: $\\dfrac{-3+7}{2}=\\dfrac{4}{2}=2$.",
                "Kontrol: $2$ nin $-3$ e uzaklığı $5$, $7$ ye uzaklığı da $5$ birimdir."),
            ornek(
                "Sayı doğrusunda $A=-4$ ve $B=8$ noktaları verilsin.",
                "$[AB]$ yi $A$ dan başlayarak $1:3$ oranında bölen noktayı bulalım.",
                "$|AB|=8-(-4)=12$ birim. $1:3$ oranı, uzunluğun $4$ eşit parçaya bölünmesi demektir.",
                "Bir parça $12:4=3$ birim; nokta $A$ dan $3$ birim sağdadır.",
                "Aranan nokta $-4+3=-1$. Kontrol: $A$ ya uzaklığı $3$, $B$ ye uzaklığı $9$; oran $1:3$."),
            ornek(
                "Sayı doğrusunda $5$ e uzaklığı $3$ birim olan noktalar sorulsun.",
                "Bu noktaları bulalım.",
                "$5$ ten sağa $3$ birim: $8$. $5$ ten sola $3$ birim: $2$.",
                "İki nokta vardır: $2$ ve $8$. Bu soru, $|x-5|=3$ denkleminin sayı doğrusundaki karşılığıdır."),
            hap("Sayı doğrusunda $a$ ile $b$ arasındaki uzaklık $|a-b|$, orta nokta $\\dfrac{a+b}{2}$ olur."),
        ]},
        {"baslik": "Aralıklar ve aralıktaki tam sayılar", "icerik": [
            "Sayı doğrusunda iki sayı arasındaki bölgeye <strong>aralık</strong> denir. Uç noktanın aralığa dahil olup olmadığı iki şekilde gösterilir: sayı doğrusunda dolu nokta dahil, boş nokta hariç demektir; yazıda ise köşeli parantez dahil, normal parantez hariç demektir.",
            tablo(["Eşitsizlik", "Aralık", "Uç noktalar"], [
                ["$a \\leq x \\leq b$", "$[a, b]$", "İkisi de dahil"],
                ["$a<x<b$", "$(a, b)$", "İkisi de hariç"],
                ["$a \\leq x<b$", "$[a, b)$", "Yalnız $a$ dahil"],
                ["$a<x \\leq b$", "$(a, b]$", "Yalnız $b$ dahil"],
            ]),
            "Bir ucu olmayan aralıklar da vardır. $x>2$ eşitsizliği, $2$ nin sağındaki bütün sayıları anlatır ve $(2, \\infty)$ biçiminde yazılır. $x \\leq -1$ ise $(-\\infty, -1]$ dir. Sonsuz bir sayı olmadığı ve hiçbir zaman ulaşılamadığı için sonsuz tarafında her zaman normal parantez kullanılır. İki aralığın ortak kısmını bulmak için ikisini aynı sayı doğrusu üzerinde çizmek yeter: $x \\geq -3$ ile $x<2$ nin ortak kısmı $[-3, 2)$ dir.",
            ornek(
                "$-3<x \\leq 4$ aralığı verilsin.",
                "Bu aralıkta kaç tam sayı vardır?",
                "$-3$ hariç, $4$ dahil. Tam sayılar: $-2, -1, 0, 1, 2, 3, 4$.",
                "Terim sayısı formülüyle: $4-(-2)+1=7$.",
                "Aralıkta $7$ tam sayı vardır."),
            ornek(
                "$-2.5 \\leq x<3.2$ aralığı verilsin.",
                "Bu aralıktaki tam sayıları bulalım.",
                "Uç noktalar tam sayı değil; bu yüzden dahil ya da hariç olmaları sonucu değiştirmez.",
                "$-2.5$ ten büyük en küçük tam sayı $-2$, $3.2$ den küçük en büyük tam sayı $3$.",
                "Tam sayılar $-2, -1, 0, 1, 2, 3$: toplam $6$ tane."),
        ]},
        {"baslik": "Tam sayıları ve ondalık sayıları sıralama", "icerik": [
            "Pozitif sayılarda büyüklük alışıldığı gibidir. Negatif sayılarda ise sıfırdan uzaklaştıkça sayı küçülür: $-9$, $-2$ den küçüktür çünkü sayı doğrusunda daha soldadır. Kısaca: iki negatif sayıdan mutlak değeri büyük olan daha küçüktür.",
            "Ondalık sayıları karşılaştırırken önce tam kısma, tam kısımlar eşitse ondalık basamaklara soldan sağa sırayla bakılır. Basamak sayıları farklıysa sona sıfır eklemek karşılaştırmayı kolaylaştırır; $0.3$ ile $0.300$ aynı sayıdır.",
            ornek(
                "$0.3$, $0.305$ ve $0.35$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Basamakları eşitleyelim: $0.300$, $0.305$, $0.350$.",
                "Onda birler basamağı hepsinde $3$; yüzde birler basamağında $0$, $0$, $5$; binde birler basamağında $0$ ile $5$.",
                "Sıralama: $0.3<0.305<0.35$."),
            ornek(
                "$-0.3$, $-0.305$ ve $-0.35$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Mutlak değerler bir önceki örnekteki sayılardır: $0.3<0.305<0.35$.",
                "Negatif sayılarda sıra ters döner.",
                "Sıralama: $-0.35<-0.305<-0.3$."),
            dikkat(
                "Basamak sayısı fazla olan ondalık sayı daha büyük değildir.",
                "$0.305$ in üç ondalık basamağı var, $0.35$ in iki; ama $0.35$ daha büyüktür. Karşılaştırma basamak sayısına göre değil, soldan başlayarak basamak değerlerine göre yapılır."),
            hap("Termometrede $-9$ derece, $-2$ dereceden daha soğuktur.", "İki negatif sayıdan mutlak değeri büyük olan daha küçüktür; sayı doğrusunda daha soldadır.", gunluk=True),
        ]},
        {"baslik": "Kesirleri sıralama", "icerik": [
            "Kesirleri sıralamanın tek bir yolu yoktur; sayılara bakıp en kısa yolu seçmek gerekir. Aşağıdaki yöntemler pozitif kesirler içindir:",
            "<ul><li><strong>Paydalar eşitse:</strong> payı büyük olan büyüktür. $\\dfrac{5}{9}>\\dfrac{4}{9}$.</li>"
            "<li><strong>Paylar eşitse:</strong> paydası küçük olan büyüktür. $\\dfrac{4}{7}>\\dfrac{4}{9}$; bir bütünü $7$ parçaya bölmek, $9$ parçaya bölmekten daha büyük parçalar verir.</li>"
            "<li><strong>Paydaları eşitlemek:</strong> kesirler ortak paydaya genişletilir, sonra paylar karşılaştırılır.</li>"
            "<li><strong>Ondalığa çevirmek:</strong> her kesir bölme işlemiyle ondalık sayıya çevrilir.</li>"
            "<li><strong>Çapraz çarpım:</strong> $b$ ve $d$ pozitifken $\\dfrac{a}{b}$ ile $\\dfrac{c}{d}$ yi karşılaştırmak için $a \\cdot d$ ile $b \\cdot c$ karşılaştırılır.</li></ul>",
            ornek(
                "$\\dfrac{3}{5}$, $\\dfrac{5}{8}$ ve $\\dfrac{7}{12}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Paydaların en küçük ortak katı $120$. Genişletelim: $\\dfrac{72}{120}$, $\\dfrac{75}{120}$, $\\dfrac{70}{120}$.",
                "Payları karşılaştıralım: $70<72<75$.",
                "Sıralama: $\\dfrac{7}{12}<\\dfrac{3}{5}<\\dfrac{5}{8}$. Ondalıkla kontrol: yaklaşık $0.583$, $0.6$ ve $0.625$."),
            ornek(
                "$\\dfrac{5}{8}$ ile $\\dfrac{7}{11}$ kesirleri verilsin.",
                "Hangisinin büyük olduğunu çapraz çarpımla bulalım.",
                "$5 \\cdot 11=55$ ve $8 \\cdot 7=56$.",
                "$55<56$ olduğu için $\\dfrac{5}{8}<\\dfrac{7}{11}$."),
            "<h3>Bire olan uzaklıkla sıralama</h3>",
            "Pay ile paydası arasındaki fark aynı olan kesirlerde en hızlı yol, kesirlerin $1$ e ne kadar uzak olduğuna bakmaktır.",
            ornek(
                "$\\dfrac{3}{4}$, $\\dfrac{5}{6}$ ve $\\dfrac{7}{8}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Her biri $1$ den biraz küçük: $1-\\dfrac{1}{4}$, $1-\\dfrac{1}{6}$, $1-\\dfrac{1}{8}$.",
                "$1$ den çıkarılan parça ne kadar küçükse kesir o kadar büyüktür: $\\dfrac{1}{8}<\\dfrac{1}{6}<\\dfrac{1}{4}$.",
                "Sıralama: $\\dfrac{3}{4}<\\dfrac{5}{6}<\\dfrac{7}{8}$."),
            ornek(
                "$\\dfrac{5}{4}$, $\\dfrac{7}{6}$ ve $\\dfrac{9}{8}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Her biri $1$ den biraz büyük: $1+\\dfrac{1}{4}$, $1+\\dfrac{1}{6}$, $1+\\dfrac{1}{8}$.",
                "Bu kez $1$ e eklenen parça büyük olan büyüktür.",
                "Sıralama: $\\dfrac{9}{8}<\\dfrac{7}{6}<\\dfrac{5}{4}$."),
            ornek(
                "$\\dfrac{2025}{2026}$ ile $\\dfrac{2026}{2027}$ kesirleri verilsin.",
                "Hangisi büyüktür?",
                "$\\dfrac{2025}{2026}=1-\\dfrac{1}{2026}$ ve $\\dfrac{2026}{2027}=1-\\dfrac{1}{2027}$.",
                "$\\dfrac{1}{2027}<\\dfrac{1}{2026}$ olduğu için $1$ den daha az çıkarılan büyüktür.",
                "$\\dfrac{2025}{2026}<\\dfrac{2026}{2027}$."),
            hap("Paylar eşitse paydası küçük olan, paydalar eşitse payı büyük olan kesir büyüktür (pozitif kesirlerde).",
                "Pay ile payda arasındaki fark sabitse kesirleri $1$ e olan uzaklıklarıyla karşılaştır."),
        ]},
        {"baslik": "Negatif kesirleri sıralama", "icerik": [
            "Negatif kesirlerde önce işaretleri yok sayıp pozitif kesirler gibi sıralarsın, sonra sırayı ters çevirirsin. Sayı doğrusunda sıfırdan uzak olan negatif sayı daha küçüktür.",
            ornek(
                "$-\\dfrac{2}{3}$ ile $-\\dfrac{3}{4}$ sayıları verilsin.",
                "Hangisi büyüktür?",
                "Mutlak değerleri karşılaştıralım: $\\dfrac{2}{3}=\\dfrac{8}{12}$ ve $\\dfrac{3}{4}=\\dfrac{9}{12}$; yani $\\dfrac{2}{3}<\\dfrac{3}{4}$.",
                "Negatiflerde sıra ters döner.",
                "$-\\dfrac{3}{4}<-\\dfrac{2}{3}$; büyük olan $-\\dfrac{2}{3}$ dir."),
        ]},
        {"baslik": "Köklü sayıları sıralama", "icerik": [
            "Köklü sayıları karşılaştırmanın en güvenilir yolu, hepsini tek bir kökün içine almaktır. Pozitif sayılarda kökün içi büyük olan sayı büyüktür. Kökün dışındaki bir katsayı, karesi alınarak içeri taşınır: $a\\sqrt{b}=\\sqrt{a^2 b}$.",
            ornek(
                "$2\\sqrt{3}$, $3\\sqrt{2}$, $4$ ve $\\sqrt{15}$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Hepsini tek kök içine alalım: $2\\sqrt{3}=\\sqrt{12}$, $3\\sqrt{2}=\\sqrt{18}$, $4=\\sqrt{16}$, $\\sqrt{15}$.",
                "Kök içlerini karşılaştıralım: $12<15<16<18$.",
                "Sıralama: $2\\sqrt{3}<\\sqrt{15}<4<3\\sqrt{2}$."),
            "Bir köklü sayının hangi iki tam sayı arasında olduğunu bulmak için kökün içine en yakın tam kareler aranır. $16<17<25$ olduğu için $4<\\sqrt{17}<5$; $49<50<64$ olduğu için $7<\\sqrt{50}<8$ dir. $\\sqrt{17}$, $16$ ya çok yakın olduğu için $4$ e yakındır.",
            dikkat(
                "Katsayı kök içine alınırken karesi alınır.",
                "$3\\sqrt{2}=\\sqrt{6}$ yazmak yanlıştır; doğrusu $3\\sqrt{2}=\\sqrt{9 \\cdot 2}=\\sqrt{18}$ dir."),
        ]},
        {"baslik": "Üslü sayıları sıralama", "icerik": [
            "Üslü sayıları karşılaştırmak için ya tabanları ya da üsleri eşitlemeye çalışılır. Tabanlar eşit ve $1$ den büyükse üssü büyük olan büyüktür. Üsler eşit ve tabanlar pozitifse tabanı büyük olan büyüktür.",
            ornek(
                "$4^5$, $8^3$ ve $16^2$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Tabanları $2$ ye çevirelim: $4^5=2^{10}$, $8^3=2^9$, $16^2=2^8$.",
                "Tabanlar eşit; üsleri karşılaştıralım: $8<9<10$.",
                "Sıralama: $16^2<8^3<4^5$."),
            ornek(
                "$2^{30}$, $3^{20}$ ve $5^{10}$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Tabanlar eşitlenemez, ama üslerin ortak böleni $10$: $2^{30}=(2^3)^{10}=8^{10}$ ve $3^{20}=(3^2)^{10}=9^{10}$.",
                "Üsler eşit; tabanları karşılaştıralım: $5<8<9$.",
                "Sıralama: $5^{10}<2^{30}<3^{20}$."),
            hap("Üslü sayıları sıralarken ya tabanları ya da üsleri eşitle.",
                "Köklü sayıları sıralarken hepsini tek bir kökün içine al."),
        ]},
        {"baslik": "Farklı türden sayıları sıralama", "icerik": [
            "Sınavda sıralanacak sayılar karışık da gelebilir: bir kesir, bir ondalık sayı ve bir köklü sayı aynı soruda yer alabilir. Bu durumda en pratik yol, hepsini aynı biçime, genellikle ondalık yaklaşık değere çevirmektir. Yaklaşık değerler birbirine çok yakın çıkarsa bir basamak daha hesaplanır.",
            ornek(
                "$-1.2$, $-\\dfrac{5}{4}$ ve $-\\sqrt{2}$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Ondalık değerler: $-\\dfrac{5}{4}=-1.25$ ve $-\\sqrt{2}$ yaklaşık $-1.41$.",
                "Mutlak değerler: $1.2<1.25<1.41$. Negatif sayılarda sıra ters döner.",
                "Sıralama: $-\\sqrt{2}<-\\dfrac{5}{4}<-1.2$."),
            ornek(
                "$3.14$, $\\pi$ ve $\\dfrac{22}{7}$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "$\\pi$ nin ilk basamakları $3.14159$, $\\dfrac{22}{7}$ nin ilk basamakları $3.14285$.",
                "İlk iki ondalık basamak üçünde de aynı; üçüncü basamakta $0$, $1$ ve $2$ var.",
                "Sıralama: $3.14<\\pi<\\dfrac{22}{7}$. Buradan $\\dfrac{22}{7}$ nin $\\pi$ ye çok yakın ama ondan biraz büyük bir kesir olduğu da görülür."),
            dikkat(
                "Yaklaşık değerle sıralarken yeterli basamak kullan.",
                "$\\pi$ ile $\\dfrac{22}{7}$ yi iki ondalık basamakla karşılaştırırsan ikisi de $3.14$ görünür ve eşit sanılır. Fark ancak üçüncü basamakta ortaya çıkar."),
        ]},
        {"baslik": "Harfle verilen sayıları sıralama", "icerik": [
            "Bazı sorularda sayının kendisi değil, bulunduğu aralık verilir. $0<x<1$ ise $x$ in kuvvetleri alındıkça sayı küçülür, kökü alındıkça büyür, tersi ise $1$ den büyüktür:",
            "$$x^2<x<\\sqrt{x}<\\dfrac{1}{x}$$",
            ornek(
                "$x=\\dfrac{1}{4}$ olsun.",
                "$x^2$, $x$, $\\sqrt{x}$ ve $\\dfrac{1}{x}$ i sıralayalım.",
                "Hesaplayalım: $x^2=\\dfrac{1}{16}$, $x=\\dfrac{1}{4}$, $\\sqrt{x}=\\dfrac{1}{2}$, $\\dfrac{1}{x}=4$.",
                "Ondalıkla: $0.0625<0.25<0.5<4$.",
                "Yani $x^2<x<\\sqrt{x}<\\dfrac{1}{x}$."),
            "Negatif aralıklardaki sıralama tabloları için <a href=\"/blog/pozitif-ve-negatif-sayilar/\">Pozitif ve Negatif Sayılar</a> yazısındaki sıralama bölümüne bakabilirsin.",
        ]},
        {"baslik": "Sınavda sayı doğrusu ve sıralama", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu kesir, köklü ve üslü sayıları sıralama, aralıktaki tam sayıları sayma ve sayı doğrusunda uzaklık biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde sıralama bilgisi sayısal akıl yürütme sorularının içinde de karşına çıkabilir: verilen seçeneklerden en büyüğünü ya da en küçüğünü bulma gibi."),
            "Sıralama sorularında her sayıyı aynı biçime getirmek işin yarısıdır: kesirleri ortak paydaya, köklüleri tek köke, üslüleri ortak tabana ya da ortak üsse. Sayılar aynı dili konuştuğunda karşılaştırma kendiliğinden ortaya çıkar. Seçeneklerde birbirine çok yakın değerler varsa yaklaşık değer yerine kesin bir yöntemi, yani ortak paydayı, çapraz çarpımı ya da tek kök yöntemini tercih et.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$-9>-2$ sanmak", "$-9<-2$"],
                ["Basamağı çok olan ondalığı büyük sanmak", "$0.305<0.35$"],
                ["Paydası büyük kesri büyük sanmak", "$\\dfrac{4}{9}<\\dfrac{4}{7}$"],
                ["$3\\sqrt{2}=\\sqrt{6}$ yazmak", "$3\\sqrt{2}=\\sqrt{18}$"],
                ["Negatif kesirde sırayı çevirmemek", "$-\\dfrac{3}{4}<-\\dfrac{2}{3}$"],
                ["Aralıkta uç noktayı yanlış saymak", "Dolu nokta dahil, boş nokta hariç"],
            ]),
            "Bu hataların ortak noktası, sayıyı sayı doğrusunda hayal etmeden karşılaştırmaktır. Emin olamadığında iki sayıyı doğru üzerine yerleştir: sağda olan büyüktür.",
        ]},
    ],
    "sss": [
        ("Sayı doğrusu nedir?",
         "Başlangıç noktası, birim uzunluğu ve yönü seçilmiş bir doğrudur. Her gerçek sayı bu doğru üzerinde tek bir noktaya karşılık gelir."),
        ("Sayı doğrusunda iki nokta arasındaki uzaklık nasıl bulunur?",
         "Büyük sayıdan küçük sayı çıkarılır. Hangisinin büyük olduğu bilinmiyorsa farkın mutlak değeri alınır."),
        ("Kesirler nasıl sıralanır?",
         "Paydalar eşitlenip paylar karşılaştırılabilir, kesirler ondalığa çevrilebilir ya da iki kesir çapraz çarpımla karşılaştırılabilir. Paylar eşitse paydası küçük olan büyüktür."),
        ("Negatif sayılarda hangisi büyüktür?",
         "Sıfıra daha yakın olan, yani mutlak değeri küçük olan büyüktür. Örneğin eksi 2, eksi 9 dan büyüktür."),
        ("Köklü sayılar nasıl karşılaştırılır?",
         "Katsayılar karesi alınarak kökün içine taşınır ve kök içleri karşılaştırılır. Kök içi büyük olan sayı büyüktür."),
        ("Aralıkta köşeli parantez ne demektir?",
         "Uç noktanın aralığa dahil olduğunu gösterir. Normal parantez ise uç noktanın hariç olduğunu gösterir."),
    ],
    "kontrol": [
        "Sayı doğrusunu başlangıç noktası, birim ve yönle kurabiliyorum.",
        "Kesirleri ve negatif kesirleri sayı doğrusuna yerleştirebiliyorum.",
        "İki nokta arasındaki uzaklığı ve orta noktayı bulabiliyorum.",
        "Bir doğru parçasını verilen oranda bölen noktayı bulabiliyorum.",
        "Aralık gösterimini okuyup aralıktaki tam sayıları sayabiliyorum.",
        "Ondalık sayıları basamak basamak karşılaştırabiliyorum.",
        "Kesirleri en uygun yöntemi seçerek sıralayabiliyorum.",
        "Negatif kesirleri sıralarken sırayı ters çevirmeyi unutmuyorum.",
        "Köklü sayıları tek kök içine alarak sıralayabiliyorum.",
        "Üslü sayıları ortak taban ya da ortak üsse getirerek sıralayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["pozitif-ve-negatif-sayilar", "mutlak-deger-konu-anlatimi-pdf", "ardisik-sayilar"],
}
