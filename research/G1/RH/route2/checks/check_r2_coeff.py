"""Plan 48 (NUMERICAL): Theorem RII (p = s = 2, alpha_x = -1/2) and the drifting-order (tilt) model, ROUTE2.md §§4-5.
w = k^{-2} Psi, Psi(k) = exp(L(log k)), L(u) = sqrt(log(e^u + e)) (analytic: the RII hypothesis H_an holds with L1 = L);
theta_n := L'(log n).  v = k^{-2};  v_sig := k^{-sig} with sig = s - theta_n (the "drifting-order" comparison: its hard-edge
Bessel order is alpha_x - theta_n/p).  Index convention: b_n couples p_{n-1}, p_n (b_n^2 = b2[n-1]); a_n = a[n].
Columns:
  B_n := n^p b_n(w)/c(p) - 1 and n*B_n  (RII: O(1/n));   E_n := n (a[n]/(2 sqrt(b2[n])) - 1) for w, the pairing of RH/checks/check_fine.py (RII: O(1); pure-power baseline e1 = p/2 = 1;
  with the other pairing a[n]/(2 sqrt(b2[n-1])) the pure power gives -1: an index-convention shift of the 1/n term);
  T_n := n (b_n(w)/b_n(v) - 1)/theta_n  (tilt law: -> 1/2; ROUTE2 §5: the O(eta_N/N) term of Prop. D');
  R_n := n (b_n(w)/b_n(v_sig) - 1)/theta_n  (drifting-order model residual; -> 0 means the tilt captures the 1/n term).
long double RKPW at K = 120000 and 240000 (truncation check).
Run from the jacobi-asymptotics root: .venv/bin/python ../ja-plan48/research/G1/RH/route2/checks/check_r2_coeff.py"""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.weyl import c_p

p, s = 2.0, 2.0; c = c_p(p)
L = lambda u: np.sqrt(np.log(np.exp(u) + np.e))  # noqa: E731
dL = lambda u: np.exp(u) / (2 * (np.exp(u) + np.e) * np.sqrt(np.log(np.exp(u) + np.e)))  # noqa: E731
NS = (100, 200, 400, 800)


def coeffs(K, logw, N):
    k = np.arange(1, K + 1, dtype=float); lw = logw(k); lw = lw - lw.max()
    r = jacobi_coeffs(DiscreteMeasure(k ** -p, np.exp(lw)), N, prec="ld")
    return np.sqrt(np.asarray(r.b2, float)), np.asarray(r.a, float)


for K in (120000, 240000):
    bw, aw = coeffs(K, lambda k: -s * np.log(k) + L(np.log(k)), 802)
    bv, _ = coeffs(K, lambda k: -s * np.log(k), 802)
    rows = []
    for n in NS:
        th = dL(np.log(n)); sig = s - th
        bs, _ = coeffs(K, lambda k: -sig * np.log(k), n + 2)
        Bn = n ** p * bw[n - 1] / c - 1; En = n * (aw[n] / (2 * bw[n]) - 1)  # Phase-0 (check_fine) pairing a[n], b2[n]; baseline e1 = p/2
        Tn = n * (bw[n - 1] / bv[n - 1] - 1) / th; Rn = n * (bw[n - 1] / bs[n - 1] - 1) / th
        rows.append(f"n={n}: theta={th:.4f} nB={n*Bn:+.4f} E={En:+.4f} T={Tn:.4f} R={Rn:+.4f}")
    print(f"K={K}:\n  " + "\n  ".join(rows), flush=True)
