"""Plan 62 helpers (NUMERICAL): sequences and asymptotic fits.
y_n  := n^p b_n / c(p) - 1                      ~ d1/n + d2/n^2 + ...
er_n := alpha_{n-1}/(2 b_n) - 1   (repo pairing a_n/(2b_n), a_n = alpha_{n-1})   ~ e1/n + ...
es_n := alpha_n/(2 b_n) - 1       (Paper 2 / standard pairing)                    ~ e1s/n + ...
g_N  := gamma_N^2 / (c (N/2)^{-p}) - 1          ~ (k0 + k1 (-1)^N)/N + ...   (symmetric chain, gamma_0 = 0:
        alpha_0 = gamma_1^2, b_m^2 = gamma_{2m-1}^2 gamma_{2m}^2, alpha_m = gamma_{2m}^2 + gamma_{2m+1}^2)."""
import numpy as np
import mpmath as mp
from so_coeffs import c_p_mp


def sequences(p, alpha, b):
    mp.mp.dps = 40
    c = c_p_mp(p)
    nmax = len(b)
    n = np.arange(1, nmax + 1)
    y = np.array([float(mp.mpf(int(k)) ** p * b[k - 1] / c - 1) for k in n])
    er = np.array([float(alpha[k - 1] / (2 * b[k - 1]) - 1) for k in n])
    es = np.array([float(alpha[k] / (2 * b[k - 1]) - 1) for k in n[:-1]] + [np.nan])
    # chain
    gam = [mp.mpf(0)] * (2 * nmax + 1)
    gam[1] = alpha[0]
    for m in range(1, nmax):
        gam[2 * m] = b[m - 1] ** 2 / gam[2 * m - 1]
        gam[2 * m + 1] = alpha[m] - gam[2 * m]
    N = np.arange(1, 2 * nmax)
    g = np.array([float(gam[k] / (c * (mp.mpf(int(k)) / 2) ** (-p)) - 1) for k in N])
    return n, y, er, es, N, g


def exponents(p, J):
    """the first J exponents of {1 + i + j p : i, j >= 0} (sorted, duplicates merged at tolerance 1e-9)."""
    E = sorted({round(1 + i + j * p, 9) for i in range(J + 2) for j in range(J + 2)})
    return E[:J]


def fit(n, v, J, p=None, parity=False, logterm=False):
    """least squares v ~ sum_e d_e n^{-e} over the first J exponents (integers if p is None), optionally
    + parity terms (-1)^n n^{-e} over the same exponents, + a term n^{-2} log n.  Returns (exps, coef)."""
    n = np.asarray(n, float)
    E = list(range(1, J + 1)) if p is None else exponents(p, J)
    n0 = n.min()
    cols, names = [], []
    for e in E:
        cols.append((n0 / n) ** e); names.append(("", e))
    if parity:
        for e in E:
            cols.append((-1.0) ** n * (n0 / n) ** e); names.append(("par", e))
    if logterm:
        cols.append((n0 / n) ** 2 * np.log(n / n0)); names.append(("log", 2))
    A = np.vstack(cols).T
    co = np.linalg.lstsq(A, v, rcond=None)[0]
    return names, co * np.array([n0 ** e for _, e in names])


def first_coef(n, v, p=None, Js=(4, 5, 6, 7), fracs=(0.1, 0.2, 0.3), parity=False, logterm=False, which=("", 1)):
    """estimate of one coefficient (default the n^{-1} one) over orders J and windows [frac*nmax, nmax]:
    returns (median, half-range, all estimates)."""
    n = np.asarray(n); v = np.asarray(v)
    ok = np.isfinite(v)
    nmax = n[ok].max()
    est = []
    for J in Js:
        for fr in fracs:
            m = ok & (n >= fr * nmax)
            names, co = fit(n[m], v[m], J, p, parity, logterm)
            est.append(co[names.index(which)])
    est = np.array(est)
    return float(np.median(est)), float((est.max() - est.min()) / 2), est
