from lib import *

ORIG = dict(
    id="19p-44", chapter=1, page=19, num=44, source="2022년 수능특강 [22009-0026]", type="객관식",
    stem=r"양의 실수 $t$에 대하여 좌표평면 위에 네 점 $\mathrm{A}(t,\,0)$, $\mathrm{B}(0,\,1)$, $\mathrm{C}(0,\,t)$, $\mathrm{D}(-1,\,0)$이 있다. 곡선 $y=\sqrt x$가 선분 $\mathrm{AB}$와 만나는 점을 $\mathrm{P}$, 곡선 $y=x^2\,(x<0)$이 선분 $\mathrm{CD}$와 만나는 점을 $\mathrm{Q}$라 하자. 원점 $\mathrm{O}$에 대하여 삼각형 $\mathrm{OAP}$의 넓이를 $S(t)$, 삼각형 $\mathrm{OQD}$의 넓이를 $T(t)$라 할 때, $\displaystyle\lim_{t\to\infty}\frac{tT(t)}{S(t)}$의 값은?",
    choices=["1/4", "1/2", "3/4", "1", "5/4"], answer="1",
    general="P: √x=1−x/t → y_P=(−t+√(t²+4t))/2 → 1, S=½t·y_P. Q: x²=t(x+1), x<0 → x_Q=(t−√(t²+4t))/2 → −1, y_Q→1, T=½·1·y_Q. tT/S → t·½/(½t)=1.",
    special="① t→∞ 에서 P→(1,1), Q→(−1,1) 로 극한 위치만 보고 계산 — 극한 위치의 y 가 0 이 아니라서 통함. t→0+ 처럼 점들이 원점으로 모이면 차수(√t, t)를 비교해야 함.",
    perspective="각 넓이의 t 에 대한 주요 차수를 구해 비교.",
    table=[
        ("t→∞", "t→0+ (점들이 원점으로 모임)", "방향을 바꾸면 y_P~√t, y_Q~t 로 차수가 달라져 극한 0"),
        ("D(−1,0)", "—", "D(−2,0) 이면 Q→(−2,4) (생존)"),
    ],
    sweep=["t→∞: y_P, y_Q → 1", "t→0+: y_P ~ √t, y_Q ~ t"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (극한 방향 → 주요 차수 변화)",
        changed=["t→∞ → t→0+"], naturalness="",
        stem=r"양의 실수 $t$에 대하여 좌표평면 위에 네 점 $\mathrm{A}(t,\,0)$, $\mathrm{B}(0,\,1)$, $\mathrm{C}(0,\,t)$, $\mathrm{D}(-1,\,0)$이 있다. 곡선 $y=\sqrt x$가 선분 $\mathrm{AB}$와 만나는 점을 $\mathrm{P}$, 곡선 $y=x^2\,(x<0)$이 선분 $\mathrm{CD}$와 만나는 점을 $\mathrm{Q}$라 하자. 원점 $\mathrm{O}$에 대하여 삼각형 $\mathrm{OAP}$의 넓이를 $S(t)$, 삼각형 $\mathrm{OQD}$의 넓이를 $T(t)$라 할 때, $\displaystyle\lim_{t\to0+}\frac{tT(t)}{S(t)}$의 값은?",
        choices=["0", "1/4", "1/2", "1", "2"], answer="0", trap_answer="1",
        trap_path="원문처럼 P, Q 의 y 좌표가 1 로 간다고 보고 tT/S → t·½/(½t)=1.",
        explanation=[
            r"$y_{\mathrm P}$는 $y^2+ty-t=0$의 양의 근이므로 $y_{\mathrm P}=\dfrac{-t+\sqrt{t^2+4t}}{2}$, $t\to0+$일 때 $y_{\mathrm P}\approx\sqrt t$이다.",
            r"$x_{\mathrm Q}=\dfrac{t-\sqrt{t^2+4t}}{2}\approx-\sqrt t$이므로 $y_{\mathrm Q}=x_{\mathrm Q}^2\approx t$이다.",
            r"함정: $t\to0+$에서는 P, Q가 원점으로 모이므로 좌표가 $1$로 가지 않는다.",
            r"$\dfrac{tT}{S}=\dfrac{t\cdot\frac12y_{\mathrm Q}}{\frac12t\,y_{\mathrm P}}\approx\dfrac{t}{\sqrt t}=\sqrt t\to0$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (D(−1,0) → D(−2,0))",
        changed=["D(−1,0) → D(−2,0)"], naturalness="",
        stem=r"양의 실수 $t$에 대하여 좌표평면 위에 네 점 $\mathrm{A}(t,\,0)$, $\mathrm{B}(0,\,1)$, $\mathrm{C}(0,\,t)$, $\mathrm{D}(-2,\,0)$이 있다. 곡선 $y=\sqrt x$가 선분 $\mathrm{AB}$와 만나는 점을 $\mathrm{P}$, 곡선 $y=x^2\,(x<0)$이 선분 $\mathrm{CD}$와 만나는 점을 $\mathrm{Q}$라 하자. 원점 $\mathrm{O}$에 대하여 삼각형 $\mathrm{OAP}$의 넓이를 $S(t)$, 삼각형 $\mathrm{OQD}$의 넓이를 $T(t)$라 할 때, $\displaystyle\lim_{t\to\infty}\frac{tT(t)}{S(t)}$의 값은?",
        choices=["2", "4", "6", "8", "10"], answer="8", trap_answer=None, trap_path=None,
        explanation=[
            r"$t\to\infty$일 때 P는 $(1,\,1)$로 가므로 $S(t)\approx\dfrac t2$이다.",
            r"직선 CD는 $y=\dfrac t2(x+2)$이므로 $t\to\infty$일 때 Q는 $(-2,\,4)$로 간다.",
            r"$T(t)\to\dfrac12\times2\times4=4$이다.",
            r"$\dfrac{tT}{S}\to\dfrac{4t}{t/2}=8$이다.",
        ],
    ),
]

t = Symbol('t', positive=True)


def ratio(d):
    y = Symbol('y', positive=True)
    yP = [s for s in solve(Eq(y, 1 - y**2/t), y)][0]  # P: x=y², AB: y=1−x/t
    X = Symbol('X', real=True)
    xs = [s for s in solve(Eq(X**2, t*(X + d)/d), X)]
    xQ = [s for s in xs if s.subs(t, 1).evalf() < 0][0]
    S = t*yP/2
    T = d*xQ**2/2
    return simplify(t*T/S), xQ


def verify(c):
    for d in (1, 2):
        r, xQ = ratio(d)
        c.check(f"d={d}: Q 가 선분 CD 위 (−d<x_Q<0)", all(-d < xQ.subs(t, tv) < 0 for tv in (Rational(1, 100), 1, 100)))
    c.ans('orig', limit(ratio(1)[0], t, oo))
    c.ans(1, limit(ratio(1)[0], t, 0, '+'))
    c.trap(1, limit(ratio(1)[0], t, oo))
    c.ans(2, limit(ratio(2)[0], t, oo))
