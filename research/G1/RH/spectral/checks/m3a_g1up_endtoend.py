"""JZC M3a, Theorem H item 1 for 0 < p < 1 (JZC_M3a_H_G1u_plt1.md §5): end-to-end test of the glued alpha-frame comparison in the
regime |beta'| >= 1 at p < 1 (beta' = alpha + 2 delta <= -1). The stored p < 1 Hurwitz fits (m3a_g3_model) have beta' >= -1/3 only.
NUMERICAL (Rule N): Jacobi coefficients of the actual Hurwitz measures sigma^d = sum_{k>=1} (k+d)^{-s} delta_{(k+d)^{-p}}
(second_order/checks/so_coeffs.coeffs: K atoms + Gauss-Jacobi continuum tail, binary128 RKPW, n <= 1600; cache tmp/plan62_cache),
fitted by least squares over the exponents {1 + i + j p} (spec_common.fit: median over windows and truncation orders; tolerance
max(3 * half-range, floor), as in m3a_g1u_endtoend.py). Rule X: nothing is fitted to the predictions; the predictions are closed forms.
Cases (alpha = (s - 1 - p)/p = -1/2): (p, s, delta) = (0.6, 1.3, -0.8), (0.6, 1.3, -0.5), (0.75, 1.375, -0.8); beta' = -2.1, -1.5, -2.1.
Predictions of M(beta', nu = alpha) with the Hurwitz band factor (Theorem H(i)-(ii), JZC_M3a_H §1, §3.2):
  d1 = -p(beta' + 1)/2 (= -(s-1)/2 - p delta);
  d2 = p(p+1)(beta'+1)^2/8 - (p+2)alpha^2/8 + (p+1)/12 (decoupled E2 formula; cross-checked against m4_rh4.run(p, beta', nu=alpha));
  eps_j (n^{-1-jp}) = C(2j, j) p c^j * (-(jp/pi) Gamma(jp) (2 pi)^{-jp} S_j(delta)),  S_j(delta) = sum_m sin(pi j p/2 - 2 pi m delta)/m^{1+jp}
      (the Fourier-sum form, JZC_M3a_H §3.2; S_j from the Hurwitz series by residue classes, delta rational); j = 1, 2.
Rows: d1 (free fit); eps1, d2 (fits of y - d1/n over the free basis); eps2 (after subtracting d1, eps1, d2); d2|eps (after subtracting d1,
eps1, eps2: the n^-2 coefficient is poorly separated from n^{-1-p}, n^{-1-2p} at p = 0.6 in the free fit; each subtracted term is
itself tested in its own row, so the conditional row is not circular).
Controls (must fail): the lattice prediction (delta ignored: beta' -> alpha) for d1; H2 (beta = nu = alpha + 2 delta) for d2|eps; the lattice
band factor (S_1(0) in place of S_1(delta)) for eps1.
Truncation: K and 2K measures give the same fits (difference < tolerance / 10).
Rows whose tolerance exceeds |prediction|/3 are printed but not asserted (not discriminating; Rule N)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
os.environ.setdefault("KORD", "4")
import numpy as np, mpmath as mp
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import Checks, fit
import m4_rh4 as M
mp.mp.dps = 40
C_ = Checks(); PI = mp.pi
CASES = [(0.6, 1.3, (-4, 5), (160000, 320000)), (0.6, 1.3, (-1, 2), (160000, 320000)), (0.75, 1.375, (-4, 5), (160000, 320000))]


def d2dec(p, beta, nu): return p*(p + 1)*(beta + 1)**2/8 - (p + 2)*nu**2/8 + (p + 1)/mp.mpf(12)


def S_series(k, p, dnum, dden):
    sig = 1 + k*p; Q = dden; d = mp.mpf(dnum)/dden
    Z = sum(mp.expj(-2*PI*j*d)*mp.zeta(sig, mp.mpf(j)/Q) for j in range(1, Q + 1))/mp.mpf(Q)**sig
    return mp.im(mp.expj(PI*k*p/2)*Z)


def eps(j, p, c, S): return mp.binomial(2*j, j)*p*c**j*(-(j*p/PI)*mp.gamma(j*p)*(2*PI)**(-j*p)*S)


for (p, s, (dn, dd), Ks) in CASES:
    P = mp.mpf(p); al = (mp.mpf(s) - 1 - P)/P; D = mp.mpf(dn)/dd; d = float(D); bp = al + 2*D; c = mp.mpf(c_p_mp(p))
    S1, S2, S10 = S_series(1, P, dn, dd), S_series(2, P, dn, dd), S_series(1, P, 0, 1)
    pred = {"d1": -P*(bp + 1)/2, "eps1": eps(1, P, c, S1), "d2": d2dec(P, bp, al), "eps2": eps(2, P, c, S2)}
    pred["d2|eps"] = pred["d2"]
    base, _ = M.run(P, bp, c=c, nu=al)
    assert abs(base[1] - pred["d1"]) < 1e-25 and abs(base[2] - pred["d2"]) < 1e-25, (base[1], base[2])
    # Remark 3.3 (NOT QUOTED; NUMERICAL): eps_j = C(2j,j) p c^j zeta(-jp, 1+delta)
    assert abs(pred["eps1"] - 2*P*c*mp.zeta(-P, 1 + D)) < 1e-25
    ctrl = {"d1 (lattice, delta ignored)": -P*(al + 1)/2, "d2|eps (H2: beta = nu = alpha + 2 delta)": d2dec(P, bp, bp),
            "eps1 (lattice band factor, S_1(0))": eps(1, P, c, S10)}
    e1, e2 = 1 + p, 1 + 2*p
    fits = {}
    for K in Ks:
        alpha_c, b = coeffs(p, s, K, 1600, d)
        n, y, *_ = sequences(p, alpha_c, b); n = n.astype(float)
        F = {"d1": fit(n, y, p, [], 1.0)}
        r = y - float(pred["d1"])/n
        F["eps1"] = fit(n, r, p, [1.0], e1)
        F["d2"] = fit(n, r, p, [1.0], 2.0)
        r2 = r - float(pred["eps1"])/n**e1 - float(pred["d2"])/n**2
        F["eps2"] = fit(n, r2, p, [1.0, e1, 2.0], e2)
        r3 = r - float(pred["eps1"])/n**e1 - float(pred["eps2"])/n**e2
        F["d2|eps"] = fit(n, r3, p, [1.0, e1, e2], 2.0)
        fits[K] = F
    K0 = Ks[0]; floors = {"d1": 1e-5, "d2": 1e-4, "d2|eps": 1e-4, "eps1": 1e-4, "eps2": 1e-3}
    print(f"p={p} s={s} delta={d} (alpha={float(al):+.3f}, beta'={float(bp):+.3f}), K = {Ks}; S_1(delta) = {mp.nstr(S1, 8)}, S_1(0) = {mp.nstr(S10, 8)}:")
    for k, v in pred.items():
        val, hr = fits[K0][k]; tol = max(3*hr, floors[k])
        vac = tol > abs(float(v))/3          # Rule N: a row whose tolerance exceeds a third of the value is not discriminating
        print(f"   {k:5s}: fit {val:+.7f} (half-range {hr:.1e}) | M(beta', alpha) {float(v):+.7f} | dev/tol {abs(val - float(v))/tol:.3f}"
              + ("  [NOT ASSERTED: tolerance > |value|/3, not discriminating]" if vac else ""), flush=True)
        if vac: continue
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
