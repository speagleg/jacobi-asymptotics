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

## Phase 2: g-function and signs (RH.md §4)

- **Density.** ψ matches WLXZ (2.1) at p = 1 to 10 digits, and g′ matches WLXZ (4.2) in the right half-plane.
- **Variational conditions.** Equality on the band to 7e−13; strict inequality on the saturated part.
- **Lens signs.** Re φ < 0 over the band, by an exact identity. Re φ̃ < 0 on the saturated part (checked for
  p = 1, 2, 3).
- **Bug found and fixed.** The node-density normalization in the check was off by a factor 2: (1/q)|x|^{−1−1/q}, not
  half of it. The ratio ψ/constraint is now exactly 1 on the saturated part.
- **Gate 2: GO.**
- **Structural finding (RH.md §5).** The origin is regular iff r = 1 + p/2 (α = 0); otherwise there is a Fisher–Hartwig
  |z|^{2α} singularity at 0, which needs a Bessel parametrix. Ruling: Phases 3–5 are done first on the regular family
  r = 1 + p/2, then extended.

## Phase 3: R-jumps, D-functions, global parametrix (RH.md §6)

- **End-to-end check** (actual OPs, N = 24): the poles are removed (|U₁₂| ~ 1/dist; R bounded). The band weight is
  exactly the constant −2πi/p on the regular family (Lemma 3.1).
- **D-functions for p = 2.** The jump identity holds to 1e−26 on the right; normalization |DE| → 1/√(2πN); D̃ − 1 = O(1/N).
  The left side needs mirrored functions (as WLXZ).
- **Scope finding.** The WLXZ D-function construction needs t(z) single-valued in ℂ±. In the symmetric variable that
  holds iff 2/p ∈ ℤ (p = 1, 2). General p needs option (ii) (x-variable, edge parametrix) or a sectorial D.
- **Gate 3: GO for p ∈ {1, 2}**; general p deferred. The new content for p ∈ {1, 2} is the pointwise law for weights
  r ≠ 1 + p/2, which needs the Bessel/Fisher–Hartwig origin parametrix. This covers Haynes–Zudilin a = 2 and
  Monien a = 1.

## Phase 4: local parametrices (RH.md §7)

- **Airy edges.** Square-root vanishing proved, with an explicit constant √(r*² − x²)/(πq r*²) (numerics match for
  p = 1, 2, 3).
- **Origin.** A regular interior point, ψ(0) = 1/(πr*(q+1)). KV §5 (read) is the local problem, with Fisher–Hartwig
  exponent α = (2r − 2 − p)/(2p): structure verified, prefactor bookkeeping pending.
- **Top end.** The saturated jump is exponentially small uniformly up to k_N (raw entry 3e−14 at N = 160), so no
  parametrix is needed.
- **First run of the top-end check (recorded honestly).** Taking the sup over [1.05r*, k_N] grew with N, because the
  sup sat inside the would-be Airy disc and the raw entry carries polynomial N-factors. Restricting to a fixed disc
  complement gives clean exponential decay.
- **Gate 4: GO for p ∈ {1, 2}.** Phase 5 (bookkeeping, small norm, extraction, acceptance test against Phase 0's
  d₁ and e₁) is next.

## Phase 5: assembly and acceptance (RH.md §8)

- **Test A (outer strong asymptotics, p = 2, r = 2 and 3, N up to 240).** No exponential drift; the ratios converge
  at O(1/N); |T₁₁| ∝ 1/N. The g-function and RH structure are confirmed.
- **Test B (extraction).** The leading γ_N² = c(N/2)^{−p} is confirmed. The corrections are (k₀ + k₁(−1)^N)/N with
  k₁ = 0 iff α = 0 (the Bessel/Fisher–Hartwig signature).
- **Lemma 5.1 (unfolding).** e₁ = p/2 for every weight, and d₁ = (p/2 + k₀)/2. This explains Phase 0 exactly.
- **Status.** Theorem RH for p ∈ {1, 2} is a PROOF SKETCH, numerically validated. To reach PROVED it still needs
  symbol-by-symbol jump bookkeeping, explicit small-norm uniformity, and Rule R.
- **Housekeeping.** check_fine.py now has a `__main__` guard, because importing it from check_phase5 re-ran Phase 0.
