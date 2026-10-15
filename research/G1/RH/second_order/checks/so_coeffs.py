"""Plan 62 (NUMERICAL): Jacobi coefficients of sigma_{p,s} = sum_{k>=1} k^{-s} delta_{k^{-p}} with a controlled tail.

Measure used:  sum_{k<=K} k^{-s} delta_{k^{-p}}  +  Gauss-Jacobi quadrature (M nodes) of the continuum tail
    T_K(f) := int_{K+1/2}^inf t^{-s} f(t^{-p}) dt = (1/p) int_0^X x^beta f(x) dx,  X = (K+1/2)^{-p}, beta = (s-1)/p - 1,
which reproduces T_K exactly on polynomials of degree <= 2M-1, hence (M >= nmax+2) the first nmax Jacobi coefficients
of (atoms + T_K) exactly.  The remaining error is the midpoint Euler-Maclaurin defect sum_{k>K} g(k) - T_K(f)
= g'(K+1/2)/24 + ..., measured by K -> 2K (Rule N: precision/truncation differences are estimates, not bounds).
Coefficients: binary128 RKPW kernel (csrc), atoms stored as float64 (relative perturbation 1e-16 of the measure).
Output convention: alpha[k] = alpha_k (k = 0..nmax-1, monic p_{k+1} = (x - alpha_k) p_k - b_k^2 p_{k-1}),
b[n-1] = b_n (n = 1..nmax).  Repo (item 11) indexing: a_n = alpha_{n-1}."""
import os
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.special import roots_jacobi
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw

CACHE = Path(__file__).resolve().parents[5] / "tmp" / "plan62_cache"


def c_p_mp(p):
    p = mp.mpf(p)
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + mp.mpf(1) / 2) / mp.gamma(1 / p + 1)
    return (mp.pi / (2 * I)) ** p / 4


def measure(p, s, K, M, delta=0.0):
    """atoms (k+delta)^{-p}, weights (k+delta)^{-s}, k = 1..K, plus the Gauss-Jacobi continuum tail beyond K + 1/2."""
    k = np.arange(1, K + 1, dtype=np.float64) + delta
    x, w = k ** (-p), k ** (-s)
    beta = (s - 1) / p - 1
    u, wu = roots_jacobi(M, 0.0, beta)              # weight (1+u)^beta on [-1, 1]
    X = (K + 0.5 + delta) ** (-p)
    xt = X * (1 + u) / 2
    wt = wu * (X / 2) ** (beta + 1) / p
    return DiscreteMeasure.from_atoms(x, w, tail=(xt, wt))


def coeffs(p, s, K, nmax, delta=0.0):
    """returns (alpha, b) as mpf arrays (dps 40), alpha_0..alpha_{nmax-1}, b_1..b_nmax; cached.
    delta != 0: shifted lattice (k+delta)^{-p} with weights (k+delta)^{-s} (used only by check_so_lattice.py)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    tag = "" if delta == 0 else f"_d{delta}"
    f = CACHE / f"p{p}_s{s}_K{K}_n{nmax}{tag}.txt"
    mp.mp.dps = 40
    if f.exists():
        rows = [l.split() for l in open(f)]
        return (np.array([mp.mpf(r[0]) for r in rows], dtype=object),
                np.array([mp.mpf(r[1]) for r in rows], dtype=object))
    mu = measure(p, s, K, nmax + 8, delta)
    jc = jacobi_rkpw(mu, nmax + 1, prec="q")
    alpha = np.array(jc.a[:nmax], dtype=object)
    b = np.array([mp.sqrt(v) for v in jc.b2[:nmax]], dtype=object)
    with open(f, "w") as fh:
        for a_, b_ in zip(alpha, b):
            fh.write(f"{mp.nstr(a_, 36)} {mp.nstr(b_, 36)}\n")
    return alpha, b
