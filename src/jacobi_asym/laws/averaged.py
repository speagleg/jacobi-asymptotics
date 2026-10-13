"""Averaged (doubly-Cesaro, geometric) Law-P statistic of PROOF.md Thm H / H_L."""
import numpy as np
from .weyl import c_p


def averaged_law(b, x, p: float, ns) -> dict:
    b = np.asarray(b, float)
    x = np.asarray(x, float)
    lj = np.log(b / x[: b.size])
    lc = np.log(c_p(p))
    out = {}
    for n in ns:
        if n < 2 or n - 1 > b.size:
            raise ValueError(f"need 2 <= n <= len(b) + 1 = {b.size + 1}; got {n}")
        j = np.arange(1, n)
        out[int(n)] = float(2 / n ** 2 * np.sum((n - j) * lj[: n - 1]) - lc)
    return out
