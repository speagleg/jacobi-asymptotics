"""SPEC §3.5 (exact identity, checked at 50 digits): for nodes y_k > 0 with masses w_k and phi(y) = y/(1 + kappa y),
  D_m( sum_k w_k delta_{phi(y_k)} ) = D_m( sum_k w_k (1 + kappa y_k)^{-2(m-1)} delta_{y_k} ),
since phi(a) - phi(b) = (a - b)/((1 + kappa a)(1 + kappa b)) and Heine's formula D_m = (1/m!) sum over m-tuples of prod (x_i - x_j)^2 prod w.
(Hankel determinants of moments; random small discrete measure.)"""
import mpmath as mp
mp.mp.dps = 50
import random
random.seed(3)
y = [mp.mpf(random.random()) for _ in range(9)]; w = [mp.mpf(random.random()) for _ in range(9)]
kap = mp.mpf('0.7')
def hankel(nodes, masses, m):
    mom = [sum(ms*x**j for x, ms in zip(nodes, masses)) for j in range(2*m - 1)]
    return mp.det(mp.matrix([[mom[i + j] for j in range(m)] for i in range(m)]))
worst = 0
for m in range(1, 8):
    lhs = hankel([yy/(1 + kap*yy) for yy in y], w, m)
    rhs = hankel(y, [ww*(1 + kap*yy)**(-2*(m - 1)) for yy, ww in zip(y, w)], m)
    rel = abs(lhs - rhs)/abs(lhs); worst = max(worst, rel)
    print(f"m={m}: D_m(phi_* sigma) = {mp.nstr(lhs, 15)}   D_m(varying weight) = {mp.nstr(rhs, 15)}   rel {mp.nstr(rel, 2)}")
assert worst < mp.mpf(10)**-40
print("ALL ASSERTIONS PASSED")
