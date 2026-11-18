// vercel.json kaynak kaliplarini (path-to-regexp alt kumesi) JS regex'e cevirir.
// Desteklenen: :ad*  :ad(regex)  :ad  (regex)  \.  ve duz metin. Baska bir sey
// gorulurse hata firlatir (derleme durur, sessiz yanlis eslesme yok).
export function compile(src) {
  let re = '^', i = 0;
  while (i < src.length) {
    const rest = src.slice(i);
    let m;
    if ((m = rest.match(/^:([A-Za-z_]\w*)\*/))) { re += `(?<${m[1]}>.*)`; i += m[0].length; continue; }
    if ((m = rest.match(/^:([A-Za-z_]\w*)\(([^()]*)\)/))) { re += `(?<${m[1]}>${m[2]})`; i += m[0].length; continue; }
    if ((m = rest.match(/^:([A-Za-z_]\w*)/))) { re += `(?<${m[1]}>[^/]+)`; i += m[0].length; continue; }
    if ((m = rest.match(/^\(([^()]*)\)/))) { re += `(?:${m[1]})`; i += m[0].length; continue; }
    if (rest.startsWith('\\.')) { re += '\\.'; i += 2; continue; }
    const c = src[i];
    if (/[*+?^${}|[\]\\()]/.test(c)) throw new Error('cevrilemeyen kalip: ' + src);
    re += c === '.' ? '\\.' : c;
    i++;
  }
  return new RegExp(re + '$');
}

export function fill(dest, groups) {
  // "https://" icindeki ":" bir ad ile devam etmedigi icin eslesmez.
  return dest.replace(/:([A-Za-z_]\w*)\*?/g, (all, name) => (groups && name in groups ? groups[name] : all));
}

export const isParam = (src) => /[:(]/.test(src);
// Vercel: permanent yoksa 307 (canlida /x.php -> 307 olculdu), true ise 308.
export const statusOf = (r) => r.statusCode || (r.permanent === true ? 308 : 307);
