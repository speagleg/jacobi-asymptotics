# Theorem RH₁: pointwise Law P for σ = Σ k^{−3/2} δ_{1/k}, by perturbing WLXZ (Tricomi–Carlitz, α = 1)

Status: **REVIEWED** 2026-10-13 (Rule R `review/REVIEW_RH1.md`: ACCEPT WITH FIXES, all fixes applied, re-check
CONFIRMED). Label: PROVED-mod-cite (WLXZ v1 §§2–6). This is option 1 of the post-review plan (RH review, REVIEW_RH.md): finish
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

Numerically (`checks/check_p1_tc.out`, fix F7) the true deviation is O(n⁻²). Both measures go through the same
pipeline, which is validated against TC's exact coefficients (bias 3e−10 at tail cut-off 1e16). The comparison gives
n²(b_n^σ/b_n^{TC} − 1) = −0.0413, −0.0416, −0.0416, −0.0417 at n = 50, 200, 800, 1500, and the same for a_n. This is
consistent with a limit −1/24 (conjecture, not proved).

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

Source: WLXZ arXiv:1410.3948**v1**, quoted in CITATIONS.md (Rule C). The Anal. Appl. version was not read.

**Facts at α = 1.**
- (i) WLXZ's D̃ (their (4.15)) equals 1/H_n identically. This was verified with mpmath to 30 digits for n = 10, 100,
  1000 at real and complex z.
- (ii) σ's rescaled weight is w·H_n = n^{1/2}(e/√(2π))t^{−3/2} with t = n/z², a pure power.
- (iii) The residual band weight is w₀/D̃² = −e^L(4 − z²)·H_n for TC. For σ it is −e^L(4 − z²)·H_n².

So WLXZ's own band jump for TC already differs from their model (global-parametrix) jump by the factor H_n. Their
(6.34) absorbs exactly this as "I + O(1/n) on (−2+ε, −ε) ∪ (ε, 2−ε)".

**Stirling with a sectorial bound** (DLMF 5.11.1 and §5.11(ii), read).
ln Γ(z) = (z − ½)ln z − z + ½ln(2π) + Σ_{k<m} B_{2k}/(2k(2k−1)z^{2k−1}) + R_m. For complex z, |R_m| is at most
sec^{2m}(½ ph z) times the first neglected term. Hence H(t) = 1 + O(1/|t|) uniformly in |ph t| ≤ π − ε. In the
z-variable this means uniformly in the sectors |arg(±z)| ≤ π/2 − ε/2. WLXZ's band, lens lips, discs and saturated
contours lie in these sectors, near the real axis.

**Lemma W1.** Run WLXZ's steepest-descent analysis (§§3–6, α = 1) **verbatim** with weight w·H_n in place of w:
- the same transformations R, T, Q, V;
- the same g, φ, D, D̃, D̂ and E (they depend only on n/z² and α);
- the same global parametrix N;
- local parametrices built from σ's own weight.

Then the final S-jumps satisfy J_S = I + O(1/n) on the disc boundaries and band pieces, and I + O(e^{−cn}) elsewhere,
exactly as in (6.34). Hence S = I + O(1/n) (6.37), with S₁ = O(1/n).

*Proof.*
1. **R, T, Q.** These are algebraic in w. H_n is analytic and nonvanishing on all Ω-regions (off iℝ, with
   |arg(±z)| < π/2) and at the nodes (t = k + 1 ≥ 1). So pole removal (3.13)–(3.18) holds. g and φ do not involve
   the weight.
2. **V.** Built with WLXZ's D-functions, which are unchanged. The residual weights acquire factors H_n^{±1} relative to
   TC. On the long saturated pieces, Σ^△ and the vertical segments up to ±k_n, t = n/x² ≥ ½. There H_n and 1/H_n are
   bounded (|H| ∈ [1.00, 1.17] on Re t ≥ ½, checked by the reviewer). So entries that are O(e^{−cn}) for TC stay
   O(e^{−cn}) for σ, with the sign conditions (5.8) unchanged.
3. **Band, outside the discs.** The S-jump is N₋·M·N₋^{−1}, where M differs from the identity by the factor
   H_n² = 1 + O(z²/n) in the off-diagonal model jump. So it is I + O(1/n) uniformly on (ε, 2−ε) and (−2+ε, −ε).
   This is the same mechanism as WLXZ's own H_n mismatch for TC.
4. **Airy discs U(±2, ε)** (fix F2). Build V_r and V_l from σ's own weight: WLXZ (6.5)–(6.21) with w → wH_n. That
   construction needs w̃ and ŵ analytic and nonvanishing in U(±2, ε), which holds because t ≈ n/4 there. Then the
   local jumps are matched exactly. The matching (6.14) holds with I + O(1/n), because D̃²/w̃ equals TC's quantity times
   H_n^{±1}, and H_n^{±1} = 1 + O(1/n) on ∂U(±2, ε), and E_r stays analytic. No residual jump is left inside the discs.
5. **Origin U(0, ε).** Define V₀ as WLXZ (6.26) and Remark 6.1. Their (6.27) holds for σ:
   - the band-jump ratio is H_n² = 1 + O(z²/n);
   - the lip entries are bounded, since Re φ < 0;
   - the upper-right Σ_r entries are super-exponentially small in the sectors.

   Remark 6.1's single-layer argument then gives V₀ = V_loc⁰(I + O(1/n)).
6. **Small norm** (fix F6). ‖J_S − I‖_{L²∩L^∞(Σ_S)} = O(1/n) as in (6.35), and ‖J_S − I‖_{L¹(Σ_S)} = O(1/n),
   because the bounded pieces are O(1/n) and the long pieces of length ≍ √n are O(e^{−cn}). So S = I + O(1/n) (6.37),
   and S₁ = −(1/2πi)∫S₋(J_S − I) = O(1/n). ∎

**Behaviour at 0 ((Y4) for σ).** The mass ratio k^{−3/2}/w_d(node) = (√(2π)/e)·H(k) is bounded above and below. So the discrete
Cauchy transforms satisfy Y₁₂, Y₂₂ = O(log|z|) at 0, exactly as WLXZ (2.17). Their Theorem 2.3 (Fokas–Its–Kitaev
uniqueness) applies.

## 3. Extraction (PROVED from W1; fix F5)

- **Notation.** β_n := ‖π_n‖²/‖π_{n−1}‖², the squared recurrence coefficient. (WLXZ's γ_n is a *leading coefficient*,
  their (1.9). We avoid the symbol γ.) WLXZ (2.18) gives Y₂₁ = π_{n−1}/‖π_{n−1}‖², so
  (Y₁)₁₂(Y₁)₂₁ = β_n. The rescaling (3.1) gives (U₁)₁₂(U₁)₂₁ = n·β_n.
- **Global value.** From WLXZ (5.11) at α = 1: N₁₂ ∼ −ie^L/z and N₂₁ ∼ ie^{−L}/z, so (N₁)₁₂(N₁)₂₁ = 1. Consistently,
  nβ_n^{TC} = n/(n+1) → 1.
- **Invariance.** The diagonal conjugations (e^{nlσ₃/2}, n^{(α−½)σ₃}, (DE)^{σ₃}, e^{ngσ₃}) have determinant 1 or tend
  to constants, so they do not change the product. Hence nβ_n = (N₁)₁₂(N₁)₂₁ + O(1/n) = 1 + O(1/n) for σ, using S₁ from
  W1. The same holds for TC. So β_n(σ) = β_n(TC)(1 + O(1/n)).
- **Fold.** a_m = β_{2m−2} + β_{2m−1} (positive terms) and b_m² = β_{2m−1}β_{2m}. Relative O(1/m) errors are
  preserved. ∎

## 4. What is cited, what is new

- **Cited** (read; WLXZ, arXiv:1410.3948): the entire TC(α) steepest-descent analysis, for α = 1:
  - the IP (2.14)–(2.18), with Fokas–Its–Kitaev uniqueness under (Y4) (behaviour at 0, their (2.17));
  - R, T, Q, V (§§3–5);
  - the global parametrix (§5);
  - the local parametrices at ±2 (Airy, §6.1) and 0 (§6.2, with Remark 6.1);
  - small norm (6.29)–(6.37).

  Behaviour at 0 is inherited: H_n is bounded near 0 within the sectors |arg(±z)| ≤ π/2 − ε, since n/z² → ∞ there
  and H → 1.
- **New here:** the identification of §1 (exact), Lemma W1 (running WLXZ verbatim with weight wH_n; no extra
  conjugation), and the extraction comparison §3.
- **Reliance noted.** WLXZ assert, without full detail, that the jumps are O(e^{−cn}) uniformly up to k_n. RH₁
  depends on WLXZ for this point.
- **What remains unproved** (review missing steps 2, 3, 5 for general p or r): nothing for this theorem *provided WLXZ's
  analysis is correct*. Their α > 0 covers α = 1. The p = 2 issues (two-sided D, odd θ) do not arise, because p = 1
  is WLXZ's own geometry. The Fisher–Hartwig issue does not arise either, because r = 3/2 gives α_FH = 0.
- **Label: PROVED-mod-cite (WLXZ v1 §§2–6), REVIEWED** (review/REVIEW_RH1.md, re-check passed).

## 5. Scope

- **General r for p = 1.** The weight k^{−r} = k^{−3/2}·k^{3/2−r} = (TC weight)·H·t^{3/2−r}. The extra factor
  t^{3/2−r} = (n/z²)^{3/2−r} is not 1 + O(1/n) near 0: it is the |z|^{2α_FH} singularity, α_FH = r − 3/2. This
  needs the Bessel origin parametrix and Vanlessen/KMVV (unread), i.e. missing step 5 of the review.
- **p = 2.** Needs the two-sided D-function construction (missing step 2).
