from lib import *

def stem(p, fp, hp):
    return (r"다항함수 $f(x)$와 실수 전체의 집합에서 미분가능한 함수 $g(x)$는 모든 실수 $x$에 대하여 $(x^2-1)g(x)=f(x)-2$를 만족시킨다. 함수 $h(x)=f(x)g(x)$에 대하여 $f'(" + p + r")=" + fp + r"$, $h'(" + p + r")=" + hp + r"$일 때, $g'(" + p + r")$의 값을 구하시오.")

ORIG = dict(
    id="61p-29", chapter=3, page=61, num=29, source="2022년 수능완성 [22054-0129]", type="주관식",
    stem=stem("1", "-2", "6"), answer="2",
    general="x=1: f(1)=2. 양변 미분: 2xg+(x²−1)g'=f' → x=1: 2g(1)=f'(1)=−2 → g(1)=−1. h'(1)=f'(1)g(1)+f(1)g'(1)=2+2g'(1)=6 → g'(1)=2.",
    special="① 미분한 식에 x=1 을 넣어 2x→2 — 점을 −1 로 옮기면 2x→−2 로 부호가 바뀜.",
    perspective="항등식 미분 후 근에서 대입.",
    table=[
        ("점 x=1", "x=−1 (2x 의 부호)", "−1 에서 물으면 2x=−2 → g(−1)=−f'(−1)/2"),
        ("h'(1)=6", "—", "12 이면 g'(1)=5 (생존)"),
    ],
    sweep=["x²−1 의 근 ±1 에서 2x=±2"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 7 (대입값 2x 의 부호)",
        changed=["점 x=1 → x=−1 (f'(−1)=−2, h'(−1)=6)"], naturalness="세 조건의 점을 한꺼번에 옮긴 한 가지 변경.",
        stem=stem("-1", "-2", "6"), answer="4", trap_answer="2",
        trap_path="원문처럼 2g(−1)=f'(−1) 로 두어 g(−1)=−1 → 2+2g'(−1)=6 → 2 (실제는 −2g(−1)=f'(−1)).",
        explanation=[
            r"$x=-1$을 대입하면 $f(-1)=2$이다.",
            r"양변을 미분하면 $2xg(x)+(x^2-1)g'(x)=f'(x)$이고 $x=-1$에서 $-2g(-1)=f'(-1)=-2$, $g(-1)=1$이다.",
            r"함정: $2x$는 $x=-1$에서 $-2$이다.",
            r"$h'(-1)=f'(-1)g(-1)+f(-1)g'(-1)=-2+2g'(-1)=6$이므로 $g'(-1)=4$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (h'(1)=6 → 12)",
        changed=["h'(1)=6 → 12"], naturalness="",
        stem=stem("1", "-2", "12"), answer="5", trap_answer=None, trap_path=None,
        explanation=[
            r"$x=1$에서 $f(1)=2$이다.",
            r"미분하면 $2xg+(x^2-1)g'=f'$이고 $x=1$에서 $2g(1)=-2$, $g(1)=-1$이다.",
            r"$h'(1)=(-2)(-1)+2g'(1)=12$이므로 $g'(1)=5$이다.",
        ],
    ),
]


def solve_gp(p, fpv, hpv):
    # f 를 일반 다항식(4차 이하), g=(f−2)/(x²−1) 이 다항식(미분가능) 이도록 두고 조건 풀기
    cs = symbols('c0:5')
    f = sum(ci*x**i for i, ci in enumerate(cs))
    rem_ = rem(Poly(f - 2, x), Poly(x**2 - 1, x)).as_expr()
    eqs = [Poly(rem_, x).coeff_monomial(1), Poly(rem_, x).coeff_monomial(x)]
    g = quo(Poly(f - 2, x), Poly(x**2 - 1, x)).as_expr()
    h = f*g
    eqs += [diff(f, x).subs(x, p) - fpv, diff(h, x).subs(x, p) - hpv]
    sols = solve(eqs, cs, dict=True)
    vals = {simplify(diff(g, x).subs(x, p).subs(s)) for s in sols}
    return vals


def verify(c):
    for key, p, fpv, hpv in (('orig', 1, -2, 6), (1, -1, -2, 6), (2, 1, -2, 12)):
        v = solve_gp(p, fpv, hpv)
        c.check(f"{key}: g'({p}) 값이 하나로 결정", len(v) == 1 and not list(v)[0].free_symbols)
        c.ans(key, list(v)[0])
    c.trap(1, solve_gp(1, -2, 6).pop())
