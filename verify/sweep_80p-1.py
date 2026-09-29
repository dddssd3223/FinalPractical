"""3-B 임계값 스윕: f(x) = -x^3 + a x^2 + m x (원문 m=2), a>0, m>0"""
from sympy import reduce_inequalities, Symbol
from common import *

a, m = symbols('a m', positive=True)
f = -x**3 + a*x**2 + m*x
sA = diff(f, x).subs(x, a)
A = (a, m*a)
Bx = (tangent_x_intercept(f, a), 0)
By = (0, tangent_y_intercept(f, a))
O = (0, 0)

print("O 접선 y=mx와의 교점:", solve(Eq(f, m*x), x), "(x=0 중근)")
print("A에서의 접선 기울기 s =", sA, "→ 수평:", solve(Eq(sA, 0), a))
print("x축 교점 B =", Bx, " / y축 교점 B =", By)
print("B_x > 0 (m=2) ⇔", reduce_inequalities([Bx[0].subs(m, 2) > 0], a))
for axis, B in (("x축", Bx), ("y축", By)):
    for name, (P, Q, R) in {"O": (O, A, B), "A": (A, O, B), "B": (B, O, A)}.items():
        print(f"{axis} B, 직각 at {name}: a =", solve(Eq(simplify(dot(vec(P, Q), vec(P, R))), 0), a))
aA = sqrt(m + 1/m)
print("x축 B, ∠A=90°에서 OA·AB =", simplify((dist(O, A) * dist(A, Bx)).subs(a, aA)), "(m=2 → 25)")
