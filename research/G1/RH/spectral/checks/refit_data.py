"""REFIT (research/G1/RH/spectral/REFIT.md): a corrected measure generator for the general weighted node sets of JZC_W / JZC_M4 /
SPEC (NUMERICAL tooling; nothing here is a proof).

It removes the two data defects found in JZC_W2 Rule A items 5-7 from w_common.run_measure / spec_common.run / so_coeffs.coeffs
(the Plan 62 pipeline), which all (a) represent the measure beyond the last atom by a pure-power continuum (any correction to
lam_k ~ k^p, e.g. kappa, a k^{p-1}, McMahon's terms, the multiplicity's 1, is dropped there) cut sharply at K + 1/2 (midpoint
Euler-Maclaurin defect), and (b) pass float64 atoms, masses and scipy float64 Gauss-Jacobi rules to the binary128 RKPW kernel.
Generator (extends checks/w2_data.py, which is imported, not modified):
  * atoms 1/lam(k), masses m(k) at mpmath dps 40 handed to w2_data's binary128 RKPW kernel copy as double-double pairs;
  * a C^infinity partition of unity in k on [K, K2 = 2K] exactly as w2_data (TAIL 3): atoms weighted by chi(k), the complement
    sum_k F(k)(1 - chi(k)) replaced by its integral (Poisson summation), Gauss-Legendre (MGL = 1600 nodes, Newton-refined at
    dps 40 by w2_data.gauss_jacobi_mp) on [K, K2];
  * NEW: the continuum beyond K2 integrated in u = K2/t in (0, 1] on geometric panels [r^{j+1}, r^j] (r = 1/4, MP = 64
    Gauss-Legendre nodes each; MP_PLT1 = 512 for p < 1, where p_n has ~10^2 zeros per panel there; dps 40), down to u = r^J with r^{J (sl - 1)} < 1e-38 (sl = the decay exponent of the mass
    density in t); the node positions are the exact 1/lam(t), so no expansion of lam(t) in powers of t is needed (w2_data's
    Gauss-Jacobi-in-x tail needs the density to be x^beta times a function analytic in x, true for the kappa family only);
  * y_n = n^p b_n/c - 1 kept in mpmath.
lam_t(t), m_t(t) (continuous t >= K) must be the analytic continuation of the integer-k definitions; asserted at k = K..K+3.
Validated against w2_data (TAIL 3) on the JZC_W2 case P15a (refit_validate.out)."""
import os, sys, time, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np, mpmath as mp
import w2_data as W2D
from so_coeffs import c_p_mp
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
RC = os.path.join(ROOT, 'tmp', 'refit'); os.makedirs(RC, exist_ok=True)
W2D.W2C = RC                       # Gauss rules and the compiled kernel are cached under tmp/refit (w2_data reads W2C at call time)
mp.mp.dps = 40
MGL, MP, R = 1600, 64, mp.mpf(1)/4
MP_PLT1 = int(os.environ.get('REFIT_MP_PLT1', '512'))


def _gl(n):
    return W2D.gauss_jacobi_mp(n, 0, 0)


def data(tag, p, lam_k, m_k, lam_t, m_t, sl, K, nmax=1600, verbose=True):
    """returns (n, y): n = 1..nmax (numpy), y list of mpf; cache tmp/refit/<tag>__<key>.txt (columns k, alpha_k, beta_k).
    lam_k, m_k: integer k >= 1 -> mpf; lam_t, m_t: real t >= K -> mpf; sl: m_t(t) ~ t^-sl (sl > 1)."""
    P = mp.mpf(p); MPp = MP if p > 1 else MP_PLT1          # p < 1: hundreds of zeros of p_n lie in the far tail (REFIT.md §1)
    key = hashlib.sha256(repr((tag, str(p), K, nmax, MGL, MPp, str(R), W2D.CSRC, 'refit-v1')).encode()).hexdigest()[:16]
    fn = os.path.join(RC, f"{tag}__{key}.txt")
    if not os.path.exists(fn):
        t0 = time.time(); K2 = 2*K
        with mp.workdps(40):
            for k in range(K, K + 4):
                assert abs(lam_t(mp.mpf(k))/lam_k(k) - 1) < mp.mpf(10)**-30 and abs(m_t(mp.mpf(k))/m_k(k) - 1) < mp.mpf(10)**-30, k
            Sf = lambda u: mp.exp(-1/u)/(mp.exp(-1/u) + mp.exp(-1/(1 - u))) if 0 < u < 1 else (mp.mpf(0) if u <= 0 else mp.mpf(1))
            recs = []
            for k in range(1, K2):
                chi = 1 - Sf(mp.mpf(k - K)/(K2 - K)) if k > K else 1
                if chi > 0:
                    lam = lam_k(k); recs.append((1/lam, m_k(k)*chi))
            gx, gw = _gl(MGL)
            for xi, wi in zip(gx, gw):
                t = K + (K2 - K)*(1 + xi)/2
                recs.append((1/lam_t(t), m_t(t)*Sf((t - K)/(K2 - K))*wi*(K2 - K)/2))
            ux, uw = _gl(MPp)
            J = int(mp.ceil(38/((sl - 1)*mp.log10(1/R)))) + 1
            for j in range(J):
                b, a = R**j, R**(j + 1)
                for xi, wi in zip(ux, uw):
                    u = a + (b - a)*(1 + xi)/2; t = K2/u
                    recs.append((1/lam_t(t), m_t(t)*K2/u**2*wi*(b - a)/2))
            recs.sort(key=lambda r: -r[0])
            assert all(r[1] > 0 for r in recs)
            arr = np.array([W2D.dd(x) + W2D.dd(w) for x, w in recs], dtype='<f8')
        fin = fn + '.bin'; arr.tofile(fin)
        import subprocess
        subprocess.run([W2D.kernel(), fin, str(nmax + 2), fn + '.tmp'], check=True); os.remove(fin); os.replace(fn + '.tmp', fn)
        if verbose: print(f"   [refit data {os.path.basename(fn)}: {len(recs)} records, {time.time() - t0:.0f}s]", flush=True)
    rows = [l.split() for l in open(fn)]
    with mp.workdps(40):
        c = mp.mpf(c_p_mp(P))
        b = [mp.sqrt(mp.mpf(r[2])) for r in rows[1:nmax + 1]]
        y = [mp.mpf(k)**P*b[k - 1]/c - 1 for k in range(1, nmax + 1)]
    return np.arange(1, nmax + 1), y


# ------------------------------------------------------------------ the families (exact definitions, dps 40) -----------------------
def fam_kappa(p, d, kap, s):
    """lam = (k + d)^p + kap, masses lam^{-s/p} (w_spectra.famK, JZC_W2, w_outer_e2e)"""
    P, D, Kp, S = (mp.mpf(x) for x in (p, d, kap, s))
    lam = lambda t: (t + D)**P + Kp; m = lambda t: lam(t)**(-S/P)
    return lam, m, lam, m, float(s)


def fam_A(p, a, s):
    """lam = k^p + a k^{p-1}, masses lam^{-s/p} (w_spectra.famA)"""
    P, A, S = (mp.mpf(x) for x in (p, a, s))
    lam = lambda t: t**P + A*t**(P - 1); m = lambda t: lam(t)**(-S/P)
    return lam, m, lam, m, float(s)


def fam_M1(s):
    """lam = l(l+1), mass (2l+1) lam^{-s/2} (w_spectra.sphere)"""
    S = mp.mpf(s)
    lam = lambda t: mp.mpf(t)*(t + 1); m = lambda t: (2*t + 1)*lam(t)**(-S/2)     # mpf: an int k would make 1/lam a float64
    return lam, m, lam, m, float(s) - 1


def fam_M2(s, p=1.5):
    """lam = l^p, mass (2l+1) l^{-s} (w_spectra.multlat)"""
    P, S = mp.mpf(p), mp.mpf(s)
    lam = lambda t: t**P; m = lambda t: (2*t + 1)*t**(-S)
    return lam, m, lam, m, float(s) - 1


def fam_bessel(nu, Pw, s, K0=300):
    """lam = (j_{nu,k}/pi)^P, masses lam^{-s/P}: k <= K0 from mpmath.besseljzero (w_spectra's 30-digit cache, recomputed here at
    dps 40), beyond from McMahon's five terms (as w_spectra.bessel; relative truncation ~k^-11 < 1e-26 at k > 300)"""
    import w_spectra as WS
    nu_, P, S = mp.mpf(nu), mp.mpf(Pw), mp.mpf(s)
    zf = os.path.join(RC, f"besselzeros40_nu{nu}_K{K0}.txt")
    if not os.path.exists(zf):
        with mp.workdps(45):
            z = [mp.besseljzero(nu_, k) for k in range(1, K0 + 1)]
        open(zf, 'w').write("\n".join(mp.nstr(x, 42) for x in z))
    z = [mp.mpf(l) for l in open(zf).read().split()]
    e = WS.mcmahon_e(nu_)
    def tt(t):
        kp = t + nu_/2 - mp.mpf(1)/4; return kp*(1 + sum(e[i]*kp**(-2*i - 2) for i in range(4)))
    lam_t = lambda t: tt(t)**P
    lam_k = lambda k: (z[k - 1]/mp.pi)**P if k <= K0 else lam_t(mp.mpf(k))
    m_t = lambda t: lam_t(t)**(-S/P); m_k = lambda k: lam_k(k)**(-S/P)
    return lam_k, m_k, lam_t, m_t, float(s)


def fam_hurwitz(p, s, delta=0):
    """lam = (k + delta)^p, masses (k + delta)^{-s} (so_coeffs.coeffs, the Plan 62 lattices)"""
    P, S, D = mp.mpf(p), mp.mpf(s), mp.mpf(delta)
    lam = lambda t: (t + D)**P; m = lambda t: (t + D)**(-S)
    return lam, m, lam, m, float(s)


def run(tag, p, fam, K, nmax=1600):
    lk, mk, lt, mt, sl = fam
    return data(tag, p, lk, mk, lt, mt, sl, K, nmax)
