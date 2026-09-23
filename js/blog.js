/* js/blog.js — blog bolumunun kucuk arayuz betigi (23.09.2026)
 *
 * Blog sayfalari ana temanin jQuery yiginini YUKLEMEZ; burasi sade JS.
 * Bes is yapar: okuma ilerleme cubugu, icindekilerde etkin baslik,
 * hub'da kategori suzgeci, tiklanabilir kontrol listesi ve paylasim. Arama ayri dosyada (js/arama.js) ve ana site
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

  // 4) tiklanabilir kontrol listesi
  //
  // Ahmet (23.09): "kontrol listesi tiklanabilir checklist gibi olsun."
  // Isaretler YALNIZCA tarayicida saklanir; sunucuya hicbir sey gitmez,
  // hesap da istenmez. localStorage erisimi gizli sekmede ya da site
  // verileri kapaliyken HATA FIRLATABILIR, bu yuzden her erisim try ile
  // sarili; depolama yoksa liste calisir, yalniz hatirlamaz.
  var sar = document.querySelector('.bs-kontrol-sar');
  if (sar) {
    var anahtar = 'ac-kontrol:' + (sar.getAttribute('data-yazi') || '');
    var kutular = [].slice.call(sar.querySelectorAll('input[type=checkbox]'));
    var toplam = kutular.length;
    var durum = sar.querySelector('.bs-kontrol-durum strong');
    var cubuk = sar.querySelector('.bs-kontrol-cubuk span');
    var sifirla = sar.querySelector('.bs-kontrol-sifirla');

    function oku() {
      try { return JSON.parse(localStorage.getItem(anahtar) || '[]') || []; }
      catch (e) { return []; }
    }
    function yazDepo(d) {
      try { localStorage.setItem(anahtar, JSON.stringify(d)); } catch (e) { /* yoksay */ }
    }
    function tazele() {
      var n = 0;
      for (var i = 0; i < toplam; i++) { if (kutular[i].checked) n++; }
      if (durum) { durum.textContent = String(n); }
      if (cubuk) { cubuk.style.width = toplam ? (n / toplam * 100).toFixed(0) + '%' : '0%'; }
      if (sifirla) { sifirla.hidden = n === 0; }
      sar.classList.toggle('bs-bitti', toplam > 0 && n === toplam);
    }

    var kayitli = oku();
    for (var i = 0; i < toplam; i++) {
      if (kayitli.indexOf(i) !== -1) { kutular[i].checked = true; }
    }
    tazele();

    sar.addEventListener('change', function (e) {
      if (!e.target || e.target.type !== 'checkbox') { return; }
      var secili = [];
      for (var j = 0; j < toplam; j++) { if (kutular[j].checked) { secili.push(j); } }
      yazDepo(secili);
      tazele();
    });
    if (sifirla) {
      sifirla.addEventListener('click', function () {
        for (var j = 0; j < toplam; j++) { kutular[j].checked = false; }
        yazDepo([]);
        tazele();
      });
    }
  }


  // 5) paylasim
  //
  // Ahmet (23.09): "en altta paylas butonu da olsun sayfayi paylasabilsin."
  // Ucuncu taraf paylasim betigi YUKLENMEZ: her biri izleme cerezi tasiyor
  // ve sayfaya yuz kilobayt ekliyor. Once tarayicinin KENDI paylasim
  // penceresi denenir (navigator.share; mobilde WhatsApp, Instagram, mesaj,
  // hepsi orada cikar). Masaustunde cogu tarayicida yok; o zaman baglanti
  // panoya kopyalanir.
  var paylasKutu = document.querySelector('.bs-paylas');
  if (paylasKutu) {
    var baslik = paylasKutu.getAttribute('data-baslik') || document.title;
    var adres = location.origin + (paylasKutu.getAttribute('data-yol') || location.pathname);
    var kopyaDugme = paylasKutu.querySelector('.bs-paylas-kopya');
    var wa = paylasKutu.querySelector('.bs-paylas-whatsapp');
    if (wa) {
      wa.href = 'https://wa.me/?text=' + encodeURIComponent(baslik + ' ' + adres);
    }
    var xd = paylasKutu.querySelector('.bs-paylas-x');
    if (xd) {
      xd.href = 'https://x.com/intent/post?text=' + encodeURIComponent(baslik)
              + '&url=' + encodeURIComponent(adres);
    }

    function panoyaYaz() {
      var bitti = function () {
        if (!kopyaDugme) { return; }
        var eski = kopyaDugme.lastChild;
        kopyaDugme.classList.add('bs-kopyalandi');
        if (eski && eski.nodeType === 3) { eski.nodeValue = 'Kopyalandı'; }
        setTimeout(function () {
          kopyaDugme.classList.remove('bs-kopyalandi');
          if (eski && eski.nodeType === 3) { eski.nodeValue = 'Bağlantıyı kopyala'; }
        }, 1800);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(adres).then(bitti, function () {});
        return;
      }
      // Eski tarayici: gecici alan uzerinden kopyala
      try {
        var alan = document.createElement('textarea');
        alan.value = adres; alan.setAttribute('readonly', '');
        alan.style.position = 'fixed'; alan.style.left = '-9999px';
        document.body.appendChild(alan); alan.select();
        document.execCommand('copy'); document.body.removeChild(alan);
        bitti();
      } catch (e) { /* yoksay */ }
    }

    var anaDugme = paylasKutu.querySelector('.bs-paylas-ana');
    if (anaDugme) {
      anaDugme.addEventListener('click', function () {
        if (navigator.share) {
          navigator.share({ title: baslik, url: adres }).catch(function () {});
        } else {
          panoyaYaz();
        }
      });
    }
    if (kopyaDugme) { kopyaDugme.addEventListener('click', panoyaYaz); }

    // Instagram web uzerinden baglanti paylasimi KABUL ETMIYOR (X'teki gibi
    // bir intent adresi yok). Yapilabilecek tek durust sey baglantiyi
    // kopyalayip kullaniciyi yonlendirmek.
    var ig = paylasKutu.querySelector('.bs-paylas-instagram');
    if (ig) {
      ig.addEventListener('click', function () {
        panoyaYaz();
        var yazi = ig.lastChild;
        if (yazi && yazi.nodeType === 3) {
          ig.classList.add('bs-kopyalandi');
          yazi.nodeValue = 'Kopyalandı, hikâyene yapıştır';
          setTimeout(function () {
            ig.classList.remove('bs-kopyalandi');
            yazi.nodeValue = 'Instagram';
          }, 2600);
        }
      });
    }
  }

  // 3) hub: iki eksenli suzgec (Konu VE Sinav)
  //
  // Ahmet (23.09): "sagda kategoriler ve sinavlar diye ayri bloklar olsun."
  // Yan bloktaki baglantilar /blog/#<kategori> ve /blog/#sinav-<ad>
  // adreslerine gidiyor; hub acilinca adres parcasi okunup ilgili dugme
  // tiklaniyor, boylece baglanti gercekten bir ise yariyor.
  var satirlar = [].slice.call(document.querySelectorAll('.bs-suzgec'));
  if (satirlar.length) {
    var kartlar = [].slice.call(document.querySelectorAll('.bs-kart'));
    var secim = { kat: '*', sinav: '*' };

    function suz() {
      var gorunen = 0;
      kartlar.forEach(function (kart) {
        var katUyar = secim.kat === '*' || kart.getAttribute('data-kat') === secim.kat;
        var sinavlar = (kart.getAttribute('data-sinav') || '').split(/\s+/);
        var sinavUyar = secim.sinav === '*' || sinavlar.indexOf(secim.sinav) !== -1;
        var ac = katUyar && sinavUyar;
        kart.hidden = !ac;
        if (ac) { gorunen++; }
      });
      var bos = document.querySelector('.bs-suzgec-bos');
      if (bos) { bos.hidden = gorunen !== 0; }
    }

    satirlar.forEach(function (satir) {
      satir.addEventListener('click', function (e) {
        var d = e.target.closest('button');
        if (!d) { return; }
        var eksen = d.hasAttribute('data-sinav') ? 'sinav' : 'kat';
        secim[eksen] = d.getAttribute('data-' + (eksen === 'sinav' ? 'sinav' : 'kat'));
        [].forEach.call(satir.querySelectorAll('button'), function (b) {
          b.setAttribute('aria-pressed', String(b === d));
        });
        suz();
      });
    });

    var parcaSec = function () {
      var p = (location.hash || '').replace('#', '');
      if (!p) { return; }
      var d;
      if (p.indexOf('sinav-') === 0) {
        d = document.querySelector('[data-sinav="' + p.slice(6).replace(/"/g, '') + '"]');
      } else {
        d = document.querySelector('[data-kat="' + p.replace(/"/g, '') + '"]');
      }
      if (d) { d.click(); }   // "konular" / "sinavlar" gibi capa adlari eslesmez, yoksayilir
    };
    parcaSec();
    addEventListener('hashchange', parcaSec);
  }
})();
