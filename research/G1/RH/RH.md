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

## 4. Phase 2: g-function, φ-functions, sign structure

**Definitions.**

  g(z) := ∫ log(z − y) dμ*_sym(y) = ∫_0^1 log((z + z√(1 − ρ_t²/z²))/2) dt,
  g′(z) = ∫_0^1 dt/(z√(1 − ρ_t²/z²)),

with ρ_t = r* t^{−q} and branches ∼ log z and 1/z at ∞. The Lagrange constant is l := 2Re g(0⁺). Put φ := l/2 − g on
ℂ±. On the saturated part, put φ̃ := φ ∓ iθ/N (+ const), as in WLXZ (2.4) (their 2πi/s³ is −iθ′/n for θ = nπ/s²).

**Lemma 2.1 (density; PROVED).** μ*_sym has density

  ψ(x) = (1/π)∫_0^{min(1,t_x)} dt/√(ρ_t² − x²),  t_x = (r*/|x|)^{1/q}.

On |x| ≥ r* it equals the node density (1/q)|x|^{−1−1/q} (N nodes, mass 1/N each); on |x| < r* it is strictly smaller.
This is G2 B*(i) pushed forward under x ↦ ±√x, since each arcsine law on [0, β] maps to the arcsine law on [−√β, √β].
For p = 1, ψ coincides with WLXZ (2.1) (checked to 10 digits).

**Lemma 2.2 (variational conditions; PROVED).**
- For a symmetric measure, ∫ log|Z − Y| dμ*_sym(Y) = ½U*(Z²) after rescaling. So G2 B*(ii) gives
  g₊ + g₋ = 2Re g = l on the band, and > l on the saturated part.
- Numerically: |2Re g − l| ≤ 7e−13 on the band, and 2Re g − l = 0.0037, 0.75, 3.03 (p = 1) at x/r* = 1.01, 1.5, 4.

**Lemma 2.3 (lens signs; PROVED).**
- **Over the band** (|x| < r*): Re φ(x + iy) = −½∫ log(1 + y²/(x − s)²) dμ*_sym(s) < 0 for every y ≠ 0, because
  Re g(x) = l/2 on the band. So the lens factors e^{2Nφ} are exponentially small on the lens boundaries away from the
  real axis. Numerically, Re φ = −0.017, −0.008, −0.004 at y = ±0.05 (p = 1, 2, 3).
- **Over the saturated part:** φ̃ has no jump across it, because −g′ ∓ iθ′/N removes the jump −2πiψ, where ψ equals
  the node density there. Re φ̃(x) = l/2 − Re g(x) < 0 strictly there, with values −0.02, −0.72, −2.48 (p = 1) at
  x/r* = 1.05, 2, 10. By continuity Re φ̃ < 0 in a thin lens, uniformly away from ±r*. The growth of 2Re g − l as
  |x| → ∞ keeps this uniform up to the top node N^q.

**Gate 2: GO.** All sign conditions needed for lens opening hold, with strict signs away from ±r*. The left
half-plane is handled by symmetry. My transcription of WLXZ (4.2) used the principal √(z² − 4), which behaves like −z
for Re z < 0; this caused the apparent g′ mismatch at −1.5 + 2i. Their branch behaves like +z. Our t-integral uses the
correct branch.

## 5. Structure found for Phases 3–4: the origin is a Fisher–Hartwig point unless r = 1 + p/2

Near z = 0 the jumps involve w/Π = wθ′/sin θ. Here w(z) ∝ (z²)^{r/p} and θ′(z) ∝ z(z²)^{−1/p−1}, so

  wθ′ ∝ z^{−1}(z²)^{(r−1)/p} ∝ |z|^{2α}·(sign factors),  α := (2r − 2 − p)/(2p).

- **α = 0, i.e. r = 1 + p/2.** The power cancels, and the origin is regular, exactly as in WLXZ. This holds for
  Tricomi–Carlitz (p = 1, r = 3/2) and for Lommel ν = ½ (p = 2, r = 2). There the elementary WLXZ origin parametrix
  (I + O(z²/N) matching) should carry over directly.
- **α ≠ 0.** The weight has a root-type (Fisher–Hartwig) singularity |z|^{2α} at the interior band point 0. The
  standard remedy is a Bessel-function local parametrix (Kuijlaars–Vanlessen type, for |x|^{2α} at an interior point),
  composed with the WLXZ triangular factors. **Not yet read: a citation task for Phase 4.**
- **Suggested order.** Phases 3–5 first for the regular family r = 1 + p/2 (every p ≥ 1). Then the general r via the
  Bessel parametrix. Phase 0's d₁ = −(r−1)/2 becomes −p/4 on the regular family.
