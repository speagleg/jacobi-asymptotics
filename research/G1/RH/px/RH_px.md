# RH_px: pointwise Law P for σ_{p,s} = Σ k^{−s} δ_{k^{−p}}, p > 1, in the x-variable (Plan 12)

Status: **DRAFT, pending Rule R** (Phases 0–5 written, Gates 1–4 GO). Not reviewed. No PROVED labels yet. Not reviewed. No PROVED labels.

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

## 3. D-functions, the scalar function F, global parametrix (Phase 3; Gate 3 GO)

**Definitions** (p > 1, on the slit plane ℂ ∖ (−∞, 0]):
- D̃(z) := √(2π)t^{t−½}e^{−t}/Γ(t) = exp(−μ(t)), where μ is Binet's function;
- D(z) := D̃(z)/(1 − e^{∓2iθ(z)}) in ℂ± (the WLXZ (4.16) pattern).

**Lemma 3.1.**
- (i) D̃ is analytic and nonvanishing on the slit plane (Lemma 1.1). D is analytic in ℂ± and nonvanishing.
- (ii) On (4c, ∞) away from nodes, D₊/D₋ = −e^{2iθ}.
- (iii) On (−∞, 0), D₋ = conj(D₊), so D₊/D₋ = e^{iℓ̂(x)} with ℓ̂ := 2arg D₊ real and continuous.
  - ℓ̂(0⁻) = 0. More precisely, ℓ̂ = O(|x|^{1/p}/N) as x → 0⁻ (Binet).
  - ℓ̂(−∞) = π/p − π, from D₊ ~ −i t₊^{−1/2}/√(2π) as t → 0.
- (iv) |D(z)| ~ |t|^{−1/2}/√(2π) as z → ∞, i.e. ∝ |z|^{1/(2p)}.

*Proof.*
- (ii) Use (1 − e^{2iθ})/(1 − e^{−2iθ}) = −e^{2iθ}.
- (iii) Reflection symmetry.
- (iv) 1/Γ(t) ~ t and 1 − e^{∓2πit} ~ ±2πit as t → 0.

Checks (`checks/check_px_phase3a.out`, p ∈ {1.5, 2, 3}, N ∈ {20, 80}): |D₊/D₋| = 1 exactly; arg D₊ runs monotonically
from 0 to π/(2p) − π/2; |D|·|t|^{1/2}√(2π) → 1.

**The Binet cut is absorbed exactly** (this replaces RH₁(r)'s Stirling truncation, which fails for 1/p ∉ ℤ).

  S(z) := exp( −(1/2πi)∫_{−∞}^0 iℓ̂(y)[1/(y − z) − 1/(y − 1)]dy ).

**Lemma 3.2.**
- (i) S is analytic and nonvanishing off (−∞, 0], with S₊/S₋ = D₋/D₊ on (−∞, 0). So DS has **no jump** on (−∞, 0).
- (ii) S is continuous and nonzero up to 0, because ℓ̂ is Hölder with ℓ̂(0⁻) = 0.
- (iii) S ~ C z^{½−1/(2p)} at ∞, because ℓ̂(−∞) = π/p − π.
- (iv) On compacts, S/S(1) = 1 + O(1/N). The contributions are: |y| ≲ N^p, where ℓ̂ = O(|y|^{1/p}/N) and the kernel is
  O(|y|^{−2}); and |y| ≳ N^p, where ℓ̂ = O(1) and the kernel integrates to O(N^{−p}).
- (v) **Near the hard edge**, D̃S has jump (1 − e^{−2iθ₊})/(1 − e^{2iθ₋}) = 1 + O(exp(−2πN sin(π/p)|x|^{−1/p})) on
  (−δ, 0). This is super-exponentially small, although D̃ alone jumps by O(|x|^{1/p}/N).

**Normalization.** Put E(z) := (4c − z)^{−1/2} (principal: cut [4c, ∞), with jump −1 there) and

  F := D·S·E  (in Ω_∞ and the saturated regions),  F̃ := D̃·S·E  (in the band lens).

**Lemma 3.3.**
- (i) F has no jump on (−∞, 0).
- (ii) F₊/F₋ = e^{2iθ} on (4c, ∞) off nodes. So V := Q F^{σ₃} removes T's jump diag(e^{−2iθ}, e^{2iθ}) on the
  saturated region and beyond the top node.
- (iii) F → F_∞ ≠ 0 at ∞. The exponents are D ~ z^{1/(2p)}, S ~ z^{½−1/(2p)} and E ~ z^{−½}.

Checks (`checks/check_px_phase3b.out`, p = 2, N = 20): |(DS)₊/(DS)₋ − 1| ≤ 1e−10 at x = −10⁻³, −1, −10³, −10⁶ (the
residual is the finite offset); S(0) = 0.9958, the same from all directions; F(z) → 0.0079247 in all directions as
|z| → ∞; |F₊/F₋e^{−2iθ} − 1| ≤ 2e−11 on (4c, ∞).

**Why the normalization closes only through S** (a Rule A note). D alone has monodromy e^{iπ/p} at ∞. E's half-integer
power cannot cancel it unless 1/p ∈ ℤ, which is why WLXZ needed no S at p = 1. S carries exactly the complementary
z^{½−1/(2p)}.

**Band weight and global parametrix.** In the band lens, conjugation by F̃^{σ₃} turns the band jump into
[[0, w₀], [−1/w₀, 0]] with

  w₀(x) = W(x)(4c − x)/(D̃(x)²S(x)²) = C_N·x^{α_x}(4c − x)·h_N(x),  h_N = (1 + O(1/N))/(D̃S/(D̃S)(1))².

Here h_N is analytic on a neighbourhood of (0, 4c], positive up to a constant phase, and continuous at 0.
- The **global parametrix** is the standard one for a Jacobi-type weight on [0, 4c]: N = D_{w,∞}^{σ₃}N₀D_w^{−σ₃}, with
  a(z) = ((z − 4c)/z)^{1/4} and Szegő function D_w.
- At 4c the weight vanishes linearly, exactly like WLXZ's (4 − z²)^{2α−1} at α = 1. So the band–saturated Airy
  construction of WLXZ §6.1 applies verbatim in structure.
- **The band jump is exact.** There is no H_n-type mismatch: D̃ enters w₀ exactly, and its N-dependence is carried by
  h_N.
- Leading order: the band [0, 4c] gives b_n → 4c/4 = c in rescaled units, i.e. n^p b_n → c(p), which is Law P.

**Gate 3: GO.** Outside the discs at 0 and 4c (and the top-end segments):
- the band jump is exact;
- the lips are O(e^{−cN}) by Lemma 2.2;
- D/D̃ − 1 = O(e^{−2|Im θ|}) is exponentially small off ℝ;
- the Σ^△ lips are O(e^{−cN}) by Lemma 2.1(iii) and Lemma 2.2;
- there is no jump on (−∞, 0).

## 4. Local parametrices (Phase 4; Gate 4 GO)

### 4.1 Hard edge x = 0: Bessel parametrix (KMVV §6, read; CITATIONS (KMVV))

**Conformal map.** Put f(z) := (φ(z) ± iπ)²/4 in ℂ±.

**Lemma 4.1.** f is analytic in a disc U(0, δ), with f(0) = 0 and f′(0) < 0. f is negative on (0, δ) and positive on
(−δ, 0). So ζ := N²f(z) maps the band to arg ζ = π and the outside segment to ζ > 0, which is KMVV's orientation after
reflection.

*Proof.*
- φ = l/2 − g, with g(0±) = U*(0) ± iπ, so φ(0±) = ∓iπ.
- Across the band, φ₊ = −φ₋ (Lemma 2.1(i)), so (φ₊ + iπ)² = (φ₋ − iπ)².
- Across (−δ, 0), g₊ − g₋ = 2πi (total mass 1), so φ₊ + iπ = φ₋ − iπ.
- Hence f has no jumps, and it is bounded, so 0 is removable. φ ± iπ ~ c√z because ψ ~ Cx^{−1/2} (hard edge). So
  f ~ −κz with κ > 0.
- On the band φ₊ ∈ iℝ, so f < 0. On (−δ, 0), Im φ₊ = −π, so f = (Re φ)²/4 > 0. ∎

Check ([1] of `checks/check_px_phase4.out`, p = 2): |f₊ − f₋| ≤ 2e−26 on both segments, and f(z)/z = −0.10132… at
complex z near 0. The constant is 1/π² to 4 digits.

**W and the model jumps.** In U(0, δ), V's jumps are:
- band [[0, w₀], [−1/w₀, 0]], with w₀ = C_N x^{α_x}(4c − x)h_N (§3);
- lips [[D/D̃, *], [−(DD̃ … )e^{2Nφ}, D̃/D]], the WLXZ (5.4) pattern;
- no jump on (−δ, 0) (Lemma 3.3(i)).

Define

  W(z) := (C_N z^{α_x}(4c − z)h_N(z))^{1/2},  h_N := (const)/(D̃S)²,

with z^{α_x} cut along the band [0, δ). By Lemma 3.2(v), W is analytic across (−δ, 0) up to a factor
1 + O(e^{−2πN sin(π/p)|x|^{−1/p}}).

The **model problem** at 0 is KMVV's RHP for P (their (6.1)–(6.6)):
- off-diagonal band jump with weight W₊W₋ = w₀;
- lower-triangular lip jumps with e^{2Nφ}/W²;
- no jump outside the band.

The true jumps differ from it by:
- (h1) diag(D/D̃) − I and the upper-right e^{−2Nφ̃}-entries on the lips;
- (h2) the super-small jump of W on (−δ, 0).

**Construction** (KMVV (6.27), (6.31), with Ψ from (6.23)–(6.25), Bessel order α_x > −1):

  P₀ := E_N Ψ(N²f(z)) W(z)^{−σ₃} e^{−Nφ(z)σ₃}·(the constant sign conventions of Lemma 4.1).

Here E_N := N(z)W(z)^{σ₃}(1/√2)[[1, −i], [−i, 1]] f(z)^{σ₃/4}(2πN)^{σ₃/2}. Also e^{2Nf^{1/2}} = ±e^{Nφ} (from
f^{1/2} = (φ ± iπ)/2), and e^{Nφ} is single-valued because N ∈ ℤ.

**Lemma 4.2 (Bessel parametrix).**
- (i) P₀ has exactly the model jumps.
- (ii) det P₀ ≡ 1.
- (iii) E_N is analytic in U(0, δ) up to the factor of (h2), and bounded with bounded inverse uniformly in N.
  KMVV's removability needs W/D_w and D_w/W bounded at 0 (their Lemma 6.4 pattern). Here both are x^{α_x/2} times
  bounded continuous factors, because h_N is continuous and nonzero at 0 (Lemma 3.2(ii)).
- (iv) P₀N^{−1} = I + O(1/N) on ∂U(0, δ), by KMVV (6.28)–(6.32).

**Lemma 4.3 (hard-edge mismatch).** With H := VP₀^{−1}, on Σ ∩ U(0, δ) and for every K,

  |J_H − I| ≤ C_K N^{−K}·min(1, |z|^K).

*Proof.*
- The (h1) and (h2) entries carry e^{−2|Im θ|}, e^{−2N Re φ̃} or e^{−2πN sin(π/p)|x|^{−1/p}}. On the lips (leaving 0
  at the angles ±π/3, by Lemma 4.1) and on (−δ, 0), each is ≤ exp(−c N|z|^{−1/p}).
  - Re φ̃ ~ π sin(arg z/p)|z|^{−1/p}, from iθ/N = iπz^{−1/p}.
- The amplification by P₀ is at most poly(N, |z|^{−1}) (KMVV (6.4)–(6.6) for ζ ≤ 1, (6.28) for ζ ≥ 1), together with
  e^{2N|Re φ|} ≤ e^{CN|z|^{1/2}}.
- exp(−cN|z|^{−1/p}) beats both: it is ≤ C_K(N|z|^{−1/p})^{−2K} and dominates e^{CN|z|^{1/2}} for small δ.

Check ([3]): log₁₀ of mismatch × amplification (α = 3) ≤ −84 at |z| = 0.1, N = 20, decreasing with N and as z → 0. ∎

**No Stirling truncation.** Unlike RH₁(r) (Lemma S, Q_m), all mismatches here are super-exponentially small. The
Binet non-analyticity sits in h_N, which is continuous at 0. Its cut is cancelled exactly by S, and the Bessel model
needs h only through W (KMVV).

### 4.2 Soft edge 4c: Airy parametrix (WLXZ §6.1 in x)

- Near 4c, our V-jumps have exactly WLXZ's (6.4) form with (w̃, D̃, φ̃) ↦ ours:
  - band (4c − ε, 4c) with weight w₀/D̃²;
  - lower-triangular on (4c, 4c + ε) with D̃²e^{2Nφ̃}/w̃;
  - upper-triangular on the vertical segments.
- E = (4c − z)^{−1/2} reproduces WLXZ's (z² − 4)^{(1/2−α)σ₃} behaviour at α = 1.
- φ̃ = −κ̃(z − 4c)^{3/2}(1 + O(z − 4c)) with κ̃ > 0. Check ([2]): φ̃/(z − 4c)^{3/2} → −0.1720, and Re φ̃ < 0 to the
  right. This holds because ρ − ψ ~ √(4c − x) on the band side (1 − I_y(1/p + ½, ½) ~ C√(1 − y)).
- The construction (6.5)–(6.21) needs only that w̃ and D̃ are analytic and nonvanishing in U(4c, ε). That holds:
  t ≈ N(4c)^{−1/p} is large there, and D̃ = exp(−μ(t)). It gives V_r with exact jumps and V_rN^{−1} = I + O(1/N).

### 4.3 Top end (x ≈ N^p)

- Beyond the top node, F removes T's jump exactly (Lemma 3.3(ii)).
- On the Σ^△ lips and the closing vertical segment at Re z = N^p + δ′, every non-identity entry is polynomial in N
  times e^{2N Re φ̃} (or e^{−2N Re φ̂}-type).
- Re φ̃(x) = log c + p − U*(x) ≤ −(1/2)log x for x ≥ x₀, since U*(x) = log x + o(1). So the entries are
  ≤ poly(N)·N^{−pN}.
- Unlike RH₁, this is not a reliance on WLXZ: the bound is explicit. (The precise entry list of the segment jumps,
  the WLXZ (3.22) analogue, is in §1.)

**Gate 4: GO.**

## 5. Identification, small norm, extraction (Phase 5)

**(Y4)_x (behaviour at the hard edge).** For z → 0 with δ₀ ≤ |arg z| ≤ π,

  Y₁₂, Y₂₂ = O(1 + |z|^{α_x}ℓ(z)).

*Proof.* Σ_k k^{−s}/max(|z|, k^{−p}) = Σ_{k^{−p}≥|z|} k^{p−s} + |z|^{−1}Σ_{k^{−p}<|z|} k^{−s}, which is
O(1 + |z|^{(s−1)/p−1}), and (s−1)/p − 1 = α_x. In the lens sectors use the K_± representation of RH₁(r) §6(b),
with |wθ′| ≍ |z|^{α_x}. ∎

**Identification.** The argument of RH_p1_general.md §6 transfers:
- Lemma O1 (un-lensing for α_x ≥ 0; O(|z|^{α_x}) for α_x ∈ (−1, 0)), using KMVV (6.4)–(6.6) for P₀;
- Lemma X, solving the inverse jump X̃₊ = J_H^{−1}X̃₋. Its δ is now arbitrary, by Lemma 4.3;
- circle-integral removability: ∫_{|z|=r}|HX̃| ≤ C r^{min(0,α_x)}(r + r^{K+1/2}) → 0, because α_x > −1. Note that
  α_x ∈ (−1, −½] needs Lemma X, since H is then not L²;
- L² uniqueness.

**Small norm.**
- J_S − I = O(1/N) on ∂U(0, δ) and ∂U(4c, ε) (Lemma 4.2(iv) and §4.2);
- J_S − I = O(e^{−cN}) on the lips and the saturated pieces outside the discs (Lemma 2.2 and Lemma 2.1(iii));
- J_S − I = O(N^{−K}) inside U(0, δ) (Lemma 4.3);
- J_S − I = O(N^{−pN}poly) at the top (§4.3).

The contour pieces near the top have length ≍ N^p, which is absorbed by the N^{−pN} factor. So S = I + O(1/N).

**Extraction** (directly in x, no fold). With U = N^{pNσ₃}Y(·/N^p):
- (U₁)₁₂(U₁)₂₁ = N^{2p}b_N²;
- a_N is obtained from Y₁ and Y₂ by the standard formula a_N = (Y₂)₁₂/(Y₁)₁₂ − (Y₁)₂₂, rescaled by N^p.

For the global parametrix of a Jacobi-type weight on [0, 4c]:
- (N₁)₁₂(N₁)₂₁ = (4c/4)² = c²; the Szegő conjugation does not change it (as in RH₁(r) §3);
- the a-functional of N equals the band centre 2c.

Hence N^p b_N = c(p)(1 + O(1/N)) and N^p a_N = 2c(p)(1 + O(1/N)), so a_N/(2b_N) = 1 + O(1/N).

## 6. Statement

**Theorem RH_p (claimed, pending Rule R).** For p > 1 and s > 1, σ_{p,s} = Σ k^{−s}δ_{k^{−p}} satisfies

  n^p b_n = c(p)(1 + O(1/n))  and  a_n/(2b_n) = 1 + O(1/n).

Together with RH₁(r) (p = 1, every r > 1), this gives the pointwise Law P with a rate for all pure powers with power
weights, p ≥ 1. That includes the Haynes–Zudilin measures and Lommel (p = 2).

**Open:** 0 < p < 1, where Γ's poles enter the slit plane on arg z = ±pπ (Lemma 1.1).

**Reliance and gaps to be checked by Rule R:**
- (a) KMVV §6 used with an h that is analytic only up to a super-small jump and continuous at 0. KMVV assume h
  analytic in a disc.
- (b) WLXZ §6.1 reused at 4c.
- (c) The top-end segment jumps, written out only by analogy with WLXZ (3.22).
- (d) The a_N extraction formula and its global value 2c.
