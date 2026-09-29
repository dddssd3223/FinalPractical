from lib import *

ORIG = dict(
    id="19p-43", chapter=1, page=19, num=43, source="2023년 수능특강 [23009-0024]", type="객관식",
    stem=r"다음 조건을 만족시키는 두 실수 $a$, $b$의 모든 순서쌍 $(a,\,b)$의 개수는?",
    box=[r"(가) $\displaystyle\lim_{x\to1}\frac{x-1}{x^2-a}=b$",
         r"(나) $\displaystyle\lim_{x\to0}\left|\frac{x^3+ax^2+bx}{x^k}\right|=\frac12$인 자연수 $k$가 존재한다."],
    choices=["1", "2", "3", "4", "5"], answer="3",
    general="(가): a=1 이면 b=1/2, a≠1 이면 b=0. (나): (1, ½) → x(x²+x+½), k=1 에서 ½ ✓. b=0: x²(x+a) → a≠0 이면 k=2, |a|=½ → a=±½; a=0 이면 x³, k=3 → 1 ✗. 총 3개.",
    special="① (가)에서 분모가 0 이 되는 a=1 경우를 빠뜨림. ② (나)에서 a=0 이면 차수가 올라가는 경우를 확인하지 않음(값이 ½ 이 아니라 우연히 제외).",
    perspective="(나)는 '가장 낮은 차수 항의 계수의 절댓값' 이 값이 되는 구조.",
    table=[
        ("(가)의 극한점 1", "a=1 (분모도 0)", "극한점을 바꾸면 특수 a 도 바뀜"),
        ("(나)의 값 ½", "a=0 (x³, 값 1)", "값을 1 로 바꾸면 a=0 이 살아나고 a=1 은 (가) 때문에 제외"),
    ],
    sweep=["a=x₀² 에서 (가)가 0/0", "a=0 에서 (나)의 최저차항이 x³"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 2행 / 3-C 1 (a=0 에서 최저차항 변화, a=1 은 (가)의 b 가 달라 제외)",
        changed=["(나)의 값 ½ → 1"], naturalness="",
        stem=r"다음 조건을 만족시키는 두 실수 $a$, $b$의 모든 순서쌍 $(a,\,b)$의 개수는?",
        box=[r"(가) $\displaystyle\lim_{x\to1}\frac{x-1}{x^2-a}=b$",
             r"(나) $\displaystyle\lim_{x\to0}\left|\frac{x^3+ax^2+bx}{x^k}\right|=1$인 자연수 $k$가 존재한다."],
        choices=["1", "2", "3", "4", "5"], answer="2", trap_answer="3",
        trap_path="b=0 에서 |a|=1 → a=±1 을 모두 세고 a=0 까지 더해 3 (a=1 이면 (가)에서 b=½ 이라 (1,0) 은 불가).",
        explanation=[
            r"(가): $a=1$이면 $b=\frac12$, $a\neq1$이면 $b=0$이다.",
            r"$(1,\,\frac12)$: $x^3+x^2+\frac12x$의 최저차항 계수가 $\frac12$이므로 값이 $1$이 될 수 없다.",
            r"$b=0$, $a\neq0$: $k=2$에서 $|a|=1$, 함정: $a=1$은 (가)에서 $b=\frac12$이므로 제외하고 $a=-1$만.",
            r"$b=0$, $a=0$: $\frac{x^3}{x^3}$에서 값 $1$이므로 가능하다.",
            r"$(-1,\,0)$, $(0,\,0)$의 $2$개이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 1행 (극한점 1 → 2, 값 ½ → ¼)",
        changed=["(가)의 극한점 1 → 2", "(나)의 값 ½ → ¼"],
        naturalness="극한점을 옮기면 특수 a 의 b 값이 ¼ 로 바뀌어, 같은 구조를 유지하려고 (나)의 값을 함께 맞춘 것.",
        stem=r"다음 조건을 만족시키는 두 실수 $a$, $b$의 모든 순서쌍 $(a,\,b)$의 개수는?",
        box=[r"(가) $\displaystyle\lim_{x\to2}\frac{x-2}{x^2-a}=b$",
             r"(나) $\displaystyle\lim_{x\to0}\left|\frac{x^3+ax^2+bx}{x^k}\right|=\frac14$인 자연수 $k$가 존재한다."],
        choices=["1", "2", "3", "4", "5"], answer="3", trap_answer=None, trap_path=None,
        explanation=[
            r"(가): $a=4$이면 $b=\frac14$, $a\neq4$이면 $b=0$이다.",
            r"$(4,\,\frac14)$: $k=1$에서 값 $\frac14$로 가능하다.",
            r"$b=0$: $a\neq0$이면 $k=2$에서 $|a|=\frac14$, $a=\pm\frac14$. $a=0$이면 값 $1$이라 불가.",
            r"모두 $3$개이다.",
        ],
    ),
]


def pairs(x0, v):
    out = set()
    # (가)의 특수 경우 a = x0²
    a_s = x0**2
    b_s = limit((x - x0)/(x**2 - a_s), x, x0)
    cands = [(a_s, b_s)]
    # 일반 경우 b=0, a≠x0²: 후보 a 는 |a|=v 의 해와 0
    for a in {v, -v, 0}:
        if a != a_s:
            cands.append((a, 0))
    for a, b in cands:
        c1 = limit((x - x0)/(x**2 - a), x, x0) == b
        e = x**3 + a*x**2 + b*x
        c2 = any(limit(Abs(e/x**k), x, 0) == v for k in range(1, 7))
        if c1 and c2:
            out.add((a, b))
    return out


def verify(c):
    c.check("원문 쌍 {(1,½), (½,0), (−½,0)}", pairs(1, Rational(1, 2)) == {(1, Rational(1, 2)), (Rational(1, 2), 0), (-Rational(1, 2), 0)})
    c.ans('orig', len(pairs(1, Rational(1, 2))))
    r = pairs(1, 1)
    c.check("1: 쌍 {(−1,0), (0,0)}", r == {(-1, 0), (0, 0)})
    c.ans(1, len(r))
    c.trap(1, len({(1, 0), (-1, 0), (0, 0)}))
    r = pairs(2, Rational(1, 4))
    c.ans(2, len(r))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1]['drop'] = '생존 확인형: 수치만 바꾼 쉬운 변형 (함정 없음)'
