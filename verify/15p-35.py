from lib import *

ORIG = dict(
    id="15p-35", chapter=1, page=15, num=35, source="2024년 수능특강 [24009-0022]", type="주관식",
    stem=r"삼차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(-3)$의 값을 구하시오.",
    box=[r"(가) 집합 $\{-1,\,1,\,2\}$의 모든 원소 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{xf(x)-2a}{x-a}$의 값이 존재한다.",
         r"(나) $\displaystyle\lim_{x\to3}\frac{x-1}{f(x)}=-1$"],
    answer="22",
    general="분모→0 이므로 af(a)=2a, a≠0 이라 f(a)=2 (a=−1,1,2). f−2=k(x+1)(x−1)(x−2). (나): f(3)=−2 (분자 2≠0) → 2+8k=−2, k=−½. f(−3)=2+(−½)(−2)(−4)(−5)=22.",
    special="① af(a)=2a 에서 a 로 나누는 단계 — 집합에 0 이 있으면 그 원소는 정보를 주지 않음. ② 분모가 x−a 라 a=0 이어도 같은 꼴이라고 생각하는 것.",
    perspective="각 원소에서 '분모의 근 차수 ≤ 분자의 근 차수' 를 따로 적용.",
    table=[
        ("집합 원소가 모두 0 아님", "a=0 (a f(a)=2a 가 0=0)", "0 을 넣으면 정보가 하나 줄거나(분모 x−a), 다른 정보(f(0)=0, 분모 x²−a²)가 생김"),
        ("(나)의 분자 x−1 이 x=3 에서 2", "f(3)=0 (발산)", "값만 바꾸면 k 만 바뀜 (생존)"),
    ],
    sweep=["a=0: 분자·분모 모두 a 배", "분모를 x²−a² 로 바꾸면 a=0 에서 분모 차수 2"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 1 (a=0 에서는 a 로 나눌 수 없음)",
        changed=["집합 {−1, 1, 2} → {−1, 0, 2}", "분모 x−a → x²−a²"],
        naturalness="0 을 넣으면 분모 x−a 로는 정보가 사라져 문제가 성립하지 않음 → 분모를 x²−a² 로 바꿔 a=0 이 다른 정보(f(0)=0)를 주게 한 것은 필수.",
        stem=r"삼차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(-3)$의 값을 구하시오.",
        box=[r"(가) 집합 $\{-1,\,0,\,2\}$의 모든 원소 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{xf(x)-2a}{x^2-a^2}$의 값이 존재한다.",
             r"(나) $\displaystyle\lim_{x\to3}\frac{x-1}{f(x)}=-1$"],
        answer="32", trap_answer="12",
        trap_path="a=0 에도 f(a)=2 를 적용해 f−2=kx(x+1)(x−2) → k=−⅓ → f(−3)=12.",
        explanation=[
            r"$a=-1,\,2$일 때 분모가 $0$으로 가므로 $af(a)=2a$, 즉 $f(-1)=f(2)=2$이다.",
            r"함정: $a=0$이면 조건은 $\displaystyle\lim_{x\to0}\frac{xf(x)}{x^2}=\lim_{x\to0}\frac{f(x)}{x}$의 존재, 즉 $f(0)=0$이다. $f(0)=2$가 아니다.",
            r"$f(x)-2=(x+1)(x-2)(px+q)$에 $f(0)=0$을 넣으면 $q=1$이다.",
            r"(나)에서 $f(3)=-2$이므로 $2+4(3p+1)=-2$, $p=-\tfrac23$이다.",
            r"$f(-3)=2+(-2)(-5)(2+1)=32$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 ((나)의 극한값 −1 → −1/3)",
        changed=["(나)의 극한값 −1 → −1/3"], naturalness="",
        stem=r"삼차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(-3)$의 값을 구하시오.",
        box=[r"(가) 집합 $\{-1,\,1,\,2\}$의 모든 원소 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{xf(x)-2a}{x-a}$의 값이 존재한다.",
             r"(나) $\displaystyle\lim_{x\to3}\frac{x-1}{f(x)}=-\frac13$"],
        answer="42", trap_answer=None, trap_path=None,
        explanation=[
            r"각 원소 $a$에서 분모가 $0$으로 가므로 $af(a)=2a$, $a\neq0$이라 $f(a)=2$이다.",
            r"$f(x)-2=k(x+1)(x-1)(x-2)$로 둔다.",
            r"(나)에서 $\frac{2}{f(3)}=-\frac13$, $f(3)=-6$이므로 $2+8k=-6$, $k=-1$이다.",
            r"$f(-3)=2+(-1)(-2)(-4)(-5)=42$이다.",
        ],
    ),
]


def order_at(expr, a):
    n = 0
    while simplify(expr.subs(x, a)) == 0 and n < 6:
        expr = diff(expr, x); n += 1
    return n


def solve_f(S, D, v):
    cs = symbols('c0:4')
    f = sum(ci*x**i for i, ci in enumerate(cs))
    eqs = []
    for a in S:
        N = x*f - 2*a
        d = order_at(D(a), a)
        eqs += [diff(N, x, j).subs(x, a) for j in range(d)]
    eqs.append(2 - v*f.subs(x, 3))  # f(3)≠0 이어야 극한 존재(분자 2)
    out = []
    for s in solve(eqs, cs, dict=True):
        F = expand(f.subs(s))
        out.append(F)
    return out


def check_all(F, S, D, v):
    ok = all(lim_exists((x*F - 2*a)/D(a), a)[0] for a in S)
    return ok and limit((x - 1)/F, x, 3) == v and Poly(F, x).degree() == 3


def verify(c):
    S, D = [-1, 1, 2], (lambda a: x - a)
    r = solve_f(S, D, -1)
    c.check("원문: 해 하나, 조건 재확인", len(r) == 1 and check_all(r[0], S, D, -1))
    c.ans('orig', r[0].subs(x, -3))

    S, D = [-1, 0, 2], (lambda a: x**2 - a**2)
    r = solve_f(S, D, -1)
    c.check("1: 해 하나, 조건 재확인", len(r) == 1 and not (r[0].free_symbols - {x}) and check_all(r[0], S, D, -1))
    c.check("1: f(0)=0", r[0].subs(x, 0) == 0)
    c.ans(1, r[0].subs(x, -3))
    k = Symbol('k')
    ft = 2 + k*x*(x + 1)*(x - 2)
    kt = solve(Eq(ft.subs(x, 3), -2), k)[0]
    c.trap(1, ft.subs(k, kt).subs(x, -3))

    S, D = [-1, 1, 2], (lambda a: x - a)
    r = solve_f(S, D, -Rational(1, 3))
    c.check("2: 해 하나, 조건 재확인", len(r) == 1 and check_all(r[0], S, D, -Rational(1, 3)))
    c.ans(2, r[0].subs(x, -3))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
