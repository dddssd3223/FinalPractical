from lib import *

ORIG = dict(
    id="9p-15", chapter=1, page=9, num=15, source="2024년 수능완성 [24054-0093]", type="객관식",
    stem=r"두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킨다. $\displaystyle\lim_{x\to0}\frac{f(x)g(x)\{g(x)-2\}}{x^2}$의 값은?",
    box=[r"(가) $\displaystyle\lim_{x\to0}\frac{f(x)+g(x)-2}{x}=5$",
         r"(나) 모든 실수 $x$에 대하여 $\{f(x)+x\}\{g(x)-2\}=x^2\{f(x)+9\}$이다."],
    choices=["4", "6", "8", "10", "12"], answer="12",
    general="(가)에서 f(0)+g(0)=2, (나)에 x=0 → f(0){g(0)−2}=0. 두 경우 모두 f(0)=0, g(0)=2. f=xq, g−2=xp 로 두면 (q+1)p=xq+9, q(0)+p(0)=5. x=0 대입: (q₀+1)p₀=9 → p₀²−6p₀+9=0 → p₀=3, q₀=2. 극한 = q₀·g(0)·p₀ = 2·2·3 = 12.",
    special="① (나)에서 곧바로 'f(0)=0 이고 g(0)=2' 로 둠 → (가)의 상수가 2일 때만 두 경우가 합쳐짐. ② p₀ 의 이차방정식이 중근이라 한 값만 나오는 것은 상수 9 덕분(다른 상수면 두 쌍 가능). ③ 식을 f/x, g, (g−2)/x 로 쪼개는 것은 f(0)=0 일 때만 가능.",
    perspective="x=0 근방 전개(0차·1차 계수)만 비교하면 된다. (나)의 상수 K 에 대해 p₀²−6p₀+K=0.",
    table=[
        ("(가)의 상수 2", "f(0)=0 인 경우와 g(0)=2 인 경우가 같은 결론", "상수를 바꾸면 f(0)≠0 인 경우가 생기고 한쪽 경우는 모순"),
        ("(나)의 상수 9", "p₀ 가 두 개인 경우(중근으로 고정)", "8 로 바꾸면 p₀=2, 4 두 경우 모두 다항식 존재"),
        ("(가)의 극한값 5", "—", "q₀+p₀ 값이 바뀜"),
    ],
    sweep=["p₀²−(d+1)p₀+K=0 의 판별식 (d+1)²−4K=0 ⇔ 원문 (d=5, K=9)", "f(0)+g(0)=c 에서 c≠2 이면 f(0)=c−2 (g(0)=2) 경우만 가능"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 6 (x=0 대입에서 나온 두 경우 f(0)=0, g(0)=2 가 서로 다른 해로 갈라짐)",
        changed=["(가) (f+g−2)/x=5 → (f+g−11)/x=−2", "묻는 값: g(1)의 모든 값의 합"],
        naturalness="바꾼 조건은 (가)의 상수 둘. 두 경우가 모두 존재하므로 묻는 값을 '모든 값의 합'으로 바꾼 것은 필수.",
        stem=r"두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킬 때, $g(1)$의 값이 될 수 있는 모든 값의 합은?",
        box=[r"(가) $\displaystyle\lim_{x\to0}\frac{f(x)+g(x)-11}{x}=-2$",
             r"(나) 모든 실수 $x$에 대하여 $\{f(x)+x\}\{g(x)-2\}=x^2\{f(x)+9\}$이다."],
        choices=["4", "11", "13", "15", "17"], answer="15", trap_answer="11",
        trap_path="원문처럼 f(0)=0 만 보고 g(0)=11 → f=x²−x, g=x²−x+11 → g(1)=11 에서 멈춤(g(0)=2 인 경우 누락).",
        explanation=[
            r"(가)에서 $f(0)+g(0)=11$, (나)에 $x=0$을 넣으면 $f(0)\{g(0)-2\}=0$이다.",
            r"(i) $f(0)=0$, $g(0)=11$: $f(x)+x=x^2r(x)$로 두면 $r\{g-2-x^2\}=9-x$이고 (가)까지 만족시키는 것은 $f=x^2-x$, $g=x^2-x+11$뿐이다.",
            r"(ii) $g(0)=2$, $f(0)=9$: $g-2=x^2s(x)$ 꼴이 되고 $f=9-2x$, $g=2x^2+2$가 조건을 만족시킨다.",
            r"함정: 원문은 (가)의 상수가 $2$여서 두 경우가 같은 결론이었지만 여기서는 서로 다른 해가 된다.",
            r"$g(1)$의 값은 $11$, $4$이므로 합은 $15$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 (중근을 만들던 상수 9 → 8, 두 경우 모두 존재)",
        changed=["(나)의 상수 9 → 8", "묻는 값: 가능한 모든 값의 합"],
        naturalness="바꾼 조건은 상수 하나. 경우가 둘로 갈려 묻는 값을 '모든 값의 합'으로 바꾼 것은 필수.",
        stem=r"두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킬 때, $\displaystyle\lim_{x\to0}\frac{f(x)g(x)\{g(x)-2\}}{x^2}$의 값이 될 수 있는 모든 값의 합은?",
        box=[r"(가) $\displaystyle\lim_{x\to0}\frac{f(x)+g(x)-2}{x}=5$",
             r"(나) 모든 실수 $x$에 대하여 $\{f(x)+x\}\{g(x)-2\}=x^2\{f(x)+8\}$이다."],
        choices=["8", "12", "16", "20", "24"], answer="20", trap_answer="12",
        trap_path="p₀²−6p₀+8=0 에서 한 근(p₀=2)만 쓰고 끝냄 → 12. (다른 근 p₀=4 도 f=x, g=½x²+4x+2 로 실제 존재)",
        explanation=[
            r"원문과 같이 $f(0)=0$, $g(0)=2$이고 $f=xq$, $g-2=xp$로 두면 $(q+1)p=xq+8$, $q(0)+p(0)=5$이다.",
            r"$x=0$을 넣으면 $(q_0+1)p_0=8$, 즉 $p_0^2-6p_0+8=0$에서 $p_0=2$ 또는 $p_0=4$이다.",
            r"$p_0=2$: $f=3x$, $g=\tfrac34x^2+2x+2$ → 극한 $3\cdot2\cdot2=12$",
            r"$p_0=4$: $f=x$, $g=\tfrac12x^2+4x+2$ → 극한 $1\cdot2\cdot4=8$",
            r"함정: 원문은 상수 $9$로 중근을 만들어 한 경우만 남겼다. 두 경우가 모두 존재하므로 합은 $20$이다.",
        ],
    ),
]


def families(K, c, d, maxf=2, maxg=2):
    """(f+x)(g−2)=x²(f+K), f(0)+g(0)=c, f'(0)+g'(0)=d 를 만족시키는 다항식 쌍 (차수 제한 내, 조건을 함께 풀어 특수해 누락 방지)"""
    res = set()
    for df in range(maxf + 1):
        for dg in range(maxg + 1):
            fc = symbols(f'a0:{df+1}'); gc = symbols(f'b0:{dg+1}')
            f = sum(cf * x**i for i, cf in enumerate(fc)); g = sum(cg * x**i for i, cg in enumerate(gc))
            eqs = Poly(expand((f + x)*(g - 2) - x**2*(f + K)), x).all_coeffs()
            eqs += [f.subs(x, 0) + g.subs(x, 0) - c, diff(f + g, x).subs(x, 0) - d]
            for s in solve(eqs, list(fc) + list(gc), dict=True):
                F, G = expand(f.subs(s)), expand(g.subs(s))
                res.add((F, G))  # 매개변수가 남으면 값 집합 검사에서 걸러짐
    return sorted(res, key=str)


def values(K, c, d):
    return {simplify(limit(F*G*(G - 2)/x**2, x, 0)) for F, G in families(K, c, d)}


def verify(c):
    v0 = values(9, 2, 5)
    c.check("원문: 극한값이 하나로 결정", len(v0) == 1)
    c.ans('orig', list(v0)[0])
    fam1 = families(9, 11, -2)
    c.check("1: 해가 정확히 두 쌍 (f(0)=0 인 쌍, g(0)=2 인 쌍)", len(fam1) == 2
            and {F.subs(x, 0) for F, G in fam1} == {0, 9})
    c.ans(1, sum(G.subs(x, 1) for F, G in fam1))
    c.trap(1, [G.subs(x, 1) for F, G in fam1 if F.subs(x, 0) == 0][0])
    v2 = values(8, 2, 5)
    c.check("2: 극한값 두 개 {8, 12}", v2 == {8, 12})
    c.ans(2, sum(v2))
    c.trap(2, 12)
