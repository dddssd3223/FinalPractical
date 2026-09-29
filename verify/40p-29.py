from lib import *

def stem(fcond):
    return (r"실수 전체의 집합에서 연속이고 " + fcond + r" 함수 $f(x)$와 $\displaystyle\lim_{x\to1+}g(x)>\lim_{x\to1-}g(x)$인 함수 $g(x)$가 있다. 두 함수 $f(x)$, $g(x)$가 다음 조건을 만족시킬 때, $10f(1)$의 값을 구하시오.")

def box(s):
    return [r"(가) 함수 $|f(x)g(x)|$는 실수 전체의 집합에서 연속이다.",
            r"(나) $x<1$일 때 $f(x)g(x)=x^2-2x-8$이고, $x>1$일 때 $\dfrac{g(x)}{f(x)}=" + s + r"$이다."]

ORIG = dict(
    id="40p-29", chapter=2, page=40, num=29, source="2023년 수능특강 [23009-0045]", type="주관식",
    stem=stem(r"모든 실수 $x$에 대하여 $f(x)>0$인"), box=box("3x+1"), answer="15",
    general="x→1−: fg→−9, |fg|→9. x→1+: fg=f²(3x+1)→4f(1)². |fg| 연속 → 4f(1)²=9, f>0 → f(1)=3/2 → 15. (g 좌 −6, 우 6 으로 부등식 만족)",
    special="① f>0 이라 제곱근의 부호가 바로 결정되어 lim g 부등식을 쓰지 않음 — f 의 부호 조건이 없으면 부등식이 부호를 골라 줌.",
    perspective="|fg| 연속은 크기만, g 의 한쪽 극한 대소는 부호를 준다.",
    table=[
        ("f>0", "f(1)<0 인 경우", "f≠0 로만 두면 f(1)=±3/2, 부등식이 −3/2 를 제외"),
        ("x>1 에서 g/f=3x+1", "—", "3x+6 이면 9f(1)²=9 → f(1)=1 (생존)"),
    ],
    sweep=["f(1)=±3/2 에서 g 의 좌 −9/f(1), 우 4f(1)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="주관식",
        basis="3-A 1행 (f 의 부호 조건이 없으면 lim g 대소가 부호를 결정)",
        changed=["f(x)>0 → f(x)≠0"], naturalness="",
        stem=stem(r"모든 실수 $x$에 대하여 $f(x)\neq0$인"), box=box("3x+1"), answer="15", trap_answer="-15",
        trap_path="4f(1)²=9 에서 f(1)=−3/2 도 택함 (이때 g 의 좌 6, 우 −6 이라 lim_{x→1+}g > lim_{x→1−}g 위반).",
        explanation=[
            r"$x\to1-$일 때 $f(x)g(x)\to-9$, $x\to1+$일 때 $f(x)g(x)=\{f(x)\}^2(3x+1)\to4\{f(1)\}^2$이다.",
            r"(가)에서 $4\{f(1)\}^2=9$, $f(1)=\pm\frac32$이다.",
            r"$\displaystyle\lim_{x\to1-}g=\frac{-9}{f(1)}$, $\displaystyle\lim_{x\to1+}g=4f(1)$이므로 $f(1)=-\frac32$이면 좌 $6$, 우 $-6$으로 조건에 어긋난다.",
            r"함정: 부호는 $g$의 극한 대소 조건으로 정해진다. $f(1)=\frac32$, $10f(1)=15$이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="주관식",
        basis="3-A 2행 (g/f=3x+1 → 3x+6)",
        changed=["x>1 에서 g/f=3x+1 → 3x+6"], naturalness="",
        stem=stem(r"모든 실수 $x$에 대하여 $f(x)>0$인"), box=box("3x+6"), answer="10", trap_answer=None, trap_path=None,
        explanation=[
            r"$x\to1-$일 때 $|fg|\to9$, $x\to1+$일 때 $|fg|=\{f(x)\}^2(3x+6)\to9\{f(1)\}^2$이다.",
            r"$9\{f(1)\}^2=9$, $f>0$이므로 $f(1)=1$이다.",
            r"$10f(1)=10$이다.",
        ],
    ),
]


def f1_values(s, positive):
    F = Symbol('F', real=True)
    left = limit(x**2 - 2*x - 8, x, 1, '-')
    right_fg = F**2*s.subs(x, 1)
    out = []
    for v in solve(Eq(Abs(left)**2, right_fg**2), F):
        if v == 0 or (positive and v < 0):
            continue
        gl = left/v
        gr = v*s.subs(x, 1)
        if gr > gl:
            out.append(v)
    return out


def verify(c):
    r = f1_values(3*x + 1, True)
    c.check("원문: f(1) 하나", len(r) == 1)
    c.ans('orig', 10*r[0])
    r = f1_values(3*x + 1, False)
    c.check("1: 부등식 적용 후 f(1) 하나", len(r) == 1)
    c.ans(1, 10*r[0])
    c.trap(1, -Rational(15))
    r = f1_values(3*x + 6, True)
    c.check("2: f(1) 하나", len(r) == 1)
    c.ans(2, 10*r[0])
