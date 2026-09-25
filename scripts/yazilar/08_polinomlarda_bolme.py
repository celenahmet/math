# scripts/yazilar/08_polinomlarda_bolme.py — Polinomlarda Bolme (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "polinomlarda-bolme",
    "baslik": "Polinomlarda Bölme İşlemi",
    "aciklama": "Polinom bölmesi nasıl yapılır? Bölünen, bölen, bölüm ve kalan, uzun bölme adımları, eksik terimler, derece kuralları, Horner yöntemi ve kalansız bölme; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "polinomlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "polinomlarda-bolme",
    "kapak_alt": "Polinomlarda bölme: renkli terim bloklarını ahşap bir düzenekte adım adım bölüm ve kalan bölmelerine yerleştiren iki öğrenci",
    "ozet": "Polinomlar da sayılar gibi bölünür ve bölmenin sonunda bir bölüm ile bir kalan bulunur. Bölme işlemi, bir polinomun başka bir polinomla tam bölünüp bölünmediğini, kalanın ne olduğunu ve polinomun hangi çarpanlara ayrılabileceğini gösterir. Bu yazıda bölme eşitliğini, uzun bölmenin adımlarını, eksik terimlerle bölmeyi, ikinci dereceden bir bölenle bölmeyi, bölüm ve kalanın derecesini, Horner yöntemini, sonucu kontrol etmeyi ve kalansız bölmeyi çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Polinom bölmesi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için polinomların derecesini, çarpmasını ve sayılarda bölmeyi biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/polinomlar-konu-anlatimi/\">Polinomlar Konu Anlatımı</a> yazısına göz at."),
            "$P(x)$ polinomu, sıfırdan farklı bir $B(x)$ polinomuna bölündüğünde öyle bir $Q(x)$ bölümü ve $K(x)$ kalanı bulunur ki aşağıdaki eşitlik her $x$ için sağlanır ve kalanın derecesi bölenin derecesinden küçüktür:",
            "$$P(x)=B(x) \\cdot Q(x)+K(x)$$",
            "Bu eşitliğe <strong>bölme eşitliği</strong> denir. Sayılardaki bölme de aynı yapıdadır: $17=5 \\cdot 3+2$ eşitliğinde kalan $2$, bölen $5$ ten küçüktür. Polinomlarda ise karşılaştırılan şey sayının büyüklüğü değil, derecedir.",
            hap("$P(x)=B(x) \\cdot Q(x)+K(x)$",
                "Kalanın derecesi bölenin derecesinden küçüktür."),
        ]},
        {"baslik": "Bölmenin terimleri", "icerik": [
            "Bölme eşitliğindeki dört polinomun her birinin bir adı vardır. Soru metinlerinde bu adlar sık kullanıldığı için hangisinin hangisi olduğunu karıştırmamak gerekir.",
            tablo(["Terim", "Gösterim", "Anlamı"], [
                ["Bölünen", "$P(x)$", "Bölünen polinom"],
                ["Bölen", "$B(x)$", "Bölen polinom"],
                ["Bölüm", "$Q(x)$", "Bölmenin sonucu"],
                ["Kalan", "$K(x)$", "Artan kısım"],
            ]),
            "Kapaktaki düzenek de bu ayrımı gösterir: bloklar adım adım bölüm bölmesine yerleştirilir, sonunda yerleştirilemeyen parça kalan bölmesinde toplanır.",
        ]},
        {"baslik": "Uzun bölmenin adımları", "icerik": [
            "Polinomlarda uzun bölme, sayılardaki uzun bölmeyle aynı mantıkla ilerler. Her adımda bölünenin en büyük dereceli terimi yok edilir.",
            tablo(["Adım", "Yapılacak iş"], [
                ["1", "Bölünen ve bölen azalan kuvvetlere göre sıralanır"],
                ["2", "Bölünenin ilk terimi bölenin ilk terimine bölünür"],
                ["3", "Bulunan terim bölümün bir terimi olur, bölenle çarpılır"],
                ["4", "Çarpım bölünenden çıkarılır"],
                ["5", "Kalanın derecesi bölenden küçük olana kadar tekrarlanır"],
            ]),
            "Çıkarma adımı en çok hata yapılan yerdir: çarpımın bütün terimlerinin işareti değiştirilerek toplanır. Bir terimin işaretini değiştirmeyi unutmak, sonraki bütün adımları bozar.",
        ]},
        {"baslik": "İlk örnek: kalansız bölme", "icerik": [
            ornek(
                "$P(x)=x^2+5x+6$ polinomu $B(x)=x+2$ polinomuna bölünsün.",
                "Bölümü ve kalanı bulalım.",
                "İlk terimler: $x^2:x=x$. Bölüme $x$ yazılır; $x \\cdot (x+2)=x^2+2x$ çıkarılır ve $3x+6$ kalır.",
                "Yeni ilk terim: $3x:x=3$. Bölüme $3$ eklenir; $3 \\cdot (x+2)=3x+6$ çıkarılır ve $0$ kalır.",
                "Bölüm $Q(x)=x+3$, kalan $0$ dır."),
            "Kalan sıfır olduğu için $x+2$, $P(x)$ polinomunun bir çarpanıdır: $x^2+5x+6=(x+2)(x+3)$. Sonucu sayılarla da denetlemek mümkündür: $x=10$ için bölünen $156$, bölen $12$ ve bölüm $13$ olur; gerçekten $156:12=13$ tür.",
        ]},
        {"baslik": "İkinci örnek: kalanlı bölme", "icerik": [
            ornek(
                "$P(x)=2x^3-3x^2+4x-5$ polinomu $B(x)=x-1$ polinomuna bölünsün.",
                "Bölümü ve kalanı bulalım.",
                "$2x^3:x=2x^2$; $2x^2(x-1)=2x^3-2x^2$ çıkarılınca $-x^2+4x-5$ kalır.",
                "$-x^2:x=-x$; $-x(x-1)=-x^2+x$ çıkarılınca $3x-5$ kalır.",
                "$3x:x=3$; $3(x-1)=3x-3$ çıkarılınca $-2$ kalır. Bölüm $2x^2-x+3$, kalan $-2$ dir."),
            "Kalan negatif olabilir; önemli olan yalnızca derecesinin bölenden küçük olmasıdır. Kontrol: $(x-1)(2x^2-x+3)=2x^3-3x^2+4x-3$ ve buna $-2$ eklenince bölünen elde edilir.",
        ]},
        {"baslik": "Eksik terimler", "icerik": [
            "Bölünende bazı kuvvetler eksikse, uzun bölmeye başlamadan önce bu kuvvetler sıfır katsayıyla yazılır. Böylece her adımda aynı dereceli terimler alt alta gelir ve çıkarma hatası yapılmaz.",
            ornek(
                "$P(x)=x^3-8$ polinomu $x-2$ ye bölünsün.",
                "Bölümü ve kalanı bulalım.",
                "Bölünen $x^3+0x^2+0x-8$ olarak yazılır.",
                "$x^3:x=x^2$; çıkarınca $2x^2+0x-8$. $2x^2:x=2x$; çıkarınca $4x-8$. $4x:x=4$; çıkarınca $0$.",
                "Bölüm $x^2+2x+4$, kalan $0$ dır."),
            "Bu sonuç, küp farkı özdeşliğinin bir örneğidir: $x^3-8=(x-2)(x^2+2x+4)$. Özdeşliği bilen öğrenci bölmeyi hiç yapmadan sonucu yazabilir; bilmeyen için de sıfır katsayılı uzun bölme aynı sonuca güvenle ulaştırır.",
        ]},
        {"baslik": "İkinci dereceden bölen", "icerik": [
            "Bölen ikinci dereceden olduğunda da adımlar aynıdır; yalnızca kalan birinci dereceden bir polinom olabilir, çünkü derecesi $2$ den küçük olmalıdır.",
            ornek(
                "$P(x)=x^4+x^3-x+2$ polinomu $B(x)=x^2+1$ polinomuna bölünsün.",
                "Bölümü ve kalanı bulalım.",
                "Bölünen $x^4+x^3+0x^2-x+2$ olarak yazılır. $x^4:x^2=x^2$; $x^2(x^2+1)$ çıkarılınca $x^3-x^2-x+2$ kalır.",
                "$x^3:x^2=x$; $x(x^2+1)$ çıkarılınca $-x^2-2x+2$ kalır.",
                "$-x^2:x^2=-1$; $-(x^2+1)$ çıkarılınca $-2x+3$ kalır. Bölüm $x^2+x-1$, kalan $-2x+3$ tür."),
            "Kalan $-2x+3$ birinci derecedendir ve bölen ikinci dereceden olduğu için bölme burada durur. Kalanın derecesi bölenin derecesinden küçük olduğu sürece bölmeye devam edilmez.",
        ]},
        {"baslik": "Dereceler eşit olduğunda", "icerik": [
            "Bölünen ile bölenin dereceleri eşitse bölüm bir sabittir, çünkü derecesi $0$ dır. Bu sabit, baş katsayıların oranıdır; kalan ise bölünenden bölenin bu sabit katı çıkarılarak bulunur.",
            ornek(
                "$P(x)=6x^2+x-2$ polinomu $B(x)=3x^2+1$ polinomuna bölünsün.",
                "Bölümü ve kalanı bulalım.",
                "Bölüm: $6x^2:3x^2=2$.",
                "Kalan: $6x^2+x-2-2(3x^2+1)=x-4$. Kalanın derecesi $1$, bölenin derecesi $2$ olduğu için bölme biter."),
        ]},
        {"baslik": "Bölüm ve kalanın derecesi", "icerik": [
            "Bölme yapılmadan da bölüm ve kalanın derecesi hakkında bilgi edinilebilir. Bölme eşitliğinde derece kuralları uygulanınca şu sonuçlar çıkar:",
            tablo(["Büyüklük", "Derece"], [
                ["Bölüm $Q(x)$", "$\\text{der}[P]-\\text{der}[B]$"],
                ["Kalan $K(x)$", "$\\text{der}[B]$ den küçük"],
            ]),
            ornek(
                "Derecesi $5$ olan bir polinom, derecesi $2$ olan bir polinoma bölünsün.",
                "Bölümün derecesini ve kalanın derecesi için en büyük değeri bulalım.",
                "Bölümün derecesi: $5-2=3$.",
                "Kalanın derecesi en fazla $1$ dir; kalan bir sabit ya da sıfır da olabilir."),
            dikkat(
                "Kalanın derecesinin tam olarak bölenin bir eksiği olduğunu sanmak.",
                "Kalanın derecesi bölenin derecesinden küçüktür ama daha da küçük olabilir. İkinci dereceden bir bölenle bölmede kalan birinci dereceden, sabit ya da sıfır olabilir."),
            hap("Bölümün derecesi, bölünenin derecesinden bölenin derecesi çıkarılarak bulunur.", "Kalanın derecesi bölenin derecesinden küçüktür."),
        ]},
        {"baslik": "Birinci dereceden bölenle kalan", "icerik": [
            "Bölen birinci dereceden olduğunda kalanın derecesi $0$ dan küçük olmalıdır; bu yüzden kalan her zaman bir sabittir. Bu gözlem, kalanı bölme yapmadan bulmayı sağlayan kalan teoreminin temelidir.",
            "Bölme eşitliği $P(x)=(x-a) \\cdot Q(x)+k$ biçiminde yazılır ve $x$ yerine $a$ konunca $(x-a)$ çarpanı sıfır olur: $P(a)=k$. Yani $P(x)$ polinomunun $x-a$ ile bölümünden kalan $P(a)$ dır. Ayrıntısı <a href=\"/blog/polinomlarda-kalan/\">Polinomlarda Kalan Bulma</a> yazısında.",
            ornek(
                "$P(x)=2x^3-3x^2+4x-5$ polinomu verilsin.",
                "$x-1$ ile bölümünden kalanı bölme yapmadan bulalım.",
                "$P(1)=2-3+4-5=-2$.",
                "Uzun bölmede bulunan kalanla aynıdır."),
            hap("$P(x)$ polinomunun $x-a$ ile bölümünden kalan $P(a)$ olur."),
        ]},
        {"baslik": "Horner yöntemi", "icerik": [
            "Bölen $x-a$ biçimindeyse bölme, yalnızca katsayılarla çalışan kısa bir yöntemle yapılabilir. Bu yönteme <strong>Horner yöntemi</strong> ya da sentetik bölme denir. Katsayılar azalan kuvvet sırasıyla yazılır; ilk katsayı aşağı indirilir, her indirilen sayı $a$ ile çarpılıp bir sonraki katsayıya eklenir.",
            ornek(
                "$P(x)=2x^3-3x^2+4x-5$ polinomu $x-1$ ile bölünsün; burada $a=1$ dir.",
                "Horner yöntemiyle bölüm ve kalanı bulalım.",
                "Katsayılar: $2$, $-3$, $4$, $-5$. İlk katsayı $2$ aşağı iner.",
                "$2 \\cdot 1+(-3)=-1$; $-1 \\cdot 1+4=3$; $3 \\cdot 1+(-5)=-2$.",
                "Son sayı kalandır: $-2$. Önceki sayılar bölümün katsayılarıdır: $2x^2-x+3$."),
            tablo(["Katsayı", "$2$", "$-3$", "$4$", "$-5$"], [
                ["Eklenen", "", "$2$", "$-1$", "$3$"],
                ["Sonuç", "$2$", "$-1$", "$3$", "$-2$"],
            ]),
            "Horner yöntemi uzun bölmeyle aynı sonucu verir ama çok daha kısadır. Eksik terimler burada da sıfır katsayıyla yazılmalıdır; aksi hâlde katsayılar yanlış sütunlara kayar.",
            hap("Horner yönteminde $x-a$ ile bölerken $a$, $x+a$ ile bölerken $-a$ kullanılır.", "Bölünende eksik kuvvet varsa o sütuna $0$ yazılır."),
        ]},
        {"baslik": "Horner yönteminde eksik terimler", "icerik": [
            "Horner yönteminde her sütun bir kuvvete karşılık gelir. Bölünende eksik kuvvet varsa o sütuna $0$ yazılır; aksi hâlde bütün katsayılar bir sütun kayar ve sonuç yanlış çıkar.",
            ornek(
                "$P(x)=x^4-16$ polinomu $x-2$ ile bölünsün; burada $a=2$ dir.",
                "Bölümü ve kalanı bulalım.",
                "Katsayılar: $1$, $0$, $0$, $0$, $-16$.",
                "İşlemler: $1$; $1 \\cdot 2+0=2$; $2 \\cdot 2+0=4$; $4 \\cdot 2+0=8$; $8 \\cdot 2-16=0$.",
                "Bölüm $x^3+2x^2+4x+8$, kalan $0$ dır."),
        ]},
        {"baslik": "Horner yöntemiyle çarpan bulmak", "icerik": [
            "Horner yönteminin sonunda kalan sıfır çıkarsa bölen bir çarpandır ve polinom, bölen ile bölümün çarpımı olarak yazılır. Bölüm daha düşük dereceli olduğu için çarpanlara ayırma işlemi onun üzerinde sürdürülür.",
            ornek(
                "$P(x)=x^3-4x^2+x+6$ polinomu $x+1$ ile bölünsün; burada $a=-1$ dir.",
                "Bölümü, kalanı ve polinomun çarpanlarını bulalım.",
                "Katsayılar: $1$, $-4$, $1$, $6$. İşlemler: $1$; $1 \\cdot (-1)-4=-5$; $-5 \\cdot (-1)+1=6$; $6 \\cdot (-1)+6=0$.",
                "Kalan $0$, bölüm $x^2-5x+6$ dır. Bölüm de çarpanlarına ayrılır: $(x-2)(x-3)$.",
                "Sonuç: $P(x)=(x+1)(x-2)(x-3)$."),
        ]},
        {"baslik": "Bölen ax + b biçiminde olduğunda", "icerik": [
            "Bölenin baş katsayısı $1$ değilse uzun bölme aynen uygulanır; yalnızca her adımda bölümün terimi bulunurken baş katsayıya da bölünür. Kalan yine bir sabittir ve $ax+b=0$ yapan $x$ değeri yazılarak bulunur.",
            ornek(
                "$P(x)=6x^2+x-2$ polinomu $2x-1$ ile bölünsün.",
                "Bölümü ve kalanı bulalım.",
                "$6x^2:2x=3x$; $3x(2x-1)=6x^2-3x$ çıkarılınca $4x-2$ kalır.",
                "$4x:2x=2$; $2(2x-1)=4x-2$ çıkarılınca $0$ kalır. Bölüm $3x+2$, kalan $0$ dır.",
                "Kontrol: $2x-1=0$ için $x=\\dfrac{1}{2}$; $P(\\dfrac{1}{2})=\\dfrac{6}{4}+\\dfrac{1}{2}-2=0$."),
        ]},
        {"baslik": "Özdeşliklerle hızlı bölme", "icerik": [
            "Bölünen bilinen bir özdeşliğe uyuyorsa bölme yapmadan sonuç yazılabilir. İki kare farkı ve iki küp toplamı ile farkı en sık karşılaşılan özdeşliklerdir.",
            tablo(["Bölme", "Bölüm"], [
                ["$(x^2-9):(x-3)$", "$x+3$"],
                ["$(x^3-8):(x-2)$", "$x^2+2x+4$"],
                ["$(x^3+27):(x+3)$", "$x^2-3x+9$"],
            ]),
            "Bu tablodaki her bölmede kalan sıfırdır, çünkü bölen bölünenin bir çarpanıdır. Özdeşliği tanımak, uzun bölmenin birkaç satırını tek bir satıra indirir; tanınmadığında ise uzun bölme her zaman aynı sonuca götürür.",
        ]},
        {"baslik": "İkinci dereceden bölenle kalan bulmak", "icerik": [
            "Bölen ikinci dereceden ve kökleri kolay bulunuyorsa kalan, bölme yapılmadan da bulunabilir. Kalan $ax+b$ biçiminde yazılır ve bölenin kökleri bölme eşitliğine yerleştirilir; bölen sıfır olduğu için yalnızca kalan kalır.",
            ornek(
                "$P(x)=x^5+2x+3$ polinomu $x^2-x$ ile bölünsün.",
                "Kalanı bulalım.",
                "Kalan $ax+b$ olsun. Bölenin kökleri $0$ ve $1$ dir.",
                "$P(0)=b=3$ ve $P(1)=a+b=6$; buradan $a=3$.",
                "Kalan $3x+3$ tür."),
            dikkat(
                "İkinci dereceden bölenle bölmede kalanı bir sabit sanmak.",
                "Kalanın derecesi $2$ den küçük olmalıdır; yani kalan birinci dereceden olabilir. Kalanı yalnızca $b$ diye almak, $a$ yı yok saymak demektir ve bu örnekte yanlış olarak $3$ sonucunu verir."),
        ]},
        {"baslik": "Sonucu kontrol etmek", "icerik": [
            "Bölmenin doğru yapıldığını anlamanın en güvenli yolu bölme eşitliğini denetlemektir: bölen ile bölüm çarpılır, kalan eklenir ve sonuç bölünene eşit olmalıdır. Tam çarpım yapmak yerine $x$ yerine basit bir sayı yazmak da hataların çoğunu yakalar.",
            ornek(
                "$x^4+x^3-x+2$ polinomunun $x^2+1$ ile bölümünden bölüm $x^2+x-1$, kalan $-2x+3$ bulundu.",
                "Sonucu $x=2$ için kontrol edelim.",
                "Bölünen: $16+8-2+2=24$.",
                "Sağ taraf: $(4+1)(4+2-1)+(-4+3)=5 \\cdot 5-1=24$. İki taraf eşittir."),
            "Tek bir sayıyla yapılan kontrol hatanın olmadığını kesin olarak göstermez ama hatalı bir sonucun bu kontrolden geçmesi pek olası değildir. İki farklı sayıyla denemek güveni daha da artırır. Seçilen sayının bölenin kökü olmamasına dikkat edilmelidir; kökte bölen sıfır olur ve kontrol yalnızca kalanı sınar.",
        ]},
        {"baslik": "Bölüm ve kalandan bölüneni bulmak", "icerik": [
            "Bazı sorularda bölen, bölüm ve kalan verilir ve bölünen istenir. Bu durumda bölme eşitliği doğrudan uygulanır: bölen ile bölüm çarpılıp kalan eklenir.",
            ornek(
                "Bir $P(x)$ polinomunun $x^2-1$ ile bölümünden bölüm $x+2$, kalan $3x-1$ dir.",
                "$P(x)$ polinomunu ve $P(1)$ değerini bulalım.",
                "$P(x)=(x^2-1)(x+2)+3x-1=x^3+2x^2-x-2+3x-1=x^3+2x^2+2x-3$.",
                "$P(1)=1+2+2-3=2$. Aynı değer kalandan da bulunur: $x=1$ için $x^2-1=0$ olduğundan $P(1)=3 \\cdot 1-1=2$."),
        ]},
        {"baslik": "İki kalandan iki bilinmeyen", "icerik": [
            "Polinomda iki bilinmeyen katsayı varsa iki farklı bölmeden gelen kalan bilgisi gerekir. Her kalan bilgisi, kalan teoremiyle bir denkleme dönüşür ve iki denklem birlikte çözülür.",
            ornek(
                "$P(x)=x^3+ax+b$ polinomunun $x-1$ ile bölümünden kalan $4$, $x+1$ ile bölümünden kalan $2$ dir.",
                "$a$ ve $b$ yi bulalım.",
                "$P(1)=1+a+b=4$, yani $a+b=3$.",
                "$P(-1)=-1-a+b=2$, yani $b-a=3$. İki denklemden $b=3$ ve $a=0$ bulunur.",
                "Kontrol: $P(x)=x^3+3$ için $P(1)=4$ ve $P(-1)=2$."),
        ]},
        {"baslik": "Bölümün değerini bulmak", "icerik": [
            "Bölme eşitliği yalnızca bölüneni değil bölümü de bulmaya yarar. Bölen, kalan ve bölünenin bir değeri biliniyorsa bölümün o noktadaki değeri eşitlikten çekilir.",
            ornek(
                "$P(x)=(x+1) \\cdot Q(x)+4$ eşitliği veriliyor ve $P(1)=10$ dur.",
                "$Q(x)$ polinomunun katsayılar toplamını bulalım.",
                "Katsayılar toplamı $Q(1)$ dir. $x=1$ yazılır: $10=2 \\cdot Q(1)+4$.",
                "$Q(1)=3$."),
        ]},
        {"baslik": "Kalansız bölünme koşulu", "icerik": [
            "Bir polinom $x-a$ ile kalansız bölünüyorsa kalan sıfırdır, yani $P(a)=0$ dır. Bu koşul, polinomdaki bilinmeyen bir katsayıyı bulmak için kullanılır.",
            ornek(
                "$P(x)=x^3+mx+6$ polinomu $x-1$ ile kalansız bölünüyor.",
                "$m$ yi bulalım.",
                "Kalansız bölünme için $P(1)=0$ olmalıdır: $1+m+6=0$.",
                "$m=-7$. Kontrol: $x^3-7x+6=(x-1)(x^2+x-6)=(x-1)(x-2)(x+3)$."),
            "Kalansız bölünme, bölenin polinomun bir çarpanı olması demektir. Çarpanlara ayırmanın ayrıntısı <a href=\"/blog/polinomlarda-carpanlara-ayirma/\">Polinomlarda Çarpanlara Ayırma</a> yazısında.",
        ]},
        {"baslik": "Sayı bölmesiyle karşılaştırma", "icerik": [
            "Polinom bölmesi ile sayı bölmesi arasındaki benzerlik bir örnekle açıkça görülür. $x=10$ yazılınca polinomlar ondalık sayılara dönüşür ve uzun bölmenin her adımı, sayılardaki uzun bölmenin bir adımına karşılık gelir.",
            tablo(["Polinom", "$x=10$ için"], [
                ["Bölünen $x^2+5x+6$", "$156$"],
                ["Bölen $x+2$", "$12$"],
                ["Bölüm $x+3$", "$13$"],
                ["Kalan $0$", "$0$"],
            ]),
            "Fark, polinomlarda eldenin olmamasıdır. Sayılarda bir basamaktaki değer $9$ u aşınca bir üst basamağa geçer; polinomlarda katsayılar her büyüklükte olabildiği için böyle bir aktarma yapılmaz.",
            hap("$156$ lirayı $12$ kişiye paylaştırmak, $x=10$ için $x^2+5x+6$ polinomunu $x+2$ ye bölmek gibidir.", "Bölüm $x+3$ olduğu için kişi başına $13$ lira düşer ve artan para kalmaz.", gunluk=True),
        ]},
        {"baslik": "Sınavda polinom bölmesi", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) polinom bölmesi bölüm ve kalanın bulunması, bölme eşitliği ve kalansız bölünme koşulu biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) ikinci dereceden bölenle bölme, bölüm ve kalanın derecesi ve bölmeyle çarpanlara ayırma da sorulabilir."),
            "Bölme sorularında önce ne istendiğine bak. Yalnızca kalan isteniyorsa bölme yapmaya gerek yoktur; kalan teoremi yeterlidir. Bölüm isteniyorsa ve bölen $x-a$ biçimindeyse Horner yöntemi, diğer durumlarda uzun bölme en güvenli yoldur.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Eksik terimleri yazmamak", "Eksik kuvvetler $0$ katsayıyla yazılır"],
                ["Çıkarmada işaretleri değiştirmemek", "Çarpımın bütün işaretleri değişir"],
                ["Kalan bölenden küçük olmadan durmak", "Kalanın derecesi bölenden küçük olmalı"],
                ["Horner yönteminde $x+1$ için $a=1$ almak", "$x+1$ için $a=-1$"],
                ["Kalanı negatif olamaz sanmak", "Kalan negatif olabilir"],
                ["Bölüm derecesini derecelerin toplamı sanmak", "Derecelerin farkıdır"],
            ]),
            "Bu hataların çoğu, sıralama ve işaret disiplininin gevşemesinden doğar. Bölünen ve bölen her zaman azalan kuvvetlere göre sıralanmalı, eksik terimler yazılmalı ve her çıkarma işareti değiştirilerek toplama olarak yapılmalıdır.",
        ]},
    ],
    "sss": [
        ("Polinom bölmesi nasıl yapılır?",
         "Bölünenin ilk terimi bölenin ilk terimine bölünür, bulunan terim bölenle çarpılıp bölünenden çıkarılır. Kalanın derecesi bölenin derecesinden küçük olana kadar bu adımlar tekrarlanır."),
        ("Bölme eşitliği nedir?",
         "Bölünen, bölen ile bölümün çarpımına kalanın eklenmesiyle elde edilir. Kalanın derecesi bölenin derecesinden küçüktür."),
        ("Horner yöntemi ne zaman kullanılır?",
         "Bölen x − a biçiminde olduğunda kullanılır. Yalnızca katsayılarla çalışır ve uzun bölmeden çok daha kısadır."),
        ("Bölümün derecesi nasıl bulunur?",
         "Bölünenin derecesinden bölenin derecesi çıkarılır. Derecesi 5 olan bir polinom derecesi 2 olan bir polinoma bölünürse bölümün derecesi 3 tür."),
        ("Kalan negatif olabilir mi?",
         "Evet. Kalan için tek koşul derecesinin bölenin derecesinden küçük olmasıdır; işareti herhangi olabilir."),
        ("Bir polinom x − a ile ne zaman kalansız bölünür?",
         "P(a) = 0 ise kalansız bölünür. Bu durumda x − a polinomun bir çarpanıdır."),
        ("Bölünen ile bölenin dereceleri eşitse bölüm ne olur?",
         "Bölüm bir sabittir ve baş katsayıların oranına eşittir. Kalan, bölünenden bölenin bu sabit katı çıkarılarak bulunur."),
        ("İkinci dereceden bir bölenle bölmede kalan nasıl bulunur?",
         "Kalan ax + b biçiminde yazılır ve bölenin kökleri bölme eşitliğine yerleştirilir. Bölen sıfır olduğu için iki denklem çıkar ve a ile b bulunur."),
    ],
    "kontrol": [
        "Bölme eşitliğini yazabiliyorum.",
        "Bölünen, bölen, bölüm ve kalanı ayırt edebiliyorum.",
        "Uzun bölmeyi adım adım yapabiliyorum.",
        "Eksik terimleri sıfır katsayıyla yazabiliyorum.",
        "İkinci dereceden bir bölenle bölme yapabiliyorum.",
        "Bölüm ve kalanın derecesini bölme yapmadan bulabiliyorum.",
        "Horner yöntemini uygulayabiliyorum.",
        "Bölme sonucunu bölme eşitliğiyle kontrol edebiliyorum.",
        "Bölüm ve kalandan bölüneni bulabiliyorum.",
        "Kalansız bölünme koşulundan bilinmeyen katsayıyı bulabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["polinomlar-konu-anlatimi", "polinomlarda-kalan", "polinomlarda-carpanlara-ayirma"],
}
