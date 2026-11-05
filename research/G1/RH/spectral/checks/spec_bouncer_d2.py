"""SPEC probe: the n^-2 coefficient for the Dirichlet/Neumann bouncer (p = 2/3), from the caches of spec_bouncer.py /
spec_neumann.py. Prediction (index-shift layer): with index offset delta = a - 1 (Dirichlet a = 3/4, Neumann a = 1/4),
  d2 = d2_0(p, s) + p(p+1) delta^2/2 - (p+1) delta d1_0,  d1_0 = -(s-1)/2,
since the WKB corrections to lam'^{1/p} are O(k^{-2}) (they enter the index map at relative order t^-2, i.e. n^-3 in b_n).
The zeta layer: eps_1 = eps_2 = 0 (Z(-1) = Z(-2) = 0), so nothing is subtracted beyond d1."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from spec_common import run, fit, NMAX, CACHE, _find, Checks
C_ = Checks()
from spec_airy import zeros
import mpmath as mp
d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
p = 2/3; K = 200*NMAX
print(f"{'case':>10} {'s':>4} | {'n^-2 fit':>12} {'(hr)':>8} | {'index-shift':>12} {'diff':>9} | {'lattice d2_0':>12}")
for case, a, tag in (("Dirichlet", 0.75, "bouncer_s{s}"), ("Neumann", 0.25, "neumann_s{s}")):
    for s in (2.0, 3.0):
        try: _find(tag.format(s=s))
        except FileNotFoundError: continue
        n, y = run(tag.format(s=s), None, p, s, 0.0, K)
        delta = a - 1; d10 = -(s - 1)/2
        d1 = d10 - p*delta
        v, h = fit(n, y - d1/n, p, [1.0], 2.0)
        pred = d2f(p, s) + p*(p + 1)*delta**2/2 - (p + 1)*delta*d10
        print(f"{case:>10} {s:4} | {v:+12.6f} {h:8.1e} | {pred:+12.6f} {v - pred:+9.1e} | {d2f(p, s):+12.6f}")
        C_.check(f"d2 {case} s={s}", v, pred, max(3*h, 1e-4))
C_.finish()
