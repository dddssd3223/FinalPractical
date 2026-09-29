from lib import *

ORIG = dict(
    id="23p-55", chapter=1, page=23, num=55, source="2020학년도 수능 9월 모의평가 16번", type="객관식",
    stem=r"다항함수 $f(x)$가 $\displaystyle\lim_{x\to\infty}\frac{f(x)}{x^3}=1$, $\displaystyle\lim_{x\to-1}\frac{f(x)}{x+1}=2$를 만족시킨다. $f(1)\le12$일 때, $f(2)$의 최댓값은? [4점]",
    choices=["27", "30", "33", "36", "39"], answer="33",
    general="f 는 최고차 1 삼차, f(−1)=0, f'(−1)=2 → f=(x+1)(x²+px+q), 1−p+q=2 → q=p+1. f(1)=4p+4≤12 → p≤2. f(2)=9p+15 (p 에 대해 증가) → 33.",
    special="① 두 번째 극한을 곧바로 f'(−1)=2 로 — 분모가 x+1 이라 그대로. 분모가 x²−1 이면 (x−1)→−2 가 붙음. ② f(2) 가 p 의 증가함수임을 확인하지 않고 경계 대입.",
    perspective="f(x)=(x+1)(x²+px+p+1) 에서 p 의 계수가 (x+1)² ≥ 0 이라 모든 f(x) 가 p 에 대해 증가.",
    table=[
        ("분모 x+1", "대입할 다른 인수", "x²−1 로 바꾸면 f'(−1)/(−2)=2 → f'(−1)=−4"),
        ("f(1)≤12", "—", "상한만 바꾸면 p 의 범위만 바뀜 (생존)"),
    ],
    sweep=["p 의 계수 (x+1)²: 모든 x 에서 f(x) 가 p 에 대해 비감소"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 7 (분모의 다른 인수 x−1 → −2 로 대입, 부호 포함)",
        changed=["둘째 극한의 분모 x+1 → x²−1"], naturalness="",
        stem=r"다항함수 $f(x)$가 $\displaystyle\lim_{x\to\infty}\frac{f(x)}{x^3}=1$, $\displaystyle\lim_{x\to-1}\frac{f(x)}{x^2-1}=2$를 만족시킨다. $f(1)\le12$일 때, $f(2)$의 최댓값은?",
        choices=["30", "33", "36", "39", "42"], answer="42", trap_answer="30",
        trap_path="x−1 을 +2 로 대입해 f'(−1)=4 → q=p+3, p≤1 → 30.",
        explanation=[
            r"$f$는 최고차항의 계수가 $1$인 삼차함수이고 $f(-1)=0$이다.",
            r"$\displaystyle\lim_{x\to-1}\frac{f(x)}{(x+1)(x-1)}=\frac{f'(-1)}{-2}=2$이므로 $f'(-1)=-4$이다. 함정: $x-1\to-2$의 부호.",
            r"$f(x)=(x+1)(x^2+px+q)$에서 $1-p+q=-4$, $q=p-5$이다.",
            r"$f(1)=2(2p-4)\le12$에서 $p\le5$이고, $f(2)=3(3p-1)$은 $p$에 대해 증가한다.",
            r"$f(2)$의 최댓값은 $p=5$일 때 $42$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (f(1)≤12 → f(1)≤20)",
        changed=["f(1)≤12 → f(1)≤20"], naturalness="",
        stem=r"다항함수 $f(x)$가 $\displaystyle\lim_{x\to\infty}\frac{f(x)}{x^3}=1$, $\displaystyle\lim_{x\to-1}\frac{f(x)}{x+1}=2$를 만족시킨다. $f(1)\le20$일 때, $f(2)$의 최댓값은?",
        choices=["42", "45", "48", "51", "54"], answer="51", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)=(x+1)(x^2+px+q)$이고 $f'(-1)=1-p+q=2$에서 $q=p+1$이다.",
            r"$f(1)=4p+4\le20$에서 $p\le4$이다.",
            r"$f(2)=3(3p+5)$는 $p$에 대해 증가하므로 최댓값은 $p=4$일 때 $51$이다.",
        ],
    ),
]


def max_f2(D, bound):
    p, q = symbols('p q', real=True)
    f = (x + 1)*(x**2 + p*x + q)
    L = limit(f/D, x, -1)
    qs = solve(Eq(L, 2), q)[0]
    fs = f.subs(q, qs)
    c1 = limit(fs/x**3, x, oo) == 1
    pmax = solve(Eq(fs.subs(x, 1), bound), p)[0]
    f2 = expand(fs.subs(x, 2))
    inc = Poly(f2, p).coeff_monomial(p) > 0 and Poly(fs.subs(x, 1), p).coeff_monomial(p) > 0
    return c1 and inc, f2.subs(p, pmax)


def verify(c):
    ok, v = max_f2(x + 1, 12)
    c.check("원문: f(1), f(2) 모두 p 에 대해 증가", ok)
    c.ans('orig', v)
    ok, v = max_f2(x**2 - 1, 12)
    c.check("1: 단조성", ok)
    c.ans(1, v)
    # 함정: f'(−1)/(+2)=2 → f'(−1)=4
    p, q = symbols('p q', real=True)
    f = (x + 1)*(x**2 + p*x + q)
    qs = solve(Eq(diff(f, x).subs(x, -1), 4), q)[0]
    fs = f.subs(q, qs)
    pm = solve(Eq(fs.subs(x, 1), 12), p)[0]
    c.trap(1, fs.subs(x, 2).subs(p, pm))
    ok, v = max_f2(x + 1, 20)
    c.check("2: 단조성", ok)
    c.ans(2, v)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
