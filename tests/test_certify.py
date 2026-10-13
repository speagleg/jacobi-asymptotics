import numpy as np
import mpmath as mp
import pytest
flint = pytest.importorskip("flint")
from flint import arb
from jacobi_asym.measures import DiscreteMeasure
from jacobi_asym.jacobi import jacobi_mp
from jacobi_asym.certify import certified_jacobi, certified_cp


def test_balls_contain_high_precision_reference():
    rng = np.random.default_rng(11)
    mu = DiscreteMeasure.from_atoms(rng.uniform(0.01, 1, 30), rng.uniform(0.1, 2, 30))
    A, B2 = certified_jacobi(mu, 12, prec_bits=300)
    a, b2 = jacobi_mp(mu, 12, dps=90)
    for ball, ref in zip(A + B2, a + b2):
        assert ball.overlaps(arb(mp.nstr(ref, 85)))
        assert float(ball.rad()) < 1e-40 * max(1.0, abs(float(ball.mid())))


def test_certified_cp():
    assert certified_cp(2).overlaps(arb.pi() ** 2 / 16)
    assert certified_cp(1).overlaps(arb(1) / 2)
    assert float(certified_cp(2).rad()) < 1e-60


def test_n_limit():
    mu = DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 1.0])
    with pytest.raises(ValueError, match="n < N"):
        certified_jacobi(mu, 2)
