from pathlib import Path
import numpy as np
import pytest
from jacobi_asym.measures import zero_measure, smooth_zeta, DiscreteMeasure
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import averaged_law

D = Path(__file__).parent / "data"


def test_A10_reproduction():
    g = np.array([float(l) for l in open(D / "zeta_zeros_4000_dps60.txt") if l.strip()])
    mu = zero_measure(g, tail=False)
    ref = np.load(D / "A10_b_zeta_4000atoms_n400.npz")["b_sq"]
    r = jacobi_coeffs(mu, 400)
    assert np.max(np.abs(r.b2 / ref - 1)) < 1e-12


@pytest.mark.slow
def test_smooth_zeta_averaged_law_item11():
    mu = smooth_zeta(2001052)
    r = jacobi_coeffs(mu, 1000)
    S = averaged_law(r.b, mu.atoms, 2, [100, 300, 1000])
    assert S[100] == pytest.approx(-0.12627466819980426, abs=1e-9)
    assert S[300] == pytest.approx(-0.09699890257227572, abs=1e-9)
    assert S[1000] == pytest.approx(-0.07455905815171271, abs=1e-9)


@pytest.mark.slow
def test_HL_adversarial_log_cubed():
    k = np.arange(1, 2_000_001, dtype=float)
    x = k ** -2.0 * np.log(np.e + k) ** 3
    mu = DiscreteMeasure(x, x.copy())
    r = jacobi_coeffs(mu, 1000)
    S = averaged_law(r.b, x, 2, [300, 1000])
    assert S[300] == pytest.approx(-0.11818, abs=6e-6)
    assert S[1000] == pytest.approx(-0.09009, abs=6e-6)
