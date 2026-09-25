# scripts/yazilar/26_trigonometrik_denklemler.py — Trigonometrik Denklemler (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

PI_ISARET = [(math.pi / 2, "π/2"), (math.pi, "π"), (3 * math.pi / 2, "3π/2"), (2 * math.pi, "2π")]

YAZI = {
    "slug": "trigonometrik-denklemler",
    "baslik": "Trigonometrik Denklemler Nasıl Çözülür?",
    "aciklama": "Trigonometrik denklemler nasıl çözülür? Genel çözüm, aralıkta çözüm, katlı açı, ikinci dereceden ve homojen denklemler, kök kaybı ve fazladan kök; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "trigonometrik-denklemler",
    "kapak_alt": "Trigonometrik denklemler: ahşap çember üzerinde aynı yüksekliğe ulaşan iki dönen kolu ışıklı işaretlerle gösteren iki öğrenci",
    "ozet": "Trigonometrik denklemlerde bilinmeyen bir açıdır ve çözüm, verilen trigonometrik değeri üreten açıları bulmaktır. Periyodiklik yüzünden bu denklemlerin genellikle sonsuz çözümü vardır. Bu yazıda sinüs, kosinüs, tanjant ve kotanjant denklemlerinin genel çözümünü, özel değerleri, belirli bir aralıktaki çözümleri, katlı ve ötelenmiş açıları, iki tarafında aynı fonksiyon bulunan denklemleri, ikinci dereceden ve homojen denklemleri, özdeşlikle tek fonksiyona indirmeyi, kök kaybı ve fazladan kök tuzaklarını ve gerçek hayattan bir uygulamayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Trigonometrik denklem nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birim çemberi, özel açıların değerlerini ve temel özdeşlikleri biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/birim-cember/\">Birim Çember Konu Anlatımı</a> ve <a href=\"/blog/trigonometrik-ozdeslikler-formuller/\">Trigonometrik Özdeşlikler ve Formüller</a> yazılarına göz at."),
            "Bilinmeyeni bir trigonometrik fonksiyonun içinde bulunan denklemlere <strong>trigonometrik denklem</strong> denir. $\\sin x=\\dfrac{1}{2}$, $2\\cos^2 x-1=0$ ya da $\\tan 2x=1$ birer trigonometrik denklemdir. Bu denklemleri çözmek, eşitliği sağlayan tüm açıları bulmak demektir.",
            "Kapaktaki çemberde iki kol farklı yönlerden dönüyor ama ikisinin ucu da aynı yüksekliğe ulaşıyor. Trigonometrik denklemlerin temel fikri budur: aynı sinüs değerini veren birden fazla açı vardır ve çözüm, bunların hepsini bulmayı gerektirir.",
        ]},
        {"baslik": "Neden sonsuz çözüm var?", "icerik": [
            "Sinüs ve kosinüs $2\\pi$ periyotlu, tanjant ve kotanjant ise $\\pi$ periyotlu fonksiyonlardır. Bir açı denklemi sağlıyorsa ona bir periyot eklenerek ya da çıkarılarak elde edilen her açı da denklemi sağlar. Bu yüzden bir çözüm bulunduğunda aslında sonsuz çözüm bulunmuş olur.",
            koordinat_grafik("y = sin x ile y = 1/2 doğrusunun kesişimi", [("", math.sin)], (-0.5, 7), (-1.5, 1.5), adim=0.5, etiket_adim=1, x_isaretler=PI_ISARET,
                             yataylar=[0.5], noktalar=[(math.pi / 6, 0.5, "", True), (5 * math.pi / 6, 0.5, "", True)]),
            "Grafikte sinüs dalgası $y=\\dfrac{1}{2}$ doğrusunu bir periyotta iki kez kesiyor. Dalga sonsuza kadar tekrar ettiği için kesişimler de her $2\\pi$ de bir tekrar eder. Çözümler bu yüzden genel çözüm denen bir kalıpla ya da istenen aralıkla sınırlandırılarak yazılır.",
        ]},
        {"baslik": "Sinüs denkleminin genel çözümü", "icerik": [
            "$\\sin x=a$ denkleminde $-1 \\le a \\le 1$ ise, sinüsü $a$ olan bir $\\alpha$ açısı bulunur. Sinüs birinci ve ikinci bölgede aynı değeri aldığı için ikinci çözüm $\\pi-\\alpha$ dır. Genel çözüm, $k$ bir tam sayı olmak üzere şöyle yazılır:",
            "$$x=\\alpha+2k\\pi$$",
            "ya da",
            "$$x=\\pi-\\alpha+2k\\pi$$",
            ornek(
                "$\\sin x=\\dfrac{\\sqrt{2}}{2}$ denklemi verilsin.",
                "Genel çözümü yazalım.",
                "Sinüsü $\\dfrac{\\sqrt{2}}{2}$ olan açılardan biri $\\alpha=\\dfrac{\\pi}{4}$ dir.",
                "Genel çözüm $x=\\dfrac{\\pi}{4}+2k\\pi$ ya da $x=\\dfrac{3\\pi}{4}+2k\\pi$ olur."),
            hap("$\\sin x=a$ denkleminin çözümleri $x=\\alpha+2k\\pi$ ve $x=\\pi-\\alpha+2k\\pi$ olur.", "İkinci kalıp unutulursa çözümlerin yarısı kaybolur."),
        ]},
        {"baslik": "Kosinüs denkleminin genel çözümü", "icerik": [
            "$\\cos x=a$ denkleminde kosinüsü $a$ olan açı $\\alpha$ ise ikinci çözüm $-\\alpha$ dır; çünkü kosinüs dikey eksene göre simetrik bir fonksiyondur. Birim çemberde bu iki açı yatay eksene göre birbirinin yansımasıdır:",
            "$$x=\\pm\\alpha+2k\\pi$$",
            ornek(
                "$\\cos x=\\dfrac{1}{2}$ denklemi verilsin.",
                "Genel çözümü yazalım.",
                "Kosinüsü $\\dfrac{1}{2}$ olan açılardan biri $\\alpha=\\dfrac{\\pi}{3}$ dir.",
                "Genel çözüm $x=\\pm\\dfrac{\\pi}{3}+2k\\pi$ olur; $[0, 2\\pi)$ aralığında bu $\\dfrac{\\pi}{3}$ ve $\\dfrac{5\\pi}{3}$ açılarıdır."),
            hap("$\\cos x=a$ denkleminin çözümleri $x=\\pm\\alpha+2k\\pi$ olur."),
        ]},
        {"baslik": "Tanjant ve kotanjant denklemleri", "icerik": [
            "Tanjant ve kotanjant her gerçek değeri alır ve periyotları $\\pi$ dir. Bu yüzden $\\tan x=a$ ve $\\cot x=a$ denklemlerinin her gerçek $a$ için çözümü vardır ve genel çözüm tek bir kalıpla yazılır:",
            "$$x=\\alpha+k\\pi$$",
            ornek(
                "$\\tan x=\\sqrt{3}$ ve $\\cot x=-1$ denklemleri verilsin.",
                "Genel çözümleri yazalım.",
                "$\\tan \\dfrac{\\pi}{3}=\\sqrt{3}$ olduğundan birincinin çözümü $x=\\dfrac{\\pi}{3}+k\\pi$ olur.",
                "$\\cot \\dfrac{3\\pi}{4}=-1$ olduğundan ikincinin çözümü $x=\\dfrac{3\\pi}{4}+k\\pi$ olur."),
            hap("$\\tan x=a$ denkleminin her gerçek $a$ için çözümü vardır ve çözümler $x=\\alpha+k\\pi$ olur."),
        ]},
        {"baslik": "Özel değerler", "icerik": [
            "Sağ taraf $0$, $1$ ya da $-1$ olduğunda çözümler birim çemberin eksenlerle kesiştiği noktalardadır. Bu durumlarda iki ayrı kalıp tek bir kalıba iner ve ezberlemek zaman kazandırır:",
            tablo(["Denklem", "Genel çözüm"], [
                ["$\\sin x=0$", "$x=k\\pi$"],
                ["$\\sin x=1$", "$x=\\dfrac{\\pi}{2}+2k\\pi$"],
                ["$\\sin x=-1$", "$x=\\dfrac{3\\pi}{2}+2k\\pi$"],
                ["$\\cos x=0$", "$x=\\dfrac{\\pi}{2}+k\\pi$"],
                ["$\\cos x=1$", "$x=2k\\pi$"],
                ["$\\cos x=-1$", "$x=\\pi+2k\\pi$"],
            ]),
        ]},
        {"baslik": "Çözümü olmayan denklemler", "icerik": [
            "Sinüs ve kosinüs yalnızca $-1$ ile $1$ arasındaki değerleri alır. Sağ tarafı bu aralığın dışında kalan bir sinüs ya da kosinüs denkleminin çözümü yoktur. Bu kontrol, bir denklemi çözmeye başlamadan önce yapılmalıdır.",
            ornek(
                "$2\\sin x=3$ ve $\\cos x+3=1$ denklemleri verilsin.",
                "Çözümleri inceleyelim.",
                "Birinci denklem $\\sin x=\\dfrac{3}{2}$ olur; $\\dfrac{3}{2}>1$ olduğundan çözüm yoktur.",
                "İkinci denklem $\\cos x=-2$ olur; $-2<-1$ olduğundan bunun da çözümü yoktur."),
        ]},
        {"baslik": "Aralıkta çözüm", "icerik": [
            "Sorular çoğu zaman genel çözüm yerine belirli bir aralıktaki çözümleri ister. Önce birinci bölgedeki referans açı bulunur, sonra sağ tarafın işaretine göre hangi bölgelerde çözüm olduğu belirlenir.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin x=-\\dfrac{1}{2}$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "Referans açı $\\dfrac{\\pi}{6}$ dir. Sinüs negatif olduğundan çözümler üçüncü ve dördüncü bölgededir.",
                "$x=\\pi+\\dfrac{\\pi}{6}=\\dfrac{7\\pi}{6}$ ve $x=2\\pi-\\dfrac{\\pi}{6}=\\dfrac{11\\pi}{6}$ olur."),
            ornek(
                "$[0, 2\\pi)$ aralığında $\\cos x=-\\dfrac{\\sqrt{3}}{2}$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "Referans açı $\\dfrac{\\pi}{6}$ dir. Kosinüs negatif olduğundan çözümler ikinci ve üçüncü bölgededir.",
                "$x=\\dfrac{5\\pi}{6}$ ve $x=\\dfrac{7\\pi}{6}$ olur."),
        ]},
        {"baslik": "Katlı açılar", "icerik": [
            "Fonksiyonun içinde $2x$ ya da $3x$ gibi katlı bir açı varsa önce bu açı için genel çözüm yazılır, sonra $x$ e geçilir. Aralık istendiğinde katlı açının aralığı da aynı oranda genişler; bu yüzden katlı açılarda daha fazla çözüm çıkar.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin 2x=\\dfrac{\\sqrt{3}}{2}$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$0 \\le 2x<4\\pi$ aralığında $2x=\\dfrac{\\pi}{3}, \\dfrac{2\\pi}{3}, \\dfrac{7\\pi}{3}, \\dfrac{8\\pi}{3}$ olur.",
                "İkiye bölünce $x=\\dfrac{\\pi}{6}, \\dfrac{\\pi}{3}, \\dfrac{7\\pi}{6}, \\dfrac{4\\pi}{3}$ bulunur."),
            dikkat(
                "Katlı açıda yalnızca ilk turdaki çözümleri alıp ikiye bölmek.",
                "Örnekte yalnızca $2x=\\dfrac{\\pi}{3}$ ve $\\dfrac{2\\pi}{3}$ alınsaydı iki çözüm kaybolurdu. $x$ aralığı $[0, 2\\pi)$ ise $2x$ aralığı $[0, 4\\pi)$ dir ve iki tam tur taranmalıdır."),
        ]},
        {"baslik": "Ötelenmiş açılar", "icerik": [
            "Fonksiyonun içinde $x-\\dfrac{\\pi}{6}$ gibi ötelenmiş bir açı varsa, bu ifade tek bir açı gibi düşünülür. Önce onun için çözüm yazılır, sonra öteleme miktarı eklenir ya da çıkarılır.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\cos\\left(x-\\dfrac{\\pi}{6}\\right)=0$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$x-\\dfrac{\\pi}{6}=\\dfrac{\\pi}{2}+k\\pi$, yani $x=\\dfrac{2\\pi}{3}+k\\pi$.",
                "Aralıktaki çözümler $\\dfrac{2\\pi}{3}$ ve $\\dfrac{5\\pi}{3}$ olur."),
        ]},
        {"baslik": "İki tarafta aynı fonksiyon", "icerik": [
            "$\\sin A=\\sin B$ biçimindeki bir denklemde iki açının sinüsleri eşittir. Bu, açıların ya eşit ya da bütünler olmasıyla mümkündür; periyot eklenerek iki kalıp elde edilir:",
            "$$A=B+2k\\pi$$",
            "ya da",
            "$$A=\\pi-B+2k\\pi$$",
            ornek(
                "$[0, \\pi)$ aralığında $\\sin 3x=\\sin x$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "Birinci kalıp: $3x=x+2k\\pi$, yani $x=k\\pi$; aralıkta $x=0$. İkinci kalıp: $3x=\\pi-x+2k\\pi$, yani $x=\\dfrac{\\pi}{4}+\\dfrac{k\\pi}{2}$.",
                "Aralıktaki çözümler $0$, $\\dfrac{\\pi}{4}$ ve $\\dfrac{3\\pi}{4}$ olur."),
        ]},
        {"baslik": "Kosinüs ve tanjantta eşitlik", "icerik": [
            "$\\cos A=\\cos B$ denkleminde açılar ya eşit ya da ters işaretlidir: $A=\\pm B+2k\\pi$. $\\tan A=\\tan B$ denkleminde ise tanjantın periyodu $\\pi$ olduğu için tek kalıp yeterlidir: $A=B+k\\pi$.",
            ornek(
                "$[0, \\pi]$ aralığında $\\cos 3x=\\cos x$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$3x=x+2k\\pi$ kalıbından $x=k\\pi$, yani $0$ ve $\\pi$; $3x=-x+2k\\pi$ kalıbından $x=\\dfrac{k\\pi}{2}$, yani $0$, $\\dfrac{\\pi}{2}$ ve $\\pi$.",
                "Ortak olanlar bir kez yazılır: çözümler $0$, $\\dfrac{\\pi}{2}$ ve $\\pi$ olur."),
        ]},
        {"baslik": "İkinci dereceden denklemler", "icerik": [
            "Denklemde aynı trigonometrik fonksiyonun hem karesi hem kendisi varsa, o fonksiyon yeni bir değişken gibi düşünülür. Böylece denklem ikinci dereceden bir denkleme dönüşür; bulunan her kök ayrı bir temel denklem verir.",
            ornek(
                "$[0, 2\\pi)$ aralığında $2\\sin^2 x-3\\sin x+1=0$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$\\sin x=t$ yazılırsa $2t^2-3t+1=0$, yani $(2t-1)(t-1)=0$ olur.",
                "$\\sin x=\\dfrac{1}{2}$ için $\\dfrac{\\pi}{6}$ ve $\\dfrac{5\\pi}{6}$; $\\sin x=1$ için $\\dfrac{\\pi}{2}$ bulunur."),
            "Yardımcı değişkenin köklerinden biri $-1$ ile $1$ aralığının dışında çıkarsa o kök atılır; çünkü sinüs ya da kosinüs o değeri alamaz.",
        ]},
        {"baslik": "Özdeşlikle tek fonksiyona indirmek", "icerik": [
            "Denklemde iki farklı fonksiyon varsa temel özdeşlikle biri diğerine çevrilir. $\\cos^2 x$ görüldüğünde $1-\\sin^2 x$ yazmak, denklemi yalnızca sinüs içeren ikinci dereceden bir denkleme dönüştürür.",
            ornek(
                "$[0, 2\\pi)$ aralığında $2\\cos^2 x-\\sin x-1=0$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$2(1-\\sin^2 x)-\\sin x-1=0$, yani $2\\sin^2 x+\\sin x-1=0$ ve $(2\\sin x-1)(\\sin x+1)=0$.",
                "$\\sin x=\\dfrac{1}{2}$ için $\\dfrac{\\pi}{6}$ ve $\\dfrac{5\\pi}{6}$; $\\sin x=-1$ için $\\dfrac{3\\pi}{2}$ bulunur."),
            "İki kat açı içeren denklemlerde de aynı fikir uygulanır: önce iki kat açı formülüyle tek açıya, sonra temel özdeşlikle tek fonksiyona inilir. Ayrıntılı örnekler için <a href=\"/blog/iki-kat-yarim-aci/\">İki Kat Açı ve Yarım Açı Formülleri</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Çarpanlara ayırma", "icerik": [
            "Denklemin her teriminde ortak bir çarpan varsa o çarpan paranteze alınır. Çarpımın sıfır olması için çarpanlardan en az biri sıfır olmalıdır; her çarpan ayrı bir denklem olarak çözülür.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\tan x \\sin x=\\sin x$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$\\sin x(\\tan x-1)=0$ olur. $\\sin x=0$ için $x=0$ ya da $\\pi$.",
                "$\\tan x=1$ için $x=\\dfrac{\\pi}{4}$ ya da $\\dfrac{5\\pi}{4}$. Dört çözümde de kosinüs sıfırdan farklıdır, yani tanjant tanımlıdır."),
        ]},
        {"baslik": "Homojen denklemler", "icerik": [
            "Her terimi sinüs ve kosinüs bakımından aynı dereceden olan denklemlere homojen denklem denir. Bu denklemlerde iki taraf uygun bir kosinüs kuvvetine bölünerek yalnızca tanjant içeren bir denklem elde edilir. Bölmeden önce kosinüsün sıfır olduğu değerlerin çözüm olup olmadığı kontrol edilmelidir.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin^2 x=3\\cos^2 x$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "$\\cos x=0$ iken sol taraf $1$, sağ taraf $0$ olur; bu değerler çözüm değildir. İki taraf $\\cos^2 x$ e bölünür: $\\tan^2 x=3$.",
                "$\\tan x=\\pm\\sqrt{3}$ olduğundan çözümler $\\dfrac{\\pi}{3}$, $\\dfrac{2\\pi}{3}$, $\\dfrac{4\\pi}{3}$ ve $\\dfrac{5\\pi}{3}$ olur."),
        ]},
        {"baslik": "Sinüs ve kosinüsün toplamı", "icerik": [
            "$a\\sin x+b\\cos x=c$ biçimindeki denklemlerde sol taraf toplam formülüyle tek bir sinüse çevrilir. Böylece iki fonksiyon içeren denklem tek bir temel denkleme iner.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin x+\\cos x=1$ denklemi verilsin.",
                "Çözümleri bulalım.",
                "Sol taraf $\\sqrt{2}\\sin\\left(x+\\dfrac{\\pi}{4}\\right)$ olur; denklem $\\sin\\left(x+\\dfrac{\\pi}{4}\\right)=\\dfrac{\\sqrt{2}}{2}$ biçimine iner.",
                "$x+\\dfrac{\\pi}{4}=\\dfrac{\\pi}{4}$ ya da $\\dfrac{3\\pi}{4}$ olduğundan çözümler $0$ ve $\\dfrac{\\pi}{2}$ olur."),
            "Dönüşümün ayrıntısı için <a href=\"/blog/trigonometrik-toplam-fark/\">Trigonometrik Toplam ve Fark Formülleri</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kare almak fazladan kök üretir", "icerik": [
            "Aynı denklem iki tarafın karesi alınarak da çözülebilir gibi görünür. Ancak kare almak, işareti farklı olan çözümleri de denkleme katar. Bu yüzden kare alınarak bulunan her çözüm asıl denklemde denenmelidir.",
            ornek(
                "$\\sin x+\\cos x=1$ denkleminin iki tarafının karesi alınsın.",
                "Bulunan çözümleri asıl denklemde deneyelim.",
                "Kare alınınca $1+2\\sin x \\cos x=1$, yani $\\sin 2x=0$ olur ve $[0, 2\\pi)$ aralığında $0$, $\\dfrac{\\pi}{2}$, $\\pi$ ve $\\dfrac{3\\pi}{2}$ bulunur.",
                "$x=\\pi$ için sol taraf $0+(-1)=-1$, $x=\\dfrac{3\\pi}{2}$ için $-1+0=-1$ olur. Bu iki değer fazladan köktür; gerçek çözümler yalnızca $0$ ve $\\dfrac{\\pi}{2}$ dir."),
        ]},
        {"baslik": "Bölmek kök kaybettirir", "icerik": [
            "Bilinmeyen içeren bir ifadeye bölmek, o ifadeyi sıfır yapan çözümleri siler. Bu hata trigonometrik denklemlerde çok sık yapılır; ortak çarpan her zaman bölmek yerine paranteze alınmalıdır.",
            dikkat(
                "$\\tan x \\sin x=\\sin x$ denkleminde iki tarafı $\\sin x$ e bölmek.",
                "Bölme yapılsaydı $\\tan x=1$ kalır ve yalnızca $\\dfrac{\\pi}{4}$ ile $\\dfrac{5\\pi}{4}$ bulunurdu. $\\sin x=0$ yapan $0$ ve $\\pi$ çözümleri kaybolurdu."),
            "Tersine, denklemin tanım kümesi de kontrol edilmelidir. Paydada kosinüs olan bir denklemde bulunan kök kosinüsü sıfır yapıyorsa çözüm değildir. Örneğin $\\dfrac{1-\\sin x}{\\cos x}=0$ denkleminde pay $x=\\dfrac{\\pi}{2}$ için sıfır olur, ama bu değerde payda da sıfırdır; denklemin çözümü yoktur.",
            hap("Bilinmeyen içeren bir ifadeye bölmek, o ifadeyi sıfır yapan çözümleri siler.", "Ortak çarpan bölünmez, paranteze alınır."),
        ]},
        {"baslik": "Eşitsizlikler", "icerik": [
            "Trigonometrik eşitsizlik çözerken önce eşitlik durumu çözülür, sonra birim çemberde ya da grafikte hangi yayların eşitsizliği sağladığına bakılır. Sınır noktalarının dahil olup olmadığı eşitsizliğin türüne bağlıdır.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\cos x<\\dfrac{1}{2}$ eşitsizliği verilsin.",
                "Çözüm kümesini bulalım.",
                "Eşitlik $x=\\dfrac{\\pi}{3}$ ve $x=\\dfrac{5\\pi}{3}$ için sağlanır. Kosinüs bu iki açı arasında $\\dfrac{1}{2}$ den küçüktür.",
                "Çözüm kümesi $\\left(\\dfrac{\\pi}{3}, \\dfrac{5\\pi}{3}\\right)$ aralığıdır."),
        ]},
        {"baslik": "Çözüm sayısı", "icerik": [
            "Yalnızca çözüm sayısı soruluyorsa periyot sayısı kullanılır. $\\sin(bx)=a$ denkleminde $-1<a<1$ ise her periyotta iki çözüm vardır; aralıktaki periyot sayısı ikiyle çarpılır.",
            ornek(
                "$[0, 2\\pi)$ aralığında $\\sin 3x=\\dfrac{1}{2}$ denklemi verilsin.",
                "Çözüm sayısını bulalım.",
                "$\\sin 3x$ in periyodu $\\dfrac{2\\pi}{3}$ olduğundan aralık üç tam periyot içerir.",
                "Her periyotta iki çözüm vardır; toplam altı çözüm bulunur."),
        ]},
        {"baslik": "Uygulama: dönme dolap", "icerik": [
            "Periyodik hareketler trigonometrik denklemlerle modellenir. Bir dönme dolabın kabini bir turu $30$ saniyede tamamlasın ve kabinin yerden yüksekliği metre cinsinden $h(t)=10-8\\cos\\left(\\dfrac{\\pi t}{15}\\right)$ ile verilsin. Kabin en alçakta $2$, en yüksekte $18$ metreye çıkar.",
            ornek(
                "İlk tur içinde, yani $0 \\le t<30$ aralığında kabinin $14$ metre yükseklikte olduğu anlar istensin.",
                "Denklemi çözelim.",
                "$10-8\\cos\\left(\\dfrac{\\pi t}{15}\\right)=14$ olduğundan $\\cos\\left(\\dfrac{\\pi t}{15}\\right)=-\\dfrac{1}{2}$.",
                "$\\dfrac{\\pi t}{15}=\\dfrac{2\\pi}{3}$ ya da $\\dfrac{4\\pi}{3}$ olduğundan $t=10$ ve $t=20$ saniye bulunur; kabin bu yüksekliğe bir kez çıkarken bir kez inerken ulaşır."),
            "Aynı hesap sonraki turlarda da geçerlidir: periyot $30$ saniye olduğundan kabin $40$ ve $50$ saniyelerde, sonra her turda yine iki kez bu yüksekliğe ulaşır. Modeldeki periyot, denklemin genel çözümündeki tekrar aralığıyla aynıdır.",
            hap("Periyodik bir harekette aynı yüksekliğe bir turda iki kez ulaşılır: biri çıkarken, biri inerken.", "Yüksekliği $h(t)=10-8\\cos \\dfrac{\\pi t}{15}$ metre olan kabin, $30$ saniyelik bir turda $10$ metreye $t=7.5$ ve $t=22.5$ saniyelerde ulaşır.", gunluk=True),
        ]},
        {"baslik": "Sınavda trigonometrik denklemler", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) trigonometrik denklemler; belirli aralıktaki çözümler, çözümlerin toplamı ya da sayısı, katlı açılar ve ikinci dereceden denklemler biçiminde karşına çıkabilir.",
                "Özdeşliklerle sadeleştirme gerektiren denklemler de sık sorulur."),
            "Çözüme başlamadan önce üç soruyu sor: sağ taraf sinüs ya da kosinüsün alabileceği aralıkta mı, denklemde kaç farklı fonksiyon ve açı var, istenen aralık katlı açı için nasıl genişliyor? Bu üç soru, yöntemi seçmeyi ve kök kaybetmemeyi sağlar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\sin x=a$ için yalnızca $\\alpha$ yı yazmak", "$\\pi-\\alpha$ çözümü de var"],
                ["Tanjantta periyodu $2\\pi$ almak", "Tanjantın periyodu $\\pi$"],
                ["Katlı açıda aralığı genişletmemek", "$2x$ için aralık iki katına çıkar"],
                ["Ortak çarpana bölmek", "Paranteze alınır"],
                ["Kare alıp kökleri denememek", "Fazladan kökler elenir"],
                ["$\\sin x=2$ için çözüm aramak", "Çözüm yoktur"],
            ]),
            "Bulduğun her çözümü asıl denkleme yerleştirerek kontrol etmek, hem fazladan kökleri hem de hesap hatalarını yakalar. Özel açılarda bu kontrol birkaç saniye sürer.",
        ]},
    ],
    "sss": [
        ("Trigonometrik denklem nedir?",
         "Bilinmeyenin bir trigonometrik fonksiyonun içinde bulunduğu denklemdir. Örneğin sin x eşittir 1 bölü 2 bir trigonometrik denklemdir."),
        ("sin x eşittir a denkleminin genel çözümü nedir?",
         "Sinüsü a olan açı alfa ise çözümler alfa artı 2 k pi ve pi eksi alfa artı 2 k pi dir."),
        ("cos x eşittir a denkleminin genel çözümü nedir?",
         "Kosinüsü a olan açı alfa ise çözümler artı eksi alfa artı 2 k pi dir."),
        ("Tanjant denkleminin genel çözümü nasıl yazılır?",
         "Tanjantı a olan açı alfa ise çözümler alfa artı k pi dir; tanjantın periyodu pi olduğu için tek kalıp yeterlidir."),
        ("Trigonometrik denklemde neden kök kaybedilir?",
         "Bilinmeyen içeren bir ifadeye bölündüğünde o ifadeyi sıfır yapan çözümler kaybolur. Ortak çarpan paranteze alınmalıdır."),
        ("Katlı açıda aralık nasıl değişir?",
         "x için aralık 0 ile 2 pi ise 2x için aralık 0 ile 4 pi olur. Katlı açının aralığı aynı katla genişletilir."),
    ],
    "kontrol": [
        "Trigonometrik denklemin neden sonsuz çözümü olduğunu açıklayabiliyorum.",
        "Sinüs ve kosinüs denklemlerinin genel çözümünü yazabiliyorum.",
        "Tanjant ve kotanjant denklemlerini çözebiliyorum.",
        "Çözümü olmayan denklemleri tanıyabiliyorum.",
        "Belirli bir aralıktaki çözümleri bulabiliyorum.",
        "Katlı ve ötelenmiş açılı denklemleri çözebiliyorum.",
        "İki tarafında aynı fonksiyon bulunan denklemleri çözebiliyorum.",
        "İkinci dereceden ve homojen denklemleri çözebiliyorum.",
        "Kök kaybı ve fazladan kök tuzaklarından kaçınabiliyorum.",
        "Trigonometrik denklemlerle gerçek hayat problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["trigonometrik-toplam-fark", "iki-kat-yarim-aci", "trigonometrik-fonksiyon-grafikleri"],
}
