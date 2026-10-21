"""JZC M3a, gap 1 of Theorem H (JZC_M3a_H_G1u.md §5): end-to-end test of the n-uniform comparison in the regime |beta'| >= 1
(beta' = alpha + 2 delta <= -1), which H-d's data covered only at one point (p = 1.5, s = 2, delta = -1/2: beta' = -4/3).
NUMERICAL (Rule N): Jacobi coefficients of the actual Hurwitz measures sigma^d = sum_{k>=1} (k+d)^{-s} delta_{(k+d)^{-p}}
(second_order/checks/so_coeffs.coeffs: K atoms + Gauss-Jacobi continuum tail, binary128 RKPW, n <= 1600), fitted by least squares
over the exponents {1 + i + j p} (spec_common.fit: median over windows and truncation orders; tolerance max(3 * half-range, floor)
as in spec_hur.py). Rule X: nothing is fitted to the predictions; the predictions are closed forms / m4_rh4 outputs.
Cases (alpha = (s - 1 - p)/p = -1/2): (p, s, delta) = (1.5, 1.75, -0.8), (1.5, 1.75, -0.5), (3, 2.5, -0.8), (3, 2.5, -0.5);
beta' = -2.1, -1.5, -2.1, -1.5. Predictions of M(beta', nu = alpha) (Theorem H(i), JZC_M4 §7):
  d1 = -p(beta' + 1)/2 (= -(s-1)/2 - p delta);  d2 = p(p+1)(beta'+1)^2/8 - (p+2)alpha^2/8 + (p+1)/12 (decoupled E2 formula, exact);
  p = 1.5: eps1 (n^{-1-p}) = 2 p c zeta(-p, a) (beta-free; zeta(-p, a) by mpmath, the identification of Remark 3.3, NUMERICAL);
  p = 3: d3 = m4_rh4.run(p, beta', nu = alpha)[3] (mu = 0; no band-factor term lands on n^{-3} at p = 3).
Controls (must fail): the lattice prediction (delta ignored: beta' -> alpha) for d1; H2 (beta = nu = alpha + 2 delta) for d2.
Truncation: the K and 2K measures give the same fits (difference < tolerance / 10) where both were computed."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
os.environ.setdefault("KORD", "4")
import numpy as np, mpmath as mp
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import Checks, fit
import m4_rh4 as M
mp.mp.dps = 40
C_ = Checks()
CASES = [(1.5, 1.75, -0.8, (160000, 320000)), (1.5, 1.75, -0.5, (160000, 320000)), (3.0, 2.5, -0.8, (160000, 320000)), (3.0, 2.5, -0.5, (160000,))]


def d2dec(p, beta, nu): return p*(p + 1)*(beta + 1)**2/8 - (p + 2)*nu**2/8 + (p + 1)/mp.mpf(12)


for (p, s, d, Ks) in CASES:
    P = mp.mpf(p); al = (mp.mpf(s) - 1 - P)/P; D = mp.mpf(d); bp = al + 2*D; c = mp.mpf(c_p_mp(p)); a = 1 + D
    pred = {"d1": -P*(bp + 1)/2, "d2": d2dec(P, bp, al)}
    if p == 1.5: pred["eps1"] = 2*P*c*mp.zeta(-P, a)
    if p == 3.0:
        base, _ = M.run(P, bp, c=c, nu=al); pred["d3"] = base[3]
        assert abs(base[1] - pred["d1"]) < 1e-25 and abs(base[2] - pred["d2"]) < 1e-25
    ctrl = {"d1 (lattice, delta ignored)": -P*(al + 1)/2, "d2 (H2: beta = nu = alpha + 2 delta)": d2dec(P, bp, bp)}
    fits = {}
    for K in Ks:
        alpha_c, b = coeffs(p, s, K, 1600, d)
        n, y, *_ = sequences(p, alpha_c, b); n = n.astype(float)
        F = {}
        F["d1"] = fit(n, y, p, [], 1.0)
        r = y - float(pred["d1"])/n
        F["d2"] = fit(n, r, p, [1.0], 2.0)
        r2 = r - float(pred["d2"])/n**2
        if p == 1.5: F["eps1"] = fit(n, r2, p, [1.0, 2.0], 1 + p)
        if p == 3.0: F["d3"] = fit(n, r2, p, [1.0, 2.0], 3.0)
        fits[K] = F
    K0 = Ks[0]; floors = {"d1": 1e-5, "d2": 1e-4, "eps1": 1e-4, "d3": 1e-3}
    print(f"p={p} s={s} delta={d} (alpha={float(al):+.3f}, beta'={float(bp):+.3f}), K = {Ks}:")
    for k, v in pred.items():
        val, hr = fits[K0][k]; tol = max(3*hr, floors[k])
        print(f"   {k:5s}: fit {val:+.7f} (half-range {hr:.1e}) | M(beta', alpha) {float(v):+.7f} | dev/tol {abs(val - float(v))/tol:.3f}", flush=True)
        C_.check(f"{k} p={p} s={s} d={d}", val, float(v), tol)
        if len(Ks) > 1:
            v2, _ = fits[Ks[1]][k]
            print(f"          K -> 2K: {val:+.7f} -> {v2:+.7f} (diff {abs(v2 - val):.1e})")
            C_.check(f"truncation K -> 2K {k} p={p} d={d}", abs(v2 - val), 0.0, tol/10)
    for k, v in ctrl.items():
        key = k.split()[0]; val, hr = fits[K0][key]; tol = max(3*hr, floors[key])
        dev = abs(val - float(v))/tol
        print(f"   control {k}: {float(v):+.7f}, dev/tol {dev:.1f} (must be > 10)")
        C_.check(f"CONTROL {k} excluded p={p} d={d}", float(dev > 10), 1.0, 0.0)
C_.finish()
