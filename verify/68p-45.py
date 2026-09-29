from lib import *

def box(g0, side, dsign):
    return [r"(가) $f(0)=0$, $g(0)=" + g0 + r"$",
            r"(나) 모든 " + side + r" $x$에 대하여 $f(x)" + dsign + r"0$이다.",
            r"(다) 모든 " + side + r" $t$에 대하여 점 $(t,\,f(t))$와 원점 사이의 거리는 $tg(t)$이다."]

HEAD = r"다항함수 $f(x)$와 연속함수 $g(x)$가 다음 조건을 만족시킬 때, $f'(0)$의 값은?"

ORIG = dict(
    id="68p-45", chapter=3, page=68, num=45, source="2025년 수능특강 [25009-0073]", type="객관식",
    stem=HEAD, box=box("5", "양수", ">"), choices=["2*sqrt(6)", "5", "sqrt(26)", "3*sqrt(3)", "2*sqrt(7)"], answer="2*sqrt(6)",
    general="t>0: √(t²+f²)=tg → g=√(1+(f/t)²). g 연속 → t→0+: √(1+f'(0)²)=5 → f'(0)²=24. f(0)=0, x>0 에서 f>0 → f'(0)>0 → 2√6.",
    special="① f/t → f'(0) 의 부호는 f 의 부호 ÷ t 의 부호 — 음수 쪽에서 f>0 이면 f'(0)<0.",
    perspective="거리식을 g 로 풀고 0 에서 연속.",
    table=[
        ("양수 t 쪽 (t>0, f>0 → f'(0)>0)", "음수 t 쪽 (t<0, f>0 → f'(0)<0)", "음수 쪽이면 g=−√(1+(f/t)²), g(0)=−5, f'(0)=−2√6"),
        ("g(0)=5", "—", "3 이면 f'(0)=2√2 (생존)"),
    ],
    sweep=["f'(0)²=g(0)²−1"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (t<0 에서 f/t 의 부호)",
        changed=["(나)(다) 양수 → 음수", "g(0)=5 → −5"],
        naturalness="t<0 이면 거리 tg(t) 가 양수이려면 g(t)<0 이라 g(0) 을 −5 로 함께 바꾼 것.",
        stem=HEAD, box=box("-5", "음수", ">"),
        choices=["-2*sqrt(6)", "-5", "-sqrt(26)", "5", "2*sqrt(6)"], answer="-2*sqrt(6)", trap_answer="2*sqrt(6)",
        trap_path="원문처럼 'f>0 이면 f'(0)>0' 으로 보아 2√6 (음수 쪽에서 f>0 이면 f(t)/t<0).",
        explanation=[
            r"$t<0$에서 $\sqrt{t^2+\{f(t)\}^2}=tg(t)$이므로 $g(t)=-\sqrt{1+\left\{\frac{f(t)}t\right\}^2}$이다.",
            r"$g$가 연속이므로 $t\to0-$에서 $-\sqrt{1+\{f'(0)\}^2}=-5$, $\{f'(0)\}^2=24$이다.",
            r"함정: $t<0$에서 $f(t)>0$이므로 $\frac{f(t)}t<0$, 즉 $f'(0)\le0$이다.",
            r"따라서 $f'(0)=-2\sqrt6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (g(0)=5 → 3)",
        changed=["g(0)=5 → 3"], naturalness="",
        stem=HEAD, box=box("3", "양수", ">"), choices=["2", "2*sqrt(2)", "3", "2*sqrt(3)", "4"], answer="2*sqrt(2)", trap_answer=None, trap_path=None,
        explanation=[
            r"$t>0$에서 $g(t)=\sqrt{1+\left\{\frac{f(t)}t\right\}^2}$이다.",
            r"$t\to0+$에서 $\sqrt{1+\{f'(0)\}^2}=3$이므로 $\{f'(0)\}^2=8$이다.",
            r"$x>0$에서 $f>0$이므로 $f'(0)>0$, $f'(0)=2\sqrt2$이다.",
        ],
    ),
]


def fp0(g0, side):
    """f=c1 x + c2 x² (f(0)=0; 극한은 c1 만 관여), side=+1 양수 쪽 / −1 음수 쪽"""
    c1, c2 = symbols('c1 c2', real=True)
    t = Symbol('t', real=True)
    f = c1*t + c2*t**2
    dirn = '+' if side > 0 else '-'
    g2 = limit((t**2 + f**2)/t**2, t, 0, dirn)  # g(t)² 의 극한 (g 부호는 tg>0 에서 side 부호)
    out = []
    for v in solve(g2 - g0**2, c1):
        # g(0) 부호: g = dist/t 이므로 side 쪽 부호
        if sign(g0) != side:
            continue
        # (나): side 쪽 작은 t 에서 f>0
        ft = f.subs({c1: v, c2: 0})
        if ft.subs(t, side*Rational(1, 1000)) > 0:
            out.append(v)
    return out


def verify(c):
    v = fp0(5, 1)
    c.check("원문: 유일", len(v) == 1)
    c.ans('orig', v[0])
    v = fp0(-5, -1)
    c.check("1: 유일", len(v) == 1)
    c.ans(1, v[0])
    c.trap(1, fp0(5, 1)[0])
    v = fp0(3, 1)
    c.check("2: 유일", len(v) == 1)
    c.ans(2, v[0])


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '부호만 바뀌는 쉬운 변형'
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
