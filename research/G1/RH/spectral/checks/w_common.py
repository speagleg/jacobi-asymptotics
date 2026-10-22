"""JZC_W (Conjecture W) common helpers: measures, the W prediction, fits.  NUMERICAL tooling; no claim is proved here.

Conjecture W (JZC_W.md §1) for a weighted node set: nodes lam_k (distinct, increasing, lam_k ~ k^p), masses
w_k = lam_k^{-s/p} v(lam_k), measure sigma = sum_k w_k delta_{1/lam_k}.  Data read from the spectrum:
  - Z(w) = sum_k lam_k^{-w} (node zeta, continued); Z(0); Z(-j) (j >= 1, finite part if resonant);
  - the non-Weyl poles q of w -> Z(-w) with w-residues R_q (the Weyl pole is w = -1/p);
  - the mass factor v(lam) = v0 lam^tau (1 + ...): s_eff := s - p tau, alpha := (s_eff - 1 - p)/p;
  - the density factor D(x) := (dNbar/dlam) / ((1/p) lam^{1/p - 1}) = 1 - p sum_q R_q x^{q + 1/p}  (x = 1/lam; exact given
    the expansion of the smoothed count Nbar(lam) = lam^{1/p} + sum_r A_r lam^r + Z(0), since Res_{w=q} Z(-w) = q A_{-q});
  - the band tilt T(x) := log[ v(1/x) x^tau / v0 ] + log D(x) = sum_rho B_rho x^rho.
Prediction for n^p b_n / c (c = c(p)):
  (a) the decoupled model M(beta, nu) (JZC_M4 §7; engine m4_rh4.run) with nu = alpha and beta = alpha - 2 Z(0) - 1;
  (b) flowed along the Toda hierarchy (JZC_M4 §8) with times t_j = -2 Z(-j)/j + B_j (integer rho = j), i.e. engine band-factor
      parameters mu_j = -t_j (the coefficient of z^j n^{-jp}); first and second order in the times;
  (c) pole terms  p R_q W(q) pi cot(pi q) (n/N)^p N^{-1-pq}   (N = n + (beta + 1)/2),
      branched tilts (non-integer rho)  -(p rho W(rho)/2) B_rho (n/N)^p N^{-1-p rho},
  W(q) = (4c)^q Gamma(q + 1/2)/(sqrt(pi) Gamma(q + 1)).
Special cases: Theorem N.6 (lattice), Theorem H (Hurwitz), the pole law (SPEC §3.12), S1'''' (SPEC §3.15: the rho = q + 1/p
tilt is the "Jacobian" term, the (n/N)^p N^{-1-pq} expansion is the "shifted pole" term)."""
import os, sys, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'second_order', 'checks'))
os.environ.setdefault("KORD", "4")
from pathlib import Path
from collections import defaultdict
import numpy as np, mpmath as mp
from scipy.special import roots_jacobi
from so_coeffs import c_p_mp
from so_fit import sequences
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
import m4_rh4 as M

NMAX = 1600
ROOT = Path(HERE).resolve().parents[4]
WC = ROOT / 'tmp' / 'w_cache'; WC.mkdir(parents=True, exist_ok=True)
mp.mp.dps = 40


def W(q, c):
    q = mp.mpf(q); return (4*c)**q*mp.gamma(q + mp.mpf(1)/2)/(mp.sqrt(mp.pi)*mp.gamma(q + 1))


def isint(x, tol=1e-9): return abs(x - round(float(x))) < tol


def gA(j, p): return (j**2*(j**2 + 2*j - 2)*p**3 + 2*(j + 1)*(2*j**2 - 1)*p**2 + (5*j**2 + 2*j - 6)*p + 2*(j - 2))/(24*(2*j - 1)*p)
def gB(j, p): return (p + 2)*(j**2*p**2 + (j + 1)*p + 2)/(8*(2*j - 1)*p)     # JZC_M4 §6 / Theorem N.6(ii): g_j = A_j + B_j nu^2


# ------------------------------------------------------------------ measures ------------------------------------------------
def run_measure(tag, lam, wts, p, tails, nmax=NMAX):
    """atoms 1/lam_k with masses wts_k, plus continuum tails [(T0, C, s_eff), ...]: int_{T0}^inf C t^{-s_eff} f(t^{-p}) dt
    (Gauss-Jacobi, exact on polynomials of degree < 2(nmax+8)).  Cache keyed by sha256 of (lam, wts, p, tails, nmax).
    Returns (n, y) with y_n = n^p b_n / c(p) - 1."""
    h = hashlib.sha256(np.ascontiguousarray(np.asarray(lam, np.float64)).tobytes())
    h.update(np.ascontiguousarray(np.asarray(wts, np.float64)).tobytes()); h.update(repr((float(p), tails, nmax)).encode())
    f = WC / f"{tag}__{h.hexdigest()[:16]}.txt"
    if not f.exists():
        xs, ws = [1/np.asarray(lam, np.float64)], [np.asarray(wts, np.float64)]
        tx, tw = [], []
        for (T0, C, se) in tails:
            beta = (se - 1)/p - 1; u, wu = roots_jacobi(nmax + 8, 0.0, beta); X = T0**(-p)
            tx.append(X*(1 + u)/2); tw.append(C*wu*(X/2)**(beta + 1)/p)
        mu = DiscreteMeasure.from_atoms(xs[0], ws[0], tail=(np.concatenate(tx), np.concatenate(tw)))
        jc = jacobi_rkpw(mu, nmax + 1, prec="q")
        with open(f, "w") as fh:
            for a_, b2 in zip(jc.a[:nmax], jc.b2[:nmax]): fh.write(f"{mp.nstr(a_, 36)} {mp.nstr(mp.sqrt(b2), 36)}\n")
    rows = [l.split() for l in open(f)]
    al = np.array([mp.mpf(r[0]) for r in rows], dtype=object); b = np.array([mp.mpf(r[1]) for r in rows], dtype=object)
    n, y, *_ = sequences(p, al, b)
    return n.astype(float), y, f.name


# ------------------------------------------------------------------ model engine ----------------------------------------------
def model(p, beta, nu, js, pairs, tag):
    """d_k (k <= KORD) of M(beta, nu) and the Toda responses: r1[j][k] = dd_k/dmu_j, r2[(j, j')][k] = d^2 d_k/dmu_j dmu_j'.
    Central differences at dps 40 (h = 1e-12 first order, 1e-7 second order).  Cached in tmp/w_cache (json)."""
    key = WC / f"model_{tag}_{hashlib.sha256(repr((str(p), str(beta), str(nu), js, pairs, M.KORD)).encode()).hexdigest()[:12]}.json"
    if key.exists():
        D = json.load(open(key)); return ({'d': [mp.mpf(x) for x in D['d']], 'r1': {int(j): [mp.mpf(x) for x in v] for j, v in D['r1'].items()},
                                          'r2': {tuple(map(int, k.split(','))): [mp.mpf(x) for x in v] for k, v in D['r2'].items()}})
    P, B, Nu = mp.mpf(p), mp.mpf(beta), mp.mpf(nu); c = mp.mpf(c_p_mp(P))
    run = lambda mu: M.run(P, B, c=c, nu=Nu, mu=mu or None)[0]
    d = run({}); r1 = {}; r2 = {}
    h = mp.mpf(10)**-12
    for j in js:
        up, dn = run({j: h}), run({j: -h}); r1[j] = [(a - b)/(2*h) for a, b in zip(up, dn)]
    H = mp.mpf(10)**-7
    for (j, jj) in pairs:
        if j == jj:
            up, dn = run({j: H}), run({j: -H}); r2[(j, j)] = [(a - 2*b0 + b)/H**2 for a, b0, b in zip(up, d, dn)]
        else:
            pp_, pm_, mp_, mm_ = run({j: H, jj: H}), run({j: H, jj: -H}), run({j: -H, jj: H}), run({j: -H, jj: -H})
            r2[(j, jj)] = [(a - b - cc + e)/(4*H*H) for a, b, cc, e in zip(pp_, pm_, mp_, mm_)]
    json.dump({'d': [str(x) for x in d], 'r1': {str(j): [str(x) for x in v] for j, v in r1.items()},
               'r2': {f"{a},{b}": [str(x) for x in v] for (a, b), v in r2.items()}}, open(key, 'w'))
    return {'d': d, 'r1': r1, 'r2': r2}


# ------------------------------------------------------------------ series in monomials x^rho ----------------------------------
def ser_mul(A, B, rmax):
    out = defaultdict(lambda: mp.mpf(0))
    for a, ca in A.items():
        for b, cb in B.items():
            if a + b <= rmax + 1e-9: out[round(a + b, 9)] += ca*cb
    return dict(out)


def ser_log1p(A, rmax):
    """log(1 + A), A = {rho: coef} with all rho > 0"""
    out = defaultdict(lambda: mp.mpf(0)); pw = dict(A); k = 1
    while pw:
        for r, cr in pw.items(): out[r] += (-1)**(k + 1)*cr/k
        pw = ser_mul(pw, A, rmax); k += 1
    return dict(out)


# ------------------------------------------------------------------ the W prediction ---------------------------------------------
def predict(spec, emax=4.6, toda2=True, variant=None):
    """spec: dict with p, s_eff, Z0, Zneg {j: Z(-j)}, poles [(q, R)], vtilt {rho: B} (log of the mass factor beyond lam^tau),
    tag.  Returns (terms, info): terms = list of (exponent, coefficient, label).  variant switches off pieces (alternatives)."""
    variant = variant or set()
    p = mp.mpf(spec['p']); c = mp.mpf(c_p_mp(p)); al = (mp.mpf(spec['s_eff']) - 1 - p)/p
    Z0 = mp.mpf(spec['Z0']); beta = al - 2*Z0 - 1 if 'beta=alpha' not in variant else al
    dN = (beta + 1)/2
    poles = [(mp.mpf(q), mp.mpf(R)) for q, R in spec['poles']]
    # band tilt T(x) = log V + log D
    rmax = float((emax - 1)/p) + 1e-9
    Dser = {round(float(q + 1/p), 9): -p*R for q, R in poles if R != 0 and float(q + 1/p) <= rmax}
    T = defaultdict(lambda: mp.mpf(0))
    if 'no density tilt' not in variant:
        for r, v in ser_log1p(Dser, rmax).items(): T[r] += v
    if 'no mass tilt' not in variant:
        for r, v in spec.get('vtilt', {}).items():
            if float(r) <= rmax: T[round(float(r), 9)] += mp.mpf(v)
    # Toda times (integer rho) and branched tilts
    Bint = {int(round(r)): v for r, v in T.items() if isint(r)}
    Bbr = {r: v for r, v in T.items() if not isint(r)}
    js = [j for j in range(1, 12) if 1 + j*float(p) <= emax + 1e-9]
    resonant = {int(round(float(q))) for q, R in poles if isint(q) and R != 0 and float(q) >= 1}
    X = {}                                                                 # mu_j = -t_j = 2 Z(-j)/j - B_j
    for j in js:
        if j in resonant: continue
        Zj = mp.mpf(spec['Zneg'][j]) if 'no zeta' not in variant else mp.mpf(0)
        X[j] = 2*Zj/j - Bint.get(j, 0)
    pairs = [(j, jj) for j in X for jj in X if j <= jj and 2 + (j + jj)*float(p) <= emax + 1e-9] if toda2 else []
    mod = model(p, beta, al, tuple(sorted(X)), tuple(pairs), spec['tag'])
    terms = []
    for k in range(1, M.KORD + 1): terms.append((k, mod['d'][k], 'model'))
    for j, x in X.items():
        for k in range(1, M.KORD + 1):
            if k + j*p <= emax + 1e-9: terms.append((k + j*float(p), x*mod['r1'][j][k], f'toda mu{j}'))
    for (j, jj) in pairs:
        f = X[j]*X[jj]*(mp.mpf(1)/2 if j == jj else 1)
        for k in range(2, M.KORD + 1):
            if k + (j + jj)*p <= emax + 1e-9: terms.append((k + (j + jj)*float(p), f*mod['r2'][(j, jj)][k], f'toda mu{j}mu{jj}'))
    if 'no pole' not in variant:
        for q, R in poles:
            if isint(q) or R == 0: continue
            L = p*R*W(q, c)*mp.pi*mp.cot(mp.pi*q)
            terms.append((float(1 + p*q), L, f'pole q={float(q):.4g}'))
            if 'no shift' not in variant: terms.append((float(2 + p*q), -(1 + p*q + p)*dN*L, f'pole-shift q={float(q):.4g}'))
    if 'dressing' in variant:                 # W' (post hoc, JZC_W §2.4): the zeta layer's N^-2 dressing g(w) = A(w) + B(w) nu^2
        h = mp.mpf(10)**-15                    # (JZC_M4 §6) continued to w = q, and the second-order natural-index shift
        for q, R in poles:
            if isint(q) or R == 0: continue
            f = lambda w: mp.cot(mp.pi*w)*(gA(w, p) + gB(w, p)*al**2)
            cg = (f(q + h) + f(q - h))/2                                           # finite at q = 1/2 (0 * infinity)
            L0 = p*R*W(q, c)*mp.pi
            terms.append((float(3 + p*q), L0*cg, f'pole-dressing q={float(q):.4g}'))
            terms.append((float(3 + p*q), L0*mp.cot(mp.pi*q)*(1 + p*q + p)*(2 + p*q + p)/2*dN**2, f'pole-shift2 q={float(q):.4g}'))
        for r, B in Bbr.items():
            Tt = -(p*mp.mpf(r)*W(r, c)/2)*B
            terms.append((float(3 + p*r), Tt*(gA(mp.mpf(r), p) + gB(mp.mpf(r), p)*al**2 + (1 + p*r + p)*(2 + p*r + p)/2*dN**2), f'tilt-dressing rho={r:.4g}'))
    if 'no branched tilt' not in variant:
        for r, B in Bbr.items():
            Tt = -(p*mp.mpf(r)*W(r, c)/2)*B
            terms.append((float(1 + p*r), Tt, f'tilt rho={r:.4g}'))
            if 'no shift' not in variant: terms.append((float(2 + p*r), -(1 + p*r + p)*dN*Tt, f'tilt-shift rho={r:.4g}'))
    terms = [(round(e, 6), v, l) for e, v, l in terms if e <= emax + 1e-6]
    info = dict(alpha=al, beta=beta, N_shift=dN, c=c, X=X, Bint=Bint, Bbr=Bbr, resonant=sorted(resonant),
                logexps=[round(float(1 + p*q), 6) for q, R in poles if isint(q) and R != 0])
    return terms, info


def by_exponent(terms):
    out = defaultdict(lambda: mp.mpf(0))
    for e, v, _ in terms: out[e] += v
    return dict(sorted(out.items()))


# ------------------------------------------------------------------ fits ------------------------------------------------------
def pool(p, emax=9.0, extra=()):
    return sorted({round(i + j*p, 6) for i in range(1, 10) for j in range(0, 12) if i + j*p <= emax} | {round(e, 6) for e in extra})


def fit_target(n, y, p, target, pred, logexps=(), los=(100, 200, 400), Js=(3, 4, 5, 6)):
    """coefficient of n^-target in y - sum_{e < target} pred[e] n^-e, nuisance: the next exponents of {i + jp} (and n^-e log n at
    resonant exponents e >= target).  Returns (median, half-range)."""
    r = np.array(y, float) - sum(float(v)*n**(-e) for e, v in pred.items() if e < target - 1e-6)
    P = [e for e in pool(p) if e > target + 1e-6]
    est = []
    for J in Js:
        E = [target] + P[:J - 1]
        cols = [n**(-e) for e in E] + [n**(-e)*np.log(n) for e in logexps if e >= target - 1e-6 and e <= E[-1] + 1e-6]
        for lo in los:
            m = n >= lo; A = np.vstack([cc[m] for cc in cols]).T
            sc = np.abs(A).max(axis=0); co = np.linalg.lstsq(A/sc, r[m], rcond=None)[0]/sc
            est.append(co[0])
    est = np.array(est)
    return float(np.median(est)), float((est.max() - est.min())/2)


class Checks:
    def __init__(s): s.fails = []; s.n = 0
    def check(s, label, ok):
        s.n += 1
        if not ok: s.fails.append(label)
        return ok
    def finish(s):
        for f in s.fails: print("  FAIL", f)
        print(f"ALL {s.n} CHECKS PASSED" if not s.fails else f"{len(s.fails)} OF {s.n} CHECKS FAILED")
        return not s.fails
