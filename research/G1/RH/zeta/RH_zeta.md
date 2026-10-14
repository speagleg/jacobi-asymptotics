# RH_zeta: pointwise Law P for the smooth-ζ model (Plan 13)

Status: **Rule R: ACCEPT WITH FIXES** for Phases 1–2 (review/REVIEW_RHzeta.md; fixes applied, §5). Labels:
- E1: PROVED-mod-G2;
- E2, E3: PROVED;
- E4: NUMERICAL (convention-dependent);
- E5: derivation plus NUMERICAL;
- Phase 2: NUMERICAL, CONFIRMED by the absolute test with Ξ;
- §4 theorem: **PROOF SKETCH (conditional)**. Open: the log-weight hard-edge lemma (F1), Lemma Z (certified winding
  plus a uniform bound) and uniform Airy.

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
- √x ρ_N is decreasing in x on (0, x_e). Exactly: with x = 1/(γ² + ¼) and γ′(x) = −1/(2x²γ),
  √x ρ_N = log(γ/2π)(γ² + ¼)^{3/2}/(4πNγ). Both factors are positive and increasing in γ for γ > 2π, and γ decreases
  with x (Rule R F8);
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

  β_N/(4x_N) = c(2)(1 + κ/log N + o(1/log N)),  κ = −2(2J′(2)/J(2) + log J(2)) = −2(log(π/2) − (1 − log 2))
  = −0.28946…

Check (checks/check_z_kappa.out, the edge equation alone, N up to 10¹⁵): log N·(β_N/(4x_N c₂) − 1) = −0.381, −0.367,
−0.359, −0.346, −0.337, −0.331, −0.326, −0.320 for N = 10², 10³, 10⁴, 10⁶, 10⁸, 10¹⁰, 10¹², 10¹⁵. A fit a + b/log N on
the last two points gives a ≈ −0.300, consistent with κ up to the log log N terms in ℓ (γ_N = 2πN/log N·(1 + O(log log
N/log N))). At n ≤ 3200 the measured coefficient (−0.226/c₂ = −0.366 relative) is dominated by these secondary terms.

**Status of Phase 1:**
- E1–E3: proof sketch, pending Rule R. They are G2 B* plus Abel inversion.
- E4: NUMERICAL.
- E5: derivation plus NUMERICAL. A rigorous o(1/log N) bound needs a uniform regular-variation lemma, which is routine.

## 2. Phase 2 design note: the far end (SUPERSEDED by §4.2; kept for the record, Rule R F7)

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


## 3. Phase 2: global parametrix, validated end to end (Gate 2 GO; NUMERICAL)

**Two corrections to the RH_px recipe**, both found by the probe.

- **(a) WLXZ α-shift at the far end.** The constraint lives only on the monotone branch t ≥ 3/8. So
  μ((x, ∞)) = (t(x) − 3/8)/N on the saturated region, and T's jump there is diag(e^{∓2πi(t−3/8)}). D's
  −e^{2iθ} removes the e^{∓2iθ} part and leaves a constant phase.
  - This is exactly WLXZ's α-shift. Their TC nodes sit at n/z² = k + α; ours sit at t − 3/8 = (j − 1) + 5/8, i.e.
    α_W = 5/8.
  - Hence WLXZ's E = (4 − z²)^{1/2−α} becomes **K := (β̂ − z)^{κ} with κ = TMIN − ½ = −1/8**. Pure powers have
    TMIN = 0 and κ = −½, as in RH_px.
  - The band weight becomes w₀ = W(β̂ − x)^{−2κ}/(D̃B)² = C·x^{α_x}·(β̂ − x)^{1/4}·h_N. The soft-edge exponent changes;
    the Airy construction is WLXZ §6.1 with general α, cf. their (5.7) V = O(1)(z² − 4)^{(1/2−α)σ₃}.
  - Without this correction the probe error is O(1) and **N-independent**: about 0.65 off-diagonal at N = 10, 20, 40.
- **(b) D̃ on (−∞, 0) by analytic continuation.** Along the negative axis, t(x) crosses the negative real t-axis at
  |γ| = 2πe (x ≈ −1/(4π²e² − ¼) unrescaled). There the principal-branch formula
  √(2π)exp((t − ½)Log t − t − logΓ(t)) jumps.
  - The relevant D̃ is the analytic continuation from 0⁻: track log t continuously and use the entire function 1/Γ.
  - With it, ℓ̂ = 2arg D₊ is tame (range −0.010 … 0.366); the principal branch gives an artificial winding of ≈ 47.
  - B is built from the continued ℓ̂.

**Probe** (`checks/check_z_e2e.py`).
- **True side:** U from the true smooth-ζ OPs, with exact atoms j ≤ 60N and the tail beyond by a midpoint
  Euler–Maclaurin integral on log panels (insensitive to doubling K).
- **Model side:**
  - Lemma E1's N-dependent μ, through g and ℓ by integration by parts against A(u) on refined Gauss–Legendre grids;
  - D, B and K;
  - the Szegő function of w₀ and the Jacobi-type global N on [0, β̂].
- **Test:** M(z) := e^{−Nℓσ₃/2}U e^{Nφσ₃}F^{σ₃}N^{−1} must be a **constant** diagonal matrix plus O(1/N). The constant
  absorbs the omitted far-field scalars Ξ (§2). The quantities reported are |M_ii(z)/M_ii(z₀) − 1| and the
  D_∞-scaled off-diagonals at 7 points.
- **Validation** (MODEL=pp2: pure power p = 2 with masses 2x_j, the same code path). It reproduces the
  exact-moment RH_px reviewer probe (check_px_e2e.py 2 2) to 4 digits: N·max = 0.3768 vs 0.37671 at z = 1.2 + i,
  N = 40. Earlier runs needed log-spaced u-panels, because errors in g are multiplied by N in e^{Ng}.

**Result** (check_z_e2e_zeta.out, max over the 4 reported entries, times N):

| N  | z = 1.2+i | 0.5+0.8i | −1+0.5i | −1.5+0.5i | 2.5i | 3−1.2i | 4.5+1.5i | s·x_e (far end) |
|----|-----------|----------|---------|-----------|------|--------|----------|-----------------|
| 10 | 0.30 | 0.26 | 0.15 | 0.19 | 0.19 | 0.26 | 0.27 | 64 |
| 20 | 0.30 | 0.25 | 0.15 | 0.16 | 0.16 | 0.29 | 0.22 | 151 |
| 40 | 0.33 | 0.27 | 0.17 | 0.17 | 0.18 | 0.36 | 0.22 | 381 |

N·error is stable, so **VN^{−1} − I = O(1/N) near the band**. This holds with the N-dependent equilibrium of
Lemma E1 and the α = 5/8 shift. The omitted far-end scalars recede like s·x_e ~ N²/log²N and are invisible at this
accuracy. In the same runs, b_N/(β_N/4) − 1 = 0.0280, 0.0139, 0.0070 (N·dev ≈ 0.28; check_z_edge2 too) and
a_N/(2b_N) − 1 = 0.063, 0.033, 0.017 (N·dev ≈ 0.63–0.69).

**What Phases 3–4 must prove:**
1. **Far end.** The construction of §2 (split Ω_∞ at L, F_far, Ξ) with the α-shift built in. The continued D̃ and
   its cut structure on the negative axis beyond |γ| = 2πe. Monodromy bookkeeping.
2. **Uniformity in N** of the hard-edge (KMVV left endpoint, as RH_px §4.1) and Airy (with general α) parametrices.
   The rescaled data converge to p = 2 only at rate 1/log N.
3. **Small norm and extraction:** b_N = (β_N/4)(1 + O(1/N)) and a_N/(2b_N) = 1 + O(1/N). With E5, this gives
   **b_n/x_n = π²/16 + O(1/log n)** for the smooth-ζ model.

## 4. Phases 3–4: the argument (PROOF SKETCH; the far-field lemma is the main open technical step)

**Notation.**
- Rescaled variable z = sx, with s = 1/x_N.
- Band [0, β̂], with β̂ = sβ_N (Lemma E1).
- Saturated region (β̂, X_e), with X_e := s·x_e ≍ N²/log²N.
- The constraint ends at X_e with density vanishing linearly there. The atoms stop at the top node X₁ = s·x₁ < X_e.

**4.1 Transformations** (RH_px §3, with the α-shift):
- R and T as in RH_px, with Π, w(z) = 2z, θ = πt.
- μ = μ_N from Lemma E1 has **bounded support** (0, X_e]. So g(z) = log z + O(1/z), and T = I + O(1/z) at ∞. The
  unbounded-support normalization of RH_px Lemma 3.5 is not needed.
- On (β̂, X_e), T has the jump diag(e^{−2πit̂}, e^{2πit̂}), with t̂ := t − 3/8. On (X_e, ∞) it has none.

**4.2 Scalar functions and the far-field lemma.** Fix a closed curve C enclosing the band, the lenses, the saturated
region up to X₁ + δ′, and (−r, 0). C crosses ℝ at −r and at x_m ∈ (X₁ + δ′, X_e). Take r ≍ x_m ≍ X_e, with r below
the t-axis crossing at |γ| = 2πe.
- **Inside C**, F_in := D·B·K_α, where:
  - D = D̃/(1 − e^{∓2iθ}), with D̃ the continued Stirling–Binet function (§3(b));
  - B is the **full-axis** Binet-cut scalar on (−∞, 0), built from the continued ℓ̂. A cut only on (−r, 0) would create
    a power singularity at −r (Rule R F4).
  - K_α = (β̂ − z)^{−1/8}.
- **Outside C**, F_out := exp(∫_{β̂}^{X_e} t̂(y)dy/(y − z)). It is the exact scalar with jump e^{2πit̂}. Only its
  part outside C is used. The cut starts at β̂ (inside C), so F_out is regular at the crossing x_m; a cut starting at
  x_m would create a power singularity there. It is regular at X_e because t̂(X_e) = 0, and F_out → 1 at ∞.
- F_in uses the principal sheet of t in each half-plane. B makes D·B continuous across (−∞, 0).
- V := Q·F^{σ₃}, with F = F_in or F_out. V then has, besides the local jumps, the explicit diagonal jump
  (F_out/F_in)^{σ₃} on C. The cyclic condition holds at the two crossing points, because both F_in and F_out cancel
  T's real-axis jump there.

**Lemma Z (far field; TO PROVE).** log(F_out/F_in) has a continuous, single-valued branch on C. Then
Ξ := exp(∫_C log(F_out/F_in)dζ/(2πi(ζ − z))) is analytic off C and bounded at the crossing points, and
Ξ(z) = Ξ(0)(1 + O(|z|·sup_C|log(F_out/F_in)|/dist(C))) = Ξ(0)(1 + O(log^k N/N²)) near the band and both edges.
- sup_C|log(F_out/F_in)| grows like log N: 3.8, 5.5, 7.1 at N = 20, 40, 80.
- The measured log Ξ(z) − log Ξ(0) at z = 1.2 + i is 0.0049, 0.0019, 0.00072. It decays by a factor ≈ 2.6 per
  doubling.

Replacing F by **F·Ξ on both sides** (sign corrected, Rule R F4) removes the jump on C.
- C must also avoid the saddle level curve Im t = 0 that leaves x_e vertically. That curve carries D's poles at
  t = 0, −1, −2 and ends at the t-axis crossing. The chosen C (N-independent in x-units) stays outside it with margin
  |z − c₀|/R ≥ 1.21 (checks/check_z_saddle_curve.py).
- **What remains for a proof:** one N-independent *certified* winding computation (C is fixed in x-units), plus a
  uniform-in-N perturbation bound for log(F_out/F_in) on C. The local weights acquire the analytic,
near-constant factor Ξ^{±2}, which the Szegő function and the local parametrices absorb exactly.

*What is needed:*
- (i) **checked numerically** (checks/check_z_farfield.out, N = 20 and 40; C is a circle through −r, which lies inside
  the t-axis crossing, and through x_m ∈ (X₁, X_e)):
  - max |arg t| on C is about 2.86 < π, so the Stirling sector holds;
  - total winding of F_out/F_in = 0, to 10⁻⁸;
  - at x_m the ratio is continuous to 10⁻⁸;
  - at −r the jump of arg(F_out/F_in) is 4.5·10⁻⁴ at distance 10⁻³ and 6·10⁻⁵ at 10⁻⁶ from the axis. The limiting
    values ±4π give continuity mod 2π; the residual comes from the grid interpolation of ℓ̂.
- (ii) boundedness at the junctions, which is standard for scalar RHPs whose jump data satisfy the cyclic relation
  and are Hölder.

**4.3 Local parametrices, uniform in N.**
- **Hard edge 0 — OPEN (Rule R F1, major).** This is **not** RH_px §4.1 verbatim.
  - The band weight is w₀ ∝ z^{−1/2}·log(γ/2π)·(…), with an **unbounded log(1/z) factor** at 0. So h_N := w₀x^{1/2}/
    (smooth part) is not Hölder at 0. For example, at N = 1000, h_N = 1.21, 1.64, 2.27, 3.55 at x = 10⁻¹, 10⁻³, 10⁻⁶,
    10⁻¹². That is an O(1) variation at the Bessel scale x ~ N^{−2}.
  - The continued weight's jump on (−δ, 0) is −(Λ − iπ/2)/(Λ + iπ/2), with Λ = log(γ/2π) ~ log N, not the constant
    −1 of a pure x^{−1/2}.
  - So RH_px Lemmas 4.2(iii) and 4.3 do not apply as stated. The probe nonetheless shows O(1/N) near the band. A
    heuristic says the log-weight effect on b_N is O(1/(N log N)).
  - Needed: a **log-weight hard-edge lemma**. Candidate routes:
    - use the Szegő function D_w itself in place of W̃ and prove a lip-mismatch bound;
    - adapt Conway–Deift (SIGMA 2018), on log-type singular weights at a hard edge. That would need to be read and
      verified before citing.
- **Soft edge β̂:** WLXZ §6.1 for general α (here α_W = 5/8). WLXZ treat every α > 0; the local behaviour is
  V = O(1)(z − β̂)^{(1/2−α)σ₃}.
  - Uniformity: φ̃ = −κ̃_N(z − β̂)^{3/2}(1 + O(z − β̂)) with κ̃_N → κ̃_∞ > 0. This holds because the rescaled ρ_N
    converges to the p = 2 density uniformly near β̂, at rate 1/log N.
- **Top end and saturated lips:** Re φ̃ = ℓ/2 − U^μ < 0 on (β̂, X_e) (Lemma E1(iii)). Near X₁ ~ N²/log²N,
  U^μ − ℓ/2 ≥ c log(X₁/β̂). So the Σ^△ and segment entries are O(poly(N)·e^{−cN log N}), as in RH_px §4.3.

**4.4 Small norm and extraction.** As in RH_px §5:
- 𝒵 = I + O(1/N) in the D_{w,∞}-frame;
- (N₁)₁₂(N₁)₂₁ = (β̂/4)², and a(N) = β̂/2.

Hence **b_N = (β_N/4)(1 + O(1/N))** and **a_N/(2b_N) = 1 + O(1/N)**. Combined with E5,
b_n/x_n = π²/16·(1 + κ/log n + o(1/log n)), with κ = −0.2895.

Numerically: N·(b_N/(β_N/4) − 1) ≈ 0.27–0.28 (check_z_edge2.out, N ≤ 3200), and N·(a_N/(2b_N) − 1) ≈ 0.63–0.69
(check_z_e2e_zeta.out).

**Status:** PROOF SKETCH (conditional), numerically validated end to end (§3, §5). The open technical steps for
PROVED are the log-weight hard-edge lemma (F1, major) and:
- Lemma Z (the far field);
- the uniform-in-N versions of the two edge parametrices — routine, but they must be written;
- Rule R.


## 5. Rule R corrections (review/REVIEW_RHzeta.md), applied

- **Canonical numerical test** (F2, F3). The **absolute** test with Ξ built explicitly is
  `checks/check_z_e2e_xi.py` (the reviewer's probe, committed) with output `check_z_e2e_xi.out`. It reports
  max|D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}| with no free constant. N × error:

  | N  | 1.2+i | 0.5+0.8i | −1+0.5i | −1.5+0.5i | 2.5i | 3−1.2i | 4.5+1.5i |
  |----|-------|----------|---------|-----------|------|--------|----------|
  | 10 | 0.228 | 0.178 | 0.070 | 0.066 | 0.093 | 0.281 | 0.141 |
  | 20 | 0.234 | 0.181 | 0.078 | 0.073 | 0.100 | 0.311 | 0.154 |
  | 40 | 0.239 | 0.183 | 0.084 | 0.078 | 0.105 | 0.337 | 0.166 |

  - The §3 relative test is blind to constant diagonal factors, and it hid a probe bug.
  - That bug (F2): `Afun` used unsorted breakpoints. It is fixed in check_z_e2e.py, and check_z_e2e_zeta.out is
    regenerated.
  - Ξ is **not** invisible at N ≤ 40: abs(log Ξ(z) − log Ξ(z₀)) ≈ 0.011 at N = 20, the same size as the relative
    entries. It is asymptotically negligible.
- **Controls:**
  - no α-shift (κ_K = −½): the closure jump of log(F_out/F_in) is ≈ (3π/4)i, and N·err = 15–83. This confirms both
    the α-shift and that Lemma Z's continuity at x_m is the α-shift condition;
  - pp2 reference: check_px_e2e.py 2 2 → `check_px_e2e_p2s2_reference.out`.
- **F5 (gauge).** The cut t_c = 3/8 is a gauge, not canonical.
  - Any (t_c, α_W = 1 − t_c, K = (β̂ − z)^{t_c − 1/2}) works end to end; t_c = ½ with K ≡ 1 also passes.
  - β_N depends on t_c at O(1/N), so E4's constant 0.27 is the t_c = 3/8 convention (t_c = ½ gives 0.43).
  - E1's statement "the canonical constraint" should read "a constraint on the monotone branch t ≥ t_c". The O(1/N)
    claims are gauge-invariant.
- **F6 (κ).** The closed form is corrected: κ = −2(log(π/2) − (1 − log 2)) = −0.28946. A fit up to N = 10⁶⁰ with
  the secondary log log N/log N term gives a = −0.289472, agreeing to 1.2·10⁻⁵.
- **F4.** Lemma Z text corrected: full-axis B, F·Ξ on both sides, the log^k N bound, the saddle curve.
- **F8.** E3 monotonicity is now explicit. **F7:** §2 is marked superseded.
- **Labels:** see the status line. The §4 theorem is **not** PROVED.
