from lib import *

G_TXT = r"g(x)=\begin{cases}\dfrac{f(x+3)\{f(x)+1\}}{f(x)} & (f(x)\neq0)\\ 3 & (f(x)=0)\end{cases}"

def stem(lim, ask):
    return (r"최고차항의 계수가 $1$인 삼차함수 $f(x)$에 대하여 함수 $g(x)$를 $" + G_TXT + r"$이라 하자. $\displaystyle\lim_{x\to3}g(x)=" + lim + r"$일 때, $" + ask + r"$의 값은?")

ORIG = dict(
    id="50p-54", chapter=2, page=50, num=54, source="2024학년도 수능 9월 모의평가 15번", type="객관식",
    stem=stem("g(3)-1", "g(5)") + " [4점]", choices=["14", "16", "18", "20", "22"], answer="20",
    general="f(3)≠0 이면 g 는 3 에서 연속 → 극한=g(3) 모순 → f(3)=0, g(3)=3, 극한 2. x→3 에서 분모→0 → f(6)=0. f=(x−3)(x−6)(x−c), 극한 = f'(6)/f'(3) = −(6−c)/(3−c) = 2 → c=4. g(5)=f(8){f(5)+1}/f(5)=40·(−1)/(−2)=20.",
    special="① g(5) 를 식으로 계산 — f(5)≠0 이라 가능. 묻는 점이 f 의 근이면 g 의 값은 정의에 따라 3.",
    perspective="극한 조건이 f 의 근 3, 6 과 비율 f'(6)/f'(3) 을 준다.",
    table=[
        ("극한값 g(3)−1=2", "—", "g(3)−5 (비율 −2) 이면 c=0 (생존)"),
        ("묻는 점 5 (f(5)≠0)", "묻는 점이 f 의 근인 경우", "비율 ½ 이면 c=5 → g(5)=3 (정의값)"),
    ],
    sweep=["c=(6+3r)/(1+r), r=극한값", "c=5 ⇔ r=½ (묻는 점이 근)"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 1행 (극한값 → 비율 −2)",
        changed=["lim g = g(3)−1 → g(3)−5"], naturalness="",
        stem=stem("g(3)-5", "g(5)"), choices=["64", "68", "72", "76", "80"], answer="72", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(3)\neq0$이면 $g$가 $x=3$에서 연속이라 모순이므로 $f(3)=0$, $g(3)=3$이고 극한은 $-2$이다.",
            r"분모가 $0$으로 가므로 $f(6)=0$, $f(x)=(x-3)(x-6)(x-c)$이고 극한은 $\dfrac{f'(6)}{f'(3)}=-\dfrac{6-c}{3-c}=-2$에서 $c=0$이다.",
            r"$f(5)=-10$, $f(8)=80$이므로 $g(5)=\dfrac{80\times(-9)}{-10}=72$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 (묻는 점이 f 의 근 → 정의값 3)",
        changed=["lim g = g(3)−1 → g(3)−5/2"], naturalness="",
        stem=stem(r"g(3)-\frac52", "g(5)"), choices=["0", "1", "2", "3", "4"], answer="3", trap_answer="0",
        trap_path="f(5)=0 인데 식 f(8){f(5)+1}/f(5) 를 분자 0 처럼 처리해 0 으로 답함 (f(5)=0 이면 g(5)=3).",
        explanation=[
            r"$f(3)=0$, $g(3)=3$이고 극한은 $\frac12$이다. $f(6)=0$이므로 $f(x)=(x-3)(x-6)(x-c)$이다.",
            r"$-\dfrac{6-c}{3-c}=\dfrac12$에서 $c=5$, $f(x)=(x-3)(x-5)(x-6)$이다.",
            r"함정: $f(5)=0$이므로 $g(5)$는 식이 아니라 정의에 따라 $3$이다.",
        ],
    ),
]


def solve_c(L):
    c_ = Symbol('c')
    f = (x - 3)*(x - 6)*(x - c_)
    r = diff(f, x).subs(x, 6)/diff(f, x).subs(x, 3)
    cs = solve(Eq(r, L), c_)
    out = []
    for cv in cs:
        F = expand(f.subs(c_, cv))
        G = F.subs(x, x + 3)*(F + 1)/F
        if limit(G, x, 3) == L:
            out.append(F)
    return out


def g_at(F, v):
    return 3 if F.subs(x, v) == 0 else (F.subs(x, v + 3)*(F.subs(x, v) + 1)/F.subs(x, v))


def verify(c):
    # f(3)≠0 이면 연속이라 모순 → f(3)=0, f(6)=0 은 위 풀이의 필요조건. 삼차함수 f 에 대해 비율 조건 전수
    for key, L in (('orig', 2), (1, -2), (2, Rational(1, 2))):
        r = solve_c(L)
        c.check(f"{key}: f 하나", len(r) == 1)
        c.ans(key, g_at(r[0], 5))
    c.trap(2, 0)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
