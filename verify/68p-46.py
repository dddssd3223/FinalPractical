from lib import *

def stem(k, right):
    return (r"함수 $f(x)=\begin{cases}|x+1| & (x\le " + k + r") \\ " + right + r" & (x>" + k + r")\end{cases}$가 있다. "
            r"최고차항의 계수가 $1$인 이차함수 $g(x)$에 대하여 함수 $f(x)g(x)$가 실수 전체의 집합에서 미분가능할 때, $g(4)$의 값은?")

ORIG = dict(
    id="68p-46", chapter=3, page=68, num=46, source="2025년 수능특강 [25009-0074]", type="객관식",
    stem=stem("0", "3x+1"), choices=["12", "14", "16", "18", "20"], answer="20",
    general="x=−1: |x+1| 꺾임 (f=0) → g(−1)=0. x=0: f 연속, 기울기 1 vs 3 → f(0)g'(0)+f'g(0) 비교 → g(0)=0. g=x(x+1) → g(4)=20.",
    special="① 경계 x=0 에서 f 가 연속이라 조건은 g(0)=0 하나. ② 경계가 −1 보다 왼쪽이면 |x+1| 의 꺾임은 정의역 밖이고, f 는 경계에서 끊어짐.",
    perspective="fg 의 미분가능성: f 의 꺾임·끊김마다 g 의 근 (끊김이면 중근).",
    table=[
        ("경계 x=0 (f 연속, |x+1| 꺾임 포함)", "경계 k<−1 (f 불연속, 꺾임 없음)", "k=−2 면 g(−2)=g'(−2)=0 → g=(x+2)² → 36"),
        ("오른쪽 3x+1 과 경계 0", "—", "경계 1, 오른쪽 3x−1 이면 g=(x+1)(x−1) → 15 (생존)"),
    ],
    sweep=["경계 k: f(k−)=|k+1|, f(k+)=3k+1 — k=0 에서만 연속"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (경계에서 f 가 끊어지면 g 가 중근)",
        changed=["경계 x=0 → x=−2"], naturalness="",
        stem=stem("-2", "3x+1"), choices=["28", "30", "32", "34", "36"], answer="36", trap_answer="30",
        trap_path="원문처럼 |x+1| 의 꺾임 −1 과 경계 −2 에서 g=0 으로 두어 g=(x+1)(x+2) → 30 (x≤−2 에는 꺾임이 없고, −2 에서 f 가 끊어짐).",
        explanation=[
            r"$x\le-2$에서 $f(x)=-x-1$이므로 $|x+1|$의 꺾이는 점 $-1$은 이 구간에 없다.",
            r"$f(-2)=1$, $\displaystyle\lim_{x\to-2+}f(x)=-5$로 끊어지므로 $fg$가 연속이려면 $g(-2)=0$이다.",
            r"함정: 좌미분계수 $1\cdot g'(-2)$와 우미분계수 $-5g'(-2)$가 같아야 하므로 $g'(-2)=0$, 즉 $g(x)=(x+2)^2$이다.",
            r"$g(4)=36$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (경계 0 → 1, 오른쪽 3x+1 → 3x−1)",
        changed=["경계 x=0 → x=1", "3x+1 → 3x−1"],
        naturalness="경계를 1 로 옮기면서 f 가 연속으로 이어지도록 오른쪽 식의 상수를 함께 맞춘 것.",
        stem=stem("1", "3x-1"), choices=["11", "13", "15", "17", "19"], answer="15", trap_answer=None, trap_path=None,
        explanation=[
            r"$x=-1$에서 $|x+1|$이 꺾이고 $f(-1)=0$이므로 $g(-1)=0$이다.",
            r"$x=1$에서 $f$는 연속($f(1)=2$)이고 기울기가 $1$, $3$으로 다르므로 $g(1)=0$이다.",
            r"$g(x)=(x+1)(x-1)$이므로 $g(4)=15$이다.",
        ],
    ),
]


def solve_g(k, right):
    p, q = symbols('p q')
    g = x**2 + p*x + q
    # f 조각: x≤k 는 |x+1| (−1 에서 나눔), x>k 는 right
    P = []
    if k > -1:
        P += [(-(x + 1), -oo, -1), (x + 1, -1, k)]
    else:
        P += [(-(x + 1), -oo, k)]
    P += [(right, k, oo)]
    FG = [(expand(e*g), lo, hi) for e, lo, hi in P]
    pts = sorted({hi for _, _, hi in P if hi != oo})
    eqs = []
    for t in pts:
        eqs.append(piece_at(FG, t, '-').subs(x, t) - piece_at(FG, t, '+').subs(x, t))  # 연속 (f(k)=왼쪽 값)
        eqs.append(plim(FG, lambda e: diff(e, x), t, '-') - plim(FG, lambda e: diff(e, x), t, '+'))
    sols = solve(eqs, [p, q], dict=True)
    return [g.subs(s) for s in sols]


def verify(c):
    s = solve_g(0, 3*x + 1)
    c.check("원문: 유일", len(s) == 1)
    c.ans('orig', s[0].subs(x, 4))
    s = solve_g(-2, 3*x + 1)
    c.check("1: 유일", len(s) == 1)
    c.ans(1, s[0].subs(x, 4))
    c.trap(1, ((x + 1)*(x + 2)).subs(x, 4))
    s = solve_g(1, 3*x - 1)
    c.check("2: 유일", len(s) == 1)
    c.ans(2, s[0].subs(x, 4))
