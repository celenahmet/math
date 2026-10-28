/* sinavlar/js/sinav-takvimi.js — 21.09.2026 (2. surum: yeni tasarim)
 *
 * Butun sinav geri sayim sayfalarinin TEK tarih kaynagi. Tarih degisince
 * yalnizca bu dosya guncellenir, ardindan `python3 scripts/sinav_sayfa_uygula.py`
 * kosulur (meta aciklama ve statik kart listesi ayni veriden uretilir).
 *
 * KAYNAK: yalnizca ÖSYM resmi sinav takvimi
 *   https://www.osym.gov.tr/Sayfa/SinavTakvimi   (21.09.2026'da alindi; KPSS On Lisans/Ortaogretim 22.09.2026)
 *   2027 takvimi: ÖSYM duyurusu 28.10.2026, PDF
 *   https://dokuman.osym.gov.tr/web/2026/10/osym-2027-yili-sinav-takvimi-7d09wi-28090734.pdf
 *   (28.10.2026'da okundu; 2027'de KPSS On Lisans/Ortaogretim yok, 2026 kaydi kalir)
 * Takvim siteleri, haber siteleri ve "tahmini tarih" iceren kaynaklar
 * KULLANILMAZ. ÖSYM yeni takvimi yayimlayinca asagidaki tablo guncellenir.
 *
 * NOT: ÖSYM takviminde sinav SAATI cogu sinav icin yayimlanmiyor; saat
 * yayimlanmissa o kullanilir, yayimlanmamissa geri sayimin calisabilmesi
 * icin 10:00 varsayilir ve sayfada saat GOSTERILMEZ.
 *
 * SONRAKI DONEM: ÖSYM yeni yilin takvimini her yil Ekim'de yayimliyor; o
 * sirada yilin son sinavlari (ALES/3) henuz yapilmamis oluyor. Boyle bir
 * sinava sonrakiDonem / sonrakiTarih / sonrakiSonuc (istege bagli
 * sonrakiEk) yazilir: sinav gunu gecince sayfa kendiliginden sonraki doneme
 * gecer (saat yayimlanmamis sayilir). Python ureticileri de ayni kurali
 * uygular (jsonld_uygula.js_sinavlar, sinav_sayfa_uygula.py).
 *
 * Sayfa DOM sozlesmesi (scripts/sinav_sayfa_uygula.py uretir):
 *   #gs-durum  durum cumlesi          #gs-sayac  4 kutu (gun/saat/dk/sn)
 *   #gs-gun #gs-saat #gs-dk #gs-sn    #gs-bilgi  cipler
 *   [data-sinav=anahtar] .gs-rozet    kart rozeti ("N gun kaldi" / "tamamlandi")
 *   #gs-kaynak                        kaynak + guncelleme satiri
 * jQuery gerektirmez.
 */
(function (window, document) {
  'use strict';

  var KAYNAK = 'https://www.osym.gov.tr/Sayfa/SinavTakvimi';
  var KAYNAK_TARIHI = '28.10.2026';

  /* ÖSYM 2027 takvimi (KPSS On Lisans/Ortaogretim 2026'dan kalir: iki yilda
     bir). saatResmi=false → saat ÖSYM'ce yayimlanmadi. */
  var SINAVLAR = {
    msu: {
      kisa: 'MSÜ', yol: 'msu',
      uzun: 'MSÜ (Millî Savunma Üniversitesi Askerî Öğrenci Aday Belirleme Sınavı)',
      donem: '2027-MSÜ', tarih: '2027-03-20', saat: '10:00', saatResmi: false,
      sonuc: '15.04.2027'
    },
    ales1: {
      kisa: 'ALES/1', yol: 'ales1',
      uzun: 'ALES/1 (Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı)',
      donem: '2027-ALES/1', tarih: '2027-04-18', saat: '10:00', saatResmi: false,
      sonuc: '07.05.2027'
    },
    ags: {
      kisa: 'AGS', yol: 'ags',
      uzun: 'AGS (Millî Eğitim Bakanlığı Akademi Giriş Sınavı)',
      donem: '2027-MEB-AGS', tarih: '2027-05-08', saat: '10:00', saatResmi: false,
      sonuc: '11.06.2027',
      ek: 'Öğretmenlik Alan Bilgisi Testi (ÖABT) oturumu: 09.05.2027'
    },
    tyt: {
      kisa: 'TYT', yol: 'tyt',
      uzun: 'TYT (Temel Yeterlilik Testi)',
      donem: '2027-YKS 1. Oturum (TYT)', tarih: '2027-06-19', saat: '10:00', saatResmi: false,
      sonuc: '21.07.2027'
    },
    ayt: {
      kisa: 'AYT', yol: 'ayt',
      uzun: 'AYT (Alan Yeterlilik Testi)',
      donem: '2027-YKS 2. Oturum (AYT)', tarih: '2027-06-20', saat: '10:00', saatResmi: false,
      sonuc: '21.07.2027'
    },
    ales2: {
      kisa: 'ALES/2', yol: 'ales2',
      uzun: 'ALES/2 (Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı)',
      donem: '2027-ALES/2', tarih: '2027-07-11', saat: '10:00', saatResmi: false,
      sonuc: '30.07.2027'
    },
    dgs: {
      kisa: 'DGS', yol: 'dgs',
      uzun: 'DGS (Dikey Geçiş Sınavı)',
      donem: '2027-DGS', tarih: '2027-07-18', saat: '10:00', saatResmi: false,
      sonuc: '12.08.2027'
    },
    kpssa: {
      kisa: 'KPSS', yol: 'kpssa',
      uzun: 'KPSS Lisans (Kamu Personel Seçme Sınavı)',
      donem: '2027-KPSS A Grubu (Genel Yetenek-Genel Kültür)', tarih: '2027-09-12', saat: '10:00', saatResmi: false,
      sonuc: '13.10.2027',
      ek: 'Alan Bilgisi oturumları: 18.09.2027 ve 19.09.2027'
    },
    kpssonlisans: {
      kisa: 'KPSS Ön Lisans', yol: 'kpss-onlisans',
      uzun: 'KPSS Ön Lisans (Kamu Personel Seçme Sınavı)',
      donem: '2026-KPSS Ön Lisans', tarih: '2026-10-04', saat: '10:15', saatResmi: true,
      sonuc: '30.10.2026', ikiYilda: true,
      ek: 'KPSS Ön Lisans genellikle iki yılda bir düzenlenir'
    },
    kpssorta: {
      kisa: 'KPSS Ortaöğretim', yol: 'kpss-ortaogretim',
      uzun: 'KPSS Ortaöğretim (Kamu Personel Seçme Sınavı)',
      donem: '2026-KPSS Ortaöğretim', tarih: '2026-10-25', saat: '10:00', saatResmi: false,
      sonuc: '19.11.2026', ikiYilda: true,
      ek: 'KPSS Ortaöğretim genellikle iki yılda bir düzenlenir'
    },
    ales3: {
      kisa: 'ALES/3', yol: 'ales3',
      uzun: 'ALES/3 (Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı)',
      donem: '2026-ALES/3', tarih: '2026-11-29', saat: '10:00', saatResmi: false,
      sonuc: '17.12.2026',
      sonrakiDonem: '2027-ALES/3', sonrakiTarih: '2027-11-28', sonrakiSonuc: '17.12.2027'
    }
  };

  /* Kart listesinde gosterilme sirasi: 2027 takvim sirasi (ALES/2 bu yil
     DGS'den once). AGS 28.10.2026'da eklendi. */
  var SIRA = ['msu', 'ales1', 'ags', 'tyt', 'ayt', 'ales2', 'dgs', 'kpssa', 'kpssonlisans', 'kpssorta', 'ales3'];

  var KOK = '/sinavlar/';

  function parcala(s) {
    var p = s.split('-');
    return { yil: +p[0], ay: +p[1], gun: +p[2] };
  }

  function tarihNesnesi(sinav) {
    var d = parcala(sinav.tarih);
    var sa = sinav.saat.split(':');
    return new Date(d.yil, d.ay - 1, d.gun, +sa[0], +sa[1], 0);
  }

  function gosterimTarihi(sinav) {
    var d = parcala(sinav.tarih);
    function iki(n) { return (n < 10 ? '0' : '') + n; }
    return iki(d.gun) + '.' + iki(d.ay) + '.' + d.yil;
  }

  function gectiMi(sinav) {
    return tarihNesnesi(sinav).getTime() <= Date.now();
  }

  /* Takvim gunu farki (saatten bagimsiz): "N gun kaldi" rozeti icin. */
  function kalanGun(sinav) {
    var d = parcala(sinav.tarih);
    var hedef = new Date(d.yil, d.ay - 1, d.gun);
    var bugun = new Date(); bugun.setHours(0, 0, 0, 0);
    return Math.round((hedef - bugun) / 86400000);
  }

  /* Sinav gecti ve sonraki donemi biliniyorsa sonraki donem; yoksa kendisi. */
  function gecerli(s) {
    if (!s || !s.sonrakiTarih || !gectiMi(s)) { return s; }
    return {
      kisa: s.kisa, yol: s.yol, uzun: s.uzun, donem: s.sonrakiDonem, tarih: s.sonrakiTarih,
      saat: '10:00', saatResmi: false, sonuc: s.sonrakiSonuc, ek: s.sonrakiEk
    };
  }

  /* Tarihi en yakin, henuz yapilmamis sinav. SIRA sirasina guvenilmez:
     yeni yil takvimi gelince listede iki yil bir arada bulunur. */
  function siradakiSinav() {
    var en = null;
    for (var i = 0; i < SIRA.length; i++) {
      var s = gecerli(SINAVLAR[SIRA[i]]);
      if (!gectiMi(s) && (!en || tarihNesnesi(s) < tarihNesnesi(en))) { en = s; }
    }
    return en;
  }

  function el(id) { return document.getElementById(id); }
  function iki(n) { return (n < 10 ? '0' : '') + n; }

  function cip(metin) { return '<span class="gs-cip">' + metin + '</span>'; }

  /* Kart rozetleri: her sayfada ayni, tarih durumuna gore. */
  function rozetleriYaz(bulunduguAnahtar) {
    var kartlar = document.querySelectorAll('[data-sinav]');
    for (var i = 0; i < kartlar.length; i++) {
      var k = kartlar[i], s = gecerli(SINAVLAR[k.getAttribute('data-sinav')]);
      var r = k.querySelector('.gs-rozet');
      if (!s || !r) { continue; }
      var t = k.querySelector('.gs-kart-tarih');
      if (t) { t.textContent = gosterimTarihi(s); }
      if (gectiMi(s)) {
        r.textContent = 'Tamamlandı'; r.className = 'gs-rozet gs-bitti';
      } else {
        var g = kalanGun(s);
        r.textContent = g <= 0 ? 'Bugün' : g + ' gün kaldı'; r.className = 'gs-rozet gs-yakin';
      }
      if (k.getAttribute('data-sinav') === bulunduguAnahtar) { k.className += ' gs-secili'; }
    }
  }

  function sayaciBaslat(sinav) {
    var kutu = el('gs-sayac');
    if (!kutu) { return; }
    kutu.hidden = false;
    var hedef = tarihNesnesi(sinav).getTime();
    function tik() {
      var fark = Math.max(0, hedef - Date.now());
      var sn = Math.floor(fark / 1000);
      el('gs-gun').textContent = Math.floor(sn / 86400);
      el('gs-saat').textContent = iki(Math.floor(sn % 86400 / 3600));
      el('gs-dk').textContent = iki(Math.floor(sn % 3600 / 60));
      el('gs-sn').textContent = iki(sn % 60);
      if (fark <= 0) { clearInterval(z); durumYaz(sinav, true); }
    }
    tik();
    var z = setInterval(tik, 1000);
  }

  /* sonuc 'GG.AA.YYYY': o gün başladıysa açıklandı sayılır. */
  function sonucAciklandiMi(s) {
    var p = s.sonuc.split('.');
    return new Date(+p[2], +p[1] - 1, +p[0]) <= new Date();
  }

  function durumYaz(s, one) {
    var d = el('gs-durum');
    if (!d) { return; }
    var tarih = gosterimTarihi(s);
    if (!gectiMi(s)) {
      d.innerHTML = (one ? '' : '') + '<strong>' + s.donem + '</strong> sınavı <strong>' + tarih + '</strong>' +
        (s.saatResmi ? ' saat ' + s.saat : '') + ' tarihinde yapılacak.' +
        (s.ek ? '<br>' + s.ek + '.' : '');
    } else {
      var siradaki = siradakiSinav();
      d.innerHTML = '<strong>' + s.donem + '</strong> sınavı <strong>' + tarih + '</strong> tarihinde yapıldı' +
        (s.sonuc ? ', sonuçlar ' + s.sonuc + ' tarihinde ' + (sonucAciklandiMi(s) ? 'açıklandı' : 'açıklanacak') : '') + '.' +
        (s.ek ? '<br>' + s.ek + '.' : '') +
        (s.ikiYilda
          ? '<br>Bir sonraki dönemin tarihi ÖSYM takviminde yayımlandığında geri sayım bu sayfada yeniden başlar.'
          : '<br>' + (parcala(s.tarih).yil + 1) + ' sınav takvimi ÖSYM tarafından henüz yayımlanmadı; yayımlandığında geri sayım bu sayfada yeniden başlar.') +
        (siradaki && siradaki !== s
          ? '<br>Şu an geri sayımı süren sınav: <a href="' + KOK + siradaki.yol + '/"><strong>' +
            siradaki.donem + '</strong> · ' + gosterimTarihi(siradaki) + '</a>'
          : '');
    }
  }

  function bilgiYaz(s) {
    var b = el('gs-bilgi');
    if (!b) { return; }
    var h = cip('Sınav tarihi: <strong>' + gosterimTarihi(s) + '</strong>');
    if (s.saatResmi) { h += cip('Saat: <strong>' + s.saat + '</strong>'); }
    if (s.sonuc) { h += cip('Sonuç: <strong>' + s.sonuc + '</strong>'); }
    h += cip('Kaynak: <a href="' + KAYNAK + '" target="_blank" rel="noopener">ÖSYM sınav takvimi</a>');
    b.innerHTML = h;
  }

  function kaynakYaz() {
    var k = el('gs-kaynak');
    if (!k) { return; }
    k.innerHTML = 'Tarihler ÖSYM resmî sınav takviminden alınmıştır (<a href="' + KAYNAK +
      '" target="_blank" rel="noopener">osym.gov.tr</a>). Sınavı düzenleyen kurum tarihi değiştirebilir. ' +
      'Bu sayfa <strong>' + KAYNAK_TARIHI + '</strong> tarihinde güncellendi.';
  }

  /**
   * Sayfayi baslatir.
   * @param {string} anahtar SINAVLAR anahtari (tyt, ayt, ...) ya da 'tumu'
   *   (genel sayfa: geri sayimi suren en yakin sinav one cikar).
   */
  function sinavGeriSayim(anahtar) {
    var s = anahtar === 'tumu' ? siradakiSinav() : gecerli(SINAVLAR[anahtar]);
    if (!s) {
      var d = el('gs-durum');
      if (d) { d.textContent = 'Bir sonraki sınav takvimi ÖSYM tarafından henüz yayımlanmadı.'; }
      rozetleriYaz(null); kaynakYaz();
      return;
    }
    if (anahtar === 'tumu') {
      var b = el('gs-one-cikan');
      if (b) { b.innerHTML = 'Sıradaki sınav: <a href="' + KOK + s.yol + '/">' + s.uzun + '</a>'; }
    }
    durumYaz(s);
    if (!gectiMi(s)) { sayaciBaslat(s); }
    bilgiYaz(s);
    rozetleriYaz(anahtar === 'tumu' ? s.yol : anahtar);
    kaynakYaz();
  }

  window.SINAV_TAKVIMI = { sinavlar: SINAVLAR, sira: SIRA, kaynak: KAYNAK, kaynakTarihi: KAYNAK_TARIHI };
  window.sinavGeriSayim = sinavGeriSayim;
})(window, document);
