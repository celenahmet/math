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

  // 2) icindekiler: etkin bolum + sag blokta AKILLI pencere
  //
  // Iki icindekiler var: yazinin basindaki tam liste ve sag bloktaki
  // okuma konumu. Ikisi de ayni etkin bolumu isaretliyor.
  //
  // Sag blokta ondort baslik birden basilsa sutun yine ekrandan uzun olur
  // ve yapiskan davranis bozulur (23.09'da yasandi). Bu yuzden liste tam
  // basiliyor ama yalnizca BULUNDUGUN bolumun cevresindeki bes tanesi
  // acik biraktiliyor; ustte kacinci bolumde oldugun ve ilerleme cubugu.
  var tocler = [].slice.call(document.querySelectorAll('.bs-toc'));
  var yanToc = document.querySelector('.bs-toc-yan');
  if (tocler.length && 'IntersectionObserver' in window) {
    var basliklar = [].slice.call(document.querySelectorAll('.bs-icerik h2[id]'));
    var sira = basliklar.map(function (h) { return h.id; });
    var gorunen = [];
    var PENCERE = 2;   // etkin bolumun iki ustu, iki alti
    var simdiki = 0;
    var hepsiAcik = false;
    // ⚠️ Konum ve ileri/geri, sagdaki icindekilerin KENDI baglantilarindan
    // hesaplanir; sayfadaki butun h2'lerden degil. "Bunlar da ilgini
    // cekebilir" gibi basliklar icindekilerde yok; h2 sirasini kullanmak
    // ilgili yazi ciktigi anda sayaci ve pencereyi bir kaydirirdi.
    var gezinti = yanToc ? [].map.call(yanToc.querySelectorAll('ol a[href^="#"]'),
      function (a) { return a.getAttribute('href').slice(1); }) : sira;

    function git(i) {
      if (i < 0 || i >= gezinti.length) { return; }
      var h = document.getElementById(gezinti[i]);
      if (h) { h.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    }

    function isaretle(hedef) {
      tocler.forEach(function (toc) {
        [].forEach.call(toc.querySelectorAll('a[href^="#"]'), function (a) {
          a.classList.toggle('etkin', a.getAttribute('href').slice(1) === hedef);
        });
      });
      if (!yanToc) { return; }
      var i = gezinti.indexOf(hedef);
      if (i === -1) { i = simdiki; }   // icindekilerde olmayan baslik: konum korunur
      simdiki = i;
      var ogeler = [].slice.call(yanToc.querySelectorAll('ol li'));
      ogeler.forEach(function (li, j) {
        li.hidden = !hepsiAcik && Math.abs(j - i) > PENCERE;
      });
      var onc = yanToc.querySelector('.bs-toc-onceki');
      var son = yanToc.querySelector('.bs-toc-sonraki');
      if (onc) { onc.disabled = i <= 0; }
      if (son) { son.disabled = i >= gezinti.length - 1; }
      var sayac = yanToc.querySelector('.bs-konum');
      if (sayac) { sayac.textContent = String(i + 1); }
      var cubuk = yanToc.querySelector('.bs-toc-cubuk span');
      if (cubuk && ogeler.length) {
        cubuk.style.width = ((i + 1) / ogeler.length * 100).toFixed(0) + '%';
      }
    }

    var g = new IntersectionObserver(function (girisler) {
      girisler.forEach(function (x) {
        var i = gorunen.indexOf(x.target.id);
        if (x.isIntersecting && i === -1) { gorunen.push(x.target.id); }
        if (!x.isIntersecting && i !== -1) { gorunen.splice(i, 1); }
      });
      var hedef = null;
      if (gorunen.length) {
        // Gorunenler arasindan sayfada EN USTTEKI bolum
        hedef = sira.filter(function (id) { return gorunen.indexOf(id) !== -1; })[0];
      } else {
        for (var j = 0; j < basliklar.length; j++) {
          if (basliklar[j].getBoundingClientRect().top < 120) { hedef = basliklar[j].id; }
        }
      }
      if (hedef) { isaretle(hedef); }
    }, { rootMargin: '-80px 0px -70% 0px', threshold: 0 });
    basliklar.forEach(function (h) { g.observe(h); });
    if (sira.length) { isaretle(sira[0]); }

    // Ahmet (23.09): "sagdaki icindekilerde 1.ciye donus olmuyor, ileri
    // gidis daha kolay olmali." Pencere yalniz cevreyi gosterdigi icin
    // uzaktaki bolume ulasmak zordu: onceki/sonraki, tum bolumler ve basa
    // don dugmeleri eklendi.
    if (yanToc) {
      var q = function (c) { return yanToc.querySelector(c); };
      if (q('.bs-toc-onceki')) { q('.bs-toc-onceki').addEventListener('click', function () { git(simdiki - 1); }); }
      if (q('.bs-toc-sonraki')) { q('.bs-toc-sonraki').addEventListener('click', function () { git(simdiki + 1); }); }
      if (q('.bs-toc-basa')) {
        q('.bs-toc-basa').addEventListener('click', function () { scrollTo({ top: 0, behavior: 'smooth' }); });
      }
      var hepsiDugme = q('.bs-toc-hepsi');
      if (hepsiDugme) {
        hepsiDugme.addEventListener('click', function () {
          hepsiAcik = !hepsiAcik;
          hepsiDugme.setAttribute('aria-expanded', String(hepsiAcik));
          hepsiDugme.textContent = hepsiAcik ? 'Daralt' : 'Tüm bölümler';
          yanToc.classList.toggle('bs-toc-acik', hepsiAcik);
          isaretle(gezinti[simdiki]);
        });
      }
    }
  }

  // 4) tiklanabilir kontrol listesi
  //
  // ⚠️ 23.09: bu bolum bir onceki duzenlemede YANLISLIKLA SILINMISTI
  // (icindekiler bolumu yeniden yazilirken aradaki kod da gitti); sayac
  // 0/10'da kaliyordu. Geri kondu ve Ahmet'in istegiyle tamamlaninca
  // tebrik satiri gosteriliyor.
  //
  // Isaretler YALNIZCA tarayicida saklanir; sunucuya hicbir sey gitmez.
  // localStorage gizli sekmede hata firlatabilir, her erisim try ile sarili.
  var sar = document.querySelector('.bs-kontrol-sar');
  if (sar) {
    var anahtar = 'ac-kontrol:' + (sar.getAttribute('data-yazi') || '');
    var kutular = [].slice.call(sar.querySelectorAll('input[type=checkbox]'));
    var toplam = kutular.length;
    var durum = sar.querySelector('.bs-kontrol-durum strong');
    var cubuk2 = sar.querySelector('.bs-kontrol-cubuk span');
    var sifirla = sar.querySelector('.bs-kontrol-sifirla');
    var tebrik = sar.querySelector('.bs-kontrol-tebrik');

    var oku = function () {
      try { return JSON.parse(localStorage.getItem(anahtar) || '[]') || []; } catch (e) { return []; }
    };
    var yazDepo = function (d) {
      try { localStorage.setItem(anahtar, JSON.stringify(d)); } catch (e) { /* yoksay */ }
    };
    var tazele = function () {
      var n = 0;
      for (var i = 0; i < toplam; i++) { if (kutular[i].checked) { n++; } }
      if (durum) { durum.textContent = String(n); }
      if (cubuk2) { cubuk2.style.width = toplam ? (n / toplam * 100).toFixed(0) + '%' : '0%'; }
      if (sifirla) { sifirla.hidden = n === 0; }
      var bitti = toplam > 0 && n === toplam;
      sar.classList.toggle('bs-bitti', bitti);
      if (tebrik) { tebrik.hidden = !bitti; }
    };

    var kayitli = oku();
    kutular.forEach(function (k, i) { if (kayitli.indexOf(i) !== -1) { k.checked = true; } });
    tazele();

    sar.addEventListener('change', function (e) {
      if (!e.target || e.target.type !== 'checkbox') { return; }
      var secili = [];
      kutular.forEach(function (k, i) { if (k.checked) { secili.push(i); } });
      yazDepo(secili);
      tazele();
    });
    if (sifirla) {
      sifirla.addEventListener('click', function () {
        kutular.forEach(function (k) { k.checked = false; });
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


  // 6) goruntulenme sayaci (Vercel fonksiyonu + Upstash Redis)
  //
  // Ahmet (23.09): "goruntulenme sayacini vercelde tutsak." Ayni tarayici
  // bir yaziyi gunde BIR KEZ sayar (yerel bayrak); sonraki acilislarda
  // yalniz okur. Depo bagli degilse ya da bir hata olursa sayac GIZLI
  // kalir: uydurma sayi gosterilmez. Sunucuya kisisel veri gitmez.
  var gor = document.querySelector('.bs-goruntulenme');
  if (gor && window.fetch) {
    var gyol = gor.getAttribute('data-yol') || '';
    var bugun = new Date().toISOString().slice(0, 10);
    var bayrak = 'ac-gor:' + gyol + ':' + bugun;
    var sayildi = false;
    try { sayildi = localStorage.getItem(bayrak) === '1'; } catch (e) { /* yoksay */ }
    fetch('/api/goruntulenme/?yol=' + encodeURIComponent(gyol), {
      method: sayildi ? 'GET' : 'POST', credentials: 'omit'
    })
      .then(function (r) { if (!r.ok) { throw new Error(String(r.status)); } return r.json(); })
      .then(function (v) {
        if (typeof v.sayi !== 'number' || v.sayi < 1) { return; }
        var alan = gor.querySelector('.bs-gor-sayi');
        if (alan) { alan.textContent = v.sayi.toLocaleString('tr-TR'); }
        gor.hidden = false;
        if (!sayildi) { try { localStorage.setItem(bayrak, '1'); } catch (e) { /* yoksay */ } }
      })
      .catch(function () { /* sayac gizli kalir */ });
  }

  // 7) sag blok: "En popüler / En yeni"
  //
  // Ahmet (23.09): "sag blokta en populer yazilar olsun, 5 tane gozuksun;
  // en populer en yeni diye degistirilebilsin." "En yeni" sunucuda hazir.
  // Populer sirasi /api/populer/ dan gelir; yanit yoksa, hata varsa ya da
  // hic sayim yoksa "En popüler" dugmesi GIZLI kalir. innerHTML YOK: gizli
  // basilmis ogeler yeniden dizilip acilir.
  var yb = document.querySelector('.bs-yazilar-blok');
  if (yb) {
    var sekmeler = [].slice.call(yb.querySelectorAll('.bs-yazilar-sekme button'));
    var paneller = [].slice.call(yb.querySelectorAll('.bs-yazilar'));
    var sec = function (ad) {
      sekmeler.forEach(function (b) { b.setAttribute('aria-pressed', String(b.getAttribute('data-sekme') === ad)); });
      paneller.forEach(function (p) { p.hidden = p.getAttribute('data-panel') !== ad; });
      var bas = yb.querySelector('.bs-yazilar-baslik');
      if (bas && bas.getAttribute('data-' + ad)) { bas.textContent = bas.getAttribute('data-' + ad); }
    };
    sekmeler.forEach(function (b) {
      b.addEventListener('click', function () { sec(b.getAttribute('data-sekme')); });
    });
    var ppanel = yb.querySelector('[data-panel="populer"]');
    var psekme = yb.querySelector('[data-sekme="populer"]');
    if (ppanel && psekme && window.fetch) {
      fetch('/api/populer/', { credentials: 'omit' })
        .then(function (r) { if (!r.ok) { throw new Error(String(r.status)); } return r.json(); })
        .then(function (v) {
          if (!v || !Array.isArray(v.yazilar) || !v.yazilar.length) { return; }
          var sira = {};
          v.yazilar.forEach(function (x, i) { if (x && typeof x.yol === 'string') { sira[x.yol] = i; } });
          var ogeler = [].slice.call(ppanel.children);
          var ilk = ogeler.map(function (li, i) { return [li, i]; });
          // sayimi olanlar sayiya gore, kalanlar "en yeni" sirasiyla
          ilk.sort(function (a, b) {
            var sa = a[0].getAttribute('data-yol'), sb = b[0].getAttribute('data-yol');
            var ka = Object.prototype.hasOwnProperty.call(sira, sa) ? sira[sa] : 1000 + a[1];
            var kb = Object.prototype.hasOwnProperty.call(sira, sb) ? sira[sb] : 1000 + b[1];
            return ka - kb;
          });
          var adet = parseInt(ppanel.getAttribute('data-adet'), 10) || 5;
          ilk.forEach(function (c, i) { c[0].hidden = i >= adet; ppanel.appendChild(c[0]); });
          var secici = yb.querySelector('.bs-yazilar-sekme');
          if (secici) { secici.hidden = false; }
          sec('populer');
        })
        .catch(function () { /* populer sekmesi gizli kalir */ });
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
