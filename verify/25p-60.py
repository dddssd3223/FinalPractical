from lib import *

ORIG = dict(
    id="25p-60", chapter=1, page=25, num=60, source="2017학년도 수능 나형 18번", type="객관식",
    stem=r"최고차항의 계수가 $1$인 이차함수 $f(x)$가 $\displaystyle\lim_{x\to a}\frac{f(x)-(x-a)}{f(x)+(x-a)}=\frac35$을 만족시킨다. 방정식 $f(x)=0$의 두 근을 $\alpha$, $\beta$라 할 때, $|\alpha-\beta|$의 값은? (단, $a$는 상수이다.) [4점]",
    choices=["1", "2", "3", "4", "5"], answer="4",
    general="f(a)≠0 이면 극한 1 ≠ 3/5 → f(a)=0, f=(x−a)(x−b). 약분: (x−b−1)/(x−b+1) → (d−1)/(d+1)=3/5 (d=a−b) → d=4 → |α−β|=4.",
    special="① f=(x−a)(x−b) 로 바로 둠 — 극한값이 1 이 아니라서 f(a)=0 이 강제된 것. ② 최고차 계수 1 이라 약분 뒤 d−1, d+1 꼴(계수 k 면 kd−1, kd+1).",
    perspective="값이 1 이 아닌 이유로 분모·분자 공통근 강제 → 약분 후 대입.",
    table=[
        ("최고차 계수 1", "계수 k≠1", "2 로 바꾸면 (2d−1)/(2d+1)=3/5 → d=2"),
        ("극한값 3/5 (≠1)", "f(a)≠0 인 경우(값 1)", "값만 바꾸면 d 만 바뀜 (생존). 값 1 이면 결정 불가"),
    ],
    sweep=["극한값 r=1 이면 f(a)=0 이 강제되지 않음", "r=−1 이면 d=0 (중근)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (최고차 계수가 약분 뒤 식에 남음)",
        changed=["최고차항의 계수 1 → 2"], naturalness="",
        stem=r"최고차항의 계수가 $2$인 이차함수 $f(x)$가 $\displaystyle\lim_{x\to a}\frac{f(x)-(x-a)}{f(x)+(x-a)}=\frac35$을 만족시킨다. 방정식 $f(x)=0$의 두 근을 $\alpha$, $\beta$라 할 때, $|\alpha-\beta|$의 값은? (단, $a$는 상수이다.)",
        choices=["1", "2", "3", "4", "5"], answer="2", trap_answer="4",
        trap_path="약분 후 원문처럼 (d−1)/(d+1) 로 두어 d=4 (계수 2 를 빠뜨림).",
        explanation=[
            r"$f(a)\neq0$이면 극한이 $1$이므로 $f(a)=0$, $f(x)=2(x-a)(x-b)$이다.",
            r"$(x-a)$로 약분하면 $\dfrac{2(x-b)-1}{2(x-b)+1}\to\dfrac{2d-1}{2d+1}$ ($d=a-b$)이다.",
            r"함정: 최고차항의 계수 $2$가 약분 뒤에도 남는다.",
            r"$\dfrac{2d-1}{2d+1}=\dfrac35$에서 $d=2$이므로 $|\alpha-\beta|=2$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (극한값 3/5 → 5/7)",
        changed=["극한값 3/5 → 5/7"], naturalness="",
        stem=r"최고차항의 계수가 $1$인 이차함수 $f(x)$가 $\displaystyle\lim_{x\to a}\frac{f(x)-(x-a)}{f(x)+(x-a)}=\frac57$을 만족시킨다. 방정식 $f(x)=0$의 두 근을 $\alpha$, $\beta$라 할 때, $|\alpha-\beta|$의 값은? (단, $a$는 상수이다.)",
        choices=["2", "4", "6", "8", "10"], answer="6", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(a)\neq0$이면 극한이 $1$이므로 $f(a)=0$, $f(x)=(x-a)(x-b)$이다.",
            r"약분하면 $\dfrac{d-1}{d+1}=\dfrac57$ ($d=a-b$)이다.",
            r"$d=6$이므로 $|\alpha-\beta|=6$이다.",
        ],
    ),
]


def solve_d(k, r):
    a, b, cc = symbols('a b cc', real=True)
    f = k*x**2 + b*x + cc
    out = set()
    # 경우 A: f(a)≠0 → 극한 1
    if r == 1:
        return None
    # 경우 B: f(a)=0
    bb = Symbol('bb', real=True)
    f = k*(x - a)*(x - bb)
    L = limit((f - (x - a))/(f + (x - a)), x, a)
    for s in solve(Eq(L, r), bb):
        out.add(simplify(Abs(a - s)))
    return out


def verify(c):
    for key, k, r in (('orig', 1, Rational(3, 5)), (1, 2, Rational(3, 5)), (2, 1, Rational(5, 7))):
        d = solve_d(k, r)
        c.check(f"{key}: |α−β| 하나", d is not None and len(d) == 1)
        c.ans(key, list(d)[0])
    c.trap(1, list(solve_d(1, Rational(3, 5)))[0])


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[0]['drop'] = '계수 2 누락뿐 — 원문 풀이(약분)가 그대로 통함'
