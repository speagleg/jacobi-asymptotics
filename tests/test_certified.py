"""Certified suite (certified/): fast subsets here; the full scripts run under -m slow."""
import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

flint = pytest.importorskip("flint")
from flint import arb, ctx, fmpq  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ["c01_constants", "c02_lommel", "c03_zeta_hankel", "c04_monien_density"]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "certified" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(autouse=True)
def _restore_prec():
    old = ctx.prec
    yield
    ctx.prec = old


def test_constants_exact_values_and_kappa():
    from jacobi_asym.certify.constants import c_p, dlogc, dlogc_series, kappa_zeta
    ctx.prec = 256
    assert c_p(1).contains(arb(1) / 2)
    assert c_p(2).overlaps(arb.pi() ** 2 / 16) and c_p(2).rad() < arb(2) ** -200
    kz = kappa_zeta()
    assert kz.overlaps(-2 * dlogc(2)) and kz.overlaps(-2 * dlogc_series(2))
    assert dlogc("3/2").overlaps(dlogc_series("3/2"))


def test_rounding_helpers_are_strict():
    from jacobi_asym.certify.report import rounds_to, truncates_to
    from jacobi_asym.certify.constants import kappa_zeta
    ctx.prec = 256
    kz = kappa_zeta()
    assert rounds_to(kz, "-0.28946") and not rounds_to(kz, "-0.28945")
    assert truncates_to(kz, "-0.289459") and not truncates_to(kz, "-0.289460")


def test_c01_constants_script_passes():
    assert load("c01_constants").main() == 0


def test_lommel_small_N():
    assert load("c02_lommel").main(40) == 0


def test_chebyshev_rejects_low_precision_gracefully():
    from jacobi_asym.certify.moments import zeta_moments, chebyshev, adaptive, rel_bits_ok
    # at 53 bits the problem is too ill-conditioned: either an ArithmeticError or wide balls, never a wrong ball
    ctx.prec = 53
    try:
        A, B = chebyshev(zeta_moments(2, 2, 40), 20)
        pi2 = arb.pi() ** 2
        assert all(A[n].overlaps(2 * pi2 / ((4 * n + 1) * (4 * n + 5))) for n in range(1, 20))
    except ArithmeticError:
        pass
    (A, B), bits = adaptive(lambda: chebyshev(zeta_moments(2, 2, 40), 20), rel_bits_ok(64))
    assert bits >= 256 and all(b > 0 for b in B)


def test_baricz_stampach_small_n():
    m = load("c03_zeta_hankel")
    from jacobi_asym.certify.moments import adaptive, rel_bits_ok
    for l in (0, 1, 2):
        D, bits = adaptive(lambda: m.zeta_dets(fmpq(2), fmpq(2 * l - 2), 8), rel_bits_ok(80))
        ctx.prec = bits
        for n in range(1, 9):
            r, e = m.bs_closed_rational(n, l)
            assert D[n - 1].overlaps(arb(r) * arb.pi() ** e)
            assert D[n - 1].log().overlaps(m.log_bs_closed(n, l))


def test_c04_monien_density_script_passes():
    assert load("c04_monien_density").main() == 0


@pytest.mark.slow
@pytest.mark.parametrize("name", SCRIPTS)
def test_full_script_matches_stored_output(name):
    out = subprocess.run([sys.executable, "-I", str(ROOT / "certified" / f"{name}.py")], capture_output=True,
                         text=True, check=False)
    assert out.returncode == 0, out.stdout[-2000:] + out.stderr[-2000:]
    assert out.stdout.strip().endswith("RESULT: PASS")
    assert out.stdout == (ROOT / "certified" / f"{name}.out").read_text()
