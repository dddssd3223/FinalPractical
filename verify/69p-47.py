from lib import *

def box(m, summand, rhs):
    return [r"(가) 모든 실수 $x$에 대하여 $f'(x)+f'(" + m + r"-x)=0$이다.",
            r"(나) $\displaystyle\sum_{k=1}^{10}" + summand + r"=" + rhs + r"$"]

PLAIN = r"\lim_{h\to0}\frac{f(k-3+h)-f(k-3-h)}{h}"
ABS = r"\lim_{h\to0+}\frac{|f(k-3+h)-f(k-3-h)|}{h}"
HEAD = r"최고차항의 계수가 $1$인 이차함수 $f(x)$가 다음 조건을 만족시킬 때, $f(1)$의 값을 구하시오."

ORIG = dict(
    id="69p-47", chapter=3, page=69, num=47, source="2025년 수능특강 [25009-0076]", type="주관식",
    stem=HEAD, box=box("8", PLAIN, "-f(0)"), answer="53",
    general="(가) → f' 이 x=4 에 대해 점대칭 → 꼭짓점 4, f=(x−4)²+c. (나): 극한=2f'(k−3)=4(k−7), 합 4(55−70)=−60=−f(0)=−(16+c) → c=44 → f(1)=53.",
    special="① 극한이 2f'(a) (양쪽 h) — 절댓값이 붙으면 꼭짓점 기준으로 부호가 갈려 |f'| 합이 됨.",
    perspective="대칭 → 꼭짓점, 극한 → 2f'.",
    table=[
        ("분자에 절댓값 없음 (부호 상쇄)", "|분자| (h→0+) → 2|f'(k−3)|", "절댓값이면 합 4·27=108=f(0) → f(1)=101"),
        ("(가) 8−x (꼭짓점 4)", "—", "6−x 면 꼭짓점 3 → 15 (생존)"),
    ],
    sweep=["k−3 이 꼭짓점 4 를 지나는 k=7 에서 f' 부호 바뀜"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (절댓값 → 꼭짓점 좌우로 부호 분기)",
        changed=["(나) 분자에 절댓값, h→0+ ", "우변 −f(0) → f(0)"],
        naturalness="절댓값을 씌우면 좌변이 양수라 우변을 f(0) 으로 바꾸고, 절댓값/h 의 양쪽 극한은 존재하지 않으므로 h→0+ 로 둔 것.",
        stem=HEAD, box=box("8", ABS, "f(0)"), answer="101", trap_answer="-67",
        trap_path="절댓값을 무시하고 원문처럼 합을 −60 으로 두어 f(0)=−60 → c=−76 → f(1)=−67.",
        explanation=[
            r"(가)에서 $f'(x)$의 그래프가 점 $(4,0)$에 대칭이므로 $f(x)=(x-4)^2+c$, $f'(x)=2(x-4)$이다.",
            r"$\displaystyle\lim_{h\to0+}\frac{|f(a+h)-f(a-h)|}{h}=2|f'(a)|$이므로 각 항은 $4|k-7|$이다.",
            r"함정: $k<7$과 $k>7$에서 부호가 달라 상쇄되지 않는다. $\sum|k-7|=21+6=27$이다.",
            r"$4\times27=108=f(0)=16+c$에서 $c=92$이다.",
            r"$f(1)=9+92=101$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 ((가) 8−x → 6−x)",
        changed=["(가) 8−x → 6−x"], naturalness="",
        stem=HEAD, box=box("6", PLAIN, "-f(0)"), answer="15", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)에서 꼭짓점이 $x=3$이므로 $f(x)=(x-3)^2+c$이다.",
            r"각 항은 $2f'(k-3)=4(k-6)$이고 합은 $4(55-60)=-20$이다.",
            r"$-f(0)=-(9+c)=-20$에서 $c=11$, $f(1)=4+11=15$이다.",
        ],
    ),
]


def solve_f(m, absval, rhs_sign):
    p, q = symbols('p q')
    f = x**2 + p*x + q
    fp = diff(f, x)
    s1 = solve(Poly(expand(fp + fp.subs(x, m - x)), x).all_coeffs(), [p], dict=True)
    assert len(s1) == 1
    f = f.subs(s1[0])
    h = Symbol('h', positive=True)
    tot = 0
    for k in range(1, 11):
        num = f.subs(x, k - 3 + h) - f.subs(x, k - 3 - h)
        if absval:
            tot += limit(Abs(expand(num))/h, h, 0, '+')
        else:
            tot += limit(num/h, h, 0)
    s2 = solve(tot - rhs_sign*f.subs(x, 0), q)
    assert len(s2) == 1
    return f.subs(q, s2[0])


def verify(c):
    c.ans('orig', solve_f(8, False, -1).subs(x, 1))
    c.ans(1, solve_f(8, True, 1).subs(x, 1))
    c.trap(1, solve_f(8, False, 1).subs(x, 1))
    c.ans(2, solve_f(6, False, -1).subs(x, 1))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='5', trap_path="극한을 f'(k−3) 으로 보아 합 −10 → f(0)=10 → c=1 → f(1)=5 (양쪽 h 라 2f'(k−3)).")
VARS[1]['explanation'].insert(-1, "함정: 분자가 $f(a+h)-f(a-h)$이므로 극한은 $f'(a)$가 아니라 $2f'(a)$이다.")
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, (lambda cc: (x**2 - 6*x + 9 + cc).subs(x, 1))(solve(sum(2*(k - 3 - 3) for k in range(1, 11)) + (9 + Symbol('cc')), Symbol('cc'))[0]))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '생존형: 원문 풀이가 그대로 통하고 함정이 계산 실수 수준'
