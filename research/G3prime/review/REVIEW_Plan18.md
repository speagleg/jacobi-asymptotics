# Rule R review: Plan 18 (PROOF.md §9, Theorem P, Proposition P′, numerics)

Reviewer: independent agent, fresh context, adversarial. Date: 2026-10-14. Worktree `ja-plan18`, branch
`plan-18-primes-to-lawp`. Scope: PROOF.md §9 (9.1–9.4), the §8.2 interface, CITATIONS.md (C7)–(C9), the plan,
`checks/check_pc_numerics.py/.out`. Read in full: AGENTS.md, VERIFICATION_POLICY.md, the plan, PROOF.md §0 and §§8–9,
CITATIONS.md (C3), (C5)–(C9).

Sources downloaded independently into the session scratchpad (`rr18/`) and read with `pdftotext -layout`:
- Montgomery–Soundararajan arXiv:math/0409258v1: §0, Theorems 1–3, (16), (17), Corollary 1, Conjectures 1–2, the
  G–M remark.
- Goldston arXiv:math/0412313: §4 ((4.1), (4.2), (4.9), Theorem 1), §5, §6 ((6.1)–(6.15), Lemma 1, Theorem 4),
  §7 (Theorem 5), §9 (Theorem 7, (9.3), footnote 6, the proof sketch).
- MRT arXiv:1707.01315v3: abstract, Theorem 1.3.
- BGST arXiv:2501.14545v3: §3, (3.1), to check the §9.3 remark.

Scratch scripts (`.venv` python, `-I`, kept outside the repo): `rr18s/p1.py` re-runs part [1] with counts and a
height split. `rr18s/stab.py` and `stab2.py` are a precision and truncation check of part [2]. The worktree has no
`data/raw` and no `csrc/build`, so the repo script cannot run there (see N3). The scripts point `DATA_ROOT` and
`BIN_DIR` at the main checkout `jacobi-asymptotics/`. The zeros file's SHA-256 matches `data/SHA256SUMS`.

## Verdict: ACCEPT WITH FIXES

- **Theorem P is correct as an implication.** The chain is RH + (V) ⇒ SPC (G–M Theorem 7 converse, via the
  Saffari–Vaughan step that the notes only state) ⇒ PCC (Goldston Theorem 4) ⇒ (SG) (Theorem C) ⇒ G3′. The ranges and
  normalizations match (details under "Checked and OK").
- **Must fix before REVIEWED:**
  - **F1.** Goldston's footnote 6 says (V) in this range implies RH. That makes §9.3's question "can RH be removed?"
    mis-posed for Theorem P as stated.
  - **F2.** P′(a) asserts two things without proof: that F on [0, 2 − ε] "cannot give" N(T, β) → 0, and that (SG)
    "needs F(α) for all bounded α".
  - **F3–F5.** Missing hypotheses and missing labels.
- The remaining findings are wording, citation-scope and Rule N bookkeeping.
- No re-derivation failed. After the fixes, a light re-check is enough, without a full second pass.

## Findings

**F1 (Major: misframed open problem). §9.3 and the statement of Theorem P.**

*Problem.*
- Goldston's notes, §9, footnote 6 attached to (9.3): "If (9.3) holds for this range of h it implies RH."
- So, per the cited source, the hypothesis (V) of Theorem P already implies RH. "RH and (V)" is then logically the
  same hypothesis as "(V)".
- §9.3 asks "can RH be removed?" and calls it open, saying Steps 1–2 "use RH". For Theorem P as stated, removing RH
  is (modulo the footnote) formally trivial. The real question is different: can a *weaker or RH-free* prime input
  (a restricted range of h, or an unconditional variance identity in the GLSS style) give PCC or (SG)?
- The footnote is stated without proof in the notes, so it is a *secondary* statement.

*Fix.*
- Add a remark after Theorem P. Goldston (C8, §9 fn. 6) states without proof that (V) in this range implies RH, so
  RH is formally redundant in Theorem P. It is kept as an explicit hypothesis because every cited step (Theorem 7,
  Theorem 4) assumes it. This is a logical relation between hypotheses, not a statement about RH (AGENTS.md rule 3).
- Reword §9.3 as "can the input be weakened?", e.g.:
  - (V) on a restricted range of h, together with an RH-free substitute for Theorem 7's explicit-formula step; or
  - an RH-free prime-variance identity in the GLSS style.
- Keep "Not attempted."
- Add the footnote quote to (C8).

**F2 (Major: unproved impossibility and necessity claims). §9.2(a), second and third bullets, and the first
bullet's "only".**

*Problem.*
- (i) "[F(α) on [0, 2 − ε]] cannot give N(T, β) → 0 as β → 0." No argument is given, and none is known to me.
  - What is true is that the Fourier-kernel method (Goldston §5: a majorant or minorant whose transform has support
    in [−Δ, Δ], Δ < 2) gives bounds with a positive floor, of order 1/Δ, that do not tend to 0 with β.
  - Whether the *information* "F = 1 + o(1) on [1, 2 − ε]" (together with Theorem 1, F ≥ 0 and Lemma 1) forces
    N(T, β) → 0 is an extremal problem. I checked the obvious perturbation constructions. They do not settle it
    either way: a perturbation with spectral gap (−2, 2) moves only O(β) mass into [0, β], not an atom at 0⁺.
- (ii) "(SG), which needs F(α) for all bounded α." This is unproved. (SG) is implied by PCC, and PCC by SPC (on RH).
  Nothing shows that (SG) needs SPC.
- (iii) The first bullet says (6.3) "yields (V) **only** for h ≤ X^{1/2−ε}". Goldston says (6.3) implies (9.3) *in*
  that range. "Only" asserts that no more follows, which is unproved.
- The closing parenthesis ("a statement about the route") is good, but it does not cover (i) and (ii), which are
  stated as facts.

*Fix.*
- (iii) Change to "the known argument gives (V) for h ≤ X^{1/2−ε}, hence SPC on 1 ≤ α ≤ 2 − ε (C8 §9)".
- (i) Change to "with F known only on |α| < 2, the standard kernel method (Goldston §5) gives bounds for N(T, β)
  that do not tend to 0 as β → 0. Whether this information implies (SG) is not known to us."
- (ii) Change to "the known route to (SG) (PCC, via Theorem 4) uses F on all of [1, M] for every M".
- Keep the "route, not impossibility" sentence.

**F3 (Medium: missing hypothesis). §9.2(a).**

*Problem.*
- The first bullet has no RH hypothesis. Goldston's "straightforward exercise" sits inside §9, under Theorem 7's
  standing "Assume the Riemann Hypothesis".
- M–S Theorem 3 assumes (20) for all k ≤ K, including k = 1. M–S say: "the hypothesis that E_1(N; {1}) ≪ N^{1/2+ε}
  is equivalent to the Riemann Hypothesis".

*Fix.* Write "Assume RH and (6.3). Then …". This is a labelled hypothesis of a conditional result, as AGENTS.md
rule 3 requires.

**F4 (Medium: label, theorem vs heuristic). §9.2 heading, and (b), (c).**

*Problem.*
- "Proposition P′" reads as a proved statement, but only (a)'s first bullet is a citation (KNOWN: Goldston §9 /
  Bolanz).
- (b) is triangle-inequality bookkeeping. Its arithmetic is right (see OK-5), but it shows only that MRT's
  *absolute* error bounds do not suffice. It does not exclude that MRT-type methods capture the *signed* cancellation
  across shifts that (V) needs. "Fall short by a power of X" is correct in that sense.
- (c) is a heuristic dictionary.

*Fix.*
- Rename to "Remarks P′", or keep "Proposition" only for (a) with label KNOWN (C8 §9).
- Label (b) "HEURISTIC (bookkeeping, triangle inequality)" and (c) "HEURISTIC".
- In (b):
  - the pair sum runs over 0 < |d| < H, not |d| < H;
  - name the E_1 (ψ) cross terms, which are controlled on RH;
  - add that MRT's exceptional set (O(H log^{−A}X) shifts per window, bounded trivially) also costs H²X log^{1−A}X,
    likewise too large;
  - add that MRT's sums are dyadic (X < n ≤ 2X), while (V) is ∫_1^X (harmless).

**F5 (Medium: secondary step not flagged in the proof). §9.1 Step 1.**

*Problem.*
- G–M Theorem 7's converse takes (9.1) in δ-form: "(9.1) holds uniformly for X^{−1/A1}(log x)^{−3} ≤ δ ≤
  X^{−1/A2}(log x)³". (V) is in h-form.
- The h → δ passage is the Saffari–Vaughan argument, which the notes only mention ("an argument of Saffari and
  Vaughan [33] is used …").
- CITATIONS (C8) calls this "secondary", correctly. PROOF §9.1 Step 1 cites "Theorem 7 and (9.3)" with no flag, and
  Theorem P carries no label at all.
- Small point: the δ-range reaches δX = (log X)^{−3} < 1, below (V)'s h ≥ 1. That piece holds trivially: for h < 1,
  (x, x + h] holds at most one integer, so the integral is hΣ_{n≤X}Λ(n)² + O(h²X) ∼ hX log X ∼ hX log(X/h), since
  log(1/h) = O(log log X). Say so in one line.

*Fix.*
- In Step 1, write "via the SPC ⇔ (9.3) equivalence stated (with the Saffari–Vaughan reduction, not reproduced) in
  C8 §9: a secondary statement".
- Spell out the range map. For SPC on [1, M], take A1 = 1 and A2 = M. Theorem 7 then needs (9.1) for
  δ ≤ X^{−1/M}(log X)³, i.e. h ≲ X^{1−1/M}(log X)³, which (V) with ε < 1/M covers.
- Add the h < 1 remark.

**F6 (Minor: watchlist name). §9.1 Step 2, "Pólya's argument".**

*Problem.*
- "Pólya 1918/1926" is on the Rule C watchlist. The fact used is elementary: nondecreasing functions converging
  pointwise to a continuous limit converge uniformly on compact intervals. It is correct here: N(T, ·) is
  nondecreasing in β, and the limit is continuous.
- The uniformity is formally needed, because GLSS's PCC (C5) is stated "uniformly in each interval
  0 < λ0 ≤ λ ≤ λ1", and Theorem C cites GLSS Theorem 1, whose hypothesis is that PCC. Theorem C's own small-gap step
  uses only fixed λ.

*Fix.* Replace the name with the three-line proof:
1. Partition [λ0, λ1] by a mesh fine enough that the limit G varies by < ε on each cell.
2. Sandwich N(T, β) between its values at the cell endpoints.
3. Take T large.

**F7 (Medium: uncited literature claim; Rule C, Rule N). §9.4 [1], last bullet.**

*Problem.*
- "The ≈10–15% deficit at moderate δ is the known finite-height effect at γ ~ 10⁶. It is consistent with arithmetic
  corrections." No source is cited ("known" is not a citation, Rule C.3). The deficit is not analysed.
- Also, "Wigner surmise" is the 2 × 2 approximation to the GUE (N → ∞) spacing law, not that law. Its small-s
  constant is 32/(3π²) = 1.0808, against π²/9 = 1.0966 for the pair density.
- "Follows the δ³ law": at δ = 0.02 the sample has **17** gaps (Poisson ±25%), and 255 at δ = 0.05. The table does
  not say so.

*Fix.*
- Replace the bullet with: "The empirical fraction is 9–16% below both limiting predictions at δ ≥ 0.1. Finite-height
  corrections to the limiting law are expected (not cited, not analysed here)."
- Add the internal evidence I computed. The deficit shrinks with height:

  | δ | lower half (k ≤ 10⁶) | upper half | limit |
  |---|---|---|---|
  | 0.10 | 8.80e−4 | 9.44e−4 | 1.07e−3 (surmise) / 1.09e−3 (PCC) |
  | 0.50 | 0.1009 | 0.1033 | 0.112 / 0.113 |

  (At δ ≤ 0.05 the halves are within noise.)
- Label the column "Wigner surmise (approximation to the GUE NN law)".
- Add the counts, or Poisson error bars, to the table.

**F8 (Minor: framing and over-reading). §9.4 [2].**

*Problem.*
- (i) "well inside Theorem B's interval [−3 log C, 0]": C is not computed (Remark B3), and Theorem B is a liminf
  statement, so finite-n values are not constrained by it. The phrase adds nothing and mixes finite n with an
  asymptotic statement.
- (ii) "shrinks roughly like n^{−0.8}": the local exponents log₂(ratio) are 0.49, 0.64, 0.73, 0.81, 0.86, still
  rising.
- (iii) "RH_ζ's κ": in a section where "RH" means the Riemann Hypothesis, the repo's theorem name RH_ζ (Plans 13–14)
  is ambiguous.

*Fix.*
- (i) Delete the phrase.
- (ii) Write "local exponent increasing from 0.5 to 0.86 over n = 100–3200".
- (iii) Write "Theorem RH_ζ (README, Plans 13–14)", or rename locally.

**F9 (Minor: citation scope). §9.3, third bullet (BGST).**

*Problem.*
- The BGST formula F(x, T) := Σ x^{ρ−ρ′}W(ρ − ρ′) is BGST (3.1), in §3. (C3) records BGST as read in §1 only.
- I checked (3.1) and its surroundings ("Since W(ρ−ρ′) is complex-valued …", proof of Lemma 4). The description is
  accurate.
- "Indefinite" is loose: the precise statement is that the weights are complex, so positivity (F ≥ 0) is lost.

*Fix.* Extend (C3)'s read scope to §3 and quote (3.1). Replace "indefinite" with "complex-valued, so the positivity
F ≥ 0 used on RH is unavailable".

**F10 (Minor: wording). §9.2(a), first and second bullets.**

*Problem.*
- (i) "equivalently (C7) Theorem 3 with K = 2, range H ≤ N^{1/2}": not equivalent. M–S Theorem 3 is a discrete
  moment with log N ≤ H. It needs (20) for k = 1 (RH) and for pairs with d_i ≤ H. Its error term
  O(H^K N^{1/2+ε}) = O(H²N^{1/2+ε}) makes the effective range H ≤ N^{1/2−ε}.
- (ii) "This improves the constants in Theorem B and the simple-zero proportions": Theorem B is unconditional with a
  non-explicit C. F on [0, 2) would give a *conditional* variant (on RH + (6.3)). That has not been done here.

*Fix.*
- (i) Write "compare (C7) Theorem 3 (K = 2; effective range H ≤ N^{1/2−ε})".
- (ii) Write "would give conditional improvements (not carried out)".

**F11 (Minor: notation and overreach). §9.2(c).**

*Problem.*
- (i) "−h log h in Σ_{d≤h}S(d) (C7 (16))": M–S (16) concerns R_2(h) = Σ_{d1≠d2 ≤ h} S_0({d1, d2}). Since
  S_0({d1, d2}) = S(d2 − d1) − 1, this is Σ_{0<|d|<h}(h − |d|)(S(d) − 1). The sum written in §9.2(c) is not that
  quantity. The −h log h term is in (17) for Σ S(D) over pairs, and in (16).
- (ii) "Twin-prime-type existence results (bounded gaps) push the other way: they produce clustering." This is vague,
  and it suggests a tension that does not exist: bounded-gap results are logically compatible with (V) and say
  nothing about it at h ≥ X^{1/2}.

*Fix.*
- (i) Correct the formula.
- (ii) Delete the bullet, or write "existence results for prime clusters (bounded gaps) have no bearing on (V) in the
  needed range".

**F12 (Minor: bookkeeping and novelty).**

*Problem.*
- §0's status table and §8.3 do not list Theorem P.
- The heading says "pending Rule R".
- The implication RH + (V) ⇒ PCC is KNOWN: G–M Theorem 7 with Goldston Theorem 4, and M–S cite it. The only new
  content is composing it with Theorem C.

*Fix.*
- Add a P row to both tables.
- State the novelty: "corollary of KNOWN (C8) + Theorem C; novelty UNCHECKED".
- Optionally call it "Corollary P".

### Numerics notes (Rule N)

- **N1.** Part [2] has no precision or truncation check recorded. I ran one (`rr18s/stab*.py`):
  - J = 1·10⁵, 2·10⁵, 4·10⁵ in double, and J = 2·10⁵ in long double, all reproduce the `.out` values to every printed
    digit for n = 100–800.
  - At n = 1600 and 3200 in long double, J = 2·10⁵ and J = 4·10⁵ reproduce −0.068015 / −5.814e−05 and
    −0.059915 / −3.187e−05.

  Add a J-doubling and `prec="ld"` pass to the script, so that the NUMERICAL label carries its own stability evidence.
- **N2.** The docstring says N(β) counts "all pairs, not only neighbours", but the code counts forward pairs with
  index offset m ≤ 7. The cap is adequate. I counted 44 pairs with m = 2 within β = 0.5, and none with m = 2 for
  β ≤ 0.2 or with m = 3 for β ≤ 0.5. So N(β)/K and #{g < δ}/K agree to the printed digits. Fix the docstring ("index
  offsets m ≤ 7; m ≥ 3 contributes 0 for β ≤ 0.5").
- **N3.** The script cannot run in the worktree: `data/raw/` and `csrc/build/` are absent. Note in the script header
  that it must run from a checkout with `data/fetch.py odlyzko` and `make -C csrc` done.
- **N4.** The §9.4 table omits the δ = 0.3 row that the `.out` contains (harmless). Every value in the table matches
  `.out`, and the part [1] re-run reproduces them exactly.
- **N5.** The framing sentence ("statements about a finite sample, not evidence about the asymptotics") is correct
  and required. Rule X: the measure takes Odlyzko's ordinates as real inputs, as rule 3 requires. That is stated.

## Checked and OK

1. **Quotes (C7), (C8), (C9)** against the PDFs:
   - (C7): M–S (16), (18), Theorem 3 with (20) and range log N ≤ H ≤ N^{1/K}, the k = 1 ⇔ RH remark, Conjecture 1,
     and the G–M sentence are all accurate.
   - (C8): SPC (6.6), PCC (6.7), Theorem 4, Theorem 7 (both directions and ranges), (9.3), and the (6.3) ⇒ SPC on
     [1, 2 − ε] remark are all accurate.
   - (C9): the abstract quote is accurate. Theorem 1.3(i) (error X log^{−A}X for all but O(H log^{−A}X) shifts
     |h − h0| ≤ H, X^{σ+ε} ≤ H ≤ X^{1−ε}, sum over X < n ≤ 2X) supports P′(b). Recommend upgrading (C9) to cite
     Theorem 1.3, read 2026-10-14.
2. **Theorem 7 range map.**
   - (9.2) for T^{A1} ≤ X ≤ T^{A2} is F(α) ∼ 1 uniformly on [A1, A2], with x = T^α and normalization (4.9).
   - A1 ≥ 1 is required, which matches SPC's [1, M].
   - The δ upper limit X^{−1/A2}(log X)³ corresponds to h ≈ X^{1−1/M}, inside X^{1−ε} for ε < 1/M. So "(V) for every
     ε ⇒ SPC for every M" is correct (modulo F5's secondary step).
3. **Theorem 4** (RH; SPC ⇒ PCC and SZC). Its proof is self-contained in the notes: Lemma 1, (6.13)–(6.15),
   differencing via monotonicity.
4. **PCC compatibility (Goldston ↔ GLSS).**
   - Goldston: (T log T/2π)^{−1}Σ_{0<γ,γ′≤T, 0<γ′−γ≤2πβ/log T} 1. GLSS: N(λ) with 0 < (γ′−γ)L ≤ λ, normalization TL,
     L = log T/2π. Since 2πβ/log T = β/L and T log T/2π = TL, these are identical with λ = β.
   - Both count zeros with multiplicity: Goldston (5.5) ff., "counts distinct zeros weighted by their multiplicity";
     GLSS uses the multiset Z.
   - Under RH every nontrivial zero has β = ½, so the index sets coincide.
   - Uniformity: OK via the monotone-limit argument (F6).
5. **P′(b) bookkeeping.**
   - M_2 = Σ_{h1,h2≤H}Σ_n Λ_0(n+h1)Λ_0(n+h2).
   - Diagonal: ∼ H(X log X + O(X)).
   - Off-diagonal: the weights are (H − |d|), with total ≈ H², and the main terms give X·R_2(H) = X(−H log H + AH)
     by M–S (16).
   - Sum: HX log(X/H) + O(HX), as stated.
   - So the weighted error sum must be o(HX log X), i.e. o(X log X/H) on (weighted) average per shift. That is a
     power saving X^{−η} for H = X^η. MRT's log^{−A} saving falls short by ≈ H/log^{A+1}X, a power of X. Correct as
     bookkeeping (labelling per F4).
6. **Theorem C interface (§8.2).**
   - Theorem C assumes GLSS-form PCC with no RH. Theorem P supplies it under RH (identical objects, item 4).
   - Theorem C then gives (SG), and G3′-L + G3′-U give log D_n = Φ_n + o(n²).
   - The b_j-form restatement matches §8.1's equivalence.
7. **AGENTS.md framing.**
   - RH appears only as a labelled hypothesis in Theorem P and §9.3. Nothing says RH is supported or tested.
   - §9.4 carries the finite-sample disclaimer.
   - The remaining framing risks are F1 (stating the fn. 6 relation neutrally), F3 (an RH hypothesis is missing, not
     extra), and F8(iii) (the RH_ζ name clash).
8. **Numerics** reproduced: part [1] re-run exactly, part [2] reproduced and stable (N1).

## Recommended labels

- **Theorem P:** PROVED-mod-cite: (C8) G–M Theorem 7 (converse); (C8) SPC ⇔ (9.3) via Saffari–Vaughan, a
  **secondary statement**; (C8) Theorem 4; (C5); (C1). Plus mod-input RH, (V) and Theorem H (through Theorem C,
  G3′-L, G3′-U).
  - Note: per (C8) fn. 6 (secondary), (V) implies RH.
  - Novelty: UNCHECKED. The RH + (V) ⇒ PCC part is KNOWN (G–M, Goldston Theorem 4).
  - Becomes REVIEWED after F1, F5, F6 and F12.
- **P′(a):** KNOWN (C8 §9, Bolanz via C8) for the "(6.3) + RH ⇒ SPC on [1, 2 − ε]" part. The rest is a REMARK,
  reworded per F2 and F3.
- **P′(b):** HEURISTIC (bookkeeping; triangle inequality on MRT Theorem 1.3).
- **P′(c):** HEURISTIC.
- **§9.3:** OPEN, reframed per F1. Not attempted.
- **§9.4:** NUMERICAL (finite sample). Add the N1 stability pass to the script and `.out`.

## Re-check (commit ffd8e6c), 2026-10-14

Verdict: **ACCEPT**. All findings are resolved:

- **F1.** Corollary P carries the footnote-6 note, labelled secondary and stated neutrally as a relation between
  hypotheses. §9.3 is reframed as (Q1) and (Q2).
- **F2, F3, F10.** P′(a) now assumes RH. It reads "known route" and "the standard kernel method does not give …";
  it records that the conditional improvements are not carried out, and gives C7 Theorem 3's effective range
  N^{1/2−ε}.
- **F4, F11.** (b) and (c) are labelled HEURISTIC. The R_2(h) formula is correct. The bounded-gaps bullet is neutral.
- **F5.** Step 1 spells out the range map (A₁ = 1, A₂ = M, ε < 1/M) and flags Saffari–Vaughan as secondary.
- **F6.** The uniformity proof is written out (grid plus monotone sandwich) and is correct.
- **F7, F8.** §9.4 wording is fixed: the surmise is called an approximation, the ±25% at δ = 0.02 and the
  7-neighbour cap are stated, the shortfall is "not analysed", the local exponents are 0.49→0.86, the Theorem B
  comparison is gone, and the κ reference reads "Theorem RH_ζ (G1)".
- **F9.** The BGST §3 (3.1) quote is in (C3). I checked W(u) = 4/(4 − u²) against the PDF.
- **F12.** P rows are in §0 and §8.3.
- **N1–N3.**
  - The script docstring is fixed.
  - Part [3] in `.out` matches my independent runs.
  - The header notes the data and kernel dependency.

Non-blocking nits:
- (Q2) says "hypothesis-free formulation". It is still a hypothesis (complex-weighted SPC), only RH-free, so
  "RH-free formulation" is more accurate.
- Part [3] stops at n = 1600. My runs at n = 3200 (long double, J = 2·10⁵ and 4·10⁵) were also identical.

### Final labels
- **Corollary P:** PROVED-mod-cite (C8 Thm 7 converse; C8 SPC ⇔ (9.3), secondary; C8 Thm 4; C5; C1) + mod-input RH,
  (V), Theorem H. **REVIEWED.** Novelty UNCHECKED (the RH + (V) ⇒ PCC part is KNOWN).
- **P′(a):** KNOWN (C8 §9), plus a remark. **P′(b), (c):** HEURISTIC. **§9.3:** OPEN (Q1, Q2), not attempted.
- **§9.4:** NUMERICAL (finite sample, stability recorded).
- Replace "re-check pending" with "REVIEWED" in §0, §8.3 and the §9 heading.
