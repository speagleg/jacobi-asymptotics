# RHPRIME: RH + a one-sided prime-variance bound ⇒ (SG) ⇒ G3′ (Plan 21) — NOT REVIEWED (Rule R pending)

Answers RHFREE.md §6 and RHFREE2.md §4 ((Q1) of PROOF.md §9.3). On RH, the Tauberian obstruction of RHFREE2 §4 is
**avoided**, not overcome: the Fejér weight in Goldston's R(x, T) is kept throughout. On RH every pair term is
non-negative, so a *weighted* small-gap count needs no Hilbert-space argument. (The weighted Lemma G of RHFREE2 §4 is
needed only RH-free, where it stays OPEN.)

| Item | Content | Label |
|---|---|---|
| (V⁺) | One-sided prime variance on a bounded δ-range | HYPOTHESIS (with RH) |
| Lemma P1 | RH + (V⁺) ⇒ G(T^α) ≤ (1 + o(1))N_Ψ on [1, M] | PROVED-mod-cite ((C8) (9.7)–(9.9), with (9.9)'s full-range error as stated, sketch only, in (C8)) + mod-input RH, (V⁺) |
| Lemma P2 | RH ⇒ G(T^α) = N_Ψ(T^{−2α}log T + α) + O(T^α log T) + o(N_Ψ) on [0, 1] | PROVED-mod-cite ((C8) (4.2)–(4.4), (C3) (3.5), (C1)) + mod-input RH |
| Lemma P3 | weighted K² sum: S_Ψ ≤ N_Ψ(1 + D(η)) + o(N_Ψ) | PROVED-mod-cite ((C6) §3 algebra) + mod-input RH, (V⁺) |
| Theorem V⁺ | RH + (V⁺) ⇒ (SG) with rate δ³ ⇒ G3′ | PROVED-mod-cite (above, (C1)) + mod-input RH, (V⁺), Theorem H; novelty UNCHECKED |

## 0. Setting (RH is assumed throughout this file, as a labelled hypothesis)

- Ordinates γ run over all nontrivial zeros, with multiplicity and with both signs.
- c(u) := 1/(1 + u²) and w(u) := 4/(4 + u²).
- Goldston ((C8) (4.1)–(4.2), read): "∫|Σ_{0<γ≤T} x^{iγ}/(1 + (t − γ)²)|²dt = (π/2)Σ_{0<γ,γ′≤T}x^{i(γ−γ′)}w(γ − γ′)".
  Equivalently, (2/π)∫_ℝ c(t − γ)c(t − γ′)dt = w(γ − γ′).
- Fix T. Put δ := 1/T, κ := log(1 + δ), φ(t) := (sin(κt/2)/(κt/2))² and S_x(t) := Σ_γ x^{iγ}c(t − γ). Define

    G(x) := (2/π)∫_0^∞ φ(t)|S_x(t)|²dt,  so that Goldston's R(x, T) = 2xκ²G(x) ((C8) (9.7)).

- **Pair form (exact).** G(x) = Σ_{γ,γ′} x^{i(γ−γ′)}w(γ − γ′)Ψ(γ, γ′), where

    Ψ(γ, γ′) := (2/π)∫_0^∞ φ(t)c(t − γ)c(t − γ′)dt / w(γ − γ′) ∈ [0, 1].

  - Ψ is an average of φ·1_{t≥0} under the probability density ∝ c(t − γ)c(t − γ′).
  - The double sum converges absolutely, since Σ_γ c(t − γ) ≪ log(|t| + 2) (C1) and φ(t) ≤ min(1, 4/(κt)²).
  - G is real, G ≥ 0, and G(1/x) = G(x) (swap γ and γ′).
- **Weighted count.** N_Ψ := Σ_γ Ψ(γ, γ) = (2/π)∫_0^∞ φ(t)Σ_γ c(t − γ)²dt.
- **Prime side** ((C8) §9, read). I(X, δ) := ∫_1^X (ψ((1 + δ)x) − ψ(x) − δx)²dx.

**Hypothesis (V⁺) (one-sided, bounded range).** For every M ≥ 1 and ε > 0 there is X₀ such that
I(X, δ) ≤ (½ + ε)δX²log(1/δ) for all X ≥ X₀ and X^{−1} ≤ δ ≤ X^{−1/M}.
- This is the upper half of (C8) (9.1) on the range δ ∈ [X^{−1}, X^{−1/M}].
- Equivalently, by (C8), upper bounds of the shape of (9.3) for 1 ≤ h ≤ X^{1−1/M}. That direction is not used.
- Theorem 7 of (C8) relates (9.1) on such ranges to SPC on α ∈ [1, M].

## 1. Lemma P1 (primes ⇒ upper bound for G on [1, M])

**Inputs** ((C8), read; quotes in CITATIONS (C8) Plan-20/21 addenda).
- (9.7)–(9.8): on RH, L(x, T) = R(x, T) + O((log T)²/T).
- (9.9): "L(x, T) = 4x³∫_x^∞ I(y, δ)dy/y⁵ + O(x²(log T)²/T³)". Goldston adds that "the error term in (9.9) can be
  replaced by O(x(log x)⁴/T^{3/2})" on the full range. That claim is stated with a sketch ("Stieltjes integration and the
  PNT with the RH error (3.4) … Cauchy Schwarz"), not a full proof. **It is used here as cited.**

**Lemma P1.** Assume RH + (V⁺). Then for each M, uniformly for 1 ≤ α ≤ M: G(T^α) ≤ (1 + o(1))·(T/2)log T.

*Proof.* Let x = T^α ∈ [T, T^M] and Y := T^{2M+1}.
- For x ≤ y ≤ Y we have y^{−1} ≤ δ = 1/T ≤ y^{−1/(2M+1)}, so (V⁺) (with M replaced by 2M + 1) gives
  I(y, δ) ≤ (½ + ε)δy²log T.
- For y > Y use the trivial bound. Since ψ(b) − ψ(a) ≤ (b − a + 1)log b, we get
  |ψ((1+δ)u) − ψ(u) − δu| ≤ 3δu log(2u) for u ≥ T, and ≤ 3 log(2u) for u < T. Hence I(y, δ) ≪ δ²y³log²y for y ≥ T.
- So 4x³∫_x^∞ I(y, δ)y^{−5}dy ≤ (1 + 2ε)xδ log T + O(x³δ²log²Y/Y).
- The O-term, divided by xδ log T, is ≪ T^{2α−1}M²log T/T^{2M+1} → 0.
- With (9.9) (full-range error) and (9.7): R(x, T) ≤ (1 + 2ε)xδ log T + O(x(log x)⁴/T^{3/2}) + O(log²T/T)
  = (1 + 2ε + o(1))(x/T)log T.
- Divide by 2xκ², using κ = 1/T + O(1/T²). ∎

## 2. Lemma P2 (weighted Montgomery theorem on [0, 1]; RH only)

**Inputs.**
- (C8) (4.4): "F(x, T) = (2/π)∫_0^T|Σ_γ x^{iγ}/(1 + (t − γ)²)|²dt + O((log T)³)", where (4.2) defines
  F(x, T) := Σ_{0<γ,γ′≤T}x^{i(γ−γ′)}w(γ − γ′).
- (C3) (3.5), the full-window MT. On RH its F_{(0,t]} is (4.2)'s F, since W(i(γ−γ′)) = w(γ − γ′). It gives
  F(x, t) = (t log²t/2πx²)(1 + O(1/√log t)) + (t/2π)log x + O(t√log t) for 1 ≤ x ≤ t.

**Lemma P2.** On RH, uniformly for 0 ≤ α ≤ 1 (x = T^α):
- N_Ψ = (T/2)log T·(1 + O(1/log T));
- G(x) = N_Ψ(T^{−2α}log T(1 + o(1)) + α) + O(T^α log T) + o(N_Ψ).

*Proof.* Put H(t) := (2/π)∫_0^t|S_x(u)|²du. By (4.4), H(t) = F(x, t) + O(log³t). Let Λ := log²T. Then
G = ∫_0^x φ dH + ∫_x^{ΛT} φ dH + ∫_{ΛT}^∞ φ|S_x|²(2/π)dt.

- **Tail.** Using |S_x(t)| ≤ Σ_γ c(t − γ) ≪ log t, the last integral is ≪ ∫_{ΛT}^∞ T²t^{−2}log²t dt ≪ T log²T/Λ = O(T).
- **Low part.** 0 ≤ ∫_0^x φ dH ≤ H(x) = F(x, x) + O(log³x) ≪ x log x = O(T^α log T), by (3.5) at t = x.
- **Middle.** On [x, ΛT] write H = M + E, with M(t) := (t log²t)/(2πx²) + (t/2π)log x and
  |E(t)| ≪ t√log t + t log^{3/2}t/x² + log³t. The middle term matters only for x² < log t. It is absorbed below into
  the (1 + o(1)) factor of the spike term T^{−2α}log T. Then
  ∫_x^{ΛT}φ dH = ∫_x^{ΛT}φM′dt + [φE]_x^{ΛT} − ∫_x^{ΛT}Eφ′dt.
  - The boundary terms are O(x√log x + T√log T/Λ).
  - **E-integral, by dyadic blocks [U, 2U].**
    - For U ≤ T: |φ′(t)| ≪ κ²t, so the variation of φ on the block is ≪ κ²U². The contribution is
      ≪ Σ_{U≤T} U√log U·κ²U² ≪ T√log T.
    - For T < U ≤ ΛT: φ has ≍ κU oscillations of amplitude ≪ (κU)^{−2} on the block, so its variation there is
      ≪ T/U. Each block contributes ≪ T√log U, and there are O(log Λ) = O(log log T) blocks.
    - Total: O(T√log T log log T) = o(T log T), plus O((T log^{3/2}T/x²)log log T) from the middle term of E, which is
      o of the spike term (T log²T)/(2x²).
  - **Main.** ∫_x^{ΛT}φM′dt = ∫_x^{ΛT}φ(t)[(log²t + 2 log t)/(2πx²) + (log x)/2π]dt.
    - Since ∫_0^∞ φ = π/κ, ∫_0^∞ φ(t)log t dt = (π/κ)(log(1/κ) + O(1)), and φ(t) ≤ 4/(κt)², this equals
      (T log²T/2x²)(1 + o(1)) + (T/2)log x + O(x log²T + T log²T/Λ).
- **N_Ψ.** Σ_γ c(t − γ)² = ∫c(t − u)²dN(u). Using N(u) = (u/2π)log(u/2πe) + O(log u) (C1) and integrating by parts
  against the smooth weight (φ∗c²)(u):
  N_Ψ = (2/π)(π/2)∫_0^∞ φ(t)(log t/2π)dt + O(log T) = (T/2)log T(1 + O(1/log T)).
- Collect the terms. ∎

## 3. Lemma P3 (weighted K² sum)

Take η, K, Q, D(η) as in RHFREE §1 (η real, even, C_c^∞((−λ, λ)), ∫η² = 1), and L := (1/2π)log T. On RH,
z := i(ρ − ρ′)L = −(γ − γ′)L is real, and K(z)² ≥ 0.

**Lemma P3.** Assume RH + (V⁺). Then S_Ψ := Σ_{γ,γ′}Ψ(γ, γ′)K((γ − γ′)L)² ≤ N_Ψ(1 + D(η)) + o(N_Ψ).

*Proof.*
- **Weight removal.** As in (C6) (3.3): with r_T := Q − Q″/(4 log²T), we have
  r̂_T(z) = (1 + π²z²/log²T)K(z)² = K(z)²/w(γ − γ′). Multiplying by Ψw, summing (absolutely convergent), and using the
  pair form of G:

    S_Ψ = ∫ r_T(α)G(T^α)dα = ∫QG − (4 log²T)^{−1}∫Q″G.

- **Q″ term.** Since G ≥ 0, |∫Q″G| ≤ ‖Q″‖_∞∫_{|α|≤2λ}G = O_λ(N_Ψ) by P1 and P2, so this term is o(N_Ψ).
- **|α| ≤ 1** (P2 and evenness). ∫_{−1}^{1}QG = N_Ψ(Q(0) + 2∫_0^1αQ) + o(N_Ψ). The O(T^α log T) term integrates to
  O(N_Ψ/log T).
- **1 ≤ |α| ≤ 2λ** (P1 with M = 2λ; Q ≥ 0). ∫QG ≤ (1 + o(1))N_Ψ·2∫_1^{2λ}Q.
- **Sum.** The bracket is 1 + D(η), as in RHFREE Lemma PC. ∎

## 4. Theorem V⁺

**Theorem V⁺.** Assume RH and (V⁺). Then:
- for every δ > 0, limsup_K K^{−1}#{k ≤ K : g_k < δ} ≤ Cδ³, with an absolute C;
- hence (SG) holds, and log D_n(σ) = Φ_n + o(n²): G3′ holds, mod Theorem H.

*Proof.*
- **Counting, using positivity only.** Fix δ. Take λ := 1/(8πδ) and η = η_λ (RHFREE §1 scaling).
  - For |u| ≤ 2δ = 1/(4πλ): K(u) ≥ 1 − 2π²λ²u² ≥ 7/8, so K(u)² ≥ ¾.
  - Every term of S_Ψ is ≥ 0. The diagonal (the same zero counted with itself) contributes N_Ψ.
  - Hence, over ordered pairs of distinct zeros ρ ≠ ρ′ (with multiplicity, so repeated ordinates count) with
    |γ − γ′|L < 2δ: Σ Ψ(γ, γ′) ≤ (4/3)(S_Ψ − N_Ψ) ≤ (4/3)(D(η_λ)N_Ψ + o(N_Ψ)).
- **Ψ is bounded below on the bulk.** Fix R > 1. For T/R < γ ≤ T and |γ − γ′| ≤ 1, Ψ(γ, γ′) ≥ 0.7 for large T:
  - Ψ averages φ·1_{t≥0} against a density ∝ c(t − γ)c(t − γ′), which has tails ≪ |t − γ|^{−4};
  - φ ≥ (sin 1/1)² > 0.708 on [0, 2T];
  - the mass of the density outside [0, 2T] is O(T^{−3}).
- **Gaps.**
  - The consecutive pairs (k, k+1) with γ_k ∈ (T/R, T] and g_k < δ are distinct ordered pairs with
    (γ_{k+1} − γ_k)L < 2δ, by the normalization argument of Theorem C's proof.
  - So their number is ≤ (1/0.7)(4/3)(D N_Ψ + o(N_Ψ)) ≤ 1.91·D·(π + o(1))N(T), since N_Ψ = (π + o(1))N(T) by P2
    and (C1).
  - Indices with γ_k ≤ T/R number ≤ (1/R + o(1))N(T).
  - With D(η_λ) ≤ ‖Q₁″‖_∞(8πδ)³/12 this gives #{k ≤ N(T) : g_k < δ} ≤ (Cδ³ + 1/R + o(1))N(T).
- **(SG), then G3′.** Take R = 3/η, and use G3′-L (mod Theorem H) and G3′-U, as in Theorem C. ∎

**Remarks.**
- **V1 (what is weakened, relative to Corollary P (§9.1)).**
  - Corollary P assumes RH + the *two-sided* asymptotic (V) (equivalently SPC on all of [1, ∞)).
  - Theorem V⁺ assumes RH + an *upper* bound only, on δ ∈ [X^{−1}, X^{−1/M}] for each M. For a given (SG) tolerance η
    one needs M ≍ η^{−1/3}.
  - The Tauberian step of (C8) Theorem 7, which needs both bounds, is bypassed: the zero side is weighted by the same
    Fejér kernel as R(x, T).
- **V2 (the weighted route needs RH).** L = R ((9.7)) is proved on RH. Positivity of each term of S_Ψ is also used,
  and it holds because K((γ − γ′)L)² ≥ 0 for real arguments. RH-free, both fail. That is where the weighted Lemma G of
  RHFREE2 §4 would be needed (OPEN).
- **V3 (dependence on (C8)).** The full-range error in (9.9) is cited from (C8), where it is stated with a sketch.
  - With only the displayed error O(x²(log T)²/T³), P1 holds for 1 ≤ α ≤ 2 − ε.
  - That gives Lemma P3 only for 2λ < 2, i.e. small-gap bounds only at fixed δ > 1/(8π). (SG) needs λ → ∞, so this
    is insufficient.
  - So Theorem V⁺ is **mod-cite on the full-range claim**.
- **V4.** Novelty: UNCHECKED. The weighted, one-sided transfer might be implicit in [18] (Goldston–Montgomery), which
  has not been read.

## 5. Numerics (NUMERICAL; `checks/check_weighted_pc.py` → `.out`; Odlyzko's first 2,001,052 zeros)

The setup takes Ψ(γ, γ′) ≈ φ((γ + γ′)/2), with T ∈ {2·10⁴, 5·10⁴, 10⁵} and λ ∈ {½, 1, 2}:

- **Bound holds.** S_Ψ/N_Ψ < 1 + D(λ) in all cases. This is consistent with Lemma P3, which in effect assumes
  (V⁺) with equality, i.e. the GUE value.
- **Fixed scale L = log T/2π** (as in the theorem): 1.5286 / 1.1000 / 1.0138 at T = 10⁵, against 1 + D =
  1.7067 / 1.1560 / 1.0238.
- **Local unfolding:** 1.6844 / 1.1401 / 1.0197. This is within 0.4–1.4% of the GUE value, consistent with lower-order
  corrections at these heights (a recollection, not cited).
- **N_Ψ against πN(T):** the ratio is 1.18, 1.13 and 1.09 for T = 2·10⁴, 5·10⁴ and 10⁵, consistent with
  1 + O(1/log T).
