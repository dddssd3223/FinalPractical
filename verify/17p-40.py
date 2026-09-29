from lib import *

ORIG = dict(
    id="17p-40", chapter=1, page=17, num=40, source="2023년 수능특강 [23009-0026]", type="주관식",
    stem=r"$t$가 $\frac14$보다 큰 실수일 때, 곡선 $y=tx^2$ 위의 점 $\mathrm{P}$에서 직선 $y=x-1$에 내린 수선의 발을 $\mathrm{Q}$라 하자. 선분 $\mathrm{PQ}$의 길이가 최소일 때, 직선 $\mathrm{OP}$가 직선 $y=x-1$과 만나는 점을 $\mathrm{R}$라 하고, 삼각형 $\mathrm{PQR}$의 넓이를 $S(t)$라 하자. $\displaystyle\lim_{t\to\frac14+}\frac{S(t)}{\left(t-\frac14\right)^2}$의 값을 구하시오. (단, $\mathrm{O}$는 원점이고, 점 $\mathrm{P}$는 제1사분면에 있다.)",
    answer="12",
    general="PQ 최소 ⇔ 접선 기울기 1: P(1/(2t), 1/(4t)). OP 기울기 1/2(고정) → R(2,1). ∠Q=90°, OP 와 직선의 사잇각 tanθ=1/3 → QR=3PQ, S=3PQ²/2. PQ=(1−1/(4t))/√2 → S/(t−¼)² → 12.",
    special="① OP 기울기가 t 와 무관하게 1/2 이라 R 이 고정 — 곡선이 원점을 지나는 y=tx² 라서 생긴 우연. 곡선을 평행이동하면 R 이 움직이고 QR/PQ 비도 바뀜. ② QR=3PQ 를 외워 쓰는 풀이.",
    perspective="넓이 = ½·PQ²·cotθ (θ: OP 와 직선의 사잇각의 극한). PQ ∝ (t−t₀).",
    table=[
        ("곡선 y=tx² (원점 지남)", "OP 기울기가 변하는 경우", "y=tx²+1 이면 OP 기울기 1/2+2t, 극한에서 cotθ=7"),
        ("직선 y=x−1", "—", "y=x−3 이면 t₀=1/12, 구조 동일 (생존)"),
        ("t>1/4", "P 가 직선 위(t=1/4)", "—"),
    ],
    sweep=["t₀: P 가 직선 위에 올 때(접할 때)", "OP 기울기 = y_P/x_P"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (OP 기울기 고정이 깨짐 → QR/PQ 비가 바뀜)",
        changed=["곡선 y=tx² → y=tx²+1", "t>1/4 → t>1/8 (접하는 값이 따라 바뀜)"],
        naturalness="실질 변경은 곡선의 평행이동 하나, 범위는 그에 따라 자동으로 바뀌는 값.",
        stem=r"$t$가 $\frac18$보다 큰 실수일 때, 곡선 $y=tx^2+1$ 위의 점 $\mathrm{P}$에서 직선 $y=x-1$에 내린 수선의 발을 $\mathrm{Q}$라 하자. 선분 $\mathrm{PQ}$의 길이가 최소일 때, 직선 $\mathrm{OP}$가 직선 $y=x-1$과 만나는 점을 $\mathrm{R}$라 하고, 삼각형 $\mathrm{PQR}$의 넓이를 $S(t)$라 하자. $\displaystyle\lim_{t\to\frac18+}\frac{S(t)}{\left(t-\frac18\right)^2}$의 값을 구하시오. (단, $\mathrm{O}$는 원점이고, 점 $\mathrm{P}$는 제1사분면에 있다.)",
        answer="448", trap_answer="192",
        trap_path="원문처럼 QR=3PQ (OP 기울기 1/2 고정) 로 두고 S=3PQ²/2 → 192.",
        explanation=[
            r"PQ가 최소이려면 P에서의 접선의 기울기가 $1$: $\mathrm{P}\left(\frac1{2t},\,\frac1{4t}+1\right)$이다.",
            r"$\overline{\mathrm{PQ}}=\dfrac{\left|\frac1{4t}-2\right|}{\sqrt2}=\dfrac{8(t-\frac18)}{4\sqrt2\,t}$이다.",
            r"함정: OP의 기울기는 $\frac12+2t$로 변하고 $t\to\frac18$일 때 $\frac34$이다. 원문처럼 $\frac12$이 아니다.",
            r"OP와 직선 $y=x-1$이 이루는 각 $\theta$는 $\tan\theta=\dfrac{1-\frac34}{1+\frac34}=\dfrac17$이므로 $\overline{\mathrm{QR}}\approx7\,\overline{\mathrm{PQ}}$이다.",
            r"$S(t)\approx\dfrac72\overline{\mathrm{PQ}}^2$이므로 극한은 $\dfrac72\times\dfrac{64}{32}\times64=448$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (직선 y=x−1 → y=x−3)",
        changed=["직선 y=x−1 → y=x−3", "t>1/4 → t>1/12 (접하는 값이 따라 바뀜)"],
        naturalness="실질 변경은 직선 하나, 범위는 자동으로 바뀌는 값.",
        stem=r"$t$가 $\frac1{12}$보다 큰 실수일 때, 곡선 $y=tx^2$ 위의 점 $\mathrm{P}$에서 직선 $y=x-3$에 내린 수선의 발을 $\mathrm{Q}$라 하자. 선분 $\mathrm{PQ}$의 길이가 최소일 때, 직선 $\mathrm{OP}$가 직선 $y=x-3$과 만나는 점을 $\mathrm{R}$라 하고, 삼각형 $\mathrm{PQR}$의 넓이를 $S(t)$라 하자. $\displaystyle\lim_{t\to\frac1{12}+}\frac{S(t)}{\left(t-\frac1{12}\right)^2}$의 값을 구하시오. (단, $\mathrm{O}$는 원점이고, 점 $\mathrm{P}$는 제1사분면에 있다.)",
        answer="972", trap_answer=None, trap_path=None,
        explanation=[
            r"PQ가 최소이려면 $\mathrm{P}\left(\frac1{2t},\,\frac1{4t}\right)$이고 OP의 기울기는 $\frac12$로 일정하다.",
            r"OP와 직선이 이루는 각은 $\tan\theta=\frac13$이므로 $\overline{\mathrm{QR}}=3\overline{\mathrm{PQ}}$, $S=\frac32\overline{\mathrm{PQ}}^2$이다.",
            r"$\overline{\mathrm{PQ}}=\dfrac{3-\frac1{4t}}{\sqrt2}=\dfrac{12(t-\frac1{12})}{4\sqrt2\,t}$이다.",
            r"$\displaystyle\lim\frac{S(t)}{(t-\frac1{12})^2}=\frac32\times\frac{9}{2\cdot\frac1{144}}=972$이다.",
        ],
    ),
]

t, X = symbols('t X', positive=True)


def geom(curve, b):
    xp = solve(Eq(diff(curve, X), 1), X)[0]
    yp = curve.subs(X, xp)
    d = (xp - yp - b)/2
    Q = (xp - d, yp + d)
    k = yp/xp
    xr = solve(Eq(k*X, X - b), X)[0]
    R = (xr, k*xr)
    S = Abs((Q[0] - xp)*(R[1] - yp) - (R[0] - xp)*(Q[1] - yp))/2
    PQ2 = ((xp - Q[0])**2 + (yp - Q[1])**2)
    t0 = solve(Eq(xp - yp - b, 0), t)[0]
    return simplify(S), PQ2, t0, (xp, yp)


def verify(c):
    for key, curve, b in (('orig', t*X**2, 1), (1, t*X**2 + 1, 1), (2, t*X**2, 3)):
        S, PQ2, t0, P = geom(curve, b)
        c.check(f"{key}: P 제1사분면 (t₀ 근방)", P[0].subs(t, t0*Rational(11, 10)) > 0 and P[1].subs(t, t0*Rational(11, 10)) > 0)
        c.ans(key, limit(S/(t - t0)**2, t, t0, '+'))
        if key == 1:
            c.trap(1, limit(Rational(3, 2)*PQ2/(t - t0)**2, t, t0, '+'))
