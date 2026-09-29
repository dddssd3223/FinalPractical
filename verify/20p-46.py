from lib import *

ORIG = dict(
    id="20p-46", chapter=1, page=20, num=46, source="2025년 수능특강 [25009-0023]", type="객관식",
    stem=r"곡선 $y=x^2-2x$ 위의 점 $\mathrm{P}(t,\,t^2-2t)\,(0<t<2)$를 지나고 기울기가 $-2$인 직선이 곡선 $y=x^2-2x$와 만나는 점 중 $\mathrm{P}$가 아닌 점을 $\mathrm{Q}$라 하자. 선분 $\mathrm{OQ}$의 길이를 $L(t)$라 할 때, $\displaystyle\lim_{t\to0+}\frac{L(t)}{t}$의 값은? (단, $\mathrm{O}$는 원점이다.)",
    choices=["sqrt(3)", "2", "sqrt(5)", "sqrt(6)", "sqrt(7)"], answer="sqrt(5)",
    general="연립: x²−2x=−2(x−t)+t²−2t → x²=t² → Q(−t, t²+2t). L=t√(1+(t+2)²) → L/t→√5.",
    special="① 기울기 −2 가 곡선의 일차항 계수 −2 와 같아 x 항이 소거되고 x_Q=−t 가 됨 — 기울기가 다르면 x_Q=(2+m)−t 로 Q 가 원점으로 가지 않음.",
    perspective="근과 계수: x_P+x_Q=2+m. m=−2 일 때만 Q→O.",
    table=[
        ("기울기 −2", "Q 가 원점에서 멀어지는 경우", "−3 이면 Q→(−1,3), L→√10 (L/t 발산)"),
        ("곡선 x²−2x", "—", "x²−4x 와 기울기 −4 면 같은 구조 (생존)"),
    ],
    sweep=["x_Q=2+m−t: m=−2 에서만 x_Q→0"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (기울기가 일차항 계수와 달라 Q 가 원점으로 가지 않음)",
        changed=["기울기 −2 → −3", "묻는 값 lim L/t → lim L²"],
        naturalness="기울기를 바꾸면 L/t 가 발산하므로 묻는 값을 L² 로 바꾸는 것은 필수.",
        stem=r"곡선 $y=x^2-2x$ 위의 점 $\mathrm{P}(t,\,t^2-2t)\,(0<t<2)$를 지나고 기울기가 $-3$인 직선이 곡선 $y=x^2-2x$와 만나는 점 중 $\mathrm{P}$가 아닌 점을 $\mathrm{Q}$라 하자. 선분 $\mathrm{OQ}$의 길이를 $L(t)$라 할 때, $\displaystyle\lim_{t\to0+}\{L(t)\}^2$의 값은? (단, $\mathrm{O}$는 원점이다.)",
        choices=["0", "2", "5", "8", "10"], answer="10", trap_answer="0",
        trap_path="원문처럼 x_Q=−t 로 두어 Q→O, L²→0.",
        explanation=[
            r"$x^2-2x=-3(x-t)+t^2-2t$에서 $x^2+x-(t^2+t)=0$, $(x-t)(x+t+1)=0$이다.",
            r"함정: 기울기가 $-2$가 아니므로 $x$항이 소거되지 않아 $x_{\mathrm Q}=-t-1$이다.",
            r"$t\to0+$일 때 $\mathrm Q\to(-1,\,3)$이다.",
            r"$\{L(t)\}^2\to1+9=10$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (곡선 x²−4x, 기울기 −4: 소거 구조 유지)",
        changed=["곡선 x²−2x → x²−4x, 기울기 −2 → −4 (0<t<4)"], naturalness="곡선과 기울기를 같은 구조로 함께 바꾼 한 가지 변경.",
        stem=r"곡선 $y=x^2-4x$ 위의 점 $\mathrm{P}(t,\,t^2-4t)\,(0<t<4)$를 지나고 기울기가 $-4$인 직선이 곡선 $y=x^2-4x$와 만나는 점 중 $\mathrm{P}$가 아닌 점을 $\mathrm{Q}$라 하자. 선분 $\mathrm{OQ}$의 길이를 $L(t)$라 할 때, $\displaystyle\lim_{t\to0+}\frac{L(t)}{t}$의 값은? (단, $\mathrm{O}$는 원점이다.)",
        choices=["sqrt(13)", "sqrt(15)", "sqrt(17)", "sqrt(19)", "sqrt(21)"], answer="sqrt(17)", trap_answer=None, trap_path=None,
        explanation=[
            r"$x^2-4x=-4(x-t)+t^2-4t$에서 $x^2=t^2$이므로 $\mathrm Q(-t,\,t^2+4t)$이다.",
            r"$L(t)=\sqrt{t^2+(t^2+4t)^2}=t\sqrt{1+(t+4)^2}$이다.",
            r"$\displaystyle\lim_{t\to0+}\frac{L(t)}{t}=\sqrt{17}$이다.",
        ],
    ),
]

t = Symbol('t', positive=True)


def Q_of(k, m):
    X = Symbol('X', real=True)
    curve = X**2 - k*X
    line = m*(X - t) + (t**2 - k*t)
    roots = solve(Eq(curve, line), X)
    xq = [r for r in roots if simplify(r - t) != 0][0]
    return xq, curve.subs(X, xq)


def verify(c):
    xq, yq = Q_of(2, -2)
    c.ans('orig', limit(sqrt(xq**2 + yq**2)/t, t, 0, '+'))
    xq, yq = Q_of(2, -3)
    c.ans(1, limit(xq**2 + yq**2, t, 0, '+'))
    c.trap(1, limit((t**2 + (t**2 + 2*t)**2), t, 0, '+'))
    xq, yq = Q_of(4, -4)
    c.ans(2, limit(sqrt(xq**2 + yq**2)/t, t, 0, '+'))
