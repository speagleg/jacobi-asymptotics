"""SPEC direction 4: GUE-like vs Poisson node statistics. Nodes lam_k = x_k^p, weights x_k^{-s}, where x_k = k for k > M and, for
k <= M = 3000:
  gue:     unfolded CUE eigenphases (Haar unitary of size M via QR, seed 7): x = M theta/(2 pi), shifted so x_1 = 1 (deviation O(sqrt log k));
  poisson: 1 + cumulative Exp(1) spacings, rescaled so x_M = M (a Poisson bridge; deviation O(sqrt k)).
Diagnostics, with y_lat the pure lattice:
  N(n) := n (y_n - y_n^lat);
  count predictor  C(n) := p * Delta(n),  Delta(n) := #{k: x_k < x*(n)} - #{k: k < x*(n)},  x*(n) := n (4c)^{-1/p} (threshold, u = 1);
  S2' predictor    S(n) := sum over nodes with u <= 1 - eta of p[(1 - u_act)^{-1/2} - (1 - u_lat)^{-1/2}], eta = 3 n^{-2/3} (cut at the
                   Airy scale), plus p * (count difference inside the cut window);
  report RMS of N, of N - C, of N - S over n-octaves, and correlations."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np
from spec_common import run, c_p_mp, NMAX
from so_coeffs import coeffs
from so_fit import sequences
mode = sys.argv[1]; seed = int(sys.argv[2]) if len(sys.argv) > 2 else 7; p, s, M = 0.6, 2.0, 3000; K = 200*NMAX
x = np.arange(1, K + 1, dtype=np.float64)
if mode == "gue":
    rng = np.random.default_rng(seed)
    Z = (rng.standard_normal((M, M)) + 1j*rng.standard_normal((M, M)))/np.sqrt(2)
    Q, R = np.linalg.qr(Z); Q = Q*(np.diag(R)/np.abs(np.diag(R)))
    th = np.sort(np.mod(np.angle(np.linalg.eigvals(Q)), 2*np.pi))
    xs = M*th/(2*np.pi); xs = xs - xs[0] + 1.0
elif mode == "poisson":
    rng = np.random.default_rng(seed)
    e = rng.exponential(1.0, M - 1); xs = np.concatenate([[1.0], 1 + np.cumsum(e)]); xs = 1 + (xs - 1)*(M - 1)/(xs[-1] - 1)
x[:M] = xs
assert np.all(np.diff(x) > 0)
print(f"{mode} seed {seed}: max |x_k - k| (k <= M) = {np.max(np.abs(xs - np.arange(1, M + 1))):.2f}")
n, y = run(f"stats_{mode}_p{p}_s{s}" + ("" if seed == 7 else f"_seed{seed}"), x**p, p, s, 0.0, K)
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
c = float(c_p_mp(p)); N = n*(y - y0); kk = np.arange(1, K + 1, dtype=np.float64)
C = np.empty_like(N); S = np.empty_like(N)
for i, nv in enumerate(n):
    xstar = nv*(4*c)**(-1/p)
    C[i] = p*(np.searchsorted(x, xstar) - np.searchsorted(kk, xstar))
    eta = 3*nv**(-2/3)
    ua = 4*c*(x[:M + 10]/nv)**p; ul = 4*c*(kk[:M + 10]/nv)**p
    ma, ml = ua <= 1 - eta, ul <= 1 - eta
    S[i] = p*(np.sum((1 - ua[ma])**-0.5) - np.sum((1 - ul[ml])**-0.5))
print(f"{'window':>12} {'RMS N':>10} {'RMS N-C':>10} {'RMS N-S':>10} {'corr(N,C)':>10} {'corr(N,S)':>10}")
for lo in (50, 100, 200, 400, 800):
    sel = (n >= lo) & (n < 2*lo)
    r = lambda v: np.sqrt(np.mean(v[sel]**2))
    print(f"[{lo:4d},{2*lo:4d}) {r(N):10.3e} {r(N - C):10.3e} {r(N - S):10.3e} {np.corrcoef(N[sel], C[sel])[0,1]:10.4f} {np.corrcoef(N[sel], S[sel])[0,1]:10.4f}")
