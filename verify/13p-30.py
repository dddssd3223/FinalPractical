from lib import *

ORIG = dict(
    id="13p-30", chapter=1, page=13, num=30, source="2025년 수능완성 [25054-0115]", type="주관식",
    stem=r"양수 $a$와 최고차항의 계수가 $1$인 이차함수 $f(x)$에 대하여 $\displaystyle\lim_{x\to2}\frac{f(x)f(x-a)}{(x-2)^2}=-9$일 때, $f(5)$의 값을 구하시오.",
    answer="18",
    general="분자 N=f(x)f(x−a) 가 x=2 에서 이중 이상 근. (i) f(2)=0, f(2−a)=0 → f=(x−2)(x−2+a), 극한 −a² → a=3, f(5)=18. (ii) f=(x−2)² → 극한 a² ≥0. (iii) f=(x−2+a)² → 극한 a² ≥0. 음수 −9 라 (i)만 가능.",
    special="① 곧바로 f(2)=0 이라 두고 f=(x−2)(x−b) 로 시작 → 극한값이 음수라 우연히 맞음. ② 중근 경우 (ii)(iii)을 검토하지 않음.",
    perspective="N 의 x=2 근 차수를 두 인수 f(x), f(x−a) 에 어떻게 나눠 줄지(1+1, 2+0, 0+2)로 분류.",
    table=[
        ("극한값 −9 (음수)", "중근 경우 (ii)(iii) (극한 a²≥0)", "양수로 바꾸면 (ii)(iii) 두 경우가 살아나고 (i)은 불가"),
        ("a>0", "a=0 (f(x)², 극한 ≥0)", "—"),
        ("최고차 1", "—", "계수가 바뀌면 극한값 스케일만 바뀜"),
    ],
    sweep=["극한값 부호: 음수 → (i), 양수 → (ii)(iii)", "a=0 이면 모든 경우 겹침"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (극한값 부호 → 근 배분 경우)",
        changed=["극한값 −9 → 9", "묻는 값: f(5) 의 모든 값의 합"],
        naturalness="바꾼 조건은 극한값의 부호 하나. 두 경우가 생겨 묻는 값을 '모든 값의 합'으로 바꾼 것은 필수.",
        stem=r"양수 $a$와 최고차항의 계수가 $1$인 이차함수 $f(x)$에 대하여 $\displaystyle\lim_{x\to2}\frac{f(x)f(x-a)}{(x-2)^2}=9$일 때, $f(5)$의 값이 될 수 있는 모든 값의 합을 구하시오.",
        answer="45", trap_answer="9",
        trap_path="원문처럼 f(2)=0 을 먼저 두고 (i)이 안 되자 f=(x−2)² 하나만 찾아 f(5)=9. f(x−a) 쪽이 중근을 갖는 f=(x+1)² 을 놓침.",
        explanation=[
            r"분자 $f(x)f(x-a)$가 $x=2$에서 이중 이상의 근을 가져야 한다.",
            r"(i) $f(x)=(x-2)(x-2+a)$: 극한 $-a^2<0$ 이므로 불가.",
            r"(ii) $f(x)=(x-2)^2$: 극한 $a^2=9$, $a=3$ → $f(5)=9$",
            r"(iii) $f(x-a)=(x-2)^2$, 즉 $f(x)=(x+1)^2$: 극한 $f(2)=9$ ($a=3$) → $f(5)=36$. 함정: 이 경우를 놓치기 쉽다.",
            r"따라서 합은 $9+36=45$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 3행 (극한값 −9 → −4, 음수 유지)",
        changed=["극한값 −9 → −4"], naturalness="",
        stem=r"양수 $a$와 최고차항의 계수가 $1$인 이차함수 $f(x)$에 대하여 $\displaystyle\lim_{x\to2}\frac{f(x)f(x-a)}{(x-2)^2}=-4$일 때, $f(5)$의 값을 구하시오.",
        answer="15", trap_answer=None, trap_path=None,
        explanation=[
            r"분자가 $x=2$에서 이중 이상의 근을 가져야 하고, 극한이 음수이므로 중근 경우는 불가능하다.",
            r"$f(2)=0$, $f(2-a)=0$에서 $f(x)=(x-2)(x-2+a)$이다.",
            r"극한은 $a\times(-a)=-a^2=-4$이므로 $a=2$, $f(x)=x(x-2)$이다.",
            r"따라서 $f(5)=15$이다.",
        ],
    ),
]


def sols(value):
    p, q = symbols('p q', real=True)
    a = Symbol('a', positive=True)
    f = x**2 + p*x + q
    N = expand(f * f.subs(x, x - a))
    eqs = [N.subs(x, 2), diff(N, x).subs(x, 2), diff(N, x, 2).subs(x, 2)/2 - value]
    out = []
    for s in solve(eqs, [p, q, a], dict=True):
        if s[a].is_positive:
            fs = f.subs(s)
            if limit(fs*fs.subs(x, x - s[a])/(x - 2)**2, x, 2) == value:
                out.append((expand(fs), s[a]))
    return out


def verify(c):
    r = sols(-9)
    c.check("원문: 해 하나", len({F for F, a in r}) == 1)
    c.ans('orig', r[0][0].subs(x, 5))
    r = sols(9)
    Fs = {F for F, a in r}
    c.check("1: 해 두 개 (x−2)², (x+1)²", Fs == {expand((x - 2)**2), expand((x + 1)**2)})
    c.ans(1, sum(F.subs(x, 5) for F in Fs))
    c.trap(1, expand((x - 2)**2).subs(x, 5))
    r = sols(-4)
    c.check("2: 해 하나", len({F for F, a in r}) == 1)
    c.ans(2, r[0][0].subs(x, 5))
