/* sinavlar/js/sinav-takvimi.js — 21.09.2026
 *
 * Butun sinav geri sayim sayfalarinin TEK tarih kaynagi. Tarih degisince
 * yalnizca bu dosya guncellenir; 9 sayfaya tek tek dokunulmaz.
 *
 * KAYNAK: yalnizca ÖSYM resmi sinav takvimi
 *   https://www.osym.gov.tr/Sayfa/SinavTakvimi   (21.09.2026'da alindi)
 * Takvim siteleri, haber siteleri ve "tahmini tarih" iceren kaynaklar
 * KULLANILMAZ. ÖSYM yeni takvimi yayimlayinca asagidaki tablo guncellenir.
 *
 * NOT: ÖSYM takviminde sinav SAATI cogu sinav icin yayimlanmiyor; saat
 * yayimlanmissa o kullanilir, yayimlanmamissa geri sayimin calisabilmesi
 * icin 10:00 varsayilir ve sayfada saat GOSTERILMEZ.
 */
(function (window) {
  'use strict';

  var KAYNAK = 'https://www.osym.gov.tr/Sayfa/SinavTakvimi';
  var KAYNAK_TARIHI = '21.09.2026';

  /* ÖSYM 2026 takvimi. saatResmi=false → saat ÖSYM'ce yayimlanmadi. */
  var SINAVLAR = {
    msu: {
      kisa: 'MSÜ', yol: 'msu',
      uzun: 'MSÜ (Millî Savunma Üniversitesi Askerî Öğrenci Aday Belirleme Sınavı)',
      donem: '2026-MSÜ', tarih: '2026-03-01', saat: '10:15', saatResmi: true,
      sonuc: '24.03.2026'
    },
    ales1: {
      kisa: 'ALES/1', yol: 'ales1',
      uzun: 'ALES/1 (Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı)',
      donem: '2026-ALES/1', tarih: '2026-05-10', saat: '10:00', saatResmi: false,
      sonuc: '05.06.2026'
    },
    tyt: {
      kisa: 'TYT', yol: 'tyt',
      uzun: 'TYT (Temel Yeterlilik Testi)',
      donem: '2026-YKS 1. Oturum (TYT)', tarih: '2026-06-20', saat: '10:00', saatResmi: false,
      sonuc: '21.07.2026'
    },
    ayt: {
      kisa: 'AYT', yol: 'ayt',
      uzun: 'AYT (Alan Yeterlilik Testi)',
      donem: '2026-YKS 2. Oturum (AYT)', tarih: '2026-06-21', saat: '10:00', saatResmi: false,
      sonuc: '21.07.2026'
    },
    dgs: {
      kisa: 'DGS', yol: 'dgs',
      uzun: 'DGS (Dikey Geçiş Sınavı)',
      donem: '2026-DGS', tarih: '2026-07-19', saat: '10:00', saatResmi: false,
      sonuc: '13.08.2026'
    },
    ales2: {
      kisa: 'ALES/2', yol: 'ales2',
      uzun: 'ALES/2 (Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı)',
      donem: '2026-ALES/2', tarih: '2026-08-02', saat: '10:00', saatResmi: false,
      sonuc: '14.08.2026'
    },
    kpssa: {
      kisa: 'KPSS', yol: 'kpssa',
      uzun: 'KPSS Lisans (Kamu Personel Seçme Sınavı)',
      donem: '2026-KPSS Lisans (Genel Yetenek-Genel Kültür)', tarih: '2026-09-06', saat: '10:00', saatResmi: false,
      sonuc: '07.10.2026',
      ek: 'Alan Bilgisi oturumları: 12.09.2026 ve 13.09.2026'
    },
    ales3: {
      kisa: 'ALES/3', yol: 'ales3',
      uzun: 'ALES/3 (Akademik Personel ve Lisansüstü Eğitimi Giriş Sınavı)',
      donem: '2026-ALES/3', tarih: '2026-11-29', saat: '10:00', saatResmi: false,
      sonuc: '17.12.2026'
    }
  };

  /* Listede gosterilme sirasi: takvim sirasi. */
  var SIRA = ['msu', 'ales1', 'tyt', 'ayt', 'dgs', 'ales2', 'kpssa', 'ales3'];

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
    return tarihNesnesi(sinav).getTime() <= new Date().getTime();
  }

  /* "Diger Sinavlar" listesi: her sayfada ayni, tek yerden uretilir. */
  function digerSinavlar(bulunduguAnahtar) {
    var html = '<p>Diğer Sınavlar</p>';
    for (var i = 0; i < SIRA.length; i++) {
      var a = SIRA[i];
      if (a === bulunduguAnahtar) continue;
      var s = SINAVLAR[a];
      var etiket = gosterimTarihi(s) + (gectiMi(s) ? ' (tamamlandı)' : '');
      html += '<p><a href="' + KOK + s.yol + '">' + s.uzun + '</a> ' + etiket + '</p>';
    }
    return html;
  }

  function kaynakSatiri() {
    return '<p style="font-size:13px;opacity:.85;">Tarihler ÖSYM resmî sınav takviminden alınmıştır ' +
      '(<a href="' + KAYNAK + '" target="_blank" rel="noopener">osym.gov.tr</a>).<br>' +
      'Bu sayfa <strong>' + KAYNAK_TARIHI + '</strong> tarihinde güncellendi.</p>';
  }

  /**
   * Sayfayi baslatir.
   * @param {string} anahtar SINAVLAR icindeki anahtar (tyt, ayt, dgs, ...)
   */
  function sinavGeriSayim(anahtar) {
    var s = SINAVLAR[anahtar];
    if (!s) { return; }
    /* Sayfa kendi sinavi gecmisse, ziyaretciyi en yakin ileri tarihli
       sinava yonlendirebilmek icin o sinavi hesapla. */
    var siradaki = null;
    for (var i = 0; i < SIRA.length; i++) {
      if (!gectiMi(SINAVLAR[SIRA[i]])) { siradaki = SINAVLAR[SIRA[i]]; break; }
    }

    var tarihMetni = gosterimTarihi(s);
    var $slogan = jQuery('.slogan');
    var $sayim = jQuery('.count-down-wrapper');

    if (!gectiMi(s)) {
      /* Sinav ileride: knob geri sayimi calissin. */
      var d = parcala(s.tarih);
      jQuery('.count-down').ccountdown(d.gun, d.ay, d.yil, s.saat);
      $slogan.find('p').first().html(
        '<strong>' + s.donem + '</strong> · ' + tarihMetni +
        '<br>Aşağıda gün, saat, dakika, saniye biçiminde canlı geri sayım bulunmaktadır.'
      );
    } else {
      /* Sinav gecti: yaniltici geri sayim gosterme. */
      $sayim.hide();
      $slogan.find('p').first().html(
        '<strong>' + s.donem + '</strong> sınavı <strong>' + tarihMetni + '</strong> tarihinde yapıldı' +
        (s.sonuc ? ', sonuçlar ' + s.sonuc + ' tarihinde açıklandı' : '') + '.' +
        (s.ek ? '<br>' + s.ek + '.' : '') +
        '<br><strong>2027 sınav takvimi ÖSYM tarafından henüz yayımlanmadı.</strong> ' +
        'Takvim yayımlandığında geri sayım bu sayfada yeniden başlayacak.' +
        (siradaki && siradaki !== s
          ? '<br>Şu an geri sayımı süren sınav: <a href="' + KOK + siradaki.yol + '">' +
            siradaki.donem + ' · ' + gosterimTarihi(siradaki) + '</a>'
          : '')
      );
    }

    var $liste = jQuery('#diger-sinavlar');
    if ($liste.length) {
      $liste.html(digerSinavlar(anahtar) + kaynakSatiri());
    }
  }

  window.SINAV_TAKVIMI = { sinavlar: SINAVLAR, sira: SIRA, kaynak: KAYNAK };
  window.sinavGeriSayim = sinavGeriSayim;
})(window);
