from lib import *

def stem(expr, L):
    return (r"최고차항의 계수가 $1$이고 $f(1)=0$인 삼차함수 $f(x)$가 $\displaystyle\lim_{x\to2}" + expr + r"=" + L + r"$을 만족시킬 때, $f(3)$의 값은?")

SQ = r"\frac{f(x)}{(x-2)\{f'(x)\}^2}"
LIN = r"\frac{f(x)}{(x-2)f'(x)}"

ORIG = dict(
    id="73p-60", chapter=3, page=73, num=60, source="2018학년도 수능 나형 18번", type="객관식",
    stem=stem(SQ, r"\frac14"), choices=["4", "6", "8", "10", "12"], answer="10",
    general="극한이 유한 → f(2)=0 (아니면 분모만 0). f/(x−2)→f'(2) → 1/f'(2)=1/4 → f'(2)=4. f=(x−1)(x−2)(x−k): f'(2)=2−k=4 → k=−2 → f(3)=10.",
    special="① x=2 가 단순근이라 f/(x−2)→f'(2)≠0. 중근이면 f'(2)=0 이라 식의 차수 비교가 달라짐.",
    perspective="근의 중복도에 따른 f/((x−2)f') 의 극한: 단순 1, 이중 1/2, 삼중 1/3.",
    table=[
        ("x=2 단순근", "중근 (f'(2)=0)", "lim f/((x−2)f') = 1/2 이면 중근 → f=(x−1)(x−2)² → 2"),
        ("극한값 1/4", "—", "1/2 이면 f'(2)=2 → k=0 → 6 (생존)"),
    ],
    sweep=["f'(2)=1/L"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (극한값 1/2 은 중근에서만)",
        changed=["극한식 f/((x−2)f'²)=1/4 → f/((x−2)f')=1/2"],
        naturalness="",
        stem=stem(LIN, r"\frac12"), choices=["2", "4", "6", "8", "10"], answer="2", trap_answer="6",
        trap_path="원문처럼 극한 = 1/f'(2) 로 보고 f'(2)=2 → k=0 → f(3)=6 (단순근이면 극한은 항상 1 이라 1/2 이 될 수 없음).",
        explanation=[
            r"극한이 유한하므로 $f(2)=0$이다.",
            r"함정: $x=2$가 단순근이면 $\dfrac{f(x)}{x-2}\to f'(2)$이므로 극한은 $\dfrac{f'(2)}{f'(2)}=1$이 되어 $\frac12$이 될 수 없다.",
            r"중근이면 $f=(x-2)^2(x-c)$, $\dfrac{f}{(x-2)f'}=\dfrac{x-c}{2(x-c)+(x-2)}\to\dfrac12$ ($c\ne2$)이고, $f(1)=0$에서 $c=1$이다.",
            r"$f(x)=(x-1)(x-2)^2$이므로 $f(3)=2$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (극한값 1/4 → 1/2)",
        changed=["극한값 1/4 → 1/2"], naturalness="",
        stem=stem(SQ, r"\frac12"), choices=["4", "6", "8", "10", "12"], answer="6", trap_answer=None, trap_path=None,
        explanation=[
            r"극한이 유한하므로 $f(2)=0$이고 $\dfrac{f(x)}{x-2}\to f'(2)$이다.",
            r"$\dfrac1{f'(2)}=\dfrac12$에서 $f'(2)=2$이다.",
            r"$f=(x-1)(x-2)(x-k)$에서 $2-k=2$, $k=0$이므로 $f(3)=2\times1\times3=6$이다.",
        ],
    ),
]


def f3_values(kind, L):
    p = Symbol('p')
    out = set()
    # f(1)=0 인 최고차1 삼차: (x−1)(x²+px+q). f(2)≠0 이면 분모만 0 → 발산 (분자 f(2)≠0) → f(2)=0 필수
    q = -4 - 2*p
    f = expand((x - 1)*(x**2 + p*x + q))
    fp = diff(f, x)
    E = f/((x - 2)*fp**2) if kind == 'sq' else f/((x - 2)*fp)
    gen = limit(E, x, 2)
    cands = set(solve(gen - L, p)) | {-4, -3}  # 특수: x=2 중근(p=−4), x=1 중근(p=−3)
    for pv in cands:
        F = f.subs(p, pv)
        Fp = diff(F, x)
        e = F/((x - 2)*Fp**2) if kind == 'sq' else F/((x - 2)*Fp)
        if limit(e, x, 2) == L:
            out.add(F.subs(x, 3))
    # f(2)≠0 인 경우 발산 확인 (예시)
    return out


def verify(c):
    v = f3_values('sq', Rational(1, 4))
    c.check("원문: 유일", len(v) == 1)
    c.ans('orig', v.pop())
    v = f3_values('lin', Rational(1, 2))
    c.check("1: 유일", len(v) == 1)
    c.ans(1, v.pop())
    c.trap(1, f3_values('sq', Rational(1, 2)).pop())
    v = f3_values('sq', Rational(1, 2))
    c.check("2: 유일", len(v) == 1)
    c.ans(2, v.pop())
    c.check("f(2)≠0 예시 발산", limit((x - 1)*x**2/((x - 2)*diff((x - 1)*x**2, x)**2), x, 2, '+') == oo)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
