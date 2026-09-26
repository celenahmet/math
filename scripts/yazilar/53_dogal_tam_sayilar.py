# scripts/yazilar/53_dogal_tam_sayilar.py — Dogal Sayilar ve Tam Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "dogal-sayilar-ve-tam-sayilar",
    "baslik": "Doğal Sayılar ve Tam Sayılar",
    "aciklama": "Doğal sayılar ve tam sayılar nedir? Dört işlem, işaret kuralları, işlem önceliği, bölme ve kalan, sıralama ve sayma soruları; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "dogal-sayilar-ve-tam-sayilar",
    "kapak_alt": "Doğal sayılar ve tam sayılar: sıfırdan iki yöne uzanan ray üzerinde kırmızı ve mavi boncukları dizen iki öğrenci",
    "ozet": "Doğal sayılar saymakla başlar; tam sayılar ise sıfırın öbür tarafına, negatiflere geçer. Dört işlemin kuralları ilk olarak bu iki kümede öğrenilir ve dikkat isteyen noktalar da buradadır: işaret kuralı, işlem önceliği, negatif sayının kuvveti ve negatif sayının bölümünden kalan. Bu yazıda iki kümeyi tanımlıyor, dört işlemi ve kurallarını adım adım işliyor, sayma ve işaret sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Doğal sayılar", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi ve sayı doğrusunu biliyor olman yeterli.",
                "Sayı kümelerinin genel resmi için <a href=\"/blog/sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf/\">Sayılar ve Sayı Kümeleri Konu Anlatımı PDF</a> yazısına göz at."),
            "<strong>Doğal sayılar</strong>, saymak ve sıralamak için kullandığımız sayılardır. Küme $\\mathbb{N}$ ile gösterilir ve $0$ dan başlar:",
            "$$\\mathbb{N}=\\{0,1,2,3,\\ldots\\}$$",
            "Doğal sayıların en küçüğü $0$ dır, en büyüğü yoktur. Her doğal sayının bir <strong>ardılı</strong> vardır: $n$ nin ardılı $n+1$ dir. $0$ dışındaki her doğal sayının bir de <strong>öncülü</strong> vardır: $n-1$.",
            "Doğal sayılarda toplama ve çarpma her zaman yapılabilir, sonuç yine doğal sayıdır. Çıkarma ve bölme ise her zaman yapılamaz: $3-5$ ve $3 \\div 5$ doğal sayı değildir. Tam sayılara geçmemizin sebebi tam olarak bu eksikliktir.",
            hap("Doğal sayılar $0$ dan başlar; en küçük doğal sayı $0$ dır.",
                "Doğal sayılarda toplama ve çarpma her zaman yapılabilir, çıkarma ve bölme her zaman yapılamaz."),
        ]},
        {"baslik": "İşlem özellikleri", "icerik": [
            "Toplama ve çarpma işlemlerinin bazı özellikleri hem doğal sayılarda hem tam sayılarda geçerlidir. Bunlar hesap yaparken işlemleri kolaylaştırmak için kullanılır:",
            "<ul>"
            "<li><strong>Değişme:</strong> $a+b=b+a$ ve $a \\cdot b=b \\cdot a$. Sıranın önemi yoktur.</li>"
            "<li><strong>Birleşme:</strong> $(a+b)+c=a+(b+c)$ ve $(a \\cdot b) \\cdot c=a \\cdot (b \\cdot c)$. Gruplamanın önemi yoktur.</li>"
            "<li><strong>Dağılma:</strong> $a \\cdot (b+c)=a \\cdot b+a \\cdot c$. Çarpma, toplamaya dağılır.</li>"
            "<li><strong>Etkisiz eleman:</strong> toplamada $0$, çarpmada $1$. $a+0=a$ ve $a \\cdot 1=a$.</li>"
            "<li><strong>Yutan eleman:</strong> çarpmada $0$. $a \\cdot 0=0$.</li>"
            "</ul>",
            "Çıkarma ve bölmede değişme ve birleşme özellikleri <strong>yoktur</strong>: $8-3 \\neq 3-8$ ve $(12 \\div 6) \\div 2 \\neq 12 \\div (6 \\div 2)$. Soldaki $1$, sağdaki $4$ eder.",
            "Dağılma özelliği çıkarmada da geçerlidir: $a \\cdot (b-c)=a \\cdot b-a \\cdot c$. Bu, zihinden hızlı çarpma yapmayı sağlar: $25 \\cdot 98=25 \\cdot (100-2)=2500-50=2450$.",
            ornek(
                "$37 \\cdot 25+37 \\cdot 75$ işlemi verilsin.",
                "Sonucu kısa yoldan bulalım.",
                "Ortak çarpan $37$ yi dağılma özelliğinin tersiyle dışarı alalım: $37 \\cdot (25+75)$.",
                "Parantezin içi $100$ eder: $37 \\cdot 100=3700$."),
        ]},
        {"baslik": "Tam sayılar ve zıt sayı", "icerik": [
            "Doğal sayılara negatif sayılar eklenince <strong>tam sayılar</strong> kümesi $\\mathbb{Z}$ oluşur:",
            "$$\\mathbb{Z}=\\{\\ldots,-3,-2,-1,0,1,2,3,\\ldots\\}$$",
            "Negatif sayılar günlük hayatta sıfırın altındaki hava sıcaklığı, deniz seviyesinin altındaki yükseklik ya da bir hesaptaki borç gibi durumları anlatır. Sayı doğrusunda sıfırın solunda yer alırlar.",
            "Her tam sayının bir <strong>zıttı</strong> (toplama işlemine göre tersi) vardır. $a$ nın zıttı $-a$ dır ve ikisinin toplamı $0$ dır: $5+(-5)=0$. Zıt sayılar sayı doğrusunda $0$ a eşit uzaklıktadır. $0$ ın zıttı kendisidir.",
            "Bir sayının $0$ a olan uzaklığına <strong>mutlak değer</strong> denir ve $|a|$ ile gösterilir: $|-7|=7$ ve $|7|=7$. Uzaklık negatif olamayacağı için mutlak değer hiçbir zaman negatif değildir.",
            hap("$a$ nın zıttı $-a$ dır ve $a+(-a)=0$.",
                "Mutlak değer, sıfıra olan uzaklıktır; hiçbir zaman negatif değildir."),
            dikkat(
                "$-a$ her zaman negatif bir sayı değildir.",
                "$a=-3$ ise $-a=3$ tür. $-a$, \"$a$ nın zıttı\" demektir; işareti $a$ ya bağlıdır."),
        ]},
        {"baslik": "Tam sayılarda sıralama", "icerik": [
            "Sayı doğrusunda sağdaki sayı her zaman soldakinden büyüktür. Pozitif sayılarda bu alışık olduğumuz sıralamadır. Negatif sayılarda ise sıfırdan uzaklaştıkça sayı küçülür: $-7<-2<0<3$.",
            "Bu yüzden iki negatif sayıdan <strong>mutlak değeri büyük</strong> olan daha küçüktür. $-15$ ile $-4$ ten küçük olan $-15$ tir.",
            "Sıralamada zıt sayılar da sık kullanılır. $a<b$ ise $-a>-b$ dir: bir eşitsizliğin iki tarafı $-1$ ile çarpılınca yön değişir. Örneğin $2<5$ iken $-2>-5$ tir.",
            ornek(
                "$-8$, $3$, $-1$, $0$, $-12$, $5$ sayıları verilsin.",
                "Bu sayıları küçükten büyüğe sıralayalım.",
                "Negatifleri mutlak değeri büyük olandan başlayarak yazarız: $-12$, $-8$, $-1$.",
                "Sonra $0$, sonra pozitifler: $3$, $5$.",
                "Sıralama: $-12<-8<-1<0<3<5$."),
            hap("İki negatif sayıdan mutlak değeri büyük olan <strong>daha küçüktür</strong>.",
                "Her negatif sayı $0$ dan, $0$ da her pozitif sayıdan küçüktür."),
        ]},
        {"baslik": "Toplama ve çıkarma", "icerik": [
            "Tam sayılarda toplama iki kurala dayanır:",
            "<ul><li><strong>Aynı işaretli</strong> iki sayı toplanırken mutlak değerler toplanır, ortak işaret sonuca yazılır: $(-8)+(-5)=-13$.</li><li><strong>Farklı işaretli</strong> iki sayı toplanırken büyük mutlak değerden küçüğü çıkarılır, mutlak değeri büyük olanın işareti sonuca yazılır: $(-8)+5=-3$.</li></ul>",
            "Çıkarma için ayrı bir kural gerekmez. Bir sayıyı çıkarmak, zıttını eklemektir. Böylece her çıkarma bir toplamaya çevrilir:",
            "$$a-b=a+(-b)$$",
            ornek(
                "$7-(-4)$ ve $-6-9$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "$7-(-4)=7+4=11$. Negatif bir sayıyı çıkarmak, pozitifini eklemektir.",
                "$-6-9=-6+(-9)=-15$. Aynı işaretli iki sayı toplandı."),
            ornek(
                "Bir şehirde sabah sıcaklık $-4$ derece. Öğlene kadar $9$ derece artıyor, akşama kadar $12$ derece düşüyor.",
                "Akşam sıcaklık kaç derecedir?",
                "Artışı toplama, düşüşü çıkarma olarak yazalım: $-4+9-12$.",
                "Soldan sağa: $-4+9=5$ ve $5-12=-7$.",
                "Akşam sıcaklık $-7$ derecedir."),
            hap("Çıkarma, zıt sayıyı eklemektir: $a-b=a+(-b)$.",
                "Bu yüzden $a-(-b)=a+b$ olur."),
        ]},
        {"baslik": "Çarpma ve bölme", "icerik": [
            "Çarpma ve bölmede mutlak değerler çarpılır ya da bölünür, işaret ise şu kuralla bulunur: <strong>aynı işaretliler pozitif, farklı işaretliler negatif</strong> sonuç verir.",
            tablo(["İşaretler", "Sonucun işareti"], [
                ["$(+) \\cdot (+)$", "Pozitif"],
                ["$(-) \\cdot (-)$", "Pozitif"],
                ["$(+) \\cdot (-)$", "Negatif"],
                ["$(-) \\cdot (+)$", "Negatif"],
            ]),
            "Aynı tablo bölme için de geçerlidir: $(-36) \\div 9=-4$ ve $(-36) \\div (-9)=4$.",
            "Birden fazla çarpan varsa negatif çarpanlar sayılır. Negatif çarpan sayısı çiftse sonuç pozitif, tekse negatiftir. Aynı fikir kuvvetlerde de geçerlidir: $(-1)^{25}=-1$ ve $(-2)^2=4$ olduğundan $(-1)^{25} \\cdot (-2)^2=-4$ tür.",
            hap("Negatif çarpanların sayısı çiftse çarpım pozitif, tekse negatiftir.",
                "Bir çarpanı $0$ olan çarpım $0$ dır."),
            dikkat(
                "Sıfıra bölme tanımsızdır; $5 \\div 0$ diye bir sayı yoktur.",
                "Sıfırın bir sayıya bölümü ise sıfırdır: $0 \\div 5=0$. İkisini karıştırma."),
        ]},
        {"baslik": "Negatif tabanlı kuvvetler", "icerik": [
            "Kuvvet, aynı sayının tekrarlı çarpımıdır. Taban negatifse her çarpan bir eksi işareti getirir; bu yüzden sonucun işareti üssün tek ya da çift olmasına bağlıdır. En sık kullanılan taban $-1$ dir:",
            "$$(-1)^{\\text{çift}}=1 \\ \\ \\ \\text{ve} \\ \\ \\ (-1)^{\\text{tek}}=-1$$",
            "Bu kural, $(-1)$ in kuvvetlerinden oluşan uzun toplamları birkaç satırda çözmeyi sağlar: ardışık iki terim birbirini götürür.",
            ornek(
                "$(-1)^1+(-1)^2+(-1)^3+\\cdots+(-1)^{101}$ toplamı verilsin.",
                "Bu toplam kaçtır?",
                "Terimler sırayla $-1$, $1$, $-1$, $1$, ... diye gider. Her ardışık $(-1)+1$ çifti $0$ eder.",
                "İlk $100$ terim $50$ çift oluşturur ve toplamları $0$ dır.",
                "Geriye $101$. terim kalır: $(-1)^{101}=-1$. Toplam $-1$ dir."),
            hap("$(-1)$ in çift kuvveti $1$, tek kuvveti $-1$ dir.",
                "Uzun toplamlarda ardışık terimleri eşleştir; eşleşmeyen terim sonucu verir."),
        ]},
        {"baslik": "İşlem önceliği", "icerik": [
            "Birden fazla işlemin bulunduğu ifadelerde işlemler şu sırayla yapılır:",
            "<ol><li>Parantez içi (içteki parantezden dışa doğru).</li><li>Üslü ifadeler.</li><li>Çarpma ve bölme, <strong>soldan sağa</strong>.</li><li>Toplama ve çıkarma, <strong>soldan sağa</strong>.</li></ol>",
            "Çarpma ile bölme aynı önceliktedir; hangisi önce geliyorsa o yapılır. Toplama ile çıkarma için de aynısı geçerlidir.",
            ornek(
                "$12-3 \\cdot (-2)^2+8 \\div (-4)$ ifadesi verilsin.",
                "Sonucu işlem önceliğine göre bulalım.",
                "Önce kuvvet: $(-2)^2=4$. İfade $12-3 \\cdot 4+8 \\div (-4)$ olur.",
                "Sonra çarpma ve bölme: $3 \\cdot 4=12$ ve $8 \\div (-4)=-2$. İfade $12-12+(-2)$ olur.",
                "Son olarak toplama ve çıkarma: $12-12-2=-2$."),
            ornek(
                "$-2^2+(-3) \\cdot [4-(-1)]$ ifadesi verilsin.",
                "Sonucu bulalım.",
                "Köşeli parantezin içi: $4-(-1)=4+1=5$.",
                "$-2^2=-4$ tür; eksi işareti kuvvete girmez.",
                "Çarpma: $(-3) \\cdot 5=-15$.",
                "Sonuç: $-4+(-15)=-19$."),
            dikkat(
                "Çarpma ve bölme soldan sağa yapılır, çarpma önce yapılmaz.",
                "$24 \\div 4 \\cdot 2$ işleminde önce $24 \\div 4=6$, sonra $6 \\cdot 2=12$ bulunur. Sonuç $3$ değildir."),
            hap("Tanesi $10$ liradan $3$ ekmek ve tanesi $25$ liradan $2$ süt alan birinin tutarı $3 \\cdot 10+2 \\cdot 25=80$ lira olur.", "İşlem önceliği bozulursa $(3 \\cdot 10+2) \\cdot 25=800$ gibi yanlış bir tutar çıkar.", gunluk=True),
        ]},
        {"baslik": "Bölme ve kalan", "icerik": [
            "Bir tam sayıyı pozitif bir tam sayıya böldüğümüzde bölüm ve kalan şu eşitlikle tanımlanır:",
            "$$a=b \\cdot q+r \\ \\ \\ (0 \\leq r<b)$$",
            "Burada $a$ bölünen, $b$ bölen, $q$ bölüm ve $r$ kalandır. En önemli şart kalanın $0$ ile $b-1$ arasında olmasıdır: kalan hiçbir zaman negatif değildir ve bölenden küçüktür.",
            ornek(
                "$47$ sayısı $6$ ya bölünsün.",
                "Bölüm ve kalanı bulalım.",
                "$6 \\cdot 7=42$ ve $47-42=5$.",
                "$47=6 \\cdot 7+5$. Bölüm $7$, kalan $5$ tir."),
            ornek(
                "$-17$ sayısı $5$ e bölünsün.",
                "Bölüm ve kalanı bulalım.",
                "Kalan negatif olamayacağı için $-17$ den küçük ya da ona eşit olan en büyük $5$ katını ararız: $5 \\cdot (-4)=-20$.",
                "$-17=5 \\cdot (-4)+3$.",
                "Bölüm $-4$, kalan $3$ tür. $-3$ değildir."),
            "Kalan soruları, sayının kendisini bilmeden de çözülebilir. Bir sayının $b$ ile bölümünden kalanı biliyorsan, o sayının katlarının ve toplamlarının kalanını da bulabilirsin.",
            ornek(
                "Bir $n$ doğal sayısının $7$ ile bölümünden kalan $4$ olsun.",
                "$3n$ nin $7$ ile bölümünden kalan kaçtır?",
                "$n=7q+4$ yazalım. O zaman $3n=21q+12$ olur.",
                "$21q$, $7$ ye tam bölünür. Geriye $12$ nin kalanı kalır: $12=7 \\cdot 1+5$.",
                "Kalan $5$ tir. Kontrol: $n=11$ için $3n=33$ ve $33=7 \\cdot 4+5$."),
            "Kalan en fazla $b-1$ olabilir. Örneğin $9$ ile bölümünden kalan en fazla $8$ dir. Bölümü $12$ olan ve kalanı en büyük olan sayı $9 \\cdot 12+8=116$ dır.",
            hap("Kalan her zaman $0 \\leq r<b$ aralığındadır.",
                "Negatif sayıyı bölerken kalanı negatif yazma; bölümü bir azaltıp kalanı pozitife çevir."),
        ]},
        {"baslik": "Tam sayıları sayma ve toplama", "icerik": [
            "İki tam sayı ve aralarındaki bütün tam sayılar bir ardışık dizi oluşturur. Bu dizideki eleman sayısı ve toplam kısa formüllerle bulunur.",
            "<ul><li>$a$ dan $b$ ye kadar (ikisi dahil) tam sayıların sayısı: $b-a+1$.</li><li>Uçlar hariçse iki eksik: $b-a-1$.</li><li>Toplam: $\\dfrac{a+b}{2} \\cdot (b-a+1)$.</li></ul>",
            ornek(
                "$-4$ ile $6$ arasındaki tam sayıları düşünelim.",
                "Uçlar dahil ve hariç kaç tam sayı vardır?",
                "Uçlar dahil: $6-(-4)+1=11$ tane.",
                "Uçlar hariç: $11-2=9$ tane ($-3$ ten $5$ e kadar)."),
            ornek(
                "$-10$ dan $12$ ye kadar olan bütün tam sayılar toplansın.",
                "Toplam kaçtır?",
                "$-10$ ile $10$, $-9$ ile $9$, ... birbirini götürür; $0$ da toplamı değiştirmez.",
                "Geriye $11$ ve $12$ kalır: toplam $23$ tür.",
                "Formülle kontrol: $\\dfrac{-10+12}{2} \\cdot 23=1 \\cdot 23=23$."),
            hap("Simetrik bir aralıkta ($-n$ den $n$ ye) tam sayıların toplamı $0$ dır.",
                "Simetrik olmayan aralıkta önce simetrik kısmı at, kalanları topla."),
        ]},
        {"baslik": "İşaret soruları", "icerik": [
            "Bazı sorularda sayıların kendisi değil, yalnızca işaretleriyle ilgili bilgiler verilir. Yöntem şudur: kesin işareti bilinen sayıdan başla, çarpım ve bölüm bilgilerini tek tek kullanarak diğerlerine geç.",
            ornek(
                "$a$, $b$, $c$ sıfırdan farklı tam sayılar olsun. $a<0$, $a \\cdot b>0$ ve $b \\cdot c<0$ verilsin.",
                "$a \\cdot c$, $a+b$ ve $c-a$ ifadelerinin işaretini bulalım.",
                "$a<0$ ve $a \\cdot b>0$ ise $b$ de negatiftir, çünkü çarpım pozitif çıkmış.",
                "$b<0$ ve $b \\cdot c<0$ ise $c$ pozitiftir.",
                "$a \\cdot c$: negatif ile pozitifin çarpımı, negatif.",
                "$a+b$: iki negatifin toplamı, negatif.",
                "$c-a=c+(-a)$: iki pozitifin toplamı, pozitif."),
            dikkat(
                "Toplamın işareti, çarpımınki gibi yalnızca işaretlerden bulunamayabilir.",
                "$a<0<b$ ise $a+b$ nin işareti, hangisinin mutlak değerinin büyük olduğuna bağlıdır. $-5+3<0$ ama $-2+3>0$."),
        ]},
        {"baslik": "Sınavda doğal sayılar ve tam sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu bir problemin içinde de gelebilir: işlem önceliği, negatif sayının kuvveti ve bölme ve kalan soruları bu türdendir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde işlem hızı öne çıkar. İşlem özelliklerini (dağılma, ortak çarpan parantezi) bilmek uzun hesapları kısaltır."),
            "Bu konuda hatalar yalnızca kavramdan değil, işaret ve işlem sırasından da çıkabilir. Her adımda işareti ayrı yazmak ve işlem önceliğini sırayla uygulamak bu tür hataları önler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$-2^2=4$ yazmak", "$-2^2=-4$, $(-2)^2=4$"],
                ["$7-(-4)=3$ yazmak", "$7+4=11$"],
                ["Çarpmayı bölmeden önce yapmak", "Soldan sağa"],
                ["Negatif sayıda kalanı negatif yazmak", "$0 \\leq r<b$"],
                ["$-a$ yı her zaman negatif sanmak", "İşareti $a$ ya bağlı"],
                ["Uçlar dahil sayarken $+1$ i unutmak", "$b-a+1$"],
                ["$0 \\div 5$ ile $5 \\div 0$ ı karıştırmak", "$0$ ve tanımsız"],
            ]),
            "Bu tablodaki hataların hepsi ayrıntıya dikkat etmekle önlenir. Özellikle eksi işaretinin nereye ait olduğu (sayıya mı, kuvvete mi, işleme mi) her adımda açıkça belirtilmelidir.",
        ]},
    ],
    "sss": [
        ("Doğal sayılar ile tam sayılar arasındaki fark nedir?",
         "Doğal sayılar 0 dan başlayan ve 1 er artan sayılardır. Tam sayılar ise doğal sayılara negatif sayıların eklenmesiyle oluşur. Her doğal sayı bir tam sayıdır ama negatif tam sayılar doğal sayı değildir."),
        ("İşlem önceliği nasıldır?",
         "Önce parantez içi, sonra üslü ifadeler, sonra çarpma ve bölme, en son toplama ve çıkarma yapılır. Aynı önceliğe sahip işlemler soldan sağa doğru yapılır."),
        ("Eksi ile eksinin çarpımı neden artıdır?",
         "Bir sayıyı negatif bir sayıyla çarpmak, sayıyı sıfıra göre ters yöne çevirmek demektir. Negatif bir sayı ters çevrilince pozitif olur. Bu yüzden iki negatif sayının çarpımı pozitiftir."),
        ("Negatif bir sayının bölümünden kalan nasıl bulunur?",
         "Kalan hiçbir zaman negatif olamaz ve bölenden küçük olmalıdır. Bu yüzden bölünen sayıdan küçük ya da ona eşit en büyük bölen katı bulunur. Örneğin eksi 17 nin 5 ile bölümünde bölüm eksi 4, kalan 3 tür."),
        ("Sıfır tam sayı mıdır?",
         "Evet. Sıfır hem bir doğal sayı hem bir tam sayıdır. Ne pozitif ne negatiftir."),
        ("Mutlak değer nedir?",
         "Bir sayının sayı doğrusunda sıfıra olan uzaklığıdır. Uzaklık negatif olamayacağı için mutlak değer her zaman sıfır ya da pozitiftir. Örneğin eksi 7 nin de 7 nin de mutlak değeri 7 dir."),
        ("İki tam sayı arasında kaç tam sayı vardır?",
         "Uçlar dahilse büyük sayıdan küçük sayı çıkarılır ve 1 eklenir. Uçlar hariçse sonuçtan 2 çıkarılır. Örneğin eksi 4 ile 6 arasında uçlar dahil 11, uçlar hariç 9 tam sayı vardır."),
    ],
    "kontrol": [
        "Doğal sayılar ile tam sayılar arasındaki farkı bir örnekle açıklayabiliyorum.",
        "Değişme, birleşme ve dağılma özelliklerini bir hesabı kısaltmak için kullanabiliyorum.",
        "Bir tam sayının zıttını ve mutlak değerini yazabiliyorum.",
        "Negatif sayıları doğru sıralayabiliyorum.",
        "Çıkarmayı zıt sayıyı ekleyerek toplamaya çevirebiliyorum.",
        "Çarpma ve bölmede işaret kuralını birden çok çarpanla uygulayabiliyorum.",
        "İşlem önceliğini sırasıyla uygulayıp $-2^2$ ile $(-2)^2$ yi ayırt edebiliyorum.",
        "Negatif bir sayının bölümünden kalanı doğru bulabiliyorum.",
        "İki tam sayı arasındaki tam sayıları sayıp toplayabiliyorum.",
        "Verilen işaret bilgilerinden bir ifadenin işaretini bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["temel-kavramlar-konu-anlatimi-pdf", "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf", "rasyonel-sayilar-konu-anlatimi-pdf"],
}
