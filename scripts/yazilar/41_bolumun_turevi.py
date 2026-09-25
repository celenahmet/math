# scripts/yazilar/41_bolumun_turevi.py — Bolumun Turevi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "bolumun-turevi",
    "baslik": "Bölümün Türevi Nasıl Alınır?",
    "aciklama": "Bölümün türevi nasıl alınır? Bölüm kuralı ve ispatı, paydaki sıra, ters fonksiyon kuralı, tanjantın türevi, doğrusal kesirler ve uygulamalar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "bolumun-turevi",
    "kapak_alt": "Bölümün türevi: iki paralel raydaki kaydırıcıları tek bir oran çıkışına bağlayan düzeneği inceleyen iki öğrenci",
    "ozet": "İki fonksiyonun bölümünün türevi, türevlerin bölümü değildir. Bölüm kuralına göre payın türevi paydayla, pay paydanın türeviyle çarpılır, bu iki çarpımın farkı paydanın karesine bölünür. Bu yazıda türevlerin bölümünün neden yanlış olduğunu, bölüm kuralını ve çarpım kuralından ispatını, paydaki sıranın önemini, ters fonksiyon kuralını, doğrusal kesirler için kısa formülü, tanjant ve kotanjantın türevini, üstel, logaritmik ve trigonometrik bölümleri, önce sadeleştirmeyi, bölümün türevinin işaretini ve ortalama maliyet ile ilaç derişimi gibi uygulamaları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Bölümün türevi neden özel?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için temel türev kurallarını ve çarpım kuralını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> ve <a href=\"/blog/carpimin-turevi/\">Çarpımın Türevi Nasıl Alınır?</a> yazılarına göz at."),
            "Çarpımın türevi türevlerin çarpımı olmadığı gibi, bölümün türevi de türevlerin bölümü değildir. Bunu en basit örnekle görmek mümkündür: $\\dfrac{x^2}{x}=x$ olduğu için türev $1$ dir; oysa türevlerin bölümü $\\dfrac{2x}{1}=2x$ olur. İki sonuç yalnızca $x=\\dfrac{1}{2}$ de eşittir, genel olarak farklıdır.",
            "Kapaktaki öğrenciler iki paralel raydaki kaydırıcıları tek bir oran çıkışına bağlayan bir düzeneği inceliyor. Üstteki kaydırıcı payı, alttaki paydayı temsil ediyor; ikisi birlikte hareket ettiğinde oranın nasıl değiştiği iki hareketin birleşik etkisine bağlı. Bölüm kuralı bu birleşik etkiyi tek bir formülle hesaplar.",
        ]},
        {"baslik": "Bölüm kuralı", "icerik": [
            "$f$ ve $g$ türevli ve $g(x) \\neq 0$ olsun. Bölümün türevi şu formülle bulunur:",
            "$$\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f' \\cdot g-f \\cdot g'}{g^2}$$",
            "Kural sözle şöyle hatırlanır: payın türevi çarpı payda, eksi pay çarpı paydanın türevi, bölü paydanın karesi. Paydaki iki terim çarpım kuralındaki terimlerin aynısıdır; farkı, aralarındaki işaretin eksi olmasıdır.",
            hap("Bölümün türevinde paydaki sıra önemlidir: önce payın türevi.",
                "Payda her zaman paydanın karesidir ve pozitiftir."),
        ]},
        {"baslik": "Kuralın ispatı", "icerik": [
            "Bölüm kuralı çarpım kuralından elde edilir. $q=\\dfrac{f}{g}$ olsun; o hâlde $f=q \\cdot g$ dir. Bu eşitliğin iki tarafının türevi alınırsa çarpım kuralına göre $f'=q' \\cdot g+q \\cdot g'$ olur.",
            "Bu denklemden $q'$ yalnız bırakılır: $q'=\\dfrac{f'-q \\cdot g'}{g}$. Son olarak $q$ yerine $\\dfrac{f}{g}$ yazılıp pay ve payda $g$ ile çarpılınca $q'=\\dfrac{f'g-fg'}{g^2}$ bulunur. Böylece bölüm kuralı, çarpım kuralının doğal bir sonucu olarak ortaya çıkar.",
            "Kural doğrudan türevin tanımından da ispatlanabilir, ama bu yol daha uzundur. İspatın bu biçimi, kuralı unutan birinin onu çarpım kuralından birkaç satırda yeniden kurabileceğini de gösterir.",
        ]},
        {"baslik": "Kuralın sezgisel anlamı", "icerik": [
            "Bir kesrin payı büyürse kesir büyür, paydası büyürse kesir küçülür. Bölüm kuralındaki iki terim bu iki etkiyi ayrı ayrı ölçer: $f'g$ terimi payın büyümesinin artırıcı etkisini, $-fg'$ terimi ise paydanın büyümesinin azaltıcı etkisini gösterir.",
            "İki etki birbirine eşitse türev sıfır olur ve oran o an değişmez. Paydadaki $g^2$ ise etkilerin paydanın büyüklüğüne göre ölçeklenmesinden gelir: büyük bir paydaya bölünen kesirde küçük değişimler oranı daha az etkiler.",
        ]},
        {"baslik": "Paydaki sıra neden önemli?", "icerik": [
            "Çarpım kuralında terimlerin sırası önemsizdir, çünkü toplama değişmelidir. Bölüm kuralında ise terimler arasında eksi işareti vardır ve sıra değişirse sonucun işareti ters döner.",
            dikkat(
                "Paydaki terimleri $f g'-f' g$ sırasıyla yazmak.",
                "Bu yazım doğru sonucun tam tersini verir. Sıra, önce payın türeviyle başlayacak biçimde yazılmalıdır. Emin olunamadığında $\\dfrac{x}{1}$ gibi basit bir bölümle denemek doğru sırayı gösterir: sonuç $1$ çıkmalıdır."),
        ]},
        {"baslik": "İlk örnek", "icerik": [
            "Kuralın uygulanışı her zaman aynı adımlarla yürür: pay ve payda ayrı ayrı adlandırılır, türevleri yazılır, formüle yerleştirilir ve pay sadeleştirilir. Payda genellikle açılmadan kare olarak bırakılır.",
            ornek(
                "$h(x)=\\dfrac{x+1}{x-1}$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "$f=x+1$, $g=x-1$ ve $f'=g'=1$ olur: $h'(x)=\\dfrac{1 \\cdot (x-1)-(x+1) \\cdot 1}{(x-1)^2}$.",
                "Pay $-2$ ye sadeleşir: $h'(x)=-\\dfrac{2}{(x-1)^2}$."),
            "Türev her $x \\neq 1$ için negatiftir; bu yüzden fonksiyon $x=1$ in solunda da sağında da azalandır. Paydanın kare olması, türevin işaretini yalnızca payın belirlediğini gösterir.",
        ]},
        {"baslik": "Paydası ikinci dereceden bölüm", "icerik": [
            "Paydanın türevi birinci dereceden bir ifadeyse paydaki çarpımlar biraz daha uzun olur. Yine de açıp sadeleştirmek genellikle kısa bir ifade verir.",
            ornek(
                "$h(x)=\\dfrac{x}{x^2+1}$ fonksiyonu verilsin.",
                "Türevini ve türevin sıfır olduğu noktaları bulalım.",
                "$h'(x)=\\dfrac{1 \\cdot (x^2+1)-x \\cdot 2x}{(x^2+1)^2}=\\dfrac{1-x^2}{(x^2+1)^2}$ olur.",
                "Pay $x=-1$ ve $x=1$ de sıfırdır; türev bu iki noktada sıfır olur."),
            "Payda hiçbir zaman sıfır olmadığı için bu fonksiyon her yerde türevlidir. Türevin $-1$ ile $1$ arasında pozitif, dışında negatif olması, fonksiyonun $x=1$ de en büyük, $x=-1$ de en küçük değerini aldığını gösterir.",
        ]},
        {"baslik": "Doğrusal kesirler için kısa yol", "icerik": [
            "Pay ve paydası birinci dereceden olan $\\dfrac{ax+b}{cx+d}$ biçimindeki kesirlerde, bölüm kuralı uygulandığında $x$ li terimler birbirini götürür ve pay her zaman sabit bir sayıya sadeleşir. Bu sayı katsayılardan doğrudan hesaplanır:",
            "$$\\left(\\dfrac{ax+b}{cx+d}\\right)'=\\dfrac{ad-bc}{(cx+d)^2}$$",
            ornek(
                "$h(x)=\\dfrac{2x+3}{x+4}$ fonksiyonu verilsin.",
                "Türevini kısa yolla bulalım.",
                "$a=2$, $b=3$, $c=1$, $d=4$ olduğundan $ad-bc=8-3=5$ olur.",
                "$h'(x)=\\dfrac{5}{(x+4)^2}$ bulunur; fonksiyon her iki aralıkta da artandır."),
        ]},
        {"baslik": "Ters fonksiyon kuralı", "icerik": [
            "Payı sabit olan bölümler için kural kısalır. $f=1$ alınırsa $f'=0$ olur ve birinci terim kaybolur. Pay başka bir sabitse sonuç o sabitle çarpılır:",
            "$$\\left(\\dfrac{1}{g}\\right)'=-\\dfrac{g'}{g^2}$$",
            ornek(
                "$h(x)=\\dfrac{1}{x^2+1}$ fonksiyonu verilsin.",
                "Türevini bulalım.",
                "$g=x^2+1$ ve $g'=2x$ olur.",
                "$h'(x)=-\\dfrac{2x}{(x^2+1)^2}$ bulunur."),
            "Aynı sonuç zincir kuralıyla da bulunur: $(x^2+1)^{-1}$ in türevi $-(x^2+1)^{-2} \\cdot 2x$ tir. İki yolun aynı sonucu vermesi kuralların tutarlılığını gösterir.",
        ]},
        {"baslik": "Paydada kök", "icerik": [
            "Payı sabit ve paydası kök olan kesirlerde ters fonksiyon kuralı ya da negatif kesirli üs kullanılır. İki yol da aynı sonucu verir ve sonuç çoğu zaman kök içeren bir kesir olarak yazılır.",
            ornek(
                "$h(x)=\\dfrac{1}{\\sqrt{x}}$ fonksiyonu verilsin, $x>0$.",
                "Türevini iki yoldan bulalım.",
                "Ters fonksiyon kuralıyla $-\\dfrac{\\dfrac{1}{2\\sqrt{x}}}{x}=-\\dfrac{1}{2x\\sqrt{x}}$ olur.",
                "Üslü yazımla $h(x)=x^{-1/2}$ ve $h'(x)=-\\dfrac{1}{2}x^{-3/2}$ olur; iki sonuç aynıdır."),
        ]},
        {"baslik": "Pay ve paydada aynı ifade", "icerik": [
            "Pay ve paydada benzer ifadeler bulunuyorsa kesir önce bir sabit ile daha basit bir kesrin farkı olarak yazılabilir. Bu dönüşüm türevi kısaltır ve bölüm kuralıyla bulunan sonucu denetlemeye yarar.",
            ornek(
                "$h(x)=\\dfrac{x^2}{x^2+1}$ fonksiyonu verilsin.",
                "Türevini iki yoldan bulalım.",
                "Bölüm kuralıyla $\\dfrac{2x(x^2+1)-x^2 \\cdot 2x}{(x^2+1)^2}=\\dfrac{2x}{(x^2+1)^2}$ olur.",
                "$h(x)=1-\\dfrac{1}{x^2+1}$ yazılırsa ters fonksiyon kuralıyla da $\\dfrac{2x}{(x^2+1)^2}$ bulunur."),
        ]},
        {"baslik": "Bir noktadaki türev değeri", "icerik": [
            "Fonksiyonların kendileri yerine bir noktadaki değerleri ve türev değerleri verilirse bölüm kuralı bu dört sayıyla doğrudan uygulanır.",
            ornek(
                "$f(1)=2$, $f'(1)=3$, $g(1)=4$ ve $g'(1)=-1$ olsun.",
                "$\\left(\\dfrac{f}{g}\\right)'(1)$ değerini bulalım.",
                "$\\dfrac{f'(1)g(1)-f(1)g'(1)}{g(1)^2}=\\dfrac{3 \\cdot 4-2 \\cdot (-1)}{16}$ olur.",
                "$\\dfrac{14}{16}=\\dfrac{7}{8}$ bulunur."),
            "Bu tür sorularda işaret hatası sık yapılır: $g'(1)$ negatif olduğu için paydaki ikinci terim çıkarılırken işaret artıya döner.",
        ]},
        {"baslik": "Tanjant ve kotanjantın türevi", "icerik": [
            "Tanjant ve kotanjantın türevleri bölüm kuralının en önemli uygulamalarıdır. İkisi de temel özdeşlik $\\sin^2 x+\\cos^2 x=1$ ile sadeleşir.",
            ornek(
                "$\\tan x=\\dfrac{\\sin x}{\\cos x}$ ve $\\cot x=\\dfrac{\\cos x}{\\sin x}$ yazılsın.",
                "Türevlerini bulalım.",
                "$(\\tan x)'=\\dfrac{\\cos^2 x+\\sin^2 x}{\\cos^2 x}=\\dfrac{1}{\\cos^2 x}$ olur.",
                "$(\\cot x)'=\\dfrac{-\\sin^2 x-\\cos^2 x}{\\sin^2 x}=-\\dfrac{1}{\\sin^2 x}$ olur."),
            "Tanjantın türevi her yerde pozitiftir; bu yüzden tanjant tanımlı olduğu her aralıkta artandır. Kotanjantın türevi ise her yerde negatiftir ve kotanjant her aralıkta azalandır.",
        ]},
        {"baslik": "Tanjantın iki yazımı", "icerik": [
            "Tanjantın türevi iki farklı biçimde yazılır: $\\dfrac{1}{\\cos^2 x}$ ve $1+\\tan^2 x$. İki biçim eşittir; çünkü $1+\\tan^2 x$ ifadesinde paydalar eşitlenince $\\dfrac{\\cos^2 x+\\sin^2 x}{\\cos^2 x}=\\dfrac{1}{\\cos^2 x}$ olur.",
            "Soruda tanjant değerleri verilmişse ikinci biçim, kosinüs değerleri verilmişse birinci biçim işi kısaltır. Örneğin $x=\\dfrac{\\pi}{4}$ de $\\tan x=1$ olduğundan türev $1+1=2$ dir; $\\cos x=\\dfrac{\\sqrt{2}}{2}$ ile birinci biçim de $\\dfrac{1}{1/2}=2$ verir.",
        ]},
        {"baslik": "Trigonometrik bölüm", "icerik": [
            "Sinüsün $x$ e bölümü gibi ifadelerde bölüm kuralı, türevin pay ve paydasını ayrı ayrı yorumlamaya elverişli bir biçim verir. Bu fonksiyon limit konusunda da önemlidir; sıfırdaki limiti $1$ dir ama o noktada tanımsızdır.",
            ornek(
                "$h(x)=\\dfrac{\\sin x}{x}$ fonksiyonu verilsin, $x \\neq 0$.",
                "Türevini ve $h'(\\pi)$ değerini bulalım.",
                "$h'(x)=\\dfrac{x\\cos x-\\sin x}{x^2}$ olur.",
                "$h'(\\pi)=\\dfrac{\\pi \\cdot (-1)-0}{\\pi^2}=-\\dfrac{1}{\\pi}$ bulunur."),
        ]},
        {"baslik": "Üstel fonksiyonlu bölüm", "icerik": [
            "Payda ya da paydada üstel fonksiyon varsa, türevde bu fonksiyon ortak çarpan olarak ortaya çıkar. Ortak çarpan alınınca türevin sıfırları kolayca görülür; üstel fonksiyon hiçbir zaman sıfır olmadığı için yalnızca kalan çarpana bakılır.",
            ornek(
                "$h(x)=\\dfrac{e^x}{x}$ fonksiyonu verilsin, $x \\neq 0$.",
                "Türevini ve türevin sıfır olduğu noktayı bulalım.",
                "$h'(x)=\\dfrac{e^x \\cdot x-e^x \\cdot 1}{x^2}=\\dfrac{e^x(x-1)}{x^2}$ olur.",
                "$e^x$ hiç sıfır olmadığı için türev yalnızca $x=1$ de sıfırdır."),
        ]},
        {"baslik": "Logaritmik bölüm", "icerik": [
            "Logaritmanın bir polinoma bölümünde logaritmanın türevi olan $\\dfrac{1}{x}$ paydaki $x$ ile sadeleşir. Sonuç, logaritmayı içeren kısa bir pay verir. Logaritma yalnızca pozitif sayılarda tanımlı olduğu için bu fonksiyonlar $x>0$ için incelenir.",
            ornek(
                "$h(x)=\\dfrac{\\ln x}{x}$ fonksiyonu verilsin, $x>0$.",
                "Türevini ve türevin sıfır olduğu noktayı bulalım.",
                "$h'(x)=\\dfrac{\\dfrac{1}{x} \\cdot x-\\ln x \\cdot 1}{x^2}=\\dfrac{1-\\ln x}{x^2}$ olur.",
                "$\\ln x=1$ ise $x=e$ bulunur; fonksiyon en büyük değerini bu noktada alır ve bu değer $\\dfrac{1}{e}$ dir."),
        ]},
        {"baslik": "Önce sadeleştirmek", "icerik": [
            "Bölüm kuralı her kesirde zorunlu değildir. Pay ve payda ortak çarpan içeriyorsa önce sadeleştirmek, paydası tek terimliyse terimlere ayırmak ve paydası yalnızca bir kuvvet olan kesirleri negatif üslü yazmak çok daha kısadır.",
            ornek(
                "$h(x)=\\dfrac{x^2-1}{x-1}$ ve $k(x)=\\dfrac{5}{x^3}$ fonksiyonları verilsin.",
                "Türevlerini en kısa yoldan bulalım.",
                "$x \\neq 1$ için $h(x)=x+1$ olduğundan $h'(x)=1$ olur.",
                "$k(x)=5x^{-3}$ olduğundan $k'(x)=-15x^{-4}=-\\dfrac{15}{x^4}$ olur."),
        ]},
        {"baslik": "Bölüm ve zincir birlikte", "icerik": [
            "Pay ya da paydada kök veya kuvvet bulunuyorsa o parçanın türevi zincir kuralıyla alınır ve bölüm kuralına yerleştirilir. Sonuç, paydaki kesirler ortak paydada birleştirilerek sadeleştirilir.",
            ornek(
                "$h(x)=\\dfrac{\\sqrt{x}}{x+1}$ fonksiyonu verilsin.",
                "Türevini bulup sadeleştirelim.",
                "$h'(x)=\\dfrac{\\dfrac{1}{2\\sqrt{x}}(x+1)-\\sqrt{x}}{(x+1)^2}$ olur.",
                "Pay ortak paydayla $\\dfrac{1-x}{2\\sqrt{x}}$ olur; $h'(x)=\\dfrac{1-x}{2\\sqrt{x}(x+1)^2}$ ve $h'(1)=0$ bulunur."),
            "Zincir kuralının ayrıntısı için <a href=\"/blog/zincir-kurali/\">Bileşke Fonksiyonun Türevi: Zincir Kuralı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Bölüm kuralıyla teğet", "icerik": [
            "Kesirli bir eğrinin teğet doğrusu, bölüm kuralıyla bulunan eğim ve fonksiyon değeriyle yazılır. Nokta ve eğim bilindiğinde doğru denklemi tek adımda bulunur.",
            ornek(
                "$y=\\dfrac{x+1}{x-1}$ eğrisi ve $x=2$ noktası verilsin.",
                "Bu noktadaki teğet denklemini bulalım.",
                "$y(2)=3$ ve $y'(2)=-\\dfrac{2}{1}=-2$ olur.",
                "Teğet $y-3=-2(x-2)$, yani $y=-2x+7$ olur."),
            "Teğet denklemi için daha fazla örnek <a href=\"/blog/teget-denklemi/\">Türevde Teğet Denklemi Nasıl Bulunur?</a> yazısında.",
        ]},
        {"baslik": "Türevin işareti", "icerik": [
            "Bölüm kuralında payda bir kare olduğu için tanımlı olduğu her yerde pozitiftir. Bu yüzden türevin işaretini yalnızca pay belirler ve işaret tablosu yalnızca paya bakılarak yapılır.",
            "Örneğin $\\dfrac{x}{x^2+1}$ in türevinin payı $1-x^2$ dir: $-1$ ile $1$ arasında pozitif, dışında negatiftir. Doğrusal kesirlerde ise pay sabit olduğu için türev her yerde aynı işaretlidir ve fonksiyon her aralıkta ya hep artar ya hep azalır.",
        ]},
        {"baslik": "Parametreli bölüm", "icerik": [
            "Payda ya da payda bir bilinmeyen varsa ve bir noktadaki türev değeri verilmişse, bölüm kuralı uygulanıp nokta yerine yazılır ve bilinmeyen bulunur.",
            ornek(
                "$h(x)=\\dfrac{ax+1}{x+2}$ ve $h'(0)=\\dfrac{5}{4}$ olsun.",
                "$a$ değerini bulalım.",
                "Kısa yolla $h'(x)=\\dfrac{2a-1}{(x+2)^2}$ olur; $h'(0)=\\dfrac{2a-1}{4}$.",
                "$2a-1=5$ denkleminden $a=3$ bulunur."),
        ]},
        {"baslik": "Bölümün ikinci türevi", "icerik": [
            "İkinci türev için bölüm kuralı ikinci kez uygulanır. Sonuç çoğu zaman uzundur; bu yüzden mümkünse ifade önce negatif üslü biçime çevrilir ya da birinci türev sadeleştirildikten sonra ikinci kez türev alınır.",
            ornek(
                "$h(x)=\\dfrac{1}{x}$ fonksiyonu verilsin.",
                "İkinci türevini bulalım.",
                "$h'(x)=-\\dfrac{1}{x^2}=-x^{-2}$ olur.",
                "$h''(x)=2x^{-3}=\\dfrac{2}{x^3}$ bulunur."),
        ]},
        {"baslik": "Uygulama: ortalama maliyet", "icerik": [
            "Toplam maliyetin üretim miktarına bölümü birim başına ortalama maliyeti verir ve bir bölüm olduğu için türevi bölüm kuralıyla alınır. Ortalama maliyetin türevi, üretim arttıkça birim maliyetin nasıl değiştiğini gösterir.",
            ornek(
                "Toplam maliyet $C(x)=100+5x$ TL olsun; ortalama maliyet $A(x)=\\dfrac{100+5x}{x}$ tir.",
                "Ortalama maliyetin türevini bulalım ve yorumlayalım.",
                "Kısa yolla $A'(x)=\\dfrac{5 \\cdot 0-100 \\cdot 1}{x^2}=-\\dfrac{100}{x^2}$ olur.",
                "Türev her zaman negatiftir; üretim arttıkça sabit maliyet daha çok birime bölündüğü için birim maliyet düşer."),
        ]},
        {"baslik": "Uygulama: ilaç derişimi", "icerik": [
            "Kandaki ilaç derişimi bazı modellerde bir bölümle ifade edilir. Türevin sıfır olduğu an, derişimin en yüksek olduğu andır.",
            ornek(
                "Derişim $c(t)=\\dfrac{5t}{t^2+1}$ miligram bölü litre olsun; $t$ saat cinsindendir.",
                "Derişimin en yüksek olduğu anı ve değeri bulalım.",
                "$c'(t)=\\dfrac{5(t^2+1)-5t \\cdot 2t}{(t^2+1)^2}=\\dfrac{5(1-t^2)}{(t^2+1)^2}$ olur; türev $t=1$ de sıfırdır.",
                "Derişim ilk bir saatte artar, sonra azalır; en yüksek değer $c(1)=2.5$ miligram bölü litredir."),
        ]},
        {"baslik": "Kural seçimi", "icerik": [
            tablo(["Kesir", "Önerilen yol"], [
                ["Pay ve payda ortak çarpanlı", "Önce sadeleştir"],
                ["Payda tek terim", "Terimlere ayır"],
                ["$\\dfrac{c}{x^n}$", "Negatif üslü kuvvet kuralı"],
                ["$\\dfrac{ax+b}{cx+d}$", "$\\dfrac{ad-bc}{(cx+d)^2}$"],
                ["$\\dfrac{1}{g}$", "$-\\dfrac{g'}{g^2}$"],
                ["Diğer bölümler", "Bölüm kuralı"],
            ]),
            "Hangi yol seçilirse seçilsin sonuç aynıdır. Yol seçimi yalnızca işlem uzunluğunu ve hata olasılığını değiştirir.",
        ]},
        {"baslik": "Sınavda bölümün türevi", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) bölümün türevi; fonksiyon değerleri verilen sorular, doğrusal kesirler, tanjantın türevi ve bir noktadaki türev değeri biçiminde karşına çıkabilir.",
                "Bölüm kuralı ekstremum ve artan azalan sorularında da sık kullanılır."),
            "Doğrusal kesir görüyorsan $ad-bc$ kısa yolunu kullan. Türevin işareti soruluyorsa paydayı hesaplamaya gerek yok; payda karedir ve pozitiftir, işareti yalnızca pay belirler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\left(\\dfrac{f}{g}\\right)'=\\dfrac{f'}{g'}$", "Bölüm kuralı kullanılır"],
                ["Payda $f g'-f' g$ yazmak", "$f' g-f g'$"],
                ["Paydayı $g$ bırakmak", "Payda $g^2$ dir"],
                ["Paydaki eksiyi dağıtmayı unutmak", "Parantez açılırken işaret değişir"],
                ["Önce sadeleştirmeden kural uygulamak", "Kısa yolu kaçırmak"],
                ["Paydanın sıfır olduğu noktada türev yazmak", "Orada fonksiyon tanımsız"],
            ]),
            "En sık hata paydaki sıradır. Kuralı $\\dfrac{x}{1}$ ile denemek hatayı hemen ortaya çıkarır: doğru sıra $\\dfrac{1 \\cdot 1-x \\cdot 0}{1}=1$ verir.",
        ]},
    ],
    "sss": [
        ("Bölümün türevi nasıl alınır?",
         "Payın türevi paydayla çarpılır, pay paydanın türeviyle çarpılır, bu iki çarpımın farkı paydanın karesine bölünür. Paydaki sıra önemlidir: önce payın türevi yazılır."),
        ("Bölümün türevi türevlerin bölümü müdür?",
         "Hayır. x kare bölü x in türevi 1 iken türevlerin bölümü 2x olur."),
        ("ax + b bölü cx + d nin türevi nedir?",
         "ad eksi bc bölü (cx + d) nin karesidir. Pay sabit olduğu için türev her yerde aynı işaretlidir."),
        ("1 bölü g nin türevi nedir?",
         "Eksi g üssü bölü g nin karesidir."),
        ("tan x in türevi bölüm kuralıyla nasıl bulunur?",
         "tan x, sin x bölü cos x olarak yazılır. Bölüm kuralı ve temel özdeşlikle türev 1 bölü cos kare x çıkar."),
        ("Bölümün türevinin işaretini ne belirler?",
         "Payda bir kare olduğu için pozitiftir. Türevin işaretini yalnızca pay belirler."),
        ("Bölüm kuralı ne zaman gereksizdir?",
         "Kesir sadeleşiyorsa, paydası tek terimliyse ya da yalnızca x in bir kuvvetiyse önce sadeleştirmek, terimlere ayırmak ya da negatif üslü yazmak daha kısadır."),
        ("Bölüm kuralı nasıl ispatlanır?",
         "Bölüm q ise f eşittir q çarpı g dir. Bu eşitliğe çarpım kuralı uygulanır ve q üssü yalnız bırakılınca bölüm kuralı elde edilir."),
    ],
    "kontrol": [
        "Bölümün türevinin neden türevlerin bölümü olmadığını açıklayabiliyorum.",
        "Bölüm kuralını doğru sırayla yazabiliyorum.",
        "Bölüm kuralını çarpım kuralından ispatlayabiliyorum.",
        "Doğrusal kesirler için kısa formülü kullanabiliyorum.",
        "Ters fonksiyon kuralını uygulayabiliyorum.",
        "Değerleri verilen fonksiyonlarla bir noktadaki türevi hesaplayabiliyorum.",
        "Tanjant ve kotanjantın türevini bölüm kuralıyla bulabiliyorum.",
        "Üstel, logaritmik ve trigonometrik bölümlerin türevini alabiliyorum.",
        "Gerektiğinde önce sadeleştirip kısa yolu seçebiliyorum.",
        "Bölüm kuralını maliyet ve derişim problemlerinde kullanabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["carpimin-turevi", "zincir-kurali", "turev-alma-kurallari"],
}
