from lib import *

def stem(A, rng):
    return (r"함수 $f(x)=x^3-2x$에 대하여 곡선 $y=f(x)$ 위의 점 $\mathrm A" + A + r"$에서의 접선이 이 곡선과 만나는 점 중 $\mathrm A$가 아닌 점을 $\mathrm B(b,\,f(b))$라 하자. "
            r"직선 $x=k\ (" + rng + r")$가 곡선 $y=f(x)$와 만나는 점을 $\mathrm P_k$라 할 때, 삼각형 $\mathrm{AP}_k\mathrm B$의 넓이의 최댓값은?")

ORIG = dict(
    id="81p-5", chapter=4, page=81, num=5, source="2022년 수능완성 [22054-0132]", type="객관식",
    stem=stem("(-1,\\,1)", r"-1<k<b"), choices=["5", "21/4", "11/2", "23/4", "6"], answer="6",
    general="접선 y=x+2, x³−3x−2=(x+1)²(x−2) → B(2,4). 넓이=(3/2)(k+2−f(k))=(3/2)(−k³+3k+2) → k=1 에서 최대 4 → 6.",
    special="① 최대가 되는 k=1 이 허용 범위 안 — 범위가 k≤0 이면 끝점에서 최대.",
    perspective="넓이 = 밑변 AB × (P 와 직선 사이 세로 거리)/… — 세로 차의 최대.",
    table=[
        ("k 범위 (−1, 2)", "(−1, 0] (꼭짓점 k=1 밖)", "−1<k≤0 이면 k=0 에서 최대 → 3"),
        ("접점 A(−1,1)", "—", "A(−2,−4) 면 B(4,56), 최댓값 96 (생존)"),
    ],
    sweep=["최댓값 위치 k=1 과 범위 끝의 비교"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (극대점이 범위 밖이면 끝점)",
        changed=["k 의 범위 −1<k<b → −1<k≤0"], naturalness="",
        stem=stem("(-1,\\,1)", r"-1<k\le0"), choices=["3", "4", "5", "11/2", "6"], answer="3", trap_answer="6",
        trap_path="원문처럼 k=1 에서의 최댓값 6 을 씀 (k=1 은 범위 밖).",
        explanation=[
            r"접선은 $y=x+2$이고 $x^3-3x-2=(x+1)^2(x-2)$이므로 $\mathrm B(2,4)$이다.",
            r"넓이는 $\frac12\times3\times\{(k+2)-f(k)\}=\frac32(-k^3+3k+2)$이다.",
            r"함정: $-k^3+3k+2$는 $k=1$에서 최대이지만 범위 $-1<k\le0$에서는 증가하므로 $k=0$에서 최대이다.",
            r"최댓값은 $\frac32\times2=3$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (A(−1,1) → A(−2,−4))",
        changed=["A(−1,1) → A(−2,−4)"], naturalness="",
        stem=stem("(-2,\\,-4)", r"-2<k<b"), choices=["80", "88", "96", "104", "112"], answer="96", trap_answer=None, trap_path=None,
        explanation=[
            r"$f'(-2)=10$이므로 접선은 $y=10x+16$이고 $x^3-12x-16=(x+2)^2(x-4)$에서 $\mathrm B(4,56)$이다.",
            r"넓이는 $\frac12\times6\times\{10k+16-f(k)\}=3(k+2)^2(4-k)$이다.",
            r"$k=2$에서 최대 $3\times16\times2=96$이다.",
        ],
    ),
]


def max_area(a, lo_open, hi, hi_closed):
    f = x**3 - 2*x
    t = diff(f, x).subs(x, a)*(x - a) + f.subs(x, a)
    roots = [r for r in solve(f - t, x) if r != a]
    b = roots[0]
    k = Symbol('k', real=True)
    A, B, P = (a, f.subs(x, a)), (b, f.subs(x, b)), (k, f.subs(x, k))
    hi = b if hi is None else hi
    # 부호 고정 구간에서 다항식으로
    sgn = sign(((B[0] - A[0])*(P[1] - A[1]) - (B[1] - A[1])*(P[0] - A[0])).subs(k, (lo_open + hi)/2))
    g = expand(sgn*((B[0] - A[0])*(P[1] - A[1]) - (B[1] - A[1])*(P[0] - A[0]))/2)
    cands = [r for r in solve(diff(g, k), k) if r.is_real and lo_open < r < hi]
    if hi_closed:
        cands.append(hi)
    vals = [g.subs(k, r) for r in cands]
    sup_open = max([g.subs(k, lo_open)] + ([] if hi_closed else [g.subs(k, hi)]))
    m = max(vals)
    assert m > sup_open  # 최댓값이 실제로 달성됨
    return m


def verify(c):
    c.ans('orig', max_area(-1, -1, None, False))
    c.ans(1, max_area(-1, -1, 0, True))
    c.trap(1, max_area(-1, -1, None, False))
    c.ans(2, max_area(-2, -2, None, False))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
