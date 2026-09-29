from lib import *

ORIG = dict(
    id="26p-62", chapter=1, page=26, num=62, source="2024학년도 수능 6월 모의평가 11번", type="객관식",
    stem=r"그림과 같이 실수 $t\,(0<t<1)$에 대하여 곡선 $y=x^2$ 위의 점 중에서 직선 $y=2tx-1$과의 거리가 최소인 점을 $\mathrm P$라 하고, 직선 $\mathrm{OP}$가 직선 $y=2tx-1$과 만나는 점을 $\mathrm Q$라 할 때, $\displaystyle\lim_{t\to1-}\frac{\overline{\mathrm{PQ}}}{1-t}$의 값은? (단, $\mathrm O$는 원점이다.) [4점]",
    choices=["sqrt(6)", "sqrt(7)", "2*sqrt(2)", "3", "sqrt(10)"], answer="2*sqrt(2)",
    general="거리 최소 ⇔ 접선 기울기 2t → P(t,t²). OP: y=tx, Q(1/t, 1). PQ=(1−t²)√(1+1/t²) → /(1−t) → 2√2.",
    special="① t→1 에서 직선이 곡선에 접해 PQ→0 인 구조 — 직선의 y절편 −1 과 극한점 t=1 이 맞물린 것. 절편을 바꾸면 접하는 t 가 달라져 PQ 가 0 으로 가지 않음. ② 0<t<1 은 직선이 곡선과 만나지 않게(최소 거리점 유일) 하는 조건.",
    perspective="PQ=(b−t²)√(1+1/t²) (직선 y=2tx−b), 접점 t=√b 에서만 0.",
    table=[
        ("직선 y절편 −1", "접하는 t 가 1 이 아닌 경우", "−2 로 바꾸면 t→1 에서 PQ→√2 (0 이 아님)"),
        ("0<t<1", "직선이 곡선과 만나 최소점이 둘인 경우", "—"),
        ("극한 t→1−", "—", "y=2tx−4, t→2− 이면 같은 구조 (생존)"),
    ],
    sweep=["접하는 t: t²=b", "t²>b 이면 직선과 곡선이 만나 P 가 유일하지 않음"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (극한점에서 직선이 곡선에 접하지 않음)",
        changed=["직선 y=2tx−1 → y=2tx−2", "묻는 값 PQ/(1−t) → PQ"],
        naturalness="절편을 바꾸면 PQ/(1−t) 가 발산하므로 묻는 값을 PQ 로 바꾼 것은 필수.",
        stem=r"실수 $t\,(0<t<1)$에 대하여 곡선 $y=x^2$ 위의 점 중에서 직선 $y=2tx-2$와의 거리가 최소인 점을 $\mathrm P$라 하고, 직선 $\mathrm{OP}$가 직선 $y=2tx-2$와 만나는 점을 $\mathrm Q$라 할 때, $\displaystyle\lim_{t\to1-}\overline{\mathrm{PQ}}$의 값은? (단, $\mathrm O$는 원점이다.)",
        choices=["0", "1", "sqrt(2)", "sqrt(3)", "2"], answer="sqrt(2)", trap_answer="0",
        trap_path="원문처럼 t→1 에서 P 가 직선 위로 온다고 보고 PQ→0.",
        explanation=[
            r"P에서의 접선의 기울기가 $2t$이므로 $\mathrm P(t,\,t^2)$이고 OP: $y=tx$이다.",
            r"$tx=2tx-2$에서 $\mathrm Q\left(\frac2t,\,2\right)$이다.",
            r"$\overline{\mathrm{PQ}}=(2-t^2)\sqrt{1+\frac1{t^2}}$이다. 함정: 직선이 곡선에 접하는 것은 $t=\sqrt2$일 때라 $t\to1$에서 PQ는 $0$으로 가지 않는다.",
            r"$\displaystyle\lim_{t\to1-}\overline{\mathrm{PQ}}=1\times\sqrt2=\sqrt2$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 3행 (직선 y=2tx−4, t→2−)",
        changed=["직선 y=2tx−1 → y=2tx−4, 0<t<1 → 0<t<2, t→1− → t→2−"], naturalness="접하는 t 를 옮긴 한 가지 변경에 범위·극한점을 맞춘 것.",
        stem=r"실수 $t\,(0<t<2)$에 대하여 곡선 $y=x^2$ 위의 점 중에서 직선 $y=2tx-4$와의 거리가 최소인 점을 $\mathrm P$라 하고, 직선 $\mathrm{OP}$가 직선 $y=2tx-4$와 만나는 점을 $\mathrm Q$라 할 때, $\displaystyle\lim_{t\to2-}\frac{\overline{\mathrm{PQ}}}{2-t}$의 값은? (단, $\mathrm O$는 원점이다.)",
        choices=["2*sqrt(3)", "4", "2*sqrt(5)", "2*sqrt(6)", "2*sqrt(7)"], answer="2*sqrt(5)", trap_answer=None, trap_path=None,
        explanation=[
            r"$\mathrm P(t,\,t^2)$, OP: $y=tx$, $\mathrm Q\left(\frac4t,\,4\right)$이다.",
            r"$\overline{\mathrm{PQ}}=(4-t^2)\sqrt{1+\frac1{t^2}}=(2-t)(2+t)\sqrt{1+\frac1{t^2}}$이다.",
            r"$\displaystyle\lim_{t\to2-}\frac{\overline{\mathrm{PQ}}}{2-t}=4\sqrt{\frac54}=2\sqrt5$이다.",
        ],
    ),
]

t = Symbol('t', positive=True)


def PQ(b):
    X = Symbol('X', real=True)
    xp = solve(Eq(2*X, 2*t), X)[0]
    P = (xp, xp**2)
    xq = solve(Eq(t*X, 2*t*X - b), X)[0]
    Q = (xq, t*xq)
    return sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2), P


def no_intersection(b, tmax):
    return all(discriminant(X**2 - 2*tv*X + b, X) < 0 for tv in (Rational(k, 10)*tmax for k in range(1, 10))) if False else \
        all((4*tv**2 - 4*b) < 0 for tv in (Rational(k, 10)*tmax for k in range(1, 10)))


def verify(c):
    d, P = PQ(1)
    c.check("원문: 0<t<1 에서 직선과 곡선이 만나지 않음", no_intersection(1, 1))
    c.ans('orig', sqrt(limit(d**2/(1 - t)**2, t, 1, '-')))  # 양수끼리라 제곱 후 제곱근 (sympy √ 극한 부호 오류 회피)
    d, P = PQ(2)
    c.check("1: 0<t<1 에서 만나지 않음", no_intersection(2, 1))
    c.ans(1, limit(d, t, 1, '-'))
    d1, _ = PQ(1)
    c.trap(1, limit(d1, t, 1, '-'))
    d, P = PQ(4)
    c.check("2: 0<t<2 에서 만나지 않음", no_intersection(4, 2))
    c.ans(2, sqrt(limit(d**2/(2 - t)**2, t, 2, '-')))
