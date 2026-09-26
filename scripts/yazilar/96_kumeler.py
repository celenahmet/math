# scripts/yazilar/96_kumeler.py — Kumeler (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kumeler-konu-anlatimi-pdf",
    "baslik": "Kümeler Konu Anlatımı PDF",
    "aciklama": "Küme nedir? Gösterim, eleman sayısı, boş küme, alt küme sayısı, birleşim, kesişim, fark, tümleyen, eleman sayısı formülü ve Venn şeması problemleri; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "kumeler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kumeler-konu-anlatimi-pdf",
    "kapak_alt": "Kümeler: kesişen iki halka içine biçimlerine göre nesneler yerleştiren iki öğrenci",
    "ozet": "Küme, belirli bir özelliğe göre bir araya getirilmiş nesnelerin topluluğudur. Kümeler matematiğin ortak dilidir: sayı kümeleri, çözüm kümeleri, olasılıkta örnek uzay ve olaylar hep kümelerle anlatılır. Bu yazıda kümenin tanımını ve gösterim biçimlerini, eleman sayısını, boş kümeyi, alt kümeleri ve alt küme sayısını, birleşim, kesişim, fark ve tümleyen işlemlerini, eleman sayısı formülünü ve Venn şemasıyla çözülen problemleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Küme nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için sayı kümelerini ve basit saymayı biliyor olman yeterli.",
                "Sayı kümeleri için <a href=\"/blog/sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf/\">Sayılar ve Sayı Kümeleri Konu Anlatımı PDF</a> yazısına göz at."),
            "Hangi nesnelerin içinde olup hangilerinin olmadığı kesin olarak belirlenebilen topluluklara <strong>küme</strong> denir. Kümeyi oluşturan nesnelere <strong>eleman</strong> denir. Bir $a$ nesnesi $A$ kümesinin elemanıysa $a \\in A$, değilse $a \\notin A$ yazılır.",
            "\"Sınıftaki uzun boylu öğrenciler\" bir küme değildir, çünkü kimin uzun boylu sayılacağı kişiden kişiye değişir. \"Sınıfta boyu $170$ santimetreden uzun olan öğrenciler\" ise bir kümedir, çünkü her öğrenci için içinde olup olmadığı kesin olarak söylenebilir.",
            hap("Küme, elemanları kesin olarak belirlenebilen topluluktur.",
                "$a \\in A$: $a$, $A$ nın elemanıdır."),
        ]},
        {"baslik": "Kümelerin gösterimi", "icerik": [
            "Bir küme üç biçimde gösterilebilir. Aynı küme her üç gösterimle de yazılabilir; hangisinin seçileceği kümenin büyüklüğüne ve kullanım amacına bağlıdır.",
            tablo(["Gösterim", "Örnek"], [
                ["Liste yöntemi", "$A=\\{2, 4, 6, 8\\}$"],
                ["Ortak özellik yöntemi", "$A$, $10$ dan küçük pozitif çift sayılar"],
                ["Venn şeması", "Kapalı bir eğrinin içine elemanlar yazılır"],
            ]),
            "Liste yönteminde elemanların sırası önemli değildir ve bir eleman bir kez yazılır: $\\{2, 4, 6\\}$ ile $\\{6, 2, 4\\}$ aynı kümedir. Kapaktaki halkalar ise Venn şemasının somut hâlidir: her halka bir kümeyi, halkaların kesiştiği bölge ortak elemanları gösterir.",
        ]},
        {"baslik": "Eleman sayısı ve boş küme", "icerik": [
            "Bir $A$ kümesinin eleman sayısı $s(A)$ ile gösterilir. Hiç elemanı olmayan kümeye <strong>boş küme</strong> denir ve $\\emptyset$ ya da $\\{\\}$ ile gösterilir; $s(\\emptyset)=0$ dır.",
            ornek(
                "$A=\\{2, 4, 6, 8\\}$, $B=\\{0\\}$ ve $C$, karesi negatif olan gerçek sayıların kümesi olsun.",
                "Kümelerin eleman sayılarını bulalım.",
                "$s(A)=4$.",
                "$B$ nin bir elemanı vardır, o da $0$ dır: $s(B)=1$.",
                "Hiçbir gerçek sayının karesi negatif değildir: $C=\\emptyset$ ve $s(C)=0$."),
            dikkat(
                "$\\{0\\}$ kümesini boş küme sanmak.",
                "$\\{0\\}$ kümesinin bir elemanı vardır: $0$. Boş kümenin ise hiç elemanı yoktur. Benzer biçimde $\\{\\emptyset\\}$ de boş değildir; tek elemanı boş kümedir."),
        ]},
        {"baslik": "Sonlu ve sonsuz kümeler", "icerik": [
            "Eleman sayısı bir doğal sayıyla ifade edilebilen kümelere <strong>sonlu küme</strong>, elemanları sayılarak bitirilemeyen kümelere <strong>sonsuz küme</strong> denir. Haftanın günleri sonlu bir kümedir ve $7$ elemanlıdır. Doğal sayılar kümesi ise sonsuzdur: hangi doğal sayıyı alırsan al, ondan büyük bir doğal sayı vardır.",
            "Sonsuz kümeler liste yöntemiyle tam olarak yazılamaz; ilk birkaç eleman yazılıp üç nokta konur: $\\mathbb{N}=\\{0, 1, 2, 3, \\ldots\\}$. Eleman sayısı kavramı sonlu kümeler için kullanılır; bu yazıdaki bütün eleman sayısı hesapları sonlu kümeler içindir.",
            ornek(
                "$A$, $20$ den küçük asal sayıların kümesi olsun.",
                "Kümeyi liste yöntemiyle yazıp eleman sayısını bulalım.",
                "$A=\\{2, 3, 5, 7, 11, 13, 17, 19\\}$.",
                "$s(A)=8$; $A$ sonlu bir kümedir."),
        ]},
        {"baslik": "Alt küme", "icerik": [
            "$A$ kümesinin her elemanı $B$ kümesinin de elemanıysa $A$ ya $B$ nin <strong>alt kümesi</strong> denir ve $A \\subset B$ yazılır. Her küme kendisinin alt kümesidir ve boş küme her kümenin alt kümesidir.",
            "Elemanları aynı olan iki kümeye <strong>eşit kümeler</strong> denir. Eleman sayıları aynı olan kümelere ise <strong>denk kümeler</strong> denir: $\\{1, 2, 3\\}$ ile $\\{a, b, c\\}$ denktir ama eşit değildir.",
            ornek(
                "$A=\\{1, 2\\}$, $B=\\{1, 2, 3\\}$ ve $C=\\{2, 4\\}$ kümeleri verilsin.",
                "Alt küme ilişkilerini inceleyelim.",
                "$A$ nın her elemanı $B$ de vardır: $A \\subset B$.",
                "$C$ nin elemanı $4$, $B$ de yoktur: $C$, $B$ nin alt kümesi değildir."),
        ]},
        {"baslik": "Alt küme sayısı", "icerik": [
            "$n$ elemanlı bir kümenin alt küme sayısı $2^n$ dir. Her eleman için iki seçenek vardır: alt kümeye girer ya da girmez; bu seçimler çarpılır. Kümenin kendisi dışındaki alt kümelere <strong>öz alt küme</strong> denir ve sayıları $2^n-1$ dir.",
            ornek(
                "$A=\\{a, b, c\\}$ kümesi verilsin.",
                "Alt kümelerini yazalım ve sayısını bulalım.",
                "Alt kümeler: $\\emptyset$, $\\{a\\}$, $\\{b\\}$, $\\{c\\}$, $\\{a, b\\}$, $\\{a, c\\}$, $\\{b, c\\}$, $\\{a, b, c\\}$.",
                "Toplam $8=2^3$ alt küme; öz alt küme sayısı $7$."),
            ornek(
                "$A=\\{a, b, c, d\\}$ kümesi verilsin.",
                "$a$ yı içeren alt kümelerin sayısını bulalım.",
                "$a$ her alt kümede kesin olarak yer alır; kalan $3$ eleman için $2^3=8$ seçenek vardır.",
                "$a$ yı içeren $8$ alt küme vardır; bu, bütün alt kümelerin yarısıdır: $16:2=8$."),
            "Belirli sayıda elemanlı alt kümeler kombinasyonla sayılır: $n$ elemanlı bir kümenin $r$ elemanlı alt kümelerinin sayısı $C(n, r)$ dir. Ayrıntısı <a href=\"/blog/kombinasyon-konu-anlatimi-pdf/\">Kombinasyon Konu Anlatımı PDF</a> yazısında.",
            hap("$n$ elemanlı bir kümenin $2^n$ alt kümesi ve $2^n-1$ öz alt kümesi vardır."),
        ]},
        {"baslik": "Koşullu alt küme soruları", "icerik": [
            "Alt küme sorularında çoğu zaman belirli koşulları sağlayan alt kümeler sayılır. Genel yöntem şudur: kesin olarak girecek elemanlar alt kümeye önceden konur, kesin olarak girmeyecek elemanlar kümeden çıkarılır ve kalan her eleman için iki seçenek çarpılır.",
            ornek(
                "$A=\\{1, 2, 3, 4, 5\\}$ kümesi verilsin.",
                "Koşullu alt küme sayılarını bulalım.",
                "$1$ i içeren ama $2$ yi içermeyen alt kümeler: $1$ kesin girer, $2$ kesin girmez; kalan $3$ eleman için $2^3=8$.",
                "Boş olmayan alt kümeler: $2^5-1=31$.",
                "İki elemanlı alt kümeler: $C(5, 2)=10$. Üç elemanlı alt kümeler de $C(5, 3)=10$ tanedir."),
            "İki elemanlı ve üç elemanlı alt kümelerin sayısının eşit çıkması rastlantı değildir. Her iki elemanlı alt kümenin dışında kalan elemanlar bir üç elemanlı alt küme oluşturur; bu eşleme iki sayının eşit olduğunu gösterir.",
        ]},
        {"baslik": "Birleşim ve kesişim", "icerik": [
            "İki kümenin elemanlarının hepsinden oluşan kümeye <strong>birleşim</strong> denir ve $A \\cup B$ ile gösterilir. İki kümenin ortak elemanlarından oluşan kümeye <strong>kesişim</strong> denir ve $A \\cap B$ ile gösterilir. Kesişimi boş olan kümelere <strong>ayrık kümeler</strong> denir.",
            ornek(
                "$A=\\{1, 2, 3, 4, 5\\}$ ve $B=\\{4, 5, 6, 7\\}$ kümeleri verilsin.",
                "Birleşimi ve kesişimi bulalım.",
                "$A \\cup B=\\{1, 2, 3, 4, 5, 6, 7\\}$.",
                "$A \\cap B=\\{4, 5\\}$."),
            tablo(["İşlem", "Anlamı", "Sözel karşılığı"], [
                ["$A \\cup B$", "En az birinde olanlar", "$A$ ya da $B$"],
                ["$A \\cap B$", "İkisinde birden olanlar", "$A$ ve $B$"],
            ]),
        ]},
        {"baslik": "Birleşim ve kesişimin özellikleri", "icerik": [
            "Birleşim ve kesişim işlemleri, sayılardaki toplama ve çarpmaya benzeyen özelliklere sahiptir. Bu özellikler uzun küme ifadelerini sadeleştirmeyi sağlar.",
            tablo(["Özellik", "Birleşim", "Kesişim"], [
                ["Değişme", "$A \\cup B=B \\cup A$", "$A \\cap B=B \\cap A$"],
                ["Birleşme", "$(A \\cup B) \\cup C=A \\cup (B \\cup C)$", "$(A \\cap B) \\cap C=A \\cap (B \\cap C)$"],
                ["Boş küme", "$A \\cup \\emptyset=A$", "$A \\cap \\emptyset=\\emptyset$"],
                ["Kendisiyle", "$A \\cup A=A$", "$A \\cap A=A$"],
            ]),
            "Birleşim ile kesişim arasında dağılma özelliği de vardır: $A \\cap (B \\cup C)=(A \\cap B) \\cup (A \\cap C)$. Ayrıca $A \\subset B$ ise $A \\cup B=B$ ve $A \\cap B=A$ olur; küçük küme büyük kümenin içinde kalır.",
        ]},
        {"baslik": "Fark ve tümleyen", "icerik": [
            "$A$ da olup $B$ de olmayan elemanların kümesine $A$ ile $B$ nin <strong>farkı</strong> denir ve $A-B$ ile gösterilir. Üzerinde çalışılan bütün elemanları içeren kümeye <strong>evrensel küme</strong> denir; evrensel kümede olup $A$ da olmayan elemanlar da $A$ nın <strong>tümleyenidir</strong> ve $A'$ ile gösterilir.",
            ornek(
                "Evrensel küme $E=\\{1, 2, 3, 4, 5, 6, 7, 8\\}$, $A=\\{1, 2, 3, 4, 5\\}$ ve $B=\\{4, 5, 6, 7\\}$ olsun.",
                "$A-B$, $B-A$ ve $A'$ kümelerini bulalım.",
                "$A-B=\\{1, 2, 3\\}$.",
                "$B-A=\\{6, 7\\}$.",
                "$A'=\\{6, 7, 8\\}$."),
            dikkat(
                "$A-B$ ile $B-A$ yı aynı sanmak.",
                "Fark işlemi yer değiştirmez. $A-B$, $A$ ya özgü elemanlardır; $B-A$ ise $B$ ye özgü elemanlardır. Örnekte ikisi tamamen farklı kümelerdir."),
        ]},
        {"baslik": "Eleman sayısı formülü", "icerik": [
            "İki kümenin birleşiminin eleman sayısı, eleman sayılarının toplamından kesişimin eleman sayısı çıkarılarak bulunur, çünkü ortak elemanlar iki kez sayılmıştır:",
            "$$s(A \\cup B)=s(A)+s(B)-s(A \\cap B)$$",
            ornek(
                "$40$ kişilik bir sınıfta $25$ öğrenci İngilizce, $18$ öğrenci Almanca biliyor ve $8$ öğrenci iki dili de biliyor.",
                "En az bir dil bilen ve hiçbir dil bilmeyen öğrenci sayılarını bulalım.",
                "En az bir dil bilen: $25+18-8=35$.",
                "Hiçbir dil bilmeyen: $40-35=5$.",
                "Yalnız İngilizce bilen: $25-8=17$; yalnız Almanca bilen: $18-8=10$."),
            "Formül, olasılıktaki birleşim kuralıyla aynı mantığa dayanır. Olasılıkta eleman sayıları yerine olasılıklar kullanılır; ayrıntısı <a href=\"/blog/olasilik-konu-anlatimi-pdf/\">Olasılık Konu Anlatımı PDF</a> yazısında.",
            hap("$s(A \\cup B)=s(A)+s(B)-s(A \\cap B)$ olur; kesişim iki kez sayıldığı için bir kez çıkarılır."),
        ]},
        {"baslik": "Farkın eleman sayısı", "icerik": [
            "Fark kümesinin eleman sayısı, kümenin eleman sayısından kesişimin eleman sayısı çıkarılarak bulunur. Birleşim de ayrık üç parçaya bölünebilir: yalnız $A$ da olanlar, yalnız $B$ de olanlar ve ortak kısım.",
            "$$s(A-B)=s(A)-s(A \\cap B)$$",
            "$$s(A \\cup B)=s(A-B)+s(B-A)+s(A \\cap B)$$",
            ornek(
                "$s(A)=15$, $s(B)=12$ ve $s(A \\cup B)=22$ veriliyor.",
                "Kesişimin ve farkların eleman sayılarını bulalım.",
                "$s(A \\cap B)=15+12-22=5$.",
                "$s(A-B)=15-5=10$ ve $s(B-A)=12-5=7$.",
                "Kontrol: $10+7+5=22$."),
        ]},
        {"baslik": "Venn şemasıyla problem çözmek", "icerik": [
            "Küme problemlerinde en güvenli yöntem, Venn şemasını bölge bölge doldurmaktır. İşe her zaman kesişimden başlanır; sonra yalnızca bir kümede olan bölgeler, en son da hiçbir kümede olmayanlar doldurulur.",
            ornek(
                "$30$ öğrencinin $18$ i futbol, $15$ i basketbol oynuyor ve $5$ öğrenci ikisini de oynamıyor.",
                "İki sporu da oynayan ve yalnızca futbol oynayan öğrenci sayılarını bulalım.",
                "En az bir spor oynayan: $30-5=25$.",
                "İkisini de oynayan: $18+15-25=8$.",
                "Yalnız futbol: $18-8=10$; yalnız basketbol: $15-8=7$. Kontrol: $10+8+7+5=30$."),
            dikkat(
                "Yalnız bir kümede olanları küme sayısıyla karıştırmak.",
                "\"Futbol oynayan $18$ öğrenci\" iki sporu da oynayanları da kapsar. Yalnızca futbol oynayanların sayısı, ortak bölge çıkarılarak bulunur: $18-8=10$."),
            hap("Bir ofiste çay içen $18$, kahve içen $12$ ve ikisini de içen $5$ kişi varsa en az birini içen $18+12-5=25$ kişi vardır.", "Venn şeması her zaman kesişimden başlanarak doldurulur.", gunluk=True),
        ]},
        {"baslik": "Yüzdeli küme problemleri", "icerik": [
            "Küme problemlerinde sayılar yerine yüzdeler de verilebilir. Yöntem değişmez: bütün grup yüzde yüz kabul edilir ve eleman sayısı formülü yüzdelerle aynen uygulanır.",
            ornek(
                "Bir işyerindeki çalışanların $\\%60$ ı çay, $\\%50$ si kahve içiyor ve $\\%20$ si ikisini de içiyor.",
                "Hiçbirini içmeyenlerin oranını bulalım.",
                "En az birini içen: $60+50-20=90$, yani $\\%90$.",
                "Hiçbirini içmeyen: $100-90=10$, yani $\\%10$.",
                "Çalışan sayısı $200$ ise hiçbirini içmeyen $20$ kişidir."),
        ]},
        {"baslik": "Üç kümeli problemler", "icerik": [
            "Üç küme için eleman sayısı formülü, ikili kesişimlerin çıkarılması ve üçlü kesişimin geri eklenmesiyle yazılır:",
            "$$s(A \\cup B \\cup C)=s(A)+s(B)+s(C)-s(A \\cap B)-s(A \\cap C)-s(B \\cap C)+s(A \\cap B \\cap C)$$",
            ornek(
                "Bir okulda $3$ kulübün üye sayıları $20$, $18$ ve $15$ tir. İkişer kulübe birden üye olanların sayıları $7$, $5$ ve $4$, üç kulübe birden üye olanların sayısı $2$ dir.",
                "En az bir kulübe üye olan öğrenci sayısını bulalım.",
                "Tekli toplam: $20+18+15=53$. İkili kesişimler: $7+5+4=16$.",
                "En az bir kulübe üye: $53-16+2=39$."),
            "Üçlü kesişimin geri eklenmesinin nedeni şudur: üç kulübe birden üye olan bir öğrenci, tekli toplamda üç kez sayılır, ikili kesişimlerde üç kez çıkarılır ve hiç sayılmamış olur. Geri eklemek bu öğrenciyi bir kez saymayı sağlar.",
        ]},
        {"baslik": "En az ve en çok soruları", "icerik": [
            "Kesişimin eleman sayısı verilmediğinde soru bazen olası en büyük ya da en küçük değeri sorar. Kesişim, küçük kümenin eleman sayısından büyük olamaz; birleşim ise bütün grubun eleman sayısını aşamaz.",
            ornek(
                "$30$ kişilik bir sınıfta $18$ öğrenci satranç, $20$ öğrenci yüzme kursuna gidiyor.",
                "İki kursa birden giden öğrenci sayısının en az ve en çok kaç olabileceğini bulalım.",
                "En çok: kesişim satranç kümesinden büyük olamaz; en çok $18$ öğrenci.",
                "En az: birleşim sınıf mevcudunu aşamaz; bu yüzden kesişim en az $18+20-30=8$ olur."),
            "En çok durumda satranç oynayan herkes yüzmeye de gider; en az durumda ise sınıfta hiçbir kursa gitmeyen öğrenci kalmaz. Uç değerleri bulurken bu iki durumu Venn şemasında çizmek, sonucun gerçekten mümkün olduğunu gösterir.",
        ]},
        {"baslik": "Tümleyen ve De Morgan kuralları", "icerik": [
            "Birleşim ve kesişimin tümleyenleri arasında iki önemli eşitlik vardır. Bu eşitliklere De Morgan kuralları denir:",
            "$$(A \\cup B)'=A' \\cap B'$$",
            "$$(A \\cap B)'=A' \\cup B'$$",
            "Birinci kural şunu söyler: \"$A$ ya da $B$ de olmayanlar\", \"hem $A$ da hem $B$ de olmayanlardır\". İkinci kural ise: \"ikisinde birden olmayanlar\", \"en az birinde olmayanlardır\".",
            ornek(
                "Evrensel küme $E=\\{1, 2, 3, 4, 5, 6, 7, 8\\}$, $A=\\{1, 2, 3, 4, 5\\}$ ve $B=\\{4, 5, 6, 7\\}$ olsun.",
                "$(A \\cup B)'$ ve $A' \\cap B'$ kümelerini bulup karşılaştıralım.",
                "$A \\cup B=\\{1, 2, 3, 4, 5, 6, 7\\}$; tümleyeni $\\{8\\}$.",
                "$A'=\\{6, 7, 8\\}$ ve $B'=\\{1, 2, 3, 8\\}$; kesişimleri $\\{8\\}$.",
                "İki küme eşittir."),
            hap("$(A \\cup B)'=A' \\cap B'$ ve $(A \\cap B)'=A' \\cup B'$ olur."),
        ]},
        {"baslik": "Kartezyen çarpım", "icerik": [
            "$A$ nın her elemanıyla $B$ nin her elemanının oluşturduğu sıralı ikililerin kümesine $A$ ile $B$ nin <strong>kartezyen çarpımı</strong> denir ve $A \\times B$ ile gösterilir. Eleman sayısı çarpımla bulunur: $s(A \\times B)=s(A) \\cdot s(B)$.",
            ornek(
                "$A=\\{1, 2\\}$ ve $B=\\{a, b, c\\}$ olsun.",
                "Kartezyen çarpımı yazalım.",
                "$A \\times B=\\{(1,a), (1,b), (1,c), (2,a), (2,b), (2,c)\\}$.",
                "$s(A \\times B)=2 \\cdot 3=6$."),
            "Sıralı ikililerde sıra önemlidir: $(1,a)$ ile $(a,1)$ farklı ikililerdir. Bu kural, saymanın temel ilkesi olan çarpma kuralının küme dilindeki karşılığıdır; iki aşamalı bir seçimin bütün sonuçları bir kartezyen çarpım oluşturur.",
        ]},
        {"baslik": "Sayı kümeleri arasındaki ilişki", "icerik": [
            "Sayı kümeleri birbirinin içine geçen kümelerdir. Her doğal sayı bir tam sayıdır, her tam sayı bir rasyonel sayıdır ve her rasyonel sayı bir gerçek sayıdır:",
            "$$\\mathbb{N} \\subset \\mathbb{Z} \\subset \\mathbb{Q} \\subset \\mathbb{R}$$",
            "Bu zincir, alt küme kavramının en tanıdık örneğidir. Ters yön ise doğru değildir: $-3 \\in \\mathbb{Z}$ ama $-3 \\notin \\mathbb{N}$. Benzer biçimde $\\dfrac{1}{2} \\in \\mathbb{Q}$ ama bir tam sayı değildir.",
        ]},
        {"baslik": "Sınavda kümeler", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kümeler alt küme sayısı, küme işlemleri ve özellikle Venn şemasıyla çözülen sözel problemler biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de küme problemleri sayısal akıl yürütmenin parçasıdır."),
            "Küme problemlerinde Venn şemasını çizmek ve bölgeleri kesişimden başlayarak doldurmak neredeyse her zaman en hızlı yoldur. Şema dolduğunda bütün bölgelerin toplamının evrensel kümenin eleman sayısına eşit olduğunu kontrol etmek, hatayı hemen gösterir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\{0\\}$ ı boş küme sanmak", "Bir elemanı vardır"],
                ["Alt küme sayısını $2n$ almak", "$2^n$"],
                ["Birleşimde kesişimi çıkarmamak", "Ortak elemanlar bir kez sayılır"],
                ["$A-B$ ile $B-A$ yı aynı sanmak", "Fark yer değiştirmez"],
                ["\"$A$ da olan\" ile \"yalnız $A$ da olan\"ı karıştırmak", "Yalnız $A$: $A-B$"],
                ["Üç kümede üçlü kesişimi geri eklememek", "Üçlü kesişim eklenir"],
            ]),
            "Bu hataların çoğu, bir elemanın kaç kez sayıldığını takip etmemekten doğar. Venn şemasını bölge bölge doldurmak, her elemanın tam olarak bir kez sayılmasını sağlar.",
        ]},
    ],
    "sss": [
        ("Küme nedir?",
         "Elemanları kesin olarak belirlenebilen nesneler topluluğudur. Bir nesnenin kümede olup olmadığı tartışmasız biçimde söylenebilmelidir."),
        ("Boş küme nedir?",
         "Hiç elemanı olmayan kümedir. Eleman sayısı sıfırdır; sıfırı eleman olarak içeren küme ise boş değildir."),
        ("Bir kümenin kaç alt kümesi vardır?",
         "n elemanlı bir kümenin 2 üzeri n alt kümesi vardır. Kümenin kendisi dışındaki alt kümelerin, yani öz alt kümelerin sayısı bundan bir eksiktir."),
        ("Birleşim ile kesişim arasındaki fark nedir?",
         "Birleşim, iki kümeden en az birinde olan elemanlardır. Kesişim ise iki kümede birden olan elemanlardır."),
        ("İki kümenin birleşiminin eleman sayısı nasıl bulunur?",
         "Eleman sayıları toplanır ve kesişimin eleman sayısı çıkarılır. Ortak elemanlar iki kez sayıldığı için bir kez çıkarılır."),
        ("Venn şeması nasıl doldurulur?",
         "Önce kesişim bölgesi, sonra yalnızca bir kümede olan bölgeler, en son hiçbir kümede olmayanlar doldurulur. Bütün bölgelerin toplamı evrensel kümenin eleman sayısına eşit olmalıdır."),
        ("Denk küme ile eşit küme arasındaki fark nedir?",
         "Eşit kümelerin elemanları aynıdır. Denk kümelerin ise yalnızca eleman sayıları aynıdır; elemanları farklı olabilir."),
        ("Kartezyen çarpımın eleman sayısı nasıl bulunur?",
         "İki kümenin eleman sayıları çarpılır. 2 elemanlı bir kümeyle 3 elemanlı bir kümenin kartezyen çarpımı 6 elemanlıdır."),
    ],
    "kontrol": [
        "Kümenin iyi tanımlanmış olma koşulunu açıklayabiliyorum.",
        "Bir kümeyi liste, ortak özellik ve Venn şemasıyla gösterebiliyorum.",
        "Eleman sayısını bulabiliyor, boş kümeyi tanıyabiliyorum.",
        "Alt küme, eşit küme ve denk küme kavramlarını ayırt edebiliyorum.",
        "Alt küme ve öz alt küme sayılarını hesaplayabiliyorum.",
        "Birleşim, kesişim, fark ve tümleyen işlemlerini yapabiliyorum.",
        "İki kümenin birleşiminin eleman sayısını formülle bulabiliyorum.",
        "Venn şemasını kesişimden başlayarak doldurabiliyorum.",
        "Üç kümeli eleman sayısı formülünü kullanabiliyorum.",
        "De Morgan kurallarını bir örnekle gösterebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["mantik-konu-anlatimi-pdf", "olasilik-konu-anlatimi-pdf", "sayilar-ve-sayi-kumeleri-konu-anlatimi-pdf"],
}
