import sys, numpy as np, mpmath as mp
from math import comb
from pathlib import Path
import os; sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'second_order', 'checks'))
from so_coeffs import c_p_mp
from so_fit import sequences
from scipy.special import roots_jacobi
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.jacobi.rkpw import jacobi_rkpw
NMAX = 1600
CACHE = Path(__file__).resolve().parents[5] / 'tmp' / 'spectral_cache'
CACHE.mkdir(parents=True, exist_ok=True)
def _key(lam, p, s, tail_delta, K):
    """hash of the measure inputs (REVIEW_SPEC2_B F2: caches keyed by tag only could silently mask a changed measure)."""
    import hashlib
    h = hashlib.sha256(np.ascontiguousarray(np.asarray(lam, dtype=np.float64)).tobytes())
    h.update(repr((float(p), float(s), float(tail_delta), int(K), NMAX)).encode())
    return h.hexdigest()[:16]
def _find(tag):
    fs = sorted(CACHE.glob(f"{tag}__*.txt"))
    if len(fs) != 1: raise FileNotFoundError(f"cache for tag {tag!r}: {len(fs)} hashed files (need exactly 1; run the generating script)")
    return fs[0]
def load_raw(tag):
    """(alpha, b) as mpf lists from the unique hashed cache of `tag` (for scripts that only read)."""
    mp.mp.dps = 40; rows = [l.split() for l in open(_find(tag))]
    return [mp.mpf(r[0]) for r in rows], [mp.mpf(r[1]) for r in rows]
def run(tag, lam, p, s, tail_delta, K):
    """atoms 1/lam_k, weights lam_k^{-s/p} (k<=K), pure-power continuum tail of (k+tail_delta)^p beyond K+1/2.
    Cache file: CACHE/<tag>__<sha256 of (lam, p, s, tail_delta, K)>.txt; lam=None reads the unique cache of <tag>."""
    mp.mp.dps = 40
    f = _find(tag) if lam is None else CACHE / f"{tag}__{_key(lam, p, s, tail_delta, K)}.txt"
    if not f.exists():
        x, w = 1/lam, lam**(-s/p)
        beta = (s-1)/p - 1; u, wu = roots_jacobi(NMAX+8, 0.0, beta); X = (K+0.5+tail_delta)**(-p)
        mu = DiscreteMeasure.from_atoms(x, w, tail=(X*(1+u)/2, wu*(X/2)**(beta+1)/p))
        jc = jacobi_rkpw(mu, NMAX+1, prec="q")
        with open(f, "w") as fh:
            for a_, b2 in zip(jc.a[:NMAX], jc.b2[:NMAX]): fh.write(f"{mp.nstr(a_, 36)} {mp.nstr(mp.sqrt(b2), 36)}\n")
    rows = [l.split() for l in open(f)]
    al = np.array([mp.mpf(r[0]) for r in rows], dtype=object); b = np.array([mp.mpf(r[1]) for r in rows], dtype=object)
    n, y, *_ = sequences(p, al, b)
    return n.astype(float), y
class Checks:
    """pass/fail assertions for numerical comparisons (REVIEW_SPEC2_B F4): check(label, value, pred, tol)."""
    def __init__(self): self.fails = []; self.n = 0
    def check(self, label, value, pred, tol):
        self.n += 1; ok = abs(value - pred) <= tol
        if not ok: self.fails.append(f"{label}: {value:+.6g} vs {pred:+.6g} (tol {tol:.1e})")
        return ok
    def finish(self):
        for fl in self.fails: print("  FAIL", fl)
        assert not self.fails, f"{len(self.fails)} of {self.n} checks failed"
        print(f"ALL {self.n} CHECKS PASSED")
def fit(n, r, p, skip, tgt, fr=(0.1, 0.2, 0.3), Js=(4, 5, 6, 7)):
    E_all = sorted({round(1+i+j*p, 9) for i in range(8) for j in range(8)})
    E0 = [e for e in E_all if all(abs(e-x) > 1e-9 for x in skip)]; out = []
    for J in Js:
        E = E0[:J]
        for f_ in fr:
            m = n >= f_*n.max(); n0 = n[m].min()
            A = np.vstack([(n0/n[m])**e for e in E]).T
            out.append((np.linalg.lstsq(A, r[m], rcond=None)[0]*np.array([n0**e for e in E]))[E.index(round(tgt, 9))])
    out = np.array(out); return float(np.median(out)), float((out.max()-out.min())/2)
