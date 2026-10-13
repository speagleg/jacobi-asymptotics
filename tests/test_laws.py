import numpy as np
import pytest
from jacobi_asym.laws import I_p, c_p, K_weyl, predict_b, averaged_law, weyl_count


def test_constants():
    assert c_p(1) == pytest.approx(0.5, rel=1e-14)
    assert c_p(2) == pytest.approx(np.pi ** 2 / 16, rel=1e-14)
    assert I_p(2) == pytest.approx(1.0, rel=1e-14)          # int_0^{pi/2} cos
    assert I_p(1) == pytest.approx(np.pi / 4, rel=1e-14)    # int_0^{pi/2} cos^2
    for p in (1, 1.5, 2, 3):
        assert K_weyl(2 * c_p(p), c_p(p), p) == pytest.approx(1.0, abs=1e-8)
    assert K_weyl(2.0, 1.0, 2) == pytest.approx(4 / np.pi, abs=1e-8)


def test_weyl_count_toeplitz():
    # N x N Toeplitz a=1, b=0.25: eigenvalues 1 + 0.5 cos(pi i/(N+1)); count above 1 is N/2 within 1
    a = np.ones(100); b = 0.25 * np.ones(100)
    assert abs(weyl_count(1.0, a, b) - 50) <= 1


@pytest.mark.parametrize("p", [1, 2, 3])
def test_predict_b_pure_powers(p):
    f = lambda xi: np.asarray(xi, float) ** (-p)
    finv = lambda B: B ** (-1.0 / p)
    r = predict_b(1000, f, finv) / f(1000) / c_p(p)
    assert abs(r - 1) < 2e-3          # observed 1 - p/(2n) + ... (0.999001 for p = 2)
    assert predict_b(100, f, finv) > predict_b(1000, f, finv)


def test_predict_b_small_n_rejected():
    with pytest.raises(ValueError, match="n >= 2"):
        predict_b(1, lambda xi: xi ** -2.0, lambda B: B ** -0.5)


def test_averaged_law_on_exact_ratio():
    # b_j/x_j == c(p) exactly: (2/n^2) sum_{j<n}(n-j) = (n-1)/n, so S_n = -log c(p) / n (item-11 convention)
    j = np.arange(1, 501, dtype=float)
    x = j ** -2.0
    b = c_p(2) * x
    S = averaged_law(b, x, 2, [10, 100, 500])
    for n, v in S.items():
        assert v == pytest.approx(-np.log(c_p(2)) / n, abs=1e-13)
    with pytest.raises(ValueError):
        averaged_law(b, x, 2, [600])
