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
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan39.md). Fixes applied:
  - F1: Conjecture R's normalisation is |β_n/β_{n−1} − 1|, with c = η_W/4 (A) and η_W/8 (B). The spikes are one-signed,
    so e^{x} − 1 ≥ x applies. η_W/2 is the constant for log β².
  - F2: sign in log(β_m²/β_{m−1}²) = F_m + 2p log(m/(m−1)).
  - F3: RW-d now says the decay is exponential only below θ₀(p), and o(1) via LP-w between θ₀(p) and u_s.
  - F4: s_i is the pointwise sign function.
  - F5: labels for Lemma u_s (PROVED) and LP-w (PROVED-mod-cite); B*(i) is (P)-free; the §0 row now says N ≥ N₀.
  - F6: the stale "remains NUMERICAL" sentences are dated "as of Plan 33"; the §3.2 header is amended.
  - F8: "for ε ≤ ε₀" added to the §3.10 header.
  - F7: no change needed.
  - Re-check ACCEPT — REVIEWED.

## 2026-10-14 — Plan 40 (Lemma LR: linear response with explicit ε² remainder)
- **Lemma LR:** for any finite-moment base v and bounded f, ε := ½ osc f:
  |log b_n²(ve^f) − log b_n²(v) − ⟨f, μ_n^v − μ_{n−1}^v⟩| ≤ ε² (C = 1; the outline's 2 also valid). Proof: Lemma R2 one
  difference lower, but with Bessel's inequality ‖K_m(fq_m)‖² ≤ Var_{μ_m}(f) in place of R2's crude A/B bounds, giving
  |ΔV_m| ≤ Var_{μ_m}(f) ≤ ε², hence |(log b_n²)″| ≤ 2ε² at every t along ve^{tf} (uniform: each t is a new base).
- **Lemma LR′:** ratio form |F_N(w) − F_N(v) − ⟨f, Δ²μ_N^v⟩| ≤ 2ε² (sharpens R2: |F_N″| ≤ 4ε² vs 16‖f‖²).
- **Lemma LRa:** a_n′ = b_{n+1}γ_n − b_nγ_{n−1} (γ_m = ⟨fq_m, q_{m+1}⟩; FVa via the recurrence), γ_n′ from Lemma TV's
  q̇_m; |a_n″| ≤ ε²(b_n + b_{n+1}), so |a_n(w) − a_n(v) − L_n^{a,v}(f)| ≤ (e^ε − 1 − ε)(b_n + b_{n+1})(v).
- **Corollary LR-law** (pure power, PROVED-mod-cite RH_px/RH₁(r)/RH_plt1b): limsup|log β_n²(w)| and limsup|L_n^v(f)| differ
  by ≤ ε²; exact along rays: L_n^v(f) → 0 iff E(τf) = o(τ). Same for a_n with ½ε²e^ε.
- **Constants:** absolute — independent of n, p, s, nodes, v.
- **Not proved:** the fixed-f iff (no ε² band) — needs second-order chirp control (outline §2.5 T7b). Sharpness of the
  constants is NUMERICAL (reviewer hill-climb: 1.0000 LR, 0.993 LR′, 0.9999 LRa); the pointwise LRa constant 1 is attained
  (two atoms ±1, sinh θ = ±1).
- **Numerics** (`checks/check_lr.out`, NUMERICAL): p = s = 2 and p = 1, s = 2, n ≤ 200, random + adversarial f,
  ε = 0.4 … 0.025: worst |R_b|/ε² = 0.53, |R_F|/ε² = 0.61, |R_a|/bound = 0.19; Rule A exhaustive signs on tiny measures
  (13000 cases) 0.986 / 0.887; g″(t) formula = finite difference (5 digits) at t = 0, ½, 1; float64 vs longdouble 1e-12.
- **Rule A:** small cases, m = 0 / n = 0, constant f, no-completeness check (Bessel only), cross-term vanishing — logged in §3.11.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan40.md; no math errors). F1 (sharpness restated as NUMERICAL attained
  constants + two-atom example), F2 (FV+TV route promoted to main proof of ΔV_m; Heine route = cross-check, Gram form
  valid for general atoms), F3 (Λ ≤ 2ε, Λ^a ≤ ε, E^a/Λ^a defined, ray bound), F4 (script: R_F for n ≥ 2 = 1.889 ≤ 2,
  skipped count 0, docstring/runtime; .out regenerated), F5 polish applied. Re-check ACCEPT — REVIEWED.

## 2026-10-14 — Plan 41 (Theorem Ra: fixed-size rough weights break the pointwise a-law)
- **Lemma Toda:** ȧ_n = ⟨f, ΔE_n⟩, E_n := b_{n+1}q_nq_{n+1}. One line from FVa: multiply the recurrence by q_n, so
  (x − a_n)μ_n = E_n + E_{n−1}. Independent check via K̇_m = ½[(1−K)fK + Kf(1−K)] and Tr(XK_m) = Σ_{j<m}a_j. Numerics
  ([1] of `checks/check_ra.out`): finite differences agree to ≤ 1.2·10⁻⁸; Toda vs FVa to 10⁻²⁰.
- **Lemma R2a:** |ä_n| ≤ 2(b_n + b_{n+1})·inf_c‖f − c‖²_∞. Key: q̇_j = ½(1 − K_{j+1})fq_j − ½K_jfq_j (orthogonal
  pieces), so ‖q̇_j‖ ≤ ½‖f‖; plus FV for ḃ. Numerically the ratio to the bound is 0.005–0.10.
- **Lemma R1a:** for the pure power, ‖N^pΔE_N‖₁ + ‖N^pΔE_{N+1}‖₁ ≥ 2c(p)I − o(1), I = (1/π)∫min(1, H(2cos θ))dθ ≈ 0.314.
  Direct (no contradiction): both differences are exact quadratic forms in (q_N, q_{N+1}); the free forms
  (2uv − zu², zv² − 2uv) vanish together only for z ∈ {−2, 0, 2}; Lemma LP's weak convergence to the arcsine law
  (continuous test function; stated as Lemma LP′ after review) finishes. Window 2, explicit η_a = c(p)I/2.
- **Theorem Ra:** windows (−1)^iε·sign(ΔE^v_{n_i}) on [θn_i, n_i^γ] at polynomially separated good scales, as in Theorem R;
  b-bound along paths from FV (b ≤ e^ε b(v)); head/tail via Sat_p⁺ and TL. Result: for ε ≤ I/16,
  limsup (n^pa_n(w) − 2c) ≥ εη_a/2 and liminf ≤ −εη_a/2. Numerics [4]: single-window jumps match first order to ≤ 2%;
  a two-scale f gives ±0.08c(p) spikes at both scales.
- **Rule A (adversarial pass, self):** n = 0 (b_0 = 0, E_{−1} = 0) consistent; constant shifts of f leave every quantity
  unchanged (checked in R2a); degenerate cases u = 0 / v = 0 in the zero set of H handled; atoms with y > 4c and head
  atoms (z large) are covered because the test function min(1, H) is bounded and continuous on [0, ∞); μ_{N+1} with
  scaling N^p has the same moment limits; the cross-scale path stays in the sandwich class, where Sat_p⁺, TL and the
  FV b-bound are uniform. No counterexample found. Self-review only — does not count for Rule R.
- **Not claimed:** whether the b-law (or a_n/(2b_n) → 1) also fails for the same w. For p > 1 the tail-Cesàro a-law A4′
  still holds for w (Theorem CL), so pointwise and tail-Cesàro a-laws separate.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan52.md; no mathematical error). Fixes applied: F1 chain-sequence form of
  Lemma CS (a_n = β_n/(α_{n−1}α_n) = (1 − m_{n−1})m_n, minimal parameter sequence, CS ⟺ m_n → ½); CS labelled "PROVED; very likely
  KNOWN (chain sequences: Wall; Chihara 1978 Ch. I, III — not read, pointer only)"; F2 base-window remark (α_x ∈ (−½, ½] suffices
  for s > 1 + p/2); F3 numerics scope; F4 sharpness example for |G_n − c| = O(√r_n) in Rule A (e); F5 tilt transfer CONDITIONAL
  (implication PROVED); F6 "with infinite support" + SH propagates future p ≤ 1 / other-node base cases; F7 CITATIONS. Rule R ACCEPT WITH FIXES (review/REVIEW_Plan52.md), fixes applied — REVIEWED. Novelty UNCHECKED.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan41.md; no mathematical error, crux "joint law of (q_N, q_{N+1})
  not needed" confirmed). F1 (cross-reference to §3.11 Lemma LRa: same Toda form, constant 1 in R2a, ε₀ = I/8 possible;
  R2a and ε₀ = I/16 kept), F2 (Lemma LP′ weak form stated and cited), F3 (H 1-Lipschitz), F4 (wording; joint-law remark),
  F5 (interleaving HEURISTIC; A4′ label), F6 (quoted range 0.1069; script label [10, 99], .out regenerated; [3]/[4]
  marked not K-checked), F7 (N₀ not explicit) applied. Re-check ACCEPT — REVIEWED.

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

## 2026-10-14 — Plan 44 (Theorem B-cond: all slowly varying weights, conditional on QL)
- **Lemma L0** (PROVED): ε_n := sup_{m≥n}δ_m(2) → 0; dyadic chaining upward gives |g_n(k)| ≤ ε_n(1 + log₂(k/n)) for k ≥ n,
  and Potter bounds e^{−A_η}k^{−η} ≤ Ψ ≤ e^{A_η}k^{η}. Uses only the sequence form (λ = 2); no UCT, no BGT citation.
- **Lemma FV⁺** (PROVED): FV and FVa for unbounded f under Σ_k v_k max(1, e^{f_k})(1 + |f_k|) < ∞ (Weierstrass M-test on
  the Heine sums; Tonelli/Fubini for the series). Chosen instead of T3-log's K-cutoff because the cut paths are not on
  vΨ^t, so QL would otherwise have to be assumed for them too.
- **Hypothesis QL**: Λ_n := sup_t max_{m∈{n−1,n}} Σ_{n≤k≤n^γ}log(k/n)μ_m^{(t)}(k), γ > κ; QL is ε_nΛ_n → 0. The proof
  uses only QL₀: sup_t Σ_{n≤k≤n^γ}|g_n|(μ_n + μ_{n−1})^{(t)} → 0 (t-average suffices).
- **Theorem B-cond** (CONDITIONAL on QL + PROVED-mod-cite RH_px/RH₁(r)/RH_plt1b): explicit unconditional bounds
  |log b_n²(w) − log b_n²(v)| ≤ 2δ_n(M₀) + Q_n + r_n and n^p|a_n(w) − a_n(v)| ≤ 4M₀^p(2δ_n(M₀) + Q_n) + r′_n, r_n, r′_n → 0
  (head by Sat_p⁺ with Potter, far tail by TLw with γ > κ and Potter); so QL ⇒ the full pointwise Law P.
- **Lemma QLb** (PROVED): power-tail localization (outline QL-b) ⇒ Λ_n ≤ (1 + log C)/α (layer cake) ⇒ QL.
- **Cases of QL proved:** only old ones. ε_n log n → 0 (trivial bound Λ_n ≤ (γ−1)log n) forces D(γ) < ∞ (T3-log);
  bounded Ψ gives QL₀ via T3-all/Theorem L. No D(γ) = ∞ case. Theorem L does not give QL (fixed M only).
- **Rule A attempts:** Ψ eventually constant (ε_n = 0; reduces to T3-conv); downward chaining (not claimed, not used);
  boundedness audit of head/tail/FVa constants (none needed); dependence on γ (any γ > κ; smaller is weaker); sup_t vs
  t-average (average suffices); the m = n − 1 term (sum still centred at n). No counterexample found.
- **Numerics** (`checks/check_sv_general.out`, p = s = 2): for exp(√log(k+e)) and exp((log(k+e))^{0.8}),
  n·dev/ϑ_n → 0.49 (ϑ_n = L′(log n); K- and precision-checked); QL log-moment Λ_n ≈ 0.41–0.43, max at t = 0, ≈ LP constant 0.4156 (truncated).
- **Why the elementary methods stop** recorded as HEURISTIC (outline_B_sv.md §4), not proved.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan44.md; no mathematical error). F1 (Bc2 numbers), F2 (sup_t Λ_n at t = 0;
  LP constant 0.4156; QL at t = 0 is QLP, unproved), F3 (downward chaining needs ε_{⌈n/λ⌉}), F4 (Cauchy–Schwarz for the FVa
  cross piece), F5 (K-gap grows with n), F6 (QL₀ framing), F7 (labels: FV⁺ standard; L0 in §0; "full sequence"; QL/QL₀
  HYPOTHESIS; tilt law CONJECTURE) applied. Re-check ACCEPT (N1 QL wording, N2 K-qualifier applied) — REVIEWED.

## 2026-10-14 — Plan 45 (QL numerics N1–N3; outline_B_sv.md WP2) — NUMERICAL; Rule R ACCEPT WITH FIXES — REVIEWED
- **Script** `checks/check_ql_numerics.py` / `.out` (≈ 8 min). Model: atoms k ≤ K plus a Gauss–Legendre log-panel tail
  quadrature to 10⁴⁸ (as Plan 10 Phase 0), so the hard-edge region k ≍ n^{1+2/p} is represented at p ≤ 1. RKPW long double;
  μ_m by long-double recurrence above an adaptive start index (long double vs float64 agreement); K_m(fq_m) by streaming.
  Checks: K vs 2K, quad vs long double, Lanczos (full reorthogonalization), TV identity by finite difference in t.
- **Tooling note (exploratory runs, not in the .out).** A fixed head cutoff k0 = θ·m for the recurrence fails (garbage of size 10²⁰–10⁵⁰ for θ below ~0.8 of
  the band edge (4c)^{−1/p}m; the safe θ grows with m); the first adaptive rule (relative agreement only) cut too high
  (missing mass 10⁻⁷, flagged near zeros of p_m); the final rule (1e−9 relative or 1e−14 absolute) loses ≤ 5·10⁻¹⁸ where checked (Lanczos, m ≤ 200, K = 2·10⁴, no tail); for m ≤ 1600 with the tail only |1 − Σμ| ≤ 2·10⁻¹³ is shown.
- **N1:** at p = 1 and ½ the tilt ratio n·dev/ϑ_n rises toward 0.5 (0.465–0.493 at n = 1600) but more slowly than at p = 2;
  the exact pure-power tilt k^{−(s−ϑ_n)} gives 0.5 (d₁ shift confirmed), and dev_w/dev_tilt = 0.93 (p = ½), 0.97 (p = 1),
  0.99 (p = 2) at n = 1600 (sqrt only); (1 − dev_w/dev_tilt)·log n decreases for every p, so the defect decays at least like 1/log n. Limit 0.5 consistent, not established; tilt law stays CONJECTURE.
- **N2:** QL-b power tails with α = min(p/2, 0.8) and C ≈ 0.4–0.6 flat in n and t; arcsine slope −p/2 then far-tail
  slope −(s − 1) (−0.9 at t = 1), crossover M_x ≍ n^{2/p} (grid-quantized brackets [1.6, 6.6]n² at p = 1, [0.17, 0.67]n⁴ at p = ½; sqrt only); Λ_n with the tail approaches the LP
  constants 0.4156 / 0.9297 / 2.0762, flat in t; ε_nΛ_n decreasing in every case.
- **N3 (go/no-go):** R = |⟨1_Aq_m, K_m(g_nq_m)⟩|/μ_m(A) ≤ 0.93·ε_n(1 + log M) on all data (p ∈ {2, 1, ½}, t ∈ {0, ½, 1},
  n ≤ 400, M ≤ 2²⁹, sqrt only). **Route I′ not dead** on the outline's literal criterion; CB plausible numerically
  (mainly at p = 2, partly p = 1), unproved. (Rule R F1: the saturation beyond the hard edge, R → |P(0)/p_m(0)|, is
  structural for any f and is not evidence; at p = ½ the tested window cannot separate the CB and Cauchy–Schwarz scales.)
- No proof claimed; README.md and THEOREMS.md not edited.
- **Plan 44 correction (F8).** With the tail, sup_tΛ_n is attained at t = 1 in every row; Plan 44's "sup at t = 0" (§3.14
  Bc2) was a truncation artifact (size ≤ 5·10⁻³; no conclusion changes). Dated note added in Bc2.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan45.md). F1 (saturation structural; p = ½ non-discriminating; verdict on
  the literal criterion), F2 (R vs mean_A g_n), F3 (one weight in N2–N3), F4 (crossover brackets; exception n ∈ {25, 50};
  exponent 2/p), F5 (p = 2 plateau −0.3 … −0.8), F6 (defect decays ≥ 1/log n; tilt comparison sqrt only; 0.465; fit bias),
  F7 (tail-mass K-gap = boundary quantization), F8 (sup at t = 1), F9 (check scope; TV finite-difference check added at
  p = 1 and ½, agreeing to 5 digits for M = 2 … 2²⁹; script rerun, all other output identical), F10 (tooling note marked
  exploratory), F11 (QL-b constant uses m = n, t ∈ {0, 1}) applied — REVIEWED.

## 2026-10-14 — Plan 46 (Lemma QLP: uniform hard-edge localization for pure powers)
- **Route.** Not asymptotics on the band: the hard-edge tail is bounded by the Stieltjes transform at z = τe^{5πi/6}
  (Lemma ST, a Markov-type inequality: ν([0, τ]) ≤ (8/√3)τ|S(z)|), and S = −V₁₁V₁₂/(V₁)₁₂ exactly (Lemma GS: Green's function
  = p_n·Cauchy transform of p_n by orthogonality; the scalar/diagonal factors of the RH chain cancel). At z the RH solution is
  in Ω_∞, non-oscillatory, at distance ≍ |z| from every jump contour, so the small-norm matrix is I + O(1/N) there (Lemma Z;
  p = 1: O(N^{−1/2}) because RH₁(r)'s jump inside the disc is only O(1/n)·min(1, (n|s|)^δ), δ ≥ 2). The hard-edge prefactor
  is N-uniformly bounded (Lemma A: maximum principle on |z| = δ; h_N is σ-free). The Bessel model enters as I_α(u)·K_α(u),
  bounded by explicit integral/series estimates uniform in the order (Lemma BK; DLMF 10.25.2, 10.32.4, 10.32.9 read and quoted
  in CITATIONS.md (DLMF-3)).
- **Result.** For each fixed σ > 1, all p > 0, m ∈ {n−1, n}, every M ≥ 1: μ_m((Mn, ∞)) ≤ CM^{−p/2} for M ≤ n^{2/p};
  ≤ Cn^{−1}(M/n^{2/p})^{−β}(1 + log) beyond (β = min(p, σ−1), p ≠ 1; min(½, σ−1), p = 1); ≤ C_ϑM^{−ϑ} for all M,
  ϑ < min(p/2, σ − 1) (endpoint ϑ = p/2 when σ − 1 > p/2 for p ≠ 1 only). Corollary: Σ_{k≥n}log(k/n)μ_m(k) = O(1) — QL at t = 0. Bessel crossover at M ≍ n^{2/p}
  (k ≍ n^{1+2/p}). Labels: ST, GS PROVED; BK PROVED-mod-cite (DLMF); QLP/QLP-Λ PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b,
  KMVV (6.23), Vanlessen (4.27); KV (5.21)–(5.22) as a consistency check) for fixed σ.
- **Gap (precise).** Uniformity in σ on compacts is CONDITIONAL on (RU): the cited small-norm estimates hold with σ-free N₀ and
  constants. Audit U (PROOF SKETCH) locates the σ-dependence: only α_x and C_N; the one quantitative input is the Bessel
  matching on ∂U(0, δ) uniform in the order, for which DLMF 10.40.10–12 (+10.34.2, 10.27.8; read, quoted) give order-uniform
  remainders; plus RH₁(r) Lemma M's amplification constant uniform in a. Not re-proved line by line.
- **Not obtained.** QL along vΨ^t for t > 0 (B-cond's hypothesis): no new case of the pointwise law. The proved exponent β
  is below the heuristic σ − 1 when σ − 1 > p (resp. ½): Lemma ST is lossy there (harmless for (a), (c)).
- **Soft route (Remark QLP2).** LP + monotonicity in M (Pólya-type uniformity) gives the bound only for M ≤ M_n → ∞ at an
  unknown rate, hence Λ_n = o(log n) only; ensemble/Christoffel bounds lose a factor n. Recorded: no soft uniform-in-M bound.
- **Rule A.** σ ↓ 1 (constants blow up; K compact needed); α = 0 log (numerically visible at p = 0.5, σ = 1.5); z ∈ Ω_∞ for
  every p (lip/seam angles); scale invariance of Lemma Z; N-uniformity of A; m = n − 1. No counterexample.
- **Numerics** (`checks/check_qlp.out`, NUMERICAL): sup_{M≤n^{2/p}} tail·M^{p/2} = 0.48–0.71, flat in n, p ∈ {2, 1, 0.5},
  σ ∈ {1.5, 2, 3}; deep slopes ≈ −(σ−1); Lemma ST's inequality holds in every row. Small n, lumped tail (≤ 1.4%).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan46.md; main argument correct). F1 (sector-II formula is Vanlessen
  (4.27), not WLXZ (4.27)), F2 (endpoint ϑ = p/2 of (c) restricted to p ≠ 1), F3 (Lemma Z for |z| ≤ δ₁/2), F4 (check_qlp β at
  p = 1 = min(½, σ − 1); .out regenerated), F5 (QLP3(ii) reworded), F6 (Audit U6 gap disclosed: band rays/lips need BK beyond
  |ph u| ≤ π/3), F7–F9 (J2 terms, GS wording, closed-disc maximum principle, max(A, 1)) applied — REVIEWED.

## 2026-10-14 — Plan 48 (Route II, stage 1: RH analysis for slowly varying weights, p > 1)
- Write-up: `RH/route2/ROUTE2.md`; summary PROOF.md §3.17 and §0 row "RII / B_{p>1}". Plan: docs/superpowers/plans/2026-10-14-plan-48-route2.md.
- **RedA** (PROVED): Gaussian smoothing of the piecewise-linear interpolant of log Ψ(e^τ); entire L₁, L₁^{(j)} → 0 in strips,
  Ψ/Ψ₁ → 1, from the sequence form only (local oscillation ≤ 2δ_m(2e²)); base change by T3-conv's proof. The outline's claim
  "T3-conv's proof never uses the base weight" checked line by line: true except that Sat_p⁺'s ratio W/w_k involves the
  base; Potter (L0(ii)) supplies k^{s+η}. No BGT/UCT cited or used.
- **RH set-up** (ROUTE2 §2): only w₀ (factor q_N = Ψ₁(Nz^{−1/p})/Ψ₁(N)), D_w, poly(N) factors on saturated/top pieces, and the
  hard edge change; μ*, g, φ, D̃, B, K, F, normalization, Airy unchanged.
- **Stop condition (i): RESOLVED-mod-cite.** The direct (glued-W̃, possibly drifting-order) parametrix does fail: the jump
  1 + O(ε₁) on (−δ, 0) without rate becomes O(Nε₁) at the Bessel scale. Avoided as in RH_ζ_close §1: fixed-order comparison
  parametrix with W̃ := D_w; new Lemma LW1′ (lip mismatch ≤ C(|z|^ν log + ε₁(log N − C))) gives ‖v − ṽ‖_∞ → 0 without rate,
  enough for C–D's resolvent comparison; Proposition D′ gains 1/N from Bessel localization.
- **Stop condition (ii): MOOT** (fixed order α_x; drifting-order uniformity not established, not used; relevant only for the
  1/n coefficient).
- New for general α_x ∈ (−1, 1): local form of KMVV's Ψ (DLMF 10.25.2, 10.31.2 read and quoted in RH/CITATIONS.md "DLMF-4", renamed from "DLMF-3" per REVIEW_Plan48.md F2);
  Lemma UR′ (Lemma W with a = ±α/2); Lemma W′ (log-commutator, α = 0).
- **Theorem RII** (PROVED-mod-cite): p > 1, 1 < s < 1 + 2p, (H_an) ⇒ n^pb_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n).
  **Corollary B_{p>1}**: Theorem B for p > 1, 1 < s < 1 + 2p, every sequence-form slowly varying Ψ (first D(γ) = ∞ case).
- **GAP:** s ≥ 1 + 2p (α_x ≥ 1: Q̃ not L²_loc, C–D frame fails); p ≤ 1 (WP5); the 1/n coefficient (tilt law, CONJECTURE).
- **Rule A attempts** (ROUTE2 §6): Ψ₁ const (reduces to RH_px); Ψ = k^ρ (ε₁ ↛ 0, mismatch ≈ |e^{iπρ/p} − 1|, method
  correctly inapplicable); α_x → ±1 (constants blow up, consistent with GAP); log-type (consistent with check_log_weights);
  oscillating L; strip width (only |Im log t| < π/p used); UR′ independent of ε₁. No counterexample found.
- **Numerics** (`RH/route2/checks/`, p = s = 2): RedA [1]–[3]; LW1′ mismatch/ε₁ = 2.40 → 2.90 (N = 10² → 10¹², → π, the
  pure-tilt value); n(n^pb_n/c − 1) bounded (−0.39 … −0.41); tilt ratio 0.489 → 0.493; drifting-order model residual
  n·dev/ϑ_n ≈ −0.006; Lemma W′ Mellin symbol bounded (π² on the diagonal).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan48.md; RedA ACCEPT; RII and B_{p>1} ACCEPT WITH FIXES). Fixes applied:
  - F1 (high): UR′(b) depended on α (the crude product bound for m := C(gQ̃₊^{−1})Q̃ gives c_{−1} ≲ ε^{1/2−|α|}, which blows up
    for |α_x| > ½). New UR′(b′) in ROUTE2 §4.1: estimate m through UR′(d)'s factorization Q̃ = G(z)(−z)^{ασ₃/2}Θ(z) (fixed N):
    core terms (−z)^a∫h(s)(−s)^{−a}/(s − z)ds ≲ ‖h‖_η d^{−1/2} + C_η|z|^{−|a|} (|a| = |α|/2 < ½), K-term ≲ C_N‖g‖|z|^{−|α|/2},
    log variant for α = 0; area integral ≲ ε^{3/2} + ε^{2−|α|/2} = o(ε) for every |α| < 1. **F1 closed for all |α_x| < 1**;
    the claim stays 1 < s < 1 + 2p.
  - F2: "(DLMF-3)" renamed "(DLMF-4)". F3: the overclaim "the slowly varying factor costs O(ε₁/n)" removed; what is proved is
    Q₁ − Q̃₁, Q₂ − Q̃₂ = O(ε′_N/N) (the lip mismatch versus the comparison problem, which itself depends on Ψ₁).
    F4: (H_an) stated on {Re u ≥ −c₀, |Im u| ≤ π/p}; Ω_∞ never uses w. F5: det Ψ ≡ 1 from DLMF 1.13.4 + 10.28.2 (read, quoted).
    F6: the D_w 1/z-coefficient remark moved to the Q₁ vs V₁ step. F7: check_r2_redA [3] now uses L₁ for all k (FFT
    convolution on a τ-grid, validated against direct quadrature). F8: n = 800 convergence claim corrected (K = 4.8·10⁵ run
    added). F9: cross-references in PROOF.md §0 G1-R row, §3.14 and §4. F10: Lemma W′ flattening sentence.
  - Rule R ACCEPT WITH FIXES (review/REVIEW_Plan48.md), fixes applied, re-check ACCEPT — REVIEWED.

## 2026-10-14 — Plan 49 (Route I′: commutator lemma CB; CB ⇒ QL ⇒ law)
- **Goal** (outline_B_sv.md §5, Route I′): prove CB, |⟨1_Aq_m, K_m(g_nq_m)⟩| ≲ ε_nμ_m(A)(1 + log M), and from it QL. **CB is not
  proved.** What is proved (§3.18):
  - **TV⁺** (PROVED, standard extension): Lemma TV for unbounded f under FV⁺'s summability.
  - **BF** (PROVED): X_A = Σ_{k∈A, l∉A}q_m(k)K_m(k,l)q_m(l)(f(l) − f(k)) (only straddling pairs; uses K_mq_m = 0 and
    antisymmetry); Cov(f, 1_A) − 2X_A = flux of K_m + K_{m+1}; CD form with the Toda density ψ.
  - **RF** (PROVED): X_A = Σ_{k∈A}μ_m(k)R_m(x_k), R_m = P_m/p_m — makes exact the Plan 45 review's observation that beyond the
    hard edge X/μ(A) → R_m(0) for any f; the deep-range part of CB is a bound on R_m on the zero-free interval [0, z₁(m)].
  - **FM** (PROVED, Fourier): free Toeplitz model: X = (ε/πp)Cl₂(φ), Cov = 2X exactly (TV derivative ≡ 0),
    X/μ(A) = (ε/p)(1 + log(1/φ)) + O(φ²): the log M in CB is sharp in the free model (relevance to μ_m^{(t)} HEURISTIC, NUMERICAL support); predicts R/(ε_n(1 + log M)) ≈ 0.72, as observed.
  - **DB** (PROVED): |X| ≤ Σ_i a_ie_i over dyadic row-blocks of E_d = ⟨1_Aq_m, q_{m−d}⟩ and G_d = ⟨gq_m, q_{m−d}⟩; Jackson form
    e_i ≤ ℰ_{2^i−1}(g; μ_m); block bounds (OD-E), (OD-F) ⇒ |X| ≤ Cεy(3 + log₂(1/y)).
  - **NO** (PROVED): Nishida–Ovsyannikov comparison lemma for an ordered scale (only finiteness of the a priori bound used).
  - **Theorem QL-CB** (PROVED-mod-cite QLP at t = 0 for σ = s + B-cond; CONDITIONAL on CB): CB with a small constant
    η ≤ η₀(p, s, α, a) (deeper-layer and M^{−a} terms allowed) ⇒ sup_tμ_m((Mn, ∞)) ≤ CM^{−α} for every α < min(p/2, s − 1) ⇒ QL ⇒
    Law P. Grönwall in the scale of moments Y_β = Σmax(1, k/n)^βμ_m: the ε log M rate becomes a loss in β (no additive floor,
    no M^{Cε} blow-up).
  - **Theorem B-OD** (CONDITIONAL on OD-E, OD-F along the path).
- **Obstruction (HEURISTIC, Remark CB-ob):** OD-F needs a bounded hard-edge density of μ_m in the arcsine angle (plus
  smoothness of g in log x), OD-E needs 1/d decay of the spectral-projection row (phase coherence of q_m, q_{m−d}); tail
  transport only gives tails with a loss M^{Cε}, which re-enters the commutator rate as M^{O(ε)} = n^{O(ε_n)}; the loop
  closes only for ε_n log n = O(1) (log-type, T3-log). Route-II (hard-edge parametrix along the path) information would
  supply both. No new case of the law.
- **Rule A:** constants / A = ∅, all; f ↦ f + c; sharpness of log M (in the free model only); necessity of a small η in QL-CB (needed by the
  argument, no failure claimed); sign of X (positive, unused); rough f (OD-F fails, consistent with Theorem R); deep tail
  with small p_m(0) (z₁ > 0); Fubini domains. No counterexample.
- **Numerics** (`checks/check_cb.py/.out`, ≈ 70 s; p = 2 and 1 only, per REVIEW_Plan45.md; s = 2, exp(√log(k+e))):
  BF/RF/TV identities to 9–10 digits vs finite differences; FM to 10 digits; R/(ε_n(1 + log M)) ≤ 0.74; R/R_FM 0.86–0.93
  (p = 2), 0.69–0.88 (p = 1) in the arcsine range; DB/|X| ≤ 1.26; C_E ≤ 1.03, C_F ≤ 0.68 (p = 2), 1.26 (p = 1), flat in n ≤ 400
  and t; |R_m(0)|/(ε_n log n) = 0.63–0.74 (p = 2), 0.93–1.00 (p = 1); transport defect |T|/(ε_ny(1 + log M)) ≤ 0.05 (p = 2) /
  0.10 (p = 1) in the arcsine range, ≤ 0.58 beyond the Bessel scale (genuine far-tail tilt). The deep-range saturation is the
  structural RF limit and is not evidence for the arcsine-range form of CB (REVIEW_Plan45.md); the arcsine-range evidence is
  the free-model agreement.
- Note: §3.16 (QLP) is on master (Plan 46, merged); this branch was cut before the merge and cites it by section.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan49.md; no mathematical error; QL-CB, NO, DB, BF, RF re-derived; numerics re-run
  digit for digit). F1 (log M sharpness only in the free model; HEURISTIC for μ_m), F2 (FM(iii) proof via the product formula for
  sin), F3 (η₁ with α₂ < s − 1 − 2η₁), F4 (RF "Use": CB is implied by, not equivalent to, the R_m bound), F5 (η₀(p, s, α, a);
  "a sufficient condition"), F6 (inherited citations in the QL-CB label), F7 (numerics quoting; m = n only), F8 (neutral
  cross-reference to Plan 48 §3.17, in review: law for p > 1, 1 < s < 1 + 2p without QL; QL-CB's prospective new content would be
  p ≤ 1, s ≥ 1 + 2p and QL itself), F9 (NO: attribution only; any a ≥ 0; no monotonicity), F10 (BF(iii) not to be split;
  m = 0 conventions) applied — REVIEWED.

## 2026-10-14 — Plan 50 (Route II for p = 1, WP5a; Christoffel transfer) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan50.md), fixes applied — REVIEWED
- Write-up: `RH/route2/ROUTE2_p1.md`; summary PROOF.md §3.19 and §0 row "RII₁ / B_{p=1} / CT". Plan:
  docs/superpowers/plans/2026-10-14-plan-50-r2p1.md.
- **Range check.** RH₁(r) covers every r > 1 (pure powers). Its hard point is the band centre of the symmetrized problem, with
  Fisher–Hartwig exponent a = r − 3/2 (KV/Vanlessen Bessel model, orders a ± ½); unsymmetrized hard-edge order α_x = r − 2.
- **RedA** carries over unchanged (stated for every p > 0 and every strip). Strip needed at p = 1: the open strip |Im u| < π
  (WLXZ's regions in |arg(±z)| ≤ π/2 − θ_W; lips |Im u| ≤ π/2 + π/12); openness is necessary for exp √log(t + e).
- **Stop condition (i) at p = 1: RESOLVED-mod-cite for 1 < r < 2.** A quotient construction must continue q_n = Ψ₁(n/z²)/Ψ₁(n)
  across iℝ (Im u = ±π: the branch line of the model example; otherwise a jump 1 + O(ε₁) amplified by ρ^{−2|a|}). Avoided by the
  C–D comparison with W̃ := W·D_ϱ, D_ϱ the Szegő function of the whole non-FH band factor e^L(4 − x²)H_n²q_n: Ẽ_n = const·KV's E_n for
  the pure |x|^{2a}; the comparison problem has no jumps inside U(0, δ) (RH₁(r)'s Q_m/κ_n/Lemma M are not used). (ii) MOOT.
- **New:** Lemma LW1₁ (|D_ϱ²/ϱ − 1| ≤ C(|z| + ε₁,n); the q_n-part needs the even pairing 2z/(z² − x²) because R(z) does not vanish at
  the band centre; no decay in |z|); Lemma LF₁ (Ψ_a = Ψ̂ζ^{aσ₃}S_j, det Ψ̂ = 1, |a| < ½; Vanlessen (4.27), (4.53), DLMF 10.25.2,
  10.27.4 — no log case); UR₁ (Lemma W at ±a; large-ζ block commutator-free by Vanlessen (4.43)–(4.46)); UR₁(b′); Q ∈ L²_loc;
  C₁; D₁ (Q₁ − Q̃₁ = O(ε′_n/n)).
- **Theorem RII₁** (PROVED-mod-cite): p = 1, 1 < r < 2, (H_an₁) ⇒ nβ_n = 1 + O(1/n), nb_n = ½(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n).
  **Corollary B_{p=1}** (PROVED-mod-cite): the law for every sequence-form slowly varying Ψ (incl. D(γ) = ∞), 1 < r < 2.
- **Lemma CT₁** (renamed after review) (PROVED, self-contained): J(xμ) = LᵀL for the Cholesky factor of J(μ) (classical Christoffel/Darboux step; proved,
  attribution only), and Law P for μ ⟺ Law P for xμ, any weights, any p > 0 (**Lemma D**: parabolic map x ↦ 2 − 1/x, positivity
  excludes the repelling side). (After merging master: (i) and "⟹" are Plan 52's Lemma CT / CS + SH,
  §3.21; renamed Lemma CT₁; the new content is "⟸".) **Corollary B_{p=1}⁺**: every non-integer r > 1 at p = 1, with rate O(1/n)
  under (H_an₁) via §3.21's SH-r. (The first version's "B_{p>1}⁺" is Plan 52's Corollary B_all and is withdrawn here.)
- **GAP:** p = 1, r ∈ {2, 3, …} (GAP-int; ⟺ the law at r = 2 by CT₁ "⟺"); tilt law (CONJECTURE). **OBSTRUCTION** (scoped to
  the band-centre C–D frame): |a| ≥ ½ (Q̃ ∉ L²_loc, Lemma W fails; the symmetrization halves ROUTE2's α-range).
- **Rule A attempts** (ROUTE2_p1 §7): Ψ₁ const (second proof of RH₁(r) on 1 < r < 2); Ψ = k^ρ (ε₁ ↛ 0, method inapplicable,
  correctly); a → ±½ (constants blow up); necessity of the even pairing; strip edge never used; Lemma CT on degenerate μ (finite
  support, atom at 0 — excluded by hypothesis) and the repelling side of the dynamics (excluded by positivity); UR₁ independent
  of ε₁; analyticity of 𝒵̃ in U(0, δ). No counterexample found.
- **Literature (Rule L) not done.** Lemma CT(i) is classical (Christoffel's theorem / Darboux "LU ↦ UL"); no source was read, so it
  is proved in full and not cited. Whether CT(ii) (transfer of Law P) is in the literature: UNCHECKED.
- **Numerics** (`RH/route2/checks/check_r2p1_{lw1,coeff,ct}`): LW1₁ mismatch/ε₁-sample 2.04 → 2.76 (n = 10² → 10¹²), no decay to
  |z| = 10⁻¹⁴; Ψ̂ entire with det 1 (a ∈ {−0.4, 0, 0.3, 0.45}); s = 1.5: n(nb_n/c − 1) = −0.137 … −0.157 (n = 50 … 800, five
  truncations incl. tail cut-off 10¹⁴, spread ≤ 2·10⁻⁶ for nB, E, T, ≤ 2·10⁻⁵ for R); s = 2 (GAP-int): −0.382 … −0.407; tilt ratio → ½ slowly; drifting
  model residual ≈ −0.02; CT identity to 3·10⁻¹⁶; x_n = n^pl_n²/c → 1 like 1 − 1.05/n; p = 2, s = 6 law bounded.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan50.md; no counterexample; numerics re-run byte-identical). Fixes applied
  after `git merge master` (Plan 52):
  - F1: Lemma CT renamed CT₁ (Cholesky form); (i) and "⟹" cited from §3.21 (CT, CS, SH); "⟸" with Lemma D(b) kept as the new
    content; B_{p>1}⁺ replaced by a cross-reference to B_all; "closes GAP-α" claims removed. F2: B_{p=1}⁺ with rate via SH-r;
    GAP-rate₁ reduced to the tilt law. F3: Lemma D(b) constants (A_n − z_n ≥ 0.49, 2 − z_n ≥ 0.48, error ≤ 13ε). F4: Airy-disc
    prefactor (𝔇_∞/D_{h_W,∞})^{σ₃}. F5: CT₁ on [0, ∞); mass at 0 does not affect the law; Rule A (f) corrected. F6: GAP-int ⟺ law
    at r = 2, and the failed alternatives listed. F7: spread wording (R column 2·10⁻⁵). F8: check_r2p1_ct [4] not independent.
    F9: chain-sequence pointer (novelty UNCHECKED). F10: remark that D_ϱ drops out of Q̃'s local form.
  - Rule R ACCEPT WITH FIXES (review/REVIEW_Plan50.md), fixes applied — REVIEWED.

## 2026-10-14 — Plan 51 (Route II for 0 < p < 1, WP5b; Christoffel step for all s > 1) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan51.md), fixes applied — REVIEWED
- Write-up: `RH/route2/ROUTE2_plt1.md`; summary PROOF.md §3.20 and §0 row "RII_{<1} / CT-Ch / B_{p<1}". Plan:
  docs/superpowers/plans/2026-10-14-plan-51-r2plt1.md.
- **Strip (Lemma S_w):** for p < 1 the weight is evaluated only in S_in = {|arg z| < πp/2} (band lens, Ω^△, lips at ±πp/4,
  (Y4)_x sector, top segment), so |Im u| ≤ π/2 suffices — not π/p. RedA's L₁ satisfies any strip (RedA(ii) for every σ₀; the
  constant e^{σ₀²/2} only). exp √log(t + e) (branch points at Im u = ±π) satisfies the π/2 strip but not π/p for p ≤ 1.
- **Seams:** Ψ₁ does not enter the seam scalar F (L±, X are node data); V, Q have no seam jump; with W̃ := D_w the comparison
  parametrix has none either (RH_plt1b's super-small glued-W̃ seam jump disappears). The seams enter only through e^{−2X} in h_N.
- **Lemma X0** (PROVED-mod-cite DLMF 5.5.1, 5.11.1 + §5.11(ii); new quote entry "(DLMF-5.11, Plan 51)"): N-uniform
  |L±(ζ)| ≤ C|ζ| (|ζ| ≤ 1), ≤ C(1 + log|ζ|) (|ζ| ≥ 1), hence |X(z) − X(0)| ≤ C|z|(1 + log(1/|z|)), |X′| ≤ C(1 + log(1/|z|)) off the seams.
- **LW1′_{<1}** (PROVED): lip mismatch ≤ C(|z|^{1/2}log(2/|z|) + ε₁(T_N)) at the lips ±πp/4; ε′_N = N^{−1}log N + ε₁.
- **UR′_{<1}** incl. (b′), C′_{<1}, D′_{<1}: ROUTE2 §4 with the star {0, ±πp/4} at the hard edge (KMVV angle π − θ_L).
- **Theorem RII_{<1}** (PROVED-mod-cite): 0 < p < 1, 1 < s < 1 + 2p, (H_an^{<1}) ⇒ O(1/n) law.
- **Lemma CT-Ch** (renamed from "CT", Rule R F1; PROVED, self-contained; Christoffel/Darboux identity J(xσ) = LᵀL for J(σ) = LLᵀ, novelty of the identity not
  claimed): a_n/b_n → 2, b_{n−1}/b_n → 1 ⇒ the same for xσ (r_n = l_n/m_n → 1 by a parabolic-recursion argument using r_n > 0);
  O(1/n) in ⇒ O(1/n) out (r_n − 1 = O(n^{−1/2})). Since xσ_{s,Ψ} = σ_{s+p,Ψ}: **Corollary RII⁺_{<1} and B_{p<1} for every s > 1**;
  Remark CT-px: a second proof of Plan 52's Corollary B_all (p > 1, every s > 1; §3.21), not a new result. Corollary B_{p<1}: law for every sequence-form slowly varying Ψ (incl. D(γ) = ∞), all s > 1.
- **GAP:** the 1/n coefficient (tilt law, CONJECTURE); p = 1 (WP5a, not treated).
- **Rule A** (ROUTE2_plt1 §5.1, §7): Ψ₁ const; Ψ = k^ρ; strip edge cases (nothing evaluated at |arg z| ≥ πp/2); N-uniformity of
  X0 (log N only in X(0), a constant); α_x → ±1; CT on Laguerre (exact) and on truncated measures (hypothesis fails, r_n ↛ 1 —
  consistent); existence of s₀ ∈ (1, 1 + p]. No counterexample.
- **Numerics** (`RH/route2/checks/check_r2p_{coeff,lw1}.py/.out`, p = ½, Ψ = exp √log(k + e), quadrature tail to 10⁴⁸ as in
  Plan 45): n(n^pb_n/c − 1) bounded for s = 1.5, 1.75, 2, 2.5 (−0.40 … −0.42 at s = 2), n(a_n/(2b_n) − 1) → ¼ = p/2;
  K-doubling ≤ 10⁻⁷, quad ≤ 5·10⁻¹⁴; CT identity to 8·10⁻¹⁷, r_n − 1 = O(1/n); LW1′ ratio 1.65 → 2.51 (N = 10² → 10¹², → π);
  Lemma X0 ratio flat in N. Atoms-only (no tail) values are wrong (law fails for the truncated measure).
- **Found while reading (RH_plt1b.md not edited; corrected per Rule R F2):** RH_plt1b §1's L± = −μ − … and its t → 0 expansion are
  correct with Binet's μ (RH_px §1, D̃ = e^{−μ}); only its displayed definition μ(t) := ½log 2π + (t − ½)Log t − t − LogΓ(t) has the
  wrong sign (it is −μ_Binet). ROUTE2_plt1 uses λ := log D̃ = −μ. Text-only; no statement affected. check_r2p_lw1.py [2a]
  reproduces RH_plt1b's X(0) probe.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan51.md; no mathematical error; Lemma CT re-derived, identity checked to 10⁻⁶⁰,
  numerics re-run digit for digit). Fixes applied (after merging master with Plan 52):
  - F1: lemma renamed CT-Ch (Cholesky/Darboux form); equivalence with Plan 52's CS/CS-r (g_j = l_j², h_j = m_{j−1}²) stated; its
    proof kept as an independent second proof (PROVED, classical); Remark CT-px turned into a cross-reference to B_all; §0 G1-R
    and §4 cross-references merged with Plan 52's.
  - F2: sign-slip note relocated to RH_plt1b's displayed definition of μ; local μ renamed λ := log D̃ (ROUTE2_plt1 §3.2, PROOF
    §3.20, this entry, check_r2p_lw1.py docstring).
  - F3: X0(ii) large-|z| clause (1 + log|z|)². F4: (h1) exponent −√2πN|z|^{−1/p}. F5: q_N constant ε₁(π/4 + |log(x/|z|)|/p).
  - F6: Rule A (e) corrected (s₀ ∈ (1, 1 + p] gives α_x ∈ (−1, 0]); remark: s₀ ∈ (1 + p/2, 1 + 3p/2] keeps |α_x| ≤ ½.
  - F7: "model measure" scope; check_r2p_lw1.py [2b] now prints the sup over |z| ≤ 10⁻² (0.085–0.089, flat in N). F8: b̃_n/b_n → 1
    in the §0 row.
## 2026-10-14 — Plan 52 (Route II for s ≥ 1 + 2p: GAP-α closed for the law by Christoffel transfer) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan52.md), fixes applied — REVIEWED
- Write-up: `RH/route2/ROUTE2_alpha.md`; summary PROOF.md §3.21 and §0 row "SH / B_all". Plan:
  docs/superpowers/plans/2026-10-14-plan-52-r2alpha.md.
- **Route chosen: (b) Christoffel transfer.** x·σ_s = σ_{s+p} exactly. Lemma CP (zeros of P_n in (0, ∞), self-contained),
  Lemma CT (Christoffel / Darboux formulas α_n = g_n + h_n, β_n = g_{n−1}h_n, α̃_n = g_n + h_{n+1}, β̃_n = g_nh_n,
  g_n = −P_{n+1}(0)/P_n(0); re-proved, not cited), Lemma CS (Law P ⇒ n^pg_n → c: parabolic fixed point of
  F(G) = 2c − c²/G plus positivity), Theorem SH (Law P passes to x·σ, any σ ≥ 0 on [0, ∞)), Lemma CS-r / Theorem SH-r
  (regular rate r_n preserved; |G_n − c| = O(√r_n) but increments O(r_n)). **Finding:** contrary to the plan's expectation, no
  p_n(0) asymptotics from the hard-edge RH analysis are needed — the law at σ and positivity determine n^pg_n → c.
- **Corollary B_all** (PROVED-mod-cite, inherits RII): p > 1, every s > 1, every sequence-form slowly varying Ψ: full
  pointwise Law P; O(1/n) under (H_an). Base s₀ ∈ (1, 1 + 2p) (proof as written: s₀ ∈ [1 + p, 1 + 2p) for s ≥ 1 + p). Rule R F2:
  any base window of length p works; for s > 1 + p/2 take s₀ ∈ (1 + p/2, 1 + 3p/2] (α_x ∈ (−½, ½]), so UR′(b′) (Plan 48 F1) is
  needed only for 1 < s ≤ 1 + p/2; Lemma W′ (α_x = 0) is genuinely needed.
- **Route (a)** (frame change with a pole): not pursued; superseded for the law; recorded as HEURISTIC (Schlesinger ↔
  Christoffel) and a scoped OBSTRUCTION (needs pointwise Y_σ(0) control, not given by the L²-comparison).
- **Remark SH-1/n:** exact identity n^p√β̃_n = n^p√β_n·κ_n^{1/2}(G_n/G_{n−1})^{1/2}; 1/n coefficient shifts by −p/2 iff
  n(G_n − G_{n−1}) → 0 (hypothesis NUMERICAL); tilt-law transfer CONDITIONAL (implication PROVED; Rule R F5).
- **Numerics** (`RH/route2/checks/check_r2alpha_{christoffel,law}.out`): transfer exact to 2·10⁻⁵⁹ (60-digit RKPW, K = 1200,
  n ≤ 300, incl. p = ½) and to 8·10⁻¹⁶ (binary128 RKPW, K = 4·10⁴, n ≤ 600; double-input floor). A first attempt with the
  discretized Stieltjes procedure in mpmath gave O(1) discrepancies even at 250 digits for p = 2 — an instability of that
  coefficient algorithm for clustered atoms, not of Lemma CT; replaced by RKPW. Law at p = 2, s = 5, 6, Ψ = 1 and
  exp √log(k + e): n(n^pb_n/c − 1) bounded (−1.99, −2.49 for Ψ = 1 at n = 400 → −(s − 1)/2), n(a_n/(2b_n) − 1) → 1;
  1/n shift per step → −0.995 (−p/2 = −1; K-stable to 2·10⁻³); n·½log(g_n/h_n) ≈ s − 5/2 (p = 2; K-converged at n = 100, and
  at n = 200 for s ≥ 4 only). K-doubling: s = 5, 6 rows stable to ≤ 10⁻³ for n ≤ 400 (bases s = 3, 4: 2–3·10⁻³ at n = 400);
  n = 800 not converged, not used (Rule R F3).
- **Rule A** (ROUTE2_alpha §8): truncated measures, mass at 0, c > 0, fixed-point uniqueness, rate loss, converse,
  exactness of the shift with the same Ψ, p = ½. No counterexample.
- **Rule L:** not done (Christoffel's theorem / Darboux transformations are classical — e.g. Szegő's book, Bueno–Marcellán,
  Grünbaum–Haine — none read here; Lemma CT is re-proved in full and not cited). Novelty UNCHECKED.
- **Open:** p ≤ 1 with D(γ) = ∞ (no base case); tilt law (GAP-rate); RH analysis of the weight for α_x ≥ 1 (not needed).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan52.md; no mathematical error). Fixes applied: F1 chain-sequence form of
  Lemma CS (a_n = β_n/(α_{n−1}α_n) = (1 − m_{n−1})m_n, minimal parameter sequence, CS ⟺ m_n → ½); CS labelled "PROVED; very likely
  KNOWN (chain sequences: Wall; Chihara 1978 Ch. I, III — not read, pointer only)"; F2 base-window remark (α_x ∈ (−½, ½] suffices
  for s > 1 + p/2); F3 numerics scope; F4 sharpness example for |G_n − c| = O(√r_n) in Rule A (e); F5 tilt transfer CONDITIONAL
  (implication PROVED); F6 "with infinite support" + SH propagates future p ≤ 1 / other-node base cases; F7 CITATIONS. Rule R ACCEPT WITH FIXES (review/REVIEW_Plan52.md), fixes applied — REVIEWED.

## 2026-10-14 — Plan 53 (GAP-int, boundary frame: the boundary a = ½ at p = 1 by folding the symmetric problem; second proof of §3.23's p = 1 result) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan53.md), fixes applied — REVIEWED
- Write-up: `RH/route2/ROUTE2_bnd.md`; summary PROOF.md §3.22 and §0 row "RII₁ᶠ / B_{p=1}^{all,ᶠ}". Plan:
  docs/superpowers/plans/2026-10-14-plan-53-r2bnd.md.
- **Range check (option iii).** RH₁(r) is fine at a = ½ for pure powers (quotient construction; Lemma M's mismatch decays like
  |z|^{4m+2}, δ = 5). T3-all / T3-log cover bounded and log-type Ψ at r = 2. So GAP-int = D(γ) = ∞ at r = 2, and OBSTRUCTION-a is
  an obstruction of the C–D comparison in the **symmetric** frame.
- **Diagnosis.** In that frame the D₁ integrand for (Q₁)₂₁ (i.e. for the individual β_n) is ≍ δ_n(z)/(πζ) on the lips — the
  rank-one factor times |ζ| is exactly 1/π (check_bnd_fold [4]) — non-integrable unless L₁′ is Dini (HEURISTIC). Option (i)
  (L^p / E^p, scalar power weights): the two columns need p < 2 and p > 2 at a = ½; OBSTRUCTION (heuristic — the A_p "only if"
  (Hunt–Muckenhoupt–Wheeden) was not read); not pursued.
- **Idea (option (ii) in the folded variable).** For even degree n = 2m the symmetric problem is σ₃-even (Lemma P), so
  fold X := z^{−σ₃/2}Xz^{σ₃/2} is a function of x = z²; fold Y_ν^{(2m)} = L·Y_μ^{(m)} (Lemma F0, the quadratic transformation in RH
  form). The band centre of exponent a becomes the hard edge of μ of order α_x = a − ½ = r − 2, and L²(|dx|) on σ₃-even functions
  is the matrix-weighted space in which the C–D comparison works for |α_x| < 1 — ROUTE2's (Plan 48) range, including α_x = 0
  (Lemma W′). The law is read off a_m, b_m of μ (1/x, 1/x² coefficients), never off β_n.
- **New lemmas:** F0 (PROVED); P (PROVED-mod-cite WLXZ: w, θ even, Π odd, g(−z) = g(z) ∓ iπ, D even, D̂(−z) = D̃(z); R, T carry −1
  on Ω^△, cancelled by the odd V^△±); FS (D_ϱ(z) = D^x_{ϱ_x}(z²); Γ := D^x_{x^α}(z²)/D_a with Γ₊Γ₋ = 1/|y|); FJ (folded jumps:
  band constant, hard-edge lips with w_x = x^αϱ_x, nothing on ℝ₋); FN (fold(N₀^{KV})Γ^{σ₃} = [[1, 0], [−i, 1]]N₀^x, uniqueness);
  Fφ (f_K := −f(√x)²/4, e^{2nφ^x} = e^{−4(n²f_K)^{1/2}}, reversed ordering; KMVV angle π/2); FY (fold R = RH_px's one-sided
  interpolation problem at p = 1; (Y4)_x).
- **Theorem RII₁ᶠ** (PROVED-mod-cite): p = 1, 1 < r < 3, (H_an₁) ⇒ m b_m = ½(1 + O(1/m)), a_m/(2b_m) = 1 + O(1/m) (ROUTE2 §§3–4
  in the folded variable: H1ᶠ, LW1ᶠ = x^α-factor × LW1₁, URᶠ, Q^x ∈ I + ∂C, Cᶠ, Dᶠ = O(ε′_n/n), RH_px invariance lemma).
  **Corollary B_{p=1}^{all,ᶠ}** (PROVED-mod-cite; renamed after review): every r > 1 incl. integers, every sequence-form slowly
  varying Ψ (RedA + SH-r) — a second proof of §3.23's B_{p=1}^{all}; GAP-int is closed by §3.23 (Plan 54). OBSTRUCTION-a stands, scoped to the symmetric frame.
- **Hybrid route** (task item): interpolation in r via FV⁺ (Lemma IR, PROVED) needs a log-moment localization uniform as a → ½
  (QL-type, open); a Theorem-L Grönwall from a log-type base meets Plan 49's commutator term. Recorded, not used (HEURISTIC).
- **Rule A attempts** (ROUTE2_bnd §7): Ψ ≡ 1 (third proof of RH₁(r) on 1 < r < 3); odd degree (fold is the xμ problem; unused);
  the Ω^△ sign (cancelled); poly(n) fold factors on long pieces (absorbed); item-by-item check that the folded problem has
  ROUTE2's hard-edge structure; α = 0 exactly (ROUTE2's log case); no step needs |a| < ½; the folded C–D integrals never
  represent (Q₁)₂₁ alone. No counterexample.
- **Literature (Rule L) not done.** The quadratic transformation of OPs is classical (pointer: Chihara 1978, Ch. I — not read);
  Lemma F0 is proved, not cited. Whether the law at p = 1 for D(γ) = ∞ weights is known: UNCHECKED.
- **Numerics** (`RH/route2/checks/check_bnd_{coeff,fold}.out`): p = 1, Ψ = exp √log(k + e), five truncations (K-doubling 1, 2,
  4·10⁵; t_end = 10¹⁴; finer tail quadrature), n = 50 … 1600: n(nb_n/c − 1) = −0.382 … −0.411 (r = 2; spread ≤ 4.7·10⁻⁸,
  K-doubling ≤ 1.7·10⁻¹⁰), −0.628 … −0.661 (r = 2.5), −0.875 … −0.911 (r = 3): bounded; n(a_n/(2b_n) − 1) → ½; tilt ratio
  0.47 → 0.485. Fold checks (40 digits): Lemma F0 to 10⁻³⁹; Lemma FN constant [[1, 0], [−i, 1]] to 10⁻³⁹ (a = 0.1, 0.5, 0.8); WLXZ
  g-parity (D, D̂/D̃ lines tautological; those parities analytic); model factors: unfolded |·||ζ| → 1/π (5 digits), folded (KMVV α = 0) |·| ≤ 0.13(1 + log²|ζ|).
- **Citations:** RH/CITATIONS.md "(WLXZ-v1, Plan 53)" (parity formulas; also corrects the transcription of WLXZ (4.12) in the
  RH_px entry) and "(Fold-attrib, Plan 53)" (attribution only, not read).
- **Open:** tilt law (GAP-rate₁, CONJECTURE).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan53.md; no mathematical error; both checks re-run identical). After
  `git merge master` (Plan 54, §3.23, which closes GAP-int in the x-frame), fixes applied: F1 reframed as an independent second
  proof of §3.23's p = 1 result; corollaries renamed B_{p=1}^{bnd,ᶠ}, B_{p=1}^{all,ᶠ}; one "GAP-int closed" claim (§3.23); ROUTE2_p1
  note points to §3.23 and §3.22. F2 "Relation to §3.23" (ROUTE2_bnd §3.8, PROOF §3.22): independent — global frame, outer model,
  Airy disc, lip mismatch, equilibrium input; shared — ROUTE2's α_x = 0 comparison (Lemma W′, UR′(a)/(b′)/(d), D′), KMVV §6, C–D,
  RH_px invariance lemma and (Y4)_x, RedA, SH-r, WLXZ v1; coefficient numerics identical to Plan 54's check_x1_coeff. F3 quotes
  (2.14), (3.1), (3.4), (2.4), (4.28) and φ̂(−z) = φ̃(z) for (5.8). F4 residue vs FIK convention. F5 §1.4 wording. F6 "(a_n, b_n) part
  of RII₁ / RH₁(r)". F7 β_n remark labelled, both index conventions. F8 K-doubling ≤ 1.1·10⁻⁹ for E. F9 numerics scope
  (tautological D lines; 1/π to 5 digits; model factors only). F10 range sentence (Rule A (h)). F11 ray-angle precedents. PROOF.md
  §4 updated (p = 1, D(γ) = ∞ no longer open). Rule R ACCEPT WITH FIXES (review/REVIEW_Plan53.md), fixes applied — REVIEWED.

## 2026-10-14 — Plan 54 (GAP-int: x-frame and other routes) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan54.md), fixes applied — REVIEWED
- Write-up: `RH/route2/ROUTE2_xframe1.md`; summary PROOF.md §3.23 and §0 row "RII_x1 / GAP-int / B_{p=1}^{all}". Plan:
  docs/superpowers/plans/2026-10-14-plan-54-r2xframe.md.
- **Route (B) works.** RH_px's "p > 1" was audited step by step. At p = 1, Lemma 1.1 holds as an open sector, but Γ's poles
  t = −m lie on the negative z-axis. Lemma X1 (DLMF 5.5.1, 5.5.3): D = D̃/(1 − e^{∓2iθ}) = exp μ(−N/z), analytic off [0, ∞), so
  ℓ̂ ≡ 0, B ≡ 1. Lemma X2: the only genuine failure is RH_px Lemma 3.2(v) (sin(π/p) = 0: the (h2) jump of D̃B on (−δ, 0) is
  −e^{−2iθ}, O(1); the continued h_N has poles at −N/m), used only by RH_px's quotient hard-edge construction. ROUTE2's C–D hard
  edge (W̃ := D_w) never continues across (−δ, 0), so **Theorem RII_x1** (p = 1, 1 < r < 3, incl. r = 2 = α_x 0) holds,
  PROVED-mod-cite. With RedA and SH-r: **GAP-int closed**; p = 1 every r > 1; with §§3.20–3.21 the law holds for every p > 0, s > 1,
  every sequence-form slowly varying Ψ.
- Strip at p = 1: |Im u| ≤ π/3 + π/24 (lips at ±π/3), so (H_an^{x1}) on |Im u| ≤ π/2 suffices (exp √log(t + e) is singular at
  Im u = ±π).
- **Route (C)** (scoped, not needed): symmetrization = the obstructed RH₁(r) frame; Uvarov/rational factors keep r; Geronimus to
  r = 1 (α_x = −1, finite only if ΣΨ(k)/k < ∞); interpolation in r has non-uniform constants.
- **Numerics** (`RH/route2/checks/check_x1_{frame,e2e,coeff}.out`): Lemma X1 to 10⁻²⁷; (h2) jump O(1) at p = 1 vs 10⁻¹²⁰ at p = 1.1;
  LW1-x1 ratio 2.09 → 2.75 (bounded); e2e N·err stable (N = 10, 20, 40) at r = 1.5, 2, 2.5; coefficients bounded at r = 2, 2.5, 3
  for exp √log(k + e) and an oscillating Ψ (spreads ≤ 1.3·10⁻⁸). **Numerical incident:** the first p = 1 e2e run gave an
  N-independent O(1) error; diagnosed as V ≈ CNC^{−1} from a wrong D_{w,∞}, caused by catastrophic cancellation in the probe's
  D̃ = √(2π)exp((t − ½)ln t − t − LnΓ(t)) at t ≳ 10⁶⁰ (dps 30); fixed with the Stirling series for |t| > 10⁴. p > 1 probe
  outputs not re-run.
- **Rule A** (ROUTE2_xframe1 §7): Ψ ≡ 1, p → 1 limits of ℓ̂/B/monodromy, D̃ near the negative axis, strip, α_x = 0, k^ρ, top end.
  No counterexample.
- **Rule L:** not done. Novelty UNCHECKED.
- **Open:** GAP-rate₁ (tilt law).
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan54.md; main line correct; all fixes LOW/INFO; all three checks reproduced
  bit-for-bit). Fixes applied: F1 Lemma 3.5 rate at p = 1 is g − log z = O(|z|^{−1}log|z|) (first moment of μ* diverges), argument
  unchanged — added to §1's p-dependent list and the transfer table; F2 X2 reworded (only Lemma 3.2(v) and its uses fail; Lemma 1.1's
  non-uniformity never needed), OBSTRUCTION scoped to "RH_px §4.1 as written"; F3 Rule N note: the old D̃ formula is O(1) wrong for
  10²⁵ ≲ t ≲ 10⁶⁰, catastrophic near 10⁶⁶; reviewer's re-run of the REVIEWED p > 1 probes (check_px_e2e (2,3), (1.5,3), (3,2.5);
  check_px_bessel) with the fix is digit-identical — no reviewed conclusion affected (plt1 precedent); F4 Stirling guard note
  (check_x1_frame [4] unaffected); F5 e2e = pure power outside the discs; F6 dated notes at the stale GAP-int places (PROOF.md §0
  RII₁ row, G1-R row, §3.19 "Remaining (GAP)"; ROUTE2_p1.md label table and §7; ROUTE2.md §6) — THEOREMS.md left to the
  coordinator; F7 numerics wording (E up to 0.5006, E spread 1.9·10⁻⁸, r = 1.5 e2e row with all three N); F8 LnΓ branch wording.
  Rule R ACCEPT WITH FIXES (review/REVIEW_Plan54.md), fixes applied — REVIEWED.

## 2026-10-15 — Plan 55 (any strip: the O(1/n)-rate results under analyticity in an arbitrarily thin strip) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan55.md), fixes applied — REVIEWED
- Write-up: PROOF.md §3.24 (Theorem AS) and §0 row "AS (Plan 55)"; paper: papers/paper2 revision 3 (NOTES.md "Revision 3").
  Plan: docs/superpowers/plans/2026-10-15-plan-55-strip.md.
- **Result.** For every p > 0, s > 1: if Ψ₁ = exp L₁(log t) with L₁ analytic on {Re u ≥ −c₀, |Im u| ≤ ϑ} for **some** ϑ > 0
  (real, bounded for Re u ≤ 0, L₁′ → 0) — (A_ϑ) — then n^pb_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n). Previously
  (H_an) |Im u| ≤ π/p (p > 1), (H_an^{<1}), (H_an^{x1}) π/2, (H_an₁) π (p = 1, band centre). PROVED-mod-cite (inherits RII,
  RII_{<1}, RII_x1); proof of record papers/paper2 rev. 3 + PROOF.md §3.24 audit (ROUTE2*.md do not prove AS as written).
- **Mechanism.** Paper 2 Lemma 5.7: the weight is evaluated only in Z_n = {|arg z| < ϑ_w}; the lens leaves 0 at ϑ_lip, the
  Bessel rays are at ±(π − ϑ_lip), and KMVV's angle freedom (CITATIONS "(KMVV, angle freedom; Plan 15b)": any angle in (0, π))
  lets ϑ_lip → 0. Scaling the old angles by m = min(1, pϑ/ϑ_w⁰) keeps (5/4)ϑ_lip < ϑ_w < π/2, ϑ_w < πp/2 (p < 1) and gives
  ϑ_w ≤ pϑ.
- **Audit** (PROOF.md §3.24 table, 26 locations): decay factors sin(ϑ_lip/2), sin(¾ϑ_lip/p); Lemma 5.5(iii) needs ϑ_w/p < π/2;
  Lemma 5.6 (corner rounding in the open set G₊, h₁ with arcsin(h₀/4c) < ϑ_w); Table 1; Binet-cut (|arg z| < π/2 only), p = 1
  reflection ((O5) |arg u| ≤ π − ¾ϑ_lip), seams (lens inside S_in; τ₀ = sin(πp/2 − ϑ_w)); Lemma 6.3 (convex sector, |arg z| ≥
  ½ϑ_lip separation); Frame Proposition; §7 Bessel model (DLMF 10.40 used on |ph 2ζ^{1/2}| ≤ ½(π − ϑ_lip), a closed subsector
  of |ph| < π/2 for fixed ϑ_lip > 0; Hankel formulas in the thin sectors), Lemmas 7.1, 7.3; App. B (φ₁ = ½ϑ_lip,
  sin(ϑ_lip/p)), App. C (angle-free star lemmas), App. D; Airy edge independent of ϑ_lip (confirmed). **No minimum angle.**
  Upper bounds only internal: ϑ_lip < (4/5)ϑ_w, ϑ_w < min(π/2, πp/2 for p < 1) and ≤ pϑ.
- **Scope.** Verified on Paper 2's write-up (x-frame, all p). ROUTE2*.md as written use wider strips; the band-centre (§3.19) and
  fold (§3.22) proofs were not re-examined; their conclusions are covered via RII_x1. Dated Plan 55 notes added (no history
  rewritten) in PROOF.md §§3.17, 3.19–3.23, ROUTE2*.md (6 files), THEOREMS.md §§2.7–2.8.
- **Numerics** (`RH/route2/checks/check_p55_strip.py/.out`, NUMERICAL): p = 2, L₁(u) = √(u+1) + (u+2)^{−1/2}log(1 − q cos 2u),
  q = 1/cosh 0.6 (singular at u = πm ± 0.3i for every m: (A_ϑ) only for ϑ < 0.3; the old (A_{π/2}) fails). n = 50…3200 (25
  points), five truncations (spread ≤ 2·10⁻⁹): s = 2: n(n²b_n/c − 1) ∈ [−0.603, −0.029], s = 3: [−1.101, −0.549]; max modulus
  on the disjoint windows 50 ≤ n < 400 / 400 < n ≤ 3200: 0.598 / 0.589 (s = 2), 1.097 / 1.088 (s = 3) — log-periodic, bounded,
  but only ≈ 1.3 periods covered (weak evidence against growth); n(a_n/(2b_n) − 1) ∈ [−1.009, −0.951].
- **Rule A:** minimum-angle search, order of smallness choices, domain of ε₁, choice of a test function with singularities
  along the whole strip boundary. No counterexample.
- **Rule L:** not done. Novelty UNCHECKED.
- **Rule R:** ACCEPT WITH FIXES (review/REVIEW_Plan55.md; no mathematical error, no hidden minimum angle; all fixes LOW/INFO;
  numerics reproduced, Lanczos cross-check identical). Fixes applied: F1 numerics on disjoint windows + ≈ 1.3 periods caveat
  (PROOF.md §3.24, this entry, Paper 2 §9); F2 label "proof of record papers/paper2 rev. 3 + §3.24 audit; ROUTE2*.md do not prove
  AS as written" (§0 row, §3.24, THEOREMS.md); F3 DLMF 10.17.5–6, 10.17.11–12 read and quoted verbatim (CITATIONS
  "(DLMF-10.17, Plan 55)"), cited in Paper 2 §7.2 and T4; F4 OUTLINE.md / NOTES.md ϑ_p notes, check_p55_strip.py/.out copied to
  papers/paper2/checks, absolute path in NOTES.md removed; F5 order-of-choices sentence in Remark 5.8; F6 "half-angle" in the
  abstract and §1; F7 Rule N note in the script header. Rule R ACCEPT WITH FIXES (review/REVIEW_Plan55.md), fixes applied —
  REVIEWED.
