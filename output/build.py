"""템플릿(수학 교재 내지.dc.html)에 변형문항 데이터만 넣어 챕터별 자료를 만든다.
- output/변형문항.dc.html : 챕터마다 표지 → 문항(한 쪽에 한 문항) … 마지막에 해설 표지 → 정답 및 해설 → 빠른 정답 (일괄)
  문항 번호는 책 전체에서 01 부터 이어짐. drop 표시된 변형(함정 없는 쉬운 변형)은 싣지 않음
페이지 규칙: 쪽 번호는 책 전체에서 이어지고, 짝수 = 왼쪽 스타일(번호 왼쪽 아래), 홀수 = 오른쪽 스타일(번호 오른쪽 아래),
챕터 시작 스타일(p04 머리띠)은 챕터의 첫 문항 쪽에만 쓴다. 조건 상자·<보기>·선지는 템플릿 색(#e7c3ce 테두리 등)과 글꼴을 그대로 쓴다.
해설 쪽은 블록 높이를 브라우저에서 잰 뒤(measure.js) 두 단에 차례로 채워 나눈다."""
import html, json, pathlib, re, subprocess, sys, unicodedata
from sympy import sympify, latex, nsimplify
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from figs import FIGS
from gichul import G as GICHUL
import shutil

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
TPL = next(p for p in ROOT.glob("*.dc.html") if unicodedata.normalize("NFC", p.name) == "수학 교재 내지.dc.html")
HTML = TPL.read_text()
CHAPTERS = {1: ("01", "함수의 극한", "함수의<br>극한"), 2: ("02", "함수의 연속", "함수의<br>연속"),
            3: ("03", "미분계수와 도함수", "미분계수와<br>도함수"), 4: ("04", "도함수의 활용", "도함수의<br>활용")}
CIRC = "①②③④⑤"
COL_H = 860          # 해설 단 높이(px): 1123 − top 165 − bottom 26mm(98)
SAFETY = 0.95        # 글꼴 차이 여유


def section(sid):
    return re.search(r'<section class="page" id="%s".*?</section>' % sid, HTML, re.S).group(0)


def sub1(pattern, repl, s, flags=re.S):
    out, n = re.subn(pattern, repl, s, count=1, flags=flags)
    assert n == 1, pattern
    return out


P04, P05, SOL, SOLCOVER, QUICK, COVER = (section(s) for s in ("p04", "p05", "sol", "sol-cover", "quick", "ch01-cover"))
FOOT_L = re.search(r'\n  <div style="position: absolute; left: 0; bottom: 14mm;.*?\n  </div>', P04, re.S).group(0)
P04_TXT_R = re.search(r'\n  <div style="position: absolute; right: 18mm; bottom: 15mm;.*?</div>', P04, re.S).group(0)
P05_TXT = re.search(r'\n  <div style="position: absolute; left: 20mm; bottom: 15mm;.*?</div>', P05, re.S).group(0)
P05_NUM = re.search(r'\n  <div style="position: absolute; right: 0; bottom: 14mm;.*?\n  </div>', P05, re.S).group(0)


def set_num(sec, num):
    return re.sub(r'(font-size: 12px; color: #ffffff;">)\d+(</div>)', r'\g<1>%02d\2' % num, sec)


def chapter_text(sec, ch):
    no, title, _ = CHAPTERS[ch]
    return sec.replace('CHAPTER 1</span> <span style="font-weight: 300;">함수의 극한과 연속, 미분계수와 도함수',
                       f'CHAPTER {int(no)}</span> <span style="font-weight: 300;">{title}')


# ── 값 표기 ──
def esc(s):
    """데이터 문자열의 < > & 를 이스케이프 (수식 속 a<b 가 태그로 읽히지 않도록; KaTeX 는 텍스트로 읽음)"""
    return html.escape(s, quote=False)


def is_bogi(s):
    return any("ㄱ" <= ch <= "ㆎ" for ch in s)


def tex(s):
    if is_bogi(s):
        return ", ".join(p.strip() for p in s.split(","))
    return "$" + latex(nsimplify(sympify(s))) + "$"


def answer_text(q):
    if q.get("answer_display"):
        return q["answer_display"]
    if q["type"] == "객관식":
        return CIRC[q["choices"].index(q["answer"])]
    return tex(q["answer"])


# ── 문항 쪽 ──
BOX = '<div style="border: 1px solid #e7c3ce; padding: 4mm 6mm; font-size: 14px; line-height: 2.0;">{}</div>'
BOGI = ('<div style="position: relative; border: 1px solid #e7c3ce; padding: 6mm 6mm 4mm; font-size: 14px; line-height: 2.0;">'
        '<span style="position: absolute; top: -2.2mm; left: 50%; transform: translateX(-50%); background: #ffffff; padding: 0 3mm; '
        "font-family: 'Aggro', sans-serif; font-weight: 300; font-size: 12px; color: #d2436a; letter-spacing: 0.2em;\">&lt;보기&gt;</span>{}</div>")
CHOICES = '<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 4mm; font-size: 14px;">\n      {}\n    </div>'


def body_html(q):
    parts = [f'<p style="margin: 0; font-size: 14px; line-height: 2.1;">{esc(q["stem"])}</p>']
    if q.get("fig"):  # 기출: 원본에서 잘라 낸 그림
        parts.append(f'<div style="align-self: center;"><img src="figs/{q["fig"]}.png" style="max-width: 82mm; max-height: 62mm;"></div>')
    elif q["id"] in FIGS:  # 그림 (도형·그래프 문항)
        parts.append('<div style="align-self: center;">' + FIGS[q["id"]]() + "</div>")
    if q.get("box"):
        parts.append(BOX.format("".join(f'<p style="margin: 0;">{esc(l)}</p>' for l in q["box"])))
    if q.get("bogi"):
        parts.append(BOGI.format("".join(f'<p style="margin: 0;">{esc(l)}</p>' for l in q["bogi"])))
    if q["type"] == "객관식":
        parts.append(CHOICES.format("".join(f"<span>{CIRC[i]} {tex(c)}</span>" for i, c in enumerate(q["choices"]))))
    return "\n    ".join(parts)


def fill_problem(sec, q, label):
    sec = sub1(r'(flex: none;">)[^<]*(</div>)', r'\g<1>%s\2' % label, sec)
    sec = sub1(r'(letter-spacing: -0.01em; text-align: right;">)[^<]*(</span>)', lambda m: m.group(1) + esc(q["source"]) + m.group(2), sec)
    # 머리줄(번호·출처) 다음부터 본문 영역 끝까지를 새 본문으로 교체
    head_end = sec.index("</span>\n    </div>", sec.index("text-align: right;")) + len("</span>\n    </div>")
    body_end = sec.index("\n  </div>\n", head_end)
    return sec[:head_end] + "\n    " + body_html(q) + sec[body_end:]


HEAD_R = "display: flex; align-items: center; justify-content: flex-end; padding-right: 18mm; box-sizing: border-box;"
HEAD_L = "display: flex; align-items: center; justify-content: flex-start; padding-left: 18mm; box-sizing: border-box;"


def mirror_head(sec, num):
    """머리띠 문구 위치는 템플릿 그대로 (좌우 반전 안 함)"""
    return sec


def problem_page(q, label, num, first, ch):
    if first:  # 챕터 머리띠 스타일 (p04) — 챕터 첫 쪽부터 한 쪽씩 걸러
        sec = P04
        sec = sec.replace('flex: 0 0 auto;">01</span>', 'flex: 0 0 auto;">%s</span>' % CHAPTERS[ch][0])
        sec = sub1(r'(letter-spacing: -0.01em;">)[^<]*(</span></div></div>)', r'\g<1>%s\2' % CHAPTERS[ch][1], sec)
        sec = sec.replace("height: 451px", "")  # 본문 높이 고정 해제 (긴 문항)
        if num % 2 == 1:  # 홀수 쪽: 오른쪽 스타일 꼬리말
            sec = sec.replace(FOOT_L, P05_NUM).replace(P04_TXT_R, P05_TXT)
            sec = chapter_text(sec, ch)
    else:
        sec = P05
        if num % 2 == 0:  # 왼쪽 스타일: 번호 왼쪽 아래, 챕터 문구 오른쪽 아래
            sec = sec.replace(P05_NUM, FOOT_L).replace(P05_TXT, P05_TXT.replace("left: 20mm", "right: 20mm"))
        sec = chapter_text(sec, ch)
        sec = mirror_head(sec, num)
    sec = re.sub(r'id="p0\d"', f'id="q{num:03d}"', sec, count=1)
    # 본문 오른쪽 끝을 머리띠 문구 오른쪽 끝선(챕터 머리띠 22mm, 일반 18mm)에 맞춤
    sec = sec.replace("width: 671px", "right: %dmm" % (22 if first else 18))
    return set_num(fill_problem(sec, q, label), num)


# ── 해설 ──
SOL_BLOCKS = re.findall(r'\n    <div style="break-inside: avoid;[^"]*">.*?\n    </div>', SOL, re.S)
SOL_HEAD = SOL_BLOCKS[0].split('<p style="margin: 0;">')[0]


def sol_block(label, q):
    b = SOL_HEAD.replace(">1-1</div>", f">{label}</div>").replace('<span style="font-size: 14px;">⑤</span>',
                                                                   f'<span style="font-size: 14px;">{answer_text(q)}</span>')
    return b + "".join(f'<p style="margin: 0;">{esc(l)}</p>\n      ' for l in q["explanation"]).rstrip() + "\n    </div>"


def solution_page(blocks, num):
    sec = SOL
    start = sec.index(SOL_BLOCKS[0]); end = sec.index(SOL_BLOCKS[-1]) + len(SOL_BLOCKS[-1])
    sec = sec[:start] + "".join(blocks) + sec[end:]
    sec = sec.replace('<div style="position: absolute; left: 18mm; right: 18mm; top: 165px; bottom: 26mm; column-count: 2;',
                      '<div style="position: absolute; left: 18mm; right: 18mm; top: 165px; bottom: 26mm; column-count: 2; column-fill: auto;')
    if num % 2 == 0:
        num_block = re.search(r'\n  <div style="position: absolute; right: 0; bottom: 14mm;.*?\n  </div>', sec, re.S).group(0)
        sec = sec.replace(num_block, FOOT_L).replace("left: 18mm; bottom: 15mm; font-family", "right: 18mm; bottom: 15mm; font-family")
    sec = sec.replace("column-gap: 12mm; font-size: 13px;", "column-gap: 12mm; font-size: 12px;")
    sec = mirror_head(sec, num)
    sec = sec.replace('id="sol"', f'id="s{num:03d}"')
    return set_num(sec, num)


def paginate(heights):
    """블록 높이 목록 → 쪽마다 블록 인덱스 목록 (왼쪽 단 → 오른쪽 단 순서로 채움)"""
    cap = COL_H*SAFETY
    pages, cur, col, used = [], [], 0, 0
    for i, h in enumerate(heights):
        if used + h > cap and used > 0:
            col += 1; used = 0
            if col == 2:
                pages.append(cur); cur, col = [], 0
        cur.append(i); used += h
    if cur:
        pages.append(cur)
    return pages


# ── 표지·빠른 정답 ──
def cover(ch):
    no, _, big = CHAPTERS[ch]
    sec = COVER.replace('line-height: 0.9;">01</span>', f'line-height: 0.9;">{no}</span>')
    sec = sub1(r'(letter-spacing: -0.02em;">)강남3구<br>부교재 <br>연계문항<br><br>(</div>)', r'\g<1>%s\2' % big, sec)
    return sec.replace('id="ch01-cover"', f'id="cover{no}"')


QROW = ('        <span style="font-weight: 700; color: #d2436a;">{}</span><span style="font-family: \'Noto Serif KR\', serif;">{}</span>'
        '<span style="font-weight: 700; color: #d2436a;">{}</span><span style="font-family: \'Noto Serif KR\', serif;">{}</span>')


def quick(chapter_rows):
    """chapter_rows: [(ch, [(l1, a1, l2, a2), ...]), ...] → 빠른 정답 한 쪽 (왼쪽 단부터 채우고 넘치면 오른쪽 단)"""
    grid = re.search(r'<div style="display: grid; grid-template-columns: 11mm 16mm 11mm 16mm;[^"]*">', QUICK).group(0)
    head = QUICK[:QUICK.index('<div style="position: absolute; left: 16mm; right: 16mm; top: 46mm;')]
    chip0 = re.search(r'<div style="background: #d2436a; border-radius: 5mm;[^>]*>Chapter 01 <span[^>]*>[^<]*</span></div>', QUICK).group(0)
    CAP = 30  # 한 단에 들어가는 줄 수 (칩 1개 = 2줄)
    cols, cur, used = [], [], 0
    for ch, rows in chapter_rows:
        no, title, _ = CHAPTERS[ch]
        chip = chip0.replace("Chapter 01", f"Chapter {no}").replace("함수의 극한과 연속, 미분계수와 도함수", title)
        i = 0
        while i < len(rows):
            if used + 3 > CAP:
                cols.append(cur); cur, used = [], 0
            take = min(len(rows) - i, CAP - used - (2 if i == 0 else 0))
            if i == 0:
                cur.append(chip); used += 2
            cur.append(grid + "\n" + "\n".join(QROW.format(*r) for r in rows[i:i + take]) + "\n      </div>")
            used += take; i += take
    cols.append(cur)
    cols += [[]]*(len(cols) % 2)
    pages = []
    for i in range(0, len(cols), 2):  # 두 단씩 한 쪽
        body = ('<div style="position: absolute; left: 16mm; right: 16mm; top: 46mm; display: grid; grid-template-columns: 1fr 1fr; gap: 10mm;">\n'
                + "\n".join('    <div style="display: flex; flex-direction: column; gap: 5mm;">\n      ' + "\n      ".join(c) + "\n    </div>" for c in cols[i:i + 2])
                + "\n  </div>\n</section>")
        pages.append(head.replace('id="quick"', f'id="quick{i // 2 + 1}"') + body)
    return pages


CONTENTS = section("contents")
CROW = re.findall(r'\n    <div style="border-top: 1px solid #eeb5c8;.*?\n    </div>', CONTENTS, re.S)


def contents(rows):
    """rows: [(왼쪽 칩 문구, 제목, 쪽)]"""
    tpl = CROW[0]
    out = []
    for chip, title, page in rows:
        r = tpl.replace("Chapter 01", chip).replace("함수의 극한과 연속, 미분계수와 도함수", title).replace(">03</span>", f">{page:02d}</span>")
        if not chip:
            r = r.replace('<span style="font-weight: 700; font-size: 19px; color: #d2436a;"></span>', "<span></span>")
        out.append(r)
    start = CONTENTS.index(CROW[0]); end = CONTENTS.index(CROW[-1]) + len(CROW[-1])
    sec = CONTENTS[:start] + "".join(out) + CONTENTS[end:]
    return sec.replace("PRACTICAL SERIES", "PRACTICAL ESSENCE").replace('color: #201a1c;">수학Ⅱ</span>', 'color: #201a1c;">미적분1</span>')


def brand(page_html):
    """머리말·꼬리말 문구: 프랙티컬 수학Ⅱ / 미적분I → 프랙티컬 ESSENCE 미적분1"""
    for old in ("수학Ⅱ", "미적분I"):
        page_html = page_html.replace(f'프랙티컬</span> <span style="font-weight: 700;">{old}', '프랙티컬 ESSENCE</span> <span style="font-weight: 700;">미적분1')
    return page_html


def wrap(pages):
    head = HTML[:HTML.index("<doc-page")]
    head = head.replace('src="./support.js"', 'src="../support.js"').replace('src="./doc-page.js"', 'src="../doc-page.js"')
    head = head.replace('url("fonts/', 'url("../')
    return head + re.search(r"<doc-page[^>]*>", HTML).group(0) + "\n\n" + "\n\n".join(pages) + "\n\n" + HTML[HTML.index("</doc-page>"):]


def load():
    """변형 + 학교 기출. 기출은 짝 원문의 마지막 번호 뒤에 n-1, n-2 …, 짝이 없으면 단원 맨 뒤에 새 번호."""
    vs = [json.loads(p.read_text()) for p in (ROOT / "variants").glob("*.json")]
    vs = [v for v in vs if not v.get("drop")]
    key = lambda oid: (int(oid.split("p-")[0]), int(oid.split("p-")[1]))
    by_ch = {}
    for v in vs:
        by_ch.setdefault(v["chapter"], {}).setdefault(v["origin"], []).append(v)
    for g in GICHUL:
        by_ch.setdefault(g["chapter"], {})
    out, n = {}, 0
    for ch, d in sorted(by_ch.items()):
        items = []
        for oid in sorted(d, key=key):
            for v in sorted(d[oid], key=lambda v: v["id"]):
                n += 1
                items.append((f"{n:02d}", v))
            base = n
            for j, g in enumerate([g for g in GICHUL if g["attach"] == oid], 1):
                items.append((f"{base:02d}-{j}", g))
        for g in [g for g in GICHUL if g["chapter"] == ch and g["attach"] is None]:
            n += 1
            items.append((f"{n:02d}", g))
        out[ch] = items
    attached = {g["attach"] for g in GICHUL if g["attach"]}
    have = {v["origin"] for v in vs}
    assert attached <= have, attached - have
    return out


def memo():
    """빈 쪽 (MEMO) — 챕터 표지를 홀수 쪽에 맞출 때"""
    head = QUICK[:QUICK.index('<div style="position: absolute; left: 16mm; right: 16mm; top: 46mm;')].replace("빠른 정답", "MEMO")
    lines = "".join(f'<div style="height: 1px; background: #f3c6d5; margin-top: 13mm;"></div>' for _ in range(16))
    return head.replace('id="quick"', 'id="memo"') + f'<div style="position: absolute; left: 18mm; right: 18mm; top: 46mm;">{lines}</div>\n</section>'


def measure(all_blocks):
    """해설 블록 높이를 브라우저에서 측정 (단 폭·글꼴 설정은 해설 쪽과 동일)"""
    style = re.search(r"<style>.*?</style>", HTML, re.S).group(0).replace('url("fonts/', 'url("../')
    page = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">' + style +
            '</head><body><div id="col" style="width: 306px; font-family: \'Noto Serif KR\', serif; color: #1e1a1b; font-size: 12px; line-height: 2.0;">'
            + "".join(all_blocks) + "</div></body></html>")
    mp = OUT / "_measure.html"
    mp.write_text(page)
    res = subprocess.run(["node", str(OUT / "measure.js"), str(mp)], capture_output=True, text=True, timeout=300)
    if res.returncode:
        raise SystemExit(res.stderr[-2000:])
    mp.unlink()
    hs = json.loads(res.stdout.strip().splitlines()[-1])
    assert len(hs) == len(all_blocks), (len(hs), len(all_blocks), res.stderr[-500:])
    return hs


def main():
    data = load()
    allitems = [(ch, l, q) for ch, items in data.items() for l, q in items]
    blocks = [sol_block(l, q) for _, l, q in allitems]
    hs = measure(blocks)
    pages, num = [None, memo()], 2  # 1쪽 목차(나중에 채움), 2쪽 MEMO, 3쪽 챕터 표지, 4쪽 첫 문항 (템플릿 쪽 번호와 같음)
    toc = []
    for ch, items in data.items():
        num += 1
        pages.append(cover(ch))
        toc.append((f"Chapter {CHAPTERS[ch][0]}", CHAPTERS[ch][1], num))
        for i, (label, q) in enumerate(items):
            num += 1
            pages.append(problem_page(q, label, num, i % 2 == 0, ch))  # 챕터 머리띠 쪽과 일반 쪽을 번갈아
        print(f"ch{ch}: {len(items)}문항 (기출 {sum(1 for _, q in items if q['id'].startswith('G-'))})")
    num += 1
    pages.append(SOLCOVER)
    toc.append(("", "정답 및 해설", num))
    for idx in paginate(hs):
        num += 1
        pages.append(solution_page([blocks[i] for i in idx], num))
    rows = []
    for ch, items in data.items():
        flat = [(l, tex(q["answer"]) if q.get("answer_display") else answer_text(q)) for l, q in items]  # 서술형은 최종 답만
        rs = []
        for j in range(0, len(flat), 2):
            a = flat[j]; b = flat[j + 1] if j + 1 < len(flat) else ("", "")
            rs.append((a[0], a[1], b[0], b[1]))
        rows.append((ch, rs))
    for qp in quick(rows):
        num += 1
        pages.append(qp)
    for old in OUT.glob("ch*.dc.html"):
        old.unlink()
    pages[0] = contents(toc)
    (OUT / "변형문항.dc.html").write_text(brand(wrap(pages)))
    figs = OUT / "figs"
    figs.mkdir(exist_ok=True)
    print(f"총 {len(allitems)}문항, {len(pages)}쪽 (끝 쪽 {num})")


if __name__ == "__main__":
    main()
