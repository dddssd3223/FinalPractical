from lib import *

def stem(P):
    return (r"좌표평면 위의 점 $\mathrm P" + P + r"$를 중심으로 하고 반지름의 길이가 $r\,(r>0)$인 원 $C$와 실수 $m$에 대하여 원 $C$와 직선 $y=mx$가 만나는 점의 개수를 $f(m)$이라 하자. <보기>에서 옳은 것만을 있는 대로 고른 것은?")

def bogi(s):
    return [r"ㄱ. $f(1)=1$이면 $r=\frac{\sqrt2}{2}$이다.", r"ㄴ. $r>5$이면 모든 실수 $m$에 대하여 $f(m)=2$이다.",
            r"ㄷ. 함수 $f(m)$이 $m=k$에서 불연속인 실수 $k$의 개수가 $1$이 되도록 하는 모든 $r$의 값의 합은 $" + s + r"$이다."]

CH = ["ㄱ", "ㄷ", "ㄱ,ㄴ", "ㄴ,ㄷ", "ㄱ,ㄴ,ㄷ"]
ORIG = dict(
    id="39p-27", chapter=2, page=39, num=27, source="2024년 수능완성 [24054-0103]", type="객관식",
    stem=stem(r"(3,\,4)"), bogi=bogi("8"), choices=CH, answer="ㄱ,ㄴ,ㄷ",
    general="d(m)=|3m−4|/√(m²+1). ㄱ: d(1)=1/√2=r ✓. ㄴ: d≤OP=5 (m=−3/4 에서 최대) → r>5 이면 항상 2 ✓. ㄷ: f 는 d(m)=r 인 m 에서만 불연속. (3m−4)²=r²(m²+1) 의 실근 개수가 1 ⇔ 이차항 계수 9−r²=0 (r=3, 수직선이 빠져 한 근) 또는 판별식 0 (r=5) → 합 8 ✓.",
    special="① r=3 을 놓침 — m→±∞ 에서 d→3 이지만 수직선 x=0 은 y=mx 꼴이 아니라서 d=3 인 m 이 하나뿐. 이 부분을 놓치면 합을 5 로 착각.",
    perspective="(3m−4)²−r²(m²+1)=0 의 m 에 대한 근 개수(차수 하락 포함).",
    table=[
        ("직선 y=mx (수직선 제외)", "수직선 x=0 과의 접함", "ㄷ 의 합을 5 로 제시하면 r=3 을 놓친 풀이가 '참'으로 오판"),
        ("중심 (3,4)", "—", "(4,3) 이면 점근값 4 → 합 9 (생존)"),
    ],
    sweep=["9−r²=0 (r=3): 이차식 → 일차식", "판별식 0 ⇔ r=5 (또는 0)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (수직선이 빠져 r=3 에서 근이 하나)",
        changed=["ㄷ 의 합 8 → 5"], naturalness="",
        stem=stem(r"(3,\,4)"), bogi=bogi("5"), choices=CH, answer="ㄱ,ㄴ", trap_answer="ㄱ,ㄴ,ㄷ",
        trap_path="판별식 0 인 r=5 만 세어 ㄷ 을 참으로 판단 (r=3 에서 이차항 계수가 0 이 되어 근이 하나인 경우 누락).",
        explanation=[
            r"점 P와 직선 $mx-y=0$ 사이의 거리는 $d(m)=\dfrac{|3m-4|}{\sqrt{m^2+1}}$이다. ㄱ: $d(1)=\frac1{\sqrt2}=r$이므로 참.",
            r"ㄴ: $d(m)\le\overline{\mathrm{OP}}=5$이므로 $r>5$이면 항상 두 점에서 만난다. 참.",
            r"ㄷ: $f$는 $d(m)=r$인 $m$에서만 불연속이고, $(3m-4)^2=r^2(m^2+1)$의 실근이 하나인 경우는 판별식이 $0$인 $r=5$와, 이차항 계수 $9-r^2=0$인 $r=3$이다.",
            r"함정: $r=3$이면 $y$축(수직선)이 접선이지만 $y=mx$ 꼴이 아니므로 근이 하나만 남는다. 합은 $8$이므로 ㄷ은 거짓이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (중심 (3,4) → (4,3))",
        changed=["중심 (3,4) → (4,3)", "ㄷ 의 합 8 → 9"], naturalness="중심을 옮기면 점근값이 4 로 바뀌므로 ㄷ 의 수치를 같은 구조로 맞춘 것.",
        stem=stem(r"(4,\,3)"), bogi=bogi("9"), choices=CH, answer="ㄱ,ㄴ,ㄷ", trap_answer=None, trap_path=None,
        explanation=[
            r"$d(m)=\dfrac{|4m-3|}{\sqrt{m^2+1}}$이다. ㄱ: $d(1)=\frac1{\sqrt2}$이므로 참.",
            r"ㄴ: $d(m)\le\overline{\mathrm{OP}}=5$이므로 참.",
            r"ㄷ: $(4m-3)^2=r^2(m^2+1)$의 실근이 하나 ⇔ $16-r^2=0$ ($r=4$) 또는 판별식 $0$ ($r=5$). 합 $9$이므로 참.",
        ],
    ),
]


def analyse(px, py, claimed_sum):
    m = Symbol('m', real=True)
    r = Symbol('r', positive=True)
    d = Abs(px*m - py)/sqrt(m**2 + 1)
    s1 = solve(Eq(d.subs(m, 1), r), r)
    t1 = s1 == [sqrt(2)/2]
    # ㄴ: d 의 최댓값 = OP
    dmax = sqrt(px**2 + py**2)
    t2 = all(d.subs(m, mv) <= dmax for mv in [Rational(k, 7) for k in range(-70, 71)]) and simplify(d.subs(m, -Rational(px, py)) - dmax) == 0
    # ㄷ: (px m − py)² − r²(m²+1) 의 실근 개수가 1 인 r
    Q = expand((px*m - py)**2 - r**2*(m**2 + 1))
    rs = set()
    lead = Poly(Q, m).coeff_monomial(m**2)
    rs |= {v for v in solve(lead, r)}
    rs |= {v for v in solve(discriminant(Q, m), r) if v > 0}
    # 각 r 에서 실제 근 개수 확인
    rs = {v for v in rs if len(set(solve(Q.subs(r, v), m))) == 1}
    t3 = simplify(sum(rs) - claimed_sum) == 0
    return {"ㄱ": t1, "ㄴ": t2, "ㄷ": t3}, rs


def verify(c):
    st, rs = analyse(3, 4, 8)
    c.check("원문: 근이 하나인 r = {3, 5}", rs == {3, 5})
    c.ans('orig', bogi_eval(st))
    st, rs = analyse(3, 4, 5)
    c.ans(1, bogi_eval(st))
    c.trap(1, bogi_eval({"ㄱ": True, "ㄴ": True, "ㄷ": True}))
    st, rs = analyse(4, 3, 9)
    c.check("2: r = {4, 5}", rs == {4, 5})
    c.ans(2, bogi_eval(st))
