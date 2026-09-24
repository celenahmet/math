# scripts/yazilar/68_kesir_siralama.py — Kesirlerde Siralama ve Karsilastirma (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kesirlerde-siralama-ve-karsilastirma",
    "baslik": "Kesirlerde Sıralama ve Karşılaştırma",
    "aciklama": "Kesirler nasıl sıralanır? Ortak payda, ortak pay, çapraz çarpım, yarım ve bire göre karşılaştırma, iki kesir arasına kesir yerleştirme; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kesirlerde-siralama-ve-karsilastirma",
    "kapak_alt": "Kesirlerde sıralama ve karşılaştırma: farklı uzunluktaki blokları küçükten büyüğe dizen öğrenci",
    "ozet": "İki kesirden hangisinin büyük olduğunu söylemek, tam sayılardaki kadar kolay değildir: sekizde beş mi büyük, on birde yedi mi? Bu yazıda kesirleri karşılaştırmanın yedi yolunu, hangi durumda hangisinin en kısa olduğunu, negatif kesirlerde sıranın nasıl döndüğünü, pay ve paydaya aynı sayı eklenince kesrin nasıl değiştiğini ve iki kesrin arasına yeni bir kesir yerleştirmeyi çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kesirleri karşılaştırmak neden zordur?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesir kavramını, denk kesirleri ve EKOK'u biliyor olman yeterli.",
                "Kesirlerin temeli için <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a> yazısına göz at."),
            "Bir kesrin büyüklüğü iki sayıya birden bağlıdır: pay büyüdükçe kesir büyür, payda büyüdükçe kesir küçülür. İki kesrin hem payı hem paydası farklıysa bu iki etki birbirine karışır ve sadece sayılara bakarak karar vermek zorlaşır. Bu yüzden karşılaştırmanın özü, iki kesri <strong>ortak bir dile</strong> getirmektir: ya aynı paydaya, ya aynı paya, ya da ortak bir referansa.",
            dikkat(
                "Tek bir sayıya bakarak karar veren kısa yollar yanıltır.",
                "\"Payı büyük olan büyüktür\" kuralı yanlıştır: $3>2$ ama $\\dfrac{3}{10}<\\dfrac{2}{3}$ dir.",
                "\"Paydası küçük olan büyüktür\" kuralı da tek başına yanlıştır: $3<4$ ama $\\dfrac{1}{3}<\\dfrac{3}{4}$ tür."),
            "Aşağıdaki yöntemlerde aksi söylenmedikçe kesirler pozitiftir. Negatif kesirler ayrı bir bölümde ele alınıyor.",
        ]},
        {"baslik": "Paydalar eşitse ya da paylar eşitse", "icerik": [
            "<strong>Paydalar eşitse</strong> payı büyük olan kesir büyüktür. Bütün aynı sayıda eş parçaya bölünmüştür; daha çok parça alan daha büyük pay alır: $\\dfrac{5}{9}>\\dfrac{4}{9}$.",
            "<strong>Paylar eşitse</strong> paydası küçük olan kesir büyüktür. Aynı sayıda parça alınmıştır ama parçaların büyüklüğü paydaya bağlıdır; bütünü az parçaya bölmek büyük parça verir: $\\dfrac{4}{7}>\\dfrac{4}{9}$.",
            hap("Paydalar eşitse payı büyük olan, paylar eşitse paydası küçük olan kesir büyüktür.",
                "Bu iki kural pozitif kesirler içindir."),
        ]},
        {"baslik": "Ortak paydaya getirme", "icerik": [
            "Paydalar farklıysa kesirler genişletilerek aynı paydaya getirilir. Ortak payda olarak paydaların EKOK'u seçilirse sayılar olabildiğince küçük kalır. Paydalar eşitlenince paylar karşılaştırılır.",
            ornek(
                "$\\dfrac{5}{6}$, $\\dfrac{7}{9}$ ve $\\dfrac{11}{12}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Paydaların EKOK'u: $\\text{EKOK}(6, 9, 12)=36$.",
                "Genişletelim: $\\dfrac{30}{36}$, $\\dfrac{28}{36}$, $\\dfrac{33}{36}$.",
                "Payları karşılaştıralım: $28<30<33$.",
                "Sıralama: $\\dfrac{7}{9}<\\dfrac{5}{6}<\\dfrac{11}{12}$."),
            "EKOK'un nasıl bulunduğu için <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Ortak paya getirme", "icerik": [
            "Paylar küçük, paydalar büyükse paylar eşitlenir. Bu yöntem, paydaların EKOK'u çok büyük çıktığında işi hızlandırır.",
            ornek(
                "$\\dfrac{4}{9}$, $\\dfrac{6}{13}$ ve $\\dfrac{12}{25}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Payların EKOK'u $12$. Genişletelim: $\\dfrac{4}{9}=\\dfrac{12}{27}$ ve $\\dfrac{6}{13}=\\dfrac{12}{26}$; üçüncüsü zaten $\\dfrac{12}{25}$.",
                "Paylar eşit; paydası küçük olan büyüktür: $25<26<27$.",
                "Sıralama: $\\dfrac{4}{9}<\\dfrac{6}{13}<\\dfrac{12}{25}$."),
            "Aynı soruyu ortak paydayla çözmek için $9$, $13$ ve $25$ in EKOK'u olan $2925$ i kullanmak gerekirdi. Ortak pay yöntemi burada çok daha kısadır ve büyük sayılarla uğraşmayı gerektirmez.",
        ]},
        {"baslik": "Çapraz çarpım", "icerik": [
            "İki kesri karşılaştırmanın en hızlı yolu çapraz çarpımdır. $b$ ve $d$ pozitifken:",
            "$$\\dfrac{a}{b}<\\dfrac{c}{d} \\text{ ancak ve ancak } a \\cdot d<b \\cdot c$$",
            "Neden işe yaradığını görmek için iki kesri $b \\cdot d$ paydasına getirmek yeter: $\\dfrac{a \\cdot d}{b \\cdot d}$ ile $\\dfrac{b \\cdot c}{b \\cdot d}$. Paydalar eşit olduğu için yalnızca paylar karşılaştırılır.",
            ornek(
                "$\\dfrac{5}{8}$ ile $\\dfrac{7}{11}$ verilsin.",
                "Hangisinin büyük olduğunu bulalım.",
                "Çapraz çarpımlar: $5 \\cdot 11=55$ ve $8 \\cdot 7=56$.",
                "$55<56$ olduğu için $\\dfrac{5}{8}<\\dfrac{7}{11}$."),
            dikkat(
                "Çapraz çarpım paydaların pozitif olmasını gerektirir.",
                "Paydalardan biri negatifse eşitsizliğin yönü değişebilir. Bu yüzden önce eksi işaretini kesrin önüne ya da paya taşı, paydaları pozitif yap."),
        ]},
        {"baslik": "Referans kesirle karşılaştırma", "icerik": [
            "Bazen iki kesri doğrudan karşılaştırmak yerine ikisini de tanıdık bir sayıyla, örneğin $\\dfrac{1}{2}$ ya da $1$ ile karşılaştırmak yeter. Biri referansın altında, diğeri üstündeyse sıralama hesapsız ortaya çıkar. Bu, seçenekli sorularda zaman kazandıran bir ilk kontroldür.",
            "<h3>Yarımla karşılaştırma</h3>",
            "Bir kesrin payının iki katı paydadan küçükse kesir $\\dfrac{1}{2}$ den küçüktür, büyükse $\\dfrac{1}{2}$ den büyüktür.",
            ornek(
                "$\\dfrac{5}{11}$ ile $\\dfrac{7}{12}$ verilsin.",
                "Hangisinin büyük olduğunu bulalım.",
                "$\\dfrac{5}{11}$: $2 \\cdot 5=10<11$, yani yarımdan küçük.",
                "$\\dfrac{7}{12}$: $2 \\cdot 7=14>12$, yani yarımdan büyük.",
                "Sonuç: $\\dfrac{5}{11}<\\dfrac{1}{2}<\\dfrac{7}{12}$."),
            "<h3>Bire olan uzaklık</h3>",
            "Pay ile payda arasındaki fark aynı olan kesirlerde kesirlerin $1$ e uzaklığına bakılır.",
            ornek(
                "$\\dfrac{2024}{2025}$ ile $\\dfrac{2025}{2026}$ verilsin.",
                "Hangisinin büyük olduğunu bulalım.",
                "$\\dfrac{2024}{2025}=1-\\dfrac{1}{2025}$ ve $\\dfrac{2025}{2026}=1-\\dfrac{1}{2026}$.",
                "$\\dfrac{1}{2026}<\\dfrac{1}{2025}$ olduğu için $1$ den daha az çıkarılan büyüktür.",
                "Sonuç: $\\dfrac{2024}{2025}<\\dfrac{2025}{2026}$."),
            ornek(
                "$\\dfrac{9}{7}$ ile $\\dfrac{13}{11}$ verilsin.",
                "Hangisinin büyük olduğunu bulalım.",
                "İkisi de $1$ den büyük: $\\dfrac{9}{7}=1+\\dfrac{2}{7}$ ve $\\dfrac{13}{11}=1+\\dfrac{2}{11}$.",
                "$\\dfrac{2}{7}>\\dfrac{2}{11}$ olduğu için $\\dfrac{9}{7}>\\dfrac{13}{11}$."),
        ]},
        {"baslik": "Pay ve paydaya aynı sayıyı eklemek", "icerik": [
            "Pozitif bir kesrin hem payına hem paydasına aynı pozitif sayı eklenirse kesir $1$ e yaklaşır:",
            "<ul><li>Kesir $1$ den küçükse <strong>büyür</strong>: $\\dfrac{3}{5}<\\dfrac{4}{6}<\\dfrac{5}{7}$.</li>"
            "<li>Kesir $1$ den büyükse <strong>küçülür</strong>: $\\dfrac{7}{5}>\\dfrac{8}{6}>\\dfrac{9}{7}$.</li>"
            "<li>Kesir $1$ e eşitse değişmez.</li></ul>",
            "Nedeni çapraz çarpımda görülür. $a$, $b$ ve $k$ pozitifken $\\dfrac{a}{b}$ ile $\\dfrac{a+k}{b+k}$ yı karşılaştıralım: $a \\cdot (b+k)=ab+ak$ ve $b \\cdot (a+k)=ab+bk$. Fark yalnızca $ak$ ile $bk$ arasındadır; $a<b$ ise $ak<bk$ olur ve yeni kesir büyüktür.",
            ornek(
                "$\\dfrac{3}{5}$, $\\dfrac{13}{15}$ ve $\\dfrac{23}{25}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Her kesir bir öncekinin payına ve paydasına $10$ eklenerek elde edilmiş.",
                "Kesirler $1$ den küçük olduğu için her adımda büyür.",
                "Sıralama: $\\dfrac{3}{5}<\\dfrac{13}{15}<\\dfrac{23}{25}$. Kontrol: $0.6$, yaklaşık $0.867$ ve $0.92$."),
        ]},
        {"baslik": "Ondalığa çevirme", "icerik": [
            "Kesirleri ondalık sayıya çevirmek her zaman işe yarayan ama bazen uzun süren bir yoldur. Paydalar $2$, $4$, $5$, $8$, $10$ gibi kolay sayılarsa ya da kesirler ondalık sayılarla birlikte sıralanacaksa en pratik yol budur.",
            ornek(
                "$\\dfrac{3}{8}$, $0.4$ ve $\\dfrac{7}{20}$ verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Ondalığa çevirelim: $\\dfrac{3}{8}=0.375$ ve $\\dfrac{7}{20}=0.35$.",
                "Karşılaştıralım: $0.35<0.375<0.4$.",
                "Sıralama: $\\dfrac{7}{20}<\\dfrac{3}{8}<0.4$."),
            dikkat(
                "Yakın kesirlerde yeterli basamak kullan.",
                "Ondalık değerler ilk iki basamakta aynı çıkıyorsa bir basamak daha hesapla ya da çapraz çarpıma geç. Yuvarlanmış değerler yanlış sıralamaya götürebilir."),
        ]},
        {"baslik": "Negatif kesirleri sıralama", "icerik": [
            "Negatif kesirlerde önce işaretler bir kenara bırakılıp kesirler pozitifmiş gibi sıralanır, sonra sıra ters çevrilir. Sayı doğrusunda sıfırdan uzak olan negatif sayı daha küçüktür.",
            ornek(
                "$-\\dfrac{3}{5}$, $-\\dfrac{2}{3}$ ve $-\\dfrac{5}{8}$ verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Mutlak değerleri ortak paydaya getirelim; $\\text{EKOK}(5, 3, 8)=120$: $\\dfrac{72}{120}$, $\\dfrac{80}{120}$, $\\dfrac{75}{120}$.",
                "Mutlak değerlerin sırası: $\\dfrac{3}{5}<\\dfrac{5}{8}<\\dfrac{2}{3}$.",
                "Negatiflerde sıra ters döner: $-\\dfrac{2}{3}<-\\dfrac{5}{8}<-\\dfrac{3}{5}$."),
            "Pozitif ve negatif kesirler birlikte verildiyse iş kolaydır: her negatif kesir, her pozitif kesirden küçüktür.",
        ]},
        {"baslik": "İki kesir arasına kesir yerleştirmek", "icerik": [
            "İki farklı kesir ne kadar yakın olursa olsun, aralarında her zaman başka bir kesir vardır. Bu yüzden iki kesir arasında sonsuz sayıda kesir bulunur. Arada kalan bir kesri bulmanın iki kolay yolu vardır.",
            "<h3>Genişleterek</h3>",
            ornek(
                "$\\dfrac{1}{3}$ ile $\\dfrac{1}{2}$ verilsin.",
                "Aralarında bir kesir bulalım.",
                "Ortak paydaya getirelim: $\\dfrac{2}{6}$ ve $\\dfrac{3}{6}$. Arada paydası $6$ olan bir kesir yok.",
                "Bir kez daha genişletelim: $\\dfrac{4}{12}$ ve $\\dfrac{6}{12}$.",
                "Arada $\\dfrac{5}{12}$ var: $\\dfrac{1}{3}<\\dfrac{5}{12}<\\dfrac{1}{2}$."),
            "<h3>Payları ve paydaları toplayarak</h3>",
            "Paydaları pozitif iki kesirde $\\dfrac{a}{b}<\\dfrac{c}{d}$ ise paylar ve paydalar ayrı ayrı toplanarak elde edilen $\\dfrac{a+c}{b+d}$ kesri her zaman ikisinin arasındadır. Örneğin $\\dfrac{1}{3}$ ile $\\dfrac{1}{2}$ arasında $\\dfrac{1+1}{3+2}=\\dfrac{2}{5}$ vardır.",
            dikkat(
                "Bu yöntem toplama işlemi değildir.",
                "$\\dfrac{2}{5}$, iki kesrin toplamı değil, aralarında kalan bir kesirdir. Kesirlerin toplamı $\\dfrac{1}{3}+\\dfrac{1}{2}=\\dfrac{5}{6}$ tir."),
        ]},
        {"baslik": "Sayı doğrusunda karşılaştırma", "icerik": [
            "Sayı doğrusu, iki kesrin hangisinin büyük olduğunu gözle görmenin yoludur. $0$ ile $1$ arası ortak paydanın gösterdiği sayıda eş parçaya bölünür ve her kesir kendi yerine konur; sağdaki kesir büyüktür.",
            ornek(
                "$\\dfrac{2}{3}$ ile $\\dfrac{3}{5}$ verilsin.",
                "Sayı doğrusunda yerlerini karşılaştıralım.",
                "Ortak payda $15$: $\\dfrac{2}{3}=\\dfrac{10}{15}$ ve $\\dfrac{3}{5}=\\dfrac{9}{15}$.",
                "$0$ ile $1$ arası $15$ eş parçaya bölünürse $\\dfrac{2}{3}$ onuncu, $\\dfrac{3}{5}$ dokuzuncu çizgidedir.",
                "$\\dfrac{2}{3}$ daha sağda olduğu için büyüktür. Aralarındaki uzaklık $\\dfrac{1}{15}$ dir."),
            "Sayı doğrusu ayrıca bir kesrin tersiyle ilişkisini de gösterir: $0$ ile $1$ arasındaki pozitif bir kesrin tersi her zaman $1$ den büyüktür. $\\dfrac{3}{5}<1$ iken $\\dfrac{5}{3}>1$ dir.",
        ]},
        {"baslik": "Kuvvet ve kök alınca sıra", "icerik": [
            "$0$ ile $1$ arasındaki bir kesrin karesi kendisinden küçük, karekökü ise kendisinden büyüktür. Bir kesir kendisiyle çarpıldığında, $1$ den küçük bir sayıyla çarpılmış olur ve küçülür.",
            ornek(
                "$x=\\dfrac{4}{9}$ olsun.",
                "$x^2$, $x$ ve $\\sqrt{x}$ i sıralayalım.",
                "$x^2=\\dfrac{16}{81}$ ve $\\sqrt{x}=\\dfrac{2}{3}$.",
                "Ortak paydayla karşılaştıralım: $\\dfrac{16}{81}$, $\\dfrac{36}{81}$, $\\dfrac{54}{81}$.",
                "Sıralama: $x^2<x<\\sqrt{x}$, yani $\\dfrac{16}{81}<\\dfrac{4}{9}<\\dfrac{2}{3}$."),
            "Kesir $1$ den büyükse sıra tersine döner: karesi büyür, karekökü küçülür. $\\dfrac{9}{4}$ için kare $\\dfrac{81}{16}$, karekök $\\dfrac{3}{2}$ tür ve $\\dfrac{3}{2}<\\dfrac{9}{4}<\\dfrac{81}{16}$ olur.",
        ]},
        {"baslik": "Beş kesri birden sıralamak", "icerik": [
            "Kesir sayısı arttıkça tek bir yöntemde ısrar etmek yerine yöntemleri birleştirmek işi kısaltır. Önce referans bir sayıyla kesirleri gruplara ayır, sonra her grubun içinde çapraz çarpım ya da ondalık değer kullan.",
            ornek(
                "$\\dfrac{3}{7}$, $\\dfrac{5}{12}$, $\\dfrac{4}{9}$, $\\dfrac{7}{15}$ ve $\\dfrac{2}{5}$ kesirleri verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Önce yarımla karşılaştıralım: her birinde payın iki katı paydadan küçük, yani hepsi yarımdan küçük. Referans burada ayırmıyor.",
                "Bu durumda ondalık değerlere geçelim: yaklaşık $0.429$, $0.417$, $0.444$, $0.467$ ve $0.4$.",
                "Sıralama: $\\dfrac{2}{5}<\\dfrac{5}{12}<\\dfrac{3}{7}<\\dfrac{4}{9}<\\dfrac{7}{15}$.",
                "Kontrol için komşu iki kesir çapraz çarpımla karşılaştırılabilir: $\\dfrac{3}{7}$ ile $\\dfrac{4}{9}$ için $27<28$."),
            dikkat(
                "Birbirine çok yakın kesirlerde ondalık değerleri üç basamakla hesapla.",
                "$\\dfrac{3}{7}$ ile $\\dfrac{5}{12}$ iki basamakta $0.43$ ve $0.42$ görünür; fark ancak dikkatli yuvarlamayla güvenilir olur. Emin olamadığında çapraz çarpıma dön."),
        ]},
        {"baslik": "Günlük hayatta karşılaştırma", "icerik": [
            "Kesirleri karşılaştırmak yalnızca bir sınav becerisi değildir. İki indirimden hangisinin daha avantajlı olduğu, iki sınıftan hangisinin daha başarılı olduğu gibi sorular aslında birer kesir karşılaştırmasıdır.",
            ornek(
                "Bir mağaza ürünlerde $\\dfrac{3}{8}$ indirim, başka bir mağaza yüzde $35$ indirim uyguluyor.",
                "Hangi indirim daha büyüktür?",
                "$\\dfrac{3}{8}=0.375$, yani yüzde $37.5$.",
                "Yüzde $37.5$, yüzde $35$ ten büyük olduğu için ilk mağazanın indirimi daha büyüktür."),
            ornek(
                "Bir sınavda A sınıfında $25$ öğrenciden $18$ i, B sınıfında $30$ öğrenciden $21$ i başarılı olsun.",
                "Hangi sınıfın başarı oranı daha yüksektir?",
                "Oranlar: $\\dfrac{18}{25}$ ve $\\dfrac{21}{30}$.",
                "Çapraz çarpım: $18 \\cdot 30=540$ ve $25 \\cdot 21=525$.",
                "$540>525$ olduğu için A sınıfının oranı daha yüksektir: yüzde $72$ ile yüzde $70$."),
            "Son örnekte başarılı öğrenci sayısı B sınıfında daha fazladır ($21>18$), ama oran A sınıfında daha yüksektir. Karşılaştırmada sayılar değil oranlar, yani kesirler esas alınır. Farklı büyüklükteki grupları karşılaştırırken bu ayrım, yanlış sonuca varmayı önler.",
        ]},
        {"baslik": "Harfli kesirleri karşılaştırmak", "icerik": [
            "Kesirlerin payında ya da paydasında harf olduğunda da aynı kurallar işler; yalnızca harfin pozitif olup olmadığına dikkat etmek gerekir.",
            ornek(
                "$x$ pozitif bir sayı olsun.",
                "$\\dfrac{x}{x+1}$ ile $\\dfrac{x+1}{x+2}$ i karşılaştıralım.",
                "İkinci kesir, birincinin payına ve paydasına $1$ eklenerek elde edilmiştir.",
                "Birinci kesir $1$ den küçüktür, çünkü pay paydadan küçüktür. Pay ve paydaya aynı pozitif sayı eklenince $1$ den küçük kesir büyür.",
                "Sonuç: $\\dfrac{x}{x+1}<\\dfrac{x+1}{x+2}$. Kontrol: $x=1$ için $\\dfrac{1}{2}<\\dfrac{2}{3}$."),
        ]},
        {"baslik": "Hangi yöntem ne zaman?", "icerik": [
            tablo(["Durum", "En kısa yol"], [
                ["Paydalar eşit", "Payları karşılaştır"],
                ["Paylar eşit", "Paydası küçük olan büyük"],
                ["Paylar küçük, paydalar büyük", "Ortak pay"],
                ["İki kesir", "Çapraz çarpım"],
                ["Pay ile payda farkı sabit", "Bire olan uzaklık"],
                ["Kesirler yarımın iki yanında", "Yarımla karşılaştır"],
                ["Ondalık sayılarla karışık", "Ondalığa çevir"],
            ]),
            "Birden fazla yöntem uygun olabilir; önemli olan hesabı en kısa tutan yolu seçmektir. Sonucu ikinci bir yöntemle kontrol etmek, sınavda yapılan sıralama hatalarını önler.",
        ]},
        {"baslik": "Sınavda kesirlerde sıralama", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu kesirleri, ondalık sayıları ve köklü sayıları birlikte sıralama ya da iki kesir arasındaki kesirleri bulma biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde sıralama bilgisi sayısal akıl yürütme sorularında, seçenekler arasından en büyük ya da en küçük değeri bulmak için de gerekebilir."),
            "Seçeneklerde kesirler, ondalık sayılar ve yüzdeler karışık verilmişse hepsini aynı biçime çevirmek ilk adımdır. Yüzdeyi paydası $100$ olan kesir, ondalık sayıyı da paydası $10$ un kuvveti olan kesir gibi düşünmek, farklı biçimleri tek bir dilde buluşturur.",
            "Sıralama sorusunda seçeneklere bakmadan önce kesirlerin yapısına bak: paylar mı ortak, paydalar mı, pay ile payda farkı mı sabit? Yapıyı fark etmek, bazen hiç hesap yapmadan sıralamayı gösterir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Paydası büyük olanı büyük sanmak", "$\\dfrac{4}{9}<\\dfrac{4}{7}$"],
                ["Negatiflerde sırayı çevirmemek", "$-\\dfrac{2}{3}<-\\dfrac{3}{5}$"],
                ["Paydası negatifken çapraz çarpım", "Önce paydayı pozitif yap"],
                ["Yuvarlanmış ondalıkla sıralamak", "Yeterli basamak kullan"],
                ["$\\dfrac{a+c}{b+d}$ yi toplam sanmak", "Arada kalan kesirdir"],
                ["Pay ve paydaya ekleme hep büyütür sanmak", "$1$ den büyükse küçülür"],
            ]),
            "Bu hataların ortak noktası, kesrin büyüklüğünün pay ile paydanın birlikte belirlediği bir oran olduğunu unutmaktır. Emin olmadığında iki kesri çapraz çarpımla karşılaştırmak her zaman güvenilir bir kontroldür.",
        ]},
    ],
    "sss": [
        ("Paydası büyük olan kesir büyük müdür?",
         "Hayır. Paylar eşitse paydası büyük olan kesir küçüktür, çünkü bütün daha çok parçaya bölünmüş ve her parça küçülmüştür."),
        ("Kesirler en hızlı nasıl karşılaştırılır?",
         "İki kesir için çapraz çarpım en hızlı yoldur. Paydalar pozitifken birinci kesrin payı ile ikincinin paydası, ikinci kesrin payı ile birincinin paydası çarpılıp karşılaştırılır."),
        ("Ortak pay yöntemi ne zaman kullanılır?",
         "Paylar küçük, paydalar büyük olduğunda. Payları eşitlemek, büyük paydaların EKOK'unu bulmaktan daha kısa sürer."),
        ("İndirimler kesirle nasıl karşılaştırılır?",
         "Kesir biçimindeki indirim ondalık sayıya ya da yüzdeye çevrilir. Örneğin sekizde üç indirim yüzde 37,5 eder ve yüzde 35 indirimden büyüktür."),
        ("Negatif kesirler nasıl sıralanır?",
         "Önce işaretler yokmuş gibi sıralanır, sonra sıra ters çevrilir. Sıfırdan uzak olan negatif kesir daha küçüktür."),
        ("İki kesrin eşit olduğu nasıl anlaşılır?",
         "Çapraz çarpımlar eşitse, paydalar pozitifken iki kesir eşittir. Örneğin dörtte üç ile sekizde altı için 3 çarpı 8 ile 4 çarpı 6 aynı sonucu verir."),
        ("İki kesir arasında kaç kesir vardır?",
         "Sonsuz sayıda. İki kesir genişletilerek ya da payları ve paydaları ayrı ayrı toplanarak aralarında her zaman yeni bir kesir bulunabilir."),
        ("Kesirleri ondalığa çevirmek her zaman işe yarar mı?",
         "Her zaman doğru sonuç verir ama bazen uzun sürer ve devirli ondalıklarda yuvarlama hatasına açıktır. Birbirine çok yakın kesirlerde çapraz çarpım daha güvenilirdir."),
        ("Pay ve paydaya aynı sayı eklenince kesir büyür mü?",
         "Pozitif bir kesirde kesir 1 den küçükse büyür, 1 den büyükse küçülür. Kesir her durumda 1 e yaklaşır."),
    ],
    "kontrol": [
        "Paydaları eşit ve payları eşit kesirleri hemen karşılaştırabiliyorum.",
        "Kesirleri EKOK ile ortak paydaya getirip sıralayabiliyorum.",
        "Paylar küçükken ortak pay yöntemini kullanabiliyorum.",
        "Çapraz çarpımın neden işe yaradığını açıklayabiliyorum.",
        "Kesirleri yarımla karşılaştırabiliyorum.",
        "Pay ile payda farkı sabit kesirleri bire uzaklıkla sıralayabiliyorum.",
        "Pay ve paydaya aynı sayı eklenince kesrin nasıl değiştiğini açıklayabiliyorum.",
        "Kesirleri ondalık sayılarla birlikte sıralayabiliyorum.",
        "Negatif kesirleri sıralarken sırayı ters çevirmeyi unutmuyorum.",
        "İki kesir arasına yeni bir kesir yerleştirebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kesirler-konu-anlatimi-pdf", "sayi-dogrusu-ve-sayilari-siralama", "ebob-ve-ekok-konu-anlatimi-pdf"],
}
