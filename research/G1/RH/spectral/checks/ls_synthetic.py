"""LS_BOLZA (pre-registration stage): synthetic positive and negative controls for the Lanczos–Selberg pipeline, run BEFORE
any Bolza data is read.  NUMERICAL.

Node sets (p = 1, s = 2, unit masses), density nu = 2/5, counting function N(lambda) = nu*lambda - a - 1/2 + A w(lambda) sin(l0 r),
r = sqrt(lambda - 1/4), l0 = 3.057141838961996 (Bolza systole), taper w = 1 on lambda < 600, cos^2 to 0 on [600, 850], cut at
lambda_cut = 998 with the exact Hurwitz tail beyond (ls_common).  Nodes solve N(lambda_k) = k - 1/2.
 (S0) A = 0: D_n = 0 identically (negative control: the pipeline adds nothing).
 (S1) A = 1/2: the EDGE LAW (LS_BOLZA §2), D_n ~ E[N_osc](n) := -(1/2) f.p. int_0^1 (1 - u)^{-3/2} N_osc(u lambda*) du,
      lambda* = N/(2 nu), N = n + alpha/2 - Z(0) (= n + 4/5 here), holds with corr <= -0.9 and slope in [-1.1, -0.85] on
      n in [40, 300]; CLEAN finds l0 first (within 0.1) with phase near -pi/4.
 (S2) A = 1/2 plus a second line A2 = 1/4 at l2 = 4.896904895356152, plus i.i.d. jitter of the nodes (uniform +-0.15 spacing,
      seed 11): CLEAN's first two lines are l0 and l2 (within 0.1); edge-law corr <= -0.7.
Calibration record (Rule X): the first run used the naive "adiabatic" law D_n ~ N_osc(lambda*); it found the line but with
amplitude 3.70 against 0.5 and a phase offset.  The edge law above is the S2' kernel (u(1-u)^{-3/2}/2k per displaced node,
SPEC §3.18) integrated against a slowly varying displacement field; it was derived after that run and before any Bolza data."""
import os, sys, random, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mpmath as mp
import numpy as np
from ls_common import *
for f in (__file__, os.path.join(HERE, 'ls_common.py')):
    print(f"sha256 {os.path.basename(f)}: {hashlib.sha256(open(f, 'rb').read()).hexdigest()}", flush=True)
mp.mp.dps = 60
NU, A0, S = mp.mpf(2)/5, mp.mpf('0.3'), 2
L0, L2 = mp.mpf('3.057141838961996'), mp.mpf('4.896904895356152')
LCUT, NMAX, PREC = 998, 300, int(os.environ.get('LS_PREC', 11000))
NS = list(range(40, NMAX))


def taper(lam):
    if lam < 600: return mp.mpf(1)
    if lam > 850: return mp.mpf(0)
    return mp.cos(mp.pi*(lam - 600)/500)**2


def nodes(lines, jitter=0, seed=11):
    rng = random.Random(seed)
    def Nf(lam):
        r = mp.sqrt(lam - mp.mpf(1)/4) if lam > mp.mpf(1)/4 else mp.mpf(0)
        return NU*lam - A0 - mp.mpf(1)/2 + taper(lam)*sum(A*mp.sin(l*r) for A, l in lines)
    out = []; k = 1
    K = int(mp.ceil(NU*LCUT - A0))
    while k < K:
        lam = invert_counting(Nf, k, mp.mpf('0.3'), mp.mpf(3*LCUT))
        if jitter and lam < 850: lam += (rng.random()*2 - 1)*jitter/NU
        out.append(lam); k += 1
    return out, K


def run(lines, jitter=0):
    nd, K = nodes(lines, jitter)
    b2, bits = b2_series(nd, [1]*len(nd), NU, A0, K, S, NMAX, PREC)
    return b2, bits, nd



def edge_law(ns, lines, shift):
    out = {}
    for n in ns:
        ls = (n + shift)/(2*NU)
        f = lambda u: float(taper(u*ls)*sum(A*mp.sin(l*mp.sqrt(max(u*ls - 0.25, 0))) for A, l in lines))
        f1 = f(1.0)
        I = mp.quad(lambda u: (f(float(u)) - f1)/(1 - u)**1.5, [0, 0.5, 0.9, 0.99, 1])
        out[n] = 0.5*(float(I) - 2*f1)
    return out


def corr_slope(D, P):
    Y = np.array([float(D[n]) for n in NS]); X = np.array([P[n] for n in NS])
    return float(np.corrcoef(X, Y)[0, 1]), float(np.dot(X, Y)/np.dot(X, X))


SHIFT = 4/5                                   # N - n = alpha/2 - Z(0), alpha = 0, Z(0) = zeta(0, 1 + a) = -1/2 - a
ELLS = [1 + 0.005*i for i in range(1400)]
b2s, bits0 = b2_series([], [], NU, A0, 1, S, NMAX, PREC)
print(f"smooth comparator: bits left {bits0:.0f}", flush=True)
ok = True
b2, bits, nd = run([])
D = D_series(b2, b2s, NU, 1)
m0 = max(abs(D[n]) for n in NS)
print(f"(S0) A = 0: {len(nd)} explicit nodes, bits left {bits:.0f}, max |D_n| = {mp.nstr(m0, 3)}", flush=True)
ok &= m0 < mp.mpf(10)**-20
A1 = mp.mpf(1)/2
b2, bits, nd = run([(A1, L0)])
D = D_series(b2, b2s, NU, 1)
c, sl = corr_slope(D, edge_law(NS, [(A1, L0)], SHIFT))
cl = clean(NS, D, NU, ELLS, k=3, shift=SHIFT)
print(f"(S1) bits left {bits:.0f}; edge law: corr = {c:.4f}, slope = {sl:.4f}; CLEAN lines (l, amp, phase) = "
      f"{[(round(l, 3), round(a, 3), round(p, 2)) for l, a, p in cl]}", flush=True)
ok &= c <= -0.9 and -1.1 <= sl <= -0.85 and abs(cl[0][0] - float(L0)) < 0.1
lines2 = [(A1, L0), (mp.mpf(1)/4, L2)]
b2, bits, nd = run(lines2, jitter=0.15)
D = D_series(b2, b2s, NU, 1)
c, sl = corr_slope(D, edge_law(NS, lines2, SHIFT))
cl = clean(NS, D, NU, ELLS, k=3, shift=SHIFT)
print(f"(S2) bits left {bits:.0f}; edge law: corr = {c:.4f}, slope = {sl:.4f}; CLEAN lines = "
      f"{[(round(l, 3), round(a, 3), round(p, 2)) for l, a, p in cl]}", flush=True)
ok &= c <= -0.7 and abs(cl[0][0] - float(L0)) < 0.1 and abs(cl[1][0] - float(L2)) < 0.1
print("ALL SYNTHETIC CONTROLS PASSED" if ok else "SYNTHETIC CONTROLS: NOT ALL PASSED", flush=True)
