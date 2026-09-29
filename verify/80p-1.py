from lib import *

ORIG = dict(
    id="80p-1", chapter=4, page=80, num=1, source="2024학년도 대수능 20번", type="주관식",
    stem=r"$a>\sqrt2$인 실수 $a$에 대하여 함수 $f(x)=-x^3+ax^2+2x$라 하자. 곡선 $y=f(x)$ 위의 점 $\mathrm{O}(0,\,0)$에서의 접선이 곡선 $y=f(x)$와 만나는 점 중 $\mathrm{O}$가 아닌 점을 $\mathrm{A}$라 하고, 곡선 $y=f(x)$ 위의 점 $\mathrm{A}$에서의 접선이 $x$축과 만나는 점을 $\mathrm{B}$라 하자. 점 $\mathrm{A}$가 선분 $\mathrm{OB}$를 지름으로 하는 원 위의 점일 때, $\overline{\mathrm{OA}}\times\overline{\mathrm{AB}}$의 값을 구하시오. [4점]",
    answer="25",
    general="O에서의 접선 y=2x와 연립 → x²(x−a)=0, A(a, 2a). f'(a)=2−a². A가 OB 지름 원 위 ⇔ ∠OAB=90° ⇔ 2(2−a²)=−1 ⇔ a²=5/2. OA×AB=2△OAB=OB×y_A=(2a³)(2a)=25.",
    special="① '원점 접선의 다른 교점 x=a' 암기 → 최고차계수가 −1이 아니거나 접점이 원점이 아니면 깨짐. ② 원 조건을 곧바로 기울기 곱 −1로만 처리 → '직각삼각형' 조건이면 꼭짓점별 분류가 빠짐. ③ B를 양의 x축에 두고 푸는 것은 a>√2 덕분.",
    perspective="f=−x³+ax²+mx로 두면 a²=m+1/m, OA×AB=(m²+1)².",
    table=[
        ("a>√2", "a=√2: A에서 접선 수평 → x축 교점 B 없음. 0<a<√2: B가 음의 x축", "지워도 답 불변. 단 y축으로 바꾸면 a=√2가 정답 경우로 살아남"),
        ("기준 축 x축", "수평 접선 경우(B 없음)", "y축이면 B(0, a³) 항상 존재 → ∠B=90° 가능"),
        ("도형 조건 '지름 원'", "직각 위치를 A로 고정", "'직각삼각형'이면 O·A·B별 분류"),
        ("고정 계수 2", "—", "m으로 바꿔도 논리 유지, 답 (m²+1)² → 생존 확인형"),
        ("최고차계수 −1", "'다른 교점 x=a' 지름길", "−k면 다른 교점 x=a/k"),
    ],
    sweep=["a=√m: A에서 접선 수평", "a=0: A=O, B=O", "x_B>0 ⇔ a>√m (원문 a>√2의 역할)",
           "직각 위치: x축 B → A에서만. y축 B → A(a²=m+1/m), B(a=√m). O는 불가"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A a>√2·x축·지름 원 행 / 3-C 10·11 (축 교체로 수평 접선 경우 부활, 직각 위치별 분류)",
        changed=["x축 → y축", "지름 원 조건 → 삼각형 OAB가 직각삼각형", "a>√2 → 양수 a"],
        naturalness="바꾼 조건 3개. 범위 완화는 축 교체로 살아난 a=√2 경우를 포함하려면 필수, 직각삼각형은 지름 원 조건의 일반화라 덧붙인 조건이 아님.",
        stem=r"양수 $a$에 대하여 함수 $f(x)=-x^3+ax^2+2x$라 하자. 곡선 $y=f(x)$ 위의 점 $\mathrm{O}(0,\,0)$에서의 접선이 곡선 $y=f(x)$와 만나는 점 중 $\mathrm{O}$가 아닌 점을 $\mathrm{A}$라 하고, 곡선 $y=f(x)$ 위의 점 $\mathrm{A}$에서의 접선이 $y$축과 만나는 점을 $\mathrm{B}$라 하자. 삼각형 $\mathrm{OAB}$가 직각삼각형이 되도록 하는 모든 $a$의 값에 대하여 삼각형 $\mathrm{OAB}$의 넓이의 합을 $S$라 할 때, $8S$의 값을 구하시오.",
        answer="41", trap_answer="25",
        trap_path="원문처럼 ∠OAB=90°만 보고 a²=5/2, S=25/8 → 8S=25. 점 B에서 직각인 경우(수평 접선, a=√2)를 놓침.",
        explanation=[
            r"O에서의 접선은 $y=2x$이고 $x^2(x-a)=0$에서 $\mathrm{A}(a,\,2a)$, $f'(a)=2-a^2$이다.",
            r"A에서의 접선의 $y$절편은 $a^3$이므로 $\mathrm{B}(0,\,a^3)$이고, OA의 기울기가 $2$라 $\angle\mathrm{O}\neq 90^\circ$이다.",
            r"(i) $\angle\mathrm{A}=90^\circ$: $2(2-a^2)=-1$, $a^2=\tfrac52$, 넓이 $\tfrac{a^4}{2}=\tfrac{25}{8}$",
            r"(ii) $\angle\mathrm{B}=90^\circ$: $f'(a)=0$, $a=\sqrt2$, 넓이 $\tfrac12\cdot 2\sqrt2\cdot\sqrt2=2$",
            r"함정: 원문은 $a>\sqrt2$와 $x$축으로 (ii)를 막아 두었지만 $y$축에서는 수평 접선도 B를 만든다.",
            r"$S=\tfrac{25}{8}+2=\tfrac{41}{8}$이므로 $8S=41$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 고정 계수 행 (2 → 3, 범위는 B 존재 조건 a>√m 에 맞춰 이동)",
        changed=["2x → 3x (범위 a>√2 → a>√3은 같은 역할로 따라감)"], naturalness="",
        stem=r"$a>\sqrt3$인 실수 $a$에 대하여 함수 $f(x)=-x^3+ax^2+3x$라 하자. 곡선 $y=f(x)$ 위의 점 $\mathrm{O}(0,\,0)$에서의 접선이 곡선 $y=f(x)$와 만나는 점 중 $\mathrm{O}$가 아닌 점을 $\mathrm{A}$라 하고, 곡선 $y=f(x)$ 위의 점 $\mathrm{A}$에서의 접선이 $x$축과 만나는 점을 $\mathrm{B}$라 하자. 점 $\mathrm{A}$가 선분 $\mathrm{OB}$를 지름으로 하는 원 위의 점일 때, $\overline{\mathrm{OA}}\times\overline{\mathrm{AB}}$의 값을 구하시오.",
        answer="100", trap_answer=None, trap_path=None,
        explanation=[
            r"O에서의 접선은 $y=3x$이고 $x^2(x-a)=0$에서 $\mathrm{A}(a,\,3a)$이다.",
            r"$f'(a)=3-a^2$이고 $\angle\mathrm{OAB}=90^\circ$이므로 $3(3-a^2)=-1$, $a^2=\tfrac{10}{3}$이다.",
            r"B의 $x$좌표는 $a-\dfrac{3a}{3-a^2}=10a$이다.",
            r"$\overline{\mathrm{OA}}\times\overline{\mathrm{AB}}=\overline{\mathrm{OB}}\times 3a=30a^2=100$이다.",
        ],
    ),
]


def setup(m, axis):
    a = Symbol('a', positive=True)
    f = -x**3 + a*x**2 + m*x
    s = diff(f, x).subs(x, a)
    A = (a, m*a)
    B = (a - m*a/s, 0) if axis == 'x' else (0, simplify(m*a - s*a))
    return a, f, A, B


def perp(P, Q, R):
    return simplify((Q[0]-P[0])*(R[0]-P[0]) + (Q[1]-P[1])*(R[1]-P[1]))


def area(P, Q, R):
    return Abs((Q[0]-P[0])*(R[1]-P[1]) - (R[0]-P[0])*(Q[1]-P[1])) / 2


def verify(c):
    O = (0, 0)
    # 원문
    a, f, A, B = setup(2, 'x')
    c.check("O 접선의 다른 교점 x=a", [r for r in solve(Eq(f, 2*x), x) if r != 0] == [a])
    sol = [s for s in solve(perp(A, O, B), a) if s > sqrt(2)]
    c.check("원문 해 유일", len(sol) == 1)
    av = sol[0]
    Av, Bv = [tuple(simplify(sympify(p).subs(a, av)) for p in P) for P in (A, B)]
    c.ans('orig', simplify(sqrt(Av[0]**2+Av[1]**2) * sqrt((Bv[0]-Av[0])**2 + (Bv[1]-Av[1])**2)))
    # 변형1: y축, 직각 위치 전수
    a, f, A, B = setup(2, 'y')
    cases = {n: [s for s in solve(perp(P, Q, R), a) if s.is_positive]
             for n, (P, Q, R) in {"O": (O, A, B), "A": (A, O, B), "B": (B, O, A)}.items()}
    c.check("1: O 직각 불가", cases["O"] == [])
    c.check("1: A 직각 a²=5/2, B 직각 a=√2", len(cases["A"]) == 1 and cases["B"] == [sqrt(2)])
    areas = {n: [simplify(area(O, *[tuple(sympify(p).subs(a, s) for p in P) for P in (A, B)])) for s in v]
             for n, v in cases.items()}
    c.check("1: 삼각형 퇴화 없음", all(ar != 0 for v in areas.values() for ar in v))
    c.ans(1, 8 * (sum(areas["A"]) + sum(areas["B"])))
    c.trap(1, 8 * sum(areas["A"]))
    # 변형2: m=3, a>√3
    a, f, A, B = setup(3, 'x')
    sol = [s for s in solve(perp(A, O, B), a) if s > sqrt(3)]
    c.check("2: 해 유일", len(sol) == 1)
    av = sol[0]
    Av, Bv = [tuple(simplify(sympify(p).subs(a, av)) for p in P) for P in (A, B)]
    c.check("2: B가 양의 x축", Bv[0] > 0)
    c.ans(2, simplify(sqrt(Av[0]**2+Av[1]**2) * sqrt((Bv[0]-Av[0])**2 + (Bv[1]-Av[1])**2)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
