from lib import *

BOX = lambda sgn, m: [r"(가) $\{x\,|\,f(x)=3\}=\{-a,\ a,\ 2a\}$", r"(나) $f(0)" + sgn + r"0$, $f'(1)=" + m + r"$"]

ORIG = dict(
    id="64p-37", chapter=3, page=64, num=37, source="2024년 수능특강 [24009-0069]", type="객관식",
    stem=r"최고차항의 계수가 $1$인 삼차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(3)$의 값은? (단, $a$는 $0$이 아닌 실수이다.)",
    box=BOX(">", "-2"), choices=["7", "8", "9", "10", "11"], answer="11",
    general="f−3=(x+a)(x−a)(x−2a) → f'(1)=3−4a−a²=−2 → a=1 또는 −5. f(0)=3+2a³>0 → a=1. f(3)=11.",
    special="① f(0)>0 이 a 두 값 중 하나를 버리는 조건 — 부호가 바뀌면 다른 쪽이 답.",
    perspective="(가)로 f 를 a 하나로, (나)로 a 선택.",
    table=[
        ("f(0)>0 (a=1 선택)", "f(0)<0 (다른 근 선택)", "f'(1)=6, f(0)<0 이면 a=−3 → f(3)=3"),
        ("f'(1)=−2", "—", "6 이면 a=−1, −3 중 f(0)>0 인 a=−1 → 43 (생존)"),
    ],
    sweep=["a²+4a+(m−3)=0 두 근 합 −4, f(0)=3+2a³ 부호 경계 a=−(3/2)^(1/3)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (f(0) 부호가 바뀌면 반대쪽 근 선택)",
        changed=["f(0)>0 → f(0)<0", "f'(1)=−2 → 6", "주관식"],
        naturalness="f'(1)=−2 그대로 부호만 바꾸면 a=−5 로 f(3)=−205 가 되어 답이 커서, a 후보가 −1, −3 이 되도록 f'(1)=6 으로 함께 바꾼 것.",
        stem=r"최고차항의 계수가 $1$인 삼차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(3)$의 값을 구하시오. (단, $a$는 $0$이 아닌 실수이다.)",
        box=BOX("<", "6"), answer="3", trap_answer="43",
        trap_path="원문처럼 절댓값이 작은 근 a=−1 을 골라 f(3)=43 (a=−1 이면 f(0)=1>0 이라 조건 위반).",
        explanation=[
            r"(가)에서 $f(x)-3=(x+a)(x-a)(x-2a)=x^3-2ax^2-a^2x+2a^3$이다.",
            r"$f'(1)=3-4a-a^2=6$에서 $a=-1$ 또는 $a=-3$이다.",
            r"함정: $f(0)=3+2a^3$이므로 $a=-1$이면 $f(0)=1>0$이다. $f(0)<0$이려면 $a=-3$이다.",
            r"$f(3)=3+(3-3)(3+3)(3+6)=3$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (f'(1)=−2 → 6)",
        changed=["f'(1)=−2 → 6", "주관식"], naturalness="43 이 원문 선지 범위(7~11)를 벗어나 주관식으로 바꾼 것.",
        stem=r"최고차항의 계수가 $1$인 삼차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(3)$의 값을 구하시오. (단, $a$는 $0$이 아닌 실수이다.)",
        box=BOX(">", "6"), answer="43", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)-3=(x+a)(x-a)(x-2a)$이고 $f'(1)=3-4a-a^2=6$에서 $a=-1$ 또는 $-3$이다.",
            r"$f(0)=3+2a^3>0$이므로 $a=-1$이다.",
            r"$f(3)=3+(3-1)(3+1)(3+2)=43$이다.",
        ],
    ),
]


def f3_values(sgn, m):
    a, p, q, r = symbols('a p q r')
    f = x**3 + p*x**2 + q*x + r
    out = set()
    for s in solve([f.subs(x, -a) - 3, f.subs(x, a) - 3, f.subs(x, 2*a) - 3, diff(f, x).subs(x, 1) - m], [a, p, q, r], dict=True):
        if s[a] == 0 or not s[a].is_real:
            continue
        F = f.subs(s)
        roots = set(Poly(F - 3, x).real_roots())
        if roots != {-s[a], s[a], 2*s[a]}:
            continue
        f0 = F.subs(x, 0)
        if (f0 > 0) if sgn == '>' else (f0 < 0):
            out.add(F.subs(x, 3))
    return out


def verify(c):
    v = f3_values('>', -2)
    c.check("원문: 유일", len(v) == 1)
    c.ans('orig', v.pop())
    v = f3_values('<', 6)
    c.check("1: 유일", len(v) == 1)
    c.ans(1, v.pop())
    c.trap(1, f3_values('>', 6).pop())
    v = f3_values('>', 6)
    c.check("2: 유일", len(v) == 1)
    c.ans(2, v.pop())


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='3', trap_path="f'(1)=6 의 두 근 중 a=−3 을 택해 f(3)=3 (a=−3 이면 f(0)=−51<0 이라 조건 위반).")
VARS[1]['explanation'].insert(-1, '함정: $a=-3$이면 $f(0)=3-54<0$이라 조건에 맞지 않는다.')
_verify0 = verify


def verify(c):
    _verify0(c)
    a0 = Symbol('a0')
    c.trap(2, (3 + (x + a0)*(x - a0)*(x - 2*a0)).subs({x: 3, a0: -3}))
