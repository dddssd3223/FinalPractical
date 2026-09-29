from lib import *

def S(l, r):
    return r"함수 $f(x)=\begin{cases}" + l + r" & (x\le0)\\ " + r + r" & (x>0)\end{cases}$에 대하여 함수 $f(x)f(x-a)$가 $x=a$에서 연속이 되도록 하는 "

ORIG = dict(
    id="34p-9", chapter=2, page=34, num=9, source="2014학년도 대수능 A형 28번", type="주관식",
    stem=S("x+1", r"-\frac12x+7") + r"모든 실수 $a$의 값의 합을 구하시오. [4점]",
    answer="13",
    general="f 는 0 에서만 불연속(좌 1, 우 7, f(0)=1). a≠0: x=a 에서 f(x)→f(a), f(x−a) 의 좌·우 1, 7 → f(a)·1=f(a)·7 → f(a)=0 → a=−1 (x≤0 ✓), a=14 (x>0 ✓). a=0: f² 의 좌·우 1, 49 → 불연속. 합 13.",
    special="① a=0 경우를 '두 인수가 모두 점프' 로 따로 검토하지 않음 — 원문은 좌·우 극한의 제곱이 달라 우연히 제외. ② f(a)=0 의 해를 구간 확인 없이 채택 — 원문은 두 해가 모두 구간 안.",
    perspective="x=a 에서 점프하는 인수 f(x−a) 를 다른 인수 f(a) 가 0 으로 눌러 주거나, a=0 이면 f² 의 좌·우 극한 비교.",
    table=[
        ("좌·우 극한 1, 7 (제곱이 다름)", "a=0 에서 f² 연속인 경우(좌·우 극한이 부호만 다름)", "좌 −4, 우 4 로 바꾸면 a=0 도 가능"),
        ("f(a)=0 의 해가 모두 구간 안", "해가 구간 밖", "왼쪽을 x−3 으로 바꾸면 해 3 은 x≤0 밖"),
    ],
    sweep=["a=0: (좌극한)² = (우극한)² ?", "각 조각의 근이 해당 구간 안인가"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (a=0 에서 f² 가 연속이 되는 경우)",
        changed=["f 의 두 조각 (x²−4, 4−x)", "묻는 값: a 의 합 → a 의 개수"],
        naturalness="a=0 은 합에 영향이 없어 '개수'로 물어야 경우 누락이 드러남 → 묻는 값 변경은 필수.",
        stem=S("x^2-4", "4-x") + r"실수 $a$의 개수를 구하시오.",
        answer="3", trap_answer="2",
        trap_path="원문처럼 f(a)=0 인 a(−2, 4)만 세고 a=0 을 놓침 → 2.",
        explanation=[
            r"$f$는 $x=0$에서 좌극한 $-4$, 우극한 $4$, $f(0)=-4$로 불연속이다.",
            r"$a\neq0$: 연속이려면 $f(a)=0$. $x\le0$에서 $x^2-4=0$ → $a=-2$ ($a=2$는 구간 밖), $x>0$에서 $4-x=0$ → $a=4$.",
            r"$a=0$: $\{f(x)\}^2$의 좌극한 $16$, 우극한 $16$, 함숫값 $16$이므로 연속이다. 함정: 이 경우를 놓치기 쉽다.",
            r"$a=-2,\,0,\,4$의 $3$개이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 2행 / 3-C 4 (f(a)=0 의 해가 구간 밖)",
        changed=["x≤0 조각 x+1 → x−3"], naturalness="",
        stem=S("x-3", r"-\frac12x+7") + r"모든 실수 $a$의 값의 합을 구하시오.",
        answer="14", trap_answer="17",
        trap_path="x−3=0 의 해 3 을 구간(x≤0) 확인 없이 포함 → 3+14=17.",
        explanation=[
            r"$f$는 $x=0$에서 좌극한 $-3$, 우극한 $7$로 불연속이다.",
            r"$a\neq0$이면 $f(a)=0$이어야 한다. $x>0$에서 $-\frac12a+7=0$, $a=14$.",
            r"함정: $x-3=0$의 해 $3$은 $x\le0$이 아니므로 $f(3)=\frac{11}{2}\neq0$이다.",
            r"$a=0$이면 $\{f(x)\}^2$의 좌극한 $9$, 우극한 $49$로 불연속이다. 따라서 합은 $14$이다.",
        ],
    ),
]


def good_as(left, right):
    P = [(left, -oo, 0), (right, 0, oo)]
    fval = lambda v: left.subs(x, v) if v <= 0 else right.subs(x, v)
    cands = {Integer(0)}
    naive = set()
    for e, dom in ((left, lambda v: v <= 0), (right, lambda v: v > 0)):
        for z in solve(e, x):
            if z.is_real:
                naive.add(z)
                if dom(z):
                    cands.add(z)
    grid = {Rational(k, 3) for k in range(-45, 46)}

    def cont(a):
        Fl = piece_at(P, a, '-'); Fr = piece_at(P, a, '+')
        Gl = piece_at(P, 0, '-').subs(x, x - a); Gr = piece_at(P, 0, '+').subs(x, x - a)
        l = limit(Fl*Gl, x, a, '-'); r = limit(Fr*Gr, x, a, '+')
        v = fval(a)*fval(0)
        return simplify(l - r) == 0 and simplify(l - v) == 0
    good = {a for a in cands | grid if cont(a)}
    return good, naive


def verify(c):
    g, n = good_as(x + 1, -x/2 + 7)
    c.check("원문: {−1, 14}", g == {-1, 14})
    c.ans('orig', sum(g))
    g, n = good_as(x**2 - 4, 4 - x)
    c.check("1: {−2, 0, 4}", g == {-2, 0, 4})
    c.ans(1, len(g))
    c.trap(1, len(g - {0}))
    g, n = good_as(x - 3, -x/2 + 7)
    c.check("2: {14}", g == {14})
    c.ans(2, sum(g))
    c.trap(2, sum(n))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '구간 확인 누락뿐 — 원문 풀이가 그대로 통함'
