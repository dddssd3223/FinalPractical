from lib import *

def stem(pt, L, tail):
    return (r"사차함수 $f(x)$에 대하여 함수 $g(x)=\begin{cases}\dfrac{f(x)}{x^2-4} & (|x|\neq2) \\ -x+a & (|x|=2)\end{cases}$라 하자. "
            r"함수 $g(x)$가 실수 전체의 집합에서 미분가능하고 $\displaystyle\lim_{x\to" + pt + r"}\frac{g(x)-3}{f(x)}=" + L + r"$일 때, " + tail + r" (단, $a$는 상수이다.)")

ORIG = dict(
    id="66p-42", chapter=3, page=66, num=42, source="2022년 수능특강 [22009-0073]", type="객관식",
    stem=stem("2", r"\frac14", r"$g(a)$의 값은?"), choices=["21", "23", "25", "27", "29"], answer="21",
    general="g 연속 → f(±2)=0, f=(x²−4)q (q 이차), g=q. q(2)=a−2, q(−2)=a+2. 극한: g(2)=3 → a=5, q(−2)=7; (q−3)/((x²−4)q) → q'(2)/(4·3)=1/4 → q'(2)=3. q=x²−x+1 → g(5)=21.",
    special="① x→2 에서 x+2→4 (양수) — x→−2 로 옮기면 x−2→−4 로 부호가 바뀜. ② 분모 f 안의 q(2)=3 도 곱해짐.",
    perspective="g=f/(x²−4) 가 다항식 q 로 이어지는 구조.",
    table=[
        ("극한점 x=2 (남는 인수 x+2→4)", "x=−2 (남는 인수 x−2→−4)", "x→−2, 값 −1/4 이면 q=−x²−x+5, g(1)=3"),
        ("극한값 1/4", "—", "7/12 면 q=2x²−x−3 → g(5)=42 (생존)"),
    ],
    sweep=["q'(2)=12L, α=(12L+1)/4"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 7 (남는 인수 x−2 가 −4)",
        changed=["극한점 x→2 → x→−2", "극한값 1/4 → −1/4"],
        naturalness="극한점을 −2 로 옮기면 1/4 로는 q 의 계수가 분수가 되어 값의 부호를 함께 바꾼 것.",
        stem=stem("-2", r"-\frac14", r"$g(a)$의 값은?"), choices=["-3/2", "1", "3", "5", "7"], answer="3", trap_answer="-3/2",
        trap_path="원문처럼 남는 인수를 +4 로 두어 q'(−2)/(4·3)=−1/4 → q'(−2)=−3 → q=x²/2−x−1 → g(1)=−3/2.",
        explanation=[
            r"$g$가 연속이므로 $f(\pm2)=0$, $f(x)=(x^2-4)q(x)$ ($q$는 이차식)이고 $g=q$, $q(2)=a-2$, $q(-2)=a+2$이다.",
            r"극한이 존재하므로 $q(-2)=3$, $a=1$, $q(2)=-1$이다.",
            r"$\dfrac{q(x)-3}{(x-2)(x+2)q(x)}\to\dfrac{q'(-2)}{(-4)\times3}=-\dfrac14$이므로 $q'(-2)=3$이다. 함정: $x-2\to-4$이다.",
            r"$q=\alpha x^2+\beta x+\gamma$에서 $4\beta=q(2)-q(-2)=-4$, $\beta=-1$, $-4\alpha-1=3$, $\alpha=-1$, $\gamma=5$이다.",
            r"$g(a)=g(1)=-1-1+5=3$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (극한값 1/4 → 7/12)",
        changed=["극한값 1/4 → 7/12"], naturalness="",
        stem=stem("2", r"\frac7{12}", r"$g(a)$의 값은?"), choices=["34", "36", "38", "40", "42"], answer="42", trap_answer=None, trap_path=None,
        explanation=[
            r"원문과 같이 $f=(x^2-4)q$, $g=q$이고 $q(2)=3$에서 $a=5$, $q(-2)=7$이다.",
            r"극한값 $\dfrac{q'(2)}{4\times3}=\dfrac7{12}$에서 $q'(2)=7$이다.",
            r"$\beta=-1$, $4\alpha-1=7$, $\alpha=2$, $\gamma=-3$이므로 $q=2x^2-x-3$이다.",
            r"$g(5)=50-5-3=42$이다.",
        ],
    ),
]


def solve_g(pt, L):
    cs = symbols('c0:5')
    a = Symbol('a')
    f = sum(ci*x**i for i, ci in enumerate(cs))
    sols = []
    # g 가 ±2 에서 유한 극한 → f(±2)=0 (필요), 그때 g = 몫 q
    base = solve([f.subs(x, 2), f.subs(x, -2)], [cs[0], cs[1]], dict=True)[0]
    F = f.subs(base)
    q = cancel(F/(x**2 - 4))
    assert q.is_polynomial(x)
    eqs = [q.subs(x, 2) - (-2 + a), q.subs(x, -2) - (2 + a)]  # 연속 (미분가능성은 q 다항식이라 자동)
    # 극한 존재: g(pt)=3 필요, 그 후 극한값
    eqs.append(q.subs(x, pt) - 3)
    for s in solve(eqs, [a, cs[2], cs[3]], dict=True):
        qq = q.subs(s)
        free = qq.free_symbols - {x}
        lim_ = limit((qq - 3)/(F.subs(s)), x, pt)
        s2 = solve(lim_ - L, list(free), dict=True)
        for t in s2:
            q3 = qq.subs(t)
            assert not (q3.free_symbols - {x}) and degree(q3, x) == 2
            av = s[a].subs(t)
            sols.append((q3, av))
    return sols


def verify(c):
    s = solve_g(2, Rational(1, 4))
    c.check("원문: 유일", len(s) == 1)
    q, a = s[0]
    c.ans('orig', q.subs(x, a))
    s = solve_g(-2, Rational(-1, 4))
    c.check("1: 유일", len(s) == 1)
    q, a = s[0]
    c.ans(1, q.subs(x, a))
    # 함정: 남는 인수 부호를 +4 로 → 극한값 +1/4 로 푼 것과 같음
    s = solve_g(-2, Rational(1, 4))
    q, a = s[0]
    c.trap(1, q.subs(x, a))
    s = solve_g(2, Rational(7, 12))
    c.check("2: 유일", len(s) == 1)
    q, a = s[0]
    c.ans(2, q.subs(x, a))
