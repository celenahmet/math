# scripts/yazilar/94_kombinasyon.py — Kombinasyon (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kombinasyon-konu-anlatimi-pdf",
    "baslik": "Kombinasyon Konu Anlatımı PDF",
    "aciklama": "Kombinasyon nedir? Permütasyonla farkı, simetri, gruplardan seçim, en az koşulu, Pascal üçgeni, alt kümeler, geometri ve gruplara ayırma soruları; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "sayma",
    "sinavlar": ["TYT", "AYT", "ALES", "KPSS"],
    "kapak": "kombinasyon-konu-anlatimi-pdf",
    "kapak_alt": "Kombinasyon: küp, küre ve piramitlerden oluşan grupları sıra gözetmeden seçen iki öğrenci",
    "ozet": "Kombinasyon, sıra önemli olmadan yapılan seçimleri saymaktır. Bir sınıftan temsilci grubu seçmek, bir menüden üç yemek seçmek ya da bir düzlemdeki noktalarla kaç üçgen çizilebileceğini bulmak kombinasyon sorularıdır. Bu yazıda kombinasyonun tanımını, permütasyonla farkını, simetri özelliğini, gruplardan seçimi, en az ve en çok koşullarını, belirli bir kişinin dahil ya da hariç olduğu seçimleri, Pascal üçgenini, alt küme sayısını, geometri ve tokalaşma sorularını ve gruplara ayırmayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kombinasyon nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için faktöriyeli ve permütasyonu biliyor olman yeterli.",
                "Temeller için <a href=\"/blog/faktoriyel-konu-anlatimi-pdf/\">Faktöriyel Konu Anlatımı PDF</a> ve <a href=\"/blog/permutasyon-konu-anlatimi-pdf/\">Permütasyon Konu Anlatımı PDF</a> yazılarına göz at."),
            "$n$ farklı nesneden, sıra gözetmeden $r$ tanesinin seçilmesine <strong>kombinasyon</strong> denir. Seçim sayısı $C(n, r)$ ile gösterilir ve şöyle hesaplanır:",
            "$$C(n, r)=\\dfrac{n!}{r! \\cdot (n-r)!}$$",
            "Kombinasyonda yalnızca hangi nesnelerin seçildiği önemlidir; hangi sırayla seçildikleri önemli değildir. A, B ve C den oluşan bir grup ile C, A ve B den oluşan grup aynı gruptur. Kapaktaki öğrencilerin yaptığı da budur: farklı biçimlerdeki nesnelerden gruplar oluşturulur ama grupların içindeki nesnelerin sırası önemsenmez.",
            hap("Kombinasyon, sıra gözetmeden seçimdir.",
                "$C(n, r)=\\dfrac{n!}{r! \\cdot (n-r)!}$"),
        ]},
        {"baslik": "Permütasyon ile kombinasyon arasındaki fark", "icerik": [
            "Aynı $r$ nesnenin kendi aralarında $r!$ farklı sıralaması vardır. Permütasyon bu sıralamaların hepsini ayrı sayar, kombinasyon ise hepsini tek bir seçim sayar. Bu yüzden kombinasyon sayısı, permütasyon sayısının $r!$ e bölümüdür:",
            "$$C(n, r)=\\dfrac{P(n, r)}{r!}$$",
            ornek(
                "Beş kişilik bir gruptan üç kişi seçilecek.",
                "Seçilenlerin görevleri farklıysa ve aynıysa kaç seçim olduğunu bulalım.",
                "Görevler farklıysa sıra önemlidir: $P(5, 3)=5 \\cdot 4 \\cdot 3=60$.",
                "Görevler aynıysa sıra önemsizdir: her üçlü $3!=6$ kez sayılmıştır; $60:6=10$.",
                "Formülle: $C(5, 3)=\\dfrac{5!}{3! \\cdot 2!}=10$. Görevler farklıyken bulunan $60$ dizilimin her biri, aynı üç kişinin farklı görev dağılımlarıdır."),
            tablo(["Soru", "Sıra önemli mi?", "Yöntem"], [
                ["Başkan, yardımcı ve sekreter seçmek", "Evet", "Permütasyon"],
                ["Üç kişilik komisyon seçmek", "Hayır", "Kombinasyon"],
                ["Yarışmada ilk üç derece", "Evet", "Permütasyon"],
                ["Menüden üç yemek seçmek", "Hayır", "Kombinasyon"],
            ]),
        ]},
        {"baslik": "Temel değerler ve simetri", "icerik": [
            "Bazı kombinasyon değerleri doğrudan bilinir ve hesabı kısaltır:",
            tablo(["İfade", "Değer", "Anlamı"], [
                ["$C(n, 0)$", "$1$", "Hiçbirini seçmemenin tek yolu"],
                ["$C(n, 1)$", "$n$", "Tek bir nesne seçmek"],
                ["$C(n, n)$", "$1$", "Hepsini seçmenin tek yolu"],
                ["$C(n, 2)$", "$\\dfrac{n \\cdot (n-1)}{2}$", "İkili seçimler"],
            ]),
            "Bu değerler formül açılmadan kullanılabilir ve birçok soruyu tek adımda çözer. Kombinasyonun en kullanışlı özelliği ise <strong>simetridir</strong>: $C(n, r)=C(n, n-r)$. $n$ nesneden $r$ tanesini seçmek, geride bırakılacak $n-r$ tanesini seçmekle aynı şeydir.",
            ornek(
                "$C(10, 8)$ ifadesi verilsin.",
                "Değerini simetriyle hesaplayalım.",
                "$C(10, 8)=C(10, 2)$.",
                "$C(10, 2)=\\dfrac{10 \\cdot 9}{2}=45$."),
        ]},
        {"baslik": "Basit seçim soruları", "icerik": [
            "Tek bir gruptan belirli sayıda eleman seçildiğinde formül doğrudan uygulanır. Büyük faktöriyelleri hesaplamak yerine pay ve payda sadeleştirilir.",
            ornek(
                "$12$ kişilik bir sınıftan $4$ kişilik bir komisyon seçilecek.",
                "Kaç farklı komisyon oluşturulabileceğini bulalım.",
                "$C(12, 4)=\\dfrac{12 \\cdot 11 \\cdot 10 \\cdot 9}{4 \\cdot 3 \\cdot 2 \\cdot 1}$.",
                "$\\dfrac{11880}{24}=495$ komisyon."),
            "Paydaya $r!$, paya ise $n$ den başlayarak $r$ tane azalan sayının çarpımı yazılır. Bu yazım, $C(n, r)=\\dfrac{P(n, r)}{r!}$ eşitliğinin doğrudan uygulamasıdır.",
        ]},
        {"baslik": "Gruplardan seçim", "icerik": [
            "Seçim birden fazla gruptan yapılıyorsa her gruptan yapılan seçim ayrı ayrı sayılır ve çarpma ilkesiyle çarpılır.",
            ornek(
                "Bir kulüpte $6$ kız ve $5$ erkek üye var. $2$ kız ve $3$ erkekten oluşan bir ekip seçilecek.",
                "Kaç farklı ekip seçilebileceğini bulalım.",
                "Kızlardan seçim: $C(6, 2)=15$. Erkeklerden seçim: $C(5, 3)=10$.",
                "Toplam: $15 \\cdot 10=150$ ekip."),
            dikkat(
                "Gruplardan yapılan seçimleri toplamak.",
                "Kız ve erkek seçimleri art arda yapılır ve her kız ikilisi her erkek üçlüsüyle eşleşir. Bu yüzden sonuçlar çarpılır; toplamak $25$ gibi yanlış bir sonuç verir."),
        ]},
        {"baslik": "En az ve en çok koşulları", "icerik": [
            "\"En az bir\" gibi koşullar iki yolla çözülür: durumlar tek tek toplanır ya da bütün seçimlerden koşulu sağlamayanlar çıkarılır. Tümleyen yolu çoğu zaman daha kısadır.",
            ornek(
                "$6$ kız ve $5$ erkek üyeden $4$ kişilik bir ekip seçilecek ve ekipte en az bir kız olacak.",
                "Kaç farklı ekip seçilebileceğini bulalım.",
                "Bütün seçimler: $C(11, 4)=330$.",
                "Hiç kız olmayan seçimler, yani yalnızca erkeklerden: $C(5, 4)=5$.",
                "En az bir kız olan ekipler: $330-5=325$."),
            "Aynı soru durumları toplayarak da çözülebilir: $1$, $2$, $3$ ya da $4$ kız seçilen durumlar ayrı ayrı hesaplanıp toplanır. $C(6,1)C(5,3)+C(6,2)C(5,2)+C(6,3)C(5,1)+C(6,4)=60+150+100+15=325$ bulunur ve sonuç aynıdır.",
        ]},
        {"baslik": "En çok koşulu", "icerik": [
            "\"En çok\" koşullarında izin verilen durumlar genellikle azdır; bu yüzden durumlar tek tek sayılıp toplanır.",
            ornek(
                "$6$ kız ve $5$ erkek üyeden $4$ kişilik bir ekip seçilecek ve ekipte en çok $2$ kız olacak.",
                "Kaç farklı ekip seçilebileceğini bulalım.",
                "Hiç kız yok: $C(5, 4)=5$. Bir kız: $C(6, 1) \\cdot C(5, 3)=6 \\cdot 10=60$.",
                "İki kız: $C(6, 2) \\cdot C(5, 2)=15 \\cdot 10=150$.",
                "Toplam: $5+60+150=215$ ekip."),
        ]},
        {"baslik": "Birlikte olamayan kişiler", "icerik": [
            "İki kişinin aynı ekipte olmaması isteniyorsa bütün seçimlerden ikisinin birlikte bulunduğu seçimler çıkarılır.",
            ornek(
                "A ve B nin de bulunduğu $10$ kişiden $4$ kişilik bir ekip seçilecek ve A ile B aynı ekipte olmayacak.",
                "Kaç farklı ekip seçilebileceğini bulalım.",
                "Bütün seçimler: $C(10, 4)=210$.",
                "A ile B nin birlikte olduğu seçimler: ikisi seçilmiş sayılır, kalan $2$ kişi $8$ kişiden seçilir: $C(8, 2)=28$.",
                "A ile B nin birlikte olmadığı seçimler: $210-28=182$."),
        ]},
        {"baslik": "Belirli bir kişinin dahil ya da hariç olması", "icerik": [
            "Belirli bir kişinin seçilmesi zorunluysa o kişi önceden seçilmiş sayılır ve kalan yerler kalan kişilerden seçilir. Kişinin seçilmemesi isteniyorsa o kişi gruptan çıkarılır.",
            ornek(
                "A nın da bulunduğu $10$ kişiden $4$ kişilik bir ekip seçilecek.",
                "A nın ekipte olduğu ve olmadığı seçimleri sayalım.",
                "A kesin ekipte: kalan $3$ kişi kalan $9$ kişiden seçilir: $C(9, 3)=84$.",
                "A ekipte değil: $4$ kişi kalan $9$ kişiden seçilir: $C(9, 4)=126$.",
                "Kontrol: $84+126=210=C(10, 4)$."),
            "Son satır, kombinasyonun temel bir özelliğini gösterir: bütün seçimler, belirli bir kişiyi içerenler ve içermeyenler olarak iki ayrık gruba ayrılır. Bu gözlem Pascal üçgeninin de temelidir.",
        ]},
        {"baslik": "Pascal üçgeni", "icerik": [
            "Önceki bölümdeki gözlem genel olarak şöyle yazılır: $C(n, r)=C(n-1, r-1)+C(n-1, r)$. Bu eşitliğe Pascal özdeşliği denir. Kombinasyon değerleri bir üçgen biçiminde dizildiğinde her sayı, üstündeki iki sayının toplamıdır.",
            tablo(["$n$", "$C(n, 0), C(n, 1), \\ldots, C(n, n)$"], [
                ["$0$", "$1$"],
                ["$1$", "$1$, $1$"],
                ["$2$", "$1$, $2$, $1$"],
                ["$3$", "$1$, $3$, $3$, $1$"],
                ["$4$", "$1$, $4$, $6$, $4$, $1$"],
                ["$5$", "$1$, $5$, $10$, $10$, $5$, $1$"],
            ]),
            "Üçgendeki her satır simetriktir; bu, $C(n, r)=C(n, n-r)$ özelliğinin görünümüdür. Her satırın sayılarının toplamı ise $2$ nin bir kuvvetidir: beşinci satırın toplamı $1+5+10+10+5+1=32=2^5$ tir.",
        ]},
        {"baslik": "Alt küme sayısı", "icerik": [
            "$n$ elemanlı bir kümenin bütün alt kümelerinin sayısı $2^n$ dir. Her eleman için iki seçenek vardır: alt kümeye girer ya da girmez. Aynı sayı kombinasyonlarla da bulunur: $0$, $1$, $2$ ve $n$ ye kadar elemanlı alt kümelerin sayıları toplanır.",
            ornek(
                "$4$ elemanlı bir küme verilsin.",
                "Alt kümelerin sayısını iki yolla bulalım.",
                "Her eleman için $2$ seçenek: $2^4=16$.",
                "Eleman sayısına göre: $C(4,0)+C(4,1)+C(4,2)+C(4,3)+C(4,4)=1+4+6+4+1=16$."),
            "Kümelerin ayrıntısı <a href=\"/blog/kumeler-konu-anlatimi-pdf/\">Kümeler Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Geometri soruları", "icerik": [
            "Düzlemde herhangi üçü aynı doğru üzerinde olmayan noktalarla çizilebilecek doğru ve üçgenlerin sayısı kombinasyonla bulunur. Bir doğru iki noktayla, bir üçgen üç noktayla belirlenir ve noktaların sırası önemli değildir.",
            ornek(
                "Düzlemde herhangi üçü doğrusal olmayan $8$ nokta verilsin.",
                "Bu noktalarla kaç doğru ve kaç üçgen çizilebileceğini bulalım.",
                "Doğru: $C(8, 2)=28$.",
                "Üçgen: $C(8, 3)=56$."),
            ornek(
                "Altıgenin köşegenleri verilsin.",
                "Bir altıgenin kaç köşegeni olduğunu bulalım.",
                "Altı köşeden seçilen her ikili bir kenar ya da bir köşegen belirler: $C(6, 2)=15$.",
                "Bunların $6$ sı kenardır; köşegen sayısı $15-6=9$ dur."),
        ]},
        {"baslik": "Paralel doğrularla oluşan şekiller", "icerik": [
            "Birbirini kesen iki paralel doğru ailesi bir ızgara oluşturur. Bu ızgaradaki her paralelkenar, birinci aileden iki doğru ile ikinci aileden iki doğrunun seçilmesiyle belirlenir.",
            ornek(
                "Düzlemde birbirine paralel $5$ doğru ve bunları kesen, birbirine paralel $4$ doğru var.",
                "Bu doğruların oluşturduğu paralelkenar sayısını bulalım.",
                "Birinci aileden iki doğru: $C(5, 2)=10$. İkinci aileden iki doğru: $C(4, 2)=6$.",
                "Paralelkenar sayısı: $10 \\cdot 6=60$. Her paralelkenarın dört kenarı bu dört doğrunun üzerinde olduğu için başka bir paralelkenar sayılmamış kalmaz."),
        ]},
        {"baslik": "Binom açılımına bakış", "icerik": [
            "Pascal üçgeninin satırları, $(a+b)^n$ ifadesi açıldığında terimlerin katsayılarını verir. Bu yüzden kombinasyon değerlerine <strong>binom katsayıları</strong> da denir.",
            ornek(
                "$(a+b)^4$ ifadesi verilsin.",
                "Açılımın katsayılarını Pascal üçgeninden okuyalım.",
                "Dördüncü satır: $1$, $4$, $6$, $4$, $1$.",
                "$(a+b)^4=a^4+4a^3b+6a^2b^2+4ab^3+b^4$."),
            "Katsayıların kombinasyon olmasının nedeni saymadır: $(a+b)^4$ çarpımı açılırken $a^2b^2$ terimi, dört parantezden ikisinde $b$ nin seçildiği her durumda bir kez oluşur ve bu durumların sayısı $C(4, 2)=6$ dır. İki terimli bir ifadenin karesi için bilinen $(a+b)^2=a^2+2ab+b^2$ özdeşliği de bu kuralın en küçük örneğidir.",
        ]},
        {"baslik": "Tokalaşma ve maç soruları", "icerik": [
            "Bir gruptaki herkesin birbiriyle birer kez tokalaşması ya da bir ligdeki her takımın diğerleriyle birer kez karşılaşması, gruptan ikili seçmekle aynıdır.",
            ornek(
                "$10$ kişilik bir toplantıda herkes birbiriyle birer kez tokalaşıyor.",
                "Toplam tokalaşma sayısını bulalım.",
                "Her tokalaşma iki kişilik bir seçimdir: $C(10, 2)=45$.",
                "Başka bir yol: her kişi $9$ kişiyle tokalaşır, $10 \\cdot 9=90$ bulunur; ama her tokalaşma iki kez sayılmıştır: $90:2=45$."),
            "Aynı ligde takımlar birbiriyle hem kendi sahasında hem deplasmanda oynuyorsa sıra önemli olur ve maç sayısı $P(n, 2)=n \\cdot (n-1)$ olur.",
        ]},
        {"baslik": "Ekip ve kaptan seçmek", "icerik": [
            "Bir ekip seçilip ekibin içinden bir de kaptan belirleniyorsa iş iki adımda yapılır: önce ekip kombinasyonla seçilir, sonra ekibin üyelerinden biri kaptan olarak seçilir. İki adımın seçenekleri çarpılır.",
            ornek(
                "$10$ kişiden $5$ kişilik bir ekip seçilecek ve ekibin içinden bir kaptan belirlenecek.",
                "Kaç farklı seçim yapılabileceğini bulalım.",
                "Ekip: $C(10, 5)=252$. Kaptan: ekibin $5$ üyesinden biri, $5$ seçenek.",
                "Toplam: $252 \\cdot 5=1260$."),
            "Aynı sonuca önce kaptanı seçerek de ulaşılır: kaptan $10$ kişiden biri, kalan $4$ ekip üyesi ise kalan $9$ kişiden seçilir: $10 \\cdot C(9, 4)=10 \\cdot 126=1260$. İki yolun aynı sonucu vermesi, kurulumun doğru olduğunu gösterir.",
        ]},
        {"baslik": "Seçip dizmek", "icerik": [
            "Bazı sorularda önce seçim yapılır, sonra seçilenler dizilir. Bu durumda kombinasyon ile seçilenlerin dizilim sayısı çarpılır.",
            ornek(
                "$7$ farklı kitaptan $3$ tanesi seçilip bir rafa dizilecek.",
                "Kaç farklı dizilim olduğunu bulalım.",
                "Seçim: $C(7, 3)=35$. Dizilim: $3!=6$.",
                "Toplam: $35 \\cdot 6=210$. Bu sayı $P(7, 3)=7 \\cdot 6 \\cdot 5$ ile aynıdır."),
            "Seçip dizmek, doğrudan permütasyondur. Ama seçimde ek koşullar varsa, örneğin belirli bir kitabın mutlaka seçilmesi, önce kombinasyonla koşullu seçim yapmak ve sonra dizmek daha kolaydır.",
        ]},
        {"baslik": "Gruplara ayırma", "icerik": [
            "Bir topluluğu gruplara ayırırken grupların adının ya da görevinin olup olmadığı sonucu değiştirir. Gruplar birbirinden ayırt edilemiyorsa, aynı büyüklükteki grupların kendi aralarındaki sıralama sayısına bölünür.",
            ornek(
                "$6$ kişi ikişer kişilik $3$ gruba ayrılacak.",
                "Grupların adı yokken ve gruplar A, B ve C takımları olarak adlandırıldığında kaç ayrım olduğunu bulalım.",
                "Adlandırılmış takımlar: $C(6, 2) \\cdot C(4, 2) \\cdot C(2, 2)=15 \\cdot 6 \\cdot 1=90$.",
                "Adsız gruplar: aynı üç grup $3!=6$ farklı sırada seçilmiş olur; $90:6=15$."),
        ]},
        {"baslik": "Kombinasyon denklemleri", "icerik": [
            "Bilinmeyen kombinasyonun içindeyse formül açılarak cebirsel bir denkleme dönüştürülür. Simetri özelliği de denklemleri çözmekte kullanılır.",
            ornek(
                "$C(n, 2)=28$ denklemi verilsin.",
                "$n$ yi bulalım.",
                "$\\dfrac{n \\cdot (n-1)}{2}=28$, yani $n \\cdot (n-1)=56$.",
                "Ardışık iki sayının çarpımı $56$ ise sayılar $8$ ve $7$ dir: $n=8$."),
            ornek(
                "$C(n, 3)=C(n, 5)$ eşitliği verilsin.",
                "$n$ yi bulalım.",
                "Simetriden $C(n, 3)=C(n, n-3)$. Eşitliğin sağlanması için $n-3=5$ olmalıdır.",
                "$n=8$. Kontrol: $C(8, 3)=C(8, 5)=56$."),
        ]},
        {"baslik": "Sınavda kombinasyon", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kombinasyon gruplardan seçim, en az koşulu, geometri ve tokalaşma soruları biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) Pascal üçgeni, binom açılımı ve olasılık hesaplarıyla birlikte kullanılır; <strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de sayma sorularının temelidir."),
            "Bir seçim sorusunda önce sıranın önemli olup olmadığına karar ver. Sonra seçimin tek gruptan mı birden fazla gruptan mı yapıldığına bak ve \"en az\" gibi bir koşul varsa tümleyen yolunu dene. Bu üç karar, soruların neredeyse tamamını çözer.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Sırasız seçimi permütasyonla saymak", "Kombinasyon kullan"],
                ["Gruplardan seçimleri toplamak", "Art arda seçimler çarpılır"],
                ["En az koşulunda yalnızca bir durumu saymak", "Tümleyen ya da bütün durumlar"],
                ["Adsız grupları adlı gibi saymak", "Aynı büyüklükteki gruplar için böl"],
                ["Doğrusal üç noktayla üçgen saymak", "Doğrusal noktalar üçgen oluşturmaz"],
                ["Köşegen sayısında kenarları çıkarmamak", "İkililerden kenarları çıkar"],
            ]),
            "Bu hataların çoğu, sıranın ve grup adlarının önemini gözden kaçırmaktan doğar. Küçük sayılarla, örneğin dört nesneyle, bütün seçimleri tek tek yazıp formülle karşılaştırmak, hangi yöntemin doğru olduğunu hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Kombinasyon nedir?",
         "n farklı nesneden sıra gözetmeden r tanesini seçme sayısıdır. n faktöriyelin, r faktöriyel ile n eksi r faktöriyelin çarpımına bölümüyle hesaplanır."),
        ("Permütasyon ile kombinasyon arasındaki fark nedir?",
         "Permütasyonda sıra önemlidir, kombinasyonda önemli değildir. Kombinasyon sayısı, permütasyon sayısının seçilen nesne sayısının faktöriyeline bölümüdür."),
        ("Kombinasyonda simetri ne demektir?",
         "n nesneden r tanesini seçmek, geride kalacak n eksi r tanesini seçmekle aynıdır. Bu yüzden C(n, r) ile C(n, n eksi r) eşittir."),
        ("En az bir koşulu nasıl çözülür?",
         "Bütün seçimlerden koşulu hiç sağlamayan seçimler çıkarılır. Bu tümleyen yolu genellikle durumları tek tek toplamaktan daha kısadır."),
        ("n noktayla kaç üçgen çizilir?",
         "Herhangi üçü doğrusal değilse, noktalardan üçlü seçme sayısı kadar üçgen çizilir. 8 nokta için bu sayı 56 dır."),
        ("Pascal üçgeni nedir?",
         "Kombinasyon değerlerinin satır satır dizildiği üçgendir. Her sayı üstündeki iki sayının toplamıdır ve her satırın toplamı 2 nin bir kuvvetidir."),
        ("İki kişinin aynı grupta olmaması nasıl sayılır?",
         "Bütün seçimlerden ikisinin birlikte bulunduğu seçimler çıkarılır. İkisinin birlikte olduğu seçimler, bu iki kişi seçilmiş sayılarak kalan yerler için yapılan seçimlerdir."),
    ],
    "kontrol": [
        "Kombinasyonu sırasız seçim olarak açıklayabiliyorum.",
        "Kombinasyon formülünü uygulayabiliyorum.",
        "Permütasyon ile kombinasyon arasındaki ilişkiyi kullanabiliyorum.",
        "Simetri özelliğiyle hesabı kısaltabiliyorum.",
        "Gruplardan yapılan seçimleri çarpma ilkesiyle sayabiliyorum.",
        "En az koşulunu tümleyen yoluyla çözebiliyorum.",
        "Belirli bir kişinin dahil ya da hariç olduğu seçimleri sayabiliyorum.",
        "Pascal üçgenini oluşturup özelliklerini açıklayabiliyorum.",
        "Noktalarla çizilebilecek doğru, üçgen ve köşegen sayısını bulabiliyorum.",
        "Adlı ve adsız gruplara ayırma sorularını çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["permutasyon-konu-anlatimi-pdf", "faktoriyel-konu-anlatimi-pdf", "olasilik-konu-anlatimi-pdf"],
}
