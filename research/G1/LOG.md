# G1 log

## 2026-10-13: Plan 9

- **Regularity numerics** (`checks/check_regularity.out`, NUMERICAL; rkpw, K vs 2K).
  - **p = 2, 3, pure power, weights k^{−s}, k^{−6} or log-periodic k^{−s}(2 + sin log k).** β_n − 1 and a_n/(2b_n) − 1
    decay like n^{−0.8} to n^{−0.95}. b_n is monotone for n ≥ 50, and ω(δ) is small (≤ 6e−4).
  - **Parity weights k^{−s}(2 + (−1)^k)** (item 11's A3). β_n and a_n/(2b_n) oscillate between consecutive n, with
    amplitude decaying. (The exponents n^{−0.2} to n^{−0.8} come from fitting 6 samples of an oscillating sequence and
    are unreliable. The reviewer's envelope run gives max consecutive |Δβ| over [m, m+100] of 6.0e−2, 4.2e−2, 3.0e−2,
    2.1e−2 and 1.9e−2 at m = 200…1900, about n^{−0.5}, stable for K = 60k, 240k and 480k.) b_n is non-monotone at
    almost every step (900–1300 violations). That is step-to-step behaviour, **not** a failure of item 11's (T4),
    which is a δn-scale condition. ω(δ) was reported only at n = 1000; its shrinking with n is supported by the
    envelope run, not by check_regularity itself.
  - **Smooth ζ model.** b_n/(c(2)x_n) − 1 = −0.049 at n = 1600, decaying slowly (≈ 1/log n, as expected from
    ε(n) ~ 2/log n). a_n/(2b_n) − 1 ≈ 5e−4 (∝ 1/n). Rule N difference 5e−11.
  - **p = 1 is truncation-limited** (K = 2·10⁵): the K vs 2K difference is 3e−3 to 2e−2, and the errors grow after
    n ≈ 400. No conclusion for p = 1 at large n.
  - **p = 2 and 3 are also truncation-limited at large n.** The K vs 2K differences (≈ 5e−4) are comparable to the
    n = 1600 errors, so the fitted exponents −0.80 to −0.95 are biased. The true exponent for pure powers is −1:
    Plan 10 Phase 0, with a quadrature tail, finds d₁ = −(s−1)/2 exactly.
  - **Conclusion (NUMERICAL).** No non-convergence was seen. In every class tested the pointwise law looks true, with
    power-rate convergence; the parity class is the slowest.
- **Rule A, Task 2** (`checks/check_tauberian.out`).
  - Lemma K holds to 4e−13.
  - A fast-oscillating u_j = (−1)^j has G(n) = O(n), yet u_n does not tend to 0, so (T3) cannot be dropped from G1-T.
  - A slowly oscillating u_j = 1/log j has G/n² and u_n → 0 together.
  - Prop A1 on real data (p = 2, parity weights, L = 20): the minimum window average of a/(2b) is 1.0012, against the
    bound 0.9888.
- **Ruling.** Prop A1 (Task 3 material) was written together with Task 2, since it shares the window/kernel technique.
- **Task 3 (a_n side).** A1 (window lower bound) is PROVED. A2 (Heine tail identity, p > 1) is PROVED. A3
  (Q_p = 2c(p)/(p−1)) is PROVED by a cancellation argument and checked numerically to 8 digits. A4 is conditional on
  the concentration lemma (CL). The tail sums of a_j converge to Q_p numerically (`checks/check_tailsum.out`).
  - **Missing lemma (CL):** saturation exactness of the Heine ensemble. Single-atom exclusions in the saturated
    region must be rare enough that the u^{−p}-weighted deficit vanishes. This is invisible to n²-speed large
    deviations.
- **Task 4 (G1-R, time-boxed).**
  - Literature read (CITATIONS.md): BKMM, where RH pointwise asymptotics need finite node sets; WLXZ, where accumulating
    nodes are handled only for Tricomi–Carlitz.
  - The windowed-energy attempt shows that energy methods control only window averages (o(n²)/h²), not (T3).
  - Stop report in PROOF.md §4: GAP with precise missing statements (T3) and (CL), and a suggested RH project for pure
    powers with power weights. "As hard as an open problem" is **not** claimed.
- **Rule R** (`review/REVIEW_G1.md`): ACCEPT WITH FIXES, all applied. Main fixes:
  - A4's density claim withdrawn (counterexample), replaced by block-Cesàro and window-average statements;
  - the "(T4) fails" claim retracted;
  - G1-L inequality indices fixed;
  - A2 index shifted to Σ_{j>n};
  - A3 relabelled PROVED;
  - BKMM analyticity and saturation quotes added;
  - numerics truncation caveats added;
  - check_tauberian's "slow" test is only a sanity check, not a test of G1-T.
