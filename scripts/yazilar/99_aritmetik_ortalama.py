# scripts/yazilar/99_aritmetik_ortalama.py — Aritmetik Ortalama ve Veri Analizi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, sutun_grafik  # noqa: E402

YAZI = {
    "slug": "aritmetik-ortalama-ve-veri-analizi",
    "baslik": "Aritmetik Ortalama ve Veri Analizi",
    "aciklama": "Aritmetik ortalama nasıl bulunur? Ortalama problemleri, ağırlıklı ortalama, ortanca, tepe değer, açıklık, çeyrekler açıklığı ve standart sapma; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "veri",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "aritmetik-ortalama-ve-veri-analizi",
    "kapak_alt": "Aritmetik ortalama ve veri analizi: farklı yükseklikteki halka sütunlarını eşitleyerek ortalamayı gösteren iki öğrenci",
    "ozet": "Aritmetik ortalama, bir veri grubunu tek bir sayıyla özetlemenin en bilinen yoludur. Ama tek başına yeterli değildir: aynı ortalamaya sahip iki grup çok farklı dağılabilir ve tek bir uç değer ortalamayı olduğundan farklı gösterebilir. Bu yazıda aritmetik ortalamayı ve ortalama problemlerini, ağırlıklı ortalamayı, ortanca ve tepe değeri, açıklığı, çeyrekler açıklığını ve standart sapmayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Aritmetik ortalama nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi ve tablo okumayı biliyor olman yeterli.",
                "Tablo ve grafik okumak için <a href=\"/blog/tablo-ve-grafik-yorumlama/\">Tablo ve Grafik Yorumlama</a> yazısına göz at."),
            "Bir veri grubundaki bütün değerlerin toplamının değer sayısına bölümüne <strong>aritmetik ortalama</strong> denir. Günlük dilde \"ortalama\" denildiğinde çoğu zaman bu kastedilir.",
            "$$\\text{Aritmetik ortalama}=\\dfrac{\\text{değerlerin toplamı}}{\\text{değer sayısı}}$$",
            ornek(
                "Bir öğrencinin beş sınavdan aldığı puanlar $7$, $9$, $10$, $12$ ve $12$ olsun.",
                "Puanların aritmetik ortalamasını bulalım.",
                "Toplam: $7+9+10+12+12=50$.",
                "Ortalama: $50:5=10$."),
            hap("Ortalama = toplam bölü değer sayısı.",
                "Toplam = ortalama çarpı değer sayısı."),
        ]},
        {"baslik": "Ortalama bir eşitlemedir", "icerik": [
            "Aritmetik ortalama, bütün değerlerin eşit olsaydı ne olacağını söyler. Kapaktaki halka sütunları bunu gösterir: yüksek sütunlardan alçak sütunlara halka aktarılarak bütün sütunlar eşitlenirse, ulaşılan ortak yükseklik ortalamadır.",
            sutun_grafik("Dört sütundaki halka sayıları (ortalama 4)", ["A", "B", "C", "D"], [2, 5, 3, 6], y_son=6, adim=1),
            ornek(
                "Dört sütunda $2$, $5$, $3$ ve $6$ halka var.",
                "Sütunları eşitleyelim.",
                "Toplam $16$ halka dört sütuna eşit dağıtılırsa her sütunda $4$ halka olur.",
                "B sütunu $1$, D sütunu $2$ halka verir; A sütunu $2$, C sütunu $1$ halka alır."),
            "Buradan önemli bir özellik çıkar: değerlerin ortalamadan farklarının toplamı her zaman sıfırdır. Bu örnekte farklar $-2$, $1$, $-1$ ve $2$ dir ve toplamları $0$ dır. Ortalamanın üstündeki fazlalık, altındaki eksikliği tam olarak karşılar.",
        ]},
        {"baslik": "Toplamı ortalamadan bulmak", "icerik": [
            "Ortalama problemlerinin çoğu, ortalamadan toplama geçilerek çözülür. Ortalama ile değer sayısı çarpılınca toplam bulunur; toplam üzerinde işlem yapmak ortalamalar üzerinde işlem yapmaktan çok daha güvenlidir.",
            ornek(
                "Beş sayının ortalaması $12$ dir ve bu sayılardan biri $20$ dir.",
                "Kalan dört sayının ortalamasını bulalım.",
                "Beş sayının toplamı: $5 \\cdot 12=60$.",
                "Kalan dört sayının toplamı: $60-20=40$. Ortalamaları: $40:4=10$."),
        ]},
        {"baslik": "Veri eklemek ve çıkarmak", "icerik": [
            "Gruba yeni bir değer eklendiğinde ya da gruptan bir değer çıkarıldığında önce eski toplam bulunur, sonra değişiklik toplama uygulanır ve yeni değer sayısına bölünür.",
            ornek(
                "$20$ öğrencilik bir sınıfın sınav ortalaması $70$ tir. Sınava sonradan giren bir öğrenci $91$ alıyor.",
                "Sınıfın yeni ortalamasını bulalım.",
                "Eski toplam: $20 \\cdot 70=1400$. Yeni toplam: $1400+91=1491$.",
                "Yeni ortalama: $1491:21=71$."),
            ornek(
                "$10$ sayının ortalaması $15$ tir. Sayılardan biri çıkarılınca kalanların ortalaması $14$ oluyor.",
                "Çıkarılan sayıyı bulalım.",
                "İlk toplam: $10 \\cdot 15=150$. Kalan $9$ sayının toplamı: $9 \\cdot 14=126$.",
                "Çıkarılan sayı: $150-126=24$."),
            "Eklenen değer ortalamadan büyükse ortalama artar, küçükse azalır, ortalamaya eşitse değişmez. Birinci örnekte $91$, $70$ ten büyük olduğu için ortalama yükselmiştir.",
        ]},
        {"baslik": "Bir değeri değiştirmek", "icerik": [
            "Bir değer yanlış yazılmışsa ya da değiştirilmişse toplam, iki değer arasındaki fark kadar değişir. Ortalama ise bu farkın değer sayısına bölümü kadar değişir.",
            ornek(
                "$8$ sayının ortalaması $25$ olarak hesaplanmış. Sonra sayılardan birinin $18$ yerine yanlışlıkla $42$ yazıldığı fark ediliyor.",
                "Doğru ortalamayı bulalım.",
                "Toplam $42-18=24$ fazla hesaplanmıştır.",
                "Ortalama $24:8=3$ fazla hesaplanmıştır. Doğru ortalama: $25-3=22$.",
                "Kontrol: $8 \\cdot 25-24=176$ ve $176:8=22$."),
        ]},
        {"baslik": "Hedef ortalama için gereken değer", "icerik": [
            "Bir hedef ortalamaya ulaşmak için gereken değer de toplamlar üzerinden bulunur: hedef ortalamanın gerektirdiği toplamdan mevcut toplam çıkarılır.",
            ornek(
                "Bir öğrencinin dört sınavdaki ortalaması $70$ tir.",
                "Beşinci sınavdan kaç alırsa ortalamasının $74$ olacağını bulalım.",
                "Beş sınavda ortalamanın $74$ olması için toplam $5 \\cdot 74=370$ olmalıdır.",
                "Mevcut toplam: $4 \\cdot 70=280$. Gereken puan: $370-280=90$."),
            "Sonuç şöyle de yorumlanabilir: yeni sınav hem hedef ortalama olan $74$ puanı karşılamalı hem de eski dört sınavın her birinde hedefe eksik kalan $4$ puanı tamamlamalıdır. Gereken puan $74+4 \\cdot 4=90$ olarak da bulunur.",
        ]},
        {"baslik": "Ardışık sayıların ortalaması", "icerik": [
            "Aralarındaki fark sabit olan sayıların, yani ardışık sayıların ortalaması, ilk ve son terimin ortalamasıdır. Sayılar ortanın iki yanında simetrik dizildiği için ortalama tam ortadaki değere eşittir.",
            "$$\\text{Ortalama}=\\dfrac{\\text{ilk terim}+\\text{son terim}}{2}$$",
            ornek(
                "$12$ den $30$ a kadar olan çift sayılar verilsin.",
                "Bu sayıların ortalamasını ve toplamını bulalım.",
                "Ortalama: $\\dfrac{12+30}{2}=21$.",
                "Terim sayısı: $\\dfrac{30-12}{2}+1=10$. Toplam: $10 \\cdot 21=210$."),
            "Aynı kural $1$ den $99$ a kadar olan sayılar için ortalamayı $\\dfrac{1+99}{2}=50$ verir. Ardışık sayıların toplamı sorulduğunda ortalamayı terim sayısıyla çarpmak, sayıları tek tek toplamaktan çok daha hızlıdır.",
        ]},
        {"baslik": "Ağırlıklı ortalama", "icerik": [
            "Değerlerin önemi ya da sayısı farklıysa her değer kendi ağırlığıyla çarpılır ve toplam, ağırlıkların toplamına bölünür. Buna <strong>ağırlıklı ortalama</strong> denir.",
            ornek(
                "Bir okulda A sınıfındaki $30$ öğrencinin ortalaması $70$, B sınıfındaki $20$ öğrencinin ortalaması $80$ dir.",
                "İki sınıfın birlikte ortalamasını bulalım.",
                "Toplam puan: $30 \\cdot 70+20 \\cdot 80=2100+1600=3700$.",
                "Toplam öğrenci: $50$. Ortalama: $3700:50=74$."),
            dikkat(
                "Grupların ortalamalarının ortalamasını almak.",
                "$\\dfrac{70+80}{2}=75$ yanlıştır, çünkü A sınıfı daha kalabalıktır ve ortalamayı kendi değerine doğru çeker. İki grup ancak eşit sayıdaysa ortalamaların ortalaması doğru sonucu verir."),
            "Üniversitelerdeki not ortalaması da ağırlıklı ortalamadır: her dersin notu kredisiyle çarpılır. Kredisi $4$ olan bir dersten $80$, kredileri $3$ olan iki dersten $70$ ve $90$ alan bir öğrencinin ortalaması $\\dfrac{4 \\cdot 80+3 \\cdot 70+3 \\cdot 90}{10}=80$ dir.",
        ]},
        {"baslik": "Ortalama hız tuzağı", "icerik": [
            "Ortalama hız, toplam yolun toplam süreye bölümüdür; hızların aritmetik ortalaması değildir. Aynı yol farklı hızlarla gidilip dönüldüğünde yavaş gidilen kısımda daha uzun zaman geçer ve ortalama hız yavaş hıza yaklaşır.",
            ornek(
                "Bir araç $120$ kilometrelik yolu saatte $60$ kilometre hızla gidip saatte $40$ kilometre hızla dönüyor.",
                "Ortalama hızı bulalım.",
                "Gidiş süresi: $120:60=2$ saat. Dönüş süresi: $120:40=3$ saat.",
                "Ortalama hız: $\\dfrac{240}{5}=48$ kilometre bölü saat; $50$ değil."),
            "Hareket problemlerinin ayrıntısı <a href=\"/blog/hareket-problemleri-konu-anlatimi-pdf/\">Hareket Problemleri Konu Anlatımı PDF</a> yazısında.",
        ]},
        {"baslik": "Ortanca", "icerik": [
            "Veriler küçükten büyüğe sıralandığında tam ortada kalan değere <strong>ortanca</strong> ya da medyan denir. Değer sayısı tekse ortanca tek bir değerdir; çiftse ortadaki iki değerin ortalamasıdır.",
            ornek(
                "$3$, $8$, $5$, $12$ ve $7$ verileri ile $4$, $9$, $2$, $7$, $10$ ve $6$ verileri verilsin.",
                "İki veri grubunun ortancasını bulalım.",
                "Birinci grup sıralanır: $3$, $5$, $7$, $8$, $12$. Ortadaki değer $7$ dir.",
                "İkinci grup sıralanır: $2$, $4$, $6$, $7$, $9$, $10$. Ortadaki iki değer $6$ ve $7$ dir; ortanca $\\dfrac{6+7}{2}=6.5$ tir."),
            dikkat(
                "Verileri sıralamadan ortadaki değeri almak.",
                "Birinci grupta sıralamadan ortadaki değere bakılsaydı $5$ bulunurdu. Ortanca her zaman sıralanmış veride aranır."),
        ]},
        {"baslik": "Tepe değer", "icerik": [
            "Veri grubunda en çok tekrar eden değere <strong>tepe değer</strong> ya da mod denir. Bir veri grubunun birden fazla tepe değeri olabilir; bütün değerler eşit sayıda tekrar ediyorsa tepe değer yoktur.",
            ornek(
                "$2$, $3$, $3$, $5$, $7$, $7$, $7$ ve $9$ verileri verilsin.",
                "Tepe değeri bulalım.",
                "$7$ üç kez, $3$ iki kez, diğerleri birer kez tekrar ediyor.",
                "Tepe değer $7$ dir."),
            "Tepe değer sayısal olmayan veriler için de kullanılabilen tek merkezî eğilim ölçüsüdür. En çok tercih edilen renk ya da en sık kullanılan ulaşım biçimi gibi sorular tepe değerle cevaplanır; bu tür verilerin ortalaması ya da ortancası olmaz.",
        ]},
        {"baslik": "Sıklık tablosundan ortalama", "icerik": [
            "Veriler sıklık tablosuyla verildiğinde her değer sıklığıyla çarpılır ve toplam, veri sayısına bölünür. Bu da bir ağırlıklı ortalamadır: ağırlıklar sıklıklardır.",
            tablo(["Not", "Öğrenci sayısı", "Not çarpı sayı"], [
                ["$1$", "$2$", "$2$"],
                ["$2$", "$6$", "$12$"],
                ["$3$", "$14$", "$42$"],
                ["$4$", "$10$", "$40$"],
                ["$5$", "$8$", "$40$"],
                ["Toplam", "$40$", "$136$"],
            ]),
            ornek(
                "Tabloda $40$ öğrencinin notları veriliyor.",
                "Ortalamayı, ortancayı ve tepe değeri bulalım.",
                "Ortalama: $136:40=3.4$.",
                "Ortanca: $40$ değer sıralanınca ortadaki iki değer $20$. ve $21$. değerlerdir. İlk $8$ öğrencinin notu $1$ ya da $2$, sonraki $14$ öğrencinin notu $3$ tür; bu iki değer de $3$ tür. Ortanca $3$.",
                "Tepe değer: en kalabalık grup $14$ öğrenciyle not $3$."),
        ]},
        {"baslik": "Ortalama mı, ortanca mı?", "icerik": [
            "Aritmetik ortalama bütün değerleri hesaba kattığı için uç değerlerden çok etkilenir. Ortanca ise yalnızca sıralamaya baktığı için uç değerlerden etkilenmez.",
            sutun_grafik("Bir işyerindeki beş çalışanın aylık kazancı (bin TL)", ["1.", "2.", "3.", "4.", "5."], [20, 22, 24, 26, 108], y_son=120, adim=20),
            ornek(
                "Beş çalışanın aylık kazançları $20$, $22$, $24$, $26$ ve $108$ bin TL.",
                "Ortalamayı ve ortancayı bulup karşılaştıralım.",
                "Ortalama: $\\dfrac{20+22+24+26+108}{5}=\\dfrac{200}{5}=40$ bin TL.",
                "Ortanca: $24$ bin TL.",
                "Beş çalışandan dördü ortalamanın altında kazanır. Tek bir yüksek değer, ortalamayı grubun çoğunluğundan uzaklaştırmıştır."),
            "Bu yüzden gelir, konut fiyatı gibi uç değer içeren verilerde ortanca, tipik değeri ortalamadan daha iyi gösterir. Uç değer yoksa ve veri simetrik dağılıyorsa ortalama ile ortanca birbirine yakın çıkar.",
        ]},
        {"baslik": "Açıklık", "icerik": [
            "Ortalama, verinin merkezini gösterir ama verinin ne kadar yayıldığını göstermez. Yayılımın en basit ölçüsü <strong>açıklıktır</strong>: en büyük değerden en küçük değerin çıkarılmasıyla bulunur.",
            ornek(
                "A grubunun puanları $48$, $50$ ve $52$; B grubunun puanları $20$, $50$ ve $80$ dir.",
                "İki grubun ortalamasını ve açıklığını karşılaştıralım.",
                "İki grubun ortalaması da $50$ dir.",
                "A grubunun açıklığı $52-48=4$, B grubunun açıklığı $80-20=60$ tır.",
                "Ortalamalar aynı olsa da A grubu ortalamanın çevresinde toplanmış, B grubu ise geniş bir aralığa yayılmıştır."),
            "Açıklık hesaplaması kolaydır ama yalnızca iki değere bakar. Tek bir uç değer açıklığı çok büyütebilir; bu yüzden yayılımı daha güvenilir ölçen başka ölçüler de kullanılır.",
        ]},
        {"baslik": "Çeyrekler açıklığı", "icerik": [
            "Sıralanmış veri ortancayla iki yarıya ayrılır. Alt yarının ortancasına <strong>alt çeyrek</strong>, üst yarının ortancasına <strong>üst çeyrek</strong> denir. İkisinin farkı <strong>çeyrekler açıklığıdır</strong> ve verinin ortadaki yarısının ne kadar yayıldığını gösterir. Değer sayısı tekse ortanca iki yarıya da katılmaz.",
            ornek(
                "$3$, $5$, $7$, $8$, $10$, $12$, $15$ ve $20$ verileri verilsin.",
                "Ortancayı, çeyrekleri ve çeyrekler açıklığını bulalım.",
                "Ortanca: $\\dfrac{8+10}{2}=9$.",
                "Alt yarı $3$, $5$, $7$, $8$; alt çeyrek $\\dfrac{5+7}{2}=6$. Üst yarı $10$, $12$, $15$, $20$; üst çeyrek $\\dfrac{12+15}{2}=13.5$.",
                "Çeyrekler açıklığı: $13.5-6=7.5$."),
            "Çeyrekler açıklığı en küçük ve en büyük değerleri hesaba katmaz. Bu yüzden uç değerlerden etkilenmez: son değer $20$ yerine $200$ olsaydı açıklık çok büyürdü ama çeyrekler açıklığı değişmezdi.",
        ]},
        {"baslik": "Standart sapma", "icerik": [
            "<strong>Standart sapma</strong>, değerlerin ortalamadan ortalama olarak ne kadar uzaklaştığını ölçer. Her değerin ortalamadan farkının karesi alınır, kareler toplanır, değer sayısının bir eksiğine bölünür ve karekök alınır:",
            "$$s=\\sqrt{\\dfrac{(x_1-\\overline{x})^2+(x_2-\\overline{x})^2+\\cdots+(x_n-\\overline{x})^2}{n-1}}$$",
            ornek(
                "$7$, $7$, $10$, $13$ ve $13$ verileri verilsin.",
                "Standart sapmayı bulalım.",
                "Ortalama: $\\dfrac{50}{5}=10$. Farklar: $-3$, $-3$, $0$, $3$, $3$.",
                "Farkların kareleri: $9$, $9$, $0$, $9$, $9$; toplam $36$.",
                "$s=\\sqrt{\\dfrac{36}{4}}=\\sqrt{9}=3$."),
            "Standart sapma küçükse veriler ortalamanın çevresinde toplanmıştır; büyükse geniş bir alana yayılmıştır. Bütün değerler eşitse standart sapma $0$ dır. Bazı kaynaklarda paydada $n-1$ yerine $n$ kullanılır; bu durumda sonuç biraz küçük çıkar ama iki grubun karşılaştırması değişmez.",
        ]},
        {"baslik": "Bütün değerleri değiştirmek", "icerik": [
            "Bir veri grubunun bütün değerlerine aynı sayı eklenirse ortalama, ortanca ve tepe değer de o sayı kadar artar; açıklık ve standart sapma ise değişmez, çünkü değerler arasındaki uzaklıklar aynı kalır. Bütün değerler aynı pozitif sayıyla çarpılırsa ise merkez ölçüleri de yayılım ölçüleri de o sayıyla çarpılır.",
            ornek(
                "$7$, $7$, $10$, $13$ ve $13$ verilerinin ortalaması $10$, standart sapması $3$ tür.",
                "Her değere $5$ eklenince ve her değer $2$ ile çarpılınca ortalamanın ve standart sapmanın nasıl değiştiğini bulalım.",
                "Her değere $5$ eklenince veri $12$, $12$, $15$, $18$, $18$ olur: ortalama $15$, standart sapma yine $3$.",
                "Her değer $2$ ile çarpılınca veri $14$, $14$, $20$, $26$, $26$ olur: ortalama $20$, standart sapma $6$."),
            "Bu özellik, bir sınavın bütün puanlarına aynı ek puan verildiğinde sınıfın başarı sıralamasının ve puanların dağılımının neden değişmediğini açıklar: herkes aynı miktarda yükselir.",
        ]},
        {"baslik": "Farkların karesi neden alınır?", "icerik": [
            "Standart sapma hesabında farklar doğrudan toplanmaz, çünkü ortalamadan farkların toplamı her zaman sıfırdır. Kare almak, negatif ve pozitif farkların birbirini götürmesini önler ve ortalamadan uzak değerlere daha fazla ağırlık verir.",
            "Karekök ise sonucu verinin kendi birimine geri döndürür. Puanlarla çalışılıyorsa standart sapma da puan cinsindendir; bu sayede \"değerler ortalamadan tipik olarak $3$ puan uzaklaşıyor\" gibi bir yorum yapılabilir.",
        ]},
        {"baslik": "Sınavda ortalama ve veri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) ortalama, veri ekleme, çıkarma ve değiştirme problemleri, ağırlıklı ortalama, ortanca ve tepe değer biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde ortalama soruları sayısal akıl yürütmenin ve tablo yorumlamanın parçasıdır."),
            "Ortalama sorularında ilk adım neredeyse her zaman aynıdır: ortalamayı değer sayısıyla çarpıp toplama geç. Toplam üzerinde ekleme, çıkarma ya da değiştirme yap ve en son yeni değer sayısına böl. Bu üç adım, ortalama problemlerinin büyük bölümünü çözer.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Ortalamaların ortalamasını almak", "Grup büyüklükleriyle ağırlıklandır"],
                ["Ortalama hızı hızların ortalaması sanmak", "Toplam yol bölü toplam süre"],
                ["Ortancayı sıralamadan bulmak", "Önce küçükten büyüğe sırala"],
                ["Veri çıkarınca eski sayıya bölmek", "Yeni değer sayısına böl"],
                ["Uç değerli veride yalnız ortalamaya bakmak", "Ortancayı da kontrol et"],
                ["Aynı ortalamayı aynı dağılım sanmak", "Açıklık ya da standart sapmaya bak"],
            ]),
            "Bu hataların çoğu ortalamanın ne anlattığını unutmaktan doğar. Ortalama bir eşitlemedir; bir veri grubunu tek sayıya indirirken bilginin bir kısmını kaybeder. Bu yüzden iyi bir veri analizi, merkezi gösteren bir ölçüyü yayılımı gösteren bir ölçüyle birlikte kullanır.",
        ]},
    ],
    "sss": [
        ("Aritmetik ortalama nasıl bulunur?",
         "Bütün değerler toplanır ve toplam, değer sayısına bölünür. 7, 9, 10, 12 ve 12 puanlarının ortalaması 50 bölü 5, yani 10 dur."),
        ("Ortanca nedir?",
         "Veriler küçükten büyüğe sıralandığında ortada kalan değerdir. Değer sayısı çiftse ortadaki iki değerin ortalamasıdır."),
        ("Tepe değer nedir?",
         "Veri grubunda en çok tekrar eden değerdir. Birden fazla olabilir; bütün değerler eşit sayıda tekrar ediyorsa tepe değer yoktur."),
        ("Ağırlıklı ortalama nedir?",
         "Her değerin ağırlığıyla çarpıldığı ve toplamın ağırlıkların toplamına bölündüğü ortalamadır. Farklı büyüklükteki grupların birlikte ortalaması böyle bulunur."),
        ("Ortalama ile ortanca ne zaman farklı çıkar?",
         "Veride uç değerler varsa ortalama bu değerlere doğru kayar, ortanca ise etkilenmez. Simetrik ve uç değersiz verilerde ikisi birbirine yakındır."),
        ("Standart sapma neyi gösterir?",
         "Değerlerin ortalamadan tipik olarak ne kadar uzaklaştığını gösterir. Küçük standart sapma verilerin ortalama çevresinde toplandığını, büyük standart sapma geniş bir alana yayıldığını anlatır."),
    ],
    "kontrol": [
        "Aritmetik ortalamayı hesaplayabiliyorum.",
        "Ortalamanın bir eşitleme olduğunu açıklayabiliyorum.",
        "Ortalamadan toplama geçerek problem çözebiliyorum.",
        "Veri ekleme, çıkarma ve değiştirme problemlerini çözebiliyorum.",
        "Ağırlıklı ortalamayı hesaplayabiliyorum.",
        "Ortanca ve tepe değeri bulabiliyorum.",
        "Uç değerlerin ortalamaya ve ortancaya etkisini yorumlayabiliyorum.",
        "Açıklığı ve çeyrekler açıklığını hesaplayabiliyorum.",
        "Küçük bir veri grubunun standart sapmasını bulabiliyorum.",
        "Merkez ve yayılım ölçülerini birlikte yorumlayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["tablo-ve-grafik-yorumlama", "hareket-problemleri-konu-anlatimi-pdf", "yuzdeler-konu-anlatimi-pdf"],
}
