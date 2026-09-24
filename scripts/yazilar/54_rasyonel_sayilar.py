# scripts/yazilar/54_rasyonel_sayilar.py — Rasyonel Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "rasyonel-sayilar-konu-anlatimi-pdf",
    "baslik": "Rasyonel Sayılar Konu Anlatımı PDF",
    "aciklama": "Rasyonel sayı nedir? Kesir türleri, sadeleştirme, dört işlem, sıralama, ondalık gösterim ve devirli ondalık sayıyı kesre çevirme; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "rasyonel-sayilar-konu-anlatimi-pdf",
    "kapak_alt": "Rasyonel sayılar konu anlatımı: daireleri ve çubukları eş parçalara ayırarak kesirleri gösteren iki öğrenci",
    "ozet": "Bir bütünü eş parçalara ayırdığında ortaya çıkan her parça bir rasyonel sayıyla anlatılır. Kesirler, ondalık sayılar ve yüzdeler aslında aynı sayıların farklı yazılışlarıdır. Bu yazıda rasyonel sayıyı tanımlıyor, sadeleştirmeyi, dört işlemi ve sıralamayı adım adım işliyor, bir kesrin ondalık gösteriminin ne zaman sonlu ne zaman devirli olduğunu ve devirli ondalık sayının kesre nasıl çevrildiğini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Rasyonel sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için tam sayılarla dört işlemi, EBOB ve EKOK kavramlarını biliyor olman yeterli.",
                "Tam sayılarda işaret kuralları için <a href=\"/blog/dogal-sayilar-ve-tam-sayilar/\">Doğal Sayılar ve Tam Sayılar</a> yazısına göz at."),
            "$a$ ve $b$ tam sayı ve $b \\neq 0$ olmak üzere $\\dfrac{a}{b}$ biçiminde yazılabilen sayılara <strong>rasyonel sayı</strong> denir. $a$ ya <strong>pay</strong>, $b$ ye <strong>payda</strong> denir. Rasyonel sayılar kümesi $\\mathbb{Q}$ ile gösterilir.",
            "Kesir çizgisi aslında bir bölme işaretidir: $\\dfrac{3}{4}$, \"$3$ ün $4$ e bölümü\" demektir. Paydanın sıfır olamamasının sebebi de budur; sıfıra bölme tanımsızdır.",
            "Her tam sayı bir rasyonel sayıdır, çünkü paydasına $1$ yazılabilir: $-6=\\dfrac{-6}{1}$. Payı sıfır olan kesir ise sıfıra eşittir: $\\dfrac{0}{7}=0$.",
            "Rasyonel sayılar toplama, çıkarma, çarpma ve sıfır hariç bölme işlemlerine göre kapalıdır: iki rasyonel sayıyla bu işlemleri yaptığında sonuç yine rasyoneldir. Tam sayılarda bölmenin yarattığı eksiklik burada kapanır.",
            hap("$\\dfrac{a}{b}$ da payda sıfır olamaz: $b \\neq 0$.",
                "Pay sıfırsa kesrin değeri sıfırdır: $\\dfrac{0}{b}=0$."),
            dikkat(
                "$\\dfrac{0}{5}=0$ tanımlıdır, $\\dfrac{5}{0}$ tanımsızdır.",
                "Sıfır payda olduğunda sorun çıkar, pay olduğunda çıkmaz."),
        ]},
        {"baslik": "Denk kesirler ve sadeleştirme", "icerik": [
            "Bir kesrin payı ve paydası sıfırdan farklı aynı sayıyla çarpılır ya da bölünürse değeri değişmez. Çarpmaya <strong>genişletme</strong>, bölmeye <strong>sadeleştirme</strong> denir. Aynı değeri veren kesirlere <strong>denk kesirler</strong> denir:",
            "$$\\frac{3}{4}=\\frac{6}{8}=\\frac{9}{12}=\\frac{75}{100}$$",
            "Pay ile payda arasında $1$ den başka ortak bölen kalmadığında kesir <strong>en sade</strong> hâlindedir. En sade hâle tek adımda ulaşmak için pay ve payda EBOB larına bölünür.",
            ornek(
                "$\\dfrac{84}{126}$ kesri verilsin.",
                "Bu kesri en sade hâline getirelim.",
                "$84=2^2 \\cdot 3 \\cdot 7$ ve $126=2 \\cdot 3^2 \\cdot 7$. Ortak çarpanlar $2$, $3$ ve $7$ dir; EBOB $=42$.",
                "Pay ve paydayı $42$ ye bölelim: $\\dfrac{84}{126}=\\dfrac{2}{3}$."),
            hap("En sade hâl için pay ve paydayı EBOB larına böl.",
                "Genişletme ve sadeleştirme kesrin değerini değiştirmez."),
        ]},
        {"baslik": "Kesir türleri", "icerik": [
            "Pozitif kesirler payın paydaya göre büyüklüğüne göre üç gruba ayrılır:",
            "<ul><li><strong>Basit kesir:</strong> pay paydadan küçüktür, değeri $1$ den küçüktür: $\\dfrac{3}{5}$.</li>"
            "<li><strong>Bileşik kesir:</strong> pay paydaya eşit ya da ondan büyüktür, değeri $1$ ya da $1$ den büyüktür: $\\dfrac{7}{3}$, $\\dfrac{4}{4}$.</li>"
            "<li><strong>Tam sayılı kesir:</strong> bir tam sayı ile bir basit kesrin birlikte yazılışıdır: $2\\dfrac{1}{3}$, \"iki tam üçte bir\" diye okunur.</li></ul>",
            "Tam sayılı kesir ile bileşik kesir birbirine çevrilebilir. Tam kısım payda ile çarpılıp paya eklenir:",
            "$$2\\frac{1}{3}=\\frac{2 \\cdot 3+1}{3}=\\frac{7}{3}$$",
            "Tersine, $\\dfrac{7}{3}$ de $7$ yi $3$ e bölersek bölüm $2$, kalan $1$ çıkar. Bölüm tam kısım, kalan yeni pay olur: $2\\dfrac{1}{3}$.",
            dikkat(
                "$2\\dfrac{1}{3}$ bir çarpım değil, bir toplamdır: $2+\\dfrac{1}{3}$.",
                "İşlem yapmadan önce tam sayılı kesri bileşik kesre çevir."),
        ]},
        {"baslik": "Toplama ve çıkarma", "icerik": [
            "Kesirler ancak <strong>paydaları eşitse</strong> doğrudan toplanır ya da çıkarılır: paylar toplanır, payda aynı kalır. Paydalar farklıysa önce ortak payda bulunur. En küçük ortak payda, paydaların EKOK udur.",
            "$$\\frac{a}{c}+\\frac{b}{c}=\\frac{a+b}{c}$$",
            ornek(
                "$\\dfrac{5}{6}+\\dfrac{3}{4}$ işlemi verilsin.",
                "Sonucu bulalım.",
                "Paydaların EKOK u: $\\text{EKOK}(6,4)=12$.",
                "Kesirleri genişletelim: $\\dfrac{5}{6}=\\dfrac{10}{12}$ ve $\\dfrac{3}{4}=\\dfrac{9}{12}$.",
                "Topla: $\\dfrac{10}{12}+\\dfrac{9}{12}=\\dfrac{19}{12}$. Bu kesir en sade hâlindedir."),
            ornek(
                "$2\\dfrac{1}{2}-1\\dfrac{3}{4}$ işlemi verilsin.",
                "Sonucu bulalım.",
                "Önce bileşik kesre çevirelim: $2\\dfrac{1}{2}=\\dfrac{5}{2}$ ve $1\\dfrac{3}{4}=\\dfrac{7}{4}$.",
                "Paydaları eşitleyelim: $\\dfrac{5}{2}=\\dfrac{10}{4}$.",
                "Çıkaralım: $\\dfrac{10}{4}-\\dfrac{7}{4}=\\dfrac{3}{4}$."),
            dikkat(
                "Kesirler toplanırken paylar ve paydalar ayrı ayrı toplanmaz.",
                "$\\dfrac{1}{2}+\\dfrac{1}{3}$ in sonucu $\\dfrac{2}{5}$ değil, $\\dfrac{5}{6}$ tir. Kontrol: $\\dfrac{2}{5}$, $\\dfrac{1}{2}$ den bile küçüktür; iki pozitif sayının toplamı onlardan küçük olamaz."),
            hap("Toplama ve çıkarmada önce paydaları eşitle; ortak payda olarak EKOK u kullan.",
                "Paylar toplanır, payda aynı kalır."),
        ]},
        {"baslik": "Çarpma ve bölme", "icerik": [
            "Çarpmada ortak payda gerekmez: paylar kendi arasında, paydalar kendi arasında çarpılır. İşlemden önce çapraz sadeleştirme yapmak sayıları küçültür.",
            "$$\\frac{a}{b} \\cdot \\frac{c}{d}=\\frac{a \\cdot c}{b \\cdot d}$$",
            "Bölmede ikinci kesir ters çevrilip çarpılır. $\\dfrac{c}{d}$ nin çarpmaya göre tersi $\\dfrac{d}{c}$ dir:",
            "Bir sayının <strong>çarpmaya göre tersi</strong>, onunla çarpıldığında $1$ veren sayıdır: $\\dfrac{2}{3} \\cdot \\dfrac{3}{2}=1$. Sıfırın çarpmaya göre tersi yoktur, çünkü sıfırla çarpılan her sayı sıfır verir. Bölmenin \"ters çevir ve çarp\" kuralı bu tanımdan gelir.",
            "$$\\frac{a}{b} \\div \\frac{c}{d}=\\frac{a}{b} \\cdot \\frac{d}{c}$$",
            ornek(
                "$\\dfrac{3}{5} \\div \\dfrac{9}{10}$ işlemi verilsin.",
                "Sonucu bulalım.",
                "İkinci kesri ters çevirip çarpalım: $\\dfrac{3}{5} \\cdot \\dfrac{10}{9}$.",
                "Çapraz sadeleştirelim: $3$ ile $9$ u $3$ e, $10$ ile $5$ i $5$ e bölelim: $\\dfrac{1}{1} \\cdot \\dfrac{2}{3}$.",
                "Sonuç $\\dfrac{2}{3}$ dir."),
            "Kesrin içinde kesir bulunan ifadelere <strong>merdiven kesir</strong> denir. Bu ifadeler en alttan başlanarak yukarı doğru çözülür.",
            ornek(
                "$\\dfrac{1}{1+\\dfrac{1}{1+\\dfrac{1}{2}}}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "En alttan başlayalım: $1+\\dfrac{1}{2}=\\dfrac{3}{2}$.",
                "Bir üst basamak: $\\dfrac{1}{3/2}=\\dfrac{2}{3}$ ve $1+\\dfrac{2}{3}=\\dfrac{5}{3}$.",
                "En üst: $\\dfrac{1}{5/3}=\\dfrac{3}{5}$."),
            hap("Bölmede ikinci kesri ters çevir ve çarp.",
                "Merdiven kesir en alttan yukarı doğru çözülür."),
        ]},
        {"baslik": "Rasyonel sayıları sıralama", "icerik": [
            "İki kesri karşılaştırmanın en güvenli yolu paydalarını eşitlemektir; paydası eşit iki pozitif kesirden payı büyük olan büyüktür. Bazı durumlarda daha kısa yollar vardır:",
            "<ul><li><strong>Payları eşitse:</strong> paydası küçük olan büyüktür. $\\dfrac{3}{7}>\\dfrac{3}{8}$, çünkü aynı bütün daha az parçaya bölünmüştür.</li>"
            "<li><strong>Bire yakınlık:</strong> $\\dfrac{7}{8}$ ile $\\dfrac{8}{9}$ in bire uzaklıkları $\\dfrac{1}{8}$ ve $\\dfrac{1}{9}$ dir. Bire daha yakın olan $\\dfrac{8}{9}$ daha büyüktür.</li>"
            "<li><strong>Ondalığa çevirme:</strong> kesirleri ondalık sayıya çevirip karşılaştırmak da her zaman işe yarar.</li></ul>",
            ornek(
                "$a=\\dfrac{2}{3}$, $b=\\dfrac{3}{5}$ ve $c=\\dfrac{5}{8}$ olsun.",
                "Bu sayıları küçükten büyüğe sıralayalım.",
                "Paydaların EKOK u $120$ dir. Genişletelim: $a=\\dfrac{80}{120}$, $b=\\dfrac{72}{120}$, $c=\\dfrac{75}{120}$.",
                "Paylara bakarak: $72<75<80$.",
                "Sıralama: $b<c<a$."),
            hap("Payları eşit pozitif kesirlerde paydası <strong>küçük</strong> olan büyüktür.",
                "$\\dfrac{n-1}{n}$ biçimindeki kesirlerde $n$ büyüdükçe kesir de büyür."),
            "Rasyonel sayıların sıralamasında bir özellik daha vardır: iki rasyonel sayı arasında her zaman başka bir rasyonel sayı bulunur. İki sayının ortalaması bunlardan biridir; bu işlem sonsuza kadar tekrarlanabilir.",
        ]},
        {"baslik": "Sayı doğrusunda rasyonel sayılar", "icerik": [
            "Her rasyonel sayı sayı doğrusunda bir noktadır. Bir kesri yerleştirmek için önce hangi iki tam sayı arasında olduğunu bul, sonra o birim aralığı paydadaki sayı kadar eş parçaya böl.",
            ornek(
                "$\\dfrac{7}{3}$ sayısı verilsin.",
                "Bu sayıyı sayı doğrusunda yerleştirelim.",
                "Tam sayılı kesre çevirelim: $\\dfrac{7}{3}=2\\dfrac{1}{3}$. Sayı $2$ ile $3$ arasındadır.",
                "$2$ ile $3$ arasındaki birim aralığı $3$ eş parçaya bölelim.",
                "$2$ den sonraki ilk bölme çizgisi $\\dfrac{7}{3}$ dir."),
            "Negatif kesirler de aynı yolla, sıfırın solunda yerleştirilir. $-\\dfrac{5}{4}=-1\\dfrac{1}{4}$ sayısı $-2$ ile $-1$ arasında, $-1$ e daha yakın olan yerdedir.",
        ]},
        {"baslik": "Negatif kesirler ve işaret", "icerik": [
            "Bir kesrin eksi işareti paya, paydaya ya da kesrin önüne yazılabilir; üçü de aynı sayıdır:",
            "$$-\\frac{3}{4}=\\frac{-3}{4}=\\frac{3}{-4}$$",
            "Pay ve paydanın ikisi de negatifse eksiler birbirini götürür: $\\dfrac{-3}{-4}=\\dfrac{3}{4}$. Bu, tam sayılardaki bölme işaret kuralının kesirdeki karşılığıdır.",
            "Negatif kesirleri sıralarken pozitif kesirlerdeki sıra <strong>tersine döner</strong>. $\\dfrac{1}{2}>\\dfrac{1}{3}$ dir, ama $-\\dfrac{1}{2}<-\\dfrac{1}{3}$ dir; çünkü $-\\dfrac{1}{2}$ sıfırdan daha uzaktadır.",
            ornek(
                "$-\\dfrac{2}{3}$, $-\\dfrac{3}{4}$ ve $-\\dfrac{1}{2}$ sayıları verilsin.",
                "Bu sayıları küçükten büyüğe sıralayalım.",
                "Önce mutlak değerleri sıralayalım. Ortak payda $12$: $\\dfrac{8}{12}$, $\\dfrac{9}{12}$, $\\dfrac{6}{12}$. Yani $\\dfrac{1}{2}<\\dfrac{2}{3}<\\dfrac{3}{4}$.",
                "Negatiflerde mutlak değeri büyük olan daha küçüktür; sıra ters döner.",
                "Sıralama: $-\\dfrac{3}{4}<-\\dfrac{2}{3}<-\\dfrac{1}{2}$."),
            hap("Negatif kesirlerde sıralama, mutlak değerlerin sıralamasının <strong>tersidir</strong>.",
                "Eksi işareti paya, paydaya ya da önüne yazılabilir; değer değişmez."),
        ]},
        {"baslik": "Kesir, ondalık ve yüzde", "icerik": [
            "Yüzde, paydası $100$ olan bir kesirdir: $\\%25=\\dfrac{25}{100}=\\dfrac{1}{4}=0.25$. Bu yüzden bir rasyonel sayı kesir, ondalık ya da yüzde olarak yazılabilir; üçü de aynı değeri gösterir.",
            "<ul><li>Kesirden yüzdeye: kesri $100$ ile çarp. $\\dfrac{3}{5}=\\dfrac{60}{100}=\\%60$.</li><li>Ondalıktan yüzdeye: virgülü iki basamak sağa kaydır. $0.07=\\%7$.</li><li>Yüzdeden kesre: $100$ e böl ve sadeleştir. $\\%40=\\dfrac{40}{100}=\\dfrac{2}{5}$.</li></ul>",
            ornek(
                "$\\dfrac{3}{8}$ kesri verilsin.",
                "Bu kesri ondalık ve yüzde olarak yazalım.",
                "Ondalık: $3 \\div 8=0.375$.",
                "Yüzde: $0.375 \\cdot 100=37.5$, yani $\\%37.5$."),
            "Sık kullanılan eşleşmeleri bilmek işlemleri hızlandırır: $\\dfrac{1}{2}=0.5=\\%50$, $\\dfrac{1}{4}=0.25=\\%25$, $\\dfrac{3}{4}=0.75=\\%75$, $\\dfrac{1}{5}=0.2=\\%20$, $\\dfrac{1}{8}=0.125=\\%12.5$.",
        ]},
        {"baslik": "Kesirlerin kuvveti", "icerik": [
            "Bir kesrin kuvveti alınırken pay ve payda ayrı ayrı kuvvete yükseltilir:",
            "$$\\left(\\frac{a}{b}\\right)^n=\\frac{a^n}{b^n}$$",
            "Örneğin $\\left(\\dfrac{2}{3}\\right)^2=\\dfrac{4}{9}$ ve $\\left(-\\dfrac{1}{2}\\right)^3=-\\dfrac{1}{8}$ dir. İşaret kuralı burada da geçerlidir: negatif kesrin tek kuvveti negatiftir.",
            "Basit kesirlerde ilginç bir durum vardır: $0$ ile $1$ arasındaki bir sayının kuvveti alındıkça sayı <strong>küçülür</strong>. $\\dfrac{1}{2}$, $\\dfrac{1}{4}$, $\\dfrac{1}{8}$ diye gider. Tam sayılardaki \"kuvvet alınca büyür\" alışkanlığı burada tersine işler.",
            dikkat(
                "$0$ ile $1$ arasındaki sayılarda $x^2<x$ tir.",
                "Örneğin $x=\\dfrac{1}{3}$ için $x^2=\\dfrac{1}{9}$ ve $\\dfrac{1}{9}<\\dfrac{1}{3}$. Karşılaştırma sorularında bu durum sık unutulur."),
        ]},
        {"baslik": "Ondalık gösterim", "icerik": [
            "Bir kesri ondalık sayıya çevirmek için pay paydaya bölünür. Sonuç iki biçimde çıkabilir: bölme bir yerde biter ya da bir basamak grubu sonsuza kadar tekrar eder.",
            "<ul><li><strong>Sonlu ondalık:</strong> $\\dfrac{3}{8}=0.375$, $\\dfrac{7}{20}=0.35$.</li><li><strong>Devirli ondalık:</strong> $\\dfrac{1}{3}=0.333\\ldots$, $\\dfrac{1}{6}=0.1666\\ldots$ Tekrar eden kısım üstü çizilerek yazılır: $0.\\overline{3}$ ve $0.1\\overline{6}$.</li></ul>",
            "Hangisinin çıkacağı bölmeden önce bilinebilir. Kesri en sade hâline getir ve paydanın asal çarpanlarına bak: paydada $2$ ve $5$ ten başka asal çarpan yoksa ondalık gösterim sonludur, varsa devirlidir. Sebebi şudur: sonlu bir ondalık, paydası $10$, $100$, $1000$ gibi bir sayı olan kesirdir ve bu sayıların asal çarpanları yalnızca $2$ ve $5$ tir.",
            hap("En sade hâldeki kesrin paydasında yalnız $2$ ve $5$ çarpanları varsa ondalık gösterim <strong>sonludur</strong>.",
                "Başka bir asal çarpan varsa gösterim <strong>devirlidir</strong>."),
            ornek(
                "$\\dfrac{7}{40}$, $\\dfrac{5}{12}$ ve $\\dfrac{9}{75}$ kesirleri verilsin.",
                "Hangilerinin ondalık gösterimi sonludur?",
                "$\\dfrac{7}{40}$ en sade hâlindedir ve $40=2^3 \\cdot 5$. Yalnız $2$ ve $5$ var: sonlu, $0.175$.",
                "$\\dfrac{5}{12}$ en sade hâlindedir ve $12=2^2 \\cdot 3$. Paydada $3$ var: devirli, $0.41\\overline{6}$.",
                "$\\dfrac{9}{75}$ sadeleşir: $\\dfrac{3}{25}$ ve $25=5^2$. Sonlu, $0.12$."),
            dikkat(
                "Bu kontrol kesir <strong>sadeleştirildikten sonra</strong> yapılır.",
                "$\\dfrac{3}{12}$ ün paydasında $3$ çarpanı vardır, ama sadeleşince $\\dfrac{1}{4}=0.25$ olur ve gösterim sonludur."),
        ]},
        {"baslik": "Devirli ondalık sayıyı kesre çevirme", "icerik": [
            "Devirli bir ondalık sayı her zaman bir kesre çevrilebilir; bu yüzden rasyoneldir. Çevirmenin kısa kuralı şudur:",
            "$$\\frac{\\text{sayının tamamı}-\\text{devretmeyen kısım}}{\\text{devreden basamak kadar 9, devretmeyen ondalık kadar 0}}$$",
            "Kuralın nereden geldiğini en basit örnekte görelim. $x=0.333\\ldots$ olsun. İki tarafı $10$ ile çarparsak $10x=3.333\\ldots$ olur. Alttan üsttekini çıkarınca sonsuz kuyruklar birbirini götürür: $9x=3$, yani $x=\\dfrac{3}{9}=\\dfrac{1}{3}$.",
            ornek(
                "$0.1\\overline{6}$ sayısı verilsin.",
                "Bu sayıyı kesre çevirelim.",
                "Sayının tamamı virgülsüz $16$, devretmeyen kısım $1$ dir.",
                "Devreden basamak $1$ tane ($6$), devretmeyen ondalık basamak $1$ tane ($1$). Payda: $90$.",
                "$\\dfrac{16-1}{90}=\\dfrac{15}{90}=\\dfrac{1}{6}$."),
            ornek(
                "$1.\\overline{27}$ sayısı verilsin.",
                "Bu sayıyı kesre çevirelim.",
                "Sayının tamamı virgülsüz $127$, devretmeyen kısım $1$ dir.",
                "Devreden basamak $2$ tane, devretmeyen ondalık yok. Payda: $99$.",
                "$\\dfrac{127-1}{99}=\\dfrac{126}{99}=\\dfrac{14}{11}$. Kontrol: $14 \\div 11=1.2727\\ldots$"),
            dikkat(
                "$0.\\overline{9}$ sayısı $1$ e eşittir.",
                "Kurala göre $\\dfrac{9}{9}=1$ dir. $\\dfrac{1}{3}=0.\\overline{3}$ ün iki tarafını $3$ ile çarparak da görebilirsin: $1=0.\\overline{9}$."),
        ]},
        {"baslik": "Sınavda rasyonel sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) rasyonel sayılar dört işlem, merdiven kesir, sıralama ve devirli ondalık sayıları kesre çevirme biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde kesirler bir problemin içinde de karşına çıkabilir: \"bir işin üçte biri\", \"paranın beşte ikisi\" gibi ifadeler kesirle işlem gerektirir."),
            "Kesir problemlerinde bütünün ne olduğunu en başta belirlemek önemlidir. \"Kalanın yarısı\" ile \"tamamın yarısı\" farklı bütünlere göre hesaplanır.",
            ornek(
                "Bir öğrenci harçlığının $\\dfrac{1}{4}$ ini kitaba, kalanın $\\dfrac{2}{3}$ sini yemeğe harcıyor.",
                "Harçlığının kaçta kaçı kalmıştır?",
                "Kitaptan sonra kalan: $1-\\dfrac{1}{4}=\\dfrac{3}{4}$.",
                "Yemeğe harcanan kalanın $\\dfrac{2}{3}$ si: $\\dfrac{3}{4} \\cdot \\dfrac{2}{3}=\\dfrac{1}{2}$.",
                "Kalan: $\\dfrac{3}{4}-\\dfrac{1}{2}=\\dfrac{1}{4}$. Harçlığın dörtte biri kalmıştır."),
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{2}{5}$", "Önce payda eşitlenir: $\\dfrac{5}{6}$"],
                ["Bölmede birinci kesri ters çevirmek", "İkinci kesir ters çevrilir"],
                ["$2\\dfrac{1}{3}$ i çarpım sanmak", "$2+\\dfrac{1}{3}=\\dfrac{7}{3}$"],
                ["Sadeleştirmeden sonlu/devirli kararı", "Önce sadeleştir"],
                ["$0.\\overline{9}$ u $1$ den küçük sanmak", "$0.\\overline{9}=1$"],
                ["\"Kalanın\" ile \"tamamın\" karıştırmak", "Bütünü önce belirle"],
            ]),
            "Kesirlerdeki hataların çoğu bir kuralın yanlış işleme taşınmasından doğar: çarpmadaki \"pay paya, payda paydaya\" kuralı toplamaya taşınınca $\\dfrac{2}{5}$ gibi yanlış sonuçlar çıkar. Her işlemin kendi kuralını ayrı ayrı hatırla.",
        ]},
    ],
    "sss": [
        ("Rasyonel sayı nedir?",
         "Payı ve paydası tam sayı olan, paydası sıfırdan farklı kesir biçiminde yazılabilen sayılara rasyonel sayı denir. Tam sayılar, sonlu ondalık sayılar ve devirli ondalık sayılar rasyoneldir."),
        ("Devirli ondalık sayılar rasyonel midir?",
         "Evet. Her devirli ondalık sayı bir kesre çevrilebilir. Örneğin 0,333... üçte bire, 0,1666... altıda bire eşittir."),
        ("Bir kesrin ondalık gösteriminin sonlu olup olmadığı nasıl anlaşılır?",
         "Kesir en sade hâline getirilir ve paydanın asal çarpanlarına bakılır. Paydada yalnızca 2 ve 5 çarpanları varsa gösterim sonludur, başka bir asal çarpan varsa devirlidir."),
        ("Kesirler nasıl toplanır?",
         "Önce paydalar eşitlenir. Ortak payda olarak paydaların EKOK u kullanılır. Sonra paylar toplanır ve payda aynı bırakılır. Paylar ve paydalar ayrı ayrı toplanmaz."),
        ("Sıfır virgül dokuz devirli neden 1 e eşittir?",
         "Devirli ondalığı kesre çevirme kuralına göre 0,999... sayısı dokuz bölü dokuza, yani 1 e eşittir. Üçte birin 0,333... olduğunu bilip iki tarafı 3 ile çarparak da aynı sonuca ulaşılır."),
        ("Merdiven kesir nasıl çözülür?",
         "Merdiven kesir en alttaki kesirden başlanarak yukarı doğru çözülür. Her basamakta bulunan değer bir üstteki kesrin paydasına yazılır."),
        ("Paydası sıfır olan kesir neden tanımsızdır?",
         "Kesir çizgisi bir bölme işaretidir ve sıfıra bölme tanımsızdır. Bir sayıyı sıfıra bölmek, sıfırla çarpıldığında o sayıyı veren bir sayı aramak demektir; sıfırla çarpılan her sayı sıfır verdiği için böyle bir sayı yoktur."),
        ("Kesir ile rasyonel sayı aynı şey midir?",
         "Kesir bir yazılış biçimidir, rasyonel sayı ise bir sayı türüdür. Her rasyonel sayı bir kesir olarak yazılabilir; aynı rasyonel sayı sonsuz sayıda denk kesirle gösterilebilir. Karekök iki bölü iki gibi paydalı yazılan her ifade ise rasyonel değildir."),
    ],
    "kontrol": [
        "Rasyonel sayıyı tanımlayıp paydanın neden sıfır olamayacağını açıklayabiliyorum.",
        "Bir kesri EBOB kullanarak tek adımda en sade hâline getirebiliyorum.",
        "Tam sayılı kesri bileşik kesre ve tersine çevirebiliyorum.",
        "Farklı paydalı kesirleri EKOK ile toplayıp çıkarabiliyorum.",
        "Kesirlerle çarpma ve bölme yapabiliyor, bölmede hangi kesrin ters çevrileceğini biliyorum.",
        "Merdiven kesri en alttan başlayarak çözebiliyorum.",
        "Kesirleri payda eşitleyerek ya da bire yakınlıkla sıralayabiliyorum.",
        "Bir kesrin ondalık gösteriminin sonlu mu devirli mi olduğunu bölmeden söyleyebiliyorum.",
        "Devirli ondalık sayıyı kesre çevirebiliyorum.",
        "Kesir problemlerinde \"kalanın\" ile \"tamamın\" farkını gözetiyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["dogal-sayilar-ve-tam-sayilar", "irrasyonel-sayilar-ve-gercek-sayilar", "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf"],
}
