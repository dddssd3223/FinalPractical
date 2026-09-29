from lib import *
from itertools import product

def stem(eq, cond, pts):
    return r"실수 전체의 집합에서 연속인 함수 $f(x)$가 모든 실수 $x$에 대하여 $" + eq + r"=0$을 만족시킨다. " + cond + r" $" + pts + r"$의 값은?"

ORIG = dict(
    id="36p-17", chapter=2, page=36, num=17, source="2022학년도 대수능 12번", type="객관식",
    stem=stem(r"\{f(x)\}^3-\{f(x)\}^2-x^2f(x)+x^2", r"함수 $f(x)$의 최댓값이 $1$이고 최솟값이 $0$일 때,", r"f\left(-\frac43\right)+f(0)+f\left(\frac12\right)"),
    choices=["1/2", "1", "3/2", "2", "5/2"], answer="3/2",
    general="(f−1)(f−x)(f+x)=0 → f(x)∈{1, x, −x}. 최댓값 1, 최솟값 0 → |x|>1 이면 f=1, 최솟값 0 을 위해 f(0)=0 → [−1,1] 에서 f=|x| (갈래를 바꿀 수 있는 곳은 갈래가 만나는 x=0, ±1 뿐). 1+0+½=3/2.",
    special="① |x|>1 에서 f=1 로 바로 둠 — 최댓값 1 조건 덕분. 최댓값 조건이 없으면 |x| 갈래도 가능. ② 갈래 전환점 ±1 은 1=±x 에서 나옴(계수가 바뀌면 전환점도 바뀜).",
    perspective="연속인 선택 함수는 갈래가 만나는 점에서만 갈래를 바꿀 수 있다.",
    table=[
        ("최댓값 1", "|x|>1 에서 |x| 갈래", "최댓값 조건을 빼면 바깥은 1 또는 |x| → 값이 여러 개"),
        ("x² (계수 1)", "전환점이 ±1 이 아닌 경우", "4x² 이면 전환점 ±½ (생존)"),
    ],
    sweep=["갈래가 만나는 점: 1=kx, 1=−kx, kx=−kx"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (최댓값 조건이 없으면 바깥 구간의 갈래가 둘)",
        changed=["'최댓값 1, 최솟값 0' → '최솟값 0'", "묻는 값 → 그 값의 최댓값"],
        naturalness="최댓값 조건을 빼면 f 가 하나로 정해지지 않으므로 '최댓값'을 묻는 것은 필수.",
        stem=stem(r"\{f(x)\}^3-\{f(x)\}^2-x^2f(x)+x^2", r"함수 $f(x)$의 최솟값이 $0$일 때,", r"f\left(-\frac43\right)+f(0)+f\left(\frac12\right)") .replace("의 값은?", "의 최댓값은?"),
        choices=["3/2", "5/3", "11/6", "2", "7/3"], answer="11/6", trap_answer="3/2",
        trap_path="원문처럼 |x|>1 에서 f=1 로 두어 3/2 (최댓값 조건이 없으므로 f(−4/3)=4/3 도 가능).",
        explanation=[
            r"$(f-1)(f-x)(f+x)=0$이므로 $f(x)\in\{1,\,x,\,-x\}$이고, 갈래는 $x=0,\,\pm1$에서만 바꿀 수 있다.",
            r"최솟값이 $0$이므로 $f\ge0$이고 $f(0)=0$, 따라서 $-1\le x\le1$에서 $f(x)=|x|$이다.",
            r"함정: 최댓값 조건이 없으므로 $|x|>1$에서는 $f=1$ 또는 $f=|x|$ 모두 가능하다.",
            r"$f\left(-\frac43\right)=\frac43$일 때 최대이고 $\frac43+0+\frac12=\frac{11}{6}$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (x² → 4x², 전환점 ±½)",
        changed=["x² → 4x² (두 곳)", "f(1/2) → f(1/3), f(−4/3) → f(−3/4)"],
        naturalness="계수를 바꾸면 전환점이 ±½ 로 옮겨 가므로 묻는 점을 그 안팎으로 맞춘 것.",
        stem=stem(r"\{f(x)\}^3-\{f(x)\}^2-4x^2f(x)+4x^2", r"함수 $f(x)$의 최댓값이 $1$이고 최솟값이 $0$일 때,", r"f\left(-\frac34\right)+f(0)+f\left(\frac13\right)"),
        choices=["4/3", "3/2", "5/3", "2", "7/3"], answer="5/3", trap_answer=None, trap_path=None,
        explanation=[
            r"$(f-1)(f-2x)(f+2x)=0$이므로 $f(x)\in\{1,\,2x,\,-2x\}$이다.",
            r"최댓값 $1$, 최솟값 $0$이므로 $|x|>\frac12$에서 $f=1$, $|x|\le\frac12$에서 $f=2|x|$이다.",
            r"$f\left(-\frac34\right)+f(0)+f\left(\frac13\right)=1+0+\frac23=\frac53$이다.",
        ],
    ),
]


def selections(k, need_max):
    br = [Integer(1), k*x, -k*x]
    cuts = [-Rational(1, k), Integer(0), Rational(1, k)]
    out = []
    for choice in product(range(3), repeat=4):
        fs = [br[i] for i in choice]
        if not all(simplify(fs[j].subs(x, cuts[j]) - fs[j + 1].subs(x, cuts[j])) == 0 for j in range(3)):
            continue
        # 값의 범위: 바깥 두 구간이 비유계면 최대/최소가 없음
        vals = []
        unb_hi = unb_lo = False
        for j, e in enumerate(fs):
            lo = -oo if j == 0 else cuts[j - 1]
            hi = oo if j == 3 else cuts[j]
            for end in (lo, hi):
                v = limit(e, x, end)
                if v == oo: unb_hi = True
                elif v == -oo: unb_lo = True
                else: vals.append(v)
        mn = None if unb_lo else min(vals)
        mx = None if unb_hi else max(vals)
        if mn != 0:
            continue
        if need_max and mx != 1:
            continue
        def F(v, fs=fs, cuts=cuts):
            j = 0 if v < cuts[0] else 1 if v < cuts[1] else 2 if v < cuts[2] else 3
            return fs[j].subs(x, v)
        out.append(F)
    return out


def verify(c):
    s = selections(1, True)
    c.check("원문: f 하나", len(s) == 1)
    F = s[0]
    c.ans('orig', F(-Rational(4, 3)) + F(0) + F(Rational(1, 2)))
    s = selections(1, False)
    vals = {F(-Rational(4, 3)) + F(0) + F(Rational(1, 2)) for F in s}
    c.check("1: 가능한 값 {3/2, 11/6}", vals == {Rational(3, 2), Rational(11, 6)})
    c.ans(1, max(vals))
    c.trap(1, Rational(3, 2))
    s = selections(2, True)
    c.check("2: f 하나", len(s) == 1)
    F = s[0]
    c.ans(2, F(-Rational(3, 4)) + F(0) + F(Rational(1, 3)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
