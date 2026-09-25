# scripts/yazilar/61_uslu_sayilar.py — Uslu Sayilar (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "uslu-sayilar-konu-anlatimi-pdf",
    "baslik": "Üslü Sayılar Konu Anlatımı PDF",
    "aciklama": "Üslü sayılar nedir? Sıfır ve negatif üs, çarpma ve bölme kuralları, ortak paranteze alma, üslü denklemler, bilimsel gösterim; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "uslu-sayilar-konu-anlatimi-pdf",
    "kapak_alt": "Üslü sayılar: tekrarlı çarpmayı gösteren, katman katman büyüyen mavi küp yapısı kuran iki öğrenci",
    "ozet": "Üslü sayılar, aynı sayının tekrar tekrar çarpılmasını kısa yoldan yazmanın yoludur ve çok büyük ya da çok küçük sayılarla çalışmayı mümkün kılar. Bu yazıda üslü sayıyı tanımlıyor, sıfır ve negatif üslerin neden öyle tanımlandığını gösteriyor, çarpma, bölme ve üssün üssü kurallarını, toplamada ortak paranteze almayı, üslü denklemleri, bilimsel gösterimi ve son basamak sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Üslü sayı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi ve negatif sayılarda işaret kurallarını biliyor olman yeterli.",
                "Negatif sayılarla çarpma için <a href=\"/blog/pozitif-ve-negatif-sayilar/\">Pozitif ve Negatif Sayılar</a> yazısına göz at."),
            "Bir sayının kendisiyle tekrar tekrar çarpılmasına <strong>kuvvet alma</strong> denir. $a$ sayısının $n$ tane çarpımı kısaca $a^n$ biçiminde yazılır ve \"$a$ nın $n$ inci kuvveti\" ya da \"$a$ üzeri $n$\" diye okunur. Burada $a$ ya <strong>taban</strong>, $n$ ye <strong>üs</strong> denir.",
            "$$a^n=a \\cdot a \\cdot a \\cdots a$$",
            "Örneğin $2^5=2 \\cdot 2 \\cdot 2 \\cdot 2 \\cdot 2=32$ dir. İkinci kuvvete <strong>kare</strong>, üçüncü kuvvete <strong>küp</strong> de denir: $5^2=25$, \"beşin karesi\"; $3^3=27$, \"üçün küpü\" diye okunur.",
            hap("$a^n$, $a$ nın kendisiyle $n$ kez çarpımıdır; $a$ taban, $n$ üstür.",
                "Üs, tabanla çarpılmaz: $2^5$, $2 \\cdot 5$ değil, $32$ dir."),
        ]},
        {"baslik": "Özel üsler: bir, sıfır ve negatif", "icerik": [
            "Birinci kuvvet sayının kendisidir: $a^1=a$. Birin her kuvveti birdir: $1^n=1$. Sıfırın pozitif her kuvveti sıfırdır: $n>0$ için $0^n=0$.",
            "<h3>Sıfırıncı kuvvet</h3>",
            "Sıfırdan farklı her sayının sıfırıncı kuvveti $1$ dir: $a \\neq 0$ için $a^0=1$. Bu bir ezber değil, bölme kuralının sonucudur. Bir sayıyı kendisine bölersek $1$ buluruz; öte yandan aynı tabanlı üslü sayıları bölerken üsler çıkarılır:",
            "$$\\dfrac{a^3}{a^3}=a^{3-3}=a^0 \\text{ ve } \\dfrac{a^3}{a^3}=1$$",
            "İki sonucun aynı olması için $a^0=1$ tanımlanır. $0^0$ ise tanımsız kabul edilir; çünkü yukarıdaki bölmede $a=0$ alınırsa sıfıra bölme ortaya çıkar.",
            "Sıfırın negatif kuvveti de tanımsızdır: $0^{-1}$, $\\dfrac{1}{0}$ anlamına gelirdi ve sıfıra bölme tanımlı değildir. Negatif üs kuralındaki $a \\neq 0$ koşulu bu yüzden vardır.",
            "<h3>Negatif üs</h3>",
            "Negatif üs, sayının tersinin kuvveti demektir: $a \\neq 0$ için",
            "$$a^{-n}=\\dfrac{1}{a^n}$$",
            "Bu tanım da bölmeden gelir: $\\dfrac{a^0}{a^n}=a^{0-n}=a^{-n}$ ve aynı zamanda $\\dfrac{a^0}{a^n}=\\dfrac{1}{a^n}$ dir. Kesirli bir tabanın negatif kuvvetinde kesir ters çevrilir, üs pozitif olur.",
            ornek(
                "$2^{-3}$ ve $\\left(\\dfrac{2}{3}\\right)^{-2}$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$2^{-3}=\\dfrac{1}{2^3}=\\dfrac{1}{8}$.",
                "$\\left(\\dfrac{2}{3}\\right)^{-2}=\\left(\\dfrac{3}{2}\\right)^2=\\dfrac{9}{4}$."),
            dikkat(
                "Negatif üs sonucu negatif yapmaz.",
                "$2^{-3}=\\dfrac{1}{8}$ dir, $-8$ değildir. Negatif üs yalnızca sayının tersini alır; işaret tabana bağlıdır."),
        ]},
        {"baslik": "Negatif tabanlı üslü sayılar", "icerik": [
            "Kuvvet tekrarlı çarpma olduğu için negatif tabanda işaret, negatif çarpanların sayısına bağlıdır. Negatif bir sayının <strong>çift</strong> kuvveti pozitif, <strong>tek</strong> kuvveti negatiftir.",
            ornek(
                "$(-3)^3$, $(-3)^4$ ve $-3^4$ ifadeleri verilsin.",
                "Değerlerini bulalım.",
                "$(-3)^3=(-3) \\cdot (-3) \\cdot (-3)=-27$: üç negatif çarpan, sonuç negatif.",
                "$(-3)^4=81$: dört negatif çarpan, sonuç pozitif.",
                "$-3^4=-81$: parantez olmadığı için kuvvet yalnızca $3$ e uygulanır, eksi sonra gelir."),
            "Negatif taban negatif üsle birleştiğinde iki kural ayrı ayrı uygulanır: negatif üs sayıyı ters çevirir, tabanın işareti ise üssün tek ya da çift olmasına göre kalır ya da gider. Örneğin $(-2)^{-2}=\\dfrac{1}{(-2)^2}=\\dfrac{1}{4}$ ve $(-2)^{-3}=\\dfrac{1}{(-2)^3}=-\\dfrac{1}{8}$ dir.",
            "Parantezin yeri sonucu değiştirir. Bu farkın ayrıntısı için <a href=\"/blog/pozitif-ve-negatif-sayilar/\">Pozitif ve Negatif Sayılar</a> yazısındaki kuvvetler bölümüne bakabilirsin.",
        ]},
        {"baslik": "Çarpma kuralları", "icerik": [
            "<strong>Tabanlar aynıysa</strong> çarpmada üsler toplanır. Çünkü $a^m$ de $m$ tane, $a^n$ de $n$ tane $a$ vardır ve çarpımda toplam $m+n$ tane $a$ olur:",
            "$$a^m \\cdot a^n=a^{m+n}$$",
            "<strong>Üsler aynıysa</strong> çarpmada tabanlar çarpılır, üs aynen kalır:",
            "$$a^n \\cdot b^n=(a \\cdot b)^n$$",
            ornek(
                "$2^3 \\cdot 2^4$ ve $2^5 \\cdot 5^5$ çarpımları verilsin.",
                "Sonuçları üslü biçimde bulalım.",
                "Tabanlar aynı: $2^3 \\cdot 2^4=2^{3+4}=2^7=128$.",
                "Üsler aynı: $2^5 \\cdot 5^5=(2 \\cdot 5)^5=10^5=100000$."),
            dikkat(
                "Taban da üs de farklıysa bu kurallar doğrudan uygulanmaz.",
                "$2^3 \\cdot 3^2$ için ne üsler toplanır ne tabanlar çarpılır; değer ayrı ayrı hesaplanır: $8 \\cdot 9=72$."),
            hap("Tabanlar aynıysa çarpmada üsler toplanır: $a^m \\cdot a^n=a^{m+n}$.", "Toplamada böyle bir kural yoktur: $2^3+2^4$ toplamı $2^7$ değildir."),
        ]},
        {"baslik": "Bölme kuralları", "icerik": [
            "Tabanlar aynıysa bölmede payın üssünden paydanın üssü çıkarılır; üsler aynıysa tabanlar bölünür. İkisi de $a \\neq 0$ ve $b \\neq 0$ koşuluyla geçerlidir:",
            "$$\\dfrac{a^m}{a^n}=a^{m-n} \\text{ ve } \\dfrac{a^n}{b^n}=\\left(\\dfrac{a}{b}\\right)^n$$",
            ornek(
                "$\\dfrac{3^7}{3^5}$ ve $\\dfrac{6^4}{3^4}$ bölümleri verilsin.",
                "Değerlerini bulalım.",
                "$\\dfrac{3^7}{3^5}=3^{7-5}=3^2=9$.",
                "$\\dfrac{6^4}{3^4}=\\left(\\dfrac{6}{3}\\right)^4=2^4=16$."),
            ornek(
                "$\\dfrac{2^3}{2^8}$ bölümü verilsin.",
                "Sonucu üslü ve kesirli biçimde yazalım.",
                "Üsleri çıkaralım: $2^{3-8}=2^{-5}$.",
                "Negatif üs kuralıyla: $2^{-5}=\\dfrac{1}{32}$."),
        ]},
        {"baslik": "Üssün üssü", "icerik": [
            "Bir üslü sayının kuvveti alınırken üsler çarpılır. $(a^m)^n$, $a^m$ nin $n$ kez çarpımıdır ve her birinde $m$ tane $a$ olduğu için toplam $m \\cdot n$ tane $a$ vardır:",
            "$$(a^m)^n=a^{m \\cdot n}$$",
            dikkat(
                "$(2^3)^2$ ile $2^{3^2}$ aynı şey değildir.",
                "$(2^3)^2=2^6=64$ tür: önce parantezin içi, sonra kuvvet.",
                "$2^{3^2}=2^9=512$ dir: burada önce üsteki $3^2=9$ hesaplanır."),
            ornek(
                "$4^5$ sayısı verilsin.",
                "Bu sayıyı $2$ tabanında yazalım.",
                "$4=2^2$ olduğu için $4^5=(2^2)^5$.",
                "Üsleri çarpalım: $(2^2)^5=2^{10}=1024$."),
            hap("Tabanlar aynıysa çarpmada üsler toplanır, bölmede çıkarılır; kuvvetin kuvvetinde üsler çarpılır.",
                "Üsler aynıysa çarpmada ve bölmede tabanlar işleme girer, üs aynen kalır."),
        ]},
        {"baslik": "Harfli üslü ifadeleri sadeleştirme", "icerik": [
            "Kurallar harfli ifadelerde de aynen geçerlidir. Sadeleştirirken her tabanı ayrı ele almak, önce parantezin kuvvetini dağıtmak ve en sonda negatif üsleri kesre çevirmek işi düzenli tutar.",
            ornek(
                "$a$ ve $b$ sıfırdan farklı olmak üzere $\\dfrac{(a^3 \\cdot b^{-2})^2}{a^4 \\cdot b^{-3}}$ ifadesi verilsin.",
                "İfadeyi sadeleştirelim.",
                "Parantezin kuvvetini dağıtalım: $(a^3 \\cdot b^{-2})^2=a^6 \\cdot b^{-4}$.",
                "Her tabanı ayrı bölelim: $a^{6-4}=a^2$ ve $b^{-4-(-3)}=b^{-1}$.",
                "Sonuç: $a^2 \\cdot b^{-1}=\\dfrac{a^2}{b}$."),
            dikkat(
                "Negatif üs çıkarılırken işaret karışıklığına dikkat et.",
                "$b^{-4}$ ün $b^{-3}$ e bölümünde üsler $-4-(-3)=-1$ olur, $-7$ değil."),
        ]},
        {"baslik": "Toplama, çıkarma ve ortak paranteze alma", "icerik": [
            "Üslü sayılarda toplama ve çıkarma için çarpmadaki gibi bir üs kuralı yoktur. Yalnızca <strong>aynı</strong> üslü terimler, benzer terimler gibi toplanır: $3 \\cdot 2^5+2^5=4 \\cdot 2^5$.",
            dikkat(
                "$2^3+2^4=2^7$ yazmak yanlıştır.",
                "$2^3+2^4=8+16=24$ tür, $2^7=128$ ise çok daha büyüktür. Üsler yalnızca çarpmada toplanır."),
            "Farklı üslü terimler toplanırken en güçlü araç <strong>ortak paranteze almaktır</strong>. Küçük üslü terim dışarı alınır, geriye kalanlar parantez içinde hesaplanır.",
            ornek(
                "$2^{10}+2^{11}$ toplamı verilsin.",
                "Toplamı tek bir çarpım olarak yazalım.",
                "$2^{11}=2^{10} \\cdot 2$ olduğu için $2^{10}$ ortak çarpandır.",
                "$2^{10}+2^{11}=2^{10} \\cdot (1+2)=3 \\cdot 2^{10}$."),
            ornek(
                "$\\dfrac{3^5+3^6}{3^4}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Payda $3^5$ ortak paranteze alınır: $3^5+3^6=3^5 \\cdot (1+3)=4 \\cdot 3^5$.",
                "Bölelim: $\\dfrac{4 \\cdot 3^5}{3^4}=4 \\cdot 3=12$."),
            ornek(
                "$\\dfrac{5^{12}-5^{10}}{5^{10}+5^{10}}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Pay: $5^{10} \\cdot (5^2-1)=24 \\cdot 5^{10}$.",
                "Payda: $2 \\cdot 5^{10}$.",
                "Sonuç: $\\dfrac{24}{2}=12$."),
        ]},
        {"baslik": "Üslü denklemler", "icerik": [
            "Bilinmeyen üsteyse iki tarafın tabanı eşitlenir. Tabanlar eşit, pozitif ve $1$ den farklıysa üsler de eşit olmalıdır. Bu koşul önemlidir: $1^2=1^5$ olduğu hâlde $2 \\neq 5$ tir; tabanı $1$ olan kuvvetlerden üslerin eşitliği çıkarılamaz.",
            ornek(
                "$2^{x+1}=32$ denklemi verilsin.",
                "$x$ i bulalım.",
                "$32=2^5$ olduğu için $2^{x+1}=2^5$.",
                "Üsler eşit: $x+1=5$, yani $x=4$."),
            ornek(
                "$9^x=27$ denklemi verilsin.",
                "$x$ i bulalım.",
                "İki tarafı $3$ tabanında yazalım: $9^x=3^{2x}$ ve $27=3^3$.",
                "$2x=3$, yani $x=\\dfrac{3}{2}$."),
            ornek(
                "$4^{x-1}=8^x$ denklemi verilsin.",
                "$x$ i bulalım.",
                "İki tarafı $2$ tabanında yazalım: $2^{2x-2}=2^{3x}$.",
                "$2x-2=3x$, yani $x=-2$.",
                "Kontrol: $4^{-3}=\\dfrac{1}{64}$ ve $8^{-2}=\\dfrac{1}{64}$."),
            ornek(
                "$2^x+2^{x+1}+2^{x+2}=56$ denklemi verilsin.",
                "$x$ i bulalım.",
                "Üç terimde de $2^x$ ortak çarpandır: $2^x \\cdot (1+2+4)=56$.",
                "$7 \\cdot 2^x=56$, yani $2^x=8=2^3$.",
                "$x=3$. Kontrol: $8+16+32=56$."),
            "<h3>Üsler eşitse</h3>",
            "Bilinmeyen tabandaysa ve üsler eşitse üssün tek ya da çift olmasına bakılır. Tek kuvvette işaret korunur, bu yüzden tek çözüm vardır. Çift kuvvette ise pozitif ve negatif iki sayı aynı sonucu verir.",
            ornek(
                "$x^3=-8$ ve $x^4=81$ denklemleri verilsin.",
                "Gerçek sayılardaki çözümleri bulalım.",
                "$x^3=-8$: üs tek; $(-2)^3=-8$ olduğu için tek çözüm $x=-2$.",
                "$x^4=81$: üs çift; $3^4=81$ ve $(-3)^4=81$ olduğu için $x=3$ ya da $x=-3$."),
        ]},
        {"baslik": "Günlük hayatta üslü sayılar", "icerik": [
            "Her adımda iki katına çıkan bir büyüklük, üslü sayılarla anlatılır. Bu tür büyümeye <strong>katlanarak büyüme</strong> denir ve ilk adımlarda yavaş görünse de kısa sürede çok büyük değerlere ulaşır.",
            ornek(
                "Bir bakteri her $20$ dakikada bir ikiye bölünsün ve başlangıçta tek bir bakteri olsun.",
                "$3$ saat sonra kaç bakteri olur?",
                "$3$ saat $180$ dakikadır; bu sürede $180:20=9$ bölünme olur.",
                "Her bölünmede sayı iki katına çıkar: $2^9$.",
                "$3$ saat sonra $2^9=512$ bakteri olur."),
            ornek(
                "Kalınlığı $0.1$ milimetre olan bir kâğıt her katlamada ikiye katlansın.",
                "$10$ kez katlanınca kalınlık kaç milimetre olur?",
                "Her katlamada kalınlık iki katına çıkar; $10$ katlamada $2^{10}=1024$ katına çıkar.",
                "Kalınlık: $0.1 \\cdot 1024=102.4$ milimetre, yani yaklaşık $10$ santimetre."),
        ]},
        {"baslik": "Bilimsel gösterim", "icerik": [
            "Çok büyük ve çok küçük sayılar, $1$ ile $10$ arasında bir sayı ile $10$ un bir kuvvetinin çarpımı olarak yazılır. Bu yazıma <strong>bilimsel gösterim</strong> denir: $1 \\leq a<10$ olmak üzere $a \\cdot 10^n$.",
            ornek(
                "$3400000$ ve $0.00052$ sayıları verilsin.",
                "Bilimsel gösterimle yazalım.",
                "Tam sayılarda virgül sayının sonunda kabul edilir. $3400000$ de virgülü $6$ basamak sola kaydırırsak $3.4$ elde ederiz: $3.4 \\cdot 10^6$.",
                "$0.00052$ de virgülü $4$ basamak sağa kaydırırsak $5.2$ elde ederiz: $5.2 \\cdot 10^{-4}$."),
            ornek(
                "$(3 \\cdot 10^4) \\cdot (5 \\cdot 10^{-7})$ çarpımı verilsin.",
                "Sonucu bilimsel gösterimle yazalım.",
                "Sayıları ve $10$ un kuvvetlerini ayrı çarpalım: $15 \\cdot 10^{-3}$.",
                "$15$, $1$ ile $10$ arasında olmadığı için $15=1.5 \\cdot 10$ yazalım.",
                "Sonuç: $1.5 \\cdot 10^{-2}$."),
            "Virgül sola kaydırıldıkça üs artar, sağa kaydırıldıkça azalır. Sayı $1$ den küçükse üs negatif olur.",
            hap("Işığın bir saniyede aldığı yol yaklaşık $300000000$ metre, yani $3 \\cdot 10^8$ metredir.", "Bilimsel gösterim, sıfırları saymadan büyüklüğü tek bakışta gösterir.", gunluk=True),
        ]},
        {"baslik": "Üslü sayıları sıralama", "icerik": [
            "Tabanlar eşit ve $1$ den büyükse üssü büyük olan sayı büyüktür: $2^5<2^7$. Taban $0$ ile $1$ arasındaysa durum tersine döner; kuvvet arttıkça sayı küçülür: $\\left(\\dfrac{1}{2}\\right)^3=\\dfrac{1}{8}$ ve $\\left(\\dfrac{1}{2}\\right)^2=\\dfrac{1}{4}$ olduğu için $\\left(\\dfrac{1}{2}\\right)^3<\\left(\\dfrac{1}{2}\\right)^2$ dir.",
            "Tabanlar eşitlenemiyorsa üsler eşitlenmeye çalışılır. Üsler eşit ve tabanlar pozitifse tabanı büyük olan sayı büyüktür.",
            ornek(
                "$2^{40}$, $3^{30}$ ve $5^{20}$ sayıları verilsin.",
                "Küçükten büyüğe sıralayalım.",
                "Üslerin ortak böleni $10$: $2^{40}=16^{10}$, $3^{30}=27^{10}$, $5^{20}=25^{10}$.",
                "Üsler eşit; tabanları karşılaştıralım: $16<25<27$.",
                "Sıralama: $2^{40}<5^{20}<3^{30}$."),
        ]},
        {"baslik": "Bir çarpımın basamak sayısı", "icerik": [
            "$2$ ile $5$ in çarpımı $10$ olduğu için, içinde $2$ ve $5$ in kuvvetleri bulunan bir sayıda bunları $10$ un kuvveti olarak eşleştirmek basamak sayısını hesapsız verir.",
            ornek(
                "$2^{10} \\cdot 5^{12}$ sayısı verilsin.",
                "Bu sayının kaç basamaklı olduğunu bulalım.",
                "$10$ tane $2$ yi $10$ tane $5$ ile eşleştirelim: $2^{10} \\cdot 5^{10}=10^{10}$.",
                "Geriye $5^2=25$ kalır: sayı $25 \\cdot 10^{10}$ dur.",
                "$25$ in sonuna $10$ sıfır eklenir; sayı $2+10=12$ basamaklıdır."),
        ]},
        {"baslik": "Son basamak soruları", "icerik": [
            "Bir sayının büyük bir kuvvetinin son basamağı sorulduğunda kuvvetin tamamını hesaplamak gerekmez. Son basamaklar belirli bir düzenle tekrar eder ve bu tekrarın uzunluğu bulunur.",
            ornek(
                "$7^{2026}$ sayısı verilsin.",
                "Birler basamağını bulalım.",
                "Kuvvetlerin son basamakları: $7^1$ için $7$, $7^2=49$ için $9$, $7^3=343$ için $3$, $7^4=2401$ için $1$. Sonra düzen başa döner.",
                "Düzen $4$ adımda tekrar ediyor. $2026$ nın $4$ e bölümünden kalan $2$.",
                "Kalan $2$ olduğu için son basamak, düzendeki ikinci basamakla aynıdır: $9$."),
            ornek(
                "$2^{100}$ sayısı verilsin.",
                "Birler basamağını bulalım.",
                "Son basamaklar: $2, 4, 8, 6$ ve sonra yine $2$. Düzen $4$ adımda tekrar ediyor.",
                "$100$ ün $4$ e bölümünden kalan $0$; kalan $0$, düzenin son elemanına karşılık gelir.",
                "Son basamak $6$ dır."),
            hap("Son basamak sorularında önce tekrar düzeninin uzunluğunu bul, sonra üssün bu uzunluğa bölümünden kalana bak.",
                "Kalan $0$ ise düzenin son elemanını al."),
            dikkat(
                "Kalan $0$ çıktığında düzenin ilk elemanını değil, son elemanını al.",
                "$2^4=16$ nın son basamağı $6$ dır ve $4$ ün $4$ e bölümünden kalan $0$ dır; kalan $0$ düzenin dördüncü, yani son elemanıdır."),
        ]},
        {"baslik": "Sınavda üslü sayılar", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu üslü ifadeleri sadeleştirme, ortak paranteze alma, tabanları eşitleyerek denklem çözme, sıralama ve son basamak biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde üslü sayı bilgisi sayısal akıl yürütme sorularının içinde, işlemi kısaltmak için de gerekebilir."),
            "Üslü sayı sorularında işe yarayan bir alışkanlık, bütün sayıları mümkün olan en küçük asal tabanlara ayırmaktır: $4$, $8$, $16$ yerine $2$ nin kuvvetleri; $9$, $27$, $81$ yerine $3$ ün kuvvetleri. Tabanlar ortaklaşınca çarpma, bölme ve denklem kuralları doğrudan uygulanır.",
            "Üslü sayıların sıralanması için <a href=\"/blog/sayi-dogrusu-ve-sayilari-siralama/\">Sayı Doğrusu ve Sayıları Sıralama</a> yazısındaki üslü sayılar bölümüne bakabilirsin. Kesirli üsler ve kök ile ilişkisi ise <a href=\"/blog/koklu-sayilar-konu-anlatimi-pdf/\">Köklü Sayılar Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$2^5=10$ yazmak", "$2^5=32$"],
                ["$2^{-3}=-8$ yazmak", "$2^{-3}=\\dfrac{1}{8}$"],
                ["$-3^4=81$ yazmak", "$-3^4=-81$"],
                ["$2^3+2^4=2^7$ yazmak", "$2^3+2^4=24$"],
                ["$(2^3)^2=2^9$ yazmak", "$(2^3)^2=2^6$"],
                ["$0^0=1$ sanmak", "$0^0$ tanımsızdır"],
            ]),
            "Bu hataların çoğu, çarpmadaki kuralları toplamaya ya da kuvvetin kuvvetine taşımaktan doğar. Şüphede kaldığında üslü ifadeyi açık çarpım olarak yazıp saymak doğru kuralı hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Bir sayının sıfırıncı kuvveti neden 1 dir?",
         "Aynı tabanlı üslü sayılar bölünürken üsler çıkarılır. Bir sayıyı kendisine bölmek hem 1 i hem de sıfırıncı kuvveti verdiği için sıfırdan farklı her sayının sıfırıncı kuvveti 1 olarak tanımlanır."),
        ("Sıfırın sıfırıncı kuvveti kaçtır?",
         "Tanımsız kabul edilir. Sıfırıncı kuvveti veren bölme işleminde taban sıfır alınırsa sıfıra bölme ortaya çıkar."),
        ("Negatif üs ne demektir?",
         "Sayının tersinin kuvveti demektir. Örneğin 2 nin eksi üçüncü kuvveti, 1 bölü 8 dir."),
        ("Negatif sayının çift kuvveti neden pozitiftir?",
         "Kuvvet tekrarlı çarpmadır ve her iki negatif çarpan birlikte pozitif bir sonuç verir. Çift kuvvette negatif çarpanlar ikişer ikişer eşleştiği için sonuç pozitif olur."),
        ("Üslü sayılarda toplama nasıl yapılır?",
         "Üsler toplanmaz. Aynı üslü terimler benzer terim gibi toplanır; farklı üslü terimlerde küçük üslü terim ortak paranteze alınır."),
        ("Üslü denklem nasıl çözülür?",
         "İki tarafın tabanı eşitlenir. Tabanlar eşit, pozitif ve 1 den farklıysa üsler eşitlenerek denklem çözülür."),
        ("Bilimsel gösterim nedir?",
         "Bir sayının 1 ile 10 arasında bir sayı ile 10 un bir kuvvetinin çarpımı olarak yazılmasıdır. Çok büyük ve çok küçük sayıları kısa yazmak için kullanılır."),
    ],
    "kontrol": [
        "Üslü sayıda tabanı ve üssü ayırt edebiliyorum.",
        "Sıfırıncı kuvvetin neden $1$ olduğunu bölme kuralıyla açıklayabiliyorum.",
        "Negatif üslü bir sayıyı kesir olarak yazabiliyorum.",
        "Negatif tabanlı kuvvetlerde işareti doğru belirleyebiliyorum.",
        "Çarpma ve bölme kurallarını tabanlar ya da üsler aynıyken uygulayabiliyorum.",
        "$(a^m)^n$ ile $a^{m^n}$ arasındaki farkı açıklayabiliyorum.",
        "Farklı üslü terimleri ortak paranteze alarak sadeleştirebiliyorum.",
        "Tabanları eşitleyerek üslü denklem çözebiliyorum.",
        "Bir sayıyı bilimsel gösterimle yazabiliyorum.",
        "Büyük bir kuvvetin son basamağını tekrar düzeniyle bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["koklu-sayilar-konu-anlatimi-pdf", "islem-onceligi-nasil-yapilir", "pozitif-ve-negatif-sayilar"],
}
