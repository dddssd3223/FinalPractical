from lib import *

def box(ga):
    return [ga, r"(나) $f'(3)=0$"]

HEAD = r"함수 $f(x)=x^3+ax^2+bx$가 다음 조건을 만족시킬 때, $f(1)$의 값은? (단, $a$, $b$는 상수이다.)"

ORIG = dict(
    id="80p-3", chapter=4, page=80, num=3, source="2025년 수능특강 [25009-0081]", type="객관식",
    stem=HEAD, box=box(r"(가) 닫힌구간 $[0,\,2]$에서 평균값 정리를 만족시키는 상수 $c$의 값은 $\frac23$이다."),
    choices=["-8", "-7", "-6", "-5", "-4"], answer="-6",
    general="평균변화율 4+2a+b = f'(c)=3c²+2ac+b → 3c²+2ac−4−2a=0 에 c=2/3 → a=−4 (다른 근 c=2 는 끝점이라 제외). f'(3)=27−24+b=0 → b=−3 → f(1)=−6.",
    special="① c 는 열린구간 (0,2) 안에서만 — 이차방정식의 다른 근이 끝점·밖이면 버림.",
    perspective="평균값 정리 → c 에 대한 이차방정식.",
    table=[
        ("c 값 하나 주어짐", "c 값들의 합 (근과 계수 사용 유혹)", "[0,3] 에서 c 값의 합 1 이면 두 근 중 하나가 끝점 3 → a=−6 → 4"),
        ("c=2/3", "—", "4/3 이면 a=−2 → f(1)=−16 (생존)"),
    ],
    sweep=["3c²+2ac−(t²+at)=0 의 (0,t) 안 근"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (근과 계수의 관계는 두 근이 모두 (0,t) 안일 때만)",
        changed=["(가) [0,2], c=2/3 → [0,3], 모든 c 의 값의 합이 1"], naturalness="",
        stem=HEAD, box=box(r"(가) 닫힌구간 $[0,\,3]$에서 평균값 정리를 만족시키는 모든 상수 $c$의 값의 합은 $1$이다."),
        choices=["-37/2", "-4", "0", "4", "8"], answer="4", trap_answer="-37/2",
        trap_path="3c²+2ac−9−3a=0 의 두 근의 합 −2a/3=1 → a=−3/2 → b=−18 → f(1)=−37/2 (이때 한 근은 음수라 c 가 아님).",
        explanation=[
            r"평균변화율은 $\frac{f(3)-f(0)}3=9+3a+b$이므로 $3c^2+2ac-9-3a=0$을 만족시키는 $0<c<3$이 $c$이다.",
            r"함정: 두 근의 합 $-\frac{2a}3=1$로 두면 $a=-\frac32$인데, 이때 두 근의 곱이 음수라 한 근은 구간 밖이고 남은 근의 합이 $1$이 아니다.",
            r"근이 하나만 구간 안이고 그 값이 $1$이면 $3+2a-9-3a=0$, $a=-6$이고 다른 근은 $3$(끝점)이라 조건을 만족한다.",
            r"(나)에서 $27-36+b=0$, $b=9$이므로 $f(1)=1-6+9=4$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (c=2/3 → 4/3)",
        changed=["(가) c=2/3 → 4/3"], naturalness="",
        stem=HEAD, box=box(r"(가) 닫힌구간 $[0,\,2]$에서 평균값 정리를 만족시키는 상수 $c$의 값은 $\frac43$이다."),
        choices=["-18", "-17", "-16", "-15", "-14"], answer="-16", trap_answer=None, trap_path=None,
        explanation=[
            r"$3c^2+2ac-4-2a=0$에 $c=\frac43$을 넣으면 $\frac{16}3+\frac{8a}3-4-2a=0$, $a=-2$이다 (다른 근 $0$은 끝점).",
            r"(나)에서 $27-12+b=0$, $b=-15$이다.",
            r"$f(1)=1-2-15=-16$이다.",
        ],
    ),
]


def mvt_cs(a, t):
    c = Symbol('c', real=True)
    b = Symbol('b')
    f = x**3 + a*x**2 + b*x
    eq = expand(diff(f, x).subs(x, c) - (f.subs(x, t) - f.subs(x, 0))/t)
    assert b not in eq.free_symbols
    return [r for r in solve(eq, c) if r.is_real and 0 < r < t]


def f1(a):
    b = solve(27 + 6*a + Symbol('b'), Symbol('b'))[0]
    return (x**3 + a*x**2 + b*x).subs(x, 1)


def verify(c):
    a = Symbol('a', real=True)
    # 원문: c=2/3 이 유일한 c
    s = [av for av in solve(expand((3*x**2 + 2*a*x - 4 - 2*a).subs(x, Rational(2, 3))), a) if mvt_cs(av, 2) == [Rational(2, 3)]]
    c.check("원문: a 유일", len(s) == 1)
    c.ans('orig', f1(s[0]))
    # 1: 모든 c 의 합이 1 — 경우: 한 근만 (0,3) 안 (그 근 =1) / 두 근 모두 안 (합 −2a/3=1)
    cand = set(solve(expand((3*x**2 + 2*a*x - 9 - 3*a).subs(x, 1)), a)) | set(solve(-2*a/3 - 1, a))
    good = [av for av in cand if simplify(sum(mvt_cs(av, 3)) - 1) == 0 and mvt_cs(av, 3)]
    c.check("1: a 유일 (=−6)", good == [-6])
    c.ans(1, f1(good[0]))
    c.trap(1, f1(Rational(-3, 2)))
    s = [av for av in solve(expand((3*x**2 + 2*a*x - 4 - 2*a).subs(x, Rational(4, 3))), a) if mvt_cs(av, 2) == [Rational(4, 3)]]
    c.check("2: a 유일", len(s) == 1)
    c.ans(2, f1(s[0]))
