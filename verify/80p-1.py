"""원문 80p-1 (2024 수능 20번) 정답 재계산"""
import json, pathlib
from common import *

a = symbols('a', positive=True)
f = -x**3 + a*x**2 + 2*x
O = (0, 0)

# O에서의 접선과 곡선의 교점
m = diff(f, x).subs(x, 0)
roots = solve(Eq(f, m*x), x)
others = [r for r in roots if simplify(r) != 0]
check("O 접선의 다른 교점이 x=a 하나", others == [a])
A = (a, f.subs(x, a))
B = (tangent_x_intercept(f, a), 0)

# 조건: 각 OAB = 90도, a > sqrt2
sols = [s for s in solve(Eq(dot(vec(A, O), vec(A, B)), 0), a) if s.is_real and s > sqrt(2)]
check("해가 유일 (a>√2)", len(sols) == 1)
av = sols[0]
check("a^2 = 5/2", simplify(av**2 - Rational(5, 2)) == 0)
Av = at(A, a, av)
Bv = at(B, a, av)
ans = simplify(dist(O, Av) * dist(Av, Bv))
print("  OA*AB =", ans)
data = json.loads((pathlib.Path(__file__).parent.parent / "problems/80p-1.json").read_text())
check("정답 == 기록값", ans == data["answer"])
finish("80p-1")
