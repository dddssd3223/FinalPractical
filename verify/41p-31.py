from lib import *

def stem(fx, n):
    return (r"실수 $t$에 대하여 함수 $f(x)=\left|" + fx + r"\right|$의 그래프가 직선 $y=ax+t\,(a>0)$과 만나는 서로 다른 점의 개수를 $g(t)$라 하자. 양수 $k$에 대하여 $a=k$일 때, 함수 $g(t)$가 $t=\alpha$에서 불연속이 되도록 하는 실수 $\alpha$의 개수를 $N(k)$라 하자. $\displaystyle\sum_{k=1}^{" + n + r"}N(k)$의 값을 구하시오.")

ORIG = dict(
    id="41p-31", chapter=2, page=41, num=31, source="2022년 수능특강 [22009-0049]", type="주관식",
    stem=stem(r"\frac12x^2-2", "10"), answer="12",
    general="꺾인 점 (±2, 0) 에서 양쪽 곡선의 기울기 크기는 2. a<2 (k=1): 가운데 볼록 부분에 접할 때 + 두 꺾인 점을 지날 때 개수가 바뀜 → 3. a≥2: 직선이 꺾인 점의 기울기 이상이라 꺾인 점을 지나도 개수 불변, 바깥 곡선에 접할 때만 → 1. 3+9×1=12.",
    special="① '접선 + 꺾인 점' 을 모든 k 에 똑같이 셈 — 꺾인 점을 지날 때 개수가 바뀌는지는 a 와 꺾인 점 기울기(2)의 대소에 달림. ② 원문은 k=1 만 2 보다 작음.",
    perspective="g 의 불연속 = 교점 개수가 바뀌는 t. 꺾인 점 통과 시 개수 변화 ⇔ 직선 기울기 < 꺾인 점에서의 한쪽 기울기.",
    table=[
        ("꺾인 점 기울기 2 (f=|½x²−2|)", "2 보다 작은 k 가 여럿인 경우", "|½x²−8| 이면 꺾인 점 기울기 4 → k=1,2,3 에서 N=3"),
        ("합의 범위 k≤10", "—", "k≤20 이면 3+19 (생존)"),
    ],
    sweep=["a=꺾인 점 기울기에서 접점이 꺾인 점과 일치", "a<꺾인 점 기울기: 불연속점 3개, 이상: 1개"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (꺾인 점 기울기와 k 의 대소가 바뀌는 범위)",
        changed=["f=|½x²−2| → |½x²−8|"], naturalness="",
        stem=stem(r"\frac12x^2-8", "10"), answer="16", trap_answer="12",
        trap_path="원문처럼 k=1 에서만 N=3, 나머지 1 로 세어 3+9=12 (꺾인 점 (±4,0) 의 기울기가 4 라 k=2, 3 도 N=3).",
        explanation=[
            r"$f$는 $x=\pm4$에서 꺾이고, 꺾인 점에서 곡선의 기울기의 크기는 $4$이다.",
            r"$k<4$이면 가운데 부분 $y=8-\frac12x^2$에 접할 때와 두 꺾인 점을 지날 때 교점의 개수가 바뀌어 $N(k)=3$이다.",
            r"$k\ge4$이면 꺾인 점을 지나도 개수가 그대로이고 바깥 곡선에 접할 때만 바뀌어 $N(k)=1$이다.",
            r"함정: 원문은 꺾인 점 기울기가 $2$라 $k=1$만 $3$이었다. 여기서는 $k=1,2,3$이 $3$이다.",
            r"$\sum N(k)=3\times3+7\times1=16$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (합의 범위 10 → 20)",
        changed=["Σ_{k=1}^{10} → Σ_{k=1}^{20}"], naturalness="",
        stem=stem(r"\frac12x^2-2", "20"), answer="22", trap_answer=None, trap_path=None,
        explanation=[
            r"꺾인 점 $(\pm2,0)$에서 곡선의 기울기의 크기는 $2$이다.",
            r"$k=1$: 가운데 부분에 접할 때, 두 꺾인 점을 지날 때 → $N(1)=3$.",
            r"$k\ge2$: 바깥 곡선에 접할 때만 → $N(k)=1$.",
            r"$3+19=22$이다.",
        ],
    ),
]

t = Symbol('t', real=True)


def count(F, R, a, tv):
    sols = set()
    for s in solve(Eq(F, a*x + tv), x):
        if s.is_real and abs(s) >= R:
            sols.add(nsimplify(s))
    for s in solve(Eq(-F, a*x + tv), x):
        if s.is_real and abs(s) <= R:
            sols.add(nsimplify(s))
    return len(sols)


def N(F, R, a):
    crit = set()
    for G in (F, -F):
        crit |= set(solve(discriminant(Poly(G - a*x - t, x).as_expr(), x), t))
    crit |= {Integer(-a*R), Integer(a*R)}
    n = 0
    for cv in sorted(v for v in crit if v.is_real):
        e = Rational(1, 1000)
        vals = {count(F, R, a, cv - e), count(F, R, a, cv), count(F, R, a, cv + e)}
        n += len(vals) > 1
    return n


def verify(c):
    F = x**2/2 - 2
    Ns = [N(F, 2, k) for k in range(1, 21)]
    c.check("원문: N(1)=3, N(k≥2)=1", Ns[0] == 3 and all(v == 1 for v in Ns[1:]))
    c.ans('orig', sum(Ns[:10]))
    c.ans(2, sum(Ns[:20]))
    F2 = x**2/2 - 8
    Ns2 = [N(F2, 4, k) for k in range(1, 11)]
    c.check("1: N=3 (k=1,2,3), 1 (k≥4)", Ns2 == [3, 3, 3] + [1]*7)
    c.ans(1, sum(Ns2))
    c.trap(1, 3 + 9)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
