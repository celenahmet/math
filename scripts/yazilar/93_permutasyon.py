# scripts/yazilar/93_permutasyon.py — Permutasyon (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "permutasyon-konu-anlatimi-pdf",
    "baslik": "Permütasyon Konu Anlatımı PDF",
    "aciklama": "Permütasyon nedir? Çarpma ve toplama ilkesi, sıralı seçim, tekrarlı dizilim, yan yana ve ayrı durma, sabit yer, dairesel permütasyon ve şifre; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "sayma",
    "sinavlar": ["TYT", "AYT", "ALES", "KPSS"],
    "kapak": "permutasyon-konu-anlatimi-pdf",
    "kapak_alt": "Permütasyon: farklı renk ve biçimdeki nesneleri sıralı raflara dizen iki öğrenci",
    "ozet": "Permütasyon, nesnelerin sıralı dizilişlerini saymaktır. Beş kişinin bir fotoğraf için kaç farklı biçimde sıralanabileceği, bir yarışmada ilk üç derecenin kaç farklı biçimde belirlenebileceği ya da bir kelimenin harfleriyle kaç farklı dizilim yazılabileceği permütasyon sorularıdır. Bu yazıda çarpma ve toplama ilkelerini, sıralı seçimi, özdeş nesnelerin dizilimini, yan yana ve ayrı durma koşullarını, sabit yer koşullarını, dairesel permütasyonu ve şifre sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Sayma ilkeleri", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için faktöriyeli ve faktöriyelli ifadeleri sadeleştirmeyi biliyor olman yeterli.",
                "Faktöriyelin temeli için <a href=\"/blog/faktoriyel-konu-anlatimi-pdf/\">Faktöriyel Konu Anlatımı PDF</a> yazısına göz at."),
            "Permütasyon da dahil olmak üzere bütün sayma soruları iki temel ilkeye dayanır ve bu ilkeler iyi anlaşıldığında formüllerin çoğu ezber gerektirmez. <strong>Çarpma ilkesi:</strong> bir iş art arda yapılan adımlardan oluşuyorsa, her adımın seçenek sayıları çarpılır. <strong>Toplama ilkesi:</strong> bir iş birbirinden ayrık yollardan biriyle yapılabiliyorsa, yolların seçenek sayıları toplanır.",
            ornek(
                "Bir öğrencinin $3$ tişörtü ve $4$ pantolonu var.",
                "Bir tişört ve bir pantolondan oluşan kaç farklı kombin yapabileceğini bulalım.",
                "Önce tişört, sonra pantolon seçilir; iki adım art arda yapılır.",
                "Çarpma ilkesi: $3 \\cdot 4=12$ kombin. Her tişört, dört pantolonun her biriyle ayrı bir kombin oluşturur."),
            ornek(
                "Bir şehirden diğerine günde $5$ otobüs ve $3$ tren seferi var.",
                "Yolculuk için kaç farklı sefer seçilebileceğini bulalım.",
                "Yolcu ya otobüse ya trene biner; iki seçenek birbirinden ayrıktır.",
                "Toplama ilkesi: $5+3=8$ sefer. Burada çarpma yapılmaz, çünkü yolcu iki araca birden binmez; yalnızca birini seçer."),
            hap("Art arda adımlar: seçenekleri çarp.",
                "Ayrık seçenekler: seçenekleri topla."),
        ]},
        {"baslik": "Permütasyon nedir?", "icerik": [
            "Nesnelerin <strong>sıralı</strong> dizilişlerine permütasyon denir. Permütasyonda sıra önemlidir: ABC ile BAC aynı harflerden oluşsa da farklı dizilişlerdir. Kapaktaki raflara dizilen nesneler de bu fikri gösterir: aynı nesneler farklı sıralarla farklı dizilimler oluşturur. $n$ farklı nesnenin tamamının bir sıraya dizilme sayısı $n!$ dir.",
            "$n$ farklı nesneden $r$ tanesi seçilip sıraya dizildiğinde dizilim sayısı $P(n, r)$ ile gösterilir:",
            "$$P(n, r)=\\dfrac{n!}{(n-r)!}=n \\cdot (n-1) \\cdots (n-r+1)$$",
            "Son yazım, çarpma ilkesinin doğrudan sonucudur: birinci sıraya $n$, ikinci sıraya $n-1$ nesne gelebilir ve bu, $r$ sıra dolana kadar sürer.",
            tablo(["İfade", "Değer"], [
                ["$P(5, 5)$", "$5!=120$"],
                ["$P(5, 2)$", "$5 \\cdot 4=20$"],
                ["$P(8, 3)$", "$8 \\cdot 7 \\cdot 6=336$"],
                ["$P(n, 1)$", "$n$"],
            ]),
        ]},
        {"baslik": "Sıralı seçim", "icerik": [
            "Seçilen kişilerin ya da nesnelerin farklı görevleri, sıraları ya da dereceleri varsa seçim sıralıdır ve permütasyonla sayılır.",
            ornek(
                "$8$ kişilik bir kulüpte başkan, başkan yardımcısı ve sekreter seçilecek. Bir kişi yalnızca bir görev alabilir.",
                "Kaç farklı yönetim oluşturulabileceğini bulalım.",
                "Görevler farklı olduğu için sıra önemlidir.",
                "$P(8, 3)=8 \\cdot 7 \\cdot 6=336$ farklı yönetim."),
            ornek(
                "$10$ koşucunun katıldığı bir yarışta ilk üç derece belirlenecek.",
                "İlk üç derecenin kaç farklı biçimde oluşabileceğini bulalım.",
                "Birinci için $10$, ikinci için $9$, üçüncü için $8$ koşucu vardır.",
                "$10 \\cdot 9 \\cdot 8=720$ farklı sonuç."),
            dikkat(
                "Sırasız seçimi permütasyonla saymak.",
                "Görevleri aynı olan üç kişilik bir komisyon seçiliyorsa sıra önemli değildir ve sonuç $336$ değil, $336:3!=56$ dır. Sıranın önemli olup olmadığı her soruda ilk karar verilmesi gereken şeydir."),
        ]},
        {"baslik": "Özdeş nesnelerin dizilimi", "icerik": [
            "Dizilen nesnelerden bazıları birbirinin aynısıysa, bu nesnelerin kendi aralarında yer değiştirmesi yeni bir dizilim oluşturmaz. Bu yüzden toplam dizilim sayısı, özdeş grupların kendi içindeki sıralama sayılarına bölünür:",
            "$$\\dfrac{n!}{n_1! \\cdot n_2! \\cdots n_k!}$$",
            ornek(
                "KAPAK kelimesinin harfleri kullanılarak beş harfli diziler yazılacak.",
                "Kaç farklı dizi yazılabileceğini bulalım.",
                "Beş harfte iki K ve iki A vardır; P bir tanedir.",
                "Dizi sayısı: $\\dfrac{5!}{2! \\cdot 2!}=\\dfrac{120}{4}=30$."),
            ornek(
                "ANANAS kelimesinin harfleri verilsin.",
                "Harflerle kaç farklı altı harfli dizi yazılabileceğini bulalım.",
                "Üç A, iki N ve bir S vardır.",
                "Dizi sayısı: $\\dfrac{6!}{3! \\cdot 2!}=\\dfrac{720}{12}=60$."),
            "Aynı kural renkli toplar ya da bayraklar için de geçerlidir: $3$ kırmızı ve $2$ mavi özdeş top bir sıraya $\\dfrac{5!}{3! \\cdot 2!}=10$ farklı biçimde dizilir.",
        ]},
        {"baslik": "Belirli nesneler yan yana", "icerik": [
            "Belirli nesnelerin yan yana olması isteniyorsa bu nesneler tek bir blok gibi düşünülür. Önce blok ile diğer nesneler sıralanır, sonra bloğun içindeki nesneler kendi aralarında sıralanır.",
            ornek(
                "A ve B nin de aralarında bulunduğu $5$ kişi bir sıraya dizilecek.",
                "A ile B nin yan yana olduğu kaç dizilim olduğunu bulalım.",
                "A ile B yi tek blok sayalım: blok ve diğer $3$ kişi, toplam $4$ birim; $4!=24$ dizilim.",
                "Blok içinde A ile B yer değiştirebilir: $2!=2$.",
                "Toplam: $24 \\cdot 2=48$ dizilim."),
            ornek(
                "$3$ matematik ve $2$ fizik kitabı bir rafa dizilecek. Kitapların hepsi farklıdır ve aynı dersin kitapları yan yana olacak.",
                "Kaç farklı dizilim olduğunu bulalım.",
                "İki ders bloğu kendi aralarında $2!$ biçimde sıralanır.",
                "Matematik kitapları kendi içinde $3!$, fizik kitapları $2!$ biçimde sıralanır.",
                "Toplam: $2! \\cdot 3! \\cdot 2!=2 \\cdot 6 \\cdot 2=24$ dizilim."),
        ]},
        {"baslik": "Belirli nesneler yan yana olmasın", "icerik": [
            "\"Yan yana olmasın\" koşulu doğrudan sayılmaz; tümleyen yoluyla hesaplanır. Bütün dizilimlerin sayısından yan yana oldukları dizilimlerin sayısı çıkarılır.",
            ornek(
                "A ve B nin de aralarında bulunduğu $5$ kişi bir sıraya dizilecek.",
                "A ile B nin yan yana olmadığı kaç dizilim olduğunu bulalım.",
                "Bütün dizilimler: $5!=120$.",
                "Yan yana oldukları dizilimler: $48$.",
                "Yan yana olmadıkları dizilimler: $120-48=72$."),
            "<h3>Araya yerleştirme yöntemi</h3>",
            "Birden fazla nesnenin hiçbirinin yan yana gelmemesi isteniyorsa diğer nesneler önce dizilir ve istenmeyen nesneler aralara yerleştirilir. Örneğin $3$ erkek ve $2$ kız öğrenci, kızlar yan yana gelmeyecek biçimde dizilecekse önce erkekler $3!=6$ biçimde dizilir. Erkeklerin arasında ve iki ucunda $4$ boşluk vardır; kızlar bu boşluklardan ikisine $P(4, 2)=12$ biçimde yerleşir. Toplam $6 \\cdot 12=72$ dizilim bulunur.",
        ]},
        {"baslik": "Aralarında belirli sayıda kişi", "icerik": [
            "İki kişinin arasında tam olarak belirli sayıda kişi bulunması isteniyorsa önce bu iki kişinin yerleşebileceği konum çiftleri sayılır. Sonra iki kişinin kendi aralarındaki sırası ve kalan kişilerin dizilimi çarpılır.",
            ornek(
                "A ve B nin de aralarında bulunduğu $5$ kişi bir sıraya dizilecek.",
                "A ile B nin arasında tam olarak bir kişi bulunan dizilimleri sayalım.",
                "A ile B arasında bir yer boşluk bırakan konum çiftleri: $1$ ile $3$, $2$ ile $4$, $3$ ile $5$; toplam $3$ çift.",
                "Her çiftte A ile B yer değiştirebilir: $3 \\cdot 2=6$.",
                "Kalan $3$ kişi kalan yerlere $3!=6$ biçimde dizilir. Toplam: $6 \\cdot 6=36$ dizilim."),
        ]},
        {"baslik": "Dönüşümlü dizilimler", "icerik": [
            "İki grubun üyelerinin sırayla, dönüşümlü olarak dizilmesi isteniyorsa önce dizilimin kalıbı belirlenir, sonra her grup kendi yerlerine sıralanır.",
            ornek(
                "$3$ kız ve $3$ erkek öğrenci bir sıraya kız ve erkek dönüşümlü olacak biçimde dizilecek.",
                "Kaç farklı dizilim olduğunu bulalım.",
                "İki kalıp vardır: kızla başlayan ya da erkekle başlayan.",
                "Her kalıpta kızlar kendi yerlerine $3!$, erkekler kendi yerlerine $3!$ biçimde dizilir.",
                "Toplam: $2 \\cdot 3! \\cdot 3!=2 \\cdot 6 \\cdot 6=72$ dizilim."),
            dikkat(
                "Kalıp sayısını unutmak.",
                "Gruplar eşit sayıdaysa dizilim iki kalıpla başlayabilir. Gruplardan biri bir kişi fazlaysa, örneğin $3$ kız ve $2$ erkek, yalnızca kızla başlayan kalıp mümkündür."),
        ]},
        {"baslik": "Sayı yazma soruları", "icerik": [
            "Rakamları farklı sayıların yazılması da bir permütasyon sorusudur: basamaklar sıralı yerlerdir ve rakamlar bu yerlere dizilir. Ek koşullar önce kısıtlı basamağa uygulanır.",
            ornek(
                "$1$, $2$, $3$, $4$ ve $5$ rakamlarıyla rakamları farklı üç basamaklı sayılar yazılacak.",
                "Kaç sayı yazılabileceğini ve bunlardan kaçının $300$ den büyük olduğunu bulalım.",
                "Bütün sayılar: $P(5, 3)=5 \\cdot 4 \\cdot 3=60$.",
                "$300$ den büyük olması için yüzler basamağı $3$, $4$ ya da $5$ olmalıdır: $3$ seçenek.",
                "Kalan iki basamak kalan $4$ rakamdan $4 \\cdot 3=12$ biçimde dolar. Toplam: $3 \\cdot 12=36$ sayı."),
        ]},
        {"baslik": "Izgarada en kısa yollar", "icerik": [
            "Bir ızgarada yalnızca sağa ve yukarı hareket ederek bir köşeden karşı köşeye giden yolların sayısı, özdeş nesnelerin dizilimi olarak sayılır. Her yol, belirli sayıda sağ ve yukarı adımın bir sıralamasıdır.",
            ornek(
                "Bir ızgarada A noktasından B noktasına gitmek için $3$ adım sağa ve $2$ adım yukarı gitmek gerekiyor. Yalnızca sağa ve yukarı hareket edilebiliyor.",
                "Kaç farklı en kısa yol olduğunu bulalım.",
                "Her yol $3$ tane S ve $2$ tane Y harfinden oluşan bir dizidir; örneğin SSYSY.",
                "Özdeş harflerin dizilimi: $\\dfrac{5!}{3! \\cdot 2!}=10$ yol."),
            "Bu fikir, yol sorularını ezbere gerek kalmadan çözmeyi sağlar: sağ ve yukarı adımların sayısı belirlenir ve özdeş nesnelerin dizilim formülü uygulanır.",
        ]},
        {"baslik": "Sabit yer koşulları", "icerik": [
            "Bir nesnenin belirli bir yerde olması isteniyorsa önce o yer doldurulur, sonra kalan nesneler kalan yerlere dizilir.",
            ornek(
                "A nın da aralarında bulunduğu $5$ kişi bir sıraya dizilecek.",
                "A nın en başta olduğu ve A nın en başta, B nin en sonda olduğu dizilimleri sayalım.",
                "A en başta: kalan $4$ kişi kalan $4$ yere $4!=24$ biçimde dizilir.",
                "A en başta ve B en sonda: kalan $3$ kişi ortadaki $3$ yere $3!=6$ biçimde dizilir."),
            ornek(
                "A nın da aralarında bulunduğu $5$ kişi bir sıraya dizilecek.",
                "A nın uçlardan birinde olduğu dizilimleri sayalım.",
                "A için $2$ uç vardır. Her durumda kalan $4$ kişi $4!=24$ biçimde dizilir.",
                "Toplam: $2 \\cdot 24=48$ dizilim."),
        ]},
        {"baslik": "Dairesel permütasyon", "icerik": [
            "Nesneler bir çember etrafına dizildiğinde başlangıç noktası yoktur; bütün nesneler aynı yönde bir yer kaydırıldığında dizilim değişmez. Bu yüzden $n$ farklı nesnenin bir çember etrafındaki dizilim sayısı $(n-1)!$ dir.",
            ornek(
                "$5$ kişi yuvarlak bir masanın etrafına oturacak.",
                "Kaç farklı oturma düzeni olduğunu bulalım.",
                "Bir kişiyi sabitleyip diğerlerini ona göre dizelim: $(5-1)!=4!=24$.",
                "Düz bir sıraya dizilseydi $5!=120$ dizilim olurdu; her dairesel düzen $5$ farklı düz sıraya karşılık gelir: $120:5=24$."),
            "Kolye ve anahtarlık gibi ters çevrilebilen nesnelerde ise saat yönündeki ve ters yöndeki dizilim aynı sayılır. Bu durumda sonuç yeniden $2$ ye bölünür: $n$ farklı boncuklu bir kolye $\\dfrac{(n-1)!}{2}$ biçimde dizilir. $5$ farklı boncuk için bu sayı $12$ dir. Dairesel dizilimde de blok yöntemi kullanılır: $5$ kişiden A ile B nin yuvarlak masada yan yana oturduğu düzenler, blok ve kalan $3$ kişiden oluşan $4$ birimin dairesel dizilimi $(4-1)!=6$ ile blok içi sıralama $2$ çarpılarak $12$ bulunur.",
        ]},
        {"baslik": "Şifre ve tekrarlı seçim", "icerik": [
            "Aynı nesne birden fazla kez kullanılabiliyorsa her yer için seçenek sayısı değişmez ve çarpma ilkesi doğrudan uygulanır. Şifre soruları bunun en tipik örneğidir.",
            ornek(
                "Dört haneli bir şifrenin her hanesine $0$ ile $9$ arasındaki rakamlardan biri yazılabiliyor.",
                "Rakamlar tekrar edebildiğinde ve edemediğinde kaç farklı şifre olduğunu bulalım.",
                "Tekrar serbest: her hane için $10$ seçenek; $10^4=10000$ şifre.",
                "Tekrar yok: $10 \\cdot 9 \\cdot 8 \\cdot 7=5040$ şifre. Şifre üç ya da dört haneli olabiliyorsa ve tekrar serbestse, iki durum ayrık olduğu için toplama ilkesiyle $10^3+10^4=11000$ şifre bulunur."),
            "Şifrede ilk hanenin $0$ olabildiğine dikkat edilmelidir; bu yüzden sayı yazma sorularından farklıdır. Rakamlarla sayı yazma soruları <a href=\"/blog/sayi-basamaklari-konu-anlatimi-pdf/\">Sayı Basamakları Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Kelime soruları", "icerik": [
            "Bir kelimenin harfleriyle yazılabilecek diziler, harflerin hepsi farklıysa $n!$ ile, özdeş harfler varsa bölmeli formülle sayılır. Ek koşullar blok ya da sabit yer yöntemiyle eklenir. Harflerin bir kısmı özdeşse önce bölmeli formül yazılır, sonra koşul uygulanır.",
            ornek(
                "KALEM kelimesinin harfleri verilsin.",
                "Harflerin farklı dizilişlerini ve sesli harflerin yan yana olduğu dizilişleri sayalım.",
                "Beş harf de farklıdır: $5!=120$ dizi.",
                "Sesli harfler A ve E dir. Bunları bir blok sayalım: blok ve $3$ sessiz harf, $4!=24$ dizilim; blok içi $2!=2$.",
                "Sesli harflerin yan yana olduğu diziler: $24 \\cdot 2=48$."),
        ]},
        {"baslik": "Sınavda permütasyon", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) permütasyon sayma ilkeleri, sıralı seçim, yan yana ve sabit yer koşulları biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) özdeş nesneler, dairesel permütasyon ve koşullu dizilimler de sorulur; <strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde sayma soruları sayısal akıl yürütmenin parçasıdır."),
            "Bir sayma sorusunda üç soruyu sırayla sor: sıra önemli mi, tekrar serbest mi, özel bir koşul var mı? İlk soru permütasyon ile kombinasyonu ayırır, ikincisi formülü seçtirir, üçüncüsü blok, tümleyen ya da sabit yer yöntemlerinden hangisinin kullanılacağını belirler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Sırasız seçimi permütasyonla saymak", "Sıra önemsizse kombinasyon"],
                ["Özdeş nesneleri farklı saymak", "Özdeşlerin faktöriyeline böl"],
                ["Blok içi sıralamayı unutmak", "Blok içini de sırala"],
                ["\"Yan yana olmasın\"ı doğrudan saymak", "Tümden çıkar"],
                ["Dairesel dizilimi $n!$ almak", "$(n-1)!$"],
                ["Şifrede ilk haneye $0$ koymamak", "Şifrede $0$ ilk hanede olabilir"],
            ]),
            "Bu hataların çoğu, sorudaki koşulları dikkatle okumamaktan doğar. Küçük sayılarla, örneğin üç nesneyle, dizilimleri tek tek yazıp formülün doğru sayı verip vermediğini denemek, hangi yöntemin doğru olduğunu hızlıca gösterir.",
        ]},
    ],
    "sss": [
        ("Permütasyon nedir?",
         "Nesnelerin sıralı dizilişleridir. n farklı nesnenin tamamı n faktöriyel biçimde, r tanesi ise n faktöriyelin n eksi r faktöriyele bölümü kadar biçimde sıralanır."),
        ("Çarpma ilkesi ile toplama ilkesi arasındaki fark nedir?",
         "Art arda yapılan adımların seçenekleri çarpılır. Birbirinden ayrık seçeneklerden biri seçiliyorsa seçenekler toplanır."),
        ("Özdeş nesneler nasıl dizilir?",
         "Toplam nesne sayısının faktöriyeli, her özdeş grubun eleman sayısının faktöriyeline bölünür. KAPAK kelimesinin harfleriyle 30 farklı dizi yazılır."),
        ("Belirli kişilerin yan yana olması nasıl sayılır?",
         "Bu kişiler tek bir blok sayılır. Blok ve diğerleri sıralanır, sonra blok içindeki kişilerin kendi aralarındaki sıralamaları ile çarpılır."),
        ("Dairesel permütasyon nedir?",
         "n farklı nesnenin bir çember etrafına dizilmesidir. Başlangıç noktası olmadığı için dizilim sayısı n eksi bir faktöriyeldir."),
        ("Şifre sorularında rakam tekrarı neyi değiştirir?",
         "Tekrar serbestse her hane için seçenek sayısı aynı kalır. Tekrar yoksa her hanede bir önceki haneden bir eksik seçenek vardır."),
        ("Izgarada en kısa yol sayısı nasıl bulunur?",
         "Gereken sağ ve yukarı adım sayıları belirlenir. Toplam adım sayısının faktöriyeli, sağ ve yukarı adım sayılarının faktöriyellerine bölünür."),
    ],
    "kontrol": [
        "Çarpma ve toplama ilkelerini doğru yerde kullanabiliyorum.",
        "Permütasyonun sıralı diziliş olduğunu açıklayabiliyorum.",
        "Sıralı seçim sayısını hesaplayabiliyorum.",
        "Özdeş nesnelerin dizilim sayısını bulabiliyorum.",
        "Belirli nesneleri blok yöntemiyle yan yana dizebiliyorum.",
        "Yan yana olmama koşulunu tümleyenle hesaplayabiliyorum.",
        "Araya yerleştirme yöntemini kullanabiliyorum.",
        "Sabit yer koşullu dizilimleri sayabiliyorum.",
        "Dairesel permütasyon sayısını bulabiliyorum.",
        "Tekrarlı ve tekrarsız şifre sayılarını hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["faktoriyel-konu-anlatimi-pdf", "kombinasyon-konu-anlatimi-pdf", "olasilik-konu-anlatimi-pdf"],
}
