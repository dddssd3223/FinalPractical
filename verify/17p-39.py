from lib import *
from itertools import product

A_TXT = r"A=\left\{a\,\middle|\,\displaystyle\lim_{x\to a}\frac{x^3(x-1)}{f(x)}\text{의 값이 존재한다.}\right\}"
B_TXT = r"B=\left\{b\,\middle|\,\displaystyle\lim_{x\to b}\frac{f(x)}{x^2(x-1)^4}\text{의 값이 존재하지 않는다.}\right\}"

ORIG = dict(
    id="17p-39", chapter=1, page=17, num=39, source="2022년 수능특강 [22009-0024]", type="주관식",
    stem=r"두 실수 $a$, $b$와 최고차항의 계수가 $1$인 오차함수 $f(x)$에 대하여 두 집합 $A$, $B$를 각각 $" + A_TXT + r"$, $" + B_TXT + r"$라 하자. $0\in(A-B)$, $1\in(B-A)$이고 $\displaystyle\lim_{x\to3}f(x)=18$일 때, $f(4)$의 값을 구하시오.",
    answer="216",
    general="x=0 의 근 차수 m₀: 0∈A ⇔ m₀≤3, 0∉B ⇔ m₀≥2. x=1 의 근 차수 m₁: 1∈B ⇔ m₁<4, 1∉A ⇔ m₁>1. 오차식이므로 (m₀,m₁)=(2,2),(2,3),(3,2) → 한꺼번에 f=x²(x−1)²(x−c). f(3)=36(3−c)=18 → c=5/2, f(4)=216.",
    special="① 곧바로 f=x²(x−1)²(x−c) 로 둠 — 오차라 남는 인수가 일차 하나여서 (2,3),(3,2) 가 c=1, c=0 으로 흡수됨(차수가 바뀌면 깨짐). ② 극한 존재를 '분모 근 차수 ≤ 분자 근 차수' 로 읽는 것은 일반적.",
    perspective="근 차수 부등식으로 집합 조건을 번역하면 차수 제한이 경우를 결정한다.",
    table=[
        ("오차함수", "남는 인수가 없거나 둘 이상인 경우", "사차면 f=x²(x−1)² 로 완전히 결정 → (x−c) 를 붙이면 틀림"),
        ("f(3)=18", "c 가 0 이나 1 인 경우", "값만 바꾸면 c 만 바뀜 (생존)"),
        ("0∈A−B, 1∈B−A", "반대 소속 (모순)", "—"),
    ],
    sweep=["m₀∈{2,3}, m₁∈{2,3}, m₀+m₁≤차수", "c=0 → (3,2), c=1 → (2,3)"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (f(3)=18 → 36)",
        changed=["lim_{x→3} f(x)=18 → 36"], naturalness="",
        stem=r"두 실수 $a$, $b$와 최고차항의 계수가 $1$인 오차함수 $f(x)$에 대하여 두 집합 $A$, $B$를 각각 $" + A_TXT + r"$, $" + B_TXT + r"$라 하자. $0\in(A-B)$, $1\in(B-A)$이고 $\displaystyle\lim_{x\to3}f(x)=36$일 때, $f(4)$의 값을 구하시오.",
        answer="288", trap_answer=None, trap_path=None,
        explanation=[
            r"$x=0$에서의 근의 차수를 $m_0$라 하면 $0\in A$에서 $m_0\le3$, $0\notin B$에서 $m_0\ge2$이다.",
            r"$x=1$에서의 근의 차수를 $m_1$이라 하면 $1\in B$에서 $m_1<4$, $1\notin A$에서 $m_1>1$이다.",
            r"오차함수이므로 $f(x)=x^2(x-1)^2(x-c)$ 꼴이다.",
            r"$f(3)=36(3-c)=36$에서 $c=2$이므로 $f(4)=16\times9\times2=288$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 9 (차수가 바뀌면 남는 인수가 없음)",
        changed=["오차함수 → 사차함수"], naturalness="",
        stem=r"두 실수 $a$, $b$와 최고차항의 계수가 $1$인 사차함수 $f(x)$에 대하여 두 집합 $A$, $B$를 각각 $" + A_TXT + r"$, $" + B_TXT + r"$라 하자. $0\in(A-B)$, $1\in(B-A)$이고 $\displaystyle\lim_{x\to3}f(x)=36$일 때, $f(4)$의 값을 구하시오.",
        answer="144", trap_answer="288",
        trap_path="원문처럼 f=x²(x−1)²(x−c) 로 두고 f(3)=36 에서 c=2 → 288 (그러면 오차함수가 되어 조건 위반).",
        explanation=[
            r"원문과 같이 $m_0\in\{2,3\}$, $m_1\in\{2,3\}$이다.",
            r"사차함수이므로 $m_0+m_1\le4$, 즉 $m_0=m_1=2$이고 $f(x)=x^2(x-1)^2$이다.",
            r"함정: 원문처럼 인수 $(x-c)$를 하나 더 붙이면 오차함수가 된다.",
            r"$f(3)=9\times4=36$으로 조건과 맞고, $f(4)=16\times9=144$이다.",
        ],
    ),
]


def mult(F, r):
    n = 0
    while n < 7 and simplify(F.subs(x, r)) == 0:
        F = diff(F, x); n += 1
    return n


def conds_ok(F):
    inA = lambda a: lim_exists(x**3*(x - 1)/F, a)[0]
    inB = lambda b: not lim_exists(F/(x**2*(x - 1)**4), b)[0]
    return inA(0) and not inB(0) and inB(1) and not inA(1)


def candidates(deg, v):
    """근 차수 경우를 전수: f=x^m0 (x−1)^m1 · (최고차 1, 0·1 이 아닌 근을 갖는 나머지)"""
    out = set()
    for m0, m1 in product(range(0, deg + 1), repeat=2):
        rest = deg - m0 - m1
        if rest < 0:
            continue
        if rest == 0:
            F = x**m0*(x - 1)**m1
            if F.subs(x, 3) == v:
                out.add(expand(F))
        elif rest == 1:
            cc = Symbol('cc')
            F = x**m0*(x - 1)**m1*(x - cc)
            for s in solve(Eq(F.subs(x, 3), v), cc):
                if s not in (0, 1):
                    out.add(expand(F.subs(cc, s)))
    return {F for F in out if conds_ok(F) and mult(F, 0) >= 0}


def verify(c):
    r = candidates(5, 18)
    c.check("원문: 해 하나", len(r) == 1)
    c.ans('orig', list(r)[0].subs(x, 4))
    r = candidates(5, 36)
    c.check("1: 해 하나", len(r) == 1)
    c.ans(1, list(r)[0].subs(x, 4))
    r = candidates(4, 36)
    c.check("2: 해 하나 x²(x−1)²", r == {expand(x**2*(x - 1)**2)})
    c.ans(2, list(r)[0].subs(x, 4))
    cc = Symbol('cc')
    Ft = x**2*(x - 1)**2*(x - cc)
    c.trap(2, Ft.subs(cc, solve(Eq(Ft.subs(x, 3), 36), cc)[0]).subs(x, 4))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
