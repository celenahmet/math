# scripts/yazilar/69_kesir_toplama.py — Kesirlerde Toplama ve Cikarma (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kesirlerde-toplama-ve-cikarma",
    "baslik": "Kesirlerde Toplama ve Çıkarma",
    "aciklama": "Kesirlerde toplama ve çıkarma nasıl yapılır? Eşit ve farklı paydalar, EKOK ile ortak payda, tam sayılı kesirler, negatif kesirler ve problemler.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kesirlerde-toplama-ve-cikarma",
    "kapak_alt": "Kesirlerde toplama ve çıkarma: daire dilimlerini birleştirip ayırarak kesir işlemi yapan iki öğrenci",
    "ozet": "Kesirleri toplamak, aynı büyüklükteki parçaları bir araya getirmektir. Parçalar farklı büyüklükteyse önce onları aynı büyüklüğe getirmek gerekir; ortak paydanın anlamı budur. Bu yazıda eşit ve farklı paydalı kesirlerde toplama ve çıkarmayı, ortak payda olarak EKOK kullanmanın nedenini, tam sayılı kesirlerde ödünç almayı, negatif kesirleri, ardışık kesirlerin birbirini götürdüğü toplamları ve kesir problemlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Paydalar eşitse", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için kesir kavramını, denk kesirleri ve EKOK'u biliyor olman yeterli.",
                "Kesirlerin temeli için <a href=\"/blog/kesirler-konu-anlatimi-pdf/\">Kesirler Konu Anlatımı PDF</a> yazısına göz at."),
            "Paydaları eşit kesirler toplanırken ya da çıkarılırken <strong>paylar</strong> toplanır ya da çıkarılır, <strong>payda aynen kalır</strong>.",
            "$$\\dfrac{a}{c}+\\dfrac{b}{c}=\\dfrac{a+b}{c} \\text{ ve } \\dfrac{a}{c}-\\dfrac{b}{c}=\\dfrac{a-b}{c}$$",
            "Nedeni modelde açıktır. $\\dfrac{2}{7}$ ile $\\dfrac{3}{7}$ ün ikisi de yedide birlik parçalardan oluşur: iki parça ile üç parça birleşince beş parça olur, parçaların büyüklüğü değişmez. Sonuç $\\dfrac{5}{7}$ tir. Payda, parçanın adıdır; iki elma ile üç elmanın toplamının beş elma olması gibi.",
            ornek(
                "$\\dfrac{7}{12}+\\dfrac{11}{12}$ ve $\\dfrac{9}{10}-\\dfrac{3}{10}$ işlemleri verilsin.",
                "Sonuçları en sade hâlde bulalım.",
                "Birinci: $\\dfrac{7+11}{12}=\\dfrac{18}{12}=\\dfrac{3}{2}$.",
                "İkinci: $\\dfrac{9-3}{10}=\\dfrac{6}{10}=\\dfrac{3}{5}$."),
            dikkat(
                "Sonucu sadeleştirmeyi unutma.",
                "$\\dfrac{18}{12}$ doğru ama en sade değildir. Pay ve payda EBOB'larına bölünerek $\\dfrac{3}{2}$ yazılır."),
        ]},
        {"baslik": "Paydalar farklıysa: ortak payda", "icerik": [
            "Paydaları farklı kesirlerde parçalar farklı büyüklüktedir: yarım ile üçte bir aynı parça değildir. Bu yüzden önce kesirler genişletilerek <strong>aynı paydaya</strong> getirilir, sonra paylar toplanır.",
            "Ortak payda, paydaların her birinin katı olan bir sayı olmalıdır. En küçük seçenek paydaların <strong>EKOK</strong>'udur. Paydaların çarpımı da her zaman ortak paydadır ama sayıları gereksiz büyütebilir.",
            ornek(
                "$\\dfrac{5}{6}+\\dfrac{3}{8}$ işlemi verilsin.",
                "Toplamı EKOK ile bulalım.",
                "$\\text{EKOK}(6, 8)=24$.",
                "Genişletelim: $\\dfrac{5}{6}=\\dfrac{20}{24}$ ve $\\dfrac{3}{8}=\\dfrac{9}{24}$.",
                "Toplayalım: $\\dfrac{20+9}{24}=\\dfrac{29}{24}=1\\dfrac{5}{24}$."),
            "Aynı işlem paydaların çarpımıyla yapılırsa: $\\dfrac{40}{48}+\\dfrac{18}{48}=\\dfrac{58}{48}$ bulunur. Sonuç doğrudur ama sadeleştirilince yine $\\dfrac{29}{24}$ olur. EKOK kullanmak bu fazladan sadeleştirme adımını ortadan kaldırır ve sayıları küçük tuttuğu için işlem hatası olasılığını da azaltır.",
            ornek(
                "$\\dfrac{7}{15}-\\dfrac{2}{9}$ işlemi verilsin.",
                "Farkı bulalım.",
                "$\\text{EKOK}(15, 9)=45$.",
                "Genişletelim: $\\dfrac{21}{45}-\\dfrac{10}{45}$.",
                "Fark: $\\dfrac{11}{45}$."),
            "EKOK'un nasıl bulunduğu için <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısına bakabilirsin.",
            hap("Paydalar farklıysa önce paydaların EKOK'unu bul, kesirleri bu paydaya genişlet, sonra payları topla ya da çıkar.",
                "Paydaların çarpımı da işe yarar ama sonuç daha sonra sadeleştirilmelidir."),
        ]},
        {"baslik": "Ortak payda neden gerekir?", "icerik": [
            "Bir pizzanın yarısını ve aynı büyüklükteki başka bir pizzanın üçte birini düşün. İki parçayı yan yana koyduğunda toplam ne kadar pizza ettiğini söylemek için parçaları aynı birimle ölçmen gerekir. Yarım pizza ile üçte bir pizza farklı büyüklükte dilimlerdir; onları doğrudan \"iki dilim\" diye toplamak anlamsızdır.",
            "Çözüm, iki pizzayı da aynı büyüklükte dilimlere yeniden bölmektir. Her pizza $6$ eş dilime bölünürse yarım pizza $3$ dilim, üçte bir pizza $2$ dilim eder. Artık dilimler aynı büyüklükte olduğu için sayılabilir: toplam $5$ dilim, yani $\\dfrac{5}{6}$ pizza.",
            "Ortak paydanın anlamı budur: kesirleri aynı büyüklükteki parçalarla ifade etmek. $6$ seçilmesinin nedeni, hem $2$ ye hem $3$ e bölünebilen en küçük sayı olmasıdır; yani $2$ ile $3$ ün EKOK'udur.",
        ]},
        {"baslik": "Klasik yanlış: pay paya, payda paydaya", "icerik": [
            "Kesir toplamada karşılaşılan klasik yanlış, payları ve paydaları ayrı ayrı toplamaktır.",
            dikkat(
                "$\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{2}{5}$ yazmak yanlıştır.",
                "$\\dfrac{2}{5}$ yarımdan küçüktür; oysa yarıma bir şey ekleyince sonuç yarımdan büyük olmalıdır.",
                "Doğrusu: $\\dfrac{3}{6}+\\dfrac{2}{6}=\\dfrac{5}{6}$."),
            "Bu yanlışı yakalamanın kolay bir yolu, sonucun büyüklüğünü tahmin etmektir. İki pozitif kesrin toplamı, her birinden büyük olmalıdır. Bulduğun toplam kesirlerden birinden küçükse bir hata vardır.",
        ]},
        {"baslik": "Tam sayı ile kesir", "icerik": [
            "Bir tam sayı, paydası $1$ olan bir kesir gibi düşünülebilir: $3=\\dfrac{3}{1}$. Tam sayı ile kesir toplanırken ya da çıkarılırken tam sayı kesrin paydasına genişletilir.",
            ornek(
                "$3-\\dfrac{2}{5}$ ve $2+\\dfrac{3}{4}$ işlemleri verilsin.",
                "Sonuçları bileşik kesir olarak bulalım.",
                "$3=\\dfrac{15}{5}$: $\\dfrac{15}{5}-\\dfrac{2}{5}=\\dfrac{13}{5}$.",
                "$2=\\dfrac{8}{4}$: $\\dfrac{8}{4}+\\dfrac{3}{4}=\\dfrac{11}{4}$."),
            "İkinci işlemin sonucu aslında $2\\dfrac{3}{4}$ tam sayılı kesridir. Tam sayılı kesir, bir tam sayı ile bir basit kesrin toplamıdır.",
        ]},
        {"baslik": "Tam sayılı kesirlerde toplama ve çıkarma", "icerik": [
            "Tam sayılı kesirlerde iki yol vardır: ya hepsi bileşik kesre çevrilir, ya da tam kısımlar ve kesir kısımları ayrı ayrı işlenir. İkinci yol sayıları küçük tutar.",
            ornek(
                "$3\\dfrac{1}{4}+2\\dfrac{2}{3}$ işlemi verilsin.",
                "Toplamı bulalım.",
                "Tam kısımlar: $3+2=5$.",
                "Kesir kısımları: $\\dfrac{1}{4}+\\dfrac{2}{3}=\\dfrac{3}{12}+\\dfrac{8}{12}=\\dfrac{11}{12}$.",
                "Sonuç: $5\\dfrac{11}{12}$."),
            "Hangi yolun seçileceği sayılara bağlıdır. Tam kısımlar büyükse, örneğin $12\\dfrac{1}{3}+7\\dfrac{1}{2}$ gibi, ayrı işlemek sayıları küçük tutar. Tam kısımlar küçükse bileşik kesre çevirmek, ödünç alma adımını ortadan kaldırdığı için daha güvenli olabilir.",
            "<h3>Çıkarmada ödünç almak</h3>",
            "Çıkarmada kesir kısmı yetmiyorsa, tam kısımdan $1$ ödünç alınır ve kesre eklenir. Bu, tam sayılarda onlar basamağından ödünç almaya benzer.",
            ornek(
                "$5\\dfrac{1}{6}-2\\dfrac{3}{4}$ işlemi verilsin.",
                "Farkı bulalım.",
                "Kesir kısımlarını ortak paydaya getirelim: $\\dfrac{1}{6}=\\dfrac{2}{12}$ ve $\\dfrac{3}{4}=\\dfrac{9}{12}$. $\\dfrac{2}{12}$ den $\\dfrac{9}{12}$ çıkmaz.",
                "Tam kısımdan $1$ ödünç alalım: $5\\dfrac{2}{12}=4\\dfrac{14}{12}$.",
                "Şimdi çıkaralım: tam kısımlar $4-2=2$, kesir kısımları $\\dfrac{14}{12}-\\dfrac{9}{12}=\\dfrac{5}{12}$.",
                "Sonuç: $2\\dfrac{5}{12}$. Kontrol: $\\dfrac{31}{6}-\\dfrac{11}{4}=\\dfrac{62}{12}-\\dfrac{33}{12}=\\dfrac{29}{12}=2\\dfrac{5}{12}$."),
            dikkat(
                "Ödünç alınan $1$, kesrin paydası cinsinden eklenir.",
                "$5\\dfrac{2}{12}$ den $1$ ödünç alınınca kesre $\\dfrac{12}{12}$ eklenir ve $\\dfrac{14}{12}$ olur; $\\dfrac{2}{12}$ ye $1$ eklenip $\\dfrac{3}{12}$ yazılmaz."),
        ]},
        {"baslik": "Üç ya da daha fazla kesir", "icerik": [
            "Birden fazla kesir toplanırken bütün paydaların EKOK'u alınır ve kesirler tek seferde bu paydaya getirilir. Toplama ve çıkarma soldan sağa yapılır, ama hepsi aynı paydada olduğu için paylar tek satırda işlenebilir.",
            ornek(
                "$\\dfrac{1}{2}+\\dfrac{1}{3}+\\dfrac{1}{6}$ ve $\\dfrac{3}{4}-\\dfrac{1}{6}+\\dfrac{5}{12}$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "Birinci: EKOK $6$; $\\dfrac{3}{6}+\\dfrac{2}{6}+\\dfrac{1}{6}=\\dfrac{6}{6}=1$.",
                "İkinci: EKOK $12$; $\\dfrac{9}{12}-\\dfrac{2}{12}+\\dfrac{5}{12}=\\dfrac{12}{12}=1$."),
            "İlk toplam ilginç bir sonuç veriyor: yarım, üçte bir ve altıda bir bir araya gelince tam bir bütün oluşur. Bir pastayı üç kişi arasında bu oranlarla bölüştürmek pastanın tamamını dağıtır.",
        ]},
        {"baslik": "Toplamanın özelliklerini kullanmak", "icerik": [
            "Kesirlerde toplama da tam sayılardaki gibi <strong>değişme</strong> ve <strong>birleşme</strong> özelliklerine sahiptir: terimlerin yeri değiştirilebilir ve istenen terimler önce gruplanabilir. Bu özellik, paydaları aynı olan ya da toplamı tam sayı veren kesirleri bir araya getirerek hesabı kısaltır.",
            ornek(
                "$\\dfrac{1}{3}+\\dfrac{5}{7}+\\dfrac{2}{3}$ işlemi verilsin.",
                "Toplamı kısa yoldan bulalım.",
                "Paydası $3$ olanları gruplayalım: $\\left(\\dfrac{1}{3}+\\dfrac{2}{3}\\right)+\\dfrac{5}{7}$.",
                "Parantez içi $1$ eder: $1+\\dfrac{5}{7}=1\\dfrac{5}{7}$."),
            "Aynı toplam soldan sağa yapılsaydı önce $\\dfrac{1}{3}+\\dfrac{5}{7}=\\dfrac{22}{21}$ bulunur, sonra buna $\\dfrac{2}{3}=\\dfrac{14}{21}$ eklenirdi: $\\dfrac{36}{21}=\\dfrac{12}{7}$. Sonuç aynıdır ama yol uzundur.",
        ]},
        {"baslik": "Tahminle kontrol", "icerik": [
            "Kesir işlemlerinde sonucu önceden kabaca tahmin etmek, işlem hatalarını yakalamanın en kolay yoludur. Her kesri en yakın yarıma ya da tama yuvarla, tahmini hesapla ve bulduğun sonucu bu tahminle karşılaştır.",
            ornek(
                "$\\dfrac{7}{8}+\\dfrac{5}{9}$ işlemi verilsin.",
                "Sonucu önce tahmin edelim, sonra hesaplayalım.",
                "$\\dfrac{7}{8}$ yaklaşık $1$, $\\dfrac{5}{9}$ yaklaşık $\\dfrac{1}{2}$; toplam yaklaşık $1.5$ olmalı.",
                "Hesap: EKOK $72$; $\\dfrac{63}{72}+\\dfrac{40}{72}=\\dfrac{103}{72}$.",
                "$\\dfrac{103}{72}$ yaklaşık $1.43$ tür; tahminle uyumlu."),
            "Tahmin, $\\dfrac{7}{8}+\\dfrac{5}{9}=\\dfrac{12}{17}$ gibi pay paya, payda paydaya yapılan bir hatayı hemen gösterir: $\\dfrac{12}{17}$ birden küçüktür, oysa sonuç birden büyük olmalıdır.",
        ]},
        {"baslik": "Ondalık sayı ve harfli kesirlerle toplama", "icerik": [
            "Kesirlerle ondalık sayılar birlikte verildiğinde ikisini aynı biçime getirmek gerekir. Kesrin ondalık gösterimi devirliyse ondalık sayıyı kesre çevirmek daha güvenlidir.",
            ornek(
                "$0.25+\\dfrac{2}{3}$ işlemi verilsin.",
                "Toplamı kesir olarak bulalım.",
                "$0.25=\\dfrac{1}{4}$.",
                "$\\dfrac{1}{4}+\\dfrac{2}{3}=\\dfrac{3}{12}+\\dfrac{8}{12}=\\dfrac{11}{12}$."),
            "Harfli kesirlerde de ortak payda aynı yolla bulunur. Paydaları $x$ ve $2x$ olan kesirlerde ortak payda $2x$ tir: $\\dfrac{1}{x}+\\dfrac{1}{2x}=\\dfrac{2}{2x}+\\dfrac{1}{2x}=\\dfrac{3}{2x}$. Genel olarak paydaları $b$ ve $d$ olan iki kesir için:",
            "$$\\dfrac{a}{b}+\\dfrac{c}{d}=\\dfrac{a \\cdot d+b \\cdot c}{b \\cdot d}$$",
            "Bu formül paydaların çarpımını ortak payda olarak kullanır; bu yüzden sonuç sadeleştirilmeye açık olabilir.",
        ]},
        {"baslik": "Eksik kesri bulmak", "icerik": [
            "Bir toplamın ya da farkın bir terimi bilinmiyorsa, toplama ile çıkarmanın birbirinin tersi olduğu kullanılır.",
            ornek(
                "$\\dfrac{3}{4}-A=\\dfrac{1}{6}$ ve $B+\\dfrac{2}{5}=1$ eşitlikleri verilsin.",
                "$A$ ve $B$ yi bulalım.",
                "$A=\\dfrac{3}{4}-\\dfrac{1}{6}=\\dfrac{9}{12}-\\dfrac{2}{12}=\\dfrac{7}{12}$.",
                "$B=1-\\dfrac{2}{5}=\\dfrac{3}{5}$."),
        ]},
        {"baslik": "Negatif kesirlerde toplama ve çıkarma", "icerik": [
            "Negatif kesirlerde tam sayılardaki işaret kuralları aynen geçerlidir. Önce ortak payda bulunur, sonra paylar işaretleriyle birlikte toplanır. Negatif bir kesri çıkarmak, pozitifini eklemektir.",
            ornek(
                "$-\\dfrac{3}{4}+\\dfrac{1}{6}$ ve $\\dfrac{2}{5}-\\left(-\\dfrac{1}{3}\\right)$ işlemleri verilsin.",
                "Sonuçları bulalım.",
                "Birinci: EKOK $12$; $-\\dfrac{9}{12}+\\dfrac{2}{12}=-\\dfrac{7}{12}$.",
                "İkinci: negatifi çıkarmak pozitifi eklemektir: $\\dfrac{2}{5}+\\dfrac{1}{3}=\\dfrac{6}{15}+\\dfrac{5}{15}=\\dfrac{11}{15}$."),
            "Sayı doğrusunda düşünmek de yardımcı olur: negatif bir kesir eklemek sola, pozitif bir kesir eklemek sağa gitmektir. $-\\dfrac{3}{4}$ ten başlayıp $\\dfrac{1}{6}$ kadar sağa gidersen sıfıra henüz ulaşamazsın; sonucun negatif çıkması bu yüzdendir.",
            "İşaret kurallarının ayrıntısı için <a href=\"/blog/pozitif-ve-negatif-sayilar/\">Pozitif ve Negatif Sayılar</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Birbirini götüren kesirler", "icerik": [
            "Bazı uzun toplamlar ilk bakışta çok zor görünür ama her terim iki kesrin farkı olarak yazılınca terimler birbirini götürür. Bunun anahtarı şu eşitliktir:",
            "$$\\dfrac{1}{n \\cdot (n+1)}=\\dfrac{1}{n}-\\dfrac{1}{n+1}$$",
            "Doğruluğunu görmek için sağ tarafı ortak paydaya getirmek yeter: $\\dfrac{n+1}{n \\cdot (n+1)}-\\dfrac{n}{n \\cdot (n+1)}=\\dfrac{1}{n \\cdot (n+1)}$.",
            ornek(
                "$\\dfrac{1}{1 \\cdot 2}+\\dfrac{1}{2 \\cdot 3}+\\dfrac{1}{3 \\cdot 4}+\\cdots+\\dfrac{1}{9 \\cdot 10}$ toplamı verilsin.",
                "Toplamı bulalım.",
                "Her terimi fark olarak yazalım: $\\left(1-\\dfrac{1}{2}\\right)+\\left(\\dfrac{1}{2}-\\dfrac{1}{3}\\right)+\\cdots+\\left(\\dfrac{1}{9}-\\dfrac{1}{10}\\right)$.",
                "Ortadaki terimler birbirini götürür; geriye ilk ve son terim kalır.",
                "Sonuç: $1-\\dfrac{1}{10}=\\dfrac{9}{10}$."),
        ]},
        {"baslik": "Fark ne kadar büyük?", "icerik": [
            "Çıkarma, iki kesrin arasındaki farkı ölçer. \"Hangisi büyük?\" sorusunun cevabını karşılaştırma verir; \"ne kadar büyük?\" sorusunun cevabını ise çıkarma verir.",
            ornek(
                "$\\dfrac{5}{6}$ ile $\\dfrac{3}{4}$ verilsin.",
                "Büyük olan küçük olandan ne kadar büyüktür?",
                "Ortak payda $12$: $\\dfrac{10}{12}$ ve $\\dfrac{9}{12}$. Büyük olan $\\dfrac{5}{6}$ tir.",
                "Fark: $\\dfrac{10}{12}-\\dfrac{9}{12}=\\dfrac{1}{12}$."),
            "Fark küçük çıktığında iki kesir birbirine yakındır. Bu bilgi, sıralama sorularında hangi kesirlerin dikkatle karşılaştırılması gerektiğini gösterir.",
        ]},
        {"baslik": "Günlük hayatta toplama ve çıkarma", "icerik": [
            "Tarif ölçüleri, süreler ve uzunluklar kesirlerle toplanıp çıkarılır. Bu tür sorularda sonucu hem kesir hem de günlük birimle (dakika, bardak, metre) yazmak anlamı netleştirir.",
            ornek(
                "Bir tarif $\\dfrac{1}{2}$ su bardağı süt ve $\\dfrac{1}{3}$ su bardağı su istiyor.",
                "Toplam kaç su bardağı sıvı kullanılır?",
                "$\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{3}{6}+\\dfrac{2}{6}=\\dfrac{5}{6}$ su bardağı.",
                "Bir bardağın tamamından $\\dfrac{1}{6}$ bardak eksiktir."),
            ornek(
                "Bir öğrenci $1\\dfrac{1}{2}$ saat matematik, $\\dfrac{3}{4}$ saat fizik çalışıyor.",
                "Toplam çalışma süresi ne kadardır?",
                "Kesir kısımları: $\\dfrac{1}{2}+\\dfrac{3}{4}=\\dfrac{2}{4}+\\dfrac{3}{4}=\\dfrac{5}{4}=1\\dfrac{1}{4}$.",
                "Toplam: $1+1\\dfrac{1}{4}=2\\dfrac{1}{4}$ saat, yani $2$ saat $15$ dakika."),
        ]},
        {"baslik": "Adım adım yöntem", "icerik": [
            "Kesirlerde toplama ve çıkarma sorularında şu sıra izlenirse hata payı çok azalır:",
            "<ol><li>Tam sayılı kesir varsa ya bileşik kesre çevir ya da tam kısımları ayrı işle.</li>"
            "<li>Paydaları kontrol et; eşit değilse EKOK'larını bul.</li>"
            "<li>Her kesri ortak paydaya genişlet; payı da çarpmayı unutma.</li>"
            "<li>Payları işaretleriyle birlikte topla ya da çıkar, paydayı aynen yaz.</li>"
            "<li>Sonucu EBOB ile sadeleştir, gerekiyorsa tam sayılı kesre çevir.</li>"
            "<li>Sonucu kabaca bir tahminle karşılaştır.</li></ol>",
            hap("Toplama ve çıkarmada ortak payda şarttır; çarpma ve bölmede değildir.",
                "Sonucu hem sadeleştir hem de tahminle kontrol et."),
        ]},
        {"baslik": "Kesir problemleri", "icerik": [
            "Günlük hayattaki birçok soru kesirlerde toplama ve çıkarmayla çözülür. Burada bütün, $1$ olarak düşünülür ve kalan kısım $1$ den çıkarılarak bulunur.",
            ornek(
                "Bir işin $\\dfrac{1}{3}$ ini Ali, $\\dfrac{2}{5}$ sini Ayşe yapmış olsun.",
                "İşin ne kadarı yapılmadan kalmıştır?",
                "Yapılan kısım: $\\dfrac{1}{3}+\\dfrac{2}{5}=\\dfrac{5}{15}+\\dfrac{6}{15}=\\dfrac{11}{15}$.",
                "Kalan: $1-\\dfrac{11}{15}=\\dfrac{4}{15}$."),
            ornek(
                "Bir öğrenci harçlığının $\\dfrac{1}{4}$ ini kitaba, $\\dfrac{1}{6}$ ini ulaşıma harcıyor ve geriye $210$ lirası kalıyor.",
                "Harçlığı kaç liradır?",
                "Harcanan: $\\dfrac{1}{4}+\\dfrac{1}{6}=\\dfrac{3}{12}+\\dfrac{2}{12}=\\dfrac{5}{12}$.",
                "Kalan: $1-\\dfrac{5}{12}=\\dfrac{7}{12}$; bu $210$ lira.",
                "Bir parça $210:7=30$ lira; harçlık $12 \\cdot 30=360$ liradır."),
            ornek(
                "Bir su deposunun $\\dfrac{3}{8}$ ü dolu. Deponun tamamının $\\dfrac{1}{4}$ i kadar su kullanılıyor.",
                "Depoda deponun ne kadarı kadar su kalır?",
                "$\\dfrac{3}{8}-\\dfrac{1}{4}=\\dfrac{3}{8}-\\dfrac{2}{8}=\\dfrac{1}{8}$.",
                "Deponun $\\dfrac{1}{8}$ i kadar su kalır."),
            ornek(
                "Bir yolun ilk gün $\\dfrac{1}{4}$ i, ikinci gün $\\dfrac{1}{3}$ i gidiliyor ve iki günde toplam $35$ kilometre yol alınıyor.",
                "Yolun tamamı kaç kilometredir?",
                "İki günde gidilen: $\\dfrac{1}{4}+\\dfrac{1}{3}=\\dfrac{3}{12}+\\dfrac{4}{12}=\\dfrac{7}{12}$.",
                "Yolun $\\dfrac{7}{12}$ si $35$ kilometre: bir parça $35:7=5$ kilometre.",
                "Yolun tamamı $12 \\cdot 5=60$ kilometredir."),
            dikkat(
                "Kesirler aynı bütünün kesri olmalıdır.",
                "Depo örneğinde kullanılan su deponun tamamının $\\dfrac{1}{4}$ idir. Kalan suyun $\\dfrac{1}{4}$ i olsaydı işlem çıkarma değil, çarpma gerektirirdi: $\\dfrac{3}{8} \\cdot \\dfrac{3}{4}=\\dfrac{9}{32}$ kalırdı."),
        ]},
        {"baslik": "Sınavda kesirlerde toplama ve çıkarma", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu doğrudan işlem sorusu, tam sayılı kesirlerle işlem, birbirini götüren toplamlar ve kalan kısmı bulma problemleri biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde kesirlerle toplama ve çıkarma, iş ve harcama gibi problemlerin içinde de gerekebilir."),
            "Problemlerde kesirlerin hangi bütüne ait olduğunu belirlemek, işlemi seçmekten önce gelir. Aynı bütünün parçaları toplanır ya da çıkarılır; bir parçanın parçası söz konusuysa çarpma gerekir. Bu ayrımı yapmadan işleme başlamak, doğru hesapla yanlış sonuca götürür.",
            "Uzun bir işlemde bütün kesirleri baştan tek bir ortak paydaya getirmek, adım adım ikişer ikişer toplamaktan hem daha hızlı hem daha güvenlidir. Sonucu sadeleştirmeyi ve büyüklüğünü tahminle kontrol etmeyi unutma.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\dfrac{1}{2}+\\dfrac{1}{3}=\\dfrac{2}{5}$", "$\\dfrac{5}{6}$"],
                ["Paydaları da toplamak", "Payda aynen kalır"],
                ["Genişletirken yalnız paydayı çarpmak", "Pay da çarpılır"],
                ["Ödünç alınan $1$ i paya eklemek", "Payda cinsinden ekle"],
                ["Sonucu sadeleştirmemek", "EBOB ile sadeleştir"],
                ["Farklı bütünlerin kesrini toplamak", "Aynı bütüne göre yaz"],
            ]),
            "Bu hataların hepsi, paydanın parçanın büyüklüğünü anlattığını unutmaktan doğar. Payda bir adı gösterir, bir miktarı değil: aynı adlı parçalar toplanır, adlar toplanmaz.",
        ]},
    ],
    "sss": [
        ("Paydaları eşit kesirler nasıl toplanır?",
         "Paylar toplanır, payda aynen kalır. Örneğin yedide iki ile yedide üçün toplamı yedide beştir."),
        ("Paydaları farklı kesirler nasıl toplanır?",
         "Önce paydaların EKOK'u bulunur, kesirler bu ortak paydaya genişletilir, sonra paylar toplanır."),
        ("Kesirleri toplarken paydalar neden toplanmaz?",
         "Payda parçanın büyüklüğünü gösterir. Aynı büyüklükteki parçaları bir araya getirmek parçanın büyüklüğünü değiştirmez; yalnızca parça sayısı değişir."),
        ("Negatif kesirler nasıl toplanır?",
         "Önce ortak payda bulunur, sonra paylar işaretleriyle birlikte toplanır. Negatif bir kesri çıkarmak, aynı kesrin pozitifini eklemekle aynıdır."),
        ("Tam sayılı kesirlerde çıkarma nasıl yapılır?",
         "Tam kısımlar ve kesir kısımları ayrı çıkarılır. Kesir kısmı yetmezse tam kısımdan 1 ödünç alınır ve payda cinsinden kesre eklenir."),
        ("Kesirlerde toplama işleminin sonucu nasıl kontrol edilir?",
         "Her kesir en yakın yarıma ya da tama yuvarlanarak sonuç kabaca tahmin edilir. Bulunan sonuç bu tahminden çok uzaksa işlemde bir hata vardır."),
        ("Kesir toplamada sonuç neden sadeleştirilir?",
         "Sadeleştirilmiş sonuç aynı değeri en küçük sayılarla gösterir. Böylece sonucu okumak, karşılaştırmak ve sonraki işlemlerde kullanmak kolaylaşır."),
        ("Ortak payda olarak paydaların çarpımı kullanılabilir mi?",
         "Evet, her zaman ortak paydadır ama sayıları büyütür. EKOK kullanmak sonucu daha az sadeleştirme gerektirir."),
        ("Ardışık iki sayının çarpımının tersi nasıl yazılır?",
         "1 bölü n ile 1 bölü n artı 1 in farkı olarak yazılır. Bu eşitlik, ardışık kesirlerin toplamlarında terimlerin birbirini götürmesini sağlar."),
    ],
    "kontrol": [
        "Paydaları eşit kesirleri toplayıp çıkarabiliyorum.",
        "Paydanın neden toplanmadığını açıklayabiliyorum.",
        "Farklı paydalı kesirleri EKOK ile ortak paydaya getirebiliyorum.",
        "Sonucu EBOB ile en sade hâline getirebiliyorum.",
        "Tam sayı ile kesri toplayıp çıkarabiliyorum.",
        "Tam sayılı kesirlerde ödünç alarak çıkarma yapabiliyorum.",
        "Üç ya da daha fazla kesri tek ortak paydada işleyebiliyorum.",
        "Negatif kesirlerle toplama ve çıkarma yapabiliyorum.",
        "Birbirini götüren kesir toplamlarını fark yazarak hesaplayabiliyorum.",
        "Kalan kısım problemlerini bütünü $1$ alarak çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kesirlerde-carpma-ve-bolme", "kesirler-konu-anlatimi-pdf", "ebob-ve-ekok-konu-anlatimi-pdf"],
}
