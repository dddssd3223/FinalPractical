// PDF 출력: node pdf.js <html> <out.pdf>
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
  await p.waitForTimeout(9000);
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close();
})();
