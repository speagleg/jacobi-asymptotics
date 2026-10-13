# Theorem RH for p = 2: full steepest-descent bookkeeping

Status: written 2026-10-13. NOT REVIEWED. This upgrades RH.md §8.4 from a proof sketch: every transformation, jump
and estimate is written out. The local parametrices are cited constructions (Airy: WLXZ §6.1; Bessel: KV §5), with
their hypotheses verified here. Notation follows RH.md, with p = 2 and q = 1. For p = 1 replace t(z) = N/z by N/z²
(see §9).

## 0. Statement

**Theorem RH (p = 2).** Let r > 1 and σ := Σ_{k≥1} k^{−r} δ_{k^{−2}}. Then, as n → ∞,

  n² b_n = c(2)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n),  c(2) = π²/16.

Equivalently, for the symmetrized measure ν = Σ_k (k^{−r}/2)(δ_{1/k} + δ_{−1/k}) (RH.md §1), the recurrence
coefficients satisfy γ_N = (r*/2)N^{−1}(1 + O(1/N)), with r* = 2^{1+q}√c(p) = 4·(π/4) = π for p = 2. The equivalence is Lemma 5.1 of RH.md together with the fold relations.

## 1. Data

- **Nodes.** ±Z_k, with Z_k := N/k (k ≥ 1), in the rescaled variable z = Ns, where s is the variable of ν.
- **Node function.** θ(z) := πN/z. It is odd, analytic on ℂ ∖ {0}, and θ(±Z_k) = ±πk.
- **θ′(z)** = −πN/z². It is even and negative on ℝ ∖ {0}.
- **Π** := sin θ/θ′. Then Π(±Z_k) = 0 and Π′(±Z_k) = cos(±πk) = (−1)^k.
- **Weight.** w(z) := (N/2)N^{−r}(z²)^{r/2}, using the principal branch. The cut is the imaginary axis, and
  w(±Z_k) = N·(mass k^{−r}/2), which is the residue factor after rescaling (§2).
- **Effective band weight.** W(z) := 2iθ′(z)w(z) = −iπN^{2−r}(z²)^{(r−2)/2}. On ℝ: W(x) = −iπN^{2−r}|x|^{r−2}. Its
  modulus is π (= 2π/p) for r = 2, and in general it carries |x|^{2α}, with α = (r−2)/2 = (2r − 2 − p)/(2p).
- **Decay.** For z = x + iy: Im θ = −πNy/|z|². So |e^{−iθ}| = e^{−πNy/|z|²} < 1 on ℂ₊ and |e^{iθ}| < 1 on ℂ₋. *This
  differs from the even case of RH.md Lemma 1.1(d). Because θ is odd here, one factor serves each whole half-plane.*

## 2. Y → U → R

- **Y.** The interpolation problem of RH.md §2: Y₁₁ = R_N(s); Y₁₂ = Σ ν_j R_N(s_j)/(s − s_j) over both signs of the
  nodes; Y₂₁ = R_{N−1}(s)/h_{N−1}; Y₂₂ = Σ ν_j R_{N−1}(s_j)/(s − s_j)/h_{N−1}, where h_n := Σ ν_j R_n(s_j)². Then
  Y(s)s^{−Nσ₃} → I as s → ∞.
- **U.** U(z) := N^{Nσ₃}Y(z/N). Then U(z)z^{−Nσ₃} → I, and Res_{±Z_k}U = lim U(z)[[0, w(±Z_k)], [0, 0]].
- **Regions.** Fix δ > 0 small and k_N := N + ½ (between the top node N and ∞). Above the real axis:
  - Ω_b⁺ is bounded by (−r*, r*) and the arc Σ_b⁺ from −r* to r* through iδ, and contains 0 on its boundary. (The
    arcs leave ±r* and pass near 0 at angles in (0, π/2) to the real axis; the contour is pinched at 0, see §6.)
  - Ω_s⁺ is the pair of regions above (r*, k_N) and (−k_N, −r*), bounded by arcs Σ_s⁺ and by the vertical segments
    ±r* + i(0, δ).

  Mirror these below the axis to get Ω_b⁻, Ω_s⁻. The outer region is Ω_∞.
- **Factors.**

    R := U·[[1, −w e^{−iθ}/Π], [0, 1]]               on Ω_b⁺,
    R := U·[[1, −w e^{+iθ}/Π], [0, 1]]               on Ω_b⁻,
    R := U·Π^{−σ₃}[[1, 0], [−e^{−iθ}/(Πw), 1]]       on Ω_s⁺,
    R := U·Π^{−σ₃}[[1, 0], [−e^{+iθ}/(Πw), 1]]       on Ω_s⁻,
    R := U                                           on Ω_∞.

**Lemma P1 (no poles; PROVED).** R is analytic at every node.
- On Ω_b±: the residue of the (1,2) entry of R is w(Z)·U₁₁(Z) − (residue of w e^{∓iθ}/Π)·U₁₁(Z), and the second term
  equals w(Z)U₁₁(Z) by §1. The other entries are unaffected.
- On Ω_s±: the (1,2) entry is U₁₂Π, where the zero of Π cancels the pole. The residue of the (1,1) entry is
  U₁₁(Z)/Π′(Z) − w(Z)^{−1}U₁₂-residue·e^{∓iθ(Z)}/Π′(Z) = (−1)^k[U₁₁(Z) − U₁₁(Z)] = 0, as in WLXZ (3.15)–(3.17).
- Checked numerically from actual OPs (RH.md §6.1). ∎

**Jumps of R** (orientation left to right on ℝ; upper arcs from left to right; ₊ is the left side). U has no jump
off the nodes, so each jump is a product of factors:
- (R-a) Band (−r*, r*) ∖ {0}: J_R = [[1, W], [0, 1]], since (w e^{iθ} − w e^{−iθ})/Π = 2iθ′w = W.
- (R-b) Saturated (r* < |x| < k_N): J_R = [[1, 0], [2iθ′/w, 1]], since (e^{iθ} − e^{−iθ})/(Πw) = 2iθ′/w.
- (R-c) Upper arcs Σ_b⁺: J_R = [[1, w e^{−iθ}/Π], [0, 1]]. Lower arcs Σ_b⁻: J_R = [[1, −w e^{iθ}/Π], [0, 1]]. The
  saturated arcs and the vertical segments get the analogous products of the two adjacent factors.
- (R-d) |x| > k_N: no jump.

**Behaviour at 0.** U₁₂ and U₂₂ are discrete Cauchy transforms with masses accumulating at 0. On the arcs near 0,
|e^{∓iθ}| = e^{−πNy/|z|²} decays super-exponentially along every ray into the half-plane. So R stays bounded as z → 0
within each sector, and R = O(1, log|z|) (WLXZ (3.24)), which makes the R-problem uniquely solvable. ∎

## 3. g-function and T

- **g.** g(z) := ∫ log(z − y) dμ*_sym(y), with the explicit formula of RH.md §4. g(z) = log z + O(z⁻²) at ∞, because
  μ*_sym is symmetric.
- **Constants.** l := 2Re g₊(0⁺). Put Φ(x) := μ*_sym((x, ∞)), so that g₊ − g₋ = 2πiΦ on ℝ and Φ(x) = 1/x for
  x ≥ r* (node density 1/x²; q = 1).
- **T.** T := e^{−Nlσ₃/2} R e^{N(l/2 − g)σ₃}.

**Jumps of T.**
- (T-a) Band: J_T = [[e^{−2πiNΦ}, W], [0, e^{2πiNΦ}]], because g₊ + g₋ = l there (RH.md Lemma 2.2).
- (T-b) Saturated: J_T = [[e^{−2iθ}, 0], [(2iθ′/w)e^{N(l − g₊ − g₋)}, e^{2iθ}]]. Here NΦ(x) = N/x = θ/π for x > r*,
  and the same identity holds for x < −r* because N ∈ ℤ.
- (T-c) |x| > k_N: J_T = diag(e^{−2iθ}, e^{2iθ}).
- (T-d) Arcs: J_T = e^{−N(l/2−g)σ₃} J_R e^{N(l/2−g)σ₃}. On Σ_b⁺ the (1,2) entry is
  (w e^{−iθ}/Π)e^{N(2g−l)} = W·e^{−2iθ}e^{N(2g−l)}/(1 − e^{−2iθ}). This uses
  Π = (e^{iθ} − e^{−iθ})/(2iθ′). The others are analogous.

**Lemma P2 (the arc factors are exponentially small; PROVED).** On Σ_b⁺, |e^{−2iθ}e^{N(2g−l)}| ≤ e^{−cN}, with c > 0
uniform on compact pieces of the arc away from ±r*. Near 0 the bound is super-exponential.

*Proof.* For z = x + iy on the arc, Re[−2iθ + N(2g − l)] = N·E(x, y), where E(x, y) := −2πy/|z|² + 2Re g(z) − l.
For x on the band, Re g(x) = l/2, so 2Re g(x+iy) − l = ∫ log(1 + y²/(x−s)²) dμ*_sym(s) = 2πψ(x)y + o(y) as y ↓ 0,
because ∫_ℝ log(1 + y²/u²)du = 2πy and ψ is continuous at x. Also 2πy/|z|² = 2πy/x² + O(y³), and 1/x² is the node
density (q = 1). So E(x, y) = 2πy(ψ(x) − 1/x²) + o(y). Here ψ(x) − 1/x² < 0 strictly on (−r*, r*) ∖ {0} (RH.md
Lemma 2.1), uniformly on compacts away from 0 and ±r*. Hence E ≤ −c·y for 0 < y ≤ δ(K) on each such compact K, and
the arcs are chosen at height ≤ δ(K) there. Near 0, −2πy/|z|² = −2π sin β/|z| on a ray at angle β, which tends to −∞,
while 2Re g − l stays bounded. Near ±r* the arcs enter the Airy discs. ∎

## 4. Lens opening: T → Q

On the band, (T-a) factorizes as

  J_T = [[1, 0], [e^{2Nφ₋}/W, 1]]·[[0, W], [−1/W, 0]]·[[1, 0], [e^{2Nφ₊}/W, 1]],

with φ := l/2 − g, so that φ₊ = −πiΦ = −φ₋ on the band (WLXZ (4.11)). Put Q := T·[[1, 0], [∓e^{2Nφ}/W, 1]] in
Ω_b^±, and Q := T elsewhere. W is analytic in Ω_b^± (its cut is the imaginary axis, which meets the closure of Ω_b^±
only at 0).

**Jumps of Q.**
- (Q-a) Band: [[0, W], [−1/W, 0]].
- (Q-b) Σ_b^±: J_T multiplied by [[1, 0], [e^{2Nφ}/W, 1]]^{±1}. That is lower-triangular with entry e^{2Nφ}/W, times
  the exponentially small upper-triangular factor of Lemma P2.
- (Q-c) Saturated, arcs, vertical segments and |x| > k_N: as for T, with the △ structure.

**Lemma P3 (PROVED).** |e^{2Nφ}| = e^{−N∫log(1+y²/(x−s)²)dμ*} on Ω_b^± (RH.md Lemma 2.3). Hence the lens entries are
O(e^{−cN}) uniformly on Σ_b^± away from ±r* and 0. Near 0 they are not small, because the arcs pass through 0; that
is handled by the local problem of §7. ∎

## 5. Normalization: Q → V

The saturated-part jumps (T-b) and the jumps beyond k_N (T-c) carry oscillating diagonal factors e^{∓2iθ}. These are
removed with the D-functions of RH.md §6.2, built from t(z) = N/z:
- D̃(z) := √(2π)t^{t−½}e^{−t}/Γ(t), analytic on ℂ ∖ (−∞, 0], with D̃ = 1 + O(z/N) uniformly on compacts;
- D := D̃/(1 − e^{∓2iθ}) on ℂ±;
- mirrored D̂ and Ê, built from −z, for Re z < 0;
- E(z) := (z² − r*²)^{1/4}(r*² − z²)^{−1/2}.

Put V := (const)^{σ₃}·Q·(D E)^{σ₃} on the right half-plane and V := (const)^{σ₃}·Q·(D̂ Ê)^{σ₃} on the left. The
constants are the ∞-limits; DE → (2πN)^{−1/2}·(unimodular constant) at ∞ (RH.md §6.2, checked).

**Lemma P4 (PROVED by construction; checked numerically).**
- D₊E₊ = D₋E₋e^{2iθ} on x > k_N (and the mirrored identity on x < −k_N), so V has no jump on |x| > k_N.
- On the saturated part, (DE)^{−σ₃}J_Q(DE)^{σ₃} = [[1, 0], [(D̃²/w̃)e^{2Nφ̃}, 1]], the WLXZ (5.4) form, with
  w̃ := w·(analytic factor from E) and φ̃ = φ ∓ iθ/N.
- Checks: the jump identity to 1e−26 (RH.md §6.2), and the smallness of the raw saturated entry uniformly up to k_N
  (RH.md Lemma 4.4).

**Jumps of V outside the discs U(±r*, δ) and U(0, δ).**
- (V-a) Band: [[0, w₀], [−1/w₀, 0]], with w₀ := W/(E²·D̃²), analytic and nonvanishing on the band away from 0 and
  ±r*. Near 0, w₀ = |x|^{2α}h(x) with h analytic and nonzero, using α = (r−2)/2 and D̃ = 1 + O(z/N).
- (V-b) Every other jump is I + O(e^{−cN}): Lemmas P2, P3, RH.md Lemma 2.3 (φ̃ part) and Lemma 4.4.

## 6. Global parametrix

𝒩(z) := F_∞^{σ₃}·N₀(z)·F(z)^{−σ₃} (written 𝒩 to avoid a clash with the degree N), where:
- N₀ = [[(a + a⁻¹)/2, (a − a⁻¹)/(2i)], [−(a − a⁻¹)/(2i), (a + a⁻¹)/2]] with a(z) = ((z − r*)/(z + r*))^{1/4};
- F is the Szegő function of w₀ on [−r*, r*]: F₊F₋ = w₀ on (−r*, r*), F analytic and nonvanishing off
  [−r*, r*], F → F_∞ at ∞, given by the standard integral F(z) = exp(√(z²−r*²)/(2π)∫_{−r*}^{r*}
  log w₀(x)/(√(r*²−x²)(z − x)) dx).

Then 𝒩₊ = 𝒩₋[[0, w₀], [−1/w₀, 0]] on the band. 𝒩 has |z ∓ r*|^{−1/4} singularities at ±r*, and near 0 it behaves like
|z|^{±α} through F (KV §4, "the parametrix for the outside region", which includes |x|^{2α}).

## 7. Local parametrices

- **At ±r*:** Airy, in the band–saturated form of WLXZ §6.1, with conformal map f̃ = (−(3/2)Nφ̃)^{2/3}. This is
  valid by the square-root vanishing of RH.md Lemma 4.1. Matching: P_{±r*}𝒩⁻¹ = I + O(1/N) on ∂U(±r*, δ).
- **At 0:** KV §5. The local jumps in U(0, δ) are:
  - (i) the band jump [[0, |x|^{2α}h], [−(|x|^{2α}h)⁻¹, 0]], which is KV (5.2) after the analytic h is absorbed into
    F (as KV absorb e^{−nV});
  - (ii) four lens arcs carrying [[1, 0], [e^{2Nφ}/w₀, 1]], which is KV (5.1);
  - (iii) on the same arcs, the extra R-step factors of Lemma P2, which near 0 are I + O(e^{−cN/|z|});
  - (iv) the D̃-correction D̃ = 1 + O(z/N).

  KV's P solves (i)–(ii) exactly, with P𝒩⁻¹ = I + O(1/N) on ∂U(0, δ). The true jumps differ from KV's by
  I + O(|z|/N) inside the disc, from (iii) and (iv). As in WLXZ Remark 6.1, a single-layer small-norm argument in
  L²(Σ ∩ U(0, δ)) absorbs this into a factor I + O(1/N). The hypotheses ψ(0) > 0 (RH.md Lemma 4.2) and the conformal
  map f(z) = ±iφ(z) − iφ₊(0), with f′(0) = πψ(0), are verified.
- **At the top:** no parametrix (RH.md Lemma 4.4, and Lemma P4 for |x| > k_N).

## 8. Small norm and extraction

Let P be the parametrix: 𝒩 outside the discs, and the local P's inside. Put S := V·P⁻¹.
- The jumps of S are I + O(1/N) on the disc boundaries, I + O(e^{−cN}) elsewhere, and I + O(1/N) inside U(0, δ)
  after the §7 single-layer step.
- They are uniform in L² ∩ L^∞ of the jump contour, which is bounded except for |x| > k_N, where there is no jump.
- By the standard small-norm theorem (as in KV §6 and WLXZ §6.3), S = I + O(1/N) uniformly.

**Extraction.** In Ω_∞, U = e^{Nlσ₃/2}·(const)^{−σ₃}·S·𝒩·(DE)^{−σ₃}·e^{N(g − l/2)σ₃}. As z → ∞:
- g = log z + O(z⁻²);
- (DE)^{−σ₃} → constant diagonal;
- S = I + S₁/z + …, with S₁ = O(1/N);
- 𝒩 = F_∞^{σ₃}(I + 𝒩₁/z + …)F_∞^{−σ₃}, with (𝒩₁)₁₂(𝒩₁)₂₁ = (r*/2)², the standard value for [−r*, r*].

Constant diagonal conjugations leave the product (U₁)₁₂(U₁)₂₁ unchanged, so

  N²γ_N² = (U₁)₁₂(U₁)₂₁ = (r*/2)²(1 + O(1/N)).

Here U₁ = N·N^{Nσ₃}Y₁N^{−Nσ₃} and (Y₁)₁₂(Y₁)₂₁ = h_N/h_{N−1} = γ_N². Hence γ_N = (r*/2)N^{−1}(1 + O(1/N)) for both
parities. With r* = π (p = 2) this is γ_N² = (π²/4)N^{−2} = c(2)(N/2)^{−2}. RH.md Lemma 5.1 then gives Theorem RH. ∎

## 9. p = 1

- t(z) = N/z² and θ = πN/z², which is even, as in WLXZ.
- The decay pattern is that of RH.md Lemma 1.1(d): opposite factors in the left and right quarter-planes, exactly as
  WLXZ (3.12).
- r* = 2 and α = r − 3/2.
- §§2–8 go through with WLXZ's region assignments. The only change from WLXZ is the weight: pure power k^{−r} instead
  of Tricomi–Carlitz. It enters only through w and hence through F, D and E. **Theorem RH (p = 1)** follows the same
  way.

## 10. What this document relies on (dependency list)

- **Proved here or in RH.md:**
  - P1 (no poles), P2 and P3 (exponential smallness), P4 (D/E identities);
  - RH.md Lemmas 2.1–2.3, 4.1, 4.2, 4.4 (the last numerical), 5.1;
  - the global parametrix (standard).
- **Cited constructions** (read):
  - the Airy band–saturated parametrix (WLXZ §6.1);
  - the Bessel origin parametrix and the outside parametrix with |x|^{2α} (KV §§4–5);
  - the small-norm theorem and the single-layer argument (KV §6, WLXZ Remark 6.1).
- **Lemma 4.4, now PROVED.** F(x) := 2Re g(x) − l is continuous and > 0 on [r* + δ, ∞) (RH.md Lemma 2.2), and
  F(x) ~ 2 log x as x → ∞. So inf_{x≥r*+δ} F =: c(δ) > 0. On [r* + δ, N + ½]:
  - |θ′| ≤ πN/r*² and 1/|w| ≤ 2N^{r−1}r*^{−r};
  - |D̃| is bounded, since t = N/x ≥ N/(N+½) ≥ 2/3, where D̃ is continuous and nonvanishing;
  - the E factors and conjugation constants are polynomial in N.

  So the saturated jump entries are O(N^K e^{−c(δ)N}) uniformly. RH.md Lemma 4.4's numbers illustrate this.
- **Label:** PROVED-mod-cite (WLXZ §6.1, KV §§4–6), pending Rule R.
