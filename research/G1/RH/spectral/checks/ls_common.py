"""LS_BOLZA common: Jacobi coefficients of a measure on reciprocal eigenvalues with an exact smooth (Hurwitz) tail, the
fluctuation D_n against the smooth comparator, and a least-squares periodogram in r = sqrt(lambda* - 1/4).  Nothing fitted
here except where a function says so.

Measure (p = 1):  mu = sum_{lambda_i < lambda_cut} w_i delta_{1/lambda_i}  +  sum_{k >= K} lam_k^{-s} delta_{1/lam_k},
  lam_k = (k + a)/nu  (the smooth continuation: node counting N(lambda) = nu*lambda + 1/2 - a);
  moments of the tail are exact: sum_{k>=K} lam_k^{-s-j} = nu^{s+j} zeta(s + j, K + a)  (Arb Hurwitz zeta).
Comparator: the full smooth lattice lam_k, k >= 1 (a Hurwitz lattice: JZC_P1 / Paper IV Thm 6.1 at p = 1).
Recurrence: classical Chebyshev algorithm on the moments in ball arithmetic; the relative radius of the last b_n^2 is reported.
Normalisation: b_n of the unit-density lattice ~ c/n with c = 1/2; nodes scaled by nu => c_eff = nu/2,
  y_n = n b_n / c_eff - 1,  D_n := n (y_n - y_n^smooth) = n^2 (b_n - b_n^smooth)/c_eff.
Edge: u = 1 at lambda*(n) = n/(2 nu) (unit-density edge lambda' = n/(4c) = n/2, rescaled)."""
import math
from flint import arb, fmpq, ctx
import mpmath as mp


def chebyshev(M, n):
    m = 2*n; sp_ = [arb(0)]*m; sc = M[:m]; al = [sc[1]/sc[0]]; be = [sc[0]]
    for k in range(1, n):
        new = [arb(0)]*m
        for l in range(k, m - k): new[l] = sc[l + 1] - al[k - 1]*sc[l] - be[k - 1]*sp_[l]
        al.append(new[k + 1]/new[k] - sc[k]/sc[k - 1]); be.append(new[k]/sc[k - 1]); sp_, sc = sc, new
    return al, be


def to_arb(x):
    if isinstance(x, arb): return x
    if isinstance(x, (tuple, list)): return arb(fmpq(*x))
    return arb(str(x)) if isinstance(x, str) else arb(mp.nstr(mp.mpf(x), 60) if not isinstance(x, int) else x)


def moments(nodes, weights, nu, a, K, s, n, prec):
    """nodes: eigenvalues lambda_i (strings / mpf / arb) below the cut; weights: masses w_i (multiply lambda^-s);
    tail lattice (k + a)/nu for k >= K."""
    ctx.prec = prec
    NU, A, S = to_arb(nu), to_arb(a), to_arb(s)
    m = 2*n; M = [arb(0)]*m
    for lam, w in zip(nodes, weights):
        L = to_arb(lam); x = 1/L; xi = to_arb(w)*L**(-S)
        for i in range(m): M[i] += xi; xi *= x
    if K is not None:
        for i in range(m): M[i] += NU**(S + i)*(S + i).zeta(A + K)
    return M


def b2_series(nodes, weights, nu, a, K, s, n, prec):
    al, be = chebyshev(moments(nodes, weights, nu, a, K, s, n, prec), n)
    rel = be[n - 1].rad()/be[n - 1]
    bits = float(rel.mid().log()/math.log(2)) if rel.mid() > 0 else -prec
    return [mp.mpf(x.mid().str(80, radius=False)) for x in be], bits


def D_series(b2, b2s, nu, nmin=1):
    ce = mp.mpf(nu)/2
    return {n: n*n*(mp.sqrt(b2[n]) - mp.sqrt(b2s[n]))/ce for n in range(nmin, len(b2))}


def rstar(n, nu, shift=0):
    lam = (n + shift)/(2*mp.mpf(nu))
    return mp.sqrt(lam - mp.mpf(1)/4)


def periodogram(ns, D, nu, ells, detrend=2, shift=0):
    """least-squares power of A cos(l r) + B sin(l r) in D_n (n in ns) after removing a polynomial in r of degree `detrend`;
    returns list of (l, amplitude sqrt(A^2+B^2))."""
    import numpy as np
    r = np.array([float(rstar(n, nu, shift)) for n in ns]); y = np.array([float(D[n]) for n in ns])
    P = np.vstack([r**k for k in range(detrend + 1)]).T
    y = y - P @ np.linalg.lstsq(P, y, rcond=None)[0]
    out = []
    for l in ells:
        X = np.vstack([np.cos(l*r), np.sin(l*r)] + [r**k for k in range(detrend + 1)]).T
        c = np.linalg.lstsq(X, y, rcond=None)[0]
        out.append((l, float(math.hypot(c[0], c[1]))))
    return out


def peaks(pg, k=5, sep=0.25):
    pts = sorted(pg, key=lambda t: -t[1]); sel = []
    for l, p in pts:
        if all(abs(l - q) > sep for q, _ in sel): sel.append((l, p))
        if len(sel) == k: break
    return sel


def invert_counting(Nfun, k, lo, hi):
    """lambda with Nfun(lambda) = k - 1/2 (bisection; Nfun increasing on [lo, hi])."""
    t = mp.mpf(k) - mp.mpf(1)/2
    for _ in range(200):
        mid = (lo + hi)/2
        if Nfun(mid) < t: lo = mid
        else: hi = mid
    return (lo + hi)/2


def clean(ns, D, nu, ells, k=4, detrend=2, shift=0, grow=0.5):
    """CLEAN: repeatedly find the frequency whose model r^grow (A cos(l r) + B sin(l r)) best fits the current residual
    (after a degree-`detrend` polynomial in r), record (l, A, B), subtract the fitted line, repeat k times.  grow = 1/2 is the
    edge law's sqrt(l r) amplitude growth (LS_BOLZA §2).  Returns [(l, amplitude at the window's mean r, phase)]."""
    import numpy as np
    r = np.array([float(rstar(n, nu, shift)) for n in ns]); y = np.array([float(D[n]) for n in ns])
    P = np.vstack([r**j for j in range(detrend + 1)]).T
    y = y - P @ np.linalg.lstsq(P, y, rcond=None)[0]
    w = r**grow; rm = float(np.mean(r)); out = []
    for _ in range(k):
        best = None
        for l in ells:
            X = np.vstack([w*np.cos(l*r), w*np.sin(l*r)] + [r**j for j in range(detrend + 1)]).T
            c, res, *_ = np.linalg.lstsq(X, y, rcond=None)
            rr = float(np.sum((y - X @ c)**2))
            if best is None or rr < best[0]: best = (rr, l, c, X)
        rr, l, c, X = best
        y = y - X[:, :2] @ c[:2]
        out.append((l, float(math.hypot(c[0], c[1])*rm**grow), float(math.atan2(-c[1], c[0]))))
    return out
