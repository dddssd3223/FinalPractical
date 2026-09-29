from lib import *

def box(pts, lim):
    return [r"(가) 함수 $\dfrac{x}{f(x)}$는 " + pts + r"에서 불연속이다.", r"(나) $" + lim + r"$"]

ORIG = dict(
    id="45p-44", chapter=2, page=45, num=44, source="2019학년도 수능 6월 모의평가 나형 28번", type="주관식",
    stem=r"이차함수 $f(x)$가 다음 조건을 만족시킨다. $f(4)$의 값을 구하시오. [4점]",
    box=box(r"$x=1$, $x=2$", r"\displaystyle\lim_{x\to2}\frac{f(x)}{x-2}=4"),
    answer="24",
    general="x/f 가 불연속 ⇔ f=0 → f(1)=f(2)=0, f=k(x−1)(x−2). (나) k·(2−1)=4 → k=4 → f(4)=4·3·2=24.",
    special="① (나)의 분모가 x−2 라 약분 후 남는 (x−1) 만 대입 — 분모에 다른 인수가 있으면 그 값도 대입해야 함.",
    perspective="분모의 근 ⇔ 불연속점, 약분 후 남은 인수를 모두 대입.",
    table=[
        ("(나) 분모 x−2", "분모의 다른 인수", "x²−4 이면 (x+2)→4 도 대입 → k=16"),
        ("(가) x=1, 2", "—", "x=0, 2 로 바꾸면 f=kx(x−2) (생존)"),
    ],
    sweep=["분모 인수의 x=2 에서의 값"],
)

VARS = [
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (불연속점 1 → 0)",
        changed=["(가) x=1, x=2 → x=0, x=2"], naturalness="",
        stem=r"이차함수 $f(x)$가 다음 조건을 만족시킨다. $f(4)$의 값을 구하시오.",
        box=box(r"$x=0$, $x=2$", r"\displaystyle\lim_{x\to2}\frac{f(x)}{x-2}=4"),
        answer="16", trap_answer=None, trap_path=None,
        explanation=[
            r"$\frac{x}{f(x)}$는 $f(x)=0$인 점에서 정의되지 않아 불연속이므로 $f(0)=f(2)=0$이다.",
            r"$f(x)=kx(x-2)$이고 (나)에서 $2k=4$, $k=2$이다.",
            r"$f(4)=2\times4\times2=16$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 / 3-C 7 (분모의 다른 인수 x+2 대입)",
        changed=["(나) 분모 x−2 → x²−4"], naturalness="",
        stem=r"이차함수 $f(x)$가 다음 조건을 만족시킨다. $f(4)$의 값을 구하시오.",
        box=box(r"$x=1$, $x=2$", r"\displaystyle\lim_{x\to2}\frac{f(x)}{x^2-4}=4"),
        answer="96", trap_answer="24",
        trap_path="원문처럼 k(2−1)=4 로 두어 k=4 → 24 ((x+2)→4 를 빠뜨림).",
        explanation=[
            r"(가)에서 $f(1)=f(2)=0$이므로 $f(x)=k(x-1)(x-2)$이다.",
            r"$\displaystyle\lim_{x\to2}\frac{k(x-1)(x-2)}{(x-2)(x+2)}=\frac{k}{4}=4$이므로 $k=16$이다.",
            r"함정: 약분 후 남는 $x+2$도 $4$로 대입해야 한다.",
            r"$f(4)=16\times3\times2=96$이다.",
        ],
    ),
]


def solve_f(roots, D):
    k = Symbol('k')
    f = k*(x - roots[0])*(x - roots[1])
    kv = solve(Eq(limit(f/D, x, 2), 4), k)[0]
    F = f.subs(k, kv)
    disc = set(real_roots(Poly(F, x)))
    return F, disc == set(roots)


def verify(c):
    F, ok = solve_f((1, 2), x - 2)
    c.check("원문: 불연속점 재확인", ok)
    c.ans('orig', F.subs(x, 4))
    F, ok = solve_f((0, 2), x - 2)
    c.check("1: 불연속점 재확인", ok)
    c.ans(1, F.subs(x, 4))
    F, ok = solve_f((1, 2), x**2 - 4)
    c.check("2: 불연속점 재확인", ok)
    c.ans(2, F.subs(x, 4))
    Ft, _ = solve_f((1, 2), x - 2)
    c.trap(2, Ft.subs(x, 4))
