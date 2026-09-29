"""80p-1-2: 최고차계수 변경 -> 다른 교점 x=a/2"""
import json, pathlib
from sympy import Abs
from common import *

ROOT = pathlib.Path(__file__).parent.parent
data = json.loads((ROOT / "variants/80p-1-2.json").read_text())
a = symbols('a', positive=True)
f = -2*x**3 + a*x**2 + x
O = (0, 0)

m = diff(f, x).subs(x, 0)
others = [r for r in solve(Eq(f, m*x), x) if simplify(r) != 0]
check("A의 x좌표가 a/2 하나", others == [a/2])
p = others[0]
A = (p, f.subs(x, p))
B = (tangent_x_intercept(f, p), 0)

sols = [s for s in solve(Eq(simplify(dot(vec(A, O), vec(A, B))), 0), a) if s.is_positive]
print("  a =", sols)
check("해가 유일 (a>0)", len(sols) == 1)
av = sols[0]
check("A에서의 접선 기울기 != 0 (B 존재)", diff(f, x).subs(x, p).subs(a, av) != 0)
Av, Bv = at(A, a, av), at(B, a, av)
check("A != O, B != O", Av != (0, 0) and Bv != (0, 0))
ans = simplify(av * dist(O, Bv))
print("  a*OB =", ans)
check("정답 재계산 == 기록값", ans == data["answer"])

# 함정: A를 (a, f(a))로 두고 푼 경로 — 원문 암기 공식
ft = f
At = (a, m*a)                 # O 접선 y=x 위의 점으로 착각
st = diff(ft, x).subs(x, a)   # 1 - 4a^2
tsol = [s for s in solve(Eq(m*st, -1), a) if s.is_positive]
check("함정 경로 해 유일", len(tsol) == 1)
ta = tsol[0]
xBt = simplify((At[0] - At[1]/st).subs(a, ta))
trap = simplify(ta * Abs(xBt))
print("  trap =", trap)
check("함정 답 재계산 == 기록값", trap == data["trap_answer"])
check("함정 답 != 정답", data["trap_answer"] != data["answer"])
check("수치 품질: 정답이 자연수", ans.is_integer and ans > 0)
finish("80p-1-2")
