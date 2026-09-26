# scripts/yazilar/85_faiz_problemleri.py — Faiz Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "faiz-problemleri-nasil-cozulur",
    "baslik": "Faiz Problemleri Nasıl Çözülür?",
    "aciklama": "Faiz problemleri nasıl çözülür? Basit faiz formülü, ay ve yıl dönüşümü, anapara, oran ve süre bulma, bileşik faiz, iki hesaba bölünen para; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "faiz-problemleri-nasil-cozulur",
    "kapak_alt": "Faiz problemleri: giderek yükselen disk yığınlarıyla zaman içinde büyüyen birikimi modelleyen öğrenci",
    "ozet": "Faiz, paranın belirli bir süre kullanılması karşılığında ödenen bedeldir ve faiz problemleri bu bedelin anapara, oran ve süreyle ilişkisini konu alır. Basit faizde faiz yalnızca başlangıçtaki paraya işler; bileşik faizde ise her dönemin faizi anaparaya eklenir ve sonraki dönemde o da faiz kazanır. Bu yazıda basit faiz formülünü, ay ve yıl dönüşümünü, anaparayı, oranı ve süreyi bulmayı, paranın ikiye katlanmasını, bileşik faizi, basit ve bileşik faizin karşılaştırmasını ve iki hesaba bölünen para sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Faiz nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için yüzde hesaplarını, çarpan yöntemini ve üslü sayıları biliyor olman yeterli.",
                "Yüzde ve çarpan yöntemi için <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a>, üsler için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısına göz at."),
            "Faiz, bir paranın belirli bir süre kullanılması karşılığında ödenen bedeldir. Bankaya yatırılan para için banka faiz öder; kredi alan kişi ise bankaya faiz öder. Yani faiz, paranın zaman içindeki kullanım bedelidir. Faiz problemlerinde şu dört temel kavram kullanılır ve hepsi birbirine bağlıdır:",
            tablo(["Kavram", "Anlamı"], [
                ["Anapara", "Başlangıçta yatırılan ya da borç alınan para"],
                ["Faiz oranı", "Genellikle yıllık yüzde olarak verilen oran"],
                ["Süre", "Paranın faizde kaldığı zaman"],
                ["Faiz tutarı", "Süre sonunda anaparaya eklenen para"],
            ]),
            "Faiz problemlerinde en önemli ayrım, faizin nasıl hesaplandığıdır. Faiz iki biçimde hesaplanır. <strong>Basit faizde</strong> faiz yalnızca anaparaya işler ve her yıl aynı miktarda faiz eklenir. <strong>Bileşik faizde</strong> ise her dönemin faizi anaparaya eklenir ve sonraki dönemde o da faiz kazanır. Bu yazıdaki oranlar yalnızca hesap örneğidir; gerçek faiz oranları bankaya, ürüne ve zamana göre değişir.",
            hap("Basit faiz yalnızca anaparaya işler.",
                "Bileşik faizde faiz de faiz kazanır."),
        ]},
        {"baslik": "Basit faiz formülü", "icerik": [
            "Basit faizde faiz tutarı, anaparanın yıllık faiz oranıyla ve yıl cinsinden süreyle çarpımıdır. Oran yüzde olarak verildiği için $100$ e bölünür:",
            "$$\\text{Faiz}=\\dfrac{\\text{Anapara} \\cdot \\text{Oran} \\cdot \\text{Süre}}{100}$$",
            "Formüldeki oran yıllık, süre de yıl cinsindendir. Süre sonunda eldeki toplam para, anapara ile faizin toplamıdır. Basit faizde faiz tutarı süreyle doğru orantılıdır: süre iki katına çıkarsa faiz de iki katına çıkar.",
            ornek(
                "$8000$ lira, yıllık yüzde $30$ basit faizle $2$ yıl bankada kalıyor.",
                "Faiz tutarını ve süre sonundaki toplam parayı bulalım.",
                "Faiz: $\\dfrac{8000 \\cdot 30 \\cdot 2}{100}=4800$ lira.",
                "Toplam: $8000+4800=12800$ lira.",
                "Her yıl eşit faiz eklenir: birinci yıl $2400$, ikinci yıl yine $2400$ lira."),
        ]},
        {"baslik": "Süre ay ya da gün olarak verilirse", "icerik": [
            "Oran yıllık verildiği hâlde süre ay olarak verilmişse süre yıla çevrilir: $t$ ay, $\\dfrac{t}{12}$ yıldır. Gün olarak verilen sürelerde bir yılın kaç gün kabul edileceği soruda belirtilir ve süre o sayıya bölünerek yıla çevrilir.",
            ornek(
                "$6000$ lira, yıllık yüzde $24$ basit faizle $5$ ay bankada kalıyor.",
                "Faiz tutarını bulalım.",
                "Süre: $\\dfrac{5}{12}$ yıl.",
                "Faiz: $6000 \\cdot 0.24 \\cdot \\dfrac{5}{12}=600$ lira."),
            "Aynı hesap aylık oranla da yapılabilir: yıllık yüzde $24$ basit faiz, aylık yüzde $2$ demektir. $6000$ liranın aylık faizi $120$ lira, $5$ aylık faizi $600$ liradır.",
            dikkat(
                "Süreyi yıla çevirmeden formüle koymak.",
                "Yıllık oranla $5$ ay hesaplanırken süre $5$ olarak yazılırsa faiz $12$ kat büyük çıkar: $7200$ lira. Oran ve süre her zaman aynı birimde olmalıdır."),
        ]},
        {"baslik": "Anaparayı bulmak", "icerik": [
            "Faiz tutarı, oran ve süre biliniyorsa anapara, formülün tersinden bulunur: faiz, oran ile sürenin çarpımına bölünür ve $100$ ile çarpılır.",
            ornek(
                "Bir para yıllık yüzde $25$ basit faizle $3$ yılda $1800$ lira faiz getiriyor.",
                "Anaparayı bulalım.",
                "Formül: $1800=\\dfrac{A \\cdot 25 \\cdot 3}{100}$, yani $1800=0.75A$.",
                "$A=1800:0.75=2400$ lira."),
            ornek(
                "Bir para yıllık yüzde $20$ basit faizle $2$ yıl sonunda $7000$ lira oluyor.",
                "Anaparayı bulalım.",
                "$2$ yılda anaparanın yüzde $40$ ı kadar faiz eklenir; toplam para anaparanın $1.4$ katıdır.",
                "$1.4A=7000$, yani $A=5000$ lira. Faiz $2000$ liradır."),
            dikkat(
                "Toplam parayı faiz sanmak.",
                "İkinci örnekte $7000$ lira faiz değil, anapara ile faizin toplamıdır. Soru \"… lira oluyor\" diyorsa verilen sayı toplamdır ve anaparanın bir katı olarak yazılır."),
        ]},
        {"baslik": "Oranı ve süreyi bulmak", "icerik": [
            "Formüldeki dört nicelikten üçü biliniyorsa dördüncüsü bulunur. Oran ve süre sorularında da aynı formül kullanılır; yalnızca bilinmeyenin yeri değişir.",
            ornek(
                "$5000$ lira $2$ yılda $1500$ lira basit faiz getiriyor.",
                "Yıllık faiz oranını bulalım.",
                "$1500=\\dfrac{5000 \\cdot n \\cdot 2}{100}$, yani $1500=100n$.",
                "$n=15$; yıllık yüzde $15$."),
            ornek(
                "$4000$ lira yıllık yüzde $20$ basit faizle yatırılıyor.",
                "Kaç yılda $2400$ lira faiz getireceğini bulalım.",
                "Bir yıllık faiz: $4000 \\cdot 0.2=800$ lira.",
                "$2400:800=3$ yıl."),
        ]},
        {"baslik": "Para kaç yılda iki katına çıkar?", "icerik": [
            "Basit faizde paranın iki katına çıkması, faizin anaparaya eşit olması demektir. Bu durumda formül $A=\\dfrac{A \\cdot n \\cdot t}{100}$ olur ve $A$ sadeleşince $n \\cdot t=100$ kalır. Yani oran ile sürenin çarpımı $100$ olmalıdır.",
            ornek(
                "Bir para yıllık yüzde $25$ basit faizle yatırılıyor.",
                "Paranın kaç yılda iki katına çıkacağını bulalım.",
                "$25 \\cdot t=100$, yani $t=4$ yıl.",
                "Kontrol: $1000$ lira her yıl $250$ lira faiz alır; $4$ yılda $1000$ lira faiz eklenir ve para $2000$ olur."),
            "Aynı mantıkla para üç katına çıkacaksa faiz anaparanın iki katı olmalıdır: $n \\cdot t=200$. Yüzde $25$ oranla bu $8$ yıl sürer.",
            hap("Basit faizde oran ile sürenin çarpımı $100$ olduğunda para iki katına çıkar.", "Yıllık yüzde $25$ basit faizle para $4$ yılda iki katına çıkar."),
        ]},
        {"baslik": "Bileşik faiz", "icerik": [
            "Bileşik faizde her dönemin sonunda faiz anaparaya eklenir ve bir sonraki dönemin faizi bu yeni tutar üzerinden hesaplanır. Bu, her dönem aynı çarpanla çarpmak demektir. Yıllık oran $r$ ise $t$ yıl sonraki tutar şöyledir:",
            "$$\\text{Tutar}=A \\cdot \\left(1+\\dfrac{r}{100}\\right)^t$$",
            ornek(
                "$10000$ lira yıllık yüzde $10$ bileşik faizle $2$ yıl bankada kalıyor.",
                "Süre sonundaki tutarı bulalım.",
                "Birinci yıl sonunda: $10000 \\cdot 1.1=11000$ lira.",
                "İkinci yıl sonunda: $11000 \\cdot 1.1=12100$ lira.",
                "Formülle: $10000 \\cdot 1.1^2=12100$. Toplam faiz $2100$ liradır."),
            "İkinci yılın faizi $1100$ liradır, birinci yılınki ise $1000$ lira. Aradaki $100$ lira, birinci yılın faizinin ikinci yılda kazandığı faizdir. Bileşik faizin gücü bu \"faizin faizinden\" gelir. Süre uzadıkça bu ek kazanç da büyür, çünkü her yıl bir önceki yılların bütün faizleri de faiz kazanmaya devam eder. Örneğin yıllık yüzde $10$ bileşik faizle $3$ yılın toplam artışı yüzde $33.1$ iken $6$ yılınki yaklaşık yüzde $77$ dir; süre iki katına çıkınca artış iki katından fazla olur.",
            hap("Bileşik faizde $t$ yıl sonraki tutar, anaparanın $\\left(1+\\dfrac{r}{100}\\right)^t$ ile çarpımıdır."),
        ]},
        {"baslik": "Basit ve bileşik faizin karşılaştırması", "icerik": [
            "Aynı anapara ve aynı oranla basit ve bileşik faiz, ilk yılın sonunda aynı sonucu verir. Sonraki yıllarda bileşik faiz öne geçer ve fark her yıl büyür.",
            tablo(["Yıl", "Basit faizle tutar", "Bileşik faizle tutar"], [
                ["$1$", "$11000$", "$11000$"],
                ["$2$", "$12000$", "$12100$"],
                ["$3$", "$13000$", "$13310$"],
            ]),
            "Tablo $10000$ liranın yıllık yüzde $10$ oranla büyümesini gösteriyor. Basit faizde tutar her yıl aynı miktarda, $1000$ lira artar; bileşik faizde ise her yıl bir önceki tutarın yüzde $10$ u kadar artar. Basit faiz düz bir çizgi gibi, bileşik faiz ise giderek dikleşen bir eğri gibi büyür.",
            dikkat(
                "Bileşik faizi basit faiz gibi hesaplamak.",
                "Yıllık yüzde $10$ bileşik faizle $3$ yılın toplam artışı yüzde $30$ değil, yüzde $33.1$ dir. Çarpanlar toplanmaz, çarpılır: $1.1^3=1.331$."),
        ]},
        {"baslik": "İki hesaba bölünen para", "icerik": [
            "Bir para iki kısma ayrılıp farklı oranlarla yatırıldığında her kısmın faizi ayrı ayrı yazılır ve toplanır. Kısımlardan birine $x$ denir, diğeri toplamdan $x$ çıkarılarak yazılır. Süreler farklıysa her kısmın süresi de ayrı ayrı yazılır.",
            ornek(
                "$20000$ liranın bir kısmı yıllık yüzde $20$, kalanı yıllık yüzde $30$ basit faizle $1$ yıllığına yatırılıyor. Toplam faiz $5000$ lira.",
                "Her orana yatırılan parayı bulalım.",
                "Yüzde $20$ ye yatırılan $x$, yüzde $30$ a yatırılan $20000-x$ olsun.",
                "Toplam faiz: $0.2x+0.3(20000-x)=5000$, yani $6000-0.1x=5000$.",
                "$0.1x=1000$, yani $x=10000$. Her orana $10000$ lira yatırılmıştır. Kontrol: $2000+3000=5000$."),
            "Bu tür sorularda sonucu kontrol etmenin kısa bir yolu da vardır. Toplam faiz, iki oranın ağırlıklı ortalamasıyla düşünülebilir: $5000$ lira, $20000$ liranın yüzde $25$ idir. Yüzde $25$, yüzde $20$ ile yüzde $30$ un tam ortası olduğu için para iki orana eşit bölünmüştür.",
        ]},
        {"baslik": "Borç ve eşit taksitler", "icerik": [
            "Basit faizli bir borçta ödenecek toplam tutar, anapara ile faizin toplamıdır. Bu tutar eşit taksitlerle ödenecekse toplam, taksit sayısına bölünür. Gerçek kredilerde taksit hesabı daha karmaşık yöntemlerle yapılır; burada yalnızca basit faizli bir örnek hesap gösteriliyor.",
            ornek(
                "$12000$ liralık bir borç yıllık yüzde $18$ basit faizle $8$ ay sonra ödenecek ve toplam tutar $8$ eşit taksite bölünecek.",
                "Faizi, toplam tutarı ve taksit miktarını bulalım.",
                "Süre: $\\dfrac{8}{12}$ yıl. Faiz: $12000 \\cdot 0.18 \\cdot \\dfrac{8}{12}=1440$ lira.",
                "Toplam tutar: $12000+1440=13440$ lira.",
                "Bir taksit: $13440:8=1680$ lira."),
        ]},
        {"baslik": "Farklı zamanlarda yatırılan paralar", "icerik": [
            "Bir hesaba farklı zamanlarda para yatırıldığında her yatırım, bankada kaldığı süre kadar faiz kazanır. Faizler ayrı ayrı hesaplanıp toplanır.",
            ornek(
                "Bir kişi yılbaşında $10000$ lira yatırıyor, altı ay sonra aynı hesaba $10000$ lira daha ekliyor. Hesap yıllık yüzde $20$ basit faiz veriyor.",
                "Yıl sonunda kazanılan toplam faizi bulalım.",
                "İlk yatırım $1$ yıl kalır: $10000 \\cdot 0.2 \\cdot 1=2000$ lira.",
                "İkinci yatırım $6$ ay, yani yarım yıl kalır: $10000 \\cdot 0.2 \\cdot \\dfrac{1}{2}=1000$ lira.",
                "Toplam faiz: $3000$ lira."),
            dikkat(
                "Bütün paralara aynı süreyi uygulamak.",
                "İki yatırımı toplayıp $20000$ lira için bir yıllık faiz hesaplamak $4000$ lira verir ve yanlıştır. Sonradan yatırılan para daha kısa süre faizde kalır."),
        ]},
        {"baslik": "Bileşik faizde süre bulmak", "icerik": [
            "Bileşik faizde paranın belirli bir tutara ulaşma süresi, çarpanın kuvvetleri tek tek hesaplanarak bulunur. Süre tam yıl olarak sorulduğunda, tutarın hedefi ilk kez geçtiği yıl aranır.",
            ornek(
                "$10000$ lira yıllık yüzde $20$ bileşik faizle yatırılıyor.",
                "Paranın ilk kez iki katını geçtiği yılı bulalım.",
                "Çarpanın kuvvetleri: $1.2^2=1.44$, $1.2^3=1.728$, $1.2^4=2.0736$.",
                "Üçüncü yılın sonunda tutar $17280$ lira, dördüncü yılın sonunda $20736$ liradır.",
                "Para ilk kez dördüncü yılın sonunda iki katını geçer."),
            "Aynı oranla basit faizde paranın iki katına çıkması $100:20=5$ yıl sürerdi. Bileşik faiz, faizin faizi sayesinde aynı hedefe bir yıl önce ulaştırır.",
        ]},
        {"baslik": "Hangi teklif daha iyi?", "icerik": [
            "Farklı faiz türleri ve oranlar karşılaştırılırken yalnızca orana bakmak yanıltıcı olabilir. Doğru yol, aynı anapara ve aynı süre için her teklifin süre sonundaki tutarını ayrı ayrı hesaplamaktır.",
            ornek(
                "$10000$ lira için iki teklif var: A bankası $2$ yıl boyunca yıllık yüzde $30$ basit faiz, B bankası $2$ yıl boyunca yıllık yüzde $28$ bileşik faiz veriyor.",
                "Hangi teklifin daha fazla kazandırdığını bulalım.",
                "A bankası: $10000+10000 \\cdot 0.3 \\cdot 2=16000$ lira.",
                "B bankası: $10000 \\cdot 1.28^2=16384$ lira.",
                "Oranı daha düşük görünen B bankası, $384$ lira daha fazla kazandırır."),
            "Süre uzadıkça bileşik faizin üstünlüğü artar. Bir yıllık yatırımda ise aynı oranla basit ve bileşik faiz aynı sonucu verir; bu durumda daha yüksek oranlı teklif daha iyidir.",
            hap("Teklifler karşılaştırılırken aynı anapara ve aynı süre için süre sonundaki tutarlar hesaplanır; yalnızca orana bakılmaz."),
        ]},
        {"baslik": "Aylık ve yıllık oran", "icerik": [
            "Basit faizde aylık oran ile yıllık oran arasında doğrudan orantı vardır: yıllık oran, aylık oranın $12$ katıdır. Aylık yüzde $2$ basit faiz, yıllık yüzde $24$ basit faize eşdeğerdir.",
            "Bileşik faizde ise bu ilişki geçerli değildir. Aylık yüzde $2$ bileşik faiz bir yılda $1.02^{12}$ çarpanına ulaşır ve bu değer $1.24$ ten büyüktür; yani yıllık etkisi yüzde $24$ ten fazladır. Bu yüzden bileşik faizli ürünlerde aylık oranı $12$ ile çarparak yıllık oranı bulmak doğru değildir.",
            hap("Borç her ay yüzde $4$ bileşik faizle büyürse bir yılda yüzde $48$ değil, yaklaşık yüzde $60$ büyür.", "Çünkü $1.04^{12} \\approx 1.60$ olur.", gunluk=True),
        ]},
        {"baslik": "Sınavda faiz problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) faiz problemleri çoğunlukla basit faiz formülü, süre dönüşümü, anapara bulma ve iki hesaba bölünen para biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde bileşik faiz ve yüzde çarpanları da gerekebilir."),
            "Faiz sorularında ilk iş, verilen sayının faiz mi yoksa anapara ile faizin toplamı mı olduğunu belirlemektir. İkinci iş, oran ile sürenin aynı birimde olup olmadığını kontrol etmektir. Bu iki kontrol yapıldığında formül hemen her soruyu doğrudan çözer.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Ayı yıla çevirmeden hesaplamak", "$t$ ay, $\\dfrac{t}{12}$ yıldır"],
                ["Toplam parayı faiz sanmak", "Toplam, anapara ile faizin toplamıdır"],
                ["Bileşik faizde yüzdeleri toplamak", "Çarpanları çarp"],
                ["Aylık bileşik oranı $12$ ile çarpmak", "Kuvvet alınır"],
                ["İki hesapta kalanı yanlış yazmak", "Toplamdan $x$ çıkarılır"],
                ["Faizi yeni tutar üzerinden hesaplamak", "Basit faizde hep anapara"],
            ]),
            "Bu hataların çoğu, basit ve bileşik faizi birbirine karıştırmaktan ya da birimleri kontrol etmemekten doğar. Soru hangi faiz türünü kullandığını söylemiyorsa genellikle basit faiz kastedilir; yine de soru metnini dikkatle okumak gerekir.",
        ]},
    ],
    "sss": [
        ("Basit faiz nasıl hesaplanır?",
         "Anapara, yıllık faiz oranı ve yıl cinsinden süre çarpılır ve 100 e bölünür. Süre ay olarak verilmişse önce 12 ye bölünerek yıla çevrilir."),
        ("Basit faiz ile bileşik faiz arasındaki fark nedir?",
         "Basit faizde faiz yalnızca anaparaya işler. Bileşik faizde her dönemin faizi anaparaya eklenir ve sonraki dönemde o da faiz kazanır."),
        ("Para basit faizle kaç yılda iki katına çıkar?",
         "Faiz anaparaya eşit olduğunda para iki katına çıkar. Bu, oran ile sürenin çarpımının 100 olması demektir; yüzde 25 oranla 4 yıl sürer."),
        ("Bileşik faizle toplam tutar nasıl bulunur?",
         "Anapara, bir artı yıllık oranın yüzde karşılığının süre kadar kuvvetiyle çarpılır. 10000 lira yüzde 10 bileşik faizle 2 yılda 12100 lira olur."),
        ("İki farklı orana bölünen para nasıl bulunur?",
         "Bir kısma x, diğer kısma toplamdan x çıkarılarak yazılır. İki kısmın faizleri toplanıp toplam faize eşitlenir ve x bulunur."),
        ("Aylık oran yıllık orana nasıl çevrilir?",
         "Basit faizde aylık oran 12 ile çarpılır. Bileşik faizde ise bu yöntem doğru değildir; yıllık etki aylık çarpanın 12 nci kuvvetiyle bulunur."),
        ("Farklı zamanlarda yatırılan paranın faizi nasıl hesaplanır?",
         "Her yatırım bankada kaldığı süre kadar faiz kazanır. Faizler ayrı ayrı hesaplanır ve toplanır; paralar toplanıp tek bir süre uygulanmaz."),
        ("Basit ve bileşik faiz teklifleri nasıl karşılaştırılır?",
         "Aynı anapara ve aynı süre için her teklifin süre sonundaki tutarı ayrı ayrı hesaplanır. Oranı düşük görünen bileşik faiz, uzun sürede daha yüksek oranlı basit faizi geçebilir."),
    ],
    "kontrol": [
        "Anapara, oran, süre ve faiz tutarı kavramlarını açıklayabiliyorum.",
        "Basit faiz formülünü kullanabiliyorum.",
        "Ay olarak verilen süreyi yıla çevirebiliyorum.",
        "Faiz ile toplam parayı birbirinden ayırt edebiliyorum.",
        "Anaparayı, oranı ve süreyi formülün tersinden bulabiliyorum.",
        "Paranın iki katına çıkma süresini hesaplayabiliyorum.",
        "Bileşik faizi çarpanın kuvvetiyle hesaplayabiliyorum.",
        "Basit ve bileşik faizin zamanla nasıl ayrıştığını açıklayabiliyorum.",
        "İki hesaba bölünen para sorularını denklemle çözebiliyorum.",
        "Aylık ve yıllık oran arasında doğru geçiş yapabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["yuzde-problemleri-nasil-cozulur", "kar-ve-zarar-problemleri-konu-anlatimi-pdf", "uslu-sayilar-konu-anlatimi-pdf"],
}
