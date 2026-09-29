from lib import *

def stem(P):
    return (r"두 함수 $f(x)=x^3-3x^2+2x+a$, $g(x)=x^2+bx+c$가 다음 조건을 만족시킬 때, $|abc|$의 값은? (단, $a$, $b$, $c$는 상수이다.)")

def box(P):
    return [r"(가) 두 곡선 $y=f(x)$, $y=g(x)$가 점 $\mathrm A" + P + r"$에서 만난다.",
            r"(나) 곡선 $y=f(x)$ 위의 점 $\mathrm A$에서의 접선과 곡선 $y=g(x)$ 위의 점 $\mathrm A$에서의 접선이 서로 수직이다."]

ORIG = dict(
    id="81p-8", chapter=4, page=81, num=8, source="2024년 수능완성 [24054-0116]", type="객관식",
    stem=stem("(1,2)"), box=box("(1,\\,2)"), choices=["5/2", "3", "7/2", "4", "9/2"], answer="4",
    general="f(1)=a=2. f'(1)=−1 → g'(1)=1 (곱 −1) → b=−1. g(1)=c=2. |abc|=4.",
    special="① f'(1)=−1 이라 수직 기울기 −1/m 과 −m 이 같음 — 다른 점에서는 달라짐.",
    perspective="수직: 기울기 곱 −1.",
    table=[
        ("접점 x=1 (m=−1)", "m≠±1 인 점", "A(2,2) 면 m=2 → g'(2)=−1/2 → 63"),
        ("A 의 y좌표 2", "—", "3 이면 a=c=3 → 9 (생존)"),
    ],
    sweep=["g'(p)=−1/f'(p)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (m=−1 에서만 −1/m=−m)",
        changed=["A(1,2) → A(2,2)"], naturalness="",
        stem=stem("(2,2)"), box=box("(2,\\,2)"), choices=["45", "54", "63", "120", "126"], answer="63", trap_answer="120",
        trap_path="원문에서처럼 g' 을 −f' 로 잡아 g'(2)=−2 → b=−6, c=10 → 120 (수직이면 −1/2).",
        explanation=[
            r"$f(2)=8-12+4+a=2$에서 $a=2$이다.",
            r"$f'(2)=12-12+2=2$이므로 수직인 기울기는 $-\frac12$이다. 함정: $-2$가 아니다.",
            r"$g'(2)=4+b=-\frac12$에서 $b=-\frac92$, $g(2)=4-9+c=2$에서 $c=7$이다.",
            r"$|abc|=2\times\frac92\times7=63$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (A(1,2) → A(1,3))",
        changed=["A(1,2) → A(1,3)"], naturalness="",
        stem=stem("(1,3)"), box=box("(1,\\,3)"), choices=["3", "6", "9", "12", "15"], answer="9", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(1)=a=3$이고 $f'(1)=-1$이므로 $g'(1)=2+b=1$, $b=-1$이다.",
            r"$g(1)=1-1+c=3$에서 $c=3$이다.",
            r"$|abc|=9$이다.",
        ],
    ),
]


def solve_abc(px, py, perp=True):
    a, b, c = symbols('a b c')
    f = x**3 - 3*x**2 + 2*x + a
    g = x**2 + b*x + c
    m1 = diff(f, x).subs(x, px)
    rel = m1*diff(g, x).subs(x, px) + 1 if perp else diff(g, x).subs(x, px) + m1
    s = solve([f.subs(x, px) - py, g.subs(x, px) - py, rel], [a, b, c], dict=True)
    assert len(s) == 1
    return Abs(s[0][a]*s[0][b]*s[0][c])


def verify(c):
    c.ans('orig', solve_abc(1, 2))
    c.ans(1, solve_abc(2, 2))
    c.trap(1, solve_abc(2, 2, perp=False))
    c.ans(2, solve_abc(1, 3))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
