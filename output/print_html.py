"""ch*.dc.html → 인쇄용 HTML (doc-page 없이 A4 쪽을 차례로 배치, KaTeX 자동 렌더) — PDF 출력용"""
import pathlib, re, sys
OUT = pathlib.Path(__file__).resolve().parent
srcs = sys.argv[2:] or sorted(str(p) for p in OUT.glob("ch*.dc.html"))
style = None
secs = []
for s in srcs:
    h = pathlib.Path(s).read_text()
    style = style or re.search(r"<style>.*?</style>", h, re.S).group(0)
    secs += re.findall(r'<section class="page".*?</section>', h, re.S)
page = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@400;500;600&amp;family=Noto+Sans+KR:wght@400;500;700&amp;display=swap">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
{style}
<style>@page {{ size: A4; margin: 0; }} section.page {{ width: 210mm; height: 297mm; box-sizing: border-box; page-break-after: always; break-after: page; }}</style>
</head><body>
{chr(10).join(secs)}
<script>window.addEventListener('load', () => renderMathInElement(document.body, {{delimiters: [{{left: '$', right: '$', display: false}}], throwOnError: false}}));</script>
</body></html>"""
pathlib.Path(sys.argv[1]).write_text(page)
print(len(secs), "쪽")
