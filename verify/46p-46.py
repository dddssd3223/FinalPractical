from lib import *

def stem(curve):
    return (r"실수 $t$에 대하여 직선 $y=t$가 곡선 $" + curve + r"$와 만나는 점의 개수를 $f(t)$라 하자. 최고차항의 계수가 $1$인 이차함수 $g(t)$에 대하여 함수 $f(t)g(t)$가 모든 실수 $t$에서 연속일 때, $f(3)+g(3)$의 값을 구하시오.")

ORIG = dict(
    id="46p-46", chapter=2, page=46, num=46, source="2016학년도 수능 6월 모의평가 A형 29번", type="주관식",
    stem=stem(r"y=|x^2-2x|") + " [4점]", answer="8",
    general="f(t): t<0 →0, t=0 →2, 0<t<1 →4, t=1 →3, t>1 →2. f 가 불연속인 t=0, 1 에서 fg 가 연속이려면 g(0)=g(1)=0 → g=t(t−1). f(3)+g(3)=2+6=8.",
    special="① f(3)=2 를 W 모양 전체에서 셈 — 정의역이 잘리면 바깥쪽 교점 수가 달라짐. ② g 는 f 의 불연속점에서 0 이어야 한다는 일반 원리.",
    perspective="f 의 점프 지점마다 g=0.",
    table=[
        ("정의역 전체", "x≥0 처럼 일부만인 경우", "x≥0 이면 f(3)=1 (오른쪽 가지만)"),
        ("y=|x²−2x|", "—", "+1 로 올리면 불연속점 1, 2 → g=(t−1)(t−2) (생존)"),
    ],
    sweep=["f 의 불연속점 = 극값 0, 1", "정의역을 자르면 t 가 클 때의 교점 수 변화"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (정의역이 잘려 교점 개수가 바뀜)",
        changed=["곡선 y=|x²−2x| → y=|x²−2x| (x≥0)"], naturalness="",
        stem=stem(r"y=|x^2-2x|\ (x\ge0)"), answer="7", trap_answer="8",
        trap_path="원문처럼 t>1 에서 교점 2 개로 보아 f(3)=2 → 8 (x≥0 이면 오른쪽 가지 하나뿐).",
        explanation=[
            r"$x\ge0$에서 $y=|x^2-2x|$는 $x=1$에서 극댓값 $1$을 갖고 $x=0,\,2$에서 $0$이다.",
            r"$f(t)$: $t<0$에서 $0$, $t=0$에서 $2$, $0<t<1$에서 $3$, $t=1$에서 $2$, $t>1$에서 $1$이다.",
            r"$f$가 불연속인 $t=0,\,1$에서 $g=0$이어야 하므로 $g(t)=t(t-1)$이다.",
            r"함정: $t>1$일 때 교점은 $x>2$ 쪽 하나뿐이다. $f(3)+g(3)=1+6=7$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (곡선을 1 만큼 올림)",
        changed=["y=|x²−2x| → y=|x²−2x|+1"], naturalness="",
        stem=stem(r"y=|x^2-2x|+1"), answer="4", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(t)$: $t<1$에서 $0$, $t=1$에서 $2$, $1<t<2$에서 $4$, $t=2$에서 $3$, $t>2$에서 $2$이다.",
            r"$f$가 불연속인 $t=1,\,2$에서 $g=0$이므로 $g(t)=(t-1)(t-2)$이다.",
            r"$f(3)+g(3)=2+2=4$이다.",
        ],
    ),
]


def f_count(curve_pieces, tv):
    sols = set()
    for e, lo, hi in curve_pieces:
        for r in real_roots(Poly(e - tv, x)):
            if lo <= r <= hi:
                sols.add(r)
    return len(sols)


def solve_g(pieces, crit):
    p, q = symbols('p q')
    g = Symbol('T')**2 + p*Symbol('T') + q
    T = Symbol('T')
    eqs = []
    jumps = []
    for cv in crit:
        e = Rational(1, 100)
        vals = [f_count(pieces, cv - e), f_count(pieces, cv), f_count(pieces, cv + e)]
        if len(set(vals)) > 1:
            jumps.append(cv)
            eqs.append(g.subs(T, cv))
    s = solve(eqs, [p, q], dict=True)
    return g.subs(s[0]).subs(T, 3), jumps


def verify(c):
    W = [(x**2 - 2*x, -oo, 0), (2*x - x**2, 0, 2), (x**2 - 2*x, 2, oo)]
    g3, jumps = solve_g(W, [Integer(0), Integer(1)])
    c.check("원문: 불연속점 {0, 1}", jumps == [0, 1])
    c.ans('orig', f_count(W, 3) + g3)
    W1 = [(x**2 - 2*x, 0, 0), (2*x - x**2, 0, 2), (x**2 - 2*x, 2, oo)]
    g3, jumps = solve_g(W1, [Integer(0), Integer(1)])
    c.check("1: 불연속점 {0, 1}", jumps == [0, 1])
    c.ans(1, f_count(W1, 3) + g3)
    c.trap(1, f_count(W, 3) + g3)
    W2 = [(e + 1, lo, hi) for e, lo, hi in W]
    g3, jumps = solve_g(W2, [Integer(1), Integer(2)])
    c.check("2: 불연속점 {1, 2}", jumps == [1, 2])
    c.ans(2, f_count(W2, 3) + g3)
