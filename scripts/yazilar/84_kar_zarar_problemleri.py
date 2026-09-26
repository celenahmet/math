# scripts/yazilar/84_kar_zarar_problemleri.py — Kar ve Zarar Problemleri (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "kar-ve-zarar-problemleri-konu-anlatimi-pdf",
    "baslik": "Kâr ve Zarar Problemleri Konu Anlatımı PDF",
    "aciklama": "Kâr ve zarar problemleri nasıl çözülür? Maliyet, satış, kâr yüzdesi, etiket ve indirim, toplu satış, fire ve aynı fiyata satılan iki mal; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "problemler",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "kar-ve-zarar-problemleri-konu-anlatimi-pdf",
    "kapak_alt": "Kâr ve zarar problemleri: terazi ve renkli disk yığınlarıyla alış ve satış fiyatını karşılaştıran öğrenci",
    "ozet": "Kâr ve zarar problemleri, bir malın alış ve satış fiyatı arasındaki farkı konu alır. Temel kural tektir: aksi belirtilmedikçe kâr ve zarar yüzdesi maliyete göre hesaplanır. Bu kural bir kez oturduğunda soruların hepsi yüzde çarpanlarıyla çözülür. Bu yazıda maliyet, satış, kâr ve zarar kavramlarını, kâr yüzdesini, satış fiyatını ve maliyeti bulmayı, etiket fiyatı ve indirimi, toplu satışları, fireli malları ve aynı fiyata satılan iki malı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Temel kavramlar", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için yüzde hesaplarını ve çarpan yöntemini biliyor olman yeterli.",
                "Yüzdenin temeli için <a href=\"/blog/yuzdeler-konu-anlatimi-pdf/\">Yüzdeler Konu Anlatımı PDF</a>, soru türleri için <a href=\"/blog/yuzde-problemleri-nasil-cozulur/\">Yüzde Problemleri Nasıl Çözülür?</a> yazısına göz at."),
            "Kâr ve zarar problemlerinde birkaç temel kavram kullanılır. Bu kavramların birbirine nasıl bağlandığını bilmek, soruların büyük bölümünü doğrudan çözer. Maliyet her zaman satıcının cebinden çıkan paradır; satış fiyatı ise cebine giren paradır. Kâr ve zarar bu ikisinin farkından doğar.",
            tablo(["Kavram", "Anlamı"], [
                ["Maliyet", "Malın alış fiyatı ya da üretim masrafı"],
                ["Satış fiyatı", "Malın satıldığı fiyat"],
                ["Kâr", "Satış fiyatı, maliyetten büyükse aradaki fark"],
                ["Zarar", "Satış fiyatı, maliyetten küçükse aradaki fark"],
                ["Etiket fiyatı", "İndirimden önce mala konan fiyat"],
            ]),
            "Ticaret problemlerinin temel kuralı şudur: <strong>aksi belirtilmedikçe kâr ve zarar yüzdesi maliyete göre hesaplanır.</strong> Maliyet bütün kabul edilir ve kâr ya da zarar bu bütünün yüzdesi olarak ifade edilir.",
            "$$\\text{Kâr yüzdesi}=\\dfrac{\\text{Satış}-\\text{Maliyet}}{\\text{Maliyet}} \\cdot 100$$",
            hap("Kâr ve zarar yüzdesi aksi belirtilmedikçe maliyete göre hesaplanır.",
                "Yüzde $a$ kâr maliyeti $1+\\dfrac{a}{100}$, yüzde $a$ zarar $1-\\dfrac{a}{100}$ ile çarpmaktır."),
        ]},
        {"baslik": "Kâr yüzdesini bulmak", "icerik": [
            "Maliyet ve satış fiyatı biliniyorsa önce kâr ya da zarar miktarı bulunur, sonra maliyete bölünür. Sonuç $100$ ile çarpılarak yüzdeye çevrilir.",
            ornek(
                "Maliyeti $240$ lira olan bir ürün $300$ liraya satılıyor.",
                "Kâr yüzdesini bulalım.",
                "Kâr miktarı: $300-240=60$ lira.",
                "Kâr yüzdesi: $\\dfrac{60}{240} \\cdot 100=25$; yüzde $25$ kâr."),
            ornek(
                "Maliyeti $450$ lira olan bir ürün $405$ liraya satılıyor.",
                "Zarar yüzdesini bulalım.",
                "Zarar miktarı: $450-405=45$ lira.",
                "Zarar yüzdesi: $\\dfrac{45}{450} \\cdot 100=10$; yüzde $10$ zarar."),
            dikkat(
                "Kâr yüzdesini satış fiyatına göre hesaplamak.",
                "İlk örnekte $60$ liralık kâr satış fiyatının yüzde $20$ si, maliyetin ise yüzde $25$ idir. Soru özellikle \"satış fiyatına göre\" demiyorsa bölünen sayı maliyettir."),
        ]},
        {"baslik": "Satış fiyatını bulmak", "icerik": [
            "Maliyet ve kâr ya da zarar yüzdesi biliniyorsa satış fiyatı, maliyetin çarpanla çarpılmasıyla bulunur.",
            ornek(
                "Maliyeti $180$ lira olan bir ürün yüzde $35$ kârla satılacak.",
                "Satış fiyatını bulalım.",
                "Çarpan: $1.35$.",
                "Satış fiyatı: $180 \\cdot 1.35=243$ lira. Kâr miktarı $63$ liradır."),
            ornek(
                "Maliyeti $600$ lira olan bir ürün yüzde $15$ zararla satılıyor.",
                "Satış fiyatını bulalım.",
                "Çarpan: $0.85$.",
                "Satış fiyatı: $600 \\cdot 0.85=510$ lira. Zarar miktarı $90$ liradır."),
        ]},
        {"baslik": "Maliyeti bulmak", "icerik": [
            "Satış fiyatı ile kâr ya da zarar yüzdesi biliniyor ve maliyet soruluyorsa satış fiyatı çarpana bölünür. Satış fiyatına yüzde eklemek ya da çıkarmak yanlış sonuç verir, çünkü yüzde satışın değil maliyetin yüzdesidir.",
            ornek(
                "Bir ürün yüzde $20$ zararla $320$ liraya satılıyor.",
                "Ürünün maliyetini bulalım.",
                "Maliyet $x$ olsun: $0.8x=320$.",
                "$x=320:0.8=400$ lira. Zarar miktarı $80$ liradır."),
            dikkat(
                "Satış fiyatına zarar yüzdesini eklemek.",
                "$320$ ye yüzde $20$ eklemek $384$ verir ve yanlıştır. Zarar yüzde $20$ ise satış fiyatı maliyetin yüzde $80$ idir; maliyet, satış fiyatının $0.8$ e bölünmesiyle bulunur."),
            hap("Satış fiyatından maliyete dönerken satış fiyatı çarpana bölünür; satış fiyatından yüzde çıkarmak yanlış sonuç verir."),
        ]},
        {"baslik": "Birim fiyatla kâr hesabı", "icerik": [
            "Mallar adet adet alınıp satıldığında kâr, bir malın kârı ile adet sayısının çarpımıdır. Kâr yüzdesi ise adetten bağımsızdır; bir malın kâr yüzdesi, bütün partinin kâr yüzdesiyle aynıdır.",
            ornek(
                "Bir kırtasiye tanesi $8$ liradan $120$ kalem alıyor ve tanesini $11$ liradan satıyor.",
                "Toplam kârı ve kâr yüzdesini bulalım.",
                "Bir kalemin kârı: $11-8=3$ lira. Toplam kâr: $3 \\cdot 120=360$ lira.",
                "Kâr yüzdesi: $\\dfrac{3}{8} \\cdot 100=37.5$; yüzde $37.5$.",
                "Toplam üzerinden kontrol: maliyet $960$, gelir $1320$; $\\dfrac{360}{960}$ yine yüzde $37.5$ eder."),
        ]},
        {"baslik": "Denklemle kurulan kâr soruları", "icerik": [
            "Maliyetin bilinmediği ve iki farklı satış senaryosunun karşılaştırıldığı sorularda maliyete $x$ denir ve her senaryonun kârı ya da zararı $x$ cinsinden yazılır.",
            ornek(
                "Bir ürün $540$ liraya satılınca elde edilen kâr, $360$ liraya satılınca edilen zararın $2$ katıdır.",
                "Ürünün maliyetini bulalım.",
                "Maliyet $x$ olsun. $540$ liralık satışta kâr $540-x$, $360$ liralık satışta zarar $x-360$ tır.",
                "Denklem: $540-x=2(x-360)$, yani $540-x=2x-720$ ve $3x=1260$.",
                "$x=420$ lira. Kontrol: kâr $120$, zarar $60$; $120=2 \\cdot 60$."),
            "Denklem kurmanın genel adımları <a href=\"/blog/denklem-kurma-problemleri-nasil-cozulur/\">Denklem Kurma Problemleri Nasıl Çözülür?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Maliyet değişince kâr nasıl değişir?", "icerik": [
            "Satış fiyatı sabit kalırken maliyet artarsa kâr hem miktar olarak hem de yüzde olarak azalır. Yüzdedeki azalış iki yönden gelir: kâr miktarı küçülür ve bölünen maliyet büyür.",
            ornek(
                "Bir ürün yüzde $50$ kârla satılıyor. Ürünün maliyeti yüzde $20$ artıyor ama satış fiyatı değişmiyor.",
                "Yeni kâr yüzdesini bulalım.",
                "Eski maliyet $100$ olsun; satış fiyatı $150$.",
                "Yeni maliyet: $120$. Yeni kâr: $150-120=30$.",
                "Yeni kâr yüzdesi: $\\dfrac{30}{120} \\cdot 100=25$; kâr yüzde $50$ den yüzde $25$ e düşer."),
            "Maliyetteki yüzde $20$ lik artış, kâr yüzdesini $20$ puan değil $25$ puan düşürdü. Bu tür sorularda sonucu sezgiyle tahmin etmek yerine maliyeti $100$ alıp adım adım hesaplamak en güvenli yoldur.",
        ]},
        {"baslik": "Etiket fiyatı ve indirim", "icerik": [
            "Birçok soruda satıcı önce maliyetin üzerine bir yüzde ekleyerek etiket fiyatı belirler, sonra bu etiket üzerinden indirim yapar. İki değişim art arda uygulandığı için çarpanlar çarpılır ve sonuç maliyete göre okunur.",
            ornek(
                "Bir satıcı maliyetin yüzde $50$ fazlasını etiket fiyatı olarak belirliyor ve ürünü etiket fiyatı üzerinden yüzde $20$ indirimle satıyor.",
                "Satıcının kâr yüzdesini bulalım.",
                "Maliyet $100$ olsun. Etiket fiyatı: $150$.",
                "İndirimli satış: $150 \\cdot 0.8=120$.",
                "Kâr: $120-100=20$; yüzde $20$ kâr. Çarpanla: $1.5 \\cdot 0.8=1.2$."),
            ornek(
                "Maliyeti $200$ lira olan bir ürüne maliyetin yüzde $60$ fazlası etiket fiyatı olarak konuyor.",
                "Satıcının zarar etmemek için en fazla yüzde kaç indirim yapabileceğini bulalım.",
                "Etiket fiyatı: $200 \\cdot 1.6=320$ lira.",
                "Zarar etmemek için satış fiyatı en az $200$ lira olmalı; indirim en fazla $320-200=120$ lira olabilir.",
                "Yüzde olarak: $\\dfrac{120}{320} \\cdot 100=37.5$; en fazla yüzde $37.5$ indirim yapılabilir."),
            dikkat(
                "Etiket artışı ile indirimi birbirinden çıkarmak.",
                "Yüzde $50$ artış ve yüzde $20$ indirim, yüzde $30$ kâr değildir. İndirim etiket fiyatına uygulandığı için çarpanlar çarpılır: $1.5 \\cdot 0.8=1.2$, yani yüzde $20$ kâr."),
            hap("Maliyeti $400$ lira olan bir ayakkabının etiketine yüzde $50$ kârla $600$ lira yazılır.", "Mağaza yüzde $20$ indirim yapınca satış fiyatı $480$ lira olur ve kâr yüzde $20$ ye düşer.", gunluk=True),
        ]},
        {"baslik": "Toplu alım ve satım", "icerik": [
            "Aynı maldan çok sayıda alınıp bir kısmı bir fiyattan, kalanı başka bir fiyattan satıldığında toplam kâr, iki satışın toplamı üzerinden hesaplanır. Bir malın maliyetini $1$ birim kabul etmek hesabı sadeleştirir.",
            ornek(
                "Bir satıcı aynı maldan $100$ tane alıyor. Bunların $60$ ını yüzde $30$ kârla, kalan $40$ ını yüzde $10$ zararla satıyor.",
                "Toplam kâr yüzdesini bulalım.",
                "Bir malın maliyeti $1$ birim olsun; toplam maliyet $100$ birim.",
                "Gelir: $60 \\cdot 1.3+40 \\cdot 0.9=78+36=114$ birim.",
                "Kâr: $114-100=14$ birim; toplam kâr yüzde $14$ tür."),
            "Toplam kâr yüzdesi, iki yüzdenin basit ortalaması değildir ve bu sık yapılan bir hatadır. Kârlı satılan mal sayısı daha fazla olduğu için sonuç kârlı tarafa daha yakındır. Bu, farklı büyüklükteki grupların birleşik yüzdesiyle aynı mantıktır. İki yüzdenin ortalaması olan yüzde $10$ yanlış olurdu; doğru sonuç her grubun gelirini ayrı ayrı hesaplayıp toplamakla bulunur.",
        ]},
        {"baslik": "Fireli ve kırılan mallar", "icerik": [
            "Bazı sorularda alınan malların bir kısmı kırılır, bozulur ya da satılamaz. Bu durumda toplam maliyet değişmez ama satılabilecek mal sayısı azalır; hedeflenen kâr, kalan mallardan elde edilmek zorundadır.",
            ornek(
                "Bir satıcı tanesi $20$ liradan $50$ bardak alıyor ve bunların $5$ i kırılıyor.",
                "Kalan bardakları tanesi kaç liradan satarsa toplamda yüzde $35$ kâr edeceğini bulalım.",
                "Toplam maliyet: $50 \\cdot 20=1000$ lira. Hedeflenen gelir: $1000 \\cdot 1.35=1350$ lira.",
                "Satılabilecek bardak: $50-5=45$.",
                "Bir bardağın satış fiyatı: $1350:45=30$ lira."),
            dikkat(
                "Kırılan malları maliyetten düşmek.",
                "Kırılan bardaklar için de para ödenmiştir; toplam maliyet $1000$ lira olarak kalır. Maliyeti $45 \\cdot 20=900$ lira almak, satıcının kırılan bardakların parasını hiç ödemediğini varsaymaktır."),
        ]},
        {"baslik": "Aynı fiyata satılan iki mal", "icerik": [
            "İki mal aynı fiyata satılıyor ve biri kârla, diğeri aynı yüzdeyle zararla satılıyorsa toplam sonuç başa baş değildir; her zaman zarardır. Nedeni, kâr ve zarar yüzdelerinin farklı maliyetlere göre hesaplanmasıdır.",
            ornek(
                "İki malın her biri $1200$ liraya satılıyor. Birinden yüzde $20$ kâr, diğerinden yüzde $20$ zarar ediliyor.",
                "Toplam kâr ya da zararı bulalım.",
                "Kârlı malın maliyeti: $1200:1.2=1000$ lira. Zararlı malın maliyeti: $1200:0.8=1500$ lira.",
                "Toplam maliyet $2500$ lira, toplam satış $2400$ lira.",
                "Toplam zarar $100$ lira; yüzde olarak $\\dfrac{100}{2500} \\cdot 100=4$, yani yüzde $4$ zarar."),
            "Bu sonuç ilk bakışta şaşırtıcıdır ama sezgisel açıklaması basittir: zarar edilen malın maliyeti daha yüksektir, bu yüzden aynı yüzde daha büyük bir tutara karşılık gelir. Kârlı maldan $200$ lira kazanılırken zararlı maldan $300$ lira kaybedilir.",
            hap("Aynı fiyata satılan iki maldan biri yüzde $a$ kârla, öteki yüzde $a$ zararla satılırsa toplamda her zaman zarar edilir."),
        ]},
        {"baslik": "Kâr miktarından maliyete", "icerik": [
            "Bazı sorularda kâr yüzdesi ile kâr miktarı birlikte verilir. Kâr miktarı maliyetin belirli bir yüzdesi olduğu için maliyet doğrudan bulunur.",
            ornek(
                "Bir ürün yüzde $25$ kârla satılıyor ve satıcı bu satıştan $90$ lira kâr ediyor.",
                "Ürünün maliyetini ve satış fiyatını bulalım.",
                "Kâr maliyetin yüzde $25$ i, yani dörtte biridir: maliyet $90 \\cdot 4=360$ lira.",
                "Satış fiyatı: $360+90=450$ lira. Kontrol: $360 \\cdot 1.25=450$."),
        ]},
        {"baslik": "Zincirleme kâr: üreticiden tüketiciye", "icerik": [
            "Bir mal tüketiciye ulaşana kadar birkaç elden geçebilir ve her aşamada kâr eklenir. Her aşamanın kârı bir önceki aşamanın satış fiyatına göre hesaplandığı için çarpanlar çarpılır.",
            ornek(
                "Bir üretici malını maliyetinin yüzde $20$ fazlasına toptancıya, toptancı yüzde $25$ kârla perakendeciye, perakendeci de yüzde $40$ kârla tüketiciye satıyor.",
                "Tüketicinin ödediği fiyatın üretim maliyetinin kaç katı olduğunu bulalım.",
                "Toplam çarpan: $1.2 \\cdot 1.25 \\cdot 1.4=2.1$.",
                "Tüketici, üretim maliyetinin $2.1$ katını öder; yani maliyetin yüzde $110$ fazlasını.",
                "Maliyet $100$ lira olsaydı: toptancıya $120$, perakendeciye $150$, tüketiciye $210$ lira."),
            "Kârların toplamı yüzde $85$ gibi görünse de gerçek artış yüzde $110$ dur; çünkü her aşama bir öncekinin kârı eklenmiş fiyat üzerinden kâr koyar.",
        ]},
        {"baslik": "Hedef kâr için satılması gereken adet", "icerik": [
            "Bir malın birim kârı biliniyorsa belirli bir toplam kâra ulaşmak için kaç mal satılması gerektiği, toplam kârın birim kâra bölünmesiyle bulunur.",
            ornek(
                "Tanesi $15$ liraya mal edilen bir ürün $20$ liradan satılıyor.",
                "$1000$ lira kâr etmek için kaç ürün satılması gerektiğini bulalım.",
                "Bir ürünün kârı: $20-15=5$ lira.",
                "Gereken adet: $1000:5=200$ ürün."),
            "Bu soru türüne sabit giderler de eklenebilir: örneğin bir stant kirası için ödenen $300$ lira varsa, önce bu gideri karşılamak gerekir ve gereken adet $(1000+300):5=260$ olur.",
            hap("Gereken satış adedi, hedeflenen toplam kârın bir malın kârına bölünmesiyle bulunur."),
        ]},
        {"baslik": "Satışa göre kâr soruları", "icerik": [
            "Bazı sorular kâr yüzdesini açıkça satış fiyatına göre verir. Bu durumda bütün satış fiyatıdır ve kurulum değişir: satış fiyatına göre yüzde $a$ kâr, maliyetin satış fiyatının $1-\\dfrac{a}{100}$ katı olması demektir.",
            ornek(
                "Bir ürün, satış fiyatına göre yüzde $20$ kârla $500$ liraya satılıyor.",
                "Ürünün maliyetini ve maliyete göre kâr yüzdesini bulalım.",
                "Kâr, satış fiyatının yüzde $20$ si: $500 \\cdot 0.2=100$ lira. Maliyet: $500-100=400$ lira.",
                "Maliyete göre kâr yüzdesi: $\\dfrac{100}{400} \\cdot 100=25$; yüzde $25$."),
            "Aynı kâr miktarı satışa göre yüzde $20$, maliyete göre yüzde $25$ eder. Soru kökünde \"satış fiyatına göre\" ifadesi görülmüyorsa her zaman maliyet esas alınır.",
        ]},
        {"baslik": "Sınavda kâr ve zarar problemleri", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kâr ve zarar problemleri etiket fiyatı ve indirim, toplu satış, aynı fiyata satılan iki mal ve maliyet bulma soruları biçiminde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de kâr ve zarar soruları sayısal bölümün düzenli soru türlerindendir."),
            "Maliyeti $100$ kabul etmek bu soruların çoğunu tam sayılarla çözmeyi sağlar. Etiket fiyatı, indirim ve kâr gibi birden fazla yüzde varsa çarpanları çarpmak, ara fiyatları hesaplamaktan daha hızlıdır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Kâr yüzdesini satışa göre hesaplamak", "Maliyete göre"],
                ["Maliyeti bulmak için satışa yüzde eklemek", "Satışı çarpana böl"],
                ["Etiket artışından indirimi çıkarmak", "Çarpanları çarp"],
                ["Toplu satışta yüzdelerin ortalamasını almak", "Gelirleri ayrı ayrı topla"],
                ["Kırılan malları maliyetten düşmek", "Maliyet değişmez"],
                ["Aynı fiyata kâr ve zararı başa baş sanmak", "Toplamda zarar vardır"],
            ]),
            "Bu hataların çoğu, yüzdenin hangi fiyata göre alındığını karıştırmaktan doğar. Her kâr ve zarar yüzdesinin yanına \"maliyetin\" kelimesini eklemek, doğru bütünü seçmeyi sağlar.",
        ]},
    ],
    "sss": [
        ("Kâr yüzdesi nasıl hesaplanır?",
         "Kâr miktarı maliyete bölünür ve 100 ile çarpılır. Aksi belirtilmedikçe kâr ve zarar yüzdesi her zaman maliyete göre hesaplanır."),
        ("Satış fiyatı ve kâr yüzdesinden maliyet nasıl bulunur?",
         "Satış fiyatı, kâr çarpanına bölünür. Yüzde 25 kârla 450 liraya satılan ürünün maliyeti 450 bölü 1,25, yani 360 liradır."),
        ("Etiket fiyatı ve indirimde kâr nasıl hesaplanır?",
         "Etiket artışının ve indirimin çarpanları çarpılır. Yüzde 50 artış ve yüzde 20 indirim, 1,5 çarpı 0,8 eşittir 1,2 olduğu için yüzde 20 kâr verir."),
        ("Aynı fiyata satılan iki maldan biri yüzde 20 kâr, diğeri yüzde 20 zararla satılırsa ne olur?",
         "Toplamda zarar edilir. Zararlı malın maliyeti daha yüksek olduğu için aynı yüzde daha büyük bir tutara karşılık gelir."),
        ("Kırılan mallar maliyeti değiştirir mi?",
         "Hayır. Kırılan mallar için de para ödendiği için toplam maliyet aynı kalır; yalnızca satılabilecek mal sayısı azalır."),
        ("Satışa göre kâr ile maliyete göre kâr arasındaki fark nedir?",
         "Satışa göre kârda bütün satış fiyatıdır, maliyete göre kârda bütün maliyettir. Aynı kâr miktarı satışa göre daha küçük bir yüzde eder."),
        ("Maliyet artarsa kâr yüzdesi nasıl değişir?",
         "Satış fiyatı sabitse kâr miktarı azalır ve bölünen maliyet büyür. Maliyeti 100 kabul edip eski ve yeni kârı ayrı ayrı hesaplamak en güvenli yoldur."),
        ("Zincirleme kârda toplam artış nasıl hesaplanır?",
         "Her aşamanın kâr çarpanı çarpılır. Yüzde 20, yüzde 25 ve yüzde 40 kârın çarpımı 2,1 olduğu için tüketici maliyetin yüzde 110 fazlasını öder; kâr yüzdeleri toplanmaz."),
    ],
    "kontrol": [
        "Maliyet, satış, kâr, zarar ve etiket fiyatını ayırt edebiliyorum.",
        "Kâr ve zarar yüzdesini maliyete göre hesaplayabiliyorum.",
        "Maliyet ve kâr yüzdesinden satış fiyatını bulabiliyorum.",
        "Satış fiyatı ve yüzdeden maliyeti bulabiliyorum.",
        "Etiket fiyatı ve indirim içeren soruları çarpanlarla çözebiliyorum.",
        "Zarar etmeden yapılabilecek en büyük indirimi hesaplayabiliyorum.",
        "Toplu satışlarda toplam kâr yüzdesini bulabiliyorum.",
        "Fireli mallarda gereken satış fiyatını hesaplayabiliyorum.",
        "Aynı fiyata satılan iki malın toplam sonucunu bulabiliyorum.",
        "Satışa göre ve maliyete göre kâr yüzdesini birbirine çevirebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["yuzde-problemleri-nasil-cozulur", "yuzdeler-konu-anlatimi-pdf", "faiz-problemleri-nasil-cozulur"],
}
