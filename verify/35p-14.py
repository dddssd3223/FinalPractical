from lib import *

F_TXT = r"f(x)=\begin{cases}-x+3 & (x<-1)\\ 3x+a & (x\ge-1)\end{cases}"

def stem(g):
    return r"두 함수 $" + F_TXT + r"$, $g(x)=" + g + r"$에 대하여 함수 $f(x)g(x)$가 실수 전체의 집합에서 연속이 되도록 하는 모든 실수 $a$의 값의 합은?"

ORIG = dict(
    id="35p-14", chapter=2, page=35, num=14, source="2025년 수능완성 [25054-0125]", type="객관식",
    stem=stem("-x^2+4x+a"), choices=["11", "12", "13", "14", "15"], answer="12",
    general="x=−1 에서 f 의 좌 4, 우 a−3. (i) f 연속: a=7. (ii) g(−1)=a−5=0: a=5. 합 12.",
    special="① 두 경우를 따로 구해 더함 — 두 경우의 a 가 달라서 통함.",
    perspective="곱이 연속 ⇔ f 연속 또는 g(−1)=0.",
    table=[
        ("g(−1)=a−5 (일차)", "g(−1)=0 의 근이 (i)의 7 과 겹치는 경우", "g 의 상수항을 a²−4a−16 으로 바꾸면 근 7, −3 → 7 중복"),
        ("g=−x²+4x+a", "—", "−x²+2x+a 면 a=3 (생존)"),
    ],
    sweep=["g(−1)=0 의 근 중 (i)과 같은 값"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 6 (두 경우의 a 가 겹침)",
        changed=["g=−x²+4x+a → −x²+4x+a²−4a−16"], naturalness="",
        stem=stem("-x^2+4x+a^2-4a-16"), choices=["-3", "4", "7", "11", "14"], answer="4", trap_answer="11",
        trap_path="(i)의 7 과 (ii)의 근 7, −3 을 모두 더해 11 (7 중복).",
        explanation=[
            r"$x=-1$에서 $f$의 좌극한 $4$, 함숫값 $a-3$이다.",
            r"(i) $f$가 연속: $a=7$.",
            r"(ii) $g(-1)=a^2-4a-21=(a-7)(a+3)=0$: $a=7$ 또는 $-3$.",
            r"함정: $a=7$은 두 경우에 모두 나오지만 한 번만 센다. 합은 $7+(-3)=4$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (g=−x²+2x+a)",
        changed=["g=−x²+4x+a → −x²+2x+a"], naturalness="",
        stem=stem("-x^2+2x+a"), choices=["9", "10", "11", "12", "13"], answer="10", trap_answer=None, trap_path=None,
        explanation=[
            r"(i) $f$가 $x=-1$에서 연속: $4=a-3$, $a=7$.",
            r"(ii) $g(-1)=-3+a=0$: $a=3$.",
            r"합은 $10$이다.",
        ],
    ),
]


def good_as(gexpr):
    a = Symbol('a', real=True)
    cands = set(solve(Eq(4, a - 3), a)) | set(solve(gexpr.subs(x, -1), a))
    good = set()
    for av in cands:
        g = gexpr.subs(a, av)
        l = limit((-x + 3)*g, x, -1, '-'); v = ((3*x + av)*g).subs(x, -1)
        r = limit((3*x + av)*g, x, -1, '+')
        if simplify(l - r) == 0 and simplify(l - v) == 0:
            good.add(av)
    return good


def verify(c):
    a = Symbol('a', real=True)
    g = good_as(-x**2 + 4*x + a)
    c.check("원문: {7, 5}", g == {7, 5})
    c.ans('orig', sum(g))
    g = good_as(-x**2 + 4*x + a**2 - 4*a - 16)
    c.check("1: {7, −3}", g == {7, -3})
    c.ans(1, sum(g))
    c.trap(1, 7 + 7 - 3)
    g = good_as(-x**2 + 2*x + a)
    c.ans(2, sum(g))
