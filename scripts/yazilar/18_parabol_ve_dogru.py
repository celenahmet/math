# scripts/yazilar/18_parabol_ve_dogru.py — Parabol ve Dogru (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import math, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "parabol-ve-dogru",
    "baslik": "Parabol ve Doğrunun Birbirine Göre Durumları",
    "aciklama": "Parabol ile doğru nasıl kesişir? Kesişme, teğetlik ve kesişmeme, parametreli sorular, teğet noktası, kesişim noktaları ve eşitsizlik yorumu; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["AYT"],
    "kapak": "parabol-ve-dogru",
    "kapak_alt": "Parabol ve doğru: iki noktada kesişme, teğet olma ve kesişmeme durumlarını üç panelde karşılaştıran iki öğrenci",
    "ozet": "Bir parabol ile bir doğru iki noktada kesişebilir, tek noktada değebilir ya da hiç kesişmeyebilir. Hangi durumun geçerli olduğu, iki denklemin eşitlenmesiyle oluşan ikinci dereceden denklemin diskriminantından okunur. Bu yazıda bu yöntemi ve üç durumu, parametreli kesişme ve teğetlik sorularını, teğet noktasını bulmayı, belirli eğimli ve belirli bir noktadan geçen teğetleri, kesişim noktalarının orta noktasını, iki parabolün kesişimini ve grafik üzerinden eşitsizlik yorumunu çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Parabol ile doğru nasıl karşılaştırılır?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için parabolün yapısını ve diskriminantı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/parabol-konu-anlatimi/\">Parabol Konu Anlatımı</a> ve <a href=\"/blog/diskriminant-delta/\">Diskriminant Nedir? Delta Nasıl Hesaplanır?</a> yazılarına göz at."),
            "$y=ax^2+bx+c$ parabolü ile $y=mx+n$ doğrusunun ortak noktaları, iki denklemi birlikte sağlayan noktalardır. Bir ortak noktada iki fonksiyon aynı değeri alır; bu yüzden denklemler eşitlenir:",
            "$$ax^2+bx+c=mx+n$$",
            "Her şey bir tarafa toplanınca $ax^2+(b-m)x+(c-n)=0$ biçiminde ikinci dereceden bir denklem elde edilir. Bu denklemin her gerçek kökü, bir ortak noktanın yatay koordinatıdır. Kök sayısı ortak nokta sayısını, kökler de ortak noktaların yerini verir. Doğru yerine başka bir parabol verilse de yöntem değişmez; yalnızca eşitlemeden çıkan denklemin katsayıları farklı olur.",
            hap("Ortak noktalar için denklemler eşitlenir.",
                "Oluşan denklemin diskriminantı durumu belirler."),
        ]},
        {"baslik": "Üç durum", "icerik": [
            "Eşitlemeden elde edilen denklemin diskriminantı, parabol ile doğrunun durumunu tek başına belirler. Kapaktaki üç panel bu üç durumu yan yana gösteriyor.",
            tablo(["Diskriminant", "Ortak nokta", "Durum"], [
                ["$\\Delta>0$", "İki", "Doğru parabolü iki noktada keser"],
                ["$\\Delta=0$", "Bir", "Doğru parabole teğettir"],
                ["$\\Delta<0$", "Yok", "Doğru ile parabol kesişmez"],
            ]),
            "Teğet durumunda doğru parabole tek bir noktada değer ve o noktada parabolün iki yanına geçmez. Dikey olmayan bir doğrunun parabolle tek ortak noktası varsa bu nokta her zaman bir teğet noktasıdır. Bu yüzden teğetlik sorularında \"tek ortak nokta\" ile \"teğet\" ifadeleri aynı anlamda kullanılır.",
        ]},
        {"baslik": "İki noktada kesişme", "icerik": [
            "Diskriminant pozitifse denklemin iki farklı kökü vardır ve doğru parabolü iki noktada keser. Noktaların dikey koordinatları, bulunan kökler doğru denkleminde ya da parabol denkleminde yerine yazılarak bulunur.",
            ornek(
                "$y=x^2$ parabolü ile $y=x+2$ doğrusu verilsin.",
                "Ortak noktaları bulalım.",
                "$x^2=x+2$, yani $x^2-x-2=0$. $\\Delta=1+8=9>0$.",
                "$(x-2)(x+1)=0$; $x=2$ için $y=4$, $x=-1$ için $y=1$. Ortak noktalar $(-1, 1)$ ve $(2, 4)$ tür."),
            koordinat_grafik("y = x² parabolü ile y = x + 2 doğrusu iki noktada kesişir", [("y = x²", lambda x: x * x), ("y = x + 2", lambda x: x + 2)], (-3, 4), (-1, 6),
                             noktalar=[(-1, 1, "(−1, 1)", True), (2, 4, "(2, 4)", True)]),
        ]},
        {"baslik": "Teğet olma", "icerik": [
            "Diskriminant sıfırsa denklemin çakışık bir kökü vardır ve doğru parabole tek bir noktada değer. Bu nokta teğet noktasıdır ve yatay koordinatı çakışık köktür.",
            ornek(
                "$y=x^2$ parabolü ile $y=2x-1$ doğrusu verilsin.",
                "Durumu ve ortak noktayı bulalım.",
                "$x^2=2x-1$, yani $x^2-2x+1=0$. $\\Delta=4-4=0$.",
                "$(x-1)^2=0$; $x=1$ ve $y=1$. Doğru parabole $(1, 1)$ noktasında teğettir."),
            koordinat_grafik("y = 2x − 1 doğrusu y = x² parabolüne (1, 1) noktasında teğettir", [("y = x²", lambda x: x * x), ("y = 2x − 1", lambda x: 2 * x - 1)], (-2, 3), (-2, 5),
                             noktalar=[(1, 1, "(1, 1)", True)]),
        ]},
        {"baslik": "Kesişmeme", "icerik": [
            "Diskriminant negatifse denklemin gerçek kökü yoktur ve doğru ile parabol hiçbir noktada buluşmaz. Kolları yukarı bakan bir parabol için bu, doğrunun parabolün tamamen altında kaldığı anlamına gelir.",
            ornek(
                "$y=x^2$ parabolü ile $y=x-1$ doğrusu verilsin.",
                "Durumu inceleyelim.",
                "$x^2=x-1$, yani $x^2-x+1=0$. $\\Delta=1-4=-3<0$.",
                "Ortak nokta yoktur; doğru parabolün altında kalır."),
            "Bu durumda iki eğri arasındaki dikey uzaklık hiçbir yerde sıfır olmaz. Parabol her $x$ için doğrunun üstünde kaldığı için $x^2>x-1$ eşitsizliği bütün gerçek sayılar için doğrudur.",
        ]},
        {"baslik": "Aynı eğimli üç doğru", "icerik": [
            "Eğimleri aynı, yalnızca yükseklikleri farklı doğrular aynı parabolle karşılaştırılınca üç durumun nasıl birbirine geçtiği açıkça görülür. Doğru aşağı indikçe iki kesişim noktası birbirine yaklaşır, teğet noktasında birleşir ve sonra kaybolur.",
            koordinat_grafik("y = x² parabolü ile aynı eğimli üç doğru", [("y = x²", lambda x: x * x), ("y = 2x (Δ > 0)", lambda x: 2 * x), ("y = 2x − 1 (Δ = 0)", lambda x: 2 * x - 1), ("y = 2x − 2 (Δ < 0)", lambda x: 2 * x - 2)],
                             (-2, 4), (-3, 6), noktalar=[(0, 0, "", True), (2, 4, "", True), (1, 1, "", True)]),
            tablo(["Doğru", "Eşitlemeden çıkan denklem", "$\\Delta$"], [
                ["$y=2x$", "$x^2-2x=0$", "$4$"],
                ["$y=2x-1$", "$x^2-2x+1=0$", "$0$"],
                ["$y=2x-2$", "$x^2-2x+2=0$", "$-4$"],
            ]),
        ]},
        {"baslik": "İki noktada kesme koşulundan parametre", "icerik": [
            "Doğrunun parabolü iki farklı noktada kesmesi isteniyorsa koşul $\\Delta>0$ dır ve parametre için bir eşitsizlik elde edilir. Eşitsizliğin çözümü, parametrenin alabileceği bütün değerleri bir aralık olarak verir.",
            ornek(
                "$y=x^2+2x+3$ parabolü ile $y=x+k$ doğrusu iki farklı noktada kesişiyor.",
                "$k$ nın alabileceği değerleri bulalım.",
                "$x^2+x+3-k=0$ ve $\\Delta=1-4(3-k)=4k-11>0$.",
                "$k>\\dfrac{11}{4}$."),
        ]},
        {"baslik": "Bir kesişim noktası verildiğinde", "icerik": [
            "Kesişim noktalarından biri biliniyorsa bu nokta iki denklemi de sağlar ve parametre hemen bulunur. Diğer kesişim noktası, eşitlemeden çıkan denklemin ikinci kökü olarak hesaplanır.",
            ornek(
                "$y=x^2$ parabolü ile $y=mx+2$ doğrusu $x=2$ noktasında kesişiyor.",
                "$m$ yi ve diğer kesişim noktasını bulalım.",
                "$x=2$ için parabolde $y=4$; doğruda $4=2m+2$, yani $m=1$.",
                "$x^2=x+2$ denkleminin diğer kökü $-1$ dir; diğer kesişim noktası $(-1, 1)$ dir."),
            "Diğer kök, kökler çarpımından da bulunur: $x^2-x-2=0$ denkleminde çarpım $-2$ dir ve bir kök $2$ olduğu için diğeri $-1$ dir. Bu yol ikinci kökü denklemi çözmeden verir.",
        ]},
        {"baslik": "Teğet olma koşulundan parametre", "icerik": [
            "Doğru ya da parabol denkleminde bir parametre varsa teğetlik koşulu $\\Delta=0$ parametre için bir denklem verir. Parametre ikinci dereceden geçiyorsa genellikle iki değer bulunur; bunlar parabole iki farklı teğet doğruya karşılık gelir.",
            ornek(
                "$y=x^2+3$ parabolü ile $y=mx$ doğrusu teğettir.",
                "$m$ yi bulalım.",
                "$x^2+3=mx$, yani $x^2-mx+3=0$. $\\Delta=m^2-12=0$.",
                "$m=2\\sqrt{3}$ ya da $m=-2\\sqrt{3}$. Başlangıç noktasından parabole iki teğet çizilir."),
        ]},
        {"baslik": "Yatay doğrular ve tepe noktası", "icerik": [
            "$y=k$ biçimindeki yatay doğrular için durum tepe noktasının yüksekliğiyle belirlenir. Kolları yukarı bakan bir parabolde doğru tepe noktasının üstündeyse iki noktada keser, tepe noktasından geçiyorsa teğettir, altındaysa kesişmez.",
            ornek(
                "$y=x^2-4x+5$ parabolü ile $y=k$ doğrusu verilsin.",
                "Doğrunun parabolü kesmediği $k$ değerlerini bulalım.",
                "$x^2-4x+5-k=0$ ve $\\Delta=16-4(5-k)=4k-4<0$; yani $k<1$.",
                "Tepe noktası $(2, 1)$ dir: yükseklik $1$ in altındaki yatay doğrular parabolü kesmez."),
            tablo(["$k$", "Ortak nokta"], [
                ["$k>1$", "İki"],
                ["$k=1$", "Bir, tepe noktasında teğet"],
                ["$k<1$", "Yok"],
            ]),
        ]},
        {"baslik": "Kolları aşağı bakan parabol ve yatay doğrular", "icerik": [
            "Kollar aşağı bakıyorsa durum tersine döner: tepe noktası en yüksek noktadır ve yatay doğru tepe noktasının altındaysa parabolü iki noktada keser, üstündeyse kesişmez.",
            ornek(
                "$y=-x^2+4x$ parabolü ile $y=k$ doğrusu verilsin.",
                "Kesişim sayısını $k$ ya göre inceleyelim.",
                "Tepe noktası $(2, 4)$ tür; en büyük değer $4$ tür.",
                "$k<4$ ise iki nokta, $k=4$ ise tepe noktasında teğet, $k>4$ ise ortak nokta yoktur."),
        ]},
        {"baslik": "Mutlak değerli parabol ve yatay doğrular", "icerik": [
            "Mutlak değerli bir parabolün grafiği, parabolün eksenin altında kalan kısmının yukarı yansıtılmasıyla oluşur. Bu grafik yatay doğrularla parabolden daha fazla noktada kesişebilir, çünkü yansıyan kısım yeni bir tepe oluşturur.",
            ornek(
                "$y=|x^2-4|$ grafiği ile $y=k$ doğrusu verilsin.",
                "Kesişim sayısını $k$ ya göre inceleyelim.",
                "Yansıyan kısmın tepesi $(0, 4)$ tür; grafik $x=\\pm 2$ de eksene değer.",
                "$k<0$ ise yok, $k=0$ ise iki, $0<k<4$ ise dört, $k=4$ ise üç, $k>4$ ise iki ortak nokta vardır."),
        ]},
        {"baslik": "Dikey doğrular", "icerik": [
            "$x=a$ biçimindeki dikey doğrular parabolü her zaman tam olarak bir noktada keser, çünkü parabol bir fonksiyon grafiğidir ve her $x$ için tek bir $y$ değeri vardır. Kesişim noktası $(a, f(a))$ dır.",
            "Dikey bir doğrunun parabolle tek ortak noktası olsa da bu doğru teğet değildir: parabolün iki yanına geçer. Teğetlik ölçütü olarak diskriminant yalnızca dikey olmayan doğrular için kullanılır; dikey doğrular bu yöntemin dışında kalır.",
        ]},
        {"baslik": "Teğet noktasını bulmak", "icerik": [
            "Teğetlik koşulundan parametre bulunduktan sonra teğet noktası, çakışık kök formülüyle bulunur: eşitlemeden çıkan denklemin çakışık kökü $-\\dfrac{B}{2A}$ dir. Bu değer parabol ya da doğru denkleminde yerine yazılarak noktanın dikey koordinatı hesaplanır.",
            ornek(
                "$y=x^2-2x+3$ parabolü ile $y=2x+k$ doğrusu teğettir.",
                "$k$ yı ve teğet noktasını bulalım.",
                "$x^2-4x+3-k=0$ ve $\\Delta=16-4(3-k)=4+4k=0$; $k=-1$.",
                "Çakışık kök $x=2$; $y=2 \\cdot 2-1=3$. Teğet noktası $(2, 3)$ tür."),
            "Bulunan noktanın hem parabolde hem doğruda olduğu kontrol edilmelidir: parabolde $4-4+3=3$, doğruda $4-1=3$ bulunur. İki değerin eşit çıkması, teğet noktasının doğru bulunduğunu gösterir.",
        ]},
        {"baslik": "Belirli eğimli teğet", "icerik": [
            "Eğimi belli olan bir teğet isteniyorsa doğru $y=mx+n$ biçiminde yazılır ve yalnızca $n$ bilinmez. Teğetlik koşulu $n$ yi verir.",
            ornek(
                "$y=x^2$ parabolüne eğimi $4$ olan teğet istensin.",
                "Teğet doğrusunu ve teğet noktasını bulalım.",
                "$x^2=4x+n$, yani $x^2-4x-n=0$. $\\Delta=16+4n=0$; $n=-4$.",
                "Teğet $y=4x-4$ tür; çakışık kök $x=2$, teğet noktası $(2, 4)$ tür."),
            "Aynı hesap genel olarak yapılırsa $y=x^2$ parabolüne eğimi $m$ olan teğetin $x=\\dfrac{m}{2}$ noktasında değdiği görülür. Türev konusunda bu sonuç çok daha kısa bir yoldan elde edilir.",
        ]},
        {"baslik": "Bir noktadan çizilen teğetler", "icerik": [
            "Parabolün dışındaki bir noktadan parabole iki teğet çizilebilir. Doğru o noktadan geçecek biçimde eğim cinsinden yazılır ve teğetlik koşulu eğim için ikinci dereceden bir denklem verir.",
            ornek(
                "$(0, -1)$ noktasından $y=x^2$ parabolüne çizilen teğetler istensin.",
                "Teğetlerin eğimlerini ve teğet noktalarını bulalım.",
                "Doğru $y=mx-1$ olsun: $x^2-mx+1=0$ ve $\\Delta=m^2-4=0$; $m=2$ ya da $m=-2$.",
                "$m=2$ için teğet noktası $(1, 1)$, $m=-2$ için $(-1, 1)$ dir."),
            koordinat_grafik("(0, −1) noktasından y = x² parabolüne çizilen iki teğet", [("y = x²", lambda x: x * x), ("y = 2x − 1", lambda x: 2 * x - 1), ("y = −2x − 1", lambda x: -2 * x - 1)],
                             (-3, 3), (-2, 5), noktalar=[(0, -1, "(0, −1)", True), (1, 1, "(1, 1)", True), (-1, 1, "(−1, 1)", True)]),
        ]},
        {"baslik": "Kesişim noktalarının orta noktası", "icerik": [
            "Doğru parabolü iki noktada kesiyorsa bu noktaların yatay koordinatları eşitlemeden çıkan denklemin kökleridir. Kökler toplamı bulunarak orta noktanın yatay koordinatı, kesişim noktaları hesaplanmadan bulunur.",
            ornek(
                "$y=x^2-3x+1$ parabolü ile $y=x+k$ doğrusu iki noktada kesişiyor.",
                "Kesişim noktalarını birleştiren parçanın orta noktasının yatay koordinatını bulalım.",
                "$x^2-4x+1-k=0$; kökler toplamı $4$ tür.",
                "Orta noktanın yatay koordinatı $\\dfrac{4}{2}=2$ dir ve $k$ ya bağlı değildir."),
            "Sonucun $k$ dan bağımsız olması ilginçtir: aynı eğimli bütün kesen doğruların parabolde ayırdığı parçaların orta noktaları aynı dikey doğru üzerindedir. Kökler toplamının ayrıntısı <a href=\"/blog/kokler-toplami-carpimi/\">Kökler Toplamı ve Kökler Çarpımı Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Kesen doğrunun eğimini bulmak", "icerik": [
            "Kesişim noktalarının yatay koordinatlarının toplamı, eşitlemeden çıkan denklemin kökler toplamıdır ve doğrunun eğimine bağlıdır. Bu toplam verilmişse eğim tek adımda bulunur.",
            ornek(
                "$(0, 2)$ noktasından geçen bir doğru $y=x^2$ parabolünü iki noktada kesiyor ve bu noktaların yatay koordinatlarının toplamı $3$ tür.",
                "Doğrunun eğimini bulalım.",
                "Doğru $y=mx+2$ olsun: $x^2-mx-2=0$. Kökler toplamı $m$ dir.",
                "$m=3$; doğru $y=3x+2$ dir. Diskriminant $9+8=17>0$ olduğu için gerçekten iki kesişim noktası vardır."),
        ]},
        {"baslik": "Kesişim noktaları arasındaki uzaklık", "icerik": [
            "Kesişim noktaları bulunduktan sonra aralarındaki uzaklık iki nokta arasındaki uzaklık formülüyle hesaplanır. Yatay ve dikey farkların kareleri toplanıp karekök alınır.",
            ornek(
                "$y=x^2$ parabolü ile $y=x+2$ doğrusunun kesişim noktaları $(-1, 1)$ ve $(2, 4)$ tür.",
                "Bu iki nokta arasındaki uzaklığı bulalım.",
                "Yatay fark $3$, dikey fark $3$ tür.",
                "Uzaklık $\\sqrt{9+9}=3\\sqrt{2}$ dir."),
            "Kesişim noktaları bir doğru üzerinde olduğu için dikey fark, yatay farkın doğrunun eğimiyle çarpımıdır. Eğimi $1$ olan bu doğruda iki fark eşit çıkmıştır; eğim $m$ olsaydı uzaklık yatay farkın $\\sqrt{1+m^2}$ katı olurdu.",
        ]},
        {"baslik": "İki parabolün kesişimi", "icerik": [
            "Aynı yöntem iki parabol için de geçerlidir: denklemler eşitlenir ve oluşan denklem çözülür. Baş katsayılar farklıysa denklem yine ikinci derecedendir ve en fazla iki ortak nokta vardır.",
            ornek(
                "$y=x^2$ ve $y=-x^2+4x$ parabolleri verilsin.",
                "Ortak noktaları bulalım.",
                "$x^2=-x^2+4x$, yani $2x^2-4x=0$ ve $2x(x-2)=0$.",
                "Ortak noktalar $(0, 0)$ ve $(2, 4)$ tür."),
            "Baş katsayıları eşit iki parabol eşitlenince $x^2$ li terimler birbirini götürür ve birinci dereceden bir denklem kalır. Bu durumda iki parabolün en fazla bir ortak noktası vardır. Aralarındaki fark birinci dereceden bir ifade olduğu için ortak noktada işaret değiştirir; bu yüzden böyle iki parabol birbirine teğet olamaz, ortak noktada birbirini keser.",
        ]},
        {"baslik": "Eşitsizlik yorumu", "icerik": [
            "Parabol ile doğrunun durumu, eşitsizlik sorularının da grafik karşılığıdır. $f(x)>g(x)$ eşitsizliği, parabolün doğrunun üstünde kaldığı $x$ değerlerini sorar; bu değerler kesişim noktalarının dışında ya da arasında kalan aralıklardır.",
            ornek(
                "$x^2>x+2$ eşitsizliği verilsin.",
                "Çözüm kümesini grafik yorumuyla bulalım.",
                "Kesişim noktaları $x=-1$ ve $x=2$ dir.",
                "Parabol bu noktaların dışında doğrunun üstündedir: $x<-1$ ya da $x>2$."),
        ]},
        {"baslik": "En kısa dikey uzaklık", "icerik": [
            "Parabol ile doğru kesişmiyorsa aralarındaki dikey uzaklık her $x$ için pozitiftir ve bu uzaklık ikinci dereceden bir fonksiyondur. En kısa dikey uzaklık bu fonksiyonun tepe noktasında bulunur.",
            ornek(
                "$y=x^2+1$ parabolü ile $y=x$ doğrusu verilsin.",
                "Aralarındaki en kısa dikey uzaklığı bulalım.",
                "Dikey uzaklık $d(x)=x^2+1-x=x^2-x+1$ dir; diskriminantı negatif olduğu için her zaman pozitiftir.",
                "Tepe noktası $x=\\dfrac{1}{2}$; $d(\\dfrac{1}{2})=\\dfrac{1}{4}-\\dfrac{1}{2}+1=\\dfrac{3}{4}$."),
        ]},
        {"baslik": "Sınavda parabol ve doğru", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) parabol ve doğru; kesişme, teğet olma ve kesişmeme koşullarından parametre bulma, teğet noktasını hesaplama ve kesişim noktalarıyla ilgili sorular biçiminde karşına çıkabilir.",
                "Belirli bir noktadan geçen ya da belirli eğimli teğetler ve iki parabolün kesişimi de sorulabilir."),
            "Bu sorularda yöntem hiç değişmez: denklemleri eşitle, her şeyi bir tarafa topla ve diskriminanta bak. Soru kesişim noktalarının kendisini değil toplamını ya da orta noktasını istiyorsa kökler toplamı formülü kökleri bulmaktan çok daha hızlıdır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Eşitlemeden sonra terimleri bir tarafa toplamamak", "Önce standart biçime getirilir"],
                ["Teğetliği $\\Delta>0$ sanmak", "Teğetlik $\\Delta=0$"],
                ["Dikey doğruyu diskriminantla incelemek", "Dikey doğru her zaman bir noktada keser"],
                ["Teğet noktasının yalnız $x$ ini yazmak", "Nokta $(x, y)$ olarak verilir"],
                ["Kesişim sayısını kök sayısından ayrı düşünmek", "Kök sayısı ortak nokta sayısıdır"],
                ["İki parametre değerinden birini atmak", "İki teğet de geçerli olabilir"],
            ]),
            "Bu hataların çoğu, eşitlemeden sonra denklemin standart biçime getirilmemesinden doğar. $b-m$ ve $c-n$ katsayılarını dikkatle hesaplamak, sonraki bütün adımların doğruluğunu belirler.",
        ]},
    ],
    "sss": [
        ("Parabol ile doğrunun ortak noktaları nasıl bulunur?",
         "İki denklem eşitlenir ve bir tarafa toplanır. Oluşan ikinci dereceden denklemin kökleri ortak noktaların yatay koordinatlarıdır."),
        ("Doğru parabole ne zaman teğettir?",
         "Eşitlemeden çıkan denklemin diskriminantı sıfırsa doğru parabole tek bir noktada değer; bu durumda teğettir."),
        ("Doğru ile parabol ne zaman kesişmez?",
         "Eşitlemeden çıkan denklemin diskriminantı negatifse ortak nokta yoktur."),
        ("Teğet noktası nasıl bulunur?",
         "Teğetlik koşulundan parametre bulunur, sonra eşitlemeden çıkan denklemin çakışık kökü hesaplanır ve denklemde yerine yazılır."),
        ("Bir noktadan parabole kaç teğet çizilir?",
         "Parabolün dışındaki bir noktadan iki teğet çizilebilir. Eğim için kurulan denklemin iki kökü bu iki teğeti verir."),
        ("Dikey doğru parabole teğet olabilir mi?",
         "Hayır. Dikey doğru parabolü her zaman tek bir noktada keser ama parabolün iki yanına geçtiği için teğet değildir."),
        ("Kesişim noktalarının orta noktası nasıl bulunur?",
         "Eşitlemeden çıkan denklemin kökler toplamı ikiye bölünür. Orta noktanın yatay koordinatı kesişim noktaları bulunmadan hesaplanır."),
    ],
    "kontrol": [
        "Parabol ile doğrunun ortak noktalarını eşitleyerek bulabiliyorum.",
        "Diskriminanta göre üç durumu ayırt edebiliyorum.",
        "Kesişim noktalarının koordinatlarını hesaplayabiliyorum.",
        "Teğetlik koşulundan parametre bulabiliyorum.",
        "Yatay doğruların durumunu tepe noktasıyla yorumlayabiliyorum.",
        "Teğet noktasını bulabiliyorum.",
        "Belirli eğimli ve bir noktadan geçen teğetleri bulabiliyorum.",
        "Kesişim noktalarının orta noktasını kökler toplamıyla bulabiliyorum.",
        "İki parabolün ortak noktalarını bulabiliyorum.",
        "Parabol ve doğru eşitsizliklerini grafik yardımıyla yorumlayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["diskriminant-delta", "parabol-grafigi", "parabol-konu-anlatimi"],
}
