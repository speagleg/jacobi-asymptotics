"""JZC_W_exact §3 (Rule X): PRE-REGISTERED predictions for the general-p exact engine run (w_exact_poles.py), written BEFORE that
run. Inputs: only (a) the closed forms A_j, B_j of Theorem N.6(ii) (JZC_M4 §6) and (b) the hard-edge branched coefficient
    H(rho) := (1/2)(p rho + 2 rho + 1) kappa^{-rho-1/2} Phi_nu(rho)/C(2rho,rho),  kappa = 1/(p+2)^2 (c = 1),
    Phi_nu(rho) = Gamma(-1-2rho) Gamma(nu+rho+1)/(Gamma(-rho)^2 Gamma(nu-rho))      (regularised Mellin moment of J_nu(2 sqrt y)^2),
derived from the Bessel hard-edge profile n sqrt(kappa) J_nu(2 n sqrt(kappa z))^2 of p_n^2 w (HEURISTIC universality argument,
JZC_W_exact §2.3) and checked EXACTLY only at p = -1 (Laguerre, w_exact_laguerre.out). Here H is the coefficient of
n^{-2rho-2} in the response (per mu C(2rho,rho)) of n^p b_n/c to exp(-mu z^rho); relative to the leading p rho/2 n^{-1} it sits at
relative order N^{-2rho-1}.
Mechanism to be tested: the engine's continued (symbolic-j) response has poles at half-integer j; the true response to a tilt
z^rho is finite there, so the branched series must cancel them. Predictions (identities in nu at each fixed p):
  P0  Res_{j=1/2} g1[3] = -Res_{rho=1/2} H                    (N^{-3}: relative N^{-2}; already an identity in p, w_exact_wprime)
  P1  Res_{j=3/2} g1[5] = -Res_{rho=3/2} H                    (N^{-5}: relative N^{-4}; leading branched term at rho = 3/2)
  P2  Res_{j=1/2} g1[5] = -Res_{rho=1/2} [H(rho) g(rho*)],  rho* := rho + (2rho+1)/p, g(w) = A(w) + B(w) nu^2
      (CONJECTURE "reflection": the branched series is H N^{-2rho-2}(1 + g(rho*) N^{-2} + ...), i.e. the analytic response at the
      exponent rho* with p rho* = p rho + 2rho + 1; at p = -1, rho* = -1-rho, which is exact for Laguerre (w_exact_laguerre))
  P3  g1[4] = 0 identically in (nu, j) (natural form: no N^{-4-jp} term), and g1[5] has no pole at j = 1/2, 3/2 other than simple.
g1[k] is the engine's natural-form coefficient of N^{-k} of (N/n)^{(j+1)p} x response, mu normalised by C(2j, j) (m4_rh_exact2)."""
import os, sys, json, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import w_exact_lag as L

for fn in [__file__, L.__file__]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}")
nu, j = L.al, sp.Symbol('j')
PS = [sp.Rational(3, 2), sp.Integer(2), sp.Integer(3), sp.Rational(1, 2), sp.Rational(5, 2)]
def A(w, p): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def B(w, p): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)
def ResH(r0, p): return sp.factor(sp.Rational(1, 2)*(p*r0 + 2*r0 + 1)*(p + 2)**(2*r0 + 1)*L.PhiC_residue(r0))
pred = {"written": time.strftime("%Y-%m-%d %H:%M:%S"), "unix": time.time(), "p": {}}
for p in PS:
    h = sp.Rational(1, 2); rs = h + (2*h + 1)/p
    P0 = sp.factor(-ResH(h, p)); P1 = sp.factor(-ResH(sp.Rational(3, 2), p))
    P2 = sp.factor(-ResH(h, p)*(A(rs, p) + B(rs, p)*nu**2))
    pred["p"][str(p)] = {"P0": str(P0), "P1": str(P1), "P2": str(P2)}
    print(f"p = {p}:\n  P0 Res_(j=1/2) g1[3] = {P0}\n  P1 Res_(j=3/2) g1[5] = {P1}\n  P2 Res_(j=1/2) g1[5] = {P2}  (rho* = {rs})")
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "w_exact_predictions.json")
# Registration guard (2026-11-05, adversarial review): a registration is never rewritten. To re-register on purpose, set
# W_REREGISTER=1 and commit the new json BEFORE running the test, so git (not mtimes) orders prediction and test.
if os.path.exists(out) and os.environ.get("W_REREGISTER") != "1":
    print("w_exact_predictions.json exists: registration is never rewritten (set W_REREGISTER=1 to override)"); sys.exit(0)
json.dump(pred, open(out, "w"), indent=1)
print(f"predictions written {pred['written']} -> {os.path.basename(out)}")
