# JZC M3a: Theorem H — Jacobi coefficients for Hurwitz lattices (λ_k = (k + δ)^p)

Status (2026-10-22): DRAFT, assembled. Every memo-level link of Theorem H (i) is now REVIEWED, including its input JZC_M4_proof
Theorem N.6 (Lemmas N.6a–d), which is PROVED-mod-cite + REVIEWED since Rule R review B of JZC_M4_proof (REVIEW_JZC_M4_proof_B.md;
fixes M1–M5 applied) (updated 2026-10-22 after Rule R review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md); the honest label of (i) and (ii) is in §4. Rule R review A of the p>1 chain
(research/G1/review/REVIEW_JZC_M3a_H_pgt1_chain_A.md: ACCEPT WITH FIXES, fixes applied 2026-10-21) makes H-a, H-d (i)–(iii), G1u (p > 1)
and H-c (p > 1) REVIEWED. Rule R reviews B (research/G1/review/REVIEW_JZC_M3a_H_plt1_inputs_B.md, REVIEW_JZC_M3a_H_plt1_G1up_B.md,
REVIEW_JZC_M3a_H_assembly_B.md; fixes applied 2026-10-22) make G12, G3 (Lemmas 1–3, Prop 4, Cor 5), G23plt1 (L2.1′–P2.6, Lemma M,
F.1_δ (i)–(iv)), G1u_plt1 (L P1–P5, Prop G1u′), Hc.5 and m3a_e37_decoupled REVIEWED; Theorem N.6 is PROVED-mod-cite + REVIEWED
(reviews A and B of JZC_M4_proof) (§4) (fixed per Rule R review B, C-7, updated for the reviews B now done). The pieces are:
- JZC_M3a_Hd.md: the index transfer H-d, with the jump algebra;
- JZC_M3a_H_G12.md: the outer scalar (G1) and the a-priori bound (G2), p > 1;
- JZC_M3a_H_G3.md: the seam outer scalar, p < 1 (G3);
- §3 below: citations (G4) and the decoupled model in exact algebra (G5);
- §4: the resulting status and the precise list of what is still open.

Labels per VERIFICATION_POLICY.md.

## 1. Statement

Setting:
- −1 < δ ≤ 0, a := 1 + δ, p > 0, p ≠ 1 (for p < 1 the inputs G3, G23plt1, G1u_plt1, Hc.5 assume δ < 0; at δ = 0 Theorem H is
  JZC_M4_proof Theorem N.6 for the lattice) (fixed per Rule R review B, C-3), s ∈ (1, 1 + 2p) (Paper 2's standing assumption; |α| < 1 is used in Cor L2) (fixed per
  Rule R review A of G12, F6, and of G3, F8);
- σ^δ := Σ_{k≥1}(k + δ)^{−s}δ_{(k+δ)^{−p}}, the measure on the reciprocals of the Hurwitz lattice;
- α := (s − 1 − p)/p, c = c(p) (the lattice constant; the continuum density is unchanged);
- the shifted Szegő exponent **β′ := α + 2δ** (= α − 2Z(0) − 1, where Z(0) = ζ(0, a) = −½ − δ);
- the band-factor parameters μ^δ_{n,j} := 2m_j(δ) = 2ζ(−jp, a)/(jn^{jp}), where m_j(δ) is the Fourier sum of §3.2 and the
  equality is Remark 3.3 (PROVED-mod-cite (CITATIONS (Hurwitz-DK)); the Fourier-sum form remains equivalent; NUMERICAL support kept)
  (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)); fixed per Rule R review B, C-4) (fixed per H-c: the former "2m_j(δ)n^{jp}" was n-free; JZC_M3a_H_Hc.md §0).

**Theorem H (target; status per §4).**
- (i) *Reduction.* For every K, J, B, the expansion of n^pb_n(σ^δ)/c is the double expansion of Theorem N.6(i) for the
  **decoupled model M(β′, ν = α)** (JZC_M4 §7): Bessel order α, Szegő exponent β′, the lattice g-function and n^p scaling,
  degree n, band factor exp(−Σ_jμ^δ_{n,j}z^j). The remainder is O(n^{−K−1} + n^{−2−(B+1)p} + n^{−1−(J+1)p}).
- (ii) *Natural form.* With N := n + (β′+1)/2 = n + α/2 + ½ + δ (so −Z(0) = ½ + δ):

  n^pb_n/c = (n/N)^p[1 + f₂N⁻² + f₄N⁻⁴ + Σ_jε_j(δ)N^{−1−jp}(1 + g_jN⁻²) + …]

  - f_{2k} = f_{2k}(p, α) are the lattice integer-layer coefficients (JZC_M4 §5): the integer layer does not depend on δ in N;
  - ε_j(δ) = C(2j, j)pc^jζ(−jp, a), equivalently the Fourier-sum form C(2j, j)pc^j·(−(jp/π)Γ(jp)(2π)^{−jp}S_j(δ)) (§3.2), by
    Remark 3.3 (PROVED-mod-cite (CITATIONS (Hurwitz-DK)); NUMERICAL support to 10⁻²⁷ for p > 1, 2·10⁻²⁴ for p < 1)
    (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)) (fixed per Rule R review B, C-4);
  - g_j(p, α) are the lattice dressings (JZC_M4 §6).

  This is **rule H** (SPEC §3.11(a)) at the orders of Theorem N.6, with the β′-independence of the natural form supplied by
  JZC_M4 Prop S. That is exact algebra for the integer layer to order 4, and for the zeta layer at first order (j = 1, 2, 3 and
  symbolic j, i.e. every j ≥ 1, to N⁻⁴ relative) by §3.3; beyond that it is Conjecture Σ.
  The terms shown are exact (Prop S at exact orders) for f₂, f₄ and for ε_jN^{−1−jp}(1 + g_jN⁻²) for every j (the symbolic-j decoupled
  check was added to m3a_g5_exact per REVIEW_JZC_M3a_H_assembly_B B-1); for f₆ and for the second-order layer ε₁²N^{−2−2p}(3p+1)/(2p)
  + … of N.6(iii), the natural form in N is CONDITIONAL on Conjecture Σ (fixed per Rule R review B, C-9; for p < 2/3 the ε₁² term is
  larger than f₄N⁻⁴).

## 2. Structure of the proof

| step | content | source | status |
|---|---|---|---|
| H-a | interpolation with sin π(t − δ) and 1/Γ(t − δ); node masses; top node X₁ = (n/a)^p | Paper 2 L5.1–5.2, with t ↦ t − δ | JZC_M3a_H_Ha.md (PROVED-mod-cite + REVIEWED, Rule R review A of the p>1 chain; incl. F5 on the moved arcs, C-1) |
| H-b | outer scalar j_δ: sectors and bounds, via the shift identity j_δ(t) = j(t−δ) + (t−δ−½)Log(1−δ/t) + δ and Paper 2's Binet bound (no DLMF 5.11.8 needed) | Paper 2 L6.1, L6.4; H-d §2 | p > 1: G12 L1.1–C1.5 (PROVED-mod-cite; REVIEWED after review B) (fixed per Rule R review B, C-2); p < 1: G3 Lemmas 1–3, Prop 4 (PROVED-mod-cite + REVIEWED, Rule R review B) |
| H-b′ | a-priori bound and L² boundary values for the normalised Q♮, lattice exponent \|α\|/2 (column factorisation) | Paper 2 App C | p > 1: G12 L2.1–P2.4 (PROVED-mod-cite; REVIEWED after review B); p < 1: JZC_M3a_H_G23plt1.md L2.1′–P2.6 (PROVED-mod-cite + REVIEWED, Rule R review B; this is H-d (iv) for p < 1, which G3 Cor 5 does not cover) (fixed per Rule R review B, C-1 / H-1 (1)) |
| H-c | band factor: Binet-cut B_δ (p > 1) or seam χ_δ (p < 1); moments m_j(δ) as Fourier sums; gauge on the circles | E_pgt1 L E.2, E3 L F.1′, E3.4–E3.5, E_plt1 L F.1, SPEC §3.1 | §3.2; JZC_M3a_H_Hc.md: p > 1 Hc.1–Hc.3 (PROVED-mod-cite + REVIEWED, review A of the p>1 chain); p < 1 Hc.5 given G23plt1 F.1_δ (PROVED-mod-cite + REVIEWED, Rule R review B); p < 1 also L P5 of JZC_M3a_H_G1u_plt1.md (fixed per Rule R review B, H-1 (4)) |
| H-d | index transfer: F_δ ∼ C_δ(−z)^δ at ∞, absorbed by the gauge (−z)^{−δσ₃}; result M(β′, α) | JZC_M3a_Hd.md | jump algebra PROVED + REVIEWED (review A of the p>1 chain); analytic inputs G1–G3; for p < 1, G3 Cor 5 gives H-d (i)–(iii), not (iv) (fixed per Rule R review A of G3, F1); (iv) is G23plt1 P2.6; both REVIEWED (Rule R review B) |
| H-e | circle jumps, small norm, residue recursion for M(β, ν) | JZC_M4_proof Lemmas N.6a–c (PROVED-mod-cite + REVIEWED, Rule R reviews A and B (updated 2026-10-22 after Rule R review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md)) (β enters the model only through ρ² = φ^{2(β+1)} and φ^{−2(β+1)}, bounded above and below on the circles, with a jump across the band; fixed per Rule R review B, B-3, C-7); for p > 1 the hard-edge circle data are JZC_M3a_H_G1u.md (REVIEWED); for p < 1 they are JZC_M3a_H_G1u_plt1.md L P3 (glued parametrix; REVIEWED, Rule R review B) (fixed per Rule R review B, C-2 / H-1 (2)); E3 Lemma E3.7 for M(β, ν) | §3.3 |
| H-f | exact algebra for M(β, ν); natural form | m4_shift_exact, m3a_g5_exact | §3.3 |

## 3. Gaps closed here

### 3.1 G4: citations
- **DLMF 5.11.8** (read 2026-10-21, dlmf.nist.gov/5.11, from the TeX alttext): "Ln Γ(z + h) ∼ (z + h − ½) ln z − z + ½ ln(2π) +
  Σ_{k=2}^∞ (−1)^kB_k(h)/(k(k−1)z^{k−1})", in the group of expansions introduced by "As z → ∞ in the sector |ph z| ≤ π − δ".
  It is used with h = −δ fixed, for j_δ(t) = LnΓ(t − δ) − (t − δ − ½)ln t + t − ½ ln 2π = O(1/t) as t → ∞ in |ph t| ≤ π − δ₀. That
  is the hard-edge statement of H-b: nothing changes at 0. **Superseded (G12 L1.1, G3 Lemma 3):** the exact shift identity
  j_δ(t) = j(t−δ) + (t−δ−½)Log(1−δ/t) + δ reduces every bound on j_δ to Paper 2's own Binet bound on j, so the proof no longer
  uses DLMF 5.11.8. The quotation is kept for the record only.
- **Hurwitz's formula is QUOTED** (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)): CITATIONS (Hurwitz-DK)
  quotes it from Dixit–Kumar, arXiv:1912.01199v1, Theorem 1.1 (hypotheses 0 < a ≤ 1, Re s < 0, verbatim; a secondary source quoting
  Titchmarsh (2.17.3)); DLMF 25.11.9 itself still truncates under our fetcher. Applied at s = −kp, a = 1 + δ (both hypotheses hold for
  k ≥ 1, p > 0, −1 < δ ≤ 0). The proof produces the band-factor moments as the explicit Fourier sums (§3.2); their identification with
  ζ(−jp, a) is Remark 3.3, now PROVED-mod-cite (CITATIONS (Hurwitz-DK)), so Theorem H is stated with ζ(−jp, a) directly (the Fourier-sum
  form remains equivalent). NUMERICAL support kept: 10⁻²⁷ for p > 1, spec_hurwitz_moments.out; 2·10⁻²⁴ for p < 1, m3a_g23_F1.out [E]
  (per Rule R review B, B3-2); the formula itself against mpmath at 96 comparisons to 5·10⁻⁴², control fails (checks/m3a_hurwitz_formula.out).
  (Previously: NOT QUOTED, the DLMF page truncating before 25.11.9 and the Wikipedia text having the formulas stripped.)

### 3.2 The band-factor moments as Fourier sums (H-c)
SPEC §3.1 (p > 1) and its p < 1 analogue compute the moments directly from the Binet-cut and seam integrals:
- the jump density 𝔢_δ = 2 Im Log(1 − e^{−2πi(t₊−δ)}) on the cut;
- the Mellin integral ∫_0^∞ e^{−mu}u^{kp−1}du = Γ(kp)m^{−kp} (DLMF 5.2.1, quoted in CITATIONS (DLMF-zeta, Plan 67)) for p < 1; for
  p > 1 the constant is complex (m·2πine^{−iπ/p}) and the input is DLMF 5.9.1 (CITATIONS "(Plan E3)") (fixed per H-c).

With these (SPEC §3.1, proof of Lemma H, first two steps; no Hurwitz formula needed):

  m_k(δ) := (1/2π)∫_{−∞}^0𝔢_δ(y)y^{−k−1}dy = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ),   S_k(δ) := Σ_{m≥1} sin(πkp/2 − 2πmδ)/m^{1+kp}.

This needs only DLMF 5.2.1 (p < 1) or 5.9.1 (p > 1), DLMF 25.2.1, and absolute convergence; the Fubini bound is that of E3 Lemma
F.1′ (p > 1; Hc.2) or E_plt1 Lemma F.1 with complex densities (p < 1; G23plt1 F.1_δ) (fixed per Rule R review B, C-5). Theorem H
uses μ^δ_{n,k} := 2m_k(δ), and so ε_j(δ) = C(2j, j)pc^j·(−(jp/π)Γ(jp)(2π)^{−jp}S_j(δ)), which is C(2j, j)pc^jζ(−jp, a) by Remark 3.3
(updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)).
For p < 1 the seam integrals give the same Fourier sum (SPEC §3.1, "p < 1"; spec_hurwitz_moments_plt1.out).

**Remark 3.3** (PROVED-mod-cite (CITATIONS (Hurwitz-DK)); updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)).
m_k(δ) = ζ(−kp, a)/(kn^{kp}), so ε_j(δ) = C(2j, j)pc^jζ(−jp, a). *Proof.* Hurwitz's formula (Dixit–Kumar Thm 1.1; 0 < a ≤ 1, Re s < 0)
at s = −kp (Re s = −kp < 0) and a = 1 + δ ∈ (0, 1]: cos(2πma) = cos(2πmδ), sin(2πma) = sin(2πmδ), sin(−πkp/2) = −sin(πkp/2), so the
bracket is Σ_m[−sin(πkp/2)cos(2πmδ) + cos(πkp/2)sin(2πmδ)]/m^{1+kp} = −S_k(δ); and 2Γ(1+kp)(2π)^{−1−kp} = (kp/π)Γ(kp)(2π)^{−kp}.
Hence ζ(−kp, a) = −(kp/π)Γ(kp)(2π)^{−kp}S_k(δ) = kn^{kp}m_k(δ) by §3.2. ∎ (Derivation as in CITATIONS (Hurwitz-DK).) NUMERICAL support:
checked to 10⁻²⁷ for p ∈ {1.25, 1.5, 3} at the Hurwitz parameters a ∈ {0.5, 0.3, 0.75, 0.4} of spec_hurwitz_moments.out (stored there as δ ∈ {−0.5, 0.3, 0.75, 1.4}, compared at a = frac(δ); corrected 2026-10-22), and to 5·10⁻⁴² at a = 1+δ, δ ∈ {0, −0.3, −0.5, −0.9} (m3a_hurwitz_formula.out); for p < 1 to 2·10⁻²⁴ (m3a_g23_F1.out [E]) (fixed per Rule R
review B, B3-2); the formula at 96 points to 5·10⁻⁴² (checks/m3a_hurwitz_formula.out). This citation step has not had a second reader
(Rule R). (Previously: NOT QUOTED under Rule C, NUMERICAL only.)

### 3.3 G5: the decoupled model
- Lemmas N.6a–c hold for M(β, ν) verbatim. β enters the model only through ρ² = φ^{2(β+1)} (hard edge) and φ^{−2(β+1)} (soft edge)
  (definition of M(β, ν), JZC_M4 §7; m4_rh_exact2 l. 195, 218). Both are bounded above and below on the circles and jump across the
  band (ρ₊ρ₋ = 1 there); the Δ_k^{mod} are nonetheless meromorphic in both discs (N.6b; the engine asserts the parity in u_to_w)
  (fixed per Rule R review B, B-3; this is how the model is defined — the checks verify its consequences, not that the Hurwitz problem
  reduces to it, which is H-d + G1u/G1u_plt1 + Hc). The sign-pattern and meromorphy arguments involve only ν (Bessel) and
  the Airy data.
  E3 Lemma E3.7 (the n⁻¹ coefficient is d₁ + cpM_μ(4c), exactly linear in μ) also holds for M(β, ν). The soft-edge part of its
  identity is free of the weight exponent symbol. The hard-edge part needs [G_μ(0), A₀(β, ν)] = 0 (fixed per Rule R review A of the p>1 chain, C-2).
  **E3.7 for M(β, ν): exact** (checks/m3a_e37_decoupled.py/.out, ALL IDENTITIES HOLD, ALL 36 CHECKS PASSED incl. 11 controls that
  fail as required; 47 s in the 2026-10-22 re-run; the Laurent-depth check [1] now covers all entries, per Rule R review B, B-4). The model Laurent data of Δ₁^{mod} are read from the exact engine m4_rh_exact2 (DECOUPLE=1, field
  Q(p, α, j, β), α = ν, c = 1), not typed in: B_r, A_r depend on β only, A₀ = (p+2)(4ν²−1)/16·[[1, i], [i, −1]] on ν only, and at β = ν
  they equal check_e3_gauge.py's data. Route 1 (check_e3_gauge's identity with β ≠ ν, all orders in μ, M(4c), M′(4c), M(0) free
  symbols): det G(4c) = 1, G(4c)B_rG(4c)⁻¹ = B_r, [G(0), A₀(β, ν)] = 0, e(M) − e(0) = cpM(4c), e(0) = d₁ = −p(β+1)/2, and the full shift
  Res_{4c} − A_r = M₄c²p[[M₄c − β − 1, …]] with the Szegő exponent β. Route 2 (the engine's own gauge, small-norm recursion and extraction,
  dual numbers to order 3 in μ_j): response p·Q_j(4) at first order and 0 at orders 2, 3, for j = 1, 2, 3 and for symbolic j. Controls:
  the shift with ν in place of β, e − e(0) = cpM(0), A_r(β) = A_r(ν), G(4c) commuting with A_r, response 0 or p·Q_j(0) — all fail.
  Label: PROVED (exact computer algebra, as E3.7 itself), c = 1 normalisation as in the engine; REVIEWED (review B: re-run, controls
  verified nonzero at random points, independent derivation by renaming α ↦ β in check_e3_gauge.py's identity plus an independent
  contour-integral check) (fixed per Rule R review B, C-12). The reviewer's
  numerical check (REVIEW_JZC_M3a_H_pgt1_chain_A C-2: second differences ≤ 10⁻³⁹ at three (p, α, β′), m4_rh4 at dps 40) agrees.
- *F5 on the moved arcs* (C-1 of the same review): Paper 2's far-arc bound on the lengthened Σ^{△±}, the saturated segment up to X₁ + δ′
  and the moved top segment holds with constants depending also on a; written in JZC_M3a_H_Ha.md §4 (fixed per Rule R review A of the p>1 chain, C-1).
- Exact algebra, identically in (p, ν, β):
  - integer layer β-free in N = n + (β+1)/2, with f_odd = 0 and the reflection identity of Theorem R, to order 4
    (m4_shift_exact.out, ALL IDENTITIES HOLD); f₂, f₄ equal their closed forms at the Bessel order (asserted in m3a_g5_exact.out)
    (fixed per Rule R review B, B-2). Controls (added per Rule R review B, B-1; all fail as required): re-expansion in the wrong index
    N′ = n + (α+1)/2 (f₁ = p(α − β)/2) and N′ = n (f₁ = −p(β+1)/2), and reflection about the wrong centre. An order-6 run was stopped at its time limit after order 4;
    order 6 is NUMERICAL only (m4_shift_num.out);
  - first-order zeta layer for j = 1, 2, 3 and for symbolic j (μ normalised by C(2j, j); added per Rule R review B, B-1): no N^{−jp}
    term, leading coefficient C(2j, j)pj/2 (resp. pj/2), no N^{−2−jp} or N^{−4−jp} term, and dressing A_j + B_jν² (β-free)
    (m3a_g5_exact.out, ALL IDENTITIES HOLD, ALL CONTROLS FAIL: 29 identities, 10 controls; ≈ 62 min, of which the
    symbolic-j case 55 min). Controls (B-1): the same raw coefficients re-expanded in N′ = n + (α+1)/2
    or N′ = n (integer layer: f₁ ≠ 0, β-dependent), and the zeta layer with the prefactor (N/n)^p instead of (N/n)^{(j+1)p} or in
    N′ = n + (α+1)/2 — the identities fail, as required.
  - Independence (per Rule R review B, B-5): m4_shift_exact.py and m4_rh_exact2.py share the μ = 0 code path line for line, so the exact
    results are one implementation; independence comes from check [5] of m3a_e37_decoupled (engine data = check_e3_gauge.py's hand data at
    β = ν), the float engine m4_rh4 (m4_shift_num.out) and review B's contour-integral check.
- Numerically: m4_shift_num.out (order 8, 108 checks), m4_shift_zeta.out (40 checks), and m3a_hd_model.out (the Hurwitz data,
  42 checks).

## 4. Status of Theorem H (2026-10-22; every memo-level link of (i) is REVIEWED, Theorem N.6 included since REVIEW_JZC_M4_proof_B.md; (ii) is exact only at the orders stated and CONDITIONAL on Conjecture Σ beyond; the REVIEWED links are listed under "Rule R reviews")

**What is done.**
- *Fixed-n analytic inputs.*
  - p > 1: H-b (outer scalar, G12 §1) and H-b′ (a-priori bound, G12 §2) (REVIEWED, review B).
  - p < 1: H-b (seam outer scalar, G3), and Lemma H-d (i)–(iii) (G3 Cor 5); H-d (iv), the a-priori bound, is item 2 below
    (fixed per Rule R review A of G3, F1) (all REVIEWED, review B).
  - −1 < δ ≤ 0 throughout (δ < 0 for p < 1).
  - Each of these is a statement for fixed n.
- *Jump algebra.* H-d (JZC_M3a_Hd.md). The Hurwitz problem is exactly M(α + 2δ, α) with Hurwitz band factor, in the n^p frame.
- *Algebra of the model.* H-f to order 4 in 1/N and first order in the zeta layer (j ≤ 3), identically in (p, ν, β) (§3.3).

**What is still open for (i)**, in order of difficulty:
1. ~~**The n-uniform hard-edge comparison with Szegő exponent β′**~~: **done for p > 1** in JZC_M3a_H_G1u.md (PROVED-mod-cite +
   REVIEWED, review A of the p>1 chain).
   - The comparison runs in the α-frame. β′ enters only through ρ♮ = ρ^{(α)}/G, which is bounded above and below on the fixed
     disc uniformly in n, for every real β′. The lip limit is e^{∓iπβ′}e^{±2πiδ} = e^{∓iπα}, which matches Bessel order α.
   - The a-priori bound is G12 P2.4.
   - Prop G1u (A): Paper 2 §7 holds verbatim.
   - Prop G1u (B): the order-K small-norm expansion (N.6c) holds, with remainder O(n^{−K−1} + n^{−1−(J+1)p}). It uses H-a and item 5
     (both done) and, for the step to N.6(i), E3.7 for M(β′, α) (§3.3, exact) (fixed per Rule R review B, H-1 (3) / C-10).
   - Checks: m3a_g1u_hardedge.out (110 checks incl. 34 controls; the circle jump is I + Δ₁♮/n + O(n⁻²) at β′ down to −2.2)
     and m3a_g1u_endtoend.out (29 checks incl. 8 controls: fitted Hurwitz Jacobi coefficients at β′ = −2.1, −1.5 match
     M(β′, α); the alternatives are excluded by 10⁴–10⁵ tolerances).
   - **p < 1: done** in JZC_M3a_H_G1u_plt1.md (PROVED-mod-cite + REVIEWED, Rule R review B).
     - E_plt1's glued parametrix is rebuilt with W̃♮ (L P2–P3).
     - The key new step is Lemma P1, a Cauchy-difference bound on the seam band factor. It is δ-uniform.
     - The glue jump is polynomially amplified in the Q-frame.
     - L P5 is an independent proof of H-c for p < 1.
     - Prop G1u′ gives (A) Paper 2 §7 verbatim and (B) the order-K small-norm expansion.
     - Checks: m3a_g1up_hardedge.out (159 checks incl. 36 controls since the N-1 re-run of Rule R review B; the actual seam band factor, β′ down to −2.2) and
       m3a_g1up_endtoend.out (29 checks incl. 9 controls; fitted Hurwitz Jacobi coefficients at p = 0.6, 0.75, β′ = −2.1,
       −1.5).
   - Still OPEN: α ≥ 1, in-lens identification. That is outside the Setting (|α| < 1).
   - A naive β′ treatment fails: the bound |z|^{−|β′|/2} is not L² when |β′| ≥ 1.
2. ~~**H-b′ for p < 1**~~: **done** in JZC_M3a_H_G23plt1.md §1 (PROVED-mod-cite + REVIEWED, Rule R review B).
   - G12's sum bound is p-free (L2.1′).
   - Lens sectors (L2.2′) carry a corrected arc constant, 0.792.
   - The column factorisation holds verbatim (L2.3′).
   - New L2.5: e^{χ_δ} is bounded up to the seams at ∞ and χ_δ → 0 uniformly. The polynomial bound (the unproved sentence of Paper 2
     Lemma seam (iv), δ < 0) is also G3 Lemma 3 (iii′); L2.5 adds the uniform limit (per Rule R review B, B23-1).
   - P2.6 gives Prop apriori and Cor L2 for p < 1, with exponent |α|/2.
   - Check: m3a_g23_apriori.out (132 checks, with controls).
3. ~~E_plt1 Lemma F.1(iv) with complex seam densities~~: **done** in JZC_M3a_H_G23plt1.md §2 (PROVED-mod-cite + REVIEWED, Rule R
   review B).
   - The estimates go through with the pointwise bounds |ℓ_±| ≤ ℓ and |ℓ_±′| ≤ ℓ′ (Lemma M), and the constants are δ-free.
   - (iii) changes: the moments come out as the Fourier sums of §3.2, and the step to ζ(−kp)/(kn^{kp}) is dropped.
   - Check: m3a_g23_F1.out (398 checks, with controls).
4. ~~H-a written out~~: done in JZC_M3a_H_Ha.md (PROVED / PROVED-mod-cite + REVIEWED; m3a_ha_interp.out, 298 checks and
   33 controls that fail as required). It needs Paper 2's T1(a) re-proved at the top node, since x₁ = a^{−p} > 1; the
   expansion holds for |z| > X₁ = (n/a)^p. It also shows why δ > 0 is excluded: the point t = δ is a phantom node, with no
   mass on it, and pole removal fails there.
5. ~~**H-c, the band-factor gauge with Hurwitz moments**~~: **done for p > 1** in JZC_M3a_H_Hc.md (Hc.1 = E_pgt1 L E.2 for δ,
   Hc.2 = E3 L F.1′ for δ with δ-free constants, Hc.3 = the gauge Δ_k♮ = G_{μ^δ}Δ_k^{mod,β′}G_{μ^δ}^{−1} + O(n^{−(J+1)p}) for every k;
   PROVED-mod-cite + REVIEWED for p > 1; m3a_hc_pgt1.out, m3a_hc_gauge.out). For p < 1, Hc.5 gives the gauge from JZC_M3a_H_G23plt1.md
   Lemma F.1_δ (iv) (both PROVED-mod-cite + REVIEWED, Rule R review B; also L P5 of JZC_M3a_H_G1u_plt1.md).

**Status by part.**
- **(i)**: for p > 1, item 5 (H-c) is now JZC_M3a_H_Hc.md (Cor Hc.4), so (i) is PROVED-mod-cite for p > 1, including the remainder
  n^{−2−(B+1)p}, which needs E3.7 for M(β′, α) (§3.3: exact, m3a_e37_decoupled). For p < 1 H-c is Hc.5 (given G23plt1 F.1_δ; also
  G1u_plt1 L P5), and (i) is PROVED-mod-cite for p < 1 as well (inputs G3, G23plt1, H-a, JZC_M3a_H_G1u_plt1.md, JZC_M4_proof N.6).
  Every other ingredient keeps its own label: Paper 2 results are cited (Rule C, quoted in the memos); the E-series lemmas are REVIEWED;
  JZC_M4_proof N.6a–d and Theorem N.6 are PROVED-mod-cite + REVIEWED (Rule R reviews A and B of JZC_M4_proof) (fixed per Rule R
  review B, C-8; (updated 2026-10-22 after Rule R review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md)).
  **Honest label of (i)** (per REVIEW_JZC_M3a_H_assembly_B.md C, last paragraph, updated for the reviews B of G3, G23plt1, G1u_plt1 and
  Hc.5 now done): PROVED-mod-cite for p ≠ 1 (−1 < δ ≤ 0; δ < 0 for p < 1, δ = 0 being Theorem N.6 itself); for p > 1 **and** for
  0 < p < 1 every memo-level link is REVIEWED (Ha, Hd (i)–(iii), G12, G1u, Hc.1–Hc.4; G3, G23plt1, G1u_plt1, Hc.5; m3a_e37_decoupled;
  **JZC_M4_proof Theorem N.6 / Lemmas N.6a–d**, REVIEWED since Rule R review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md, fixes M1–M5
  applied). So **(i) is PROVED-mod-cite and REVIEWED for p ≠ 1** (every memo-level link REVIEWED), with the band-factor constants as
  the Fourier sums S_j(δ) of §3.2 (updated 2026-10-22 after Rule R review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md). With Remark 3.3
  (PROVED-mod-cite (CITATIONS (Hurwitz-DK))), (i) holds with ε_j = C(2j, j)pc^jζ(−jp, a) (μ^δ_{n,j} = 2ζ(−jp, a)/(jn^{jp})) directly: that
  form is **PROVED-mod-cite (adds CITATIONS (Hurwitz-DK))**; the REVIEWED marker covers the Fourier-sum form and everything else, while
  this new citation step (CITATIONS (Hurwitz-DK) and Remark 3.3) has not had a second reader (Rule R) (updated 2026-10-22: Hurwitz's
  formula quoted, CITATIONS (Hurwitz-DK)). (The extension of N.6a–c from the lattice to M(β′, α) is §3.3, checked by Rule R review B of the assembly, B-3, and used
  inside the REVIEWED Prop G1u (B) / Prop G1u′ (B).) Band-factor constants: the Fourier sums = ζ(−jp, a)/(jn^{jp}) by Remark 3.3, PROVED-mod-cite
  (CITATIONS (Hurwitz-DK)), NUMERICAL support kept (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)). Numerically, (i) is confirmed against all stored Hurwitz fits (m3a_hd_model.out, 42 checks; m3a_g3_model.out, 25
  checks, p < 1).
- **(ii)** follows from (i) and Prop S at the exact orders: the integer layer to N⁻⁴ and the first-order zeta layer with its
  N⁻²-relative dressing, every j ≥ 1 (j = 1, 2, 3 and symbolic j, m3a_g5_exact; per Rule R review B, B-1, C-9), at every β. The
  second-order layer ε₁²N^{−2−2p}(3p+1)/(2p) is not checked for M(β, ν) at all (C-9). The orders where Prop S is exact do not cover the full remainder of Theorem N.6, so
  beyond them (ii) is CONDITIONAL on Conjecture Σ, with NUMERICAL support to order 8 (m4_shift_num.out, 108 checks) and for
  the zeta layer (m4_shift_zeta.out, 40 checks).
- **Band-factor constants.** These are the Fourier sums S_j(δ) (§3.2), unconditionally. The identification with ζ(−jp, a) is
  Remark 3.3: PROVED-mod-cite (CITATIONS (Hurwitz-DK)), not yet second-read (Rule R); NUMERICAL support kept (updated 2026-10-22:
  Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)).

**Not covered:** δ > 0 (phantom nodes); p = 1 with δ ≠ 0.

**Rule R reviews (2026-10-21):** JZC_M3a_H_G12.md, reviewer A (research/G1/review/REVIEW_JZC_M3a_H_G12_A.md): ACCEPT WITH
FIXES (no mathematical error; F1–F6 MINOR/INFO, applied). JZC_M3a_H_G3.md, reviewer A (research/G1/review/REVIEW_JZC_M3a_H_G3_A.md):
ACCEPT WITH FIXES (one MAJOR scope fix, F1: Cor 5 restricted to H-d (i)–(iii); F2–F9 MINOR, applied). Those reviews did not re-run the
checks; reviews B (below) did, and both memos are now REVIEWED.
JZC_M3a_H_Ha.md, JZC_M3a_Hd.md, JZC_M3a_H_G1u.md, JZC_M3a_H_Hc.md, reviewer A (research/G1/review/REVIEW_JZC_M3a_H_pgt1_chain_A.md):
ACCEPT WITH FIXES for all four (no MAJOR finding; Ha-1–3, Hd-1–2, G1u-1–3, Hc-1–2 MINOR/INFO, applied 2026-10-21). This review
re-derived the key steps and **re-ran all seven checks (byte-identical outputs)**, so with the fixes applied these memos are REVIEWED
(VERIFICATION_POLICY.md, Rule R and the REVIEWED row), within the scope the review covered: Ha in full; Hd Lemma (i)–(iii); G1u L1–L4 and
Prop G1u for p > 1; Hc.1–Hc.3 and Cor Hc.4 (p > 1). Hc.5 and G1u's "p < 1" paragraph were not reviewed by it. (Review A's last
paragraph anticipated a further reader. Under VERIFICATION_POLICY.md Rule R, a reader who re-derives the key steps and re-runs the checks
suffices, and review A did both; the REVIEWED markers rest on that. JZC_M4_proof.md is held to the stricter reading: see C-7.) (Added
per Rule R review B, C-6; a human should decide which reading the repo uses and make JZC_M4_proof.md and the H chain consistent.)
**Rule R reviews B (2026-10-22)** (reviewer B; each re-derived the key steps and re-ran the checks byte-identically):
- research/G1/review/REVIEW_JZC_M3a_H_plt1_inputs_B.md: JZC_M3a_H_G3.md and JZC_M3a_H_G23plt1.md ACCEPT WITH FIXES (B3-1 – B3-7,
  B23-1 – B23-9, all MINOR/typo/INFO, applied). REVIEWED: G3 Lemmas 1–3 (incl. (ii′), (iii′)), Prop 4, Cor 5 (i)–(iii); G23plt1
  L2.1′–L2.5, P2.6, Lemma M, F.1_δ (i)–(iv). Remark H stayed NUMERICAL at that review; it is now PROVED-mod-cite (CITATIONS
  (Hurwitz-DK)), not yet second-read (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)).
- research/G1/review/REVIEW_JZC_M3a_H_plt1_G1up_B.md: JZC_M3a_H_G1u_plt1.md ACCEPT / ACCEPT WITH FIXES (P3-1, G-1, P1-1, N-1 – N-4,
  applied; m3a_g1up_hardedge re-run after N-1), Hc.5 ACCEPT WITH FIXES (Hc5-1, Hc5-2, applied); H-1 applied here. REVIEWED: L P1–P5,
  Prop G1u′ (A), (B); Hc.5.
- research/G1/review/REVIEW_JZC_M3a_H_assembly_B.md: A. JZC_M3a_H_G12.md ACCEPT (A-1, A-2 applied): REVIEWED. B. exact checks of §3.3
  ACCEPT WITH FIXES (B-1: controls added to m4_shift_exact.py and m3a_g5_exact.py, plus the symbolic-j case; B-2, B-3, B-4, B-5 applied;
  scripts re-run): m3a_e37_decoupled REVIEWED. C. this memo ACCEPT WITH FIXES (C-1 – C-12 applied).
*Response to the chain links.* **C-1** (F5 on the moved arcs): the reviewer's verification is now JZC_M3a_H_Ha.md §4 "F5 on the moved
arcs", and G1u §1 row F5 points there. **C-2** (E3.7 for M(β, ν) used but not stated): stated in §3.3 and **checked exactly** with β and ν
independent (checks/m3a_e37_decoupled.py/.out: ALL IDENTITIES HOLD, ALL 36 CHECKS PASSED, controls fail). The provisional label the
review proposed for (i)'s remainder term ("PROVED-mod-cite, with E3.7 for M(β′, α) NUMERICAL") is therefore not needed: the remainder
n^{−2−(B+1)p} is PROVED-mod-cite, with E3.7 for M(β′, α) by exact computer algebra (REVIEWED: review B re-ran it, verified the controls
nonzero at random points, and re-derived E3.7 for M(β, ν) by renaming α ↦ β in check_e3_gauge.py's identity plus an independent
contour-integral check; fixed per Rule R review B, C-12).
With C-1 and C-2 closed, the review's chain verdict applies: for p > 1 the chain H-a → H-b → H-b′ → H-c → H-d → H-e → (i) has no known gap;
its last link not marked REVIEWED at the time, JZC_M4_proof Theorem N.6 / Lemmas N.6a–c, is now PROVED-mod-cite + REVIEWED (Rule R
review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md) — G12 and m3a_e37_decoupled are REVIEWED by review B (REVIEW_JZC_M3a_H_assembly_B.md)
(fixed per Rule R review B, C-7; (updated 2026-10-22 after Rule R review B of JZC_M4_proof, REVIEW_JZC_M4_proof_B.md)).

**For FIXES (via a human; Rule 1):** two wording gaps in Paper 2. (1) Binetcut (iv), (O5) at ∞. The text says "where 𝔟′ is bounded";
the argument needs |𝔟′(y)| ≤ C/|y|, which Paper 2's own proof of (ii) supplies (G12 §4 item 6). (2) Lemma seam (iv), (O5) at ∞
(app_outer.tex, last lines of (O5)): "In S_in ∩ {|z| ≥ n^p+δ′} … D, B_in, K and e^χ are bounded above and below by powers of |z|"
is not justified for e^χ there (Lemma corner (ii) gives only a log² bound, away from the seams); the claim is true by a window
argument (G3 Lemma 3 (ii′), (iii′); G3 §6 item 9) (added per Rule R review A of G3, F2). The results are unaffected.

**Corrections to JZC_M3a_Hd.md** (G12 §5): (2.1) needs no DLMF 5.11.8; the monodromy step in (2.4) is replaced by Lemma
normalisation; the vertex is X₁ + δ′ = (n/a)^p + δ′; §3(iv)'s identity [·] = (4c/Υ)^δe^{±iπδ} holds in ℂ_± with principal
branches (arg Υ ∈ (0, π) in ℂ₊), and only its modulus |G| = |4c/Υ|^δ is used (fixed per Rule R review A of G12, F3). No claim of
the memo was found false.
