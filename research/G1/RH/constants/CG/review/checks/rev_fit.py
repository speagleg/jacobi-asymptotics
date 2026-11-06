"""Least-squares/collocation fit of r_m (from rev_*.out) with non-integer correction exponents (p<1: m^{-1-p})."""
import re, sys, mpmath as mp
mp.mp.dps = 30
def load(fn):
    d = {}
    for line in open(fn):
        g = re.match(r"m=\s*(\d+) r_m=\[([0-9.]+)", line)
        if g: d[int(g.group(1))] = mp.mpf(g.group(2))
    return d
for fn, p, s in [("rev_p06_s19.out", mp.mpf('0.6'), mp.mpf('1.9')), ("rev_p25_s5.out", mp.mpf('2.5'), 5)]:
    r = load(fn); ms = sorted(r)
    E = (p + 2) * (s - 1) / p; sh = (s - 1) / (2 * p)
    exps = sorted(set([1, 2, 3, 1 + p, 2 + p, 1 + 2 * p] if p < 1 else [1, 2, 3, 4]))
    for k in range(2, len(exps) + 1):
        ex = exps[:k]; use = ms[-(k + 1):]
        A = mp.matrix([[1] + [mp.mpf(m) ** (-e) for e in ex] for m in use]); b = mp.matrix([r[m] for m in use])
        sol = mp.lu_solve(A, b)
        print(f"{fn}: exps {[float(e) for e in ex]} on m={use}: limit-1 = {mp.nstr(sol[0]-1, 3)}, c1 = {mp.nstr(sol[1], 6)}"
              f"  (E*(s-1)/(2p) = {mp.nstr(-E*sh, 6)})")
