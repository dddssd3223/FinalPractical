"""템플릿(수학 교재 내지.dc.html)에 변형문항 데이터만 넣어 챕터별 자료를 만든다.
- output/ch<N>.dc.html : 챕터 표지 → 문항(한 쪽에 한 문항, 번호 n-1, n-2) → 해설 표지 → 정답 및 해설 → 빠른 정답
페이지 규칙: 쪽 번호는 책 전체에서 이어지고, 짝수 = 왼쪽 스타일(번호 왼쪽 아래), 홀수 = 오른쪽 스타일(번호 오른쪽 아래),
챕터 시작 스타일(p04 머리띠)은 챕터의 첫 문항 쪽에만 쓴다. 조건 상자·<보기>·선지는 템플릿 색(#e7c3ce 테두리 등)과 글꼴을 그대로 쓴다.
해설 쪽은 블록 높이를 브라우저에서 잰 뒤(measure.js) 두 단에 차례로 채워 나눈다."""
import html, json, pathlib, re, subprocess, sys, unicodedata
from sympy import sympify, latex, nsimplify

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "output"
TPL = next(p for p in ROOT.glob("*.dc.html") if unicodedata.normalize("NFC", p.name) == "수학 교재 내지.dc.html")
HTML = TPL.read_text()
CHAPTERS = {1: ("01", "함수의 극한", "함수의<br>극한"), 2: ("02", "함수의 연속", "함수의<br>연속"),
            3: ("03", "미분계수와 도함수", "미분계수와<br>도함수"), 4: ("04", "도함수의 활용", "도함수의<br>활용")}
CIRC = "①②③④⑤"
COL_H = 860          # 해설 단 높이(px): 1123 − top 165 − bottom 26mm(98)
SAFETY = 0.97        # 글꼴 차이 여유


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
    if q["type"] == "객관식":
        return CIRC[q["choices"].index(q["answer"])]
    return tex(q["answer"])


# ── 문항 쪽 ──
BOX = '<div style="border: 1px solid #e7c3ce; padding: 4mm 6mm; font-size: 15px; line-height: 2.0;">{}</div>'
BOGI = ('<div style="position: relative; border: 1px solid #e7c3ce; padding: 6mm 6mm 4mm; font-size: 15px; line-height: 2.0;">'
        '<span style="position: absolute; top: -2.2mm; left: 50%; transform: translateX(-50%); background: #ffffff; padding: 0 3mm; '
        "font-family: 'Aggro', sans-serif; font-weight: 300; font-size: 12px; color: #d2436a; letter-spacing: 0.2em;\">&lt;보기&gt;</span>{}</div>")
CHOICES = '<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 4mm; font-size: 15px;">\n      {}\n    </div>'


def body_html(q):
    parts = [f'<p style="margin: 0; font-size: 15px; line-height: 2.1;">{esc(q["stem"])}</p>']
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


def problem_page(q, label, num, first, ch):
    if first:  # 챕터 시작 스타일 (p04)
        sec = P04
        sec = sec.replace('flex: 0 0 auto;">01</span>', 'flex: 0 0 auto;">%s</span>' % CHAPTERS[ch][0])
        sec = sub1(r'(letter-spacing: -0.01em;">)[^<]*(</span></div></div>)', r'\g<1>%s 변형문항\2' % CHAPTERS[ch][1], sec)
        sec = sec.replace("height: 451px", "")  # 본문 높이 고정 해제 (긴 문항)
        if num % 2 == 1:  # 홀수 쪽: 오른쪽 스타일 꼬리말
            sec = sec.replace(FOOT_L, P05_NUM).replace(P04_TXT_R, P05_TXT)
            sec = chapter_text(sec, ch)
    else:
        sec = P05
        if num % 2 == 0:  # 왼쪽 스타일: 번호 왼쪽 아래, 챕터 문구 오른쪽 아래
            sec = sec.replace(P05_NUM, FOOT_L).replace(P05_TXT, P05_TXT.replace("left: 20mm", "right: 20mm"))
        sec = chapter_text(sec, ch)
    sec = re.sub(r'id="p0\d"', f'id="q{num:03d}"', sec, count=1)
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
    sec = sub1(r'(letter-spacing: -0.02em;">)강남3구<br>부교재 <br>연계문항<br><br>(</div>)', r'\g<1>%s<br>변형문항\2' % big, sec)
    return sec.replace('id="ch01-cover"', f'id="cover{no}"')


QROW = ('        <span style="font-weight: 700; color: #d2436a;">{}</span><span style="font-family: \'Noto Serif KR\', serif;">{}</span>'
        '<span style="font-weight: 700; color: #d2436a;">{}</span><span style="font-family: \'Noto Serif KR\', serif;">{}</span>')


def quick(ch, rows):
    no, title, _ = CHAPTERS[ch]
    grids = re.findall(r'(<div style="display: grid; grid-template-columns: 11mm 16mm 11mm 16mm;[^"]*">)\n.*?\n      </div>', QUICK, re.S)
    g_left, g_right = grids[0], grids[-1]
    half = (len(rows) + 1)//2
    fmt = lambda rs: "\n".join(QROW.format(*r) for r in rs)
    head = QUICK[:QUICK.index('<div style="position: absolute; left: 16mm; right: 16mm; top: 46mm;')]
    chip = re.search(r'<div style="background: #d2436a; border-radius: 5mm;[^>]*>Chapter 01 <span[^>]*>[^<]*</span></div>', QUICK).group(0)
    chip = chip.replace("Chapter 01", f"Chapter {no}").replace("함수의 극한과 연속, 미분계수와 도함수", title)
    body = ('<div style="position: absolute; left: 16mm; right: 16mm; top: 46mm; display: grid; grid-template-columns: 1fr 1fr; gap: 10mm;">\n'
            '    <div style="display: flex; flex-direction: column; gap: 5mm;">\n      ' + chip + "\n      " + g_left + "\n" + fmt(rows[:half]) + "\n      </div>\n    </div>\n\n"
            '    <div style="display: flex; flex-direction: column; gap: 5mm;">\n      ' + g_right + "\n" + fmt(rows[half:]) + "\n      </div>\n    </div>\n  </div>\n</section>")
    return head.replace('id="quick"', f'id="quick{no}"') + body


def wrap(pages):
    head = HTML[:HTML.index("<doc-page")]
    head = head.replace('src="./support.js"', 'src="../support.js"').replace('src="./doc-page.js"', 'src="../doc-page.js"')
    head = head.replace('url("fonts/', 'url("../')
    return head + re.search(r"<doc-page[^>]*>", HTML).group(0) + "\n\n" + "\n\n".join(pages) + "\n\n" + HTML[HTML.index("</doc-page>"):]


def load():
    vs = [json.loads(p.read_text()) for p in (ROOT / "variants").glob("*.json")]
    key = lambda oid: (int(oid.split("p-")[0]), int(oid.split("p-")[1]))
    by_ch = {}
    for v in vs:
        by_ch.setdefault(v["chapter"], {}).setdefault(v["origin"], []).append(v)
    out = {}
    for ch, d in sorted(by_ch.items()):
        items = []
        for n, oid in enumerate(sorted(d, key=key), 1):
            for v in sorted(d[oid], key=lambda v: v["id"]):
                items.append((f"{n}-{v['id'].rsplit('-', 1)[1]}", v))
        out[ch] = items
    return out


def measure(all_blocks):
    """해설 블록 높이를 브라우저에서 측정 (단 폭·글꼴 설정은 해설 쪽과 동일)"""
    style = re.search(r"<style>.*?</style>", HTML, re.S).group(0).replace('url("fonts/', 'url("../')
    page = ('<!DOCTYPE html><html><head><meta charset="utf-8">'
            '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">' + style +
            '</head><body><div id="col" style="width: 306px; font-family: \'Noto Serif KR\', serif; color: #1e1a1b; font-size: 13px; line-height: 2.0;">'
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
    blocks = {ch: [sol_block(l, q) for l, q in items] for ch, items in data.items()}
    flat = [b for ch in sorted(blocks) for b in blocks[ch]]
    hs = measure(flat)
    k = 0
    num = 3  # 표지가 3쪽, 첫 문항이 4쪽 (템플릿과 같음)
    for ch, items in data.items():
        pages = [cover(ch)]
        for i, (label, q) in enumerate(items):
            num += 1
            pages.append(problem_page(q, label, num, i == 0, ch))
        num += 1
        pages.append(SOLCOVER.replace('id="sol-cover"', f'id="solcover{CHAPTERS[ch][0]}"'))
        chs = hs[k:k + len(items)]; k += len(items)
        for idx in paginate(chs):
            num += 1
            pages.append(solution_page([blocks[ch][i] for i in idx], num))
        rows = []
        for j in range(0, len(items), 2):
            (l1, q1), (l2, q2) = items[j], items[j + 1]
            rows.append((l1, answer_text(q1), l2, answer_text(q2)))
        num += 1
        pages.append(quick(ch, rows))
        (OUT / f"ch{ch}.dc.html").write_text(wrap(pages))
        print(f"ch{ch}: 문항 {len(items)}, 쪽 {len(pages)}, 끝 쪽 {num}")
        num += 1  # 다음 챕터 표지


if __name__ == "__main__":
    main()
