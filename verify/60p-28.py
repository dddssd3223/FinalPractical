from lib import *

def stem(inf, zero, extra, ask):
    return (r"최고차항의 계수가 $1$인 다항함수 $f(x)$가 $\displaystyle\lim_{x\to\infty}\frac{f(x)}{xf'(x)}=" + inf
            + r"$, $\displaystyle\lim_{x\to0}\frac{f(x)}{xf'(x)}=" + zero + r"$" + extra + r"을 만족시킬 때, $f(" + ask + r")$의 값을 구하시오.")

ORIG = dict(
    id="60p-28", chapter=3, page=60, num=28, source="2025년 수능완성 [25054-0139]", type="주관식",
    stem=stem(r"\frac13", r"\frac13", "", "2"), answer="8",
    general="f 의 최고차 n, 최저차 k (x^k 계수≠0) 이면 x→∞ 에서 f/(xf')→1/n, x→0 에서 →1/k. n=k=3 → f=x³ → f(2)=8.",
    special="① x→0 극한이 1/k 가 되려면 x^k 항 계수가 0 이 아니어야 함 — 계수가 0 이 되는 해는 최저차가 달라져 버려야 함.",
    perspective="f/(xf') 는 최고차항(∞)·최저차항(0)만 보는 식.",
    table=[
        ("최저차 = 최고차 = 3 (한 항뿐)", "최저차 < 최고차 (계수 결정 필요, 계수 0 인 해 제외)", "x→0 값 1/2 이면 f=x³+ax², a≠0 확인 필요"),
        ("극한값 1/3", "—", "둘 다 1/4 이면 f=x⁴ (생존)"),
    ],
    sweep=["1/n 에서 n=최고차, 1/k 에서 k=최저차(계수≠0)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (최저차항 계수가 0 이 되는 해 제외)",
        changed=["x→0 극한값 1/3 → 1/2", "조건 f(1)f(−1)=f(2)−9 추가", "묻는 값 f(2) → f(3)"],
        naturalness="x→0 극한값을 1/2 로 바꾸면 f=x³+ax² 꼴이 되어 a 를 정할 조건이 필요하므로 조건을 하나 추가했고, f(2) 는 조건식에 쓰였으므로 f(3) 을 묻는다.",
        stem=stem(r"\frac13", r"\frac12", r", $f(1)f(-1)=f(2)-9$", "3"), answer="63", trap_answer="27",
        trap_path="f=x³+ax² 에서 a²=4a 의 두 해 중 a=0 을 골라 f=x³ → 27 (a=0 이면 x→0 극한이 1/3 이 되어 조건 위반).",
        explanation=[
            r"$x\to\infty$의 극한이 $\frac13$이므로 $f$는 삼차식, $x\to0$의 극한이 $\frac12$이므로 최저차항은 $x^2$이다.",
            r"$f(x)=x^3+ax^2\ (a\neq0)$로 놓으면 $f(1)f(-1)=a^2-1$, $f(2)-9=4a-1$이다.",
            r"$a^2=4a$에서 $a=0$ 또는 $a=4$이다. 함정: $a=0$이면 $f=x^3$이 되어 $x\to0$ 극한이 $\frac13$이므로 제외한다.",
            r"$f(x)=x^3+4x^2$이므로 $f(3)=27+36=63$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (극한값 1/3 → 1/4)",
        changed=["두 극한값 1/3 → 1/4"], naturalness="두 극한값을 같은 값으로 함께 바꾼 한 가지 변경.",
        stem=stem(r"\frac14", r"\frac14", "", "2"), answer="16", trap_answer=None, trap_path=None,
        explanation=[
            r"$x\to\infty$의 극한 $\frac14$에서 최고차는 $4$, $x\to0$의 극한 $\frac14$에서 최저차도 $4$이다.",
            r"최고차와 최저차가 같으므로 $f$는 한 항뿐이고 최고차항의 계수가 $1$이므로 $f(x)=x^4$이다.",
            r"따라서 $f(2)=16$이다.",
        ],
    ),
]


def candidates(n_inf, n_zero, extra, N=6):
    """최고차 1..N 인 모든 다항식 중 두 극한 조건 + extra(f) 를 만족하는 f 목록"""
    out = []
    for n in range(1, N + 1):
        cs = symbols(f'c0:{n}')
        f = x**n + sum(ci*x**i for i, ci in enumerate(cs))
        if limit(f/(x*diff(f, x)), x, oo) != n_inf:
            continue
        # 최저차 k: c0..c_{k-1}=0, c_k≠0 (k=n 이면 f=x^n)
        for k in range(0, n + 1):
            sub = {cs[i]: 0 for i in range(k)}
            g = f.subs(sub)
            rest = [ci for ci in cs[k:]]
            eqs = [e for e in extra(g)]
            sols = solve(eqs, rest, dict=True) if eqs else [{}]
            for s in sols:
                h = g.subs(s)
                if h.free_symbols - {x}:
                    # 남은 계수가 자유: x^k 계수≠0 이면 x→0 극한은 계수와 무관 → 조건 맞으면 f 가 결정 안 됨
                    if limit(h/(x*diff(h, x)), x, 0) == n_zero:
                        out.append(('free', h))
                    continue
                if limit(h/(x*diff(h, x)), x, 0) == n_zero:
                    out.append(('ok', expand(h)))
    return {h for tag, h in out if tag == 'ok'}, [h for tag, h in out if tag == 'free']


def verify(c):
    s, free = candidates(Rational(1, 3), Rational(1, 3), lambda g: [])
    c.check("원문: f=x³ 유일", s == {x**3} and not [h for h in free if limit(h/(x*diff(h, x)), x, 0) == Rational(1, 3)])
    c.ans("orig", list(s)[0].subs(x, 2))
    extra = lambda g: [g.subs(x, 1)*g.subs(x, -1) - g.subs(x, 2) + 9]
    s, free = candidates(Rational(1, 3), Rational(1, 2), extra)
    c.check("1: f 유일, 자유 계수 없음", len(s) == 1 and not free)
    c.ans(1, list(s)[0].subs(x, 3))
    # 함정: a=0 해
    a = Symbol('a')
    roots = solve((x**3 + a*x**2).subs(x, 1)*(x**3 + a*x**2).subs(x, -1) - (x**3 + a*x**2).subs(x, 2) + 9, a)
    c.check("1: a 후보 {0,4}", set(roots) == {0, 4})
    c.trap(1, (x**3).subs(x, 3))
    s, free = candidates(Rational(1, 4), Rational(1, 4), lambda g: [])
    c.check("2: f=x⁴ 유일", s == {x**4})
    c.ans(2, list(s)[0].subs(x, 2))
