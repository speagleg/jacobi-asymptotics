"""Theorem H, gap G5 (JZC_M3a_H.md): the decoupled model M(beta, nu) in exact arithmetic over Q(p, alpha, j, beta)[i]
(m4_rh_exact2 with DECOUPLE=1: alpha = Bessel order nu, beta = Szego exponent), first order in mu_j for integer j = 1, 2, 3
and for SYMBOLIC j (KORD = 4). Asserted identically in (p, alpha, beta[, j]): in the natural form N = n + (beta+1)/2, the
response (N/n)^{(j+1)p} sum_k e_k n^{-k} has vanishing N^{-jp} coefficient, leading coefficient C(2j,j) p j/2 (symbolic j: mu
normalised by C(2j, j), so p j/2), vanishing N^{-2-jp} and N^{-4-jp} coefficients, and N^{-3-jp}/N^{-1-jp} = A_j + B_j alpha^2
-- i.e. the zeta layer depends on beta only through N (Prop S for the zeta layer, exact), with the lattice dressings g_j
evaluated at the Bessel order. Also asserts the integer layer f_1..f_4 is beta-free.
Controls (must fail, asserted to fail; added per Rule R review B, REVIEW_JZC_M3a_H_assembly_B.md B-1): the same raw
coefficients re-expanded (i) in the wrong index N' = n + (alpha+1)/2 (Bessel order in the index) and N' = n: the integer layer
then has f_1 != 0 (f_1 = p(alpha - beta)/2 resp. -p(beta+1)/2) and is beta-dependent; (ii) the zeta layer with the prefactor
(N/n)^p instead of (N/n)^{(j+1)p}: N^{-2-jp} != 0 (beta-dependent); (iii) the zeta layer in N' = n + (alpha+1)/2: the
natural-form identities (N^{-2-jp} = 0 and N^{-3-jp}/N^{-1-jp} = A_j + B_j alpha^2) fail. The raw 1/n coefficients of the zeta
layer are recovered exactly from the engine's natural-form output (inverse re-expansion; asserted to round-trip, and the
helper is asserted to reproduce the engine's f from its raw d)."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ["DECOUPLE"] = "1"; os.environ.setdefault("EO", "1"); os.environ.setdefault("KORD", "4"); os.environ.setdefault("SHI", "14")
import m4_rh_exact2 as X
from sympy import binomial, Symbol
K, p, al, be, jj, ZERO = X.K, X.p, X.al, X.be, X.jj, X.ZERO
KORD = X.KORD
X._provenance(__file__, X)
A = lambda j: (j**2*(j**2 + 2*j - 2)*p**3 + 2*(j + 1)*(2*j**2 - 1)*p**2 + (5*j**2 + 2*j - 6)*p + 2*(j - 2))/(24*(2*j - 1)*p)
B = lambda j: (p + 2)*(j**2*p**2 + (j + 1)*p + 2)/(8*(2*j - 1)*p)
f4 = ((p + 1)*(6*p**3 + 46*p**2 + 55*p + 3)/(1440*p*(3*p + 2)) - 5*(p + 1)*(p + 2)*al**2/(96*(3*p + 2))
      - p*(p + 2)**2*al**4/(128*(3*p + 2)))
BS = Symbol('beta')
ok = True; NID = 0; NCTL = 0
def chk(lab, v):
    """identity: v must be the zero of the field"""
    global ok, NID
    z = (v == ZERO); ok &= z; NID += 1; print(f"{lab} identically: {z}", flush=True)
def ctl(lab, holds):
    """control: the identity `holds` must be False"""
    global ok, NCTL
    ok &= (not holds); NCTL += 1
    print(f"CONTROL (must fail) {lab}: {'holds -> FAIL' if holds else 'fails -> PASS'}", flush=True)
def bdep(v): return v.as_expr().has(BS)

# ---- exact re-expansion between 1/n and 1/N (same series algebra as the engine's extraction) ----
def _ser(cs): return X.S(0, [X.G(v) for v in cs], KORD)
def to_N(raw, dl, a):
    """coefficients in 1/N, N = n + dl, of (N/n)^a sum_k raw_k n^{-k}"""
    hi0 = X.S.HI; X.S.HI = KORD
    one = X.S.const(1); x = X.S(1, [X.G1]); y = x*(one - x*X.G(dl)).inv()
    tot = X.S.const(X.G(raw[0])); q = X.S.const(1)
    for k in range(1, KORD + 1): q = q*y; tot = tot + q*X.G(raw[k])
    F = (one - x*X.G(dl)).powr1(-a)*tot
    out = [F.get(k).a for k in range(KORD + 1)]; X.S.HI = hi0; return out
def to_n(c, dl, a):
    """inverse of to_N: raw_k with (N/n)^a sum raw_k n^{-k} = sum c_k N^{-k}, N = n + dl"""
    hi0 = X.S.HI; X.S.HI = KORD
    one = X.S.const(1); y = X.S(1, [X.G1]); x = y*(one + y*X.G(dl)).inv()
    tot = X.S.const(X.G(c[0])); q = X.S.const(1)
    for k in range(1, KORD + 1): q = q*x; tot = tot + q*X.G(c[k])
    R = (one + y*X.G(dl)).powr1(-a)*tot
    out = [R.get(k).a for k in range(KORD + 1)]; X.S.HI = hi0; return out

DL = be/2 + K(1)/2                 # natural index N = n + (beta+1)/2 (the engine's delta)
DL_bad = al/2 + K(1)/2             # control: Bessel order in the index
for j in (1, 2, 3, 'sym'):
    t0 = time.time(); d, f, g = X.run(verbose=False, jmu=j); g1 = g[1]
    jv = jj if j == 'sym' else K(j); lead = jv*p/2 if j == 'sym' else K(int(binomial(2*j, j)))*p*j/2
    if j == 1:
        chk("helper: to_N(raw d, (beta+1)/2, p) = engine f", ZERO if to_N(d, DL, p) == list(f) else K(1))
        chk("integer layer f1 = f3 = 0 (beta-free)", f[1]); chk("f3 = 0", f[3])
        chk("f2 = (p+1)/12 - (p+2)alpha^2/8 (beta-free)", f[2] - (p + 1)/12 + (p + 2)*al**2/8)
        chk("f4 = closed form at the Bessel order (beta-free)", f[4] - f4)
        fb = to_N(d, DL_bad, p); print(f"   control: index N' = n + (alpha+1)/2 gives f1 = {fb[1].as_expr().factor()}", flush=True)
        ctl("integer layer in N' = n + (alpha+1)/2: f1 = 0 and f1..f4 beta-free", fb[1] == ZERO and not any(bdep(v) for v in fb[1:]))
        f0 = to_N(d, ZERO, p); print(f"   control: index N' = n gives f1 = {f0[1].as_expr().factor()}", flush=True)
        ctl("integer layer in N' = n: f1 = 0 and f1..f4 beta-free", f0[1] == ZERO and not any(bdep(v) for v in f0[1:]))
    a_true = (jv + 1)*p
    e = to_n(g1, DL, a_true)
    chk(f"j={j}: helper round trip to_N(to_n(g)) = g", ZERO if to_N(e, DL, a_true) == list(g1) else K(1))
    chk(f"j={j}: N^-(jp) = 0", g1[0])
    chk(f"j={j}: lead = {'p j/2 (mu normalised by C(2j,j))' if j == 'sym' else 'C(2j,j) p j/2'}", g1[1] - lead)
    chk(f"j={j}: N^-(2+jp) = 0", g1[2])
    chk(f"j={j}: N^-(3+jp)/N^-(1+jp) = A_j + B_j alpha^2 (beta-free)", g1[3]/g1[1] - A(jv) - B(jv)*al**2)
    chk(f"j={j}: N^-(4+jp) = 0", g1[4])
    gp = to_N(e, DL, p)
    ctl(f"j={j}: zeta layer with prefactor (N/n)^p: N^-(2+jp) = 0 and beta-free", gp[2] == ZERO and not bdep(gp[3]/gp[1]))
    gb = to_N(e, DL_bad, a_true)
    ctl(f"j={j}: zeta layer in N' = n + (alpha+1)/2: N^-(2+jp) = 0 and N^-(3+jp)/N^-(1+jp) = A_j + B_j alpha^2",
        gb[2] == ZERO and gb[3]/gb[1] - A(jv) - B(jv)*al**2 == ZERO)
    print(f"   ({time.time() - t0:.0f}s)", flush=True)
print(f"{NID} identities, {NCTL} controls")
print("ALL IDENTITIES HOLD, ALL CONTROLS FAIL" if ok else "IDENTITY OR CONTROL FAILURE"); assert ok
