import mpmath as mp
import numpy as np
from jacobi_asym.measures import pure_power
from jacobi_asym.jacobi import jacobi_coeffs
from jacobi_asym.laws import averaged_law, c_p


def test_lean_blaw_quantity_matches_toolkit_averaged_law():
    mu = pure_power(2, 3000)
    r = jacobi_coeffs(mu, 40)
    n = 40
    lean_q = 2 / n ** 2 * sum((n - j) * np.log(np.sqrt(r.b2[j - 1]) / mu.atoms[j - 1]) for j in range(1, n))
    assert abs(lean_q - (averaged_law(r.b, mu.atoms, 2, [n])[n] + np.log(c_p(2)))) < 1e-12
