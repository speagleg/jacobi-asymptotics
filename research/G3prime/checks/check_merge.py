"""G3' sensitivity probe (NUMERICAL, rkpw double).
[1] smooth model with a fraction phi of indices made double zeros, spread over all scales: shift of S_n vs phi=0,
    against the heuristic 2 log(1-phi).
[2] the same, but double zeros only in the index window [n0/2, n0): at which n does the shift appear?
[3] true zeros (Odlyzko, M = 2e6): S_n with true x_j and with smooth x~_j, against the smooth model; normalized gaps.
Measures: sigma = sum 2 x_k delta_{x_k}, x_k = 1/(gamma_k^2 + 1/4), indexed WITH multiplicity; equal atoms are merged
(weights added) before building the DiscreteMeasure (from_atoms rejects duplicates)."""
import sys
import time
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.measures.lfun import (Ninv, _atoms, load_odlyzko, merge_repeats, model_zeros, tail_nodes)
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.averaged import averaged_law


def measure_merged(g, label):
    """Zero measure for ordinates g (with multiplicity), equal atoms merged, smooth tail beyond the data."""
    x, w = _atoms(g)
    ux, inv = np.unique(x, return_inverse=True)
    uw = np.bincount(inv, weights=w)
    T, m = tail_nodes(Ninv(len(g) + 0.5))
    return DiscreteMeasure.from_atoms(ux, uw, tail=_atoms(T, m), label=label), x


def S(g, ns, label):
    mu, x = measure_merged(g, label)
    nmax = max(ns)
    t = time.time()
    b = jacobi_coeffs(mu, nmax).b
    return averaged_law(b, x, 2.0, ns), time.time() - t


def part1(J=200_000, ns=(250, 500, 1000, 2000, 4000)):
    print("[1] smooth model J=%d, double zeros at every m-th index (fraction phi = 1/m of indices repeated)" % J)
    g0 = model_zeros(J)
    base, _ = S(g0, ns, "smooth")
    print("    phi=0 S_n: " + "  ".join(f"n={n}:{base[n]:+.5f}" for n in ns))
    for m in (10, 4, 2):
        phi = 1 / m
        idx = np.arange(0, J - 1, m)
        s, dt = S(merge_repeats(g0, idx), ns, f"merged m={m}")
        print(f"    phi={phi:.3f} pred 2log(1-phi)={2*np.log(1-phi):+.4f}  shift: " +
              "  ".join(f"n={n}:{s[n]-base[n]:+.4f}" for n in ns) + f"   ({dt:.0f}s)")


def part2(J=200_000, n0=2000, ns=(500, 1000, 1500, 2000, 3000, 4000, 8000)):
    print(f"[2] double zeros only in index window [{n0//2}, {n0}) (every 2nd index there)")
    g0 = model_zeros(J)
    base, _ = S(g0, ns, "smooth")
    idx = np.arange(n0 // 2, n0 - 1, 2)
    s, _ = S(merge_repeats(g0, idx), ns, "window")
    print("    shift: " + "  ".join(f"n={n}:{s[n]-base[n]:+.5f}" for n in ns))


def part3(M=2_000_000, ns=(100, 1000, 5000, 10000, 20000)):
    print(f"[3] true zeros, Odlyzko M={M}")
    g = load_odlyzko(M)
    gs = model_zeros(M)
    mu_t, xt = measure_merged(g, "true")
    mu_s, xs = measure_merged(gs, "smooth")
    nmax = max(ns)
    t = time.time()
    bt = jacobi_coeffs(mu_t, nmax).b
    bs = jacobi_coeffs(mu_s, nmax).b
    print(f"    rkpw time {time.time()-t:.0f}s; distinct true atoms {mu_t.N} (incl. tail)")
    St, Sts, Ss = averaged_law(bt, xt, 2, ns), averaged_law(bt, xs, 2, ns), averaged_law(bs, xs, 2, ns)
    for n in ns:
        print(f"    n={n:6d}  S_smooth={Ss[n]:+.6f}  S_true(x_true)={St[n]:+.6f}  S_true(x_smooth)={Sts[n]:+.6f}"
              f"  diff(true x)={St[n]-Ss[n]:+.2e}  diff(smooth x)={Sts[n]-Ss[n]:+.2e}")
    d = np.diff(g) * np.log(g[:-1] / (2 * np.pi)) / (2 * np.pi)
    print(f"    normalized gaps: min={d.min():.5f} at k={int(d.argmin())+1}; repeated ordinates: {int(np.sum(d == 0))}")
    for delta in (0.01, 0.05, 0.1):
        print(f"    fraction of normalized gaps < {delta}: {np.mean(d < delta):.3e}")
    print(f"    max |gamma_k - gamma~_k| = {np.max(np.abs(g - gs)):.4f}")


if __name__ == "__main__":
    parts = sys.argv[1:] or ["1", "2", "3"]
    for p in parts:
        {"1": part1, "2": part2, "3": part3}[p]()
        sys.stdout.flush()
