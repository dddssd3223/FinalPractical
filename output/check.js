// 렌더 점검: node check.js <html> <shot_dir> [쪽 id,...]  — 넘침·KaTeX 오류 보고, 지정한 쪽 캡처
const { chromium } = require('playwright');
const L = (process.env.LIBS || '') + '/node_modules/';
const map = [
  [/katex@[^/]+\/dist\/(.*)$/, m => L + 'katex/dist/' + m[1]],
  [/react@[^/]+\/umd\/(.*)$/, m => L + 'react/umd/' + m[1]],
  [/react-dom@[^/]+\/umd\/(.*)$/, m => L + 'react-dom/umd/' + m[1]],
];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1000, height: 1300 } });
  const errs = [];
  p.on('pageerror', e => errs.push(String(e)));
  await p.route(/^https:\/\//, async r => {
    const u = r.request().url();
    for (const [re, fn] of map) { const m = u.match(re); if (m) return r.fulfill({ path: fn(m) }); }
    return r.abort();
  });
  await p.goto('file://' + process.argv[2]);
  await p.waitForTimeout(9000);
  const info = await p.evaluate(() => {
    const secs = [...document.querySelectorAll('section.page')];
    const bad = [];
    for (const s of secs) {
      const r = s.getBoundingClientRect();
      const mm = r.height / 297;
      // 본문 영역: top 165px 에서 시작하는 절대 위치 div
      const body = [...s.children].find(c => c.style.top === '165px');
      if (body) {
        if (body.style.columnCount === '2') {
          if (body.scrollWidth > body.clientWidth + 2) bad.push([s.id, 'sol-overflow']);
        } else {
          const bb = body.getBoundingClientRect();
          if (bb.bottom > r.bottom - 26 * mm) bad.push([s.id, 'body-bottom', Math.round(bb.bottom - r.top)]);
        }
      }
      const out = [...s.querySelectorAll('*')].filter(k => { const q = k.getBoundingClientRect(); return q.width > 0 && (q.right > r.right + 1 || q.left < r.left - 1) && !k.closest('[style*="overflow: hidden"]:not(section)'); });
      if (out.length && s.id.startsWith('q')) bad.push([s.id, 'x-overflow', out.length]);
    }
    return { n: secs.length, katex: document.querySelectorAll('.katex').length, kerr: document.querySelectorAll('.katex-error').length, bad };
  });
  console.log(JSON.stringify(info), errs.slice(0, 5));
  const want = (process.argv[4] || '').split(',').filter(Boolean);
  for (const id of want) {
    const el = await p.$('section.page#' + id);
    if (el) await el.screenshot({ path: process.argv[3] + '/' + id + '.png' });
  }
  await b.close();
})();
