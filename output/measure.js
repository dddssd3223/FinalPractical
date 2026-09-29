// 해설 블록 높이 측정: node measure.js <html>  (CDN 은 LIBS 폴더의 npm 패키지로 대체)
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
  await p.route(/^https:\/\//, async r => {
    const u = r.request().url();
    for (const [re, fn] of map) { const m = u.match(re); if (m) return r.fulfill({ path: fn(m) }); }
    return r.abort();
  });
  await p.goto('file://' + process.argv[2]);
  await p.waitForTimeout(3000);
  if (!(await p.evaluate(() => !!window.renderMathInElement))) {
    await p.addScriptTag({ path: L + 'katex/dist/katex.min.js' });
    await p.addScriptTag({ path: L + 'katex/dist/contrib/auto-render.min.js' });
  }
  await p.evaluate(() => window.renderMathInElement(document.getElementById('col'), { delimiters: [{ left: '$', right: '$', display: false }], throwOnError: false }));
  await p.waitForTimeout(1500);
  const hs = await p.evaluate(() => [...document.querySelectorAll('#col > div')].map(d => {
    const cs = getComputedStyle(d); return d.getBoundingClientRect().height + parseFloat(cs.marginBottom || 0); }));
  console.log(JSON.stringify(hs));
  await b.close();
})();
