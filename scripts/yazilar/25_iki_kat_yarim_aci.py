# scripts/yazilar/25_iki_kat_yarim_aci.py — Iki Kat Aci ve Yarim Aci Formulleri (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "iki-kat-yarim-aci",
    "baslik": "İki Kat Açı ve Yarım Açı Formülleri",
    "aciklama": "İki kat açı ve yarım açı formülleri nelerdir? Kosinüsün üç biçimi, kuvvet azaltma, yarım açıda işaret, üç kat açı, denklem ve uygulamalar; çözümlü örneklerle.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "trigonometri",
    "sinavlar": ["AYT"],
    "kapak": "iki-kat-yarim-aci",
    "kapak_alt": "İki kat açı ve yarım açı formülleri: iki ahşap diskte aynı açı diliminin iki katına genişlemesini ve ikiye bölünmesini gösteren öğrenci",
    "ozet": "İki kat açı formülleri bir açının iki katının trigonometrik değerlerini, yarım açı formülleri ise yarısının değerlerini açının kendi değerleriyle hesaplar. İkisi de toplam formüllerinden doğar ve birbirinin tersidir. Bu yazıda sinüs, kosinüs ve tanjantın iki kat açı formüllerini, kosinüsün üç biçimini ve hangisinin ne zaman seçileceğini, kuvvet azaltma formüllerini, yarım açı formüllerini ve karekökte işaret seçimini, üç kat açı formüllerini, tanjant yarım açı dönüşümünü ve bu formüllerin sadeleştirme, denklem ve uygulama sorularında kullanımını çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "İki kat ve yarım açı nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için toplam formüllerini, özel açıların değerlerini ve temel özdeşliği biliyor olman yeterli.",
                "Temel bilgiler için <a href=\"/blog/trigonometrik-toplam-fark/\">Trigonometrik Toplam ve Fark Formülleri</a> ve <a href=\"/blog/trigonometrik-ozdeslikler-formuller/\">Trigonometrik Özdeşlikler ve Formüller</a> yazılarına göz at."),
            "Bir açının trigonometrik değerleri biliniyorsa iki katının ya da yarısının değerleri de hesaplanabilir. $\\sin 2x$ değeri $2\\sin x$ değildir ve $\\sin \\dfrac{x}{2}$ değeri de $\\dfrac{\\sin x}{2}$ değildir; açı iki katına çıktığında değerler karmaşık bir biçimde değişir. İki kat ve yarım açı formülleri bu değişimi tam olarak hesaplar.",
            "Kapaktaki öğrenci iki ahşap disk üzerinde aynı açı dilimiyle çalışıyor: soldaki diskte dilim iki katına genişletiliyor, sağdakinde ise ikiye bölünüyor. Yazının iki yarısı bu iki işleme karşılık geliyor.",
        ]},
        {"baslik": "İki kat açı formülleri nereden gelir?", "icerik": [
            "Toplam formüllerinde iki açı birbirine eşit alınırsa, yani $a=b=x$ yazılırsa iki kat açı formülleri doğrudan elde edilir:",
            tablo(["Toplam formülü", "$a=b=x$ için"], [
                ["$\\sin(a+b)=\\sin a \\cos b+\\cos a \\sin b$", "$\\sin 2x=2\\sin x \\cos x$"],
                ["$\\cos(a+b)=\\cos a \\cos b-\\sin a \\sin b$", "$\\cos 2x=\\cos^2 x-\\sin^2 x$"],
                ["$\\tan(a+b)=\\dfrac{\\tan a+\\tan b}{1-\\tan a \\tan b}$", "$\\tan 2x=\\dfrac{2\\tan x}{1-\\tan^2 x}$"],
            ]),
            "Bu yüzden iki kat açı formüllerini ayrıca ezberlemeye gerek yoktur; toplam formülü bilen biri onları birkaç saniyede yeniden kurabilir.",
        ]},
        {"baslik": "Sinüsün iki katı", "icerik": [
            "$\\sin 2x=2\\sin x \\cos x$ formülü, hem sinüse hem kosinüse ihtiyaç duyar. Yalnızca biri verildiğinde diğeri temel özdeşlikle ya da bir dik üçgenle bulunur.",
            ornek(
                "$x$ dar açı ve $\\sin x=\\dfrac{5}{13}$ olsun.",
                "$\\sin 2x$ değerini bulalım.",
                "Dik üçgenden ya da temel özdeşlikten $\\cos x=\\dfrac{12}{13}$ bulunur.",
                "$\\sin 2x=2 \\cdot \\dfrac{5}{13} \\cdot \\dfrac{12}{13}=\\dfrac{120}{169}$ olur."),
            "Formül tersten de çok kullanılır: $\\sin x \\cos x$ çarpımı $\\dfrac{\\sin 2x}{2}$ e eşittir. Örneğin $\\sin 22.5^\\circ \\cos 22.5^\\circ=\\dfrac{\\sin 45^\\circ}{2}=\\dfrac{\\sqrt{2}}{4}$ olur.",
        ]},
        {"baslik": "Kosinüsün üç biçimi", "icerik": [
            "$\\cos 2x=\\cos^2 x-\\sin^2 x$ formülünde $\\sin^2 x$ yerine $1-\\cos^2 x$ ya da $\\cos^2 x$ yerine $1-\\sin^2 x$ yazılınca iki yeni biçim daha elde edilir:",
            tablo(["Biçim", "Ne zaman seçilir?"], [
                ["$\\cos 2x=\\cos^2 x-\\sin^2 x$", "İki oran da biliniyorsa"],
                ["$\\cos 2x=2\\cos^2 x-1$", "Yalnızca kosinüs biliniyorsa"],
                ["$\\cos 2x=1-2\\sin^2 x$", "Yalnızca sinüs biliniyorsa"],
            ]),
            ornek(
                "$\\cos x=\\dfrac{1}{3}$ olsun.",
                "$\\cos 2x$ değerini bulalım.",
                "Yalnızca kosinüs bilindiği için $2\\cos^2 x-1$ biçimi seçilir.",
                "$\\cos 2x=2 \\cdot \\dfrac{1}{9}-1=-\\dfrac{7}{9}$ olur."),
            "Uygun biçim seçildiğinde eksik oranı bulmaya, dolayısıyla açının bölgesini düşünmeye gerek kalmaz. Kosinüsün iki katı, açının bölgesinden bağımsız olarak tek bir değer verir.",
        ]},
        {"baslik": "Tanjantın iki katı", "icerik": [
            "$\\tan 2x=\\dfrac{2\\tan x}{1-\\tan^2 x}$ formülü yalnızca tanjant cinsinden yazılmıştır; sinüs ya da kosinüse gerek yoktur. Paydanın sıfır olduğu durumda, yani $\\tan x=\\pm 1$ iken $\\tan 2x$ tanımsızdır.",
            ornek(
                "$\\tan x=\\dfrac{1}{2}$ olsun.",
                "$\\tan 2x$ değerini bulalım.",
                "$\\tan 2x=\\dfrac{2 \\cdot \\dfrac{1}{2}}{1-\\dfrac{1}{4}}=\\dfrac{1}{\\dfrac{3}{4}}$.",
                "Sonuç $\\dfrac{4}{3}$ olur."),
            "Tanjantın iki katı, açının bölgesini bilmeden yalnızca tanjant değeriyle hesaplanabildiği için tanjantı verilen sorularda en kısa yoldur. Sonucun işareti ise iki kat açının hangi bölgede bulunduğu hakkında da bilgi verir.",
        ]},
        {"baslik": "Bölgesi verilen açıda iki kat", "icerik": [
            "Açı ikinci bölgede olduğunda kosinüs negatiftir. Bu işaret $\\sin 2x$ in işaretini doğrudan etkiler; $\\cos 2x$ in işareti ise karelerin farkından belirlenir.",
            ornek(
                "$x$ ikinci bölgede ve $\\sin x=\\dfrac{12}{13}$ olsun.",
                "$\\sin 2x$ ve $\\cos 2x$ değerlerini bulalım.",
                "$\\cos x=-\\dfrac{5}{13}$. $\\sin 2x=2 \\cdot \\dfrac{12}{13} \\cdot \\left(-\\dfrac{5}{13}\\right)=-\\dfrac{120}{169}$.",
                "$\\cos 2x=\\dfrac{25}{169}-\\dfrac{144}{169}=-\\dfrac{119}{169}$ olur."),
            "İki değerin de negatif çıkması $2x$ açısının üçüncü bölgede olduğunu gösterir. Bu tutarlıdır: $x$ yaklaşık $112.6^\\circ$ olduğundan $2x$ yaklaşık $225.2^\\circ$ olur.",
        ]},
        {"baslik": "İki kattan açının oranlarına dönmek", "icerik": [
            "Bazı sorularda iki kat açının değeri verilir ve açının kendi oranları istenir. Bu durumda kosinüsün iki biçimi tersten kullanılır: $\\cos 2x$ biliniyorsa $\\sin^2 x$ ve $\\cos^2 x$ doğrudan hesaplanır, işaret ise açının bölgesinden seçilir.",
            ornek(
                "$x$ dar açı ve $\\cos 2x=\\dfrac{7}{25}$ olsun.",
                "$\\sin x$ ve $\\cos x$ değerlerini bulalım.",
                "$1-2\\sin^2 x=\\dfrac{7}{25}$ olduğundan $\\sin^2 x=\\dfrac{9}{25}$, yani $\\sin x=\\dfrac{3}{5}$.",
                "$2\\cos^2 x-1=\\dfrac{7}{25}$ olduğundan $\\cos^2 x=\\dfrac{16}{25}$, yani $\\cos x=\\dfrac{4}{5}$ olur."),
        ]},
        {"baslik": "Tersten kullanım kalıpları", "icerik": [
            "İki kat açı formüllerinin tersten okunuşu, uzun görünen ifadeleri tek bir değere indirir. En sık görülen üç kalıp şunlardır:",
            tablo(["İfade", "Eşiti"], [
                ["$2\\sin x \\cos x$", "$\\sin 2x$"],
                ["$\\cos^2 x-\\sin^2 x$", "$\\cos 2x$"],
                ["$1-2\\sin^2 x$ ya da $2\\cos^2 x-1$", "$\\cos 2x$"],
            ]),
            ornek(
                "$\\cos^2 22.5^\\circ-\\sin^2 22.5^\\circ$ ve $1-2\\sin^2 15^\\circ$ ifadeleri verilsin.",
                "İfadelerin değerini bulalım.",
                "Birincisi $\\cos 45^\\circ=\\dfrac{\\sqrt{2}}{2}$ olur.",
                "İkincisi $\\cos 30^\\circ=\\dfrac{\\sqrt{3}}{2}$ olur."),
        ]},
        {"baslik": "Kuvvet azaltma formülleri", "icerik": [
            "Kosinüsün iki biçimi kareli terim için çözülünce kuvvet azaltma formülleri elde edilir. Bu formüller kare terimi, iki kat açının birinci kuvvetine çevirir:",
            "$$\\sin^2 x=\\dfrac{1-\\cos 2x}{2}$$",
            "$$\\cos^2 x=\\dfrac{1+\\cos 2x}{2}$$",
            "Bu formüller integral hesabında, periyot sorularında ve dördüncü kuvvetli ifadeleri sadeleştirmede kullanılır. Kuvvet azalırken açının iki katına çıktığına dikkat etmek gerekir.",
        ]},
        {"baslik": "Dördüncü kuvvetler", "icerik": [
            "$\\sin^4 x+\\cos^4 x$ gibi ifadeler, iki kare toplamının karesinden yararlanılarak sadeleşir. $(\\sin^2 x+\\cos^2 x)^2=1$ olduğundan dördüncü kuvvetlerin toplamı $1-2\\sin^2 x \\cos^2 x$ tir.",
            ornek(
                "$\\sin^4 15^\\circ+\\cos^4 15^\\circ$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "$2\\sin^2 x \\cos^2 x=\\dfrac{\\sin^2 2x}{2}$ olduğundan ifade $1-\\dfrac{\\sin^2 30^\\circ}{2}$ olur.",
                "$1-\\dfrac{1}{8}=\\dfrac{7}{8}$ bulunur."),
            "Benzer yolla $\\cos^4 x-\\sin^4 x$ farkı, iki kare farkı olarak açılıp $(\\cos^2 x-\\sin^2 x)(\\cos^2 x+\\sin^2 x)=\\cos 2x$ biçimine iner.",
        ]},
        {"baslik": "Yarım açı formülleri", "icerik": [
            "Kuvvet azaltma formüllerinde $x$ yerine $\\dfrac{x}{2}$ yazılır ve karekök alınırsa yarım açı formülleri elde edilir:",
            "$$\\sin \\dfrac{x}{2}=\\pm\\sqrt{\\dfrac{1-\\cos x}{2}}$$",
            "$$\\cos \\dfrac{x}{2}=\\pm\\sqrt{\\dfrac{1+\\cos x}{2}}$$",
            hap("Karekökün önündeki işaret formülden gelmez.",
                "İşaret, yarım açının hangi bölgede olduğuna bakılarak seçilir."),
        ]},
        {"baslik": "Yarım açıyla değer hesaplamak", "icerik": [
            "Yarım açı formülleri, özel açıların yarısı olan $22.5^\\circ$ ve $15^\\circ$ gibi açıların değerlerini verir. Bu açılar birinci bölgede olduğu için karekökün işareti pozitiftir.",
            ornek(
                "$\\cos 22.5^\\circ$ ve $\\sin 22.5^\\circ$ değerleri istensin.",
                "Yarım açı formülleriyle bulalım.",
                "$\\cos 22.5^\\circ=\\sqrt{\\dfrac{1+\\cos 45^\\circ}{2}}=\\sqrt{\\dfrac{2+\\sqrt{2}}{4}}=\\dfrac{\\sqrt{2+\\sqrt{2}}}{2}$.",
                "$\\sin 22.5^\\circ=\\sqrt{\\dfrac{1-\\cos 45^\\circ}{2}}=\\dfrac{\\sqrt{2-\\sqrt{2}}}{2}$ olur."),
            "İki değerin karelerinin toplamı $\\dfrac{2+\\sqrt{2}}{4}+\\dfrac{2-\\sqrt{2}}{4}=1$ çıkar; temel özdeşlikle yapılan bu kontrol, hesapta hata olmadığını gösterir.",
        ]},
        {"baslik": "Yarım açıda işaret seçimi", "icerik": [
            "Açı birinci bölgede değilse yarım açının bölgesi dikkatle belirlenmelidir. $x$ açısı bir aralıktaysa $\\dfrac{x}{2}$ açısı bu aralığın yarısındadır; işaret bu yeni aralıktan okunur.",
            ornek(
                "$180^\\circ<x<270^\\circ$ ve $\\cos x=-\\dfrac{3}{5}$ olsun.",
                "$\\sin \\dfrac{x}{2}$ ve $\\cos \\dfrac{x}{2}$ değerlerini bulalım.",
                "$90^\\circ<\\dfrac{x}{2}<135^\\circ$ olduğundan yarım açı ikinci bölgededir: sinüs pozitif, kosinüs negatif.",
                "$\\sin \\dfrac{x}{2}=\\sqrt{\\dfrac{1+\\dfrac{3}{5}}{2}}=\\dfrac{2\\sqrt{5}}{5}$ ve $\\cos \\dfrac{x}{2}=-\\sqrt{\\dfrac{1-\\dfrac{3}{5}}{2}}=-\\dfrac{\\sqrt{5}}{5}$ olur."),
            dikkat(
                "Yarım açının bölgesini açının kendi bölgesiyle karıştırmak.",
                "Örnekte $x$ üçüncü bölgededir ama $\\dfrac{x}{2}$ ikinci bölgededir. İşaret $x$ e göre seçilseydi iki değerin de negatif alınması gerekirdi ve sinüsün işareti yanlış olurdu."),
        ]},
        {"baslik": "Tanjantın yarım açısı", "icerik": [
            "Tanjantın yarım açı formülü karekök içermeyen iki biçimde yazılabilir. Bu biçimler, $\\dfrac{\\sin x}{1+\\cos x}$ kesrinin pay ve paydası iki kat açı formülleriyle açılarak elde edilir:",
            "$$\\tan \\dfrac{x}{2}=\\dfrac{\\sin x}{1+\\cos x}=\\dfrac{1-\\cos x}{\\sin x}$$",
            ornek(
                "$\\tan 22.5^\\circ$ ve $\\tan 15^\\circ$ değerleri istensin.",
                "Karekök içermeyen biçimle bulalım.",
                "$\\tan 22.5^\\circ=\\dfrac{1-\\cos 45^\\circ}{\\sin 45^\\circ}=\\dfrac{1-\\dfrac{\\sqrt{2}}{2}}{\\dfrac{\\sqrt{2}}{2}}=\\sqrt{2}-1$.",
                "$\\tan 15^\\circ=\\dfrac{1-\\cos 30^\\circ}{\\sin 30^\\circ}=\\dfrac{1-\\dfrac{\\sqrt{3}}{2}}{\\dfrac{1}{2}}=2-\\sqrt{3}$ olur."),
            "Bu biçimin üstünlüğü işaret sorununu ortadan kaldırmasıdır: kesir kendi işaretini taşıdığı için bölge tartışmasına gerek kalmaz.",
        ]},
        {"baslik": "Tanjant yarım açı dönüşümü", "icerik": [
            "$t=\\tan \\dfrac{x}{2}$ yazılırsa sinüs ve kosinüs yalnızca $t$ cinsinden ifade edilebilir. Bu dönüşüm, farklı oranları içeren ifadeleri tek bir değişkene indirmenin güçlü bir yoludur:",
            tablo(["Oran", "$t=\\tan \\dfrac{x}{2}$ ile"], [
                ["$\\sin x$", "$\\dfrac{2t}{1+t^2}$"],
                ["$\\cos x$", "$\\dfrac{1-t^2}{1+t^2}$"],
                ["$\\tan x$", "$\\dfrac{2t}{1-t^2}$"],
            ]),
            ornek(
                "$\\tan \\dfrac{x}{2}=2$ olsun.",
                "$\\sin x$ ve $\\cos x$ değerlerini bulalım.",
                "$\\sin x=\\dfrac{2 \\cdot 2}{1+4}=\\dfrac{4}{5}$.",
                "$\\cos x=\\dfrac{1-4}{1+4}=-\\dfrac{3}{5}$ olur; kareleri toplamı $1$ dir."),
        ]},
        {"baslik": "Üç kat açı formülleri", "icerik": [
            "Üç kat açı, iki kat açı ile açının kendisinin toplamı olarak yazılır. Toplam formülü ve iki kat açı formülleri birlikte uygulanınca sonuç tek bir oran cinsinden elde edilir:",
            tablo(["Formül", "Açılımı"], [
                ["$\\sin 3x$", "$3\\sin x-4\\sin^3 x$"],
                ["$\\cos 3x$", "$4\\cos^3 x-3\\cos x$"],
            ]),
            ornek(
                "$x=60^\\circ$ için kosinüsün üç kat formülünü kontrol edelim.",
                "İki tarafı ayrı ayrı hesaplayalım.",
                "Sol taraf: $\\cos 180^\\circ=-1$.",
                "Sağ taraf: $4 \\cdot \\dfrac{1}{8}-3 \\cdot \\dfrac{1}{2}=\\dfrac{1}{2}-\\dfrac{3}{2}=-1$. İki taraf eşittir."),
        ]},
        {"baslik": "Sadeleştirme", "icerik": [
            "İki kat açı içeren kesirler, pay ve payda aynı açıya indirilince çoğu zaman tek bir orana sadeleşir. Paydada $1+\\cos 2x$ ya da $1-\\cos 2x$ görülüyorsa kosinüsün uygun biçimi seçilir; böylece sabit $1$ yok olur.",
            ornek(
                "$\\dfrac{1-\\cos 2x}{\\sin 2x}$ ifadesi verilsin.",
                "İfadeyi sadeleştirelim.",
                "Pay $1-(1-2\\sin^2 x)=2\\sin^2 x$, payda $2\\sin x \\cos x$ olur.",
                "Sadeleşince $\\dfrac{\\sin x}{\\cos x}=\\tan x$ kalır."),
            "Aynı yolla $\\dfrac{\\sin 2x}{1+\\cos 2x}$ ifadesinin de $\\tan x$ e eşit olduğu gösterilir. Bu iki kesir, tanjantın yarım açı formülünün $x$ yerine $2x$ yazılmış hâlidir.",
        ]},
        {"baslik": "Kotanjant ile tanjantın farkı", "icerik": [
            "İki kat açı formüllerinin kesirli ifadelerdeki bir başka kullanımı, $\\cot x-\\tan x$ farkıdır. Fark sinüs ve kosinüs cinsinden yazılıp paydalar eşitlenince pay $\\cos 2x$, payda ise $\\dfrac{\\sin 2x}{2}$ olur. Sonuçta $\\cot x-\\tan x=2\\cot 2x$ özdeşliği elde edilir.",
            ornek(
                "$\\cot 15^\\circ-\\tan 15^\\circ$ ifadesi verilsin.",
                "İfadenin değerini bulalım.",
                "Özdeşlikle ifade $2\\cot 30^\\circ$ olur.",
                "$2\\sqrt{3}$ bulunur; $\\cot 15^\\circ=2+\\sqrt{3}$ ve $\\tan 15^\\circ=2-\\sqrt{3}$ değerleriyle de aynı sonuç çıkar."),
        ]},
        {"baslik": "Özdeşlik ispatı", "icerik": [
            "İki kat açılı özdeşliklerde genellikle karmaşık taraf açılır ve temel özdeşlikle sadeleştirilir. Kare açılımlarında ortaya çıkan $2\\sin x \\cos x$ terimi $\\sin 2x$ olarak tanınmalıdır.",
            ornek(
                "$(\\sin x+\\cos x)^2=1+\\sin 2x$ eşitliği verilsin.",
                "Eşitliğin özdeşlik olduğunu gösterelim.",
                "Sol taraf açılır: $\\sin^2 x+2\\sin x \\cos x+\\cos^2 x$.",
                "Kareler toplamı $1$, orta terim $\\sin 2x$ tir; sonuç sağ tarafa eşittir."),
        ]},
        {"baslik": "İki kat açıyla denklem", "icerik": [
            "Denklemde $\\cos 2x$ ile $\\sin x$ birlikte görülüyorsa $\\cos 2x$ için $1-2\\sin^2 x$ biçimi seçilir. Böylece denklem $\\sin x$ e göre ikinci dereceden bir denkleme dönüşür.",
            ornek(
                "$[0^\\circ, 360^\\circ)$ aralığında $\\cos 2x+\\sin x=0$ denklemi verilsin.",
                "Denklemi çözelim.",
                "$1-2\\sin^2 x+\\sin x=0$, yani $2\\sin^2 x-\\sin x-1=0$ ve $(2\\sin x+1)(\\sin x-1)=0$.",
                "$\\sin x=1$ için $x=90^\\circ$; $\\sin x=-\\dfrac{1}{2}$ için $x=210^\\circ$ ya da $330^\\circ$."),
        ]},
        {"baslik": "En büyük ve en küçük değer", "icerik": [
            "$\\sin x \\cos x$ çarpımı içeren ifadeler iki kat açıyla tek bir sinüse indirilir; sonra sinüsün $-1$ ile $1$ arasında kalması kullanılır.",
            ornek(
                "$y=4\\sin x \\cos x+1$ fonksiyonu verilsin.",
                "En büyük ve en küçük değeri bulalım.",
                "$4\\sin x \\cos x=2\\sin 2x$ olduğundan $y=2\\sin 2x+1$ olur.",
                "$-2 \\le 2\\sin 2x \\le 2$ olduğundan $y$ en az $-1$, en fazla $3$ olur."),
        ]},
        {"baslik": "Uygulama: eğik atış menzili", "icerik": [
            "Fizikte yerden $v$ hızıyla ve yatayla $\\theta$ açısı yapacak biçimde atılan bir cismin menzili $R=\\dfrac{v^2 \\sin 2\\theta}{g}$ formülüyle bulunur. Formüldeki $\\sin 2\\theta$, iki kat açı formülünün $2\\sin \\theta \\cos \\theta$ çarpımından gelir.",
            ornek(
                "$v=20$ metre bölü saniye ve $g=10$ metre bölü saniye kare alınsın.",
                "$15^\\circ$, $45^\\circ$ ve $75^\\circ$ lik atışların menzillerini karşılaştıralım.",
                "$R=\\dfrac{400}{10}\\sin 2\\theta=40\\sin 2\\theta$. $15^\\circ$ için $40\\sin 30^\\circ=20$ metre.",
                "$75^\\circ$ için $40\\sin 150^\\circ=20$ metre; $45^\\circ$ için $40\\sin 90^\\circ=40$ metre ile en büyük menzil elde edilir."),
            "Tümler iki açıyla yapılan atışların aynı menzile ulaşması, $\\sin 2\\theta$ ile $\\sin(180^\\circ-2\\theta)$ değerlerinin eşit olmasından kaynaklanır.",
        ]},
        {"baslik": "Formüllerin özeti", "icerik": [
            tablo(["Konu", "Formül"], [
                ["İki kat sinüs", "$\\sin 2x=2\\sin x \\cos x$"],
                ["İki kat kosinüs", "$\\cos 2x=2\\cos^2 x-1=1-2\\sin^2 x$"],
                ["İki kat tanjant", "$\\tan 2x=\\dfrac{2\\tan x}{1-\\tan^2 x}$"],
                ["Kuvvet azaltma", "$\\sin^2 x=\\dfrac{1-\\cos 2x}{2}$"],
                ["Yarım açı", "$\\cos \\dfrac{x}{2}=\\pm\\sqrt{\\dfrac{1+\\cos x}{2}}$"],
                ["Tanjant yarım açı", "$\\tan \\dfrac{x}{2}=\\dfrac{1-\\cos x}{\\sin x}$"],
            ]),
            "Tablodaki her formül toplam formüllerinden ve temel özdeşlikten türetilebilir. Türetme yolunu bir kez kavramak, tabloyu ezberlemekten daha kalıcıdır.",
        ]},
        {"baslik": "Sınavda iki kat ve yarım açı", "icerik": [
            sinavda(
                "İleri düzeyde (<strong>AYT</strong>) bu formüller; bir orandan iki kat açının değerini bulma, kosinüsün uygun biçimini seçme, tersten kullanım kalıpları, yarım açıda işaret seçimi ve denklem çözme biçiminde karşına çıkabilir.",
                "Kuvvet azaltma formülleri periyot ve integral sorularında da dolaylı olarak gerekir."),
            "Soruda $\\sin x \\cos x$, $\\cos^2 x-\\sin^2 x$ ya da $1-2\\sin^2 x$ görüyorsan ilk iş bunları iki kat açıya çevirmektir. Yarım açı sorularında ise hesaba başlamadan önce yarım açının bölgesini yaz; işaret hatası bu soruların en yaygın tuzağıdır.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$\\sin 2x=2\\sin x$", "$\\sin 2x=2\\sin x \\cos x$"],
                ["$\\cos 2x=2\\cos x-1$", "$\\cos 2x=2\\cos^2 x-1$"],
                ["$\\sin \\dfrac{x}{2}=\\dfrac{\\sin x}{2}$", "Yarım açı formülü kullanılır"],
                ["Yarım açıda işareti açının bölgesinden almak", "Yarım açının bölgesinden"],
                ["Kuvvet azaltmada açıyı aynı bırakmak", "Açı iki katına çıkar"],
                ["$\\tan x=\\pm 1$ iken $\\tan 2x$ i hesaplamak", "$\\tan 2x$ tanımsızdır"],
            ]),
            "Bir formülün doğru hatırlanıp hatırlanmadığını $x=30^\\circ$ gibi bir özel açıyla denemek en güvenilir kontroldür. Örneğin $2\\cos^2 30^\\circ-1=\\dfrac{1}{2}=\\cos 60^\\circ$ olduğu için kosinüs biçimi doğrudur.",
        ]},
    ],
    "sss": [
        ("İki kat açı formülü nedir?",
         "sin 2x eşittir 2 sin x cos x, cos 2x eşittir cos kare x eksi sin kare x ve tan 2x eşittir 2 tan x bölü 1 eksi tan kare x tir."),
        ("cos 2x in üç biçimi nelerdir?",
         "cos kare x eksi sin kare x, 2 cos kare x eksi 1 ve 1 eksi 2 sin kare x tir. Hangi oran biliniyorsa ona uygun biçim seçilir."),
        ("Yarım açı formülünde işaret nasıl seçilir?",
         "Karekökün işareti, yarım açının bulunduğu bölgeye göre seçilir. Açının kendi bölgesi değil, yarısının bölgesi önemlidir."),
        ("Kuvvet azaltma formülü nedir?",
         "sin kare x eşittir 1 eksi cos 2x bölü 2, cos kare x eşittir 1 artı cos 2x bölü 2 dir."),
        ("tan 22.5 derece kaçtır?",
         "Tanjantın yarım açı formülüyle kök 2 eksi 1 bulunur."),
        ("Üç kat açı formülü nedir?",
         "sin 3x eşittir 3 sin x eksi 4 sin küp x, cos 3x eşittir 4 cos küp x eksi 3 cos x tir."),
    ],
    "kontrol": [
        "İki kat açı formüllerini toplam formüllerinden türetebiliyorum.",
        "Bir orandan iki kat açının sinüs, kosinüs ve tanjantını bulabiliyorum.",
        "Kosinüsün üç biçiminden uygun olanı seçebiliyorum.",
        "Bölgesi verilen açıda iki kat açının işaretlerini belirleyebiliyorum.",
        "Tersten kullanım kalıplarını tanıyabiliyorum.",
        "Kuvvet azaltma formüllerini kullanabiliyorum.",
        "Yarım açı formülleriyle değer hesaplayabiliyorum.",
        "Yarım açıda karekökün işaretini doğru seçebiliyorum.",
        "Tanjant yarım açı dönüşümünü ve üç kat açı formüllerini uygulayabiliyorum.",
        "İki kat açı formülleriyle sadeleştirme ve denklem çözme yapabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["trigonometrik-toplam-fark", "trigonometrik-ozdeslikler-formuller", "trigonometrik-denklemler"],
}
