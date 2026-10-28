"""LS_ZETA common: Jacobi coefficients of measures on reciprocal ordinates by the discretized Stieltjes procedure (stable for
n << number of atoms), the smooth zeta-zero counting function, GUE null spectra, and CLEAN in the phase variable T*(n).
NUMERICAL.  No claim about RH: the ordinates are inputs (item 11, E1).

Measure: mu = sum_k T_k^{-s} delta_{1/T_k} over explicit atoms (data below T_cut, smooth continuation N̄^{-1}(k - 1/2) above,
up to K_tot atoms).  Data and comparator share the continuation, so the truncation enters D_n only at second order;
lz_validate.py measures it against the exact Arb pipeline of ls_common on a Hurwitz case.
D_n := n (b_n / b_n^smooth - 1)   (for a lattice this is n^2 (b_n - b_n^s)/c, the D of LS_BOLZA).
Phase variable: T*(n) solves  int (1 - T/T*)^{-1/2} rhō(T) dT = n + 1/2  (the continuum soft-edge condition, SPEC §3.16;
rhō = dN̄/dT); a constant shift of n only moves phases, not line positions."""
import math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad


# ---------------------------------------------------------------- Stieltjes procedure
def stieltjes(x, w, n, dtype=np.float64):
    """recurrence coefficients (alpha_k, beta_k = b_k^2), k < n, of sum w_i delta_{x_i} (discretized Stieltjes; three-term
    recurrence of normalised vectors)."""
    x = np.asarray(x, dtype=dtype); w = np.asarray(w, dtype=dtype)
    al = np.zeros(n, dtype=dtype); be = np.zeros(n, dtype=dtype)
    p_prev = np.zeros_like(x); p = np.ones_like(x)
    nrm = np.sum(w*p*p); be[0] = nrm
    for k in range(n):
        al[k] = np.sum(w*x*p*p)/nrm
        if k == n - 1: break
        p_next = (x - al[k])*p - (be[k] if k > 0 else 0)*p_prev
        nrm_next = np.sum(w*p_next*p_next)
        be[k + 1] = nrm_next/nrm
        # rescale to avoid under/overflow
        sc = math.sqrt(float(nrm_next))
        p_prev, p, nrm = p/sc, p_next/sc, nrm_next/(sc*sc)
    return al, be


def D_of(be, bes, n0=1):
    b = np.sqrt(be.astype(np.float64)); bs = np.sqrt(bes.astype(np.float64))
    n = np.arange(len(b))
    return {int(k): float(k*(b[k]/bs[k] - 1)) for k in range(n0, len(b))}


# ---------------------------------------------------------------- zeta-zero smooth counting
def Nbar(T):
    return T/(2*math.pi)*math.log(T/(2*math.pi)) - T/(2*math.pi) + 7/8


def rhobar(T):
    return math.log(T/(2*math.pi))/(2*math.pi) if T > 2*math.pi else 0.0


def Nbar_inv(y, lo=7.0, hi=1e9):
    return brentq(lambda T: Nbar(T) - y, lo, hi, xtol=1e-13, rtol=1e-15)


def smooth_nodes(k_from, k_to):
    """T_k = N̄^{-1}(k - 1/2), k in [k_from, k_to) (vectorised Newton from the asymptotic guess)."""
    k = np.arange(k_from, k_to, dtype=np.float64); y = k - 0.5
    T = 2*np.pi*np.maximum(y, 1.0)/np.maximum(np.log(np.maximum(y, 3.0)), 1.0) + 15
    for _ in range(60):
        f = T/(2*np.pi)*np.log(T/(2*np.pi)) - T/(2*np.pi) + 7/8 - y
        T = T - f/(np.log(T/(2*np.pi))/(2*np.pi))
    return T


def Tstar(n, shift=0.5):
    def F(Ts):                                    # T = Ts (1 - v^2): smooth integrand
        vmax = math.sqrt(1 - 2*math.pi/Ts)
        return quad(lambda v: 2*Ts*rhobar(Ts*(1 - v*v)), 0, vmax, limit=200)[0] - (n + shift)
    return brentq(F, 2*math.pi + 1e-6, 1e7)


# ---------------------------------------------------------------- GUE null (Dumitriu–Edelman beta = 2), unfolded
def gue_unfolded(N, rng, keep=0.6):
    """eigenvalues of the beta = 2 Hermite tridiagonal model of size N, unfolded by the exact semicircle CDF to unit density;
    returns the middle `keep` fraction, shifted to start near 1."""
    from scipy.linalg import eigh_tridiagonal
    d = rng.normal(0, math.sqrt(2), N)/math.sqrt(2)
    e = np.sqrt(rng.chisquare(2*np.arange(N - 1, 0, -1)))/math.sqrt(2)
    ev = eigh_tridiagonal(d, e, eigvals_only=True)
    R = 2*math.sqrt(N)                                    # semicircle radius sqrt(2 beta N) at beta = 2
    x = np.clip(ev/R, -1, 1)
    cdf = N*(0.5 + (x*np.sqrt(1 - x*x) + np.arcsin(x))/math.pi)
    i0 = int(N*(1 - keep)/2); u = cdf[i0:i0 + int(N*keep)]
    return u - u[0] + 1.0


# ---------------------------------------------------------------- explicit-formula lines (for the positive control)
def primes_upto(P):
    s = [True]*(P + 1); s[0] = s[1] = False
    for i in range(2, int(P**0.5) + 1):
        if s[i]: s[i*i::i] = [False]*len(s[i*i::i])
    return [i for i in range(P + 1) if s[i]]


def S_lines(T, P=13, kmax=3):
    """-(1/pi) sum_{p <= P, k <= kmax} sin(k T log p)/(k p^{k/2})  (truncated explicit formula for S(T))."""
    out = np.zeros_like(np.asarray(T, dtype=float))
    for p in primes_upto(P):
        for k in range(1, kmax + 1):
            out -= np.sin(k*np.asarray(T)*math.log(p))/(k*p**(k/2))/math.pi
    return out


# ---------------------------------------------------------------- CLEAN in a phase variable
def clean_var(x, y, ells, k=6, detrend=2):
    """CLEAN with constant-amplitude sinusoids in x (after a degree-`detrend` polynomial); returns [(l, amplitude, phase)]."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    xc = (x - x.mean())/(x.std() if x.std() > 0 else 1)
    P = np.vstack([xc**j for j in range(detrend + 1)]).T
    y = y - P @ np.linalg.lstsq(P, y, rcond=None)[0]
    out = []
    C = np.cos(np.outer(ells, x)); Sn = np.sin(np.outer(ells, x))
    for _ in range(k):
        best = None
        for i, l in enumerate(ells):
            X = np.vstack([C[i], Sn[i]] + [xc**j for j in range(detrend + 1)]).T
            c = np.linalg.lstsq(X, y, rcond=None)[0]
            rr = float(np.sum((y - X @ c)**2))
            if best is None or rr < best[0]: best = (rr, l, c, X)
        rr, l, c, X = best
        y = y - X[:, :2] @ c[:2]
        out.append((float(l), float(math.hypot(c[0], c[1])), float(math.atan2(-c[1], c[0]))))
    return out


def lanczos(x, w, n):
    """recurrence coefficients (alpha_k, beta_k = b_k^2) of sum w_i delta_{x_i} by Lanczos on diag(x) with the start vector
    sqrt(w)/|sqrt(w)| and full reorthogonalisation (twice per step); beta_0 = sum w."""
    x = np.asarray(x, np.float64); w = np.asarray(w, np.float64)
    M = len(x); Q = np.zeros((n, M)); al = np.zeros(n); be = np.zeros(n)
    q = np.sqrt(w); be[0] = float(np.sum(w)); q /= np.linalg.norm(q)
    Q[0] = q; bprev = 0.0
    for k in range(n):
        v = x*Q[k]
        al[k] = float(np.dot(Q[k], v))
        if k == n - 1: break
        v -= al[k]*Q[k]
        if k > 0: v -= bprev*Q[k - 1]
        for _ in range(2):
            v -= Q[:k + 1].T @ (Q[:k + 1] @ v)
        bk = float(np.linalg.norm(v)); be[k + 1] = bk*bk; bprev = bk
        Q[k + 1] = v/bk
    return al, be


def tail_quadrature(xK, density, m):
    """m-point Gauss–Legendre stand-in for the continuum tail density*dx on (0, xK]."""
    t, wt = np.polynomial.legendre.leggauss(m)
    return xK*(t + 1)/2, density*xK*wt/2


def zeta_tail(T_end, J=70, m=16):
    """composite Gauss–Legendre stand-in for the continuum tail of mu beyond T_end: masses T^{-2} rhō(T) dT become
    rhō(1/x) dx on (0, 1/T_end] (log-singular at 0), on geometric panels [x_e 2^{-j-1}, x_e 2^{-j}], j < J, plus [0, x_e 2^{-J}]."""
    xe = 1.0/T_end; t, wt = np.polynomial.legendre.leggauss(m); xs = []; ws = []
    edges = [xe*2.0**(-j) for j in range(J + 1)] + [0.0]
    for hi, lo in zip(edges[:-1], edges[1:]):
        xx = lo + (hi - lo)*(t + 1)/2; ww = (hi - lo)*wt/2
        dens = np.log(1/(2*np.pi*xx))/(2*np.pi)
        xs.append(xx); ws.append(ww*dens)
    return np.concatenate(xs), np.concatenate(ws)


def zero_measure(T_atoms, K_data):
    """atoms 1/T_k with masses T_k^{-2} for k <= K_data (T_atoms), then the continuum tail from N̄ = K_data."""
    T_end = Nbar_inv(float(K_data))
    xq, wq = zeta_tail(T_end)
    T = np.asarray(T_atoms, float)
    return np.concatenate([1/T, xq]), np.concatenate([T**-2.0, wq])
