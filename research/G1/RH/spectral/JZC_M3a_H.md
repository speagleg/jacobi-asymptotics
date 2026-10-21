# JZC M3a: Theorem H — Jacobi coefficients for Hurwitz lattices (λ_k = (k + δ)^p)

Status (2026-10-21): DRAFT, assembled; NOT REVIEWED (Rule R pending for every piece). The pieces are:
- JZC_M3a_Hd.md: the index transfer H-d, with the jump algebra;
- JZC_M3a_H_G12.md: the outer scalar (G1) and the a-priori bound (G2), p > 1;
- JZC_M3a_H_G3.md: the seam outer scalar, p < 1 (G3);
- §3 below: citations (G4) and the decoupled model in exact algebra (G5);
- §4: the resulting status and the precise list of what is still open.

Labels per VERIFICATION_POLICY.md.

## 1. Statement

Setting:
- −1 < δ ≤ 0, a := 1 + δ, p > 0, p ≠ 1, s ∈ (1, 1 + 2p) (Paper 2's standing assumption; |α| < 1 is used in Cor L2) (fixed per
  Rule R review A of G12, F6, and of G3, F8);
- σ^δ := Σ_{k≥1}(k + δ)^{−s}δ_{(k+δ)^{−p}}, the measure on the reciprocals of the Hurwitz lattice;
- α := (s − 1 − p)/p, c = c(p) (the lattice constant; the continuum density is unchanged);
- the shifted Szegő exponent **β′ := α + 2δ** (= α − 2Z(0) − 1, where Z(0) = ζ(0, a) = −½ − δ);
- the band-factor parameters μ^δ_{n,j} := 2m_j(δ)n^{jp}, where m_j(δ) is given by the Fourier sum of §3.2
  (= ζ(−jp, a)/(jn^{jp}), Remark 3.3).

**Theorem H (target; status per §4).**
- (i) *Reduction.* For every K, J, B, the expansion of n^pb_n(σ^δ)/c is the double expansion of Theorem N.6(i) for the
  **decoupled model M(β′, ν = α)** (JZC_M4 §7): Bessel order α, Szegő exponent β′, the lattice g-function and n^p scaling,
  degree n, band factor exp(−Σ_jμ^δ_{n,j}z^j). The remainder is O(n^{−K−1} + n^{−2−(B+1)p} + n^{−1−(J+1)p}).
- (ii) *Natural form.* With N := n + (β′+1)/2 = n + α/2 + ½ + δ (so −Z(0) = ½ + δ):

  n^pb_n/c = (n/N)^p[1 + f₂N⁻² + f₄N⁻⁴ + Σ_jε_j(a)N^{−1−jp}(1 + g_jN⁻²) + …]

  - f_{2k} = f_{2k}(p, α) are the lattice integer-layer coefficients (JZC_M4 §5): the integer layer does not depend on δ in N;
  - ε_j(a) = C(2j, j)pc^jζ(−jp, a);
  - g_j(p, α) are the lattice dressings (JZC_M4 §6).

  This is **rule H** (SPEC §3.11(a)) at the orders of Theorem N.6, with the β′-independence of the natural form supplied by
  JZC_M4 Prop S. That is exact algebra for the integer layer to order 4, and for the zeta layer at first order (j ≤ 3) by §3.3;
  beyond that it is Conjecture Σ.

## 2. Structure of the proof

| step | content | source | status |
|---|---|---|---|
| H-a | interpolation with sin π(t − δ) and 1/Γ(t − δ); node masses; top node X₁ = (n/a)^p | Paper 2 L5.1–5.2, with t ↦ t − δ | JZC_M3a_H_Ha.md (PROVED-mod-cite, NOT REVIEWED) |
| H-b | outer scalar j_δ: sectors and bounds, via the shift identity j_δ(t) = j(t−δ) + (t−δ−½)Log(1−δ/t) + δ and Paper 2's Binet bound (no DLMF 5.11.8 needed) | Paper 2 L6.1, L6.4; H-d §2 | p > 1: G12 L1.1–C1.5; p < 1: G3 Lemmas 1–3, Prop 4 (PROVED-mod-cite, NOT REVIEWED) |
| H-b′ | a-priori bound and L² boundary values for the normalised Q♮, lattice exponent \|α\|/2 (column factorisation) | Paper 2 App C | p > 1: G12 L2.1–P2.4 (PROVED-mod-cite, NOT REVIEWED); p < 1: OPEN (= H-d (iv) for p < 1; G3 Cor 5 covers H-d (i)–(iii) only, fixed per Rule R review A of G3, F1) |
| H-c | band factor: Binet-cut B_δ (p > 1) or seam χ_δ (p < 1); moments m_j(δ) as Fourier sums | E_pgt1 L E.2, E3 L F.1′, E_plt1 L F.1, SPEC §3.1 | §3.2 |
| H-d | index transfer: F_δ ∼ C_δ(−z)^δ at ∞, absorbed by the gauge (−z)^{−δσ₃}; result M(β′, α) | JZC_M3a_Hd.md | jump algebra PROVED (NOT REVIEWED); analytic inputs G1–G3; for p < 1, G3 Cor 5 gives H-d (i)–(iii), not (iv) (fixed per Rule R review A of G3, F1) |
| H-e | circle jumps, small norm, residue recursion for M(β, ν) | JZC_M4_proof Lemmas N.6a–c (β enters only through ρ² = φ^{2(β+1)}, bounded and analytic on the circles) | §3.3 |
| H-f | exact algebra for M(β, ν); natural form | m4_shift_exact, m3a_g5_exact | §3.3 |

## 3. Gaps closed here

### 3.1 G4: citations
- **DLMF 5.11.8** (read 2026-10-21, dlmf.nist.gov/5.11, from the TeX alttext): "Ln Γ(z + h) ∼ (z + h − ½) ln z − z + ½ ln(2π) +
  Σ_{k=2}^∞ (−1)^kB_k(h)/(k(k−1)z^{k−1})", in the group of expansions introduced by "As z → ∞ in the sector |ph z| ≤ π − δ".
  It is used with h = −δ fixed, for j_δ(t) = LnΓ(t − δ) − (t − δ − ½)ln t + t − ½ ln 2π = O(1/t) as t → ∞ in |ph t| ≤ π − δ₀. That
  is the hard-edge statement of H-b: nothing changes at 0. **Superseded (G12 L1.1, G3 Lemma 3):** the exact shift identity
  j_δ(t) = j(t−δ) + (t−δ−½)Log(1−δ/t) + δ reduces every bound on j_δ to Paper 2's own Binet bound on j, so the proof no longer
  uses DLMF 5.11.8. The quotation is kept for the record only.
- **Hurwitz's formula (DLMF 25.11.9) is NOT QUOTED.** No source we could read in full shows it: the DLMF page truncates before
  25.11.9 under our fetcher, and the Wikipedia text has the formulas stripped. Theorem H is therefore stated with the band-factor
  moments as the explicit Fourier sums that the proof produces (§3.2). The identification with ζ(−jp, a) is Remark 3.3:
  classical, and NUMERICAL to 10⁻²⁷ (spec_hurwitz_moments*.out).

### 3.2 The band-factor moments as Fourier sums (H-c)
SPEC §3.1 (p > 1) and its p < 1 analogue compute the moments directly from the Binet-cut and seam integrals:
- the jump density 𝔢_δ = 2 Im Log(1 − e^{−2πi(t₊−δ)}) on the cut;
- the Mellin integral ∫_0^∞ e^{−mu}u^{kp−1}du = Γ(kp)m^{−kp} (DLMF 5.2.1, quoted in CITATIONS (DLMF-zeta, Plan 67)).

With these (SPEC §3.1, proof of Lemma H, first two steps; no Hurwitz formula needed):

  m_k(δ) := (1/2π)∫_{−∞}^0𝔢_δ(y)y^{−k−1}dy = −(p/π)Γ(kp)(2πn)^{−kp}S_k(δ),   S_k(δ) := Σ_{m≥1} sin(πkp/2 − 2πmδ)/m^{1+kp}.

This needs only DLMF 5.2.1, DLMF 25.2.1, and absolute convergence; the Fubini bound is that of E3 Lemma F.1′. Theorem H
uses μ^δ_{n,k} := 2m_k(δ), and so ε_j(δ) := C(2j, j)pc^j·(−(jp/π)Γ(jp)(2π)^{−jp}S_j(δ)) in place of C(2j, j)pc^jζ(−jp, a).
For p < 1 the seam integrals give the same Fourier sum (SPEC §3.1, "p < 1"; spec_hurwitz_moments_plt1.out).

**Remark 3.3.** By Hurwitz's formula the Fourier sum equals ζ(−kp, a)/(kn^{kp}), so ε_j(a) = C(2j, j)pc^jζ(−jp, a). This is
checked numerically to 10⁻²⁷ for p ∈ {1.25, 1.5, 3}, δ ∈ {0, −½, 0.3, 1.4} (and p < 1). NOT QUOTED under Rule C.

### 3.3 G5: the decoupled model
- Lemmas N.6a–c hold for M(β, ν) verbatim. β enters only through ρ² = φ^{2(β+1)} and the soft-edge factor φ^{−2(β+1)}, both
  analytic and bounded above and below on the circles. The sign-pattern and meromorphy arguments involve only ν (Bessel) and
  the Airy data.
- Exact algebra, identically in (p, ν, β):
  - integer layer β-free in N = n + (β+1)/2, with f_odd = 0, f₂ and f₄ in closed form, and the reflection identity of
    Theorem R, to order 4 (m4_shift_exact.out, ALL IDENTITIES HOLD). An order-6 run was stopped at its time limit after order 4;
    order 6 is NUMERICAL only (m4_shift_num.out);
  - first-order zeta layer for j = 1, 2, 3: leading coefficient C(2j, j)pj/2, no N^{−2−jp} or N^{−4−jp} term, and dressing
    A_j + B_jν² (β-free) (m3a_g5_exact.out, ALL IDENTITIES HOLD).
- Numerically: m4_shift_num.out (order 8, 108 checks), m4_shift_zeta.out (40 checks), and m3a_hd_model.out (the Hurwitz data,
  42 checks).

## 4. Status of Theorem H (2026-10-21; nothing below is REVIEWED)

**What is done.**
- *Fixed-n analytic inputs.*
  - p > 1: H-b (outer scalar, G12 §1) and H-b′ (a-priori bound, G12 §2).
  - p < 1: H-b (seam outer scalar, G3), and Lemma H-d (i)–(iii) (G3 Cor 5); H-d (iv), the a-priori bound, is item 2 below
    (fixed per Rule R review A of G3, F1).
  - −1 < δ ≤ 0 throughout (δ < 0 for p < 1).
  - Each of these is a statement for fixed n.
- *Jump algebra.* H-d (JZC_M3a_Hd.md). The Hurwitz problem is exactly M(α + 2δ, α) with Hurwitz band factor, in the n^p frame.
- *Algebra of the model.* H-f to order 4 in 1/N and first order in the zeta layer (j ≤ 3), identically in (p, ν, β) (§3.3).

**What is still open for (i)**, in order of difficulty:
1. ~~**The n-uniform hard-edge comparison with Szegő exponent β′**~~: **done for p > 1** in JZC_M3a_H_G1u.md (PROVED-mod-cite,
   NOT REVIEWED).
   - The comparison runs in the α-frame. β′ enters only through ρ♮ = ρ^{(α)}/G, which is bounded above and below on the fixed
     disc uniformly in n, for every real β′. The lip limit is e^{∓iπβ′}e^{±2πiδ} = e^{∓iπα}, which matches Bessel order α.
   - The a-priori bound is G12 P2.4.
   - Prop G1u (A): Paper 2 §7 holds verbatim.
   - Prop G1u (B): the order-K small-norm expansion (N.6c) holds, with remainder O(n^{−K−1} + n^{−1−(J+1)p}). It is
     conditional on H-a (now done) and on item 5.
   - Checks: m3a_g1u_hardedge.out (110 checks incl. 34 controls; the circle jump is I + Δ₁♮/n + O(n⁻²) at β′ down to −2.2)
     and m3a_g1u_endtoend.out (29 checks incl. 8 controls: fitted Hurwitz Jacobi coefficients at β′ = −2.1, −1.5 match
     M(β′, α); the alternatives are excluded by 10⁴–10⁵ tolerances).
   - The local analysis at 0 holds for p < 1, but the p < 1 case is conditional on items 2–3 and on E_plt1's glued parametrix
     with W̃♮.
   - Still OPEN: α ≥ 1, in-lens identification. That is outside the Setting (|α| < 1).
   - A naive β′ treatment fails: the bound |z|^{−|β′|/2} is not L² when |β′| ≥ 1.
2. **H-b′ for p < 1** (Paper 2 App C in the seam geometry). The Hurwitz sum bound G12 L2.1 is p-free, so the expected route is
   L2.1 + L2.3 with the seam lens. This is H-d (iv) for p < 1, which G3 Cor 5 no longer claims (fixed per Rule R review A of
   G3, F1); in progress in JZC_M3a_H_G23plt1.md.
3. E_plt1 Lemma F.1(iv) with the complex seam densities of G3 (expected verbatim; not checked line by line).
4. ~~H-a written out~~: done in JZC_M3a_H_Ha.md (PROVED / PROVED-mod-cite, NOT REVIEWED; m3a_ha_interp.out, 298 checks and
   33 controls that fail as required). It needs Paper 2's T1(a) re-proved at the top node, since x₁ = a^{−p} > 1; the
   expansion holds for |z| > X₁ = (n/a)^p. It also shows why δ > 0 is excluded: the point t = δ is a phantom node, with no
   mass on it, and pole removal fails there.
5. **H-c, the band-factor gauge with Hurwitz moments** (E_pgt1 L E.2–E.3 / E_plt1 L F.1 for H_n^δ: the expansion of the
   band factor in μ^δ_{n,j} = 2m_j(δ)n^{jp} with uniform remainder). The moments themselves are §3.2. The gauge lemma is
   restated for δ but not yet re-proved line by line.

**Status by part.**
- **(i)** is CONDITIONAL on the open items 2, 3 and 5 above (item 1 is done for p > 1; for p < 1 it also needs items 2–3). Every other ingredient is PROVED-mod-cite (Paper 2, E-series lemmas) and NOT
  REVIEWED. Numerically, (i) is confirmed against all stored Hurwitz fits (m3a_hd_model.out, 42 checks; m3a_g3_model.out, 25
  checks, p < 1).
- **(ii)** follows from (i) and Prop S at the exact orders: the integer layer to N⁻⁴ and the first-order zeta layer with its
  N⁻²-relative dressing, j ≤ 3, at every β. The orders where Prop S is exact do not cover the full remainder of Theorem N.6, so
  beyond them (ii) is CONDITIONAL on Conjecture Σ, with NUMERICAL support to order 8 (m4_shift_num.out, 108 checks) and for
  the zeta layer (m4_shift_zeta.out, 40 checks).
- **Band-factor constants.** These are the Fourier sums S_j(δ) (§3.2), unconditionally. The identification with ζ(−jp, a) is
  Remark 3.3 (classical; NOT QUOTED under Rule C).

**Not covered:** δ > 0 (phantom nodes); p = 1 with δ ≠ 0.

**Rule R reviews (2026-10-21):** JZC_M3a_H_G12.md, reviewer A (research/G1/review/REVIEW_JZC_M3a_H_G12_A.md): ACCEPT WITH
FIXES (no mathematical error; F1–F6 MINOR/INFO, applied). JZC_M3a_H_G3.md, reviewer A (research/G1/review/REVIEW_JZC_M3a_H_G3_A.md):
ACCEPT WITH FIXES (one MAJOR scope fix, F1: Cor 5 restricted to H-d (i)–(iii); F2–F9 MINOR, applied). Neither memo is REVIEWED
yet: a second reader who re-runs the checks is pending.

**For FIXES (via a human; Rule 1):** two wording gaps in Paper 2. (1) Binetcut (iv), (O5) at ∞. The text says "where 𝔟′ is bounded";
the argument needs |𝔟′(y)| ≤ C/|y|, which Paper 2's own proof of (ii) supplies (G12 §4 item 6). (2) Lemma seam (iv), (O5) at ∞
(app_outer.tex, last lines of (O5)): "In S_in ∩ {|z| ≥ n^p+δ′} … D, B_in, K and e^χ are bounded above and below by powers of |z|"
is not justified for e^χ there (Lemma corner (ii) gives only a log² bound, away from the seams); the claim is true by a window
argument (G3 Lemma 3 (ii′), (iii′); G3 §6 item 9) (added per Rule R review A of G3, F2). The results are unaffected.

**Corrections to JZC_M3a_Hd.md** (G12 §5): (2.1) needs no DLMF 5.11.8; the monodromy step in (2.4) is replaced by Lemma
normalisation; the vertex is X₁ + δ′ = (n/a)^p + δ′; §3(iv)'s identity [·] = (4c/Υ)^δe^{±iπδ} holds in ℂ_± with principal
branches (arg Υ ∈ (0, π) in ℂ₊), and only its modulus |G| = |4c/Υ|^δ is used (fixed per Rule R review A of G12, F3). No claim of
the memo was found false.
