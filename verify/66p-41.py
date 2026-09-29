from lib import *

def box(rhs):
    return [r"(가) 두 함수 $f(x)$, $g(x)$는 모두 최고차항의 계수가 정수이다.",
            r"(나) 모든 실수 $x$에 대하여 $\displaystyle\lim_{h\to0}\frac{f\left(x+\frac h2\right)-f(x)}{h}\times\lim_{h\to0}\frac{g\left(x-\frac h3\right)-g(x)}{h}=" + rhs + r"$이다."]

HEAD = r"삼차함수 $f(x)$와 이차함수 $g(x)$가 다음 조건을 만족시킨다. "

ORIG = dict(
    id="66p-41", chapter=3, page=66, num=41, source="2022년 수능특강 [22009-0072]", type="주관식",
    stem=HEAD + r"함수 $f'(x)$가 최솟값 $m$을 가질 때, $g'(m)$의 값을 구하시오.",
    box=box("-x^3-x^2+2"), answer="4",
    general="(나): (1/2)f'·(−1/3)g' = −x³−x²+2 → f'g'=6(x−1)(x²+2x+2). 최고차 계수 p, q: 6pq=6, 정수 → p=q=±1. f' 최솟값 → p=1. x²+2x+2 는 기약이라 g'=2(x−1), f'=3(x²+2x+2) → m=3 → g'(3)=4.",
    special="① pq=1 에서 p=q=−1 도 가능 — '최솟값' 조건이 p=1 을 고름. ② 일차 인수 (x−1) 은 g' 쪽으로만 감 (f' 은 이차).",
    perspective="도함수 곱의 인수분해로 f', g' 분배.",
    table=[
        ("f' 이 최솟값 (p>0)", "최댓값 (p=q=−1)", "최댓값 M 을 물으면 f'=−3(x²+2x+2), M=−3, g'=−2(x−1) → 8"),
        ("우변 −x³−x²+2", "—", "−x³+2x+4 = −(x−2)(x²+2x+2) 면 g'(3)=2 (생존)"),
    ],
    sweep=["pq=1 → (1,1), (−1,−1)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (정수 조건 pq=1 의 음수 해)",
        changed=["f'(x) 최솟값 m → 최댓값 M, 묻는 값 g'(M)"], naturalness="",
        stem=HEAD + r"함수 $f'(x)$가 최댓값 $M$을 가질 때, $g'(M)$의 값을 구하시오.",
        box=box("-x^3-x^2+2"), answer="8", trap_answer="4",
        trap_path="최고차항 계수를 원문처럼 양수(p=q=1)로 두어 f'=3(x²+2x+2) 의 극값 3 → g'(3)=4 (p=1 이면 최댓값이 없음).",
        explanation=[
            r"(나)에서 $\frac12f'(x)\times\left(-\frac13g'(x)\right)=-x^3-x^2+2$, 즉 $f'(x)g'(x)=6(x-1)(x^2+2x+2)$이다.",
            r"$f$, $g$의 최고차항 계수를 $p$, $q$라 하면 $3p\cdot2q=6$, $pq=1$이고 정수이므로 $p=q=1$ 또는 $p=q=-1$이다.",
            r"함정: $f'(x)$가 최댓값을 가지려면 $3p<0$이므로 $p=q=-1$이다.",
            r"$g'(x)=-2(x-1)$, $f'(x)=-3(x^2+2x+2)$이므로 $M=f'(-1)=-3$이다.",
            r"$g'(-3)=-2\times(-4)=8$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (우변 → −x³+2x+4)",
        changed=["우변 −x³−x²+2 → −x³+2x+4"], naturalness="",
        stem=HEAD + r"함수 $f'(x)$가 최솟값 $m$을 가질 때, $g'(m)$의 값을 구하시오.",
        box=box("-x^3+2x+4"), answer="2", trap_answer=None, trap_path=None,
        explanation=[
            r"$f'(x)g'(x)=6(x^3-2x-4)=6(x-2)(x^2+2x+2)$이다.",
            r"최고차항 계수 $p=q=1$ (최솟값 존재)이고 $g'(x)=2(x-2)$, $f'(x)=3(x^2+2x+2)$이다.",
            r"$m=f'(-1)=3$이므로 $g'(3)=2$이다.",
        ],
    ),
]


def cases(rhs):
    p, q, f2, f1, g1 = symbols('p q f2 f1 g1')
    fp = 3*p*x**2 + 2*f2*x + f1
    gp = 2*q*x + g1
    h = Symbol('h')
    # (나)의 두 극한을 직접 계산 (f, g 는 상수항 0 으로 둬도 무관)
    f = p*x**3 + f2*x**2 + f1*x
    g = q*x**2 + g1*x
    L = limit((f.subs(x, x + h/2) - f)/h, h, 0)*limit((g.subs(x, x - h/3) - g)/h, h, 0)
    eqs = Poly(expand(L - rhs), x).all_coeffs()
    out = []
    for pv in [i for i in range(-12, 13) if i != 0]:  # 최고차 계수 정수 후보 (|6pq|=6 이라 충분)
        for s in solve([e.subs(p, pv) for e in eqs], [q, f2, f1, g1], dict=True):
            if all(v.is_real for v in s.values()) and s[q].is_integer:
                s[p] = pv
                out.append((fp.subs(s), gp.subs(s), pv))
    return out


def verify(c):
    rhs = -x**3 - x**2 + 2
    cs = cases(rhs)
    c.check("원문: 정수 해 두 가지 (p=±1)", sorted(p for _, _, p in cs) == [-1, 1])
    mins = [(fp, gp) for fp, gp, p in cs if p > 0]
    fp, gp = mins[0]
    m = fp.subs(x, solve(diff(fp, x), x)[0])
    c.ans('orig', gp.subs(x, m))
    maxs = [(fp, gp) for fp, gp, p in cs if p < 0]
    c.check("1: 최댓값 갖는 경우 하나", len(maxs) == 1)
    fp, gp = maxs[0]
    M = fp.subs(x, solve(diff(fp, x), x)[0])
    c.ans(1, gp.subs(x, M))
    fp, gp = mins[0]
    c.trap(1, gp.subs(x, fp.subs(x, solve(diff(fp, x), x)[0])))
    cs = cases(-x**3 + 2*x + 4)
    mins = [(fp, gp) for fp, gp, p in cs if p > 0]
    c.check("2: 최솟값 경우 하나", len(mins) == 1)
    fp, gp = mins[0]
    c.ans(2, gp.subs(x, fp.subs(x, solve(diff(fp, x), x)[0])))
