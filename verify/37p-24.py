from lib import *

def box(iv):
    return [r"(가) $g(x)=\begin{cases}\dfrac{x}{f(x)} & (x\neq0)\\ \dfrac13 & (x=0)\end{cases}$",
            r"(나) " + iv + r"에서 방정식 $g(x)=\frac12$은 오직 하나의 실근을 갖는다."]

STEM = r"최고차항의 계수가 $1$인 삼차함수 $f(x)$에 대하여 실수 전체의 집합에서 연속인 함수 $g(x)$가 다음 조건을 만족시킨다. "

ORIG = dict(
    id="37p-24", chapter=2, page=37, num=24, source="2025년 수능완성 [25054-0127]", type="객관식",
    stem=STEM + r"$f(1)$의 값이 자연수일 때, $g(4)$의 값은?", box=box(r"열린구간 $(0,\,1)$"),
    choices=["1", "1/3", "1/5", "1/7", "1/9"], answer="1/7",
    general="g 연속 → f(0)=0, f'(0)=3, 다른 실근 없음: f=x(x²+px+3), p²<12. (나): x²+px+1=0 이 (0,1) 에 근 하나 — 두 근의 곱 1 이라 서로 다른 두 양근이면 정확히 하나 → p<−2. f(1)=4+p 자연수, p 정수 → p=−3. g(4)=1/(16−12+3)=1/7.",
    special="① (0,1) 의 근 하나를 '두 근의 곱 1' 로 판정 — 열린구간이라 중근 x=1 (p=−2) 이 빠짐. 구간이 (0,1] 이면 p=−2 도 가능.",
    perspective="x²+px+1 의 두 근은 역수 관계.",
    table=[
        ("(나) 열린구간 (0,1)", "근이 x=1 인 경우 (p=−2, 중근)", "(0,1] 이면 p=−2 도 조건 만족"),
        ("g(0)=1/3", "—", "—"),
        ("묻는 값 g(4)", "—", "g(5) 로 바꾸면 생존 확인"),
    ],
    sweep=["p=−2: x²−2x+1=(x−1)² (x=1 중근)", "p²<12: f 의 다른 실근 없음"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (구간 끝의 중근 x=1)",
        changed=["(나) 열린구간 (0,1) → 구간 (0,1]", "묻는 값 → f(1) 의 모든 값의 합"],
        naturalness="구간을 넓히면 f 가 둘이 되어 묻는 값을 '모든 값의 합'으로 바꾼 것은 필수.",
        stem=STEM + r"$f(1)$의 값이 자연수일 때, $f(1)$의 값이 될 수 있는 모든 값의 합은?", box=box(r"구간 $(0,\,1]$"),
        choices=["1", "2", "3", "4", "5"], answer="3", trap_answer="1",
        trap_path="원문처럼 두 근이 서로 다른 양근(p<−2)만 보고 p=−3 → f(1)=1.",
        explanation=[
            r"원문과 같이 $f(x)=x(x^2+px+3)$, $p^2<12$이고 (나)는 $x^2+px+1=0$이 $(0,1]$에서 근을 하나만 갖는 것이다.",
            r"$p=-3$: 근 $\frac{3\pm\sqrt5}2$ 중 하나만 $(0,1]$에 있다.",
            r"함정: $p=-2$이면 $(x-1)^2=0$으로 근이 $x=1$ 하나이고 $(0,1]$에 속한다.",
            r"$f(1)=4+p$는 $1$, $2$이므로 합은 $3$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 3행 (묻는 점 4 → 5)",
        changed=["묻는 값 g(4) → g(5)"], naturalness="",
        stem=STEM + r"$f(1)$의 값이 자연수일 때, $g(5)$의 값은?", box=box(r"열린구간 $(0,\,1)$"),
        choices=["1/7", "1/9", "1/11", "1/13", "1/15"], answer="1/13", trap_answer=None, trap_path=None,
        explanation=[
            r"$g$가 연속이므로 $f(x)=x(x^2+px+3)$이고 $x^2+px+3$은 실근이 없다.",
            r"(나)에서 $x^2+px+1=0$이 $(0,1)$에 근 하나 → $p<-2$, $f(1)$이 자연수이므로 $p=-3$이다.",
            r"$g(5)=\dfrac{1}{25-15+3}=\dfrac1{13}$이다.",
        ],
    ),
]


def candidates(interval):
    out = []
    for p in range(-6, 7):
        f = x*(x**2 + p*x + 3)
        g = x/f
        # (가): g 연속 (0 에서 1/3, 다른 실근 없음)
        if limit(g, x, 0) != Rational(1, 3):
            continue
        if any(r != 0 for r in real_roots(Poly(f, x))):
            continue
        # (나): 구간에서 g=1/2 의 해 개수 1
        sols = {r for r in real_roots(Poly(2*x - f, x)) if r != 0 and interval(r)}
        if len(sols) != 1:
            continue
        if (f.subs(x, 1)).is_integer and f.subs(x, 1) > 0:
            out.append(f)
    return out


def verify(c):
    r = candidates(lambda v: 0 < v < 1)
    c.check("원문: f 하나", len(r) == 1)
    c.ans('orig', (x/r[0]).subs(x, 4))
    r1 = candidates(lambda v: 0 < v <= 1)
    c.check("1: f 두 개 (p=−3, −2)", len(r1) == 2)
    c.ans(1, sum(f.subs(x, 1) for f in r1))
    c.trap(1, r[0].subs(x, 1))
    c.ans(2, (x/r[0]).subs(x, 5))
