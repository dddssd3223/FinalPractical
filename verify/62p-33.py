from lib import *

BOX = lambda m: [r"(가) $\displaystyle\lim_{x\to\infty}\frac{\{f(x)\}^2}{3x^2f(x)+f(x^2)}=3$", r"(나) $\displaystyle\lim_{x\to0}\frac{f(x)}{x}=" + m + r"$"]

ORIG = dict(
    id="62p-33", chapter=3, page=62, num=33, source="2023년 수능특강 [23009-0065]", type="객관식",
    stem=r"이차함수 $f(x)$가 다음 조건을 만족시킬 때, $f'(1)$의 값은?",
    box=BOX("2"), choices=["24", "26", "28", "30", "32"], answer="26",
    general="(나) → f(0)=0, f'(0)=2 → f=ax²+2x. (가): 분자 a²x⁴, 분모 3ax⁴+ax⁴=4ax⁴ → a/4=3 → a=12 → f'(1)=26.",
    special="① 이차라 3x²f 와 f(x²) 가 둘 다 x⁴ — 차수가 3 이상이면 f(x²) 만 최고차 (분모 계수 a), 1차면 3x²f 만.",
    perspective="분모 두 항의 차수 비교가 차수 n 에 따라 갈림.",
    table=[
        ("f 가 이차 (3x²f, f(x²) 같은 차수)", "차수 미정 (n≥3 이면 a=3)", "'삼차 이하 다항함수' 면 n=2, n=3 두 경우"),
        ("(나) 값 2", "—", "4 면 f=12x²+4x → 28 (생존)"),
    ],
    sweep=["n=1: 극한 0 / n=2: a/4 / n≥3: a"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (차수가 정해지지 않으면 n=2, n=3 두 경우)",
        changed=["이차함수 → 삼차 이하의 다항함수", "f(1)=14 추가, 묻는 값: f'(1) 의 모든 값의 합"],
        naturalness="차수를 열어 두면 삼차에서 이차항 계수가 남으므로 f(1)=14 로 정했고, 두 경우가 모두 가능해 값의 합을 묻는다.",
        stem=r"삼차 이하의 다항함수 $f(x)$가 다음 조건을 만족시키고 $f(1)=14$일 때, 가능한 모든 $f'(1)$의 값의 합을 구하시오.",
        box=BOX("2"), answer="55", trap_answer="26",
        trap_path="원문처럼 이차함수만 보고 f=12x²+2x → 26 (삼차 f=3x³+9x²+2x 도 가능).",
        explanation=[
            r"(나)에서 $f(0)=0$, $f'(0)=2$이다. 최고차 $n$, 최고차항 계수 $a$라 하자.",
            r"$n=1$이면 (가)의 극한은 $0$이다. $n=2$이면 분모의 최고차항이 $4ax^4$이므로 $\frac a4=3$, $a=12$이다.",
            r"함정: $n=3$이면 분모는 $f(x^2)$의 $ax^6$만 남아 $a=3$이다. $f=3x^3+bx^2+2x$, $f(1)=14$에서 $b=9$이다.",
            r"$n=2$: $f=12x^2+2x$, $f'(1)=26$ / $n=3$: $f'(1)=9+18+2=29$이다.",
            r"합은 $55$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 ((나) 값 2 → 4)",
        changed=["(나) 값 2 → 4"], naturalness="",
        stem=r"이차함수 $f(x)$가 다음 조건을 만족시킬 때, $f'(1)$의 값은?",
        box=BOX("4"), choices=["24", "26", "28", "30", "32"], answer="28", trap_answer=None, trap_path=None,
        explanation=[
            r"(나)에서 $f(0)=0$, $f'(0)=4$이므로 $f(x)=ax^2+4x$이다.",
            r"(가)에서 분자 $a^2x^4$, 분모 $4ax^4$이므로 $\frac a4=3$, $a=12$이다.",
            r"$f'(x)=24x+4$이므로 $f'(1)=28$이다.",
        ],
    ),
]


def solutions(degs, m, extra):
    """차수 n∈degs, 최고차 계수≠0 인 f 중 (가)(나)+extra 만족 → f 목록 (자유 계수 남으면 'free')"""
    out = []
    for n in degs:
        cs = symbols(f'c0:{n+1}')
        f = sum(ci*x**i for i, ci in enumerate(cs))
        f = f.subs({cs[0]: 0, cs[1]: m}) if n >= 1 else f  # (나): f(0)=0, f'(0)=m (극한 존재 조건)
        if n == 1:  # f=mx 로 결정: 극한 직접 계산
            if limit(f**2/(3*x**2*f + f.subs(x, x**2)), x, oo) == 3 and all(e == 0 for e in extra(f)):
                out.append(f)
            continue
        a = cs[n]
        P = Poly(expand(f**2), x)
        Q = Poly(expand(3*x**2*f + f.subs(x, x**2)), x)
        # a≠0 에서 Q 의 최고차 계수 (다른 계수가 0 이 되지 않도록 top 이 a 의 배수인지 확인)
        qd, qc = Q.degree(), Q.LC()
        assert simplify(qc/a).is_number, (n, qc)
        if P.degree() < qd:
            continue  # 극한 0
        assert P.degree() == qd
        eqs = [P.LC()/qc - 3] + extra(f)
        for s in solve(eqs, cs[2:n+1], dict=True):
            if s.get(a, a) == 0:
                continue
            g = f.subs(s)
            out.append(g if not (g.free_symbols - {x}) else 'free')
    return out


def verify(c):
    fs = solutions([2], 2, lambda f: [])
    c.check("원문: 이차 f 유일", len(fs) == 1 and fs[0] != 'free')
    g = fs[0]
    c.check("원문: 극한 재확인", limit(g**2/(3*x**2*g + g.subs(x, x**2)), x, oo) == 3 and limit(g/x, x, 0) == 2)
    c.ans('orig', diff(g, x).subs(x, 1))
    fs = solutions([1, 2, 3], 2, lambda f: [f.subs(x, 1) - 14])
    c.check("1: 두 경우, 자유 계수 없음", len(fs) == 2 and 'free' not in fs)
    c.check("1: 각 f 극한 재확인", all(limit(g**2/(3*x**2*g + g.subs(x, x**2)), x, oo) == 3 for g in fs))
    c.ans(1, sum(diff(g, x).subs(x, 1) for g in fs))
    c.trap(1, diff(solutions([2], 2, lambda f: [])[0], x).subs(x, 1))
    fs = solutions([2], 4, lambda f: [])
    c.check("2: 유일", len(fs) == 1)
    c.ans(2, diff(fs[0], x).subs(x, 1))
