"""High-precision reference: discretized Stieltjes procedure in mpmath (O(N n) mpf operations; use N <~ 2000)."""
import mpmath as mp
from ..measures.base import DiscreteMeasure


def jacobi_mp(mu: DiscreteMeasure, n: int, dps: int = 50):
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    with mp.workdps(dps):
        x = [mp.mpf(float(v)) for v in mu.atoms]
        w = [mp.mpf(float(v)) for v in mu.weights]
        N = len(x)
        p_prev = [mp.mpf(0)] * N
        p = [mp.mpf(1)] * N
        nrm_prev = None
        nrm = mp.fsum(w)
        a, b2 = [], []
        for k in range(n):
            ak = mp.fsum(w[i] * x[i] * p[i] ** 2 for i in range(N)) / nrm
            a.append(ak)
            if nrm_prev is None:
                p_next = [(x[i] - ak) * p[i] for i in range(N)]
            else:
                r = nrm / nrm_prev
                p_next = [(x[i] - ak) * p[i] - r * p_prev[i] for i in range(N)]
            nrm_next = mp.fsum(w[i] * p_next[i] ** 2 for i in range(N))
            b2.append(nrm_next / nrm)
            p_prev, p, nrm_prev, nrm = p, p_next, nrm, nrm_next
        return a, b2
