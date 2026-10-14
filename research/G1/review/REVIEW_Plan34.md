# Rule R review: Plan 34 (Lemma TC, Theorem T3-avg)

Reviewer: independent Rule R pass, 2026-10-14. Target: worktree `ja-plan34`, branch `plan-34-density`, commit 1ba1c13.
Scope: research/G1/PROOF.md §3.7 (Lemma TC, Theorem T3-avg, Remarks avg1–avg2), status rows TC and T3-avg, LOG Plan-34
entry, docs/superpowers/plans/2026-10-14-plan-34-density.md (Review focus), research/G1/checks/check_sv_density.py/.out.
§3.6 (Theorem R) is the pre-review version and was not reviewed here. Only the way §3.7 refers to it was checked.

## Verdict

**ACCEPT WITH FIXES.** I found no mathematical error that changes a statement. Lemma TC is correct and uniform over the
sandwich class. The T3-avg argument (telescoping over n ∈ [N, 2N] against a tail set A_N that does not depend on n) is
sound.

Fixes are needed in four places:
- the hypothesis "Ψ slowly varying" and the uniform convergence theorem (UCT) step, which is a citation-gate problem
  (F1);
- the label of TC, which hides the external input (P) (F2);
- the way the effective M is used in step 3, and a loose constant (F3, F4);
- the density-one step, plus two overstated remarks (F5–F7), and stale text elsewhere (F8).

## Independent checks done

1. **A-U's tail-split bound is uniform in the weights through W.** G2 §2, A-U proof: with S = H ∪ T, T = S ∩ (Mn, ∞),
   |T| = m, N = n − m:
   - cross pairs ≤ (N!)^{−2pm}: no weights involved;
   - tail D_m(tail) ≤ W^m(Mn)^{−pm(m−1)} (Hadamard): weights enter only through W;
   - head Σ_HΠ_Hw·V(H) ≤ W^N·sup V(H), with sup V(H) from Corollary A2: C′_M depends only on (p, M).

   So log T_m ≤ −pn²log n + E_pn² + n²φ_M(t) + O(n log n), where the O-constant depends only on (p, M, max(1, W)).
   Along T3-avg's path, W(t) ≤ max(1, C)ζ(s), so this is uniform. ✓
2. **The algebra of φ_M ≤ At − pt²log M, A = 4p + 2|E_p|, redone.**
   - −2pt(1−t)log(1−t) ≤ 2pt²;
   - −p(1−t)²log(1−t) ≤ pt(1−t);
   - together these are pt(1+t);
   - +2pt(1−t) ≤ 2pt;
   - |E_p((1−t)² − 1)| = |E_p|t(2 − t) ≤ 2|E_p|t.

   The total is ≤ (4p + 2|E_p|)t. ✓ With E_p = κ_p (B*(iii)), A = 4p + 2|κ_p|. ✓ (See F2: this identification is
   what carries the citation (P).)
3. **A-L is uniform over the sandwich.** G2 A-L lower-bounds D_n by the single Heine term at the quantile configuration
   S*.
   - Steps 1–3 involve no weights. η and U = U(η) depend only on p.
   - Step 4 uses Π_{S*}w ≥ c₁^n(U′n + 1)^{−sn}, which depends on the weights only through (c₁, s).
   - Hence log D_n ≥ −pn²log n + (κ_p − η)n² − C(p, η, c₁, s)·n log n, uniformly, with c₁ = min(1, c) along the path. ✓
4. **Probability and expectation in TC.**
   - At t₁ = 2A/(p log M): At₁ − pt₁²log M = At₁ − 2At₁ = −At₁. For t > t₁ the bracket is more negative, since it
     is concave and decreasing beyond t₁/2. ✓
   - P_m(j ≥ t₁m) ≤ (m+1)·exp(−At₁m² + O_M(m log m) + o(m²)). ✓
   - j ≤ m gives 𝔼j ≤ t₁m + m·P(j ≥ t₁m) = t₁m + o(1). This is even better than the stated o(m). ✓
   - If t₁ ≥ 1 the lemma is trivially true. Nothing requires A-U to be valid only for p > 1: G2 A1/A2/A-U are stated
     and proved for every p > 0 (|g′| is decreasing for every p). ✓ (See F8 for the stale §3.3 remark that says
     otherwise.)
5. **Path, centering, pointwise split (step 1).**
   - w(t) = vΨ^t lies in [min(1, c), max(1, C)]·v. ✓
   - Σμ_n = Σμ_{n−1} = 1 allows centering by log Ψ(n). ✓
   - The middle region for index n is [n/M, M′N]. With n ∈ [N, 2N], the ratio k/n lies in [1/M, M′]. ✓
   - Bound: |·| ≤ ∫_0^1[2δ_N + G·(μ_n + μ_{n−1})(head ∪ A_N)]dt. ✓
6. **Head (step 2).** μ_m ≤ 1 − ρ_m together with Sat_p⁺ gives ≤ C″n^{s+1}(n+1)²e^{−2(n−1)}, uniformly in t. This is
   the T3-sv head bound verbatim (W(t)/w_k(t) ≤ max(1, C)ζ(s)k^s/min(1, c)). ✓
7. **Telescoping (step 3), index ranges.**
   - Σ_{n=N}^{2N}μ_n(A) = ρ_{2N+1}(A) − ρ_N(A) ≤ ρ_{2N+1}(A).
   - Σ_{n=N}^{2N}μ_{n−1}(A) = ρ_{2N}(A) − ρ_{N−1}(A) ≤ ρ_{2N}(A) ≤ ρ_{2N+1}(A).
   - Monotonicity: μ_m = ρ_{m+1} − ρ_m ≥ 0, and ρ_m(A) = 𝔼_m#(S ∩ A).
   - The key design point is correct: A_N = (M′N, ∞) is the same for every n in the block, which is what lets the
     telescoping work. ✓
8. **The "Fubini" step** is only the interchange of a *finite* sum over n with ∫_0^1dt. It needs each
   t ↦ (μ_n^{(t)} + μ_{n−1}^{(t)})(A_N) to be measurable.
   - It is continuous: ρ_m^{(t)}(A_N) = m − ρ_m^{(t)}(A_N^c), with A_N^c finite and each ρ_m^{(t)}(k) continuous in t
     (D_m(t) smooth, T3-conv step 1).
   - Since the TC bound is uniform in t, the average over t is bounded by the sup over t. ✓ (A one-line justification
     would help; optional.)
9. **a_n (step 5).**
   - Centered FVa gives |ȧ_n| ≤ Σ|g_n|[|x_k − a_n|μ_n + b_n(μ_{n−1} + μ_n)], using 2|q_{n−1}q_n| ≤ μ_{n−1} + μ_n.
   - T3a step 1's bounds a_n^{(t)} ≤ 2M^pn^{−p} and b_n^{(t)} ≤ 2M^p(n−1)^{−p} use only the head mass (Sat_p⁺). They do
     not use Lemma TL or polynomial slow variation, so they hold here, uniformly in t. ✓
   - Off the head (middle and A_N): 0 ≤ x_k ≤ (M/n)^p and 0 ≤ a_n ≤ 2M^pn^{−p}, so |x_k − a_n| ≤ 2M^pn^{−p} ≤ 3M^pn^{−p}. ✓
   - After multiplying by n^p, the A_N term is ≤ G·C(M, p)·(μ_n + μ_{n−1})(A_N), and it telescopes as in step 3. The
     resulting bound C′(δ_N + G/log(M′/3)) + o(1), with C′ depending on (M, p, A), is right. M is fixed before
     M′ → ∞. ✓
10. **Numerics.** I reran the script from the main checkout. It reproduces `check_sv_density.out` digit for digit
    (≈ 48 s), apart from a harmless RuntimeWarning (division 0/0 at n = 0). A sanity check on the size of the effect:
    - locally Ψ ≈ k^α with α = cos(log log k)/(Ψ·log k) ≈ −0.006 (n = 200) to −0.022 (n = 3200);
    - changing s by α moves β_n only at relative order α/n;
    - so differences of 10⁻⁵–10⁻⁶ are plausible.

## Findings

**F1 (MAJOR, citation gate / hypothesis; T3-avg statement and step 1).** "Ψ(λk)/Ψ(k) → 1 for each λ > 0", with Ψ a
sequence, is not well defined (λk is not an integer), and the UCT as usually stated has further requirements.
- The UCT (Bingham–Goldie–Teugels, Thm 1.2.1) needs Ψ to be a *measurable* function on [a, ∞). Without measurability
  it can fail (Hamel-basis counterexamples).
- For sequences, the usual definition is via Ψ(⌊λn⌋)/Ψ(n). Uniformity then needs an extra theorem (Galambos–Seneta /
  BGT §1.9). That is my recollection only; it is not verified.
- No UCT source is in CITATIONS.md, and AGENTS.md rule 4 requires one.

*Fix (preferred, citation-free):* state the hypothesis directly in the form used:

  δ_N(M, M′) := sup{|log Ψ(k) − log Ψ(n)| : n ∈ [N, 2N], k ∈ ℕ ∩ [n/M, M′N]} → 0 for every M, M′ ≥ 1.

Call it "uniformly slowly varying". Then remark that it holds when Ψ(k) = Φ(k) for a measurable slowly varying Φ on
[1, ∞) (UCT; quote BGT Thm 1.2.1 with hypotheses in CITATIONS.md if the remark is kept).
- The example 2 + sin(log log k) satisfies the uniform form directly: on k ∈ [n/M, M′n], log log k moves by
  O((log M + log M′)/log n), and sin is 1-Lipschitz. This is the TL1 argument.
- *Alternative:* keep "slowly varying", define Ψ as a measurable function on [1, ∞), and add the UCT citation.

**F2 (MINOR, label; status row TC, §3.7 statement).** TC compares A-U's upper constant E_p with A-L's lower constant
κ_p. That needs E_p ≤ κ_p, i.e. B*(iii), which is PROVED-mod-cite (P). So the row's label "PROVED-mod-cite (G2 A-U,
A-L)" names internal results and hides the external input.
*Fix:* "PROVED-mod-cite (P) (through G2 B*(iii); internal: G2 A1/A2, A-U, A-L)", as in the CL row. Add "novelty
UNCHECKED" (see F9). In the TC proof, say explicitly "using E_p = κ_p (B*(iii))" where A-U is quoted with κ_p.

**F3 (MINOR, step 3: effective M).** Lemma TC is stated for a *fixed* M ≥ 2: its o(m) depends on M through C′_M. Step 3
applies it with M = M′N/(2N + 1), which varies with N. The text also allows M′ = 4, giving M′/3 < 2, below TC's range.
(The approach is salvageable: C′_M is monotone in M and M stays in [M′/3, M′/2].)
*Fix:* for N ≥ 1, M′N ≥ (M′/3)(2N + 1), so A_N ⊂ ((M′/3)(2N + 1), ∞). Apply TC with the fixed M := M′/3, and require
M′ ≥ 6.

**F4 (MINOR, step 4 constant).** The algebra gives
(1/N)·G·(4A/(p log(M′/3)))(2N + 1) → 8AG/(p log(M′/3)), or ≤ 12AG/(p log(M′/3)) for every N ≥ 1. "24A" is a valid
upper bound but is off by a factor 3 from what the argument gives. The middle term is 2δ_N(N + 1)/N, not 2δ_N.
Harmless.
*Fix:* write 8A (asymptotically) or 12A, or just "C(p)·G/log(M′/3)".

**F5 (MINOR, step 6 / statement "along a set of density one").** Step 6 shows only that, for each ε, E_ε := {n : X_n > ε}
has density 0. The statement asserts one density-one set J along which n^pb_n → c(p) and n^pa_n → 2c(p). Two steps are
missing.
- **Single set.** The step from "each E_ε has density 0" to one set J is the standard diagonal argument
  (Koopman–von Neumann): choose N_j ↑ with |E_{1/j} ∩ [1, X]| ≤ X/j for X ≥ N_j, and let J be the complement of
  ∪_j(E_{1/j} ∩ [N_j, N_{j+1})).
- **Dyadic blocks to Cesàro.** The step from block averages to (1/X)Σ_{n≤X}, used for the density count, should also
  be written: blocks below N₀ cost O(N₀), and the rest cost ≤ 2ηX.
- Then intersect the b- and a-sets, and use n^pb_n(w) = n^pb_n(v)·exp(½(log b_n²(w) − log b_n²(v))).

*Fix:* add these two lines.

**F6 (MODERATE, overclaim; Remark avg1 and LOG).** "Upgrading this to all n is *equivalent* to localization at scale Mn"
is not justified.
- Localization ⇒ all-n follows from the §3.2 reduction.
- The converse (pointwise law ⇒ μ_n((Mn, ∞)) ≤ ε(M) uniformly along the path) is neither proved nor plausible as
  stated.

The LOG line "all-n … (needs Mn localization)" has the same problem.
*Fix:* "Upgrading this to all n would follow from localization at scale Mn (§3.2 reduction; §3.4 TL2; OPEN)"; in the
LOG, "(would follow from Mn localization)".

**F7 (MINOR, Theorem R remark in avg1).** "Theorem R shows that some bounded weights fail the pointwise law on a sparse
(density-zero) set of scales. This is consistent with T3-avg's density-one form …" has two problems.
- **The parenthetical.** Theorem R (as currently stated) proves failure *at least* along the sparse sequence N_i. It
  does not show that the failure set has density zero, or that a density-one law holds for those weights.
- **"Consistent".** The word is vacuous, because T3-avg does not apply to Theorem R's weights.

*Fix:* "Theorem R (§3.6) gives bounded, not slowly varying, weights for which the pointwise law fails along a sparse
sequence of n. T3-avg does not apply to them, and whether a density-one law holds for such weights is open."

**F8 (MINOR, stale text elsewhere in PROOF.md).**
- **§3.3 T3c2, "Averaged version (SKETCH)".** It says the needed tail count comes from "G2 A-U … for p > 1 … nothing is
  stated for p ≤ 1". A-U holds for all p > 0, and TC now proves the averaged version. Mark it as superseded by §3.7
  (TC, T3-avg; all p > 0).
- **§3.4 TL1/TL2 and §3.2.** The OPEN remarks on 2 + sin(log log k) should add "(density-one version: T3-avg, §3.7)".
- **§4 Plans 29–32 summary.** Could add one line for Plan 34.

**F9 (MINOR, novelty).** The TC row has no novelty marker; the T3-avg row has UNCHECKED, which is correct.
- Tail-count and large-deviation bounds for discrete Coulomb/Heine ensembles are in the spirit of the
  Johansson/Féral-type literature.
- Cesàro or density-one versions of ratio asymptotics may be known in the Máté–Nevai–Totik / Simon (Cesàro-averaged
  Jacobi parameters) circle.

Neither was searched. *Fix:* add "novelty UNCHECKED" to TC; keep it on T3-avg.

**F10 (COSMETIC, numerics).**
- The `.out` A-row header says "at the same n", but the script prints da[3199] in the last column, not da[3200].
- The [N, 2N] averages use the slice N:2N, i.e. [N, 2N).
- avg2's text ("≤ 1.8·10⁻⁵ and decreasing at n = 200 … 3200"; K-converged between 1.2·10⁵ and 2.4·10⁵) matches the
  output. The K-convergence statement is about the *differences* only, which is all that is claimed. Note that §3.5
  T3a2 found the individual A columns not K-converged at n ≥ 2000. The caveat "weak evidence only" is appropriate.

*Fix (optional):* print n = 3200 for A (request 3202 coefficients) or relabel, and silence the n = 0 warning.

## Answers to the review focus

- **TC uniformity:** yes. The A-U constants depend on the weights only via W (and p, M), and the A-L constants only via
  (c₁, s) (checks 1, 3).
- **Probability and expectation:** correct (check 4). The constant A = 4p + 2|κ_p| is G2's, with E_p = κ_p (F2).
- **Telescoping index range:** correct (check 7).
- **Effective M:** needs F3.
- **Uniformity in t and Fubini:** fine (check 8).
- **δ_N via UCT:** needs F1.
- **a_n analogue:** correct. T3a step 1's bounds use only the head (check 9).
- **Density one:** needs F5.

## Recommended labels (after fixes)

| Row | Label |
|---|---|
| TC | PROVED-mod-cite (P) (through G2 B*(iii); internal: G2 A1/A2, A-U, A-L); REVIEWED after fixes; novelty UNCHECKED |
| T3-avg | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; (P) via TC; plus BGT UCT only if F1's alternative is taken; internal: FV, FVa, Sat_p⁺, TC); REVIEWED after fixes; novelty UNCHECKED |
| avg2 | NUMERICAL (p = s = 2 only) |

A re-check is needed only for F1 (the restated hypothesis and its example) and F5. The other fixes are textual.
