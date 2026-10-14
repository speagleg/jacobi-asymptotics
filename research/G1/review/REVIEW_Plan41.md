# Rule R review: Plan 41 (Theorem Ra, §3.12)

Reviewer: independent agent (Rule R), 2026-10-14. Branch `plan-41-ra`, commit 79c69a7 (`git diff master...HEAD`).
Scope: research/G1/PROOF.md §3.12 (Lemma Toda, Lemma R2a, Definition H/I, Lemma R1a, Theorem Ra, remarks), §0 row
**Ra**, research/G1/LOG.md (Plan 41 entry), docs/superpowers/plans/2026-10-14-plan-41-ra.md (Review focus, item by
item), research/G1/checks/check_ra.py / .out. Compared against FV (§3.2), Sat_p⁺ (§3.3), TL (§3.4), FVa (§3.5),
Theorem R / R1 / R2 (§3.6), TV / LP (§3.8). Also compared against the parallel branch `plan-40-lr` (§3.11, Lemma LRa),
which overlaps.

## Verdict

**ACCEPT WITH FIXES (minor only).** Every step re-derived. No mathematical error found. The crux question
(R1a needs the joint law of (q_N, q_{N+1}) at the atoms?) resolves in the write-up's favour: it does **not**. The lower
bound in R1a step 3 is pointwise in each atom and depends only on u_k² + v′_k², so only the marginal μ_N + μ_{N+1}
enters, and LP's weak convergence of that marginal suffices. The findings are presentation, labelling and
merge-coordination items. None changes a statement.

## Checks performed

1. **Lemma Toda.** Re-derived. (Rec)·q_n gives (x − a_n)μ_n = E_n + E_{n−1} with E_{n−1} = b_nq_{n−1}q_n. So
   ΔE_n = (x − a_n)μ_n − 2b_nq_{n−1}q_n = 2E_n − (x − a_n)μ_n, which pairs with f to give exactly FVa's right side.
   The index conventions agree with §3.5: b_n couples q_{n−1} and q_n; b_0 = 0; E_{−1} = 0, so n = 0 is consistent.
   ⟨1, E_m⟩ = 0 and ⟨x, E_m⟩ = b_{m+1}² also check.
   - The independent derivation is correct. The range of K_m(t) is e^{tf/2}·Range K_m(0), so
     K̇ = (1−K)(f/2)K + K(f/2)(1−K). Then (1 − K_m)XK_m = b_mq_mq_{m−1}ᵀ (only Xq_{m−1} leaves the range), so
     Ṫ_m = Φ_{m−1}.
   - Tr(XK_m) is finite rank, so trace-class issues for p ≤ 1 do not arise.
2. **Lemma R2a.**
   - **q̇.** From TV's q̇_j = ½fq_j − K_j(fq_j) − ½⟨fq_j, q_j⟩q_j, splitting ½fq_j along K_j, q_j, 1 − K_{j+1} gives
     q̇_j = ½(1 − K_{j+1})fq_j − ½K_jfq_j. The two pieces are orthogonal, so ‖q̇_j‖ ≤ ½‖fq_j‖ ≤ ½‖f‖_∞. **Correct.**
   - **ḃ.** FV gives ḃ_{m+1} = ½b_{m+1}⟨f, μ_{m+1} − μ_m⟩, so |ḃ_{m+1}| ≤ b_{m+1}‖f‖_∞. **Correct.**
   - **Constant.** |Φ̇_m| ≤ b_{m+1}(‖f‖² + ½‖f‖² + ½‖f‖²) = 2b_{m+1}‖f‖², which gives 2(b_n + b_{n+1}). **Correct.**
   - **Centering.** Replacing f by f − c rescales the weight by e^{−ct}, so q, a, b are unchanged. Φ_m is unchanged
     too, since ⟨1, E_m⟩ = 0. So inf_c is legitimate; it equals ½ osc f.
   - **Numerics.** The ratio is 0.005–0.10.
3. **H and I.**
   - **Zero set.** Re-derived. The cases u = 0 and v = 0 force z = 0. When uv ≠ 0, z² = 4. All three points are
     attained (φ = π/2, π/4, 3π/4). Restricting to φ ∈ [0, π] suffices because the forms are even under (u, v) ↦ −(u, v).
   - **Homogeneity.** |2uv′ − zu²| + |zv′² − 2uv′| ≥ H(z)(u² + v′²) holds by homogeneity. I also checked it on random
     samples: the minimum ratio is 1.0000001.
   - **Lipschitz constant.** H is in fact 1-Lipschitz (F3).
   - **I > 0.** Correct. The integrand is continuous and ≥ 0, and it vanishes only at θ ∈ {0, π/2, π}.
   - **Value of I.** Independent quadrature gives I ≈ 0.3139 (8001-point φ grid). The script reports 0.3140, so the
     two agree.
4. **Lemma R1a.**
   - **Step 1.** Both formulas are exact. ΔE_N = 2Buv′ − (x − a_N)u². ΔE_{N+1} = (x − a_{N+1})v′² − 2Buv′, using the
     second form of Toda at N and the first at N + 1, with the same B = b_{N+1}.
   - **Step 2.** Expanding, N^pΔE_N = c(2uv′ − zu²) + 2(N^pB − c)uv′ + (N^pa_N − 2c)u², and similarly for N + 1.
     With 2|uv′| ≤ u² + v′², |r_N| + |r′_N| ≤ τ_N(u² + v′²). This is right, with no slack lost.
   - **τ_N → 0.** This needs N^pb_{N+1} → c and N^pa_{N+1} → 2c. Both follow from the pure-power laws, since
     (N/(N+1))^p → 1.
   - **Crux (cross terms).** Step 3 bounds each atom from below by c·H(z_k)(u_k² + v′_k²). That is a deterministic
     inequality valid for every pair (u_k, v′_k). So no information on the joint law of (q_N, q_{N+1}), or on phases,
     is needed. The sum involves only ⟨H(z), μ_N + μ_{N+1}⟩. The vanishing set {−2, 0, 2} matters only through I > 0.
   - **Step 4.** ∫x^jdμ_m = (J^j)_{mm} holds for any measure with moments. The moments of μ_{N+1} under N^p scaling
     use a_m, b_m with |m − N − 1| ≤ j. Moment convergence to a compactly supported (determinate) limit gives weak
     convergence. The test function min(1, H((y − 2c)/c)) is bounded and continuous on [0, ∞).
   - **Substitution.** y = 2c(1 + cos θ) pushes uniform dθ/π to the arcsine density 1/(π√(y(4c − y))), and
     (y − 2c)/c = 2cos θ. So the limit is 2I. **Correct.**
   - **Step 5.** Correct, including ‖m^pΔE_m‖₁ ≥ ‖N^pΔE_m‖₁ for m ≥ N.
5. **Theorem Ra.**
   - **Step 1.** FV gives |d log b_m/dt| ≤ ½‖g‖·2 ≤ ε, so b_m(ve^g) ≤ e^εb_m(v). e^{1/16} < 2, so n₁ depends only on
     p and s. 𝒮 = {ve^g : |g| ≤ ε} is exactly the set of path points used.
   - **Step 2.** The Taylor remainder is ≤ ½ sup|ä|, and n^p|ä| ≤ 2·4c·ε², which gives 4cε². **Correct.**
   - **Step 3.** The atomwise bound |ΔE_n| ≤ ½b̄(μ_{n−1} + 2μ_n + μ_{n+1}) is correct.
     - Head: k < θn ≤ n/2 ≤ m and k/m ≤ 2θ for m ≥ n − 1, n ≥ 2. Sat_p⁺ applies with W/w_k ≤ e^{2ε}ζ(s)k^s, uniformly.
     - Tail: TL at index n + 1 bounds ρ_{n+2}-tails, and μ_{n−1}, μ_n, μ_{n+1} ≤ ρ_{n+2} by monotonicity of ρ_m. The
       sandwich constants are C/c = e^{2ε}, and γ = κ + 1 > κ.
     - So ω(n) → 0 uniformly over 𝒮. **Correct.**
   - **Step 4.** For j < i, W_j ⊂ [1, n_{i−1}^γ] ⊂ [1, θn_i), since θn_i > (i − 1)n_{i−1}^γ ≥ n_{i−1}^γ. For j > i,
     W_j ⊂ [θn_{i+1}, ∞) ⊂ (n_i^γ, ∞). Good indices exist in every pair {N, N + 1}. **Correct.**
   - **Steps 5–6.**
     - The path ve^{f_i + t(f − f_i)} stays in 𝒮 because the supports are disjoint.
     - Toda applies at an arbitrary finite-moment base.
     - supp(f − f_i) ⊂ A_{n_i}, and W_i^c = A_{n_i}.
     - Both error terms are εω(n_i). **Correct.**
   - **Step 7.** 4cε² ≤ εcI/4 ⇔ ε ≤ I/16. Then εη_a − 4cε² ≥ εcI/4 = εη_a/2. **Correct.**
   - **limsup and liminf.** Both follow, from the even and the odd i respectively (infinitely many of each), together
     with n^pa_n(v) → 2c.
6. **Labels.**
   - Toda and R2a PROVED: they use only Rec, FV and TV, which are internal.
   - R1a and Ra PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b), with the same citation basis as T3a and LP. These labels
     are appropriate.
   - I ≈ 0.314 is correctly marked NUMERICAL. The proofs use only 0 < I ≤ 1.
7. **Numerics.** Re-ran check_ra.py (about 75 s). The output is byte-identical to check_ra.out, and every quoted
   number matches up to the trivia in F6.

## Findings

**F1 (minor, merge coordination; §3.12 Toda, R2a; parallel branch plan-40-lr §3.11).** Plan 40's Lemma LRa (step 4)
already contains the Toda/Lax form a_n′ = b_{n+1}γ_n − b_nγ_{n−1}. That is the same identity as Lemma Toda. Plan 40
also proves |ä_n| ≤ ε²(b_n + b_{n+1}) with ε = ½ osc f = inf_c‖f − c‖_∞. That bound is 2× sharper than R2a, and would
give ε₀ = I/8. Neither branch cites the other.
*Fix:* whichever merges second adds a cross-reference: "Toda = LRa step 4; R2a is LRa with constant 2". Optionally
note that LRa improves ε₀ to I/8. Keep R2a as is (it is correct and self-contained). Section numbering 3.12 assumes
§3.10 (Plan 39) and §3.11 (Plan 40) merge first. Check the order at merge.

**F2 (minor, R1a step 4 / §0 row "via Lemma LP").** R1a uses the *proof* of LP (weak convergence of the rescaled
μ_N), plus a variant for μ_{N+1} with N^p scaling. LP's *statement* gives only tail masses. The argument is right
(re-checked), but a load-bearing step should not rest on another lemma's proof text.
*Fix:* add a one-line statement "Lemma LP′ (weak form): for fixed i ∈ ℤ, the image of μ_{N+i}^v under x ↦ N^px
converges weakly to ν", with the moment argument quoted from LP. Then cite LP′ in R1a and in the §0 row.

**F3 (trivial, Definition H).** "H is 2-Lipschitz" is true but loose. Each term changes by ≤ |z − z′|cos²φ and
≤ |z − z′|sin²φ, so H is 1-Lipschitz (numerically: 1.0000).
*Fix:* say 1-Lipschitz, or keep 2 and add "(1 also works)".

**F4 (minor, LOG and plan T3 wording).** "Lemma LP's weak convergence to the arcsine law (no atoms) finishes" suggests
that absence of atoms is used. It is not: the test function is continuous, and positivity comes from I > 0 directly.
*Fix:* drop "(no atoms)", or replace it with "(continuous test function)". Also say explicitly, in R1a or a remark,
that the joint law of (q_N, q_{N+1}) is not needed (only u² + v′² enters). This is the point readers will question.

**F5 (minor, remark Ra-a).**
- (a) "Running R and Ra on interleaved scales would break both at once; not written out." This is plausible (the
  cross-scale bookkeeping of R and Ra is the same), but unproved.
  *Fix:* label it HEURISTIC (or "expected; not proved").
- (b) "the tail-Cesàro a-law A4′ … holds for this w." A4′ is PROVED-mod-cite (P) (through G2 B*(iii)).
  *Fix:* add "(A4′, PROVED-mod-cite (P))" so the remark does not read as unconditional.

**F6 (trivial, numerics transcription).**
- (a) Ra-e [4] quotes "±0.0985…0.1077 at ε = 0.2". 0.1077 is the first-order value. The observed jumps are
  0.0985–0.1069. *Fix:* 0.0985…0.1069.
- (b) check_ra.py prints "n₁ = 40 on [10, 100]" but uses [10, 99] (PROOF.md says [10, 99], correctly).
  *Fix:* the print label.
- (c) No K-doubling run for [3] and [4] (Rule N spirit; §3.2 [2] shows a polynomial tail beyond 6n). These numbers are
  illustrative only and nothing depends on them. *Fix (optional):* one K = 40n rerun at n = 100 for [3], or a note
  "not K-checked".

**F7 (trivial, Ra-c / R1a remark (i)).** "explicit constant η_a" is explicit up to N₀, which is not explicit (it comes
from the rates in the pure-power laws). Ra-b already says this for Ra.
*Fix:* add "(N₀ not explicit)" to R1a remark (i).

## Plan Review-focus items (each checked)
- **Toda.**
  - Atomwise identity: OK.
  - Index conventions (b_n couples q_{n−1}, q_n; b_0 = 0): OK.
  - Agreement with FVa: exact.
- **R2a.**
  - Orthogonal decomposition and ‖q̇_j‖ ≤ ½‖f‖: OK.
  - FV bound on ḃ: OK.
  - Constant 2(b_n + b_{n+1}): OK.
  - Invariance under f ↦ f − c: OK.
- **R1a.**
  - ΔE_{N+1} formula: exact.
  - τ_N: OK.
  - Zero set of H (cases u = 0, v = 0, uv ≠ 0): OK.
  - Continuity of H: OK (1-Lipschitz).
  - LP proof used for μ_N and μ_{N+1} under N^p: OK (F2 for presentation).
  - Substitution giving I: OK.
- **Ra.**
  - Step 1 (b ≤ e^εb(v) along every path in 𝒮): OK.
  - Step 2 constant 4cε²: OK.
  - Step 3 head/tail, uniform over 𝒮 (Sat_p⁺ with k/m ≤ 2θ; TL at n + 1): OK.
  - Scale separation and ∪_{j≠i}W_j ⊂ A_{n_i}: OK.
  - ε₀ = I/16 and the final inequality: OK.
  - limsup and liminf both: OK.
- **Scope.** The b-law and a_n/(2b_n) are not claimed. I is NUMERICAL. Both are correctly stated.

## Recommended labels (after F1–F7 are applied)
- Lemma Toda: PROVED (standard; novelty not claimed) + REVIEWED.
- Lemma R2a: PROVED + REVIEWED (note: superseded in constant by LRa once Plan 40 merges).
- Lemma R1a: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal LP) + REVIEWED.
- Theorem Ra: PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, TV, LP, Sat_p⁺, TL) + REVIEWED.
- Novelty: UNCHECKED (Rule L not run).
- I ≈ 0.314: NUMERICAL.

The fixes are wording, cross-references and labels only. A light re-check, a diff read of F1–F7, is enough.
