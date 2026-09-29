from lib import *

ORIG = dict(
    id="20p-45", chapter=1, page=20, num=45, source="2025년 수능특강 [25009-0022]", type="주관식",
    stem=r"두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $f(0)=1$, $f(1)=3$, $g(0)=5$일 때, $g(6)$의 값을 구하시오.",
    box=[r"(가) $\displaystyle\lim_{x\to0+}x^2f\!\left(\frac1x\right)=4$",
         r"(나) $\displaystyle\lim_{x\to\infty}\frac{f(x)-2g(x)}{x}=3$"],
    answer="62",
    general="(가): 1/x=t→∞, f(t)/t²→4 → f 는 이차, 최고차 4. f(0)=1, f(1)=3 → f=4x²−2x+1. (나): f−2g=3x+s, g(0)=5 → s=1−10=−9 → g=(4x²−5x+10)/2, g(6)=62.",
    special="① (나)를 f−2g 의 일차항 계수 3 으로 읽음 — x→+∞ 이고 분모가 x 라서 부호 그대로. x→−∞ 에서 √(x²+1) 로 나누면 부호가 바뀜.",
    perspective="x²f(1/x) 는 f 의 이차항 계수, (f−2g)/x 는 일차항 계수.",
    table=[
        ("x→∞, 분모 x", "x→−∞ 에서 √(x²) = −x", "분모를 √(x²+1), x→−∞ 로 바꾸면 f−2g 의 기울기 부호 반전"),
        ("(가)의 값 4", "—", "2 로 바꾸면 f 만 바뀜 (생존)"),
    ],
    sweep=["x→−∞ 에서 √(x²+1)/x → −1"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (x→−∞ 에서 √(x²+1) 의 부호)",
        changed=["(나) lim_{x→∞} (f−2g)/x → lim_{x→−∞} (f−2g)/√(x²+1)"], naturalness="",
        stem=r"두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $f(0)=1$, $f(1)=3$, $g(0)=5$일 때, $g(6)$의 값을 구하시오.",
        box=[r"(가) $\displaystyle\lim_{x\to0+}x^2f\!\left(\frac1x\right)=4$",
             r"(나) $\displaystyle\lim_{x\to-\infty}\frac{f(x)-2g(x)}{\sqrt{x^2+1}}=3$"],
        answer="80", trap_answer="62",
        trap_path="√(x²+1)≈x 로 보고 f−2g=3x+s 로 둠 → 62 (x→−∞ 에서는 √(x²+1)≈−x).",
        explanation=[
            r"(가)에서 $f$는 최고차항의 계수가 $4$인 이차함수이고 $f(0)=1$, $f(1)=3$이므로 $f(x)=4x^2-2x+1$이다.",
            r"(나)에서 $f-2g$는 일차 이하이고, $x\to-\infty$일 때 $\sqrt{x^2+1}\approx-x$이다.",
            r"함정: 따라서 $f(x)-2g(x)=-3x+s$이다. 기울기는 $+3$이 아니라 $-3$이다.",
            r"$g(0)=5$에서 $s=1-10=-9$이므로 $g(x)=\dfrac{4x^2+x+10}{2}$이다.",
            r"$g(6)=\dfrac{144+6+10}{2}=80$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 ((가)의 값 4 → 2)",
        changed=["(가)의 값 4 → 2"], naturalness="",
        stem=r"두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $f(0)=1$, $f(1)=3$, $g(0)=5$일 때, $g(6)$의 값을 구하시오.",
        box=[r"(가) $\displaystyle\lim_{x\to0+}x^2f\!\left(\frac1x\right)=2$",
             r"(나) $\displaystyle\lim_{x\to\infty}\frac{f(x)-2g(x)}{x}=3$"],
        answer="32", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)에서 $f$는 최고차항의 계수가 $2$인 이차함수이고 $f(0)=1$, $f(1)=3$이므로 $f(x)=2x^2+1$이다.",
            r"(나)에서 $f(x)-2g(x)=3x+s$이고 $g(0)=5$에서 $s=-9$이다.",
            r"$g(x)=\dfrac{2x^2-3x+10}{2}$이므로 $g(6)=\dfrac{72-18+10}{2}=32$이다.",
        ],
    ),
]


def solve_g(A, lim2):
    a2, a1, a0, b2, b1, b0 = symbols('a2 a1 a0 b2 b1 b0', real=True)
    f = a2*x**2 + a1*x + a0
    g = b2*x**2 + b1*x + b0
    eqs = [Eq(a2, A), f.subs(x, 0) - 1, f.subs(x, 1) - 3, g.subs(x, 0) - 5]
    h = f - 2*g
    # (나): 이차항 0, 극한값 조건
    eqs += [Eq(Poly(h, x).coeff_monomial(x**2), 0)]
    sol0 = solve(eqs, [a2, a1, a0, b2, b0], dict=True)[0]
    hs = h.subs(sol0)
    s1 = solve(Eq(lim2(hs), 3), b1, dict=True)
    G = g.subs(sol0).subs(s1[0])
    F = f.subs(sol0)
    return F, expand(G)


def verify(c):
    fs = symbols('fs')
    for key, A, L in (('orig', 4, lambda h: limit(h/x, x, oo)),
                      (1, 4, lambda h: limit(h/sqrt(x**2 + 1), x, -oo)),
                      (2, 2, lambda h: limit(h/x, x, oo))):
        F, G = solve_g(A, L)
        c.check(f"{key}: (가) 재확인", limit(x**2*F.subs(x, 1/x), x, 0, '+') == A)
        c.ans(key, G.subs(x, 6))
    F, G = solve_g(4, lambda h: limit(h/x, x, oo))
    c.trap(1, G.subs(x, 6))
