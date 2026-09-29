from lib import *

def stem(cond, r, ask):
    return (cond + r" 함수 $f(x)=\begin{cases}x+a & (x<-1)\\ x & (-1\le x<3)\\ " + r + r" & (x\ge3)\end{cases}$이다. 함수 $|f(x)|$가 실수 전체의 집합에서 연속일 때, " + ask)

ORIG = dict(
    id="32p-1", chapter=2, page=32, num=1, source="2023학년도 대수능 6월 모의평가 6번", type="객관식",
    stem=stem(r"두 양수 $a$, $b$에 대하여", "bx-2", r"$a+b$의 값은? [3점]"),
    choices=["7/3", "8/3", "3", "10/3", "11/3"], answer="11/3",
    general="x=−1: |a−1|=|−1| → a=2 또는 0 → a>0 이라 2. x=3: |3|=|3b−2| → b=5/3 또는 −1/3 → b>0 이라 5/3. a+b=11/3.",
    special="① 절댓값 방정식의 두 근 중 '양수' 조건으로 하나씩만 남는 구조 — 조건이 없거나 두 근이 모두 양수면 여러 쌍.",
    perspective="|f| 연속 ⇔ 경계에서 좌·우 값이 같거나 부호만 반대.",
    table=[
        ("a>0", "a=0 (x<−1 에서 f=x)", "a 를 실수로 풀면 a=0 도 가능 → 두 쌍"),
        ("오른쪽 조각 bx−2", "두 근이 모두 양수인 경우", "bx−4 이면 b=7/3, 1/3 모두 양수"),
    ],
    sweep=["|a−1|=1 의 근 0, 2", "|3b−c|=3 의 두 근의 부호"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (a 의 부호 조건이 없으면 a=0 도 가능)",
        changed=["'두 양수 a, b' → '실수 a 와 양수 b'", "묻는 값 → 가능한 a+b 의 값의 합"],
        naturalness="a 의 부호 조건을 풀면 쌍이 둘이 되어 '값의 합'으로 묻는 것은 필수.",
        stem=stem(r"실수 $a$와 양수 $b$에 대하여", "bx-2", r"$a+b$의 값이 될 수 있는 모든 값의 합은?"),
        choices=["5/3", "3", "11/3", "16/3", "17/3"], answer="16/3", trap_answer="11/3",
        trap_path="원문처럼 a=2 만 택해 11/3 (a=0 이어도 x<−1 에서 f=x, |f| 가 −1 에서 연속).",
        explanation=[
            r"$x=-1$에서 $|a-1|=|-1|=1$이므로 $a=2$ 또는 $a=0$이다.",
            r"$x=3$에서 $|3b-2|=3$이므로 $b=\frac53$ 또는 $-\frac13$이고 $b>0$이라 $b=\frac53$이다.",
            r"함정: $a$는 양수 조건이 없으므로 $a=0$도 가능하다.",
            r"$a+b$의 값은 $\frac53$, $\frac{11}3$이고 합은 $\frac{16}3$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 (두 근이 모두 양수)",
        changed=["오른쪽 조각 bx−2 → bx−4", "묻는 값 → a+b 의 최댓값"],
        naturalness="두 근이 모두 조건을 만족해 값이 둘이 되므로 '최댓값'으로 묻는 것은 필수.",
        stem=stem(r"두 양수 $a$, $b$에 대하여", "bx-4", r"$a+b$의 최댓값은?"),
        choices=["7/3", "3", "11/3", "13/3", "5"], answer="13/3", trap_answer="7/3",
        trap_path="|3b−4|=3 에서 한 근 b=1/3 만 택함 → 7/3 (b=7/3 도 양수).",
        explanation=[
            r"$x=-1$에서 $|a-1|=1$, $a>0$이므로 $a=2$이다.",
            r"$x=3$에서 $|3b-4|=3$이므로 $b=\frac73$ 또는 $b=\frac13$이다.",
            r"함정: 두 값이 모두 양수라 둘 다 가능하다.",
            r"$a+b$의 최댓값은 $2+\frac73=\frac{13}3$이다.",
        ],
    ),
]


def pairs(cst, a_pos):
    a, b = symbols('a b', real=True)
    out = set()
    for av in solve(Eq(Abs(-1 + a), Abs(-1)), a):
        if a_pos and not av > 0:
            continue
        for bv in solve(Eq(Abs(3), Abs(3*b - cst)), b):
            if bv > 0:
                P = [(x + av, -oo, -1), (x, -1, 3), (bv*x - cst, 3, oo)]
                val = lambda v: (x + av if v < -1 else x if v < 3 else bv*x - cst).subs(x, v)
                ok = all(plim_exists(P, lambda e: Abs(e), pt)[0] and simplify(plim(P, lambda e: Abs(e), pt, '-') - Abs(val(pt))) == 0 for pt in (-1, 3))
                if ok:
                    out.add((av, bv))
    return out


def verify(c):
    p = pairs(2, True)
    c.check("원문: (2, 5/3)", p == {(2, Rational(5, 3))})
    c.ans('orig', sum(p.pop()))
    p = pairs(2, False)
    c.check("1: (0,5/3), (2,5/3)", p == {(0, Rational(5, 3)), (2, Rational(5, 3))})
    c.ans(1, sum(a + b for a, b in p))
    c.trap(1, Rational(11, 3))
    p = pairs(4, True)
    c.check("2: (2,7/3), (2,1/3)", p == {(2, Rational(7, 3)), (2, Rational(1, 3))})
    c.ans(2, max(a + b for a, b in p))
    c.trap(2, min(a + b for a, b in p))
