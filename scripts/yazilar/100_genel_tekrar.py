# scripts/yazilar/100_genel_tekrar.py — Temel Matematik Problemleri Genel Tekrar (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "temel-matematik-problemleri-genel-tekrar",
    "baslik": "Temel Matematik Problemleri Genel Tekrar",
    "aciklama": "Temel matematik problemleri tek yazıda: sayı, kesir, yaş, yüzde, kâr-zarar, faiz, oran, işçi, hareket, karışım, ortalama, sayma ve küme problemleri; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "temel-matematik-problemleri-genel-tekrar",
    "kapak_alt": "Temel matematik problemleri genel tekrar: terazi, kesir dairesi ve bloklardan oluşan düzenekle problem çözen üç öğrenci",
    "ozet": "Problem soruları, temel matematiğin bütün konularını bir araya getirir: bir yaş sorusu denklem kurmayı, bir kâr sorusu yüzde hesabını, bir karışım sorusu oran kurmayı ister. Bu yazı, problem türlerinin her birini temel kuralı ve çözümlü bir örnekle özetleyen bir genel tekrardır. Önce bütün problemlerde işe yarayan dört adımlı çözüm yöntemini, sonra sayı, kesir, yaş, yüzde, kâr ve zarar, faiz, oran ve orantı, işçi ve havuz, hareket, karışım, ortalama, sayma ve küme problemlerini ele alıyoruz.",
    "bolumler": [
        {"baslik": "Problem çözmenin dört adımı", "icerik": [
            onkosul(
                "Bu yazı bir genel tekrardır; her problem türünün ayrıntılı anlatımı kendi yazısında yer alıyor.",
                "Denklem kurmanın temelleri için <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "Problem türü ne olursa olsun, çözüm aynı dört adımla ilerler. Bu adımları alışkanlık hâline getirmek, hangi konudan gelirse gelsin yeni bir soruyla karşılaşıldığında nereden başlanacağını gösterir.",
            tablo(["Adım", "Ne yapılır?"], [
                ["Anla", "Verilenleri ve isteneni ayır"],
                ["Planla", "Bilinmeyeni seç, ilişkiyi yaz"],
                ["Çöz", "Denklemi ya da işlemi yap"],
                ["Kontrol et", "Sonucu soruya yerleştir"],
            ]),
            hap("Önce isteneni yaz, sonra bilinmeyeni seç.",
                "Bulduğun sonucu mutlaka sorunun içine yerleştirip kontrol et."),
        ]},
        {"baslik": "Bilinmeyeni doğru seçmek", "icerik": [
            "Birden fazla bilinmeyen varsa en küçük ya da diğerlerinin kendisine göre tanımlandığı büyüklük $x$ seçilir. Böylece diğer büyüklükler $x$ cinsinden kesirsiz yazılır ve denklem sade kalır.",
            ornek(
                "İki sayının toplamı $48$ dir ve büyük sayı küçük sayının $3$ katıdır.",
                "Sayıları bulalım.",
                "Küçük sayı $x$ olsun; büyük sayı $3x$ olur.",
                "$x+3x=48$, yani $4x=48$ ve $x=12$. Sayılar $12$ ve $36$ dır."),
            "Büyük sayı $x$ seçilseydi küçük sayı $\\dfrac{x}{3}$ olurdu ve denklemde kesirle uğraşmak gerekirdi. Sonuç aynıdır ama yol uzar ve hata olasılığı artar.",
        ]},
        {"baslik": "Sayı problemleri", "icerik": [
            "Sayı problemlerinde sözel ifadeler matematik diline çevrilir: \"katı\" çarpma, \"fazlası\" toplama, \"eksiği\" çıkarma demektir. Çeviri doğru yapılırsa geriye yalnızca birinci dereceden bir denklem kalır.",
            ornek(
                "Bir sayının $3$ katının $7$ fazlası, aynı sayının $5$ katından $9$ eksiktir.",
                "Sayıyı bulalım.",
                "$3x+7=5x-9$.",
                "$16=2x$, yani $x=8$. Kontrol: $3 \\cdot 8+7=31$ ve $5 \\cdot 8-9=31$."),
            "Ayrıntılı anlatım: <a href=\"/blog/sayi-problemleri-konu-anlatimi-pdf/\">Sayı Problemleri Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Kesir problemleri", "icerik": [
            "Kesir problemlerinde en önemli ayrım, kesrin bütünün mü yoksa kalanın mı kesri olduğudur. \"Kalanın\" ifadesi geçtiğinde her adımda yeni bütün, bir önceki adımdan kalan kısımdır.",
            ornek(
                "Bir öğrenci harçlığının üçte birini kitaba, kalanın dörtte birini yemeğe harcıyor ve geriye $300$ TL kalıyor.",
                "Harçlığı bulalım.",
                "Kitaptan sonra harçlığın üçte ikisi kalır. Yemekten sonra bu kalanın dörtte üçü kalır.",
                "Kalan: $\\dfrac{2}{3} \\cdot \\dfrac{3}{4}=\\dfrac{1}{2}$. Harçlığın yarısı $300$ TL ise harçlık $600$ TL.",
                "Kontrol: kitaba $200$, kalan $400$; yemeğe $100$, kalan $300$."),
            "Ayrıntılı anlatım: <a href=\"/blog/kesir-problemleri-nasil-cozulur/\">Kesir Problemleri Nasıl Çözülür?</a>",
        ]},
        {"baslik": "Yaş problemleri", "icerik": [
            "Yaş problemlerinin temel gerçeği şudur: zaman herkes için aynı hızla geçer. Bu yüzden iki kişinin yaş farkı hiçbir zaman değişmez ve $t$ yıl sonra herkesin yaşı $t$ kadar artar.",
            ornek(
                "Bir anne $38$, kızı $10$ yaşındadır.",
                "Kaç yıl sonra annenin yaşının kızının yaşının $2$ katı olacağını bulalım.",
                "$t$ yıl sonra: $38+t=2(10+t)$.",
                "$38+t=20+2t$, yani $t=18$. Kontrol: anne $56$, kız $28$ yaşında olur."),
            dikkat(
                "Yaş farkının zamanla değiştiğini sanmak.",
                "Anne ile kızı arasındaki fark hem bugün hem $18$ yıl sonra $28$ yıldır. Yaşların oranı değişir ama farkı değişmez."),
            "Ayrıntılı anlatım: <a href=\"/blog/yas-problemleri-konu-anlatimi-pdf/\">Yaş Problemleri Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Yüzde problemleri", "icerik": [
            "Yüzde problemlerinde başlangıç değeri $100$ seçmek hesabı çok kolaylaştırır. Art arda yapılan yüzde değişimleri toplanmaz; her değişim bir öncekinin sonucuna uygulanır.",
            ornek(
                "Bir ürünün fiyatına önce $\\%20$ zam, sonra yeni fiyat üzerinden $\\%20$ indirim yapılıyor.",
                "Son fiyatın ilk fiyata göre değişimini bulalım.",
                "İlk fiyat $100$ olsun. Zamdan sonra $120$.",
                "İndirim $120$ nin $\\%20$ si, yani $24$ tür. Son fiyat $96$.",
                "Son fiyat ilk fiyattan $\\%4$ düşüktür."),
            "Ayrıntılı anlatım: <a href=\"/blog/yuzde-problemleri-nasil-cozulur/\">Yüzde Problemleri Nasıl Çözülür?</a>",
        ]},
        {"baslik": "Kâr ve zarar problemleri", "icerik": [
            "Kâr ve zarar yüzdeleri her zaman maliyet üzerinden hesaplanır. Satış fiyatı, maliyete kârın eklenmesiyle ya da maliyetten zararın çıkarılmasıyla bulunur.",
            ornek(
                "Maliyeti $400$ TL olan bir ürün $\\%25$ kârla satılıyor. Başka bir üründe satış fiyatı $360$ TL olduğunda $\\%20$ zarar ediliyor.",
                "Birinci ürünün satış fiyatını ve ikinci ürünün maliyetini bulalım.",
                "Birinci ürün: $400 \\cdot 1.25=500$ TL.",
                "İkinci ürün: satış fiyatı maliyetin $\\%80$ idir. Maliyet: $360:0.8=450$ TL."),
            "Ayrıntılı anlatım: <a href=\"/blog/kar-ve-zarar-problemleri-konu-anlatimi-pdf/\">Kâr ve Zarar Problemleri Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Faiz problemleri", "icerik": [
            "Basit faizde faiz yalnızca ana para üzerinden hesaplanır ve her yıl aynı miktarda eklenir. Faiz, ana para, yıllık faiz oranı ve süre çarpılıp $100$ e bölünerek bulunur.",
            "$$\\text{Faiz}=\\dfrac{\\text{ana para} \\cdot \\text{oran} \\cdot \\text{yıl}}{100}$$",
            ornek(
                "$20000$ TL, yıllık $\\%15$ basit faizle $2$ yıl bankada tutuluyor.",
                "Faizi ve dönem sonundaki toplam parayı bulalım.",
                "Faiz: $\\dfrac{20000 \\cdot 15 \\cdot 2}{100}=6000$ TL.",
                "Toplam: $20000+6000=26000$ TL."),
            "Ayrıntılı anlatım: <a href=\"/blog/faiz-problemleri-nasil-cozulur/\">Faiz Problemleri Nasıl Çözülür?</a>",
        ]},
        {"baslik": "Oran ve orantı problemleri", "icerik": [
            "Oranla paylaştırmada her pay bir $k$ sayısıyla yazılır: $3$ ve $5$ ile orantılı paylar $3k$ ve $5k$ dır. Ters orantıda ise çarpım sabittir: işçi sayısı artarsa iş süresi aynı oranda azalır.",
            ornek(
                "$400$ TL, $3$ ve $5$ sayılarıyla doğru orantılı olarak iki kişiye paylaştırılıyor. Ayrıca $6$ işçinin $10$ günde bitirdiği bir işi aynı hızda çalışan $4$ işçi yapacak.",
                "Payları ve $4$ işçinin işi kaç günde bitireceğini bulalım.",
                "$3k+5k=400$, yani $k=50$. Paylar $150$ ve $250$ TL.",
                "İşçi sayısı ile süre ters orantılıdır: $6 \\cdot 10=4 \\cdot t$, yani $t=15$ gün."),
            "Ayrıntılı anlatım: <a href=\"/blog/oran-ve-oranti-problemleri/\">Oran ve Orantı Problemleri</a>.",
        ]},
        {"baslik": "İşçi ve havuz problemleri", "icerik": [
            "İşçi ve havuz problemlerinde süre değil, bir birim zamanda yapılan iş toplanır. Bir işi $a$ günde bitiren kişi bir günde işin $\\dfrac{1}{a}$ ini yapar; havuzu boşaltan musluğun hızı eksi işaretle yazılır.",
            ornek(
                "A bir işi $6$ günde, B aynı işi $12$ günde bitiriyor. Ayrıca bir havuzu bir musluk $4$ saatte dolduruyor, bir başka musluk $6$ saatte boşaltıyor.",
                "İşin birlikte kaç günde biteceğini ve iki musluk birlikte açıkken boş havuzun kaç saatte dolacağını bulalım.",
                "Birlikte bir günde: $\\dfrac{1}{6}+\\dfrac{1}{12}=\\dfrac{3}{12}=\\dfrac{1}{4}$. İş $4$ günde biter.",
                "Musluklar birlikte bir saatte: $\\dfrac{1}{4}-\\dfrac{1}{6}=\\dfrac{1}{12}$. Havuz $12$ saatte dolar."),
            "Ayrıntılı anlatım: <a href=\"/blog/isci-ve-havuz-problemleri-konu-anlatimi-pdf/\">İşçi ve Havuz Problemleri Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Hareket problemleri", "icerik": [
            "Hareket problemlerinin tek formülü yol eşittir hız çarpı zamandır. Birbirine doğru giden araçlarda hızlar toplanır, aynı yönde giden araçlarda ise hızların farkı alınır.",
            ornek(
                "Aralarında $420$ kilometre bulunan iki şehirden iki araç aynı anda birbirine doğru saatte $60$ ve $80$ kilometre hızla yola çıkıyor.",
                "Araçların kaç saat sonra karşılaşacağını bulalım.",
                "Araçlar her saatte $60+80=140$ kilometre yaklaşır.",
                "Karşılaşma süresi: $420:140=3$ saat."),
            "Ayrıntılı anlatım: <a href=\"/blog/hareket-problemleri-konu-anlatimi-pdf/\">Hareket Problemleri Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Karışım problemleri", "icerik": [
            "Karışım problemlerinde yüzdeler değil, saf madde miktarları toplanır. Her karışımdaki saf madde bulunur, toplanır ve yeni toplam miktara bölünür.",
            ornek(
                "Tuz oranı $\\%20$ olan $300$ gram tuzlu suya $100$ gram tuz ekleniyor.",
                "Yeni karışımın tuz oranını bulalım.",
                "İlk tuz: $300 \\cdot 0.2=60$ gram. Yeni tuz: $60+100=160$ gram.",
                "Yeni toplam: $400$ gram. Tuz oranı: $\\dfrac{160}{400}=0.4$, yani $\\%40$."),
            "Ayrıntılı anlatım: <a href=\"/blog/karisim-problemleri-konu-anlatimi-pdf/\">Karışım Problemleri Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Ortalama problemleri", "icerik": [
            "Ortalama problemlerinde ortalamadan toplama geçilir, işlem toplam üzerinde yapılır ve en son yeni değer sayısına bölünür.",
            ornek(
                "Beş sayının ortalaması $16$ dır. Altıncı bir sayı eklenince ortalama $18$ oluyor.",
                "Eklenen sayıyı bulalım.",
                "Beş sayının toplamı: $5 \\cdot 16=80$. Altı sayının toplamı: $6 \\cdot 18=108$.",
                "Eklenen sayı: $108-80=28$."),
            "Ayrıntılı anlatım: <a href=\"/blog/aritmetik-ortalama-ve-veri-analizi/\">Aritmetik Ortalama ve Veri Analizi</a>.",
        ]},
        {"baslik": "Sayma ve olasılık problemleri", "icerik": [
            "Sayma problemlerinde ilk karar, sıranın önemli olup olmadığıdır: sıra önemliyse permütasyon, değilse kombinasyon kullanılır. Olasılık ise istenen durumların sayısının bütün durumların sayısına bölümüdür.",
            ornek(
                "$4$ kişi bir sıraya dizilecek. Ayrıca iki zar atılıyor.",
                "Dizilim sayısını ve zarların toplamının $7$ olma olasılığını bulalım.",
                "Dizilim: $4!=24$.",
                "İki zarda $36$ eşit olası sonuç vardır ve toplamı $7$ yapan $6$ sonuç bulunur: $\\dfrac{6}{36}=\\dfrac{1}{6}$."),
            "Ayrıntılı anlatım: <a href=\"/blog/permutasyon-konu-anlatimi-pdf/\">Permütasyon Konu Anlatımı PDF</a> ve <a href=\"/blog/olasilik-konu-anlatimi-pdf/\">Olasılık Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Küme problemleri", "icerik": [
            "Küme problemlerinde iki kümenin birleşiminin eleman sayısı, eleman sayılarının toplamından ortak kısmın çıkarılmasıyla bulunur. Venn şeması kesişimden başlanarak doldurulur.",
            ornek(
                "$50$ kişilik bir grupta $32$ kişi çay, $28$ kişi kahve içiyor ve $6$ kişi ikisini de içmiyor.",
                "İkisini birden içenlerin sayısını bulalım.",
                "En az birini içen: $50-6=44$.",
                "İkisini birden içen: $32+28-44=16$."),
            "Ayrıntılı anlatım: <a href=\"/blog/kumeler-konu-anlatimi-pdf/\">Kümeler Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "Basamak problemleri", "icerik": [
            "Rakamlarla kurulan problemlerde sayı çözümlenerek yazılır: onlar basamağı $a$, birler basamağı $b$ olan iki basamaklı sayı $10a+b$ dir. Rakamların yeri değişince sayı $10b+a$ olur ve iki sayının farkı $9(b-a)$ çıkar.",
            ornek(
                "İki basamaklı bir sayının rakamları toplamı $11$ dir. Rakamların yeri değiştirilince sayı $27$ artıyor.",
                "Sayıyı bulalım.",
                "$9(b-a)=27$, yani $b-a=3$. Ayrıca $a+b=11$.",
                "İki eşitlik toplanınca $2b=14$, yani $b=7$ ve $a=4$. Sayı $47$ dir. Kontrol: $74-47=27$."),
            "Ayrıntılı anlatım: <a href=\"/blog/sayi-basamaklari-konu-anlatimi-pdf/\">Sayı Basamakları Konu Anlatımı PDF</a>.",
        ]},
        {"baslik": "İki bilinmeyenli problemler", "icerik": [
            "Bazı problemlerde iki bilinmeyen ve iki ayrı bilgi verilir. Her bilgi bir denklem olarak yazılır ve denklemlerden biri diğerinden çıkarılarak bir bilinmeyen yok edilir.",
            ornek(
                "Bir kumbarada $5$ liralık ve $1$ liralık toplam $20$ madenî para var ve paraların toplam değeri $60$ lira.",
                "Her türden kaç para olduğunu bulalım.",
                "$5$ liralıkların sayısı $x$, $1$ liralıkların sayısı $y$ olsun: $x+y=20$ ve $5x+y=60$.",
                "İkinci denklemden birincisi çıkarılınca $4x=40$, yani $x=10$ ve $y=10$. Kontrol: $10 \\cdot 5+10 \\cdot 1=60$."),
            "Aynı soru tek bilinmeyenle de çözülebilir: bütün paralar $1$ liralık olsaydı toplam $20$ lira olurdu. Eksik kalan $40$ lira, her $5$ liralığın getirdiği $4$ liralık fazlalıktan gelir; bu yüzden $40:4=10$ tane $5$ liralık vardır.",
        ]},
        {"baslik": "Grafikten problem çözmek", "icerik": [
            "Bazı problemlerde veriler bir tablo ya da grafikle verilir. Bu sorularda önce grafiğin başlığı, eksenleri ve birimi okunur; sonra gereken değerler alınıp bilinen problem kurallarıyla işlem yapılır.",
            ornek(
                "Bir daire grafiğinde $240$ öğrencinin okula geliş biçimleri gösteriliyor ve yürüyerek gelenlerin diliminin merkez açısı $90$ derece.",
                "Yürüyerek gelen öğrenci sayısını bulalım.",
                "$90$ derece dairenin dörtte biridir.",
                "Yürüyerek gelen: $240:4=60$ öğrenci."),
            "Ayrıntılı anlatım: <a href=\"/blog/tablo-ve-grafik-yorumlama/\">Tablo ve Grafik Yorumlama</a>.",
        ]},
        {"baslik": "Ortadaki değerden başlamak", "icerik": [
            "Ardışık sayılarla kurulan problemlerde ortadaki sayıyı bilinmeyen seçmek, denklemi en kısa hâle getirir. Ardışık sayıların ortalaması ortadaki sayıya eşit olduğu için ortadaki sayı, toplamın terim sayısına bölümüdür.",
            ornek(
                "Ardışık üç tek sayının toplamı $57$ dir.",
                "Sayıları bulalım.",
                "Ortadaki sayı: $57:3=19$.",
                "Sayılar $17$, $19$ ve $21$ dir. Kontrol: $17+19+21=57$."),
            "Aynı fikir çift sayıda terimde de işler: ardışık dört sayının toplamı $50$ ise ortalamaları $12.5$ tir ve sayılar $11$, $12$, $13$ ve $14$ tür. Ayrıntılı anlatım: <a href=\"/blog/ardisik-sayilar/\">Ardışık Sayılar</a>.",
        ]},
        {"baslik": "Çok adımlı problemler", "icerik": [
            "Sınav sorularının çoğu tek bir konuyla sınırlı kalmaz: bir kâr sorusu yüzde hesabı, bir karışım sorusu oran kurmayı da ister. Bu sorularda her adımda yalnızca bir büyüklük bulunur ve bir sonraki adıma geçilir.",
            ornek(
                "Bir mağaza bir ürünü $\\%25$ kârla $500$ TL fiyatla satıyor. Mağaza satış fiyatında $\\%10$ indirim yapıyor.",
                "İndirimden sonraki kâr yüzdesini bulalım.",
                "Maliyet: $500:1.25=400$ TL.",
                "Yeni satış fiyatı: $500 \\cdot 0.9=450$ TL. Yeni kâr: $450-400=50$ TL.",
                "Kâr yüzdesi: $\\dfrac{50}{400} \\cdot 100=12.5$; kâr $\\%12.5$ e düşer."),
            dikkat(
                "İndirim yüzdesini kâr yüzdesinden doğrudan çıkarmak.",
                "$\\%25-\\%10=\\%15$ demek yanlıştır. Kâr maliyet üzerinden, indirim ise satış fiyatı üzerinden hesaplanır; iki yüzdenin tabanı farklıdır."),
        ]},
        {"baslik": "Sonucu kontrol etmek", "icerik": [
            "Bulunan sonucu kontrol etmenin üç yolu vardır. Birincisi, sonucu sorudaki bütün koşullara yerleştirmektir. İkincisi birimdir: yol kilometre, süre saat, fiyat TL cinsinden çıkmalıdır. Üçüncüsü mantıklılıktır: negatif bir yaş, kesirli bir işçi sayısı ya da yüzde yüzü aşan bir tuz oranı, bir yerde hata yapıldığını gösterir.",
            "Seçenekli sorularda seçenekler de bir kontrol aracıdır. Denklem kurmak zor geliyorsa seçenekler sırayla soruya yerleştirilebilir; koşulların hepsini sağlayan seçenek doğru cevaptır. Bu yöntem yavaş olabilir ama özellikle yaş ve sayı problemlerinde güvenilir bir yedek yoldur.",
        ]},
        {"baslik": "Sınavda problemler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) problemler sayı, kesir, yaş, yüzde, kâr ve zarar, oran, işçi, hareket, karışım ve ortalama gibi türlerden oluşabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de problemler sayısal akıl yürütmenin önemli bir parçasıdır."),
            "Problem sorularında hız, çok sayıda soru çözerek kazanılır; ama çözülen her sorunun hangi türe girdiğini ve hangi kuralla çözüldüğünü not etmek, aynı türün bir sonraki sorusunu çok daha hızlı tanımayı sağlar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Kalanın kesrini bütünün kesri sanmak", "Her adımda yeni bütün kalandır"],
                ["Yaş farkının değiştiğini sanmak", "Yaş farkı sabittir"],
                ["Art arda yüzdeleri toplamak", "Her değişim yeni değere uygulanır"],
                ["Kâr yüzdesini satış fiyatından almak", "Kâr maliyet üzerinden hesaplanır"],
                ["İşçi problemlerinde süreleri toplamak", "Birim zamanda yapılan işler toplanır"],
                ["Karışımda yüzdeleri toplamak", "Saf madde miktarları toplanır"],
                ["Sonucu kontrol etmemek", "Sonucu sorunun içine yerleştir"],
            ]),
            "Bu hataların çoğu, sorunun hangi büyüklük üzerinden kurulduğunu gözden kaçırmaktan doğar. Her problemde \"neyin yüzdesi\", \"neyin kesri\" ve \"hangi zamandaki yaş\" sorularını sormak, hataların büyük bölümünü önler.",
        ]},
    ],
    "sss": [
        ("Problem sorularına nasıl başlanır?",
         "Önce verilenler ve istenen ayrılır. Sonra bilinmeyen seçilir, ilişki denklem olarak yazılır, denklem çözülür ve sonuç soruya yerleştirilerek kontrol edilir."),
        ("Bilinmeyen nasıl seçilir?",
         "Diğer büyüklüklerin kendisine göre tanımlandığı ya da en küçük olan büyüklük seçilir. Böylece denklem kesirsiz ve sade kalır."),
        ("Art arda yapılan zam ve indirim neden birbirini götürmez?",
         "Çünkü ikinci yüzde, ilk değişimden sonraki yeni fiyat üzerinden hesaplanır. Yüzde 20 zam ve ardından yüzde 20 indirim, fiyatı yüzde 4 düşürür."),
        ("Kâr yüzdesi neye göre hesaplanır?",
         "Kâr ve zarar yüzdeleri maliyet üzerinden hesaplanır. Maliyeti 400 TL olan ürün yüzde 25 kârla 500 TL fiyatla satılır."),
        ("İşçi problemlerinde neden süreler toplanmaz?",
         "Çünkü birlikte çalışmak süreyi kısaltır. Her kişinin bir günde yaptığı iş toplanır ve işin tamamının bu toplam hıza bölünmesiyle süre bulunur."),
        ("Karışım problemlerinde neler toplanır?",
         "Yüzdeler değil, her karışımdaki saf madde miktarları toplanır. Yeni oran, toplam saf maddenin toplam karışım miktarına bölümüdür."),
    ],
    "kontrol": [
        "Problem çözmenin dört adımını uygulayabiliyorum.",
        "Bilinmeyeni denklemi sade tutacak biçimde seçebiliyorum.",
        "Sözel ifadeleri matematik diline çevirebiliyorum.",
        "Kalanın kesri ile bütünün kesrini ayırt edebiliyorum.",
        "Yaş problemlerinde yaş farkının sabit olduğunu kullanabiliyorum.",
        "Art arda yüzde değişimlerini doğru hesaplayabiliyorum.",
        "Kâr ve zarar yüzdesini maliyet üzerinden hesaplayabiliyorum.",
        "İşçi ve havuz problemlerinde birim zamandaki işi kullanabiliyorum.",
        "Karışım problemlerinde saf madde miktarlarıyla çalışabiliyorum.",
        "Bulduğum sonucu soruya yerleştirerek kontrol edebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["denklem-kurma-problemleri-nasil-cozulur", "yuzde-problemleri-nasil-cozulur", "aritmetik-ortalama-ve-veri-analizi"],
}
