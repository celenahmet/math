# scripts/yazilar/74_oran_oranti.py — Oran ve Oranti (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "oran-ve-oranti-konu-anlatimi-pdf",
    "baslik": "Oran ve Orantı Konu Anlatımı PDF",
    "aciklama": "Oran ve orantı nedir? İçler dışlar çarpımı, orantı sabiti, orantının özellikleri, birleşik oranlar, bölüşüm ve ölçek problemleri; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "oran-ve-oranti-konu-anlatimi-pdf",
    "kapak_alt": "Oran ve orantı: farklı sayıda mavi ve turuncu blokla ölçekli kuleler kuran iki öğrenci",
    "ozet": "Oran, iki büyüklüğün birbirine göre ne kadar olduğunu söyler; orantı ise iki oranın eşitliğidir. Bir tarifi iki katına çıkarmak, bir haritada mesafe ölçmek ya da bir ödülü emeğe göre paylaştırmak hep oran ve orantıyla yapılır. Bu yazıda oranın ve orantının ne olduğunu, içler dışlar çarpımını, orantı sabitiyle çözüm yolunu, orantının özelliklerini, birleşik oranları, bölüşüm problemlerini ve ölçeği çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Oran nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesirleri ve denk kesirleri biliyor olman yeterli.",
                "Denk kesirler için <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a> yazısına göz at."),
            "Aynı türden iki büyüklüğün bölümüne <strong>oran</strong> denir. $a$ nın $b$ ye oranı $\\dfrac{a}{b}$ ya da $a:b$ biçiminde yazılır ve \"$a$ nın $b$ ye oranı\" diye okunur. Oranın her iki terimi de aynı birimle ölçülmelidir.",
            ornek(
                "Bir sınıfta $12$ kız ve $18$ erkek öğrenci olsun.",
                "Kızların erkeklere oranını en sade biçimde yazalım.",
                "Oran: $\\dfrac{12}{18}$.",
                "Pay ve payda $6$ ya bölününce $\\dfrac{2}{3}$; yani $2:3$.",
                "Bu, her $2$ kıza karşılık $3$ erkek öğrenci olduğu anlamına gelir."),
            "Oran, kesirler gibi sadeleştirilebilir ve genişletilebilir; değeri değişmez. $12:18$, $2:3$ ve $4:6$ aynı oranı anlatır.",
            dikkat(
                "Birimler aynı olmalıdır.",
                "$50$ santimetre ile $2$ metrenin oranı $\\dfrac{50}{2}=25$ değildir. Önce ikisi aynı birime çevrilir: $\\dfrac{50}{200}=\\dfrac{1}{4}$."),
            "Farklı türden iki büyüklüğün bölümü ise yeni bir büyüklük tanımlar: yolun zamana bölümü hız, kütlenin hacme bölümü yoğunluk, fiyatın miktara bölümü birim fiyattır. Bunlara <strong>birimli oran</strong> da denir ve birimleri yazılarak kullanılır: saatte $60$ kilometre, kilogramı $40$ lira gibi.",
        ]},
        {"baslik": "Orantı nedir?", "icerik": [
            "İki oranın eşitliğine <strong>orantı</strong> denir:",
            "$$\\dfrac{a}{b}=\\dfrac{c}{d}$$",
            "Bu orantıda $a$ ile $d$ ye <strong>dışlar</strong>, $b$ ile $c$ ye <strong>içler</strong> denir. $a:b=c:d$ biçiminde yazıldığında dışlar iki uçta, içler ortada durur ve adlar buradan gelir.",
            "<h3>İçler dışlar çarpımı</h3>",
            "Bir orantıda içlerin çarpımı dışların çarpımına eşittir: $\\dfrac{a}{b}=\\dfrac{c}{d}$ ise $a \\cdot d=b \\cdot c$ dir. Bu, iki tarafı $b \\cdot d$ ile çarpmanın sonucudur ve bilinmeyeni bulmanın en hızlı yoludur.",
            ornek(
                "$\\dfrac{3}{5}=\\dfrac{x}{40}$ orantısı verilsin.",
                "$x$ i bulalım.",
                "İçler dışlar çarpımı: $5 \\cdot x=3 \\cdot 40$.",
                "$5x=120$, yani $x=24$."),
            ornek(
                "$\\dfrac{x+1}{x-2}=\\dfrac{7}{4}$ orantısı verilsin.",
                "$x$ i bulalım.",
                "İçler dışlar çarpımı: $4 \\cdot (x+1)=7 \\cdot (x-2)$.",
                "$4x+4=7x-14$, yani $3x=18$ ve $x=6$.",
                "Kontrol: $\\dfrac{7}{4}=\\dfrac{7}{4}$."),
            hap("Orantıda içlerin çarpımı dışların çarpımına eşittir: $\\dfrac{a}{b}=\\dfrac{c}{d}$ ise $a \\cdot d=b \\cdot c$.",
                "Bilinmeyen tek bir terimdeyse içler dışlar çarpımı onu doğrudan verir."),
        ]},
        {"baslik": "Orantı sabiti", "icerik": [
            "Eşit oranların ortak değerine <strong>orantı sabiti</strong> denir ve genellikle $k$ ile gösterilir. $\\dfrac{a}{b}=\\dfrac{c}{d}=k$ ise $a=b \\cdot k$ ve $c=d \\cdot k$ yazılabilir. Bu yazım, birden fazla bilinmeyen olduğunda soruyu tek bilinmeyenli hâle getirir.",
            ornek(
                "$\\dfrac{a}{3}=\\dfrac{b}{5}=\\dfrac{c}{7}$ ve $a+b+c=45$ olsun.",
                "$a$, $b$ ve $c$ yi bulalım.",
                "Ortak oranı $k$ diyelim: $a=3k$, $b=5k$, $c=7k$.",
                "Toplam: $3k+5k+7k=15k=45$, yani $k=3$.",
                "$a=9$, $b=15$, $c=21$."),
            ornek(
                "$\\dfrac{a}{2}=\\dfrac{b}{3}$ ve $a \\cdot b=54$ olsun; $a$ ve $b$ pozitif.",
                "$a$ ve $b$ yi bulalım.",
                "$a=2k$, $b=3k$: $2k \\cdot 3k=6k^2=54$, yani $k^2=9$.",
                "$a$ ve $b$ pozitif olduğu için $k=3$: $a=6$, $b=9$."),
            hap("$\\dfrac{a}{b}=\\dfrac{c}{d}=k$ ise $a=bk$ ve $c=dk$ yazılır; birden fazla bilinmeyen tek bilinmeyene iner."),
        ]},
        {"baslik": "Orantının özellikleri", "icerik": [
            "Eşit oranlar kendi aralarında toplanıp çıkarıldığında oran değişmez. $\\dfrac{a}{b}=\\dfrac{c}{d}=k$ ise:",
            "$$\\dfrac{a+c}{b+d}=k \\text{ ve } \\dfrac{a-c}{b-d}=k$$",
            "İkinci eşitlik için $b \\neq d$ olmalıdır. Daha genel olarak, $m$ ve $n$ sayıları için $\\dfrac{m \\cdot a+n \\cdot c}{m \\cdot b+n \\cdot d}=k$ dır; payda sıfır olmadığı sürece. Nedeni basittir: $a=b \\cdot k$ ve $c=d \\cdot k$ yerine yazılınca pay, paydanın $k$ katı olur.",
            ornek(
                "$\\dfrac{a}{b}=\\dfrac{3}{4}$ olsun.",
                "$\\dfrac{2a+b}{a-b}$ ifadesinin değerini bulalım.",
                "$a=3k$ ve $b=4k$ yazalım.",
                "$\\dfrac{2 \\cdot 3k+4k}{3k-4k}=\\dfrac{10k}{-k}=-10$."),
            dikkat(
                "Oranları toplamak, kesirleri toplamak değildir.",
                "$\\dfrac{a+c}{b+d}=k$ özelliği yalnızca oranlar eşitse geçerlidir. Eşit olmayan iki kesirde payları ve paydaları toplamak, kesirlerin toplamını vermez."),
        ]},
        {"baslik": "Birleşik oranlar", "icerik": [
            "Üç büyüklüğün ikişer ikişer oranları verilmişse, ortak terim eşitlenerek üçünün birden oranı yazılır. Buna <strong>birleşik oran</strong> denir.",
            ornek(
                "$\\dfrac{a}{b}=\\dfrac{2}{3}$ ve $\\dfrac{b}{c}=\\dfrac{4}{5}$ olsun.",
                "$a:b:c$ oranını bulalım.",
                "Ortak terim $b$: birinci oranda $3$, ikincide $4$. İkisinin EKOK'u $12$.",
                "Birinci oranı $4$ ile genişletelim: $a:b=8:12$. İkincisini $3$ ile genişletelim: $b:c=12:15$.",
                "Birleşik oran: $a:b:c=8:12:15$."),
            "Ortak terimi eşitlemek için EKOK kullanılır; nasıl bulunduğu <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Bölüşüm problemleri", "icerik": [
            "Bir miktar verilen oranlarda paylaştırılırken oran sayıları toplanır ve miktar bu toplama bölünerek bir <strong>pay</strong>ın değeri bulunur. Sonra her kişinin pay sayısı bu değerle çarpılır.",
            ornek(
                "$360$ lira üç kişi arasında $2:3:4$ oranında paylaştırılsın.",
                "Her kişinin payını bulalım.",
                "Toplam pay sayısı: $2+3+4=9$.",
                "Bir payın değeri: $360:9=40$ lira.",
                "Paylar: $2 \\cdot 40=80$, $3 \\cdot 40=120$ ve $4 \\cdot 40=160$ lira. Kontrol: toplam $360$."),
            ornek(
                "İki arkadaş bir işe $3:5$ oranında emek veriyor ve kazançtan küçük pay alan $90$ lira alıyor.",
                "Toplam kazanç kaç liradır?",
                "Küçük pay $3$ parça ve $90$ lira: bir parça $30$ lira.",
                "Toplam $3+5=8$ parça: $8 \\cdot 30=240$ lira."),
            dikkat(
                "Bölüşümde oranlar tersine de verilebilir.",
                "\"Yaşlarıyla ters orantılı paylaştırma\" gibi ifadelerde paylar yaşların tersleriyle orantılıdır. Ters orantının ayrıntısı <a href=\"/blog/dogru-oranti-ve-ters-oranti/\">Doğru Orantı ve Ters Orantı</a> yazısında."),
            hap("Bir miktar verilen oranda paylaştırılırken oran sayıları toplanır ve miktar bu toplama bölünerek bir payın değeri bulunur."),
        ]},
        {"baslik": "Ölçek", "icerik": [
            "Harita ve planlarda gerçek uzunlukların belirli bir oranda küçültülmesine <strong>ölçek</strong> denir. Ölçek, çizimdeki uzunluğun gerçek uzunluğa oranıdır ve genellikle $1:n$ biçiminde yazılır.",
            ornek(
                "Ölçeği $1:50000$ olan bir haritada iki şehir arası $4$ santimetre olsun.",
                "Gerçek uzaklık kaç kilometredir?",
                "Gerçek uzunluk, çizimdekinin $50000$ katıdır: $4 \\cdot 50000=200000$ santimetre.",
                "$1$ kilometre $100000$ santimetre olduğu için $200000$ santimetre $2$ kilometredir."),
            ornek(
                "Gerçekte $6$ metre olan bir duvar, bir planda $3$ santimetre olarak çizilmiş olsun.",
                "Planın ölçeğini bulalım.",
                "Birimleri eşitleyelim: $6$ metre $600$ santimetredir.",
                "Ölçek: $\\dfrac{3}{600}=\\dfrac{1}{200}$, yani $1:200$."),
            dikkat(
                "Ölçek uzunluklar içindir, alanlar için değil.",
                "Uzunluklar $200$ kat küçülürken alanlar $200 \\cdot 200=40000$ kat küçülür. $1:200$ ölçekli bir planda $1$ santimetrekarelik bir bölge, gerçekte $40000$ santimetrekare, yani $4$ metrekaredir. Alan hesabında ölçeğin karesi kullanılır."),
            hap("Ölçeği $1:100000$ olan bir haritada $3$ santimetrelik uzunluk gerçekte $300000$ santimetre, yani $3$ kilometredir.", "Ölçekte sağdaki sayı, haritadaki bir birimin gerçekte kaç birim olduğunu söyler.", gunluk=True),
        ]},
        {"baslik": "Günlük hayatta oran", "icerik": [
            "Tarif ölçekleme, karışım hazırlama ve fiyat karşılaştırma oranın günlük kullanımlarıdır. Birim fiyat hesabı, farklı büyüklükteki paketlerden hangisinin daha ucuz olduğunu gösterir.",
            ornek(
                "$400$ gramlık bir paket $32$ liraya, $750$ gramlık bir paket $57$ liraya satılıyor.",
                "Hangisi daha ucuzdur?",
                "Birinci paketin kilogram fiyatı: $32:0.4=80$ lira.",
                "İkinci paketin kilogram fiyatı: $57:0.75=76$ lira.",
                "Kilogramı daha ucuz olan ikinci pakettir."),
            ornek(
                "Bir limonata tarifinde su ile limon suyu $5:1$ oranında karıştırılıyor.",
                "$1.8$ litre limonata için kaç litre limon suyu gerekir?",
                "Toplam $5+1=6$ pay; bir pay $1.8:6=0.3$ litre.",
                "Limon suyu $1$ pay: $0.3$ litre."),
        ]},
        {"baslik": "Oran ile kesir: parça ve bütün", "icerik": [
            "$a:b=2:3$ oranı, $a$ nın $b$ ye göre büyüklüğünü anlatır; $a$ nın toplam içindeki payını değil. Toplam $2+3=5$ pay olduğu için $a$ toplamın $\\dfrac{2}{5}$ si, $b$ ise $\\dfrac{3}{5}$ ü kadardır. Oranla verilen bir soruda parça ile bütün arasında geçiş yaparken bu ayrım belirleyicidir.",
            ornek(
                "Bir torbadaki kırmızı bilyelerin mavi bilyelere oranı $2:3$ ve torbada toplam $40$ bilye olsun.",
                "Kırmızı bilye sayısını bulalım.",
                "Toplam pay: $2+3=5$; bir pay $40:5=8$ bilye.",
                "Kırmızı bilye sayısı: $2 \\cdot 8=16$.",
                "Kesirle de aynı sonuç çıkar: $40 \\cdot \\dfrac{2}{5}=16$."),
            dikkat(
                "Oranı parçanın bütüne oranı sanmak.",
                "Kırmızıların mavilere oranı $\\dfrac{2}{3}$ dir; ama kırmızılar bütün bilyelerin $\\dfrac{2}{3}$ si değil, $\\dfrac{2}{5}$ sidir. Soru \"bütünün ne kadarı\" diye soruyorsa oran sayıları toplanarak bütün bulunur."),
            hap("$a:b=2:3$ ise $a$ toplamın $\\dfrac{2}{5}$ si, $b$ ise $\\dfrac{3}{5}$ ü kadardır."),
        ]},
        {"baslik": "Oranı değişen problemler", "icerik": [
            "Bir oranı oluşturan miktarlara ekleme ya da çıkarma yapılınca oran değişir. Bu sorularda başlangıç miktarları orantı sabitiyle yazılır, değişiklik eklenir ve yeni oran bir orantı olarak kurulur.",
            ornek(
                "Bir sınıfta kızların erkeklere oranı $3:4$ tür. Sınıfa $4$ kız öğrenci katılınca kızların sayısı erkeklerin sayısına eşit oluyor.",
                "Başlangıçta sınıfta kaç öğrenci olduğunu bulalım.",
                "Kızlar $3k$, erkekler $4k$ olsun.",
                "Yeni durumda $3k+4=4k$, yani $k=4$.",
                "Başlangıçta $12$ kız ve $16$ erkek vardı; toplam $28$ öğrenci."),
            ornek(
                "Bir karışımda şekerin suya oranı $1:4$ ve karışım $500$ gram olsun.",
                "Kaç gram şeker eklenirse oranın $1:2$ olacağını bulalım.",
                "Şeker: $500 \\cdot \\dfrac{1}{5}=100$ gram; su: $400$ gram.",
                "Eklenen şeker $x$ gram olsun. Su değişmez: $\\dfrac{100+x}{400}=\\dfrac{1}{2}$.",
                "İçler dışlar çarpımı: $2 \\cdot (100+x)=400$, yani $x=100$ gram."),
            "Bu tür sorularda değişmeyen miktarı bulmak işi kolaylaştırır. İkinci örnekte su hiç değişmedi ve yeni oran doğrudan suya göre kuruldu.",
        ]},
        {"baslik": "Yaş problemlerinde oran", "icerik": [
            "Yaş sorularında geçen her yılda herkesin yaşı $1$ artar. Bu yüzden iki kişinin yaşları arasındaki fark hiç değişmez ama yaşlarının oranı değişir.",
            ornek(
                "Ece'nin yaşının Can'ın yaşına oranı $2:3$ tür ve $5$ yıl sonra bu oran $3:4$ olacaktır.",
                "İkisinin bugünkü yaşlarını bulalım.",
                "Bugünkü yaşlar $2k$ ve $3k$ olsun.",
                "$5$ yıl sonra: $\\dfrac{2k+5}{3k+5}=\\dfrac{3}{4}$.",
                "İçler dışlar çarpımı: $4 \\cdot (2k+5)=3 \\cdot (3k+5)$, yani $8k+20=9k+15$ ve $k=5$.",
                "Ece $10$, Can $15$ yaşındadır. Kontrol: $5$ yıl sonra $15$ ve $20$ yaşında olurlar ve $\\dfrac{15}{20}=\\dfrac{3}{4}$."),
            dikkat(
                "İki yaşa farklı süreler eklemek.",
                "Aynı süre herkes için geçer. $5$ yıl sonrası sorulduğunda iki yaşa da $5$ eklenir; yalnızca birine eklemek yanlış bir orantı kurdurur."),
        ]},
        {"baslik": "Orta orantılı", "icerik": [
            "$\\dfrac{a}{x}=\\dfrac{x}{b}$ orantısındaki $x$ e, $a$ ile $b$ nin <strong>orta orantılısı</strong> denir. İçler dışlar çarpımından $x^2=a \\cdot b$ bulunur. Pozitif sayılarla çalışılıyorsa $x=\\sqrt{a \\cdot b}$ olur.",
            ornek(
                "$4$ ve $9$ sayıları verilsin.",
                "Bu iki sayının pozitif orta orantılısını bulalım.",
                "$\\dfrac{4}{x}=\\dfrac{x}{9}$ ise $x^2=36$.",
                "Pozitif çözüm: $x=6$.",
                "Kontrol: $\\dfrac{4}{6}=\\dfrac{2}{3}$ ve $\\dfrac{6}{9}=\\dfrac{2}{3}$."),
            "Orta orantılı, ardışık terimlerin hep aynı oranla büyüdüğü dizilerde ortaya çıkar: $4$, $6$, $9$ dizisinde her terim bir öncekinin $\\dfrac{3}{2}$ katıdır. Bu yüzden ortadaki terim, iki komşusunun orta orantılısıdır.",
        ]},
        {"baslik": "Orantıda terimlerin yer değiştirmesi", "icerik": [
            "Bir orantıda terimlerin yeri belirli kurallarla değiştirilebilir ve orantı bozulmaz. $\\dfrac{a}{b}=\\dfrac{c}{d}$ ise, terimlerin hiçbiri sıfır olmamak koşuluyla şunlar da doğrudur:",
            "<ul><li><strong>İçlerin yer değiştirmesi:</strong> $\\dfrac{a}{c}=\\dfrac{b}{d}$.</li>"
            "<li><strong>Dışların yer değiştirmesi:</strong> $\\dfrac{d}{b}=\\dfrac{c}{a}$.</li>"
            "<li><strong>İki oranı da ters çevirme:</strong> $\\dfrac{b}{a}=\\dfrac{d}{c}$.</li></ul>",
            "Üçünde de içler dışlar çarpımı yine $a \\cdot d=b \\cdot c$ verir; bu yüzden hepsi aynı orantının farklı yazılışlarıdır.",
            ornek(
                "$\\dfrac{3}{5}=\\dfrac{12}{20}$ orantısı verilsin.",
                "İçleri yer değiştirerek yeni bir orantı yazalım ve doğruluğunu kontrol edelim.",
                "İçler $5$ ve $12$: $\\dfrac{3}{12}=\\dfrac{5}{20}$.",
                "İki taraf da sadeleşince $\\dfrac{1}{4}$ olur; orantı doğrudur."),
        ]},
        {"baslik": "Oranlarla karşılaştırma", "icerik": [
            "Farklı büyüklükteki iki grubu karşılaştırmanın doğru yolu, sayıları değil oranları karşılaştırmaktır. Daha büyük bir grupta sayının daha büyük olması, oranın da daha büyük olduğu anlamına gelmez.",
            ornek(
                "A sınıfındaki $24$ öğrenciden $18$ i, B sınıfındaki $30$ öğrenciden $21$ i bir sınavı geçmiş olsun.",
                "Hangi sınıfın başarı oranının daha yüksek olduğunu bulalım.",
                "A sınıfı: $\\dfrac{18}{24}=\\dfrac{3}{4}=0.75$.",
                "B sınıfı: $\\dfrac{21}{30}=\\dfrac{7}{10}=0.7$.",
                "B sınıfında geçen öğrenci sayısı daha fazla, ama başarı oranı A sınıfında daha yüksek."),
            ornek(
                "Bir araç $150$ kilometreyi $2$ saatte, başka bir araç $200$ kilometreyi $2.5$ saatte gidiyor.",
                "Hangisinin daha hızlı olduğunu bulalım.",
                "Birinci aracın hızı: $150:2=75$ kilometre bölü saat.",
                "İkinci aracın hızı: $200:2.5=80$ kilometre bölü saat. İkinci araç daha hızlıdır."),
        ]},
        {"baslik": "Sınavda oran ve orantı", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu içler dışlar çarpımı, orantı sabitiyle çözüm, birleşik oran ve bölüşüm problemleri biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde oran bilgisi sayısal akıl yürütme, grafik yorumlama ve karışım sorularında da gerekebilir."),
            "Birden fazla bilinmeyen içeren oran sorularında ilk iş, ortak oranı $k$ ile göstermektir. Bu tek adım, soruyu genellikle tek bilinmeyenli basit bir denkleme indirger.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Farklı birimlerle oran kurmak", "Önce aynı birime çevir"],
                ["İçler dışlar çarpımını yanlış eşleştirmek", "$a \\cdot d=b \\cdot c$"],
                ["Bölüşümde toplam payı almamak", "Oran sayılarını topla"],
                ["Birleşik oranda ortak terimi eşitlememek", "Ortak terimi EKOK ile eşitle"],
                ["Ölçekte birimleri karıştırmak", "Aynı birime çevir"],
                ["$k$ yı bulunca soruyu bitmiş saymak", "İstenen terimi hesapla"],
            ]),
            "Bu hataların çoğu, oranın iki büyüklüğün karşılaştırması olduğunu ve iki büyüklüğün de aynı ölçüyle ifade edilmesi gerektiğini unutmaktan doğar. Oran kurmadan önce birimleri, bölüşümden önce toplam payı kontrol etmek bu hataları önler.",
        ]},
    ],
    "sss": [
        ("Oran nedir?",
         "Aynı türden iki büyüklüğün bölümüdür. a nın b ye oranı a bölü b ya da a iki nokta b biçiminde yazılır."),
        ("Orantı nedir?",
         "İki oranın eşitliğidir. Örneğin beşte üç ile kırkta yirmi dört bir orantı oluşturur."),
        ("İçler dışlar çarpımı nedir?",
         "Bir orantıda içlerin çarpımı dışların çarpımına eşittir. Bilinmeyen bir terimi bulmanın en hızlı yoludur."),
        ("Orantı sabiti ne işe yarar?",
         "Eşit oranların ortak değeridir. Terimleri bu sabitle yazmak, birden fazla bilinmeyeni tek bilinmeyene indirger."),
        ("Bölüşüm problemi nasıl çözülür?",
         "Oran sayıları toplanır, paylaştırılacak miktar bu toplama bölünerek bir payın değeri bulunur ve her kişinin pay sayısıyla çarpılır."),
        ("Ölçek ne demektir?",
         "Çizimdeki uzunluğun gerçek uzunluğa oranıdır. Bire elli bin ölçekli bir haritada 1 santimetre, gerçekte 500 metreye karşılık gelir."),
        ("Oran ile kesir aynı şey midir?",
         "Yazılışları benzer ama anlamları farklı olabilir. İkiye üç oranındaki iki gruptan birincisi, iki grubun toplamının beşte ikisidir; üçte ikisi değildir."),
        ("Yaş problemlerinde oran neden değişir?",
         "Her yıl iki yaşa da aynı sayı eklenir. Yaşlar arasındaki fark sabit kalır ama oran değişir; bu yüzden yeni oran ayrı bir orantı olarak kurulur."),
        ("İki grubun başarısı nasıl karşılaştırılır?",
         "Başarılı kişi sayıları değil, her grubun kendi içindeki oranı karşılaştırılır. Küçük bir grupta oran, büyük bir gruptakinden yüksek olabilir."),
        ("Ölçekli bir planda alan nasıl hesaplanır?",
         "Önce plandaki uzunluklar ölçekle gerçek uzunluklara çevrilir, sonra alan bu gerçek uzunluklarla hesaplanır. Doğrudan alanla çalışılacaksa ölçeğin karesi kullanılır."),
        ("Orta orantılı nedir?",
         "a nın x e oranı x in b ye oranına eşitse x sayısı a ile b nin orta orantılısıdır. x in karesi a ile b nin çarpımına eşittir; örneğin 4 ile 9 un pozitif orta orantılısı 6 dır."),
    ],
    "kontrol": [
        "Oranı tanımlayıp en sade biçimde yazabiliyorum.",
        "Oran kurmadan önce birimleri eşitleyebiliyorum.",
        "Orantıda içleri ve dışları ayırt edebiliyorum.",
        "İçler dışlar çarpımıyla bilinmeyeni bulabiliyorum.",
        "Orantı sabitiyle birden fazla bilinmeyeni çözebiliyorum.",
        "Orantının toplama ve çıkarma özelliklerini kullanabiliyorum.",
        "İkişer ikişer verilen oranları birleşik orana çevirebiliyorum.",
        "Bir miktarı verilen oranlarda paylaştırabiliyorum.",
        "Ölçekten gerçek uzunluğu ve gerçek uzunluktan ölçeği bulabiliyorum.",
        "Birim fiyatla farklı paketleri karşılaştırabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["dogru-oranti-ve-ters-oranti", "yuzdeler-konu-anlatimi-pdf", "kesirler-konu-anlatimi-pdf"],
}
