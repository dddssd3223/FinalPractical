from lib import *

def box(fx):
    return [r"(가) $0\le x\le k$일 때, $f(x)=" + fx + r"$", r"(나) 모든 실수 $x$에 대하여 $f(x+k)=f(x)+f(k)$이다."]

ORIG = dict(
    id="56p-12", chapter=3, page=56, num=12, source="2023년 수능완성 [23054-0126]", type="객관식",
    stem=r"함수 $f(x)$가 다음 조건을 만족시킨다. 함수 $f(x)$가 실수 전체의 집합에서 미분가능하도록 하는 양수 $k$의 값은?",
    box=box("x^3-6x^2+10x"), choices=["1", "2", "3", "4", "5"], answer="4",
    general="(나)로 [k,2k] 에서 f(x)=f(x−k)+f(k) → x=k 의 우미분계수 f'(0)=10, 좌미분계수 3k²−12k+10. 같으려면 3k²−12k=0 → k=4.",
    special="① x=k 한 점만 확인 — (나)로 모든 이음매가 같은 조건. ② (가)의 삼차식은 [0,k] 에서만 성립, 밖은 (나)로 이어 붙인 함수.",
    perspective="이음매에서 f'(k−)=f'(0+).",
    table=[
        ("(가)의 식은 [0,k] 에서만", "구간 밖에서 삼차식을 쓰는 경우", "f(10) 을 물으면 (나)로 옮겨야 함 (삼차식 대입은 틀림)"),
        ("−6x²", "—", "−9x² 이면 k=6 (생존)"),
    ],
    sweep=["3k²+2pk=0 (p: 이차항 계수)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 4 (식이 성립하는 구간 밖)",
        changed=["묻는 값: k → f(10) (주관식)"], naturalness="",
        stem=r"함수 $f(x)$가 다음 조건을 만족시킨다. 함수 $f(x)$가 실수 전체의 집합에서 미분가능하도록 하는 양수 $k$에 대하여 $f(10)$의 값을 구하시오.",
        box=box("x^3-6x^2+10x"), answer="20", trap_answer="500",
        trap_path="(가)의 삼차식에 x=10 을 바로 대입해 500 (식은 0≤x≤4 에서만 성립).",
        explanation=[
            r"원문과 같이 $x=k$에서 좌미분계수 $3k^2-12k+10$과 우미분계수 $f'(0)=10$이 같아야 하므로 $k=4$이다.",
            r"함정: (가)의 식은 $0\le x\le4$에서만 성립하므로 $f(10)$에 바로 대입할 수 없다.",
            r"(나)에서 $f(10)=f(6)+f(4)=f(2)+2f(4)$이다.",
            r"$f(2)=8-24+20=4$, $f(4)=64-96+40=8$이므로 $f(10)=4+16=20$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (이차항 −6x² → −9x²)",
        changed=["(가) x³−6x²+10x → x³−9x²+10x"], naturalness="",
        stem=r"함수 $f(x)$가 다음 조건을 만족시킨다. 함수 $f(x)$가 실수 전체의 집합에서 미분가능하도록 하는 양수 $k$의 값은?",
        box=box("x^3-9x^2+10x"), choices=["3", "4", "5", "6", "7"], answer="6", trap_answer=None, trap_path=None,
        explanation=[
            r"$[k,2k]$에서 $f(x)=f(x-k)+f(k)$이므로 $x=k$의 우미분계수는 $f'(0)=10$이다.",
            r"좌미분계수는 $3k^2-18k+10$이다.",
            r"$3k^2-18k=0$에서 $k=6$이다.",
        ],
    ),
]


def k_of(cubic):
    k = Symbol('k', positive=True)
    fp = diff(cubic, x)
    ks = solve(Eq(fp.subs(x, k), fp.subs(x, 0)), k)
    return ks


def F(cubic, k, v):
    """(나)로 확장한 f(v)"""
    n = floor(v/k)
    return cubic.subs(x, v - n*k) + n*cubic.subs(x, k)


def diffable(cubic, k):
    """이음매 x=k, 2k, 0 에서 좌·우 미분계수 비교"""
    P = []
    for n in range(-2, 4):
        P.append((cubic.subs(x, x - n*k) + n*cubic.subs(x, k), n*k, (n + 1)*k))
    return all(simplify(plim(P, lambda e: diff(e, x), p, '-') - plim(P, lambda e: diff(e, x), p, '+')) == 0 for p in (0, k, 2*k))


def verify(c):
    cub = x**3 - 6*x**2 + 10*x
    ks = k_of(cub)
    c.check("원문: k 하나, 이음매 미분가능", ks == [4] and diffable(cub, 4))
    c.ans('orig', ks[0])
    c.ans(1, F(cub, 4, 10))
    c.trap(1, cub.subs(x, 10))
    cub2 = x**3 - 9*x**2 + 10*x
    ks = k_of(cub2)
    c.check("2: k 하나, 미분가능", ks == [6] and diffable(cub2, 6))
    c.ans(2, ks[0])


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
