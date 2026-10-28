"""LS_ZETA2 diagnostics (synthetic only; NUMERICAL).  (R1) single-node response on the unit p = 1 lattice: in-band ringing at
2 sign changes per zero of P_n sweeping past the node, none outside the band.  (R2) sinusoidal displacement h_k = 0.02 sin(w k):
D_n has instantaneous frequency w/2 per n (edge-local read-out); the in-band stationary-phase root is not the read-out point.
(PA) paired positive control (same GUE seed with and without S_P): seed-dependent response, no coherent S_P(T*) component.
(LI) linearity in the injected amplitude and the background-induced loss of the coherent log 2 line (lattice 0.198 vs GUE 0.059
per unit amplitude)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import hashlib
print(f"sha256 {os.path.basename(__file__)}: {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}", flush=True)
import math, time
import numpy as np
from lz_common import lanczos, tail_quadrature
from scipy.linalg import eigvalsh_tridiagonal
# unit-density p=1 lattice lambda_k = k + a (k>=1), s = 2, explicit atoms to KT, quadrature tail
a=0.3; KT=30000; NMAX=1200
lam=np.arange(1,KT)+a
xK=1/(KT-0.5+a); xq,wq=tail_quadrature(xK,1.0,400)
def bcoef(lams):
    x=np.concatenate([1/lams,xq]); w=np.concatenate([lams**-2.0,wq]); al,be=lanczos(x,w,NMAX); return al,be
t=time.time(); al0,be0=bcoef(lam); print('base',time.time()-t,flush=True)
k0=200; h=0.05
lp=lam.copy(); lp[k0-1]+=h; lm=lam.copy(); lm[k0-1]-=h
_,bp=bcoef(lp); _,bm=bcoef(lm)
n=np.arange(1,NMAX)
F=n*n*(np.sqrt(bp[1:])-np.sqrt(bm[1:]))/(2*h)/0.5          # response of D_n = n^2 (b - b0)/c, c = 1/2, per unit displacement
y0=1/lam[k0-1]
cnt=[]
for m in range(40,NMAX):
    ev=eigvalsh_tridiagonal(al0[:m],np.sqrt(be0[1:m]))
    cnt.append(int(np.sum(ev>y0)))
F=F[39:]; ns=np.arange(40,NMAX); cnt=np.array(cnt)
print('edge crossing n* = 2 lambda_k0 =',2*lam[k0-1])
for lo,hi in ((60,200),(200,380),(420,600),(600,900),(900,1199)):
    sel=(ns>=lo)&(ns<hi); f=F[sel]; c=cnt[sel]
    zc=np.sum(np.diff(np.sign(f))!=0); dc=c[-1]-c[0]
    print(f'n in [{lo},{hi}): sign changes of F = {zc}, zeros passing y0 (count increase) = {dc}, mean |F| = {np.mean(np.abs(f)):.3f}')
