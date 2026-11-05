"""SPEC §3.17 probe: is the Lanczos noise a LINEAR statistic of the spectral displacements?
Nodes x_k(eps) = k + eps (x_k - k) for k <= M = 3000 (x_k: the gue / poisson realisations of spec_stats.py, seed 7), x_k = k beyond;
lam = x^p, weights x^{-s} (p = 0.6, s = 2). N_eps(n) := n (y_n(eps) - y_n(lattice)).
Linear part L(n) := [N_eps - N_{-eps}]/(2 eps) at eps = 0.05; compared with the full N_1 (cached by spec_stats.py) and with N_{1/2}.
If N_1 ~ L, the noise is the linear statistic sum_k F(n;k) h_k (h_k = x_k - k) of the single-node kernel of spec_edgekernel.py, and
its variance is set by the displacement covariance (rigidity), i.e. sum_{k,l} F F Cov(h_k, h_l)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np
from spec_common import run, NMAX
from so_coeffs import coeffs
from so_fit import sequences
p, s, M = 0.6, 2.0, 3000; K = 200*NMAX
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
k = np.arange(1, K + 1, dtype=np.float64)
def realisation(mode, seed=7):
    rng = np.random.default_rng(seed)
    if mode == "gue":
        Z = (rng.standard_normal((M, M)) + 1j*rng.standard_normal((M, M)))/np.sqrt(2)
        Q, R = np.linalg.qr(Z); Q = Q*(np.diag(R)/np.abs(np.diag(R)))
        th = np.sort(np.mod(np.angle(np.linalg.eigvals(Q)), 2*np.pi)); xs = M*th/(2*np.pi); return xs - xs[0] + 1.0
    e = rng.exponential(1.0, M - 1); xs = np.concatenate([[1.0], 1 + np.cumsum(e)]); return 1 + (xs - 1)*(M - 1)/(xs[-1] - 1)
for mode in sys.argv[1:] or ["gue", "poisson"]:
    h = realisation(mode) - k[:M]
    N = {}
    for eps in (0.05, -0.05, 0.5, 1.0):
        x = k.copy(); x[:M] += eps*h; assert np.all(np.diff(x) > 0)
        tag = f"stats_{mode}_p{p}_s{s}" if eps == 1.0 else f"noiselin_{mode}_eps{eps}"
        n, y = run(tag, x**p, p, s, 0.0, K); N[eps] = n*(y - y0)
    L = (N[0.05] - N[-0.05])/0.1; Q = (N[0.05] + N[-0.05])/(2*0.05**2)
    print(f"{mode} (seed 7): max|h| = {np.max(np.abs(h)):.2f}, RMS h = {np.sqrt(np.mean(h**2)):.2f}")
    print(f"  {'window':>12} {'RMS N_1':>9} {'RMS L':>9} {'RMS(N_1-L)':>11} {'corr(N_1,L)':>11} {'RMS(N_.5-L/2)':>13} {'RMS Q':>9}")
    for lo in (50, 100, 200, 400, 800):
        sel = (n >= lo) & (n < 2*lo); r = lambda v: np.sqrt(np.mean(v[sel]**2))
        print(f"  [{lo:4d},{2*lo:4d}) {r(N[1.0]):9.3f} {r(L):9.3f} {r(N[1.0] - L):11.3f} {np.corrcoef(N[1.0][sel], L[sel])[0, 1]:11.4f} {r(N[0.5] - L/2):13.3f} {r(Q):9.3f}")
