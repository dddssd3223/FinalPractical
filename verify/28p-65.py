from lib import *

BOX = r"모든 실수 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{g(x)\times|f(x)|}{f(x)}$의 값과 $\displaystyle\lim_{x\to a}\frac{|g(x)-f(x)|}{g(x)}$의 값이 모두 존재한다."
ORIG = dict(
    id="28p-65", chapter=1, page=28, num=65, source="2026학년도 수능 6월 모의평가 21번", type="주관식",
    stem=r"함수 $f(x)=(x-1)(x-2)$와 최고차항의 계수가 $1$인 사차함수 $g(x)$가 다음 조건을 만족시킨다. $g(-1)$의 값을 구하시오. [4점]",
    box=[BOX], answer="42",
    general="첫 극한: f 부호가 바뀌는 1, 2 에서 g=0. 둘째: g 의 실근은 f 의 근이어야 하고(아니면 발산), 1, 2 에서 단순근이며 g'(1)=f'(1), g'(2)=f'(2). g=(x−1)(x−2)q, q(1)=q(2)=1 → q=(x−1)(x−2)+1=x²−3x+3 (실근 없음 ✓). g(−1)=6·7=42.",
    special="① q(1)=q(2)=1 만 풀고 q 에 실근이 없는지 확인 생략 — 최고차 계수 1 이면 판별식 −3 이라 우연히 통과. 계수가 4 이상이면 q 가 실근을 가져 조건 위반.",
    perspective="q=k(x−1)(x−2)+1 의 판별식 k(k−4)<0 ⇔ 0<k<4.",
    table=[
        ("g 최고차 계수 1", "q 가 실근을 갖는 경우(k≥4 또는 k<0)", "계수를 자연수로 풀면 k=1,2,3 만 가능, k=4 는 중근 3/2 에서 위반"),
        ("f 의 두 근 간격 1", "간격 ≥2 (q 실근)", "—"),
    ],
    sweep=["q 의 판별식 k(k−4): k=4 에서 중근", "g 의 1, 2 에서 근 차수 ≥2 이면 둘째 극한 발산"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (q 가 실근을 갖지 않아야 함, 경계 k=4)",
        changed=["g 최고차 계수 1 → 자연수", "묻는 값: g(−1) 의 모든 값의 합"],
        naturalness="계수를 자연수로 풀어 여러 g 가 생기므로 '모든 값의 합'으로 묻는 것은 필수.",
        stem=r"함수 $f(x)=(x-1)(x-2)$와 최고차항의 계수가 자연수인 사차함수 $g(x)$가 다음 조건을 만족시킨다. $g(-1)$의 값이 될 수 있는 모든 값의 합을 구하시오.",
        box=[BOX], answer="234", trap_answer="384",
        trap_path="q=k(x−1)(x−2)+1 의 판별식을 k(k−4)≤0 으로 잡아 k=4 까지 포함 → 42+78+114+150=384.",
        explanation=[
            r"원문과 같이 $g(x)=(x-1)(x-2)q(x)$, $q(1)=q(2)=1$이고 $q$는 실근이 없어야 한다.",
            r"최고차항의 계수를 $k$라 하면 $q(x)=k(x-1)(x-2)+1$이고 판별식은 $k^2-4k$이다.",
            r"함정: $k=4$이면 $q=(2x-3)^2$이 되어 $x=\frac32$에서 $g=0$, $f\neq0$이므로 둘째 극한이 없다. 따라서 $k=1,2,3$.",
            r"$g(-1)=6q(-1)=6(6k+1)$이므로 $42+78+114=234$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 1행 (최고차 계수 1 → 2, 판별식 음수 유지)",
        changed=["g 최고차 계수 1 → 2"], naturalness="",
        stem=r"함수 $f(x)=(x-1)(x-2)$와 최고차항의 계수가 $2$인 사차함수 $g(x)$가 다음 조건을 만족시킨다. $g(-1)$의 값을 구하시오.",
        box=[BOX], answer="78", trap_answer=None, trap_path=None,
        explanation=[
            r"첫 극한에서 $g(1)=g(2)=0$, 둘째 극한에서 $g$의 실근은 $1$, $2$뿐이고 $g'(1)=f'(1)$, $g'(2)=f'(2)$이다.",
            r"$g(x)=(x-1)(x-2)q(x)$에서 $q(1)=q(2)=1$, $q(x)=2(x-1)(x-2)+1=2x^2-6x+5$ (실근 없음)이다.",
            r"$g(-1)=6\times13=78$이다.",
        ],
    ),
]

F = (x - 1)*(x - 2)


def conds_ok(G):
    pts = sorted(set([Rational(1), Rational(2)] + [r for r in real_roots(Poly(G, x))] + [Rational(k, 4) for k in range(-8, 16)]))
    for a in pts:
        if not lim_exists(G*Abs(F)/F, a)[0]:
            return False
        if not lim_exists(Abs(G - F)/G, a)[0]:
            return False
    return True


def g_of(k):
    b, cc = symbols('b cc', real=True)
    q = k*x**2 + b*x + cc
    G = F*q
    s = solve([diff(G, x).subs(x, 1) - diff(F, x).subs(x, 1), diff(G, x).subs(x, 2) - diff(F, x).subs(x, 2)], [b, cc], dict=True)[0]
    return expand(G.subs(s)), expand(q.subs(s))


def verify(c):
    G, q = g_of(1)
    c.check("원문: 조건 전수 확인", conds_ok(G))
    c.ans('orig', G.subs(x, -1))
    good, allk = [], []
    for k in range(1, 8):
        G, q = g_of(k)
        allk.append((k, G))
        if conds_ok(G):
            good.append(G)
    c.check("1: 가능한 k = 1,2,3", [k for k, G in allk if conds_ok(G)] == [1, 2, 3])
    c.ans(1, sum(G.subs(x, -1) for G in good))
    c.trap(1, sum(G.subs(x, -1) for k, G in allk if discriminant(g_of(k)[1], x) <= 0))
    G, q = g_of(2)
    c.check("2: 조건 전수 확인", conds_ok(G))
    c.ans(2, G.subs(x, -1))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
