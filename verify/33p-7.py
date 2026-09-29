from lib import *

ORIG = dict(
    id="33p-7", chapter=2, page=33, num=7, source="2025년 수능완성 [25054-0123]", type="주관식",
    stem=r"$k>-2$인 실수 $k$에 대하여 함수 $f(x)=\begin{cases}-2x^2-4x+6 & (x<1)\\ 2x+k & (x\ge1)\end{cases}$이다. 실수 $t$에 대하여 닫힌구간 $[t,\,t+2]$에서 함수 $f(x)$의 최댓값을 $g(t)$라 하자. 함수 $g(t)$가 실수 전체의 집합에서 연속일 때, $g(2)$의 최댓값을 구하시오.",
    answer="14",
    general="왼쪽 조각 −2(x+1)²+8 (꼭짓점 8), x→1− 에서 0, f(1)=2+k>0 (위로 점프). 구간이 x=1 을 처음 포함하는 t=−1 에서 구간 [−1,1] 의 최댓값은 max(8, 2+k), 직전은 8 → 2+k≤8, k≤6. g(2)=f(4)=8+k ≤ 14.",
    special="① '점프한 값 ≤ 직전 최댓값' 에서 직전 최댓값을 꼭짓점 8 로 잡음 — 구간 길이 2 라서 t=−1 일 때 꼭짓점이 구간 안에 있기 때문. 길이가 1 이면 비교 대상이 f(0)=6.",
    perspective="g 가 끊길 수 있는 곳 = 구간 끝이 점프 지점 x=1 을 지나는 순간. 그 순간 구간 안의 최댓값과 비교.",
    table=[
        ("구간 길이 2", "꼭짓점이 구간 밖인 경우", "길이 1 이면 t=0 에서 비교값이 f(0)=6 → k≤4"),
        ("k>−2 (위로 점프)", "아래로 점프(최댓값 존재 문제)", "—"),
        ("왼쪽 조각 +6", "—", "+10 이면 꼭짓점 12, k≤10 (생존)"),
    ],
    sweep=["t+2=1 (t=−1): 구간이 점프를 포함", "t=1: 구간 왼끝이 점프를 지남"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (구간 길이 → 점프 순간의 비교값이 꼭짓점이 아님)",
        changed=["구간 [t, t+2] → [t, t+1]", "g(2) → g(2) (최댓값 구간 [2,3])"],
        naturalness="실질 변경은 구간 길이 하나.",
        stem=r"$k>-2$인 실수 $k$에 대하여 함수 $f(x)=\begin{cases}-2x^2-4x+6 & (x<1)\\ 2x+k & (x\ge1)\end{cases}$이다. 실수 $t$에 대하여 닫힌구간 $[t,\,t+1]$에서 함수 $f(x)$의 최댓값을 $g(t)$라 하자. 함수 $g(t)$가 실수 전체의 집합에서 연속일 때, $g(2)$의 최댓값을 구하시오.",
        answer="10", trap_answer="12",
        trap_path="원문처럼 비교값을 꼭짓점 8 로 잡아 2+k≤8, k≤6 → g(2)=f(3)=6+k → 12.",
        explanation=[
            r"$f$는 $x<1$에서 $-2(x+1)^2+8$이고 $x\to1-$일 때 $0$, $f(1)=2+k>0$이다.",
            r"구간 $[t,\,t+1]$이 처음 $x=1$을 포함하는 것은 $t=0$일 때이고, 이때 구간 $[0,1)$에서 $f$는 감소하므로 직전 최댓값은 $f(0)=6$에 가깝다.",
            r"함정: 꼭짓점 $x=-1$은 구간 $[0,1]$ 밖이므로 비교값은 $8$이 아니라 $6$이다. 연속이려면 $2+k\le6$, $k\le4$이다.",
            r"$g(2)=\max_{[2,3]}f=f(3)=6+k\le10$이므로 최댓값은 $10$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 3행 (왼쪽 조각 상수 6 → 10, 범위 k>2)",
        changed=["왼쪽 조각 −2x²−4x+6 → −2x²−4x+10", "k>−2 → k>2 (위로 점프 유지)"],
        naturalness="꼭짓점만 올리고, 점프 방향(위로)이 유지되도록 범위를 함께 옮긴 한 가지 변경.",
        stem=r"$k>2$인 실수 $k$에 대하여 함수 $f(x)=\begin{cases}-2x^2-4x+10 & (x<1)\\ 2x+k & (x\ge1)\end{cases}$이다. 실수 $t$에 대하여 닫힌구간 $[t,\,t+2]$에서 함수 $f(x)$의 최댓값을 $g(t)$라 하자. 함수 $g(t)$가 실수 전체의 집합에서 연속일 때, $g(2)$의 최댓값을 구하시오.",
        answer="18", trap_answer=None, trap_path=None,
        explanation=[
            r"$x<1$에서 $f(x)=-2(x+1)^2+12$이고 $x\to1-$일 때 $4$, $f(1)=2+k>4$이다.",
            r"$t=-1$일 때 구간 $[-1,1]$의 최댓값은 $\max(12,\,2+k)$이고 직전은 $12$이므로 $2+k\le12$, $k\le10$이다.",
            r"$g(2)=f(4)=8+k\le18$이다.",
        ],
    ),
]


def make_g(left, k, L):
    """[t, t+L] 에서의 최댓값 g(t) (수치). 왼쪽 조각은 x<1, 오른쪽 2x+k (x≥1)."""
    lf = lambdify(x, left)
    f = lambda v: lf(v) if v < 1 else 2*v + k
    vx = float(solve(diff(left, x), x)[0])
    lim1 = lf(1.0)

    def g(t):
        a, b = t, t + L
        cands = [f(a), f(b)]
        if a <= vx <= b and vx < 1:
            cands.append(lf(vx))
        if a <= 1 <= b:
            cands.append(f(1.0))
            if a < 1 and lim1 > max(cands) + 1e-12:
                return None  # 최댓값 없음
        return max(cands)
    return g


def continuous(left, k, L):
    g = make_g(left, k, L)
    ts = [i/400 for i in range(-2400, 2400)]
    vals = [g(t) for t in ts]
    if any(v is None for v in vals):
        return False
    return all(abs(vals[i + 1] - vals[i]) < 0.1 for i in range(len(vals) - 1))


def best_k(left, klo, L, kmax_claim):
    ok_at = continuous(left, kmax_claim, L)
    bad_above = not continuous(left, kmax_claim + 0.5, L)
    ok_below = all(continuous(left, kv, L) for kv in (klo + 0.5, (klo + kmax_claim)/2))
    return ok_at and bad_above and ok_below


def verify(c):
    left = -2*x**2 - 4*x + 6
    c.check("원문: 연속 ⇔ k≤6 (경계 수치 확인)", best_k(left, -2, 2, 6))
    c.ans('orig', nsimplify(make_g(left, 6, 2)(2)))
    c.check("1: 연속 ⇔ k≤4", best_k(left, -2, 1, 4))
    c.ans(1, nsimplify(make_g(left, 4, 1)(2)))
    c.trap(1, nsimplify(make_g(left, 6, 1)(2)))
    left2 = -2*x**2 - 4*x + 10
    c.check("2: 연속 ⇔ k≤10", best_k(left2, 2, 2, 10))
    c.ans(2, nsimplify(make_g(left2, 10, 2)(2)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
