# scripts/yazilar/70_kesir_carpma.py — Kesirlerde Carpma ve Bolme (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kesirlerde-carpma-ve-bolme",
    "baslik": "Kesirlerde Çarpma ve Bölme",
    "aciklama": "Kesirlerde çarpma ve bölme nasıl yapılır? Parçanın parçası, çapraz sadeleştirme, çarpmaya göre ters, merdiven kesirler, kesirlerde üs ve problemler.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kesirlerde-carpma-ve-bolme",
    "kapak_alt": "Kesirlerde çarpma ve bölme: şeffaf mavi ve kırmızı ızgaraları üst üste koyarak parçanın parçasını gösteren iki öğrenci",
    "ozet": "Kesirlerde çarpma, toplamadan daha kolay görünür: paylar çarpılır, paydalar çarpılır. Ama bu kuralın arkasında güçlü bir fikir vardır: bir kesirle çarpmak, bir şeyin bir parçasını almaktır. Bölme ise bir miktarın içine başka bir miktarın kaç kez sığdığını sorar. Bu yazıda iki işlemi modelleriyle birlikte anlatıyor, işlemden önce sadeleştirmeyi, tam sayılı kesirleri, çarpmaya göre tersi, merdiven kesirleri, kesirlerde üs almayı ve problemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kesirle tam sayıyı çarpmak", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesir kavramını, sadeleştirmeyi ve EBOB'u biliyor olman yeterli.",
                "Kesirlerin temeli için <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a> yazısına göz at."),
            "Tam sayılarda çarpma tekrarlı toplamadır; kesirlerde de öyle başlar. $3 \\cdot \\dfrac{2}{5}$, üç tane $\\dfrac{2}{5}$ nin toplamıdır:",
            "$$3 \\cdot \\dfrac{2}{5}=\\dfrac{2}{5}+\\dfrac{2}{5}+\\dfrac{2}{5}=\\dfrac{6}{5}$$",
            "Kısaca: tam sayı kesrin payıyla çarpılır, payda aynen kalır. Tam sayıyı paydası $1$ olan bir kesir olarak yazarsan bu, genel çarpma kuralının özel bir hâlidir: $\\dfrac{3}{1} \\cdot \\dfrac{2}{5}=\\dfrac{6}{5}$.",
        ]},
        {"baslik": "Kesirle kesri çarpmak: parçanın parçası", "icerik": [
            "İki kesir çarpılırken <strong>paylar çarpılıp paya</strong>, <strong>paydalar çarpılıp paydaya</strong> yazılır:",
            "$$\\dfrac{a}{b} \\cdot \\dfrac{c}{d}=\\dfrac{a \\cdot c}{b \\cdot d}$$",
            "Bu kuralın anlamı, \"bir kesrin kesri\" fikridir. $\\dfrac{2}{3} \\cdot \\dfrac{3}{4}$, dörtte üçün üçte ikisi demektir. Bir kareyi dikey çizgilerle $4$ eş şeride bölüp $3$ ünü boyadığını düşün. Sonra aynı kareyi yatay çizgilerle $3$ eş şeride bölüp boyalı kısmın $2$ şeridini tekrar işaretle. Kare toplam $4 \\cdot 3=12$ küçük parçaya bölünmüştür ve iki kez işaretlenen parça sayısı $3 \\cdot 2=6$ dır:",
            "$$\\dfrac{2}{3} \\cdot \\dfrac{3}{4}=\\dfrac{6}{12}=\\dfrac{1}{2}$$",
            "Bu yüzden Türkçede \"-nın\" eki çarpma anlamına gelir: bir sayının $\\dfrac{3}{4}$ ü, o sayının $\\dfrac{3}{4}$ ile çarpımıdır.",
            ornek(
                "$\\dfrac{2}{5}$ nin $\\dfrac{3}{4}$ ü sorulsun.",
                "Değerini bulalım.",
                "\"-in\" eki çarpma demektir: $\\dfrac{3}{4} \\cdot \\dfrac{2}{5}$.",
                "Payları ve paydaları çarpalım: $\\dfrac{6}{20}=\\dfrac{3}{10}$."),
            hap("Kesirlerde çarpma: pay pay ile, payda payda ile çarpılır.",
                "Bir sayının kesri, o sayının kesirle çarpımıdır."),
        ]},
        {"baslik": "Çarpmadan önce sadeleştirmek", "icerik": [
            "Çarpımı hesaplayıp sonra sadeleştirmek büyük sayılarla uğraşmayı gerektirir. Bunun yerine çarpmadan önce, bir kesrin payı ile herhangi bir kesrin paydası arasında ortak çarpan varsa sadeleştirme yapılabilir. Buna <strong>çapraz sadeleştirme</strong> denir. Çarpım tek bir kesir gibi davrandığı için bu işlem sonucu değiştirmez.",
            ornek(
                "$\\dfrac{14}{15} \\cdot \\dfrac{25}{28}$ çarpımı verilsin.",
                "Çarpmadan önce sadeleştirerek bulalım.",
                "$14$ ile $28$ i $14$ e bölelim: $1$ ve $2$.",
                "$25$ ile $15$ i $5$ e bölelim: $5$ ve $3$.",
                "Kalan çarpım: $\\dfrac{1 \\cdot 5}{3 \\cdot 2}=\\dfrac{5}{6}$.",
                "Kontrol: $\\dfrac{350}{420}=\\dfrac{5}{6}$."),
            dikkat(
                "Çapraz sadeleştirme yalnızca çarpmada yapılır.",
                "$\\dfrac{2}{3}+\\dfrac{3}{4}$ toplamında $3$ ler sadeleştirilemez. Toplamada kesirler önce ortak paydaya getirilir."),
            hap("Çarpmadan önce bir payla herhangi bir payda arasındaki ortak çarpan sadeleştirilir.", "Bu çapraz sadeleştirme yalnız çarpmada yapılır, toplamada yapılmaz."),
        ]},
        {"baslik": "Tam sayılı kesirlerde çarpma", "icerik": [
            "Tam sayılı kesirler çarpılmadan önce <strong>bileşik kesre</strong> çevrilir. Tam kısımları ve kesir kısımlarını ayrı ayrı çarpmak yanlış sonuç verir.",
            ornek(
                "$2\\dfrac{1}{2} \\cdot 1\\dfrac{1}{3}$ çarpımı verilsin.",
                "Çarpımı bulalım.",
                "Bileşik kesre çevirelim: $2\\dfrac{1}{2}=\\dfrac{5}{2}$ ve $1\\dfrac{1}{3}=\\dfrac{4}{3}$.",
                "Çarpalım: $\\dfrac{5}{2} \\cdot \\dfrac{4}{3}=\\dfrac{20}{6}=\\dfrac{10}{3}$.",
                "Tam sayılı olarak: $3\\dfrac{1}{3}$."),
            dikkat(
                "Tam kısımları ve kesirleri ayrı çarpma.",
                "$2 \\cdot 1+\\dfrac{1}{2} \\cdot \\dfrac{1}{3}=2\\dfrac{1}{6}$ yazmak yanlıştır; doğru sonuç $3\\dfrac{1}{3}$ dir. Tam sayılı kesir bir toplamdır ve toplamların çarpımında her terim diğer her terimle çarpılmalıdır."),
        ]},
        {"baslik": "Çarpınca büyür mü, küçülür mü?", "icerik": [
            "Tam sayılarda çarpmanın sonucu büyütür diye düşünülür. Kesirlerde bu her zaman doğru değildir. Pozitif bir sayı:",
            "<ul><li>$1$ den <strong>küçük</strong> pozitif bir kesirle çarpılırsa <strong>küçülür</strong>: $12 \\cdot \\dfrac{3}{4}=9$.</li>"
            "<li>$1$ den <strong>büyük</strong> bir kesirle çarpılırsa <strong>büyür</strong>: $12 \\cdot \\dfrac{5}{4}=15$.</li>"
            "<li>$1$ ile çarpılırsa değişmez.</li></ul>",
            "Negatif kesirlerde tam sayılardaki işaret kuralları aynen geçerlidir: farklı işaretli iki kesrin çarpımı negatif, aynı işaretli iki kesrin çarpımı pozitiftir. Örneğin $-\\dfrac{2}{3} \\cdot \\dfrac{3}{4}=-\\dfrac{1}{2}$ ve $\\left(-\\dfrac{2}{3}\\right) \\cdot \\left(-\\dfrac{3}{4}\\right)=\\dfrac{1}{2}$ dir.",
            "Nedeni \"parçanın parçası\" fikrindedir: $\\dfrac{3}{4}$ ile çarpmak, sayının dörtte üçünü almaktır ve bu sayının kendisinden azdır. Bölmede ise durum tersine döner; bunu aşağıda göreceğiz.",
            hap("Pozitif bir sayı $1$ den küçük pozitif bir kesirle çarpılırsa küçülür, $1$ den büyük bir kesirle çarpılırsa büyür."),
        ]},
        {"baslik": "Çarpmaya göre ters", "icerik": [
            "Çarpımları $1$ olan iki sayıya birbirinin <strong>çarpmaya göre tersi</strong> denir. Sıfırdan farklı bir kesrin tersi, pay ile paydanın yer değiştirmesiyle bulunur:",
            "$$\\dfrac{a}{b} \\cdot \\dfrac{b}{a}=1$$",
            "Örneğin $\\dfrac{3}{7}$ ün tersi $\\dfrac{7}{3}$, $5$ in tersi $\\dfrac{1}{5}$, $-\\dfrac{2}{9}$ nin tersi $-\\dfrac{9}{2}$ dur. Tersin işareti sayının işaretiyle aynıdır.",
            dikkat(
                "Sıfırın çarpmaya göre tersi yoktur.",
                "Sıfır hangi sayıyla çarpılırsa çarpılsın sonuç sıfırdır, hiçbir zaman $1$ olmaz. $\\dfrac{0}{1}$ ın pay ve paydası yer değiştirse $\\dfrac{1}{0}$ elde edilirdi ve bu tanımsızdır."),
        ]},
        {"baslik": "Kesirlerde bölme", "icerik": [
            "Kesirlerde bölme, çarpmaya dönüştürülerek yapılır: bölünen aynen yazılır, bölen <strong>ters çevrilir</strong> ve çarpılır.",
            "$$\\dfrac{a}{b}:\\dfrac{c}{d}=\\dfrac{a}{b} \\cdot \\dfrac{d}{c}=\\dfrac{a \\cdot d}{b \\cdot c}$$",
            "<h3>Kural nereden geliyor?</h3>",
            "Bölme, \"içine kaç kez sığar\" sorusudur. $1:\\dfrac{1}{4}$ işleminde bir bütünün içine kaç tane dörtte bir sığdığı sorulur: $4$ tane. Yani $\\dfrac{1}{4}$ e bölmek, $4$ ile çarpmakla aynıdır. Genel olarak bir kesre bölmek, o kesrin tersiyle çarpmaktır.",
            "Başka bir açıklama da şudur: bölme, çarpmanın tersidir. $\\dfrac{a}{b}:\\dfrac{c}{d}=x$ ise $x \\cdot \\dfrac{c}{d}=\\dfrac{a}{b}$ olmalıdır. İki tarafı $\\dfrac{d}{c}$ ile çarpınca $x=\\dfrac{a}{b} \\cdot \\dfrac{d}{c}$ bulunur.",
            ornek(
                "$\\dfrac{3}{4}:\\dfrac{2}{5}$ işlemi verilsin.",
                "Sonucu bulalım.",
                "Böleni ters çevirip çarpalım: $\\dfrac{3}{4} \\cdot \\dfrac{5}{2}$.",
                "Sonuç: $\\dfrac{15}{8}=1\\dfrac{7}{8}$."),
            ornek(
                "$\\dfrac{6}{7}:3$ ve $4:\\dfrac{2}{3}$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "$3$ ün tersi $\\dfrac{1}{3}$: $\\dfrac{6}{7} \\cdot \\dfrac{1}{3}=\\dfrac{2}{7}$.",
                "$\\dfrac{2}{3}$ nin tersi $\\dfrac{3}{2}$: $4 \\cdot \\dfrac{3}{2}=6$. Bir $4$ metrelik ipten $\\dfrac{2}{3}$ metrelik $6$ parça çıkar."),
            dikkat(
                "Ters çevrilen bölendir, bölünen değil.",
                "$\\dfrac{3}{4}:\\dfrac{2}{5}$ işleminde $\\dfrac{4}{3} \\cdot \\dfrac{2}{5}$ yazmak yanlıştır. Yalnızca ikinci kesir, yani bölen ters çevrilir."),
            "Çarpmadaki kuralın tersi burada da geçerlidir: pozitif bir sayı $1$ den küçük pozitif bir kesre bölünürse <strong>büyür</strong>. $12:\\dfrac{3}{4}=16$ dır; $12$ nin içine dörtte üçlük $16$ parça sığar.",
            hap("Kesirlerde bölme: bölüneni aynen yaz, böleni ters çevir, çarp.",
                "Pozitif bir sayı $1$ den küçük pozitif bir kesre bölününce büyür."),
        ]},
        {"baslik": "Bölmede ortak payda yöntemi", "icerik": [
            "Kesirlerde bölmenin bir yolu daha vardır: iki kesir aynı paydaya getirilirse bölme işlemi yalnızca payların bölümüne dönüşür. Çünkü aynı büyüklükteki parçalardan kaç tanesinin sığdığı, parça sayılarının oranıdır.",
            ornek(
                "$\\dfrac{3}{4}:\\dfrac{1}{8}$ işlemi verilsin.",
                "Ortak payda yöntemiyle bulalım.",
                "Aynı paydaya getirelim: $\\dfrac{6}{8}:\\dfrac{1}{8}$.",
                "Altı tane sekizde birin içinde bir tane sekizde bir altı kez vardır: $6:1=6$.",
                "Kontrol: ters çevirerek $\\dfrac{3}{4} \\cdot 8=6$."),
            "Bu yöntem bölmenin \"kaç tane sığar\" anlamını açıkça gösterir. Hesap açısından ise ters çevirip çarpmak çoğu durumda daha kısadır; iki yol aynı sonucu verir.",
        ]},
        {"baslik": "Çarpmanın özellikleri", "icerik": [
            "Kesirlerde çarpma da tam sayılardaki özelliklere sahiptir. <strong>Değişme</strong>: çarpanların yeri değiştirilebilir. <strong>Birleşme</strong>: çarpanlar istenen sırayla gruplanabilir. <strong>Dağılma</strong>: bir kesir, parantez içindeki toplamın her terimiyle ayrı ayrı çarpılabilir. Bu özellikler, uygun gruplama yaparak hesabı kısaltmayı sağlar.",
            ornek(
                "$\\dfrac{4}{7} \\cdot 14+\\dfrac{4}{7} \\cdot 7$ işlemi verilsin.",
                "Dağılma özelliğiyle kısa yoldan bulalım.",
                "Ortak çarpan $\\dfrac{4}{7}$ ü dışarı alalım: $\\dfrac{4}{7} \\cdot (14+7)=\\dfrac{4}{7} \\cdot 21$.",
                "$21:7=3$ ve $4 \\cdot 3=12$."),
            ornek(
                "$\\dfrac{5}{9} \\cdot \\dfrac{7}{11} \\cdot \\dfrac{9}{5}$ çarpımı verilsin.",
                "Birleşme ve değişme özelliğiyle bulalım.",
                "Birbirinin tersi olan çarpanları yan yana getirelim: $\\left(\\dfrac{5}{9} \\cdot \\dfrac{9}{5}\\right) \\cdot \\dfrac{7}{11}$.",
                "Parantez $1$ eder; sonuç $\\dfrac{7}{11}$."),
        ]},
        {"baslik": "Ondalık sayılar ve harfli kesirler", "icerik": [
            "Ondalık sayılarla kesirler çarpılırken ondalık sayıyı kesre çevirmek sadeleştirmeyi kolaylaştırır. Harfli kesirlerde de aynı kurallar geçerlidir; yalnızca paydadaki harfin sıfır olmaması gerekir.",
            ornek(
                "$0.6 \\cdot \\dfrac{5}{9}$ çarpımı ile $x \\neq 0$ için $\\dfrac{x}{2} \\cdot \\dfrac{4}{x}$ verilsin.",
                "İkisini de sadeleştirerek bulalım.",
                "$0.6=\\dfrac{3}{5}$: $\\dfrac{3}{5} \\cdot \\dfrac{5}{9}=\\dfrac{3}{9}=\\dfrac{1}{3}$.",
                "$\\dfrac{x}{2} \\cdot \\dfrac{4}{x}=\\dfrac{4x}{2x}=2$; $x$ ler sadeleşir."),
            "Harfli bölmede de ters çevirme kuralı işler: $a$, $b$ ve $c$ sıfırdan farklıyken $\\dfrac{a}{b}:\\dfrac{a}{c}=\\dfrac{a}{b} \\cdot \\dfrac{c}{a}=\\dfrac{c}{b}$ olur.",
        ]},
        {"baslik": "Bölmenin sonucunu çarpmayla kontrol etmek", "icerik": [
            "Bölme, çarpmanın tersi olduğu için her bölmenin sonucu bir çarpmayla kontrol edilebilir: bölüm ile bölen çarpılınca bölünen elde edilmelidir. Bu kontrol birkaç saniye sürer ve ters çevirme hatalarını hemen yakalar.",
            ornek(
                "$\\dfrac{3}{4}:\\dfrac{2}{5}=\\dfrac{15}{8}$ sonucu bulunmuş olsun.",
                "Sonucu çarpmayla kontrol edelim.",
                "Bölüm ile böleni çarpalım: $\\dfrac{15}{8} \\cdot \\dfrac{2}{5}=\\dfrac{30}{40}=\\dfrac{3}{4}$.",
                "Bölünen elde edildi; sonuç doğrudur."),
            "Aynı kontrol yanlış bir sonuçta işe yarar: bölünen yanlışlıkla ters çevrilip $\\dfrac{4}{3} \\cdot \\dfrac{2}{5}=\\dfrac{8}{15}$ bulunmuş olsaydı, $\\dfrac{8}{15} \\cdot \\dfrac{2}{5}=\\dfrac{16}{75}$ çıkar ve bu $\\dfrac{3}{4}$ değildir.",
        ]},
        {"baslik": "Yüzde ile kesir çarpımı", "icerik": [
            "Yüzdeler, paydası $100$ olan kesirlerdir. Bir yüzdenin kesri ya da bir kesrin yüzdesi sorulduğunda ikisi de kesre çevrilip çarpılır.",
            ornek(
                "Bir sınıftaki öğrencilerin yüzde $40$ ı spor kulübüne üye ve bu üyelerin $\\dfrac{3}{4}$ ü futbol oynuyor.",
                "Sınıfın yüzde kaçı futbol oynar?",
                "Yüzde $40$, $\\dfrac{40}{100}=\\dfrac{2}{5}$ dir.",
                "Futbol oynayanlar: $\\dfrac{3}{4} \\cdot \\dfrac{2}{5}=\\dfrac{6}{20}=\\dfrac{3}{10}$.",
                "Bu, sınıfın yüzde $30$ udur. Kontrol: $20$ kişilik bir sınıfta $8$ üye olur ve bunların $6$ sı futbol oynar; $6$, $20$ nin yüzde $30$ udur."),
        ]},
        {"baslik": "Merdiven kesirler", "icerik": [
            "Payında ya da paydasında başka kesirler bulunan kesirlere <strong>merdiven kesir</strong> denir. Ana kesir çizgisi bir bölme işaretidir; üst kısım alt kısma bölünür.",
            ornek(
                "$\\dfrac{\\dfrac{1}{2}}{\\dfrac{3}{4}}$ kesri verilsin.",
                "Değerini bulalım.",
                "Ana kesir çizgisi bölme demektir: $\\dfrac{1}{2}:\\dfrac{3}{4}$.",
                "Böleni ters çevirip çarpalım: $\\dfrac{1}{2} \\cdot \\dfrac{4}{3}=\\dfrac{4}{6}=\\dfrac{2}{3}$."),
            "Merdiven uzunsa en alttan başlanır ve yukarı doğru çıkılır. Her adımda yalnızca bir kesir sadeleştirilir.",
            ornek(
                "$\\dfrac{1}{1+\\dfrac{1}{1+\\dfrac{1}{2}}}$ kesri verilsin.",
                "Değerini bulalım.",
                "En alttan başlayalım: $1+\\dfrac{1}{2}=\\dfrac{3}{2}$.",
                "Bir üst basamak: $\\dfrac{1}{\\dfrac{3}{2}}=\\dfrac{2}{3}$ ve $1+\\dfrac{2}{3}=\\dfrac{5}{3}$.",
                "En üst: $\\dfrac{1}{\\dfrac{5}{3}}=\\dfrac{3}{5}$."),
            "Merdiven kesirlerde işlem sırası için <a href=\"/blog/islem-onceligi-nasil-yapilir/\">İşlem Önceliği Nasıl Yapılır?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kesirlerde üs", "icerik": [
            "Bir kesrin kuvveti alınırken hem pay hem payda o kuvvete yükseltilir, çünkü kuvvet tekrarlı çarpmadır ve kesirlerde çarpma pay pay ile, payda payda ile yapılır:",
            "$$\\left(\\dfrac{a}{b}\\right)^n=\\dfrac{a^n}{b^n}$$",
            ornek(
                "$\\left(\\dfrac{2}{3}\\right)^3$ ve $\\left(\\dfrac{3}{2}\\right)^{-2}$ verilsin.",
                "Değerlerini bulalım.",
                "$\\left(\\dfrac{2}{3}\\right)^3=\\dfrac{2^3}{3^3}=\\dfrac{8}{27}$.",
                "Negatif üs kesri ters çevirir: $\\left(\\dfrac{3}{2}\\right)^{-2}=\\left(\\dfrac{2}{3}\\right)^2=\\dfrac{4}{9}$."),
            "$0$ ile $1$ arasındaki bir kesrin kuvveti alındıkça sayı küçülür: $\\dfrac{1}{2}$, $\\dfrac{1}{4}$, $\\dfrac{1}{8}$, $\\ldots$ Üslü sayıların kuralları için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Kesirlerde çarpma ve bölme problemleri", "icerik": [
            "Problemlerde \"-nın\" eki ve \"kaç tane sığar\" soruları işlemi belirler: birincisi çarpma, ikincisi bölmedir.",
            ornek(
                "$6$ metrelik bir kumaşın $\\dfrac{3}{4}$ ü, her biri $\\dfrac{3}{8}$ metre olan parçalara bölünüyor.",
                "Kaç parça elde edilir?",
                "Kullanılan kumaş: $6 \\cdot \\dfrac{3}{4}=\\dfrac{9}{2}$ metre.",
                "Parça sayısı: $\\dfrac{9}{2}:\\dfrac{3}{8}=\\dfrac{9}{2} \\cdot \\dfrac{8}{3}=12$."),
            ornek(
                "Bir tarif $4$ kişilik ve $\\dfrac{2}{3}$ bardak şeker gerektiriyor.",
                "Aynı tarif $10$ kişi için kaç bardak şeker gerektirir?",
                "Kişi başına şeker: $\\dfrac{2}{3}:4=\\dfrac{2}{3} \\cdot \\dfrac{1}{4}=\\dfrac{1}{6}$ bardak.",
                "$10$ kişi için: $10 \\cdot \\dfrac{1}{6}=\\dfrac{5}{3}=1\\dfrac{2}{3}$ bardak."),
            ornek(
                "Bir sayının $\\dfrac{2}{5}$ sinin $\\dfrac{3}{4}$ ü $18$ olsun.",
                "Sayıyı bulalım.",
                "Sayının $\\dfrac{3}{4} \\cdot \\dfrac{2}{5}=\\dfrac{3}{10}$ ü $18$ dir.",
                "Sayı: $18:\\dfrac{3}{10}=18 \\cdot \\dfrac{10}{3}=60$."),
            "Son örnekte olduğu gibi \"kesrin kesri\" soruları, kesirleri çarparak tek bir kesre indirgenir ve sonra kesri verilen çokluk bulunur.",
        ]},
        {"baslik": "Çarpma mı bölme mi? Problemin dilini okumak", "icerik": [
            "Kesir problemlerinde asıl zorluk hesap değil, hangi işlemin yapılacağına karar vermektir. Problemin dilindeki bazı ifadeler bu kararı verir:",
            tablo(["İfade", "İşlem", "Örnek"], [
                ["\"...nın kesri\"", "Çarpma", "$60$ ın $\\dfrac{2}{3}$ si: $60 \\cdot \\dfrac{2}{3}=40$"],
                ["\"Kaç tane sığar\"", "Bölme", "$3$ metrede kaç $\\dfrac{3}{4}$ metre: $4$"],
                ["\"Kişi başına\"", "Bölme", "$\\dfrac{3}{5}$ kilo, $3$ kişiye: $\\dfrac{1}{5}$ kilo"],
                ["\"Kesri verilen bütün\"", "Bölme", "$\\dfrac{2}{3}$ si $40$ olan: $60$"],
            ]),
            "Emin olamadığında sonucun büyüklüğünü düşün: bir bütünün parçası sorulduysa sonuç bütünden küçük olmalıdır ve bu çarpmayı gösterir. Bir parçadan bütüne gidiliyorsa sonuç parçadan büyük olmalıdır ve bu bölmeyi gösterir.",
            ornek(
                "Bir araç saatte $60$ kilometre hızla gidiyor.",
                "$\\dfrac{3}{4}$ saatte kaç kilometre yol alır? $90$ kilometreyi kaç saatte alır?",
                "Yol, hız ile sürenin çarpımıdır: $60 \\cdot \\dfrac{3}{4}=45$ kilometre.",
                "Süre, yolun hıza bölümüdür: $90:60=\\dfrac{3}{2}$ saat, yani $1$ saat $30$ dakika."),
            hap("$3$ litre ayranla yarım litrelik şişelerden $3:\\dfrac{1}{2}=6$ tane doldurulur.", "Kaç tane sığar sorusu bir bölmedir.", gunluk=True),
        ]},
        {"baslik": "Sınavda kesirlerde çarpma ve bölme", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu işlem sorusu, merdiven kesir, kesrin kesri ve parça sayısı problemleri biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde kesirlerle çarpma ve bölme, oran, tarif ve iş problemleri gibi soruların içinde de gerekebilir."),
            "Uzun işlemlerde önce bütün bölmeleri çarpmaya çevirmek, sonra tek bir kesir çizgisi altında bütün payları ve paydaları yazıp çapraz sadeleştirme yapmak, adım adım hesaplamaktan hem daha hızlı hem daha güvenlidir.",
            "İşlem sorularında en büyük zaman kazancı çarpmadan önce sadeleştirmektir. Sonucu kontrol etmek için de büyüme ve küçülme kuralını kullanabilirsin: $1$ den küçük bir kesirle çarpınca sonuç küçülmeli, $1$ den küçük bir kesre bölünce büyümelidir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Çarpmada ortak payda aramak", "Pay pay ile, payda payda ile"],
                ["Bölmede bölüneni ters çevirmek", "Böleni ters çevir"],
                ["Tam sayılı kesirleri parça parça çarpmak", "Önce bileşik kesre çevir"],
                ["Toplamada çapraz sadeleştirmek", "Yalnız çarpmada"],
                ["Sıfırın tersini $\\dfrac{1}{0}$ yazmak", "Sıfırın tersi yoktur"],
                ["Çarpma hep büyütür sanmak", "$1$ den küçük kesir küçültür"],
            ]),
            "Bu hataların ortak noktası, toplama ve çarpmanın kurallarını birbirine karıştırmaktır. Toplamada ortak payda gerekir, çarpmada gerekmez; çarpmada çapraz sadeleştirme yapılır, toplamada yapılmaz.",
        ]},
    ],
    "sss": [
        ("Kesirlerde çarpma nasıl yapılır?",
         "Paylar çarpılıp paya, paydalar çarpılıp paydaya yazılır. Çarpmadan önce çapraz sadeleştirme yapmak sayıları küçük tutar."),
        ("Kesirlerde bölme nasıl yapılır?",
         "Bölünen aynen yazılır, bölen ters çevrilir ve iki kesir çarpılır."),
        ("Bir kesre bölmek neden tersiyle çarpmaktır?",
         "Bölme, bir miktarın içine başka bir miktarın kaç kez sığdığını sorar. Örneğin bir bütünün içine dört tane dörtte bir sığar; dörtte bire bölmek dört ile çarpmakla aynıdır."),
        ("Kesirlerde bölmenin sonucu nasıl kontrol edilir?",
         "Bulunan bölüm bölenle çarpılır. Sonuç bölüneni veriyorsa bölme doğrudur; vermiyorsa büyük olasılıkla yanlış kesir ters çevrilmiştir."),
        ("Çarpmaya göre ters ne demektir?",
         "Çarpımları 1 olan iki sayı birbirinin çarpmaya göre tersidir. Sıfırdan farklı bir kesrin tersi pay ile paydanın yer değiştirmesiyle bulunur; sıfırın tersi yoktur."),
        ("Kesir problemlerinde çarpma mı bölme mi yapılacağı nasıl anlaşılır?",
         "Bir bütünün kesri soruluyorsa çarpma, bir miktarın içine kaç tane sığdığı ya da kesri verilen bütün soruluyorsa bölme yapılır. Sonucun büyüklüğünü tahmin etmek de doğru işlemi gösterir."),
        ("Tam sayılı kesirler nasıl çarpılır?",
         "Önce bileşik kesre çevrilir, sonra paylar ve paydalar çarpılır. Tam kısımları ve kesir kısımlarını ayrı çarpmak yanlış sonuç verir."),
        ("Bir sayıyı kesirle çarpınca sayı neden küçülebilir?",
         "Birden küçük pozitif bir kesirle çarpmak sayının bir parçasını almak demektir ve parça bütünden küçüktür."),
    ],
    "kontrol": [
        "Kesirle tam sayı çarpımını tekrarlı toplama olarak açıklayabiliyorum.",
        "İki kesrin çarpımını parçanın parçası modeliyle gösterebiliyorum.",
        "Bir sayının kesrini çarpma olarak yazabiliyorum.",
        "Çarpmadan önce çapraz sadeleştirme yapabiliyorum.",
        "Tam sayılı kesirleri bileşik kesre çevirip çarpabiliyorum.",
        "Bir kesirle çarpınca sonucun büyüyüp küçüleceğini önceden söyleyebiliyorum.",
        "Bir kesrin çarpmaya göre tersini bulabiliyorum ve sıfırın tersi olmadığını biliyorum.",
        "Kesirlerde bölmeyi böleni ters çevirerek yapabiliyorum.",
        "Merdiven kesirleri en alttan başlayarak sadeleştirebiliyorum.",
        "Kesrin kesri problemlerini tek bir kesre indirgeyerek çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kesirlerde-toplama-ve-cikarma", "kesirler-konu-anlatimi-pdf", "islem-onceligi-nasil-yapilir"],
}
