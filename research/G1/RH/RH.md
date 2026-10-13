# RH analysis for pure powers (Plan 10)

Status: Phases 0–1 written 2026-10-13. NOT REVIEWED. Notation: the weight exponent is **r** (r > 1), to avoid a clash
with the symmetric variable s.

## 0. Model and target

- **Measure.** σ = σ_{p,r} := Σ_{k≥1} k^{−r} δ_{x_k}, with x_k := k^{−p}, p > 0, r > 1. Its monic OPs are π_m, and its
  Jacobi coefficients a_m, b_m use item 11 indexing.
- **Target.** n^p b_n = c(p)(1 + d₁/n + O(n⁻²)) and a_n/(2b_n) = 1 + e₁/n + O(n⁻²).
- **Phase 0 numerics** (LOG.md) give d₁ = −(r−1)/2 and e₁ = p/2.

## 1. Symmetrization (option (i); Gate 1 decision)

Put q := p/2, s_k := k^{−q} (so s_k² = x_k), and ν := Σ_k (k^{−r}/2)(δ_{s_k} + δ_{−s_k}). Then ∫ f(s²) dν = ∫ f dσ.
- **Symmetric OPs.** The monic OPs R_N of ν satisfy R_{2m}(s) = π_m(s²) and R_{2m+1}(s) = s·π^{(1)}_m(s²), where
  π^{(1)} are the monic OPs of xσ.
- **Recurrence.** s R_N = R_{N+1} + γ_N² R_{N−1} (zero diagonal). The fold relations (as in `reference._fold`, which
  item 11 used for Lommel) are b_m² = γ_{2m−1}²γ_{2m}² and a_m = γ_{2m−2}² + γ_{2m−1}².
- **Translated target.** Pointwise Law P for σ is equivalent to γ_N² = c(p)(N/2)^{−p}(1 + o(1)) for both parities.
  The Phase 0 corrections become statements about γ_N² up to O(N⁻²). This translation is done in Phase 5.

**Why option (i).** In the x-variable the accumulation point x = 0 is the left *edge* of the band (G2: band (0, 4c)).
In the s-variable it is the band's *centre*, as in WLXZ. There WLXZ's parametrix at the origin (their §6.2) is
elementary: the local solution is N(z) times explicit triangular factors, with mismatch I + O(z²/n), followed by a
small-norm argument (their (6.24)–(6.28), read). This is the step the plan identified as the main risk. Option (i)
reduces it to a generalization of an existing construction.

## 2. Interpolation problem and rescaling

- **Interpolation problem.** Y(z) is meromorphic in ℂ ∖ {0}, with simple poles at the nodes ±s_k, and
  Res_{z=±s_k} Y = lim_{z→±s_k} Y(z)[[0, ν_k], [0, 0]] with ν_k := k^{−r}/2. Also Y(z)z^{−Nσ₃} → I as z → ∞. The
  solution is Y₁₁ = R_N, and Y₁₂ is the discrete Cauchy transform of R_N ν. The second row uses R_{N−1}, as in
  BKMM/WLXZ.
- **Rescaling.** U(z) := N^{qNσ₃}Y(N^{−q}z). Its nodes are ±Z_k with Z_k := (k/N)^{−q} ∈ (0, N^q].
- **Rescaled weight**, as in WLXZ (3.4): w(z) := N^{q}·½(N(z²)^{−1/p})^{−r}. This is analytic off the imaginary axis,
  and w(±Z_k) equals N^q times the mass k^{−r}/2.
- **Node-encoding function.**

    θ(z) := πN (z²)^{−1/p},  Π(z) := sin θ(z)/θ′(z),

  using the principal branch of (z²)^{−1/p}, whose cut is the imaginary axis (z² ≤ 0). For p = 1 this is WLXZ's
  θ = πn/z² with α = 0 (their α-shift is absent because our nodes start at k = 1).

**Lemma 1.1 (checked numerically to 30 digits in `checks/check_phase1.out`).**
- (a) θ(±Z_k) = πk.
- (b) Π(±Z_k) = 0 and Π′(±Z_k) = (−1)^k. Hence w e^{±iθ}/Π has residue exactly w(±Z_k) at ±Z_k, because
  e^{±iθ(±Z_k)} = (−1)^k.
- (c) In each closed sector |arg(±z)| ≤ π/2 − ε, the zeros of sin θ are exactly the nodes. The argument-principle count
  is 280.000 against 280 nodes in a box, for p = 1, 2 and 3.
- (d) e^{−iθ} decays in the upper-right and lower-left sectors, and e^{+iθ} decays in the upper-left and lower-right
  sectors. This is the same pattern as WLXZ's θ = nπ/z².

*Proof sketch.*
- (a) Direct.
- (b) Π′ = cos θ − sin θ·θ″/θ′², evaluated at θ = πk.
- (c) θ is real only on the real axis in these sectors: (z²)^{−1/p} has argument −2 arg(z)/p mod 2π. For p ≥ 1 this
  is nonzero mod π off the real axis within the sector. (For p < 1 there are extra rays where θ is real. **They must be
  checked when p < 1; Phase 1 is stated for p ≥ 1.**)
- (d) Im θ has the sign of −arg(z²) in the right half-plane, and symmetrically on the left.

## 3. Transformation to a Riemann–Hilbert problem (WLXZ §3 template)

- **Triangular factors.** As in WLXZ (3.9)–(3.10):
  - upper triangular U_±(z) := [[1, −w e^{±iθ}/Π], [0, 1]], used near the band;
  - lower triangular U^△_±(z) := Π^{−σ₃}[[1, 0], [−e^{±iθ}/(Πw), 1]], used near the saturated part.
- **Lemma 1.1(b) removes the poles.** In the regions where they are applied (Figure 3 analogue: lens regions above and
  below (−k_N, k_N), with k_N := N^q + δ, split at 0 and at ±r* into band and △ parts), R := U·U_± or U·U^△_± is
  analytic.
- **Cut.** It lies on the imaginary axis, so the regions where θ, Π and w must be analytic are those in sectors
  |arg(±z)| < π/2. The contours leave 0 at angles strictly inside these sectors. In the outer region Ω_∞ no factor
  is applied, so the cut is never crossed (Review Focus 1).
- **The band and the saturated part.** The band is (−r*, r*) with r* := 2^{1+q}√c(p): G2's band (0, 4c) for degree
  m = N/2 in x, mapped by Z² = 2^p·m^p x. For p = 1, r* = 2√(2·½) = 2, which is exactly WLXZ's band (−2, 2). The
  saturated part is r* < |Z| ≤ N^q.
- **Equilibrium in Z.** G2's μ* pushes forward under x ↦ ±√x. Each arcsine law on [0, β] becomes the symmetric arcsine
  on [−√β, √β]. So

    μ*_sym = ∫_0^1 ω^{sym}_{[−ρ_t, ρ_t]} dt,  ρ_t := r* t^{−q}.

  The variational conditions transfer from G2 B*: equality on the band, strict inequality on the saturated part.

**Gate 1: GO (option (i)), for p ≥ 1.** The RHP for R is well posed with the WLXZ structure. Open items for later
phases:
- the extra θ-real rays for p < 1;
- the sign conventions of g₊ + g₋ − l on the saturated part (Phase 2; WLXZ (4.4) is written for their normalization);
- the end of the node set at |Z| = N^q (Review Focus 4).
