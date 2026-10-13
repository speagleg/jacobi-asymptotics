import numpy as np
import pytest
from jacobi_asym.measures import pure_power, DiscreteMeasure
from jacobi_asym.jacobi import jacobi_coeffs, jacobi_lanczos


def test_lanczos_vs_rkpw_on_20k_atoms():
    mu = pure_power(2, 20000)
    r = jacobi_coeffs(mu, 300, method="rkpw")
    l = jacobi_lanczos(mu, 300)
    assert np.max(np.abs(np.sqrt(l.b2 / r.b2) - 1)) < 1e-12
    assert np.max(np.abs(l.a / r.a - 1)) < 1e-12


def test_dispatch_mp_returns_float_arrays():
    mu = pure_power(1, 40, s=2)
    m = jacobi_coeffs(mu, 10, method="mp", dps=40)
    r = jacobi_coeffs(mu, 10)
    assert m.prec == "dps40" and m.a.dtype == np.float64
    assert np.max(np.abs(m.b2 / r.b2 - 1)) < 1e-12


def test_dispatch_rejects_unknown_method():
    with pytest.raises(ValueError, match="method"):
        jacobi_coeffs(pure_power(2, 10), 3, method="qr")


def test_lanczos_n_limit():
    with pytest.raises(ValueError, match="n < N"):
        jacobi_lanczos(DiscreteMeasure.from_atoms([0.5, 0.1], [1.0, 1.0]), 2)
