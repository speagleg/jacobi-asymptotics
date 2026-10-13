"""Law-P constants and the Weyl-law (local arcsine) predictor (item 11 note (W), (P); PROOF.md section 1)."""
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import gamma

_GL = np.polynomial.legendre.leggauss(200)


def I_p(p: float) -> float:
    return float(np.sqrt(np.pi) / 2 * gamma(1 / p + 0.5) / gamma(1 / p + 1))


def c_p(p: float) -> float:
    return float(0.25 * (np.pi / (2 * I_p(p))) ** p)


def K_weyl(alpha: float, beta: float, p: float) -> float:
    def th(u):
        s = (u ** p - alpha) / (2 * beta)
        return np.arccos(np.clip(s, -1.0, 1.0))
    top = (alpha + 2 * beta) ** (1 / p)
    pts = [(alpha - 2 * beta) ** (1 / p)] if alpha - 2 * beta > 0 else None
    return float(quad(th, 0, top, points=pts, limit=200, epsabs=1e-12, epsrel=1e-12)[0] / np.pi)


def weyl_count(eps: float, a, b) -> float:
    z = np.clip((eps - np.asarray(a, float)) / (2 * np.asarray(b, float)), -1, 1)
    return float(np.sum(np.arccos(z)) / np.pi)


def _n_of_B(B, f, finv):
    t, w = _GL
    xiB = float(finv(B))
    k0 = int(np.floor(xiB / 2))
    s = 0.0
    if k0 >= 1:
        k = np.arange(1, k0 + 1, dtype=float)
        s = float(np.sum(1 / np.sqrt(-np.expm1(np.log(B) - np.log(f(k))))))
    lo = k0 + 0.5 if k0 >= 1 else 0.5
    u = (t + 1) / 2
    xi = xiB - (xiB - lo) * u ** 2                     # removes the (xi_B - xi)^{-1/2} singularity
    integrand = 2 * (xiB - lo) * u / np.sqrt(-np.expm1(np.log(B) - np.log(f(xi))))
    return s + float(np.sum(w / 2 * integrand))


def predict_b(n: int, f, finv) -> float:
    """b_n^W from the smoothed Weyl inversion (P).  f: decreasing atom function on xi >= 1/2, finv its inverse.
    f must accept numpy arrays (it is evaluated on arrays of nodes)."""
    if n < 2:
        raise ValueError("predict_b needs n >= 2 (the bracket degenerates at n = 1)")
    g = lambda lB: _n_of_B(np.exp(lB), f, finv) - n
    lo = np.log(f(2.0 * n + 2))                      # count there is >= n + 1 > n
    hi = np.log(f(1.0))
    if g(hi) >= 0:                                   # slowly decaying f: push xi_B down towards 1/2
        hi = np.log(f(0.5 + 1e-6))
        if g(hi) >= 0:
            raise ValueError(f"predict_b: cannot bracket n = {n} for this f (n(B) >= n already at xi_B ~ 1/2)")
    lB = brentq(g, lo, hi, xtol=1e-14)
    return float(np.exp(lB) / 4)
