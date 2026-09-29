from lib import *

F_TXT = r"f(x)=\begin{cases}x+3 & (x<a)\\ 3x-4 & (x\ge a)\end{cases}"

def stem(g):
    return r"두 함수 $" + F_TXT + r"$, $g(x)=" + g + r"$에 대하여 함수 $f(x)g(x)$가 실수 전체의 집합에서 연속이 되도록 하는 모든 실수 $a$의 값의 합은?"

ORIG = dict(
    id="34p-12", chapter=2, page=34, num=12, source="2024년 수능완성 [24054-0104]", type="객관식",
    stem=stem("x^2+ax+a-1"), choices=["3", "7/2", "4", "9/2", "5"], answer="3",
    general="x=a 에서 f 의 좌 a+3, 우 3a−4. (i) f 가 연속: a=7/2. (ii) g(a)=0: 2a²+a−1=0 → a=½, −1. 합 7/2+½−1=3.",
    special="① (i)과 (ii)를 따로 모아 더함 — 두 경우의 a 가 겹치지 않아 통함. 겹치면 한 번만 세야 함.",
    perspective="곱이 연속 ⇔ (f 연속) 또는 (g(a)=0).",
    table=[
        ("g(a)=2a²+a−1 의 근 ½, −1", "(i)의 a=7/2 와 겹치는 경우", "g=x²+ax−5a−7 이면 근 7/2, −1 → 7/2 중복"),
        ("g 의 상수항 a−1", "—", "−3 이면 근 ±√(3/2) (생존)"),
    ],
    sweep=["(i) a=7/2 가 g(a)=0 의 근인지"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 6 (두 경우의 a 가 겹침)",
        changed=["g=x²+ax+a−1 → x²+ax−5a−7"], naturalness="",
        stem=stem("x^2+ax-5a-7"), choices=["5/2", "3", "7/2", "5", "6"], answer="5/2", trap_answer="6",
        trap_path="(i)의 7/2 와 (ii)의 근 7/2, −1 을 모두 더해 6 (7/2 중복).",
        explanation=[
            r"$x=a$에서 $f$의 좌극한 $a+3$, 함숫값 $3a-4$이다.",
            r"(i) $f$가 연속: $a+3=3a-4$, $a=\frac72$.",
            r"(ii) $g(a)=0$: $2a^2-5a-7=0$, $(2a-7)(a+1)=0$, $a=\frac72$ 또는 $-1$.",
            r"함정: $\frac72$는 두 경우에 모두 나오지만 한 번만 센다. 합은 $\frac72+(-1)=\frac52$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (g 의 상수항 a−1 → −3)",
        changed=["g=x²+ax+a−1 → x²+ax−3"], naturalness="",
        stem=stem("x^2+ax-3"), choices=["3", "7/2", "4", "9/2", "5"], answer="7/2", trap_answer=None, trap_path=None,
        explanation=[
            r"(i) $f$가 $x=a$에서 연속: $a=\frac72$.",
            r"(ii) $g(a)=2a^2-3=0$: $a=\pm\sqrt{\frac32}$, 두 값의 합은 $0$.",
            r"모든 $a$의 합은 $\frac72$이다.",
        ],
    ),
]


def good_as(gexpr):
    a = Symbol('a', real=True)
    cands = set(solve(Eq(a + 3, 3*a - 4), a)) | set(solve(gexpr.subs(x, a), a))
    good = set()
    for av in cands:
        g = gexpr.subs(a, av)
        l = limit((x + 3)*g, x, av, '-'); r = limit((3*x - 4)*g, x, av, '+')
        v = ((3*x - 4)*g).subs(x, av)
        if simplify(l - r) == 0 and simplify(l - v) == 0:
            good.add(simplify(av))
    # 후보 밖 점검: 임의의 a 에서는 불연속
    for av in (Rational(1, 3), 2, -3):
        g = gexpr.subs(a, av)
        assert simplify(limit((x + 3)*g, x, av, '-') - ((3*x - 4)*g).subs(x, av)) != 0
    return good, a


def verify(c):
    a = Symbol('a', real=True)
    g, _ = good_as(x**2 + a*x + a - 1)
    c.check("원문: {7/2, 1/2, −1}", g == {Rational(7, 2), Rational(1, 2), -1})
    c.ans('orig', sum(g))
    g, _ = good_as(x**2 + a*x - 5*a - 7)
    c.check("1: {7/2, −1}", g == {Rational(7, 2), -1})
    c.ans(1, sum(g))
    c.trap(1, Rational(7, 2) + Rational(7, 2) - 1)
    g, _ = good_as(x**2 + a*x - 3)
    c.ans(2, simplify(sum(g)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
