#!/usr/bin/env python3
# scripts/pdf_veri.py — blog yazilarinin PDF surum defteri ve ortak yardimcilar
# (28.09.2026)
#
# Ahmet (28.09): "yazilarin guzel tasarimli PDF'ini olusturacagiz; PDF merkezi
# olacak; her yazinin surumu olacak, surumler teyit edilebilir olacak; yazi
# numarasi, yazi kodu ve QR kod olacak. QR hem siteye goturecek hem guncelligini
# kontrol ettirecek. Degisiklikleri surum gecmisi olarak her yazida yazariz;
# amacimiz bir hatamiz olursa bunu guncel olarak paylasmak. PDF sonradan
# degistirilemedigi icin kullanicinin elindekine boyle bir cozum buldum."
# Kararlar (28.09, Ahmet): kod AC-010 · Surum 1.2; merkez /pdf/, dogrulama
# /d/ac-010/1-0/; PDF'ler Google'a kapali (medya zaten noindex); bekleme
# ekraninda UniConnectly, PDF'te site tanitimi.
#
# TEK KAYNAK: pdf/kayit.json (depoda, yayinda /pdf/kayit.json). Surumler
# YALNIZ EKLENIR; yayimlanmis bir surumun dosyasi, ozeti, tarihi degismez.
# Dogrulama sayfalari ve tarayicidaki dosya denetimi bu dosyayi okur.
#
# Surum kurali:
#   ilk      → 1.0
#   bicim    → x.(y+1)  sayfa duzeni / sablon degisti, icerik ayni
#   duzeltme → x.(y+1)  yazim, anlatim, gorsel duzeltmesi
#   hata     → (x+1).0  matematiksel ya da olgusal HATA duzeltildi
#   icerik   → (x+1).0  yeni bolum, ornek, bilgi eklendi
# Eski bir surumden sonra "hata" turunde bir surum varsa dogrulama sayfasi
# o eski surumu KIRMIZI gosterir: elindeki belgede hata var, guncelini kullan.
#
# Icerik ozeti PDF'e giren GOVDE HTML'inden hesaplanir (kaynak sozlukten
# degil): matematik.py ya da kutu HTML'i degisse bile PDF'in icerigi
# degistiyse ozet degisir ve yeni surum istenir (pdf_uret.py denetle).
import hashlib, json, pathlib, re, sys

KOK = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(KOK / "scripts"))
import blog_veri                                  # noqa: E402

ALAN = "https://ahmetcelen.com.tr"
MEDYA = "https://medya.ahmetcelen.com.tr"
KAYIT = KOK / "pdf" / "kayit.json"
YEREL_DIZIN = KOK / "pdf" / "blog"                # uretilen PDF'ler (git ve Vercel disi)
SUNUCU_DIZIN = "/srv/docker/ahmetcelen/pdf/blog"  # medya konteyneri bu koku salt okunur sunar
YAYIN_YOLU = "/pdf/blog/"                          # medya.ahmetcelen.com.tr/pdf/blog/<dosya>

# Yazdirma sablonu surumu. Sablon/CSS/alt bilgi degisince 1 artir: denetim
# butun belgeler icin "bicim" surumu ister (eski PDF'ler eski sablonda kalir).
SABLON = 4
# 4 (28.09): Diger yapimlarimiz cumlesi toparlandi, UniConnectly de bizim yapimimiz diye metinde.
# 3 (28.09): alt bilgi ve ilk sayfadaki site adi tiklanabilir (URI notlari).
# 2 (28.09): son sayfada "Diger yapimlarimiz" (BOTE, Veterito), site blogu 3 sutun.
# Duyuru oncesi oldugu icin 1.0 yeniden basildi (pdf_uret.py on_yayin_yenile), surum acilmadi.

# /pdf/<slug>/ indirme sayfalari; /pdf/ altindaki eski sayfa adlariyla cakismasin.
AYRILMIS = {"blog", "parabol", "kayit"}

TURLER = {
    "ilk": "İlk yayın",
    "bicim": "Biçim güncellemesi",
    "duzeltme": "Düzeltme",
    "hata": "Hata düzeltmesi",
    "icerik": "İçerik güncellemesi",
}
AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz",
         "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


def tr_tarih(iso):
    y, a, g = (int(x) for x in iso.split("-"))
    return f"{g} {AYLAR[a - 1]} {y}"


# ── yazilar (numarali) ───────────────────────────────────────────────────
def yazilar():
    """(no, YAZI) ciftleri, numara sirasiyla. Numara dosya adindaki sayidir
    (scripts/yazilar/10_carpanlara_ayirma.py → 10); blog_veri de sirayi
    oradan aliyor. Taslaklar PDF'e girmez."""
    dosyalar = sorted((KOK / "scripts/yazilar").glob("[0-9]*.py"),
                      key=lambda p: int(p.stem.split("_")[0]))
    no_of = {}
    for p in dosyalar:
        m = re.search(r'"slug":\s*"([a-z0-9-]+)"', p.read_text(encoding="utf-8"))
        if m:
            no_of[m.group(1)] = int(p.stem.split("_")[0])
    out = []
    for y in blog_veri.yayinda():
        no = no_of.get(y["slug"])
        assert no is not None, f"pdf_veri: {y['slug']} icin dosya numarasi bulunamadi"
        assert y["slug"] not in AYRILMIS, f"pdf_veri: {y['slug']} /pdf/ altinda ayrilmis bir ad"
        out.append((no, y))
    nolar = [n for n, _ in out]
    assert len(nolar) == len(set(nolar)), "pdf_veri: iki yazi ayni numarayi tasiyor"
    return sorted(out, key=lambda t: t[0])


def kod(no):
    return f"AC-{no:03d}"


def kod_yol(k):
    return k.lower()                      # AC-010 → ac-010


def surum_yol(s):
    return s.replace(".", "-")            # 1.2 → 1-2


def dogrulama_yolu(k, s=None):
    return f"/d/{kod_yol(k)}/" + (f"{surum_yol(s)}/" if s else "")


def indirme_yolu(slug):
    return f"/pdf/{slug}/"


def dosya_adi(k, slug, s, kisa=None):
    # Indirilen dosya kullanicinin klasorunde de anlasilsin: kod + konu + surum.
    # "-konu-anlatimi-pdf" ile biten adreslerde sondaki "-pdf" tekrar etmesin.
    # `kisa`: dosyanin SHA-256'sinin ilk 8 hanesi. Adres icerige bagli olur;
    # ayni adreste farkli bayt ASLA sunulmaz (medya 1 yil "immutable" onbellekli).
    konu = re.sub(r"-pdf$", "", slug)
    return f"{kod_yol(k)}-{konu}-s{surum_yol(s)}" + (f"-{kisa}" if kisa else "") + ".pdf"


def pdf_adi(baslik):
    """Gorunen PDF adi (Ahmet 28.09): yazinin adi + PDF; adinda PDF varsa ikinci
    kez eklenmez; soru isaretiyle biten baslikta "Nedir? PDF" yerine "(PDF)"."""
    if "PDF" in baslik:
        return baslik
    return f"{baslik} (PDF)" if baslik.rstrip().endswith("?") else f"{baslik} PDF"


def medya_adresi(dosya):
    return MEDYA + YAYIN_YOLU + dosya


# ── surum defteri ────────────────────────────────────────────────────────
def oku():
    if KAYIT.exists():
        return json.loads(KAYIT.read_text(encoding="utf-8"))
    return {"aciklama": ("ahmetcelen.com.tr blog PDF surum defteri. Her belge (AC-NNN) icin "
                         "yayimlanan surumler, dosyalarin SHA-256 ozetleri ve degisiklik notlari. "
                         "Dogrulama: https://ahmetcelen.com.tr/d/"),
            "sablon": SABLON, "belgeler": {}}


def yaz(kayit):
    kayit["sablon"] = SABLON
    kayit["belgeler"] = dict(sorted(kayit["belgeler"].items()))
    KAYIT.parent.mkdir(parents=True, exist_ok=True)
    metin = json.dumps(kayit, ensure_ascii=False, indent=1) + "\n"
    if not KAYIT.exists() or KAYIT.read_text(encoding="utf-8") != metin:
        KAYIT.write_text(metin, encoding="utf-8")


def son(belge):
    return belge["surumler"][-1] if belge and belge.get("surumler") else None


def yayinda_mi(s):
    """Dosyasi uretilmis ve sunucuya yuklenmis surum."""
    return bool(s.get("sha256")) and bool(s.get("yuklendi"))


def yayindaki_son(belge):
    for s in reversed(belge.get("surumler", []) if belge else []):
        if yayinda_mi(s):
            return s
    return None


def sonraki_surum(onceki, tur):
    if onceki is None:
        return "1.0"
    b, k = (int(x) for x in onceki.split("."))
    return f"{b + 1}.0" if tur in ("hata", "icerik") else f"{b}.{k + 1}"


def durum(belge, s):
    """Bir surumun bugunku durumu: guncel / eski / hata.
    Yalniz YAYINDAKI surumler hesaba katilir; henuz yuklenmemis bir surum
    elindeki belgeyi eskitmez."""
    yayinda = [x for x in belge["surumler"] if yayinda_mi(x)]
    sira = [x["surum"] for x in yayinda]
    if s["surum"] not in sira or s["surum"] == sira[-1]:
        return "guncel"
    sonraki = yayinda[sira.index(s["surum"]) + 1:]
    return "hata" if any(x["tur"] == "hata" for x in sonraki) else "eski"


# ── PDF govdesi ve icerik ozeti ──────────────────────────────────────────
def _mutlak(parca):
    # Ic baglantilar PDF'te yerel sunucuya degil siteye gitmeli.
    return re.sub(r'href="/(?!/)', f'href="{ALAN}/', parca)


def govde(y):
    """PDF'e giren icerik: bolumler, hap ozeti, sik sorulanlar, kontrol listesi.
    Ekran ogeleri (paylas, yorum, oneriler, okuma konumu) yok. Formuller MathML."""
    import blog_uygula as B      # agir modul; yalniz gerektiginde
    parca = ""
    for b in y["bolumler"]:
        icerik = "\n".join(p if p.lstrip().startswith("<") else f"<p>{p}</p>" for p in b["icerik"])
        parca += f'<h2 id="{B.kimlik(b["baslik"])}">{B.k(b["baslik"])}</h2>\n{icerik}\n'
    parca = B._olu_baglantiyi_duzle(y["slug"], parca)
    ozet, _ = B.hap_ozeti(parca)
    ek = ozet
    if y.get("sss"):
        ek += (B.bolum_basligi("b-sss", "sss", "Sık sorulanlar")
               + "".join(f'<div class="p-sss"><p class="p-soru">{B.k(s)}</p><p>{c}</p></div>'
                         for s, c in y["sss"]) + "\n")
    if y.get("kontrol"):
        # Basili listede isaretlenecek bos kutular: ogrenci kagit uzerinde isaretler.
        ek += (B.bolum_basligi("b-kontrol", "kontrol", "Kontrol listesi")
               + '<ul class="p-kontrol">' + "".join(f"<li>{m}</li>" for m in y["kontrol"]) + "</ul>\n")
    return _mutlak(B.mm(parca) + B.mm(ek))


def bolumler(y):
    """Icindekiler: (kimlik, baslik)."""
    import blog_uygula as B
    out = [(B.kimlik(b["baslik"]), b["baslik"]) for b in y["bolumler"]]
    if "bs-hap" in "".join("".join(b["icerik"]) for b in y["bolumler"]):
        out.append(("b-hap-ozet", "Hap bilgi özeti"))
    if y.get("sss"):
        out.append(("b-sss", "Sık sorulanlar"))
    if y.get("kontrol"):
        out.append(("b-kontrol", "Kontrol listesi"))
    return out


def icerik_ozeti(y):
    """PDF'in icerigini belirleyen her seyin SHA-256'si: baslik, ozet, kategori,
    sinavlar, kapak gorselinin baytlari ve govde HTML'i."""
    h = hashlib.sha256()
    for parca in (y["baslik"], y["ozet"], y["kategori"], ",".join(map(str, y.get("sinavlar", [])))):
        h.update(parca.encode("utf-8") + b"\x00")
    if y.get("kapak"):
        h.update((KOK / "blog/kapak" / f"{y['kapak']}.avif").read_bytes())
    h.update(govde(y).encode("utf-8"))
    return h.hexdigest()


def parmak_izi(ozet):
    """Kapakta basilan kisa icerik ozeti: 12 hane, dortlu gruplar."""
    u = ozet[:12].upper()
    return " ".join(u[i:i + 4] for i in range(0, 12, 4))
