from lib import *

def box(cond):
    return [r"(가) $f(4)=10$", r"(나) $2<x<4$인 모든 실수 $x$에 대하여 $" + cond + r"$이다."]

HEAD = r"다음 조건을 만족시키는 모든 다항함수 $f(x)$에 대하여 $f(2)$의 최댓값을 $M$, 최솟값을 $m$이라 할 때, $M-m$의 값은?"

ORIG = dict(
    id="81p-6", chapter=4, page=81, num=6, source="2023년 수능완성 [23054-0130]", type="객관식",
    stem=HEAD, box=box(r"|f'(x)|\le6"), choices=["18", "20", "22", "24", "26"], answer="24",
    general="평균값 정리: f(4)−f(2)=2f'(c), |f'(c)|≤6 → |f(4)−f(2)|≤12 → f(2)∈[−2,22] (f=±6(x−4)+10 에서 등호) → 24.",
    special="① 제한이 대칭(|f'|≤6)이라 위·아래 폭이 같음 — 비대칭 제한이면 폭이 달라짐.",
    perspective="평균값 정리로 기울기 제한 → 값 제한.",
    table=[
        ("대칭 제한 |f'|≤6", "비대칭 −2≤f'≤6", "비대칭이면 f(2)∈[−2,14] → 16"),
        ("상한 6", "—", "5 면 [0,20] → 20 (생존)"),
    ],
    sweep=["f(2)=f(4)−2f'(c), f'(c)∈[L,U] → 폭 2(U−L)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (비대칭 제한)",
        changed=["|f'(x)|≤6 → −2≤f'(x)≤6"], naturalness="",
        stem=HEAD, box=box(r"-2\le f'(x)\le6"), choices=["12", "16", "20", "24", "28"], answer="16", trap_answer="24",
        trap_path="원문처럼 f(2)=10±12 로 두어 24 (아래 제한이 −2 라 f(2)≤10+4).",
        explanation=[
            r"평균값 정리에서 $f(4)-f(2)=2f'(c)$인 $c\in(2,4)$가 있다.",
            r"$-2\le f'(c)\le6$이므로 $-4\le10-f(2)\le12$, 즉 $-2\le f(2)\le14$이다.",
            r"함정: 제한이 대칭이 아니므로 폭이 다르다. $f=6x-14$, $f=-2x+18$에서 양 끝이 실제로 된다.",
            r"$M-m=14-(-2)=16$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (상한 6 → 5)",
        changed=["|f'(x)|≤6 → |f'(x)|≤5"], naturalness="",
        stem=HEAD, box=box(r"|f'(x)|\le5"), choices=["16", "18", "20", "22", "24"], answer="20", trap_answer=None, trap_path=None,
        explanation=[
            r"평균값 정리에서 $|f(4)-f(2)|=2|f'(c)|\le10$이다.",
            r"$0\le f(2)\le20$이고 $f=\pm5(x-4)+10$에서 등호가 성립한다.",
            r"$M-m=20$이다.",
        ],
    ),
]


def spread(L, U):
    # 범위: f(2)=f(4)−2f'(c), f'(c)∈[L,U]; 끝값은 일차함수 f=s(x−4)+10 (s=L,U) 에서 달성
    vals = []
    for s in (L, U):
        f = s*(x - 4) + 10
        assert all(L <= diff(f, x) <= U for _ in [0])
        vals.append(f.subs(x, 2))
    # 평균값 정리 한계 확인: 임의 c 에 대해 f(2) ∈ [10−2U, 10−2L]
    assert set(vals) == {10 - 2*U, 10 - 2*L}
    return max(vals) - min(vals)


def verify(c):
    c.ans('orig', spread(-6, 6))
    c.ans(1, spread(-2, 6))
    c.trap(1, spread(-6, 6))
    c.ans(2, spread(-5, 5))
