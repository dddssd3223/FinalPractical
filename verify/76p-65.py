from lib import *

def stem(A, B):
    return (r"함수 $f(x)=\begin{cases}x+1 & (x<1) \\ -2x+4 & (x\ge1)\end{cases}$이고, 좌표평면 위에 두 점 $\mathrm A" + A + r"$, $\mathrm B" + B + r"$가 있다. "
            r"실수 $x$에 대하여 점 $(x,\,f(x))$에서 점 $\mathrm A$까지의 거리의 제곱과 점 $\mathrm B$까지의 거리의 제곱 중 크지 않은 값을 $g(x)$라 하자. "
            r"함수 $g(x)$가 $x=a$에서 미분가능하지 않은 모든 $a$의 값의 합이 $p$일 때, $80p$의 값을 구하시오.")

ORIG = dict(
    id="76p-65", chapter=3, page=76, num=65, source="2017학년도 수능 6월 모의평가 나형 29번", type="주관식",
    stem=stem("(-1,\\,-1)", "(1,\\,2)"), answer="186",
    general="dA²−dB²=4x+6f−3. x<1: 10x+3=0 → −3/10, x≥1: −8x+21=0 → 21/8 (두 곳 모두 부호가 바뀌고 기울기 다름 → 꺾임). x=1 은 B 자신이라 dB² 가 양쪽 모두 기울기 0 → 미분가능. p=93/40 → 186.",
    special="① f 의 꺾이는 점 x=1 은 B 가 곡선 위에 있어 (거리 0) dB² 의 기울기가 양쪽 0 — B 가 곡선 밖이면 x=1 도 꺾임.",
    perspective="min 의 꺾임 = 교차점 + 선택된 함수 자체의 꺾임.",
    table=[
        ("B 가 곡선 위 (x=1 에서 dB²=0)", "B 가 곡선 밖 (dB² 가 x=1 에서 꺾임)", "B(1,3) 이면 {0,1,2} → 240"),
        ("A(−1,−1)", "—", "A(−2,−1) 이면 {−1/2, 4} → 280 (생존)"),
    ],
    sweep=["교차: dA²=dB² 의 부호 변화 점"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (B 가 곡선 밖이면 f 의 꺾임이 g 로 전달)",
        changed=["B(1,2) → B(1,3)"], naturalness="",
        stem=stem("(-1,\\,-1)", "(1,\\,3)"), answer="240", trap_answer="160",
        trap_path="원문처럼 x=1 은 미분가능하다고 보고 교차점 0, 2 만 더해 80·2=160 (B 가 곡선 밖이라 x=1 에서 dB² 가 꺾임).",
        explanation=[
            r"$d_A^2-d_B^2=4x+8f(x)-8$이고 $x<1$에서 $12x$, $x\ge1$에서 $-12x+24$이므로 교차점은 $x=0$, $x=2$이다.",
            r"교차점에서 두 함수의 기울기가 달라 $g$는 꺾인다.",
            r"함정: $x=1$에서는 $d_B^2=1<d_A^2=13$이고 $d_B^2$의 좌미분계수 $-2$, 우미분계수 $4$가 달라 $g$도 미분가능하지 않다.",
            r"$p=0+1+2=3$이므로 $80p=240$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (A(−1,−1) → A(−2,−1))",
        changed=["A(−1,−1) → A(−2,−1)"], naturalness="",
        stem=stem("(-2,\\,-1)", "(1,\\,2)"), answer="280", trap_answer=None, trap_path=None,
        explanation=[
            r"$d_A^2-d_B^2=6x+6f(x)$이고 $x<1$에서 $12x+6$, $x\ge1$에서 $-6x+24$이다.",
            r"교차점은 $x=-\frac12$, $x=4$이고, $x=1$은 B가 곡선 위라 미분가능하다.",
            r"$p=\frac72$이므로 $80p=280$이다.",
        ],
    ),
]


def nondiff(A, B):
    P = [(x + 1, -oo, 1), (-2*x + 4, 1, oo)]
    out = set()
    d = lambda P0, e: (x - P0[0])**2 + (e - P0[1])**2
    G = []  # 조각별로 min 을 구성: 각 조각 안 교차점 찾기
    for e, lo, hi in P:
        dA, dB = expand(d(A, e)), expand(d(B, e))
        for r in solve(dA - dB, x):
            if r.is_real and lo < r < hi:
                sgn_change = sign((dA - dB).subs(x, r - Rational(1, 100))) != sign((dA - dB).subs(x, r + Rational(1, 100)))
                slope_diff = diff(dA - dB, x).subs(x, r) != 0
                if sgn_change and slope_diff:
                    out.add(r)
    # 경계 x=1: 양쪽에서 선택된 함수의 좌·우 미분계수 비교
    def gpiece(side):
        e = piece_at(P, 1, side)
        dA, dB = d(A, e), d(B, e)
        vA, vB = dA.subs(x, 1), dB.subs(x, 1)
        assert vA != vB
        return dA if vA < vB else dB
    L = diff(gpiece('-'), x).subs(x, 1)
    R = diff(gpiece('+'), x).subs(x, 1)
    if L != R:
        out.add(Integer(1))
    return out


def verify(c):
    s = nondiff((-1, -1), (1, 2))
    c.check("원문: {−3/10, 21/8}", s == {Rational(-3, 10), Rational(21, 8)})
    c.ans('orig', 80*sum(s))
    s = nondiff((-1, -1), (1, 3))
    c.check("1: {0,1,2}", s == {0, 1, 2})
    c.ans(1, 80*sum(s))
    c.trap(1, 80*sum(s - {1}))
    s = nondiff((-2, -1), (1, 2))
    c.ans(2, 80*sum(s))
