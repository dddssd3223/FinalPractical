from lib import *

ORIG = dict(
    id="11p-24", chapter=1, page=11, num=24, source="2025년 수능완성 [25054-0112]", type="객관식",
    stem=r"양수 $a$에 대하여 함수 $f(x)=|x(x-a)|$가 $\displaystyle\lim_{x\to0}\frac{f(x)f(-x)}{x^2}=\frac12$을 만족시킬 때, $\displaystyle\lim_{x\to a+}\frac{f(x)f(-x)}{x-a}$의 값은?",
    choices=["-sqrt(2)", "-1", "sqrt(2)/2", "1", "sqrt(2)"], answer="sqrt(2)/2",
    general="f(x)f(−x)=x²|x−a||x+a|. x→0 이면 a²=1/2, a=√2/2. x→a+ 에서 |x−a|/(x−a)=1 이므로 극한 = a²·2a = 2a³ = √2/2.",
    special="① |x−a|/(x−a) 를 부호 확인 없이 1 로 둠(우극한이라 통함, 좌극한이면 −1). ② 절댓값 밖 인수가 없어 f(x)f(−x)≥0 이 자동(절댓값이 일부만 씌워지면 부호가 생김).",
    perspective="절댓값 인수는 |x−a|/(x−a)=sgn(x−a) 로 떼어 내고 나머지는 대입.",
    table=[
        ("x→a+ (우극한)", "좌극한일 때 부호 −1", "a− 로 바꾸면 부호 반전"),
        ("f 전체에 절댓값", "절댓값 밖 인수의 부호", "f=x|x−a| 면 f(x)f(−x)=−x²|x²−a²| 로 부호가 붙음"),
        ("a>0", "a<0 인 경우", "식 x²|x²−a²| 는 a 부호 무관 → 답 불변"),
    ],
    sweep=["x=a 에서 |x−a| 부호 전환", "a=0 이면 첫 극한 0 (조건 불성립)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 (절댓값 밖 인수 x 의 부호)",
        changed=["f=|x(x−a)| → f=x|x−a|", "첫 극한값 1/2 → −1/2"],
        naturalness="절댓값 범위를 줄이면 f(x)f(−x) 의 부호가 음이 되어 극한값도 음수여야 함 → 두 번째 변경은 첫 번째의 필연적 결과.",
        stem=r"양수 $a$에 대하여 함수 $f(x)=x|x-a|$가 $\displaystyle\lim_{x\to0}\frac{f(x)f(-x)}{x^2}=-\frac12$을 만족시킬 때, $\displaystyle\lim_{x\to a+}\frac{f(x)f(-x)}{x-a}$의 값은?",
        choices=["-sqrt(2)", "-sqrt(2)/2", "0", "sqrt(2)/2", "sqrt(2)"], answer="-sqrt(2)/2", trap_answer="sqrt(2)/2",
        trap_path="f(−x)=(−x)|−x−a| 의 −x 부호를 빠뜨려 f(x)f(−x)=x²|x−a||x+a| 로 계산 → √2/2.",
        explanation=[
            r"$f(-x)=-x|-x-a|=-x|x+a|$이므로 $f(x)f(-x)=-x^2|x-a||x+a|$이다.",
            r"$\displaystyle\lim_{x\to0}\frac{f(x)f(-x)}{x^2}=-a^2=-\frac12$에서 $a=\frac{\sqrt2}{2}$이다.",
            r"함정: 절댓값 밖의 $-x$ 때문에 부호가 음이 된다. 원문처럼 전부 절댓값이라 보면 부호를 잃는다.",
            r"$x\to a+$에서 $\frac{|x-a|}{x-a}=1$이므로 극한은 $-a^2\cdot2a=-2a^3=-\frac{\sqrt2}{2}$이다.",
        ],
    ),
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (한쪽 극한 방향: |x−a|/(x−a) 의 부호)",
        changed=["첫 극한값 1/2 → 4", "x→a+ → x→a−"],
        naturalness="극한값 변경은 답을 원문과 구분하기 위한 수치 조정, 실질 변경은 극한 방향 하나.",
        stem=r"양수 $a$에 대하여 함수 $f(x)=|x(x-a)|$가 $\displaystyle\lim_{x\to0}\frac{f(x)f(-x)}{x^2}=4$를 만족시킬 때, $\displaystyle\lim_{x\to a-}\frac{f(x)f(-x)}{x-a}$의 값은?",
        choices=["-16", "-8", "0", "8", "16"], answer="-16", trap_answer="16",
        trap_path="원문처럼 |x−a|/(x−a)=1 로 두어 2a³=16.",
        explanation=[
            r"$f(x)f(-x)=x^2|x-a||x+a|$이므로 $\displaystyle\lim_{x\to0}\frac{f(x)f(-x)}{x^2}=a^2=4$, $a=2$이다.",
            r"$x\to a-$이면 $x-a<0$이므로 $\frac{|x-a|}{x-a}=-1$이다.",
            r"함정: 우극한이던 원문과 달리 부호가 $-1$이다.",
            r"극한은 $-a^2\cdot 2a=-2a^3=-16$이다.",
        ],
    ),
]


def solve_a(fexpr, target):
    a = Symbol('a', positive=True)
    F = fexpr(a)
    prod = F * F.subs(x, -x)
    sols = [s for s in solve(Eq(limit(prod / x**2, x, 0), target), a)]
    return a, prod, sols


def verify(c):
    a, prod, sols = solve_a(lambda a: Abs(x*(x - a)), Rational(1, 2))
    c.check("원문 a 유일", len(sols) == 1)
    av = sols[0]
    c.ans('orig', limit(prod.subs(a, av) / (x - av), x, av, '+'))

    a, prod, sols = solve_a(lambda a: x*Abs(x - a), -Rational(1, 2))
    c.check("1: a 유일", len(sols) == 1)
    av = sols[0]
    c.ans(1, limit(prod.subs(a, av) / (x - av), x, av, '+'))
    wrong = (x**2*Abs(x - a)*Abs(x + a)).subs(a, av)
    c.trap(1, limit(wrong / (x - av), x, av, '+'))

    a, prod, sols = solve_a(lambda a: Abs(x*(x - a)), 4)
    c.check("2: a=2 유일", sols == [2])
    av = sols[0]
    c.ans(2, limit(prod.subs(a, av) / (x - av), x, av, '-'))
    c.trap(2, limit(prod.subs(a, av) / (x - av), x, av, '+'))
