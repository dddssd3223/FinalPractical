from lib import *

def stem(d, ask, sgn):
    return (r"최고차항의 계수가 양수인 삼차함수 $f(x)$에 대하여 곡선 $y=f(x)$와 직선 $y=\frac12x$가 서로 다른 세 점 $\mathrm O$, $\mathrm A$, $\mathrm B$에서 만난다. "
            r"곡선 $y=f(x)$ 위의 점 $\mathrm A$에서의 접선이 $x$축과 만나는 점을 $\mathrm C$라 하자. $\overline{\mathrm{OA}}=\overline{\mathrm{AB}}$이고 $\overline{\mathrm{OC}}=\overline{\mathrm{BC}}=" + d
            + r"$일 때, $f(" + ask + r")$의 값을 구하시오. (단, 점 $\mathrm A$의 $x$좌표는 " + sgn + r"이고, $\mathrm O$는 원점이다.)")

ORIG = dict(
    id="81p-7", chapter=4, page=81, num=7, source="2025년 수능완성 [25054-0143]", type="주관식",
    stem=stem(r"\frac52", "6", "양수"), answer="33",
    general="A 는 OB 의 중점: A(t,t/2), B(2t,t). C(c,0), OC=BC → c=5t/4=5/2 → t=2. 접선 기울기 (1−0)/(2−5/2)=−2. f−x/2=kx(x−2)(x−4), f'(2)=1/2−4k=−2 → k=5/8 → f(6)=3+30=33.",
    special="① t>0 조건으로 A 가 오른쪽 — t<0 이면 세 점이 왼쪽에 놓여 f(6) 이 크게 바뀜.",
    perspective="등거리 → 수직이등분선, 중점 → 근의 배치.",
    table=[
        ("A 의 x좌표 양수 (t=2)", "음수 (t=−2)", "음수면 f−x/2=(5/8)x(x+2)(x+4) → f(6)=303"),
        ("OC=5/2", "—", "5/4 면 t=1, k=5/2 → f(4)=62 (생존)"),
    ],
    sweep=["c=5t/4, |c|=d → t=±4d/5"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (A 의 위치 부호)",
        changed=["단서 A 의 x좌표 양수 → 음수"], naturalness="",
        stem=stem(r"\frac52", "6", "음수"), answer="303", trap_answer="33",
        trap_path="원문처럼 A(2,1), B(4,2) 로 두어 33 (A 가 음수 쪽이라 A(−2,−1), B(−4,−2)).",
        explanation=[
            r"A가 OB의 중점이므로 $\mathrm A(t,\frac t2)$, $\mathrm B(2t,t)$이고, $\overline{\mathrm{OC}}=\overline{\mathrm{BC}}$에서 $\mathrm C(\frac{5t}4,0)$이다.",
            r"함정: $t<0$이므로 $\frac{5|t|}4=\frac52$에서 $t=-2$, $\mathrm A(-2,-1)$, $\mathrm C(-\frac52,0)$이다.",
            r"접선의 기울기는 $\frac{-1-0}{-2+\frac52}=-2$이고 $f(x)-\frac x2=kx(x+2)(x+4)$에서 $f'(-2)=\frac12-4k=-2$, $k=\frac58$이다.",
            r"$f(6)=3+\frac58\times6\times8\times10=303$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (OC=5/2 → 5/4)",
        changed=["OC=BC=5/2 → 5/4", "묻는 값 f(6) → f(4)"],
        naturalness="거리를 바꾸면 f(6)=303 으로 커져서 f(4) 를 묻는다.",
        stem=stem(r"\frac54", "4", "양수"), answer="62", trap_answer=None, trap_path=None,
        explanation=[
            r"$\mathrm C(\frac{5t}4,0)$에서 $t=1$, $\mathrm A(1,\frac12)$, $\mathrm B(2,1)$이다.",
            r"접선 기울기 $\frac{1/2}{1-5/4}=-2$이고 $f-\frac x2=kx(x-1)(x-2)$에서 $\frac12-k=-2$, $k=\frac52$이다.",
            r"$f(4)=2+\frac52\times4\times3\times2=62$이다.",
        ],
    ),
]


def solve_f(d, positive, ask):
    t, k, cc = symbols('t k cc', real=True)
    out = set()
    for tv in solve(Abs(Rational(5, 4)*t) - d, t):
        if (tv > 0) != positive:
            continue
        A, B = (tv, tv/2), (2*tv, tv)
        cv = solve((cc)**2 - ((cc - B[0])**2 + B[1]**2), cc)[0]
        assert abs(cv) == d
        f = x/2 + k*x*(x - A[0])*(x - B[0])
        slope = (A[1] - 0)/(A[0] - cv)
        for kv in solve(diff(f, x).subs(x, A[0]) - slope, k):
            if kv > 0:
                F = f.subs(k, kv)
                assert simplify(F.subs(x, A[0]) - A[1]) == 0
                out.add(F.subs(x, ask))
    assert len(out) == 1
    return out.pop()


def verify(c):
    c.ans('orig', solve_f(Rational(5, 2), True, 6))
    c.ans(1, solve_f(Rational(5, 2), False, 6))
    c.trap(1, solve_f(Rational(5, 2), True, 6))
    c.ans(2, solve_f(Rational(5, 4), True, 4))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '좌우 대칭 이동뿐인 쉬운 변형'
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
