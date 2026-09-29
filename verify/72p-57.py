from lib import *
from fractions import Fraction as Fr

def hdef(blocks):
    return r"h(x)=\begin{cases}" + r" \\ ".join(f"{e} & ({a}\\le x<{b})" if i < len(blocks) - 1 else f"{e} & ({a}\\le x\\le {b})" for i, (e, a, b) in enumerate(blocks)) + r"\end{cases}"

def stem(blocks, end):
    return (r"좌표평면 위의 영역 $\{(x,\,y)\,|\,0\le x\le " + str(end) + r",\ 0\le y\le h(x)\}$ (단, $" + hdef(blocks) + r"$)과 네 점 $(0,\,0)$, $(t,\,0)$, $(t,\,t)$, $(0,\,t)$를 꼭짓점으로 하는 정사각형이 겹치는 부분의 넓이를 $f(t)$라 하자. "
            r"열린구간 $(0,\," + str(end) + r")$에서 함수 $f(t)$가 미분가능하지 않은 모든 $t$의 값의 합은?")

B0 = [("1", 0, 1), ("x", 1, 2), ("2", 2, 3), ("3", 3, 4)]
B1 = [("2", 0, 1), ("x", 1, 2), ("2", 2, 3), ("3", 3, 4)]
B2 = B0 + [("4", 4, 5)]

ORIG = dict(
    id="72p-57", chapter=3, page=72, num=57, source="2014학년도 수능 예시문항 A형 21번", type="객관식",
    stem=stem(B0, 4), choices=["2", "3", "4", "5", "6"], answer="4",
    general="f'(t)= (오른쪽 변 x=t 위 겹친 길이 min(h(t),t)) + (윗변 y=t 위 겹친 길이 |{x<t : h(x)>t}|). t<1: 2t, 1<t<2: t, 2<t<3: 2, 3<t<4: 3 → 1 에서 2→1, 3 에서 2→3 으로 끊김, 2 에서는 2→2 로 이어짐. 합 4.",
    special="① 도형이 꺾이는 x=2 에서 f 는 미분가능 (min(h,t) 가 연속). ② 앞쪽 높이가 t 보다 크면 윗변 쪽 기여가 생겨 끊기는 점이 '높이 = t' 로 옮겨감.",
    perspective="f' = 두 변 위의 겹친 길이 합, 끊김만 찾기.",
    table=[
        ("[0,1] 높이 1 (t 보다 작아짐)", "앞 높이 > t (윗변 기여)", "[0,1] 높이 2 면 끊김 {2, 3} → 5"),
        ("도형 x≤4", "—", "[4,5] 높이 4 를 덧붙이고 (0,5) 면 {1,3,4} → 8 (생존)"),
    ],
    sweep=["끊김 후보: h 의 불연속·꺾임 점, t=높이 값"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (앞 높이가 t 보다 크면 윗변 기여)",
        changed=["0≤x<1 의 높이 1 → 2"], naturalness="",
        stem=stem(B1, 4), choices=["2", "3", "4", "5", "6"], answer="5", trap_answer="4",
        trap_path="원문처럼 x=1 (높이가 바뀌는 곳)과 x=3 에서 끊긴다고 보아 1+3=4 (높이 2 의 첫 칸은 t<2 이면 윗변까지 덮어 x=1 에서 이어지고, t=2 에서 끊김).",
        explanation=[
            r"$f'(t)$는 정사각형의 오른쪽 변과 윗변 위에서 도형과 겹친 길이의 합이다.",
            r"$0<t<1$: $2t$, $1<t<2$: 첫 칸이 윗변을 덮어 $1+t$이므로 $t=1$에서 이어진다.",
            r"함정: $2<t<3$이면 첫 칸 높이 $2<t$라 윗변 기여가 사라져 $f'=2$, $t=2$에서 $3\to2$로 끊긴다.",
            r"$3<t<4$: $f'=3$이므로 $t=3$에서도 끊긴다. 합은 $2+3=5$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 ([4,5] 높이 4 추가, 구간 (0,5))",
        changed=["도형에 4≤x≤5, 높이 4 칸 추가", "구간 (0,4) → (0,5)"],
        naturalness="칸을 덧붙이면 정의역 끝이 5 가 되므로 구간을 함께 늘린 것.",
        stem=stem(B2, 5), choices=["4", "5", "6", "7", "8"], answer="8", trap_answer=None, trap_path=None,
        explanation=[
            r"원문과 같이 $f'$은 $0<t<1$에서 $2t$, $1<t<2$에서 $t$, $2<t<3$에서 $2$, $3<t<4$에서 $3$이다.",
            r"$4<t<5$에서 $f'=4$이므로 $t=4$에서도 $3\to4$로 끊긴다.",
            r"끊기는 점은 $1$, $3$, $4$이고 합은 $8$이다.",
        ],
    ),
]


def to_lin(blocks):
    H = []
    for e, a, b in blocks:
        H.append((1, 0, a, b) if e == "x" else (0, int(e), a, b))
    return H


def seg(m, k, a, b, t):
    if b <= a:
        return Fr(0)
    ha, hb = m*a + k, m*b + k
    if ha <= t and hb <= t:
        return (ha + hb)*(b - a)/2
    if ha >= t and hb >= t:
        return t*(b - a)
    cpt = Fr(t - k)/m
    return seg(m, k, a, cpt, t) + seg(m, k, cpt, b, t)


def F(H, t):
    return sum(seg(m, k, a, min(b, t), t) for m, k, a, b in H if a < t)


def nondiff(blocks, end):
    """정확한 유리수 넓이로 좌·우 차분몫 비교 (f 는 조각별 2차라 ε 오차 O(ε)); 격자 1/60 은 모든 후보(정수)를 포함"""
    H = to_lin(blocks)
    eps = Fr(1, 10**6)
    out = []
    for i in range(1, 60*end):
        t = Fr(i, 60)
        L = (F(H, t) - F(H, t - eps))/eps
        R = (F(H, t + eps) - F(H, t))/eps
        if abs(L - R) > Fr(1, 1000):
            out.append(t)
    return out


def verify(c):
    v = nondiff(B0, 4)
    c.check("원문: {1,3}", v == [1, 3])
    c.ans('orig', Integer(sum(v)))
    v = nondiff(B1, 4)
    c.check("1: {2,3}", v == [2, 3])
    c.ans(1, Integer(sum(v)))
    c.trap(1, Integer(1 + 3))
    v = nondiff(B2, 5)
    c.check("2: {1,3,4}", v == [1, 3, 4])
    c.ans(2, Integer(sum(v)))
