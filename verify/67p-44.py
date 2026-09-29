from lib import *
from itertools import permutations

def box(m):
    return [r"(가) $\displaystyle\lim_{x\to\infty}\frac{f(x)}{x^3}=2$", r"(나) $\displaystyle\lim_{x\to0}\frac{f(x)-2}{x}=" + m + r"$"]

def stem(order, ask):
    return (r"다항함수 $f(x)$가 다음 조건을 만족시킨다. 함수 $y=f(x)$의 그래프와 직선 $y=2$는 서로 다른 세 점 $\mathrm A$, $\mathrm B$, $\mathrm C$에서 만나고 점 $\mathrm B$는 선분 $\mathrm{AC}$를 $1:2$로 내분하는 점일 때, "
            + ask + r" (단, " + order + r")")

ORD_O = r"원점 $\mathrm O$에 대하여 $\overline{\mathrm{OA}}<\overline{\mathrm{OB}}<\overline{\mathrm{OC}}$이다."
ORD_X = r"세 점 $\mathrm A$, $\mathrm B$, $\mathrm C$의 $x$좌표는 모두 정수이고 이 순서대로 커진다."

ORIG = dict(
    id="67p-44", chapter=3, page=67, num=44, source="2024년 수능특강 [24009-0075]", type="주관식",
    stem=stem(ORD_O, r"$f(1)$의 최댓값을 구하시오."), box=box("24"), answer="44",
    general="f=2x³+px²+24x+2. f=2 ⇔ x(2x²+px+24)=0 → 근 0, α, β (αβ=12). OA<OB<OC ⇔ |x| 순 → A=0. B=C/3 → 3α²=12 → (α,β)=±(2,6) → p=∓16 → f(1)=28+p 최대 44.",
    special="① 원점 거리 순서라 A=(0,2) 이 확정, B·C 의 부호는 자유 → 두 경우 중 최댓값. ② x좌표 순서 조건이면 부호가 고정.",
    perspective="근과 계수 + 내분 비.",
    table=[
        ("원점 거리 순서 (부호 자유)", "x좌표 순서 (A<B<C)", "x좌표 순서면 A=0, B=2, C=6 한 경우 → f(1)=12"),
        ("(나) 24", "—", "54 면 (3,9) → 최댓값 82 (생존)"),
    ],
    sweep=["배치 6가지 중 A=0 만 성립 (B=0: AC<0 모순, C=0: 무리수)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (순서 조건이 부호를 고정)",
        changed=["단서 OA<OB<OC → x좌표가 정수이고 A, B, C 순으로 증가", "묻는 값 f(1) 최댓값 → f(1)"],
        naturalness="x좌표 순서만 두면 0 이 C 인 무리수 배치(−3√2, −2√2, 0)도 생겨 정수 조건을 함께 넣었고, 그러면 f 가 하나로 정해지므로 f(1) 을 묻는다.",
        stem=stem(ORD_X, r"$f(1)$의 값을 구하시오."), box=box("24"), answer="12", trap_answer="44",
        trap_path="원문처럼 B, C 가 음수인 경우 (0, −2, −6) 도 넣어 최댓값 44 (x좌표가 감소하므로 조건 위반).",
        explanation=[
            r"(가)(나)에서 $f(x)=2x^3+px^2+24x+2$이고, $f(x)=2$의 해는 $0$과 $2x^2+px+24=0$의 두 근 $\alpha$, $\beta$ ($\alpha\beta=12$)이다.",
            r"$\alpha\beta>0$이므로 두 근은 부호가 같고 $0$이 가운데(B)일 수 없다. $0$이 C이면 $B=\frac23A$에서 $A^2=18$이 되어 정수가 아니다.",
            r"함정: A$=0$이면 $B=\frac C3$이고 x좌표가 증가하므로 $B=2$, $C=6$만 가능하다 ($-2$, $-6$은 감소).",
            r"$\alpha+\beta=8=-\frac p2$에서 $p=-16$이므로 $f(1)=2-16+24+2=12$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 ((나) 24 → 54)",
        changed=["(나) 24 → 54"], naturalness="",
        stem=stem(ORD_O, r"$f(1)$의 최댓값을 구하시오."), box=box("54"), answer="82", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)=2x^3+px^2+54x+2$이고 $f(x)=2$의 근은 $0$, $\alpha$, $\beta$ ($\alpha\beta=27$)이다.",
            r"원점 거리 순서로 A$=0$, $B=\frac C3$이므로 $3\alpha^2=27$, $(\alpha,\beta)=\pm(3,9)$이다.",
            r"$p=\mp24$이고 $f(1)=58+p$의 최댓값은 $82$이다.",
        ],
    ),
]


def f1_values(m, order):
    p, q, r, a, b = symbols('p q r a b')
    f = 2*x**3 + p*x**2 + q*x + r
    s0 = solve([f.subs(x, 0) - 2, diff(f, x).subs(x, 0) - m], [r, q], dict=True)[0]
    f = f.subs(s0)
    vals = set()
    for A, B, C in permutations([0, a, b]):
        for s in solve([3*B - 2*A - C, a*b - Rational(m, 2)], [a, b], dict=True):
            av, bv = s[a], s[b]
            if not (av.is_real and bv.is_real) or av == bv or av == 0 or bv == 0:
                continue
            X = [Integer(0) if t == 0 else t.subs(s) for t in (A, B, C)]
            if order == 'X' and not all(t.is_integer for t in X):
                continue
            if order == 'O':
                ok = abs(X[0]) < abs(X[1]) < abs(X[2])
            else:
                ok = X[0] < X[1] < X[2]
            if not ok:
                continue
            pv = solve(av + bv + p/2, p)[0]
            F = f.subs(p, pv)
            assert all(simplify(F.subs(x, t) - 2) == 0 for t in X)
            assert limit(F/x**3, x, oo) == 2 and limit((F - 2)/x, x, 0) == m
            vals.add(F.subs(x, 1))
    return vals


def verify(c):
    v = f1_values(24, 'O')
    c.ans('orig', max(v))
    v = f1_values(24, 'X')
    c.check("1: 유일", len(v) == 1)
    c.ans(1, v.pop())
    c.trap(1, max(f1_values(24, 'O')))
    c.ans(2, max(f1_values(54, 'O')))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='34', trap_path='B, C 를 양수 쪽 (3, 9) 으로만 잡아 p=−24 → f(1)=34 (음수 쪽 (−3,−9) 이 더 큰 82).')
VARS[1]['explanation'].insert(-1, '함정: 부호가 음수인 경우 $p=24$가 최댓값을 준다.')
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, min(f1_values(54, 'O')))
