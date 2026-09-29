"""80p-1-2 (생존 확인형): 계수 2 → 3, 원문 풀이가 그대로 통하는지"""
import json, pathlib
from common import *

ROOT = pathlib.Path(__file__).parent.parent
data = json.loads((ROOT / "variants/80p-1-2.json").read_text())
a = symbols('a', positive=True)
f = -x**3 + a*x**2 + 3*x
O = (0, 0)

m = diff(f, x).subs(x, 0)
others = [r for r in solve(Eq(f, m*x), x) if simplify(r) != 0]
check("A의 x좌표가 a 하나 (원문 풀이 그대로)", others == [a])
A = (a, f.subs(x, a))
B = (tangent_x_intercept(f, a), 0)

# 완전성: a>0 전체에서 직각 위치별로 풀고, a>√3 만 남김
allsol = {}
for name, (P, Q, R) in {"O": (O, A, B), "A": (A, O, B), "B": (B, O, A)}.items():
    allsol[name] = [s for s in solve(Eq(simplify(dot(vec(P, Q), vec(P, R))), 0), a) if s.is_positive]
print("  a>0에서 직각 위치별 해:", allsol)
check("완전성: 직각은 A에서만, O·B는 해 없음", allsol["O"] == [] and allsol["B"] == [])
sols = [s for s in allsol["A"] if s > sqrt(3)]
check("유일성: a>√3 에서 해 하나", len(sols) == 1)
av = sols[0]
check("a^2 = 10/3", simplify(av**2 - Rational(10, 3)) == 0)
Av, Bv = at(A, a, av), at(B, a, av)
check("B가 양의 x축 위, A에서 접선 기울기 ≠ 0", Bv[0] > 0 and diff(f, x).subs(x, av).subs(a, av) != 0)
ans = simplify(dist(O, Av) * dist(Av, Bv))
print("  OA*AB =", ans)
check("정답 재계산 == 기록값", ans == data["answer"])
check("일반식 (m^2+1)^2 과 일치", ans == (3**2 + 1)**2)
check("생존 확인형: 함정 답 없음", data["variant_type"] == "생존 확인형" and data["trap_answer"] is None)
check("수치 품질: 정답 자연수", ans.is_integer and ans > 0)
finish("80p-1-2")
