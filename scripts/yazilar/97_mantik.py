# scripts/yazilar/97_mantik.py — Mantik (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "mantik-konu-anlatimi-pdf",
    "baslik": "Mantık Konu Anlatımı PDF",
    "aciklama": "Önerme nedir? Doğruluk değeri, değil, ve, veya, ya da, koşullu ve iki yönlü koşullu önerme, doğruluk tablosu, De Morgan, totoloji ve niceleyiciler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "kumeler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "mantik-konu-anlatimi-pdf",
    "kapak_alt": "Mantık: koşullu yollardan oluşan ahşap bir düzenekte topların hareketini inceleyen öğrenci",
    "ozet": "Mantık, doğru ya da yanlış olduğu kesin olarak söylenebilen ifadelerle ve bu ifadelerin birleştirilmesiyle ilgilenir. Matematikte her tanım, her teorem ve her ispat mantığın diliyle kurulur. Bu yazıda önermeyi ve doğruluk değerini, değil, ve, veya, ya da bağlaçlarını, koşullu ve iki yönlü koşullu önermeleri, doğruluk tablosu kurmayı, De Morgan kurallarını, totoloji ve çelişkiyi, açık önermeleri ve niceleyicileri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Önerme nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için küme işlemlerini biliyor olman yeterli; mantık bağlaçları küme işlemleriyle aynı yapıdadır.",
                "Küme işlemleri için <a href=\"/blog/kumeler-konu-anlatimi-pdf/\">Kümeler Konu Anlatımı PDF</a> yazısına göz at."),
            "Doğru ya da yanlış olduğu kesin olarak söylenebilen ifadelere <strong>önerme</strong> denir. Önermeler genellikle $p$, $q$, $r$ gibi küçük harflerle gösterilir.",
            tablo(["İfade", "Önerme mi?"], [
                ["$7$ bir asal sayıdır.", "Evet, doğru"],
                ["$2+3=6$", "Evet, yanlış"],
                ["Bu soru çok zor.", "Hayır, kişiye göre değişir"],
                ["Kapıyı kapat.", "Hayır, doğru ya da yanlış değildir"],
            ]),
            "Bir ifadenin önerme olması için doğru olması gerekmez; doğru mu yanlış mı olduğunun kesin olarak belirlenebilmesi yeterlidir. Soru, emir ve kişisel değerlendirme içeren cümleler önerme değildir.",
        ]},
        {"baslik": "Doğruluk değeri", "icerik": [
            "Bir önermenin doğru ya da yanlış olmasına <strong>doğruluk değeri</strong> denir. Doğru önermenin doğruluk değeri $1$, yanlış önermenin doğruluk değeri $0$ ile gösterilir. Bazı kaynaklarda bunların yerine D ve Y harfleri kullanılır.",
            "Doğruluk değerleri aynı olan iki önermeye <strong>denk önermeler</strong> denir ve aralarına $\\equiv$ işareti konur. \"$7$ bir asal sayıdır\" ile \"$9$ bir tam karedir\" önermeleri, konuları farklı olsa da ikisi de doğru olduğu için denktir.",
            hap("Doğru önerme: $1$. Yanlış önerme: $0$.",
                "Denk önermelerin doğruluk değerleri aynıdır."),
        ]},
        {"baslik": "Bir önermenin değili", "icerik": [
            "Bir önermenin hükmünün tersine çevrilmesiyle elde edilen önermeye o önermenin <strong>değili</strong> ya da olumsuzu denir. $p$ önermesinin değili $p'$ ile gösterilir. Önerme doğruysa değili yanlış, önerme yanlışsa değili doğrudur.",
            tablo(["$p$", "$p'$"], [
                ["$1$", "$0$"],
                ["$0$", "$1$"],
            ]),
            ornek(
                "$p$: \"$12$ bir çift sayıdır.\" önermesi verilsin.",
                "Önermenin değilini yazalım ve doğruluk değerlerini bulalım.",
                "$p'$: \"$12$ bir çift sayı değildir.\"",
                "$p$ doğrudur, bu yüzden $p'$ yanlıştır."),
            "Bir önermenin değilinin değili, önermenin kendisine denktir: $(p')' \\equiv p$. \"Yağmur yağmıyor değil\" demek, \"yağmur yağıyor\" demektir.",
        ]},
        {"baslik": "Ve bağlacı", "icerik": [
            "İki önermenin \"ve\" bağlacıyla birleştirilmesiyle elde edilen önerme $p \\wedge q$ ile gösterilir. Bu önerme yalnızca iki önerme de doğruysa doğrudur; önermelerden biri bile yanlışsa yanlıştır.",
            tablo(["$p$", "$q$", "$p \\wedge q$"], [
                ["$1$", "$1$", "$1$"],
                ["$1$", "$0$", "$0$"],
                ["$0$", "$1$", "$0$"],
                ["$0$", "$0$", "$0$"],
            ]),
            ornek(
                "$p$: \"$5$ bir asal sayıdır.\" ve $q$: \"$5$ bir çift sayıdır.\" önermeleri verilsin.",
                "\"Ve\" ile bağlanan önermenin doğruluk değerini bulalım.",
                "$p$ doğru, $q$ yanlıştır.",
                "Biri yanlış olduğu için birleşik önerme yanlıştır: $1 \\wedge 0 \\equiv 0$."),
        ]},
        {"baslik": "Veya bağlacı", "icerik": [
            "İki önermenin \"veya\" bağlacıyla birleştirilmesiyle elde edilen önerme $p \\vee q$ ile gösterilir. Bu önerme, önermelerden en az biri doğruysa doğrudur; yalnızca ikisi de yanlışsa yanlıştır.",
            tablo(["$p$", "$q$", "$p \\vee q$"], [
                ["$1$", "$1$", "$1$"],
                ["$1$", "$0$", "$1$"],
                ["$0$", "$1$", "$1$"],
                ["$0$", "$0$", "$0$"],
            ]),
            "Matematikteki \"veya\", günlük dildekinden biraz farklıdır: iki önermenin birlikte doğru olması da kabul edilir. \"Sayı $2$ ile veya $3$ ile bölünür\" önermesi, $6$ gibi iki koşulu da sağlayan sayılar için de doğrudur.",
        ]},
        {"baslik": "Ya da bağlacı", "icerik": [
            "\"Ya da\" bağlacı, iki önermeden yalnızca birinin doğru olmasını ister ve $p \\veebar q$ ile gösterilir. Önermelerin doğruluk değerleri farklıysa birleşik önerme doğru, aynıysa yanlıştır.",
            tablo(["$p$", "$q$", "$p \\veebar q$"], [
                ["$1$", "$1$", "$0$"],
                ["$1$", "$0$", "$1$"],
                ["$0$", "$1$", "$1$"],
                ["$0$", "$0$", "$0$"],
            ]),
            dikkat(
                "\"Veya\" ile \"ya da\" bağlaçlarını karıştırmak.",
                "İki bağlaç yalnızca ilk satırda ayrılır: iki önerme de doğruysa \"veya\" doğru, \"ya da\" yanlıştır. Soruda hangi bağlacın kullanıldığına dikkat et."),
        ]},
        {"baslik": "Bağlaçların özellikleri", "icerik": [
            "Ve ile veya bağlaçları, kümelerdeki kesişim ve birleşim gibi değişme, birleşme ve dağılma özelliklerine sahiptir. Aşağıdaki denklikler doğruluk tablosuyla kolayca kontrol edilebilir.",
            tablo(["Özellik", "Ve", "Veya"], [
                ["Değişme", "$p \\wedge q \\equiv q \\wedge p$", "$p \\vee q \\equiv q \\vee p$"],
                ["Tek başına", "$p \\wedge p \\equiv p$", "$p \\vee p \\equiv p$"],
                ["Doğru ile", "$p \\wedge 1 \\equiv p$", "$p \\vee 1 \\equiv 1$"],
                ["Yanlış ile", "$p \\wedge 0 \\equiv 0$", "$p \\vee 0 \\equiv p$"],
                ["Değili ile", "$p \\wedge p' \\equiv 0$", "$p \\vee p' \\equiv 1$"],
            ]),
            "Dağılma özelliği de iki yönlüdür: $p \\wedge (q \\vee r) \\equiv (p \\wedge q) \\vee (p \\wedge r)$ ve $p \\vee (q \\wedge r) \\equiv (p \\vee q) \\wedge (p \\vee r)$. Sayılarda toplama çarpma üzerine dağılmaz; mantıkta ise iki bağlaç da birbiri üzerine dağılır.",
        ]},
        {"baslik": "De Morgan kuralları", "icerik": [
            "Birleşik bir önermenin değili alınırken bağlaç değişir ve her önermenin değili alınır. Bu kurallara De Morgan kuralları denir:",
            "$$(p \\wedge q)' \\equiv p' \\vee q'$$",
            "$$(p \\vee q)' \\equiv p' \\wedge q'$$",
            ornek(
                "\"Ali hem matematik hem fizik sınavını geçti.\" önermesi verilsin.",
                "Önermenin değilini yazalım.",
                "Önerme \"ve\" bağlacıyla kurulmuştur: matematik ve fizik.",
                "Değili: \"Ali matematik sınavını veya fizik sınavını geçemedi.\" Yani en az birini geçemedi."),
            "Kümelerdeki De Morgan kuralları da aynı yapıdadır: birleşimin tümleyeni tümleyenlerin kesişimi, kesişimin tümleyeni tümleyenlerin birleşimidir.",
            hap("$(p \\wedge q)' \\equiv p' \\vee q'$ ve $(p \\vee q)' \\equiv p' \\wedge q'$ olur; değil alınınca bağlaç değişir."),
        ]},
        {"baslik": "Koşullu önerme", "icerik": [
            "\"$p$ ise $q$\" biçimindeki önermeye <strong>koşullu önerme</strong> denir ve $p \\Rightarrow q$ ile gösterilir. $p$ önermesine hipotez, $q$ önermesine hüküm denir. Koşullu önerme yalnızca hipotez doğru ve hüküm yanlış olduğunda yanlıştır.",
            tablo(["$p$", "$q$", "$p \\Rightarrow q$"], [
                ["$1$", "$1$", "$1$"],
                ["$1$", "$0$", "$0$"],
                ["$0$", "$1$", "$1$"],
                ["$0$", "$0$", "$1$"],
            ]),
            "Bunu bir sözle düşünmek kolaylaştırır: \"Sınavı geçersen sana bisiklet alacağım.\" Söz yalnızca sınav geçildiği hâlde bisiklet alınmazsa bozulmuş olur. Sınav geçilmediyse, bisiklet alınsa da alınmasa da söz bozulmamıştır.",
            dikkat(
                "Hipotez yanlışken koşullu önermeyi yanlış saymak.",
                "Hipotez yanlışsa koşullu önerme hükümden bağımsız olarak doğrudur. Tablonun son iki satırı bu yüzden $1$ dir."),
            hap("\"Yağmur yağarsa maç ertelenir\" sözü, yağmur yağmadığı hâlde maç ertelenirse çiğnenmiş olmaz.", "Söz yalnızca yağmur yağdığı hâlde maç oynanırsa yanlış çıkar.", gunluk=True),
        ]},
        {"baslik": "Koşullu önermenin denkliği", "icerik": [
            "Koşullu önerme, değil ve veya bağlaçlarıyla da yazılabilir. Bu denklik, koşullu önermelerin bulunduğu ifadeleri sadeleştirmenin anahtarıdır:",
            "$$p \\Rightarrow q \\equiv p' \\vee q$$",
            "Doğruluk tablosunda $p' \\vee q$ önermesi yalnızca $p$ doğru ve $q$ yanlış olduğunda yanlıştır; bu, koşullu önermenin yanlış olduğu tek satırdır. Bu yüzden iki önerme denktir. Buradan koşullu önermenin değili de bulunur: $(p \\Rightarrow q)' \\equiv p \\wedge q'$.",
        ]},
        {"baslik": "Karşıt, ters ve karşıt ters", "icerik": [
            "Bir koşullu önermeden yer değiştirme ve değil alma yoluyla üç yeni önerme elde edilir.",
            tablo(["Ad", "Biçim"], [
                ["Koşullu önerme", "$p \\Rightarrow q$"],
                ["Karşıtı", "$q \\Rightarrow p$"],
                ["Tersi", "$p' \\Rightarrow q'$"],
                ["Karşıt tersi", "$q' \\Rightarrow p'$"],
            ]),
            "Bir koşullu önerme, karşıt tersine her zaman denktir: $p \\Rightarrow q \\equiv q' \\Rightarrow p'$. Karşıtı ve tersi ise koşullu önermeye denk olmak zorunda değildir; ama karşıt ile ters birbirine denktir.",
            ornek(
                "\"Bir sayı $4$ ile bölünüyorsa çifttir.\" önermesi verilsin.",
                "Karşıtını ve karşıt tersini yazıp doğruluklarını inceleyelim.",
                "Karşıtı: \"Bir sayı çiftse $4$ ile bölünür.\" Yanlıştır; $6$ çifttir ama $4$ ile bölünmez.",
                "Karşıt tersi: \"Bir sayı çift değilse $4$ ile bölünmez.\" Doğrudur, tıpkı önermenin kendisi gibi."),
            hap("Koşullu önerme karşıt tersine denktir: $p \\Rightarrow q \\equiv q' \\Rightarrow p'$ olur.", "Karşıtı ve tersi ise koşullu önermeye denk değildir."),
        ]},
        {"baslik": "İki yönlü koşullu önerme", "icerik": [
            "\"$p$ ancak ve ancak $q$\" biçimindeki önermeye <strong>iki yönlü koşullu önerme</strong> denir ve $p \\Leftrightarrow q$ ile gösterilir. İki önermenin doğruluk değerleri aynıysa doğru, farklıysa yanlıştır.",
            tablo(["$p$", "$q$", "$p \\Leftrightarrow q$"], [
                ["$1$", "$1$", "$1$"],
                ["$1$", "$0$", "$0$"],
                ["$0$", "$1$", "$0$"],
                ["$0$", "$0$", "$1$"],
            ]),
            "İki yönlü koşullu önerme, iki koşullu önermenin \"ve\" ile bağlanmasıdır: $p \\Leftrightarrow q \\equiv (p \\Rightarrow q) \\wedge (q \\Rightarrow p)$. Tablosunun \"ya da\" bağlacının tablosunun tam değili olduğuna da dikkat et.",
        ]},
        {"baslik": "Doğruluk tablosu kurmak", "icerik": [
            "Birleşik bir önermenin bütün durumlardaki doğruluk değeri, doğruluk tablosuyla bulunur. $n$ farklı önerme varsa her biri iki değer alabildiği için tabloda $2^n$ satır bulunur: iki önermede $4$, üç önermede $8$ satır.",
            ornek(
                "$(p \\wedge q) \\Rightarrow p$ önermesi verilsin.",
                "Doğruluk tablosunu kurup sonucu yorumlayalım.",
                "$p \\wedge q$ yalnızca ilk satırda doğrudur; o satırda $p$ de doğrudur ve koşullu önerme doğrudur.",
                "Diğer üç satırda hipotez yanlış olduğu için koşullu önerme yine doğrudur.",
                "Önerme bütün satırlarda doğrudur."),
            "Tablo kurarken sütunları içten dışa doğru sırala: önce önermeler, sonra parantez içindeki bağlaçlar, en son dıştaki bağlaç. Bu sıra işlem hatasını büyük ölçüde önler.",
            hap("$n$ farklı önermeyle kurulan doğruluk tablosunda $2^n$ satır vardır."),
        ]},
        {"baslik": "Totoloji ve çelişki", "icerik": [
            "Doğruluk tablosunun bütün satırlarında doğru olan önermeye <strong>totoloji</strong>, bütün satırlarında yanlış olan önermeye <strong>çelişki</strong> denir. Bir önermenin totoloji olduğunu göstermek için tablo kurmak ya da denkliklerle $1$ e indirmek yeterlidir.",
            tablo(["Önerme", "Tür"], [
                ["$p \\vee p'$", "Totoloji"],
                ["$p \\wedge p'$", "Çelişki"],
                ["$(p \\wedge q) \\Rightarrow p$", "Totoloji"],
                ["$p \\Rightarrow (p \\vee q)$", "Totoloji"],
                ["$p \\wedge q$", "İkisi de değil"],
            ]),
            "Bir önerme ne her zaman doğru ne her zaman yanlışsa, doğruluğu önermelerin değerlerine bağlıdır. Sınav sorularının çoğu, verilen bir önermenin bu üç türden hangisine girdiğini sorar.",
        ]},
        {"baslik": "Denkliklerle sadeleştirme", "icerik": [
            "Uzun bir birleşik önerme, doğruluk tablosu kurmadan denklikler art arda uygulanarak sadeleştirilebilir.",
            ornek(
                "$(p \\wedge q) \\vee (p \\wedge q')$ önermesi verilsin.",
                "Önermeyi en sade biçimine getirelim.",
                "Dağılma özelliğiyle $p$ ortak paranteze alınır: $p \\wedge (q \\vee q')$.",
                "$q \\vee q' \\equiv 1$ olduğu için önerme $p \\wedge 1$ olur.",
                "$p \\wedge 1 \\equiv p$."),
            ornek(
                "$(p \\Rightarrow q) \\wedge p$ önermesi verilsin.",
                "Önermeyi sadeleştirelim.",
                "Koşullu önermenin denkliğiyle: $(p' \\vee q) \\wedge p$.",
                "Dağılma: $(p' \\wedge p) \\vee (q \\wedge p) \\equiv 0 \\vee (q \\wedge p)$.",
                "Sonuç: $p \\wedge q$."),
        ]},
        {"baslik": "Doğruluk değerinden geriye gitmek", "icerik": [
            "Bazı sorular birleşik bir önermenin doğruluk değerini verir ve bileşenlerin değerlerini sorar. Bu sorularda en çok bilgi veren bağlaçtan başlanır: yanlış bir koşullu önerme, yanlış bir \"veya\" ya da doğru bir \"ve\" önermesi bileşenlerin değerlerini kesin olarak belirler.",
            ornek(
                "$p \\Rightarrow (q \\vee r)$ önermesinin yanlış olduğu biliniyor.",
                "$p$, $q$ ve $r$ önermelerinin doğruluk değerlerini bulalım.",
                "Koşullu önerme yalnızca hipotez doğru, hüküm yanlışken yanlıştır: $p \\equiv 1$ ve $q \\vee r \\equiv 0$.",
                "\"Veya\" önermesi yalnızca ikisi de yanlışken yanlıştır: $q \\equiv 0$ ve $r \\equiv 0$."),
        ]},
        {"baslik": "Açık önermeler ve doğruluk kümesi", "icerik": [
            "İçinde değişken bulunan ve değişkenin değerine göre doğru ya da yanlış olan ifadelere <strong>açık önerme</strong> denir. $x+2<5$ ifadesi tek başına bir önerme değildir; $x$ yerine bir sayı konunca önerme olur. Açık önermeyi doğru yapan değerlerin kümesine <strong>doğruluk kümesi</strong> denir.",
            ornek(
                "Doğal sayılarda $p(x)$: $x+2<5$ açık önermesi verilsin.",
                "Doğruluk kümesini bulalım.",
                "$x<3$ olmalıdır.",
                "Doğruluk kümesi: $\\{0, 1, 2\\}$."),
            "Açık önermeler kümelerle mantık arasındaki köprüdür. İki açık önermenin \"ve\" ile bağlanmasının doğruluk kümesi, doğruluk kümelerinin kesişimidir; \"veya\" ile bağlanmasınınki ise birleşimidir.",
        ]},
        {"baslik": "Niceleyiciler", "icerik": [
            "\"Her\" ve \"bazı\" sözcükleri açık önermeleri önermeye dönüştürür. \"Her\" anlamına gelen <strong>evrensel niceleyici</strong> $\\forall$, \"en az bir\" anlamına gelen <strong>varlıksal niceleyici</strong> $\\exists$ ile gösterilir.",
            tablo(["Önerme", "Okunuşu", "Doğruluk"], [
                ["$\\forall x \\in \\mathbb{N}$, $x+1>x$", "Her doğal sayı için $x+1>x$", "Doğru"],
                ["$\\exists x \\in \\mathbb{N}$, $x+3=1$", "$x+3=1$ olan bir doğal sayı vardır", "Yanlış"],
                ["$\\exists x \\in \\mathbb{Z}$, $x+3=1$", "$x+3=1$ olan bir tam sayı vardır", "Doğru"],
            ]),
            "Niceleyicili bir önermenin değili alınırken niceleyici değişir ve açık önermenin değili alınır: \"her\" yerine \"bazı\", \"bazı\" yerine \"her\" gelir. \"Her öğrenci sınavı geçti\" önermesinin değili \"Sınavı geçemeyen en az bir öğrenci var\" önermesidir; \"Hiçbir öğrenci sınavı geçmedi\" değildir.",
        ]},
        {"baslik": "Mantık ve kümeler", "icerik": [
            "Mantık bağlaçlarıyla küme işlemleri arasında birebir bir eşleme vardır. Bu eşlemeyi bilmek, bir konudaki kuralı ötekine aktarmayı sağlar.",
            tablo(["Mantık", "Kümeler"], [
                ["Değil $p'$", "Tümleyen $A'$"],
                ["Ve $\\wedge$", "Kesişim $\\cap$"],
                ["Veya $\\vee$", "Birleşim $\\cup$"],
                ["Koşullu $\\Rightarrow$", "Alt küme $\\subset$"],
                ["Totoloji $1$", "Evrensel küme $E$"],
                ["Çelişki $0$", "Boş küme $\\emptyset$"],
            ]),
            "Kapaktaki ahşap düzenek de bu yapının somut bir modelidir: her kavşak bir koşuldur ve top, koşulun doğru ya da yanlış olmasına göre bir yola sapar. Bilgisayarların içindeki devreler de aynı ve, veya ve değil işlemleriyle çalışır.",
        ]},
        {"baslik": "Sınavda mantık", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) mantık, bağlaçların doğruluk tabloları, koşullu önermenin denkliği, De Morgan kuralları ve niceleyicilerin değili biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde ise sözel mantık ve akıl yürütme sorularının temeli bu kurallardır."),
            "Mantık sorularında en hızlı yöntem, her bağlacın yanlış ya da doğru olduğu tek durumu ezberlemektir: \"ve\" yalnızca ikisi de doğruyken doğru, \"veya\" yalnızca ikisi de yanlışken yanlış, koşullu önerme yalnızca $1 \\Rightarrow 0$ durumunda yanlıştır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Soru ya da emir cümlesini önerme saymak", "Önerme doğru ya da yanlış olmalı"],
                ["Veya ile ya da bağlacını karıştırmak", "İkisi de doğruysa veya doğru, ya da yanlış"],
                ["Hipotez yanlışken koşullu önermeyi yanlış saymak", "Hipotez yanlışsa önerme doğru"],
                ["Koşullu önermeyi karşıtına denk sanmak", "Karşıt tersine denktir"],
                ["De Morgan'da bağlacı değiştirmemek", "Ve, veya olur; veya, ve olur"],
                ["\"Her\" önermesinin değilini \"hiçbiri\" yapmak", "Değili \"en az biri değil\""],
            ]),
            "Bu hataların çoğu, günlük dildeki alışkanlıkları matematiğe taşımaktan doğar. Şüphede kaldığında doğruluk tablosunu kurmak, sezginin yanıldığı yeri hemen gösterir.",
        ]},
    ],
    "sss": [
        ("Önerme nedir?",
         "Doğru ya da yanlış olduğu kesin olarak söylenebilen ifadedir. Soru, emir ve kişisel değerlendirme içeren cümleler önerme değildir."),
        ("Ve ile veya bağlacı arasındaki fark nedir?",
         "Ve bağlacıyla kurulan önerme yalnızca iki önerme de doğruysa doğrudur. Veya bağlacıyla kurulan önerme ise yalnızca iki önerme de yanlışsa yanlıştır."),
        ("Koşullu önerme ne zaman yanlıştır?",
         "Yalnızca hipotez doğru ve hüküm yanlış olduğunda yanlıştır. Hipotez yanlışsa koşullu önerme her zaman doğrudur."),
        ("Totoloji nedir?",
         "Önermelerin doğruluk değerleri ne olursa olsun her zaman doğru olan birleşik önermedir. Bir önerme ile değilinin veya ile bağlanması bir totolojidir."),
        ("De Morgan kuralları nedir?",
         "Birleşik bir önermenin değili alınırken ve bağlacı veya, veya bağlacı ve olur; önermelerin her birinin de değili alınır."),
        ("Her önermesinin değili nasıl yazılır?",
         "Her yerine bazı gelir ve açık önermenin değili alınır. Her öğrenci geçti önermesinin değili, geçemeyen en az bir öğrenci var önermesidir."),
    ],
    "kontrol": [
        "Bir ifadenin önerme olup olmadığına karar verebiliyorum.",
        "Doğruluk değerini ve denk önermeleri açıklayabiliyorum.",
        "Bir önermenin değilini yazabiliyorum.",
        "Ve, veya ve ya da bağlaçlarının tablolarını kurabiliyorum.",
        "Koşullu önermenin yanlış olduğu tek durumu biliyorum.",
        "Koşullu önermenin karşıtını, tersini ve karşıt tersini yazabiliyorum.",
        "De Morgan kurallarını önermelere uygulayabiliyorum.",
        "Doğruluk tablosu kurarak totoloji ve çelişkiyi ayırt edebiliyorum.",
        "Açık önermenin doğruluk kümesini bulabiliyorum.",
        "Niceleyicili bir önermenin değilini yazabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["kumeler-konu-anlatimi-pdf", "olasilik-konu-anlatimi-pdf", "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf"],
}
