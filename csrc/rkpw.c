/* Item 11 — Jacobi (recurrence) coefficients of a discrete measure  mu = sum_i w_i delta_{x_i}
 * by the RKPW algorithm (Rutishauser; Kahan; Pal; Walker; Gragg & Harrod, Numer. Math. 44 (1984) 317-335),
 * in the form of W. Gautschi's OPQ routine RKPW.m ("Orthogonal Polynomials: Computation and Approximation",
 * OUP 2004, §2.2.3).  Atoms are added one at a time and the bulge is chased down with plane rotations.
 *
 * Only the leading M coefficients are kept: the update at row k depends only on rows < k (the chase runs
 * top-down), so truncating the chase at row M leaves alpha_0..alpha_{M-1}, beta_0..beta_{M-1} exact
 * (verified numerically against Lanczos, see LOG.md).
 *
 * Output convention (monic recurrence  p_{k+1} = (x - alpha_k) p_k - beta_k p_{k-1}):
 *   alpha_k  (k = 0..M-1)  -> "a_{k+1}" in item-11 notation (diagonal of the Jacobi matrix),
 *   beta_0 = mu(R), beta_k = b_k^2 (k >= 1)  (b_k = off-diagonal).
 *
 * Build:  gcc -O3 -march=native -o rkpw_d   rkpw.c -lm                (double)
 *         gcc -O3 -march=native -DLD  -o rkpw_ld rkpw.c -lm            (long double, 64-bit mantissa)
 *         gcc -O3 -march=native -DQUAD -o rkpw_q rkpw.c -lquadmath -lm (__float128, 113-bit mantissa)
 * Usage:  rkpw_X  atoms.bin  M  out.txt
 *   atoms.bin: little-endian float64 pairs (x_i, w_i), i = 1..N, in the order they are to be added.
 *   out.txt:   lines "k alpha_k beta_k" with 20 significant digits.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#ifdef QUAD
#include <quadmath.h>
typedef __float128 real;
#define FMT(buf, v) quadmath_snprintf(buf, sizeof buf, "%.21Qe", v)
#elif defined(LD)
typedef long double real;
#define FMT(buf, v) snprintf(buf, sizeof buf, "%.21Le", v)
#else
typedef double real;
#define FMT(buf, v) snprintf(buf, sizeof buf, "%.17e", v)
#endif

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s atoms.bin M out.txt\n", argv[0]); return 1; }
    FILE *f = fopen(argv[1], "rb");
    if (!f) { perror("atoms"); return 1; }
    fseek(f, 0, SEEK_END); long nb = ftell(f); fseek(f, 0, SEEK_SET);
    long N = nb / 16;
    double *xw = malloc(nb);
    if (fread(xw, 16, N, f) != (size_t)N) { fprintf(stderr, "short read\n"); return 1; }
    fclose(f);
    long M = atol(argv[2]);
    if (M > N) M = N;
    real *p0 = calloc(M + 1, sizeof(real)), *p1 = calloc(M + 1, sizeof(real));
    p0[0] = xw[0]; p1[0] = xw[1];
    for (long n = 1; n < N; n++) {
        real pn = xw[2 * n + 1], gam = 1, sig = 0, t = 0, xlam = xw[2 * n], rho, tmp, tsig, tk;
        long kmax = (n + 1 < M) ? n + 1 : M;   /* rows 0..kmax-1 */
        for (long k = 0; k < kmax; k++) {
            rho = p1[k] + pn; tmp = gam * rho; tsig = sig;
            if (rho <= 0) { gam = 1; sig = 0; }
            else { gam = p1[k] / rho; sig = pn / rho; }
            tk = sig * (p0[k] - xlam) - gam * t;
            p0[k] = p0[k] - (tk - t); t = tk;
            if (sig <= 0) pn = tsig * p1[k];
            else pn = (t * t) / sig;
            p1[k] = tmp;
        }
        if (n + 1 <= M) { /* new row n gets initialised on first touch: rows beyond n were zero */ }
    }
    FILE *o = fopen(argv[3], "w");
    char b1[64], b2[64];
    for (long k = 0; k < M; k++) { FMT(b1, p0[k]); FMT(b2, p1[k]); fprintf(o, "%ld %s %s\n", k, b1, b2); }
    fclose(o);
    return 0;
}
