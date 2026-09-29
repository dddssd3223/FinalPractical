from lib import *

G_TXT = r"g(x)=\begin{cases}-f(x) & (x<t)\\ f(x) & (x\ge t)\end{cases}"

def box(second):
    return [r"(가) 모든 실수 $a$에 대하여 $\displaystyle\lim_{x\to a+}\frac{g(x)}{x(x-2)}$의 값이 존재한다.",
            r"(나) $\displaystyle\lim_{x\to m+}\frac{g(x)}{x(x-2)}$의 값이 음수가 되도록 하는 자연수 $m$의 집합은 $\left\{g(-1),\,"
            + second + r"\right\}$이다."]

def stem(ask, note):
    return (r"최고차항의 계수가 양수인 삼차함수 $f(x)$와 실수 $t$에 대하여 함수 $" + G_TXT + r"$는 실수 전체의 집합에서 연속이고 다음 조건을 만족시킨다. $" + ask + r"$의 값을 구하시오. (단, " + note + r")")

ORIG = dict(
    id="51p-55", chapter=2, page=51, num=55, source="2026학년도 대수능 21번", type="주관식",
    stem=stem("g(-5)", r"$g(-1)\neq-\frac72g(1)$") + " [4점]", box=box(r"-\frac72g(1)"), answer="65",
    general="g 연속 → f(t)=0. (가) x→0+, 2+ 에서 분모→0 → g(0)=g(2)=0 → f(0)=f(2)=0. 셋째 근을 r 라 하면 x(x−2) 로 약분되어 오른쪽 극한 = sgn·k(m−r) (sgn=−1 (m<t), +1 (m≥t)). t∉{0,2} 이면 r=t 라 값이 음수가 되는 m 이 없음 → t∈{0,2}. t=0: 음수인 m 은 m<s, 그런데 −7/2 g(1)<0 이라 불가. t=2: 원소 {2,3} (3<s≤4), g(−1)=3k(1+s), −7/2 g(1)=7k(s−1)/2 → g(−1)=3, −7/2g(1)=2 → s=11/3, k=3/14. g(−5)=−f(−5)=65.",
    special="① t 를 f 의 셋째 근으로 두는 것(t∉{0,2}) — 이 경우 (나)의 집합이 비어 불가. ② t=0 과 t=2 중 어느 쪽인지를 (나)의 두 원소의 부호로 가름 — −7/2 g(1) 의 부호가 t=0 경우를 배제.",
    perspective="g/(x(x−2)) = ±k(x−r) 인 꺾은 일차함수로 보기.",
    table=[
        ("(나) 의 −7/2 g(1)", "t=0 경우 (g(1)>0 이라 음수)", "7/2 g(1) 로 바꾸면 t=0 경우가 답, t=2 는 불가"),
        ("묻는 값 g(−5)", "—", "g(−12) 로 바꾸면 계산만 바뀜 (생존)"),
    ],
    sweep=["t∈{0,2} vs 셋째 근", "원소 개수 2 ⇔ s 의 범위 (t=2: 3<s≤4, t=0: 2<s≤3)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (부호가 바뀌어 t=0 경우가 살아나고 t=2 는 불가)",
        changed=["(나) 의 −7/2 g(1) → 7/2 g(1) (단서도 같이)"], naturalness="",
        stem=stem("g(-5)", r"$g(-1)\neq\frac72g(1)$"), box=box(r"\frac72g(1)"), answer="50", trap_answer="65",
        trap_path="원문처럼 t=2 로 두고 g(1) 의 부호를 무시해 g(−1)=3, 7/2|g(1)|=2 로 풀면 원문의 f → 65 (t=2 이면 7/2 g(1)<0 이라 자연수가 될 수 없음).",
        explanation=[
            r"원문과 같이 $f(0)=f(2)=0$이고 $t\in\{0,2\}$이며, $f(x)=kx(x-2)(x-s)$, $\dfrac{g(x)}{x(x-2)}=\pm k(x-s)$이다.",
            r"$t=2$: 음수가 되는 $m$은 $2\le m<s$이고 $g(1)=-f(1)=-k(s-1)<0$이라 $\frac72g(1)$이 자연수가 될 수 없다. 함정: 원문의 경우가 여기서는 불가능하다.",
            r"$t=0$: 모든 자연수 $m$에서 부호는 $+$이므로 음수 ⇔ $m<s$, 원소 $\{1,2\}$에서 $2<s\le3$이다.",
            r"$g(-1)=-f(-1)=3k(1+s)$, $\frac72g(1)=\frac72k(s-1)$. $3k(1+s)=2$, $\frac72k(s-1)=1$에서 $s=\frac52$, $k=\frac4{21}$이다.",
            r"$g(-5)=-f(-5)=-\frac4{21}(-5)(-7)\left(-\frac{15}2\right)=50$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (묻는 값 g(−5) → g(−12))",
        changed=["묻는 값 g(−5) → g(−12)"], naturalness="",
        stem=stem("g(-12)", r"$g(-1)\neq-\frac72g(1)$"), box=box(r"-\frac72g(1)"), answer="564", trap_answer=None, trap_path=None,
        explanation=[
            r"원문과 같이 $t=2$, $f(x)=\frac3{14}x(x-2)\left(x-\frac{11}3\right)$이다.",
            r"$-12<t$이므로 $g(-12)=-f(-12)$이다.",
            r"$-f(-12)=-\frac3{14}(-12)(-14)\left(-\frac{47}3\right)=564$이다.",
        ],
    ),
]


def build(k, s, t):
    f = k*x*(x - 2)*(x - s)
    return f, (lambda v: -f.subs(x, v) if v < t else f.subs(x, v))


def right_lim(f, t, m):
    piece = -f if m < t else f
    return limit(piece/(x*(x - 2)), x, m, '+')


def check(k, s, t, second_coef):
    f, g = build(k, s, t)
    if f.subs(x, t) != 0:
        return False
    # (가): 모든 a 에서 오른쪽 극한 존재 (0, 2 포함 표본)
    for a in [0, 2, t, Rational(1, 3), -3, 5]:
        if not right_lim(f, t, a).is_finite:
            return False
    neg = {m for m in range(1, 30) if right_lim(f, t, m) < 0}
    target = {g(-1), second_coef*g(1)}
    return len(target) == 2 and neg == target


def solve_all(second_coef):
    """t∈{0,2} 경우를 s,k 연립으로 풀고, t 가 셋째 근인 경우는 집합이 비어 불가함을 표본으로 확인"""
    k, s = symbols('k s', positive=True)
    found = []
    for t in (0, 2):
        f = k*x*(x - 2)*(x - s)
        gm1 = -f.subs(x, -1) if -1 < t else f.subs(x, -1)
        g1 = (-f.subs(x, 1) if 1 < t else f.subs(x, 1))*second_coef
        for A, B in ((1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1), (3, 4), (4, 3), (2, 4), (4, 2)):
            for sol in solve([gm1 - A, g1 - B], [k, s], dict=True):
                kv, sv = sol[k], sol[s]
                if kv > 0 and check(kv, sv, t, second_coef):
                    found.append((kv, sv, t))
    return found


def verify(c):
    # 셋째 근 = t (t∉{0,2}) 이면 음수가 되는 m 이 없음
    c.check("t 가 셋째 근이면 (나)의 집합이 빔", all(
        not {m for m in range(1, 20) if right_lim(Rational(1)*x*(x - 2)*(x - tv), tv, m) < 0} for tv in (Rational(7, 2), 5, -1)))
    r = solve_all(-Rational(7, 2))
    c.check("원문: 해 하나 (t=2, s=11/3, k=3/14)", r == [(Rational(3, 14), Rational(11, 3), 2)])
    kv, sv, t = r[0]
    f, g = build(kv, sv, t)
    c.ans('orig', g(-5))
    c.ans(2, g(-12))
    r1 = solve_all(Rational(7, 2))
    c.check("1: 해 하나 (t=0, s=5/2, k=4/21)", r1 == [(Rational(4, 21), Rational(5, 2), 0)])
    kv, sv, t = r1[0]
    f1, g1 = build(kv, sv, t)
    c.ans(1, g1(-5))
    c.trap(1, g(-5))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
