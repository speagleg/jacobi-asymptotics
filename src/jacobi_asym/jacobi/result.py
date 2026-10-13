from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class JacobiCoeffs:
    """a[i] = a_{i+1} (diagonal), b2[i] = b_{i+1}^2 (squared off-diagonal), i = 0..n-1.  Numerical, not certified."""
    a: np.ndarray
    b2: np.ndarray
    method: str
    prec: str
    mass: float

    @property
    def b(self) -> np.ndarray:
        return np.sqrt(self.b2)
