# Rule R review: JZC M4 proof, reviewer A: JZC_M4_proof.md, Theorem N.6 (lattice expansion to n⁻⁶, p > 1)

Reviewer: independent second reader (Rule R), reviewer **A**. Date: 2026-10-21.
- Target: research/G1/RH/spectral/JZC_M4_proof.md (Theorem N.6; Lemmas N.6a, N.6b, Prop N.6c, Lemma N.6d), commit 1d30d47
  (branch plan-e2-d2); checks/m4_rh_exact.py, m4_zeta_exact.py and outputs m4_rh_exact_k4.out, m4_rh_exact_k6.out,
  m4_zeta_exact.out.
- Context read: AGENTS.md, VERIFICATION_POLICY.md; second_order/E2_pgt1.md (Prop E2.5, Lemmas E2.3, E2.4, E2.6) and
  checks/check_e2_sym.py; second_order/E3.md (Lemmas F.1′, E3.4, E3.5, E3.7, Prop E3.6); spectral/JZC_M4.md §§5–6;
  review/REVIEW_PlanE2_A.md (B2); RH/CITATIONS.md entries (KMVV-orient, Paper 2), (DLMF-10.40, Paper 2), (DLMF-10.17, Plan 55),
  (DLMF-9, Paper 2), (DLMF-9.7.2, Plan 65), (Plan 65 reuse), (Plan E2 reuse), (JZC M4 reuse).
- I edited no file except this report. My scripts are in the session scratchpad (`…/scratchpad/review/`: shi_test.py,
  shi_zeta.py, mutate.py, sector_k3.py).

## Overall verdict: **ACCEPT WITH FIXES**

I found **no mathematical error** in the residue recursion, the order-K small-norm induction, the jump data, the scripts or
the natural-form conversion. All exact identities hold, and I re-ran them. One MAJOR fix concerns scope: Theorem N.6(iii)
and the "Consequences" present as proved asymptotic coefficients several terms that lie below the theorem's own remainder
O(n^{−2−2p}) (F1). The other fixes are MINOR or INFO.

Output status at the time of review: m4_rh_exact_k4.out, m4_rh_exact_k6.out and m4_zeta_exact.out all end with
"ALL IDENTITIES HOLD" / "EXIT 0". (k6 finished 12:04:21 and zeta 12:07:09; both were still running when this review began.)
F6 notes a provenance issue with the zeta output.

| Item | Verdict | Fixes |
|---|---|---|
| Lemma N.6a (jumps to every order, sector independence) | ACCEPT WITH FIXES (correct; the Airy wording is literally false in some subsectors) | F3 |
| Lemma N.6b (meromorphy) | ACCEPT WITH FIXES (wording of the parity statement) | F4 |
| Prop N.6c (order-K small norm) | ACCEPT WITH FIXES (the induction claim must carry the n^{−1−(J+1)p} term) | F2 |
| Lemma N.6d (exact algebra) | ACCEPT (re-run; truncation independent; guard verified) | F6, F7, I1 |
| Thm N.6(i)–(ii) | ACCEPT | I2 |
| Thm N.6(iii) and Consequences | ACCEPT WITH FIXES (visibility of terms) | F1, F5 |
| Rule C | ACCEPT WITH FIXES (the hypotheses line is missing from "(JZC M4 reuse)") | F8 |

## Findings

**F1 (MAJOR; scope; Thm N.6(iii), header table, "Consequences", JZC_M4.md table rows Prop N.3, N.4).** The remainder of
(iii) is O(n⁻⁷ + n^{−2−2p}). Several displayed terms are smaller than n^{−2−2p} for some or all p > 1, so (iii) does not
determine them as coefficients of n^pb_n/c. The displayed formula stays *true*, since terms inside an O are harmless. But
"g_j (j ≤ 5) … now proved" and "f₄, f₆ … now proved" overstate what (iii) gives. Term by term, against n⁻⁷ + n^{−2−2p}:

| term | exponent | visible (= determined by (iii)) iff |
|---|---|---|
| f₂N⁻², f₄N⁻⁴ | 2, 4 | all p > 1 |
| f₆N⁻⁶ | 6 | p > 2 |
| ε₁N^{−1−p} | 1 + p | p < 6 |
| ε₁g₁N^{−3−p} | 3 + p | p < 4 |
| ε₂N^{−1−2p} | 1 + 2p | p < 3 |
| ε₂g₂N^{−3−2p}, and ε_jg_j for every j ≥ 2 | 3 + jp ≥ 3 + 2p | never |
| ε_jN^{−1−jp}, j ≥ 3 | 1 + jp ≥ 1 + 3p > 2 + 2p | never |
| "f₅ = 0" read as a statement about b_n | 5 | p > 3/2 |

Example: at p = 3/2 the N⁻⁵ coefficient of b_n is (3p+1)/(2p)·ε₁² ≠ 0 (JZC_M4 §6, NUMERICAL), not f₅ = 0.
- What *is* proved for g_j (j ≥ 2), ε_j (j ≥ 3), and f₆ when p ≤ 2: they are identities for the μ = 0 layer 𝔇_K(n; 0) and its
  first μ_j-derivative, i.e. Lemma N.6d combined with Thm N.6(ii). They are not asymptotic coefficients of b_n.
- The ζ(−p)² layer (and, at n⁻³, μ₁² cross terms) sits at N^{−2−2p}, N^{−3−2p}, … and is not controlled. So, for example, the
  N^{−3−2p} coefficient of b_n is ε₂g₂ *plus* an uncomputed second-order term. JZC_M4 §6 reports numerically that this term
  vanishes; that is not proved.

*Fix:*
- Add the visibility table (or equivalent sentences) after Thm N.6(iii).
- Restate the Consequences: "f₂, f₄ (all p > 1), f₆ (p > 2), ε₁, ε₁g₁ (p < 4), ε₂ (p < 3) are coefficients of n^pb_n/c."
  The remaining items "are proved as coefficients of the first-order (in μ) model layer 𝔇_K, Thm N.6(ii)."
- Mirror this in the JZC_M4.md label table (Prop N.3: f₆ PROVED-mod-cite for p > 2 only; Prop N.4: as above).
- Alternatively, extend the dual numbers to second order (ε³ = 0, two directions) and prove the μ² layer. That would push the
  remainder to n^{−3−3p}-type terms and make g₂ and f₆ (p ≤ 2) visible.

**F2 (MINOR; Prop N.6c, induction claim).** As stated, "R₋ = Σ_{k<K}R₋⁽ᵏ⁾n^{−k} + O_{L²}(n^{−K})" is false at stage m once
n^{−1−(J+1)p} ≫ n^{−m}, i.e. m > 1 + (J+1)p. The jump error contains Δ_k − Δ_k^{μ_n} = O(n^{−(J+1)p}) at order n^{−1}, and it
enters R₋ at that size. Example: J = 1, p = 1.1, K = 6. The proposition's *conclusion* (error η_n) is correct. For K = 6,
J = 5, p > 1 the issue does not arise, because 1 + 6p > 7.
*Fix:* make the induction claim R₋ = Σ_{k<m}R₋⁽ᵏ⁾n^{−k} + O_{L²}(n^{−m} + n^{−1−(J+1)p}) for m ≤ K + 1, and carry the extra term
through the step: it is multiplied by J − I = O(1/n) or appears once, so it stays O(η_n). Also name the running index m to
avoid the clash with the fixed Poincaré order K.

**F3 (MINOR; Lemma N.6a proof and E2 Lemma E2.3, Airy sectors).** The claim "ξ(q^{±1}ζ) = −ξ(ζ)", with principal branches as
DLMF 9.7.5–9.7.6 require, is false in some subsectors.
- Example: for π/3 < arg ζ < π and Z = e^{2πi/3}ζ, the principal argument of Z wraps, and ξ(Z) = +ξ(ζ). This is confirmed
  numerically at arg ζ = 1.5, 2.4, 2.9 (sector_k3.py, "m = 1" rows show the (−1)^k pattern).
- The parenthetical "(I_α, Ai at the rotated argument)" for the (−1)^k column is also inexact. In sector I the (−1)^k column is
  Ai(ζ) itself (y₀), and the rotated column carries the + pattern.

The *conclusion* (C_k′ and X_k are sector-independent for every k) is correct. *Fix:* replace the sentence by the tie
argument, which is k-uniform and branch-proof:
- every column is a k-independent constant times Ai(Z) or Ai′(Z), with Z = e^{2πim/3}ζ and |ph Z| ≤ π − δ;
- then Z^{3/2} = ±ζ^{3/2}, and 9.7.5–9.7.6 give e^{−ξ(Z)}Σ(−1)^ku_kξ(Z)^{−k} = e^{∓ξ}Σ(∓1)^ku_kξ^{−k};
- so (−1)^k sits exactly on the column carrying e^{−ξ}, whichever branch occurs;
- the Bessel analogue is the same: H⁽¹⁾_α(x) = (const)e^{−Y}Σa_kY^{−k} with Y = −ix = ±w; H⁽²⁾ has Y = ix; I_α, K_α have Y = −w, w.

Which column carries e^{±ξ} (or e^{±w}) is fixed at k = 0, so C_k, C_k′ follow for every k. The same wording should be
corrected in E2 Lemma E2.3 (E2 is REVIEWED; the fix is textual only).

**F4 (MINOR; Lemma N.6b, "Computer-algebra confirmation").** "u^{3k+1}Δ_k^r has only even powers of u" is wrong for even k.
E2 Lemma E2.6(a) correctly says u⁷Δ₂^r has only *odd* powers. What `u_to_w` asserts is that Δ_k^r itself contains only even
powers of u, i.e. u^{3k+1}Δ_k^r contains only powers ≡ 3k + 1 (mod 2). *Fix:* reword.
- Also, the caveat in §7 item 3 is too modest. It says the parity test is "like E2's parity check … does not detect every
  possible swap". My mutation run (mutate.py) shows that the parity assertion *does* catch a flipped (−1)^k column at k = 3
  and k = 4 on both edges.
- The swaps a₃ ↔ b₃ and u₃ ↔ v₃ pass parity but are caught by f₃ = 0. Doubling u₄, v₄ is caught only by the f₄ closed form.
  That form was reconstructed from m4_rh4.py, which uses the same input formulas, so this catch is not independent of the
  inputs (Rule X).
- The independent catch is the lattice fit m4_f4_lattice.out (f₄ to 3·10⁻¹⁰ at p = 4).
- Record these results in §7.

**F5 (MINOR; Theorem N.6(iii) remainder bookkeeping).** The bracket's "O(N⁻⁴)" relative error contributes O(N^{−5−jp}). For
j = 1 this is n^{−5−p}, which is not o(n⁻⁷) when p < 2. It *is* inside O(n^{−2−2p}) for p < 3, and inside O(n⁻⁷) for p ≥ 2,
so the stated total remainder is right. But the proof never says so. *Fix:* one sentence: "the bracket's O(N⁻⁴) is
O(n^{−5−p}) ⊂ O(n⁻⁷ + n^{−2−2p})". Also note that the N^{−4−jp} coefficient is proved zero, so the bracket error is really
O(N⁻⁵) relative.

**F6 (MINOR; provenance of m4_zeta_exact.out).** The run that wrote m4_zeta_exact.out started at 11:54:50. m4_rh_exact.py was
last modified at 11:58:35 (the committed version, 1d30d47). Python imported the module at start, so the committed zeta output
was produced by an *earlier, uncommitted* version of m4_rh_exact.py.
- I re-ran j = 1 (KORD = 5, SHI = 18) with the committed script. All five identities hold, EXIT 0, with the same timings.
- I also ran j = 1, 3 at KORD = 4 with SHI 14 and 18, with identical exact results. So nothing indicates a discrepancy.
- Under Rule N.3 (reproducible script), however, the committed .out must come from the committed .py.

*Fix:* re-run `KORD=5 SHI=18 JMAX=5 python -B m4_zeta_exact.py` against the committed script. Print a sha256 of
m4_rh_exact.py in both outputs, and update MANIFEST.

**F7 (INFO; m4_rh_exact.py docstring, N.6d wording).**
- The docstring (lines 9–10) lists the assertions only up to f₄. The script also asserts f₅ = 0 and f₆ (KORD ≥ 6).
- N.6d says "d₂ does not depend on c …, and nothing does: every input depends on z/c only". This is true for the integer
  layer only: the μ_j-response scales as c^j (see I2).

**F8 (MINOR; Rule C.2; CITATIONS "(JZC M4 reuse)").** The entry lists the formulas but has no "Hypotheses checked" line, unlike
"(Plan E2 reuse)". Lemma N.6a applies 10.40.1–4, 10.17.5–6, .11–.12 and 9.7.5–6 to K + 1 terms; their hypotheses are ν = α > −1
fixed (no DLMF restriction) and the sectors |ph w| < π/3 (10.40.1–4), ph 2(−ζ)^{1/2} ∈ (−π/6, π/6) (10.17.x) and |ph Z| ≤ π − δ
(Airy). The lemma also uses the KMVV (6.23)–(6.25) Bessel model ("KMVV-orient, Paper 2") and the Paper 2 Airy model. Neither
is named in the reuse entry. *Fix:* add the hypotheses line and these two entries to "(JZC M4 reuse)". Every quoted formula
itself is present verbatim in CITATIONS. I found no statement that relies on an unquoted external source.

**I1 (INFO; the exact scripts, item 3(a)–(d)).** I read every routine. Results:
- *Class S.* add (lo = min, hi = min) is correct. mul (hi = min(hi₁ + lo₂, hi₂ + lo₁)) is correct, and conservative when lo is
  not trimmed. inv (hi − lo preserved after trim) is correct. powr1 is the J.C.P. Miller recurrence
  b_k = (1/k)Σ_j((e+1)j − k)q_jb_{k−j}, valid over the commutative dual ring, with hi preserved. shift and the cap at S.HI only
  lower hi.
- *u_to_w and z_to_v.* u_to_w (hi ↦ ⌊hi/2⌋, odd known coefficients asserted zero) and z_to_v (hi ↦ 2hi + 1; the extra odd
  coefficient is exactly zero) are correct.
- *Re-expansion.* reexpand (binomial (d + t)^{−m}, d = z_e − z_o, exact, so hi = 11 is a true bound) is correct.
- *Principal-part guard.* pp requires hi ≥ −1, so every coefficient down to the residue is known; the output principal part is
  an exact polynomial in 1/w. The guard really trips: at KORD = 2 with SHI = 4, and at KORD = 4 with SHI = 10, 12, it raises
  "truncation too shallow" rather than returning a value. At KORD = 2 the exact d's are identical for SHI ∈ {6, 8, 10, 30};
  at KORD = 4 for SHI ∈ {14, 18}.
- *Dual arithmetic.* G.__mul__ and G.inv are correct to first order.
- *(b) Local data.* The local data agree line by line with check_e2_sym.py at c = 1: S-series, κ = S(0)/(8p) = 1/(6p),
  𝔞_∞² = u/z^{1/2}, h₂ = ((z^{1/2} + u)/2)^{−(2+2α)}, conj_soft; f = −z(Σ)²/(16p²), f^{1/2} = v((p+2)²g)^{1/2}/(p+2),
  a2h = (4 + v²)^{1/2}/v, ρ² = (v/2 + (1 + v²/4)^{1/2})^{2(α+1)}, conj_hard; the factors (−1/φ̃)^k and (2f^{1/2})^{−k}.
  Xk(1), Xk(2), Xik(1), Xik(2) equal E2's X₁, X₂, Ξ₁, Ξ₂ (checked by hand). The KORD = 2 assertion d₂ = E2 Thm E2.1 is
  therefore a meaningful re-derivation in independent code: a different series class, and exact field arithmetic instead of
  sympy series.
- *(c) Gauge derivative.* ∂_{μ_j}cosh h|₀ = 0 and ∂_{μ_j}(sinh h/𝓡)|₀ = Q_j/2, so ∂_{μ_j}G_μ|₀ = 𝒢_j as stated. The code's
  `gen` builds T[[0, −(z−4)Q_jε/2], [−zQ_jε/2, 0]]T⁻¹ with Q_j = Σ_i z^{j−1−i}C(2i, i), in the local variable z = 4 + w
  (soft edge) or z (hard edge). It then applies Δ ↦ Δ + [𝒢_j, Δ]. This is correct. The sign is pinned by the asserted lead
  C(2j, j)pj/2 = p·Q_j(4) (E3 Lemma E3.7, REVIEWED): the opposite gauge would flip it.
- *(d) Natural form.* x = 1/N and 1/n = x/(1 − δx) with δ = α/2 + ½. The integer layer is (N/n)^p = (1 − δx)^{−p}. The zeta
  layer is n^{−jp} = N^{−jp}(N/n)^{jp}, hence the factor (1 − δx)^{−(j+1)p}. Then μ_{n,j}·(C(2j, j)pj/2) = C(2j, j)pζ(−jp) =
  ε_j at c = 1. Correct.

**I2 (INFO; Thm N.6(ii) and the c remark).**
- In (ii), the analyticity of 𝔇_K in μ does not need "(Q₁)₁₂(Q₁)₂₁ bounded away from 0". The n⁰ term of Q₁₂Q₂₁ is exactly c²
  (P₁ is μ-free), so each d_k(μ) is a polynomial in the entries of R_1⁽ⁱ⁾(μ), i ≤ k, and these are entire and n-independent.
  This gives the Taylor bound directly. The use of E3 Lemma E3.7 (d₁(μ) exactly linear), which makes the μ² remainder
  O(|μ|²n⁻²) = O(n^{−2−2p}), is correct.
- §7 item 7 says "the gauge coefficient scales as c^{j−1} through Q_j". The complete statement: with z = cζ, (z − 4c)Q_j and
  zQ_j are c^j times their c = 1 values. So 𝒢_j(z) = c^j𝒢_j^{(1)}(ζ), and μ_j enters only through c^jμ_j. The ratio g_j is
  c-free and ε_j carries c^j. The text's conclusion is right; state the reason in this form.

## Re-derivations

**Prop N.6c (item 1).**
- Orientation: with clockwise circles, the + side is outside, R_out = R_inJ, so order by order
  R_out⁽ᵏ⁾ = R_in⁽ᵏ⁾ + Σ_{j=1}^kR_in⁽ᵏ⁻ʲ⁾Δ_j = R_in⁽ᵏ⁾ + F_k. The left factor order matches E2 Prop E2.5 (R₋(J − I)).
- Uniqueness: R_out⁽ᵏ⁾ analytic outside the discs, vanishing at ∞, with R_out − F_k analytic in each disc, is the sum of
  principal parts (Liouville).
- Cauchy transform: for z outside, (1/2πi)∮_{cw}F(s)ds/(s − z) = +pp(F)(z); this is the sign of the residue at s = e of
  F(s)/(s − z) in clockwise orientation. Inside, it is pp − F. The minus side of a clockwise circle is the inside, so
  𝒞₋(F_mχ) = R_in⁽ᵐ⁾ on the circles. Off the circles 𝒞₋ = 𝒞 = R_out⁽ᵐ⁾, which is continuous across the other pieces.
- Moment: R_1 = −(1/2πi)∫R₋(J − I), and −(1/2πi)∮_{cw}F = ΣRes.
- Hypothesis strength: L² on Σ_R plus Cauchy–Schwarz against the kernel (distance ≥ d) gives the uniform statement off the
  contour, as in E2. The off-circle pieces have R₋⁽ᵏ⁾ = R_out⁽ᵏ⁾ bounded and O(1/|z|), against jumps O(e^{−n/C}) or O(n^{−pn/4})
  on length O(n^p). The hard-edge mismatch is O(n^{−K′}) on a bounded set. All of these are η_n-small.
- The only defect is F2. The code's recursion (lines 243–260) implements exactly this: F_k = ΣRin[k−j]·Δ_j, Rout = own pp +
  re-expanded other pp, Rin = Rout − F_k, and R1 = ΣRes.

**Lemma N.6a at k = 3 (item 2).**
- *By hand, Bessel, 2π/3 < arg ζ < π.* ζ^{1/2} has arg ∈ (π/3, π/2) and (−ζ)^{1/2} = −iζ^{1/2}, so x = 2(−ζ)^{1/2} = −iw,
  with ph x ∈ (−π/6, 0) inside both 10.17.5 and 10.17.6.
  - 10.17.5: e^{ix} = e^{w}, and i³a₃/x³ = i³a₃/((−i)³w³) = −a₃/w³.
  - 10.17.6: e^{−ix} = e^{−w}, and (−i)³a₃/x³ = +a₃/w³.
  - 10.17.11–12 give −b₃/w³ and +b₃/w³ in the same columns.
  - KMVV (6.24) puts H⁽¹⁾ in column 1 (the e^{+w} column). So C₃ = [[−a₃, a₃], [−b₃, b₃]], as for I_α, K_α in the central sector.
- *Lower sector, −π < arg ζ < −2π/3.* x = +iw. KMVV (6.25) puts H⁽²⁾ in column 1, with e^{−ix} = e^{w} and
  (−i)³/(i³w³) = −1/w³. Same C₃.
- *Airy, by hand.* In sector I, the column Ai(e^{−2πi/3}ζ) has ph ∈ (−2π/3, 0), so ξ ↦ −ξ and the u₃, v₃ terms enter with the +
  sign. Ai(ζ) carries −u₃, −v₃. So C₃′ = [[u₃, −u₃], [v₃, −v₃]]. In sector II the decaying column is Ai(e^{2πi/3}ζ). Its
  principal argument wraps, so ξ(Z) = +ξ(ζ) and the column carries (−1)³ (F3), with the same C₃′.
- *Numerically* (sector_k3.py, mpmath at 40 digits, my own KMVV Ψ):
  - Bessel: ‖w³(M⁻¹(2πζ^{1/2})^{σ₃/2}Ψe^{−wσ₃} − I − Ξ₁/w − Ξ₂/w²) − Ξ₃‖ halves (ratios 0.488–0.499) when |ζ| goes 400 → 1600.
    Tested at α ∈ {0.3, −0.6, 1.7} and arg ζ ∈ {0, 1.5, −1.9, ±2.3, ±2.9}, so all three sectors, with Ξ₃ = M⁻¹(M∘C₃).
  - Control: the wrong pattern in column 1 at arg ζ = 2.3 leaves an O(1) error of 0.128.
  - Airy: Ai(Z) and Ai′(Z), Z = e^{2πim/3}ζ, m ∈ {0, ±1}, for eight arguments in both half-planes. The error times |ξ|³ of
    the three-term sum, taken with the tie pattern of F3, drops by 1/8 when |ζ| × 4.
- **Pattern holds.**

## Independent verification (commands and outputs)

Python: `…/scratchpad/venv/bin/python -B`; scripts in `…/scratchpad/review/`.
- `KORD=2 SHIS=4,6,8,10,30 python -B shi_test.py`: SHI = 4 gives "ASSERTION truncation too shallow". SHI = 6, 8, 10, 30 all give
  d₁ = −p(α+1)/2 and d₂ = (3p²α² + 6p²α + 3p² + 6pα + 5p − 6α² + 2)/24 (= E2 Thm E2.1), identical across SHI.
- `KORD=4 SHIS=10,12,14,18 python -B shi_test.py`: SHI 10 and 12 give "truncation too shallow". SHI 14 (9 s) and 18 (34 s) give
  identical d and f.
- `python -B shi_zeta.py` (KORD = 4, j = 1, 3, SHI 14 vs 18): zeta response identical, g[1] = p (j = 1) and 30p (j = 3), equal to
  C(2j, j)pj/2.
- `python -B mutate.py` (KORD = 4, SHI = 14):
  - unmutated: all identities hold;
  - Bessel or Airy (−1)^k column flipped at k = 3 or k = 4: "ASSERTION not even" (4/4);
  - a₃ ↔ b₃ and u₃ ↔ v₃: d₂ ok, f₃ ≠ 0, f₄ wrong;
  - u₄, v₄ doubled: f₃ = 0, f₄ wrong.
- `KORD=5 SHI=18 JMAX=1 python -B m4_zeta_exact.py` (copy of the committed script; sha256 identical to the repo's): j = 1, all
  five identities True, "ALL IDENTITIES HOLD", EXIT 0 (140 s).
- `python -B sector_k3.py`: Bessel and Airy k = 3 results as in "Re-derivations".
- Repo outputs re-read after completion:
  - m4_rh_exact_k6.out: d₁, d₂, f₁–f₆ all True, "ALL IDENTITIES HOLD", EXIT 0 (331 s);
  - m4_zeta_exact.out: j = 1…5 all True, "ALL IDENTITIES HOLD", EXIT 0 (but see F6);
  - m4_rh_exact_k4.out: "ALL IDENTITIES HOLD".
- Not done: the KORD = 6 run, by instruction.

Novelty: not assessed (outside remit).
