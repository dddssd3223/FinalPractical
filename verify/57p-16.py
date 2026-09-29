from lib import *

def stem(inside, rng):
    return (r"함수 $f(x)=(x-2)\left|" + inside + r"\right|$이 실수 전체의 집합에서 미분가능하도록 하는 " + rng + r" 자연수 $a$, $b$의 모든 순서쌍 $(a,\,b)$의 개수는?")

ORIG = dict(
    id="57p-16", chapter=3, page=57, num=16, source="2024년 수능완성 [24054-0111]", type="객관식",
    stem=stem("(x-a)(x-b)^2", "한 자리의"), choices=["11", "13", "15", "17", "19"], answer="17",
    general="f=(x−2)(x−b)²|x−a|. |x−a| 의 꺾임은 곱해진 (x−2)(x−b)² 가 x=a 에서 0 이면 사라짐 → a=2 또는 a=b. a=2: 9쌍, a=b: 9쌍, (2,2) 중복 → 17.",
    special="① (x−b)² 는 제곱이라 절댓값 밖으로 나와 꺾임이 x=a 하나뿐 — (x−b) 가 1제곱이면 x=b 에서도 꺾임.",
    perspective="|x−c|·p(x) 는 p(c)=0 이면 c 에서 미분가능.",
    table=[
        ("(x−b)²", "(x−b) 1제곱 (꺾임 둘)", "|(x−a)(x−b)| 면 a=b 만 가능 → 9"),
        ("한 자리 자연수", "—", "10 이하면 10+10−1=19 (생존)"),
    ],
    sweep=["꺾이는 점: x=a (그리고 1제곱이면 x=b)"],
)

VARS = [
    dict(
        variant_type="분기 유발형", type="객관식",
        basis="3-A 1행 (절댓값 안 인수가 1제곱이면 꺾이는 점이 둘)",
        changed=["|(x−a)(x−b)²| → |(x−a)(x−b)|"], naturalness="",
        stem=stem("(x-a)(x-b)", "한 자리의"), choices=["9", "11", "13", "15", "17"], answer="9", trap_answer="17",
        trap_path="원문처럼 꺾이는 점을 x=a 하나로 보아 a=2 또는 a=b → 17.",
        explanation=[
            r"$f(x)=(x-2)|x-a||x-b|$이다.",
            r"$a\neq b$이면 $x=a$와 $x=b$에서 모두 꺾이고, 두 점에서 모두 $(x-2)\times(\text{나머지})=0$이려면 $a=b=2$여야 하므로 모순이다.",
            r"함정: 원문과 달리 $x=b$에서도 꺾인다. $a=b$이면 $|x-a|^2=(x-a)^2$이 되어 미분가능하다.",
            r"따라서 $a=b$인 $9$쌍이다.",
        ],
    ),
    dict(
        variant_type="생존 확인형", type="객관식",
        basis="3-A 2행 (범위: 한 자리 → 10 이하)",
        changed=["한 자리의 자연수 → 10 이하의 자연수"], naturalness="",
        stem=stem("(x-a)(x-b)^2", r"$10$ 이하의"), choices=["17", "18", "19", "20", "21"], answer="19", trap_answer=None, trap_path=None,
        explanation=[
            r"$f(x)=(x-2)(x-b)^2|x-a|$는 $x=a$에서만 꺾일 수 있다.",
            r"$(x-2)(x-b)^2$이 $x=a$에서 $0$이면 미분가능하므로 $a=2$ 또는 $a=b$이다.",
            r"$10+10-1=19$쌍이다.",
        ],
    ),
]


def diffable_all(f, pts):
    return all(simplify(limit((f - f.subs(x, p))/(x - p), x, p, '-') - limit((f - f.subs(x, p))/(x - p), x, p, '+')) == 0 for p in pts)


def count(inside_fn, N):
    n = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            f = (x - 2)*Abs(inside_fn(a, b))
            if diffable_all(f, sorted({a, b, 2})):
                n += 1
    return n


def verify(c):
    c.ans('orig', count(lambda a, b: (x - a)*(x - b)**2, 9))
    c.ans(1, count(lambda a, b: (x - a)*(x - b), 9))
    c.trap(1, count(lambda a, b: (x - a)*(x - b)**2, 9))
    c.ans(2, count(lambda a, b: (x - a)*(x - b)**2, 10))


# ── 난이도 검토 (함정 없는 쉬운 변형 제외 / 생존형에 실제 함정 경로 추가) ──
VARS[1].update(trap_answer='20', trap_path='a=2 인 10쌍과 a=b 인 10쌍을 그냥 더해 20 ((2,2) 가 두 번 세어짐).')
VARS[1]['explanation'].insert(-1, '함정: $(2,2)$는 두 경우에 모두 들어가므로 한 번 빼야 한다.')
_verify0 = verify


def verify(c):
    _verify0(c)
    c.trap(2, len([1 for a in range(1, 11) if a == 2]*10) + len([1 for a in range(1, 11)]))

# ── 2차 검토: 원문 풀이 방식이 그대로 통하는 변형 제외 ──
VARS[1]['drop'] = '생존형: 원문 풀이가 그대로 통하고 함정이 계산 실수 수준'
