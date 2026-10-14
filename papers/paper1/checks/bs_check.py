"""Paper 1 Remark (NUMERICAL): Baricz-Stampach closed forms (as quoted in research/program/novelty_G2.md) for
det_{1<=i,j<=n} zeta(2(i+j)+2l-2), l in {0,1,2}, vs direct determinants, and the n^2 constant vs kappa_2."""
import mpmath as mp
mp.mp.dps = 60
nu = mp.mpf(1)/2
def log_sigma_det(n, l):
    # log det H_n^{(l)}(1/2), H_n^{(l)}(nu)_{ij} = sigma_{2(i+j)+2l-2}(nu)
    if l in (0, 1):
        return -2*n*(n+l)*mp.log(2) + mp.fsum((k-2*n-l)*mp.log(nu+k) for k in range(1, 2*n+l))
    if l == 2:
        return (-2*n*(n+2)*mp.log(2) + mp.log(n+1) + mp.log(n+nu+1)
                + mp.fsum((k-2*n-2)*mp.log(nu+k) for k in range(1, 2*n+2)))
def log_zeta_det_closed(n, l):
    # zeta(2m) = pi^{2m} sigma_{2m}(1/2); entry (i,j) has m = i+j+l-1: row factor pi^{2i+l-1}, column factor pi^{2j+l-1}
    return log_sigma_det(n, l) + 2*sum(2*i+l-1 for i in range(1, n+1))*mp.log(mp.pi)
def log_zeta_det_direct(n, l):
    M = mp.matrix(n, n)
    for i in range(1, n+1):
        for j in range(1, n+1):
            M[i-1, j-1] = mp.zeta(2*(i+j)+2*l-2)
    return mp.log(mp.det(M))
print("[1] closed form vs direct determinant (b = 2l-2)")
for l in (0, 1, 2):
    for n in (1, 2, 3, 5, 8):
        c, d = log_zeta_det_closed(n, l), log_zeta_det_direct(n, l)
        print(f"  l={l} b={2*l-2:+d} n={n}: closed {mp.nstr(c, 20)}  direct {mp.nstr(d, 20)}  diff {mp.nstr(c-d, 3)}")
kap2 = 3 + mp.log(mp.pi**2/16)
print(f"[2] kappa_2 = 3 + log(pi^2/16) = {mp.nstr(kap2, 15)}")
mp.mp.dps = 30
for l in (0, 1, 2):
    for n in (100, 1000, 10000, 100000):
        v = (log_zeta_det_closed(n, l) + 2*n*n*mp.log(n))/n**2
        print(f"  l={l} n={n}: (log det + 2n^2 log n)/n^2 = {mp.nstr(v, 12)}   minus kappa_2 = {mp.nstr(v-kap2, 6)}"
              f"   times n/log n = {mp.nstr((v-kap2)*n/mp.log(n), 6)}")
