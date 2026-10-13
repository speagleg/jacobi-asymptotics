import numpy as np
import mpmath as mp
import pytest
from jacobi_asym.measures import DiscreteMeasure, pure_power
from jacobi_asym.jacobi import jacobi_mp, jacobi_rkpw, JacobiCoeffs


def test_two_atom_closed_form_mp():
    # mu = w1 d_{x1} + w2 d_{x2}: a_1 = (w1x1+w2x2)/(w1+w2), b_1^2 = w1 w2 (x1-x2)^2/(w1+w2)^2
    mu = DiscreteMeasure.from_atoms([0.75, 0.25], [1.0, 3.0])
    a, b2 = jacobi_mp(mu, 1, dps=40)
    assert abs(a[0] - mp.mpf(0.375)) < mp.mpf(10) ** -35
    assert abs(b2[0] - mp.mpf(3) * mp.mpf(0.25) / 16) < mp.mpf(10) ** -35


def test_rkpw_matches_mp_random_measure():
    rng = np.random.default_rng(7)
    x = np.sort(rng.uniform(0.01, 1.0, 60))[::-1]
    w = rng.uniform(0.1, 2.0, 60)
    mu = DiscreteMeasure.from_atoms(x, w)
    a_ref, b2_ref = jacobi_mp(mu, 30, dps=60)
    r = jacobi_rkpw(mu, 30)
    assert isinstance(r, JacobiCoeffs) and r.a.dtype == np.float64
    assert np.max(np.abs(r.a / np.array([float(v) for v in a_ref]) - 1)) < 1e-11
    assert np.max(np.abs(r.b2 / np.array([float(v) for v in b2_ref]) - 1)) < 1e-11
    assert r.mass == pytest.approx(mu.mass, rel=1e-14)


def test_rkpw_long_double_and_quad_keep_precision_type():
    mu = pure_power(2, 2000)
    rd, rl, rq = (jacobi_rkpw(mu, 100, prec=p) for p in ("d", "ld", "q"))
    assert rl.a.dtype == np.longdouble and rq.b2.dtype == object
    # the extra bits must survive parsing (a float64 round-trip would make this exactly 0)
    assert np.max(np.abs(rl.b2 - rl.b2.astype(np.float64).astype(np.longdouble))) > 0
    assert np.max(np.abs(rd.b2 / rl.b2.astype(np.float64) - 1)) < 1e-11
    rq_ld = np.array([np.longdouble(mp.nstr(v, 25)) for v in rq.b2])
    assert np.max(np.abs(rl.b2 / rq_ld - 1)) < 1e-14


@pytest.mark.parametrize("engine", ["rkpw", "mp"])
def test_n_must_be_below_number_of_atoms(engine):
    mu = DiscreteMeasure.from_atoms([0.5, 0.3, 0.1], [1.0, 1.0, 1.0])
    with pytest.raises(ValueError, match="n < N"):
        jacobi_rkpw(mu, 3) if engine == "rkpw" else jacobi_mp(mu, 3)


def test_missing_kernel_message(monkeypatch, tmp_path):
    import jacobi_asym.jacobi.rkpw as R
    monkeypatch.setattr(R, "BIN_DIR", tmp_path)
    with pytest.raises(R.KernelMissing, match="make -C csrc"):
        jacobi_rkpw(pure_power(2, 10), 3)


def test_quad_precision_is_actually_delivered():
    # binary128 must deliver ~1e-30, not long-double accuracy (final review, Important #1)
    rng = np.random.default_rng(5)
    mu = DiscreteMeasure.from_atoms(rng.uniform(0.01, 1, 40), rng.uniform(0.1, 2, 40))
    a_ref, b2_ref = jacobi_mp(mu, 20, dps=60)
    rq = jacobi_rkpw(mu, 20, prec="q")
    assert max(abs(rq.b2[i] / b2_ref[i] - 1) for i in range(20)) < 1e-25
    assert max(abs(rq.a[i] / a_ref[i] - 1) for i in range(20)) < 1e-25
    with mp.workdps(40):
        assert abs(rq.b[3] - mp.sqrt(b2_ref[3])) / abs(rq.b[3]) < 1e-25
