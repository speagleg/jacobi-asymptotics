"""G3'* probe T (NUMERICAL): does the averaged law survive arbitrary thinning of the smooth model when normalized by the
measure's OWN atoms y_j?  S_n^own := (2/n^2) sum (n-j) log(b_j / y_j) - log(pi^2/16).  Reports S_n^own(E) - S_n^own(N).
Patterns delete index blocks; 'holes' patterns make the atom density oscillate log-periodically (macroscopically)."""
import sys
import time
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.measures.lfun import Ninv, _atoms, model_zeros, tail_nodes
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.averaged import averaged_law

J = int(sys.argv[1]) if len(sys.argv) > 1 else 400_000
NS = [250, 354, 500, 707, 1000, 1414, 2000, 2828, 4000, 5657, 8000, 11314, 16000]


def S_own(keep, label):
    g = model_zeros(J)[keep]
    x, w = _atoms(g)
    T, m = tail_nodes(Ninv(J + 0.5))
    mu = DiscreteMeasure.from_atoms(x, w, tail=_atoms(T, m), label=label)
    t = time.time()
    b = jacobi_coeffs(mu, max(NS)).b
    return averaged_law(b, mu.atoms, 2, NS), time.time() - t


def block_mask(lo_frac, hi_frac, kmin=4, every=1):
    """delete (every-th index of) [lo*2^k, hi*2^k) for all k >= kmin (0-based indices)"""
    keep = np.ones(J, bool)
    k = kmin
    while lo_frac * 2 ** k < J:
        a, b = int(lo_frac * 2 ** k), min(int(hi_frac * 2 ** k), J)
        keep[a:b:every] = False if every == 1 else keep[a:b:every] & False
        k += 1
    return keep


if __name__ == "__main__":
    base, dt = S_own(np.ones(J, bool), "smooth")
    print(f"J={J}  n: " + " ".join(f"{n:>7d}" for n in NS))
    print("smooth S_n^own:  " + " ".join(f"{base[n]:+.4f}" for n in NS) + f"  ({dt:.0f}s)")
    pats = {
        "holes [1,1.5)2^k full": block_mask(1.0, 1.5),
        "holes [1,1.8)2^k full": block_mask(1.0, 1.8),
        "holes [1,1.5)2^k every2": block_mask(1.0, 1.5, every=2),
        "random keep 50%": np.random.default_rng(0).random(J) < 0.5,
    }
    for name, keep in pats.items():
        keep[:8] = True
        s, dt = S_own(keep, name)
        print(f"{name:24s} shift: " + " ".join(f"{s[n]-base[n]:+.4f}" for n in NS) + f"  ({dt:.0f}s)")
        sys.stdout.flush()
