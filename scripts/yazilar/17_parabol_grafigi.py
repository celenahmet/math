# scripts/yazilar/17_parabol_grafigi.py — Parabol Grafigi (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo, koordinat_grafik  # noqa: E402

_F = lambda x: x * x - 2 * x - 3

YAZI = {
    "slug": "parabol-grafigi",
    "baslik": "Parabol Grafiği Nasıl Çizilir?",
    "aciklama": "Parabol grafiği nasıl çizilir? Adım adım çizim, tepe noktası, simetrik noktalar, kökü olmayan parabol, öteleme, mutlak değer ve grafik okuma; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "denklemler",
    "sinavlar": ["AYT"],
    "kapak": "parabol-grafigi",
    "kapak_alt": "Parabol grafiği: dört ızgaralı panelde simetrik noktalardan tamamlanmış eğriye adım adım parabol çizen iki öğrenci",
    "ozet": "Bir parabolün grafiğini çizmek için çok sayıda nokta hesaplamak gerekmez: kolların yönü, tepe noktası, simetri ekseni ve birkaç simetrik nokta eğrinin biçimini tamamen belirler. Bu yazıda parabol çizmenin adımlarını, tepe noktasından ve eksen kesişimlerinden başlayarak eğriyi kurmayı, kolları aşağı bakan, kökü olmayan ve eksene teğet olan parabolleri, farklı denklem biçimlerinden çizimi, ötelemeyi, mutlak değerli ve kısıtlı aralıktaki parabolleri ve grafikten bilgi okumayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Parabol çizmenin adımları", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için parabolün yapısını ve tepe noktasını biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/parabol-konu-anlatimi/\">Parabol Konu Anlatımı</a> ve <a href=\"/blog/parabol-tepe-noktasi/\">Parabolün Tepe Noktası Nasıl Bulunur?</a> yazılarına göz at."),
            "Parabol çizmek bir tahmin işi değildir; birkaç belirleyici nokta bulunur ve eğri bu noktalardan simetriye uygun biçimde geçirilir. Aşağıdaki sıra hemen her parabolde işe yarar:",
            tablo(["Adım", "Yapılacak iş"], [
                ["1", "Baş katsayıya bak: kollar yukarı mı aşağı mı?"],
                ["2", "Tepe noktasını ve simetri eksenini bul"],
                ["3", "$y$ ekseni kesişimini bul: $(0, c)$"],
                ["4", "Kökleri bul: $x$ ekseni kesişimleri"],
                ["5", "Simetrik noktaları işaretle"],
                ["6", "Noktaları düzgün bir eğriyle birleştir"],
            ]),
            hap("Tepe noktası ve simetri ekseni grafiğin iskeletidir.",
                "Her noktanın simetri eksenine göre bir eşi vardır."),
        ]},
        {"baslik": "Ölçek ve eksenler", "icerik": [
            "Çizime başlamadan önce eksenlerin ne kadar uzanacağı belirlenir. Tepe noktası, kökler ve $y$ ekseni kesişimi hesaplandıktan sonra bu noktaların hepsini içine alan bir aralık seçilir; eğri kâğıdın dışına taşmamalı ama çok küçük de kalmamalıdır.",
            "İki eksende aynı ölçeği kullanmak parabolün biçimini gerçeğe uygun gösterir. Değerler çok büyükse dikey eksende daha büyük bir birim seçilebilir, ama bu durumda parabol olduğundan dar görünür. Sınav sorularındaki grafikler de çoğu zaman bu yüzden ızgara üzerinde verilir: noktaların konumu biçimden daha güvenilir bir bilgidir.",
        ]},
        {"baslik": "Sabit terimden hızlı bir nokta çifti", "icerik": [
            "Her parabolde $(0, c)$ noktası vardır ve simetri eksenine göre simetriği $(2r, c)$ noktasıdır. Bu çift, kök bulmaya gerek kalmadan iki nokta verir ve özellikle kökleri irrasyonel olan parabollerde işe yarar.",
            ornek(
                "$y=x^2-6x+5$ parabolü verilsin.",
                "Sabit terimden bir nokta çifti bulalım.",
                "$c=5$ ve $r=3$.",
                "Noktalar $(0, 5)$ ve $(6, 5)$ tir. Kontrol: $36-36+5=5$."),
        ]},
        {"baslik": "Adım adım bir örnek", "icerik": [
            "Adımları $y=x^2-2x-3$ parabolü üzerinde uygulayalım. Kapaktaki dört panel de aynı ilerleyişi gösterir: boş ızgara, belirleyici noktalar, simetrik noktalar ve tamamlanmış eğri.",
            ornek(
                "$y=x^2-2x-3$ parabolü verilsin.",
                "Grafiği çizmek için gereken noktaları bulalım.",
                "$a=1>0$: kollar yukarı. Tepe noktası: $r=1$ ve $k=1-2-3=-4$; $T(1, -4)$.",
                "$y$ ekseni: $(0, -3)$. Kökler: $(x-3)(x+1)=0$; $(-1, 0)$ ve $(3, 0)$.",
                "$(0, -3)$ noktasının $x=1$ e göre simetriği $(2, -3)$ tür."),
            koordinat_grafik("Birinci aşama: belirleyici noktalar işaretlendi", [], (-3, 5), (-5, 5), dikeyler=[1],
                             noktalar=[(1, -4, "T(1, −4)", True), (0, -3, "(0, −3)", True), (2, -3, "(2, −3)", True), (-1, 0, "(−1, 0)", True), (3, 0, "(3, 0)", True)]),
            koordinat_grafik("İkinci aşama: noktalar simetriye uygun eğriyle birleştirildi", [("y = x² − 2x − 3", _F)], (-3, 5), (-5, 5), dikeyler=[1],
                             noktalar=[(1, -4, "T(1, −4)", True), (0, -3, "", True), (2, -3, "", True), (-1, 0, "(−1, 0)", True), (3, 0, "(3, 0)", True)]),
            "Beş nokta, eğrinin biçimini tamamen belirlemeye yeter. Daha düzgün bir çizim için tepe noktasından iki birim uzaktaki noktalar da eklenebilir: $x=-1$ ve $x=3$ zaten köklerdir, bu yüzden eğri bu noktalarda $x$ eksenini keser.",
        ]},
        {"baslik": "Nokta en çok nerede gerekir?", "icerik": [
            "Parabolün en çok kıvrıldığı yer tepe noktasının çevresidir; kollar ise tepe noktasından uzaklaştıkça doğruya benzer biçimde dikleşir. Bu yüzden tepe noktasının hemen iki yanına birer nokta koymak, eğrinin kıvrımını doğru çizmek için en değerli adımdır.",
            "Tepe noktasından uzaktaki noktalar ise eğrinin ne kadar hızlı yükseldiğini gösterir. İyi bir çizim için tepe noktası, her iki yanda birer yakın nokta ve birer uzak nokta, yani toplam beş nokta çoğu zaman yeterlidir. Kökler ve $y$ ekseni kesişimi bu noktalardan bazılarının yerini tutabilir.",
        ]},
        {"baslik": "Değer tablosu yöntemi", "icerik": [
            "Kökler kolay bulunmuyorsa tepe noktasının iki yanından eşit aralıklarla $x$ değerleri seçilerek bir değer tablosu kurulur. Simetri sayesinde tablonun yarısı hesaplanır, diğer yarısı aynalanır; bu da hesap yükünü neredeyse yarıya indirir.",
            tablo(["$x$", "$-1$", "$0$", "$1$", "$2$", "$3$"], [
                ["$y=x^2-2x-3$", "$0$", "$-3$", "$-4$", "$-3$", "$0$"],
            ]),
            "Tablodaki değerler tepe noktası $x=1$ in iki yanında aynıdır: $x=0$ ile $x=2$, $x=-1$ ile $x=3$ aynı yüksekliktedir. Bu simetri, hesaplama hatalarını da yakalar: iki yandaki değerler farklı çıkıyorsa bir hesap yanlıştır.",
        ]},
        {"baslik": "Kolları aşağı bakan parabol", "icerik": [
            "Baş katsayı negatifse aynı adımlar uygulanır; yalnızca tepe noktası eğrinin en yüksek noktası olur ve kollar aşağı iner.",
            ornek(
                "$y=-x^2+4x$ parabolü verilsin.",
                "Grafiği çizmek için gereken noktaları bulalım.",
                "$a=-1<0$: kollar aşağı. Tepe noktası: $r=2$ ve $k=-4+8=4$; $T(2, 4)$.",
                "Kökler: $-x(x-4)=0$; $(0, 0)$ ve $(4, 0)$. $y$ ekseni kesişimi de $(0, 0)$ dır."),
            koordinat_grafik("y = −x² + 4x: kolları aşağı bakan parabol", [("y = −x² + 4x", lambda x: -x * x + 4 * x)], (-1, 5), (-2, 5), dikeyler=[2],
                             noktalar=[(2, 4, "T(2, 4)", True), (0, 0, "(0, 0)", True), (4, 0, "(4, 0)", True), (1, 3, "(1, 3)", True), (3, 3, "(3, 3)", True)]),
        ]},
        {"baslik": "Kökü olmayan parabol", "icerik": [
            "Diskriminant negatifse parabol $x$ eksenini kesmez ve kök bulunmaz. Grafik yine tepe noktası, $y$ ekseni kesişimi ve bu noktanın simetriğiyle çizilir.",
            ornek(
                "$y=x^2+2x+3$ parabolü verilsin.",
                "Grafiği çizmek için gereken noktaları bulalım.",
                "$\\Delta=4-12=-8<0$; kök yoktur. Tepe noktası: $r=-1$ ve $k=1-2+3=2$; $T(-1, 2)$.",
                "$y$ ekseni: $(0, 3)$; simetriği $(-2, 3)$ tür."),
            koordinat_grafik("y = x² + 2x + 3: x eksenini kesmeyen parabol", [("y = x² + 2x + 3", lambda x: x * x + 2 * x + 3)], (-4, 2), (-1, 7), dikeyler=[-1],
                             noktalar=[(-1, 2, "T(−1, 2)", True), (0, 3, "(0, 3)", True), (-2, 3, "(−2, 3)", True)]),
            "Kolları yukarı bakan bir parabolün tepe noktası eksenin üstündeyse eğri hiçbir yerde eksene inemez. Kök olmaması grafikte tam olarak bu durumdur. Bu tür parabollerde kök bulunmadığı için ek nokta olarak tepe noktasının iki birim yanındaki noktalar da kullanılabilir: $x=1$ ve $x=-3$ için $y=6$ dır.",
        ]},
        {"baslik": "Eksene teğet olan parabol", "icerik": [
            "Diskriminant sıfırsa tepe noktası $x$ ekseni üzerindedir ve parabol eksene bu noktada değer. Tepe noktası aynı zamanda tek köktür.",
            ornek(
                "$y=x^2-4x+4$ parabolü verilsin.",
                "Grafiği çizmek için gereken noktaları bulalım.",
                "$y=(x-2)^2$; tepe noktası $T(2, 0)$ ve eksene teğettir.",
                "$y$ ekseni: $(0, 4)$; simetriği $(4, 4)$ tür."),
            koordinat_grafik("y = x² − 4x + 4: x eksenine teğet parabol", [("y = (x − 2)²", lambda x: (x - 2) ** 2)], (-1, 5), (-1, 6), dikeyler=[2],
                             noktalar=[(2, 0, "T(2, 0)", True), (0, 4, "(0, 4)", True), (4, 4, "(4, 4)", True)]),
        ]},
        {"baslik": "Eksene göre yansıyan parabol", "icerik": [
            "$y=-f(x)$ grafiği, $y=f(x)$ grafiğinin $x$ eksenine göre yansımasıdır. Parabolde bu, kolların yön değiştirmesi ve tepe noktasının dikey koordinatının işaret değiştirmesi demektir; kökler aynı kalır.",
            ornek(
                "$y=x^2-2x-3$ ve $y=-x^2+2x+3$ parabolleri verilsin.",
                "İkinci grafiği birinciden elde edelim.",
                "İkinci denklem birincinin eksi işaretlisidir.",
                "Tepe noktası $(1, -4)$ ten $(1, 4)$ e geçer; kökler $-1$ ve $3$ olarak kalır."),
            koordinat_grafik("y = x² − 2x − 3 ve x eksenine göre yansıması", [("y = x² − 2x − 3", _F), ("y = −x² + 2x + 3", lambda x: -_F(x))], (-3, 5), (-5, 7),
                             noktalar=[(1, -4, "(1, −4)", True), (1, 4, "(1, 4)", True), (-1, 0, "", True), (3, 0, "", True)]),
        ]},
        {"baslik": "Tepe noktası biçiminden çizmek", "icerik": [
            "Denklem $y=a(x-r)^2+k$ biçimindeyse tepe noktası doğrudan okunur ve grafik hızla çizilir. Tepe noktasından bir birim sağa ya da sola gidildiğinde $y$, $a$ kadar değişir; iki birim gidildiğinde $4a$ kadar değişir.",
            ornek(
                "$y=2(x-1)^2-2$ parabolü verilsin.",
                "Grafiği çizmek için gereken noktaları bulalım.",
                "Tepe noktası $T(1, -2)$ ve $a=2$.",
                "$x=0$ ve $x=2$ için $y=2-2=0$; kökler $0$ ve $2$ dir. $x=-1$ ve $x=3$ için $y=8-2=6$."),
            koordinat_grafik("y = 2(x − 1)² − 2", [("y = 2(x − 1)² − 2", lambda x: 2 * (x - 1) ** 2 - 2)], (-2, 4), (-3, 9), dikeyler=[1],
                             noktalar=[(1, -2, "T(1, −2)", True), (0, 0, "(0, 0)", True), (2, 0, "(2, 0)", True), (-1, 6, "(−1, 6)", True), (3, 6, "(3, 6)", True)]),
        ]},
        {"baslik": "Kök biçiminden çizmek", "icerik": [
            "Denklem çarpanlarına ayrılmışsa kökler hemen okunur, simetri ekseni köklerin ortalamasıdır ve tepe noktası bu değerde hesaplanır.",
            ornek(
                "$y=-(x+1)(x-3)$ parabolü verilsin.",
                "Grafiği çizmek için gereken noktaları bulalım.",
                "Kökler $-1$ ve $3$; simetri ekseni $x=1$.",
                "Tepe noktası: $-(2)(-2)=4$; $T(1, 4)$. $y$ ekseni: $-(1)(-3)=3$; $(0, 3)$."),
            koordinat_grafik("y = −(x + 1)(x − 3)", [("y = −(x + 1)(x − 3)", lambda x: -(x + 1) * (x - 3))], (-2, 4), (-3, 5), dikeyler=[1],
                             noktalar=[(1, 4, "T(1, 4)", True), (-1, 0, "(−1, 0)", True), (3, 0, "(3, 0)", True), (0, 3, "(0, 3)", True), (2, 3, "(2, 3)", True)]),
        ]},
        {"baslik": "Genişliği doğru çizmek", "icerik": [
            "Parabolün genişliği baş katsayıya bağlıdır ve grafikte doğru görünmesi için tepe noktasının yanındaki noktalar dikkatle yerleştirilmelidir. Tepe noktasından $d$ birim uzakta eğri $a d^2$ kadar yükselir ya da alçalır.",
            tablo(["Tepe noktasına uzaklık", "$a=1$", "$a=2$", "$a=\\dfrac{1}{2}$"], [
                ["$1$ birim", "$1$", "$2$", "$\\dfrac{1}{2}$"],
                ["$2$ birim", "$4$", "$8$", "$2$"],
                ["$3$ birim", "$9$", "$18$", "$\\dfrac{9}{2}$"],
            ]),
            "Tablo, dar ve geniş parabollerin farkını sayılarla gösterir. Grafiği çizerken bu noktaları işaretlemek, eğrinin rastgele değil doğru genişlikte çizilmesini sağlar.",
        ]},
        {"baslik": "Ötelemeyle çizmek", "icerik": [
            "Bir parabol başka bir parabolün ötelenmesiyse grafiği baştan hesaplanmaz; bilinen grafik kaydırılır. $y=(x-r)^2+k$ grafiği, $y=x^2$ grafiğinin $r$ birim yatay ve $k$ birim dikey ötelenmesidir.",
            ornek(
                "$y=(x+2)^2-1$ parabolü verilsin.",
                "Grafiği $y=x^2$ den öteleyerek çizelim.",
                "Tepe noktası $(0, 0)$ dan $(-2, -1)$ e taşınır.",
                "$y=x^2$ üzerindeki her nokta $2$ birim sola ve $1$ birim aşağı kaydırılır."),
            koordinat_grafik("y = x² grafiğinden y = (x + 2)² − 1 grafiğine öteleme", [("y = x²", lambda x: x * x), ("y = (x + 2)² − 1", lambda x: (x + 2) ** 2 - 1)], (-5, 3), (-2, 6),
                             noktalar=[(0, 0, "", True), (-2, -1, "(−2, −1)", True)]),
        ]},
        {"baslik": "Kısıtlı aralıkta parabol", "icerik": [
            "Tanım kümesi bir aralıkla sınırlandırıldığında grafik yalnızca o aralıkta çizilir. Aralığın uç noktaları dahilse dolu, değilse boş daireyle gösterilir; tepe noktası aralığın içindeyse eğrinin en alçak ya da en yüksek noktası olarak yer alır.",
            ornek(
                "$[0, 3]$ aralığında $f(x)=x^2-2x$ fonksiyonu verilsin.",
                "Grafiği çizip en küçük ve en büyük değerleri bulalım.",
                "Tepe noktası $(1, -1)$ aralığın içindedir.",
                "Uçlar: $f(0)=0$ ve $f(3)=3$. En küçük değer $-1$, en büyük değer $3$ tür."),
            koordinat_grafik("[0, 3] aralığında y = x² − 2x", [("y = x² − 2x (0 ≤ x ≤ 3)", lambda x: x * x - 2 * x if 0 <= x <= 3 else None)], (-1, 4), (-2, 4),
                             noktalar=[(0, 0, "(0, 0)", True), (3, 3, "(3, 3)", True), (1, -1, "(1, −1)", True)]),
        ]},
        {"baslik": "Mutlak değerli parabol", "icerik": [
            "$y=|f(x)|$ grafiği çizilirken önce $y=f(x)$ çizilir; $x$ ekseninin altında kalan kısımlar eksene göre yukarı yansıtılır. Mutlak değer negatif olamayacağı için grafik hiçbir yerde eksenin altına inmez.",
            ornek(
                "$y=|x^2-4|$ fonksiyonu verilsin.",
                "Grafiği çizelim.",
                "$y=x^2-4$ parabolü $-2$ ile $2$ arasında eksenin altındadır; tepe noktası $(0, -4)$ tür.",
                "Bu kısım yukarı yansıtılır: yeni grafikte $(0, 4)$ bir tepe noktası gibi görünür ve $x=\\pm 2$ de köşeler oluşur."),
            koordinat_grafik("y = x² − 4 ve y = |x² − 4| grafikleri", [("y = x² − 4", lambda x: x * x - 4), ("y = |x² − 4|", lambda x: abs(x * x - 4))], (-4, 4), (-5, 6),
                             noktalar=[(0, 4, "(0, 4)", True), (-2, 0, "", True), (2, 0, "", True)]),
        ]},
        {"baslik": "İki parabolü birlikte çizmek", "icerik": [
            "İki parabol aynı düzlemde çizildiğinde kesişim noktaları iki denklemin eşitlenmesiyle bulunur. Grafik, bu noktaların sayısını ve konumunu doğrular.",
            ornek(
                "$y=x^2$ ve $y=-x^2+2$ parabolleri verilsin.",
                "Kesişim noktalarını bulalım.",
                "$x^2=-x^2+2$, yani $x^2=1$ ve $x=\\pm 1$.",
                "Kesişim noktaları $(-1, 1)$ ve $(1, 1)$ dir."),
            koordinat_grafik("y = x² ile y = −x² + 2 kesişimi", [("y = x²", lambda x: x * x), ("y = −x² + 2", lambda x: -x * x + 2)], (-3, 3), (-3, 4),
                             noktalar=[(-1, 1, "(−1, 1)", True), (1, 1, "(1, 1)", True)]),
        ]},
        {"baslik": "Artan ve azalan aralıkları okumak", "icerik": [
            "Grafik soldan sağa okunur. Kolları yukarı bakan parabol tepe noktasına kadar alçalır, sonra yükselir; bu yüzden simetri ekseninin solunda azalan, sağında artandır.",
            ornek(
                "$y=x^2-2x-3$ grafiği verilsin.",
                "Artan ve azalan aralıkları okuyalım.",
                "Tepe noktası $x=1$ tedir ve kollar yukarı bakar.",
                "Fonksiyon $(-\\infty, 1]$ aralığında azalan, $[1, \\infty)$ aralığında artandır."),
        ]},
        {"baslik": "Grafikle denklem çözmek", "icerik": [
            "Bir denklemin iki tarafı ayrı ayrı çizilirse kesişim noktalarının yatay konumları denklemin çözümleridir. Parabol ile bir doğrunun kesişimi, bu yöntemin en sık görülen örneğidir.",
            ornek(
                "$x^2-2x-3=x-3$ denklemi verilsin.",
                "Denklemi grafiklerin kesişimiyle çözelim.",
                "Sol taraf parabol, sağ taraf doğrudur. Cebirsel olarak $x^2-3x=0$, yani $x(x-3)=0$.",
                "Kesişim noktaları $(0, -3)$ ve $(3, 0)$ dır; çözümler $0$ ve $3$ tür."),
            koordinat_grafik("y = x² − 2x − 3 parabolü ile y = x − 3 doğrusunun kesişimi", [("y = x² − 2x − 3", _F), ("y = x − 3", lambda x: x - 3)], (-3, 5), (-5, 5),
                             noktalar=[(0, -3, "(0, −3)", True), (3, 0, "(3, 0)", True)]),
            "Parabol ile doğrunun durumlarının ayrıntısı <a href=\"/blog/parabol-ve-dogru/\">Parabol ve Doğrunun Birbirine Göre Durumları</a> yazısında.",
        ]},
        {"baslik": "Grafikten denklem yazmak", "icerik": [
            "Grafik verildiğinde tepe noktası ve bir nokta okunabiliyorsa denklem hemen yazılır. Grafikteki bilgiyi denkleme çevirmek, çizimin tersidir.",
            ornek(
                "Tepe noktası $(-1, 2)$ olan ve $y$ eksenini $3$ te kesen bir parabolün grafiği verilsin.",
                "Denklemi yazalım.",
                "$y=a(x+1)^2+2$ ve $x=0$ için $3=a+2$; $a=1$.",
                "$y=(x+1)^2+2=x^2+2x+3$. Bu, kökü olmayan parabol örneğindeki eğridir."),
            "Denklem yazmanın bütün yolları <a href=\"/blog/parabol-denklemi/\">Parabol Denklemi Nasıl Yazılır?</a> yazısında anlatılıyor.",
        ]},
        {"baslik": "Grafikten bilgi okumak", "icerik": [
            "Çizilmiş bir parabolden pek çok bilgi doğrudan okunur. Aşağıdaki tablo, $y=x^2-2x-3$ grafiğinden okunan bilgileri özetler.",
            tablo(["Soru", "Grafikte bakılan yer", "Cevap"], [
                ["Kollar hangi yöne?", "Eğrinin uçları", "Yukarı, $a>0$"],
                ["En küçük değer?", "Tepe noktası", "$-4$"],
                ["$f(x)=0$ ın kökleri?", "$x$ ekseni kesişimleri", "$-1$ ve $3$"],
                ["$f(x)<0$ nerede?", "Eksenin altı", "$(-1, 3)$"],
                ["Görüntü kümesi?", "En alçak nokta ve yukarısı", "$[-4, \\infty)$"],
            ]),
            ornek(
                "Aynı grafik verilsin.",
                "$f(x)=5$ denkleminin çözümlerini bulalım.",
                "$y=5$ doğrusunun grafiği kestiği noktalar aranır: $x^2-2x-3=5$, yani $x^2-2x-8=0$.",
                "$(x-4)(x+2)=0$; çözümler $-2$ ve $4$ tür."),
        ]},
        {"baslik": "Çizimi kontrol etmek", "icerik": [
            "Çizim bittikten sonra birkaç kısa kontrol grafiğin doğruluğunu güvenceye alır. Bu kontroller birkaç saniye sürer ama yanlış çizilmiş bir grafikten yanlış bilgi okunmasını önler.",
            tablo(["Kontrol", "Beklenen"], [
                ["Kolların yönü", "Baş katsayının işaretiyle uyumlu"],
                ["Simetri", "Eşleşen noktalar aynı yükseklikte"],
                ["$y$ ekseni kesişimi", "$(0, c)$"],
                ["Kök sayısı", "Diskriminantla uyumlu"],
            ]),
            "Bu dört kontrolden biri tutmuyorsa hesapta ya da çizimde bir hata vardır. En sık görülen hata, tepe noktasının işaretinin karıştırılmasıdır; tepe noktasını denklemde yerine yazmak bu hatayı hemen gösterir.",
        ]},
        {"baslik": "Sınavda parabol grafiği", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) parabol grafiği; grafiği verilen parabolün denklemini ya da katsayılarının işaretlerini bulma, grafikten değer ve aralık okuma ve iki grafiğin kesişimi biçiminde karşına çıkabilir.",
                "Mutlak değerli ve kısıtlı aralıktaki parabollerin grafikleri de sorulabilir."),
            "Grafik sorularında önce grafikte kesin okunabilen noktalara odaklan: tepe noktası, eksen kesişimleri ve ızgaraya tam oturan noktalar. Bu noktalar hem denklemi kurmaya hem de istenen değeri okumaya yeter.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["Eğriyi tepe noktasında sivri çizmek", "Tepe noktası düzgün bir kıvrımdır"],
                ["Simetrik noktaları farklı yüksekliğe koymak", "Simetrik noktalar aynı yükseklikte"],
                ["Kolları doğru gibi çizmek", "Kollar giderek dikleşir"],
                ["Kısıtlı aralıkta eğriyi uzatmak", "Yalnız aralıkta çizilir"],
                ["Mutlak değerde negatif kısmı bırakmak", "Eksenin altı yukarı yansıtılır"],
                ["Genişliği baş katsayıdan bağımsız çizmek", "Uzaklık $d$ ise yükseklik $ad^2$"],
            ]),
            "Bu hataların çoğu, eğriyi noktalar olmadan serbest elle çizmekten doğar. Tepe noktası ile en az dört simetrik nokta işaretlenip eğri bu noktalardan geçirilirse grafik hem doğru biçimde hem doğru genişlikte olur.",
        ]},
    ],
    "sss": [
        ("Parabol grafiği nasıl çizilir?",
         "Kolların yönüne bakılır, tepe noktası ve simetri ekseni bulunur, eksen kesişimleri ve simetrik noktalar işaretlenir. Noktalar düzgün bir eğriyle birleştirilir."),
        ("Kökü olmayan parabol nasıl çizilir?",
         "Tepe noktası, y ekseni kesişimi ve bu noktanın simetri eksenine göre simetriği kullanılır. Eğri x eksenini kesmez."),
        ("Parabolün genişliği grafikte nasıl doğru çizilir?",
         "Tepe noktasından d birim uzaktaki noktalar a çarpı d kare kadar yükseltilir. Bu noktalar işaretlenerek eğri çizilir."),
        ("Mutlak değerli parabolün grafiği nasıl çizilir?",
         "Önce parabol çizilir, x ekseninin altında kalan kısımlar eksene göre yukarı yansıtılır."),
        ("Grafikten eşitsizliğin çözümü nasıl okunur?",
         "f(x) küçüktür sıfır için grafiğin x ekseninin altında kaldığı aralık, büyüktür sıfır için üstünde kaldığı aralık okunur."),
        ("Ötelenmiş bir parabolün grafiği nasıl çizilir?",
         "Temel parabol çizilir ve her noktası tepe noktasındaki değişim kadar yatay ve dikey kaydırılır."),
        ("Parabol çizmek için en az kaç nokta gerekir?",
         "Tepe noktası ile her iki yanda birer yakın ve birer uzak nokta, yani beş nokta çoğu zaman yeterlidir. Simetri sayesinde bunların yalnızca üçü hesaplanır."),
    ],
    "kontrol": [
        "Parabol çizmenin adımlarını sırayla uygulayabiliyorum.",
        "Tepe noktası ve simetri ekseniyle grafiğin iskeletini kurabiliyorum.",
        "Değer tablosunu simetriden yararlanarak doldurabiliyorum.",
        "Kolları aşağı bakan parabolü çizebiliyorum.",
        "Kökü olmayan ve eksene teğet olan parabolleri çizebiliyorum.",
        "Tepe noktası ve kök biçiminden grafik çizebiliyorum.",
        "Baş katsayıya göre doğru genişlikte çizebiliyorum.",
        "Ötelemeyle grafik çizebiliyorum.",
        "Kısıtlı aralıktaki ve mutlak değerli parabolleri çizebiliyorum.",
        "Grafikten değer, aralık ve kesişim okuyabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["parabol-konu-anlatimi", "parabol-tepe-noktasi", "parabol-ve-dogru"],
}
