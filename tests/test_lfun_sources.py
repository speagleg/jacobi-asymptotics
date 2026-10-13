import hashlib
import numpy as np
import pytest
from jacobi_asym.measures import (Nsmooth, Ninv, model_zeros, smooth_zeta, zero_measure, load_odlyzko,
                                  DataMissing, synthetic_unfolded, synthetic_zeta)


def test_Ninv_inverts_Nsmooth():
    for q in (1, 3, 4):
        T = np.array([20.0, 100.0, 1e4, 1e8])
        assert np.allclose(Ninv(Nsmooth(T, q), q), T, rtol=1e-12)


def test_model_zeros_gram_convention():
    g = model_zeros(1000)
    assert np.all(np.diff(g) > 0)
    assert np.allclose(Nsmooth(g), np.arange(1, 1001) - 0.5, atol=1e-8)


def test_smooth_zeta_measure_structure():
    mu = smooth_zeta(5000)
    assert mu.N > 5000                      # tail nodes appended
    g = model_zeros(5000)
    assert np.allclose(mu.atoms[:5000], 1 / (g ** 2 + 0.25))
    assert np.allclose(mu.weights[:5000], 2 * mu.atoms[:5000])


def test_zero_measure_mass_close_to_zeta_constant():
    # total mass of sum_rho 1/(rho(1-rho)) = 2 + gamma_E - log(4 pi) ~ 0.04619; smooth model is close (~1e-3)
    mu = smooth_zeta(100000)
    assert abs(mu.mass - (2 + np.euler_gamma - np.log(4 * np.pi))) < 5e-3


def test_load_odlyzko_missing_message(tmp_path):
    with pytest.raises(DataMissing, match="fetch.py odlyzko"):
        load_odlyzko(10, root=tmp_path)


def test_synthetic_deterministic_and_mean_spacing():
    u1, u2 = synthetic_unfolded("cue", 2000, seed=1), synthetic_unfolded("cue", 2000, seed=1)
    assert np.array_equal(u1, u2)
    assert abs(np.mean(np.diff(synthetic_unfolded("poisson", 20000, seed=2))) - 1) < 0.03
    mu = synthetic_zeta("jitter", 3000, seed=1)
    assert mu.N > 3000


def test_fetch_sha256_helper(tmp_path):
    import importlib.util, pathlib
    spec = importlib.util.spec_from_file_location("fetch", pathlib.Path(__file__).parents[1] / "data" / "fetch.py")
    fetch = importlib.util.module_from_spec(spec); spec.loader.exec_module(fetch)
    p = tmp_path / "x.bin"; p.write_bytes(b"abc")
    assert fetch.sha256(p) == hashlib.sha256(b"abc").hexdigest()


@pytest.mark.data
def test_true_zeta_if_data_present():
    try:
        g = load_odlyzko(100)
    except DataMissing:
        pytest.skip("Odlyzko data not fetched")
    assert abs(g[0] - 14.134725141734693) < 1e-8
