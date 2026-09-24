# scripts/yazilar/80_sayi_problemleri.py — Sayi Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "sayi-problemleri-konu-anlatimi-pdf",
    "baslik": "Sayı Problemleri Konu Anlatımı PDF",
    "aciklama": "Sayı problemleri nasıl çözülür? Toplam ve fark, kat, ardışık sayılar, bölme ve kalan, basamak, kesir, ortalama ve tersten çözme soruları; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "sayi-problemleri-konu-anlatimi-pdf",
    "kapak_alt": "Sayı problemleri: boncuklu sayı çubuğu, kutular ve örtülü bir nesneyle sayılar arasındaki ilişkiyi görselleştiren öğrenci",
    "ozet": "Sayı problemleri, bilinmeyen bir ya da birkaç sayının, aralarındaki ilişkiler verilerek bulunmasını ister. Toplam ve fark, kat ilişkisi, ardışık sayılar, bölme ve kalan, rakamlar ve ortalama bu problemlerin en sık kullandığı ilişkilerdir. Bu yazıda her problem türünün nasıl denkleme çevrileceğini, işi kısaltan formülleri ve kısayolları, tersten çözme yöntemini ve sık yapılan hataları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Sayı problemi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birinci dereceden denklem çözmeyi ve sözel ifadeleri cebire çevirmeyi biliyor olman yeterli.",
                "Denklem kurmanın adımları için <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "Sayı problemlerinde aranan şey bir ya da birkaç sayıdır. Sayıların kendisi verilmez; bunun yerine aralarındaki ilişkiler anlatılır: toplamları, farkları, biri diğerinin kaç katı, ardışık olup olmadıkları ya da bölündüklerinde ne kaldığı. Çözüm, bu ilişkileri denkleme çevirmekten ibarettir. İlişkiler doğru çevrildiğinde geriye kalan iş, birkaç satırlık basit bir hesaptır.",
            "Bu yazıda ele aldığımız başlıca problem türleri şunlar:",
            tablo(["Tür", "Temel ilişki"], [
                ["Toplam ve fark", "İki denklem, iki bilinmeyen"],
                ["Kat ilişkisi", "Bir sayı diğerinin katı"],
                ["Ardışık sayılar", "Sayılar eşit aralıklarla artar"],
                ["Bölme ve kalan", "Bölünen, bölen ile bölümün çarpımına kalanın eklenmesidir"],
                ["Basamak", "İki basamaklı sayı, onlar basamağının on katı ile birler basamağının toplamıdır"],
                ["Ortalama", "Toplam, ortalama ile sayı adedinin çarpımıdır"],
            ]),
            hap("Sayı problemlerinde sayılar verilmez, aralarındaki ilişkiler verilir.",
                "Her ilişki bir denkleme dönüşür."),
        ]},
        {"baslik": "Toplam ve farkı verilen iki sayı", "icerik": [
            "İki sayının toplamı ve farkı biliniyorsa sayılar iki denklemle bulunur. Bu tür soruların çok sık çıkması, işi hızlandıran bir formülü de yararlı kılar.",
            ornek(
                "İki sayının toplamı $50$, farkı $14$ tür.",
                "Sayıları bulalım.",
                "Büyük sayı $a$, küçük sayı $b$ olsun: $a+b=50$ ve $a-b=14$.",
                "Denklemleri taraf tarafa toplayalım: $2a=64$, yani $a=32$.",
                "$b=50-32=18$. Sayılar $32$ ve $18$ dir."),
            "Aynı işlemi genel olarak yaparsak şu sonuç çıkar:",
            "$$\\text{büyük}=\\dfrac{\\text{toplam}+\\text{fark}}{2}$$",
            "$$\\text{küçük}=\\dfrac{\\text{toplam}-\\text{fark}}{2}$$",
            "Örnekte büyük sayı $\\dfrac{50+14}{2}=32$, küçük sayı $\\dfrac{50-14}{2}=18$ olur. Formül ezberlenmese de denklemleri toplama fikri akılda kalırsa aynı sonuca her zaman ulaşılır.",
            dikkat(
                "Toplam ile fark ya ikisi de tek ya ikisi de çift olmalıdır.",
                "Sayılar tam sayıysa toplam ile fark ya ikisi de tek ya ikisi de çift olur. Toplamı $50$, farkı $15$ olan iki tam sayı yoktur; böyle bir sonuç, sorunun yanlış okunduğunu gösterir."),
        ]},
        {"baslik": "Kat ilişkisi", "icerik": [
            "\"Bir sayı diğerinin $4$ katı\" gibi ifadelerde küçük sayıya $x$ demek en kısa yoldur; büyük sayı doğrudan $4x$ olur. Bu seçim kesirli ifadelerle uğraşmayı önler.",
            ornek(
                "Bir sayı diğerinin $4$ katıdır ve farkları $36$ dır.",
                "Sayıları bulalım.",
                "Küçük sayı $x$, büyük sayı $4x$ olsun: $4x-x=36$.",
                "$3x=36$, yani $x=12$. Sayılar $12$ ve $48$ dir."),
            ornek(
                "Bir sayının $3$ katının $7$ fazlası, aynı sayının $5$ katının $9$ eksiğine eşittir.",
                "Sayıyı bulalım.",
                "Sayı $x$ olsun: $3x+7=5x-9$.",
                "$16=2x$, yani $x=8$.",
                "Kontrol: $3 \\cdot 8+7=31$ ve $5 \\cdot 8-9=31$."),
            ornek(
                "Üç sayıdan ikincisi birincinin $2$ katı, üçüncüsü ikincinin $3$ fazlasıdır. Üç sayının toplamı $58$ dir.",
                "Sayıları bulalım.",
                "Birinci sayı $x$ olsun; ikinci $2x$, üçüncü $2x+3$ olur.",
                "Toplam: $x+2x+2x+3=58$, yani $5x=55$ ve $x=11$.",
                "Sayılar $11$, $22$ ve $25$ tir. Kontrol: $11+22+25=58$."),
            "Kat ilişkisi toplamla birlikte verildiğinde de aynı mantık işler: bir sayı diğerinin $4$ katı ve toplamları $60$ ise $x+4x=60$ yazılır ve $x=12$, büyük sayı $48$ bulunur. Toplam, küçük sayının $5$ katıdır; bu yüzden toplamı $5$ e bölmek küçük sayıyı doğrudan verir.",
        ]},
        {"baslik": "Ardışık sayılar", "icerik": [
            "Ardışık sayılar eşit aralıklarla artan sayılardır. Ardışık tam sayılar birer, ardışık çift ya da tek sayılar ikişer artar. En küçüğüne $x$ denirse diğerleri buna göre yazılır.",
            tablo(["Tür", "Yazılışı"], [
                ["Ardışık tam sayılar", "$x$, $x+1$, $x+2$"],
                ["Ardışık çift sayılar", "$x$, $x+2$, $x+4$"],
                ["Ardışık tek sayılar", "$x$, $x+2$, $x+4$"],
                ["$5$ in ardışık katları", "$x$, $x+5$, $x+10$"],
            ]),
            "Ardışık çift ve ardışık tek sayılar aynı biçimde yazılır; aradaki fark yalnızca $x$ in çift mi tek mi olduğudur.",
            ornek(
                "Ardışık dört çift sayının toplamı $100$ dür.",
                "Bu sayıları bulalım.",
                "Sayılar $x$, $x+2$, $x+4$ ve $x+6$ olsun: $4x+12=100$.",
                "$4x=88$, yani $x=22$. Sayılar $22$, $24$, $26$ ve $28$ dir.",
                "Kısa yol: ortalama $100:4=25$ tir. Ortalama tam ortada durduğu için sayılar $25$ in iki yanına simetrik yerleşir: $22$, $24$, $26$, $28$."),
            "Ardışık sayıların ayrıntısı <a href=\"/blog/ardisik-sayilar/\">Ardışık Sayılar</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Oranla verilen sayılar", "icerik": [
            "İki sayının oranı verildiğinde sayılar ortak bir çarpanla yazılır. Oran $3:5$ ise sayılar $3k$ ve $5k$ biçiminde yazılır; sorudaki ikinci bilgi $k$ yı verir.",
            ornek(
                "İki sayının oranı $3:5$ ve toplamları $64$ tür.",
                "Sayıları bulalım.",
                "Sayılar $3k$ ve $5k$ olsun: $3k+5k=64$.",
                "$8k=64$, yani $k=8$. Sayılar $24$ ve $40$ tır.",
                "Kontrol: $24+40=64$ ve $\\dfrac{24}{40}=\\dfrac{3}{5}$."),
            "Oran bilgisinin ayrıntısı <a href=\"/blog/oran-ve-oranti-konu-anlatimi-pdf/\">Oran ve Orantı Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Bölme ve kalan", "icerik": [
            "Bölme içeren sayı problemlerinin temel eşitliği şudur: bölünen, bölen ile bölümün çarpımına kalanın eklenmesiyle bulunur. Kalan her zaman bölenden küçüktür.",
            "$$\\text{Bölünen}=\\text{Bölen} \\cdot \\text{Bölüm}+\\text{Kalan}$$",
            ornek(
                "Bir sayı $7$ ile bölündüğünde bölüm $12$, kalan $5$ tir.",
                "Sayıyı bulalım.",
                "Bölünen $=7 \\cdot 12+5$.",
                "Sayı $89$ dur. Kontrol: $89=7 \\cdot 12+5$ ve $5<7$."),
            ornek(
                "Bir sayının $6$ ile bölümünden kalan $4$ tür.",
                "Bu sayının $3$ katının $6$ ile bölümünden kalanı bulalım.",
                "Sayı $6k+4$ biçimindedir. $3$ katı: $18k+12$.",
                "$18k$ ve $12$ nin ikisi de $6$ ya tam bölünür; kalan $0$ dır.",
                "Sayısal kontrol: $10$ un $6$ ile bölümünden kalan $4$ tür; $30$ un $6$ ile bölümünden kalan $0$ dır."),
            dikkat(
                "Kalanı bölenden büyük ya da eşit almak.",
                "Kalan her zaman bölenden küçüktür. Bir hesapta kalan bölene eşit ya da ondan büyük çıkarsa bölüm bir artırılır ve kalan küçültülür."),
        ]},
        {"baslik": "Basamak içeren sayı problemleri", "icerik": [
            "İki basamaklı bir sayının onlar basamağındaki rakam $a$, birler basamağındaki rakam $b$ ise sayının değeri $10a+b$ dir. Rakamların yeri değişince sayı $10b+a$ olur. Bu yazım, rakamlarla ilgili bütün soruları denkleme çevirmeyi sağlar.",
            ornek(
                "İki basamaklı bir sayının rakamları toplamı $11$ dir. Rakamların yeri değiştirilince sayı $27$ artıyor.",
                "Sayıyı bulalım.",
                "Sayı $10a+b$, yeni sayı $10b+a$ olsun. Fark: $(10b+a)-(10a+b)=9b-9a=27$, yani $b-a=3$.",
                "$a+b=11$ ve $b-a=3$: toplam ve fark formülüyle $b=7$, $a=4$.",
                "Sayı $47$ dir. Kontrol: $74-47=27$ ve $4+7=11$."),
            "Bu örnek güzel bir genellemeyi de gösterir: iki basamaklı bir sayı ile rakamlarının yeri değişmiş hâlinin farkı her zaman $9$ un katıdır, çünkü fark $9(b-a)$ dır.",
            dikkat(
                "Rakamları çarpar gibi yazmak.",
                "Onlar basamağı $a$, birler basamağı $b$ olan sayı $a \\cdot b$ değil, $10a+b$ dir. Örneğin $47$ sayısı $4 \\cdot 7=28$ değil, $4 \\cdot 10+7$ dir."),
        ]},
        {"baslik": "Üç basamaklı sayılar", "icerik": [
            "Üç basamaklı bir sayının yüzler, onlar ve birler basamağındaki rakamlar $a$, $b$ ve $c$ ise sayının değeri $100a+10b+c$ dir. Rakamlar hakkında verilen her bilgi bir denkleme dönüşür.",
            ornek(
                "Üç basamaklı bir sayının yüzler basamağı $4$, birler basamağı yüzler basamağının $2$ katı ve rakamlarının toplamı $15$ tir.",
                "Sayıyı bulalım.",
                "Yüzler basamağı $4$, birler basamağı $2 \\cdot 4=8$.",
                "Rakamlar toplamı: $4+b+8=15$, yani $b=3$.",
                "Sayı $438$ dir. Kontrol: $4+3+8=15$."),
            "Rakamların her biri $0$ ile $9$ arasında bir tam sayıdır ve yüzler basamağı $0$ olamaz. Bir denklem bu koşulları sağlamayan bir değer verirse, kurulumda bir hata vardır.",
        ]},
        {"baslik": "Çarpımı verilen ardışık sayılar", "icerik": [
            "Ardışık iki sayının çarpımı verildiğinde denklem ikinci dereceden olur, ama çoğu zaman tahminle hızla çözülür: ardışık iki sayının çarpımı, sayıların ortalamasının karesine çok yakındır.",
            ornek(
                "Ardışık iki pozitif tam sayının çarpımı $132$ dir.",
                "Bu sayıları bulalım.",
                "Sayılar $x$ ve $x+1$ olsun: $x(x+1)=132$.",
                "$11 \\cdot 11=121$ ve $12 \\cdot 12=144$ olduğu için sayılar $11$ ile $12$ civarındadır.",
                "Deneyelim: $11 \\cdot 12=132$. Sayılar $11$ ve $12$ dir."),
        ]},
        {"baslik": "Kalan koşuluyla sayı bulmak", "icerik": [
            "Bazı sorularda sayının kendisi değil, farklı sayılara bölündüğünde verdiği kalanlar bilinir. Bu durumda koşulları sağlayan sayılar düzenli aralıklarla tekrar eder; aralık, bölenlerin EKOK'udur.",
            ornek(
                "Bir kutudaki bilyeler dörder dörder sayılınca $3$ bilye, beşer beşer sayılınca $2$ bilye artıyor. Kutuda $50$ den az bilye var.",
                "Kutuda kaç bilye olabileceğini bulalım.",
                "$4$ e bölümünden kalan $3$ olan sayılar: $3$, $7$, $11$, $15$, $19$, $23$, $27$ ve devamı.",
                "Bunlardan $5$ e bölümünden kalanı $2$ olan ilk sayı $7$ dir. EKOK$(4, 5)=20$ olduğu için sonraki çözümler $20$ şer artar: $7$, $27$ ve $47$.",
                "Kutuda $7$, $27$ ya da $47$ bilye olabilir. Kontrol: $47=4 \\cdot 11+3$ ve $47=5 \\cdot 9+2$."),
            "EKOK'un nasıl bulunduğu <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Kesir içeren sayı problemleri", "icerik": [
            "Bir sayının belirli bir kesri üzerinden kurulan sorularda sayıya $x$ denir ve kesir $x$ ile çarpılır. Paydaları yok etmek için iki taraf paydaların EKOK'u ile çarpılır.",
            ornek(
                "Bir sayının beşte üçünün $2$ fazlası $20$ dir.",
                "Sayıyı bulalım.",
                "Sayı $x$ olsun: $\\dfrac{3x}{5}+2=20$.",
                "$\\dfrac{3x}{5}=18$, yani $3x=90$ ve $x=30$.",
                "Kontrol: $30$ un beşte üçü $18$, $2$ fazlası $20$ dir."),
            ornek(
                "Bir sayının yarısı ile üçte birinin toplamı $45$ tir.",
                "Sayıyı bulalım.",
                "Denklem: $\\dfrac{x}{2}+\\dfrac{x}{3}=45$.",
                "İki tarafı $6$ ile çarpalım: $3x+2x=270$, yani $5x=270$ ve $x=54$.",
                "Kontrol: $27+18=45$."),
            "Kesir hesaplarının ayrıntısı <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Ortalama ile kurulan problemler", "icerik": [
            "Birkaç sayının aritmetik ortalaması, sayıların toplamının sayı adedine bölünmesidir. Bu yüzden ortalama problemlerinde işe her zaman <strong>toplamı bularak</strong> başlamak gerekir: toplam, ortalama ile sayı adedinin çarpımıdır.",
            ornek(
                "Beş sayının ortalaması $18$ dir. Bu sayılardan biri çıkarılınca kalan dört sayının ortalaması $16$ oluyor.",
                "Çıkarılan sayıyı bulalım.",
                "Beş sayının toplamı: $5 \\cdot 18=90$.",
                "Kalan dört sayının toplamı: $4 \\cdot 16=64$.",
                "Çıkarılan sayı: $90-64=26$."),
            ornek(
                "Bir sınıftaki $20$ öğrencinin not ortalaması $70$ tir. Sınıfa katılan yeni bir öğrenciyle ortalama $71$ oluyor.",
                "Yeni öğrencinin notunu bulalım.",
                "Önceki toplam: $20 \\cdot 70=1400$. Yeni toplam: $21 \\cdot 71=1491$.",
                "Yeni öğrencinin notu: $1491-1400=91$."),
            "İkinci örneğin kısa bir yolu da var: yeni öğrenci ortalamayı $1$ puan artırdıysa notu, eski ortalamanın üzerine yeni sınıftaki $21$ öğrencinin her birine $1$ puan dağıtacak kadar fazladır. Yani not $70+21 \\cdot 1=91$ olur ve toplamları ayrı ayrı hesaplamaya gerek kalmaz.",
            dikkat(
                "Ortalamaları doğrudan toplamak ya da çıkarmak.",
                "İlk örnekte $18-16=2$ yazmak anlamsızdır. Ortalamalar farklı sayıda sayıya ait olduğu için önce her birinin toplamı bulunur, işlem toplamlar üzerinden yapılır."),
        ]},
        {"baslik": "Tersten çözme", "icerik": [
            "Bir sayıya art arda işlemler uygulanıp sonuç verildiğinde, sondan başa doğru ters işlemler uygulanarak sayı bulunur. Toplamanın tersi çıkarma, çarpmanın tersi bölmedir. Bu yöntem, denklem kurmaktan çoğu zaman daha hızlıdır. Önemli olan, işlemleri sorudaki sıranın tam tersiyle, sondan başa doğru uygulamaktır.",
            ornek(
                "Bir sayıya $5$ ekleniyor, sonuç $3$ ile çarpılıyor, çıkan sonuçtan $6$ çıkarılıyor ve en son $2$ ye bölünüyor. Elde edilen sonuç $18$ dir.",
                "Başlangıçtaki sayıyı bulalım.",
                "Sondan başa ters işlemler: $2$ ye bölmenin tersi, $18 \\cdot 2=36$.",
                "$6$ çıkarmanın tersi $36+6=42$; $3$ ile çarpmanın tersi $42:3=14$.",
                "$5$ eklemenin tersi $14-5=9$. Sayı $9$ dur. Kontrol: $(9+5) \\cdot 3=42$, $42-6=36$, $36:2=18$."),
            "Aynı soru denklemle de çözülür: $\\dfrac{3(x+5)-6}{2}=18$. Ama ters işlem yöntemi, parantez ve kesirle uğraşmadan aynı sonuca ulaşır. İşlem sırası karışık verilmişse ya da bilinmeyen birden fazla yerde geçiyorsa denklem yöntemi daha güvenlidir.",
        ]},
        {"baslik": "Sınavda sayı problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) problem bölümünün ilk soruları çoğunlukla sayı problemleridir: toplam ve fark, kat, ardışık sayılar, basamak ve ortalama bu soruların temel kalıplarıdır.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde sayı problemleri, sayısal akıl yürütme sorularının da temelini oluşturur."),
            "Sayı problemlerinde çözümü kontrol etmek çok kolaydır: bulunan sayıları sorudaki her cümlede denemek yeterlidir. Bu kontrol birkaç saniye sürer ve yanlış kurulmuş bir denklemi hemen ortaya çıkarır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Ardışık çift sayıları $x$, $x+1$ yazmak", "$x$, $x+2$, $x+4$"],
                ["İki basamaklı sayıyı $a \\cdot b$ yazmak", "$10a+b$"],
                ["Kalanı bölenden büyük almak", "Kalan bölenden küçüktür"],
                ["Ortalamaları doğrudan çıkarmak", "Önce toplamları bul"],
                ["Tersten çözerken işlem sırasını karıştırmak", "Sondan başa ters işlem"],
                ["Bulunan $x$ i cevap sanmak", "Sorulan sayıyı hesapla"],
            ]),
            "Bu hataların çoğu, sayılar arasındaki ilişkiyi cebire çevirirken yapılır. Kurulan her ifadeyi küçük bir sayıyla denemek, örneğin iki basamaklı sayıda $47$ için $10a+b$ nin gerçekten $47$ verdiğini görmek, hatayı işin başında yakalar.",
        ]},
    ],
    "sss": [
        ("Sayı problemi nedir?",
         "Bilinmeyen bir ya da birkaç sayının, aralarındaki toplam, fark, kat, ardışıklık ya da bölme ilişkileri verilerek bulunmasını isteyen problemdir."),
        ("Toplamı ve farkı verilen iki sayı nasıl bulunur?",
         "Büyük sayı, toplam ile farkın toplamının yarısıdır; küçük sayı, toplamdan farkın çıkarılmasının yarısıdır."),
        ("Ardışık çift sayılar nasıl yazılır?",
         "En küçüğü x olmak üzere x, x artı iki, x artı dört diye yazılır. Ardışık tek sayılar da aynı biçimde yazılır; yalnızca x tektir."),
        ("İki basamaklı sayı nasıl ifade edilir?",
         "Onlar basamağı a, birler basamağı b olan sayı on a artı b olarak yazılır. Rakamların yeri değişince sayı on b artı a olur."),
        ("Ortalama problemlerinde nereden başlanır?",
         "Önce toplam bulunur. Toplam, ortalama ile sayı adedinin çarpımıdır; sonraki işlemler toplamlar üzerinden yapılır."),
        ("Tersten çözme ne zaman kullanılır?",
         "Bir sayıya art arda işlemler uygulanıp sonuç verildiğinde kullanılır. Sondan başa doğru her işlemin tersi uygulanır."),
        ("Oranı verilen iki sayı nasıl bulunur?",
         "Sayılar oran sayılarının ortak bir k ile çarpımı olarak yazılır. Toplam ya da fark gibi ikinci bilgi k yı verir ve sayılar hesaplanır."),
        ("Kalanları verilen sayı nasıl bulunur?",
         "Koşulları sağlayan en küçük sayı deneme ile bulunur. Sonraki çözümler, bölenlerin EKOK'u kadar aralıklarla tekrar eder."),
        ("Birden fazla sayı varsa hangisine x denir?",
         "Diğer sayıların en kolay ifade edildiği sayıya x denir. Genellikle bu, başka sayıların katı ya da fazlası olarak anlatılan sayıdır."),
    ],
    "kontrol": [
        "Sayı problemlerinde verilen ilişkileri denkleme çevirebiliyorum.",
        "Toplamı ve farkı verilen iki sayıyı bulabiliyorum.",
        "Kat ilişkisinde küçük sayıya bilinmeyen vermeyi tercih edebiliyorum.",
        "Ardışık tam, çift ve tek sayıları doğru yazabiliyorum.",
        "Ardışık sayılarda ortalama kısayolunu kullanabiliyorum.",
        "Bölünen, bölen, bölüm ve kalan ilişkisini kullanabiliyorum.",
        "İki basamaklı sayıları rakamları cinsinden ifade edebiliyorum.",
        "Kesirli ifadelerle kurulan sayı problemlerini çözebiliyorum.",
        "Ortalama problemlerini toplamlar üzerinden çözebiliyorum.",
        "Art arda işlemler verilen sorularda tersten çözme yapabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["denklem-kurma-problemleri-nasil-cozulur", "ardisik-sayilar", "birinci-dereceden-denklemler-konu-anlatimi-pdf"],
}
