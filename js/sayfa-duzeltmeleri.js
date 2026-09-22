/* js/sayfa-duzeltmeleri.js — 22.09.2026
 *
 * Tema betiginden (js/script.js) ONCE, jQuery ve eklentilerden SONRA yuklenir.
 * Tema dosyalarina dokunmadan davranis duzeltir; her madde OLCULMUS bir
 * soruna karsilik gelir. Olcum araci: Lighthouse (masaustu), /ss/kpss/.
 *
 * ── 1) CLS 1,001 → 0  (performans 60 → 82) ───────────────────────────────
 * Baslangic: CLS 1,001 (Google esigi 0,1), performans 60.
 * Ikili elemeyle kaynak bulundu:
 *     script.js kapali            → CLS 0      perf 82
 *     scrollToFixed + menuler yok → CLS 0      perf 82
 *     yalniz mmenu yok            → CLS 0,002  perf 81   ← tek suclu mmenu
 *
 * `$('nav#menu').mmenu()` sayfa yuklenir yuklenmez mobil menuyu kuruyor:
 * DOM'u sarmalayip tasiyor, boylece govdenin tamami bir kez yeniden
 * yerlesiyor (olculen kayma: SECTION.cs-sayfa 0 → 400 px).
 *
 * Cozum: mmenu'yu SILMIYORUZ, GECIKTIRIYORUZ. Kurulum ilk kullanici
 * etkilesimine baglaniyor (menu dugmesine tiklama ya da ilk dokunus).
 * Boylece:
 *   · sayfa acilirken DOM'a dokunulmuyor  → kayma yok
 *   · etkilesimden sonraki 500 ms icindeki kaymalar zaten CLS'e SAYILMAZ
 *     (hadRecentInput), yani menu acilirken olusan yerlesim cezalandirilmaz
 *   · menu davranisi aynen duruyor; ilk tiklamada kurulum ~10 ms suruyor ve
 *     tiklama mmenu'ye yeniden gonderiliyor, kullanici tek dokunusla aciyor
 *
 * ── 2) scrollToFixed → CSS sticky ────────────────────────────────────────
 * `$('.navbar-scrolltofixed').scrollToFixed()` baslik cubugunu JS ile
 * `position: fixed` yapiyordu; cubuk akistan cikinca altindaki icerik bir
 * baslik boyu yukari siciyor. Ayni gorunum CSS `position: sticky` ile
 * kayma uretmeden elde ediliyor (duzeltmeler.css blok 16). Eklenti burada
 * etkisiz kilindi. `.summary` icin de cagriliyor ama sitede `.summary`
 * tasiyan sayfa yok (olculdu: 0 dosya).
 */
(function () {
  'use strict';
  var $ = window.jQuery;
  if (!$ || !$.fn) { return; }

  // 3) kaldirilan eklentiler icin bos karsilik (sim)
  //
  // scripts/js_yuku.py sayfada karsiligi olmayan tema betiklerini kaldiriyor
  // (bir icerik sayfasinda ~1,05 MB ham JS'in ~650 KB'i bos yere iniyordu).
  // Tema betigi js/script.js bazi eklentileri KORUMASIZ cagiriyor; eklenti
  // yoksa TypeError firlar ve o noktadan sonraki tema kodu hic calismaz.
  // Burada eksik adlar zararsiz bir fonksiyonla doldurulur. GERCEK eklenti
  // yuklenmisse dokunulmaz: yalniz tanimsiz olanlar doldurulur.
  // 'stellar' parallax.js'ten geliyordu; script.js:276 KORUMASIZ cagiriyor.
  var eksikler = ['stellar', 'magnificPopup', 'selectpicker', 'counterUp', 'countdown',
    'datetimepicker', 'datepicker', 'isotope', 'parallax', 'slider',
    'owlCarousel', 'slick', 'maximage', 'cycle', 'pogoSlider', 'circlechart',
    'progressBar', 'replaceProgressBar', 'snackbar', 'simplebar'];
  for (var i = 0; i < eksikler.length; i++) {
    if (!$.fn[eksikler[i]]) {
      $.fn[eksikler[i]] = function () { return this; };
    }
  }
  // wow.min.js kaldirildi; tema `new WOW().init()` diyor.
  if (!window.WOW) {
    window.WOW = function () { this.init = function () {}; };
  }

  // 2) baslik cubugu: JS fixed yerine CSS sticky
  // 22.09: jquery-scrolltofixed-min.js (28 KB) sayfalardan tamamen kaldirildi.
  // Eskiden "varsa etkisiz kil" idi; artik HIC yuklenmedigi icin kosulsuz
  // tanimlanir, yoksa script.js:17 TypeError firlatiyor.
  $.fn.scrollToFixed = function () { return this; };

  // 1) mobil menu: ilk etkilesime kadar kurulmaz
  if ($.fn.mmenu) {
    var gercekMmenu = $.fn.mmenu;
    $.fn.mmenu = function () {
      var hedef = this, argumanlar = arguments, kuruldu = false;

      function kur(olay) {
        if (kuruldu) { return; }
        kuruldu = true;
        gercekMmenu.apply(hedef, argumanlar);
        // mmenu kendi dinleyicilerini yeni kurdu; kullanicinin tiklamasi
        // ona ulasmadi -> ayni dugmeye tiklamayi bir kez daha gonderiyoruz.
        if (olay && olay.currentTarget) {
          olay.preventDefault();
          var dugme = olay.currentTarget;
          setTimeout(function () { dugme.click(); }, 0);
        }
      }

      $(document).on('click', 'a[href="#menu"]', kur);
      // Dokunmatikte ilk temasta hazirla: menuye basildiginda gecikme olmasin.
      $(document).one('touchstart', function () { kur(null); });
      return this;
    };
  }
})();
