# scripts/yazilar/79_denklem_kurma.py — Denklem Kurma Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "denklem-kurma-problemleri-nasil-cozulur",
    "baslik": "Denklem Kurma Problemleri Nasıl Çözülür?",
    "aciklama": "Denklem kurma nasıl yapılır? Sözel ifadeleri cebire çevirme, bilinmeyen seçimi, tablo yöntemi, sayı, yaş, para ve geometri soruları; çözümlü örneklerle.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "cebir",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "denklem-kurma-problemleri-nasil-cozulur",
    "kapak_alt": "Denklem kurma problemleri: terazinin kefelerine küpler ve toplar yerleştirerek verilen ilişkiyi dengeye dönüştüren iki öğrenci",
    "ozet": "Problem çözmenin en zor adımı çoğu zaman hesap değil, cümleyi denkleme çevirmektir. Denklem bir kez doğru kurulduğunda geri kalanı birkaç satırlık işlemdir. Bu yazıda sözel ifadelerin cebirsel karşılıklarını, bilinmeyenin nasıl seçileceğini, bilgileri tabloya dökmeyi, sayı, yaş, para ve geometri sorularını, iki bilinmeyenli kurulumları ve bulunan cevabın nasıl kontrol edileceğini çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Denklem kurmak ne demek?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için cebirsel ifadeleri ve birinci dereceden denklem çözmeyi biliyor olman yeterli.",
                "Denklem çözme adımları için <a href=\"/blog/birinci-dereceden-denklemler-konu-anlatimi-pdf/\">Birinci Dereceden Denklemler Konu Anlatımı PDF</a> yazısına göz at."),
            "Bir problemde bilinmeyen bir nicelik ile bilinen nicelikler arasındaki ilişki cümlelerle anlatılır. <strong>Denklem kurmak</strong>, bu cümleleri matematik diline çevirip bilinmeyeni bulmaya yarayan bir eşitlik yazmaktır. Kapaktaki terazi bu işin özetidir: problemdeki bilgi, iki kefesi dengede duran bir eşitliğe dönüştürülür.",
            "Hemen her problem aynı beş adımla çözülür:",
            "<ol><li><strong>Oku:</strong> Soruyu sonuna kadar oku ve neyin sorulduğunu belirle.</li>"
            "<li><strong>Bilinmeyeni seç:</strong> Bir niceliğe $x$ de ve diğerlerini $x$ cinsinden yaz.</li>"
            "<li><strong>İlişkiyi yaz:</strong> Cümledeki eşitliği bul ve denklemi kur.</li>"
            "<li><strong>Çöz:</strong> Denklemi çözerek $x$ i bul.</li>"
            "<li><strong>Kontrol et ve cevapla:</strong> Bulduğun değeri soruda dene ve sorulan niceliği yaz.</li></ol>",
            hap("Denklem kurmak, problemdeki ilişkiyi bir eşitliğe çevirmektir.",
                "Oku, bilinmeyeni seç, ilişkiyi yaz, çöz, kontrol et."),
        ]},
        {"baslik": "Sözel ifadelerin cebirsel karşılıkları", "icerik": [
            "Problemlerde aynı kalıplar tekrar tekrar kullanılır. Bu kalıpların karşılığını bilmek, cümleyi denkleme çevirmeyi hızlandırır. Aşağıda bilinmeyen sayı $x$ ile gösterilmiştir:",
            tablo(["Sözel ifade", "Cebirsel karşılık"], [
                ["Bir sayının $7$ fazlası", "$x+7$"],
                ["Bir sayının $7$ eksiği", "$x-7$"],
                ["$7$ nin bir sayıdan farkı", "$7-x$"],
                ["Bir sayının $3$ katı", "$3x$"],
                ["Bir sayının yarısı", "$\\dfrac{x}{2}$"],
                ["Bir sayının $\\dfrac{2}{5}$ si", "$\\dfrac{2}{5}x$"],
                ["Bir sayının $3$ katının $4$ eksiği", "$3x-4$"],
                ["Bir sayının $4$ eksiğinin $3$ katı", "$3(x-4)$"],
                ["Bir sayının karesi", "$x^2$"],
            ]),
            dikkat(
                "Kelimelerin sırası işlemin sırasını belirler.",
                "\"$3$ katının $4$ eksiği\" ile \"$4$ eksiğinin $3$ katı\" aynı kelimelerden oluşur ama farklı ifadelerdir. İlkinde önce çarpılır sonra çıkarılır, ikincisinde önce çıkarılır sonra çarpılır. \"$7$ eksiği\" ile \"$7$ den farkı\" da farklıdır: $x-7$ ile $7-x$."),
            hap("Bir sayının $4$ eksiğinin $3$ katı $3(x-4)$, $3$ katının $4$ eksiği $3x-4$ olur; işlemlerin sırası cümleden okunur."),
        ]},
        {"baslik": "Bilinmeyeni seçmek", "icerik": [
            "Doğru bilinmeyeni seçmek denklemi kısaltır. Genel kural, <strong>diğer niceliklerin kolayca ifade edilebildiği</strong> niceliğe $x$ demektir. Çoğu zaman bu, en küçük nicelik ya da başka niceliklerin katı olarak anlatılan niceliktir.",
            ornek(
                "İki sayının toplamı $48$ ve büyük sayı küçük sayının $3$ katı olsun.",
                "Sayıları bulalım.",
                "Büyük sayı küçüğün katı olarak anlatıldığı için küçüğe $x$ diyelim; büyük sayı $3x$ olur.",
                "Toplam: $x+3x=48$, yani $4x=48$ ve $x=12$.",
                "Sayılar $12$ ve $36$. Kontrol: $12+36=48$ ve $36=3 \\cdot 12$."),
            "Büyük sayıya $x$ deseydik küçük sayı $\\dfrac{x}{3}$ olurdu ve kesirli bir denklemle uğraşmak zorunda kalırdık. Sonuç aynı çıkar ama yol uzar ve kesirli işlemlerde hata yapma olasılığı artar.",
        ]},
        {"baslik": "Sayı problemleri", "icerik": [
            "Sayı problemlerinde bilinmeyen bir ya da birkaç sayıdır ve aralarındaki ilişki toplam, fark, kat ya da kesir olarak verilir.",
            ornek(
                "Ardışık üç tek sayının toplamı $87$ dir.",
                "Bu sayıları bulalım.",
                "Ardışık tek sayılar ikişer artar: en küçüğü $x$ ise diğerleri $x+2$ ve $x+4$ tür.",
                "$x+(x+2)+(x+4)=87$, yani $3x+6=87$ ve $x=27$.",
                "Sayılar $27$, $29$ ve $31$. Kontrol: toplamları $87$ dir."),
            ornek(
                "Bir sayının $\\dfrac{2}{3}$ si ile $\\dfrac{1}{4}$ i arasındaki fark $15$ tir.",
                "Sayıyı bulalım.",
                "Denklem: $\\dfrac{2}{3}x-\\dfrac{1}{4}x=15$.",
                "Paydaların EKOK'u $12$: $8x-3x=180$, yani $5x=180$ ve $x=36$.",
                "Kontrol: $36$ nın $\\dfrac{2}{3}$ si $24$, $\\dfrac{1}{4}$ i $9$ dur; $24-9=15$."),
            "Ardışık sayıların ayrıntısı <a href=\"/blog/ardisik-sayilar/\">Ardışık Sayılar</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Bilinmeyeni akıllıca seçmek: ortadaki terim", "icerik": [
            "Ardışık sayı sorularında bilinmeyeni ortadaki terime vermek denklemi daha da kısaltır. Ardışık tek sayıların ortadakine $x$ dersek diğerleri $x-2$ ve $x+2$ olur; toplamda $-2$ ile $+2$ birbirini götürür.",
            ornek(
                "Ardışık üç tek sayının toplamı $87$ dir.",
                "Bu kez ortadaki sayıya $x$ diyerek çözelim.",
                "Sayılar $x-2$, $x$ ve $x+2$: toplam $3x=87$.",
                "$x=29$; sayılar $27$, $29$ ve $31$."),
            "Bu, ardışık sayıların genel bir özelliğini de gösterir: tek sayıda ardışık terimin toplamı, ortadaki terim ile terim sayısının çarpımıdır. Bu yüzden toplam terim sayısına bölününce ortadaki terim doğrudan bulunur: $87:3=29$.",
            hap("Ardışık tek ya da çift sayılarda ortadakine $x$ denirse diğerleri $x-2$ ve $x+2$ olur; toplamda $-2$ ile $+2$ birbirini götürür."),
        ]},
        {"baslik": "Kurmadan önce tahmin etmek", "icerik": [
            "Denklemi kurmadan önce cevabın yaklaşık nerede olması gerektiğini düşünmek, yanlış kurulmuş bir denklemi fark etmenin en hızlı yoludur. Tahmin kaba olabilir; amaç yalnızca sonucun makul bir aralıkta olup olmadığını görmektir.",
            "Örneğin toplamı $48$ olan ve biri diğerinin $3$ katı olan iki sayıda küçük sayının $48$ in dörtte birine yakın olması gerekir, çünkü toplam dört eşit paya bölünüyor. Denklem $x=16$ ya da $x=24$ gibi bir sonuç verirse, kurulumda bir hata vardır. Aynı şekilde yaş sorularında bir kişinin yaşı negatif ya da yüzlerce yıl çıkarsa, cümlelerden biri yanlış çevrilmiştir.",
        ]},
        {"baslik": "Yaş problemleri", "icerik": [
            "Yaş problemlerinde zaman geçtikçe herkesin yaşı aynı miktarda artar. Bu yüzden iki kişinin yaş farkı hiç değişmez. Bilgileri \"şimdi\" ve \"sonra\" diye iki sütunlu bir tabloya yazmak, denklemi kurmayı kolaylaştırır.",
            ornek(
                "Bir annenin yaşı kızının yaşının $4$ katıdır. $6$ yıl sonra annenin yaşı kızının yaşının $3$ katı olacaktır.",
                "İkisinin bugünkü yaşlarını bulalım.",
                "Kızın yaşı $x$, annenin yaşı $4x$ olsun. $6$ yıl sonra yaşlar $x+6$ ve $4x+6$ olur.",
                "Denklem: $4x+6=3(x+6)$, yani $4x+6=3x+18$ ve $x=12$.",
                "Kız $12$, anne $48$ yaşındadır. Kontrol: $6$ yıl sonra $18$ ve $54$; $54=3 \\cdot 18$."),
            tablo(["", "Şimdi", "$6$ yıl sonra"], [
                ["Kız", "$x$", "$x+6$"],
                ["Anne", "$4x$", "$4x+6$"],
            ]),
            dikkat(
                "Süreyi yalnızca bir kişiye eklemek.",
                "Geçen $6$ yıl herkes için geçer. Annenin yaşına $6$ eklenip kızınkine eklenmezse denklem yanlış kurulur."),
        ]},
        {"baslik": "Para ve adet problemleri: tablo yöntemi", "icerik": [
            "Farklı değerlerdeki nesnelerin sayısı ve toplam değeri verildiğinde bilgileri bir tabloya yazmak en güvenli yoldur. Her satırda adet ile birim değer çarpılır ve toplam değer bulunur.",
            ornek(
                "Bir kasada yalnızca $5$ ve $10$ liralık banknotlardan toplam $30$ adet var ve kasadaki para $220$ lira.",
                "Her banknottan kaç tane olduğunu bulalım.",
                "$5$ liralıkların sayısı $x$ olsun; $10$ liralıklar $30-x$ tanedir.",
                "Toplam para: $5x+10(30-x)=220$, yani $5x+300-10x=220$.",
                "$-5x=-80$, yani $x=16$. $16$ tane $5$ liralık, $14$ tane $10$ liralık vardır. Kontrol: $80+140=220$."),
            tablo(["Banknot", "Adet", "Birim değer", "Toplam"], [
                ["$5$ lira", "$x$", "$5$", "$5x$"],
                ["$10$ lira", "$30-x$", "$10$", "$10(30-x)$"],
                ["Toplam", "$30$", "", "$220$"],
            ]),
            "Aynı tablo; bilet, ürün ya da puan sorularına da uygulanır. Satırlar değişir ama \"adet çarpı birim değer eşittir toplam\" ilişkisi aynı kalır.",
            hap("Cüzdanda yalnız $10$ ve $20$ liralık banknotlardan $20$ tane ve toplam $290$ lira varsa $10x+20(20-x)=290$ denklemi kurulur.", "$x=11$ bulunur: $11$ tane $10$ liralık, $9$ tane $20$ liralık banknot vardır.", gunluk=True),
        ]},
        {"baslik": "Geometri problemleri", "icerik": [
            "Şekillerin çevresi ve alanı da denklem kurmak için sık kullanılan ilişkilerdir. Kenarlardan biri $x$ seçilir, diğerleri $x$ cinsinden yazılır ve çevre ya da alan formülü denkleme dönüşür.",
            ornek(
                "Bir dikdörtgenin uzun kenarı kısa kenarından $4$ santimetre fazla ve çevresi $40$ santimetre.",
                "Kenar uzunluklarını ve alanını bulalım.",
                "Kısa kenar $x$, uzun kenar $x+4$ olsun. Çevre: $2(x+x+4)=40$.",
                "$4x+8=40$, yani $x=8$. Kenarlar $8$ ve $12$ santimetre.",
                "Alan: $8 \\cdot 12=96$ santimetrekare. Kontrol: $2 \\cdot (8+12)=40$."),
            ornek(
                "Bir karenin kenarı $3$ santimetre uzatılınca alanı $57$ santimetrekare artıyor.",
                "Karenin ilk kenar uzunluğunu bulalım.",
                "İlk kenar $x$ olsun. Alan farkı: $(x+3)^2-x^2=57$.",
                "Parantezi açalım: $x^2+6x+9-x^2=57$, yani $6x+9=57$ ve $x=8$.",
                "Kontrol: $11^2-8^2=121-64=57$."),
            "İkinci örnekte denklem ilk bakışta ikinci dereceden görünür, ama $x^2$ terimleri birbirini götürür ve geriye birinci dereceden bir denklem kalır.",
        ]},
        {"baslik": "Bilgileri listelemek: çok koşullu bir soru", "icerik": [
            "Uzun bir soruda bütün bilgileri tek seferde denkleme dökmeye çalışmak kafa karıştırır. Önce \"ne biliyorum?\" ve \"ne soruluyor?\" diye iki kısa liste yazmak, hangi bilginin nereye gideceğini netleştirir.",
            ornek(
                "Bir kırtasiyede bir defterin fiyatı bir kalemin fiyatının $3$ katıdır. $2$ defter ve $5$ kalem için toplam $110$ lira ödeniyor.",
                "Bir defterin ve bir kalemin fiyatını bulalım.",
                "Bilinenler: defter kalemin $3$ katı; $2$ defter ve $5$ kalem $110$ lira. Sorulan: iki fiyat.",
                "Kalem $x$ lira olsun; defter $3x$ lira olur. Denklem: $2 \\cdot 3x+5x=110$.",
                "$11x=110$, yani $x=10$. Kalem $10$ lira, defter $30$ lira. Kontrol: $60+50=110$."),
            "Listeyi yazmak ilk bakışta zaman kaybı gibi görünür ama uzun sorularda bir bilginin unutulmasını ya da iki kez kullanılmasını önler. Listedeki her bilgi, denklemde tam bir kez yer almalıdır.",
        ]},
        {"baslik": "Kesirli ifadelerle kurulan problemler", "icerik": [
            "\"Kalanın\" kelimesi geçen sorularda kesir, bütüne değil bir önceki adımdan geriye kalan miktara uygulanır. Bu ayrımı yapmak, kesir problemlerinin en önemli adımıdır.",
            ornek(
                "Bir öğrenci harçlığının üçte birini kitaba, kalan paranın dörtte birini yemeğe harcıyor ve geriye $300$ lirası kalıyor.",
                "Harçlığın tamamını bulalım.",
                "Harçlık $x$ olsun. Kitaptan sonra kalan: $x-\\dfrac{x}{3}=\\dfrac{2x}{3}$.",
                "Yemeğe giden: kalanın dörtte biri, yani $\\dfrac{2x}{3} \\cdot \\dfrac{1}{4}=\\dfrac{x}{6}$. Geriye kalan: $\\dfrac{2x}{3}-\\dfrac{x}{6}=\\dfrac{x}{2}$.",
                "$\\dfrac{x}{2}=300$, yani $x=600$ lira. Kontrol: kitap $200$, kalan $400$; yemek $100$, kalan $300$."),
            dikkat(
                "\"Kalanın\" kesrini bütüne uygulamak.",
                "Yemeğe harcanan para harçlığın dörtte biri değil, kitaptan sonra kalan paranın dörtte biridir. Bütüne uygulanırsa $150$ lira bulunur ve denklem yanlış kurulur."),
        ]},
        {"baslik": "Hız ve yüzde içeren kısa kurulumlar", "icerik": [
            "Hareket ve yüzde soruları da aynı mantıkla kurulur; yalnızca kullanılan ilişki değişir. Harekette yol hız ile zamanın çarpımıdır, yüzdede ise değişim bir çarpanla anlatılır.",
            ornek(
                "Aralarında $360$ kilometre olan iki şehirden iki araç aynı anda birbirine doğru yola çıkıyor. Hızları saatte $50$ ve $70$ kilometre.",
                "Kaç saat sonra karşılaşacaklarını bulalım.",
                "Geçen süre $t$ saat olsun. Karşılaştıklarında aldıkları yolların toplamı $360$ kilometredir: $50t+70t=360$.",
                "$120t=360$, yani $t=3$ saat. Kontrol: $150+210=360$."),
            ornek(
                "Bir ürüne yüzde $20$ zam yapıldıktan sonra fiyatı $540$ lira oluyor.",
                "Zamdan önceki fiyatı bulalım.",
                "Eski fiyat $x$ olsun. Yüzde $20$ zam, fiyatı $1.2$ ile çarpmaktır: $1.2x=540$.",
                "$x=450$ lira. Kontrol: $450 \\cdot 1.2=540$."),
            "Yüzde hesaplarının ayrıntısı <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a>, oranlı kurulumlar ise <a href=\"/blog/oran-ve-oranti-konu-anlatimi-pdf/\">Oran ve Orantı Konu Anlatımı PDF</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "İki bilinmeyenle kurmak", "icerik": [
            "Bazen iki niceliği iki ayrı harfle göstermek daha doğaldır. Bu durumda iki bilinmeyen için iki ayrı denklem kurulur ve sistem çözülür.",
            ornek(
                "Bir sınıfta $32$ öğrenci var ve kızların sayısı erkeklerin sayısından $6$ fazla.",
                "Kız ve erkek öğrenci sayılarını bulalım.",
                "Kızlar $k$, erkekler $e$ olsun: $k+e=32$ ve $k-e=6$.",
                "Denklemleri taraf tarafa toplayalım: $2k=38$, yani $k=19$ ve $e=13$.",
                "Kontrol: $19+13=32$ ve $19-13=6$."),
            "Aynı soru tek bilinmeyenle de kurulabilirdi: erkekler $e$, kızlar $e+6$ olsun; $2e+6=32$ ve $e=13$. İki yol aynı sonucu verir. Hangisinin seçileceği, problemdeki ilişkilerin hangi biçimde daha kolay yazıldığına bağlıdır.",
        ]},
        {"baslik": "Cevabı kontrol etmek ve anlamlandırmak", "icerik": [
            "Denklemi çözmek işin sonu değildir. Bulunan değer problemin bağlamına uymalı ve sorunun istediği nicelik yazılmalıdır.",
            "<ul><li><strong>Anlamlı mı?</strong> Kişi, banknot ya da kitap sayısı negatif ya da kesirli çıkamaz; böyle bir sonuç, denklemin yanlış kurulduğunu gösterir.</li>"
            "<li><strong>Sorulan bu mu?</strong> $x$ küçük sayıysa ve soru büyük sayıyı istiyorsa cevap $x$ değil, $3x$ tir.</li>"
            "<li><strong>Bütün koşullar sağlanıyor mu?</strong> Bulunan değeri sorudaki her cümlede dene; yalnızca kurduğun denklemde değil.</li></ul>",
            ornek(
                "Bir sayının $5$ fazlasının $2$ katı $26$ dır ve soruda bu sayının karesi isteniyor.",
                "Cevabı bulalım.",
                "Sayı $x$ olsun: $2(x+5)=26$, yani $x+5=13$ ve $x=8$.",
                "Soru sayının karesini istediği için cevap $8$ değil, $8^2=64$ tür."),
            hap("Bulunan değer problemin bağlamına uymalıdır: kişi ya da banknot sayısı negatif ya da kesirli çıkamaz."),
        ]},
        {"baslik": "Sınavda denklem kurma", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) problem sorularının büyük bölümü, bir cümleyi doğru denkleme çevirmeye dayanır: sayı, yaş, para, işçi, hareket ve karışım soruları bunun örnekleridir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de sayısal bölümün önemli bir kısmı denklem kurmayı gerektiren sözel problemlerden oluşur."),
            "Seçenekli sorularda seçenekleri denkleme koymak bazen denklemi çözmekten hızlıdır. Ama bu yol, denklem kurma becerisinin yerini tutmaz; seçeneklerin denenemeyeceği sorularda yine denklem gerekir.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["\"$4$ eksiğinin $3$ katı\" için $3x-4$ yazmak", "$3(x-4)$"],
                ["\"$7$ den farkı\" için $x-7$ yazmak", "$7-x$"],
                ["Yaş sorusunda süreyi tek kişiye eklemek", "Herkese aynı süre eklenir"],
                ["Ardışık tek sayıları $x$, $x+1$ diye yazmak", "$x$, $x+2$, $x+4$"],
                ["$x$ i bulup sorulanı yazmamak", "Sorulan niceliği hesapla"],
                ["Negatif ya da kesirli adedi kabul etmek", "Kurulumu yeniden kontrol et"],
            ]),
            "Bu hataların çoğu, soruyu okurken acele etmekten doğar. Denklemi kurduktan sonra her terimin cümlede neye karşılık geldiğini tek tek göstermek, hatayı çözümden önce yakalamayı sağlar.",
        ]},
    ],
    "sss": [
        ("Denklem kurma problemleri nasıl çözülür?",
         "Soru okunur, bilinmeyen seçilir, diğer nicelikler bu bilinmeyen cinsinden yazılır, cümledeki eşitlik denkleme çevrilir, denklem çözülür ve sonuç soruda denenir."),
        ("Bilinmeyeni nasıl seçmeliyim?",
         "Diğer niceliklerin en kolay ifade edilebildiği niceliği seç. Çoğu zaman bu, en küçük nicelik ya da başka niceliklerin katı olarak anlatılan niceliktir."),
        ("Fazlası ile farkı arasındaki fark nedir?",
         "Bir sayının yedi fazlası x artı yedidir. Yedinin bir sayıdan farkı ise yedi eksi x tir. Kelimelerin sırası işlemin sırasını belirler."),
        ("Yaş problemlerinde nelere dikkat edilir?",
         "Geçen süre herkesin yaşına eklenir ve yaş farkı değişmez. Bilgileri şimdi ve sonra sütunlarından oluşan bir tabloya yazmak kurulumu kolaylaştırır."),
        ("Tablo yöntemi ne zaman kullanılır?",
         "Farklı değerlerdeki nesnelerin sayısı ve toplam değeri verildiğinde kullanılır. Her satırda adet ile birim değer çarpılır ve toplam değere eşitlenir."),
        ("Bulduğum sonuç kesirli çıktıysa ne yapmalıyım?",
         "Kişi ya da nesne sayısı soruluyorsa kesirli sonuç, denklemin yanlış kurulduğunu gösterir. Cümleleri yeniden okuyup her terimin karşılığını kontrol et."),
        ("Kalanın kesri sorularında nasıl denklem kurulur?",
         "Her adımdan sonra geriye kalan miktar bilinmeyen cinsinden yazılır ve bir sonraki kesir bu kalana uygulanır. Kesri bütüne uygulamak en sık yapılan kurulum hatasıdır."),
        ("Hareket problemlerinde hangi ilişki kullanılır?",
         "Yol, hız ile zamanın çarpımıdır. Karşılıklı gelen araçlarda aldıkları yolların toplamı aradaki mesafeye eşittir."),
        ("Cevabı tahmin etmek neden işe yarar?",
         "Kaba bir tahmin, bulunan sonucun makul olup olmadığını hemen gösterir. Sonuç tahminden çok uzaksa denklem büyük olasılıkla yanlış kurulmuştur."),
        ("Seçenekleri denklemde denemek ne zaman işe yarar?",
         "Seçenekler az ve denklem uzunsa seçenekleri yerine koymak hızlı olabilir. Ama doğru denklemi kurmak yine şarttır; deneme yalnızca kurulmuş bir denklemi hızlı çözmenin yoludur."),
    ],
    "kontrol": [
        "Bir problemi beş adımda çözmenin sırasını açıklayabiliyorum.",
        "Fazlası, eksiği, katı ve farkı gibi ifadeleri doğru çevirebiliyorum.",
        "Kelimelerin sırasının işlemin sırasını belirlediğini biliyorum.",
        "Diğer niceliklerin kolayca yazılabildiği bilinmeyeni seçebiliyorum.",
        "Ardışık sayıları doğru biçimde ifade edebiliyorum.",
        "Yaş problemlerini şimdi ve sonra tablosuyla kurabiliyorum.",
        "Para ve adet problemlerini tablo yöntemiyle çözebiliyorum.",
        "Çevre ve alan bilgisinden denklem kurabiliyorum.",
        "Gerektiğinde iki bilinmeyenle iki denklem kurabiliyorum.",
        "Bulduğum cevabın anlamlı olup olmadığını ve sorulanı karşılayıp karşılamadığını kontrol edebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["birinci-dereceden-denklemler-konu-anlatimi-pdf", "cebirsel-ifadeler-konu-anlatimi-pdf", "sayi-problemleri-konu-anlatimi-pdf"],
}
