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
  if (!kutu || !liste || !blok || !window.fetch) { return; }
  var kampanya = blok.getAttribute('data-kampanya') || 'ahmetcelen';
  var SITE = 'https://uniconnectly.com';
  var ETIKET = { rehber: 'Rehber', firsat: 'Fırsat', kampus: 'Kampüs', kariyer: 'Kariyer', teknoloji: 'Teknoloji', burs: 'Burs' };

  function ref(yol) {
    return SITE + yol + '?ref=ahmetcelen.com.tr&utm_source=ahmetcelen.com.tr&utm_medium=referral&utm_campaign=' + kampanya;
  }
  function metin(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }

  function kart(y, etiket) {
    return '<a class="uc-yazi" href="' + ref('/blog/' + y.slug) + '" target="_blank" rel="noopener">' +
      '<img src="' + SITE + y.coverUrl + '" alt="" loading="lazy" decoding="async" width="600" height="400">' +
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
    var SIRA = ['rehber', 'kariyer', 'akademi', 'etkinlik', 'topluluk', 'girisimcilik', 'markalar', 'duyuru'];
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
