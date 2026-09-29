"""문항 그림 (SVG) — 원문에 그림이 있던 도형·그래프 문항에만 대표 값으로 그린다.
FIGS[변형 id] = svg 문자열. 색은 템플릿 팔레트(#d2436a 곡선, #1e1a1b 선, #8e888c 축, #fdf2f6 채움)."""
import math

PINK, INK, GRAY, FILL = "#d2436a", "#1e1a1b", "#8e888c", "#f7c9da"


class Fig:
    def __init__(self, x0, x1, y0, y1, w=330, h=None):
        """h 를 주면 세로 배율을 따로 둠 (개형 그림)"""
        self.x0, self.x1, self.y0, self.y1 = x0, x1, y0, y1
        self.w = w
        self.h = h or w*(y1 - y0)/(x1 - x0)
        self.el = []

    def P(self, x, y):
        return (x - self.x0)/(self.x1 - self.x0)*self.w, self.h - (y - self.y0)/(self.y1 - self.y0)*self.h

    def axes(self, xl="x", yl="y", origin=True):
        a, b = self.P(self.x0, 0), self.P(self.x1, 0)
        c, d = self.P(0, self.y0), self.P(0, self.y1)
        m = '<marker id="ar" viewBox="0 0 6 6" refX="5" refY="3" markerWidth="6" markerHeight="6" orient="auto"><path d="M0,0 L6,3 L0,6 z" fill="%s"/></marker>' % GRAY
        self.el.append("<defs>%s</defs>" % m)
        self.el.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{GRAY}" stroke-width="0.9" marker-end="url(#ar)"/>')
        self.el.append(f'<line x1="{c[0]:.1f}" y1="{c[1]:.1f}" x2="{d[0]:.1f}" y2="{d[1]:.1f}" stroke="{GRAY}" stroke-width="0.9" marker-end="url(#ar)"/>')
        self.text(self.x1, 0, xl, dx=-8, dy=14)
        self.text(0, self.y1, yl, dx=6, dy=10)
        if origin:
            self.text(0, 0, "O", dx=-12, dy=13, italic=False)

    def curve(self, f, a, b, color=PINK, width=1.6, n=240, dash=None):
        pts = []
        for i in range(n + 1):
            x = a + (b - a)*i/n
            y = f(x)
            if y is None or not (self.y0 - 1e3 < y < self.y1 + 1e3):
                continue
            pts.append(self.P(x, y))
        d = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="{width}"{extra}/>')

    def line(self, p, q, color=INK, width=1.0, dash=None):
        a, b = self.P(*p), self.P(*q)
        extra = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{color}" stroke-width="{width}"{extra}/>')

    def poly(self, pts, fill=FILL, stroke=INK, width=0.9, opacity=0.8):
        d = " ".join("%.1f,%.1f" % self.P(*p) for p in pts)
        self.el.append(f'<polygon points="{d}" fill="{fill}" fill-opacity="{opacity}" stroke="{stroke}" stroke-width="{width}"/>')

    def dot(self, p, label=None, dx=6, dy=-6, italic=False):
        a = self.P(*p)
        self.el.append(f'<circle cx="{a[0]:.1f}" cy="{a[1]:.1f}" r="2.3" fill="{INK}"/>')
        if label:
            self.text(p[0], p[1], label, dx=dx, dy=dy, italic=italic)

    def text(self, x, y, s, dx=0, dy=0, italic=True, size=12, color=INK):
        a = self.P(x, y)
        st = "italic" if italic else "normal"
        self.el.append(f'<text x="{a[0] + dx:.1f}" y="{a[1] + dy:.1f}" font-family="\'Times New Roman\', serif" font-style="{st}" font-size="{size}" fill="{color}">{s}</text>')

    def svg(self):
        pad = 14
        W, H = self.w + 2*pad, self.h + 2*pad
        k = min(1.0, 250/H)  # 그림 높이 상한 250px (약 66mm)
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {W:.0f} {H:.0f}" '
                f'style="width: {W*k:.0f}px; height: {H*k:.0f}px;">' + "".join(self.el) + "</svg>")


def lineq(p, q):
    """두 선분 p1p2, q1q2 의 교점"""
    (x1, y1), (x2, y2) = p
    (x3, y3), (x4, y4) = q
    d = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4))/d
    return x1 + t*(x2 - x1), y1 + t*(y2 - y1)


def f17():  # y=tx²+1, 직선 y=x−1, t=0.15
    t = 0.15
    F = Fig(-1.2, 6.2, -2, 5.2, w=320, h=220)
    F.axes()
    F.curve(lambda x: t*x*x + 1, -1.2, 5.5)
    F.curve(lambda x: x - 1, -1, 6.2, color=INK, width=1.1)
    P = (1/(2*t), 1/(4*t) + 1)
    Q = ((P[0] + P[1] + 1)/2, (P[0] + P[1] - 1)/2)
    s = P[1]/P[0]
    R = (1/(1 - s), s/(1 - s))
    F.line((0, 0), R, dash="4 3")
    F.poly([P, Q, R])
    F.dot(P, "P", -14, -6); F.dot(Q, "Q", 6, 12); F.dot(R, "R", 6, -4)
    F.text(5.2, 5.2 - 1, "y=x−1", dx=-40, dy=26, size=11)
    return F.svg()


def f19():  # t=0.5
    t = 0.5
    F = Fig(-1.4, 1.3, -0.3, 1.3, w=300)
    F.axes()
    F.curve(lambda x: math.sqrt(x) if x >= 0 else None, 0, 1.25)
    F.curve(lambda x: x*x, -1.1, 0)
    A, B, C, D = (t, 0), (0, 1), (0, t), (-1, 0)
    F.line(A, B); F.line(C, D)
    # P: √x = 1 − x/t,  Q: x² = t(x+1)
    # √x=u 로 두면 u = 1 − u²/t → u² + t u − t = 0
    u = (-t + math.sqrt(t*t + 4*t))/2
    Pp = (u*u, u)
    xq = (t - math.sqrt(t*t + 4*t))/2
    Qp = (xq, xq*xq)
    F.poly([(0, 0), A, Pp]); F.poly([(0, 0), Qp, D])
    F.dot(A, "A", 2, 14); F.dot(B, "B", 6, -2); F.dot(C, "C", 6, 4); F.dot(D, "D", -6, 14)
    F.dot(Pp, "P", 6, -6); F.dot(Qp, "Q", -14, -6)
    return F.svg()


def f20():  # y=x²−2x, 기울기 −3, t=0.8
    t = 0.8
    F = Fig(-2.6, 3.0, -1.6, 7.6, w=300, h=230)
    F.axes()
    F.curve(lambda x: x*x - 2*x, -2.5, 2.95)
    P = (t, t*t - 2*t)
    xq = -1 - t
    Q = (xq, xq*xq - 2*xq)
    F.curve(lambda x: P[1] - 3*(x - P[0]), -2.25, 1.3, color=INK, width=1.0)
    F.line((0, 0), Q, color=PINK, dash="4 3", width=1.2)
    F.dot(P, "P", 6, 14); F.dot(Q, "Q", -16, -4)
    return F.svg()


def f21():  # 정사각형 ABCD, t=0.5
    t = 0.5
    F = Fig(-0.25, 1.25, -0.2, 1.2, w=230)
    A, D, B, C = (0, 1), (1, 1), (0, 0), (1, 0)
    F.poly([A, D, C, B], fill="#ffffff")
    P = (1, t); Q = (0, t/2)
    R = lineq((B, P), (C, Q))
    F.poly([C, P, R])
    F.line(B, P); F.line(C, Q)
    for p, l, dx, dy in ((A, "A", -14, -4), (D, "D", 6, -4), (B, "B", -14, 12), (C, "C", 6, 12),
                         (P, "P", 6, 4), (Q, "Q", -14, 4), (R, "R", -4, -8)):
        F.dot(p, l, dx, dy)
    return F.svg()


def f26a():  # y=x²+x, y=x+t, t=1
    F = Fig(-2.8, 1.8, -0.8, 3)
    F.axes()
    F.curve(lambda x: x*x + x, -2.7, 1.3)
    F.curve(lambda x: x + 1, -2.2, 1.6, color=INK, width=1.1)
    A, B, C, H = (1, 2), (-1, 0), (-2, 2), (-1, 2)
    F.line(C, A, dash="4 3"); F.line(B, H, dash="4 3")
    F.dot(A, "A", 6, -4); F.dot(B, "B", -16, 14); F.dot(C, "C", -14, -6); F.dot(H, "H", 4, -8)
    return F.svg()


def f26b():  # y=x², y=2tx−2, t=0.6
    t = 0.6
    F = Fig(-1.2, 4.2, -2.6, 3.4)
    F.axes()
    F.curve(lambda x: x*x, -1.2, 1.8)
    F.curve(lambda x: 2*t*x - 2, -0.6, 4.2, color=INK, width=1.1)
    P = (t, t*t); Q = (2/t, 2)
    F.line((0, 0), Q, dash="4 3")
    F.dot(P, "P", -6, -10); F.dot(Q, "Q", 6, -6)
    return F.svg()


def f72():  # 영역 h(x)=2,x,2,3 과 정사각형 t=2.5
    F = Fig(-0.4, 4.6, -0.4, 3.6, w=300)
    F.axes()
    F.poly([(0, 0), (0, 2), (1, 2), (1, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 0)], fill="#f5d3df", opacity=0.9)
    t = 2.5
    F.poly([(0, 0), (t, 0), (t, t), (0, t)], fill="none", stroke=PINK, width=1.3)
    for k in range(1, 5):
        F.text(k, 0, str(k), dx=-3, dy=14, italic=False, size=11)
    for k in range(1, 4):
        F.text(0, k, str(k), dx=-12, dy=4, italic=False, size=11)
    F.text(t, 0, "t", dx=-3, dy=26, size=11, color=PINK)
    return F.svg()


def f81():  # f=x³−2x, A(−1,1), B(2,4), k=−0.5
    f = lambda x: x**3 - 2*x
    F = Fig(-1.9, 2.5, -1.8, 4.8, w=300, h=230)
    F.axes()
    F.curve(f, -1.8, 2.15)
    F.curve(lambda x: x + 2, -1.9, 2.5, color=INK, width=1.0)
    A, B = (-1, 1), (2, 4)
    k = -0.5
    Pk = (k, f(k))
    F.poly([A, Pk, B])
    F.line((k, -1.7), (k, 4.6), color=GRAY, dash="3 3")
    F.dot(A, "A", -14, -4); F.dot(B, "B", 6, 4); F.dot(Pk, "P<tspan font-size='8' dy='3'>k</tspan>", 5, 12)
    F.text(k, 0, "x=k", dx=4, dy=-80, size=10)
    return F.svg()


FIGS = {"17p-40-1": f17, "19p-44-1": f19, "20p-46-1": f20, "21p-48-1": f21, "26p-61-1": f26a,
        "26p-62-1": f26b, "72p-57-1": f72, "81p-5-1": f81}  # 원문에 그림이 있던 문항만 (80p-1 은 원문에 그림 없음)
