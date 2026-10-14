"""Paper 1 Remark (NUMERICAL): Monien's p=1 density (arXiv:0901.1883 Thm 3.1, as quoted in research/G2/CITATIONS.md (M))
vs the density of mu*_u at p=1 from Theorem B*, rho*(u) = I_{min(1, 1/(2u))}(3/2, 1/2) (regularized incomplete beta)."""
import mpmath as mp
mp.mp.dps = 30
def monien(x):
    if x <= mp.mpf(1)/2: return mp.mpf(1)
    r = mp.sqrt(2*x-1)
    return 2/mp.pi*(mp.atan(1/r) - r/(2*x))
def rho_star(u, p=1):
    I = mp.sqrt(mp.pi)/2*mp.gamma(1/mp.mpf(p)+mp.mpf(1)/2)/mp.gamma(1/mp.mpf(p)+1)
    c = (mp.pi/(2*I))**p/4
    V = min(mp.mpf(1), u**(-p)/(4*c))
    return mp.betainc(1/mp.mpf(p)+mp.mpf(1)/2, mp.mpf(1)/2, 0, V, regularized=True)
mx = 0
for x in ['0.1','0.5','0.5001','0.6','0.75','1','2','5','10','100','1e4']:
    x = mp.mpf(x); d = monien(x)-rho_star(x); mx = max(mx, abs(d))
    print(f"x={mp.nstr(x,6):>8}  Monien {mp.nstr(monien(x),20)}  rho* {mp.nstr(rho_star(x),20)}  diff {mp.nstr(d,3)}")
print("max |diff| =", mp.nstr(mx, 3))
# total mass of rho*_u for a few p (should be 1)
for p in (0.5, 1, 2, 3):
    I = mp.sqrt(mp.pi)/2*mp.gamma(1/mp.mpf(p)+mp.mpf(1)/2)/mp.gamma(1/mp.mpf(p)+1); us = 2*I/mp.pi
    m = mp.quad(lambda u: rho_star(u, p), [0, us, 2*us, 10, 100, 1000, mp.inf])
    print(f"p={p}: int rho* du = {mp.nstr(m, 15)}")
