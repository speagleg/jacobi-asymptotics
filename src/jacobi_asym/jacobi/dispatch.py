import numpy as np
from ..measures.base import DiscreteMeasure
from .result import JacobiCoeffs
from .rkpw import jacobi_rkpw
from .lanczos import jacobi_lanczos
from .mp import jacobi_mp


def jacobi_coeffs(mu: DiscreteMeasure, n: int, method: str = "rkpw", prec: str = "d", dps: int = 50) -> JacobiCoeffs:
    if method == "rkpw":
        return jacobi_rkpw(mu, n, prec)
    if method == "lanczos":
        return jacobi_lanczos(mu, n)
    if method == "mp":
        a, b2 = jacobi_mp(mu, n, dps)
        return JacobiCoeffs(np.array([float(v) for v in a]), np.array([float(v) for v in b2]), "mp", f"dps{dps}", mu.mass)
    raise ValueError(f"unknown method {method!r}; use 'rkpw', 'lanczos' or 'mp'")
