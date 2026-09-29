from lib import *

ORIG = dict(
    id="18p-42", chapter=1, page=18, num=42, source="2024년 수능특강 [24009-0025]", type="주관식",
    stem=r"함수 $f(x)=\begin{cases}\frac19(x+3)(x-3) & (x<0)\\ (x-\alpha)(x-\beta)(x-\gamma) & (0\le x<1)\\ -x+3 & (x\ge1)\end{cases}$의 그래프가 그림과 같고, 함수 $g(x)$는 최고차항의 계수가 $1$인 삼차함수이다. $-3<a<3$인 모든 실수 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{g(x)}{f(x)}$의 값이 존재할 때, $g(3)$의 값을 구하시오. (단, $\alpha$, $\beta$, $\gamma$는 서로 다른 상수이다.) [그림: $f(0)=1$, $0\le x<1$에서 $f(x)>0$, $\displaystyle\lim_{x\to1-}f(x)=0$, $f(1)=2$, $\displaystyle\lim_{x\to0-}f(x)=-1$]",
    answer="12",
    general="x=0: 좌극한 g(0)/(−1), 우극한 g(0)/1 → g(0)=0. x=1: 우극한 g(1)/2, 좌극한은 분모→0 → g(1)=0, 좌극한 g'(1)/m'(1) 이 우극한 0 과 같아야 → g'(1)=0. g=x(x−1)², g(3)=12. (−3,3) 안의 f 의 다른 근 없음.",
    special="① x=0 에서 좌·우 f 값이 달라(−1, 1) g(0)=0 이 나오는 것 — f 가 x=0 에서 연속이면 이 조건이 사라지고 대신 f 의 근에서 조건이 생김. ② 가운데 삼차식의 α, β, γ 를 구하려 드는 것(필요 없음).",
    perspective="g/f 의 극한이 존재하지 않을 수 있는 점 = f 의 불연속점 ∪ f 의 근. 각 점에서 좌·우를 따로.",
    table=[
        ("x=0 에서 f 의 점프(−1 → 1)", "f 가 0 에서 연속인 경우", "왼쪽 조각을 x+1 로 바꾸면 x=0 조건 소멸, 대신 근 x=−1 에서 g(−1)=0"),
        ("오른쪽 f(1)=2 ≠ 0", "양쪽 모두 0 인 경우", "—"),
        ("g 최고차 1", "—", "2 로 바꾸면 g=2x(x−1)² (생존)"),
    ],
    sweep=["f 의 근: ±3 (왼쪽 조각, x<0 에서는 −3 만), 1(가운데), 3(오른쪽)", "구간 (−3,3) 끝점 제외"],
)

MID_TXT = r"$0\le x<1$에서 $f(x)=(x-\alpha)(x-\beta)(x-\gamma)>0$, $f(0)=1$, $\displaystyle\lim_{x\to1-}f(x)=0$"

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (x=0 의 점프가 사라지고 왼쪽 조각의 근 x=−1 이 구간 안에 들어옴)",
        changed=["x<0 조각 ⅑(x+3)(x−3) → x+1"], naturalness="",
        stem=r"함수 $f(x)=\begin{cases}x+1 & (x<0)\\ (x-\alpha)(x-\beta)(x-\gamma) & (0\le x<1)\\ -x+3 & (x\ge1)\end{cases}$의 그래프가 그림과 같고, 함수 $g(x)$는 최고차항의 계수가 $1$인 삼차함수이다. $-3<a<3$인 모든 실수 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{g(x)}{f(x)}$의 값이 존재할 때, $g(3)$의 값을 구하시오. (단, $\alpha$, $\beta$, $\gamma$는 서로 다른 상수이다.)",
        answer="16", trap_answer="12",
        trap_path="원문처럼 x=0 에서 g(0)=0 을 쓰고 g=x(x−1)² → 12 (x=0 은 연속이라 조건이 없고, 대신 x=−1 이 f 의 근).",
        explanation=[
            r"$x\to0$에서 좌극한 $f\to1$, $f(0)=1$이므로 $f$는 $x=0$에서 연속이고 $0$이 아니다. 함정: 원문의 $g(0)=0$ 조건이 없다.",
            r"$x=-1$에서 $f(-1)=0$이므로 $g(-1)=0$이어야 한다.",
            r"$x=1$에서 우극한은 $\frac{g(1)}{2}$, 좌극한은 분모가 $0$으로 가므로 $g(1)=0$이고, 좌극한이 $0$이 되려면 $g'(1)=0$이다.",
            r"$g(x)=(x+1)(x-1)^2$이므로 $g(3)=4\times4=16$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 3행 (g 의 최고차항 계수 1 → 2)",
        changed=["g 의 최고차항 계수 1 → 2"], naturalness="",
        stem=r"함수 $f(x)=\begin{cases}\frac19(x+3)(x-3) & (x<0)\\ (x-\alpha)(x-\beta)(x-\gamma) & (0\le x<1)\\ -x+3 & (x\ge1)\end{cases}$에 대하여 " + MID_TXT + r"이다. 최고차항의 계수가 $2$인 삼차함수 $g(x)$에 대하여 $-3<a<3$인 모든 실수 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{g(x)}{f(x)}$의 값이 존재할 때, $g(3)$의 값을 구하시오. (단, $\alpha$, $\beta$, $\gamma$는 서로 다른 상수이다.)",
        answer="24", trap_answer=None, trap_path=None,
        explanation=[
            r"$x=0$에서 좌극한 $\frac{g(0)}{-1}$, 우극한 $\frac{g(0)}{1}$이 같아야 하므로 $g(0)=0$이다.",
            r"$x=1$에서 우극한 $\frac{g(1)}2$, 좌극한은 분모가 $0$으로 가므로 $g(1)=0$, 좌극한이 $0$이려면 $g'(1)=0$이다.",
            r"$g(x)=2x(x-1)^2$이므로 $g(3)=2\times3\times4=24$이다.",
        ],
    ),
]

MID = (x - 1)*(x + Rational(1, 2))*(x - 2)  # 조건을 만족시키는 가운데 조각의 한 예 (f(0)=1, [0,1) 에서 양수)


def solve_g(left, lead):
    p, q, r = symbols('p q r', real=True)
    g = lead*x**3 + p*x**2 + q*x + r
    P = [(left, -oo, 0), (MID, 0, 1), (-x + 3, 1, oo)]
    F = lambda e: g/e
    eqs = []
    # x=0: 좌·우극한 비교 (분모가 0 아니면 값 비교, 0 이면 분자 0)
    l0, r0 = left.subs(x, 0), MID.subs(x, 0)
    if l0 == 0:
        eqs.append(g.subs(x, 0))
    elif l0 != r0:
        eqs.append(g.subs(x, 0)/l0 - g.subs(x, 0)/r0)
    # f 의 근 (−3,3) 안: 왼쪽 조각의 근
    for z in solve(left, x):
        if -3 < z < 0:
            eqs.append(g.subs(x, z))
    # x=1: 좌측 분모→0 → g(1)=0, 좌극한 g'(1)/MID'(1) = 우극한 g(1)/2 = 0
    eqs += [g.subs(x, 1), diff(g, x).subs(x, 1)]
    sols = solve(eqs, [p, q, r], dict=True)
    out = []
    for s in sols:
        G = expand(g.subs(s))
        pts = [Rational(k, 4) for k in range(-11, 12)]
        if all(plim_exists(P, lambda e: G/e, a)[0] for a in pts):
            out.append(G)
    return out


def verify(c):
    c.check("가운데 조각 예시: f(0)=1, [0,1) 양수, 1 에서 0", MID.subs(x, 0) == 1 and MID.subs(x, 1) == 0
            and all(MID.subs(x, Rational(k, 10)) > 0 for k in range(10)))
    for key, left, lead in (('orig', (x + 3)*(x - 3)/9, 1), (1, x + 1, 1), (2, (x + 3)*(x - 3)/9, 2)):
        r = solve_g(left, lead)
        c.check(f"{key}: g 하나, 모든 a 에서 극한 존재", len(r) == 1)
        c.ans(key, r[0].subs(x, 3))
    c.trap(1, (x*(x - 1)**2).subs(x, 3))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
