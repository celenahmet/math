/* js/etkilesim.js — yazi sonu etkilesimi: faydali mi, ifade, yorum (25.09.2026)
 *
 * Sunucu: api/etkilesim.js (guvenlik ve kisisel veri notu api/_etkilesim.js).
 * Kapali hata: depo bagli degilse (503) ya da tarayici is kanitini
 * hesaplayamiyorsa bolumler GIZLI kalir; uydurma sayi, islemeyen dugme yok.
 * Performans: yalniz yazi sayfalarinda, defer ile gelir; veri yazi sonuna
 * yaklasinca istenir, ilk boyamaya ve LCP'ye dokunmaz.
 */
(function () {
  'use strict';

  var kart = document.querySelector('.bs-etk');
  var yb = document.querySelector('.bs-yorumlar');
  if (!kart && !yb) { return; }
  if (!window.fetch || !window.crypto || !crypto.subtle || !window.TextEncoder || !window.Promise) { return; }
  var yol = (kart || yb).getAttribute('data-yol');
  var API = '/api/etkilesim/';

  // Okura donuk metinler VARSAYILAN; son hali Ahmet'in.
  var METIN = {
    sinir: 'Bu ağdan bu yazıya bugün yeterince tepki verildi.',
    hiz: 'Çok sık denendi, biraz sonra yeniden dene.',
    hata: 'Kaydedilemedi, biraz sonra yeniden dene.',
    geriTamam: 'Mesajın iletildi.',
    yorumTamam: 'Yorumun alındı; onaylandıktan sonra burada görünecek.',
    rumuz: 'Ad ya da rumuz 2 ile 40 karakter arasında olmalı; harf, rakam, boşluk ve . - _ kullanılabilir.',
    metin: 'Metin en az 3 karakter olmalı.',
    baglanti: 'En çok iki bağlantı eklenebilir.',
    kuyruk: 'Şu an yeni yorum alınamıyor, biraz sonra yeniden dene.'
  };

  // ── yerel durum ──
  // Kendi secimin tarayicida tutulur (dugmeyi basili gostermek icin).
  // Sayac CDN'de 20 sn onbellekli: oy verip hemen yenileyen okur eski
  // sayiyi gormesin diye son yanit oturumda 60 sn saklanir.
  var SAKLA = 'etk:' + yol, OTURUM = 'etk-sayi:' + yol;
  function oku(depo, a) { try { return JSON.parse(depo.getItem(a)); } catch (e) { return null; } }
  function yaz(depo, a, d) { try { depo.setItem(a, JSON.stringify(d)); } catch (e) { /* gizli sekme */ } }
  var ben = oku(localStorage, SAKLA) || {};
  var son = { oy: {}, ifade: {} };

  // ── is kaniti ──
  // Sunucunun imzaladigi bulmaca; cozum tek kullanimlik. Bir sonraki
  // islem icin cozum ARKA PLANDA hazirlanir: tiklama beklemez.
  var hazir = null, suruyor = null;
  function hex(buf) {
    var b = new Uint8Array(buf), s = '';
    for (var i = 0; i < b.length; i++) { s += (b[i] < 16 ? '0' : '') + b[i].toString(16); }
    return s;
  }
  function coz() {
    if (hazir) { return Promise.resolve(hazir); }
    if (suruyor) { return suruyor; }
    suruyor = fetch(API + '?meydan=1', { credentials: 'omit', cache: 'no-store' })
      .then(function (r) { if (!r.ok) { throw new Error('bulmaca'); } return r.json(); })
      .then(function (m) {
        var enc = new TextEncoder(), n = 0;
        return new Promise(function (tamam, red) {
          // 400'luk yiginlar: tarayici paralel hesaplar, aralarda sekmeye nefes verilir.
          (function tur() {
            var bas = n, isler = [];
            for (; n <= m.ust && n < bas + 400; n++) { isler.push(crypto.subtle.digest('SHA-256', enc.encode(m.tuz + n))); }
            Promise.all(isler).then(function (l) {
              for (var i = 0; i < l.length; i++) {
                if (hex(l[i]) === m.meydan) { return tamam({ tuz: m.tuz, meydan: m.meydan, imza: m.imza, sayi: bas + i }); }
              }
              if (n > m.ust) { return red(new Error('cozum')); }
              setTimeout(tur, 0);
            }, red);
          })();
        });
      })
      .then(function (c) { hazir = c; suruyor = null; return c; },
            function (e) { suruyor = null; throw e; });
    return suruyor;
  }
  function hazirla() { setTimeout(function () { coz().catch(function () {}); }, 30); }

  function gonder(veri) {
    return coz().then(function (cozum) {
      hazir = null;   // tek kullanimlik
      veri.yol = yol;
      veri.cozum = cozum;
      return fetch(API, {
        method: 'POST', credentials: 'same-origin',
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(veri)
      });
    }).then(function (r) {
      hazirla();
      return r.json().catch(function () { return {}; }).then(function (j) { j.kod = r.status; return j; });
    });
  }

  // ── sayilar ve secimler ──
  function kopya(s) { return JSON.parse(JSON.stringify(s)); }
  function sayilariBas(s) {
    son = { oy: s.oy || {}, ifade: s.ifade || {} };
    [].forEach.call(document.querySelectorAll('.bs-etk-n'), function (el) {
      var a = el.getAttribute('data-n');
      var v = a.indexOf('i:') === 0 ? son.ifade[a.slice(2)] : son.oy[a];
      el.textContent = v > 0 ? String(v) : '';
    });
  }
  function secimleriBas() {
    if (!kart) { return; }
    [].forEach.call(kart.querySelectorAll('[data-oy]'), function (b) {
      b.setAttribute('aria-pressed', String(ben.oy === b.getAttribute('data-oy')));
    });
    [].forEach.call(kart.querySelectorAll('[data-ifade]'), function (b) {
      b.setAttribute('aria-pressed', String(ben.ifade === b.getAttribute('data-ifade')));
    });
  }
  function hataMetni(j) {
    return METIN[{ sinir: 'sinir', hiz: 'hiz', rumuz: 'rumuz', metin: 'metin', baglanti: 'baglanti', 'kuyruk-dolu': 'kuyruk' }[j.hata]] || METIN.hata;
  }

  // ── faydali mi + ifade ──
  if (kart) {
    var durumK = kart.querySelector('.bs-etk-durum');
    var geri = kart.querySelector('.bs-etk-geri');
    var mesgul = false;
    var durum = function (t) { durumK.textContent = t || ''; };
    var geriGoster = function (ac) {
      geri.hidden = !ac;
      if (ac) { geri.querySelector('textarea').focus({ preventScroll: true }); }
    };

    var sec = function (tur, deger) {
      if (mesgul) { return; }
      var alan = tur === 'oy' ? 'oy' : 'ifade';
      var eskiBen = { oy: ben.oy || '', ifade: ben.ifade || '' };
      var eskiSay = kopya(son);
      var yeni = eskiBen[alan] === deger ? '' : deger;
      // Iyimser guncelleme: tiklama aninda gorunur, sunucu yaniti duzeltir.
      var s = kopya(son), kume = s[alan];
      if (eskiBen[alan]) { kume[eskiBen[alan]] = Math.max(0, (kume[eskiBen[alan]] || 0) - 1); }
      if (yeni) { kume[yeni] = (kume[yeni] || 0) + 1; }
      ben[alan] = yeni;
      sayilariBas(s);
      secimleriBas();
      durum('');
      if (tur === 'oy') { geriGoster(yeni === 'begenmeme'); }
      mesgul = true;
      kart.setAttribute('aria-busy', 'true');
      gonder({ tur: tur, deger: yeni }).then(function (j) {
        if (j.oy) {
          // Basarida da sinirda da sunucunun bildigi secim ve GERCEK sayilar esas.
          ben[alan] = j.secim || '';
          sayilariBas({ oy: j.oy, ifade: j.ifade });
          yaz(sessionStorage, OTURUM, { t: Date.now(), oy: j.oy, ifade: j.ifade });
        } else {
          ben = eskiBen;
          sayilariBas(eskiSay);
        }
        if (j.kod !== 200) { durum(hataMetni(j)); }
      }, function () {
        ben = eskiBen;
        sayilariBas(eskiSay);
        durum(METIN.hata);
      }).then(function () {
        yaz(localStorage, SAKLA, ben);
        secimleriBas();
        if (tur === 'oy' && ben.oy !== 'begenmeme') { geriGoster(false); }
        mesgul = false;
        kart.removeAttribute('aria-busy');
      });
    };

    kart.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-oy], button[data-ifade]');
      if (!b) { return; }
      if (b.hasAttribute('data-oy')) { sec('oy', b.getAttribute('data-oy')); }
      else { sec('ifade', b.getAttribute('data-ifade')); }
    });
    kart.querySelector('.bs-etk-vazgec').addEventListener('click', function () { geriGoster(false); });
    geri.addEventListener('submit', function (e) {
      e.preventDefault();
      var alanG = geri.querySelector('textarea'), dugme = geri.querySelector('[type=submit]');
      var t = alanG.value.trim();
      if (t.length < 3) { durum(METIN.metin); return; }
      dugme.disabled = true;
      gonder({ tur: 'geri', metin: t }).then(function (j) {
        if (j.kod === 200) { geri.reset(); geriGoster(false); durum(METIN.geriTamam); }
        else { durum(hataMetni(j)); }
      }, function () { durum(METIN.hata); }).then(function () { dugme.disabled = false; });
    });
  }

  // ── yorumlar ──
  var tarih = function (ms) {
    try { return new Date(ms).toLocaleDateString('tr-TR', { day: 'numeric', month: 'long', year: 'numeric' }); }
    catch (e) { return ''; }
  };
  function yorumlariBas(l) {
    var liste = yb.querySelector('.bs-yorum-liste');
    liste.textContent = '';
    l.forEach(function (y) {
      // textContent: yorum metni HTML olarak ASLA yorumlanmaz.
      var li = document.createElement('li');
      var ust = document.createElement('p');
      ust.className = 'bs-yorum-ust';
      var ad = document.createElement('strong');
      ad.textContent = y.rumuz;
      var t = document.createElement('time');
      t.dateTime = new Date(y.zaman).toISOString();
      t.textContent = tarih(y.zaman);
      ust.appendChild(ad);
      ust.appendChild(t);
      var m = document.createElement('p');
      m.className = 'bs-yorum-metin';
      m.textContent = y.metin;
      li.appendChild(ust);
      li.appendChild(m);
      liste.appendChild(li);
    });
    yb.querySelector('.bs-yorum-sayi').textContent = l.length ? String(l.length) : '';
    yb.querySelector('.bs-yorum-bos').hidden = l.length > 0;
  }
  if (yb) {
    var form = yb.querySelector('.bs-yorum-form');
    var ac = yb.querySelector('.bs-yorum-ac');
    var durumY = yb.querySelector('.bs-yorum-durum');
    var formAc = function (evet) {
      form.hidden = !evet;
      ac.hidden = evet;
      ac.setAttribute('aria-expanded', String(evet));
      if (evet) {
        var r = oku(localStorage, 'etk-rumuz');
        if (r && !form.rumuz.value) { form.rumuz.value = r; }
        (form.rumuz.value ? form.metin : form.rumuz).focus();
      }
    };
    ac.addEventListener('click', function () { durumY.textContent = ''; formAc(true); });
    yb.querySelector('.bs-yorum-vazgec').addEventListener('click', function () { formAc(false); });
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var dugme = form.querySelector('[type=submit]');
      var rumuz = form.rumuz.value.trim(), metin = form.metin.value.trim();
      if (rumuz.length < 2) { durumY.textContent = METIN.rumuz; return; }
      if (metin.length < 3) { durumY.textContent = METIN.metin; return; }
      dugme.disabled = true;
      durumY.textContent = '';
      gonder({ tur: 'yorum', rumuz: rumuz, metin: metin, web: form.web.value }).then(function (j) {
        if (j.kod === 200) {
          yaz(localStorage, 'etk-rumuz', rumuz);
          form.metin.value = '';
          formAc(false);
          durumY.textContent = METIN.yorumTamam;
        } else {
          durumY.textContent = hataMetni(j);
        }
      }, function () { durumY.textContent = METIN.hata; }).then(function () { dugme.disabled = false; });
    });
  }

  // ── yukleme ──
  function yukle() {
    fetch(API + '?yol=' + encodeURIComponent(yol), { credentials: 'omit', cache: 'no-cache' })
      .then(function (r) { if (!r.ok) { throw new Error('depo'); } return r.json(); })
      .then(function (j) {
        var o = oku(sessionStorage, OTURUM);
        sayilariBas(o && Date.now() - o.t < 60000 ? o : j);
        secimleriBas();
        if (kart) { kart.hidden = false; }
        if (yb) { yorumlariBas(j.yorumlar || []); yb.hidden = false; }
        hazirla();
      })
      .catch(function () { /* depo yok ya da ag hatasi: bolumler gizli kalir */ });
  }
  // Gizli ogeyi IntersectionObserver goremez (kutusu yok); yazinin sonuna
  // yaklasildigini gorunur bir komsudan anliyoruz.
  var isaret = document.getElementById('b-kontrol') || document.querySelector('.bs-paylas');
  if (isaret && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (g) {
      if (g.some(function (x) { return x.isIntersecting; })) { io.disconnect(); yukle(); }
    }, { rootMargin: '1200px 0px' });
    io.observe(isaret);
  } else {
    yukle();
  }
})();
