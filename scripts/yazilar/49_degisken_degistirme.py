# scripts/yazilar/49_degisken_degistirme.py — Integralde Degisken Degistirme (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "degisken-degistirme",
    "baslik": "İntegralde Değişken Değiştirme Yöntemi",
    "aciklama": "İntegralde değişken değiştirme nasıl yapılır? Zincirin tersi, u seçimi, katsayı ayarı, üstel, logaritmik ve trigonometrik örnekler, sınır dönüşümü; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "degisken-degistirme",
    "kapak_alt": "İntegralde değişken değiştirme: kıvrımlı mavi şeritleri ahşap çerçeveden geçirip düz şeritlere dönüştüren iki öğrenci",
    "ozet": "Değişken değiştirme, karmaşık görünen bir integrali yeni bir değişken tanımlayarak tablodaki basit bir integrale dönüştürme yöntemidir. Zincir kuralının tersidir ve integrali alınan fonksiyonda bir iç fonksiyon ile onun türevi birlikte bulunduğunda kullanılır. Bu yazıda yöntemin zincir kuralıyla ilişkisini, adımlarını, doğru yeni değişkeni seçmeyi, katsayı ayarlamayı, kök, kesir, üstel, logaritmik ve trigonometrik integrallerde kullanımı, doğrusal iç fonksiyonları, belirli integralde sınırların dönüştürülmesini, eski değişkeni yeni değişkenle ifade etmeyi ve yöntemin sınırlarını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Değişken değiştirme nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için zincir kuralını ve temel integral kurallarını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/zincir-kurali/\">Bileşke Fonksiyonun Türevi: Zincir Kuralı</a> ve <a href=\"/blog/belirsiz-integral/\">Belirsiz İntegral Konu Anlatımı</a> yazılarına göz at."),
            "$\\int 2x(x^2+1)^3\\,dx$ gibi bir integrali açarak hesaplamak mümkündür ama uzundur; kuvvet büyüdükçe neredeyse imkânsız hâle gelir. <strong>Değişken değiştirme</strong> yönteminde içteki ifadeye yeni bir ad verilir ve integral, tablodaki basit bir integrale dönüşür.",
            "Kapaktaki öğrenciler kıvrımlı mavi şeritleri ahşap bir çerçeveden geçiriyor; çerçevenin öbür yanından şeritler düz olarak çıkıyor. Değişken değiştirme de böyle bir dönüşümdür: karmaşık görünen integral, yeni değişkenin çerçevesinden geçince düz ve tanıdık bir biçim alır.",
        ]},
        {"baslik": "Zincir kuralının tersi", "icerik": [
            "Zincir kuralına göre $F(g(x))$ in türevi $F'(g(x)) \\cdot g'(x)$ tir. $F'=f$ yazılırsa bu eşitlik tersten okunarak bir integral kuralı verir:",
            "$$\\int f(g(x)) \\cdot g'(x)\\,dx=F(g(x))+C$$",
            "Yani integrali alınan ifadede bir iç fonksiyon $g(x)$ ve onun türevi $g'(x)$ çarpan olarak birlikte bulunuyorsa, integral dış fonksiyonun ters türevinin iç fonksiyonda hesaplanmasıyla bulunur. Değişken değiştirme, bu kuralı sistemli uygulamanın yoludur.",
            hap("İç fonksiyon ile türevi birlikte görünüyorsa değişken değiştir.",
                "Yöntem, zincir kuralını tersten okumaktır."),
        ]},
        {"baslik": "dx ve du nin anlamı", "icerik": [
            "İntegraldeki $dx$, değişkendeki çok küçük bir değişimi temsil eder. $u=g(x)$ seçildiğinde $x$ çok az değişirse $u$ yaklaşık $g'(x)$ katı kadar değişir; bu yüzden $du=g'(x)\\,dx$ yazılır. Bu eşitlik, integraldeki $g'(x)\\,dx$ çarpımının tamamen $du$ ile değiştirilebileceğini söyler.",
            "Bu bakış, yöntemin neden türevi integralde bulunan ifadelerde işlediğini açıklar: türev çarpanı ile $dx$ birlikte $du$ ya dönüşür ve integralde yalnızca $u$ kalır. Türev çarpanı yoksa $dx$ tek başına $du$ ya çevrilemez.",
            hap("Değişken değiştirmek birim değiştirmeye benzer: bir yol kilometre yerine metreyle ölçülürse her kilometre $1000$ metre sayılır.", "$du=g'(x)\\,dx$ eşitliği de iki değişken arasındaki bu dönüşüm katsayısıdır.", gunluk=True),
        ]},
        {"baslik": "Yöntemin adımları", "icerik": [
            "Değişken değiştirme, hangi integral olursa olsun aynı beş adımda yapılır. Adımların her biri kısa bir işlemdir ve sırası her integralde aynıdır:",
            tablo(["Adım", "İşlem"], [
                ["1", "İç fonksiyonu $u$ olarak seç"],
                ["2", "Türevini al: $du=u'\\,dx$"],
                ["3", "İntegrali tamamen $u$ ve $du$ ile yaz"],
                ["4", "Yeni integrali hesapla"],
                ["5", "$u$ yerine eski ifadeyi yaz"],
            ]),
            "Üçüncü adımda integralde $x$ kalmamalıdır. Hâlâ $x$ kalıyorsa ya $u$ yanlış seçilmiştir ya da $x$ in $u$ cinsinden yazılması gerekir.",
        ]},
        {"baslik": "İlk örnek", "icerik": [
            "Yöntemin adımları, açarak da hesaplanabilen bir integralle izlenirse neyin neden yapıldığı daha iyi görülür. Burada içteki ifade $x^2+1$, onun türevi olan $2x$ ise integralde çarpan olarak zaten bulunuyor.",
            ornek(
                "$\\int 2x(x^2+1)^3\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+1$ seçilirse $du=2x\\,dx$ olur ve integral $\\int u^3\\,du=\\dfrac{u^4}{4}+C$ ye dönüşür.",
                "$u$ yerine yazılınca sonuç $\\dfrac{(x^2+1)^4}{4}+C$ olur."),
            "Sonucun türevi zincir kuralıyla $\\dfrac{4(x^2+1)^3 \\cdot 2x}{4}=2x(x^2+1)^3$ verir; integral doğrudur.",
        ]},
        {"baslik": "Doğru u yu seçmek", "icerik": [
            "Değişken değiştirmenin en önemli ve en çok deneyim isteyen adımı $u$ nun seçimidir. Genel kural şudur: türevi integralde çarpan olarak bulunan iç ifade $u$ seçilir. Bu ifade çoğu zaman bir parantezin, bir kökün, bir paydanın ya da bir üssün içindedir.",
            tablo(["İntegralde görülen", "Seçilecek $u$"], [
                ["$(x^2+1)^n$ ve $x$", "$x^2+1$"],
                ["$\\sqrt{x^2+4}$ ve $x$", "$x^2+4$"],
                ["$e^{x^2}$ ve $x$", "$x^2$"],
                ["$\\ln x$ ve $\\dfrac{1}{x}$", "$\\ln x$"],
                ["$\\sin^n x$ ve $\\cos x$", "$\\sin x$"],
            ]),
            "Seçim yanlışsa üçüncü adımda $x$ ler temizlenmez ve integral daha karmaşık hâle gelir. Bu durumda başka bir $u$ denenir; yöntem deneme gerektirir ama doğru seçim genellikle ilk bakışta görülür.",
            hap("Türevi integralde çarpan olarak bulunan iç ifade $u$ seçilir."),
        ]},
        {"baslik": "Katsayıyı ayarlamak", "icerik": [
            "İç fonksiyonun türevi integralde tam olarak değil, bir sabit katsayı farkıyla bulunuyorsa integral yine değişken değiştirmeyle alınır. Eksik ya da fazla sabit, integralin dışında düzeltilir.",
            ornek(
                "$\\int x(x^2+1)^5\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+1$ için $du=2x\\,dx$, yani $x\\,dx=\\dfrac{du}{2}$ olur; integral $\\dfrac{1}{2}\\int u^5\\,du=\\dfrac{u^6}{12}+C$ olur.",
                "Sonuç $\\dfrac{(x^2+1)^6}{12}+C$ dir."),
            dikkat(
                "Eksik olan bir değişkeni dışarıdan eklemeye çalışmak.",
                "Sabit bir katsayı integralin dışına alınıp düzeltilebilir, ama eksik bir $x$ çarpanı düzeltilemez. $\\int (x^2+1)^5\\,dx$ integralinde $x$ çarpanı olmadığı için bu değişken değiştirme işe yaramaz; bu integral açılarak hesaplanır."),
            hap("İç fonksiyonun türevi yalnız bir sabit farkıyla bulunuyorsa eksik sabit integralin dışında düzeltilir.", "Eksik bir $x$ çarpanı ise bu yolla düzeltilemez."),
        ]},
        {"baslik": "Kök içeren integraller", "icerik": [
            "Kök içindeki ifade $u$ seçilir; kök, $u$ nun kesirli kuvvetine dönüşür ve kuvvet kuralıyla integrali alınır. Sonuç yeniden kök biçiminde yazılabilir.",
            ornek(
                "$\\int x\\sqrt{x^2+4}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+4$ için $x\\,dx=\\dfrac{du}{2}$ olur; integral $\\dfrac{1}{2}\\int u^{1/2}\\,du=\\dfrac{1}{2} \\cdot \\dfrac{2}{3}u^{3/2}$ olur.",
                "Sonuç $\\dfrac{(x^2+4)^{3/2}}{3}+C$ dir."),
        ]},
        {"baslik": "Paydada karekök", "icerik": [
            "Kesrin paydasında bir karekök, payında da kökün iç ifadesinin türevi varsa kök içi $u$ seçilir. Kesir böylece $u^{-1/2}$ biçiminde bir kuvvete dönüşür ve kuvvet kuralıyla integrali alınır.",
            ornek(
                "$\\int \\dfrac{x}{\\sqrt{x^2+1}}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+1$ için integral $\\dfrac{1}{2}\\int u^{-1/2}\\,du=\\dfrac{1}{2} \\cdot 2u^{1/2}$ olur.",
                "Sonuç $\\sqrt{x^2+1}+C$ dir."),
        ]},
        {"baslik": "Paydada kuvvet", "icerik": [
            "Kesrin paydasında bir ifadenin kuvveti, payında da o ifadenin türevi varsa, ifade $u$ seçilir ve kesir negatif üslü bir kuvvete dönüşür.",
            ornek(
                "$\\int \\dfrac{x}{(x^2+1)^2}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2+1$ için integral $\\dfrac{1}{2}\\int u^{-2}\\,du=-\\dfrac{1}{2u}+C$ olur.",
                "Sonuç $-\\dfrac{1}{2(x^2+1)}+C$ dir."),
        ]},
        {"baslik": "Pay paydanın türevi", "icerik": [
            "Payı paydanın türevine eşit olan kesirler değişken değiştirmenin özel ve çok sık görülen bir durumudur. Payda $u$ seçilince integral $\\int \\dfrac{du}{u}$ olur ve sonuç doğal logaritmadır.",
            ornek(
                "$\\int \\dfrac{3x^2}{x^3+1}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^3+1$ için $du=3x^2\\,dx$ olur ve integral $\\int \\dfrac{du}{u}=\\ln|u|+C$ ye dönüşür.",
                "Sonuç $\\ln|x^3+1|+C$ dir."),
            "Bu kalıp genel olarak $\\int \\dfrac{g'(x)}{g(x)}\\,dx=\\ln|g(x)|+C$ biçiminde yazılır ve logaritmik türevin tersidir.",
        ]},
        {"baslik": "Üstel integraller", "icerik": [
            "Üssünde bir ifade bulunan üstel fonksiyonlarda üsteki ifade $u$ seçilir; üstel fonksiyon türevde de integralde de biçimini koruduğu için bu seçim hesabı çok kısaltır. Üssün türevi integralde çarpan olarak bulunuyorsa integral $\\int e^u\\,du=e^u+C$ ye dönüşür.",
            ornek(
                "$\\int x e^{x^2}\\,dx$ ve $\\int \\dfrac{e^{\\sqrt{x}}}{\\sqrt{x}}\\,dx$ integralleri verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "Birincide $u=x^2$ ve $x\\,dx=\\dfrac{du}{2}$ olur; sonuç $\\dfrac{e^{x^2}}{2}+C$ dir.",
                "İkincide $u=\\sqrt{x}$ ve $\\dfrac{dx}{\\sqrt{x}}=2\\,du$ olur; sonuç $2e^{\\sqrt{x}}+C$ dir."),
        ]},
        {"baslik": "Üstel kesir", "icerik": [
            "Paydasında üstel bir ifade bulunan bazı kesirlerde pay, paydanın türevine eşittir. Bu durumda payda $u$ seçilir ve sonuç logaritma olur.",
            ornek(
                "$\\int \\dfrac{e^x}{e^x+1}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=e^x+1$ için $du=e^x\\,dx$ olur ve integral $\\int \\dfrac{du}{u}$ ya dönüşür.",
                "Sonuç $\\ln(e^x+1)+C$ dir; $e^x+1$ her zaman pozitif olduğu için mutlak değere gerek yoktur."),
        ]},
        {"baslik": "Logaritmik integraller", "icerik": [
            "İntegralde $\\ln x$ ile birlikte $\\dfrac{1}{x}$ çarpanı görülüyorsa $u=\\ln x$ seçilir; çünkü $du=\\dfrac{dx}{x}$ tir. Bu seçim logaritmayı basit bir değişkene çevirir.",
            ornek(
                "$\\int \\dfrac{\\ln x}{x}\\,dx$ ve $\\int \\dfrac{1}{x\\ln x}\\,dx$ integralleri verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "Birincide $u=\\ln x$ ile $\\int u\\,du=\\dfrac{u^2}{2}$ olur; sonuç $\\dfrac{(\\ln x)^2}{2}+C$ dir.",
                "İkincide aynı seçimle $\\int \\dfrac{du}{u}$ olur; sonuç $\\ln|\\ln x|+C$ dir."),
        ]},
        {"baslik": "Trigonometrik integraller", "icerik": [
            "Sinüs ve kosinüs, işaret dışında birbirinin türevi olduğu için trigonometrik çarpımlarda değişken değiştirme çok sık kullanılır. Kuvveti olan fonksiyon $u$ seçilir, diğeri türev olarak $du$ yu oluşturur.",
            ornek(
                "$\\int \\sin x\\cos x\\,dx$ ve $\\int \\sin^4 x\\cos x\\,dx$ integralleri verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=\\sin x$ için $du=\\cos x\\,dx$ olur; birincisi $\\dfrac{\\sin^2 x}{2}+C$ olur.",
                "Aynı seçimle ikincisi $\\int u^4\\,du=\\dfrac{\\sin^5 x}{5}+C$ olur."),
            "Birinci integral $\\dfrac{1}{2}\\sin 2x$ in integrali olarak da hesaplanabilir ve $-\\dfrac{\\cos 2x}{4}+C$ bulunur. İki sonuç farklı görünür ama yalnızca sabitleri farklıdır; çünkü $\\dfrac{\\sin^2 x}{2}=\\dfrac{1-\\cos 2x}{4}$ tir.",
        ]},
        {"baslik": "Kosinüsün kuvveti", "icerik": [
            "Kosinüsün kuvveti ile sinüsün çarpımında $u=\\cos x$ seçilir. Bu kez $du=-\\sin x\\,dx$ olduğu için integralin önüne bir eksi işareti gelir.",
            ornek(
                "$\\int \\cos^3 x\\sin x\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=\\cos x$ için $\\sin x\\,dx=-du$ olur ve integral $-\\int u^3\\,du=-\\dfrac{u^4}{4}$ olur.",
                "Sonuç $-\\dfrac{\\cos^4 x}{4}+C$ dir."),
        ]},
        {"baslik": "Tanjantın integrali", "icerik": [
            "Tanjant, sinüsün kosinüse bölümüdür ve paydaki sinüs, paydadaki kosinüsün türevinin eksisidir; bu gözlem tanjantın integralini tek adımda verir. Bu yüzden payda $u$ seçilince integral logaritmaya dönüşür.",
            ornek(
                "$\\int \\tan x\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$\\tan x=\\dfrac{\\sin x}{\\cos x}$ ve $u=\\cos x$ için $du=-\\sin x\\,dx$ olur.",
                "İntegral $-\\int \\dfrac{du}{u}=-\\ln|\\cos x|+C$ olur."),
        ]},
        {"baslik": "Açının içinde ifade", "icerik": [
            "Trigonometrik fonksiyonun içinde $x^2$ gibi bir ifade bulunuyorsa ve bu ifadenin türevi çarpan olarak varsa, açı $u$ seçilir. Böylece fonksiyon temel tablodaki sinüs ya da kosinüs integraline döner.",
            ornek(
                "$\\int 2x\\cos(x^2)\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2$ için $du=2x\\,dx$ olur ve integral $\\int \\cos u\\,du$ ya dönüşür.",
                "Sonuç $\\sin(x^2)+C$ dir."),
        ]},
        {"baslik": "Doğrusal iç fonksiyon", "icerik": [
            "İç fonksiyon $ax+b$ biçimindeyse türevi sabit bir sayı olan $a$ dır ve integralde çarpan olarak bulunmasına gerek yoktur. Bu yüzden değişken değiştirme her zaman işler ve sonuç, dış fonksiyonun integralinin $a$ ya bölünmesidir.",
            ornek(
                "$\\int (3x-1)^4\\,dx$ ve $\\int \\cos(2x+1)\\,dx$ integralleri verilsin.",
                "İntegralleri hesaplayalım.",
                "Birincide $u=3x-1$ ve $dx=\\dfrac{du}{3}$ olur; sonuç $\\dfrac{(3x-1)^5}{15}+C$ dir.",
                "İkincide $u=2x+1$ ve $dx=\\dfrac{du}{2}$ olur; sonuç $\\dfrac{\\sin(2x+1)}{2}+C$ dir."),
        ]},
        {"baslik": "Belirli integralde sınırları dönüştürmek", "icerik": [
            "Belirli integralde değişken değiştirilirken sınırlar da yeni değişkene göre yazılır; her sınır $u$ nun tanımında yerine konarak yeni sınır bulunur. Böylece sonuç eski değişkene dönmeden, doğrudan yeni sınırlarla hesaplanır.",
            ornek(
                "$\\int_0^1 x e^{x^2}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x^2$ için $x=0$ da $u=0$, $x=1$ de $u=1$ olur; integral $\\dfrac{1}{2}\\int_0^1 e^u\\,du$ ya dönüşür.",
                "Sonuç $\\dfrac{e-1}{2}$ olur."),
            ornek(
                "$\\int_0^{\\pi/2}\\sin x\\cos x\\,dx$ integrali verilsin.",
                "Sınırları dönüştürerek hesaplayalım.",
                "$u=\\sin x$ için $x=0$ da $u=0$, $x=\\dfrac{\\pi}{2}$ de $u=1$ olur.",
                "İntegral $\\int_0^1 u\\,du=\\dfrac{1}{2}$ olur."),
            hap("Belirli integralde $u$ seçilince eski sınırlar $u$ nun tanımında yerine konur ve yeni sınırlar bulunur."),
        ]},
        {"baslik": "Değişken değiştirmeyle belirli integral", "icerik": [
            "Logaritma veren kalıplar belirli integralde de sık kullanılır. Sınırlar dönüştürüldükten sonra sonuç logaritmaların farkı olarak yazılır ve logaritma kurallarıyla sadeleştirilir.",
            ornek(
                "$\\int_0^2 \\dfrac{x}{x^2+1}\\,dx$ integrali verilsin.",
                "İntegrali hesaplayalım.",
                "$u=x^2+1$ için sınırlar $1$ ve $5$ olur; integral $\\dfrac{1}{2}\\int_1^5 \\dfrac{du}{u}$ ya dönüşür.",
                "Sonuç $\\dfrac{1}{2}(\\ln 5-\\ln 1)=\\dfrac{\\ln 5}{2}$ olur."),
        ]},
        {"baslik": "Sınırları dönüştürmemek", "icerik": [
            "Belirli integral için ikinci bir yol da vardır: belirsiz integral önce değişken değiştirilerek bulunur, eski değişkene geri dönülür ve eski sınırlar kullanılır. İki yol da aynı sonucu verir; önemli olan ikisini karıştırmamaktır.",
            dikkat(
                "Değişken değiştirip eski sınırları yeni değişkenle kullanmak.",
                "$\\int_0^1 x e^{x^2}\\,dx$ integralinde $u=x^2$ yazıldıktan sonra sınırlar $0$ ve $1$ olarak kaldı; burada bu tesadüfen doğrudur. Ama örneğin $\\int_1^2 2x(x^2+1)^3\\,dx$ te yeni sınırlar $2$ ve $5$ tir; eski sınırlar kullanılırsa sonuç yanlış çıkar."),
            "Bu integralin doğru değeri $\\int_2^5 u^3\\,du=\\dfrac{625-16}{4}=\\dfrac{609}{4}$ dur.",
        ]},
        {"baslik": "Eski değişkeni yeni değişkenle yazmak", "icerik": [
            "Bazen $u$ seçildikten sonra integralde hâlâ $x$ kalır. Bu durumda $x$, $u$ cinsinden yazılır ve integral tamamen yeni değişkene çevrilir. Yöntem özellikle kök içinde doğrusal bir ifade bulunduğunda işe yarar.",
            ornek(
                "$\\int_1^2 x\\sqrt{x-1}\\,dx$ integrali verilsin.",
                "Değişken değiştirerek hesaplayalım.",
                "$u=x-1$ için $x=u+1$ ve $du=dx$ olur; sınırlar $0$ ve $1$ dir. İntegral $\\int_0^1 (u+1)u^{1/2}\\,du=\\int_0^1 (u^{3/2}+u^{1/2})\\,du$ olur.",
                "$\\dfrac{2}{5}+\\dfrac{2}{3}=\\dfrac{16}{15}$ bulunur."),
        ]},
        {"baslik": "Sonucu türevle denetlemek", "icerik": [
            "Değişken değiştirmenin sonucu her zaman türev alınarak denetlenebilir. Türev alınırken zincir kuralı iç fonksiyonun türevini geri getirir ve integrali alınan ifade yeniden ortaya çıkar.",
            ornek(
                "$\\int x\\sqrt{x^2+4}\\,dx=\\dfrac{(x^2+4)^{3/2}}{3}+C$ sonucu verilsin.",
                "Sonucu türevle denetleyelim.",
                "Türev $\\dfrac{1}{3} \\cdot \\dfrac{3}{2}(x^2+4)^{1/2} \\cdot 2x$ olur.",
                "Sadeleşince $x\\sqrt{x^2+4}$ kalır; sonuç doğrudur."),
        ]},
        {"baslik": "Yöntemin sınırları", "icerik": [
            "Değişken değiştirme her integrali çözmez. Yöntemin işlemesi için iç fonksiyonun türevinin, bir sabit çarpan dışında, integralde bulunması gerekir. Örneğin $\\int e^{x^2}\\,dx$ integralinde $x$ çarpanı olmadığı için $u=x^2$ seçimi sonuç vermez; bu integralin ters türevi temel fonksiyonlarla yazılamaz.",
            "Lise düzeyindeki sorular, yöntemin işleyeceği biçimde seçilir. Bir değişken değiştirme sonuç vermiyorsa önce başka bir $u$ denenir; hâlâ olmuyorsa açma, terimlere ayırma ya da özdeşlik gibi diğer yöntemlere dönülür.",
        ]},
        {"baslik": "Kalıpların özeti", "icerik": [
            tablo(["İntegral biçimi", "Sonuç"], [
                ["$\\int g^n g'\\,dx$", "$\\dfrac{g^{n+1}}{n+1}+C$"],
                ["$\\int \\dfrac{g'}{g}\\,dx$", "$\\ln|g|+C$"],
                ["$\\int e^{g} g'\\,dx$", "$e^{g}+C$"],
                ["$\\int \\cos(g) g'\\,dx$", "$\\sin(g)+C$"],
                ["$\\int \\sin(g) g'\\,dx$", "$-\\cos(g)+C$"],
                ["$\\int f(ax+b)\\,dx$", "$\\dfrac{F(ax+b)}{a}+C$"],
            ]),
            "Tablodaki her satır, temel bir integral kuralında $x$ yerine $g(x)$ yazılmış ve türevi $g'(x)$ çarpan olarak eklenmiş hâlidir. Bu tabloyu tanımak, çoğu soruda $u$ yazmadan doğrudan sonuca gitmeyi sağlar.",
        ]},
        {"baslik": "Sınavda değişken değiştirme", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) değişken değiştirme; kuvvet, kök, üstel, logaritmik ve trigonometrik integraller ve belirli integralde sınır dönüştürme biçiminde karşına çıkabilir.",
                "Sorular çoğu zaman tablodaki kalıplardan birine indirgenecek biçimde seçilir."),
            "Soruda bir iç fonksiyon ve yanında onun türevine benzeyen bir çarpan gördüğünde hemen değişken değiştirmeyi düşün. Belirli integralde sınırları dönüştürmeyi unutma ya da eski değişkene geri dönüp eski sınırları kullan.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$dx$ i $du$ ya çevirmemek", "$du=u'\\,dx$ yazılır"],
                ["Katsayıyı ayarlamayı unutmak", "Eksik sabit dışarıda düzeltilir"],
                ["Eksik $x$ çarpanını eklemek", "Değişken düzeltilemez"],
                ["Belirli integralde eski sınırları kullanmak", "Sınırlar dönüştürülür"],
                ["Sonuçta $u$ yu bırakmak", "Eski değişkene dönülür"],
                ["$\\int \\tan x\\,dx=\\ln|\\cos x|$", "$-\\ln|\\cos x|+C$"],
            ]),
            "Değişken değiştirmenin sonucu, tıpkı diğer integrallerde olduğu gibi, türev alınarak denetlenir. Türev alınırken zincir kuralı iç fonksiyonun türevini geri getirmelidir.",
        ]},
    ],
    "sss": [
        ("Değişken değiştirme yöntemi nedir?",
         "İntegraldeki bir iç fonksiyona yeni bir değişken adı verilerek integralin basit bir biçime dönüştürülmesidir. Zincir kuralının tersidir."),
        ("u nasıl seçilir?",
         "Türevi integralde çarpan olarak bulunan iç ifade seçilir. Bu ifade genellikle bir parantezin, kökün, paydanın ya da üssün içindedir."),
        ("Katsayı eksikse ne yapılır?",
         "Eksik olan sabit bir sayıysa integralin dışında düzeltilir. Eksik olan bir değişkense bu değişken değiştirme işe yaramaz."),
        ("Belirli integralde değişken değiştirilirken sınırlar ne olur?",
         "Sınırlar yeni değişkene göre yeniden yazılır. İstenirse eski değişkene dönülüp eski sınırlar da kullanılabilir."),
        ("tan x in integrali nedir?",
         "Eksi ln mutlak cos x artı C dir. Payda cos x seçilerek değişken değiştirmeyle bulunur."),
        ("ln x bölü x in integrali nedir?",
         "u eşittir ln x seçilir ve sonuç ln x in karesi bölü 2 artı C olur."),
        ("Değişken değiştirmenin sonucu nasıl denetlenir?",
         "Sonucun türevi zincir kuralıyla alınır. Türev, integrali alınan fonksiyona eşitse sonuç doğrudur."),
        ("Her integral değişken değiştirmeyle çözülür mü?",
         "Hayır. İç fonksiyonun türevi, bir sabit çarpan dışında, integralde bulunmuyorsa yöntem işe yaramaz. O zaman başka yöntemler denenir."),
    ],
    "kontrol": [
        "Değişken değiştirmenin zincir kuralının tersi olduğunu açıklayabiliyorum.",
        "Yöntemin beş adımını uygulayabiliyorum.",
        "Doğru yeni değişkeni seçebiliyorum.",
        "Eksik sabit katsayıyı ayarlayabiliyorum.",
        "Kök ve kesir içeren integralleri çözebiliyorum.",
        "Üstel ve logaritmik integralleri değişken değiştirmeyle hesaplayabiliyorum.",
        "Trigonometrik çarpımların ve tanjantın integralini bulabiliyorum.",
        "Doğrusal iç fonksiyonlu integralleri hızla hesaplayabiliyorum.",
        "Belirli integralde sınırları dönüştürebiliyorum.",
        "Eski değişkeni yeni değişkenle yazarak integral alabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["belirsiz-integral", "belirli-integral", "zincir-kurali"],
}
