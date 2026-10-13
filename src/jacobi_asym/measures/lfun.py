"""Measures from L-function zero ordinates gamma (taken as REAL numbers on the critical line: an input, not
evidence; item 11 E1).  sigma = sum_j 2 x_j delta_{x_j}, x_j = 1/(gamma_j^2 + 1/4), plus a smooth
Riemann-von Mangoldt tail beyond the last tabulated ordinate (ported from math-pursuits item 11 measures.py)."""
from pathlib import Path
import numpy as np
from scipy.special import lambertw
from .base import DiscreteMeasure

CONST = {1: 7 / 8, 4: 1 / 8, 3: 1 / 8}
DATA_ROOT = Path(__file__).resolve().parents[3] / "data" / "raw"


class DataMissing(FileNotFoundError):
    pass


def Nsmooth(T, q=1):
    T = np.asarray(T, float)
    return T / (2 * np.pi) * np.log(q * T / (2 * np.pi * np.e)) + CONST[q]


def Ninv(N, q=1):
    y = (np.asarray(N, float) - CONST[q]) * q / np.e
    return 2 * np.pi * np.e / q * np.exp(lambertw(y).real)


def model_zeros(J, q=1, j0=1):
    return Ninv(np.arange(j0, J + 1) - 0.5, q)


def tail_nodes(Tstart, q=1, Tend=1e18, ratio=1.05, k=6):
    u0, u1 = np.log(Tstart), np.log(Tend)
    edges = np.arange(u0, u1 + np.log(ratio), np.log(ratio))
    t, wt = np.polynomial.legendre.leggauss(k)
    U, W = [], []
    for a, b in zip(edges[:-1], edges[1:]):
        U.append((a + b) / 2 + (b - a) / 2 * t)
        W.append((b - a) / 2 * wt)
    U, W = np.concatenate(U), np.concatenate(W)
    T = np.exp(U)
    dens = np.log(q * T / (2 * np.pi)) / (2 * np.pi) * T
    return T, W * dens


def _atoms(g, mult=None):
    x = 1 / (np.asarray(g, float) ** 2 + 0.25)
    return x, (2 * x if mult is None else 2 * x * mult)


def merge_repeats(gammas, idx):
    """Synthetic double zeros: gamma[k+1] := gamma[k] for k in idx (0-based, non-adjacent)."""
    g = np.array(gammas, float, copy=True)
    idx = np.sort(np.asarray(idx, int))
    if idx.size and (np.any(np.diff(idx) < 2) or idx[-1] + 1 >= g.size):
        raise ValueError("idx must be non-adjacent and < len(gammas) - 1")
    g[idx + 1] = g[idx]
    return g


def zero_measure(gammas, q=1, tail=True, label="", **tailkw) -> DiscreteMeasure:
    g = np.asarray(gammas, float)
    x, w = _atoms(g)
    t = None
    if tail:
        T, m = tail_nodes(Ninv(len(g) + 0.5, q), q, **tailkw)
        t = _atoms(T, m)
    return DiscreteMeasure.from_atoms(x, w, tail=t, label=label or f"zero_measure(q={q}, M={len(g)}, tail={tail})")


def smooth_zeta(J, q=1, tail=True) -> DiscreteMeasure:
    return zero_measure(model_zeros(J, q), q, tail, label=f"smooth_zeta(J={J}, q={q})")


def load_odlyzko(M=None, root=None) -> np.ndarray:
    f = Path(root or DATA_ROOT) / "zeta_zeros_odlyzko6.npy"
    if not f.exists():
        raise DataMissing(f"{f} not found: run `.venv/bin/python data/fetch.py odlyzko`")
    g = np.load(f)
    return g if M is None else g[:M]


def true_zeta(M=None, tail=True) -> DiscreteMeasure:
    return zero_measure(load_odlyzko(M), 1, tail, label=f"true_zeta(M={M}, tail={tail})")
