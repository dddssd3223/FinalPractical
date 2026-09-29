from lib import *

def stem(iv):
    return r"두 함수 $f(x)=x^3+x^2$, $g(x)=x-2$와 $10$ 이하의 자연수 $n$에 대하여 $x$에 대한 방정식 $f(x)=ng(x)$는 $n$의 값에 관계없이 오직 하나의 실근을 갖는다. 이 실근이 " + iv + r"에 속하도록 하는 $10$ 이하의 모든 자연수 $n$의 값의 합을 구하시오."

ORIG = dict(
    id="37p-23", chapter=2, page=37, num=23, source="2024년 수능완성 [24054-0105]", type="주관식",
    stem=stem(r"열린구간 $(-3,\,-2)$"), answer="5",
    general="h=x³+x²−nx+2n, 실근이 하나이고 h→−∞ (x→−∞) 이므로 근의 왼쪽은 음, 오른쪽은 양. 근∈(−3,−2) ⇔ h(−3)<0<h(−2): 5n−18<0, 4n−4>0 → n=2,3 → 5.",
    special="① 끝값 부호만으로 판정 — 실근이 하나라는 전제 덕분. ② 열린구간이라 n=1 (근이 −2) 제외.",
    perspective="실근이 하나인 삼차방정식: 근의 위치 ⇔ 구간 끝값의 부호.",
    table=[
        ("열린구간 (−3,−2)", "근이 끝점인 경우", "닫힌구간이면 n=1 (근 −2) 포함"),
        ("n≤10 (실근 하나)", "n 이 커져 실근이 셋인 경우", "—"),
        ("구간 (−3,−2)", "—", "(−4,−3) 이면 n=4..7 (생존)"),
    ],
    sweep=["h(−2)=4n−4=0 ⇔ n=1", "h(−3)=5n−18"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (근이 구간 끝점인 경우 포함)",
        changed=["열린구간 (−3,−2) → 닫힌구간 [−3,−2]"], naturalness="",
        stem=stem(r"닫힌구간 $[-3,\,-2]$"), answer="6", trap_answer="5",
        trap_path="원문처럼 h(−3)<0<h(−2) 엄격 부등식으로 풀어 n=2,3 → 5 (n=1 이면 근이 −2 로 포함).",
        explanation=[
            r"$h(x)=x^3+x^2-nx+2n$은 실근이 하나이므로 근의 왼쪽에서 $h<0$, 오른쪽에서 $h>0$이다.",
            r"근이 $[-3,\,-2]$에 속하려면 $h(-3)\le0\le h(-2)$, 즉 $5n-18\le0$, $4n-4\ge0$이다.",
            r"함정: $n=1$이면 $h(-2)=0$으로 근이 $-2$ 자체이므로 닫힌구간에 속한다.",
            r"$n=1,\,2,\,3$이므로 합은 $6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 3행 (구간 (−3,−2) → (−4,−3))",
        changed=["열린구간 (−3,−2) → (−4,−3)"], naturalness="",
        stem=stem(r"열린구간 $(-4,\,-3)$"), answer="22", trap_answer=None, trap_path=None,
        explanation=[
            r"$h(x)=x^3+x^2-nx+2n$의 근이 $(-4,\,-3)$에 속하려면 $h(-4)<0<h(-3)$이다.",
            r"$h(-4)=6n-48<0$에서 $n<8$, $h(-3)=5n-18>0$에서 $n>\frac{18}5$이다.",
            r"$n=4,5,6,7$이므로 합은 $22$이다.",
        ],
    ),
]


def ns(cond):
    out = []
    for n in range(1, 11):
        h = x**3 + x**2 - n*x + 2*n
        rr = real_roots(Poly(h, x))
        assert len(set(rr)) == 1
        if cond(rr[0]):
            out.append(n)
    return out


def verify(c):
    c.ans('orig', sum(ns(lambda r: -3 < r < -2)))
    c.ans(1, sum(ns(lambda r: -3 <= r <= -2)))
    c.trap(1, sum(ns(lambda r: -3 < r < -2)))
    c.ans(2, sum(ns(lambda r: -4 < r < -3)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='30', trap_path='h(−4)≤0≤h(−3) 로 등호를 넣어 n=8 까지 포함 → 30 (n=8 이면 근이 −4 로 열린구간 밖).')
VARS[1]['explanation'].insert(-1, '함정: $n=8$이면 근이 정확히 $-4$라 열린구간에 속하지 않는다.')
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, sum(ns(lambda r: -4 <= r < -3)))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '생존형: 원문 풀이가 그대로 통하고 함정이 계산 실수 수준'
