# scripts/yazilar/67_kesirler.py — Kesirler (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kesirler-konu-anlatimi-pdf",
    "baslik": "Kesirler Konu Anlatımı PDF",
    "aciklama": "Kesir nedir? Pay ve payda, kesir modelleri, basit, bileşik ve tam sayılı kesir, denk kesirler, bir çokluğun kesri ve kesir problemleri; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kesirler-konu-anlatimi-pdf",
    "kapak_alt": "Kesirler: dilimlere ayrılmış mavi daire ve renkli kesir çubuklarıyla bütünün parçalarını inceleyen iki öğrenci",
    "ozet": "Kesirler, bir bütünün eş parçalarını anlatmanın yoludur: bir pastanın dörtte üçü, bir yolun yarısı, bir sınıfın beşte ikisi. Bu yazıda kesrin ne olduğunu, pay ve paydanın anlamını, kesri görmenin üç farklı modelini, basit, bileşik ve tam sayılı kesirleri, denk kesirleri ve sadeleştirmeyi, bir çokluğun kesrini bulmayı, kesirlerin ondalık ve yüzde karşılıklarını ve kesir problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kesir nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi ve bölme kavramını biliyor olman yeterli.",
                "Kesirlerin rasyonel sayılarla bağlantısı için <a href=\"/blog/rasyonel-sayilar-konu-anlatimi-pdf/\">Rasyonel Sayılar Konu Anlatımı PDF</a> yazısına göz at."),
            "Bir bütün <strong>eş</strong> parçalara bölündüğünde, bu parçalardan bir kısmını anlatan sayıya <strong>kesir</strong> denir. $\\dfrac{a}{b}$ biçiminde yazılır. Alttaki $b$ sayısına <strong>payda</strong> denir ve bütünün kaç eş parçaya bölündüğünü söyler. Üstteki $a$ sayısına <strong>pay</strong> denir ve bu parçalardan kaç tanesinin alındığını söyler. Aradaki çizgiye <strong>kesir çizgisi</strong> denir.",
            "Örneğin bir pizza $8$ eş dilime bölünür ve $3$ dilim yenirse yenen kısım $\\dfrac{3}{8}$ tür: payda $8$, pay $3$. \"Sekizde üç\" diye okunur. Türkçede kesir önce payda, sonra pay söylenerek okunur.",
            dikkat(
                "Parçaların eş olması şarttır.",
                "Bir pizza biri büyük biri küçük iki parçaya ayrılırsa her parça \"yarım\" değildir. Kesir, ancak bütün eşit büyüklükte parçalara bölündüğünde anlam taşır."),
            "<h3>Payda neden sıfır olamaz?</h3>",
            "Kesir aynı zamanda bir bölme işlemidir: $\\dfrac{a}{b}=a:b$. Sıfıra bölme tanımsız olduğu için paydası sıfır olan bir kesir de tanımsızdır. Anlamı da bunu gösterir: bir bütünü sıfır parçaya bölmek mümkün değildir. Pay ise sıfır olabilir: $\\dfrac{0}{5}=0$ dır, yani hiç parça alınmamıştır.",
            hap("Payda bütünün kaç eş parçaya bölündüğünü, pay kaç parçanın alındığını söyler.",
                "Payda sıfır olamaz; pay sıfır olursa kesrin değeri sıfırdır."),
        ]},
        {"baslik": "Kesri görmenin üç yolu", "icerik": [
            "Aynı kesir üç farklı biçimde düşünülebilir. Soruya göre birini seçmek çözümü kolaylaştırır.",
            "<ul><li><strong>Alan modeli:</strong> bir şekil eş parçalara bölünür, bazı parçalar boyanır. $\\dfrac{3}{4}$, dört eş parçadan üçünün boyandığı bir karedir.</li>"
            "<li><strong>Sayı doğrusu modeli:</strong> $0$ ile $1$ arası payda kadar eş parçaya bölünür ve pay kadar ilerlenir. $\\dfrac{3}{4}$, $0$ dan başlayıp dört eş adımın üçünü atınca varılan noktadır.</li>"
            "<li><strong>Küme modeli:</strong> bir nesne topluluğu eş gruplara ayrılır. $12$ bilyenin $\\dfrac{3}{4}$ ü, bilyeleri $4$ eş gruba ayırıp $3$ grubu almak demektir: $9$ bilye.</li></ul>",
            "Hangi modelin seçileceği sorunun diline bağlıdır: pasta ve alan sorularında alan modeli, yol ve uzunluk sorularında sayı doğrusu, sınıf ve grup sorularında küme modeli doğal olarak işe yarar. Aynı soruyu iki farklı modelle düşünmek, bulduğun sonucu kontrol etmenin de kolay ve güvenilir bir yoludur.",
            "Sayı doğrusu modeli, kesirleri sıralarken ve $1$ den büyük kesirleri düşünürken özellikle işe yarar. Ayrıntısı için <a href=\"/blog/sayi-dogrusu-ve-sayilari-siralama/\">Sayı Doğrusu ve Sayıları Sıralama</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kesir türleri", "icerik": [
            "Pozitif kesirler, pay ile paydanın karşılaştırılmasına göre üç türe ayrılır:",
            tablo(["Tür", "Koşul", "Örnek"], [
                ["Basit kesir", "Pay paydadan küçük", "$\\dfrac{3}{5}$"],
                ["Bileşik kesir", "Pay paydaya eşit ya da büyük", "$\\dfrac{7}{4}$"],
                ["Tam sayılı kesir", "Tam sayı ve basit kesir", "$1\\dfrac{3}{4}$"],
            ]),
            "Basit kesir $1$ den küçüktür, çünkü bütünün tamamı alınmamıştır. Bileşik kesir $1$ e eşit ya da $1$ den büyüktür. Tam sayılı kesir, bileşik kesrin başka bir yazılışıdır: $1\\dfrac{3}{4}$, \"bir tam dörtte üç\" diye okunur ve $1+\\dfrac{3}{4}$ anlamına gelir.",
            "<h3>Bileşik kesir ile tam sayılı kesir arasında dönüşüm</h3>",
            ornek(
                "$\\dfrac{11}{4}$ ve $3\\dfrac{2}{5}$ verilsin.",
                "Birincisini tam sayılı, ikincisini bileşik kesir olarak yazalım.",
                "$11:4$ işleminde bölüm $2$, kalan $3$: $\\dfrac{11}{4}=2\\dfrac{3}{4}$.",
                "Tam kısmı paydayla çarpıp paya ekleyelim: $3 \\cdot 5+2=17$.",
                "$3\\dfrac{2}{5}=\\dfrac{17}{5}$."),
            dikkat(
                "Tam sayılı kesir bir çarpım değildir.",
                "$2\\dfrac{3}{4}$, $2 \\cdot \\dfrac{3}{4}$ anlamına gelmez; $2+\\dfrac{3}{4}=\\dfrac{11}{4}$ anlamına gelir. İşlemlerde karışıklık olmaması için tam sayılı kesri önce bileşik kesre çevirmek güvenlidir."),
        ]},
        {"baslik": "Birim kesirler", "icerik": [
            "Payı $1$ olan kesirlere <strong>birim kesir</strong> denir: $\\dfrac{1}{2}$, $\\dfrac{1}{3}$, $\\dfrac{1}{10}$ gibi. Her kesir, birim kesirlerin tekrarı olarak düşünülebilir: $\\dfrac{3}{8}$, üç tane $\\dfrac{1}{8}$ demektir.",
            "Bazı kesirler farklı birim kesirlerin toplamı olarak da yazılabilir: $\\dfrac{3}{4}=\\dfrac{1}{2}+\\dfrac{1}{4}$ ve $\\dfrac{5}{6}=\\dfrac{1}{2}+\\dfrac{1}{3}$ dir. Bu yazım, bir bütünü farklı büyüklükte parçalarla paylaştırmayı düşünmek için kullanışlıdır.",
            "Birim kesirlerde payda büyüdükçe kesir küçülür. Bir pastayı $2$ kişiyle paylaşmak, $10$ kişiyle paylaşmaktan daha büyük bir dilim verir: $\\dfrac{1}{10}<\\dfrac{1}{2}$. Kesirleri karşılaştırırken bu sezgi çok işe yarar.",
        ]},
        {"baslik": "Denk kesirler ve sadeleştirme", "icerik": [
            "Aynı miktarı gösteren kesirlere <strong>denk kesirler</strong> denir. Bir kesrin payı ve paydası sıfırdan farklı aynı sayıyla çarpılırsa kesir <strong>genişletilmiş</strong> olur; aynı sayıya bölünürse <strong>sadeleştirilmiş</strong> olur. İki işlem de kesrin değerini değiştirmez.",
            "$$\\dfrac{2}{3}=\\dfrac{4}{6}=\\dfrac{10}{15}=\\dfrac{20}{30}$$",
            "Bunun nedeni modelde görülür: bir bütünü $3$ yerine $6$ parçaya böldüğünde her parça yarıya iner, ama $2$ parça yerine $4$ parça aldığın için toplam miktar aynı kalır.",
            "Pay ve paydanın $1$ den başka ortak böleni kalmayınca kesir <strong>en sade</strong> hâlindedir. En sade hâle tek adımda ulaşmak için pay ve payda EBOB'larına bölünür.",
            ornek(
                "$\\dfrac{36}{48}$ kesri verilsin.",
                "Kesri en sade hâline getirelim.",
                "$\\text{EBOB}(36, 48)=12$.",
                "Pay ve paydayı $12$ ye bölelim: $\\dfrac{36}{48}=\\dfrac{3}{4}$."),
            "EBOB'un nasıl bulunduğu için <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısına bakabilirsin.",
            dikkat(
                "Sadeleştirmede yalnızca çarpanlar bölünür, terimler bölünmez.",
                "$\\dfrac{2+6}{2}$ kesrinde $2$ ler sadeleşmez: değer $\\dfrac{8}{2}=4$ tür, $1+6=7$ değildir. Pay bir toplam olduğunda önce toplam hesaplanır."),
        ]},
        {"baslik": "Bir çokluğun kesri", "icerik": [
            "Bir çokluğun $\\dfrac{a}{b}$ sını bulmak için çokluk paydaya bölünür, çıkan sonuç payla çarpılır. Bu, çokluğu $b$ eş gruba ayırıp $a$ grubunu almak demektir.",
            ornek(
                "$60$ sayısı verilsin.",
                "$60$ ın $\\dfrac{2}{5}$ sini bulalım.",
                "$60$ ı $5$ eş gruba ayıralım: $60:5=12$.",
                "$2$ grup alalım: $12 \\cdot 2=24$."),
            "<h3>Kesri verilen çokluğu bulmak</h3>",
            "Tersinden de sorulabilir: bir sayının kesri biliniyorsa sayının kendisi bulunur. Bu durumda verilen miktar paya bölünür, çıkan sonuç paydayla çarpılır.",
            ornek(
                "Bir sayının $\\dfrac{3}{7}$ ü $21$ olsun.",
                "Sayıyı bulalım.",
                "$7$ eş parçadan $3$ ü $21$ ise bir parça $21:3=7$ dir.",
                "Sayı $7$ parçanın tamamıdır: $7 \\cdot 7=49$."),
            hap("Çokluğun kesri: çokluğu paydaya böl, payla çarp.",
                "Kesri verilen çokluk: verilen miktarı paya böl, paydayla çarp."),
        ]},
        {"baslik": "Kesir ve kalanlı bölme", "icerik": [
            "Kesir, bölmenin sonucunu tam olarak yazmanın yoludur. Tam sayılarda kalanlı bölme bir bölüm ve bir kalan verir; kesir ise kalanı da paylaştırır.",
            ornek(
                "$17$ ekmek $5$ kişiye eşit olarak paylaştırılsın.",
                "Kişi başına ne kadar ekmek düşer?",
                "Kalanlı bölme: $17=5 \\cdot 3+2$. Her kişi $3$ bütün ekmek alır, $2$ ekmek artar.",
                "Artan $2$ ekmek de $5$ e bölünür: her kişiye $\\dfrac{2}{5}$ ekmek daha düşer.",
                "Kişi başına $3\\dfrac{2}{5}=\\dfrac{17}{5}$ ekmek düşer."),
            "Bu örnek, tam sayılı kesrin anlamını da gösterir: tam kısım bölüm, kesrin payı kalan, paydası bölendir.",
        ]},
        {"baslik": "Günlük hayatta kesirler", "icerik": [
            "Kesirler günlük dilin içindedir. \"Yarım saat\", \"çeyrek saat\", \"üçte bir indirim\" gibi ifadelerin hepsi bir kesri anlatır. Bu ifadeleri sayıya çevirmek, birçok problemi hızlıca çözmeyi sağlar.",
            tablo(["Günlük ifade", "Kesir", "Örnek değer"], [
                ["Yarım saat", "$\\dfrac{1}{2}$ saat", "$30$ dakika"],
                ["Çeyrek saat", "$\\dfrac{1}{4}$ saat", "$15$ dakika"],
                ["Üç çeyrek", "$\\dfrac{3}{4}$ saat", "$45$ dakika"],
                ["Dörtte bir indirim", "$\\dfrac{1}{4}$", "$200$ liralık üründe $50$ lira"],
            ]),
            ornek(
                "Bir öğrenci günde $2$ saat ders çalışıyor ve bu sürenin $\\dfrac{3}{4}$ ünü matematiğe ayırıyor.",
                "Matematiğe günde kaç dakika ayırır?",
                "$2$ saat $120$ dakikadır.",
                "$120$ nin $\\dfrac{3}{4}$ ü: $120:4=30$ ve $30 \\cdot 3=90$ dakika."),
        ]},
        {"baslik": "Denk kesir problemleri", "icerik": [
            "Bir kesre denk olan kesirlerin hepsi, pay ve paydanın aynı sayıyla çarpılmasıyla elde edilir. Bu yüzden $\\dfrac{2}{3}$ ye denk her kesir $\\dfrac{2k}{3k}$ biçimindedir. Bu gözlem, bir koşulu sağlayan denk kesri bulmayı kolaylaştırır.",
            ornek(
                "$\\dfrac{2}{3}$ ye denk olan ve payı ile paydasının toplamı $35$ olan kesir aransın.",
                "Bu kesri bulalım.",
                "Kesir $\\dfrac{2k}{3k}$ biçimindedir; $2k+3k=35$ ise $k=7$.",
                "Kesir: $\\dfrac{14}{21}$. Kontrol: $14+21=35$ ve $\\dfrac{14}{21}=\\dfrac{2}{3}$."),
            ornek(
                "$\\dfrac{3}{5}$ e denk olan ve paydası payından $12$ fazla olan kesir aransın.",
                "Bu kesri bulalım.",
                "Kesir $\\dfrac{3k}{5k}$ biçimindedir; $5k-3k=12$ ise $k=6$.",
                "Kesir: $\\dfrac{18}{30}$."),
        ]},
        {"baslik": "Pay ve payda değişince kesir nasıl değişir?", "icerik": [
            "Pozitif bir kesirde payda sabitken pay artarsa kesir büyür; pay sabitken payda artarsa kesir küçülür. Pay ile payda aynı sayıyla çarpılırsa ya da bölünürse kesir değişmez.",
            "<ul><li>Pay iki katına çıkarsa kesir iki katına çıkar: $\\dfrac{3}{8}$ ten $\\dfrac{6}{8}$ ya.</li>"
            "<li>Payda iki katına çıkarsa kesir yarıya iner: $\\dfrac{3}{8}$ ten $\\dfrac{3}{16}$ e.</li>"
            "<li>İkisi birden iki katına çıkarsa kesir aynı kalır: $\\dfrac{3}{8}=\\dfrac{6}{16}$.</li></ul>",
            "Bu kurallar, kesirleri karşılaştırmanın da temelidir; ayrıntısı <a href=\"/blog/kesirlerde-siralama-ve-karsilastirma/\">Kesirlerde Sıralama ve Karşılaştırma</a> yazısında.",
        ]},
        {"baslik": "Kesir, ondalık sayı ve yüzde", "icerik": [
            "Kesir bir bölme işlemi olduğu için her kesir bölme yapılarak ondalık sayıya çevrilebilir: $\\dfrac{7}{4}=7:4=1.75$. Paydası $100$ olan bir kesir de yüzde olarak okunur: $\\dfrac{25}{100}$, yüzde $25$ tir.",
            tablo(["Kesir", "Ondalık", "Yüzde"], [
                ["$\\dfrac{1}{2}$", "$0.5$", "$\\%50$"],
                ["$\\dfrac{1}{4}$", "$0.25$", "$\\%25$"],
                ["$\\dfrac{3}{4}$", "$0.75$", "$\\%75$"],
                ["$\\dfrac{1}{5}$", "$0.2$", "$\\%20$"],
                ["$\\dfrac{1}{8}$", "$0.125$", "$\\%12.5$"],
            ]),
            "Her kesrin ondalık gösterimi sonlu değildir. $\\dfrac{1}{3}=0.333\\ldots$ gibi bazı kesirlerin ondalık gösterimi sonsuza kadar tekrar eder. Bu sayılara devirli ondalık sayı denir; ayrıntısı <a href=\"/blog/rasyonel-sayilar-konu-anlatimi-pdf/\">Rasyonel Sayılar Konu Anlatımı PDF</a> yazısında.",
            dikkat(
                "Sonlu ondalık gösterim paydaya bağlıdır.",
                "En sade hâldeki bir kesrin paydasında $2$ ve $5$ ten başka asal çarpan yoksa ondalık gösterimi sonludur: $\\dfrac{3}{8}=0.375$. Paydada başka bir asal varsa, örneğin $\\dfrac{1}{6}$ daki $3$ gibi, gösterim devirlidir."),
        ]},
        {"baslik": "Kesir problemleri", "icerik": [
            "Kesir problemlerinde en önemli soru şudur: kesir <strong>neyin</strong> kesri? \"Kalanın\" kesri ile \"tamamın\" kesri farklı sonuçlar verir.",
            ornek(
                "Bir kitabın önce $\\dfrac{1}{3}$ i, sonra kalan sayfaların $\\dfrac{1}{4}$ i okunuyor ve geriye $60$ sayfa kalıyor.",
                "Kitap kaç sayfadır?",
                "İlk okumadan sonra kalan: $1-\\dfrac{1}{3}=\\dfrac{2}{3}$.",
                "İkinci okuma kalanın $\\dfrac{1}{4}$ i: $\\dfrac{1}{4} \\cdot \\dfrac{2}{3}=\\dfrac{1}{6}$. Geriye $\\dfrac{2}{3}-\\dfrac{1}{6}=\\dfrac{1}{2}$ kalır.",
                "Kitabın yarısı $60$ sayfa ise kitap $120$ sayfadır."),
            ornek(
                "Bir su deposunun $\\dfrac{2}{5}$ si dolu. Depoya $21$ litre su eklenince deponun $\\dfrac{3}{4}$ ü doluyor.",
                "Deponun tamamı kaç litredir?",
                "Eklenen su, iki kesrin farkı kadardır: $\\dfrac{3}{4}-\\dfrac{2}{5}=\\dfrac{15}{20}-\\dfrac{8}{20}=\\dfrac{7}{20}$.",
                "Deponun $\\dfrac{7}{20}$ si $21$ litre: bir parça $21:7=3$ litre.",
                "Depo $20 \\cdot 3=60$ litredir."),
            ornek(
                "Bir sınıftaki öğrencilerin $\\dfrac{3}{8}$ ü kız ve kız öğrenci sayısı $12$ olsun.",
                "Sınıfta kaç erkek öğrenci vardır?",
                "$8$ parçanın $3$ ü $12$ ise bir parça $4$ öğrencidir; sınıf $8 \\cdot 4=32$ kişidir.",
                "Erkekler $\\dfrac{5}{8}$ lik kısımdır: $5 \\cdot 4=20$ erkek öğrenci."),
            ornek(
                "Bir otobüsteki yolcuların $\\dfrac{2}{7}$ si ilk durakta iniyor, ardından $4$ yolcu biniyor ve otobüste $24$ yolcu oluyor.",
                "Başlangıçta otobüste kaç yolcu vardır?",
                "Başlangıçtaki yolcu sayısı $x$ olsun. İnenlerden sonra kalan: $x-\\dfrac{2}{7}x=\\dfrac{5}{7}x$.",
                "$4$ yolcu binince: $\\dfrac{5}{7}x+4=24$, yani $\\dfrac{5}{7}x=20$.",
                "$x=20 \\cdot \\dfrac{7}{5}=28$ yolcu."),
            dikkat(
                "\"Kalanın\" kesrini \"tamamın\" kesri gibi alma.",
                "Kitap örneğinde ikinci okuma kitabın $\\dfrac{1}{4}$ i değil, kalan $\\dfrac{2}{3}$ lik kısmın $\\dfrac{1}{4}$ idir. Tamamın $\\dfrac{1}{4}$ i alınsaydı yanlış sonuç çıkardı."),
        ]},
        {"baslik": "Kesirlerle işlemlere giriş", "icerik": [
            "Kesirlerle dört işlem ayrı yazılarda ayrıntılı anlatılıyor. Burada kısa bir özet:",
            "<ul><li><strong>Toplama ve çıkarma:</strong> paydalar eşitlenir, paylar toplanır ya da çıkarılır. Ayrıntı: <a href=\"/blog/kesirlerde-toplama-ve-cikarma/\">Kesirlerde Toplama ve Çıkarma</a>.</li>"
            "<li><strong>Çarpma ve bölme:</strong> paylar ve paydalar çarpılır; bölmede ikinci kesir ters çevrilip çarpılır. Ayrıntı: <a href=\"/blog/kesirlerde-carpma-ve-bolme/\">Kesirlerde Çarpma ve Bölme</a>.</li>"
            "<li><strong>Sıralama:</strong> paydalar ya da paylar eşitlenir, çapraz çarpım yapılır. Ayrıntı: <a href=\"/blog/kesirlerde-siralama-ve-karsilastirma/\">Kesirlerde Sıralama ve Karşılaştırma</a>.</li></ul>",
        ]},
        {"baslik": "Sınavda kesirler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kesirler hem doğrudan işlem sorusu olarak hem de problemlerin içinde karşına çıkabilir: bir çokluğun kesri, kalanın kesri ve depo problemleri gibi.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde kesir bilgisi sayısal akıl yürütme sorularında oran, pay ve bütün ilişkisi kurmak için de gerekebilir."),
            "Kesir problemlerinde bütünü bir değişkenle göstermek ya da bütünü paydaların EKOK'u kadar birim kabul etmek işi kolaylaştırır. Örneğin depo problemlerinde depoyu $20$ birim kabul etmek, $\\dfrac{2}{5}$ si $8$ birim, $\\dfrac{3}{4}$ ü $15$ birim yapar ve kesirlerle uğraşmadan çözüme ulaştırır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Eş olmayan parçaları kesirle anlatmak", "Parçalar eş olmalı"],
                ["Paydası sıfır olan kesir yazmak", "Payda sıfır olamaz"],
                ["$2\\dfrac{3}{4}$ ü $2 \\cdot \\dfrac{3}{4}$ sanmak", "$2+\\dfrac{3}{4}=\\dfrac{11}{4}$"],
                ["Toplamda terimleri sadeleştirmek", "Önce toplamı hesapla"],
                ["Kalanın kesrini tamamın kesri almak", "Kesrin neyin kesri olduğuna bak"],
                ["$\\dfrac{1}{10}>\\dfrac{1}{2}$ sanmak", "Payda büyüdükçe birim kesir küçülür"],
            ]),
            "Bu hataların ortak noktası, kesrin bir bütünün eş parçalarını anlattığını unutmaktır. Emin olmadığında kesri bir çizimle, örneğin eş parçalara bölünmüş bir dikdörtgenle göstermek doğru yolu hemen ortaya çıkarır.",
        ]},
    ],
    "sss": [
        ("Kesir nedir?",
         "Bir bütünün eş parçalarından bir kısmını anlatan sayıdır. Payda bütünün kaç eş parçaya bölündüğünü, pay bu parçalardan kaç tanesinin alındığını gösterir."),
        ("Tam sayılı kesir ne anlama gelir?",
         "Bir tam sayı ile bir basit kesrin toplamıdır. Örneğin üç tam beşte iki, üç artı beşte iki demektir ve beşte on yedi olarak da yazılabilir."),
        ("Payda neden sıfır olamaz?",
         "Kesir bir bölme işlemidir ve sıfıra bölme tanımsızdır. Bir bütünü sıfır parçaya bölmek de mümkün değildir."),
        ("Basit, bileşik ve tam sayılı kesir arasındaki fark nedir?",
         "Basit kesirde pay paydadan küçüktür. Bileşik kesirde pay paydaya eşit ya da büyüktür. Tam sayılı kesir ise bileşik kesrin tam sayı ve basit kesir olarak yazılışıdır."),
        ("Kesir ile bölme arasında nasıl bir ilişki vardır?",
         "Her kesir bir bölme işlemidir: pay paydaya bölünür. Kalanlı bölmede tam kısım bölümü, kesrin payı kalanı, paydası da böleni gösterir."),
        ("Denk kesir nedir?",
         "Aynı miktarı gösteren kesirlerdir. Bir kesrin payı ve paydası sıfırdan farklı aynı sayıyla çarpılır ya da bölünürse denk bir kesir elde edilir."),
        ("Bir sayının kesri nasıl bulunur?",
         "Sayı kesrin paydasına bölünür ve çıkan sonuç payla çarpılır. Örneğin 60 ın beşte ikisi 24 tür."),
        ("Her kesir sonlu bir ondalık sayıya çevrilebilir mi?",
         "Hayır. En sade hâldeki kesrin paydasında 2 ve 5 ten başka asal çarpan varsa ondalık gösterim devirli olur, örneğin üçte bir."),
    ],
    "kontrol": [
        "Pay ve paydanın ne anlattığını bir örnekle açıklayabiliyorum.",
        "Paydanın neden sıfır olamayacağını açıklayabiliyorum.",
        "Bir kesri alan, sayı doğrusu ve küme modeliyle gösterebiliyorum.",
        "Basit, bileşik ve tam sayılı kesirleri ayırt edebiliyorum.",
        "Bileşik kesir ile tam sayılı kesir arasında dönüşüm yapabiliyorum.",
        "Denk kesir yazıp bir kesri EBOB ile en sade hâline getirebiliyorum.",
        "Bir çokluğun kesrini ve kesri verilen çokluğu bulabiliyorum.",
        "Temel kesirlerin ondalık ve yüzde karşılıklarını biliyorum.",
        "Bir kesrin ondalık gösteriminin sonlu olup olmayacağını paydadan anlayabiliyorum.",
        "Kalanın kesri ile tamamın kesrini ayırt ederek problem çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kesirlerde-siralama-ve-karsilastirma", "kesirlerde-toplama-ve-cikarma", "rasyonel-sayilar-konu-anlatimi-pdf"],
}
