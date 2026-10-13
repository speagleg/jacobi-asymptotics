"""Pins the Lean definition jb2 k = D_{k+1} D_{k-1} / D_k^2 to the toolkit's b2 convention."""
import mpmath as mp
import numpy as np
from jacobi_asym.measures import DiscreteMeasure
from jacobi_asym.jacobi import jacobi_mp
from jacobi_asym.hankel import hankel_det_mp


def test_b2_equals_hankel_ratio():
    rng = np.random.default_rng(4)
    mu = DiscreteMeasure.from_atoms(rng.uniform(0.05, 1.0, 12), rng.uniform(0.2, 1.5, 12))
    a, b2 = jacobi_mp(mu, 6, dps=60)
    with mp.workdps(60):
        D = [mp.mpf(1)] + [hankel_det_mp(mu, n, dps=60) for n in range(1, 8)]
        for k in range(1, 6):
            assert abs(b2[k - 1] / (D[k + 1] * D[k - 1] / D[k] ** 2) - 1) < mp.mpf(10) ** -40
