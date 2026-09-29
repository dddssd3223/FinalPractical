from lib import *
import random

BOGI = [r"ㄱ. $f(-2)=f(2)$", r"ㄴ. 함수 $f(x)$의 최댓값과 최솟값의 합은 $0$이다.", r"ㄷ. 방정식 $f(x)=0$의 서로 다른 실근의 개수는 적어도 $12$이다."]
CH = ["ㄱ", "ㄷ", "ㄱ,ㄴ", "ㄴ,ㄷ", "ㄱ,ㄴ,ㄷ"]

def stem(ga, nr):
    return (r"$-12\le x\le12$에서 정의되고 연속인 함수 $f(x)$가 다음 조건을 만족시킨다. <보기>에서 옳은 것만을 있는 대로 고른 것은?")

def box(ga, nr):
    return [r"(가) $-2\le x\le2$에서 $f(x)=3$과 $f(x)=-3$을 만족시키는 $x$의 값은 각각 " + ga + r" 있다.",
            r"(나) " + nr + r"인 모든 실수 $x$에 대하여 $f(x)=f(x+4)$이다."]

ORIG = dict(
    id="37p-22", chapter=2, page=37, num=22, source="2021년 수능완성 [21054-0134]", type="객관식",
    stem=stem("오직 한 개씩", r"-12\le x\le8"), box=box("오직 한 개씩", r"-12\le x\le8"), bogi=BOGI,
    choices=CH, answer="ㄱ,ㄴ,ㄷ",
    general="ㄱ: (나)에 x=−2 → f(−2)=f(2). ㄴ: [−2,2] 에서 3 보다 큰 값이 있으면 f(−2)=f(2) 와 사잇값 정리로 f=3 인 점이 둘 → 모순, 따라서 최댓값 3, 같은 이유로 최솟값 −3 (주기로 전체 구간도 같음). ㄷ: 한 주기(길이 4)에서 3 과 −3 사이를 오가므로 0 을 적어도 두 번 → 6 주기에서 12 개 이상.",
    special="① (나)가 정의역 전체([−12,12])를 주기 4 로 덮는 것 — 범위가 줄면 나머지 구간은 자유. ② (가)의 '오직 한 개씩' 이 최댓값·최솟값을 ±3 으로 묶음.",
    perspective="주기 구간이 덮는 범위 × 한 주기 안의 사잇값 정리.",
    table=[
        ("(나) −12≤x≤8 (전체 덮음)", "주기가 일부 구간에만 성립", "−12≤x≤4 로 줄이면 [8,12] 가 자유 → ㄴ, ㄷ 거짓"),
        ("(가) 오직 한 개씩", "값 3 을 여러 번 갖는 경우", "'적어도 한 개씩'이면 최댓값이 3 보다 클 수 있음 → ㄴ 거짓"),
    ],
    sweep=["(나)가 덮는 구간 길이 = 주기 수", "f=±3 의 해 개수 조건"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (주기 조건이 정의역 일부만 덮음)",
        changed=["(나) −12≤x≤8 → −12≤x≤4"], naturalness="",
        stem=stem("오직 한 개씩", r"-12\le x\le4"), box=box("오직 한 개씩", r"-12\le x\le4"), bogi=BOGI,
        choices=CH, answer="ㄱ", trap_answer="ㄱ,ㄴ,ㄷ",
        trap_path="원문처럼 [−12,12] 전체가 주기 4 로 덮인다고 보아 ㄱ,ㄴ,ㄷ.",
        explanation=[
            r"ㄱ. $x=-2$는 $-12\le x\le4$에 속하므로 $f(-2)=f(2)$로 참이다.",
            r"(나)는 $f$를 $[-12,\,8]$에서만 주기 $4$로 묶고, $8<x\le12$에서는 연속이기만 하면 된다.",
            r"함정: 원문과 달리 $[8,\,12]$에서 $f$가 $3$보다 큰 값을 가질 수 있으므로 ㄴ은 거짓이다.",
            r"ㄷ. $[-12,\,8]$의 5주기에서 보장되는 실근은 $10$개이고 $[8,12]$에서 $f>0$일 수 있으므로 거짓이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 ('오직 한 개'가 최댓값·최솟값을 묶던 역할)",
        changed=["(가) '오직 한 개씩' → '적어도 한 개씩'"], naturalness="",
        stem=stem("적어도 한 개씩", r"-12\le x\le8"), box=box("적어도 한 개씩", r"-12\le x\le8"), bogi=BOGI,
        choices=["ㄱ", "ㄴ", "ㄱ,ㄴ", "ㄱ,ㄷ", "ㄱ,ㄴ,ㄷ"], answer="ㄱ,ㄷ", trap_answer="ㄱ,ㄴ,ㄷ",
        trap_path="원문처럼 최댓값 3, 최솟값 −3 으로 보아 ㄴ 도 참으로 판단.",
        explanation=[
            r"ㄱ. (나)에 $x=-2$를 넣으면 $f(-2)=f(2)$로 참이다.",
            r"ㄴ. 함정: '적어도 한 개씩'이면 $f$가 $3$을 두 번 지나 $4$까지 올라갈 수 있으므로 최댓값과 최솟값의 합이 $0$이 아닐 수 있다. 거짓.",
            r"ㄷ. 한 주기에서 $f$는 $3$과 $-3$을 모두 가지므로 $0$을 적어도 두 번 지나고, $6$주기에서 $12$개 이상이다. 참.",
            r"따라서 ㄱ, ㄷ이다.",
        ],
    ),
]


# ── 구간별 일차(꺾은선) 함수로 조건·보기를 점검 ──
def pl_eval(pts, v):
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        if x0 <= v <= x1:
            return y0 + (y1 - y0)*(v - x0)/(x1 - x0)
    raise ValueError


def count_sol(pts, cval, lo, hi):
    """꺾은선의 f=c 해 개수 (평평한 구간이 c 이면 무한)"""
    sols = set()
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        a, b = max(x0, lo), min(x1, hi)
        if a > b:
            continue
        ya, yb = pl_eval(pts, a), pl_eval(pts, b)
        if ya == cval and yb == cval:
            return float('inf')
        if (ya - cval)*(yb - cval) <= 0 and ya != yb:
            sols.add(round(a + (cval - ya)*(b - a)/(yb - ya), 9))
    return len(sols)


def periodic_from(base, lo_p, hi_p, tail):
    """[−2,2] 모양 base 를 주기 4 로 [−12, hi_p+4] 에 반복, 이후 tail 점들 이어붙임"""
    pts = []
    for s in range(-12, hi_p + 4, 4):
        for bx, by in base:
            X = bx + 2 + s  # base 는 [−2,2] 기준 → [s, s+4]
            if not pts or X > pts[-1][0]:
                pts.append((X, by))
    return pts + [p for p in tail if p[0] > pts[-1][0]]


def check_conds(pts, ga_exact, per_hi):
    c3, cm3 = count_sol(pts, 3, -2, 2), count_sol(pts, -3, -2, 2)
    ok_ga = (c3 == 1 and cm3 == 1) if ga_exact else (c3 >= 1 and cm3 >= 1)
    grid = [Rational(k, 8) for k in range(-96, 8*per_hi + 1)]
    ok_na = all(abs(pl_eval(pts, v) - pl_eval(pts, v + 4)) < 1e-12 for v in grid)
    return ok_ga and ok_na and pts[0][0] <= -12 and pts[-1][0] >= 12


def statements(pts):
    ys = [y for X, y in pts if -12 <= X <= 12] + [pl_eval(pts, -12), pl_eval(pts, 12)]  # 꺾은선의 극값은 꼭짓점
    return {"ㄱ": pl_eval(pts, -2) == pl_eval(pts, 2),
            "ㄴ": max(ys) + min(ys) == 0,
            "ㄷ": count_sol(pts, 0, -12, 12) >= 12}


def verify(c):
    base = [(-2, 0), (-1, 3), (1, -3), (2, 0)]  # 한 주기 예시
    # 원문: 예시 + 무작위 꺾은선(조건 만족하는 것만)으로 ㄱㄴㄷ 모두 참 확인
    random.seed(1)
    ok_all = True
    for _ in range(30):
        m = Rational(random.randint(-20, 20), 10)
        p = Rational(random.randint(-19, -1), 10); q = Rational(random.randint(1, 19), 10)
        b = sorted([(-2, m), (p, 3), (q, -3), (2, m)]) if random.random() < .5 else [(-2, m), (p, -3), (q, 3), (2, m)]
        b = sorted(b)
        pts = periodic_from(b, -12, 8, [])
        if check_conds(pts, True, 8):
            ok_all &= all(statements(pts).values())
    c.check("원문: 조건을 만족하는 무작위 30개에서 ㄱㄴㄷ 모두 참", ok_all)
    pts = periodic_from(base, -12, 8, [])
    c.check("원문 예시가 조건 만족", check_conds(pts, True, 8))
    c.ans('orig', bogi_eval(statements(pts)))
    # 변형1: (나)가 −12≤x≤4 → [8,12] 자유. 반례: 8 이후 5 까지 올라가 양수 유지
    pts1 = periodic_from(base, -12, 4, [(9, 5), (12, 5)])
    c.check("1: 반례가 조건 만족", check_conds(pts1, True, 4))
    st = statements(pts1)
    c.check("1: 반례에서 ㄴ, ㄷ 거짓, ㄱ 참", st == {"ㄱ": True, "ㄴ": False, "ㄷ": False})
    c.ans(1, bogi_eval(st))
    c.trap(1, "ㄱ,ㄴ,ㄷ")
    # 변형2: 적어도 한 개씩 → 반례: 한 주기에서 3 을 두 번 지나 4 까지
    b2 = [(-2, 0), (-Rational(3, 2), 4), (-1, 2), (0, 3), (1, -3), (2, 0)]
    pts2 = periodic_from(b2, -12, 8, [])
    c.check("2: 반례가 조건 만족", check_conds(pts2, False, 8))
    st2 = statements(pts2)
    c.check("2: 반례에서 ㄴ 거짓, ㄱ ㄷ 참", st2 == {"ㄱ": True, "ㄴ": False, "ㄷ": True})
    c.ans(2, bogi_eval(st2))
    c.trap(2, "ㄱ,ㄴ,ㄷ")
