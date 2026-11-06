"""Check (NUMERICAL): for p<1 the o(1) in log(X_n (2 pi n)^p) decays like n^{-p} (slow); large-n values."""
from math import log, pi
from xn_freeform import cp, S_n, M_n
for p in [0.5, 0.75]:
    c = cp(p)
    for n in [160, 320, 640, 1280]:
        S, _ = S_n(p, n); M, _ = M_n(p, n, T=200.0)
        r = -log(c) - 2*n*p - M + S + p*log(2*pi*n)
        print(f"p={p} n={n:5d} log(X_n(2pi n)^p)={r:+.5e}  n^p*that={n**p*r:+.5f}")
