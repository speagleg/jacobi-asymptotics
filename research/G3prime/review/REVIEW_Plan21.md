# Rule R review: Plan 21 (rhfree/RHPRIME.md: Theorem V⁺, Lemmas P1–P3, numerics)

Reviewer: independent Rule R referee (adversarial). Target: branch plan-21-prime-onesided, commit 754997a.

Read:
- AGENTS.md; RHPRIME.md (all); the plan doc docs/superpowers/plans/2026-10-14-plan-21-prime-onesided.md;
- RHFREE.md (Lemma PC, scaling of D(η_λ)); RHFREE2.md §4; PROOF.md §4 ((SG), G3′-L), §8.2 (Theorem C), §9 (Corollary P);
- CITATIONS.md (C3) and its addenda, (C6) addendum, (C8) and its Plan-20/Plan-21 addenda;
- checks/check_weighted_pc.py and check_weighted_pc.out.

Sources checked against the text extractions:
- Goldston arXiv:math/0412313. Prop. 1 (3.11)–(3.12), §4 (4.1)–(4.5), §8 (8.2)–(8.8), §9 (Theorem 7 and its proof,
  (9.4)–(9.9) and the full-range remark). Both raw and layout modes were used.
- BGST arXiv:2501.14545v3 §3: MT (3.2), (3.3)–(3.5) and their derivation.

Scratch (not in the repo): scratchpad/p21rev/npsi.py (smooth-density model of N_Ψ, with and without truncation at
γ_max). The 10-minute script was not re-run: the smooth model reproduces the .out's N_Ψ values to 4 digits (F6).

## Verdict: ACCEPT WITH FIXES

The argument is correct and I found no counterexample. Checked step by step:
- the pair form;
- the y-range bookkeeping of P1;
- the Stieltjes/dyadic analysis of P2;
- the weight removal in P3;
- the positivity count.

The normalizations all close. In particular (V⁺)'s constant ½ produces exactly G ≤ (1 + o(1))(T/2)log T = (1 + o(1))N_Ψ.

The fixes:
- (i) One error term in P2 is misstated. As written it is too weak to give the lemma; the true bound is fine (F1).
- (ii) Labelling of the dependence on (C8) (9.9), which is sketch-level in the only source read (F2, F8).
- (iii) Rule C: one transcription error in the CITATIONS quote of (9.7) (F3), plus small quote and bookkeeping items
  (F9).
- (iv) One overclaimed "equivalently" in the hypothesis framing (F4), and one implication worth stating explicitly
  (F5).
- (v) The N_Ψ numerics are dominated by truncation at γ_max (F6).

No major findings. Medium: F1, F2. Minor: F3–F9. Info: F10–F12.

## Checked and OK

### Pair form (§0), Review focus 1
- **Normalization.** With c = π·(Cauchy density), (2/π)∫_ℝ c(t − a)c(t − b)dt = (2/π)·π²·2/(π(4 + u²)) = w(u). This
  matches (4.1)–(4.2). ✔
- **G = R/(2xκ²).** The source (9.7) has RHS "(4xκ²/π)∫_0^∞ (sin(κt/2)/(κt/2))²|Σ_γ x^{iγ}/(1 + (t − γ)²)|² dt". So
  R = 2xκ²·(2/π)∫_0^∞ φ|S_x|² = 2xκ²G exactly. ✔
- **Ψ.** Ψ ∈ [0, 1], since 0 ≤ φ ≤ 1, c > 0 and ∫_0^∞ ≤ ∫_ℝ. Absolute convergence holds by Tonelli:
  Σ_{γ,γ′}(2/π)∫_0^∞ φcc = (2/π)∫_0^∞ φ(Σ_γ c(t − γ))² ≪ ∫ min(1, 4/(κt)²)log²(t + 2) < ∞. ✔
- **Σ_γ over all zeros.** This is consistent with the source:
  - (9.7) is obtained "Using (3.11) to express G_κ(t) in terms of a sum over zeros".
  - The Σ_γ of Prop. 1 (from Landau's explicit formula) is unrestricted.
  - §4 says: "we may restrict the sum to this range [0 < γ ≤ T] with a small error". That only makes sense if the
    original Σ_γ is unrestricted.
- **It does not matter.** For t ≥ 0, Σ_{γ<0}c(t − γ) ≪ log(t + 2)/(1 + t). Including or dropping negative ordinates
  changes G by O(log³T) = o(N_Ψ). ✔
- **Symmetry.** G(1/x) = G(x) and G ≥ 0. ✔

### Lemma P1, Review focus 2
- **Shape of (9.9).** The raw extraction of (9.7) reads "(Σ_{y<n≤y+y/T} … )² dy/y". With
  a_y(x)² = min(y/x, (x/y)³) ((3.12)), integration by parts gives:
  - ∫_1^x (y/x)dI/y = I(x)/x;
  - ∫_x^∞ (x/y)³dI/y = −I(x)/x + 4x³∫_x^∞ I/y⁵.

  The sum is exactly 4x³∫_x^∞ I(y, δ)dy/y⁵, which is the shape of (9.9). This confirms the measure dy/y (see F3) and
  the role of I(y, δ) = ∫_1^y.
- **Main term.** 4x³∫_x^∞ ½δy²log(1/δ)·y^{−5}dy = 2x³δ log T·(2x²)^{−1} = xδ log T. ✔ This matches the zero side:
  2xκ²·(T/2)log T = (x/T)log T(1 + O(1/T)) = xδ log T. So the GUE constant ½ in (V⁺) corresponds exactly to
  G ≤ (1 + o(1))N_Ψ. ✔
- **y-range.** Take x = T^α ∈ [T, T^M] and x ≤ y ≤ Y = T^{2M+1}. Then y ≥ T ⇔ δ = 1/T ≥ y^{−1}, and
  y ≤ T^{2M+1} ⇔ δ ≤ y^{−1/(2M+1)}. Also y ≥ T ≥ X₀(2M + 1, ε) for large T. ✔
  - Y = T^{2M} would already suffice, so 2M + 1 is harmless slack.
  - P1 uses (9.9) directly at δ = 1/T, so it never needs Theorem 7's (log x)^{±3} padding of the δ-range. ✔
- **Trivial tail.**
  - ψ(b) − ψ(a) ≤ (b − a + 1)log b holds, since there are at most b − a + 1 integers in (a, b] and Λ ≤ log b.
  - Hence I(y, δ) ≪ T log²T + δ²y³log²y ≪ δ²y³log²y for y ≥ T, since δ²y³ ≥ T.
  - The tail is 4x³∫_Y^∞ ≪ x³δ²log²Y/Y. Relative to xδ log T this is ≪ T^{2α−1}(2M+1)²log T/T^{2M+1} → 0. ✔
- **Upper I ⇒ upper L.** (9.9) is an identity with a two-sided error, and only the main term involves I. So an upper
  bound on I on [x, ∞) gives an upper bound on L. This needs no Tauberian step and no positivity beyond I ≥ 0. ✔
- **Error terms.** The full-range error x(log x)⁴/T^{3/2}, relative to x log T/T, is (log x)⁴/(T^{1/2}log T) → 0 for
  x ≤ T^M. The (9.7) error (log T)²/T, relative to the same, is log T/x → 0. ✔ The displayed (9.9) error alone gives
  α ≤ 2 − ε, as Remark V3 says. ✔

### Lemma P2, Review focus 3
- **H = F + O(log³).** H(t) = F(x, t) + O(log³t) follows from (4.4), whose Σ_γ is unrestricted. On RH,
  W(i(γ − γ′)) = 4/(4 + (γ − γ′)²) = w and x^{ρ−ρ′} = x^{i(γ−γ′)}, so BGST's F_{(0,t]}(x) (from (3.3)) is Goldston's
  (4.2) F(x, t).
- **(3.5).** BGST derive (3.5) "for 1 ≤ x ≤ T", and the error terms are uniform in x on that range. P2 applies it only
  with t ≥ x: on [x, ΛT], and at t = x for the low part. ✔
- **Low part.** 0 ≤ ∫_0^x φ dH ≤ H(x), with H(x) = F(x, x) + O(log³x) ≪ x log x. ✔ (See F12: this term is ≍ N_Ψ at
  α = 1. It is legitimately inside O(T^α log T).)
- **Dyadic variation of φ = sinc²(κt/2).**
  - For t ≤ T, |φ′| ≪ κ²t, so the variation on [U, 2U] is ≪ κ²U² and the sum is Σκ²U³√log U ≪ T√log T. ✔
  - For t > T, φ′ = 2sin(κt)/(κt²) − 8sin²(κt/2)/(κ²t³), so |φ′| ≪ 1/(κt²). The variation on [U, 2U] is
    ≪ 1/(κU) ≍ T/U, and each block contributes ≪ T√log U. There are O(log Λ) = O(log log T) blocks. ✔
  - The E-piece t log^{3/2}t/x² gives O((T log^{3/2}T/x²)log log T), which is o of the spike (T log²T)/(2x²). ✔
    The log³ piece contributes O(log³T). ✔
- **Truncation and tail.** φ ≤ 4/(κt)² and |S_x| ≪ log t give a tail ≪ T log²T/Λ = O(T) for Λ = log²T. ✔
- **Boundary terms.** [φE]_x^{ΛT} = O(x√log x + T√log T/Λ), plus a T log^{3/2}T/(Λx²) piece that the text omits and
  that is harmless (F1).
- **Main term.**
  - ∫_0^∞φ = π/κ;
  - ∫_0^∞φ log^k t = (π/κ)(log^k(1/κ) + O(log^{k−1}(1/κ))) for k = 1, 2, since ∫ sinc²u·log²u du < ∞.
  - The result is (T log²T/2x²)(1 + O(1/log T)) + (T/2)log x. ✔ (The quoted truncation error is wrong: F1.)
- **N_Ψ.** Write N_Ψ = ∫k(u)dN(u) with k(u) := (2/π)∫_0^∞φ(t)c(t − u)²dt, which is smooth. The remainder
  N(u) − smooth = O(log(|u| + 2)) contributes ∫|k′(u)|log(|u| + 2)du.
  - On [0, 1/κ]: ∫κ²u log u du ≪ log T.
  - On [1/κ, ∞): ∫log u/(κu²) ≪ log T.
  - For u < 0: O(1).

  So the remainder is O(log T), the main term is (T/2)log T(1 + O(1/log T)), and the variation of φ∗c² is bounded
  enough. ✔

### Lemma P3, Review focus 4
- **Weight removal.** At z = −(γ − γ′)L, π²z²/log²T = (γ − γ′)²/4, so r̂_T(z) = K(z)²/w(γ − γ′) exactly. Also
  e^{−2πiαz} = T^{iα(γ−γ′)}, since 2πL = log T. Fubini holds because Σ_{γ,γ′}Ψw < ∞ (above) and r_T ∈ C_c^∞. So
  S_Ψ = ∫r_T(α)G(T^α)dα. ✔
- **Q″ term.** By G ≥ 0, P1 and P2, ∫_{|α|≤2λ}G = O(N_Ψ), and this is divided by 4log²T. ✔
- **|α| ≤ 1.** The spike integrates to N_Ψ(Q(0) + o(1)), the α-term to 2N_Ψ∫_0^1αQ, and the O(T^α log T) term to
  O(T) = O(N_Ψ/log T). ✔ The P1 range M = 2λ needs (V⁺) at 4λ + 1. ✔
- **Bracket.** Q(0) + 2∫_0^1αQ + 2∫_1^{2λ}Q = 1 + D(η), as in RHFREE Lemma PC. ✔

### Theorem V⁺, Review focus 5
- **K lower bound.** K(u) = ∫η²cos(2πuv) ≥ 1 − 2π²λ²u². With λ = 1/(8πδ), |u| ≤ 2δ = 1/(4πλ) gives K ≥ 7/8 and
  K² = 49/64 ≥ ¾. ✔
- **Positivity count.** On RH every term ΨK² is ≥ 0. The diagonal, each multiset element with itself, gives exactly
  N_Ψ. Distinct copies of a repeated zero are distinct elements, so repeats (g_k = 0) are counted. ✔
- **Ψ ≥ 0.7.** κt/2 ≤ κT = T log(1 + 1/T) < 1 on [0, 2T], and sinc is decreasing on [0, π], so φ ≥ sin²1 = 0.70807…
  ✔
  - For γ ∈ (T/R, T] and |γ − γ′| ≤ 1, the normalized density c(t − γ)c(t − γ′)/((π/2)w), with w ≥ 4/5, has mass
    O_R(T^{−3}) outside [0, 2T].
  - Consecutive pairs with g_k < δ have γ_{k+1} − γ_k < 2δ/L → 0, so |γ − γ′| ≤ 1 holds. ✔
- **Constants.** (1/0.7)(4/3) = 1.905 ≤ 1.91. D(η_λ) ≤ ‖Q₁″‖_∞(8πδ)³/12. N_Ψ = (π + o(1))N(T) follows from
  (T/2)log T against (T/2π)log T. ✔
- **Normalization and conclusion.** The normalization step is as in Theorem C: log(γ_k/2π)/(2πL) → 1 uniformly on
  (T/R, T]. Then (SG), with R = 3/η and Cδ³ ≤ η/3, followed by G3′-L and G3′-U. ✔

### Framing, Review focus 6
- **(V⁺) is genuinely one-sided.** For each tolerance it is used only on a bounded range: η ↦ δ ≍ η^{1/3}, λ ≍ η^{−1/3},
  and (V⁺) at M′ = 4λ + 1 ≍ η^{−1/3}. ✔
- **RH.** RH is used only as a labelled hypothesis (§0, table, V2), and no claim about RH is made (AGENTS rule 3). ✔
- **Numerics.** The S_Ψ/N_Ψ values and the "0.4–1.4%" claim match the .out:
  - 1.6844/1.7067 = 0.987;
  - 1.1401/1.1560 = 0.986;
  - 1.0197/1.0238 = 0.996. ✔

## Findings

**F1 (MEDIUM, §2 Lemma P2, "Main" bullet).**
- **Issue.** The truncation error "O(x log²T + T log²T/Λ)" is wrong as written, and it is too weak.
  - At α near 1, x log²T ≍ T log²T ≫ N_Ψ.
  - Integrated, ∫_0^1 T^α log²T dα ≍ T log T ≍ N_Ψ. That would destroy the o(N_Ψ) in Lemma P3, and it contradicts the
    lemma's own O(T^α log T).
- **Correct bound.** ∫_0^x(log²t + 2 log t)dt = x log²x exactly. So
  |∫_0^x φM′| ≤ log²x/(2πx) + (x log x)/2π + O(1) = O(T^α log T + 1).
- **Fix.** Replace the term by "O(x log x + 1) + O(T log²T/Λ)". Also add the omitted T log^{3/2}T/(Λx²) to the ΛT
  boundary term. It is harmless: o of the spike.

**F2 (MEDIUM, labels of P1 and Theorem V⁺; Remark V3).**
- **Issue.** The dependence on (9.9) is sketch-level. Two quotes show this:
  - Goldston writes "All the details may be found in [18] **except how L(x, T) is related to I(X, δ)**, since the proof
    there proceeds from (2.14) rather than Proposition 1".
  - Both the displayed (9.9) ("one finds that") and the full-range error are only sketched in the notes, which are the
    only source read.
  So P1 rests on an unproved-in-any-read-source step. The file says this for the full-range error. It should also be
  visible that (9.9) itself is a sketched derivation, not a proved statement.
- **Fix.**
  - In the table and in P1's Inputs, write "(C8) (9.9) and its full-range error: stated with sketch in (C8); the
    L–I relation is not in [18] per (C8)", and quote that sentence.
  - Carry this into Theorem V⁺'s row (F8).
- **Optional upgrade.** A self-contained proof of the full-range error looks routine.
  - Replacing a_n(x) by a_y(x) on (y, y + y/T] changes the weight by a_y·O(1/T).
  - Using ψ(v) = v + O(√v log²v) (RH) and Stieltjes integration, the difference term B satisfies
    ∫B²dy/y ≪ x log⁴x/T².
  - Cauchy–Schwarz then gives an error ≪ x(log x)^{5/2}(log T)^{1/2}/T^{3/2}. This is o(xδ log T) for all x ≤ T^M.
  - But the subtracted expected-value term in (9.7) ("x∫_{xe^{−κ}}^{x} a_v(y) dv/v" in the extraction) is garbled in
    the text layer, so pin it down from the PDF before attempting this.

**F3 (MINOR, Rule C, CITATIONS (C8) Plan-21 addendum, the (9.7) quote).**
- **Issue.** The quote reads "|Σ… − x∫…|² dy/y²", but the source has "( … )² dy/y". The ² is the square, and the
  measure is dy/y.
- **Evidence.** The raw extraction reads "… av(y) dv v 2 dy y". Only dy/y reproduces (9.9)'s 4x³∫_x^∞ I dy/y⁵ (see
  "Checked" above). With dy/y² the main term would scale like δ log T, not xδ log T.
- **Fix.** Correct the quote. Use round brackets as in the source, or say "|·|²" is the author's rendering.

**F4 (MINOR, §0, second bullet under (V⁺)).**
- **Issue.** "Equivalently, by (C8), upper bounds of the shape of (9.3) for 1 ≤ h ≤ X^{1−1/M}" is an overclaim.
  - (C8) states only an *asymptotic* equivalence on RH: SPC ⇔ (9.3), via Saffari–Vaughan, and this is itself only
    stated.
  - Nothing in (C8) asserts a one-sided equivalence between the δ-form and the h-form.
- **Fix.** Write instead: "A one-sided h-form analogue is plausible via Saffari–Vaughan but is not stated in (C8);
  not used."

**F5 (MINOR, Remark V1).**
- **Issue.** "Weakened relative to Corollary P" should be shown as an implication.
- **Fix.** Add the explicit chain:
  - RH + (V) ⇒ SPC: Corollary P step 1, which uses the secondary h ↔ δ step.
  - RH + SPC ⇒ (V⁺) for each M: Theorem 7 (first direction) with B₁ = 1/M and B₂ = 1. Its zero-side range
    X^{1/M}(log X)^{−3} ≤ T ≤ X(log X)³ reaches α slightly below 1, where MT gives
    F = (T/2π)log T(1 + o(1)) anyway, and slightly above M, which is covered by SPC on [1, M + 1].
  - So Corollary P's input implies Theorem V⁺'s, and (V⁺) is implied by RH + SPC directly.

**F6 (MINOR, §5 Numerics, the N_Ψ against πN(T) bullet).**
- **Issue.** The ratios 1.18 / 1.13 / 1.09 are mainly a truncation artefact. φ has a ∝ T²/t² tail, and about 70% of
  its mass lies at t > T. The sample stops at γ_max = 1.13·10⁶, where the .out itself prints φ(γ_max) = 1.1·10⁻².
- **Evidence.** A smooth-density model (scratch npsi.py: ∫φ dN with N′ = log(t/2π)/2π) gives the following.
  - Truncated at γ_max it reproduces the .out to 4 digits: 1.1805 / 1.1331 / 1.0858.
  - Untruncated it gives 1.2014 / 1.1783 / 1.1640, and 1.107 at T = 10⁷.
  So the sample misses about 2%, 4% and 7% of N_Ψ. The steep downward trend is not evidence for the 1 + O(1/log T)
  rate; the untruncated decline is.
- **Fix.**
  - State the truncation and the missing fraction, or add a smooth tail correction for t > γ_max.
  - Note that S_Ψ/N_Ψ is also computed on the truncated sample. The ratio is only mildly affected.
  - Minor: the script uses κ = 1/T rather than log(1 + 1/T), which is negligible. It also approximates
    Ψ ≈ φ((γ + γ′)/2), as stated.

**F7 (MINOR, §2, the H = F + O(log³) step).**
- **Issue.** (4.4) is stated at a fixed x. P2 uses it uniformly in x and with T → t variable.
- **Fix.** Add one line: uniformity in x is implicit in the derivation, since |x^{iγ}| = 1 and the restriction and
  extension errors are bounded by absolute values via (2.18). Write O(log³(t + 2)) so that small t is covered.

**F8 (MINOR, table row for Theorem V⁺).**
- **Fix.** List "(C8) (9.9) full-range error (sketch)" among the mod-cites, as V3 already says ("mod-cite on the
  full-range claim"). Then the row cannot be read as resting only on proved inputs.

**F9 (MINOR, Rule C and bookkeeping).**
- §0's quote of (4.1)–(4.2) drops the integral limits ∫_{−∞}^{∞} that appear in the source. Restore them.
- In CITATIONS, "Used in" should add rhfree/RHPRIME.md:
  - (C3) Plan-20 addendum (3.5): Lemma P2;
  - (C6) addendum §3 algebra: Lemma P3;
  - (C1): P2 and Theorem V⁺.
- The PROOF.md §8.3 status row and LOG entry are pending under T7.

**F10 (INFO, Remark V4, novelty).** Keep novelty UNCHECKED. As related prior art in a read source, mention (C8) §8:
Heath-Brown's results (8.3)–(8.4) pass a *one-sided* zero-side hypothesis ((8.2) F(α) ≪ 1) to primes through the same
R(x, T): "assuming (8.2), R(x, T) ≪ (x/T)log T". That is the reverse direction of the one-sided mechanism used here.

**F11 (INFO, §0, last bullet under (V⁺)).** "Theorem 7 of (C8) relates (9.1) on such ranges to SPC on α ∈ [1, M]".
Theorem 7's δ-ranges carry (log x)^{±3} paddings, so "on slightly larger ranges" is more accurate. P1 does not need
Theorem 7 at all (see Checked).

**F12 (INFO, Lemma P2 statement).** Pointwise, the O(T^α log T) error is not o(N_Ψ) near α = 1. The low part
∫_0^x φ dH is ≍ (T/2π)log T there. Only the integrated form is used, in P3 and in the Q″ term, and that is fine. Add a
half-sentence saying so.

## Recommended labels (after F1–F9; re-check required before REVIEWED)
- (V⁺): HYPOTHESIS (with RH). It is implied by RH + SPC (F5), and hence by Corollary P's input.
- Lemma P1: PROVED-mod-cite ((C8) (9.7)–(9.9), where (9.9) and its full-range error are sketched in (C8) and the
  L–I relation is not in [18]) + mod-input RH, (V⁺).
- Lemma P2: PROVED-mod-cite ((C8) (4.2)–(4.4), (C3) (3.5), (C1)) + mod-input RH.
- Lemma P3: PROVED-mod-cite ((C6) §3 algebra, via P1 and P2) + mod-input RH, (V⁺).
- Theorem V⁺: PROVED-mod-cite (P1–P3, including the sketched (9.9) full-range error; (C1)) + mod-input RH, (V⁺),
  Theorem H. Novelty: UNCHECKED.
- §5: NUMERICAL, with the truncation caveat (F6).

## Re-check (commit a02aa4d)

Diff 754997a..a02aa4d read in full: RHPRIME.md, CITATIONS.md, LOG.md. Each finding was checked against the fix.

| Finding | Status | Note |
|---|---|---|
| F1 | RESOLVED | Main error is now O(x log x + 1 + T log x/Λ), with the exact ∫_0^x(log²t + 2 log t) = x log²x stated. The ΛT tail and boundary also produce T log²T/(Λx²). That piece is not in the new O-term, but it is (spike)/Λ, so it lies inside the spike's (1 + o(1)) (nit R2). |
| F2 | RESOLVED, with residual R1 | The P1 and Theorem V⁺ rows name the sketch dependence, and V5 records the self-contained proof as OPEN. |
| F3 | RESOLVED | The (9.7) quote reads dy/y. (Source brackets are round; the |·|² rendering is acceptable.) |
| F4, F11 | RESOLVED | The "Equivalently" claim is removed. "Slightly larger (log-padded) ranges" is added. |
| F5 | RESOLVED | V1 shows RH + (V) ⇒ SPC ⇒ (V⁺) via Theorem 7 forward with B₁ = 1/M, B₂ = 1. Nit R3: RH + (V) ⇒ SPC also uses the secondary Saffari–Vaughan h ↔ δ step, as in Corollary P step 1. Saying "as used in Corollary P" covers this implicitly. |
| F6 | RESOLVED | The truncation caveat is added, with the 2/4/7% figures and the statement that the trend is not evidence. |
| F7 | RESOLVED | A uniformity line for (4.4) is added. Cosmetic: "Let Λ := log²T. Then" is now at the end of the F7 bullet. Move it back after the bullets. |
| F8 | RESOLVED | |
| F9 | RESOLVED | The ∫_{−∞}^{∞} limits are restored. The "Used in" additions for (C3), (C6) and (C1) are collected under the (C8) Plan-21 addendum, not under each entry. That is acceptable. The PROOF.md status row is still pending (T7), to be done at promotion. |
| F10 | RESOLVED | V4 cites (C8) §8 Heath-Brown. |
| F12 | RESOLVED | |

**Residuals.**
- **R1 (Rule C; one line; required before REVIEWED).** The new labels assert that "the L ↔ I step is not covered by
  [18]". That sentence is a claim from the source, but it is quoted nowhere: neither in RHPRIME P1's Inputs nor in
  CITATIONS (C8) Plan-21. Add the verbatim quote (Goldston §9): "All the details may be found in [18] except how
  L(x, T) is related to I(X, δ), since the proof there proceeds from (2.14) rather than Proposition 1."
- **R2, R3 (nits).** Optional; see the table.

**Re-check verdict: ACCEPT** (once R1 is applied; R2, R3 and the F7 cosmetic are optional).

**Final labels.**
- (V⁺): HYPOTHESIS (with RH), implied by RH + SPC and hence by Corollary P's input.
- Lemma P1: PROVED-mod-cite ((C8) (9.7)–(9.9); (9.9) and its full-range error are sketched in (C8), and the L ↔ I step
  is not in [18]) + mod-input RH, (V⁺). REVIEWED.
- Lemma P2: PROVED-mod-cite ((C8) (4.2)–(4.4), (C3) (3.5), (C1)) + mod-input RH. REVIEWED.
- Lemma P3: PROVED-mod-cite ((C6) §3 algebra) + mod-input RH, (V⁺). REVIEWED.
- Theorem V⁺: PROVED-mod-cite (P1–P3, including the sketched full-range (9.9); (C1)) + mod-input RH, (V⁺), Theorem H.
  Novelty UNCHECKED. REVIEWED.
- V5 (self-contained (9.9)): OPEN. §5: NUMERICAL (with the truncation caveat).
