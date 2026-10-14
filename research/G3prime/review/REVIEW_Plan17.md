# Rule R review: Plan 17 (PROOF.md §8, Theorems B and C)

Reviewer: independent agent, fresh context, adversarial. Date: 2026-10-14. Branch `plan-17-g3prime-pc`, commit
ad2fa18. Scope: PROOF.md §8 (8.1–8.3), CITATIONS.md (C5), (C6), the plan. Read in full: AGENTS.md,
VERIFICATION_POLICY.md, the plan, PROOF.md §§0–8, CITATIONS.md. Sources downloaded independently and read:
GLSS arXiv:2503.15449v4 (all 10 pages), Lamzouri arXiv:2609.02882v2 (§1, Theorem 1.1, the Lemma 3.1 pointer).
Scratch script: `rr17s/greedy.py` in the session scratchpad (`.venv` python, `-I`).

## Verdict: ACCEPT WITH FIXES

- **Theorem C:** correct. The fixes are explicitness fixes only.
- **Theorem B:** the *statement* is true, but the *proof as written has a gap* at Step 4 (F1). The greedy rule does
  not give convergent density from blockwise density. Step 6 needs convergent density, because Theorem T, Remark T′
  and G3′*-L all need it.
- **Repair (F1, Fix A):** replace Steps 4–7 by the reviewed §4 argument (G3′-L, steps 2–7). Lemma S is run with a
  constant C in place of 1 + 2η. That argument needs only π(j) ≤ Cj and a uniform lower bound on forward gaps, and
  Steps 1–3 supply both. It gives liminf ≥ −3 log C, so Theorem B holds with θ₀ := C^{−3/2}.
- After Fix A, Theorem B can be marked REVIEWED without a second pass, because it reuses a REVIEWED proof with one
  constant changed. If the authors keep the G3′*-L route instead (Fix B), a re-review is needed.

## Findings

**F1 (Major: gap). §8.1 Step 4 ("Convergent density"), and Step 6, which depends on it.**

*Problem.* Step 3 gives |S ∩ (T, 2T]| ≥ c₀M_T on each dyadic block. That is positive density *per dyadic block*. It
is not the window lower density of the N′ Remarks, which asks for |E ∩ (K′, K]| ≥ δ(K − K′) − o(K) for *all*
K′ < K. Caro–Wei says nothing about where I_T sits inside the block. I_T may lie entirely in the top c₀-fraction of
(T, 2T].

*Why the greedy rule then fails.* Let E = top c-fraction of each index block (2^m, 2^{m+1}]. Run the greedy rule
"add k iff |E′ ∩ [1, k)| < δ′k" with δ′ = c/2. The density f(K)/K then stalls across the empty window
(2^m, (2 − c)2^m] and oscillates between δ′/(2 − c) and δ′. Simulation, c = 0.2, K ≤ 2²²: min 0.0556, max 0.1001,
target 0.1. There is no convergence.

*Consequences.* Theorem T needs d(K) → θ. Remark T′ needs a band ±η with η small: Lemma R needs
ε = (8η/(1−η))^{1/3} < ½. So does G3′*-L. None of them applies to E′ as constructed, and Step 7's "π(j)/j → 1/θ₀"
is unjustified for the same reason.

*Fix A (recommended).* Drop Steps 4, 6 and 7, and use the §4 proof directly.
- Let E := E_S, the first-occurrence indices of S (no thinning), enumerated by π.
- **π(j) ≤ Cj.** By Step 3 summed over dyadic blocks below γ_K/2, |E ∩ [1, K]| ≥ c₀N(γ_K/2)(1 − o(1)) ≥
  (c₀/2 − o(1))K. So π(j) ≤ Cj for j ≥ j₀, with C := 2/c₀ + 1.
- **Gap input.** In §4 step 3, the input "g_a ≥ δ" is used only as γ_b − γ_a ≥ 2πδ/log(γ_a/2π) for a < b in E.
  For S this holds with δ = ½ for large a. Elements of S are more than 2π/log(2T) apart, and log(2T) ≤ 2 log(γ/2π)
  for γ ∈ (T, 2T], T large.
- **Lemma S** holds for every η ≥ 0, not just small η. With π(a) ≤ Ca it gives the factor C⁻³.
- **The rest.** Steps 4–7 of §4 do not use the size of η. The near-partner count, the per-element cost, the weights
  ≥ c⁻¹·2x̃ and Lemma W all go through unchanged.
- **Result.** liminf (1/n²)[log D_n(σ) − Φ_n] ≥ −3 log C. So Theorem B holds with θ₀ := C^{−3/2}, or restate it with
  the constant −3 log C.
- Step 5 (monotonicity) is replaced by §4 step 2: restriction of the Heine sum to index subsets of E.

*Fix B (alternative, heavier).* Redo Steps 1–3 on blocks (T, (1 + 1/R)T].
- Using (6.1) at height (1 + 1/R)T alone gives P ≤ A′R·M on such a block. The independent-set density is then
  c(R) ≍ A⁻³R⁻³.
- The greedy rule with δ′ = c(R)/2 gives a band of relative width η ≍ 4/R.
- For R large (η < 1/65), Remark T′ plus the G3′*-L transfer give liminf ≥ 2 log δ′ − ω(4/R) > −∞. Here ω is finite
  for fixed R, although C_θ depends on θ = δ′.
- This works, but it needs a fresh check of the G3′*-L transfer under a band rather than a limit.

**F2 (Minor: incorrect sentence). §8.1 Step 1, the subtraction of (6.1) at 2T and T.**
- *Problem.* The two instances use different L: L(2T) and L(T). So the pairs with both ordinates ≤ T do **not**
  cancel, contrary to the bullet "Pairs with both elements below T cancel".
- *Sign.* Their weights satisfy w_{L(2T)} ≤ w_{L(T)}. So the difference *understates* the sum over the new pairs. That
  is the wrong direction for an upper bound.
- *Size.* The correction is ≤ (log 2/log 2T)·#{pairs ≤ T with |d|L(T) ≤ 2} = O(TL/log T) = o(TL), using (6.1) at
  λ = 4. So the conclusion survives, but the bullet is false as written.
- *Fix (simplest).* Do not subtract. All weights are ≥ 0, so (6.1) at height 2T alone gives
  P_T ≤ 2·2T·L(2T)·(2 + log 4/(2π²) + O(1)) ≤ A·M_T, with A := 4(2 + log 4/(2π²)) + O(1). This also matches §8's
  normalization |γ − γ′|L(2T). Delete the two "cancel / only enlarge" bullets and adjust the stated value of A.

**F3 (Minor: inaccurate). §8.1 Step 6 parenthetical, "they are O(n log n) in total".**
- *Problem.* In the G3′*-L proof, near-short pairs with a ≤ M₂n are o(n²), namely n·C log(M₂n). Those with
  a > M₂n are bounded by (t₀(M₂)n)² on 𝒮 via Lemma K, which is not O(n log n).
- *Fix.* Moot under Fix A. Under Fix B, write "o(n²) + log(1/(cθ₀))·t₀(M₂)²n², which vanishes as M₂ → ∞".

**F4 (Minor: Rule C presentation). CITATIONS.md (C5), Proposition 2.**
- *Problem.* Proposition 2 is Fujii's/Tsang's result *as stated by GLSS*. GLSS do not prove it ("For the proof of this
  Proposition, see Fujii … and Tsang …"). The (C5) entry does not mark it as secondary.
- *Precedent.* (C3) accepted secondary statements only with an explicit flag ("via the survey"; "that convention comes
  from the secondary source").
- *Quote.* The quoted sentence is truncated without an ellipsis. GLSS: "They both prove this unconditionally for the
  2k-th moments."
- *Fix.* Add: "Proposition 2 is a secondary statement (GLSS quoting Fujii [Fuj74, Fuj81] and Tsang [Tsa84, Tsa86]);
  the primary sources were not read. Proposition 1 (Gallagher–Mueller) is proved in GLSS §9." Restore the quote's
  ending. Under the house rules this is acceptable as it stands once flagged, in the same way as (C3).

**F5 (Minor: explicitness). §8.2 Theorem C, "Small positive gaps" bullet.**
- *Problem.* §4's g_k is normalized by log(γ_k/2π)/2π, while N(λ) at height T uses L(T). For γ_k much smaller than
  T, for example γ_k ≈ √T, the ratio log T/log(γ_k/2π) is about 2. So "L(1 + o(1)) on dyadic blocks" needs one more
  line.
- *Fix.* For fixed R, split k ≤ N(T) into two ranges:
  - γ_k ≤ T/R: at most N(T/R) ≈ K/R such k;
  - γ_k ∈ (T/R, T]: (γ_{k+1} − γ_k)L(T) < δ(1 + o(1)) ≤ 2δ.
- Apply PCC at the *fixed* λ = 2δ. This needs no λ₀ → 0 and no uniformity:
  N(2δ) ≤ TL∫_0^{2δ}(1 − (sin πα/πα)²)dα + o(TL) ≤ (8π²/9)δ³TL + o(TL), since 1 − (sin x/x)² ≤ x²/3.
- So the upper density is ≤ Cδ³ + 1/R. Let R → ∞.
- Also convert K to T := γ_K with N(γ_K) ≤ K + 2E(γ_K) (Z1). The current wording ("by GLSS's PCC estimate") points
  to the λ₀ → 0 estimate of GLSS's proof of Theorem 1. The direct PCC bound at fixed λ is cleaner and fully covered by
  the quoted PCC statement.

**F6 (Minor: labels/status). §0 status table, header line 1, §8.3.**
- *Problem.* Theorems B and C have no rows in §0. §8.3 calls B "unconditional" without noting that, like every
  result here, it is mod-input Theorem H (via H5/H6/W, or G3′*-L).
- *Fix.* Add rows:
  - B: "PROVED-mod-cite (C1), (C5; Prop 2 secondary) + mod-input Theorem H + REVIEWED (after F1 Fix A)".
  - C: "PROVED-mod-cite (C1), (C5) + mod-input PCC (GLSS form), Theorem H + REVIEWED".
- In §8.3, write "unconditional (no hypothesis on the zeros; mod-input Theorem H)".

**F7 (Low: Rule A). LOG.md.**
- *Problem.* There is no Rule A (adversarial pass) entry for Plan 17. Rule A would have caught F1, for example with
  the block-concentrated set above.
- *Fix.* Log a Rule A pass covering at least:
  - the F1 example;
  - the L(T)/L(2T) issue of F2;
  - the degenerate case where all zeros of a block are on few lines. This is handled by Step 2: |V_T| ≥ M_T/A.

**F8 (Low: wording). §8.1 Remark B3, the Lamzouri bullet.**
- *Problem.* "If (D∞) held, the own-normalized shift would be 2 log θ" is true for Φ*_n − Φ_n. But the defect
  equals 2 log θ only under (D∞) + (SG*) (G3′*-L). Under (D∞) alone, G3′*-U gives only defect ≤ 2 log θ.
- *Fix.* Say "Φ*_n − Φ_n = 2n² log θ + o(n²), with θ ≥ 0.6725 (distinct ordinates ⊇ ordinates of simple zeros on the
  line)".
- *Optional.* The 0.4075 figures in §§5–7 are now stale relative to (C6). Add a pointer from those sentences to (C6),
  without editing reviewed claims.

**F9 (Low). §8.1 Step 4 sub-bullet "θ₀ := c₀/2".** Under Fix A this is replaced by θ₀ := C^{−3/2} with C = 2/c₀ + 1.
Make the theorem statement and Remark B2 consistent with it. B2's interval becomes [−3 log C, 0].

## Checked and OK

1. **GLSS (6.1) hypotheses at λ = 2.** U = λ/L ≤ 1 and λ² ≤ L for large T. λ is fixed, so the O-term is O(TL) with
   a non-explicit constant (correctly ruled in the plan). The weight 1 − |d|L/2 ≥ ½ for |d|L ≤ 1 is right. The sum
   runs over the multiset Z, so ordered pairs include ρ = ρ′.
2. **M_T.** M_T = N(2T) − N(T) = TL(T)(1 + o(1)), and 2T·L(2T)/M_T → 2.
3. **Step 2.**
   - Σ_v H(v) = M_T (H counts with multiplicity, GLSS §7).
   - Σ_v H(v)² = #{ordered pairs on one horizontal line in the block} ≤ P_T.
   - Cauchy–Schwarz gives |V_T| ≥ M_T²/P_T ≥ M_T/A.
4. **Step 3.**
   - Each edge {u, v} yields 2H(u)H(v) ≥ 2 ordered off-line-distinct pairs, and different edges give disjoint pair
     sets. So 2|E| ≤ P_T − ΣH² ≤ A·M_T.
   - Caro–Wei plus convexity gives α ≥ n²/(n + 2|E|). Using n ≥ M_T/A in the numerator and n ≤ M_T in the
     denominator is valid (both monotone the right way), giving ≥ M_T/(A²(A + 1)).
   - The boundary deletion is O(log T) by (C1).
   - Cross-block separation is in fact > ~2 in normalized units, more than the "> 1 up to 1 + o(1)" claimed.
   - Separation in the §4/(SG*) normalization log(γ/2π)/2π is > 1 − o(1), since log(γ/2π) < log(2T).
5. **Step 5 (monotonicity).** Restriction keeps merged weights, and Heine terms are ≥ 0.
6. **Step 6, conditionally on a convergent index density** (which F1 shows is not available as written). The G3′*-L
   proof uses the full distinct list only through:
   - the density of its index set (Lemma R via T′);
   - forward-gap separation (near-short pairs, "a ≍ θ′N(γ_A)");
   - Z1/Z1′ positions;
   - (Hw) weights 2m·y ≥ c j⁻² and ≤ C log j·L(Cj) j⁻².

   All of these transfer to a sub-list with B_δ = ∅. F ≥ cθ₀δ with δ = 1 is right. Nothing uses "all distinct
   ordinates" beyond the density. So Fix B is viable.
7. **Step 7 arithmetic.** It is right *given* π(j)/j → 1/θ₀: L_{S′}(j) = (j/π(j))²L(π(j))(1 + o(1)), and
   L(π(j))/L(j) → 1 by H6(a). So Φ*_n(S′) − Φ_n = 2n² log θ₀ + o(n²).
8. **Theorem C, repeats.**
   - #{k : γ_{k+1} = γ_k, γ_k ≤ T} = Σ_lines (H − 1) ≤ Σ_lines H(H − 1) = N^⊛(T) − N(T).
   - HMH (N^⊛ = TL + o(TL)) is from the proof of GLSS Theorem 1, quoted accurately. N(T) = TL + o(TL) is GLSS (3.7).
   - So the repeats are o(TL).
   - Distinct k give distinct ordered pairs (ρ_k, ρ_{k+1}) with γ′ − γ > 0, as N(λ) requires. (SG)'s "for all K ≥ K₀"
     form follows from the upper density bound.
9. **Theorem C ⇒ G3′.** (SG) ⇒ G3′-L (REVIEWED) and G3′-U ⇒ G3′.
10. **Rule C quotes.**
    - (C5) is verbatim against the PDF for (3.6), (3.7), (4.3), PCC, Prop 2, the §6 lead-in, (6.1), (7.1), Theorem 1,
      the proof of Theorem 1 ("N(λ₀) ≪ TL∫α²dα = O(λ₀³TL)"; "N^⊛(T) = TL + o(TL) which establishes HMH") and the "do
      not assume RH" sentence. The only exception is the truncation in F4.
    - (C6) is verbatim: Theorem 1.1, C₀ = 0.67250…, C₁ = 0.83625…, and "Montgomery's pair correlation theorem in the
      unconditional form obtained by Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh (see Lemma 5 of [3])".
    - (C6)'s N_d counts distinct *zeros*, and §8 correctly distinguishes them from distinct ordinates.
11. **Framing (AGENTS.md rule 3).**
    - Theorem C is stated as an implication from a named conjecture about vertical distances. Remark C2 is
      appropriate.
    - The "simple and critical" statements are attributed citations of GLSS Theorem 1 and Lamzouri Theorem 1.1, not
      claims of this repo.
    - No RH claim was found.
12. **"Before Plan 17 the lower bound was only conditional" (B1).** Accurate. §§4–7 contain only conditional lower
    bounds (G3′-L under (SG); G3′*-L under (D∞) + (SG*)). Prop N and N′ are upper bounds or counterexamples. No
    unconditional liminf > −∞ appears earlier.

## Recommended labels

- **Theorem B.** After Fix A: PROVED-mod-cite (C1), (C5) [Prop 2 secondary] + mod-input Theorem H; REVIEWED. As
  written: GAP at Step 4. Novelty: UNCHECKED (Rule L not run).
- **Theorem C.** PROVED-mod-cite (C1), (C5) + mod-input PCC (GLSS form, no RH) and Theorem H; REVIEWED after F5.
  Novelty: UNCHECKED.
- **Remarks B1–B3, C1–C2.** Fine after F8 and F9.
