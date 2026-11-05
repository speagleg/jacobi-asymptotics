"""LS_BOLZA §4: the registered Bolza run (B1)-(B4).  Written and committed with the pre-registration, before the data was read.
NUMERICAL.  Usage: python -B ls_bolza.py <path to eig-bolza-refined0-1000.txt>  (sha256-checked against bolzakit's pin)."""
import os, sys, hashlib, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import mpmath as mp
import numpy as np
from ls_common import *
SU_SHA256 = "869f48bcc1403cd2ae722b9c7d8ae94e016a4030a353d49c68ce5e6eb4520345"     # bolzakit/spectral/eigen.py
for f in (__file__, os.path.join(HERE, 'ls_common.py')):
    print(f"sha256 {os.path.basename(f)}: {hashlib.sha256(open(f, 'rb').read()).hexdigest()}", flush=True)
path = sys.argv[1]
h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
print(f"sha256 data: {h} ({'MATCHES' if h == SU_SHA256 else 'DOES NOT MATCH'} bolzakit's pin)", flush=True)
assert h == SU_SHA256
mp.mp.dps = 60
lam = sorted(mp.mpf(x) for x in open(path).read().split())
# distinct eigenvalues (bolzakit's clustering rule: relative tolerance 1e-9, cluster mean)
cl = []
for x in lam:
    if cl and abs(x - cl[-1][-1]) <= mp.mpf('1e-9')*x: cl[-1].append(x)
    else: cl.append([x])
dist = [(sum(c)/len(c), len(c)) for c in cl]
print(f"{len(lam)} eigenvalues, {len(dist)} distinct; max = {mp.nstr(lam[-1], 8)}; multiplicities "
      f"{dict(sorted({m: sum(1 for _, mm in dist if mm == m) for _, m in dist}.items()))}", flush=True)
LCUT, S, PREC = 900, 2, int(os.environ.get('LS_PREC', 11000))
# smooth parameters: least squares N_dist(lambda) = nu*lambda - a - 1/2 on [50, 900] (sampled at the midpoints between nodes)
xs = [float(l) for l, _ in dist]
grid = np.linspace(50, LCUT, 4000)
Nd = np.searchsorted(np.array(xs), grid, side='right').astype(float)
nu_f, c_f = np.polyfit(grid, Nd, 1)
nu_f, c_f = float(nu_f), float(c_f)
NU = mp.mpf(repr(nu_f)); A = mp.mpf(repr(-c_f - 0.5))
print(f"smooth fit: nu = {nu_f:.6f}, a = {float(A):.6f}  (N_dist = nu*lambda - a - 1/2)", flush=True)
NMAX = min(300, int(1.2*nu_f*LCUT)); NS = list(range(40, NMAX))
SHIFT = float(1 + A)                       # N - n = alpha/2 - Z(0); alpha = 0, Z(0) = zeta(0, 1 + a) = -1/2 - a
print(f"fit range n in [40, {NMAX}); natural-index shift {SHIFT:.4f}", flush=True)
below = [(l, m) for l, m in dist if l < LCUT]
K = int(mp.ceil(NU*LCUT - A))               # first lattice index of the tail, (K + a)/nu >= lambda_cut
b2s, bs = b2_series([], [], NU, A, 1, S, NMAX, PREC)
b21, b1 = b2_series([l for l, _ in below], [1]*len(below), NU, A, K, S, NMAX, PREC)
b22, bm = b2_series([l for l, _ in below], [m for _, m in below], NU, A, K, S, NMAX, PREC)
print(f"bits left: comparator {bs:.0f}, M1 {b1:.0f}, M2 {bm:.0f}", flush=True)
D1 = D_series(b21, b2s, NU, 1); D2 = D_series(b22, b2s, NU, 1)

# N_osc from the data and its edge transform E[N_osc]
xa = np.array(xs)
def Nosc(L):
    return float(np.searchsorted(xa, L, side='right')) - (nu_f*L - float(A) - 0.5)
def E(n):
    ls = (n + SHIFT)/(2*nu_f)
    f = lambda u: Nosc(u*ls)
    f1 = Nosc(ls - 1e-12)
    # piecewise-constant integrand: integrate on a fine grid of u with the finite part at u = 1
    us = np.linspace(0, 1, 20001)[:-1]; du = us[1] - us[0]
    vals = np.array([(f(u) - f1)/(1 - u)**1.5 for u in us + du/2])
    return 0.5*(float(np.sum(vals)*du) - 2*f1)
EN = {n: E(n) for n in NS}
Y = np.array([float(D1[n]) for n in NS]); X = np.array([EN[n] for n in NS])
corr = float(np.corrcoef(X, Y)[0, 1]); slope = float(np.dot(X, Y)/np.dot(X, X))
print(f"(B1) edge law: corr(D_n, E[N_osc]) = {corr:.4f}, slope = {slope:.4f}   [registered: corr <= -0.6, slope in [-1.3, -0.6]]",
      flush=True)
ELLS = [1 + 0.005*i for i in range(1400)]
c1 = clean(NS, D1, nu_f, ELLS, k=5, shift=SHIFT)
cE = clean(NS, {n: mp.mpf(EN[n]) for n in NS}, nu_f, ELLS, k=5, shift=SHIFT)
c2 = clean(NS, D2, nu_f, ELLS, k=5, shift=SHIFT)
fmt = lambda c: [(round(l, 3), round(a, 3), round(p, 2)) for l, a, p in c]
print(f"CLEAN D_n (M1):   {fmt(c1)}", flush=True)
print(f"CLEAN E[N_osc]:   {fmt(cE)}", flush=True)
print(f"CLEAN D_n (M2):   {fmt(c2)}", flush=True)
LSYS = 2*float(mp.acosh(1 + mp.sqrt(2)))
B1 = corr <= -0.6 and -1.3 <= slope <= -0.6
B2 = any(abs(l - LSYS) <= 0.12 for l, _, _ in c1)
B3 = all(any(abs(l - q) <= 0.12 for q, _, _ in cE) for l, _, _ in c1[:3])
B4 = all(any(abs(l - q) <= 0.12 for q, _, _ in c2[:3]) for l, _, _ in c1[:3])
for k, v in (('B1', B1), ('B2', B2), ('B3', B3), ('B4', B4)): print(f"({k}) {'PASS' if v else 'FAIL'}", flush=True)
import json
os.makedirs(os.path.join(HERE, '..', '..', '..', '..', '..', 'tmp'), exist_ok=True)
json.dump(dict(nu=nu_f, a=float(A), nmax=NMAX, D1={n: float(D1[n]) for n in NS}, D2={n: float(D2[n]) for n in NS}, E=EN),
          open(os.path.join(HERE, '..', '..', '..', '..', '..', 'tmp', 'ls_bolza.json'), 'w'))
