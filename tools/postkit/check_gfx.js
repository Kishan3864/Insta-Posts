() => {
  // Graphics containment check: every visible element must stay inside its nearest "box"
  // (an ancestor with a background, border, shadow or clipping). Add class "free" to an
  // element (or ancestor) only for deliberate decoration that may cross a box edge.
  const out = [];
  const W = 1080, H = 1350;
  const isBox = (el) => {
    if (!el || el === document.body) return false;
    if (el.classList.contains('pg') || el.classList.contains('vis')) return false;
    const s = getComputedStyle(el);
    return s.backgroundColor !== 'rgba(0, 0, 0, 0)' || s.backgroundImage !== 'none' ||
      parseFloat(s.borderTopWidth) > 0 || s.boxShadow !== 'none' || s.overflow !== 'visible';
  };
  const name = (el) => (el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ')[0] : '') + (el.textContent ? ' "' + el.textContent.trim().slice(0, 18) + '"' : ''));
  document.querySelectorAll('.pg *').forEach((el) => {
    if (el.closest('.free') || el.closest('svg') && el.tagName.toLowerCase() !== 'svg') return;
    const r = el.getBoundingClientRect();
    if (r.width < 2 || r.height < 2) return;
    const s = getComputedStyle(el);
    if (s.visibility === 'hidden' || s.display === 'none' || parseFloat(s.opacity) === 0) return;
    if (r.left < 24 || r.right > W - 24 || r.top < 12 || r.bottom > H - 12) out.push('EDGE ' + name(el));
    let p = el.parentElement;
    while (p && p !== document.body && !isBox(p)) p = p.parentElement;
    if (!p || p === document.body || p.classList.contains('pg')) return;
    const pr = p.getBoundingClientRect();
    const tol = 2;
    if (r.left < pr.left - tol || r.right > pr.right + tol || r.top < pr.top - tol || r.bottom > pr.bottom + tol)
      out.push('ESCAPES ' + name(el) + ' from ' + name(p).slice(0, 40));
  });
  return [...new Set(out)].slice(0, 25);
}
