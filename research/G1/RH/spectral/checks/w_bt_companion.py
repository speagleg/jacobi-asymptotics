"""JZC_W_BT §3-§4: the hard-edge companion of a branched tilt, DERIVED from the lip mismatch (w_bt_core), and its exact tests.

Part (L) Laguerre anchor, p = -1, beta = nu - 1 (w_bt_engine PVAL=-1, SZOFF=-1, KORD=5): the derived companion c_k (k <= 4) equals
    the exact Laguerre branched series rat_k of JZC_W_exact §2.2 (w_exact_lag.response_B), identically in (nu, rho).
Part (P) fixed p in {1/2, 3/2, 2, 3, 5} (lattice frame beta = nu, KORD = 4; k <= 3), identically in (nu, rho):
    c_0 = (p rho + 2 rho + 1)/2  [i.e. the companion is H(rho) N^{-2rho-2}, H of JZC_W_exact Finding WE.4],  c_1 = c_3 = 0,
    the odd-shift Mellin part (K(2rho+3)) vanishes,
    c_2(1/2)/c_0(1/2) = X(p, nu) of JZC_W_exact Obs WE.6 (post hoc there; derived here),
    Res_{j=1/2} g1[5] = -Res[(p+2)^{2rho+1} Phi/C c_2] using the cached engine residues of w_exact_poles (tmp/w_exact), where present.
Part (B) decoupled beta (DECOUPLE=1) at p = 3/2, KORD = 4: c_k (k <= 3) do not depend on beta (natural index N = n + (beta+1)/2).
Part (Q) pole terms (kappa-problem structure): the lip mismatch of the composite factor exp(C(-z)^q) vanishes identically
    (tau tan(pi q) = pi sigma), so pole terms carry no companion; checked symbolically.
Controls (must fail): R_in -> I in the lip integrand (dressing wrong); K^2 moments dropped; Laguerre with sin(pi(rho+nu))
(i.e. c_k with the reflection rho -> -rho); X with the refuted P2 form g(rho*), rho* = rho + (2rho+1)/p.
Usage: python w_bt_companion.py L | P | B | Q"""
import os, sys, json, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
T0 = time.time()
part = sys.argv[1]
if part == "L": os.environ.update(PVAL="-1", SZOFF="-1", KORD="5", SHI="20"); os.environ.pop("DECOUPLE", None)
if part == "P": os.environ.update(KORD="4", SHI="18"); os.environ.pop("DECOUPLE", None); os.environ.pop("SZOFF", None)
if part == "B": os.environ.update(KORD="4", SHI="18", DECOUPLE="1", PVAL="3/2"); os.environ.pop("SZOFF", None)
import sympy as sp
import w_exact_lag as L
here = os.path.dirname(os.path.abspath(__file__))
for fn in [__file__, os.path.join(here, "w_bt_core.py"), os.path.join(here, "w_bt_engine.py"), L.__file__]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
J, nu, beta = sp.Symbol('j'), sp.Symbol('alpha'), sp.Symbol('beta')
def ex(v): return sp.factor(v.as_expr())
def badzero(r): return all(x.iszero() for e in r['lam_bad'] for row in r['lam_bad'][e] for x in row)
def Xpost(p): return ((9*p**4 + 642*p**3 + 4588*p**2 + 11000*p + 7360) + 12*(p + 2)*(5*p**3 + 24*p**2 + 44*p - 32)*nu**2)/(1536*(p + 4)*(3*p + 2))
def gA(w, p): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def gB(w, p): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)

def load(ps=None):
    for m in ("w_bt_core", "w_bt_engine"): sys.modules.pop(m, None)
    if ps is not None: os.environ["PVAL"] = ps
    import w_bt_core as C
    return C

if part == "L":
    C = load(); t0 = time.time(); r = C.run(5)
    c = [ex(x) for x in r['comp_nat'][:5]]; print(f"   p = -1 companion ({time.time() - t0:.0f}s)", flush=True)
    GB = L.response_B(4)
    chk("(L) odd-shift Mellin part vanishes", badzero(r))
    chk("(L) raw companion has no n^{-2rho-1} term (the n^{+1} part of Lambda cancels in the extraction)", r['comp_raw'].get(-1, 0) == 0)
    for k in range(5):
        chk(f"(L) derived c_{k} = exact Laguerre rat_{k} (identically in nu, rho)",
            sp.simplify(c[k].subs({nu: L.al, J: L.rho}) - GB[k]) == 0)
    chk("(L) control: c_2 = Laguerre rat_2 with rho -> -rho", sp.simplify(c[2].subs({nu: L.al, J: -L.rho}) - GB[2]) == 0, must_fail=True)
    rc = C.run(5, control='rin_identity'); cc = [ex(x) for x in rc['comp_nat'][:5]]
    chk("(L) control: R_in -> I in the lip integrand reproduces rat_2", sp.simplify(cc[2].subs({nu: L.al, J: L.rho}) - GB[2]) == 0, must_fail=True)
    rc = C.run(5, control='no_K2'); cc = [ex(x) for x in rc['comp_nat'][:5]]
    chk("(L) control: K^2 moments dropped reproduces rat_2 (rat_0 comes from the K K' moment alone)", sp.simplify(cc[2].subs({nu: L.al, J: L.rho}) - GB[2]) == 0, must_fail=True)
    print("   c_4 (p = -1) =", c[4], flush=True)

if part == "P":
    CACHE = os.path.join(here, "..", "..", "..", "..", "..", "tmp", "w_exact")
    for ps in ("1/2", "3/2", "2", "3", "5"):
        C = load(ps); p = sp.Rational(ps); t0 = time.time(); r = C.run(4)
        c = [ex(x) for x in r['comp_nat'][:4]]
        print(f"--- p = {p} ({time.time() - t0:.0f}s): c_0 = {c[0]}\n   c_2 = {c[2]}", flush=True)
        chk(f"p={p}: odd-shift Mellin part vanishes; no n^(-2rho-1) term", badzero(r) and r['comp_raw'].get(-1, 0) == 0)
        chk(f"p={p}: c_0 = (p rho + 2 rho + 1)/2 (= H(rho) C(2rho,rho)/((p+2)^(2rho+1) Phi))", sp.simplify(c[0] - (p*J + 2*J + 1)/2) == 0)
        chk(f"p={p}: c_1 = c_3 = 0", c[1] == 0 and c[3] == 0)
        Xd = sp.factor(c[2].subs(J, sp.Rational(1, 2))/c[0].subs(J, sp.Rational(1, 2)))
        chk(f"p={p}: derived dressing at rho = 1/2 equals X(p, nu) (JZC_W_exact Obs WE.6, post hoc there): {Xd}", sp.simplify(Xd - Xpost(p)) == 0)
        rstar = sp.Rational(1, 2) + 2/p
        chk(f"p={p}: control: refuted P2 dressing g(rho*) at rho = 1/2", sp.simplify(Xd - gA(rstar, p) - gB(rstar, p)*nu**2) == 0, must_fail=True)
        fn = os.path.join(CACHE, f"poles_p{str(p).replace('/', '_')}.json")
        if os.path.exists(fn):
            d = json.load(open(fn)); r2 = sp.sympify(d["r2"], locals={"alpha": nu})
            pred = sp.factor(-(p + 2)**2*c[2].subs(J, sp.Rational(1, 2))*L.PhiC_residue(sp.Rational(1, 2)).subs(L.al, nu))
            chk(f"p={p}: Res_(j=1/2) g1[5] (cached engine run, w_exact_poles) = -(p+2)^2 c_2(1/2) Res(Phi/C)", sp.simplify(r2 - pred) == 0)
        else:
            print(f"   (no cached engine residue for p = {p})", flush=True)

if part == "B":
    C = load(); t0 = time.time(); r = C.run(4)
    c = [ex(x) for x in r['comp_nat'][:4]]; print(f"   p = 3/2, decoupled beta ({time.time() - t0:.0f}s)", flush=True)
    for k in range(4): print(f"   c_{k} = {c[k]}", flush=True)
    chk("(B) c_0..c_3 are independent of beta (natural index N = n + (beta+1)/2)", all(not c[k].has(beta) for k in range(4)))
    chk("(B) c_0 = (p rho + 2 rho + 1)/2, c_1 = c_3 = 0 at p = 3/2", sp.simplify(c[0] - (sp.Rational(3, 2)*J + 2*J + 1)/2) == 0 and c[1] == 0 and c[3] == 0)
    raw = [sp.factor(v.as_expr()) for k, v in sorted(r['comp_raw'].items()) if k >= 0]
    chk("(B) control: the RAW (n-expanded) companion is beta-free", all(not x.has(beta) for x in raw), must_fail=True)

if part == "Q":
    z, q, Cc, mu, sig = sp.symbols('z q C mu sigma')
    t = sp.tan(sp.pi*q)
    # weight continuation exp(C(-z)^q) in C_+/-: (-z)^q = z^q e^{-/+ i pi q}; split = tilt exp(tau z^q) x lip phase exp(-/+ i pi sigma z^q)
    for sgn in (1, -1):
        tau = Cc*sp.cos(sp.pi*q); pisig = Cc*sp.sin(sp.pi*q)
        chk(f"(Q) side {'+' if sgn > 0 else '-'}: C(-z)^q = (tau -/+ i pi sigma) z^q with tau = C cos(pi q), pi sigma = C sin(pi q)",
            sp.simplify(sp.expand_complex((Cc*sp.exp(-sgn*sp.I*sp.pi*q) - (tau - sgn*sp.I*pisig)).rewrite(sp.cos))) == 0)
        # lip mismatch exponent for tilt h = exp(-mu z^q) (mu = -tau) with lip factor exp(+/- i pi sigma z^q) on the (2,1) entries:
        # omega_true/omega_a = exp(+/- i (mu tan(pi q) + pi sigma) z^q)  (Lemma BT.1); here:
        expo = sp.simplify(-tau*t + pisig)
        chk(f"(Q) side {'+' if sgn > 0 else '-'}: mu tan(pi q) + pi sigma = 0 for the composite factor (no lip mismatch)", expo == 0)
    a = sp.Symbol('a')
    chk("(Q) W_outer P W-out.5/6 data tau_m = 2 pi cot(pi q) a, sigma_m = 2a: tau tan(pi q) = pi sigma",
        sp.simplify(2*sp.pi*sp.cot(sp.pi*q)*a*t - sp.pi*2*a) == 0)
    chk("(Q) control: a genuine tilt (sigma = 0) has a mismatch", sp.simplify(2*sp.pi*sp.cot(sp.pi*q)*a*t) == 0, must_fail=True)

print(f"total {NCHK} checks ({time.time() - T0:.0f}s)")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
