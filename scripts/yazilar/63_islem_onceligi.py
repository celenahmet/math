# scripts/yazilar/63_islem_onceligi.py — Islem Onceligi (24.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "islem-onceligi-nasil-yapilir",
    "baslik": "İşlem Önceliği Nasıl Yapılır?",
    "aciklama": "İşlem önceliği nasıl yapılır? Parantez, üs ve kök, çarpma-bölme, toplama-çıkarma sırası, soldan sağa kuralı, kesir çizgisi ve çözümlü örnekler.",
    "tarih": "2026-09-24",
    "guncelleme": None,
    "kategori": "sayilar",
    "sinavlar": ["TYT", "ALES", "KPSS"],
    "kapak": "islem-onceligi-nasil-yapilir",
    "kapak_alt": "İşlem önceliği: iç içe geçmiş ahşap çerçevelere içten dışa doğru bloklar yerleştiren öğrenci",
    "ozet": "Aynı işlemi iki kişi farklı sırayla yaparsa farklı sonuç bulabilir. İşlem önceliği, bir ifadede hangi işlemin önce yapılacağını belirleyen ortak kuraldır ve herkesin aynı ifadeden aynı sonucu çıkarmasını sağlar. Bu yazıda öncelik sırasını gerekçesiyle veriyor, parantezleri, üs ve kökleri, soldan sağa kuralını, kesir çizgisini ve negatif sayılarla ilgili tuzakları çözümlü örneklerle adım adım ele alıyoruz.",
    "bolumler": [
        {"baslik": "İşlem önceliği neden gerekir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için dört işlemi, negatif sayıları ve üslü sayıları biliyor olman yeterli.",
                "Üslü sayılar için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısına göz at."),
            "$2+3 \\cdot 4$ ifadesini düşün. Soldan sağa okuyup önce toplarsan $5 \\cdot 4=20$ bulursun. Önce çarparsan $2+12=14$ bulursun. İki sonuçtan yalnızca biri doğru olabilir; hangisinin doğru olduğunu belirleyen kurala <strong>işlem önceliği</strong> denir.",
            "Matematikte kabul edilen kurala göre çarpma, toplamadan önce yapılır; bu yüzden doğru sonuç $14$ tür. Bu kural bir doğa yasası değil, herkesin aynı ifadeyi aynı biçimde okuması için yapılmış bir anlaşmadır. Önemi de buradan gelir: kural bilinmeden yazılan bir ifade, farklı kişilere farklı şeyler söyler.",
            hap("İşlem önceliği, bir ifadede işlemlerin hangi sırayla yapılacağını belirleyen ortak kuraldır.",
                "$2+3 \\cdot 4=14$ tür, $20$ değil: çarpma toplamadan önce gelir."),
        ]},
        {"baslik": "Öncelik sırası", "icerik": [
            "İşlemler dört basamakta yapılır. Bir basamaktaki işlemlerin tamamı bitmeden bir sonrakine geçilmez:",
            tablo(["Sıra", "İşlem", "Not"], [
                ["$1$", "Parantez içi", "İç içe ise en içteki"],
                ["$2$", "Üs ve kök", "Üs yalnız solundaki tabana"],
                ["$3$", "Çarpma ve bölme", "Aynı basamak, soldan sağa"],
                ["$4$", "Toplama ve çıkarma", "Aynı basamak, soldan sağa"],
            ]),
            "Tablodaki en önemli ayrıntı üçüncü ve dördüncü satırdadır: çarpma ile bölme <strong>aynı önceliktedir</strong>, toplama ile çıkarma da öyle. Aynı basamaktaki işlemler, hangisi önce yazılmışsa o önce yapılarak <strong>soldan sağa</strong> ilerler.",
            "İngilizce kaynaklarda bu sıra PEMDAS gibi kısaltmalarla anlatılır. Bu kısaltmalar çarpmayı bölmeden, toplamayı çıkarmadan önce yazdığı için yanıltıcı olabilir; aslında her ikili aynı önceliktedir.",
        ]},
        {"baslik": "Sıra neden böyle?", "icerik": [
            "Öncelik sırası rastgele seçilmiş değildir; işlemlerin birbirinden nasıl türediğini izler. Çarpma, tekrarlı toplamadır: $3 \\cdot 4$, dört tane üçün ya da üç tane dördün toplamıdır. Kuvvet de tekrarlı çarpmadır: $2^3=2 \\cdot 2 \\cdot 2$.",
            "Bu yüzden $2+3 \\cdot 4$ yazıldığında $3 \\cdot 4$ tek bir sayı gibi, bir paket gibi düşünülür: \"iki artı üç tane dört\". Aynı şekilde $5 \\cdot 2^3$ ifadesinde $2^3$ bir pakettir: \"beş tane sekiz\". Daha güçlü işlem, yani başka işlemlerin tekrarı olan işlem, daha sıkı bağlanır ve önce yapılır.",
            "Parantez ise bu doğal sırayı bilerek değiştirmenin yoludur. $(2+3) \\cdot 4$ yazan kişi, önce toplamanın yapılmasını istediğini açıkça söyler.",
        ]},
        {"baslik": "Parantezler", "icerik": [
            "Parantez, \"önce bunu yap\" demenin yoludur. İç içe parantezlerde farklı biçimler kullanılabilir: normal parantez, köşeli parantez ve süslü parantez. Hangi biçim kullanılırsa kullanılsın, <strong>en içteki</strong> parantezden başlanır ve dışa doğru ilerlenir.",
            ornek(
                "$2 \\cdot [3+(8-2) \\cdot 2]$ ifadesi verilsin.",
                "Değerini bulalım.",
                "En içteki parantez: $8-2=6$.",
                "Köşeli parantezin içi: $3+6 \\cdot 2=3+12=15$.",
                "Parantezin içinde de çarpma toplamadan önce yapıldı.",
                "Son adım: $2 \\cdot 15=30$."),
            ornek(
                "$\\{20-[4+(7-5)^3]\\}:2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "En içteki parantez: $7-5=2$ ve $2^3=8$.",
                "Köşeli parantez: $4+8=12$.",
                "Süslü parantez: $20-12=8$.",
                "Son adım: $8:2=4$."),
            dikkat(
                "Parantezin içinde de öncelik kuralı geçerlidir.",
                "$(3+4 \\cdot 5)$ parantezinin değeri $35$ değil, $3+20=23$ tür. Parantez yalnızca dışarıya karşı öncelik verir; içerisi kendi kurallarıyla hesaplanır."),
            hap("İç içe parantezlerde en içten başla ve her parantezin içinde de öncelik kuralını uygula.",
                "Parantezin biçimi (normal, köşeli, süslü) önceliği değiştirmez; yalnızca okumayı kolaylaştırır."),
        ]},
        {"baslik": "Üs ve kök", "icerik": [
            "Parantezlerden sonra üsler ve kökler hesaplanır. Bir üs yalnızca hemen solundaki tabana uygulanır; taban parantez içindeyse üs parantezin tamamına uygulanır.",
            ornek(
                "$3+2^3$ ve $(3+2)^3$ ifadeleri verilsin.",
                "İkisini karşılaştıralım.",
                "$3+2^3=3+8=11$: üs yalnızca $2$ ye uygulandı.",
                "$(3+2)^3=5^3=125$: parantez önce hesaplandı, üs sonra uygulandı."),
            dikkat(
                "$-3^2$ ile $(-3)^2$ farklıdır.",
                "$-3^2=-9$ dur: üs, eksiden önce yalnızca $3$ e uygulanır.",
                "$(-3)^2=9$ dur: eksi parantezin içinde olduğu için üsse dahildir."),
            "<h3>Üs üste gelirse</h3>",
            "Bir üssün de üssü varsa, yani $2^{3^2}$ gibi bir yazım varsa, önce en üstteki kuvvet hesaplanır: $3^2=9$ ve $2^9=512$. Bu, parantezli $(2^3)^2=2^6=64$ ifadesinden farklıdır. Ayrıntı için <a href=\"/blog/uslu-sayilar-konu-anlatimi-pdf/\">Üslü Sayılar Konu Anlatımı PDF</a> yazısındaki üssün üssü bölümüne bakabilirsin.",
            "Kök işareti de bir parantez gibi davranır: kökün altındaki ifade önce hesaplanır, sonra kökü alınır. $\\sqrt{9+16}=\\sqrt{25}=5$ tir; bu değer $\\sqrt{9}+\\sqrt{16}=7$ ile aynı değildir.",
            ornek(
                "$\\sqrt{3^2+4^2}+2 \\cdot \\sqrt[3]{8}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Kökün içi: $3^2+4^2=9+16=25$ ve $\\sqrt{25}=5$.",
                "Küpkök: $\\sqrt[3]{8}=2$.",
                "Çarpma ve toplama: $5+2 \\cdot 2=5+4=9$."),
        ]},
        {"baslik": "Çarpma ve bölme: soldan sağa", "icerik": [
            "Çarpma ve bölme aynı önceliktedir. İkisi yan yana geldiğinde çarpmaya öncelik verilmez; ifade soldan sağa okunur.",
            ornek(
                "$24:4 \\cdot 2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Soldan başlayalım: $24:4=6$.",
                "Sonra: $6 \\cdot 2=12$.",
                "Sonuç $12$ dir.",
                "Önce çarpma yapılsaydı $24:8=3$ gibi yanlış bir sonuç çıkardı."),
            ornek(
                "$48:6:2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Soldan başlayalım: $48:6=8$.",
                "Sonra: $8:2=4$.",
                "Sonuç $4$ tür.",
                "Sağdan başlansaydı $48:3=16$ bulunurdu; bu yanlıştır."),
            dikkat(
                "Bölme, çarpma gibi yer değiştirmeye izin vermez.",
                "$a \\cdot b=b \\cdot a$ dır ama sıfırdan farklı $a$ ve $b$ için $a:b$ ile $b:a$ yalnızca $a=b$ ya da $a=-b$ iken eşittir. Bu yüzden bölme içeren bir ifadede soldan sağa sırası bozulamaz."),
            hap("Çarpma ve bölme aynı önceliktedir ve soldan sağa yapılır: $24:4 \\cdot 2=12$ olur."),
        ]},
        {"baslik": "Toplama ve çıkarma: soldan sağa", "icerik": [
            "Toplama ve çıkarma da aynı önceliktedir ve soldan sağa yapılır. Çıkarmayı, zıt sayıyı eklemek olarak düşünmek hatayı önler: $10-4+3=10+(-4)+3=9$.",
            ornek(
                "$10-4+3$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Soldan başlayalım: $10-4=6$.",
                "Sonra: $6+3=9$.",
                "Sonuç $9$ dur.",
                "Önce $4+3$ yapılsaydı $10-7=3$ bulunurdu; bu yanlıştır."),
            hap("Aynı basamaktaki işlemler (çarpma ile bölme, toplama ile çıkarma) soldan sağa yapılır.",
                "Çıkarmayı zıt sayıyı eklemek olarak yazmak sırayı korumayı kolaylaştırır."),
        ]},
        {"baslik": "Bölme zincirleri", "icerik": [
            "Art arda gelen bölmelerde soldan sağa kuralı, sonucu büyük ölçüde değiştirir. $a:b:c$ ifadesi soldan sağa okunduğunda $(a:b):c$ demektir ve bu, $a$ nın $b \\cdot c$ ye bölünmesine eşittir.",
            ornek(
                "$60:12:4$ ve $60:(12:4)$ ifadeleri verilsin.",
                "İkisini karşılaştıralım.",
                "$60:12:4$: soldan sağa, $60:12=5$ ve $5:4=\\dfrac{5}{4}=1.25$.",
                "Aynı sonuç $60:(12 \\cdot 4)=60:48=\\dfrac{5}{4}$ olarak da bulunur.",
                "$60:(12:4)$: önce parantez, $12:4=3$ ve $60:3=20$.",
                "İki ifade farklıdır: $1.25$ ve $20$."),
            dikkat(
                "Bölmeyi sağdan başlatmak, parantez eklemek gibidir.",
                "$60:12:4$ ifadesini $60:3$ diye okumak, yazılmamış bir parantezi varsaymaktır. Parantez yoksa işlem her zaman soldan başlar."),
        ]},
        {"baslik": "Kesir çizgisi ve mutlak değer", "icerik": [
            "Kesir çizgisi görünmez bir parantez gibidir: önce pay ve payda ayrı ayrı hesaplanır, sonra bölme yapılır.",
            ornek(
                "$\\dfrac{8+4}{2 \\cdot 3}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Pay: $8+4=12$. Payda: $2 \\cdot 3=6$.",
                "Bölme: $12:6=2$."),
            "Aynı ifade tek satırda yazılsaydı parantez gerekirdi: $(8+4):(2 \\cdot 3)=2$. Parantezsiz yazılan $8+4:2 \\cdot 3$ ise bambaşka bir ifadedir: $8+2 \\cdot 3=8+6=14$.",
            "Mutlak değer işareti de parantez gibi davranır. $|3-7| \\cdot 2$ ifadesinde önce içerisi hesaplanır: $|-4| \\cdot 2=4 \\cdot 2=8$.",
            ornek(
                "$2 \\cdot |1-4|-|-3| \\cdot 2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Mutlak değerlerin içi: $|1-4|=|-3|=3$ ve $|-3|=3$.",
                "Çarpmalar: $2 \\cdot 3=6$ ve $3 \\cdot 2=6$.",
                "Çıkarma: $6-6=0$."),
            "İç içe kesirlerde, yani merdiven kesirlerde, en alttaki kesirden başlanır ve yukarı doğru çıkılır. Örneğin $\\dfrac{1}{1+\\dfrac{1}{2}}$ için önce payda hesaplanır: $1+\\dfrac{1}{2}=\\dfrac{3}{2}$. Sonra $1:\\dfrac{3}{2}=\\dfrac{2}{3}$ bulunur.",
            dikkat(
                "Kısaltılmış çarpım yazımında belirsizlik doğabilir.",
                "$6:2(1+2)$ gibi bir yazımda soldan sağa kuralı uygulanırsa $6:2 \\cdot 3=3 \\cdot 3=9$ bulunur. Bu tür yazımlar farklı okunabildiği için kendi çözümlerinde bölmeyi kesir çizgisiyle ya da parantezle açıkça göster."),
        ]},
        {"baslik": "Negatif sayılar ve işaret", "icerik": [
            "Negatif sayılar işlem önceliğinde dikkat isteyen bir yerdir. Kural değişmez; yalnızca eksi işaretinin neye ait olduğuna dikkat etmek gerekir.",
            ornek(
                "$-3^2+4 \\cdot (-2)$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Üs: $-3^2=-9$.",
                "Çarpma: $4 \\cdot (-2)=-8$.",
                "Toplama: $-9+(-8)=-17$."),
            ornek(
                "$-(-2)^3-(-1)^4$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Üsler: $(-2)^3=-8$ ve $(-1)^4=1$.",
                "Yerine yazalım: $-(-8)-1=8-1$.",
                "Sonuç: $7$."),
        ]},
        {"baslik": "Dağılma özelliği ve ortak çarpan", "icerik": [
            "Dağılma özelliği, çarpmanın toplama ve çıkarma üzerine dağıldığını söyler: $a \\cdot (b+c)=a \\cdot b+a \\cdot c$. Bu özellik işlem önceliğini bozmaz; ifadeyi aynı değere sahip başka bir ifadeye çevirir. Doğru kullanıldığında hesabı çok kısaltır.",
            ornek(
                "$7 \\cdot 98$ çarpımı verilsin.",
                "Dağılma özelliğiyle hesaplayalım.",
                "$98=100-2$ yazalım: $7 \\cdot (100-2)$.",
                "Dağıtalım: $7 \\cdot 100-7 \\cdot 2=700-14=686$."),
            ornek(
                "$37 \\cdot 45+37 \\cdot 55$ ifadesi verilsin.",
                "Ortak çarpanı dışarı alarak hesaplayalım.",
                "İki terimde de $37$ çarpanı var: $37 \\cdot (45+55)$.",
                "Parantez: $45+55=100$. Sonuç: $37 \\cdot 100=3700$."),
            dikkat(
                "Dağılma özelliği bölmede yalnızca bir yönde çalışır.",
                "$(8+4):2=8:2+4:2=6$ doğrudur. Ama $12:(2+4)$ ifadesi $12:2+12:4$ diye dağıtılamaz: $12:6=2$ iken $6+3=9$ bulunur."),
        ]},
        {"baslik": "Ondalık sayılarla öncelik", "icerik": [
            "Ondalık sayılarla yapılan işlemlerde de kural değişmez. Ondalık sayılar, hesabı zorlaştırdığı için sırayı atlamaya daha yatkın bir ortam yaratır; her adımı ayrı yazmak burada da işe yarar.",
            ornek(
                "$0.5+0.2 \\cdot 3$ ve $(0.5+0.2) \\cdot 3$ ifadeleri verilsin.",
                "İkisini karşılaştıralım.",
                "Birincide önce çarpma: $0.2 \\cdot 3=0.6$ ve $0.5+0.6=1.1$.",
                "İkincide önce parantez: $0.5+0.2=0.7$ ve $0.7 \\cdot 3=2.1$."),
        ]},
        {"baslik": "Kesirli ifadelerde öncelik", "icerik": [
            "Kesirlerle yapılan işlemlerde de aynı sıra geçerlidir. Kesirli ifadelerde dikkat edilecek nokta, çarpmayı beklemeden toplamamaktır.",
            ornek(
                "$\\dfrac{1}{2}+\\dfrac{1}{3} \\cdot \\dfrac{3}{4}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Önce çarpma: $\\dfrac{1}{3} \\cdot \\dfrac{3}{4}=\\dfrac{1}{4}$.",
                "Sonra toplama: $\\dfrac{1}{2}+\\dfrac{1}{4}=\\dfrac{3}{4}$.",
                "Önce toplama yapılsaydı $\\dfrac{5}{6} \\cdot \\dfrac{3}{4}=\\dfrac{5}{8}$ gibi yanlış bir sonuç çıkardı."),
            ornek(
                "$\\left(\\dfrac{2}{3}-\\dfrac{1}{2}\\right):\\dfrac{1}{6}+2^{-1}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Parantez: $\\dfrac{2}{3}-\\dfrac{1}{2}=\\dfrac{4}{6}-\\dfrac{3}{6}=\\dfrac{1}{6}$.",
                "Üs: $2^{-1}=\\dfrac{1}{2}$.",
                "Bölme: $\\dfrac{1}{6}:\\dfrac{1}{6}=1$.",
                "Toplama: $1+\\dfrac{1}{2}=\\dfrac{3}{2}$."),
        ]},
        {"baslik": "Adım adım uzun örnekler", "icerik": [
            "Uzun bir ifadede en güvenli yöntem, her adımda yalnızca bir basamaktaki işlemleri yapıp ifadeyi yeniden yazmaktır. Aşağıdaki örneklerde her satır bir basamağı gösteriyor.",
            ornek(
                "$5-2 \\cdot [3-(4-6)^2:2]$ ifadesi verilsin.",
                "Değerini bulalım.",
                "En içteki parantez ve üssü: $(4-6)^2=(-2)^2=4$.",
                "Köşeli parantezin içi: $3-4:2=3-2=1$.",
                "Dışarıda: $5-2 \\cdot 1=5-2=3$."),
            ornek(
                "$(2^3-3^2) \\cdot (-1)^5+\\sqrt{16}:2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Parantez içi: $2^3-3^2=8-9=-1$.",
                "Üs ve kök: $(-1)^5=-1$ ve $\\sqrt{16}=4$.",
                "Çarpma ve bölme: $(-1) \\cdot (-1)=1$ ve $4:2=2$.",
                "Toplama: $1+2=3$."),
            ornek(
                "$12-3 \\cdot 2^2+18:(5-2) \\cdot 2$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Parantez: $5-2=3$. Üs: $2^2=4$.",
                "İfade: $12-3 \\cdot 4+18:3 \\cdot 2$.",
                "Çarpma ve bölme soldan sağa: $3 \\cdot 4=12$; $18:3=6$ ve $6 \\cdot 2=12$.",
                "Toplama ve çıkarma soldan sağa: $12-12+12=12$."),
        ]},
        {"baslik": "Günlük hayatta işlem önceliği", "icerik": [
            "Bir problemi işlem olarak yazarken öncelik kuralını bilmek, parantezin nereye konacağını belirler. Yanlış yerde unutulan bir parantez, doğru düşünülmüş bir çözümü yanlış sonuca götürür.",
            ornek(
                "Bir öğrenci kırtasiyeden tanesi $12$ lira olan $3$ defter ve tanesi $5$ lira olan $2$ kalem alıp $100$ lira veriyor.",
                "Para üstünü tek bir işlemle yazıp hesaplayalım.",
                "Harcanan tutar: $3 \\cdot 12+2 \\cdot 5$. Para üstü, bu tutarın $100$ den çıkarılmasıdır: $100-(3 \\cdot 12+2 \\cdot 5)$.",
                "Parantez içi: $36+10=46$.",
                "Para üstü: $100-46=54$ lira."),
            dikkat(
                "Burada parantezi unutmak sonucu değiştirir.",
                "$100-3 \\cdot 12+2 \\cdot 5$ yazılırsa kalemlerin tutarı çıkarılmak yerine eklenir: $100-36+10=74$ bulunur. Bu yanlış bir sonuçtur."),
            hap("Market fişinde tanesi $15$ lira olan $3$ süt ve tanesi $20$ lira olan $2$ paket makarna varsa tutar $3 \\cdot 15+2 \\cdot 20=85$ lira olur.", "Önce çarpmalar, sonra toplama yapılır.", gunluk=True),
        ]},
        {"baslik": "Kendini dene", "icerik": [
            "Aşağıdaki iki ifadeyi önce kendin çöz, sonra çözümle karşılaştır.",
            ornek(
                "$-2^2+(-2)^2-2^{-2}$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Üsler: $-2^2=-4$, $(-2)^2=4$, $2^{-2}=\\dfrac{1}{4}$.",
                "Yerine yazalım: $-4+4-\\dfrac{1}{4}$.",
                "Sonuç: $-\\dfrac{1}{4}$."),
            ornek(
                "$3-3:3+3 \\cdot 3-3$ ifadesi verilsin.",
                "Değerini bulalım.",
                "Önce bölme ve çarpma: $3:3=1$ ve $3 \\cdot 3=9$.",
                "İfade: $3-1+9-3$.",
                "Soldan sağa: $3-1=2$, $2+9=11$, $11-3=8$."),
        ]},
        {"baslik": "Sınavda işlem önceliği", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) işlem önceliği; kesirli ifadeler, üslü ve köklü sayılar ve negatif sayılarla yapılan işlemlerin içinde karşına çıkabilir.",
                "<strong>ALES</strong> ve <strong>KPSS</strong> düzeyinde de işlem önceliği, sayısal akıl yürütme sorularında gereken bir beceridir."),
            "Uzun bir ifadeyle karşılaştığında önce parantezleri, üsleri ve çarpma-bölme gruplarını işaretlemek, hangi parçaların birbirinden bağımsız hesaplanabileceğini gösterir. Örneğin $12-3 \\cdot 2^2+18:(5-2) \\cdot 2$ ifadesinde üç ayrı parça vardır: $12$, $3 \\cdot 2^2$ ve $18:(5-2) \\cdot 2$. Parçalar ayrı ayrı hesaplanıp en sonda soldan sağa toplanır ve çıkarılır. Bu yöntem, uzun ifadelerde adım atlamayı zorlaştırır.",
            "Sınavda zaman baskısı altında bilinen bir kuralı aceleyle atlamak kolaydır. Her adımda ifadeyi yeniden yazmak birkaç saniye alır ama işaret ve sıra hatalarının çoğunu önler.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$2+3 \\cdot 4=20$", "$2+3 \\cdot 4=14$"],
                ["$24:4 \\cdot 2=3$", "$24:4 \\cdot 2=12$"],
                ["$10-4+3=3$", "$10-4+3=9$"],
                ["$-3^2=9$", "$-3^2=-9$"],
                ["$\\sqrt{9+16}=7$", "$\\sqrt{9+16}=5$"],
                ["Kesirde önce toplamak", "Önce çarpma ve bölme"],
            ]),
            "Bu hataların hepsi iki kuraldan birinin unutulmasından doğar: çarpma ve bölme toplamadan önce gelir; aynı basamaktaki işlemler soldan sağa yapılır. Bu iki cümleyi hatırlamak, tablodaki hataların hepsini önler.",
        ]},
    ],
    "sss": [
        ("İşlem önceliği sırası nedir?",
         "Önce parantez içi, sonra üs ve kök, sonra çarpma ve bölme, en son toplama ve çıkarma yapılır. Aynı basamaktaki işlemler soldan sağa yapılır."),
        ("Çarpma mı önce yapılır bölme mi?",
         "İkisi aynı önceliktedir. Hangisi solda yazılmışsa o önce yapılır."),
        ("Toplama mı önce yapılır çıkarma mı?",
         "İkisi aynı önceliktedir ve soldan sağa yapılır. Örneğin 10 eksi 4 artı 3 işleminin sonucu 9 dur."),
        ("Önce üs mü yapılır çarpma mı?",
         "Önce üs yapılır. Örneğin 5 çarpı 2 üzeri 3 işleminde önce 2 üzeri 3 yani 8 bulunur, sonra 5 ile çarpılarak 40 elde edilir."),
        ("İç içe parantezlerde nereden başlanır?",
         "En içteki parantezden başlanır ve dışa doğru ilerlenir. Parantezin içinde de öncelik kuralı geçerlidir."),
        ("Eksi 3 ün karesi ile eksi 3 kare aynı mıdır?",
         "Hayır. Parantez içindeki eksi 3 ün karesi 9, parantezsiz yazılan eksi 3 kare ise eksi 9 dur. Parantez yoksa üs yalnızca 3 e uygulanır."),
        ("PEMDAS ne demektir?",
         "İşlem önceliğini İngilizce kelimelerin baş harfleriyle hatırlatan bir kısaltmadır. Çarpmayı bölmeden, toplamayı çıkarmadan önce yazdığı için yanıltıcı olabilir; bu ikililer aynı önceliktedir ve soldan sağa yapılır."),
        ("Kesir çizgisi işlem önceliğini nasıl etkiler?",
         "Kesir çizgisi görünmez bir parantez gibidir. Önce pay ve payda ayrı ayrı hesaplanır, sonra bölme yapılır."),
    ],
    "kontrol": [
        "İşlem önceliğinin neden gerekli olduğunu bir örnekle açıklayabiliyorum.",
        "Dört basamaklı öncelik sırasını sayabiliyorum.",
        "İç içe parantezlerde en içten başlayarak ilerleyebiliyorum.",
        "Üssün yalnızca hemen solundaki tabana uygulandığını biliyorum.",
        "$-3^2$ ile $(-3)^2$ arasındaki farkı açıklayabiliyorum.",
        "Çarpma ile bölmeyi soldan sağa sırayla yapabiliyorum.",
        "Toplama ile çıkarmayı soldan sağa sırayla yapabiliyorum.",
        "Kesir çizgisini ve mutlak değeri parantez gibi kullanabiliyorum.",
        "Kesirli ifadelerde önce çarpma ve bölmeyi yapabiliyorum.",
        "Uzun bir ifadeyi her adımda yeniden yazarak çözebiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["uslu-sayilar-konu-anlatimi-pdf", "pozitif-ve-negatif-sayilar", "rasyonel-sayilar-konu-anlatimi-pdf"],
}
