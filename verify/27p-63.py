from lib import *

ORIG = dict(
    id="27p-63", chapter=1, page=27, num=63, source="2027학년도 수능 6월 모의평가 11번", type="객관식",
    stem=r"일차함수 $f(x)$에 대하여 $\displaystyle\lim_{x\to a}\frac{f(x+2)}{x\{f(x)-3\}}$의 값이 $a=0$일 때 존재하고 $a=3$일 때 존재하지 않는다. $f(4)$의 값은? [4점]",
    choices=["6", "7", "8", "9", "10"], answer="6",
    general="a=0: 분모→0. f(0)=3 이면 분모가 이중근인데 일차 분자는 이중근 불가 → f(0)≠3, f(2)=0, f=p(x−2). a=3: 분자 f(5)=3p≠0 이므로 분모 3(f(3)−3)=0 → p=3. f(4)=6.",
    special="① a=0 에서 곧바로 f(2)=0 — f(0)=3(분모 이중근) 경우를 일차라서 배제한 것. ② a=3 에서 '존재하지 않음 = 분모 0, 분자 ≠0' 한 경우만.",
    perspective="각 점에서 분자·분모의 근 차수 비교.",
    table=[
        ("a=3", "—", "a=1 로 바꾸면 f(1)=3 → p=−3 (생존)"),
        ("f 일차", "f(0)=3 인 이중근 경우, 두 번째 근", "이차(최고차 1)면 f=(x−2)(x−s), a=3 에서 f(3)=3 → s=0"),
    ],
    sweep=["f(0)=3 ⇔ 분모 이중근", "p=−3/2 이면 a=0 극한의 분모 −2p−3=0"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 1행 (a=3 → a=1)",
        changed=["존재하지 않는 점 a=3 → a=1"], naturalness="",
        stem=r"일차함수 $f(x)$에 대하여 $\displaystyle\lim_{x\to a}\frac{f(x+2)}{x\{f(x)-3\}}$의 값이 $a=0$일 때 존재하고 $a=1$일 때 존재하지 않는다. $f(4)$의 값은?",
        choices=["-8", "-6", "-4", "-2", "0"], answer="-6", trap_answer=None, trap_path=None,
        explanation=[
            r"$a=0$: $f(0)=3$이면 분모가 $x^2$ 꼴이 되어 일차식 분자로는 극한이 없으므로 $f(0)\neq3$, $f(2)=0$이다.",
            r"$f(x)=p(x-2)$로 두면 $a=1$에서 분자 $f(3)=p\neq0$이므로 분모 $f(1)-3=0$이어야 한다.",
            r"$-p-3=0$에서 $p=-3$이므로 $f(4)=-6$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 / 3-C 9 (차수가 올라가면 인수 하나가 더 필요)",
        changed=["일차함수 → 최고차항의 계수가 1인 이차함수"], naturalness="",
        stem=r"최고차항의 계수가 $1$인 이차함수 $f(x)$에 대하여 $\displaystyle\lim_{x\to a}\frac{f(x+2)}{x\{f(x)-3\}}$의 값이 $a=0$일 때 존재하고 $a=3$일 때 존재하지 않는다. $f(4)$의 값은?",
        choices=["2", "4", "6", "8", "10"], answer="8", trap_answer="6",
        trap_path="원문처럼 f=p(x−2) 일차로 두고 f(3)=3 에서 p=3 → 6.",
        explanation=[
            r"$a=0$: $f(0)=3$이면 분자 $f(x+2)$가 $x=0$에서 이중근이어야 해 $f(x)=(x-2)^2$인데 $f(0)=4\neq3$이다. 따라서 $f(0)\neq3$, $f(2)=0$이다.",
            r"함정: 이차함수이므로 $f(x)=(x-2)(x-s)$로 두어야 한다.",
            r"$a=3$: 분자 $f(5)=3(5-s)$, 분모 $3\{f(3)-3\}$. $s=5$이면 $f(3)=-2$로 분모가 $0$이 아니라 극한이 존재하므로, $f(3)=3$이어야 한다.",
            r"$3-s=3$에서 $s=0$, $f(x)=x(x-2)$이므로 $f(4)=8$이다.",
        ],
    ),
]


def classify(F, a):
    ok, _ = lim_exists(F.subs(x, x + 2)/(x*(F - 3)), a)
    return ok


def solve_f(kind, a_bad):
    if kind == 1:
        p, q = symbols('p q', real=True)
        f = p*x + q
        unknowns = [p, q]
    else:
        p, q = symbols('p q', real=True)
        f = x**2 + p*x + q
        unknowns = [p, q]
    out = []
    # a=0 에서 존재: (A) f(0)≠3 → f(2)=0,  (B) f(0)=3 → f(x+2) 가 x=0 에서 이중근
    cases = [[f.subs(x, 2)], [f.subs(x, 0) - 3, f.subs(x, 2), diff(f, x).subs(x, 2)]]
    # a_bad 에서 존재X: (C) 분모 0 → f(a)=3 (분자 확인은 뒤에서)
    for c0 in cases:
        for s in solve(c0 + [f.subs(x, a_bad) - 3], unknowns, dict=True):
            F = expand(f.subs(s))
            if F.free_symbols - {x}:
                out.append(('param', F)); continue
            if kind == 1 and Poly(F, x).degree() != 1:
                continue
            if classify(F, 0) and not classify(F, a_bad):
                out.append(('ok', F))
    # (D) 분자도 0 인데 차수 부족으로 존재X 인 경우도 전수 점검
    for c0 in cases:
        for s in solve(c0 + [f.subs(x, a_bad + 2)], unknowns, dict=True):
            F = expand(f.subs(s))
            if not (F.free_symbols - {x}) and (kind == 2 or Poly(F, x).degree() == 1):
                if classify(F, 0) and not classify(F, a_bad):
                    out.append(('ok', F))
    return out


def verify(c):
    for key, kind, ab in (('orig', 1, 3), (1, 1, 1), (2, 2, 3)):
        r = solve_f(kind, ab)
        c.check(f"{key}: 해 하나", [k for k, F in r] == ['ok'])
        c.ans(key, r[0][1].subs(x, 4))
    c.trap(2, (3*(x - 2)).subs(x, 4))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
