from lib import *

def stem(sym, fp4):
    return (r"함수 $y=f(x)$의 그래프는 " + sym + r"에 대하여 대칭이고, $f'(2)=-3$, $f'(4)=" + fp4
            + r"$일 때, $\displaystyle\lim_{x\to-2}\frac{f(x^2)-f(4)}{f(x)-f(-2)}$의 값은?")

ORIG = dict(
    id="70p-51", chapter=3, page=70, num=51, source="2010학년도 수능 6월 모의평가 가형 6번", type="객관식",
    stem=stem(r"$y$축", "6"), choices=["-8", "-4", "4", "8", "12"], answer="-8",
    general="분자·분모를 x+2 로 나누면 → 2x·f'(x²) / f'(x) at x=−2 = (−4)(6)/f'(−2). y축 대칭 → f' 은 원점 대칭 → f'(−2)=3. 값 −24/3=−8.",
    special="① y축 대칭이면 f'(−a)=−f'(a) — 원점 대칭이면 f'(−a)=f'(a) 로 부호가 바뀜. ② 합성 f(x²) 미분의 2x 가 x=−2 에서 −4.",
    perspective="미분계수 정의 두 개의 비.",
    table=[
        ("y축 대칭 (f' 홀함수)", "원점 대칭 (f' 짝함수)", "원점 대칭이면 f'(−2)=−3 → 8"),
        ("f'(4)=6", "—", "9 면 −12 (생존)"),
    ],
    sweep=["f'(−2)=∓f'(2) (대칭 종류)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (대칭 종류에 따른 f'(−2) 부호)",
        changed=["y축 대칭 → 원점 대칭"], naturalness="",
        stem=stem("원점", "6"), choices=["-8", "-4", "4", "8", "12"], answer="8", trap_answer="-8",
        trap_path="원문처럼 f'(−2)=−f'(2)=3 으로 두어 −8 (원점 대칭이면 f' 은 y축 대칭이라 f'(−2)=−3).",
        explanation=[
            r"주어진 식은 $\dfrac{f(x^2)-f(4)}{x^2-4}\cdot(x-2)\cdot\dfrac{x+2}{f(x)-f(-2)}$이므로 극한은 $\dfrac{f'(4)\times(-4)}{f'(-2)}$이다.",
            r"함정: 그래프가 원점 대칭이면 $f(-x)=-f(x)$를 미분해 $f'(-x)=f'(x)$, 즉 $f'(-2)=f'(2)=-3$이다.",
            r"값은 $\dfrac{6\times(-4)}{-3}=8$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (f'(4)=6 → 9)",
        changed=["f'(4)=6 → 9"], naturalness="",
        stem=stem(r"$y$축", "9"), choices=["-16", "-12", "-8", "8", "12"], answer="-12", trap_answer=None, trap_path=None,
        explanation=[
            r"극한은 $\dfrac{f'(4)\times(-4)}{f'(-2)}$이다.",
            r"$y$축 대칭이므로 $f'(-2)=-f'(2)=3$이다.",
            r"값은 $\dfrac{9\times(-4)}{3}=-12$이다.",
        ],
    ),
]


def value(parity, fp4):
    """parity=0 짝(y축), 1 홀(원점). 6차 이하 해당 다항식 일반형에서 극한 계산 → 자유 계수 무관 확인"""
    cs = symbols('c0:8')
    f = sum(cs[i]*x**i for i in range(8) if i % 2 == parity)
    fp = diff(f, x)
    s = solve([fp.subs(x, 2) + 3, fp.subs(x, 4) - fp4], [cs[parity + 2], cs[parity + 4]], dict=True)[0]
    F = f.subs(s)
    t = Symbol('t')
    num = F.subs(x, (t - 2)**2) - F.subs(x, 4)
    den = F.subs(x, t - 2) - F.subs(x, -2)
    q = cancel(expand(num)/t) / cancel(expand(den)/t)
    v = simplify(q.subs(t, 0))
    return v


def verify(c):
    v = value(0, 6)
    c.check("원문: 자유 계수 무관", not (v.free_symbols))
    c.ans('orig', v)
    v = value(1, 6)
    c.check("1: 자유 계수 무관", not v.free_symbols)
    c.ans(1, v)
    c.trap(1, value(0, 6))
    v = value(0, 9)
    c.check("2: 자유 계수 무관", not v.free_symbols)
    c.ans(2, v)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='12', trap_path="f'(−2)=f'(2)=−3 으로 두어 12 (y축 대칭이면 f' 은 원점 대칭이라 f'(−2)=3).")
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, value(1, 9))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '생존형: 원문 풀이가 그대로 통하고 함정이 계산 실수 수준'
