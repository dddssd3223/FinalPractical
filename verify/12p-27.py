from lib import *

ORIG = dict(
    id="12p-27", chapter=1, page=12, num=27, source="2024년 수능완성 [24054-0092]", type="객관식",
    stem=r"두 다항함수 $f(x)$, $g(x)$가 모든 실수 $x$에 대하여 $-2x^2+5\le f(x)+g(x)\le -4x+7$을 만족시키고, $\displaystyle\lim_{x\to1}\frac{2f(x)+g(x)}{f(x)+2g(x)}=8$일 때, $\displaystyle\lim_{x\to1}\{f(x)-g(x)\}$의 값은?",
    choices=["6", "7", "8", "9", "10"], answer="7",
    general="두 경계의 차 2(x−1)² → x=1 에서 접함 → f(1)+g(1)=3. 분모 f(1)+2g(1)≠0 이면 (2f₁+g₁)=8(f₁+2g₁) → f₁=−5g₁/2 → g₁=−2, f₁=5 → f₁−g₁=7. (분모가 0이면 분자도 0 → f₁=g₁=0 → 합 3 과 모순)",
    special="① 극한을 값의 비로 바로 대입(분모≠0 확인 생략) — f(1)+g(1)≠0 이라 통함. ② 끼인 값이 0 이 되면 0/0 이 되어 미분계수 비로 가야 함.",
    perspective="끼움 정리는 값(p(1))과 기울기(p'(1), 두 경계가 접하므로)를 함께 준다.",
    table=[
        ("경계가 x=1 에서 값 3 으로 접함", "f(1)+g(1)=0 인 경우", "값이 0 이면 f(1)=g(1)=0 → 0/0 → 기울기 비로 결정"),
        ("극한값 8", "분모가 0 인 경우", "다른 값이면 f₁, g₁ 만 바뀜 (생존)"),
        ("묻는 값이 값의 차", "기울기를 묻는 경우", "(f−g)/(x−1) 을 물으면 끼움 정리의 기울기가 필요"),
    ],
    sweep=["끼인 값 s=f₁+g₁=0 ⇔ f₁=g₁=0 (k≠−1)", "k=−1 이면 해 없음"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 2 (분자·분모 모두 0 → 미분계수 비)",
        changed=["경계 −2x²+5, −4x+7 → −2x²+2, −4x+4 (접하는 값 3 → 0)", "극한값 8 → 5", "묻는 값: lim (f−g)/(x−1)"],
        naturalness="경계를 3만큼 내려 끼인 값을 0 으로 만든 것이 핵심 변경. 값이 0 이 되면 f(1)−g(1) 은 0 이라 묻는 값을 기울기로 옮기는 것이 필수, 극한값 5 는 정수 답을 위한 조정.",
        stem=r"두 다항함수 $f(x)$, $g(x)$가 모든 실수 $x$에 대하여 $-2x^2+2\le f(x)+g(x)\le -4x+4$를 만족시키고, $\displaystyle\lim_{x\to1}\frac{2f(x)+g(x)}{f(x)+2g(x)}=5$일 때, $\displaystyle\lim_{x\to1}\frac{f(x)-g(x)}{x-1}$의 값은?",
        choices=["-8", "-4", "0", "4", "8"], answer="-8", trap_answer="8",
        trap_path="끼움 정리를 (x−1)로 나눌 때 x<1 쪽 부등호 방향을 무시해 f'(1)+g'(1)=4 로 잡음 → 8.",
        explanation=[
            r"두 경계의 차가 $2(x-1)^2$이므로 $x=1$에서 $f(1)+g(1)=0$이고, 두 경계가 접하므로 $f'(1)+g'(1)=-4$이다.",
            r"$f(1)=-g(1)$이면 $\frac{2f(1)+g(1)}{f(1)+2g(1)}=-1\neq5$이므로 $f(1)=g(1)=0$, 즉 $0/0$ 꼴이다.",
            r"$\displaystyle\lim_{x\to1}\frac{2f+g}{f+2g}=\frac{2f'(1)+g'(1)}{f'(1)+2g'(1)}=5$에서 $f'(1)=-3g'(1)$이다.",
            r"$f'(1)+g'(1)=-4$와 연립하면 $g'(1)=2$, $f'(1)=-6$이다. 함정: 기울기 $-4$의 부호.",
            r"따라서 $\displaystyle\lim_{x\to1}\frac{f(x)-g(x)}{x-1}=f'(1)-g'(1)=-8$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (극한값 8 → −4)",
        changed=["극한값 8 → −4"], naturalness="",
        stem=r"두 다항함수 $f(x)$, $g(x)$가 모든 실수 $x$에 대하여 $-2x^2+5\le f(x)+g(x)\le -4x+7$을 만족시키고, $\displaystyle\lim_{x\to1}\frac{2f(x)+g(x)}{f(x)+2g(x)}=-4$일 때, $\displaystyle\lim_{x\to1}\{f(x)-g(x)\}$의 값은?",
        choices=["9", "12", "15", "18", "21"], answer="15", trap_answer=None, trap_path=None,
        explanation=[
            r"두 경계의 차가 $2(x-1)^2$이므로 $f(1)+g(1)=3$이다.",
            r"$f(1)+2g(1)=0$이면 분자도 $0$이어야 해 $f(1)=g(1)=0$이 되어 모순이므로 분모는 $0$이 아니다.",
            r"$2f(1)+g(1)=-4\{f(1)+2g(1)\}$에서 $6f(1)=-9g(1)$, $f(1)=-\tfrac32g(1)$이다.",
            r"$f(1)+g(1)=3$과 연립하면 $g(1)=-6$, $f(1)=9$이므로 $f(1)-g(1)=15$이다.",
        ],
    ),
]


def local(s, k, ask):
    """f=f1+u(x−1)+..., g=g1+v(x−1)+... 로 두고 조건을 풀어 (답 후보 집합) 반환"""
    f1, g1, u, v = symbols('f1 g1 u v', real=True)
    t = x - 1
    F, G = f1 + u*t + 7*t**2, g1 + v*t - 3*t**2  # 2차항은 임의(결과 무관 확인용)
    out = set()
    for sv in solve([f1 + g1 - s], [f1], dict=True):
        Fs, Gs = F.subs(sv), G.subs(sv)
        for gv in [g1]:
            pass
        # 경우 1: 분모≠0
        L = simplify(limit((2*Fs + Gs)/(Fs + 2*Gs), x, 1))
        for sol in solve(Eq(L, k), [g1], dict=True):
            if simplify((Fs + 2*Gs).subs(x, 1).subs(sol)) != 0:
                out.add(simplify(ask(Fs.subs(sol), Gs.subs(sol), u, v)))
        # 경우 2: f1=g1=0
        if s == 0:
            F0, G0 = Fs.subs(g1, 0), Gs.subs(g1, 0)
            L0 = simplify(limit((2*F0 + G0)/(F0 + 2*G0), x, 1))
            for sol in solve([Eq(L0, k), Eq(u + v, -4)], [u, v], dict=True):
                out.add(simplify(ask(F0.subs(sol), G0.subs(sol), u, v)))
    return out


def verify(c):
    lo, hi = -2*x**2 + 5, -4*x + 7
    c.check("원문 경계가 x=1 에서 접함", factor(hi - lo) == 2*(x - 1)**2)
    r = local(3, 8, lambda F, G, u, v: limit(F - G, x, 1))
    c.check("원문 답 유일", len(r) == 1)
    c.ans('orig', list(r)[0])

    lo, hi = -2*x**2 + 2, -4*x + 4
    c.check("1: 경계가 x=1 에서 값 0 으로 접함", factor(hi - lo) == 2*(x - 1)**2 and hi.subs(x, 1) == 0)
    r = local(0, 5, lambda F, G, u, v: limit((F - G)/(x - 1), x, 1))
    c.check("1: 답 유일", len(r) == 1)
    c.ans(1, list(r)[0])
    fex, gex = -6*(x - 1), 2*(x - 1)
    c.check("1: 예시 f=−6(x−1), g=2(x−1) 가 조건 만족",
            limit((2*fex + gex)/(fex + 2*gex), x, 1) == 5 and all((fex + gex - lo).subs(x, p) >= 0 and (hi - fex - gex).subs(x, p) >= 0 for p in range(-5, 6)))
    u, v = symbols('u v')
    tr = solve([Eq((2*u + v)/(u + 2*v), 5), Eq(u + v, 4)], [u, v], dict=True)[0]
    c.trap(1, tr[u] - tr[v])

    r = local(3, -4, lambda F, G, u, v: limit(F - G, x, 1))
    c.check("2: 답 유일", len(r) == 1)
    c.ans(2, list(r)[0])


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
