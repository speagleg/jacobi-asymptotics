# Plan 10 (RH) log

## Phase 0: fine numerics (`checks/check_fine.out`, NUMERICAL)

- **Method.** Atoms beyond K are replaced by an Euler–Maclaurin Gauss–Legendre tail. Without the tail, the fits are
  truncation-dominated: d₁ moves from −1.27 to −0.70 between K and 2K, because about n²/K zeros of P_n lie below
  K^{−p}. With the tail, every case is stable to 4 digits under K-doubling.
- **Exact anchor.** Lommel ν = ½ is exactly σ_{2,2} up to scale, since j_{½,k} = kπ. Its fit gives d = (−0.5, 0.3125)
  and e = (1, 0.625), which the closed forms confirm.
- **Fitted first-order corrections**, for (p, s) ∈ {(2, 2), (2, 3), (2, 4), (2, 6), (3, 3), (3, 4), (3, 6),
  (1.5, 1.5), (1.5, 3)}:

    n^p b_n/c(p) = 1 − (s−1)/(2n) + O(n⁻²),   a_n/(2b_n) = 1 + p/(2n) + O(n⁻²).

  So d₁ = −(s−1)/2 is independent of p, and e₁ = p/2 is independent of s, to 4 digits in all 9 cases. The O(n⁻²)
  coefficients depend on both p and s.
- **Gate 0: GO.** The corrections have the form 1 + c/n + O(n⁻²), with no log terms and no oscillation. The RH analysis
  must reproduce d₁ = −(s−1)/2 and e₁ = p/2. Equivalently, b_n ≈ c(p)(n + (s−1)/(2p))^{−p}.

## Phase 1: interpolation problem → RHP (RH.md §1–3)

- **Option (i), symmetrization, chosen.** WLXZ's origin parametrix is elementary when the accumulation point is
  interior to the band (their (6.24)–(6.28), read).
- **Lemma 1.1, checked to 30 digits** (`checks/check_phase1.out`): θ(±Z_k) = πk; Π′(±Z_k) = (−1)^k; residues cancel;
  the nodes are the only zeros of sin θ off the cut (argument principle 280.000 = 280 for p = 1, 2, 3); the decay
  sectors match WLXZ.
- **Band.** r* = 2^{1+q}√c(p) reproduces WLXZ's (−2, 2) at p = 1, a consistency check of the scaling.
- **Gate 1: GO for p ≥ 1.** For p < 1, θ is real on extra rays, which is deferred. Open for Phase 2: the
  saturated-region sign conventions.
