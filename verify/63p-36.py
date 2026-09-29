from lib import *

def stem(k, shift, ask):
    return (r"최고차항의 계수가 $1$인 이차함수 $f(x)$에 대하여 함수 $g(x)$를 $g(x)=\begin{cases} f(x) & (x<" + k + r") \\ f(x+" + shift + r")-f(x) & (x\ge " + k + r")\end{cases}$"
            r"이라 하자. 함수 $g(x)$가 $x=" + k + r"$에서 미분가능할 때, $f(" + ask + r")$의 값은?")

ORIG = dict(
    id="63p-36", chapter=3, page=63, num=36, source="2024년 수능특강 [24009-0071]", type="객관식",
    stem=stem("1", "1", "2"), choices=["6", "7", "8", "9", "10"], answer="6",
    general="f=x²+px+q. x≥1: f(x+1)−f(x)=2x+1+p (기울기 2). 미분: f'(1)=2+p=2 → p=0. 연속: 1+q=3 → q=2. f(2)=6.",
    special="① 오른쪽 조각 기울기 2 는 이동량 1 × 2 — 이동량이 2 면 기울기 4.",
    perspective="f(x+d)−f(x) 는 기울기 2d 인 일차식.",
    table=[
        ("이동량 1 (기울기 2)", "이동량 2 (기울기 4)", "f(x+2)−f(x) 면 p=2, q=9 → f(2)=17"),
        ("경계 x=1", "—", "x=2 면 f=x²−2x+3 → f(4)=11 (생존)"),
    ],
    sweep=["경계 k, 이동량 d: f'(k)=2d → p=2d−2k"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (이동량 2 → 오른쪽 조각 기울기 4)",
        changed=["f(x+1)−f(x) → f(x+2)−f(x)"], naturalness="",
        stem=stem("1", "2", "2"), choices=["11", "13", "15", "17", "19"], answer="17", trap_answer="11",
        trap_path="원문처럼 오른쪽 조각 기울기를 2 로 두어 p=0, 연속에서 q=7 → f(2)=11.",
        explanation=[
            r"$f(x)=x^2+px+q$라 하면 $x\ge1$에서 $g(x)=f(x+2)-f(x)=4x+4+2p$이다.",
            r"함정: 이동량이 $2$이므로 오른쪽 조각의 기울기는 $4$이다.",
            r"미분가능: $f'(1)=2+p=4$에서 $p=2$, 연속: $1+p+q=8+2p$에서 $q=9$이다.",
            r"$f(x)=x^2+2x+9$이므로 $f(2)=17$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (경계 x=1 → x=2)",
        changed=["경계 x=1 → x=2", "묻는 값 f(2) → f(4)"],
        naturalness="경계가 2 로 바뀌면 f(2) 가 연속 조건 식에 바로 쓰이므로 f(4) 를 묻는다.",
        stem=stem("2", "1", "4"), choices=["7", "8", "9", "10", "11"], answer="11", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)=x^2+px+q$이면 $x\ge2$에서 $g(x)=2x+1+p$이다.",
            r"미분가능: $f'(2)=4+p=2$에서 $p=-2$, 연속: $4+2p+q=5+p$에서 $q=3$이다.",
            r"$f(x)=x^2-2x+3$이므로 $f(4)=11$이다.",
        ],
    ),
]


def solve_f(k, d):
    p, q = symbols('p q')
    f = x**2 + p*x + q
    P = [(f, -oo, k), (expand(f.subs(x, x + d) - f), k, oo)]
    cont = piece_at(P, k, '-').subs(x, k) - piece_at(P, k, '+').subs(x, k)
    der = plim(P, lambda e: diff(e, x), k, '-') - plim(P, lambda e: diff(e, x), k, '+')
    s = solve([cont, der], [p, q], dict=True)
    assert len(s) == 1
    return f.subs(s[0])


def verify(c):
    c.ans('orig', solve_f(1, 1).subs(x, 2))
    c.ans(1, solve_f(1, 2).subs(x, 2))
    # 함정: 오른쪽 기울기를 2 로 보고 p=0, 연속만 맞춤
    q = Symbol('q')
    ft = x**2 + q
    qv = solve(ft.subs(x, 1) - (ft.subs(x, 3) - ft.subs(x, 1)), q)[0]
    c.trap(1, ft.subs(q, qv).subs(x, 2))
    c.ans(2, solve_f(2, 1).subs(x, 4))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '기울기 2→4 만 바뀌는 쉬운 변형'
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
