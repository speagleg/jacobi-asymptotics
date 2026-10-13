from dataclasses import dataclass
import mpmath as mp
import numpy as np


@dataclass(frozen=True)
class JacobiCoeffs:
    """a[i] = a_{i+1} (diagonal), b2[i] = b_{i+1}^2 (squared off-diagonal), i = 0..n-1.  Numerical, not certified.
    dtype: float64 (prec 'd'), np.longdouble ('ld'), object arrays of mpmath mpf ('q', binary128 ~ 33 digits)."""
    a: np.ndarray
    b2: np.ndarray
    method: str
    prec: str
    mass: float

    @property
    def b(self) -> np.ndarray:
        if self.b2.dtype == object:
            with mp.workdps(40):
                return np.array([mp.sqrt(v) for v in self.b2], dtype=object)
        return np.sqrt(self.b2)
