from lib import *

def stem(cond):
    return (r"함수 $f(x)=x^2-2x+a$와 실수 $t$에 대하여 $x$에 대한 방정식 $|f(x)|=t$의 서로 다른 실근의 개수를 $g(t)$라 하면 " + cond + r" $f(a)$의 값을 구하시오. (단, $a$는 상수이다.)")

ORIG = dict(
    id="43p-35", chapter=2, page=43, num=35, source="2025년 수능특강 [25009-0050]", type="주관식",
    stem=stem(r"함수 $g(t)$는 $t=\alpha$, $t=\beta\,(\alpha<\beta)$에서만 불연속이고 $\alpha+\beta=4$이다."),
    answer="12",
    general="꼭짓점 값 m=a−1. m>0 이면 g 는 t=m 에서만, m=0 이면 t=0 에서만 불연속. m<0 이면 W 모양: t=0 (2개), 0<t<|m| (4개), t=|m| (3개) → t=0, |m| 두 곳에서 불연속. α=0, β=1−a=4 → a=−3, f(−3)=12.",
    special="① 곧바로 W 모양(꼭짓점이 x축 아래)으로 둠 — 불연속점이 두 개라는 조건 때문. 불연속점이 하나로 주어지면 꼭짓점이 x축 위(또는 위)인 경우로 가야 함.",
    perspective="꼭짓점 값 m 의 부호에 따른 g(t) 표.",
    table=[
        ("불연속점 두 개", "꼭짓점이 x축 위/위에 있는 경우 (불연속점 하나)", "'t=2 에서만 불연속'이면 m=2 → a=3"),
        ("α+β=4", "—", "6 이면 a=−5 (생존)"),
    ],
    sweep=["m=a−1 의 부호: >0 (불연속 1개), =0 (1개), <0 (2개)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (꼭짓점이 x축 위인 경우)",
        changed=["'t=α, t=β 에서만 불연속, α+β=4' → 't=2 에서만 불연속'"], naturalness="",
        stem=stem(r"함수 $g(t)$는 $t=2$에서만 불연속이다."), answer="6", trap_answer="2",
        trap_path="원문처럼 W 모양의 극댓값 |m|=2 로 두어 a=−1 → f(−1)=2 (이때는 t=0 에서도 불연속).",
        explanation=[
            r"$f(x)=(x-1)^2+a-1$이고 꼭짓점의 $y$좌표를 $m=a-1$이라 하자.",
            r"$m<0$이면 $g(t)$는 $t=0$과 $t=|m|$ 두 곳에서 불연속이므로 조건에 맞지 않는다. 함정: 원문의 W 모양을 그대로 쓰면 안 된다.",
            r"$m=0$이면 $t=0$에서만 불연속이므로 맞지 않고, $m>0$이면 $t=m$에서만 불연속이므로 $m=2$, $a=3$이다.",
            r"$f(3)=9-6+3=6$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (α+β=4 → 6)",
        changed=["α+β=4 → 6"], naturalness="",
        stem=stem(r"함수 $g(t)$는 $t=\alpha$, $t=\beta\,(\alpha<\beta)$에서만 불연속이고 $\alpha+\beta=6$이다."),
        answer="30", trap_answer=None, trap_path=None,
        explanation=[
            r"불연속점이 두 개이므로 꼭짓점이 $x$축 아래, $m=a-1<0$이다.",
            r"$\alpha=0$, $\beta=|m|=1-a$이므로 $1-a=6$, $a=-5$이다.",
            r"$f(-5)=25+10-5=30$이다.",
        ],
    ),
]


def g_count(f, tv):
    if tv < 0:
        return 0
    rs = set(real_roots(Poly(f - tv, x))) | set(real_roots(Poly(f + tv, x)))
    return len(rs)


def disconts(a):
    f = x**2 - 2*x + a
    m = a - 1
    crit = sorted({Integer(0), Abs(m), m} - {None})
    out = []
    for cv in crit:
        e = Rational(1, 100)
        if len({g_count(f, cv - e), g_count(f, cv), g_count(f, cv + e)}) > 1:
            out.append(cv)
    return out


def verify(c):
    A = [Integer(k) for k in range(-10, 11)]
    sol = [a for a in A if len(disconts(a)) == 2 and sum(disconts(a)) == 4]
    c.check("원문: a 하나", sol == [-3])
    c.ans('orig', (x**2 - 2*x + sol[0]).subs(x, sol[0]))
    sol1 = [a for a in A if disconts(a) == [2]]
    c.check("1: a 하나", sol1 == [3])
    c.ans(1, (x**2 - 2*x + sol1[0]).subs(x, sol1[0]))
    c.check("1: 함정 a=−1 은 불연속점 두 개", disconts(-1) == [0, 2])
    c.trap(1, (x**2 - 2*x - 1).subs(x, -1))
    sol2 = [a for a in A if len(disconts(a)) == 2 and sum(disconts(a)) == 6]
    c.check("2: a 하나", sol2 == [-5])
    c.ans(2, (x**2 - 2*x + sol2[0]).subs(x, sol2[0]))
