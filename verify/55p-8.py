from lib import *

def stem(den):
    return (r"다항함수 $f(x)$가 다음 조건을 만족시킬 때, $\displaystyle\lim_{x\to-2}\frac{f(x)-f(-2)}{" + den + r"}$의 값을 구하시오.")

def box(b):
    return [r"(가) $x$의 값이 $-2$에서 $" + b + r"$까지 변할 때의 함수 $y=f(x)$의 평균변화율과 $x=-2$에서의 미분계수가 서로 같다.",
            r"(나) $\displaystyle\lim_{h\to0}\frac{f(-2-h)-(1-h)f(-2)}{h}=f(" + b + r")-60$"]

ORIG = dict(
    id="55p-8", chapter=3, page=55, num=8, source="2024년 수능특강 [24009-0052]", type="주관식",
    stem=stem("x^2+5x+6"), box=box("1"), answer="15",
    general="(나): {f(−2−h)−f(−2)}/h + f(−2) → −f'(−2)+f(−2) = f(1)−60. (가): f(1)−f(−2)=3f'(−2). 연립하면 3f'(−2)=60−f'(−2) → f'(−2)=15. 구하는 극한 = f'(−2)/(−2+3) = 15.",
    special="① 분모 x²+5x+6=(x+2)(x+3) 에서 (x+3)→1 이라 f'(−2) 그대로 — 남는 인수의 값이 1 이 아니면 나눠야 함.",
    perspective="(나)를 미분계수 정의 + 상수항으로 분해.",
    table=[
        ("분모의 다른 인수 x+3 (→1)", "값이 1 이 아닌 인수", "x²+7x+10 이면 (x+5)→3 → 5"),
        ("(가)의 구간 [−2,1]", "—", "[−2,2] 와 f(2)−60 이면 f'(−2)=12 (생존)"),
    ],
    sweep=["남는 인수의 x=−2 에서의 값"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 7 (약분 후 남는 인수 x+5→3)",
        changed=["분모 x²+5x+6 → x²+7x+10"], naturalness="",
        stem=stem("x^2+7x+10"), box=box("1"), answer="5", trap_answer="15",
        trap_path="원문처럼 극한 = f'(−2) 로 두어 15 ((x+5)→3 을 빠뜨림).",
        explanation=[
            r"(나): $\dfrac{f(-2-h)-f(-2)}{h}+f(-2)\to-f'(-2)+f(-2)=f(1)-60$이다.",
            r"(가): $f(1)-f(-2)=3f'(-2)$이므로 $3f'(-2)=60-f'(-2)$, $f'(-2)=15$이다.",
            r"$\displaystyle\lim_{x\to-2}\frac{f(x)-f(-2)}{(x+2)(x+5)}=\frac{f'(-2)}{3}$이다. 함정: 남는 인수 $x+5$는 $3$이다.",
            r"따라서 값은 $5$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (구간 끝 1 → 2)",
        changed=["(가)(나)의 1 → 2"], naturalness="",
        stem=stem("x^2+5x+6"), box=box("2"), answer="12", trap_answer=None, trap_path=None,
        explanation=[
            r"(나)에서 $-f'(-2)+f(-2)=f(2)-60$이다.",
            r"(가)에서 $f(2)-f(-2)=4f'(-2)$이므로 $4f'(-2)=60-f'(-2)$, $f'(-2)=12$이다.",
            r"극한은 $\dfrac{f'(-2)}{-2+3}=12$이다.",
        ],
    ),
]


def solve_fp(b, den):
    cs = symbols('c0:4')
    f = sum(ci*x**i for i, ci in enumerate(cs))  # 삼차 이하로 충분 (조건은 f(−2), f'(−2), f(b) 만 사용)
    h = Symbol('h')
    fp = diff(f, x)
    e1 = Eq((f.subs(x, b) - f.subs(x, -2))/(b + 2), fp.subs(x, -2))
    e2 = Eq(limit((f.subs(x, -2 - h) - (1 - h)*f.subs(x, -2))/h, h, 0), f.subs(x, b) - 60)
    s = solve([e1, e2], [cs[1], cs[2]], dict=True)[0]  # c0 는 두 식에서 소거됨
    F = f.subs(s)
    val = simplify(limit((F - F.subs(x, -2))/den, x, -2))
    return val


def verify(c):
    v = solve_fp(1, x**2 + 5*x + 6)
    c.check("원문: 값이 다른 계수와 무관", not (v.free_symbols))
    c.ans('orig', v)
    v = solve_fp(1, x**2 + 7*x + 10)
    c.check("1: 계수 무관", not v.free_symbols)
    c.ans(1, v)
    c.trap(1, solve_fp(1, x**2 + 5*x + 6))
    v = solve_fp(2, x**2 + 5*x + 6)
    c.check("2: 계수 무관", not v.free_symbols)
    c.ans(2, v)
