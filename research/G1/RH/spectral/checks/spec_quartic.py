"""SPEC §3.18 probe: the pole law on a real operator with cot != 0 -- the quartic oscillator H = -d^2/dq^2 + q^4 on R.
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
p, s = 4/3, 2.0; KEX = 1200; K = 100*NMAX
mp.mp.dps = 30
A = float(mp.quad(lambda t: mp.sqrt(1 - t**4), [-1, 1])/mp.pi)

def ho_eigs(Nb, nkeep, om):
    """lowest nkeep eigenvalues of p^2 + q^4 in the HO basis of frequency om (size Nb); sparse build, band storage (upper, 5 rows)."""
    import scipy.sparse as sp
    n = np.arange(Nb + 4, dtype=np.float64)
    Q2 = sp.diags([(2*n + 1)/(2*om), np.sqrt((n[:-2] + 1)*(n[:-2] + 2))/(2*om), np.sqrt((n[:-2] + 1)*(n[:-2] + 2))/(2*om)], [0, 2, -2], format='csr')
    Q4 = (Q2 @ Q2).tocsr()[:Nb, :Nb]
    m_ = np.arange(Nb, dtype=np.float64); o = -om*np.sqrt((m_[:-2] + 1)*(m_[:-2] + 2))/2
    H = (Q4 + sp.diags([om*(2*m_ + 1)/2, o, o], [0, 2, -2])).todia()
    ab = np.zeros((5, Nb))
    for d in range(5): ab[4 - d, d:] = H.diagonal(d)
    return eig_banded(ab, lower=False, eigvals_only=True, select='i', select_range=(0, nkeep - 1))

if __name__ == "__main__":
    C_ = Checks()
    Emax = (KEX/A)**(4/3); om = Emax**0.25          # balances q_max^2 om = p_max^2/om
    E1 = ho_eigs(4000, KEX, om); E2 = ho_eigs(5000, KEX, om)
    conv = np.abs(E1 - E2)/E2
    print(f"A = {A:.15f}; HO basis om = {om:.2f}: relative change 4000 -> 5000 basis: max over K <= {KEX}: {conv.max():.1e}, at K <= 800: {conv[:800].max():.1e}")
    print(f"E_1..E_4 = {E2[:4]}  (known ground state 1.0603620905)")
    C_.check("ground state", E2[0], 1.0603620905, 1e-8)
    Ke = np.arange(1, KEX + 1, dtype=np.float64); r = Ke - 0.5 - A*E2**0.75
    sel = (Ke > 200) & (Ke <= 900)
    Am = np.vstack([E2[sel]**-0.75, E2[sel]**-2.25]).T; B, Cc = np.linalg.lstsq(Am, r[sel], rcond=None)[0]
    Bs = np.linalg.lstsq(Am[:, :1], r[sel], rcond=None)[0][0]
    print(f"WKB fit on 200 < K <= 900: B = {B:.10f}, C = {Cc:.6f} (one-term B = {Bs:.10f}); residual at K=1000: {r[999] - B*E2[999]**-0.75 - Cc*E2[999]**-2.25:+.1e}")
    gamma = -A*B                                   # lam^{3/4} = A E^{3/4}, E^{-3/4} = A/lam^{3/4} ~ A/k'  =>  gamma = -A B
    # nodes: exact for K <= 1000, series beyond (solve K - 1/2 = A E^{3/4} + B E^{-3/4} + C E^{-9/4} by Newton)
    KK = np.arange(1, K + 1, dtype=np.float64); E = ((KK - 0.5)/A)**(4/3)
    for _ in range(30):
        f = A*E**0.75 + B*E**-0.75 + Cc*E**-2.25 - (KK - 0.5); df = 0.75*A*E**-0.25 - 0.75*B*E**-1.75 - 2.25*Cc*E**-3.25; E = E - f/df
    E[:1000] = E2[:1000]
    lam = A**(4/3)*E
    n, y = run("quartic_p1.333", lam, p, s, -0.5, K)
    c = c_p_mp(p); pm = mp.mpf(p)
    # Z(-1) = sum lam - regularised: sum_K [lam_K - (K - 1/2)^p] + zeta(-p, 1/2), the bracket converging like K^{p-3} (gamma term regularised)
    kp = KK - 0.5; brk = lam - kp**p
    # asymptotic bracket ~ p gamma kp^{p-2} + ...: subtract and add back its Hurwitz-regularised sum
    Zm1 = float(mp.zeta(-pm, 0.5)) + np.sum(brk - p*gamma*kp**(p - 2)) + p*gamma*float(mp.zeta(2 - pm, 0.5))
    eps1 = float(2*pm*c)*Zm1
    d10 = -(s - 1)/2; delta = -0.5; d1 = d10 - p*delta
    d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
    d2shift = d2f(p, s) + p*(p + 1)*delta**2/2 - (p + 1)*delta*d10
    print(f"gamma = -A B = {gamma:+.8f} (pi gamma = {np.pi*gamma:.8f}; 1/12 = {1/12:.8f});  predicted d1 = {d1:+.8f};  eps1 = 2pcZ(-1) = {eps1:+.8f} (Z(-1) = {Zm1:+.8f})")
    print(f"d2 predictions: shift-only {d2shift:+.6f};  + pi gamma (pole law) {d2shift + np.pi*gamma:+.6f};  - pi gamma (sign flipped) {d2shift - np.pi*gamma:+.6f}")
    v1, h1 = fit(n, y, p, [], 1.0); print(f"d1 fit {v1:+.8f} ({h1:.1e})"); C_.check("d1", v1, d1, max(3*h1, 1e-6))
    v2, h2 = fit(n, y - d1/n - eps1*n**(-1 - p), p, [1.0, 1 + p], 2.0)
    print(f"d2 fit (after d1, eps1) {v2:+.6f} ({h2:.1e});  minus pole-law prediction {v2 - d2shift - np.pi*gamma:+.1e}")
    ve, he = fit(n, y - d1/n, p, [1.0], 1 + p); print(f"eps1 fit {ve:+.6f} ({he:.1e}) vs {eps1:+.6f}")
    C_.check("d2 pole law", v2, d2shift + np.pi*gamma, max(3*h2, 1e-4))
    C_.check("eps1 = 0 (Z(-1) = 0: no integer heat exponent for q^4)", ve, 0.0, max(3*he, 1e-4))
    C_.finish()
