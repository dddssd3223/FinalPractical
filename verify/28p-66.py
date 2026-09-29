from lib import *
from itertools import product

ORIG = dict(
    id="28p-66", chapter=1, page=28, num=66, source="2015학년도 수능 6월 모의평가 A형 21번", type="객관식",
    stem=r"최고차항의 계수가 $1$인 두 삼차함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $g(5)$의 값은? [4점]",
    box=[r"(가) $g(1)=0$", r"(나) $\displaystyle\lim_{x\to n}\frac{f(x)}{g(x)}=(n-1)(n-2)$ ($n=1,\,2,\,3,\,4$)"],
    choices=["4", "6", "8", "10", "12"], answer="12",
    general="n=1: g(1)=0, 극한 0 → f 가 1 에서 g 보다 높은 차수 → f(1)=f'(1)=0. n=2: 극한 0 이고 g(2)≠0 (g(2)=0 이면 f 가 2 에서도 이중근 필요 → 삼차 불가) → f(2)=0. f=(x−1)²(x−2). n=3,4: g(3)=2, g(4)=3 → g=(x−1)(x²−7x+13), g(5)=12.",
    special="① 극한값이 0 이 아닌 n=3, 4 에서 g(n)≠0 을 당연시 — (가)의 근이 1 이라 성립. g 의 주어진 근이 극한값이 0 이 아닌 점에 있으면 f(n)=0 과 미분계수 비 조건이 필요.",
    perspective="각 n 에서 g 의 근 차수 m 을 경우로 두고 f 의 근 차수와 비교(전수 조사).",
    table=[
        ("(가) g(1)=0 (극한값 0 인 점)", "g 의 주어진 근이 극한값 ≠0 인 점", "g(3)=0 이면 f(3)=0, f'(3)=2g'(3)"),
        ("(나)의 값 (n−1)(n−2)", "—", "부호를 바꾸면 g 만 바뀜 (생존)"),
    ],
    sweep=["g(n)=0 인 n 의 근 차수 m: f 는 차수 ≥m (극한값 0 이면 >m)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (g 의 근이 극한값이 0 이 아닌 점 → 0/0 에서 미분계수 비)",
        changed=["(가) g(1)=0 → g(3)=0"], naturalness="",
        stem=r"최고차항의 계수가 $1$인 두 삼차함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $g(5)$의 값은?",
        box=[r"(가) $g(3)=0$", r"(나) $\displaystyle\lim_{x\to n}\frac{f(x)}{g(x)}=(n-1)(n-2)$ ($n=1,\,2,\,3,\,4$)"],
        choices=["4", "6", "8", "10", "12"], answer="6", trap_answer="8",
        trap_path="원문처럼 f=(x−1)²(x−2) 로 두고 g(4)=3, g'(3)=f'(3)/2=4 로 g 를 구해 8 (이 f 는 f(3)≠0 이라 n=3 극한이 발산).",
        explanation=[
            r"$n=3$: $g(3)=0$이고 극한값이 $2$이므로 $f(3)=0$, $\dfrac{f'(3)}{g'(3)}=2$이다.",
            r"$n=1,\,2$: 극한값이 $0$이고 $g(1)$, $g(2)$가 $0$이면 $f$가 그 점에서 이중근이어야 해 삼차함수가 될 수 없으므로 $f(1)=f(2)=0$이다.",
            r"함정: 원문처럼 $f(x)=(x-1)^2(x-2)$로 두면 $f(3)\neq0$이다. $f(x)=(x-1)(x-2)(x-3)$이다.",
            r"$g(x)=(x-3)(x^2+px+q)$에서 $f'(3)=2=2g'(3)$, $g(4)=\frac{f(4)}6=1$이므로 $9+3p+q=1$, $16+4p+q=1$, $p=-7$, $q=13$이다.",
            r"$g(5)=2\times(25-35+13)=6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 ((나)의 값에 −1 을 곱함)",
        changed=["(나)의 값 (n−1)(n−2) → −(n−1)(n−2)"], naturalness="",
        stem=r"최고차항의 계수가 $1$인 두 삼차함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $g(5)$의 값은?",
        box=[r"(가) $g(1)=0$", r"(나) $\displaystyle\lim_{x\to n}\frac{f(x)}{g(x)}=-(n-1)(n-2)$ ($n=1,\,2,\,3,\,4$)"],
        choices=["4", "6", "8", "10", "12"], answer="4", trap_answer=None, trap_path=None,
        explanation=[
            r"원문과 같이 $f(x)=(x-1)^2(x-2)$이다.",
            r"$n=3$: $\frac{f(3)}{g(3)}=-2$에서 $g(3)=-2$, $n=4$: $\frac{f(4)}{g(4)}=-6$에서 $g(4)=-3$이다.",
            r"$g(x)=(x-1)(x^2+px+q)$에서 $9+3p+q=-1$, $16+4p+q=-1$이므로 $p=-7$, $q=11$이다.",
            r"$g(5)=4\times(25-35+11)=4$이다.",
        ],
    ),
]


def solve66(vals, zero_at, ns=(1, 2, 3, 4)):
    a = symbols('a0:3'); b = symbols('b0:3')
    f = x**3 + a[2]*x**2 + a[1]*x + a[0]
    g = x**3 + b[2]*x**2 + b[1]*x + b[0]
    sols = set()
    for ms in product(range(3), repeat=len(ns)):  # 각 n 에서 g 의 근 차수 가정
        if ms[ns.index(zero_at)] == 0 or sum(ms) > 3:
            continue
        eqs = []
        for n, m, v in zip(ns, ms, vals):
            eqs += [diff(g, x, j).subs(x, n) for j in range(m)]
            if m == 0:
                eqs.append(f.subs(x, n) - v*g.subs(x, n))
            else:
                eqs += [diff(f, x, j).subs(x, n) for j in range(m)]
                eqs.append(diff(f, x, m).subs(x, n) - v*diff(g, x, m).subs(x, n))
        for s in solve(eqs, list(a) + list(b), dict=True):
            F, G = expand(f.subs(s)), expand(g.subs(s))
            if (F + G).free_symbols - {x}:
                sols.add(('param', F, G)); continue
            if all(limit(F/G, x, n) == v for n, v in zip(ns, vals)):
                sols.add(('ok', F, G))
    return sols


def verify(c):
    for key, vals, z in (('orig', [(n - 1)*(n - 2) for n in (1, 2, 3, 4)], 1),
                         (1, [(n - 1)*(n - 2) for n in (1, 2, 3, 4)], 3),
                         (2, [-(n - 1)*(n - 2) for n in (1, 2, 3, 4)], 1)):
        r = solve66(vals, z)
        c.check(f"{key}: 해 하나 (근 차수 경우 전수)", [t for t, F, G in r] == ['ok'])
        c.ans(key, list(r)[0][2].subs(x, 5))
    p, q = symbols('p q')
    Ft = (x - 1)**2*(x - 2)
    Gt = (x - 3)*(x**2 + p*x + q)
    s = solve([Gt.subs(x, 4) - Ft.subs(x, 4)/6, diff(Gt, x).subs(x, 3) - diff(Ft, x).subs(x, 3)/2], [p, q], dict=True)[0]
    c.trap(1, Gt.subs(s).subs(x, 5))
