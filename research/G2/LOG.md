# G2 log

## 2026-10-13: Plan 8

- **Averaged law** (`checks/check_averaged.out`, NUMERICAL). S_n → 0 for p = 1.5, 3, 4 and 6.
  - Rule N: K-doubling changes S_n by ≤ 5.4e−4, 2.8e−5, 1.4e−6 and 7e−8 respectively. ld and q agree.
  - p = 0.5 is truncation-limited: K-doubling changes S_n by 1.1e−2 and S_n is not monotone. The atoms k^{−1/2} decay
    too slowly for K = 2·10⁵ at n ≥ 400. The theory (Part A) covers p = 0.5; the numerics do not.
- **Explicit optimizer** (`checks/check_energy.out`, NUMERICAL). μ* := ∫_0^1 ω_{[0, 4c(p)t^{−p}]} dt, in x = u^{−p}.
  - Its density equals the constraint for x ≥ 4c and is strictly below it for x < 4c.
  - Its potential is constant, log c + p, on (0, 4c) (to 1e−15) and larger beyond. These are the KKT conditions.
  - Monte Carlo I(μ*) = κ_p within error for p ∈ {0.5, 1, 1.5, 2, 3, 4, 6}.
  - So Route B1 is realized by superposing Weyl-law arcsine measures (in the Buyarov–Rakhmanov spirit), not by a
    Mellin transform. (Ruling, Plan 8 Task 4.)
- **Frank–Wolfe solver** (scratch, pre-plan). E_p − κ_p is +3e−4 to +6e−4 for p ∈ {1, 1.5, 2, 3, 4}, which is
  discretization error. The geometric-grid saturation points underestimate u_s = (4c)^{−1/p}, because Frank–Wolfe
  does not fully converge at the saturation edge; the uniform grid came closer (0.641 vs 0.637 for p = 2).
