from lib import *

ORIG = dict(
    id="13p-32", chapter=1, page=13, num=32, source="2024년 수능완성 [24054-0096]", type="객관식",
    stem=r"삼차함수 $f(x)$가 $\displaystyle\lim_{x\to1}\frac{f(x)-f(-1)}{x-1}=3$, $\displaystyle\lim_{x\to0}\frac{f(x+1)}{f(x-1)}=-3$을 만족시킬 때, $f(3)$의 값은?",
    choices=["4", "8", "12", "16", "20"], answer="20",
    general="첫 극한: 분모→0 이므로 f(1)=f(−1), 그러면 극한은 f'(1)=3. 둘째: f(1)=f(−1)≠0 이면 비가 1 ≠ −3 → f(1)=f(−1)=0, 0/0 → f'(1)/f'(−1)=−3 → f'(−1)=−1. f=k(x²−1)(x−c): 2k(1−c)=3, 2k(1+c)=−1 → k=½, c=−2 → f(3)=20.",
    special="① 첫 식을 보자마자 f'(1)=3 으로 읽음 — f(−1)=f(1) 을 먼저 확인해야 함. ② 분모가 x−1 이라 (x+1) 같은 대입 인수가 없음(분모가 x²−1 이면 ½ 이 붙음).",
    perspective="두 조건 모두 '분모→0 ⇒ 분자→0' 후 미분계수 비로 바뀌는 구조.",
    table=[
        ("분모 x−1", "대입해야 할 다른 인수", "x²−1 로 바꾸면 (x+1)→2 가 붙어 f'(1)=6"),
        ("둘째 극한값 −3", "비가 1(값이 그대로 통과)인 경우", "−3 ≠ 1 이라 f(±1)=0 강제. 값만 바꾸면 생존"),
        ("삼차함수", "이차(대칭이면 f'(−1)=−f'(1))", "—"),
    ],
    sweep=["둘째 극한값 r=1 이면 f(±1)=0 이 강제되지 않음", "r=−1 이면 k=0 (삼차 불가)"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (둘째 극한값 −3 → 3)",
        changed=["둘째 극한값 −3 → 3"], naturalness="",
        stem=r"삼차함수 $f(x)$가 $\displaystyle\lim_{x\to1}\frac{f(x)-f(-1)}{x-1}=3$, $\displaystyle\lim_{x\to0}\frac{f(x+1)}{f(x-1)}=3$을 만족시킬 때, $f(3)$의 값은?",
        choices=["20", "24", "28", "32", "36"], answer="28", trap_answer=None, trap_path=None,
        explanation=[
            r"첫 극한에서 $f(1)=f(-1)$이고 $f'(1)=3$이다.",
            r"$f(1)=f(-1)\neq0$이면 둘째 극한이 $1$이므로 $f(1)=f(-1)=0$이고 $\frac{f'(1)}{f'(-1)}=3$, $f'(-1)=1$이다.",
            r"$f(x)=k(x^2-1)(x-c)$에서 $2k(1-c)=3$, $2k(1+c)=1$이므로 $k=1$, $c=-\tfrac12$이다.",
            r"$f(3)=8\times\tfrac72=28$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 7 (대입해야 할 인수 x+1)",
        changed=["첫 극한의 분모 x−1 → x²−1"], naturalness="",
        stem=r"삼차함수 $f(x)$가 $\displaystyle\lim_{x\to1}\frac{f(x)-f(-1)}{x^2-1}=3$, $\displaystyle\lim_{x\to0}\frac{f(x+1)}{f(x-1)}=-3$을 만족시킬 때, $f(3)$의 값은?",
        choices=["20", "24", "30", "36", "40"], answer="40", trap_answer="20",
        trap_path="원문처럼 f'(1)=3 으로 두고 (x+1)→2 를 빠뜨림 → 원문 답 20.",
        explanation=[
            r"분모가 $0$으로 가므로 $f(1)=f(-1)$이고, 극한은 $\frac{f'(1)}{2}=3$, 즉 $f'(1)=6$이다.",
            r"함정: 분모의 $x+1$은 $x\to1$에서 $2$로 대입되어야 한다.",
            r"둘째 조건에서 원문과 같이 $f(1)=f(-1)=0$, $\frac{f'(1)}{f'(-1)}=-3$이므로 $f'(-1)=-2$이다.",
            r"$f(x)=k(x^2-1)(x-c)$에서 $2k(1-c)=6$, $2k(1+c)=-2$이므로 $k=1$, $c=-2$이다.",
            r"$f(3)=8\times5=40$이다.",
        ],
    ),
]


def cubics(D1, r2):
    """lim_{x→1}(f(x)−f(−1))/D1 = (주어진 값 v1), lim_{x→0} f(x+1)/f(x−1) = r2 를 만족시키는 삼차함수 목록"""
    cs = symbols('c0:4')
    f = sum(ci*x**i for i, ci in enumerate(cs))
    return f, cs


def solve_cubic(D1, v1, r2):
    cs = symbols('c0:4')
    f = sum(ci*x**i for i, ci in enumerate(cs))
    N1 = f - f.subs(x, -1)
    base = [N1.subs(x, 1), diff(N1, x).subs(x, 1)/diff(D1, x).subs(x, 1) - v1]
    out = []
    # 경우 A: f(−1)≠0 → f(1)/f(−1)=r2 ; 경우 B: f(1)=f(−1)=0 → f'(1)/f'(−1)=r2
    A = base + [f.subs(x, 1) - r2*f.subs(x, -1)]
    B = base + [f.subs(x, 1), f.subs(x, -1), diff(f, x).subs(x, 1) - r2*diff(f, x).subs(x, -1)]
    for eqs, need_nonzero in ((A, True), (B, False)):
        for s in solve(eqs, cs, dict=True):
            F = expand(f.subs(s))
            if need_nonzero and simplify(F.subs(x, -1)) == 0:
                continue  # 경우 A 는 f(−1)≠0 이어야 함
            if F.free_symbols - {x}:
                out.append(('param', F))
                continue
            if Poly(F, x).degree() != 3:
                continue
            ok = limit(((F - F.subs(x, -1))/D1), x, 1) == v1 and limit(F.subs(x, x+1)/F.subs(x, x-1), x, 0) == r2
            if ok:
                out.append(('ok', F))
    return out


def verify(c):
    r = solve_cubic(x - 1, 3, -3)
    c.check("원문: 삼차 해 하나, 매개변수 없음", [k for k, F in r] == ['ok'])
    c.ans('orig', r[0][1].subs(x, 3))
    r = solve_cubic(x - 1, 3, 3)
    c.check("1: 삼차 해 하나", [k for k, F in r] == ['ok'])
    c.ans(1, r[0][1].subs(x, 3))
    r = solve_cubic(x**2 - 1, 3, -3)
    c.check("2: 삼차 해 하나", [k for k, F in r] == ['ok'])
    c.ans(2, r[0][1].subs(x, 3))
    t = solve_cubic(x - 1, 3, -3)  # 함정: 분모를 x−1 로 본 경로 = 원문
    c.trap(2, t[0][1].subs(x, 3))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
