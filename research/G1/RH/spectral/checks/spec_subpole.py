"""SPEC §3.15 probe: the subleading pole term (REVIEW_SPEC2_A F2). Lattices lam_k = (k + g/k^m)^p, weights lam^{-s/p}, m = 1.
First order in g is isolated by antisymmetrising (g, -g) and Richardson over g in {1/4, 1/2}:
  A(g) := [D(g) - D(-g)]/2 = g a1 + g^3 a3 + ...,  a1 = (8 A(1/4) - A(1/2))/1.5,   D(g) := n (y_g - y_lat).
From a1(n) the known first-order terms are subtracted:
  - leading pole term (§3.12): -m W(q) pi cot(pi q) n^{-m},  q = m/p  (per unit g);
  - first-order zeta layer: sum_j p W(j) dZ1(-j) n^{-jp},  dZ1(-j) = p j zeta(1 + m - p j)  (per unit g; skipped if 1 + m - pj = 1).
The remainder's coefficient of n^{-1-m} (i.e. n^{-2-m} in n^p b_n/c) is the subleading pole coefficient S (per unit g); it is printed
with candidate mechanisms of §3.14 (Prop. 3.14.4), with q1 = (m+1)/p:
  (a) Jacobian tilt through E3.7 (if E3.7 extends to branched tilts): m p q1 W(q1)/2;
  (b) the tan pole of the phase perturbation at w = q1:                 p q1 W(q1);
No assertion on the candidates (exploration); assertions only on the stability of the extraction.
Usage: spec_subpole.py p[:s] [p[:s] ...]   (s defaults to 2)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import Checks, run, NMAX, c_p_mp
from so_coeffs import coeffs
from so_fit import sequences
C_ = Checks(); m = 1.0
for arg in sys.argv[1:]:
    p, s = (float(v) for v in arg.split(':')) if ':' in arg else (float(arg), 2.0)
    K = (200 if p < 1 else 100)*NMAX; k = np.arange(1, K + 1, dtype=np.float64)
    al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
    D = {}
    for g in (0.25, -0.25, 0.5, -0.5):
        n, y = run(f"pole_p{p}_s{s}_g{g}_m{m}", (k + g*k**(-m))**p, p, s, 0.0, K)
        D[g] = n*(y - y0)
    A = lambda g: (D[g] - D[-g])/2
    a1 = (8*A(0.25) - A(0.5))/1.5
    mp.mp.dps = 30; c = c_p_mp(p); pm = mp.mpf(p); mm = mp.mpf(m)
    W = lambda q: (4*c)**q*mp.gamma(q + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(q + 1))
    q, q1 = mm/pm, (mm + 1)/pm
    lead = float(-mm*W(q)*mp.pi*mp.cot(mp.pi*q))
    R = a1 - lead*n**(-m)
    zeta_terms = []
    for j in range(1, int(np.ceil(3.5/p))):
        arg = 1 + mm - pm*j
        if abs(arg - 1) < 1e-12: continue
        cj = float(pm*W(j)*pm*j*mp.zeta(arg)); zeta_terms.append((j*p, cj)); R = R - cj*n**(-j*p)
    tgt = 1 + m
    print(f"p={p} s={s} m={m}: q={float(q):.4f} q1={float(q1):.4f}  lead pole coef {lead:+.6f}  zeta terms {[(round(e, 3), round(v, 6)) for e, v in zeta_terms]}")
    # fit R on n >= lo with a pool of exponents around the target (first order in g only)
    pool = sorted({round(e, 9) for e in [tgt, tgt + 1, 1 + m + p, 1 + p, 1 + 2*p, 2 + p, m + p, 2 + m + p, 3 + m] if e > m + 1e-9})
    res = []
    for lo in (200, 400):
        for J in (4, 5, 6):
            E = [e for e in pool if e != tgt][:J - 1] + [tgt]
            sel = n >= lo; Am = np.vstack([n[sel]**-e for e in E]).T
            co = np.linalg.lstsq(Am, R[sel], rcond=None)[0]; res.append(co[E.index(tgt)])
    res = np.array(res); S, hr = float(np.median(res)), float((res.max() - res.min())/2)
    ca, cb = float(mm*pm*q1*W(q1)/2), float(pm*q1*W(q1))
    print(f"   subleading coefficient of n^-{tgt} (per unit g): S = {S:+.6f} (half-range {hr:.1e})")
    print(f"   candidates: (a) Jacobian {ca:+.6f}   (b) tan pole {cb:+.6f}   (a)+(b) {ca + cb:+.6f}   (b)-(a) {cb - ca:+.6f}")
    print(f"   ratios: S/(p q1 W(q1)) = {S/cb:+.6f}   S/lead = {S/lead if lead else float('nan'):+.6f}   S/W(q1) = {S/float(W(q1)):+.6f}")
    # g^3 contamination check: compare a1 with the plain antisymmetric A(1/4)/(1/4) at the target
    for e, v in zeta_terms:
        if abs(e - tgt) < 1e-9: print(f"   collision with the zeta layer at n^-{tgt}: total first-order coefficient (zeta + subleading) = {S + v:+.6f}")
    C_.check(f"extraction stable p={p}", hr, 0.0, max(0.05*abs(S), 2e-3))
C_.finish()
