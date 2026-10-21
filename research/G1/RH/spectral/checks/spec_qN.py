"""SPEC §3.17: the pole law on H = -d^2/dq^2 + q^N (N even; argv[1], default 4). For N = 4 see the quartic notes below; for general N:
  a = (N+2)/(2N) = 1/p, K - 1/2 = A E^a + B E^-a + C E^-3a, gamma = -A B, pole term in d2 = (N-1)/(6(N+2)) (derived from second-order WKB),
  eps1 = 0 when 1 is not a heat-trace exponent (exponents -a + 2a j).
Original N = 4 description:
Eigenvalues E_0 < E_1 < ...: exact (harmonic-oscillator basis, banded matrix, two basis sizes for convergence) for K <= KEX, and the
Bohr-Sommerfeld/WKB series beyond:  K - 1/2 = A E^{3/4} + B E^{-3/4} + C E^{-9/4} + ...  (K = 1, 2, ...; A = (1/pi) int_{-1}^1 sqrt(1-t^4) dt
exact; B, C fitted to the exact eigenvalues and cross-checked).
Normalised nodes lam_K := A^{4/3} E_K, so lam^{3/4} = (K - 1/2) - B A E^{-3/4} - ... = k' + gamma/k' + O(k'^-3), k' := K - 1/2, gamma := -A B
(E^{-3/4} = A/lam^{3/4} ~ A/k'). p = 4/3, s = 2; weights lam^{-s/p}.
Predictions (S1', pole law; no fitted constant):
  d1 = -(s-1)/2 - p delta,  delta = -1/2 (Hurwitz offset)  =>  d1 = +1/6;  Z(0) = zeta(0, 1/2) = 0 (Voros: Z(0) = 0 for the quartic);
  n^{-1-p} = n^{-7/3}:  eps1 = 2 p c Z(-1)  (Z(-1) regularised from the actual nodes);
  n^{-2}:  d2 = d2_0 + p(p+1) delta^2/2 - (p+1) delta d1_0  +  pi gamma        [pole q = m/p = 3/4: W(3/4) = W(1/p) = 1, cot(3 pi/4) = -1,
           term -m gamma W(q) pi cot(pi q) = +pi gamma];  alternatives: -pi gamma (sign) or 0 (no kernel)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from scipy.linalg import eig_banded
from spec_common import run, NMAX, c_p_mp, fit, Checks
NPOW = int(sys.argv[1]) if len(sys.argv) > 1 else 4
AEX = (NPOW + 2)/(2*NPOW); p, s = 1/AEX, 2.0; KEX = 1200 if NPOW == 4 else 900; K = 100*NMAX
mp.mp.dps = 30
A = float(mp.quad(lambda t: mp.sqrt(1 - t**NPOW), [-1, 1])/mp.pi)

def ho_eigs(Nb, nkeep, om):
    """lowest nkeep eigenvalues of p^2 + q^NPOW in the HO basis of frequency om (size Nb); sparse build, band storage."""
    import scipy.sparse as sp
    n = np.arange(Nb + NPOW, dtype=np.float64)
    off = np.sqrt((n[:-2] + 1)*(n[:-2] + 2))/(2*om)
    Q2 = sp.diags([(2*n + 1)/(2*om), off, off], [0, 2, -2], format='csr'); QN = Q2
    for _ in range(NPOW//2 - 1): QN = (QN @ Q2).tocsr()
    QN = QN[:Nb, :Nb]
    m_ = np.arange(Nb, dtype=np.float64); o = -om*np.sqrt((m_[:-2] + 1)*(m_[:-2] + 2))/2
    H = (QN + sp.diags([om*(2*m_ + 1)/2, o, o], [0, 2, -2])).todia(); bw = NPOW
    ab = np.zeros((bw + 1, Nb))
    for d in range(bw + 1): ab[bw - d, d:] = H.diagonal(d)
    return eig_banded(ab, lower=False, eigvals_only=True, select='i', select_range=(0, nkeep - 1))

if __name__ == "__main__":
    C_ = Checks()
    Emax = (KEX/A)**(1/AEX); om = Emax**(0.5 - 1/NPOW)     # balances q_max^2 om = p_max^2/om
    E1 = ho_eigs(4000 if NPOW == 4 else 7000, KEX, om); E2 = ho_eigs(5000 if NPOW == 4 else 9000, KEX, om)
    conv = np.abs(E1 - E2)/E2
    print(f"A = {A:.15f}; HO basis om = {om:.2f}: relative change 4000 -> 5000 basis: max over K <= {KEX}: {conv.max():.1e}, at K <= 800: {conv[:800].max():.1e}")
    print(f"E_1..E_4 = {E2[:4]}")
    if NPOW == 4: C_.check("ground state", E2[0], 1.0603620905, 1e-8)
    Ke = np.arange(1, KEX + 1, dtype=np.float64); r = Ke - 0.5 - A*E2**AEX
    sel = (Ke > 150) & (Ke <= 700)
    Am = np.vstack([E2[sel]**-AEX, E2[sel]**(-3*AEX)]).T; B, Cc = np.linalg.lstsq(Am, r[sel], rcond=None)[0]
    Bs = np.linalg.lstsq(Am[:, :1], r[sel], rcond=None)[0][0]
    print(f"WKB fit on 200 < K <= 900: B = {B:.10f}, C = {Cc:.6f} (one-term B = {Bs:.10f}); residual at K=800: {r[799] - B*E2[799]**-AEX - Cc*E2[799]**(-3*AEX):+.1e}")
    gamma = -A*B; poleterm = -gamma*np.pi/np.tan(np.pi/p)  # = (N-1)/(6(N+2))
    _g = 0                                  # lam^{3/4} = A E^{3/4}, E^{-3/4} = A/lam^{3/4} ~ A/k'  =>  gamma = -A B
    # nodes: exact for K <= 1000, series beyond (solve K - 1/2 = A E^{3/4} + B E^{-3/4} + C E^{-9/4} by Newton)
    KK = np.arange(1, K + 1, dtype=np.float64); E = ((KK - 0.5)/A)**(1/AEX); a_ = AEX
    for _ in range(30):
        f = A*E**a_ + B*E**-a_ + Cc*E**(-3*a_) - (KK - 0.5); df = a_*A*E**(a_ - 1) - a_*B*E**(-a_ - 1) - 3*a_*Cc*E**(-3*a_ - 1); E = E - f/df
    nex = 1000 if NPOW == 4 else 800; E[:nex] = E2[:nex]
    lam = A**(1/AEX)*E
    n, y = run("quartic_p1.333" if NPOW == 4 else f"homog_N{NPOW}", lam, p, s, -0.5, K)
    c = c_p_mp(p); pm = mp.mpf(p)
    # Z(-1) = sum lam - regularised: sum_K [lam_K - (K - 1/2)^p] + zeta(-p, 1/2), the bracket converging like K^{p-3} (gamma term regularised)
    kp = KK - 0.5; brk = lam - kp**p
    # asymptotic bracket ~ p gamma kp^{p-2} + ...: subtract and add back its Hurwitz-regularised sum
    Zm1 = float(mp.zeta(-pm, 0.5)) + np.sum(brk - p*gamma*kp**(p - 2)) + p*gamma*float(mp.zeta(2 - pm, 0.5))
    eps1 = float(2*pm*c)*Zm1
    d10 = -(s - 1)/2; delta = -0.5; d1 = d10 - p*delta
    d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
    d2shift = d2f(p, s) + p*(p + 1)*delta**2/2 - (p + 1)*delta*d10
    print(f"gamma = -A B = {gamma:+.8f} (pole term -gamma pi cot(pi/p) = {poleterm:.8f});  predicted d1 = {d1:+.8f};  eps1 = 2pcZ(-1) = {eps1:+.8f} (Z(-1) = {Zm1:+.8f})")
    print(f"d2 predictions: shift-only {d2shift:+.6f};  + pi gamma (pole law) {d2shift + poleterm:+.6f};  sign flipped {d2shift - poleterm:+.6f};  (N-1)/(6(N+2)) = {(NPOW-1)/(6*(NPOW+2)):.8f}")
    v1, h1 = fit(n, y, p, [], 1.0); print(f"d1 fit {v1:+.8f} ({h1:.1e})"); C_.check("d1", v1, d1, max(3*h1, 1e-6))
    v2, h2 = fit(n, y - d1/n - eps1*n**(-1 - p), p, [1.0, 1 + p], 2.0)
    print(f"d2 fit (after d1, eps1) {v2:+.6f} ({h2:.1e});  minus pole-law prediction {v2 - d2shift - poleterm:+.1e}")
    ve, he = fit(n, y - d1/n, p, [1.0], 1 + p); print(f"eps1 fit {ve:+.6f} ({he:.1e}) vs {eps1:+.6f}")
    C_.check("d2 pole law", v2, d2shift + poleterm, max(3*h2, 1e-4))
    C_.check("eps1 = 0 (Z(-1) = 0: 1 is not a heat exponent)", ve, 0.0, max(3*he, 1e-4))
    C_.finish()
