#!/usr/bin/env python3
# scripts/blog_ikon.py — blogun satir ici SVG ikon takimi (23.09.2026)
#
# Ahmet: "kategorileri de iyi ayirmaliyiz, bunlara da ikonlu yapalim."
#
# NEDEN SATIR ICI SVG: ikon YAZI TIPI kullanmiyoruz. font-awesome-az.css
# yalniz sitede gecen simgeleri tasiyor; yeni bir kod noktasi eklemek
# altkumeyi yeniden uretmeyi gerektirir ve unutulursa ekranda kutu (□)
# cikar (22.09'da menu oklarinda yasandi). Satir ici SVG'de ek istek de
# yok, yazi tipi bagimliligi da.
#
# Bicim: 24x24 tuval, yalnizca cizgi (stroke), renk `currentColor`.
# Boylece ikon bulundugu kutunun rengini aliyor; ayri renk tanimi gerekmez.
# EV KURALI: yildiz/parilti ikonu YOK, dekoratif gradyan YOK.

_BAS = ('<svg class="bs-ikon" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" '
        'aria-hidden="true" focusable="false">')

_YOL = {
    # ── kategoriler ──────────────────────────────────────────────────────
    # Fonksiyonlar: giris → kutu → cikis (fonksiyon makinesi).
    # Ilk tasarim iki kume arasi esleme oklariydi; 16 px'te okunmuyordu
    # (olculdu, 23.09). Makine metaforu kucuk boyutta da aninda anlasiliyor.
    "fonksiyonlar": '<rect x="8.5" y="8.5" width="7" height="7" rx="1.6"/>'
                    '<path d="M2.5 12h6"/><path d="M15.5 12h6"/>'
                    '<path d="M19.2 9.7 21.5 12l-2.3 2.3"/>',
    # Polinomlar: ustuste terimler
    "polinomlar": '<path d="M4 7h16"/><path d="M4 12h11"/><path d="M4 17h7"/>'
                  '<path d="M18.5 15v4"/><path d="M16.5 17h4"/>',
    # Denklem ve parabol: parabol egrisi + eksen
    "denklemler": '<path d="M4 19V5"/><path d="M4 19h16"/>'
                  '<path d="M6 17c2.2-8 9.8-8 12 0"/>',
    # Trigonometri: birim cember ve yaricap
    "trigonometri": '<circle cx="12" cy="12" r="7.5"/><path d="M12 12h7.5"/>'
                    '<path d="M12 12 17.3 6.7"/><path d="M15.6 12a3.6 3.6 0 0 0-1.05-2.55"/>',
    # Logaritma ve diziler: giderek buyuyen adimlar
    "logaritma": '<path d="M4 19h16"/><path d="M6 19v-3"/><path d="M10.7 19v-6"/>'
                 '<path d="M15.3 19v-9"/><path d="M20 19V7"/>',
    # Analiz: egri uzerinde teget
    "analiz": '<path d="M4 19V5"/><path d="M4 19h16"/>'
              '<path d="M5.5 16.5c4-1 6.5-6.5 13-11"/><path d="M8 18.5 16 9.5"/>'
              '<circle cx="12" cy="14" r="1.3"/>',

    # ── kutular ──────────────────────────────────────────────────────────
    # Once sunlari bil: acik kitap
    "onkosul": '<path d="M12 6.5C10.4 5.3 8.4 4.7 6 4.7H4v13h2c2.4 0 4.4.6 6 1.8"/>'
               '<path d="M12 6.5c1.6-1.2 3.6-1.8 6-1.8h2v13h-2c-2.4 0-4.4.6-6 1.8"/>'
               '<path d="M12 6.5v13"/>',
    # Hap bilgi: kapsul (adi zaten "hap")
    "hap": '<rect x="2.8" y="9" width="18.4" height="6" rx="3"/><path d="M12 9v6"/>',
    # Dikkat: unlemli ucgen
    "dikkat": '<path d="M12 4.2 21 19.3H3z"/><path d="M12 10v4"/><path d="M12 16.6h.01"/>',
    # Ornek: kalem
    "ornek": '<path d="M16.5 3.9 20.1 7.5 8.6 19H5v-3.6z"/><path d="M14.2 6.2l3.6 3.6"/>',
    # Sinavda nasil cikar: isaretli kagit
    "sinavda": '<path d="M7 3.6h10a1.4 1.4 0 0 1 1.4 1.4v14a1.4 1.4 0 0 1-1.4 1.4H7A1.4 1.4 0 0 1 5.6 19V5A1.4 1.4 0 0 1 7 3.6z"/>'
               '<path d="M9 8.4h6"/><path d="M9 12h6"/><path d="M9 15.6h3.5"/>',
    # Kontrol listesi basligi
    "kontrol": '<path d="M4 6.5 6 8.5 9.5 5"/><path d="M4 12.5 6 14.5 9.5 11"/>'
               '<path d="M4 18.5 6 20.5 9.5 17"/><path d="M13 7h7"/><path d="M13 13h7"/><path d="M13 19h7"/>',
    "sss": '<circle cx="12" cy="12" r="8.2"/><path d="M9.7 9.6a2.4 2.4 0 1 1 3.1 2.3c-.6.2-.8.7-.8 1.3v.4"/>'
           '<path d="M12 16.6h.01"/>',
    "kaynak": '<path d="M10.5 13.5a4 4 0 0 0 5.7 0l2.6-2.6a4 4 0 0 0-5.7-5.7l-1.1 1.1"/>'
              '<path d="M13.5 10.5a4 4 0 0 0-5.7 0l-2.6 2.6a4 4 0 0 0 5.7 5.7l1.1-1.1"/>',
    # paylasim
    "paylas": '<circle cx="18" cy="5.5" r="2.6"/><circle cx="6" cy="12" r="2.6"/>'
              '<circle cx="18" cy="18.5" r="2.6"/><path d="M8.3 10.8 15.7 6.7"/>'
              '<path d="M8.3 13.2 15.7 17.3"/>',
    "baglanti": '<path d="M10.5 13.5a4 4 0 0 0 5.7 0l2.6-2.6a4 4 0 0 0-5.7-5.7l-1.1 1.1"/>'
                '<path d="M13.5 10.5a4 4 0 0 0-5.7 0l-2.6 2.6a4 4 0 0 0 5.7 5.7l1.1-1.1"/>',
    "whatsapp": '<path d="M20 11.7a8 8 0 0 1-11.9 7L4 20l1.4-4a8 8 0 1 1 14.6-4.3z"/>'
                '<path d="M9 9.2c.3 1.6 2.2 3.5 3.8 3.8l.9-1.2 1.8.8v1.3c-2.6.5-5.9-2.8-5.4-5.4h1.3l.8 1.8z"/>',
    # kunye ve yol
    "saat": '<circle cx="12" cy="12" r="8.2"/><path d="M12 7.6V12l3 1.8"/>',
    "goz": '<path d="M2.6 12S6 5.8 12 5.8 21.4 12 21.4 12 18 18.2 12 18.2 2.6 12 2.6 12z"/>'
           '<circle cx="12" cy="12" r="2.9"/>',
    "ev": '<path d="M4 10.2 12 4l8 6.2V19a1.2 1.2 0 0 1-1.2 1.2H5.2A1.2 1.2 0 0 1 4 19z"/>'
          '<path d="M9.6 20.2v-6h4.8v6"/>',
    "ok-sag": '<path d="M9.5 6.5 15 12l-5.5 5.5"/>',
    "ok-sol": '<path d="M14.5 6.5 9 12l5.5 5.5"/>',
    "ok-yukari": '<path d="M12 19V5.5"/><path d="M6.5 11 12 5.5 17.5 11"/>',
    "liste": '<path d="M4.5 7h2"/><path d="M9.5 7h10"/><path d="M4.5 12h2"/>'
             '<path d="M9.5 12h10"/><path d="M4.5 17h2"/><path d="M9.5 17h10"/>',
    "x": '<path d="M4 4l16 16"/><path d="M20 4L4 20"/>',
    "instagram": '<rect x="3.6" y="3.6" width="16.8" height="16.8" rx="4.6"/>'
                 '<circle cx="12" cy="12" r="3.9"/><circle cx="17" cy="7" r="1"/>',
    "ilgili": '<rect x="3.6" y="4.6" width="7" height="7" rx="1.4"/>'
              '<rect x="13.4" y="4.6" width="7" height="7" rx="1.4"/>'
              '<rect x="3.6" y="14.4" width="7" height="5" rx="1.4"/>'
              '<rect x="13.4" y="14.4" width="7" height="5" rx="1.4"/>',
}


def ikon(ad):
    """Adi bilinmeyen ikon SESSIZCE bos donmez; hata firlatir ki sayfada
    gorunmez bir bosluk kalmasin."""
    if ad not in _YOL:
        raise KeyError(f"blog_ikon: tanimsiz ikon '{ad}' · var olanlar: {', '.join(sorted(_YOL))}")
    return _BAS + _YOL[ad] + "</svg>"


def varsa(ad):
    return _YOL.get(ad) and ikon(ad) or ""
