from lib import *

def box(fg, g0):
    return [r"(가) 모든 실수 $x$에 대하여 $f(x)g(x)=" + fg + r"$이다.", r"(나) $g(0)=" + g0 + r"$"]

STEM = r"최고차항의 계수가 $1$인 삼차함수 $f(x)$에 대하여 실수 전체의 집합에서 연속인 함수 $g(x)$가 다음 조건을 만족시킨다. $f(1)$이 자연수일 때, $g(2)$의 최솟값은?"

ORIG = dict(
    id="49p-51", chapter=2, page=49, num=51, source="2019학년도 대수능 나형 21번", type="객관식",
    stem=STEM + " [4점]", box=box("x(x+3)", "1"), choices=["5/13", "5/14", "1/3", "5/16", "5/17"], answer="5/13",
    general="g=x(x+3)/f 가 연속이려면 f 의 실근은 분자의 근 0, −3 중 단순근만. g(0)=1 → f(0)=0, f=xq, g=(x+3)/q, q(0)=3. q 가 −3 을 근으로 가지면 다른 근 −1 이 생겨 불가 → q=x²+px+3 (실근 없음, p²<12). f(1)=4+p 자연수 → p≤3 정수. g(2)=5/(7+2p) → p=3 에서 5/13.",
    special="① q 가 실근이 없는 경우만 봄 — 원문은 q(0)=3 때문에 −3 을 근으로 갖는 q 가 불가능해서 우연히 통함. 분자에 (x+3)² 이 있으면 q=(x+3)² 도 가능.",
    perspective="f 의 실근 ⊂ 분자의 근 (차수 포함), 나머지 인수는 실근 없음.",
    table=[
        ("분자 x(x+3) (−3 이 단순근)", "f 가 −3 을 근으로 갖는 경우", "x(x+3)² 이면 f=x(x+3)² 도 가능 → g≡1"),
        ("g(0)=1", "—", "1/3 이면 q(0)=9 (생존)"),
    ],
    sweep=["q 의 판별식 p²−4q(0)<0", "q 가 분자의 근을 가질 수 있는지"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 6 (분자의 중근을 f 가 가져가는 경우)",
        changed=["(가) f(x)g(x)=x(x+3) → x(x+3)²"], naturalness="",
        stem=STEM, box=box("x(x+3)^2", "1"), choices=["25/29", "1", "25/23", "25/21", "25/19"], answer="1", trap_answer="25/23",
        trap_path="원문처럼 f=x(x²+px+q) 의 이차식이 실근이 없는 경우만 보고 p=5 에서 25/23.",
        explanation=[
            r"$g=\dfrac{x(x+3)^2}{f(x)}$가 연속이고 $g(0)=1$이므로 $f(x)=xq(x)$, $g=\dfrac{(x+3)^2}{q(x)}$, $q(0)=9$이다.",
            r"(i) $q$가 실근이 없으면 $q=x^2+px+9$ ($p^2<36$), $f(1)=10+p$가 자연수이므로 $p\le5$이고 $g(2)=\dfrac{25}{13+2p}\ge\dfrac{25}{23}$이다.",
            r"(ii) 함정: $q(x)=(x+3)^2$이면 $f(x)=x(x+3)^2$, $g(x)=1$로 연속이고 $f(1)=16$도 자연수이다.",
            r"따라서 $g(2)$의 최솟값은 $1$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (g(0)=1 → 1/3)",
        changed=["(나) g(0)=1 → 1/3"], naturalness="",
        stem=STEM, box=box("x(x+3)", r"\frac13"), choices=["5/23", "5/21", "5/19", "5/17", "5/13"], answer="5/23", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)=xq(x)$, $g=\dfrac{x+3}{q}$, $g(0)=\dfrac3{q(0)}=\dfrac13$에서 $q(0)=9$이다.",
            r"$q$가 $-3$을 근으로 가지면 $q=(x+3)^2$이 되어 $g=\frac1{x+3}$이 불연속이므로 $q=x^2+px+9$ ($p^2<36$)이다.",
            r"$f(1)=10+p$가 자연수이므로 $p\le5$, $g(2)=\dfrac{5}{13+2p}$의 최솟값은 $\dfrac5{23}$이다.",
        ],
    ),
]


def candidates(N, g0):
    """f=x³+ax²+bx+c (정수 계수 범위 탐색) 중 조건을 만족하는 (f, g) — f(1) 자연수라 계수 합이 정수가 되도록 a,b 정수 탐색"""
    out = []
    for a in range(-10, 11):
        for b in range(-30, 31):
            f = x**3 + a*x**2 + b*x
            g = cancel(N/f)
            num, den = fraction(g)
            if Poly(den, x).degree() > 0 and real_roots(Poly(den, x)):
                continue
            if g.subs(x, 0) != g0:
                continue
            f1 = f.subs(x, 1)
            if f1.is_integer and f1 > 0:
                out.append((f, g))
    return out


def verify(c):
    r = candidates(x*(x + 3), 1)
    c.ans('orig', min(g.subs(x, 2) for f, g in r))
    r1 = candidates(x*(x + 3)**2, 1)
    c.check("1: f=x(x+3)² 포함", any(expand(f - x*(x + 3)**2) == 0 for f, g in r1))
    c.ans(1, min(g.subs(x, 2) for f, g in r1))
    c.trap(1, min(g.subs(x, 2) for f, g in r1 if expand(f - x*(x + 3)**2) != 0))
    r2 = candidates(x*(x + 3), Rational(1, 3))
    c.ans(2, min(g.subs(x, 2) for f, g in r2))
