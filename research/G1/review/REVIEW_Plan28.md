# REVIEW_Plan28: Rule R second reading of G1 §3.2 ((T3) for rough weights, Plan 28), 2026-10-14

- **Reviewer.** An independent second-reader agent (opus). It edited no repo files except this one.
- **Scope.** research/G1/PROOF.md §3.2 (Lemma FV, Consequence, Numerics [1]–[3], Conjecture R, requirements (i)–(iii),
  re-scope of G1-R); the status rows FV and Conj R; the §4 note; the README G1-R line; the G1 LOG Plan-28 entry; the
  plan docs/superpowers/plans/2026-10-14-plan-28-t3.md; checks/check_t3_rough.py/.out. Context read: G1 §§0–2, §3.1
  (Lemma Sat_p), §4; check_regularity.out.
- **Re-runs** (scratch scripts; nothing committed):
  - `r1.py`: the same Lanczos as the check reproduces every [1] number in the .out (n = 100, 200, 400, K = 20n). Max
    |QQᵀ − I| = 1.3–1.8·10⁻¹⁵ in every run. It adds K = 40n (n = 100, 200), n = 400 with K = 40n, **n = 800** (K = 20n),
    and the first-order prediction of the quantity that is actually compared (second difference, F1).
  - `mp.py`: an **independent method and precision**. Discretized Stieltjes in mpmath, n = 60, K = 1200, at 400 and 600
    digits (identical). b₆₀ = 1.69630820033066·10⁻⁴ agrees with float64 Lanczos to 15 digits. The adversarial jumps
    are 0.0275451 (ε = 0.05) and 0.113116 (ε = 0.2), identical to float64. (At 80 digits Stieltjes is off by a factor
    of 100. This confirms the LOG remark that plain recurrences are unstable here.)
  - `r2.py`: repo RKPW kernels (long double and binary128) at n = 200, 400, K = 20n agree with Lanczos b_n to 12
    digits and give the same jumps (0.0246/0.1000 at n = 200; 0.0291/0.1204 at n = 400).
  - `r4.py`: K = 200n (n = 200) with the sign pattern recomputed on the larger measure: jump 0.0238/0.0984, against
    0.0246/0.1000 at K = 20n. Restricting f to the window [0.6n, 1.6n] keeps 92% (0.0910).
  - `r3.py`: one weight sequence with **three** windows N = 60, 240, 960 (ε = 0.2, K = 24000, n ≤ 1000), plus the
    960 window alone.

| Item | Verdict | Required fixes |
|---|---|---|
| Lemma FV | ACCEPT (minor F9) | — |
| "Consequence" paragraph | **REJECT AS WRITTEN (Major)** | F1 (wrong quantity), F2 (the robustness "only if" is false) |
| Numerics [1]–[3] | ACCEPT WITH FIXES | F1 (the "70–85%" claim is an artefact), F3, F7, F8 |
| Conjecture R | ACCEPT as CONJECTURE / NUMERICAL, WITH FIXES | F2 (reframe the evidence), F4, F10 |
| Requirements (i)–(iii) | ACCEPT WITH FIXES | F10 |
| Re-scope / localization reduction | ACCEPT WITH FIXES | F5 (valid for bounded log Ψ; it proves more than (T3)) |
| Labels / §4 / README / LOG / plan | ACCEPT WITH FIXES | F6, F7, F11 |

**Overall: ACCEPT WITH FIXES.** Lemma FV is correct, and its index conventions match the code. The numerics are
correct and stable. I reproduced them by an independent method at 400 digits, and they are robust to K → 10K and to
n = 800. Two parts of the text are wrong, though:
- The "Consequence" paragraph applies FV to the wrong quantity (F1). As a result, the reported "70–85%" first-order
  agreement is an artefact. In fact FV agrees to 1–6%, and the correct second-difference prediction to < 3%.
- The TV-nondecay criterion is presented as evidence against (T3), but it is not (F2). The same TV ≈ 0.405 holds for
  Chebyshev weights on [−1, 1], where Rakhmanov-type theorems make b_n converge for every bounded perturbation. The real
  evidence for Conjecture R is locality plus cross-scale independence ([2], [3]). My three-window run strengthens that
  evidence.

Conjecture R is plausible and adequately hedged once these fixes are made.

## Findings

**F1 (Major; §3.2 "Consequence"; check_t3_rough.py `pred`; .out "1st-order" column; "70–85%" claim).**
- *Issue.* Lemma FV gives d log b_n² = ⟨f, μ_n − μ_{n−1}⟩. The Consequence instead asserts this for
  log(b_n²/b_{n−1}²). By FV applied at n and at n−1, the correct first variation of the ratio is
  **⟨f, μ_n − 2μ_{n−1} + μ_{n−2}⟩**.
- The script prints `pred = f@(mn−mn1)`, the first variation of log b_n², next to Δ = change of log(b_n²/b_{n−1}²).
  Comparing these two produced the "70–85%" statement.
- Re-run (r1), ε = 0.05 / 0.2:

  | n | Δ log b_n² | FV for it | Δ log ratio | 2nd-difference FV |
  |---|---|---|---|---|
  | 100 | +0.0415 / +0.1598 | +0.0419 / +0.1675 | +0.0598 / +0.2371 | +0.0598 / +0.2394 |
  | 200 | +0.0387 / +0.1484 | +0.0392 / +0.1569 | +0.0486 / +0.1906 | +0.0489 / +0.1956 |
  | 400 | +0.0404 / +0.1542 | +0.0409 / +0.1638 | +0.0559 / +0.2199 | +0.0562 / +0.2248 |
  | 800 | +0.0394 / +0.1528 | +0.0398 / +0.1590 | +0.0538 / +0.2141 | +0.0539 / +0.2155 |

  First order is accurate to ≤ 1% at ε = 0.05 and ≤ 6% at ε = 0.2. This is *good* news for requirement (ii).
- The jump in the ratio exceeds 2ε·TV because −⟨f, μ_{n−1} − μ_{n−2}⟩ > 0 for this f.
- The supremum over |f| ≤ ε of the ratio's first variation is ε‖μ_n − 2μ_{n−1} + μ_{n−2}‖₁. That norm is ≈ 1.22–1.35
  (n = 100…800), not 2·TV ≈ 0.8.
- *Fix.*
  - Rewrite the Consequence with the second difference.
  - In the script, print both predictions (or the second-difference one only).
  - Replace "70–85%" by the correct agreement.

**F2 (Major; §3.2 "Consequence" last sentence; framing of Numerics [1] as counter-evidence).**
- *Issue.* "(T3) can be robust to bounded rough perturbations only if TV(μ_n, μ_{n−1}) → 0" is false as a statement
  about the limit. It holds only for "the first variation at a single n vanishes uniformly".
- Counter-model: the Chebyshev weight on [−1, 1]. There μ_n = (2/π)cos²(nθ)dθ and
  μ_n − μ_{n−1} = −(2/π)sin((2n−1)θ)sinθ dθ. Hence TV(μ_n, μ_{n−1}) → (1/2)(2/π)(2/π)·2 = **4/π² ≈ 0.405**, which is
  essentially the value observed in [1].
- Yet Rakhmanov-type theorems give b_n → 1/2 for every bounded multiplicative perturbation. (Cite with exact
  hypotheses per Rule 4 if used: Rakhmanov; Denisov–Rakhmanov; Máté–Nevai–Totik.)
- So [1] (non-decaying TV and single-n adversarial jumps) is equally present where (T3) is *robust*. It is not by itself
  evidence against (T3).
- What distinguishes the accumulating discrete case:
  - [2] locality: μ_n lives at index scale n, so windows at different scales are disjoint in k.
  - [3]/(iii) cross-scale independence: one bounded f can serve infinitely many N_i. On [−1, 1] every μ_n spreads over
    the whole interval, and the sign patterns for different N interfere.
- *Fix.*
  - State the Consequence as a first-order statement at fixed n only.
  - Add the Chebyshev contrast.
  - Present [2] + [3] as the actual evidence and (iii) as the core requirement.

**F3 (Minor; Numerics [3]).**
- *Issue 1.* "against 0.002–0.009 elsewhere" samples five values of n. Scanning every n, the maximum jump between
  windows is 0.0154 (n ∈ [100, 230]) and 0.0143 (n ∈ [300, 940]). This is still ≈ 7× below the window jumps.
- *Issue 2.* The perturbation produces a *spike*, not a step. The jump is ≈ 0.10 at both N and N+1 (n = 60: 0.112, 61:
  0.101; 240: 0.110, 241: 0.100), so β_N is an isolated outlier. The β_N/β_{N−1} reading is fine, but say so.
- *Supporting re-run* (r3, windows N = 60, 240, 960 in one sequence): jumps 0.112, 0.110 and 0.104 at those N.
  - With the 960 window alone, jumps at n ≤ 400 move by ≤ 3·10⁻⁴ (n = 60: 1.4·10⁻⁴ → 1.4·10⁻⁴; n = 240: 8·10⁻⁶ →
    1.5·10⁻⁵).
  - This is direct numerical evidence for (iii) and supports Conjecture R. It reaches the third scale.
- *Fix.* Report the max over gaps and the spike shape. Optionally add the third window to the check.

**F4 (Minor; status row Conj R vs text).** The row says "for some weights e^{−ε}k^{−s} ≤ w_k ≤ e^{ε}k^{−s}" for
general s and atoms. The conjecture text and all numerics are for x_k = k^{−2}, w = k^{−2} (p = s = 2) only.
*Fix.* State p = s = 2 in the row, or say "conjecturally for all p > 1, s; tested at p = s = 2".

**F5 (Moderate; §3.2 "Re-scoping", localization reduction).**
- *The reduction is valid* in the following form. Take w(t) = vΨ^t with ‖log Ψ‖_∞ =: L < ∞ and Ψ slowly varying, and
  put g := log Ψ − log Ψ(n). The constant drops out because μ_n and μ_{n−1} are probability vectors. Then
  |⟨g, μ_n − μ_{n−1}⟩| ≤ 2 sup_{[n/M, Mn]}|g| + 2L·(μ_n + μ_{n−1})([n/M, Mn]ᶜ).
- Integrating over t ∈ [0, 1] needs localization **for every t along the path**. The path vΨ^t stays in the sandwich
  class with ε = L, so "uniform in the sandwich class" covers it. The order of limits is lim_{M→∞} limsup_n sup_t.
- Head: say explicitly that w_k p_n(x_k)² = ρ_{n+1}(k) − ρ_n(k) ≤ 1 − ρ_n(k). Lemma Sat_p then gives head mass
  ≤ C n^{s+1} e^{−2n g_p(1/M)}, with the factor W/w_k ≤ Ck^s absorbed.
- *Issues.*
  - (a) The reduction proves **more** than (T3): log b_n(vΨ) − log b_n(v) → 0. With v = k^{−s} (RH_p: pointwise law)
    this gives the pointwise law for w directly, without G1-T. With a general base v it only transfers (T3) from v to
    vΨ. So the re-scope must name the base (v = k^{−s}, or any v with a known pointwise law).
  - (b) For *unbounded* slowly varying Ψ (e.g. log k):
    - the path leaves every fixed sandwich class;
    - g is unbounded on the tail and in the head;
    - one needs a quantitative tail bound beating the growth of |log Ψ(k) − log Ψ(n)|.
    "Ψ slowly varying" alone is not enough.
- *Fix.* State the reduction for bounded log Ψ, slowly varying, with base v = k^{−s}. Conclude b_n(w)/b_n(v) → 1, hence
  the pointwise law. Add the head inequality, and note the extra requirements in case (b).

**F6 (Minor; §3.2 "Re-scoping", first bullet).**
- *Issue.* "G1-R as posed in §4 (pointwise law from atom regularity and *sandwiched* weights)". §4 and the G1 Setting
  pose (T3) under Σw < ∞ and w_k ≥ c₁k^{−s} (one-sided). The sandwich class is a subclass.
- The logic is still right: a counterexample in the subclass refutes the broader statement.
- Also, Conjecture R contradicts β_n → 1 directly, since a non-decaying jump precludes convergence. G1-T is not needed
  for that implication, only for the equivalence remark.
- *Fix.* Describe §4 accurately. Say "a fortiori".

**F7 (Minor; reproducibility; §3.2 last Numerics bullet, plan T1, LOG).**
- *Issue.* "Generic rough weights (parity, random; scratch runs) give ≍ n^{−1/2}" rests on uncommitted runs. Plan T1 is
  ticked with no artefact. Parity is partly covered by the existing check_regularity.out (p = 2 parity:
  β_n − 1 = 5.0·10⁻², 2.8·10⁻², 1.5·10⁻² at n = 50, 200, 800, and ω(0.1) at n = 1000 is 1.4·10⁻², consistent with
  n^{−1/2}). Random weights are not covered at all.
- *Fix.* Commit the scratch script/output, or cite check_regularity.out for parity and drop "random". Label the claim
  NUMERICAL.

**F8 (Minor; Numerics robustness; Rule N).**
- *Confirmed.* Truncation K = 20n → 40n changes the jumps by ≤ 2% (n = 100: 0.0304 → 0.0300; n = 200: 0.0246 →
  0.0241). K = 200n (n = 200) gives 0.0984 vs 0.1000. Precision is confirmed by 400/600-digit mpmath and by RKPW
  binary128. Non-decay is confirmed at n = 800 (TV 0.398; jumps 0.0273 and 0.1130).
- *Caveat to record.* Transplanting the K = 20n sign pattern onto a K = 250 000 measure (f = 0 beyond 20n) gives only
  0.0206/0.0826 at n = 400. The pattern must be computed on the measure it perturbs. Only ~93% of the TV mass lies in
  k ≤ 6n: the tail beyond 6n is 6.4–7.0% for every n tested, and it decays only polynomially in M.
- *Fix.* Add one K-doubling line to the .out (Rule N), and note the n = 800 result.

**F9 (Minor; Lemma FV proof).**
- The Heine derivative, h_n = D_{n+1}/D_n, ρ_m(k) = w_kΣ_{j<m}p_j(x_k)² and ρ_{n+1} − 2ρ_n + ρ_{n−1} = w(p_n² − p_{n−1}²)
  are all correct.
- b_n² = h_n/h_{n−1} is the Lanczos b[n] that couples Q[n−1] = √w p_{n−1} and Q[n] = √w p_n, i.e. the repo's b2[n−1]
  (1-based b_n). This matches the script's use of b[n], Q[n] and Q[n−1].
- Two additions:
  - one line justifying termwise differentiation of the infinite Heine sum. It is dominated, since
    |∂_t Π_S w_k(t)| ≤ m‖f‖_∞ Π_S w_k(t), and the moments of ve^{tf} are finite because f is bounded;
  - optionally a sanity check: f = x gives d log b_n² = a_n − a_{n−1}, the Toda flow.
- Novelty: classical (Toda/Heine first variation). Mark it "standard; novelty not claimed".

**F10 (Minor; requirements (i)–(iii)).**
- (i) should bound the quantity that drives the jump, ⟨f, μ_N − 2μ_{N−1} + μ_{N−2}⟩ on the window (F1). A TV lower bound
  on the first difference is not the right quantity.
- "For all base measures in the sandwich class" is sufficient but stronger than needed. Only the measures produced
  by the inductive construction matter.
- (ii) as stated (control along the path) is right, and numerically mild (F1 table: near-linear in ε).
- (iii) is the essential ingredient (F2), not an add-on. Note that the Christoffel tail of μ_N beyond index Mn is only
  polynomially small. That is why super-exponential separation of the N_i is plausible and probably needed, while
  geometric separation (×4 in [3]) already works numerically.
- *Fix.* Reorder: (iii) first. Restate (i) with the second difference.

**F11 (Minor; LOG/README/plan).**
- LOG "≈ 0.6ε": correct (0.030/0.05, 0.12/0.2; n = 800: 0.55ε, 0.57ε).
- LOG "TV ≈ 0.4 for all n": correct, but add the F2 caveat that this alone is not counter-evidence.
- README: "numerical counterexample" overstates. Nothing is a counterexample; it is numerical evidence for a
  conjecture. Use "numerical evidence (Conjecture R)".
- Plan: T1 is ticked without an artefact (F7). The Review focus items were checked: indexing OK (F9), numerics OK
  (F8), hedging OK after F1–F2 and F5.

## Recommended labels

| Row | Label |
|---|---|
| FV | PROVED (standard; novelty not claimed) — REVIEWED after F9 |
| Conj R | CONJECTURE; NUMERICAL evidence (p = s = 2; three scales, n ≤ 1000, independent 400-digit check) — REVIEWED as a conjecture after F1–F4, F10 |
| Localization reduction | PROVED-reduction for bounded slowly varying log Ψ with base k^{−s} (yields the pointwise law via RH_p); GAP: the localization lemma's upper tail |
| G1-R | GAP; for sandwiched rough weights conjecturally false (Conj R); positive target: regular weights |

Rule R status for §3.2: **ACCEPT WITH FIXES**. A re-check after the fixes should only need to confirm the F1 text and
script change, the F2 reframing and the F5 statement.

## Re-check (commit 21c2527), 2026-10-14

Read: the new §3.2, the status rows FV / Conj R, the §4 note, README, the LOG Plan-28 entry, the plan, and
check_t3_rough.py/.out. Spot re-run (scratch `rc.py`, same Lanczos, f = ε·sign(Δ²μ), K = 20n): Δlog(b_n²/b_{n−1}²) and the
jump reproduce the new .out exactly (n = 100: +0.0672/0.034 and +0.2636/0.141; n = 200: +0.0614/0.031 and
+0.2404/0.128). The full script was not re-run.

| Finding | Status |
|---|---|
| **F1** | **RESOLVED.** FV now states both formulas, and the second follows by differencing. The script uses f = sign(Δ²μ) and prints both pairings. The text's agreement figures match the .out: Δlog b_n² within 2% (ε = 0.05) and ≤ 11% (ε = 0.2); the ratio within 3%; ‖Δ²μ‖₁ = 1.23–1.35. |
| **F2** | **RESOLVED.** The robustness "only if" is gone. The "What the evidence is" paragraph gives the Chebyshev contrast (4/π²) and locates the evidence in [2] + [3]. The Rakhmanov remark is labelled "recollection, not cited" and is used only as contrast, never in a proof. That is acceptable under Rule 4 as written; quote the source if it is ever used in an argument. |
| **F3** | RESOLVED. Spikes at N and N+1 and the max over all other n (0.030) are reported. |
| **F4** | RESOLVED. Conjecture R and its status row are restricted to p = s = 2. |
| **F5** | **RESOLVED.** The reduction is stated with base k^{−s}, Ψ bounded above and below with log Ψ slowly varying, the path in a fixed sandwich class, the head bound μ_n ≤ 1 − ρ_n via Sat_p, localization uniform along the path, and the conclusion b_n(vΨ)/b_n(v) → 1 (more than (T3)). Unbounded Ψ is flagged. Nit: the localization hypothesis is needed for μ_{n−1}^{(t)} as well as μ_n^{(t)} (trivially the same statement at n−1). |
| **F6** | RESOLVED. The one-sided conditions are cited, with "a fortiori" and the direct refutation of β_n → 1. |
| **F7** | RESOLVED. Generic-weight decay is committed as [4]. Over n = 250 → 3600 both families drop by a factor of 4.05, against √14.4 = 3.8, consistent with n^{−1/2}. Minor: at n = 3600 the K vs 2K values differ by 5% (parity) and 8% (random), so the last column is at the edge of truncation. Optional caveat. |
| **F8** | RESOLVED. [1b] K = 20n vs 40n gives 0.128 for both, and the transplant caveat is stated. |
| **F9** | RESOLVED. The dominated-convergence line and the Toda check were added, and the label is "standard; novelty not claimed". |
| **F10** | RESOLVED. The list is reordered with (iii) first, (i) is restated with ‖Δ²μ_N‖₁ for the measures that arise in the construction, and (ii) is kept. |
| **F11** | RESOLVED. README says "numerical evidence", the LOG records the Rule R outcome, and plan T1 points to [4]. |

**Residual items.**
- **R1 (must fix before merge; PROOF.md line 366).** "Plan 29 (§3.3) proves the case Ψ_k → L, where the tail is not
  needed." There is no §3.3 at this commit, and no Plan 29 appears in the LOG, README or plans. This is a dangling forward
  reference to unreviewed work. Fix: delete it, or rephrase it as "(planned: Ψ_k → L; the tail term then vanishes
  because g_n → 0 uniformly on k ≥ n/M)" and add it when Plan 29 lands.
- **R2 (cosmetic).** The Conj R status row and the [3] bullet cite "three scales, n ≤ 1000, independent 400-digit
  check". Those are reviewer scratch runs, not committed checks. Fix: append "(REVIEW_Plan28 re-runs)" to the row, or
  commit an equivalent script.
- **R3 (cosmetic).** After this re-check, update the §3.2 heading, the FV row and the LOG ("re-check pending") to the
  final status.

**Re-check verdict: ACCEPT**, conditional on R1. R2 and R3 are cosmetic.

**Final labels.**

| Row | Label |
|---|---|
| FV | PROVED (standard; novelty not claimed) — REVIEWED |
| Conj R | CONJECTURE; NUMERICAL (p = s = 2; committed: two scales n ≤ 400 plus Rule N; reviewer re-runs: three scales n ≤ 1000, n = 800, 400-digit mpmath) — REVIEWED as a conjecture |
| Localization reduction | PROVED-reduction (bounded Ψ with slowly varying log Ψ, base k^{−s}; gives the pointwise law via RH_p); localization upper tail = GAP — REVIEWED |
| G1-R | GAP; conjecturally false for sandwiched rough weights (Conj R, p = s = 2); positive target is regular weights |
| §3.2 | Rule R ACCEPT WITH FIXES; re-check ACCEPT (after R1) — REVIEWED |
