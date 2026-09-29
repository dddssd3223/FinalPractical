from lib import *

def stem(ineq):
    return (r"최고차항의 계수가 $a$인 이차함수 $f(x)$가 모든 실수 $x$에 대하여 $" + ineq + r"$를 만족시킨다. 함수 $y=f(x)$의 그래프의 대칭축이 직선 $x=1$일 때, 실수 $a$의 최댓값은?")

ORIG = dict(
    id="74p-62", chapter=3, page=74, num=62, source="2021학년도 수능 9월 모의평가 나형 18번", type="객관식",
    stem=stem(r"|f'(x)|\le 4x^2+5"), choices=["3/2", "2", "5/2", "3", "7/2"], answer="2",
    general="f'=2a(x−1). 4x²+5∓2a(x−1)≥0 두 개: 판별식 → a²−8a−20≤0 (−2≤a≤10), a²+8a−20≤0 (−10≤a≤2). 공통 −2≤a≤2 → 최댓값 2.",
    special="① 절댓값이라 위·아래 두 부등식 — a>0 에서 막는 쪽은 f'≥−(4x²+5) (x<1 쪽).",
    perspective="이차부등식 항상 성립 → 판별식.",
    table=[
        ("절댓값 (양쪽 제한)", "한쪽만 f'≤4x²+5", "절댓값 없으면 −2≤a≤10 → 10"),
        ("상수 5", "—", "12 면 −4≤a≤4 → 4 (생존)"),
    ],
    sweep=["a²∓8a−4c≤0 (c: 상수항)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (절댓값이 없으면 막는 부등식이 바뀜)",
        changed=["|f'(x)| ≤ 4x²+5 → f'(x) ≤ 4x²+5"], naturalness="",
        stem=stem(r"f'(x)\le 4x^2+5"), choices=["2", "4", "6", "8", "10"], answer="10", trap_answer="2",
        trap_path="원문처럼 −(4x²+5)≤f' 쪽 조건까지 적용해 2 (절댓값이 없어 그 조건은 필요 없음).",
        explanation=[
            r"대칭축이 $x=1$이므로 $f'(x)=2a(x-1)$이다.",
            r"$4x^2+5-2a(x-1)=4x^2-2ax+2a+5\ge0$이 항상 성립해야 하므로 $\frac D4=a^2-4(2a+5)\le0$이다.",
            r"함정: 아래쪽 제한 $f'\ge-(4x^2+5)$은 없으므로 이 조건 하나만 쓴다.",
            r"$a^2-8a-20\le0$에서 $-2\le a\le10$이므로 최댓값은 $10$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (상수 5 → 12)",
        changed=["4x²+5 → 4x²+12"], naturalness="",
        stem=stem(r"|f'(x)|\le 4x^2+12"), choices=["3", "7/2", "4", "9/2", "5"], answer="4", trap_answer=None, trap_path=None,
        explanation=[
            r"$f'(x)=2a(x-1)$이고 $4x^2+12\mp2a(x-1)\ge0$이 항상 성립해야 한다.",
            r"판별식에서 $a^2-8a-48\le0$ ($-4\le a\le12$), $a^2+8a-48\le0$ ($-12\le a\le4$)이다.",
            r"공통 범위 $-4\le a\le4$에서 최댓값은 $4$이다.",
        ],
    ),
]


def amax(B, both):
    a = Symbol('a', real=True)
    fp = 2*a*(x - 1)
    conds = [B - fp] + ([B + fp] if both else [])
    ineqs = []
    for g in conds:
        P = Poly(g, x)
        assert P.LC() > 0
        A2, A1, A0 = P.all_coeffs()
        ineqs.append(A1**2 - 4*A2*A0 <= 0)
    S = reduce_inequalities(ineqs, a)
    I = S.as_set()
    return I.sup, I


def verify(c):
    m, I = amax(4*x**2 + 5, True)
    c.check("원문: 구간 [−2,2]", I == Interval(-2, 2))
    c.ans('orig', m)
    m, I = amax(4*x**2 + 5, False)
    c.check("1: 구간 [−2,10]", I == Interval(-2, 10))
    c.ans(1, m)
    c.trap(1, amax(4*x**2 + 5, True)[0])
    m, I = amax(4*x**2 + 12, True)
    c.ans(2, m)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='12', trap_path="f'(x)≤4x²+12 한쪽만 써서 −4≤a≤12 → 12 (절댓값이라 f'≥−(4x²+12) 도 필요).")
VARS[1]['choices'] = ['2', '4', '6', '8', '12']
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, amax(4*x**2 + 12, False)[0])

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '생존형: 원문 풀이가 그대로 통하고 함정이 계산 실수 수준'
