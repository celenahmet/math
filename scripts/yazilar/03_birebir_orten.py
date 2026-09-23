# scripts/yazilar/03_birebir_orten.py — ucuncu blog yazisi (23.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "birebir-orten-fonksiyon",
    "baslik": "Birebir ve Örten Fonksiyon Nedir?",
    "aciklama": "Birebir, örten, içine ve birebir örten fonksiyon nedir, nasıl gösterilir? Yatay doğru testi, sayma formülleri ve çözümlü örneklerle.",
    "tarih": "2026-09-23",
    "guncelleme": None,
    "kategori": "fonksiyonlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "birebir-orten-fonksiyon",
    "kapak_alt": "Birebir ve örten fonksiyon: soldaki mavi düğmeleri sağdaki renkli düğmelere iplerle eşleyen ahşap eşleme tahtası ve onu inceleyen iki öğrenci",
    "ozet": "Bir eşlemenin fonksiyon olduğunu gösterdikten sonra sorulacak iki soru daha vardır. Farklı girişler farklı çıkışlara mı gidiyor? Değer kümesinde boşta kalan eleman var mı? Birincisinin cevabı birebirliği, ikincisininki örtenliği belirler. Bu yazıda iki kavramı ayrı ayrı tanımlıyor, cebirle ve grafikle nasıl gösterildiklerini, sonlu kümelerde nasıl sayıldıklarını ve ters fonksiyonla ilişkilerini adım adım ele alıyoruz.",
    "bolumler": [
        {"baslik": "Fonksiyondan sonra sorulan iki soru", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için fonksiyonun tanımını ve tanım, değer, görüntü kümesi arasındaki farkı biliyor olman yeterli.",
                "Bu kavramlar yeni geliyorsa önce <a href=\"/blog/tanim-deger-goruntu-kumeleri/\">Tanım, Değer ve Görüntü Kümeleri</a> yazısına göz at."),
            "Fonksiyon olma şartı yalnızca tanım kümesine bakar: soldaki her elemandan <strong>tam bir</strong> ok çıkmalıdır. Sağ taraf, yani değer kümesi, bu şartta hiç sorgulanmaz. Birebirlik ve örtenlik tam da o sağ tarafı inceler.",
            "<ul><li><strong>Birebirlik:</strong> Sağdaki bir elemana birden fazla ok geliyor mu?</li><li><strong>Örtenlik:</strong> Sağda hiç ok gelmeyen eleman kalıyor mu?</li></ul>",
            "Bir eşleme tahtası düşün: soldaki çivilerden sağdaki çivilere ipler gerilmiş. Soldaki her çividen tam bir ip çıkıyorsa fonksiyonun var. Sağdaki hiçbir çiviye iki ip bağlanmamışsa fonksiyon birebirdir. Sağda ipsiz çivi kalmamışsa örtendir.",
            hap("Fonksiyon şartı <strong>sol</strong> tarafa, birebirlik ve örtenlik <strong>sağ</strong> tarafa bakar.",
                "Birebir: sağa en fazla bir ok. Örten: sağa en az bir ok."),
        ]},
        {"baslik": "Birebir fonksiyon", "icerik": [
            "Farklı girişler her zaman farklı çıkışlara gidiyorsa fonksiyon <strong>birebirdir</strong>. Sözle: hiçbir iki eleman aynı görüntüyü paylaşmaz. Simgeyle:",
            "$$x_1 \\neq x_2 \\Rightarrow f(x_1) \\neq f(x_2)$$",
            "Aynı şart ters yönden de yazılabilir ve işlem yaparken çoğu zaman bu biçim daha kullanışlıdır: iki çıkış eşitse girişler de eşittir.",
            "$$f(x_1)=f(x_2) \\Rightarrow x_1=x_2$$",
            ornek(
                "$A=\\{1,2,3\\}$ ve $B=\\{a,b,c,d\\}$ olsun. $f$ fonksiyonu $1 \\to a$, $2 \\to c$, $3 \\to d$ biçiminde, $g$ fonksiyonu ise $1 \\to a$, $2 \\to a$, $3 \\to b$ biçiminde tanımlansın.",
                "Hangisi birebirdir?",
                "$f$ de sağdaki her elemana en fazla bir ok geliyor. $f$ birebirdir.",
                "$g$ de $a$ ya iki ok geliyor: $g(1)=g(2)=a$. $g$ birebir değildir."),
            hap("Birebir değildir demek için <strong>tek bir karşı örnek</strong> yeter: $x_1 \\neq x_2$ ama $f(x_1)=f(x_2)$.",
                "Birebirdir demek için ise <strong>genel</strong> bir gösterim gerekir."),
        ]},
        {"baslik": "Birebirliği cebirle gösterme", "icerik": [
            "Kural verilmiş bir fonksiyonda birebirliği göstermenin standart yolu şudur: $f(x_1)=f(x_2)$ olduğunu varsay ve bu eşitlikten $x_1=x_2$ sonucuna ulaşmaya çalış. Ulaşırsan fonksiyon birebirdir.",
            ornek(
                "$f(x)=\\dfrac{2x+1}{x-3}$ olsun, tanım kümesi $\\mathbb{R}-\\{3\\}$.",
                "$f$ birebir midir?",
                "$f(x_1)=f(x_2)$ diyelim: $\\dfrac{2x_1+1}{x_1-3}=\\dfrac{2x_2+1}{x_2-3}$.",
                "İçler dışlar çarpımı: $(2x_1+1)(x_2-3)=(2x_2+1)(x_1-3)$.",
                "Açalım: $2x_1x_2-6x_1+x_2-3=2x_1x_2-6x_2+x_1-3$.",
                "Ortak terimler sadeleşir: $-6x_1+x_2=-6x_2+x_1$, yani $7x_2=7x_1$.",
                "Buradan $x_1=x_2$ çıkar. $f$ birebirdir."),
            "Birebir olmayan bir fonksiyonda aynı yol bir yerde tıkanır ve tıkandığı yer sana karşı örneği verir.",
            ornek(
                "$f(x)=x^2-2x$ olsun, tanım kümesi $\\mathbb{R}$.",
                "$f$ birebir midir?",
                "$f(x_1)=f(x_2)$ diyelim: $x_1^2-2x_1=x_2^2-2x_2$.",
                "Düzenleyelim: $x_1^2-x_2^2-2(x_1-x_2)=0$, yani $(x_1-x_2)(x_1+x_2-2)=0$.",
                "Bu eşitlik $x_1=x_2$ olmadan da sağlanabilir: $x_1+x_2=2$ olması yeter.",
                "Örneğin $x_1=0$ ve $x_2=2$ için $f(0)=0$ ve $f(2)=0$. $f$ birebir değildir."),
        ]},
        {"baslik": "Yatay doğru testi", "icerik": [
            "Grafiği verilen bir fonksiyonda birebirliği gözle sınayabilirsin. Grafiği kesen <strong>her yatay doğru</strong> grafiği en fazla bir noktada kesiyorsa fonksiyon birebirdir. Bir yatay doğru grafiği iki noktada kesiyorsa, aynı $y$ değerine iki farklı $x$ gidiyor demektir.",
            "<ul><li>$y=x^3$: her yatay doğru grafiği tam bir noktada keser. Birebirdir.</li>"
            "<li>$y=x^2$: örneğin $y=4$ doğrusu grafiği $x=-2$ ve $x=2$ de keser. Birebir değildir.</li>"
            "<li>$y=|x|$: $y=3$ doğrusu $x=-3$ ve $x=3$ te keser. Birebir değildir.</li>"
            "<li>$y=2^x$: her yatay doğru grafiği en fazla bir noktada keser. Birebirdir.</li></ul>",
            "Tanım kümesi daraltılınca birebir olmayan bir kural birebir hâle gelebilir. $f(x)=x^2$ kuralı $\\mathbb{R}$ de birebir değildir, ama tanım kümesi $[0,\\infty)$ alınırsa birebirdir; çünkü artık negatif girişler yoktur.",
            "Grafiğe bakmadan da işe yarayan bir ölçüt vardır: tanım kümesinin tamamında <strong>artan</strong> (ya da tamamında <strong>azalan</strong>) bir fonksiyon birebirdir. Çünkü $x_1<x_2$ ise $f(x_1)<f(x_2)$ olur ve iki çıkış eşit olamaz.",
            hap("<strong>Dikey doğru testi:</strong> fonksiyon mu?<br><strong>Yatay doğru testi:</strong> birebir mi?",
                "Tanım kümesinin tamamında artan ya da azalan fonksiyon birebirdir."),
            dikkat(
                "Bu ölçütün tersi her zaman doğru değildir.",
                "$f(x)=\\dfrac{1}{x}$ birebirdir, ama tanım kümesinin tamamında azalan değildir: $-1<1$ iken $f(-1)=-1<f(1)=1$.",
                "Fonksiyon her parçada ayrı ayrı azalır; birebirlik bu yüzden bozulmaz."),
        ]},
        {"baslik": "Örten fonksiyon", "icerik": [
            "Değer kümesinde boşta eleman kalmıyorsa, yani her elemana en az bir ok geliyorsa fonksiyon <strong>örtendir</strong>. Bu, görüntü kümesinin değer kümesine eşit olması demektir:",
            "$$f:A \\to B \\text{ örten } \\Leftrightarrow f(A)=B$$",
            "Değer kümesinde en az bir eleman boşta kalıyorsa fonksiyon <strong>içine</strong> fonksiyondur. Her fonksiyon ya örtendir ya içinedir; üçüncü bir seçenek yoktur.",
            "Örtenlik yalnızca kurala değil, <strong>değer kümesine</strong> de bağlıdır. Aynı kural bir değer kümesiyle örten, başka biriyle içine olabilir. Bu yüzden \"$f(x)=x^2+1$ örten midir?\" sorusu değer kümesi söylenmeden cevaplanamaz.",
            ornek(
                "$f(x)=x^2+1$ kuralını iki ayrı değer kümesiyle ele alalım.",
                "$f:\\mathbb{R} \\to \\mathbb{R}$ ve $f:\\mathbb{R} \\to [1,\\infty)$ örten midir?",
                "$x^2 \\geq 0$ olduğu için $x^2+1 \\geq 1$ dir; görüntü kümesi $[1,\\infty)$ dur.",
                "$f:\\mathbb{R} \\to \\mathbb{R}$ olarak örten değildir; örneğin $0$ a hiç ok gelmez.",
                "$f:\\mathbb{R} \\to [1,\\infty)$ olarak örtendir, çünkü görüntü kümesi değer kümesine eşittir."),
            hap("Örten $\\Leftrightarrow$ görüntü kümesi = değer kümesi.",
                "Örtenlik sorusunda önce görüntü kümesini bul, sonra değer kümesiyle karşılaştır."),
        ]},
        {"baslik": "Örtenliği cebirle gösterme", "icerik": [
            "Örtenliği göstermek için değer kümesinden <strong>herhangi</strong> bir $y$ alırsın ve $f(x)=y$ denklemini $x$ için çözersin. Çıkan $x$ her $y$ için tanım kümesinin içindeyse fonksiyon örtendir.",
            ornek(
                "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=3x-5$ olsun.",
                "$f$ örten midir?",
                "Herhangi bir $y$ için $3x-5=y$ denklemini çözelim: $x=\\dfrac{y+5}{3}$.",
                "Bu sayı her $y$ için bir gerçel sayıdır, yani tanım kümesinin içindedir.",
                "Kontrol: $f\\left(\\dfrac{y+5}{3}\\right)=y+5-5=y$. $f$ örtendir."),
            "Tanım kümesi de örtenliği etkiler. $f(x)=2x$ kuralı $\\mathbb{R} \\to \\mathbb{R}$ olarak örtendir. Aynı kural tam sayılarda, yani $\\mathbb{Z} \\to \\mathbb{Z}$ olarak örten değildir: $2x=3$ denkleminin çözümü $x=1.5$ tir ve bu bir tam sayı değildir. Tek sayıların hiçbirine ok gelmez. Yine de bu fonksiyon birebirdir.",
            ornek(
                "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=2x+|x|$ olsun.",
                "$f$ birebir ve örten midir?",
                "Mutlak değeri açalım. $x \\geq 0$ için $f(x)=3x$, $x<0$ için $f(x)=x$ olur.",
                "İki parça da artandır ve $x=0$ da ikisi de $0$ değerini verir; fonksiyon her yerde artandır. Bu yüzden birebirdir.",
                "Birinci parça $[0,\\infty)$ aralığını, ikinci parça $(-\\infty,0)$ aralığını doldurur. Birleşimleri $\\mathbb{R}$ dir; $f$ örtendir."),
        ]},
        {"baslik": "Yatay doğruyla birebirlik ve örtenlik", "icerik": [
            "Yatay doğru testi yalnızca birebirliği değil, örtenliği de gösterebilir. Değer kümesindeki her $k$ için $y=k$ doğrusunu düşün ve grafiği kaç kez kestiğine bak:",
            "<ul><li>Her doğru grafiği <strong>en fazla bir</strong> kez kesiyorsa fonksiyon birebirdir.</li><li>Her doğru grafiği <strong>en az bir</strong> kez kesiyorsa fonksiyon örtendir.</li><li>Her doğru grafiği <strong>tam bir</strong> kez kesiyorsa fonksiyon birebir örtendir.</li></ul>",
            "Burada önemli olan, doğruların yalnızca <strong>değer kümesindeki</strong> $k$ değerleri için çizilmesidir. Değer kümesi değişince bakılacak doğrular da değişir.",
            ornek(
                "$f(x)=x^2-4x+3$ olsun. Tepe noktası $(2,-1)$ dir.",
                "$f:\\mathbb{R} \\to \\mathbb{R}$ ve $f:[2,\\infty) \\to [-1,\\infty)$ için birebirlik ve örtenliği yatay doğrularla inceleyelim.",
                "$f:\\mathbb{R} \\to \\mathbb{R}$ için $y=-2$ doğrusu grafiği hiç kesmez; $f$ örten değildir. $y=3$ doğrusu grafiği $x=0$ ve $x=4$ te keser; $f$ birebir de değildir.",
                "$f:[2,\\infty) \\to [-1,\\infty)$ için grafik yalnızca tepe noktasından sağa giden koldur. $k \\geq -1$ olan her $y=k$ doğrusu bu kolu tam bir kez keser.",
                "Bu hâliyle $f$ birebir örtendir."),
            "<h3>Parçalı fonksiyonda dikkat</h3>",
            "Parçalı bir fonksiyonun her parçası ayrı ayrı birebir olabilir, ama fonksiyonun tamamı birebir olmayabilir. Parçaların görüntü kümeleri <strong>çakışıyorsa</strong> iki farklı parçadan aynı değer çıkar.",
            ornek(
                "$x<0$ için $f(x)=x+1$, $x \\geq 0$ için $f(x)=x^2$ olsun, $f:\\mathbb{R} \\to \\mathbb{R}$.",
                "$f$ birebir ve örten midir?",
                "Birinci parçanın görüntü kümesi $(-\\infty,1)$, ikinci parçanınki $[0,\\infty)$ dur.",
                "Birleşimleri $\\mathbb{R}$ olduğu için $f$ örtendir.",
                "İki görüntü kümesi ise $[0,1)$ aralığında çakışıyor. Örneğin $f(-0.5)=0.5$ ve $f\\left(\\sqrt{0.5}\\right)=0.5$.",
                "$f$ birebir değildir."),
            hap("Parçalı fonksiyonda birebirlik için her parçanın birebir olması yetmez; parçaların görüntü kümeleri de çakışmamalıdır.",
                "Örtenlik için parçaların görüntü kümelerinin birleşimi değer kümesine eşit olmalıdır."),
        ]},
        {"baslik": "Dört durum ve eleman sayıları", "icerik": [
            "Birebirlik ve örtenlik birbirinden bağımsızdır. Bir fonksiyon ikisine de sahip olabilir, yalnız birine sahip olabilir ya da hiçbirine sahip olmayabilir:",
            tablo(["Durum", "Örnek"], [
                ["Birebir ve örten", "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=x^3$"],
                ["Birebir, örten değil", "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=2^x$"],
                ["Örten, birebir değil", "$f:\\mathbb{R} \\to [0,\\infty)$, $f(x)=x^2$"],
                ["İkisi de değil", "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=x^2$"],
            ]),
            "Sonlu kümelerde eleman sayıları bu dört durumdan bazılarını baştan eler. $A$ da $B$ den fazla eleman varsa, bazı elemanlar aynı yere gitmek zorundadır; buna <strong>güvercin yuvası ilkesi</strong> denir. $A$ da $B$ den az eleman varsa, oklar $B$ nin hepsine yetmez.",
            hap("Sonlu kümelerde: $s(A)>s(B)$ ise fonksiyon birebir olamaz. $s(A)<s(B)$ ise örten olamaz.",
                "$s(A)=s(B)$ ise birebir olmak ile örten olmak aynı şeydir: biri varsa öteki de vardır."),
            dikkat(
                "Son kural yalnızca <strong>sonlu ve eşit sayıda elemanlı</strong> kümeler için geçerlidir.",
                "Sonsuz kümelerde bozulur: $f:\\mathbb{Z} \\to \\mathbb{Z}$, $f(x)=2x$ birebirdir ama örten değildir."),
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu şema üzerinden gelebilir: birkaç eşleme verilir, hangisinin birebir, örten ya da birebir örten olduğu sorulur. Eleman sayısı soruları da bu düzeydedir.",
                "İleri düzeyde (<strong>AYT</strong>) kural verilir ve bir parametre istenir: \"birebir örten ise $a$ kaçtır?\" gibi. Ters fonksiyonun var olup olmadığını tartışmak için de kullanılır."),
        ]},
        {"baslik": "Birebir örten fonksiyon", "icerik": [
            "Hem birebir hem örten olan fonksiyona <strong>birebir örten</strong> fonksiyon denir. Bu durumda $B$ deki her elemana <strong>tam bir</strong> ok gelir: ne boşta eleman kalır ne de iki ok aynı yere gider. İki küme arasında kusursuz bir eşleşme kurulmuş olur.",
            "Birebir örten fonksiyonun en önemli sonucu, geriye dönüşün de bir fonksiyon olmasıdır. Her çıkış tek bir girişten geldiği için okları ters çevirdiğinde yine bir fonksiyon elde edersin. Bu, <strong>ters fonksiyondur</strong>.",
            hap("Bir fonksiyonun tersinin var olması için birebir <strong>ve</strong> örten olması gerekir ve yeter.",
                "Birebir değilse ters çevrilen oklardan biri iki yere gider. Örten değilse boşta kalan eleman geriye dönemez."),
            "Parametreli sorularda bu bilgi doğrudan kullanılır.",
            ornek(
                "$f:\\mathbb{R} \\to \\mathbb{R}$, $f(x)=(a-2)x^2+3x+1$ fonksiyonu birebir örten olsun.",
                "$a$ kaçtır?",
                "$a-2 \\neq 0$ olsaydı $f$ ikinci dereceden olurdu. Parabol bir tepe noktasından sonra yön değiştirdiği için birebir olamazdı.",
                "O hâlde $a-2=0$, yani $a=2$ olmalı.",
                "Kontrol: $a=2$ için $f(x)=3x+1$ olur. Bu doğrusal fonksiyon $\\mathbb{R} \\to \\mathbb{R}$ olarak birebir ve örtendir."),
            ornek(
                "$f:[2,\\infty) \\to [k,\\infty)$, $f(x)=x^2-4x+1$ fonksiyonu birebir örten olsun.",
                "$k$ kaçtır?",
                "Tepe noktasının apsisi $x=-\\dfrac{-4}{2}=2$ dir; tanım kümesi tam tepe noktasından başlıyor. Bu aralıkta fonksiyon artandır ve birebirdir.",
                "Görüntü kümesi $f(2)$ den başlar: $f(2)=4-8+1=-3$.",
                "Örten olması için değer kümesi görüntü kümesine eşit olmalı: $[k,\\infty)=[-3,\\infty)$.",
                "$k=-3$ tür."),
        ]},
        {"baslik": "Sayma: kaç birebir, kaç örten?", "icerik": [
            "$s(A)=m$ ve $s(B)=n$ olsun. $A$ dan $B$ ye tanımlanabilen fonksiyonları türlerine göre saymak için sırayla düşünürüz.",
            "<ul><li><strong>Bütün fonksiyonlar:</strong> her eleman için $n$ seçenek, toplam $n^m$.</li>"
            "<li><strong>Birebir fonksiyonlar</strong> ($m \\leq n$): ilk eleman için $n$, ikinci için $n-1$, ... seçenek. Toplam $n \\cdot (n-1) \\cdots (n-m+1)=\\dfrac{n!}{(n-m)!}$.</li>"
            "<li><strong>Birebir örten fonksiyonlar</strong> ($m=n$): $n!$.</li>"
            "<li><strong>İçine fonksiyonlar:</strong> bütün fonksiyonlardan örtenler çıkarılır.</li></ul>",
            "Örten fonksiyonları saymak daha zordur, çünkü \"her elemana en az bir ok\" şartı doğrudan çarpıma dönüşmez. Küçük durumlarda boşta eleman bırakanları çıkararak sayarız.",
            ornek(
                "$s(A)=4$ ve $s(B)=3$ olsun, $B=\\{a,b,c\\}$.",
                "$A$ dan $B$ ye kaç örten fonksiyon vardır?",
                "Bütün fonksiyonlar: $3^4=81$.",
                "$a$ yı boşta bırakanlar, yani yalnızca $\\{b,c\\}$ ye gidenler: $2^4=16$. $b$ yi ve $c$ yi boşta bırakanlar için de $16$ şar tane vardır.",
                "Bu üç grubu toplarsak iki elemanı birden boşta bırakanları iki kez çıkarmış oluruz. Bunlar sabit fonksiyonlardır ve $3$ tanedir; onları geri ekleriz.",
                "Örten fonksiyon sayısı: $81-3 \\cdot 16+3=36$."),
            "Bu yola <strong>içerme dışarma ilkesi</strong> denir. Genel hâli şudur:",
            "$$\\sum_{k=0}^{n} (-1)^k \\binom{n}{k} (n-k)^m$$",
            hap("$s(B)=2$ ise örten fonksiyon sayısı $2^m-2$ dir.",
                "$s(A)=s(B)=n$ ise birebir, örten ve birebir örten fonksiyonların sayısı aynıdır: $n!$."),
            ornek(
                "$A=\\{1,2,3\\}$ ve $B=\\{a,b,c\\}$ olsun.",
                "Kaç içine fonksiyon vardır?",
                "Bütün fonksiyonlar: $3^3=27$.",
                "Eleman sayıları eşit olduğu için örten fonksiyonlar birebir örten fonksiyonlarla aynıdır: $3!=6$.",
                "İçine fonksiyonlar: $27-6=21$."),
        ]},
        {"baslik": "Sık karşılaşılan fonksiyonlar", "icerik": [
            "Aşağıdaki tablo, sınavda en çok karşına çıkacak fonksiyonların $\\mathbb{R}$ den $\\mathbb{R}$ ye tanımlandığındaki durumunu özetliyor. Tanım ya da değer kümesi değişirse sonuç da değişebilir.",
            tablo(["Fonksiyon", "Birebir", "Örten"], [
                ["$f(x)=x$ (birim)", "Evet", "Evet"],
                ["$f(x)=c$ (sabit)", "Hayır", "Hayır"],
                ["$f(x)=ax+b$, $a \\neq 0$", "Evet", "Evet"],
                ["$f(x)=x^2$", "Hayır", "Hayır"],
                ["$f(x)=x^3$", "Evet", "Evet"],
                ["$f(x)=|x|$", "Hayır", "Hayır"],
                ["$f(x)=2^x$", "Evet", "Hayır"],
            ]),
            "$2^x$ fonksiyonunun görüntü kümesi $(0,\\infty)$ dur. Değer kümesi $(0,\\infty)$ alınırsa birebir örten olur; $2$ tabanında logaritma fonksiyonu tam da bu fonksiyonun tersidir.",
            dikkat(
                "Sabit fonksiyonun birebir olmaması tanım kümesinde en az iki eleman olmasına bağlıdır.",
                "Tanım kümesi tek elemanlıysa sabit fonksiyon da birebirdir. Tablodaki \"Hayır\" cevabı, tanım kümesi $\\mathbb{R}$ olduğu için doğrudur."),
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Örtenliği değer kümesine bakmadan söylemek", "Örtenlik değer kümesine bağlıdır"],
                ["Birebirliği birkaç değer deneyerek kanıtlamak", "Genel gösterim gerekir"],
                ["Dikey ve yatay doğru testini karıştırmak", "Dikey: fonksiyon mu, yatay: birebir mi"],
                ["$s(A)=s(B)$ kuralını sonsuz kümelere uygulamak", "Yalnızca sonlu kümelerde geçerli"],
                ["Birebir fonksiyonun tersi her zaman vardır sanmak", "Örten de olmalı"],
                ["$A$ da $B$ den fazla eleman varken birebir aramak", "Birebir fonksiyon yoktur"],
            ]),
            "Bu hataların ortak noktası şu: birebirlik ve örtenlik kuralın değil, <strong>kural ile iki kümenin</strong> birlikte özelliğidir. Soruda tanım ve değer kümesini görmeden karar verme.",
        ]},
    ],
    "sss": [
        ("Birebir fonksiyon nedir?",
         "Farklı girişleri her zaman farklı çıkışlara götüren fonksiyondur. Değer kümesindeki hiçbir elemana birden fazla ok gelmez."),
        ("Örten fonksiyon nedir?",
         "Değer kümesinde boşta eleman bırakmayan fonksiyondur. Görüntü kümesi değer kümesine eşittir."),
        ("İçine fonksiyon nedir?",
         "Örten olmayan fonksiyondur. Değer kümesinde hiç ok gelmeyen en az bir eleman vardır."),
        ("Birebir örten fonksiyonun tersi her zaman var mıdır?",
         "Evet. Bir fonksiyonun tersinin var olması için birebir ve örten olması gerekir ve yeter. Bu iki şarttan biri eksikse ters fonksiyon yoktur."),
        ("Yatay doğru testi neyi gösterir?",
         "Bir fonksiyonun birebir olup olmadığını gösterir. Her yatay doğru grafiği en fazla bir noktada kesiyorsa fonksiyon birebirdir."),
        ("Eleman sayıları eşit iki sonlu küme arasında birebir olan fonksiyon örten midir?",
         "Evet. Eleman sayıları eşit sonlu kümelerde birebir olmak ile örten olmak aynı şeydir. Bu kural sonsuz kümelerde geçerli değildir."),
    ],
    "kontrol": [
        "Bir şemada birebirlik ve örtenliği sağ taraftaki ok sayısına bakarak ayırt edebiliyorum.",
        "Birebirliği $f(x_1)=f(x_2) \\Rightarrow x_1=x_2$ yoluyla gösterebiliyorum.",
        "Birebir olmayan bir fonksiyon için tek bir karşı örnek verebiliyorum.",
        "Yatay doğru testini bir grafik üzerinde uygulayabiliyorum.",
        "Örtenliği $f(x)=y$ denklemini çözerek gösterebiliyorum.",
        "Aynı kuralın değer kümesine göre örten ya da içine olabileceğini bir örnekle açıklayabiliyorum.",
        "Sonlu kümelerde eleman sayılarından hangi durumların imkânsız olduğunu söyleyebiliyorum.",
        "Birebir örten olma şartından bir parametreyi bulabiliyorum.",
        "Birebir, birebir örten ve içine fonksiyonların sayısını hesaplayabiliyorum.",
        "Küçük kümelerde örten fonksiyonları boşta eleman bırakanları çıkararak sayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["tanim-deger-goruntu-kumeleri", "bileske-fonksiyon", "ters-fonksiyon"],
}
