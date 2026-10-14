# Plan 34: density-one pointwise law for slowly varying weights (Lemma TC, Theorem T3-avg)

## Tasks
- [x] **T1.** Lemma TC (from G2 A-U/A-L).
- [x] **T2.** Theorem T3-avg (b and a), via averaged tail counts and Fubini.
- [x] **T3.** Numerics `research/G1/checks/check_sv_density`.
- [x] **T4.** Rule R review.

## Review focus
- Lemma TC: uniformity of the A-U/A-L constants over the sandwich class; the probability bound and the expectation.
- T3-avg step 3: the telescoping inequality Σ_{n=N}^{2N}(μ_n + μ_{n−1})(A) ≤ 2𝔼_{2N+1}#(A) (check the index range);
  the effective M in Lemma TC; uniformity in t; the Fubini step.
- Step 1: δ_N → 0 by the uniform convergence theorem (Ψ bounded, slowly varying).
- Step 5: the a_n analogue with FVa and the uniform a/b bounds.
- Density-one conclusion.
