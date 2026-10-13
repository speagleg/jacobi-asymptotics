# G1 log

## 2026-10-13: Plan 9

- **Regularity numerics** (`checks/check_regularity.out`, NUMERICAL; rkpw, K vs 2K).
  - **p = 2, 3, pure power, weights k^{−s}, k^{−6} or log-periodic k^{−s}(2 + sin log k).** β_n − 1 and a_n/(2b_n) − 1
    decay like n^{−0.8} to n^{−0.95}. b_n is monotone for n ≥ 50, and ω(δ) is small (≤ 6e−4).
  - **Parity weights k^{−s}(2 + (−1)^k)** (item 11's A3). β_n and a_n/(2b_n) oscillate between consecutive n, with
    amplitude decaying like n^{−0.2} to n^{−0.8}. b_n is non-monotone at almost every step (900–1300 violations), so
    item 11's (T4) fails at the fine scale. ω(δ) ≈ 1.4e−2 to 3.7e−2 at n = 1000 and shrinks with n.
  - **Smooth ζ model.** b_n/(c(2)x_n) − 1 = −0.049 at n = 1600, decaying slowly (≈ 1/log n, as expected from
    ε(n) ~ 2/log n). a_n/(2b_n) − 1 ≈ 5e−4 (∝ 1/n). Rule N difference 5e−11.
  - **p = 1 is truncation-limited** (K = 2·10⁵): the K vs 2K difference is 3e−3 to 2e−2, and the errors grow after
    n ≈ 400. No conclusion for p = 1 at large n.
  - **Conclusion (NUMERICAL).** No non-convergence was seen. In every class tested the pointwise law looks true, with
    power-rate convergence; the parity class is the slowest.
- **Rule A, Task 2** (`checks/check_tauberian.out`).
  - Lemma K holds to 4e−13.
  - A fast-oscillating u_j = (−1)^j has G(n) = O(n), yet u_n does not tend to 0, so (T3) cannot be dropped from G1-T.
  - A slowly oscillating u_j = 1/log j has G/n² and u_n → 0 together.
  - Prop A1 on real data (p = 2, parity weights, L = 20): the minimum window average of a/(2b) is 1.0012, against the
    bound 0.9888.
- **Ruling.** Prop A1 (Task 3 material) was written together with Task 2, since it shares the window/kernel technique.
