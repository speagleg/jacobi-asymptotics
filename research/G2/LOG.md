# G2 log

## 2026-10-13: Plan 8

- **Averaged law** (`checks/check_averaged.out`, NUMERICAL). S_n → 0 for p = 1.5, 3, 4 and 6.
  - Rule N: K-doubling changes S_n by ≤ 5.4e−4, 2.8e−5, 1.4e−6 and 7e−8 respectively. ld and q agree.
  - p = 0.5 is truncation-limited: K-doubling changes S_n by 1.1e−2 and S_n is not monotone. The atoms k^{−1/2} decay
    too slowly for K = 2·10⁵ at n ≥ 400. The theory (Part A) covers p = 0.5; the numerics do not.
- **Explicit optimizer** (`checks/check_energy.out`, NUMERICAL). μ* := ∫_0^1 ω_{[0, 4c(p)t^{−p}]} dt, in x = u^{−p}.
  - Its density equals the constraint for x ≥ 4c and is strictly below it for x < 4c. The one exception, 0.9862 at
    p = 0.5, x = 1000·4c, is quadrature error; the closed form I_{min(1,x/4c)}(1/p+½, ½) gives exactly 1.
  - Its potential is constant, log c + p, on (0, 4c) (to 1e−15) and larger beyond. These are the KKT conditions. The
    1e−15 is circular (Rule X): it plugs B0's value into the t-quadrature. B0 was checked independently by the
    reviewer's direct quadrature.
  - Monte Carlo I(μ*) = κ_p within error for p ∈ {0.5, 1, 1.5, 2, 3, 4, 6}.
  - So Route B1 is realized by superposing Weyl-law arcsine measures (in the Buyarov–Rakhmanov spirit), not by a
    Mellin transform. (Ruling, Plan 8 Task 4.)
- **Frank–Wolfe solver** (scratch, pre-plan). E_p − κ_p is +3e−4 to +6e−4 for p ∈ {1, 1.5, 2, 3, 4}. That this gap
  is discretization error was asserted without N-doubling or Richardson extrapolation. Plan Task 1 Step 2 (precision
  1e−4) was **superseded** by the exact Theorem B* and not done (Ruling). The geometric-grid saturation points underestimate u_s = (4c)^{−1/p}, because Frank–Wolfe
  does not fully converge at the saturation edge; the uniform grid came closer (0.641 vs 0.637 for p = 2).

## Rule A (adversarial pass), per lemma

- **B0.** Checked by direct quadrature, independent of the Fourier proof (reviewer `r1.py`). Edge cases: x = 0 and
  x = β (continuity by domination), and x ≫ β (monotone).
- **B\*.**
  - Degenerate p: small p (0.3, 0.5) and large p (6, 7). J(p) − (2/p)I(p) ≈ 1e−17 (reviewer).
  - Sign conventions checked against (P).
  - μ ∈ 𝒜 with I(μ) = −∞ is trivially allowed.
  - E_p < ∞ is shown in the proof.
- **A1.**
  - Excess divided by n log n stays in [−4, 1.8] (reviewer `a1.py`; explicit bound ≈ 5.4) for p ∈ {0.5, 1, 3},
    n ≤ 80, M = 4, on degenerate S: consecutive block, evens, random, geometric.
  - The cell A_1 = [0, 1/n], where g blows up, is fine because only a lower bound on the cell average is needed.
  - Isolated far points are excluded by the k ≤ Mn cap. This is why the H7 split is needed.
- **A-U.**
  - The N = 0 edge case (t = 1) is checked.
  - Only Σw < ∞ is used.
  - Uniform in m.
- **A-L.**
  - The i = 1 block (B_1 starts at 0) is handled in steps 3(a) and 3(d).
  - Near pairs (j ≤ i + 2) are handled separately (3c), because h(b) = −∞ at j = i + 2.
  - The quantile configuration of the untruncated μ* tracks κ_p within O(log n/n) (reviewer `al.py`).
- **H_all.**
  - H4's hypotheses for general p: f′ < 0 is derived.
  - The error is o(n²), not O(n log n).
- **HZ.**
  - Indexing exact to 12 digits (`check_hz.out`).
  - Prior art: Monien (p = 1, heuristic) recorded in CITATIONS (M).

## Rule R

`review/REVIEW_G2.md`: ACCEPT WITH FIXES, all fixes applied 2026-10-13. The main fixes:
- A-L step 3 written out in full (the reviewer's scheme);
- the A-L step 1 scaling formula corrected;
- A-L restated as ≥ κ_p, citation-free;
- the mutual-energy finiteness citation added;
- Monien prior art recorded, with the novelty wording narrowed.
