from lib import *
from itertools import product

def box(ns):
    return [r"(가) $5$ 이하의 모든 자연수 $n$에 대하여 $\displaystyle\sum_{k=1}^{n}f(k)=f(n)f(n+1)$이다.",
            r"(나) $n=" + ns + r"$일 때, $f(x)$에서 $x$의 값이 $n$에서 $n+2$까지 변할 때의 평균변화율은 양수가 아니다."]

HEAD = r"사차함수 $f(x)$가 다음 조건을 만족시킨다. "

ORIG = dict(
    id="77p-67", chapter=3, page=77, num=67, source="2019학년도 수능 6월 모의평가 나형 30번", type="주관식",
    stem=HEAD + r"$128\times f\left(\frac52\right)$의 값을 구하시오.", box=box("3,\\,4"), answer="65",
    general="(가)를 이웃한 n 끼리 빼면 f(n){f(n+1)−f(n−1)−1}=0 (n=2..5), n=1: f(1){1−f(2)}=0. 각 n 에서 f(n)=0 또는 f(n+1)=f(n−1)+1 로 분기 → 사차가 되는 경우 중 (나) f(5)≤f(3), f(6)≤f(4) 를 만족하는 것은 f(1..6)=−1,1,0,0,0,−6 뿐 → f=−(x−3)(x−4)(x−5)(5x−6)/24 → 128f(5/2)=65.",
    special="① (나)는 분기 중 하나를 고르는 조건 — 비교하는 n 이 바뀌면 다른 가지가 선택됨.",
    perspective="점화 관계의 분기 + 평균변화율 부등식으로 가지치기.",
    table=[
        ("(나) n=3,4", "(나) n=1,2 (다른 가지)", "n=1,2 면 f(1..5)=0,0,0,0,1/5 → f(8)=7"),
        ("(나) n=3,4", "—", "n=2,3 이어도 같은 f → 128f(3/2)=105 (생존)"),
    ],
    sweep=["분기 2^5 가지 중 사차가 되는 것 10개"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 ((나)가 고르는 가지 변경)",
        changed=["(나) n=3,4 → n=1,2", "묻는 값 128f(5/2) → f(8)"],
        naturalness="(나)를 바꾸면 f=(x−1)(x−2)(x−3)(x−4)/120 이 되어 128f(5/2) 가 분수가 되므로 f(8) 을 묻는다.",
        stem=HEAD + r"$f(8)$의 값을 구하시오.", box=box("1,\\,2"), answer="7", trap_answer="-85",
        trap_path="원문의 가지 f(1..6)=−1,1,0,0,0,−6 을 그대로 써서 f(8)=−85 (이 f 는 f(3)=0>f(1)=−1 이라 새 (나) 위반).",
        explanation=[
            r"(가)에서 $n=1$: $f(1)\{1-f(2)\}=0$, $n\ge2$: $f(n)\{f(n+1)-f(n-1)-1\}=0$이다.",
            r"각 $n$에서 $f(n)=0$ 또는 $f(n+1)=f(n-1)+1$로 나뉘고, 사차함수가 되는 가지 중 (나) $f(3)\le f(1)$, $f(4)\le f(2)$를 만족하는 것은 $f(1)=f(2)=f(3)=f(4)=0$, $f(5)=\frac15$, $f(6)=1$뿐이다.",
            r"함정: 원문의 가지는 $f(3)=0>f(1)=-1$이라 탈락한다.",
            r"$f(x)=\frac1{120}(x-1)(x-2)(x-3)(x-4)$이므로 $f(8)=\frac{7\cdot6\cdot5\cdot4}{120}=7$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 ((나) n=3,4 → n=2,3)",
        changed=["(나) n=3,4 → n=2,3", "묻는 값 128f(5/2) → 128f(3/2)"],
        naturalness="(나)를 바꿔도 같은 f 가 남으므로 답이 달라지도록 묻는 점을 함께 바꾼 것.",
        stem=HEAD + r"$128\times f\left(\frac32\right)$의 값을 구하시오.", box=box("2,\\,3"), answer="105", trap_answer=None, trap_path=None,
        explanation=[
            r"(가)의 분기 중 사차함수이고 $f(4)\le f(2)$, $f(5)\le f(3)$인 것은 $f(1..6)=-1,1,0,0,0,-6$뿐이다.",
            r"$f(x)=-\frac1{24}(x-3)(x-4)(x-5)(5x-6)$이다.",
            r"$128f\left(\frac32\right)=105$이다.",
        ],
    ),
]


def all_quartics():
    A = symbols('a1:7')
    out = set()
    for br in product([0, 1], repeat=5):
        eqs = [A[0] if br[0] == 0 else A[1] - 1]
        for n in range(2, 6):
            eqs.append(A[n - 1] if br[n - 1] == 0 else A[n] - A[n - 2] - 1)
        for s in solve(eqs, A, dict=True):
            v = [a.subs(s) for a in A]
            cs = symbols('c0:5')
            f = sum(ci*x**i for i, ci in enumerate(cs))
            fs = sorted(set().union(*[vv.free_symbols for vv in v]), key=str)
            for t in solve([f.subs(x, k + 1) - v[k] for k in range(6)], list(cs) + fs, dict=True):
                F = expand(f.subs(t))
                assert not (F.free_symbols - {x})
                if F != 0 and degree(F, x) == 4:
                    assert all(sum(F.subs(x, k) for k in range(1, n + 1)) == F.subs(x, n)*F.subs(x, n + 1) for n in range(1, 6))
                    out.add(F)
    return out


def pick(Q, ns):
    return [F for F in Q if all(F.subs(x, n + 2) - F.subs(x, n) <= 0 for n in ns)]


def verify(c):
    Q = all_quartics()
    s = pick(Q, (3, 4))
    c.check("원문: 유일", len(s) == 1)
    c.ans('orig', 128*s[0].subs(x, Rational(5, 2)))
    s1 = pick(Q, (1, 2))
    c.check("1: 유일", len(s1) == 1)
    c.ans(1, s1[0].subs(x, 8))
    c.trap(1, s[0].subs(x, 8))
    s2 = pick(Q, (2, 3))
    c.check("2: 유일", len(s2) == 1)
    c.ans(2, 128*s2[0].subs(x, Rational(3, 2)))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
