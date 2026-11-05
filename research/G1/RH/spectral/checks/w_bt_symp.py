"""JZC_W_BT Thm BT, leading layer as an identity in (p, nu, beta, rho): w_bt_core with SYMBOLIC p and decoupled beta (DECOUPLE=1),
KORD = 2 (valid for c_0, c_1). Asserted: odd-shift Mellin part = 0; no n^(-2rho-1) term; c_0 = (p rho + 2 rho + 1)/2 [this is
JZC_W_exact's H(rho) for every p]; c_1 = 0. Control (must fail): c_0 = (p rho + 1)/2 (the companion without the n^(-2rho) scale)."""
import os, sys, time, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.update(KORD="2", SHI="10", DECOUPLE="1")
for k in ("PVAL", "SZOFF"): os.environ.pop(k, None)
here = os.path.dirname(os.path.abspath(__file__))
for fn in [__file__, os.path.join(here, "w_bt_core.py"), os.path.join(here, "w_bt_engine.py")]:
    print(f"sha256 {os.path.basename(fn)}: {hashlib.sha256(open(fn, 'rb').read()).hexdigest()}", flush=True)
import w_bt_core as C, sympy as sp
NCHK = 0; ok = True
def chk(label, holds, must_fail=False):
    global NCHK, ok
    NCHK += 1; passed = (not holds) if must_fail else holds; ok &= passed
    print(f"[{NCHK:2d}] {'CONTROL (must fail)' if must_fail else 'identity'}: {label}: {'holds' if holds else 'FAILS'} -> "
          f"{'PASS' if passed else 'FAIL'}", flush=True)
t0 = time.time(); r = C.run(2); p, j = sp.symbols('p j')
print(f"   symbolic (p, nu, beta, rho) run: {time.time() - t0:.0f}s", flush=True)
c = [sp.factor(v.as_expr()) for v in r['comp_nat'][:2]]
print("   c_0 =", c[0], "  c_1 =", c[1], flush=True)
chk("odd-shift Mellin part vanishes", all(x.iszero() for e in r['lam_bad'] for row in r['lam_bad'][e] for x in row))
chk("no n^(-2rho-1) term", r['comp_raw'].get(-1, 0) == 0)
chk("c_0 = (p rho + 2 rho + 1)/2 identically in (p, nu, beta, rho)", sp.simplify(c[0] - (p*j + 2*j + 1)/2) == 0)
chk("c_1 = 0", c[1] == 0)
chk("control: c_0 = (p rho + 1)/2", sp.simplify(c[0] - (p*j + 1)/2) == 0, must_fail=True)
print(f"total {NCHK} checks")
print(f"ALL {NCHK} CHECKS PASSED" if ok else "SOME CHECKS FAILED")
assert ok
