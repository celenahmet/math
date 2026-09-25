# scripts/yazilar/11_ikinci_dereceden_denklemler.py — Ikinci Dereceden Denklemler (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "ikinci-dereceden-denklemler",
    "baslik": "İkinci Dereceden Denklemler Konu Anlatımı",
    "aciklama": "İkinci dereceden denklem nasıl çözülür? Çarpanlara ayırma, tam kareye tamamlama, kök formülü, diskriminant, özel biçimler, köklü ve kesirli denklemler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "ikinci-dereceden-denklemler",
    "kapak_alt": "İkinci dereceden denklemler: yatay bir çubuğu iki noktada kesen esnek bir parabol modeli kuran iki öğrenci",
    "ozet": "İkinci dereceden denklemler, bilinmeyenin karesini içeren denklemlerdir ve cebirin en çok kullanılan araçlarından biridir. Alan, hız ve kâr problemleri çoğu zaman bu tür bir denkleme dönüşür. Bu yazıda denklemin standart biçimini, özel biçimlerin hızlı çözümünü, çarpanlara ayırmayı, tam kareye tamamlamayı, kök formülünü, diskriminantın rolünü, grafikle bağlantıyı, değişken değiştirmeyi, kesirli ve köklü denklemleri ve denklem kurma problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "İkinci dereceden denklem nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birinci dereceden denklemleri ve çarpanlara ayırmayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/birinci-dereceden-denklemler-konu-anlatimi-pdf/\">Birinci Dereceden Denklemler Konu Anlatımı PDF</a> ve <a href=\"/blog/polinomlarda-carpanlara-ayirma/\">Polinomlarda Çarpanlara Ayırma</a> yazılarına göz at."),
            "$a$, $b$ ve $c$ gerçek sayılar ve $a \\neq 0$ olmak üzere aşağıdaki biçimde yazılabilen denklemlere <strong>ikinci dereceden bir bilinmeyenli denklem</strong> denir:",
            "$$ax^2+bx+c=0$$",
            "$a$ sıfır olsaydı $x^2$ li terim kaybolur ve denklem birinci dereceden olurdu. Bu yüzden $a \\neq 0$ koşulu tanımın ayrılmaz parçasıdır. Denklemi sağlayan $x$ değerlerine denklemin <strong>kökleri</strong>, köklerin kümesine de <strong>çözüm kümesi</strong> denir.",
            hap("$ax^2+bx+c=0$ ve $a \\neq 0$.",
                "İkinci dereceden bir denklemin en fazla iki gerçek kökü vardır."),
        ]},
        {"baslik": "Bir sayının kök olup olmadığını denetlemek", "icerik": [
            "Bir sayının denklemin kökü olup olmadığını anlamak için denklemi çözmeye gerek yoktur: sayı denklemde yerine yazılır. Sonuç sıfırsa sayı köktür, değilse kök değildir.",
            ornek(
                "$2x^2-5x-3=0$ denklemi verilsin.",
                "$3$ ve $-1$ sayılarının kök olup olmadığını inceleyelim.",
                "$x=3$ için $18-15-3=0$; $3$ bir köktür.",
                "$x=-1$ için $2+5-3=4$; $-1$ kök değildir."),
        ]},
        {"baslik": "Standart biçim ve katsayılar", "icerik": [
            "Bir denklem çözülmeden önce bütün terimler bir tarafa toplanıp standart biçime getirilir. Katsayılar ancak bu biçimde doğru okunur; eksik terimlerin katsayısı sıfırdır.",
            tablo(["Denklem", "Standart biçim", "$a$, $b$, $c$"], [
                ["$3x^2-5=0$", "$3x^2+0x-5=0$", "$3$, $0$, $-5$"],
                ["$x^2=4x$", "$x^2-4x=0$", "$1$, $-4$, $0$"],
                ["$2x^2=7-x$", "$2x^2+x-7=0$", "$2$, $1$, $-7$"],
            ]),
            dikkat(
                "Denklemi standart biçime getirmeden katsayı okumak.",
                "$2x^2=7-x$ denkleminde $b=-1$ ve $c=7$ değildir. Terimler sol tarafa geçince işaret değiştirir: $b=1$ ve $c=-7$ olur."),
        ]},
        {"baslik": "x² = k biçimindeki denklemler", "icerik": [
            "Denklem yalnızca bir kare ve bir sabitten oluşuyorsa iki tarafın karekökü alınır. Karekök alınırken hem pozitif hem negatif kök yazılmalıdır, çünkü bir sayının karesi ile tersinin karesi aynıdır.",
            ornek(
                "$x^2=9$, $x^2=-4$ ve $(x-1)^2=16$ denklemleri verilsin.",
                "Çözüm kümelerini bulalım.",
                "$x^2=9$ için $x=3$ ya da $x=-3$.",
                "$x^2=-4$ denkleminin gerçek kökü yoktur; hiçbir gerçek sayının karesi negatif değildir.",
                "$(x-1)^2=16$ için $x-1=\\pm 4$; $x=5$ ya da $x=-3$."),
        ]},
        {"baslik": "Sabit terimi olmayan denklemler", "icerik": [
            "$c=0$ ise denklem $ax^2+bx=0$ biçimindedir ve $x$ ortak çarpan olarak paranteze alınır. Köklerden biri her zaman $0$ dır.",
            ornek(
                "$2x^2-6x=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$2x(x-3)=0$.",
                "$x=0$ ya da $x=3$. Çözüm kümesi $\\{0, 3\\}$."),
            dikkat(
                "İki tarafı $x$ e bölmek.",
                "$2x^2=6x$ denkleminde iki taraf $x$ e bölünürse $2x=6$ bulunur ve $x=0$ kökü kaybolur. Bilinmeyen içeren bir ifadeye bölmek yerine ortak çarpan alınmalıdır."),
        ]},
        {"baslik": "Birinci dereceden terimi olmayan denklemler", "icerik": [
            "$b=0$ ise denklem $ax^2+c=0$ biçimindedir ve $x^2$ yalnız bırakılır. $-\\dfrac{c}{a}$ pozitifse iki kök, sıfırsa tek kök, negatifse gerçek kök yoktur.",
            ornek(
                "$x^2-7=0$ ve $3x^2+12=0$ denklemleri verilsin.",
                "Çözüm kümelerini bulalım.",
                "$x^2=7$ için $x=\\sqrt{7}$ ya da $x=-\\sqrt{7}$.",
                "$3x^2=-12$ için $x^2=-4$; gerçek kök yoktur."),
        ]},
        {"baslik": "Çarpanlara ayırarak çözmek", "icerik": [
            "İfade çarpanlarına ayrılabiliyorsa en hızlı yol budur. Bir çarpım sıfırsa çarpanlardan en az biri sıfırdır; bu yüzden her çarpan ayrı ayrı sıfıra eşitlenir.",
            ornek(
                "$x^2-x-6=0$ denklemi verilsin.",
                "Denklemi çarpanlara ayırarak çözelim.",
                "Çarpımı $-6$, toplamı $-1$ olan sayılar $-3$ ve $2$ dir: $(x-3)(x+2)=0$.",
                "$x=3$ ya da $x=-2$. Çözüm kümesi $\\{-2, 3\\}$."),
            ornek(
                "$2x^2+5x-3=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Çapraz çarpımla: $(2x-1)(x+3)=0$.",
                "$x=\\dfrac{1}{2}$ ya da $x=-3$."),
        ]},
        {"baslik": "Katsayıları kesirli denklemler", "icerik": [
            "Katsayılar kesirliyse denklem önce paydaların ortak katıyla çarpılır. Denklemin her iki tarafı sıfırdan farklı aynı sayıyla çarpılınca kökler değişmez; yalnızca hesap kolaylaşır.",
            ornek(
                "$\\dfrac{1}{2}x^2-\\dfrac{1}{3}x-\\dfrac{1}{6}=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "İki taraf $6$ ile çarpılır: $3x^2-2x-1=0$.",
                "$(3x+1)(x-1)=0$; kökler $1$ ve $-\\dfrac{1}{3}$ dir."),
        ]},
        {"baslik": "Tam kareye tamamlama", "icerik": [
            "Çarpanlara ayrılamayan denklemlerde ifade bir tam kareye tamamlanır. $x^2+bx$ ifadesine $(\\dfrac{b}{2})^2$ eklenince $(x+\\dfrac{b}{2})^2$ elde edilir; denklemin dengesi bozulmasın diye aynı sayı diğer tarafa da eklenir.",
            ornek(
                "$x^2+6x+2=0$ denklemi verilsin.",
                "Tam kareye tamamlayarak çözelim.",
                "$x^2+6x=-2$. İki tarafa $(\\dfrac{6}{2})^2=9$ eklenir: $x^2+6x+9=7$.",
                "$(x+3)^2=7$, yani $x+3=\\pm\\sqrt{7}$.",
                "$x=-3+\\sqrt{7}$ ya da $x=-3-\\sqrt{7}$."),
            "Tam kareye tamamlama yalnızca bir çözüm yöntemi değildir; kök formülünün de, parabolün tepe noktasının da kaynağıdır. Bu yüzden adımlarını anlamak, formülü ezberlemekten daha değerlidir.",
        ]},
        {"baslik": "Kök formülü", "icerik": [
            "Genel denklem $ax^2+bx+c=0$ tam kareye tamamlanırsa her ikinci dereceden denklemi çözen formül elde edilir. $\\Delta=b^2-4ac$ olmak üzere kökler şunlardır:",
            "$$x=\\dfrac{-b \\pm \\sqrt{\\Delta}}{2a}$$",
            ornek(
                "$x^2-4x+1=0$ denklemi verilsin.",
                "Kök formülüyle çözelim.",
                "$a=1$, $b=-4$, $c=1$. $\\Delta=16-4=12$.",
                "$x=\\dfrac{4 \\pm \\sqrt{12}}{2}=\\dfrac{4 \\pm 2\\sqrt{3}}{2}=2 \\pm \\sqrt{3}$."),
            dikkat(
                "Formülde $-b$ yi yanlış işaretle yazmak.",
                "$b=-4$ ise $-b=4$ tür. Katsayının işaretini parantez içinde yazmak, $-(-4)$ gibi ifadelerde işaret hatasını önler."),
        ]},
        {"baslik": "Kök formülü nereden gelir?", "icerik": [
            "Kök formülü, genel denklemin tam kareye tamamlanmasıyla elde edilir. Adımları izlemek, formülü unutulsa bile yeniden kurmayı sağlar.",
            tablo(["Adım", "İşlem"], [
                ["1", "İki taraf $a$ ya bölünür: $x^2+\\dfrac{b}{a}x=-\\dfrac{c}{a}$"],
                ["2", "İki tarafa $\\dfrac{b^2}{4a^2}$ eklenir"],
                ["3", "Sol taraf tam karedir: $(x+\\dfrac{b}{2a})^2=\\dfrac{b^2-4ac}{4a^2}$"],
                ["4", "Karekök alınır ve $x$ yalnız bırakılır"],
            ]),
            "Son adımda karekökün içinde $b^2-4ac$ kalır. Bu yüzden diskriminant formülün tam kalbindedir: negatifse karekök gerçek sayılarda alınamaz ve denklemin gerçek kökü yoktur.",
        ]},
        {"baslik": "b çift olduğunda kısa formül", "icerik": [
            "$b$ katsayısı çift olduğunda $b=2b'$ yazılır ve formül sadeleşir. Bu kısa biçim, hem hesabı küçültür hem de sonucu doğrudan sade hâlde verir:",
            "$$x=\\dfrac{-b' \\pm \\sqrt{b'^2-ac}}{a}$$",
            ornek(
                "$x^2-4x+1=0$ denklemi verilsin.",
                "Kısa formülle çözelim.",
                "$b=-4$ olduğu için $b'=-2$ dir.",
                "$x=\\dfrac{2 \\pm \\sqrt{4-1}}{1}=2 \\pm \\sqrt{3}$; uzun formülle bulunan sonuçla aynıdır."),
            "Köklü sonuçlar da denklemde yerine yazılarak kontrol edilebilir: $(2+\\sqrt{3})^2-4(2+\\sqrt{3})+1=7+4\\sqrt{3}-8-4\\sqrt{3}+1=0$.",
        ]},
        {"baslik": "Diskriminant ve kök sayısı", "icerik": [
            "Kök formülündeki $\\Delta=b^2-4ac$ sayısına <strong>diskriminant</strong> denir. Karekökün içindeki bu sayının işareti, denklemin kaç gerçek kökü olduğunu belirler.",
            tablo(["Diskriminant", "Gerçek kök sayısı"], [
                ["$\\Delta>0$", "İki farklı kök"],
                ["$\\Delta=0$", "İki eşit kök, yani tek kök"],
                ["$\\Delta<0$", "Gerçek kök yok"],
            ]),
            "Ayrıntısı <a href=\"/blog/diskriminant-delta/\">Diskriminant Nedir? Delta Nasıl Hesaplanır?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Gerçek kökü olmayan bir denklem", "icerik": [
            "Her ikinci dereceden denklemin gerçek kökü yoktur. Diskriminant negatif çıktığında tam kareye tamamlama bunun nedenini açıkça gösterir: bir kare, negatif bir sayıya eşitlenmiş olur.",
            ornek(
                "$x^2+2x+5=0$ denklemi verilsin.",
                "Denklemin gerçek kökü olup olmadığını inceleyelim.",
                "$\\Delta=4-20=-16$; diskriminant negatiftir.",
                "Tam kareye tamamlanınca $(x+1)^2=-4$ bulunur. Hiçbir gerçek sayının karesi negatif olmadığı için çözüm kümesi boştur."),
            "Bu durumda parabol $x$ ekseninin tamamen üstünde kalır. Denklemin gerçek kökünün olmaması, fonksiyonun hiçbir noktada sıfır değerini almaması demektir.",
        ]},
        {"baslik": "Kökler ile katsayılar arasındaki bağıntı", "icerik": [
            "Denklemin kökleri $x_1$ ve $x_2$ ise köklerin toplamı ve çarpımı, kökler bulunmadan katsayılardan hesaplanabilir:",
            tablo(["Bağıntı", "Değer"], [
                ["$x_1+x_2$", "$-\\dfrac{b}{a}$"],
                ["$x_1 \\cdot x_2$", "$\\dfrac{c}{a}$"],
            ]),
            ornek(
                "$x^2-x-6=0$ denklemi verilsin.",
                "Kökler toplamını ve çarpımını hem katsayılardan hem köklerden bulalım.",
                "Katsayılardan: toplam $1$, çarpım $-6$.",
                "Köklerden: $3+(-2)=1$ ve $3 \\cdot (-2)=-6$."),
            "Ayrıntısı <a href=\"/blog/kokler-toplami-carpimi/\">Kökler Toplamı ve Kökler Çarpımı Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Grafikle bağlantı", "icerik": [
            "$ax^2+bx+c=0$ denkleminin kökleri, $y=ax^2+bx+c$ parabolünün $x$ eksenini kestiği noktaların yatay konumlarıdır. Kapaktaki esnek çubuk da bunu gösterir: kemer yatay çubuğu iki noktada keser ve bu iki nokta denklemin kökleridir.",
            koordinat_grafik("y = x² − x − 6 parabolü x eksenini köklerde keser", [("y = x² − x − 6", lambda x: x * x - x - 6)], (-4, 5), (-7, 3),
                             noktalar=[(-2, 0, "(−2, 0)", True), (3, 0, "(3, 0)", True)]),
            "Grafik, kök sayısını da gösterir: parabol ekseni iki noktada kesiyorsa iki kök, eksene teğetse tek kök, ekseni hiç kesmiyorsa gerçek kök yoktur. Parabolün ayrıntısı <a href=\"/blog/parabol-konu-anlatimi/\">Parabol Konu Anlatımı</a> yazısında.",
        ]},
        {"baslik": "Değişken değiştirme", "icerik": [
            "Bazı denklemler ikinci dereceden değildir ama bir parçası yeni bir değişkenle gösterilince ikinci dereceden olur. En sık karşılaşılan durum, yalnızca $x^4$ ve $x^2$ içeren denklemlerdir.",
            ornek(
                "$x^4-13x^2+36=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$x^2=t$ yazılır: $t^2-13t+36=0$, yani $(t-4)(t-9)=0$.",
                "$t=4$ için $x=\\pm 2$; $t=9$ için $x=\\pm 3$. Çözüm kümesi $\\{-3, -2, 2, 3\\}$."),
            dikkat(
                "Yeni değişkenin kökünü asıl değişkenin kökü sanmak.",
                "Bulunan $4$ ve $9$ değerleri $t$ nin kökleridir. Asıl soru $x$ i sorduğu için $x^2=t$ eşitliğine geri dönülmelidir; $t$ negatif çıksaydı o değer gerçek kök vermezdi."),
        ]},
        {"baslik": "Kesirli denklemler", "icerik": [
            "Paydasında bilinmeyen olan denklemlerde iki taraf paydalarla çarpılarak kesirlerden kurtulunur. Bulunan kökler paydayı sıfır yapıyorsa atılır.",
            ornek(
                "$x+\\dfrac{6}{x}=5$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$x \\neq 0$ olmak üzere iki taraf $x$ ile çarpılır: $x^2+6=5x$.",
                "$x^2-5x+6=0$, yani $(x-2)(x-3)=0$. Kökler $2$ ve $3$ tür ve ikisi de paydayı sıfır yapmaz."),
            "Paydalardan kurtulurken denklem bir ifadeyle çarpıldığı için o ifadeyi sıfır yapan değerler ilk denklemde tanımsızdır. Çözüm bittikten sonra bu değerlerin köklerin arasında olup olmadığına bakmak, sonucun geçerliliğini güvenceye alır.",
        ]},
        {"baslik": "Köklü denklemler", "icerik": [
            "Karekök içeren bir denklemde iki tarafın karesi alınır. Kare alma yeni ve sahte kökler üretebilir, çünkü iki farklı sayının kareleri aynı olabilir; bu yüzden her kök ilk denklemde denenmelidir.",
            ornek(
                "$\\sqrt{x+2}=x$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Kare alınır: $x+2=x^2$, yani $x^2-x-2=0$ ve $(x-2)(x+1)=0$.",
                "$x=2$ için $\\sqrt{4}=2$; sağlar. $x=-1$ için $\\sqrt{1}=1$ ve $1 \\neq -1$; sağlamaz.",
                "Çözüm kümesi $\\{2\\}$."),
        ]},
        {"baslik": "Mutlak değerli denklemler", "icerik": [
            "$x^2$ ile $|x|$ birlikte geçiyorsa $x^2=|x|^2$ eşitliğinden yararlanılır ve $|x|$ yeni bir değişken gibi kullanılır. $|x|$ negatif olamayacağı için negatif kökler atılır.",
            ornek(
                "$x^2-|x|-6=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$|x|=t$ olsun: $t^2-t-6=0$, yani $(t-3)(t+2)=0$.",
                "$t=-2$ olamaz, çünkü mutlak değer negatif değildir. $|x|=3$ ten $x=3$ ya da $x=-3$."),
        ]},
        {"baslik": "Ortak kök", "icerik": [
            "İki denklemin ortak kökü, iki denklemi birden sağlayan sayıdır. Denklemlerin baş katsayıları eşitse biri ötekinden çıkarılınca $x^2$ li terim kaybolur ve ortak kök birinci dereceden bir denklemden bulunur.",
            ornek(
                "$x^2-5x+6=0$ ve $x^2-x-2=0$ denklemleri verilsin.",
                "Ortak kökü bulalım.",
                "İkinci denklem birinciden çıkarılır: $-4x+8=0$, yani $x=2$.",
                "Kontrol: $4-10+6=0$ ve $4-2-2=0$. Ortak kök $2$ dir."),
        ]},
        {"baslik": "Kökleri verilen denklemi yazmak", "icerik": [
            "Kökleri $x_1$ ve $x_2$ olan baş katsayısı $1$ denklem $(x-x_1)(x-x_2)=0$ dır. Açılınca $x^2-(x_1+x_2)x+x_1 x_2=0$ biçimine gelir; yani denklem kökler toplamı ve çarpımıyla doğrudan yazılabilir.",
            ornek(
                "Kökleri $2$ ve $-5$ olan denklem istensin.",
                "Denklemi yazalım.",
                "Toplam $-3$, çarpım $-10$.",
                "$x^2+3x-10=0$."),
        ]},
        {"baslik": "Bir kökü verilen parametreli denklem", "icerik": [
            "Denklemde bir parametre bulunuyor ve köklerden biri biliniyorsa, bu kök denklemi sağladığı için yerine yazılır. Bulunan parametreyle denklem tamamlanır ve diğer kök bulunur.",
            ornek(
                "$x^2-(m+1)x+m=0$ denkleminin bir kökü $3$ tür.",
                "$m$ yi ve diğer kökü bulalım.",
                "$x=3$ yazılır: $9-3(m+1)+m=0$, yani $6-2m=0$ ve $m=3$.",
                "Denklem $x^2-4x+3=0$ olur: $(x-1)(x-3)=0$. Diğer kök $1$ dir."),
        ]},
        {"baslik": "Denklem kurma problemleri", "icerik": [
            "Sözel problemler çoğu zaman ikinci dereceden bir denkleme dönüşür. Denklem çözüldükten sonra köklerin problemin koşullarına uyup uymadığına bakılır: uzunluk negatif olamaz, kişi sayısı kesirli olamaz.",
            ornek(
                "Ardışık iki tam sayının çarpımı $56$ dır.",
                "Bu sayıları bulalım.",
                "Küçük sayı $n$ olsun: $n(n+1)=56$, yani $n^2+n-56=0$ ve $(n+8)(n-7)=0$.",
                "$n=7$ için sayılar $7$ ve $8$; $n=-8$ için sayılar $-8$ ve $-7$. İki çözüm de tam sayıdır."),
            ornek(
                "Bir dikdörtgenin uzun kenarı kısa kenarından $3$ santimetre fazla ve alanı $40$ santimetrekaredir.",
                "Kenarları bulalım.",
                "Kısa kenar $w$ olsun: $w(w+3)=40$, yani $w^2+3w-40=0$ ve $(w+8)(w-5)=0$.",
                "Uzunluk negatif olamayacağı için $w=5$; kenarlar $5$ ve $8$ santimetredir."),
            "Denklem kurmanın ayrıntısı <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısında.",
        ]},
        {"baslik": "Alan problemi", "icerik": [
            "Geometrik problemler de sık sık ikinci dereceden denkleme dönüşür, çünkü alan iki uzunluğun çarpımıdır. Kenar uzunluğu değiştiğinde yeni alan, eski kenarın karesini içeren bir ifade olur.",
            ornek(
                "Bir karenin kenarı $2$ santimetre uzatılınca alanı $49$ santimetrekare oluyor.",
                "İlk kenar uzunluğunu bulalım.",
                "İlk kenar $x$ olsun: $(x+2)^2=49$, yani $x+2=\\pm 7$.",
                "$x=5$ ya da $x=-9$. Uzunluk negatif olamayacağı için ilk kenar $5$ santimetredir."),
        ]},
        {"baslik": "Hangi yöntem ne zaman?", "icerik": [
            "Her ikinci dereceden denklem kök formülüyle çözülür ama çoğu zaman daha kısa bir yol vardır. Yöntemi denklemin biçimine göre seçmek zaman kazandırır.",
            tablo(["Denklemin biçimi", "En hızlı yöntem"], [
                ["$ax^2+c=0$", "$x^2$ yi yalnız bırakıp karekök"],
                ["$ax^2+bx=0$", "Ortak çarpan $x$"],
                ["Tam sayı kökler seziliyor", "Çarpanlara ayırma"],
                ["$x^2+bx+c$ ve $b$ çift", "Tam kareye tamamlama"],
                ["Diğer bütün durumlar", "Kök formülü"],
            ]),
        ]},
        {"baslik": "Sınavda ikinci dereceden denklemler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) denklemler çarpanlara ayırarak çözme, kök formülü, kökler toplamı ve çarpımı ile denklem kurma problemleri biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) diskriminant yorumu, parametreli denklemler, değişken değiştirme ve parabolle bağlantı da sorulabilir."),
            "Sınavda kökleri tek tek bulmak her zaman gerekmez. Soru yalnızca köklerin toplamını, çarpımını ya da kaç kök olduğunu istiyorsa katsayılar ve diskriminant yeterlidir; kökleri bulmaya çalışmak zaman kaybettirir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$x^2=9$ için yalnız $3$ yazmak", "$x=3$ ya da $x=-3$"],
                ["İki tarafı $x$ e bölmek", "Ortak çarpan alınır, $0$ kökü korunur"],
                ["Standart biçime getirmeden katsayı okumak", "Önce her şey bir tarafa toplanır"],
                ["Kök formülünde $-b$ nin işaretini karıştırmak", "Katsayı parantezle yazılır"],
                ["Köklü denklemde kökleri denememek", "Sahte kökler atılır"],
                ["Kesirli denklemde paydayı sıfır yapan kökü tutmak", "Bu kökler atılır"],
            ]),
            "Bu hataların çoğu, çözüm bittikten sonra kontrol yapılmamasından doğar. Bulunan her kökü ilk denklemde yerine yazmak birkaç saniye sürer ve hem işlem hatalarını hem sahte kökleri yakalar.",
        ]},
    ],
    "sss": [
        ("İkinci dereceden denklem nedir?",
         "a sıfırdan farklı olmak üzere ax kare artı bx artı c eşittir sıfır biçimindeki denklemdir. En fazla iki gerçek kökü vardır."),
        ("İkinci dereceden denklem nasıl çözülür?",
         "Çarpanlara ayrılabiliyorsa çarpanlar sıfıra eşitlenir. Ayrılamıyorsa tam kareye tamamlanır ya da kök formülü kullanılır."),
        ("Kök formülü nedir?",
         "x, eksi b artı eksi karekök delta bölü 2a dır. Delta, b kare eksi 4ac ye eşittir."),
        ("Denklemin gerçek kökü olmadığı nasıl anlaşılır?",
         "Diskriminant negatifse gerçek kök yoktur. Grafikte bu, parabolün x eksenini hiç kesmemesi demektir."),
        ("Köklü denklemlerde neden kontrol gerekir?",
         "İki tarafın karesi alınınca ilk denklemi sağlamayan sahte kökler ortaya çıkabilir. Her kök ilk denklemde denenmelidir."),
        ("Kökleri verilen denklem nasıl yazılır?",
         "Kökler toplamı ve çarpımı bulunur. Baş katsayısı 1 olan denklem x kare eksi toplam çarpı x artı çarpım eşittir sıfırdır."),
        ("İkinci dereceden bir denklemin kaç kökü olabilir?",
         "En fazla iki gerçek kökü olabilir. Diskriminant pozitifse iki, sıfırsa bir, negatifse hiç gerçek kök yoktur."),
    ],
    "kontrol": [
        "Bir denklemi standart biçime getirip katsayılarını okuyabiliyorum.",
        "x² = k biçimindeki denklemleri çözebiliyorum.",
        "Sabit terimi ya da birinci dereceden terimi olmayan denklemleri çözebiliyorum.",
        "Çarpanlara ayırarak denklem çözebiliyorum.",
        "Tam kareye tamamlama yöntemini uygulayabiliyorum.",
        "Kök formülünü kullanabiliyorum.",
        "Diskriminantla kök sayısını belirleyebiliyorum.",
        "Değişken değiştirerek denklem çözebiliyorum.",
        "Kesirli ve köklü denklemlerde geçersiz kökleri ayıklayabiliyorum.",
        "Sözel problemleri ikinci dereceden denkleme dönüştürüp çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["diskriminant-delta", "kokler-toplami-carpimi", "parabol-konu-anlatimi"],
}
