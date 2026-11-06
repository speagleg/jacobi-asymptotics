"""Check (Rule N, NUMERICAL): exact h_n of sigma_{p,s} against
   (A) the frame expression  h_n^frame := (2pi/p) c^{2n} c^{alpha+1} n^{1-s-2pn} exp(S_n - M_n)   (Theorem 1, eq. (1.3))
   (B) Conjecture C          h_n^C     := (2pi/p) c^{2n+1} c^{alpha+1} n^{1-s} Gamma(n+1)^{-2p}.
Theorem 1 asserts h_n/h_n^frame = |(Q_1)_12|/c = 1 + O(1/n) for 1 < s < 1+2p; Conjecture C asserts h_n/h_n^C -> 1.
h_n from the exact moments m_j = zeta(s + p j) by the Chebyshev algorithm (Gautschi, Orthogonal Polynomials, Alg. 2.1)
in mpmath with working precision well above the Hankel conditioning (dps printed; result checked at two precisions).
"""
import mpmath as mp
from math import log, pi
from xn_freeform import cp, S_n, M_n


def hn_list(p, s, N, dps):
    mp.mp.dps = dps
    p = mp.mpf(p); s = mp.mpf(s)
    mom = [mp.zeta(s + p * j) for j in range(2 * N + 2)]
    # Chebyshev algorithm: sigma_{k,l}
    a = [mp.mpf(0)] * (N + 1); b = [mp.mpf(0)] * (N + 1)
    sig_prev = [mp.mpf(0)] * (2 * N + 2)
    sig = mom[:]
    a[0] = mom[1] / mom[0]; b[0] = mom[0]
    h = [mom[0]]
    for k in range(1, N + 1):
        new = [mp.mpf(0)] * (2 * N + 2)
        for l in range(k, 2 * N - k + 2):
            new[l] = sig[l + 1] - a[k - 1] * sig[l] - b[k - 1] * sig_prev[l]
        a[k] = new[k + 1] / new[k] - sig[k] / sig[k - 1]
        b[k] = new[k] / sig[k - 1]
        h.append(new[k])          # sigma_{k,k} = h_k
        sig_prev, sig = sig, new
    return h


if __name__ == "__main__":
    cases = [(0.5, 1.4), (1.0, 1.5), (1.0, 2.5), (2.0, 2.0), (2.0, 4.0), (3.0, 2.5)]
    N = 64
    for (p, s) in cases:
        c = cp(p); al = (s - 1 - p) / p
        dps = int(2 * p * N * log(N, 10) + 80)
        h1 = hn_list(p, s, N, dps)
        h2 = hn_list(p, s, N, dps + 40)
        print(f"(p,s)=({p},{s}) alpha={al:+.3f}  dps={dps}")
        mp.mp.dps = 30
        for n in [8, 16, 32, 64]:
            hn = h1[n]
            prec = abs(h1[n] / h2[n] - 1)
            S, _ = S_n(p, n); M, _ = M_n(p, n)
            lf = log(2 * pi / p) + 2 * n * log(c) + (al + 1) * log(c) + (1 - s - 2 * p * n) * log(n) + S - M
            lC = log(2 * pi / p) + (2 * n + 1) * log(c) + (al + 1) * log(c) + (1 - s) * log(n) - 2 * p * mp.loggamma(n + 1)
            rf = mp.log(hn) - lf
            rC = mp.log(hn) - lC
            print(f"  n={n:3d}  log(h/h_frame)={mp.nstr(rf, 6):>12}  n*.={mp.nstr(n * rf, 5):>9}   "
                  f"log(h/h_C)={mp.nstr(rC, 6):>12}  n*.={mp.nstr(n * rC, 5):>9}   [prec {mp.nstr(prec, 2)}]")
