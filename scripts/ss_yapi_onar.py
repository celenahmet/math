#!/usr/bin/env python3
# scripts/ss_yapi_onar.py — /ss/* (cikmis sorular) sayfalarinda kart
# satirlarinin (.row) kapanmayan/fazla kapanan div'lerini onarir.
#
# Neden: kpss ve dgs sayfalarinda her `.row` bir onceki kapanmadan aciliyordu
# (5 kat ic ice satir → her katta -15px kenar boslugu birikip sayfa mobilde
# saga tasiyordu: baslik kesik, yatay kaydirma). tyt'de 2021 karti satirin
# disinda kalmis, sonunda 3 fazla </div> vardi. Metin, baslik, baglanti
# DEGISMEZ; yalnizca div kapanislari ve karttaki fazla '"' isareti duzelir.
#
# Kullanim: python3 scripts/ss_yapi_onar.py [--kuru]
import re, sys, pathlib

KOK = pathlib.Path(__file__).resolve().parent.parent
KURU = "--kuru" in sys.argv
AC = re.compile(r"<div\b")

def onar(metin):
    a = metin.index('<section id="our-courses"')
    b = metin.index("</section>", a)
    satirlar = metin[a:b].split("\n")
    cikti, derinlik = [], 0
    for s in satirlar:
        t = s.strip()
        if t.startswith('<div class="row">') and derinlik >= 2:
            # onceki satir kapanmamis: container (1) seviyesine in
            cikti.append("\t\t\t</div>" * (derinlik - 1))
            derinlik = 1
        if t.startswith('<div class="col-sm-6 col-lg-3">') and derinlik == 1:
            # kart satirin disinda kalmis: satiri erken kapatan </div>'i geri al
            for i in range(len(cikti) - 1, -1, -1):
                if cikti[i].strip() == "</div>":
                    del cikti[i]; derinlik = 2; break
        if t.startswith("<h3") and "Bu soruların" in t and derinlik >= 2:
            cikti.append("\t\t\t</div>" * (derinlik - 1)); derinlik = 1
        ac, kapa = len(AC.findall(s)), s.count("</div>")
        if kapa and derinlik - (kapa - ac) < 0:
            fazla = (kapa - ac) - derinlik
            s = s.replace("</div>", "", fazla) if s.strip() == "</div>" and fazla else s
            kapa = s.count("</div>")
        derinlik += ac - kapa
        cikti.append(s)
    if derinlik > 0:
        cikti.append("\t\t</div>" * derinlik); derinlik = 0
    yeni = "\n".join(cikti)
    yeni = yeni.replace('<li>"<a', "<li><a")
    yeni = yeni.replace("<h3> <center> ", '<h3 class="text-center">')
    yeni = re.sub(r"<h3>(Bağlantılar|Yukarıdaki)", r'<h3 class="text-center">\1', yeni)
    return metin[:a] + yeni + metin[b:]

for p in sorted((KOK / "ss").glob("*/index.html")):
    eski = p.read_text(encoding="utf-8")
    yeni = onar(eski)
    ac, kapa = len(AC.findall(yeni)), yeni.count("</div>")
    print(f"{p.relative_to(KOK)}: div {ac}/{kapa} {'degisti' if yeni != eski else 'ayni'}")
    if not KURU and yeni != eski:
        p.write_text(yeni, encoding="utf-8")
