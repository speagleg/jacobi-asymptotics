"""CERTIFIED recurrence coefficients and Hankel determinants from exactly known moments.

Moments m_j of sigma_{p,s} = sum_k k^{-s} delta_{k^{-p}} are zeta(s + p j).  Arb's zeta is rigorous (the Euler-
Maclaurin tail is bounded inside Arb), so the moment balls contain the exact moments; for even integer arguments a
second, independent enclosure is zeta(2m) = (-1)^{m+1} B_{2m} (2 pi)^{2m} / (2 (2m)!) with exact Bernoulli numbers.
The Chebyshev algorithm and the determinants below use only ball operations, so every returned ball contains the exact
coefficient / determinant of the measure.  The problem is badly conditioned (D_n ~ exp(-p n^2 log n)); insufficient
precision only widens the balls, it never makes them wrong.  `adaptive` doubles the precision until a target accuracy
is met."""
from flint import arb, arb_mat, ctx, fmpq


def zeta_moments(p, s, count):
    """Balls for m_j = zeta(s + p j), j < count.  p, s exact rationals (fmpq) or ints."""
    P, S = arb(fmpq(p) if not isinstance(p, fmpq) else p), arb(fmpq(s) if not isinstance(s, fmpq) else s)
    return [arb.zeta(S + P * j) for j in range(count)]


def zeta_even_bernoulli(m):
    """zeta(2m), m >= 1, from the exact Bernoulli number (independent of arb.zeta)."""
    B = fmpq.bernoulli(2 * m)
    sign = 1 if m % 2 == 1 else -1
    return sign * arb(B) * (2 * arb.pi()) ** (2 * m) / (2 * arb.fac_ui(2 * m))


def chebyshev(mom, n):
    """Chebyshev algorithm (Gautschi, Orthogonal Polynomials, Alg. 2.1) in ball arithmetic.
    Returns (a_0..a_{n-1}, B_0..B_{n-1}) with x P_k = P_{k+1} + a_k P_k + B_k P_{k-1}, B_k = b_k^2 (k >= 1), B_0 = m_0.
    Needs len(mom) >= 2n."""
    if len(mom) < 2 * n:
        raise ValueError("need 2n moments")
    zero = arb(0)
    sig_prev = [zero] * (2 * n)          # sigma_{-1, l}
    sig = list(mom[:2 * n])              # sigma_{0, l}
    A = [mom[1] / mom[0]]
    B = [mom[0]]
    for k in range(1, n):
        new = [zero] * (2 * n)
        for l in range(k, 2 * n - k):
            new[l] = sig[l + 1] - A[k - 1] * sig[l] - B[k - 1] * sig_prev[l]
        if new[k].contains(0):
            raise ArithmeticError(f"sigma_{k},{k} ball contains 0; increase precision")
        A.append(new[k + 1] / new[k] - sig[k] / sig[k - 1])
        B.append(new[k] / sig[k - 1])
        sig_prev, sig = sig, new
    return A, B


def hankel_det(mom, n, shift=0):
    """det (m_{i+j+shift})_{0<=i,j<n} as a ball (arb_mat.det: rigorous)."""
    if n == 0:
        return arb(1)
    return arb_mat([[mom[i + j + shift] for j in range(n)] for i in range(n)]).det()


def adaptive(fn, accurate, start_bits=256, max_bits=1 << 16):
    """Run fn() at increasing precision until accurate(result) holds.  Returns (result, bits)."""
    old = ctx.prec
    bits = start_bits
    try:
        while True:
            ctx.prec = bits
            try:
                res = fn()
                if accurate(res):
                    return res, bits
            except ArithmeticError:
                pass
            if bits >= max_bits:
                raise ArithmeticError(f"target accuracy not reached at {bits} bits")
            bits *= 2
    finally:
        ctx.prec = old


def rel_bits_ok(target_bits):
    """accuracy predicate: every ball in a (nested) list has >= target_bits relative accuracy."""
    def ok(res):
        stack = [res]
        while stack:
            x = stack.pop()
            if isinstance(x, (list, tuple)):
                stack.extend(x)
            elif x.rel_accuracy_bits() < target_bits:
                return False
        return True
    return ok
