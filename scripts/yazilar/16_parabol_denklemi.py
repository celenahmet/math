# scripts/yazilar/16_parabol_denklemi.py — Parabol Denklemi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "parabol-denklemi",
    "baslik": "Parabol Denklemi Nasıl Yazılır?",
    "aciklama": "Parabol denklemi nasıl yazılır? Tepe noktası, kökler ve üç noktayla denklem, grafikten denklem, öteleme, biçimler arası geçiş ve kemer problemi; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["AYT"],
    "kapak": "parabol-denklemi",
    "kapak_alt": "Parabol denklemi: tepe noktası ve simetrik noktalardan geçen bir parabolü ızgaralı tahtada kuran iki öğrenci",
    "ozet": "Bir parabolün denklemini yazmak, onu belirleyen bilgileri doğru denklem biçimine yerleştirmektir. Tepe noktası verildiğinde bir biçim, kökler verildiğinde başka bir biçim, yalnızca noktalar verildiğinde ise genel biçim işi kısaltır. Bu yazıda parabolü belirlemek için kaç bilgi gerektiğini, tepe noktası, kökler ve noktalar yardımıyla denklem kurmayı, grafikten denklem okumayı, ötelemeyle denklem yazmayı, biçimler arasında geçişi ve kemer ile atış problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Parabol denklemi yazmak ne demektir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için parabolün yapısını ve tepe noktasını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/parabol-konu-anlatimi/\">Parabol Konu Anlatımı</a> ve <a href=\"/blog/parabol-tepe-noktasi/\">Parabolün Tepe Noktası Nasıl Bulunur?</a> yazılarına göz at."),
            "Bir parabolün denklemi $y=ax^2+bx+c$ biçimindedir ve üç katsayı içerir. Bu yüzden bir parabolü tam olarak belirlemek için genellikle birbirinden bağımsız üç bilgi gerekir: üç nokta, bir tepe noktası ve bir nokta, iki kök ve bir nokta gibi.",
            "Kapaktaki öğrenciler tahtada tepe noktasını ve iki yandaki simetrik noktaları çivilerle sabitliyor; esnek şerit bu noktalardan geçtiği anda tek bir parabol biçimini alıyor. Denklem yazmak da aynı işi cebirle yapmaktır: verilen bilgiler, katsayıları tek bir biçimde belirler.",
            hap("Parabolü belirlemek için genellikle üç bilgi gerekir.",
                "Tepe noktası iki bilgi sayılır: yatay ve dikey koordinat."),
        ]},
        {"baslik": "İki nokta neden yetmez?", "icerik": [
            "İki noktadan tek bir doğru geçer ama sonsuz sayıda parabol geçer. Bu yüzden parabol denklemi için iki nokta yeterli değildir; üçüncü bir bilgi, yani bir nokta, bir tepe noktası ya da bir simetri ekseni gerekir.",
            ornek(
                "$(0, 0)$ ve $(1, 1)$ noktaları verilsin.",
                "Bu iki noktadan geçen farklı paraboller bulalım.",
                "$y=x^2$ için $x=0$ da $0$, $x=1$ de $1$ bulunur.",
                "$y=2x^2-x$ için de $x=0$ da $0$, $x=1$ de $2-1=1$ bulunur. İki farklı parabol aynı noktalardan geçer."),
            "Aslında $y=ax^2+(1-a)x$ biçimindeki her parabol, $a \\neq 0$ olduğu sürece bu iki noktadan geçer. Üçüncü bilgi, bu ailenin içinden tek bir üyeyi seçer.",
        ]},
        {"baslik": "Hangi bilgi, hangi biçim?", "icerik": [
            "Denklem yazmanın en önemli adımı doğru biçimi seçmektir. Verilen bilgiye uygun biçimle başlanırsa bilinmeyen sayısı azalır ve çoğu zaman tek bir bilinmeyen kalır.",
            tablo(["Verilen bilgi", "Kullanılacak biçim"], [
                ["Tepe noktası ve bir nokta", "$y=a(x-r)^2+k$"],
                ["İki kök ve bir nokta", "$y=a(x-x_1)(x-x_2)$"],
                ["Eksene teğet olduğu nokta ve bir nokta", "$y=a(x-r)^2$"],
                ["Üç nokta", "$y=ax^2+bx+c$"],
            ]),
            "Tepe noktası biçiminde tepe noktası doğrudan yerleşir ve geriye yalnızca $a$ kalır. Kök biçiminde de kökler yerleşir ve yine yalnızca $a$ bilinmez. Genel biçim ise üç bilinmeyen içerdiği için üç denklem gerektirir.",
        ]},
        {"baslik": "Tepe noktası ve bir nokta", "icerik": [
            "Tepe noktası $(r, k)$ biliniyorsa denklem $y=a(x-r)^2+k$ biçiminde yazılır. Parabol üzerindeki başka bir nokta yerine konunca $a$ bulunur.",
            ornek(
                "Tepe noktası $(1, -4)$ olan ve $(3, 0)$ noktasından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$y=a(x-1)^2-4$. $(3, 0)$ noktası için $0=4a-4$; $a=1$.",
                "$y=(x-1)^2-4=x^2-2x-3$."),
            koordinat_grafik("Tepe noktası (1, −4) olan ve (3, 0) noktasından geçen parabol", [("y = x² − 2x − 3", lambda x: x * x - 2 * x - 3)], (-3, 5), (-5, 5),
                             dikeyler=[1], noktalar=[(1, -4, "T(1, −4)", True), (3, 0, "(3, 0)", True), (-1, 0, "(−1, 0)", True)]),
            "Simetri sayesinde parabol $(-1, 0)$ noktasından da geçer: $(3, 0)$ noktasının $x=1$ eksenine göre simetriği budur. Bulunan denklem bu noktayla da kontrol edilebilir: $1+2-3=0$.",
        ]},
        {"baslik": "Tepe noktası ve y ekseni kesişimi", "icerik": [
            "$y$ ekseni kesişimi $(0, c)$ biçiminde bir nokta olduğu için tepe noktası biçimine aynı yolla yerleştirilir. Hesap özellikle kısadır, çünkü $x=0$ yazılır ve geriye tek bir çarpma kalır.",
            ornek(
                "Tepe noktası $(2, 1)$ olan ve $y$ eksenini $9$ da kesen parabol istensin.",
                "Denklemi yazalım.",
                "$y=a(x-2)^2+1$ ve $x=0$ için $9=4a+1$; $a=2$.",
                "$y=2(x-2)^2+1=2x^2-8x+9$."),
        ]},
        {"baslik": "İki kök ve bir nokta", "icerik": [
            "Kökler $x_1$ ve $x_2$ biliniyorsa denklem $y=a(x-x_1)(x-x_2)$ biçiminde yazılır. Köklerden farklı bir nokta yerine konunca $a$ bulunur.",
            ornek(
                "$x$ eksenini $-1$ ve $3$ te kesen ve $(0, -6)$ noktasından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$y=a(x+1)(x-3)$. $x=0$ için $-6=-3a$; $a=2$.",
                "$y=2(x+1)(x-3)=2x^2-4x-6$."),
            dikkat(
                "Kök biçiminde işaret hatası yapmak.",
                "Kökü $-1$ olan çarpan $(x-(-1))=(x+1)$ dir. Kökü doğrudan parantez içine yazmak, yani $(x-1)$ demek, kökü $1$ yapar ve bütün denklemi değiştirir."),
        ]},
        {"baslik": "Kökler ve en büyük değer", "icerik": [
            "Kökler ve tepe noktasının yüksekliği birlikte verildiğinde simetri ekseni köklerin ortalamasıdır. Böylece tepe noktası tamamen bilinir ve $a$ bu noktadan bulunur.",
            ornek(
                "Kökleri $0$ ve $4$ olan ve en büyük değeri $8$ olan parabol istensin.",
                "Denklemi yazalım.",
                "Simetri ekseni $x=2$; tepe noktası $(2, 8)$ dir. $y=ax(x-4)$ ve $x=2$ için $8=a \\cdot 2 \\cdot (-2)$; $a=-2$.",
                "$y=-2x(x-4)=-2x^2+8x$."),
            "Baş katsayının negatif çıkması, sorunun bir en büyük değer vermesiyle uyumludur: en büyük değeri olan parabolün kolları aşağı bakar. Bulunan işaret bu tutarlılıkla kontrol edilebilir.",
        ]},
        {"baslik": "Kökler ve en küçük değer", "icerik": [
            "En küçük değer verildiğinde de aynı yol izlenir: simetri ekseni köklerin ortalamasıdır ve tepe noktasının yüksekliği en küçük değerdir. Bu kez baş katsayının pozitif çıkması beklenir.",
            ornek(
                "Kökleri $1$ ve $5$ olan ve en küçük değeri $-8$ olan parabol istensin.",
                "Denklemi yazalım.",
                "Simetri ekseni $x=3$; tepe noktası $(3, -8)$. $y=a(x-1)(x-5)$ ve $x=3$ için $-8=a \\cdot 2 \\cdot (-2)$; $a=2$.",
                "$y=2(x-1)(x-5)=2x^2-12x+10$."),
        ]},
        {"baslik": "Tepe noktası ve bir kök", "icerik": [
            "Tepe noktası ve bir kök biliniyorsa diğer kök simetriden bulunur: iki kök simetri eksenine eşit uzaklıktadır. Sonra kök biçimi ya da tepe noktası biçimi kullanılabilir.",
            ornek(
                "Tepe noktası $(2, -9)$ olan ve bir kökü $-1$ olan parabol istensin.",
                "Denklemi yazalım.",
                "$-1$ simetri ekseninden $3$ birim soldadır; diğer kök $3$ birim sağda, yani $5$ tir.",
                "$y=a(x+1)(x-5)$ ve $x=2$ için $-9=a \\cdot 3 \\cdot (-3)$; $a=1$. Denklem $y=x^2-4x-5$ tir."),
        ]},
        {"baslik": "Üç nokta", "icerik": [
            "Yalnızca üç nokta verildiğinde genel biçim kullanılır ve her nokta bir denklem verir. Noktalardan biri $y$ ekseni üzerindeyse $c$ hemen bulunur ve denklem sayısı ikiye iner.",
            ornek(
                "$(0, 1)$, $(1, 0)$ ve $(2, 3)$ noktalarından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$(0, 1)$ den $c=1$. $(1, 0)$ dan $a+b+1=0$, $(2, 3)$ ten $4a+2b+1=3$.",
                "$a+b=-1$ ve $2a+b=1$; buradan $a=2$ ve $b=-3$.",
                "$y=2x^2-3x+1$. Kontrol: $x=2$ için $8-6+1=3$."),
        ]},
        {"baslik": "y eksenine göre simetrik parabol", "icerik": [
            "Simetri ekseni $y$ ekseniyse $b=0$ dır ve denklem $y=ax^2+c$ biçimine iner. Bilinmeyen sayısı ikiye düştüğü için iki nokta yeterlidir.",
            ornek(
                "$y$ eksenine göre simetrik olan ve $(1, 3)$ ile $(2, 9)$ noktalarından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$y=ax^2+c$. İki noktadan $a+c=3$ ve $4a+c=9$.",
                "Çıkarınca $3a=6$: $a=2$ ve $c=1$. Denklem $y=2x^2+1$ dir."),
        ]},
        {"baslik": "Başlangıç noktasından geçen parabol", "icerik": [
            "Parabol başlangıç noktasından geçiyorsa $c=0$ dır, çünkü $x=0$ için $y=0$ olmalıdır. Denklem $y=ax^2+bx$ biçimindedir ve iki nokta daha katsayıları belirler.",
            ornek(
                "Başlangıç noktasından, $(1, 1)$ ve $(2, 6)$ noktalarından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$c=0$. $(1, 1)$ den $a+b=1$, $(2, 6)$ dan $4a+2b=6$, yani $2a+b=3$.",
                "Çıkarınca $a=2$ ve $b=-1$. Denklem $y=2x^2-x$ tir."),
        ]},
        {"baslik": "Bir noktadan geçme koşulu", "icerik": [
            "Denklemde yalnızca bir parametre bilinmiyorsa parabolün geçtiği tek bir nokta bu parametreyi bulmaya yeter. Nokta denklemde yerine yazılır ve parametre için birinci dereceden bir denklem elde edilir.",
            ornek(
                "$y=x^2+mx+4$ parabolü $(1, 2)$ noktasından geçiyor.",
                "$m$ yi bulalım.",
                "$2=1+m+4$.",
                "$m=-3$; parabol $y=x^2-3x+4$ tür."),
        ]},
        {"baslik": "Eksene teğet olan parabol", "icerik": [
            "Parabol $x$ eksenine bir noktada teğetse o nokta çakışık köktür ve aynı zamanda tepe noktasıdır. Denklem $y=a(x-r)^2$ biçimindedir; tek bir nokta daha $a$ yı belirler.",
            ornek(
                "$x$ eksenine $x=2$ de teğet olan ve $(0, 8)$ noktasından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$y=a(x-2)^2$ ve $x=0$ için $8=4a$; $a=2$.",
                "$y=2(x-2)^2=2x^2-8x+8$."),
        ]},
        {"baslik": "Simetri ekseni ve iki nokta", "icerik": [
            "Simetri ekseni biliniyor ama tepe noktasının yüksekliği bilinmiyorsa tepe noktası biçimi iki bilinmeyenle yazılır: $a$ ve $k$. İki nokta iki denklem verir.",
            ornek(
                "Simetri ekseni $x=1$ olan ve $(0, 3)$ ile $(3, 0)$ noktalarından geçen parabol istensin.",
                "Denklemi yazalım.",
                "$y=a(x-1)^2+k$. $(0, 3)$ ten $a+k=3$; $(3, 0)$ dan $4a+k=0$.",
                "Çıkarınca $3a=-3$: $a=-1$ ve $k=4$.",
                "$y=-(x-1)^2+4=-x^2+2x+3$."),
            "Bu yol, simetri ekseni verildiğinde genel biçimle üç denklem kurmaktan çok daha kısadır. Simetri ekseni bir bilgi sayılır; iki nokta ile birlikte toplam üç bilgi parabolü belirler.",
        ]},
        {"baslik": "Grafikten tepe noktasıyla denklem", "icerik": [
            "Grafiği verilen bir parabolün denklemi yazılırken önce grafikte kesin okunabilen noktalar seçilir: tepe noktası, eksen kesişimleri ve ızgara çizgilerine denk gelen noktalar. Tepe noktası okunabiliyorsa tepe noktası biçimi en kısa yoldur.",
            koordinat_grafik("Tepe noktası (−1, −2) olan ve (1, 2) noktasından geçen parabol", [("y = x² + 2x − 1", lambda x: x * x + 2 * x - 1)], (-4, 3), (-3, 5),
                             noktalar=[(-1, -2, "T(−1, −2)", True), (1, 2, "(1, 2)", True), (-3, 2, "(−3, 2)", True)]),
            ornek(
                "Grafikteki parabolün tepe noktası $(-1, -2)$ ve üzerindeki bir nokta $(1, 2)$ dir.",
                "Denklemi yazalım.",
                "$y=a(x+1)^2-2$ ve $x=1$ için $2=4a-2$; $a=1$.",
                "$y=(x+1)^2-2=x^2+2x-1$. Simetrik nokta $(-3, 2)$ de denklemi sağlar: $9-6-1=2$."),
        ]},
        {"baslik": "Grafikten köklerle denklem", "icerik": [
            "Grafik $x$ eksenini ızgara noktalarında kesiyorsa kök biçimi en güvenilir yoldur. $y$ ekseni kesişimi de okunabiliyorsa $a$ tek adımda bulunur.",
            ornek(
                "Grafik $x$ eksenini $-2$ ve $1$ de, $y$ eksenini $-4$ te kesiyor.",
                "Denklemi yazalım.",
                "$y=a(x+2)(x-1)$ ve $x=0$ için $-4=-2a$; $a=2$.",
                "$y=2(x+2)(x-1)=2x^2+2x-4$."),
            dikkat(
                "Grafikten okunamayan bir değeri tahminle kullanmak.",
                "Izgara çizgisine denk gelmeyen bir nokta tahminle okunur ve yanlış bir $a$ verir. Denklem yazarken yalnızca grafikte açıkça belirtilen ya da ızgaraya tam oturan noktalar kullanılmalıdır."),
        ]},
        {"baslik": "Ötelemeyle denklem yazmak", "icerik": [
            "Bir parabol başka bir parabolün ötelenmesiyle elde edilmişse tepe noktası biçimi doğrudan yazılır: $y=ax^2$ parabolü $r$ birim yatay, $k$ birim dikey ötelenince $y=a(x-r)^2+k$ olur.",
            ornek(
                "$y=x^2$ parabolü $3$ birim sağa ve $2$ birim aşağı ötelensin.",
                "Yeni parabolün denklemini yazalım.",
                "Tepe noktası $(3, -2)$ olur: $y=(x-3)^2-2$.",
                "Genel biçim: $y=x^2-6x+7$."),
        ]},
        {"baslik": "Aynı biçimde başka yerde", "icerik": [
            "İki parabolün baş katsayıları eşitse biçimleri aynıdır; biri ötekinin ötelenmişidir. Bu yüzden bir parabolle aynı biçimde olup tepe noktası farklı olan parabol, baş katsayı korunarak yazılır.",
            ornek(
                "$y=3x^2$ ile aynı biçimde olan ve tepe noktası $(-1, 5)$ olan parabol istensin.",
                "Denklemi yazalım.",
                "Baş katsayı $3$ olarak kalır.",
                "$y=3(x+1)^2+5=3x^2+6x+8$."),
            "Baş katsayı korunduğu için iki parabol birbirinin aynısıdır; biri ötekinin $1$ birim sola ve $5$ birim yukarı taşınmış hâlidir.",
        ]},
        {"baslik": "Biçimler arasında geçiş", "icerik": [
            "Bir parabolün denklemini bir biçimden ötekine çevirmek, farklı soruları aynı denklemle cevaplamayı sağlar. Genel biçimden tepe noktası biçimine tam kareye tamamlamayla, kök biçimine çarpanlara ayırmayla geçilir.",
            ornek(
                "$y=2x^2-4x-6$ parabolü verilsin.",
                "Tepe noktası ve kök biçimlerini yazalım.",
                "Tepe noktası biçimi: $y=2(x^2-2x+1)-2-6=2(x-1)^2-8$.",
                "Kök biçimi: $y=2(x^2-2x-3)=2(x+1)(x-3)$."),
            "Her biçim farklı bir soruya hızlı cevap verir: tepe noktası biçimi en küçük değeri, kök biçimi $x$ ekseni kesişimlerini, genel biçim $y$ ekseni kesişimini doğrudan gösterir.",
        ]},
        {"baslik": "Denklemi kontrol etmek", "icerik": [
            "Yazılan denklemin doğruluğu, verilen her bilginin denklemde sağlanıp sağlanmadığına bakılarak denetlenir. Soruda verilen noktalar yerine yazılır, tepe noktası formülüyle yeniden hesaplanır ya da kökler bulunur.",
            ornek(
                "Tepe noktası $(1, -4)$ olan ve $(3, 0)$ dan geçen parabol için $y=x^2-2x-3$ bulundu.",
                "Denklemi kontrol edelim.",
                "$(3, 0)$ için $9-6-3=0$.",
                "Tepe noktası: $r=1$ ve $k=1-2-3=-4$. İki bilgi de sağlanıyor."),
        ]},
        {"baslik": "Kemer problemi", "icerik": [
            "Köprü ve kapı kemerleri çoğu zaman parabol biçimindedir. Böyle bir problemde koordinat sistemi akıllıca yerleştirilirse denklem kolaylaşır: simetri ekseni $y$ ekseni seçilince kökler simetrik olur ve $b=0$ çıkar.",
            ornek(
                "Parabol biçimindeki bir kemerin tabanı $20$ metre genişliğinde, ortadaki yüksekliği $5$ metredir.",
                "Kemerin denklemini ve ortadan $6$ metre uzaktaki yüksekliği bulalım.",
                "Kökler $-10$ ve $10$, tepe noktası $(0, 5)$: $y=a(x^2-100)$ ve $5=-100a$; $a=-\\dfrac{1}{20}$.",
                "$y=-\\dfrac{x^2}{20}+5$. $x=6$ için $y=-\\dfrac{36}{20}+5=3.2$ metre."),
            "Koordinat sisteminin yeri sonucu değiştirmez ama hesabı değiştirir. Kemerin sol ucu başlangıç noktası seçilseydi kökler $0$ ve $20$ olurdu; aynı yükseklik bulunur ama denklem daha karmaşık görünür.",
        ]},
        {"baslik": "Atış verisinden denklem", "icerik": [
            "Fırlatılan bir cismin yükseklik fonksiyonu da parabol olduğu için ölçülen birkaç değerden denklemi yazılabilir. En yüksek noktanın zamanı ve yüksekliği biliniyorsa tepe noktası biçimi kullanılır.",
            ornek(
                "Bir top $2$ metre yükseklikten atılıyor ve $1$ saniye sonra en yüksek noktası olan $7$ metreye ulaşıyor.",
                "Yükseklik fonksiyonunu yazalım.",
                "Tepe noktası $(1, 7)$: $h(t)=a(t-1)^2+7$. $t=0$ için $2=a+7$; $a=-5$.",
                "$h(t)=-5(t-1)^2+7=-5t^2+10t+2$."),
            "Bulunan fonksiyonla başka sorular da cevaplanır. Örneğin $2$. saniyede top yeniden $2$ metre yüksekliktedir, çünkü $h(2)=-20+20+2=2$ dir; bu, $t=0$ anının simetri eksenine göre simetriğidir.",
        ]},
        {"baslik": "Sınavda parabol denklemi", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) parabol denklemi; tepe noktası ve bir nokta, kökler ve bir nokta, üç nokta ya da grafikten okunan bilgilerle denklem kurma biçiminde karşına çıkabilir.",
                "Denklemi yazılan parabolden bir değer, bir kesişim ya da en büyük değer istemek de sık kullanılan bir soru biçimidir."),
            "Denklem sorusunda önce verilen bilgileri listele ve hangi biçimin bu bilgileri doğrudan içerdiğine bak. Tepe noktası varsa tepe biçimi, kökler varsa kök biçimi; ikisi de yoksa genel biçim. Doğru biçim seçildiğinde çoğu soruda yalnızca $a$ bilinmez kalır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Kökü $-1$ olan çarpanı $(x-1)$ yazmak", "$(x+1)$ yazılır"],
                ["Tepe noktası $(2, 1)$ için $(x+2)^2$ yazmak", "$(x-2)^2+1$"],
                ["Kök biçiminde $a$ yı unutmak", "$y=a(x-x_1)(x-x_2)$"],
                ["Grafikten tahminle nokta okumak", "Yalnız kesin noktalar kullanılır"],
                ["Bulunan denklemi kontrol etmemek", "Verilen noktalar yerine yazılır"],
                ["En büyük değer varken $a>0$ bulmak", "Kollar aşağı, $a<0$ olmalı"],
            ]),
            "Bu hataların çoğu, verilen bilgilerin biçime yanlış yerleştirilmesinden doğar. Denklemi bulduktan sonra soruda verilen her bilgiyi tek tek denetlemek, hatayı her zaman gösterir.",
        ]},
    ],
    "sss": [
        ("Parabol denklemi yazmak için kaç bilgi gerekir?",
         "Genellikle üç bilgi gerekir, çünkü denklemde üç katsayı vardır. Tepe noktası iki bilgi sayılır; bir nokta daha eklenince parabol belirlenir."),
        ("Tepe noktası verilen parabolün denklemi nasıl yazılır?",
         "y eşittir a çarpı x eksi r nin karesi artı k biçimi kullanılır. Parabol üzerindeki bir nokta yerine yazılarak a bulunur."),
        ("Kökleri verilen parabolün denklemi nasıl yazılır?",
         "y eşittir a çarpı x eksi birinci kök çarpı x eksi ikinci kök biçimi kullanılır. Köklerden farklı bir nokta a yı verir."),
        ("Üç noktadan parabol denklemi nasıl bulunur?",
         "Genel biçim kullanılır ve her nokta bir denklem verir. Noktalardan biri y ekseni üzerindeyse c hemen bulunur."),
        ("Grafikten denklem yazarken nelere dikkat edilir?",
         "Yalnızca kesin okunabilen noktalar kullanılır: tepe noktası, eksen kesişimleri ve ızgaraya tam oturan noktalar."),
        ("Parabolün denklemi farklı biçimlere nasıl çevrilir?",
         "Tam kareye tamamlanarak tepe noktası biçimine, çarpanlara ayrılarak kök biçimine geçilir."),
        ("İki noktadan kaç parabol geçer?",
         "Sonsuz sayıda parabol geçer. Parabolü tek olarak belirlemek için üçüncü bir bilgi gerekir."),
    ],
    "kontrol": [
        "Parabolü belirlemek için kaç bilgi gerektiğini açıklayabiliyorum.",
        "Verilen bilgiye uygun denklem biçimini seçebiliyorum.",
        "Tepe noktası ve bir noktadan denklem yazabiliyorum.",
        "Kökler ve bir noktadan denklem yazabiliyorum.",
        "Üç noktadan denklem kurabiliyorum.",
        "Eksene teğet olan parabolün denklemini yazabiliyorum.",
        "Grafikten denklem okuyabiliyorum.",
        "Ötelemeyle parabol denklemi yazabiliyorum.",
        "Denklemi biçimler arasında çevirebiliyorum.",
        "Kemer ve atış problemlerinde parabol denklemi kurabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["parabol-tepe-noktasi", "parabol-grafigi", "parabol-konu-anlatimi"],
}
