"""Rule N check for C.md §R (rate of Theorem C).
Prediction: log(h_n/ThmC) = e/n - 2 sum_{j: jp<=1-} eps_j n^{-jp}/(jp) + o(1/n),
  e = d1 + d1^2 - 2 d2, d1 = -(s-1)/2, d2 = (p+1)(s-1)^2/(8p) - (p+2)(s-1-p)^2/(8p^2) + (p+1)/12,
  eps_j = binom(2j,j) p c^j zeta(-jp)  (j <= floor(1/p) for p<1; j = 1 for 1<p<2; negligible for p >= 2).
Printed: R_n = n*(log(h_n/ThmC) + 2 sum eps_j n^{-jp}/(jp)) which should tend to e.
h_n from the Chebyshev algorithm on exact moments zeta(s+jp) (cglib), precision-doubling check."""
import sys, mpmath as mp
sys.path.insert(0, __file__.rsplit('/', 3)[0] + '/CG/checks')
from cglib import recurrence, c_of_p

def run(p, s, n, dps):
    mp.mp.dps = dps
    p = mp.mpf(p); s = mp.mpf(s); c = c_of_p(p)
    al, be = recurrence(p, s, n)
    logh = [mp.log(be[0])]
    for k in range(1, n + 1): logh.append(logh[-1] + mp.log(be[k]))
    d1 = -(s - 1) / 2
    d2 = (p + 1) * (s - 1) ** 2 / (8 * p) - (p + 2) * (s - 1 - p) ** 2 / (8 * p ** 2) + (p + 1) / 12
    e = d1 + d1 ** 2 - 2 * d2
    J = int(mp.floor(1 / p)) if p < 1 else (1 if p < 2 else 0)
    eps = [mp.binomial(2 * j, j) * p * c ** j * mp.zeta(-j * p) for j in range(1, J + 1)]
    out = {}
    for k in range(1, n + 1):
        lC = mp.log(2 * mp.pi / p) + (2 * k + 1) * mp.log(c) + (s - 1) * (mp.log(c) / p - mp.log(k)) - 2 * p * mp.loggamma(k + 1)
        L = logh[k] - lC + 2 * sum(eps[j - 1] * mp.mpf(k) ** (-j * p) / (j * p) for j in range(1, J + 1))
        out[k] = k * L
    return e, out

def fit(vals, ns, gams):
    """Solve vals[n] = e + sum_g a_g n^{-g} exactly on the given points; return e."""
    A = mp.matrix([[1] + [mp.mpf(k) ** (-g) for g in gams] for k in ns])
    return mp.lu_solve(A, mp.matrix([vals[k] for k in ns]))[0]

if __name__ == '__main__':
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 80
    cases = [(2, 3, [1, 2, 3, 4]), (3, 2.5, [1, 2, 3, 4]), (2.5, 4, [1, 1.5, 2, 2.5, 3]), (1.5, 2, [0.5, 1, 1.5, 2, 2.5]),
             (0.7, 1.6, [0.4, 0.7, 0.8, 1, 1.1, 1.2, 1.4])]
    for (p, s, g) in cases:
        e, o1 = run(p, s, n, 1200)
        _, o2 = run(p, s, n, 2000)
        dd = max(abs(o1[k] - o2[k]) for k in range(n // 2, n + 1))
        ns = [n - 3 * i for i in range(len(g), -1, -1)]
        print(f"(p,s)=({p},{s}) predicted e={mp.nstr(e,12)}  R_n:",
              '  '.join(f"{k}:{mp.nstr(o2[k],9)}" for k in (n // 4, n // 2, n)),
              f"| extrap(exps {g}) {mp.nstr(fit(o2, ns, g),9)} | dps-diff {mp.nstr(dd,3)}", flush=True)
