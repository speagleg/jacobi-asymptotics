"""G2 Part B check (NUMERICAL): the explicit candidate optimizer
    mu* = int_0^1 omega_[0, beta_t] dt,  beta_t = 4 c(p) t^{-p}   (x = u^{-p} variable; omega = arcsine measure)
[1] density of mu* vs the constraint sigma(x) = (1/p) x^{-1-1/p}: saturated (=) for x >= 4c, strictly below for x < 4c;
    in u: saturated on (0, u_s], u_s = (4c)^{-1/p}.
[2] I(mu*) by quadrature of the closed form  I = log c - p E[log min(s,t)] = log c + 3p/2  vs kappa_p, and a direct
    Monte Carlo of iint log|x - y| d mu* d mu* (independent of the closed form).
[3] potential U*(x) = int log|x-y| d mu*(y): constant log c + p on (0, 4c), >= that beyond (KKT conditions)."""
import numpy as np
from scipy import integrate
from jacobi_asym.laws.weyl import c_p

rng = np.random.default_rng(0)


def dens(x, p, c):
    """density of mu* at x>0: (1/pi) int_0^min(1, t_x) dt / sqrt(x (beta_t - x)), t_x = (4c/x)^{1/p}"""
    tx = (4 * c / x) ** (1 / p)
    top = min(1.0, tx)
    f = lambda t: 1 / np.sqrt(x * (4 * c * t ** (-p) - x))
    val, _ = integrate.quad(f, 0, top, limit=200)
    return val / np.pi


def sample(p, c, N):
    t = rng.random(N)
    beta = 4 * c * t ** (-p)
    return beta * np.sin(np.pi * rng.random(N) / 2) ** 2      # arcsine on [0, beta]


def U(x, p, c):
    """potential: int_0^1 U_t(x) dt, U_t = log(beta_t/4) inside, log((x - b/2 + sqrt(x(x-b)))/2) outside"""
    def Ut(t):
        b = 4 * c * t ** (-p)
        if x <= b:
            return np.log(b / 4)
        return np.log((x - b / 2 + np.sqrt(x * (x - b))) / 2)
    val, _ = integrate.quad(Ut, 0, 1, limit=200, points=[min(1, (4 * c / x) ** (1 / p))])
    return val


for p in [0.5, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0]:
    c = c_p(p)
    kap = 1.5 * p + np.log(c)
    sig = lambda x: x ** (-1 - 1 / p) / p
    xs = 4 * c * np.array([0.01, 0.1, 0.5, 0.9, 0.999, 1.001, 2, 10, 1e3])
    ratio = [dens(x, p, c) / sig(x) for x in xs]
    xa, xb = sample(p, c, 400_000), sample(p, c, 400_000)
    mc = np.mean(np.log(np.abs(xa - xb)))
    Us = [U(x, p, c) for x in xs]
    print(f"p={p}: c={c:.6f} u_s={(4*c)**(-1/p):.4f}  kappa_p={kap:.6f}  MC I(mu*)={mc:.4f}+-{np.std(np.log(np.abs(xa-xb)))/np.sqrt(4e5):.4f}")
    print("   density/sigma at x/(4c) in [.01,.1,.5,.9,.999,1.001,2,10,1e3]: " + " ".join(f"{r:.4f}" for r in ratio))
    print(f"   U*(x) - (log c + p):                                        " + " ".join(f"{u-(np.log(c)+p):+.1e}" for u in Us))
