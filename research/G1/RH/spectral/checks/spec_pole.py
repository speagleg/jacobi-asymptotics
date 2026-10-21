"""SPEC probe: the pole law. Index-corrected lattices lam_k = (k + g k^{-m})^p (weights lam^{-s/p}); Z(0) unchanged.
Mellin-Barnes reading of the zeta layer, (p/n) sum_j W(j) Z(-j) n^{-jp} with W(q) := C(2q,q) c^q = (4c)^q Gamma(q+1/2)/(sqrt(pi) Gamma(q+1)),
written as -(1/2 pi i) int W(w) Z(-w) pi cot(pi w) n^{-wp} dw: a pole of Z(-w) at w = q with residue R contributes
  (p/n) * (-R) W(q) pi cot(pi q) n^{-pq}  (sign calibrated by the m = 1 data at p = 0.6, 1.5).
Here Z(s) = sum (k + g k^{-m})^{-ps} = zeta(ps) - p s g zeta(ps + m + 1) + O(g^2): pole at w = q := m/p with R = -m g/p, so
  prediction: n (y - y_lat) contains  -m g W(m/p) pi cot(pi m/p) n^{-m}   (m = 1: a shift of d2 by -g pi cot(pi/p)).
Method: subtract the exact first-order zeta-layer change sum_j W(j) p DeltaZ(-j) n^{-jp} (regularised), then least-squares fit."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import run, NMAX, c_p_mp
from so_coeffs import coeffs
from so_fit import sequences
p, s, g, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
K = (200 if p < 1 else 100)*NMAX; k = np.arange(1, K + 1, dtype=np.float64)
n, y = run(f"pole_p{p}_s{s}_g{g}_m{m}", (k + g*k**(-m))**p, p, s, 0.0, K)
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
mp.mp.dps = 30; c = c_p_mp(p); pm = mp.mpf(p); mm = mp.mpf(m); gg = mp.mpf(g)
W = lambda q: (4*c)**q*mp.gamma(q + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(q + 1))
def dZ(j, terms=10, kex=3000):
    # regularised sum_k [(k + g k^-m)^{jp} - k^{jp}] = sum_{i>=1} binom(jp, i) g^i zeta((m+1) i - jp) + convergent remainder
    q = j*pm
    reg = sum(mp.binomial(q, i)*gg**i*mp.zeta((mm + 1)*i - q) for i in range(1, terms))
    rem = sum((mp.mpf(kk) + gg*mp.mpf(kk)**(-mm))**q - sum(mp.binomial(q, i)*gg**i*mp.mpf(kk)**(q - (mm + 1)*i) for i in range(terms)) for kk in range(1, kex + 1))
    return reg + rem
D = n*(y - y0)
jmax = int(np.ceil(2.5/p)) - 1        # j p < 2.5 (the fit range); avoids poles of Z(-w) colliding with integers beyond it (e.g. p = 3/4: w = 3/p = 4)
for j in range(1, jmax + 1):
    D = D - float(p*W(j)*dZ(j))*n**(-j*p)
pred = float(-mm*gg*W(mm/pm)*mp.pi*mp.cot(mp.pi*mm/pm))
print(f"p={p} s={s} g={g} m={m}: predicted coefficient of n^-{m} in n(y - y_lat) - zeta layer: {pred:+.6f}"
      f"   (W(m/p) = {float(W(mm/pm)):.6f}, cot(pi m/p) = {float(mp.cot(mp.pi*mm/pm)):+.6f})")
E0 = sorted({round(e, 9) for e in [m, 1.0, 2.0, 2*m, m + 1, m + p, 1 + p, 2*p, 3*p, 2 + p, 3.0] if e > 0})
for lo in (200, 400, 800):
    sel = n >= lo
    for J in (5, 6, 7):
        E = E0[:J] if m in E0[:J] else E0[:J - 1] + [m]
        A = np.vstack([n[sel]**-e for e in E]).T; co = np.linalg.lstsq(A, D[sel], rcond=None)[0]
        if J == 6:
            print(f"  n >= {lo}, exponents {E}: coefficient of n^-{m} = {co[E.index(m)]:+.6f}   (pred {pred:+.6f})")
