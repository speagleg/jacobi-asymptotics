import numpy as np
import mpmath as mp
import pytest
from jacobi_asym.measures import DiscreteMeasure, pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.hankel import log_hankel, hankel_det_mp, heine_sum_mp, difference_ratio


def _mu():
    rng = np.random.default_rng(3)
    return DiscreteMeasure.from_atoms(rng.uniform(0.05, 1.0, 9), rng.uniform(0.2, 1.5, 9))


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_heine_equals_hankel_det(n):
    mu = _mu()
    d1, d2 = hankel_det_mp(mu, n, dps=60), heine_sum_mp(mu, n, dps=60)
    assert abs(d1 / d2 - 1) < mp.mpf(10) ** -40


@pytest.mark.parametrize("n", [1, 2, 3, 4, 5])
def test_h2_identity(n):
    mu = _mu()
    jc = jacobi_coeffs(mu, 7, method="mp", dps=60)
    assert log_hankel(jc, n) == pytest.approx(float(mp.log(hankel_det_mp(mu, n, dps=60))), abs=1e-10)


def test_log_hankel_bounds():
    jc = jacobi_coeffs(pure_power(2, 100), 10)
    with pytest.raises(ValueError):
        log_hankel(jc, 12)


def test_difference_ratio_lemma_H5_pure_power_log():
    # f = xi^-2 L, L = log(e + xi) nondecreasing: ratio vs g = xi^-2 lies in [(1-eps*(a)/2) L(a), L(a)]
    L = lambda t: np.log(np.e + t)
    f = lambda t: t ** -2.0 * L(t)
    g = lambda t: t ** -2.0
    for a, b in [(1.0, 2.0), (3.0, 1e4), (100.0, 101.0)]:
        r = difference_ratio(f, g, a, b)
        assert r <= L(a) * (1 + 1e-12)
        assert r >= (1 - 0.5 / np.log(np.e + a)) * L(a) * (1 - 1e-12)   # eps(t) = t/((e+t) L(t)) <= 1/L(t)
