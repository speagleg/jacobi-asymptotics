# REVIEW_Plan27: Rule R second reading of G1 §3.1 Theorem CL (Plan 27), 2026-10-14

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files except this one.
- **Scope.** research/G1/PROOF.md §3.1 (Lemma Sat_p, Lemma WC, Theorem CL, Corollary A4′, Remarks CL1–CL3); the G1
  status-table rows A4, CL and G1-R; the §4 edit; the G1 LOG Plan-27 entry; the README G1-R line; the plan
  docs/superpowers/plans/2026-10-14-plan-27-cl.md; checks/check_cl_rough.py/.out. Context read: G1 §3 (A2–A4), G2
  §§0–3 (𝒜, I, scaling, B0, B*, A1, A2, A-U, A-L), G3′ §5.2 (Lemmas H and Sat).
- **Re-runs.**
  - `check_cl_rough.py` reproduces `check_cl_rough.out` byte-identically (49 s).
  - Scratch `sat.py` (mpmath, 400 digits, Stieltjes/Christoffel on 120 atoms): exact 1 − ρ_n(k) against Lemma
    Sat_p's bound for p ∈ {1.25, 1.5, 3}, weights k^{−2} and k^{−2}(1 + ½(−1)^k), n ∈ {12, 24, 40}, every k < n.
    **No violations.** The bound is far from tight, as expected. For example, p = 3, n = 40, k = 1 gives C = 695.4 against 639.5.
  - Scratch `idx.py`: the pointwise ratio with the repo's indexing convention (finding F6).

| Result | Verdict | Required fixes |
|---|---|---|
| Lemma Sat_p | ACCEPT | — (minor wording, F7) |
| Lemma WC | **ACCEPT WITH FIXES (Major)** | F1: the parameters are circular (c′ depends on R, and R must be large in terms of 1/c′); prove a gap uniform over all of 𝒜 (x-variable compactness), then choose t₀ and then M; F2 |
| Theorem CL | ACCEPT WITH FIXES | F3: make the partition explicit (the layer is already covered by (a)) |
| Corollary A4′ | ACCEPT | — |
| Status table / §3 / §4 / README / LOG | ACCEPT WITH FIXES | F4 (stale text), F5 (labels) |
| Numerics | ACCEPT WITH FIXES | F6: off-by-one index in the pointwise ratio |

**Overall: ACCEPT WITH FIXES.** Lemma Sat_p and the three-region argument of Theorem CL are correct. Lemma WC has a
real gap in the order of its quantifiers (F1). The statement is true, and the repair below is standard and short.
It also makes the 𝒜^R u.s.c. step unnecessary. After F1–F6, I recommend REVIEWED after a re-check of the rewritten
Lemma WC.

## Verification notes (what was checked and holds)

**Lemma Sat_p.**
- *Reduction.* G3′ Lemma Sat's first display holds for any finite-mass discrete μ whose head atoms x_1 > … > x_n are
  distinct and whose other atoms lie in (0, x_n). For x_k = k^{−p} this holds. Also ρ_n(k) = w_kK_n(x_k, x_k) = P_n(k ∈ S),
  by Lemma H's single-deletion case together with Heine. Replacing W_{>n} by W only weakens the bound.
- *Factor bounds.* x_j/|x_j − x_k| = k^p/|k^p − j^p|. For p ≥ 1 and j > k,
  j^p − k^p = j^{p−1}j − k^{p−1}k ≥ j^{p−1}(j − k), since k^{p−1} ≤ j^{p−1}. The case j < k is symmetric. The j < k
  product is k^{k−1}/(k−1)! = k^k/k! ≤ e^k. The j > k product is k^{p(n−k)}/((n−k)!(n!/k!)^{p−1}).
- *Constants.* With k = θn, log Π ≤ θn + p(1−θ)n log(θn) − (1−θ)n log((1−θ)n) + (1−θ)n
  − (p−1)(n log n − n − θn log(θn) + θn).
  - The log n coefficient is p(1−θ) − (1−θ) − (p−1) + (p−1)θ = 0.
  - The remainder is n[p + (p−θ)log θ − (1−θ)log(1−θ) − (p−1)θ] = −n·g_p(θ). This is exactly the stated g_p.
  - At p = 2 it is (2−θ)log(1/θ) + (1−θ)log(1−θ) − 2 + θ, which is G3′'s g.
- *Monotonicity.* g_p′ = log θ − p/θ + 1 − log(1−θ) − 1 + p − 1 = log(θ/(1−θ)) − p/θ + p − 1, as stated. On (0, ½)
  both parts are negative, since −p/θ + p − 1 < −p − 1. Also g_p → ∞ as θ → 0.

**Lemma WC.** I checked the following and they are correct.
- 𝒜^R is weakly compact. Mass 1 is kept because 2R ≥ 1 and the support is compact, and μ(I) ≤ |I| passes to limits.
- The uniform tail estimate ∬(k − L)⁺dμdμ ≤ 2p∫_0^{e^{−L/p}} log(1/u)du holds uniformly on all of 𝒜.
- The maximum over a closed subset of a compact set is attained, and μ*_u lies outside the bad set, so
  sup < κ_p for fixed R.
- *Scaling step.* μ′(B) := μ̄_H(τB)/τ has density ≤ 1, and its support is in [0, R/τ] ⊂ [0, 2R]. We have
  ⟨φ, μ̄_H⟩ = τ∫φ(τu)dμ′. The bound (1 − τ)‖φ‖ + ω_φ(2R(1−τ)) is correct, since φ(u) and φ(τu) both vanish for
  u > 2R.
- *Energy step.* I(μ̄_H) = τ²(I(μ′) − p log τ) ≤ τ²(κ_p − p log τ) − 2c′τ², and τ² ≥ ½ makes this ≤ … − c′.
- *Insertion into G2.* Inserting into Corollary A2 (via A1, with N(N−1) and the scaling) lowers the head bound by
  exactly c′n². The cross-pair and tail factors of A-U do not depend on whether H is bad. The sum over m < t₀n adds
  only log n.
- *The t ≥ t₀ branch.* At − pt² log M ≤ t(A − pt₀ log M) ≤ −At₀ once pt₀ log M ≥ 2A.
- *A-L.* Its hypothesis w ≥ c₁k^{−s} is exactly the setting.

**Theorem CL.**
- *Identity.* 𝔼_n[Σ_{k∉S}x_k] = Σ_k k^{−p}(1 − ρ_n(k)), and n^{p−1}Σ_k k^{−p}(·) = ∫u^{−p}d(λ_n − m_n).
- *(a) Saturated part.* For k ≤ θn ≤ n/2, monotonicity gives g_p(k/n) ≥ g_p(θ) ≥ 1. The bound
  n^{p−1}Σ_{k≤θn}(W/c₁)k^{s−p}e^{−2n} = O(n^{p+s}e^{−2n}) holds. On the limit side ρ* = 1 on (0, θ] ⊂ (0, u_s] (G2 B*(i)).
  Note that Sat_p is needed only for θ small (g_p(θ) ≥ 1). The whole region [θ, u_s] is handled by WC, because u^{−p}
  is bounded there.
- *(b) Middle.* u^{−p}χ ∈ C_c((0, ∞)), so WC gives ⟨u^{−p}χ, m_n⟩ → ∫u^{−p}χρ*du.
- *(c) Tail.* The tail bound R^{1−p}/(p−1) + o(1) holds.
- *Limit.* The limit is Q_p by A3.

**Corollary A4′.** Σ_{j≥n}a_j = 𝔼_{n−1}[Σ_{k∉S}x_k] by A2, and (n/(n−1))^{p−1} → 1. Correct.

## Findings

**F1 (Major — Lemma WC, steps 1–3: the parameter choice is circular).**

*Issue.* The constants are chosen in this order:
- R is fixed with supp φ ⊂ (0, R].
- c′ = c′(R) is the energy gap on the bad part of 𝒜^R.
- t₀ is chosen with At₀ ≤ c′/2, and small enough for the φ-comparison.
- Step 2 needs pt₀ log R ≥ 2A, with M := R, so that the t ≥ t₀ branch is exponentially small.

So R must satisfy log R ≥ 4A²/(p·c′(R)). Enlarging R is allowed, since supp φ ⊂ (0, R] persists. But 𝒜^R grows with
R, so c′(R) is non-increasing. Nothing in the text shows that c′(R) stays bounded below, or even decays more slowly
than 1/log R. The u.s.c./compactness argument is confined to 𝒜^R, and it cannot see mass escaping to u = ∞.
Decoupling M from R (tail cut at Mn, compactness on 𝒜^{2M}) has the same problem. As written, the proof does not
close.

*Fix.* Prove the gap uniformly over all of 𝒜:

  sup{I(μ) : μ ∈ 𝒜, |⟨φ, μ⟩ − ⟨φ, μ*_u⟩| ≥ δ/4} =: κ_p − 2c′ < κ_p.

Do it in the x-variable, where this is the standard compactness argument.
- Suppose μ_j is in the bad set and I(μ_j) → κ_p. Put ν_j := g_*μ_j ≤ σ. Then ν_j((X, ∞)) ≤ X^{−1/p} uniformly, so
  (ν_j) is tight on [0, ∞).
- Pass to a subsequence with ν_j → ν weakly on [0, ∞), where ν is a probability measure.
- The kernel log|x − y| is u.s.c. and bounded above on compacts. Its positive part is uniformly integrable, since
  log⁺|x − y| ≤ log(1+x) + log(1+y) and σ has a finite log moment. Hence limsup I(μ_j) ≤ ∬log|x − y|dν dν.
- An atom of ν at x = 0 (mass escaping to u = ∞) forces the right side to be −∞. So ν({0}) = 0, ν ≤ σ on (0, ∞),
  and ν pulls back to 𝒜 with energy ≥ κ_p. By B*(iii), ν = μ*.
- Since φ∘g⁻¹ ∈ C_c((0, ∞)), ⟨φ, μ_j⟩ → ⟨φ, μ*_u⟩. This contradicts badness.

Then c′ = c′(φ, δ) does not depend on R or M.
- Choose t₀ from c′ and from the φ-comparison. The comparison uses ω_φ(2R(1−τ)), with R tied to supp φ only.
- Then choose the tail cut M ≥ R with pt₀ log M ≥ 2A.
- Step 3 needs μ′ ∈ 𝒜 only. Its support lies in [0, M/τ], which is irrelevant now.

This also removes the need for 𝒜^R and the u-variable u.s.c. argument (F2). The finite log moment and the
u.s.c. are already used in G2 B*(iii) via (P) §1, so no new citation is needed.

**F2 (Minor — Lemma WC step 1, u.s.c.).** "Each truncation is weakly continuous on [0, 2R]²" is not literally true.
- max(min(k, L), −L′) is discontinuous at the corner (0, 0). Along u = v it equals −L′. Along u = v/2 it tends to L.
- It is continuous elsewhere: near the diagonal it is −L′, and near u = 0 with v > 0 it is L.
- The corner is μ⊗μ-null for μ with density ≤ 1. So ∫f dμ_j⊗μ_j → ∫f dμ⊗μ still holds, by the continuous-mapping
  form of the portmanteau theorem.
- Say so, or drop the step entirely under F1's fix.

Also say "uniform limit of u.s.c. functions" explicitly. I is the uniform limit (error ≤ 2p∫_0^{e^{−L/p}}log(1/u)du)
of I_L := inf_{L′}∬max(min(k, L), −L′).

**F3 (Minor — Theorem CL proof, the partition).** (a), (b) and (c) overlap on [θ(1−ε), θ) as written. Write instead
1 = χ + (1 − χ), where 1 − χ is supported in (0, θ) ∪ (R, ∞).
- On (0, θ), 0 ≤ ∫u^{−p}(1−χ)d(λ_n − m_n) ≤ ∫_{(0,θ]}u^{−p}d(λ_n − m_n), which tends to 0 by (a). This uses
  λ_n − m_n ≥ 0.
- The separate "layer" estimate is then unnecessary. It is harmless, but as stated it double-counts.
- The limit side is the same, with 1 − ρ* = 0 on (0, θ).

**F4 (Moderate — stale text elsewhere in G1/PROOF.md).** Only the "Missing statements" bullet of §4 and the table
were updated. The following passages still say (CL) is open or out of reach, which contradicts §3.1:
- §3 "*Status of (CL).*" (after A4): "it is not written here"; "**(CL) is the precise missing lemma for the a_n side**".
- §4 "Where G1 stands": "… conditional on (CL) (A4)".
- §4 "Why the tools here stop short" 1: "(CL) likewise needs single-atom exclusion probabilities … below n²
  resolution". CL1 now refutes this as a limitation.
- §4 "Stop condition": "The remaining G1 statements (T3) and (CL) are not reached …"; "The precise missing statements
  are (T3) and (CL) above."
- The file header "Status: REVIEWED 2026-10-13" should note that §3.1 is pending Rule R.

Mark these as historical (Plan 9) or update them to point at §3.1.

**F5 (Minor — labels and table wording).**
- *CL row.* "PROVED-mod-cite (G2 A1, A-U, A-L, B*; G3′ §5.2 Lemmas H, Sat)" mixes dependencies with citations.
  - G2 A1, A-U and A-L are PROVED internal results, and A3 is citation-free.
  - The only external citation is (P), entering through B*(iii) uniqueness. G1-T's row uses the style
    "PROVED-mod-cite (G2 (P))".
  - Recommended: "PROVED-mod-cite (G2 (P), via B*(iii)); depends on G2 A1, A2, A-U, A-L, B*; G3′ §5.2 Lemmas H, Sat
    (REVIEWED)".
- *A4 row.* "(CL) now PROVED" should read "PROVED-mod-cite, Rule R pending" until review is done. State that A4
  (i)–(ii) remain CONDITIONAL on β_n → 1 ((T3)).
- *G1-R row and README.* "GAP for (T3) only" is accurate for (CL) as A4 defines it (pure powers, C = 1, p > 1). Add
  that (CL) for general regularly spaced nodes (H-a) and for p ≤ 1 is not covered:
  - Sat_p uses exact k^{−p};
  - WC uses G2 A1 with exact g;
  - A2 needs a trace-class J.
  The README phrase "(CL) is proved for pure-power atoms" is fine. The previous README line also covered general
  nodes, so a reader could misread the new one as closing that.
- *CL1 and §3 heuristic.* Saturation-exactness is in fact needed only near u = 0 (θ with g_p(θ) ≥ 1), not on all of
  (0, u_s). WC handles [θ, u_s]. This is worth one sentence in CL1.

**F6 (Minor — numerics, off-by-one in the pointwise ratio).**
- `check_cl_rough.py` prints a[1598]/(2*b[1599]). By `JacobiCoeffs` (a[i] = a_{i+1}, b2[i] = b_{i+1}²) that is
  a_{1599}/(2b_{1600}), not a_n/(2b_n). The other G1 checks use a[i]/(2b[i]).
- Correctly indexed values (scratch `idx.py`):

  | weights | a_n/(2b_n), n = 1599 | n = 1600 |
  |---|---|---|
  | smooth | 1.00068 | 1.00068 |
  | parity | 1.0119 | 0.9909 |
  | random | 0.9993 | 1.0067 |

- The printed smooth value 1.0019 is mostly this index artifact, since b_{n+1}/b_n ≈ 1 − 2/n.
- The qualitative claim stands: parity weights keep the pointwise ratio oscillating at order 10⁻². But CL2's quoted
  numbers (1.0044 vs 0.9799) must be corrected, and the script fixed and re-run.
- The tail-sum figures (1.233924, 1.233941, 1.233929 at n = 3200) match the .out and are unaffected. The error goes
  roughly like 1/n up to n = 1600. The 3200 point is slightly faster, plausibly K = 2·10⁵ truncation, as in the G1
  review. The NUMERICAL label is appropriate.

**F7 (Cosmetic — Lemma Sat_p).**
- Say explicitly that the bound is applied with W ≥ W_{>n}.
- The bound log(k^k/k!) ≤ k is what produces the θ term.
- The lemma holds for 1 ≤ k < n with any p ≥ 1, but monotonicity is claimed only on (0, ½). Theorem CL uses θ ≤ ½,
  so this is consistent. Note it.

## Novelty
UNCHECKED is correct. Lemma WC is the standard n²-speed large-deviation upper bound for (discrete, constrained) Coulomb
gases. Before any novelty claim, the search should check these unverified pointers, which were not read here:
- Johansson, discrete orthogonal-polynomial ensembles (2000s);
- Féral, large deviations for discrete Coulomb gases (2008);
- Dragnev–Saff, Kuijlaars–Rakhmanov: constrained equilibrium and saturation for discrete OPs.

Lemma Sat_p is elementary.

## Recommended labels
- **Lemma Sat_p:** PROVED (elementary; uses the REVIEWED G3′ Lemma Sat). REVIEWED after F7.
- **Lemma WC:** after F1 (and F2 if kept), PROVED-mod-cite (P) (via G2 B*(iii)); REVIEWED after a re-check of the new
  gap argument.
- **Theorem CL and Corollary A4′:** PROVED-mod-cite (P), REVIEWED after F1, F3 and the re-check; novelty UNCHECKED.
- **A4 (i)–(ii):** still CONDITIONAL on β_n → 1.
- **G1-R:** GAP for (T3); also state the scope of (CL) (F5).
- **Plan doc:** T5 stays open until the fixes are applied and re-checked. The Review focus list is accurate. Add "uniformity
  of c′ in R/M" (F1).

## Re-check (fixes at b94785e), 2026-10-14

Same reviewer. I read the rewritten §3.1, the table rows, the file header, §3 "Status of (CL)", §4, README, LOG, the
plan doc and the re-indexed check. The re-run values in `check_cl_rough.out` (smooth 1.0007/1.0007, parity
1.0119/0.9909, random 0.9993/1.0067) agree with my scratch `idx.py`. The tail sums are unchanged.

**Verdict: ACCEPT.** All of F1–F7 are resolved. The four items below are cosmetic and do not block REVIEWED.

**F1 (Lemma WC): resolved.**
- *Step 1, the uniform gap over B ⊂ 𝒜 with no support restriction.* Each part checks out:
  - Tightness at ∞ comes from σ([X, ∞)) = X^{−1/p}.
  - Prokhorov applies on [0, ∞).
  - Upper semicontinuity: min(k, L) is u.s.c. and bounded above, so Portmanteau applies to μ_k^x ⊗ μ_k^x → ν ⊗ ν. Also
    ∬min(k, L)dν² ≤ I(ν).
  - The bound on (k − L)⁺ is uniform: (a + b − L)⁺ ≤ (2a − L)⁺ + (2b − L)⁺, and μ^x ≤ σ gives a uniformly small log
    tail.
  - An atom at 0 forces I(ν) = −∞, a contradiction. So ν({0}) = 0.
  - ν ≤ σ holds, from open sets plus regularity. Mass 1 is preserved, so ν pulls back into 𝒜, and B*(iii) gives
    ν = μ*.
  - φ∘g⁻¹ extends continuously by 0 at x = 0, so ⟨φ, μ_k⟩ converges. This contradicts badness.
  - c′ now depends only on (φ, δ).
- *Step 2, the order of constants.* t₀ is chosen from (c′, φ, δ) alone, and t₀ ≤ 1 − 1/√2 gives τ² ≥ ½. Then M is
  chosen with p·t₀·log M ≥ 2A and M ≥ R_φ. The circularity is gone.
  - A = 4p + 2|κ_p| matches G2 A-U, with E_p = κ_p.
- *Steps 3–4.*
  - T ⊂ (Mn, ∞) lies outside supp φ.
  - The φ-comparison uses only u ≤ R_φ/τ ≤ √2·R_φ ≤ 2R_φ, so it does not depend on M.
  - The energy drop of c′n² is correct.
  - The two exponents combine with A-L as before.

**F2–F7: resolved.**
- F2: the step was removed.
- F3: the split is now χ + (1 − χ).
  - Part (b) implicitly uses 0 ≤ 1 − χ ≤ 1 and λ_n − m_n ≥ 0, which is fine.
  - It uses k < θn ≤ n/2, so g_p(k/n) ≥ 1.
- F4:
  - The header and §4 are updated.
  - §3 "Status of (CL)" is kept as historical Plan 9 text, with a "superseded" tag. That is acceptable.
- F5: the CL, A4 and G1-R rows, CL4 and the README scope are fixed.
- F6: the check is re-indexed, re-run and annotated.
- F7: done.

**Residual items (cosmetic, optional):**
1. *WC step 1.* If B = ∅ or sup_B I = −∞, then c′ = +∞. Define c′ := min(1, (κ_p − sup_B I)/2). Also write
   ∬…dμ_k^x dμ_k^x, using the x-measures, in the u.s.c. bullet.
2. *WC step 4.* "On the bad event μ′ ∈ B" needs δ − ω_φ(1/n) − δ/4 ≥ δ/4, i.e. n large. Say "for n ≥ n₀(φ, δ)".
3. *Plan doc Review focus.* It still mentions "support ⊂ [0, 2R]" and "layer remainders". It could note the F1 rewrite.
   T5 can be ticked after this re-check.
4. *G1 LOG Plan-27 entry.*
   - The bullet "upper semicontinuity of I on bounded-support 𝒜" is superseded by the x-compactness gap.
   - "G1-R is reduced to (T3) alone" should add "for pure-power atoms, p > 1", matching CL4 and the G1-R row.

**Final labels.**
- Lemma Sat_p: **PROVED + REVIEWED**.
- Lemma WC, Theorem CL, Corollary A4′: **PROVED-mod-cite (P)** (through G2 B*(iii); internal inputs G2 A1, A-U, A-L,
  B*(i); G3′ §5.2 Lemma Sat) **+ REVIEWED**; novelty UNCHECKED.
- A4: tail-Cesàro part unconditional for pure-power atoms with p > 1 (by Theorem CL); (i)–(ii) CONDITIONAL on
  β_n → 1.
- G1-R: GAP for (T3). (CL) remains open for general regularly spaced nodes and for p ≤ 1.
