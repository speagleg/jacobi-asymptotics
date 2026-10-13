# REVIEW_G3prime: Rule R second reading of research/G3prime (Plan 7)

- **Reviewer.** An independent second-reader agent (opus), 2026-10-13. It edited no repo files.
- **Read line by line.** PROOF.md §0–§5, CITATIONS.md, LOG.md and checks/*; item 11 PROOF.md §1, §2, §7 and §7b; the
  Lean `heineD_eq_det` hypotheses.
- **Citations.** Both sources were re-read from their PDFs: arXiv:1208.5846v2 and arXiv:2501.14545v3. The quotes match
  verbatim.
- **Re-runs.** check_shift, check_ratio and check_merge [1]–[3] all reproduce the committed `.out` files.
- **Reviewer's own adversarial numerics** (NUMERICAL):
  - Z2 against synthetic sequences with |γ − γ̃| ≤ C₀ (random, ±C₀, extreme pairs): 0 violations, minimum slack 2e−4.
  - Lemma S at the extremal π: minimum ratio 1.00007, never < 1.
  - Lemma W: the s-scaling of log det ζ(2(i+j)+s) at n ≤ 24 and dps 400 confirms an (s−3) n log n loss.
  - Prop N indexing: max |π − ψ| = 1, and ξ(log h)′ ∈ [−2.94, −1.96].

## Verdicts

| Result | Verdict | Required fixes |
|---|---|---|
| Z1 | ACCEPT WITH FIXES | (1) the multiplicity bound is 2E, not 2E+1; (2) prove C₀ analytically: the ratio is decreasing, since E′(u)(u−c) − E(u) < 0 with u = log T, so C₀ = value at 10⁶ = 2.6613; (3) state the all-k form with C₀′ := max(C₀, max_{k<k₁}\|γ_k − γ̃_k\|); (4) (C1): "with multiplicity" follows from Trudgian's πN(T) = Δ arg ξ (argument principle), not from the quoted sentence |
| Z2 | ACCEPT WITH FIXES | the "small indices" bound must hold for a < k₂ and every b > a |
| G3′-U | ACCEPT | minor: state c₂ = 2cL(1); make labels consistent with N |
| S | ACCEPT | minor: add the extremal configuration to check_shift |
| W | ACCEPT | minor: the reference weights are exactly π⁻²k⁻² and π⁻⁴k⁻⁴; state the uniform O(1/j) bound |
| G3′-L | ACCEPT WITH FIXES | (1a) ℓ_n(a) needs an extra C′(1+log n)² term (far partners of small a); (1b) the near-pair count is min(n−1, ·), giving ≤ C′(1+log a)(1+log n) also for a > eⁿ; (2) the weight bound becomes c₃e^{−C″(1+log n)²}j^{−s_n}; (3) use π(j) ≤ C_η j, not (1+2η)j + j₀; (4) write out the lower sum/denominator factors: ≥ 1 − C₀/γ̃_a ≥ (1+2C₀/γ̃_a)⁻¹ and (γ̃/(γ̃+C₀))² ≥ (1+2C₀/γ̃)⁻²; (5) split the far-partner bound into b ≤ a+n and b > a+n |
| N | ACCEPT WITH FIXES | (1) prove (log h)′ = O(1/ξ) directly from h = 2γγ′/(γ²+¼)², γ′ = 2π/log(γ/2π); (2) take sups over the interval between u and u′, which lies in [1,∞); (3) (i) "better constant" is wrong (7.5 > 2.7): the shift is ≤ 2π/log(γ̃_{i−1}/2π) → 0. Minor: \|π − ψ\| ≤ 1, with a one-line proof; "same counting function up to O(1)" |
| N′ (statement) | ACCEPT WITH FIXES | drop "equivalent to density-one simplicity": N′ + L would sandwich G3′ between (SG) and density-zero repeated ordinates. A repeated ordinate ≠ a multiple zero: by (C3) §1.3, horizontal multiplicity H(γ) also counts symmetric pairs. Retitle the LOG stop condition; hardness is not established (GAP N′). §5: "must use information beyond (C1), e.g. …" |

Review Focus 1–5: all OK. The one caveat is item 2, which needs the explicit all-k sentence.

**Overall verdict: ACCEPT WITH FIXES.** Every required fix is local, and the stated conclusions survive. After the fixes,
Z1, Z2, G3′-U, S, W, G3′-L and N may be marked REVIEWED. N′ stays GAP, with the corrected framing.

(Condensed from the reviewer's full report, as relayed in the session. Every required fix is listed above.)
