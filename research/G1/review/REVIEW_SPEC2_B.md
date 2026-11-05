# Rule R review, reviewer B (computation): SPEC.md §§3.3–3.13

Reviewer: independent second reader B (Rule R, computation side). Remit:
1. Re-run the §§3.3–3.13 checks from the caches and compare with the committed .out files.
2. Recompute key predictions with my own code: Robin zeta values; the pole law at a new (p, m); the Lommel closed form at a
   new μ; the Hurwitz rule H at a new (p, δ).
3. Sabotage tests (Rule A for computations).
4. Fit robustness of the headline numbers.
5. Rule X: which "predictions" in §§3.10–3.13 were adjusted after the data were seen.

- **Target:** research/G1/RH/spectral/SPEC.md §§3.3–3.13 (2026-10-21, HEAD 7a5d63c), and checks/spec_*.py with their .out
  files.
- **Context read:** AGENTS.md, VERIFICATION_POLICY.md (Rules N, X, A), SPEC.md §§0–2, REVIEW_SPEC_A.md and
  REVIEW_PlanE3_B.md (for the house style), second_order/checks/so_coeffs.py and so_fit.py, and the git history of
  spec_pole.py, spec_resonance.py and spec_robin.py.
- **Independence.** REVIEW_SPEC2_A.md (reviewer A, same sections) is in the repo. I did not read it before or while writing
  this report.
- **Files.** I edited no repository file except this report. Scripts ran with `python -B` through a wrapper that points both
  caches at the scratchpad (symlinks to the repo caches, plus new files). Scratch:
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/reviewSPEC2B/, with:
  - `wrap.py`, `rerun.sh`, `rerun/` (task 1);
  - `indep/` (tasks 2 and 4; own code, own cache `cache_own/`);
  - `sabotage/` (task 3).

## Overall verdict: **ACCEPT WITH FIXES** (computation side)

**Reproduction.** All 17 requested checks re-run from the caches. 16 reproduce their .out exactly. spec_pole.out does not:
two of its rows come from an earlier version of the script (F3).

**Independent recomputations.** Every one confirms the note.
- **Robin zeta values.** Z_E(−1) = −h²/2 and Z_E(−2) = h(h³+1)/2 at h = ½, 1, 2. I computed them from the eigenvalues by a
  Hurwitz-type regularisation, using an asymptotic expansion of the Robin zeros that I derived myself. Agreement is
  10⁻¹³–10⁻⁸.
- **Pole law at new parameters.** At p = 1.1, m = 1 the prediction is +5.349641 and the fit gives +5.34969 ± 1.3·10⁻⁴. At
  p = 0.6, m = ½ (W = 0.841) the prediction is +1.14367 and the fit gives +1.1453 ± 4·10⁻³; the W-dropped value 1.3604 is
  excluded.
- **Lommel.** The closed form holds at μ = 2.5 and 0.7 to 4·10⁻¹⁶ and 8·10⁻¹⁶.
- **Rule H at p = 1.25, δ = ½.** d₂ agrees to 6·10⁻⁷ and ε₁ to 1·10⁻⁷. d₃ is confirmed only at the 10⁻² level, and the
  n^{−(2+p)} term is not resolvable.

**Two MAJOR findings.** Neither changes a number in the note.
- **F1.** As written, the general pole-law formula of §3.12 has the opposite sign to the note's own prediction and to the
  data. The sign is not a calibration: it follows from the Mellin–Barnes integral.
- **F2.** Caches are keyed by a tag string only. A change to the measure (the operator, the boundary condition, the
  normalisation) is invisible to a re-run when a cache with the same tag exists. I demonstrated this with two sabotages.

**Precision.** Several headline numbers are quoted more precisely than the fits support (F5). None of the conclusions
changes.

**Rule X.** The record is good. Git shows that the pole-law predictions were committed before the measures were generated
(F10). The resonance constant term is a derivation, not a fit, but the a priori test there is the log coefficient (F6).

| Item | Verdict | Fixes |
|---|---|---|
| Task 1: re-runs of the 17 checks | ACCEPT WITH FIXES (16/17 identical; spec_pole.out mixes two script versions) | F3 |
| §3.3 Prop. B numerics (spec_bouncer_closed) | ACCEPT (identical; the assertions have teeth) | — |
| §3.4 Neumann/Maslov (spec_neumann) | ACCEPT | F4 |
| §3.5 Möbius identity, κ law (spec_mobius, _pred, kappa_fit) | ACCEPT WITH FIXES (the p = 0.3 "0.1%" is within a 60% half-range) | F5 |
| §3.8 Airy index map (spec_airy_index) | ACCEPT (INFO: docstring, self-calibrated offset) | F9 |
| §3.10 S1′ evidence (hur_d2, bouncer_d2, lommel, hur_small) | ACCEPT (identical; Lommel re-verified at μ = 2.5, 0.7) | F9 |
| §3.11(a) rule H (spec_shift_hi) | ACCEPT WITH FIXES (H holds; the quoted d₃ agreements are optimistic by 10²–10³; at δ = −½ the n^{−3.5} probe does not discriminate) | F5 |
| §3.11(b) γ/k^m lattices (spec_gamma, gamma2) | ACCEPT (identical) | — |
| §3.12 pole law: numbers | ACCEPT (re-verified at two new (p, m)) | F3, F5, F8 |
| §3.12 pole law: statement and sign | FIX REQUIRED (sign error in the general formula; the "calibration" is unnecessary) | F1 |
| §3.13 log resonance | ACCEPT WITH FIXES (derivation re-done; weak control; 6-digit quote) | F5, F6 |
| §3.13 Robin zeta values and ε₁ | ACCEPT (independently confirmed; add the n^{−4/3} test and the no-pole remark) | F4, F7 |
| Check infrastructure (caches, assertions) | FIX REQUIRED | F2, F4 |

## 1. Task 1: re-runs from the caches

The wrapper sets spec_common.CACHE and so_coeffs.CACHE to scratch directories that symlink every repo cache file. Nothing
was regenerated except where noted. I compared each output against the committed .out with `diff`, after removing my
`###` header lines.

| Script (args as in the .out) | Result |
|---|---|
| spec_bouncer_closed | identical; ALL ASSERTIONS PASSED |
| spec_neumann 2.0 | identical |
| spec_mobius | identical; ALL ASSERTIONS PASSED |
| spec_mobius_pred | identical |
| spec_airy_index | identical; ALL ASSERTIONS PASSED |
| spec_hur_d2 | identical |
| spec_bouncer_d2 | identical (Neumann s = 3 absent in both: no cache) |
| spec_lommel | identical; ALL ASSERTIONS PASSED |
| spec_hur_small 3/4 2.0 −0.5 | identical. Cached in plan62_cache (`_d-0.5`). The committed .out has a stray line "[exited with code 0]" (F9). |
| spec_shift_hi | identical |
| spec_gamma (5 argument sets), spec_gamma2 (2) | identical |
| spec_pole (6 argument sets) | **differs** in 4 numbers: p = 0.8 (n ≥ 200/400/800: −1.570783/−1.570792/−1.570813, against −1.570792/−1.570795/−1.570815 in the .out), and p = 1.25, m = ½ at n ≥ 200 (−0.235177 against −0.235178). F3. |
| spec_resonance 0.5 2.0 0.5 0.5 | identical |
| spec_robin 1.0 2.0 (and 0.5, 2.0 from the same cache) | identical |
| spec_stats_summary, spec_kappa_fit | identical |

I traced the spec_pole difference. Running the first committed version (c554aa3, with `jmax = floor(2.5/p) + 1`) on the same
caches reproduces the .out values exactly. That version also subtracts j = 4 at p = 0.8. The current script
(`jmax = ceil(2.5/p) − 1`, changed at 04:28:14 because j = 4 hits ζ(1) at p = ¾) gives my values. So the committed .out was
assembled from runs of two script versions. The note's §3.12 table row for p = 0.8 quotes the old numbers. The effect is
≤ 9·10⁻⁶, but the .out does not certify the committed .py.

## 2. Task 2: independent recomputations (own code; NUMERICAL)

### 2.1 (a) Robin zeta values from the eigenvalues (`indep/robin_zeta.py`, `indep/dlmf_check.py`)

This route does not touch F′/F or the Mellin step.
1. I check the oscillatory forms DLMF 9.7.9–9.7.10 for Ai(−z) and Ai′(−z) numerically at z = 20 and 60 (errors 10⁻¹⁴ and
   10⁻²⁰).
2. Robin condition Ai′(−E) = hAi(−E). Write ζ = (2/3)E^{3/2} and τ = π(k − ¾). Then
   ζ = τ + arctan Q, with Q = (hU_e z^{−1/2} + V_o)/(V_e − hU_o z^{−1/2}). I solve this by fixed-point iteration as an exact
   series in ε = τ^{−1/3} to order ε¹⁶ (sympy). Leading term: δ = 18^{1/3}/3·hε + O(ε³). Only odd powers of ε occur.
3. Then E^{−s} = (3τ/2)^{−2s/3}Σ_ig_i(s)τ^{−i/3}. I regularise term by term with ζ(2s/3 + i/3, ¼), use exact zeros
   (mpmath findroot) for k ≤ 80, and evaluate at s = −j ± 10⁻¹², +10⁻²⁰.
4. Possible poles at s = −j come from i = 2j + 3. I find g_{2j+3}(−j) = 0 for j = 0, 1, 2, so Z_E is regular there, and the
   ± values agree.

| h | Z_E(0) | Z_E(−1): computed / −h²/2 | Z_E(−2): computed / h(h³+1)/2 |
|---|---|---|---|
| ½ | 0.25 (diff 4·10⁻²¹) | −0.124999999999727 / −1/8 | 0.281250000037 / 9/32 |
| 1 | 0.25 | −0.499999999999783 / −1/2 | 1.0000000000575 / 1 |
| 2 | 0.25 | −1.99999999995398 / −2 | 9.0000000126 / 9 |

The residuals 10⁻¹³–10⁻⁸ come from truncating at ε¹⁶. Their E₁ values (1.40744436727, 1.64761941349, 1.90327571905) agree
with the bisection values in spec_robin.out. **Confirmed.** This also bears on F7: the expansion has only odd powers of
ε = τ^{−1/3}, so every index correction sits at q = i/2 with i odd, a half-integer. The poles of Z_E at integer s are absent.

### 2.2 (b) The pole law at new (p, m), fresh measures (`indep/meas.py`, `indep/pole_own.py`)

Code and inputs:
- my own measure builder (atoms 1/λ, masses λ^{−s/p}, Gauss–Jacobi continuum tail; the toolkit's jacobi_rkpw, binary128);
- my own lattice runs;
- ΔZ(−j) regularised by my own binomial-series code (i < 12, k ≤ 4000);
- my own exponent pool {a + bp + lm} and fits with scaled columns, over J = 5–8 and n ≥ 100, 200, 400, 800.

γ = ½, s = 2.

| p | m | W(m/p) | cot(πm/p) | predicted −mγWπcot | fit: core (J ≤ 7, n ≥ 100–400) | excluded alternatives |
|---|---|---|---|---|---|---|
| 1.1 | 1 | 1 | −3.40569 | **+5.349641** | +5.34969 ± 1.3·10⁻⁴ | wrong sign (47 half-ranges of the full scan) |
| 0.6 | ½ | 0.840715 | −1.73205 | **+1.143666** | +1.1453 ± 4·10⁻³ (J ≤ 6 on n ≥ 100–400, and J = 7 on n ≥ 100–200) | W dropped: 1.3604 (≈ 50 core half-ranges); wrong sign |
| 1.25 | 1 (own re-run of a note case) | 1 | −1.37638 | +2.162016 | +2.16203 ± 7·10⁻⁵ | — |

**Confirmed** at both new points, including W(q) ≠ 1 at a q (0.833) not used in the note. At p = 0.6, m = ½ the J = 7–8 fits
on n ≥ 400–800 are unstable (up to 2.4). I excluded them from the core.

### 2.3 (c) Lommel at new μ (`indep/lommel_own.py`)

Own measure: zeros from mpmath.besseljzero for k ≤ 300, my own McMahon series beyond (DLMF 10.21.19, four terms, checked to
2·10⁻¹⁶ at k = 400), K = 200000, and a Gauss–Jacobi tail with offset μ/2 − ¼. Checked for n ≤ 40 against
n²b_n/c = 4n²/((2n+μ)√((2n+μ)²−1)): worst relative difference 4.1·10⁻¹⁶ (μ = 2.5) and 8.1·10⁻¹⁶ (μ = 0.7). **Confirmed.**

### 2.4 (d) Rule H at p = 1.25, δ = ½ (`indep/hur_own.py`; own lattice and shifted-lattice measures)

The expansion of (1 + δ/n)^{−p}Φ(n + δ) is my own sympy computation.

| Quantity | Predicted (H) | Fit (median, half-range) | Verdict |
|---|---|---|---|
| d₁ | −1.125 | −1.125000000 (7·10⁻⁹) | ✓ |
| d₂ | +1.3103125 | +1.3103119 (3.2·10⁻⁴) | ✓, diff 6·10⁻⁷ |
| ε₁ = 2pcζ(−p, 3/2) | −0.5249698 | −0.5249699 (4.3·10⁻⁵); unshifted ζ would be −0.0655 | ✓, diff 1·10⁻⁷ |
| lattice d₂⁰ (E2 closed form) | +0.39625 | +0.396242 (5.4·10⁻⁴) | ✓ |
| d₃ from the fitted d₃⁰ | −1.61125 | −1.6100 (9·10⁻²); same-config differences: median −3·10⁻⁵, range [−0.086, +0.004] | consistent, ~10⁻² level only |
| n^{−(2+p)} = n^{−3.25} | +1.629 | +1.63 (2.2) | not resolvable (n^{−3} and n^{−3.25} are degenerate on n ≤ 1600) |

H is confirmed through ε₁ at a new (p, δ). At p = 1.25 the third-order part is only weakly tested.

## 3. Task 3: sabotage (`sabotage/s*.py`, `sabotage/sabotage.out`)

Each sabotage is a one-line change in a copy (two lines for s5). "Detected" means that the printed comparison is off by ≫ the
spread. Only s10 and s11 make the script fail: no other numerical check has an assertion (F4).

| # | Sabotage | Script | Outcome |
|---|---|---|---|
| s1 | sign of the prediction (+cot) | spec_pole | detected by eye (all rows); exit 0 |
| s2 | W(q) → 1 | spec_pole | **invisible at m = 1** (W(1/p) = 1 identically); detected at m = ½ (−0.4535 against −0.4247 at p = 1.5); exit 0. F8 |
| s3 | ζ(−jp, a) → ζ(−jp) in the ε_j subtraction | spec_hur_d2 | detected at p = 0.6 and 0.75; **invisible at p = 1.5** (1 + p = 2.5 fails `e < 2.5`, so nothing is subtracted; harmless for d₂, F9); exit 0 |
| s4 | sign of δ in the d₂ shift | spec_hur_d2 | detected; exit 0 |
| s5 | δ → −δ in the d₃ and n^{−3.5} predictions | spec_shift_hi | d₃ detected (1.8 against 10⁻³). n^{−3.5} at δ = −½: H off by 0.11, **within** the 0.13 spread; detected at δ = ½ and 1; exit 0 |
| s6 | ζ(−p, a) → ζ(−p) | spec_shift_hi | detected; exit 0 |
| s7 | h → −h in the Robin eigenvalue equation | spec_robin | **invisible with the existing cache.** Every fitted number is unchanged, because the stale robin_h1.0 cache is reused (F2). The only sign is "residual max \|F\| 2.3e+00" in a print. The bisection then silently returns the Dirichlet zeros (E₁ = 2.338). With a fresh cache: detected (ε₁ fit −432); exit 0 |
| s8 | C → C^{1/2} in Z_{λ′}(−1) | spec_robin | detected (−0.176 against −0.105); exit 0 |
| s9 | drop −γW(j) in the resonance constant | spec_resonance | detected (+0.0232 against −0.181); exit 0 |
| s10 | v_k formula | spec_bouncer_closed | AssertionError ✓ |
| s11 | δ = μ/2 + ¼ in the index-shift identity | spec_lommel | AssertionError ✓ |
| s12 | C → C^{1/2} (the bouncer normalisation) | spec_bouncer | prediction side detected (Z(−1) = 2782). Measure side **invisible with the existing cache**; with a fresh cache, d₁ = −4600; exit 0 |
| s13 | drop the regularisation terms of Z(−1) | spec_gamma | detected; exit 0 |

**Checks without teeth:**
- (i) every numerical comparison script has no pass/fail assertion. Pass/fail is human reading of printed numbers.
- (ii) spec_robin.py line 32, `assert … == 0 or True`, can never fail.
- (iii) the Robin bisection's residual and bracket validity are printed, not asserted.
- (iv) the measure side of every `run(tag, …)` / `coeffs(…)` check is shielded by tag-keyed caches (F2).
- (v) W(q) is untested at m = 1 by construction.
- (vi) spec_airy_index asserts only that the offsets agree with offs[0], not that the offset is 1/6.

## 4. Task 4: fit robustness (`indep/robust_*.py`)

For each number: re-fits on the authors' caches over J and windows (n ≥ 100–800), with scaled columns. I also checked the
sensitivity to 10⁻¹⁵ relative noise in b_n: ≤ 3·10⁻⁸ for every pole fit, so float rounding is irrelevant.

| Headline (note) | Note quotes | Honest spread (J ≤ 7, n ≥ 100–400) | Including n ≥ 800 / larger J | Assessment |
|---|---|---|---|---|
| Pole p = 1.25, m = 1: 2.162016 | "to 10⁻⁶" (§3.12 title) | ±3.9·10⁻⁶ (median = prediction to 10⁻⁷) | ±6.7·10⁻⁴ | supported at ~4·10⁻⁶ |
| Pole p = 1.8, m = 1 | 0.276974 | ±2·10⁻⁷ | ±4·10⁻⁵ | supported |
| Pole p = 0.8, m = 1 | −1.570792 (old .out) | ±4.5·10⁻⁵ | ±1.2·10⁻³ | "10⁻⁶" overstated |
| Pole p = 0.75, m = 1 | −0.906866 … | ±4.2·10⁻⁵ (median off by 1.5·10⁻⁵) | ±2.1·10⁻³ | "10⁻⁶" overstated |
| Pole p = 1.5, m = ½ | −0.424703 | ±3.7·10⁻⁵ | ±2.1·10⁻³ | ok at 10⁻⁵ |
| Pole p = 1.25, m = ½ | −0.235178 | ±2.9·10⁻⁴ | ±6·10⁻² | ok at 3·10⁻⁴ |
| Resonance log coefficient | +0.102071 (pred 0.102062) | +0.102067 ± 1.4·10⁻⁴ (J = 4–5, n ≥ 100–200) | up to 1.17 (J = 6, n ≥ 400) | agreement ~10⁻⁴ (0.1%), not 10⁻⁵ |
| Resonance n^{−1/2} coefficient | −0.180969 (pred −0.180893) | −0.18093 ± 1.6·10⁻³ | up to −14 | agreement ~1%; the uncorrected value +0.0232 is excluded by ~130 spreads |
| Robin ε₁ (h = ½, 1, 2) | −0.0262417 / −0.1049772 / −0.4198287 with spreads | core medians −0.0262469 / −0.1049843 / −0.4198486; ±8·10⁻⁴ / 1.6·10⁻³ / 3.3·10⁻³ | ±1.8–7.3 | supported; the note's spreads are honest (pred − fit = 2–4% of the spread) |
| Hurwitz d₃ (p = 1.5), §3.11(a) | 9·10⁻⁷, 2·10⁻⁵, 7·10⁻⁵ | same-config differences: ranges ≤ 1·10⁻⁴, 1.9·10⁻³, 1.3·10⁻² (δ = −½, ½, 1) | up to 8·10⁻² | supported at relative 3·10⁻⁴–2·10⁻³ of the shifts; the quoted values are best-case medians |
| Hurwitz n^{−3.5} H vs A | "alternative off by 0.056, 1.1, 7.0 (spreads ≈ 0.14)" | H − fit core medians 3·10⁻⁴, 10⁻³, 1.4·10⁻³; A − fit 0.056, 1.1, 7.0 | — | discriminating at δ = ½ and 1; **not** at δ = −½ (0.056 < spread) |
| κ law, p = 0.3 | "all agree within 0.1%" | half-range 0.74 (60%); geometric extrapolation −1.324 (8% off) | — | the 0.1% at p = 0.3 is not supported; spec_mobius_pred's trend (0.86 → 0.947) is the real evidence |

**Robin, a new direct test of "cot = 0 at q = ½"** (`indep/robin_43.py`). Put n^{−4/3} into the pool (the exponent of the
hk^{−1/3} pole term). Its fitted coefficient is +5·10⁻⁸, +3·10⁻⁷ and +3·10⁻⁶ (spreads 1–5·10⁻⁵) at h = ½, 1, 2. A
non-vanishing kernel at q = ½ would give a term of order p·|R|·W(½)·π ≈ 0.17h, with R = −mγ/p, m = ⅓ and γ = 18^{1/3}h/(3π^{4/3}).
So the kernel vanishes at q = ½ to ~3·10⁻⁴ relative. This is a sharper test of the cot-zero claim than the d₂ column of the
§3.13 table (spreads 8·10⁻³–3·10⁻²).

**Resonance control** (`indep/robust_res.py`). The script's control (RMS 3.37·10⁻⁸ without the log term, 2.48·10⁻⁸ with it)
is weak, because the fit without the log column refits all the other powers. Fix the log coefficient instead, at 0, at the
prediction, and at twice the prediction. The RMS residuals are 1.69·10⁻⁶ / 2.2·10⁻⁸ / 1.69·10⁻⁶ (n ≥ 100) and
2.8·10⁻⁷ / 2.3·10⁻⁸ / 2.8·10⁻⁷ (n ≥ 200). The log term is required, at the predicted value.

## 5. Task 5: Rule X and the derivations

**Pole-law sign (§3.12).** The note says the sign "is calibrated once, by the m = 1 data at p = 0.6". The sign is not free:
- Take the stated integral, −(p/n)(1/2πi)∫W(w)Z(−w)π cot(πw)n^{−wp}dw, upward along Re w = c with c slightly negative.
- Close to the right; n^{−wp} decays there, and the contour is clockwise. The value is **+** Σ residues.
- The integer residues are +W(j)Z(−j). That is required, and it fixes the overall sign.
- A pole of Z(−w) at w = q with residue R_w then contributes +p·R_w·W(q)·π cot(πq)·n^{−1−pq}.
- For λ_k = (k + γk^{−m})^p, R_w = Res_{w=m/p}Z(−w) = −mγ/p. The term in D is −mγW(m/p)π cot(πm/p)n^{−m}, which is the
  note's prediction and agrees with the data.
- The note's general formula reads "−p·R·W(q)·π cot(πq)" with "R = −mγ/p". That gives +mγWπcot, the opposite sign (F1).
- §3.11 uses the residue in s (γ/p at s = −1/p), while §3.12 says "Z(s) … has a pole at q = m/p with residue R = −mγ/p",
  which mixes the s and w conventions.

So the sign is derivable. The real content, which cannot be calibrated, is the choice of kernel π cot(πw); §3.13 motivates it
heuristically. The kernel is not fixed by the integer residues: adding sin(πw)·(entire) changes the non-integer poles. That
choice was identified from the p = 0.6 and 1.5 data (both give π/√3). Those two rows are fits; the rest are predictions.

**Pre-registration (git).**
- c554aa3 (04:20:10) commits spec_pole.py with the explicit prediction −mγW(m/p)π cot(πm/p).
- The six pole caches were created at 04:21–04:27, so the §3.12 rows for p = 1.25, 1.8, 0.8, 0.75 and the two m = ½ rows are
  genuine out-of-sample tests.
- The later jmax change (04:28:14) alters which zeta-layer terms are subtracted. It is a code fix (j = 4 hits ζ(1) at p = ¾),
  not a fit. My own code, with a different subtraction set and pool, gives the same numbers (§2.2, §4).
- The Robin closed forms were committed at 04:48:09 (3f13e62), before the h = ½ and h = 2 runs (04:50:32). The h = 1 run
  (04:47:32) preceded the commit, but the formula has no free parameter.

**Resonance constant.** The brief reports that the −γW(j) term was added after a mismatch. Neither the note nor git records
this, because spec_resonance.py was first committed with it. I re-derived the formula independently:
- Perturb m′ = p(j + ε).
- Integer term: pW(j)ΔZ_ε(−j)n^{−jp}, with ΔZ_ε(−j) = jγ/ε + Z_fin + O(ε), and ζ(1 + pε) = 1/(pε) + γ_E.
- Pole term: p·(−(j + ε)γ)·W(j + ε)·π cot(πε)·n^{−(j+ε)p}.
- The 1/ε terms cancel. The limit is p²jγW(j)n^{−jp}log n + pn^{−jp}[W(j)Z_fin − γW(j) − jγW′(j)].
- The −γW(j) term is the ε·(1/ε) product from the prefactor (j + ε). It is forced by the pole law; there is no freedom.
- Numerically, the sum of the two terms at m′ = p(1 + ε), n = 1000, tends to the limit formula: 0.016574950806 at ε = 10⁻⁴,
  0.0165743599856 at 10⁻⁶, limit 0.0165743540134.

Judgement: **a derivation that corrected an omitted step, not a fit.** The a priori test is the log coefficient, which
involves no correction. The constant term after the correction is a consistency check, and the note should say so (F6).

**Other provenance points.**
- §3.5: the κ candidate −2(2−p)cκ was identified from p = 0.6, κ = 1, so that row is a fit. κ = ½ and p = 0.3 are tests; the
  p = 0.3 test is weak (§4).
- §3.11(a): the d₃ and n^{−3.5} "predictions" use the fitted d₃⁰ and f⁰. They test the δ-dependence only, as the note says.

## 6. Findings and required fixes

**F1 (MAJOR): the pole-law statement has the wrong sign (§3.12).**
- **Problem.** With R defined as the residue of w ↦ Z(−w) (as the text says, and R = −mγ/p as computed), the contribution is
  +p·R·W(q)·π cot(πq)·n^{−1−pq}, not −p·R·…. The note's numerical prediction −mγWπcot is right; the general formula
  contradicts it.
- **Fix.**
  - State: "a pole of Z(−w) at w = q with residue R_w contributes +pR_wW(q)π cot(πq)n^{−1−pq}". Equivalently, −p·Res_{s=−q}Z(s)·….
  - Specify the contour (Re w = c ∈ (max(−½, −1/p), 0)) and that it is closed to the right.
  - Replace "the sign is calibrated once" by the residue argument of §5.
  - Make the residue convention uniform in §3.11 and §3.12.
  - Add to §3.12: "the kernel π cot was identified from p = 0.6 and 1.5; the other rows are pre-registered (c554aa3)".

**F2 (MAJOR): caches are keyed by a tag, not by content.**
- **Problem.** `spec_common.run(tag, lam, …)` and `so_coeffs.coeffs` return the cached file whenever the tag exists,
  whatever `lam` now is. Sabotages s7 (Robin sign) and s12 (bouncer normalisation) are invisible on re-run. spec_bouncer_d2
  even calls `run(…, None, …)`. So the .out files certify the cached measures, not the committed code.
- **Fix.**
  - Store a hash of (λ array, masses, K, tail offset, NMAX, code version) in the cache file name or a header, and verify it
    on load.
  - Before REVIEWED, regenerate the §§3.3–3.13 caches from a clean directory, regenerate the .out files, and record this in
    §6. At the measured ~1–2.5 min per measure on 2 cores this is about an hour.

**F3 (MINOR): spec_pole.out is not reproducible from the committed spec_pole.py.**
- **Problem.** The p = 0.8 rows and the p = 1.25, m = ½, n ≥ 200 value come from c554aa3 (old jmax). See §1.
- **Fix.** Regenerate spec_pole.out with the current script and update the §3.12 table (p = 0.8: −1.570783 / −1.570792 /
  −1.570813).

**F4 (MINOR): no pass/fail in the numerical checks; one toothless assert.**
- **Problem.**
  - None of spec_pole, spec_resonance, spec_robin, spec_hur_d2, spec_bouncer_d2, spec_shift_hi, spec_gamma(2),
    spec_hur_small, spec_neumann (part 3) or spec_kappa_fit has an assertion (Rule N.3 asks for computed pass/fail).
  - spec_robin.py line 32 is `assert … or True`.
  - The Robin bisection does not assert that the bracket changes sign or that the residual is small. With h → −h it returns
    the Dirichlet zeros silently.
- **Fix.**
  - Assert |fit − pred| ≤ k·half-range, with k stated, and also that the main alternative is excluded (wrong sign, W dropped,
    unshifted ζ, uncorrected resonance constant).
  - Assert the residual and sign change in spec_robin.
  - Remove `or True`.

**F5 (MINOR): precision overstated in places.** Quote these instead (§4):
- §3.12 title "to 10⁻⁶": ~4·10⁻⁶ for p > 1, m = 1; 4–5·10⁻⁵ for p < 1; 4·10⁻⁵–3·10⁻⁴ for m = ½.
- §3.13 resonance: log coefficient 0.10207 ± 1.4·10⁻⁴ against 0.102062; constant −0.1809 ± 1.6·10⁻³ against −0.180893.
- §3.11(a) d₃: agreement within same-config ranges of 10⁻⁴, 2·10⁻³ and 1.3·10⁻². Also state that at δ = −½ the n^{−3.5}
  probe does not separate H from A (gap 0.056 < spread 0.13).
- §3.5: drop "all agree within 0.1%" for p = 0.3 (half-range 0.74), and cite the spec_mobius_pred trend instead.

**F6 (MINOR): resonance write-up.**
- **Problem.** The control in spec_resonance is weak (§4). The −γW(j) correction is not recorded as post hoc.
- **Fix.**
  - Replace the control by the fixed-log-coefficient test (RMS ×76 at n ≥ 100 for L = 0 or 2L).
  - State the ε → 0 derivation (§5) and that the constant-term agreement is post-correction. The pre-correction value
    +0.0232 is excluded by ~130 spreads. The log coefficient is the a priori test.

**F7 (MINOR): Robin, two additions that strengthen §3.13.**
- (i) Z_E(−j) is finite because the coefficient g_{2j+3}(−j) of the would-be ζ(1) term vanishes (verified for j = 0, 1, 2,
  §2.1). Say so; otherwise "Z_E(−1)" needs a finite-part definition.
- (ii) Add the n^{−4/3} coefficient test (§4). It tests cot(π/2) = 0 directly, at ~3·10⁻⁴ relative, which the d₂ column
  cannot.
- Optionally also cite my eigenvalue-side confirmation of Z_E(−1) and Z_E(−2) (§2.1). It is independent of the Hadamard and
  Mellin steps, which are still NOT QUOTED under Rule C.

**F8 (INFO): W(q) is tested only at m = ½.** W(1/p) = 1 identically, so the four m = 1 rows cannot see W (sabotage s2).
§2.2 adds a third W ≠ 1 case (p = 0.6, m = ½, W = 0.8407), confirmed at 0.3%.

**F9 (INFO): hygiene.**
- **Run-order dependencies.** spec_bouncer_d2, spec_mobius_pred and spec_stats_summary need other scripts' caches or
  outputs; document the order.
- **Stray line.** spec_hur_small.out ends with "[exited with code 0]".
- **spec_airy_index.** The docstring says "φ(x)/π − 1/4 + …", but the offset is 1/6 (as the note says). The assertion only
  checks that the offsets are constant; assert 1/6.
- **spec_hur_d2 at p = 1.5.** ε₁ (exponent 2.5) is not subtracted because of `e < 2.5`. It is harmless (2.5 is in the fit
  pool), but the docstring implies otherwise.
- **Lattice construction.** The Plan 62 lattice (x = k^{−p}, w = k^{−s}) and spec_common.run (1/λ, λ^{−s/p}) differ in
  float64 rounding. b_n differs by 6.5·10⁻¹⁵ relative, so D = n(y − y_lat) carries ~10⁻¹¹ noise. My tests show no effect on
  any fit (§4).
- **Runtime.** The brief's "3–5 min per measure" is now ~1.1 min (p > 1, K = 160000) and ~2.2 min (p < 1, K = 320000).

**F10 (INFO, positive): provenance is checkable and good.** The pole-law predictions were committed before the data (§5),
and the Robin closed forms have no free parameter. Record the commit hashes in the §6 Rule X log of SPEC.md.

## 7. Run log (session scratchpad `reviewSPEC2B/`, 2026-10-21, MDT; venv python, `-B`)

| Time | What | Duration |
|---|---|---|
| 04:55–04:57 | rerun.sh: the 17 checks (all argument sets) from symlinked caches; diff against the .out files | ~2 min in total (spec_robin 36 s, mostly bisection; the rest ≤ 10 s each) |
| 04:57–05:03 | dlmf_check.py; robin_zeta.py (sympy series to ε¹⁶; h = ½, 1, 2; j = 0, 1, 2) | ~5 min |
| 05:03–05:12 | pole_own.py: new measures pole p1.1/m1, lat p1.1, pole p0.6/m0.5, lat p0.6, pole p1.25/m1, lat p1.25 | 68, 68, 134, 132, 66, 67 s |
| 05:12–05:14 | robust_pole.py (6 note cases, two lattices, noise sensitivity); spec_pole determinism re-runs (OMP threads 1) | ~2 min |
| 05:14–05:16 | robust_res.py (ε-limit check, scans, fixed-log control) | ~1 min |
| 05:16–05:17 | hur_own.py: new measure Hurwitz p1.25/δ½ | 67 s |
| 05:17–05:18 | robust_shift.py, robust_robin.py, robin_43.py | < 1 min each |
| 05:18 | lommel_own.py (μ = 2.5, 0.7) | 2 s each |
| 05:18–05:24 | sabotage/run.sh: s1–s13; fresh caches for s7 (Robin, 174 s) and s12 (bouncer, 142 s) | ~6 min |
| 05:25 | the original c554aa3 spec_pole.py on the same caches (reproduces the committed .out) | 20 s |

**Not done.**
- Analytic review of §§3.3–3.13: Proposition B's proof, the Rule C items, and the S1‴ heuristics are reviewer A's remit.
- Heat-trace fits (spec_bouncer_heat).
- Second-order (γ²) pole terms.
- The p = ¾ log-resonance at w = 4.
