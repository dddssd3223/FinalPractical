from lib import *

def stem(cond, tail):
    return (r"최고차항의 계수가 $1$인 삼차함수 $f(x)$가 다음 조건을 만족시킨다. $f(0)=1$, " + cond + r"일 때, $f(3)$의 값은?" + tail)

BOX = [r"방정식 $f(x)=9$는 서로 다른 세 실근을 갖고, 이 세 실근은 크기 순서대로 등비수열을 이룬다."]

ORIG = dict(
    id="72p-58", chapter=3, page=72, num=58, source="2022학년도 수능 예시문항 11번", type="객관식",
    stem=stem(r"$f'(2)=-2$", ""), box=BOX, choices=["6", "7", "8", "9", "10"], answer="7",
    general="세 근 β/r, β, βr → f(0)−9=−β³=−8 → β=2. f−9=(x−2)(x²−sx+4), f'(2)=8−2s=−2 → s=5 → 근 1,2,4. f(3)=9+(1)(−2)=7.",
    special="① '크기 순서대로' — 다른 두 근이 음수(공비 음수)면 크기 순으로는 등비가 아님. s>0 일 때만 성립.",
    perspective="등비수열 세 수의 곱 = 가운데 항³.",
    table=[
        ("s=5>0 (다른 두 근 양수)", "s<0 (공비 음수, 크기 순 깨짐)", "|f'(2)|=18 이면 s=13 또는 −5, −5 는 제외 → −17"),
        ("f'(2)=−2", "—", "−4 면 s=6 → f(3)=4 (생존)"),
    ],
    sweep=["s=(8−f'(2))/2, s>4 이어야 서로 다른 세 실근이자 크기순 등비"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (공비 음수면 크기 순 등비가 아님)",
        changed=["f'(2)=−2 → |f'(2)|=18"], naturalness="",
        stem=stem(r"$|f'(2)|=18$", ""), box=BOX, choices=["-17", "-7", "7", "17", "37"], answer="-17", trap_answer="37",
        trap_path="f'(2)=18 쪽 s=−5 (근 −4, −1, 2) 을 택해 f(3)=37 (−4<−1<2 는 크기 순으로 등비가 아님).",
        explanation=[
            r"세 근을 $\frac\beta r$, $\beta$, $\beta r$라 하면 $f(0)-9=-\beta^3=-8$에서 $\beta=2$이고 $f(x)-9=(x-2)(x^2-sx+4)$이다.",
            r"$f'(2)=8-2s=\pm18$에서 $s=-5$ 또는 $s=13$이다.",
            r"함정: $s=-5$이면 근이 $-4$, $-1$, $2$로 크기 순 $-4,-1,2$는 등비수열이 아니다 (공비가 음수인 $-1,2,-4$만 등비).",
            r"$s=13$이면 두 근은 양수이고 $\frac\beta r<2<\beta r$로 크기 순 등비이다.",
            r"$f(3)=9+(3-2)(9-39+4)=-17$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (f'(2)=−2 → −4)",
        changed=["f'(2)=−2 → −4"], naturalness="",
        stem=stem(r"$f'(2)=-4$", ""), box=BOX, choices=["2", "3", "4", "5", "6"], answer="4", trap_answer=None, trap_path=None,
        explanation=[
            r"$\beta=2$이고 $f(x)-9=(x-2)(x^2-sx+4)$이다.",
            r"$f'(2)=8-2s=-4$에서 $s=6$, 두 근 $3\pm\sqrt5$는 양수라 크기 순 등비이다.",
            r"$f(3)=9+(9-18+4)=4$이다.",
        ],
    ),
]


def f3_values(fp2_list):
    r = Symbol('r', real=True)
    out = set()
    beta = real_root(9 - 1, 3)  # β³ = 9 − f(0)
    f = 9 + (x - beta/r)*(x - beta)*(x - beta*r)
    for m in fp2_list:
        for rv in solve(diff(f, x).subs(x, 2) - m, r):
            if not rv.is_real or rv in (0, 1, -1):
                continue
            F = expand(f.subs(r, rv))
            roots = sorted([simplify(beta/rv), beta, simplify(beta*rv)], key=lambda z: float(z))
            assert all(simplify(F.subs(x, z) - 9) == 0 for z in roots)
            if len(set(roots)) != 3:
                continue
            a, b, cc = roots
            if simplify(b**2 - a*cc) == 0 and simplify(b/a - cc/b) == 0:  # 크기 순 등비
                out.add(simplify(F.subs(x, 3)))
    return out


def verify(c):
    v = f3_values([-2])
    c.check("원문: 유일", len(v) == 1)
    c.ans('orig', v.pop())
    v = f3_values([18, -18])
    c.check("1: 유일", len(v) == 1)
    c.ans(1, v.pop())
    s = Symbol('s')
    F = 9 + (x - 2)*(x**2 + 5*x + 4)  # s=−5
    c.check("함정 f: f'(2)=18, 근 −4,−1,2", diff(F, x).subs(x, 2) == 18 and set(Poly(F - 9, x).real_roots()) == {-4, -1, 2})
    c.trap(1, F.subs(x, 3))
    v = f3_values([-4])
    c.check("2: 유일", len(v) == 1)
    c.ans(2, v.pop())
