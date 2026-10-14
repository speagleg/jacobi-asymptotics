# Rule R review: Plan 26 (Theorem Ch, §5.4)

Reviewer: independent second reader (Rule R), 2026-10-14. Branch `plan-26-charact`, commit 3e5a91c.
Scope: PROOF.md §5.4 (Theorem Ch: definitions, (i), (ii), corollaries N″/N‴/L′/sliver, remarks Ch1–Ch2), the status
row "Ch", the "(Ch)" bullet, README edits, the LOG Plan-26 entry, the plan's review focus, and
`checks/check_clusters.py/.out`.
Building blocks taken as REVIEWED: Z1, Z2, G3′-U (§3); G3′-L, Lemma S, Lemma W (§4); Lemma Tr, Theorem L′ (§4.1);
Lemma H, Lemma Sat, N″ (§5.2); N‴ (§5.3); Lemma K (§7).

## Verdict

**ACCEPT WITH FIXES.** Both directions are correct, and together they give G3′ ⟺ 𝒞(K) = o(K²) (mod (C1) and
Theorem H, given G3′-U). I found no counterexample and no gap that needs a new idea. All findings are presentation
fixes, missing bookkeeping steps that are each a line or two, stale cross-references, or numerical typos.
- The necessity proof is clean. Grouping by T = S ∩ W replaces the move map, because repeat pairs get P = ∞
  automatically.
- In the sufficiency proof, the n-dependent good set is legitimate, but one cost (the weights) is not written down
  (F3).

## Verification summary (what was checked and how)

**(ii) Necessity.**
- *Step 1, near-pair factor.* For a ≥ k₂, x_a − x_b ≤ 2(γ_b − γ_a)/γ_a³, since |dx/dγ| = 2γ/(γ² + ¼)² ≤ 2/γ³.
  - A near pair has b − a ≤ 1 + (2C₀/π)log((γ̃_a + 4C₀)/2π) = O(log a), so b ≤ C″a for all a ≥ k₂, and
    G(a) − G(b) ≥ 2(b − a)/b³ ≥ c′a^{−3}.
  - With γ_b − γ_a = 2πd_ab/log(γ_a/2π), γ_a ≍ a/log a and Λ ≥ L(1), this gives ε_ab ≤ C(log a)²d_ab. ✓
  - The proof says b ≤ 2a. That is true only for large a, and finitely many a can be absorbed into C (F1).
- *The min(ρ*, ε) replacement.* min(ρ*, ε) ≤ ρ*·min(1, ε), since ρ* ≥ 1. The ρ* product is the uniform
  e^{O(n log²n)} of G3′-U step 3, so term_σ(S) ≤ e^{O(n log²n)}Λ^{n(n−1)}term_ν(S)Π_near min(1, ε_ab)². ✓
  - The phrase "drop nonnegative terms 2 log ρ*" is slightly loose when ε_ab > 1, where ρ* is kept, but the bound is
    right (F1).
  - Repeated pairs give ε = 0 and term 0, consistent with P = ∞.
- *P_ε ≥ P − C|T| log n log log n.* log⁺(x/c) ≥ log⁺x − log c for c = C(log a)² ≥ 1. The number of near partners
  per element is O(log K) by the *smooth*-ordinate definition, uniformly in T. ✓
  - Defining "near" through γ̃ is what makes this count deterministic.
- *Grouping.* Σ_{S∩W=T}term_ν(S) ≤ Σ_{S∩(W∖T)=∅}term_ν(S) = D_n(ν ∖ (W ∖ T)), because the terms are nonnegative.
  The near-pair factor depends on S only through S ∩ W. ✓
- *Lemma H and Lemma Sat.* They are applied to ν with head G(j) = j^{−2} for j ≤ Mn and tail ≤ (Mn)^{−2}.
  - For k ∈ W ∖ T: 1 ≤ k₂ ≤ k ≤ K = ⌊θn⌋ < n, log(W_{>n}/w_k) = O(log n), and g is decreasing on (0, ½].
  - I checked g′(θ) = log(θ/(1−θ)) − 2/θ + 1 < 0 there. ✓
- *Entropy.* 2^{|W|} ≤ e^{θn log 2} = e^{O(n)}. ✓
- *Bracket vs 𝒞(K).* 2P ≥ P. For drops, 2n·g(θ) ≥ θn ≥ K, but the O(log n) is not absorbed. At θ = θ_c,
  2ng(θ_c) = θ_c n exactly, so the bracket is ≥ 𝒞(K) − O(n log n), not ≥ 𝒞(K). This is harmless (F2).
- *θ_c.* mpmath gives θ_c = 0.29256… (root of 2g(θ) = θ), and θ₀ = 0.31538…. Since g is decreasing,
  2g(θ) ≥ θ on all of (0, θ_c]. ✓ ("≈ 0.29".)
- *Scales and order of limits.* With n := ⌈K/θ⌉: K ≤ θn < K + θ, so ⌊θn⌋ = K. Distinct K give distinct n → ∞. The
  sequence of K depends only on ε, not on M.
  - The bound is A₂²/(8 log M) − θ²(c − ε) + o(1) along these n. Then M → ∞, then ε → 0. ✓
  - c ≤ 1 automatically, since 𝒞(K) ≤ K·|W| ≤ K².

**(i) Sufficiency.**
- *Per-n good set.* This is legitimate. Each D_n(σ) is bounded below separately. Every constant (C₀, k₂, the near
  count, the far-pair O(log²n), Lemma Tr's C′) is uniform, and only the shift D_n of π_n varies.
  - Lemma S is a per-a statement (π(a) ≤ (1+η)a for *that* a, η ≥ 0 arbitrary). So η_j := (π(j) − j)/j is
    allowed, including small j where π(j)/j is large. ✓
  - G3′-L's j₀ device is not needed.
- *Drop count.* D_n ≤ 𝒞(Mn)/(Mn) = o(n), because P ≥ 0. ✓
  - T_n has no repeated near pair, since P(T_n) < ∞.
  - Far pairs have γ_b − γ_a ≥ 2C₀ > 0 by Z1, so all atoms indexed by T_n are distinct.
- *Near cost.* The lower pair ratio is ≥ (γ_b − γ_a)/(4C₀)·(1 + 2C₀/γ̃_a)^{−5}. Its log-cost is
  ≤ log⁺(1/d_ab) + log(C log γ_a), and it is a gain when the ratio is > 1. ✓
  - Over S ⊂ T_n, 2P(T_n) bounds the energy part uniformly in S.
  - #(near pairs in S) ≤ Cn log(Mn), so the remainder is O(n log n log log n). ✓
- *Far pairs.* G3′-L step 4 applies verbatim, since the m-th far partner has b − a ≥ m in any subset of ℕ. ✓
- *Lemma S total.* Per pair the cost is 3 log(1 + D′/j) in the *difference*, so 6 log(1 + D′/j) in the squared
  Heine factor (F3), with D′ := D_n + k₂ (F3). Over S′ = {j_1 < … < j_n} in rank space, j_p ≥ p and monotonicity
  give ≤ 6n Σ_{j≤n}log(1 + D′/j).
  - Σ_{j≤n}log(1 + D/j) ≤ ∫_0^n log(1 + D/x)dx = D log(1 + n/D) + n log(1 + D/n) ≤ D(2 + log(n/D)).
  - So the total is O(n·D log(n/D)) = o(n²) for D = o(n). ✓ (The text's "D(1 + log(n/D))" is off by an additive D,
    which is harmless.)
- *L∘π ≥ L, ε* nonincreasing.* Both follow from π(j) ≥ j. ✓
- *Lemma Tr and Lemma W.* J = |T_n| ≥ Mn − k₂ − D_n ≥ (M/2)n for M ≥ 8, and the weights j^{−4} are fixed. ✓
  - liminf ≥ −C′/log(M/2) for each M. Then M → ∞. ✓

**Exhaustiveness.** limsup 𝒞(K)/K² ∈ [0, 1], and the two cases are = 0, covered by (i), and > 0, covered by (ii). So
the equivalence is exact, given G3′-U.
- *Robustness.* The drop price K could be any cK. For c ≤ 1, 𝒞_c ≤ 𝒞 ≤ 𝒞_c/c, so the o(K²) condition does not
  depend on the price.
- *k₂.* It enters only through finitely many indices.
- *Multiplicity.* Equal ordinates are always near: |γ̃_b − γ̃_a| ≤ 2C₀ < 4C₀ for a ≥ k₁. So they give P = ∞ inside T,
  as intended.

**Corollaries.**
- *N″.* Correct, and in fact stronger than stated. Any two indices with one value form a near pair with d = 0, so at
  most one index per value is kept. Hence #drops ≥ |E ∩ (k₂, K]| and 𝒞(K) ≥ ηK² − o(K²) along a subsequence. The
  stated η/2 is also true. The equivalence recovers N″ only qualitatively, with constant θ_c²η < c*η (F7).
- *N‴.* Correct if the pairs (k, k+1), k ∈ T_β, are taken disjoint (spacing ≥ 2, as in N‴ step 1), so that one drop
  cannot serve two pairs. This needs saying (F6).
  - (k, k+1) is near, since γ̃_{k+1} − γ̃_k ≤ g-term + 2C₀ < 4C₀.
  - d_{k,k+1} = g_k exactly, so the kept cost is ≥ βk with no −O(log log k).
- *L′.* Correct, and slightly simpler than stated. For b > a, d_ab ≥ g_a exactly (ordinates are nondecreasing), so
  log⁺(1/d_ab) ≤ log⁺(1/g_a) with no O(1). Only the smaller index needs to lie off B_η.
- *Sliver.* Correct, *provided the other gaps are bounded below* (g_k ≥ δ for the remaining k), which the text leaves
  implicit (F5).
  - Then any near pair with b ≥ a + 2 straddles a normal gap: d ≥ cδ, at O(1) cost, over O(K log K) pairs.
  - The disjoint tiny pairs give 𝒞(K) ≥ Σ_{k≤K, tiny} min(k/log k, K) ≍ K²/(4 log K). So 𝒞 ≍ K²/log K, both ways.
  - The example is a hypothetical ordinate sequence satisfying (C1). Ch applies to it because its proof uses only
    (C1) and Theorem H. Say so (F5).

**Numerics.** I re-ran `check_clusters.py` from the jacobi-asymptotics venv (mpmath, 300 digits). The output is
identical to the committed `.out` (see the end of this file). Increments from ε = 10⁻² to 10⁻⁸:
- m = 2: 14.19 + 13.10 = 27.29 ✓ (27.3).
- m = 3: 49.42 + 32.54 = 81.96 ✓ (82.0).
- **m = 4: 96.51 + 54.53 = 151.04, not 150.8** (F8).
- 2 log 10⁶ = 27.63 ✓.

The saturated values are 77.68 / 146.95 / 209.29, against the predictions 78.13 / 139.03 / 186.31 ✓ (F8 on the
wording).

## Findings

**F1 (minor; §5.4 (ii) step 1).**
- "b ≤ 2a" holds only for a ≥ a₀. Elsewhere, use b − a = O(log a), hence b ≤ C″a, or absorb the finitely many
  a < a₀ into C.
- The replacement is better stated as min(ρ*, ε) ≤ ρ*·min(1, ε), with the ρ* product bounded by G3′-U step 3,
  rather than "drop nonnegative terms 2 log ρ*".
- *Fix:* one sentence each.

**F2 (minor; (ii) step 3).** "Since 2n·g(θ) ≥ θn ≥ K, the bracket is ≥ 𝒞(K)" ignores the −O(log n) in the drop
price. At θ = θ_c the inequality 2ng(θ) − O(log n) ≥ K fails.
- *Fix:* "the bracket is ≥ min_T[P(T) + (K − C log n)|W ∖ T|] ≥ 𝒞(K) − CK log n = 𝒞(K) − o(n²)".

**F3 (moderate, bookkeeping; (i) step 4).**
- (a) **Weights are not accounted for.** L′ step 5 used w_{π(j)} ≥ c j^{−2}, via π(j) ≤ C_η j. Here π_n(1) can be
  ≈ D_n (if T_n drops the first D_n indices), so that bound fails for small j.
  - The cost is still small: x̃_{π(j)}/x̃_j ≥ c(j/π(j))², and over S it is ≤ 2Σ_{p≤n}log(1 + D′/p) + O(n)
    = O(D′ log(n/D′)) + O(n) = o(n²).
  - It must be written down.
- (b) π(j) ≤ j + D_n should read π(j) ≤ j + D_n + k₂ − 1, since T_n ⊂ [k₂, Mn]. Use D′ := D_n + k₂.
- (c) The Lemma S cost per pair is 3 log(1 + D′/j) in the *difference*, so 6 log(1 + D′/j) per squared Heine
  factor.
- (d) Σ_{j≤n}log(1 + D/j) ≤ D(2 + log(n/D)), not D(1 + log(n/D)).
- None of these changes the o(n²) conclusion. *Fix:* add the weight line, and replace D_n by D′ := D_n + k₂ with
  the factor 6.

**F4 (minor; notation, (i)).** D_n denotes both the Hankel determinant D_n(σ) and the drop count
|[k₂, Mn] ∖ T_n|, in the same proof (e.g. "D_n(σ) ≥ …" next to "D_n := |…|").
- *Fix:* rename the drop count, e.g. δ_n or Δ_n.

**F5 (minor; corollary "former sliver").** The claim that the other near pairs have normal distances needs an
explicit hypothesis: g_k ≥ δ > 0 for the remaining k (otherwise P may be larger). The example is a hypothetical
sequence, not ζ.
- *Fix:* "for an ordinate sequence satisfying (C1) with g_k = e^{−k/log k} on odd k and g_k ≥ δ on even k, Ch
  applies (its proof uses only (C1) and Theorem H), and 𝒞(K) ≍ K²/log K".
- Optionally add the matching lower bound from the disjoint pairs.

**F6 (minor; corollary N‴).** "Each such pair is either dropped (cost K) or kept" adds costs over pairs, so the pairs
must be disjoint. One drop could otherwise kill two overlapping pairs.
- *Fix:* "Take a subset of T_β with spacing ≥ 2 (N‴ step 1), of upper density ≥ η/2". Also note d_{k,k+1} = g_k, so
  the kept cost is ≥ βk with no correction.

**F7 (minor; status row, "(Ch)" bullet, Corollaries header).**
- "Contains N″, N‴, L′": the containment is *qualitative*. Via Ch, N″ gives liminf ≤ −θ_c²η, weaker than N″'s
  −c*η = −0.2397η, and N‴'s explicit bound is likewise not recovered. Say "qualitatively".
- The N″ corollary can be stated with η instead of η/2 (each value keeps at most one index).
- The row's "Depends on" omits Z1, Z2 and Lemma S. Add them.

**F8 (minor; Remark Ch1 numerics).**
- (a) The m = 4 increment is 151.0, not 150.8. *Fix:* "151.0".
- (b) For m = 4, the model min_s[…] is already capped at ε = 10⁻⁸: the minimum is at s = 2, value 175.87. So the
  comparison "6 × 27.6 = 165.8" is not in the uncapped regime; the model's own increment is 175.87 − 55.26 = 120.6.
  - *Fix:* note this, or restrict the pair-count comparison to m = 2, 3.
- (c) "Saturates near the cost of dropping m − 1 slots": for m = 4 the loss exceeds the summed single-deletion costs
  by 12%.
  - This direction is what Lemma H predicts: joint deletion costs at least the sum of single costs.
  - *Fix:* say "≥, consistent with Lemma H".

**F9 (minor; stale cross-references in PROOF.md).** These still say the window is open or unproved:
- L′1 "What remains (F4)" (line ≈310);
- N‴1 "Open: the window between those two conditions" and the heuristic "Σ min(log⁺(1/g_k), K) = o(K²) … Not
  proved" (lines ≈609–612);
- the status paragraph "G3′ closes as: U unconditional; L under (SG); necessity of d(E) = 0 by N″" (line ≈722).
- *Fix:* add "(superseded by Theorem Ch, §5.4)" pointers.
- Also note in N‴1 or Ch1 that 𝒞 is pair-based, not gap-based. A cluster of m ≍ log k points at mutual distance ε has
  gap sum (m − 1)log(1/ε) but pair energy ≍ m² log(1/ε). So the N‴1 heuristic condition is not equivalent to
  𝒞 = o(K²) in general.

**F10 (minor; Remark Ch2).**
- "It holds under (SG), PCC, RH + (V⁺), SPC_ℂ⁺, by the earlier theorems": say how. Those theorems give G3′, and then
  Ch(ii) (contrapositive) gives 𝒞 = o(K²), mod Theorem H. (SG) and (LG*) also imply it directly (L′ corollary).
- "𝒞 depends only on the ordinates" should add: and on the fixed constants C₀, k₂. The o(K²) condition does not
  depend on them, by the theorem itself.

**F11 (minor; LOG Plan-26 entry).**
- It says "group by T = S ∩ [1, θn]" and "≤ e^{−2P(T)}·D_n(ν ∖ (W ∖ T))". PROOF uses W = [k₂, K] and P_ε. Align them.
- "Rule R: pending" should be updated after fixes.

**F12 (minor; README).** "~~Sufficiency gap~~: closed by Theorem Ch" is accurate as an *exact characterization*. The
added clause "what remains is to decide that condition for ζ, which implies proportion-one distinct ordinates" is
correct: 𝒞 = o(K²) ⇒ d(E) = 0, via the N″ corollary or directly, since each repeat forces a drop of price K.
- After acceptance, change "Rule R pending" to REVIEWED.
- Keep "mod Theorem H" visible in the README line; it is currently implicit.

## Things checked and found fine (no action)
- The grouping inequality, the 2^{|W|} entropy, θ_c = 0.2926, and the −θ²c constant.
- The order of limits in (ii); the per-n good set in (i); Lemma S with a-dependent η.
- The near count O(log n) per element (smooth-ordinate definition), and the P_ε vs P correction o(n²).
- d = 0 excluded from T_n (P < ∞), and no repeated ordinates among far pairs (Z1).
- J ≥ (M/2)n for Lemma Tr, and the exhaustiveness of (i)/(ii) (c ∈ (0, 1]).
- The L′ corollary (even without the O(1)).
- No move map is needed in (ii), because repeat pairs are handled by P = ∞. This is correct and simpler than
  N″/N‴.

## Recommended labels
After F1–F12 (all local edits):
- **Theorem Ch:** PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED (after re-check); novelty UNCHECKED.
- **Corollaries N″/N‴/L′/sliver:** PROVED (qualitative), same labels.
- **Remark Ch1:** NUMERICAL (exact, illustration only).
- **Remark Ch2:** heuristic / interpretive; the "holds under …" clause is PROVED via Ch(ii) and the cited theorems.

Novelty: UNCHECKED. Pair-energy and keep-or-drop functionals resemble log-energy and determinantal-process arguments;
no literature search was done.

## Re-run of check_clusters (reviewer)
`.venv/bin/python ../ja-plan26/research/G3prime/checks/check_clusters.py` from jacobi-asymptotics: output
byte-identical to the committed `checks/check_clusters.out`. θ_c, θ₀ recomputed with mpmath findroot:
θ_c = 0.292563190…, θ₀ = 0.315379374….

## Re-check (commit a3f920f)

Reviewer: same Rule R reader, 2026-10-14. Verified each fix against §5.4, the Ch row, L′1, N‴1, the G3′ status
paragraph, LOG and README (diff 3e5a91c..a3f920f).

**Verdict: ACCEPT.** F1–F12 are applied correctly. One cosmetic wording item remains (R1); it is optional.

| Finding | Status | Note |
|---|---|---|
| F1 | ✓ | "b ≤ 2a for large a, small a into C"; min(ρ*, ε) ≤ ρ*·min(1, ε) with ρ* keeping its uniform bound. |
| F2 | ✓ | bracket ≥ 𝒞(K) − O(n log n), using \|W ∖ T\| ≤ n; o(n²), so step 4 is unchanged. |
| F3 | ✓ | Δ′ = Δ_n + k₂, factor 6, sum ≤ 6nΔ′(2 + log(n/Δ′)) = o(n²). Weights checked below. |
| F4 | ✓ | Δ_n rename (Δ′ is used without its subscript in two lines; harmless). |
| F5 | ✓ | hypothetical (C1) sequence, g_k ≥ δ elsewhere, Ch applies via (C1) + Theorem H. |
| F6 | ✓ | disjoint pairs, spacing ≥ 2, d_{k,k+1} = g_k, kept cost ≥ βk. |
| F7 | ✓ | "qualitatively" in the row and in the corollaries; −θ_c²η vs −c*η; Depends-on adds Lemma S, Z1, Z2. The N″ corollary is now ηK² (one drop per repeated index; the boundary at k₂ is O(1)). |
| F8 | ✓ (see R1) | 151.0; the m = 4 capped-regime caveat is stated; saturation is compared with summed single deletions. |
| F9 | ✓ | L′1 "What remained … now closed by Ch"; N‴1 window closed, heuristic "superseded: pair-based"; the status paragraph adds Ch. |
| F10 | ✓ | constants C₀, k₂ and price independence; "holds under …" via those theorems + Ch(ii) contrapositive; pair- vs gap-based. |
| F11 | ✓ | LOG uses W = [k₂, ⌊θn⌋] and P_ε; Rule R line updated. |
| F12 | ✓ | README has "(mod Theorem H)" and "ACCEPT WITH FIXES, re-check pending". |

**F3 weight line, checked.** For j ≥ Δ′: (j + Δ′)^{−2} ≥ (2j)^{−2} ≥ j^{−4}/4, a constant factor.
- For j < Δ′: (j + Δ′)²/j⁴ ≤ (1 + Δ′/j)², so the loss is ≤ 2 log(1 + Δ′/j) per element.
- The p-th element of S has rank ≥ p, so the total is ≤ 2Σ_{p<Δ′}log(1 + Δ′/p) = O(Δ′) = o(n).
- The stated O(Δ′ log(n/Δ′)) is a valid overestimate. ✓

**R1 (cosmetic; Ch1).** "the loss saturates at 77.7, 147.0 and 209.3. That is *at or above* the summed single-slot
deletion costs 78.1, 139.0 and 186.3".
- For m = 2 the loss (77.68) is slightly *below* 78.13.
- Lemma H's superadditivity is for exact deletion, whereas the clustered configuration merges weights. So it is a
  heuristic guide here, not a prediction.
- *Suggested wording:* "close to (m = 2) or above (m = 3, 4) the summed single-slot deletion costs … (cf. Lemma H's
  superadditivity for exact deletion)". No mathematical consequence.

**Not required (from the first pass, left as is).** The L′ corollary keeps "+ O(1)" and "+ O(K log K)". These are
valid overestimates.

**Final labels.**
- **Theorem Ch (§5.4):** PROVED-mod-cite (C1) + mod-input Theorem H; Rule R ACCEPT WITH FIXES, fixes applied,
  re-check ACCEPT — **REVIEWED**; novelty UNCHECKED.
- **Corollaries N″/N‴/L′/sliver:** PROVED (qualitative recoveries), same labels; REVIEWED.
- **Remark Ch1:** NUMERICAL (exact, mpmath 300 digits; illustration only). The reviewer's re-run is byte-identical.
- **Remark Ch2:** interpretive. Its "holds under …" clause is PROVED via the cited REVIEWED theorems and Ch(ii).

**Status strings to update to REVIEWED** ("re-check pending" → "re-check ACCEPT — REVIEWED"):
- the §5.4 heading;
- the Ch row;
- LOG Plan-26 "Rule R";
- README;
- plan T4.
