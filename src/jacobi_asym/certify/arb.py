"""CERTIFIED (ball-arithmetic) computations.  Atoms/weights are taken as the exact binary64 values given; every
operation is an Arb ball operation, so the returned balls contain the exact Jacobi coefficients of that measure."""
from flint import arb, ctx
from ..measures.base import DiscreteMeasure


def certified_jacobi(mu: DiscreteMeasure, n: int, prec_bits: int = 256):
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    old = ctx.prec
    ctx.prec = prec_bits
    try:
        x = [arb(float(v)) for v in mu.atoms]
        w = [arb(float(v)) for v in mu.weights]
        N = len(x)
        p_prev = [arb(0)] * N
        p = [arb(1)] * N
        nrm = sum(w, arb(0))
        nrm_prev = None
        A, B2 = [], []
        for _ in range(n):
            if nrm.contains(0):
                raise ArithmeticError("norm ball contains 0; increase prec_bits")
            ak = sum((w[i] * x[i] * p[i] * p[i] for i in range(N)), arb(0)) / nrm
            A.append(ak)
            if nrm_prev is None:
                p_next = [(x[i] - ak) * p[i] for i in range(N)]
            else:
                r = nrm / nrm_prev
                p_next = [(x[i] - ak) * p[i] - r * p_prev[i] for i in range(N)]
            nrm_next = sum((w[i] * p_next[i] * p_next[i] for i in range(N)), arb(0))
            B2.append(nrm_next / nrm)
            p_prev, p, nrm_prev, nrm = p, p_next, nrm, nrm_next
        return A, B2
    finally:
        ctx.prec = old


def certified_cp(p: int, prec_bits: int = 256):
    old = ctx.prec
    ctx.prec = prec_bits
    try:
        P = arb(p)
        I = arb.pi().sqrt() / 2 * arb.gamma(1 / P + arb(1) / 2) / arb.gamma(1 / P + 1)
        return (arb.pi() / (2 * I)) ** P / 4
    finally:
        ctx.prec = old
