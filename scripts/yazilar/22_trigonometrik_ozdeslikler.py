# scripts/yazilar/22_trigonometrik_ozdeslikler.py — Trigonometrik Ozdeslikler (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "trigonometrik-ozdeslikler-formuller",
    "baslik": "Trigonometrik Özdeşlikler ve Formüller",
    "aciklama": "Trigonometrik özdeşlikler nelerdir? Temel özdeşlik, toplam ve fark, iki kat ve yarım açı, dönüşüm formülleri, sadeleştirme, ispat ve denklem çözme; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "trigonometrik-ozdeslikler-formuller",
    "kapak_alt": "Trigonometrik özdeşlikler: aynı kareyi farklı parçalarla dolduran renkli yapboz parçalarını karşılaştıran öğrenci",
    "ozet": "Trigonometrik özdeşlikler, farklı görünen iki ifadenin aslında aynı değeri verdiğini söyleyen eşitliklerdir. Sadeleştirmenin, değer hesaplamanın ve trigonometrik denklem çözmenin araçları bu formüllerdir. Bu yazıda temel özdeşliği ve ondan türeyenleri, bölüm özdeşliklerini, sadeleştirme ve ispat yöntemini, toplam ve fark formüllerini, iki kat ve yarım açı formüllerini, kuvvet azaltmayı, toplamdan çarpıma ve çarpımdan toplama dönüşüm formüllerini ve özdeşliklerin denklem çözmede kullanımını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Özdeşlik nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için trigonometrik oranları, özel açıları ve birim çemberi biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/trigonometrik-oranlar/\">Trigonometrik Oranlar: Sinüs, Kosinüs, Tanjant ve Kotanjant</a> ve <a href=\"/blog/birim-cember/\">Birim Çember Konu Anlatımı</a> yazılarına göz at."),
            "Tanımlı olduğu her değer için doğru olan eşitliklere <strong>özdeşlik</strong> denir. Bir denklem yalnızca belirli değerlerde sağlanırken, bir özdeşlik değişken ne olursa olsun sağlanır. $\\sin x=\\dfrac{1}{2}$ bir denklemdir; $\\sin^2 x+\\cos^2 x=1$ ise bir özdeşliktir.",
            "Kapaktaki yapboz bu fikri görselleştiriyor: aynı kare iki farklı biçimde parçalara ayrılmış, ama iki durumda da toplam alan aynı. Trigonometrik özdeşlikler de aynı değeri farklı parçalarla ifade eder ve bir sorunun hangi biçimde daha kolay çözüleceğini seçmeyi sağlar.",
            hap("Özdeşlik, tanımlı olduğu her değer için doğrudur.",
                "Denklem ise yalnızca belirli değerlerde sağlanır."),
        ]},
        {"baslik": "Temel özdeşlik", "icerik": [
            "Birim çemberdeki nokta $(\\cos x, \\sin x)$ ve çemberin denklemi $x^2+y^2=1$ olduğu için her açı için şu eşitlik doğrudur:",
            "$$\\sin^2 x+\\cos^2 x=1$$",
            "Bu özdeşlikten iki sık kullanılan biçim elde edilir: $\\sin^2 x=1-\\cos^2 x$ ve $\\cos^2 x=1-\\sin^2 x$. İfadede $1$ ile bir karenin farkı görüldüğünde bu biçimlerin kullanılabileceği düşünülmelidir.",
            ornek(
                "$\\dfrac{1-\\sin^2 x}{\\cos x}$ ifadesi verilsin, $\\cos x \\neq 0$.",
                "İfadeyi sadeleştirelim.",
                "Pay $\\cos^2 x$ olarak yazılır.",
                "$\\dfrac{\\cos^2 x}{\\cos x}=\\cos x$."),
        ]},
        {"baslik": "Temel özdeşlikten türeyenler", "icerik": [
            "Temel özdeşliğin iki tarafı $\\cos^2 x$ e bölünürse tanjantla, $\\sin^2 x$ e bölünürse kotanjantla ilgili iki yeni özdeşlik elde edilir. Bölme yapılırken bölünen ifadenin sıfır olmadığı varsayılır.",
            tablo(["Özdeşlik", "Nereden gelir"], [
                ["$1+\\tan^2 x=\\sec^2 x$", "İki taraf $\\cos^2 x$ e bölünür"],
                ["$1+\\cot^2 x=\\csc^2 x$", "İki taraf $\\sin^2 x$ e bölünür"],
            ]),
            ornek(
                "$\\tan x=2$ olduğu biliniyor ve $x$ dar açı.",
                "$\\cos^2 x$ değerini bulalım.",
                "$1+\\tan^2 x=5=\\dfrac{1}{\\cos^2 x}$.",
                "$\\cos^2 x=\\dfrac{1}{5}$."),
        ]},
        {"baslik": "Bölüm özdeşlikleri", "icerik": [
            "Tanjant ve kotanjant, sinüs ve kosinüsün bölümü olarak yazılır. Bu özdeşlikler, farklı oranlar içeren ifadeleri tek bir oran türüne çevirmenin en kısa yoludur.",
            tablo(["Özdeşlik", "Koşul"], [
                ["$\\tan x=\\dfrac{\\sin x}{\\cos x}$", "$\\cos x \\neq 0$"],
                ["$\\cot x=\\dfrac{\\cos x}{\\sin x}$", "$\\sin x \\neq 0$"],
                ["$\\tan x \\cdot \\cot x=1$", "İkisi de tanımlıysa"],
            ]),
            "Bir ifadede hem tanjant hem sinüs ve kosinüs varsa hepsini sinüs ve kosinüs cinsinden yazmak çoğu zaman sadeleştirmenin ilk adımıdır.",
        ]},
        {"baslik": "Sadeleştirme", "icerik": [
            "Trigonometrik ifadeleri sadeleştirirken üç araç birlikte kullanılır: temel özdeşlik, bölüm özdeşlikleri ve cebirsel özdeşlikler. Tam kare açılımı ve iki kare farkı özellikle sık işe yarar.",
            ornek(
                "$(\\sin x+\\cos x)^2$ ifadesi verilsin.",
                "İfadeyi açıp sadeleştirelim.",
                "$(\\sin x+\\cos x)^2=\\sin^2 x+2\\sin x \\cos x+\\cos^2 x$.",
                "Temel özdeşlikle: $1+2\\sin x \\cos x$."),
            ornek(
                "$\\dfrac{\\sin^4 x-\\cos^4 x}{\\sin^2 x-\\cos^2 x}$ ifadesi verilsin.",
                "İfadeyi sadeleştirelim.",
                "Pay iki kare farkıdır: $(\\sin^2 x-\\cos^2 x)(\\sin^2 x+\\cos^2 x)$.",
                "Sadeleşince $\\sin^2 x+\\cos^2 x=1$ kalır."),
        ]},
        {"baslik": "Toplam verilince çarpımı bulmak", "icerik": [
            "Sık sorulan bir soru tipinde $\\sin x+\\cos x$ toplamı verilir ve $\\sin x \\cos x$ çarpımı istenir. Toplamın karesi alınınca içinden temel özdeşlik ve çarpımın iki katı çıkar; böylece açının kendisini bulmadan çarpıma ulaşılır.",
            ornek(
                "$\\sin x+\\cos x=\\dfrac{7}{5}$ olduğu biliniyor.",
                "$\\sin x \\cos x$ ve $\\sin 2x$ değerlerini bulalım.",
                "Kare alınır: $1+2\\sin x \\cos x=\\dfrac{49}{25}$, yani $2\\sin x \\cos x=\\dfrac{24}{25}$.",
                "$\\sin x \\cos x=\\dfrac{12}{25}$ ve $\\sin 2x=\\dfrac{24}{25}$ olur."),
            "Aynı yol fark için de işler: $(\\sin x-\\cos x)^2=1-2\\sin x \\cos x$ olduğundan toplamın karesi ile farkın karesinin toplamı her zaman $2$ dir.",
        ]},
        {"baslik": "Tümler açılarla sadeleştirme", "icerik": [
            "Toplamı $90^\\circ$ olan iki açıdan birinin sinüsü diğerinin kosinüsüne eşittir. Bu kural, özel olmayan açıların karelerini içeren ifadeleri temel özdeşliğe çevirir ve hesap makinesi gerektirecek gibi görünen soruları birkaç satırda bitirir.",
            ornek(
                "$\\sin^2 20^\\circ+\\sin^2 70^\\circ$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "$70^\\circ$ ile $20^\\circ$ tümlerdir: $\\sin 70^\\circ=\\cos 20^\\circ$.",
                "İfade $\\sin^2 20^\\circ+\\cos^2 20^\\circ$ olur ve değeri $1$ dir."),
        ]},
        {"baslik": "Özdeşlik ispatı", "icerik": [
            "Bir özdeşliği ispatlamak için genellikle daha karmaşık görünen taraftan başlanır ve adım adım diğer tarafa ulaşılır. İki tarafı birden değiştirmek yerine tek taraf üzerinde çalışmak, ispatın doğruluğunu güvenceye alır.",
            ornek(
                "$\\tan x+\\cot x=\\dfrac{1}{\\sin x \\cos x}$ eşitliği verilsin.",
                "Eşitliğin özdeşlik olduğunu gösterelim.",
                "Sol taraf sinüs ve kosinüsle yazılır: $\\dfrac{\\sin x}{\\cos x}+\\dfrac{\\cos x}{\\sin x}=\\dfrac{\\sin^2 x+\\cos^2 x}{\\sin x \\cos x}$.",
                "Pay $1$ dir; sonuç sağ tarafa eşittir."),
            dikkat(
                "Özdeşliği ispatlarken sonucu baştan doğru kabul etmek.",
                "İspat, iki tarafın eşit olduğunu göstermelidir. Eşitliği baştan doğru sayıp iki tarafa işlem yapmak ve doğru bir eşitliğe varmak, başlangıçtaki eşitliğin doğru olduğunu kanıtlamaz."),
        ]},
        {"baslik": "Toplam formülleri", "icerik": [
            "İki açının toplamının trigonometrik değerleri, açıların kendi değerlerinden hesaplanır. Bu formüller, özel olmayan birçok açının değerini özel açılardan bulmayı sağlar:",
            tablo(["Formül", ""], [
                ["$\\sin(a+b)$", "$\\sin a \\cos b+\\cos a \\sin b$"],
                ["$\\cos(a+b)$", "$\\cos a \\cos b-\\sin a \\sin b$"],
                ["$\\tan(a+b)$", "$\\dfrac{\\tan a+\\tan b}{1-\\tan a \\tan b}$"],
            ]),
            ornek(
                "$\\sin 75^\\circ$ değeri istensin.",
                "Toplam formülüyle bulalım.",
                "$75^\\circ=45^\\circ+30^\\circ$: $\\sin 75^\\circ=\\sin 45^\\circ \\cos 30^\\circ+\\cos 45^\\circ \\sin 30^\\circ$.",
                "$\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2}+\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{1}{2}=\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$."),
        ]},
        {"baslik": "Tanjant toplam formülüyle açı bulmak", "icerik": [
            "Tanjant toplam formülü yalnızca değer hesaplamak için değil, iki açının toplamını bulmak için de kullanılır. İki dar açının tanjantları biliniyorsa toplamlarının tanjantı hesaplanır, sonra hangi açıya karşılık geldiğine bakılır.",
            ornek(
                "$a$ ve $b$ dar açılar, $\\tan a=2$ ve $\\tan b=3$ olsun.",
                "$a+b$ toplamını bulalım.",
                "$\\tan(a+b)=\\dfrac{2+3}{1-2 \\cdot 3}=\\dfrac{5}{-5}=-1$.",
                "İki dar açının toplamı $0^\\circ$ ile $180^\\circ$ arasındadır; tanjantı $-1$ olan açı $135^\\circ$ dir."),
            "Tanjant değeri tek başına açıyı belirlemez; aynı tanjant değeri $180^\\circ$ arayla tekrar eder. Bu yüzden açının hangi aralıkta olduğu mutlaka ayrıca kontrol edilmelidir.",
        ]},
        {"baslik": "Fark formülleri", "icerik": [
            "Fark formülleri, toplam formüllerinde $b$ yerine $-b$ yazılarak elde edilir. Kosinüs çift, sinüs tek olduğu için yalnızca işaretler değişir:",
            tablo(["Formül", ""], [
                ["$\\sin(a-b)$", "$\\sin a \\cos b-\\cos a \\sin b$"],
                ["$\\cos(a-b)$", "$\\cos a \\cos b+\\sin a \\sin b$"],
                ["$\\tan(a-b)$", "$\\dfrac{\\tan a-\\tan b}{1+\\tan a \\tan b}$"],
            ]),
            ornek(
                "$\\cos 15^\\circ$ ve $\\tan 15^\\circ$ değerleri istensin.",
                "Fark formülleriyle bulalım.",
                "$\\cos 15^\\circ=\\cos(45^\\circ-30^\\circ)=\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2}+\\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{1}{2}=\\dfrac{\\sqrt{6}+\\sqrt{2}}{4}$.",
                "$\\tan 15^\\circ=\\dfrac{1-\\dfrac{\\sqrt{3}}{3}}{1+\\dfrac{\\sqrt{3}}{3}}=2-\\sqrt{3}$."),
            "$\\cos 15^\\circ$ ile $\\sin 75^\\circ$ nin aynı çıkması tesadüf değildir: iki açı tümlerdir ve bir açının kosinüsü tümlerinin sinüsüne eşittir.",
        ]},
        {"baslik": "Açılar toplanmaz", "icerik": [
            "Trigonometrik fonksiyonlar toplamaya dağılmaz. $\\sin(a+b)$ ifadesi $\\sin a+\\sin b$ ye eşit değildir; toplam formülü bu yüzden gereklidir.",
            ornek(
                "$a=30^\\circ$ ve $b=60^\\circ$ verilsin.",
                "$\\sin(a+b)$ ile $\\sin a+\\sin b$ yi karşılaştıralım.",
                "$\\sin 90^\\circ=1$.",
                "$\\sin 30^\\circ+\\sin 60^\\circ=\\dfrac{1}{2}+\\dfrac{\\sqrt{3}}{2}=\\dfrac{1+\\sqrt{3}}{2}$, yaklaşık $1.37$. İki değer farklıdır."),
        ]},
        {"baslik": "İki kat açı formülleri", "icerik": [
            "Toplam formüllerinde $a=b=x$ yazılınca iki kat açı formülleri elde edilir. Kosinüsün iki kat açı formülünün üç biçimi vardır ve temel özdeşlikle birbirine dönüşür:",
            tablo(["Formül", ""], [
                ["$\\sin 2x$", "$2\\sin x \\cos x$"],
                ["$\\cos 2x$", "$\\cos^2 x-\\sin^2 x$"],
                ["$\\cos 2x$", "$2\\cos^2 x-1$"],
                ["$\\cos 2x$", "$1-2\\sin^2 x$"],
                ["$\\tan 2x$", "$\\dfrac{2\\tan x}{1-\\tan^2 x}$"],
            ]),
            ornek(
                "$x$ dar açı ve $\\sin x=\\dfrac{3}{5}$ olsun.",
                "$\\sin 2x$, $\\cos 2x$ ve $\\tan 2x$ değerlerini bulalım.",
                "$\\cos x=\\dfrac{4}{5}$. $\\sin 2x=2 \\cdot \\dfrac{3}{5} \\cdot \\dfrac{4}{5}=\\dfrac{24}{25}$.",
                "$\\cos 2x=\\dfrac{16}{25}-\\dfrac{9}{25}=\\dfrac{7}{25}$ ve $\\tan 2x=\\dfrac{24}{7}$."),
        ]},
        {"baslik": "Bölgesi verilen açıda iki kat", "icerik": [
            "Açı ikinci bölgedeyse kosinüs negatif, sinüs pozitiftir. İki kat açı formülleri uygulanırken bu işaretler sonucu doğrudan etkiler; önce eksik oran temel özdeşlikle bulunur, işareti bölgeden seçilir, sonra formül uygulanır.",
            ornek(
                "$x$ ikinci bölgede ve $\\cos x=-\\dfrac{3}{5}$ olsun.",
                "$\\sin 2x$ ve $\\cos 2x$ değerlerini bulalım.",
                "$\\sin x=\\dfrac{4}{5}$ tür. $\\sin 2x=2 \\cdot \\dfrac{4}{5} \\cdot \\left(-\\dfrac{3}{5}\\right)=-\\dfrac{24}{25}$.",
                "$\\cos 2x=\\dfrac{9}{25}-\\dfrac{16}{25}=-\\dfrac{7}{25}$ olur."),
        ]},
        {"baslik": "Kısa hesap kalıpları", "icerik": [
            "İki kat açı formülleri tersten okunursa bazı çarpımlar ve farklar tek bir değere dönüşür. $\\sin x \\cos x$ çarpımı $\\sin 2x$ in yarısıdır; $\\cos^2 x-\\sin^2 x$ farkı ise doğrudan $\\cos 2x$ tir.",
            ornek(
                "$\\sin 15^\\circ \\cos 15^\\circ$ ve $\\cos^2 15^\\circ-\\sin^2 15^\\circ$ ifadeleri verilsin.",
                "İki ifadenin değerini bulalım.",
                "$\\sin 15^\\circ \\cos 15^\\circ=\\dfrac{\\sin 30^\\circ}{2}=\\dfrac{1}{4}$.",
                "$\\cos^2 15^\\circ-\\sin^2 15^\\circ=\\cos 30^\\circ=\\dfrac{\\sqrt{3}}{2}$ olur."),
        ]},
        {"baslik": "Kuvvet azaltma", "icerik": [
            "Kosinüsün iki kat açı formülü kare terimler için çözülünce kuvvet azaltma formülleri elde edilir. Bu formüller kareli ifadeleri birinci kuvvete indirir ve özellikle integral konusunda çok kullanılır:",
            tablo(["Formül", ""], [
                ["$\\cos^2 x$", "$\\dfrac{1+\\cos 2x}{2}$"],
                ["$\\sin^2 x$", "$\\dfrac{1-\\cos 2x}{2}$"],
            ]),
            ornek(
                "$\\cos^2 15^\\circ$ değeri istensin.",
                "Kuvvet azaltma formülüyle bulalım.",
                "$\\cos^2 15^\\circ=\\dfrac{1+\\cos 30^\\circ}{2}=\\dfrac{1+\\dfrac{\\sqrt{3}}{2}}{2}$.",
                "Sonuç $\\dfrac{2+\\sqrt{3}}{4}$ tür."),
        ]},
        {"baslik": "Yarım açı formülleri", "icerik": [
            "Kuvvet azaltma formüllerinde $x$ yerine $\\dfrac{x}{2}$ yazılıp karekök alınınca yarım açı formülleri elde edilir. Karekökün işareti, yarım açının bulunduğu bölgeye göre seçilir:",
            "$$\\sin \\dfrac{x}{2}=\\pm\\sqrt{\\dfrac{1-\\cos x}{2}}$$",
            "$$\\cos \\dfrac{x}{2}=\\pm\\sqrt{\\dfrac{1+\\cos x}{2}}$$",
            ornek(
                "$\\sin 15^\\circ$ değeri istensin.",
                "Yarım açı formülüyle bulalım.",
                "$15^\\circ$ birinci bölgededir, işaret pozitiftir: $\\sin 15^\\circ=\\sqrt{\\dfrac{1-\\cos 30^\\circ}{2}}$.",
                "$\\sqrt{\\dfrac{2-\\sqrt{3}}{4}}=\\dfrac{\\sqrt{2-\\sqrt{3}}}{2}$, yaklaşık $0.2588$."),
        ]},
        {"baslik": "Üç kat açı", "icerik": [
            "Toplam ve iki kat açı formülleri birleştirilerek üç kat açı formülleri de elde edilir. $\\sin 3x=\\sin(2x+x)$ yazılıp açılırsa sonuç yalnızca $\\sin x$ cinsinden yazılabilir:",
            "$$\\sin 3x=3\\sin x-4\\sin^3 x$$",
            ornek(
                "$x=30^\\circ$ için formülü kontrol edelim.",
                "İki tarafı ayrı ayrı hesaplayalım.",
                "Sol taraf: $\\sin 90^\\circ=1$.",
                "Sağ taraf: $3 \\cdot \\dfrac{1}{2}-4 \\cdot \\dfrac{1}{8}=\\dfrac{3}{2}-\\dfrac{1}{2}=1$. İki taraf eşittir."),
        ]},
        {"baslik": "Toplamdan çarpıma dönüşüm", "icerik": [
            "İki sinüsün ya da iki kosinüsün toplamı ve farkı bir çarpım olarak yazılabilir. Bu dönüşümler, toplam biçimindeki ifadeleri çarpanlarına ayırarak denklem çözmeyi ve sadeleştirmeyi kolaylaştırır:",
            tablo(["Toplam", "Çarpım"], [
                ["$\\sin a+\\sin b$", "$2\\sin \\dfrac{a+b}{2} \\cos \\dfrac{a-b}{2}$"],
                ["$\\sin a-\\sin b$", "$2\\cos \\dfrac{a+b}{2} \\sin \\dfrac{a-b}{2}$"],
                ["$\\cos a+\\cos b$", "$2\\cos \\dfrac{a+b}{2} \\cos \\dfrac{a-b}{2}$"],
                ["$\\cos a-\\cos b$", "$-2\\sin \\dfrac{a+b}{2} \\sin \\dfrac{a-b}{2}$"],
            ]),
            ornek(
                "$\\sin 75^\\circ+\\sin 15^\\circ$ ifadesi verilsin.",
                "Dönüşüm formülüyle hesaplayalım.",
                "$2\\sin 45^\\circ \\cos 30^\\circ=2 \\cdot \\dfrac{\\sqrt{2}}{2} \\cdot \\dfrac{\\sqrt{3}}{2}$.",
                "Sonuç $\\dfrac{\\sqrt{6}}{2}$ dır."),
        ]},
        {"baslik": "Çarpımdan toplama dönüşüm", "icerik": [
            "Tersine, iki trigonometrik değerin çarpımı toplam olarak yazılabilir. Bu formüller toplam ve fark formüllerinin taraf tarafa toplanmasıyla elde edilir:",
            tablo(["Çarpım", "Toplam"], [
                ["$2\\sin a \\cos b$", "$\\sin(a+b)+\\sin(a-b)$"],
                ["$2\\cos a \\cos b$", "$\\cos(a+b)+\\cos(a-b)$"],
                ["$2\\sin a \\sin b$", "$\\cos(a-b)-\\cos(a+b)$"],
            ]),
            ornek(
                "$2\\sin 75^\\circ \\cos 15^\\circ$ ifadesi verilsin.",
                "Çarpımı toplama çevirerek hesaplayalım.",
                "$\\sin 90^\\circ+\\sin 60^\\circ$.",
                "Sonuç $1+\\dfrac{\\sqrt{3}}{2}$ olur."),
        ]},
        {"baslik": "Denklem çözmede özdeşlik", "icerik": [
            "Trigonometrik denklemlerde farklı açılar ya da farklı oranlar varsa önce özdeşliklerle tek bir açıya ve tek bir orana indirgenir. Sonra denklem çarpanlarına ayrılır ve her çarpan ayrı ayrı çözülür.",
            ornek(
                "$[0^\\circ, 360^\\circ)$ aralığında $\\sin 2x=\\sin x$ denklemi verilsin.",
                "Denklemi çözelim.",
                "İki kat açı formülüyle: $2\\sin x \\cos x-\\sin x=0$, yani $\\sin x(2\\cos x-1)=0$.",
                "$\\sin x=0$ için $x=0^\\circ$ ya da $180^\\circ$; $\\cos x=\\dfrac{1}{2}$ için $x=60^\\circ$ ya da $300^\\circ$."),
            dikkat(
                "Denklemin iki tarafını $\\sin x$ e bölmek.",
                "$\\sin x$ e bölünseydi $2\\cos x=1$ kalır ve $\\sin x=0$ yapan $0^\\circ$ ile $180^\\circ$ çözümleri kaybolurdu. Bilinmeyen içeren bir ifadeye bölmek yerine ortak çarpan paranteze alınmalıdır."),
        ]},
        {"baslik": "İki kat açıyla denklem", "icerik": [
            "Denklemde $\\cos 2x$ ile $\\cos x$ birlikte görünüyorsa $\\cos 2x$ için $2\\cos^2 x-1$ biçimi seçilir. Böylece denklem $\\cos x$ e göre ikinci dereceden bir denkleme dönüşür ve çarpanlara ayırarak çözülür.",
            ornek(
                "$[0^\\circ, 360^\\circ)$ aralığında $\\cos 2x=\\cos x$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$2\\cos^2 x-\\cos x-1=0$, yani $(2\\cos x+1)(\\cos x-1)=0$.",
                "$\\cos x=1$ için $x=0^\\circ$; $\\cos x=-\\dfrac{1}{2}$ için $x=120^\\circ$ ya da $240^\\circ$."),
        ]},
        {"baslik": "En büyük ve en küçük değer", "icerik": [
            "$a\\sin x+b\\cos x$ biçimindeki bir ifade, toplam formülü sayesinde tek bir sinüs olarak yazılabilir. Sonuçta ifadenin alabileceği en büyük değer $\\sqrt{a^2+b^2}$, en küçük değer ise bunun negatifidir.",
            ornek(
                "$3\\sin x+4\\cos x$ ifadesi verilsin.",
                "İfadenin alabileceği en büyük ve en küçük değeri bulalım.",
                "$\\sqrt{3^2+4^2}=\\sqrt{25}=5$.",
                "İfade $[-5, 5]$ aralığında değer alır."),
            "Aynı fikirle $\\sin x \\cos x=\\dfrac{\\sin 2x}{2}$ çarpımının en büyük değerinin $\\dfrac{1}{2}$ olduğu da hemen görülür.",
        ]},
        {"baslik": "Formüllerin özeti", "icerik": [
            "En sık kullanılan formüller aşağıdaki tabloda bir araya getirilmiştir. Hepsi temel özdeşlik ile toplam formüllerinden türetilebilir; bu yüzden türetme yolunu bilmek, tabloyu ezberlemekten daha güvenilirdir.",
            tablo(["Konu", "Formül"], [
                ["Temel", "$\\sin^2 x+\\cos^2 x=1$"],
                ["Toplam", "$\\sin(a+b)=\\sin a \\cos b+\\cos a \\sin b$"],
                ["Toplam", "$\\cos(a+b)=\\cos a \\cos b-\\sin a \\sin b$"],
                ["İki kat", "$\\sin 2x=2\\sin x \\cos x$"],
                ["İki kat", "$\\cos 2x=2\\cos^2 x-1$"],
                ["Kuvvet azaltma", "$\\sin^2 x=\\dfrac{1-\\cos 2x}{2}$"],
            ]),
        ]},
        {"baslik": "Sınavda özdeşlikler", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) özdeşlikler; sadeleştirme, toplam ve fark formülleriyle değer hesaplama, iki kat açı formülleri ve denklem çözme biçiminde karşına çıkabilir.",
                "Dönüşüm formülleri ve yarım açı formülleri de özellikle değer hesaplama sorularında kullanılabilir."),
            "Özdeşlik sorularında önce ifadede hangi açıların ve hangi oranların bulunduğuna bak. Açılar farklıysa toplam ya da iki kat açı formülleriyle tek açıya, oranlar farklıysa bölüm özdeşlikleriyle sinüs ve kosinüse indir. Çoğu soru bu iki adımdan sonra temel özdeşlikle biter.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\sin(a+b)=\\sin a+\\sin b$", "Toplam formülü kullanılır"],
                ["$\\sin 2x=2\\sin x$", "$\\sin 2x=2\\sin x \\cos x$"],
                ["$\\cos(a+b)$ de artı işareti kullanmak", "Kosinüs toplamında eksi vardır"],
                ["Yarım açıda işareti bölgeye göre seçmemek", "İşaret yarım açının bölgesinden"],
                ["Denklemde $\\sin x$ e bölmek", "Ortak çarpan alınır"],
                ["$\\cos 2x$ in yalnız bir biçimini bilmek", "Üç biçim de kullanılabilir"],
            ]),
            "Bu hataların çoğu formülleri ezberleyip nereden geldiğini bilmemekten doğar. Şüpheye düşüldüğünde formülü özel bir açıyla, örneğin $x=30^\\circ$ ile denemek, doğru hatırlanıp hatırlanmadığını hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Trigonometrik özdeşlik nedir?",
         "Tanımlı olduğu her açı için doğru olan trigonometrik eşitliktir. Sinüs kare artı kosinüs kare eşittir 1 en temel özdeşliktir."),
        ("Sinüs toplam formülü nedir?",
         "sin(a + b), sin a çarpı cos b artı cos a çarpı sin b ye eşittir."),
        ("İki kat açı formülü nedir?",
         "sin 2x eşittir 2 sin x cos x tir. cos 2x ise cos kare x eksi sin kare x, 2 cos kare x eksi 1 ya da 1 eksi 2 sin kare x biçiminde yazılabilir."),
        ("Kuvvet azaltma formülü ne işe yarar?",
         "Sinüs ya da kosinüsün karesini iki kat açının kosinüsü cinsinden, yani birinci kuvvetten bir ifadeyle yazar. İntegral hesaplarında çok kullanılır."),
        ("Özdeşlik nasıl ispatlanır?",
         "Genellikle karmaşık taraftan başlanır ve özdeşlikler adım adım uygulanarak diğer tarafa ulaşılır. İki tarafa birden işlem yapılmaz."),
        ("sin 75 derece nasıl hesaplanır?",
         "75 derece 45 ile 30 derecenin toplamı olarak yazılır ve toplam formülü uygulanır. Sonuç kök 6 artı kök 2 bölü 4 tür."),
        ("Tanjant toplam formülü nedir?",
         "tan(a + b), tan a artı tan b nin 1 eksi tan a çarpı tan b ye bölümüdür. Payda sıfır olursa toplam açının tanjantı tanımsızdır."),
        ("3 sin x artı 4 cos x ifadesinin en büyük değeri kaçtır?",
         "3 ün karesi ile 4 ün karesinin toplamının karekökü, yani 5 tir. En küçük değeri ise eksi 5 tir."),
    ],
    "kontrol": [
        "Özdeşlik ile denklem arasındaki farkı açıklayabiliyorum.",
        "Temel özdeşliği ve ondan türeyen özdeşlikleri kullanabiliyorum.",
        "Bölüm özdeşlikleriyle ifadeleri sinüs ve kosinüse çevirebiliyorum.",
        "Trigonometrik ifadeleri sadeleştirebiliyorum.",
        "Bir özdeşliği adım adım ispatlayabiliyorum.",
        "Toplam ve fark formülleriyle değer hesaplayabiliyorum.",
        "İki kat açı formüllerini kullanabiliyorum.",
        "Kuvvet azaltma ve yarım açı formüllerini uygulayabiliyorum.",
        "Toplamdan çarpıma ve çarpımdan toplama dönüşüm yapabiliyorum.",
        "Özdeşliklerle trigonometrik denklem çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["trigonometrik-oranlar", "birim-cember", "trigonometrik-fonksiyon-grafikleri"],
}
