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
from scipy.signal import hilbert
a=0.3; KT=30000; NMAX=1200
lam=np.arange(1,KT)+a
xK=1/(KT-0.5+a); xq,wq=tail_quadrature(xK,1.0,400)
def bcoef(lams):
    x=np.concatenate([1/lams,xq]); w=np.concatenate([lams**-2.0,wq]); return lanczos(x,w,NMAX)
al0,be0=bcoef(lam)
res={}
for om in (0.6,1.0,1.6):
    eps=0.02; kk=np.arange(1,KT); h=eps*np.sin(om*kk)*(kk<2500)       # displacement in lambda (unit density)
    _,be=bcoef(lam+h)
    n=np.arange(1,NMAX); D=n*n*(np.sqrt(be[1:])-np.sqrt(be0[1:]))/0.5
    res[om]=D
# zero-count table Z(n, y_k) = # zeros of P_n above y_k (continuous), k <= 2500
K=2500; y=1/lam[:K]
Ztab=np.zeros((NMAX,K))
for m in range(20,NMAX):
    z=np.sort(eigvalsh_tridiagonal(al0[:m],np.sqrt(be0[1:m])))
    Ztab[m]=m-np.interp(y,z,np.arange(1,m+1),left=0,right=m)

for om,D in res.items():
    ns=np.arange(1,NMAX); sel=(ns>=150)&(ns<1150)
    an=hilbert(D[sel]-np.mean(D[sel])); ph=np.unwrap(np.angle(an)); fi=np.gradient(ph)   # measured inst. freq (rad per n)
    pred=[]
    for m in ns[sel]:
        dZk=2*np.pi*np.gradient(Ztab[m])          # phase per node (rad/node), as function of k
        # stationary node: 2 pi dZ/dk = om (take the in-band root with the largest amplitude region: nearest to the edge)
        idx=np.where(np.diff(np.sign(np.abs(dZk)-om))!=0)[0]
        if len(idx)==0: pred.append(np.nan); continue
        k=idx[-1]
        pred.append(2*np.pi*(Ztab[m+1,k]-Ztab[m,k]) if m+1<NMAX else np.nan)
    pred=np.array(pred)
    ok=np.isfinite(pred)
    q=lambda v: np.nanmedian(v)
    print(f'omega={om}: measured inst. freq (median, |.|) {q(np.abs(fi)):.3f} rad/n; predicted 2pi dZ/dn at k* (median) {q(np.abs(pred[ok])):.3f}; '
          f'corr(meas,pred) over n = {np.corrcoef(np.abs(fi[ok]),np.abs(pred[ok]))[0,1]:.3f}; rms D = {D[sel].std():.3f}')
