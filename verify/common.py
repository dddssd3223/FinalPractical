import sys
from sympy import sympify, symbols, simplify, sqrt, Eq, solve, diff, Rational, nsimplify, fraction

x = symbols('x', real=True)
_results = []


def check(name, cond):
    ok = bool(cond)
    _results.append((name, ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    return ok


def finish(qid):
    bad = [n for n, ok in _results if not ok]
    print(f"{qid}: {'PASS' if not bad else 'FAIL ' + str(bad)}")
    sys.exit(1 if bad else 0)


def tangent_x_intercept(f, p):
    s = diff(f, x).subs(x, p)
    return simplify(p - f.subs(x, p) / s)


def tangent_y_intercept(f, p):
    s = diff(f, x).subs(x, p)
    return simplify(f.subs(x, p) - s * p)


def dist(P, Q):
    return sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)


def dot(u, v):
    return u[0] * v[0] + u[1] * v[1]


def vec(P, Q):
    return (Q[0] - P[0], Q[1] - P[1])


def at(P, s, v):
    return tuple(simplify(sympify(c).subs(s, v)) for c in P)
