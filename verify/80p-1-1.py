"""80p-1-1: 직각 위치 경우 분류"""
import json, pathlib
from sympy import Abs
from common import *

ROOT = pathlib.Path(__file__).parent.parent
data = json.loads((ROOT / "variants/80p-1-1.json").read_text())
a = symbols('a', positive=True)
f = -x**3 + a*x**2 + 2*x
O = (0, 0)

m = diff(f, x).subs(x, 0)
others = [r for r in solve(Eq(f, m*x), x) if simplify(r) != 0]
check("A의 x좌표가 a 하나", others == [a])
A = (a, f.subs(x, a))
B = (0, tangent_y_intercept(f, a))

def area(P, Q, R):
    return Abs((Q[0]-P[0])*(R[1]-P[1]) - (R[0]-P[0])*(Q[1]-P[1])) / 2

# 세 꼭짓점 각각에서 직각인 a (a>0) 모두 수집
cases = {}
for name, (P, Q, R) in {"O": (O, A, B), "A": (A, O, B), "B": (B, O, A)}.items():
    sols = [s for s in solve(Eq(simplify(dot(vec(P, Q), vec(P, R))), 0), a) if s.is_positive]
    cases[name] = sols
    print(f"  직각 at {name}: a = {sols}")
check("O에서 직각인 경우 없음", cases["O"] == [])
check("A에서 직각: a^2=5/2 하나", len(cases["A"]) == 1 and simplify(cases["A"][0]**2 - Rational(5, 2)) == 0)
check("B에서 직각: a=√2 하나", cases["B"] == [sqrt(2)])

all_a = set(cases["A"]) | set(cases["B"])
tri_ok = True
for av in all_a:
    Av, Bv = at(A, a, av), at(B, a, av)
    if area(O, Av, Bv) == 0 or Av == (0, 0) or Bv == Av or Bv == (0, 0):
        tri_ok = False
check("각 경우 삼각형이 퇴화하지 않음", tri_ok)

S = simplify(sum(area(O, at(A, a, av), at(B, a, av)) for av in all_a))
print("  S =", S)
ans = simplify(8 * S)
check("정답 재계산 == 기록값", ans == data["answer"])
trap = simplify(8 * area(O, at(A, a, cases["A"][0]), at(B, a, cases["A"][0])))
check("함정 답 재계산 == 기록값", trap == data["trap_answer"])
check("함정 답 != 정답", data["trap_answer"] != data["answer"])
check("수치 품질: 정답이 자연수", ans.is_integer and ans > 0)
finish("80p-1-1")
