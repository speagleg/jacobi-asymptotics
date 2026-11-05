"""CARLITZ_PENNER: the Hankel determinants of the Tricomi–Carlitz measure as Barnes G-function products, and the comparison with
the Penner (Laguerre) partition function.  Exact identities checked in mpmath (40 digits).  NUMERICAL check of exact algebra.

Measure (y-image, as in JZC_P1 (C)): nodes 1/(k+a), masses (k+a)^{k-1} e^{-k}/k!, total mass e^a/a; S-fraction (Carlitz)
coefficients beta_j = j/((j+a-1)(j+a)), b_n^2 = beta_{2n-1} beta_{2n}.
 (H1) H_N = m0^N prod_{k<N} (b_k^2)^{N-k} equals the Hankel determinant of the moments (accurate moments: direct sum + Euler–Maclaurin tail).
 (H2) H_N = m0^N [Gamma(a)Gamma(a+1)]^{N-1} prod_{k=1}^{N-1} (2k)!/(Gamma(2k+a)Gamma(2k+a+1)), and by Gauss duplication
      log H_N = log G(N+1/2) + log G(N+1) - log G(N+a/2) - 2 log G(N+(a+1)/2) - log G(N+a/2+1) + elementary(N) + const.
 Penner: the Penner model is a Laguerre (complex Wishart) Hankel determinant G(N+1)G(N+alpha+1)/G(alpha+1) (quoted, not
 re-derived here).  So Carlitz = "Gaussian over two Laguerres" on the doubled lattice: same Barnes-G family, not the same object."""
import os, hashlib
import mpmath as mp
print(f"sha256 {os.path.basename(__file__)}: {hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}", flush=True)
mp.mp.dps = 40
ok = True
for a in (mp.mpf('0.3'), mp.mpf('0.7'), mp.mpf(1)):
    beta = lambda j: j/((j + a - 1)*(j + a)); m0 = mp.e**a/a
    rec = lambda N: N*mp.log(m0) + mp.fsum((N - k)*(mp.log(beta(2*k - 1)) + mp.log(beta(2*k))) for k in range(1, N))
    def bar(N):
        def lp(c):
            e = mp.fsum((2*k + c - 1) for k in range(1, N))*mp.log(2) - (N - 1)*mp.log(mp.pi)/2
            gg = lambda d: mp.log(mp.barnesg(N + d)) - mp.log(mp.barnesg(1 + d))
            return e + gg(c/2) + gg((c + 1)/2)
        return N*mp.log(m0) + (N - 1)*(mp.loggamma(a) + mp.loggamma(a + 1)) + lp(1) - lp(a) - lp(a + 1)
    w = lambda k: mp.exp(-k + (k - 1)*mp.log(k + a) - mp.loggamma(k + 1))
    S = lambda f: mp.fsum(f(k) for k in range(60)) + mp.nsum(f, [60, mp.inf], method='euler-maclaurin')
    mom = [S(lambda k, j=j: w(k)*(k + a)**(-j)) for j in range(16)]
    e1 = max(abs(mp.log(mp.det(mp.matrix([[mom[i + j] for j in range(N)] for i in range(N)]))) - rec(N)) for N in (3, 5, 8))
    e2 = max(abs(rec(N) - bar(N)) for N in (5, 20, 60))
    print(f"a = {a}: (H1) |log det(moments) - recurrence| <= {mp.nstr(e1, 3)};  (H2) |recurrence - Barnes G| <= {mp.nstr(e2, 3)}", flush=True)
    ok &= e1 < 1e-20 and e2 < 1e-30
print("ALL PASSED" if ok else "NOT ALL PASSED")
