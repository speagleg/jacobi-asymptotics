# RH_zeta: pointwise Law P for the smooth-ζ model (Plan 13)

Status: **IN PROGRESS.** Phase 0 is done. Phase 1 is written; it is a proof sketch pending Rule R. Phase 2 has a design
note only. No PROVED labels.

## 0. Model and baseline

- **The measure σ_ζ** (toolkit `smooth_zeta`; Lean Corollary H_L-ζ) has atoms x_j = 1/(γ_j² + ¼) and weights 2x_j,
  where N₀(γ_j) = j − ½ and N₀(γ) = (γ/2π)log(γ/(2πe)) + 7/8.
- **Index function.** t(x) := N₀(γ(x)) + ½, with γ(x) = √(1/x − ¼), so t(x_j) = j.
  - t is decreasing in x only on (0, x_e], where x_e := 1/(4π² + ¼) (γ = 2π, the minimum of N₀), and t(x_e) = 3/8.
  - Its inverse x(t) is analytic and decreasing on (3/8, ∞), via Lambert W: γ = 2πe·exp(W((t − 11/8)/e)).
  - The atoms are x(j) for j ≥ 1. The top atom x₁ = x(1) < x_e.
- **Baseline** (NUMERICAL, checks/check_z_phase0.out, J = 8·10⁵, n ≤ 3200, J-halving stable to 1e−10):
  - b_n/x_n − π²/16 ≈ −0.226/log n;
  - a_n/(2b_n) − 1 ≈ 0.70/n … 0.84/n.

## 1. Finite-N constrained equilibrium and the edge equation (Phase 1)

**Lemma E1 (generalizing G2 B\*).** Let ρ ≥ 0 be a density on (0, x_e] such that x ↦ √x ρ(x) is decreasing and
∫_0^{x_e} ρ = ∞, with √x ρ ∈ L¹ near x_e. Put

  A(u) := ∫_u^{x_e} √x ρ(x)(x − u)^{−1/2} dx,  0 < u < x_e.

Suppose:
- A is strictly decreasing, with A(0⁺) = ∞ and A(x_e⁻) = 0;
- β ∈ (0, x_e) is the unique solution of the **edge equation A(β) = 1**.

Define τ(u) := A(u) on [β, x_e], with inverse u = β(τ) for τ ∈ (0, 1], and μ := ∫_0^1 ω_{[0,β(τ)]}dτ, where ω_{[0,b]}
is the arcsine law on [0, b]. Then:
- (i) μ is a probability measure with dμ/dx = ρ on [β, x_e] and dμ/dx < ρ on (0, β);
- (ii) U^μ(x) := ∫log|x − y|dμ(y) = ∫_0^1 log(β(τ)/4)dτ =: ℓ/2 on (0, β], and U^μ ≥ ℓ/2 on (0, ∞);
- (iii) Re g′(x) = ∫_{τ: β(τ)<x} dτ/√(x(x − β(τ))) > 0 for x ∈ (β, x_e). So U^μ is strictly increasing there, and
  U^μ > ℓ/2 on (β, x_e];
- (iv) μ maximizes the logarithmic energy among probability measures ν ≤ ρ dx. This is G2's optimality argument
  verbatim, using only (i), (ii) and the positivity lemma (P). It is not needed for the RH analysis.

*Proof.*
- **(i)** For x ∈ [β, x_e], with ψ := dμ/dx and the substitution u = β(τ),

    πψ(x) = ∫_{β(τ)>x} dτ/√(x(β(τ) − x)) = x^{−1/2}∫_x^{x_e}(−A′(u))(u − x)^{−1/2}du.

  - By Abel's inversion formula (A is the Abel transform of √x ρ), ∫_x^{x_e}(−A′(u))(u − x)^{−1/2}du = π√x ρ(x).
    Hence ψ = ρ.
  - For x < β, Abel inversion on all of (x, x_e) gives π√x ρ(x) = ∫_x^{x_e}(−A′)(u − x)^{−1/2}du. The part over
    (x, β) is > 0 because −A′ > 0, so π√x ψ(x) = ∫_β^{x_e}(−A′)(u − x)^{−1/2}du < π√x ρ(x).
  - Mass: ∫_0^1 dτ = 1.
- **(ii)** The arcsine law ω_{[0,b]} has U = log(b/4) on [0, b] and U ≥ log(b/4) everywhere (G2 Lemma B0). For x ≤ β,
  every component has x ≤ β(τ). Fubini applies, as in G2 B*(ii).
- **(iii)** The components with β(τ) > x contribute purely imaginary terms to g′(x + i0). The others contribute
  1/√(x(x − β(τ))) > 0.
- **(iv)** G2 PROOF.md "Optimality", with σ ↦ ρ dx. ∎

**Corollary E2 (pure powers).** For ρ = (1/p)x^{−1−1/p} on (0, ∞) (x_e = ∞), the edge equation gives
β^{1/p} = (1/p)B(1/p, ½) = π/(2I(p)), i.e. **β = 4c(p)**. So Law P's constant is the band edge of this equilibrium,
recovering G2. (check_z_edge.out [0]: 11 digits for p = 1.5, 2, 3.)

**Corollary E3 (index form).** With ρ_N := |t′(x)|/N on (0, x_e] (the smoothed node-counting density at degree N),
substitute x = x(s):

  A(β) = (1/N)∫_{3/8}^{T} (1 − x(T)/x(s))^{−1/2} ds,  β = x(T).

So **β_N = x(T_N)**, where (1/N)∫_{3/8}^{T_N}(1 − x(T_N)/x(s))^{−1/2}ds = 1.

The hypotheses of E1 for σ_ζ:
- √x ρ_N ≍ γ²log(γ/2π)/(4πN) is decreasing in x on (0, x_e) (checked: |t′| increases with γ for γ > 2π);
- A(0⁺) = ∞;
- A(x_e⁻) = 0, since ρ_N vanishes linearly at x_e (t − 3/8 is quadratic in x − x_e);
- strict monotonicity of A follows from that of √x ρ_N.

**Proposition E4 (the edge equation captures Law P's slow term; NUMERICAL).** checks/check_z_edge2.out (canonical E3,
J = 8·10⁵):

  b_N/(β_N/4) − 1 = +0.2786/N, 0.2783/N, 0.2778/N, 0.2772/N, 0.2763/N, 0.2753/N, 0.2743/N,

for N = 50 … 3200. So b_N = (β_N/4)(1 + 0.27/N + o(1/N)). The slow −0.226/log n deviation of b_n/x_n is entirely the
finite-N equilibrium.
- *Convention note.* checks/check_z_edge.out integrated |t′| over all of (0, 4), which also counts the non-monotone
  leg (x_e, 4). That shifts β_N by O(1/N) (N·dev ≈ −1.1 … −1.4 there). The canonical constraint is the monotone branch.

**Proposition E5 ((Z3), the slow term; derivation plus NUMERICAL).** Write x(t) = t^{−2}ℓ(t), with ℓ slowly varying and
ε(t) := tℓ′(t)/ℓ(t) ~ 2/log t. Regular variation in E3 gives T_N ~ N/J(2 − ε) with
J(p) := ∫_0^1(1 − u^p)^{−1/2}du = √πΓ(1 + 1/p)/Γ(1/p + ½). Hence

  β_N/(4x_N) = c(2)(1 + κ/log N + o(1/log N)),  κ = −2(2J′(2)/J(2) + log J(2)) = −2(log(π/2) − (1/2)(1 − log 2))
  = −0.28946…

Check (checks/check_z_kappa.out, the edge equation alone, N up to 10¹⁵): log N·(β_N/(4x_N c₂) − 1) = −0.381, −0.367,
−0.359, −0.346, −0.337, −0.331, −0.326, −0.320 for N = 10², 10³, 10⁴, 10⁶, 10⁸, 10¹⁰, 10¹², 10¹⁵. A fit a + b/log N on
the last two points gives a ≈ −0.300, consistent with κ up to the log log N terms in ℓ (γ_N = 2πN/log N·(1 + O(log log
N/log N))). At n ≤ 3200 the measured coefficient (−0.226/c₂ = −0.366 relative) is dominated by these secondary terms.

**Status of Phase 1:**
- E1–E3: proof sketch, pending Rule R. They are G2 B* plus Abel inversion.
- E4: NUMERICAL.
- E5: derivation plus NUMERICAL. A rigorous o(1/log N) bound needs a uniform regular-variation lemma, which is routine.

## 2. Phase 2 design note: the far end (new relative to RH_px)

**The obstruction.** t(x) is analytic across x_e, but there t − 3/8 has a *double zero*. On (x_e, 4) it increases again
to 11/8, and it crosses t = 1 at a spurious point x_s with no atom. So D := D̃/(1 − e^{∓2iθ}), which has poles where
t ∈ ℤ, has a spurious pole at x_s on the real axis inside Ω_∞. The RH_px recipe (F = D·B·K globally in Ω_∞) breaks.

**Proposed fix (to be verified).**
- D is needed only near Σ^△, where the exact relation D̃ = D(1 − e^{∓2iθ}) makes the Σ^△ diagonals cancel. Split Ω_∞
  by the vertical line L := x_m + iℝ, with x_m ∈ (x₁ + δ′, x_e):
  - left of L use D·B·K;
  - right of L use an explicit scalar F_far, the Cauchy integral on (x_m, x_e) of T's jump e^{∓2iθ̂}, θ̂ := π(t − 3/8),
    so that the constraint mass beyond x is (t − 3/8)/N, a WLXZ-type α-shift.
- The resulting diagonal jump on L is explicit, and it is absorbed by one more scalar Cauchy integral Ξ on L. Ξ
  lies at rescaled distance ≍ N²/log²N from the band, so near the band and both edges Ξ = const·(1 + O(log²N/N²)).
- Any monodromy at ∞ is also absorbed far away: a cut along (x_e, ∞) and a z^{κσ₃} normalization in both V and N.
- **Gate 2 test:** an end-to-end probe (the check_px_e2e pattern) with the N-dependent μ from E1. Expect
  VN^{−1} − I = O(1/N) at points near the band.
