"""JZC_W_exact §3.4 (POST HOC; labelled): rational reconstruction in p of the relative N^{-2} dressing of the hard-edge companion at
rho = 1/2,  X(p, nu) := -Res_{j=1/2} g1[5] / Res_{rho=1/2} H  (= c0(p) + c2(p) nu^2),
from the exact residues cached by w_exact_poles.py (tmp/w_exact/poles_p*.json; every p there is an exact engine run).
Ansatz: c_i(p) = P_i(p) / (p^m (p+4)(3p+2)) with P_i a polynomial; the degree is the smallest one for which the interpolant through
the first deg+1 points (in the order listed) reproduces ALL remaining points exactly; at least 3 spare points are required.
The registered P2 (c0 + c2 nu^2 = g(rho*), rho* = 1/2 + 2/p) is shown to fail at every cached p != -1 (control) and to hold at
p = -1 (where it is the exact Laguerre reflection)."""
import os, sys, json, glob, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
here = os.path.dirname(os.path.abspath(__file__))
print(f"sha256 {os.path.basename(__file__)}: {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}")
CACHE = os.path.join(here, "..", "..", "..", "..", "..", "tmp", "w_exact")
nu, P = sp.Symbol('alpha'), sp.Symbol('p')
data = {}
for fn in sorted(glob.glob(os.path.join(CACHE, "poles_p*.json"))):
    d = json.load(open(fn)); p = sp.Rational(d["p"]); X = sp.expand(sp.sympify(d["X"], locals={"alpha": nu}))
    data[p] = (X.coeff(nu, 0), X.coeff(nu, 2), sp.simplify(X - X.coeff(nu, 0) - X.coeff(nu, 2)*nu**2) == 0, d["registered"])
    print(f"p = {p}: X = {sp.factor(X)}   ({'registered' if d['registered'] else 'post hoc'} p; file {os.path.basename(fn)}, {d['time']})")
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}")
chk(f"X is quadratic in nu (c0 + c2 nu^2) at all {len(data)} p", all(v[2] for v in data.values()))
def A(w, p): return (w**2*(w**2 + 2*w - 2)*p**3 + 2*(w + 1)*(2*w**2 - 1)*p**2 + (5*w**2 + 2*w - 6)*p + 2*(w - 2))/(24*(2*w - 1)*p)
def B(w, p): return (p + 2)*(w**2*p**2 + (w + 1)*p + 2)/(8*(2*w - 1)*p)
def p2form(p, c0, c2): return sp.simplify(c0 + c2*nu**2 - A(sp.Rational(1, 2) + 2/p, p) - B(sp.Rational(1, 2) + 2/p, p)*nu**2) == 0
if -1 in data:
    chk("at p = -1 the registered P2 form holds (it is the exact Laguerre reflection, rho* = -1 - rho)", p2form(-1, *data[-1][:2]))
chk("control: registered P2 form X = g(1/2 + 2/p) at some cached p != -1",
    any(p2form(p, c0, c2) for p, (c0, c2, _, _) in data.items() if p != -1), must_fail=True)
pts = sorted(data)
found = {}
for i, name in ((0, "c0"), (1, "c2")):
    for m in range(0, 4):
        ys = {p: data[p][i]*p**m*(p + 4)*(3*p + 2) for p in pts}
        for deg in range(0, len(pts) - 3):
            fit = sp.interpolate([(p, ys[p]) for p in pts[:deg + 1]], P)
            if all(sp.simplify(fit.subs(P, p) - ys[p]) == 0 for p in pts):
                found[name] = (m, deg, sp.factor(fit/(P**m*(P + 4)*(3*P + 2))))
                break
        if name in found: break
for name in ("c0", "c2"):
    if name in found:
        m, deg, expr = found[name]
        print(f"   {name}(p) = {expr}   (numerator degree {deg}, m = {m}; {len(pts) - deg - 1} spare points reproduced exactly)")
    else:
        print(f"   {name}(p): no fit with numerator degree <= {len(pts) - 4} and m <= 3 (needs more p values)")
chk("c0 and c2 reconstructed with >= 3 spare points", "c0" in found and "c2" in found)
if "c0" in found and "c2" in found:
    Xp = found["c0"][2] + found["c2"][2]*nu**2
    print("   X(p, nu) =", sp.factor(sp.together(Xp)))
    print("   at p = -1 (Laguerre reflection: X = g(-3/2) at p = -1 = -105/1536 + 19 nu^2/128):", sp.expand(Xp.subs(P, -1)))
print(f"total {NCHK} checks")
print("ALL IDENTITIES HOLD" if ok else "IDENTITY FAILURE")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
