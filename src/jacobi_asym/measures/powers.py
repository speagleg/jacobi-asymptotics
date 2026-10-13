"""Pure-power model measures: atoms C k^{-p}, weights k^{-s} (or the atoms themselves)."""
import numpy as np
from .base import DiscreteMeasure


def pure_power(p: float, K: int, s: float | None = None, C: float = 1.0) -> DiscreteMeasure:
    k = np.arange(1, K + 1, dtype=np.float64)
    x = C * k ** (-float(p))
    w = x.copy() if s is None else k ** (-float(s))
    return DiscreteMeasure(x, w, label=f"pure_power(p={p}, K={K}, s={s}, C={C})")
