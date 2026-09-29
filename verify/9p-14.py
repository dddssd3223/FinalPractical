from lib import *

ORIG = dict(
    id="9p-14", chapter=1, page=9, num=14, source="2025년 수능완성 [25054-0108]", type="객관식",
    stem=r"함수 $f(x)=\begin{cases}-\frac12x-\frac32 & (x<-1)\\ -x+2 & (x\ge-1)\end{cases}$이다. $\displaystyle\lim_{x\to-1}|f(x)-k|$의 값이 존재하도록 하는 상수 $k$에 대하여 $\displaystyle\lim_{x\to a}\frac{f(x)}{|f(x)-k|}$의 값이 존재하지 않도록 하는 모든 실수 $a$의 값의 합은?",
    choices=["-5", "-3", "-1", "1", "3"], answer="-5",
    general="x→−1 좌극한 −1, 우극한 3 → |−1−k|=|3−k| 에서 k=1. f/|f−1| 은 f(a)=1 인 점(분모→0, 분자≠0)과 x=−1(좌 −1/2, 우 3/2)에서 극한 없음. f=1 을 구간별로 풀면 x=−5 (x<−1 ✓), x=1 (x≥−1 ✓). 합 −5−1+1=−5.",
    special="① f(a)=k 인 점만 세고 구간 경계 x=−1 을 빠뜨림. ② 각 식=k 의 해를 구간 확인 없이 채택(원문은 두 해가 모두 구간 안이라 우연히 통함). ③ 분모→0 이면 무조건 극한 없음으로 처리(k=0 이고 f 가 0에 접하면 틀림).",
    perspective="극한이 없는 점 = (구간 경계에서 좌·우 값이 다른 점) ∪ (f=k 이면서 f−k 가 부호를 바꾸거나 분자≠0 인 점).",
    table=[
        ("k 를 좌·우극한 평균으로 결정", "좌·우극한이 같을 때(k 가 정해지지 않음)", "좌·우 극한이 반대 부호면 k=0 → 분자도 0이 되는 점 생김"),
        ("두 조각이 모두 일차식", "f=k 가 접하는 경우(부호 불변)", "한 조각을 이차식으로 바꾸면 접하는 근에서 극한 존재"),
        ("f=k 의 해가 각 구간 안", "해가 구간 밖인 경우", "조각식을 바꾸면 가짜 해가 생김"),
    ],
    sweep=["경계값: x=−1 (좌·우극한 다름)", "k=(L+R)/2, L=−R 이면 k=0", "f−k=0 의 해가 구간 경계를 넘는 계수값"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1·2행 / 3-C 3 (k=0, 접하는 근은 부호 불변 → 극한 존재)",
        changed=["f 의 두 조각식 (x<−1: −x−3, x≥−1: ½(x−1)²)"],
        naturalness="바꾼 것은 함수 식 하나(조건 문장은 그대로).",
        stem=r"함수 $f(x)=\begin{cases}-x-3 & (x<-1)\\ \frac12(x-1)^2 & (x\ge-1)\end{cases}$이다. $\displaystyle\lim_{x\to-1}|f(x)-k|$의 값이 존재하도록 하는 상수 $k$에 대하여 $\displaystyle\lim_{x\to a}\frac{f(x)}{|f(x)-k|}$의 값이 존재하지 않도록 하는 모든 실수 $a$의 값의 합은?",
        choices=["-5", "-4", "-3", "-2", "-1"], answer="-4", trap_answer="-3",
        trap_path="f(a)=k 인 점을 모두 제외 대상으로 봐서 x=1 까지 포함 → −3−1+1=−3.",
        explanation=[
            r"$x\to-1$일 때 좌극한 $-2$, 우극한 $2$이므로 $|-2-k|=|2-k|$에서 $k=0$이다.",
            r"$\dfrac{f(x)}{|f(x)|}$는 $f(x)>0$이면 $1$, $f(x)<0$이면 $-1$이므로 $f$의 부호가 바뀌는 곳에서만 극한이 없다.",
            r"$x=-3$에서 $-x-3$의 부호가 바뀌고, $x=-1$에서도 좌 $-1$, 우 $1$로 다르다.",
            r"함정: $x=1$은 $f(1)=0$이지만 $\frac12(x-1)^2\ge0$이라 부호가 안 바뀌어 극한이 $1$로 존재한다.",
            r"따라서 합은 $-3+(-1)=-4$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 3행 / 3-C 4 (f=k 의 해가 구간 밖)",
        changed=["x≥−1 조각: −x+2 → 2x+5"], naturalness="",
        stem=r"함수 $f(x)=\begin{cases}-\frac12x-\frac32 & (x<-1)\\ 2x+5 & (x\ge-1)\end{cases}$이다. $\displaystyle\lim_{x\to-1}|f(x)-k|$의 값이 존재하도록 하는 상수 $k$에 대하여 $\displaystyle\lim_{x\to a}\frac{f(x)}{|f(x)-k|}$의 값이 존재하지 않도록 하는 모든 실수 $a$의 값의 합은?",
        choices=["-8", "-7", "-6", "-5", "-4"], answer="-6", trap_answer="-8",
        trap_path="2x+5=1 의 해 x=−2 를 구간(x≥−1) 확인 없이 포함 → −5−2−1=−8.",
        explanation=[
            r"$x\to-1$일 때 좌극한 $-1$, 우극한 $3$이므로 $k=1$이다.",
            r"$x=-1$에서 $\dfrac{f}{|f-1|}$의 좌극한 $-\tfrac12$, 우극한 $\tfrac32$가 달라 극한이 없다.",
            r"$f(x)=1$: $x<-1$에서 $-\tfrac12x-\tfrac32=1$, $x=-5$ (구간 안).",
            r"함정: $x\ge-1$에서 $2x+5=1$의 해 $x=-2$는 구간 밖이라 버려야 한다.",
            r"따라서 합은 $-5+(-1)=-6$이다.",
        ],
    ),
]


def analyse(pieces, cut=-1):
    """pieces=(left, right). k 결정, 극한이 없는 점 집합, 구간 확인한 후보, 순진한 후보 반환"""
    L, R = pieces
    P = [(L, -oo, cut), (R, cut, oo)]
    lv, rv = L.subs(x, cut), R.subs(x, cut)
    k = Symbol('k', real=True)
    ks = solve(Eq((lv - k)**2, (rv - k)**2), k)
    assert len(ks) == 1
    k = ks[0]
    F = lambda e: e / Abs(e - k)
    cands, naive = {cut}, {cut}
    for expr, dom in ((L, lambda s: s < cut), (R, lambda s: s >= cut)):
        for s in solve(Eq(expr, k), x):
            naive.add(s)
            if dom(s):
                cands.add(s)
    bad = {a for a in cands if not plim_exists(P, F, a)[0]}
    grid = [Rational(p, 3) for p in range(-30, 30)]
    others_ok = all(plim_exists(P, F, a)[0] for a in grid if a not in cands)
    return k, bad, cands, naive, others_ok


def verify(c):
    k, bad, cands, naive, ok = analyse((-x/2 - Rational(3, 2), -x + 2))
    c.check("원문 k=1", k == 1)
    c.check("원문 후보 밖은 극한 존재", ok)
    c.ans('orig', sum(bad))

    k, bad, cands, naive, ok = analyse((-x - 3, (x - 1)**2 / 2))
    c.check("1: k=0", k == 0)
    c.check("1: x=1 에서 극한 존재(접하는 근)", 1 in cands and 1 not in bad)
    c.check("1: 후보 밖 극한 존재", ok)
    c.ans(1, sum(bad))
    c.trap(1, sum(cands))

    k, bad, cands, naive, ok = analyse((-x/2 - Rational(3, 2), 2*x + 5))
    c.check("2: k=1", k == 1)
    c.check("2: x=−2 는 구간 밖", -2 in naive and -2 not in cands)
    c.check("2: 후보 밖 극한 존재", ok)
    c.ans(2, sum(bad))
    c.trap(2, sum(naive))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '구간 확인 누락뿐 — 원문 풀이가 그대로 통함'
