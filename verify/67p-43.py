from lib import *

def box(pt, cond):
    return [r"(가) 임의의 두 실수 $x_1$, $x_2\,(x_1<x_2)$에 대하여 $x$의 값이 $x_1$에서 $x_2$까지 변할 때의 함수 $y=f(x)$의 평균변화율은 $2$로 일정하다.",
            r"(나) 두 함수 $y=f(x)$, $y=g(x)$의 그래프는 점 $" + pt + r"$에서 만난다.",
            r"(다) 함수 $|f(x)-g(x)|$가 " + cond]

HEAD = r"함수 $f(x)$와 최고차항의 계수가 $1$인 삼차함수 $g(x)$가 다음 조건을 만족시킨다. "

ORIG = dict(
    id="67p-43", chapter=3, page=67, num=43, source="2022년 수능특강 [22009-0074]", type="주관식",
    stem=HEAD + r"$f(3)+g(3)$의 값을 구하시오.",
    box=box("(1,\\,3)", "실수 전체의 집합에서 미분가능하다."), answer="22",
    general="(가) → f=2x+b, (나) → f=2x+1. h=g−f 는 최고차1 삼차, h(1)=0. |h| 는 h 의 단순근에서 꺾임 → 모든 실근이 중복근 → h=(x−1)³. f(3)+g(3)=7+(7+8)=22.",
    special="① 삼차는 실근 중복도 합이 3 이라 '단순근 없음' → 삼중근. ② 미분불가 점이 하나 지정되면 그 점만 단순근, 1 은 중근.",
    perspective="|h| 의 꺾임 = h 의 홀수(1)중근.",
    table=[
        ("|f−g| 전체 미분가능 (단순근 없음)", "x=3 에서만 미분불가 (3 단순근, 1 중근)", "h=(x−1)²(x−3) → g(4)=18"),
        ("만나는 점 (1,3)", "—", "(2,5) 면 h=(x−2)³ → 15 (생존)"),
    ],
    sweep=["h 의 근 배치: 삼중근 / 중근+단순근"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (미분불가 점 지정 → 어느 근이 중근인지)",
        changed=["(다) 전체 미분가능 → x=3 에서만 미분가능하지 않음", "묻는 값 g(4)"],
        naturalness="(다)를 바꾸면 g(3)=f(3) 이 되어 원래 묻는 값이 조건에서 바로 나오므로 g(4) 를 묻는다.",
        stem=HEAD + r"$g(4)$의 값을 구하시오.",
        box=box("(1,\\,3)", r"$x=3$에서만 미분가능하지 않다."), answer="18", trap_answer="12",
        trap_path="미분불가 점 3 을 중근으로 잡아 h=(x−1)(x−3)² → g(4)=9+3=12 (실제로는 중근에서 미분가능, 단순근 1 에서 꺾임).",
        explanation=[
            r"(가)(나)에서 $f(x)=2x+1$이고 $h(x)=g(x)-f(x)$는 최고차항 계수 $1$인 삼차식, $h(1)=0$이다.",
            r"$|h(x)|$는 $h$의 단순근에서만 미분가능하지 않으므로 $3$은 단순근이고 다른 실근은 중근이어야 한다.",
            r"함정: 미분불가능한 점이 단순근이다. 따라서 $1$이 중근, $h(x)=(x-1)^2(x-3)$이다.",
            r"$g(4)=f(4)+h(4)=9+9=18$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (만나는 점 (1,3) → (2,5))",
        changed=["(나) 점 (1,3) → (2,5)"], naturalness="",
        stem=HEAD + r"$f(3)+g(3)$의 값을 구하시오.",
        box=box("(2,\\,5)", "실수 전체의 집합에서 미분가능하다."), answer="15", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)=2x+b$가 $(2,5)$를 지나므로 $f(x)=2x+1$이다.",
            r"$h=g-f$는 단순근이 없어야 하므로 $h(x)=(x-2)^3$이다.",
            r"$f(3)+g(3)=7+(7+1)=15$이다.",
        ],
    ),
]


def nondiff(h):
    """|h| 가 미분가능하지 않은 점 = h 의 실근 중 h'≠0 인 것"""
    return {r for r in set(Poly(h, x).real_roots()) if diff(h, x).subs(x, r) != 0}


def candidates(p0, want_nd):
    """f=2x+b 가 p0 지남, h=g−f=(x−x0)(x²+ux+v): |h| 미분불가 점 집합 == want_nd 인 h (정수 격자 탐색 + 구조 확인)"""
    x0, y0 = p0
    b = y0 - 2*x0
    f = 2*x + b
    out = set()
    # h=(x−x0)(x−r)(x−s) (실근) 또는 (x−x0)·(허근 이차) — 후자는 x0 단순근이라 미분불가점 {x0}
    for r in range(-6, 7):
        for s in range(r, 7):
            h = expand((x - x0)*(x - r)*(x - s))
            if nondiff(h) == set(want_nd):
                out.add((f, h))
    if set(want_nd) == {x0}:
        out.add('complex')
    return out


def verify(c):
    s = candidates((1, 3), set())
    c.check("원문: h=(x−1)³ 유일", s == {(2*x + 1, expand((x - 1)**3))})
    f, h = list(s)[0]
    c.ans('orig', f.subs(x, 3) + (f + h).subs(x, 3))
    s = candidates((1, 3), {3})
    c.check("1: h=(x−1)²(x−3) 유일", s == {(2*x + 1, expand((x - 1)**2*(x - 3)))})
    f, h = list(s)[0]
    c.ans(1, (f + h).subs(x, 4))
    c.trap(1, (f + (x - 1)*(x - 3)**2).subs(x, 4))
    s = candidates((2, 5), set())
    c.check("2: 유일", len(s) == 1)
    f, h = list(s)[0]
    c.ans(2, f.subs(x, 3) + (f + h).subs(x, 3))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
