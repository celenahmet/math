# scripts/yazilar/62_koklu_sayilar.py — Koklu Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "koklu-sayilar-konu-anlatimi-pdf",
    "baslik": "Köklü Sayılar Konu Anlatımı PDF",
    "aciklama": "Köklü sayılar nedir? Karekök ve küpkök, kök dışına çıkarma, dört işlem, paydayı rasyonel yapma, iç içe kök ve köklü denklemler; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "koklu-sayilar-konu-anlatimi-pdf",
    "kapak_alt": "Köklü sayılar: kare biçimli ahşap çerçevede mavi karelerden oluşan alanı ve kenar uzunluğunu inceleyen iki öğrenci",
    "ozet": "Köklü sayılar kuvvet almanın tersidir: karesi 9 olan pozitif sayıyı, küpü 8 olan sayıyı arar. Bu yazıda karekökü ve daha yüksek dereceli kökleri tanımlıyor, kökün üslü sayıyla bağlantısını kuruyor, kök dışına çıkarmayı, köklü sayılarda dört işlemi, paydayı rasyonel yapmayı, iç içe kökleri ve yabancı köklere dikkat ederek köklü denklemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Karekök nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için üslü sayıların kurallarını ve mutlak değeri biliyor olman yeterli.",
                "Kuvvet kuralları için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısına göz at."),
            "Negatif olmayan bir $a$ sayısının <strong>karekökü</strong>, karesi $a$ olan negatif olmayan sayıdır ve $\\sqrt{a}$ biçiminde gösterilir. Örneğin $3^2=9$ olduğu için $\\sqrt{9}=3$ tür. Geometride bunun anlamı açıktır: alanı $9$ birimkare olan bir karenin kenar uzunluğu $\\sqrt{9}=3$ birimdir.",
            "Karekök, karesi alınınca içerideki sayıyı veren sayıdır; bu yüzden $a \\geq 0$ için $(\\sqrt{a})^2=a$ dır. Gerçek sayılarda negatif bir sayının karekökü tanımlı değildir, çünkü hiçbir gerçek sayının karesi negatif olamaz.",
            dikkat(
                "$\\sqrt{9}=\\pm 3$ yazmak yanlıştır.",
                "Karekök her zaman negatif olmayan sonucu verir: $\\sqrt{9}=3$.",
                "$\\pm 3$ ise $x^2=9$ denkleminin çözümleridir. Denklem iki çözümlü, karekök tek değerlidir."),
            "Karesi bir tam sayı olan sayılara <strong>tam kare</strong> denir. İlk tam kareler $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225$ tir. Bu listeyi bilmek, kök dışına çıkarma işlemlerini çok hızlandırır.",
            "Tam kare olmayan bir doğal sayının karekökü irrasyoneldir: $\\sqrt{2}$, $\\sqrt{3}$, $\\sqrt{5}$ gibi sayılar kesir olarak yazılamaz ve ondalık gösterimleri devretmeden sonsuza kadar sürer. Bu sayıların ayrıntısı <a href=\"/blog/irrasyonel-sayilar-ve-gercek-sayilar/\">İrrasyonel Sayılar ve Gerçek Sayılar</a> yazısında.",
        ]},
        {"baslik": "Küpkök ve n inci dereceden kök", "icerik": [
            "Küpü $a$ olan sayıya $a$ nın <strong>küpkökü</strong> denir ve $\\sqrt[3]{a}$ ile gösterilir: $2^3=8$ olduğu için $\\sqrt[3]{8}=2$. Genel olarak $\\sqrt[n]{a}$, $n$ inci kuvveti $a$ olan sayıdır; $n$ ye kökün <strong>derecesi</strong> denir.",
            "Derecenin tek ya da çift olması tanım kümesini değiştirir:",
            "<ul><li><strong>Tek dereceli kök:</strong> her gerçek sayı için tanımlıdır ve işaret korunur. $\\sqrt[3]{-8}=-2$ dir, çünkü $(-2)^3=-8$.</li>"
            "<li><strong>Çift dereceli kök:</strong> yalnızca negatif olmayan sayılar için tanımlıdır ve sonuç negatif olmaz. $\\sqrt[4]{16}=2$ dir; $\\sqrt[4]{-16}$ gerçek sayılarda tanımsızdır.</li></ul>",
            hap("Çift dereceli kökün içi negatif olamaz ve sonucu negatif olmaz.",
                "Tek dereceli kök her gerçek sayıda tanımlıdır ve içerideki sayının işaretini korur."),
        ]},
        {"baslik": "Kökün tanımlı olduğu değerler", "icerik": [
            "Kök içinde bir bilinmeyen varsa ifadenin hangi değerler için tanımlı olduğuna dikkat etmek gerekir. Çift dereceli kökte içerisi negatif olamaz; tek dereceli kökte ise bir kısıt yoktur. Bu koşul, köklü denklemlerde bulunan köklerin kontrolünde de işe yarar.",
            ornek(
                "$\\sqrt{x-3}$ ve $\\sqrt[3]{x-3}$ ifadeleri verilsin.",
                "Hangi $x$ değerleri için tanımlı olduklarını bulalım.",
                "$\\sqrt{x-3}$ için $x-3 \\geq 0$, yani $x \\geq 3$.",
                "$\\sqrt[3]{x-3}$ her gerçek $x$ için tanımlıdır."),
            ornek(
                "$\\sqrt{5-x}+\\sqrt{x-1}$ ifadesi verilsin.",
                "İfadeyi tanımlı yapan tam sayıların sayısını bulalım.",
                "İki kökün içi de negatif olmamalı: $5-x \\geq 0$ ve $x-1 \\geq 0$.",
                "Buradan $1 \\leq x \\leq 5$.",
                "Tam sayılar $1, 2, 3, 4, 5$: toplam $5$ tane."),
        ]},
        {"baslik": "Köklü sayıyı üslü yazmak", "icerik": [
            "Kök, kesirli bir üs olarak da yazılabilir. $a>0$ için:",
            "$$\\sqrt[n]{a^m}=a^{\\frac{m}{n}}$$",
            "Özel olarak $\\sqrt{a}=a^{\\frac{1}{2}}$ ve $\\sqrt[3]{a}=a^{\\frac{1}{3}}$ tür. Bu yazım sayesinde üslü sayıların bütün kuralları köklü sayılarda da kullanılabilir.",
            ornek(
                "$8^{\\frac{2}{3}}$ ve $27^{-\\frac{1}{3}}$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$8^{\\frac{2}{3}}=(\\sqrt[3]{8})^2=2^2=4$.",
                "$27^{-\\frac{1}{3}}=\\dfrac{1}{27^{\\frac{1}{3}}}=\\dfrac{1}{\\sqrt[3]{27}}=\\dfrac{1}{3}$."),
            ornek(
                "$\\sqrt{2} \\cdot \\sqrt[3]{2}$ çarpımı verilsin.",
                "Sonucu tek bir kök olarak yazalım.",
                "Üslü yazalım: $2^{\\frac{1}{2}} \\cdot 2^{\\frac{1}{3}}=2^{\\frac{1}{2}+\\frac{1}{3}}=2^{\\frac{5}{6}}$.",
                "Kök olarak: $2^{\\frac{5}{6}}=\\sqrt[6]{2^5}=\\sqrt[6]{32}$."),
        ]},
        {"baslik": "Kök dışına çıkarma", "icerik": [
            "Kökün içindeki sayı, bir tam kare ile başka bir sayının çarpımı olarak yazılabiliyorsa tam kare kısım kök dışına çıkarılır. $a \\geq 0$ ve $b \\geq 0$ için:",
            "$$\\sqrt{a^2 \\cdot b}=a\\sqrt{b}$$",
            "Pratikte içerideki sayının <strong>en büyük</strong> tam kare çarpanı aranır. Küçük bir tam kare seçilirse işlem bir adımda bitmez.",
            ornek(
                "$\\sqrt{72}$, $\\sqrt{48}$ ve $\\sqrt[3]{54}$ sayıları verilsin.",
                "Kök dışına çıkarılabilen kısımları çıkaralım.",
                "$72=36 \\cdot 2$: $\\sqrt{72}=6\\sqrt{2}$.",
                "$48=16 \\cdot 3$: $\\sqrt{48}=4\\sqrt{3}$.",
                "$54=27 \\cdot 2$ ve $27=3^3$: $\\sqrt[3]{54}=3\\sqrt[3]{2}$."),
            hap("Kök dışına çıkarırken kök içindeki en büyük tam kare çarpanı ara.",
                "Dışarıdaki pozitif bir sayı kök içine karesi alınarak girer: $3\\sqrt{5}=\\sqrt{45}$."),
            "Tersine, kökün dışındaki bir pozitif sayı karesi alınarak içeri taşınır: $3\\sqrt{5}=\\sqrt{9 \\cdot 5}=\\sqrt{45}$. Bu işlem köklü sayıları karşılaştırırken işe yarar.",
            "<h3>Karekök ve mutlak değer</h3>",
            "Bir sayının karesinin karekökü, sayının kendisi değil mutlak değeridir: $\\sqrt{x^2}=|x|$. Örneğin $\\sqrt{(-5)^2}=\\sqrt{25}=5$ tir. Tek dereceli köklerde ise işaret korunduğu için $\\sqrt[3]{x^3}=x$ dir. Mutlak değerin ayrıntısı için <a href=\"/blog/mutlak-deger-konu-anlatimi-pdf/\">Mutlak Değer Konu Anlatımı PDF</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Köklü sayılarda toplama ve çıkarma", "icerik": [
            "Köklü sayılar yalnızca <strong>kök içleri ve dereceleri aynıysa</strong> toplanıp çıkarılabilir; bu durumda katsayılar toplanır, kök aynen kalır. Bu, cebirdeki benzer terimlerin toplanmasına benzer: $2x+3x=5x$ olduğu gibi $2\\sqrt{3}+3\\sqrt{3}=5\\sqrt{3}$ tür. Kök içleri farklı görünüyorsa önce kök dışına çıkarma denenir.",
            ornek(
                "$\\sqrt{12}+\\sqrt{27}-\\sqrt{3}$ ifadesi verilsin.",
                "İfadeyi sadeleştirelim.",
                "Kök dışına çıkaralım: $\\sqrt{12}=2\\sqrt{3}$ ve $\\sqrt{27}=3\\sqrt{3}$.",
                "Kök içleri aynı oldu: $2\\sqrt{3}+3\\sqrt{3}-\\sqrt{3}=4\\sqrt{3}$."),
            dikkat(
                "$\\sqrt{2}+\\sqrt{3}=\\sqrt{5}$ yazmak yanlıştır.",
                "$\\sqrt{2}$ yaklaşık $1.41$, $\\sqrt{3}$ yaklaşık $1.73$; toplamları yaklaşık $3.15$ tir. $\\sqrt{5}$ ise yaklaşık $2.24$ tür. Kök içleri toplamada birleştirilmez."),
        ]},
        {"baslik": "Köklü sayılarda çarpma ve bölme", "icerik": [
            "Aynı dereceli kökler çarpılırken ve bölünürken kök içleri birleştirilir. $a \\geq 0$ ve $b \\geq 0$ için:",
            "$$\\sqrt{a} \\cdot \\sqrt{b}=\\sqrt{a \\cdot b} \\text{ ve } \\dfrac{\\sqrt{a}}{\\sqrt{b}}=\\sqrt{\\dfrac{a}{b}}$$",
            "Bölmede ayrıca $b \\neq 0$ olmalıdır.",
            ornek(
                "$\\sqrt{8} \\cdot \\sqrt{2}$, $\\dfrac{\\sqrt{50}}{\\sqrt{2}}$ ve $\\sqrt[3]{2} \\cdot \\sqrt[3]{4}$ verilsin.",
                "Değerlerini bulalım.",
                "$\\sqrt{8} \\cdot \\sqrt{2}=\\sqrt{16}=4$.",
                "$\\dfrac{\\sqrt{50}}{\\sqrt{2}}=\\sqrt{25}=5$.",
                "$\\sqrt[3]{2} \\cdot \\sqrt[3]{4}=\\sqrt[3]{8}=2$."),
            dikkat(
                "Çarpma kuralının koşulu, çift dereceli köklerde içlerin negatif olmamasıdır.",
                "$\\sqrt{-4} \\cdot \\sqrt{-9}$ gerçek sayılarda tanımsızdır; bu yüzden onu $\\sqrt{36}=6$ diye hesaplamak yanlıştır. Tek dereceli köklerde böyle bir kısıt yoktur."),
        ]},
        {"baslik": "Kuvvet alma ve iki terimli çarpımlar", "icerik": [
            "Köklü bir sayının kuvveti alınırken kök üslü biçimde düşünülür: $(\\sqrt{3})^4=(3^{\\frac{1}{2}})^4=3^2=9$ ve $(\\sqrt[3]{2})^6=2^2=4$ tür. Katsayılı köklerde katsayının da kuvveti alınır: $(2\\sqrt{2})^2=4 \\cdot 2=8$.",
            "İki terimli köklü ifadeler çarpılırken dağılma özelliği ve özdeşlikler kullanılır. İki kare farkı ile tam kare özdeşliği en işe yarayanlarıdır.",
            ornek(
                "$(\\sqrt{5}+\\sqrt{3})(\\sqrt{5}-\\sqrt{3})$ ve $(\\sqrt{3}+1)^2$ ifadeleri verilsin.",
                "İkisini de hesaplayalım.",
                "İki kare farkı: $(\\sqrt{5})^2-(\\sqrt{3})^2=5-3=2$.",
                "Tam kare: $(\\sqrt{3})^2+2 \\cdot \\sqrt{3} \\cdot 1+1^2=3+2\\sqrt{3}+1=4+2\\sqrt{3}$."),
            "<h3>Farklı dereceli kökleri çarpmak</h3>",
            "Dereceleri farklı kökler doğrudan birleştirilemez. Önce dereceler, en küçük ortak katlarına eşitlenir; bunun için kök içindeki sayının da uygun kuvveti alınır.",
            ornek(
                "$\\sqrt{2} \\cdot \\sqrt[3]{3}$ çarpımı verilsin.",
                "Sonucu tek bir kök olarak yazalım.",
                "$2$ ile $3$ ün en küçük ortak katı $6$: $\\sqrt{2}=\\sqrt[6]{2^3}=\\sqrt[6]{8}$ ve $\\sqrt[3]{3}=\\sqrt[6]{3^2}=\\sqrt[6]{9}$.",
                "Dereceler eşit oldu: $\\sqrt[6]{8} \\cdot \\sqrt[6]{9}=\\sqrt[6]{72}$."),
        ]},
        {"baslik": "Kesirli köklü ifadeleri sadeleştirme", "icerik": [
            "Payı birden fazla terimden oluşan bir kesir, her terim ayrı ayrı paydaya bölünerek sadeleştirilebilir. Bu yöntem, paydayı rasyonel yapmaktan daha kısa olabilir.",
            ornek(
                "$\\dfrac{\\sqrt{12}+\\sqrt{18}}{\\sqrt{6}}$ ifadesi verilsin.",
                "İfadeyi sadeleştirelim.",
                "Her terimi ayrı bölelim: $\\dfrac{\\sqrt{12}}{\\sqrt{6}}+\\dfrac{\\sqrt{18}}{\\sqrt{6}}=\\sqrt{2}+\\sqrt{3}$.",
                "Bölme kuralını kullandık: $\\dfrac{\\sqrt{12}}{\\sqrt{6}}=\\sqrt{\\dfrac{12}{6}}$ ve $\\dfrac{\\sqrt{18}}{\\sqrt{6}}=\\sqrt{\\dfrac{18}{6}}$."),
        ]},
        {"baslik": "Paydayı rasyonel yapmak", "icerik": [
            "Paydasında kök bulunan bir kesri sadeleştirmek için pay ve payda aynı sayıyla çarpılır ve paydadaki kök kaldırılır. Bu işleme <strong>paydayı rasyonel yapmak</strong> denir.",
            ornek(
                "$\\dfrac{1}{\\sqrt{2}}$ ve $\\dfrac{6}{\\sqrt{3}}$ kesirleri verilsin.",
                "Paydalarını rasyonel yapalım.",
                "$\\dfrac{1}{\\sqrt{2}}=\\dfrac{\\sqrt{2}}{\\sqrt{2} \\cdot \\sqrt{2}}=\\dfrac{\\sqrt{2}}{2}$.",
                "$\\dfrac{6}{\\sqrt{3}}=\\dfrac{6\\sqrt{3}}{3}=2\\sqrt{3}$."),
            "Paydada iki terim varsa <strong>eşlenik</strong> kullanılır. $\\sqrt{a}-\\sqrt{b}$ nin eşleniği $\\sqrt{a}+\\sqrt{b}$ dir ve iki kare farkı özdeşliğiyle çarpımları kökten kurtulur:",
            "$$(\\sqrt{a}-\\sqrt{b})(\\sqrt{a}+\\sqrt{b})=a-b$$",
            ornek(
                "$\\dfrac{1}{\\sqrt{3}-\\sqrt{2}}$ ve $\\dfrac{4}{\\sqrt{5}+1}$ kesirleri verilsin.",
                "Paydalarını rasyonel yapalım.",
                "Birincide eşlenik $\\sqrt{3}+\\sqrt{2}$: payda $3-2=1$ olur ve kesir $\\sqrt{3}+\\sqrt{2}$ ye eşittir.",
                "İkincide eşlenik $\\sqrt{5}-1$: payda $5-1=4$ olur ve kesir $\\dfrac{4(\\sqrt{5}-1)}{4}=\\sqrt{5}-1$ e eşittir."),
            hap("Paydada tek kök varsa aynı kökle, iki terim varsa eşlenikle çarp.",
                "Eşleniklerin çarpımı iki kare farkıdır: $(\\sqrt{a}-\\sqrt{b})(\\sqrt{a}+\\sqrt{b})=a-b$."),
        ]},
        {"baslik": "İç içe kökler", "icerik": [
            "$\\sqrt{7+2\\sqrt{10}}$ gibi iç içe bir kök, bazen iki kökün toplamı ya da farkı olarak yazılabilir. $x \\geq y \\geq 0$ olmak üzere:",
            "$$\\sqrt{x+y+2\\sqrt{x \\cdot y}}=\\sqrt{x}+\\sqrt{y} \\text{ ve } \\sqrt{x+y-2\\sqrt{x \\cdot y}}=\\sqrt{x}-\\sqrt{y}$$",
            "Yöntem şudur: içteki kökün önünde $2$ olacak biçimde yaz, sonra toplamı dıştaki sayıya, çarpımı içteki köke eşit iki sayı ara. Farklı durumunda büyük sayının kökü önce yazılır ki sonuç negatif çıkmasın.",
            ornek(
                "$\\sqrt{7+2\\sqrt{10}}$ ve $\\sqrt{5-2\\sqrt{6}}$ verilsin.",
                "İkisini de sadeleştirelim.",
                "Toplamı $7$, çarpımı $10$ olan sayılar $5$ ve $2$: $\\sqrt{7+2\\sqrt{10}}=\\sqrt{5}+\\sqrt{2}$.",
                "Toplamı $5$, çarpımı $6$ olan sayılar $3$ ve $2$: $\\sqrt{5-2\\sqrt{6}}=\\sqrt{3}-\\sqrt{2}$.",
                "Kontrol: $(\\sqrt{5}+\\sqrt{2})^2=5+2+2\\sqrt{10}=7+2\\sqrt{10}$."),
            dikkat(
                "İçteki kökün önünde $2$ yoksa önce onu oluştur.",
                "$\\sqrt{4+\\sqrt{12}}$ için $\\sqrt{12}=2\\sqrt{3}$ yazılır: $\\sqrt{4+2\\sqrt{3}}=\\sqrt{3}+1$, çünkü $3+1=4$ ve $3 \\cdot 1=3$."),
        ]},
        {"baslik": "Sonsuz iç içe kök", "icerik": [
            "$\\sqrt{6+\\sqrt{6+\\sqrt{6+\\cdots}}}$ gibi sonsuza kadar süren bir ifadede, ifadenin kendisi kendi içinde tekrar eder. Bu tekrar bir denklem kurmayı sağlar.",
            ornek(
                "$x=\\sqrt{6+\\sqrt{6+\\sqrt{6+\\cdots}}}$ olsun.",
                "$x$ in değerini bulalım.",
                "İlk kökün içindeki ifade yine $x$ tir: $x=\\sqrt{6+x}$.",
                "Karesini alalım: $x^2=6+x$, yani $x^2-x-6=0$ ve $(x-3)(x+2)=0$.",
                "Karekök negatif olamayacağı için $x=-2$ elenir; $x=3$."),
            dikkat(
                "Bu yöntemde de elenmesi gereken kök çıkabilir.",
                "Kare alma adımı $x=-2$ gibi negatif bir değer üretebilir. Karekökle tanımlanan bir ifade negatif olamayacağı için bu değer atılır."),
        ]},
        {"baslik": "Köklü denklemler ve yabancı kök", "icerik": [
            "Bilinmeyen kök içindeyse iki tarafın karesi alınır. Ama kare alma işlemi yeni, sahte çözümler doğurabilir; bunlara <strong>yabancı kök</strong> denir. Bu yüzden bulunan her kök mutlaka ilk denklemde kontrol edilir.",
            ornek(
                "$\\sqrt{x+3}=5$ denklemi verilsin.",
                "$x$ i bulalım.",
                "Karesini alalım: $x+3=25$.",
                "$x=22$. Kontrol: $\\sqrt{25}=5$ sağlanır."),
            ornek(
                "$\\sqrt{2x-1}=x-2$ denklemi verilsin.",
                "Çözüm kümesini bulalım.",
                "Karesini alalım: $2x-1=x^2-4x+4$, yani $x^2-6x+5=0$.",
                "Çarpanlara ayıralım: $(x-1)(x-5)=0$; adaylar $x=1$ ve $x=5$.",
                "$x=1$ için sol taraf $\\sqrt{1}=1$, sağ taraf $-1$: sağlanmaz, yabancı köktür.",
                "$x=5$ için sol taraf $\\sqrt{9}=3$, sağ taraf $3$: sağlanır. Çözüm kümesi $\\{5\\}$."),
            "Yabancı kökün nedeni şudur: $\\sqrt{2x-1}$ hiçbir zaman negatif olmaz, ama kare alındıktan sonra denklem $\\sqrt{2x-1}=-(x-2)$ durumunu da kapsar hâle gelir. Kontrol adımı bu fazlalığı ayıklar.",
        ]},
        {"baslik": "Köklü sayıları tahmin etme ve sıralama", "icerik": [
            "Bir köklü sayının hangi iki tam sayı arasında olduğunu bulmak için kök içine en yakın tam kareler aranır. $\\sqrt{50}$ için $49<50<64$ olduğundan $7<\\sqrt{50}<8$ dir ve $50$, $49$ a çok yakın olduğu için $\\sqrt{50}$ de $7$ ye yakındır.",
            "Bilinmesi yararlı yaklaşık değerler: $\\sqrt{2}$ yaklaşık $1.414$, $\\sqrt{3}$ yaklaşık $1.732$, $\\sqrt{5}$ yaklaşık $2.236$. Köklü sayıları sıralamak için hepsini tek bir kökün içine almak en güvenilir yoldur; ayrıntısı <a href=\"/blog/sayi-dogrusu-ve-sayilari-siralama/\">Sayı Doğrusu ve Sayıları Sıralama</a> yazısında.",
            "Aynı yöntem daha büyük sayılarda da işler. $\\sqrt{130}$ için $121<130<144$ olduğundan $11<\\sqrt{130}<12$ dir; $130$, $121$ e $144$ ten daha yakın olduğu için $\\sqrt{130}$ da $11$ e daha yakındır.",
            ornek(
                "$\\sqrt{10}$, $2\\sqrt{3}$ ve $3$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Hepsini kök içine alalım: $\\sqrt{10}$, $2\\sqrt{3}=\\sqrt{12}$, $3=\\sqrt{9}$.",
                "Kök içleri: $9<10<12$.",
                "Sıralama: $3<\\sqrt{10}<2\\sqrt{3}$."),
        ]},
        {"baslik": "Köklü sayılar ve geometri", "icerik": [
            "Köklü sayılar geometride uzunluk olarak doğal biçimde ortaya çıkar. Dik üçgende dik kenarların kareleri toplamı hipotenüsün karesine eşittir; bu yüzden kenarlar tam sayı olsa bile hipotenüs köklü çıkabilir.",
            ornek(
                "Kenarı $1$ birim olan bir kare ve alanı $50$ birimkare olan başka bir kare verilsin.",
                "Birinci karenin köşegenini ve ikinci karenin kenarını bulalım.",
                "Köşegen, dik kenarları $1$ olan dik üçgenin hipotenüsüdür: $\\sqrt{1^2+1^2}=\\sqrt{2}$ birim.",
                "İkinci karenin kenarı: $\\sqrt{50}=\\sqrt{25 \\cdot 2}=5\\sqrt{2}$ birim."),
            "Buradan bir sonuç daha çıkar: kenarı $a$ olan bir karenin köşegeni her zaman $a\\sqrt{2}$ dir. Kenarı $5$ olan karenin köşegeni $5\\sqrt{2}$, yani alanı $50$ olan karenin kenarıyla aynıdır.",
        ]},
        {"baslik": "Sınavda köklü sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu kök dışına çıkarma, köklü ifadeleri sadeleştirme, paydayı rasyonel yapma, iç içe kök ve sıralama biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde köklü sayı bilgisi işlemi kısaltmak ya da bir değeri tahmin etmek için de gerekebilir."),
            "Bulduğun sonucu kontrol etmenin kısa bir yolu, sonucun karesini almaktır. Örneğin $\\sqrt{7+2\\sqrt{10}}=\\sqrt{5}+\\sqrt{2}$ sonucunun karesi $7+2\\sqrt{10}$ olduğu için sonuç doğrudur. Paydası rasyonel yapılmış bir kesri de ilk kesirle çapraz çarparak kontrol edebilirsin.",
            "Köklü ifadelerde iyi bir ilk adım, kök içlerini en sade hâle getirmektir. Kök içleri sadeleşince toplanabilecek terimler ve birbirini götüren çarpanlar kendiliğinden ortaya çıkar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\sqrt{9}=\\pm 3$ yazmak", "$\\sqrt{9}=3$"],
                ["$\\sqrt{2}+\\sqrt{3}=\\sqrt{5}$ yazmak", "Kök içleri toplanmaz"],
                ["$\\sqrt{x^2}=x$ yazmak", "$\\sqrt{x^2}=|x|$"],
                ["$\\sqrt{-4} \\cdot \\sqrt{-9}=6$ yazmak", "Gerçek sayılarda tanımsız"],
                ["$3\\sqrt{2}=\\sqrt{6}$ yazmak", "$3\\sqrt{2}=\\sqrt{18}$"],
                ["Köklü denklemde kontrol yapmamak", "Yabancı kökü ayıkla"],
            ]),
            "Bu hataların çoğu, kökü sıradan bir işlem gibi toplama ve çıkarmaya dağıtmaktan ya da kökün tanım koşulunu unutmaktan doğar. Her adımda kök içinin negatif olmadığını ve sonucun negatif çıkmadığını kontrol et.",
        ]},
    ],
    "sss": [
        ("Karekök nedir?",
         "Negatif olmayan bir sayının karekökü, karesi o sayıya eşit olan negatif olmayan sayıdır. Örneğin 9 un karekökü 3 tür."),
        ("Karekök 9 neden artı eksi 3 değildir?",
         "Karekök tanım gereği negatif olmayan tek bir değer verir; bu yüzden 9 un karekökü 3 tür. Artı eksi 3, x kare eşittir 9 denkleminin iki çözümüdür."),
        ("Negatif sayının karekökü alınır mı?",
         "Gerçek sayılarda alınmaz, çünkü hiçbir gerçek sayının karesi negatif değildir. Tek dereceli kökler ise negatif sayılarda da tanımlıdır."),
        ("Kök dışına nasıl çıkarılır?",
         "Kök içindeki sayı en büyük tam kare çarpanı ile başka bir sayının çarpımı olarak yazılır ve tam karenin karekökü dışarı çıkarılır."),
        ("Köklü sayılar nasıl toplanır?",
         "Yalnızca kök içleri ve dereceleri aynıysa katsayılar toplanır. Kök içleri farklıysa önce kök dışına çıkarma denenir."),
        ("Paydayı rasyonel yapmak ne demek?",
         "Paydadaki kökü kaldırmak için kesri uygun bir sayıyla genişletmektir. Paydada tek kök varsa aynı kök, iki terim varsa eşlenik kullanılır."),
        ("Farklı dereceli kökler nasıl çarpılır?",
         "Önce kök dereceleri en küçük ortak katlarına eşitlenir ve kök içindeki sayıların uygun kuvvetleri alınır. Dereceler eşitlenince kök içleri çarpılır."),
        ("Yabancı kök nedir?",
         "Köklü denklemde kare alırken ortaya çıkan ama ilk denklemi sağlamayan değerdir. Bulunan her kök ilk denklemde kontrol edilerek ayıklanır."),
    ],
    "kontrol": [
        "Karekökün neden negatif olmayan tek bir değer verdiğini açıklayabiliyorum.",
        "Tek ve çift dereceli köklerin tanım koşullarını ayırt edebiliyorum.",
        "Köklü bir sayıyı kesirli üs olarak yazabiliyorum.",
        "Kök içindeki en büyük tam kare çarpanı bulup kök dışına çıkarabiliyorum.",
        "$\\sqrt{x^2}=|x|$ eşitliğini kullanabiliyorum.",
        "Kök içleri aynı olan terimleri toplayıp çıkarabiliyorum.",
        "Köklü sayılarda çarpma ve bölme kurallarını koşuluyla uygulayabiliyorum.",
        "Paydayı tek kökle ya da eşlenikle rasyonel yapabiliyorum.",
        "İç içe kökü iki kökün toplamı ya da farkı olarak yazabiliyorum.",
        "Köklü denklemde yabancı kökü kontrol ederek ayıklayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["uslu-sayilar-konu-anlatimi-pdf", "irrasyonel-sayilar-ve-gercek-sayilar", "mutlak-deger-konu-anlatimi-pdf"],
}
