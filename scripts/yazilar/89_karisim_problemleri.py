# scripts/yazilar/89_karisim_problemleri.py — Karisim Problemleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "karisim-problemleri-konu-anlatimi-pdf",
    "baslik": "Karışım Problemleri Konu Anlatımı PDF",
    "aciklama": "Karışım problemleri nasıl çözülür? Madde miktarı, madde ve su ekleme, buharlaştırma, iki karışımı birleştirme, çapraz yöntem, alaşım ve fiyat; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "karisim-problemleri-konu-anlatimi-pdf",
    "kapak_alt": "Karışım problemleri: şeffaf kaplarda mavi ve turuncu boncukları farklı oranlarda karıştıran öğrenci",
    "ozet": "Karışım problemleri, bir maddenin karışım içindeki oranının nasıl değiştiğini konu alır: tuzlu su, şekerli su, alaşım ya da farklı fiyatlı ürünlerin karışımı. Bu problemlerin hepsi tek bir ilkeye dayanır: karışıma dışarıdan eklenmedikçe ya da çıkarılmadıkça maddenin miktarı değişmez. Bu yazıda madde miktarını, madde ve su eklemeyi, buharlaştırmayı, iki karışımı birleştirmeyi, istenen orana ulaşmayı, çapraz yöntemi, karışımdan alıp yerine su koymayı, alaşımları ve fiyat karışımlarını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Temel ilke: madde miktarı", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için yüzde hesaplarını ve birinci dereceden denklem kurmayı biliyor olman yeterli.",
                "Yüzdenin temeli için <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a>, soru türleri için <a href=\"/blog/yuzde-problemleri-nasil-cozulur/\">Yüzde Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "Bir karışımda bir maddenin oranı, o maddenin miktarının karışımın toplam miktarına bölümüdür. \"Yüzde $15$ lik tuzlu su\" demek, karışımın yüzde $15$ inin tuz, geri kalanının su olduğu demektir. Bu tanımdan karışım problemlerinin temel eşitliği çıkar:",
            "$$\\text{Madde miktarı}=\\text{Karışım miktarı} \\cdot \\text{Oran}$$",
            "Karışım problemlerinin anahtarı şu gözlemdir: karışıma o maddeden eklenmedikçe ya da karışımdan o madde çıkarılmadıkça <strong>maddenin miktarı değişmez</strong>. Su eklemek ya da suyu buharlaştırmak tuzun miktarını değiştirmez; yalnızca toplam miktarı ve dolayısıyla oranı değiştirir.",
            hap("Madde miktarı, karışım miktarı ile oranın çarpımıdır.",
                "Madde eklenmedikçe ya da çıkarılmadıkça madde miktarı değişmez."),
        ]},
        {"baslik": "Oran mı, yüzde mi?", "icerik": [
            "Karışım sorularında iki farklı ifade karıştırılabilir. \"Tuzun suya oranı\" tuzu suyla karşılaştırır; \"tuz yüzdesi\" ise tuzu bütün karışımla karşılaştırır. İkisi aynı şey değildir.",
            ornek(
                "Bir karışımda tuzun suya oranı $1:4$ tür.",
                "Karışımın tuz yüzdesini bulalım.",
                "Tuz $1$ pay, su $4$ pay; karışımın tamamı $5$ paydır.",
                "Tuz yüzdesi: $\\dfrac{1}{5}=0.2$, yani yüzde $20$; yüzde $25$ değil."),
            dikkat(
                "Madde ile su oranını madde yüzdesi sanmak.",
                "Oran $1:4$ ise $\\dfrac{1}{4}$ tuzun suya oranıdır. Yüzde için bölünen sayı karışımın tamamı olmalıdır: $1+4=5$."),
        ]},
        {"baslik": "Tablo yöntemi", "icerik": [
            "Karışım sorularında bilgileri bir tabloya yazmak hataları önler. Her satır bir karışımı, sütunlar ise toplam miktarı, oranı ve madde miktarını gösterir. Son satır, karışımların birleşimidir: toplam miktarlar ve madde miktarları toplanır, oran ise en son hesaplanır.",
            tablo(["Karışım", "Toplam miktar", "Oran", "Madde miktarı"], [
                ["Birinci", "$m_1$", "$o_1$", "$m_1 \\cdot o_1$"],
                ["İkinci", "$m_2$", "$o_2$", "$m_2 \\cdot o_2$"],
                ["Birleşim", "$m_1+m_2$", "?", "$m_1 \\cdot o_1+m_2 \\cdot o_2$"],
            ]),
            dikkat(
                "Oranları toplamak.",
                "Tabloda toplanan sütunlar miktarlardır; oranlar toplanmaz. Yeni oran, toplam madde miktarının toplam karışım miktarına bölünmesiyle bulunur."),
        ]},
        {"baslik": "Madde eklemek", "icerik": [
            "Karışıma aynı maddeden saf olarak eklendiğinde hem madde miktarı hem de toplam miktar eklenen kadar artar. Madde miktarı da toplam miktar da aynı sayıda gram artar; ama bu artış madde miktarına göre çok daha büyük bir pay olduğu için oran büyür. Eklenen madde ne kadar çok olursa oran o kadar büyür ama hiçbir zaman yüzde $100$ e ulaşmaz.",
            ornek(
                "$300$ gram yüzde $20$ lik şekerli suya $100$ gram şeker ekleniyor.",
                "Yeni şeker oranını bulalım.",
                "Başlangıçtaki şeker: $300 \\cdot 0.2=60$ gram.",
                "Yeni şeker $60+100=160$ gram, yeni toplam $300+100=400$ gram.",
                "Yeni oran: $\\dfrac{160}{400}=0.4$, yani yüzde $40$."),
            "Soru tersine de sorulabilir: aynı şekerli suyun yüzde $40$ lık olması için kaç gram şeker eklenmeli? Eklenen şeker $x$ gram ise $60+x=0.4(300+x)$ olmalıdır. Buradan $60+x=120+0.4x$, yani $0.6x=60$ ve $x=100$ gram bulunur. Saf madde eklenirken bilinmeyen hem madde miktarına hem de toplam miktara eklenir.",
        ]},
        {"baslik": "Su eklemek: seyreltme", "icerik": [
            "Karışıma su eklendiğinde madde miktarı değişmez, toplam miktar artar. Bu yüzden oran küçülür. Bu işleme seyreltme denir. Ne kadar su eklenirse eklensin oran sıfıra yaklaşır ama sıfır olmaz, çünkü madde karışımda kalmaya devam eder.",
            ornek(
                "$400$ gram yüzde $30$ luk tuzlu suya $200$ gram su ekleniyor.",
                "Yeni tuz oranını bulalım.",
                "Tuz: $400 \\cdot 0.3=120$ gram; değişmez.",
                "Yeni toplam: $400+200=600$ gram.",
                "Yeni oran: $\\dfrac{120}{600}=0.2$, yani yüzde $20$."),
            "Aynı soru tersine de sorulabilir: $400$ gram yüzde $30$ luk tuzlu suyu yüzde $20$ lik yapmak için kaç gram su eklenmeli? Tuz $120$ gram kalır ve yeni karışımın yüzde $20$ si olmalıdır: $120:0.2=600$ gram. Eklenecek su $600-400=200$ gramdır.",
        ]},
        {"baslik": "Su buharlaştırmak: derişikleştirme", "icerik": [
            "Karışımdaki suyun bir kısmı buharlaştırıldığında madde miktarı yine değişmez ama toplam miktar azalır. Bu yüzden oran büyür.",
            ornek(
                "$500$ gram yüzde $12$ lik tuzlu sudan $200$ gram su buharlaştırılıyor.",
                "Yeni tuz oranını bulalım.",
                "Tuz: $500 \\cdot 0.12=60$ gram; değişmez.",
                "Yeni toplam: $500-200=300$ gram.",
                "Yeni oran: $\\dfrac{60}{300}=0.2$, yani yüzde $20$."),
            dikkat(
                "Buharlaşan suyla tuzu da azaltmak.",
                "Buharlaşan yalnızca sudur; tuz karışımda kalır. Tuz miktarını buharlaşan oranda azaltmak, oranın değişmediği yanlış bir sonuç verir."),
        ]},
        {"baslik": "İki karışımı birleştirmek", "icerik": [
            "İki karışım birleştirildiğinde madde miktarları toplanır, toplam miktarlar toplanır ve yeni oran bu iki toplamın bölümüdür. Yeni oran her zaman iki oranın arasında kalır ve miktarı fazla olan karışımın oranına daha yakındır.",
            ornek(
                "$200$ gram yüzde $10$ luk tuzlu su ile $300$ gram yüzde $25$ lik tuzlu su karıştırılıyor.",
                "Yeni karışımın tuz oranını bulalım.",
                "Tuz miktarları: $200 \\cdot 0.1=20$ gram ve $300 \\cdot 0.25=75$ gram. Toplam tuz $95$ gram.",
                "Toplam karışım: $200+300=500$ gram.",
                "Yeni oran: $\\dfrac{95}{500}=0.19$, yani yüzde $19$."),
            "Sonuç yüzde $10$ ile yüzde $25$ arasındadır ve miktarı daha fazla olan ikinci karışımın oranına daha yakındır. İki oranın basit ortalaması olan yüzde $17.5$, yalnızca miktarlar eşitse doğru olurdu.",
        ]},
        {"baslik": "Üç karışımı birleştirmek", "icerik": [
            "İkiden fazla karışım birleştirildiğinde de yöntem değişmez: bütün madde miktarları ve bütün toplam miktarlar ayrı ayrı toplanır, sonra bölünür.",
            ornek(
                "$100$ gram yüzde $10$ luk, $200$ gram yüzde $20$ lik ve $200$ gram yüzde $35$ lik tuzlu su karıştırılıyor.",
                "Yeni karışımın tuz oranını bulalım.",
                "Tuz miktarları: $10$, $40$ ve $70$ gram; toplam $120$ gram.",
                "Toplam karışım: $100+200+200=500$ gram.",
                "Yeni oran: $\\dfrac{120}{500}=0.24$, yani yüzde $24$."),
        ]},
        {"baslik": "Buharlaştırarak istenen orana ulaşmak", "icerik": [
            "Bir karışımın oranını artırmak için ne kadar su buharlaştırılması gerektiği sorulduğunda, madde miktarının değişmediği bilgisinden yararlanılır. Madde miktarı istenen orana bölünerek yeni toplam bulunur; buharlaşan su, eski ve yeni toplamın farkıdır.",
            ornek(
                "$600$ gram yüzde $15$ lik tuzlu su var.",
                "Karışımın yüzde $25$ lik olması için kaç gram su buharlaştırılması gerektiğini bulalım.",
                "Tuz: $600 \\cdot 0.15=90$ gram; değişmez.",
                "Yeni toplam: $90:0.25=360$ gram.",
                "Buharlaşması gereken su: $600-360=240$ gram."),
        ]},
        {"baslik": "Hem madde hem su eklemek", "icerik": [
            "Karışıma aynı anda hem madde hem su eklendiğinde madde miktarı yalnızca eklenen madde kadar, toplam miktar ise eklenen madde ile suyun toplamı kadar artar.",
            ornek(
                "$200$ gram yüzde $20$ lik şekerli suya $50$ gram şeker ve $50$ gram su ekleniyor.",
                "Yeni şeker oranını bulalım.",
                "Başlangıçtaki şeker $40$ gram; yeni şeker $40+50=90$ gram.",
                "Yeni toplam: $200+50+50=300$ gram.",
                "Yeni oran: $\\dfrac{90}{300}=0.3$, yani yüzde $30$."),
            "Eklenen kısım kendi başına bir karışım gibi düşünülebilir: $50$ gram şeker ve $50$ gram su, $100$ gramlık yüzde $50$ lik bir şekerli sudur. Soru böylece iki karışımı birleştirme sorusuna dönüşür.",
        ]},
        {"baslik": "İstenen orana ulaşmak", "icerik": [
            "Bir karışıma başka bir karışımdan ne kadar eklenmesi gerektiği sorulduğunda eklenecek miktara $x$ denir. Madde miktarlarının toplamı, yeni karışımın istenen orandaki madde miktarına eşitlenir.",
            ornek(
                "$300$ gram yüzde $10$ luk tuzlu suya yüzde $40$ lık tuzlu su ekleniyor.",
                "Karışımın yüzde $20$ lik olması için kaç gram eklenmesi gerektiğini bulalım.",
                "Eklenecek miktar $x$ gram olsun. Tuz: $300 \\cdot 0.1+0.4x=30+0.4x$.",
                "Yeni karışım $300+x$ gram ve yüzde $20$ tuzlu: $30+0.4x=0.2(300+x)$.",
                "$30+0.4x=60+0.2x$, yani $0.2x=30$ ve $x=150$ gram. Kontrol: $\\dfrac{30+60}{450}=0.2$."),
        ]},
        {"baslik": "Çapraz yöntem", "icerik": [
            "İki karışım birleştirilip belirli bir orana ulaşılmak istendiğinde, karıştırılacak miktarların oranı çapraz yöntemle hızlıca bulunur. Hedef oranın iki orana olan uzaklıkları hesaplanır; miktarlar bu uzaklıklarla <strong>ters orantılıdır</strong>.",
            ornek(
                "Yüzde $10$ luk ve yüzde $40$ lık iki tuzlu su karıştırılarak yüzde $20$ lik tuzlu su elde edilecek.",
                "İki karışımın hangi oranda karıştırılması gerektiğini bulalım.",
                "Hedefin yüzde $10$ a uzaklığı $10$, yüzde $40$ a uzaklığı $20$ dir.",
                "Miktarlar uzaklıklarla ters orantılı: yüzde $10$ luktan $20$, yüzde $40$ lıktan $10$ pay; yani $2:1$.",
                "Önceki örnekte $300$ gram yüzde $10$ luğa $150$ gram yüzde $40$ lık eklenmesi de tam bu $2:1$ oranıdır."),
            "Çapraz yöntemin mantığı bir teraziye benzer: hedef oran destek noktasıdır ve hedefe daha yakın olan karışımdan daha fazla kullanılır. Hedef bir orana ne kadar yakınsa o karışımın ağırlığı o kadar büyüktür.",
        ]},
        {"baslik": "Karışımdan alıp yerine su koymak", "icerik": [
            "Bir karışımdan bir miktar alınıp yerine aynı miktarda su konduğunda toplam miktar değişmez, madde miktarı ise alınan karışımdaki madde kadar azalır.",
            ornek(
                "$40$ litre yüzde $50$ alkollü bir karışımdan $10$ litre alınıp yerine $10$ litre su konuyor.",
                "Yeni karışımın alkol oranını bulalım.",
                "Başlangıçtaki alkol: $40 \\cdot 0.5=20$ litre.",
                "Alınan $10$ litrede $10 \\cdot 0.5=5$ litre alkol vardır; kalan alkol $15$ litre.",
                "Toplam yine $40$ litre; yeni oran $\\dfrac{15}{40}=0.375$, yani yüzde $37.5$."),
            "Bu işlem aynı biçimde tekrar edilirse her seferinde alkol miktarı aynı oranla azalır. Burada her işlemde alkolün dörtte biri gider ve dörtte üçü kalır; ikinci işlemden sonra alkol $15 \\cdot \\dfrac{3}{4}=11.25$ litre olur.",
        ]},
        {"baslik": "Alaşım problemleri", "icerik": [
            "Metal karışımlarına alaşım denir ve oran çoğu zaman ayar ya da yüzde olarak verilir. Alaşım soruları da tuzlu su sorularıyla aynı mantıkla çözülür: tuzun yerini saf metal, suyun yerini diğer metaller alır. Altında saf altın $24$ ayar kabul edilir; $18$ ayar altın, kütlesinin $\\dfrac{18}{24}=\\dfrac{3}{4}$ ü saf altın olan alaşımdır.",
            ornek(
                "$60$ gram $18$ ayar altına saf altın eklenerek $22$ ayar altın elde edilecek.",
                "Kaç gram saf altın eklenmesi gerektiğini bulalım.",
                "$60$ gramdaki saf altın: $60 \\cdot \\dfrac{18}{24}=45$ gram.",
                "Eklenen saf altın $x$ gram olsun. Yeni alaşım $22$ ayar: $45+x=\\dfrac{22}{24}(60+x)$.",
                "$45+x=55+\\dfrac{11}{12}x$, yani $\\dfrac{x}{12}=10$ ve $x=120$ gram. Kontrol: $\\dfrac{165}{180}=\\dfrac{11}{12}=\\dfrac{22}{24}$."),
        ]},
        {"baslik": "Fiyat karışımları", "icerik": [
            "Farklı fiyatlı ürünler karıştırıldığında karışımın birim fiyatı, toplam tutarın toplam miktara bölümüdür. Bu problemler de karışım problemleriyle aynı yapıdadır: \"madde miktarı\" yerine toplam tutar kullanılır. Karışımın birim fiyatı, tıpkı karışım oranı gibi, her zaman iki fiyatın arasında kalır.",
            ornek(
                "Kilosu $40$ lira ve $70$ lira olan iki çay karıştırılarak kilosu $50$ liradan $30$ kilogram karışım hazırlanacak.",
                "Her çaydan kaç kilogram kullanılması gerektiğini bulalım.",
                "Ucuz çaydan $a$, pahalı çaydan $30-a$ kilogram kullanılsın. Toplam tutar: $40a+70(30-a)=30 \\cdot 50=1500$.",
                "$40a+2100-70a=1500$, yani $30a=600$ ve $a=20$.",
                "Ucuz çaydan $20$, pahalı çaydan $10$ kilogram kullanılır. Kontrol: $800+700=1500$."),
            "Çapraz yöntemle: hedef fiyat $50$, ucuz çaya $10$, pahalı çaya $20$ uzaklıktadır; miktarlar $20:10=2:1$ oranında olmalıdır. $30$ kilogramın üçte ikisi $20$, üçte biri $10$ kilogramdır.",
        ]},
        {"baslik": "Oranla verilen karışımlar", "icerik": [
            "Karışımdaki maddelerin birbirine oranı verildiğinde maddeler $k$ ile yazılır. Eklenen ya da çıkarılan madde ilgili terime eklenir ve yeni oran bir orantı olarak kurulur.",
            ornek(
                "Bir karışımda A sıvısının B sıvısına oranı $2:3$ tür. Karışıma $4$ litre A eklenince iki sıvının miktarı eşit oluyor.",
                "Başlangıçtaki miktarları bulalım.",
                "A $2k$, B $3k$ litre olsun. $4$ litre A eklenince: $2k+4=3k$.",
                "$k=4$. Başlangıçta $8$ litre A ve $12$ litre B vardı.",
                "Kontrol: $4$ litre eklenince A $12$ litre olur ve B ile eşitlenir."),
            "Oranla verilen soruların ayrıntısı <a href=\"/blog/oran-ve-oranti-problemleri/\">Oran ve Orantı Problemleri</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Sınavda karışım problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) karışım problemleri su ekleme, buharlaştırma, iki karışımı birleştirme ve istenen orana ulaşma soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde fiyat karışımları ve çapraz yöntem de sık kullanılır."),
            "Karışım sorularında ilk iş, her karışımdaki madde miktarını ayrı ayrı yazmaktır. İkinci iş, madde miktarının değişip değişmediğine karar vermektir: su ekleniyor ya da buharlaşıyorsa değişmez, madde ekleniyor ya da karışım alınıyorsa değişir. Bu iki adım yapıldığında denklem genellikle tek satırda kurulur.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Karışımların oranlarını toplamak", "Madde miktarlarını topla"],
                ["Su eklenince madde miktarını değiştirmek", "Madde miktarı sabit kalır"],
                ["Buharlaşmada tuzu da azaltmak", "Yalnızca su buharlaşır"],
                ["Birleşik oranı basit ortalama sanmak", "Miktarlarla ağırlıklandır"],
                ["Çapraz yöntemde uzaklıkları doğru orantılı almak", "Miktarlar uzaklıklarla ters orantılı"],
                ["Karışımdan alınan kısımdaki maddeyi unutmak", "Alınan kısmın maddesini çıkar"],
            ]),
            "Bu hataların çoğu, madde miktarı ile oranı karıştırmaktan doğar. Oranlar toplanmaz ve çıkarılmaz; toplanan ve çıkarılan her zaman miktarlardır. Oran yalnızca en son adımda, toplam madde toplam karışıma bölünerek bulunur.",
        ]},
    ],
    "sss": [
        ("Karışım problemleri nasıl çözülür?",
         "Her karışımdaki madde miktarı, karışım miktarı ile oranın çarpılmasıyla bulunur. Madde miktarları ve toplam miktarlar ayrı ayrı toplanır, yeni oran bunların bölümüdür."),
        ("Karışıma su eklenince ne değişir?",
         "Madde miktarı değişmez, toplam miktar artar. Bu yüzden maddenin oranı küçülür."),
        ("Su buharlaşınca oran nasıl değişir?",
         "Yalnızca su azalır, madde miktarı aynı kalır. Toplam miktar küçüldüğü için maddenin oranı büyür."),
        ("İki karışım birleşince yeni oran nasıl bulunur?",
         "İki karışımdaki madde miktarları toplanır ve toplam karışım miktarına bölünür. Oranların basit ortalaması yalnızca miktarlar eşitse doğrudur."),
        ("Çapraz yöntem nedir?",
         "Hedef oranın iki karışımın oranlarına uzaklıkları hesaplanır. Karıştırılacak miktarlar bu uzaklıklarla ters orantılıdır."),
        ("Karışımdan alınıp yerine su konursa ne olur?",
         "Toplam miktar değişmez, madde miktarı alınan kısımdaki madde kadar azalır. İşlem tekrarlanırsa madde her seferinde aynı oranla azalır."),
        ("Ayar ne demektir?",
         "Altın alaşımlarında saflık ölçüsüdür. Saf altın 24 ayar kabul edilir; 18 ayar altın, kütlesinin dörtte üçü saf altın olan alaşımdır."),
        ("Fiyat karışımları nasıl çözülür?",
         "Toplam tutar, her ürünün miktarı ile birim fiyatının çarpımlarının toplamıdır. Karışımın birim fiyatı toplam tutarın toplam miktara bölümüdür."),
        ("Tuzun suya oranı ile tuz yüzdesi aynı mı?",
         "Hayır. Oran tuzu suyla, yüzde ise tuzu bütün karışımla karşılaştırır. Tuzun suya oranı 1 e 4 ise tuz yüzdesi 5 te 1, yani yüzde 20 dir."),
        ("Buharlaştırarak oran nasıl artırılır?",
         "Madde miktarı değişmediği için madde miktarı istenen orana bölünerek yeni toplam bulunur. Buharlaşacak su, eski ve yeni toplam arasındaki farktır."),
    ],
    "kontrol": [
        "Bir karışımdaki madde miktarını hesaplayabiliyorum.",
        "Madde miktarının ne zaman değişip ne zaman değişmediğini açıklayabiliyorum.",
        "Karışım bilgilerini tablo hâlinde düzenleyebiliyorum.",
        "Madde ve su ekleme sorularında yeni oranı bulabiliyorum.",
        "Buharlaştırma sorularında yeni oranı bulabiliyorum.",
        "İki karışımın birleşiminin oranını hesaplayabiliyorum.",
        "İstenen orana ulaşmak için eklenecek miktarı bulabiliyorum.",
        "Çapraz yöntemle karışım oranını hızlıca bulabiliyorum.",
        "Karışımdan alıp yerine su koyma sorularını çözebiliyorum.",
        "Alaşım ve fiyat karışımı sorularını çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["yuzde-problemleri-nasil-cozulur", "oran-ve-oranti-problemleri", "yuzdeler-konu-anlatimi-pdf"],
}
