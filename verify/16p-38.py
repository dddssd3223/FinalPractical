from lib import *

ORIG = dict(
    id="16p-38", chapter=1, page=16, num=38, source="2022년 수능특강 [22009-0022]", type="객관식",
    stem=r"다항식 $f(x)$를 $(x-2)^2$으로 나누었을 때의 몫을 $Q(x)$, 나머지를 $R(x)$라 하자. $Q(2)=R(2)$일 때, $\displaystyle\lim_{x\to2}\frac{f(x)+2x^2}{f(x)-R(x)}=k$이다. 상수 $k$의 값은?",
    choices=["3/4", "1", "5/4", "3/2", "7/4"], answer="3/4",
    general="f−R=(x−2)²Q → 분모 이중근. 분자 (x−2)²Q+R+2x² 에서 R+2x² 가 이중근을 가져야 함: 2x²+ax+b=2(x−2)² → R=−8x+8, R(2)=−8=Q(2). k=1+2/Q(2)=3/4.",
    special="① R+2x² 가 이차식이라 2(x−2)² 로 맞출 수 있음 — 분자에 붙은 식이 일차면 항등적으로 0 이어야 함. ② k=1+2/Q(2) 는 Q(2)≠0 일 때만.",
    perspective="분자·분모에서 공통인 (x−2)²Q 를 떼면 (R+2x²)/((x−2)²Q) 만 남는다.",
    table=[
        ("분자의 2x² (이차식)", "R+(더한 식) 이 이중근을 못 갖는 경우", "일차식 2x 로 바꾸면 R+2x≡0 이어야 함 → k=1"),
        ("Q(2)=R(2)", "Q(2)=0 (분모 삼중근)", "Q(2)=−R(2) 등으로 바꾸면 k 만 바뀜 (생존)"),
    ],
    sweep=["더한 식의 차수 < 2 이면 이중근 조건이 항등식으로", "Q(2)=0 이면 극한 발산"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 9 (차수 조건: 일차식은 이중근을 가질 수 없음)",
        changed=["분자 f(x)+2x² → f(x)+2x"], naturalness="",
        stem=r"다항식 $f(x)$를 $(x-2)^2$으로 나누었을 때의 몫을 $Q(x)$, 나머지를 $R(x)$라 하자. $Q(2)=R(2)$일 때, $\displaystyle\lim_{x\to2}\frac{f(x)+2x}{f(x)-R(x)}=k$이다. 상수 $k$의 값은?",
        choices=["1/2", "3/4", "1", "5/4", "3/2"], answer="1", trap_answer="1/2",
        trap_path="원문처럼 R+2x=2(x−2)² 꼴로 두고 k=1+2/Q(2), Q(2)=R(2)=−4 → 1/2 (일차식 R+2x 는 이중근을 가질 수 없음).",
        explanation=[
            r"$f(x)-R(x)=(x-2)^2Q(x)$이므로 분자는 $(x-2)^2Q(x)+\{R(x)+2x\}$이다.",
            r"극한이 존재하려면 $R(x)+2x$가 $(x-2)^2$을 인수로 가져야 한다.",
            r"함정: $R(x)+2x$는 일차 이하의 식이므로 $R(x)+2x=0$, 즉 $R(x)=-2x$뿐이다.",
            r"이때 $Q(2)=R(2)=-4\neq0$이고 $k=\displaystyle\lim_{x\to2}\frac{(x-2)^2Q(x)}{(x-2)^2Q(x)}=1$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (Q(2)=R(2) → Q(2)=−R(2))",
        changed=["Q(2)=R(2) → Q(2)=−R(2)"], naturalness="",
        stem=r"다항식 $f(x)$를 $(x-2)^2$으로 나누었을 때의 몫을 $Q(x)$, 나머지를 $R(x)$라 하자. $Q(2)=-R(2)$일 때, $\displaystyle\lim_{x\to2}\frac{f(x)+2x^2}{f(x)-R(x)}=k$이다. 상수 $k$의 값은?",
        choices=["3/4", "1", "5/4", "3/2", "7/4"], answer="5/4", trap_answer=None, trap_path=None,
        explanation=[
            r"분자는 $(x-2)^2Q(x)+\{R(x)+2x^2\}$이므로 $R(x)+2x^2=2(x-2)^2$, $R(x)=-8x+8$이다.",
            r"$R(2)=-8$이므로 $Q(2)=-R(2)=8$이다.",
            r"$k=1+\dfrac{2}{Q(2)}=1+\dfrac28=\dfrac54$이다.",
        ],
    ),
]


def solve_k(add, rel):
    a, b, q0, q1 = symbols('a b q0 q1', real=True)
    Q = q0 + q1*(x - 2)
    R = a*x + b
    f = (x - 2)**2*Q + R
    N = f + add
    eqs = [N.subs(x, 2), diff(N, x).subs(x, 2), rel(Q.subs(x, 2), R.subs(x, 2))]
    out = set()
    for s in solve(eqs, [a, b, q0], dict=True):
        if simplify(Q.subs(x, 2).subs(s)) == 0:
            continue
        L = simplify(limit((N/(f - R)).subs(s), x, 2))
        out.add(L)
    return out


def verify(c):
    r = solve_k(2*x**2, lambda Q2, R2: Q2 - R2)
    c.check("원문: k 하나", len(r) == 1)
    c.ans('orig', list(r)[0])
    r = solve_k(2*x, lambda Q2, R2: Q2 - R2)
    c.check("1: k 하나", len(r) == 1)
    c.ans(1, list(r)[0])
    c.trap(1, 1 + Rational(2, -4))
    r = solve_k(2*x**2, lambda Q2, R2: Q2 + R2)
    c.check("2: k 하나", len(r) == 1)
    c.ans(2, list(r)[0])
