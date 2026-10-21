"""SPEC probe: the zeta layer of Hurwitz lattices at p = 1/j (j = 3, 4), shift d (a = 1 + d).
Predictions (S1 + index-shift layer):
  eps_i(a) = C(2i,i) p c^i zeta(-ip, a), i < j (fitted after subtracting d1 and the other eps; reported individually);
  n^-2 coefficient (merged) = d2_shift(d) + eps_j(a), eps_j(a) = p zeta(-1, a) since C(2j,j) c(1/j)^j = 1,
  d2_shift(d) = d2_0 + p(p+1) d^2/2 - (p+1) d d1_0."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from math import comb
from so_coeffs import coeffs, c_p_mp
from so_fit import sequences
from spec_common import fit, NMAX, Checks
C_ = Checks()
d2f = lambda p, s: (p + 1)*(s - 1)**2/(8*p) - (p + 2)*(s - 1 - p)**2/(8*p*p) + (p + 1)/12
jj, s, d = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
p = 1/jj; a = 1 + d; K = 200*NMAX
al, b = coeffs(p, s, K, NMAX, d); n, y, *_ = sequences(p, al, b); n = n.astype(float)
c = c_p_mp(p); eps = lambda i: float(comb(2*i, i)*p*c**i*mp.zeta(-i*mp.mpf(p), a))
d10 = -(s - 1)/2; d1 = d10 - p*d
base = y - d1/n
print(f"p = 1/{jj}, s = {s}, d = {d} (a = {a})")
for i in range(1, jj):
    r = base.copy(); skip = [1.0]
    for i2 in range(1, jj):
        if i2 != i: r = r - eps(i2)*n**(-1 - i2*p); skip.append(round(1 + i2*p, 9))
    v, h = fit(n, r, p, skip, 1 + i*p)
    C_.check(f"eps_{i}", v, eps(i), max(3*h, 1e-5))
    print(f"  eps_{i}: fit {v:+.7f} ({h:.1e})   Hurwitz {eps(i):+.7f}   diff {v - eps(i):+.1e}   [unshifted {float(comb(2*i,i)*p*c**i*mp.zeta(-i*mp.mpf(p))):+.7f}]")
r = base - sum(eps(i)*n**(-1 - i*p) for i in range(1, jj)); skip = [1.0] + [round(1 + i*p, 9) for i in range(1, jj)]
v, h = fit(n, r, p, skip, 2.0)
d2s = d2f(p, s) + p*(p + 1)*d*d/2 - (p + 1)*d*d10; ej = float(p*mp.zeta(-1, a))
print(f"  n^-2 (merged): fit {v:+.6f} ({h:.1e})   d2_shift + eps_{jj}(a) = {d2s:+.6f} + {ej:+.6f} = {d2s + ej:+.6f}   diff {v - d2s - ej:+.1e}"
      f"   [without eps_{jj}: diff {v - d2s:+.1e}]")
C_.check("merged n^-2", v, d2s + ej, max(3*h, 1e-4)); C_.finish()
