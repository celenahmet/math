# scripts/yazilar/98_tablo_grafik.py — Tablo ve Grafik Yorumlama (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, sutun_grafik, cizgi_grafik, daire_grafik  # noqa: E402

YAZI = {
    "slug": "tablo-ve-grafik-yorumlama",
    "baslik": "Tablo ve Grafik Yorumlama",
    "aciklama": "Tablo ve grafik nasıl okunur? Sıklık ve çift yönlü tablo, sütun, çizgi ve daire grafiği, artış yüzdesi, merkez açı ve yanıltıcı grafikler; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "veri",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "tablo-ve-grafik-yorumlama",
    "kapak_alt": "Tablo ve grafik yorumlama: renkli pullarla dolu bir tabla ve farklı yükseklikte blok sütunlarıyla veri karşılaştıran iki öğrenci",
    "ozet": "Tablo ve grafikler, çok sayıda veriyi bir bakışta okunabilir hâle getirir. Doğru okunduklarında karşılaştırmayı, değişimi ve dağılımı hemen gösterirler; yanlış okunduklarında ise insanı kolayca yanıltırlar. Bu yazıda sıklık tablosunu, çift yönlü tabloyu, sütun, çizgi ve daire grafiklerini, artış ve azalış yüzdesini, merkez açıyla sayı bulmayı, iki grafiği birlikte okumayı ve yanıltıcı grafikleri çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Veri, tablo ve grafik", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için yüzde hesabını ve oran kurmayı biliyor olman yeterli.",
                "Yüzde hesabı için <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a> yazısına göz at."),
            "Sayım, ölçüm ya da gözlemle elde edilen bilgilere <strong>veri</strong> denir. Bir sınıftaki öğrencilerin notları, bir mağazanın aylık satışları ya da bir şehrin günlük sıcaklıkları birer veri topluluğudur. Veriler ham hâlde bir sayı yığınıdır; tablo ve grafikler bu yığını düzenleyerek anlamlı hâle getirir.",
            "Tablo, verileri satır ve sütunlara yerleştirerek kesin değerleri gösterir. Grafik ise verileri şekillerle gösterir ve karşılaştırmayı, değişimi ya da bütünün parçalarını bir bakışta görmeyi sağlar. İyi bir okuyucu önce grafiğin neyi gösterdiğini, sonra hangi birimle gösterdiğini ve en son sayıların ne söylediğini sorar.",
            hap("Önce başlığı, eksenleri ve birimi oku.",
                "Sonra değerleri oku, en son yorum yap."),
        ]},
        {"baslik": "Sıklık tablosu", "icerik": [
            "Bir değerin veri içinde kaç kez görüldüğüne o değerin <strong>sıklığı</strong> denir. Değerleri ve sıklıklarını gösteren tabloya <strong>sıklık tablosu</strong> denir. Sıklığın toplama oranına ise <strong>bağıl sıklık</strong> denir ve çoğu zaman yüzde olarak yazılır.",
            tablo(["Not", "Öğrenci sayısı", "Yüzde"], [
                ["$1$", "$2$", "$\\%5$"],
                ["$2$", "$6$", "$\\%15$"],
                ["$3$", "$14$", "$\\%35$"],
                ["$4$", "$10$", "$\\%25$"],
                ["$5$", "$8$", "$\\%20$"],
                ["Toplam", "$40$", "$\\%100$"],
            ]),
            ornek(
                "Tabloda $40$ öğrencinin matematik notları veriliyor.",
                "Notu $4$ ve üstü olan öğrencilerin sayısını ve yüzdesini bulalım.",
                "Notu $4$ olan $10$, notu $5$ olan $8$ öğrenci var: $10+8=18$.",
                "Yüzde: $\\dfrac{18}{40} \\cdot 100=45$, yani $\\%45$. Tablodaki yüzdelerden de bulunur: $25+20=45$."),
            "Sıklık tablosu okunurken iki kontrol yapılmalıdır: sıklıkların toplamı veri sayısına, yüzdelerin toplamı da yüzde yüze eşit olmalıdır. Bu tabloda $2+6+14+10+8=40$ ve $5+15+35+25+20=100$ dür. En sık görülen not ise $3$ tür; bu değere verinin <strong>tepe değeri</strong> denir.",
        ]},
        {"baslik": "Çift yönlü tablo", "icerik": [
            "Veriler iki özelliğe göre birlikte sınıflandırıldığında <strong>çift yönlü tablo</strong> kullanılır. Satırlar bir özelliği, sütunlar diğer özelliği gösterir; kenarlardaki toplamlar da her özelliğin tek başına dağılımını verir.",
            tablo(["Sınıf", "Gözlüklü", "Gözlüksüz", "Toplam"], [
                ["$9$. sınıf", "$18$", "$62$", "$80$"],
                ["$10$. sınıf", "$12$", "$48$", "$60$"],
                ["Toplam", "$30$", "$110$", "$140$"],
            ]),
            ornek(
                "Tabloda bir okuldaki $140$ öğrencinin sınıfına ve gözlük kullanımına göre dağılımı veriliyor.",
                "Gözlüklülerin yüzde kaçının $9$. sınıfta olduğunu ve $10$. sınıfın yüzde kaçının gözlüklü olduğunu bulalım.",
                "Gözlüklüler içinde $9$. sınıf: $\\dfrac{18}{30} \\cdot 100=60$, yani $\\%60$.",
                "$10$. sınıf içinde gözlüklü: $\\dfrac{12}{60} \\cdot 100=20$, yani $\\%20$."),
            dikkat(
                "Yüzde sorusunda paydayı yanlış seçmek.",
                "\"Gözlüklülerin yüzde kaçı\" sorusunda payda gözlüklülerin toplamı olan $30$ dur. \"$9$. sınıfın yüzde kaçı\" sorusunda ise payda $9$. sınıfın toplamı olan $80$ dir. Sorudaki \"nın yüzde kaçı\" kalıbı, paydanın hangi grup olduğunu söyler."),
        ]},
        {"baslik": "Oranları karşılaştırmak", "icerik": [
            "Çift yönlü tablolarda en sık sorulan sorulardan biri, iki grupta bir özelliğin hangisinde daha yaygın olduğudur. Bu soruda sayılar değil oranlar karşılaştırılır, çünkü grupların büyüklükleri farklıdır.",
            ornek(
                "Gözlük tablosu verilsin.",
                "Gözlüklü öğrenci oranının hangi sınıfta daha yüksek olduğunu bulalım.",
                "$9$. sınıf: $\\dfrac{18}{80}=0.225$, yani $\\%22.5$.",
                "$10$. sınıf: $\\dfrac{12}{60}=0.2$, yani $\\%20$.",
                "Oran $9$. sınıfta daha yüksektir."),
            "Burada sayıları doğrudan karşılaştırmak da aynı sonucu verir; ama bu her zaman böyle değildir. Kalabalık bir grupta bir özelliğe sahip kişi sayısı fazla olabilir ama oranı düşük kalabilir. \"Hangi grupta daha çok\" ile \"hangi grupta daha yaygın\" farklı sorulardır.",
        ]},
        {"baslik": "Sütun grafiği", "icerik": [
            "<strong>Sütun grafiği</strong>, kategorileri yan yana sütunlarla gösterir; her sütunun yüksekliği o kategorinin değerine eşittir. Farklı kategorileri karşılaştırmak için en uygun grafiktir.",
            sutun_grafik("Bir kırtasiyenin ilk beş aydaki defter satışları (adet)", ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs"], [40, 50, 70, 56, 84], y_son=90, adim=15),
            ornek(
                "Grafikte bir kırtasiyenin ilk beş aydaki defter satışları veriliyor.",
                "Toplam satışı, aylık ortalamayı ve satışların azaldığı ayı bulalım.",
                "Toplam: $40+50+70+56+84=300$ defter.",
                "Aylık ortalama: $300:5=60$ defter.",
                "Satışlar yalnızca Mart ayından Nisan ayına geçerken azalmıştır: $70$ ten $56$ ya."),
            "Sütun grafiğinde değer, sütunun tepesinin karşısındaki eksen değeridir. Sütunların üzerine değer yazılmamışsa ızgara çizgilerinden yararlanılır; iki çizgi arasına düşen değerler ise ancak yaklaşık olarak okunabilir. Bu yüzden kesin hesap gereken yerde değerin grafikte yazılı olup olmadığına bakılmalıdır.",
        ]},
        {"baslik": "Artış ve azalış yüzdesi", "icerik": [
            "Grafik sorularının büyük bölümü değişimi sorar. Değişim iki biçimde ifade edilir: <strong>miktar</strong> olarak, yani yeni değerden eski değer çıkarılarak ya da <strong>yüzde</strong> olarak, yani bu farkın eski değere oranıyla.",
            "$$\\text{Değişim yüzdesi}=\\dfrac{\\text{yeni}-\\text{eski}}{\\text{eski}} \\cdot 100$$",
            ornek(
                "Defter satışı grafiği verilsin.",
                "Ocaktan Şubata, Marttan Nisana ve Nisandan Mayısa değişim yüzdelerini bulalım.",
                "Ocaktan Şubata: $\\dfrac{50-40}{40} \\cdot 100=25$; $\\%25$ artış.",
                "Marttan Nisana: $\\dfrac{56-70}{70} \\cdot 100=-20$; $\\%20$ azalış.",
                "Nisandan Mayısa: $\\dfrac{84-56}{56} \\cdot 100=50$; $\\%50$ artış."),
            dikkat(
                "Değişim yüzdesini yeni değere bölerek bulmak.",
                "Payda her zaman eski değerdir. $56$ dan $84$ e artış $\\%50$ dir; ama $84$ ten $56$ ya azalış $\\%50$ değil, yaklaşık $\\%33$ tür. Aynı fark, farklı başlangıç değerlerinde farklı yüzdelere karşılık gelir."),
        ]},
        {"baslik": "Miktar mı, yüzde mi?", "icerik": [
            "Bir grafikte en büyük artış sorulduğunda, sorunun miktarı mı yoksa yüzdeyi mi istediği dikkatle okunmalıdır. İkisi farklı cevaplar verebilir.",
            tablo(["Mağaza", "Geçen yıl", "Bu yıl", "Artış", "Artış yüzdesi"], [
                ["A", "$200$", "$240$", "$40$", "$\\%20$"],
                ["B", "$50$", "$75$", "$25$", "$\\%50$"],
            ]),
            "A mağazasının satışı miktar olarak daha çok, B mağazasınınki ise oran olarak daha çok artmıştır. Küçük bir başlangıç değeri, küçük bir artışla bile büyük bir yüzde üretebilir. Bu yüzden haberlerde ve reklamlarda verilen yüzdeler, başlangıç değeri bilinmeden yorumlanmamalıdır.",
        ]},
        {"baslik": "Çizgi grafiği", "icerik": [
            "<strong>Çizgi grafiği</strong>, bir büyüklüğün zaman içindeki değişimini gösterir. Noktalar ölçülen değerleri, noktaları birleştiren çizgiler ise değişimin yönünü gösterir: yükselen çizgi artışı, alçalan çizgi azalışı anlatır.",
            cizgi_grafik("Bir öğrencinin altı deneme sınavındaki netleri", ["1.", "2.", "3.", "4.", "5.", "6."], [40, 46, 44, 52, 58, 60], y_son=65, adim=5, y_bas=35),
            ornek(
                "Grafikte bir öğrencinin altı deneme sınavındaki netleri veriliyor.",
                "Netin düştüğü denemeyi, en büyük artışı ve ilk denemeden son denemeye değişim yüzdesini bulalım.",
                "Net yalnızca $2$. denemeden $3$. denemeye düşmüştür: $46$ dan $44$ e.",
                "En büyük artış $3$. denemeden $4$. denemeye olmuştur: $52-44=8$ net.",
                "İlk denemeden son denemeye: $\\dfrac{60-40}{40} \\cdot 100=50$; $\\%50$ artış."),
            "Bu grafikte düşey eksen $35$ ten başlar. Çizgi grafiklerinde bu yaygın bir tercihtir, çünkü amaç değişimin yönünü göstermektir; ama noktaların yüksekliklerini birbirine oranlamak bu yüzden yanlış olur. Eksenin nereden başladığı her zaman kontrol edilmelidir.",
        ]},
        {"baslik": "Çizginin eğimini yorumlamak", "icerik": [
            "Çizgi grafiğinde iki nokta arasındaki çizginin dikliği, değişimin hızını gösterir. Dik bir çizgi hızlı, yatık bir çizgi yavaş değişimi anlatır; yatay çizgi ise değişim olmadığını gösterir.",
            "Deneme grafiğinde $3$. ile $4$. deneme arasındaki çizgi en diktir, çünkü en büyük artış $8$ net ile bu aralıktadır. $5$. ile $6$. deneme arasındaki çizgi ise yatığa yakındır; artış yalnızca $2$ nettir. Net artmaya devam etse de artış hızı yavaşlamıştır.",
            "Grafikteki altı denemenin ortalaması $\\dfrac{40+46+44+52+58+60}{6}=50$ nettir. Son üç denemenin hepsi bu ortalamanın üzerindedir; bu da öğrencinin genel eğiliminin yükselişte olduğunu gösterir. Ortalamanın ayrıntısı <a href=\"/blog/aritmetik-ortalama-ve-veri-analizi/\">Aritmetik Ortalama ve Veri Analizi</a> yazısında.",
        ]},
        {"baslik": "Daire grafiği", "icerik": [
            "<strong>Daire grafiği</strong>, bir bütünün parçalara nasıl bölündüğünü gösterir. Dairenin tamamı $360$ derecedir ve her dilimin merkez açısı, o parçanın bütüne oranıyla orantılıdır:",
            "$$\\text{Merkez açı}=\\dfrac{\\text{parça}}{\\text{bütün}} \\cdot 360$$",
            daire_grafik("Bir okuldaki 240 öğrencinin okula geliş biçimi (merkez açılar)", [("Otobüs: 120°", 120), ("Yürüyerek: 90°", 90), ("Servis: 60°", 60), ("Özel araç: 60°", 60), ("Bisiklet: 30°", 30)]),
            ornek(
                "Grafikte bir okuldaki $240$ öğrencinin okula geliş biçimi veriliyor.",
                "Otobüsle ve yürüyerek gelen öğrenci sayılarını bulalım.",
                "Otobüs: $\\dfrac{120}{360} \\cdot 240=80$ öğrenci.",
                "Yürüyerek: $\\dfrac{90}{360} \\cdot 240=60$ öğrenci; bu, bütünün $\\%25$ idir."),
            "Bütün dilimler için aynı hesap yapılırsa otobüs $80$, yürüyerek $60$, servis $40$, özel araç $40$ ve bisiklet $20$ öğrenci bulunur. Toplam $240$ tır; bu, hesabın doğru yapıldığını gösterir.",
        ]},
        {"baslik": "Açıdan sayıya, sayıdan açıya", "icerik": [
            "Daire grafiği sorularında üç büyüklük vardır: dilimin açısı, dilimin temsil ettiği sayı ve bütünün sayısı. İkisi bilinirse üçüncüsü orantıyla bulunur.",
            ornek(
                "Aynı grafikte servisle gelen öğrenci sayısı $40$ tır.",
                "Servis diliminin merkez açısını bulalım.",
                "$\\dfrac{40}{240} \\cdot 360=60$ derece."),
            ornek(
                "Bir daire grafiğinde bisiklet diliminin açısı $30$ derece ve bisikletle gelen öğrenci sayısı $20$ dir.",
                "Toplam öğrenci sayısını bulalım.",
                "$30$ derece $20$ öğrenciye karşılık geliyorsa $360$ derece bunun $12$ katıdır.",
                "Toplam: $20 \\cdot 12=240$ öğrenci."),
            hap("Merkez açı, parçanın bütüne oranının $360$ ile çarpımıdır.",
                "Bir derecenin kaç kişiye karşılık geldiğini bulmak çoğu soruyu tek adıma indirir."),
        ]},
        {"baslik": "Dilimler arasındaki fark", "icerik": [
            "İki dilim arasındaki fark sorulduğunda dilimleri ayrı ayrı hesaplamaya gerek yoktur. Açıların farkı bulunur ve bu fark sayıya çevrilir.",
            ornek(
                "Okula geliş grafiği verilsin.",
                "Otobüsle gelenlerin yürüyerek gelenlerden kaç fazla olduğunu bulalım.",
                "Açı farkı: $120-90=30$ derece.",
                "Sayı farkı: $\\dfrac{30}{360} \\cdot 240=20$ öğrenci. Kontrol: $80-60=20$."),
            "Bu grafikte her $3$ derece $2$ öğrenciye karşılık gelir, çünkü $240$ öğrenci $360$ dereceye yayılmıştır. Böyle bir çevirme katsayısı bulunduğunda bütün dilimler zihinden hesaplanabilir.",
        ]},
        {"baslik": "Resim grafiği", "icerik": [
            "<strong>Resim grafiği</strong>, değerleri tekrarlanan sembollerle gösterir. Her sembolün kaç birime karşılık geldiği grafiğin yanında belirtilir; yarım sembol bu değerin yarısıdır.",
            tablo(["Gün", "Ödünç verilen kitap (● = $10$ kitap)"], [
                ["Pazartesi", "● ● ●"],
                ["Salı", "● ● ● ◐"],
                ["Çarşamba", "● ●"],
                ["Perşembe", "● ● ● ● ●"],
                ["Cuma", "● ● ● ● ◐"],
            ]),
            ornek(
                "Tabloda bir kütüphanenin haftanın beş gününde ödünç verdiği kitaplar sembollerle gösteriliyor.",
                "Her günün kitap sayısını ve haftalık toplamı bulalım.",
                "Pazartesi $30$, Salı $35$, Çarşamba $20$, Perşembe $50$, Cuma $45$.",
                "Toplam: $30+35+20+50+45=180$ kitap."),
            "Resim grafiğinde en sık yapılan hata, sembollerin sayısını değer sanmaktır. Perşembe günü $5$ sembol vardır ama ödünç verilen kitap sayısı $50$ dir.",
        ]},
        {"baslik": "Gruplanmış veriler", "icerik": [
            "Veri çok sayıda farklı değer içerdiğinde değerler aralıklara ayrılarak gruplanır. Her aralıktaki veri sayısı tabloyla ya da bitişik sütunlardan oluşan bir <strong>histogramla</strong> gösterilir.",
            sutun_grafik("30 öğrencinin boy uzunlukları (santimetre aralıkları)", ["150-159", "160-169", "170-179", "180-189"], [4, 12, 10, 4], y_son=14, adim=2),
            ornek(
                "Grafikte $30$ öğrencinin boy uzunlukları aralıklara göre veriliyor.",
                "Boyu $170$ santimetre ve üstünde olan öğrenci sayısını ve en kalabalık aralığı bulalım.",
                "$170$ ve üstü: $10+4=14$ öğrenci.",
                "En kalabalık aralık $12$ öğrenciyle $160$ ile $169$ arasıdır."),
            dikkat(
                "Gruplanmış veriden kesin değer çıkarmaya çalışmak.",
                "Grafik, boyu tam olarak $165$ santimetre olan öğrenci sayısını söylemez; yalnızca $160$ ile $169$ arasında $12$ öğrenci olduğunu söyler. Gruplama bilgiyi özetler ama ayrıntıyı kaybettirir."),
        ]},
        {"baslik": "İki grafiği birlikte okumak", "icerik": [
            "<strong>ALES</strong> ve <strong>KPSS</strong> gibi sınavlarda iki grafik birlikte verilebilir: biri toplam değeri, diğeri bu toplamın dağılımını gösterir. Bu sorularda önce toplam bulunur, sonra dağılım bu toplama uygulanır.",
            sutun_grafik("Bir şirketin yıllık bütçesi (bin TL)", ["2023", "2024", "2025"], [200, 250, 300], y_son=300, adim=50),
            daire_grafik("2025 bütçesinin dağılımı (merkez açılar)", [("Personel: 144°", 144), ("Malzeme: 90°", 90), ("Kira: 72°", 72), ("Diğer: 54°", 54)]),
            ornek(
                "Grafiklerde bir şirketin üç yıllık bütçesi ve 2025 bütçesinin giderlere dağılımı veriliyor.",
                "2025 yılında personele ve malzemeye ayrılan tutarları ve bütçenin 2023 ile 2025 arasındaki artış yüzdesini bulalım.",
                "Personel: $\\dfrac{144}{360} \\cdot 300=120$ bin TL.",
                "Malzeme: $\\dfrac{90}{360} \\cdot 300=75$ bin TL.",
                "Bütçe artışı: $\\dfrac{300-200}{200} \\cdot 100=50$; $\\%50$ artış."),
            "Daire grafiği yalnızca 2025 yılına aittir; 2023 ya da 2024 yılının dağılımı hakkında bir şey söylemez. İki grafiği birlikte okurken her grafiğin hangi yılı ya da hangi grubu anlattığını ayrı ayrı belirlemek gerekir.",
        ]},
        {"baslik": "Hangi grafik ne zaman kullanılır?", "icerik": [
            "Her grafik türü belirli bir soruyu yanıtlamak için uygundur. Veriyi gösterecek grafiği seçerken verinin hangi özelliğinin öne çıkarılacağına bakılır.",
            tablo(["Amaç", "Uygun gösterim"], [
                ["Kategorileri karşılaştırmak", "Sütun grafiği"],
                ["Zaman içindeki değişimi göstermek", "Çizgi grafiği"],
                ["Bütünün parçalarını göstermek", "Daire grafiği"],
                ["Aralıklara bölünmüş sayısal veri", "Histogram"],
                ["İki özelliğe göre sayım", "Çift yönlü tablo"],
                ["Kesin değerleri vermek", "Tablo"],
            ]),
            "Bir grafiğin yanlış seçilmesi, verinin anlattığı hikâyeyi gizleyebilir. Örneğin aylık satışları daire grafiğiyle göstermek ayların sırasını ve değişimin yönünü kaybettirir; aynı veri çizgi ya da sütun grafiğinde çok daha açık okunur.",
        ]},
        {"baslik": "Yanıltıcı grafikler", "icerik": [
            "Grafikler doğru verilerle bile yanlış izlenim yaratabilir. En yaygın yöntem, düşey ekseni sıfırdan değil daha büyük bir değerden başlatmaktır. Aşağıdaki iki grafik aynı veriyi gösterir.",
            sutun_grafik("Eksen sıfırdan başlıyor", ["A", "B"], [96, 100], y_son=100, adim=20),
            sutun_grafik("Eksen 94 ten başlıyor", ["A", "B"], [96, 100], y_son=100, adim=2, y_bas=94),
            "İkinci grafikte B sütunu A sütununun üç katı yükseklikte görünür, çünkü sütunların görünen boyları $96-94=2$ ve $100-94=6$ birimdir. Gerçekte B, A dan yalnızca $4$ birim, yani yaklaşık $\\%4$ fazladır. Birinci grafik bu küçük farkı doğru gösterir.",
            dikkat(
                "Sütun boylarını oranlayarak karşılaştırmak.",
                "Sütun boyları ancak eksen sıfırdan başlıyorsa değerlerle orantılıdır. Eksen kesikse değerler eksenden okunup öyle karşılaştırılmalıdır."),
        ]},
        {"baslik": "Grafik neyi söylemez?", "icerik": [
            "Bir grafik yalnızca gösterdiği veriyi anlatır. İki büyüklüğün birlikte artması, birinin diğerine neden olduğunu göstermez. Dondurma satışları ile boğulma olaylarının yaz aylarında birlikte artması, dondurmanın boğulmaya yol açtığı anlamına gelmez; ikisini de sıcak hava artırır.",
            "Benzer biçimde, grafikte gösterilmeyen dönemler hakkında kesin yargıya varılamaz. Deneme grafiğindeki öğrencinin yedinci denemede de netini artıracağı kesin değildir; grafik yalnızca bir eğilim gösterir. Sınav sorularında \"kesinlikle doğrudur\" ile \"doğru olabilir\" arasındaki fark çoğu zaman bu noktada ortaya çıkar.",
        ]},
        {"baslik": "Sınavda tablo ve grafik", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) tablo ve grafik soruları sütun, çizgi ve daire grafiklerini okumayı, yüzde ve oran hesaplamayı gerektirir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde ise birlikte verilen iki grafikten birkaç sorunun üretildiği soru setleri de karşına çıkabilir."),
            "Grafik sorularında zaman kazanmanın yolu, soruları okumadan önce grafiğe kısa bir bakış atmaktır: başlık, eksenler, birim ve toplam. Sonra her soruda yalnızca gereken değerler okunur. Daire grafiğinde bir derecenin kaç birime karşılık geldiğini baştan bulmak, bütün sorularda işe yarar.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Birimi okumamak", "Bin TL, adet, yüzde ayrı birimlerdir"],
                ["Yüzde sorusunda yanlış payda", "\"Kimin yüzde kaçı\" paydayı belirler"],
                ["Artış yüzdesini yeni değere bölmek", "Eski değere bölünür"],
                ["Kesik eksende boyları oranlamak", "Değerler eksenden okunur"],
                ["Daire grafiğinde açıyı yüzde sanmak", "Yüzde, açının $360$ a oranıdır"],
                ["Birlikte artışı neden sonuç sanmak", "Grafik nedeni göstermez"],
            ]),
            "Bu hataların çoğu grafiğe acele bakmaktan doğar. Başlığı, eksenleri ve birimi okumak birkaç saniye sürer ama yanlış okunan bir değerle çözülen bütün soruların kaybedilmesini önler.",
        ]},
    ],
    "sss": [
        ("Tablo ve grafik arasındaki fark nedir?",
         "Tablo kesin değerleri satır ve sütunlarda verir. Grafik ise verileri şekillerle gösterir ve karşılaştırmayı ya da değişimi bir bakışta görmeyi sağlar."),
        ("Sütun grafiği ne zaman kullanılır?",
         "Farklı kategorilerin değerlerini karşılaştırmak için kullanılır. Her sütunun yüksekliği o kategorinin değerini gösterir."),
        ("Daire grafiğinde merkez açı nasıl bulunur?",
         "Parçanın bütüne oranı 360 ile çarpılır. Bütünün dörtte biri olan bir parçanın merkez açısı 90 derecedir."),
        ("Artış yüzdesi nasıl hesaplanır?",
         "Yeni değerden eski değer çıkarılır, fark eski değere bölünür ve 100 ile çarpılır. 40 tan 50 ye artış yüzde 25 tir."),
        ("Çizgi grafiği neyi gösterir?",
         "Bir büyüklüğün zaman içindeki değişimini gösterir. Yükselen çizgi artışı, alçalan çizgi azalışı, çizginin dikliği de değişimin hızını anlatır."),
        ("Grafikler nasıl yanıltıcı olabilir?",
         "En yaygın yöntem, düşey ekseni sıfırdan başlatmamaktır. Bu durumda küçük farklar sütun boylarında çok büyük görünür."),
    ],
    "kontrol": [
        "Bir grafiğin başlığını, eksenlerini ve birimini okuyabiliyorum.",
        "Sıklık tablosunda sıklık ve yüzde hesaplayabiliyorum.",
        "Çift yönlü tabloda doğru paydayı seçebiliyorum.",
        "Farklı büyüklükteki grupları oranlarla karşılaştırabiliyorum.",
        "Sütun grafiğinden değer okuyup toplam ve ortalama bulabiliyorum.",
        "Artış ve azalış yüzdesini eski değere göre hesaplayabiliyorum.",
        "Çizgi grafiğinde değişimin yönünü ve hızını yorumlayabiliyorum.",
        "Daire grafiğinde açıdan sayıya ve sayıdan açıya geçebiliyorum.",
        "İki grafiği birlikte okuyarak soru çözebiliyorum.",
        "Kesik eksenli yanıltıcı grafikleri fark edebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["aritmetik-ortalama-ve-veri-analizi", "yuzdeler-konu-anlatimi-pdf", "oran-ve-oranti-problemleri"],
}
