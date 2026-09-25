# scripts/yazilar/40_carpimin_turevi.py — Carpimin Turevi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "carpimin-turevi",
    "baslik": "Çarpımın Türevi Nasıl Alınır?",
    "aciklama": "Çarpımın türevi nasıl alınır? Çarpım kuralı, geometrik ve limitle ispat, üç çarpan, ortak paranteze alma, zincirle birlikte kullanım ve uygulamalar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "carpimin-turevi",
    "kapak_alt": "Çarpımın türevi: genişliği ve yüksekliği kaydırıcılarla değişen ahşap dikdörtgeni ayarlayan iki öğrenci",
    "ozet": "İki fonksiyonun çarpımının türevi, türevlerin çarpımı değildir. Çarpım kuralına göre birinci fonksiyonun türevi ikinciyle, birinci fonksiyon ikincinin türeviyle çarpılır ve bu iki terim toplanır. Bu yazıda türevlerin çarpımının neden yanlış olduğunu, çarpım kuralını ve onun dikdörtgen alanıyla geometrik ispatını, limitle ispatını, polinom, üstel, trigonometrik ve logaritmik çarpımlarda kullanımını, bir noktadaki türev değerini, üç çarpanlı kuralı, sonucu ortak paranteze almayı, zincir kuralıyla birlikte kullanımı, ikinci türevi ve değişim oranı uygulamalarını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Çarpımın türevi neden özel?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için temel türev kurallarını ve türevin tanımını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> ve <a href=\"/blog/turevin-tanimi/\">Türevin Tanımı ve Türev Nasıl Bulunur?</a> yazılarına göz at."),
            "Toplamın türevi türevlerin toplamıdır; bu yüzden çarpımın türevinin de türevlerin çarpımı olduğunu düşünmek doğaldır. Ancak bu düşünce yanlıştır. En basit örnekle görülür: $x \\cdot x=x^2$ dir ve türevi $2x$ tir; oysa iki çarpanın türevleri $1$ ve $1$ olduğu için çarpımları $1$ olur. İki sonuç farklıdır.",
            "Kapaktaki öğrenciler bir dikdörtgenin genişliğini ve yüksekliğini iki ayrı kaydırıcıyla değiştiriyor. Alan, genişlik ile yüksekliğin çarpımıdır; iki kenar birlikte değiştiğinde alandaki değişimin iki ayrı kaynağı vardır. Çarpım kuralı bu iki kaynağı ayrı ayrı hesaplayıp toplar.",
        ]},
        {"baslik": "Çarpım kuralı", "icerik": [
            "$f$ ve $g$ türevli iki fonksiyon olsun. Çarpımlarının türevi, birinci fonksiyonun türevi ile ikincinin çarpımına birinci fonksiyon ile ikincinin türevinin çarpımı eklenerek bulunur:",
            "$$(f \\cdot g)'=f' \\cdot g+f \\cdot g'$$",
            "Kural sözle şöyle hatırlanır: birincinin türevi çarpı ikinci, artı birinci çarpı ikincinin türevi. Toplamda iki terim vardır ve her terimde çarpanlardan yalnızca biri türevlenir.",
            hap("Çarpımın türevinde her seferinde tek bir çarpan türevlenir.",
                "İki terim toplanır; türevlerin çarpımı alınmaz."),
        ]},
        {"baslik": "Geometrik ispat: dikdörtgenin alanı", "icerik": [
            "Kenarları $f$ ve $g$ olan bir dikdörtgen düşün. Alanı $f \\cdot g$ dir. Kenarlar çok küçük $\\Delta f$ ve $\\Delta g$ miktarları kadar uzarsa yeni alan $(f+\\Delta f)(g+\\Delta g)$ olur.",
            "Alan artışı üç parçadan oluşur: yanda $\\Delta f \\cdot g$ lik bir şerit, üstte $f \\cdot \\Delta g$ lik bir şerit ve köşede $\\Delta f \\cdot \\Delta g$ lik küçük bir kare. Artış bir zaman aralığına bölünüp aralık sıfıra götürülünce iki şerit türevin iki terimine dönüşür; köşedeki kare ise iki küçük sayının çarpımı olduğu için ortadan kalkar.",
            "Bu yüzden çarpım kuralında iki terim vardır ve üçüncü bir terim yoktur. Kapaktaki düzenekte kaydırıcılar çok az hareket ettirildiğinde alana eklenen şeritler tam olarak bunlardır.",
        ]},
        {"baslik": "Limitle ispat", "icerik": [
            "Kural türevin tanımından da ispatlanır ve bu ispat geometrik fikrin cebirsel karşılığıdır. Tanımdaki farka $f(x+h)g(x)$ terimi bir kez eklenip bir kez çıkarılır; böylece fark iki parçaya ayrılır:",
            "$$f(x+h)\\left(g(x+h)-g(x)\\right)+g(x)\\left(f(x+h)-f(x)\\right)$$",
            "Her parça $h$ ye bölünüp limit alınınca birincisi $f(x)g'(x)$ e, ikincisi $g(x)f'(x)$ e gider. Burada $f$ türevli olduğu için sürekli olduğu ve $f(x+h)$ nin $f(x)$ e gittiği kullanılır. İki sonuç toplanınca çarpım kuralı elde edilir.",
        ]},
        {"baslik": "Sabitle çarpım bir özel durumdur", "icerik": [
            "Çarpanlardan biri sabitse çarpım kuralı, bilinen sabitle çarpım kuralına dönüşür. Sabitin türevi sıfır olduğu için birinci terim kaybolur: $(c \\cdot f)'=0 \\cdot f+c \\cdot f'=c \\cdot f'$.",
            "Bu gözlem, çarpım kuralının diğer kurallarla çelişmediğini gösterir. Genel bir kural, özel durumlarda daha önce öğrenilen sonuçları vermelidir; çarpım kuralı bu sınavı geçer.",
        ]},
        {"baslik": "Kuvvet kuralı çarpımdan çıkar", "icerik": [
            "Çarpım kuralı çok sayıda çarpana genellenir: her terimde bir çarpan türevlenir ve bütün terimler toplanır. $x^n$ yi $n$ tane $x$ in çarpımı olarak düşünürsek her terim $x^{n-1}$ olur ve $n$ tane terim vardır.",
            "Böylece $(x^n)'=n x^{n-1}$ sonucu yeniden elde edilir. Örneğin $x^3=x \\cdot x \\cdot x$ için üç terimin her biri $x^2$ dir ve toplam $3x^2$ olur. Kuvvet kuralı, çarpım kuralının en sık kullanılan sonucudur.",
        ]},
        {"baslik": "İlk örnek: kontrol", "icerik": [
            "Kuralı açılabilen bir çarpımla denemek, doğru uygulandığını görmenin en iyi yoludur. Aynı fonksiyonun türevi iki yoldan bulunur ve sonuçlar karşılaştırılır.",
            ornek(
                "$h(x)=(2x+1)(x^2-3)$ fonksiyonu verilsin.",
                "Türevini çarpım kuralıyla bulup açarak kontrol edelim.",
                "Çarpım kuralı: $2(x^2-3)+(2x+1)(2x)=6x^2+2x-6$ olur.",
                "Açarak: $h(x)=2x^3+x^2-6x-3$ ve $h'(x)=6x^2+2x-6$; iki sonuç aynıdır."),
            "Polinom çarpımlarında açmak çoğu zaman daha kısadır. Çarpım kuralı ise açılması zor ya da imkânsız olan çarpımlarda, örneğin bir polinomla bir üstel ya da trigonometrik fonksiyonun çarpımında vazgeçilmezdir.",
        ]},
        {"baslik": "Üstel fonksiyonla çarpım", "icerik": [
            "$e^x$ in türevi kendisi olduğu için, bir polinomla $e^x$ in çarpımının türevinde $e^x$ her iki terimde de görünür ve ortak paranteze alınır.",
            ornek(
                "$h(x)=x^3 e^x$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "$f=x^3$, $g=e^x$: $h'(x)=3x^2 e^x+x^3 e^x$ olur.",
                "Ortak çarpan alınınca $h'(x)=x^2 e^x(x+3)$ olur."),
            "Ortak paranteze alınmış biçim, türevin sıfır olduğu noktaları hemen gösterir: $x=0$ ya da $x=-3$. Çünkü $e^x$ hiçbir zaman sıfır olmaz.",
            hap("Polinomla $e^x$ çarpımının türevinde $e^x$ ortak paranteze alınır: $(x^n e^x)'=e^x(nx^{n-1}+x^n)$."),
        ]},
        {"baslik": "Sıfırları bulmak", "icerik": [
            "Çarpım kuralıyla elde edilen türev sadeleştirilip çarpanlarına ayrılırsa, türevin sıfır olduğu yerler yani yatay teğetli noktalar kolayca bulunur.",
            ornek(
                "$h(x)=x e^x$ fonksiyonu verilsin.",
                "Türevini ve türevin sıfır olduğu noktayı bulalım.",
                "$h'(x)=e^x+x e^x=e^x(1+x)$ olur.",
                "$e^x$ pozitif olduğu için türev yalnızca $x=-1$ de sıfırdır; bu noktada teğet yataydır."),
        ]},
        {"baslik": "Trigonometrik çarpım", "icerik": [
            "Trigonometrik fonksiyonların çarpımında da kural aynıdır. Sonuç çoğu zaman trigonometrik özdeşliklerle sadeleşir; bu yüzden türevi aldıktan sonra bilinen bir formüle benzeyip benzemediğine bakmak yararlıdır.",
            ornek(
                "$h(x)=\\sin x \\cos x$ fonksiyonu verilsin.",
                "Türevini bulalım ve sadeleştirelim.",
                "$h'(x)=\\cos x \\cdot \\cos x+\\sin x \\cdot (-\\sin x)=\\cos^2 x-\\sin^2 x$ olur.",
                "İki kat açı formülüyle $h'(x)=\\cos 2x$ bulunur."),
            "Sonuç başka bir yoldan da doğrulanır: $\\sin x \\cos x=\\dfrac{1}{2}\\sin 2x$ olduğundan türev $\\dfrac{1}{2} \\cdot 2\\cos 2x=\\cos 2x$ tir. Formülün ayrıntısı için <a href=\"/blog/iki-kat-yarim-aci/\">İki Kat Açı ve Yarım Açı Formülleri</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Negatif üslü üstel çarpım", "icerik": [
            "Üssü negatif olan üstel fonksiyonların türevinde zincir kuralı gereği bir eksi işaret ortaya çıkar. Çarpım kuralıyla birleşince türev, ortak paranteze alınarak işaret incelemesine hazır hâle getirilir.",
            ornek(
                "$h(x)=x^2 e^{-x}$ fonksiyonu verilsin.",
                "Türevini ve türevin sıfır olduğu noktaları bulalım.",
                "$h'(x)=2x e^{-x}+x^2 \\cdot (-e^{-x})=x e^{-x}(2-x)$ olur.",
                "Türev $x=0$ ve $x=2$ de sıfırdır."),
        ]},
        {"baslik": "Polinom ve kosinüs", "icerik": [
            "Kosinüsün türevinde eksi işaret bulunduğu için polinom ile kosinüsün çarpımında ikinci terim eksiyle yazılır. İşaret hatası bu tür sorulardaki en yaygın hatadır.",
            ornek(
                "$h(x)=x\\cos x$ fonksiyonu verilsin.",
                "Türevini ve $h'(\\pi)$ değerini bulalım.",
                "$h'(x)=\\cos x-x\\sin x$ olur.",
                "$h'(\\pi)=-1-\\pi \\cdot 0=-1$ bulunur."),
        ]},
        {"baslik": "Logaritmik çarpım", "icerik": [
            "Logaritma bir polinomla çarpıldığında türevde logaritmanın türevi olan $\\dfrac{1}{x}$ polinomla sadeleşir. Bu yüzden sonuç çoğu zaman basit bir ifadeye iner. Logaritmanın tanım kümesi gereği bu tür fonksiyonlar yalnızca pozitif $x$ değerlerinde incelenir.",
            ornek(
                "$h(x)=x \\ln x$ fonksiyonu verilsin, $x>0$.",
                "Türevini ve türevin sıfır olduğu noktayı bulalım.",
                "$h'(x)=1 \\cdot \\ln x+x \\cdot \\dfrac{1}{x}=\\ln x+1$ olur.",
                "$\\ln x=-1$ ise $x=\\dfrac{1}{e}$ bulunur; türev bu noktada sıfırdır."),
        ]},
        {"baslik": "Köklü çarpım", "icerik": [
            "Kök içeren çarpımlarda kök önce üslü yazılır, sonra çarpım kuralı uygulanır; karekökün türevi $\\dfrac{1}{2\\sqrt{x}}$ olarak kullanılır. Sonucu tek bir kesir olarak yazmak için ortak payda alınır.",
            ornek(
                "$h(x)=\\sqrt{x}(x-1)$ fonksiyonu verilsin.",
                "Türevini ve $h'(1)$ değerini bulalım.",
                "$h'(x)=\\dfrac{1}{2\\sqrt{x}}(x-1)+\\sqrt{x}$ olur; ortak paydayla $\\dfrac{3x-1}{2\\sqrt{x}}$ bulunur.",
                "$h'(1)=\\dfrac{2}{2}=1$ olur."),
        ]},
        {"baslik": "Bir noktadaki türev değeri", "icerik": [
            "Fonksiyonların kendileri değil yalnızca bir noktadaki değerleri ve türev değerleri verilebilir. Çarpım kuralı bu değerlerle doğrudan uygulanır; fonksiyonların formülü bilinmese de çarpımın o noktadaki türevi bulunur.",
            ornek(
                "$f(2)=3$, $f'(2)=-1$, $g(2)=4$ ve $g'(2)=5$ olsun.",
                "$(f \\cdot g)'(2)$ değerini bulalım.",
                "$(f \\cdot g)'(2)=f'(2)g(2)+f(2)g'(2)=(-1) \\cdot 4+3 \\cdot 5$ olur.",
                "Sonuç $11$ dir."),
            "Bu tür sorularda fonksiyonları bulmaya çalışmak gereksizdir; kural yalnızca bu dört sayıyı ister.",
        ]},
        {"baslik": "Üç çarpanlı kural", "icerik": [
            "Çarpan sayısı üç olduğunda kural genişletilir: her terimde çarpanlardan yalnızca biri türevlenir ve üç terim toplanır:",
            "$$(f g h)'=f' g h+f g' h+f g h'$$",
            ornek(
                "$k(x)=x(x+1)(x+2)$ fonksiyonu verilsin.",
                "$k'(1)$ değerini bulalım.",
                "$k'(x)=(x+1)(x+2)+x(x+2)+x(x+1)$ olur.",
                "$k'(1)=6+3+2=11$ bulunur; açarak $k(x)=x^3+3x^2+2x$ ve $k'(1)=3+6+2=11$ ile de doğrulanır."),
            hap("$(fgh)'=f'gh+fg'h+fgh'$ olur; her terimde yalnız bir çarpan türevlenir."),
        ]},
        {"baslik": "Türevin işaretiyle davranış", "icerik": [
            "Çarpım kuralıyla bulunan türev ortak paranteze alındığında işaret tablosu kolayca yapılır. Böylece fonksiyonun nerede azaldığı, nerede arttığı ve en küçük değerini nerede aldığı bulunur.",
            ornek(
                "$h(x)=x e^x$ fonksiyonu verilsin.",
                "Artan ve azalan olduğu aralıkları ve en küçük değeri bulalım.",
                "$h'(x)=e^x(1+x)$; $x<-1$ için negatif, $x>-1$ için pozitiftir.",
                "Fonksiyon $x=-1$ e kadar azalır, sonra artar; en küçük değer $h(-1)=-\\dfrac{1}{e}$ dir."),
        ]},
        {"baslik": "Kare fonksiyon: özel durum", "icerik": [
            "Çarpım kuralı aynı fonksiyonun kendisiyle çarpımına uygulanırsa $(f^2)'=f'f+ff'=2ff'$ bulunur. Bu, zincir kuralının bir özel hâlidir ve kareli ifadelerin türevini açmadan almayı sağlar.",
            ornek(
                "$h(x)=(x^2+1)^2$ fonksiyonu verilsin.",
                "Türevini çarpım kuralının özel hâliyle bulalım.",
                "$h'(x)=2(x^2+1) \\cdot 2x$ olur.",
                "$h'(x)=4x^3+4x$ bulunur; açarak alınan türevle aynıdır."),
            hap("$(f^2)'=2f \\cdot f'$ olur; kareli ifadenin türevi açılmadan alınır."),
        ]},
        {"baslik": "Çarpım ve zincir birlikte", "icerik": [
            "Çarpanlardan biri bileşke bir fonksiyonsa, o çarpanın türevi zincir kuralıyla alınır ve çarpım kuralına yerleştirilir; iki kural birbirini tamamlar ve sırayla uygulanır. Sonuç genellikle ortak çarpanlar alınarak sadeleştirilir.",
            ornek(
                "$h(x)=x^2(3x+1)^4$ fonksiyonu verilsin.",
                "Türevini bulup sadeleştirelim.",
                "$h'(x)=2x(3x+1)^4+x^2 \\cdot 4(3x+1)^3 \\cdot 3$ olur.",
                "Ortak çarpan $2x(3x+1)^3$ alınınca $h'(x)=2x(3x+1)^3(9x+1)$ bulunur."),
            "Zincir kuralının ayrıntısı için <a href=\"/blog/zincir-kurali/\">Bileşke Fonksiyonun Türevi: Zincir Kuralı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Çarpımın ikinci türevi", "icerik": [
            "Çarpım kuralı iki kez uygulanırsa ikinci türev için şu formül çıkar: $(fg)''=f''g+2f'g'+fg''$. Katsayılar, binom açılımındaki $1$, $2$, $1$ katsayılarıyla aynıdır. Ortadaki terim, iki çarpanın birer kez türevlendiği iki farklı sıralamanın toplamından gelir.",
            ornek(
                "$h(x)=x e^x$ fonksiyonu verilsin.",
                "İkinci türevini bulalım.",
                "$f=x$ için $f'=1$, $f''=0$; $g=e^x$ için bütün türevler $e^x$ tir.",
                "$h''(x)=0+2e^x+x e^x=e^x(x+2)$ olur."),
        ]},
        {"baslik": "Teğet eğimi uygulaması", "icerik": [
            "Çarpım biçimindeki bir eğrinin herhangi bir noktadaki teğet eğimi, çarpım kuralıyla bulunan türeve o nokta yazılarak hesaplanır. Eğimin sıfır çıktığı noktalar yatay teğetli noktalardır.",
            ornek(
                "$y=x e^x$ eğrisi verilsin.",
                "Başlangıç noktasındaki teğet eğimini ve teğet denklemini bulalım.",
                "$y'=e^x(1+x)$ olduğundan $x=0$ da eğim $1$ dir.",
                "Eğri $(0, 0)$ dan geçer; teğet $y=x$ olur."),
            "Teğet denklemi yazmanın genel yöntemi <a href=\"/blog/teget-denklemi/\">Türevde Teğet Denklemi Nasıl Bulunur?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Uygulama: değişen dikdörtgen", "icerik": [
            "Kenarları zamanla değişen bir dikdörtgenin alanının değişim hızı çarpım kuralıyla bulunur. Kapaktaki düzeneğin sayısal karşılığı budur.",
            ornek(
                "Bir dikdörtgenin uzun kenarı $10$ cm ve saniyede $2$ cm uzuyor; kısa kenarı $5$ cm ve saniyede $1$ cm uzuyor.",
                "O andaki alanın değişim hızını bulalım.",
                "$A=u \\cdot k$ ise $A'=u' \\cdot k+u \\cdot k'=2 \\cdot 5+10 \\cdot 1$ olur.",
                "Alan saniyede $20$ santimetrekare artmaktadır."),
            "Aynı anda iki kenarın uzamasının etkisi ayrı ayrı hesaplanıp toplanır: uzun kenarın uzaması $10$, kısa kenarın uzaması $10$ santimetrekare katkı yapar.",
        ]},
        {"baslik": "Uygulama: gelir", "icerik": [
            "Ekonomide gelir, fiyat ile satış miktarının çarpımıdır. Fiyat ve miktar zamanla değişiyorsa gelirin değişim hızı çarpım kuralıyla bulunur ve iki etki birbirini dengeleyebilir.",
            ornek(
                "Bir ürünün fiyatı $p(t)=20+t$ TL ve günlük satış miktarı $q(t)=100-2t$ adet olsun.",
                "$t=0$ anındaki gelirin değişim hızını bulalım.",
                "$R'=p' \\cdot q+p \\cdot q'=1 \\cdot 100+20 \\cdot (-2)$ olur.",
                "Gelir günde $60$ TL artmaktadır; fiyat artışının etkisi satış düşüşünün etkisinden büyüktür."),
            hap("Bir kafede kahvenin fiyatı her ay $2$ lira artarken satışı her ay $30$ fincan azalıyor.", "Fiyat $50$ lira, satış $900$ fincanken aylık ciro ayda $2 \\cdot 900+50 \\cdot (-30)=300$ lira artar.", gunluk=True),
        ]},
        {"baslik": "Parametreli çarpım", "icerik": [
            "Çarpanlardan birinde bilinmeyen bir katsayı varsa ve bir noktadaki türev değeri verilmişse, çarpım kuralı uygulanıp nokta yerine yazılır; ortaya çıkan denklem katsayıyı verir.",
            ornek(
                "$h(x)=(x^2+a)e^x$ ve $h'(0)=3$ olsun.",
                "$a$ değerini bulalım.",
                "$h'(x)=2x e^x+(x^2+a)e^x$ olduğundan $h'(0)=0+a$ olur.",
                "$a=3$ bulunur."),
        ]},
        {"baslik": "Açmak mı, kural mı?", "icerik": [
            "Çarpım kuralı her çarpımda zorunlu değildir. Hangi yolun daha kısa olduğu çarpanların türüne bağlıdır:",
            tablo(["Çarpım", "Önerilen yol"], [
                ["İki kısa polinom", "Açıp terim terim türev"],
                ["Polinom ve $e^x$", "Çarpım kuralı"],
                ["Polinom ve $\\sin x$", "Çarpım kuralı"],
                ["Polinom ve $\\ln x$", "Çarpım kuralı"],
                ["Yüksek kuvvetli parantez", "Çarpım ve zincir kuralı"],
                ["$x^a \\cdot x^b$", "Üsleri toplayıp kuvvet kuralı"],
            ]),
            "Yalnızca bir noktadaki türev değeri isteniyorsa açmak yerine kuralı uygulayıp sayıyı hemen yazmak çoğu zaman en hızlı yoldur.",
        ]},
        {"baslik": "Sınavda çarpımın türevi", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) çarpımın türevi; fonksiyon değerleri ve türev değerleri verilen sorular, polinomla üstel ya da trigonometrik fonksiyon çarpımları ve teğet eğimi biçiminde karşına çıkabilir.",
                "Çarpım kuralı çoğu zaman zincir ve bölüm kurallarıyla birlikte kullanılır."),
            "Soruda $f(a)$, $f'(a)$, $g(a)$ ve $g'(a)$ gibi değerler verildiyse fonksiyonları bulmaya çalışma; kuralı bu dört sayıyla hemen uygula. Türevin sıfır olduğu noktalar soruluyorsa sonucu ortak paranteze almayı unutma.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$(fg)'=f'g'$", "$(fg)'=f'g+fg'$"],
                ["İki terimden birini unutmak", "Her çarpan bir kez türevlenir"],
                ["$(fg)'=f'g-fg'$ yazmak", "Çarpımda artı, bölümde eksi"],
                ["Üç çarpanda iki terim yazmak", "Üç terim vardır"],
                ["$e^x$ i ortak paranteze almamak", "Sıfırlar ancak böyle görülür"],
                ["$(fg)''=f''g''$ yazmak", "$f''g+2f'g'+fg''$"],
            ]),
            "Çarpım kuralını doğru hatırlayıp hatırlamadığını denetlemek için $x \\cdot x$ ile dene: kural $1 \\cdot x+x \\cdot 1=2x$ vermelidir ve bu, $x^2$ nin türevidir.",
        ]},
    ],
    "sss": [
        ("Çarpımın türevi nasıl alınır?",
         "Birinci fonksiyonun türevi ikinciyle, birinci fonksiyon ikincinin türeviyle çarpılır ve bu iki terim toplanır: (fg) üssü eşittir f üssü g artı f g üssü."),
        ("Çarpımın türevi türevlerin çarpımı mıdır?",
         "Hayır. x çarpı x in türevi 2x iken türevlerin çarpımı 1 olur; iki sonuç farklıdır."),
        ("Üç fonksiyonun çarpımının türevi nedir?",
         "Her terimde yalnızca bir çarpan türevlenir ve üç terim toplanır: f üssü g h artı f g üssü h artı f g h üssü."),
        ("x e üzeri x in türevi nedir?",
         "e üzeri x artı x e üzeri x, yani e üzeri x çarpı (x + 1) dir."),
        ("x ln x in türevi nedir?",
         "ln x artı 1 dir. Türev x eşittir 1 bölü e noktasında sıfır olur."),
        ("Çarpım kuralı ne zaman kullanılmaz?",
         "İki kısa polinomun çarpımında ifadeyi açıp terim terim türev almak çoğu zaman daha kısadır."),
        ("Çarpımın türevi nasıl ispatlanır?",
         "Türevin tanımındaki farka aynı terim bir kez eklenip bir kez çıkarılır ve fark iki parçaya ayrılır. Limit alınınca iki parça kuralın iki terimini verir."),
        ("Çarpımın ikinci türevi nasıl bulunur?",
         "Çarpım kuralı iki kez uygulanır ve sonuç f iki üssü g artı 2 f üssü g üssü artı f g iki üssü olur. Katsayılar binom açılımındaki 1, 2, 1 katsayılarıdır."),
    ],
    "kontrol": [
        "Çarpımın türevinin neden türevlerin çarpımı olmadığını açıklayabiliyorum.",
        "Çarpım kuralını doğru yazıp uygulayabiliyorum.",
        "Kuralı dikdörtgen alanıyla geometrik olarak açıklayabiliyorum.",
        "Polinom ve üstel fonksiyon çarpımlarının türevini alabiliyorum.",
        "Trigonometrik ve logaritmik çarpımların türevini bulabiliyorum.",
        "Değerleri verilen fonksiyonlarla bir noktadaki türevi hesaplayabiliyorum.",
        "Üç çarpanlı kuralı kullanabiliyorum.",
        "Sonucu ortak paranteze alıp türevin sıfırlarını bulabiliyorum.",
        "Çarpım ve zincir kuralını birlikte uygulayabiliyorum.",
        "Değişim oranı problemlerini çarpım kuralıyla çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["turev-alma-kurallari", "bolumun-turevi", "zincir-kurali"],
}
