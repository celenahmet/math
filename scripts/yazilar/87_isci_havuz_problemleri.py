# scripts/yazilar/87_isci_havuz_problemleri.py — Isci ve Havuz Problemleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "isci-ve-havuz-problemleri-konu-anlatimi-pdf",
    "baslik": "İşçi ve Havuz Problemleri Konu Anlatımı PDF",
    "aciklama": "İşçi ve havuz problemleri nasıl çözülür? Çalışma hızı, birlikte ve sırayla çalışma, işçi sayısı, dolduran ve boşaltan musluklar ve kısmen dolu havuz; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "isci-ve-havuz-problemleri-konu-anlatimi-pdf",
    "kapak_alt": "İşçi ve havuz problemleri: şeffaf bir hazneye iki kanaldan boncuk akıtarak dolum hızlarını karşılaştıran iki öğrenci",
    "ozet": "İşçi ve havuz problemleri aynı fikre dayanır: bir işi ya da bir havuzu dolduran herkesin bir çalışma hızı vardır ve birlikte çalışıldığında hızlar toplanır. Süreler asla toplanmaz. Bu yazıda çalışma hızı kavramını, iki ve üç kişinin birlikte çalışmasını, iki kişi için kısa formülü, bir kişinin süresini bulmayı, ara verme ve sırayla çalışma sorularını, işçi sayısı ile süre ilişkisini, farklı hızdaki işçileri, dolduran ve boşaltan muslukları ve kısmen dolu havuzları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Çalışma hızı fikri", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesirlerle toplama ve çıkarmayı ve basit denklem kurmayı biliyor olman yeterli.",
                "Kesir işlemleri için <a href=\"/blog/kesirlerde-toplama-ve-cikarma/\">Kesirlerde Toplama ve Çıkarma</a>, kesirli kurulum için <a href=\"/blog/kesir-problemleri-nasil-cozulur/\">Kesir Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "İşçi problemlerinde yapılacak işin kendisi genellikle bir sayıyla verilmez: bir duvar, bir proje ya da bir sipariş. Bu yüzden <strong>işin tamamı $1$ birim</strong> kabul edilir. Bir işi tek başına $t$ günde bitiren biri, bir günde işin $\\dfrac{1}{t}$ kadarını yapar. Bu değere o kişinin <strong>çalışma hızı</strong> denir.",
            "Birlikte çalışan kişilerin bir günde yaptığı iş, hızlarının toplamıdır. Hızların toplamı bulunduğunda birlikte bitirme süresi, bu toplamın tersidir. Kapaktaki iki kanaldan akan boncuklar bu fikrin somut hâlidir: iki kanal birlikte açıkken hazne, kanalların akış hızlarının toplamıyla dolar.",
            tablo(["Durum", "Bir günde yapılan iş"], [
                ["İşi tek başına $a$ günde bitiren", "$\\dfrac{1}{a}$"],
                ["İşi tek başına $b$ günde bitiren", "$\\dfrac{1}{b}$"],
                ["İkisi birlikte", "$\\dfrac{1}{a}+\\dfrac{1}{b}$"],
                ["Birlikte bitirme süresi", "$\\dfrac{1}{\\frac{1}{a}+\\frac{1}{b}}$"],
            ]),
            hap("İşin tamamı $1$ birimdir; $t$ günde bitiren kişinin hızı $\\dfrac{1}{t}$ dir.",
                "Birlikte çalışmada hızlar toplanır, süreler toplanmaz."),
        ]},
        {"baslik": "İki kişi birlikte çalışırsa", "icerik": [
            "İki kişinin tek başına bitirme süreleri biliniyorsa birlikte bitirme süresi, hızlar toplanarak bulunur.",
            ornek(
                "Bir işi Ali tek başına $12$ günde, Veli tek başına $24$ günde bitiriyor.",
                "İkisinin birlikte bu işi kaç günde bitireceğini bulalım.",
                "Hızlar: $\\dfrac{1}{12}$ ve $\\dfrac{1}{24}$. Toplam: $\\dfrac{2}{24}+\\dfrac{1}{24}=\\dfrac{3}{24}=\\dfrac{1}{8}$.",
                "Birlikte bir günde işin sekizde birini yaparlar; iş $8$ günde biter."),
            "<h3>İki kişi için kısa formül</h3>",
            "Yalnızca iki kişi için hızların toplamının tersi tek bir kesirle yazılabilir. Tek başına $a$ ve $b$ günde bitirenler birlikte $\\dfrac{a \\cdot b}{a+b}$ günde bitirir. Örnekte $\\dfrac{12 \\cdot 24}{12+24}=\\dfrac{288}{36}=8$ gün bulunur.",
            dikkat(
                "Süreleri toplamak ya da ortalamasını almak.",
                "$12+24=36$ gün ya da ortalama $18$ gün demek yanlıştır. Birlikte çalışan iki kişi, işi tek başına en hızlı olanından bile daha kısa sürede bitirir. Sonuç her zaman en kısa süreden küçüktür: burada $8<12$."),
        ]},
        {"baslik": "Üç kişi birlikte çalışırsa", "icerik": [
            "Üç ya da daha fazla kişi için kısa formül işlemez; hızlar tek tek toplanır. Paydaların EKOK'u ortak payda olarak kullanılır.",
            ornek(
                "Bir işi A $10$ günde, B $15$ günde, C $30$ günde bitiriyor.",
                "Üçünün birlikte kaç günde bitireceğini bulalım.",
                "Ortak payda $30$: $\\dfrac{3}{30}+\\dfrac{2}{30}+\\dfrac{1}{30}=\\dfrac{6}{30}=\\dfrac{1}{5}$.",
                "Birlikte bir günde işin beşte birini yaparlar; iş $5$ günde biter."),
            "İşin tamamını $1$ yerine paydaların EKOK'u kadar birim almak da hesabı sadeleştirir. İş $30$ birim olursa A günde $3$, B $2$, C $1$ birim yapar; birlikte günde $6$ birim yaparlar ve $30$ birimi $5$ günde bitirirler.",
        ]},
        {"baslik": "Bir kişinin süresini bulmak", "icerik": [
            "Birlikte bitirme süresi ve kişilerden birinin süresi biliniyorsa, diğerinin hızı toplam hızdan çıkarılarak bulunur.",
            ornek(
                "A bir işi tek başına $20$ günde bitiriyor. A ile B birlikte aynı işi $12$ günde bitiriyor.",
                "B nin işi tek başına kaç günde bitireceğini bulalım.",
                "B nin hızı: $\\dfrac{1}{12}-\\dfrac{1}{20}=\\dfrac{5}{60}-\\dfrac{3}{60}=\\dfrac{2}{60}=\\dfrac{1}{30}$.",
                "B işi tek başına $30$ günde bitirir; yani A dan daha yavaş çalışır.",
                "Kontrol: $\\dfrac{1}{20}+\\dfrac{1}{30}=\\dfrac{3}{60}+\\dfrac{2}{60}=\\dfrac{1}{12}$."),
        ]},
        {"baslik": "Bir süre birlikte, sonra tek başına", "icerik": [
            "Kişiler bir süre birlikte çalışıp sonra biri ayrılırsa, önce birlikte yapılan iş hesaplanır, sonra kalan işin tek başına kalan kişi tarafından ne kadar sürede bitirileceği bulunur.",
            ornek(
                "Bir işi A $18$ günde, B $36$ günde bitiriyor. İkisi birlikte $4$ gün çalışıyor, sonra B ayrılıyor ve işi A tek başına bitiriyor.",
                "İşin toplam kaç günde bittiğini bulalım.",
                "Birlikte bir günlük iş: $\\dfrac{1}{18}+\\dfrac{1}{36}=\\dfrac{3}{36}=\\dfrac{1}{12}$. $4$ günde: $\\dfrac{4}{12}=\\dfrac{1}{3}$.",
                "Kalan iş: $1-\\dfrac{1}{3}=\\dfrac{2}{3}$. A bunu $\\dfrac{2}{3} \\cdot 18=12$ günde bitirir.",
                "İş toplam $4+12=16$ günde biter."),
            dikkat(
                "Kalan işi bütün iş gibi hesaplamak.",
                "B ayrıldıktan sonra A nın işin tamamını değil yalnızca kalan üçte ikisini yapacağı unutulmamalıdır. A nın süresi $18$ gün değil, $12$ gündür."),
        ]},
        {"baslik": "Sırayla çalışma", "icerik": [
            "Bir kişi işe başlayıp bir süre sonra ayrıldığında işi bir başkası devralırsa, her kişinin yaptığı iş ayrı ayrı yazılır ve toplamı $1$ e eşitlenir.",
            ornek(
                "Bir işi A $10$ günde, B $15$ günde bitiriyor. İşe A başlıyor, $4$ gün çalışıp ayrılıyor ve kalan işi B bitiriyor.",
                "B nin kaç gün çalıştığını bulalım.",
                "A nın yaptığı iş: $\\dfrac{4}{10}=\\dfrac{2}{5}$. Kalan: $\\dfrac{3}{5}$.",
                "B kalan işi $\\dfrac{3}{5} \\cdot 15=9$ günde bitirir.",
                "Kontrol: $\\dfrac{4}{10}+\\dfrac{9}{15}=\\dfrac{2}{5}+\\dfrac{3}{5}=1$."),
        ]},
        {"baslik": "İşin bir kısmı verildiğinde", "icerik": [
            "Bazı sorularda bir kişinin işin tamamını değil yalnızca bir kısmını ne kadar sürede yaptığı verilir. Hız değişmediği için önce işin tamamının süresi bulunur, sonra her zamanki gibi hızlar toplanır.",
            ornek(
                "A bir işin beşte ikisini $8$ günde yapıyor. B aynı işin tamamını $30$ günde bitiriyor.",
                "İkisinin birlikte işi kaç günde bitireceğini bulalım.",
                "A işin beşte birini $4$ günde yapar; tamamını $5 \\cdot 4=20$ günde bitirir.",
                "Hızlar toplamı: $\\dfrac{1}{20}+\\dfrac{1}{30}=\\dfrac{3}{60}+\\dfrac{2}{60}=\\dfrac{5}{60}=\\dfrac{1}{12}$.",
                "Birlikte işi $12$ günde bitirirler."),
        ]},
        {"baslik": "Sonradan katılan işçiler", "icerik": [
            "İş sırasında işçi sayısı değişirse işin büyüklüğü işçi-gün olarak hesaplanır. Değişiklikten önce yapılan kısım çıkarılır ve kalan iş yeni işçi sayısına bölünür.",
            ornek(
                "Bir iş $6$ işçiyle $20$ günde bitecektir. $4$ gün sonra işe aynı hızda çalışan $2$ işçi daha katılıyor.",
                "İşin toplam kaç günde biteceğini bulalım.",
                "İşin büyüklüğü: $6 \\cdot 20=120$ işçi-gün. İlk $4$ günde yapılan: $6 \\cdot 4=24$ işçi-gün.",
                "Kalan iş: $120-24=96$ işçi-gün. Artık $8$ işçi var: $96:8=12$ gün.",
                "İş toplam $4+12=16$ günde biter; planlanandan $4$ gün önce."),
            "Aynı yöntem işçilerin ayrıldığı durumlarda da işler; tek fark, kalan işin daha az işçiye bölünmesi ve sürenin uzamasıdır.",
        ]},
        {"baslik": "İşçi sayısı ve süre", "icerik": [
            "Aynı hızda çalışan işçilerde işçi sayısı ile işin bitme süresi ters orantılıdır: işçi sayısı ile gün sayısının çarpımı, işin <strong>işçi-gün</strong> olarak büyüklüğünü verir ve sabittir.",
            ornek(
                "Bir işi $8$ işçi $15$ günde bitiriyor.",
                "Aynı işi aynı hızda çalışan $12$ işçinin kaç günde bitireceğini bulalım.",
                "İşin büyüklüğü: $8 \\cdot 15=120$ işçi-gün.",
                "$12$ işçi: $120:12=10$ gün."),
            "İşçi sayısı ile sürenin ters orantısı <a href=\"/blog/dogru-oranti-ve-ters-oranti/\">Doğru Orantı ve Ters Orantı</a> yazısında da anlatılıyor. İşçi-gün kavramı, iş sırasında işçi sayısı değiştiğinde de kullanılır: yapılan kısım çıkarılır, kalan işçi-gün yeni işçi sayısına bölünür.",
        ]},
        {"baslik": "Farklı hızdaki işçiler", "icerik": [
            "İşçilerin hızları birbirine göre verildiğinde, en yavaş olanın hızına bir harf verilir ve diğerleri onun katı olarak yazılır.",
            ornek(
                "Bir usta, çırağından $2$ kat hızlı çalışıyor ve ikisi birlikte bir işi $6$ günde bitiriyor.",
                "Her birinin işi tek başına kaç günde bitireceğini bulalım.",
                "Çırağın hızı $r$, ustanın hızı $2r$ olsun. Birlikte: $3r \\cdot 6=1$, yani $r=\\dfrac{1}{18}$.",
                "Çırak işi tek başına $18$ günde, usta $9$ günde bitirir.",
                "Kontrol: $\\dfrac{1}{9}+\\dfrac{1}{18}=\\dfrac{3}{18}=\\dfrac{1}{6}$."),
            dikkat(
                "\"$2$ kat hızlı\" ifadesini \"$2$ kat süre\" sanmak.",
                "Usta $2$ kat hızlıysa aynı işi yarı sürede bitirir. Hız ile süre ters orantılıdır; ustanın süresi çırağınkinin $2$ katı değil, yarısıdır."),
        ]},
        {"baslik": "Ara vererek çalışma", "icerik": [
            "Bir işçi düzenli aralıklarla dinleniyorsa işin bitmesi için gereken çalışma günü değişmez; yalnızca takvimdeki toplam süre uzar. Önce kaç gün çalışılması gerektiği bulunur, sonra aradaki dinlenme günleri eklenir.",
            ornek(
                "Bir işçi bir işi tek başına $12$ çalışma gününde bitiriyor. Her $3$ gün çalıştıktan sonra $1$ gün dinleniyor.",
                "İşin takvimde kaç günde biteceğini bulalım.",
                "$12$ çalışma günü, $3$ er günlük $4$ bloktan oluşur.",
                "Bloklar arasında $3$ dinlenme günü vardır; son bloktan sonra iş bittiği için dinlenmeye gerek kalmaz.",
                "Toplam süre: $12+3=15$ gün."),
            dikkat(
                "Son bloktan sonra da dinlenme günü saymak.",
                "İş son çalışma gününde bittiği için ondan sonraki dinlenme günü hesaba katılmaz. $4$ dinlenme günü sayılırsa sonuç $16$ gün çıkar ve yanlıştır."),
        ]},
        {"baslik": "Havuz problemleri: doldurma", "icerik": [
            "Havuz problemleri işçi problemleriyle aynı mantıkla çözülür. Havuzun tamamı $1$ birimdir; bir havuzu $t$ saatte dolduran musluk bir saatte havuzun $\\dfrac{1}{t}$ kadarını doldurur. Birlikte açılan muslukların hızları toplanır.",
            ornek(
                "Bir havuzu birinci musluk $6$ saatte, ikinci musluk $9$ saatte dolduruyor.",
                "İki musluk birlikte açılırsa havuzun kaç saatte dolacağını bulalım.",
                "Hızlar toplamı: $\\dfrac{1}{6}+\\dfrac{1}{9}=\\dfrac{3}{18}+\\dfrac{2}{18}=\\dfrac{5}{18}$.",
                "Süre: $\\dfrac{18}{5}=3.6$ saat, yani $3$ saat $36$ dakika.",
                "Kısa formülle: $\\dfrac{6 \\cdot 9}{6+9}=\\dfrac{54}{15}=3.6$ saat."),
            "Ondalıklı saatler dakikaya çevrilirken ondalık kısım $60$ ile çarpılır: $0.6$ saat $0.6 \\cdot 60=36$ dakikadır.",
        ]},
        {"baslik": "Dolduran ve boşaltan musluklar", "icerik": [
            "Havuzun dibinde bir boşaltma musluğu varsa bu musluğun hızı <strong>çıkarılır</strong>. Net hız pozitifse havuz dolar, negatifse boşalır.",
            ornek(
                "Bir havuzu bir musluk $4$ saatte dolduruyor, dipteki bir musluk ise dolu havuzu $12$ saatte boşaltıyor.",
                "İkisi birlikte açıkken boş havuzun kaç saatte dolacağını bulalım.",
                "Net hız: $\\dfrac{1}{4}-\\dfrac{1}{12}=\\dfrac{3}{12}-\\dfrac{1}{12}=\\dfrac{2}{12}=\\dfrac{1}{6}$.",
                "Havuz $6$ saatte dolar."),
            ornek(
                "Bir havuzu bir musluk $8$ saatte dolduruyor, dipteki musluk ise dolu havuzu $6$ saatte boşaltıyor.",
                "İkisi birlikte açılırsa dolu havuzun ne olacağını bulalım.",
                "Net hız: $\\dfrac{1}{8}-\\dfrac{1}{6}=\\dfrac{3}{24}-\\dfrac{4}{24}=-\\dfrac{1}{24}$.",
                "Net hız negatif olduğu için havuz boşalır; dolu havuz $24$ saatte tamamen boşalır."),
        ]},
        {"baslik": "Kısmen dolu havuzlar", "icerik": [
            "Havuz başlangıçta boş değilse doldurulması gereken kısım $1$ den çıkarılarak bulunur. Süre, bu kısmın net hıza bölünmesiyle hesaplanır.",
            ornek(
                "Bir havuzun üçte biri dolu. Havuzu bir musluk $6$ saatte dolduruyor, dipteki musluk dolu havuzu $9$ saatte boşaltıyor. İkisi birlikte açılıyor.",
                "Havuzun kaç saatte dolacağını bulalım.",
                "Doldurulacak kısım: $1-\\dfrac{1}{3}=\\dfrac{2}{3}$.",
                "Net hız: $\\dfrac{1}{6}-\\dfrac{1}{9}=\\dfrac{3}{18}-\\dfrac{2}{18}=\\dfrac{1}{18}$.",
                "Süre: $\\dfrac{2}{3}:\\dfrac{1}{18}=\\dfrac{2}{3} \\cdot 18=12$ saat."),
            dikkat(
                "Havuzu boş kabul etmek.",
                "Havuz üçte biri doluyken tamamı için $18$ saat hesaplamak, zaten dolu olan kısmı yeniden doldurmaktır. Önce eksik kısım bulunur, sonra süre hesaplanır."),
        ]},
        {"baslik": "Üç musluklu havuz", "icerik": [
            "Birden fazla dolduran ve boşaltan musluk birlikte açıldığında dolduranların hızları toplanır, boşaltanların hızları çıkarılır. Net hız, havuzun ne kadar sürede dolacağını ya da boşalacağını belirler.",
            ornek(
                "Bir havuzu iki musluk $6$ ve $12$ saatte dolduruyor; dipteki bir musluk ise dolu havuzu $8$ saatte boşaltıyor. Üçü birlikte açılıyor.",
                "Boş havuzun kaç saatte dolacağını bulalım.",
                "Ortak payda $24$: $\\dfrac{4}{24}+\\dfrac{2}{24}-\\dfrac{3}{24}=\\dfrac{3}{24}=\\dfrac{1}{8}$.",
                "Net hız havuzun sekizde biri olduğu için havuz $8$ saatte dolar."),
            "Havuzu $24$ birim kabul etmek bu hesabı tam sayılara indirir: dolduranlar saatte $4$ ve $2$ birim ekler, boşaltan $3$ birim götürür; net $3$ birim ile $24$ birim $8$ saatte dolar.",
        ]},
        {"baslik": "Önce biri, sonra ikisi birlikte", "icerik": [
            "Musluklardan biri bir süre tek başına açık kalıp sonra diğeri açılırsa, önce tek başına doldurulan kısım hesaplanır, sonra kalan kısım iki musluğun birlikte hızıyla doldurulur.",
            ornek(
                "Bir havuzu birinci musluk $12$ saatte, ikinci musluk $6$ saatte dolduruyor. Birinci musluk $3$ saat tek başına açık kalıyor, sonra ikinci musluk da açılıyor.",
                "Havuzun toplam kaç saatte dolacağını bulalım.",
                "Birinci musluğun $3$ saatte doldurduğu kısım: $\\dfrac{3}{12}=\\dfrac{1}{4}$. Kalan: $\\dfrac{3}{4}$.",
                "Birlikte hız: $\\dfrac{1}{12}+\\dfrac{1}{6}=\\dfrac{3}{12}=\\dfrac{1}{4}$. Kalan kısım $\\dfrac{3}{4}:\\dfrac{1}{4}=3$ saatte dolar.",
                "Toplam süre: $3+3=6$ saat."),
        ]},
        {"baslik": "Sınavda işçi ve havuz problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) işçi ve havuz problemleri birlikte çalışma, bir kişinin süresini bulma, ara verme ve dolduran ile boşaltan musluk soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de bu soru türü sayısal bölümün klasik soruları arasındadır."),
            "Bu sorularda işin tamamını paydaların EKOK'u kadar birim almak, kesirlerle uğraşmadan tam sayılarla çalışmayı sağlar. Bulunan birlikte bitirme süresinin tek başına en kısa süreden küçük olup olmadığına bakmak da hızlı bir kontroldür.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Süreleri toplamak", "Hızları topla"],
                ["Sürelerin ortalamasını almak", "Hızların toplamının tersini al"],
                ["Üç kişide kısa formülü kullanmak", "Hızları tek tek topla"],
                ["Boşaltan musluğun hızını eklemek", "Boşaltan hız çıkarılır"],
                ["Kısmen dolu havuzu boş saymak", "Önce eksik kısmı bul"],
                ["\"$2$ kat hızlı\" ifadesini \"$2$ kat süre\" sanmak", "Süre yarıya iner"],
            ]),
            "Bu hataların hepsi, süre ile hızın ters orantılı olduğunu unutmaktan doğar. Her soruda önce süreleri hıza çevirmek, sonra hızlarla işlem yapmak ve en sonda yeniden süreye dönmek, hataları büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("İşçi problemleri nasıl çözülür?",
         "İşin tamamı 1 birim kabul edilir. Tek başına t günde bitiren kişinin bir günlük işi t de birdir. Birlikte çalışanların hızları toplanır ve birlikte bitirme süresi bu toplamın tersidir."),
        ("İki kişi birlikte bir işi kaç günde bitirir?",
         "Tek başına a ve b günde bitiriyorlarsa birlikte a çarpı b bölü a artı b günde bitirirler. 12 ve 24 günde bitirenler birlikte 8 günde bitirir."),
        ("Birlikte bitirme süresi neden en kısa süreden küçüktür?",
         "Çünkü en hızlı kişiye bir yardımcı eklenmiştir. Yardımcı ne kadar yavaş olursa olsun işe katkı yapar ve süreyi kısaltır."),
        ("Boşaltan musluk nasıl hesaba katılır?",
         "Boşaltan musluğun hızı dolduran muslukların hızından çıkarılır. Net hız pozitifse havuz dolar, negatifse boşalır."),
        ("Havuz kısmen doluysa ne yapılır?",
         "Önce doldurulması gereken kısım bulunur. Süre, bu kısmın net hıza bölünmesiyle hesaplanır."),
        ("İşçi sayısı ile süre arasında nasıl bir ilişki vardır?",
         "Aynı hızda çalışan işçilerde işçi sayısı ile süre ters orantılıdır. İşçi sayısı ile gün sayısının çarpımı sabittir."),
        ("Bir süre birlikte çalışıp sonra biri ayrılırsa ne yapılır?",
         "Önce birlikte yapılan iş hesaplanır ve 1 den çıkarılır. Kalan iş, çalışmaya devam eden kişinin hızına bölünerek süre bulunur."),
        ("Ondalıklı saat dakikaya nasıl çevrilir?",
         "Ondalık kısım 60 ile çarpılır. Örneğin 3,6 saat 3 saat ve 0,6 çarpı 60, yani 36 dakikadır."),
        ("İş sırasında işçi sayısı değişirse ne yapılır?",
         "İşin büyüklüğü işçi-gün olarak hesaplanır. Değişiklikten önce yapılan kısım çıkarılır ve kalan iş yeni işçi sayısına bölünür."),
        ("Ara vererek çalışan bir işçinin süresi nasıl bulunur?",
         "Önce gereken çalışma günü bulunur, sonra bloklar arasındaki dinlenme günleri eklenir. İş son çalışma gününde biterse ondan sonraki dinlenme günü sayılmaz."),
    ],
    "kontrol": [
        "İşin tamamını 1 birim kabul edip çalışma hızını yazabiliyorum.",
        "Birlikte çalışmada hızları toplayabiliyorum.",
        "İki kişi için kısa formülü kullanabiliyorum.",
        "Üç kişinin birlikte bitirme süresini bulabiliyorum.",
        "Birlikte süreden bir kişinin tek başına süresini bulabiliyorum.",
        "Ara verme ve sırayla çalışma sorularında kalan işi hesaplayabiliyorum.",
        "İşçi sayısı ile süre arasındaki ters orantıyı kullanabiliyorum.",
        "Farklı hızdaki işçilerin sürelerini bulabiliyorum.",
        "Dolduran ve boşaltan musluklarda net hızı hesaplayabiliyorum.",
        "Kısmen dolu havuzların dolma süresini bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["dogru-oranti-ve-ters-oranti", "kesir-problemleri-nasil-cozulur", "hareket-problemleri-konu-anlatimi-pdf"],
}
