from lib import *

def stem(kind, S):
    return (r"함수 $f(x)$는 최고차항의 계수가 $1$인 " + kind + r"이고, 실수 $t$에 대하여 곡선 $y=f(x)$ 위의 점 $(t,\,f(t))$에서의 접선의 기울기를 함수 $g(t)$라 하자. "
            r"$\left\{x\,\middle|\,\displaystyle\lim_{h\to0}\frac{f(x+h)-f(x)}{h}=2\right\}=\{" + S + r"\}$일 때, ")

ORIG = dict(
    id="62p-34", chapter=3, page=62, num=34, source="2024년 수능특강 [24009-0067]", type="객관식",
    stem=stem("삼차함수", "-3,\\,4") + r"$g(-2)$의 값은?", choices=["-20", "-19", "-18", "-17", "-16"], answer="-16",
    general="g=f'. f'(x)=2 의 해가 −3, 4 뿐 → f'(x)−2=3(x+3)(x−4) → g(−2)=3·1·(−6)+2=−16.",
    special="① f' 이 이차라 해 두 개가 곧 인수 전부 — f 가 사차면 f'−2 가 삼차라 한 근이 중근이어야 하고 어느 쪽인지 두 경우. ② f'−2 의 최고차 계수는 3 (1 아님).",
    perspective="방정식 f'(x)=2 의 해집합 = f'−2 의 서로 다른 실근.",
    table=[
        ("f 삼차 (f'−2 이차, 근 2개)", "f 사차 (중근 위치 두 경우)", "사차면 4(x+3)²(x−4) 또는 4(x+3)(x−4)²"),
        ("해집합 {−3,4}", "—", "{−1,4} 면 g(−2)=20 (생존)"),
    ],
    sweep=["f 차수 n: f'−2 는 n−1 차, 서로 다른 실근 2개 → n=3 이면 인수 결정, n=4 이면 중근 2가지"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (f'−2 가 삼차면 중근이 −3 인지 4 인지 두 경우)",
        changed=["삼차함수 → 사차함수", "묻는 값: g(−2) 의 모든 값의 합"],
        naturalness="사차로 바꾸면 f 가 두 가지로 나뉘므로 값의 합을 묻는다.",
        stem=stem("사차함수", "-3,\\,4") + r"가능한 모든 $g(-2)$의 값의 합을 구하시오.", answer="124", trap_answer="-22",
        trap_path="f'−2 의 중근을 −3 쪽 하나로만 잡아 4(x+3)²(x−4) → −22 (4(x+3)(x−4)² 도 가능).",
        explanation=[
            r"$g(x)=f'(x)$이고 $f'(x)-2$는 최고차항의 계수가 $4$인 삼차식이며 서로 다른 실근이 $-3$, $4$뿐이다.",
            r"삼차식은 실근을 세 개(중복 포함) 가지므로 둘 중 하나가 중근이다.",
            r"함정: 중근은 $-3$일 수도 $4$일 수도 있다. $4(x+3)^2(x-4)$이면 $g(-2)=-24+2=-22$이다.",
            r"$4(x+3)(x-4)^2$이면 $g(-2)=144+2=146$이다.",
            r"합은 $124$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (해집합 {−3,4} → {−1,4})",
        changed=["해집합 {−3, 4} → {−1, 4}"], naturalness="",
        stem=stem("삼차함수", "-1,\\,4") + r"$g(-2)$의 값은?", choices=["16", "18", "20", "22", "24"], answer="20", trap_answer=None, trap_path=None,
        explanation=[
            r"$g(x)=f'(x)$이고 $f'(x)=2$의 해가 $-1$, $4$뿐이다.",
            r"$f'(x)-2=3(x+1)(x-4)$이다.",
            r"$g(-2)=3\times(-1)\times(-6)+2=20$이다.",
        ],
    ),
]


def real_roots(p):
    return {r for r in Poly(p, x).real_roots()}


def g_values(n, S):
    """최고차 1 인 n 차 f 중 {x | f'(x)=2} = S 인 것들의 f'(−2) 집합 (계수 일반형에서 풀이)"""
    cs = symbols(f'c1:{n}')
    fp = n*x**(n - 1) + sum(i*ci*x**(i - 1) for i, ci in zip(range(1, n), cs))
    eqs = [fp.subs(x, s) - 2 for s in S]
    vals = set()
    sols = solve(eqs, cs, dict=True)
    assert len(sols) == 1
    fam = fp.subs(sols[0])
    free = sorted(fam.free_symbols - {x}, key=str)
    if not free:
        assert real_roots(fam - 2) == set(S)
        return {fam.subs(x, -2)}
    # 자유 계수 1개: f'−2 = n(x−s1)(x−s2)(x−γ) 꼴 → 해집합이 S 가 되려면 γ∈S (다른 γ 는 해 추가)
    assert len(free) == 1
    t = free[0]
    for gam in list(S) + [Rational(1, 2), -7, 10]:  # S 원소와 다른 γ 샘플
        tv = solve(Poly(expand(fam - 2 - n*prod(x - s for s in S)*(x - gam)), x).coeffs(), t)
        tv = tv[t] if isinstance(tv, dict) else tv[0]
        h = fam.subs(t, tv)
        ok = real_roots(h - 2) == set(S)
        assert ok == (gam in S), gam
        if ok:
            vals.add(h.subs(x, -2))
    return vals


def verify(c):
    v = g_values(3, [-3, 4])
    c.check("원문: 유일", len(v) == 1)
    c.ans('orig', v.pop())
    v = g_values(4, [-3, 4])
    c.check("1: 두 경우", v == {-22, 146})
    c.ans(1, sum(v))
    c.trap(1, expand(4*(x + 3)**2*(x - 4) + 2).subs(x, -2))
    v = g_values(3, [-1, 4])
    c.check("2: 유일", len(v) == 1)
    c.ans(2, v.pop())


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='8', trap_path="f'−2 의 최고차항 계수를 1 로 두어 (x+1)(x−4) → g(−2)=6+2=8 (f' 의 최고차항 계수는 3).")
VARS[1]['choices'] = ['8', '12', '16', '20', '24']
VARS[1]['explanation'].insert(-1, "함정: $f'(x)-2$의 최고차항의 계수는 $1$이 아니라 $3$이다.")
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, ((x + 1)*(x - 4) + 2).subs(x, -2))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '생존형: 원문 풀이가 그대로 통하고 함정이 계산 실수 수준'
