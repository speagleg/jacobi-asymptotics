"""RKPW (Gragg-Harrod / Gautschi) via the compiled kernels in csrc/build (double, long double, binary128)."""
import os
import subprocess
import tempfile
from pathlib import Path
import mpmath as mp
import numpy as np
from ..measures.base import DiscreteMeasure
from .result import JacobiCoeffs

BIN_DIR = Path(__file__).resolve().parents[3] / "csrc" / "build"
_EXE = {"d": "rkpw_d", "ld": "rkpw_ld", "q": "rkpw_q"}


class KernelMissing(RuntimeError):
    pass


def jacobi_rkpw(mu: DiscreteMeasure, n: int, prec: str = "d") -> JacobiCoeffs:
    if prec not in _EXE:
        raise ValueError(f"prec must be one of {sorted(_EXE)}")
    if not 1 <= n < mu.N:
        raise ValueError(f"need 1 <= n < N = {mu.N} (b_N = 0); got n = {n}")
    exe = Path(BIN_DIR) / _EXE[prec]
    if not exe.exists():
        raise KernelMissing(f"{exe} not found: run `make -C csrc` in the repo root")
    with tempfile.TemporaryDirectory() as td:
        fin, fout = os.path.join(td, "atoms.bin"), os.path.join(td, "out.txt")
        np.stack([mu.atoms, mu.weights], 1).astype("<f8").tofile(fin)
        subprocess.run([str(exe), fin, str(n + 1), fout], check=True)
        if prec == "q":
            # binary128 output (36 digits) is parsed to mpf: np.longdouble would round it to 64 bits
            with mp.workdps(40):
                rows = [l.split() for l in open(fout) if l.strip()]
                alpha = np.array([mp.mpf(r[1]) for r in rows], dtype=object)
                beta = np.array([mp.mpf(r[2]) for r in rows], dtype=object)
        else:
            dt = np.float64 if prec == "d" else np.longdouble
            d = np.loadtxt(fout, dtype=dt, ndmin=2)
            alpha, beta = d[:, 1], d[:, 2]
    return JacobiCoeffs(a=alpha[:n].copy(), b2=beta[1:n + 1].copy(), method="rkpw", prec=prec, mass=float(beta[0]))
