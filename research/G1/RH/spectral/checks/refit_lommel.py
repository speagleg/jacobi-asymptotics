"""REFIT: an exact test of the corrected generator (and SPEC §3.10's Lommel row). Bessel-zero measure lam_k = (j_{mu,k}/pi)^2, s = 2
(refit_data.fam_bessel at P = 2: 300 exact zeros at dps 45, McMahon beyond), against the exact closed form of spec_lommel.py
(Lommel polynomials, Dickinson 1954 / Van Assche 1996 §3 as quoted there): n^2 b_n/c = 4n^2/((2n+mu) sqrt((2n+mu)^2 - 1)), c = pi^2/16.
spec_lommel.out (float64 zeros, pure-power tail) agrees to 1.6e-15 / 5.8e-16; here: n <= 40, K = 40000 and 4000. NUMERICAL."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mpmath as mp
import refit_data as RD, w2_common as W2C_
for f in (__file__, RD.__file__): W2C_.provenance(f)
for mu in (0, 1.5):
    for K in (4000, 40000):
        n, y = RD.run(f"lommel_mu{mu}_K{K}", 2, RD.fam_bessel(mu, 2, 2), K, nmax=40)
        with mp.workdps(40):
            M = mp.mpf(mu); worst = max(abs((1 + y[k - 1]) - 4*mp.mpf(k)**2/((2*k + M)*mp.sqrt((2*k + M)**2 - 1))) for k in range(1, 41))
        print(f"mu={mu} K={K}: max_n<=40 |n^2 b_n/c - closed form| = {mp.nstr(worst, 3)}", flush=True)
