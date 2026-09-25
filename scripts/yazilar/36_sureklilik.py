# scripts/yazilar/36_sureklilik.py — Sureklilik Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "sureklilik-konu-anlatimi",
    "baslik": "Süreklilik Konu Anlatımı",
    "aciklama": "Süreklilik nedir? Bir noktada süreklilik koşulları, süreksizlik türleri, sürekli yapan parametre, aralıkta süreklilik ve ara değer teoremi; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "sureklilik-konu-anlatimi",
    "kapak_alt": "Süreklilik konu anlatımı: kopuksuz mavi bir yol ile parçalı ve kesintili bir yolu karşılaştıran öğrenci",
    "ozet": "Süreklilik, bir fonksiyonun grafiğinin kopmadan, sıçramadan ve boşluk bırakmadan ilerlemesidir. Bir noktadaki süreklilik, fonksiyonun o noktadaki değeri ile limitinin eşit olmasıyla tanımlanır. Bu yazıda sürekliliğin sezgisel anlamını ve üç koşullu tanımını, kaldırılabilir, sıçrama ve sonsuz süreksizlik türlerini, sürekli fonksiyon ailelerini, rasyonel fonksiyonların süreksiz olduğu noktaları, parçalı fonksiyonu sürekli yapan parametreleri, mutlak değer ve tam değer fonksiyonlarını, aralıkta sürekliliği, ara değer teoremini ve en büyük ve en küçük değer teoremini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Süreklilik nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için limiti ve soldan ve sağdan limiti biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/limit-konu-anlatimi/\">Limit Konu Anlatımı</a> ve <a href=\"/blog/sagdan-soldan-limit/\">Sağdan ve Soldan Limit Nasıl Bulunur?</a> yazılarına göz at."),
            "Bir fonksiyonun grafiği bir noktada kopmuyor, sıçramıyor ve boşluk bırakmıyorsa fonksiyon o noktada <strong>süreklidir</strong>. Sezgisel olarak sürekli bir grafik, kalem kâğıttan hiç kaldırılmadan çizilebilir; kalemin kaldırılması gereken her yer bir süreksizlik noktasıdır.",
            "Kapaktaki öğrenci iki yolu karşılaştırıyor: üstteki mavi yol baştan sona kopuksuz ilerliyor, alttaki ise parçalardan oluşuyor ve aralarında boşluklar var. Üstteki yol sürekli bir grafiğe, alttaki süreksiz bir grafiğe benzer. Bu yazı, bir grafiğin hangi noktalarda koptuğunu ve kopukluğun türünü belirlemeyi anlatıyor.",
        ]},
        {"baslik": "Bir noktada süreklilik", "icerik": [
            "Sezgisel tanım limit diliyle kesinleştirilir. Bir $f$ fonksiyonunun $x=a$ noktasında sürekli olması için üç koşulun birlikte sağlanması gerekir:",
            tablo(["Koşul", "Anlamı"], [
                ["$f(a)$ tanımlı", "Grafikte o noktada bir nokta var"],
                ["$\\lim_{x \\to a} f(x)$ var", "İki yön aynı değere gidiyor"],
                ["$\\lim_{x \\to a} f(x)=f(a)$", "Nokta, gidilen yerde duruyor"],
            ]),
            hap("Süreklilik için limit, fonksiyonun değerine eşit olmalıdır.",
                "Üç koşuldan biri bile bozulursa fonksiyon o noktada süreksizdir."),
        ]},
        {"baslik": "Sürekli bir örnek", "icerik": [
            "Koşulların nasıl kontrol edildiğini basit bir fonksiyonla görelim. Polinomlarda üç koşul da her noktada kendiliğinden sağlanır.",
            ornek(
                "$f(x)=x^2+1$ fonksiyonu ve $x=2$ noktası verilsin.",
                "Fonksiyonun bu noktada sürekli olup olmadığını inceleyelim.",
                "$f(2)=5$ tir, yani fonksiyon tanımlıdır. $\\lim_{x \\to 2}(x^2+1)=5$ tir, yani limit vardır.",
                "Limit fonksiyon değerine eşit olduğu için $f$, $x=2$ de süreklidir."),
        ]},
        {"baslik": "Tanımsız noktada süreksizlik", "icerik": [
            "Fonksiyon bir noktada tanımlı değilse o noktada sürekli olamaz. Limit var olsa bile birinci koşul sağlanmaz. Paydayı sıfır yapan noktalar ve kök içini negatif yapan değerler bu tür noktaların en sık görülen örnekleridir.",
            koordinat_grafik("y = (x² - 4)/(x - 2) grafiği", [("", lambda x: x + 2 if abs(x - 2) > 1e-9 else None)], (-2, 4.5), (-1, 7), adim=1,
                             noktalar=[(2, 4, "", False)]),
            ornek(
                "$f(x)=\\dfrac{x^2-4}{x-2}$ fonksiyonu verilsin.",
                "$x=2$ deki sürekliliği inceleyelim ve fonksiyonu sürekli yapmanın yolunu bulalım.",
                "$f(2)$ tanımsızdır; ama $x \\neq 2$ için $f(x)=x+2$ olduğundan limit $4$ tür.",
                "$f(2)=4$ olarak tanımlanırsa fonksiyon $x=2$ de sürekli olur."),
            "Bu tür süreksizliğe <strong>kaldırılabilir süreksizlik</strong> denir: grafikte yalnızca tek bir nokta eksiktir ve o nokta eklenerek boşluk kapatılabilir.",
        ]},
        {"baslik": "Süreksizliği gideren değer", "icerik": [
            "Kaldırılabilir bir süreksizlikte fonksiyonun o noktadaki değeri bir bilinmeyenle verilebilir. Fonksiyonun sürekli olması için bu bilinmeyen, noktadaki limite eşit olmalıdır.",
            ornek(
                "$x \\neq 3$ için $f(x)=\\dfrac{x^2-9}{x-3}$ ve $f(3)=k$ olsun.",
                "Fonksiyonun $x=3$ te sürekli olması için $k$ yı bulalım.",
                "$x \\neq 3$ için kesir $x+3$ e sadeleşir; limit $6$ olur.",
                "Süreklilik için $k=6$ olmalıdır."),
        ]},
        {"baslik": "Limit ile değerin farklı olması", "icerik": [
            "Fonksiyon tanımlı ve limit var olsa bile ikisi farklıysa süreklilik yine bozulur. Grafikte nokta, eğrinin gittiği yerden koparılıp başka bir yüksekliğe konmuş gibidir.",
            ornek(
                "$x \\neq 2$ için $f(x)=x+1$ ve $f(2)=5$ olsun.",
                "Sürekliliği inceleyelim.",
                "$\\lim_{x \\to 2} f(x)=3$ tür ama $f(2)=5$ tir.",
                "Limit değere eşit olmadığı için fonksiyon $x=2$ de süreksizdir; $f(2)$ nin $3$ olarak yeniden tanımlanması süreksizliği kaldırır."),
        ]},
        {"baslik": "Sıçrama süreksizliği", "icerik": [
            "Soldan ve sağdan limitler var ama farklıysa grafik o noktada bir yükseklikten başka bir yüksekliğe sıçrar. Bu tür süreksizlik tek bir nokta değiştirilerek kaldırılamaz; çünkü limitin kendisi yoktur.",
            ornek(
                "$x<1$ için $f(x)=x^2$, $x \\ge 1$ için $f(x)=x+2$ olsun.",
                "$x=1$ deki sürekliliği inceleyelim.",
                "Soldan limit $1$, sağdan limit $3$ tür; limit yoktur.",
                "Fonksiyon $x=1$ de sıçrama süreksizliğine sahiptir; sıçramanın büyüklüğü $3-1=2$ dir."),
        ]},
        {"baslik": "Sonsuz süreksizlik", "icerik": [
            "Fonksiyon bir noktanın yakınında sınırsız büyüyor ya da küçülüyorsa grafikte dikey bir asimptot vardır. Bu noktada fonksiyon tanımsızdır ve limit sonlu bir sayı değildir.",
            ornek(
                "$f(x)=\\dfrac{1}{x-2}$ fonksiyonu verilsin.",
                "$x=2$ deki sürekliliği inceleyelim.",
                "Soldan limit $-\\infty$, sağdan limit $+\\infty$ dur.",
                "Fonksiyon $x=2$ de sonsuz süreksizliğe sahiptir; grafik $x=2$ doğrusunun iki yanında ters yönlere kaçar."),
        ]},
        {"baslik": "Süreksizlik türleri", "icerik": [
            "Süreksizlikler, grafikte nasıl göründüklerine ve kaldırılıp kaldırılamayacaklarına göre sınıflandırılır:",
            tablo(["Tür", "Limit", "Grafikte", "Kaldırılabilir mi?"], [
                ["Kaldırılabilir", "Var", "Tek noktalık boşluk", "Evet"],
                ["Sıçrama", "Yok, iki yön farklı", "Basamak", "Hayır"],
                ["Sonsuz", "Sonlu değil", "Dikey asimptot", "Hayır"],
            ]),
            "Kaldırılabilir süreksizlik, fonksiyonun o noktadaki değerinin limit olarak yeniden tanımlanmasıyla giderilir. Diğer iki türde böyle bir düzeltme mümkün değildir; çünkü ortada fonksiyonun gitmesi gereken tek bir değer yoktur.",
            hap("Kaldırılabilir süreksizlik tek bir değer değiştirilerek giderilir.", "Sıçrama ve sonsuz süreksizlik ise bir değer değiştirilerek giderilemez."),
        ]},
        {"baslik": "Sürekli fonksiyon aileleri", "icerik": [
            "Birçok temel fonksiyon tanımlı olduğu her noktada süreklidir. Bu bilgi, süreklilik sorularında yalnızca şüpheli noktaları incelemeyi yeterli kılar:",
            tablo(["Fonksiyon", "Sürekli olduğu yer"], [
                ["Polinomlar", "Bütün gerçek sayılar"],
                ["Rasyonel fonksiyonlar", "Paydayı sıfır yapmayan noktalar"],
                ["Köklü fonksiyonlar", "Tanım kümesi"],
                ["Üstel fonksiyonlar", "Bütün gerçek sayılar"],
                ["Logaritma", "Pozitif sayılar"],
                ["$\\sin x$ ve $\\cos x$", "Bütün gerçek sayılar"],
            ]),
            "Sürekli fonksiyonların toplamı, farkı, çarpımı ve bileşkesi de süreklidir. Bölümleri ise paydanın sıfır olmadığı her noktada süreklidir.",
        ]},
        {"baslik": "Rasyonel fonksiyonun süreksiz noktaları", "icerik": [
            "Rasyonel bir fonksiyon yalnızca paydasını sıfır yapan noktalarda süreksizdir. Bu noktaları bulmak için payda sıfıra eşitlenir. Pay o noktada sıfırdan farklıysa süreksizlik sonsuz türdendir; pay da sıfırsa önce sadeleştirme yapılır ve nokta yeniden incelenir.",
            ornek(
                "$f(x)=\\dfrac{x+1}{x^2-5x+6}$ fonksiyonu verilsin.",
                "Fonksiyonun süreksiz olduğu noktaları bulalım.",
                "Payda $(x-2)(x-3)$ olarak çarpanlarına ayrılır.",
                "Fonksiyon $x=2$ ve $x=3$ te süreksizdir; diğer bütün noktalarda süreklidir."),
        ]},
        {"baslik": "Her yerde sürekli olma koşulu", "icerik": [
            "Bir rasyonel fonksiyonun bütün gerçek sayılarda sürekli olması için paydasının hiçbir gerçek sayıda sıfır olmaması gerekir. Payda ikinci dereceden bir polinomsa bu, diskriminantın negatif olması demektir.",
            ornek(
                "$f(x)=\\dfrac{x-1}{x^2-2x+m}$ fonksiyonu verilsin.",
                "Fonksiyonun her yerde sürekli olması için $m$ nin alabileceği değerleri bulalım.",
                "Paydanın gerçek kökü olmamalı: $\\Delta=4-4m<0$.",
                "Buradan $m>1$ bulunur."),
            "Diskriminantın ayrıntısı için <a href=\"/blog/diskriminant-delta/\">Diskriminant</a> yazısına bakabilirsin.",
            hap("Paydası ikinci dereceden olan bir rasyonel fonksiyonun her yerde sürekli olması için paydanın diskriminantı negatif olmalıdır."),
        ]},
        {"baslik": "Tanjant fonksiyonunun sürekliliği", "icerik": [
            "Tanjant, sinüsün kosinüse bölümüdür. Sinüs ve kosinüs her yerde sürekli olduğu için tanjant, kosinüsün sıfır olmadığı her noktada süreklidir; kosinüsün sıfır olduğu $x=\\dfrac{\\pi}{2}+k\\pi$ noktalarında ise sonsuz süreksizlik vardır.",
            ornek(
                "$\\tan x$ fonksiyonu $[0, 2\\pi]$ aralığında verilsin.",
                "Bu aralıkta kaç noktada süreksiz olduğunu bulalım.",
                "Aralıkta kosinüs $\\dfrac{\\pi}{2}$ ve $\\dfrac{3\\pi}{2}$ noktalarında sıfırdır.",
                "Tanjant bu iki noktada süreksizdir."),
        ]},
        {"baslik": "Bileşke fonksiyonun sürekliliği", "icerik": [
            "Sürekli fonksiyonların bileşkesi süreklidir. Dıştaki fonksiyonun süreksiz olduğu bir nokta varsa, içteki fonksiyonun bu değeri aldığı her $x$ te bileşke süreksiz olur.",
            ornek(
                "$f(x)=\\dfrac{1}{x-1}$ ve $g(x)=x^2$ olsun.",
                "$f(g(x))$ bileşkesinin süreksiz olduğu noktaları bulalım.",
                "$f$, $1$ de süreksizdir; bu yüzden $g(x)=1$, yani $x^2=1$ olan noktalar aranır.",
                "Bileşke $x=1$ ve $x=-1$ de süreksizdir; gerçekten $f(g(x))=\\dfrac{1}{x^2-1}$ olur."),
        ]},
        {"baslik": "Parçalı fonksiyonu sürekli yapmak", "icerik": [
            "Parçalı bir fonksiyonun kritik noktada sürekli olması için soldan limit, sağdan limit ve fonksiyonun değeri eşit olmalıdır. Kurallarda bilinmeyen varsa bu eşitlik bir denklem verir.",
            ornek(
                "$x<2$ için $f(x)=ax-1$, $x \\ge 2$ için $f(x)=x^2+a$ olsun.",
                "Fonksiyonun her yerde sürekli olması için $a$ yı bulalım.",
                "Soldan limit $2a-1$, sağdan limit ve $f(2)$ ise $4+a$ dır.",
                "$2a-1=4+a$ denkleminden $a=5$ bulunur."),
        ]},
        {"baslik": "İki parametreli süreklilik", "icerik": [
            "Kritik noktada fonksiyonun değeri ayrıca tanımlanmışsa üç değerin eşitliği iki ayrı denklem verir; böylece iki bilinmeyen birlikte bulunur.",
            ornek(
                "$x<1$ için $f(x)=x+a$, $f(1)=3$ ve $x>1$ için $f(x)=bx+1$ olsun.",
                "Fonksiyonun $x=1$ de sürekli olması için $a$ ve $b$ yi bulalım.",
                "Soldan limit $f(1)$ e eşit olmalı: $1+a=3$, yani $a=2$.",
                "Sağdan limit $f(1)$ e eşit olmalı: $b+1=3$, yani $b=2$."),
        ]},
        {"baslik": "Mutlak değer fonksiyonu", "icerik": [
            "$|x|$ fonksiyonunun grafiği sıfırda sivri bir köşe yapar ama kopmaz. Soldan ve sağdan limitler de fonksiyonun değeri de $0$ dır; bu yüzden mutlak değer fonksiyonu her yerde süreklidir.",
            "Sürekli bir fonksiyonun mutlak değeri de süreklidir: $|x^2-4|$ gibi ifadeler grafikte köşeler oluştursa da hiçbir yerde kopmaz. Köşeli noktalarda türev yoktur ama süreklilik vardır; bu ayrım türev konusunda önem kazanır.",
        ]},
        {"baslik": "Tam değer fonksiyonu", "icerik": [
            "$\\lfloor x \\rfloor$ fonksiyonu her tam sayıda bir birim sıçrar. Tam sayılarda soldan ve sağdan limitler farklı olduğu için bu noktalarda süreksizdir; tam sayı olmayan noktalarda ise sabit olduğu için süreklidir.",
            ornek(
                "$\\lfloor x \\rfloor$ fonksiyonu $(0, 5)$ aralığında verilsin.",
                "Fonksiyonun bu aralıkta kaç noktada süreksiz olduğunu bulalım.",
                "Aralıktaki tam sayılar $1$, $2$, $3$ ve $4$ tür.",
                "Fonksiyon bu dört noktada süreksizdir; örneğin $x=2.5$ te süreklidir."),
        ]},
        {"baslik": "Aralıkta süreklilik", "icerik": [
            "Bir fonksiyon açık bir aralığın her noktasında sürekliyse o aralıkta süreklidir. Kapalı bir $[a, b]$ aralığında süreklilik için iç noktalarda süreklilik ve uç noktalarda tek yönlü süreklilik istenir: $a$ da sağdan, $b$ de soldan limit fonksiyon değerine eşit olmalıdır.",
            "Örneğin $\\sqrt{x}$ fonksiyonu $[0, \\infty)$ aralığında süreklidir. Sıfırın solunda tanımlı olmadığı için orada yalnızca sağdan limite bakılır ve $\\lim_{x \\to 0^+}\\sqrt{x}=0=\\sqrt{0}$ olduğu için uç noktada da süreklilik sağlanır.",
        ]},
        {"baslik": "Ara değer teoremi", "icerik": [
            "Kapalı bir $[a, b]$ aralığında sürekli bir fonksiyon, $f(a)$ ile $f(b)$ arasındaki her değeri en az bir kez alır. Özellikle $f(a)$ ile $f(b)$ ters işaretliyse fonksiyon aralıkta en az bir kez sıfır olur; yani denklemin bu aralıkta kökü vardır.",
            ornek(
                "$f(x)=x^3+x-1$ fonksiyonu $[0, 1]$ aralığında verilsin.",
                "$f(x)=0$ denkleminin bu aralıkta kökü olup olmadığını inceleyelim.",
                "$f(0)=-1<0$ ve $f(1)=1>0$ dır; fonksiyon polinom olduğu için süreklidir.",
                "Ara değer teoremine göre $(0, 1)$ aralığında en az bir kök vardır."),
            "Teorem sürekliliğe dayanır. $\\dfrac{1}{x}$ fonksiyonu $[-1, 1]$ aralığında uçlarda ters işaretli değerler alır ama hiç sıfır olmaz; çünkü $x=0$ da süreksizdir.",
            hap("$[a, b]$ aralığında sürekli bir fonksiyonda $f(a)$ ile $f(b)$ ters işaretliyse bu aralıkta en az bir kök vardır."),
        ]},
        {"baslik": "Kökü yaklaşık bulmak", "icerik": [
            "Ara değer teoremi, kökün yerini adım adım daraltmak için de kullanılır. Aralık ikiye bölünür, işaret değişiminin olduğu yarı seçilir ve işlem tekrarlanır. Bu yönteme ikiye bölme yöntemi denir.",
            ornek(
                "Yine $f(x)=x^3+x-1$ fonksiyonu verilsin.",
                "Kökü daha dar bir aralığa yerleştirelim.",
                "$f(0.5)=-0.375<0$ olduğundan kök $(0.5, 1)$ aralığındadır.",
                "$f(0.75)=0.171875>0$ olduğundan kök $(0.5, 0.75)$ aralığındadır; gerçek kök yaklaşık $0.682$ dir."),
        ]},
        {"baslik": "En büyük ve en küçük değer", "icerik": [
            "Kapalı bir aralıkta sürekli olan her fonksiyon bu aralıkta bir en büyük ve bir en küçük değer alır. Bu sonuç, türevle en büyük ve en küçük değer bulma yönteminin güvencesidir.",
            ornek(
                "$f(x)=x^2$ fonksiyonu $[-1, 2]$ aralığında verilsin.",
                "En büyük ve en küçük değeri bulalım.",
                "En küçük değer $x=0$ da alınır ve $0$ dır.",
                "En büyük değer $x=2$ de alınır ve $4$ tür."),
            "Aralık kapalı değilse teorem geçerli olmayabilir: $\\dfrac{1}{x}$ fonksiyonu $(0, 1]$ aralığında süreklidir ama sıfıra yaklaşırken sınırsız büyüdüğü için en büyük değeri yoktur.",
        ]},
        {"baslik": "Günlük hayatta süreklilik", "icerik": [
            "Sıcaklık, bir aracın hızı ya da bir bitkinin boyu gibi nicelikler zamanla sürekli değişir; bir anda bir değerden diğerine atlamazlar. Bu yüzden sabah $10$ derece olan sıcaklık öğlen $20$ dereceyse, arada bir anda tam olarak $15$ derece olmuştur; bu, ara değer teoreminin günlük bir örneğidir.",
            "Taksi ücreti, kargo tarifesi ya da bir sınavdaki not baremi ise basamaklıdır ve belirli eşiklerde sıçrar. Bu nicelikler süreksiz fonksiyonlarla modellenir ve eşiklerin iki yanında farklı değerler alır.",
            hap("Boyun $1.50$ metreden $1.60$ metreye çıktıysa arada bir gün tam $1.55$ metre olmuşsundur.", "Boy zamanla sürekli değiştiği için arada kalan her değerden geçer; bu, ara değer teoreminin sonucudur.", gunluk=True),
        ]},
        {"baslik": "Süreklilik ve türev", "icerik": [
            "Bir fonksiyonun bir noktada türevi varsa o noktada mutlaka süreklidir. Tersi doğru değildir: $|x|$ fonksiyonu sıfırda süreklidir ama köşe yaptığı için orada türevi yoktur.",
            "Bu yüzden süreklilik, türevin var olması için gerekli ama yeterli olmayan bir koşuldur. Bir noktada süreksiz olan fonksiyonun o noktada türevi olamaz; türev sorularında önce süreklilik kontrol edilir. Türevin tanımı <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sınavda süreklilik", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) süreklilik; grafikten süreksiz noktaları bulma, parçalı fonksiyonu sürekli yapan parametre, rasyonel fonksiyonların süreksiz noktaları ve her yerde sürekli olma koşulu biçiminde karşına çıkabilir.",
                "Ara değer teoremi de kök varlığı sorularında kullanılır."),
            "Süreklilik sorusunda önce şüpheli noktaları belirle: parçalı fonksiyonlarda kritik noktalar, rasyonel fonksiyonlarda paydanın kökleri, tam değerde tam sayılar. Diğer noktalarda fonksiyon zaten süreklidir; üç koşulu yalnızca şüpheli noktalarda kontrol et.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Limit varsa sürekli sanmak", "Limit değere eşit olmalı"],
                ["Tanımsız noktada sürekli demek", "Önce tanımlı olmalı"],
                ["Parçalı fonksiyonda $f(a)$ yı kontrol etmemek", "Üç değer eşit olmalı"],
                ["Köşeli grafiği süreksiz sanmak", "$|x|$ süreklidir"],
                ["Payda sıfırken sürekli demek", "Rasyonel fonksiyon orada süreksiz"],
                ["Ara değer teoremini süreksiz fonksiyona uygulamak", "Süreklilik şart"],
            ]),
            "Hataların çoğu üç koşuldan birini atlamaktan doğar. Süreklilik sorusunda koşulları sırayla yazmak, hangisinin bozulduğunu ve süreksizliğin türünü hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Süreklilik nedir?",
         "Bir fonksiyonun grafiğinin bir noktada kopmaması, sıçramaması ve boşluk bırakmamasıdır. Limit ile fonksiyon değerinin eşit olmasıyla tanımlanır."),
        ("Bir fonksiyon bir noktada ne zaman süreklidir?",
         "Fonksiyon o noktada tanımlıysa, limiti varsa ve limit fonksiyonun değerine eşitse süreklidir."),
        ("Kaldırılabilir süreksizlik nedir?",
         "Limitin var olduğu ama fonksiyonun tanımsız ya da farklı değerli olduğu süreksizliktir. Fonksiyon değeri limit olarak tanımlanırsa süreksizlik kalkar."),
        ("Polinomlar sürekli midir?",
         "Evet, polinomlar bütün gerçek sayılarda süreklidir. Rasyonel fonksiyonlar ise yalnızca paydayı sıfır yapan noktalarda süreksizdir."),
        ("Ara değer teoremi nedir?",
         "Kapalı bir aralıkta sürekli bir fonksiyon, uç değerleri arasındaki her değeri alır. Uçlarda ters işaretli değerler varsa aralıkta en az bir kök vardır."),
        ("Mutlak değer fonksiyonu sürekli midir?",
         "Evet. Grafik sıfırda köşe yapar ama kopmaz; bu yüzden süreklidir. Ancak o noktada türevi yoktur."),
        ("Tam değer fonksiyonu nerelerde süreksizdir?",
         "Tam değer fonksiyonu her tam sayıda bir birim sıçradığı için tam sayılarda süreksizdir. Tam sayı olmayan noktalarda sabit olduğu için süreklidir."),
        ("Türevli bir fonksiyon sürekli midir?",
         "Evet. Bir noktada türevi olan fonksiyon o noktada mutlaka süreklidir. Tersi doğru değildir; mutlak değer fonksiyonu sıfırda süreklidir ama türevi yoktur."),
    ],
    "kontrol": [
        "Sürekliliğin sezgisel anlamını açıklayabiliyorum.",
        "Bir noktada süreklilik için üç koşulu kontrol edebiliyorum.",
        "Kaldırılabilir, sıçrama ve sonsuz süreksizliği ayırt edebiliyorum.",
        "Kaldırılabilir süreksizliği gidermek için fonksiyonu yeniden tanımlayabiliyorum.",
        "Sürekli fonksiyon ailelerini ve sürekli oldukları yerleri biliyorum.",
        "Rasyonel fonksiyonların süreksiz noktalarını bulabiliyorum.",
        "Her yerde süreklilik için parametre koşulunu bulabiliyorum.",
        "Parçalı fonksiyonu sürekli yapan parametreleri bulabiliyorum.",
        "Aralıkta sürekliliği ve uç noktaları inceleyebiliyorum.",
        "Ara değer teoremiyle kök varlığını gösterebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["limit-konu-anlatimi", "sagdan-soldan-limit", "turev-konu-anlatimi"],
}
