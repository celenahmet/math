# scripts/yazilar/83_yuzde_problemleri.py — Yuzde Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "yuzde-problemleri-nasil-cozulur",
    "baslik": "Yüzde Problemleri Nasıl Çözülür?",
    "aciklama": "Yüzde problemleri nasıl çözülür? 100 kabul etme, çarpan yöntemi, yüzdenin yüzdesi, değişen oranlar, fiyat ve miktar, karşılaştırma ve anket soruları; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "yuzde-problemleri-nasil-cozulur",
    "kapak_alt": "Yüzde problemleri: yüzlük ızgaralarda mavi karelerle artış, azalış ve parça bütün ilişkisini gösteren iki öğrenci",
    "ozet": "Yüzde problemleri, yüzde kavramı bilindiği hâlde en çok hata yapılan problem türlerinden biridir. Hatanın kaynağı hesap değil, yüzdenin hangi bütüne göre alındığının karıştırılmasıdır. Bu yazıda yüzde problemlerini çözmenin iki temel aracını, yani bütünü 100 kabul etmeyi ve çarpan yöntemini, yüzdenin yüzdesini, oranı değişen grupları, fiyat ile miktar ilişkisini, iki niceliği yüzdeyle karşılaştırmayı, art arda değişimleri ve anket sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Yüzde problemlerinin iki temel aracı", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için yüzdenin tanımını, bir sayının yüzdesini bulmayı ve yüzde artış ile azalışı biliyor olman yeterli.",
                "Bu temeller için <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a> yazısına göz at."),
            "Yüzde problemlerinin neredeyse hepsi iki araçla çözülür. Birincisi <strong>bütünü 100 kabul etmektir</strong>: bütün $100$ birim alındığında yüzdeler doğrudan birim sayısına dönüşür ve hesap tam sayılarla yürür. İkincisi <strong>çarpan yöntemidir</strong>: yüzde $a$ artış değeri $1+\\dfrac{a}{100}$ ile, yüzde $a$ azalış $1-\\dfrac{a}{100}$ ile çarpmaktır.",
            tablo(["Durum", "Hangi araç?"], [
                ["Bütün bilinmiyor, oranlar soruluyor", "Bütünü $100$ kabul et"],
                ["Art arda değişimler var", "Çarpan yöntemi"],
                ["Bütün biliniyor, parça soruluyor", "Doğrudan çarp"],
                ["Parça biliniyor, bütün soruluyor", "Çarpana böl"],
            ]),
            hap("Bütün bilinmiyorsa $100$ kabul et.",
                "Art arda değişimlerde çarpanları çarp, yüzdeleri toplama."),
        ]},
        {"baslik": "Bütünü 100 kabul etmek", "icerik": [
            "Soruda bütünün kendisi verilmiyor ve yalnızca oranlar isteniyorsa bütünü $100$ kabul etmek en kısa yoldur. Sonuç yine yüzde olarak okunur. $100$ seçmenin nedeni basittir: $100$ ün yüzde $a$ sı tam olarak $a$ dır ve hiçbir çevirme gerekmez.",
            ornek(
                "Bir malın fiyatına önce yüzde $20$ zam yapılıyor, sonra yeni fiyat üzerinden yüzde $25$ indirim uygulanıyor.",
                "Son fiyatın ilk fiyata göre yüzde kaç değiştiğini bulalım.",
                "İlk fiyat $100$ olsun. Zamla $120$ olur.",
                "$120$ nin yüzde $25$ i $30$ dur; indirimle $120-30=90$ olur.",
                "Son fiyat $90$; yani ilk fiyata göre yüzde $10$ azalmıştır."),
            "Bu yöntemin gücü, her adımın somut bir sayıyla izlenebilmesidir. Aynı soru çarpanlarla da çözülür: $1.2 \\cdot 0.75=0.9$, yani yüzde $10$ azalış.",
        ]},
        {"baslik": "Yüzdenin yüzdesi", "icerik": [
            "Bir grubun belirli bir yüzdesinin de bir yüzdesi sorulduğunda iki yüzde çarpılır. Sonuç, en baştaki bütüne göre bir yüzdedir.",
            ornek(
                "Bir okuldaki öğrencilerin yüzde $45$ i kızdır ve kızların yüzde $20$ si bir spor kulübüne üyedir.",
                "Spor kulübüne üye kızların okuldaki bütün öğrencilerin yüzde kaçı olduğunu bulalım.",
                "Okulu $100$ öğrenci kabul edelim: $45$ kız.",
                "Kızların yüzde $20$ si: $45 \\cdot 0.2=9$ öğrenci.",
                "Sonuç: okulun yüzde $9$ u. Çarpanla: $0.45 \\cdot 0.2=0.09$."),
            dikkat(
                "İki yüzdeyi toplamak ya da çıkarmak.",
                "Yüzde $45$ ile yüzde $20$ farklı bütünlere aittir: birincisi okula, ikincisi kızlara. Bu yüzden $45-20=25$ ya da $45+20=65$ gibi işlemler anlamsızdır; yüzdenin yüzdesi çarparak bulunur."),
            hap("Yüzdenin yüzdesi sorulduğunda iki yüzde çarpılır ve sonuç $100$ e bölünür.", "Yüzde $45$ in yüzde $20$ si, bütünün yüzde $9$ u olur."),
        ]},
        {"baslik": "Oranı değişen gruplar", "icerik": [
            "Bir gruba kişi eklenip çıkarıldığında gruptaki bir alt grubun yüzdesi değişir. Bu sorularda hem alt grubun sayısı hem de bütünün kendisi değişir; ikisi de denkleme ayrı ayrı yazılmalıdır.",
            ornek(
                "Bir sınıftaki öğrencilerin yüzde $40$ ı kızdır. Sınıfa $6$ kız öğrenci katılınca kızların oranı yüzde $50$ ye çıkıyor.",
                "Sınıfın başlangıçtaki mevcudunu bulalım.",
                "Başlangıç mevcudu $x$ olsun; kızlar $0.4x$.",
                "$6$ kız gelince kızlar $0.4x+6$, mevcut $x+6$ olur: $0.4x+6=0.5(x+6)$.",
                "$0.4x+6=0.5x+3$, yani $0.1x=3$ ve $x=30$. Kontrol: başta $12$ kız, sonra $18$ kız ve $36$ kişi; $\\dfrac{18}{36}$ yüzde $50$ dir."),
            dikkat(
                "Yalnızca alt grubu değiştirip bütünü sabit bırakmak.",
                "$6$ kız katıldığında sınıfın mevcudu da $6$ artar. $0.4x+6=0.5x$ gibi bir kurulum, bütünün değişmediğini varsaymaktır ve yanlış sonuç verir."),
        ]},
        {"baslik": "Fiyat ile miktar ilişkisi", "icerik": [
            "Harcanan para sabitken fiyat ile alınabilen miktar ters orantılıdır. Fiyat bir çarpanla artarsa miktar aynı çarpanın tersiyle azalır. Bu yüzden fiyattaki yüzde artış, miktardaki yüzde azalışa eşit değildir.",
            ornek(
                "Bir ürünün fiyatı yüzde $25$ artıyor.",
                "Aynı parayla alınabilen ürün miktarının yüzde kaç azaldığını bulalım.",
                "Fiyat çarpanı $1.25$ ise miktar çarpanı $\\dfrac{1}{1.25}=0.8$ dir.",
                "$0.8$ çarpanı yüzde $20$ azalış demektir.",
                "Sayıyla kontrol: fiyatı $4$ lira olan üründen $100$ liraya $25$ tane alınır. Fiyat $5$ lira olunca $20$ tane alınır; $25$ ten $20$ ye düşüş yüzde $20$ dir."),
            "Oran ve ters orantı ilişkisinin ayrıntısı <a href=\"/blog/dogru-oranti-ve-ters-oranti/\">Doğru Orantı ve Ters Orantı</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "İki niceliği yüzdeyle karşılaştırmak", "icerik": [
            "\"$A$, $B$ den yüzde $25$ fazladır\" cümlesinde bütün $B$ dir. Aynı ilişki ters yönden söylendiğinde bütün $A$ olur ve yüzde değişir. Bu asimetri, yüzde problemlerinin en sık tuzağıdır.",
            ornek(
                "Ali'nin harçlığı Ayşe'ninkinden yüzde $25$ fazladır.",
                "Ayşe'nin harçlığının Ali'ninkinden yüzde kaç az olduğunu bulalım.",
                "Ayşe'nin harçlığı $100$ olsun; Ali'ninki $125$ olur.",
                "Fark $25$ tir ama bu kez bütün Ali'nin harçlığıdır: $\\dfrac{25}{125}=\\dfrac{1}{5}$.",
                "Ayşe'nin harçlığı Ali'ninkinden yüzde $20$ azdır."),
            tablo(["$A$, $B$ den ... fazla", "$B$, $A$ dan ... az"], [
                ["Yüzde $25$", "Yüzde $20$"],
                ["Yüzde $50$", "Yüzde $33.\\overline{3}$"],
                ["Yüzde $100$", "Yüzde $50$"],
            ]),
            "Tablodaki son satır bu farkı en açık biçimde gösterir: $A$, $B$ nin iki katıysa $A$, $B$ den yüzde $100$ fazladır; ama $B$, $A$ dan yalnızca yüzde $50$ azdır.",
            hap("$A$, $B$ den yüzde $25$ fazlaysa $B$, $A$ dan yüzde $20$ azdır.", "İki cümlede bütün farklı olduğu için yüzdeler de farklıdır."),
        ]},
        {"baslik": "Art arda değişimler ve eşdeğer tek değişim", "icerik": [
            "Birden fazla yüzde değişim art arda uygulandığında, çarpanlar çarpılarak tek bir eşdeğer değişim bulunur. Bu, özellikle seçenekli sorularda hesabı çok kısaltır ve ara değerleri hesaplamaya gerek bırakmaz.",
            ornek(
                "Bir fiyata önce yüzde $20$, sonra yüzde $25$ zam yapılıyor.",
                "İki zamın toplam etkisini tek bir yüzdeyle ifade edelim.",
                "Toplam çarpan: $1.2 \\cdot 1.25=1.5$.",
                "$1.5$ çarpanı yüzde $50$ artış demektir; yüzde $45$ değil."),
            ornek(
                "Bir çalışanın maaşına yüzde $10$ zam yapılıyor, ertesi ay maaş yüzde $10$ azaltılıyor.",
                "Son maaşın ilk maaşa göre durumunu bulalım.",
                "Toplam çarpan: $1.1 \\cdot 0.9=0.99$.",
                "Maaş başa dönmez; ilk maaşa göre yüzde $1$ azalmıştır."),
            hap("Etiketinde yüzde $20$ indirim olan bir ürüne kasada ek yüzde $10$ indirim uygulanırsa toplam indirim yüzde $30$ değil, yüzde $28$ olur.", "Çarpanlar çarpılır: $0.8 \\cdot 0.9=0.72$ olur.", gunluk=True),
        ]},
        {"baslik": "Büyüme ve bileşik artış", "icerik": [
            "Bir nicelik her dönem bir önceki dönemin üzerine aynı yüzdeyle artıyorsa, her dönem aynı çarpanla çarpılır. $n$ dönem sonra değer, başlangıç değeri ile çarpanın $n$ inci kuvvetinin çarpımıdır.",
            ornek(
                "Bir öğrenci kulübünün üye sayısı $200$ dür ve her yıl bir önceki yıla göre yüzde $10$ artıyor.",
                "$2$ yıl sonraki üye sayısını bulalım.",
                "Bir yıl sonra: $200 \\cdot 1.1=220$.",
                "İki yıl sonra: $220 \\cdot 1.1=242$.",
                "Toplam artış $42$ üyedir, yani yüzde $21$; yüzde $20$ değil. İkinci yılın artışı, birinci yılda gelen üyeleri de kapsar."),
            "Bu mantık bileşik faizin de temelidir. Faiz hesaplarının ayrıntısı <a href=\"/blog/faiz-problemleri-nasil-cozulur/\">Faiz Problemleri Nasıl Çözülür?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Son değerden başa dönmek", "icerik": [
            "Art arda değişimlerden sonraki değer verilip başlangıç değeri sorulduğunda, toplam çarpan bulunur ve son değer bu çarpana bölünür. Değişimleri tek tek geri almak da aynı sonucu verir ama daha uzundur.",
            ornek(
                "Bir ürünün fiyatı önce yüzde $20$ artırılıyor, sonra yeni fiyat üzerinden yüzde $10$ indirim yapılıyor ve ürün $540$ liraya satılıyor.",
                "Ürünün ilk fiyatını bulalım.",
                "Toplam çarpan: $1.2 \\cdot 0.9=1.08$.",
                "İlk fiyat: $540:1.08=500$ lira.",
                "Kontrol: $500 \\cdot 1.2=600$, $600 \\cdot 0.9=540$."),
            dikkat(
                "Yüzdeleri geri alırken aynı yüzdeyle ters işlem yapmak.",
                "Yüzde $10$ indirimi geri almak için $540$ a yüzde $10$ eklemek $594$ verir ve yanlıştır. Doğru geri alma, $540$ ı $0.9$ a bölmektir: $600$. Her değişim, kendi çarpanına bölünerek geri alınır."),
        ]},
        {"baslik": "Sık kullanılan yüzdelerin kesir karşılıkları", "icerik": [
            "Bazı yüzdelerin kesir karşılıklarını bilmek, özellikle zihinden hesapta büyük kolaylık sağlar. Yüzde $25$ ile çarpmak $4$ e bölmek, yüzde $12.5$ ile çarpmak $8$ e bölmektir.",
            tablo(["Yüzde", "Kesir"], [
                ["$\\%12.5$", "$\\dfrac{1}{8}$"],
                ["$\\%20$", "$\\dfrac{1}{5}$"],
                ["$\\%25$", "$\\dfrac{1}{4}$"],
                ["$\\%33.\\overline{3}$", "$\\dfrac{1}{3}$"],
                ["$\\%50$", "$\\dfrac{1}{2}$"],
                ["$\\%66.\\overline{6}$", "$\\dfrac{2}{3}$"],
                ["$\\%75$", "$\\dfrac{3}{4}$"],
            ]),
            "Örneğin $360$ ın yüzde $75$ i, $360$ ın dörtte üçüdür: $360:4=90$ ve $90 \\cdot 3=270$. Kesir karşılığı bilinen yüzdelerde ondalık çarpma yapmaya gerek kalmaz.",
        ]},
        {"baslik": "Yüzde puan ile yüzde farkı", "icerik": [
            "İki oranın farkı anlatılırken \"yüzde puan\" ile \"yüzde\" farklı şeyler söyler. Yüzde puan iki oranın doğrudan farkıdır; yüzde ise bu farkın eski orana göre büyüklüğüdür.",
            ornek(
                "Bir kulübün etkinliklerine katılım oranı yüzde $30$ dan yüzde $36$ ya çıkıyor.",
                "Değişimi yüzde puan ve yüzde olarak ifade edelim.",
                "Yüzde puan: $36-30=6$.",
                "Yüzde: $\\dfrac{6}{30} \\cdot 100=20$. Katılım oranı yüzde $20$ artmıştır."),
            "Haberlerde ve raporlarda iki ifade sık karıştırılır. Soru \"kaç puan arttı\" diye soruyorsa fark, \"yüzde kaç arttı\" diye soruyorsa farkın eski orana bölümü istenir.",
            hap("İki oranın doğrudan farkı yüzde puandır; bu farkın eski orana bölümü ise yüzde değişimdir."),
        ]},
        {"baslik": "Anket ve dağılım soruları", "icerik": [
            "Bir bütünün farklı gruplara yüzdelerle dağıtıldığı sorularda yüzdelerin toplamı $100$ dür. Verilmeyen grubun yüzdesi, $100$ den diğerlerinin çıkarılmasıyla bulunur.",
            ornek(
                "Bir ankete $250$ kişi katılıyor. Katılanların yüzde $36$ sı A seçeneğini, yüzde $44$ ü B seçeneğini, geri kalanı C seçeneğini işaretliyor.",
                "C seçeneğini işaretleyen kişi sayısını bulalım.",
                "C nin yüzdesi: $100-36-44=20$.",
                "$250$ nin yüzde $20$ si: $250 \\cdot 0.2=50$ kişi.",
                "Kontrol: A $90$, B $110$, C $50$ kişi; toplam $250$."),
            "Grafik ve tablolarla verilen dağılım soruları da aynı mantıkla çözülür: önce hangi bütünün yüzdesinin verildiği belirlenir, sonra parça hesaplanır.",
        ]},
        {"baslik": "Denklemle kurulan yüzde problemleri", "icerik": [
            "Aynı sayının iki farklı yüzdesi birbiriyle karşılaştırıldığında sayıya $x$ denir ve yüzdeler ondalık çarpanlarla yazılır. Böylece soru sıradan bir birinci dereceden denkleme dönüşür.",
            ornek(
                "Bir sayının yüzde $30$ unun $12$ fazlası, aynı sayının yüzde $50$ sine eşittir.",
                "Sayıyı bulalım.",
                "Denklem: $0.3x+12=0.5x$.",
                "$12=0.2x$, yani $x=60$.",
                "Kontrol: $60$ ın yüzde $30$ u $18$, $12$ fazlası $30$; yüzde $50$ si de $30$ dur."),
            "Ondalık katsayılardan kurtulmak için iki taraf $10$ ya da $100$ ile çarpılabilir: $3x+120=5x$ denklemi aynı sonucu verir. Denklem çözmenin ayrıntısı <a href=\"/blog/birinci-dereceden-denklemler-konu-anlatimi-pdf/\">Birinci Dereceden Denklemler Konu Anlatımı PDF</a> yazısında.",
        ]},
        {"baslik": "Farklı büyüklükteki grupların birleşik yüzdesi", "icerik": [
            "İki grubun kendi içindeki yüzdeleri biliniyorsa, iki grubun birlikte oluşturduğu bütündeki yüzde, yüzdelerin basit ortalaması değildir. Gruplar farklı büyüklükteyse her grubun katkısı kendi büyüklüğüyle orantılıdır.",
            ornek(
                "Bir sınıfta $20$ kız ve $30$ erkek öğrenci var. Kızların yüzde $60$ ı, erkeklerin yüzde $40$ ı gözlük kullanıyor.",
                "Sınıfın yüzde kaçının gözlük kullandığını bulalım.",
                "Gözlüklü kızlar: $20 \\cdot 0.6=12$. Gözlüklü erkekler: $30 \\cdot 0.4=12$.",
                "Toplam gözlüklü: $24$ öğrenci; sınıf $50$ kişi.",
                "Oran: $\\dfrac{24}{50}$, yani yüzde $48$."),
            dikkat(
                "Yüzdelerin ortalamasını almak.",
                "Yüzde $60$ ile yüzde $40$ ın ortalaması olan yüzde $50$ yanlıştır, çünkü erkekler kızlardan daha kalabalıktır ve düşük yüzdeli grup sonucu kendine doğru çeker. Basit ortalama yalnızca gruplar eşit büyüklükteyse doğrudur."),
        ]},
        {"baslik": "Hedefe ulaşmak için gereken yüzde", "icerik": [
            "Bir hedefin yüzdeyle verildiği sorularda önce hedefin kendisi sayıya çevrilir, sonra şimdiye kadar yapılan çıkarılarak geriye ne kaldığı bulunur.",
            ornek(
                "$40$ soruluk bir sınavda geçmek için soruların yüzde $75$ ini doğru cevaplamak gerekiyor. Bir öğrenci ilk $25$ sorunun yüzde $80$ ini doğru cevaplamış.",
                "Kalan $15$ sorudan en az kaçını doğru cevaplaması gerektiğini bulalım.",
                "Hedef: $40$ ın yüzde $75$ i, yani $30$ doğru.",
                "Şimdiye kadar: $25$ in yüzde $80$ i, yani $20$ doğru.",
                "Gereken: $30-20=10$ doğru. Kalan $15$ sorunun en az $10$ unu doğru cevaplamalıdır."),
            "Bu tür sorular eşitsizlikle de kurulabilir: kalan sorulardan $d$ doğru yapılırsa $20+d \\geq 30$ olmalıdır. Eşitsizliklerin ayrıntısı <a href=\"/blog/esitsizlikler-konu-anlatimi-pdf/\">Eşitsizlikler Konu Anlatımı PDF</a> yazısında.",
        ]},
        {"baslik": "Bilinmeyen yüzdeyi bulmak", "icerik": [
            "Eski ve yeni değer biliniyor, değişimin yüzdesi soruluyorsa değişim miktarı <strong>eski değere</strong> bölünür ve $100$ ile çarpılır.",
            ornek(
                "Bir ürünün fiyatı $80$ liradan $92$ liraya çıkıyor.",
                "Artışın yüzdesini bulalım.",
                "Artış miktarı: $92-80=12$ lira.",
                "Yüzde: $\\dfrac{12}{80} \\cdot 100=15$. Fiyat yüzde $15$ artmıştır."),
            ornek(
                "Bir ürün yüzde $15$ indirimle $340$ liraya satılıyor.",
                "İndirimsiz fiyatı bulalım.",
                "İndirim çarpanı $0.85$: $0.85x=340$.",
                "$x=340:0.85=400$ lira. Kontrol: $400 \\cdot 0.85=340$."),
        ]},
        {"baslik": "Sınavda yüzde problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) yüzde problemleri art arda değişim, yüzdenin yüzdesi, oranı değişen gruplar ve karşılaştırma soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde yüzde bilgisi grafik yorumlama ve veri analizi sorularında da gerekir."),
            "Bir yüzde sorusuyla karşılaştığında ilk soru \"bu yüzde neyin yüzdesi?\" olmalıdır. Bütünü doğru belirleyen öğrenci için geri kalan iş, bir çarpma ya da bir bölmedir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Art arda yüzdeleri toplamak", "Çarpanları çarp"],
                ["Farklı bütünlerin yüzdelerini toplamak", "Yüzdenin yüzdesi çarpılır"],
                ["Kişi eklenince bütünü sabit tutmak", "Bütün de değişir"],
                ["Fiyat artışı kadar miktar azalır sanmak", "Miktar çarpanı fiyat çarpanının tersi"],
                ["$A$ yüzde $25$ fazlaysa $B$ yüzde $25$ az sanmak", "Yüzde $20$ az"],
                ["Değişimi yeni değere bölmek", "Eski değere böl"],
            ]),
            "Bu hataların hepsinin ortak noktası, yüzdenin hangi bütüne göre alındığını gözden kaçırmaktır. Her yüzdenin yanına bütününü yazmak, hataların çoğunu daha kurulum aşamasında önler.",
        ]},
    ],
    "sss": [
        ("Yüzde problemleri nasıl çözülür?",
         "Önce yüzdenin hangi bütüne göre alındığı belirlenir. Bütün bilinmiyorsa 100 kabul edilir; art arda değişimlerde çarpan yöntemi kullanılır."),
        ("Yüzdenin yüzdesi nasıl bulunur?",
         "İki yüzde çarpılır. Öğrencilerin yüzde 45 i kız ve kızların yüzde 20 si kulüp üyesiyse, üye kızlar öğrencilerin yüzde 9 udur."),
        ("Fiyat yüzde 25 artarsa miktar yüzde kaç azalır?",
         "Harcanan para sabitse miktar çarpanı fiyat çarpanının tersidir. 1,25 in tersi 0,8 olduğu için miktar yüzde 20 azalır."),
        ("A, B den yüzde 25 fazlaysa B, A dan yüzde kaç azdır?",
         "Yüzde 20. Fark aynıdır ama ikinci ifadede bütün A olduğu için yüzde küçülür."),
        ("Art arda iki zam nasıl hesaplanır?",
         "Çarpanlar çarpılır. Yüzde 20 ve yüzde 25 zamın çarpanları 1,2 ve 1,25 tir; çarpımları 1,5 olduğu için toplam etki yüzde 50 artıştır."),
        ("Yüzde değişim neye göre hesaplanır?",
         "Eski değere göre hesaplanır. Değişim miktarı eski değere bölünür ve 100 ile çarpılır."),
        ("İki grubun yüzdeleri birleştirilirken ortalama alınır mı?",
         "Yalnızca gruplar eşit büyüklükteyse alınır. Aksi hâlde her gruptaki sayı ayrı ayrı bulunur, toplanır ve toplam kişi sayısına bölünür."),
        ("Yüzde ile verilen bir hedef nasıl hesaplanır?",
         "Önce hedef sayıya çevrilir, sonra şimdiye kadar yapılan çıkarılır. Geriye kalan miktar, hedefe ulaşmak için gereken en az değerdir."),
        ("Art arda değişimden sonraki fiyattan ilk fiyat nasıl bulunur?",
         "Değişimlerin çarpanları çarpılarak toplam çarpan bulunur ve son fiyat bu çarpana bölünür. Yüzde 20 zam ve yüzde 10 indirimden sonra 540 liraya satılan ürünün ilk fiyatı 500 liradır."),
    ],
    "kontrol": [
        "Bir yüzdenin hangi bütüne göre alındığını belirleyebiliyorum.",
        "Bütünü 100 kabul ederek yüzde sorularını tam sayılarla çözebiliyorum.",
        "Çarpan yöntemiyle art arda değişimleri hesaplayabiliyorum.",
        "Yüzdenin yüzdesini çarparak bulabiliyorum.",
        "Oranı değişen gruplarda hem alt grubu hem bütünü güncelleyebiliyorum.",
        "Fiyat ile miktar arasındaki ters ilişkiyi kullanabiliyorum.",
        "İki niceliği yüzdeyle karşılaştırırken bütünü doğru seçebiliyorum.",
        "Bileşik büyümeyi çarpanın kuvvetiyle hesaplayabiliyorum.",
        "Anket ve dağılım sorularında eksik yüzdeyi bulabiliyorum.",
        "Eski ve yeni değerden değişimin yüzdesini hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["yuzdeler-konu-anlatimi-pdf", "kar-ve-zarar-problemleri-konu-anlatimi-pdf", "faiz-problemleri-nasil-cozulur"],
}
