"""템플릿(수학 교재 내지.dc.html)에 variants/*.json 데이터만 넣어 output/<origin>.dc.html 생성.
디자인(스타일)은 건드리지 않고 텍스트·자산 경로만 치환한다."""
import glob, json, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL = next(p for p in ROOT.glob("*.dc.html") if unicodedata.normalize("NFC", p.name) == "수학 교재 내지.dc.html")
CHAPTER = ("02", "도함수의 활용")
BAND_TITLE = "수능 기출 변형문항"


def section(html, sid):
    m = re.search(r'<section class="page" id="%s".*?</section>' % sid, html, re.S)
    return m.group(0)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def band(sec):
    sec = sec.replace('line-height: 1; color: rgb(255, 255, 255); flex: 0 0 auto;">01</span>',
                      'line-height: 1; color: rgb(255, 255, 255); flex: 0 0 auto;">%s</span>' % CHAPTER[0])
    return re.sub(r'(letter-spacing: -0.01em;">)[^<]*(</span></div></div>)', r'\g<1>%s\2' % BAND_TITLE, sec, count=1)


def fill_problem(sec, v, old_id, old_src):
    sec = sec.replace(f">{old_id}</div>", f">{v['id'].split('-', 1)[1]}</div>")
    sec = sec.replace(old_src, esc(v["source"]))
    # 그림 자리·첫 문장·선지 제거 (주관식), 발문 교체
    sec = re.sub(r'\s*<p style="margin: 0; font-size: 15px; line-height: 1.85;">.*?</p>', "", sec, flags=re.S)
    sec = re.sub(r'\s*<div style="align-self: center;[^>]*>\s*<span[^>]*>graph[^<]*</span>\s*</div>', "", sec)
    sec = re.sub(r'\s*<div style="display: grid; grid-template-columns: repeat\(5, 1fr\).*?</div>', "", sec, flags=re.S)
    sec = re.sub(r'(<p style="margin: 0; font-size: 15px; line-height: 2.1;">).*?(</p>)',
                 lambda m: m.group(1) + v["stem"] + m.group(2), sec, flags=re.S)
    sec = sec.replace("CHAPTER 1</span> <span style=\"font-weight: 300;\">함수의 극한과 연속, 미분계수와 도함수",
                      f"CHAPTER {int(CHAPTER[0])}</span> <span style=\"font-weight: 300;\">{CHAPTER[1]}")
    return sec


def fill_solutions(sec, vs):
    blocks = re.findall(r'\n    <div style="break-inside: avoid;[^"]*">.*?\n    </div>', sec, re.S)
    proto = blocks[0]
    head = proto.split('<p style="margin: 0;">')[0]
    out = []
    for v in vs:
        b = head.replace(">1-1</div>", f">{v['id'].split('-', 1)[1]}</div>")
        b = b.replace('<span style="font-size: 14px;">⑤</span>', f'<span style="font-size: 14px;">{v["answer"]}</span>')
        b += "".join(f'<p style="margin: 0;">{line}</p>\n      ' for line in v["explanation"]).rstrip() + "\n    </div>"
        out.append(b)
    start = sec.index(blocks[0]); end = sec.index(blocks[-1]) + len(blocks[-1])
    return sec[:start] + "".join(out) + sec[end:]


def build(origin):
    html = TPL.read_text()
    vs = sorted((json.loads(pathlib.Path(p).read_text()) for p in glob.glob(str(ROOT / "variants/*.json"))), key=lambda d: d["id"])
    vs = [v for v in vs if v["origin"] == origin]
    head = html[:html.index("<doc-page")]
    head = head.replace('src="./support.js"', 'src="../support.js"').replace('src="./doc-page.js"', 'src="../doc-page.js"')
    head = head.replace('url("fonts/', 'url("../')
    doc_open = re.search(r"<doc-page[^>]*>", html).group(0)
    tail = html[html.index("</doc-page>"):]
    pages = []
    for i, v in enumerate(vs):
        if i == 0:
            pages.append(band(fill_problem(section(html, "p06"), v, "2-1", "2025년 단대부고 2학기 중간고사 19번")))
        else:
            pages.append(fill_problem(section(html, "p05"), v, "1-2", "2026년 세화고등학교 1학기 기말고사 27번"))
    pages.append(section(html, "sol-cover"))
    pages.append(fill_solutions(section(html, "sol"), vs))
    out = ROOT / f"output/{origin}.dc.html"
    out.write_text(head + doc_open + "\n\n" + "\n\n".join(pages) + "\n\n" + tail)
    print("wrote", out)


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "80p-1")
