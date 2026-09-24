# scripts/yazilar/75_dogru_ters_oranti.py — Dogru Oranti ve Ters Oranti (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "dogru-oranti-ve-ters-oranti",
    "baslik": "Doğru Orantı ve Ters Orantı",
    "aciklama": "Doğru orantı ve ters orantı nedir, nasıl ayırt edilir? Orantı sabiti, grafikler, bileşik orantı, işçi ve hız soruları ve sık yanılgılar; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "dogru-oranti-ve-ters-oranti",
    "kapak_alt": "Doğru orantı ve ters orantı: artan çubuklar ve dişli çarklarla birlikte değişen büyüklükleri karşılaştıran öğrenci",
    "ozet": "Bazı büyüklükler birlikte artar: alınan kalem sayısı iki katına çıkınca ödenen para da iki katına çıkar. Bazıları ise biri artarken diğeri aynı oranda azalır: işçi sayısı iki katına çıkınca işin süresi yarıya iner. Bu yazıda doğru orantıyı ve ters orantıyı tanımlıyor, ikisini nasıl ayırt edeceğini, grafiklerini, sık yapılan yanılgıyı, birden fazla büyüklüğün birlikte değiştiği bileşik orantıyı ve işçi, hız ve fiyat problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Doğru orantı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için oran, orantı ve içler dışlar çarpımını biliyor olman yeterli.",
                "Oran ve orantının temeli için <a href=\"/blog/oran-ve-oranti-konu-anlatimi-pdf/\">Oran ve Orantı Konu Anlatımı PDF</a> yazısına göz at."),
            "İki büyüklükten biri kaç katına çıkınca diğeri de aynı kat kadar artıyorsa bu büyüklükler <strong>doğru orantılıdır</strong>. Doğru orantıda iki büyüklüğün <strong>oranı sabittir</strong>:",
            "$$\\dfrac{y}{x}=k \\text{ ya da } y=k \\cdot x$$",
            "Buradaki $k$ ya <strong>orantı sabiti</strong> denir. Örneğin tanesi $15$ lira olan kalemden $x$ tane alınırsa ödenen para $y=15x$ olur: kalem sayısı iki katına çıkınca para da iki katına çıkar ve $\\dfrac{y}{x}$ her zaman $15$ tir.",
            ornek(
                "$3$ kalem $45$ lira olsun.",
                "Aynı kalemden $7$ tanesi kaç liradır?",
                "Doğru orantı: $\\dfrac{45}{3}=\\dfrac{y}{7}$.",
                "İçler dışlar çarpımı: $3y=45 \\cdot 7=315$, yani $y=105$ lira."),
            hap("Doğru orantıda büyüklüklerin oranı sabittir: $y=k \\cdot x$.",
                "Biri kaç katına çıkarsa diğeri de o kadar katına çıkar."),
        ]},
        {"baslik": "Ters orantı nedir?", "icerik": [
            "İki büyüklükten biri kaç katına çıkınca diğeri aynı kat kadar azalıyorsa, yani o sayıya bölünüyorsa bu büyüklükler <strong>ters orantılıdır</strong>. Ters orantıda iki büyüklüğün <strong>çarpımı sabittir</strong>:",
            "$$x \\cdot y=k \\text{ ya da } y=\\dfrac{k}{x}$$",
            "Örneğin bir işi $6$ işçi $10$ günde bitiriyorsa işin tamamı $6 \\cdot 10=60$ işçi-gündür. İşçi sayısı iki katına çıkınca gün sayısı yarıya iner, ama çarpım hep $60$ kalır.",
            ornek(
                "Bir işi $6$ işçi $10$ günde bitirsin.",
                "Aynı işi aynı hızda çalışan $4$ işçi kaç günde bitirir?",
                "Ters orantı: işçi sayısı ile gün sayısının çarpımı sabit: $6 \\cdot 10=4 \\cdot y$.",
                "$4y=60$, yani $y=15$ gün."),
            ornek(
                "Bir yolu saatte $60$ kilometre hızla giden bir araç $3$ saatte alsın.",
                "Aynı yolu saatte $90$ kilometre hızla kaç saatte alır?",
                "Yol sabit olduğu için hız ile süre ters orantılıdır: $60 \\cdot 3=90 \\cdot t$.",
                "$90t=180$, yani $t=2$ saat."),
            hap("Ters orantıda büyüklüklerin çarpımı sabittir: $x \\cdot y=k$.",
                "Biri kaç katına çıkarsa diğeri o sayıya bölünür."),
        ]},
        {"baslik": "Nasıl ayırt edilir? Tablo testi", "icerik": [
            "İki büyüklüğün doğru mu ters mi orantılı olduğunu anlamanın en güvenilir yolu, birkaç değer çiftinde oranı ve çarpımı hesaplamaktır:",
            "<ul><li>Bütün çiftlerde $\\dfrac{y}{x}$ aynıysa <strong>doğru orantı</strong> vardır.</li>"
            "<li>Bütün çiftlerde $x \\cdot y$ aynıysa <strong>ters orantı</strong> vardır.</li>"
            "<li>İkisi de değişiyorsa büyüklükler <strong>orantılı değildir</strong>.</li></ul>",
            tablo(["$x$", "$y$", "$\\dfrac{y}{x}$", "$x \\cdot y$"], [
                ["$2$", "$12$", "$6$", "$24$"],
                ["$3$", "$8$", "$\\dfrac{8}{3}$", "$24$"],
                ["$4$", "$6$", "$\\dfrac{3}{2}$", "$24$"],
                ["$6$", "$4$", "$\\dfrac{2}{3}$", "$24$"],
            ]),
            "Tablodaki büyüklüklerde oran değişiyor ama çarpım hep $24$; bu yüzden $x$ ile $y$ ters orantılıdır ve $y=\\dfrac{24}{x}$ tür.",
        ]},
        {"baslik": "Önemli bir yanılgı: biri artarken diğeri azalıyor", "icerik": [
            "\"Biri artarken diğeri azalıyorsa ters orantılıdır\" düşüncesi yanlıştır. Ters orantı yalnızca azalmayı değil, <strong>aynı oranda</strong> azalmayı gerektirir; çarpım sabit kalmalıdır.",
            ornek(
                "Elinde $10$ lira olan bir öğrenci $x$ lira harcasın ve kalan para $y$ olsun: $y=10-x$.",
                "$x$ ile $y$ ters orantılı mıdır?",
                "Değerler: $x=2$ için $y=8$; $x=4$ için $y=6$; $x=5$ için $y=5$.",
                "Çarpımlar: $16$, $24$, $25$. Çarpım sabit değil.",
                "$x$ artarken $y$ azalıyor ama ters orantı yok. Bu ilişki orantılı değildir."),
            "Aynı yanılgı doğru orantıda da yapılır: \"biri artarken diğeri de artıyorsa doğru orantılıdır\" düşüncesi de yanlıştır. $y=2x+1$ ilişkisinde $x$ arttıkça $y$ artar, ama $x=1$ için oran $3$, $x=2$ için oran $\\dfrac{5}{2}$ tir; oran sabit değildir.",
            dikkat(
                "Orantıyı yön değil, oran ya da çarpım belirler.",
                "Birlikte artmak doğru orantı için yetmez, oran sabit olmalıdır. Biri artarken diğerinin azalması ters orantı için yetmez, çarpım sabit olmalıdır."),
        ]},
        {"baslik": "Grafikler", "icerik": [
            "Doğru orantının grafiği <strong>başlangıç noktasından geçen bir doğrudur</strong>: $y=k \\cdot x$ te $x=0$ için $y=0$ dır ve $x$ her birim arttığında $y$ hep aynı miktarda, $k$ kadar artar. Doğru, başlangıç noktasından geçmiyorsa ilişki doğrusal olabilir ama doğru orantı değildir; $y=2x+1$ gibi.",
            "Ters orantının grafiği ise eksenlere yaklaşan ama onlara hiç değmeyen bir eğridir; bu eğriye <strong>hiperbol</strong> denir. $x \\cdot y=k$ olduğu için $x$ büyüdükçe $y$ sıfıra yaklaşır ama sıfır olmaz; $x$ sıfıra yaklaştıkça $y$ çok büyür. $x=0$ için $y$ tanımsızdır.",
            hap("Doğru orantının grafiği başlangıç noktasından geçen doğrudur.",
                "Ters orantının grafiği eksenlere yaklaşan bir eğridir; eksenleri kesmez."),
        ]},
        {"baslik": "Bileşik orantı", "icerik": [
            "Bazı problemlerde üç ya da daha fazla büyüklük birlikte değişir. Bu durumda her büyüklüğün sonuçla ilişkisi ayrı ayrı belirlenir: sonuçla doğru orantılı olanlar kesrin payında, ters orantılı olanlar kesrin paydasında yer alır.",
            "İşçi problemlerinde yapılan iş, işçi sayısıyla ve çalışılan günle doğru orantılıdır. Bu yüzden $\\dfrac{\\text{iş}}{\\text{işçi} \\cdot \\text{gün}}$ oranı sabittir.",
            ornek(
                "$5$ işçi $8$ günde $4$ duvar örüyor.",
                "Aynı hızda çalışan $10$ işçi $6$ günde kaç duvar örer?",
                "Sabit oran: $\\dfrac{4}{5 \\cdot 8}=\\dfrac{x}{10 \\cdot 6}$.",
                "$\\dfrac{4}{40}=\\dfrac{x}{60}$, yani $x=6$ duvar."),
            ornek(
                "$a$, $b$ ile doğru, $c$ ile ters orantılı olsun. $b=4$ ve $c=2$ iken $a=6$.",
                "$b=10$ ve $c=5$ iken $a$ kaçtır?",
                "İlişki: $a=k \\cdot \\dfrac{b}{c}$. İlk değerlerle $6=k \\cdot \\dfrac{4}{2}$, yani $k=3$.",
                "Yeni değerlerle: $a=3 \\cdot \\dfrac{10}{5}=6$."),
            dikkat(
                "Her büyüklüğün yönünü ayrı ayrı belirle.",
                "Bileşik orantıda bir büyüklüğü yanlışlıkla doğru yerine ters orantılı almak sonucu büyük ölçüde değiştirir. Her büyüklük için \"diğerleri sabitken bu artarsa sonuç artar mı azalır mı?\" diye sor."),
        ]},
        {"baslik": "Günlük hayatta doğru ve ters orantı", "icerik": [
            "Günlük hayatta iki tür ilişkinin de birçok örneği vardır. Aşağıdaki tabloda bazı örnekler var; her birinde diğer koşulların sabit tutulduğu varsayılır:",
            tablo(["Büyüklükler", "İlişki"], [
                ["Alınan ürün sayısı ve ödenen para", "Doğru orantı"],
                ["Sabit hızla gidilen süre ve yol", "Doğru orantı"],
                ["İşçi sayısı ve işin bitme süresi", "Ters orantı"],
                ["Sabit bir yolda hız ve süre", "Ters orantı"],
                ["Pizzayı paylaşan kişi sayısı ve kişi başına dilim", "Ters orantı"],
            ]),
            ornek(
                "Bir araç $100$ kilometrede $6$ litre yakıt harcasın.",
                "Aynı koşullarda $350$ kilometrede kaç litre harcar?",
                "Yol ile yakıt doğru orantılıdır: $\\dfrac{6}{100}=\\dfrac{x}{350}$.",
                "$100x=2100$, yani $x=21$ litre."),
            ornek(
                "$12$ dilimlik bir pizza önce $4$, sonra $6$ kişi arasında eşit paylaştırılsın.",
                "Kişi başına düşen dilim nasıl değişir?",
                "Kişi sayısı ile kişi başına dilim ters orantılı; çarpım hep $12$.",
                "$4$ kişide $3$ dilim, $6$ kişide $2$ dilim düşer."),
        ]},
        {"baslik": "Birim yöntemi", "icerik": [
            "Doğru ve ters orantı problemlerini orantı kurmadan çözmenin bir yolu da önce <strong>bir birimlik</strong> değeri bulmaktır. Doğru orantıda bir birimin değeri bölerek, ters orantıda ise çarparak bulunur.",
            ornek(
                "$5$ kilogram elma $120$ lira olsun.",
                "$8$ kilogram elmanın fiyatını birim yöntemiyle bulalım.",
                "$1$ kilogram: $120:5=24$ lira.",
                "$8$ kilogram: $8 \\cdot 24=192$ lira."),
            ornek(
                "Bir işi $6$ işçi $10$ günde bitirsin.",
                "Aynı işi $4$ işçinin kaç günde bitireceğini birim yöntemiyle bulalım.",
                "$1$ işçi aynı işi tek başına $6 \\cdot 10=60$ günde bitirir.",
                "$4$ işçi: $60:4=15$ gün."),
            "Birim yöntemi orantının türünü anlamayı da kolaylaştırır. Bir işçi tek başına daha uzun sürede bitirir; bu yüzden işçi sayısı azalınca süre uzar. Bir kilogram ise daha az para eder; bu yüzden miktar azalınca fiyat da azalır.",
        ]},
        {"baslik": "İş ve havuz problemleri", "icerik": [
            "Bir işi tek başına $a$ saatte bitiren biri, bir saatte işin $\\dfrac{1}{a}$ kadarını yapar. Birlikte çalışanların bir saatte yaptıkları işler toplanır. Süre ile çalışma hızı ters orantılı olduğu için toplanan şey süreler değil, hızlardır.",
            ornek(
                "Bir havuzu $A$ musluğu tek başına $6$ saatte, $B$ musluğu tek başına $12$ saatte dolduruyor.",
                "İki musluk birlikte açılırsa havuzun kaç saatte dolacağını bulalım.",
                "Bir saatte $A$ havuzun $\\dfrac{1}{6}$ kadarını, $B$ ise $\\dfrac{1}{12}$ kadarını doldurur.",
                "Birlikte bir saatte: $\\dfrac{1}{6}+\\dfrac{1}{12}=\\dfrac{3}{12}=\\dfrac{1}{4}$.",
                "Havuz $4$ saatte dolar."),
            ornek(
                "Bir havuzu bir musluk $4$ saatte dolduruyor, dipteki bir tahliye musluğu ise dolu havuzu $6$ saatte boşaltıyor.",
                "İkisi birlikte açık kalırsa boş havuzun kaç saatte dolacağını bulalım.",
                "Bir saatte net dolan kısım: $\\dfrac{1}{4}-\\dfrac{1}{6}=\\dfrac{1}{12}$.",
                "Havuz $12$ saatte dolar."),
            dikkat(
                "Süreleri toplamak ya da ortalamasını almak.",
                "$6$ saat ile $12$ saati toplayıp $18$ saat bulmak ya da ortalamasını alıp $9$ saat demek yanlıştır. Birlikte çalışan iki musluk, tek başına en hızlı olanından bile daha kısa sürede doldurur."),
        ]},
        {"baslik": "İş sırasında değişen işçi sayısı", "icerik": [
            "İş devam ederken işçi sayısı değişirse işin tamamı <strong>işçi-gün</strong> olarak hesaplanır, yapılan kısım çıkarılır ve kalan iş yeni işçi sayısına bölünür.",
            ornek(
                "Bir işi $12$ işçi $20$ günde bitirecektir. $5$ gün çalıştıktan sonra $3$ işçi ayrılıyor.",
                "Kalan işin kaç günde biteceğini bulalım.",
                "İşin tamamı: $12 \\cdot 20=240$ işçi-gün.",
                "İlk $5$ günde yapılan iş $12 \\cdot 5=60$ işçi-gün; kalan iş $240-60=180$ işçi-gün.",
                "Kalan $9$ işçi: $180:9=20$ gün. İş toplam $5+20=25$ günde biter."),
            "Aynı soruyu orantıyla da düşünebiliriz: kalan işi $12$ işçi $15$ günde bitirecekti. İşçi sayısı $12$ den $9$ a inince süre $\\dfrac{12}{9}=\\dfrac{4}{3}$ katına çıkar: $15 \\cdot \\dfrac{4}{3}=20$ gün.",
        ]},
        {"baslik": "Dişli çarklar", "icerik": [
            "Birbirine geçmiş iki dişli çarkta, birinin ilerlettiği diş sayısı diğerinin ilerlettiği diş sayısına eşittir. Bu yüzden diş sayısı ile devir sayısı ters orantılıdır: iki çarkta diş sayısı ile devir sayısının çarpımı aynıdır.",
            ornek(
                "$40$ dişli bir çark $15$ devir yaparken ona geçmiş $24$ dişli bir çark dönüyor.",
                "İkinci çarkın kaç devir yaptığını bulalım.",
                "Çarpımlar eşit: $40 \\cdot 15=24 \\cdot y$.",
                "$24y=600$, yani $y=25$ devir."),
            ornek(
                "$30$ dişli $A$ çarkı $20$ dişli $B$ çarkına, $B$ çarkı da $60$ dişli $C$ çarkına geçmiş olsun. $A$ çarkı $4$ devir yapıyor.",
                "$B$ ve $C$ çarklarının devir sayılarını bulalım.",
                "$B$ çarkı: $30 \\cdot 4=20 \\cdot y$, yani $y=6$ devir.",
                "$C$ çarkı: $20 \\cdot 6=60 \\cdot z$, yani $z=2$ devir.",
                "Ortadaki çark sonucu değiştirmez: $A$ ile $C$ doğrudan karşılaştırılsa da $30 \\cdot 4=60 \\cdot 2$ olur."),
            "Dişi az olan çark daha çok döner. Bisiklette pedaldaki dişli ile arka tekerleğin dişlisi zincirle bağlıdır ve aynı kural geçerlidir: öndeki dişlinin dişi arkadakinden fazlaysa, pedal bir tur döndüğünde arka tekerlek birden fazla tur döner.",
        ]},
        {"baslik": "Hız, yol ve zaman", "icerik": [
            "Hareket problemlerinde üç büyüklük birbirine bağlıdır: yol, hız ile zamanın çarpımıdır. Bu üç büyüklükten biri sabit tutulunca kalan ikisi arasında bir orantı ortaya çıkar:",
            tablo(["Sabit olan", "İlişki", "Neden"], [
                ["Hız", "Yol ile zaman doğru orantılı", "Yolun zamana oranı hızdır"],
                ["Zaman", "Yol ile hız doğru orantılı", "Yolun hıza oranı zamandır"],
                ["Yol", "Hız ile zaman ters orantılı", "Hız ile zamanın çarpımı yoldur"],
            ]),
            ornek(
                "İki araç aynı anda yola çıkıp aynı süre boyunca, biri saatte $60$, diğeri saatte $90$ kilometre hızla gidiyor. Birinci araç bu sürede $120$ kilometre yol alıyor.",
                "İkinci aracın aldığı yolu bulalım.",
                "Zaman sabit olduğu için yol ile hız doğru orantılıdır: $\\dfrac{120}{60}=\\dfrac{x}{90}$.",
                "$60x=10800$, yani $x=180$ kilometre."),
            "Aynı araçlarla bu kez aynı yol gidilseydi ilişki ters orantıya dönerdi: hızlı olan araç daha kısa sürede varırdı. Soru hangi büyüklüğün sabit olduğunu söylemiyorsa, önce bunu metinden çıkarmak gerekir.",
        ]},
        {"baslik": "Sınavda doğru ve ters orantı", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu işçi, hız, fiyat ve bileşik orantı problemleri ile tablodan orantı türünü belirleme biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde orantı bilgisi grafik yorumlama ve sayısal akıl yürütme sorularında da gerekebilir."),
            "Bir problemde önce hangi büyüklüğün sabit tutulduğunu belirlemek gerekir. Yol sabitse hız ile süre ters, hız sabitse yol ile süre doğru orantılıdır. Sabit olan büyüklük değişince ilişki de değişir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Azalan her ilişkiyi ters orantı sanmak", "Çarpım sabit olmalı"],
                ["Artan her ilişkiyi doğru orantı sanmak", "Oran sabit olmalı"],
                ["$y=2x+1$ i doğru orantı sanmak", "Başlangıçtan geçmeli"],
                ["İşçi problemini doğru orantıyla kurmak", "İşçi ve süre ters orantılı"],
                ["Bileşik orantıda yönü karıştırmak", "Her büyüklüğü ayrı sına"],
                ["Sabit tutulanı belirlememek", "Önce neyin sabit olduğuna bak"],
            ]),
            "Bu hataların hepsi, orantının türünü yöne bakarak belirlemekten doğar. Birkaç değer çiftinde oranı ve çarpımı hesaplamak, hangi ilişkinin geçerli olduğunu kesin olarak gösterir.",
        ]},
    ],
    "sss": [
        ("Doğru orantı nedir?",
         "İki büyüklüğün oranının sabit olduğu ilişkidir. Biri kaç katına çıkarsa diğeri de o kadar katına çıkar."),
        ("Ters orantı nedir?",
         "İki büyüklüğün çarpımının sabit olduğu ilişkidir. Biri kaç katına çıkarsa diğeri o sayıya bölünür."),
        ("Biri artarken diğeri azalıyorsa ters orantı mıdır?",
         "Her zaman değil. Ters orantı için çarpımın sabit kalması gerekir. Örneğin harcanan para arttıkça kalan para azalır ama bu ilişki ters orantı değildir."),
        ("Doğru orantının grafiği nasıldır?",
         "Başlangıç noktasından geçen bir doğrudur. Başlangıç noktasından geçmeyen doğrular orantılı bir ilişki göstermez."),
        ("Bileşik orantı nasıl çözülür?",
         "Her büyüklüğün sonuçla ilişkisi ayrı ayrı belirlenir. Doğru orantılı büyüklükler kesrin payında, ters orantılı olanlar paydasında olacak biçimde sabit bir oran yazılır."),
        ("İşçi sayısı ile süre arasında nasıl bir ilişki vardır?",
         "Aynı hızda çalışan işçilerle aynı iş yapılıyorsa işçi sayısı ile süre ters orantılıdır; işçi sayısı ile gün sayısının çarpımı sabittir."),
        ("İki musluk birlikte bir havuzu kaç saatte doldurur?",
         "Her musluğun bir saatte doldurduğu kısımlar toplanır ve 1 bu toplama bölünür. Havuzu 6 ve 12 saatte dolduran iki musluk birlikte 4 saatte doldurur."),
        ("Dişli çarklarda devir sayısı nasıl bulunur?",
         "Birbirine geçen iki çarkta diş sayısı ile devir sayısının çarpımı eşittir. Bu yüzden dişi az olan çark daha çok devir yapar."),
        ("Hız ile süre her zaman ters orantılı mıdır?",
         "Hayır, yalnızca yol sabitken ters orantılıdır. Süre sabitse hız ile alınan yol doğru orantılıdır."),
    ],
    "kontrol": [
        "Doğru orantıyı sabit oranla tanımlayabiliyorum.",
        "Ters orantıyı sabit çarpımla tanımlayabiliyorum.",
        "Bir tablodan orantı türünü oran ve çarpım hesaplayarak belirleyebiliyorum.",
        "Azalan her ilişkinin ters orantı olmadığını bir örnekle gösterebiliyorum.",
        "Doğru orantının grafiğinin başlangıç noktasından geçtiğini biliyorum.",
        "Ters orantının grafiğinin eksenleri kesmediğini açıklayabiliyorum.",
        "Doğru orantı problemlerini içler dışlar çarpımıyla çözebiliyorum.",
        "İşçi ve hız problemlerini ters orantıyla çözebiliyorum.",
        "Bileşik orantıda her büyüklüğün yönünü belirleyebiliyorum.",
        "Bir problemde hangi büyüklüğün sabit tutulduğunu belirleyebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["oran-ve-oranti-konu-anlatimi-pdf", "yuzdeler-konu-anlatimi-pdf", "kesirlerde-carpma-ve-bolme"],
}
