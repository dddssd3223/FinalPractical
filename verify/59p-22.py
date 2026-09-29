from lib import *

def stem(den, rhs, f0, fp0):
    return (r"다항함수 $f(x)$가 모든 실수 $x$에 대하여 $\displaystyle\lim_{h\to0}\frac{f(h)f(x+h)-f(h)f(x)}{" + den + r"}=" + rhs + r"$를 만족시킨다. $f(0)=" + f0 + r"$, $f'(0)=" + fp0 + r"$일 때, $f'(3)$의 값을 구하시오.")

ORIG = dict(
    id="59p-22", chapter=3, page=59, num=22, source="2024년 수능특강 [24009-0055]", type="주관식",
    stem=stem("h^2", "2x^3+4", "0", "2"), answer="29",
    general="식 = (f(h)/h)·{(f(x+h)−f(x))/h} → f'(0)f'(x) (f(0)=0 이라 f(h)/h→f'(0)). 2f'(x)=2x³+4 → f'(x)=x³+2 → f'(3)=29.",
    special="① f(h)/h → f'(0) 은 f(0)=0 일 때만. 분모가 h 이고 f(0)≠0 이면 인수가 f(0) 이 됨.",
    perspective="극한식을 두 개의 극한(미분계수)으로 분해.",
    table=[
        ("분모 h², f(0)=0", "f(0)≠0 (f(h)/h 발산)", "분모 h, f(0)=1 이면 f(0)f'(x)=2x³+4"),
        ("우변 2x³+4", "—", "2x³+2x+4 면 f'=x³+x+2 (생존)"),
    ],
    sweep=["f(0)=0 여부에 따라 앞 인수가 f'(0) 또는 f(0)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (f(0)≠0 이면 앞 인수가 f'(0) 이 아니라 f(0))",
        changed=["분모 h² → h", "f(0)=0 → f(0)=1"],
        naturalness="분모를 h 로 바꾸면 f(0)=0 일 때 극한이 0 이 되어 조건이 성립할 수 없으므로 f(0) 을 함께 바꾼 것.",
        stem=stem("h", "2x^3+4", "1", "4"), answer="58", trap_answer="29/2",
        trap_path="원문처럼 앞 인수를 f'(0)=4 로 보아 4f'(x)=2x³+4 → f'(3)=29/2 (분모가 h 라 앞 인수는 f(0)=1).",
        explanation=[
            r"$\dfrac{f(h)f(x+h)-f(h)f(x)}{h}=f(h)\cdot\dfrac{f(x+h)-f(x)}{h}$이다.",
            r"$h\to0$일 때 $f(h)\to f(0)=1$이므로 극한은 $f'(x)$이다.",
            r"함정: 분모가 $h$ 하나뿐이라 $f(h)$는 $\frac{f(h)}h$가 아니고 그대로 $f(0)$으로 간다.",
            r"$f'(x)=2x^3+4$이므로 $f'(3)=58$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (우변 2x³+4 → 2x³+2x+4)",
        changed=["우변 2x³+4 → 2x³+2x+4"], naturalness="",
        stem=stem("h^2", "2x^3+2x+4", "0", "2"), answer="32", trap_answer=None, trap_path=None,
        explanation=[
            r"식은 $\dfrac{f(h)}{h}\cdot\dfrac{f(x+h)-f(x)}{h}$이고 $f(0)=0$이므로 $f'(0)f'(x)=2f'(x)$로 간다.",
            r"$2f'(x)=2x^3+2x+4$에서 $f'(x)=x^3+x+2$이다.",
            r"$f'(3)=27+3+2=32$이다.",
        ],
    ),
]


def solve_fp3(den_pow, rhs, f0, fp0):
    cs = symbols('c0:6')
    f = sum(ci*x**i for i, ci in enumerate(cs)).subs({cs[0]: f0, cs[1]: fp0})  # f(0), f'(0) 먼저 대입
    h = Symbol('h')
    L = limit((f.subs(x, h)*f.subs(x, x + h) - f.subs(x, h)*f)/h**den_pow, h, 0)
    eqs = Poly(expand(L - rhs), x).all_coeffs() + [f.subs(x, 0) - f0, diff(f, x).subs(x, 0) - fp0]
    sols = solve(eqs, cs[2:], dict=True)
    vals = {simplify(diff(f, x).subs(x, 3).subs(s)) for s in sols}
    return vals


def verify(c):
    for key, dp, rhs, f0, fp0 in (('orig', 2, 2*x**3 + 4, 0, 2), (1, 1, 2*x**3 + 4, 1, 4), (2, 2, 2*x**3 + 2*x + 4, 0, 2)):
        v = solve_fp3(dp, rhs, f0, fp0)
        c.check(f"{key}: f'(3) 하나", len(v) == 1)
        c.ans(key, v.pop())
    c.trap(1, (2*x**3 + 4).subs(x, 3)/4)
