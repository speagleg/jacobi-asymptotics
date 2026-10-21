"""SPEC §3.17: homogeneous potentials p^2 + q^N (N even). Exact eigenvalues (HO basis, banded; two sizes), WKB fit
  K - 1/2 = A E^a + B E^-a + C E^-3a,  a = (N+2)/(2N) = 1/p.
The normalised nodes are a Hurwitz lattice (delta = -1/2) plus gamma/k', gamma = -A B (m = 1, pole q = 1/p, W(1/p) = 1), so the pole law
adds -gamma pi cot(pi/p) = A B pi cot(pi/p) to d2. Observed: this equals (N-1)/(6(N+2)) exactly (N = 4..12), i.e. the kernel cancels the
transcendental WKB constant (cot(pi/p) = -tan(pi/N)). N = 4 is tested against b_n directly in spec_quartic.py."""
# p^2 + q^N (N even): fit K - 1/2 = A E^{a} + B E^{-a} + C E^{-3a}, a = (N+2)/(2N); pole-law d2 term = -gamma pi cot(pi/p), gamma = -A B,
# p = 1/a = 2N/(N+2) (index correction m = 1, q = 1/p, W = 1).
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, scipy.sparse as sp, mpmath as mp
from spec_common import Checks
C_ = Checks()
from scipy.linalg import eig_banded
def eigs(N, Nb, nkeep, om):
    n = np.arange(Nb + N, dtype=np.float64)
    Q2 = sp.diags([(2*n + 1)/(2*om), np.sqrt((n[:-2] + 1)*(n[:-2] + 2))/(2*om), np.sqrt((n[:-2] + 1)*(n[:-2] + 2))/(2*om)], [0, 2, -2], format='csr')
    QN = Q2
    for _ in range(N//2 - 1): QN = (QN @ Q2).tocsr()
    QN = QN[:Nb, :Nb]
    m_ = np.arange(Nb, dtype=np.float64); o = -om*np.sqrt((m_[:-2] + 1)*(m_[:-2] + 2))/2
    H = (QN + sp.diags([om*(2*m_ + 1)/2, o, o], [0, 2, -2])).todia(); bw = N
    ab = np.zeros((bw + 1, Nb))
    for d in range(bw + 1): ab[bw - d, d:] = H.diagonal(d)
    return eig_banded(ab, lower=False, eigvals_only=True, select='i', select_range=(0, nkeep - 1))
mp.mp.dps = 30
for N in (4, 6, 8, 10, 12):
    a = (N + 2)/(2*N); p = 1/a
    A = float(mp.quad(lambda t: mp.sqrt(1 - t**N), [-1, 1])/mp.pi)
    keep = 900; Emax = (keep/A)**(1/a); om = Emax**(0.5 - 1/N)
    e1 = eigs(N, 7000, keep, om); e2 = eigs(N, 9000, keep, om)
    K = np.arange(1, keep + 1); r = K - 0.5 - A*e2**a; sel = (K > 150) & (K <= 700)
    M = np.vstack([e2[sel]**-a, e2[sel]**(-3*a)]).T; B, C = np.linalg.lstsq(M, r[sel], rcond=None)[0]
    gam = -A*B; term = -gam*np.pi*float(mp.cot(mp.pi/p))
    guess = (N - 1)/(6*(N + 2)); print(f"N={N}: p={p:.4f} conv {np.max(np.abs(e1 - e2)/e2):.1e} guess (N-1)/(6(N+2)) = {guess:.10f}  A={A:.10f} B={B:+.10f}  A*B*pi={A*B*np.pi:+.10f}  pole d2 term {term:+.10f}")
    C_.check(f"N={N} pole term = (N-1)/(6(N+2))", term, guess, 1e-6)
C_.finish()
