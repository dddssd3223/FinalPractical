from lib import *

def stem(l, r, g):
    return (r"두 함수 $f(x)=\begin{cases}" + l + r" & (x\le a)\\ " + r + r" & (x>a)\end{cases}$, $g(x)=" + g + r"$에 대하여 함수 $f(x)g(x)$가 실수 전체의 집합에서 연속이 되도록 하는 모든 실수 $a$의 값의 곱을 구하시오.")

ORIG = dict(
    id="46p-45", chapter=2, page=46, num=45, source="2016학년도 대수능 A형 27번", type="주관식",
    stem=stem("x+3", "x^2-x", "x-(2a+7)") + " [4점]", answer="21",
    general="x=a 에서 (i) f 연속: a+3=a²−a → a=3, −1. (ii) g(a)=0: a−(2a+7)=0 → a=−7. 곱 3·(−1)·(−7)=21.",
    special="① (i), (ii)의 a 를 모두 곱함 — 서로 겹치지 않아 통함.",
    perspective="곱이 연속 ⇔ f 연속 또는 g(a)=0.",
    table=[
        ("(ii)의 근 −7 이 (i)과 다름", "(ii)의 근이 (i)의 근과 같은 경우", "겹치면 한 번만 곱해야 함"),
        ("g 의 상수 2a+7", "—", "2a+5 면 a=−5 (생존)"),
    ],
    sweep=["(ii)의 근이 (i)의 근과 일치하는지"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 6 (두 경우의 a 가 겹침)",
        changed=["f 의 두 조각 5x−6, x²", "g=x−(2a−3)"],
        naturalness="(i)의 두 근을 양수(2, 3)로 두고 (ii)의 근을 그중 하나(3)에 맞춘 것 — 겹침을 만들기 위한 한 묶음의 변경.",
        stem=stem("5x-6", "x^2", "x-(2a-3)"), answer="6", trap_answer="18",
        trap_path="(i)의 2, 3 과 (ii)의 3 을 모두 곱해 18 (3 중복).",
        explanation=[
            r"$x=a$에서 $f$의 좌극한(함숫값) $5a-6$, 우극한 $a^2$이다.",
            r"(i) $f$가 연속: $a^2=5a-6$, $a=2$ 또는 $3$.",
            r"(ii) $g(a)=a-(2a-3)=3-a=0$: $a=3$.",
            r"함정: $a=3$은 두 경우에 모두 나오므로 한 번만 곱한다. 곱은 $2\times3=6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (g=x−(2a+5))",
        changed=["g=x−(2a+7) → x−(2a+5)"], naturalness="",
        stem=stem("x+3", "x^2-x", "x-(2a+5)"), answer="15", trap_answer=None, trap_path=None,
        explanation=[
            r"(i) $f$가 연속: $a+3=a^2-a$, $a=3$ 또는 $-1$.",
            r"(ii) $g(a)=-a-5=0$: $a=-5$.",
            r"곱은 $3\times(-1)\times(-5)=15$이다.",
        ],
    ),
]


def good(L, R, G):
    a = Symbol('a', real=True)
    cands = set(solve(Eq(L.subs(x, a), R.subs(x, a)), a)) | set(solve(G.subs(x, a), a))
    out = set()
    for av in cands:
        Ls, Rs, Gs = L.subs(a, av), R.subs(a, av), G.subs(a, av)
        l = limit(Ls*Gs, x, av, '-'); r = limit(Rs*Gs, x, av, '+'); v = (Ls*Gs).subs(x, av)
        if simplify(l - r) == 0 and simplify(l - v) == 0:
            out.add(av)
    return out


def verify(c):
    a = Symbol('a', real=True)
    g = good(x + 3, x**2 - x, x - (2*a + 7))
    c.check("원문: {3, −1, −7}", g == {3, -1, -7})
    c.ans('orig', prod(g))
    g = good(5*x - 6, x**2, x - (2*a - 3))
    c.check("1: {2, 3}", g == {2, 3})
    c.ans(1, prod(g))
    c.trap(1, 2*3*3)
    g = good(x + 3, x**2 - x, x - (2*a + 5))
    c.ans(2, prod(g))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='-3', trap_path='f 가 연속인 a=3, −1 만 곱해 −3 (g(a)=0 이면 f 가 끊겨도 fg 는 연속 → a=−5 추가).')
VARS[1]['explanation'].insert(-1, '함정: $f$가 끊겨도 $g(a)=0$이면 $fg$는 연속이다.')
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, prod(solve(Symbol('t') + 3 - (Symbol('t')**2 - Symbol('t')), Symbol('t'))))
