from lib import *

def stem(mid):
    return (r"최고차항의 계수가 $1$인 삼차함수 $f(x)$가 모든 정수 $k$에 대하여 $2k-8\le " + mid + r"\le 4k^2+14k$를 만족시킬 때, $f'(3)$의 값을 구하시오.")

ORIG = dict(
    id="75p-63", chapter=3, page=75, num=63, source="2025학년도 수능 9월 모의평가 21번", type="주관식",
    stem=stem(r"\frac{f(k+2)-f(k)}{2}"), answer="31",
    general="D(k)=(f(k+2)−f(k))/2. 위 여유 U=4k²+14k−D, 아래 여유 L=D−(2k−8), U+L=4(k+1)(k+2) → k=−1,−2 에서 U=L=0. U 는 최고차 1 인 이차 → U=(k+1)(k+2) → D=3k²+11k−2. f=x³+px²+qx: D=3k²+(6+2p)k+4+2p+q → p=5/2, q=−11 → f'(3)=31.",
    special="① 합 U+L 이 정수 k=−1,−2 에서 0 — 두 여유가 모두 0 이 되어 D 가 결정. ② (f(k+2)−f(k))/2 = f'(k+1)+1 (삼차의 셋째 항) — 미분계수와 1 차이.",
    perspective="위·아래 경계의 차가 정수에서 0 이 되는 점을 찾기.",
    table=[
        ("가운데 식이 평균변화율 (f'(k+1)+1)", "가운데가 f'(k+1)", "f'(k+1) 로 바꾸면 f'(3)=D(2)=32"),
        ("구간 폭 2", "—", "f(k+1)−f(k) 면 p=4, q=−7 → 44 (생존)"),
    ],
    sweep=["U+L=4(k+1)(k+2) 의 정수 근 −1, −2"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (평균변화율 ≠ 가운데 점의 미분계수, 차이 1)",
        changed=["(f(k+2)−f(k))/2 → f'(k+1)"], naturalness="",
        stem=stem(r"f'(k+1)"), answer="32", trap_answer="31",
        trap_path="평균변화율과 f'(k+1) 을 같은 것으로 보아 원문의 f 를 그대로 써서 31.",
        explanation=[
            r"$U=4k^2+14k-f'(k+1)$, $L=f'(k+1)-(2k-8)$이라 하면 $U+L=4(k+1)(k+2)$이다.",
            r"$k=-1,-2$에서 $U+L=0$이고 $U,L\ge0$이므로 $U=L=0$, $U$는 최고차항 계수 $1$인 이차식이라 $U=(k+1)(k+2)$이다.",
            r"$f'(k+1)=3k^2+11k-2$이고, 이는 정수에서 $L=3(k+1)(k+2)\ge0$도 만족한다.",
            r"함정: 원문의 $\frac{f(k+2)-f(k)}2$는 $f'(k+1)+1$이라 값이 $1$ 다르다. $f'(3)=f'(2+1)=12+22-2=32$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (구간 폭 2 → 1)",
        changed=["(f(k+2)−f(k))/2 → f(k+1)−f(k)"], naturalness="",
        stem=stem(r"f(k+1)-f(k)"), answer="44", trap_answer=None, trap_path=None,
        explanation=[
            r"$D(k)=f(k+1)-f(k)$에 대해 두 여유의 합은 $4(k+1)(k+2)$이므로 $D(k)=4k^2+14k-(k+1)(k+2)=3k^2+11k-2$이다.",
            r"$f=x^3+px^2+qx+r$이면 $D(k)=3k^2+(3+2p)k+1+p+q$이므로 $p=4$, $q=-7$이다.",
            r"$f'(3)=27+24-7=44$이다.",
        ],
    ),
]


def solve_fp3(mid):
    p, q, r = symbols('p q r')
    k = Symbol('k')
    f = x**3 + p*x**2 + q*x + r
    D = expand(mid(f, k))
    U = expand(4*k**2 + 14*k - D)
    L = expand(D - (2*k - 8))
    S = factor(U + L)
    zs = [z for z in solve(S, k) if z.is_integer]
    assert len(zs) == 2  # 정수에서 합이 0 → U=L=0 강제
    sol = solve([U.subs(k, z) for z in zs] + [L.subs(k, z) for z in zs], [p, q], dict=True)
    assert len(sol) == 1
    Us, Ls = U.subs(sol[0]), L.subs(sol[0])
    ok = all(Us.subs(k, t) >= 0 and Ls.subs(k, t) >= 0 for t in range(-60, 61))
    # 강제 조건만으로 p, q 가 정해지므로 유일
    return diff(f, x).subs(x, 3).subs(sol[0]), ok


def verify(c):
    avg2 = lambda f, k: (f.subs(x, k + 2) - f.subs(x, k))/2
    v, ok = solve_fp3(avg2)
    c.check("원문: 모든 정수 조건 만족", ok)
    c.ans('orig', v)
    v, ok = solve_fp3(lambda f, k: diff(f, x).subs(x, k + 1))
    c.check("1: 조건 만족", ok)
    c.ans(1, v)
    c.trap(1, solve_fp3(avg2)[0])
    v, ok = solve_fp3(lambda f, k: f.subs(x, k + 1) - f.subs(x, k))
    c.check("2: 조건 만족", ok)
    c.ans(2, v)
