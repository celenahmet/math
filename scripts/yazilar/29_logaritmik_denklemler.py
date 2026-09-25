# scripts/yazilar/29_logaritmik_denklemler.py — Logaritmik Denklemler (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

YAZI = {
    "slug": "logaritmik-denklemler",
    "baslik": "Logaritmik Denklemler Nasıl Çözülür?",
    "aciklama": "Logaritmik denklemler nasıl çözülür? Tanım koşulu, tanıma dönüş, eşit logaritmalar, kurallarla birleştirme, değişken değiştirme, üstel denklem ve eşitsizlik.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "logaritma",
    "sinavlar": ["AYT"],
    "kapak": "logaritmik-denklemler",
    "kapak_alt": "Logaritmik denklemler: hızla yükselen ahşap basamaklar üzerinde kırmızı iple aynı seviyeyi işaretleyen öğrenci",
    "ozet": "Logaritmik denklemlerde bilinmeyen bir logaritmanın içinde ya da tabanında bulunur. Bu denklemler logaritmanın tanımı ve kurallarıyla üslü ya da cebirsel denklemlere çevrilerek çözülür, ama her kökün tanım koşullarını sağlayıp sağlamadığı ayrıca kontrol edilir. Bu yazıda tanım koşulunun önemini, tanıma dönüşü, iki tarafı eşit logaritma olan denklemleri, kurallarla birleştirmeyi, değişken değiştirmeyi, tabanı bilinmeyen denklemleri, logaritma ile çözülen üstel denklemleri, logaritmalı eşitsizlikleri ve büyüme ile azalma problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Logaritmik denklem nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için logaritmanın tanımını ve logaritma kurallarını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/logaritma-konu-anlatimi/\">Logaritma Konu Anlatımı</a> ve <a href=\"/blog/logaritma-kurallari-formulleri/\">Logaritma Kuralları ve Formülleri</a> yazılarına göz at."),
            "Bilinmeyeni bir logaritmanın içinde ya da tabanında bulunan denklemlere <strong>logaritmik denklem</strong> denir. $\\log_2(x+1)=3$ ya da $\\log_x 16=2$ birer logaritmik denklemdir. Bu denklemler, logaritma üslü biçime çevrilerek ya da kurallarla tek bir logaritmada toplanarak çözülür.",
            "Kapaktaki öğrenci hızla yükselen basamakların üzerinde kırmızı bir iple belirli bir seviyeyi işaretliyor. Logaritmik denklem de aynı soruyu sorar: katlanarak büyüyen bir nicelik tam olarak hangi adımda istenen seviyeye ulaşır?",
        ]},
        {"baslik": "Önce tanım koşulu", "icerik": [
            "Logaritmik denklemlerin en önemli adımı çözümün başında yapılır: logaritması alınan her ifade pozitif, her taban pozitif ve $1$ den farklı olmalıdır. Bu koşullar denklemin tanım kümesini belirler.",
            "Cebirsel işlemler sırasında tanım kümesi genişleyebilir; örneğin iki logaritma çarpım kuralıyla birleştirildiğinde tek tek negatif olan iki ifadenin çarpımı pozitif olabilir. Bu yüzden bulunan her kök, başta yazılan koşullarla karşılaştırılmalıdır.",
            hap("Kökü bulduktan sonra tanım koşulunda dene.",
                "Koşulu sağlamayan kök, cebirsel olarak doğru görünse de çözüm değildir."),
        ]},
        {"baslik": "Tanıma dönüş", "icerik": [
            "Denklem $\\log_a f(x)=b$ biçimindeyse tanım doğrudan uygulanır: $f(x)=a^b$. Bu en temel yöntemdir ve diğer yöntemlerin çoğu sonunda bu biçime ulaşır.",
            ornek(
                "$\\log_3(2x+1)=2$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Tanım koşulu: $2x+1>0$. Tanımdan $2x+1=3^2=9$ olur.",
                "$x=4$ bulunur; $2 \\cdot 4+1=9>0$ olduğundan çözüm geçerlidir."),
            ornek(
                "$\\log(x^2-15)=1$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Taban $10$ dur: $x^2-15=10$, yani $x^2=25$.",
                "$x=5$ ya da $x=-5$; ikisinde de $x^2-15=10>0$ olduğundan iki kök de çözümdür."),
        ]},
        {"baslik": "İki tarafta eşit tabanlı logaritma", "icerik": [
            "Denklem $\\log_a f(x)=\\log_a g(x)$ biçimindeyse logaritma fonksiyonu birebir olduğu için içler eşitlenir: $f(x)=g(x)$. Ancak bulunan kök hem $f(x)$ i hem $g(x)$ i pozitif yapmalıdır.",
            ornek(
                "$\\log_5(x+3)=\\log_5(2x-1)$ denklemi verilsin.",
                "Denklemi çözelim.",
                "İçler eşitlenir: $x+3=2x-1$, yani $x=4$.",
                "$x+3=7>0$ ve $2x-1=7>0$ olduğundan $x=4$ çözümdür."),
            ornek(
                "$\\log_2(x^2-3x)=\\log_2(x-3)$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$x^2-3x=x-3$, yani $x^2-4x+3=0$ ve $(x-1)(x-3)=0$ olur.",
                "$x=1$ için $x-3=-2<0$, $x=3$ için $x-3=0$ olduğundan iki kök de atılır; denklemin çözümü yoktur."),
            hap("$\\log_a f(x)=\\log_a g(x)$ ise $f(x)=g(x)$ yazılır.", "Bulunan kök, iki taraftaki ifadenin ikisini de pozitif yapmalıdır."),
        ]},
        {"baslik": "Kare içeren logaritma", "icerik": [
            "Logaritmanın içinde bir kare varsa, ifadenin pozitif olması için karesi alınan ifadenin sıfırdan farklı olması yeter. Bu yüzden karenin logaritması ile logaritmanın iki katı farklı çözüm kümeleri verebilir.",
            ornek(
                "$\\log_3(x-1)^2=2$ ve $2\\log_3(x-1)=2$ denklemleri verilsin.",
                "İki denklemi çözüp karşılaştıralım.",
                "Birincide koşul $x \\neq 1$ dir: $(x-1)^2=9$, yani $x=4$ ya da $x=-2$; iki kök de çözümdür.",
                "İkincide koşul $x>1$ dir: $\\log_3(x-1)=1$, yani $x=4$ tek çözümdür."),
        ]},
        {"baslik": "İç içe logaritmalar", "icerik": [
            "İç içe logaritmalar dıştan içe doğru çözülür. Her adımda tanım uygulanır ve bir önceki logaritmanın değeri bulunur; en sonda bilinmeyene ulaşılır.",
            ornek(
                "$\\log_2(\\log_3(\\log_4 x))=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "En dıştaki logaritma: $\\log_3(\\log_4 x)=2^0=1$. Ortadaki: $\\log_4 x=3^1=3$.",
                "En içteki: $x=4^3=64$ bulunur."),
        ]},
        {"baslik": "Kurallarla birleştirme", "icerik": [
            "Aynı tabanlı birden fazla logaritma varsa çarpım ve bölüm kurallarıyla tek bir logaritmada toplanır. Sonra tanıma dönülür ve cebirsel denklem çözülür.",
            ornek(
                "$\\log_2 x+\\log_2(x-2)=3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Tanım koşulu: $x>2$. Çarpım kuralıyla $x(x-2)=2^3=8$, yani $x^2-2x-8=0$ ve $(x-4)(x+2)=0$.",
                "$x=-2$ koşulu sağlamaz; çözüm $x=4$ tür."),
            ornek(
                "$\\log(x+1)-\\log(x-1)=\\log 3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Tanım koşulu: $x>1$. Bölüm kuralıyla $\\dfrac{x+1}{x-1}=3$ olur.",
                "$x+1=3x-3$, yani $x=2$ bulunur ve koşulu sağlar."),
        ]},
        {"baslik": "Katsayılı logaritmalar", "icerik": [
            "Logaritmanın önünde katsayı varsa kuvvet kuralıyla üsse taşınır. Böylece her iki taraf da katsayısız tek bir logaritmaya indirilir.",
            ornek(
                "$2\\log_3 x=\\log_3(x+6)$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Tanım koşulu: $x>0$. Kuvvet kuralıyla $\\log_3 x^2=\\log_3(x+6)$, yani $x^2=x+6$ ve $(x-3)(x+2)=0$.",
                "$x=-2$ koşulu sağlamaz; çözüm $x=3$ tür."),
            dikkat(
                "Katsayıyı üsse taşırken tanım kümesini değiştirmek.",
                "Denklemdeki $2\\log_3 x$ yalnızca $x>0$ için tanımlıdır, ama $\\log_3 x^2$ her $x \\neq 0$ için tanımlıdır. Bu yüzden $x=-2$ kökü ikinci biçimde denklemi sağlar gibi görünür; asıl denklemin koşulu $x>0$ olduğu için atılmalıdır."),
        ]},
        {"baslik": "Farklı tabanları eşitlemek", "icerik": [
            "Denklemde farklı tabanlı logaritmalar varsa, tabanın kuvveti kuralı ya da taban değiştirme formülüyle hepsi aynı tabana getirilir. Tabanlar aynı asal sayının kuvvetleriyse en küçük taban seçilir.",
            ornek(
                "$\\log_2 x=\\log_4(x+2)$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Tanım koşulu: $x>0$. $\\log_4(x+2)=\\dfrac{1}{2}\\log_2(x+2)$ olduğundan $2\\log_2 x=\\log_2(x+2)$, yani $x^2=x+2$.",
                "$(x-2)(x+1)=0$; $x=-1$ atılır, çözüm $x=2$ dir."),
        ]},
        {"baslik": "Değişken değiştirme", "icerik": [
            "Denklemde aynı logaritmanın hem karesi hem kendisi varsa, logaritma yeni bir değişkenle gösterilir. Denklem ikinci dereceden olur ve bulunan her kök ayrı bir logaritma denklemi verir.",
            ornek(
                "$(\\log_2 x)^2-3\\log_2 x+2=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$\\log_2 x=t$ yazılırsa $t^2-3t+2=0$, yani $(t-1)(t-2)=0$.",
                "$t=1$ için $x=2$, $t=2$ için $x=4$ bulunur."),
            ornek(
                "$\\log_3 x+\\log_x 3=\\dfrac{5}{2}$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$\\log_x 3=\\dfrac{1}{\\log_3 x}$ olduğundan $t+\\dfrac{1}{t}=\\dfrac{5}{2}$ olur; buradan $2t^2-5t+2=0$ ve $(2t-1)(t-2)=0$.",
                "$t=2$ için $x=9$, $t=\\dfrac{1}{2}$ için $x=\\sqrt{3}$ bulunur."),
            hap("Aynı logaritmanın hem karesi hem kendisi varsa logaritma yeni bir değişkenle gösterilir ve denklem ikinci dereceden olur."),
        ]},
        {"baslik": "Tabanda bilinmeyen", "icerik": [
            "Bilinmeyen tabandaysa denklem yine üslü biçime çevrilir. Bu kez tabanın pozitif ve $1$ den farklı olma koşulu kontrol edilir.",
            ornek(
                "$\\log_x 16=2$ ve $\\log_{x-1} 9=2$ denklemleri verilsin.",
                "Denklemleri çözelim.",
                "Birincide $x^2=16$, yani $x=\\pm 4$; taban pozitif olmalı, çözüm $x=4$ tür.",
                "İkincide $(x-1)^2=9$, yani $x-1=\\pm 3$; taban pozitif olmalı, $x-1=3$ ve $x=4$ bulunur."),
        ]},
        {"baslik": "Taban ve sayıda bilinmeyen", "icerik": [
            "Bilinmeyen hem tabanda hem de logaritması alınan ifadede bulunabilir. Tanım uygulanınca cebirsel bir denklem elde edilir; köklerden tabanı pozitif ve $1$ den farklı yapan ve içteki ifadeyi pozitif yapanlar alınır.",
            ornek(
                "$\\log_x(2x+3)=2$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Tanımdan $x^2=2x+3$, yani $x^2-2x-3=0$ ve $(x-3)(x+1)=0$.",
                "$x=-1$ taban olamaz; $x=3$ için taban $3$, içteki ifade $9$ olur ve çözüm geçerlidir."),
        ]},
        {"baslik": "Kökler toplamı ve çarpımı", "icerik": [
            "Değişken değiştirmeyle çözülen denklemlerde kökler toplamı ya da çarpımı sorulabilir. Yardımcı değişkenin kökleri toplanırken asıl köklerin çarpımı ortaya çıkar; çünkü logaritmaların toplamı çarpımın logaritmasıdır.",
            ornek(
                "$(\\log_2 x)^2-5\\log_2 x+6=0$ denklemi verilsin.",
                "Köklerin toplamını ve çarpımını bulalım.",
                "$\\log_2 x=t$ yazılırsa $(t-2)(t-3)=0$; $x=4$ ve $x=8$ bulunur.",
                "Kökler toplamı $12$, çarpımı $32$ dir; çarpım $2^{2+3}=2^5$ olarak da yazılabilir."),
        ]},
        {"baslik": "Üslü ve logaritmalı birlikte", "icerik": [
            "Bazı denklemlerde bilinmeyen hem tabanda hem üste logaritma olarak bulunur. Bu durumda iki tarafın logaritması alınır ve denklem logaritmaya göre ikinci dereceden bir denkleme dönüşür.",
            ornek(
                "$x^{\\log x}=100x$ denklemi verilsin.",
                "Denklemi çözelim.",
                "İki tarafın onluk logaritması alınır: $(\\log x)^2=2+\\log x$. $\\log x=t$ yazılırsa $t^2-t-2=0$, yani $(t-2)(t+1)=0$.",
                "$t=2$ için $x=100$, $t=-1$ için $x=\\dfrac{1}{10}$ bulunur; iki değer de pozitif olduğundan ikisi de çözümdür."),
        ]},
        {"baslik": "Logaritmalı denklem sistemleri", "icerik": [
            "İki bilinmeyenli logaritmalı denklem sistemlerinde logaritmalar birer yeni değişken gibi düşünülür. Böylece sistem doğrusal bir sisteme dönüşür; bulunan logaritma değerlerinden sayılara tanım yoluyla geçilir.",
            ornek(
                "$\\log x+\\log y=3$ ve $\\log x-\\log y=1$ sistemi verilsin.",
                "Sistemi çözelim.",
                "$\\log x=u$ ve $\\log y=v$ yazılırsa $u+v=3$ ve $u-v=1$ olur; buradan $u=2$ ve $v=1$.",
                "$x=10^2=100$ ve $y=10^1=10$ bulunur; ikisi de pozitif olduğundan çözüm geçerlidir."),
        ]},
        {"baslik": "Üstel denklemler ve logaritma", "icerik": [
            "Bilinmeyeni üste olan denklemlerde iki taraf aynı tabana getirilemiyorsa logaritma alınır. Böylece üs, kuvvet kuralıyla logaritmanın önüne iner ve doğrusal bir denklem kalır.",
            ornek(
                "$5^x=3$ ve $2^x=3^{x-1}$ denklemleri verilsin.",
                "Denklemleri çözelim.",
                "Birincinin çözümü doğrudan $x=\\log_5 3$ olur.",
                "İkincide iki tarafın doğal logaritması alınır: $x\\ln 2=(x-1)\\ln 3$, buradan $x=\\dfrac{\\ln 3}{\\ln 3-\\ln 2}$, yaklaşık $2.71$ olur."),
            hap("İki taraf aynı tabana getirilemiyorsa logaritma alınır; üs, kuvvet kuralıyla öne iner."),
        ]},
        {"baslik": "Sabit çarpanlı üstel denklem", "icerik": [
            "Üssünde sabit bir ekleme bulunan denklemlerde önce üs kuralıyla sabit çarpan ayrılır. Sonra kalan kuvvet yalnız bırakılır ve logaritma alınır.",
            ornek(
                "$2^{x+1}=5$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$2 \\cdot 2^x=5$, yani $2^x=\\dfrac{5}{2}$ olur.",
                "Çözüm $x=\\log_2 \\dfrac{5}{2}=\\log_2 5-1$ olur; $2<\\dfrac{5}{2}<4$ olduğundan $x$, $1$ ile $2$ arasındadır."),
        ]},
        {"baslik": "Aynı tabana getirme", "icerik": [
            "Üstel denklemde iki taraf aynı tabanın kuvveti olarak yazılabiliyorsa logaritmaya gerek kalmaz; üsler eşitlenir. Üsler içinde aynı kuvvetin farklı katları varsa değişken değiştirme uygulanır.",
            ornek(
                "$4^x=8$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$2^{2x}=2^3$ olur.",
                "$2x=3$, yani $x=\\dfrac{3}{2}$ bulunur."),
            ornek(
                "$9^x-4 \\cdot 3^x+3=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$3^x=t$ yazılırsa $9^x=t^2$ olur ve $t^2-4t+3=0$, yani $(t-1)(t-3)=0$.",
                "$3^x=1$ için $x=0$, $3^x=3$ için $x=1$ bulunur."),
        ]},
        {"baslik": "Grafikle çözüm", "icerik": [
            "Cebirsel olarak çözülemeyen bazı denklemlerin çözümü grafikle bulunur ya da sayılır. İki tarafın grafikleri çizilir; kesişim noktalarının apsisleri denklemin çözümleridir.",
            koordinat_grafik("y = log2 x ile y = 3 - x doğrusunun kesişimi", [("y = log2 x", lambda x: math.log2(x) if x > 0 else None), ("y = 3 - x", lambda x: 3 - x)],
                             (-1, 6), (-3, 5.5), adim=1, noktalar=[(2, 1, "", True)]),
            "Grafikte artan logaritma eğrisi ile azalan doğru yalnızca bir kez kesişir; bu nokta $(2, 1)$ dir. Gerçekten $\\log_2 2=1=3-2$ olur. Biri artan diğeri azalan iki fonksiyonun en fazla bir kez kesişmesi, çözümün tek olduğunu da gösterir.",
        ]},
        {"baslik": "Logaritmalı eşitsizlikler", "icerik": [
            "Logaritmalı eşitsizliklerde iki kural birlikte uygulanır: tanım koşulu yazılır ve taban $1$ den büyükse yön korunur, $0$ ile $1$ arasındaysa yön değişir. Çözüm kümesi bu iki koşulun kesişimidir.",
            ornek(
                "$\\log_2(x-1)<3$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "Tanım koşulu $x>1$; taban $1$ den büyük olduğundan $x-1<8$, yani $x<9$.",
                "Çözüm kümesi $(1, 9)$ aralığıdır."),
            ornek(
                "$\\log_{1/3} x>2$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "Taban $1$ den küçük olduğundan yön değişir: $x<\\left(\\dfrac{1}{3}\\right)^2=\\dfrac{1}{9}$.",
                "Tanım koşuluyla birlikte çözüm kümesi $\\left(0, \\dfrac{1}{9}\\right)$ aralığıdır."),
        ]},
        {"baslik": "Kurallı eşitsizlik", "icerik": [
            "Birden fazla logaritma içeren eşitsizlikler, denklemlerde olduğu gibi önce tek bir logaritmada birleştirilir. Tanım koşulu, birleştirmeden önceki ifadelere göre yazılmalıdır.",
            ornek(
                "$\\log x+\\log(x-3) \\le 1$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "Tanım koşulu $x>3$. Birleştirince $x(x-3) \\le 10$, yani $x^2-3x-10 \\le 0$ ve $(x-5)(x+2) \\le 0$, buradan $-2 \\le x \\le 5$.",
                "Tanım koşuluyla kesişim alınınca çözüm kümesi $(3, 5]$ aralığı olur."),
        ]},
        {"baslik": "Uygulama: bileşik faiz", "icerik": [
            "Bileşik faizde para her dönem aynı oranda büyür; paranın belirli bir tutara ulaşması için gereken süre logaritma ile bulunur. Süre tam sayı olmak zorundaysa bulunan değer yukarı yuvarlanır.",
            ornek(
                "$1000$ TL yıllık yüzde $10$ bileşik faizle yatırılıyor.",
                "Paranın ilk kez $2000$ TL yi geçtiği yılı bulalım.",
                "$1000 \\cdot 1.1^n \\ge 2000$ olmalı, yani $1.1^n \\ge 2$ ve $n \\ge \\dfrac{\\log 2}{\\log 1.1}$ olur.",
                "Bu oran yaklaşık $7.27$ olduğundan para $8$ yıl sonunda iki katını geçer."),
            "Faiz hesaplarının ayrıntısı için <a href=\"/blog/faiz-problemleri-nasil-cozulur/\">Faiz Problemleri Nasıl Çözülür?</a> yazısına bakabilirsin.",
            hap("İkinci el değeri her yıl yüzde $20$ düşen bir telefonun değeri her yıl $0.8$ ile çarpılır.", "$0.8^3=0.512$ ve $0.8^4=0.4096$ olduğu için telefon, ilk değerinin yarısının altına dördüncü yılda iner.", gunluk=True),
        ]},
        {"baslik": "Uygulama: nüfus artışı", "icerik": [
            "Sabit sürelerde iki katına çıkan bir niceliğin belirli bir değere ulaşma zamanı da logaritmik bir denklemle bulunur.",
            ornek(
                "Bir bakteri kolonisinin sayısı $N(t)=100 \\cdot 2^{t/3}$ ile veriliyor; $t$ saat cinsindendir.",
                "Koloninin $1600$ bakteriye ulaştığı zamanı bulalım.",
                "$100 \\cdot 2^{t/3}=1600$ ise $2^{t/3}=16=2^4$ olur.",
                "$\\dfrac{t}{3}=4$, yani $t=12$ saat bulunur."),
        ]},
        {"baslik": "Uygulama: yarılanma süresi", "icerik": [
            "Radyoaktif maddeler sabit bir sürede yarıya iner; bu süreye yarılanma süresi denir. Kalan miktarın belirli bir değere inme zamanı, tabanı $\\dfrac{1}{2}$ olan bir üstel denklemle bulunur.",
            ornek(
                "Yarılanma süresi $5$ yıl olan bir maddeden $80$ gram var; $t$ yıl sonra kalan miktar $m(t)=80 \\cdot \\left(\\dfrac{1}{2}\\right)^{t/5}$ gramdır.",
                "Madde $10$ grama kaç yılda iner?",
                "$80 \\cdot \\left(\\dfrac{1}{2}\\right)^{t/5}=10$ ise $\\left(\\dfrac{1}{2}\\right)^{t/5}=\\dfrac{1}{8}=\\left(\\dfrac{1}{2}\\right)^3$ olur.",
                "$\\dfrac{t}{5}=3$, yani $t=15$ yıl bulunur."),
        ]},
        {"baslik": "Yöntem seçimi", "icerik": [
            "Denklemin görünüşü hangi yöntemin kullanılacağını söyler. Aşağıdaki tablo en sık karşılaşılan biçimleri ve ilk adımı özetler:",
            tablo(["Denklemin biçimi", "İlk adım"], [
                ["$\\log_a f(x)=b$", "Tanıma dön: $f(x)=a^b$"],
                ["$\\log_a f(x)=\\log_a g(x)$", "İçleri eşitle"],
                ["Birden fazla logaritma", "Kurallarla birleştir"],
                ["Farklı tabanlar", "Aynı tabana getir"],
                ["Logaritmanın karesi", "Değişken değiştir"],
                ["$a^x=b$, ortak taban yok", "Logaritma al"],
            ]),
            "Hangi yöntem seçilirse seçilsin son adım aynıdır: bulunan kökler tanım koşulunda denenir. Birden fazla yöntem gerekiyorsa sıra genellikle aynıdır: önce tabanlar eşitlenir, sonra logaritmalar birleştirilir, en sonda tanıma dönülür.",
        ]},
        {"baslik": "Sınavda logaritmik denklemler", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) logaritmik denklemler; kökler toplamı, çözüm kümesi, değişken değiştirme, tabanı bilinmeyen denklemler ve eşitsizlikler biçiminde karşına çıkabilir.",
                "Bileşik faiz ve büyüme problemleri de bu yöntemlerle çözülür."),
            "Kökler toplamı ya da çarpımı sorulduğunda, tanım koşulunu sağlamayan kökler hesaba katılmaz. Bu yüzden ikinci dereceden denklemin katsayılarından doğrudan toplam yazmak yerine kökleri tek tek bulup denemek daha güvenlidir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Kökleri tanım koşulunda denememek", "Her kök denenir"],
                ["$\\log(x+y)=\\log x+\\log y$ yazmak", "Toplamın logaritması açılmaz"],
                ["$2\\log x$ yerine $\\log x^2$ yazıp koşulu genişletmek", "Asıl denklemin koşulu geçerli"],
                ["Tabanda negatif kökü kabul etmek", "Taban pozitif ve $1$ den farklı"],
                ["Tabanı $1$ den küçük eşitsizlikte yönü korumak", "Yön değişir"],
                ["Faiz süresini aşağı yuvarlamak", "Tam dönem için yukarı yuvarlanır"],
            ]),
            "Logaritmik denklemlerdeki hataların neredeyse tamamı tanım kümesiyle ilgilidir. Çözüme başlarken koşulları yazmak ve sonunda her kökü bu koşullarla karşılaştırmak bu hataları önler.",
        ]},
    ],
    "sss": [
        ("Logaritmik denklem nedir?",
         "Bilinmeyenin bir logaritmanın içinde ya da tabanında bulunduğu denklemdir. Örneğin log3(2x + 1) eşittir 2 bir logaritmik denklemdir."),
        ("Logaritmik denklemde kökler neden kontrol edilir?",
         "Kurallarla birleştirme sırasında tanım kümesi genişleyebilir. Bulunan kök logaritması alınan ifadeyi negatif ya da sıfır yapıyorsa çözüm değildir."),
        ("İki tarafı logaritma olan denklem nasıl çözülür?",
         "Tabanlar aynıysa içler eşitlenir. Bulunan kök iki taraftaki ifadeyi de pozitif yapmalıdır."),
        ("Üstel denklem logaritma ile nasıl çözülür?",
         "İki tarafın logaritması alınır ve üs, kuvvet kuralıyla logaritmanın önüne indirilir. Örneğin 5 üzeri x eşittir 3 ise x eşittir log5 3 tür."),
        ("Logaritmalı eşitsizlikte yön ne zaman değişir?",
         "Taban 0 ile 1 arasındaysa logaritma azalan olduğu için eşitsizliğin yönü değişir. Taban 1 den büyükse yön korunur."),
        ("Para kaç yılda iki katına çıkar?",
         "Yıllık yüzde 10 bileşik faizde log 2 nin log 1.1 e bölümü yaklaşık 7.27 olduğundan para 8 yıl sonunda iki katını geçer."),
        ("Logaritmik denklemin çözümü olmayabilir mi?",
         "Evet. Bulunan bütün kökler tanım koşulunu sağlamıyorsa denklemin çözüm kümesi boştur. Bu yüzden kökler her zaman asıl denklemde denenir."),
    ],
    "kontrol": [
        "Tanım koşullarını çözüme başlamadan yazabiliyorum.",
        "Tanıma dönerek temel logaritmik denklemleri çözebiliyorum.",
        "İki tarafı eşit tabanlı logaritma olan denklemleri çözebiliyorum.",
        "Kurallarla logaritmaları birleştirip denklem çözebiliyorum.",
        "Farklı tabanları eşitleyebiliyorum.",
        "Değişken değiştirme yöntemini uygulayabiliyorum.",
        "Tabanı bilinmeyen denklemleri çözebiliyorum.",
        "Üstel denklemleri logaritma ile çözebiliyorum.",
        "Logaritmalı eşitsizlikleri çözebiliyorum.",
        "Faiz, büyüme ve yarılanma problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["logaritma-konu-anlatimi", "logaritma-kurallari-formulleri", "faiz-problemleri-nasil-cozulur"],
}
