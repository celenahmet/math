#!/usr/bin/env python3
# scripts/pdf_uret.py — blog PDF'lerini uretir, surum defterini tutar (28.09.2026)
#
# Kullanim (<venv> = .venv/bin/python; segno ve pypdf orada):
#   <venv> scripts/pdf_uret.py ornek 66        → .pdf-yapim/ornek/ altina deneme PDF'i
#                                                 (defter degismez, yayina gitmez)
#   <venv> scripts/pdf_uret.py denetle         → icerigi degisip surumu artmamis yazi var mi
#   <venv> scripts/pdf_uret.py ilk             → defterde olmayan yazilara 1.0 kaydi
#   <venv> scripts/pdf_uret.py surum 66 hata "Ornek 3'teki EKOK sonucu 36 olarak duzeltildi."
#   <venv> scripts/pdf_uret.py bas             → dosyasi olmayan surumleri basar
#   <venv> scripts/pdf_uret.py yukle           → basilmis surumleri medya sunucusuna yukler, dogrular
#
# Sonra sayfalar: python3 scripts/blog_uygula.py && python3 scripts/pdf_sayfalar.py
#   && python3 scripts/sitemap_uret.py && python3 scripts/arama_uygula.py && python3 scripts/css_surum.py
#
# Surum turleri ve kural: scripts/pdf_veri.py basindaki aciklama.
# Kimlik (Ahmet 28.09): "belgenin yazar ve kimlik bilgileri ahmetcelen.com.tr
# adresine ait olmali". Yazar, olusturan, uretici hem Info sozlugunde hem XMP'de
# ahmetcelen.com.tr; Chrome'un (Skia) ve pypdf'in adi dosyada kalmaz.
import datetime, hashlib, json, pathlib, subprocess, sys, urllib.request
from xml.sax.saxutils import escape as xe

import pdf_veri as V
import pdf_sablon as S

YAPIM = V.KOK / ".pdf-yapim"
YAYIMLAYAN = "ahmetcelen.com.tr"


def _yazdir(isler):
    dosya = YAPIM / "isler.json"
    dosya.write_text(json.dumps(isler, ensure_ascii=False), encoding="utf-8")
    subprocess.run(["node", str(V.KOK / "scripts/pdf_yazdir.mjs"), str(dosya)], check=True)


def _xmp(baslik, konu, anahtar, kd, s, tarih_iso):
    dogrula = V.ALAN + V.dogrulama_yolu(kd, s["surum"])
    return f'''<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:xmp="http://ns.adobe.com/xap/1.0/"
    xmlns:pdf="http://ns.adobe.com/pdf/1.3/"
    xmlns:xmpRights="http://ns.adobe.com/xap/1.0/rights/"
    xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/">
   <dc:format>application/pdf</dc:format>
   <dc:title><rdf:Alt><rdf:li xml:lang="x-default">{xe(baslik)}</rdf:li></rdf:Alt></dc:title>
   <dc:creator><rdf:Seq><rdf:li>{YAYIMLAYAN}</rdf:li></rdf:Seq></dc:creator>
   <dc:publisher><rdf:Bag><rdf:li>{YAYIMLAYAN}</rdf:li></rdf:Bag></dc:publisher>
   <dc:description><rdf:Alt><rdf:li xml:lang="x-default">{xe(konu)}</rdf:li></rdf:Alt></dc:description>
   <dc:identifier>{kd} {s["surum"]}</dc:identifier>
   <dc:language><rdf:Bag><rdf:li>tr-TR</rdf:li></rdf:Bag></dc:language>
   <dc:rights><rdf:Alt><rdf:li xml:lang="x-default">© {s["tarih"][:4]} {YAYIMLAYAN}</rdf:li></rdf:Alt></dc:rights>
   <xmp:CreatorTool>{YAYIMLAYAN}</xmp:CreatorTool>
   <xmp:CreateDate>{tarih_iso}</xmp:CreateDate>
   <xmp:ModifyDate>{tarih_iso}</xmp:ModifyDate>
   <xmp:MetadataDate>{tarih_iso}</xmp:MetadataDate>
   <pdf:Producer>{YAYIMLAYAN}</pdf:Producer>
   <pdf:Keywords>{xe(anahtar)}</pdf:Keywords>
   <xmpRights:Marked>True</xmpRights:Marked>
   <xmpRights:WebStatement>{xe(dogrula)}</xmpRights:WebStatement>
   <xmpMM:DocumentID>{YAYIMLAYAN}:{kd}</xmpMM:DocumentID>
   <xmpMM:VersionID>{s["surum"]}</xmpMM:VersionID>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
<?xpacket end="w"?>'''


def _kimlik(yol, no, y, s):
    """Ust veri: baslik, yayimlayan, konu, dogrulama; klasik Info + XMP.
    Sayfa sayisini da dondurur."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import NameObject, StreamObject, TextStringObject
    r = PdfReader(yol)
    w = PdfWriter(clone_from=r)
    kd = V.kod(no)
    baslik = f"{y['baslik']} ({kd} Sürüm {s['surum']})"
    konu = f"{kd} · Sürüm {s['surum']} · {V.ALAN}{V.dogrulama_yolu(kd, s['surum'])}"
    anahtar = ", ".join([y["baslik"], "konu anlatımı", "PDF", YAYIMLAYAN] + [str(x) for x in y.get("sinavlar", [])])
    olusma = r.metadata.creation_date if r.metadata else None
    olusma = (olusma or datetime.datetime.now(datetime.timezone.utc)).astimezone(datetime.timezone.utc)
    w.add_metadata({
        "/Title": baslik, "/Author": YAYIMLAYAN, "/Subject": konu, "/Keywords": anahtar,
        "/Creator": YAYIMLAYAN, "/Producer": YAYIMLAYAN,
        "/ACKod": kd, "/ACSurum": s["surum"], "/ACIcerik": s["icerik"], "/ACDogrulama": V.ALAN + V.dogrulama_yolu(kd, s["surum"]),
    })
    xmp = StreamObject()
    xmp.set_data(_xmp(baslik, konu, anahtar, kd, s, olusma.strftime("%Y-%m-%dT%H:%M:%SZ")).encode("utf-8"))
    xmp.update({NameObject("/Type"): NameObject("/Metadata"), NameObject("/Subtype"): NameObject("/XML")})
    w._root_object[NameObject("/Metadata")] = w._add_object(xmp)
    w._root_object[NameObject("/Lang")] = TextStringObject("tr-TR")
    w.write(yol)
    return len(r.pages)


def kapak_jpg(kapak):
    """Kapak AVIF'inin PDF'e gomulecek JPEG kopyasi (macOS sips, kalite 82).
    Chrome JPEG'i yeniden kodlamadan (DCTDecode) gomer."""
    kaynak = V.KOK / "blog/kapak" / f"{kapak}.avif"
    hedef = YAPIM / "kapak" / f"{kapak}.jpg"
    if not hedef.exists() or hedef.stat().st_mtime < kaynak.stat().st_mtime:
        hedef.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "82",
                        str(kaynak), "--out", str(hedef)], check=True, capture_output=True)
    return hedef


def uc_varliklari():
    """Son sayfadaki UniConnectly logosu ve magaza rozetleri; bir kez indirilir,
    basim agdan bagimsiz kalir."""
    import uniconnectly_blok as UC
    hedefler = [(UC.LOGO, "logo.webp")] + [(g, e.lower().replace(" ", "-") + ".png") for e, g, _ in UC.MAGAZALAR]
    for adres, ad in hedefler:
        p = YAPIM / "uc" / ad
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True)
            istek = urllib.request.Request(adres, headers={"User-Agent": "ahmetcelen.com.tr pdf"})
            p.write_bytes(urllib.request.urlopen(istek, timeout=30).read())


def diger_varliklari():
    """Son sayfadaki diger yapimlarin logolari (yerel depolardan; yayindaki
    logolarla ayni dosyalar)."""
    import shutil
    ev = pathlib.Path.home() / "Developer"
    for kaynak, ad in ((ev / "bote-web/assets/img/educator-logo1.png", "bote.png"),
                       (ev / "veteriner-web/dist/vet-logo-full.png", "veterito.png")):
        hedef = YAPIM / "diger" / ad
        if not hedef.exists():
            hedef.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(kaynak, hedef)


def _hazirla(no, y, s):
    if y.get("kapak"):
        kapak_jpg(y["kapak"])
    kd = V.kod(no)
    sayfa = YAPIM / f"{V.kod_yol(kd)}.html"
    sayfa.write_text(S.belge(no, y, s), encoding="utf-8")
    return {"sayfa": "/.pdf-yapim/" + sayfa.name, "ust": S.ust_bilgi(), "alt": S.alt_bilgi(kd, s["surum"])}


def _bitir(cikti, no, y, s):
    sayfa_sayisi = _kimlik(str(cikti), no, y, s)
    veri = pathlib.Path(cikti).read_bytes()
    return {"sha256": hashlib.sha256(veri).hexdigest(), "bayt": len(veri), "sayfa": sayfa_sayisi}


def ornek(no):
    YAPIM.mkdir(exist_ok=True)
    uc_varliklari()
    diger_varliklari()
    no, y = next((n, y) for n, y in V.yazilar() if n == int(no))
    s = {"surum": "1.0", "tarih": datetime.date.today().isoformat(), "tur": "ilk",
         "not": "İlk yayın.", "icerik": V.icerik_ozeti(y)}
    cikti = YAPIM / "ornek" / V.dosya_adi(V.kod(no), y["slug"], s["surum"])
    is_ = _hazirla(no, y, s)
    is_["cikti"] = str(cikti)
    _yazdir([is_])
    bilgi = _bitir(cikti, no, y, s)
    print(f"ornek: {cikti} · {bilgi['sayfa']} sayfa · {bilgi['bayt'] // 1024} KB")


# ── surum defteri komutlari ──────────────────────────────────────────────
def denetle(sessiz=False):
    """Her yayindaki yazinin son surumu bugunku icerik ve sablonla ayni mi."""
    kayit = V.oku()
    eksik, degisen = [], []
    for no, y in V.yazilar():
        b = kayit["belgeler"].get(V.kod(no))
        s = V.son(b)
        if not s:
            eksik.append(V.kod(no))
            continue
        ozet = V.icerik_ozeti(y)
        if s["icerik"] != ozet or s.get("sablon") != V.SABLON:
            neden = "icerik" if s["icerik"] != ozet else f"sablon {s.get('sablon')}→{V.SABLON}"
            degisen.append(f"{V.kod(no)} ({y['slug']}): {neden}")
    if not sessiz:
        for x in eksik:
            print(f"  defterde yok: {x}  →  pdf_uret.py ilk")
        for x in degisen:
            print(f"  surum gerekli: {x}  →  pdf_uret.py surum <no> <tur> \"<not>\"")
        print(f"denetim: {len(eksik)} eksik, {len(degisen)} degisen")
    return not eksik and not degisen


def ilk():
    kayit = V.oku()
    bugun = datetime.date.today().isoformat()
    n = 0
    for no, y in V.yazilar():
        kd = V.kod(no)
        if kd in kayit["belgeler"]:
            continue
        kayit["belgeler"][kd] = {"no": no, "slug": y["slug"], "baslik": y["baslik"], "kategori": y["kategori"],
                                 "surumler": [{"surum": "1.0", "tarih": bugun, "tur": "ilk", "not": "İlk yayın.",
                                               "icerik": V.icerik_ozeti(y), "sablon": V.SABLON}]}
        n += 1
    V.yaz(kayit)
    print(f"ilk: {n} belgeye 1.0 kaydi eklendi")


def surum(no, tur, not_):
    assert tur in V.TURLER and tur != "ilk", f"tur: {', '.join(t for t in V.TURLER if t != 'ilk')}"
    assert len(not_.strip()) >= 10, "degisiklik notu okura yazilir; en az bir cumle"
    kayit = V.oku()
    no, y = next((n, y) for n, y in V.yazilar() if n == int(no))
    b = kayit["belgeler"][V.kod(no)]
    s = V.son(b)
    assert s.get("sha256"), f"{V.kod(no)} {s['surum']} henuz basilmadi; once bas/yukle"
    yeni = V.sonraki_surum(s["surum"], tur)
    b.update({"slug": y["slug"], "baslik": y["baslik"], "kategori": y["kategori"]})
    b["surumler"].append({"surum": yeni, "tarih": datetime.date.today().isoformat(), "tur": tur,
                          "not": not_.strip(), "icerik": V.icerik_ozeti(y), "sablon": V.SABLON})
    V.yaz(kayit)
    print(f"{V.kod(no)}: {s['surum']} → {yeni} ({V.TURLER[tur]})")


def bas():
    """Dosyasi olmayan butun surumleri TEK Chrome oturumunda basar."""
    YAPIM.mkdir(exist_ok=True)
    uc_varliklari()
    diger_varliklari()
    kayit = V.oku()
    yazi = dict(V.yazilar())
    isler, bekleyen = [], []
    for kd, b in kayit["belgeler"].items():
        s = V.son(b)
        if s.get("sha256"):
            continue
        y = yazi[b["no"]]
        assert s["icerik"] == V.icerik_ozeti(y), f"{kd}: icerik defterdeki ozetle ayni degil; once surum ac"
        # Once gecici adla basilir; SHA-256 belli olunca icerige bagli ada tasinir.
        cikti = V.YEREL_DIZIN / (V.dosya_adi(kd, y["slug"], s["surum"])[:-4] + ".yapim.pdf")
        is_ = _hazirla(b["no"], y, s)
        is_["cikti"] = str(cikti)
        isler.append(is_)
        bekleyen.append((kd, b, s, y, cikti))
    if not isler:
        print("bas: basilacak surum yok")
        return
    _yazdir(isler)
    for kd, b, s, y, cikti in bekleyen:
        s.update(_bitir(cikti, b["no"], y, s))
        s["dosya"] = V.dosya_adi(kd, y["slug"], s["surum"], s["sha256"][:8])
        cikti.rename(V.YEREL_DIZIN / s["dosya"])
    V.yaz(kayit)
    toplam = sum(s["bayt"] for _, _, s, _, _ in bekleyen)
    print(f"bas: {len(bekleyen)} PDF · toplam {toplam / 1048576:.1f} MB")


def yukle():
    """Basilmis ama yuklenmemis surumleri sunucuya koyar. Var olan dosyanin
    USTUNE YAZMAZ (--ignore-existing): yayimlanmis surum degismez. Sonra her
    dosyanin sunucudaki SHA-256'si ve medya adresinden inen boyut denetlenir."""
    kayit = V.oku()
    bekleyen = [(kd, s) for kd, b in kayit["belgeler"].items() for s in b["surumler"]
                if s.get("sha256") and not s.get("yuklendi")]
    if not bekleyen:
        print("yukle: yuklenecek surum yok")
        return
    dosyalar = [str(V.YEREL_DIZIN / s["dosya"]) for _, s in bekleyen]
    subprocess.run(["ssh", "myserver", f"mkdir -p {V.SUNUCU_DIZIN} && chmod 755 {V.SUNUCU_DIZIN}"], check=True)
    # macOS'un rsync'i (openrsync) --chmod bilmiyor; izin sunucuda ayrica verilir.
    subprocess.run(["rsync", "-a", "--ignore-existing", *dosyalar, f"myserver:{V.SUNUCU_DIZIN}/"], check=True)
    subprocess.run(["ssh", "myserver", f"chmod 644 {V.SUNUCU_DIZIN}/*.pdf"], check=True)
    ozetler = subprocess.run(["ssh", "myserver", f"cd {V.SUNUCU_DIZIN} && sha256sum " + " ".join(f"'{s['dosya']}'" for _, s in bekleyen)],
                             check=True, capture_output=True, text=True).stdout
    sunucu = {ad.strip(): h for h, ad in (x.split(None, 1) for x in ozetler.strip().splitlines())}
    bugun = datetime.date.today().isoformat()
    hata = []
    for kd, s in bekleyen:
        if sunucu.get(s["dosya"]) != s["sha256"]:
            hata.append(f"{kd} {s['surum']}: sunucudaki dosya farkli (ustune yazilmadi, elle incele)")
            continue
        istek = urllib.request.Request(V.medya_adresi(s["dosya"]), method="HEAD", headers={"User-Agent": "ahmetcelen.com.tr pdf"})
        with urllib.request.urlopen(istek, timeout=30) as yanit:
            if yanit.status != 200 or int(yanit.headers.get("Content-Length", -1)) != s["bayt"]:
                hata.append(f"{kd} {s['surum']}: medya adresi {yanit.status}, boyut {yanit.headers.get('Content-Length')}")
                continue
        s["yuklendi"] = bugun
    V.yaz(kayit)
    print(f"yukle: {len(bekleyen) - len(hata)} / {len(bekleyen)} dosya yayinda")
    for x in hata:
        print("  !", x)
    if hata:
        sys.exit(1)


def on_yayin_yenile(onay=""):
    """DUYURU ONCESI tek seferlik izin (Ahmet 28.09: "PDF 1.1 yapmana gerek yok,
    henuz hic yayimlamadik; bu reklamlar icin surum degistirme"). Butun
    belgeler yalniz 1.0'daysa ve defterde "duyuru" tarihi yoksa 1.0 YENIDEN
    basilir: ayni surum, yeni dosya (adinda yeni ozet), eski dosya adlari
    `silinecek` listesine yazilir (eski_sil). Duyurudan sonra bu komut calismaz;
    her degisiklik yeni surumdur."""
    assert onay == "EVET", "kullanim: on_yayin_yenile EVET"
    kayit = V.oku()
    assert not kayit.get("duyuru"), f"belgeler {kayit['duyuru']} tarihinde duyuruldu; yeni surum acin"
    yazi = dict(V.yazilar())
    silinecek = kayit.setdefault("silinecek", [])
    for kd, b in kayit["belgeler"].items():
        assert len(b["surumler"]) == 1 and b["surumler"][0]["tur"] == "ilk", f"{kd}: birden fazla surum var"
        s = b["surumler"][0]
        if s.get("dosya"):
            silinecek.append(s["dosya"])
        for alan in ("sha256", "bayt", "sayfa", "dosya", "yuklendi"):
            s.pop(alan, None)
        s["icerik"] = V.icerik_ozeti(yazi[b["no"]])
        s["sablon"] = V.SABLON
    V.yaz(kayit)
    print(f"on_yayin_yenile: {len(kayit['belgeler'])} belge 1.0 olarak yeniden basilacak; {len(silinecek)} eski dosya silinecek")


def eski_sil():
    """on_yayin_yenile sonrasi: yeni dosyalar yayinda ve sayfalar yeni dosyaya
    baglandiktan SONRA eski dosyalari sunucudan ve yerelden siler."""
    kayit = V.oku()
    liste = kayit.get("silinecek", [])
    kullanilan = {s.get("dosya") for b in kayit["belgeler"].values() for s in b["surumler"]}
    liste = [d for d in liste if d not in kullanilan]
    if not liste:
        print("eski_sil: silinecek dosya yok")
        return
    import shlex
    subprocess.run(["ssh", "myserver", "cd " + V.SUNUCU_DIZIN + " && rm -f " + " ".join(shlex.quote(d) for d in liste)], check=True)
    for d in liste:
        (V.YEREL_DIZIN / d).unlink(missing_ok=True)
    kayit.pop("silinecek", None)
    V.yaz(kayit)
    print(f"eski_sil: {len(liste)} eski dosya silindi")


if __name__ == "__main__":
    komut, *arg = sys.argv[1:] or ["?"]
    islevler = {"ornek": ornek, "denetle": lambda: sys.exit(0 if denetle() else 1), "ilk": ilk,
                "surum": surum, "bas": bas, "yukle": yukle,
                "on_yayin_yenile": on_yayin_yenile, "eski_sil": eski_sil}
    if komut not in islevler:
        sys.exit(f"komut: {', '.join(islevler)}")
    islevler[komut](*arg)
