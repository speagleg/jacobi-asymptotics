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

## 6. Phase 3: R-jumps, D-functions, global parametrix — and a scope finding

**6.1 The R-problem, verified end to end** (`checks/check_phase3a.out`). I built Y from the actual symmetric OPs of ν
(p = 2, r = 2, N = 24, 8000 nodes, dps 60), rescaled it to U, and applied the WLXZ upper-right factor.
- Approaching the band node Z₃₀ = 0.8, |U₁₂| grows like 1/dist (2.5e14 → 2.5e18), while |R₁₂| → 3.1175e13 and
  |R₂₂| → 5.219e−14 converge. So the poles are removed.
- The real-axis jumps of R have WLXZ (3.19)–(3.22) form with γ → θ′ and w → our w. The band jump is
  [[1, W], [0, 1]] with W := 2iθ′w on (0, r*), and the mirrored form on (−r*, 0). So the effective weight on the whole
  band is −2i|θ′|w.

**Lemma 3.1 (constant band weight; PROVED, checked).**

  |θ′(x)|w(x) = (π/p)·N^{1+q−r}·|x|^{2(r−1)/p−1}.

On the regular family r = 1 + p/2, this is the constant π/p. The check gives W ≡ −i·2π/p, i.e. −πi for p = 2, to 12
digits at x = 0.4, 1.3 and 2.9. So the band problem is of Legendre type, and after the E-normalization of a Jacobi type
with an explicit Szegő function.

**6.2 D-functions.** With t := θ/π:
- D̃(z) := √(2π) t^{t−½} e^{−t}/Γ(t), so that D̃ = 1 + O(1/t) by Stirling;
- D := D̃/(1 − e^{∓2iθ}) in ℂ±, which has poles at the nodes;
- E(z) := (z² − r*²)^{(p−1)/(2p)}(r*² − z²)^{−1/2}. This generalizes WLXZ (4.19): the second factor gives the −1 jump
  across |x| > r*, and the first restores DE → const at ∞ for p ≠ 1.

Checks for p = 2 (`checks/check_phase3b.out`):
- D₊E₊ = D₋E₋e^{2iθ} on x > k_N to 1e−26, which matches the T-jump diag(e^{−2iθ}, e^{2iθ}) there;
- |DE| → 1/√(2πN) at infinity in every direction (0.0892 at N = 20, 0.0631 at N = 40);
- D̃ − 1 = O(1/N) on compacts (4e−3 → 2e−3).

The left half needs the mirrored functions (D̂, Ê, built from −z, as in WLXZ (4.22)–(4.25)). The check confirms
that the right-side functions do not serve there (error 1.8).

**6.3 Global parametrix (regular family, p ∈ {1, 2}).** After the D/E normalizations the band jump is
[[0, w₀/D̃²], [−D̃²/w₀, 0]], with w₀ := W/E² and D̃² = 1 + O(1/N). On the regular family W is constant, so
w₀ ∝ (r*² − x²)^{1/2}·(phases from the branches) on the band: a Jacobi-type weight. The global parametrix is the
standard

  N(z) = F_∞^{σ₃} N₀(z) F(z)^{−σ₃},  N₀ = [[(a + a⁻¹)/2, (a − a⁻¹)/(2i)], [−(a − a⁻¹)/(2i), (a + a⁻¹)/2]],
  a(z) = ((z − r*)/(z + r*))^{1/4},

where F is the (explicit) Szegő function of w₀ on [−r*, r*]. Leading-order output: γ_N = (r*/2)N^{−q}(1 + o(1)), so
γ_N² = c(p)(N/2)^{−p}, which is Law P (§1). This is the global-parametrix level only. The local parametrices (Phase 4)
and the small-norm argument (Phase 5) are still needed for a proof.

**6.4 Scope finding (Gate 3).** The D-functions need t(z) = θ(z)/π to be single-valued in each half-plane off the real
axis. In the symmetric variable, t(z) = N(z²)^{−1/p} is single-valued on ℂ ∖ {0} **iff 2/p ∈ ℤ**: N/z² for p = 1
(WLXZ) and N/z for p = 2. For other p ≥ 1, t has a branch cut on the imaginary axis, *inside* ℂ±, where the D-functions
and the global transformation must be analytic. So the WLXZ machinery does not transfer verbatim. Options for general
p:
- (a) work in x (option (ii)), where t = Nx^{−1/p} has its cut on (−∞, 0], away from all nodes. This costs a new edge
  parametrix at the accumulation point x = 0, and a check of D's jump on (−∞, 0];
- (b) a sectorial construction of D (separate functions in |arg z| < π/2 and in the left sectors, matched on the
  imaginary axis).

**Gate 3: GO for p ∈ {1, 2}; general p deferred with the precise obstruction above.**

**What p ∈ {1, 2} buys.** Theorem H itself was already known for p ∈ {1, 2} (item 11), and the regular weights
r = 1 + p/2 are the exactly solvable families. So the new content of the RH route for p ∈ {1, 2} is the *pointwise*
law for weights r ≠ 1 + p/2. That needs the Fisher–Hartwig/Bessel origin parametrix (§5) with α = (2r − 2 − p)/(2p).
This includes the Haynes–Zudilin a = 2 measures (r = 4 + b ≥ 5, α = (r − 2)/2 ≥ 3/2) and Monien's a = 1 measures.

## 7. Phase 4: local parametrices (p ∈ {1, 2})

**Lemma 4.1 (square-root edges; PROVED).** Near x = r*,

  (node density − ψ)(x) = √(r*² − x²)/(πq r*²)·(1 + O(r* − x)).

*Proof.* For x < r* near r*, the difference is (1/π)∫_1^{t_x} dt/√(ρ_t² − x²). Linearize
ρ_t² − x² ≈ (r*² − x²) − 2qr*²(t − 1); the endpoint t_x − 1 is where this vanishes. The integral equals
2√(r*² − x²)/(2qr*²) to leading order. ∎

Numerically, the ratio to √(r* − x) converges to √2/(πq r*^{3/2}): 0.318, 0.0808 and 0.0295 for p = 1, 2, 3
(`checks/check_phase4.out` [1]). So the band–saturated edges ±r* are of standard square-root type. **Airy
parametrices** apply there, in the band–saturated form of WLXZ §6.1, with f̃ = (−(3/2)Nφ̃)^{2/3} (their (2.5)).

**Lemma 4.2 (regular origin; PROVED).** ψ(0) = (1/π)∫_0^1 dt/ρ_t = 1/(πr*(q+1)) > 0. Checked to 10 digits for
p = 1, 2, 3. So 0 is an interior band point, and KV's conformal map f(z) = ±iφ(z) − iφ₊(0), with f′(0) = πψ(0), is
available.

**Proposition 4.3 (origin = KV local problem).** Near 0:
- the band jump is [[0, w₀/D̃²], [−D̃²/w₀, 0]], with w₀ ∝ |x|^{2α}h(x), h analytic and nonvanishing near 0
  (Lemma 3.1, E analytic near 0, D̃ = 1 + O(z/N));
- the lens and R-contours near 0 carry WLXZ (6.24)-type jumps [[1, 0], [c(z)e^{2Nφ}, 1]], with c analytic, on four
  contours meeting at 0.

This is the KV §5 local problem ((5.1)–(5.2)) with α = (2r − 2 − p)/(2p), after the analytic factor h is absorbed
into the Szegő function, as KV do for |x|^{2α}e^{−nV}. KV build its solution from Bessel functions of order α ± ½
(their §5, via Vanlessen [38]), with matching I + O(1/N). For α = 0 it reduces to WLXZ's elementary §6.2 parametrix.

*Status.* The structural hypotheses are verified (Lemmas 3.1, 4.2 and the jump forms). The exact analytic prefactors
near 0 in our notation still need full bookkeeping (Phase 5) before this is a proof. Label: **STRUCTURE VERIFIED,
mod-cite (KV §5)**.

**Lemma 4.4 (top of the node set: no parametrix).** On the saturated part outside a fixed disc around r*, up to the
last node k_N = N^q, the lower-triangular saturated jump entry is exponentially small. Even the *raw* entry, before
the Szegő/E normalization and with polynomial N-factors, gives

  sup |θ′/w|·|D̃|²·e^{N(l − 2Re g)} = 0.0795, 2.9e−3, 9.9e−7, 2.7e−14 (r = 2) and 1.9, 0.28, 3.8e−4, 4.2e−11 (r = 4)

for N = 20, 40, 80, 160 (p = 2, x ∈ [1.3r*, k_N]). The decay comes from l − 2Re g < 0 (Lemma 2.2), which grows in
magnitude towards the top, while D̃ stays bounded at t ≈ 1 (√(2π)e^{−1} ≈ 0.92). Beyond k_N the DE functions remove
the jump exactly (§6.2). NUMERICAL, supporting Review Focus 4.

**Gate 4: GO (p ∈ {1, 2}).** Every local problem is identified with a cited construction whose hypotheses are
checked:
- Airy at ±r*: square-root vanishing (Lemma 4.1);
- Bessel (KV §5) at 0: regular interior point (Lemma 4.2), Fisher–Hartwig exponent α (Lemma 3.1);
- none at the top: exponential smallness (Lemma 4.4).

**Remaining for Phase 5:**
- exact jump bookkeeping in our notation (the V-jumps, the WLXZ (5.3)–(5.4) analogues with the mirrored left-side
  functions);
- the small-norm estimate;
- extraction of γ_N, hence a_n and b_n, with the target corrections d₁ = −(r−1)/2 and e₁ = p/2 from Phase 0 as the
  acceptance test.

## 8. Phase 5: assembly, numerical acceptance, extraction (p = 2 tested; p ∈ {1, 2} in scope)

**8.1 The final problem (bookkeeping as derived).** The transformations follow WLXZ §§4–6, with γ → θ′,
n/z² → t(z) = N(z²)^{−1/p}, band 2 → r*, and their α-shift absent:
- T = e^{−Nlσ₃/2} R e^{N(l/2 − g)σ₃};
- lens opening Q by the factorization WLXZ (4.11)–(4.13);
- normalization V by the D-functions of §6.2: D̃ and D on the right, the mirrored D̂ and Ê on the left, and E;
- S = V·(parametrix)⁻¹, with the global N of §6.3, Airy discs at ±r* (§7) and the KV Bessel disc at 0 (§7).

The resulting S-jumps are I + O(1/N) on the disc boundaries and exponentially small elsewhere (Lemmas 2.3 and 4.4).
The standard small-norm theorem then gives S = I + O(1/N) uniformly (as in KV §6, "Third transformation S → R").
**Caveat.** The prefactors in these jumps were set up by analogy with WLXZ's (5.3)–(5.4), whose PDF text is partly
garbled. They are validated numerically below, not yet written out symbol by symbol in our notation.

**8.2 Acceptance test A: outer strong asymptotics** (`checks/check_phase5.out` [A]). If S = I + O(1/N), then
T₁₁(z) := N^{qN}π_N(N^{−q}z)e^{−Ng(z)} on Ω_∞ equals (an N-power normalization) × (a fixed analytic function)
× (1 + O(1/N)). Observed for p = 2, with r = 2 (α = 0) and r = 3 (α = ½), at N = 20 … 240:
- |T₁₁(2i)| ∝ 1/N exactly (0.0199, 0.00996, 0.00499, 0.00249, 0.00166);
- the ratios T₁₁(3+3i)/T₁₁(2i) and T₁₁(−5+i)/T₁₁(2i) converge at rate O(1/N) (successive differences 2e−3, 1e−3,
  6e−4, 2e−4).

A wrong g-function, band or normalization would show exponential drift (e^{±cN}). So the equilibrium, the g-function
and the overall RH structure are confirmed to exponential precision, and the 1/N rate is consistent with the small-norm
claim.

**8.3 Acceptance test B: extraction** ([B]). With γ_N² from the actual measure (unfolded from a_m, b_m):

  γ_N²/(c(p)(N/2)^{−p}) − 1 = (k₀ + k₁(−1)^N)/N + O(N⁻²),

with k₀ = −2.000, k₁ = 0.000 for r = 2 (α = 0), and k₀ = −2.996, k₁ = −1.995 for r = 3 (α = ½). The leading term
c(p)(N/2)^{−p} is the global-parametrix prediction γ_N = (r*/2)N^{−q} (§6.3). The parity-alternating correction
appears exactly when α ≠ 0, which is the signature of the Fisher–Hartwig/Bessel origin (§5).

**Lemma 5.1 (unfolding; PROVED, elementary).** Suppose γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + O(N⁻²)). Then the
fold relations b_m² = γ_{2m−1}²γ_{2m}² and a_m = γ_{2m−2}² + γ_{2m−1}² give

  m^p b_m/c = 1 + (p/2 + k₀)/(2m) + O(m⁻²),  a_m/(2b_m) = 1 + (p/2)/m + O(m⁻²).

So **e₁ = p/2 for every weight**, because the parity term and k₀ cancel. This explains Phase 0's observation that e₁
does not depend on r. Also d₁ = (p/2 + k₀)/2. With the measured k₀ = −r (p = 2) this gives d₁ = −(r−1)/2, matching
Phase 0.

*Proof.* Use γ_{2m}² = cm^{−p}(1 + (k₀ + k₁)/(2m)) and γ_{2m−1}² = cm^{−p}(1 + p/(2m))(1 + (k₀ − k₁)/(2m)), and
(m−1)^{−p} = m^{−p}(1 + p/m), to first order. Multiply the expansions for b_m and add them for a_m. ∎

**8.4 Status of the pointwise theorem (p ∈ {1, 2}).**

> **Theorem RH (target).** For σ_{p,r} = Σ k^{−r}δ_{k^{−p}}, with p ∈ {1, 2} and r > 1:
> n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n).

- **Label: PROOF SKETCH, numerically validated.**
- What is in place:
  - the RH formulation (verified end to end, §6.1);
  - the g-function and all sign conditions (proved, §4);
  - the global parametrix (explicit, §6.3);
  - every local problem identified, with its hypotheses checked: Airy (§7, Lemma 4.1), Bessel/KV (§7), the top end
    (Lemma 4.4);
  - acceptance tests A and B passed.
- What is missing for PROVED:
  1. writing every jump matrix of V and S symbol by symbol, including the mirrored left-side functions and the exact
     analytic prefactor of the KV problem at 0;
  2. the small-norm estimate with explicit uniformity, including the contour pieces near 0, where the lens and
     R-contours meet;
  3. an independent Rule R check of 1–2.
- For p ∉ {1, 2} the construction needs a new D-function (§6.4). Out of scope.
