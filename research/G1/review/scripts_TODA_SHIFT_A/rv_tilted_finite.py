"""Reviewer spot check (JZC_TODA Lemma T.A at FINITE, large tilt): b_n of sigma_tau = exp(tau x) sigma_{2,3} (infinite lattice,
p = 2, s = 3, alpha = 0; the lattice band factor vanishes at p = 2) for tau = -10, -3, +3, +10, in ball arithmetic, against the
prediction of Lemma T.A: n^p b_n/c = sum_beta e^beta B_beta(n) with e_1 = 2c mu, mu = -tau n^{-2} (layers: toda engine L1, E = 2,
KORD = 4).  Moments: m_k = sum_{k' <= K0} k'^{-s-pk} e^{tau k'^{-p}} + sum_r tau^r/r! zeta(s + p(k + r), K0 + 1) with an explicit
tail bound for r > R (|tau|^r/r! zeta(.., K0+1) <= |tau|^r/r! * 2 K0^{-(s+p(k+r))+1} for s+p(k+r) >= 2)."""
import sys, json, math
from flint import arb, fmpq, ctx
import mpmath as mp
import sympy as sp
sys.path.insert(0, '/home/claude/speagleg/jacobi-asymptotics/src')
from jacobi_asym.certify.constants import c_p
mp.mp.dps = 60
fn = sys.argv[1]; NMAX = int(sys.argv[2]); TAUS = [int(t) for t in sys.argv[3].split(',')]
P, S, K0, R = 2, 3, 1024, 160
D = json.load(open(fn)); ps, als = sp.Symbol('p'), sp.Symbol('alpha')
lay = {int(k.split(',')[0]): [mp.mpf(sp.Rational(str(sp.sympify(s, locals={'p': ps, 'alpha': als}).subs({ps: 2, als: 0})))) for s in v]
       for k, v in D['e'].items()}
cc = mp.mpf(c_p(2, 300).mid().str(70, radius=False))

def moments(tau, count):
    T = arb(tau); out = []
    for k in range(count):
        sig = S + P * k
        m = sum((arb(kk) ** (-sig) * (T * arb(kk) ** (-P)).exp() for kk in range(1, K0 + 1)), arb(0))
        tail = arb(0); fac = arb(1)
        for r in range(R + 1):
            tail += fac * arb.zeta(arb(sig + P * r), arb(K0 + 1))
            fac = fac * T / (r + 1)
        # remainder r > R: |fac_r| * zeta(sig + P r, K0+1) <= |fac_r| * 2 * K0^{-(sig + P r) + 1}, geometric in r with ratio <= 1/2
        rem = abs(fac) * 4 * arb(K0) ** (-(sig + P * (R + 1)) + 1)
        out.append(m + tail + rem * arb(0, 1))
    return out

def cheb(mom, N):
    zero = arb(0); sp_ = [zero] * (2 * N); sg = list(mom[:2 * N]); A = [mom[1] / mom[0]]; B = [mom[0]]
    for k in range(1, N):
        new = [zero] * (2 * N)
        for l in range(k, 2 * N - k): new[l] = sg[l + 1] - A[k - 1] * sg[l] - B[k - 1] * sp_[l]
        A.append(new[k + 1] / new[k] - sg[k] / sg[k - 1]); B.append(new[k] / sg[k - 1]); sp_, sg = sg, new
    return A, B

ctx.prec = 2048
for tau in TAUS:
    mom = moments(tau, 2 * NMAX + 4)
    A, B = cheb(mom, NMAX + 1)
    print(f"tau = {tau}:", flush=True)
    for n in range(6, NMAX + 1, 2):
        acc = B[n].rel_accuracy_bits()
        F = mp.sqrt(mp.mpf(B[n].mid().str(50, radius=False))) * mp.mpf(n) ** 2 / cc
        e1 = 2 * cc * (-tau) * mp.mpf(n) ** -2
        pred = sum(e1 ** b * sum(lay[b][m] * mp.mpf(n) ** -m for m in range(len(lay[b]))) for b in lay)
        unt = sum(lay[0][m] * mp.mpf(n) ** -m for m in range(len(lay[0])))
        print(f"  n={n:3d} relacc={acc:5d}  n^p b_n/c = {mp.nstr(F, 15)}  pred = {mp.nstr(pred, 15)}  (F - pred) n^5 = {mp.nstr((F - pred) * mp.mpf(n) ** 5, 6)}"
              f"  tilt effect F - B(n) = {mp.nstr(F - unt, 6)}", flush=True)
