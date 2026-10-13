"""Exact (mpmath) Hankel determinant and Heine/Andreief sum for small measures (cross-checks)."""
from itertools import combinations
import mpmath as mp
from ..measures.base import DiscreteMeasure


def hankel_det_mp(mu: DiscreteMeasure, n: int, dps: int = 50):
    with mp.workdps(dps):
        x = [mp.mpf(float(v)) for v in mu.atoms]
        w = [mp.mpf(float(v)) for v in mu.weights]
        m = [mp.fsum(wi * xi ** r for xi, wi in zip(x, w)) for r in range(2 * n - 1)]
        return mp.det(mp.matrix([[m[i + j] for j in range(n)] for i in range(n)]))


def heine_sum_mp(mu: DiscreteMeasure, n: int, dps: int = 50):
    if mu.N > 14:
        raise ValueError("heine_sum_mp enumerates subsets; use N <= 14")
    with mp.workdps(dps):
        x = [mp.mpf(float(v)) for v in mu.atoms]
        w = [mp.mpf(float(v)) for v in mu.weights]
        tot = mp.mpf(0)
        for S in combinations(range(len(x)), n):
            t = mp.fprod(w[i] for i in S)
            for i, j in combinations(S, 2):
                t *= (x[i] - x[j]) ** 2
            tot += t
        return tot
