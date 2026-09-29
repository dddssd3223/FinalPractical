from lib import *

ORIG = dict(
    id="26p-61", chapter=1, page=26, num=61, source="2023학년도 수능 9월 모의평가 12번", type="객관식",
    stem=r"실수 $t\,(t>0)$에 대하여 직선 $y=x+t$와 곡선 $y=x^2$이 만나는 두 점을 $\mathrm A$, $\mathrm B$라 하자. 점 $\mathrm A$를 지나고 $x$축에 평행한 직선이 곡선 $y=x^2$과 만나는 점 중 $\mathrm A$가 아닌 점을 $\mathrm C$, 점 $\mathrm B$에서 선분 $\mathrm{AC}$에 내린 수선의 발을 $\mathrm H$라 하자. $\displaystyle\lim_{t\to0+}\frac{\overline{\mathrm{AH}}-\overline{\mathrm{CH}}}{t}$의 값은? (단, 점 $\mathrm A$의 $x$좌표는 양수이다.) [4점]",
    choices=["1", "2", "3", "4", "5"], answer="2",
    general="x²−x−t=0: x_A=(1+√(1+4t))/2, x_B=(1−√(1+4t))/2. 대칭축 x=0 이라 x_C=−x_A. AH−CH=(x_A−x_B)−(x_B−x_C)=−2x_B=√(1+4t)−1 → /t → 2.",
    special="① C=(−x_A, ·) — 포물선의 대칭축이 y축이라서. 축이 옮겨지면 x_A+x_C≠0 이 되어 AH−CH 가 0 으로 가지 않음.",
    perspective="AH−CH=(x_A+x_C)−2x_B, x_A+x_C=2×(대칭축).",
    table=[
        ("곡선 y=x² (축 x=0)", "대칭축이 0 이 아닌 경우", "y=x²+x 이면 x_A+x_C=−1 → AH−CH→−1"),
        ("직선 기울기 1", "—", "기울기 2 이면 −2x_B=√(4+4t)−2 → 1 (생존)"),
    ],
    sweep=["t→0+ 에서 B→O", "AH−CH → 2×(축) − 0"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (대칭축이 y축이 아니면 x_C≠−x_A)",
        changed=["곡선 y=x² → y=x²+x", "묻는 값 (AH−CH)/t → AH−CH"],
        naturalness="곡선을 바꾸면 AH−CH 가 0 이 아닌 값으로 가서 /t 가 발산하므로 묻는 값을 바꾼 것은 필수.",
        stem=r"실수 $t\,(t>0)$에 대하여 직선 $y=x+t$와 곡선 $y=x^2+x$가 만나는 두 점을 $\mathrm A$, $\mathrm B$라 하자. 점 $\mathrm A$를 지나고 $x$축에 평행한 직선이 곡선 $y=x^2+x$와 만나는 점 중 $\mathrm A$가 아닌 점을 $\mathrm C$, 점 $\mathrm B$에서 직선 $\mathrm{AC}$에 내린 수선의 발을 $\mathrm H$라 하자. $\displaystyle\lim_{t\to0+}\left(\overline{\mathrm{AH}}-\overline{\mathrm{CH}}\right)$의 값은? (단, 점 $\mathrm A$의 $x$좌표는 양수이다.)",
        choices=["-2", "-1", "0", "1", "2"], answer="-1", trap_answer="0",
        trap_path="원문처럼 x_C=−x_A 로 보고 AH−CH=−2x_B=2√t → 0.",
        explanation=[
            r"$x^2+x=x+t$에서 $x=\pm\sqrt t$이므로 $x_{\mathrm A}=\sqrt t$, $x_{\mathrm B}=-\sqrt t$이다.",
            r"곡선의 대칭축은 $x=-\frac12$이므로 $x_{\mathrm C}=-1-\sqrt t$이다. 함정: $-x_{\mathrm A}$가 아니다.",
            r"$\overline{\mathrm{AH}}=x_{\mathrm A}-x_{\mathrm B}=2\sqrt t$, $\overline{\mathrm{CH}}=x_{\mathrm B}-x_{\mathrm C}=1$이다.",
            r"$\overline{\mathrm{AH}}-\overline{\mathrm{CH}}=2\sqrt t-1\to-1$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (직선 기울기 1 → 2)",
        changed=["직선 y=x+t → y=2x+t"], naturalness="",
        stem=r"실수 $t\,(t>0)$에 대하여 직선 $y=2x+t$와 곡선 $y=x^2$이 만나는 두 점을 $\mathrm A$, $\mathrm B$라 하자. 점 $\mathrm A$를 지나고 $x$축에 평행한 직선이 곡선 $y=x^2$과 만나는 점 중 $\mathrm A$가 아닌 점을 $\mathrm C$, 점 $\mathrm B$에서 선분 $\mathrm{AC}$에 내린 수선의 발을 $\mathrm H$라 하자. $\displaystyle\lim_{t\to0+}\frac{\overline{\mathrm{AH}}-\overline{\mathrm{CH}}}{t}$의 값은? (단, 점 $\mathrm A$의 $x$좌표는 양수이다.)",
        choices=["1/2", "1", "3/2", "2", "5/2"], answer="1", trap_answer=None, trap_path=None,
        explanation=[
            r"$x^2-2x-t=0$에서 $x_{\mathrm A}=1+\sqrt{1+t}$, $x_{\mathrm B}=1-\sqrt{1+t}$이다.",
            r"$x_{\mathrm C}=-x_{\mathrm A}$이므로 $\overline{\mathrm{AH}}-\overline{\mathrm{CH}}=-2x_{\mathrm B}=2(\sqrt{1+t}-1)$이다.",
            r"$\displaystyle\lim_{t\to0+}\frac{2(\sqrt{1+t}-1)}{t}=1$이다.",
        ],
    ),
]

t = Symbol('t', positive=True)


def AHmCH(curve, m):
    X = Symbol('X', real=True)
    roots = solve(Eq(curve(X), m*X + t), X)
    xA = [r for r in roots if r.subs(t, Rational(1, 100)) > 0][0]
    xB = [r for r in roots if r != xA][0]
    yA = curve(xA)
    others = [r for r in solve(Eq(curve(X), yA), X) if simplify(r - xA) != 0]
    xC = others[0]
    xH = xB
    return simplify(Abs(xA - xH) - Abs(xC - xH)), xA, xB, xC


def verify(c):
    d, *_ = AHmCH(lambda X: X**2, 1)
    c.ans('orig', limit(d/t, t, 0, '+'))
    d, xA, xB, xC = AHmCH(lambda X: X**2 + X, 1)
    c.check("1: x_C=−1−√t (수치 확인)", all(abs((xC - (-1 - sqrt(t))).subs(t, tv).evalf()) < 1e-12 for tv in (Rational(1, 7), 2, 5)))
    c.ans(1, limit(d, t, 0, '+'))
    c.trap(1, limit(-2*xB, t, 0, '+'))
    d, *_ = AHmCH(lambda X: X**2, 2)
    c.ans(2, limit(d/t, t, 0, '+'))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
