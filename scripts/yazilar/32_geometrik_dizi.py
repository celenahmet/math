# scripts/yazilar/32_geometrik_dizi.py — Geometrik Dizi Konu Anlatimi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "geometrik-dizi",
    "baslik": "Geometrik Dizi Konu Anlatımı",
    "aciklama": "Geometrik dizi nedir? Ortak oran, genel terim, geometrik ortalama, ilk n terim toplamı, sonsuz geometrik toplam, faiz ve zıplayan top problemleri; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "logaritma",
    "sinavlar": ["AYT"],
    "kapak": "geometrik-dizi",
    "kapak_alt": "Geometrik dizi: her adımda iki katına çıkan ahşap küp gruplarını yan yana dizen iki öğrenci",
    "ozet": "Geometrik dizi, ardışık iki teriminin oranı hep aynı olan dizidir. Her adımda aynı sayıyla çarpıldığı için terimleri katlanarak büyür ya da küçülür; bileşik faiz, nüfus artışı ve yarılanma gibi süreçler bu dizilerle modellenir. Bu yazıda geometrik dizinin tanımını ve ortak oranı, genel terimi, negatif ve kesirli oranları, geometrik ortalama özelliğini, simetrik terimleri, ilk n terim toplamını ve ispatını, sonsuz geometrik toplamı, devirli ondalık sayılarla bağlantısını ve faiz, bakteri, zıplayan top gibi problemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Geometrik dizi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dizi kavramını, üslü sayıları ve aritmetik diziyi biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/diziler-konu-anlatimi/\">Diziler Konu Anlatımı</a> ve <a href=\"/blog/aritmetik-dizi/\">Aritmetik Dizi Konu Anlatımı</a> yazılarına göz at."),
            "Ardışık iki teriminin oranı her zaman aynı olan dizilere <strong>geometrik dizi</strong> denir. Bu sabit orana <strong>ortak oran</strong> denir ve $r$ ile gösterilir. $3, 6, 12, 24, \\ldots$ dizisinde her terim bir öncekinin iki katıdır; ortak oran $r=2$ dir.",
            "Kapaktaki öğrenciler ahşap küpleri $1$, $2$, $4$ ve $8$ lik gruplar hâlinde diziyor. Her grup bir öncekinin iki katı olduğu için grupların büyüklükleri bir geometrik dizi oluşturuyor. Aritmetik dizide her adımda aynı sayı eklenirken geometrik dizide her adımda aynı sayıyla çarpılır.",
        ]},
        {"baslik": "Geometrik dizi olma koşulu", "icerik": [
            "Bir dizinin geometrik olup olmadığını anlamak için ardışık terimlerin oranına bakılır. Terimler sıfırdan farklıysa ve oran her $n$ için aynı sabitse dizi geometriktir: $\\dfrac{a_{n+1}}{a_n}=r$.",
            ornek(
                "$a_n=5 \\cdot 3^n$ ve $b_n=n \\cdot 2^n$ dizileri verilsin.",
                "Hangisinin geometrik dizi olduğunu bulalım.",
                "$\\dfrac{a_{n+1}}{a_n}=\\dfrac{5 \\cdot 3^{n+1}}{5 \\cdot 3^n}=3$; oran sabittir, $a_n$ geometriktir.",
                "$\\dfrac{b_{n+1}}{b_n}=\\dfrac{2(n+1)}{n}$; oran $n$ ye bağlıdır, $b_n$ geometrik değildir."),
            hap("Geometrik dizide her adımda aynı sayıyla çarpılır.",
                "Genel terimi $c \\cdot r^n$ biçiminde olan her dizi geometriktir."),
        ]},
        {"baslik": "Genel terim formülü", "icerik": [
            "Birinci terimden $n$ inci terime ulaşmak için ortak oranla $n-1$ kez çarpılır. Bu yüzden geometrik dizinin genel terimi şöyledir:",
            "$$a_n=a_1 \\cdot r^{n-1}$$",
            ornek(
                "$a_1=3$ ve $r=2$ olan geometrik dizi verilsin.",
                "Sekizinci terimi bulalım.",
                "$a_8=3 \\cdot 2^7$ olur.",
                "Sonuç $3 \\cdot 128=384$ tür."),
            "Aritmetik dizide olduğu gibi formül iki terim arasına da genellenir: $a_n=a_k \\cdot r^{n-k}$. Sıra numaraları farkı kadar ortak oranla çarpılır ya da bölünür.",
            hap("$a_n=a_1 \\cdot r^{n-1}$ olur; ortak oranın kuvveti $n-1$ olur."),
        ]},
        {"baslik": "İki terimi verilen dizi", "icerik": [
            "İki terimi bilinen bir geometrik dizide büyük sıralı terim küçük sıralı terime bölünür. Sonuç, ortak oranın sıra numaraları farkı kadar kuvvetidir.",
            ornek(
                "Bir geometrik dizide $a_2=6$ ve $a_5=162$ olsun.",
                "Ortak oranı, ilk terimi ve yedinci terimi bulalım.",
                "$\\dfrac{a_5}{a_2}=r^3=27$, yani $r=3$ olur; $a_1=\\dfrac{6}{3}=2$.",
                "$a_7=2 \\cdot 3^6=1458$ bulunur."),
            "Kuvvet çift olduğunda iki ortak oran çıkabilir. Örneğin $r^2=9$ ise $r=3$ ya da $r=-3$ olur; soruda başka bir bilgi yoksa iki dizi de koşulu sağlar.",
        ]},
        {"baslik": "Negatif ortak oran", "icerik": [
            "Ortak oran negatifse terimlerin işareti her adımda değişir. Böyle bir dizi ne artan ne azalandır; terimler sıfırın iki yanında gidip gelir ve mutlak değerleri $|r|$ ye göre büyür ya da küçülür.",
            ornek(
                "$2, -6, 18, -54, \\ldots$ dizisi verilsin.",
                "Ortak oranı ve altıncı terimi bulalım.",
                "$r=\\dfrac{-6}{2}=-3$ olur.",
                "$a_6=2 \\cdot (-3)^5=-486$ bulunur; çift sıralı terimler negatiftir."),
        ]},
        {"baslik": "Kesirli ortak oran", "icerik": [
            "Ortak oran $0$ ile $1$ arasındaysa pozitif terimli dizi azalır ve terimler sıfıra yaklaşır. Her adımda aynı oranda küçülen nicelikler bu tür dizilerle modellenir.",
            ornek(
                "$64, 32, 16, \\ldots$ dizisi verilsin.",
                "Ortak oranı ve yedinci terimi bulalım.",
                "$r=\\dfrac{32}{64}=\\dfrac{1}{2}$ olur.",
                "$a_7=64 \\cdot \\left(\\dfrac{1}{2}\\right)^6=1$ bulunur."),
        ]},
        {"baslik": "Artan, azalan ve değişken işaretli", "icerik": [
            "Geometrik dizinin davranışını ilk terimin işareti ve ortak oran birlikte belirler. İlk terim pozitifken durum şöyledir:",
            tablo(["Ortak oran", "Dizi", "Örnek"], [
                ["$r>1$", "Artan", "$2, 6, 18, \\ldots$"],
                ["$0<r<1$", "Azalan", "$81, 27, 9, \\ldots$"],
                ["$r=1$", "Sabit", "$5, 5, 5, \\ldots$"],
                ["$r<0$", "İşaret değiştirir", "$1, -2, 4, \\ldots$"],
            ]),
            "İlk terim negatifse artan ve azalan yer değiştirir: $-2, -6, -18, \\ldots$ dizisinde $r=3$ tür ama terimler küçüldüğü için dizi azalandır.",
        ]},
        {"baslik": "Geometrik ortalama özelliği", "icerik": [
            "Geometrik dizide her terimin karesi, komşu iki terimin çarpımına eşittir: $a_n^2=a_{n-1} \\cdot a_{n+1}$. Bu yüzden $a$, $b$, $c$ sayılarının geometrik dizi oluşturması için $b^2=ac$ olmalıdır. Pozitif terimlerde $b=\\sqrt{ac}$ sayısına $a$ ile $c$ nin geometrik ortalaması denir.",
            ornek(
                "$x$, $x+3$ ve $x+9$ sayıları bu sırayla bir geometrik dizinin ardışık terimleri olsun.",
                "$x$ i ve terimleri bulalım.",
                "$(x+3)^2=x(x+9)$, yani $x^2+6x+9=x^2+9x$ ve $x=3$ olur.",
                "Terimler $3$, $6$ ve $12$ dir; ortak oran $2$ dir."),
        ]},
        {"baslik": "Aritmetik ve geometrik ortalama", "icerik": [
            "İki pozitif sayının aritmetik ortalaması hiçbir zaman geometrik ortalamasından küçük değildir: $\\dfrac{a+b}{2} \\ge \\sqrt{ab}$. Eşitlik yalnızca iki sayı eşitken sağlanır.",
            ornek(
                "$4$ ve $9$ sayıları verilsin.",
                "Aritmetik ve geometrik ortalamalarını karşılaştıralım.",
                "Aritmetik ortalama $\\dfrac{4+9}{2}=6.5$ tir.",
                "Geometrik ortalama $\\sqrt{36}=6$ dır; aritmetik ortalama daha büyüktür."),
        ]},
        {"baslik": "Simetrik terimler", "icerik": [
            "Geometrik dizide sıra numaralarının toplamı eşit olan terim çiftlerinin çarpımları eşittir: $p+q=k+m$ ise $a_p \\cdot a_q=a_k \\cdot a_m$ olur. Aritmetik dizideki toplam özelliğinin çarpma karşılığıdır.",
            ornek(
                "Bir geometrik dizide $a_2 \\cdot a_9=20$ olsun.",
                "$a_5 \\cdot a_6$ ve $a_1 \\cdot a_{10}$ çarpımlarını bulalım.",
                "$2+9=5+6=11$ olduğundan $a_5 \\cdot a_6=20$ olur.",
                "$1+10=11$ olduğundan $a_1 \\cdot a_{10}=20$ olur."),
        ]},
        {"baslik": "Terim sayısı", "icerik": [
            "İlk ve son terimi ile ortak oranı bilinen bir geometrik dizinin terim sayısı, son terim ilk terime bölünerek bulunur. Bölüm, ortak oranın terim sayısından bir eksik kuvvetidir.",
            ornek(
                "$3, 6, 12, \\ldots, 768$ dizisi verilsin.",
                "Dizinin kaç terimi olduğunu bulalım.",
                "$\\dfrac{768}{3}=256=2^8$ olduğundan $n-1=8$ olur.",
                "Dizinin $9$ terimi vardır."),
        ]},
        {"baslik": "İlk n terimin toplamı", "icerik": [
            "Geometrik dizinin ilk $n$ teriminin toplamı $S_n$ olsun. $S_n$ ortak oranla çarpılıp kendisinden çıkarılırsa ortadaki bütün terimler sadeleşir ve yalnızca ilk terim ile $a_1 r^n$ kalır: $S_n-rS_n=a_1-a_1 r^n$. Buradan $r \\neq 1$ için şu formül çıkar:",
            "$$S_n=a_1 \\cdot \\dfrac{r^n-1}{r-1}$$",
            "Ortak oran $1$ ise bütün terimler eşittir ve toplam $S_n=n \\cdot a_1$ olur. Formüldeki kesir, $r<1$ iken pay ve payda negatif çıksın diye $\\dfrac{1-r^n}{1-r}$ olarak da yazılabilir; iki yazım aynı sonucu verir.",
            hap("$r \\neq 1$ için $S_n=a_1 \\cdot \\dfrac{r^n-1}{r-1}$ olur.", "$r=1$ ise bütün terimler eşittir ve $S_n=n \\cdot a_1$ olur."),
        ]},
        {"baslik": "Toplam formülünün kullanımı", "icerik": [
            "Toplam formülü ilk terim, ortak oran ve terim sayısıyla çalışır. Son terim verilmişse önce terim sayısı bulunur.",
            ornek(
                "$3, 6, 12, \\ldots$ dizisi verilsin.",
                "İlk $8$ terimin toplamını bulalım.",
                "$S_8=3 \\cdot \\dfrac{2^8-1}{2-1}$ olur.",
                "$3 \\cdot 255=765$ bulunur."),
            ornek(
                "$1+2+4+\\cdots+2^9$ toplamı verilsin.",
                "Değerini bulalım.",
                "Toplamda $10$ terim vardır, $a_1=1$ ve $r=2$ dir.",
                "$S_{10}=2^{10}-1=1023$ bulunur."),
        ]},
        {"baslik": "Kesirli oranla toplam", "icerik": [
            "Ortak oran $1$ den küçükken formülün $\\dfrac{1-r^n}{1-r}$ biçimi hesabı kolaylaştırır. Terimler küçüldüğü için toplam, terim sayısı arttıkça belirli bir sayıya yaklaşır.",
            ornek(
                "$1+\\dfrac{1}{2}+\\dfrac{1}{4}+\\cdots+\\dfrac{1}{32}$ toplamı verilsin.",
                "Değerini bulalım.",
                "Toplamda $6$ terim vardır ve $r=\\dfrac{1}{2}$ dir: $S_6=\\dfrac{1-\\left(\\dfrac{1}{2}\\right)^6}{1-\\dfrac{1}{2}}$.",
                "$2 \\cdot \\dfrac{63}{64}=\\dfrac{63}{32}$ bulunur; toplam $2$ ye çok yakındır."),
        ]},
        {"baslik": "Sonsuz geometrik toplam", "icerik": [
            "Ortak oranın mutlak değeri $1$ den küçükse $r^n$ terimi sıfıra yaklaşır. Bu yüzden $|r|<1$ olduğunda, terim sayısı sonsuza giderken toplam belirli bir sayıya ulaşır:",
            "$$S=\\dfrac{a_1}{1-r}$$",
            ornek(
                "$1+\\dfrac{1}{2}+\\dfrac{1}{4}+\\cdots$ sonsuz toplamı verilsin.",
                "Değerini bulalım.",
                "$a_1=1$ ve $r=\\dfrac{1}{2}$ olduğundan $S=\\dfrac{1}{1-\\dfrac{1}{2}}$ olur.",
                "Sonuç $2$ dir."),
            "Ortak oranın mutlak değeri $1$ ya da daha büyükse terimler küçülmez ve toplam sonsuza gider ya da bir değere yerleşmez. $1+2+4+\\cdots$ toplamının sonlu bir değeri yoktur.",
            hap("$|r|<1$ ise sonsuz toplam $\\dfrac{a_1}{1-r}$ olur.", "$|r| \\ge 1$ ise sonsuz toplam bir sayıya yaklaşmaz."),
        ]},
        {"baslik": "Devirli ondalık sayılar", "icerik": [
            "Devirli ondalık sayılar aslında sonsuz geometrik toplamlardır. $0.333\\ldots$ sayısı $\\dfrac{3}{10}+\\dfrac{3}{100}+\\cdots$ toplamıdır; ilk terimi $\\dfrac{3}{10}$, ortak oranı $\\dfrac{1}{10}$ dir.",
            ornek(
                "$0.3636\\ldots$ devirli sayısı verilsin.",
                "Sayıyı kesir olarak yazalım.",
                "Toplam $\\dfrac{36}{100}+\\dfrac{36}{10000}+\\cdots$ olur; $a_1=\\dfrac{36}{100}$ ve $r=\\dfrac{1}{100}$.",
                "$S=\\dfrac{36/100}{99/100}=\\dfrac{36}{99}=\\dfrac{4}{11}$ bulunur."),
            "Bu yöntem, devirli sayıyı kesre çevirme kuralının neden doğru olduğunu da açıklar. Ayrıntılı kurallar için <a href=\"/blog/devirli-ondalik-sayilar-nasil-kesre-cevrilir/\">Devirli Ondalık Sayılar Nasıl Kesre Çevrilir?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Üç terim problemi", "icerik": [
            "Geometrik dizi oluşturan üç sayı sorulduğunda terimleri $\\dfrac{a}{r}$, $a$ ve $ar$ olarak almak hesabı kısaltır; çünkü çarpımda ortak oran sadeleşir ve ortanca terim hemen bulunur.",
            ornek(
                "Geometrik dizi oluşturan üç pozitif sayının çarpımı $216$, toplamı $21$ olsun.",
                "Sayıları bulalım.",
                "Çarpımdan $a^3=216$, yani $a=6$. Toplamdan $\\dfrac{6}{r}+6+6r=21$, yani $2r^2-5r+2=0$ ve $r=2$ ya da $r=\\dfrac{1}{2}$.",
                "İki durumda da sayılar $3$, $6$ ve $12$ olur."),
        ]},
        {"baslik": "Problem: bileşik faiz", "icerik": [
            "Bileşik faizde her yılın sonundaki para, bir önceki yılın paranın faiz oranı kadar fazlasıdır. Bu yüzden yıl sonu tutarları ortak oranı $1+\\dfrac{\\text{faiz}}{100}$ olan bir geometrik dizi oluşturur.",
            ornek(
                "$1000$ TL yıllık yüzde $10$ bileşik faizle yatırılıyor.",
                "İlk üç yılın sonundaki tutarları bulalım.",
                "Ortak oran $1.1$ dir; birinci yıl sonunda $1100$ TL, ikinci yıl sonunda $1210$ TL olur.",
                "Üçüncü yıl sonunda $1000 \\cdot 1.1^3=1331$ TL olur."),
            "Paranın belirli bir tutara kaç yılda ulaşacağı ise logaritma ile bulunur; bunun için <a href=\"/blog/logaritmik-denklemler/\">Logaritmik Denklemler Nasıl Çözülür?</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Problem: bakteri üremesi", "icerik": [
            "Sabit sürelerde bölünerek çoğalan canlıların sayısı geometrik dizi oluşturur. Her dönemde sayı iki katına çıkıyorsa ortak oran $2$ dir ve $n$ dönem sonraki sayı başlangıç sayısının $2^n$ katı olur.",
            ornek(
                "Bir bakteri her $20$ dakikada bir ikiye bölünüyor ve başlangıçta $1$ bakteri var.",
                "İki saat sonra kaç bakteri olacağını bulalım.",
                "İki saat $120$ dakikadır; bu sürede $6$ bölünme olur.",
                "Bakteri sayısı $2^6=64$ olur."),
            hap("Her ikiye katlamada kalınlık iki katına çıkar.", "$0.1$ milimetrelik bir kâğıt $10$ kez ikiye katlanabilseydi kalınlığı $0.1 \\cdot 2^{10}=102.4$ milimetreye, yani yaklaşık $10$ santimetreye çıkardı.", gunluk=True),
        ]},
        {"baslik": "Problem: zıplayan top", "icerik": [
            "Yere çarptıktan sonra her seferinde bir önceki yüksekliğin sabit bir kesri kadar yükselen top, geometrik dizinin klasik bir uygulamasıdır. Topun aldığı toplam yol ise sonsuz geometrik toplamla bulunur.",
            ornek(
                "$16$ metre yükseklikten bırakılan bir top her çarpmadan sonra bir önceki yüksekliğin $\\dfrac{3}{4}$ ü kadar yükseliyor.",
                "Üçüncü sıçramanın yüksekliğini ve topun durana kadar aldığı toplam yolu bulalım.",
                "Sıçrama yükseklikleri $12$, $9$, $6.75$ metre olur; üçüncü sıçrama $16 \\cdot \\left(\\dfrac{3}{4}\\right)^3=6.75$ metredir.",
                "Sıçramaların toplamı $\\dfrac{12}{1-\\dfrac{3}{4}}=48$ metredir; top her sıçramada hem çıkıp hem indiği için toplam yol $16+2 \\cdot 48=112$ metre olur."),
        ]},
        {"baslik": "Problem: iç içe kareler", "icerik": [
            "Bir karenin kenar orta noktaları birleştirilince alanı yarısı kadar olan yeni bir kare oluşur. İşlem tekrarlandıkça karelerin alanları ortak oranı $\\dfrac{1}{2}$ olan bir geometrik dizi oluşturur.",
            ornek(
                "Kenarı $4$ birim olan bir karenin içine bu yolla sonsuz sayıda kare çiziliyor.",
                "Bütün karelerin alanları toplamını bulalım.",
                "Alanlar $16$, $8$, $4$, $\\ldots$ olur; $a_1=16$ ve $r=\\dfrac{1}{2}$.",
                "Toplam $\\dfrac{16}{1-\\dfrac{1}{2}}=32$ birimkare olur."),
        ]},
        {"baslik": "Problem: yarılanma", "icerik": [
            "Radyoaktif maddeler ve bazı ilaçların vücuttaki miktarı sabit sürelerde yarıya iner. Her yarılanma süresinin sonundaki miktarlar ortak oranı $\\dfrac{1}{2}$ olan bir geometrik dizi oluşturur.",
            ornek(
                "Yarılanma süresi $5$ yıl olan bir maddeden $1600$ gram var.",
                "$20$ yıl sonra kalan miktarı bulalım.",
                "$20$ yılda $4$ yarılanma olur.",
                "Kalan miktar $1600 \\cdot \\left(\\dfrac{1}{2}\\right)^4=100$ gram olur."),
        ]},
        {"baslik": "Geometrik dizinin logaritması", "icerik": [
            "Pozitif terimli bir geometrik dizinin terimlerinin logaritması alınırsa bir aritmetik dizi elde edilir. Çarpma logaritmada toplamaya dönüştüğü için ortak oranla çarpmak, ortak farkı $\\log r$ olan bir eklemeye dönüşür.",
            ornek(
                "$2, 4, 8, 16, \\ldots$ geometrik dizisi verilsin.",
                "Terimlerin $2$ tabanında logaritmalarını inceleyelim.",
                "Logaritmalar $1$, $2$, $3$, $4$, $\\ldots$ olur.",
                "Bu, ortak farkı $\\log_2 2=1$ olan bir aritmetik dizidir."),
            "Bu bağlantı, katlanarak büyüyen verilerin logaritmik ölçekte düz bir çizgi gibi görünmesinin de nedenidir. Logaritmanın ayrıntıları için <a href=\"/blog/logaritma-konu-anlatimi/\">Logaritma Konu Anlatımı</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Aritmetik ve geometrik dizi karşılaştırması", "icerik": [
            tablo(["Özellik", "Aritmetik dizi", "Geometrik dizi"], [
                ["Adım", "Aynı sayı eklenir", "Aynı sayıyla çarpılır"],
                ["Sabit", "Ortak fark $d$", "Ortak oran $r$"],
                ["Genel terim", "$a_1+(n-1)d$", "$a_1 \\cdot r^{n-1}$"],
                ["Orta terim", "$2b=a+c$", "$b^2=ac$"],
                ["Simetrik terimler", "Toplamlar eşit", "Çarpımlar eşit"],
                ["Büyüme", "Doğrusal", "Üstel"],
            ]),
            "Uzun vadede üstel büyüme her zaman doğrusal büyümeyi geçer. Her gün $100$ TL eklenen bir birikim ile her gün iki katına çıkan bir kuruş arasındaki fark, birkaç haftada çok büyük boyutlara ulaşır.",
        ]},
        {"baslik": "Sınavda geometrik dizi", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) geometrik diziler; genel terim, iki terimi verilen dizi, geometrik ortalama, simetrik terimler, toplam formülü ve sonsuz toplam biçiminde karşına çıkabilir.",
                "Faiz, nüfus ve zıplayan top gibi problemler de bu konuya dayanır."),
            "Soruda iki terim verilmişse büyük sıralıyı küçük sıralıya bölerek ortak oranın kuvvetini bul. Çarpım soruluyorsa simetrik terim özelliğine, sonsuz toplam soruluyorsa önce ortak oranın mutlak değerinin $1$ den küçük olup olmadığına bak.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$a_n=a_1 \\cdot r^n$ yazmak", "$a_n=a_1 \\cdot r^{n-1}$"],
                ["$r^2=9$ iken yalnız $r=3$ almak", "$r=-3$ de olabilir"],
                ["$|r| \\ge 1$ iken sonsuz toplam formülünü kullanmak", "Toplam sonlu değildir"],
                ["$r=1$ iken toplam formülünü kullanmak", "$S_n=n \\cdot a_1$"],
                ["Zıplayan topta sıçramaları bir kez saymak", "Çıkış ve iniş iki kez sayılır"],
                ["Geometrik ortalamada $b=\\dfrac{a+c}{2}$ yazmak", "$b^2=ac$"],
            ]),
            "Bu hataların çoğu aritmetik dizinin formüllerini geometrik diziye taşımaktan doğar. Toplama yerine çarpma, fark yerine oran ve katsayı yerine kuvvet düşünmek, iki dizi arasındaki geçişi doğru yapmayı sağlar.",
        ]},
    ],
    "sss": [
        ("Geometrik dizi nedir?",
         "Ardışık iki teriminin oranı hep aynı olan dizidir. Bu sabit orana ortak oran denir."),
        ("Geometrik dizinin genel terimi nedir?",
         "a n eşittir a 1 çarpı r üzeri n eksi 1 dir. İlk terim ortak oranla n eksi 1 kez çarpılır."),
        ("Geometrik dizide ilk n terimin toplamı nasıl bulunur?",
         "r 1 den farklıysa S n eşittir a 1 çarpı r üzeri n eksi 1 bölü r eksi 1 dir. r 1 ise toplam n çarpı a 1 olur."),
        ("Sonsuz geometrik toplam ne zaman vardır?",
         "Ortak oranın mutlak değeri 1 den küçükse vardır ve a 1 bölü 1 eksi r ye eşittir."),
        ("Geometrik ortalama nedir?",
         "İki pozitif sayının çarpımının kareköküdür. a, b, c geometrik dizi oluşturuyorsa b nin karesi a ile c nin çarpımına eşittir."),
        ("Devirli ondalık sayı geometrik diziyle nasıl kesre çevrilir?",
         "Devirli sayı sonsuz bir geometrik toplam olarak yazılır ve a 1 bölü 1 eksi r formülü uygulanır. Örneğin 0.3636 devirli sayısı 4 bölü 11 dir."),
        ("Geometrik dizi ile aritmetik dizi arasındaki fark nedir?",
         "Aritmetik dizide her adımda aynı sayı eklenir, geometrik dizide ise her adımda aynı sayıyla çarpılır. Bu yüzden aritmetik dizi doğrusal, geometrik dizi üstel büyür."),
    ],
    "kontrol": [
        "Geometrik diziyi ve ortak oranı tanımlayabiliyorum.",
        "Bir dizinin geometrik olup olmadığını belirleyebiliyorum.",
        "Genel terim formülüyle istenen terimi bulabiliyorum.",
        "İki terimi verilen dizinin ortak oranını bulabiliyorum.",
        "Negatif ve kesirli ortak oranlı dizilerin davranışını açıklayabiliyorum.",
        "Geometrik ortalama ve simetrik terim özelliklerini kullanabiliyorum.",
        "İlk n terimin toplamını hesaplayabiliyorum.",
        "Sonsuz geometrik toplamı ve koşulunu biliyorum.",
        "Devirli ondalık sayıları geometrik toplamla kesre çevirebiliyorum.",
        "Faiz, bakteri ve zıplayan top problemlerini çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["aritmetik-dizi", "diziler-konu-anlatimi", "logaritma-konu-anlatimi"],
}
