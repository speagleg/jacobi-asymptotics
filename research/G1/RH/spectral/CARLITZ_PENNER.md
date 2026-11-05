# CARLITZ–PENNER: is the Carlitz measure a Penner model?

Status (2026-10-28): **NOT REVIEWED**. Labels: the identities are exact algebra checked numerically (`checks/carlitz_penner.py`,
ALL PASSED). The Penner–Laguerre identification is quoted, not re-derived, so it is subject to Rule C. Novelty: UNCHECKED, and
probably KNOWN in substance (Barnes-G evaluations of Hankel determinants are classical).

**Question.**
- The Tricomi–Carlitz measure's Toda times are B_j = ζ(−j, a)/j, i.e. the Binet coefficients of log Γ.
- The Penner model's free energy is also a log Γ series, whose coefficients Harer–Zagier read as χ(M_{g,1}) = ζ(1 − 2g).
- Is the Carlitz Jacobi matrix a Penner model in disguise?

**Result.**
- **(H1)** The Hankel determinants of the moments equal m₀^N ∏_{k<N}(b_k²)^{N−k} built from the Carlitz coefficients
  β_j = j/((j+a−1)(j+a)). Agreement is ≤ 1.3·10⁻²⁴ for a = 0.3, 0.7, 1.
- **(H2)** By Gauss duplication,

  log H_N = log G(N+½) + log G(N+1) − log G(N+a/2) − 2 log G(N+(a+1)/2) − log G(N+a/2+1) + elementary(N) + const,

  agreeing to ≤ 4·10⁻³⁷.
- The Penner (complex Wishart / Laguerre) partition function is G(N+1)G(N+α+1)/G(α+1).
- So Carlitz is "Gaussian over two Laguerres" on the doubled lattice. It is in the same Barnes-G family as Penner, but it is not
  the same object.
- Its large-N coefficients are the Harer–Zagier Bernoulli numbers deformed into Bernoulli polynomials at the shifts a/2,
  (a+1)/2, …, the same ζ(−j, ·) structure as its Toda times.

**Reading.** The parallel is real but generic. Any measure whose recurrence coefficients are rational in n has Barnes-G Hankel
determinants, hence a "genus expansion" with Bernoulli coefficients. There is no hidden Penner model.
