# scripts/yazilar/88_hareket_problemleri.py — Hareket Problemleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "hareket-problemleri-konu-anlatimi-pdf",
    "baslik": "Hareket Problemleri Konu Anlatımı PDF",
    "aciklama": "Hareket problemleri nasıl çözülür? Yol, hız, zaman; birim dönüşümü, karşılaşma, yetişme, ortalama hız, akıntı, tren ve pist soruları; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "hareket-problemleri-konu-anlatimi-pdf",
    "kapak_alt": "Hareket problemleri: ahşap bir yol üzerinde oyuncak arabalarla yol, zaman ve hız ilişkisini inceleyen iki öğrenci",
    "ozet": "Hareket problemleri tek bir bağıntı üzerine kuruludur: alınan yol, hız ile zamanın çarpımıdır. Soruların zorluğu bu bağıntıdan değil, iki hareketlinin birbirine göre durumundan gelir: birbirine doğru mu, aynı yönde mi, zıt yönde mi gidiyorlar? Bu yazıda temel bağıntıyı, birim dönüşümlerini, karşılaşma, yetişme ve uzaklaşma sorularını, ortalama hızı, gidiş dönüş sorularını, akıntı, tren ve dairesel pist problemlerini ve geç kalma sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Temel bağıntı: yol, hız, zaman", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birinci dereceden denklem kurmayı ve doğru ile ters orantıyı biliyor olman yeterli.",
                "Orantı ilişkileri için <a href=\"/blog/dogru-oranti-ve-ters-oranti/\">Doğru Orantı ve Ters Orantı</a> yazısına göz at."),
            "Sabit hızla hareket eden bir cismin aldığı yol, hızı ile hareket süresinin çarpımıdır:",
            "$$\\text{Yol}=\\text{Hız} \\cdot \\text{Zaman}$$",
            "Bu bağıntıdan diğer iki biçim de çıkar: hız, yolun zamana bölümüdür; zaman, yolun hıza bölümüdür. Üç büyüklükten ikisi biliniyorsa üçüncüsü bulunur. Hız sabitken yol ile zaman doğru orantılı, yol sabitken hız ile zaman ters orantılıdır.",
            tablo(["Aranan", "Bağıntı"], [
                ["Yol", "Hız çarpı zaman"],
                ["Hız", "Yol bölü zaman"],
                ["Zaman", "Yol bölü hız"],
            ]),
            hap("Yol, hız ile zamanın çarpımıdır.",
                "Üç büyüklük aynı birim sisteminde olmalıdır."),
        ]},
        {"baslik": "Birim dönüşümleri", "icerik": [
            "Hız kilometre bölü saat olarak verilip süre dakika olarak verilmişse ya da tersi söz konusuysa, işleme başlamadan önce birimler uyumlu hâle getirilir. En sık kullanılan dönüşümler şunlardır: $1$ saat $60$ dakika, $1$ dakika $60$ saniye, $1$ kilometre $1000$ metredir.",
            ornek(
                "Bir aracın hızı saatte $72$ kilometre olsun.",
                "Bu hızı metre bölü saniye olarak yazalım.",
                "$72$ kilometre $72000$ metre, $1$ saat $3600$ saniyedir.",
                "Hız: $72000:3600=20$ metre bölü saniye."),
            ornek(
                "Saatte $90$ kilometre hızla giden bir araç $20$ dakika yol alıyor.",
                "Aldığı yolu bulalım.",
                "$20$ dakika, $\\dfrac{20}{60}=\\dfrac{1}{3}$ saattir.",
                "Yol: $90 \\cdot \\dfrac{1}{3}=30$ kilometre."),
            dikkat(
                "Birimleri karıştırmak.",
                "Saatte $90$ kilometre hızı $20$ dakikayla doğrudan çarpmak $1800$ kilometre gibi anlamsız bir sonuç verir. Süre önce saate çevrilmelidir."),
        ]},
        {"baslik": "Temel sorular", "icerik": [
            "Tek bir hareketlinin yolu, hızı ya da süresi sorulduğunda temel bağıntı doğrudan uygulanır.",
            ornek(
                "Bir araç $240$ kilometrelik yolu $3$ saatte alıyor.",
                "Aracın hızını bulalım.",
                "Hız: $240:3=80$ kilometre bölü saat. Yani araç her saat $80$ kilometre yol alır."),
            ornek(
                "Saatte $60$ kilometre hızla giden bir araç $150$ kilometrelik yolu alıyor.",
                "Yolun ne kadar sürdüğünü bulalım.",
                "Zaman: $150:60=2.5$ saat.",
                "$0.5$ saat $30$ dakika olduğu için süre $2$ saat $30$ dakikadır."),
            "Ondalıklı saatleri dakikaya çevirirken ondalık kısım $60$ ile çarpılır; dakikayı saate çevirirken ise $60$ a bölünür. $2.5$ saat, $2$ saat $30$ dakikadır; $2$ saat $50$ dakika değildir.",
        ]},
        {"baslik": "Birbirine doğru hareket: karşılaşma", "icerik": [
            "İki araç aralarındaki mesafenin iki ucundan aynı anda birbirine doğru hareket ettiğinde, aralarındaki mesafe her saat hızlarının toplamı kadar kısalır. Bu yüzden karşılaşma süresi, mesafenin hızların toplamına bölünmesiyle bulunur.",
            ornek(
                "Aralarında $420$ kilometre olan iki şehirden iki araç aynı anda birbirine doğru yola çıkıyor. Hızları saatte $60$ ve $80$ kilometre.",
                "Kaç saat sonra karşılaşacaklarını ve karşılaşma noktasını bulalım.",
                "Mesafe her saat $60+80=140$ kilometre kısalır. Süre: $420:140=3$ saat.",
                "Birinci araç $3$ saatte $60 \\cdot 3=180$ kilometre, ikinci araç $80 \\cdot 3=240$ kilometre gider.",
                "Karşılaşma noktası birinci şehirden $180$ kilometre uzaktadır. Kontrol: $180+240=420$."),
            dikkat(
                "Karşılaşmada hızların farkını kullanmak.",
                "Birbirine doğru giden araçlarda mesafe iki araç tarafından birlikte kapatılır; hızlar toplanır. Hızların farkı, aynı yönde giden araçlar için kullanılır."),
            hap("Birbirine doğru giden iki aracın karşılaşma süresi, aradaki mesafenin hızların toplamına bölümüdür."),
        ]},
        {"baslik": "Farklı saatlerde yola çıkan araçlar", "icerik": [
            "Araçlar aynı anda yola çıkmıyorsa önce erken çıkan aracın tek başına aldığı yol hesaplanır ve mesafeden çıkarılır. Kalan mesafe, ikisi birlikte hareket ederken karşılaşma ya da yetişme kuralına göre kapatılır.",
            ornek(
                "Aralarında $480$ kilometre olan iki şehirden birinden saat 09.00'da saatte $60$ kilometre hızla bir araç, diğerinden saat 10.00'da saatte $80$ kilometre hızla başka bir araç birbirine doğru yola çıkıyor.",
                "Araçların saat kaçta karşılaşacağını bulalım.",
                "Birinci araç $1$ saat önce çıktığı için bu sürede $60$ kilometre yol alır; kalan mesafe $480-60=420$ kilometredir.",
                "Saat 10.00'dan itibaren mesafe her saat $60+80=140$ kilometre kısalır: $420:140=3$ saat.",
                "Araçlar saat 13.00'te karşılaşır. Kontrol: birinci araç $4$ saatte $240$, ikinci araç $3$ saatte $240$ kilometre gider; toplam $480$."),
        ]},
        {"baslik": "Yolun bölümlerinde farklı hızlar", "icerik": [
            "Bir yolun farklı bölümleri farklı hızlarla gidildiğinde her bölümün süresi ayrı ayrı hesaplanır. Ortalama hız yine toplam yolun toplam zamana bölümüdür.",
            ornek(
                "Bir araç $360$ kilometrelik bir yolun ilk yarısını saatte $60$, ikinci yarısını saatte $90$ kilometre hızla gidiyor.",
                "Aracın bütün yol boyunca ortalama hızını bulalım.",
                "Her yarı $180$ kilometredir. İlk yarı $180:60=3$ saat, ikinci yarı $180:90=2$ saat sürer.",
                "Toplam süre $5$ saat, toplam yol $360$ kilometre.",
                "Ortalama hız: $360:5=72$ kilometre bölü saat; hızların ortalaması olan $75$ değil."),
            "Yolun eşit bölümleri farklı hızlarla gidildiğinde ortalama hız her zaman hızların basit ortalamasından küçük olur, çünkü yavaş gidilen bölümde daha fazla zaman geçer. Buna karşılık eşit <strong>süreler</strong> boyunca farklı hızlarla gidildiğinde ortalama hız, hızların basit ortalamasına eşittir.",
        ]},
        {"baslik": "Aynı yönde hareket: yetişme", "icerik": [
            "Aynı yönde giden iki araçtan arkadaki daha hızlıysa, aradaki mesafe her saat hızlarının farkı kadar kapanır. Yetişme süresi, aradaki mesafenin hız farkına bölünmesidir.",
            ornek(
                "Bir araç saatte $60$ kilometre hızla bir noktadan yola çıkıyor. $2$ saat sonra aynı noktadan ikinci bir araç saatte $90$ kilometre hızla aynı yöne yola çıkıyor.",
                "İkinci aracın birinciye kaç saatte yetişeceğini bulalım.",
                "İkinci araç yola çıktığında birinci araç $60 \\cdot 2=120$ kilometre öndedir.",
                "Aradaki mesafe her saat $90-60=30$ kilometre kapanır: $120:30=4$ saat.",
                "Yetişme noktası başlangıçtan $90 \\cdot 4=360$ kilometre uzaktadır. Kontrol: birinci araç $6$ saatte $360$ kilometre gider."),
            hap("Aynı yönde gidenlerde yetişme süresi, aradaki mesafenin hız farkına bölümüdür."),
        ]},
        {"baslik": "Zıt yönde hareket: uzaklaşma", "icerik": [
            "Aynı noktadan zıt yönlere giden iki araç arasındaki mesafe her saat hızlarının toplamı kadar büyür. Belirli bir süre sonraki aralarındaki mesafe, hızların toplamı ile sürenin çarpımıdır.",
            ornek(
                "Aynı noktadan iki araç zıt yönlere saatte $45$ ve $55$ kilometre hızla yola çıkıyor.",
                "$4$ saat sonra aralarındaki mesafeyi bulalım.",
                "Mesafe her saat $45+55=100$ kilometre artar.",
                "$4$ saat sonra: $100 \\cdot 4=400$ kilometre."),
            tablo(["Durum", "Aradaki mesafe her saat"], [
                ["Birbirine doğru", "Hızların toplamı kadar kısalır"],
                ["Zıt yönde", "Hızların toplamı kadar büyür"],
                ["Aynı yönde", "Hızların farkı kadar değişir"],
            ]),
        ]},
        {"baslik": "Ortalama hız", "icerik": [
            "Ortalama hız, toplam yolun toplam zamana bölümüdür. Farklı hızlarla gidilen yollarda ortalama hız, hızların basit ortalaması değildir; çünkü araç yavaş gittiği bölümde daha uzun süre kalır.",
            "$$\\text{Ortalama hız}=\\dfrac{\\text{Toplam yol}}{\\text{Toplam zaman}}$$",
            ornek(
                "Bir araç $120$ kilometrelik bir yolu saatte $60$ kilometre hızla gidiyor ve aynı yolu saatte $40$ kilometre hızla dönüyor.",
                "Aracın gidiş dönüş boyunca ortalama hızını bulalım.",
                "Gidiş süresi: $120:60=2$ saat. Dönüş süresi: $120:40=3$ saat.",
                "Toplam yol $240$ kilometre, toplam zaman $5$ saat.",
                "Ortalama hız: $240:5=48$ kilometre bölü saat."),
            dikkat(
                "Hızların ortalamasını almak.",
                "$60$ ile $40$ ın ortalaması olan $50$ yanlıştır. Araç yavaş gittiği dönüşte daha uzun süre kaldığı için ortalama hız yavaş hıza daha yakındır: $48$."),
            hap("Yolun yarısı $v_1$, diğer yarısı $v_2$ hızla gidilirse ortalama hız $\\dfrac{2v_1v_2}{v_1+v_2}$ olur.", "Bu değer hızların basit ortalamasından küçüktür."),
        ]},
        {"baslik": "Gidiş dönüş soruları", "icerik": [
            "Gidiş ve dönüş hızları ile toplam süre verildiğinde yol, bilinmeyen olarak yazılır. Her yönün süresi yolun o yönün hızına bölümüdür ve süreler toplanır.",
            ornek(
                "Bir araç A şehrinden B şehrine saatte $80$ kilometre hızla gidiyor, saatte $120$ kilometre hızla dönüyor. Gidiş dönüş toplam $5$ saat sürüyor.",
                "İki şehir arasındaki uzaklığı bulalım.",
                "Uzaklık $d$ olsun: $\\dfrac{d}{80}+\\dfrac{d}{120}=5$.",
                "Ortak payda $240$: $\\dfrac{3d+2d}{240}=5$, yani $5d=1200$ ve $d=240$ kilometre.",
                "Kontrol: gidiş $3$ saat, dönüş $2$ saat; toplam $5$ saat."),
        ]},
        {"baslik": "Akıntı problemleri", "icerik": [
            "Bir tekne akıntı yönünde giderken akıntı onu iter ve hızı artar; akıntıya karşı giderken yavaşlar. Teknenin durgun sudaki hızı $v$, akıntının hızı $a$ ise:",
            tablo(["Yön", "Hız"], [
                ["Akıntı yönünde", "$v+a$"],
                ["Akıntıya karşı", "$v-a$"],
            ]),
            ornek(
                "Durgun suda saatte $20$ kilometre hızla giden bir tekne, akıntı hızı saatte $4$ kilometre olan bir nehirde $48$ kilometre akıntı yönünde gidip aynı yolu geri dönüyor.",
                "Gidiş dönüşün toplam süresini bulalım.",
                "Akıntı yönünde hız $24$, akıntıya karşı hız $16$ kilometre bölü saattir.",
                "Gidiş: $48:24=2$ saat. Dönüş: $48:16=3$ saat.",
                "Toplam süre $5$ saattir."),
            "Akıntıda motorunu çalıştırmadan sürüklenen bir sal ise yalnızca akıntı hızıyla hareket eder. Akıntı yönündeki ve akıntıya karşı hızlar biliniyorsa, teknenin durgun sudaki hızı bu iki hızın ortalaması, akıntı hızı ise farklarının yarısıdır: $\\dfrac{24+16}{2}=20$ ve $\\dfrac{24-16}{2}=4$.",
        ]},
        {"baslik": "Tren, köprü ve tünel problemleri", "icerik": [
            "Bir tren bir köprüyü ya da tüneli tamamen geçtiğinde, trenin önü köprünün başından köprünün sonunu geçene kadar değil, trenin arkası köprüden çıkana kadar hareket eder. Bu yüzden alınan yol, köprünün uzunluğu ile trenin kendi uzunluğunun toplamıdır. Tünel sorularında da aynı kural geçerlidir: trenin tamamen tünelden çıkması için tünel ile trenin uzunluklarının toplamı kadar yol alması gerekir.",
            ornek(
                "Uzunluğu $200$ metre olan bir tren saniyede $20$ metre hızla $800$ metrelik bir köprüyü geçiyor.",
                "Trenin köprüyü tamamen geçme süresini bulalım.",
                "Alınan yol: $800+200=1000$ metre.",
                "Süre: $1000:20=50$ saniye."),
            "Aynı tren yol kenarındaki bir direğin önünden geçerken yalnızca kendi uzunluğu kadar yol alır: $200:20=10$ saniye.",
            dikkat(
                "Trenin uzunluğunu unutmak.",
                "Köprünün uzunluğunu hıza bölmek $800:20=40$ saniye verir. Bu süre trenin önünün köprünün sonuna ulaştığı andır; trenin tamamı köprüden ancak $10$ saniye sonra çıkar."),
        ]},
        {"baslik": "Dairesel pist problemleri", "icerik": [
            "Dairesel bir pistte aynı noktadan aynı anda yola çıkan iki koşucunun ilk kez buluşması, aralarındaki farkın bir tur olmasıyla gerçekleşir. Aynı yönde koşuyorlarsa hızlı olan yavaşı bir tur geride bıraktığında, zıt yönde koşuyorlarsa ikisinin aldığı yolların toplamı bir tur olduğunda buluşurlar.",
            ornek(
                "Çevresi $400$ metre olan bir pistte iki koşucu aynı noktadan aynı anda saniyede $6$ ve $4$ metre hızla koşmaya başlıyor.",
                "Aynı yönde ve zıt yönde koştuklarında kaç saniye sonra ilk kez buluşacaklarını bulalım.",
                "Aynı yönde: aradaki fark her saniye $6-4=2$ metre artar; bir tur fark için $400:2=200$ saniye.",
                "Zıt yönde: her saniye birlikte $6+4=10$ metre yol alırlar; bir tur için $400:10=40$ saniye."),
            "İlk buluşmadan sonra koşucular aynı aralıklarla yeniden buluşur, çünkü her buluşmada durum başlangıçtakiyle aynıdır. Aynı yönde koşarlarsa her $200$ saniyede bir buluşurlar; örneğin ilk $1000$ saniyede $5$ kez yan yana gelirler.",
        ]},
        {"baslik": "Geç kalma ve erken varma", "icerik": [
            "Aynı yolun iki farklı hızla alınmasıyla oluşan süre farkı verildiğinde yol bilinmeyen olarak yazılır. İki sürenin farkı, verilen dakika farkına eşitlenir; dakikalar önce saate çevrilir.",
            ornek(
                "Bir öğrenci okula saatte $5$ kilometre hızla yürürse $6$ dakika geç kalıyor, saatte $6$ kilometre hızla yürürse $4$ dakika erken varıyor.",
                "Okulun uzaklığını bulalım.",
                "İki süre arasındaki fark $6+4=10$ dakika, yani $\\dfrac{1}{6}$ saattir.",
                "Denklem: $\\dfrac{d}{5}-\\dfrac{d}{6}=\\dfrac{1}{6}$, yani $\\dfrac{d}{30}=\\dfrac{1}{6}$ ve $d=5$ kilometre.",
                "Kontrol: $5$ kilometre $5$ hızla $60$ dakika, $6$ hızla $50$ dakika sürer; fark $10$ dakikadır."),
            hap("Okula uzaklığı $2$ kilometre olan bir öğrenci saatte $4$ kilometre hızla yürürse $30$ dakikada, saatte $12$ kilometre hızla bisiklet sürerse $10$ dakikada varır.", gunluk=True),
        ]},
        {"baslik": "Yol zaman grafikleri", "icerik": [
            "Hareket bazen bir yol zaman grafiğiyle verilir. Yatay eksen zamanı, dikey eksen alınan yolu gösterir. Sabit hızlı bir hareketin grafiği bir doğrudur ve doğrunun dikliği hızı verir: doğru ne kadar dikse hız o kadar büyüktür.",
            "Grafik yatay bir parça içeriyorsa araç o sürede durmuştur, çünkü zaman ilerlerken alınan yol değişmemiştir. İki hareketlinin grafikleri kesişiyorsa kesişme noktası, ikisinin aynı anda aynı yerde olduğu anı, yani karşılaşmayı ya da yetişmeyi gösterir.",
        ]},
        {"baslik": "Sınavda hareket problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) hareket problemleri karşılaşma, yetişme, ortalama hız, akıntı ve tren soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde hareket soruları grafik yorumlama ve sayısal akıl yürütmeyle birlikte de gelebilir."),
            "Bir hareket sorusunda ilk iş birimleri kontrol etmek, ikinci iş iki hareketlinin birbirine göre durumunu belirlemektir. Birbirine doğru ve zıt yönde hareketlerde hızlar toplanır, aynı yönde hareketlerde hızların farkı alınır. Bu karar doğru verildiğinde denklem tek satırda kurulur.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Saati dakikayla karıştırmak", "Önce birimleri eşitle"],
                ["Karşılaşmada hız farkını almak", "Birbirine doğru hızlar toplanır"],
                ["Yetişmede hızları toplamak", "Aynı yönde hız farkı alınır"],
                ["Ortalama hızı hızların ortalaması sanmak", "Toplam yol bölü toplam zaman"],
                ["Trenin uzunluğunu unutmak", "Yol, köprü artı tren"],
                ["$2.5$ saati $2$ saat $50$ dakika sanmak", "$2$ saat $30$ dakika"],
            ]),
            "Bu hataların çoğu, iki hareketlinin birbirine göre durumunu gözden kaçırmaktan ya da birimleri kontrol etmemekten doğar. Soruyu okurken hareketi bir şekil üzerinde çizmek, hangi hızların toplanıp hangilerinin çıkarılacağını netleştirir.",
        ]},
    ],
    "sss": [
        ("Hareket problemlerinde temel bağıntı nedir?",
         "Yol, hız ile zamanın çarpımıdır. Hız yolun zamana, zaman yolun hıza bölünmesiyle bulunur."),
        ("İki araç ne zaman karşılaşır?",
         "Birbirine doğru giden iki araç, aradaki mesafenin hızlarının toplamına bölünmesiyle bulunan sürede karşılaşır."),
        ("Arkadaki araç öndekine ne zaman yetişir?",
         "Aynı yönde giden araçlarda aradaki mesafe hızların farkına bölünür. Bulunan süre, yetişme süresidir."),
        ("Ortalama hız nasıl hesaplanır?",
         "Toplam yol toplam zamana bölünür. Farklı hızların basit ortalaması alınmaz, çünkü yavaş gidilen bölümde daha uzun süre geçer."),
        ("Akıntı problemlerinde hız nasıl bulunur?",
         "Akıntı yönünde teknenin hızına akıntı hızı eklenir, akıntıya karşı ise çıkarılır."),
        ("Tren bir köprüyü ne kadar sürede geçer?",
         "Köprünün uzunluğu ile trenin uzunluğu toplanır ve trenin hızına bölünür. Trenin tamamen geçmesi için kendi uzunluğu kadar ek yol alması gerekir."),
        ("Dairesel pistte iki koşucu ne zaman buluşur?",
         "Aynı yönde koşuyorlarsa pist uzunluğu hızların farkına, zıt yönde koşuyorlarsa hızların toplamına bölünür."),
        ("Saatte kilometre, saniyede metreye nasıl çevrilir?",
         "Kilometre 1000 ile çarpılıp metreye, saat 3600 ile çarpılıp saniyeye çevrilir. Saatte 72 kilometre, saniyede 20 metredir."),
        ("Araçlar farklı saatlerde yola çıkarsa ne yapılır?",
         "Önce erken çıkan aracın tek başına aldığı yol hesaplanır ve mesafeden çıkarılır. Kalan mesafe, iki araç birlikte hareket ederken kapatılır."),
        ("Ortalama hız ne zaman hızların ortalamasına eşit olur?",
         "Eşit süreler boyunca farklı hızlarla gidildiğinde ortalama hız, hızların basit ortalamasına eşittir. Eşit yollar farklı hızlarla gidildiğinde ise ortalama hız daha küçüktür."),
    ],
    "kontrol": [
        "Yol, hız ve zaman arasındaki bağıntıyı kullanabiliyorum.",
        "Hız ve süre birimlerini birbirine çevirebiliyorum.",
        "Ondalıklı saatleri saat ve dakikaya çevirebiliyorum.",
        "Birbirine doğru giden araçların karşılaşma süresini bulabiliyorum.",
        "Aynı yönde giden araçlarda yetişme süresini bulabiliyorum.",
        "Zıt yönde giden araçlar arasındaki mesafeyi hesaplayabiliyorum.",
        "Ortalama hızı toplam yol ve toplam zamanla hesaplayabiliyorum.",
        "Akıntı yönünde ve akıntıya karşı hızları yazabiliyorum.",
        "Tren ve köprü sorularında trenin uzunluğunu hesaba katabiliyorum.",
        "Dairesel pistte buluşma süresini hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["dogru-oranti-ve-ters-oranti", "isci-ve-havuz-problemleri-konu-anlatimi-pdf", "denklem-kurma-problemleri-nasil-cozulur"],
}
