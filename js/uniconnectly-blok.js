/* js/uniconnectly-blok.js — UniConnectly kutusundaki "En yeniler" bolumu.
 * https://uniconnectly.com/blog-feed.json (build'de uretilir, CORS acik)
 * okunur; son 4 yazi karta donusturulur. Akis gelmezse bolum gizli kalir.
 * Baglantilar sayfanin data-kampanya degeriyle UTM'lenir. jQuery gerekmez. */
(function () {
  'use strict';
  /* Kitle sekmeleri (Ogrenciler / Topluluklar / Sirketler / Akademisyenler) */
  var sekmeler = document.querySelectorAll('[data-uc-sekme]');
  Array.prototype.forEach.call(sekmeler, function (b) {
    b.addEventListener('click', function () {
      var ad = b.getAttribute('data-uc-sekme');
      Array.prototype.forEach.call(sekmeler, function (x) {
        var acik = x === b; x.classList.toggle('uc-sekme-acik', acik); x.setAttribute('aria-selected', acik ? 'true' : 'false');
      });
      Array.prototype.forEach.call(document.querySelectorAll('[data-uc-panel]'), function (p) {
        p.hidden = p.getAttribute('data-uc-panel') !== ad;
      });
    });
  });

  var kutu = document.getElementById('uc-en-yeniler-kutu');
  var liste = document.getElementById('uc-en-yeniler');
  var blok = document.querySelector('.uc-blok');
  /* Keep logos, store badges and all ad links attributable and in a new tab. */
  if (blok) {
    Array.prototype.forEach.call(blok.querySelectorAll('a[href]'), function (a) {
      var url;
      try { url = new URL(a.href, location.href); } catch (_) { return; }
      if (url.protocol !== 'https:' && url.protocol !== 'http:') { return; }
      var takip = {
        ref: 'ahmetcelen.com.tr',
        utm_source: 'ahmetcelen.com.tr',
        utm_medium: 'referral',
        utm_campaign: blok.getAttribute('data-kampanya') || 'ahmetcelen'
      };
      Object.keys(takip).forEach(function (key) {
        if (!url.searchParams.has(key)) { url.searchParams.set(key, takip[key]); }
      });
      if (url.hostname === 'play.google.com') {
        var installRef = new URLSearchParams(url.searchParams.get('referrer') || '');
        Object.keys(takip).forEach(function (key) {
          if (!installRef.has(key)) { installRef.set(key, takip[key]); }
        });
        url.searchParams.set('referrer', installRef.toString());
      }
      a.href = url.href;
      a.target = '_blank';
      a.rel = 'noopener';
    });
  }
  /* First visit to exam pages in this tab: a compact, dismissible ad. */
  function girisReklami() {
    if (!blok || !/^\/(ss|sinavlar)(\/|$)/.test(location.pathname)) { return; }
    var anahtar = 'uc-giris-reklami-kapatildi-v1';
    try { if (sessionStorage.getItem(anahtar)) { return; } } catch (_) {}
    var d = document.createElement('dialog');
    if (typeof d.showModal !== 'function') { return; }
    d.className = 'uc-giris';
    d.setAttribute('aria-labelledby', 'uc-giris-baslik');
    var kapat = document.createElement('button');
    kapat.type = 'button'; kapat.className = 'uc-giris-kapat';
    kapat.setAttribute('aria-label', 'Reklamı kapat');
    kapat.textContent = '×';
    d.appendChild(kapat);
    var logo = blok.querySelector('.uc-logo');
    if (logo) { d.appendChild(logo.cloneNode(true)); }
    var etiket = document.createElement('p');
    etiket.className = 'uc-etiket'; etiket.textContent = 'UniConnectly · Ücretsiz indir ve kaydol';
    d.appendChild(etiket);
    var baslik = document.createElement('h2');
    var basliklar = [
      'Üniversite hayatının fırsatları tek uygulamada',
      'Öğrenciler, şirketler, topluluklar bir arada',
      'CV’ni güncelle, PDF’ini hemen indir',
      'Kampüsü keşfet, kariyerine bir adım at',
      'Staj, iş, burs ve etkinlik fırsatlarını kaçırma'
    ];
    var baslikSira = Math.floor(Math.random() * basliklar.length);
    baslik.id = 'uc-giris-baslik'; baslik.textContent = basliklar[baslikSira];
    d.appendChild(baslik);
    var faydalar = document.createElement('ul');
    faydalar.className = 'uc-faydalar';
    var maddeler = blok.querySelectorAll('[data-uc-panel="ogrenci"] li');
    var ikonlar = [
      '<path d="M14 3H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h5M14 3v6h6M14 3l6 6M8 13h4M8 17h2M18 13v8m-3-3 3 3 3-3"/>',
      '<rect x="3" y="4" width="18" height="16" rx="3"/><circle cx="9" cy="10" r="2"/><path d="M5.5 17c.5-3 6.5-3 7 0M15 9h3M15 13h3M15 17h2"/>',
      '<path d="M18 8a6 6 0 0 0-12 0c0 7-3 7-3 9h18c0-2-3-2-3-9M10 21h4M12 2v1"/>',
      '<rect x="3" y="7" width="18" height="14" rx="3"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 12c5 3 13 3 18 0M10 13h4v3h-4z"/>'
    ];
    Array.prototype.slice.call(maddeler, 0, 4).forEach(function (li, i) {
      var kart = li.cloneNode(true);
      kart.classList.add('uc-giris-ikonlu', 'uc-giris-ikon-' + i);
      var simge = document.createElement('span');
      simge.className = 'uc-giris-simge';
      simge.setAttribute('aria-hidden', 'true');
      simge.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">' + ikonlar[i] + '</svg>';
      kart.insertBefore(simge, kart.firstChild);
      faydalar.appendChild(kart);
    });
    d.appendChild(faydalar);
    var magazalar = blok.querySelector('.uc-magazalar');
    if (magazalar) { d.appendChild(magazalar.cloneNode(true)); }
    var dugme = blok.querySelector('.uc-dugme-dolu');
    if (dugme) { d.appendChild(dugme.cloneNode(true)); }
    function hatirla() { try { sessionStorage.setItem(anahtar, '1'); } catch (_) {} }
    var baslikDonus = null;
    kapat.addEventListener('click', function () { d.close(); });
    d.addEventListener('click', function (e) {
      if (e.target !== d) { return; }
      var r = d.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) { d.close(); }
    });
    d.addEventListener('close', function () {
      clearInterval(baslikDonus);
      hatirla(); document.documentElement.classList.remove('uc-giris-acik'); d.remove();
    });
    document.body.appendChild(d);
    d.showModal(); document.documentElement.classList.add('uc-giris-acik');
    baslikDonus = setInterval(function () {
      if (document.hidden || !d.open) { return; }
      baslikSira = (baslikSira + 1) % basliklar.length;
      baslik.textContent = basliklar[baslikSira];
    }, 7000);
    kapat.focus({ preventScroll: true });
  }
  girisReklami();

  /* Gorseller cdn.uniconnectly.com/web'den (25.10.2026, Vercel istek kotasi).
     Yeni bir blog kapagi R2'ye henuz yuklenmemisse uniconnectly.com'daki asil
     adrese dusulur; 'error' kabarcik yapmadigi icin yakalama evresinde dinlenir. */
  var MEDYA = 'https://cdn.uniconnectly.com/web';
  document.addEventListener('error', function (e) {
    var g = e.target;
    if (!g || g.tagName !== 'IMG' || g.getAttribute('data-uc-yedek')) { return; }
    var src = g.getAttribute('src') || '';
    if (src.indexOf(MEDYA + '/') !== 0) { return; }
    g.setAttribute('data-uc-yedek', '1');
    g.src = 'https://uniconnectly.com' + src.slice(MEDYA.length);
  }, true);

  if (!kutu || !liste || !blok || !window.fetch) { return; }
  var kampanya = blok.getAttribute('data-kampanya') || 'ahmetcelen';
  var SITE = 'https://uniconnectly.com';
  var ETIKET = { rehber: 'Rehber', firsat: 'Fırsat', kampus: 'Kampüs', kariyer: 'Kariyer', teknoloji: 'Teknoloji', burs: 'Burs' };

  function ref(yol) {
    return SITE + yol + '?ref=ahmetcelen.com.tr&utm_source=ahmetcelen.com.tr&utm_medium=referral&utm_campaign=' + kampanya;
  }
  function metin(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

  function kart(y, etiket) {
    // Akistan gelen yol yalniz duz bir dosya yoluysa kullanilir (adrese baska sey sizmasin).
    var kapak = /^\/[A-Za-z0-9._\/-]+$/.test(y.coverUrl || '') ? MEDYA + y.coverUrl : '';
    return '<a class="uc-yazi" href="' + ref('/blog/' + y.slug) + '" target="_blank" rel="noopener">' +
      (kapak ? '<img src="' + kapak + '" alt="" loading="lazy" decoding="async" width="600" height="400">' : '') +
      '<span class="uc-yazi-etiket">' + metin(etiket) + '</span>' +
      '<span class="uc-yazi-baslik">' + metin(y.title) + '</span></a>';
  }

  /* Kategori rehberi: "Seckiler" = sayfaya gomulu 8 sabit yazi; kategori
     secilince akistaki o kategorinin son 8 yazisi + "Tumunu gor". */
  function kategoriRehberi(d) {
    var cubuk = document.getElementById('uc-kategoriler');
    var yazilar = document.getElementById('uc-yazilar');
    var baslik = document.getElementById('uc-yazi-baslik');
    var tumu = document.getElementById('uc-tumu');
    if (!cubuk || !yazilar || !d.kategoriler) { return; }
    var seckiler = yazilar.innerHTML;
    var SIRA = ['indirim', 'ucretsiz', 'rehber', 'kariyer', 'akademi', 'etkinlik', 'topluluk', 'girisimcilik', 'markalar', 'duyuru'];
    SIRA.forEach(function (k) {
      var kat = d.kategoriler[k];
      if (!kat || !kat.yazilar || !kat.yazilar.length) { return; }
      var b = document.createElement('button');
      b.type = 'button'; b.className = 'uc-kategori'; b.setAttribute('data-uc-kategori', k); b.setAttribute('aria-selected', 'false');
      b.textContent = kat.etiket + ' (' + kat.sayi + ')';
      cubuk.appendChild(b);
    });
    cubuk.addEventListener('click', function (e) {
      var b = e.target.closest('[data-uc-kategori]');
      if (!b) { return; }
      var k = b.getAttribute('data-uc-kategori');
      Array.prototype.forEach.call(cubuk.querySelectorAll('[data-uc-kategori]'), function (x) {
        var acik = x === b; x.classList.toggle('uc-kategori-acik', acik); x.setAttribute('aria-selected', acik ? 'true' : 'false');
      });
      if (k === 'seckiler') {
        yazilar.innerHTML = seckiler; if (baslik) { baslik.textContent = 'Öğrenciler için rehberler'; } if (tumu) { tumu.hidden = true; }
        return;
      }
      var kat = d.kategoriler[k]; var h = '';
      kat.yazilar.forEach(function (y) { h += kart(y, kat.etiket); });
      yazilar.innerHTML = h;
      if (baslik) { baslik.textContent = kat.etiket + ' yazıları'; }
      if (tumu) {
        var a = tumu.querySelector('a');
        if (a) { a.href = ref('/blog') + (kat.sanal ? '&ara=' + encodeURIComponent(kat.arama || k) : '&kategori=' + encodeURIComponent(k)); a.textContent = 'Tümünü gör (' + kat.sayi + ' yazı)'; }
        tumu.hidden = false;
      }
    });
  }

  fetch(SITE + '/blog-feed.json', { mode: 'cors', credentials: 'omit' })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) {
      if (!d || !d.yazilar || !d.yazilar.length) { return; }
      var h = '';
      d.yazilar.slice(0, 4).forEach(function (y) { h += kart(y, ETIKET[y.category] || 'Blog'); });
      liste.innerHTML = h;
      kutu.hidden = false;
      kategoriRehberi(d);
    })
    .catch(function () { /* akis yoksa sessiz */ });
})();
