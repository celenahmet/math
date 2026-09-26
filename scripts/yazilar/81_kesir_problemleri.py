# scripts/yazilar/81_kesir_problemleri.py — Kesir Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kesir-problemleri-nasil-cozulur",
    "baslik": "Kesir Problemleri Nasıl Çözülür?",
    "aciklama": "Kesir problemleri nasıl çözülür? Parçadan bütüne, bütünden parçaya, kalanın kesri, şerit modeli, doluluk ve paylaşım soruları; adım adım çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kesir-problemleri-nasil-cozulur",
    "kapak_alt": "Kesir problemleri: kesir daireleri ve bloklarla parça ile bütün ilişkisini modelleyen iki öğrenci",
    "ozet": "Kesir problemlerinin hepsi aynı soruya dayanır: hangi bütünün hangi parçası? Bütünü doğru belirleyen öğrenci için bu problemler birkaç satırlık hesaba dönüşür; bütünü karıştıran içinse en kolay soru bile içinden çıkılmaz hâle gelir. Bu yazıda bir çokluğun kesrini bulmayı, kesri verilen çokluğun tamamını bulmayı, kalanın kesri sorularını, şerit modelini, doluluk ve paylaşım problemlerini ve kesirli ifadelerle denklem kurmayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kesir problemi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesirlerle dört işlemi ve basit denklem kurmayı biliyor olman yeterli.",
                "Kesirlerin temeli için <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a>, denklem kurmak için <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "Kesir problemlerinde bir bütünün belirli bir parçası üzerinden bilgi verilir: bir sınıfın beşte ikisi, bir deponun dörtte üçü, bir bütçenin kalanının yarısı gibi. Soru ya parçayı ya da bütünü ister. Bütün ile parça arasındaki köprü her zaman aynıdır: <strong>parça, bütün ile kesrin çarpımıdır</strong>.",
            "$$\\text{Parça}=\\text{Bütün} \\cdot \\text{Kesir}$$",
            "Bu eşitlikten iki temel soru türü çıkar. Bütün biliniyorsa parça çarparak bulunur; parça biliniyorsa bütün bölerek bulunur. Kesir problemlerinin geri kalanı, bu iki adımın farklı biçimlerde birleştirilmesidir.",
            hap("Parça, bütün ile kesrin çarpımıdır.",
                "Bütün biliniyorsa çarp, parça biliniyorsa böl."),
        ]},
        {"baslik": "Bir çokluğun kesrini bulmak", "icerik": [
            "Bir çokluğun kesrini bulmak için çokluk kesirle çarpılır. Aynı işlem iki adımda da düşünülebilir: önce çokluk paydaya bölünerek bir parçanın değeri bulunur, sonra pay kadar parça alınır.",
            ornek(
                "$60$ kişilik bir toplulukta üyelerin beşte ikisi etkinliğe katılmış olsun.",
                "Kaç kişinin katıldığını bulalım.",
                "Bir parça: $60:5=12$ kişi.",
                "Beşte iki: $2 \\cdot 12=24$ kişi.",
                "Tek adımda: $60 \\cdot \\dfrac{2}{5}=24$."),
            "İki adımlı yol, özellikle zihinden hesapta işe yarar. Önce bölmek sayıları küçültür ve çarpma kolaylaşır. Çokluk paydaya tam bölünmüyorsa sonuç kesirli çıkar; kişi ya da nesne sayısı soruluyorsa bu, sorunun yeniden okunması gerektiğini gösterir.",
        ]},
        {"baslik": "Kesri verilen çokluğun tamamını bulmak", "icerik": [
            "Bir çokluğun belirli bir kesri biliniyor ve çokluğun tamamı soruluyorsa işlem tersine çevrilir: verilen parça pay sayısına bölünerek bir parçanın değeri bulunur, sonra payda kadar parça alınır.",
            ornek(
                "Bir sınıftaki öğrencilerin yedide üçü kız ve kız öğrenci sayısı $12$ olsun.",
                "Sınıfın mevcudunu bulalım.",
                "Üç parça $12$ öğrenci ise bir parça $12:3=4$ öğrencidir.",
                "Yedi parça: $7 \\cdot 4=28$ öğrenci.",
                "Denklemle: $\\dfrac{3}{7}x=12$ ise $x=12 \\cdot \\dfrac{7}{3}=28$."),
            dikkat(
                "Parçayı kesirle çarpmak.",
                "Kızlar sınıfın yedide üçüyse sınıf mevcudu $12 \\cdot \\dfrac{3}{7}$ değildir; bu işlem $12$ den de küçük bir sayı verir ve bütünün parçadan küçük olması anlamsızdır. Bütün her zaman parçadan büyüktür."),
            hap("Kesri verilen çokluğun tamamını bulmak için verilen parça pay sayısına bölünür, sonra payda kadar parça alınır."),
        ]},
        {"baslik": "Şerit modeli", "icerik": [
            "Kesir problemlerini çözmenin en görsel yolu <strong>şerit modelidir</strong>. Bütün bir şerit olarak çizilir ve paydadaki sayı kadar eş parçaya bölünür. Sorudaki bilgiler bu parçaların üzerine yazılır ve bir parçanın değeri bulunduğunda geri kalan her şey okunur.",
            "Kapaktaki kesir daireleri ve bloklar da aynı fikri anlatır: bir bütün eş parçalara bölündüğünde her parçanın değeri aynıdır ve kesir, kaç parça alındığını söyler.",
            ornek(
                "Bir kulüp bütçesinin üçte birini etkinliğe, dörtte birini tanıtıma ayırıyor ve geriye $2500$ lira kalıyor.",
                "Bütçenin tamamını şerit modeliyle bulalım.",
                "Paydalar $3$ ve $4$; şeridi EKOK kadar, yani $12$ eş parçaya bölelim.",
                "Etkinlik $12$ nin üçte biri kadar, yani $4$ parça; tanıtım dörtte biri kadar, yani $3$ parça alır. Kalan $12-4-3=5$ parçadır.",
                "$5$ parça $2500$ lira ise bir parça $500$ lira; bütçe $12 \\cdot 500=6000$ liradır."),
            "Şerit modeli, kesirleri ortak paydaya getirmenin görsel hâlidir. $12$ parçalık şerit, üç ve dört paydalı kesirlerin ortak paydası olan $12$ nin kendisidir.",
        ]},
        {"baslik": "Kalanın kesri", "icerik": [
            "Kesir problemlerinin en çok karıştırılan türü, kesrin bütüne değil <strong>bir önceki adımdan kalana</strong> uygulandığı sorulardır. \"Kalanın\" kelimesi görüldüğünde her adımda geriye ne kaldığı ayrı ayrı yazılmalıdır.",
            ornek(
                "Bir öğrenci bir kitabın ilk gün dörtte birini, ikinci gün kalan sayfaların beşte ikisini okuyor ve geriye $135$ sayfa kalıyor.",
                "Kitabın kaç sayfa olduğunu bulalım.",
                "Kitap $x$ sayfa olsun. İlk günden sonra kalan: $x-\\dfrac{x}{4}=\\dfrac{3x}{4}$.",
                "İkinci gün okunan: $\\dfrac{3x}{4} \\cdot \\dfrac{2}{5}=\\dfrac{3x}{10}$. Kalan: $\\dfrac{3x}{4}-\\dfrac{3x}{10}=\\dfrac{9x}{20}$.",
                "$\\dfrac{9x}{20}=135$, yani $x=300$ sayfa. Kontrol: ilk gün $75$, kalan $225$; ikinci gün $90$, kalan $135$."),
            "<h3>Kısa yol: kalan oranlarını çarpmak</h3>",
            "Her adımda kalan oran yazılıp bu oranlar çarpılırsa hesap tek satıra iner. İlk gün dörtte biri okununca dörtte üçü kalır; ikinci gün kalanın beşte ikisi okununca beşte üçü kalır. Toplam kalan oran $\\dfrac{3}{4} \\cdot \\dfrac{3}{5}=\\dfrac{9}{20}$ dur ve $\\dfrac{9}{20}x=135$ denklemi aynı sonucu verir.",
            dikkat(
                "Kalanın kesrini bütüne uygulamak.",
                "İkinci gün okunan sayfa kitabın beşte ikisi değil, kalan sayfaların beşte ikisidir. Kesir bütüne uygulanırsa ikinci gün $120$ sayfa okunmuş sanılır ve denklem yanlış kurulur."),
            hap("Soruda kalanın kesri geçiyorsa kesir bütüne değil, bir önceki adımdan kalana uygulanır."),
        ]},
        {"baslik": "Parçadan parçaya geçmek", "icerik": [
            "Bazen bir kesir verilir ve aynı sayının başka bir kesri sorulur. Bu durumda önce bütün bulunur, sonra istenen kesir hesaplanır. İki adım tek bir çarpımda da birleştirilebilir.",
            ornek(
                "Bir sayının dörtte biri $18$ dir.",
                "Aynı sayının üçte ikisini bulalım.",
                "Bütün: $18 \\cdot 4=72$.",
                "Üçte iki: $72 \\cdot \\dfrac{2}{3}=48$.",
                "Tek satırda: $18 \\cdot 4 \\cdot \\dfrac{2}{3}=48$."),
            "Bu tür sorularda bütünü gerçekten hesaplamak, sonucun doğruluğunu kontrol etmeyi de kolaylaştırır: $72$ nin dörtte biri gerçekten $18$ dir.",
        ]},
        {"baslik": "Kesrin kesri", "icerik": [
            "Bir grubun bir kısmının da bir kısmı sorulduğunda kesirler çarpılır. \"Kızların dörtte biri\" ifadesindeki bütün sınıf değil, kızlardır; bu yüzden sonuç sınıfa göre iki kesrin çarpımıyla ifade edilir.",
            ornek(
                "Bir sınıftaki öğrencilerin üçte ikisi kızdır ve kızların dörtte biri gözlüklüdür. Sınıfta $36$ öğrenci vardır.",
                "Gözlüklü kızların sınıfın kaçta kaçı olduğunu ve sayısını bulalım.",
                "Gözlüklü kızların sınıfa oranı: $\\dfrac{2}{3} \\cdot \\dfrac{1}{4}=\\dfrac{2}{12}=\\dfrac{1}{6}$.",
                "Sayısı: $36 \\cdot \\dfrac{1}{6}=6$ öğrenci.",
                "Kontrol: kızlar $24$, bunların dörtte biri $6$."),
            dikkat(
                "\"Kaçta kaçı\" ile \"kaç tane\" sorularını karıştırmak.",
                "\"Kaçta kaçı\" sorusu bir kesir ister; cevap $\\dfrac{1}{6}$ dir. \"Kaç tane\" sorusu ise bir sayı ister; cevap $6$ dır. Soru kökünü dikkatle okumak, doğru hesabı yapıp yanlış seçeneği işaretlemeyi önler."),
            hap("Bir grubun bir kısmının da bir kısmı sorulduğunda kesirler çarpılır."),
        ]},
        {"baslik": "İş ve süre içeren kesir soruları", "icerik": [
            "Bir işin belirli bir kesrinin ne kadar sürede yapıldığı biliniyorsa, çalışma hızı değişmediği sürece işin tamamının süresi de bulunur. Burada bütün, işin tamamıdır ve süre, yapılan kesirle doğru orantılıdır.",
            ornek(
                "Bir işçi bir işin beşte ikisini $6$ günde bitiriyor.",
                "İşin tamamını ve kalan kısmını kaç günde bitireceğini bulalım.",
                "İşin beşte biri $6:2=3$ günde yapılır.",
                "İşin tamamı, yani beşte beşi $5 \\cdot 3=15$ gün sürer.",
                "Kalan kısım beşte üçtür: $3 \\cdot 3=9$ gün. Kontrol: $6+9=15$."),
            "Birden fazla kişinin birlikte çalıştığı iş ve havuz problemleri de kesirlerle kurulur: bir işi $a$ günde bitiren kişi bir günde işin $a$ da birini yapar. Bu kurulumun ayrıntısı <a href=\"/blog/dogru-oranti-ve-ters-oranti/\">Doğru Orantı ve Ters Orantı</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Kesirle indirim ve artış", "icerik": [
            "İndirim ve artışlar yüzde yerine kesirle de verilebilir. Beşte bir indirim fiyatın beşte dördünün ödenmesi, dörtte bir artış ise fiyatın dörtte beşinin ödenmesi demektir.",
            ornek(
                "Bir ürünün fiyatına beşte bir indirim uygulanınca ürün $480$ liraya satılıyor.",
                "İndirimsiz fiyatı bulalım.",
                "İndirimden sonra fiyatın beşte dördü kalır: $\\dfrac{4}{5}x=480$.",
                "$x=480 \\cdot \\dfrac{5}{4}=600$ lira.",
                "Beşte bir indirim, yüzde $20$ indirimle aynıdır: $600 \\cdot 0.8=480$."),
            "Kesir ile yüzde arasındaki geçiş <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a> yazısında ayrıntılı olarak anlatılıyor.",
        ]},
        {"baslik": "Doluluk problemleri", "icerik": [
            "Depo, şişe ya da havuz gibi kaplar üzerinden kurulan sorularda bütün, kabın tam kapasitesidir. Kesirler kabın ne kadarının dolu olduğunu, eklenen ya da boşaltılan miktar ise iki kesir arasındaki farkı gösterir.",
            ornek(
                "Bir depo beşte ikisi doluyken içine $30$ litre su ekleniyor ve depo onda yedisi dolu hâle geliyor.",
                "Deponun kapasitesini bulalım.",
                "Kapasite $x$ litre olsun. Eklenen su, iki doluluk arasındaki farktır: $\\dfrac{7}{10}x-\\dfrac{2}{5}x=30$.",
                "$\\dfrac{2}{5}=\\dfrac{4}{10}$ olduğu için fark $\\dfrac{3}{10}x$ tir: $\\dfrac{3}{10}x=30$, yani $x=100$ litre.",
                "Kontrol: başta $40$ litre, $30$ litre eklenince $70$ litre; $70$ litre $100$ ün onda yedisidir."),
            ornek(
                "Tam dolu bir şişedeki suyun üçte biri içiliyor, sonra kalan suyun yarısı bir bardağa dökülüyor. Şişede $200$ mililitre su kalıyor.",
                "Şişenin kapasitesini bulalım.",
                "Kalan oranlar: önce üçte iki, sonra yarısı. Toplam kalan oran $\\dfrac{2}{3} \\cdot \\dfrac{1}{2}=\\dfrac{1}{3}$ dir.",
                "$\\dfrac{1}{3}x=200$, yani şişe $600$ mililitredir."),
            "Doluluk sorularında kabın başlangıçta boş mu dolu mu olduğunu ve her işlemden sonra kabın kaçta kaçının dolu kaldığını yazmak, bütün kurulumu sadeleştirir. Eklenen ve boşaltılan miktarlar her zaman aynı bütüne, yani kabın kapasitesine göre kesre çevrilir.",
            hap("$60$ litrelik deposunun $\\dfrac{1}{4}$ i dolu olan bir aracın deposunu doldurmak için $60 \\cdot \\dfrac{3}{4}=45$ litre yakıt gerekir.", "Doldurulacak kısım, bütünden dolu kısım çıkarılarak bulunur.", gunluk=True),
        ]},
        {"baslik": "Kesirli ifadelerle denklem kurmak", "icerik": [
            "Bazı sorularda aynı sayının iki farklı kesri birbiriyle karşılaştırılır. Bu durumda sayıya $x$ denir, kesirler $x$ ile çarpılarak yazılır ve iki taraf paydaların EKOK'u ile çarpılarak kesirlerden kurtulunur.",
            ornek(
                "Bir sayının üçte ikisinin $4$ fazlası, aynı sayının dörtte üçüne eşittir.",
                "Sayıyı bulalım.",
                "Denklem: $\\dfrac{2x}{3}+4=\\dfrac{3x}{4}$.",
                "İki tarafı $12$ ile çarpalım: $8x+48=9x$, yani $x=48$.",
                "Kontrol: $48$ in üçte ikisi $32$, $4$ fazlası $36$; dörtte üçü de $36$ dır."),
            ornek(
                "Bir sayının dörtte üçü ile üçte ikisi arasındaki fark $5$ tir.",
                "Sayıyı bulalım.",
                "Denklem: $\\dfrac{3x}{4}-\\dfrac{2x}{3}=5$.",
                "Ortak payda $12$: $\\dfrac{9x-8x}{12}=\\dfrac{x}{12}=5$, yani $x=60$.",
                "Kontrol: $45-40=5$."),
        ]},
        {"baslik": "Bütünü birim olarak seçmek", "icerik": [
            "Kesirli bilgiler art arda geldiğinde bütünü paydaların uygun bir katı kadar birim kabul etmek hesabı tam sayılarla yürütmeyi sağlar. Soru sonunda bir birimin gerçek değeri bulunur ve istenen miktar hesaplanır.",
            ornek(
                "Bir bahçenin beşte ikisine domates, kalan alanın üçte birine biber ekiliyor ve geriye kalan $120$ metrekareye çim ekiliyor.",
                "Bahçenin alanını bulalım.",
                "Paydalar $5$ ve kalanın payı için $3$; bahçeyi $15$ birim alalım. Domates $6$ birim, kalan $9$ birim.",
                "Biber kalanın üçte biri: $3$ birim. Çim: $9-3=6$ birim.",
                "$6$ birim $120$ metrekare ise $1$ birim $20$ metrekare; bahçe $15 \\cdot 20=300$ metrekaredir. Kontrol: domates $120$, biber $60$, çim $120$."),
            "Birim sayısı seçilirken hem ilk kesrin paydası hem de kalanın bölüneceği parça sayısı dikkate alınır. Burada $15$ birim, önce beşe, sonra kalan $9$ birim üçe bölünebildiği için uygundur.",
        ]},
        {"baslik": "Kesirleri karşılaştırarak karar vermek", "icerik": [
            "Bazı sorular hesap değil karşılaştırma ister: iki indirimden hangisi daha büyük, iki gruptan hangisinin oranı daha yüksek gibi. Bu durumda kesirler ortak paydaya getirilir ya da ondalık sayıya çevrilir.",
            ornek(
                "Bir mağaza sekizde üç, başka bir mağaza beşte iki indirim yapıyor.",
                "Hangi indirimin daha büyük olduğunu bulalım.",
                "Ortak payda $40$: $\\dfrac{3}{8}=\\dfrac{15}{40}$ ve $\\dfrac{2}{5}=\\dfrac{16}{40}$.",
                "$\\dfrac{16}{40}>\\dfrac{15}{40}$ olduğu için beşte iki indirim daha büyüktür.",
                "Ondalık olarak: $0.4>0.375$."),
            "Kesir karşılaştırmanın diğer yolları <a href=\"/blog/kesirlerde-siralama-ve-karsilastirma/\">Kesirlerde Sıralama ve Karşılaştırma</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Paylaştırma problemleri", "icerik": [
            "Bir miktar birkaç kişi arasında kesirlerle paylaştırıldığında, kesirlerin toplamı ile bütün arasındaki fark geriye kalan payı verir. Kesirlerin toplamı $1$ i geçemez; geçiyorsa soru ya da kurulum yanlıştır.",
            ornek(
                "Bir ödül üç kişi arasında paylaştırılıyor. Birinci kişi ödülün yarısını, ikinci kişi üçte birini, üçüncü kişi kalan $1500$ lirayı alıyor.",
                "Ödülün tamamını ve her kişinin payını bulalım.",
                "İlk iki kişinin aldığı kesirlerin toplamı: $\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{5}{6}$. Üçüncü kişiye kalan kesir $\\dfrac{1}{6}$ dir.",
                "$\\dfrac{1}{6}x=1500$, yani ödül $9000$ liradır.",
                "Paylar: birinci $4500$, ikinci $3000$, üçüncü $1500$ lira. Kontrol: toplam $9000$."),
            dikkat(
                "Kesirleri toplarken paydaları eşitlememek.",
                "Yarım ile üçte birin toplamı beşte iki değildir. Paylar ve paydalar ayrı ayrı toplanamaz; önce ortak payda bulunur: $\\dfrac{3}{6}+\\dfrac{2}{6}=\\dfrac{5}{6}$."),
        ]},
        {"baslik": "Sınavda kesir problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kesir problemleri parçadan bütüne geçiş, kalanın kesri, doluluk ve paylaştırma soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de kesir problemleri sayısal bölümün temel soru türlerinden biridir."),
            "Kesir problemlerinde bütünü paydaların EKOK'u kadar kabul etmek hesabı kolaylaştırır. Örneğin paydalar $3$ ve $4$ ise bütünü $12$ birim almak, bütün kesirleri tam sayılara çevirir. Soru bittiğinde bir birimin gerçek değeri bulunur ve sonuç ona göre ölçeklenir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Bütünü bulmak için parçayı kesirle çarpmak", "Parçayı kesre böl"],
                ["Kalanın kesrini bütüne uygulamak", "Her adımda kalanı yaz"],
                ["Kesirleri paydaları eşitlemeden toplamak", "Önce ortak payda"],
                ["Paylaştırmada kalan kesri hesaplamamak", "Bütünden kesirlerin toplamını çıkar"],
                ["Doluluk farkını yanlış kurmak", "Son doluluk eksi ilk doluluk"],
                ["Bütünün parçadan küçük çıkmasını fark etmemek", "Sonucun anlamını kontrol et"],
            ]),
            "Bu hataların çoğu, bütünün ne olduğunu her adımda sormamaktan doğar. Özellikle \"kalanın\" kelimesi geçtiğinde bütün değişir; her adımda yeni bütünü yazmak hatayı büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("Kesir problemleri nasıl çözülür?",
         "Önce bütünün ne olduğu belirlenir. Bütün biliniyorsa parça, bütünün kesirle çarpımıyla; parça biliniyorsa bütün, parçanın kesre bölünmesiyle bulunur."),
        ("Kesri verilen bir çokluğun tamamı nasıl bulunur?",
         "Verilen miktar pay sayısına bölünerek bir parçanın değeri bulunur, sonra payda kadar parça alınır. Örneğin yedide üçü 12 olan sayı 28 dir."),
        ("Kalanın kesri sorularında nelere dikkat edilir?",
         "Kesir bütüne değil, bir önceki adımdan kalana uygulanır. Her adımda kalan oran yazılır ve bu oranlar çarpılarak toplam kalan oran bulunur."),
        ("Şerit modeli nedir?",
         "Bütünün paydaların EKOK'u kadar eş parçaya bölünmüş bir şerit olarak çizilmesidir. Bir parçanın değeri bulunduğunda bütün ve diğer parçalar okunur."),
        ("Doluluk problemlerinde bütün nedir?",
         "Kabın tam kapasitesidir. Eklenen ya da boşaltılan miktar, iki doluluk kesri arasındaki farkın kapasiteyle çarpımına eşittir."),
        ("Paylaştırmada kalan pay nasıl bulunur?",
         "Verilen kesirler ortak paydada toplanır ve bu toplam birden çıkarılır. Kalan kesir, geriye kalan miktarın bütüne oranıdır."),
        ("Kesrin kesri nasıl hesaplanır?",
         "Kesirler çarpılır. Bir sınıfın üçte ikisi kız ve kızların dörtte biri gözlüklüyse, gözlüklü kızlar sınıfın altıda biridir."),
        ("Bir işin bir kısmının süresi biliniyorsa tamamı nasıl bulunur?",
         "Çalışma hızı değişmiyorsa süre, yapılan kesirle doğru orantılıdır. Önce işin birim kesrinin süresi bulunur, sonra bütüne geçilir."),
        ("Kesir problemlerinde bütünü kaç birim almalıyım?",
         "Paydaların ve kalanın bölüneceği parça sayılarının ortak katını seç. Böylece bütün hesap tam sayılarla yürür ve sonunda bir birimin değeri bulunur."),
    ],
    "kontrol": [
        "Bir problemde bütünün ne olduğunu belirleyebiliyorum.",
        "Bir çokluğun kesrini iki adımda zihinden bulabiliyorum.",
        "Kesri verilen çokluğun tamamını bulabiliyorum.",
        "Bütünün parçadan büyük olması gerektiğini kontrol edebiliyorum.",
        "Şerit modelini paydaların EKOK'u ile kurabiliyorum.",
        "Kalanın kesri sorularında her adımda kalanı yazabiliyorum.",
        "Kalan oranlarını çarparak tek adımda sonuca ulaşabiliyorum.",
        "Doluluk problemlerinde iki kesrin farkıyla denklem kurabiliyorum.",
        "Aynı sayının iki kesrini karşılaştıran denklemler kurabiliyorum.",
        "Paylaştırma sorularında kalan kesri hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kesirler-konu-anlatimi-pdf", "denklem-kurma-problemleri-nasil-cozulur", "sayi-problemleri-konu-anlatimi-pdf"],
}
