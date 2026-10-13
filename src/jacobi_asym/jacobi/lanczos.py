"""Float64 Lanczos with full double reorthogonalisation (independent cross-check of RKPW; as in item 11)."""
import numpy as np
from ..measures.base import DiscreteMeasure
from .result import JacobiCoeffs


def jacobi_lanczos(mu: DiscreteMeasure, n: int) -> JacobiCoeffs:
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    x = np.asarray(mu.atoms, float)
    w = np.asarray(mu.weights, float) / mu.mass
    q = np.sqrt(w)
    Q = np.zeros((n + 1, x.size))
    Q[0] = q
    qp = np.zeros_like(q)
    A, B2, bp = [], [], 0.0
    for k in range(n):
        r = x * q
        a = q @ r
        r = r - a * q - bp * qp
        for _ in range(2):
            r -= Q[:k + 1].T @ (Q[:k + 1] @ r)
        bn = np.linalg.norm(r)
        A.append(a)
        B2.append(bn * bn)
        qp, q, bp = q, r / bn, bn
        Q[k + 1] = q
    return JacobiCoeffs(np.array(A), np.array(B2), "lanczos", "d", mu.mass)
