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

  fetch(SITE + '/blog-feed.json', { mode: 'cors', credentials: 'omit' })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (d) {
      if (!d || !d.yazilar || !d.yazilar.length) { return; }
      var h = '';
      d.yazilar.slice(0, 4).forEach(function (y) {
        var etiket = ETIKET[y.category] || 'Blog';
        h += '<a class="uc-yazi" href="' + ref('/blog/' + y.slug) + '" target="_blank" rel="noopener">' +
          '<img src="' + SITE + y.coverUrl + '" alt="" loading="lazy" decoding="async" width="600" height="400">' +
          '<span class="uc-yazi-etiket">' + metin(etiket) + '</span>' +
          '<span class="uc-yazi-baslik">' + metin(y.title) + '</span></a>';
      });
      liste.innerHTML = h;
      kutu.hidden = false;
    })
    .catch(function () { /* akis yoksa sessiz */ });
})();
