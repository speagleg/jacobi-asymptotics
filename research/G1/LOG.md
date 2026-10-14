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

## 2026-10-14 — Plan 39 (Conjecture R in window form: Lemma R1W, Theorem RW)
- **Lemma u_s:** u_s(p) = (4c(p))^{−1/p} < 1 for every p > 0 (G2 B*(i): μ*_u has density 1 on (0, u_s], and μ* charges
  (0, 4c)). So every window [aN, bN] with b ≥ 1, in particular [0.6N, 1.6N], meets the band for every p.
- **Lemma R1W:** Lemma R1 with every sum restricted to W_N = [aN, bN]. Steps 1–3 (telescoping, moduli, recurrence)
  localise verbatim; step 4 (moments) is replaced by the weak convergence ν_n → arcsine from the proof of Lemma LP,
  tested against h·dist(φ_N, Z_N)² with h ≤ 1_{W_N} continuous. Constants are explicit: c_W = (1/π)∫_{Θ_W}
  dist(2cos θ, {−2, 0, 2})²dθ, δ_W = c_W/32, J_W = ⌈2/δ_W⌉, η_W = δ_W/J_W² (p = 2, [0.6, 1.6]: η_W ≈ 9.8·10⁻⁸); N₀ is not.
- **Theorem RW:** f = ε·Σ_i sign(Δ²μ^v_{m_i})·1_{[aN_i, bN_i]} gives liminf_i F_{m_i}(w) ≥ εη_W/2 for ε ≤ η_W/16 when
  N_{i+1}/N_i → ∞, and ≥ εη_W/4 for a fixed explicit ratio R_W (≈ 1.1·10⁸ at p = 2). The proof uses the *direct* path
  ve^{tf}: R2 bounds the second-order term globally (8ε²), and the cross-window part of the linear term is evaluated at
  the pure power, where Sat_p⁺ (head) and Lemma LP (tail) apply. The TV/Grönwall transport proposed in
  outline_C_rough.md §2.1 is not needed.
- **Gaps (stated in §3.10):** every ε with an absolute c, a realistic η_W (numerically ≈ 1.1 vs 10⁻⁷), and small fixed
  separation (×4) remain NUMERICAL. All three would follow from a sharp R1W (outline target T6).
- **Numerics** (`checks/check_rw.out`, 1–2 min): FV vs finite difference to 9 digits; Q_N → c_W (0.2307 vs 0.2345 at
  p = 2, N = 300); window norms 1.06–1.09; construction at ε = 0.05, 0.2 with scales (30, 240) and (15, 60, 240): spikes
  match the linear prediction to ≤ 2%, cross-window ≤ 1.4·10⁻³, spikes exceed the off-spike maximum; K-doubling stable.
- **Rule A:** attempts logged in §3.10 remark RW-e.
- **Rule R:** pending.
