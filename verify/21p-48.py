from lib import *

ORIG = dict(
    id="21p-48", chapter=1, page=21, num=48, source="2025년 수능특강 [25009-0026]", type="객관식",
    stem=r"그림과 같이 한 변의 길이가 $1$인 정사각형 $\mathrm{ABCD}$가 있다. $0<t<1$인 실수 $t$에 대하여 선분 $\mathrm{CD}$ 위에 점 $\mathrm P$를 $\overline{\mathrm{CP}}=t$가 되도록 잡고 선분 $\mathrm{AD}$ 위에 점 $\mathrm Q$를 $\overline{\mathrm{DQ}}=\frac t2$가 되도록 잡을 때, 선분 $\mathrm{BP}$와 선분 $\mathrm{CQ}$의 교점을 $\mathrm R$이라 하자. 삼각형 $\mathrm{CPR}$의 넓이를 $S(t)$라 할 때, $\displaystyle\lim_{t\to0+}\frac{S(t)}{t^3}$의 값은? (A는 왼쪽 위, D는 오른쪽 위, B는 왼쪽 아래, C는 오른쪽 아래 꼭짓점)",
    choices=["1/8", "1/4", "3/8", "1/2", "5/8"], answer="1/4",
    general="B(0,0), C(1,0), P(1,t), Q(1−t/2, 1). BP: y=tx, CQ: (1−(t/2)s, s). 교점 s=t/(1+t²/2). S=½·CP·(R 에서 CD 까지 거리)=½·t·(t/2)s → t³/4 → 1/4.",
    special="① R→C 라서 높이 ≈ (t/2)·t 로 1차 근사 — Q 가 AD 위라 CQ 가 거의 수직이기 때문. Q 를 AB 위로 옮기면 R 이 C 로 가지 않음.",
    perspective="넓이의 t 에 대한 주요 차수 = 밑변 차수 + 높이 차수.",
    table=[
        ("Q 가 변 AD 위", "R 이 C 에서 먼 경우", "Q 를 AB 위(BQ=t/2)로 옮기면 R=(1/3, t/3) 고정 → S~t/3"),
        ("DQ=t/2", "—", "DQ=2t 면 계수만 바뀜 (생존)"),
    ],
    sweep=["R 의 x 좌표: Q 가 AD 위 → 1, Q 가 AB 위 → 1/3"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (R 이 C 로 모이지 않음 → 차수 변화)",
        changed=["Q: 선분 AD 위 DQ=t/2 → 선분 AB 위 BQ=t/2", "묻는 값 S/t³ → S/t"],
        naturalness="Q 의 위치를 바꾸면 S 가 1차가 되어 S/t³ 이 발산하므로 묻는 값의 차수를 맞춘 것은 필수.",
        stem=r"한 변의 길이가 $1$인 정사각형 $\mathrm{ABCD}$가 있다. ($\mathrm A$는 왼쪽 위, $\mathrm D$는 오른쪽 위, $\mathrm B$는 왼쪽 아래, $\mathrm C$는 오른쪽 아래 꼭짓점) $0<t<1$인 실수 $t$에 대하여 선분 $\mathrm{CD}$ 위에 점 $\mathrm P$를 $\overline{\mathrm{CP}}=t$가 되도록 잡고 선분 $\mathrm{AB}$ 위에 점 $\mathrm Q$를 $\overline{\mathrm{BQ}}=\frac t2$가 되도록 잡을 때, 선분 $\mathrm{BP}$와 선분 $\mathrm{CQ}$의 교점을 $\mathrm R$이라 하자. 삼각형 $\mathrm{CPR}$의 넓이를 $S(t)$라 할 때, $\displaystyle\lim_{t\to0+}\frac{S(t)}{t}$의 값은?",
        choices=["0", "1/6", "1/4", "1/3", "1/2"], answer="1/3", trap_answer="0",
        trap_path="원문처럼 R→C 로 보고 높이를 t² 차수로 잡아 S~t³ → S/t→0.",
        explanation=[
            r"$\mathrm B(0,0)$, $\mathrm C(1,0)$, $\mathrm P(1,t)$, $\mathrm Q(0,\frac t2)$로 두면 BP: $y=tx$, CQ: $y=\frac t2(1-x)$이다.",
            r"$tx=\frac t2(1-x)$에서 $x=\frac13$이므로 $\mathrm R\left(\frac13,\,\frac t3\right)$이다.",
            r"함정: R은 C로 다가가지 않고 $x=\frac13$에 고정된다.",
            r"$S(t)=\frac12\times t\times\left(1-\frac13\right)=\frac t3$이므로 극한은 $\frac13$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (DQ=t/2 → 2t)",
        changed=["DQ=t/2 → 2t (0<t<1/2)"], naturalness="",
        stem=r"한 변의 길이가 $1$인 정사각형 $\mathrm{ABCD}$가 있다. ($\mathrm A$는 왼쪽 위, $\mathrm D$는 오른쪽 위, $\mathrm B$는 왼쪽 아래, $\mathrm C$는 오른쪽 아래 꼭짓점) $0<t<\frac12$인 실수 $t$에 대하여 선분 $\mathrm{CD}$ 위에 점 $\mathrm P$를 $\overline{\mathrm{CP}}=t$가 되도록 잡고 선분 $\mathrm{AD}$ 위에 점 $\mathrm Q$를 $\overline{\mathrm{DQ}}=2t$가 되도록 잡을 때, 선분 $\mathrm{BP}$와 선분 $\mathrm{CQ}$의 교점을 $\mathrm R$이라 하자. 삼각형 $\mathrm{CPR}$의 넓이를 $S(t)$라 할 때, $\displaystyle\lim_{t\to0+}\frac{S(t)}{t^3}$의 값은?",
        choices=["1/4", "1/2", "3/4", "1", "5/4"], answer="1", trap_answer=None, trap_path=None,
        explanation=[
            r"BP: $y=tx$, CQ 위의 점을 $(1-2ts,\,s)$로 두면 교점에서 $s=\dfrac{t}{1+2t^2}$이다.",
            r"R에서 직선 CD까지의 거리는 $2ts=\dfrac{2t^2}{1+2t^2}$이다.",
            r"$S(t)=\frac12\times t\times\dfrac{2t^2}{1+2t^2}$이므로 $\displaystyle\lim_{t\to0+}\frac{S(t)}{t^3}=1$이다.",
        ],
    ),
]

t = Symbol('t', positive=True)


def area(Q):
    s = Symbol('s', real=True)
    C, P = (1, 0), (1, t)
    Rx, Ry = C[0] + (Q[0] - C[0])*s, C[1] + (Q[1] - C[1])*s
    sv = solve(Eq(Ry, t*Rx), s)[0]
    R = (simplify(Rx.subs(s, sv)), simplify(Ry.subs(s, sv)))
    return simplify(Abs((P[0] - C[0])*(R[1] - C[1]) - (R[0] - C[0])*(P[1] - C[1]))/2), R, sv


def verify(c):
    S, R, sv = area((1 - t/2, 1))
    c.check("원문: R 이 선분 위 (0<s<1)", 0 < sv.subs(t, Rational(1, 2)) < 1)
    c.ans('orig', limit(S/t**3, t, 0, '+'))
    S, R, sv = area((0, t/2))
    c.check("1: R=(1/3, t/3)", simplify(R[0] - Rational(1, 3)) == 0 and simplify(R[1] - t/3) == 0)
    c.ans(1, limit(S/t, t, 0, '+'))
    S0, _, _ = area((1 - t/2, 1))
    c.trap(1, limit(S0/t, t, 0, '+'))
    S, R, sv = area((1 - 2*t, 1))
    c.ans(2, limit(S/t**3, t, 0, '+'))
