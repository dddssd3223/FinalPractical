from lib import *

BOX = [r"(가) 함수 $g(x)=\dfrac{x}{f(x^2+4)}$는 $x=a$에서만 불연속이다.",
       r"(나) 함수 $h(x)=\dfrac{f(x-4)}{f(x^2)}$는 $x=b$, $x=c\,(b<c)$에서만 불연속이다."]
STEM = r"최고차항의 계수가 $1$인 이차함수 $f(x)$와 세 실수 $a$, $b$, $c$가 다음 조건을 만족시킨다. "

ORIG = dict(
    id="40p-30", chapter=2, page=40, num=30, source="2024년 수능완성 [24054-0106]", type="객관식",
    stem=STEM + r"$\displaystyle\lim_{x\to b}h(x)$의 값이 존재할 때, $f(c)\times\lim_{x\to b}h(x)$의 값은?", box=BOX,
    choices=["-5", "-4", "-3", "-2", "-1"], answer="-4",
    general="(가): x²+4=r 의 해가 하나 → 근 4 (x=0), 다른 근 r₂<4 또는 r₂=4. (나): f(x²)=0 이 두 점 → ±2, r₂<0 (0 이면 x=0 추가) 또는 r₂=4. lim_{x→−2} 존재 → f(−6)=0 → r₂=−6. f=(x−4)(x+6), lim=(x−8)/((x−2)(x²+6)) → 1/4, f(2)=−16 → −4.",
    special="① 극한 존재 조건으로 r₂ 를 바로 정함 — 이 조건이 없으면 r₂<0 또는 중근 4 의 두 갈래가 남음. ② r₂=0 이면 x=0 이 불연속점으로 추가되는 것.",
    perspective="각 조건을 'f 의 근이 어디에 있어야 하는가'로 번역.",
    table=[
        ("lim_{x→b} h 존재", "r₂=4 (중근) 갈래", "이 조건을 f(0)>0 으로 바꾸면 r₂<0 불가 → f=(x−4)²"),
        ("극한점 b", "—", "lim_{x→c} 존재로 바꾸면 f(−2)=0 → r₂=−2 (생존)"),
    ],
    sweep=["r₂<0 / r₂=0 (불연속점 3개) / 0<r₂<4 (4개) / r₂=4 (중근)"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (극한 존재 점 b → c)",
        changed=["lim_{x→b} h 존재 → lim_{x→c} h 존재 (묻는 값도 c 로)"], naturalness="극한점을 b 에서 c 로 옮긴 한 가지 변경.",
        stem=STEM + r"$\displaystyle\lim_{x\to c}h(x)$의 값이 존재할 때, $f(c)\times\lim_{x\to c}h(x)$의 값은?", box=BOX,
        choices=["-2", "-1", "1", "2", "4"], answer="2", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)에서 $f(4)=0$이고, (나)에서 $f(x^2)=0$의 해는 $\pm2$뿐이므로 $b=-2$, $c=2$이고 다른 근 $r_2<0$ (또는 중근 $4$)이다.",
            r"$\displaystyle\lim_{x\to2}h(x)$가 존재하려면 $f(-2)=0$이므로 $r_2=-2$, $f(x)=(x-4)(x+2)$이다.",
            r"$\displaystyle\lim_{x\to2}\frac{(x-8)(x-2)}{(x-2)(x+2)(x^2+2)}=\frac{-6}{24}=-\frac14$, $f(2)=-8$이다.",
            r"곱은 $2$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (중근 갈래가 답이 되는 경우)",
        changed=["'lim_{x→b} h 존재' → 'f(0)>0'", "묻는 값 → f(−1)"],
        naturalness="극한 조건을 부호 조건으로 바꾸면 f(c)×lim 을 물을 수 없어(lim 없음) 묻는 값을 바꾼 것은 필수.",
        stem=STEM + r"$f(0)>0$일 때, $f(-1)$의 값은?", box=BOX,
        choices=["-25", "-9", "9", "16", "25"], answer="25", trap_answer="-25",
        trap_path="원문의 f=(x−4)(x+6) 을 그대로 써서 f(−1)=−25 (이 f 는 f(0)<0).",
        explanation=[
            r"(가)에서 $f(4)=0$이고 다른 근 $r_2$는 $r_2<4$ 또는 $r_2=4$이다.",
            r"(나)에서 $f(x^2)=0$의 해가 두 개이려면 $r_2<0$ 또는 $r_2=4$이다 ($r_2=0$이면 $x=0$도 불연속점).",
            r"$f(0)=4r_2>0$이므로 $r_2<0$은 불가능하다. 함정: 원문처럼 음수 근만 보면 안 되고, 중근 $r_2=4$ 갈래가 답이다.",
            r"$f(x)=(x-4)^2$이므로 $f(-1)=25$이다.",
        ],
    ),
]


def discont_points(expr, cand):
    """expr 가 정의되지 않는 실수(분모의 실근)"""
    num, den = fraction(together(expr))
    return set(real_roots(Poly(den, x))) if Poly(den, x).degree() > 0 else set()


def admissible(r2):
    f = expand((x - 4)*(x - r2))
    g = x/f.subs(x, x**2 + 4)
    h = f.subs(x, x - 4)/f.subs(x, x**2)
    dg = set(real_roots(Poly(f.subs(x, x**2 + 4), x)))
    dh = sorted(set(real_roots(Poly(f.subs(x, x**2), x))))
    return f, h, len(dg) == 1, len(dh) == 2, dh


def verify(c):
    r = Symbol('r', real=True)
    # 원문: b=−2 에서 극한 존재 → f(−6)=0
    cands = [v for v in solve((-6 - 4)*(-6 - r), r)]
    ok = [v for v in cands if admissible(v)[2] and admissible(v)[3]]
    c.check("원문: r₂ 하나", len(ok) == 1)
    f, h, _, _, dh = admissible(ok[0])
    b, cc = dh
    c.ans('orig', f.subs(x, cc)*limit(h, x, b))
    # 변형1: c=2 에서 극한 존재 → f(−2)=0
    cands = [v for v in solve((-2 - 4)*(-2 - r), r)]
    ok = [v for v in cands if admissible(v)[2] and admissible(v)[3]]
    c.check("1: r₂ 하나", len(ok) == 1)
    f, h, _, _, dh = admissible(ok[0])
    b, cc = dh
    c.ans(1, f.subs(x, cc)*limit(h, x, cc))
    # 변형2: r₂ 후보를 넓게 훑어 (가)(나) 와 f(0)>0 을 만족하는 것
    grid = [Rational(k, 2) for k in range(-40, 41)]
    ok = [v for v in grid if admissible(v)[2] and admissible(v)[3] and ((x - 4)*(x - v)).subs(x, 0) > 0]
    c.check("2: r₂=4 하나", ok == [4])
    c.ans(2, ((x - 4)*(x - ok[0])).subs(x, -1))
    c.trap(2, ((x - 4)*(x + 6)).subs(x, -1))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
