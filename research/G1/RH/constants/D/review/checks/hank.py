# Rule R reviewer's own Hankel/LDL code (no cglib). Moments m_k = zeta(s + p k) of sigma_{p,s} = sum_k k^-s delta_{k^-p}.
# LDL^T of the Hankel matrix (m_{i+j}): pivots are h_k; first column of L^{-1} gives P_k(0); lambda_m = 1/sum_{k<m} P_k(0)^2/h_k.
import mpmath as mp
def run(p, s, n, dps):
    mp.mp.dps = dps
    p = mp.mpf(p); s = mp.mpf(s)
    mom = [mp.zeta(s + p*k) for k in range(2*n)]
    # LDL^T: M = L D L^T, L unit lower.  Standard O(n^3).
    L = [[mp.mpf(0)]*n for _ in range(n)]
    Dg = [mp.mpf(0)]*n
    for i in range(n):
        for j in range(i+1):
            acc = mom[i+j]
            for k in range(j):
                acc -= L[i][k]*L[j][k]*Dg[k]
            if i == j:
                Dg[i] = acc; L[i][i] = mp.mpf(1)
            else:
                L[i][j] = acc/Dg[j]
    # P_k(0) = (L^{-1})_{k,0}: solve L y = e_0
    y = [mp.mpf(0)]*n
    for i in range(n):
        acc = mp.mpf(1) if i == 0 else mp.mpf(0)
        for k in range(i):
            acc -= L[i][k]*y[k]
        y[i] = acc
    lam = []; K = mp.mpf(0); logD = []; ld = mp.mpf(0)
    for m in range(n):
        K += y[m]**2/Dg[m]; lam.append(1/K)      # lam[m] = lambda_{m+1}
        ld += mp.log(Dg[m]); logD.append(ld)     # logD[m] = log D_{m+1}
    return Dg, y, lam, logD
def cfun(p):
    p = mp.mpf(p)
    I = mp.sqrt(mp.pi)/2*mp.gamma(1/p+mp.mpf(1)/2)/mp.gamma(1/p+1)
    return (mp.pi/(2*I))**p/4
