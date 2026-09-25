# scripts/yazilar/07_polinomlar.py — Polinomlar (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "polinomlar-konu-anlatimi",
    "baslik": "Polinomlar Konu Anlatımı",
    "aciklama": "Polinom nedir? Terim, katsayı, derece, sabit terim, katsayılar toplamı, polinom eşitliği, dört işlem, derece kuralları, değer hesaplama ve grafikler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "polinomlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "polinomlar-konu-anlatimi",
    "kapak_alt": "Polinomlar: derecelerine göre sütunlara ayrılmış renkli bloklar ve bir polinom grafiği üzerinde çalışan iki öğrenci",
    "ozet": "Polinomlar, cebirin en çok kullanılan ifadeleridir: toplanır, çarpılır, bölünür, çarpanlarına ayrılır ve grafikleri çizilir. Denklemlerin, parabolün ve ileride türev ile integralin temeli polinomlardır. Bu yazıda polinomun tanımını, polinom olan ve olmayan ifadeleri, terim, katsayı ve dereceyi, sabit terim ile katsayılar toplamını, polinomların eşitliğini, toplama, çıkarma ve çarpmayı, derece kurallarını, değer hesaplamayı ve polinom grafiklerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Polinom nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için cebirsel ifadeleri ve üslü sayıları biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/cebirsel-ifadeler-konu-anlatimi-pdf/\">Cebirsel İfadeler Konu Anlatımı PDF</a> ve <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazılarına göz at."),
            "$n$ bir doğal sayı ve $a_0$, $a_1$, ..., $a_n$ gerçek sayılar olmak üzere aşağıdaki biçimde yazılabilen ifadelere $x$ değişkenine bağlı <strong>polinom</strong> denir:",
            "$$P(x)=a_n x^n+a_{n-1} x^{n-1}+\\cdots+a_1 x+a_0$$",
            "Polinomun belirleyici özelliği, değişkenin kuvvetlerinin <strong>doğal sayı</strong> olmasıdır. Negatif, kesirli ya da köklü kuvvet içeren ifadeler polinom değildir. Kapaktaki sütunlar da bu yapıyı gösterir: her sütun bir kuvveti, sütundaki bloklar o kuvvetin katsayısını temsil eder.",
            hap("Polinomda değişkenin bütün kuvvetleri doğal sayıdır.",
                "Katsayılar herhangi bir gerçek sayı olabilir."),
        ]},
        {"baslik": "Polinom olan ve olmayan ifadeler", "icerik": [
            "Bir ifadenin polinom olup olmadığına karar vermek için her terimdeki değişkenin kuvvetine bakılır. Katsayıların kesirli ya da köklü olması sorun değildir; önemli olan yalnızca değişkenin kuvvetidir.",
            tablo(["İfade", "Polinom mu?", "Neden"], [
                ["$3x^2-5x+1$", "Evet", "Kuvvetler $2$, $1$, $0$"],
                ["$\\sqrt{2}x^3+\\dfrac{1}{2}$", "Evet", "Köklü olan katsayıdır"],
                ["$x^{-1}+2$", "Hayır", "Kuvvet negatif"],
                ["$\\sqrt{x}+1$", "Hayır", "Kuvvet kesirli"],
                ["$\\dfrac{3}{x}-x$", "Hayır", "Değişken paydada"],
                ["$7$", "Evet", "Sabit polinom"],
            ]),
            ornek(
                "$P(x)=2x^{\\frac{6}{n}}+3x^{n-1}$ ifadesinin bir polinom olduğu biliniyor.",
                "$n$ nin alabileceği pozitif tam sayı değerlerinin sayısını bulalım.",
                "Kuvvetler doğal sayı olmalıdır: $\\dfrac{6}{n}$ doğal sayı ise $n$, $6$ nın pozitif bir bölenidir: $1$, $2$, $3$ ya da $6$.",
                "Bu değerlerin hepsinde $n-1$ de bir doğal sayıdır. $n$ nin alabileceği $4$ değer vardır."),
        ]},
        {"baslik": "Terim, katsayı ve derece", "icerik": [
            "Polinomu oluşturan $a_k x^k$ ifadelerinin her birine <strong>terim</strong>, $a_k$ sayılarına <strong>katsayı</strong> denir. Katsayısı sıfırdan farklı olan en büyük kuvvete polinomun <strong>derecesi</strong> denir ve $\\text{der}[P(x)]$ ile gösterilir. En büyük kuvvetli terimin katsayısına <strong>baş katsayı</strong>, $x$ içermeyen terime de <strong>sabit terim</strong> denir.",
            ornek(
                "$P(x)=4x^3-2x^2+7x-5$ polinomu verilsin.",
                "Derecesini, baş katsayısını ve sabit terimini bulalım.",
                "En büyük kuvvet $3$ tür: $\\text{der}[P(x)]=3$.",
                "Baş katsayı $4$, sabit terim $-5$ tir."),
            dikkat(
                "Polinomu sıralamadan baş katsayıyı ilk terimden okumak.",
                "$P(x)=5-2x+3x^4$ polinomunda baş katsayı $5$ değil $3$ tür. Baş katsayı her zaman en büyük kuvvetli terimin katsayısıdır; terimlerin yazılış sırası önemli değildir."),
        ]},
        {"baslik": "Sabit ve sıfır polinomu", "icerik": [
            "$P(x)=5$ gibi yalnızca sabit terimden oluşan polinomlara <strong>sabit polinom</strong> denir; derecesi $0$ dır, çünkü $5=5x^0$ olarak yazılabilir. Bütün katsayıları sıfır olan $P(x)=0$ polinomuna ise <strong>sıfır polinomu</strong> denir. Sıfır polinomunun hiçbir terimi sıfırdan farklı olmadığı için derecesi tanımsızdır.",
            ornek(
                "$P(x)=(a-3)x^2+(b+2)x+c-1$ polinomunun sıfır polinomu olduğu biliniyor.",
                "$a$, $b$ ve $c$ yi bulalım.",
                "Bütün katsayılar sıfır olmalıdır: $a-3=0$, $b+2=0$, $c-1=0$.",
                "$a=3$, $b=-2$ ve $c=1$."),
        ]},
        {"baslik": "Sabit terim ve katsayılar toplamı", "icerik": [
            "Bir polinomda $x$ yerine $0$ yazılınca $x$ içeren bütün terimler kaybolur ve geriye sabit terim kalır. $x$ yerine $1$ yazılınca ise her terim kendi katsayısına eşit olur ve katsayıların toplamı bulunur:",
            tablo(["İstenen", "Hesap"], [
                ["Sabit terim", "$P(0)$"],
                ["Katsayılar toplamı", "$P(1)$"],
            ]),
            ornek(
                "$P(x)=(2x-1)^3+x^2+4$ polinomu verilsin.",
                "Sabit terimi ve katsayılar toplamını bulalım.",
                "Sabit terim: $P(0)=(-1)^3+0+4=3$.",
                "Katsayılar toplamı: $P(1)=1^3+1+4=6$."),
            "Bu yöntem, polinomu açmadan sonuç verir. $(2x-1)^3$ ifadesini açmak birkaç satır sürer; $P(0)$ ve $P(1)$ ise birkaç saniyede hesaplanır.",
        ]},
        {"baslik": "Çift ve tek dereceli terimler", "icerik": [
            "$x$ yerine $-1$ yazılınca çift dereceli terimler aynı kalır, tek dereceli terimler işaret değiştirir. Bu yüzden $P(1)$ ile $P(-1)$ toplanınca tek dereceli terimler birbirini götürür, çıkarılınca çift dereceli terimler birbirini götürür:",
            tablo(["İstenen", "Hesap"], [
                ["Çift dereceli terimlerin katsayıları toplamı", "$\\dfrac{P(1)+P(-1)}{2}$"],
                ["Tek dereceli terimlerin katsayıları toplamı", "$\\dfrac{P(1)-P(-1)}{2}$"],
            ]),
            ornek(
                "$P(x)=(x+2)^3$ polinomu verilsin.",
                "Çift ve tek dereceli terimlerin katsayıları toplamlarını bulalım.",
                "$P(1)=27$ ve $P(-1)=1$.",
                "Çift dereceli: $\\dfrac{27+1}{2}=14$. Tek dereceli: $\\dfrac{27-1}{2}=13$.",
                "Kontrol: $(x+2)^3=x^3+6x^2+12x+8$; çift dereceli katsayılar $6+8=14$, tek dereceli katsayılar $1+12=13$."),
            "Sabit terimin derecesi $0$ olduğu için çift dereceli terimlerin arasında sayılır. Örnekteki $8$ bu yüzden çift dereceli toplamın içindedir.",
        ]},
        {"baslik": "Polinomların eşitliği", "icerik": [
            "İki polinom, aynı dereceli terimlerinin katsayıları birbirine eşitse eşittir. Bu kural, bilinmeyen katsayıları bulmak için en çok kullanılan araçtır: iki tarafta aynı kuvvetin katsayıları eşitlenir.",
            ornek(
                "$(a-2)x^2+(b+1)x+c=3x^2-4x+5$ eşitliği her $x$ için sağlanıyor.",
                "$a$, $b$ ve $c$ yi bulalım.",
                "$x^2$ nin katsayıları: $a-2=3$, yani $a=5$.",
                "$x$ in katsayıları: $b+1=-4$, yani $b=-5$. Sabit terimler: $c=5$."),
            dikkat(
                "Eşitliği tek bir $x$ değeri için sağlanan denklemle karıştırmak.",
                "Polinom eşitliği her $x$ için sağlanır ve katsayıların eşitliğini gerektirir. $x^2=4$ gibi bir denklem ise yalnızca belirli $x$ değerlerinde doğrudur; bu iki durum karıştırılmamalıdır."),
        ]},
        {"baslik": "Derece bilgisinden bilinmeyen bulmak", "icerik": [
            "Bir polinomun derecesi verildiğinde, daha büyük kuvvetli terimlerin katsayıları sıfır olmalı, verilen derecedeki terimin katsayısı ise sıfırdan farklı olmalıdır. Bu iki koşul bilinmeyen katsayılar için denklem ve eşitsizlik verir.",
            ornek(
                "$P(x)=(m-2)x^3+(n+1)x^2+4x-1$ polinomunun ikinci dereceden olduğu biliniyor.",
                "$m$ ve $n$ hakkında ne söylenebileceğini bulalım.",
                "$x^3$ lü terim olmamalıdır: $m-2=0$, yani $m=2$.",
                "$x^2$ li terim bulunmalıdır: $n+1 \\neq 0$, yani $n \\neq -1$."),
            "Koşulun ikinci kısmı sık unutulur. $n=-1$ olsaydı $x^2$ li terim de kaybolur ve polinom birinci dereceden olurdu; bu yüzden derece sorusunda hem üstteki katsayıların sıfır olması hem de istenen katsayının sıfır olmaması gerekir.",
        ]},
        {"baslik": "Verilen değerlerden katsayı bulmak", "icerik": [
            "Polinomun biçimi bilinip bazı katsayıları bilinmiyorsa, verilen değerler denklem kurmak için kullanılır. Her değer bir denklem verir; bilinmeyen sayısı kadar değer, katsayıları bulmaya yeter.",
            ornek(
                "$P(x)=ax^2+bx+3$ polinomunda $P(1)=6$ ve $P(-1)=4$ tür.",
                "$a$ ve $b$ yi bulalım.",
                "$P(1)=a+b+3=6$, yani $a+b=3$. $P(-1)=a-b+3=4$, yani $a-b=1$.",
                "İki denklem toplanınca $2a=4$: $a=2$ ve $b=1$."),
        ]},
        {"baslik": "Kökleri verilen polinomu yazmak", "icerik": [
            "Kökleri ve baş katsayısı bilinen bir polinom, kökler çarpan olarak yazılıp baş katsayıyla çarpılarak kurulur. Kökleri $r_1$ ve $r_2$, baş katsayısı $a$ olan ikinci dereceden polinom $a(x-r_1)(x-r_2)$ biçimindedir.",
            ornek(
                "Kökleri $1$ ve $-2$, baş katsayısı $3$ olan ikinci dereceden polinom istensin.",
                "Polinomu yazalım.",
                "$P(x)=3(x-1)(x+2)$.",
                "Açılınca: $P(x)=3(x^2+x-2)=3x^2+3x-6$. Kontrol: $P(1)=0$ ve $P(-2)=12-6-6=0$."),
        ]},
        {"baslik": "Toplama ve çıkarma", "icerik": [
            "Polinomlar toplanırken ya da çıkarılırken aynı dereceli terimler, yani benzer terimler kendi aralarında toplanır. Çıkarmada ikinci polinomun bütün terimlerinin işareti değişir.",
            ornek(
                "$P(x)=2x^3-x+4$ ve $Q(x)=x^3+3x^2-5$ polinomları verilsin.",
                "$P(x)+Q(x)$ ve $P(x)-Q(x)$ polinomlarını bulalım.",
                "$P(x)+Q(x)=3x^3+3x^2-x-1$.",
                "$P(x)-Q(x)=2x^3-x+4-x^3-3x^2+5=x^3-3x^2-x+9$."),
        ]},
        {"baslik": "Çarpma", "icerik": [
            "İki polinom çarpılırken birinci polinomun her terimi ikinci polinomun her terimiyle çarpılır ve benzer terimler toplanır. Terimler çarpılırken katsayılar çarpılır, kuvvetler toplanır.",
            ornek(
                "$(2x-3)(x^2+x-1)$ çarpımı verilsin.",
                "Çarpımı bulalım.",
                "$2x$ ile çarpım: $2x^3+2x^2-2x$. $-3$ ile çarpım: $-3x^2-3x+3$.",
                "Toplam: $2x^3-x^2-5x+3$."),
            "Çarpımın sonucunu kontrol etmek için $x$ yerine basit bir değer yazılır. $x=1$ için sol taraf $(-1) \\cdot 1=-1$, sağ taraf $2-1-5+3=-1$ dir; iki taraf eşittir.",
        ]},
        {"baslik": "Özdeşliklerle hızlı çarpma", "icerik": [
            "Bazı çarpımlar o kadar sık kullanılır ki sonuçları ezberlenir. Bu eşitliklere <strong>özdeşlik</strong> denir ve hem çarpmayı hızlandırır hem de ileride çarpanlara ayırmanın temelini oluşturur.",
            tablo(["Özdeşlik", "Açılımı"], [
                ["$(a+b)^2$", "$a^2+2ab+b^2$"],
                ["$(a-b)^2$", "$a^2-2ab+b^2$"],
                ["$(a-b)(a+b)$", "$a^2-b^2$"],
            ]),
            ornek(
                "$(2x+3)^2$ ve $(x-5)(x+5)$ çarpımları verilsin.",
                "Özdeşliklerle açalım.",
                "$(2x+3)^2=4x^2+12x+9$. Ortadaki terim $2 \\cdot 2x \\cdot 3=12x$ tir.",
                "$(x-5)(x+5)=x^2-25$."),
            dikkat(
                "$(a+b)^2$ yi $a^2+b^2$ sanmak.",
                "Ortadaki $2ab$ terimi unutulamaz. $a=1$ ve $b=1$ için $(1+1)^2=4$ iken $1^2+1^2=2$ dir."),
        ]},
        {"baslik": "Derece kuralları", "icerik": [
            "Polinomlarla yapılan işlemlerde sonucun derecesi, işlemi yapmadan bulunabilir. $P$ ve $Q$ sıfırdan farklı polinomlar ve $n$ pozitif bir tam sayı olmak üzere:",
            tablo(["İşlem", "Derece"], [
                ["$P(x) \\cdot Q(x)$", "$\\text{der}[P]+\\text{der}[Q]$"],
                ["$P(x)^n$", "$n \\cdot \\text{der}[P]$"],
                ["$P(x^n)$", "$n \\cdot \\text{der}[P]$"],
                ["$P(x)+Q(x)$", "En fazla büyük olanın derecesi"],
            ]),
            ornek(
                "$\\text{der}[P(x)]=3$ ve $\\text{der}[Q(x)]=2$ olsun.",
                "$P(x) \\cdot Q(x)$, $P(x)^3$, $P(x^2)$ ve $P(x)+Q(x)$ polinomlarının derecelerini bulalım.",
                "$\\text{der}[P \\cdot Q]=3+2=5$. $\\text{der}[P^3]=3 \\cdot 3=9$.",
                "$\\text{der}[P(x^2)]=3 \\cdot 2=6$. $\\text{der}[P+Q]=3$."),
            dikkat(
                "Toplamın derecesini her zaman büyük derece sanmak.",
                "İki polinomun dereceleri ve baş katsayıları eşit ama işaretleri zıtsa en büyük terimler birbirini götürür. $(x^2+x)+(-x^2+3)$ toplamının derecesi $2$ değil $1$ dir."),
        ]},
        {"baslik": "Çarpımın sabit terimi ve katsayılar toplamı", "icerik": [
            "İki polinomun çarpımının sabit terimi, sabit terimlerinin çarpımıdır; katsayılar toplamı da katsayılar toplamlarının çarpımıdır. Bunun nedeni, $P(x) \\cdot Q(x)$ çarpımında $x=0$ ya da $x=1$ yazmanın iki çarpana ayrı ayrı yazmakla aynı sonucu vermesidir.",
            ornek(
                "$P(0)=3$, $Q(0)=-2$, $P(1)=4$ ve $Q(1)=5$ olsun.",
                "$P(x) \\cdot Q(x)$ çarpımının sabit terimini ve katsayılar toplamını bulalım.",
                "Sabit terim: $P(0) \\cdot Q(0)=3 \\cdot (-2)=-6$.",
                "Katsayılar toplamı: $P(1) \\cdot Q(1)=4 \\cdot 5=20$."),
        ]},
        {"baslik": "Çarpım biçimindeki polinomun derecesi", "icerik": [
            "Polinom çarpanlar hâlinde verildiğinde derece ve baş katsayı, çarpımı açmadan bulunur: derece, çarpanların derecelerinin toplamıdır; baş katsayı da çarpanların baş katsayılarının çarpımıdır.",
            ornek(
                "$P(x)=(x^2+1)^3 \\cdot (2x-1)^2$ polinomu verilsin.",
                "Derecesini ve baş katsayısını bulalım.",
                "Derece: $2 \\cdot 3+1 \\cdot 2=8$.",
                "Baş katsayı: $1^3 \\cdot 2^2=4$."),
        ]},
        {"baslik": "Polinomda değer hesaplamak", "icerik": [
            "$P(a)$, polinomda $x$ yerine $a$ yazılarak bulunur. Bu işlem polinomun o noktadaki değerini verir ve grafik üzerinde $(a, P(a))$ noktasına karşılık gelir.",
            ornek(
                "$P(x)=x^3-2x+1$ polinomu verilsin.",
                "$P(2)$ ve $P(-1)$ değerlerini bulalım.",
                "$P(2)=8-4+1=5$.",
                "$P(-1)=-1+2+1=2$."),
            ornek(
                "$P(x+1)=x^2+3x+2$ olduğu biliniyor.",
                "$P(x)$ polinomunu ve $P(3)$ değerini bulalım.",
                "$x$ yerine $x-1$ yazılır: $P(x)=(x-1)^2+3(x-1)+2=x^2+x$.",
                "$P(3)=9+3=12$. Kontrol: $P(3)$, verilen eşitlikte $x=2$ yazılarak da bulunur: $4+6+2=12$."),
        ]},
        {"baslik": "Bileşik girdili polinomlar", "icerik": [
            "$P(2x-1)$ gibi bir ifadenin sabit terimi ve katsayılar toplamı, içteki ifadenin $0$ ve $1$ deki değerleriyle bulunur. $P(2x-1)$ de $x=0$ yazılınca $P(-1)$, $x=1$ yazılınca $P(1)$ elde edilir.",
            ornek(
                "$P(x)=x^2-3x+4$ polinomu verilsin.",
                "$P(2x-1)$ polinomunun katsayılar toplamını ve sabit terimini bulalım.",
                "Katsayılar toplamı: $x=1$ için $P(2 \\cdot 1-1)=P(1)=1-3+4=2$.",
                "Sabit terim: $x=0$ için $P(-1)=1+3+4=8$."),
            "Bu yöntem, $P(2x-1)$ polinomunu hiç açmadan sonuca ulaştırır. Soru polinomun kendisini değil yalnızca bir özelliğini istiyorsa önce bu kısa yolu düşünmek zaman kazandırır.",
        ]},
        {"baslik": "Fonksiyonel eşitlikten polinom bulmak", "icerik": [
            "Bazı sorularda polinomun kendisi değil, $P(x)+P(x-1)$ gibi bir ifadesi verilir. Polinomun derecesi biliniyorsa genel biçimi harflerle yazılır ve iki taraftaki katsayılar eşitlenir.",
            ornek(
                "Birinci dereceden bir $P(x)$ polinomu için $P(x)+P(x-1)=4x+2$ eşitliği veriliyor.",
                "$P(x)$ polinomunu bulalım.",
                "$P(x)=ax+b$ olsun: $ax+b+a(x-1)+b=2ax-a+2b$.",
                "Katsayılar eşitlenir: $2a=4$ ve $2b-a=2$. Buradan $a=2$ ve $b=2$; $P(x)=2x+2$.",
                "Kontrol: $(2x+2)+(2x)=4x+2$."),
        ]},
        {"baslik": "Polinomların grafikleri", "icerik": [
            "Polinomun derecesi grafiğinin genel biçimini belirler. Sabit polinomun grafiği yatay bir doğru, birinci dereceden polinomun grafiği eğik bir doğru, ikinci dereceden polinomun grafiği bir paraboldür. Daha yüksek dereceli polinomların grafikleri daha fazla kıvrım yapabilir.",
            koordinat_grafik("Farklı dereceli polinomların grafikleri",
                             [("y = x (1. derece)", lambda x: x), ("y = x² − 2 (2. derece)", lambda x: x * x - 2), ("y = x³ − 3x (3. derece)", lambda x: x ** 3 - 3 * x)],
                             (-3, 3), (-3, 3)),
            "Derecesi $n$ olan bir polinomun grafiği $x$ eksenini en fazla $n$ noktada keser, çünkü $P(x)=0$ denkleminin en fazla $n$ gerçek kökü vardır. Grafikteki $y=x^3-3x$ eğrisi eksenini üç noktada keser: $x=0$ ve $x=\\pm\\sqrt{3}$.",
        ]},
        {"baslik": "Bölme işlemine hazırlık", "icerik": [
            "Polinomlar da sayılar gibi bölünür. $P(x)$ polinomu $B(x)$ polinomuna bölündüğünde bir $Q(x)$ bölümü ve bir $K(x)$ kalanı bulunur ve aşağıdaki eşitlik sağlanır:",
            "$$P(x)=B(x) \\cdot Q(x)+K(x)$$",
            "Sayılardaki bölmede kalan bölenden küçüktür; polinomlarda ise kalanın <strong>derecesi</strong> bölenin derecesinden küçüktür. Bu yüzden birinci dereceden bir polinoma bölmede kalan her zaman bir sabittir. Sayılarla bir karşılaştırma yapılırsa $17=5 \\cdot 3+2$ eşitliğinde $17$ bölünen, $5$ bölen, $3$ bölüm ve $2$ kalandır; polinom bölmesi de aynı yapıdadır. Bölmenin adım adım nasıl yapıldığı ve kalanın bölme yapmadan nasıl bulunduğu bu serinin sonraki iki yazısında ayrıntılı olarak anlatılıyor.",
        ]},
        {"baslik": "Kök ve çarpan ilişkisi", "icerik": [
            "$P(a)=0$ ise $a$ sayısına polinomun <strong>kökü</strong> denir. Bir polinomun kökü $a$ ise $x-a$ ifadesi polinomun bir çarpanıdır ve polinom $x-a$ ile kalansız bölünür. Bu ilişki, polinomların bölünmesi ve çarpanlara ayrılması konularının temelidir.",
            ornek(
                "$P(x)=x^3-6x^2+11x-6$ polinomu verilsin.",
                "$1$ in bir kök olup olmadığını inceleyelim.",
                "$P(1)=1-6+11-6=0$.",
                "$1$ bir köktür; $x-1$, $P(x)$ polinomunun bir çarpanıdır. Gerçekten $P(x)=(x-1)(x-2)(x-3)$ tür."),
            "Bölme ve kalan konuları <a href=\"/blog/polinomlarda-bolme/\">Polinomlarda Bölme İşlemi</a> ve <a href=\"/blog/polinomlarda-kalan/\">Polinomlarda Kalan Bulma</a> yazılarında, çarpanlara ayırma da <a href=\"/blog/polinomlarda-carpanlara-ayirma/\">Polinomlarda Çarpanlara Ayırma</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sınavda polinomlar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) polinomlar derece, katsayılar toplamı, sabit terim, polinom eşitliği ve değer hesaplama biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) derece kuralları, bileşik girdili polinomlar, bölme, kalan ve çarpanlara ayırma da sorulabilir."),
            "Polinom sorularında ilk düşünülmesi gereken şey, istenen bilginin polinomu açmadan bulunup bulunamayacağıdır. Sabit terim için $0$, katsayılar toplamı için $1$ yazmak ve derece kurallarını kullanmak çoğu soruyu tek satıra indirir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Köklü katsayıyı polinom dışı saymak", "Yalnız değişkenin kuvvetine bakılır"],
                ["Baş katsayıyı ilk yazılan terimden almak", "En büyük kuvvetin katsayısıdır"],
                ["Sabit terimi $P(1)$ ile bulmak", "Sabit terim $P(0)$ dır"],
                ["$\\text{der}[P^3]$ ü $\\text{der}[P]+3$ almak", "$3 \\cdot \\text{der}[P]$"],
                ["Çıkarmada ikinci polinomun işaretlerini değiştirmemek", "Bütün terimlerin işareti değişir"],
                ["Sıfır polinomunun derecesini $0$ sanmak", "Derecesi tanımsızdır"],
            ]),
            "Bu hataların çoğu tanımları aceleyle uygulamaktan doğar. Özellikle derece sorularında, küçük bir örnek polinom seçip kuralı onun üzerinde denemek hatayı hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Polinom nedir?",
         "Değişkenin kuvvetlerinin doğal sayı olduğu, katsayıları gerçek sayı olan terimlerin toplamıdır. Negatif ya da kesirli kuvvet içeren ifadeler polinom değildir."),
        ("Polinomun derecesi nasıl bulunur?",
         "Katsayısı sıfırdan farklı olan en büyük kuvvet polinomun derecesidir. Terimlerin yazılış sırası dereceyi değiştirmez."),
        ("Katsayılar toplamı nasıl bulunur?",
         "Polinomda x yerine 1 yazılır. P(1) değeri bütün katsayıların toplamına eşittir."),
        ("Sabit terim nasıl bulunur?",
         "Polinomda x yerine 0 yazılır. P(0) değeri sabit terime eşittir."),
        ("İki polinom ne zaman eşittir?",
         "Aynı dereceli terimlerinin katsayıları birbirine eşitse iki polinom eşittir. Bilinmeyen katsayılar bu eşitliklerden bulunur."),
        ("Çarpımın derecesi nasıl bulunur?",
         "Çarpanların dereceleri toplanır. Derecesi 3 olan bir polinomla derecesi 2 olan bir polinomun çarpımının derecesi 5 tir."),
        ("Polinomda kök ne demektir?",
         "P(a) = 0 olan a sayısına polinomun kökü denir. Kök a ise x − a ifadesi polinomun bir çarpanıdır ve polinom x − a ile kalansız bölünür."),
        ("Çift dereceli terimlerin katsayıları toplamı nasıl bulunur?",
         "P(1) ile P(−1) toplanır ve ikiye bölünür. Tek dereceli terimler için ise P(1) den P(−1) çıkarılır ve sonuç ikiye bölünür."),
    ],
    "kontrol": [
        "Bir ifadenin polinom olup olmadığına karar verebiliyorum.",
        "Terim, katsayı, derece, baş katsayı ve sabit terimi ayırt edebiliyorum.",
        "Sabit terimi ve katsayılar toplamını polinomu açmadan bulabiliyorum.",
        "Çift ve tek dereceli terimlerin katsayıları toplamını hesaplayabiliyorum.",
        "Polinom eşitliğinden bilinmeyen katsayıları bulabiliyorum.",
        "Polinomları toplayabiliyor, çıkarabiliyor ve çarpabiliyorum.",
        "Derece kurallarını kullanabiliyorum.",
        "Polinomda değer hesaplayabiliyorum.",
        "Bileşik girdili polinomların katsayılar toplamını ve sabit terimini bulabiliyorum.",
        "Kök ile çarpan arasındaki ilişkiyi açıklayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["polinomlarda-bolme", "polinomlarda-kalan", "polinomlarda-carpanlara-ayirma"],
}
