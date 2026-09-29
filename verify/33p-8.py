from lib import *

def G(l, r):
    return r"함수 $g(x)=\begin{cases}" + l + r" & (x<1)\\ \dfrac{1}{f(x)} & (1\le x\le3)\\ " + r + r" & (x>3)\end{cases}$"

ORIG = dict(
    id="33p-8", chapter=2, page=33, num=8, source="2023년 수능완성 [23054-0116]", type="주관식",
    stem=r"이차항의 계수가 양수인 이차함수 $f(x)$에 대하여 " + G(r"\frac12", r"\frac16") + r"가 실수 전체의 집합에서 연속이다. 함수 $y=f(x)$의 그래프가 $y$축과 만나는 점의 좌표를 $(0,\,k)$라 할 때, 자연수 $k$의 최댓값을 구하시오.",
    answer="11",
    general="f(1)=2, f(3)=6, [1,3] 에서 f>0. f=a(x−1)(x−3)+2x (a>0). a≥1 이면 꼭짓점 2−1/a ∈[1,3], 최솟값 4−a−1/a>0 ⇔ a<2+√3. k=f(0)=3a<6+3√3≈11.2 → 11.",
    special="① [1,3] 에서 f>0 확인 — 끝값만 맞추면 1/f 가 구간 안에서 끊길 수 있음. ② 부등식이 엄격(<)이라 경계값을 뺌(원문은 경계가 무리수라 드러나지 않음).",
    perspective="k=f(0) 를 a 로 나타내고 '구간 안 최솟값 >0' 으로 a 범위.",
    table=[
        ("[1,3] 에서 f>0 (판별식은 꼭짓점이 구간 안일 때만 필요)", "꼭짓점이 구간 밖 (a 가 작을 때)", "양 끝 4, 9 로 두고 k 개수를 물으면 판별식이 a≤1/4 쪽을 잘못 잘라 18 (실제 19)"),
        ("이차항 계수 양수", "음수(항상 양수)", "—"),
        ("왼쪽 1/2", "—", "1/4 이면 f(1)=4, a 범위만 바뀜 (생존)"),
    ],
    sweep=["꼭짓점 2−1/a ∈ [1,3] ⇔ a≥1", "최솟값 4−a−1/a=0 ⇔ a=2±√3"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-C (꼭짓점이 [1,3] 밖이면 판별식 조건이 필요 없음)",
        changed=["x<1 조각 1/2 → 1/4", "x>3 조각 1/6 → 1/9", "묻는 값: k 의 최댓값 → 자연수 k 의 개수"],
        naturalness="최댓값만 물으면 원문처럼 판별식 하나로 풀리므로, 판별식이 너무 세게 자르는 아래쪽(a 가 작을 때)까지 드러나도록 개수를 묻고 양 끝 값을 맞춘 것.",
        stem=r"이차항의 계수가 양수인 이차함수 $f(x)$에 대하여 " + G(r"\frac14", r"\frac19") + r"가 실수 전체의 집합에서 연속이다. 함수 $y=f(x)$의 그래프가 $y$축과 만나는 점의 좌표를 $(0,\,k)$라 할 때, 가능한 자연수 $k$의 개수를 구하시오.",
        answer="19", trap_answer="18",
        trap_path="원문처럼 'f(x)=0 이 실근이 없다' (판별식<0) 로 풀어 1/4<a<25/4 → 9/4<k<81/4 → 3~20 의 18개 (a≤5/4 이면 꼭짓점이 x<1 이라 [1,3] 에서 f≥f(1)=4>0, 판별식과 무관).",
        explanation=[
            r"연속이려면 $f(1)=4$, $f(3)=9$이고 $1\le x\le3$에서 $f(x)>0$이므로 $f(x)=a(x-1)(x-3)+\frac{5x+3}2$ ($a>0$), $k=3a+\frac32$이다.",
            r"꼭짓점은 $x=2-\frac5{4a}$이다. $a<\frac54$이면 꼭짓점이 $1$보다 왼쪽이라 $[1,3]$에서 $f$는 증가하고 $f\ge f(1)=4>0$이다.",
            r"$a\ge\frac54$이면 최솟값 $\frac{13}2-a-\frac{25}{16a}>0$에서 $a<\frac{25}4$이다. 따라서 $0<a<\frac{25}4$, $\frac32<k<\frac{81}4$이다.",
            r"함정: 판별식 $<0$을 쓰면 $a>\frac14$까지 잘라 $k=2$를 놓친다 ($a=\frac16$이면 $k=2$이고 조건을 만족).",
            r"자연수 $k$는 $2,3,\ldots,20$의 $19$개이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 3행 (x<1 조각 1/2 → 1/4)",
        changed=["x<1 조각 1/2 → 1/4"], naturalness="",
        stem=r"이차항의 계수가 양수인 이차함수 $f(x)$에 대하여 " + G(r"\frac14", r"\frac16") + r"가 실수 전체의 집합에서 연속이다. 함수 $y=f(x)$의 그래프가 $y$축과 만나는 점의 좌표를 $(0,\,k)$라 할 때, 자연수 $k$의 최댓값을 구하시오.",
        answer="17", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(1)=4$, $f(3)=6$이므로 $f(x)=a(x-1)(x-3)+x+3$ ($a>0$)이다.",
            r"$a\ge\frac12$이면 꼭짓점 $x=2-\frac1{2a}$가 $[1,3]$에 있고 최솟값 $5-a-\frac1{4a}>0$에서 $4a^2-20a+1<0$, $a<\frac{5+2\sqrt6}{2}$이다.",
            r"$k=3a+3<\frac{21+6\sqrt6}{2}\approx17.8$이므로 자연수 $k$의 최댓값은 $17$이다.",
        ],
    ),
]


def k_sup(p, q):
    """f(1)=p, f(3)=q, [1,3] 에서 f>0, a>0 일 때 k=f(0) 의 상한(도달 불가)"""
    a = Symbol('a', positive=True)
    L = p + (q - p)*(x - 1)/2
    f = a*(x - 1)*(x - 3) + L
    xv = solve(diff(f, x), x)[0]
    mn = simplify(f.subs(x, xv))
    bounds = [s for s in solve(Eq(mn, 0), a) if s.is_positive]
    amax = max(b for b in bounds if (xv.subs(a, b) - 1) >= 0 and (3 - xv.subs(a, b)) >= 0)
    return f, a, amax, simplify(f.subs(x, 0).subs(a, amax))


def valid(f, a, av):
    """[1,3] 에서 f>0 (정확한 최솟값: 끝점과 구간 안 꼭짓점)"""
    fv = f.subs(a, av)
    pts = [Integer(1), Integer(3)] + [r for r in solve(diff(fv, x), x) if 1 <= r <= 3]
    return min(simplify(fv.subs(x, r)) for r in pts) > 0


def max_nat_k(p, q):
    f, a, amax, ksup = k_sup(p, q)
    kmax = ceiling(ksup) - 1 if ksup.is_integer else floor(ksup)
    av = solve(Eq(f.subs(x, 0), kmax), a)[0]
    return f, a, amax, ksup, kmax, valid(f, a, av), valid(f, a, amax)


def verify(c):
    for key, p, q in (('orig', 2, 6), (2, 4, 6)):
        f, a, amax, ksup, kmax, ok_k, ok_sup = max_nat_k(p, q)
        c.check(f"{key}: 최대 k 에서 [1,3] f>0, 상한 a 에서는 f 가 0 에 닿음", ok_k and not ok_sup)
        c.ans(key, kmax)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'


def k_range_count(p, q, disc_only):
    """자연수 k 개수: 실제 조건([1,3] 에서 f>0) 또는 판별식<0 조건"""
    a = Symbol('a', positive=True)
    f = a*(x - 1)*(x - 3) + p + Rational(q - p, 2)*(x - 1)
    k = f.subs(x, 0)
    cnt = 0
    for kk in range(1, 200):
        av = solve(Eq(k, kk), a)
        if not av or not av[0].is_positive:
            continue
        av = av[0]
        fv = f.subs(a, av)
        if disc_only:
            A, B, C = Poly(expand(fv), x).all_coeffs()
            ok = B**2 - 4*A*C < 0
        else:
            pts = [Integer(1), Integer(3)] + [r for r in solve(diff(fv, x), x) if 1 <= r <= 3]
            ok = min(fv.subs(x, r) for r in pts) > 0
        cnt += bool(ok)
    return cnt


_verify_base = verify


def verify(c):
    _verify_base(c)
    c.ans(1, k_range_count(4, 9, False))
    c.trap(1, k_range_count(4, 9, True))
