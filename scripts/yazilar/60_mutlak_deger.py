# scripts/yazilar/60_mutlak_deger.py — Mutlak Deger (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "mutlak-deger-konu-anlatimi-pdf",
    "baslik": "Mutlak Değer Konu Anlatımı PDF",
    "aciklama": "Mutlak değer nedir? Tanım, özellikler, mutlak değer açma, mutlak değerli denklemler ve eşitsizlikler, en küçük değer soruları; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "mutlak-deger-konu-anlatimi-pdf",
    "kapak_alt": "Mutlak değer: ahşap ray ortasındaki başlangıç noktasından iki yana eşit uzunlukta mavi ve kırmızı şeritler geren öğrenci",
    "ozet": "Mutlak değer, bir sayının sıfıra olan uzaklığıdır ve uzaklık hiçbir zaman negatif olmaz. Bu basit fikir, denklemlerden eşitsizliklere, en küçük değer sorularından sayı doğrusu problemlerine kadar birçok konunun anahtarıdır. Bu yazıda mutlak değeri tanımlıyor, özelliklerini gerekçeleriyle veriyor, işareti bilinen ifadelerde mutlak değeri açmayı, mutlak değerli denklem ve eşitsizlikleri çözmeyi ve en küçük değer sorularını sayı doğrusu yardımıyla çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Mutlak değer nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için sayı doğrusunu, pozitif-negatif sayıları ve basit eşitsizlikleri biliyor olman yeterli.",
                "Sayı doğrusunda uzaklık için <a href=\"/blog/sayi-dogrusu-ve-sayilari-siralama/\">Sayı Doğrusu ve Sayıları Sıralama</a> yazısına göz at."),
            "Bir sayının sayı doğrusunda sıfıra olan uzaklığına o sayının <strong>mutlak değeri</strong> denir ve $|x|$ biçiminde gösterilir. $5$ ile $-5$ sıfıra aynı uzaklıktadır; bu yüzden $|5|=5$ ve $|-5|=5$ tir. Sıfırın sıfıra uzaklığı sıfırdır: $|0|=0$.",
            "Uzaklık negatif olamayacağı için mutlak değer hiçbir zaman negatif değildir: her $x$ için $|x| \\geq 0$ dır. Mutlak değer bir sayının işaretini atar, büyüklüğünü korur.",
            hap("Mutlak değer, sıfıra olan uzaklıktır ve hiçbir zaman negatif değildir.",
                "$|x|=0$ yalnızca $x=0$ iken sağlanır."),
        ]},
        {"baslik": "Mutlak değerin tanımı", "icerik": [
            "Mutlak değerin cebirsel tanımı iki durumdan oluşur:",
            "<ul><li>$x \\geq 0$ ise $|x|=x$</li><li>$x<0$ ise $|x|=-x$</li></ul>",
            "İkinci satır ilk bakışta şaşırtıcı görünebilir: mutlak değer negatif olamıyorsa neden $-x$ yazıyoruz? Çünkü $x$ negatifken $-x$ pozitiftir. Örneğin $x=-7$ ise $-x=-(-7)=7$ olur. Buradaki eksi, sayıyı negatif yapmak için değil, negatif sayının işaretini çevirmek için oradadır.",
            "Tanımın hızlı bir sonucu, bir sayının kendi mutlak değerine bölümüdür. $x>0$ ise $\\dfrac{|x|}{x}=\\dfrac{x}{x}=1$, $x<0$ ise $\\dfrac{|x|}{x}=\\dfrac{-x}{x}=-1$ dir. Bu ifade, sayının işaretini $1$ ya da $-1$ olarak verir.",
            ornek(
                "$a<0<b$ olsun.",
                "$\\dfrac{|a|}{a}+\\dfrac{b}{|b|}$ ifadesinin değerini bulalım.",
                "$a<0$ olduğu için $\\dfrac{|a|}{a}=-1$.",
                "$b>0$ olduğu için $\\dfrac{b}{|b|}=1$.",
                "Toplam: $-1+1=0$."),
            dikkat(
                "$|-x|$ her zaman $x$ e eşit değildir.",
                "$x=-3$ için $|-x|=|3|=3$ ama $x=-3$ tür. Doğru olan $|-x|=|x|$ eşitliğidir."),
        ]},
        {"baslik": "İçi işaretli ifadelerde mutlak değeri açmak", "icerik": [
            "Mutlak değerin içinde bir ifade varsa önce bu ifadenin işaretine bakılır. İçerisi pozitif ya da sıfırsa ifade olduğu gibi dışarı çıkar; negatifse başına eksi konarak, yani işaretleri değiştirilerek çıkar.",
            ornek(
                "$|3-\\pi|$ ve $|\\sqrt{2}-2|$ ifadeleri verilsin.",
                "Mutlak değerleri açalım.",
                "$\\pi$ yaklaşık $3.14$ olduğu için $3-\\pi<0$; bu yüzden $|3-\\pi|=\\pi-3$.",
                "$\\sqrt{2}$ yaklaşık $1.41$ olduğu için $\\sqrt{2}-2<0$; bu yüzden $|\\sqrt{2}-2|=2-\\sqrt{2}$.",
                "İki sonuç da pozitiftir, yani doğru açılmıştır."),
            ornek(
                "$x<0<y$ olsun.",
                "$|x|+|y-x|-|-y|$ ifadesini sadeleştirelim.",
                "$x<0$ olduğu için $|x|=-x$.",
                "$y>x$ olduğu için $y-x>0$ ve $|y-x|=y-x$.",
                "$-y<0$ olduğu için $|-y|=y$.",
                "Toplayalım: $-x+(y-x)-y=-2x$. Kontrol: $x=-1$, $y=2$ için $1+3-2=2$ ve $-2 \\cdot (-1)=2$."),
            ornek(
                "$2<x<5$ olsun.",
                "$|x-2|+|x-5|$ ifadesini sadeleştirelim.",
                "$x>2$ olduğu için $x-2>0$ ve $|x-2|=x-2$.",
                "$x<5$ olduğu için $x-5<0$ ve $|x-5|=5-x$.",
                "Toplam: $(x-2)+(5-x)=3$. Sonuç $x$ ten bağımsızdır."),
            hap("Mutlak değeri açmadan önce içerideki ifadenin işaretini belirle.",
                "İçerisi negatifse ifadenin işaretlerini değiştirerek dışarı çıkar."),
        ]},
        {"baslik": "Mutlak değerin özellikleri", "icerik": [
            "Aşağıdaki özellikler her gerçek sayı için geçerlidir ve soruları kısaltmak için kullanılır:",
            tablo(["Özellik", "Örnek"], [
                ["$|x| \\geq 0$", "$|-4|=4 \\geq 0$"],
                ["$|-x|=|x|$", "$|-6|=|6|=6$"],
                ["$|x-y|=|y-x|$", "$|2-9|=|9-2|=7$"],
                ["$|x \\cdot y|=|x| \\cdot |y|$", "$|(-3) \\cdot 4|=3 \\cdot 4=12$"],
                ["$\\left|\\dfrac{x}{y}\\right|=\\dfrac{|x|}{|y|}$, $y \\neq 0$", "$\\left|\\dfrac{-8}{2}\\right|=\\dfrac{8}{2}=4$"],
                ["$|x|^2=x^2$", "$|-5|^2=25=(-5)^2$"],
                ["$\\sqrt{x^2}=|x|$", "$\\sqrt{(-3)^2}=\\sqrt{9}=3$"],
            ]),
            "Toplama ve çıkarma için böyle bir eşitlik yoktur. Bunun yerine <strong>üçgen eşitsizliği</strong> geçerlidir: $|x+y| \\leq |x|+|y|$. Eşitlik yalnızca $x$ ve $y$ aynı işaretliyse ya da biri sıfırsa sağlanır.",
            ornek(
                "$x=3$ ve $y=-5$ olsun.",
                "Üçgen eşitsizliğini kontrol edelim.",
                "$|x+y|=|3+(-5)|=|-2|=2$.",
                "$|x|+|y|=3+5=8$.",
                "$2 \\leq 8$ sağlanır. Farklı işaretli sayılarda toplamın mutlak değeri küçülür."),
            "Üçgen eşitsizliğinin adı geometriden gelir: bir üçgende bir kenarın uzunluğu, diğer iki kenarın uzunlukları toplamından büyük olamaz. Sayı doğrusunda da durum aynıdır. $0$ dan $x+y$ ye doğrudan gitmek $|x+y|$ birim tutar; önce $x$ e gidip oradan $y$ kadar ilerlemek ise $|x|+|y|$ birim tutar. Dolambaçlı yol, doğrudan yoldan hiçbir zaman kısa olamaz.",
            dikkat(
                "$\\sqrt{x^2}=x$ yazmak yanlıştır.",
                "$x=-3$ için $\\sqrt{(-3)^2}=3$ olur, $-3$ olmaz. Doğrusu $\\sqrt{x^2}=|x|$ tir."),
        ]},
        {"baslik": "Mutlak değer ve uzaklık", "icerik": [
            "Mutlak değerin en kullanışlı yorumu uzaklıktır. $|x|$, $x$ in $0$ a uzaklığıdır; aynı şekilde $|x-a|$, $x$ in $a$ ya uzaklığıdır. İçerideki ifade $x+a$ biçimindeyse onu $x-(-a)$ olarak okumak gerekir: $|x+1|$, $x$ in $-1$ e uzaklığıdır.",
            "Bu yorum sayesinde bir mutlak değer ifadesini okumak, sayı doğrusunda bir resim çizmek gibidir. $|x-4|=2$ denklemi \"$4$ e uzaklığı $2$ olan sayılar\" demektir ve cevap hemen görünür: $2$ ve $6$. $|x-4|<2$ ise \"$4$ e uzaklığı $2$ den az olan sayılar\" demektir: $2<x<6$.",
            ornek(
                "Sayı doğrusunda $2$ ve $10$ noktalarına eşit uzaklıkta olan nokta sorulsun.",
                "Bu noktayı mutlak değerle bulalım.",
                "Aranan $x$ için $|x-2|=|x-10|$ olmalıdır.",
                "İçler eşit olamaz çünkü $x-2=x-10$ çelişkidir. Öyleyse içler zıttır: $x-2=-(x-10)$, yani $2x=12$.",
                "$x=6$. Bu nokta, $2$ ile $10$ un orta noktasıdır: $\\dfrac{2+10}{2}=6$."),
        ]},
        {"baslik": "Mutlak değerli denklemler", "icerik": [
            "$|A|=k$ biçimindeki bir denklemde üç durum vardır:",
            "<ul><li>$k>0$ ise $A=k$ ya da $A=-k$ dır; iki durum ayrı ayrı çözülür.</li>"
            "<li>$k=0$ ise yalnızca $A=0$ dır.</li>"
            "<li>$k<0$ ise çözüm yoktur; çünkü mutlak değer negatif olamaz.</li></ul>",
            ornek(
                "$|x-3|=5$ denklemi verilsin.",
                "Çözüm kümesini bulalım.",
                "$x-3=5$ ise $x=8$.",
                "$x-3=-5$ ise $x=-2$.",
                "Çözüm kümesi $\\{-2, 8\\}$. Sayı doğrusunda bu, $3$ e uzaklığı $5$ olan iki noktadır."),
            ornek(
                "$|2x+1|=7$ denklemi verilsin.",
                "Köklerin toplamını bulalım.",
                "$2x+1=7$ ise $x=3$.",
                "$2x+1=-7$ ise $x=-4$.",
                "Köklerin toplamı $3+(-4)=-1$."),
            ornek(
                "$|x-1|=|2x+3|$ denklemi verilsin.",
                "Çözüm kümesini bulalım.",
                "İki mutlak değer eşitse içleri ya eşit ya da zıttır.",
                "$x-1=2x+3$ ise $x=-4$.",
                "$x-1=-(2x+3)$ ise $3x=-2$ ve $x=-\\dfrac{2}{3}$.",
                "Kontrol: $x=-4$ için iki taraf da $5$; $x=-\\dfrac{2}{3}$ için iki taraf da $\\dfrac{5}{3}$."),
            dikkat(
                "$|x+4|=-2$ gibi bir denklemde çözüm aramaya başlama.",
                "Mutlak değer negatif bir sayıya eşit olamaz. Çözüm kümesi boş kümedir."),
            "<h3>Sağ tarafta değişken olduğunda</h3>",
            "$|A|=B$ denkleminde $B$ bir sayı değil de $x$ e bağlı bir ifadeyse ek bir koşul gelir: mutlak değer negatif olamayacağı için $B \\geq 0$ olmalıdır. Bulunan kökler bu koşulla mutlaka kontrol edilir.",
            ornek(
                "$|x-2|=2x-7$ denklemi verilsin.",
                "Çözüm kümesini bulalım.",
                "Koşul: $2x-7 \\geq 0$, yani $x \\geq 3.5$.",
                "$x-2=2x-7$ ise $x=5$. Koşulu sağlar.",
                "$x-2=-(2x-7)$ ise $3x=9$ ve $x=3$. Koşulu sağlamaz; gerçekten $x=3$ için sol taraf $1$, sağ taraf $-1$ olur.",
                "Çözüm kümesi $\\{5\\}$."),
            "<h3>İç içe mutlak değer</h3>",
            "Mutlak değer içinde mutlak değer varsa en dıştakinden başlanır ve her adımda aynı kural uygulanır.",
            ornek(
                "$||x-2|-3|=1$ denklemi verilsin.",
                "Köklerin sayısını ve toplamını bulalım.",
                "Dış mutlak değer: $|x-2|-3=1$ ya da $|x-2|-3=-1$; yani $|x-2|=4$ ya da $|x-2|=2$.",
                "$|x-2|=4$ ise $x=6$ ya da $x=-2$.",
                "$|x-2|=2$ ise $x=4$ ya da $x=0$.",
                "Dört kök vardır: $-2, 0, 4, 6$. Toplamları $8$ dir."),
        ]},
        {"baslik": "Mutlak değerli eşitsizlikler", "icerik": [
            "Mutlak değerli eşitsizlikleri sayı doğrusundaki uzaklık fikriyle düşünmek en kolay yoldur. $a>0$ olmak üzere:",
            tablo(["Eşitsizlik", "Anlamı", "Çözüm"], [
                ["$|x|<a$", "Sıfıra uzaklığı $a$ dan az", "$-a<x<a$"],
                ["$|x|>a$", "Sıfıra uzaklığı $a$ dan fazla", "$x<-a$ ya da $x>a$"],
            ]),
            "Aynı kural içeride bir ifade olduğunda da geçerlidir: $|x-c|<a$, $x$ in $c$ ye uzaklığının $a$ dan az olduğunu söyler.",
            ornek(
                "$|x-2|<3$ eşitsizliği verilsin.",
                "Eşitsizliği sağlayan tam sayıları bulalım.",
                "Kural: $-3<x-2<3$.",
                "Her tarafa $2$ ekleyelim: $-1<x<5$.",
                "Tam sayılar $0, 1, 2, 3, 4$: toplam $5$ tane."),
            ornek(
                "$|2x-1| \\geq 5$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "$2x-1 \\geq 5$ ise $x \\geq 3$.",
                "$2x-1 \\leq -5$ ise $x \\leq -2$.",
                "Çözüm: $x \\leq -2$ ya da $x \\geq 3$."),
            ornek(
                "$1 \\leq |x-3|<4$ eşitsizliği verilsin.",
                "Kaç tam sayı bu eşitsizliği sağlar?",
                "$x$ tam sayı olduğu için $|x-3|$ yalnızca $1$, $2$ ya da $3$ olabilir.",
                "$x-3$ değerleri: $\\pm 1$, $\\pm 2$, $\\pm 3$.",
                "$x$ değerleri: $0, 1, 2, 4, 5, 6$. Toplam $6$ tam sayı; $x=3$ dışarıda kalır."),
            "Eşitsizliğin sağ tarafı sıfır ya da negatifse kuralı kör uygulamak yerine mutlak değerin negatif olamayacağını hatırlamak gerekir. $|x-3| \\leq 0$ yalnızca $x=3$ için sağlanır; $|x-3|<0$ ise hiçbir $x$ için sağlanmaz. Öte yandan $|x-3| \\geq 0$ her $x$ için doğrudur.",
            ornek(
                "Bir makine parçasının uzunluğu $50$ milimetre olmalı ve en fazla $0.2$ milimetre sapmaya izin veriliyor.",
                "Kabul edilebilir uzunlukları mutlak değerle ifade edelim.",
                "Uzunluk $x$ olsun. $50$ ye uzaklığı $0.2$ yi aşmamalı: $|x-50| \\leq 0.2$.",
                "Kural: $-0.2 \\leq x-50 \\leq 0.2$.",
                "Her tarafa $50$ ekleyelim: $49.8 \\leq x \\leq 50.2$."),
            dikkat(
                "$|x|>a$ eşitsizliğini $-a>x>a$ diye yazma.",
                "Hiçbir sayı aynı anda hem $-a$ dan küçük hem $a$ dan büyük olamaz. Doğrusu iki ayrı parçadır: $x<-a$ ya da $x>a$."),
        ]},
        {"baslik": "Kritik noktalarla mutlak değer açma", "icerik": [
            "$x$ in aralığı verilmemişse mutlak değer tek bir biçimde açılamaz. Bu durumda her mutlak değerin içini sıfır yapan noktalar bulunur; bu noktalara <strong>kritik noktalar</strong> denir. Kritik noktalar sayı doğrusunu aralıklara böler ve her aralıkta ifade ayrı ayrı açılır.",
            ornek(
                "$|x-1|+|x+3|$ ifadesi verilsin.",
                "İfadeyi her aralıkta mutlak değersiz yazalım.",
                "Kritik noktalar: $x-1=0$ için $x=1$, $x+3=0$ için $x=-3$.",
                "$x<-3$ iken iki iç de negatif: $-(x-1)-(x+3)=-2x-2$.",
                "$-3 \\leq x \\leq 1$ iken $x+3 \\geq 0$ ve $x-1 \\leq 0$: $-(x-1)+(x+3)=4$.",
                "$x>1$ iken iki iç de pozitif: $(x-1)+(x+3)=2x+2$.",
                "Kontrol: $x=-5$ için $6+2=8$ ve $-2 \\cdot (-5)-2=8$."),
            "Bu örnekte ortadaki aralıkta ifadenin sabit $4$ olduğuna dikkat et. $4$, iki kritik nokta arasındaki uzaklıktır; aşağıdaki en küçük değer yönteminin gerekçesi de budur.",
        ]},
        {"baslik": "En küçük değer soruları", "icerik": [
            "$|x-a|$ ifadesi, $x$ in $a$ ya uzaklığıdır. Bu yorum, iki ya da daha fazla mutlak değerin toplamının en küçük değerini hesapsız bulmayı sağlar.",
            "$|x-a|+|x-b|$ toplamı, $x$ in $a$ ve $b$ noktalarına olan uzaklıklarının toplamıdır. $x$, $a$ ile $b$ arasındaysa bu toplam tam olarak $|a-b|$ dir; dışarıdaysa daha büyüktür. Bu yüzden en küçük değer $|a-b|$ dir.",
            ornek(
                "$|x+2|+|x-3|$ ifadesi verilsin.",
                "En küçük değerini bulalım.",
                "$|x+2|=|x-(-2)|$, $x$ in $-2$ ye uzaklığıdır; $|x-3|$ ise $3$ e uzaklığıdır.",
                "$x$, $-2$ ile $3$ arasındayken uzaklıklar toplamı iki nokta arasındaki uzaklığa eşittir: $3-(-2)=5$.",
                "En küçük değer $5$ tir ve $-2 \\leq x \\leq 3$ olan her $x$ için elde edilir."),
            ornek(
                "$|x-1|+|x-2|+|x-6|$ ifadesi verilsin.",
                "En küçük değerini bulalım.",
                "Üç nokta var: $1$, $2$, $6$. Terim sayısı tek olduğunda en küçük değer ortadaki noktada, yani $x=2$ de elde edilir.",
                "$x=2$ için: $1+0+4=5$.",
                "En küçük değer $5$ tir. Kontrol: $x=1$ için $0+1+5=6$, $x=3$ için $2+1+3=6$."),
            "<h3>Farkın en büyük ve en küçük değeri</h3>",
            "Toplam yerine fark olduğunda durum değişir. $|x-a|-|x-b|$ ifadesi iki uzaklığın farkıdır ve iki uzaklığın farkı, noktalar arasındaki uzaklığı aşamaz. Bu yüzden ifadenin değerleri $-|a-b|$ ile $|a-b|$ arasındadır.",
            ornek(
                "$|x-2|-|x-7|$ ifadesi verilsin.",
                "En büyük ve en küçük değerini bulalım.",
                "Noktalar arası uzaklık $7-2=5$; değerler $-5$ ile $5$ arasındadır.",
                "$x \\geq 7$ için $(x-2)-(x-7)=5$: en büyük değer $5$.",
                "$x \\leq 2$ için $(2-x)-(7-x)=-5$: en küçük değer $-5$."),
            hap("$|x-a|+|x-b|$ nin en küçük değeri $|a-b|$ dir.",
                "Tek sayıda mutlak değer toplandığında en küçük değer ortadaki noktada elde edilir."),
        ]},
        {"baslik": "Sınavda mutlak değer", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu işareti bilinen ifadelerde mutlak değer açma, mutlak değerli denklem ve eşitsizlikler ve en küçük değer soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde mutlak değer bir uzaklık ya da fark problemi içinde de karşına çıkabilir: iki değer arasındaki farkın belirli bir sınırı aşmaması gibi."),
            "Mutlak değer sorularında en güçlü araç sayı doğrusudur. $|x-a|$ yı gördüğün yerde \"$x$ in $a$ ya uzaklığı\" diye okursan, denklem ve eşitsizliklerin çoğu çizim yapmadan çözülür. Bulduğun kökleri her zaman denkleme geri koyarak kontrol et; özellikle sağ tarafta değişken olan denklemlerde yabancı kök kolayca araya karışır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$|-x|=x$ yazmak", "$|-x|=|x|$"],
                ["$\\sqrt{x^2}=x$ yazmak", "$\\sqrt{x^2}=|x|$"],
                ["$|x+y|=|x|+|y|$ sanmak", "$|x+y| \\leq |x|+|y|$"],
                ["$|A|=k<0$ için kök aramak", "Çözüm yoktur"],
                ["$|x|>a$ yı $-a>x>a$ yazmak", "$x<-a$ ya da $x>a$"],
                ["İçerinin işaretine bakmadan açmak", "Önce işareti belirle"],
            ]),
            "Bu hataların çoğu, mutlak değeri \"eksiyi silen bir işlem\" olarak ezberlemekten doğar. Mutlak değer eksiyi silmez, uzaklığı ölçer. İçerideki ifade negatifse onu pozitif yapmak için başına eksi koymak gerekir.",
        ]},
    ],
    "sss": [
        ("Mutlak değer nedir?",
         "Bir sayının sayı doğrusunda sıfıra olan uzaklığıdır. Uzaklık negatif olamayacağı için mutlak değer de hiçbir zaman negatif değildir."),
        ("Mutlak değer negatif olabilir mi?",
         "Hayır. Her sayının mutlak değeri sıfır ya da pozitiftir. Bu yüzden mutlak değeri negatif bir sayıya eşit olan denklemlerin çözümü yoktur."),
        ("Mutlak değer nasıl açılır?",
         "İçerideki ifadenin işaretine bakılır. İçerisi pozitif ya da sıfırsa ifade olduğu gibi, negatifse işaretleri değiştirilerek dışarı çıkar."),
        ("Karekök x kare neden mutlak x e eşittir?",
         "Karekök her zaman negatif olmayan sonucu verir. x negatifken x in kendisi negatif olduğu için sonuç x değil, x in mutlak değeridir."),
        ("Mutlak değerli denklem nasıl çözülür?",
         "Mutlak değer pozitif bir sayıya eşitse içerisi o sayıya ya da zıttına eşitlenir ve iki durum ayrı ayrı çözülür."),
        ("İki mutlak değerin toplamının en küçük değeri nasıl bulunur?",
         "Toplam iki noktaya olan uzaklıkların toplamıdır. En küçük değeri, iki nokta arasındaki uzaklıktır."),
    ],
    "kontrol": [
        "Mutlak değeri sıfıra olan uzaklık olarak açıklayabiliyorum.",
        "Mutlak değerin iki durumlu tanımında $-x$ in neden pozitif olduğunu açıklayabiliyorum.",
        "İçi işaretli bir ifadenin mutlak değerini doğru açabiliyorum.",
        "Aralığı verilen harfli ifadelerde mutlak değerleri açıp sadeleştirebiliyorum.",
        "Çarpım, bölüm ve kare özelliklerini kullanabiliyorum.",
        "$\\sqrt{x^2}=|x|$ eşitliğinin nedenini açıklayabiliyorum.",
        "Mutlak değerli bir denklemin iki durumunu ayrı ayrı çözebiliyorum.",
        "Mutlak değeri negatif sayıya eşit olan denklemin çözümsüz olduğunu görebiliyorum.",
        "Mutlak değerli eşitsizlikleri sayı doğrusu yardımıyla çözebiliyorum.",
        "Mutlak değer toplamlarının en küçük değerini uzaklık fikriyle bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["sayi-dogrusu-ve-sayilari-siralama", "pozitif-ve-negatif-sayilar", "irrasyonel-sayilar-ve-gercek-sayilar"],
}
