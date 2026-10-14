# Rule R review: Plan 20 (rhfree/RHFREE2.md: Theorem S′, Lemma N, Proposition Q, §4 obstruction, numerics)

Reviewer: independent Rule R referee (adversarial). Target: branch plan-20-rhfree-open, commit 1f13931.
Read: AGENTS.md; RHFREE2.md (all); RHFREE.md (REVIEWED; Lemma PC, Lemma G, Theorem S); REVIEW_Plan19.md; plan doc
docs/superpowers/plans/2026-10-14-plan-20-rhfree-open.md; CITATIONS.md (C3), (C6) addendum, (C8); PROOF.md §4 (SG).
Sources checked against the text extractions: BGST arXiv:2501.14545v3 §3 (statement of MT, (3.1)–(3.5), Lemma 1
(3.6)–(3.7) and the remark after it); Goldston arXiv:math/0412313 §4 ((4.2)–(4.4)) and §9 (Theorem 7 and its proof,
(9.4)–(9.9)).
Scratch checks (not part of the repo): scratchpad/p20rev/pos.py, lemN.py, lemN2.py.

## Verdict: ACCEPT WITH FIXES

The mathematics of Theorem S′, Lemma N and Proposition Q is correct as stated. I found no counterexample and no
gap that changes a conclusion. The fixes are about (i) how the full-window positivity is sourced (the review-focus
question; the claim is true, and it can be made self-contained), (ii) Rule C bookkeeping (no CITATIONS addenda for the
new quotes; one misattributed Goldston quote), (iii) the §4 "C > 1" assertion, which is the author's analysis of a
method and not something the source says, and must be framed as a heuristic, and (iv) labels/novelty/framing.

No major findings. Minor: F1–F7. Nits: F8–F12.

## Checked and OK

### Theorem S′ / Lemma PC′
- **(3.5) quote.** Verbatim against BGST §3: "(3.5) … = T log²T/2πx² (1 + O(1/√log T)) + (T/2π) log x + O(T√log T)",
  derived "for 1 ≤ x ≤ T", followed by "Thus we have obtained MT for F_{(0,T]}(x)." The O-constants are uniform in
  1 ≤ x ≤ T (the derivation bounds M1, M2, M3 and the cross term uniformly on that range, as in (3.2)). Same shape and
  same error terms as (3.2), so Lemma PC's Steps 1–5 go through verbatim with Z(T) → {0 < γ ≤ T},
  N_T → N(T) = (T/2π)log T(1 + O(1/log T)). Step 3's expansion of 𝓕 is identical. ✔
- **Positivity of F_{(0,T]}.** The quoted remark is attached to Lemma 1 (both (3.6) and (3.7), stated for (T, 2T]):
  "This was proved unconditionally as Lemma 3 in [BGSTB24] with the sum over terms with 0 < γ ≤ T. That proof works line
  by line for both (3.6) and (3.7)." So it asserts that [BGSTB24] Lemma 3 is the (0, T] form of Lemma 1. Taking the
  (3.6) form gives F_{(0,T]} = (2/π)∫|…|² ≥ 0. This is a legitimate reading, but it rests on [BGSTB24] Lemma 3, which
  has not been read (second-hand). Two stronger supports exist in the same section (see F1):
  - BGST's MT is stated as "For x ≥ 1 and T ≥ 3, we have F(x, T) ≥ 0, F(x, T) = F(1/x, T), and (3.2)", and "The
    statement above has been modified from its original formulation in [BGSTB24], with two changes. First, … in
    [BGSTB24] the sums are taken over zeros satisfying 0 < γ, γ′ ≤ T. Secondly, … the error terms". The positivity and
    evenness clauses are not among the changes. Also "Thus we have obtained MT for F_{(0,T]}(x)" names MT, which
    includes "F ≥ 0".
  - It is elementary and window-free. For ζ, ζ′ with |Re ζ|, |Re ζ′| < 1, (2/π)∫_ℝ g_ζ(t) conj g_ζ′(t) dt =
    4/(4 − (ζ + ζ̄′)²) with g_ζ(t) := 1/(1 − (ζ − it)²) (residues). I verified this numerically, max error 9·10⁻¹⁵ over
    20 random pairs (pos.py). Then for any finite multiset of zeros invariant under ρ ↦ 1 − ρ̄ (true for every γ-window),
    Σ_{ρ,ρ′} x^{ρ−ρ′}W(ρ − ρ′) = (2/π)∫|Σ_ρ x^{ρ−½}g_{ρ−½}(t)|²dt ≥ 0 after reindexing ρ′ ↦ 1 − ρ̄′. I checked
    positivity directly on 300 random symmetric multisets with off-line pairs (min F = 2.41 > 0, imaginary part 0).
  Verdict on the review-focus question: positivity is legitimately available; the write-up should source it better.
- **Evenness.** Swap ρ ↔ ρ′; W is even. ✔
- **On RH, F_{(0,T]} = Montgomery's F.** With β = β′ = ½, ρ − ρ′ = i(γ − γ′), W(i(γ − γ′)) = 4/(4 + (γ − γ′)²) = w.
  This matches BGST's display of Montgomery's F, "Σ_{0<γ,γ′≤T} x^{i(γ−γ′)}w(γ − γ′), w(u) := 4/(4 + u²)", and Goldston
  (4.2). Both count with multiplicity (multiset). ✔
- **Normalization.** Montgomery/Goldston normalize by (T/2π)log T ((4.9): "F(α) = … (T/2π log T)^{−1}…"), the
  hypothesis by N(T). Since N(T)/((T/2π)log T) → 1, "limsup sup_{[1,M]} ≤ 1" is the same statement for both. So, on RH,
  SPC_ℂ⁺(full) is exactly "F(α) ≤ 1 + o(1) uniformly on [1, M] for each M", the upper half of (C8)'s SPC ("For any fixed
  bounded M, F(α) = 1 + o(1), for 1 ≤ α ≤ M"). ✔ (Say so in one line; F9.)
- **Single window for (SG).** Z := {i(ρ − ½)L : 0 < γ ≤ T} is conjugation-invariant (ρ ↦ 1 − ρ̄). Lemma G at gap 2δ,
  λ = 1/(8πδ): ≤ 4(4E + N_d − N₁) ≤ 20D·N + o(N); non-simple-critical endpoints ≤ 2(N − N₁) ≤ 2DN + o(N).
  Normalization: for γ_k ∈ (T/R, T] (k ≤ N(T), so γ_k ≤ T), log(γ_k/2π)/2π ≥ L(1 − log R/log T − O(1/log T)) ≥ L/2 for
  large T, so g_k < δ ⇒ (γ_{k+1} − γ_k)L < 2δ. Pairs consecutive in the full list and simple-critical at both ends are
  consecutive in the sublist. The last index (γ_{k+1} > T) is O(1). Indices with γ_k ≤ T/R are ≤ (1/R + o(1))N(T).
  D(η_λ) ≤ ‖Q₁″‖_∞/(12λ³) = ‖Q₁″‖_∞(8πδ)³/12. With R = 3/η and δ small, 22D + 1/R ≤ η, which is (SG) as in PROOF.md §4
  ("#{k ≤ K : g_k < δ} ≤ ηK for all K ≥ K₀"; take T = γ_K). No dyadic summation needed. ✔
- **Remark S′1.** M = 2λ = 1/(4πδ) ≍ η^{−1/3}. ✔

### Lemma N
- V: ℝ^{N_d} → W, e_i ↦ (f_x, g_z, h_z)_i, is onto W by definition and injective by Lemma G Step 1, so bijective. In an
  orthonormal basis of W the matrix of A|_W is M J Mᵀ with M invertible: a congruence, so Sylvester applies. J has
  exactly one negative entry −2m_z per distinct z with Im z > 0, so k negative eigenvalues. ✔
- dim V = #(distinct real) + k = N_d − k, so dim(W ⊖ V) = k. ✔
- tr(PAP) = Σ_j⟨A e_j, e_j⟩ over an orthonormal basis of W ⊖ V; ⟨e, f_x⟩ = ⟨e, g_z⟩ = 0, so ⟨Ae, e⟩ =
  −2Σ m_z⟨e, h_z⟩², and Σ_j⟨e_j, h_z⟩² = ‖P h_z‖² = dist(h_z, V)² since h_z ∈ W. ✔
- Ky Fan: Σ (k smallest eigenvalues) = min over k-dimensional U of tr(P_U A P_U) ≤ tr(PAP). Direction correct. The k
  smallest are the k negative ones. ✔
- (1 + |μ|)² ≥ 1 + 2|μ|; positive eigenvalues contribute ≥ 0. E ≥ k + 4Σ m_z d_z². ✔
- **Numerical break attempt** (lemN.py, lemN2.py): random conjugation-invariant multisets, multiplicities 1–2,
  λ ∈ {½, 1, 2, 4}, up to 5 off-line pairs, Im up to 1.0, grid quadrature. On the 394 trials with cond(basis) < 10⁹:
  E (from S) = Σ(μ − 1)² to 10⁻¹⁴ relative; the Ky Fan inequality Σ_{μ<0}|μ| ≥ 2Σ m_z d_z² and the final bound
  E ≥ k + 4Σ m_z d_z² hold in all 394; the ratio (2Σ m d²)/Σ|μ_−| reaches 0.99999999, so the Ky Fan step is essentially
  sharp in some configurations. The negative-eigenvalue count equals k in 391/394. The 3 exceptions have
  ‖A‖ ≈ 10¹⁶·⁵, where eigvalsh's absolute error ≈ ε‖A‖ ≈ 10 exceeds the small eigenvalues: a roundoff artifact, not a
  counterexample. Ill-conditioned trials (cond ≈ 10¹⁵–10¹⁷, λ = ½ dense) give spurious counts for the same reason.
  No counterexample.

### Proposition Q
- z = i(ρ − ½)L = −γL + i(β − ½)L; Im z > 0 picks β > ½, y = β − ½. ‖f_z‖² = K(z − z̄) = K(2iyL), ‖f_z̄‖² = K(−2iyL)
  = K(2iyL) (K even), ⟨f_z, f_z̄⟩ = K(0) = 1. Hence ‖h_z‖² = (2K − 2)/4 = (K(2iyL) − 1)/2, and ⟨g_z, h_z⟩ =
  (i/4)(K − 1 + 1 − K) = 0. Consistent with (C6) (2.11) "1 = ∫|g_z|² − ∫|h_z|²". ✔
- K(2iyL) = ∫η²e^{4πuyL}du ≥ e^{2πλyL}∫_{u≥λ/2}η_λ² = κ₁T^{λy} (since 2πL = log T). Needs κ₁ > 0 (F8). ✔
- Contradiction: E ≥ 4m_z d_z² ≥ 4c²‖h_z‖² ≥ 2c²(κ₁T^{λ_j c₀} − 1), and E ≤ S − N ≤ D N_T + o(N_T) by Lemma PC with
  η_{λ_j} fixed. λ_j c₀ > 1 already suffices (> 2 is fine). ✔
- Strength of conclusion: for each c₀, eventually no zero in (T, 2T] with |β − ½| ≥ c₀. Correctly not called RH. ✔
- (NA) is stated as a HYPOTHESIS and labelled as such in the table and in "Status of (NA)". ✔
- **Numerical claims vs .out.** All match: λ = ¼ all 0.000; λ = ½ GUE 0.003–0.309, Poisson 0.000–0.011; λ ∈ {2, 4},
  y ≥ 0.1: min 0.526 (Poisson λ = 2, y = 0.1) → "0.53", max 1.000; 5 extra off-line g_w at λ = 2: 0.942, 0.993, 0.969
  → "≥ 0.94"; Poisson λ = 1, y = 0.3: 0.001 → "dip to 0.001"; n = 120. Rerun reproducibility: see the end.

### §4
- Goldston quotes checked: (9.9) "L(x, T) = 4x³∫_x^∞ I(y, δ)dy/y⁵ + O(…)"; (9.7)–(9.8) "L(x, T) = R(x, T)" with
  R = (4xκ²/π)∫_0^∞(sin(κt/2)/(κt/2))²|Σ_γ x^{iγ}/(1 + (t − γ)²)|²dt (Fejér weight in t ✔); "R(x, T) can be related to
  F(x, T) through Abelian and Tauberian theorems" ✔ verbatim. One quote is misattributed (F4).
- The C − 1 computation: Step 4 of Lemma PC with 𝓕 ≤ C on [1, 2λ] gives S/N ≤ 1 + D + 2(C − 1)∫_1^{2λ}Q_λ + o(1);
  ∫_1^{2λ}Q_λ = ∫_{1/λ}^2 Q₁ → ∫_0^2 Q₁ = ½. So E/N and (N − N₁)/N are ≤ D + (C − 1) + o(1), and Lemma G's bound is
  ≈ 20(C − 1)N (22(C − 1)N with the non-simple endpoints). It does not tend to 0 as δ → 0. ✔ (nit F11.)

## Findings

**F1 (minor; RHFREE2 §1 Inputs, "Positivity" bullet and "Hence F_{(0,T]}(x) ≥ 0"; Lemma PC′ third bullet "the
full-window form of (3.6)").**
Issue: the only support given is the remark after Lemma 1, which points to [BGSTB24] Lemma 3 (not read). It is a
legitimate but second-hand reading. The doc also never displays the full-window identity it calls "the full-window
form of (3.6)".
Fix: (a) also quote the MT header ("For x ≥ 1 and T ≥ 3, we have F(x, T) ≥ 0, F(x, T) = F(1/x, T), and") and the
"modified … with two changes … 0 < γ, γ′ ≤ T … error terms" sentence. Positivity and evenness for the full window are
in the original statement, and "Thus we have obtained MT for F_{(0,T]}(x)" invokes MT. (b) Preferably make positivity
self-contained, as Plan 19 F3 did for Lemma G: prove (2/π)∫g_ζ conj g_ζ′ = W(ζ + ζ̄′) by residues and reindex
ρ′ ↦ 1 − ρ̄′. This holds for any γ-window and needs no citation. (My numerical check: pos.py, error 9·10⁻¹⁵.) Then the
label can drop "Lemma-1 remark" from mod-cite.

**F2 (minor; CITATIONS.md (C3) and (C8); Rule C, AGENTS rule 4; precedent Plan 19 F4).**
Issue: the commit adds no CITATIONS addenda. New quotes used: BGST (3.4)–(3.5) and "Thus we have obtained MT for
F_{(0,T]}(x)", the Lemma 1 remark, and (per F1) the MT header. From Goldston: (4.4), (9.7)–(9.9), "through Abelian and
Tauberian theorems", "All the details may be found in [18]".
Fix: add a "Plan 20 addendum" to (C3) and to (C8) with these verbatim quotes and "Used in: RHFREE2 §1 / §4". State
that [BGSTB24] and Goldston–Montgomery [18] were **not read**.

**F3 (minor; RHFREE2 §4 item 3 and "Why a constant C > 1 is useless"; table row §4).**
Issue: "With only an upper bound on R, a Tauberian step … gives F(x, T′) ≤ C·(main term). Here C > 1 is a fixed
constant from the shape of the Fejér kernel" is asserted as fact. The source says nothing about one-sided versions:
it only says "through Abelian and Tauberian theorems" and defers "All the details" to [18], which was not read. The
claim is the author's analysis of one argument. That analysis is plausible. With only nonnegative combinations of
dilated Fejér kernels available as majorants of 1_{[0,T]}, a single kernel gives C = min_s πs/(4 sin²(s/2)) ≈ 2.17
(at tan(s/2) = s, s ≈ 2.33) for a linear main term. Karamata-type sharpness needs majorants with negative coefficients,
hence two-sided information. But "C → 1 is impossible from one-sided data" has not been proved: one-sided bounds hold
for all κ and all x in a range simultaneously, and that extra data was not exploited.
Fix: label item 3 HEURISTIC ("the natural one-sided Tauberian argument yields only a constant C > 1; we do not prove
that no one-sided argument gives C → 1"). Mark the C > 1 assertion as not from (C8). The §4 table label
"OBSTRUCTION identified; OPEN" should read "OBSTRUCTION (heuristic, for the Theorem 7 route); OPEN".

**F4 (minor; RHFREE2 §4 item 1; Rule C accuracy).**
Issue: "Upper I ⇒ upper L (immediate)" is supported with the quote "Since the integrand is non-negative …". In
Goldston that sentence justifies the *other* direction ("if we have an asymptotic formula for L(x, T) then a simple
differencing argument will give an asymptotic formula for I(x, δ)"). The I ⇒ L direction is "The converse is
immediate."
Fix: quote "The converse is immediate." for item 1. The upper-bound version follows because the weight 4x³/y⁵ is
positive. Also note the range caveat: the stated error in (9.9) is smaller than the main term only for
"T ≤ x ≤ T^{2−ε}", and the full range needs the refined error obtained "using Stieltjes integration and the PNT with the RH error" (quote the refined O-term from the PDF; the text extraction is garbled there).

**F5 (minor; RHFREE2 §2 "Status of (NA)" and the (NA) statement; framing).**
Issue: two points are not said and should be.
- (NA) is a hypothesis about the off-line zeros of ζ. It is vacuously true on RH, and it has no numerical content for ζ
  itself: no off-line zeros are known. The probe tests synthetic configurations only.
- The tested regime is Im z = yL ≤ 1, one configuration per cell, seed 20, n = 120. Proposition Q needs (NA) at
  Im z ≥ c₀L → ∞ with λ_j → ∞, which the probe cannot reach in double precision (‖h‖² ≈ 10¹⁷ already at λ = 4,
  Im z = 1).
Fix: add both sentences. Also say that (NA) could be weakened to "|β − ½| ≥ c₀ with c = c(c₀)", since the proof only
uses that.

**F6 (minor; labels: table rows Prop. Q, Corollary N1; Lemma N).**
Issue:
- Proposition Q uses Lemma PC, which is PROVED-mod-cite ((C3) (3.1)–(3.2), (C6) §3 algebra), so its label omits the
  mod-cite part.
- Corollary N1 is not in the table, and its heading "unconditional, given SPC_ℂ⁺" is self-contradictory.
- Novelty is stated only for Theorem S′.
Fix:
- Prop. Q: "PROVED-mod-cite ((C3), (C6), via Lemma PC) + mod-input SPC_ℂ⁺, (NA)".
- Corollary N1: retitle "(conditional on SPC_ℂ⁺)" and add a table row "PROVED-mod-cite + mod-input SPC_ℂ⁺".
- Add "Novelty: UNCHECKED" to Lemma N, Prop. Q and §4. Lemma N is a routine Sylvester + Ky Fan argument; say so.

**F7 (minor, process; PROOF.md status table, RHFREE.md §4/§6, LOG.md; precedent Plan 19 F8).**
Issue: there is no LOG.md entry for Plan 20 and no pointer from RHFREE.md §4 (quasi-RH heuristic) and §6 (Q1) to
RHFREE2. PROOF.md has no Thm S′ row.
Fix: at T5 add the LOG entry (inputs read, the Rule A notes, this review's outcome). Add forward pointers in RHFREE §0
(the F1 "one-sided full-window" bullet is now resolved by S′), §4 and §6, and a PROOF.md row for Theorem S′.

**F8 (nit; §2 "Size of h_z", κ₁).** κ₁ := ∫_{u≥1/2}η₁² > 0 needs η₁ not a.e. zero on [½, 1). This is not automatic:
η₁ supported in (−½, ½) gives κ₁ = 0. Fix: assume it, or use κ₁(θ) := ∫_{u≥θ}η₁² > 0 for some θ ∈ (0, 1), which gives
T^{2θλy}.

**F9 (nit; §1 "On RH" paragraph).** Add the normalization line: Montgomery's F(α) divides by (T/2π)log T, the
hypothesis by N(T), and the ratio → 1, so the two upper bounds are equivalent. Also add "mod Theorem H" to the first
bullet of Theorem S′ ("RH + upper half … ⇒ (SG) ⇒ G3′").

**F10 (nit; Proposition Q proof).** "Choose j with λ_j c₀ > 2": > 1 suffices (T^{1+ε} ≫ T log T). The phrase
"(and ≥ 1/log T)" is automatic for large T. "Quasi-RH" deserves one precise sentence: the conclusion implies that for
each c₀ only finitely many zeros have |β − ½| ≥ c₀ (hence Θ < 1). It does not imply RH. All of this is conditional on
SPC_ℂ⁺ and (NA).

**F11 (nit; §4 "Lemma G then bounds small gaps by ≈ 20(C − 1)N").** With the non-simple-endpoint term it is
≈ 22(C − 1)N, matching Theorem S′'s constant 22. Also write "this route needs C → 1" rather than "(SG) needs C → 1".
(SG) itself might follow by other means.

**F12 (nit; §4 Reduction, "Both fail with non-constant weights").** Inaccurate. With positive conjugation-symmetric
weights, tr A_w = Σ w_z still holds exactly, A_w still has exactly N_d nonzero eigenvalues (same J-argument with
J_w), and tr A_w² = Σ w_z w_s K(z − s)² is again given by a (weighted) Fourier identity. What breaks is the choice of
target: eigenvalues should cluster near the local weight, not 1, so E_w := Σ(μ − 1)² is not small. Fix: rephrase the
obstacle accordingly. It remains OPEN. Also cite Goldston (4.4) ("F(x, T) = (2/π)∫_0^T|Σ_γ x^{iγ}/(1 + (t − γ)²)|²dt +
O((log T)³)"), the source's own link between the sharp cutoff and the t-integral, which item 3 implicitly uses.

## Recommended labels (after fixes; REVIEWED on re-check)

| Item | Label |
|---|---|
| Theorem S′ (+ Lemma PC′) | PROVED-mod-cite ((C3) (3.5); (C6) (2.4) and §3 algebra; (C1)) + mod-input SPC_ℂ⁺(full), Theorem H. Positivity is self-contained per F1(b), or else add "(C3) MT header / Lemma-1 remark". On RH the hypothesis is exactly the upper half of Montgomery's SPC. Novelty UNCHECKED. |
| Lemma N | PROVED (deterministic). Novelty UNCHECKED (routine Sylvester + Ky Fan). |
| Corollary N1 | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺. |
| Prop. Q | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺, (NA). Conclusion: no zeros with \|β − ½\| ≥ c₀ eventually, for each c₀; not RH. Novelty UNCHECKED. |
| (NA) | HYPOTHESIS; NUMERICAL support on synthetic configurations only, for Im z ≤ 1 (F5). Vacuous on RH. OPEN. |
| §4 | OBSTRUCTION (HEURISTIC, for the Theorem 7 Tauberian route; F3); weighted Lemma G OPEN. |

No claim about RH is made anywhere in RHFREE2 beyond conditional statements under labelled hypotheses. AGENTS
rule 3 is respected, given F10's wording.

## Reproducibility of `checks/check_dist_probe.out`

Rerun at commit 1f13931 with `.venv/bin/python research/G3prime/rhfree/checks/check_dist_probe.py` (about 2 min): the output is byte-identical to the committed `.out` (`diff` empty). Seed 20, deterministic.

## Re-check (fix commit 0fc9e66)

I re-read RHFREE2.md in full and the diffs of CITATIONS.md, LOG.md, PROOF.md and RHFREE.md. I reran
`checks/check_pos_identity.py`; it reproduces "max relative error 1.95e-31".

| Finding | Status | Notes |
|---|---|---|
| F1 | RESOLVED | §1 positivity is now self-contained. I re-derived the residue computation. g_ζ(t) = 1/((1 − ζ + it)(1 + ζ − it)) has an upper-half-plane pole at t = i(1 − ζ). conj g_ζ′ has one at t = i(1 + ζ̄′). These are the two poles the text names. The expansion x^{ρ−½}x^{ρ̄′−½}·W(ρ + ρ̄′ − 1) and the reindexing ρ′ ↦ 1 − ρ̄′ both check. The MT header and the "two changes" quotes match the source. [BGSTB24] is marked unread. Lemma PC′ now points to the identity. The mpmath check (dps 30, 25 pairs) is adequate as NUMERICAL confirmation. |
| F2 | RESOLVED, with residual R1 | The (C3) and (C8) Plan 20 addenda are present, and both mark [BGSTB24] and [18] as NOT read. The quotes match the source except the (9.9) error term (R1). |
| F3 | RESOLVED | §4 is labelled "OBSTRUCTION, HEURISTIC … no impossibility is claimed". Item 3 says "This is the author's analysis, not a statement of the source" and gives C ≈ 2.17. The text adds "That no one-sided argument achieves C → 1 is *not* claimed". The table label is updated. |
| F4 | RESOLVED, with residual R1 | Both sentences are now quoted, and the direction is attributed to "The converse is immediate." The range caveat T ≤ x ≤ T^{2−ε} is stated, together with a note that the full range is improved. |
| F5 | RESOLVED | (NA) is now stated with c = c(c₀) and threshold c₀. "Vacuous on RH … no numerical content for ζ itself" is stated. The probe is limited to Im z ≤ 1, whereas the proof needs Im z ≍ c₀L. Proposition Q's proof is consistent with the new (NA): it no longer needs "≥ 1/log T". |
| F6 | RESOLVED | The table now has a Cor. N1 row, and N1 is retitled "(assuming SPC_ℂ⁺)". Prop. Q is labelled PROVED-mod-cite (via Lemma PC). Novelty UNCHECKED is given for S′, Lemma N and Prop. Q. §4 is labelled heuristic with no novelty claim, which is acceptable. |
| F7 | RESOLVED | LOG.md has a Plan 20 entry (inputs read and unread, Rule A, Rule R). RHFREE.md has forward pointers in §0, §3→§4 and §6. PROOF.md has a "Thm S′" row marked "re-check pending" (update at promotion). |
| F8 | RESOLVED | The κ₁ condition is stated, and it holds for cos². |
| F9 | RESOLVED | The normalization bullet is added. "(mod Theorem H)" is on the RH bullet. |
| F10 | RESOLVED | λ_j c₀ > 1 is used. "Quasi-RH" is defined as "only finitely many dyadic windows contain a zero with \|β − ½\| ≥ c₀". |
| F11 | RESOLVED | The constant is now 22(C − 1), and the text says "this route needs C → 1". |
| F12 | RESOLVED, with nit R2 | tr A_w = Σ w_z and the N_d count are now stated correctly. The obstacle is now the target (varying w_z, not 1). |

**Residuals**
- **R1 (minor; Rule C quote accuracy; RHFREE2 §4 item 1 and the CITATIONS (C8) Plan 20 addendum).** The (9.9) error
  term is quoted as "O(x³(log T)²/T³)". The source layout (gold.txt lines 1302–1307) has exponent 2 on x:
  O(x²(log T)²/T³). This is also the only reading consistent with the source's own remark that the error is smaller
  than the main term (≍ x log T/T) "when T ≤ x ≤ T^{2−ε}". With x³ the crossover would be at x ≍ T.
  Fix: replace x³ by x² in both places. This does not affect any argument.
- **R2 (nit; RHFREE2 §4 Reduction).** The clause "off-line pairs make tr A_w² − Σ w_z² of indefinite sign" is tagged
  "(F12)", but F12 did not assert it. Drop the tag, or drop the clause; the target-mismatch sentence suffices.

**Re-check verdict: ACCEPT (REVIEWED), once R1 is corrected.** R1 is a one-character quote fix that can be made at
promotion. R2 is optional. At promotion, update the RHFREE2 header and the PROOF.md "Thm S′" row from "re-check
pending" to REVIEWED.

**Final labels**

| Item | Label |
|---|---|
| Theorem S′ (+ Lemma PC′) | PROVED-mod-cite ((C3) (3.5); (C6) (2.4) and §3 algebra; (C1)) + mod-input SPC_ℂ⁺(full), Theorem H; positivity self-contained; REVIEWED; novelty UNCHECKED. On RH the hypothesis is exactly the upper half of Montgomery's SPC. |
| Lemma N | PROVED (deterministic); REVIEWED; novelty UNCHECKED. |
| Cor. N1 | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺; REVIEWED. |
| Prop. Q | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺, (NA); REVIEWED; novelty UNCHECKED. Conclusion is quasi-RH as defined, not RH. |
| (NA) | HYPOTHESIS; synthetic NUMERICAL support only (Im z ≤ 1); vacuous on RH; OPEN. |
| §4 | OBSTRUCTION (HEURISTIC, Theorem 7 route only); weighted Lemma G OPEN. |
