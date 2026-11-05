"""JZC_W_exact §4: Refinement W' (JZC_W §1.3) in exact algebra, and its relation to the branched hard-edge companion of §2-§3.

Inputs: g(w) = A(w) + B(w) nu^2 (Theorem N.6(ii) closed forms, symbolic j; PROVED-mod-cite for integer j, continued in w), the pole term
P(q) := p R W(q) pi cot(pi q) (n/N)^p N^{-1-pq} [1 + g(q) N^{-2}], N = n + delta, W(q) = (4c)^q Gamma(q+1/2)/(sqrt(pi) Gamma(q+1)).
Asserted (identities in p, nu, delta, R, c unless stated):
  (1) Res_{w=1/2} g = -(p+2)^2 (p+4)(1-4nu^2)/(256 p); g has no other pole in w.
  (2) the n^{-3-pq} coefficient of P(q) (natural-index shift terms included) tends, as q -> 1/2, to
      R W(1/2) pi^2 (p+2)^2 (p+4)(1-4nu^2)/256   [W' closed form, CONFIRMED exactly], = (3 pi^2/8)(1-4nu^2) R at p = 2, c = c(2) = pi^2/16;
      the shift terms contribute 0 in the limit; the limit is two-sided (cot(pi q) g(q) is analytic at 1/2): values at 1/2 +- 1e-15
      agree to 1e-14 relative (mpmath, 40 digits); JZC_W §3 item 9's numbers -0.2313188 (R = -1/16, nu = 0) and -0.1734891 (nu = 1/4).
  (3) W' = the q0 = 1/2 member of the "half-integer ladder": with H(rho) the hard-edge branched coefficient (w_exact_predict.py),
      -pi^2 p R W(q0) Res_{q0}(G_{2q0+2}/G_1) = 2 pi^2 R W(q0) Res_{q0}H / q0 once Res_{q0} G_{2q0+2} = -Res_{q0} H (P0 at q0 = 1/2: an
      identity in p; P1 at q0 = 3/2: exact at five p, w_exact_poles). At q0 = 1/2 this reproduces W' exactly (identity).
  (4) A GENUINE fractional time at rho = 1/2 (not a pole term): the continued dressing g(rho) N^{-2} and the branched companion
      H N^{-2rho-1} (relative) have opposite residues, so the response carries a log: relative 2 Res_{1/2} g log N N^{-2}
      = -(p+2)^2(p+4)(1-4nu^2)/(128 p) log N N^{-2}  (exact for Laguerre, p = -1: w_exact_laguerre (D)).
  (5) Numbers for q != 1/2 (predictions of W' for pole terms, NOT tested here): q = 1/4 and q = 3/2 at p = 2, c = pi^2/16,
      nu in {0, 1/4}; and the branched companion of a genuine fractional time at rho = 1/4 (relative N^{-3/2}, ahead of W's claimed
      relative O(N^{-2})).
Controls (must fail): (2) with g's B-part only; (2) with cot -> 1/sin (pole term without the cot zero); (1) residue with (p+2)^3."""
import os, sys, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp, mpmath as mp
import w_exact_lag as L
for fn in [__file__, L.__file__]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
p, nu, de, R, c, w, e = sp.symbols('p nu delta R c w epsilon')
pp = sp.Symbol('p', positive=True)
def A(w, p): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def B(w, p): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)
g = A(w, p) + B(w, p)*nu**2
def W(q, c): return (4*c)**q*sp.gamma(q + sp.Rational(1, 2))/(sp.sqrt(sp.pi)*sp.gamma(q + 1))
h = sp.Rational(1, 2)
# (1)
resg = sp.factor(sp.cancel((w - h)*g).subs(w, h))
chk(f"(1) Res_(w=1/2) g = {resg} = -(p+2)^2(p+4)(1-4nu^2)/(256p)", sp.simplify(resg + (p + 2)**2*(p + 4)*(1 - 4*nu**2)/(256*p)) == 0)
chk("(1) g has no other pole in w (denominator in w is 2w - 1)", sp.factor(sp.denom(sp.cancel(sp.together(g)))).as_poly(w).degree() == 1)
chk("(1) control: residue with (p+2)^3", sp.simplify(resg + (p + 2)**3*(p + 4)*(1 - 4*nu**2)/(256*p)) == 0, must_fail=True)
# (2) n^{-3-pq} coefficient of P(q): (n/N)^p N^{-1-pq} = n^{-1-pq}(1 + delta/n)^{-1-p-pq}; N^{-3-pq} = n^{-3-pq}(1+...)
q = h + e
def coeff3(gfun, trig):
    shift2 = (1 + p + p*q)*(2 + p + p*q)*de**2/2               # n^{-2} relative coefficient of (1 + delta/n)^{-1-p-pq}
    return p*R*W(q, c)*sp.pi*trig*(shift2 + gfun.subs(w, q))
lim = sp.limit(sp.simplify(coeff3(g, sp.cot(sp.pi*q))), e, 0)
target = R*W(h, c)*sp.pi**2*(p + 2)**2*(p + 4)*(1 - 4*nu**2)/256
chk("(2) lim_(q->1/2) [n^{-3-pq} coefficient of the dressed pole term] = R W(1/2) pi^2 (p+2)^2(p+4)(1-4nu^2)/256  (W' closed form)",
    sp.simplify(lim - target) == 0)
lim_shift = sp.limit(sp.simplify(coeff3(sp.Integer(0), sp.cot(sp.pi*q))), e, 0)
chk("(2) the natural-index shift terms alone contribute 0 at q = 1/2", sp.simplify(lim_shift) == 0)
cp2 = sp.pi**2/16
chk("(2) p = 2, c(2) = pi^2/16: W(1/2) = 1 and the term is (3 pi^2/8)(1 - 4nu^2) R", sp.simplify(W(h, cp2) - 1) == 0 and
    sp.simplify(target.subs({p: 2, c: cp2}) - 3*sp.pi**2/8*(1 - 4*nu**2)*R) == 0)
v1 = float(target.subs({p: 2, c: cp2, R: -sp.Rational(1, 16), nu: 0})); v2 = float(target.subs({p: 2, c: cp2, R: -sp.Rational(1, 16), nu: sp.Rational(1, 4)}))
print(f"   p = 2, R = -1/16: nu = 0: {v1:.7f} (JZC_W: -0.2313188); nu = 1/4: {v2:.7f} (JZC_W: -0.1734891)")
chk("(2) JZC_W's numbers -0.2313188 and -0.1734891 reproduced (to 1e-7; JZC_W truncates 3 pi^2/128 = 0.23131885)", abs(v1 + 0.2313188) < 1e-7 and abs(v2 + 0.1734891) < 1e-7)
limB = sp.limit(sp.simplify(coeff3(B(w, p)*nu**2, sp.cot(sp.pi*q))), e, 0)
chk("(2) control: B-part of g only", sp.simplify(limB - target) == 0, must_fail=True)
fin = sp.limit(sp.simplify((q - h)*coeff3(g, 1/sp.sin(sp.pi*q))), e, 0)
chk("(2) control: cot -> 1/sin (then the term is infinite: residue != 0)", sp.simplify(fin) == 0, must_fail=True)
# two-sided numerical
mp.mp.dps = 40
def cg(qq, pv, nv):
    qq = mp.mpf(qq)
    Av = (qq**2*(qq**2 + 2*qq - 2)*pv**3 + 2*(qq + 1)*(2*qq**2 - 1)*pv**2 + (5*qq**2 + 2*qq - 6)*pv + 2*(qq - 2))/(24*(2*qq - 1)*pv)
    Bv = (pv + 2)*(qq**2*pv**2 + (qq + 1)*pv + 2)/(8*(2*qq - 1)*pv)
    return mp.cot(mp.pi*qq)*(Av + Bv*nv**2)
lo, hi = cg(mp.mpf(1)/2 - mp.mpf(10)**-15, 2, 0), cg(mp.mpf(1)/2 + mp.mpf(10)**-15, 2, 0)
exact = -mp.pi*float(resg.subs({p: 2, nu: 0}))
print(f"   cot(pi q) g(q) at p = 2, nu = 0: q = 1/2 - 1e-15: {mp.nstr(lo, 20)}; q = 1/2 + 1e-15: {mp.nstr(hi, 20)}; -pi Res g = {mp.nstr(exact, 20)}")
chk("(2) two-sided: both one-sided values equal -pi Res g to 1e-14 relative", abs(lo/exact - 1) < 1e-14 and abs(hi/exact - 1) < 1e-14)
# (3) ladder
def ResH(r0, p): return sp.Rational(1, 2)*(p*r0 + 2*r0 + 1)*(p + 2)**(2*r0 + 1)*L.PhiC_residue(r0).subs(L.al, nu)
G1h = p*h/2
ladder_half = -sp.pi**2*p*R*W(h, c)*(-ResH(h, p))/G1h
chk("(3) q0 = 1/2 ladder term -pi^2 p R W Res(G_3/G_1) with Res G_3 = -Res H (P0) equals the W' closed form", sp.simplify(ladder_half - target) == 0)
chk("(3) P0 as an identity in p: Res_(1/2)(G_3) = (p/4) Res g = -Res_(1/2) H", sp.simplify(G1h*resg + ResH(h, p)) == 0)
t32 = sp.Rational(3, 2)
lad32 = sp.factor(2*sp.pi**2*R*W(t32, c)*ResH(t32, p)/t32)
print(f"   ladder q0 = 3/2 (n^(-2-(p+2)3/2) = n^(-5-3p/2)): coefficient = {lad32}")
print(f"     at p = 2/3 (Robin/bouncer, s = 2: nu = 1/2): {sp.simplify(lad32.subs({p: sp.Rational(2, 3), nu: h}))};  "
      f"at p = 2, nu = -1/2 (Bessel/Lommel): {sp.simplify(lad32.subs({p: 2, nu: -h}))}")
chk("(3) every ladder residue carries (nu - q0)_(2q0+1): vanishes at nu = +-1/2 for q0 = 1/2, 3/2, 5/2",
    all(sp.simplify(ResH(r0, p).subs(nu, s_)) == 0 for r0 in (h, t32, sp.Rational(5, 2)) for s_ in (h, -h)))
# (4) log coefficient for a genuine fractional time at rho = 1/2
logc = sp.factor(2*resg)
chk(f"(4) relative log N N^-2 coefficient at rho = 1/2: 2 Res g = {logc}", sp.simplify(logc + (p + 2)**2*(p + 4)*(1 - 4*nu**2)/(128*p)) == 0)
chk("(4) p = -1 value equals the Laguerre slope 2r/G_1 used in w_exact_laguerre (D): 2 Res g(p=-1) = 3(1-4nu^2)/128",
    sp.simplify(logc.subs(p, -1) - 3*(1 - 4*nu**2)/128) == 0)
# (5) numbers
print("   (5) W' predictions for pole terms, p = 2, c = pi^2/16 (coefficient of n^{-3-pq} per unit R, from p W(q) pi cot(pi q) g(q)):")
for qv in (sp.Rational(1, 4), sp.Rational(3, 4), sp.Rational(3, 2)):
    for nv in (0, sp.Rational(1, 4)):
        val = 2*W(qv, cp2)*sp.pi*sp.cot(sp.pi*qv)*g.subs({w: qv, p: 2, nu: nv})
        print(f"     q = {qv}, nu = {nv}: g(q) = {sp.nsimplify(g.subs({w: qv, p: 2, nu: nv}))}, coefficient/R = {float(val):+.7f}")
print("   (5) branched companion of a genuine fractional time, p = 2, c = pi^2/16: relative coefficient H(rho)/(p rho/2) of N^{-2rho-1}:")
mp.mp.dps = 30
for rv in (mp.mpf(1)/4, mp.mpf(2)/3, mp.mpf(4)/3):
    for nv in (mp.mpf(0), mp.mpf(1)/4, -mp.mpf(1)/3):
        Hc = (2*rv + 2*rv + 1)/2*mp.mpf(4)**(2*rv + 1)*mp.gamma(-1 - 2*rv)*mp.gamma(nv + rv + 1)*mp.rgamma(-rv)**2*mp.rgamma(nv - rv)\
             /(mp.gamma(2*rv + 1)/mp.gamma(rv + 1)**2)
        print(f"     rho = {mp.nstr(rv, 4)}, nu = {mp.nstr(nv, 4)}: H/(p rho/2) = {mp.nstr(Hc/rv, 8)}  (relative; c-free under z -> z/c; at N^-{mp.nstr(2*rv + 1, 4)})")
print(f"total {NCHK} checks")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
