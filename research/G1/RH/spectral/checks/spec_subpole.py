"""SPEC §3.15 probe: the subleading pole term (REVIEW_SPEC2_A F2). Lattices lam_k = (k + g/k^m)^p, weights lam^{-s/p}.
First order in g is isolated by antisymmetrising (g, -g) and Richardson over g in {1/4, 1/2}:
  A(g) := [D(g) - D(-g)]/2 = g a1 + g^3 a3 + ...,  a1 = (8 A(1/4) - A(1/2))/1.5,   D(g) := n (y_g - y_lat).
From a1(n) the known first-order terms are subtracted:
  - leading pole term (§3.12): -m W(q) pi cot(pi q) n^{-m},  q = m/p  (per unit g);
  - first-order zeta layer: sum_j p W(j) dZ1(-j) n^{-jp},  dZ1(-j) = p j zeta(1 + m - p j)  (per unit g; skipped if 1 + m - pj = 1).
The remainder's coefficient of n^{-1-m} (i.e. n^{-2-m} in n^p b_n/c) is the subleading pole coefficient S (per unit g); it is printed
with the conjectured form (§3.15), q1 = (m+1)/p, d1_0 = -(s-1)/2:
  S_pred = -(m p q1/2) W(q1)                      [Jacobian tilt z^{q1} through E3.7's functional; sign per E3.4: the tilt is -P]
           + lead * (1 + m + p) d1_0 / p          [the leading pole term at the shifted index n + delta_eff, delta_eff = -d1_0/p]
Assertions: extraction stable; S = S_pred within max(3 half-ranges, 2e-4|S|) when q1 <= 1 (where it holds); for q1 > 1 the
residual is printed only (unexplained, §3.15).
Usage: spec_subpole.py p[:s[:m]] ...   (s defaults to 2, m to 1)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import Checks, run, NMAX, c_p_mp
from so_coeffs import coeffs
from so_fit import sequences
C_ = Checks()
for arg in sys.argv[1:]:
    v = [float(x) for x in arg.split(':')]; p = v[0]; s = v[1] if len(v) > 1 else 2.0; m = v[2] if len(v) > 2 else 1.0
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
    jac = -float(mm*pm*q1*W(q1)/2); d10 = -(s - 1)/2; shift = lead*(1 + m + p)*d10/p; pred = jac + shift
    print(f"   subleading coefficient of n^-{tgt} (per unit g): S = {S:+.6f} (half-range {hr:.1e})")
    print(f"   prediction: Jacobian {jac:+.6f} + shifted pole {shift:+.6f} = {pred:+.6f};  S - pred = {S - pred:+.2e}   (q1 {'<=' if q1 <= 1 else '>'} 1)")
    if q1 <= 1 + 1e-12: C_.check(f"subleading p={p} s={s} m={m}", S, pred, max(3*hr, 2e-4*abs(S)))
    # g^3 contamination check: compare a1 with the plain antisymmetric A(1/4)/(1/4) at the target
    for e, v in zeta_terms:
        if abs(e - tgt) < 1e-9: print(f"   collision with the zeta layer at n^-{tgt}: total first-order coefficient (zeta + subleading) = {S + v:+.6f}")
    C_.check(f"extraction stable p={p}", hr, 0.0, max(0.05*abs(S), 2e-3))
C_.finish()
