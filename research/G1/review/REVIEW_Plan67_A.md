# Rule R review: Plan 67, reviewer A (analysis): E_plt1.md, (E) for pure powers with 0 < p < 1

Reviewer: independent second reader (Rule R), reviewer **A**. My remit is the **analytic validity** of the proof and of
the optimality claim. Reviewer B re-derives the explicit constants (A_r^{lin}, C₀^{lin}, w⁽¹⁾, the a-functional, the
chain algebra) separately.
- Branch `plan-67-E-plt1`, commits d0f67bb, 2d7f6f4 (diff against a5cce25).
- Target: research/G1/RH/second_order/E_plt1.md (§§0–11), the checks check_e_plt1_flat and check_e_plt1_num, and the
  CITATIONS.md entries "(DLMF-zeta, Plan 67)" and "(Plan 67 reuse)".

**Internal inputs I re-read:**
- papers/paper2/app_outer.tex §"The case 0 < p < 1": Lemma seam (i)–(iv) with (eq. Lpm), (eq. chi), (eq. F-seam) and the
  (O3)/(O4)/(O5) proofs; Lemma corner (i)–(iii).
- papers/paper2/sec_6.tex: (eq. szego), (eq. szego-repr), (eq. DW-factor), (eq. omega), Lemma szego (i)–(vi), (eq.
  omega-root), (eq. omega-root-band), (eq. airy).
- papers/paper2/sec_5.tex: standing assumptions, (eq. thetaw), (eq. angles), Lemma invariance, (eq. imtheta).
- research/G1/RH/plt1/RH_plt1b.md §§0–3 (REVIEWED).
- E_pgt1.md Lemma E.3, Prop. E.5′ (final text, with the Plan 65 fixes A1–A4), §7, §10 "Large α".
- REVIEW_Plan65_A.md (format, and findings A1–A4, to check that their analogues are handled here).

**External sources.** I fetched dlmf.nist.gov/5.2, /25.2 and /25.4 myself (2026-10-15, curl) and read the TeX alttext:
- 5.2.1 is Γ(z) = ∫₀^∞e^{−t}t^{z−1}dt with the condition Re z > 0;
- 25.2.1 is ζ(s) = Σn^{−s} under "Re s > 1";
- 25.4.1 is ζ(1−s) = 2(2π)^{−s}cos(½πs)Γ(s)ζ(s) under "s ≠ 0, 1".

All three match the "(DLMF-zeta, Plan 67)" entry verbatim, and the hypothesis checks recorded there are correct. For the
Bessel/Airy entries reused through "(Plan 67 reuse)", I rely on my Plan 65 reading (REVIEW_Plan65_A §3). I re-checked the
new sector arithmetic for the rays at π − θ_L myself (§2.3 below).

I did not edit E_plt1.md.

## Overall verdict: **ACCEPT WITH FIXES** (analysis)

I found **no critical or major gap**. The new analytic ingredient, Lemma F.1, is correct and cleanly proved. The moment
identity is an exact identity between convergent integrals: no regularisation enters, for any k ≥ 1. The mechanism is
rigorous: the global parametrix is weight-blind in the Q-frame, so the n^{−p} variation of H_n enters only through Δ₁/n.
Every non-circle jump of R is super-small. The optimality claim (ε = p) is correct.

I list four fixes, all minor (wording or one-line extensions), plus three INFO items:
- **A1** is the one place where a stated bound does not cover a use: the chain remainder needs E_n on the negative axis.
- **A2** and **A3** are citation and bookkeeping precision.
- **A4** is a scope nit on n ≥ n₀.

| Statement | Verdict (analysis) | Fixes |
|---|---|---|
| Lemma F.1 (seam band factor; ζ(−kp) moments) | ACCEPT WITH FIXES | A1 (extend last clause of (iv) to x < 0), A4 |
| Lemma F.2 (D_q²/q = e^{λ𝓡}) | ACCEPT | — |
| Lemma E′.3 (circle jumps; Δ₁ = Δ₁^{mod} + λ_nΔ₁^{lin} + O(n^{−2p})) | ACCEPT WITH FIXES | A2 |
| Lemma E′.5 (meromorphy, structural; pole orders) | ACCEPT (structural part; Laurent values left to B) | — |
| Prop E′.5′ (second-order small norm, O(n⁻² + n^{−1−2p})) | ACCEPT WITH FIXES | A3 |
| Theorem E′.1 (b_n, α_n; α_n/(2b_n) with no n^{−1−p} term) | ACCEPT WITH FIXES (analysis); PROVED-mod-cite once A1–A3 are applied and B accepts the constants | A1–A3 |
| Optimality (ε = p sharp) | ACCEPT | — |
| Cor E′.6 (chain) | ACCEPT WITH FIXES | A1 |
| §2 (mechanism / bookkeeping), §9 consequences, §10 GAP, §11 Rule A log | ACCEPT | INFO I1 |
| Remark F.3 (NUMERICAL + HEURISTIC) | ACCEPT as labelled; not used anywhere in a proof (checked) | — |
| Rule C (DLMF-zeta; Plan 67 reuse) | ACCEPT | — |
| Numerics (check_e_plt1_flat, check_e_plt1_num) | ACCEPT (reproduced byte for byte; the single miss is benign; NUMERICAL, not used) | I2, I3 |

## 1. Re-runs (Rule N)

Python: the jacobi-asymptotics `.venv` with `PYTHONPATH=src` (worktree src). The csrc binaries were already built.
- **check_e_plt1_num.py** (from the committed Plan 62/67 cache in tmp/plan62_cache): the output is **byte-identical** to
  checks/check_e_plt1_num.out, with 131/132 rows "ok".
  - Because the script reads cached coefficients, I also **recomputed from scratch** (fresh cache, binary128 RKPW,
    K = 3.2·10⁵, n ≤ 1600) the cases (p, s) = (0.9, 1.5) and (0.5, 2).
  - The fresh α_k and b_k agree with the cached files to max|Δα| = 5·10⁻³⁷ and max relative |Δb| = 5·10⁻³⁶. So the
    cache is what it claims to be.
- **check_e_plt1_flat.py**: 8 min. The output is **byte-identical** to checks/check_e_plt1_flat.out.
  - [A]: the first seam moment equals ζ(−p)n^{−p} to ≤ 2·10⁻⁴¹ at p = 0.3, 0.5, 0.7, 0.9.
  - [B]: n^{2p}·r₁ → ζ(−2p)(z²−1)/2 and n^{3p}·r₂ → the k = 3 term, in S_in and S_out, at p = 0.5, 0.7.
  - At p = 0.3 the convergence is slow, as expected. The gap r₁ − pred₂ at n = 640, z = 0.2 is 0.0051 = r₂·n^{−p}
    (0.0355·640^{−0.3}): the next term, exactly as the asymptotic series predicts.
- **My own probe** (not committed). This is a test of Lemma F.1(ii) at the places check_e_plt1_flat does not sample:
  points straddling the seam (arg z = θ_s ± 0.02 at |z| = 0.8; θ_s ± 0.05 at |z| = 0.05; θ_s + 0.01 at |z| = 3) and
  z = −0.3, with p = ½, n = 40.
  - I evaluated the literal 𝒢(z) − 𝒢(1) (the script's quadrature of χ from Paper 2's χ±) against the right side 𝒥(z)
    of (F.1), which I computed independently by quadrature of ℓ against K.
  - They agree to 10⁻²⁰–10⁻³⁰ (1.6·10⁻⁷ at |z| = 3, where the quadrature near the seam is the limit).
  - n^{2p}|𝒢(z) − 𝒢(1) − ζ(−p)(z−1)n^{−p}| is 0.04–0.05 at all the near-seam and near-0 points, i.e. O(n^{−2p}) uniformly.

**The single miss, at (p, s) = (0.9, 1.5)** (chain, 1/n coefficient; |diff| 5.9·10⁻⁸ against a half-range of 5.4·10⁻⁸
and dK = 4·10⁻⁸). It is benign:
- *Size.* The prediction is a = (2s−2−p)/(2p) = 1/18. The miss is a relative error of 1·10⁻⁶, while the b- and
  a-coefficients at the same (p, s) match to 3·10⁻¹⁰.
- *The fit basis is near-degenerate at p = 0.9.* The exponents are 1, 1.9, 2, 2.8, 2.9, 3, … (pairs 0.1 apart). I refitted
  the same g-sequence with J = 4…10 exponents and windows f = 0.1, 0.2, 0.3, 0.5. The estimate of (coef − a) moves
  between +6·10⁻⁹ and +2·10⁻⁶ (J = 4…7, f ≤ 0.3), and it shrinks when K is doubled (e.g. J = 4, f = 0.1: 1.4·10⁻⁸ → 6·10⁻⁹;
  J = 5: 4.9·10⁻⁸ → 3.6·10⁻⁸).
- *Interpretation.* The half-range of the 12 production fits underestimates the real fit and truncation uncertainty here.
  The deviation is a truncation/fit bias that decreases with K, not a signal.
- *Why this point.* α = −0.44 at (0.9, 1.5), so the continuum-tail truncation is largest there.

§8's reporting ("131 of 132", with the exception named and quantified) is honest. See I3 for a wording suggestion.

## 2. Analytic verification, item by item

### 2.1 Lemma F.1 (the item asked about hardest)

**(i) The jump.** I re-derived it from Paper 2 (eq. Lpm) and Lemma seam (iii).
- On Γ₊: 𝒢_out − 𝒢_in = ½Log(1 − ζ/2πn) + χ_out − (−j + ϖLog(1+ζ) + χ_in) = ½Log(1 − ζ/2πn) + j − ϖLog(1+ζ) + χ₊.
  With χ₊ = −j − Log(1 − e^{−2πit}) + ϖLog(1+ζ) − ½Log(1 − ζ/2πn), this sums to −Log(1 − e^{−2πit}).
- On Γ₊, arg t = −π/2, so e^{−2πit} = e^{−2π|t|} ∈ (0, 1) and the jump is ℓ(|ζ|) > 0. Γ₋ follows by the conjugation
  symmetry.
- The boundary values of −j(t(z)), Log(1+z) and Log(1 − z/2πn) from either side are the values at ζ, since j is analytic
  off (−∞, 0] and arg t = ∓π/2 on Γ±. So the computation is legitimate for boundary values, not only formally.
- Analyticity in each sector is correct. In S_in, |arg t| < π/2. The cut (−∞, −1] of Log(1+z) is in S_out. The cut
  [2πn, ∞) of Log(1 − z/2πn) is in S_in, where that term is not used.
- Boundedness near 0 holds: j(t) → 0 by (binet-bound), B_in, B_out → 1, and χ is bounded by corner (iii).

**(ii) The Liouville/Cauchy representation.** Correct.
- K(ζ, z) = 1/(ζ − z) − 1/(ζ − 1). So 𝒥 is the Cauchy transform of ℓ over the two rays, with the same orientation and sign
  convention as Paper 2's χ, made convergent by subtracting its value at 1 (ℓ ~ log r at ∞).
- Plemelj gives 𝒥_out − 𝒥_in = ℓ on both rays. This is the same bookkeeping as Lemma seam (iii), which I checked there:
  Γ₊ has S_out on its left, and Γ₋ carries the minus sign.
- K₀ = 𝒢 − 𝒢(1) − 𝒥 is therefore continuous across the seams, analytic off them (Morera), and bounded near 0. It is
  bounded near 0 because 𝒥 is: the density vanishes to infinite order at the corner.
- The growth argument needs only that the L¹ means of |K₀| on |z| = ρ grow like o(ρ). The proof gives O_n((1 + log ρ)²),
  with ample room, so K₀ is constant, and K₀(1) = 0.
- My probe (§1) confirms (F.1) numerically to 10⁻²⁰ on both sides of a seam and on S_out.

**(iii) The moments: is the identity valid for all k, given that ζ(−kp) "arises via regularisation"?** Yes. There is no
regularisation in the proof.
- m_k is an absolutely convergent integral for every k ≥ 1, p > 0. ℓ(r) ≤ 2e^{−2πnr^{−1/p}} near 0, and
  ℓ(r) = O(1 + log r) against r^{−k−1} at ∞.
- The orientation gives m_k = −(sin(kθ)/π)∫ℓ r^{−k−1}dr. I re-did the substitution u = 2πnr^{−1/p}:
  ∫ℓ r^{−k−1}dr = p(2πn)^{−kp}∫(−log(1−e^{−u}))u^{kp−1}du.
- Tonelli + 5.2.1 (Re kp > 0) + 25.2.1 (Re(1+kp) > 1) give Γ(kp)ζ(1+kp). All quantities here are positive and finite.
- The value ζ(−kp) enters only by **renaming** ζ(1+kp) through the reflection formula 25.4.1 at s = 1 + kp ≠ 0, 1. That
  formula is an identity of the analytic continuation, valid for every such s.
- I re-derived ζ(−kp)/k = −(2π)^{−kp}sin(πkp/2)pΓ(kp)ζ(1+kp)/π, hence m_k = ζ(−kp)/(kn^{kp}).
- When kp ∈ 2ℕ, both sides vanish (sin = 0 and the trivial zero of ζ), consistently.
- The "zeta-regularised product" of Remark (1) is an *interpretation* of the constants, not an input. I1 suggests saying
  so.

**(iv) Uniformity, including the seam boundary values.** Correct.
- *Far part.* For |ζ| ≥ 2R₁, the geometric-series remainder of K is O(|ζ|^{−K−2}) uniformly in |z| ≤ R₁, with no
  dependence on the distance to the seams. Its integral against ℓ is exactly the (K+1)-moment, of size n^{−(K+1)p}.
- *Near part.* r ≤ 2R₁, where ℓ ≤ 2e^{−2πn(2R₁)^{−1/p}} uniformly. The constant-subtraction window around the nearest
  seam point z* has |ζ − z*| ≤ |z*|/2 ≤ R₁/2, so it stays inside r ≤ 2R₁. ℓ(|z*|) and ℓ′ are e^{−cn} there. Off the window,
  |ζ − z| ≥ (|ζ| + |z*|)/C. So the near part is O(e^{−cn}) including boundary values.
- The kernel's second pole 1/(ζ − 1) is harmless: |ζ − 1| ≥ sin θ_s on the seams.
- The derivative bounds are correct.
  - Cauchy's estimate holds away from the seams.
  - On the positive axis, |ζ − x| ≥ sin θ_s·max(|ζ|, x) for ζ on a seam.
  - For p < 1, c(p) ≤ ½, so 4c ≤ 2 < R₁/2 = 2c + 1. The last clause therefore covers the whole band, and the analogue of
    Plan 65's A1 does **not** arise here.
  - The ∂U_r crossing point 4c − ε is at distance (4c − ε)sin θ_s from the seams and inside |z| ≤ R₁ − 1, so the
    Cauchy-estimate clause covers it.

**The cancellation that Paper 2's (O3) bound misses.** §2 item 2 is right.
- (O3) bounds the three terms −j(t), ϖLog(1+z), χ − χ(0) separately: O(|z|^{1/p}/n), O(|z|), O(|z|log(1/|z|)).
- Their sum is O(n^{−p}) uniformly. Only the jump ℓ is n-small, and the representation (F.1) sees only the jump.
- This is the exact analogue of E_pgt1's −j / log B cancellation.

### 2.2 Lemma F.2

Correct. I re-derived it from (eq. szego-repr) with 𝔠 = log q(z) = −λz: the integrand becomes λ(z − x)/(z − x) = λ, and
∫₀^{4c}dx/√(x(4c−x)) = π. So D_q²/q = e^{λ𝓡}. This holds for every z ∉ [0, 4c]; analyticity of q is used only through
the explicit continuation e^{−λz}.

The consequences are right, and the signs agree with §11's Rule A note:
- ω^λ = ω^{mod}e^{λ𝓡} and ρ^λ = ρ^{mod}e^{−λ𝓡/2}, since ρ² ∝ 1/ω.
- The constant H_n(1)e^{λ_n} cancels in ω (D_q = q^{1/2} for constant q).

### 2.3 Lemma E′.3

**Sectors with rays at π − θ_L** (θ_L = πp/4). The geometry is consistent:
- f is conformal at 0 with f < 0 on (0, δ). So the lens |arg z| < θ_L maps to the Hankel sectors π − θ_L < |arg ζ| ≤ π.
- The seams (|arg z| = θ_s > θ_L) and the negative z-axis lie in the I/K sector |arg ζ| < π − θ_L.

The DLMF hypotheses hold:
- In |arg ζ| < π − θ_L, w = 2ζ^{1/2} has |ph w| < π/2 − θ_L/2. That is inside 10.40.1/10.40.3 (|ph| ≤ π/2 − δ, δ = θ_L/2)
  and 10.40.2/10.40.4 (|ph| ≤ 3π/2 − δ).
- In π − θ_L < ±arg ζ < π, ph 2(−ζ)^{1/2} ∈ (∓θ_L/2, 0). That is inside 10.17.5/.11 (−π + δ ≤ ph ≤ 2π − δ) and
  10.17.6/.12 (−2π + δ ≤ ph ≤ π − δ).
- The closed sectors overlap, so the expansions are uniform up to the rays.
- KMVV's angle freedom (CITATIONS "(KMVV, angle freedom; Plan 15b)") changes only where the same special-function
  formulas are used, not the formulas.
- Paper 2's θ_lip = 𝗆·πp/4 with 𝗆 = 1 for ℓ₁ ≡ 1, so θ_lip = θ_L: the frames agree inside U_0. This is the analogue of
  Plan 65's A4, handled here.

**The n-dependence.** Correct.
- ω = ω^{λ_n}·D²_{q₂}/q₂ and ρ² = (ρ^{λ_n})²q₂/D²_{q₂}, with q₂ = e^{−2E_n}. These follow from H_n = H_n(1)e^{−λ_n(z−1)}e^{−2E_n}
  and the multiplicativity of D. On ∂U_0, "the sector value" of E_n is exactly what the glued W̃ requires.
- (eq. szego-repr) with 𝔠 = −2E_n(z) holds for any number 𝔠. Together with |E_n| ≤ Cn^{−2p} (sup, boundary values
  included) and the derivative clause near the two band crossings δ and 4c − ε, it gives log(ω/ω^{λ_n}) = O(n^{−2p})
  uniformly on both circles.
- Δ₁⁰ is linear in ρ^{±2}, and Δ₁^r is analytic in (−ω)^{±1/2}. Δ₁^λ is analytic in λ with bounded λ-derivatives on the
  circles. Hence Δ₁ = Δ₁^{mod} + λ_nΔ₁^{lin} + O(λ_n² + n^{−2p}) = … + O(n^{−2p}).
- The seam glue changes the prefactor by O(e^{−c′n}) at the two points where ∂U_0 crosses the seams. That is inside
  O(n⁻²).

One citation imprecision: see A2.

### 2.4 Lemma E′.5 (structural meromorphy)

I re-did the jump computation.
- On (4c − ε, 4c): P₊ = P₋J, φ̃₊ = −φ̃₋, d₊ = 1/d₋ for d = (−ω^λ)^{1/2}. The λ-factor qualifies because 𝓡₊ = −𝓡₋.
- J d^{σ₃}J^{−1} = d^{−σ₃}.
- For X = [[−1/72, −i/12], [−i/12, 1/72]] one has JXJ^{−1} = [[1/72, i/12], [i/12, −1/72]] = −X.
- These give Δ₊ = Δ₋.
- On (0, δ), the same computation goes through with f^{1/2}₊ = −f^{1/2}₋, (ρ^λ)²₊(ρ^λ)²₋ = 1 and JQ₀J^{−1} = −Q₀. I checked the
  last identity on Q₀ = [[−(1+4α²), −2i], [−2i, 1+4α²]].
- On (−δ, 0), the model ρ² = C(−z)^α(4c−z)/(D²_{x^α}D²_{4c−x}) (times e^{−λ𝓡}) is analytic, since D_q is analytic off
  [0, 4c]. The text's ratio formulation is equivalent.
- φ̃ = u³·(analytic) is analytic on (4c, 4c + ε), as is (−ω)^{1/2} (Paper 2 (eq. omega-root)).

The growth bounds are right:
- |Δ₁^r| ≤ C|z−4c|^{−3/2}·|z−4c|^{−1/2}, so the pole at 4c has order ≤ 2.
- |Δ₁⁰| ≤ C|z|^{−1/2}·|z|^{−1/2}, so the pole at 0 has order ≤ 1.
- Differentiating in λ preserves the pole orders: the Laurent coefficients are analytic in λ.

This structural argument is sound. It also supplies the reason for the vanishing of odd powers that E_pgt1 verified only by
series. The Laurent values are B's remit.

### 2.5 Prop E′.5′ (second-order small norm)

I went jump by jump for the p < 1 frame. None of the non-circle jumps is larger than O(e^{−n/C}) or O(n^{−pn/4}).

- **Lips, Σ_v, saturated segment, Σ^△, top.** Paper 2 F5 holds for all p > 0 (the standing assumptions fix only p > 0 and
  α < 1, see A3). RH_plt1b §2 places all these pieces inside S_in. On them |J − I| ≤ Ce^{−n/C}, resp. Cn^{−pn/4}.
- **Seams outside U_0.** There is no jump: F is analytic across the seams (Lemma seam (iv)), and P₀^∞ is seam-free.
- **Inside U_0: lips.** The mismatch involves |e^{∓2iθ}| = exp(−2πn|z|^{−1/p}sin(θ_L/p)) with sin(π/4). The amplification
  by P̂₀ is poly·e^{Cn|z|^{1/2}}, so the product is ≤ exp(−n(2π sin(π/4)δ^{−1/p} − Cδ^{1/2})), exponentially small for
  small δ.
- **Inside U_0: seams (glue).** The jump is W̃_out/W̃_in = 1 − e^{∓2πit}, with |e^{∓2πit}| = exp(−2πn|z|^{−1/p}), amplified
  in the same way. It is exponentially small.
- **(−δ, 0).** For p < 1 it lies in S_out, where W̃ = (C(−z)^α(4c−z))^{1/2}/(B_oute^χ) is analytic, so there is no jump.
  This is a simplification compared with p > 1.
- **Inside U_r and on the band outside the discs.** There is no jump, as in E_pgt1.
- **The Cauchy operator.** ‖𝒞₋‖ is bounded uniformly on the n-dependent contour (Paper 2 F1: n-independent geometry inside
  the discs, plus translates of a fixed Carleson curve).
- **Circles.** J − I = (Δ₁^{mod} + λ_nΔ₁^{lin})/n + O(n⁻² + n^{−1−2p}) uniformly. So the first Cauchy integral equals the
  residue sum plus O(n⁻² + n^{−1−2p}), at distance ≥ d and for the moments R_1, R_2. The far pieces carry |s|^{k−1} ≤ Cn^p,
  which the exponentials absorb. The quadratic term is O(n⁻²).
- **R(0).** For z → 0 along (−δ, 0), the seam pieces near 0 satisfy |s − z| ≥ max(|s|, |z|), since the angle between a
  seam and the negative axis is π − θ_s > π/2. The lip pieces satisfy |s − z| ≥ c·max(|s|, |z|). So E_pgt1's
  dominated-convergence argument (its A2 fix) applies verbatim, now including the seams.

**Range of s.** §0's "Range of s" bullet covers the Plan 65 A3 issue: the Paper 2 inputs do not use α < 1, and the seam
scalar does not involve s. I agree. Lemma seam and Lemma corner contain no s at all, and F1/F5 depend only on the geometry
and on Lemma szego (vi)(b),(c), signs and gfunction. RH_plt1b states its theorem for every s > 1. See A3 for the one
bookkeeping point.

### 2.6 Extraction: why the n^{−p} change of H_n enters only via Δ₁/n

The argument is rigorous.
- Q₁ = P₁ + R_1 and Q₂ = P₂ + R_1P₁ + R_2, with P₀^∞ = T𝔞^{σ₃}T^{−1} weight-free and n-free in the Q-frame. The weight
  reaches Q only through D_W^{σ₃} on the right and D_∞^{−σ₃} on the left, which Lemma invariance removes exactly; I
  re-read its proof. So b(P₀^∞) = c² and a(P₀^∞) = 2c exactly, for every n and every band weight.
- Everything weight-dependent sits in R − I, whose jump is O(1/n) on the circles and super-small elsewhere. So a change
  δW of the weight costs at least a factor 1/n:
  - λ_nΔ₁^{lin}/n → n^{−1−p};
  - the O(λ_n²) and O(n^{−2p}) parts of Δ₁ (including F.1's remainder E_n, through q₂) → O(n^{−1−2p});
  - the quadratic small-norm term → O(n⁻²).
- The functionals are polynomial in the entries of R_1, R_2. The cross terms of a λ_n/n term with a 1/n term are
  O(n^{−2−p}).
- I checked the b-part myself. (Q₁)₁₂(Q₁)₂₁ = (ic + R₁₂)(−ic + R₂₁) = c²(1 + i(R₂₁ − R₁₂)/c + O(|R|²)). With
  A₂₁ − A₁₂ = c²p(iα − i(α+2)) = −2ic²p for A_r^{lin}, the λ_n-part is 2cpλ_n/n. So n^pb_n/c gains cpλ_n/n = κ_pn^{−1−p},
  κ_p = 2pcζ(−p).
- The a-part and A_r^{lin} itself are B's remit.

### 2.7 Optimality (ε = p) and the sign of κ_p

Both claims are correct.
- *Sign.* By 25.4.1 at s = 1 + p, ζ(−p) = −2(2π)^{−1−p}sin(πp/2)Γ(1+p)ζ(1+p). For 0 < p < 1, sin(πp/2) > 0,
  Γ(1+p) > 0, and ζ(1+p) > 0 (25.2.1). So ζ(−p) < 0 and κ_p = 2pc(p)ζ(−p) < 0 for every p ∈ (0, 1). Numerically
  κ_{1/2} = ζ(−½)/√6 = −0.0848692, and c(½) = ¼√(8/3) = 1/√6, which I re-derived from c_p = (π/(2I))^p/4 with
  I = (√π/2)Γ(5/2)/Γ(3).
- *Is n^{−1−p} genuinely the next term?* For 0 < p < 1, 1 + p < 2 and 1 + p < 1 + 2p. So n^{−1−p} dominates both remainder
  terms n^{−2} and n^{−1−2p}, for every p ∈ (0, 1), including p ≥ ½. Nothing in the O(n^{−1−2p} + n^{−2}) remainder can
  cancel it.
- Hence n^pb_n/c − 1 − d₁/n = κ_pn^{−1−p}(1 + o(1)), and (E_ε) (SECOND §0: n^pb_n/c = 1 + d₁/n + O(n^{−1−ε})) fails for
  every ε > p. The same holds for α_n and for the chain (same κ_p).
- The cancellation in α_n/(2b_n) is exact at order n^{−1−p}. The ratio of (1 + x + κn^{−1−p}) and (1 + y + κn^{−1−p}) is
  1 + (x − y) + O(n^{−2} + n^{−2−p}). No sharpness is claimed for that ratio, correctly.
- Rule X: the sign and value are also fixed by data that predate the theory (Plan 62's p = ½ fit −0.0849 of raw b_n). This
  is legitimate corroboration.

### 2.8 Remark F.3

It is labelled NUMERICAL + HEURISTIC and "not used". I searched E_plt1 for every reference: it appears only in the
summary table, in Remark (3) after Lemma F.1 (a pointer), and in its own paragraph. No proof step uses it. Its p = 1
identity log H_n = −2Σζ(−k)z^k/(kn^k) is correct: ζ(−k) = −B_{k+1}/(k+1), and the even-k terms vanish. Its p = 3 and
p = 3/2 numbers match 4c|ζ(−p)|.

## 3. Findings and required fixes

**A1 (minor; a stated bound does not cover a use).**
- *The problem.* Cor E′.6 "Remainder" evaluates log(D²_{q₂}/q₂) at z = −v², on the **negative** axis (S_out). It cites
  F.1(iv)'s last clause, which is stated only for 0 < x ≤ R₁/2.
  - Whether one takes 𝔠 = log q₂(z) = −2E_n(−v²) or 𝔠 = −2E_n(0) in (eq. szego-repr), the v-linear coefficient and the
    claimed remainder need |E_n(−v²) − E_n(0)| ≤ Cn^{−2p}v² (or at least o(v), uniformly with an n^{−2p} constant).
  - They also need E_n(0) to be the same limit from S_in and S_out.
- *Fix.*
  - Extend the last clause of F.1(iv) to real x ∈ [−R₁/2, 0) ∪ (0, R₁/2] (S_out boundary values on the negative axis).
    The proof is verbatim: for ζ on a seam and x < 0, the angle at 0 is π − θ_s > π/2, so |ζ − x| ≥ max(|ζ|, |x|).
  - Add one sentence: E_n extends continuously to 0, with the same value from every sector, since 𝒥 is the Cauchy
    integral of a density that vanishes to infinite order at the corner.
  - Optionally weaken "O(n^{−2p}v²)" to "o(v) as v → 0 at fixed n", which is all (E.6.1) uses (only the v-linear
    coefficient μ_n, |μ_n| ≤ Cn^{−2p}, enters w⁽¹⁾).
- No constant changes.

**A2 (minor; citation precision in Lemma E′.3).**
- *The problem.* The uniform bounds of ρ^{±2} and (−ω)^{±1/2} on the circles are attributed to Paper 2 Lemma szego
  (vi)(a)–(b). (vi)(a) is stated only on Z(η*/4) ∖ (0, ∞), i.e. |arg z| < θ_w. ∂U_0 is the whole circle |z| = δ, most of
  which (including the negative axis) lies outside that sector.
- *Fix.* Replace the citation for ∂U_0 by the chain actually available:
  - ρ^{mod} is explicit and bounded above and below on |z| = δ (szego (i): D²_{x^α} = (4cz/Υ)^α, D²_{4c−x} = 4c(z−4c)/Υ);
  - e^{±λ_n𝓡/2} = 1 + O(n^{−p});
  - log(D²_{q₂}/q₂) = O(n^{−2p}), as just proved.
- Keep (vi)(b) for ∂U_r.

**A3 (minor; source of the first-order small-norm bound, and listing the seam jumps).**
- *The problem.* Prop E′.5′ (1) takes "‖R₋ − I‖_{L²} = O(1/n)" from "RH_plt1b's Theorem (RH_px §5)". RH_plt1b proves the
  first-order statement in RH_px's frame. The second-order step here runs on the Q-frame contour with Paper 2 F1's
  Cauchy bound.
- *Fix.* Do as E_pgt1 Prop E.5′ now does.
  - State ‖J − I‖_{L¹∩L²∩L^∞} = O(1/n) on this contour, listing the seam glue pieces inside U_0 explicitly with their
    bound O(exp(−n(2πδ^{−1/p} − Cδ^{1/2}))) after amplification by P̂₀, next to the lips' bound with sin(π/4).
  - Then derive ‖R₋ − I‖ = O(1/n) from F1's uniform Cauchy bound.
  - Cite RH_px §5 / RH_plt1b only for the identification of Q with the small-norm solution.
- In the R(0) remark, add that the seam pieces near 0 satisfy |s − z| ≥ max(|s|, |z|) for z on (−δ, 0), since the angle is
  π − θ_s > π/2.
- No change of substance.

**A4 (minor/INFO; range of n).**
- *The problem.* Lemma F.1 is stated "for n ≥ 1". Paper 2's Lemma corner (whose (iii) is used for boundedness of 𝒢 near 0)
  is stated for n ≥ n₀.
- *Fix.* Write n ≥ n₀ in F.1(iv) (small n are irrelevant to an asymptotic statement), or note that for fixed n the
  boundedness near 0 follows directly from (F.1)'s 𝒥 and from (i).

**I1 (INFO).** In Remark (1) after Lemma F.1, mark "the zeta-regularised value of −Σlog(1 − xm^p)" and "the regularised
square of the product over the nodes" as an interpretation (HEURISTIC). The lemma's proof uses only the convergent moment
integrals (iii); the regularised product is not defined or used. This pre-empts exactly the question the brief raised.

**I2 (INFO; check coverage).** check_e_plt1_flat [B] samples no seam boundary values and no point near 4c − ε. The proof
covers both, and my probe (§1) adds near-seam points on both sides and near 0, with (F.1) matched to 10⁻²⁰. Optionally add
two near-seam points to [B].

**I3 (INFO; numerics wording).** In §8, say that the tolerance max(half-range, dK, 10⁻⁸) is an estimate. At p = 0.9 the
fit basis contains exponent pairs 0.1 apart, and the one exception (chain 1/n at (0.9, 1.5), relative error 1·10⁻⁶) moves
by more than its half-range under J and window changes, and shrinks with K. It is not evidence against the theorem.

## 4. Things I tried to break (Rule A, reviewer side)

- **Is the n^{−p} term an artefact of the seam *construction* (a choice)?** The band factor H_n depends on the choice of
  outer scalar, but b_n does not. The proof is internally consistent: whatever H_n is, the extraction sees it only through
  Δ₁/n. The value κ_p is confirmed by raw b_n data that predate the theory (Plan 62, p = ½) and by the 12-point grid.
- **Could another n-dependent object enter at order n^{−p}?** I checked, and none does:
  - f, f_r, φ̃, the band [0, 4c] and P₀^∞ are n-independent (as in E_pgt1, REVIEWED);
  - r_n ≡ 1 and 𝗐_n is a constant for pure powers;
  - the constant χ(0) (O(log n)) cancels in ω.
- **Could the seam jumps inside U_0 cost a power of n near 0?** No. exp(−2πn|z|^{−1/p}) beats the Bessel amplification
  e^{Cn|z|^{1/2}} on U(0, δ) for small δ, uniformly down to 0.
- **Could the moment identity fail for large k (kp ≥ 1, where ζ(−kp) is "beyond the critical strip")?** No. The left side
  is a convergent integral equal to −(sin(πkp/2)/π)pΓ(kp)ζ(1+kp)(2πn)^{−kp}, and 25.4.1 holds for all s ≠ 0, 1. Only the
  asymptotic (not convergent) nature in K matters, as Remark (4) says.
- **p → 0⁺ and p → 1⁻.** No uniformity is claimed (correct).
  - As p → 1, λ_n·(1/n) ~ n^{−2} merges with d₂, consistent with §10.
  - As p → 0, n^{−1−2p} ≈ n^{−1−p}, and the fits at p = 0.3 are correspondingly loose.

**Bottom line (analysis):** Theorem E′.1, the optimality of ε = p, and Corollary E′.6 are correctly proved modulo the
cited inputs once A1–A3 (wording-level; A1 a one-line extension of Lemma F.1(iv)) are applied. Reviewer B's verdict on
A_r^{lin}, C₀^{lin}, w⁽¹⁾ and the a-functional is needed for REVIEWED.
