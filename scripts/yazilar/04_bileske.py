# scripts/yazilar/04_bileske.py — dorduncu blog yazisi (23.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "bileske-fonksiyon",
    "baslik": "Bileşke Fonksiyon Konu Anlatımı",
    "aciklama": "Bileşke fonksiyon nedir, nasıl hesaplanır? Tanım kümesi, özellikler, içteki ve dıştaki fonksiyonu bulma, tekrarlı bileşke; çözümlü örneklerle.",
    "tarih": "2026-09-23",
    "guncelleme": None,
    "kategori": "fonksiyonlar",
    "sinavlar": ["TYT", "AYT", "ALES", "KPSS"],
    "kapak": "bileske-fonksiyon",
    "kapak_alt": "Bileşke fonksiyon konu anlatımı: mavi üçgeni iki aşamalı şekil dönüştürme düzeneğine yerleştiren öğrenci; birinci aşamanın çıktısı ikinci aşamaya girdi oluyor",
    "ozet": "Bir fonksiyonun çıktısını başka bir fonksiyona girdi olarak verdiğinde bileşke fonksiyon elde edersin. Fikir basittir ama hataya açık üç noktası vardır: hangi fonksiyonun önce çalıştığı, bileşkenin tanım kümesi ve verilen bileşkeden bir fonksiyonu geri çekmek. Bu yazıda bileşkeyi sayısal değerden başlayıp kural bulmaya, tanım kümesine, özelliklere ve tekrarlı bileşkeye kadar adım adım işliyoruz.",
    "bolumler": [
        {"baslik": "Bileşke fonksiyon nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için fonksiyonda değer hesaplamayı, tanım kümesi kavramını ve birinci dereceden denklem çözmeyi biliyor olman yeterli.",
                "Tanım kümesi konusu yeni geliyorsa önce <a href=\"/blog/tanim-deger-goruntu-kumeleri/\">Tanım, Değer ve Görüntü Kümeleri</a> yazısına göz at."),
            "Bir fonksiyonu girdiyi işleyip çıktı veren bir makine gibi düşün. İki makineyi arka arkaya bağlarsan, birincinin çıktısı ikincinin girdisi olur. Bu birleşik makineye <strong>bileşke fonksiyon</strong> denir.",
            "$g$ önce, $f$ sonra çalışıyorsa bileşke şöyle yazılır ve \"$f$ bileşke $g$\" diye okunur:",
            "$$(f \\circ g)(x)=f(g(x))$$",
            "Yazılışta $f$ solda olduğu hâlde önce $g$ çalışır. Bunun sebebi $f(g(x))$ ifadesinin kendisidir: $f$ nin hesaplanabilmesi için parantezin içindeki $g(x)$ in önce bilinmesi gerekir.",
            hap("$(f \\circ g)(x)=f(g(x))$: <strong>sağdaki önce</strong> çalışır.",
                "Önce $g$ uygulanır, çıkan sonuç $f$ ye verilir."),
        ]},
        {"baslik": "Sayısal değer hesaplama", "icerik": [
            "Bileşkede bir değer istendiğinde içten dışa doğru ilerlenir. Önce içteki fonksiyonun değeri hesaplanır, sonra bu sayı dıştaki fonksiyona verilir.",
            ornek(
                "$f(x)=x^2+1$ ve $g(x)=2x-3$ olsun.",
                "$(f \\circ g)(2)$ ve $(g \\circ f)(2)$ değerlerini bulalım.",
                "$(f \\circ g)(2)=f(g(2))$. Önce $g(2)=4-3=1$. Sonra $f(1)=1+1=2$.",
                "$(g \\circ f)(2)=g(f(2))$. Önce $f(2)=4+1=5$. Sonra $g(5)=10-3=7$.",
                "Sonuçlar farklı: $2$ ve $7$. Bileşkede sıra önemlidir."),
            "Fonksiyonlar kural yerine tabloyla da verilebilir. Mantık değişmez: içteki değeri tablodan okursun, çıkan sayıyı dıştaki fonksiyonun tablosunda ararsın.",
            ornek(
                "$A=\\{1,2,3\\}$ üzerinde $g$ fonksiyonu $1 \\to 2$, $2 \\to 3$, $3 \\to 1$ biçiminde, $f$ fonksiyonu ise $1 \\to 2$, $2 \\to 2$, $3 \\to 1$ biçiminde tanımlansın.",
                "$f \\circ g$ ve $g \\circ f$ yi eleman eleman yazalım.",
                "$f \\circ g$: $1 \\to f(2)=2$, $2 \\to f(3)=1$, $3 \\to f(1)=2$.",
                "$g \\circ f$: $1 \\to g(2)=3$, $2 \\to g(2)=3$, $3 \\to g(1)=2$.",
                "İki bileşke farklı fonksiyonlardır."),
            "Aynı fonksiyon kendisiyle de birleştirilebilir. $(f \\circ f)(x)=f(f(x))$ yazılır. Yukarıdaki $f(x)=x^2+1$ için $(f \\circ f)(1)=f(2)=5$ tir.",
            hap("Açılışı $20$ lira, kilometresi $15$ lira olan bir taksinin ücreti $f(y)=20+15y$, dakikada yarım kilometre giden taksinin yolu $g(t)=0.5t$ olsun.", "Ücret süreye göre $(f \\circ g)(t)=20+7.5t$ olur; $20$ dakikalık yolculuk $170$ lira tutar.", gunluk=True),
        ]},
        {"baslik": "Bileşkenin kuralını bulma", "icerik": [
            "Kuralı bulmak için dıştaki fonksiyonun kuralında $x$ gördüğün her yere içteki fonksiyonun <strong>tamamını</strong> parantez içinde yazarsın.",
            ornek(
                "$f(x)=x^2+1$ ve $g(x)=2x-3$ olsun.",
                "$(f \\circ g)(x)$ ve $(g \\circ f)(x)$ kurallarını bulalım.",
                "$(f \\circ g)(x)=f(2x-3)=(2x-3)^2+1=4x^2-12x+10$.",
                "$(g \\circ f)(x)=g(x^2+1)=2(x^2+1)-3=2x^2-1$.",
                "Kontrol: $x=2$ için $4 \\cdot 4-24+10=2$ ve $2 \\cdot 4-1=7$ bulunur. Önceki bölümdeki sonuçlarla aynı."),
            dikkat(
                "İçteki ifadeyi yerine koyarken parantez kullan.",
                "$f(x)=x^2+1$ için $f(2x-3)$ yazarken $2x-3^2+1$ değil, $(2x-3)^2+1$ yazılır."),
            hap("$f(g(x))$ i bulmak için $f$ nin kuralındaki her $x$ in yerine $(g(x))$ yaz.",
                "Kontrolü bir sayı vererek yap: iki yoldan aynı sonuç çıkmalı."),
        ]},
        {"baslik": "Bir fonksiyonu bileşkeye ayırma", "icerik": [
            "Bazen iş tersinden gelir: karmaşık görünen bir fonksiyonu iki basit fonksiyonun bileşkesi olarak yazmak istenir. Bu beceri ileride türevde zincir kuralı için de gerekecek.",
            "Yöntem şudur: $x$ e <strong>ilk</strong> yapılan işlemi içteki fonksiyon, ondan sonra yapılanı dıştaki fonksiyon olarak al.",
            ornek(
                "$h(x)=\\sqrt{3x+1}$ olsun.",
                "$h$ yi iki fonksiyonun bileşkesi olarak yazalım.",
                "$x$ e önce $3x+1$ işlemi yapılıyor, sonra sonucun karekökü alınıyor.",
                "İçteki fonksiyon $g(x)=3x+1$, dıştaki fonksiyon $f(x)=\\sqrt{x}$ tir.",
                "Kontrol: $(f \\circ g)(x)=f(3x+1)=\\sqrt{3x+1}=h(x)$."),
            "Aynı fonksiyon birden fazla biçimde ayrılabilir. $h(x)=(x^2+1)^3$ için $g(x)=x^2+1$ ve $f(x)=x^3$ seçilebilir; $g(x)=x^2$ ve $f(x)=(x+1)^3$ de seçilebilir. İki seçim de doğrudur. Çoğu zaman en kullanışlı olan, parantezin içini içteki fonksiyon alan ayrımdır.",
            hap("Bileşkeye ayırırken $x$ e ilk yapılan işlem içteki fonksiyondur.",
                "Ayrım tek değildir; kontrolü $f(g(x))$ i yeniden hesaplayarak yap."),
        ]},
        {"baslik": "Bileşkenin tanım kümesi", "icerik": [
            "$f \\circ g$ nin bir $x$ için hesaplanabilmesi için iki şart birden gerekir. Önce $x$, $g$ nin tanım kümesinde olmalıdır. Sonra çıkan $g(x)$ değeri, $f$ nin tanım kümesinde olmalıdır.",
            "$$x \\in T_g \\text{ ve } g(x) \\in T_f$$",
            "Burada $T_g$ ve $T_f$, $g$ ile $f$ nin tanım kümeleridir.",
            ornek(
                "$f(x)=\\sqrt{x}$ ve $g(x)=x-4$ olsun.",
                "$f \\circ g$ ve $g \\circ f$ nin tanım kümelerini bulalım.",
                "$(f \\circ g)(x)=\\sqrt{x-4}$. $g$ her yerde tanımlı; $g(x)=x-4$ ise $f$ nin tanım kümesinde olmalı: $x-4 \\geq 0$. Tanım kümesi $[4,\\infty)$ dur.",
                "$(g \\circ f)(x)=\\sqrt{x}-4$. İçteki $f$ için $x \\geq 0$ gerekir; $g$ ise her sayıyı kabul eder. Tanım kümesi $[0,\\infty)$ dur."),
            "Dıştaki fonksiyonun şartı içteki fonksiyonun <strong>değerine</strong> uygulanır. $f(x)=\\dfrac{1}{x-1}$ ve $g(x)=x^2$ ise $(f \\circ g)(x)=\\dfrac{1}{x^2-1}$ olur. $f$ nin şartı $g(x) \\neq 1$, yani $x^2 \\neq 1$ dir. Buradan $x \\neq 1$ ve $x \\neq -1$ çıkar; tanım kümesi $\\mathbb{R}-\\{-1,1\\}$ dir. $f$ nin kendi şartındaki tek sayı olan $1$, bileşkede iki sayıyı birden dışarıda bıraktı.",
            dikkat(
                "Bileşkenin tanım kümesi, sadeleşmiş son kurala bakılarak bulunmaz.",
                "$f(x)=\\dfrac{1}{x}$ ve $g(x)=\\dfrac{1}{x}$ olsun. $(f \\circ g)(x)=\\dfrac{1}{\\frac{1}{x}}=x$ gibi görünür.",
                "Ama $x=0$ için $g(0)$ tanımsızdır, bu yüzden $f(g(0))$ da tanımsızdır. $f \\circ g$ nin tanım kümesi $\\mathbb{R}-\\{0\\}$ dır, $\\mathbb{R}$ değil."),
            hap("$f \\circ g$ nin tanım kümesi: $g$ nin tanım kümesinden, $g(x)$ i $f$ nin tanım kümesine düşüren $x$ ler.",
                "Önce içteki fonksiyonun şartını, sonra dıştakinin şartını yaz."),
        ]},
        {"baslik": "Bileşkenin özellikleri", "icerik": [
            "<ul>"
            "<li><strong>Değişme özelliği yoktur.</strong> Genel olarak $f \\circ g \\neq g \\circ f$. Yukarıdaki örnekte $4x^2-12x+10$ ile $2x^2-1$ bulduk.</li>"
            "<li><strong>Birleşme özelliği vardır.</strong> $(f \\circ g) \\circ h=f \\circ (g \\circ h)$. İki taraf da $x$ i önce $h$ ye, sonra $g$ ye, sonra $f$ ye verir; yani ikisi de $f(g(h(x)))$ tir.</li>"
            "<li><strong>Birim fonksiyon etkisizdir.</strong> $I(x)=x$ ise $f \\circ I=I \\circ f=f$.</li>"
            "<li><strong>Ters fonksiyonla bileşke birimi verir.</strong> $f$ birebir ve örtense $f \\circ f^{-1}=f^{-1} \\circ f=I$.</li>"
            "</ul>",
            "Değişme özelliğinin olmaması, iki bileşkenin <strong>hiçbir zaman</strong> eşit olmadığı anlamına gelmez. Bazı fonksiyon çiftlerinde eşit çıkarlar.",
            ornek(
                "$f(x)=x+2$ ve $g(x)=x+5$ olsun.",
                "$f \\circ g$ ile $g \\circ f$ yi karşılaştıralım.",
                "$(f \\circ g)(x)=(x+5)+2=x+7$.",
                "$(g \\circ f)(x)=(x+2)+5=x+7$.",
                "Bu iki fonksiyon için bileşkeler eşittir. Ama bu bir kural değil, bu çifte özgü bir sonuçtur."),
            hap("Bileşkede birleşme özelliği <strong>vardır</strong>, değişme özelliği genel olarak <strong>yoktur</strong>.",
                "Birim fonksiyon $I(x)=x$ bileşkenin etkisiz elemanıdır."),
        ]},
        {"baslik": "İçteki fonksiyonu bulma", "icerik": [
            "Klasik bir soru tipi, $f$ ve $f \\circ g$ verilip $g$ nin istenmesidir. Burada yapılacak iş, $f$ nin kuralına $g(x)$ i yerleştirip çıkan ifadeyi verilen bileşkeye eşitlemektir.",
            ornek(
                "$f(x)=2x+5$ ve $(f \\circ g)(x)=4x^2-1$ olsun.",
                "$g(x)$ i bulalım.",
                "$(f \\circ g)(x)=f(g(x))=2 \\cdot g(x)+5$.",
                "Verilen bileşkeye eşitleyelim: $2 \\cdot g(x)+5=4x^2-1$.",
                "$2 \\cdot g(x)=4x^2-6$ ve $g(x)=2x^2-3$.",
                "Kontrol: $f(2x^2-3)=2(2x^2-3)+5=4x^2-1$."),
            "Dıştaki fonksiyon doğrusal değilse aynı yol yine işler, ama çözüm tek olmayabilir. Örneğin $f(x)=x^2$ ve $(f \\circ g)(x)=x^2+2x+1$ ise $g(x)^2=(x+1)^2$ olur. Hem $g(x)=x+1$ hem $g(x)=-x-1$ bu eşitliği sağlar; $g(x)=|x+1|$ de sağlar. Bu yüzden böyle bir soruda $g$ hakkında ek bilgi verilmelidir, örneğin doğrusal olduğu.",
            hap("İçteki fonksiyonu bulmak için $f(g(x))$ i $f$ nin kuralıyla yaz ve $g(x)$ i bilinmeyen gibi çöz.",
                "Sonucu mutlaka geri yerine koyarak kontrol et."),
        ]},
        {"baslik": "Dıştaki fonksiyonu bulma", "icerik": [
            "Tersi daha çok zorlar: $g$ ve $f \\circ g$ verilir, $f$ istenir. Yani $f(2x+1)=4x+7$ gibi bir eşitlikten $f(x)$ bulunacaktır. İki yol vardır.",
            "<h3>Birinci yol: yeni değişken</h3>",
            ornek(
                "$f(2x+1)=4x+7$ olsun.",
                "$f(x)$ i bulalım.",
                "Parantezin içine yeni bir ad verelim: $t=2x+1$. Buradan $x=\\dfrac{t-1}{2}$.",
                "Eşitlikte $x$ in yerine bunu yazalım: $f(t)=4 \\cdot \\dfrac{t-1}{2}+7=2t-2+7=2t+5$.",
                "Değişkenin adı önemli değildir: $f(x)=2x+5$.",
                "Kontrol: $f(2x+1)=2(2x+1)+5=4x+7$."),
            "<h3>İkinci yol: parantezin içini oluşturmak</h3>",
            "Sağ tarafı parantezin içindeki ifade cinsinden yazmaya çalışırsın. $4x+7=2(2x+1)+5$ olduğu hemen görülür. Öyleyse $f(2x+1)=2(2x+1)+5$ ve $f(x)=2x+5$ tir. Bu yol doğrusal ifadelerde hızlıdır, karmaşık ifadelerde birinci yol daha güvenlidir.",
            ornek(
                "$f(x+1)=x^2+3x$ olsun.",
                "$f(x)$ i bulalım.",
                "$t=x+1$ diyelim; $x=t-1$.",
                "$f(t)=(t-1)^2+3(t-1)=t^2-2t+1+3t-3=t^2+t-2$.",
                "$f(x)=x^2+x-2$."),
            hap("Yalnızca bir <strong>değer</strong> isteniyorsa kuralı bulmaya gerek yok: parantezin içini istenen sayıya eşitle.",
                "$f(2x+1)=4x+7$ ise $f(9)$ için $2x+1=9$, $x=4$ ve $f(9)=4 \\cdot 4+7=23$ tür."),
        ]},
        {"baslik": "Parçalı fonksiyonlarda bileşke", "icerik": [
            "Parçalı bir fonksiyon, tanım kümesinin farklı aralıklarında farklı kuralla hesaplanır. Bileşkede dikkat edilecek nokta şudur: her adımda, o adımdaki sayının <strong>hangi aralıkta</strong> olduğuna yeniden bakılır.",
            ornek(
                "$x<2$ için $f(x)=x+1$, $x \\geq 2$ için $f(x)=x^2$ olsun. Ayrıca $g(x)=3-x$ verilsin.",
                "$f(g(0))$, $g(f(1))$ ve $f(f(1))$ değerlerini bulalım.",
                "$f(g(0))$: önce $g(0)=3$. $3 \\geq 2$ olduğu için $f(3)=9$.",
                "$g(f(1))$: $1<2$ olduğu için $f(1)=2$. Sonra $g(2)=1$.",
                "$f(f(1))$: $f(1)=2$. Bu kez $2 \\geq 2$ olduğu için ikinci kural geçerli: $f(2)=4$."),
            dikkat(
                "$f(f(1))$ hesaplanırken ilk adımda birinci kural, ikinci adımda ikinci kural kullanıldı.",
                "Her adımda aralığı yeniden kontrol et; bir önceki adımın kuralı sonrakine taşınmaz."),
        ]},
        {"baslik": "Tekrarlı bileşke", "icerik": [
            "Bir fonksiyon kendisiyle defalarca birleştirildiğinde bazen bir <strong>döngü</strong> ortaya çıkar. Birkaç adım hesaplayıp döngüyü yakalamak, uzun hesabı kısaltır.",
            ornek(
                "$f(x)=\\dfrac{1}{1-x}$ olsun ($x \\neq 1$).",
                "$f$ yi $2026$ kez art arda $2$ sayısına uygularsak sonuç ne olur?",
                "$f(2)=\\dfrac{1}{1-2}=-1$.",
                "$f(-1)=\\dfrac{1}{1+1}=\\dfrac{1}{2}$.",
                "$f\\left(\\dfrac{1}{2}\\right)=\\dfrac{1}{1-\\frac{1}{2}}=2$. Başa döndük; döngünün uzunluğu $3$ tür.",
                "$2026=3 \\cdot 675+1$ olduğundan $2026$ uygulama, $675$ tam döngü ve $1$ adım demektir.",
                "Sonuç $f(2)=-1$ dir."),
            "Bu döngü tesadüf değildir. Aynı fonksiyon için cebirle $(f \\circ f)(x)=\\dfrac{x-1}{x}$ ve $(f \\circ f \\circ f)(x)=x$ bulunur ($x \\neq 0$ ve $x \\neq 1$ için). Yani $f$ yi üç kez uygulamak her sayıyı yerine geri getirir.",
            hap("Tekrarlı bileşkede birkaç adım hesapla ve döngüyü ara.",
                "Döngü uzunluğu $p$ ise $n$ uygulama, $n$ nin $p$ ye bölümünden kalan kadar uygulamayla aynı sonucu verir."),
        ]},
        {"baslik": "Bileşke içeren denklemler", "icerik": [
            "Bileşke bir denklemin içinde de karşına çıkabilir. Yapılacak iş, her bileşkeyi önce açık kuralıyla yazmak, sonra bildiğin denklem çözme yollarını kullanmaktır.",
            ornek(
                "$f(x)=2x+1$ ve $g(x)=x^2$ olsun.",
                "$(f \\circ g)(x)=(g \\circ f)(x)$ denklemini sağlayan $x$ değerlerini bulalım.",
                "$(f \\circ g)(x)=2x^2+1$.",
                "$(g \\circ f)(x)=(2x+1)^2=4x^2+4x+1$.",
                "Eşitleyelim: $2x^2+1=4x^2+4x+1$, yani $2x^2+4x=0$ ve $2x(x+2)=0$.",
                "Çözümler $x=0$ ve $x=-2$ dir.",
                "Kontrol: $x=-2$ için $f(g(-2))=f(4)=9$ ve $g(f(-2))=g(-3)=9$."),
            "İki bileşke genel olarak eşit değildir, ama bazı $x$ değerlerinde aynı sonucu verebilir. Bu örnekte yalnızca iki noktada eşittirler.",
            ornek(
                "$f(x)=x+3$ olsun.",
                "$(f \\circ f \\circ f)(x)=20$ denklemini çözelim.",
                "$f$ her uygulamada $3$ ekler; üç uygulama $9$ ekler: $(f \\circ f \\circ f)(x)=x+9$.",
                "$x+9=20$ ve $x=11$."),
        ]},
        {"baslik": "Bileşke, birebirlik ve örtenlik", "icerik": [
            "Birebir iki fonksiyonun bileşkesi de birebirdir: $f(g(x_1))=f(g(x_2))$ ise $f$ birebir olduğu için $g(x_1)=g(x_2)$, $g$ birebir olduğu için de $x_1=x_2$ olur. Benzer biçimde örten iki fonksiyonun bileşkesi de örtendir.",
            "Bu iki sonuç birleşince önemli bir kural çıkar: birebir örten iki fonksiyonun bileşkesi de birebir örtendir ve tersi vardır. Tersi alınırken sıra döner:",
            "$$(f \\circ g)^{-1}=g^{-1} \\circ f^{-1}$$",
            "Sıranın neden döndüğünü görmek için giyinmeyi düşün: önce çorap, sonra ayakkabı giyilir. Çıkarırken önce ayakkabı, sonra çorap çıkar.",
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bileşke sayısal değer olarak karşına çıkabilir: iki fonksiyon verilir, $(f \\circ g)(2)$ gibi bir değer istenir. Tabloyla ya da şemayla verilmiş fonksiyonlarda da aynı hesap yapılır.",
                "İleri düzeyde (<strong>AYT</strong>) içteki ya da dıştaki fonksiyonun bulunması, bileşkenin tanım kümesi ve ters fonksiyonla birlikte kullanılan bileşke öne çıkar.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyine hazırlanıyorsan önce sayısal değer hesaplama, kural bulma ve dıştaki fonksiyonu bulma bölümlerine çalış; bu bölümler bir değeri art arda yerine koymanın temelini verir."),
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$(f \\circ g)(x)$ te önce $f$ yi uygulamak", "Önce sağdaki, yani $g$ çalışır"],
                ["$f \\circ g=g \\circ f$ sanmak", "Genel olarak eşit değildir"],
                ["$(f \\circ g)(x)$ i $f(x) \\cdot g(x)$ sanmak", "Bileşke çarpım değildir"],
                ["Yerine koyarken parantezi unutmak", "$f(2x-3)$ için $(2x-3)^2$"],
                ["Tanım kümesini sadeleşmiş kuraldan okumak", "İçteki fonksiyonun şartı da aranır"],
                ["Parçalı fonksiyonda aralığı tekrar kontrol etmemek", "Her adımda aralığa bakılır"],
                ["$(f \\circ g)^{-1}=f^{-1} \\circ g^{-1}$ yazmak", "Sıra döner: $g^{-1} \\circ f^{-1}$"],
            ]),
            "Bu hataların çoğu, bileşkeyi bir işlem sırası olarak değil de iki fonksiyonun yan yana yazılması olarak görmekten kaynaklanır. $f(g(x))$ biçimini her zaman açık açık yazmak bu hataları büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("Bileşke fonksiyonda hangi fonksiyon önce uygulanır?",
         "f bileşke g yazıldığında önce g uygulanır, çıkan sonuç f ye verilir. Yazılışta sağda duran fonksiyon önce çalışır."),
        ("f bileşke g ile g bileşke f eşit midir?",
         "Genel olarak eşit değildir. Bileşkede değişme özelliği yoktur. Bazı özel fonksiyon çiftlerinde eşit çıkabilirler ama bu bir kural değildir."),
        ("Bileşke fonksiyonun tanım kümesi nasıl bulunur?",
         "Önce içteki fonksiyonun tanım kümesi alınır. Sonra bu kümeden, içteki fonksiyonun değerini dıştaki fonksiyonun tanım kümesine düşüren elemanlar seçilir. Sadeleşmiş son kurala bakmak yeterli değildir."),
        ("f(2x+1) verilmişse f(x) nasıl bulunur?",
         "Parantezin içine yeni bir değişken adı verilir, örneğin t eşittir 2x artı 1. Buradan x, t cinsinden çekilir ve eşitlikte yerine yazılır. Çıkan ifadede t yerine x yazılınca f(x) bulunur."),
        ("Bileşkenin tersi nasıl alınır?",
         "f bileşke g nin tersi, g nin tersi bileşke f nin tersidir. Yani sıra döner. Bunun için f ve g nin ikisinin de birebir ve örten olması gerekir."),
        ("Bileşkede birleşme özelliği var mıdır?",
         "Evet. Üç fonksiyonun bileşkesinde parantezin yeri sonucu değiştirmez. Her iki durumda da önce en sağdaki, sonra ortadaki, en son en soldaki fonksiyon uygulanır."),
        ("Bileşke fonksiyon ile iki fonksiyonun çarpımı aynı şey midir?",
         "Hayır. Çarpımda iki fonksiyonun değerleri çarpılır. Bileşkede ise bir fonksiyonun değeri öteki fonksiyona girdi olarak verilir. Örneğin f(x) eşittir x artı 1 ve g(x) eşittir 2x için çarpım 2x kare artı 2x, f bileşke g ise 2x artı 1 dir."),
    ],
    "kontrol": [
        "$(f \\circ g)(a)$ değerini içten dışa doğru hesaplayabiliyorum.",
        "Tabloyla verilmiş iki fonksiyonun bileşkesini eleman eleman yazabiliyorum.",
        "$f(g(x))$ kuralını parantez kullanarak doğru biçimde bulabiliyorum.",
        "Bileşkenin tanım kümesini içteki ve dıştaki fonksiyonun şartlarıyla bulabiliyorum.",
        "$f \\circ g \\neq g \\circ f$ olduğunu bir örnekle gösterebiliyorum.",
        "$f$ ve $f \\circ g$ verildiğinde $g$ yi bulup geri yerine koyarak kontrol edebiliyorum.",
        "$f(ax+b)$ biçiminde verilen eşitlikten $f(x)$ i yeni değişkenle bulabiliyorum.",
        "Yalnızca bir değer istendiğinde parantezin içini o sayıya eşitleyerek sonuca gidebiliyorum.",
        "Parçalı fonksiyonda her adımda hangi kuralın geçerli olduğunu kontrol ediyorum.",
        "Tekrarlı bileşkede döngüyü bulup kalan yardımıyla sonucu hesaplayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birebir-orten-fonksiyon", "ters-fonksiyon", "tanim-deger-goruntu-kumeleri"],
}
