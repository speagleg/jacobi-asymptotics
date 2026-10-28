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
import sys,os,math; sys.path.insert(0,HERE)
import numpy as np
from multiprocessing import Pool
import lz_synthetic as LZ, lz2_synthetic as L2
from lz_common import *
BES=None
L=math.log(2)
def nodes(u,eps):
    y=np.asarray(u[:LZ.K])-0.5; T=np.array([Nbar_inv(float(max(v,0.2))) for v in y])
    for _ in range(40):
        f=T/(2*np.pi)*np.log(T/(2*np.pi))-T/(2*np.pi)+7/8+eps*np.sin(L*T)-y; T=T-f/(np.log(T/(2*np.pi))/(2*np.pi))
    return np.sort(T)
def job(a):
    bg,eps=a
    u=np.arange(1,LZ.K+1,dtype=float) if bg=='lat' else gue_unfolded(8000,np.random.default_rng(7))
    return bg,eps,L2.series(nodes(u,eps),BES)
if __name__=='__main__':
    BES=LZ.comparator()
    jobs=[(bg,e) for bg in ('lat','gue') for e in (0,0.005,0.02,0.05,0.1,0.2,0.4)]
    with Pool(2,initializer=globals().update,initargs=({'BES':BES},)) as P:
        R={(b,e):y for b,e,y in P.imap_unordered(job,jobs)}
    for bg in ('lat','gue'):
        ref=(R[(bg,0.005)]-R[(bg,0)])/0.005
        print(f'background {bg}: linear-response rms per unit eps = {ref.std():.3f}; amplitude at log2 per unit eps = {L2.amplitudes(ref)["log2"][0]:.3f}')
        for e in (0.02,0.05,0.1,0.2,0.4):
            r=(R[(bg,e)]-R[(bg,0)])/e
            print(f'   eps={e}: corr(response, linear response) = {np.corrcoef(r,ref)[0,1]:.3f}, rms ratio = {r.std()/ref.std():.2f}, log2 amplitude per unit eps = {L2.amplitudes(r)["log2"][0]:.3f}')
