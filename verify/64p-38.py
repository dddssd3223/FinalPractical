from lib import *

FDEF = (r"두 함수 $f(x)=\begin{cases} -4x-2 & (x\le-1) \\ ax^2+bx-1 & (-1<x<2) \\ 2x+c & (x\ge2)\end{cases}$, "
        r"$g(x)=")

def stem(gtex, tail):
    return FDEF + gtex + r"$에 대하여 함수 $f(x)$가 실수 전체의 집합에서 미분가능할 때, " + tail + r" (단, $a$, $b$, $c$는 상수이다.)"

ORIG = dict(
    id="64p-38", chapter=3, page=64, num=38, source="2024년 수능특강 [24009-0074]", type="객관식",
    stem=stem("-x^2+4ax+b-c", r"$\displaystyle\lim_{x\to1}\frac{f(x)g(x)+12}{x-1}$의 값은?"),
    choices=["-10", "-8", "-6", "-4", "-2"], answer="-4",
    general="x=−1: 연속 a−b=3, 미분 −2a+b=−4 → a=1, b=−2. x=2: 미분 4a+b=2 (자동 성립), 연속 c=−5. f(1)=−2, g=−x²+4x+3, g(1)=6 → fg(1)=−12. 극한=(fg)'(1)=f'(1)g(1)+f(1)g'(1)=0−4=−4.",
    special="① x=1 은 가운데 조각 안이라 이차식 사용 — 묻는 점이 x≥2 이면 2x+c 조각을 써야 함.",
    perspective="미분가능 조건으로 계수 결정 후 곱의 미분.",
    table=[
        ("묻는 점 x=1 (가운데 조각)", "x≥2 쪽 점 (일차 조각)", "x=3 에서 (fg)'(3) 이면 f=2x−5 사용 → 10"),
        ("g 의 −x²", "—", "x² 로 바꾸고 상수 16 이면 −12 (생존)"),
    ],
    sweep=["조각 경계 −1, 2"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 4 (식이 성립하는 구간)",
        changed=["묻는 값: x=1 에서의 극한 → lim_{h→0} {f(3+h)g(3+h)−f(3)g(3)}/h"],
        naturalness="",
        stem=stem("-x^2+4ax+b-c", r"$\displaystyle\lim_{h\to0}\frac{f(3+h)g(3+h)-f(3)g(3)}{h}$의 값은?"),
        choices=["4", "8", "10", "16", "20"], answer="10", trap_answer="20",
        trap_path="x=3 에서도 가운데 이차식 x²−2x−1 을 써서 f(3)=2, f'(3)=4 → 4·6+2·(−2)=20.",
        explanation=[
            r"$x=-1$에서 연속·미분가능 조건 $a-b-1=2$, $-2a+b=-4$에서 $a=1$, $b=-2$이고, $x=2$에서 연속이므로 $c=-5$이다.",
            r"$g(x)=-x^2+4x+3$이므로 $g(3)=6$, $g'(3)=-2$이다.",
            r"함정: $x=3$은 $x\ge2$ 구간이므로 $f(x)=2x-5$, 즉 $f(3)=1$, $f'(3)=2$이다.",
            r"구하는 값은 $f'(3)g(3)+f(3)g'(3)=12-2=10$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (g 의 −x² → x²)",
        changed=["g 의 −x² → x²", "분자 상수 12 → 16"],
        naturalness="g 를 바꾸면 f(1)g(1)=−16 이 되어 0/0 꼴이 되도록 상수를 16 으로 맞춘 것.",
        stem=stem("x^2+4ax+b-c", r"$\displaystyle\lim_{x\to1}\frac{f(x)g(x)+16}{x-1}$의 값은?"),
        choices=["-16", "-14", "-12", "-10", "-8"], answer="-12", trap_answer=None, trap_path=None,
        explanation=[
            r"원문과 같이 $a=1$, $b=-2$, $c=-5$이다.",
            r"$f(1)=-2$, $f'(1)=0$, $g(x)=x^2+4x+3$에서 $g(1)=8$, $g'(1)=6$이다.",
            r"극한은 $f'(1)g(1)+f(1)g'(1)=0-12=-12$이다.",
        ],
    ),
]


def coeffs():
    a, b, c = symbols('a b c')
    P = [(-4*x - 2, -oo, -1), (a*x**2 + b*x - 1, -1, 2), (2*x + c, 2, oo)]
    eqs = []
    for k in (-1, 2):
        eqs.append(piece_at(P, k, '-').subs(x, k) - piece_at(P, k, '+').subs(x, k))
        eqs.append(plim(P, lambda e: diff(e, x), k, '-') - plim(P, lambda e: diff(e, x), k, '+'))
    s = solve(eqs, [a, b, c], dict=True)
    assert len(s) == 1
    return [(e.subs(s[0]), lo, hi) for e, lo, hi in P], s[0], (a, b, c)


def verify(c):
    P, s, (a, b, cc) = coeffs()
    f_at = lambda t: piece_at(P, t, '+')  # t 가 경계 아닌 점
    g = (-x**2 + 4*a*x + b - cc).subs(s)
    fm = f_at(1)
    c.check("원문: 0/0 꼴", (fm*g).subs(x, 1) + 12 == 0)
    c.ans('orig', limit((fm*g + 12)/(x - 1), x, 1))
    f3 = f_at(3)
    h = Symbol('h')
    c.ans(1, limit(((f3*g).subs(x, 3 + h) - (f3*g).subs(x, 3))/h, h, 0))
    mid = P[1][0]
    c.trap(1, (diff(mid, x)*g + mid*diff(g, x)).subs(x, 3))
    g2 = (x**2 + 4*a*x + b - cc).subs(s)
    c.check("2: 0/0 꼴", (fm*g2).subs(x, 1) + 16 == 0)
    c.ans(2, limit((fm*g2 + 16)/(x - 1), x, 1))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
