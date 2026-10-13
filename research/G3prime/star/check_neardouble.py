"""G3'* probe (NUMERICAL): add a near-duplicate atom next to every m-th smooth atom, at ordinate gap r * (local mean
spacing), and measure the own-normalized shift.  Theory: only gaps ~ exp(-c n) should break the own-normalized law."""
import numpy as np
from jacobi_asym.measures.base import DiscreteMeasure
from jacobi_asym.measures.lfun import Ninv, _atoms, model_zeros, tail_nodes
from jacobi_asym.jacobi.dispatch import jacobi_coeffs
from jacobi_asym.laws.averaged import averaged_law

J, m = 200_000, 4
NS = [250, 500, 1000, 2000, 4000]
g0 = model_zeros(J)
sp = np.diff(g0, append=g0[-1] + (g0[-1] - g0[-2]))


def S_own(g, prec="d"):
    x, w = _atoms(np.sort(g))
    T, mm = tail_nodes(Ninv(J + 0.5))
    mu = DiscreteMeasure.from_atoms(x, w, tail=_atoms(T, mm))
    b = jacobi_coeffs(mu, max(NS), prec=prec).b
    return averaged_law(np.asarray(b, float), mu.atoms, 2, NS)


base = S_own(g0)
print(f"m={m} (extra atom next to every {m}th), n: {NS}")
for r in (0.5, 1e-1, 1e-2, 1e-3, 1e-5):
    extra = g0[::m] + r * sp[::m]
    s = S_own(np.concatenate([g0, extra]))
    s_ld = S_own(np.concatenate([g0, extra]), prec="ld")
    print(f"r={r:7.0e}  own-norm shift (d):  " + " ".join(f"{s[n]-base[n]:+.4f}" for n in NS))
    print(f"           own-norm shift (ld): " + " ".join(f"{s_ld[n]-base[n]:+.4f}" for n in NS))
