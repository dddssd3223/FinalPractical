from lib import *

def stem(mono, dist):
    return (r"양의 실수 전체의 집합에서 " + mono + r"하는 함수 $f(x)$가 $x=1$에서 미분가능하다. $1$보다 큰 모든 실수 $a$에 대하여 점 $(1,\,f(1))$과 점 $(a,\,f(a))$ 사이의 거리가 $"
            + dist + r"$일 때, $f'(1)$의 값은?")

ORIG = dict(
    id="73p-59", chapter=3, page=73, num=59, source="2013학년도 수능 6월 모의평가 가형 16번", type="객관식",
    stem=stem("증가", "a^2-1"), choices=["1", "sqrt(5)/2", "sqrt(6)/2", "sqrt(2)", "sqrt(3)"], answer="sqrt(3)",
    general="(a−1)²+(f(a)−f(1))²=(a²−1)² → {(f(a)−f(1))/(a−1)}² = (a+1)²−1 → a→1+: f'(1)²=3. 증가 → f'(1)≥0 → √3.",
    special="① 제곱에서 부호를 잃음 — 증가/감소 조건이 부호를 정함.",
    perspective="거리식 → 평균변화율² → 극한.",
    table=[
        ("증가 (f'(1)≥0)", "감소 (f'(1)≤0)", "감소면 −√3"),
        ("거리 a²−1", "—", "a³−1 이면 (a²+a+1)²−1→8, 2√2 (생존)"),
    ],
    sweep=["거리 d(a): f'(1)² = lim (d/(a−1))² − 1"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (제곱에서 잃은 부호를 단조성이 정함)",
        changed=["증가 → 감소"], naturalness="",
        stem=stem("감소", "a^2-1"), choices=["-sqrt(3)", "-sqrt(2)", "-1", "sqrt(2)", "sqrt(3)"], answer="-sqrt(3)", trap_answer="sqrt(3)",
        trap_path="원문처럼 제곱근의 양수 쪽을 택해 √3 (감소함수라 평균변화율이 음수).",
        explanation=[
            r"$(a-1)^2+\{f(a)-f(1)\}^2=(a^2-1)^2$에서 $\left\{\dfrac{f(a)-f(1)}{a-1}\right\}^2=(a+1)^2-1$이다.",
            r"$a\to1+$이면 $\{f'(1)\}^2=3$이다.",
            r"함정: $f$가 감소하므로 $\dfrac{f(a)-f(1)}{a-1}<0$, 따라서 $f'(1)=-\sqrt3$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (거리 a²−1 → a³−1)",
        changed=["거리 a²−1 → a³−1"], naturalness="",
        stem=stem("증가", "a^3-1"), choices=["2", "sqrt(6)", "2*sqrt(2)", "3", "2*sqrt(3)"], answer="2*sqrt(2)", trap_answer=None, trap_path=None,
        explanation=[
            r"$\left\{\dfrac{f(a)-f(1)}{a-1}\right\}^2=\dfrac{(a^3-1)^2}{(a-1)^2}-1=(a^2+a+1)^2-1$이다.",
            r"$a\to1+$이면 $\{f'(1)\}^2=9-1=8$이다.",
            r"증가함수이므로 $f'(1)=2\sqrt2$이다.",
        ],
    ),
]


def fp1(dist, sgn):
    a = Symbol('a', positive=True)
    sq = limit((dist(a)**2 - (a - 1)**2)/(a - 1)**2, a, 1, '+')
    v = sgn*sqrt(sq)
    # 존재 확인: f(x)=f(1)+sgn·(x−1)·√(d²/(x−1)²−1) (x>1), f=v(x−1) (x≤1) 이 단조·거리 조건 만족
    slope = sgn*sqrt(cancel((dist(a)**2 - (a - 1)**2)/(a - 1)**2))
    g = (a - 1)*slope
    ok = all(simplify((t - 1)**2 + g.subs(a, t)**2 - dist(Integer(t))**2) == 0 for t in (2, 3, 5))
    mono = all((g.subs(a, t + 1) - g.subs(a, t))*sgn > 0 for t in (1, 2, 3))
    return v, ok and mono


def verify(c):
    v, ok = fp1(lambda a: a**2 - 1, 1)
    c.check("원문: 예시 함수 존재", ok)
    c.ans('orig', v)
    v, ok = fp1(lambda a: a**2 - 1, -1)
    c.check("1: 예시 함수 존재", ok)
    c.ans(1, v)
    c.trap(1, fp1(lambda a: a**2 - 1, 1)[0])
    v, ok = fp1(lambda a: a**3 - 1, 1)
    c.check("2: 예시 함수 존재", ok)
    c.ans(2, v)


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[0]['drop'] = '부호만 바뀌는 쉬운 변형'
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
