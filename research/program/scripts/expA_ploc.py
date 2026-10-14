"""Compare E1 data with the local-exponent prediction R_n ≈ [c(p_loc(n))/c(p)]·(1 − (s−1)/(2n)), p_loc := −n f'(n)/f(n)."""
import numpy as np
from scipy.special import gamma
def c(p): I = np.sqrt(np.pi)/2*gamma(1/p+.5)/gamma(1/p+1); return .25*(np.pi/(2*I))**p
p, s = 2.0, 2.0
h = 1e-6
fams = {"log1": lambda k: k**-p*np.log(k+np.e), "logm2": lambda k: k**-p*np.log(k+np.e)**-2,
        "sinll": lambda k: k**-p*(2+np.sin(np.log(np.log(k+3)))), "Ha": lambda k: k**-p*(1+1/np.log(k+2))}
obs = {"log1": [0.92501,0.94982,0.96385,0.97196,0.97687], "logm2": [0.99567,1.01948,1.02950,1.03285,1.03311],
       "sinll": [0.95211,0.97669,0.98957,0.99626,0.99974], "Ha": [0.95577,0.97900,0.99067,0.99639,0.99910]}
ns = np.array([50,100,200,400,800.])
print("dlogc/dp at p=2:", (np.log(c(2+h))-np.log(c(2-h)))/(2*h))
for nm, f in fams.items():
    pl = -ns*(np.log(f(ns+h))-np.log(f(ns-h)))/(2*h)
    pred = c(pl)/c(p)*(1-(s-1)/(2*ns))
    print(f"{nm:6s} p_loc " + " ".join(f"{v:.4f}" for v in pl) + " | pred " + " ".join(f"{v:.5f}" for v in pred)
          + " | obs " + " ".join(f"{v:.5f}" for v in obs[nm]) + " | obs-pred " + " ".join(f"{o-q:+.4f}" for o,q in zip(obs[nm],pred)))
