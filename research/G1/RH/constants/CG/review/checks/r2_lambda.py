"""Rule R review R2 of CG.md §9 (Theorem C), independent numerics. NUMERICAL (Rule N.2), Arb ball arithmetic (python-flint).

lambda_m(0; sigma_{1,s}) = 1 / (H_m^{-1})_{00}, H_m = [zeta(s+i+j)]_{i,j<m} (exact moments of sigma_{1,s}).
All m <= M at once: H = L L^T (Cholesky in arb), y = L^{-1} e_0, K_m(0,0) = sum_{k<m} y_k^2.
Compared with Theorem C:  C1 = Gamma(s-1)Gamma(s)(9/2)^{s-1},  r_m := lambda_m m^{3(s-1)} / C1  (claim: r_m = 1 + O(1/m)).
Richardson in 1/m (polynomial extrapolation in h = 1/m on m = M-K..M) estimates lim r_m.
Usage: r2_lambda.py s M prec_bits
"""
import sys
from flint import arb, ctx

def run(s_str, M, prec):
    ctx.prec = prec
    s = arb(s_str)
    mom = [(s + j).zeta() for j in range(2 * M - 1)]
    L = [[arb(0)] * M for _ in range(M)]
    for i in range(M):
        for j in range(i + 1):
            acc = mom[i + j]
            Li, Lj = L[i], L[j]
            for k in range(j):
                acc -= Li[k] * Lj[k]
            if i == j:
                L[i][i] = acc.sqrt()
            else:
                L[i][j] = acc / L[j][j]
    y = [arb(0)] * M
    for k in range(M):
        acc = arb(1) if k == 0 else arb(0)
        for i in range(k):
            acc -= L[k][i] * y[i]
        y[k] = acc / L[k][k]
    lam, K = [], arb(0)
    for m in range(1, M + 1):
        K += y[m - 1] ** 2
        lam.append(1 / K)
    return lam

def richardson(ms, vals, K):
    # Neville extrapolation to h = 0 with nodes h = 1/m
    hs = [arb(1) / m for m in ms[-(K + 1):]]
    P = list(vals[-(K + 1):])
    n = len(hs)
    for lev in range(1, n):
        for i in range(n - lev):
            P[i] = (hs[i] * P[i + 1] - hs[i + lev] * P[i]) / (hs[i] - hs[i + lev])
    return P[0]

if __name__ == "__main__":
    s_str, M, prec = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    lam = run(s_str, M, prec)
    ctx.prec = prec
    s = arb(s_str); z = s - 1
    C1 = z.gamma() * s.gamma() * (arb(9) / 2) ** z
    r = [lam[m - 1] * arb(m) ** (3 * z) / C1 for m in range(1, M + 1)]
    ms = list(range(1, M + 1))
    print(f"s={s_str} M={M} prec={prec} bits")
    print("  max rel radius of lambda_m:", max((x.rad() / abs(x.mid())) for x in lam).str(3, radius=False))
    for m in (10, 20, 40, 80, M):
        if m <= M:
            print(f"  m={m:4d}  r_m-1 = {(r[m-1]-1).mid().str(8, radius=False)}   m(r_m-1) = {(m*(r[m-1]-1)).mid().str(8, radius=False)}")
    for Kr in (4, 8, 12, 16, 20):
        lim = richardson(ms, r, Kr)
        print(f"  Richardson K={Kr:2d}: lim r_m - 1 = {(lim-1).mid().str(5, radius=False)}  (ball radius {lim.rad().str(2, radius=False)})")
    # 1/m coefficient estimate: Richardson applied to m(r_m - 1)
    t = [m * (r[m-1] - 1) for m in ms]
    print("  Richardson K=12 of m(r_m-1) (1/m coefficient):", richardson(ms, t, 12).mid().str(8, radius=False),
          "  F7 prediction for r_m normalised with m, -3*zeta^2/2:", (-3 * z * (z / 2)).str(8, radius=False))
    print("  lambda_M mid (for precision-doubling comparison):", lam[-1].mid().str(40, radius=False))
