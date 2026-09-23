/* js/blog.js — blog bolumunun kucuk arayuz betigi (23.09.2026)
 *
 * Blog sayfalari ana temanin jQuery yiginini YUKLEMEZ; burasi sade JS.
 * Uc is yapar: okuma ilerleme cubugu, icindekilerde etkin baslik,
 * hub'da kategori suzgeci. Arama ayri dosyada (js/arama.js) ve ana site
 * ile ORTAK; blog yalnizca ona modern bir deri giydiriyor (css/blog.css).
 */
(function () {
  'use strict';

  // 1) okuma ilerlemesi
  var cubuk = document.getElementById('ilerleme');
  if (cubuk) {
    var yaz = function () {
      var h = document.documentElement;
      var boy = h.scrollHeight - h.clientHeight;
      cubuk.style.width = boy > 0 ? (h.scrollTop / boy * 100).toFixed(1) + '%' : '0';
    };
    addEventListener('scroll', yaz, { passive: true });
    addEventListener('resize', yaz);
    yaz();
  }

  // 2) icindekiler: gorunen bolumu isaretle
  var toc = document.querySelector('.bs-toc');
  if (toc && 'IntersectionObserver' in window) {
    var baglar = {};
    [].forEach.call(toc.querySelectorAll('a[href^="#"]'), function (a) {
      baglar[a.getAttribute('href').slice(1)] = a;
    });
    var basliklar = [].filter.call(document.querySelectorAll('.bs-icerik h2[id]'),
      function (h) { return baglar[h.id]; });
    var gorunen = [];
    var g = new IntersectionObserver(function (girisler) {
      girisler.forEach(function (x) {
        var i = gorunen.indexOf(x.target.id);
        if (x.isIntersecting && i === -1) gorunen.push(x.target.id);
        if (!x.isIntersecting && i !== -1) gorunen.splice(i, 1);
      });
      var hedef = gorunen.length ? gorunen[0] : null;
      if (!hedef) {   // hicbiri gorunmuyorsa en son gecilen baslik
        for (var j = 0; j < basliklar.length; j++) {
          if (basliklar[j].getBoundingClientRect().top < 120) hedef = basliklar[j].id;
        }
      }
      for (var k in baglar) baglar[k].classList.toggle('etkin', k === hedef);
    }, { rootMargin: '-80px 0px -70% 0px', threshold: 0 });
    basliklar.forEach(function (h) { g.observe(h); });
  }

  // 3) hub: kategori suzgeci (adres degismez, sayfa yenilenmez)
  var suzgec = document.querySelector('.bs-suzgec');
  if (suzgec) {
    suzgec.addEventListener('click', function (e) {
      var d = e.target.closest('button');
      if (!d) return;
      var secilen = d.getAttribute('data-kat');
      [].forEach.call(suzgec.querySelectorAll('button'), function (b) {
        b.setAttribute('aria-pressed', String(b === d));
      });
      [].forEach.call(document.querySelectorAll('.bs-kart'), function (kart) {
        kart.hidden = !(secilen === '*' || kart.getAttribute('data-kat') === secilen);
      });
    });
  }
})();
