from lib import *

ORIG = dict(
    id="16p-37", chapter=1, page=16, num=37, source="2022년 수능특강 [22009-0021]", type="객관식",
    stem=r"삼차함수 $f(x)$와 일차함수 $g(x)$가 모든 실수 $x$에 대하여 $f(x)=2x^3-x^2g(x)-2x$를 만족시킨다. $\displaystyle\lim_{x\to1}\frac{g(x)}{f(x)+g(x)}=-\frac12$일 때, $g(-3)$의 값은?",
    choices=["6", "7", "8", "9", "10"], answer="8",
    general="f+g=(x²−1){2x−g(x)} 이므로 x→1 에서 분모→0 → g(1)=0, g=p(x−1). 극한 = p/{(1+1)·2} = p/4 = −1/2 → p=−2 (p≠2 라 f 삼차) → g(−3)=8.",
    special="① x=1 을 대입해 f(1)+g(1)=0 을 확인하고 분자 g(1)=0 — 극한점이 x²−1 의 근일 때만 분모가 자동으로 0. ② (x²−1) 을 (x−1) 로 약분하고 남는 (x+1) 을 대입.",
    perspective="f+g=(x²−1)(2x−g) 로 묶어 보는 것이 핵심.",
    table=[
        ("극한점 x=1", "분모가 0 이 아닌 점", "x=0 이면 (x²−1)→−1 이 남고, g(0)≠0 이면 극한 1"),
        ("삼차함수", "p=2 (f 가 이차 이하)", "—"),
        ("극한값 −1/2", "—", "값만 바꾸면 p 만 바뀜"),
    ],
    sweep=["극한점 a: a²=1 이면 분모 자동 0, 아니면 g(a)=0 이 추가로 필요", "p=2 이면 f 차수 하락"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 1행 (극한점 1 → −1, 여전히 x²−1 의 근)",
        changed=["극한점 x→1 → x→−1"], naturalness="",
        stem=r"삼차함수 $f(x)$와 일차함수 $g(x)$가 모든 실수 $x$에 대하여 $f(x)=2x^3-x^2g(x)-2x$를 만족시킨다. $\displaystyle\lim_{x\to-1}\frac{g(x)}{f(x)+g(x)}=-\frac12$일 때, $g(-3)$의 값은?",
        choices=["2", "4", "6", "8", "10"], answer="4", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)+g(x)=2x^3-2x-(x^2-1)g(x)=(x^2-1)\{2x-g(x)\}$이다.",
            r"$x\to-1$에서 분모가 $0$으로 가므로 $g(-1)=0$, $g(x)=p(x+1)$이다.",
            r"극한은 $\dfrac{p}{(-2)(-2)}=\dfrac p4=-\dfrac12$이므로 $p=-2$이다.",
            r"$g(-3)=-2\times(-2)=4$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 7 (x=0 에서는 (x²−1) 이 약분되지 않고 −1 로 대입)",
        changed=["극한점 x→1 → x→0"], naturalness="",
        stem=r"삼차함수 $f(x)$와 일차함수 $g(x)$가 모든 실수 $x$에 대하여 $f(x)=2x^3-x^2g(x)-2x$를 만족시킨다. $\displaystyle\lim_{x\to0}\frac{g(x)}{f(x)+g(x)}=-\frac12$일 때, $g(-3)$의 값은?",
        choices=["-4", "-2", "2", "4", "6"], answer="-2", trap_answer="6",
        trap_path="원문처럼 (x²−1) 이 약분된다고 보고 극한을 p/(2−p) 로 계산 → p=−2 → g(−3)=6. (x=0 에서 x²−1=−1 이 남음)",
        explanation=[
            r"$f(x)+g(x)=(x^2-1)\{2x-g(x)\}$이고 $x=0$에서 이 값은 $g(0)$이다.",
            r"$g(0)\neq0$이면 극한이 $\dfrac{g(0)}{g(0)}=1$이 되어 모순이므로 $g(0)=0$, $g(x)=px$이다.",
            r"극한은 $\dfrac{px}{(x^2-1)(2-p)x}\to\dfrac{p}{-(2-p)}$이다. 함정: $x^2-1\to-1$을 빠뜨리지 않는다.",
            r"$\dfrac{p}{p-2}=-\dfrac12$에서 $p=\dfrac23$이다.",
            r"$g(-3)=\dfrac23\times(-3)=-2$이다.",
        ],
    ),
]


def solve_g(a, value):
    p, q = symbols('p q', real=True)
    g = p*x + q
    f = 2*x**3 - x**2*g - 2*x
    out = []
    D = (f + g).subs(x, a)
    # 경우 A: 분모≠0 → 값의 비 (매개변수족이 남으면 답 불확정)
    for s in solve(Eq(g.subs(x, a), value*D), [p, q], dict=True):
        if simplify(D.subs(s)) != 0:
            out.append(('A', s))
    # 경우 B: 분모=0 → 분자=0 후 극한
    for s in solve([D, g.subs(x, a)], [p, q], dict=True):
        gs, fs = g.subs(s), f.subs(s)
        free = (gs.free_symbols | fs.free_symbols) - {x}
        L = limit(gs/(fs + gs), x, a)
        for t in solve(Eq(L, value), list(free), dict=True):
            G, F = gs.subs(t), fs.subs(t)
            if Poly(F, x).degree() == 3:
                out.append(('B', G))
    return out


def verify(c):
    for key, a, v in (('orig', 1, -Rational(1, 2)), (1, -1, -Rational(1, 2)), (2, 0, -Rational(1, 2))):
        r = solve_g(a, v)
        bs = [G for k, G in r if k == 'B']
        c.check(f"{key}: 분모≠0 경우 해 없음, 분모=0 경우 해 하나", len(r) == 1 and len(bs) == 1)
        c.ans(key, bs[0].subs(x, -3))
    pp = Symbol('p')
    tp = solve(Eq(pp/(2 - pp), -Rational(1, 2)), pp)[0]
    c.trap(2, tp*(-3))
