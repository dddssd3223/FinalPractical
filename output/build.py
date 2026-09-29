"""템플릿(수학 교재 내지.dc.html)에 데이터만 넣어 자료 생성.
- output/<origin>.dc.html      문항별 자료 (변형 N-1, N-2 → 정답 및 해설)
- output/<origin>-mix.dc.html  실전 섞기 세트 (원문+변형 셔플, 풀이 시간 칸)
페이지 규칙: 번호는 순서대로 증가, 짝수 = 왼쪽 스타일(번호 왼쪽 아래), 홀수 = 오른쪽 스타일, 챕터 시작 스타일은 첫 쪽만.
스타일은 템플릿 요소를 그대로 쓰고, 짝수 일반 쪽만 템플릿의 왼쪽 푸터(p04)와 p05 본문을 조합한다."""
import json, pathlib, random, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL = next(p for p in ROOT.glob("*.dc.html") if unicodedata.normalize("NFC", p.name) == "수학 교재 내지.dc.html")
CHAPTER = ("02", "도함수의 활용")
HTML = TPL.read_text()


def section(sid):
    return re.search(r'<section class="page" id="%s".*?</section>' % sid, HTML, re.S).group(0)


def sub1(pattern, repl, s, flags=re.S):
    out, n = re.subn(pattern, repl, s, count=1, flags=flags)
    assert n == 1, pattern
    return out


FOOT_L = re.search(r'\n  <div style="position: absolute; left: 0; bottom: 14mm;.*?\n  </div>', section("p04"), re.S).group(0)
FOOT_TXT_R = re.search(r'\n  <div style="position: absolute; right: 18mm; bottom: 15mm;.*?</div>', section("p04"), re.S).group(0)
P05_FOOT_TXT = re.search(r'\n  <div style="position: absolute; left: 20mm; bottom: 15mm;.*?</div>', section("p05"), re.S).group(0)
P05_FOOT_NUM = re.search(r'\n  <div style="position: absolute; right: 0; bottom: 14mm;.*?\n  </div>', section("p05"), re.S).group(0)


def set_num(sec, num):
    return re.sub(r'(font-size: 12px; color: #ffffff;">)\d+(</div>)', r'\g<1>%02d\2' % num, sec)


def chapter_text(sec):
    return sec.replace('CHAPTER 1</span> <span style="font-weight: 300;">함수의 극한과 연속, 미분계수와 도함수',
                       f'CHAPTER {int(CHAPTER[0])}</span> <span style="font-weight: 300;">{CHAPTER[1]}')


def problem_body(sec, q, label, timer):
    sec = sub1(r'(flex: none;">)[^<]*(</div>)', r'\g<1>%s\2' % label, sec)
    src = q["source"] + ("<br>풀이 시간&nbsp;&nbsp;______ 분 ______ 초" if timer else "")
    sec = sub1(r'(letter-spacing: -0.01em; text-align: right;">)[^<]*(</span>)', lambda m: m.group(1) + src + m.group(2), sec)
    sec = re.sub(r'\s*<p style="margin: 0; font-size: 15px; line-height: 1.85;">.*?</p>', "", sec, flags=re.S)
    sec = re.sub(r'\s*<div style="align-self: center;[^>]*>\s*<span[^>]*>graph[^<]*</span>\s*</div>', "", sec)
    sec = re.sub(r'\s*<div style="display: grid; grid-template-columns: repeat\(5, 1fr\).*?</div>', "", sec, flags=re.S)
    return sub1(r'(<p style="margin: 0; font-size: 15px; line-height: 2.1;">).*?(</p>)', lambda m: m.group(1) + q["stem"] + m.group(2), sec)


def problem_page(q, label, num, first, band_title, timer):
    if first:  # 챕터 시작 스타일 (p06, 짝수 쪽 전제)
        assert num % 2 == 0
        sec = section("p06")
        sec = sec.replace('line-height: 1; color: rgb(255, 255, 255); flex: 0 0 auto;">01</span>',
                          'line-height: 1; color: rgb(255, 255, 255); flex: 0 0 auto;">%s</span>' % CHAPTER[0])
        sec = sub1(r'(letter-spacing: -0.01em;">)[^<]*(</span></div></div>)', r'\g<1>%s\2' % band_title, sec)
    else:
        sec = section("p05")
        if num % 2 == 0:  # 왼쪽 스타일: 번호 왼쪽 아래, 챕터 문구 오른쪽 아래
            sec = sec.replace(P05_FOOT_NUM, FOOT_L)
            sec = sec.replace(P05_FOOT_TXT, P05_FOOT_TXT.replace("left: 20mm", "right: 20mm"))
        sec = chapter_text(sec)
    sec = re.sub(r'id="p0\d"', f'id="q{num:02d}"', sec)
    return set_num(problem_body(sec, q, label, timer), num)


def solution_page(qs, num):
    sec = section("sol")
    blocks = re.findall(r'\n    <div style="break-inside: avoid;[^"]*">.*?\n    </div>', sec, re.S)
    head = blocks[0].split('<p style="margin: 0;">')[0]
    out = []
    for label, q in qs:
        b = head.replace(">1-1</div>", f">{label}</div>").replace('<span style="font-size: 14px;">⑤</span>', f'<span style="font-size: 14px;">{q["answer"]}</span>')
        b += "".join(f'<p style="margin: 0;">{line}</p>\n      ' for line in q["explanation"]).rstrip() + "\n    </div>"
        out.append(b)
    start = sec.index(blocks[0]); end = sec.index(blocks[-1]) + len(blocks[-1])
    sec = sec[:start] + "".join(out) + sec[end:]
    if num % 2 == 0:
        num_block = re.search(r'\n  <div style="position: absolute; right: 0; bottom: 14mm;.*?\n  </div>', sec, re.S).group(0)
        sec = sec.replace(num_block, FOOT_L).replace('left: 18mm; bottom: 15mm; font-family', 'right: 18mm; bottom: 15mm; font-family')
    return set_num(sec, num)


def wrap(pages):
    head = HTML[:HTML.index("<doc-page")]
    head = head.replace('src="./support.js"', 'src="../support.js"').replace('src="./doc-page.js"', 'src="../doc-page.js"')
    head = head.replace('url("fonts/', 'url("../')
    return head + re.search(r"<doc-page[^>]*>", HTML).group(0) + "\n\n" + "\n\n".join(pages) + "\n\n" + HTML[HTML.index("</doc-page>"):]


def build(origin, start=2):
    orig = json.loads((ROOT / f"problems/{origin}.json").read_text())
    vs = sorted((json.loads(p.read_text()) for p in ROOT.glob("variants/*.json")), key=lambda d: d["id"])
    vs = [v for v in vs if v["origin"] == origin]

    # 문항별 자료
    num, pages, sols = start, [], []
    for i, v in enumerate(vs):
        label = v["id"].split("-", 1)[1]
        pages.append(problem_page(v, label, num, i == 0, "수능 기출 변형문항", False)); sols.append((label, v)); num += 1
    if num % 2 == 0:  # 해설 표지(번호 없음)를 짝수 쪽에 두어 해설 본문이 오른쪽(홀수) 쪽에서 시작
        pages.append(section("sol-cover")); num += 1
    pages.append(solution_page(sols, num))
    (ROOT / f"output/{origin}.dc.html").write_text(wrap(pages))

    # 실전 섞기 세트: 원문 + 변형 셔플, 한 쪽에 한 문항, 풀이 시간 칸
    pool = [orig] + vs
    random.Random(origin).shuffle(pool)
    num, pages, sols = start, [], []
    for i, q in enumerate(pool):
        label = f"{i + 1:02d}"
        pages.append(problem_page(q, label, num, i == 0, "실전 섞기 세트", True)); sols.append((label, q)); num += 1
    pages.append(solution_page(sols, num))
    (ROOT / f"output/{origin}-mix.dc.html").write_text(wrap(pages))
    print("wrote", origin, "mix order:", [q["id"] for q in pool])


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "80p-1")
