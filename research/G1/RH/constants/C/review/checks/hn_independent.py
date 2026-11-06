"""Rule R independent check (NUMERICAL): h_n of sigma_{p,s} from exact moments zeta(s+pj),
computed as the pivots of Gaussian elimination (no pivoting) of the Hankel matrix [m_{i+j}]
(pivot k = D_{k+1}/D_k = h_k). Independent of C/checks (no Chebyshev algorithm, no shared code).
Compares with (C): h_n^C = (2pi/p) c^{2n+1} (c^{1/p}/n)^{s-1} Gamma(n+1)^{-2p}.
Run at two precisions; reports |log h(dps1) - log h(dps2)|.
Usage: python hn_independent.py p s N
"""
import sys
import mpmath as mp


def hankel_pivots(p, s, N, dps):
    mp.mp.dps = dps
    p = mp.mpf(p); s = mp.mpf(s)
    m = [mp.zeta(s + p * j) for j in range(2 * N + 1)]
    A = [[m[i + j] for j in range(N + 1)] for i in range(N + 1)]
    piv = []
    for k in range(N + 1):
        pk = A[k][k]
        piv.append(pk)
        for i in range(k + 1, N + 1):
            f = A[i][k] / pk
            if f == 0:
                continue
            Ai = A[i]; Ak = A[k]
            for j in range(k + 1, N + 1):
                Ai[j] -= f * Ak[j]
    return piv


def logC(p, s, n):
    p = mp.mpf(p); s = mp.mpf(s)
    I = mp.sqrt(mp.pi) / 2 * mp.gamma(1 / p + mp.mpf(1) / 2) / mp.gamma(1 / p + 1)
    c = (mp.pi / (2 * I)) ** p / 4
    return (mp.log(2 * mp.pi / p) + (2 * n + 1) * mp.log(c) + (s - 1) * (mp.log(c) / p - mp.log(n))
            - 2 * p * mp.loggamma(n + 1))


if __name__ == "__main__":
    p = float(sys.argv[1]); s = float(sys.argv[2]); N = int(sys.argv[3])
    dps = int(2 * p * N * mp.log10(N) + 2 * N * 0 + 120)
    h1 = hankel_pivots(p, s, N, dps)
    h2 = hankel_pivots(p, s, N, dps + 60)
    mp.mp.dps = 30
    print(f"(p,s)=({p},{s})  dps={dps},{dps+60}")
    prev = None
    for n in [4, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160, 192, 256]:
        if n > N:
            break
        r = mp.log(h1[n]) - logC(p, s, n)
        prec = abs(mp.log(h1[n]) - mp.log(h2[n]))
        print(f"  n={n:4d}  log(h_n/h_n^C)={mp.nstr(r, 8):>14}  n*.={mp.nstr(n*r, 6):>10}  n^p*.={mp.nstr(n**p*r, 6):>10}  [prec {mp.nstr(prec, 2)}]")
