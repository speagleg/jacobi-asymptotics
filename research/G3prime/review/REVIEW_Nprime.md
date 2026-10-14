# Rule R review: Theorem N′ (Plan 16)

Reviewer: independent agent, fresh context, adversarial. Date: 2026-10-14. Branch `plan-16-g3prime-nprime`, commit
968ca8c. Scope: PROOF.md §5 (Theorem N′, its remarks, "G3′ status after N′ (the sandwich)"), status-table row N′, the
edited sentences in the stop-condition bullet (§5) and in §6. Read in full: AGENTS.md, VERIFICATION_POLICY.md, the
plan, PROOF.md §§0–7.1, CITATIONS.md.

## Verdict: ACCEPT WITH FIXES

The proof is correct. The mechanism is sound: adding atoms can only increase D_n. Upper bounds never need lower gap
bounds, so the tiny shifts η_k are harmless. G3′*-U's proof uses exactly the listed inputs. The normalization constant
is right. All findings are wording, explicitness or consistency fixes. None is a gap in the argument.

## Findings

**F1 (Medium: internal contradiction). §6, "Consequence for an unconditional proof (heuristic and NUMERICAL;
necessity is not proved)", line ~381.**
Problem: the edited bullet below this header now says "necessity proved by Theorem N′ in §5". The header still says
necessity is not proved.
Fix: change the header to "(heuristic and NUMERICAL for the own normalization; for the multiplicity normalization,
necessity of d_*(E) = 0 is Theorem N′)". Alternatively, move the N′ reference out of the heuristic paragraph.

**F2 (Low: consistency). §5 stop-condition bullet, lines ~274–277.**
Problem 1: "Theorem N′ below shows that excluding positive-density repeats is necessary" is stronger than N′ as
stated. N′ shows only that d_*(E) = 0 is necessary. This is weaker than d(E) = 0 and does not cover the residual
lower-density case.
Problem 2: the bold summary "stops at: U + L (mod (SG)) + N" was not updated, while the sandwich paragraph says
"closes as: U; L under (SG); necessity of d_*(E) = 0 by N′".
Fix: write "…is necessary in the sense d_*(E) = 0", and make the two summaries agree (add "+ N′ (d_*(E) = 0 is
necessary)").

**F3 (Low: scope of "special case"). Remarks, "Prop N is the special case".**
Problem: N′ is stated for the true-zero measure σ, and σ^{(m)} is not that measure. Also, Prop N's proof uses the
letter E for the complement ℕ ∖ {km+2}, which clashes with N′'s E.
Fix: say "The proof of N′ uses only Z1 for the positions, a multiplicity bound m_j = O(log γ) and convergence of
d(E′). σ^{(m)} has all three (Prop N (i); multiplicity ≤ 2). So the same argument gives Prop N's upper half,
limsup ≤ 2 log(1 − 1/m). Prop N also gives equality." Optionally state N′ for any ordinate list satisfying Z1 and the
multiplicity bound. The constants agree: d(E) = 1/m gives 2 log(1 − 1/m).

**F4 (Low: constants made explicit). Proof step 1–2.**
Problem: "C₀ + 1" needs η_k ≤ 1, which "tiny" does not say. Z2 also uses k₂ with γ̃_k ≥ 2C₀, which must be re-chosen
as γ̃_k ≥ 2(C₀ + 1). For small k the constant is C₀′ + 1.
Fix: require 0 < η_k ≤ 1 explicitly, for example η_k := min(1, g/2)·(i/(m_j+1)) for the i-th repeat in a block with
forward gap g. Then note the change of k₂ and of C₀′.

**F5 (Low: θ > 0 and the final limit). Steps 1, 5.**
Problem 1: Theorem T needs θ = 1 − δ′ ∈ (0, 1], so δ′ < 1 must hold. a priori d(E′) = 1 is not excluded by the
hypotheses as stated. (It is excluded by (C3), but N′ should not depend on (C3).)
Problem 2: "Take the inf over δ′ < d_*(E)" is loosely phrased. The admissible δ′ are the densities d(E′).
Fix: "Fix E′ ⊂ E with 0 < d(E′) = δ′ < 1. A subset of density δ ∈ (0,1] contains subsets of every density in
[0, δ], by the greedy rule of the Remarks. Let δ′ ↑ d_*(E)." With the convention log 0 = −∞ when d_*(E) = 1.

**F6 (Low: citation wording). Sandwich paragraph, "N_d(T) ≥ 0.4075·N(T)".**
Problem: (C3) gives "more than 40.75%", which is an asymptotic (liminf) statement from a secondary source. §6 and §7.1
write it with (1 + o(1)) or as a liminf, but the sandwich writes a bare inequality.
Fix: write "N_d(T) ≥ 0.4075·N(T)(1 + o(1)) ((C3), PRZD20 via the survey)". In one clause, add the two steps of the
derivation:
- the simple critical zeros have pairwise distinct ordinates, so N_d ≥ #(simple, on the line);
- K ≤ N(γ_K + 0) ≤ K + 2E(γ_K).

Then |E ∩ [1, K]| ≤ K − N_d(γ_K) + 1 ≤ 0.5925K(1 + o(1)). The conclusion is consistent with (C3) as recorded in
CITATIONS.md.

**F7 (Low: precision of the remark). Remarks, the counterexample to plain lower density.**
Problem: "d_*(E) can be 0" understates what holds, and the example's implicit growth condition is not stated.
Fix: assume a_{m+1} ≥ 4a_m and say "then d_*(E) = 0". Proof: if E′ ⊂ E has density δ′, then
|E′ ∩ [1, 4a_m)| = |E′ ∩ [1, 2a_m)|, so δ′ = δ′/2. Also mark "It needs a law for thinnings with oscillating density"
as heuristic. Whether the law fails in the residual case is not known either way.

**F8 (Low: weights bookkeeping). Step 2, weights bullet.**
Problem: it is not stated that the first-occurrence atom keeps its full merged weight 2m_j y_j, so the mass of the
re-added indices is counted twice.
Fix: say so explicitly. It is harmless:
- upper half of (Hw): weight ≤ 4E(γ)·c x̃_{π(j)} ≤ C log(j+2)·L(Cj)·j⁻², using j ≤ π(j) ≤ Cj;
- lower half: weight ≥ 2c⁻¹x̃_{π(j)} ≥ c′j⁻².

This is exactly the U(j) of G3′*-U.

## Checked and OK

1. **Monotonicity.** §1's convention says the Heine sum over the multiplicity-indexed list equals the Heine sum of the
   merged measure, by multilinearity in the weights of each block: subsets with two indices in one block contribute 0.
   D_n(μ) = (1/n!)∫Δ² dμ^{⊗n} is monotone in μ, because the integrand is ≥ 0. σ⁺ = σ + (added atoms) ≥ σ, so
   D_n(σ) ≤ D_n(σ⁺). The added atoms are distinct from each other and from σ's atoms, and their order matches the
   index order (η_k increasing within a block, below the forward gap). The atom index set is
   {k ∉ E} ∪ (E ∖ E′) = ℕ ∖ E′ = K⁺, with d(K⁺) = 1 − δ′. Also 1 ∉ E.
2. **Transfer of G3′*-U.** I re-read §7.1, the upper half of Theorem T, Lemma R, Lemma K, (Hw) and Z1/Z1′/Z2. Each
   input and how it holds for σ⁺:

   | G3′*-U input | Status for σ⁺ |
   |---|---|
   | d → θ via (D∞) and the bound K ≤ N(γ_K) ≤ K + 2E | Replaced by d(K⁺) = 1 − δ′ directly |
   | (P1), and with it Lemma R, (P3), (P4) | Follows from the density alone |
   | Z2 factors at k(a) < k(b) | Z2's proof uses Z1 at the two indices, the §1 concavity of γ̃ (smooth, independent of σ) and k₂ |
   | Z2 with tiny gaps | Upper bounds only, so tiny gaps (γ⁺ − γ = η) are harmless; no lower gap bound is used anywhere (G3′-U Remark) |
   | Z1′ (λ_y/L̃_E(Mn) → 1, and the right-hand-side comparison) | Holds for the shifted positions |
   | Multiplicity bound m_j ≤ 2E(γ*_j) | Used only in the weights, and still true because the merged weights are σ's |
   | (C1) / N(T) counting | Enters only through Z1 and the density of the first-occurrence set, which is replaced |
   | Both halves of (Hw), needed by H7 and Lemma K | Hold (F8) |

   No step uses that the atoms are true zeros beyond these points.
3. **Normalization.** L⁺(j) = j²x⁺_{π(j)} = (j/π(j))²L(π(j))(1 + o(1)) by Z1′ for the shifted positions.
   - j ≤ π(j) ≤ Cj by (P1).
   - H6(a) gives |log L(π(j)) − log L(j)| ≤ ε*(j) log C → 0.
   - Then 2Σ_{j<n}(n−j)·[2 log(1−δ′) + o(1)] = 2 log(1−δ′)·n(n−1) + o(n²) = 2n² log(1−δ′) + o(n²).

   Signs and constant are correct.
4. **Direction.** limsup[log D_n(σ) − Φ_n]/n² ≤ limsup[log D_n(σ⁺) − Φ*_n(σ⁺)]/n² + lim(Φ*_n(σ⁺) − Φ_n)/n²
   ≤ 2 log(1−δ′). The bound decreases in δ′, so the best bound comes from δ′ ↑ d_*(E). This is consistent with Prop N:
   d = 1/m gives 2 log(1 − 1/m).
5. **Greedy construction under window lower density.**
   - Upper bound: c(K) ≤ δ′K + 1 by induction.
   - Lower bound: take K′ to be the last k ≤ K with c(k−1) ≥ δ′k. Every element of E in (K′, K] is added, so
     c(K) ≥ δ′K′ + δ(K − K′) − o(K) ≥ δ′K − o(K), because δ > δ′.

   So d(E′) = δ′. This needs the o(K) to be uniform in K′, which the stated form gives.
6. **Framing (AGENTS.md rule 3).**
   - Ordinates are treated as inputs, with no RH framing.
   - "No surveyed result reaches" matches the CITATIONS.md (C3) wording policy.
   - "As hard as a known open problem" is explicitly not claimed.
   - The statement that a repeated ordinate comes from a multiple zero or from two zeros on one horizontal line is
     correct.
7. **Label.** PROVED-mod-cite (C1, through Z1) + mod-input Theorem H (through G3′*-U → Theorem T, H7, Lemma K) is
   right. (C3) is not used in the theorem, only in the sandwich commentary. Optionally list "T upper, H7" in the
   Depends-on column.
8. **NUMERICAL sanity probe** (reviewer's, not part of the proof; rkpw double, J = 2·10⁵, same pipeline as
   `checks/check_merge.py`). This tests the "law fails" direction for non-evenly-spread E′ of density 0.3, against the
   bound 2 log 0.7 = −0.713:

   | Repeats | n = 250 | n = 500 | n = 1000 | n = 2000 |
   |---|---|---|---|---|
   | random | −0.533 | −0.540 | −0.555 | −0.559 |
   | clustered (blocks of 200) | −0.852 | −0.748 | −0.682 | −0.645 |

   Both behave like the evenly spread rows of check_merge.out [1], which converge slowly: φ = 0.25 reaches −0.467 at
   n = 4000 against −0.575. Neither contradicts an asymptotic bound. The script is in the reviewer's scratchpad; it is
   not added to the repo.

## Recommended label

After F1–F8: **Theorem N′ — PROVED-mod-cite + mod-input Theorem H + REVIEWED**. Novelty: UNCHECKED. Residual
(positive lower density with d_*(E) = 0) stays **GAP**. Update the "pending Rule R" text in the header (line 4), in the
status row and in the theorem title.

## Re-check (2026-10-14, commit 9f30955)

Each fix was checked against `git show 9f30955` (PROOF.md §§0, 5, 6).

| Finding | Status | Note |
|---|---|---|
| F1 | Resolved | The §6 header now restricts "heuristic" to the own normalization and cites N′ for the multiplicity one. |
| F2 | Resolved | "in the sense d_*(E) = 0" is added, and the bold summary now includes "+ N′". |
| F3 | Resolved | "Relation to Prop N" lists the three inputs and the notation clash, and gives the generalization. |
| F4 | Resolved | η_k := min(1, g/2)·i/(m+1) lies in (0, g/2) ∩ (0, 1) and increases in i, so the atoms are distinct and ordered. C₀′ + 1 and the re-choice of k₂ are stated. |
| F5 | Resolved | δ′ < 1 is now required, and "δ′ ↑ d_*(E), log 0 := −∞" is used. The subset-density claim follows from the greedy rule, because a set of density δ has window lower density δ: both counts are δK + o(K). |
| F6 | Resolved | (1 + o(1)), the provenance (PRZD20 via the survey) and both derivation steps are added. |
| F7 | Resolved | a_{m+1} ≥ 4a_m, the proof that d_*(E) = 0, and "not known either way" plus the heuristic tag are added. |
| F8 | Resolved | The double counting is stated, with both halves of (Hw). |

Residual: none. The fixes introduce no new issue. The REVIEWED label set by the coordinator is **confirmed**: Theorem N′
is PROVED-mod-cite + mod-input Theorem H + REVIEWED, and the residual case (positive lower density, d_*(E) = 0) stays
GAP.
