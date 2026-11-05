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
import lz_synthetic as LZ
import lz2_synthetic as L2
from lz_common import *
from scipy.signal import hilbert
BES=None
def job(seed):
    u=gue_unfolded(8000,np.random.default_rng(seed))
    y=L2.series(LZ.nodes_from_u(u,False),BES)
    np.save(os.path.join(LZ.OUT,f'series_N{seed}.npy'),y); return seed
if __name__=='__main__':
    BES=LZ.comparator()
    todo=[s for s in range(1001,1021) if not os.path.exists(os.path.join(LZ.OUT,f'series_N{s}.npy'))]
    with Pool(2,initializer=globals().update,initargs=({'BES':BES},)) as P:
        for s in P.imap_unordered(job,todo): pass
    TS=LZ.TS; dif=[]
    for s in range(1001,1021):
        dif.append(np.load(os.path.join(LZ.OUT,f'series_P{s}.npy'))-np.load(os.path.join(LZ.OUT,f'series_N{s}.npy')))
    dif=np.array(dif)
    print('paired response rms per seed:',np.round(dif.std(axis=1),4))
    m=dif.mean(axis=0); print('mean response rms',m.std(),'  seed-to-seed scatter rms',(dif-m).std())
    # injected S_P sampled at T*: does the response follow S_P(T*)?  correlation and regression
    Sp=S_lines(TS)
    for lag in (-3,-2,-1,-0.5,0,0.5,1,2,3):
        Sl=S_lines(TS+lag); c=np.corrcoef(m,Sl)[0,1]; print(f'  T*+{lag:+}: corr(mean response, S_P) = {c:.3f}, slope = {np.dot(m,Sl)/np.dot(Sl,Sl):.4f}')
    # spectrum of the mean response vs T*: amplitude at prime frequencies
    am=L2.amplitudes(m); print({k:round(v[0],4) for k,v in am.items()})
