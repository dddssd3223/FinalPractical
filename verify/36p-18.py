from lib import *

F_TXT = r"f(x)=\begin{cases}\dfrac{1}{(x+1)(x-4)} & (x\neq-1,\ x\neq4)\\ 1 & (x=-1\ \text{또는}\ x=4)\end{cases}"

ORIG = dict(
    id="36p-18", chapter=2, page=36, num=18, source="2024년 수능특강 [24009-0033]", type="주관식",
    stem=r"함수 $" + F_TXT + r"$가 닫힌구간 $[a-1,\,a+1]$에서 최댓값과 최솟값을 모두 갖도록 하는 정수 $a\,(-10<a<10)$의 개수를 구하시오.",
    answer="13",
    general="x=−1, 4 근처에서 f→±∞ (−1−: +∞, −1+: −∞, 4−: −∞, 4+: +∞). 구간이 −1 또는 4 를 포함(끝점 포함)하면 한쪽이 무한 → 최댓값·최솟값 중 하나가 없음. 제외 a∈{−2,−1,0,3,4,5}, 19−6=13.",
    special="① 특이점이 구간에 들어오면 무조건 제외 — '둘 다' 묻기 때문. 최솟값만 물으면 +∞ 쪽으로만 발산하는 구간은 살아남음.",
    perspective="특이점 근방의 한쪽 극한 부호표를 먼저 만든다.",
    table=[
        ("최댓값과 최솟값 모두", "한쪽만 필요한 경우", "최솟값만 물으면 [−3,−1], [4,6] 은 가능"),
        ("구간 길이 2", "—", "길이 4 면 제외 10 개 (생존)"),
    ],
    sweep=["−1−: +∞, −1+: −∞, 4−: −∞, 4+: +∞"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (최솟값만: +∞ 로만 가는 끝점은 허용)",
        changed=["'최댓값과 최솟값을 모두' → '최솟값을'"], naturalness="",
        stem=r"함수 $" + F_TXT + r"$가 닫힌구간 $[a-1,\,a+1]$에서 최솟값을 갖도록 하는 정수 $a\,(-10<a<10)$의 개수를 구하시오.",
        answer="15", trap_answer="13",
        trap_path="원문처럼 −1, 4 를 포함하는 구간을 모두 제외(6개) → 13.",
        explanation=[
            r"$x\to-1-$일 때 $+\infty$, $x\to-1+$일 때 $-\infty$, $x\to4-$일 때 $-\infty$, $x\to4+$일 때 $+\infty$이다.",
            r"최솟값이 없으려면 구간 안에서 $-\infty$로 가는 쪽이 있어야 한다: $-1$의 오른쪽 또는 $4$의 왼쪽을 포함하는 경우.",
            r"$a=-1$ ($[-2,0]$), $a=0$ ($[-1,1]$), $a=3$ ($[2,4]$), $a=4$ ($[3,5]$)만 제외된다.",
            r"함정: $a=-2$ ($[-3,-1]$)와 $a=5$ ($[4,6]$)는 $+\infty$로만 가므로 최솟값 $\frac1{14}$을 갖는다. 개수는 $19-4=15$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (구간 길이 2 → 4)",
        changed=["[a−1, a+1] → [a−2, a+2]"], naturalness="",
        stem=r"함수 $" + F_TXT + r"$가 닫힌구간 $[a-2,\,a+2]$에서 최댓값과 최솟값을 모두 갖도록 하는 정수 $a\,(-10<a<10)$의 개수를 구하시오.",
        answer="9", trap_answer=None, trap_path=None,
        explanation=[
            r"구간이 $-1$ 또는 $4$를 포함하면 한쪽 극한이 무한대라 최댓값이나 최솟값이 없다.",
            r"$|a+1|\le2$: $a=-3,\ldots,1$ (5개), $|a-4|\le2$: $a=2,\ldots,6$ (5개)를 제외한다.",
            r"$19-10=9$개이다.",
        ],
    ),
]

P = [(1/((x + 1)*(x - 4)), -oo, -1), (1/((x + 1)*(x - 4)), -1, 4), (1/((x + 1)*(x - 4)), 4, oo)]
g = 1/((x + 1)*(x - 4))


def extrema(lo, hi):
    """닫힌구간 [lo, hi] 에서 (최댓값 존재, 최솟값 존재)"""
    has_max = has_min = True
    for s in (-1, 4):
        if lo <= s <= hi:
            if s > lo:
                v = limit(g, x, s, '-')
                has_max &= v != oo; has_min &= v != -oo
            if s < hi:
                v = limit(g, x, s, '+')
                has_max &= v != oo; has_min &= v != -oo
    return has_max, has_min


def verify(c):
    A = range(-9, 10)
    c.ans('orig', sum(1 for a in A if all(extrema(a - 1, a + 1))))
    c.ans(1, sum(1 for a in A if extrema(a - 1, a + 1)[1]))
    c.trap(1, sum(1 for a in A if all(extrema(a - 1, a + 1))))
    c.ans(2, sum(1 for a in A if all(extrema(a - 2, a + 2))))
    c.check("특이점 밖 구간에서는 연속 (최대·최소 존재)", all(extrema(a - 1, a + 1) == (True, True) for a in (-9, 2, 8)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
