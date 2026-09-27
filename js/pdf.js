/* js/pdf.js — PDF merkezi, indirme bekleme ekrani ve belge dogrulama (28.09.2026)
 * Uretici: scripts/pdf_sayfalar.py. Veri: /pdf/kayit.json (surum defteri).
 * Dosya denetimi TARAYICIDA yapilir (SubtleCrypto SHA-256); dosya hicbir
 * yere gonderilmez. JS calismazsa: indirme dugmesi CSS ile 10 sn sonra acilir,
 * liste ve sayfalar okunur kalir. */
(function () {
  'use strict';
  var $ = function (s, k) { return (k || document).querySelector(s); };
  var $$ = function (s, k) { return [].slice.call((k || document).querySelectorAll(s)); };
  var AYLAR = ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'];
  function tarih(iso) { var p = iso.split('-'); return +p[2] + ' ' + AYLAR[+p[1] - 1] + ' ' + p[0]; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function katla(s) {
    return s.toLocaleLowerCase('tr').replace(/[çğıöşüâî]/g, function (c) { return { 'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u', 'â': 'a', 'î': 'i' }[c]; });
  }

  var kayitSozu = null;
  function kayit() {
    if (!kayitSozu) kayitSozu = fetch('/pdf/kayit.json', { cache: 'no-cache' }).then(function (r) {
      if (!r.ok) throw new Error('kayit ' + r.status); return r.json();
    });
    return kayitSozu;
  }
  function yayinda(b) { return b.surumler.filter(function (s) { return s.sha256 && s.yuklendi; }); }
  function durum(b, s) {
    var y = yayinda(b), i = y.map(function (x) { return x.surum; }).indexOf(s.surum);
    if (i < 0 || i === y.length - 1) return 'guncel';
    return y.slice(i + 1).some(function (x) { return x.tur === 'hata'; }) ? 'hata' : 'eski';
  }
  function kodYol(kd) { return kd.toLowerCase(); }

  // ── merkez: arama ──────────────────────────────────────────────────────
  var ara = $('[data-pdf-ara]');
  if (ara) {
    var satirlar = $$('.pdf-satir'), gruplar = $$('.pdf-grup'), sayi = $('[data-pdf-sayi]'), bos = $('[data-pdf-bos]');
    satirlar.forEach(function (s) { s._a = katla(s.getAttribute('data-ara')); });
    var suz = function () {
      var kelimeler = katla(ara.value.trim()).split(/\s+/).filter(Boolean), n = 0;
      satirlar.forEach(function (s) {
        var gor = kelimeler.every(function (k) { return s._a.indexOf(k) >= 0 || s._a.indexOf(k.replace('-', '')) >= 0; });
        s.hidden = !gor; if (gor) n++;
      });
      gruplar.forEach(function (g) { g.hidden = !$$('.pdf-satir', g).some(function (s) { return !s.hidden; }); });
      sayi.textContent = n + ' belge'; bos.hidden = n > 0;
    };
    ara.addEventListener('input', suz);
    if (location.hash.indexOf('#ara=') === 0) { ara.value = decodeURIComponent(location.hash.slice(5)); suz(); }
  }

  // ── indirme: 10 sn bekleme ─────────────────────────────────────────────
  // Ahmet (28.09): indirdikten sonra ya da hazir olup 60 sn icinde indirilmezse
  // dugme kalkar; yeniden indirmek icin 10 sn'lik dongu tekrar baslar. Kart
  // boyu degismez (dugme visibility ile gizli), sayfa kaymaz.
  var bekle = $('[data-pdf-bekle]');
  if (bekle) {
    var sure = +bekle.getAttribute('data-pdf-bekle') || 10, GECERLILIK = 60;
    var sayac = $('[data-pdf-kalan]', bekle), metin = $('[data-pdf-bekle-metin]', bekle);
    var indir = $('[data-pdf-indir]', bekle), yeniden = $('[data-pdf-yeniden]', bekle);
    var tik = null, dolum = null, tekrar = false;
    bekle.classList.add('js');
    var doldu = function () {
      bekle.classList.remove('hazir'); bekle.classList.add('doldu');
      sayac.textContent = sure; yeniden.hidden = false;
      metin.textContent = 'İndirme bağlantısının süresi doldu. PDF\'i yeniden hazırlamak için tıklayın.';
    };
    var baslat = function () {
      var basla = Date.now();
      clearInterval(tik); clearTimeout(dolum);
      bekle.classList.remove('hazir', 'doldu'); yeniden.hidden = true;
      sayac.textContent = sure;
      tik = setInterval(function () {
        var kalan = Math.max(0, sure - Math.floor((Date.now() - basla) / 1000));
        if (kalan <= 0) {
          clearInterval(tik);
          bekle.classList.add('hazir');
          sayac.textContent = '✓';
          metin.textContent = tekrar ? 'PDF\'iniz yeniden indirilmeye hazır.' : 'PDF\'iniz hazır. İyi çalışmalar!';
          dolum = setTimeout(doldu, GECERLILIK * 1000);
        } else {
          sayac.textContent = kalan;
          metin.innerHTML = (tekrar ? 'Yeniden indirmek için ' : 'PDF\'iniz hazırlanıyor. İndirme bağlantısı ')
            + '<strong>' + kalan + ' saniye</strong>' + (tekrar ? ' bekleyin.' : ' içinde açılacak.');
        }
      }, 250);
    };
    var indirildi = function () {
      if (!bekle.classList.contains('hazir')) return;
      clearTimeout(dolum); tekrar = true;
      metin.textContent = 'İndirme başladı.';
      setTimeout(baslat, 1500);   // indirme baslasin, sonra dugme kalksin
    };
    indir.addEventListener('click', indirildi);
    indir.addEventListener('auxclick', indirildi);
    yeniden.addEventListener('click', function () { tekrar = true; baslat(); });
    baslat();
  }

  // ── indirme sayilari (28.09) ───────────────────────────────────────────
  // Sunucudaki sayac (kaynak: medya erisim kaydi, bot ve ayni gun tekrari
  // sayilmaz, IP saklanmaz) medya.ahmetcelen.com.tr/pdf/indirme.json'a yazar.
  // Okunamazsa hicbir sey gosterilmez. Sayi KADEMELI gosterilir (Ahmet 28.09:
  // "10'dan fazla olmussa +10 indirme gibi kademe kademe; tesvik icin"):
  // 10+, 25+, 50+, 100+, 250+, 500+, 1.000+ ...; 10'un altinda gosterilmez.
  // Tam sayilar yalniz indirme.json'da (Ahmet'in izlemesi icin).
  var KADEMELER = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000];
  function kademe(n) {
    var k = 0;
    for (var i = 0; i < KADEMELER.length; i++) if (n >= KADEMELER[i]) k = KADEMELER[i];
    return k ? k.toLocaleString('tr-TR') + '+' : '';
  }
  var sayiYerleri = $$('[data-pdf-indirme]');
  if (sayiYerleri.length && window.fetch) {
    fetch('https://medya.ahmetcelen.com.tr/pdf/indirme.json', { cache: 'no-cache' })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) {
        if (!d || !d.belgeler) return;
        sayiYerleri.forEach(function (el) {
          var kd = el.getAttribute('data-pdf-indirme');
          var n = kd === '*' ? d.toplam : (kd ? d.belgeler[kd] : null);
          var metin = typeof n === 'number' ? kademe(n) : '';
          if (!metin) return;
          el.textContent = (el.getAttribute('data-onek') || '') + metin + ' indirme';
          el.hidden = false;
          var kutu = el.closest('[data-pdf-indirme-kutu]');
          if (kutu) { kutu.hidden = false; el.textContent = metin; }
        });
      }).catch(function () {});
  }

  // ── dogrulama: guncel olmayan surumden gunceline yonlendirme ───────────
  var yon = $('[data-pdf-yonlendir]'), yonMetin = $('[data-pdf-yonlendir-metin]');
  if (yon && yonMetin) {
    var sn = 8, iptal = false, kalanEl = $('[data-pdf-yonlendir-kalan]');
    yonMetin.hidden = false;
    $('[data-pdf-kal]').addEventListener('click', function () { iptal = true; yonMetin.hidden = true; });
    var t = setInterval(function () {
      if (iptal) return clearInterval(t);
      sn--; kalanEl.textContent = sn;
      if (sn <= 0) { clearInterval(t); location.href = yon.getAttribute('href'); }
    }, 1000);
  }

  // ── dogrulama: kodla git ───────────────────────────────────────────────
  var form = $('[data-pdf-kod-form]');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ham = form.kod.value.toUpperCase().replace(/\s+/g, ''), sonuc = $('[data-pdf-kod-sonuc]');
      var m = ham.match(/^(?:AC-?)?0*(\d{1,4})$/);
      if (!m) { sonuc.textContent = 'Belge kodu AC-066 biçiminde olmalı.'; return; }
      var kd = 'AC-' + ('00' + m[1]).slice(-3);
      kayit().then(function (k) {
        if (k.belgeler[kd] && yayinda(k.belgeler[kd]).length) location.href = '/d/' + kodYol(kd) + '/';
        else sonuc.textContent = kd + ' kodlu yayımlanmış bir belge bulunamadı.';
      }).catch(function () { sonuc.textContent = 'Kayıt okunamadı, lütfen biraz sonra tekrar deneyin.'; });
    });
  }

  // ── dogrulama: dosyanin SHA-256'si ─────────────────────────────────────
  $$('[data-pdf-dosya]').forEach(function (kutu) {
    var girdi = $('[data-pdf-dosya-girdi]', kutu), etiket = $('.pdf-dosya-sec', kutu), sonuc = $('.pdf-dosya-sonuc', kutu);
    if (!window.crypto || !crypto.subtle) { etiket.querySelector('span').textContent = 'Tarayıcınız dosya denetimini desteklemiyor.'; return; }
    function goster(sinif, html) { sonuc.className = 'pdf-dosya-sonuc ' + sinif; sonuc.innerHTML = html; sonuc.hidden = false; }
    // Ahmet (28.09): "buraya sadece PDF kabul edilsin, guvenlik zaafiyeti olabilir."
    // Dosya hicbir yere GONDERILMEZ ve ICERIGI ACILMAZ (PDF okuyucu calismaz);
    // yalniz baytlarinin SHA-256'si hesaplanir. Yine de: tek dosya, en fazla
    // 25 MB (yayinladigimiz PDF'ler 3 MB altinda; buyuk dosya sekmeyi
    // kilitlemesin), uzanti + MIME + ilk baytlardaki "%PDF-" imzasi birlikte.
    // Dosya ADI hicbir yerde ekrana basilmaz (yalniz defterdeki metinler, kacisli).
    var SINIR = 25 * 1048576;
    function pdfMi(dosya) {
      if (!/\.pdf$/i.test(dosya.name || '')) return Promise.resolve('Yalnız PDF dosyası (.pdf) kabul edilir.');
      if (dosya.type && dosya.type !== 'application/pdf') return Promise.resolve('Yalnız PDF dosyası kabul edilir.');
      if (!dosya.size) return Promise.resolve('Dosya boş görünüyor.');
      if (dosya.size > SINIR) return Promise.resolve('Dosya çok büyük (en fazla 25 MB). Yayımladığımız PDF\'ler 3 MB\'ın altındadır.');
      return dosya.slice(0, 5).arrayBuffer().then(function (b) {
        return String.fromCharCode.apply(null, new Uint8Array(b)) === '%PDF-' ? '' : 'Bu dosya geçerli bir PDF değil.';
      });
    }
    function denetle(dosyalar) {
      if (!dosyalar || !dosyalar.length) return;
      if (dosyalar.length > 1) { goster('yok', '<p>Lütfen tek bir PDF dosyası seçin.</p>'); return; }
      var dosya = dosyalar[0];
      pdfMi(dosya).then(function (hata) {
        if (hata) { goster('yok', '<p>' + esc(hata) + '</p>'); girdi.value = ''; return; }
        ozetle(dosya);
      });
    }
    function ozetle(dosya) {
      goster('', '<p>Denetleniyor…</p>');
      Promise.all([dosya.arrayBuffer().then(function (b) { return crypto.subtle.digest('SHA-256', b); }), kayit()]).then(function (r) {
        var ozet = [].map.call(new Uint8Array(r[0]), function (x) { return ('0' + x.toString(16)).slice(-2); }).join('');
        var bulunan = null;
        Object.keys(r[1].belgeler).some(function (kd) {
          var b = r[1].belgeler[kd];
          return yayinda(b).some(function (s) { if (s.sha256 === ozet) { bulunan = { kd: kd, b: b, s: s }; return true; } });
        });
        if (!bulunan) {
          goster('yok', '<p><strong>Bu dosya, yayımladığımız hiçbir sürümle eşleşmiyor.</strong></p>' +
            '<p>Dosya değiştirilmiş, yeniden kaydedilmiş ya da başka bir kaynaktan gelmiş olabilir. Güncel ve ücretsiz sürümü <a href="/pdf/">PDF Merkezi</a>nden indirebilirsiniz.</p>');
          return;
        }
        var b = bulunan.b, s = bulunan.s, d = durum(b, s), son = yayinda(b).slice(-1)[0];
        var bas = '<p><strong>Bu dosya, ahmetcelen.com.tr\'nin yayımladığı ' + esc(bulunan.kd) + ' · Sürüm ' + esc(s.surum) + ' ile birebir aynı.</strong> ' +
          esc(b.baslik) + ', ' + tarih(s.tarih) + '.</p>';
        if (d === 'guncel') goster('guncel', bas + '<p>Bu en güncel sürüm.</p>');
        else goster(d, bas + '<p>' + (d === 'hata' ? 'Bu sürümden sonra bir hata düzeltildi. ' : 'Daha yeni bir sürüm var. ') +
          'Güncel sürüm ' + esc(son.surum) + ': <a href="/pdf/' + esc(b.slug) + '/">güncel sürümü indirin</a>.</p>');
      }).catch(function () { goster('yok', '<p>Denetim yapılamadı, lütfen tekrar deneyin.</p>'); });
    }
    girdi.addEventListener('change', function () { denetle(girdi.files); });
    ['dragenter', 'dragover'].forEach(function (o) { etiket.addEventListener(o, function (e) { e.preventDefault(); etiket.classList.add('uzerinde'); }); });
    ['dragleave', 'drop'].forEach(function (o) { etiket.addEventListener(o, function () { etiket.classList.remove('uzerinde'); }); });
    etiket.addEventListener('drop', function (e) { e.preventDefault(); denetle(e.dataTransfer.files); });
    // Kutunun disina birakilan dosya tarayicida acilmasin (yanlislikla PDF'i sekmede acmak).
    ['dragover', 'drop'].forEach(function (o) { window.addEventListener(o, function (e) { if (!etiket.contains(e.target)) e.preventDefault(); }); });
  });
})();
