"""Discrete positive measures sigma = sum_k w_k delta_{x_k} with atoms strictly decreasing to (towards) 0."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np


def _arr(v, name):
    a = np.array(v, dtype=np.float64).ravel()
    if not np.all(np.isfinite(a)):
        raise ValueError(f"{name} must be finite")
    if not np.all(a > 0):
        raise ValueError(f"{name} must be positive")
    return a


@dataclass(frozen=True)
class DiscreteMeasure:
    atoms: np.ndarray
    weights: np.ndarray
    label: str = ""

    def __post_init__(self):
        x = _arr(self.atoms, "atoms")
        w = _arr(self.weights, "weights")
        if x.shape != w.shape:
            raise ValueError(f"atoms/weights length mismatch: {x.size} vs {w.size}")
        if x.size == 0:
            raise ValueError("measure must have at least one atom")
        if np.any(np.diff(x) >= 0):
            raise ValueError("atoms must be strictly decreasing (use DiscreteMeasure.from_atoms to sort)")
        x.setflags(write=False)
        w.setflags(write=False)
        object.__setattr__(self, "atoms", x)
        object.__setattr__(self, "weights", w)

    @classmethod
    def from_atoms(cls, x, w, tail=None, label: str = "") -> "DiscreteMeasure":
        x = _arr(x, "atoms")
        w = _arr(w, "weights")
        if x.shape != w.shape:
            raise ValueError(f"atoms/weights length mismatch: {x.size} vs {w.size}")
        if tail is not None:
            xt, wt = _arr(tail[0], "tail atoms"), _arr(tail[1], "tail weights")
            if xt.shape != wt.shape:
                raise ValueError("tail atoms/weights length mismatch")
            x, w = np.concatenate([x, xt]), np.concatenate([w, wt])
        o = np.argsort(-x, kind="stable")
        x, w = x[o], w[o]
        if np.any(np.diff(x) == 0):
            raise ValueError("duplicate atoms (merge their weights before constructing)")
        return cls(x, w, label)

    @property
    def mass(self) -> float:
        return float(np.sum(self.weights))

    @property
    def N(self) -> int:
        return int(self.atoms.size)
