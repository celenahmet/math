# scripts/yazilar/52_sayi_kumeleri.py — Sayilar ve Sayi Kumeleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf",
    "baslik": "Sayılar ve Sayı Kümeleri Konu Anlatımı PDF",
    "aciklama": "Doğal, tam, rasyonel, irrasyonel ve gerçek sayı kümeleri; kapsama ilişkisi, işlemlere göre kapalılık ve sayı doğrusu, çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf",
    "kapak_alt": "Sayılar ve sayı kümeleri konu anlatımı: iç içe geçmiş şeffaf halkalara renkli bilyeleri yerleştirerek kümeler arasındaki kapsama ilişkisini gösteren iki öğrenci",
    "ozet": "Her sayı bir kümeye aittir ve kümeler iç içedir: her doğal sayı bir tam sayıdır, her tam sayı bir rasyonel sayıdır, her rasyonel sayı da bir gerçek sayıdır. Bu yazıda doğal, tam, rasyonel, irrasyonel ve gerçek sayı kümelerini tek tek tanımlıyor, aralarındaki kapsama ilişkisini, hangi kümenin hangi işlemde kapalı olduğunu ve sayı doğrusundaki yerlerini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Sayı kümeleri neden var?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi ve kesir kavramını biliyor olman yeterli.",
                "Tek ve çift, pozitif ve negatif gibi kavramlar için <a href=\"/blog/temel-kavramlar-konu-anlatimi-pdf/\">Temel Kavramlar Konu Anlatımı PDF</a> yazısına göz at."),
            "Sayı kümelerini ezberlemek yerine her birinin <strong>hangi ihtiyaçtan doğduğunu</strong> bilmek, onları karıştırmamanın en kolay yoludur. Her yeni küme, bir öncekinde yapılamayan bir işlemi mümkün kılar:",
            "<ul><li>Saymak için <strong>doğal sayılar</strong> yeter: $0, 1, 2, 3, \\ldots$</li>"
            "<li>$3-5$ işlemi doğal sayılarda yapılamaz; sonucu karşılamak için <strong>tam sayılar</strong> gerekir.</li>"
            "<li>$1 \\div 3$ işlemi tam sayılarda yapılamaz; <strong>rasyonel sayılar</strong> gerekir.</li>"
            "<li>Alanı $2$ olan bir karenin kenarı hiçbir kesirle tam olarak yazılamaz; <strong>irrasyonel sayılar</strong> gerekir.</li>"
            "<li>Rasyonel ve irrasyonel sayılar birlikte sayı doğrusunu boşluksuz doldurur; bu bütüne <strong>gerçek sayılar</strong> denir.</li></ul>",
            hap("Kümeler iç içedir: $\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$.",
                "İrrasyonel sayılar bu zincirin dışındadır: $\\mathbb{Q}$ ile birlikte $\\mathbb{R}$ yi oluşturur."),
        ]},
        {"baslik": "Doğal sayılar ve sayma sayıları", "icerik": [
            "<strong>Doğal sayılar</strong> kümesi $\\mathbb{N}$ ile gösterilir ve $0$ dan başlar:",
            "$$\\mathbb{N}=\\{0,1,2,3,\\ldots\\}$$",
            "$0$ ı dışarıda bırakan kümeye <strong>sayma sayıları</strong> denir: $\\{1,2,3,\\ldots\\}$. Nesneleri sayarken $1$ den başladığımız için bu adı alır. Bu küme bazı kaynaklarda $\\mathbb{N}^{+}$ ya da pozitif doğal sayılar olarak da geçer.",
            "Doğal sayıların en küçüğü vardır ($0$), ama en büyüğü yoktur: hangi doğal sayıyı alırsan al, $1$ ekleyince daha büyüğünü bulursun.",
            dikkat(
                "Doğal sayılar $0$ dan, sayma sayıları $1$ den başlar.",
                "\"En küçük doğal sayı\" sorusunun cevabı $0$, \"en küçük sayma sayısı\" sorusunun cevabı $1$ dir."),
        ]},
        {"baslik": "Tam sayılar", "icerik": [
            "Doğal sayılara negatif sayılar eklenince <strong>tam sayılar</strong> kümesi $\\mathbb{Z}$ elde edilir:",
            "$$\\mathbb{Z}=\\{\\ldots,-3,-2,-1,0,1,2,3,\\ldots\\}$$",
            "Tam sayılar üç parçaya ayrılır: pozitif tam sayılar $\\mathbb{Z}^{+}=\\{1,2,3,\\ldots\\}$, negatif tam sayılar $\\mathbb{Z}^{-}=\\{\\ldots,-3,-2,-1\\}$ ve $0$. Sıfır ne pozitif ne negatiftir; bu yüzden iki kümenin de dışında kalır.",
            "Tam sayıların ne en küçüğü ne de en büyüğü vardır. İki tam sayı arasında ise sonlu sayıda tam sayı bulunur: $3$ ile $4$ arasında hiç tam sayı yoktur.",
            "Her tam sayının bir <strong>zıttı</strong> vardır: $a$ ile $-a$ nın toplamı $0$ dır. $5$ in zıttı $-5$, $-8$ in zıttı $8$ dir. $0$ ın zıttı ise kendisidir. Doğal sayılarda bu özellik yoktur; $3$ ün zıttı olan $-3$ doğal sayı değildir.",
            hap("$\\mathbb{Z}=\\mathbb{Z}^{-} \\cup \\{0\\} \\cup \\mathbb{Z}^{+}$.",
                "$0$ ne $\\mathbb{Z}^{+}$ nın ne de $\\mathbb{Z}^{-}$ nin elemanıdır."),
        ]},
        {"baslik": "Rasyonel sayılar", "icerik": [
            "$a$ ve $b$ tam sayı ve $b \\neq 0$ olmak üzere $\\dfrac{a}{b}$ biçiminde yazılabilen sayılara <strong>rasyonel sayı</strong> denir. Küme $\\mathbb{Q}$ ile gösterilir:",
            "$$\\mathbb{Q}=\\left\\{\\frac{a}{b} : a, b \\in \\mathbb{Z}, b \\neq 0\\right\\}$$",
            "Her tam sayı bir rasyonel sayıdır, çünkü paydasına $1$ yazılabilir: $5=\\dfrac{5}{1}$, $-3=\\dfrac{-3}{1}$. Ondalık sayıların bir kısmı da rasyoneldir:",
            "<ul><li><strong>Sonlu ondalık</strong> sayılar rasyoneldir: $0.75=\\dfrac{3}{4}$.</li>"
            "<li><strong>Devirli ondalık</strong> sayılar, yani bir basamak grubunun sonsuza kadar tekrar ettiği sayılar da rasyoneldir: $0.333\\ldots=\\dfrac{1}{3}$.</li></ul>",
            "Bir rasyonel sayının yazılışı tek değildir: $\\dfrac{1}{2}=\\dfrac{2}{4}=\\dfrac{3}{6}$ gibi sonsuz sayıda denk kesirle gösterilebilir. Pay ile paydanın $1$ den başka ortak böleni kalmadığında kesir <strong>en sade</strong> hâlindedir.",
            "Rasyonel sayıların en önemli özelliği <strong>yoğunluktur</strong>: iki rasyonel sayı ne kadar yakın olursa olsun, aralarında mutlaka başka bir rasyonel sayı vardır. Örneğin iki sayının ortalaması her zaman aralarındadır.",
            ornek(
                "$\\dfrac{1}{3}$ ile $\\dfrac{1}{2}$ sayıları verilsin.",
                "Bu iki sayı arasında bir rasyonel sayı bulalım.",
                "Ortalamalarını alalım: $\\dfrac{1}{2} \\cdot \\left(\\dfrac{1}{3}+\\dfrac{1}{2}\\right)=\\dfrac{1}{2} \\cdot \\dfrac{5}{6}=\\dfrac{5}{12}$.",
                "Kontrol: $\\dfrac{1}{3}=\\dfrac{4}{12}$ ve $\\dfrac{1}{2}=\\dfrac{6}{12}$. $\\dfrac{5}{12}$ tam ortadadır.",
                "Aynı işlemi tekrarlayarak aralarında sonsuz sayıda rasyonel sayı bulunabilir."),
        ]},
        {"baslik": "İrrasyonel sayılar", "icerik": [
            "$\\dfrac{a}{b}$ biçiminde yazılamayan gerçek sayılara <strong>irrasyonel sayı</strong> denir. Ondalık gösterimleri sonsuza kadar gider ve hiçbir basamak grubu düzenli olarak tekrar etmez.",
            "En bilinen örnekler şunlardır: $\\sqrt{2}=1.41421\\ldots$, $\\sqrt{3}=1.73205\\ldots$, $\\pi=3.14159\\ldots$ Tam kare olmayan doğal sayıların karekökleri irrasyoneldir.",
            "Kök işareti görmek sayının irrasyonel olduğunu göstermez. $\\sqrt{9}=3$ ve $\\sqrt{\\dfrac{4}{25}}=\\dfrac{2}{5}$ rasyoneldir; köklerin içi tam karedir.",
            dikkat(
                "$\\pi$ sayısı $\\dfrac{22}{7}$ ye eşit değildir.",
                "$\\dfrac{22}{7}=3.142857\\ldots$ bir rasyonel sayıdır ve $\\pi$ ye yalnızca yakındır. $\\pi$ irrasyoneldir; hiçbir kesre eşit değildir."),
            hap("Tam kare olmayan bir doğal sayının karekökü irrasyoneldir.",
                "$\\pi$ irrasyoneldir; $\\dfrac{22}{7}$ ve $3.14$ onun yalnızca yaklaşık değerleridir."),
            "İrrasyonel sayıların ayrıntılı anlatımı, neden kesirle yazılamadıklarının ispatı ve sıralanmaları için <a href=\"/blog/irrasyonel-sayilar-ve-gercek-sayilar/\">İrrasyonel Sayılar ve Gerçek Sayılar</a> yazısına bakabilirsin.",
        ]},
        {"baslik": "Gerçek sayılar ve kapsama ilişkisi", "icerik": [
            "Rasyonel sayılar ile irrasyonel sayıların birleşimine <strong>gerçek sayılar</strong> denir ve $\\mathbb{R}$ ile gösterilir. İrrasyonel sayılar kümesi çoğu zaman $\\mathbb{I}$ ile gösterilir, ama bu harf standart değildir; bazı kitaplarda $\\mathbb{Q}'$ yazılır.",
            "$$\\mathbb{R}=\\mathbb{Q} \\cup \\mathbb{Q}' \\text{  ve  } \\mathbb{Q} \\cap \\mathbb{Q}'=\\emptyset$$",
            "Bir gerçek sayı ya rasyoneldir ya irrasyoneldir; ikisi birden olamaz ve ikisinin dışında kalamaz. Kapsama ilişkisini iç içe halkalar gibi düşünebilirsin: en içte doğal sayılar, onu saran tam sayılar, onu saran rasyonel sayılar; rasyonellerin yanında ise ayrı bir bölge olarak irrasyoneller. Hepsini saran en dış halka gerçek sayılardır.",
            tablo(["Sayı", "N", "Z", "Q", "Q'", "R"], [
                ["$7$", "Evet", "Evet", "Evet", "Hayır", "Evet"],
                ["$-4$", "Hayır", "Evet", "Evet", "Hayır", "Evet"],
                ["$\\dfrac{2}{3}$", "Hayır", "Hayır", "Evet", "Hayır", "Evet"],
                ["$0.25$", "Hayır", "Hayır", "Evet", "Hayır", "Evet"],
                ["$\\sqrt{5}$", "Hayır", "Hayır", "Hayır", "Evet", "Evet"],
                ["$\\pi$", "Hayır", "Hayır", "Hayır", "Evet", "Evet"],
            ]),
            ornek(
                "$A=\\left\\{-2, 0, \\dfrac{1}{2}, \\sqrt{4}, \\sqrt{5}, \\pi, 0.333\\ldots, 7\\right\\}$ kümesi verilsin.",
                "$A$ nın kaç elemanı doğal sayı, tam sayı, rasyonel sayı ve irrasyonel sayıdır?",
                "Önce görünüşü yanıltan elemanları sadeleştirelim: $\\sqrt{4}=2$ ve $0.333\\ldots=\\dfrac{1}{3}$.",
                "Doğal sayılar: $0$, $2$, $7$; toplam $3$ tane.",
                "Tam sayılar: $-2$, $0$, $2$, $7$; toplam $4$ tane.",
                "Rasyonel sayılar: $-2$, $0$, $\\dfrac{1}{2}$, $2$, $\\dfrac{1}{3}$, $7$; toplam $6$ tane.",
                "İrrasyonel sayılar: $\\sqrt{5}$ ve $\\pi$; toplam $2$ tane. Sekiz elemanın hepsi gerçek sayıdır."),
        ]},
        {"baslik": "İşlemlere göre kapalılık", "icerik": [
            "Bir kümeden alınan <strong>her</strong> iki elemanla bir işlem yapıldığında sonuç yine o kümede kalıyorsa, küme o işleme göre <strong>kapalıdır</strong>. Kapalı olmadığını göstermek için tek bir karşı örnek yeter.",
            tablo(["Küme", "Toplama", "Çıkarma", "Çarpma", "Bölme"], [
                ["$\\mathbb{N}$", "Kapalı", "Değil", "Kapalı", "Değil"],
                ["$\\mathbb{Z}$", "Kapalı", "Kapalı", "Kapalı", "Değil"],
                ["$\\mathbb{Q}$", "Kapalı", "Kapalı", "Kapalı", "Kapalı*"],
                ["$\\mathbb{Q}'$", "Değil", "Değil", "Değil", "Değil"],
                ["$\\mathbb{R}$", "Kapalı", "Kapalı", "Kapalı", "Kapalı*"],
            ]),
            "Yıldız işaretli bölmelerde sıfıra bölme hariç tutulur; sıfıra bölme hiçbir kümede tanımlı değildir.",
            "Tablodaki \"Değil\" satırlarının karşı örnekleri şunlardır: doğal sayılarda $3-5=-2$ ve $1 \\div 2=\\dfrac{1}{2}$ kümenin dışına çıkar. Tam sayılarda $1 \\div 2$ yine dışarıda kalır. İrrasyonel sayılarda $\\sqrt{2}+(-\\sqrt{2})=0$, $\\sqrt{2}-\\sqrt{2}=0$, $\\sqrt{2} \\cdot \\sqrt{2}=2$ ve $\\sqrt{2} \\div \\sqrt{2}=1$ sonuçlarının hepsi rasyoneldir.",
            hap("Kapalı olmadığını göstermek için <strong>tek bir</strong> karşı örnek yeter.",
                "İrrasyonel sayılar dört işlemin hiçbirinde kapalı değildir: $\\sqrt{2} \\cdot \\sqrt{2}=2$."),
            ornek(
                "$a$ ve $b$ birer irrasyonel sayı olsun.",
                "$a \\cdot b$ çarpımının rasyonel olduğu bir örnek ve irrasyonel olduğu bir örnek verelim.",
                "$a=\\sqrt{2}$ ve $b=\\sqrt{8}$ alalım: $a \\cdot b=\\sqrt{16}=4$. Sonuç rasyonel.",
                "$a=\\sqrt{2}$ ve $b=\\sqrt{3}$ alalım: $a \\cdot b=\\sqrt{6}$. Sonuç irrasyonel.",
                "İki irrasyonel sayının çarpımı için genel bir kural yoktur; her durum ayrıca incelenir."),
            dikkat(
                "İrrasyonel sayıların kapalı olmaması, işlem sonucunun <strong>her zaman</strong> rasyonel çıktığı anlamına gelmez.",
                "$\\sqrt{2}+\\sqrt{3}$ irrasyoneldir. Kapalı olmamak yalnızca kümenin dışına çıkan <strong>en az bir</strong> örnek olduğunu söyler."),
        ]},
        {"baslik": "Sayı doğrusu", "icerik": [
            "Her gerçek sayı sayı doğrusu üzerinde tek bir noktaya karşılık gelir ve doğrunun her noktası da bir gerçek sayıdır. Sağa gidildikçe sayılar büyür, sola gidildikçe küçülür. Bu yüzden $-7$, $-2$ nin solundadır ve $-7<-2$ dir: negatif sayılarda sıfırdan uzaklaştıkça sayı küçülür, mutlak değeri büyük olan daha küçüktür.",
            "Kümeler sayı doğrusunda farklı görünür. Doğal ve tam sayılar aralıklı noktalardır; aralarında boşluk vardır. Rasyonel sayılar her aralığa sıkışmıştır ama doğruyu tek başına dolduramaz: $\\sqrt{2}$ nin bulunduğu nokta rasyonel sayılarda boş kalır. İrrasyonellerle birlikte doğru boşluksuz dolar.",
            ornek(
                "$-2.5$ ile $3$ arasındaki (uçlar hariç) tam sayıları düşünelim.",
                "Bu aralıkta kaç tam sayı vardır?",
                "$-2.5$ ten büyük en küçük tam sayı $-2$ dir. $3$ hariç olduğu için en büyük tam sayı $2$ dir.",
                "Tam sayılar: $-2$, $-1$, $0$, $1$, $2$. Toplam $5$ tane.",
                "Aynı aralıkta rasyonel ve irrasyonel sayıların ise sonsuz sayıda olduğunu unutma."),
            hap("Asansör paneli dikey bir sayı doğrusu gibidir: zemin kat $0$, bodrum katlar $-1$ ve $-2$, üst katlar pozitif sayılarla gösterilir.", "Asansör $-2$ den $3$ e çıkarken $3-(-2)=5$ kat yol alır.", gunluk=True),
        ]},
        {"baslik": "Bir sayının kümesine karar verme", "icerik": [
            "Bir sayının hangi kümelere ait olduğunu bulmak için şu sırayı izle:",
            "<ol><li><strong>Sadeleştir.</strong> Kökleri, kesirleri ve ondalıkları en sade hâline getir: $\\sqrt{16}=4$, $\\dfrac{12}{4}=3$.</li>"
            "<li><strong>Tam sayı mı?</strong> Sadeleşmiş hâli bir tam sayıysa $\\mathbb{Z}$ dedir. Ayrıca $0$ ya da pozitifse $\\mathbb{N}$ dedir.</li>"
            "<li><strong>Kesir olarak yazılabiliyor mu?</strong> İki tam sayının bölümü olarak yazılabiliyorsa, ya da ondalık gösterimi sonlu veya devirliyse $\\mathbb{Q}$ dadır.</li>"
            "<li><strong>Hiçbiri değilse</strong> sayı irrasyoneldir.</li></ol>",
            "Bir sayı bir kümedeyse onu kapsayan bütün kümelerde de vardır. $4$ doğal sayıdır; öyleyse tam, rasyonel ve gerçek sayıdır da. Bu yüzden soruda \"en dar küme\" soruluyorsa zincirin en içindeki kümeyi söylemelisin.",
            hap("Önce sadeleştir, sonra zincirin en içinden dışına doğru kontrol et: $\\mathbb{N}$, $\\mathbb{Z}$, $\\mathbb{Q}$.",
                "Hiçbirine girmeyen gerçek sayı irrasyoneldir."),
        ]},
        {"baslik": "Pozitif, negatif ve negatif olmayan", "icerik": [
            "Kümelerin işaretli parçaları üst işaretle gösterilir: $\\mathbb{Z}^{+}$, $\\mathbb{Q}^{-}$, $\\mathbb{R}^{+}$ gibi. Artı işareti sıfırdan büyükleri, eksi işareti sıfırdan küçükleri seçer. Sıfır hiçbirine girmez.",
            "Soru metinlerinde bu ayrım bazen sözle yapılır ve tek kelime cevabı değiştirir:",
            "<ul><li><strong>Pozitif</strong>: sıfırdan büyük, yani $x>0$.</li><li><strong>Negatif olmayan</strong>: sıfır ya da sıfırdan büyük, yani $x \\geq 0$.</li><li><strong>Negatif</strong>: $x<0$. <strong>Pozitif olmayan</strong>: $x \\leq 0$.</li></ul>",
            dikkat(
                "\"Negatif olmayan tam sayı\" ile \"pozitif tam sayı\" aynı küme değildir.",
                "Negatif olmayan tam sayılar $\\{0,1,2,\\ldots\\}$ yani doğal sayılardır. Pozitif tam sayılar ise $\\{1,2,3,\\ldots\\}$ tür. Fark yalnızca $0$ dır, ama bir sayma sorusunda cevabı bir artırır ya da azaltır."),
        ]},
        {"baslik": "Kümeler arası işlemler", "icerik": [
            "Sayı kümeleri de birer küme olduğu için birleşim, kesişim ve fark işlemleri onlara da uygulanır. Kapsama zincirini bilen biri bu soruları çizim yapmadan cevaplar.",
            "<ul><li>$\\mathbb{N} \\cap \\mathbb{Z}=\\mathbb{N}$, çünkü $\\mathbb{N}$ zaten $\\mathbb{Z}$ nin içindedir.</li>"
            "<li>$\\mathbb{Z} \\cup \\mathbb{Q}=\\mathbb{Q}$, çünkü büyük küme küçüğü içine alır.</li>"
            "<li>$\\mathbb{Z}-\\mathbb{N}=\\mathbb{Z}^{-}$: tam sayılardan doğal sayılar çıkınca geriye negatifler kalır.</li>"
            "<li>$\\mathbb{R}-\\mathbb{Q}=\\mathbb{Q}'$: gerçek sayılardan rasyoneller çıkınca geriye irrasyoneller kalır.</li>"
            "<li>$\\mathbb{Q} \\cap \\mathbb{Q}'=\\emptyset$: hiçbir sayı hem rasyonel hem irrasyonel olamaz.</li></ul>",
            hap("İç içe iki kümenin kesişimi <strong>küçük</strong>, birleşimi <strong>büyük</strong> kümedir.",
                "$\\mathbb{Q}$ ile $\\mathbb{Q}'$ ayrık kümelerdir; birleşimleri $\\mathbb{R}$ dir."),
        ]},
        {"baslik": "İki sayı arasındaki tam sayıları sayma", "icerik": [
            "Sayı kümeleriyle ilgili bir soru tipi, iki gerçek sayı arasında kaç tam sayı olduğunu sormaktır. Yöntem basittir: alt sınırdan büyük ilk tam sayıyı ve üst sınırdan küçük son tam sayıyı bul, sonra aradakileri say.",
            "Aralıktaki tam sayılar ardışık olduğu için sayıları $\\text{son}-\\text{ilk}+1$ dir.",
            ornek(
                "$\\sqrt{10}$ ile $\\sqrt{50}$ sayıları verilsin.",
                "Bu iki sayı arasında kaç tam sayı vardır?",
                "$3^2=9<10<16=4^2$ olduğundan $3<\\sqrt{10}<4$. Aralıktaki ilk tam sayı $4$ tür.",
                "$7^2=49<50<64=8^2$ olduğundan $7<\\sqrt{50}<8$. Aralıktaki son tam sayı $7$ dir.",
                "Tam sayılar: $4$, $5$, $6$, $7$. Toplam $7-4+1=4$ tane."),
        ]},
        {"baslik": "Sınavda sayı kümeleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) sayı kümeleri bir listenin elemanlarını sınıflandırma, \"aşağıdakilerden hangisi rasyonel değildir?\" ya da kapalılık biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde kümeler problemin şartı olarak da karşına çıkabilir: \"$a$ bir pozitif tam sayı\", \"$x$ bir doğal sayı\" gibi. Bu şartı doğru okumak cevabı doğrudan belirler."),
            "Sınıflandırma sorularında dikkat edilecek nokta, sayıyı sadeleştirmeden karar vermemektir. $\\sqrt{16}$, $\\dfrac{12}{4}$ ve $0.999\\ldots$ gibi ifadeler ilk bakışta olduğundan farklı görünür; önce sadeleştir, sonra kümeye yerleştir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$0$ ı sayma sayısı saymak", "Sayma sayıları $1$ den başlar"],
                ["$0$ ı $\\mathbb{Z}^{+}$ ya koymak", "$0$ işaretsizdir"],
                ["Kök gördüğü her sayıyı irrasyonel sanmak", "$\\sqrt{9}=3$ rasyonel"],
                ["$\\pi=\\dfrac{22}{7}$ sanmak", "Yalnızca yaklaşık değer"],
                ["Devirli ondalığı irrasyonel sanmak", "Devirli ondalık rasyoneldir"],
                ["Kapalılığı birkaç örnekle kanıtlamak", "Genel gösterim gerekir"],
            ]),
            "Bu hataların ortak noktası sayının <strong>görünüşüne</strong> bakarak karar vermektir. Bir sayının hangi kümeye ait olduğunu, sadeleştirilmiş hâline bakarak söyle.",
        ]},
    ],
    "sss": [
        ("Sayı kümeleri nelerdir?",
         "Temel sayı kümeleri doğal sayılar, tam sayılar, rasyonel sayılar, irrasyonel sayılar ve gerçek sayılardır. Doğal sayılar tam sayıların, tam sayılar rasyonel sayıların, rasyonel sayılar da gerçek sayıların alt kümesidir. İrrasyonel sayılar rasyonel sayılarla birlikte gerçek sayıları oluşturur."),
        ("Sıfır hangi sayı kümelerinin elemanıdır?",
         "Sıfır bir doğal sayı, tam sayı, rasyonel sayı ve gerçek sayıdır. Sayma sayısı değildir ve ne pozitif ne negatif tam sayılar kümesine girer."),
        ("Her tam sayı rasyonel midir?",
         "Evet. Her tam sayı paydası 1 olan bir kesir olarak yazılabilir; bu yüzden her tam sayı bir rasyonel sayıdır."),
        ("Devirli ondalık sayılar rasyonel midir?",
         "Evet. Bir basamak grubu sonsuza kadar düzenli olarak tekrar eden her ondalık sayı iki tam sayının bölümü olarak yazılabilir. Örneğin 0,333... sayısı üçte bire eşittir."),
        ("Pi sayısı rasyonel midir?",
         "Hayır. Pi irrasyoneldir. 22 bölü 7 ve 3,14 yalnızca pi nin yaklaşık değerleridir; pi hiçbir kesre tam olarak eşit değildir."),
        ("Bir küme bir işleme göre kapalı ne demektir?",
         "Kümeden alınan her iki elemanla işlem yapıldığında sonuç yine aynı kümede kalıyorsa, küme o işleme göre kapalıdır. Örneğin tam sayılar çarpmaya göre kapalıdır ama bölmeye göre kapalı değildir."),
        ("Negatif olmayan tam sayılar hangi kümedir?",
         "Negatif olmayan tam sayılar sıfır ve pozitif tam sayılardan oluşur; yani doğal sayılar kümesidir. Pozitif tam sayılardan farkı sıfırı da içermesidir."),
    ],
    "kontrol": [
        "Beş temel sayı kümesini hangi ihtiyaçtan doğduklarıyla birlikte sayabiliyorum.",
        "$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$ zincirini açıklayabiliyorum.",
        "Doğal sayılar ile sayma sayıları arasındaki farkı biliyorum.",
        "$0$ ın hangi kümelere ait olduğunu söyleyebiliyorum.",
        "Sonlu ve devirli ondalık sayıların rasyonel olduğunu biliyorum.",
        "Kök içeren bir sayının rasyonel mi irrasyonel mi olduğuna sadeleştirerek karar veriyorum.",
        "Bir listenin elemanlarını sayı kümelerine göre sınıflandırabiliyorum.",
        "Bir kümenin bir işleme göre kapalı olmadığını karşı örnekle gösterebiliyorum.",
        "İki rasyonel sayı arasında başka bir rasyonel sayı bulabiliyorum.",
        "Sayı doğrusu üzerinde bir aralıktaki tam sayıları sayabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["temel-kavramlar-konu-anlatimi-pdf", "dogal-sayilar-ve-tam-sayilar", "irrasyonel-sayilar-ve-gercek-sayilar"],
}
