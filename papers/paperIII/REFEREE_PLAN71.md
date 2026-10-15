# Paper III: Rule R review and editor pass (Plan 71)

Reviewer: an independent second reader (Rule R for the new arguments) and editor. Branch `plan-71-paperIII`, draft
commits bb76d25..945c6b5. Read: `main.tex`, `sec1`–`sec8.tex`, `NOTES.md`, `STYLE_CHECK.md`; AGENTS.md,
VERIFICATION_POLICY.md, `research/program/paper_style.md`, `papers_split/SERIES.md`, `PAPER_III_OUTLINE.md`.
Sources compared:
- research/G1/RH/second_order/TAIL.md and research/G1/review/REVIEW_Plan69.md, both on master (Plan 69 is REVIEWED and
  merged; the ja-plan69 worktree no longer exists);
- Paper I (`papers/paper1/main.tex`, Thm 1.1, Cor 1.2, Thm 1.3);
- the Paper II draft (`ja-plan70/papers/paperII`: Def 1.1, Thm 1.2, Cor 1.3, Thm 1.4, Rem 1.6, §3, Prop 8.6,
  Conj 11.1–11.2);
- `lean/JacobiAsym/Christoffel.lean` (`christoffel_shift_law_converse`) and `DiscreteMeasure.lean` (`DMeasure`);
- the stored outputs cited in NOTES.md §6.3.

## Overall verdict

**ACCEPT WITH (EDITORIAL) FIXES.** I re-derived all six new arguments independently, and each one is correct. I found
no critical or major issue. Every theorem is no stronger than its reviewed source. The imports from Papers I and II
are restated accurately. All quoted numbers match the stored outputs, except three wording points and one wrong
truncation range (fixed). The minor and editorial fixes listed in §D were applied. The build is clean (29 pp,
0 warnings, 0 over/underfull boxes); the introduction is pp. 1–4.

## A. Rule R on the six new arguments

### A1. Theorem 4.4 (a-law), cross-scale step without Lemma TL: **ACCEPT**
- **The remainder needs no tail lemma.** Lemma 2.16(iii) holds for an arbitrary base v and bounded φ. Its remainder
  (e^ε − 1 − ε)(b_n + b_{n+1})(v) is evaluated at the base only. This is because |ḃ_m| ≤ εb_m along the path, so
  b_m(t) ≤ e^{εt}b_m(0). Linearising along the direct path ve^{tφ} therefore needs no control of the perturbed
  measures, and no Lemma TL.
- **The windows are disjoint and the other windows lie in A_i.** I checked this with n_{i+1} ≥ (i+1)²M₀n_i and
  W_i = [n_i/M₀, in_i]. For j < i: (i−1)n_{i−1} ≤ (i−1)n_i/(i²M₀) < n_i/M₀. For j > i: n_{i+1}/M₀ ≥ (i+1)²n_i > in_i.
- **Off-window mass.** Lemma 2.14 gives n^p‖ΔE_n|_A‖₁ ≤ c(m_{n−1} + 2m_n + m_{n+1})(A) for large n, since
  ½n^p max(b_n, b_{n+1}) → c/2. The head goes by Corollary 2.19 (n′ ≥ n_i − 1 ≥ n_i/2). For the tail: for i ≥ M,
  (in_i, ∞) ⊂ (Mn_i, ∞), and Lemma 2.20 with shifts −1, 0, 1 applies. Hence limsup ω_i ≤ 4cT_p(M) for every M, so
  ω_i → 0.
- **Signs.** (−1)^i n^p⟨φ, ΔE_{n_i}⟩ ≥ ε(n^p‖ΔE|_{W_i}‖ − n^p‖ΔE|_{A_i}‖) ≥ ε(γ_a − 2ω_i). ✓
- **Constants.** ε ≤ 𝔦/16 ≤ 1/16 gives e^ε − 1 − ε ≤ ½ε²e^ε ≤ 0.54ε², so 2c(e^ε − 1 − ε) ≤ 0.0675cε𝔦 < εγ_a/2 = 0.25cε𝔦.
  The conclusion ≥ εγ_a/2 − o(1) follows, and the alternating signs give Theorem 1.3(ii). ✓
- **Lemma 4.3 (input).** I re-derived it:
  - both identities for ΔE_N and ΔE_{N+1};
  - the remainder bound |r_N| + |r′_N| ≤ δ_N(u² + u′²);
  - the homogeneity reduction to Υ (evenness under (u, u′) ↦ −(u, u′) justifies χ ∈ [0, π]);
  - Υ is 1-Lipschitz and vanishes exactly on Z, with minimisers χ = 0, π/4, 3π/4;
  - the limit of the pairing is 2𝔦.

### A2. Lemma 2.21 from the Chebyshev expansion: **ACCEPT**
- **The inequalities (2.12)** are for P real of degree ≤ n, with ‖P‖ the sup norm on [−1, 1].
  - c_j = ((2 − δ_{j0})/π)∫₀^π P(cos θ)cos jθ dθ, so |c_j| ≤ 2‖P‖.
  - |T_j′(cos θ)| = |j sin jθ/sin θ| ≤ j² on [−1, 1].
  - Σ_{j≤n} j² ≤ n³, so max_{[−1,1]}|P′| ≤ 2n³‖P‖ (the bound is on [−1, 1], for the sup norm on [−1, 1]).
  - For |y| ≥ 1, |T_j(y)| = cosh(j arccosh|y|) is non-decreasing in j, so |P(y)| ≤ 2(n+1)|T_n(y)|‖P‖.
  - Both bounds are correct, and weaker than Markov's n² and the Chebyshev extremal bound, as intended.
- **The downstream constants are all propagated correctly.**
  - x̲/x̄ ≤ n^{−2} ≤ ¼ (n ≥ 2).
  - The affine map gives |P′| ≤ 4n³‖P‖/(x̄ − x̲) ≤ 8n³‖P‖/x̄.
  - Atom gaps: x_j − x_{j+1} ≤ pj^{−p−1} ≤ px̄/T′.
  - T′ = ⌈16pn³⌉ gives the factor ½, so ‖P‖_{[x̲,x̄]} ≤ 2 max|P(x_j)|.
  - y ≤ 1 + 4n^{−2} on [0, x̲], and T_n(1+η) ≤ e^{n√(2η)} ≤ e^{√8} < 17.
  - This gives 34(n+1), then 68(n+1), the constant 68²(n+1)², and the bound T″ ≤ (16p + 2)n^{3+2/p}.
  - The integer-T tail form via Σ_{k>T}k^{−s} ≤ T^{1−s}/(s − 1) and m_{n′} ≤ K_{n′+1} ≤ K_{n+1} is also correct.
- **Rule C.** The polynomial inequalities are now proved in the text. The D5 caveat (Markov/Chebyshev not checked
  against a source) is therefore discharged for Paper III.

### A3. Lemma 2.22, ϑ_* = (s − 1)/(4 + (2 + 2/p)s): **ACCEPT**
- **Arithmetic.** B := 3 + (2 + 2/p)s, so ϑ_* = (s − 1)/(B + 1) and γ₁ = 1/ϑ_* = (B + 1)/(s − 1).
  - The deep-range bound is C·n²·n^{(3+2/p)s}·(Mn)^{1−s} = Cn^B M^{−(s−1)}.
  - Then n^B M^{−(s−1)} = n^B M^{−Bϑ_*}M^{−ϑ_*} ≤ M^{−ϑ_*} once M^{ϑ_*} ≥ n.
  - γ₁ > 2 + 2/p holds because 4 + (2+2/p)s > (2+2/p)(s−1). This gives T ≥ Mn/2 ≥ T″ for large n, since
    γ₁ + 1 > 3 + 2/p.
  - The middle range costs only C c₂^{−p/2}n^{−1} ≤ C c₂^{−p/2}M^{−ϑ_*}.
- **Positivity and size.** ϑ_* > 0. ϑ_* < s − 1 because the denominator exceeds 1. ϑ_* < p(s−1)/(2s) < p/2.
- **Monotonicity.** d/ds has the sign of (4 + βs) − β(s − 1) = 4 + β > 0, with β = 2 + 2/p.
- **Consistency with TAIL Cor TB-C.** TAIL's exponent (s − 1)/(s(1 + 2/p) + 2) is larger. The extra n²·n^s in Lemma 2.21's
  constant raises the denominator by s + 2. Only positivity, ϑ_* < min(p/2, s − 1) and monotonicity are used: in
  Proposition 6.3 (τ₀ ≤ p/4, τ₀ < t − 1), Lemma 6.4 (a′ < ½) and Theorem 6.5. ✓

### A4. φ′(0) = log c directly from the arcsine law: **ACCEPT**
- **The computation.** ∫log y d arc_{4c} = log 2c + (1/π)∫₀^π log(1 + cos θ)dθ. Here
  log(1 + cos θ) = 2log|1 + e^{iθ}| − log 2, and the mean of log|1 + e^{iθ}| over the circle is 0. So
  φ′(0) = log 2c − log 2 = log c. ✓
- **The dominated-convergence step** from r < 1 to r = 1 is correct. |1 + re^{iθ}|² ≥ r|1 + e^{iθ}|² because
  (1 − r)² ≥ 0.
- **What it buys.** Theorem 6.5 now holds on every compact K ⊂ S_p without the enlargement K″ (b″ ≥ a″ + p) of TAIL
  Thm TS(a). The remark after Theorem 6.5 (Φ_n(s+p) − Φ_n(s) = log(n^p u_n(s))) is a consistency check, which I
  verified from Proposition 5.2 and u₀ = ζ(s+p)/ζ(s).

### A5. Theorem 1.3(iii), "n^p b_n has no limit in [0, ∞]": **ACCEPT**
- The weights 2(n − j)/n² are non-negative, sum to (n − 1)/n, and each tends to 0. So the Toeplitz conditions hold, and
  the mean of log(j^p b_j) tends to log L also for L ∈ {0, ∞}. Corollary 1.2 of Paper I forces L = c.
- Then log(b_n²/b_{n−1}²) = log(β_n²/β_{n−1}²) − 2p log(n/(n−1)) → 0, which contradicts (i).
- Case (ii) follows trivially, since limsup − liminf ≥ εγ_a > 0.

### A6. The b-law (Theorem 4.2) via Lemma 2.16(ii) (2ε²) in place of R2 (8ε²): **ACCEPT**
- **Lemma 2.16(ii).** I re-derived it. α̇_m = Var − 2‖Proj_m(φq_m)‖² ∈ [−Var, Var], and
  F̈_N = α̇_N − 2α̇_{N−1} + α̇_{N−2}, so |F̈_N| ≤ 4ε². Taylor's formula then gives 2ε². The reduction to |φ| ≤ ε by
  centring is correct, because constants do not change the coefficients or the linear terms.
- **The constants.** With ε ≤ γ_W/16, the remainder is ≤ εγ_W/8. The cross-window term in case (B) is ≤ 4εT_p(M_W)
  ≤ εγ_W/4, using T_p(M_W) ≤ γ_W/16 (I checked the closed form). This gives 5/8 (case B) and 7/8 (case A). Both are at
  least the stated ¼ and ½, which are the source's constants with 8ε².
- **The proof did not say this.** It ended at 7/8 and 5/8 while the theorem states ½ and ¼. "In particular" was added
  (editorial).
- **Lemma 4.1.** I re-derived Steps 1–4: the bound 2/J + (J+1)γ/2 ≤ 2δ, the recurrence identity in Step 3, the bound
  8δ = ι_W/4, and the contradiction with ι_W/2.

## B. Other statements, imports and scope

- **Theorems 1.2, 1.3(i)(ii), 1.4, Corollaries 1.5 and 5.5, Propositions 5.1–5.6.** Each statement equals or is
  weaker than its source, and I checked the proofs line by line:
  - Prop 5.1: the δ³/16 bookkeeping and the bound 7ε.
  - Prop 5.2.
  - Prop 5.3.
  - Lemma 5.4.
  - Cor 5.5: the TC masses 2e·v_{j}, e_N = 1/(N+1), b^TC, ϖ = e^{R(k)}, and the Lommel expansion
    1 − 1/(2j) + O(j^{−2}).
  - Prop 5.6: the ε′ bookkeeping, and 2ε′ ≤ 1 + ε′.
  - §6: Lemma 6.2 (both bounds), Prop 6.3, Lemma 6.4 (the 6C bound holds with 4C), Thm 6.5 (the sum of the
    per-cell errors is exactly A₀r_τ(s − s̲)/p), Lemma 6.6, and the K₁/K₂ split.
- **Theorem 1.4(iii) for p ≤ 1 against REVIEW_Plan69 F2.** The paper states the uniform a-limit only for compact
  K ∌ 1 + p. The text after the proof says "we do not know whether the diagonal law is uniform near s = 1 + p", and §8
  repeats the restriction. **No overclaim.** It does not mention the uniform *boundedness* of n^p a_n on every window
  compact (TAIL GAP UP-1+p, F2). That claim is proved in TAIL, not in the paper; adding it would need the extension of
  Proposition 6.3 past 1 + 2p. Optional for the author (see O1).
- **Imports.** All restatements agree with the current sources:
  - Paper I: Thm 1.1/Cor 1.2 with f(ξ) = ξ^{−p}, C = 1; Thm 1.3(i) with u_s → u_sat.
  - Paper II: Def 1.1; Thm 1.2 (the equivalence remark is correct); Cor 1.3; Thm 1.4; Rem 1.6 coefficients; Thm 3.1;
    Lemmas 3.2–3.4; Prop 8.6(a)(b) with the range 1 ≤ M ≤ γ_* n^{2/p}, m ∈ {n−1, n}; Conj 11.1 and 11.2.
  - Paper II's numbering in the plan-70 draft matches today: one shared theorem counter, prop:tail = 8.6. Re-check it
    when II is frozen.
- **The Lean sentence (§5).** The formal hypotheses are DMeasure (positive, summable weights; bounded, strictly
  decreasing atoms), atoms ≥ 0, and a scale s_n > 0 with s_n/s_{n+1} → 1. The sentence now says this (editorial).
- **The abstract** matches the scope after Plan 69: uniform statements inside the window for p ≤ 1, and the diagonal
  away from one exponent.

## C. Numerics (§7, Remark 4.5, §8) against the stored outputs

All values were checked against the stored outputs:
- `research/G1/checks/check_rw.out` [1]–[3];
- `research/G1/checks/check_ra.out` [3]–[4];
- `research/G1/checks/check_sv_general.out` [1];
- `research/G1/checks/check_t3_conv.out`;
- `research/G1/RH/second_order/checks/check_so_shift.out` [A]–[D];
- `research/G1/RH/second_order/checks/check_ul.out` [4];
- `research/G1/RH/second_order/checks/check_so_validate.out`;
- `research/G1/RH/second_order/checks/check_so_convex.out`.

| Claim | Stored value | Status |
|---|---|---|
| ι_W ≈ 0.2345, J_W = 273, γ_W ≈ 9.8e−8, R_W ≈ 1.1e8 (p = 2); ι_W ≈ 0.127, γ_W ≈ 1.6e−8 (p = 1) | 0.23445, 273, 9.831e−8, 1.099e8; 0.12679, 1.554e−8 | ✓ |
| ε ≤ γ_W/16 ≈ 6e−9 | 6.144e−9 | ✓ |
| ‖Δ²m_m\|W_N‖₁ "about 1.06–1.09 for every m ∈ [N−7, N]" | only the *minimum* over m is stored: 1.061, 1.091, 1.094 | **fixed** (now "the minimum … is 1.06, 1.09, 1.09") |
| 𝔦 ≈ 0.314; response ≈ 0.8εc, about 10× εγ_a/2 | 0.3140; ‖n^pΔE‖/c = 0.77–0.87; ratio ≈ 11 | ✓ |
| Table 1 (all 18 entries), caption 0.026 / 0.103, "within 2%", "≤ 1.4e−3", "factor > 2", "doubling K < 1e−3" | match | ✓ |
| "over all other n ∈ [10, 246]" | the script excludes \|n − m_i\| ≤ 2 | **fixed** (text and caption) |
| Table 2 (all 20 entries) | match after rounding | ✓ |
| "K between 10⁵ and 3.2·10⁵" for Table 2 | K = 2·Kof(p) = 3.2·10⁵ (p ≥ 1), 6.4·10⁵ (p = ½) | **fixed** |
| sup_s deviation 2.25e−2 … 6.63e−3; b and a deviations at n = 400; grid 1.5:0.25:4, K = 4·10⁴ | match | ✓ |
| TC comparison 4.1e−4 (n = 100), 2.6e−5 (n = 1600) | 4.136e−4, 2.603e−5 | ✓ |
| Lommel reproduction < 1e−14, n ≤ 400 | 6.59e−15 (K = 4·10⁴) | ✓ |
| exp√log(k+e): 1.09e−3 … 5.6e−5; K-doubling agreement 2e−7; n·dev ≈ ½θ_n | match (0.49/θ_n) | ✓ |
| parity/log: 3.9e−3, 1.5e−3, 8.2e−4 at 250, 1000, 3600; K = 1.2e5 | match | ✓ |
| Conj 8.1 evidence: "exact determinants for n ≤ 8", "second differences of size about 1/(p²n)" | n ∈ {1, 2, 4, 8}, p ∈ {½, 1, 2}; the *divided* differences at n = 1600 are ≈ 1/(2p²n) | **fixed** (wording made exact) |

## D. Findings by severity, and what was applied

There are no critical or major findings, and no REJECT.

**Minor (applied).**
- **M1 (§6, notation clash).** The grid step was called u₀ (and u), while u₀ = a₀ is the first chain parameter of §5,
  and the proof of Thm 1.4(iii) in the same section uses u_n(s). *Fix:* the step is renamed τ₀, τ, r_τ throughout
  Prop 6.3 and Thm 6.5.
- **M2 (§8, inaccurate justification).** "A lower bound on Φ_n″ bounds Θ_n on K by its values at one point" is not
  right as stated. *Fix:* convexity makes Θ_n non-increasing on a slightly larger K′ ⊂ S_p. So on K, Θ_n lies between
  its averages over short intervals, which converge by Thm 6.5. I checked this argument.
- **M3 (§8, overclaim).** "Both restrictions … would disappear with a uniform version of the chain-limit statement" is
  not right for the diagonal restriction at s = 1 + p. A uniform chain limit near 1 + p would need the uniform a-law
  there (circular). TAIL only claims it for uniformity outside the window. *Fix:* "they would disappear with a version
  of [the tail bound] beyond S_p, and the first one also with a … chain-limit statement uniform in s".
- **M4 (§7, numerics wording).** Three fixes, as in the table of §C: the truncation K for Table 2, the off-spike index
  set, and the Δ² minimum.
- **M5 (§8, convexity evidence wording).** The exact parameter sets, and divided differences ≈ 1/(2p²n).
- **M6 (Remark 4.7, last sentence).** "Windows … saturated in the sense of Proposition 2.2 carry no spectral weight"
  mixed two notions. *Fix:* the sentence now says that in the variable u = k/N such windows lie in (0, u_sat], where
  ρ* = 1, and that the argument given shows they carry asymptotically no spectral weight.

**Editorial (applied).**
- **E1 (Thm 4.2 proof).** Added "in particular at least εγ_W/2 and εγ_W/4" to match the statement.
- **E2 (§2.2, after Prop 2.10).** "Uniformly in the form we use" (vague) is replaced by a precise sentence.
- **E3 (§5, Lean sentence).** It now states positive summable weights and a scale with consecutive ratios → 1.
- **E4 (§8).** Added the opening paragraph that the style guide requires (§8 opened with a run-in head).
- **E5 (Remark 8.2).** \tilde P_j is replaced by p_j: the orthonormal polynomials are p_j by §2.1, and the tilde
  denotes xσ in §5.
- **E6 (NOTES.md).** The Plan 69 status is updated to REVIEWED, and the Rule R and numerics items are marked done.

**Open, for the author (not applied).**
- **O1 (optional strengthening, F2).** One sentence could be added after the proof of Thm 1.4(iii): for p ≤ 1,
  n^p a_n(s) is bounded uniformly on every compact subset of (1, 1 + 2p). This is TAIL GAP UP-1+p, "uniform boundedness
  survives", and it is REVIEWED. It needs Prop 6.3 with base points in S_p and a last cell reaching up to τ₀ beyond
  1 + 2p, which takes 2–3 lines. Do not state the uniform *limit*.
- **O2 (cosmetic).** Run-in heads use \emph, which the style guide reserves for definitions. As in Papers I–II, decide
  this series-wide.
- **O3 (notation).** Some minor overloads remain, all confined to proofs or remarks:
  - c′ is the limit constant (Lemma 2.6, Thm 2.7, Prop 5.1) and also the lower sandwich constant in Lemma 2.21; C′ is
    fixed in Lemma 2.21 but "may change from line to line" per §1.4;
  - φ (direction) versus ϕ, ϕ_N (Lemma 4.1) and ϕ(r), ϕ_n (§6);
  - ε := δ³/16 inside the proof of Prop 5.1.
  Consider c₋, C₊ in Lemma 2.21 and another letter for §6's log-moment function.
- **O4 (§7).** The phrase "W_TC = 1 that the computation indicates" is weak. Σ_j j^{j−1}e^{−j}/j! = 1 is a classical
  identity (the Borel distribution, or the tree function at 1/e). Cite a read source, or keep the wording. W_TC enters
  only the constant C(3/2), never the exponent.
- **O5.** Re-check every [II, …] number when Paper II is frozen. Today they match the plan-70 draft.

## E. Part B: does it read like a carefully written paper?

Yes, largely.
- **The introduction (pp. 1–4)** states all main results by p. 3 with explicit hypotheses. Context is in prose, with
  precise citations and no hedging. The method paragraph is one paragraph, and the organisation takes 3 sentences.
- **Section openings** state what each section proves and why (§8 now too). The long proofs have strategy paragraphs:
  Lemma 3.2, the §4 mechanism, Lemma 4.1, the §6 opening. Remarks carry referee-relevant information (sharpness,
  necessity, constants).
- **The logical order** is §2 tools, then one choice of φ per section, and it is visible throughout.
- **Repo vocabulary.** None appears (I re-grepped: no Plan/REVIEWED/Law P/TL/QLP/G1/RH, no em-dash asides). "Indeed"
  occurs once.
- **Notation** is consistent with SERIES.md §4: σ_{p,s,ℓ}, m_n, K_n, u_n, l_n, arc_β, u_sat, T_p, Θ_n, Φ_n, and the
  pairing a_n/(2b_n). The only clash, the §6 grid step u₀, is fixed.
- **One residual tell.** Some paragraphs end on a restating sentence ("This is the case …"), but these are few.
- **Build.** pdflatex, bibtex, pdflatex ×2: 29 pages, no warnings, no overfull or underfull boxes, bibtex 0 warnings.
