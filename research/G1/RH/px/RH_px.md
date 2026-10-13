# RH_px: pointwise Law P for σ_{p,s} = Σ k^{−s} δ_{k^{−p}}, p > 1, in the x-variable (Plan 12)

Status: **IN PROGRESS** (Phases 0–2 done, Gates 1–2 GO; Phase 3 next). Not reviewed. No PROVED labels.

## 0. Model, target, baseline

- σ := σ_{p,s} with p > 1, s > 1. It has monic OPs π_n and Jacobi coefficients a_n, b_n.
- Target: n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n).
- Phase 0 baseline (Plan 10, `../checks/check_fine.out`, NUMERICAL): n^p b_n/c(p) = 1 + d₁/n + … and
  a_n/(2b_n) = 1 + e₁/n + …, with d₁ = −(s−1)/2 and e₁ = p/2 exactly for p ∈ {1.5, 2, 3}. There is no (−1)^n term in
  the x-variable: the symmetric (−1)^N terms of RH₁(r) cancel in the fold.

## 1. Interpolation problem in x (Phase 1; Gate 1 GO)

**Rescaling.** Fix the degree N. Put U(z) := N^{pNσ₃} Y(z/N^p). Then:
- the nodes are X_k = (N/k)^p, k ≥ 1, accumulating at 0;
- the top node is X₁ = N^p;
- the index function is t(z) := N z^{−1/p} (principal branch, cut (−∞, 0]), with t(X_k) = k;
- θ := πt, Π := sin θ/θ′, and w(z) := N^p t(z)^{−s}, so that Res_{X_k} U₁₂ = w(X_k)U₁₁(X_k).

**Lemma 1.1 (slit plane, p > 1).** On ℂ ∖ (−∞, 0], arg t = −arg z/p ∈ (−π/p, π/p) ⊂ (−π, π). So Γ(t), Γ(t+1) and
Stirling's series for t are pole-free and valid there. ∎ (This fails for p < 1: Γ's poles enter on the rays arg z = ±pπ.)

**Transformations** (WLXZ §3 template, one-sided):
- Above the band, R = U·[[1, −we^{−iθ}/Π], [0, 1]]. In ℂ₊, Im θ < 0, so |e^{−iθ}| < 1.
- Above the saturated region, R = U·Π^{−σ₃}[[1, 0], [−e^{−iθ}/(Πw), 1]] (WLXZ (3.10) and (3.15)).
- Mirror images below the real axis.
- **Checks** (`checks/check_px_phase1.out`, p = 2, s = 3, N = 12, K = 3000 atoms, dps 80). Approaching a band node
  X₃₆ = 1/9, |U₁₂| ~ 1/dist (3e7 → 3e15), while |R₁₂| → 2726409.516 and |R₂₂| → 1.3190549e−6 converge. At a
  saturated node X₆ = 4, R₁₁ and R₁₂ also converge.

**Lemma 1.2 (band weight).** W := 2iθ′w satisfies

  |W(x)| = (2π/p)N^{1+p−s}x^{(s−1−p)/p},  arg W = −π/2.

So the band weight has a **hard-edge Jacobi exponent α_x := (s−1−p)/p at x = 0**, with α_x > −1 ⇔ s > 1. On the
regular family s = 1 + p, W ≡ −2πi/p. (Checked: |W| = π to 12 digits at x = 0.05, 0.5, 2 for p = 2, s = 3.)

Consistency: in the symmetric variable the FH exponent was a = (2s−2−p)/(2p), and |s|^{2a}ds = ½x^{a−1/2}dx, with
a − ½ = α_x.

## 2. g, φ, sign structure (Phase 2; Gate 2 GO)

**Input from G2** (REVIEWED). Put β_τ := 4c(p)τ^{−p} and μ* := ∫₀¹ ω_{[0,β_τ]}dτ, where ω is the arcsine law. The node
density is ρ(x) := (1/p)x^{−1−1/p}, so that ∫_x^∞ ρ = x^{−1/p} = t(x)/N. Then:
- dμ*/dρ = I_{min(1,x/4c)}(1/p + ½, ½) (regularized incomplete beta). So ψ := dμ*/dx < ρ on the band (0, 4c) and
  ψ = ρ on the saturated region [4c, ∞).
- U*(x) := ∫log|x − y|dμ* = log c + p on (0, 4c], and U* ≥ log c + p on (0, ∞) (B*(ii)).
- Near 0, ψ ~ C x^{−1/2}, since each arcsine law has an x^{−1/2} edge. So x = 0 is a **hard edge**. ρ ~ x^{−1−1/p} ≫ ψ
  there, so the band reaches 0.

**Definitions.**
- g(z) := ∫log(z − y)dμ*(y) = ∫₀¹ 2log((√z + √(z − β_τ))/2)dτ.
- l := 2(log c + p).
- φ := l/2 − g.
- φ̃ := φ ± iθ/N in ℂ± (the corrected sign; REVIEW_RH.md).

**Lemma 2.1.**
- (i) φ₊ + φ₋ = 0 on (0, 4c).
- (ii) g₊ − g₋ = 2πiμ*((x, ∞)) = 2iθ/N on (4c, ∞). Hence φ̃ has no jump on (4c, ∞).
- (iii) **Strictness:** Re φ̃(x) = log c + p − U*(x) < 0 for x > 4c.

*Proof.* (i) and (ii) follow from B*(ii) and ∫_x^∞ρ = t/N. For (iii), Re g′(x) = ∫_{t_x}^1 dτ/√(x(x − β_τ)) > 0 for
x > 4c, where t_x := (4c/x)^{1/p} < 1. The terms with τ < t_x are purely imaginary. So U* is strictly increasing on
(4c, ∞). This settles the strictness that REVIEW_RH.md asked about for Lemma 2.2. ∎

**Lemma 2.2 (signs off the axis).** At real x,
- ∂_y Re φ(x + iy)|_{y=0⁺} = −πψ(x);
- ∂_y Re φ̃(x + iy)|_{y=0⁺} = π(ρ − ψ)(x).

Hence, for small ε > 0 (locally uniformly):
- **band lips:** Re φ < 0 and Re φ̃ > 0, so both e^{2Nφ} and e^{−2Nφ̃} decay. This is the missing condition of
  REVIEW_RH.md item 4.
- **above the saturated region:** Re φ̃ < 0, by Lemma 2.1(iii) and continuity.

Mirror statements hold in ℂ₋.

*Proof.* By Cauchy–Riemann, g′(x + i0) = PV∫dμ*/(x − y) − iπψ, and θ′/N = −πρ. ∎

**Checks** (`checks/check_px_phase2.out`, p ∈ {1.5, 2, 3}):
- U* − (log c + p) ≤ 3e−25 on the band, and it is positive and increasing on the saturated side;
- ψ/ρ ∈ (0, 1) on the band;
- at ε = 10⁻³ and 10⁻²: Re φ < 0 and Re φ̃ > 0 above the band, and Re φ̃ < 0 above the saturated region.

Near the hard edge Re φ̃ is large (e.g. 1.15 at x = 0.01·4c, p = 1.5), because ρ ≫ ψ.

## 3. Next (Phase 3)

- D̃ := exp(−μ(t)), where μ is the Binet function (lnΓ(t) = (t − ½)ln t − t + ½ln 2π + μ(t)). D := D̃/(1 − e^{∓2iθ})
  in ℂ±.
- Find the jump of D on (−∞, 0).
- Build the scalar Szegő function for the band weight together with the (−∞, 0) jump, with a power normalization at ∞.
- Build the global parametrix.
- Gate 3.
