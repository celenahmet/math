# scripts/yazilar/55_irrasyonel_gercek.py — Irrasyonel ve Gercek Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "irrasyonel-sayilar-ve-gercek-sayilar",
    "baslik": "İrrasyonel Sayılar ve Gerçek Sayılar",
    "aciklama": "İrrasyonel sayı nedir, nasıl tanınır? Karekök tahmini, kök dışına çıkarma, sıralama, işlemler, gerçek sayılar ve aralık gösterimi; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "irrasyonel-sayilar-ve-gercek-sayilar",
    "kapak_alt": "İrrasyonel sayılar ve gerçek sayılar: karenin köşegen uzunluğunu pergelle sayı doğrusuna aktaran öğrenci",
    "ozet": "Kenarı $1$ birim olan bir karenin köşegeni ölçülebilir bir uzunluktur, ama hiçbir kesirle tam olarak yazılamaz. Bu tür sayılara irrasyonel sayı denir ve rasyonel sayılarla birlikte sayı doğrusunu boşluksuz dolduran gerçek sayıları oluştururlar. Bu yazıda irrasyonel sayıları tanımlıyor, hangi kareköklerin irrasyonel olduğunu, kök dışına çıkarmayı, yaklaşık değer bulmayı, sıralamayı ve işlemleri ele alıyor, gerçek sayılar ve aralık gösterimiyle bitiriyoruz.",
    "bolumler": [
        {"baslik": "İrrasyonel sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için rasyonel sayıları, kareköke giriş bilgisini ve tam kare sayıları ($1, 4, 9, 16, \\ldots$) biliyor olman yeterli.",
                "Rasyonel sayılar için <a href=\"/blog/rasyonel-sayilar-konu-anlatimi-pdf/\">Rasyonel Sayılar Konu Anlatımı PDF</a> yazısına göz at."),
            "İki tam sayının bölümü olarak, yani $\\dfrac{a}{b}$ biçiminde yazılamayan gerçek sayılara <strong>irrasyonel sayı</strong> denir. \"İrrasyonel\" kelimesi \"oran olarak yazılamayan\" anlamına gelir; burada oran, iki tam sayının bölümüdür.",
            "İrrasyonel sayıları ondalık gösterimlerinden de tanıyabilirsin. Rasyonel sayıların ondalık gösterimi ya biter ya da bir basamak grubu düzenli olarak tekrar eder. İrrasyonel sayıların ondalık gösterimi ise sonsuza kadar gider ve hiçbir grup düzenli olarak tekrar etmez.",
            "<ul><li>$\\sqrt{2}=1.41421356\\ldots$</li><li>$\\sqrt{3}=1.73205080\\ldots$</li><li>$\\pi=3.14159265\\ldots$</li><li>$e=2.71828182\\ldots$ (doğal logaritmanın tabanı; ileride üstel fonksiyonlarda karşına çıkacak)</li></ul>",
            hap("İrrasyonel sayı, $\\dfrac{a}{b}$ biçiminde yazılamayan gerçek sayıdır.",
                "Ondalık gösterimi sonsuzdur ve devirli değildir."),
            dikkat(
                "\"Ondalık gösterimi sonsuz\" demek tek başına irrasyonellik için yetmez.",
                "$\\dfrac{1}{3}=0.333\\ldots$ de sonsuzdur ama devirlidir; bu yüzden rasyoneldir. İrrasyonellikte sonsuzluk ile birlikte devirsizlik gerekir."),
        ]},
        {"baslik": "Hangi karekök irrasyoneldir?", "icerik": [
            "Karekök gördüğün her sayı irrasyonel değildir. Kural şudur: $n$ bir pozitif tam sayı ise $\\sqrt{n}$, ancak $n$ bir tam kare değilse irrasyoneldir. Tam kareyse karekök bir doğal sayıdır.",
            "<ul><li>$\\sqrt{4}=2$, $\\sqrt{49}=7$: tam kare, rasyonel.</li><li>$\\sqrt{2}$, $\\sqrt{5}$, $\\sqrt{12}$: tam kare değil, irrasyonel.</li><li>$\\sqrt{\\dfrac{9}{4}}=\\dfrac{3}{2}$: pay ve payda tam kare, rasyonel.</li><li>$\\sqrt{0.25}=0.5$: $0.25=\\dfrac{1}{4}$ olduğu için rasyonel.</li></ul>",
            "Kesir ve ondalık sayılarda önce sayıyı en sade kesre çevir, sonra pay ile paydanın tam kare olup olmadığına bak. Aynı kural küp kökte de geçerlidir, ama bu kez tam küp olup olmadığına bakılır: $\\sqrt[3]{8}=2$ rasyoneldir, $\\sqrt[3]{2}$ irrasyoneldir.",
            hap("Pozitif tam sayının karekökü, sayı tam kare <strong>değilse</strong> irrasyoneldir.",
                "Kesirde önce sadeleştir; pay ve payda tam kareyse karekök rasyoneldir."),
            ornek(
                "$\\sqrt{16}$, $\\sqrt{18}$, $\\sqrt{\\dfrac{25}{36}}$, $\\sqrt{0.4}$ sayıları verilsin.",
                "Bunlardan hangileri rasyoneldir?",
                "$\\sqrt{16}=4$: rasyonel.",
                "$\\sqrt{18}$: $18$ tam kare değil, irrasyonel.",
                "$\\sqrt{\\dfrac{25}{36}}=\\dfrac{5}{6}$: rasyonel.",
                "$\\sqrt{0.4}$: $0.4=\\dfrac{2}{5}$ ve ne $2$ ne $5$ tam kare. İrrasyonel. Dikkat: $\\sqrt{0.04}=0.2$ olurdu."),
        ]},
        {"baslik": "Kök 2 neden irrasyoneldir?", "icerik": [
            "Bir sayının kesirle yazılamadığını göstermek için \"yazılabilseydi ne olurdu?\" sorusunu sorarız ve bir çelişkiye ulaşırız. Bu yönteme <strong>olmayana ergi</strong> denir.",
            "<ol>"
            "<li>$\\sqrt{2}$ nin $\\dfrac{p}{q}$ biçiminde, <strong>en sade</strong> hâlde yazılabildiğini varsayalım. En sade demek, $p$ ile $q$ nun ortak böleni olmaması demektir.</li>"
            "<li>İki tarafın karesini alalım: $2=\\dfrac{p^2}{q^2}$, yani $p^2=2q^2$. Demek ki $p^2$ çifttir.</li>"
            "<li>Tek sayının karesi tek olduğu için $p$ de çift olmalıdır. $p=2k$ yazalım.</li>"
            "<li>Yerine koyalım: $4k^2=2q^2$, yani $q^2=2k^2$. Aynı gerekçeyle $q$ da çifttir.</li>"
            "<li>$p$ ile $q$ nun ikisi de çift çıktı; $2$ ortak bölendir. Bu, kesrin en sade olduğu varsayımıyla çelişir.</li>"
            "</ol>",
            "Varsayım çelişkiye götürdüğü için yanlıştır: $\\sqrt{2}$ hiçbir kesirle yazılamaz, irrasyoneldir. Aynı yol, tam kare olmayan her doğal sayının karekökü için uyarlanabilir.",
            "Bu ispatı ezberlemen gerekmez, ama kuralın nereden geldiğini gösterir. \"Neden?\" sorusunun cevabını bilen öğrenci, kök içeren ifadelerde kural ezberlemeden karar verebilir.",
            hap("A4 kâğıdının kenarları $210$ ve $297$ milimetredir; uzun kenarın kısa kenara oranı yaklaşık $\\sqrt{2} \\approx 1.414$ olur.", "Bu yüzden kâğıt ortadan ikiye katlanınca oluşan A5 kâğıdı da aynı orana sahiptir.", gunluk=True),
        ]},
        {"baslik": "Pi sayısı", "icerik": [
            "Bir çemberin çevresinin çapına oranı, çember ne kadar büyük ya da küçük olursa olsun aynıdır. Bu sabit orana $\\pi$ denir: $\\pi=3.14159265\\ldots$",
            "$\\pi$ irrasyoneldir; hiçbir kesre tam olarak eşit değildir. Günlük hesaplarda kullanılan $3.14$ ve $\\dfrac{22}{7}$ yalnızca yaklaşık değerlerdir. Sorular bu değerlerden birini kullanmanı isterse bunu açıkça belirtir: \"$\\pi$ yi $3$ alınız\" gibi.",
            "$\\pi$ nin irrasyonel olduğu 18. yüzyılda kanıtlanmıştır. Bu yüzden basamakları ne kadar uzun hesaplanırsa hesaplansın, düzenli olarak tekrar eden bir basamak grubu çıkmaz. Hesap makinesinde gördüğün değer her zaman kesilmiş bir yaklaşımdır.",
            dikkat(
                "$\\pi=\\dfrac{22}{7}$ yazmak yanlıştır; $\\dfrac{22}{7}$ bir rasyonel sayıdır.",
                "$\\dfrac{22}{7}=3.142857\\ldots$ ve $\\pi=3.141592\\ldots$ İkisi yalnızca üçüncü ondalık basamakta ayrılır; bu yüzden $3.14<\\pi<\\dfrac{22}{7}$ dir."),
        ]},
        {"baslik": "Kök dışına çıkarma ve kök içine alma", "icerik": [
            "Karekökler çarpmaya dağılır: $a$ ve $b$ negatif değilse $\\sqrt{a \\cdot b}=\\sqrt{a} \\cdot \\sqrt{b}$ dir. Kök içindeki sayıyı bir tam kare ile başka bir sayının çarpımı olarak yazarsan tam kareyi kök dışına çıkarabilirsin:",
            "$$\\sqrt{12}=\\sqrt{4 \\cdot 3}=2\\sqrt{3}$$",
            "Tersine, kök dışındaki pozitif bir sayı karesi alınarak köke sokulabilir: $3\\sqrt{2}=\\sqrt{9 \\cdot 2}=\\sqrt{18}$. Bu işlem özellikle sıralama sorularında işe yarar.",
            ornek(
                "$\\sqrt{50}$, $\\sqrt{72}$ ve $\\sqrt{8}+\\sqrt{18}$ ifadeleri verilsin.",
                "Hepsini en sade biçimde yazalım.",
                "$\\sqrt{50}=\\sqrt{25 \\cdot 2}=5\\sqrt{2}$.",
                "$\\sqrt{72}=\\sqrt{36 \\cdot 2}=6\\sqrt{2}$.",
                "$\\sqrt{8}+\\sqrt{18}=2\\sqrt{2}+3\\sqrt{2}=5\\sqrt{2}$. Kök içleri aynı olunca katsayılar toplanır."),
            hap("Kök dışına çıkarırken kök içindeki <strong>en büyük tam kare</strong> çarpanı ayır.",
                "Kök içleri aynı olan terimler toplanır: $a\\sqrt{c}+b\\sqrt{c}=(a+b)\\sqrt{c}$."),
            dikkat(
                "Karekök toplamaya dağılmaz: $\\sqrt{a+b} \\neq \\sqrt{a}+\\sqrt{b}$.",
                "Örneğin $\\sqrt{9+16}=\\sqrt{25}=5$ tir, ama $\\sqrt{9}+\\sqrt{16}=3+4=7$ dir."),
        ]},
        {"baslik": "İrrasyonel sayılarla işlemler", "icerik": [
            "Rasyonel ve irrasyonel sayılar birlikte işleme girdiğinde sonuç hakkında kesin kurallar vardır:",
            "<ul>"
            "<li><strong>Rasyonel + irrasyonel = irrasyonel.</strong> $2+\\sqrt{3}$ irrasyoneldir. Sebebi: sonuç rasyonel olsaydı, rasyonel olan $2$ yi çıkarınca $\\sqrt{3}$ de rasyonel çıkardı.</li>"
            "<li><strong>Sıfırdan farklı rasyonel · irrasyonel = irrasyonel.</strong> $5\\sqrt{2}$ irrasyoneldir. Rasyonel çarpan sıfırsa sonuç $0$ olur: $0 \\cdot \\sqrt{2}=0$.</li>"
            "</ul>",
            "İki irrasyonel sayı işleme girdiğinde ise genel bir kural yoktur; sonuç rasyonel de çıkabilir irrasyonel de:",
            "<ul><li>$\\sqrt{2}+(3-\\sqrt{2})=3$: rasyonel.</li><li>$\\sqrt{2} \\cdot \\sqrt{8}=\\sqrt{16}=4$: rasyonel.</li><li>$\\dfrac{\\sqrt{12}}{\\sqrt{3}}=\\sqrt{4}=2$: rasyonel.</li><li>$\\sqrt{2}+\\sqrt{3}$ ve $\\sqrt{2} \\cdot \\sqrt{3}=\\sqrt{6}$: irrasyonel.</li></ul>",
            hap("Rasyonel ile irrasyonelin toplamı irrasyoneldir; sıfırdan farklı rasyonel ile irrasyonelin çarpımı irrasyoneldir.",
                "İki irrasyonelin toplamı ya da çarpımı için genel kural yoktur."),
            ornek(
                "$a$ bir rasyonel sayı ve $a+\\sqrt{5}$ ile $a \\cdot \\sqrt{5}$ ifadeleri verilsin.",
                "Bu ifadeler hangi durumda rasyonel olur?",
                "$a+\\sqrt{5}$: rasyonel ile irrasyonelin toplamı her zaman irrasyoneldir. Hiçbir $a$ için rasyonel olmaz.",
                "$a \\cdot \\sqrt{5}$: $a \\neq 0$ ise irrasyoneldir. Yalnızca $a=0$ için sonuç $0$ olur ve rasyoneldir."),
        ]},
        {"baslik": "Paydayı rasyonel yapma", "icerik": [
            "Paydasında kök bulunan bir kesri, değerini değiştirmeden paydası rasyonel olan bir kesre çevirmek işi kolaylaştırabilir. Buna <strong>paydayı rasyonel yapma</strong> denir. Yöntem, kesri uygun bir ifadeyle genişletmektir.",
            "<ul><li>Paydada yalnız $\\sqrt{a}$ varsa pay ve payda $\\sqrt{a}$ ile çarpılır: $\\dfrac{1}{\\sqrt{2}}=\\dfrac{\\sqrt{2}}{2}$.</li>"
            "<li>Paydada $\\sqrt{a}-b$ gibi iki terim varsa <strong>eşleniği</strong> olan $\\sqrt{a}+b$ ile çarpılır. İki kare farkı özdeşliği, $(x-y)(x+y)=x^2-y^2$, kökü paydadan kaldırır.</li></ul>",
            ornek(
                "$\\dfrac{2}{\\sqrt{3}-1}$ ifadesi verilsin.",
                "Paydasını rasyonel yapalım.",
                "Paydanın eşleniği $\\sqrt{3}+1$ dir. Pay ve paydayı bununla çarpalım.",
                "Payda: $(\\sqrt{3}-1)(\\sqrt{3}+1)=3-1=2$.",
                "Pay: $2(\\sqrt{3}+1)$. Sonuç: $\\dfrac{2(\\sqrt{3}+1)}{2}=\\sqrt{3}+1$."),
            hap("Paydada $\\sqrt{a}$ varsa $\\sqrt{a}$ ile, $\\sqrt{a} \\pm b$ varsa eşleniğiyle genişlet.",
                "$(\\sqrt{a}-b)(\\sqrt{a}+b)=a-b^2$."),
        ]},
        {"baslik": "Karekökün yaklaşık değeri", "icerik": [
            "Tam kare olmayan bir sayının karekökünü yaklaşık bulmak için sayıyı iki ardışık tam karenin arasına yerleştirirsin. $16<20<25$ olduğundan $4<\\sqrt{20}<5$ tir.",
            "Daha hassas bir aralık için ondalıklı sayıların karelerine bakılır: $4.4^2=19.36$ ve $4.5^2=20.25$ olduğundan $4.4<\\sqrt{20}<4.5$ tir. Gerçek değer $4.472\\ldots$ dir.",
            ornek(
                "$\\sqrt{40}$ sayısı verilsin.",
                "Bu sayıya en yakın tam sayı kaçtır?",
                "$36<40<49$ olduğundan $6<\\sqrt{40}<7$.",
                "Hangisine yakın olduğunu görmek için ortadaki değere bakalım: $6.5^2=42.25$. $40<42.25$ olduğundan $\\sqrt{40}<6.5$ tir.",
                "En yakın tam sayı $6$ dır. Gerçek değer $6.324\\ldots$ tür."),
            hap("$a^2<n<b^2$ ise $a<\\sqrt{n}<b$.",
                "Hangi tam sayıya yakın olduğunu bulmak için ortadaki değerin karesiyle karşılaştır."),
            dikkat(
                "Ardışık iki tam karenin tam ortasındaki sayının karekökü, iki tam sayının tam ortasında değildir.",
                "$\\sqrt{20}$, $16$ ile $25$ in ortasına yakın bir sayının kökü olduğu hâlde $4.5$ ten küçüktür: $4.47\\ldots$ Bu yüzden karşılaştırmayı her zaman karelerle yap."),
        ]},
        {"baslik": "İrrasyonel sayıları sıralama", "icerik": [
            "Kök içeren sayıları sıralamanın en güvenli yolu hepsini aynı biçime getirmektir. Katsayıyı köke sokarak hepsini $\\sqrt{\\ }$ içine alırsın; kök içi büyük olan sayı büyüktür.",
            ornek(
                "$4$, $3\\sqrt{2}$ ve $2\\sqrt{5}$ sayıları verilsin.",
                "Bu sayıları küçükten büyüğe sıralayalım.",
                "Hepsini köke sokalım: $4=\\sqrt{16}$, $3\\sqrt{2}=\\sqrt{18}$, $2\\sqrt{5}=\\sqrt{20}$.",
                "Kök içlerini karşılaştıralım: $16<18<20$.",
                "Sıralama: $4<3\\sqrt{2}<2\\sqrt{5}$."),
            "Farklı türden sayılar karşılaştırılırken ondalık yaklaşık değerler de kullanılabilir. $\\sqrt{10}=3.162\\ldots$, $\\pi=3.141\\ldots$ ve $\\dfrac{22}{7}=3.142\\ldots$ olduğundan sıralama $\\pi<\\dfrac{22}{7}<\\sqrt{10}$ dur.",
            hap("Kökleri sıralamak için katsayıları köke sok, sonra kök içlerini karşılaştır.",
                "Pozitif sayılarda $\\sqrt{a}<\\sqrt{b} \\Leftrightarrow a<b$."),
        ]},
        {"baslik": "Gerçek sayılar", "icerik": [
            "Rasyonel ve irrasyonel sayıların birleşimine <strong>gerçek sayılar</strong> denir ve $\\mathbb{R}$ ile gösterilir. Bir gerçek sayı ya rasyoneldir ya irrasyoneldir; ikisi birden olamaz.",
            "Gerçek sayıların en önemli özelliği sayı doğrusunu <strong>boşluksuz</strong> doldurmalarıdır. Rasyonel sayılar ne kadar sık olursa olsun, aralarında boşluklar kalır: $\\sqrt{2}$ nin yeri rasyonel sayılarda boştur. İrrasyonel sayılar bu boşlukları doldurur.",
            "Bir irrasyonel sayının sayı doğrusundaki yeri geometriyle bulunabilir. Kenarı $1$ birim olan bir kare çizersen, Pisagor bağıntısına göre köşegeninin uzunluğu $\\sqrt{1^2+1^2}=\\sqrt{2}$ dir. Bu köşegeni pergelle sıfırdan başlayarak sayı doğrusuna aktarırsan $\\sqrt{2}$ nin tam yerini işaretlemiş olursun.",
            "Gerçek sayılar <strong>sıralıdır</strong>: herhangi iki gerçek sayıdan biri ötekinden büyüktür ya da ikisi eşittir. Bu özellik, gerçek sayılarla eşitsizlik kurmayı ve aralık yazmayı mümkün kılar.",
            "İki gerçek sayı arasında her zaman sonsuz sayıda rasyonel ve sonsuz sayıda irrasyonel sayı vardır. Örneğin $1$ ile $2$ arasında $1.5$ gibi rasyoneller de $\\sqrt{2}$, $\\sqrt{3}$ gibi irrasyoneller de bulunur.",
            hap("$\\mathbb{R}$, rasyonel ve irrasyonel sayıların birleşimidir ve sayı doğrusunu boşluksuz doldurur.",
                "Sayı doğrusundaki her nokta bir gerçek sayıdır, her gerçek sayı da bir noktadır."),
        ]},
        {"baslik": "Aralık gösterimi", "icerik": [
            "Gerçek sayıların bir parçasını anlatmak için <strong>aralık</strong> kullanılır. Köşeli parantez ucun dahil olduğunu, normal parantez dahil olmadığını gösterir:",
            tablo(["Gösterim", "Anlamı"], [
                ["$[a,b]$", "$a \\leq x \\leq b$"],
                ["$(a,b)$", "$a<x<b$"],
                ["$[a,b)$", "$a \\leq x<b$"],
                ["$(a,b]$", "$a<x \\leq b$"],
                ["$[a,\\infty)$", "$x \\geq a$"],
                ["$(-\\infty,b)$", "$x<b$"],
            ]),
            "Sonsuz ($\\infty$) bir sayı değil, \"sınır yok\" anlamına gelen bir semboldür. Bu yüzden sonsuz tarafında parantez her zaman normaldir; köşeli parantezle kapatılmaz.",
            ornek(
                "$(-2.5,3]$ aralığı verilsin.",
                "Bu aralıkta kaç tam sayı vardır?",
                "$-2.5$ dahil değildir; ondan büyük ilk tam sayı $-2$ dir.",
                "$3$ dahildir.",
                "Tam sayılar: $-2$, $-1$, $0$, $1$, $2$, $3$. Toplam $6$ tane."),
            ornek(
                "$x \\in [-1,4)$ ve $x$ bir tam sayı olsun.",
                "$x$ kaç farklı değer alabilir?",
                "$-1$ dahil, $4$ dahil değil.",
                "Değerler: $-1$, $0$, $1$, $2$, $3$. Toplam $5$ tane."),
            ornek(
                "$x$ bir tam sayı ve $-\\sqrt{5}<x<\\sqrt{10}$ olsun.",
                "$x$ kaç farklı değer alabilir?",
                "$4<5<9$ olduğundan $2<\\sqrt{5}<3$, yani $-3<-\\sqrt{5}<-2$. Alt sınırdan büyük ilk tam sayı $-2$ dir.",
                "$9<10<16$ olduğundan $3<\\sqrt{10}<4$. Üst sınırdan küçük son tam sayı $3$ tür.",
                "Değerler $-2$ den $3$ e kadar: $3-(-2)+1=6$ tane."),
            hap("Köşeli parantez uç <strong>dahil</strong>, normal parantez uç <strong>hariç</strong>.",
                "Sonsuz tarafında parantez her zaman normaldir."),
        ]},
        {"baslik": "Sınavda irrasyonel ve gerçek sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu \"aşağıdakilerden hangisi irrasyoneldir?\" sınıflandırmaları, köklü sayıları sıralama ve bir kökün hangi iki tam sayı arasında olduğu biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde köklü ifadeleri sadeleştirme, kök dışına çıkarma ve aralıktaki tam sayıları sayma soruları öne çıkabilir."),
            "Bu konuda işe yarayan temel beceri, sayıyı sadeleştirip karşılaştırılabilir hâle getirmektir. Kökü dışarı çıkarmayı ve içeri almayı akıcı yapmak, sınıflandırma ve sıralama sorularının ikisini birden kolaylaştırır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Her kökü irrasyonel sanmak", "$\\sqrt{16}=4$ rasyonel"],
                ["$\\pi=\\dfrac{22}{7}$ yazmak", "Yalnızca yaklaşık değer"],
                ["$\\sqrt{a+b}=\\sqrt{a}+\\sqrt{b}$ yazmak", "Kök toplamaya dağılmaz"],
                ["İki irrasyonelin toplamını hep irrasyonel sanmak", "$\\sqrt{2}+(3-\\sqrt{2})=3$"],
                ["$0 \\cdot \\sqrt{2}$ yi irrasyonel sanmak", "Sonuç $0$, rasyonel"],
                ["Sonsuz tarafına köşeli parantez koymak", "$[a,\\infty)$"],
                ["Kökleri ondalıksız sıralamaya çalışmak", "Köke sok, içleri karşılaştır"],
            ]),
            "Bu hataların çoğu bir kuralı olduğundan geniş uygulamaktan doğar: \"kök varsa irrasyoneldir\", \"irrasyonel ile işlem irrasyonel verir\" gibi. Her kuralın hangi koşulda geçerli olduğunu birlikte hatırla.",
        ]},
    ],
    "sss": [
        ("İrrasyonel sayı nedir?",
         "İki tam sayının bölümü olarak yazılamayan gerçek sayılara irrasyonel sayı denir. Ondalık gösterimleri sonsuza kadar gider ve hiçbir basamak grubu düzenli olarak tekrar etmez. Karekök iki ve pi en bilinen örneklerdir."),
        ("Her karekök irrasyonel midir?",
         "Hayır. Bir pozitif tam sayının karekökü, sayı tam kare ise doğal sayıdır ve rasyoneldir. Örneğin karekök 16 eşittir 4. Yalnızca tam kare olmayan sayıların karekökleri irrasyoneldir."),
        ("Pi sayısı neden irrasyoneldir?",
         "Pi, bir çemberin çevresinin çapına oranıdır ve hiçbir kesre tam olarak eşit olmadığı kanıtlanmıştır. 22 bölü 7 ve 3,14 yalnızca yaklaşık değerleridir."),
        ("Gerçek sayılar nedir?",
         "Rasyonel ve irrasyonel sayıların birleşimine gerçek sayılar denir. Gerçek sayılar sayı doğrusunu boşluksuz doldurur: doğrunun her noktası bir gerçek sayıdır."),
        ("İki irrasyonel sayının toplamı irrasyonel midir?",
         "Her zaman değil. Karekök 2 ile 3 eksi karekök 2 nin toplamı 3 tür ve rasyoneldir. İki irrasyonel sayının toplamı ya da çarpımı için genel bir kural yoktur, her durum ayrıca incelenir."),
        ("Aralık gösteriminde köşeli ve normal parantezin farkı nedir?",
         "Köşeli parantez ucun aralığa dahil olduğunu, normal parantez dahil olmadığını gösterir. Sonsuz bir sayı olmadığı için sonsuz tarafında her zaman normal parantez kullanılır."),
        ("Bir karekökün hangi iki tam sayı arasında olduğu nasıl bulunur?",
         "Kök içindeki sayının arasında kaldığı iki ardışık tam kare bulunur. Örneğin 20, 16 ile 25 arasındadır; bu yüzden karekök 20, 4 ile 5 arasındadır."),
        ("Paydayı rasyonel yapmak ne demektir?",
         "Paydasında kök bulunan bir kesri, değerini değiştirmeden paydasında kök kalmayacak biçimde yazmaktır. Paydada tek bir kök varsa pay ve payda o kökle, iki terimli bir ifade varsa eşleniğiyle çarpılır."),
    ],
    "kontrol": [
        "İrrasyonel sayıyı tanımlayıp devirli ondalıktan ayırt edebiliyorum.",
        "Bir karekökün rasyonel mi irrasyonel mi olduğuna tam kare kontrolüyle karar verebiliyorum.",
        "$\\sqrt{2}$ nin neden kesirle yazılamadığını ana hatlarıyla açıklayabiliyorum.",
        "$\\pi$ ile $\\dfrac{22}{7}$ nin farkını biliyorum.",
        "Kök içindeki tam kare çarpanı dışarı çıkarabiliyor, katsayıyı köke sokabiliyorum.",
        "Rasyonel ve irrasyonel sayılarla işlemlerin sonucunu kurala göre söyleyebiliyorum.",
        "Bir karekökün hangi iki tam sayı arasında olduğunu ve hangisine yakın olduğunu bulabiliyorum.",
        "Köklü sayıları köke sokarak sıralayabiliyorum.",
        "Gerçek sayıların sayı doğrusunu boşluksuz doldurduğunu açıklayabiliyorum.",
        "Aralık gösterimini okuyup bir aralıktaki tam sayıları sayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["rasyonel-sayilar-konu-anlatimi-pdf", "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf", "temel-kavramlar-konu-anlatimi-pdf"],
}
