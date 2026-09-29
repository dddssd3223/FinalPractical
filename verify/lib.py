"""문항 검증 공통 도구.

문항 파일(verify/<문항ID>.py)은 다음을 정의한다.
  ORIG  : 원문 데이터 (id, page, num, source, type, stem, box, bogi, choices, answer,
          general, special, perspective, table, sweep)
  VARS  : 변형 2개 (variant_type, basis, changed, naturalness, stem, box, bogi, choices,
          answer, trap_answer, trap_path, explanation)
  verify(c) : sympy로 원문·변형 정답과 함정 답을 실제로 계산해 c.ans / c.trap 에 넘기고,
              조건 충족·완전성·유일성 등 문항별 검사를 c.check 로 기록한다.
정답·선지는 sympy가 읽을 수 있는 문자열("25", "-1/2", "sqrt(2)")로 적고,
<보기> 선지는 "ㄱ", "ㄱ,ㄷ" 처럼 적는다.
"""
from sympy import *  # noqa: F401,F403
from sympy import sympify, simplify, nsimplify, Rational, Integer

x = Symbol('x', real=True)


def val(s):
    """정답/선지 문자열 → 비교 가능한 값 (보기형은 문자열 그대로)."""
    if isinstance(s, str) and any('ㄱ' <= ch <= 'ㆎ' for ch in s):
        return ','.join(sorted(p.strip() for p in s.split(',')))
    return nsimplify(sympify(s)) if not isinstance(s, Basic) else s


def same(a, b):
    a, b = val(a), val(b)
    if isinstance(a, str) or isinstance(b, str):
        return a == b
    return simplify(a - b) == 0


class Ctx:
    def __init__(self):
        self.results = []
        self.answers = {}
        self.traps = {}

    def check(self, name, cond):
        ok = bool(cond)
        self.results.append((name, ok))
        return ok

    def ans(self, key, value):
        """key: 'orig' 또는 변형 번호 1, 2"""
        self.answers[key] = value

    def trap(self, key, value):
        self.traps[key] = value


def bogi_eval(truths):
    """보기 참/거짓 dict {'ㄱ':True,...} → 정답 문자열"""
    return ','.join(k for k in ('ㄱ', 'ㄴ', 'ㄷ') if truths.get(k))


def one_sided(expr, point, dirn):
    return limit(expr, x, point, dirn)


def lim_exists(expr, point, var=None):
    """좌·우극한이 모두 유한하고 같으면 (True, 값)"""
    v = var or x
    l = limit(expr, v, point, '-')
    r = limit(expr, v, point, '+')
    ok = l.is_finite and r.is_finite and simplify(l - r) == 0
    return bool(ok), (l if ok else None)


# ── 구간별 함수: sympy Piecewise 의 경계 한쪽 극한 오류를 피하려고 조각을 직접 고른다 ──
# pieces = [(식, lo, hi), ...]  : 식이 열린구간 (lo, hi) 에서 성립 (lo/hi 에 -oo, oo 가능)
def piece_at(pieces, a, side):
    for e, lo, hi in pieces:
        if side == '-' and lo < a <= hi:
            return e
        if side == '+' and lo <= a < hi:
            return e
    raise ValueError(f"no piece at {a}{side}")


def plim(pieces, F, a, side):
    """F(조각식) 의 x→a± 극한"""
    return limit(F(piece_at(pieces, a, side)), x, a, side)


def plim_exists(pieces, F, a):
    l, r = plim(pieces, F, a, '-'), plim(pieces, F, a, '+')
    ok = l.is_finite and r.is_finite and simplify(l - r) == 0
    return bool(ok), (l if ok else None)


def clim(pieces, inner, F, point, side):
    """x→point(side) 일 때 F(x, f(inner(x))) 의 극한. f 는 pieces 로 정의된 구간별 함수.
    inner 가 극한값 L 에 어느 쪽에서 다가가는지 수치로 판정해 조각을 고른다.
    inner 가 L 에서 상수(=L)면 함숫값 조각 pieces_val 이 필요하므로 여기서는 다루지 않는다."""
    L = limit(inner, x, point, side)
    eps = Rational(1, 10**6) * (1 if side == '+' else -1)
    v = inner.subs(x, point + eps)
    if simplify(v - L) == 0:
        raise ValueError("inner 가 상수로 L 에 머묾")
    s = '+' if v > L else '-'
    e = piece_at(pieces, L, s)
    return limit(F(e.subs(x, inner)), x, point, side)
