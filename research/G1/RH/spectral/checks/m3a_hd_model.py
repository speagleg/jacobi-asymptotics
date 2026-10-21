"""JZC M3a, lemma H-d (JZC_M3a_Hd.md §3): which decoupled formal model M(beta, nu) (m4_rh4.run(p, beta, nu=nu, mu=...))
reproduces the Hurwitz-lattice data? Hurwitz lattice: nodes (k + d)^{-p}, weights (k + d)^{-s}, k >= 1, a = 1 + d,
alpha = (s - 1 - p)/p, c = c(p), band factor mu_{n,j} = 2 zeta(-jp, a)/(j n^{jp}) in the n^p frame (Lemma H).
Candidates:
  H1 (H-d):            beta = alpha + 2d, nu = alpha      (Szego shift, Bessel order fixed, degree n, n^p frame)
  H2 (shifted s):      beta = nu = alpha + 2d             (the pure lattice with s' = s + 2pd)
  H3 (Bessel shift):   beta = alpha, nu = alpha + 2d
  H4 (half shift):     beta = alpha + d, nu = alpha
Model coefficients (KORD = 4, dps 40): d1, d2, d3 (integer layer, mu = 0), and the mu-responses by central differences
(h = 1e-15): eps_j = (2 zeta(-jp, a)/j) dd1/dmu_j, the n^{-2-p} coefficient 2 zeta(-p, a) dd2/dmu_1.
Data (Rule X: fits made earlier by other scripts, read from their .out files, never typed here):
  spec_hur.out (d1, eps1, eps2), spec_hur_d2.out (n^-2), spec_shift_hi.out (d3 and n^-3.5 at p = 1.5, s = 2),
  spec_hur_small.out (p = 1/3, 1/4: eps_i and the merged n^-2 = d2 + eps_{1/p}).
Tolerance per datum: max(3 * fit half-range, floor) as in the source scripts. Assertions: H1 passes every datum; each of
H2, H3, H4 fails at least one datum by more than 10 tolerances. Also (exact, sympy): H1's d2 equals rule H's
d2_0 + p(p+1)d^2/2 - (p+1) d d1_0 identically."""
import os, re, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
os.environ.setdefault("KORD", "4")
import mpmath as mp, sympy as sp
import m4_rh4 as M
from so_coeffs import c_p_mp
from spec_common import Checks
mp.mp.dps = 40
C_ = Checks(); HERE = os.path.dirname(os.path.abspath(__file__))
num = r"([+-]?\d+\.\d+(?:e[+-]?\d+)?)"

# ---------------- data ----------------
data = []      # (p, s, d, kind, value, halfrange, floor)
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
for L in open(os.path.join(HERE, "spec_shift_hi.out")):
    m = re.match(r"d=(\S+): d2 used \S+ \| d3 fit " + num + r" \(" + num + r"\) \| n\^-3.5 fit " + num + r" \(" + num + r"\)", L)
    if m:
        d = float(m.group(1))
        data += [(1.5, 2.0, d, "d3", float(m.group(2)), float(m.group(3)), 1e-4), (1.5, 2.0, d, "n^-2-p", float(m.group(4)), float(m.group(5)), 1e-4)]
for L in open(os.path.join(HERE, "spec_hur_small.out")):
    m = re.match(r"p = 1/(\d), s = (\S+), d = (\S+) ", L)
    if m: cur = (1/int(m.group(1)), float(m.group(2)), float(m.group(3)))
    m = re.match(r"\s+eps_(\d): fit " + num + r" \(" + num + r"\)", L)
    if m: data.append(cur + (f"eps{m.group(1)}", float(m.group(2)), float(m.group(3)), 1e-5))
    m = re.match(r"\s+n\^-2 \(merged\): fit " + num + r" \(" + num + r"\)", L)
    if m: data.append(cur + ("n^-2", float(m.group(1)), float(m.group(2)), 1e-4))
print(f"{len(data)} data read")
assert len(data) >= 30, len(data)

# ---------------- model ----------------
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
    out = {"d1": base[1], "d3": base[3]}
    for j in resp: out[f"eps{j}"] = 2*z(j)/j*resp[j][1]
    out["n^-2-p"] = 2*z(1)*resp[1][2]
    # n^-2: d2 plus the mu_j response landing at n^-2 (j p + 1 = 2, i.e. p = 1/j)
    out["n^-2"] = base[2] + sum((2*z(j)/j*resp[j][1] for j in resp if abs(j*P - 1) < 1e-9), mp.mpf(0))
    cache[key] = out; return out

cands = {"H1": lambda al, d: (al + 2*d, al), "H2": lambda al, d: (al + 2*d, al + 2*d),
         "H3": lambda al, d: (al, al + 2*d), "H4": lambda al, d: (al + d, al)}
worst = {k: 0.0 for k in cands}
print(f"{'p':>6} {'s':>4} {'d':>5} {'coef':>7} | {'fit':>12} {'tol':>8} | " + " | ".join(f"{k}: model, dev/tol" for k in cands))
for (p, s, d, kind, v, hr, fl) in data:
    P = p if p >= 0.5 else 1/round(1/p); al = mp.mpf((s - 1 - P)/P); D = mp.mpf(d); tol = max(3*hr, fl)
    row = []
    for k, f in cands.items():
        beta, nu = f(al, D); val = float(model(p, s, d, beta, nu)[kind]); dev = abs(val - v)/tol
        worst[k] = max(worst[k], dev); row.append(f"{val:+.6f} {dev:7.2f}")
        if k == "H1": C_.check(f"H1 {kind} p={p:.4g} s={s} d={d}", val, v, tol)
    print(f"{p:6.4g} {s:4} {d:5} {kind:>7} | {v:+12.6f} {tol:8.1e} | " + " | ".join(row), flush=True)
for k in ("H2", "H3", "H4"):
    print(f"{k}: worst deviation {worst[k]:.1f} tolerances")
    C_.check(f"{k} excluded (worst deviation > 10 tolerances)", float(worst[k] > 10), 1.0, 0.0)
print(f"H1: worst deviation {worst['H1']:.2f} tolerances")

# ---------------- exact: H1's integer layer to second order is rule H (sympy) ----------------
p_, al_, d_ = sp.symbols('p alpha delta')
d2 = lambda beta, nu: p_*(p_ + 1)*(beta + 1)**2/8 - (p_ + 2)*nu**2/8 + (p_ + 1)/12     # E2 Thm E2.1 decoupled (JZC_M4 §7, Prop S)
d10 = -p_*(al_ + 1)/2
C_.check("exact: d2(H1) = rule-H d2", float(sp.simplify(d2(al_ + 2*d_, al_) - (d2(al_, al_) + p_*(p_ + 1)*d_**2/2 - (p_ + 1)*d_*d10)) != 0), 0.0, 0.0)
C_.check("exact: d1(H1) = -(s-1)/2 - p delta", float(sp.simplify(-p_*(al_ + 2*d_ + 1)/2 - (d10 - p_*d_)) != 0), 0.0, 0.0)
# the decoupled d2 formula used above agrees with the model at a fresh point
dd, _ = M.run(mp.mpf('1.3'), mp.mpf('0.25'), nu=mp.mpf('-0.4'))
v2 = float(sp.Rational(13, 10)*sp.Rational(23, 10)*sp.Rational(5, 4)**2/8 - sp.Rational(33, 10)*sp.Rational(4, 25)/8 + sp.Rational(23, 120))
C_.check("decoupled d2 formula = model (p=1.3, beta=0.25, nu=-0.4)", float(dd[2]), v2, 1e-30)
C_.finish()
