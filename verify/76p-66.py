from lib import *

def stem(mid, right):
    return (r"함수 $f(x)=\begin{cases}-x & (x\le0) \\ " + mid + r" & (0<x\le2) \\ " + right + r" & (x>2)\end{cases}$와 상수가 아닌 다항식 $p(x)$에 대하여 <보기>에서 옳은 것만을 있는 대로 고른 것은?")

BOGI = [r"ㄱ. 함수 $p(x)f(x)$가 실수 전체의 집합에서 연속이면 $p(0)=0$이다.",
        r"ㄴ. 함수 $p(x)f(x)$가 실수 전체의 집합에서 미분가능하면 $p(2)=0$이다.",
        r"ㄷ. 함수 $p(x)\{f(x)\}^2$이 실수 전체의 집합에서 미분가능하면 $p(x)$는 $x^2(x-2)^2$으로 나누어떨어진다."]
CH = ["ㄱ", "ㄱ,ㄴ", "ㄱ,ㄷ", "ㄴ,ㄷ", "ㄱ,ㄴ,ㄷ"]

ORIG = dict(
    id="76p-66", chapter=3, page=76, num=66, source="2020학년도 수능 나형 20번", type="객관식",
    stem=stem("x-1", "2x-3"), bogi=BOGI, choices=CH, answer="ㄱ,ㄴ",
    general="x=0: f 가 0→−1 로 끊김 → pf 연속이면 p(0)=0 (ㄱ 참). x=2: f 연속, 기울기 1→2 → (pf)' 비교로 p(2)=0 (ㄴ 참). f²: x=0 에서 끊김+오른쪽 (x−1)² → p(0)=p'(0)=0; x=2 는 연속·꺾임 → p(2)=0 만 → (x−2)² 불필요 (ㄷ 거짓).",
    special="① x=2 에서 f 가 연속이라 조건이 p(2)=0 하나. 끊겨 있으면 p(2)=p'(2)=0 (중근).",
    perspective="끊김 → 근 + 도함수 근, 꺾임 → 근.",
    table=[
        ("x=2 에서 f 연속", "x=2 에서 끊김", "오른쪽 2x−2 면 ㄷ 참 → ㄱ,ㄴ,ㄷ"),
        ("x=0 에서 끊김", "—", "가운데 x, 오른쪽 2x−2 (0 연속·꺾임) 면 ㄴ 만 (생존)"),
    ],
    sweep=["경계마다: 끊김 → p=p'=0, 꺾임(값≠0) → p=0"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (x=2 에서 끊기면 중근 필요)",
        changed=["x>2 조각 2x−3 → 2x−2"], naturalness="",
        stem=stem("x-1", "2x-2"), bogi=BOGI, choices=CH, answer="ㄱ,ㄴ,ㄷ", trap_answer="ㄱ,ㄴ",
        trap_path="원문처럼 x=2 를 연속인 꺾임으로 보아 ㄷ 에서 p(2)=0 만 → ㄷ 거짓 (실제로는 f(2)=1, f(2+)=2 로 끊김).",
        explanation=[
            r"ㄱ: $x=0$에서 $f$가 $0$에서 $-1$로 끊기므로 $p(0)=-p(0)$, $p(0)=0$ (참).",
            r"ㄴ: 함정: $x=2$에서 $f(2)=1$, $\lim_{x\to2+}f=2$로 끊기므로 연속에서 $p(2)=0$, 미분가능에서 $p'(2)=2p'(2)$, $p'(2)=0$이다. 특히 $p(2)=0$ (참).",
            r"ㄷ: $x=0$에서 $p(0)=p'(0)=0$, $x=2$에서도 $\{f\}^2$이 $1\to4$로 끊기므로 $p(2)=p'(2)=0$이다.",
            r"따라서 $p$는 $x^2(x-2)^2$으로 나누어떨어진다 (참). 답은 ㄱ, ㄴ, ㄷ이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (x=0 에서 연속으로)",
        changed=["0<x≤2 조각 x−1 → x", "x>2 조각 2x−3 → 2x−2"],
        naturalness="가운데 조각을 올려 x=0 에서 연속으로 만들면서 x=2 에서도 연속이 유지되도록 오른쪽 조각을 함께 맞춘 것.",
        stem=stem("x", "2x-2"), bogi=BOGI, choices=["ㄱ", "ㄴ", "ㄱ,ㄴ", "ㄴ,ㄷ", "ㄱ,ㄴ,ㄷ"], answer="ㄴ", trap_answer=None, trap_path=None,
        explanation=[
            r"ㄱ: $f$가 실수 전체에서 연속이므로 $p(0)$과 관계없이 $pf$는 연속이다 (거짓).",
            r"ㄴ: $x=2$에서 기울기가 $1\to2$로 꺾이고 $f(2)=2\ne0$이므로 $p(2)=0$ (참).",
            r"ㄷ: $\{f\}^2$은 $x=0$ 근처에서 $x^2$이라 매끄럽고, $x=2$에서는 $p(2)=0$만 필요하다 (거짓). 답은 ㄴ이다.",
        ],
    ),
]


def truths(mid, right):
    cs = symbols('c0:7')
    p = sum(ci*x**i for i, ci in enumerate(cs))
    P = [(-x, -oo, 0), (mid, 0, 2), (right, 2, oo)]

    def conds(fun, deriv):
        Q = [(expand(p*fun(e)), lo, hi) for e, lo, hi in P]
        eqs = []
        for t in (0, 2):
            eqs.append(piece_at(Q, t, '-').subs(x, t) - piece_at(Q, t, '+').subs(x, t))
            if deriv:
                eqs.append(plim(Q, lambda e: diff(e, x), t, '-') - plim(Q, lambda e: diff(e, x), t, '+'))
        eqs = [e for e in (expand(e) for e in eqs) if e != 0]
        if not eqs:
            return p
        s = solve(eqs, cs, dict=True)
        assert len(s) == 1
        return p.subs(s[0])

    p1 = conds(lambda e: e, False)
    p2 = conds(lambda e: e, True)
    p3 = conds(lambda e: e**2, True)
    # 해 공간에 상수 아닌 다항식이 존재하는지도 확인
    assert all(q.free_symbols - {x} for q in (p1, p2, p3))
    return {"ㄱ": simplify(p1.subs(x, 0)) == 0,
            "ㄴ": simplify(p2.subs(x, 2)) == 0,
            "ㄷ": rem(Poly(p3, x), Poly(x**2*(x - 2)**2, x)).is_zero}


def verify(c):
    c.ans('orig', bogi_eval(truths(x - 1, 2*x - 3)))
    c.ans(1, bogi_eval(truths(x - 1, 2*x - 2)))
    c.trap(1, bogi_eval(truths(x - 1, 2*x - 3)))
    c.ans(2, bogi_eval(truths(x, 2*x - 2)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
