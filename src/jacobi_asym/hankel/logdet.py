"""log D_n via H2: D_n = m_0^n prod_{j<n} b_j^{2(n-j)} (item 11 PROOF.md Lemma H2)."""
import numpy as np
from ..jacobi.result import JacobiCoeffs


def log_hankel(jc: JacobiCoeffs, n: int) -> float:
    b2 = np.asarray(jc.b2, float)
    if n < 1 or n - 1 > b2.size:
        raise ValueError(f"need 1 <= n <= len(b2) + 1 = {b2.size + 1}; got {n}")
    j = np.arange(1, n)
    return float(n * np.log(jc.mass) + np.sum((n - j) * np.log(b2[: n - 1])))
