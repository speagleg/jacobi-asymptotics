"""Airy zeros a_k (Ai(a_k) = 0) via DLMF 9.9.6/9.9.18: a_k = -T(3pi/8 (4k-1)),
T(t) ~ t^{2/3}(1 + 5/48 t^-2 - 5/36 t^-4 + 77125/82944 t^-6 - 108056875/6967296 t^-8 + 162375596875/334430208 t^-10)."""
import mpmath as mp, numpy as np
TC = [mp.mpf(1), mp.mpf(5)/48, -mp.mpf(5)/36, mp.mpf(77125)/82944, -mp.mpf(108056875)/6967296, mp.mpf(162375596875)/334430208]
def lam_series(k):           # -a_k from asymptotics (mp)
    t = 3*mp.pi/8*(4*k-1)
    return t**(mp.mpf(2)/3)*sum(c*t**(-2*i) for i, c in enumerate(TC))
def zeros(K, kexact=40):
    mp.mp.dps = 30
    out = np.empty(K)
    for k in range(1, kexact+1): out[k-1] = float(-mp.airyaizero(k))
    k = np.arange(kexact+1, K+1, dtype=np.float64)
    t = 3*np.pi/8*(4*k-1)
    out[kexact:] = t**(2/3)*(1 + 5/48*t**-2 - 5/36*t**-4 + 77125/82944*t**-6 - 108056875/6967296*t**-8)
    return out
if __name__ == "__main__":
    mp.mp.dps = 30
    for k in (5, 10, 20, 41, 80):
        print(k, mp.nstr(-mp.airyaizero(k) - lam_series(k), 3), mp.nstr(-mp.airyaizero(k), 20))
