# scripts/yazilar/82_yas_problemleri.py — Yas Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "yas-problemleri-konu-anlatimi-pdf",
    "baslik": "Yaş Problemleri Konu Anlatımı PDF",
    "aciklama": "Yaş problemleri nasıl çözülür? Sabit yaş farkı, tablo ve zaman çizgisi, yaş toplamı, doğmamış kişi tuzağı, oranlı yaşlar ve doğum yılı; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "yas-problemleri-konu-anlatimi-pdf",
    "kapak_alt": "Yaş problemleri: iki sıralı çubuk üzerinde mavi ve kırmızı figürlerle yaşları geçmişten geleceğe karşılaştıran iki öğrenci",
    "ozet": "Yaş problemleri, zamanın herkes için aynı hızda geçmesine dayanır. Bu tek gerçekten iki güçlü sonuç çıkar: iki kişinin yaş farkı hiç değişmez ve bir grubun yaşları toplamı her yıl kişi sayısı kadar artar. Bu yazıda yaş problemlerinin temel ilkelerini, tablo ve zaman çizgisi yöntemlerini, geçmişe ve geleceğe dönük soruları, yaş toplamı sorularını, doğmamış kişi tuzağını, oranla verilen yaşları ve doğum yılı sorularını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Yaş problemi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için birinci dereceden denklem kurmayı ve çözmeyi biliyor olman yeterli.",
                "Denklem kurmanın adımları için <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "Yaş problemlerinde bir ya da birkaç kişinin bugünkü, geçmişteki ya da gelecekteki yaşları arasındaki ilişkiler verilir ve bilinmeyen yaşlar sorulur. Bu problemlerin hepsi tek bir gerçeğe dayanır: <strong>zaman herkes için aynı hızda geçer</strong>. $5$ yıl geçtiğinde bir çocuğun da, annesinin de, dedesinin de yaşı $5$ artar.",
            "Bu gerçekten yaş problemlerinin dört temel ilkesi çıkar:",
            "<ol><li><strong>Geçen süre herkese eklenir:</strong> $t$ yıl sonra her kişinin yaşı $t$ artar, $t$ yıl önce $t$ eksiktir.</li>"
            "<li><strong>Yaş farkı sabittir:</strong> İki kişinin yaşları arasındaki fark hiç değişmez.</li>"
            "<li><strong>Yaş toplamı kişi sayısı kadar artar:</strong> $n$ kişinin yaşları toplamı $t$ yılda $n \\cdot t$ artar.</li>"
            "<li><strong>Yaş negatif olamaz:</strong> Geçmişe gidilirken henüz doğmamış biri varsa, o kişinin yaşı toplamdan düşülmez.</li></ol>",
            hap("Zaman herkes için aynı geçer: yaş farkı sabit kalır.",
                "$n$ kişinin yaşları toplamı her yıl $n$ artar."),
        ]},
        {"baslik": "Tablo yöntemi", "icerik": [
            "Yaş problemlerinde bilgileri bir tabloya yazmak, hangi yaşın hangi zamana ait olduğunu karıştırmayı önler. Satırlar kişileri, sütunlar zamanları gösterir. Bilinmeyen genellikle bir kişinin bugünkü yaşına verilir; geçmiş ve gelecek sütunları bu yaştan süre eklenip çıkarılarak doldurulur.",
            tablo(["Kişi", "$t$ yıl önce", "Bugün", "$t$ yıl sonra"], [
                ["Birinci kişi", "$x-t$", "$x$", "$x+t$"],
                ["İkinci kişi", "$y-t$", "$y$", "$y+t$"],
                ["Fark", "$x-y$", "$x-y$", "$x-y$"],
            ]),
            "Tablonun son satırı yaş farkının neden sabit olduğunu açıkça gösterir: iki yaştan da aynı süre çıkarılır ya da iki yaşa da aynı süre eklenir, bu yüzden fark değişmez.",
            hap("Yaş problemlerinde satırlara kişiler, sütunlara zamanlar yazılır; herkese aynı süre eklenir ya da çıkarılır."),
        ]},
        {"baslik": "Geleceğe dönük sorular", "icerik": [
            "\"Kaç yıl sonra\" sorulan problemlerde bilinmeyen geçecek süredir. Her kişinin bugünkü yaşına bu süre eklenir ve verilen ilişki denkleme çevrilir.",
            ornek(
                "Bir baba $36$, oğlu $8$ yaşındadır.",
                "Kaç yıl sonra babanın yaşının oğlunun yaşının $3$ katı olacağını bulalım.",
                "$t$ yıl sonra yaşlar $36+t$ ve $8+t$ olur: $36+t=3(8+t)$.",
                "$36+t=24+3t$, yani $12=2t$ ve $t=6$ yıl.",
                "Kontrol: $6$ yıl sonra baba $42$, oğul $14$ yaşında olur; $42=3 \\cdot 14$."),
            "<h3>Yaş farkıyla kısa yol</h3>",
            "Aynı soru denklem kurmadan da çözülür. Baba ile oğul arasındaki fark $36-8=28$ dir ve bu fark hiç değişmez. Babanın yaşı oğlunun $3$ katı olduğunda, fark oğlunun yaşının $2$ katıdır. Yani oğul o zaman $28:2=14$ yaşında olacaktır ve bunun için $14-8=6$ yıl geçmesi gerekir.",
            dikkat(
                "Süreyi yalnızca bir kişiye eklemek.",
                "$36+t=3 \\cdot 8$ gibi bir kurulum, oğlun yaşına süreyi eklemeyi unutmaktır. Geçen süre herkes için geçer; denklemin iki tarafında da $t$ bulunmalıdır."),
        ]},
        {"baslik": "Geçmişe dönük sorular", "icerik": [
            "\"Kaç yıl önce\" sorulan problemlerde süre her kişinin bugünkü yaşından çıkarılır. Bulunan sürenin, kişilerin yaşından büyük olmaması gerekir; aksi hâlde kişi o tarihte henüz doğmamış olur.",
            ornek(
                "Bir anne $40$, kızı $12$ yaşındadır.",
                "Kaç yıl önce annenin yaşının kızının yaşının $5$ katı olduğunu bulalım.",
                "$t$ yıl önce yaşlar $40-t$ ve $12-t$ idi: $40-t=5(12-t)$.",
                "$40-t=60-5t$, yani $4t=20$ ve $t=5$ yıl.",
                "Kontrol: $5$ yıl önce anne $35$, kız $7$ yaşındaydı; $35=5 \\cdot 7$."),
            "Yaş farkı yöntemiyle: fark $40-12=28$ dir. Annenin yaşı kızının $5$ katı olduğunda fark kızın yaşının $4$ katıdır; yani kız o zaman $28:4=7$ yaşındaydı. Bu da $12-7=5$ yıl önce demektir.",
        ]},
        {"baslik": "Yaş farkı yönteminin genel hâli", "icerik": [
            "Önceki iki örnekteki kısa yol her zaman işler. Büyük kişinin yaşı küçüğün $k$ katı olduğunda, yaş farkı küçüğün yaşının $k-1$ katıdır:",
            "$$\\text{küçüğün o zamanki yaşı}=\\dfrac{\\text{yaş farkı}}{k-1}$$",
            "Bu formül, soruda hangi zamanın sorulduğundan bağımsızdır. Önce o anda küçüğün yaşı bulunur, sonra bu yaşın bugünden kaç yıl önce ya da sonra olduğu hesaplanır.",
            ornek(
                "İki kardeş arasında $9$ yaş fark vardır.",
                "Büyüğün yaşının küçüğün yaşının $4$ katı olduğu andaki yaşları bulalım.",
                "Fark, küçüğün yaşının $4-1=3$ katıdır: küçük $9:3=3$ yaşındadır.",
                "Büyük $3+9=12$ yaşındadır. Kontrol: $12=4 \\cdot 3$."),
            hap("Büyük kişinin yaşı küçüğün $k$ katı olduğunda küçüğün o zamanki yaşı $\\dfrac{\\text{yaş farkı}}{k-1}$ olur."),
        ]},
        {"baslik": "Yaş toplamı soruları", "icerik": [
            "Bir grubun yaşları toplamı verildiğinde, zaman geçtikçe toplam her yıl grubun kişi sayısı kadar artar. Bu ilke, kişilerin yaşlarını tek tek bilmeden hesap yapmayı sağlar. Tersine, toplamdaki artış ve geçen süre biliniyorsa gruptaki kişi sayısı da bulunabilir: $5$ yılda toplam $20$ arttıysa grupta $4$ kişi vardır.",
            ornek(
                "Üç kardeşin bugünkü yaşları toplamı $30$ dur.",
                "$4$ yıl sonra yaşları toplamını bulalım.",
                "Her kardeşin yaşı $4$ artar; toplam $3 \\cdot 4=12$ artar.",
                "$4$ yıl sonra toplam: $30+12=42$."),
            ornek(
                "Dört kişilik bir ailenin yaşları toplamı $96$ dır.",
                "Kaç yıl sonra toplamın $120$ olacağını bulalım.",
                "Toplam her yıl $4$ artar: $96+4t=120$.",
                "$4t=24$, yani $t=6$ yıl."),
            hap("Bir grubun yaşları toplamı her yıl grubun kişi sayısı kadar artar."),
        ]},
        {"baslik": "Doğmamış kişi tuzağı", "icerik": [
            "Geçmişe dönük yaş toplamı sorularında, bir kişi o tarihte henüz doğmamışsa yaşı sıfırın altına inmez; o kişi toplama hiç katılmaz. Bu yüzden toplamdan her kişi için geçen süre kadar çıkarmak her zaman doğru değildir.",
            ornek(
                "Bir anne $29$ yaşında, iki çocuğu $5$ ve $3$ yaşındadır.",
                "$4$ yıl önce üçünün yaşları toplamını bulalım.",
                "Bugünkü toplam $29+5+3=37$ dir. Hızlı ama hatalı yol: $37-3 \\cdot 4=25$.",
                "Oysa $4$ yıl önce anne $25$, büyük çocuk $1$ yaşındaydı; küçük çocuk ise henüz doğmamıştı.",
                "Doğru toplam: $25+1=26$."),
            dikkat(
                "Yaşı negatif yazmak.",
                "$3$ yaşındaki çocuğun $4$ yıl önceki yaşı $-1$ değildir; o tarihte bu çocuk yoktur. Geçmişe dönük sorularda önce en küçük kişinin o tarihte doğmuş olup olmadığı kontrol edilmelidir."),
        ]},
        {"baslik": "Üç kişili yaş soruları", "icerik": [
            "Bir kişinin yaşı birkaç kişinin yaşları toplamıyla karşılaştırıldığında, toplamın her yıl kişi sayısı kadar arttığı unutulmamalıdır. Tek bir kişinin yaşı her yıl $1$ artarken iki kişinin yaşları toplamı her yıl $2$ artar.",
            ornek(
                "Bir annenin yaşı iki çocuğunun yaşları toplamının $3$ katıdır. $5$ yıl sonra annenin yaşı, çocuklarının yaşları toplamının $2$ katı olacaktır.",
                "Annenin bugünkü yaşını bulalım.",
                "Çocukların yaşları toplamı $s$, annenin yaşı $3s$ olsun.",
                "$5$ yıl sonra anne $3s+5$ yaşında olur; iki çocuğun yaşları toplamı ise $2 \\cdot 5=10$ artarak $s+10$ olur: $3s+5=2(s+10)$.",
                "$3s+5=2s+20$, yani $s=15$ ve anne $45$ yaşındadır. Kontrol: $5$ yıl sonra anne $50$, çocukların toplamı $25$; $50=2 \\cdot 25$."),
            dikkat(
                "Toplama yalnızca bir kez süre eklemek.",
                "İki çocuğun yaşları toplamına $5$ değil $10$ eklenir. Toplamda kaç kişi varsa geçen süre o kadar kez eklenir."),
        ]},
        {"baslik": "Yaşlar hiç eşit olur mu?", "icerik": [
            "Yaş farkı sabit olduğu için farklı yaştaki iki kişi hiçbir zaman aynı yaşta olamaz. $12$ ve $15$ yaşındaki iki kardeş arasındaki $3$ yıllık fark, $10$ yıl sonra da $50$ yıl sonra da $3$ yıldır. \"Kaç yıl sonra yaşları eşit olur?\" gibi bir soru, farklı yaştaki iki kişi için cevapsızdır.",
            "Buna karşılık yaşların <strong>oranı</strong> zamanla değişir ve $1$ e yaklaşır. $12$ ile $15$ in oranı $\\dfrac{4}{5}$ tür; $15$ yıl sonra yaşlar $27$ ve $30$ olur ve oran $\\dfrac{9}{10}$ a çıkar. Zaman geçtikçe oran büyür ama hiçbir zaman $1$ e ulaşmaz.",
        ]},
        {"baslik": "Ortalama yaş soruları", "icerik": [
            "Bir grubun yaş ortalaması da zamanla aynı hızda değişir: herkes $t$ yaş büyüdüğünde ortalama da $t$ artar. Gruba yeni biri katıldığında ya da biri ayrıldığında ise önce toplam bulunur, sonra yeni kişi sayısına bölünür.",
            ornek(
                "Beş kişilik bir grubun yaş ortalaması $20$ dir. Gruba $26$ yaşında biri katılıyor.",
                "Yeni ortalamayı ve bundan $3$ yıl sonraki ortalamayı bulalım.",
                "Beş kişinin yaşları toplamı: $5 \\cdot 20=100$. Yeni toplam: $100+26=126$.",
                "Yeni ortalama: $126:6=21$.",
                "$3$ yıl sonra herkes $3$ yaş büyür; ortalama $21+3=24$ olur."),
            "Ortalama ile ilgili soruların ayrıntısı <a href=\"/blog/sayi-problemleri-konu-anlatimi-pdf/\">Sayı Problemleri Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Oranla verilen yaşlar", "icerik": [
            "Yaşların oranı verildiğinde yaşlar ortak bir çarpanla yazılır. Oran zamanla değişir, çünkü iki yaşa da aynı süre eklenir ama iki yaşın oranı bu eklemeyle korunmaz.",
            ornek(
                "İki kardeşin bugünkü yaşlarının oranı $3:5$ tir. $6$ yıl sonra bu oran $2:3$ olacaktır.",
                "Kardeşlerin bugünkü yaşlarını bulalım.",
                "Bugünkü yaşlar $3k$ ve $5k$ olsun. $6$ yıl sonra: $\\dfrac{3k+6}{5k+6}=\\dfrac{2}{3}$.",
                "İçler dışlar çarpımı: $9k+18=10k+12$, yani $k=6$.",
                "Yaşlar $18$ ve $30$. Kontrol: $6$ yıl sonra $24$ ve $36$; $\\dfrac{24}{36}=\\dfrac{2}{3}$."),
            "Oran sorularının ayrıntısı <a href=\"/blog/oran-ve-oranti-konu-anlatimi-pdf/\">Oran ve Orantı Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Zaman çizgisi: \"ben senin yaşındayken\" soruları", "icerik": [
            "Bazı yaş soruları, bir kişinin diğerinin bugünkü yaşına geldiği ana göndermede bulunur. Bu sorular tabloyla karışık görünür, ama bir zaman çizgisi üzerinde çok sade hâle gelir. Kapaktaki sıralı çubuklar da bu fikri anlatır: yaşlar, eşit aralıklarla dizilmiş noktalar gibidir.",
            ornek(
                "Ece, Can'ın bugünkü yaşındayken Can $10$ yaşındaydı. Can, Ece'nin bugünkü yaşına geldiğinde Ece $40$ yaşında olacak.",
                "İkisinin bugünkü yaşlarını bulalım.",
                "Yaş farkına $d$ diyelim. Ece'nin Can'ın yaşında olduğu an $d$ yıl önceydi; o zaman Can'ın yaşı Can'ın bugünkü yaşından $d$ eksikti.",
                "Zaman çizgisinde dört yaş eşit aralıklarla dizilir: Can'ın o zamanki yaşı $10$, Can'ın bugünkü yaşı $10+d$, Ece'nin bugünkü yaşı $10+2d$, Ece'nin gelecekteki yaşı $10+3d=40$.",
                "$3d=30$, yani $d=10$. Can $20$, Ece $30$ yaşındadır. Kontrol: $10$ yıl önce Ece $20$, Can $10$; $10$ yıl sonra Can $30$, Ece $40$."),
            "Bu tür sorularda aranan dört sayı her zaman aralarındaki fark yaş farkına eşit olan bir dizi oluşturur. Zaman çizgisini çizmek, denklemleri tek tek kurmaktan çok daha hızlıdır.",
        ]},
        {"baslik": "Doğum yılı soruları", "icerik": [
            "Bazı sorularda yaş yerine yıllar verilir. Bir kişinin belirli bir yıldaki yaşı, o yıl ile doğum yılının farkıdır; doğum günü o yıl henüz gelmediyse bir eksiktir. Sorular genellikle doğum gününün geçmiş olduğunu varsayar.",
            ornek(
                "Bir kişinin $2030$ yılındaki yaşı, $2010$ yılındaki yaşının $3$ katıdır.",
                "Bu kişinin doğum yılını bulalım.",
                "$2010$ daki yaşı $y$ olsun; $20$ yıl sonra yaşı $y+20$ olur: $y+20=3y$.",
                "$2y=20$, yani $y=10$. Kişi $2010$ da $10$ yaşındaydı ve $2000$ yılında doğmuştur.",
                "Kontrol: $2030$ da yaşı $30$ olur; $30=3 \\cdot 10$."),
            ornek(
                "$2012$ yılında doğan bir kızın annesinin $2026$ yılındaki yaşı, kızının o yılki yaşının $3$ katıdır. İkisinin de doğum günü yılın başındadır.",
                "Annenin doğum yılını bulalım.",
                "Kızın $2026$ daki yaşı: $2026-2012=14$. Annenin yaşı: $3 \\cdot 14=42$.",
                "Annenin doğum yılı: $2026-42=1984$.",
                "Anne ile kız arasındaki yaş farkı $2012-1984=28$ dir ve bu fark her yıl aynı kalır."),
            hap("$2008$ doğumlu biri doğum günü geçmişse $2026$ yılında $2026-2008=18$ yaşındadır.", "Doğum günü o yıl henüz gelmediyse $17$ yaşındadır.", gunluk=True),
        ]},
        {"baslik": "Denklem mi, kısa yol mu?", "icerik": [
            "Yaş problemlerinde iki yol da aynı sonuca götürür. Denklem yolu her soruda işler ve adımları açıktır; kısa yollar ise belirli soru türlerinde zaman kazandırır. Kat ilişkisi soruluyorsa yaş farkı yöntemi, grup toplamı soruluyorsa kişi sayısı kadar artış ilkesi, \"ben senin yaşındayken\" türündeki sorularda ise zaman çizgisi en hızlı yoldur.",
            "Kısa yolu kullanırken bile sonucu denklemdeki gibi kontrol etmek gerekir: bulunan yaşları sorudaki her cümlede yerine koymak, kısa yolun o soruya gerçekten uyduğunu gösterir. Emin olunamayan durumlarda denklem yolu her zaman güvenli bir yedektir.",
        ]},
        {"baslik": "Sınavda yaş problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) yaş problemleri kat ilişkisi, yaş toplamı, oranlı yaşlar ve zaman çizgisi soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de yaş problemleri sayısal bölümün klasik soru türlerindendir."),
            "Kat ilişkisi içeren sorularda önce yaş farkı yöntemini denemek çoğu zaman en hızlı yoldur. Yaş toplamı sorularında ise her yıl toplamın kişi sayısı kadar arttığını hatırlamak, soruyu tek satıra indirir. Her iki durumda da bulunan yaşları sorudaki bütün cümlelerde denemek hatayı hemen gösterir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Süreyi yalnız bir kişiye eklemek", "Herkese aynı süre eklenir"],
                ["Yaş farkının değiştiğini sanmak", "Fark sabittir"],
                ["Toplamı yalnız bir yıl artırmak", "Toplam her yıl kişi sayısı kadar artar"],
                ["Doğmamış kişinin yaşını negatif almak", "O kişi toplama katılmaz"],
                ["Oranın zamanla korunduğunu sanmak", "Oran değişir, fark korunur"],
                ["Bulunan süreyi yaş sanmak", "Sorulanın süre mi yaş mı olduğuna bak"],
            ]),
            "Bu hataların çoğu, bilgileri zamanlara göre ayırmadan doğrudan denkleme dökmekten doğar. Tabloyu ya da zaman çizgisini çizmek, her yaşın hangi zamana ait olduğunu netleştirir.",
        ]},
    ],
    "sss": [
        ("Yaş problemleri nasıl çözülür?",
         "Bilgiler kişi ve zaman sütunlarından oluşan bir tabloya yazılır. Geçen süre herkese eklenir ya da herkesten çıkarılır ve verilen ilişki denkleme çevrilir."),
        ("Yaş farkı neden değişmez?",
         "Çünkü geçen süre herkesin yaşına aynı miktarda eklenir. İki yaşa aynı sayı eklenince aralarındaki fark aynı kalır."),
        ("Yaş farkı yöntemi nedir?",
         "Büyüğün yaşı küçüğün k katı olduğunda, yaş farkı küçüğün yaşının k eksi bir katıdır. Buradan küçüğün o anki yaşı doğrudan bulunur."),
        ("Yaş toplamı nasıl değişir?",
         "n kişinin yaşları toplamı her yıl n artar. Geçmişe gidilirken ise o tarihte doğmamış kişiler hesaba katılmaz."),
        ("Doğmamış kişi tuzağı nedir?",
         "Geçmişe dönük toplam sorularında henüz doğmamış bir kişinin yaşını negatif yazmaktır. O kişi o tarihte toplama hiç katılmaz."),
        ("Oranla verilen yaşlar nasıl bulunur?",
         "Yaşlar oran sayılarının k katı olarak yazılır, geçen süre iki yaşa da eklenir ve yeni oran bir orantı olarak kurulur."),
        ("İki kişinin yaşları hiç eşit olur mu?",
         "Hayır. Yaş farkı hiç değişmediği için farklı yaştaki iki kişi hiçbir zaman aynı yaşta olamaz. Yaşların oranı ise zamanla bire yaklaşır ama bire ulaşmaz."),
        ("Yaş ortalaması zamanla nasıl değişir?",
         "Herkes aynı süre kadar büyüdüğü için ortalama da geçen süre kadar artar. Gruba biri katılırsa önce toplam bulunur, sonra yeni kişi sayısına bölünür."),
    ],
    "kontrol": [
        "Yaş problemlerinin dört temel ilkesini açıklayabiliyorum.",
        "Bilgileri kişi ve zaman tablosuna yazabiliyorum.",
        "Geleceğe dönük yaş sorularını çözebiliyorum.",
        "Geçmişe dönük yaş sorularını çözebiliyorum.",
        "Yaş farkı yöntemiyle kat ilişkisi sorularını kısaltabiliyorum.",
        "Yaş toplamının zamanla nasıl değiştiğini hesaplayabiliyorum.",
        "Geçmişte doğmamış kişileri toplamdan ayırabiliyorum.",
        "Oranla verilen yaşları orantı kurarak bulabiliyorum.",
        "\"Ben senin yaşındayken\" sorularını zaman çizgisiyle çözebiliyorum.",
        "Doğum yılı sorularında yıl ile yaş arasında geçiş yapabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["denklem-kurma-problemleri-nasil-cozulur", "oran-ve-oranti-konu-anlatimi-pdf", "sayi-problemleri-konu-anlatimi-pdf"],
}
