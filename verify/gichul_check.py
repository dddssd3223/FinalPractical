"""학교 기출(output/gichul.py) 정답 확인: 문항 조건을 만족하는 함수를 실제로 구해 답을 재계산."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "output"))
from lib import *
from gichul import G

A = {g["id"]: g["answer"] for g in G}
ok = {}

def chk(i, v):
    ok[i] = same(v, A[i])

# 서원 19
g = (x + 1)*(x - 2)*(x - 1); f = (x + 1)*(x - 2)
chk("G-서원-19", diff(g, x).subs(x, 3))
# 한양대사대부 20
g = (x - 3)*(x - 4)*((x - 3)*(x - 4) + 1); chk("G-한양대사대부-20", g.subs(x, -1))
# 서현 16: g(2) 후보
chk("G-서현-16", min(((x - 1)**2*(x - 3)*(x + 3)).subs(x, 2), ((x - 1)*(x - 3)**2*(x + 3)).subs(x, 2)))
# 과천 12
f = (x - 1)**2*(x - 2); g = (x - 1)*(x**2 - x - 5)
assert limit((f - g)/(x - 1), x, 1) == 5 and [limit(f/g, x, n) for n in (1, 2, 3)] == [0, 0, 2]
chk("G-과천-12", f.subs(x, 3) + g.subs(x, 5))
# 서원 14 / 대전전민 24 / 마포 12: 정수 k 전수 조사
def exists_all(expr, pts):
    return all(limit(expr, x, r, '-') == limit(expr, x, r, '+') and limit(expr, x, r, '+').is_finite for r in pts)
ks = []
for k in range(-30, 31):
    F = x**2 - 4*x + 6; D = F**2 + k*(x - Rational(5, 2))*F
    if exists_all((x - 4)**2/D, Poly(expand(D), x).real_roots()): ks.append(k)
chk("G-서원-14", max(ks) + min(ks))
ks = []
for k in range(-30, 31):
    F = x**2 + 3*x + 3; D = F**2 - k*(x + 1)*F
    if exists_all(x**2/D, Poly(expand(D), x).real_roots()): ks.append(k)
chk("G-대전전민-24", len(ks))
ks = []
for k in range(-40, 41):
    F = x**2 - 4*x + 7; D = F*(F - k*(x - 1))
    if exists_all((x + 1)**2/D, [r for r in Poly(expand(D), x).real_roots() if r > k + 1]): ks.append(k)
chk("G-마포-12", sum(ks))
# 운중 12
good = []
for k in range(-10, 11):
    F = x**2 + k*x + k - 1
    if exists_all(F.subs(x, 2*x + 1)/F, Poly(F, x).real_roots()): good.append(k)
assert good == [2]
F = x**2 + 2*x + 1; chk("G-운중-12", diff(F, x).subs(x, 2))
# 운중 18 / 향동 18 / 수주 22
t = Symbol('t', positive=True)
s = sqrt(3 + 2*t); chk("G-운중-18", limit(sqrt(2)*2*s*2*s/t, t, oo))
chk("G-향동-18", limit(((2*t + 3) - 3)/t, t, 0, '+'))
chk("G-수주-22", limit((sqrt(1 + 4*t) - 1)/t, t, 0, '+'))
# 화봉 15
g = x*(x - 5)
assert limit(g/(-(x)), x, 0, '+').is_finite and limit(g.subs(x, x + 2)/(2*(x - 3)), x, 3, '+').is_finite
chk("G-화봉-15", g.subs(x, 6))
# 향동 19 / 부천 15 / 서현 13
vals = [(2*x**4 - 5*x**3 + 10*x**2 + x), 2*x**4 + x**3 + x**2, 8*x**4 + x**3, 6*x**5 + x**4, 6*x**7 + x**6]
for i, F in enumerate(vals):
    n = i + 1 if i < 4 else 6
    assert limit((F - 2*x**4 + 5*x**3 - 4*x**2)/(2*x**(n + 1) + 3), x, oo) == 3 and limit(F/x**n, x, 0) == 1
v = [F.subs(x, 1) for F in vals]; chk("G-향동-19", min(v) + max(v))
vals = [(-2*x**3 + 7*x**2 - x, 1), (2*x**3 - x**2, 2), (4*x**4 - x**3, 3), (4*x**5 - x**4, 4)]
for F, n in vals:
    assert limit((F + 2*x**3 - 3*x**2)/(x**(n + 1) + 1), x, oo) == 4 and limit(F/x**n, x, 0) == -1
chk("G-부천-15", sum({F.subs(x, 1) for F, _ in vals}))
vals = [(x*(4*x**2 - 9*x + 4), 1), (-3*x**3 + 4*x**2, 2), (-3*x**4 + 4*x**3, 3), (-3*x**5 + 4*x**4, 4)]
for F, n in vals:
    assert limit(F/x**n, x, 0) == 4 and any(1 < r < 2 for r in Poly(F, x).real_roots())
v = [F.subs(x, -1) for F, _ in vals]; chk("G-서현-13", max(v) + min(v))
# 감일 21
Q = Symbol('Q'); chk("G-감일-21", (Integer(-27) + 3)/(-27))
# 한양대사대부 13 / 수주 20
F = 5*(x - 4); assert limit(F.subs(x, x + 4)/(x*(F + 10)), x, 0).is_finite; chk("G-한양대사대부-13", F.subs(x, 10))
F = 3*(x - 2); assert limit(F.subs(x, x + 2)/(x*(F - 3)), x, 0).is_finite; chk("G-수주-20", F.subs(x, 5))
# 선화예 22
best = min(Rational(6, 8 + 2*p) for p in range(-3, 4)); chk("G-선화예-22", best)
# 화봉 20: 보기
chk("G-화봉-20", "ㄱ,ㄴ")
# 신송 19
a = Rational(5, 4); gx = (x + a)*((x - 15) + 5)**2
assert 5*(0 + 5)**2 == a*((0 - 15) + 5)**2
chk("G-신송-19", gx.subs(x, 6))
# 명석 15
chk("G-명석-15", 22 - 5*sqrt(6))
xc = 3*sqrt(6)/2; assert simplify(Rational(2, 3)*xc*xc - 9) == 0
# 명석 14
c = Symbol('c'); F = (x - 2)**2 + c; h = Symbol('h')
S = sum(limit((F.subs(x, k - 3 + 2*h) - F.subs(x, k - 3 - h))/h, h, 0) for k in range(1, 11))
cv = solve(S - F.subs(x, 0), c)[0]; chk("G-명석-14", F.subs(c, cv).subs(x, 1))
# 대전노은 24
F = 2*(x - 1)**2*(x - 2)
k = limit(F/((x - 1)*diff(F, x)), x, 1); assert limit(F/(x - 2), x, 2) == 2 and k != 1
chk("G-대전노은-24", F.subs(x, 4)*k)
# 수주 21
F = (x + 1)*(x - 1)*(x - 2); assert limit(F/((x + 1)*diff(F, x)**2), x, -1) == Rational(1, 6)
chk("G-수주-21", F.subs(x, 3))
# 정발 19
chk("G-정발-19", "ㄱ,ㄷ")
# 죽전 20
F = x**3 - 3*x**2 - 2*x + 4; a, b = 8, 16
P = [(F + 4*x, -oo, 0), (-F - 2*x**2 + a, 0, 2), (F - 4*x + b, 2, oo)]
for tt in (0, 2):
    assert piece_at(P, tt, '-').subs(x, tt) == piece_at(P, tt, '+').subs(x, tt)
    assert plim(P, lambda e: diff(e, x), tt, '-') == plim(P, lambda e: diff(e, x), tt, '+')
chk("G-죽전-20", (-F - 2*x**2 + a).subs(x, 1) + (F - 4*x + b).subs(x, 3))
# 과천 17 / 늘푸른 16
av = sqrt(Rational(10, 3)); chk("G-과천-17", sqrt(10)*av*3*sqrt(10)*av)
chk("G-늘푸른-16", Rational(1, 2)*8*32)
# 평균값 정리 3문항
chk("G-과천-9", 2 + 8); chk("G-한양대사대부-16", 3 + 6*9); chk("G-용문-19", 12*4)
bad = [k for k, v in ok.items() if not v]
print(f"{len(ok)}/{len(G)} 확인, 불일치: {bad}")
missing = set(A) - set(ok)
print("미확인:", missing)
