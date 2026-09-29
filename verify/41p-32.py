from lib import *

def stem(cond_h, v):
    return (r"함수 $f(x)=\dfrac{ax+b}{x-2}$와 양의 실수 $t$에 대하여 $x$에 대한 방정식 $|f(x)|=t$의 서로 다른 실근의 개수를 $g(t)$라 하고, $x$에 대한 방정식 $|f(x)|=tx$의 서로 다른 실근의 개수를 $h(t)$라 할 때, 두 함수 $g(t)$, $h(t)$가 다음 조건을 만족시킨다. $f(4)+h(4)=" + v + r"$일 때, $f(b)$의 값은? (단, $a$, $b$는 상수이고, $2a+b\neq0$, $b>0$이다.)")

def box(cond_h):
    return [r"(가) 함수 $g(t)$는 $t=b$에서만 불연속이다.", r"(나) " + cond_h]

ORIG = dict(
    id="41p-32", chapter=2, page=41, num=32, source="2023년 수능특강 [23009-0047]", type="객관식",
    stem=stem(None, "-3"), box=box(r"함수 $h(t)$는 양의 실수 전체의 집합에서 연속이다."),
    choices=["-10", "-8", "-6", "-4", "-2"], answer="-6",
    general="f=a+(2a+b)/(x−2) 는 a 이외의 모든 값을 한 번씩 → g(t)=2, t=|a| 에서만 1 → |a|=b. a=b: x∈(0,2) 에서 |f| 와 직선 tx 가 접하는 t 에서 h 가 1→3 으로 바뀌어 불연속 → (나) 위반. a=−b: f=−b(x−1)/(x−2), h(t)=3 (항상) → f(4)+3=−3b/2+3=−3 → b=4, f(b)=f(4)=−6.",
    special="① (나)로 a=b 경우를 버리고 h≡3 을 씀 — (나)가 '연속'이라서. (나)를 '불연속점이 존재'로 바꾸면 a=b 만 남고 h(4) 는 t₀=b(2+√3)/2 와 4 의 대소로 1 또는 3.",
    perspective="h 의 변화는 x∈(0,2) 구간에서의 접선 기울기 t₀ 하나로 결정.",
    table=[
        ("(나) h 연속", "a=b (h 가 접선 기울기에서 점프)", "'불연속점 존재'로 바꾸면 a=b 가 답, h(4) 는 1 또는 3"),
        ("f(4)+h(4)=−3", "—", "−6 으로 바꾸면 b=6 (생존)"),
    ],
    sweep=["t₀=b(2+√3)/2: a=b 일 때 h 의 불연속점", "|a|=b (g 의 불연속점)"],
)
ORIG["stem"] = stem(None, "-3")

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (a=b 경우가 살아나고 h(4) 가 t₀ 와 4 의 대소로 갈림)",
        changed=["(나) h 연속 → h 가 불연속인 점이 존재", "f(4)+h(4)=−3 → 11"],
        naturalness="(나)를 뒤집으면 a=−b 갈래가 사라져 부호가 양수가 되므로 합의 값을 양수로 맞춘 것은 필수.",
        stem=stem(None, "11"), box=box(r"함수 $h(t)$가 불연속인 양수 $t$가 존재한다."),
        choices=["8", "10", "56/5", "12", "14"], answer="10", trap_answer="56/5",
        trap_path="원문처럼 h(4)=3 으로 두어 5b/2+3=11 → b=16/5 → f(b)=56/5 (이 b 에서는 t₀≈5.97>4 라 실제 h(4)=1).",
        explanation=[
            r"(가)에서 $|a|=b$이다. $a=-b$이면 $h(t)=3$으로 항상 연속이므로 (나)에 어긋나고, $a=b$, $f(x)=\dfrac{b(x+1)}{x-2}$이다.",
            r"$0<x<2$에서 $|f(x)|$와 직선 $y=tx$가 접하는 기울기는 $t_0=\dfrac{(2+\sqrt3)b}{2}$이고, $t<t_0$이면 $h(t)=1$, $t>t_0$이면 $h(t)=3$이다.",
            r"$f(4)=\dfrac{5b}{2}$이므로 $\dfrac{5b}2+h(4)=11$. 함정: $h(4)=3$이면 $b=\frac{16}5$인데 이때 $t_0>4$라 $h(4)=1$이 되어 모순이다.",
            r"$h(4)=1$이면 $b=4$, $t_0=4+2\sqrt3>4$로 맞는다. $f(b)=f(4)=10$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (f(4)+h(4)=−3 → −6)",
        changed=["f(4)+h(4)=−3 → −6"], naturalness="",
        stem=stem(None, "-6"), box=box(r"함수 $h(t)$는 양의 실수 전체의 집합에서 연속이다."),
        choices=["-15/2", "-6", "-9/2", "-3", "-3/2"], answer="-15/2", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)에서 $|a|=b$, (나)에서 $a=b$는 불가능하므로 $a=-b$, $f(x)=-\dfrac{b(x-1)}{x-2}$이고 $h(t)=3$이다.",
            r"$f(4)+3=-\dfrac{3b}2+3=-6$에서 $b=6$이다.",
            r"$f(6)=-\dfrac{6\times5}{4}=-\dfrac{15}2$이다.",
        ],
    ),
]
ORIG["stem"] = stem(None, "-3")

t = Symbol('t', positive=True)


def g_count(f, tv):
    num, den = fraction(together(f))
    sols = set()
    for s in (1, -1):
        for r in real_roots(Poly(expand(num - s*tv*den), x)):
            if r != 2:
                sols.add(r)
    return len(sols)


def h_count(f, tv):
    num, den = fraction(together(f))
    sols = set()
    for s in (1, -1):
        for r in real_roots(Poly(expand(num - s*tv*x*den), x)):
            if r != 2 and r > 0 and simplify(Abs(f.subs(x, r)) - tv*r) == 0:
                sols.add(r)
    return len(sols)


TS = [Rational(k, 2) for k in range(1, 25)]


def check_case(a, b):
    f = (a*x + b)/(x - 2)
    gv = {tv: g_count(f, tv) for tv in TS + [Integer(b)]}
    g_ok = all(v == 2 for tv, v in gv.items() if tv != b) and gv[Integer(b)] == 1
    hv = [h_count(f, tv) for tv in TS]
    return f, g_ok, len(set(hv)) == 1, hv


def solve_b(sign, v, want_h_const):
    """f(4)=b(4·sign+1)/2 이므로 h(4)∈{0,1,2,3} 마다 b 후보를 구하고 전체 조건을 확인"""
    out = []
    for h4 in range(0, 4):
        b = Rational(2)*(v - h4)/(4*sign + 1)
        if b <= 0:
            continue
        f, g_ok, h_const, hv = check_case(sign*b, b)
        if g_ok and h_const == want_h_const and h_count(f, 4) == h4:
            out.append((b, f))
    return out


def verify(c):
    r = solve_b(-1, -3, True) + solve_b(1, -3, True)
    c.check("원문: 해 하나 (a=−b, b=4)", len(r) == 1 and r[0][0] == 4)
    b, f = r[0]
    c.ans('orig', f.subs(x, b))
    r = solve_b(-1, 11, False) + solve_b(1, 11, False)
    c.check("1: 해 하나 (a=b, b=4)", len(r) == 1 and r[0][0] == 4)
    b, f = r[0]
    c.ans(1, f.subs(x, b))
    bt = Rational(16, 5)
    ft = bt*(x + 1)/(x - 2)
    c.check("1: 함정 b=16/5 에서는 h(4)=1 (3 이 아님)", h_count(ft, 4) == 1)
    c.trap(1, ft.subs(x, bt))
    r = solve_b(-1, -6, True) + solve_b(1, -6, True)
    c.check("2: 해 하나 (b=6)", len(r) == 1 and r[0][0] == 6)
    b, f = r[0]
    c.ans(2, f.subs(x, b))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
