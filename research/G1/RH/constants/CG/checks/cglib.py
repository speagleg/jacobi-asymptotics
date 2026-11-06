"""Shared helpers for the CG constant checks (Rule N: numerical, mpmath, precision-doubling).

sigma_{p,s} = sum_k k^{-s} delta_{k^{-p}}, moments m_j = zeta(s + j p).
Recurrence xP_n = P_{n+1} + a_n P_n + b_n^2 P_{n-1} from the moments by the Chebyshev algorithm
(the same algorithm as research/program/connections/lead-verification/cg.py).
"""
import mpmath as mp


def recurrence(p, s, n, moments=None):
    """Return lists alpha[0..n], beta[0..n] with beta[0]=h_0, beta[k]=b_k^2 (k>=1)."""
    p = mp.mpf(p); s = mp.mpf(s)
    L = 2 * n + 2
    m = moments if moments is not None else [mp.zeta(s + j * p) for j in range(L)]
    sig_prev = [mp.mpf(0)] * L
    sig = list(m)
    alpha = [m[1] / m[0]]
    beta = [m[0]]
    for k in range(1, n + 1):
        new = [mp.mpf(0)] * L
        for l in range(k, 2 * n - k + 1):
            new[l] = sig[l + 1] - alpha[k - 1] * sig[l] - beta[k - 1] * sig_prev[l]
        alpha.append(new[k + 1] / new[k] - sig[k] / sig[k - 1])
        beta.append(new[k] / sig[k - 1])
        sig_prev, sig = sig, new
    return alpha, beta


def christoffel_at(x, alpha, beta, mmax):
    """Return dict m -> K_m(x,0) and K_m(0,0) data: lists P_k(0), P_k(x), h_k for k<mmax."""
    P0 = [mp.mpf(1)]; Px = [mp.mpf(1)]; h = [beta[0]]
    for k in range(mmax - 1):
        bk = beta[k] if k > 0 else 0
        P0m = P0[k - 1] if k > 0 else 0
        Pxm = Px[k - 1] if k > 0 else 0
        P0.append((0 - alpha[k]) * P0[k] - bk * P0m)
        Px.append((x - alpha[k]) * Px[k] - bk * Pxm)
        h.append(h[k] * beta[k + 1])
    return P0, Px, h


def c_of_p(p):
    p = mp.mpf(p)
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + mp.mpf(1) / 2) / mp.gamma(1 / p + 1)
    return (mp.pi / (2 * I)) ** p / 4


def conj_constant(p, s):
    """Conjecture CG: lambda_m ~ CONST * N^{-E}."""
    p = mp.mpf(p); s = mp.mpf(s)
    z = (s - 1) / p
    E = (p + 2) * z
    C = mp.gamma(z) * mp.gamma(z + 1) / p * (c_of_p(p) * (p + 2) ** 2) ** z
    return C, E


def richardson(vals, ms, K):
    """Fit vals[m] = sum_{k<=K} c_k m^{-k}; return c_0."""
    A = mp.matrix([[mp.mpf(m) ** (-k) for k in range(K + 1)] for m in ms])
    b = mp.matrix([vals[m] for m in ms])
    return mp.lu_solve(A, b)[0]
