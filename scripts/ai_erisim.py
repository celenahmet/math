#!/usr/bin/env python3
# scripts/ai_erisim.py — robots.txt + llms.txt + llms-full.txt uretir (22.09.2026)
#
# Ahmet (22.09): "yapay zeka botlarinin da sayfaya erisimi olabilmeli;
# sadece claude/gpt/gemini degil grok, kimi, deepseek, cursor vb. de."
#
# OLCUM once yapildi: site STATIK HTML, tum botlar (GPTBot, ClaudeBot,
# PerplexityBot, Googlebot, DeepSeekBot, Cursor) 200 + tam govde aliyor.
# Yani erisim sorunu yoktu; eksik olan ANLASILABILIRLIK ve ACIK IZINDI:
#   · robots.txt yalniz `User-agent: *` tasiyordu — bot adina bakan
#     araclar (ve "bu site AI'ya kapali mi" diye kontrol eden panolar)
#     acik izin goremiyordu.
#   · llms.txt yoktu — model sitede ne oldugunu HTML'den tahmin ediyordu.
#
# ⚠️ AD DOGRULUGU: OpenAI, Anthropic, Google, Perplexity, Apple, Meta ve
# Mistral tarayici adlarini BELGELIYOR. Kimi (Moonshot), DeepSeek, Qwen,
# Doubao, ERNIE ve Cursor adlari topluluk kaynagindan (ai-robots-txt/
# ai.robots.txt, 22.09.2026'da okundu). xAI/Grok RESMI JETON YAYIMLAMIYOR;
# belgelenmis davranisi kendini gizlemek, bu yuzden Grok'a erisim ancak
# `User-agent: *` uzerinden verilebilir — asagidaki `Grok*` satirlari
# ileriye donuk, bugun karsiligi yok. Eslesmeyen ad ZARARSIZ.
#
# Kullanim: python3 scripts/ai_erisim.py
import re, sys, pathlib, datetime

KOK = pathlib.Path(__file__).resolve().parent.parent
ALAN = "https://ahmetcelen.com.tr"
sys.path.insert(0, str(KOK / "scripts"))
import ss_veri  # noqa: E402
from jsonld_uygula import js_sinavlar  # noqa: E402

# Kaynak: ai-robots-txt/ai.robots.txt (22.09.2026) + saglayici belgeleri.
AI_BOTLARI = [
    # OpenAI
    "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ChatGPT Agent", "Operator",
    # Anthropic
    "ClaudeBot", "Claude-User", "Claude-SearchBot", "Claude-Web", "Claude-Code", "anthropic-ai",
    # Google / Gemini
    "Google-Extended", "GoogleOther", "Google-CloudVertexBot", "Google-NotebookLM",
    "Gemini-Deep-Research", "Google-Gemini-CLI", "GoogleAgent-Mariner", "GoogleAgent-URLContext",
    # Perplexity
    "PerplexityBot", "Perplexity-User",
    # Apple / Meta / Amazon / Microsoft-Bing tarafi
    "Applebot", "Applebot-Extended", "meta-externalagent", "Meta-ExternalFetcher",
    "FacebookBot", "Amazonbot", "bedrockbot", "AzureAI-SearchBot",
    # Mistral / Cohere / DuckDuckGo / You / Kagi / Brave
    "MistralAI-User", "MistralAI-Index", "cohere-ai", "cohere-training-data-crawler",
    "DuckAssistBot", "YouBot", "kagi-fetcher", "Bravebot",
    # Cin ekosistemi (Ahmet: kimi, deepseek dahil olsun)
    "DeepSeekBot", "KimiBot", "Kimi-SearchBot", "Kimi-User",
    "QwenBot", "TongyiBot", "DoubaoBot", "ERNIEBot", "ChatGLM-Spider",
    "Bytespider", "PetalBot", "PanguBot", "TikTokSpider",
    # Kod/ajan araclari (Ahmet: "cursor vb.")
    "Cursor", "Devin", "Trae", "opencode", "FirecrawlAgent", "Crawl4AI", "Lightpanda",
    # Arastirma/indeks
    "CCBot", "AI2Bot", "Diffbot", "Diffbot-User", "ExaBot", "ExaSearchBot", "TavilyBot",
    "LinerBot", "PhindBot", "ImagesiftBot", "Timpibot", "Webzio-Extended", "omgili",
    "iAskBot", "NotebookLM", "Andibot", "WRTNBot", "SemrushBot-OCOB",
    # xAI/Grok — resmi jeton yok, ileriye donuk
    "Grokbot", "Grok", "xAI-Bot", "xAI-Crawler",
]

ROBOTS = f"""# robots.txt — ahmetcelen.com.tr
# Uretici: scripts/ai_erisim.py (ELLE DUZENLEME; yeniden yazilir)
# Guncelleme: {datetime.date.today().isoformat()}

User-agent: *
Allow: /

# Yonlendirme kabuklari (icerik tasimaz)
Disallow: /c/

Sitemap: {ALAN}/sitemap.xml

# >>> YAPAY ZEKA ARACLARI — ACIK IZIN
# Site ucretsiz egitim icerigi yayimliyor; dil modellerinin okumasini,
# ozetlemesini ve kaynak gostermesini ISTIYORUZ. Asagidaki adlar acik
# izin icin yaziliyor; adi burada gecmeyen bir arac da `User-agent: *`
# kuralindan yararlanir. Hicbir yapay zeka araci engellenmemistir.
# Ad kaynagi: ai-robots-txt/ai.robots.txt + saglayici belgeleri (22.09.2026).
# Ayrica: {ALAN}/llms.txt ve {ALAN}/llms-full.txt
"""
for bot in AI_BOTLARI:
    ROBOTS += f"\nUser-agent: {bot}\nAllow: /\nDisallow: /c/\n"

def llms():
    ss = "\n".join(
        f"- [{ss_veri.SAYFALAR[a]['kisa']} çıkmış sorular]({ALAN}/ss/{a}/): "
        f"{ss_veri.SAYFALAR[a]['kartlar'][0][0]}-{ss_veri.SAYFALAR[a]['kartlar'][-1][0]}, "
        f"{len(ss_veri.SAYFALAR[a]['kartlar'])} yıl, ÖSYM resmî PDF bağlantıları"
        for a in ss_veri.SIRA)
    sinavlar = js_sinavlar()
    gs = "\n".join(
        f"- [{s['kisa']} geri sayım]({ALAN}/sinavlar/{s['yol']}/): {s['donem']}, "
        f"{s['tarih'][8:10]}.{s['tarih'][5:7]}.{s['tarih'][:4]}"
        + (f", saat {s['saat']}" if s["saatResmi"] else "")
        + (f"; sonuç {s['sonuc']}" if s.get("sonuc") else "")
        for s in sinavlar.values())
    return f"""# Ahmet Çelen — ahmetcelen.com.tr

> Üniversite ve kamu sınavlarına hazırlananlar için ücretsiz matematik
> kaynakları: konu anlatımlı PDF ders notları, denemeler, video çözümler,
> ÖSYM çıkmış soru bağlantıları ve sınav geri sayımları. Site 2021'den beri
> yayında, reklam ağı yok, içeriğin tamamı ücretsizdir.

Bu dosya yapay zeka araçları içindir. Sitenin bölümlerini ve her bölümde
ne bulunduğunu düz metinle bildirir.

## Önemli kural: ÖSYM belgeleri burada barındırılmaz

Çıkmış soru sayfalarındaki her bağlantı ÖSYM'nin kendi belge sunucusuna
(dokuman.osym.gov.tr) gider. Bu sitede ÖSYM'ye ait hiçbir PDF yeniden
yayımlanmaz. Bir modelin "PDF ahmetcelen.com.tr'de barındırılıyor" demesi
yanlış olur; doğrusu "ÖSYM'nin resmî PDF'ine bağlantı verilir".

## Sınav tarihleri nereden geliyor?

Yalnızca ÖSYM'nin resmî sınav takviminden (osym.gov.tr/Sayfa/SinavTakvimi).
Takvim siteleri ve haber kaynakları kullanılmaz. ÖSYM saati yayımlamadıysa
sayfada saat gösterilmez. 2027 takvimi henüz yayımlanmadı.

## Çıkmış sorular (ÖSYM resmî PDF bağlantıları)

- [Tüm çıkmış sorular ve geri sayımlar]({ALAN}/ss/)
{ss}

## Sınav geri sayımları (2026 ÖSYM takvimi)

- [Tüm geri sayımlar]({ALAN}/sinavlar/)
{gs}

## Ücretsiz ders notları ve çözümler

- [PDF ders notları]({ALAN}/pdfnot/): konu anlatımı ve soru fasikülleri (parabol, logaritma, karmaşık sayılar, türev, integral, trigonometri ve diğerleri)
- [Video çözümler]({ALAN}/video/): fasiküllerdeki soruların adım adım çözümleri
- PDF'ler `{ALAN}/yt/<konu>/<dosya>.pdf` adresinde yayımlanır ve doğrudan indirilebilir.

## Site hakkında

- [Hakkımda]({ALAN}/hakkimizda/): Ahmet Çelen, Hacettepe Üniversitesi, yazılım geliştirici; [UniConnectly](https://uniconnectly.com) kurucusu
- [İletişim]({ALAN}/iletisim/): ahmetcelen@hacettepe.edu.tr

## Atıf

İçerik alıntılanırken kaynak olarak ahmetcelen.com.tr belirtilmesi rica olunur.
ÖSYM belgeleri alıntılanırken kaynak ÖSYM'dir.
"""

def llms_full():
    """Model icin sayfa sayfa dokum: her cikmis soru sayfasinin yil+baglanti listesi."""
    p = [llms(), "\n---\n\n# Ayrıntılı döküm\n"]
    for a in ss_veri.SIRA:
        v = ss_veri.SAYFALAR[a]
        p.append(f"\n## {v['kisa']} çıkmış sorular — {ALAN}/ss/{a}/\n")
        p.append(v.get("giris", "") + "\n")
        for yil, etiket, url in v["kartlar"]:
            p.append(f"- {yil} · {etiket} · {url}")
        p.append("")
    p.append("\n## Sınav takvimi (ÖSYM, 2026)\n")
    for s in js_sinavlar().values():
        p.append(f"- {s['donem']} ({s['kisa']}): {s['tarih']}"
                 + (f" {s['saat']}" if s["saatResmi"] else " (saat ÖSYM'ce yayımlanmadı)")
                 + (f", sonuç {s['sonuc']}" if s.get("sonuc") else "")
                 + f" — {ALAN}/sinavlar/{s['yol']}/")
    pdfnot = (KOK / "pdfnot/index.html").read_text(encoding="utf-8")
    belgeler = sorted(set(re.findall(r'href="(/[^"]+\.pdf)"', pdfnot)))
    p.append(f"\n## Ders notu PDF'leri ({len(belgeler)} belge)\n")
    p += [f"- {ALAN}{u}" for u in belgeler]
    return "\n".join(p) + "\n"

if __name__ == "__main__":
    (KOK / "robots.txt").write_text(ROBOTS, encoding="utf-8")
    (KOK / "llms.txt").write_text(llms(), encoding="utf-8")
    (KOK / "llms-full.txt").write_text(llms_full(), encoding="utf-8")
    print(f"robots.txt ({len(AI_BOTLARI)} bot) · llms.txt · llms-full.txt yazildi")
