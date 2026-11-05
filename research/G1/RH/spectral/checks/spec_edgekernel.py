"""SPEC §3.16 probe: the single-node response kernel through the soft edge, in the linear regime, and its scaling collapse.
Node k0 of sigma_{p,s} (p = 0.6, s = 2) is moved to k0 +- h (weight follows the node), h = 0.05; the linear response per unit h is
  F(n; k0) := [D(n; +h) - D(n; -h)]/(2h),   D(n; h) := n (y_n(moved) - y_n(lattice)).
The node crosses the edge (u = 1) at n*(k0) = k0 (4c)^{1/p}. Collapse variable tau := (n - n*)/n*^{1/3}.
Outside the band (tau >> 1) S2' differentiated predicts F -> p^2/(2k0) u (1-u)^{-3/2} (u = 4c (k0/n)^p), i.e. F ~ C tau^{-3/2}
with no n*-scaling; inside the band (tau < 0) the response oscillates. This script prints F on a tau grid for each k0 so that the
amplitude scaling n*^a and the shape can be read off, and the integrals sum_n F (out of band, in band) per k0.
Usage: spec_edgekernel.py k0 [k0 ...]"""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np
from spec_common import run, c_p_mp, NMAX
from so_coeffs import coeffs
from so_fit import sequences
p, s, h = 0.6, 2.0, 0.05; K = 200*NMAX
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
c = float(c_p_mp(p)); kk = np.arange(1, K + 1, dtype=np.float64)
for k0 in [int(a) for a in sys.argv[1:]]:
    D = {}
    for hh in (h, -h):
        k = kk.copy(); k[k0 - 1] = k0 + hh
        n, y = run(f"turn_p{p}_s{s}_k{k0}_h{hh}", k**p, p, s, 0.0, K)
        D[hh] = n*(y - y0)
    F = (D[h] - D[-h])/(2*h); Q = (D[h] + D[-h])/2          # linear part, and the quadratic (curvature) part
    nstar = k0*(4*c)**(1/p); tau = (n - nstar)/nstar**(1/3)
    u = 4*c*(k0/n)**p
    s2 = np.where(u < 1, p*p/(2*k0)*u*np.abs(1 - u)**-1.5, np.nan)
    print(f"k0={k0}: n* = {nstar:.1f}, n*^(1/3) = {nstar**(1/3):.2f};  max|quadratic part|/max|linear part| = {np.max(np.abs(Q))/np.max(np.abs(F))/h:.3f} (per unit h)")
    print(f"   {'tau':>6} {'n':>6} {'F':>12} {'S2p-deriv':>12}")
    for t in (-12, -9, -6, -4, -3, -2, -1, -0.5, 0, 0.5, 1, 2, 3, 4, 6, 9, 12, 20):
        nv = int(round(nstar + t*nstar**(1/3)))
        if 1 <= nv <= NMAX:
            i = nv - 1; print(f"   {t:6.1f} {nv:6d} {F[i]:+12.5e} {s2[i]:+12.5e}")
    inb, outb = (tau < -1) & (n > 20), (tau > 3)
    print(f"   sum_n F over tau < -1: {np.sum(F[inb]):+.4e}   RMS F over tau in [-6,-1]: {np.sqrt(np.mean(F[(tau > -6) & (tau < -1)]**2)):.4e}"
          f"   sum_n F over tau > 3: {np.sum(F[outb]):+.4e}")
    np.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', '..', 'tmp', f'edgekernel_k{k0}.npy'), np.vstack([n, tau, F, Q]))
