# scripts/yazilar/38_turevin_tanimi.py — Turevin Tanimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "turevin-tanimi",
    "baslik": "Türevin Tanımı ve Türev Nasıl Bulunur?",
    "aciklama": "Türevin limitle tanımı nedir, türev nasıl bulunur? Tanımla türev alma, iki biçim, limitten türev tanıma, soldan ve sağdan türev, türevsiz noktalar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "analiz",
    "sinavlar": ["AYT"],
    "kapak": "turevin-tanimi",
    "kapak_alt": "Türevin tanımı: eğri üzerindeki iki temas noktasını birleştiren çubuğu tek noktadaki teğete yaklaştıran iki öğrenci",
    "ozet": "Türev, bir fonksiyonun bir noktadaki değişim hızını veren limittir. Bu limit, kesen doğrularının eğimlerinin teğet doğrusunun eğimine yaklaşmasını anlatır ve bütün türev kurallarının kaynağıdır. Bu yazıda türevin limitle tanımını ve iki eşdeğer biçimini, tanımla türev almanın adımlarını, sabit, doğrusal, kare, küp, ters ve karekök fonksiyonlarının türevlerinin tanımdan çıkarılmasını, sinüs ve üstel fonksiyonun türevini, verilen bir limitin türev olarak tanınmasını, soldan ve sağdan türevi, türevin olmadığı noktaları ve parçalı fonksiyonlarda türevlenebilirliği çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kesenden teğete", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için limit, belirsizlik ve eğim kavramlarını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/turev-konu-anlatimi/\">Türev Konu Anlatımı</a> ve <a href=\"/blog/limitte-belirsizlikler/\">Limitte Belirsizlikler Nasıl Çözülür?</a> yazılarına göz at."),
            "Bir eğri üzerinde $P$ ve $Q$ gibi iki nokta alınıp bunlardan geçen doğru çizilirse bir kesen elde edilir. $Q$ noktası eğri üzerinde $P$ ye doğru kaydırıldıkça kesen döner ve sonunda eğriye $P$ noktasında dokunan teğete yerleşir. Kesenin eğimi kolayca hesaplanır; teğetin eğimi ise bu eğimlerin limitidir.",
            "Kapaktaki öğrenciler eğri üzerindeki iki temas noktasını birleştiren bir çubuğu, noktalardan birini diğerine yaklaştırarak tek noktada dokunan bir teğete dönüştürüyor. Türevin tanımı bu hareketin matematiksel ifadesidir ve bütün türev kurallarının çıkış noktasıdır.",
        ]},
        {"baslik": "Türevin tanımı", "icerik": [
            "$P$ noktasının apsisi $a$, $Q$ noktasınınki $a+h$ olsun. Kesenin eğimi $\\dfrac{f(a+h)-f(a)}{h}$ dır. $h$ sıfıra yaklaşırken bu eğimin limiti varsa $f$, $a$ da türevlidir ve limit türevi verir:",
            "$$f'(a)=\\lim_{h \\to 0}\\dfrac{f(a+h)-f(a)}{h}$$",
            "Kesrin payı fonksiyondaki değişimi, paydası değişkendeki değişimi gösterir. $h$ pozitif de negatif de olabilir; yani $Q$ noktası $P$ ye sağdan da soldan da yaklaşabilir ve iki yönün sonucu aynı olmalıdır.",
            hap("Türev, kesen eğimlerinin limitidir.",
                "Limit yoksa fonksiyon o noktada türevli değildir."),
        ]},
        {"baslik": "İkinci biçim", "icerik": [
            "Aynı tanım, $x=a+h$ yazılarak farklı ama eşdeğer bir biçimde de ifade edilir. $h$ sıfıra giderken $x$ de $a$ ya gider:",
            "$$f'(a)=\\lim_{x \\to a}\\dfrac{f(x)-f(a)}{x-a}$$",
            "Bu biçim, özellikle bir noktadaki türevi hesaplarken çarpanlara ayırmayı kolaylaştırır. İki biçim aynı sonucu verir; hangisinin kullanılacağı sorudaki ifadenin görünüşüne bağlıdır.",
            hap("$f'(a)=\\lim_{x \\to a}\\dfrac{f(x)-f(a)}{x-a}$ biçimi de türevin tanımıdır."),
        ]},
        {"baslik": "Tanımla türev almanın adımları", "icerik": [
            "Türevi tanımla bulmak dört adımlık bir işlemdir. Adımların sırası her fonksiyon için aynıdır; değişen yalnızca ikinci adımdaki cebirsel sadeleştirmedir:",
            tablo(["Adım", "İşlem"], [
                ["1", "$f(x+h)$ yi yaz ve düzenle"],
                ["2", "$f(x+h)-f(x)$ farkını sadeleştir"],
                ["3", "Farkı $h$ ye böl, $h$ yi sadeleştir"],
                ["4", "$h$ sıfıra giderken limiti al"],
            ]),
            "Üçüncü adım belirsizliğin çözüldüğü adımdır. Pay içindeki bütün terimler $h$ çarpanı taşımalıdır; taşımıyorsa ikinci adımda bir hata yapılmıştır. Bu kontrol, hesabın doğru gidip gitmediğini dördüncü adıma geçmeden gösterir.",
        ]},
        {"baslik": "Sabit ve doğrusal fonksiyon", "icerik": [
            "En basit iki durum tanımın nasıl çalıştığını gösterir. Sabit fonksiyonda pay her zaman sıfırdır; doğrusal fonksiyonda ise pay $h$ ile orantılıdır.",
            ornek(
                "$f(x)=7$ ve $g(x)=3x+2$ fonksiyonları verilsin.",
                "Türevlerini tanımla bulalım.",
                "$\\dfrac{f(x+h)-f(x)}{h}=\\dfrac{7-7}{h}=0$ olduğundan $f'(x)=0$ dır.",
                "$\\dfrac{3(x+h)+2-(3x+2)}{h}=\\dfrac{3h}{h}=3$ olduğundan $g'(x)=3$ tür."),
            "Doğrusal fonksiyonun türevi eğimidir; bu, doğrunun her noktadaki teğetinin kendisi olmasından gelir. Sabit fonksiyon da eğimi sıfır olan bir doğrudur; iki sonuç aynı gözlemin iki yüzüdür.",
        ]},
        {"baslik": "Kare fonksiyonun türevi", "icerik": [
            "Kare fonksiyonda $(x+h)^2$ açılınca $x^2$ terimleri sadeleşir ve geriye yalnızca $h$ çarpanlı terimler kalır.",
            ornek(
                "$f(x)=x^2$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "$(x+h)^2-x^2=2xh+h^2$ olur; $h$ ye bölünce $2x+h$ kalır.",
                "$h$ sıfıra giderken limit $2x$ olur: $f'(x)=2x$."),
        ]},
        {"baslik": "Küp fonksiyonun türevi", "icerik": [
            "Küp fonksiyonda binom açılımı kullanılır: $(x+h)^3=x^3+3x^2h+3xh^2+h^3$. Birinci terim sadeleşir, diğerlerinin hepsi $h$ taşır.",
            ornek(
                "$f(x)=x^3$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "Fark $3x^2h+3xh^2+h^3$ olur; $h$ ye bölünce $3x^2+3xh+h^2$ kalır.",
                "$h$ sıfıra giderken limit $3x^2$ olur: $f'(x)=3x^2$."),
            "Aynı fikir her pozitif tam sayı üs için işler: $(x+h)^n$ açılımında $h$ ye bölündükten sonra yalnızca $nx^{n-1}$ terimi $h$ siz kalır. Kuvvet kuralının kaynağı budur.",
        ]},
        {"baslik": "Tanımla polinom türevi", "icerik": [
            "Birden fazla terimli polinomlarda da aynı adımlar izlenir. Her terimin farkı ayrı ayrı sadeleşir; sonuç, terimlerin türevlerinin toplamı olur ve bu da toplam kuralının tanımdan nasıl çıktığını gösterir.",
            ornek(
                "$f(x)=2x^2+3x$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "$f(x+h)-f(x)=2(2xh+h^2)+3h=4xh+2h^2+3h$ olur; $h$ ye bölünce $4x+2h+3$ kalır.",
                "$h$ sıfıra giderken limit $4x+3$ olur."),
        ]},
        {"baslik": "Ters fonksiyonun türevi", "icerik": [
            "$\\dfrac{1}{x}$ gibi kesirli fonksiyonlarda iki kesir önce ortak paydada birleştirilir. Pay sadeleşince $h$ çarpanı ortaya çıkar.",
            ornek(
                "$f(x)=\\dfrac{1}{x}$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "$\\dfrac{1}{x+h}-\\dfrac{1}{x}=\\dfrac{-h}{x(x+h)}$ olur; $h$ ye bölünce $\\dfrac{-1}{x(x+h)}$ kalır.",
                "$h$ sıfıra giderken limit $-\\dfrac{1}{x^2}$ olur."),
            "Sonuç kuvvet kuralıyla da uyumludur: $x^{-1}$ in türevi $-x^{-2}$ dir.",
        ]},
        {"baslik": "Karekök fonksiyonun türevi", "icerik": [
            "Karekök içeren farklarda eşlenikle çarpma kullanılır. Böylece kök farkı, köklerin toplamını paydada taşıyan bir kesre dönüşür.",
            ornek(
                "$f(x)=\\sqrt{x}$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "$\\dfrac{\\sqrt{x+h}-\\sqrt{x}}{h}$ eşleniği $\\sqrt{x+h}+\\sqrt{x}$ ile çarpılınca $\\dfrac{1}{\\sqrt{x+h}+\\sqrt{x}}$ olur.",
                "$h$ sıfıra giderken limit $\\dfrac{1}{2\\sqrt{x}}$ olur."),
            "Kuvvet kuralı bu sonucu da doğrular: $x^{1/2}$ nin türevi $\\dfrac{1}{2}x^{-1/2}$ dir. Tanım, kuralın kesirli üslerde de geçerli olduğunu gösterir. Sonucun $x=0$ da tanımsız olması da anlamlıdır: karekök grafiği başlangıç noktasında dikey olarak yükselir.",
        ]},
        {"baslik": "Bir noktada tanımla türev", "icerik": [
            "Yalnızca bir noktadaki türev istendiğinde $a$ yerine sayı yazılarak hesap kısalır. Bu durumda ikinci biçim çoğu zaman daha pratiktir.",
            ornek(
                "$f(x)=x^2-3x$ fonksiyonu verilsin.",
                "$f'(2)$ yi tanımla bulalım.",
                "$f(2+h)-f(2)=(4+4h+h^2-6-3h)-(-2)=h+h^2$ olur.",
                "$h$ ye bölünce $1+h$ kalır; limit $1$ dir, yani $f'(2)=1$."),
            ornek(
                "$f(x)=x^2$ fonksiyonu verilsin.",
                "İkinci biçimle $f'(3)$ ü bulalım.",
                "$\\dfrac{x^2-9}{x-3}=x+3$ olur.",
                "$x$ $3$ e giderken limit $6$ dır."),
        ]},
        {"baslik": "Limiti türev olarak tanımak", "icerik": [
            "Bazı sorularda türev tanımı biçiminde bir limit verilir ve değeri istenir. Limitin hangi fonksiyonun hangi noktadaki türevi olduğu tanınırsa uzun hesap yerine türev kuralı kullanılır.",
            ornek(
                "$\\lim_{h \\to 0}\\dfrac{(2+h)^4-16}{h}$ limiti verilsin.",
                "Limitin değerini bulalım.",
                "$16=2^4$ olduğundan limit, $f(x)=x^4$ fonksiyonunun $2$ deki türevidir.",
                "$f'(x)=4x^3$ olduğundan limit $f'(2)=32$ olur."),
        ]},
        {"baslik": "İkinci biçimi tanımak", "icerik": [
            "Verilen limit $x$ bir sayıya giderken $\\dfrac{f(x)-f(a)}{x-a}$ biçimindeyse ikinci tanım tanınır. Paydaki sabit sayı, fonksiyonun o noktadaki değeridir.",
            ornek(
                "$\\lim_{x \\to 2}\\dfrac{x^3-8}{x-2}$ limiti verilsin.",
                "Limiti türev olarak tanıyıp bulalım.",
                "$8=2^3$ olduğundan limit, $f(x)=x^3$ ün $2$ deki türevidir.",
                "$f'(x)=3x^2$ olduğundan limit $12$ olur; çarpanlara ayırma da aynı sonucu verir."),
        ]},
        {"baslik": "Katlı artış içeren limitler", "icerik": [
            "Tanımdaki $h$ yerine $2h$ ya da $-h$ gibi ifadeler bulunabilir. Bu durumda limit, paydadaki ile artıştaki katsayı eşitlenecek biçimde düzenlenir.",
            ornek(
                "$f'(3)=5$ olsun.",
                "$\\lim_{h \\to 0}\\dfrac{f(3+2h)-f(3)}{h}$ limitini bulalım.",
                "Pay ve payda $2$ ile düzenlenir: $2 \\cdot \\dfrac{f(3+2h)-f(3)}{2h}$ olur.",
                "Kesir $f'(3)$ e gider; limit $2 \\cdot 5=10$ olur."),
            ornek(
                "$f'(1)=4$ olsun.",
                "$\\lim_{h \\to 0}\\dfrac{f(1+h)-f(1-h)}{h}$ limitini bulalım.",
                "Pay $f(1+h)-f(1)$ ile $f(1)-f(1-h)$ farklarının toplamı olarak yazılır; her biri $h$ ye bölününce $f'(1)$ e gider.",
                "Limit $2f'(1)=8$ olur."),
            hap("$\\lim_{h \\to 0}\\dfrac{f(a+kh)-f(a)}{h}=k \\cdot f'(a)$ olur."),
        ]},
        {"baslik": "Sinüsün türevi", "icerik": [
            "Sinüsün türevi tanımdan bulunurken toplam formülü ve iki temel limit kullanılır: $\\lim_{h \\to 0}\\dfrac{\\sin h}{h}=1$ ve $\\lim_{h \\to 0}\\dfrac{\\cos h-1}{h}=0$.",
            ornek(
                "$f(x)=\\sin x$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "$\\sin(x+h)-\\sin x=\\sin x(\\cos h-1)+\\cos x \\sin h$ olur; $h$ ye bölünce iki terim kalır.",
                "Birinci terim $\\sin x \\cdot 0$ a, ikinci terim $\\cos x \\cdot 1$ e gider; türev $\\cos x$ olur."),
            "Toplam formülünün ayrıntısı için <a href=\"/blog/trigonometrik-toplam-fark/\">Trigonometrik Toplam ve Fark Formülleri</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kosinüsün türevi", "icerik": [
            "Kosinüsün türevi de aynı yolla bulunur. Bu kez kosinüs toplam formülü kullanılır: $\\cos(x+h)=\\cos x \\cos h-\\sin x \\sin h$.",
            ornek(
                "$f(x)=\\cos x$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "Fark $\\cos x(\\cos h-1)-\\sin x \\sin h$ olur; $h$ ye bölününce iki terim kalır.",
                "Birinci terim $0$ a, ikinci terim $-\\sin x$ e gider; türev $-\\sin x$ olur."),
            "Eksi işaretin geometrik anlamı açıktır: $0$ ile $\\pi$ arasında sinüs pozitiftir ve kosinüs bu aralıkta azalır; azalan bir fonksiyonun türevi negatiftir.",
        ]},
        {"baslik": "Üstel fonksiyonun türevi", "icerik": [
            "$e^x$ fonksiyonunun türevi tanımla bulunurken üs kuralı kullanılır: $e^{x+h}=e^x \\cdot e^h$. Böylece $e^x$ ortak çarpan olarak limitin dışına çıkar.",
            ornek(
                "$f(x)=e^x$ fonksiyonu verilsin.",
                "Türevini tanımla bulalım.",
                "$\\dfrac{e^{x+h}-e^x}{h}=e^x \\cdot \\dfrac{e^h-1}{h}$ olur.",
                "$\\lim_{h \\to 0}\\dfrac{e^h-1}{h}=1$ olduğundan türev $e^x$ tir."),
            "$e$ sayısını özel yapan budur: türevi kendisine eşit olan tek üstel fonksiyon $e^x$ tir. Başka bir taban için $\\dfrac{a^h-1}{h}$ in limiti $\\ln a$ olur ve türev $a^x \\ln a$ çıkar.",
        ]},
        {"baslik": "Sayısal türev", "icerik": [
            "Türev tanımındaki kesir, $h$ çok küçük seçilerek sayısal olarak hesaplanabilir. Hesap makineleri ve bilgisayarlar türevi çoğu zaman bu yolla yaklaşık bulur.",
            ornek(
                "$f(x)=2^x$ fonksiyonu verilsin.",
                "$f'(1)$ i $h=0.001$ ile yaklaşık hesaplayalım.",
                "$\\dfrac{2^{1.001}-2}{0.001}$ kesri yaklaşık $1.3868$ çıkar.",
                "Gerçek değer $2\\ln 2$, yaklaşık $1.3863$ tür; yaklaşım üç basamak doğrudur."),
        ]},
        {"baslik": "Soldan ve sağdan türev", "icerik": [
            "Tanımdaki limit iki yönden ayrı ayrı alınabilir. $h$ sıfıra soldan giderken elde edilen değere soldan türev, sağdan giderken elde edilene sağdan türev denir. Türevin var olması için ikisi eşit olmalıdır.",
            ornek(
                "$f(x)=|x|$ fonksiyonu ve $x=0$ noktası verilsin.",
                "Soldan ve sağdan türevleri bulalım.",
                "$\\dfrac{|h|-0}{h}$ kesri $h>0$ için $1$, $h<0$ için $-1$ dir.",
                "Sağdan türev $1$, soldan türev $-1$ olduğundan $|x|$ in sıfırda türevi yoktur."),
            hap("Türevin var olması için soldan ve sağdan türevler eşit olmalıdır.", "Grafiğin köşe yaptığı noktalarda bu iki türev farklıdır."),
        ]},
        {"baslik": "Dikey teğet", "icerik": [
            "Bazı fonksiyonlarda kesenin eğimi sonsuz büyür; teğet dikey olur. Dikey bir doğrunun eğimi tanımsız olduğu için bu noktada türev yoktur.",
            ornek(
                "$f(x)=\\sqrt[3]{x}$ fonksiyonu ve $x=0$ noktası verilsin.",
                "Türevin var olup olmadığını inceleyelim.",
                "Tanımdaki kesir $\\dfrac{h^{1/3}}{h}=h^{-2/3}$ olur.",
                "$h$ sıfıra giderken bu ifade sınırsız büyür; teğet dikeydir ve türev yoktur."),
        ]},
        {"baslik": "Türevin olmadığı noktalar", "icerik": [
            "Türevin olmadığı noktalar üç türe ayrılır. Grafiğe bakıldığında bu noktalar kolayca tanınır:",
            tablo(["Durum", "Örnek", "Neden?"], [
                ["Süreksizlik", "Sıçrama, boşluk", "Kesen eğimi sınırsız büyür"],
                ["Köşe", "$|x|$, $x=0$", "Soldan ve sağdan türev farklı"],
                ["Dikey teğet", "$\\sqrt[3]{x}$, $x=0$", "Eğim sonsuz"],
            ]),
            "Birinci durum, türevli her fonksiyonun sürekli olduğunu da açıklar: süreksiz bir noktada kesenin payı sıfıra gitmez, payda ise sıfıra gider ve limit oluşamaz.",
        ]},
        {"baslik": "Parçalı fonksiyonda türevlenebilirlik", "icerik": [
            "Parçalı bir fonksiyonun kritik noktada türevli olması için iki koşul gerekir: fonksiyon orada sürekli olmalı ve iki parçanın o noktadaki türevleri eşit olmalıdır. Bilinmeyen katsayılar bu iki koşuldan bulunur.",
            ornek(
                "$x \\le 1$ için $f(x)=x^2$, $x>1$ için $f(x)=ax+b$ olsun.",
                "Fonksiyonun $x=1$ de türevli olması için $a$ ve $b$ yi bulalım.",
                "Süreklilik: $1=a+b$. Türevlerin eşitliği: $2 \\cdot 1=a$, yani $a=2$.",
                "Buradan $b=-1$ bulunur; ikinci parça $y=2x-1$ olur ve bu, $x^2$ nin $1$ deki teğetidir."),
        ]},
        {"baslik": "Türev fonksiyonu ve türev değeri", "icerik": [
            "Tanım bir noktada uygulandığında bir sayı, genel $x$ için uygulandığında bir fonksiyon verir. $f'(x)$ fonksiyonuna türev fonksiyonu, $f'(a)$ sayısına ise $a$ daki türev değeri denir.",
            "Örneğin $f(x)=x^2$ için türev fonksiyonu $f'(x)=2x$ tir; bu fonksiyon her noktadaki teğet eğimini verir. $f'(3)=6$ ise yalnızca $x=3$ teki teğetin eğimidir. Önce türev fonksiyonunu bulup sonra sayı yazmak, her nokta için ayrı ayrı limit hesaplamaktan çok daha pratiktir.",
        ]},
        {"baslik": "Fiziksel yorum", "icerik": [
            "Konum fonksiyonunun tanımla alınan türevi, ortalama hızın zaman aralığı sıfıra giderken limitidir; yani anlık hızdır.",
            ornek(
                "Serbest düşen bir cismin aldığı yol yaklaşık $s(t)=4.9t^2$ metre olsun.",
                "Hız fonksiyonunu ve $t=2$ saniyedeki hızı bulalım.",
                "$\\dfrac{4.9(t+h)^2-4.9t^2}{h}=9.8t+4.9h$ olur; limit $v(t)=9.8t$ dir.",
                "$v(2)=19.6$ metre bölü saniye bulunur."),
        ]},
        {"baslik": "Türev ve küçük değişimler", "icerik": [
            "Tanımdaki kesir $h$ küçükken türeve yakın olduğu için $f(a+h)-f(a) \\approx f'(a) \\cdot h$ yazılabilir. Yani değişkendeki küçük bir değişim, fonksiyonda yaklaşık türev katı kadar değişim yaratır.",
            ornek(
                "$f(x)=x^2$ ve $a=3$ olsun.",
                "$x$ $3$ ten $3.01$ e çıkarken $f$ nin yaklaşık ne kadar değiştiğini bulalım.",
                "$f'(3)=6$ ve $h=0.01$ olduğundan değişim yaklaşık $0.06$ dır.",
                "Gerçek değişim $3.01^2-9=0.0601$ dir; yaklaşım çok iyidir."),
            hap("Kenarı $10$ santimetre olan kare bir fayans $0.1$ santimetre büyük kesilirse alan yaklaşık $2 \\cdot 10 \\cdot 0.1=2$ santimetrekare artar.", "Gerçek artış $10.1^2-10^2=2.01$ santimetrekaredir; türev bu küçük farkı çok iyi tahmin eder.", gunluk=True),
        ]},
        {"baslik": "Tanımdan kurallara", "icerik": [
            "Tanımla türev almak her fonksiyonda mümkündür ama uzun sürer. Bu yüzden tanım bir kez genel olarak uygulanır ve sonuçlar kurallar hâline getirilir: kuvvet kuralı, toplam kuralı, çarpım ve bölüm kuralları ve zincir kuralı.",
            "Kuralların hepsi tanımdan ispatlanır; bu yazıdaki hesaplar bu ispatların en basit örnekleridir. Kuralların listesi ve kullanımı için <a href=\"/blog/turev-alma-kurallari/\">Türev Alma Kuralları</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Sınavda türevin tanımı", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) türevin tanımı; verilen limitin türev olarak tanınması, katlı artış içeren limitler, soldan ve sağdan türev ve parçalı fonksiyonlarda türevlenebilirlik biçiminde karşına çıkabilir.",
                "Tanımla uzun türev hesabı nadiren istenir; genellikle limiti türev olarak tanımak beklenir."),
            "Soruda $h$ sıfıra giderken bir fark bölümü görüyorsan önce bunun hangi fonksiyonun hangi noktadaki türevi olduğunu yaz. Artıştaki katsayı ile paydadaki katsayı farklıysa limiti bu katsayılar oranıyla çarp.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$f(x+h)$ yerine $f(x)+h$ yazmak", "$x$ yerine $x+h$ konur"],
                ["Farkı açmadan $h$ ye bölmek", "Önce sadeleştirilir"],
                ["$h$ sadeleşmeden limit almak", "Belirsizlik kalır"],
                ["Katlı artışta katsayıyı unutmak", "Limit katsayıyla çarpılır"],
                ["Sürekli fonksiyonu türevli sanmak", "Köşe ve dikey teğet"],
                ["Parçalı fonksiyonda yalnız sürekliliğe bakmak", "Türevler de eşit olmalı"],
            ]),
            "En sık hata, $f(x+h)$ ifadesini yanlış yazmaktır. $f(x)=x^2$ için $f(x+h)=(x+h)^2$ dir, $x^2+h$ değildir. Bu adım doğru yapıldığında geri kalan işlem cebirsel bir sadeleştirmeden ibarettir.",
        ]},
    ],
    "sss": [
        ("Türevin tanımı nedir?",
         "f nin a daki türevi, f(a + h) eksi f(a) bölü h ifadesinin h sıfıra giderken limitidir. Bu limit kesen eğimlerinin teğet eğimine yaklaşmasını anlatır."),
        ("Türev tanımla nasıl bulunur?",
         "f(x + h) yazılır, f(x) çıkarılır, fark h ye bölünür ve h sadeleştikten sonra h sıfıra giderken limit alınır."),
        ("x karenin türevi tanımla nasıl bulunur?",
         "(x + h) kare eksi x kare, 2xh artı h kare olur. h ye bölünce 2x artı h kalır ve limit 2x tir."),
        ("Mutlak x in sıfırda türevi neden yoktur?",
         "Sağdan türev 1, soldan türev -1 dir. İki yön farklı olduğu için türev yoktur; grafikte bu nokta bir köşedir."),
        ("Verilen bir limit türev olarak nasıl tanınır?",
         "f(a + h) eksi f(a) bölü h biçimindeki limit, f nin a daki türevidir. Fonksiyon ve nokta belirlenip türev kuralı uygulanır."),
        ("Türevli her fonksiyon sürekli midir?",
         "Evet. Süreksiz bir noktada kesenin payı sıfıra gitmez ve limit oluşamaz. Tersi doğru değildir."),
        ("Sinüsün türevi neden kosinüstür?",
         "Tanımda sinüs toplam formülü açılır ve sin h bölü h ile cos h eksi 1 bölü h limitleri kullanılır. Birincisi 1 e, ikincisi 0 a gittiği için sonuç cos x olur."),
    ],
    "kontrol": [
        "Türevin kesen eğimlerinin limiti olduğunu açıklayabiliyorum.",
        "Türevin iki eşdeğer tanımını yazabiliyorum.",
        "Tanımla türev almanın dört adımını uygulayabiliyorum.",
        "Kare, küp, ters ve karekök fonksiyonlarının türevini tanımdan bulabiliyorum.",
        "Bir noktadaki türevi tanımla hesaplayabiliyorum.",
        "Verilen bir limiti türev olarak tanıyabiliyorum.",
        "Katlı artış içeren limitleri türevle çözebiliyorum.",
        "Soldan ve sağdan türevi hesaplayabiliyorum.",
        "Türevin olmadığı noktaları tanıyabiliyorum.",
        "Parçalı fonksiyonu türevli yapan katsayıları bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["turev-konu-anlatimi", "turev-alma-kurallari", "limitte-belirsizlikler"],
}
