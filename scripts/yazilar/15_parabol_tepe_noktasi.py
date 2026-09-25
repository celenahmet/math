# scripts/yazilar/15_parabol_tepe_noktasi.py — Parabolun Tepe Noktasi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "parabol-tepe-noktasi",
    "baslik": "Parabolün Tepe Noktası Nasıl Bulunur?",
    "aciklama": "Parabolün tepe noktası nasıl bulunur? Formül, tam kareye tamamlama, köklerden tepe, en büyük ve en küçük değer, kapalı aralık ve parametreler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["AYT"],
    "kapak": "parabol-tepe-noktasi",
    "kapak_alt": "Parabolün tepe noktası: ızgaralı bir tahtada parabolün en alt noktasını ve simetri eksenini gösteren iki öğrenci",
    "ozet": "Tepe noktası, parabolün en alçak ya da en yüksek noktasıdır ve parabol sorularının neredeyse hepsi bu noktadan geçer: simetri ekseni, en büyük ya da en küçük değer, görüntü kümesi ve artan azalan aralıklar tepe noktasından okunur. Bu yazıda tepe noktası formülünü ve nereden geldiğini, tam kareye tamamlamayı, köklerden ve simetrik noktalardan tepe bulmayı, tepe noktasıyla en büyük ve en küçük değer problemlerini, kapalı aralıkları ve parametreli soruları çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Tepe noktası nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için parabolün genel yapısını ve tam kareye tamamlamayı biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/parabol-konu-anlatimi/\">Parabol Konu Anlatımı</a> yazısına göz at."),
            "Parabolün simetri ekseni üzerinde bulunan noktasına <strong>tepe noktası</strong> denir ve genellikle $T(r, k)$ ile gösterilir. Kolları yukarı bakan bir parabolde tepe noktası eğrinin en alçak noktasıdır; kolları aşağı bakan bir parabolde ise en yüksek noktasıdır.",
            "Kapaktaki öğrenciler tahtadaki parabolün en alt noktasını işaretliyor ve bu noktadan geçen dikey bir çubukla simetri eksenini gösteriyor. Eğrinin iki kolu bu çubuğa göre birbirinin aynasıdır; tepe noktası da iki kolun buluştuğu tek noktadır.",
            hap("Tepe noktası $T(r, k)$, simetri ekseni $x=r$ dir.",
                "$a>0$ ise tepe en alçak, $a<0$ ise en yüksek noktadır."),
        ]},
        {"baslik": "Tepe noktası formülü", "icerik": [
            "$y=ax^2+bx+c$ parabolünün tepe noktası şu formüllerle bulunur. Yatay koordinat simetri eksenidir; dikey koordinat ise bu değerin fonksiyonda yerine yazılmasıyla ya da diskriminant yardımıyla hesaplanır:",
            tablo(["Koordinat", "Formül"], [
                ["$r$", "$-\\dfrac{b}{2a}$"],
                ["$k$", "$f(r)$ ya da $-\\dfrac{\\Delta}{4a}$"],
            ]),
            "İki yol da aynı sonucu verir. Katsayılar küçük tam sayılarsa $f(r)$ hesaplamak genellikle daha hızlıdır; $r$ kesirli çıktığında ise $-\\dfrac{\\Delta}{4a}$ formülü kesirli bir sayının karesini almaktan kurtarır ve hata payını azaltır.",
        ]},
        {"baslik": "Formül nereden gelir?", "icerik": [
            "Tepe noktası formülü, genel denklemin tam kareye tamamlanmasıyla elde edilir. $a$ ortak paranteze alınır ve parantez içi bir tam kareye tamamlanır:",
            "$$y=a\\left(x+\\dfrac{b}{2a}\\right)^2-\\dfrac{b^2-4ac}{4a}$$",
            "Kare terim her zaman sıfır ya da pozitiftir ve yalnızca $x=-\\dfrac{b}{2a}$ için sıfır olur. Bu noktada $y$ nin değeri $-\\dfrac{\\Delta}{4a}$ dır. $a>0$ ise kare terim büyüdükçe $y$ artar, bu yüzden bu değer en küçük değerdir; $a<0$ ise kare terim $y$ yi azaltır ve bu değer en büyük değerdir.",
        ]},
        {"baslik": "İlk örnek", "icerik": [
            "Formülün iki yolunu aynı parabol üzerinde karşılaştırmak, hangisinin ne zaman daha pratik olduğunu gösterir.",
            ornek(
                "$y=x^2-6x+5$ parabolü verilsin.",
                "Tepe noktasını iki yoldan bulalım.",
                "$r=-\\dfrac{-6}{2}=3$ ve $k=f(3)=9-18+5=-4$.",
                "Diskriminantla: $\\Delta=36-20=16$ ve $k=-\\dfrac{16}{4}=-4$. Tepe noktası $T(3, -4)$ tür."),
            koordinat_grafik("y = x² − 6x + 5 parabolü: tepe noktası ve simetrik noktalar", [("y = x² − 6x + 5", lambda x: x * x - 6 * x + 5)], (-1, 7), (-5, 6),
                             dikeyler=[3], noktalar=[(3, -4, "T(3, −4)", True), (1, 0, "(1, 0)", True), (5, 0, "(5, 0)", True), (0, 5, "(0, 5)", True), (6, 5, "(6, 5)", True)]),
            "Grafikte simetri de görülür: $(1, 0)$ ile $(5, 0)$ ve $(0, 5)$ ile $(6, 5)$ noktaları $x=3$ doğrusuna eşit uzaklıktadır ve aynı yüksekliktedir. Tepe noktası, bu simetrik nokta çiftlerinin tam ortasında ve hepsinden daha alçaktadır.",
        ]},
        {"baslik": "Kesirli tepe noktası", "icerik": [
            "Simetri ekseni kesirli çıktığında $f(r)$ hesabı kesirlerin karesini gerektirir ve hata yapma olasılığı artar. Bu durumda dikey koordinat için $-\\dfrac{\\Delta}{4a}$ formülü çok daha kısadır.",
            ornek(
                "$y=2x^2-3x+1$ parabolü verilsin.",
                "Tepe noktasını bulalım.",
                "$r=-\\dfrac{-3}{4}=\\dfrac{3}{4}$.",
                "$\\Delta=9-8=1$ ve $k=-\\dfrac{1}{8}$. Tepe noktası $T(\\dfrac{3}{4}, -\\dfrac{1}{8})$ dir."),
            "Aynı sonuç $f(\\dfrac{3}{4})=2 \\cdot \\dfrac{9}{16}-\\dfrac{9}{4}+1=\\dfrac{9}{8}-\\dfrac{18}{8}+\\dfrac{8}{8}=-\\dfrac{1}{8}$ hesabıyla da bulunur; ama bu yol birkaç ek adım ister.",
        ]},
        {"baslik": "Kolları aşağı bakan parabol", "icerik": [
            "Baş katsayı negatifse tepe noktası parabolün en yüksek noktasıdır. Formül aynıdır; yalnızca yorum değişir: bulunan $k$ değeri en küçük değil, en büyük değerdir.",
            ornek(
                "$y=-2x^2+8x-3$ parabolü verilsin.",
                "Tepe noktasını ve en büyük değeri bulalım.",
                "$r=-\\dfrac{8}{-4}=2$ ve $k=-8+16-3=5$.",
                "Tepe noktası $T(2, 5)$ tir; fonksiyonun en büyük değeri $5$ tir."),
            dikkat(
                "$a$ negatifken formülde işaret karıştırmak.",
                "$-\\dfrac{b}{2a}$ hesaplanırken $a=-2$ işaretiyle birlikte yazılır: $-\\dfrac{8}{2 \\cdot (-2)}=2$. İşaret unutulursa $r=-2$ bulunur ve bütün sonuç yanlış olur."),
        ]},
        {"baslik": "Tam kareye tamamlayarak tepe bulmak", "icerik": [
            "Formülü kullanmadan, parabolü doğrudan $y=a(x-r)^2+k$ biçimine getirerek de tepe noktası bulunur. Bu yol hem tepe noktasını hem parabolün ötelenme bilgisini birlikte verir.",
            ornek(
                "$y=x^2+4x+7$ parabolü verilsin.",
                "Tam kareye tamamlayarak tepe noktasını bulalım.",
                "$x^2+4x$ ifadesine $4$ eklenip çıkarılır: $y=(x^2+4x+4)+3$.",
                "$y=(x+2)^2+3$; tepe noktası $T(-2, 3)$ tür."),
            "Parantez içindeki işarete dikkat edilmelidir: $(x+2)^2$ ifadesi $(x-(-2))^2$ demektir, bu yüzden tepe noktasının yatay koordinatı $-2$ dir.",
        ]},
        {"baslik": "Baş katsayı 1 değilken tam kare", "icerik": [
            "Baş katsayı $1$ değilse önce $a$, $x$ li terimlerden ortak paranteze alınır; tam kare parantez içinde tamamlanır ve eklenen sayının $a$ katı dışarıdan çıkarılır.",
            ornek(
                "$y=2x^2-8x+5$ parabolü verilsin.",
                "Tam kareye tamamlayarak tepe noktasını bulalım.",
                "$y=2(x^2-4x)+5=2(x^2-4x+4)-8+5$.",
                "$y=2(x-2)^2-3$; tepe noktası $T(2, -3)$ tür."),
            dikkat(
                "Parantez içine eklenen sayıyı dışarıdan olduğu gibi çıkarmak.",
                "Parantez içine $4$ eklenince ifadeye aslında $2 \\cdot 4=8$ eklenmiş olur. Bu yüzden dışarıdan $4$ değil $8$ çıkarılır."),
        ]},
        {"baslik": "Köklerden tepe noktası", "icerik": [
            "Parabolün kökleri biliniyorsa simetri ekseni köklerin ortalamasıdır, çünkü parabol köklere göre simetriktir. Tepe noktasının dikey koordinatı da bu değer yerine yazılarak bulunur.",
            ornek(
                "$y=(x-2)(x-6)$ parabolü verilsin.",
                "Tepe noktasını bulalım.",
                "Kökler $2$ ve $6$; $r=\\dfrac{2+6}{2}=4$.",
                "$k=(4-2)(4-6)=-4$. Tepe noktası $T(4, -4)$ tür."),
        ]},
        {"baslik": "Simetrik noktalardan tepe", "icerik": [
            "Parabol üzerinde aynı yükseklikteki iki nokta biliniyorsa simetri ekseni bu iki noktanın yatay koordinatlarının ortalamasıdır. Kökler bu kuralın özel bir durumudur: iki kök de sıfır yüksekliğindedir.",
            ornek(
                "Bir parabolde $f(1)=f(7)$ olduğu biliniyor.",
                "Parabolün simetri eksenini bulalım.",
                "Aynı yükseklikteki iki noktanın ortalaması alınır.",
                "$r=\\dfrac{1+7}{2}=4$; simetri ekseni $x=4$ tür."),
        ]},
        {"baslik": "Simetrik noktaların yüksekliği", "icerik": [
            "Tepe noktasına eşit uzaklıktaki iki noktada parabol aynı değeri alır: her $d$ için $f(r+d)=f(r-d)$ dir. Bu özellik, değer tablosu kurarken hesap sayısını yarıya indirir ve bir değeri bilinen noktanın simetriğini hemen verir.",
            ornek(
                "$f(x)=x^2-6x+5$ fonksiyonunun tepe noktası $x=3$ tedir.",
                "Simetrik noktaların değerlerini karşılaştıralım.",
                "$f(0)=5$ ve $f(6)=36-36+5=5$.",
                "$f(2)=4-12+5=-3$ ve $f(4)=16-24+5=-3$."),
        ]},
        {"baslik": "Tepe noktasının eksene göre konumu", "icerik": [
            "Tepe noktasının dikey koordinatı $-\\dfrac{\\Delta}{4a}$ olduğu için, kolları yukarı bakan bir parabolde diskriminant pozitifse tepe noktası $x$ ekseninin altında, negatifse üstündedir. Bu, diskriminantın kök sayısını neden belirlediğinin grafik açıklamasıdır.",
            ornek(
                "$y=x^2-2x+3$ parabolü verilsin.",
                "Tepe noktasını ve parabolün $x$ eksenini kesip kesmediğini bulalım.",
                "$\\Delta=4-12=-8$ ve $k=-\\dfrac{-8}{4}=2$; tepe noktası $T(1, 2)$ dir.",
                "Kollar yukarı bakıyor ve en alçak nokta eksenin üstünde; parabol $x$ eksenini kesmez."),
        ]},
        {"baslik": "Tepe noktasından denklem yazmak", "icerik": [
            "Tepe noktası ve parabol üzerindeki bir nokta biliniyorsa denklem tepe noktası biçimiyle kurulur. Bilinmeyen yalnızca baş katsayıdır ve verilen nokta yerine yazılarak bulunur.",
            ornek(
                "Tepe noktası $(2, -3)$ olan ve $(0, 5)$ noktasından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$y=a(x-2)^2-3$ ve $x=0$ için $5=4a-3$; $a=2$.",
                "$y=2(x-2)^2-3=2x^2-8x+5$."),
            "Denklem yazmanın diğer yolları <a href=\"/blog/parabol-denklemi/\">Parabol Denklemi Nasıl Yazılır?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "En küçük değer ve görüntü kümesi", "icerik": [
            "Tepe noktası bulunduğunda fonksiyonun en küçük ya da en büyük değeri ve görüntü kümesi hemen yazılır. Kolları yukarı bakan parabol tepeden aşağı inemez; bu yüzden görüntü kümesi tepe noktasının yüksekliğinden başlar.",
            ornek(
                "$f(x)=x^2-6x+5$ fonksiyonu verilsin.",
                "En küçük değeri ve görüntü kümesini bulalım.",
                "Tepe noktası $T(3, -4)$ tür ve kollar yukarıdır.",
                "En küçük değer $-4$ tür; görüntü kümesi $[-4, \\infty)$ aralığıdır."),
        ]},
        {"baslik": "Artan ve azalan aralıklar", "icerik": [
            "Tepe noktası, parabolün artan ve azalan olduğu aralıkları ayıran noktadır. Kollar yukarı bakıyorsa fonksiyon tepe noktasına kadar azalır ve sonra artar; kollar aşağı bakıyorsa önce artar, tepe noktasından sonra azalır.",
            ornek(
                "$f(x)=x^2-6x+5$ ve $g(x)=-2x^2+8x-3$ fonksiyonları verilsin.",
                "Artan ve azalan olduğu aralıkları bulalım.",
                "$f$ nin tepesi $x=3$ te, kollar yukarı: $(-\\infty, 3]$ te azalan, $[3, \\infty)$ da artan.",
                "$g$ nin tepesi $x=2$ de, kollar aşağı: $(-\\infty, 2]$ de artan, $[2, \\infty)$ da azalan."),
        ]},
        {"baslik": "Tepe noktasından köklere", "icerik": [
            "Tepe noktası biçimi kökleri bulmanın da hızlı bir yoludur. $y=a(x-r)^2+k$ sıfıra eşitlenince $(x-r)^2=-\\dfrac{k}{a}$ bulunur; bu sayı pozitifse kökler tepe noktasının iki yanında, simetri eksenine eşit uzaklıktadır.",
            ornek(
                "$y=(x-3)^2-4$ parabolü verilsin.",
                "Kökleri tepe noktasından bulalım.",
                "$(x-3)^2=4$, yani $x-3=\\pm 2$.",
                "Kökler $1$ ve $5$ tir; ikisi de simetri ekseninden $2$ birim uzaktadır."),
        ]},
        {"baslik": "Tepe noktası aralığın dışında olduğunda", "icerik": [
            "Tanım kümesi kapalı bir aralıksa en küçük ve en büyük değer için uçlara ve tepe noktasına bakılır. Tepe noktası aralığın dışındaysa fonksiyon aralıkta yalnızca artan ya da yalnızca azalan olur ve en küçük ile en büyük değer uçlarda alınır.",
            ornek(
                "$[4, 7]$ aralığında $f(x)=x^2-6x+5$ fonksiyonu verilsin.",
                "En küçük ve en büyük değeri bulalım.",
                "Tepe noktası $x=3$ te ve aralığın dışındadır; aralıkta fonksiyon artandır.",
                "En küçük değer $f(4)=16-24+5=-3$, en büyük değer $f(7)=49-42+5=12$ dir."),
            dikkat(
                "Tepe noktası aralıkta değilken onu cevap almak.",
                "Tepe noktasındaki $-4$ değeri bu aralıkta hiç alınmaz, çünkü $x=3$ aralığa ait değildir. Önce tepe noktasının aralıkta olup olmadığı kontrol edilmelidir."),
        ]},
        {"baslik": "Tepe noktası verilen parametreli parabol", "icerik": [
            "Parabolde bir parametre varsa ve tepe noktası hakkında bilgi verilmişse, tepe noktası formülü parametre için bir denklem kurar. Bulunan parametreyle parabol tamamlanır ve istenen başka özellikler hesaplanır.",
            ornek(
                "$y=x^2-2mx+m+6$ parabolünün simetri ekseni $x=3$ tür.",
                "$m$ yi ve tepe noktasını bulalım.",
                "$r=-\\dfrac{-2m}{2}=m$ olduğu için $m=3$.",
                "Parabol $y=x^2-6x+9=(x-3)^2$ olur; tepe noktası $T(3, 0)$ dır ve parabol $x$ eksenine teğettir."),
        ]},
        {"baslik": "Tepe noktası bir doğru üzerindeyse", "icerik": [
            "Tepe noktasının belirli bir doğru üzerinde olduğu biliniyorsa, tepe noktasının koordinatları doğrunun denkleminde yerine yazılır. Bu da parametre için bir denklem verir.",
            ornek(
                "$y=x^2-4x+m$ parabolünün tepe noktası $y=x$ doğrusu üzerindedir.",
                "$m$ yi bulalım.",
                "Tepe noktası: $r=2$ ve $k=4-8+m=m-4$.",
                "$y=x$ doğrusu üzerinde olduğu için $m-4=2$, yani $m=6$. Tepe noktası $(2, 2)$ dir."),
        ]},
        {"baslik": "Tepe noktası x ekseni üzerindeyse", "icerik": [
            "Tepe noktası $x$ ekseni üzerindeyse dikey koordinatı sıfırdır ve parabol eksene teğettir. Bu durum diskriminantın sıfır olmasıyla aynı anlama gelir; bu yüzden koşul $\\Delta=0$ olarak da yazılabilir.",
            ornek(
                "$y=x^2+mx+9$ parabolünün tepe noktası $x$ ekseni üzerindedir.",
                "$m$ yi bulalım.",
                "$\\Delta=m^2-36=0$.",
                "$m=6$ ya da $m=-6$. Tepe noktaları sırasıyla $(-3, 0)$ ve $(3, 0)$ dır."),
        ]},
        {"baslik": "Tepe noktasının izlediği yol", "icerik": [
            "Parametre değiştikçe parabolün tepe noktası da yer değiştirir. Tepe noktasının koordinatları parametre cinsinden yazılıp parametre yok edilirse tepe noktalarının üzerinde bulunduğu eğri bulunur.",
            ornek(
                "$y=x^2-2mx+m^2+m$ parabolleri verilsin.",
                "Tepe noktalarının üzerinde bulunduğu doğruyu bulalım.",
                "Tam kare: $y=(x-m)^2+m$; tepe noktası $(m, m)$ dir.",
                "Yatay ve dikey koordinat eşit olduğu için bütün tepe noktaları $y=x$ doğrusu üzerindedir."),
            "Parametre değiştikçe parabolün biçimi aynı kalır, yalnızca tepe noktası bu doğru boyunca kayar. Böyle sorularda tepe noktasının iki koordinatı arasındaki ilişkiyi yazmak yeterlidir.",
        ]},
        {"baslik": "Gelir problemi", "icerik": [
            "Ekonomi problemlerinde gelir çoğu zaman fiyatın ikinci dereceden bir fonksiyonudur: fiyat arttıkça birim başına kazanç artar ama satış miktarı azalır. En yüksek gelir, bu parabolün tepe noktasında elde edilir.",
            ornek(
                "Bir ürünün fiyatı $p$ lira olduğunda satış adedi $100-2p$ dir.",
                "Geliri en büyük yapan fiyatı ve en büyük geliri bulalım.",
                "Gelir: $G(p)=p(100-2p)=-2p^2+100p$.",
                "Tepe noktası: $p=-\\dfrac{100}{-4}=25$ ve $G(25)=25 \\cdot 50=1250$. En büyük gelir $1250$ liradır."),
            "Sonuç sezgiyi de doğrular: fiyat çok düşükse birim kazanç azdır, çok yüksekse satış çok azalır. En iyi fiyat, iki etkinin dengelendiği tepe noktasındadır. Fiyat $0$ ya da $50$ lira olduğunda gelir sıfırdır; en iyi fiyat bu iki değerin tam ortasındadır.",
        ]},
        {"baslik": "Duvar kenarındaki bahçe", "icerik": [
            "En büyük alan problemlerinin sık görülen bir biçiminde dikdörtgenin bir kenarı duvardır ve çit yalnızca üç kenara çekilir. Alan yine ikinci dereceden bir fonksiyondur ve en büyük değeri tepe noktasındadır.",
            ornek(
                "$40$ metre çitle, bir kenarı duvar olan dikdörtgen bir bahçe çevrilecek.",
                "En büyük alanı bulalım.",
                "Duvara dik kenarlar $x$ ise duvara paralel kenar $40-2x$ tir; alan $A(x)=x(40-2x)=-2x^2+40x$.",
                "Tepe noktası $x=10$; alan $A(10)=10 \\cdot 20=200$ metrekaredir."),
        ]},
        {"baslik": "Tepe noktası ve öteleme", "icerik": [
            "Tepe noktası biçimi $y=a(x-r)^2+k$, parabolün $y=ax^2$ parabolünden nasıl elde edildiğini de gösterir: yatayda $r$, dikeyde $k$ birim ötelenmiştir. Bu yüzden iki parabolün tepe noktaları karşılaştırılarak aralarındaki öteleme bulunur.",
            ornek(
                "$y=x^2$ ve $y=x^2-6x+5$ parabolleri verilsin.",
                "İkinci parabolün birinciden nasıl elde edildiğini bulalım.",
                "İkinci parabolün tepe noktası $(3, -4)$ tür.",
                "$y=x^2$ parabolü $3$ birim sağa ve $4$ birim aşağı ötelenmiştir: $y=(x-3)^2-4$."),
        ]},
        {"baslik": "Sınavda tepe noktası", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) tepe noktası; formülle hesaplama, en büyük ve en küçük değer, görüntü kümesi, kapalı aralıkta uç değerler ve parametreli sorular biçiminde karşına çıkabilir.",
                "Tepe noktası bir doğru üzerinde, $x$ ekseni üzerinde ya da belirli bir bölgede verilerek parametre soruları da kurulabilir."),
            "Tepe noktası sorusunda katsayılar küçükse $r$ yi bulup yerine yaz; $r$ kesirli çıkıyorsa $k$ için $-\\dfrac{\\Delta}{4a}$ formülünü kullan. Parametre içeren sorularda ise tepe noktasının iki koordinatını da parametre cinsinden yazıp verilen koşula yerleştir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$r=\\dfrac{b}{2a}$ almak", "$r=-\\dfrac{b}{2a}$"],
                ["$(x+2)^2$ de tepeyi $2$ sanmak", "Yatay koordinat $-2$"],
                ["Tam karede dışarıdan yanlış sayı çıkarmak", "Eklenenin $a$ katı çıkarılır"],
                ["$a<0$ iken tepeyi en küçük değer sanmak", "En büyük değerdir"],
                ["Aralık dışındaki tepeyi cevap almak", "Önce tepe aralıkta mı bakılır"],
                ["$k$ yı $\\dfrac{\\Delta}{4a}$ almak", "$k=-\\dfrac{\\Delta}{4a}$"],
            ]),
            "Bu hataların çoğu işaretlerle ilgilidir. Tepe noktasını bulduktan sonra fonksiyonda yerine yazıp $k$ değerini doğrulamak ve simetrik bir noktayla kontrol etmek, hatayı neredeyse her zaman yakalar.",
        ]},
    ],
    "sss": [
        ("Tepe noktası nasıl bulunur?",
         "Yatay koordinat eksi b bölü 2a dır. Dikey koordinat bu değerin fonksiyonda yerine yazılmasıyla ya da eksi delta bölü 4a formülüyle bulunur."),
        ("Tepe noktası en büyük değer midir, en küçük değer mi?",
         "Baş katsayı pozitifse tepe noktası en küçük değeri, negatifse en büyük değeri verir."),
        ("Köklerden tepe noktası nasıl bulunur?",
         "Simetri ekseni köklerin ortalamasıdır. Bu değer fonksiyonda yerine yazılınca tepe noktasının dikey koordinatı bulunur."),
        ("Tam kareye tamamlama tepe noktasını nasıl verir?",
         "Parabol a çarpı x eksi r nin karesi artı k biçimine getirilir. Tepe noktası doğrudan r ve k olarak okunur."),
        ("Kapalı aralıkta en küçük değer nasıl bulunur?",
         "Tepe noktası aralıktaysa tepe noktası ve uçlar karşılaştırılır. Aralıkta değilse yalnızca uçlardaki değerlere bakılır."),
        ("Tepe noktası x ekseni üzerindeyse ne olur?",
         "Parabol x eksenine teğettir ve diskriminant sıfırdır. Denklemin çakışık bir kökü vardır."),
        ("Simetri ekseni kesirli çıkarsa tepe noktası nasıl bulunur?",
         "Dikey koordinat için eksi delta bölü 4a formülü kullanılır. Böylece kesirli bir sayının karesini almak gerekmez ve hata payı azalır."),
    ],
    "kontrol": [
        "Tepe noktası formülünü yazabiliyorum.",
        "Formülün tam kareye tamamlamadan geldiğini açıklayabiliyorum.",
        "Tepe noktasını iki farklı yoldan hesaplayabiliyorum.",
        "Tam kareye tamamlayarak tepe noktasını bulabiliyorum.",
        "Köklerden ve simetrik noktalardan simetri eksenini bulabiliyorum.",
        "Tepe noktasından en büyük ya da en küçük değeri ve görüntü kümesini yazabiliyorum.",
        "Kapalı aralıkta en büyük ve en küçük değeri bulabiliyorum.",
        "Tepe noktası koşulundan parametre bulabiliyorum.",
        "Tepe noktalarının izlediği yolu bulabiliyorum.",
        "En büyük gelir ve alan problemlerini tepe noktasıyla çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["parabol-konu-anlatimi", "parabol-denklemi", "parabol-grafigi"],
}
