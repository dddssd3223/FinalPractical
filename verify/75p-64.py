from lib import *

def stem(lc, m, ask):
    return (r"최고차항의 계수가 $1$인 삼차함수 $f(x)$와 최고차항의 계수가 $" + lc + r"$인 이차함수 $g(x)$가 다음 조건을 만족시킨다. " + ask)

def box(m):
    return [r"(가) $f(\alpha)=g(\alpha)$이고 $f'(\alpha)=g'(\alpha)=-" + m + r"$인 실수 $\alpha$가 존재한다.",
            r"(나) $f'(\beta)=g'(\beta)=" + m + r"$인 실수 $\beta$가 존재한다."]

ASK_GF = r"$g(\beta+1)-f(\beta+1)$의 값을 구하시오."
ASK_FG = r"$f(\beta+1)-g(\beta+1)$의 값을 구하시오."

ORIG = dict(
    id="75p-64", chapter=3, page=75, num=64, source="2018학년도 수능 6월 모의평가 나형 30번", type="주관식",
    stem=stem("2", "16", ASK_GF), box=box("16"), answer="243",
    general="g' 기울기 4: g'(β)−g'(α)=32 → β−α=8. h=f−g=(x−α)²(x−γ), h'(β)=0 → 3β=α+2γ → γ=α+12. h(β+1)=9²·(−3)=−243 → 243.",
    special="① β−α 의 부호는 g' 의 기울기(최고차 계수) 부호 — 음수면 β 가 α 왼쪽.",
    perspective="f−g 의 중근·극점 구조.",
    table=[
        ("g 최고차 계수 2 (β>α)", "음수 (β<α)", "−2 면 β−α=−8, γ=α−12 → f−g=245"),
        ("±16", "—", "±12 면 β−α=6 → 98 (생존)"),
    ],
    sweep=["β−α=2m/(2·lc), γ=α+3(β−α)/2"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (g' 기울기 부호 → β−α 부호)",
        changed=["g 최고차 계수 2 → −2", "묻는 값 g−f → f−g"],
        naturalness="계수를 −2 로 바꾸면 g(β+1)−f(β+1) 이 음수가 되어 부호를 바꿔 묻는다.",
        stem=stem("-2", "16", ASK_FG), box=box("16"), answer="245", trap_answer="-243",
        trap_path="원문처럼 β−α=8 로 두어 f−g=h(β+1)=−243 (g' 이 감소하므로 β−α=−8).",
        explanation=[
            r"$g'$은 기울기 $-4$인 일차함수이므로 $g'(\beta)-g'(\alpha)=-4(\beta-\alpha)=32$, $\beta-\alpha=-8$이다.",
            r"함정: $\beta$는 $\alpha$보다 $8$만큼 작다.",
            r"$h=f-g$는 최고차항 계수 $1$, $h(\alpha)=h'(\alpha)=0$이므로 $h=(x-\alpha)^2(x-\gamma)$, $h'(\beta)=0$에서 $3\beta=\alpha+2\gamma$, $\gamma=\alpha-12$이다.",
            r"$h(\beta+1)=(-7)^2\times(\alpha-7-\alpha+12)=49\times5=245$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (±16 → ±12)",
        changed=["±16 → ±12"], naturalness="",
        stem=stem("2", "12", ASK_GF), box=box("12"), answer="98", trap_answer=None, trap_path=None,
        explanation=[
            r"$4(\beta-\alpha)=24$에서 $\beta-\alpha=6$이다.",
            r"$h=f-g=(x-\alpha)^2(x-\gamma)$, $3\beta=\alpha+2\gamma$에서 $\gamma=\alpha+9$이다.",
            r"$h(\beta+1)=7^2\times(-2)=-98$이므로 구하는 값은 $98$이다.",
        ],
    ),
]


def value(lc, m, sign):
    a, b, p, q, r, s, t = symbols('a b p q r s t')
    f = x**3 + p*x**2 + q*x + r
    g = lc*x**2 + s*x + t
    eqs = [f.subs(x, a) - g.subs(x, a), diff(f, x).subs(x, a) + m, diff(g, x).subs(x, a) + m,
           diff(f, x).subs(x, b) - m, diff(g, x).subs(x, b) - m]
    vals = set()
    for sol in solve(eqs, [b, p, q, s, t], dict=True):
        F, G = f.subs(sol), g.subs(sol)
        B = sol[b]
        v = simplify(sign*(G - F).subs(x, B + 1))
        vals.add(v)
    return vals


def verify(c):
    v = value(2, 16, 1)
    c.check("원문: α 와 무관한 하나의 값", len(v) == 1 and not list(v)[0].free_symbols)
    c.ans('orig', v.pop())
    v = value(-2, 16, -1)
    c.check("1: 하나", len(v) == 1 and not list(v)[0].free_symbols)
    c.ans(1, v.pop())
    c.trap(1, -value(2, 16, 1).pop())
    v = value(2, 12, 1)
    c.check("2: 하나", len(v) == 1 and not list(v)[0].free_symbols)
    c.ans(2, v.pop())


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'

# ── 3차 검토: 원문과 풀이·발문 구조가 같고 함정이 부호 실수 수준 ──
VARS[0]['drop'] = '원문과 같은 풀이이고 함정이 부호 실수 수준'
