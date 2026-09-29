from lib import *
from itertools import product

ORIG = dict(
    id="25p-59", chapter=1, page=25, num=59, source="2020학년도 수능 나형 14번", type="객관식",
    stem=r"상수항과 계수가 모두 정수인 두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킬 때, $f(2)$의 최댓값은? [4점]",
    box=[r"(가) $\displaystyle\lim_{x\to\infty}\frac{f(x)g(x)}{x^3}=2$", r"(나) $\displaystyle\lim_{x\to0}\frac{f(x)g(x)}{x^2}=-4$"],
    choices=["4", "6", "8", "10", "12"], answer="8",
    general="fg 는 최고차 2 삼차, x=0 에서 이중근, x² 계수 −4 → fg=2x³−4x²=2x²(x−2). f 는 정수 계수 인수: ±2^a·x^b·(x−2)^c. (x−2) 를 포함하면 f(2)=0 → f=2x² 일 때 최대 8.",
    special="① (x−2) 인수를 포함하면 f(2)=0 이라 자연스럽게 배제 — 인수가 (x+2) 면 오히려 최대를 만드는 인수가 됨. ② 상수 인수 2 를 f 쪽에 몰아주는 것.",
    perspective="정수 계수 인수 분배 = 약수 나누기. f(2) 는 각 인수의 x=2 값의 곱.",
    table=[
        ("(나)의 값 −4", "남는 인수가 x=2 에서 0 인 경우", "+4 로 바꾸면 인수 (x+2) → x=2 에서 4, 포함해야 최대"),
        ("(가)의 값 2", "—", "4 로 바꾸면 상수 인수 4 (생존)"),
        ("정수 계수", "상수배로 무한히 키우는 경우", "—"),
    ],
    sweep=["남는 일차 인수 (x−r): r=2 이면 f(2)=0"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (남는 인수가 x=2 에서 0 이 아니라 오히려 키우는 인수)",
        changed=["(나)의 값 −4 → 4"], naturalness="",
        stem=r"상수항과 계수가 모두 정수인 두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킬 때, $f(2)$의 최댓값은?",
        box=[r"(가) $\displaystyle\lim_{x\to\infty}\frac{f(x)g(x)}{x^3}=2$", r"(나) $\displaystyle\lim_{x\to0}\frac{f(x)g(x)}{x^2}=4$"],
        choices=["8", "12", "16", "24", "32"], answer="32", trap_answer="8",
        trap_path="원문처럼 남는 일차 인수를 f 에서 빼고 f=2x² 로 두어 8 (이번 인수 x+2 는 x=2 에서 4).",
        explanation=[
            r"(가), (나)에서 $f(x)g(x)=2x^3+4x^2=2x^2(x+2)$이다.",
            r"$f(x)$는 $\pm2^a x^b(x+2)^c$ ($a,c\in\{0,1\}$, $b\in\{0,1,2\}$) 꼴이다.",
            r"함정: 원문의 $(x-2)$는 $f(2)=0$을 만들어 빼야 했지만, $(x+2)$는 $x=2$에서 $4$라 넣어야 커진다.",
            r"$f(x)=2x^2(x+2)$, $g(x)=1$일 때 $f(2)=2\times4\times4=32$로 최대이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 ((가)의 값 2 → 4)",
        changed=["(가)의 값 2 → 4"], naturalness="",
        stem=r"상수항과 계수가 모두 정수인 두 다항함수 $f(x)$, $g(x)$가 다음 조건을 만족시킬 때, $f(2)$의 최댓값은?",
        box=[r"(가) $\displaystyle\lim_{x\to\infty}\frac{f(x)g(x)}{x^3}=4$", r"(나) $\displaystyle\lim_{x\to0}\frac{f(x)g(x)}{x^2}=-4$"],
        choices=["8", "12", "16", "20", "24"], answer="16", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)g(x)=4x^3-4x^2=4x^2(x-1)$이다.",
            r"$f(x)$는 $\pm2^a x^b(x-1)^c$ ($a\in\{0,1,2\}$) 꼴이고 $x=2$에서 $x-1=1$이다.",
            r"$f(x)=4x^2(x-1)$ (또는 $4x^2$)일 때 $f(2)=16$으로 최대이다.",
        ],
    ),
]


def fg_poly(lead, low):
    """fg: 최고차 lead 인 삼차, x² 계수 low, x·상수항 0"""
    return lead*x**3 + low*x**2


def max_f2(F):
    content, facs = factor_list(F)
    content = int(content)
    divs = [d for d in range(1, abs(content) + 1) if content % d == 0]
    best = None
    ranges = [range(e + 1) for _, e in facs]
    for d in divs:
        for sgn in (1, -1):
            for exps in product(*ranges):
                f = sgn*d*prod(p**k for (p, _), k in zip(facs, exps))
                g = cancel(F/f)
                if not g.is_polynomial(x) or not all(cc.is_integer for cc in Poly(g, x).all_coeffs()):
                    continue
                v = f.subs(x, 2)
                best = v if best is None or v > best else best
    return best


def verify(c):
    for key, lead, low in (('orig', 2, -4), (1, 2, 4), (2, 4, -4)):
        F = fg_poly(lead, low)
        c.check(f"{key}: fg 조건 재확인", limit(F/x**3, x, oo) == lead and limit(F/x**2, x, 0) == low)
        c.ans(key, max_f2(F))
    c.trap(1, 2*2**2)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
