# scripts/yazilar/73_yuzdeler.py — Yuzdeler (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "yuzdeler-konu-anlatimi-pdf",
    "baslik": "Yüzdeler Konu Anlatımı PDF",
    "aciklama": "Yüzde nedir? Kesir ve ondalıkla dönüşüm, bir sayının yüzdesi, yüzde artış ve azalış, art arda değişim, yüzde puan, indirim ve vergi; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "yuzdeler-konu-anlatimi-pdf",
    "kapak_alt": "Yüzdeler: yüz eş kareden oluşan ızgarada bir kısmı kırmızıyla işaretleyen iki öğrenci",
    "ozet": "Yüzde, bir bütünün yüz eş parçasından kaç tanesinin alındığını söyler. İndirimler, faiz oranları, sınav başarıları, anket sonuçları ve büyüme rakamları hep yüzdeyle anlatılır. Bu yazıda yüzdenin kesir ve ondalık sayıyla ilişkisini, bir sayının yüzdesini bulmanın hızlı yollarını, yüzde artış ve azalışı, art arda gelen yüzde değişimlerde çarpan yöntemini, yüzde ile yüzde puan farkını ve indirim ile vergi hesaplarını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Yüzde nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesirleri ve ondalık gösterimi biliyor olman yeterli.",
                "Ondalık sayılar için <a href=\"/blog/ondalik-gosterim-konu-anlatimi-pdf/\">Ondalık Gösterim Konu Anlatımı PDF</a> yazısına göz at."),
            "Yüzde, paydası $100$ olan bir kesirdir. \"Yüzde yirmi beş\" demek, bir bütünün yüz eş parçasından yirmi beşini almak demektir ve $\\%25$ biçiminde yazılır:",
            "$$\\%25=\\dfrac{25}{100}=\\dfrac{1}{4}=0.25$$",
            "Yüzdenin gücü, farklı büyüklükteki bütünleri aynı ölçekle karşılaştırabilmesidir. $40$ kişilik bir sınıfta $10$ kişi ile $200$ kişilik bir okulda $50$ kişi aynı oranı gösterir: ikisi de yüzde $25$ tir.",
            hap("Yüzde, paydası $100$ olan kesirdir: $\\%a=\\dfrac{a}{100}$.",
                "Yüzde, farklı büyüklükteki bütünleri aynı ölçekle karşılaştırmayı sağlar."),
        ]},
        {"baslik": "Kesir, ondalık sayı ve yüzde arasında dönüşüm", "icerik": [
            "Üç gösterim aynı sayıyı anlatır ve biri ötekine kolayca çevrilir:",
            "<ul><li><strong>Yüzdeden ondalığa:</strong> $100$ e böl, yani virgülü iki basamak sola kaydır: $\\%7=0.07$.</li>"
            "<li><strong>Ondalıktan yüzdeye:</strong> $100$ ile çarp, yani virgülü iki basamak sağa kaydır: $1.2=\\%120$.</li>"
            "<li><strong>Kesirden yüzdeye:</strong> paydayı $100$ yap ya da kesri ondalığa çevirip $100$ ile çarp: $\\dfrac{3}{5}=\\dfrac{60}{100}=\\%60$.</li></ul>",
            tablo(["Kesir", "Ondalık", "Yüzde"], [
                ["$\\dfrac{3}{5}$", "$0.6$", "$\\%60$"],
                ["$\\dfrac{7}{100}$", "$0.07$", "$\\%7$"],
                ["$\\dfrac{6}{5}$", "$1.2$", "$\\%120$"],
                ["$\\dfrac{1}{8}$", "$0.125$", "$\\%12.5$"],
            ]),
            dikkat(
                "Yüzde $100$ den büyük olabilir.",
                "Yüzde $120$, bütünün tamamından yüzde $20$ fazlası demektir. Örneğin bir fiyatın yüzde $120$ si, fiyatın $1.2$ katıdır."),
        ]},
        {"baslik": "Bir sayının yüzdesini bulmak", "icerik": [
            "Bir sayının yüzde $a$ sı, sayının $\\dfrac{a}{100}$ ile çarpımıdır. Kesirlerde olduğu gibi \"-nın yüzdesi\" çarpma demektir.",
            ornek(
                "$240$ sayısı verilsin.",
                "$240$ ın yüzde $15$ ini bulalım.",
                "$240 \\cdot \\dfrac{15}{100}=\\dfrac{3600}{100}=36$."),
            "<h3>Zihinden hızlı hesap</h3>",
            "Bazı yüzdeler akılda kolay hesaplanır ve diğerleri bunların birleşimiyle bulunur:",
            tablo(["Yüzde", "Nasıl bulunur", "$240$ için"], [
                ["$\\%10$", "$10$ a böl", "$24$"],
                ["$\\%5$", "$\\%10$ un yarısı", "$12$"],
                ["$\\%25$", "$4$ e böl", "$60$"],
                ["$\\%50$", "$2$ ye böl", "$120$"],
                ["$\\%15$", "$\\%10+\\%5$", "$36$"],
            ]),
            "Son satır, yukarıdaki örneğin hesapsız çözümünü veriyor: $240$ ın yüzde $10$ u $24$, yüzde $5$ i $12$; toplam $36$.",
            dikkat(
                "Yüzdenin yeri değiştirilebilir.",
                "$a$ nın yüzde $b$ si ile $b$ nin yüzde $a$ sı aynıdır, çünkü ikisi de $\\dfrac{a \\cdot b}{100}$ eder. $50$ nin yüzde $8$ ini bulmak zor görünür ama $8$ in yüzde $50$ si kolaydır: $4$."),
        ]},
        {"baslik": "Yüzdesi verilen sayıyı bulmak", "icerik": [
            "Bir sayının belirli bir yüzdesi biliniyorsa sayının kendisi bulunur. Bu, kesri verilen çokluğu bulmakla aynıdır: verilen miktar yüzdeye bölünür ve $100$ ile çarpılır.",
            ornek(
                "Bir sayının yüzde $30$ u $42$ olsun.",
                "Sayıyı bulalım.",
                "Sayının yüzde $1$ i: $42:30=1.4$.",
                "Sayının tamamı, yani yüzde $100$ ü: $1.4 \\cdot 100=140$."),
            ornek(
                "Bir sınıftaki öğrencilerin yüzde $40$ ı kız ve kız öğrenci sayısı $12$ olsun.",
                "Sınıfta kaç öğrenci vardır?",
                "Yüzde $40$ ı $12$ ise yüzde $10$ u $3$ tür.",
                "Yüzde $100$ ü: $3 \\cdot 10=30$ öğrenci."),
        ]},
        {"baslik": "Bir sayı diğerinin yüzde kaçıdır?", "icerik": [
            "İki sayının oranı yüzde olarak sorulduğunda parça bütüne bölünür ve $100$ ile çarpılır: parça, bütünün yüzde $\\dfrac{\\text{parça}}{\\text{bütün}} \\cdot 100$ ü kadardır.",
            ornek(
                "Bir sınavda $72$ sorudan $18$ i yanlış yapılmış olsun.",
                "Yanlışlar soruların yüzde kaçıdır?",
                "Oran: $\\dfrac{18}{72}=\\dfrac{1}{4}$.",
                "Yüzde olarak: $\\dfrac{1}{4} \\cdot 100=25$; yanlışlar yüzde $25$ tir."),
            ornek(
                "Bir okuldaki $480$ öğrencinin $132$ si bir kulübe üye olsun.",
                "Kulübe üye olanlar öğrencilerin yüzde kaçıdır?",
                "Oran: $\\dfrac{132}{480}=\\dfrac{11}{40}$.",
                "Yüzde olarak: $\\dfrac{11}{40} \\cdot 100=27.5$; üyeler yüzde $27.5$ tir."),
            "Oran sade bir kesre dönüşmüyorsa önce pay ve payda ortak çarpanlarla sadeleştirilir. Böylece $100$ ile çarpma adımı küçük sayılarla yapılır ve hesap hatası azalır.",
        ]},
        {"baslik": "Yüzde artış ve yüzde azalış", "icerik": [
            "Bir değerin ne kadar değiştiği yüzdeyle anlatılırken değişim <strong>eski değere</strong> göre hesaplanır:",
            "$$\\text{Yüzde değişim}=\\dfrac{\\text{yeni}-\\text{eski}}{\\text{eski}} \\cdot 100$$",
            "Sonuç pozitifse artış, negatifse azalıştır.",
            ornek(
                "Bir ürünün fiyatı $80$ liradan $100$ liraya çıkıyor, sonra yeniden $80$ liraya iniyor.",
                "Her iki değişimin yüzdesini bulalım.",
                "Artış: $\\dfrac{100-80}{80} \\cdot 100=\\dfrac{20}{80} \\cdot 100=25$; yüzde $25$ artış.",
                "Azalış: $\\dfrac{80-100}{100} \\cdot 100=-20$; yüzde $20$ azalış."),
            "Aynı $20$ liralık fark, bir yönde yüzde $25$, öbür yönde yüzde $20$ ediyor. Nedeni, iki hesapta bölünen eski değerin farklı olmasıdır: ilkinde $80$, ikincisinde $100$.",
            dikkat(
                "Yüzde artış ile aynı yüzde azalış birbirini götürmez.",
                "Bir değer yüzde $25$ artıp sonra yüzde $25$ azalırsa başa dönmez. Hangi yüzdeyle geri dönüleceği yeni değere göre hesaplanmalıdır."),
        ]},
        {"baslik": "Çarpan yöntemi ve art arda değişim", "icerik": [
            "Yüzde değişimleri hesaplamanın en kısa yolu <strong>çarpan</strong> kullanmaktır. Yüzde $a$ artış, değeri $1+\\dfrac{a}{100}$ ile çarpmak; yüzde $a$ azalış, $1-\\dfrac{a}{100}$ ile çarpmak demektir.",
            tablo(["Değişim", "Çarpan"], [
                ["Yüzde $20$ artış", "$1.2$"],
                ["Yüzde $20$ azalış", "$0.8$"],
                ["Yüzde $5$ artış", "$1.05$"],
                ["Yüzde $35$ azalış", "$0.65$"],
            ]),
            "Art arda gelen değişimlerde çarpanlar çarpılır. Bu, her değişimin bir önceki değişimden sonraki değere uygulandığını otomatik olarak hesaba katar.",
            ornek(
                "Bir fiyat önce yüzde $20$ artıyor, sonra yüzde $20$ azalıyor.",
                "Fiyat başlangıca göre yüzde kaç değişir?",
                "Çarpanlar: $1.2$ ve $0.8$; toplam çarpan $1.2 \\cdot 0.8=0.96$.",
                "$0.96$ çarpanı yüzde $4$ azalış demektir. Fiyat başa dönmez, yüzde $4$ düşer."),
            ornek(
                "Bir değer iki kez art arda yüzde $10$ artıyor.",
                "Toplam artış yüzde kaçtır?",
                "Toplam çarpan: $1.1 \\cdot 1.1=1.21$.",
                "Toplam artış yüzde $21$ dir, yüzde $20$ değil. İkinci artış, birincinin üzerine de uygulanır."),
            hap("Yüzde $a$ artış $1+\\dfrac{a}{100}$, yüzde $a$ azalış $1-\\dfrac{a}{100}$ ile çarpmaktır.",
                "Art arda değişimlerde çarpanlar çarpılır, yüzdeler toplanmaz."),
        ]},
        {"baslik": "Yüzde ile yüzde puan farkı", "icerik": [
            "Bir oran başka bir orana dönüştüğünde değişim iki farklı biçimde anlatılabilir ve bu ikisi birbirine karıştırılabilir.",
            ornek(
                "Bir oran yüzde $10$ dan yüzde $12$ ye çıkıyor.",
                "Değişimi yüzde puan ve yüzde olarak ifade edelim.",
                "Yüzde puan olarak: $12-10=2$; oran $2$ yüzde puan artmıştır.",
                "Yüzde olarak: $\\dfrac{12-10}{10} \\cdot 100=20$; oran yüzde $20$ artmıştır."),
            "İki ifade de doğrudur ama farklı şeyleri anlatır. <strong>Yüzde puan</strong>, iki oranın doğrudan farkıdır. <strong>Yüzde</strong> ise bu farkın eski orana göre büyüklüğüdür. Haberlerde faiz, işsizlik ya da oy oranları anlatılırken bu ayrım önem taşır.",
        ]},
        {"baslik": "İndirim ve vergi", "icerik": [
            "İndirim bir yüzde azalış, fiyata eklenen vergi ise bir yüzde artıştır. İkisi de çarpan yöntemiyle hızlıca çözülür.",
            ornek(
                "Etiket fiyatı $250$ lira olan bir ürüne yüzde $20$ indirim uygulanıyor.",
                "İndirimli fiyatı bulalım.",
                "Çarpan: $0.8$.",
                "İndirimli fiyat: $250 \\cdot 0.8=200$ lira."),
            ornek(
                "Bir ürünün vergi dahil fiyatı $360$ lira ve fiyatın üzerine yüzde $20$ vergi eklenmiş olsun.",
                "Vergisiz fiyatı ve vergi tutarını bulalım.",
                "Vergisiz fiyat $x$ olsun: $1.2x=360$.",
                "$x=360:1.2=300$ lira; vergi tutarı $360-300=60$ lira."),
            dikkat(
                "Vergi dahil fiyattan vergiyi çıkarırken yüzdeyi vergi dahil fiyata uygulama.",
                "$360$ ın yüzde $20$ si $72$ dir ve $360-72=288$ yanlış sonuçtur. Vergi, vergisiz fiyatın yüzde $20$ si olduğu için önce vergisiz fiyat bulunur."),
        ]},
        {"baslik": "Başa dönmek için gereken yüzde", "icerik": [
            "Bir değer yüzde $25$ arttıktan sonra eski değerine dönmesi için yüzde $25$ değil, daha az azalması gerekir. Hesap çarpanlarla yapılır: artış çarpanı $1.25$ ise geri dönüş çarpanı $\\dfrac{1}{1.25}=0.8$ dir, yani yüzde $20$ azalış.",
            ornek(
                "Bir ürünün fiyatı $200$ liradan yüzde $25$ artarak $250$ liraya çıkmış olsun.",
                "Fiyatın yeniden $200$ liraya inmesi için yüzde kaç indirim gerektiğini bulalım.",
                "Azalış miktarı: $250-200=50$ lira.",
                "Yüzde olarak: $\\dfrac{50}{250} \\cdot 100=20$; yüzde $20$ indirim gerekir.",
                "Çarpanla kontrol: $1.25 \\cdot 0.8=1$."),
            "Tersi de geçerlidir: yüzde $20$ azalan bir değerin eski hâline dönmesi için yüzde $25$ artması gerekir, çünkü $0.8 \\cdot 1.25=1$. Geri dönüş yüzdesi her zaman yeni değere göre hesaplanır.",
        ]},
        {"baslik": "Kâr ve zarar", "icerik": [
            "Ticaret sorularında <strong>maliyet</strong>, yani alış fiyatı bütün kabul edilir. Aksi belirtilmedikçe kâr ve zarar yüzdesi maliyet üzerinden hesaplanır: yüzde $a$ kâr maliyeti $1+\\dfrac{a}{100}$ ile, yüzde $a$ zarar maliyeti $1-\\dfrac{a}{100}$ ile çarpmak demektir.",
            ornek(
                "Maliyeti $120$ lira olan bir ürün yüzde $25$ kârla satılıyor.",
                "Satış fiyatını ve kâr tutarını bulalım.",
                "Satış fiyatı: $120 \\cdot 1.25=150$ lira.",
                "Kâr tutarı: $150-120=30$ lira."),
            ornek(
                "Bir ürün yüzde $30$ zararla $91$ liraya satılıyor.",
                "Ürünün maliyetini bulalım.",
                "Maliyet $x$ olsun: $0.7x=91$.",
                "$x=91:0.7=910:7=130$ lira.",
                "Zarar tutarı: $130-91=39$ lira."),
            dikkat(
                "Kâr yüzdesini satış fiyatına göre hesaplamak.",
                "İlk örnekteki $30$ liralık kâr, maliyetin yüzde $25$ i ama satış fiyatının yalnızca yüzde $20$ si kadardır. Soru maliyete göre kârı soruyorsa bölünen sayı maliyettir."),
        ]},
        {"baslik": "Art arda indirim", "icerik": [
            "Bir ürüne önce yüzde $20$, sonra indirimli fiyat üzerinden yüzde $10$ indirim uygulanırsa toplam indirim yüzde $30$ olmaz. Çarpanlar çarpılır: $0.8 \\cdot 0.9=0.72$. Ürün etiket fiyatının yüzde $72$ sine satılır, yani toplam indirim yüzde $28$ dir.",
            ornek(
                "Etiket fiyatı $500$ lira olan bir ürüne art arda yüzde $20$ ve yüzde $10$ indirim uygulanıyor.",
                "Son fiyatı ve toplam indirimi bulalım.",
                "Son fiyat: $500 \\cdot 0.8 \\cdot 0.9=360$ lira.",
                "Toplam indirim: $500-360=140$ lira. Bu, $500$ ün yüzde $28$ i kadardır."),
            "Çarpmanın sırası sonucu değiştirmediği için indirimlerin hangi sırayla uygulandığı son fiyatı etkilemez: önce yüzde $10$, sonra yüzde $20$ indirim de aynı $360$ lirayı verir.",
        ]},
        {"baslik": "Karışım problemlerinde yüzde", "icerik": [
            "Tuzlu su, şekerli su ya da alaşım sorularında yüzde, karışımdaki maddenin toplam kütleye oranıdır. Bu sorularda en güvenli yol, önce maddenin kendi miktarını bulmak, sonra yeni toplamla yeni oranı hesaplamaktır.",
            ornek(
                "$200$ gram yüzde $15$ lik tuzlu suya $50$ gram tuz ekleniyor.",
                "Yeni tuz oranını bulalım.",
                "Başlangıçtaki tuz: $200 \\cdot 0.15=30$ gram.",
                "Yeni tuz miktarı $30+50=80$ gram, yeni toplam $200+50=250$ gram.",
                "Yeni oran: $\\dfrac{80}{250} \\cdot 100=32$; karışım yüzde $32$ lik olur."),
            ornek(
                "Aynı $200$ gram yüzde $15$ lik tuzlu suya bu kez $100$ gram saf su ekleniyor.",
                "Yeni tuz oranını bulalım.",
                "Tuz miktarı değişmez: $30$ gram. Yeni toplam $300$ gram.",
                "Yeni oran: $\\dfrac{30}{300} \\cdot 100=10$; karışım yüzde $10$ luk olur."),
            dikkat(
                "Karışımların yüzdelerini doğrudan toplamak.",
                "Yüzde $10$ luk ve yüzde $30$ luk iki karışım birleştirildiğinde sonuç yüzde $40$ olmaz; eşit miktarlar karıştırılırsa yüzde $20$ olur. Miktarlar farklıysa sonuç, madde miktarlarının toplamının karışımın toplamına oranıdır."),
        ]},
        {"baslik": "Basit faiz ve bileşik faiz", "icerik": [
            "Bankada bekleyen paraya ödenen faiz de bir yüzde hesabıdır. <strong>Basit faizde</strong> faiz yalnızca başlangıçtaki para, yani anapara üzerinden hesaplanır. Faiz tutarı, anaparanın yıllık faiz oranıyla ve yıl cinsinden süreyle çarpımıdır.",
            ornek(
                "$5000$ lira, yıllık yüzde $40$ basit faizle $6$ ay bankada kalıyor.",
                "Faiz tutarını ve dönem sonundaki toplam parayı bulalım.",
                "Süreyi yıla çevirelim: $6$ ay, $\\dfrac{1}{2}$ yıl eder.",
                "Faiz: $5000 \\cdot 0.4 \\cdot \\dfrac{1}{2}=1000$ lira.",
                "Toplam: $5000+1000=6000$ lira."),
            "Faizin her dönem sonunda anaparaya eklendiği ve bir sonraki dönemde onun da faiz kazandığı duruma <strong>bileşik faiz</strong> denir. Bileşik faizde, art arda yüzde artışta olduğu gibi çarpanlar çarpılır. Yıllık yüzde $10$ bileşik faizle iki yılda toplam çarpan $1.1 \\cdot 1.1=1.21$ olur; aynı oranla basit faizde ise iki yılın toplam artışı yüzde $20$ dir.",
            dikkat(
                "Süreyi yıla çevirmeden hesaplamak.",
                "Yıllık oran verilen bir soruda süre ay olarak verilmişse önce yıla çevrilir: $6$ ay yarım yıl, $3$ ay çeyrek yıl eder. Oran aylık verilmişse süre de ay olarak kullanılır."),
        ]},
        {"baslik": "Sınavda yüzdeler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu bir sayının yüzdesi, yüzdesi verilen sayı, yüzde artış ve azalış ve art arda indirim biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde yüzde bilgisi grafik ve tablo yorumlama, fiyat değişimi ve oran karşılaştırma sorularında da gerekebilir."),
            "Yüzde sorularında bütünü $100$ kabul etmek işi kolaylaştırır. Örneğin \"yüzde $20$ artıp yüzde $20$ azalan fiyat\" sorusunda başlangıç fiyatını $100$ almak, sonucu $96$ olarak hemen verir ve yüzde değişim doğrudan okunur.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Değişimi yeni değere göre hesaplamak", "Eski değere göre"],
                ["Yüzde $20$ artış ve azalış başa döner sanmak", "Yüzde $4$ azalır"],
                ["Art arda yüzdeleri toplamak", "Çarpanları çarp"],
                ["Yüzde ile yüzde puanı karıştırmak", "Fark ile oranı ayır"],
                ["Vergiyi vergi dahil fiyattan hesaplamak", "Önce vergisiz fiyatı bul"],
                ["Yüzdenin $100$ ü geçemeyeceğini sanmak", "Yüzde $120$ mümkündür"],
            ]),
            "Bu hataların çoğu, yüzdenin hangi bütüne göre alındığını belirlememekten doğar. Her yüzde sorusunda \"yüzde neyin yüzdesi?\" sorusunu sormak, doğru bütünü seçmeyi sağlar.",
        ]},
    ],
    "sss": [
        ("Yüzde nedir?",
         "Paydası 100 olan bir kesirdir. Yüzde 25, bir bütünün yüz eş parçasından yirmi beşi, yani dörtte biridir."),
        ("Bir sayının yüzdesi nasıl bulunur?",
         "Sayı yüzde oranıyla çarpılıp 100 e bölünür. Örneğin 240 ın yüzde 15 i 36 dır."),
        ("Yüzde artış nasıl hesaplanır?",
         "Yeni değerden eski değer çıkarılır, sonuç eski değere bölünür ve 100 ile çarpılır."),
        ("Yüzde 20 artıp yüzde 20 azalan bir fiyat başa döner mi?",
         "Hayır. Çarpanlar 1,2 ve 0,8 dir; çarpımları 0,96 olduğu için fiyat başlangıca göre yüzde 4 azalır."),
        ("Yüzde ile yüzde puan arasındaki fark nedir?",
         "Yüzde puan iki oranın doğrudan farkıdır. Yüzde ise bu farkın eski orana göre büyüklüğüdür. Yüzde 10 dan yüzde 12 ye çıkış 2 yüzde puan, yüzde 20 artıştır."),
        ("Vergi dahil fiyattan vergisiz fiyat nasıl bulunur?",
         "Vergi dahil fiyat, vergi çarpanına bölünür. Yüzde 20 vergi eklenmiş 360 liralık fiyatın vergisiz hâli 360 bölü 1,2, yani 300 liradır."),
        ("Kâr yüzdesi neye göre hesaplanır?",
         "Aksi belirtilmedikçe maliyete, yani alış fiyatına göre hesaplanır. Kâr tutarı maliyete bölünür ve 100 ile çarpılır."),
        ("Art arda iki indirim toplanır mı?",
         "Hayır. İndirim çarpanları çarpılır. Art arda yüzde 20 ve yüzde 10 indirimin toplam etkisi yüzde 30 değil, yüzde 28 dir."),
        ("Basit faiz nasıl hesaplanır?",
         "Anapara, yıllık faiz oranı ve yıl cinsinden süre çarpılır. Yıllık yüzde 40 basit faizle 5000 liranın 6 aylık faizi 1000 liradır."),
    ],
    "kontrol": [
        "Yüzdeyi paydası $100$ olan kesir olarak açıklayabiliyorum.",
        "Kesir, ondalık sayı ve yüzde arasında dönüşüm yapabiliyorum.",
        "Bir sayının yüzdesini hesaplayabiliyorum.",
        "Yüzde $10$, $5$, $25$ ve $50$ yi zihinden bulabiliyorum.",
        "Yüzdesi verilen sayıyı bulabiliyorum.",
        "Bir sayının diğerinin yüzde kaçı olduğunu hesaplayabiliyorum.",
        "Yüzde artış ve azalışı eski değere göre hesaplayabiliyorum.",
        "Art arda yüzde değişimlerini çarpan yöntemiyle hesaplayabiliyorum.",
        "Yüzde ile yüzde puan farkını açıklayabiliyorum.",
        "İndirimli ve vergisiz fiyatı doğru bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["ondalik-gosterim-konu-anlatimi-pdf", "oran-ve-oranti-konu-anlatimi-pdf", "kesirler-konu-anlatimi-pdf"],
}
