"""JZC_P1 data: Jacobi coefficients of p = 1 (and control p = 2) lattice measures in Arb ball arithmetic.  NUMERICAL inputs for
p1_continuation.py; nothing is fitted here.

Measures (all with nodes y_k = (k + d)^{-p}, k >= 0):
  (H)  pure Hurwitz lattice   mu = sum_k (k+d)^{-s} delta_{y_k},  p = 1.  Moments m_i = zeta(s + i, d) exactly (Arb Hurwitz zeta).
  (T)  time-controlled tilt  mu = sum_k (k+d)^{-s} exp(sum_{j<=J} tau_j y_k^j) delta_{y_k},  tau_j := t_j + 2 zeta(-jp, d)/j,
       so that the Toda times of Paper IV (1.3)/(5.3), t_j = -2 Z(-j)/j + B_j, are exactly the prescribed t_j for j <= J (and the
       lattice values for j > J, which enter at N^{-1-(J+1)p} and beyond).  Moments: the atoms k < K0 summed directly; the tail
       k >= K0 as sum_r e_r zeta(s + p(i + r), d + K0), where exp(sum_j tau_j y^j) = sum_r e_r y^r (e_r by the recurrence
       r e_r = sum_j j tau_j e_{r-j}), truncated at r = R with (d+K0)^{-pR} < 2^{-1.15 prec}.
Jacobi coefficients: the classical Chebyshev algorithm on the moments, in ball arithmetic at `prec` bits; the radius of b_{n-1}^2
is printed ("bits left" = log2 of its relative radius).  Output: tmp/p1/<tag>.json with the midpoints of b_k^2 (k = 1..n-1) and
alpha_k (k = 0..n-1) to 200 digits.

Usage: python -B p1_arb.py [all | <tag> ...]   (two worker processes; existing caches are kept)."""
import os, sys, json, math, hashlib
from multiprocessing import Pool
from flint import arb, fmpq, ctx

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
P1C = os.path.join(ROOT, 'tmp', 'p1'); os.makedirs(P1C, exist_ok=True)
NMAX, PREC = 90, 4500


def q(x): return fmpq(*x) if isinstance(x, (tuple, list)) else fmpq(x)


def chebyshev(M, n):
    """classical Chebyshev algorithm: monic recurrence x pi_k = pi_{k+1} + alpha_k pi_k + beta_k pi_{k-1}; returns (alpha, beta)
    with beta[0] = M[0] (the mass) and beta[k] = b_k^2 (k >= 1)."""
    m = 2*n; sp_ = [arb(0)]*m; sc = M[:m]; al = [sc[1]/sc[0]]; be = [sc[0]]
    for k in range(1, n):
        new = [arb(0)]*m
        for l in range(k, m - k): new[l] = sc[l + 1] - al[k - 1]*sc[l] - be[k - 1]*sp_[l]
        al.append(new[k + 1]/new[k] - sc[k]/sc[k - 1]); be.append(new[k]/sc[k - 1]); sp_, sc = sc, new
    return al, be


def moments_hurwitz(d, s, n):
    return [(arb(q(s)) + i).zeta(arb(q(d))) for i in range(2*n)]


def moments_tilt(d, s, p, t, n, prec, J=8, K0=40):
    D, S, P = arb(q(d)), arb(q(s)), arb(q(p))
    tau = [arb(0)]*(J + 1)
    for j in range(1, J + 1):
        tau[j] = arb(q(t.get(j, (0, 1)))) + 2*(-j*P).zeta(D)/j
    m = 2*n; M = [arb(0)]*m
    for k in range(K0):
        lam = D + k; y = lam**(-P)
        w = lam**(-S)*sum((tau[j]*y**j for j in range(1, J + 1)), arb(0)).exp(); yj = arb(1)
        for i in range(m): M[i] += w*yj; yj *= y
    R = int(prec/(float(q(p))*math.log2(K0))*1.15) + 20
    e = [arb(1)] + [arb(0)]*R
    for r in range(1, R + 1):
        e[r] = sum((j*tau[j]*e[r - j] for j in range(1, min(J, r) + 1)), arb(0))/r
    a0 = D + K0; Zt = [(S + P*i).zeta(a0) for i in range(m + R + 1)]
    for i in range(m): M[i] += sum((e[r]*Zt[i + r] for r in range(R + 1)), arb(0))
    return M


# ---------------------------------------------------------------- the registered data set
def jobs():
    J = {}
    for d in ('1/10', '1/5', '3/10', '2/5', '1/2', '3/5', '4/5', '9/10', '13/10', '17/10', '21/10'):
        J[f"hur_s3/2_d{d}"] = dict(kind='H', d=d, s='3/2', p='1')
    for s in ('5/2', '7/2'):
        for d in ('1/5', '3/10'):
            J[f"hur_s{s}_d{d}"] = dict(kind='H', d=d, s=s, p='1')
    J["tilt_p1_base"] = dict(kind='T', d='1', s='3/2', p='1', t={})
    for v in ('1/4', '-1/4', '1/2', '-1/2', '3/4', '1'):
        J[f"tilt_p1_t1={v}"] = dict(kind='T', d='1', s='3/2', p='1', t={1: v})
    for j in range(2, 7):
        for v in ('1/4', '-1/4', '1/2', '-1/2'):
            J[f"tilt_p1_t{j}={v}"] = dict(kind='T', d='1', s='3/2', p='1', t={j: v})
    for v1 in ('1/4', '-1/4'):            # cross terms t1 t2, t1^2 t2
        for v2 in ('1/4', '-1/4'):
            J[f"tilt_p1_t1={v1},t2={v2}"] = dict(kind='T', d='1', s='3/2', p='1', t={1: v1, 2: v2})
    J["tilt_p1_t1=1/2,t2=1/4"] = dict(kind='T', d='1', s='3/2', p='1', t={1: '1/2', 2: '1/4'})
    J["tilt_p1_t1=1/2,t2=-1/4"] = dict(kind='T', d='1', s='3/2', p='1', t={1: '1/2', 2: '-1/4'})
    for v in ('1/4', '-1/4'):             # p = 2 control (s = 3, alpha = 0)
        J[f"tilt_p2_t2={v}"] = dict(kind='T', d='1', s='3', p='2', t={2: v}, prec=6000)
    J["tilt_p2_base"] = dict(kind='T', d='1', s='3', p='2', t={}, prec=6000)
    return J


def frac(s): a, _, b = s.partition('/'); return (int(a), int(b or 1))


def run(item):
    tag, cfg = item
    fn = os.path.join(P1C, tag.replace('/', '_') + '.json')
    if os.path.exists(fn): return f"{tag}: cached"
    prec = cfg.get('prec', PREC); ctx.prec = prec
    if cfg['kind'] == 'H':
        M = moments_hurwitz(frac(cfg['d']), frac(cfg['s']), NMAX)
    else:
        t = {int(k): frac(v) for k, v in cfg['t'].items()}
        M = moments_tilt(frac(cfg['d']), frac(cfg['s']), frac(cfg['p']), t, NMAX, prec)
    al, be = chebyshev(M, NMAX)
    rel = be[NMAX - 1].rad()/be[NMAX - 1]
    bits = float((rel.mid()).log()/math.log(2)) if rel.mid() > 0 else -prec
    json.dump(dict(cfg=cfg, n=NMAX, prec=prec, bits_left=bits,
                   b2=[x.mid().str(200, radius=False) for x in be],
                   alpha=[x.mid().str(200, radius=False) for x in al]), open(fn, 'w'))
    return f"{tag}: bits left {bits:.0f}"


if __name__ == '__main__':
    print(f"sha256 {os.path.basename(__file__)}: {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}", flush=True)
    J = jobs()
    sel = list(J.items()) if (len(sys.argv) < 2 or sys.argv[1] == 'all') else [(t, J[t]) for t in sys.argv[1:]]
    with Pool(2) as P:
        for msg in P.imap_unordered(run, sel): print(msg, flush=True)
    print("DONE", flush=True)
