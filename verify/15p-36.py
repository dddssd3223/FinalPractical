from lib import *

ORIG = dict(
    id="15p-36", chapter=1, page=15, num=36, source="2024년 수능특강 [24009-0023]", type="객관식",
    stem=r"일차함수 $f(x)$와 이차함수 $g(x)$가 다음 조건을 만족시킬 때, $\dfrac{f(3)}{g(0)}$의 값은?",
    box=[r"(가) $\left\{a\,\middle|\,\displaystyle\lim_{x\to a}g(x)=0\right\}=\{-1\}$",
         r"(나) $\left\{b\,\middle|\,\displaystyle\lim_{x\to b}\frac{1}{g(x)-f(x)}\text{의 값이 존재하지 않는다.}\right\}=\{-2,\,1\}$"],
    choices=["6", "7", "8", "9", "10"], answer="6",
    general="(가): g 의 실근이 −1 하나 → g=k(x+1)². (나): g−f(이차, 최고차 k)의 실근이 −2, 1 → g−f=k(x+2)(x−1). f=k(x+3). f(3)/g(0)=6k/k=6.",
    special="① (나)의 원소가 두 개라 g−f 를 두 근으로 바로 인수분해 — 원소가 하나면 중근으로 봐야 함. ② g 와 f 가 만나는 점을 g 의 근으로 잡는 착각(그러면 그 점도 (나)의 집합에 들어감).",
    perspective="'극한이 존재하지 않는 점 = 분모의 실근', 이차식의 실근이 하나 ⇔ 중근.",
    table=[
        ("(가) 원소 1개", "g 가 서로 다른 두 근", "원소를 두 개로 바꾸면 g=k(x−p)(x−q) (생존)"),
        ("(나) 원소 2개", "g−f 가 중근인 경우", "원소 1개로 바꾸면 g−f=k(x−b)²"),
        ("f 일차", "g−f 차수가 떨어지는 경우", "—"),
    ],
    sweep=["(나) 원소 수 2 → 1: 판별식 0 경계"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 / 3-C 5 (원소가 하나 → 중근)",
        changed=["(나) 집합 {−2, 1} → {1}"], naturalness="",
        stem=r"일차함수 $f(x)$와 이차함수 $g(x)$가 다음 조건을 만족시킬 때, $\dfrac{f(3)}{g(0)}$의 값은?",
        box=[r"(가) $\left\{a\,\middle|\,\displaystyle\lim_{x\to a}g(x)=0\right\}=\{-1\}$",
             r"(나) $\left\{b\,\middle|\,\displaystyle\lim_{x\to b}\frac{1}{g(x)-f(x)}\text{의 값이 존재하지 않는다.}\right\}=\{1\}$"],
        choices=["6", "8", "10", "12", "14"], answer="12", trap_answer="8",
        trap_path="g−f 의 다른 근을 g 의 근 −1 로 잡아 g−f=k(x−1)(x+1) → f=2k(x+1) → 8 (이러면 −1 도 (나)의 집합에 들어가 모순).",
        explanation=[
            r"(가)에서 이차함수 $g$의 실근이 $-1$ 하나이므로 $g(x)=k(x+1)^2$이다.",
            r"(나)에서 $g-f$는 최고차항의 계수가 $k$인 이차식이고 실근이 $1$ 하나이므로 $g(x)-f(x)=k(x-1)^2$이다.",
            r"함정: 원소가 하나이면 두 근이 아니라 중근이다.",
            r"$f(x)=k\{(x+1)^2-(x-1)^2\}=4kx$이다.",
            r"$\dfrac{f(3)}{g(0)}=\dfrac{12k}{k}=12$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 1행 (근의 위치만 이동)",
        changed=["(가) {−1} → {2}, (나) {−2, 1} → {−1, 3}"], naturalness="두 집합의 수치만 바꾼 것(구조 동일).",
        stem=r"일차함수 $f(x)$와 이차함수 $g(x)$가 다음 조건을 만족시킬 때, $\dfrac{f(3)}{g(0)}$의 값은?",
        box=[r"(가) $\left\{a\,\middle|\,\displaystyle\lim_{x\to a}g(x)=0\right\}=\{2\}$",
             r"(나) $\left\{b\,\middle|\,\displaystyle\lim_{x\to b}\frac{1}{g(x)-f(x)}\text{의 값이 존재하지 않는다.}\right\}=\{-1,\,3\}$"],
        choices=["1/4", "1/2", "1", "2", "4"], answer="1/4", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)에서 $g(x)=k(x-2)^2$이다.",
            r"(나)에서 $g(x)-f(x)=k(x+1)(x-3)$이다.",
            r"$f(x)=k\{(x-2)^2-(x+1)(x-3)\}=k(-2x+7)$이다.",
            r"$\dfrac{f(3)}{g(0)}=\dfrac{k}{4k}=\dfrac14$이다.",
        ],
    ),
]


def real_root_set(p):
    return set(real_roots(Poly(p, x))) if Poly(p, x).degree() > 0 else set()


def build(A, B):
    k = Symbol('k', nonzero=True)
    g = k*(x - A[0])**2 if len(A) == 1 else k*(x - A[0])*(x - A[1])
    h = k*(x - B[0])**2 if len(B) == 1 else k*(x - B[0])*(x - B[1])
    f = expand(g - h)
    return k, f, g


def verify(c):
    for key, A, B in (('orig', [-1], [-2, 1]), (1, [-1], [1]), (2, [2], [-1, 3])):
        k, f, g = build(A, B)
        fs, gs = f.subs(k, 1), g.subs(k, 1)
        c.check(f"{key}: f 일차", Poly(fs, x).degree() == 1)
        c.check(f"{key}: 집합 조건 재확인", real_root_set(gs) == set(A) and real_root_set(gs - fs) == set(B))
        c.ans(key, simplify(f.subs(x, 3)/g.subs(x, 0)))
    k = Symbol('k')
    ft = expand(k*(x + 1)**2 - k*(x - 1)*(x + 1))
    c.check("1: 함정 f 는 (나)의 집합에 −1 을 추가", real_root_set((k*(x + 1)**2 - ft).subs(k, 1)) == {-1, 1})
    c.trap(1, simplify(ft.subs(x, 3)/(k*(x + 1)**2).subs(x, 0)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
