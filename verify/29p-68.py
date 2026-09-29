from lib import *

ORIG = dict(
    id="29p-68", chapter=1, page=29, num=68, source="2025학년도 수능 21번", type="주관식",
    stem=r"함수 $f(x)=x^3+ax^2+bx+4$가 다음 조건을 만족시키도록 하는 두 정수 $a$, $b$에 대하여 $f(1)$의 최댓값을 구하시오. [4점]",
    box=[r"모든 실수 $\alpha$에 대하여 $\displaystyle\lim_{x\to\alpha}\frac{f(2x+1)}{f(x)}$의 값이 존재한다."],
    answer="16",
    general="f 의 실근 r 마다 2r+1 도 같은 차수 이상의 근이어야 함 → 실근 집합이 r↦2r+1 에 닫힘 → 고정점 −1 뿐. 상수항 4 → f=(x+1)(x²+px+4), x²+px+4 는 실근 없음: −4<p<4, 정수. f(1)=2(p+5) → p=3 에서 16.",
    special="① 판별식을 ≤0 으로 두어 p=4 포함 → x²+4x+4=(x+2)² 로 실근 −2 가 생겨 조건 위반(−2 ↦ −3 이 근이 아님). ② 고정점 −1 을 추측으로 대입.",
    perspective="근의 궤도 r→2r+1→… 가 유한해야 하므로 고정점만 허용.",
    table=[
        ("판별식 < 0 (p=±4 제외)", "p=±4 (중근 ∓2 가 새 실근)", "최솟값을 물으면 반대쪽 경계 p=−4 가 함정"),
        ("f(2x+1): 고정점 −1", "—", "f(2x+3), 상수항 12 면 고정점 −3 (생존)"),
    ],
    sweep=["p=±4 에서 x²+px+4 가 중근", "a=p+1, b=p+4 정수 ⇔ p 정수"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (판별식 경계 p=−4 에서 새 실근 −… 생김)",
        changed=["묻는 값: f(1) 의 최댓값 → f(−2)+20 의 최솟값"],
        naturalness="묻는 값만 바꿔 반대쪽 경계를 보게 한 것 (+20 은 답을 자연수로 맞추는 조정).",
        stem=r"함수 $f(x)=x^3+ax^2+bx+4$가 다음 조건을 만족시키도록 하는 두 정수 $a$, $b$에 대하여 $f(-2)+20$의 최솟값을 구하시오.",
        box=[r"모든 실수 $\alpha$에 대하여 $\displaystyle\lim_{x\to\alpha}\frac{f(2x+1)}{f(x)}$의 값이 존재한다."],
        answer="6", trap_answer="4",
        trap_path="x²+px+4 의 판별식을 ≤0 으로 두어 p=−4 까지 허용 → f(−2)=−16 → 4 (p=−4 이면 실근 2 가 생겨 2↦5 가 근이 아니므로 위반).",
        explanation=[
            r"$f$의 실근 $r$에 대하여 $2r+1$도 $f$의 근이어야 하므로 실근은 고정점 $-1$뿐이다.",
            r"$f(x)=(x+1)(x^2+px+4)$ ($p$는 정수)이고 $x^2+px+4$는 실근이 없어야 하므로 $-4<p<4$이다.",
            r"함정: $p=-4$이면 $x^2-4x+4=(x-2)^2$로 실근 $2$가 생기고 $2\cdot2+1=5$는 근이 아니다.",
            r"$f(-2)=-(8-2p)=2p-8$은 $p=-3$일 때 최소 $-14$이므로 $f(-2)+20$의 최솟값은 $6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (고정점 −1 → −3)",
        changed=["f(2x+1) → f(2x+3), 상수항 4 → 12"], naturalness="고정점을 옮기면서 정수 조건이 유지되도록 상수항을 함께 맞춘 한 가지 변경.",
        stem=r"함수 $f(x)=x^3+ax^2+bx+12$가 다음 조건을 만족시키도록 하는 두 정수 $a$, $b$에 대하여 $f(1)$의 최댓값을 구하시오.",
        box=[r"모든 실수 $\alpha$에 대하여 $\displaystyle\lim_{x\to\alpha}\frac{f(2x+3)}{f(x)}$의 값이 존재한다."],
        answer="32", trap_answer=None, trap_path=None,
        explanation=[
            r"실근 $r$에 대하여 $2r+3$도 근이어야 하므로 실근은 고정점 $-3$뿐이다.",
            r"$f(x)=(x+3)(x^2+px+4)$이고 $-4<p<4$인 정수이다.",
            r"$f(1)=4(5+p)$는 $p=3$일 때 최대 $32$이다.",
        ],
    ),
]


def admissible(inner, const, A=range(-12, 13), B=range(-20, 21)):
    """정수 a, b 중 조건을 만족하는 f 목록 (고정밀 수치 근으로 판정).
    일차 안쪽 함수 u(x) 에 대해 f(u(x))/f(x) 의 극한 존재 ⇔ f 의 각 실근 r (차수 m) 에서 u(r) 이 차수 ≥ m 인 근."""
    out = []
    for a in A:
        for b in B:
            f = x**3 + a*x**2 + b*x + const
            real = []  # (실근, 차수): 무평방 분해로 차수를 얻고 각 인수는 수치 근
            for fac, m in sqf_list(f, x)[1]:
                for z in Poly(fac, x).nroots(n=30, maxsteps=500):
                    z = complex(z)
                    if abs(z.imag) < 1e-12:
                        real.append((z.real, m))
            ok = True
            for r, m in real:
                u = float(inner.subs(x, r))
                if not any(abs(z - u) < 1e-9 and mz >= m for z, mz in real):
                    ok = False; break
            if ok:
                out.append(f)
    return out


def spot_check(f, inner):
    return all(lim_exists(f.subs(x, inner)/f, r)[0] for r in set(real_roots(Poly(f, x))))


def verify(c):
    fs = admissible(2*x + 1, 4)
    c.check("원문: 모두 (x+1)(x²+px+4), |p|<4 (7개)", all(rem(f, x + 1, x) == 0 for f in fs) and len(fs) == 7)
    c.check("원문: 극한으로 직접 재확인", all(spot_check(f, 2*x + 1) for f in fs))
    c.ans('orig', max(f.subs(x, 1) for f in fs))
    c.ans(1, min(f.subs(x, -2) for f in fs) + 20)
    ft = expand((x + 1)*(x**2 - 4*x + 4))
    c.check("1: 함정 f (p=−4) 는 조건 위반", not spot_check(ft, 2*x + 1))
    c.trap(1, ft.subs(x, -2) + 20)
    fs2 = admissible(2*x + 3, 12)
    c.check("2: 모두 (x+3)(x²+px+4), |p|<4 (7개)", all(rem(f, x + 3, x) == 0 for f in fs2) and len(fs2) == 7)
    c.ans(2, max(f.subs(x, 1) for f in fs2))
