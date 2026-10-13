# Plan 12: RH analysis in the x-variable — pointwise Law P for σ_{p,s}, p > 1

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native). Steps use checkbox (`- [ ]`)
> syntax. This is a multi-session research plan with gates, like Plan 10.

**Goal.** Prove n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n) for

  σ_{p,s} := Σ_{k≥1} k^{−s} δ_{k^{−p}},  p > 1, s > 1.

Together with RH₁(r) (p = 1, merged in Plan 11), this gives the pointwise Law P for the model family for all p ≥ 1.

**Why the x-variable** (RH.md §6.4, Gate 3 finding, option (a)).
- In the symmetric variable the index function t = N(z²)^{−1/p} has a branch cut on iℝ unless 2/p ∈ ℤ, so WLXZ's
  D-functions do not transfer. Plan 10's p = 2 attempt was REJECTED on exactly this point (review/REVIEW_RH.md
  §6.2–6.3).
- In x the index function is t(x) = N x^{−1/p} (rescaled). Its cut is (−∞, 0], which carries no nodes. For p > 1,
  arg t = −arg x/p stays in (−π, π), so Γ(t) has no poles in the slit plane.
- **Key observation (to verify in Phase 3).** V's cut on (−∞, 0) comes from the D-functions, and its jump there is
  diagonal: D₊/D₋ = exp(μ(t₋) − μ(t₊)), with μ the Binet function. At the hard edge x = 0 this is absorbed exactly,
  with no truncation, into the Bessel parametrix's W := (x^{a}h(x))^{1/2}·D-factor. The parametrix's own jump on
  (−δ, 0) is diagonal, W₋^{σ₃}e^{±aπiσ₃}W₊^{−σ₃}, so it reproduces V's jump exactly.
  - This avoids RH₁(r)'s Stirling-truncation mechanism, which does not extend to p ≠ 1: there the Binet terms
    (z²)^{(2k−1)/p} are not entire.
  - Far out on (−∞, 0) the jump is O(1). It is removed by a scalar Szegő function on (−∞, 0] together with the
    band, with an E-type power normalization at ∞ (RH.md §6.2's exponent (p−1)/(2p)).
- **Cost.** The accumulation point x = 0 is now a *hard edge* of the band (0, 4c(p)). The density of μ* is ~ x^{−1/2}
  there (each arcsine law in G2's superposition contributes x^{−1/2}). This needs the Bessel hard-edge parametrix
  (KMVV, arXiv:math/0111252, §6), with infinitely many nodes accumulating at the edge. RH₁(r)'s Lemmas M, O1, X are
  the templates for the mismatch and identification steps.

**Out of scope.** 0 < p < 1: arg t then leaves (−π, π) and Γ's poles enter the slit plane on the rays
arg x = ±pπ. General non-analytic weights remain GAP (G1 PROOF.md §4).

**Spec.** §7 G1; G1/PROOF.md §4 ("most promising next step"); RH.md §§0–6; RH_p1.md, RH_p1_general.md (templates).

## Global Constraints

- AGENTS.md rules. Commit prefix `G1:`. Branch `plan-12-RH-general-p`. Work in `research/G1/RH/px/`
  (RH_px.md, checks/, LOG entries in research/G1/RH/LOG.md).
- Rule C: every external theorem is quoted with its hypotheses in research/G1/RH/CITATIONS.md from a source actually
  read (KMVV must be downloaded and read before use).
- Rule N: every analytic object (t, θ, Π, g, φ, D, s, N, parametrix matchings) gets a numerical check.
- Rule R before any PROVED label. Do not run pip installs; use .venv.

## Review Focus

1. **D on the slit plane.** Analyticity and nonvanishing for p > 1. The exact form of the jump on (−∞, 0). Behaviour as
   x → 0 (|t| → ∞) and as x → −∞ (t → 0).
2. **Scalar Szegő on band ∪ (−∞, 0].** Integrability at −∞, the power normalization, and boundedness near 0, where the
   band and the cut meet.
3. **Hard-edge parametrix with W containing D.** E analytic (no jump on (−δ, 0) or (0, δ)). Matching I + O(1/n). The
   KMVV hypotheses (h analytic in a disc), here replaced by "W analytic in the slit disc, with the exact cut".
4. **Identification at the hard edge with accumulating nodes:** the RH₁(r) §6 analogue.
5. **Extraction directly in x** (no fold): b_n² and a_n from Y₁, Y₂. Normalization check against Phase 0 numerics
   for p = 2, 3 and against RH₁(r) at p = 1 as a limiting sanity check.

---

### Phase 0: numerics baseline (reuse)
- [ ] Re-run or collect the check_fine.py data for p ∈ {1.5, 2, 3}, s ∈ {p, p+1, 2p}. Record d₁ and e₁ fits in LOG.
  Expected: O(1/n) corrections (Phase 0 of Plan 10 found d₁ = −(s−1)/2, e₁ = p/2).

### Phase 1: interpolation problem in x
- [ ] Rescale x ↦ N^p x so that nodes are X_k = (N/k)^p, the band is (0, 4c(p)) and the top node is at N^p.
  Define t(x) := N x^{−1/p}, θ := πt and Π := sin θ/θ′, and the mass function m(t) = t^{−s}·const (analytic off
  (−∞, 0]).
- [ ] Write the WLXZ §3 transformations (R with Π-factors on band and saturated sides, T with e^{ng}). There is only
  one side; the left of the band is the cut.
- [ ] Check (Rule N): residues removed, jumps of R at sample points (the Phase 3a analogue), p = 2.
- [ ] **Gate 1:** GO if R's jumps have the predicted form, including the new diagonal jump on (−∞, 0) if one
  appears at this stage.

### Phase 2: g, φ, signs
- [ ] g from G2's μ* in x (band (0, 4c), saturated (4c, ∞)). φ and φ̃. Sign charts on lips (band) and on Σ^△
  (saturated). Translate RH.md §4 from s to x.
- [ ] Check: numerical boundary values and signs, p = 2, 3. **Gate 2.**

### Phase 3: D, scalar Szegő, global parametrix
- [ ] D̃ = exp(−μ(t)) and D = D̃/(1 − e^{∓2iθ}) on the slit plane. Prove analyticity (p > 1) and the jump on (−∞, 0).
- [ ] Construct the scalar Szegő function S for: band weight (Lemma 3.1 analogue in x) and (−∞, 0) jump. Power
  normalization at ∞. Global parametrix N with a(x) = (x/(x − 4c))^{1/4}-type hard/soft structure.
- [ ] Check numerically: D's jump, S's jumps, N's jumps. **Gate 3:** all jumps outside discs at 0 and 4c are
  I + O(1/N) or I + O(e^{−cN}).

### Phase 4: local parametrices
- [ ] Read KMVV §6 (hard-edge Bessel). Build P₀ with W := (x^a h)^{1/2}·D^{±1}. Prove E analytic, matching, and the
  RH₁(r)-type mismatch and identification lemmas.
- [ ] Airy at 4c: the RH₁ step 4 construction, translated to x.
- [ ] Top end (x ≈ N^p): exponentially small jumps, as WLXZ (reliance noted).
- [ ] **Gate 4.**

### Phase 5: small norm, extraction
- [ ] Small norm. b_n² = (Y₁)₁₂(Y₁)₂₁ and a_n = (Y₁)₂₂ − (Y₂)… (standard formulas). Get n^p b_n = c(p)(1 + O(1/n))
  and a_n/(2b_n) = 1 + O(1/n).
- [ ] Check: leading constants vs Phase 0. Optional: predict d₁ and e₁.

### Phase 6: Rule R
- [ ] An independent opus reviewer on RH_px.md with all checks. Apply fixes, re-check, update G1 PROOF.md, README,
  spec and memory.

**Expected effort.** Several sessions. The highest risk is in Phases 3 (scalar Szegő with the infinite cut) and 4 (hard
edge). Any failed gate stops the project with the obstruction recorded.
