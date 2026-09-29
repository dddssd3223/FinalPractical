from lib import *

def stem(ineq):
    return r"모든 자연수 $k$에 대하여 두 곡선 $y=x^3+k$, $y=2x^2-2x$는 한 점에서만 만난다. 두 곡선의 교점의 $x$좌표를 $a_k$라 할 때, $" + ineq + r"$이 되도록 하는 자연수 $k$의 개수는?"

ORIG = dict(
    id="37p-21", chapter=2, page=37, num=21, source="2023년 수능특강 [23009-0038]", type="객관식",
    stem=stem(r"-2<a_k<-1"), choices=["10", "12", "14", "16", "18"], answer="14",
    general="h=x³−2x²+2x+k, h'=3x²−4x+2>0 → 증가, 근 하나. −2<a_k<−1 ⇔ h(−2)<0<h(−1): k−20<0, k−5>0 → k=6,…,19 (14개).",
    special="① 사잇값 정리로 부호만 비교 — h 가 증가함수라 근이 하나뿐이어서 충분. ② 부등호가 엄격이라 k=5, 20 제외.",
    perspective="증가함수의 근의 위치 ⇔ 구간 양 끝 부호.",
    table=[
        ("엄격부등식 −2<a_k<−1", "a_k 가 구간 끝과 같은 경우", "≤ 로 바꾸면 k=5, 20 포함 → 16"),
        ("구간 (−2,−1)", "—", "(−3,−2) 이면 21≤k≤50 (생존)"),
    ],
    sweep=["h(−2)=k−20, h(−1)=k−5 의 부호 경계"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (경계값 포함 여부)",
        changed=["−2<a_k<−1 → −2≤a_k≤−1"], naturalness="",
        stem=stem(r"-2\le a_k\le-1"), choices=["12", "14", "15", "16", "18"], answer="16", trap_answer="14",
        trap_path="원문처럼 h(−2)<0<h(−1) 로 엄격 부등식을 써서 14 (a_k=−2, −1 인 k=20, 5 누락).",
        explanation=[
            r"$h(x)=x^3-2x^2+2x+k$는 $h'(x)=3x^2-4x+2>0$이라 증가함수이고 근이 하나이다.",
            r"$-2\le a_k\le-1\iff h(-2)\le0\le h(-1)\iff k-20\le0\le k-5$이다.",
            r"함정: $k=5$이면 $a_k=-1$, $k=20$이면 $a_k=-2$로 등호가 성립하므로 포함한다.",
            r"$k=5,\,6,\,\ldots,\,20$의 $16$개이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (구간 (−2,−1) → (−3,−2))",
        changed=["−2<a_k<−1 → −3<a_k<−2"], naturalness="",
        stem=stem(r"-3<a_k<-2"), choices=["28", "29", "30", "31", "32"], answer="30", trap_answer=None, trap_path=None,
        explanation=[
            r"$h(x)=x^3-2x^2+2x+k$는 증가함수이다.",
            r"$h(-3)=k-51<0$, $h(-2)=k-20>0$이어야 하므로 $20<k<51$이다.",
            r"$k=21,\ldots,50$의 $30$개이다.",
        ],
    ),
]

h = lambda k: x**3 - 2*x**2 + 2*x + k


def root(k):
    r = real_roots(Poly(h(k), x))
    assert len(r) == 1
    return r[0]


def verify(c):
    c.check("h'>0 (판별식 음수)", discriminant(3*x**2 - 4*x + 2, x) < 0)
    ks = range(1, 101)
    c.ans('orig', sum(1 for k in ks if -2 < root(k) < -1))
    c.ans(1, sum(1 for k in ks if -2 <= root(k) <= -1))
    c.trap(1, sum(1 for k in ks if -2 < root(k) < -1))
    c.ans(2, sum(1 for k in ks if -3 < root(k) < -2))
