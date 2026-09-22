/* js/arama.js — site ici arama (22.09.2026)
 *
 * Sayfadaki buyutec dugmesi calismiyordu: masaustunde dugme hic yoktu,
 * mobilde katman aciliyor ama formun `action`i ve girdilerin `name`i
 * olmadigi icin gonderince sayfa kendini yeniliyordu.
 *
 * Site statik oldugundan arama tarayicida yapilir: scripts/arama_uygula.py
 * ile uretilen /arama.json ILK ACILISTA indirilir (sayfa yuklenirken DEGIL,
 * boylece performans turunda kazanilan agirlik geri gelmez), sonra bellekte
 * kalir. Ucuncu taraf servis ve disari veri cikisi yok.
 *
 * Turkce: "ogrenci" yazan "öğrenci"yi, "sinav" yazan "sınav"i bulur
 * (NFD ayristirmasi + birlesik isaret temizligi + i/ı esitlemesi).
 */
(function () {
  'use strict';

  var DIZIN_ADRES = '/arama.json';
  var EN_COK = 12;
  var dizin = null, yukleniyor = null, secili = -1, sonSonuc = [];

  function sade(s) {
    return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '')
      .replace(/ı/g, 'i').replace(/I/g, 'i').toLowerCase();
  }

  /* Hafif Turkce govdeleyici. Sebep (olculdu): "ders notu" aramasi 0 sonuc
   * donuyordu — sayfanin basligi "Video Ders Notlari" ve "notu" metninde
   * "notlari" ile ORTUSMUYOR. Ek listesi sade() sonrasi ASCII'ye inmis
   * metin icin yazildi. Iki tur uygulanir ki "sorular"->"soru"->"sor" ile
   * "soru"->"sor" ayni govdede bulussun; govde 3 harften kisalmaz.
   * Hedef kusursuz dilbilim degil, aramanin BOS DONMEMESI. */
  var EKLER = ['lerinden', 'larindan', 'lerini', 'larini', 'lerin', 'larin',
    'leri', 'lari', 'ler', 'lar', 'nin', 'nun', 'den', 'dan', 'ten', 'tan',
    'de', 'da', 'te', 'ta', 'in', 'un', 'yi', 'yu', 'si', 'su', 'ye', 'ya',
    'e', 'a', 'i', 'u'];

  function kok(k) {
    for (var tur = 0; tur < 2; tur++) {
      for (var i = 0; i < EKLER.length; i++) {
        var e = EKLER[i];
        if (k.length - e.length >= 3 && k.slice(-e.length) === e) { k = k.slice(0, -e.length); break; }
      }
    }
    return k;
  }

  function govde(s) {
    return sade(s).split(/[^a-z0-9]+/).filter(Boolean).map(kok).join(' ');
  }

  function kacir(s) {
    return (s || '').replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function dizinYukle() {
    if (dizin) return Promise.resolve(dizin);
    if (yukleniyor) return yukleniyor;
    yukleniyor = fetch(DIZIN_ADRES, { credentials: 'omit' })
      .then(function (y) { if (!y.ok) throw new Error(y.status); return y.json(); })
      .then(function (v) {
        dizin = (v.s || []).map(function (k) {
          k._b = sade(k.b);
          k._bs = govde(k.b);
          // Dis adresler aranabilir metne GIRMEZ: OSYM dosya adlari tarih
          // tasiyor (…12112019.pdf) ve "2019" aramasi yanlis yili getiriyordu.
          k._hs = govde([k.b, k.k || '', k.d || '', /^https?:/i.test(k.a) ? '' : k.a].join(' '));
          // Adresin son parcasi: "kpss" aramasinda /ss/kpss/ sayfasi
          // /ss/kpss-onlisans/'in altinda kaliyordu; slug esitligi one alir.
          var par = (k.a || '').replace(/[?#].*$/, '').replace(/\.[a-z0-9]+$/i, '').split('/').filter(Boolean);
          k._s = /^https?:/i.test(k.a) ? '' : govde(par.length ? par[par.length - 1] : '');
          return k;
        });
        return dizin;
      })
      .catch(function () { dizin = []; return dizin; });
    return yukleniyor;
  }

  function ara(sorgu) {
    var ham = sade(sorgu);
    var koklar = govde(sorgu).split(' ').filter(Boolean);
    if (!koklar.length) {
      return (dizin || []).filter(function (k) { return (k.w || 0) >= 4; }).slice(0, 8);
    }
    var slug = koklar.join('-'), cikti = [];
    for (var i = 0; i < dizin.length; i++) {
      var k = dizin[i], puan = 0, hepsi = true;
      for (var j = 0; j < koklar.length; j++) {
        var t = koklar[j], e = t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        // kelime BASI esleseme: kullanici yazarken "para" -> "parabol"
        if (k._bs.indexOf(t) === 0) puan += 12;
        else if (new RegExp('\\s' + e).test(k._bs)) puan += 8;
        else if (new RegExp('(^|\\s)' + e).test(k._hs)) puan += 3;
        else { hepsi = false; break; }
      }
      if (!hepsi) continue;
      if (k._b.indexOf(ham) !== -1) puan += 6;
      if (k._s && (k._s === slug || k._s === koklar.join(''))) puan += 10;
      puan += (k.w || 0);
      cikti.push({ k: k, p: puan });
    }
    cikti.sort(function (a, b) { return b.p - a.p || a.k.b.length - b.k.b.length; });
    return cikti.map(function (x) { return x.k; });
  }

  function disMi(a) { return /^https?:\/\//i.test(a); }

  function ciz(kap, sonuc, sorgu) {
    sonSonuc = sonuc.slice(0, EN_COK);
    secili = -1;
    if (!sorgu && sonSonuc.length) {
      kap.innerHTML = '<p class="arama-bilgi">Öne çıkanlar</p>' + liste(sonSonuc);
    } else if (!sonuc.length) {
      kap.innerHTML = '<p class="arama-bilgi">“' + kacir(sorgu) + '” için sonuç bulunamadı.</p>';
    } else {
      var kalan = sonuc.length - sonSonuc.length;
      kap.innerHTML = liste(sonSonuc)
        + (kalan > 0 ? '<p class="arama-bilgi">' + kalan + ' sonuç daha var, aramayı daraltın.</p>' : '');
    }
    kap.setAttribute('aria-busy', 'false');
  }

  function liste(k) {
    return '<ul class="arama-sonuc" role="listbox">' + k.map(function (x, i) {
      var dis = disMi(x.a);
      var alt = x.d ? kacir(x.d) : (dis ? x.a.replace(/^https?:\/\//, '').split('/')[0] : x.a);
      return '<li role="option" aria-selected="false"><a href="' + kacir(x.a) + '"'
        + (dis ? ' target="_blank" rel="noopener noreferrer"' : '') + ' data-sira="' + i + '">'
        + '<span class="arama-baslik">' + kacir(x.b) + (dis ? ' <span class="arama-dis">↗</span>' : '') + '</span>'
        + '<span class="arama-tur">' + kacir(x.t) + '</span>'
        + '<span class="arama-alt">' + alt + '</span></a></li>';
    }).join('') + '</ul>';
  }

  function seciliYap(kap, n) {
    var ogeler = kap.querySelectorAll('.arama-sonuc li');
    if (!ogeler.length) return;
    if (secili >= 0 && ogeler[secili]) ogeler[secili].setAttribute('aria-selected', 'false');
    secili = (n + ogeler.length) % ogeler.length;
    ogeler[secili].setAttribute('aria-selected', 'true');
    ogeler[secili].scrollIntoView({ block: 'nearest' });
  }

  function kur(girdiId, formId, ortukId) {
    var girdi = document.getElementById(girdiId);
    var form = document.getElementById(formId);
    var ortuk = document.getElementById(ortukId);
    if (!girdi || !form || !ortuk) return null;

    var kap = document.createElement('div');
    kap.className = 'arama-kutu';
    kap.setAttribute('aria-live', 'polite');
    form.parentNode.insertBefore(kap, form.nextSibling);

    var zaman = null;
    function calistir() {
      var s = girdi.value.trim();
      dizinYukle().then(function () { ciz(kap, ara(s), s); });
    }
    girdi.addEventListener('input', function () {
      clearTimeout(zaman);
      zaman = setTimeout(calistir, 120);
    });
    girdi.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown') { e.preventDefault(); seciliYap(kap, secili + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); seciliYap(kap, secili - 1); }
      else if (e.key === 'Escape') { kapat(); }
      else if (e.key === 'Enter') {
        e.preventDefault();
        var ogeler = kap.querySelectorAll('.arama-sonuc li a');
        var hedef = ogeler[secili >= 0 ? secili : 0];
        if (hedef) hedef.click();
      }
    });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ilk = kap.querySelector('.arama-sonuc li a');
      if (ilk) ilk.click();
    });
    return { girdi: girdi, kap: kap, calistir: calistir };
  }

  var kurulumlar = [];

  function ac(e) {
    if (e) e.preventDefault();
    var hepsi = document.querySelectorAll('.mk-fullscreen-search-overlay');
    for (var i = 0; i < hepsi.length; i++) hepsi[i].classList.add('mk-fullscreen-search-overlay-show');
    document.documentElement.classList.add('arama-acik');
    dizinYukle();
    // gorunur olan girdiye odaklan
    setTimeout(function () {
      for (var j = 0; j < kurulumlar.length; j++) {
        var k = kurulumlar[j];
        if (k.girdi.offsetParent !== null) { k.girdi.focus(); k.calistir(); return; }
      }
    }, 60);
  }

  function kapat() {
    var hepsi = document.querySelectorAll('.mk-fullscreen-search-overlay');
    for (var i = 0; i < hepsi.length; i++) hepsi[i].classList.remove('mk-fullscreen-search-overlay-show');
    document.documentElement.classList.remove('arama-acik');
  }

  function baslat() {
    kurulumlar = [
      kur('mk-fullscreen-search-input', 'mk-fullscreen-searchform', 'mk-search-overlay'),
      kur('mk-fullscreen-search-input2', 'mk-fullscreen-searchform2', 'mk-search-overlay2')
    ].filter(Boolean);
    if (!kurulumlar.length) return;

    var tetikler = document.querySelectorAll('#search-button, #search-button2, #search-button-listener2, .arama-tetik');
    for (var i = 0; i < tetikler.length; i++) tetikler[i].addEventListener('click', ac);
    var kapatmalar = document.querySelectorAll('a.mk-fullscreen-close');
    for (var j = 0; j < kapatmalar.length; j++) {
      kapatmalar[j].addEventListener('click', function (e) { e.preventDefault(); kapat(); });
    }
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') kapat();
      // "/" kisayolu: yazi alaninda degilken aramayi acar
      if (e.key === '/' && !/^(INPUT|TEXTAREA|SELECT)$/.test((e.target.tagName || ''))) {
        e.preventDefault(); ac();
      }
    });
    // katmanin bos alanina tiklayinca kapansin
    for (var m = 0; m < kurulumlar.length; m++) {
      (function (ortuk) {
        ortuk.addEventListener('click', function (e) { if (e.target === ortuk) kapat(); });
      })(kurulumlar[m].kap.closest('.mk-fullscreen-search-overlay'));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', baslat);
  } else {
    baslat();
  }
})();
