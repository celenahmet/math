# scripts/yazilar/09_polinomlarda_kalan.py — Polinomlarda Kalan (25.09.2026)
# Standart: blog-YAZIM-STANDARDI.md · sayisal iddialar: scripts/blog_dogrula.py
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))
from blog_ogeler import hap, dikkat, ornek, onkosul, sinavda, tablo  # noqa: E402

YAZI = {
    "slug": "polinomlarda-kalan",
    "baslik": "Polinomlarda Kalan Bulma",
    "aciklama": "Polinomda kalan nasıl bulunur? Kalan teoremi, x − a, x + a ve ax + b ile kalan, çarpan teoremi, ikinci dereceden bölen ve bilinmeyen katsayılar; çözümlü.",
    "tarih": "2026-09-25",
    "guncelleme": None,
    "kategori": "polinomlar",
    "sinavlar": ["TYT", "AYT"],
    "kapak": "polinomlarda-kalan",
    "kapak_alt": "Polinomlarda kalan bulma: renkli bloklar dizildikten sonra ayrı bir kutuda kalan parçayı gösteren iki öğrenci",
    "ozet": "Bir polinomun başka bir polinomla bölümünden kalan, çoğu zaman bölme yapılmadan bulunabilir. Kalan teoremi bu kısa yolu verir: x − a ile bölümden kalan, polinomun a daki değeridir. Bu yazıda kalan teoremini ve nedenini, x − a, x + a ve ax + b biçimindeki bölenlerle kalanı, çarpan teoremini, bilinmeyen katsayıları bulmayı, ikinci dereceden ve yüksek dereceli bölenlerle kalanı ve bölme eşitliğinden kalan çıkarmayı çözümlü örneklerle ele alıyoruz.",
    "bolumler": [
        {"baslik": "Kalan teoremi nedir?", "icerik": [
            onkosul(
                "Bu yazıyı daha rahat anlamak için polinomlarda değer hesaplamayı ve bölme eşitliğini biliyor olman yeterli.",
                "Bölme işlemi için <a href=\"/blog/polinomlarda-bolme/\">Polinomlarda Bölme İşlemi</a> yazısına göz at."),
            "Bir $P(x)$ polinomunun $x-a$ ile bölümünden kalan, polinomun $x=a$ daki değerine eşittir. Bu sonuca <strong>kalan teoremi</strong> denir ve polinom bölmesinin en çok kullanılan kısa yoludur:",
            "$$P(x) \\text{ nin } x-a \\text{ ile bölümünden kalan}=P(a)$$",
            "Kalan teoremi sayesinde uzun bölme yapmadan, yalnızca bir değer hesaplayarak kalan bulunur. Kapaktaki öğrencilerin ayrı kutuya koyduğu tek parça gibi, kalan bölmenin sonunda artan küçük bir parçadır ve onu bulmak için bütün bölmeyi yapmak gerekmez.",
            hap("$x-a$ ile bölümden kalan $P(a)$ dır.",
                "Böleni sıfır yapan değer polinomda yerine yazılır."),
        ]},
        {"baslik": "Kalan teoremi neden doğrudur?", "icerik": [
            "Bölme eşitliği $P(x)=(x-a) \\cdot Q(x)+k$ biçimindedir. Bölen birinci dereceden olduğu için kalanın derecesi $0$ dır; yani kalan bir sabittir ve burada $k$ ile gösterilmiştir.",
            "Eşitlik her $x$ için doğru olduğundan $x=a$ için de doğrudur. $x=a$ yazılınca $(x-a)$ çarpanı sıfır olur ve bölüm ne olursa olsun çarpım yok olur: $P(a)=0 \\cdot Q(a)+k=k$. Kalan, polinomun $a$ daki değerine eşittir. Bölümün ne olduğunu bilmek gerekmez; çünkü sıfırla çarpıldığı için hangi polinom olursa olsun sonuca etkisi yoktur.",
            "Bu akıl yürütme, kalan teoreminin ezberlenecek bir kural değil, bölme eşitliğinin doğal bir sonucu olduğunu gösterir. Daha karmaşık bölenlerde de aynı fikir kullanılır: böleni sıfır yapan değerler bölme eşitliğine yerleştirilir.",
        ]},
        {"baslik": "x − a ile bölümden kalan", "icerik": [
            ornek(
                "$P(x)=x^3-2x^2+5$ polinomu verilsin.",
                "$x-2$ ile bölümünden kalanı bulalım.",
                "Böleni sıfır yapan değer: $x-2=0$, yani $x=2$.",
                "Kalan: $P(2)=8-8+5=5$."),
            "Aynı sonuç uzun bölmeyle de bulunur: $x^3-2x^2+5$ polinomu $x-2$ ye bölününce bölüm $x^2$, kalan $5$ tir. Kalan teoremi bu bölmenin tamamını tek bir değer hesabına indirir; üstelik bölünenin derecesi büyüdükçe kazanılan zaman da artar.",
        ]},
        {"baslik": "x + a ile bölümden kalan", "icerik": [
            "Bölen $x+a$ biçimindeyse onu sıfır yapan değer $-a$ dır, çünkü $x+a=x-(-a)$ biçiminde yazılabilir. Kalan $P(-a)$ dır.",
            ornek(
                "$P(x)=x^3-2x^2+5$ polinomu verilsin.",
                "$x+1$ ile bölümünden kalanı bulalım.",
                "$x+1=0$ için $x=-1$.",
                "Kalan: $P(-1)=-1-2+5=2$."),
            dikkat(
                "$x+1$ ile bölmede $P(1)$ i hesaplamak.",
                "Bölen sıfır yapılmalıdır: $x+1=0$ için $x=-1$ dir. $P(1)$ ise $x-1$ ile bölümden kalandır ve bu örnekte $4$ bulunur, yani yanlış sonuç verir."),
        ]},
        {"baslik": "ax + b ile bölümden kalan", "icerik": [
            "Bölen $ax+b$ biçimindeyse böleni sıfır yapan değer $x=-\\dfrac{b}{a}$ dir ve kalan polinomun bu noktadaki değeridir. Mantık aynıdır: bölme eşitliğinde bölen sıfır olunca geriye yalnızca kalan kalır.",
            ornek(
                "$P(x)=4x^2-2x+1$ polinomu verilsin.",
                "$2x-1$ ile bölümünden kalanı bulalım.",
                "$2x-1=0$ için $x=\\dfrac{1}{2}$.",
                "Kalan: $P(\\dfrac{1}{2})=4 \\cdot \\dfrac{1}{4}-1+1=1$."),
        ]},
        {"baslik": "x ile bölümden kalan", "icerik": [
            "Bölen yalnızca $x$ ise onu sıfır yapan değer $0$ dır ve kalan $P(0)$, yani polinomun sabit terimidir. Bu sonuç sezgiyle de açıktır: $x$ içeren bütün terimler $x$ e tam bölünür, geriye yalnızca sabit terim kalır.",
            ornek(
                "$P(x)=3x^4-7x^2+x-6$ polinomu verilsin.",
                "$x$ ile bölümünden kalanı bulalım.",
                "Kalan: $P(0)=-6$."),
        ]},
        {"baslik": "Kalan, katsayılar toplamı ve sabit terim", "icerik": [
            "Kalan teoremi, polinomlar konusundaki iki kısa yolu da açıklar. $x-1$ ile bölümden kalan $P(1)$ dir ve bu değer katsayıların toplamına eşittir. $x$ ile bölümden kalan $P(0)$ dır ve bu değer sabit terime eşittir.",
            ornek(
                "$P(x)=(x+1)^5$ polinomu verilsin.",
                "$x-1$ ile bölümünden kalanı ve katsayılar toplamını bulalım.",
                "Kalan: $P(1)=2^5=32$.",
                "Katsayılar toplamı da $32$ dir; iki soru aynı hesapla cevaplanır."),
            "Bu bağlantı, bir sorunun hangi biçimde sorulduğundan bağımsız olarak aynı hesabın yapılacağını gösterir. \"Katsayılar toplamı\" ile \"$x-1$ ile bölümden kalan\" aynı sayıdır.",
        ]},
        {"baslik": "Büyük kuvvetli polinomlarda kalan", "icerik": [
            "Polinomda çok büyük kuvvetler olsa da kalan teoremi işi kolaylaştırır. $x+1$ ya da $x-1$ ile bölmede $1$ ve $-1$ in kuvvetleri kolayca hesaplanır: $1$ in her kuvveti $1$, $-1$ in çift kuvvetleri $1$, tek kuvvetleri $-1$ dir.",
            ornek(
                "$P(x)=x^{100}+x^{51}+1$ polinomu verilsin.",
                "$x+1$ ve $x-1$ ile bölümlerinden kalanları bulalım.",
                "$x+1$ ile: $P(-1)=1-1+1=1$.",
                "$x-1$ ile: $P(1)=1+1+1=3$."),
        ]},
        {"baslik": "Çarpan teoremi", "icerik": [
            "Kalan teoreminin en önemli sonucu şudur: $P(a)=0$ ise $P(x)$ polinomu $x-a$ ile kalansız bölünür ve $x-a$, polinomun bir çarpanıdır. Tersine, $x-a$ bir çarpansa $P(a)=0$ dır. Bu sonuca <strong>çarpan teoremi</strong> denir.",
            ornek(
                "$P(x)=x^3-3x^2+4$ polinomu verilsin.",
                "$x-2$ nin bir çarpan olup olmadığını inceleyelim.",
                "$P(2)=8-12+4=0$.",
                "Kalan sıfır olduğu için $x-2$ bir çarpandır. Gerçekten $P(x)=(x-2)^2(x+1)$ dir."),
            "Çarpan teoremi, polinomları çarpanlarına ayırmanın ve köklerini bulmanın temel aracıdır. Ayrıntısı <a href=\"/blog/polinomlarda-carpanlara-ayirma/\">Polinomlarda Çarpanlara Ayırma</a> yazısında.",
        ]},
        {"baslik": "Kalandan bilinmeyen katsayı bulmak", "icerik": [
            "Polinomda bir bilinmeyen katsayı varsa ve bir bölmeden kalan verilmişse kalan teoremi bir denklem verir. Bu denklem çözülerek bilinmeyen bulunur. Kalansız bölünme bilgisi de aynı biçimde kullanılır; o durumda kalan sıfır alınır.",
            ornek(
                "$P(x)=x^3+kx^2-4$ polinomunun $x-2$ ile bölümünden kalan $8$ dir.",
                "$k$ yı bulalım.",
                "$P(2)=8+4k-4=8$.",
                "$4k=4$, yani $k=1$."),
            ornek(
                "$P(x)=x^3+mx+6$ polinomu $x+2$ ile kalansız bölünüyor.",
                "$m$ yi bulalım.",
                "$P(-2)=-8-2m+6=0$.",
                "$-2m=2$, yani $m=-1$."),
        ]},
        {"baslik": "İki bilinmeyen, iki kalan", "icerik": [
            "İki bilinmeyen katsayıyı bulmak için iki ayrı kalan bilgisi gerekir. Her kalan bir denklem verir; iki denklem birlikte çözülür. Denklemlerden biri ötekinden çıkarılınca çoğu zaman bir bilinmeyen hemen yok olur.",
            ornek(
                "$P(x)=x^2+ax+b$ polinomunun $x-1$ ile bölümünden kalan $2$, $x+2$ ile bölümünden kalan $5$ tir.",
                "$a$ ve $b$ yi bulalım.",
                "$P(1)=1+a+b=2$, yani $a+b=1$.",
                "$P(-2)=4-2a+b=5$, yani $b-2a=1$.",
                "Birinci denklemden ikinci çıkarılınca $3a=0$: $a=0$ ve $b=1$. Polinom $x^2+1$ dir."),
        ]},
        {"baslik": "Bileşik girdili polinomda kalan", "icerik": [
            "$P(2x+1)$ gibi bir ifadenin bir bölümden kalanı da aynı yolla bulunur: böleni sıfır yapan değer, ifadenin içine yazılır.",
            ornek(
                "$P(x)=x^2-x+2$ polinomu verilsin.",
                "$P(2x+1)$ ifadesinin $x-1$ ile bölümünden kalanı bulalım.",
                "$x=1$ için $2x+1=3$.",
                "Kalan: $P(3)=9-3+2=8$."),
            dikkat(
                "$P(2x+1)$ in $x-1$ ile bölümünden kalanı $P(1)$ sanmak.",
                "Yerine yazılan değer $x=1$ dir ama polinomun girdisi $2x+1$ dir. Bu yüzden $P(1)$ değil $P(3)$ hesaplanır."),
        ]},
        {"baslik": "Bölme eşitliğinden kalan bulmak", "icerik": [
            "Bazı sorularda polinom açıkça verilmez; yalnızca bir bölme eşitliği ve bölüm hakkında bilgi verilir. Böyle durumlarda istenen bölenin kökü bölme eşitliğine yazılır.",
            ornek(
                "$P(x)=(x-3) \\cdot Q(x)+5$ eşitliği veriliyor ve $Q(x)$ in $x-1$ ile bölümünden kalan $2$ dir.",
                "$P(x)$ in $x-1$ ile bölümünden kalanı bulalım.",
                "İstenen kalan $P(1)$ dir. Ayrıca $Q(1)=2$ dir.",
                "$P(1)=(1-3) \\cdot 2+5=1$."),
        ]},
        {"baslik": "Kalan koşullarından polinom kurmak", "icerik": [
            "Kalansız bölünme bilgileri polinomun köklerini verir. Polinomun derecesi ve baş katsayısı da biliniyorsa polinom tam olarak yazılabilir.",
            ornek(
                "İkinci dereceden, baş katsayısı $1$ olan bir $P(x)$ polinomu $x-1$ ve $x-3$ ile kalansız bölünüyor.",
                "$P(x)$ polinomunu ve $P(0)$ değerini bulalım.",
                "Kökler $1$ ve $3$ tür: $P(x)=(x-1)(x-3)=x^2-4x+3$.",
                "$P(0)=3$."),
        ]},
        {"baslik": "Bölümün değerini kalandan bulmak", "icerik": [
            "Bölme eşitliği, polinomun değeri biliniyorsa bölümün değerini bulmak için de kullanılır. Bilinen değer eşitliğe yazılır ve bölüm yalnız bırakılır.",
            ornek(
                "$P(x)=(x-2) \\cdot Q(x)+3$ eşitliği veriliyor ve $P(1)=7$ dir.",
                "$Q(x)$ polinomunun $x-1$ ile bölümünden kalanı bulalım.",
                "İstenen kalan $Q(1)$ dir. $x=1$ yazılır: $7=(1-2) \\cdot Q(1)+3$.",
                "$-Q(1)=4$, yani $Q(1)=-4$."),
        ]},
        {"baslik": "Horner ile değer hesaplamak", "icerik": [
            "Kalan teoremi tersinden de kullanılır: bir polinomun bir noktadaki değeri, o noktaya karşılık gelen bölmenin kalanıdır. Horner yöntemi bu yüzden aynı zamanda hızlı bir değer hesaplama yöntemidir; büyük kuvvetleri tek tek hesaplamak yerine yalnızca çarpma ve toplama yapılır.",
            ornek(
                "$P(x)=2x^4-3x^3+x-7$ polinomu verilsin.",
                "$P(2)$ değerini Horner yöntemiyle bulalım.",
                "Katsayılar: $2$, $-3$, $0$, $1$, $-7$. İşlemler: $2$; $2 \\cdot 2-3=1$; $1 \\cdot 2+0=2$; $2 \\cdot 2+1=5$; $5 \\cdot 2-7=3$.",
                "$P(2)=3$. Doğrudan hesap: $32-24+2-7=3$."),
        ]},
        {"baslik": "İkinci dereceden bölenle kalan", "icerik": [
            "Bölen ikinci dereceden olduğunda kalan en fazla birinci derecedendir ve $ax+b$ biçiminde yazılır. Bölenin iki gerçek kökü varsa bu kökler bölme eşitliğine yazılır; bölen sıfır olur ve kalan için iki denklem çıkar.",
            ornek(
                "$P(x)=x^4+x+1$ polinomu $x^2-1$ ile bölünsün.",
                "Kalanı bulalım.",
                "Kalan $ax+b$ olsun. Bölenin kökleri $1$ ve $-1$ dir.",
                "$P(1)=3=a+b$ ve $P(-1)=1=-a+b$. Buradan $b=2$ ve $a=1$.",
                "Kalan $x+2$ dir. Kontrol: $x^4+x+1=(x^2-1)(x^2+1)+x+2$."),
        ]},
        {"baslik": "Kökleri gerçek olmayan bölen", "icerik": [
            "Bölen $x^2+1$ gibi gerçek kökü olmayan bir ifadeyse kök yazma yöntemi doğrudan kullanılamaz. Bu durumda başka bir yol vardır: bölen sıfıra eşitlenir ve bulunan eşitlik polinomda yerine yazılarak derece düşürülür. $x^2+1=0$ ise $x^2$ yerine $-1$ yazılır.",
            ornek(
                "$P(x)=x^4+3x^3+x+2$ polinomu $x^2+1$ ile bölünsün.",
                "Kalanı bulalım.",
                "$x^2=-1$ yazılır: $x^4=(x^2)^2=1$ ve $x^3=x^2 \\cdot x=-x$.",
                "Kalan: $1+3 \\cdot (-x)+x+2=-2x+3$."),
            dikkat(
                "Derece indirgemeyi yarıda bırakmak.",
                "İndirgeme, polinomdaki bütün kuvvetler bölenin derecesinin altına inene kadar sürdürülür. $x^4$ ü indirip $x^3$ ü unutmak, kalan yerine yine bölenden büyük dereceli bir ifade bırakır."),
            "Bu yöntem bir derece indirgemesidir: polinomdaki büyük kuvvetler, bölenin sıfıra eşitlenmesiyle elde edilen ilişki yardımıyla adım adım küçültülür. Sonunda kalan derecesi bölenin derecesinden küçük olan ifade kalandır.",
        ]},
        {"baslik": "Yüksek dereceli bölenle derece indirgeme", "icerik": [
            "Aynı fikir $x^3-1$ gibi yüksek dereceli bölenlerde de işler. $x^3-1=0$ ise $x^3=1$ dir; polinomdaki her kuvvet, $3$ e bölümünden kalana göre küçültülür.",
            ornek(
                "$P(x)=x^7+x^4+x$ polinomu $x^3-1$ ile bölünsün.",
                "Kalanı bulalım.",
                "$x^3=1$ yazılır: $x^7=(x^3)^2 \\cdot x=x$ ve $x^4=x^3 \\cdot x=x$.",
                "Kalan: $x+x+x=3x$."),
            "Kalanın derecesi $1$ dir ve bölenin derecesi olan $3$ ten küçüktür; bu yüzden işlem burada biter. Bu tür sorularda kuvvetleri böleni oluşturan kuvvete göre gruplamak, uzun bölmenin onlarca adımını birkaç satıra indirir.",
        ]},
        {"baslik": "İki kalandan birleşik kalan", "icerik": [
            "Bir polinomun $x-1$ ve $x-2$ ile bölümlerinden kalanlar biliniyorsa, $(x-1)(x-2)$ ile bölümünden kalan da bulunabilir. Bölen ikinci dereceden olduğu için kalan $ax+b$ biçimindedir ve iki kalan bilgisi iki denklem verir.",
            ornek(
                "$P(x)$ polinomunun $x-1$ ile bölümünden kalan $3$, $x-2$ ile bölümünden kalan $5$ tir.",
                "$(x-1)(x-2)$ ile bölümünden kalanı bulalım.",
                "Kalan $ax+b$ olsun: $P(1)=a+b=3$ ve $P(2)=2a+b=5$.",
                "İkinci denklemden birinci çıkarılınca $a=2$, sonra $b=1$. Kalan $2x+1$ dir."),
        ]},
        {"baslik": "Büyük bölenin kalanından küçük bölenin kalanı", "icerik": [
            "Bir polinomun ikinci dereceden bir bölenle bölümünden kalan biliniyorsa, o bölenin çarpanlarıyla bölümden kalanlar hemen bulunur. Bölenin kökü bölme eşitliğine yazılınca bölen sıfır olur ve yalnızca kalanın o noktadaki değeri kalır.",
            ornek(
                "$P(x)$ polinomunun $x^2-4$ ile bölümünden kalan $2x+3$ tür.",
                "$P(x)$ in $x-2$ ve $x+2$ ile bölümlerinden kalanları bulalım.",
                "$x-2$ ile: $P(2)=2 \\cdot 2+3=7$.",
                "$x+2$ ile: $P(-2)=2 \\cdot (-2)+3=-1$."),
            "Bu sorunun tersi de aynı fikirle çözülür: küçük bölenlerin kalanları biliniyorsa büyük bölenin kalanı, iki denklemden bulunur. İki yönde de anahtar, bölenin köklerinde bölme eşitliğinin aldığı sade biçimdir.",
        ]},
        {"baslik": "Art arda bölmelerle kalan", "icerik": [
            "Bazen bir polinomun bölümü de yeniden bölünür ve iki bölmenin bilgileri birleştirilerek daha büyük bir bölene göre kalan istenir. Bu durumda iki bölme eşitliği iç içe yazılır.",
            ornek(
                "$P(x)$ in $x-1$ ile bölümünden bölüm $Q(x)$, kalan $4$ tür. $Q(x)$ in $x-2$ ile bölümünden kalan $3$ tür.",
                "$P(x)$ in $(x-1)(x-2)$ ile bölümünden kalanı bulalım.",
                "$P(x)=(x-1)Q(x)+4$ ve $Q(x)=(x-2)R(x)+3$.",
                "Yerine yazılınca: $P(x)=(x-1)(x-2)R(x)+3(x-1)+4$.",
                "Kalan $3x+1$ dir; derecesi bölenin derecesinden küçüktür."),
        ]},
        {"baslik": "Kalan ve bölüm birlikte gerektiğinde", "icerik": [
            "Kalan teoremi yalnızca kalanı verir. Soru bölümü de istiyorsa bölme yapılmalıdır; bölen $x-a$ biçimindeyse en kısa yol Horner yöntemidir. Horner tablosunun son sayısı kalandır ve kalan teoreminin verdiği değerle aynı olmalıdır; bu, işlemin doğruluğu için iyi bir kontroldür.",
            ornek(
                "$P(x)=x^3-2x^2+5$ polinomu $x-2$ ile bölünsün.",
                "Horner yöntemiyle bölümü ve kalanı bulup kalanı kalan teoremiyle karşılaştıralım.",
                "Katsayılar: $1$, $-2$, $0$, $5$. İşlemler: $1$; $1 \\cdot 2-2=0$; $0 \\cdot 2+0=0$; $0 \\cdot 2+5=5$.",
                "Bölüm $x^2$, kalan $5$ tir. Kalan teoremi de $P(2)=5$ vermişti."),
        ]},
        {"baslik": "Sınavda kalan soruları", "icerik": [
            sinavda(
                "Temel düzeyde (<strong>TYT</strong>) kalan soruları $x-a$ ya da $x+a$ ile bölümden kalan, kalansız bölünme ve tek bilinmeyenli katsayı bulma biçiminde karşına çıkabilir.",
                "İleri düzeyde (<strong>AYT</strong>) ikinci dereceden bölenle kalan, derece indirgeme, bölme eşitliğinden kalan ve iki bilinmeyenli sorular da sorulabilir."),
            "Kalan sorusu görünce ilk adım her zaman aynıdır: böleni sıfıra eşitle ve bulduğun değeri ya da ilişkiyi polinomda yerine koy. Bölen birinci derecedense bu tek bir değer hesabıdır; ikinci derecedense kalanı $ax+b$ diye yazıp iki denklem kurarsın.",
        ]},
        {"baslik": "Sık yapılan hatalar", "icerik": [
            tablo(["Hata", "Doğrusu"], [
                ["$x+a$ ile bölmede $P(a)$ hesaplamak", "$P(-a)$ hesaplanır"],
                ["$2x-1$ ile bölmede $P(1)$ hesaplamak", "$P(\\dfrac{1}{2})$ hesaplanır"],
                ["İkinci dereceden bölende kalanı sabit almak", "Kalan $ax+b$ biçimindedir"],
                ["$P(2x+1)$ de $x$ değerini doğrudan $P$ ye yazmak", "Önce $2x+1$ hesaplanır"],
                ["Kalansız bölünmeyi $P(a)=1$ sanmak", "Kalansız bölünme $P(a)=0$ dır"],
                ["Kalan teoremiyle bölümü bulmaya çalışmak", "Bölüm için bölme gerekir"],
            ]),
            "Bu hataların hepsi tek bir ilkeyi unutmaktan doğar: kalan, böleni sıfır yapan değerde polinomun aldığı değerdir. Bu ilke akılda tutulduğunda hangi değerin yerine yazılacağı kendiliğinden belli olur.",
        ]},
    ],
    "sss": [
        ("Kalan teoremi nedir?",
         "Bir polinomun x − a ile bölümünden kalan, polinomun a daki değerine eşittir. Uzun bölme yapmadan kalan bulmayı sağlar."),
        ("x + a ile bölümden kalan nasıl bulunur?",
         "Böleni sıfır yapan değer −a dır. Kalan, polinomda x yerine −a yazılarak bulunur."),
        ("Çarpan teoremi nedir?",
         "P(a) = 0 ise x − a polinomun bir çarpanıdır ve polinom x − a ile kalansız bölünür. Tersi de doğrudur."),
        ("İkinci dereceden bir bölenle kalan nasıl bulunur?",
         "Kalan ax + b biçiminde yazılır. Bölenin kökleri bölme eşitliğine yerleştirilerek a ve b için iki denklem kurulur."),
        ("Bölenin gerçek kökü yoksa kalan nasıl bulunur?",
         "Bölen sıfıra eşitlenir ve bulunan ilişkiyle polinomun derecesi düşürülür. x kare artı 1 ile bölmede x kare yerine −1 yazılır."),
        ("x ile bölümden kalan nedir?",
         "Polinomun sabit terimidir. x yerine 0 yazılınca x içeren bütün terimler kaybolur."),
        ("Bileşik girdili bir polinomun kalanı nasıl bulunur?",
         "Böleni sıfır yapan x değeri bulunur ve önce içteki ifadede yerine yazılır. P(2x + 1) in x − 1 ile bölümünden kalan P(3) tür."),
        ("Kalan teoremi bölümü de verir mi?",
         "Hayır, yalnızca kalanı verir. Bölüm gerekiyorsa uzun bölme ya da x − a biçimindeki bölenler için Horner yöntemi kullanılır."),
    ],
    "kontrol": [
        "Kalan teoremini yazabiliyor ve nedenini açıklayabiliyorum.",
        "x − a ve x + a ile bölümden kalanı bulabiliyorum.",
        "ax + b ile bölümden kalanı bulabiliyorum.",
        "x ile bölümden kalanın sabit terim olduğunu biliyorum.",
        "Çarpan teoremini uygulayabiliyorum.",
        "Kalan bilgisinden bilinmeyen katsayıları bulabiliyorum.",
        "Bileşik girdili bir polinomun kalanını bulabiliyorum.",
        "İkinci dereceden bir bölenle kalanı bulabiliyorum.",
        "Derece indirgeme yöntemini kullanabiliyorum.",
        "Bölme eşitliğinden kalan çıkarabiliyorum.",
    ],
    "kaynaklar": [
        ("MEB Ortaöğretim Matematik Dersi Öğretim Programı", "https://mufredat.meb.gov.tr/ProgramDetay.aspx?PID=343"),
    ],
    "ilgili": ["polinomlarda-bolme", "polinomlarda-carpanlara-ayirma", "polinomlar-konu-anlatimi"],
}
