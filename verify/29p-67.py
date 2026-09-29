from lib import *

def box(num, fx):
    return [r"모든 실수 $a$에 대하여 $\displaystyle\lim_{x\to a}\frac{" + num + r"}{(f(x))^2-k(x+2)f(x)}$의 값이 존재한다."]

ORIG = dict(
    id="29p-67", chapter=1, page=29, num=67, source="2026학년도 수능 9월 모의평가 13번", type="객관식",
    stem=r"함수 $f(x)=x^2+6x+12$에 대하여 다음 조건을 만족시키는 모든 정수 $k$의 개수는? [4점]",
    box=box("x^2", "x^2+6x+12"), choices=["5", "6", "7", "8", "9"], answer="8",
    general="분모 f(f−k(x+2)), f 는 실근 없음. h=f−k(x+2)=x²+(6−k)x+12−2k 의 실근에서 분자 x² 가 같은 차수 이상으로 0 이어야 → h 가 실근이 없거나 h=x² (k=6). 판별식 (k−6)(k+2)<0 → k=−1,…,5 (7개) + k=6 → 8.",
    special="① 판별식만 보고 7 개 → h 의 근이 0(이중근)이면 분자 x² 로 상쇄되는 경우를 놓침. ② 분자의 차수: x² 라서 이중근까지 상쇄 가능(분자가 x 면 k=6 도 불가).",
    perspective="분모의 실근마다 '분자의 근 차수 ≥ 분모의 근 차수'.",
    table=[
        ("분자 x²", "h 의 이중근 0 을 상쇄 못하는 경우", "분자 x 로 바꾸면 k=6 제외 → 7"),
        ("f 는 실근 없음", "f 자체가 분모의 근을 만드는 경우", "—"),
        ("f=x²+6x+12", "—", "x²+2x+5 로 바꾸면 판별식 범위만 바뀜 (생존)"),
    ],
    sweep=["h(0)=0 ⇔ k=6, 이때 h=x²", "판별식 k²−4k−12=0 ⇔ k=−2, 6"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 / 3-C 5 (분자 차수가 낮아 이중근을 상쇄 못함)",
        changed=["분자 x² → x"], naturalness="",
        stem=r"함수 $f(x)=x^2+6x+12$에 대하여 다음 조건을 만족시키는 모든 정수 $k$의 개수는?",
        box=box("x", "x^2+6x+12"), choices=["5", "6", "7", "8", "9"], answer="7", trap_answer="8",
        trap_path="원문처럼 k=6(h=x²)도 포함해 8 (분자 x 는 이중근 x² 를 상쇄 못함).",
        explanation=[
            r"$f$는 실근이 없으므로 분모의 실근은 $h(x)=f(x)-k(x+2)=x^2+(6-k)x+12-2k$의 실근이다.",
            r"$h$가 실근이 없으려면 $(6-k)^2-4(12-2k)<0$, 즉 $-2<k<6$이다.",
            r"$k=6$이면 $h=x^2$이고 $\dfrac{x}{f(x)\cdot x^2}=\dfrac{1}{xf(x)}$는 $x\to0$에서 발산한다. 함정: 분자가 $x$라 이중근을 상쇄하지 못한다.",
            r"정수 $k$는 $-1,0,1,2,3,4,5$의 $7$개이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 3행 (f=x²+2x+5)",
        changed=["f=x²+6x+12 → x²+2x+5"], naturalness="",
        stem=r"함수 $f(x)=x^2+2x+5$에 대하여 다음 조건을 만족시키는 모든 정수 $k$의 개수는?",
        box=box("x^2", "x^2+2x+5"), choices=["7", "8", "9", "10", "11"], answer="9", trap_answer=None, trap_path=None,
        explanation=[
            r"$f$는 실근이 없고, $h(x)=x^2+(2-k)x+5-2k$의 실근에서 분자 $x^2$가 상쇄해야 한다.",
            r"$h(0)=0$이면 $k=\frac52$로 정수가 아니므로, $h$는 실근이 없어야 한다.",
            r"$(2-k)^2-4(5-2k)=k^2+4k-16<0$에서 $-2-2\sqrt5<k<-2+2\sqrt5$이다.",
            r"정수 $k$는 $-6,-5,\ldots,2$의 $9$개이다.",
        ],
    ),
]


def count(fx, num):
    k = Symbol('k')
    good = []
    for kv in range(-20, 21):
        D = expand(fx**2 - kv*(x + 2)*fx)
        roots = set(real_roots(Poly(D, x)))
        if all(lim_exists(num/D, r)[0] for r in roots):
            good.append(kv)
    return good


def verify(c):
    F = x**2 + 6*x + 12
    g0 = count(F, x**2)
    c.check("원문: k=−1..6", g0 == list(range(-1, 7)))
    c.ans('orig', len(g0))
    g1 = count(F, x)
    c.check("1: k=−1..5", g1 == list(range(-1, 6)))
    c.ans(1, len(g1))
    c.trap(1, len(g0))
    g2 = count(x**2 + 2*x + 5, x**2)
    c.ans(2, len(g2))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
