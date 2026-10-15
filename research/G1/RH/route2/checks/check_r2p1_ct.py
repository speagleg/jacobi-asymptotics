"""Plan 50 (NUMERICAL): Lemma CT (Christoffel transfer, ROUTE2_p1.md §5) and Lemma D (parabolic dynamics).
Index convention (0-based, as jacobi_coeffs): a[n] = J_{nn}, b2[n] = J_{n,n+1}^2.
Cholesky J = L L^T: l_0^2 = a_0, m_n^2 = b2[n]/l_n^2, l_{n+1}^2 = a_{n+1} - m_n^2.  CT(i): J(x mu) = L^T L, i.e.
a'[n] = l_n^2 + m_n^2, b2'[n] = l_{n+1}^2 m_n^2.
[1] exactness of CT(i): mu = sigma_{s,Psi} (p = 1, s = 1.5) and (p = 2, s = 4), Psi = exp sqrt(log(k+e)), atoms + tail
    (as check_r2p1_coeff.py, K = 1e5); max relative difference between the directly computed J(x mu) and L^T L.
[2] Lemma D(a) numerically: x_n := n^p l_n^2 / c(p) -> 1 (slowly), for the same measures; and the law for x mu read off
    from L^T L: n(n^p b'_n/c - 1).
[3] Lemma D(b) (reverse recursion u_{n+1} = b2'[n]/(a'[n] - u_n) from the exact u_0 = a_0(mu)): z_n := n^p u_n/c -> 1, and
    agreement with the Cholesky l_n^2 of mu.
[4] Corollary B_{p>1}^+ example outside Theorem RII (GAP-alpha of Plan 48): p = 2, s = 6 (alpha_x = 3/2), w = k^{-6} Psi,
    computed directly: n(n^2 b_n/c - 1) bounded (law) and = CT image of s = 4 (inside RII).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan50/research/G1/RH/route2/checks/check_r2p1_ct.py"""
import importlib.util
from pathlib import Path
import numpy as np
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

spec = importlib.util.spec_from_file_location("cc", Path(__file__).with_name("check_r2p1_coeff.py"))
cc = importlib.util.module_from_spec(spec); spec.loader.exec_module(cc)
L = cc.L
NMAX = 802


def measure_p(p, s, K, shift=0.0):
    """sigma = sum k^{-s} Psi(k) delta_{k^{-p}} (+ tail); shift adds x^shift = k^{-p*shift} to the weight."""
    k = np.arange(1, K + 1, dtype=float)
    e = np.arange(np.log(K + 0.5), np.log(1e16), np.log(1.02))
    gx, gw = np.polynomial.legendre.leggauss(8)
    U = np.concatenate([(a + b) / 2 + (b - a) / 2 * gx for a, b in zip(e[:-1], e[1:])])
    W = np.concatenate([(b - a) / 2 * gw for a, b in zip(e[:-1], e[1:])])
    T = np.exp(U)
    lw = lambda t: -(s + p * shift) * np.log(t) + L(np.log(t))  # noqa: E731
    la, lt = lw(k), lw(T) + np.log(W * T); m = max(la.max(), lt.max())
    from jacobi_asym.measures.base import DiscreteMeasure
    return DiscreteMeasure.from_atoms(k ** -p, np.exp(la - m), tail=(T ** -p, np.exp(lt - m)))


def jc(mu, N=NMAX):
    r = jacobi_coeffs(mu, N, prec="ld")
    return np.asarray(r.a, np.longdouble), np.asarray(r.b2, np.longdouble)


def cholesky(a, b2, N):
    l2 = [a[0]]; m2 = []
    for n in range(N):
        m2.append(b2[n] / l2[n]); l2.append(a[n + 1] - m2[n])
    return np.array(l2), np.array(m2)


if __name__ == "__main__":
    NS = (50, 100, 200, 400, 800)
    for p, s in ((1.0, 1.5), (2.0, 4.0)):
        c = c_p(p); N = NMAX - 2
        a, b2 = jc(measure_p(p, s, 100_000))
        a1, b21 = jc(measure_p(p, s, 100_000, shift=1.0))
        l2, m2 = cholesky(a, b2, N)
        ap, bp2 = l2[:N] + m2[:N], l2[1:N + 1] * m2[:N]
        err = max(np.max(np.abs(ap / a1[:N] - 1)), np.max(np.abs(bp2 / b21[:N] - 1)))
        print(f"p={p}, s={s} -> s+p={s+p}:\n  [1] max rel |J(x mu) - L^T L| = {float(err):.1e}")
        xs = "  ".join(f"n={n}: {float(n ** p * l2[n] / c):.4f}" for n in NS)
        print(f"  [2] x_n = n^p l_n^2/c: {xs}")
        lw = "  ".join(f"n={n}: {float(n * (n ** p * np.sqrt(bp2[n - 1]) / c - 1)):+.4f}" for n in NS)
        print(f"      law for x mu from L^T L, n(n^p b'_n/c - 1): {lw}")
        u = [a[0]]
        for n in range(N):
            u.append(b21[n] / (a1[n] - u[n]))
        u = np.array(u)
        zs = "  ".join(f"n={n}: {float(n ** p * u[n] / c):.4f}" for n in NS)
        dev = float(np.max(np.abs(u[:N] / l2[:N] - 1)))
        print(f"  [3] reverse recursion z_n = n^p u_n/c: {zs};  max |u_n/l_n^2 - 1| = {dev:.1e}")
    p, s = 2.0, 6.0; c = c_p(p)
    a6, b26 = jc(measure_p(p, s, 100_000))
    vals = "  ".join(f"n={n}: {float(n * (n ** p * np.sqrt(b26[n - 1]) / c - 1)):+.4f}" for n in NS)
    print(f"[4] p=2, s=6 (alpha_x = 1.5, outside RII; law by CT from s = 4): n(n^2 b_n/c - 1): {vals}")
