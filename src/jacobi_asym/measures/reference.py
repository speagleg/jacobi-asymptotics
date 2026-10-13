"""Exactly solvable reference families (math-pursuits item 11, PROOF.md Thm A and §7 TC fact).

Lommel (p = 2): K_nu has zero diagonal and off-diagonal c_m = 1/(2 sqrt((m+nu+1)(m+nu+2))); folding its spectral
measure to u = x^2 gives atoms j_{nu,k}^{-2} ('even'); 'odd' is u * that measure.  Tricomi-Carlitz (p = 1):
off-diagonal^2 lambda_m = m/((m+alpha)(m+alpha-1)), atoms 1/(k+alpha), k >= 0.
"""
from fractions import Fraction
import mpmath as mp
import numpy as np
from .base import DiscreteMeasure


def _num(v):
    return Fraction(v) if isinstance(v, (int, Fraction)) else mp.mpf(v)


def _fold(lam, n, variant):
    if variant == "even":
        return [lam(2 * j - 2) + lam(2 * j - 1) for j in range(1, n + 1)], [lam(2 * j - 1) * lam(2 * j) for j in range(1, n + 1)]
    if variant == "odd":
        return [lam(2 * j - 1) + lam(2 * j) for j in range(1, n + 1)], [lam(2 * j) * lam(2 * j + 1) for j in range(1, n + 1)]
    raise ValueError("variant must be 'even' or 'odd'")


def lommel_coeffs(nu, n: int, variant: str = "even"):
    nu = _num(nu)
    # lam(q) := c^2_{q-1} = off-diagonal^2 between rows q-1 and q of K_nu; lam(0) = 0
    lam = lambda q: 0 * nu if q == 0 else 1 / (4 * (q + nu) * (q + nu + 1))
    return _fold(lam, n, variant)


def tc_coeffs(alpha, n: int, variant: str = "even"):
    al = _num(alpha)
    lam = lambda m: 0 * al if m == 0 else m / ((m + al) * (m + al - 1))
    return _fold(lam, n, variant)


def lommel_measure(nu: float, K: int, dps: int = 30) -> DiscreteMeasure:
    with mp.workdps(dps):
        j = [mp.besseljzero(mp.mpf(nu), k) for k in range(1, K + 1)]
        x = np.array([float(1 / t ** 2) for t in j])
    return DiscreteMeasure(x, 4 * (nu + 1) * x, label=f"lommel(nu={nu}, K={K})")
