# Theorem RH₁: pointwise Law P for σ = Σ k^{−3/2} δ_{1/k}, by perturbing WLXZ (Tricomi–Carlitz, α = 1)

Status: written 2026-10-13. NOT REVIEWED. This is option 1 of the post-review plan (RH review, REVIEW_RH.md): finish
p = 1 first, starting with the regular weight r = 3/2.

## 0. Statement

**Theorem RH₁.** Let σ := Σ_{k≥1} k^{−3/2} δ_{1/k} (atoms x_k = 1/k, so p = 1, C = 1, and weight exponent
r = 3/2 = 1 + p/2). Its Jacobi coefficients satisfy

  a_n = a_n^{TC}(1 + O(1/n)),  b_n = b_n^{TC}(1 + O(1/n)),

where a^{TC}, b^{TC} are the explicit Tricomi–Carlitz (α = 1) coefficients:

  a_n^{TC} = 1/(2n−1) + 1/(2n) (with the n = 1 term 1/2 only), b_n^{TC} = 1/√((2n)(2n+1))

(item 11 §7: λ_m = 1/(m+1), folded). Consequently

  n b_n = ½(1 + O(1/n)) = c(1)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n).

This is the **pointwise Law P** for σ, with a rate.

Numerically (`checks/check_p1_tc.out`) the true deviation is O(n⁻²): b_n/b_n^{TC} − 1 = −1.65e−5, −4.2e−6, −1.06e−6,
−2.7e−7, −7.4e−8 and −2.5e−8 at n = 50 … 1500, with a_n the same to two digits and K-doubling stable to 6e−12.

## 1. Identification with Tricomi–Carlitz (PROVED)

- **TC (α = 1).** In the x-variable, TC(α = 1) has atoms 1/k (k ≥ 1) and masses v_k := k^{k−1}e^{−k}/k! (item 11 §7,
  α = 1, k ↦ k − 1).
- **Ratio.** σ has the same atoms with masses k^{−3/2}. So

    k^{−3/2} = √(2π)·H(k)·v_k,  H(t) := Γ(t + 1)e^t/(√(2π) t^{t+1/2}).

- **Properties of H.**
  - H is analytic and nonvanishing on ℂ ∖ (−∞, 0], since Γ(t+1) has no zeros and its poles lie at t ≤ −1.
  - By Stirling, H(t) = 1 + 1/(12t) + O(t⁻²) uniformly in |arg t| ≤ π − ε.
  - H(1) = e/√(2π) ≈ 1.084.
  - H and 1/H are bounded on {Re t ≥ ½}.
- **The constant √(2π)** does not affect monic OPs or recurrence coefficients.
- **The symmetric variable** (RH.md §1; WLXZ's setting) has atoms ±k^{−1/2} and masses halved. WLXZ's analytic weight
  is w_d(z) (their (2.15), α = 1), with t = 1/z² at the nodes. Hence our analytic weight is w_d(z)·H(1/z²), up to the
  constant. After WLXZ's rescaling z ↦ n^{−1/2}z (their (3.1)), it is w(z)·H(n/z²).

## 2. Weight-perturbation lemma

**Lemma W1.** Let w be WLXZ's rescaled weight for TC(α), and let H_n(z) := H(n/z²). Then WLXZ's steepest-descent
analysis (their §§3–6) goes through for the weight w·H_n, with the same error term O(1/n) in (6.34)–(6.36).

*Proof.* We follow WLXZ's transformations and record where the weight enters.
1. **IP and R** (WLXZ (2.14)–(3.22)). The weight appears only through w in the factors U_±, U^△_± and in the jumps
   2iγw and 2iγ/w. Replacing w by wH_n is purely algebraic. The pole cancellation (3.13)–(3.18) uses only the residue
   identity Res = w(node). That still holds, because H_n is analytic and nonzero at the nodes (n/X_k² = k + α ≥ 1).
   H_n is analytic on ℂ ∖ iℝ, which is the same domain as WLXZ's w_d.
2. **T, Q** ((4.1)–(4.13)). These are unchanged, with w → wH_n. The g-function and φ do not involve the weight.
3. **V (the D-functions, (4.14)–(5.4)).** WLXZ's D, D̃, D̂, E depend only on the nodes (via n/z² and α) and are
   unchanged. Add one more conjugation, V^H := V·D_H^{σ₃}, where D_H is the Szegő function of H_n on [−2, 2]:
   D_{H,+}D_{H,−} = H_n on (−2, 2), D_H analytic and nonvanishing on ℂ ∖ [−2, 2], D_H → D_{H,∞} at ∞. On a fixed
   neighbourhood 𝒰 of [−2, 2] (avoiding iℝ ∖ {0}), log H_n(z) = O(|z|²/n) uniformly, by Stirling, since |n/z²| ≥ n/R²
   and |arg(n/z²)| ≤ π − ε on 𝒰. Hence D_H = 1 + O(1/n) uniformly on compact subsets of ℂ ∖ [−2, 2], and
   D_{H,±} = H_n^{±1/2}(1 + O(1/n)) on the band.
4. **Jumps of V^H.**
   - (a) Band (−2, 2): WLXZ's jump [[0, w₀/D̃²], [−D̃²/w₀, 0]] becomes [[0, w₀H_n/D̃²], …]. After conjugation by
     D_H^{σ₃} it is exactly WLXZ's jump again, because D_{H,+}D_{H,−} = H_n.
   - (b) Every other jump (lens lips, saturated part, vertical segments, disc interiors) is WLXZ's jump with its
     off-diagonal entries multiplied by H_n^{±1}D_H^{∓2} (or D_{H,±}^{∓2} on the real axis).
     - On |z| ≤ R these factors are 1 + O(1/n).
     - On the long saturated pieces R ≤ |x| ≤ k_n, the factors are bounded and bounded below. There t = n/x² ≥ 1,
       so H_n and 1/H_n are bounded, and D_H is bounded since it is close to 1 off [−2, 2].
     - The entries they multiply are O(e^{−cn}) there (WLXZ (6.34), "otherwise").
   - So the modified jumps are I + O(1/n) where WLXZ's were, and I + O(e^{−cn}) where WLXZ's were.
5. **Global parametrix.** N^H := D_{H,∞}^{σ₃} N D_H^{−σ₃}, with N WLXZ's global parametrix. It solves the
   modified band jump exactly.
6. **Local parametrices** (WLXZ §6.1, 6.2). Use V_l^H := D_{H,∞}^{σ₃}V_l D_H^{−σ₃} (and the same for V_r and V₀).
   - They satisfy the modified jumps up to factors I + O(1/n), because H_n and D_H are 1 + O(1/n) on the discs around
     ±2 and 0, all inside |z| ≤ R.
   - They match N^H on the disc boundaries to I + O(1/n), since WLXZ's matching is conjugated by bounded diagonal
     factors that tend to constants.
   - Inside the discs the residual jump is I + O(1/n). Absorb it as in WLXZ Remark 6.1 (single-layer small norm).
7. **Small norm.** S^H := V^H·(Ṽ^H)⁻¹ has J_{S^H} = I + O(1/n) in L² ∩ L^∞(Σ_S), as in WLXZ (6.34)–(6.35). So
   S^H = I + O(1/n), as in (6.36). ∎

## 3. Extraction (PROVED from W1)

- In the outer region, U = e^{nlσ₃/2}·(const)·S^H·N^H·(D-factors)^{−σ₃}·e^{n(g−l/2)σ₃}.
- At ∞ the D-factors and D_H tend to constants, and constant diagonal conjugations leave (U₁)₁₂(U₁)₂₁ unchanged.
- D_H(z)^{−σ₃} = D_{H,∞}^{−σ₃}(I + O(1/z)) is diagonal, so it changes only the 1/z² terms of the off-diagonal entries.
- Hence (U₁)₁₂(U₁)₂₁ = (𝒩₁)₁₂(𝒩₁)₂₁ + O(1/n), where 𝒩 is the global parametrix of the problem without D_H.

The same expression with S^{TC} (also I + O(1/n), by WLXZ) gives TC's coefficient. So

  γ_n²(σ_sym) = γ_n²(TC_sym)·(1 + O(1/n)).

The fold relations (RH.md §1) carry this to a_m, b_m with relative error O(1/m). They are algebraic, and every factor
is 1 + O(1/m): b_m² = γ_{2m−1}²γ_{2m}², a_m = γ_{2m−2}² + γ_{2m−1}², and both terms are positive and comparable. ∎

## 4. What is cited, what is new

- **Cited** (read; WLXZ, arXiv:1410.3948): the entire TC(α) steepest-descent analysis, for α = 1:
  - the IP (2.14)–(2.18), with Fokas–Its–Kitaev uniqueness under (Y4) (behaviour at 0, their (2.17));
  - R, T, Q, V (§§3–5);
  - the global parametrix (§5);
  - the local parametrices at ±2 (Airy, §6.1) and 0 (§6.2, with Remark 6.1);
  - small norm (6.29)–(6.36).

  Behaviour at 0 is inherited: H_n is bounded near 0, since n/z² → ∞ there and H → 1.
- **New here:** the identification of §1 (exact), Lemma W1 (the weight perturbation, an extra Szegő conjugation),
  and the extraction comparison §3.
- **What remains unproved** (review missing steps 2, 3, 5 for general p or r): nothing for this theorem *provided WLXZ's
  analysis is correct*. Their α > 0 covers α = 1. The p = 2 issues (two-sided D, odd θ) do not arise, because p = 1
  is WLXZ's own geometry. The Fisher–Hartwig issue does not arise either, because r = 3/2 gives α_FH = 0.
- **Label: PROVED-mod-cite (WLXZ §§2–6)**, pending Rule R.

## 5. Scope

- **General r for p = 1.** The weight k^{−r} = k^{−3/2}·k^{3/2−r} = (TC weight)·H·t^{3/2−r}. The extra factor
  t^{3/2−r} = (n/z²)^{3/2−r} is not 1 + O(1/n) near 0: it is the |z|^{2α_FH} singularity, α_FH = r − 3/2. This
  needs the Bessel origin parametrix and Vanlessen/KMVV (unread), i.e. missing step 5 of the review.
- **p = 2.** Needs the two-sided D-function construction (missing step 2).
