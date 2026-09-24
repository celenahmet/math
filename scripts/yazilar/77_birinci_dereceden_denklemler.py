# scripts/yazilar/77_birinci_dereceden_denklemler.py — Birinci Dereceden Denklemler (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "birinci-dereceden-denklemler-konu-anlatimi-pdf",
    "baslik": "Birinci Dereceden Denklemler Konu Anlatımı PDF",
    "aciklama": "Birinci dereceden denklem nedir, nasıl çözülür? Terazi modeli, parantezli, kesirli ve ondalıklı denklemler, çözüm kümesi ve iki bilinmeyen; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "cebir",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "birinci-dereceden-denklemler-konu-anlatimi-pdf",
    "kapak_alt": "Birinci dereceden denklemler: terazinin iki kefesine mavi ve kırmızı bloklar yerleştirerek dengeyi koruyan öğrenci",
    "ozet": "Denklem, içinde bilinmeyen bulunan bir eşitliktir; denklemi çözmek, eşitliği doğru yapan değeri bulmaktır. Birinci dereceden denklemlerde bilinmeyenin en büyük üssü birdir ve bu denklemler problemlerin neredeyse tamamının son adımıdır. Bu yazıda denklemin ne olduğunu, terazi modeliyle eşitliğin nasıl korunduğunu, adım adım çözüm yolunu, parantezli, kesirli ve ondalıklı denklemleri, çözümü olmayan ve sonsuz çözümü olan denklemleri ve iki bilinmeyenli denklemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Denklem nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için cebirsel ifadeleri, parantez açmayı ve benzer terimleri birleştirmeyi biliyor olman yeterli.",
                "Bu konular için <a href=\"/blog/cebirsel-ifadeler-konu-anlatimi-pdf/\">Cebirsel İfadeler Konu Anlatımı PDF</a> yazısına göz at."),
            "İçinde bilinmeyen bulunan ve yalnızca bilinmeyenin bazı değerleri için doğru olan eşitliklere <strong>denklem</strong> denir. $2x+3=11$ bir denklemdir: $x=4$ için doğru, başka her değer için yanlıştır. Eşitliği doğru yapan değere denklemin <strong>kökü</strong> ya da <strong>çözümü</strong>, bütün çözümlerin oluşturduğu kümeye de <strong>çözüm kümesi</strong> denir.",
            "Bilinmeyenin en büyük üssü $1$ olan denklemlere <strong>birinci dereceden denklem</strong> denir. Tek bilinmeyenli birinci dereceden bir denklem, sadeleştirildiğinde her zaman şu biçime getirilebilir:",
            "$$ax+b=0$$",
            "Burada $a$ ve $b$ sabit sayılardır ve $a$ sıfırdan farklıdır; $a$ sıfır olsaydı bilinmeyen denklemden tamamen düşerdi.",
            tablo(["Denklem", "Derecesi", "Neden"], [
                ["$3x-7=5$", "$1$", "$x$ in üssü $1$"],
                ["$5=2x$", "$1$", "Taraflar yer değiştirebilir"],
                ["$x^2-4=0$", "$2$", "$x$ in üssü $2$"],
                ["$4(x+1)=3x$", "$1$", "Parantez açılınca $x$ kalır"],
            ]),
            "Her değer için doğru olan eşitlikler ise denklem değil <strong>özdeşliktir</strong>: $2(x+1)=2x+2$ eşitliği $x$ yerine hangi sayı yazılırsa yazılsın doğrudur.",
            hap("Denklem, bilinmeyenin yalnızca bazı değerleri için doğru olan eşitliktir.",
                "Birinci dereceden denklemde bilinmeyenin en büyük üssü $1$ dir: $ax+b=0$ ve $a \\neq 0$."),
        ]},
        {"baslik": "Terazi modeli: eşitliği korumak", "icerik": [
            "Bir denklemi dengedeki bir terazi gibi düşünmek, çözüm kurallarının nereden geldiğini gösterir. Terazinin iki kefesine aynı ağırlık eklenir ya da iki kefeden aynı ağırlık alınırsa denge bozulmaz. İki kefedeki her şey aynı oranda artırılır ya da azaltılırsa da denge korunur.",
            "Bu yüzden bir denklemin iki tarafına şu işlemler uygulanabilir ve çözüm değişmez:",
            "<ul><li>İki tarafa <strong>aynı sayıyı eklemek</strong> ya da iki taraftan aynı sayıyı çıkarmak,</li>"
            "<li>İki tarafı <strong>sıfırdan farklı aynı sayıyla</strong> çarpmak ya da bölmek.</li></ul>",
            ornek(
                "Terazinin sol kefesinde $3$ özdeş kutu ve $2$ gramlık bir ağırlık, sağ kefesinde $11$ gram olsun ve terazi dengede dursun.",
                "Bir kutunun ağırlığını bulalım.",
                "Bir kutunun ağırlığına $x$ diyelim: $3x+2=11$.",
                "İki kefeden $2$ gram alalım: $3x=9$.",
                "İki kefedeki her şeyi üçe bölelim: $x=3$ gram.",
                "Kontrol: $3 \\cdot 3+2=11$."),
            dikkat(
                "İki tarafı sıfırla çarpmak ya da sıfıra bölmek.",
                "İki tarafı $0$ ile çarpmak her denklemi $0=0$ a dönüştürür ve bilgiyi yok eder; sıfıra bölmek ise tanımsızdır. Çarpılan ya da bölünen sayının sıfırdan farklı olduğundan emin ol."),
        ]},
        {"baslik": "Adım adım çözüm", "icerik": [
            "Birinci dereceden bir denklem, aşağıdaki sırayla çözülebilir. Her adımda eşitliğin iki tarafına aynı işlem uygulanır:",
            "<ol><li>Paydalar varsa iki tarafı paydaların EKOK'u ile çarparak paydaları yok et.</li>"
            "<li>Parantezleri aç.</li>"
            "<li>Bilinmeyenli terimleri bir tarafa, sabit terimleri diğer tarafa topla.</li>"
            "<li>Benzer terimleri birleştir.</li>"
            "<li>İki tarafı bilinmeyenin katsayısına böl.</li>"
            "<li>Bulduğun değeri ilk denklemde yerine koyarak kontrol et.</li></ol>",
            "Bir terimi eşitliğin öbür tarafına geçirmek, aslında iki tarafa o terimin tersini eklemektir. Bu yüzden karşıya geçen terimin işareti değişir: $+5$ karşıya $-5$ olarak, $-4$ karşıya $+4$ olarak geçer.",
            ornek(
                "$5x-4=2x+11$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Bilinmeyenleri sola, sabitleri sağa toplayalım: $5x-2x=11+4$.",
                "$3x=15$, yani $x=5$.",
                "Kontrol: sol taraf $5 \\cdot 5-4=21$, sağ taraf $2 \\cdot 5+11=21$."),
            ornek(
                "$7-3x=x-9$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Bilinmeyenleri sağa, sabitleri sola toplayalım: $7+9=x+3x$.",
                "$16=4x$, yani $x=4$.",
                "Kontrol: $7-12=-5$ ve $4-9=-5$."),
            "İkinci örnekte bilinmeyenleri sağ tarafta toplamak, negatif katsayıyla uğraşmayı önledi. Hangi tarafın seçildiği sonucu değiştirmez; yalnızca işlem kolaylığı sağlar. Genel bir alışkanlık olarak bilinmeyenleri, katsayısı büyük olan tarafta toplamak işaret hatalarını azaltır.",
        ]},
        {"baslik": "Parantezli denklemler", "icerik": [
            "Parantez içeren denklemlerde önce parantezler dağılma özelliğiyle açılır. Parantezin önünde eksi işareti varsa, parantezin içindeki bütün terimlerin işareti değişir.",
            ornek(
                "$3(x-2)-2(x+1)=4$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Parantezleri açalım: $3x-6-2x-2=4$.",
                "Benzer terimleri birleştirelim: $x-8=4$, yani $x=12$.",
                "Kontrol: $3 \\cdot 10-2 \\cdot 13=30-26=4$."),
            ornek(
                "$2(3x+1)=5(x-2)+3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Parantezleri açalım: $6x+2=5x-10+3$, yani $6x+2=5x-7$.",
                "Bilinmeyenleri sola toplayalım: $6x-5x=-7-2$, yani $x=-9$.",
                "Kontrol: sol taraf $2 \\cdot (-26)=-52$, sağ taraf $5 \\cdot (-11)+3=-52$."),
            dikkat(
                "Eksiyi yalnızca ilk terime dağıtmak.",
                "$-2(x+1)$ açılırken sonuç $-2x+1$ değil, $-2x-2$ dir. Parantezin önündeki sayı ve işaret, parantezdeki her terimle ayrı ayrı çarpılır."),
        ]},
        {"baslik": "Kesirli denklemler", "icerik": [
            "Paydalı terimler içeren denklemlerde ilk iş, iki tarafı <strong>paydaların EKOK'u</strong> ile çarparak paydaları yok etmektir. Böylece denklem, kesirsiz ve çözmesi kolay bir denkleme dönüşür. EKOK'un nasıl bulunduğu <a href=\"/blog/ebob-ve-ekok-konu-anlatimi-pdf/\">EBOB ve EKOK Konu Anlatımı PDF</a> yazısında.",
            ornek(
                "$\\dfrac{x}{3}+\\dfrac{x}{4}=14$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Paydaların EKOK'u $12$. İki tarafı $12$ ile çarpalım: $4x+3x=168$.",
                "$7x=168$, yani $x=24$.",
                "Kontrol: $\\dfrac{24}{3}+\\dfrac{24}{4}=8+6=14$."),
            ornek(
                "$\\dfrac{x-1}{2}-\\dfrac{x+2}{5}=3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Paydaların EKOK'u $10$. İki tarafı $10$ ile çarpalım: $5(x-1)-2(x+2)=30$.",
                "Parantezleri açalım: $5x-5-2x-4=30$, yani $3x-9=30$.",
                "$3x=39$, yani $x=13$. Kontrol: $\\dfrac{12}{2}-\\dfrac{15}{5}=6-3=3$."),
            dikkat(
                "EKOK ile çarparken bir terimi atlamak.",
                "EKOK ile çarpma, eşitliğin iki tarafındaki <strong>her terime</strong> uygulanır; paydası olmayan terimler ve sağ taraf da dahil. İkinci örnekte sağdaki $3$ ün de $10$ ile çarpılıp $30$ olduğuna dikkat et. Payı birden fazla terimli kesirler ise çarpımdan sonra parantez içinde yazılmalıdır."),
        ]},
        {"baslik": "Ondalıklı denklemler", "icerik": [
            "Ondalık sayı içeren denklemlerde iki taraf $10$, $100$ ya da $1000$ ile çarpılarak bütün katsayılar tam sayı yapılır. Hangi sayıyla çarpılacağını, en çok ondalık basamağı olan sayı belirler.",
            ornek(
                "$0.2x+1.5=0.5x-0.3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "En çok bir ondalık basamak var; iki tarafı $10$ ile çarpalım: $2x+15=5x-3$.",
                "$15+3=5x-2x$, yani $18=3x$ ve $x=6$.",
                "Kontrol: $1.2+1.5=2.7$ ve $3-0.3=2.7$."),
            "Ondalık sayılarla çalışmanın ayrıntısı <a href=\"/blog/ondalik-gosterim-konu-anlatimi-pdf/\">Ondalık Gösterim Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Hesabı kısaltan yollar", "icerik": [
            "Her denklemde bütün adımları sırayla uygulamak gerekmez. Denklemin yapısına bakmak, çoğu zaman işlemi kısaltır.",
            "<h3>Ortak çarpana bölmek</h3>",
            "Bütün terimlerde ortak bir çarpan varsa önce iki taraf bu çarpana bölünür. Böylece küçük sayılarla çalışılır.",
            ornek(
                "$12x-36=48$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Bütün terimler $12$ ye bölünür: $x-3=4$.",
                "$x=7$. Kontrol: $12 \\cdot 7-36=84-36=48$."),
            "<h3>İki kesrin eşitliği</h3>",
            "Denklem iki kesrin eşitliği biçimindeyse EKOK yerine doğrudan içler dışlar çarpımı yapılabilir.",
            ornek(
                "$\\dfrac{2x-1}{3}=\\dfrac{x+4}{2}$ denklemi verilsin.",
                "Denklemi çözelim.",
                "İçler dışlar çarpımı: $2(2x-1)=3(x+4)$.",
                "$4x-2=3x+12$, yani $x=14$.",
                "Kontrol: $\\dfrac{27}{3}=9$ ve $\\dfrac{18}{2}=9$."),
            "Oran ve orantının bu kullanımı <a href=\"/blog/oran-ve-oranti-konu-anlatimi-pdf/\">Oran ve Orantı Konu Anlatımı PDF</a> yazısında da anlatılıyor.",
        ]},
        {"baslik": "Çözüm kümesi: tek çözüm, çözüm yok, sonsuz çözüm", "icerik": [
            "Sadeleştirme sırasında bilinmeyenli terimler birbirini götürürse denklem ya hiç çözümü olmayan bir çelişkiye ya da her değer için doğru olan bir özdeşliğe dönüşür.",
            tablo(["Sadeleşmiş hâl", "Çözüm kümesi", "Örnek"], [
                ["$ax=c$ ve $a \\neq 0$", "Tek çözüm: $x=\\dfrac{c}{a}$", "$3x=12$ ise $x=4$"],
                ["$0 \\cdot x=c$ ve $c \\neq 0$", "Çözüm yok: $\\emptyset$", "$2x+3=2x+5$"],
                ["$0 \\cdot x=0$", "Her gerçek sayı: $\\mathbb{R}$", "$2(x+3)=2x+6$"],
            ]),
            ornek(
                "$2x+3=2x+5$ ve $2(x+3)=2x+6$ denklemleri verilsin.",
                "Çözüm kümelerini bulalım.",
                "Birinci: $2x$ ler birbirini götürür ve $3=5$ kalır. Bu hiçbir zaman doğru olmadığı için çözüm kümesi $\\emptyset$ dir.",
                "İkinci: parantez açılınca $2x+6=2x+6$ olur ve $0=0$ kalır. Her değer için doğru olduğu için çözüm kümesi $\\mathbb{R}$ dir."),
            "<h3>Parametreli denklemler</h3>",
            "Katsayılardan biri harfle verilmişse, denklemin çözüm durumu bu harfin değerine bağlıdır.",
            ornek(
                "$(m-2)x=m-2$ denklemi verilsin.",
                "$m$ nin değerine göre çözüm kümesini inceleyelim.",
                "$m \\neq 2$ ise iki taraf $m-2$ ye bölünebilir: tek çözüm $x=1$.",
                "$m=2$ ise denklem $0 \\cdot x=0$ olur: her gerçek sayı çözümdür."),
            dikkat(
                "$0=0$ sonucunu \"çözüm sıfır\" sanmak.",
                "$0=0$ kalması, $x=0$ demek değildir; her değerin çözüm olduğu anlamına gelir. $3=5$ gibi bir çelişki kalması ise hiçbir değerin çözüm olmadığını gösterir."),
        ]},
        {"baslik": "Kökü verilen denklemde katsayı bulmak", "icerik": [
            "Bazı sorularda denklemin kökü verilir ve denklemdeki bilinmeyen bir katsayı sorulur. Kök, denklemi doğru yapan değer olduğu için yerine yazıldığında eşitlik sağlanmalıdır.",
            ornek(
                "$3x+a=2x-5$ denkleminin kökü $4$ olsun.",
                "$a$ yı bulalım.",
                "$x=4$ yazalım: $3 \\cdot 4+a=2 \\cdot 4-5$.",
                "$12+a=3$, yani $a=-9$.",
                "Kontrol: $3x-9=2x-5$ denkleminden $x=4$ bulunur."),
        ]},
        {"baslik": "Bilinmeyen paydada olursa", "icerik": [
            "Bilinmeyen paydada bulunuyorsa önce paydayı sıfır yapan değerler belirlenir; bu değerler kök olamaz. Sonra iki taraf paydalarla çarpılır ve çıkan denklem çözülür. Bulunan değer, yasaklı değerlerden biriyse atılır.",
            ornek(
                "$\\dfrac{6}{x-1}=3$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Payda sıfır olamaz: $x \\neq 1$.",
                "İçler dışlar çarpımı: $6=3(x-1)$, yani $6=3x-3$ ve $x=3$.",
                "$3 \\neq 1$ olduğu için kök geçerlidir. Kontrol: $\\dfrac{6}{2}=3$."),
            ornek(
                "$\\dfrac{x+2}{x-1}=\\dfrac{x+5}{x+1}$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Paydalar sıfır olamaz: $x \\neq 1$ ve $x \\neq -1$.",
                "İçler dışlar çarpımı: $(x+2)(x+1)=(x+5)(x-1)$, yani $x^2+3x+2=x^2+4x-5$.",
                "$x^2$ ler birbirini götürür: $3x+2=4x-5$, yani $x=7$. Kontrol: $\\dfrac{9}{6}=\\dfrac{12}{8}=\\dfrac{3}{2}$."),
            dikkat(
                "Paydayı sıfır yapan değeri kök sanmak.",
                "$\\dfrac{x}{x-2}=\\dfrac{2}{x-2}$ denkleminde paydalar eşitlenince $x=2$ bulunur. Ama $x=2$ paydayı sıfır yaptığı için kök olamaz; denklemin çözüm kümesi $\\emptyset$ dir."),
        ]},
        {"baslik": "Mutlak değerli basit denklemler", "icerik": [
            "$|x-3|=5$ gibi bir denklem, sayı doğrusunda $3$ e uzaklığı $5$ olan sayıları sorar. Bu sayılar iki tanedir; bu yüzden denklem iki ayrı birinci dereceden denkleme ayrılır.",
            ornek(
                "$|x-3|=5$ denklemi verilsin.",
                "Denklemi çözelim.",
                "Birinci durum: $x-3=5$, yani $x=8$.",
                "İkinci durum: $x-3=-5$, yani $x=-2$.",
                "Çözüm kümesi $\\{-2, 8\\}$ dir."),
            "Mutlak değer negatif olamayacağı için $|x-3|=-5$ gibi bir denklemin çözümü yoktur. Mutlak değerin ayrıntısı <a href=\"/blog/mutlak-deger-konu-anlatimi-pdf/\">Mutlak Değer Konu Anlatımı PDF</a> yazısında.",
        ]},
        {"baslik": "İki bilinmeyenli denklemler", "icerik": [
            "$x+y=10$ gibi iki bilinmeyenli tek bir denklemin sonsuz sayıda çözümü vardır: $(1, 9)$, $(4, 6)$, $(7, 3)$ ve daha niceleri. Tek bir çözüm bulmak için ikinci bir denkleme ihtiyaç vardır. İki denklemin birlikte oluşturduğu yapıya <strong>denklem sistemi</strong> denir.",
            "<h3>Yok etme yöntemi</h3>",
            ornek(
                "$x+y=10$ ve $x-y=4$ denklemleri verilsin.",
                "Sistemi çözelim.",
                "İki denklemi taraf tarafa toplayalım; $y$ ler birbirini götürür: $2x=14$, yani $x=7$.",
                "Birinci denklemde yerine koyalım: $7+y=10$, yani $y=3$.",
                "Kontrol: $7+3=10$ ve $7-3=4$."),
            "<h3>Yerine koyma yöntemi</h3>",
            ornek(
                "$y=2x-1$ ve $3x+y=19$ denklemleri verilsin.",
                "Sistemi çözelim.",
                "Birinci denklemdeki $y$ yi ikincide yerine koyalım: $3x+2x-1=19$.",
                "$5x=20$, yani $x=4$ ve $y=2 \\cdot 4-1=7$.",
                "Kontrol: $3 \\cdot 4+7=19$."),
            "Bir bilinmeyen diğeri cinsinden kolayca yazılabiliyorsa yerine koyma, katsayılar birbirini götürmeye uygunsa yok etme yöntemi daha kısadır.",
            "Tek bilinmeyenli denklemlerde olduğu gibi sistemlerde de çözüm olmayabilir ya da sonsuz çözüm olabilir. $x+y=3$ ve $x+y=5$ sisteminde aynı toplam iki farklı sayıya eşit olamayacağı için çözüm yoktur. $x+y=3$ ve $2x+2y=6$ sisteminde ise ikinci denklem birincinin iki katıdır; iki denklem aslında aynı bilgiyi verdiği için sonsuz çözüm vardır.",
        ]},
        {"baslik": "Problemden denkleme", "icerik": [
            "Sözel problemlerin çoğu, bilinmeyene bir harf verilip cümle denkleme çevrilince birinci dereceden bir denkleme dönüşür.",
            ornek(
                "Bir sayının $3$ katının $5$ fazlası $26$ dır.",
                "Sayıyı bulalım.",
                "Sayı $x$ olsun: $3x+5=26$.",
                "$3x=21$, yani $x=7$."),
            ornek(
                "Bir kırtasiyede $4$ defter ile $3$ kalemin toplam fiyatı $165$ lira; bir defter, bir kalemden $15$ lira pahalı.",
                "Bir kalemin fiyatını bulalım.",
                "Kalem $x$ lira olsun; defter $x+15$ lira.",
                "$4(x+15)+3x=165$, yani $7x+60=165$ ve $7x=105$.",
                "$x=15$: kalem $15$ lira, defter $30$ lira. Kontrol: $4 \\cdot 30+3 \\cdot 15=120+45=165$."),
            "Denklem kurmanın adımları ve farklı problem türleri <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısında ayrıntılı olarak ele alınıyor.",
        ]},
        {"baslik": "Sınavda birinci dereceden denklemler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) bu konu parantezli ve kesirli denklemler, çözüm kümesi, parametreli denklemler ve basit denklem sistemleri biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde denklem çözme, neredeyse bütün problem sorularının son adımıdır."),
            "Seçenekli sorularda bulduğun kökü ilk denklemde yerine koymak birkaç saniye sürer ve işaret hatalarının çoğunu yakalar. Kesirli denklemlerde ise çarpmadan önce EKOK'u doğru bulmak, sonraki bütün adımları kolaylaştırır. Parametreli sorularda ise önce katsayının sıfır olduğu durumu ayrıca incelemek, gözden kaçan seçenekleri ortaya çıkarır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Karşıya geçen terimin işaretini değiştirmemek", "$+5$ karşıya $-5$ olarak geçer"],
                ["$3x=12$ ise $x=36$ demek", "İki taraf $3$ e bölünür: $x=4$"],
                ["EKOK ile yalnız kesirli terimleri çarpmak", "Her terim çarpılır"],
                ["$-2(x+1)=-2x+1$", "$-2(x+1)=-2x-2$"],
                ["$0=0$ ı $x=0$ sanmak", "Çözüm kümesi $\\mathbb{R}$"],
                ["Kökü kontrol etmemek", "İlk denklemde yerine koy"],
            ]),
            "Bu hataların çoğu, eşitliğin iki tarafına aynı işlemin uygulandığını unutmaktan doğar. Her adımda \"iki tarafa da ne yaptım?\" diye sormak ve sonunda kökü yerine koymak hataları büyük ölçüde önler.",
        ]},
    ],
    "sss": [
        ("Birinci dereceden denklem nedir?",
         "Bilinmeyenin en büyük üssünün bir olduğu denklemdir. Sadeleştirildiğinde a iks artı b eşittir sıfır biçimine gelir ve a sıfırdan farklıdır."),
        ("Denklem nasıl çözülür?",
         "Paydalar EKOK ile yok edilir, parantezler açılır, bilinmeyenler bir tarafa ve sabitler diğer tarafa toplanır, sonra iki taraf bilinmeyenin katsayısına bölünür."),
        ("Karşıya geçen terimin işareti neden değişir?",
         "Çünkü terimi karşıya geçirmek, iki tarafa o terimin tersini eklemektir. Artı olan terim karşıya eksi, eksi olan terim artı olarak geçer."),
        ("Kesirli denklemde ne yapılır?",
         "İki taraf paydaların EKOK'u ile çarpılır. Bu çarpma eşitliğin iki tarafındaki her terime uygulanır."),
        ("Bir denklemin çözümü olmayabilir mi?",
         "Evet. Sadeleştirmede bilinmeyenler birbirini götürür ve üç eşittir beş gibi bir çelişki kalırsa çözüm kümesi boş kümedir."),
        ("İki bilinmeyenli denklem nasıl çözülür?",
         "Tek bir denklemin sonsuz çözümü vardır; tek çözüm için ikinci bir denklem gerekir. Sistem yok etme ya da yerine koyma yöntemiyle çözülür."),
        ("Bilinmeyen paydada ise nelere dikkat edilir?",
         "Önce paydayı sıfır yapan değerler belirlenir; bunlar kök olamaz. Çözüm sonunda bulunan değer bu yasaklı değerlerden biriyse atılır."),
        ("Denklemi çözdükten sonra neden kontrol etmeliyim?",
         "Bulunan değeri ilk denklemde yerine koymak, işaret ve çarpma hatalarını hemen gösterir. Bilinmeyen paydada ise kontrol, geçersiz kökleri ayıklamanın da yoludur."),
        ("Özdeşlik ile denklem arasındaki fark nedir?",
         "Özdeşlik, bilinmeyenin her değeri için doğru olan eşitliktir. Denklem ise yalnızca bazı değerler için doğrudur. Sadeleştirmede sıfır eşittir sıfır kalıyorsa eşitlik bir özdeşliktir ve her gerçek sayı çözümdür."),
    ],
    "kontrol": [
        "Denklem ile özdeşliği ayırt edebiliyorum.",
        "Bir denklemin derecesini belirleyebiliyorum.",
        "Terazi modeliyle eşitliğin nasıl korunduğunu açıklayabiliyorum.",
        "Karşıya geçen terimin işaretini doğru değiştirebiliyorum.",
        "Parantezli denklemleri işaret hatası yapmadan çözebiliyorum.",
        "Kesirli denklemleri EKOK ile çarparak çözebiliyorum.",
        "Ondalıklı denklemleri tam sayılı hâle getirebiliyorum.",
        "Çözümü olmayan ve sonsuz çözümü olan denklemleri tanıyabiliyorum.",
        "İki bilinmeyenli basit sistemleri yok etme ve yerine koyma ile çözebiliyorum.",
        "Bulduğum kökü ilk denklemde yerine koyarak kontrol edebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["cebirsel-ifadeler-konu-anlatimi-pdf", "esitsizlikler-konu-anlatimi-pdf", "denklem-kurma-problemleri-nasil-cozulur"],
}
