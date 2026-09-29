from lib import *

F_TXT = r"f(x)=\begin{cases}x^2-x & (x<2,\ x\neq1)\\ 3 & (x=1)\\ x^2+x & (x\ge2)\end{cases}"
ORIG = dict(
    id="18p-41", chapter=1, page=18, num=41, source="2021년 수능특강 [21009-0022]", type="객관식",
    stem=r"함수 $" + F_TXT + r"$와 이차함수 $g(x)$가 다음 조건을 만족시킬 때, $g(1)$의 값은?",
    box=[r"(가) $\displaystyle\lim_{x\to0}\frac{g(x)}{f(x+1)}=2$",
         r"(나) $\displaystyle\lim_{x\to-1+}f(1-x)g(x)=\lim_{x\to1+}f(x+1)g(x)$"],
    choices=["-2", "-1", "0", "1", "2"], answer="-2",
    general="(가): x→0 에서 x+1→1(1 은 아님) → f(x+1)=(x+1)²−(x+1)=x(x+1)→0 → g(0)=0, g'(0)=2, g=x(ax+2). (나): x→−1+ 이면 1−x→2− → f→2; x→1+ 이면 x+1→2+ → f→6. 2g(−1)=6g(1) → 2(a−2)=6(a+2) → a=−4, g(1)=−2.",
    special="① f(1)=3 (함숫값)을 극한에 대입 — x+1 은 1 에 가까워질 뿐 1 이 아님. ② 안쪽 함수가 2 에 어느 쪽에서 다가가는지(2−/2+) 확인 없이 한 조각식을 사용.",
    perspective="합성 극한은 '안쪽 값이 어느 쪽에서 다가가는가'로 조각을 고른다.",
    table=[
        ("(나)의 방향 −1+, 1+", "안쪽이 2+/2− 로 바뀌는 경우", "방향을 뒤집으면 f 극한값 2, 6 이 서로 바뀜"),
        ("x=1 에서 값 3", "극한과 함숫값을 혼동", "—"),
        ("(가)의 값 2", "—", "g'(0) 만 바뀜 (생존)"),
    ],
    sweep=["안쪽 1−x, x+1 이 2 를 지나는 점 x=−1, x=1", "x+1=1 ⇔ x=0 (함숫값 3 은 극한에 무관)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (한쪽 극한 방향 → 조각 선택)",
        changed=["(나)의 극한 방향 x→−1+, x→1+ → x→−1−, x→1−"], naturalness="",
        stem=r"함수 $" + F_TXT + r"$와 이차함수 $g(x)$가 다음 조건을 만족시킬 때, $g(1)$의 값은?",
        box=[r"(가) $\displaystyle\lim_{x\to0}\frac{g(x)}{f(x+1)}=2$",
             r"(나) $\displaystyle\lim_{x\to-1-}f(1-x)g(x)=\lim_{x\to1-}f(x+1)g(x)$"],
        choices=["-2", "2", "4", "6", "8"], answer="6", trap_answer="-2",
        trap_path="원문과 같은 조각(좌변 2, 우변 6)을 그대로 써서 2g(−1)=6g(1) → −2.",
        explanation=[
            r"(가): $x\to0$이면 $x+1\to1$ ($x+1\neq1$)이므로 $f(x+1)=x(x+1)\to0$, 따라서 $g(0)=0$, $g'(0)=2$이고 $g(x)=x(ax+2)$이다.",
            r"(나) 좌변: $x\to-1-$이면 $1-x\to2+$이므로 $f(1-x)\to6$이다.",
            r"(나) 우변: $x\to1-$이면 $x+1\to2-$이므로 $f(x+1)\to2$이다. 함정: 원문과 조각이 서로 바뀐다.",
            r"$6g(-1)=2g(1)$에서 $6(a-2)=2(a+2)$, $a=4$이다.",
            r"$g(1)=a+2=6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 3행 ((가)의 값 2 → 4)",
        changed=["(가)의 극한값 2 → 4"], naturalness="",
        stem=r"함수 $" + F_TXT + r"$와 이차함수 $g(x)$가 다음 조건을 만족시킬 때, $g(1)$의 값은?",
        box=[r"(가) $\displaystyle\lim_{x\to0}\frac{g(x)}{f(x+1)}=4$",
             r"(나) $\displaystyle\lim_{x\to-1+}f(1-x)g(x)=\lim_{x\to1+}f(x+1)g(x)$"],
        choices=["-6", "-4", "-2", "2", "4"], answer="-4", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)에서 $g(0)=0$, $g'(0)=4$이므로 $g(x)=x(ax+4)$이다.",
            r"(나): $x\to-1+$이면 $f(1-x)\to2$, $x\to1+$이면 $f(x+1)\to6$이다.",
            r"$2g(-1)=6g(1)$에서 $2(a-4)=6(a+4)$, $a=-8$이다.",
            r"$g(1)=-8+4=-4$이다.",
        ],
    ),
]

P = [(x**2 - x, -oo, 2), (x**2 + x, 2, oo)]  # x=1 의 값 3 은 극한과 무관(안쪽이 1 에 머물지 않음)


def solve_g(v, dl, dr):
    a, b, c0 = symbols('a b c0', real=True)
    g = a*x**2 + b*x + c0
    # (가): x→0, 안쪽 x+1 → 1 (≠1): 조각 x²−x
    D = (x**2 - x).subs(x, x + 1)
    eqs = [g.subs(x, 0)]  # 분모→0 이므로 분자→0
    gs = g.subs(c0, 0)
    eqs2 = [Eq(limit(gs/D, x, 0), v)]
    L = clim(P, 1 - x, lambda e: e*gs, -1, dl)
    R = clim(P, x + 1, lambda e: e*gs, 1, dr)
    sols = solve(eqs2 + [Eq(L, R)], [a, b], dict=True)
    return [expand(gs.subs(s)) for s in sols]


def verify(c):
    for key, v, dl, dr in (('orig', 2, '+', '+'), (1, 2, '-', '-'), (2, 4, '+', '+')):
        r = solve_g(v, dl, dr)
        c.check(f"{key}: g 하나, 이차", len(r) == 1 and Poly(r[0], x).degree() == 2)
        c.ans(key, r[0].subs(x, 1))
    r = solve_g(2, '+', '+')
    c.trap(1, r[0].subs(x, 1))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
