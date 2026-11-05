"""JZC_W2 data: Jacobi coefficients of sigma^{delta,kappa} (NUMERICAL).

Differences from w_common.run_measure (which is not modified): (1) atoms and masses are computed at mpmath dps 40 and handed to
the RKPW kernel as double-double pairs (hi + lo), so the measure is the intended one to ~32 digits, not its float64 rounding;
(2) the kernel is a copy of csrc/rkpw.c (Gragg-Harrod / Gautschi RKPW, binary128) whose only change is the input format
(4 doubles per atom: x_hi, x_lo, w_hi, w_lo); its source is embedded below and compiled into tmp/w2/; (3) y_n = n^p b_n/c - 1
is kept in mpmath (w_common/so_fit.sequences round it to float64, a floor of ~1e-16 absolute).
Measure: atoms 1/lam_k, masses lam_k^{-s/p}, k = 1..K (K = Kfac * nmax), lam_k = (k + d)^p + kappa, plus a continuum tail beyond
T0 = K + 1/2 + d (midpoint rule in t = k + d): int_{T0}^inf (t^p + kappa)^{-s/p} f(1/(t^p + kappa)) dt
  = (1/p) int_0^X x^{(s-1)/p - 1} (1 - kappa x)^{1/p - 1} f(x) dx,  X = 1/(T0^p + kappa)   (W2TAIL = 2, default),
by Gauss-Jacobi in x with the smooth factor (1 - kappa x)^{1/p-1} put into the weights. W2TAIL = 1 is run 1's tail (kappa dropped
in the tail, as famK / w_common): it leaves a measure error of relative size ~kappa T0^{-p} in the tail, visible as a ~1e-13 floor in
y_n (JZC_W2 Rule A item 6). The remaining (Euler-Maclaurin) tail error is measured by varying Kfac."""
import os, sys, subprocess, hashlib, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..', '..', 'second_order', 'checks'))
import numpy as np, mpmath as mp
from scipy.special import roots_jacobi
from so_coeffs import c_p_mp
from w2_common import W2C, ROOT

CSRC = r'''
/* copy of csrc/rkpw.c (QUAD) with double-double input: records (x_hi, x_lo, w_hi, w_lo) */
#include <stdio.h>
#include <stdlib.h>
#include <quadmath.h>
typedef __float128 real;
int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "rb"); fseek(f, 0, SEEK_END); long nb = ftell(f); fseek(f, 0, SEEK_SET);
    long N = nb / 32; double *xw = malloc(nb);
    if (fread(xw, 32, N, f) != (size_t)N) { fprintf(stderr, "short read\n"); return 1; }
    fclose(f);
    long M = atol(argv[2]); if (M > N) M = N;
    real *p0 = calloc(M + 1, sizeof(real)), *p1 = calloc(M + 1, sizeof(real));
    p0[0] = (real)xw[0] + (real)xw[1]; p1[0] = (real)xw[2] + (real)xw[3];
    for (long n = 1; n < N; n++) {
        real pn = (real)xw[4*n + 2] + (real)xw[4*n + 3], gam = 1, sig = 0, t = 0, xlam = (real)xw[4*n] + (real)xw[4*n + 1], rho, tmp, tsig, tk;
        long kmax = (n + 1 < M) ? n + 1 : M;
        for (long k = 0; k < kmax; k++) {
            rho = p1[k] + pn; tmp = gam * rho; tsig = sig;
            if (rho <= 0) { gam = 1; sig = 0; } else { gam = p1[k] / rho; sig = pn / rho; }
            tk = sig * (p0[k] - xlam) - gam * t;
            p0[k] = p0[k] - (tk - t); t = tk;
            if (sig <= 0) pn = tsig * p1[k]; else pn = (t * t) / sig;
            p1[k] = tmp;
        }
    }
    FILE *o = fopen(argv[3], "w"); char b1[64], b2[64];
    for (long k = 0; k < M; k++) { quadmath_snprintf(b1, sizeof b1, "%.36Qe", p0[k]); quadmath_snprintf(b2, sizeof b2, "%.36Qe", p1[k]);
        fprintf(o, "%ld %s %s\n", k, b1, b2); }
    fclose(o); return 0;
}
'''


LAST = None
TAIL = int(os.environ.get("W2TAIL", "3"))     # tail model: 1 = run 1 (pure power), 2 = exact lam, midpoint; 3 = smooth cut (default)


def kernel():
    src = os.path.join(W2C, 'rkpw_q2.c'); exe = os.path.join(W2C, 'rkpw_q2')
    if not os.path.exists(src) or open(src).read() != CSRC:
        open(src, 'w').write(CSRC)
        subprocess.run(['gcc', '-O3', '-march=native', '-o', exe, src, '-lquadmath', '-lm'], check=True)
    return exe


def gauss_jacobi_mp(n, a, b):
    """Gauss-Jacobi rule (weight (1-u)^a (1+u)^b on [-1, 1]) at mpmath dps 40: scipy's float64 rule refined by Newton on the
    three-term recurrence (float64 rules carry relative errors up to ~1e-13 at n ~ 1200, JZC_W2 Rule A item 7); cached."""
    fn = os.path.join(W2C, f"gj_{n}_{mp.nstr(mp.mpf(a), 20)}_{mp.nstr(mp.mpf(b), 20)}.txt")
    if os.path.exists(fn):
        rows = [l.split() for l in open(fn)]; return [mp.mpf(r[0]) for r in rows], [mp.mpf(r[1]) for r in rows]
    from scipy.special import roots_jacobi as rj
    u0, _ = rj(n, float(a), float(b)); a, b = mp.mpf(a), mp.mpf(b)
    def P(x):                     # P_n^{(a,b)}(x) and its derivative (DLMF 18.9.1-type recurrence, 18.9.15)
        p0, p1 = mp.mpf(1), (a + 1) + (a + b + 2)*(x - 1)/2
        for k in range(1, n):
            c1 = 2*(k + 1)*(k + a + b + 1)*(2*k + a + b); c2 = (2*k + a + b + 1)*(a*a - b*b)
            c3 = (2*k + a + b)*(2*k + a + b + 1)*(2*k + a + b + 2); c4 = 2*(k + a)*(k + b)*(2*k + a + b + 2)
            p0, p1 = p1, ((c2 + c3*x)*p1 - c4*p0)/c1
        dp = (n + a + b + 1)/2*Pd(x)
        return p1, dp
    def Pd(x):                    # P_{n-1}^{(a+1,b+1)}(x)
        A, B, m = a + 1, b + 1, n - 1
        p0, p1 = mp.mpf(1), (A + 1) + (A + B + 2)*(x - 1)/2
        if m == 0: return p0
        for k in range(1, m):
            c1 = 2*(k + 1)*(k + A + B + 1)*(2*k + A + B); c2 = (2*k + A + B + 1)*(A*A - B*B)
            c3 = (2*k + A + B)*(2*k + A + B + 1)*(2*k + A + B + 2); c4 = 2*(k + A)*(k + B)*(2*k + A + B + 2)
            p0, p1 = p1, ((c2 + c3*x)*p1 - c4*p0)/c1
        return p1
    C = 2**(a + b + 1)*mp.gamma(n + a + 1)*mp.gamma(n + b + 1)/(mp.gamma(n + a + b + 1)*mp.factorial(n))
    us, ws = [], []
    for x0 in u0:
        x = mp.mpf(x0)
        for _ in range(3):
            v, dv = P(x); x = x - v/dv
        v, dv = P(x); us.append(x); ws.append(C/((1 - x*x)*dv*dv))
    with open(fn, 'w') as fh:
        for x, w in zip(us, ws): fh.write(f"{mp.nstr(x, 38)} {mp.nstr(w, 38)}\n")
    return us, ws


def dd(x):
    hi = float(x); lo = float(x - mp.mpf(hi)); return hi, lo


def data(p, d, kap, s, nmax=1200, Kfac=100):
    """returns n (numpy int), y (list of mpf): y_n = n^p b_n / c(p) - 1, n = 1..nmax"""
    P, D, Kp, Sv = (mp.mpf(Fr.numerator)/Fr.denominator for Fr in map(__import__('fractions').Fraction, (p, d, kap, s)))
    key = hashlib.sha256(repr((str(p), str(d), str(kap), str(s), nmax, Kfac, CSRC) + ((TAIL, "gjmp") if TAIL == 3 else ((TAIL,) if TAIL != 1 else ()))).encode()).hexdigest()[:16]
    fn = os.path.join(W2C, f"data_p{p}_d{d}_k{kap}_s{s}_K{Kfac}_{key}.txt".replace('/', '|'))
    if not os.path.exists(fn):
        t0 = time.time(); K = Kfac*nmax
        with mp.workdps(40):
          recs = []
          if TAIL == 3:
            # run 3: smooth partition of unity in k (Poisson summation): atoms k <= K2 = 2K with weights w_k chi(k),
            # chi = 1 - S((k - K)/(K2 - K)) on [K, K2], S(u) = psi(u)/(psi(u) + psi(1 - u)), psi(u) = exp(-1/u) (C^infinity);
            # the complement sum_k F(k)(1 - chi(k)) is replaced by its integral (error ~ Fourier transform at 2 pi, super-small):
            # Gauss-Legendre (MGL nodes) on [K, K2] for F S, and Gauss-Jacobi in x for int_{K2}^inf F (as run 2).
            K2 = 2*K; MGL = 1600
            Sf = lambda u: mp.exp(-1/u)/(mp.exp(-1/u) + mp.exp(-1/(1 - u))) if 0 < u < 1 else (mp.mpf(0) if u <= 0 else mp.mpf(1))
            F = lambda t: ((t + D)**P + Kp)
            for k in range(1, K2):
                lam = (k + D)**P + Kp; chi = 1 - Sf(mp.mpf(k - K)/(K2 - K)) if k > K else 1
                if chi > 0: recs.append((1/lam, lam**(-Sv/P)*chi))
            gx, gw = gauss_jacobi_mp(MGL, 0, 0)
            for xi, wi in zip(gx, gw):
                t = K + (K2 - K)*(1 + xi)/2; lam = F(t)
                recs.append((1/lam, lam**(-Sv/P)*Sf((t - K)/(K2 - K))*wi*(K2 - K)/2))
            u, wu = gauss_jacobi_mp(nmax + 8, 0, (Sv - 1)/P - 1)
            X = 1/F(mp.mpf(K2)); g = lambda x: (1 - Kp*x)**(1/P - 1)
            for ui, wi in zip(u, wu):
                x = X*(1 + ui)/2
                recs.append((x, wi*(X/2)**((Sv - 1)/P)/P*g(x)))
          else:
            for k in range(1, K + 1):
                lam = (k + D)**P + Kp
                recs.append((1/lam, lam**(-Sv/P)))
            T0 = K + mp.mpf(1)/2 + D
            beta = float((Sv - 1)/P - 1); u, wu = roots_jacobi(nmax + 8, 0.0, beta)
            if TAIL == 1:                     # run 1: pure power t^p (kappa dropped in the tail), as famK
                X = T0**(-P); g = lambda x: 1
            else:                             # run 2: lam = t^p + kappa exactly: weight (1/p) x^{(s-1)/p-1} (1 - kappa x)^{1/p-1}
                X = 1/(T0**P + Kp); g = lambda x: (1 - Kp*x)**(1/P - 1)
            for ui, wi in zip(u, wu):
                x = X*(1 + mp.mpf(ui))/2
                recs.append((x, mp.mpf(wi)*(X/2)**((Sv - 1)/P)/P*g(x)))
          recs.sort(key=lambda r: -r[0])
          arr = np.array([dd(x) + dd(w) for x, w in recs], dtype='<f8')
        fin = fn + '.bin'; arr.tofile(fin)
        subprocess.run([kernel(), fin, str(nmax + 2), fn + '.tmp'], check=True); os.remove(fin); os.replace(fn + '.tmp', fn)
        print(f"   [data {os.path.basename(fn)}: {time.time() - t0:.0f}s]", flush=True)
    global LAST; LAST = fn
    rows = [l.split() for l in open(fn)]
    with mp.workdps(40):
        c = mp.mpf(c_p_mp(P))
        b = [mp.sqrt(mp.mpf(r[2])) for r in rows[1:nmax + 1]]          # beta_k = b_k^2, k = 1..nmax
        y = [mp.mpf(k)**P*b[k - 1]/c - 1 for k in range(1, nmax + 1)]
    return np.arange(1, nmax + 1), y
