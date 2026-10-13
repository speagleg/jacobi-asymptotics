from fractions import Fraction as F
import math
import mpmath as mp
import pytest
from jacobi_asym.measures import lommel_coeffs, tc_coeffs, lommel_measure
from jacobi_asym.jacobi import jacobi_coeffs


def _poch(a, n):
    r = F(1)
    for i in range(n):
        r *= a + i
    return r


def _lommel_moments(nu, R):
    # moments of sigma~ (atoms j^{-2}): m_r = [t^r] A(t)/B(t), A = 0F1(;nu+2;-t/4)-type series, B = 0F1(;nu+1;-t/4)
    A = [F((-1) ** i, 4 ** i * math.factorial(i)) / _poch(nu + 2, i) for i in range(R)]
    B = [F((-1) ** i, 4 ** i * math.factorial(i)) / _poch(nu + 1, i) for i in range(R)]
    q = []
    for r in range(R):
        q.append((A[r] - sum(q[i] * B[r - i] for i in range(r))) / B[0])
    return q


def _stieltjes_exact(m, n):
    def ip(p, q):
        return sum(p[i] * q[j] * m[i + j] for i in range(len(p)) for j in range(len(q)))
    Pm, Pc, nm = None, [F(1)], None
    nc = ip(Pc, Pc)
    a, b2 = [], []
    for _ in range(n):
        al = ip([F(0)] + Pc, Pc) / nc
        Pn = [F(0)] + Pc
        Pn = [Pn[i] - al * (Pc[i] if i < len(Pc) else 0) for i in range(len(Pn))]
        if Pm is not None:
            Pn = [Pn[i] - (nc / nm) * (Pm[i] if i < len(Pm) else 0) for i in range(len(Pn))]
        nn = ip(Pn, Pn)
        a.append(al)
        b2.append(nn / nc)
        Pm, Pc, nm, nc = Pc, Pn, nc, nn
    return a, b2


@pytest.mark.parametrize("nu", [F(1, 2), F(0), F(1), F(-1, 2), F(7, 3)])
def test_lommel_closed_form_equals_exact_moments(nu):
    n = 7
    mom = _lommel_moments(nu, 2 * n + 3)
    a, b2 = _stieltjes_exact(mom, n)
    ae, be = lommel_coeffs(nu, n, "even")
    assert a == ae and b2[: n - 1] == be[: n - 1]
    a, b2 = _stieltjes_exact(mom[1:], n - 1)
    ao, bo = lommel_coeffs(nu, n - 1, "odd")
    assert a == ao and b2[: n - 2] == bo[: n - 2]


def test_tc_alpha1_values():
    a, b2 = tc_coeffs(1, 4)
    assert b2 == [F(1, 2 * j * (2 * j + 1)) for j in range(1, 5)]
    assert a == [F(1, 2), F(1, 3) + F(1, 4), F(1, 5) + F(1, 6), F(1, 7) + F(1, 8)]
    _, bo = tc_coeffs(1, 3, "odd")
    assert bo == [F(1, (2 * j + 1) * (2 * j + 2)) for j in range(1, 4)]


@pytest.mark.parametrize("alpha", [mp.mpf("0.5"), 1, 3])
def test_tc_even_continued_fraction_folding(alpha):
    # symmetric zero-diagonal J-fraction with off-diagonal^2 lambda_m equals x F(x^2) with the folded coefficients
    with mp.workdps(40):
        al = mp.mpf(alpha)
        lam = lambda m: mp.mpf(0) if m == 0 else m / ((m + al) * (m + al - 1))
        Nt = 3000
        a, b2 = tc_coeffs(al, Nt)
        for x in (mp.mpc("0.3", "0.4"), mp.mpc(2, 1)):
            g = mp.mpf(0)
            for m in range(2 * Nt, 0, -1):
                g = lam(m) / (x - g)
            G = 1 / (x - g)
            f = mp.mpf(0)
            for j in range(Nt, 0, -1):
                f = 1 / (x * x - a[j - 1] - (b2[j - 1] if j < Nt else 0) * f)
            assert abs(G - x * f) / abs(G) < mp.mpf(10) ** -30


def test_odd_variants_by_christoffel_step():
    with mp.workdps(50):
        for coeffs, par in ((tc_coeffs, mp.mpf(1)), (lommel_coeffs, mp.mpf("0.5"))):
            n = 12
            a, b2 = coeffs(par, n, "even")
            J = mp.matrix(n, n)
            for j in range(n):
                J[j, j] = a[j]
                if j < n - 1:
                    J[j, j + 1] = J[j + 1, j] = mp.sqrt(b2[j])
            L = mp.cholesky(J)
            Jp = L.T * L
            ao, bo = coeffs(par, n, "odd")
            assert max(abs(Jp[j, j] - ao[j]) for j in range(n - 1)) < mp.mpf(10) ** -40
            assert max(abs(Jp[j, j + 1] ** 2 - bo[j]) for j in range(n - 2)) < mp.mpf(10) ** -40


def test_lommel_measure_converges_to_closed_form():
    # truncating to K atoms drops ~1/K of the mass: measured rel. deviation of b_1..b_5^2 is ~4e-3 at K = 200
    _, b2 = lommel_coeffs(mp.mpf("0.5"), 5)
    dev = {}
    for K in (200, 400):
        r = jacobi_coeffs(lommel_measure(0.5, K), 5, method="mp", dps=40)
        dev[K] = max(abs(r.b2[j] / float(b2[j]) - 1) for j in range(5))
    assert dev[200] < 1e-2
    assert dev[400] < 0.6 * dev[200]
