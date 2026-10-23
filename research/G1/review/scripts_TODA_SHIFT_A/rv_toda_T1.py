"""Reviewer spot check of JZC_TODA Lemma T.1, independent of toda_measures.py: exact rational arithmetic with dual numbers
(first order in t), Stieltjes procedure on a random finite measure (M atoms), tilts x^j for j = 4, 5, 6 (the author used j <= 3).
Checks, for every n < M: d log h_n = (L^j)_{nn}; d log b_n^2 = (L^j)_{nn} - (L^j)_{n-1,n-1}; d a_n = F(n) - F(n-1), F(n) = (L^j)_{n+1,n},
F(M-1) = 0; d pi_n = -sum_{m<n} (L^j)_{nm} pi_m (coefficientwise).  Controls: F(n) = (L^j)_{n,n+1}; (L^{j+1})_{nn}."""
import random
from fractions import Fraction as Fr

class D:   # dual number a + b eps
    __slots__ = ('a', 'b')
    def __init__(s, a, b=0): s.a, s.b = Fr(a), Fr(b)
    def __add__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a + o.a, s.b + o.b)
    __radd__ = __add__
    def __sub__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a - o.a, s.b - o.b)
    def __rsub__(s, o): return D(o) - s
    def __mul__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a * o.a, s.a * o.b + s.b * o.a)
    __rmul__ = __mul__
    def __truediv__(s, o): o = o if isinstance(o, D) else D(o); return D(s.a / o.a, (s.b * o.a - s.a * o.b) / o.a ** 2)
    def __neg__(s): return D(-s.a, -s.b)

def polymul_x(c): return [Fr(0)] + c   # coefficient lists, low degree first, entries D
def run(M, j, seed):
    rnd = random.Random(seed)
    xs = sorted({Fr(rnd.randint(-40, 40), rnd.randint(1, 13)) for _ in range(3 * M)})[:M]
    ws = [Fr(rnd.randint(1, 30), rnd.randint(1, 9)) for _ in xs]
    W = [D(w, w * x ** j) for w, x in zip(xs and ws, xs)]   # weight w (1 + eps x^j)
    ip = lambda f, g: sum((W[k] * ev(f, xs[k]) * ev(g, xs[k]) for k in range(M)), D(0))
    def ev(c, x):
        r = D(0)
        for co in reversed(c): r = r * x + co
        return r
    pis = [[D(1)]]; a = []; B = [None]; h = [ip(pis[0], pis[0])]
    for n in range(M):
        xp = [D(0)] + pis[n]
        an = ip(xp, pis[n]) / h[n]; a.append(an)
        if n == M - 1: break
        nxt = [xp[i] - an * (pis[n][i] if i < len(pis[n]) else 0) - (B[n] * pis[n - 1][i] if n >= 1 and i < len(pis[n - 1]) else 0) for i in range(len(xp))]
        pis.append(nxt); h.append(ip(nxt, nxt)); B.append(h[n + 1] / h[n])
    # monic Jacobi matrix L at eps = 0 (M x M): L[n][n] = a_n, L[n][n+1] = 1, L[n+1][n] = b_{n+1}^2
    L = [[Fr(0)] * M for _ in range(M)]
    for n in range(M):
        L[n][n] = a[n].a
        if n + 1 < M: L[n][n + 1] = Fr(1); L[n + 1][n] = B[n + 1].a
    def mpow(A, e):
        R = [[Fr(int(i == k)) for k in range(M)] for i in range(M)]
        for _ in range(e): R = [[sum(R[i][l] * A[l][k] for l in range(M)) for k in range(M)] for i in range(M)]
        return R
    Lj, Lj1 = mpow(L, j), mpow(L, j + 1)
    F = lambda n: Lj[n + 1][n] if n + 1 < M else Fr(0)
    Fc = lambda n: Lj[n][n + 1] if n + 1 < M else Fr(0)
    ok = ctl = 0; nid = nct = 0
    for n in range(M):
        nid += 4
        ok += (h[n].b / h[n].a == Lj[n][n])
        ok += (n == 0) or (B[n].b / B[n].a == Lj[n][n] - Lj[n - 1][n - 1])
        ok += (a[n].b == F(n) - (F(n - 1) if n >= 1 else 0))
        # d pi_n coefficients
        dp = [c.b for c in pis[n]] if n < len(pis) else None
        rhs = [Fr(0)] * (n + 1)
        for m in range(n):
            for i, c in enumerate(pis[m]): rhs[i] -= Lj[n][m] * c.a
        ok += (dp == rhs)
        nct += 2
        ctl += (a[n].b == Fc(n) - (Fc(n - 1) if n >= 1 else 0)) and Fc(n) != F(n)
        ctl += (h[n].b / h[n].a == Lj1[n][n])
    return nid, ok, nct, ctl

tot = [0, 0, 0, 0]
for j in (4, 5, 6):
    for seed in (1, 2, 3):
        r = run(7, j, seed + 10 * j)
        print(f"j = {j}, seed {seed}: identities {r[1]}/{r[0]} hold; controls holding {r[3]}/{r[2]}")
        tot = [x + y for x, y in zip(tot, r)]
print(f"TOTAL identities {tot[1]}/{tot[0]} hold; controls that (wrongly) hold: {tot[3]}/{tot[2]}")
