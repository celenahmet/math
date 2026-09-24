# scripts/yazilar/56_tek_cift.py — Tek ve Cift Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "tek-ve-cift-sayilar",
    "baslik": "Tek ve Çift Sayılar",
    "aciklama": "Tek ve çift sayılar nedir? Toplama, çarpma, kuvvet ve bölmede tek-çift kuralları, ifadelerin paritesi ve sayma problemleri; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "tek-ve-cift-sayilar",
    "kapak_alt": "Tek ve çift sayılar: mavi bilyeleri ikişerli gruplara ayırarak eşleşmeyen bilyeyi gösteren iki öğrenci",
    "ozet": "Bir sayının tek mi çift mi olduğu, ilk bakışta en basit bilgi gibi görünür. Oysa bu tek bilgiyle, sayının kendisini hiç bilmeden bir toplamın, bir çarpımın ya da bir denklemin sonucu hakkında kesin karar verebilirsin. Bu yazıda tek ve çift sayıları tanımlıyor, toplama, çarpma, kuvvet ve bölmedeki kurallarını gerekçeleriyle veriyor, ifadelerin tek-çift durumunu ve sayma problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Tek ve çift sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için tam sayıları ve dört işlemi biliyor olman yeterli.",
                "Temel kavramların genel özeti için <a href=\"/blog/temel-kavramlar-konu-anlatimi-pdf/\">Temel Kavramlar Konu Anlatımı PDF</a> yazısına göz at."),
            "$2$ ile tam bölünebilen tam sayılara <strong>çift sayı</strong>, $2$ ile bölündüğünde $1$ kalanını veren tam sayılara <strong>tek sayı</strong> denir. $k$ bir tam sayı olmak üzere:",
            "$$\\text{Çift sayı}=2k \\ \\ \\ \\ \\ \\ \\text{Tek sayı}=2k+1$$",
            "Bu tanım bütün tam sayıları kapsar. $0=2 \\cdot 0$ olduğu için $0$ çifttir. Negatif sayılar da ikiye ayrılır: $-6=2 \\cdot (-3)$ çift, $-7=2 \\cdot (-4)+1$ tektir.",
            "Bir sayının tek ya da çift olma durumuna <strong>parite</strong> denir. Bu yazıda sık kullanacağımız bir kelime: iki sayının paritesi aynıysa ikisi de tek ya da ikisi de çifttir.",
            "Somut bir düşünme yolu şudur: bir grup nesneyi ikişer ikişer eşleştir. Hiç nesne artmıyorsa sayı çift, bir nesne artıyorsa tektir.",
            hap("Çift sayı $2k$, tek sayı $2k+1$ biçimindedir.",
                "$0$ çift sayıdır; negatif sayılar da tek ya da çifttir."),
        ]},
        {"baslik": "Bir sayının paritesini anlamak", "icerik": [
            "Bir sayının tek mi çift mi olduğunu anlamak için sayının tamamına bakmak gerekmez. Yalnızca <strong>birler basamağına</strong> bakmak yeter: birler basamağı $0, 2, 4, 6, 8$ ise sayı çift, $1, 3, 5, 7, 9$ ise tektir.",
            "Bunun sebebi, onlar basamağından itibaren bütün basamakların $10$ un katı olmasıdır. $10$ çift olduğu için bu kısım her zaman çifttir; sayının paritesini yalnızca birler basamağı belirler.",
            ornek(
                "$3457218$, $-135$ ve $10^6+7$ sayıları verilsin.",
                "Hangileri tek, hangileri çift?",
                "$3457218$ in birler basamağı $8$: çift.",
                "$-135$ in birler basamağı $5$: tek. İşaret paritesini değiştirmez.",
                "$10^6$ çifttir, üzerine $7$ eklenince toplam tek olur: $10^6+7$ tektir."),
        ]},
        {"baslik": "Toplama ve çıkarmada tek ve çift", "icerik": [
            "İki sayının toplamı ya da farkı için kural şudur:",
            tablo(["İşlem", "Sonuç"], [
                ["$\\text{Tek} \\pm \\text{Tek}$", "Çift"],
                ["$\\text{Tek} \\pm \\text{Çift}$", "Tek"],
                ["$\\text{Çift} \\pm \\text{Çift}$", "Çift"],
            ]),
            "Kuralın gerekçesi tanımdan çıkar. İki tek sayı $2a+1$ ve $2b+1$ olsun. Toplamları $2a+2b+2=2(a+b+1)$ olur ve bu $2$ nin katıdır; yani çifttir.",
            "Toplamda ikiden fazla terim olduğunda her terime tek tek bakmak gerekmez. Çift terimler toplamın paritesini değiştirmez; önemli olan kaç tane tek terim olduğudur.",
            hap("Bir toplamın paritesi, içindeki <strong>tek terimlerin sayısına</strong> bağlıdır.",
                "Tek sayıda tek terim varsa toplam tek, çift sayıda tek terim varsa toplam çifttir."),
            ornek(
                "$1+2+3+\\cdots+10$ ve $1+2+3+\\cdots+100$ toplamları verilsin.",
                "Toplamları hesaplamadan tek mi çift mi olduklarını bulalım.",
                "$1$ den $10$ a kadar $5$ tek sayı var. Tek terim sayısı tek olduğu için toplam tektir. Kontrol: toplam $55$.",
                "$1$ den $100$ e kadar $50$ tek sayı var. Tek terim sayısı çift olduğu için toplam çifttir. Kontrol: toplam $5050$."),
        ]},
        {"baslik": "Çarpmada tek ve çift", "icerik": [
            "Çarpmanın kuralı toplamadan daha basittir: çarpanlardan <strong>en az biri</strong> çiftse çarpım çifttir. Çarpım ancak bütün çarpanlar tek olduğunda tek olur.",
            tablo(["İşlem", "Sonuç"], [
                ["$\\text{Tek} \\cdot \\text{Tek}$", "Tek"],
                ["$\\text{Tek} \\cdot \\text{Çift}$", "Çift"],
                ["$\\text{Çift} \\cdot \\text{Çift}$", "Çift"],
            ]),
            "Gerekçe yine tanımda: çarpanlardan biri $2k$ ise çarpımın tamamı $2$ nin katıdır. İki tek sayının çarpımı ise $(2a+1)(2b+1)=4ab+2a+2b+1=2(2ab+a+b)+1$ biçimindedir, yani tektir.",
            ornek(
                "$A=3 \\cdot 5 \\cdot 7 \\cdots 99$ ($3$ ten $99$ a kadar bütün tek sayıların çarpımı) ve $B=1 \\cdot 2 \\cdot 3 \\cdots 20$ verilsin.",
                "$A$ ve $B$ tek mi, çift mi?",
                "$A$ nın bütün çarpanları tek; bu yüzden $A$ tektir.",
                "$B$ nin çarpanlarında $2$ var; tek bir çift çarpan yeter. $B$ çifttir.",
                "Genel olarak $n \\geq 2$ için $n!$ her zaman çifttir."),
            hap("Çarpımda <strong>bir tane</strong> çift çarpan yeter: çarpım çift olur.",
                "Çarpım yalnızca bütün çarpanlar tek olduğunda tektir."),
        ]},
        {"baslik": "Kuvvetlerde tek ve çift", "icerik": [
            "Kuvvet, aynı sayının tekrarlı çarpımıdır; bu yüzden çarpma kuralından doğrudan çıkar. $n$ bir pozitif tam sayı olmak üzere tek sayının her kuvveti tek, çift sayının her kuvveti çifttir. Negatif taban da bu kuralı değiştirmez: $(-3)^4=81$ tek, $(-2)^5=-32$ çifttir.",
            dikkat(
                "Kural yalnızca pozitif üsler için geçerlidir.",
                "Sıfırdan farklı her sayının sıfırıncı kuvveti $1$ dir ve $1$ tektir: $4^0=1$. Yani çift bir sayının sıfırıncı kuvveti tek çıkar.",
                "$0^0$ ise tanımsız kabul edilir."),
            "<h3>İfadelerin paritesi</h3>",
            "Kuvvet kuralı, değişken içeren ifadelerin paritesini bulmak için güçlü bir araçtır. En sık kullanılan sonuçlar şunlar:",
            "<ul><li>$n$ ile $n^2$ aynı paritededir. Bu yüzden $n^2+n$ ve $n^2-n$ her zaman çifttir.</li>"
            "<li>$n$ ile $n+1$ ardışık olduğundan biri çifttir; $n(n+1)$ her zaman çifttir.</li>"
            "<li>$n^3-n=(n-1)n(n+1)$ üç ardışık sayının çarpımıdır ve her zaman çifttir.</li>"
            "<li>$2n+1$ her $n$ için tektir.</li></ul>",
            ornek(
                "$n$ bir tam sayı olsun.",
                "$n^2+5n+6$ ifadesi tek mi, çift mi?",
                "İfadeyi çarpanlarına ayıralım: $n^2+5n+6=(n+2)(n+3)$.",
                "$n+2$ ile $n+3$ ardışık iki sayıdır; biri mutlaka çifttir.",
                "Çarpım her $n$ için çifttir. Kontrol: $n=1$ için $1+5+6=12$, $n=2$ için $4+10+6=20$."),
        ]},
        {"baslik": "Bölmede tek ve çift", "icerik": [
            "Bölme için genel bir tek-çift kuralı yoktur: $12 \\div 4=3$ tek, $12 \\div 6=2$ çifttir ve iki bölmede de bölünen çift sayıdır. Yine de bölme <strong>tam</strong> çıkıyorsa, yani sonuç bir tam sayıysa, bazı durumlarda kesin karar verilebilir:",
            tablo(["Bölme (tam çıkıyorsa)", "Bölüm"], [
                ["$\\text{Tek} \\div \\text{Tek}$", "Tek"],
                ["$\\text{Çift} \\div \\text{Tek}$", "Çift"],
                ["$\\text{Tek} \\div \\text{Çift}$", "Tam çıkmaz"],
                ["$\\text{Çift} \\div \\text{Çift}$", "Belirsiz"],
            ]),
            "Gerekçe çarpma kuralından gelir. $a \\div b=q$ ise $a=b \\cdot q$ dur. Bölünen tek ve bölen tekse, $b \\cdot q$ nun tek olması için $q$ da tek olmalıdır. Bölünen tek, bölen çiftse $b \\cdot q$ her zaman çift çıkacağı için tek bir sayıya eşit olamaz; bölme tam çıkmaz.",
            hap("Tek bir sayı çift bir sayıya <strong>hiçbir zaman</strong> tam bölünmez.",
                "Tek bir sayının tek bir bölene bölümü tam çıkıyorsa bölüm de tektir."),
        ]},
        {"baslik": "Denklemlerde tek ve çift", "icerik": [
            "Klasik bir soru tipi, bir ifadenin paritesi verilip değişkenlerin paritesinin sorulmasıdır. Yöntem şudur: katsayısı çift olan terimleri paritesi belli olduğu için ayır, kalan terimlere kuralları uygula.",
            ornek(
                "$a$ ve $b$ tam sayılar ve $(a+1)(b+2)$ tek olsun.",
                "$a$ ve $b$ nin paritesini bulalım.",
                "Çarpım tek olduğu için iki çarpan da tek olmalı.",
                "$a+1$ tek ise $a$ çifttir.",
                "$b+2$ tek ise $b$ tektir; çünkü $2$ eklemek paritesini değiştirmez."),
            ornek(
                "$a$ ve $b$ tam sayılar ve $a^2+b^2$ çift olsun.",
                "$a+b$ ve $a \\cdot b$ hakkında ne söylenebilir?",
                "$a^2$ nin paritesi $a$ ile, $b^2$ ninki $b$ ile aynıdır. $a^2+b^2$ çift ise $a$ ile $b$ aynı paritededir.",
                "Aynı paritedeki iki sayının toplamı her zaman çifttir: $a+b$ çift.",
                "$a \\cdot b$ ise belirsizdir: ikisi de tekse tek, ikisi de çiftse çift çıkar."),
            dikkat(
                "\"Belirsiz\" demek de bir cevaptır.",
                "Bir ifadenin paritesi verilen bilgilerle belirlenemiyorsa bunu görmek önemlidir; seçeneklerde \"kesinlikle tektir\" ya da \"kesinlikle çifttir\" gibi ifadeler yer alabilir ve belirsiz durumları elemek gerekir."),
        ]},
        {"baslik": "Aralıkta tek ve çift sayıları saymak", "icerik": [
            "Belirli bir aralıktaki tek ya da çift sayıları saymak için ilk ve son uygun sayıyı bulup ardışık sayı formülünü kullanırsın. Ardışık çift ya da ardışık tek sayılarda artış $2$ olduğundan:",
            "$$\\text{Terim sayısı}=\\frac{\\text{son}-\\text{ilk}}{2}+1$$",
            ornek(
                "$17$ ile $95$ arasındaki sayılar (ikisi de dahil) verilsin.",
                "Bu aralıkta kaç çift ve kaç tek sayı vardır?",
                "Çift sayılar $18$ den $94$ e kadar: $\\dfrac{94-18}{2}+1=39$.",
                "Tek sayılar $17$ den $95$ e kadar: $\\dfrac{95-17}{2}+1=40$.",
                "Kontrol: toplam sayı adedi $95-17+1=79$ ve $39+40=79$."),
            "Özel bir durum olarak $1$ den $n$ ye kadar olan sayılarda, $n$ çiftse tek ve çift sayılar eşit sayıdadır: $\\dfrac{n}{2}$ şer tane. $n$ tekse tek sayılar bir fazladır: $\\dfrac{n+1}{2}$ tek, $\\dfrac{n-1}{2}$ çift. Örneğin $1$ den $15$ e kadar $8$ tek, $7$ çift sayı vardır.",
            "<h3>Rakam problemleri</h3>",
            "Bir sayının tek ya da çift olması yalnızca birler basamağına bağlı olduğu için, rakamlarla sayı oluşturma sorularında işe <strong>birler basamağından</strong> başlanır.",
            ornek(
                "Rakamları birbirinden farklı üç basamaklı çift sayıları sayalım.",
                "Kaç tane vardır?",
                "Birler basamağı $0$ ise: yüzler için $9$, onlar için kalan $8$ rakam. $9 \\cdot 8=72$ sayı.",
                "Birler basamağı $2$, $4$, $6$ ya da $8$ ise: $4$ seçenek. Yüzler basamağı $0$ olamaz ve birler basamağındaki rakam da kullanılamaz: $8$ seçenek. Onlar basamağı için kalan $8$ rakam. $4 \\cdot 8 \\cdot 8=256$ sayı.",
                "Toplam: $72+256=328$."),
            "Aynı mantıkla rakamları farklı üç basamaklı sayıların toplamı $9 \\cdot 9 \\cdot 8=648$ olduğundan, bunların $648-328=320$ tanesi tektir.",
            hap("Rakam problemlerinde işe <strong>birler basamağından</strong> başla; tek-çift koşulu orada belirlenir.",
                "Birler basamağının $0$ olup olmaması yüzler basamağının seçeneklerini değiştirdiği için durumları ayrı say."),
        ]},
        {"baslik": "Ardışık sayılar ve parite", "icerik": [
            "Ardışık tam sayılar tek ve çift olarak sırayla dizilir: tek, çift, tek, çift... Bu düzenin birkaç önemli sonucu var:",
            "<ul><li>Ardışık iki tam sayının toplamı her zaman tek, çarpımı her zaman çifttir.</li>"
            "<li>Ardışık iki tek sayının ya da ardışık iki çift sayının toplamı her zaman çifttir.</li>"
            "<li>İlk $n$ tek sayının toplamı $n^2$ dir: $1+3+5+\\cdots+(2n-1)=n^2$.</li>"
            "<li>İlk $n$ çift sayının toplamı $n(n+1)$ dir: $2+4+\\cdots+2n=n(n+1)$.</li></ul>",
            "Ardışık sayıların ayrıntılı anlatımı için <a href=\"/blog/ardisik-sayilar/\">Ardışık Sayılar</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Pariteyle imkânsızlığı göstermek", "icerik": [
            "Tek-çift bilgisinin en güçlü kullanımlarından biri, bir durumun <strong>hiçbir zaman</strong> gerçekleşemeyeceğini göstermektir. Bunun için sayıları tek tek denemek gerekmez; iki tarafın paritesini karşılaştırmak yeter.",
            ornek(
                "Beş tane tek sayının toplamının $30$ olması isteniyor.",
                "Bu mümkün müdür?",
                "Toplamda $5$ tek terim var. Tek terim sayısı tek olduğu için toplam her zaman tektir.",
                "$30$ ise çifttir. Tek bir sayı çift bir sayıya eşit olamaz.",
                "Bu yüzden beş tek sayının toplamı hiçbir zaman $30$ olamaz."),
            "Aynı yolla \"toplamı $100$ olan yedi tek sayı bulun\" ya da \"iki tek sayının çarpımı $50$ olsun\" gibi isteklerin imkânsız olduğu hemen görülür: ilkinde toplam tek, ikincisinde çarpım tek çıkmak zorundadır.",
            hap("Bir eşitliğin iki tarafının paritesi farklıysa eşitlik <strong>hiçbir zaman</strong> sağlanamaz.",
                "İmkânsızlık sorularında önce iki tarafın tek mi çift mi olduğuna bak."),
        ]},
        {"baslik": "Tek ve çift sayıların kareleri", "icerik": [
            "Karelerin de düzenli bir davranışı var. Çift bir sayı $2k$ ise karesi $4k^2$ olur; yani her çift sayının karesi $4$ ün katıdır. Tek bir sayı $2k+1$ ise karesi $4k^2+4k+1=4k(k+1)+1$ olur. $k(k+1)$ ardışık iki sayının çarpımı olduğu için çifttir; bu yüzden $4k(k+1)$ sayısı $8$ in katıdır.",
            "$$(2k+1)^2=8 \\cdot \\frac{k(k+1)}{2}+1$$",
            "Sonuç şaşırtıcı ama kesin: her tek sayının karesi $8$ e bölündüğünde $1$ kalanını verir. Örneğin $3^2=9=8+1$, $5^2=25=24+1$, $7^2=49=48+1$.",
            ornek(
                "$n$ tek bir tam sayı olsun.",
                "$n^2+7$ sayısının $8$ ile bölümünden kalan kaçtır?",
                "$n$ tek olduğu için $n^2$ nin $8$ ile bölümünden kalan $1$ dir.",
                "$n^2+7$ nin kalanı $1+7=8$, yani $0$ dır. $n^2+7$ her zaman $8$ in katıdır.",
                "Kontrol: $n=3$ için $9+7=16$, $n=5$ için $25+7=32$."),
        ]},
        {"baslik": "Sınavda tek ve çift sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) tek-çift soruları bir ifadenin paritesi verilip değişkenlerin paritesinin sorulması, \"kesinlikle tek olan\" ifadeyi bulma ve rakamlarla sayı oluşturma biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde aynı mantık sayı problemlerinin içinde kullanılır: bir toplamın ya da çarpımın tek çıkmasından bilinmeyenin paritesini çıkarmak gibi."),
            "Bu sorularda en hızlı yol, değişkenlere küçük sayılar vererek denemektir: $a=1, b=2$ gibi. Ancak bir ifadenin \"kesinlikle\" tek ya da çift olduğunu göstermek için tek bir deneme yetmez; kuralla gerekçelendirmek gerekir. Denemeyi yanlış seçenekleri elemek için kullan.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$0$ ı tek ya da işaretsiz diye dışarıda tutmak", "$0$ çift sayıdır"],
                ["Negatif sayıya parite vermemek", "$-7$ tek, $-6$ çift"],
                ["Toplamda her terimi tek tek hesaplamak", "Tek terimleri say"],
                ["$4^0$ ı çift sanmak", "$4^0=1$ tektir"],
                ["Bölmeye tek-çift kuralı uygulamak", "Genel kural yok"],
                ["Tek bir denemeyle \"kesinlikle\" demek", "Kuralla gerekçelendir"],
            ]),
            "Bu hataların çoğu tanımı unutmaktan gelir. Tek ve çift sayıyı $2k+1$ ve $2k$ biçiminde yazmak, şüpheli her durumda doğru cevaba götürür.",
        ]},
    ],
    "sss": [
        ("Sıfır tek mi çift mi?",
         "Sıfır çift sayıdır, çünkü 2 ile tam bölünür: 0 eşittir 2 çarpı 0."),
        ("Negatif sayılar tek ya da çift olabilir mi?",
         "Evet. Tek ve çift tanımı bütün tam sayıları kapsar. Örneğin eksi 6 çift, eksi 7 tektir."),
        ("İki tek sayının toplamı neden çifttir?",
         "İki tek sayı 2a artı 1 ve 2b artı 1 biçiminde yazılır. Toplamları 2a artı 2b artı 2, yani 2 çarpı (a artı b artı 1) olur ve bu 2 nin katıdır."),
        ("Bir çarpımın çift olması için ne gerekir?",
         "Çarpanlardan en az birinin çift olması yeterlidir. Çarpım ancak bütün çarpanlar tek olduğunda tektir."),
        ("Bölme işleminde tek-çift kuralı var mı?",
         "Genel bir kural yoktur. Ancak bölme tam çıkıyorsa bazı sonuçlar kesindir: tek bir sayının tek bir sayıya bölümü tektir, tek bir sayı çift bir sayıya ise hiçbir zaman tam bölünmez."),
        ("Bir sayının tek mi çift mi olduğu en hızlı nasıl anlaşılır?",
         "Birler basamağına bakılır. Birler basamağı 0, 2, 4, 6 ya da 8 ise sayı çift, 1, 3, 5, 7 ya da 9 ise tektir."),
        ("Tek bir sayının karesi neden 8 e bölününce 1 kalanını verir?",
         "Tek sayı 2k artı 1 biçiminde yazılır ve karesi 4k(k artı 1) artı 1 olur. k ile k artı 1 ardışık olduğu için çarpımları çifttir; bu yüzden 4k(k artı 1) sayısı 8 in katıdır ve geriye 1 kalır."),
    ],
    "kontrol": [
        "Tek ve çift sayıyı $2k+1$ ve $2k$ biçiminde yazıp $0$ ın ve negatif sayıların paritesini söyleyebiliyorum.",
        "Bir sayının paritesini birler basamağından hemen söyleyebiliyorum.",
        "Çok terimli bir toplamın paritesini tek terimleri sayarak bulabiliyorum.",
        "Bir çarpımın paritesini çarpanlara bakarak söyleyebiliyorum.",
        "Kuvvetlerde parite kuralını ve $0$ üssün istisnasını biliyorum.",
        "$n^2+n$ ya da $n^3-n$ gibi ifadelerin neden her zaman çift olduğunu açıklayabiliyorum.",
        "Tam çıkan bir bölmede bölümün paritesi hakkında ne söylenebileceğini biliyorum.",
        "Verilen bir ifadenin paritesinden değişkenlerin paritesini çıkarabiliyorum.",
        "Bir aralıktaki tek ve çift sayıları formülle sayabiliyorum.",
        "Rakamları farklı tek ya da çift sayıları birler basamağından başlayarak sayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["temel-kavramlar-konu-anlatimi-pdf", "ardisik-sayilar", "pozitif-ve-negatif-sayilar"],
}
