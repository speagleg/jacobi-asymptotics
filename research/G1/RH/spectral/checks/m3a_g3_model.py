"""JZC M3a, gap G3 (JZC_M3a_H_G3.md §4): for 0 < p < 1, does the decoupled model M(beta' = alpha + 2d, nu = alpha)
(m4_rh4.run(p, beta, nu=nu, mu=...)) with the Hurwitz band factor mu_{n,j} = 2 zeta(-jp, 1+d)/(j n^{jp}) reproduce every stored
p < 1 Hurwitz fit datum?  This is m3a_hd_model.py restricted to the p < 1 rows (pattern and tolerances copied from there):
the band factor is now the seam one (E_plt1 Lemma F.1 with the shifted jump, JZC_M3a_H_G3.md Prop 3.2), whose moments
are the same Hurwitz values (SPEC §3.1, spec_hurwitz_moments_plt1.out).
Data (Rule X: fits made earlier by other scripts from the actual Hurwitz measures, read from their .out files):
  spec_hur.out (d1, eps1, eps2 at p = 0.6, 0.75), spec_hur_d2.out (n^-2 at p = 0.6, 0.75), spec_hur_small.out (p = 1/3, 1/4).
Rows with d in (-1, 0] are the theorem's range; d = 1/2, 1 rows are outside it (printed and asserted, flagged 'ext').
Assertions: H1 = (alpha + 2d, alpha) passes every p < 1 datum within max(3 x fit half-range, floor); each alternative
H2 = (alpha+2d, alpha+2d), H3 = (alpha, alpha+2d), H4 = (alpha+d, alpha) fails some p < 1 datum by > 10 tolerances."""
import os, re, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
os.environ.setdefault("KORD", "4")
import mpmath as mp
import m4_rh4 as M
from so_coeffs import c_p_mp
from spec_common import Checks
mp.mp.dps = 40
C_ = Checks(); HERE = os.path.dirname(os.path.abspath(__file__))
num = r"([+-]?\d+\.\d+(?:e[+-]?\d+)?)"
data = []
for L in open(os.path.join(HERE, "spec_hur.out")):
    m = re.match(r"p=(\S+) s=(\S+) d=(\S+) a=\S+: d1 fit " + num + r" \(" + num + r"\).*n\^-1-p fit " + num + r" \(" + num + r"\)", L)
    if m:
        p, s, d = (float(m.group(i)) for i in (1, 2, 3)); cur = (p, s, d)
        data += [(p, s, d, "d1", float(m.group(4)), float(m.group(5)), 1e-5), (p, s, d, "eps1", float(m.group(6)), float(m.group(7)), 1e-4)]
    m = re.match(r"\s+n\^-1-2p fit " + num + r" \(" + num + r"\)", L)
    if m: data.append(cur + ("eps2", float(m.group(1)), float(m.group(2)), 1e-4))
for L in open(os.path.join(HERE, "spec_hur_d2.out")):
    m = re.match(r"\s*(\S+)\s+(\S+)\s+(\S+) \|\s+" + num + r"\s+" + num + r" \|", L)
    if m: data.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), "n^-2", float(m.group(4)), float(m.group(5)), 1e-4))
for L in open(os.path.join(HERE, "spec_hur_small.out")):
    m = re.match(r"p = 1/(\d), s = (\S+), d = (\S+) ", L)
    if m: cur = (1/int(m.group(1)), float(m.group(2)), float(m.group(3)))
    m = re.match(r"\s+eps_(\d): fit " + num + r" \(" + num + r"\)", L)
    if m: data.append(cur + (f"eps{m.group(1)}", float(m.group(2)), float(m.group(3)), 1e-5))
    m = re.match(r"\s+n\^-2 \(merged\): fit " + num + r" \(" + num + r"\)", L)
    if m: data.append(cur + ("n^-2", float(m.group(1)), float(m.group(2)), 1e-4))
data = [x for x in data if x[0] < 1]
nin = sum(1 for x in data if -1 < x[2] <= 0)
print(f"{len(data)} p < 1 data read ({nin} with -1 < d <= 0)"); assert len(data) >= 15 and nin >= 8, (len(data), nin)

cache = {}
def model(p, s, d, beta, nu):
    key = (p, s, d, float(beta), float(nu))
    if key in cache: return cache[key]
    P = mp.mpf(p) if p >= 0.5 else 1/mp.mpf(round(1/p)); c = mp.mpf(c_p_mp(float(P))); a = 1 + mp.mpf(d)
    base, _ = M.run(P, beta, c=c, nu=nu)
    h = mp.mpf(10)**-15; resp = {}
    for j in (1, 2, 3, 4):
        if j*P >= 2 - mp.mpf(10)**-9 and j > 1: continue
        up, _ = M.run(P, beta, c=c, nu=nu, mu={j: h}); dn, _ = M.run(P, beta, c=c, nu=nu, mu={j: -h})
        resp[j] = [(x - y)/(2*h) for x, y in zip(up, dn)]
    z = lambda j: mp.zeta(-j*P, a)
    out = {"d1": base[1]}
    for j in resp: out[f"eps{j}"] = 2*z(j)/j*resp[j][1]
    out["n^-2"] = base[2] + sum((2*z(j)/j*resp[j][1] for j in resp if abs(j*P - 1) < 1e-9), mp.mpf(0))
    cache[key] = out; return out

cands = {"H1": lambda al, d: (al + 2*d, al), "H2": lambda al, d: (al + 2*d, al + 2*d),
         "H3": lambda al, d: (al, al + 2*d), "H4": lambda al, d: (al + d, al)}
worst = {k: 0.0 for k in cands}; worst_in = 0.0
print(f"{'p':>6} {'s':>4} {'d':>5} {'':>3} {'coef':>5} | {'fit':>10} {'tol':>8} | " + " | ".join(f"{k}: model, dev/tol" for k in cands))
for (p, s, d, kind, v, hr, fl) in data:
    P = p if p >= 0.5 else 1/round(1/p); al = mp.mpf((s - 1 - P)/P); D = mp.mpf(d); tol = max(3*hr, fl); row = []
    for k, f in cands.items():
        beta, nu = f(al, D); val = float(model(p, s, d, beta, nu)[kind]); dev = abs(val - v)/tol
        worst[k] = max(worst[k], dev); row.append(f"{val:+.6f} {dev:8.2f}")
        if k == "H1":
            C_.check(f"H1 {kind} p={p:.4g} s={s} d={d}", val, v, tol)
            if -1 < d <= 0: worst_in = max(worst_in, dev)
    print(f"{p:6.4g} {s:4} {d:5} {'' if -1 < d <= 0 else 'ext':>3} {kind:>5} | {v:+10.6f} {tol:8.1e} | " + " | ".join(row), flush=True)
for k in ("H2", "H3", "H4"):
    print(f"{k}: worst deviation on p < 1 data {worst[k]:.1f} tolerances")
    C_.check(f"{k} excluded on p < 1 data (worst deviation > 10 tolerances)", float(worst[k] > 10), 1.0, 0.0)
print(f"H1: worst deviation {worst['H1']:.2f} tolerances (in-range rows: {worst_in:.2f})")
C_.finish()
