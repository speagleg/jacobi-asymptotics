"""JZC_W test spectra: node arrays, masses, continuum tails, and the spectral data of Conjecture W (Z(0), Z(-j), poles, mass
tilt), each computed from the spectrum's own definition (never from b_n).

Families (K = 100 nmax atoms for p > 1, 200 nmax for p < 1, as in SPEC):
  A  perturbed lattice  lam_k = k^p + a k^{p-1}  (k >= 1, |a| < 1), masses lam^{-s/p}.
     Z(-w) = sum_{i>=0} binom(w, i) a^i zeta(i - p w)  (exact; converges for |a| < 1 since (1 + a/k)^w = sum binom(w,i)(a/k)^i).
     Non-Weyl poles q_i = (i - 1)/p (i >= 2), R_{q_i} = -binom(q_i, i) a^i / p (zero when q_i in {0..i-1}); Z(0) = -1/2 - a/p.
  M1 sphere-like  nodes lam_l = l(l+1) (l >= 1), multiplicity 2l + 1: masses (2l+1) lam^{-s/2}, node exponent p = 2.
     Z(-w) = sum_i binom(w, i) (-1/4)^i zeta(2i - 2w, 3/2); poles q = i - 1/2, R = -binom(q, i)(-1/4)^i/2; Z(0) = zeta(0, 3/2) = -1.
     Mass factor 2l + 1 = 2 lam^{1/2} (1 + x/4)^{1/2}: tau = 1/2 (s_eff = s - 1), tilt (1/2) log(1 + x/4).
  M2 multiplicity lattice  nodes l^{3/2}, multiplicity 2l + 1: mass factor 2 lam^{2/3}(1 + x^{2/3}/2): s_eff = s - 1,
     tilt log(1 + x^{2/3}/2); Z = zeta(3w/2), no non-Weyl poles, Z(0) = -1/2.
  B  Bessel zeros  lam_k = (j_{nu,k}/pi)^P, masses lam^{-s/P}.  j_{nu,k} for k <= K0 = 300 from mpmath.besseljzero (30 digits);
     beyond, McMahon's expansion (DLMF 10.21.19, NOT QUOTED under Rule C: the DLMF page truncates before 10.21(vi) under our
     fetcher), five terms, checked against besseljzero below (NUMERICAL):
       j ~ A - (m-1)/(8A) - 4(m-1)(7m-31)/(3(8A)^3) - 32(m-1)(83m^2-982m+3779)/(15(8A)^5)
             - 64(m-1)(6949m^3-153855m^2+1585743m-6277237)/(105(8A)^7),   A = (k + nu/2 - 1/4) pi,  m = 4 nu^2.
     So t := j/pi = k'(1 + e1 k'^-2 + ... + e4 k'^-8), k' = k + nu/2 - 1/4.  Z(-w) = sum_{k<=K0} t_k^{Pw}
     + sum_{i<=4} C_i(w) zeta(2i - Pw, K0 + a), a = 3/4 + nu/2, (1 + e1 u + ...)^{Pw} = sum C_i(w) u^i (Hurwitz regularisation,
     SPEC §0); poles q = (2i - 1)/P with R = -C_i(q)/P; Z(0) = zeta(0, a) = -1/4 - nu/2."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import json, numpy as np, mpmath as mp
from w_common import WC, NMAX

mp.mp.dps = 40
H = mp.mpf(10)**-15


def sym(f, w):
    """value (finite part) of an analytic (or simple-pole) function at w by the symmetric average f(w+h), f(w-h)"""
    return (f(w + H) + f(w - H))/2


# ---------------------------------------------------------------- family A ----------------------------------------------------
def famA(p, a, s):
    p, a = mp.mpf(p), mp.mpf(a)
    def Zm(w, imax=320):          # Z(-w)
        return sum(mp.binomial(w, i)*a**i*mp.zeta(i - p*w) for i in range(imax))
    spec = dict(name=f"A p={float(p)} a={float(a)} s={s}", tag=f"wA_p{float(p)}_a{float(a)}_s{s}", p=float(p), s=s, s_eff=s,
                Z0=-mp.mpf(1)/2 - a/p, poles=[], vtilt={})
    spec['Z0_direct'] = sym(Zm, mp.mpf(0))
    spec['Zneg'] = {j: sym(Zm, mp.mpf(j)) for j in range(1, 8) if 1 + j*float(p) <= 5.2}
    for i in range(2, 9):
        q = (i - 1)/p
        if 1 + p*q > 6.2: break
        spec['poles'].append((q, -mp.binomial(q, i)*a**i/p))
    spec['pole_check'] = [(q, R, (mp.mpf(10)**-12)*Zm(q + mp.mpf(10)**-12)) for q, R in spec['poles'][:2]]
    K = (200 if p < 1 else 100)*NMAX; k = np.arange(1, K + 2, dtype=np.float64)
    lam = k**float(p) + float(a)*k**(float(p) - 1)
    T0 = (lam[K - 1]**(1/float(p)) + lam[K]**(1/float(p)))/2
    return spec, lam[:K], lam[:K]**(-s/float(p)), [(float(T0), 1.0, float(s))]


# ---------------------------------------------------------------- M1 sphere ---------------------------------------------------
def sphere(s):
    p = mp.mpf(2); a = mp.mpf(3)/2
    def Zm(w, imax=80): return sum(mp.binomial(w, i)*(-mp.mpf(1)/4)**i*mp.zeta(2*i - 2*w, a) for i in range(imax))
    spec = dict(name=f"M1 sphere l(l+1), mult 2l+1, s={s}", tag=f"wM1_s{s}", p=2.0, s=s, s_eff=s - 1, Z0=mp.zeta(0, a), poles=[],
                vtilt={float(m): mp.mpf(1)/2*(-1)**(m + 1)*mp.mpf(4)**(-m)/m for m in range(1, 6)})
    spec['Z0_direct'] = sym(Zm, mp.mpf(0))
    spec['Zneg'] = {j: sym(Zm, mp.mpf(j)) for j in range(1, 3)}
    for i in range(1, 5):
        q = i - mp.mpf(1)/2; spec['poles'].append((q, -mp.binomial(q, i)*(-mp.mpf(1)/4)**i/2))
    spec['pole_check'] = [(q, R, (mp.mpf(10)**-12)*Zm(q + mp.mpf(10)**-12)) for q, R in spec['poles'][:2]]
    K = 100*NMAX; l = np.arange(1, K + 1, dtype=np.float64); lam = l*(l + 1)
    T0 = np.sqrt((K + 0.5)*(K + 1.5))
    return spec, lam, (2*l + 1)*lam**(-s/2), [(float(T0), 2.0, float(s - 1))]


# ---------------------------------------------------------------- M2 multiplicity lattice --------------------------------------
def multlat(s, p=1.5):
    P = mp.mpf(p)
    spec = dict(name=f"M2 nodes l^{p}, mult 2l+1, s={s}", tag=f"wM2_p{p}_s{s}", p=p, s=s, s_eff=s - 1, Z0=mp.zeta(0), poles=[],
                vtilt={round(m/p, 9): (-1)**(m + 1)*(mp.mpf(1)/2)**m/m for m in range(1, 8)})
    spec['Z0_direct'] = mp.zeta(0)
    spec['Zneg'] = {j: mp.zeta(-j*P) for j in range(1, 6) if 1 + j*p <= 5.2}
    K = 100*NMAX; l = np.arange(1, K + 1, dtype=np.float64); lam = l**p
    return spec, lam, (2*l + 1)*l**(-float(s)), [(K + 0.5, 2.0, float(s - 1)), (K + 0.5, 1.0, float(s))]


# ---------------------------------------------------------------- B Bessel zeros -----------------------------------------------
def mcmahon_e(nu):
    m = 4*mp.mpf(nu)**2; pi = mp.pi
    c = [-(m - 1)/8, -4*(m - 1)*(7*m - 31)/(3*8**3), -32*(m - 1)*(83*m**2 - 982*m + 3779)/(15*8**5),
         -64*(m - 1)*(6949*m**3 - 153855*m**2 + 1585743*m - 6277237)/(105*8**7)]
    return [c[i]/pi**(2*i + 2) for i in range(4)]          # j/pi = k' + sum_i c_i/(pi^{2i+2} k'^{2i+1}) = k'(1 + sum e_i k'^{-2i-2})


def bessel_zeros(nu, K0=300):
    f = WC / f"besselzeros_nu{nu}_K{K0}.json"
    if f.exists(): return [mp.mpf(x) for x in json.load(open(f))]
    with mp.workdps(32):
        z = [mp.besseljzero(mp.mpf(nu), k) for k in range(1, K0 + 1)]
    json.dump([mp.nstr(x, 32) for x in z], open(f, 'w')); return z


def Cser(e, w, P):
    """C_i(w), i = 0..4: (1 + e1 u + e2 u^2 + e3 u^3 + e4 u^4)^{P w} as a power series in u"""
    L = [mp.mpf(0)]*5; base = [mp.mpf(0)] + list(e)          # log(1 + B), B = sum e_i u^i
    pw = base[:]; k = 1
    while k <= 4:
        for i in range(5): L[i] += (-1)**(k + 1)*pw[i]/k
        pw = [sum(pw[a]*base[i - a] for a in range(i + 1)) for i in range(5)]; k += 1
    E = [mp.mpf(1)] + [mp.mpf(0)]*4; term = E[:]            # exp(P w L)
    for k in range(1, 5):
        term = [sum(term[a]*L[i - a] for a in range(i + 1))*P*w/k for i in range(5)]
        E = [E[i] + term[i] for i in range(5)]
    return E


def bessel(nu, P, s, K0=300):
    P = mp.mpf(P); nu_ = mp.mpf(nu); a = mp.mpf(3)/4 + nu_/2; e = mcmahon_e(nu_)
    z = bessel_zeros(nu, K0); t = [x/mp.pi for x in z]
    def Zm(w):
        return sum(tk**(P*w) for tk in t) + sum(Cser(e, w, P)[i]*mp.zeta(2*i - P*w, K0 + a) for i in range(5))
    spec = dict(name=f"B Bessel nu={nu} P={float(P)} s={s}", tag=f"wB_nu{nu}_P{float(P)}_s{s}", p=float(P), s=s, s_eff=s,
                Z0=mp.zeta(0, a), poles=[], vtilt={})
    spec['Z0_direct'] = sym(Zm, mp.mpf(0))
    spec['Zneg'] = {j: sym(Zm, mp.mpf(j)) for j in range(1, 4) if 1 + j*float(P) <= 5.2}
    for i in range(1, 5):
        q = (2*i - 1)/P; spec['poles'].append((q, -Cser(e, q, P)[i]/P))
    spec['pole_check'] = [(q, R, (mp.mpf(10)**-12)*Zm(q + mp.mpf(10)**-12)) for q, R in spec['poles'][:1]]
    # McMahon check against besseljzero (NUMERICAL) at k = 150..300
    def mcm(k):
        kp = k + nu_/2 - mp.mpf(1)/4; return kp*(1 + sum(e[i]*kp**(-2*i - 2) for i in range(4)))
    spec['mcmahon_check'] = max(abs(mcm(k) - t[k - 1])/t[k - 1] for k in range(150, K0 + 1))
    K = 100*NMAX if P > 1 else 200*NMAX
    k = np.arange(1, K + 2, dtype=np.float64); kp = k + float(nu)/2 - 0.25; ef = [float(x) for x in e]
    tt = kp*(1 + ef[0]*kp**-2 + ef[1]*kp**-4 + ef[2]*kp**-6 + ef[3]*kp**-8)
    tt[:K0] = np.array([float(x) for x in t])
    lam = tt**float(P); T0 = (tt[K - 1] + tt[K])/2
    return spec, lam[:K], lam[:K]**(-s/float(P)), [(float(T0), 1.0, float(s))]


SPECTRA = {
    'A15m': lambda: famA(1.5, -0.75, 2.0), 'A15p': lambda: famA(1.5, 0.6, 2.0), 'A3': lambda: famA(3.0, -0.6, 2.0),
    'A06': lambda: famA(0.6, -0.3, 2.0),
    'M1': lambda: sphere(4.0), 'M2': lambda: multlat(3.0),
    'B0_15': lambda: bessel(0, 1.5, 2.0), 'B1_15': lambda: bessel(1, 1.5, 2.0), 'B0_3': lambda: bessel(0, 3, 2.0),
}
# coefficients tested against b_n (exponents of n^{-e} in y_n = n^p b_n/c - 1); chosen before any measure was generated
TARGETS = {'A15m': [1, 2, 2.5, 3, 3.5], 'A15p': [1, 2, 2.5, 3, 3.5], 'A3': [1, 2, 3], 'A06': [1, 1.6, 2, 2.2, 2.6, 2.8],
           'M1': [1, 2, 3, 4], 'M2': [1, 2, 2.5, 3, 3.5], 'B0_15': [1, 2, 2.5, 3, 3.5], 'B1_15': [1, 2, 2.5, 3, 3.5],
           'B0_3': [1, 2, 3]}


# ---------------------------------------------------------------- K: Hurwitz lattice plus a constant shift (probe of M1) ----------
def famK(p, d, kap, s):
    """lam_k = (k + d)^p + kap, masses lam^{-s/p}.  Z(-w) = sum_i binom(w, i) kap^i zeta(-p(w - i), 1 + d) (|kap| < (1+d)^p);
    poles q_i = i - 1/p (i >= 1; i = 1 is the moved Weyl pole of the kappa law), R = -binom(q_i, i) kap^i / p; Z(0) = -1/2 - d."""
    p, d, kap = mp.mpf(p), mp.mpf(d), mp.mpf(kap); a = 1 + d
    def Zm(w, imax=200): return sum(mp.binomial(w, i)*kap**i*mp.zeta(-p*(w - i), a) for i in range(imax))
    spec = dict(name=f"K p={float(p)} d={float(d)} kappa={float(kap)} s={s}", tag=f"wK_p{float(p)}_d{float(d)}_k{float(kap)}_s{s}",
                p=float(p), s=s, s_eff=s, Z0=-mp.mpf(1)/2 - d, poles=[], vtilt={})
    spec['Z0_direct'] = sym(Zm, mp.mpf(0))
    spec['Zneg'] = {j: sym(Zm, mp.mpf(j)) for j in range(1, 4) if 1 + j*float(p) <= 5.2}
    for i in range(1, 6):
        q = i - 1/p
        if kap != 0: spec['poles'].append((q, -mp.binomial(q, i)*kap**i/p))
    spec['pole_check'] = [(q, R, (mp.mpf(10)**-12)*Zm(q + mp.mpf(10)**-12)) for q, R in spec['poles'][:1]]
    K = 100*NMAX; k = np.arange(1, K + 2, dtype=np.float64)
    lam = (k + float(d))**float(p) + float(kap)
    T0 = ((lam[K - 1] - float(kap))**(1/float(p)) + (lam[K] - float(kap))**(1/float(p)))/2
    return spec, lam[:K], lam[:K]**(-s/float(p)), [(float(T0), 1.0, float(s))]


PROBE = {'H2': lambda: famK(2, 0.5, 0, 3.0), 'K2p': lambda: famK(2, 0, 0.25, 3.0), 'K2m': lambda: famK(2, 0, -0.25, 3.0)}
