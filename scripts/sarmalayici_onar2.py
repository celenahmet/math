#!/usr/bin/env python3
# scripts/sarmalayici_onar2.py — icerikteki basibos </div>'ler .wrapper'i erken
# kapatiyordu (ana sayfa 329. satir, video sayfalari ~325). Kural: yalniz tek
# basina duran `</div>` satiri, ya yigin bosken ya da .wrapper'i "Wrapper End"
# satirindan once kapatacakken KALDIRILIR. Sonuc dogrulanir: wrapper tam
# "Wrapper End" satirinda kapanmali, fazla kapanis kalmamali.
import re, pathlib, sys
KOK = pathlib.Path(__file__).resolve().parent.parent
SAYFALAR = ["index.html", "parabol/index.html", "video/index.html", "video/parabol.html", "video/parabol2.html",
            "video/ucgen/index.html", "video/ucgen/parabol.html", "video/ucgen/parabol2.html"]

def onar(lines):
    end = next((i for i, l in enumerate(lines) if "Wrapper End" in l), None)
    if end is None: return lines, "Wrapper End yok"
    stack, cikar = [], set()
    for i, l in enumerate(lines):
        yalniz = l.strip() == "</div>"
        for m in re.finditer(r"<div\b[^>]*>|</div>", l):
            if m.group(0).startswith("</"):
                if not stack or (stack[-1] == "wrapper" and i < end - 1):
                    if yalniz: cikar.add(i); break
                    return lines, f"{i+1}: satir tek basina degil, elle bak"
                stack.pop()
            else:
                idm = re.search(r'class="([^"]*)"', m.group(0)); stack.append(idm.group(1).split()[0] if idm else "?")
    yeni = [l for i, l in enumerate(lines) if i not in cikar]
    # dogrulama
    stack = []; wrap = None; fazla = 0
    end2 = next(i for i, l in enumerate(yeni) if "Wrapper End" in l)
    for i, l in enumerate(yeni):
        for m in re.finditer(r"<div\b[^>]*>|</div>", l):
            if m.group(0).startswith("</"):
                if stack:
                    t = stack.pop()
                    if t == "wrapper" and wrap is None: wrap = i
                else: fazla += 1
            else:
                idm = re.search(r'class="([^"]*)"', m.group(0)); stack.append(idm.group(1).split()[0] if idm else "?")
    ok = (wrap == end2 - 1 or wrap == end2) and fazla == 0 and not stack
    return yeni, f"{len(cikar)} satir cikti · wrapper {wrap+1 if wrap else None}/{end2+1} · fazla {fazla} · acik {len(stack)} → {'OK' if ok else 'KONTROL'}"

for s in SAYFALAR:
    p = KOK / s
    lines = p.read_text(encoding="utf-8").split("\n")
    yeni, durum = onar(lines)
    if yeni != lines and "--kuru" not in sys.argv: p.write_text("\n".join(yeni), encoding="utf-8")
    print(f"{s}: {durum}")
