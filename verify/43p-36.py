from lib import *

def stem(r):
    return (r"함수 $f(x)=\begin{cases}-3x(x-1) & (x<2)\\ " + r + r" & (x\ge2)\end{cases}$일 때, 함수 $f(x-1)f(x-a)$가 $x=3$에서 연속이 되도록 하는 모든 실수 $a$의 값의 합은?")

ORIG = dict(
    id="43p-36", chapter=2, page=43, num=36, source="2025년 수능특강 [25009-0051]", type="객관식",
    stem=stem("(x-4)(x-5)"), choices=["1", "3", "5", "7", "9"], answer="3",
    general="x=3 에서 f(x−1) 은 좌 −6, 우 6 (점프). a≠1: f(x−a) 는 연속 → f(3−a)=0 → 3−a∈{0,1,4,5} → a=3,2,−1,−2. a=1: {f(x−1)}² 의 좌·우 36, 36 → 연속. 합 3.",
    special="① a=1 (두 인수가 같은 점에서 점프) 을 따로 확인 — 원문은 좌·우 극한이 ±6 으로 제곱이 같아 포함. ② 각 조각의 근이 해당 구간 안인지 — 원문은 모두 구간 안.",
    perspective="점프하는 인수를 0 으로 눌러 주거나(다른 인수의 값 0), 두 인수가 같은 점프면 제곱 비교.",
    table=[
        ("좌·우 극한 ±6", "제곱이 다른 경우", "오른쪽 조각을 (x−4)(x−6) 으로 바꾸면 f(2)=8 → a=1 불가"),
        ("오른쪽 조각의 근 4, 5 (x≥2 안)", "근이 구간 밖", "(x+1)(x−5) 이면 근 −1 은 구간 밖"),
    ],
    sweep=["a=1: (f(2−))² vs (f(2))²", "각 조각의 근이 구간 안인지"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (a=1 에서 제곱이 달라져 제외)",
        changed=["x≥2 조각 (x−4)(x−5) → (x−4)(x−6)"], naturalness="",
        stem=stem("(x-4)(x-6)"), choices=["-1", "0", "1", "2", "3"], answer="1", trap_answer="2",
        trap_path="원문처럼 a=1 도 포함 → 1+1=2 (좌 −6, 우 8 이라 제곱 36≠64).",
        explanation=[
            r"$x=3$에서 $f(x-1)$의 좌극한은 $f(2-)=-6$, 우극한은 $f(2)=8$이다.",
            r"$a\neq1$이면 $f(3-a)=0$이어야 한다: $3-a\in\{0,1,4,6\}$, $a=3,2,-1,-3$.",
            r"함정: $a=1$이면 $\{f(x-1)\}^2$의 좌극한 $36$, 우극한 $64$로 달라 연속이 아니다.",
            r"합은 $3+2-1-3=1$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 / 3-C 4 (조각의 근이 구간 밖)",
        changed=["x≥2 조각 (x−4)(x−5) → (x+1)(x−5)"], naturalness="",
        stem=stem("(x+1)(x-5)"), choices=["1", "3", "5", "7", "9"], answer="3", trap_answer="7",
        trap_path="(x+1)(x−5)=0 의 근 −1 을 구간(x≥2) 확인 없이 써서 a=4 도 포함 → 7.",
        explanation=[
            r"$x=3$에서 $f(x-1)$의 좌극한 $-6$, 우극한 $f(2)=-9$이다.",
            r"$a\neq1$이면 $f(3-a)=0$: $x<2$에서 근 $0,\,1$ → $a=3,\,2$. $x\ge2$에서 근은 $5$뿐 → $a=-2$.",
            r"함정: $(x+1)(x-5)$의 근 $-1$은 $x\ge2$ 밖이므로 $f(-1)=-6\neq0$이다.",
            r"$a=1$이면 제곱의 좌극한 $36$, 우극한 $81$로 불연속이다. 합은 $3+2-2=3$이다.",
        ],
    ),
]


def good(right):
    left = -3*x*(x - 1)
    P = [(left, -oo, 2), (right, 2, oo)]
    fval = lambda v: left.subs(x, v) if v < 2 else right.subs(x, v)
    cands, naive = {Integer(1)}, {Integer(1)}
    for e, dom in ((left, lambda v: v < 2), (right, lambda v: v >= 2)):
        for z in solve(e, x):
            naive.add(3 - z)
            if dom(z):
                cands.add(3 - z)
    grid = {Rational(k, 2) for k in range(-12, 13)}

    def cont(a):
        # x→3±: 안쪽 x−1 → 2±, x−a → 3−a±
        l = limit(piece_at(P, 2, '-').subs(x, x - 1)*piece_at(P, 3 - a, '-').subs(x, x - a), x, 3, '-')
        r = limit(piece_at(P, 2, '+').subs(x, x - 1)*piece_at(P, 3 - a, '+').subs(x, x - a), x, 3, '+')
        v = fval(2)*fval(3 - a)
        return simplify(l - r) == 0 and simplify(l - v) == 0
    return {a for a in cands | grid if cont(a)}, naive


def verify(c):
    g, n = good((x - 4)*(x - 5))
    c.check("원문: {1, 2, 3, −1, −2}", g == {1, 2, 3, -1, -2})
    c.ans('orig', sum(g))
    g, n = good((x - 4)*(x - 6))
    c.check("1: {2, 3, −1, −3}", g == {2, 3, -1, -3})
    c.ans(1, sum(g))
    c.trap(1, sum(g) + 1)
    g, n = good((x + 1)*(x - 5))
    c.check("2: {2, 3, −2}", g == {2, 3, -2})
    c.ans(2, sum(g))
    c.trap(2, sum(g) + 4)

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '구간 확인 누락뿐 — 원문 풀이가 그대로 통함'
