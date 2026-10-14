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

## 2026-10-14 — Plan 27 (G1-R: (CL) proved for rough weights)
- **Lemma Sat_p.** The G3′ §5.2 Lagrange/Christoffel bound for x = k^{−p}, any p ≥ 1, gives
  1 − ρ ≤ (W/w)e^{−2n·g_p(k/n)}. This is the "single-atom exclusion" input that the Plan 9 stop report lacked.
- **Lemma WC.** n²-speed concentration of the empirical measure at μ*_u. It uses:
  - G2 A1 and the A-U split;
  - a uniform energy gap by compactness in the x-variable (atom at 0 ⇒ I = −∞);
  - uniqueness (B*(iii));
  - the A-L lower bound.
- **Theorem CL:** (CL) holds for pure-power atoms with rough weights, so A4's tail-Cesàro a-law is unconditional.
- **G1-R** is reduced to (T3) alone, for pure-power atoms with p > 1.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan27.md). F1 (major: circular constants in Lemma WC; fixed by a
  uniform energy gap via compactness in x with an atom at 0 ⇒ −∞), F2–F7 applied. Re-check: ACCEPT (cosmetic items applied). REVIEWED.

## 2026-10-14 — Plan 28 ((T3) for rough weights)
- **Lemma FV (exact).** d/dt log b_n² = ⟨f, μ_n − μ_{n−1}⟩ with μ_n = w p_n², via Heine plus Christoffel–Darboux.
- **Numerics** (Lanczos with full reorthogonalization):
  - TV(μ_n, μ_{n−1}) ≈ 0.4 for all n.
  - Adversarial bounded weights keep |β_n/β_{n−1} − 1| ≈ 0.6ε, not decaying in n.
  - A single sequence with separated windows shows repeated jumps.
  - Generic rough weights decay like n^{−1/2}.
- **Conjecture R:** (T3) fails for some sandwiched weights, so G1-R as posed is likely false. Re-scoped: (T3) for
  regular weights, which reduces to a localization lemma for w p_n². The upper tail is open.
- An earlier forward-recurrence attempt overflowed in the saturated region; Lanczos with reorthogonalization is
  stable.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan28.md).
  - F1: the ratio's first variation is the second difference.
  - F2: TV ↛ 0 is not by itself evidence (Chebyshev); the evidence is locality plus cross-scale independence.
  - F3–F11 applied; numerics rewritten. Re-check: ACCEPT (R1–R3 applied). REVIEWED.

## 2026-10-14 — Plan 29 ((T3) for decaying roughness)
- **Theorem T3-conv.** Let w = k^{−s}ψ with ψ_k → L.
  - Integrate Lemma FV along w(t) = vψ^t, with g = log ψ − log L.
  - The head (k < k_ε) has exponentially small μ_m mass by Lemma Sat_p⁺, which extends Sat_p to 0 < p < 1 at a
    factor 1/p per term.
  - So log b_n²(w) − log b_n²(v) → 0, and the pure-power pointwise law (RH_p etc.) transfers.
- Slowly varying Ψ without a limit needs upper-tail localization of w p_n² (OPEN). An averaged version is sketched;
  it needs a tail-count bound uniform along the path (G2 A-U for p > 1; G3′ §7 Lemma K for p = 2).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan29.md). F1 (the Sat_p⁺ proof for p < 1 now carries the polynomial
  prefactor ((n+1)/k)^{2(1−p)}) and F2–F7 applied. Re-check: ACCEPT (R1, R2 applied). REVIEWED.

## 2026-10-14 — Plan 30 (polynomial tail localization; T3-sv)
- **Lemma TL.** For deg ≤ n, Markov's inequality makes atoms in [x_{T″}, x_{T′}] (T′ = 8pn², T″ = T′n^{2/p}) a
  norming set, and Chebyshev extrapolation to [0, x_{T″}] costs ≤ 17. By Christoffel, ρ_{n+1}(k) ≤ 1156(C/c)(T″/k)^s,
  so the tail mass beyond n^κ is ≤ ε. Uniform over the sandwich class.
- **Theorem T3-sv:** pointwise b-law for polynomially slowly varying Ψ (e.g. 2 + sin√(log log k)).
- **Open:** localization at scale Mn (needed for e.g. 2 + sin(log log k)). *Heuristic:* arguments that lose Markov's
  n² factor seem unable to reach it.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan30.md). F1–F13 applied (constants, implicit hypotheses, quoted
  inequalities, wording). Re-check: ACCEPT (R1–R4 applied). REVIEWED.

## 2026-10-14 — Plan 32 (the a_n half: Lemma FVa, Theorem T3a)
- **Lemma FVa:** d a_n/dt = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩. It combines exponential tilting, the two-point
  formula from Lemma H, the rank-one update K_{n+1} = K_n + q_nq_nᵀ and Christoffel–Darboux. Toda check passes; finite
  differences agree to ≤ 8·10⁻⁸.
- **Theorem T3a:** pointwise a-law n^p a_n → 2c(p) under T3-sv's hypotheses. b_n ≤ (a_{n−1} + a_n)/2 avoids any extra
  uniformity. Full pointwise Law P therefore holds for polynomially slowly varying weights.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan32.md). F1–F8 and F10 applied; numerics re-run with an n-scan and
  K-doubling. Re-check: ACCEPT (R1 applied). REVIEWED.

## 2026-10-14 — Plan 33 (Conjecture R proved: Theorem R)
- **Lemma R2.** |F_N''| ≤ 16‖f‖². The key is K_mq_m = 0, which makes the cross term a negative semidefinite form.
- **Lemma R1.** ‖Δ²μ_m‖₁ ≥ η once in every J consecutive m, for the pure power. Proof by contradiction:
  - small second differences ⇒ small first differences ⇒ |q_N| ≈ |q_{N−1}| ≈ |q_{N−2}|;
  - the recurrence then concentrates μ_{N−1} near {a − 2b, a, a + 2b};
  - free-Jacobi moments (2, 6, 20) give m₄ − 4m₂ → −2 ≠ 0.
- **Theorem R.** Windows ε·sign(Δ²μ) at polynomially separated good scales. Cross-scale independence comes from Sat_p⁺
  (head) and Lemma TL (tail). So limsup |log(β_n²/β_{n−1}²)| ≥ εη/2.
- **The (T3) half of G1-R is REFUTED** (the (CL) half is unaffected). Dichotomy: decaying or polynomially slowly varying roughness keeps the pointwise law;
  fixed-size roughness can break it.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan33.md). F1–F10 applied. Re-check ACCEPT (r1–r3 status/header polish applied; r4 notation clash J deferred) — REVIEWED.

## 2026-10-14 — Plan 34 (density-one pointwise law for slowly varying weights)
- **Lemma TC:** expected tail count beyond Mm ≤ (2A/(p log M))m + o(1), uniformly, from G2 A-U/A-L.
- **Theorem T3-avg.**
  - The tail term in Lemmas FV/FVa telescopes over n ∈ [N, 2N] to 𝔼_{2N+1}#(tail).
  - A finite-sum/integral interchange swaps the path integral and the n-average.
  - Result: the pointwise b- and a-laws hold along a density-one set of n for uniformly slowly varying Ψ.
- **Open:** all-n for uniformly slowly varying Ψ (would follow from Mn localization).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan34.md). F1 (hypothesis restated as uniform slow variation; no UCT citation), F2–F10 applied. Re-check ACCEPT (N1–N4 polish applied) — REVIEWED.

## 2026-10-14 — Plan 35 (localization at scale Mn; all-n law for bounded slowly varying weights)
- **Lemma TV:** exact derivative of a single tail mass μ_m(A) along w(t) = we^{tf}, via q̇_m = ½fq_m − K_m(fq_m) − ½⟨fq_m,q_m⟩q_m.
  The non-local term is ≤ 2√μ_m(A)·‖fq_m‖ (projection, Cauchy–Schwarz).
- **Lemma LP:** for the pure power, n^p-rescaled μ_n → arcsine on [0, 4c(p)] by moments (pure-power laws), so
  μ_n((Mn, ∞)) → F_p(M) = (2/π)arcsin√(M^{−p}/(4c(p))).
- **Theorem L:** Grönwall on √μ transports localization from v to vΨ^t: limsup ≤ e^{4G}F_p(M).
- **Theorem T3-all:** full pointwise Law P (b and a, all n) for bounded slowly varying Ψ (PROVED-mod-cite; pure-power nodes
  k^{−p}, base k^{−s}). Contains T3-conv, T3-sv, T3-avg.
- **Numerics** (`checks/check_mn_loc.out`): TV formula vs finite difference 8 digits; pure-power tails match F_p(M) for
  p = 2, 1, 0.5.
- **Open:** unbounded slowly varying Ψ; other nodes.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan35.md). F1 (head margin M₀(p), not n/4) and F2–F8, F10 applied. Re-check ACCEPT (N1–N3 polish applied) — REVIEWED.

## 2026-10-14 — Plan 36 (unbounded log-type weights: Theorem T3-log)
- **Lemma TLw:** Lemma TL step 3 in weight-explicit form, ρ_{n+1}^u(k) ≤ 1156u_k/min_{[T′,T″]}u.
- **Theorem T3-log:** full pointwise Law P (all n) for w = k^{−s}Ψ with Ψ slowly varying and D(γ) < ∞ (e.g. (log k)^α,
  any α). Truncate Ψ to [n/M₀, n^γ] (uniform sandwich ⇒ Theorem L / T3-all apply uniformly), and control the
  truncation by Sat_p⁺ (head, exponentially small) and TLw (tail, polynomially small), both robust to polylog losses.
- **Numerics** (`checks/check_log_weights.out`): (log(k+e))^α, α = 1, −2, 3: deviations ≈ 0.47|α|/(n log n), 2–6·10⁻⁵ at n = 3200.
- **Open:** slowly varying Ψ with D(γ) = ∞ (e.g. exp(√log k)); other nodes.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan36.md). F1 (cutoff h_n·1_{k≤K}, uniform bounds, K → ∞ by moment continuity) and F2–F7 applied. Re-check ACCEPT (N1–N2 polish applied) — REVIEWED.

## 2026-10-14 — Plan 42 (Lemma RL: Law P ⟺ rescaled μ_n → arcsine with sup n^p(a_n + b_n) < ∞, equivalently in moments 1, 2, 4; target T0′)
- **Source.** Simon, JAT 126 (2004), mp_arc 03-341: TeX source fetched from mp_arc and read (§1, §3). Quotes are in
  CITATIONS.md (Simon). Theorem 3.2 (moments ℓ = 1, 2, 4 of p_n²dμ converge ⇒ b_n → b, a_{2n} → a, a_{2n+1} → c) is the
  unscaled, fixed-J analogue. It does not apply verbatim to the n-dependent n^pJ, so RL is proved self-contained by the
  same path-sum argument; the citation is attribution only.
- **Lemma RL** (§3.13), any σ with infinite support and scales s_{n+1}/s_n → 1:
  - s_na_n → α, s_nb_n → β ⟺ moments 1, 2, 4 of ν_n → those of arcsine on [α − 2β, α + 2β] ⟺ weak convergence plus
    the a priori bound sup s_n(|a_n| + b_n) < ∞ (or UI of y⁴).
  - Key step: (∗) u_n + u_{n+1} → 2β² and (∗∗) u_{n+1}u_{n+2} + u_{n−1}u_n → 2β⁴ force (γ − β²)² = 0 at every limit
    point γ of u_n = (s_nb_n)². Zero discriminant ⇔ arcsine.
- **RL-loc.** For right limits, the indices n − 1, n, n + 1 suffice.
- **RL-n.** The index n alone does not suffice. The doubly infinite J_t (B_0² = 2tβ², B_1² = 2(1 − t)β²) has the
  arcsine law as its e_0 spectral measure (excursion bijection). It is realized by a positive compact J = LLᵀ + k_0²e_0e_0ᵀ
  with atoms x_k ↓ 0, where all moments of ν_{n_j} → arcsine moments but n_j^pb_{n_j} → β√(2t).
- **RL-b.** The b-law alone is not enough: with diagonal 3c, ν_n → arcsine on [c, 5c].
- **Open:** RL-UI, i.e. whether weak convergence without the a priori bound suffices.
- **Corollaries.** Localization ⟺ Law P for pure powers with sandwiched weights (the a priori bound is T3a step 1).
  For Theorem R weights, ν_n does not converge to arcsine.
- **Numerics** (`checks/check_rl.out`): (M) to 10 digits. Slowly varying Ψ: rdev ~ 1e−5, rmom 3–7e−5. Theorem-R-type windows:
  rdev ≈ 6e−2 and rmom up to 1e−1 at N − 2 … N, versus ≤ 3e−2 elsewhere. RL-b and RL-n are confirmed on the explicit
  parameters.
- **Labels:** RL, RL-loc PROVED; RL-n, RL-b, RL-n2 PROVED (spectral theorem for compact self-adjoint operators:
  textbook-standard, stated precisely, not checked against a specific source); RL2 PROVED-mod-cite (inherits
  Theorem R). Novelty: not claimed for RL, RL-b; UNCHECKED for RL-loc, RL-n, RL-n2.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan42.md; math correct). Fixes applied:
  - F1: the a priori bound / "in moments" was added to the §0 row, §3.13 heading, this title and the plan goal.
  - F2: RL2 now says β_n ↛ 1, cites T3a step 1, and is labelled PROVED-mod-cite.
  - F3: no verbatim source for the spectral theorem was read, so RL-n and RL-b are PROVED-mod-cite (Hilbert–Schmidt).
  - F4: the numerics text is corrected; the N − 1 rows are noted as an instance of RL-n.
  - F5: LP is a special case of the forward direction.
  - F6: the monotone argument for s_{n+1}/s_n → 1 was added; C is defined.
  - F7: Remark RL-n2 (the reviewer's construction: {n, n+1} fails for moments 1, 2, 4; general measures, positivity
    open) and check_rl [4] were added; RL-loc is weakened to ℓ = 1, 2 at n ± 1.
  - F8–F11 nits.

  Re-check: ACCEPT. R1–R3 applied:
  - R1 (option (a)): RL-n, RL-b and RL-n2 are back to PROVED, with the spectral theorem marked textbook-standard per
    the repo's precedent (TL, LP).
  - R2: RL-n2 needs 0 < γ < 2.
  - R3: LP is called "a special case" in the §3.13 opening; this LOG's rmom is corrected; RL3 assumes f decreasing on
    [1, ∞); RL-n2 is added to the novelty list.

  Rule R ACCEPT WITH FIXES (review/REVIEW_Plan42.md), fixes applied, re-check ACCEPT — REVIEWED.
