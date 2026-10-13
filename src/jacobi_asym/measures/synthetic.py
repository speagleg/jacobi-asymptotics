"""Synthetic unfolded point processes with the zeta counting function (ported from item 11 synth.py)."""
import numpy as np
from .lfun import Ninv, zero_measure


def synthetic_unfolded(kind: str, J: int, seed: int, m: int = 1000) -> np.ndarray:
    rng = np.random.default_rng(seed)
    if kind == "smooth":
        return np.arange(1, J + 1) - 0.5
    if kind == "poisson":
        return np.cumsum(rng.exponential(1.0, J)) - 0.5
    if kind == "jitter":
        return np.arange(1, J + 1) - 0.5 + rng.uniform(-0.5, 0.5, J)
    if kind == "cue":
        us = []
        for blk in range(-(-J // m)):
            Z = (rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))) / np.sqrt(2)
            Qm, R = np.linalg.qr(Z)
            d = np.diag(R)
            Qm = Qm * (d / np.abs(d))
            th = np.sort(np.mod(np.angle(np.linalg.eigvals(Qm)), 2 * np.pi))
            us.append(blk * m + m * th / (2 * np.pi))
        return np.sort(np.concatenate(us))[:J]
    raise ValueError(f"unknown kind {kind!r}")


def synthetic_zeta(kind: str, J: int, seed: int):
    u = synthetic_unfolded(kind, J, seed)
    u = u[u > 0.05]
    return zero_measure(Ninv(u), 1, True, label=f"synthetic_zeta({kind}, J={J}, seed={seed})")
