"""SPEC §3.17 probe: hearing corners and perimeter from b_n (p = 1, s = 2; outside the proved framework, which excludes p = 1).
Dirichlet drums, eigenvalues rescaled to unit Weyl density, lam~ = A lam/(4 pi):  N(lam~) = lam~ - beta sqrt(lam~) + c0 + fluct.,
beta = L/sqrt(4 pi A) (perimeter), c0 = Z(0) (corners/curvature):
  square (side 1):       lam = pi^2 (a^2 + b^2), a, b >= 1;                      beta = 2/sqrt(pi),          c0 = 1/4
  equilateral triangle:  lam = (16 pi^2/9)(m^2 + mn + n^2), m, n >= 1 (ordered);  beta = 3/sqrt(pi sqrt 3),  c0 = 1/3
  (disk, for the smoothed family only: beta = 1, c0 = 1/6)
"smooth_X": the regular node set with the same beta, c0 and no fluctuations: N_s(lam_k) = k - 1/2 - c0, N_s(l) := l - beta sqrt(l)
  (then Z(0) = c0, and the perimeter is a pole of Z(-w) at w = -1/2).
Predictions (Principle E / S1 with p = 1):  D := n (y - y_lattice) -> Z(0) - zeta(0) = c0 + 1/2 at order n^0;
  the perimeter pole sits at q = -1/2 where cot(pi q) = 0, so NO n^{+1/2} term in D (it would be the leading effect of a sqrt(k)
  index drift otherwise); its subleading term appears at n^{-1/2}.
  rect (1 x golden ratio): generic, simple spectrum; beta = 2(1+phi)/sqrt(4 pi phi), c0 = 1/4.
  "smooth:beta:c0": a smoothed drum with arbitrary (beta, c0) -- isolates the corner term at fixed perimeter.
Degenerate spectra (square, triangle): b_n sees DISTINCT eigenvalues only (multiplicities merge into masses), so their leading law
is set by the count of distinct eigenvalues (sums of two squares / Loeschian numbers, ~ C Q/sqrt(log Q)), not by Weyl's law.
Atoms 1/lam~ with weight (multiplicity) lam~^{-s}; continuum tail with density dN_s from Lam* where N_s(Lam*) = K (keeps Z(0) = c0)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, mpmath as mp
from numpy.polynomial.legendre import leggauss
from spec_common import NMAX, CACHE, Checks
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
import hashlib
s = 2.0; KT = 100*NMAX; c = 0.5      # c(1) = (1/4)(pi/(2 I(1))), I(1) = pi/4
PHI = (1 + 5**0.5)/2
SH = {"square": (2/np.sqrt(np.pi), 0.25), "triangle": (3/np.sqrt(np.pi*np.sqrt(3)), 1/3), "disk": (1.0, 1/6),
      "rect": (2*(1 + PHI)/np.sqrt(4*np.pi*PHI), 0.25)}
def shape(name):
    if name.startswith("smooth:"): _, b_, c_ = name.split(":"); return float(b_), float(c_)
    return SH[name.split("_")[-1]]

def spectrum(name):
    if name == "lattice": lam = np.arange(1, KT + 1, dtype=np.float64); return lam, np.ones_like(lam), 0.0
    beta, c0 = shape(name)
    if name.startswith("smooth"):
        t = np.arange(1, KT + 1, dtype=np.float64) - 0.5 - c0            # N_s(l) = t  =>  sqrt(l) = (beta + sqrt(beta^2 + 4t))/2
        return ((beta + np.sqrt(beta**2 + 4*t))/2)**2, np.ones(KT), beta
    if name == "rect":                                                    # sides 1 x PHI: generic, no degeneracies
        A = PHI; scale = np.pi**2*A/(4*np.pi); Ma = int(np.sqrt(1.05*KT/scale)) + 2; Mb = int(PHI*np.sqrt(1.05*KT/scale)) + 2
        a = np.arange(1, Ma + 1)[:, None]; b = np.arange(1, Mb + 1)[None, :]
        lam = np.sort(((a**2 + b**2/PHI**2)*scale).ravel())[:KT]; return lam, np.ones_like(lam), SH["rect"][0]
    if name == "square":
        A = 1.0; M = int(np.sqrt(4*np.pi*1.05*KT/A)/np.pi) + 2; a = np.arange(1, M + 1)
        key = (a[:, None]**2 + a[None, :]**2).ravel(); scale = np.pi**2*A/(4*np.pi)
    else:
        A = np.sqrt(3)/4; M = int(np.sqrt(9*4*np.pi*1.05*KT/A/(16*np.pi**2))) + 2; m = np.arange(1, M + 1)
        key = (m[:, None]**2 + m[:, None]*m[None, :] + m[None, :]**2).ravel(); scale = 16*np.pi**2/9*A/(4*np.pi)
    vals, mult = np.unique(key, return_counts=True); lam = vals*scale
    cum = np.cumsum(mult); sel = cum <= KT; return lam[sel], mult[sel].astype(np.float64), beta

def coeffs_of(name):
    lam, mult, beta = spectrum(name); Ktot = mult.sum()
    Ls = ((beta + np.sqrt(beta**2 + 4*Ktot))/2)**2                     # N_s(Ls) = Ktot
    h = hashlib.sha256(lam.tobytes() + mult.tobytes() + repr((s, beta, Ktot, NMAX)).encode()).hexdigest()[:16]
    f = CACHE/f"corners_{name.replace(':', '_')}__{h}.txt"
    if not f.exists():
        X = 1/Ls; g, wg = leggauss(NMAX + 8); uu = (g + 1)/2; wg = wg/2
        xt = X*uu**2; wt = wg*2*X*uu*(1 - beta*np.sqrt(X)*uu/2)        # s = 2: lam^{-2} dN = (1 - beta sqrt(x)/2) dx
        mu = DiscreteMeasure.from_atoms(1/lam, mult*lam**(-s), tail=(xt, wt))
        jc = jacobi_rkpw(mu, NMAX + 1, prec="q"); mp.mp.dps = 40
        with open(f, "w") as fh:
            for a_, b2 in zip(jc.a[:NMAX], jc.b2[:NMAX]): fh.write(f"{mp.nstr(a_, 36)} {mp.nstr(mp.sqrt(b2), 36)}\n")
    b = np.array([float(l.split()[1]) for l in open(f)]); n = np.arange(1, len(b) + 1, dtype=np.float64)
    return n, n*b/c - 1                                                  # y_n with p = 1 (b_n ~ c/n)

C_ = Checks(); Dsm = {}
n, y0 = coeffs_of("lattice")
for name in sys.argv[1:]:
    _, y = coeffs_of(name); D = n*(y - y0)
    beta, c0 = shape(name)
    pper, p0 = -np.pi*beta/(2*np.sqrt(2)), c0 + 0.5 + np.pi**2/16*beta**2
    print(f"{name}: beta = {beta:.6f}, c0 = Z(0) = {c0:.6f}; predicted n^(+1/2) coefficient of D: -pi beta/(2 sqrt 2) = {pper:+.6f}"
          f" (pole law, W cot -> -pi (4c)^(-1/2)); n^0: c0 + 1/2 + (pi^2/16) beta^2 = {p0:+.6f} (empirical beta^2 term, §3.16)")
    if name.startswith("smooth"):
        res = {}
        for lo in (100, 200, 400):
            for E in ([-0.5, 0, 0.5, 1, 1.5, 2], [-0.5, 0, 0.5, 1, 1.5], [0, 0.5, 1, 1.5, 2], [-0.5, 0, 0.5, 1, 1.5, 2, 2.5]):
                sel = n >= lo; Am = np.vstack([n[sel]**-e for e in E]).T; co = np.linalg.lstsq(Am, D[sel], rcond=None)[0]
                res.setdefault(0, []).append(co[E.index(0)])
                if -0.5 in E: res.setdefault(-0.5, []).append(co[E.index(-0.5)])
                res.setdefault(0.5, []).append(co[E.index(0.5)])
        for e, lab in ((-0.5, "n^(+1/2)"), (0, "n^0"), (0.5, "n^(-1/2)")):
            v = np.array(res[e]); print(f"   {lab:>9}: median {np.median(v):+.6f}  half-range {(v.max() - v.min())/2:.1e}")
        vp = np.array(res[-0.5]); C_.check(f"{name} perimeter n^(1/2)", float(np.median(vp)), pper, max(3*(vp.max() - vp.min())/2, 2e-5))
        C_.check(f"{name} n^0 (median; single fits unstable)", float(np.median(res[0])), p0, 2e-3)
        Dsm[name] = D
    else:
        for lo in (100, 200, 400, 800):
            sel = (n >= lo) & (n < 2*lo)
            print(f"   n in [{lo},{2*lo}): mean D {np.mean(D[sel]):+.4f}   RMS D {np.sqrt(np.mean(D[sel]**2)):.4f}   std D {np.std(D[sel]):.4f}")
if "smooth_square" in Dsm and "smooth:1.128379:0.333333" in Dsm:     # corners at fixed perimeter: Delta c0 = 1/12
    d = Dsm["smooth:1.128379:0.333333"] - Dsm["smooth_square"]; v = []
    for lo in (100, 400):
        for E in ([0, 0.5, 1], [0, 0.5, 1, 1.5], [0, 0.5, 1, 1.5, 2]):
            sel = n >= lo; Am = np.vstack([n[sel]**-e for e in E]).T; v.append(np.linalg.lstsq(Am, d[sel], rcond=None)[0][0])
    v = np.array(v); print(f"corner difference at fixed beta: n^0 coefficient {np.median(v):+.7f} (half-range {(v.max() - v.min())/2:.1e}); predicted 1/12 = {1/12:.7f}")
    C_.check("corners at fixed perimeter", float(np.median(v)), 1/12, max(3*(v.max() - v.min())/2, 5e-5))
C_.finish() if C_.n else None
