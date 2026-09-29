from lib import *

ORIG = dict(
    id="27p-64", chapter=1, page=27, num=64, source="2020학년도 수능 6월 모의평가 나형 20번", type="객관식",
    stem=r"다음 조건을 만족시키는 모든 다항함수 $f(x)$에 대하여 $f(1)$의 최댓값은? [4점]",
    box=[r"$\displaystyle\lim_{x\to\infty}\frac{f(x)-4x^3+3x^2}{x^{n+1}+1}=6$, $\displaystyle\lim_{x\to0}\frac{f(x)}{x^n}=4$인 자연수 $n$이 존재한다."],
    choices=["12", "13", "14", "15", "16"], answer="14",
    general="n+1>3: f=6x^{n+1}+4x^n → f(1)=10. n+1=3: f=10x³+4x² → 14. n+1=2(n=1): f=4x³+3x²+4x → 11. 최댓값 14.",
    special="① n+1=3 (차수가 맞물리는 경우)만 보고 끝냄 — 원문 수치에서는 이 경우가 최대라 우연히 맞음. 수치가 바뀌면 n=1 이 최대가 될 수 있음.",
    perspective="n 에 따라 (n+1 와 3 의 대소) 세 경우를 모두 계산해 비교.",
    table=[
        ("첫 극한값 6", "n=1 이 최대가 되는 경우", "1 로 바꾸면 n=2: 9, n=1: 12 → n=1 이 최대"),
        ("둘째 극한값 4", "—", "—"),
        ("첫 극한값 6 → 8", "—", "경우별 값만 바뀌고 n=2 가 최대 (생존)"),
    ],
    sweep=["n+1 과 3(4x³ 의 차수)의 대소", "n+1=2 이면 −3x² 항이 합쳐짐"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (x² 항의 부호가 바뀌면 최대가 되는 n 의 경우가 바뀜)",
        changed=["분자 f(x)−4x³+3x² → f(x)−4x³−3x²"], naturalness="",
        stem=r"다음 조건을 만족시키는 모든 다항함수 $f(x)$에 대하여 $f(1)$의 최댓값은?",
        box=[r"$\displaystyle\lim_{x\to\infty}\frac{f(x)-4x^3-3x^2}{x^{n+1}+1}=6$, $\displaystyle\lim_{x\to0}\frac{f(x)}{x^n}=4$인 자연수 $n$이 존재한다."],
        choices=["10", "14", "15", "16", "17"], answer="17", trap_answer="14",
        trap_path="원문처럼 n+1=3 인 경우(f=10x³+4x²)만 계산해 14.",
        explanation=[
            r"$n\ge3$: $f(x)=6x^{n+1}+4x^n$이므로 $f(1)=10$이다.",
            r"$n=2$: 삼차항 계수가 $4+6=10$이므로 $f(x)=10x^3+4x^2$, $f(1)=14$이다.",
            r"$n=1$: $f(x)-4x^3-3x^2$가 최고차항 계수 $6$인 이차식이므로 $f(x)=4x^3+9x^2+4x$, $f(1)=17$이다.",
            r"함정: $x^2$항의 부호가 바뀌어 $n=1$일 때가 가장 크다. 최댓값은 $17$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 3행 (첫 극한값 6 → 8)",
        changed=["첫 극한값 6 → 8"], naturalness="",
        stem=r"다음 조건을 만족시키는 모든 다항함수 $f(x)$에 대하여 $f(1)$의 최댓값은?",
        box=[r"$\displaystyle\lim_{x\to\infty}\frac{f(x)-4x^3+3x^2}{x^{n+1}+1}=8$, $\displaystyle\lim_{x\to0}\frac{f(x)}{x^n}=4$인 자연수 $n$이 존재한다."],
        choices=["12", "13", "14", "15", "16"], answer="16", trap_answer=None, trap_path=None,
        explanation=[
            r"$n\ge3$: $f(x)=8x^{n+1}+4x^n$, $f(1)=12$이다.",
            r"$n=2$: $f(x)=12x^3+4x^2$, $f(1)=16$이다.",
            r"$n=1$: $f(x)=4x^3+5x^2+4x$, $f(1)=13$이다.",
            r"최댓값은 $16$이다.",
        ],
    ),
]


def f_of_n(n, L, B=3):
    D = max(n + 1, 3) + 1
    cs = symbols(f'a0:{D+1}')
    f = sum(ci*x**i for i, ci in enumerate(cs))
    g = expand(f - 4*x**3 + B*x**2)
    eqs = [cs[k] for k in range(n)] + [cs[n] - 4]
    eqs += [Poly(g, x).coeff_monomial(x**k) for k in range(n + 2, D + 1)]
    eqs += [Poly(g, x).coeff_monomial(x**(n + 1)) - L]
    sol = solve(eqs, cs, dict=True)
    F = expand(f.subs(sol[0]))
    free = F.free_symbols - {x}
    F = F.subs({s: 0 for s in free})  # 남는 자유 계수 없음 확인은 아래에서
    ok = (not free) and limit(g.subs(sol[0])/(x**(n + 1) + 1), x, oo) == L and limit(F/x**n, x, 0) == 4
    return F, ok


def max_f1(L, B=3):
    vals = {}
    for n in range(1, 7):
        F, ok = f_of_n(n, L, B)
        if ok:
            vals[n] = F.subs(x, 1)
    return vals


def verify(c):
    v = max_f1(6)
    c.check("원문: n=1,2,3.. 값 {11,14,10}", v[1] == 11 and v[2] == 14 and v[3] == 10)
    c.ans('orig', max(v.values()))
    v = max_f1(6, -3)
    c.check("1: n=1 이 최대", max(v, key=v.get) == 1)
    c.ans(1, max(v.values()))
    c.trap(1, v[2])
    v = max_f1(8)
    c.ans(2, max(v.values()))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
