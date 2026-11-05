"""SPEC probe: the log resonance of the pole law. lam_k = (k + g k^{-m})^p with q = m/p = j an integer (here m = p = 1/2, j = 1).
Pole law + integer term: the divergences cancel, leaving in D := n(y - y_lat) - (other zeta-layer terms j' != j):
  p^2 j g W(j) n^{-jp} log n  +  n^{-jp} p [ W(j) Zfin - g W(j) - j g W'(j) ],
with Zfin = regularised Delta Z(-j) where the divergent zeta(1) (i = 1 term) is replaced by Euler's gamma (the finite part)."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from spec_common import run, NMAX, c_p_mp, Checks
from so_coeffs import coeffs
from so_fit import sequences
p, s, g, m = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
K = (200 if p < 1 else 100)*NMAX; k = np.arange(1, K + 1, dtype=np.float64)
n, y = run(f"pole_p{p}_s{s}_g{g}_m{m}", (k + g*k**(-m))**p, p, s, 0.0, K)
al, b = coeffs(p, s, K, NMAX); _, y0, *_ = sequences(p, al, b)
mp.mp.dps = 30; c = c_p_mp(p); pm, mm, gg = mp.mpf(p), mp.mpf(m), mp.mpf(g)
W = lambda q: (4*c)**q*mp.gamma(q + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(q + 1))
jres = int(round(m/p)); assert abs(m/p - jres) < 1e-12
def dZ(j, terms=10, kex=3000, finite=False):
    q = j*pm; tot = mp.mpf(0)
    for i in range(1, terms):
        arg = (mm + 1)*i - q
        z = mp.euler if (finite and abs(arg - 1) < 1e-20) else mp.zeta(arg)
        tot += mp.binomial(q, i)*gg**i*z
    rem = sum((mp.mpf(kk) + gg*mp.mpf(kk)**(-mm))**q - sum(mp.binomial(q, i)*gg**i*mp.mpf(kk)**(q - (mm + 1)*i) for i in range(terms)) for kk in range(1, kex + 1))
    return tot + rem
D = n*(y - y0)
def resonant(j, terms=10):
    return any(abs((mm + 1)*i - j*pm - 1) < 1e-20 for i in range(1, terms))
skipped = []
for j in range(1, int(np.ceil(2.5/p))):
    if j == jres: continue
    if resonant(j): skipped.append(j); continue          # higher-order (g^i, i >= 2) resonance: left to the fit
    D = D - float(p*W(j)*dZ(j))*n**(-j*p)
print("  other resonant j (g^2 and higher, left to the fit as n^{-jp} and n^{-jp} log n):", skipped)
logc = float(p*p*jres*gg*W(jres))
Wp = mp.diff(W, jres)
fin = float(p*(W(jres)*dZ(jres, finite=True) - gg*W(jres) - jres*gg*Wp))   # -g W: from the prefactor m = p(j + eps) of the pole term
print(f"p={p} m={m} g={g}: resonance at j = {jres} (n^-{1+jres*p} log n in b_n)")
print(f"  predicted: coefficient of n^-{jres*p} log n = {logc:+.6f};  of n^-{jres*p} = {fin:+.6f}")
E = sorted({round(e, 9) for e in [1.0, 2*p, 3*p, 1 + p, 2.0, 1 + 2*p, 4*p, 2 + p]})
for lo in (200, 400, 800):
    sel = n >= lo
    for J in (4, 5, 6):
        Ex = E[:J]
        A = np.vstack([n[sel]**(-jres*p)*np.log(n[sel]), n[sel]**(-jres*p)] + [n[sel]**(-j*p)*np.log(n[sel]) for j in skipped] + [n[sel]**-e for e in Ex]).T
        co = np.linalg.lstsq(A, D[sel], rcond=None)[0]
        if J == 5: print(f"  n >= {lo}: log coefficient {co[0]:+.6f} (pred {logc:+.6f}),  n^-{jres*p} coefficient {co[1]:+.6f} (pred {fin:+.6f})")
        if J == 5 and lo == 200: res200 = (co[0], co[1])
# control: a fit without the log term
sel = n >= 400; A = np.vstack([n[sel]**(-jres*p)] + [n[sel]**(-j*p)*np.log(n[sel]) for j in skipped] + [n[sel]**-e for e in E[:5]]).T
res = D[sel] - A @ np.linalg.lstsq(A, D[sel], rcond=None)[0]
A2 = np.vstack([n[sel]**(-jres*p)*np.log(n[sel]), n[sel]**(-jres*p)] + [n[sel]**(-j*p)*np.log(n[sel]) for j in skipped] + [n[sel]**-e for e in E[:5]]).T
res2 = D[sel] - A2 @ np.linalg.lstsq(A2, D[sel], rcond=None)[0]
print(f"  control (n >= 400): RMS residual without log term {np.sqrt(np.mean(res**2)):.2e}, with log term {np.sqrt(np.mean(res2**2)):.2e}")
# pass/fail at the n >= 200 window only (later windows are degenerate; REVIEW_SPEC2_A F6, REVIEW_SPEC2_B F5: honest spreads 1.4e-4, 1.6e-3)
C_ = Checks(); C_.check("log coefficient", res200[0], logc, 5e-4); C_.check("n^-jp coefficient", res200[1], fin, 5e-3); C_.finish()
