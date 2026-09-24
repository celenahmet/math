# scripts/yazilar/95_olasilik.py — Olasilik (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "olasilik-konu-anlatimi-pdf",
    "baslik": "Olasılık Konu Anlatımı PDF",
    "aciklama": "Olasılık nedir? Örnek uzay, olay, tümleyen, iki zar, birleşim, bağımsız olaylar, geri koymalı ve koymasız çekiliş, kombinasyonla olasılık ve koşullu olasılık.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "sayma",
    "sinavlar": ["TYT", "AYT", "ALES", "KPSS"],
    "kapak": "olasilik-konu-anlatimi-pdf",
    "kapak_alt": "Olasılık: bir torbadan top çeken, önünde renkli bir çark ve delikli bir tahta bulunan öğrenci",
    "ozet": "Olasılık, bir olayın gerçekleşme şansını sıfır ile bir arasında bir sayıyla ölçer. Zar atmak, torbadan top çekmek ya da bir çarkı çevirmek sonucu önceden bilinemeyen deneylerdir; ama her sonucun ne kadar olası olduğu hesaplanabilir. Bu yazıda örnek uzay ve olay kavramlarını, klasik olasılık tanımını, tümleyen olayı, iki zar sorularını, birleşim kuralını, bağımsız olayları, geri koymalı ve geri koymasız çekilişleri, kombinasyonla olasılığı, koşullu olasılığı ve deneysel olasılığı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Deney, örnek uzay ve olay", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesirleri, permütasyonu ve kombinasyonu biliyor olman yeterli.",
                "Sayma yöntemleri için <a href=\"/blog/permutasyon-konu-anlatimi-pdf/\">Permütasyon Konu Anlatımı PDF</a> ve <a href=\"/blog/kombinasyon-konu-anlatimi-pdf/\">Kombinasyon Konu Anlatımı PDF</a> yazılarına göz at."),
            "Sonucu önceden kesin olarak bilinemeyen bir işleme <strong>deney</strong>, deneyin her olası sonucuna <strong>çıktı</strong>, bütün çıktıların kümesine <strong>örnek uzay</strong> denir. Örnek uzayın herhangi bir alt kümesi bir <strong>olaydır</strong>. Olasılık hesabının ilk adımı her zaman örnek uzayı doğru yazmaktır.",
            ornek(
                "Bir zar atılsın.",
                "Örnek uzayı ve \"çift sayı gelmesi\" olayını yazalım.",
                "Örnek uzay: $S=\\{1, 2, 3, 4, 5, 6\\}$; $6$ çıktı.",
                "Çift sayı gelmesi olayı: $A=\\{2, 4, 6\\}$; $3$ çıktı."),
            hap("Örnek uzay bütün çıktıların kümesidir.",
                "Olay, örnek uzayın bir alt kümesidir."),
        ]},
        {"baslik": "Klasik olasılık tanımı", "icerik": [
            "Örnek uzaydaki bütün çıktıların gerçekleşme şansı eşitse bir $A$ olayının olasılığı, olaydaki çıktı sayısının örnek uzaydaki çıktı sayısına bölümüdür:",
            "$$P(A)=\\dfrac{s(A)}{s(S)}$$",
            "Buradan olasılığın temel özellikleri çıkar: her olasılık $0$ ile $1$ arasındadır. Hiç gerçekleşmeyecek olayın olasılığı $0$, kesin gerçekleşecek olayın olasılığı $1$ dir.",
            ornek(
                "Bir zar atılsın.",
                "Çift sayı gelme ve $4$ ten büyük sayı gelme olasılıklarını bulalım.",
                "Çift sayı: $\\{2, 4, 6\\}$; $P=\\dfrac{3}{6}=\\dfrac{1}{2}$.",
                "$4$ ten büyük sayı: $\\{5, 6\\}$; $P=\\dfrac{2}{6}=\\dfrac{1}{3}$."),
            dikkat(
                "Çıktıların eşit olası olduğunu kontrol etmemek.",
                "Klasik tanım yalnızca bütün çıktılar eşit şansa sahipse geçerlidir. İki zarın toplamını örnek uzay olarak almak ve $2$ den $12$ ye kadar $11$ çıktıyı eşit olası saymak yanlıştır; toplam $7$ nin gelme şansı toplam $2$ ninkinden çok daha büyüktür."),
        ]},
        {"baslik": "Tümleyen olay", "icerik": [
            "Bir $A$ olayının gerçekleşmemesi olayına $A$ nın <strong>tümleyeni</strong> denir ve $A'$ ile gösterilir. Bir olay ya gerçekleşir ya gerçekleşmez, üçüncü bir durum yoktur; bu yüzden iki olasılığın toplamı her zaman $1$ dir:",
            "$$P(A')=1-P(A)$$",
            "Tümleyen, özellikle \"en az bir\" sorularında hesabı çok kısaltır: en az bir kez gerçekleşme olasılığı, hiç gerçekleşmeme olasılığının $1$ den çıkarılmasıyla bulunur.",
            ornek(
                "Bir para üç kez atılsın.",
                "En az bir kez tura gelme olasılığını bulalım.",
                "Örnek uzayda $2^3=8$ çıktı vardır.",
                "Hiç tura gelmemesi, yani üçünün de yazı gelmesi tek bir çıktıdır: $P=\\dfrac{1}{8}$.",
                "En az bir tura: $1-\\dfrac{1}{8}=\\dfrac{7}{8}$."),
        ]},
        {"baslik": "İki zar atma", "icerik": [
            "İki zar atıldığında her zar için $6$ sonuç vardır ve örnek uzayda $6 \\cdot 6=36$ eşit olası çıktı bulunur. Zarlar farklı kabul edilir: birinci zarın $1$, ikincinin $2$ gelmesi ile birincinin $2$, ikincinin $1$ gelmesi ayrı çıktılardır.",
            tablo(["Toplam", "Çıktı sayısı", "Olasılık"], [
                ["$2$", "$1$", "$\\dfrac{1}{36}$"],
                ["$4$", "$3$", "$\\dfrac{3}{36}$"],
                ["$6$", "$5$", "$\\dfrac{5}{36}$"],
                ["$7$", "$6$", "$\\dfrac{6}{36}$"],
                ["$10$", "$3$", "$\\dfrac{3}{36}$"],
                ["$12$", "$1$", "$\\dfrac{1}{36}$"],
            ]),
            ornek(
                "İki zar atılsın.",
                "Toplamın $7$ ve toplamın $10$ olma olasılıklarını bulalım.",
                "Toplam $7$: $(1,6)$, $(2,5)$, $(3,4)$, $(4,3)$, $(5,2)$, $(6,1)$; $6$ çıktı. $P=\\dfrac{6}{36}=\\dfrac{1}{6}$.",
                "Toplam $10$: $(4,6)$, $(5,5)$, $(6,4)$; $3$ çıktı. $P=\\dfrac{3}{36}=\\dfrac{1}{12}$."),
            "Toplam $7$, iki zarda en olası toplamdır, çünkü birinci zar ne gelirse gelsin ikinci zarın toplamı $7$ yapacak tam bir değeri vardır. Toplamlar $7$ den uzaklaştıkça çıktı sayısı birer birer azalır ve $2$ ile $12$ yalnızca birer çıktıyla oluşur.",
        ]},
        {"baslik": "Üç para atışı", "icerik": [
            "Birden fazla para atıldığında örnek uzayın her çıktısı, her paranın sonucunu sırayla belirten bir dizidir. Üç para için $2^3=8$ eşit olası çıktı vardır.",
            ornek(
                "Üç para atılsın.",
                "Tam olarak iki tura gelme olasılığını bulalım.",
                "Tam iki tura içeren çıktılar: TTY, TYT ve YTT; $3$ çıktı.",
                "$P=\\dfrac{3}{8}$. Tam bir tura gelme olasılığı da $\\dfrac{3}{8}$, hiç ya da üç tura gelme olasılıkları ise birer sekizde birdir; dört olasılığın toplamı $1$ dir."),
            "Aynı sayı kombinasyonla da bulunur: üç paradan hangi ikisinin tura geleceğini seçmek $C(3, 2)=3$ yolla yapılır. Bu yöntem para sayısı büyüdüğünde, örneğin on para atıldığında, bütün çıktıları yazmaktan çok daha pratiktir.",
        ]},
        {"baslik": "Hiçbiri ve en az biri", "icerik": [
            "Bağımsız denemelerde bir olayın hiç gerçekleşmemesi, her denemede gerçekleşmemesi demektir; bu yüzden gerçekleşmeme olasılıkları çarpılır. En az bir kez gerçekleşme olasılığı ise bunun tümleyenidir.",
            ornek(
                "İki zar atılsın.",
                "Hiçbir zarda $6$ gelmeme ve en az bir zarda $6$ gelme olasılıklarını bulalım.",
                "Bir zarda $6$ gelmeme olasılığı $\\dfrac{5}{6}$ tir. İki zarda da gelmemesi: $\\dfrac{5}{6} \\cdot \\dfrac{5}{6}=\\dfrac{25}{36}$.",
                "En az bir zarda $6$: $1-\\dfrac{25}{36}=\\dfrac{11}{36}$."),
            dikkat(
                "En az bir olasılığını toplayarak bulmak.",
                "Her zarda $6$ gelme olasılığı $\\dfrac{1}{6}$ olduğu için $\\dfrac{1}{6}+\\dfrac{1}{6}=\\dfrac{12}{36}$ demek yanlıştır; iki zarda birden $6$ gelmesi iki kez sayılmış olur. Doğru sonuç $\\dfrac{11}{36}$ dir."),
        ]},
        {"baslik": "Sıralama olasılığı", "icerik": [
            "Kişiler ya da nesneler rastgele sıralandığında her sıralama eşit olasıdır. İstenen koşulu sağlayan sıralamaların sayısı, bütün sıralamaların sayısına bölünür.",
            ornek(
                "A ve B nin de bulunduğu $5$ kişi rastgele bir sıraya diziliyor.",
                "A ile B nin yan yana olma olasılığını bulalım.",
                "Bütün sıralamalar: $5!=120$.",
                "Yan yana oldukları sıralamalar: $4! \\cdot 2!=48$.",
                "$P=\\dfrac{48}{120}=\\dfrac{2}{5}$."),
        ]},
        {"baslik": "İkinci çekilişin rengi", "icerik": [
            "Geri koymasız çekilişte ikinci topun bir renkte olma olasılığı, birinci topun rengine göre iki duruma ayrılarak hesaplanır. Sonuç şaşırtıcı biçimde birinci çekilişin olasılığıyla aynı çıkar.",
            ornek(
                "Bir torbada $4$ kırmızı ve $6$ mavi top var. Art arda geri koymadan iki top çekiliyor.",
                "İkinci topun kırmızı olma olasılığını bulalım.",
                "Birinci kırmızı, ikinci kırmızı: $\\dfrac{4}{10} \\cdot \\dfrac{3}{9}=\\dfrac{12}{90}$.",
                "Birinci mavi, ikinci kırmızı: $\\dfrac{6}{10} \\cdot \\dfrac{4}{9}=\\dfrac{24}{90}$.",
                "Toplam: $\\dfrac{36}{90}=\\dfrac{2}{5}$; birinci çekilişte kırmızı gelme olasılığıyla aynı."),
            "Bu sonucun nedeni simetridir: birinci topun rengi bilinmediği sürece, ikinci top da torbadaki herhangi bir top olabilir. Hangi sırada çekildiği bilinmeyen bir topun bir renkte olma olasılığı, o renkteki topların oranıdır.",
        ]},
        {"baslik": "Torbadan top çekmek", "icerik": [
            "Bir torbadan rastgele bir top çekildiğinde her topun çekilme şansı eşittir; renklerin şansı ise o renkteki top sayısıyla orantılıdır. İstenen renkteki topların sayısı, toplam top sayısına bölünür.",
            ornek(
                "Bir torbada $4$ kırmızı ve $6$ mavi top var.",
                "Çekilen bir topun kırmızı olma olasılığını bulalım.",
                "Toplam top: $10$. Kırmızı top: $4$.",
                "$P=\\dfrac{4}{10}=\\dfrac{2}{5}$. Mavi olma olasılığı ise $\\dfrac{3}{5}$ tür ve iki olasılığın toplamı $1$ dir."),
        ]},
        {"baslik": "Birleşim kuralı", "icerik": [
            "\"$A$ ya da $B$\" olayının olasılığı, iki olayın olasılıklarının toplamından ortak kısmın olasılığı çıkarılarak bulunur, çünkü ortak kısım iki kez sayılmıştır:",
            "$$P(A \\cup B)=P(A)+P(B)-P(A \\cap B)$$",
            ornek(
                "$1$ den $20$ ye kadar numaralanmış kartlardan biri rastgele çekiliyor.",
                "Çekilen kartın $2$ nin ya da $3$ ün katı olma olasılığını bulalım.",
                "$2$ nin katları: $10$ kart. $3$ ün katları: $6$ kart. Her ikisinin, yani $6$ nın katları: $3$ kart.",
                "İstenen kartlar: $10+6-3=13$.",
                "$P=\\dfrac{13}{20}$."),
            "İki olayın ortak çıktısı yoksa bu olaylara <strong>ayrık</strong> denir ve birleşimin olasılığı olasılıkların doğrudan toplamıdır. Bir zarda $1$ gelmesi ile $6$ gelmesi ayrık olaylardır: $\\dfrac{1}{6}+\\dfrac{1}{6}=\\dfrac{1}{3}$.",
        ]},
        {"baslik": "Bağımsız olaylar", "icerik": [
            "Bir olayın gerçekleşmesi diğerinin olasılığını değiştirmiyorsa bu olaylar <strong>bağımsızdır</strong>. Bağımsız iki olayın birlikte gerçekleşme olasılığı, olasılıklarının çarpımıdır:",
            "$$P(A \\cap B)=P(A) \\cdot P(B)$$",
            ornek(
                "Bir para ve bir zar birlikte atılıyor.",
                "Paranın tura, zarın $6$ gelme olasılığını bulalım.",
                "Para ve zar birbirini etkilemez; olaylar bağımsızdır.",
                "$P=\\dfrac{1}{2} \\cdot \\dfrac{1}{6}=\\dfrac{1}{12}$."),
            dikkat(
                "Ayrık olayları bağımsız sanmak.",
                "Ayrık olaylar birlikte gerçekleşemez; bu yüzden biri gerçekleşince diğerinin olasılığı sıfıra düşer. Yani olasılıkları sıfırdan farklı ayrık olaylar bağımsız değildir. Ayrık olaylarda olasılıklar toplanır, bağımsız olaylarda çarpılır."),
        ]},
        {"baslik": "Geri koymalı ve geri koymasız çekiliş", "icerik": [
            "Bir torbadan art arda top çekilirken çekilen top geri konuyorsa torbanın durumu her çekilişte aynı kalır ve çekilişler bağımsızdır. Top geri konmuyorsa ikinci çekilişin olasılıkları birinci çekilişin sonucuna bağlıdır.",
            ornek(
                "Bir torbada $4$ kırmızı ve $6$ mavi top var. Art arda iki top çekiliyor.",
                "Çekilen iki topun da kırmızı olma olasılığını, geri koyarak ve geri koymadan çekildiğinde bulalım.",
                "Geri koyarak: $\\dfrac{4}{10} \\cdot \\dfrac{4}{10}=\\dfrac{16}{100}=\\dfrac{4}{25}$.",
                "Geri koymadan: birinci top kırmızı gelirse torbada $3$ kırmızı ve toplam $9$ top kalır: $\\dfrac{4}{10} \\cdot \\dfrac{3}{9}=\\dfrac{12}{90}=\\dfrac{2}{15}$."),
            "Geri koymasız çekiliş kombinasyonla da hesaplanır: iki kırmızı seçme sayısı $C(4, 2)=6$, iki top seçme sayısı $C(10, 2)=45$ tir. Olasılık $\\dfrac{6}{45}=\\dfrac{2}{15}$ bulunur ve sonuç aynıdır.",
        ]},
        {"baslik": "Kombinasyonla olasılık", "icerik": [
            "Bir gruptan rastgele seçim yapıldığında hem örnek uzay hem de olay kombinasyonla sayılır. Olasılık, istenen seçimlerin sayısının bütün seçimlerin sayısına bölümüdür. Pay ile paydanın aynı yöntemle, yani ikisinin de sırasız seçim olarak sayılması gerekir.",
            ornek(
                "A ve B nin de bulunduğu $10$ kişiden rastgele $3$ kişilik bir ekip seçiliyor.",
                "A ile B nin ikisinin de ekipte olma olasılığını bulalım.",
                "Bütün seçimler: $C(10, 3)=120$.",
                "A ile B ekipteyse kalan $1$ kişi kalan $8$ kişiden seçilir: $C(8, 1)=8$.",
                "$P=\\dfrac{8}{120}=\\dfrac{1}{15}$."),
            ornek(
                "$5$ kız ve $4$ erkek öğrenciden rastgele $3$ kişi seçiliyor.",
                "Seçilenlerin $2$ sinin kız, $1$ inin erkek olma olasılığını bulalım.",
                "Bütün seçimler: $C(9, 3)=84$.",
                "İstenen seçimler: $C(5, 2) \\cdot C(4, 1)=10 \\cdot 4=40$.",
                "$P=\\dfrac{40}{84}=\\dfrac{10}{21}$."),
        ]},
        {"baslik": "Koşullu olasılık", "icerik": [
            "Bir olayın gerçekleştiği bilindiğinde başka bir olayın olasılığı değişebilir. $B$ nin gerçekleştiği bilindiğinde $A$ nın olasılığına <strong>koşullu olasılık</strong> denir ve şöyle hesaplanır:",
            "$$P(A|B)=\\dfrac{P(A \\cap B)}{P(B)}$$",
            "Eşit olası çıktılarda bu, örnek uzayın $B$ olayına daraltılması demektir: yeni örnek uzay $B$ dir ve $A$ nın $B$ içindeki çıktıları sayılır.",
            ornek(
                "Bir zar atılıyor ve gelen sayının $4$ ten büyük olduğu biliniyor.",
                "Gelen sayının çift olma olasılığını bulalım.",
                "Yeni örnek uzay: $\\{5, 6\\}$.",
                "Bu kümedeki çift sayı yalnızca $6$ dır: $P=\\dfrac{1}{2}$.",
                "Bilgi olmadan çift gelme olasılığı da $\\dfrac{1}{2}$ dir; burada bilgi olasılığı değiştirmemiştir."),
            ornek(
                "İki çocuklu bir ailenin çocuklarından en az birinin kız olduğu biliniyor. Her çocuğun kız ya da erkek olma olasılığı eşit kabul ediliyor.",
                "İki çocuğun da kız olma olasılığını bulalım.",
                "Olası durumlar: KK, KE, EK, EE. En az bir kız bilgisi EE durumunu eler.",
                "Kalan $3$ eşit olası durumdan yalnızca KK istenen durumdur: $P=\\dfrac{1}{3}$."),
        ]},
        {"baslik": "Çark ve alan olasılığı", "icerik": [
            "Bir çark eşit dilimlere bölünmüşse her dilimin gelme olasılığı eşittir. Dilimler eşit değilse olasılık, dilimin çarkın tamamına oranıdır; yani dilimin açısının $360$ dereceye bölümüdür. Kapaktaki çark da bu türden bir deneydir.",
            ornek(
                "Bir çark $8$ eşit dilime bölünmüş ve dilimlerin $3$ ü kırmızı.",
                "Çark çevrildiğinde kırmızı gelme olasılığını bulalım.",
                "$P=\\dfrac{3}{8}$."),
            ornek(
                "Bir çarkın mavi bölgesinin merkez açısı $120$ derece.",
                "Mavi gelme olasılığını bulalım.",
                "$P=\\dfrac{120}{360}=\\dfrac{1}{3}$."),
        ]},
        {"baslik": "Deneysel olasılık", "icerik": [
            "Olasılık, deney tekrar edilerek de tahmin edilebilir: bir olayın gerçekleşme sayısı toplam deneme sayısına bölünür. Bu orana <strong>deneysel olasılık</strong> ya da bağıl sıklık denir.",
            ornek(
                "Bir para $100$ kez atılıyor ve $47$ kez tura geliyor.",
                "Tura gelmenin deneysel olasılığını bulalım.",
                "Deneysel olasılık: $\\dfrac{47}{100}=0.47$.",
                "Teorik olasılık $\\dfrac{1}{2}=0.5$ tir; aradaki fark rastlantısaldır."),
            "Deneme sayısı arttıkça deneysel olasılık teorik olasılığa yaklaşma eğilimi gösterir. Bu gözlem, olasılığın günlük hayatta neden işe yaradığını da açıklar: tek bir atışın sonucu tahmin edilemez ama çok sayıda atışın toplam davranışı öngörülebilir. Az sayıda denemede ise iki değer arasında belirgin farklar görülebilir; $10$ atışta $7$ tura gelmesi paranın hileli olduğunu göstermez.",
        ]},
        {"baslik": "Sınavda olasılık", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) olasılık zar, para, torba ve kart soruları, tümleyen ve basit birleşim biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) koşullu olasılık, bağımsız olaylar ve kombinasyonla olasılık da sorulur; <strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde olasılık sayısal akıl yürütmenin parçasıdır."),
            "Bir olasılık sorusunda önce örnek uzayı ve çıktıların eşit olası olup olmadığını belirle. Sonra \"en az\" gibi bir ifade varsa tümleyeni dene, art arda olaylar varsa bağımsız olup olmadıklarına karar ver. Bu üç adım, soruların büyük bölümünü düzenli bir yola sokar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Eşit olası olmayan çıktıları eşit saymak", "Örnek uzayı eşit olası kur"],
                ["İki zarda $(1,2)$ ve $(2,1)$ i aynı saymak", "Ayrı çıktılardır"],
                ["Birleşimde ortak kısmı çıkarmamak", "Ortak kısım bir kez sayılır"],
                ["Ayrık olayları bağımsız sanmak", "Ayrıklar toplanır, bağımsızlar çarpılır"],
                ["Geri koymasız çekilişte torbayı güncellememek", "İkinci çekilişte top sayısı azalır"],
                ["Olasılığı $1$ den büyük bulmak", "Olasılık $0$ ile $1$ arasındadır"],
            ]),
            "Bu hataların çoğu, örnek uzayı dikkatle yazmamaktan doğar. Küçük örnek uzaylarda bütün çıktıları tek tek yazmak, hem sayma hatalarını hem de eşit olasılık yanılgılarını önler.",
        ]},
    ],
    "sss": [
        ("Olasılık nedir?",
         "Bir olayın gerçekleşme şansını 0 ile 1 arasında bir sayıyla ölçen kavramdır. Eşit olası çıktılarda olaydaki çıktı sayısının örnek uzaydaki çıktı sayısına bölümüdür."),
        ("Örnek uzay nedir?",
         "Bir deneyin bütün olası sonuçlarının kümesidir. Bir zar atıldığında örnek uzay 1 den 6 ya kadar olan sayılardır."),
        ("Tümleyen olay ne işe yarar?",
         "Bir olayın gerçekleşmeme olasılığı 1 eksi gerçekleşme olasılığıdır. En az bir kez gerçekleşme sorularında hesabı çok kısaltır."),
        ("Bağımsız olaylar nasıl hesaplanır?",
         "Bir olayın gerçekleşmesi diğerini etkilemiyorsa iki olayın birlikte gerçekleşme olasılığı olasılıklarının çarpımıdır."),
        ("Geri koymalı ve geri koymasız çekiliş arasındaki fark nedir?",
         "Geri koymalı çekilişte torba her seferinde aynı kalır ve çekilişler bağımsızdır. Geri koymasız çekilişte çekilen top torbadan çıktığı için sonraki olasılıklar değişir."),
        ("Koşullu olasılık nedir?",
         "Bir olayın gerçekleştiği bilindiğinde başka bir olayın olasılığıdır. Eşit olası çıktılarda örnek uzay bilinen olaya daraltılarak hesaplanır."),
        ("İki zarda en az birinde 6 gelme olasılığı nedir?",
         "Hiçbirinde 6 gelmeme olasılığı 5 bölü 6 nın karesi, yani 25 bölü 36 dır. En az birinde 6 gelme olasılığı bunun tümleyeni olan 11 bölü 36 dır."),
    ],
    "kontrol": [
        "Deney, çıktı, örnek uzay ve olay kavramlarını ayırt edebiliyorum.",
        "Klasik olasılık tanımını eşit olası çıktılarda uygulayabiliyorum.",
        "Tümleyen olayla en az bir sorularını çözebiliyorum.",
        "İki zar atma sorularında 36 çıktıyı kullanabiliyorum.",
        "Birleşim kuralında ortak kısmı doğru hesaba katabiliyorum.",
        "Ayrık ve bağımsız olayları ayırt edebiliyorum.",
        "Geri koymalı ve geri koymasız çekilişleri hesaplayabiliyorum.",
        "Kombinasyonla olasılık sorularını çözebiliyorum.",
        "Koşullu olasılıkta örnek uzayı daraltabiliyorum.",
        "Deneysel olasılık ile teorik olasılığı karşılaştırabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kombinasyon-konu-anlatimi-pdf", "permutasyon-konu-anlatimi-pdf", "kumeler-konu-anlatimi-pdf"],
}
