# RH_px: pointwise Law P for σ_{p,s} = Σ k^{−s} δ_{k^{−p}}, p > 1, in the x-variable (Plan 12)

Status: **Rule R: ACCEPT WITH FIXES** (review/REVIEW_RHpx.md). F1–F10 applied; the re-check CONFIRMED subject to R1–R4, which are applied. **Label: PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6 incl. (6.42)–(6.53) and Prop. 6.5; G2 PROOF.md μ*, B*), REVIEWED.** Numerically validated end to end (probe P1).

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

## 3. D-functions, the scalar functions B and F, normalization, global parametrix (Phase 3; Gate 3 GO)

**Notation** (Rule R F8):
- B is the Binet-cut scalar (previously S);
- K(z) := (4c − z)^{−1/2} (previously E);
- 𝒵 is the final small-norm matrix;
- E_N is the Bessel prefactor (§4.1).

**Definitions** (p > 1, on the slit plane ℂ ∖ (−∞, 0]):
- D̃(z) := √(2π)t^{t−½}e^{−t}/Γ(t) = exp(−μ(t)), where μ is Binet's function;
- D(z) := D̃(z)/(1 − e^{∓2iθ(z)}) in ℂ± (the WLXZ (4.16) pattern).

**Lemma 3.1.**
- (i) D̃ is analytic and nonvanishing on the slit plane (Lemma 1.1). D is analytic in ℂ± and nonvanishing.
- (ii) On (4c, ∞) off nodes, D₊/D₋ = −e^{2iθ}.
- (iii) On (−∞, 0), D₋ = conj(D₊), so D₊/D₋ = e^{iℓ̂(x)} with ℓ̂ := 2arg D₊ real and continuous.
  - ℓ̂(x) = O(|x|^{1/p}/N) as x → 0⁻ (Binet);
  - ℓ̂(−∞) = π/p − π.
- (iv) |D(z)| ~ |t|^{−1/2}/√(2π) as z → ∞.

*Proof.*
- (ii) Use (1 − e^{2iθ})/(1 − e^{−2iθ}) = −e^{2iθ}.
- (iii) Reflection symmetry. The limit at −∞ comes from D₊ ~ −it₊^{−1/2}/√(2π) as t → 0.
- (iv) 1/Γ(t) ~ t and 1 − e^{∓2πit} ~ ±2πit. ∎

Checks: `checks/check_px_phase3a.out` (p ∈ {1.5, 2, 3}, N ∈ {20, 80}).

**The Binet cut is absorbed exactly.**

  B(z) := exp( −(1/2πi)∫_{−∞}^0 iℓ̂(y)[1/(y − z) − 1/(y − 1)]dy ).

**Lemma 3.2.**
- (i) B is analytic and nonvanishing off (−∞, 0], with B₊/B₋ = D₋/D₊ on (−∞, 0). So DB has no jump on (−∞, 0).
- (ii) **Hölder at 0** (F4(b)). ℓ̂ ∈ C^{0,ν}, with ν := min(1/p, ½) on [−1, 0] and ℓ̂(0) = 0. Hence log B is Hölder-ν on
  a closed neighbourhood of 0, from each side of the cut, and B is continuous and nonzero at 0 (Lemma 3.4).
- (iii) B ~ C z^{½−1/(2p)} at ∞.
- (iv) B/B(1) = 1 + O(1/N) on compacts.
- (v) On (−δ, 0), D̃B jumps by (1 − e^{−2iθ₊})/(1 − e^{2iθ₋}) = 1 + O(exp(−2πN sin(π/p)|x|^{−1/p})).

The proofs are as before; (ii) uses Lemma 3.4.

**Normalization.** Put

- F := D·B·K in Ω_∞;
- F̃ := D̃·B·K in the band lens Ω_{b,±} **and in the saturated regions Ω^△_±** (F2).

**Lemma 3.3.**
- (i) F has no jump on (−∞, 0).
- (ii) F₊/F₋ = e^{2iθ} on (4c, ∞) off nodes. **This is used only on (N^p + δ′, ∞)**, where Ω_∞ meets the real axis
  (F2). On (4c, N^p) the diagonal factors e^{∓2iθ} are removed by WLXZ's V^△ (below).
- (iii) F → F_∞ ≠ 0 at ∞, with exponents D ~ z^{1/(2p)}, B ~ z^{½−1/(2p)}, K ~ z^{−½}.
  - D alone has monodromy e^{iπ/p}, which K cannot cancel unless 1/p ∈ ℤ. B carries the complement.

Checks: `checks/check_px_phase3b.out`.

**Transformations** (F2; WLXZ (4.1), (4.12)–(4.13), (5.1) with γ ↦ θ′):
- T := e^{−Nlσ₃/2}R e^{−N(g−l/2)σ₃}.
- Q := T × (WLXZ's lens factors V_± in the band lens; V^△_± = diag(e^{±iθ}/(2iθ′), 2iθ′e^{∓iθ}) in Ω^△_±; I in Ω_∞).
  This is WLXZ (4.12), with their signs.
- V := C_∞·Q·{F^{σ₃} in Ω_∞; F̃^{σ₃} in Ω_{b,±} ∪ Ω^△_±}, with C_∞ the constant diagonal fixed by Lemma 3.5.

**Facts about the jumps.**
- In Ω^△, Π^{−σ₃}V^△₊ = (1 − e^{−2iθ})^{−σ₃} = (D/D̃)^{σ₃}. So relative to U the effective factor is DBK. That is why
  the probe could use F in Ω_∞ unchanged.
- On (4c, N^p) the real-axis jump of V is lower-triangular:

    [[1, 0], [D̃²B²K²e^{2Nφ̃}/W, 1]] = [[1, 0], [e^{2Nφ̃}/w₀, 1]],  K² = 1/(4c − x),  W = 2iθ′w,

  as in WLXZ (5.4) on (2, k_n) and (6.4). Conjugation by V^△ divides by (2iθ′)²; Rule R re-check R1 corrected the
  power of θ′. Here Re φ̃ < 0 (Lemma 2.1(iii)).
- On (N^p + δ′, ∞) there is no jump (Lemma 3.3(ii) together with T's diag(e^{−2iθ}, e^{2iθ})).

**Lemma 3.4 (Hölder endpoint bound; self-contained, replacing a Muskhelishvili citation, F4(b)).** Let q be Hölder-ν
on [0, η] (some η > 0) with q(0) = 0, and smooth on [η/2, 4c]. Put

  Q(z) := (√(z(z − 4c))/2π)∫_0^{4c} q(x) dx/(√(x(4c − x))(z − x)).

Then Q is bounded in U(0, η/2) ∖ [0, 4c], with bounded boundary values. The same holds for the half-line Cauchy
integral defining log B, with q = ℓ̂ on (−∞, 0].

*Proof.*
- Put x₀ := Re z (projected to [0, 4c]) and write q(x) = (q(x) − q(x₀)) + q(x₀).
- The q(x₀) part is explicit: (1/π)∫_0^{4c}dx/(√(x(4c − x))(z − x)) = 1/√(z(z − 4c)). So it contributes q(x₀)/2, which
  is bounded.
- For the difference part, |z − x| ≥ |x − x₀| and |q(x) − q(x₀)| ≤ C|x − x₀|^ν. So it is at most

    C|z|^{1/2}∫_0^{η}|x − x₀|^{ν−1}x^{−1/2}dx + C|z|^{1/2}(far part)
    ≤ C|z|^{1/2}(x₀^{ν−1/2} + 1) ≤ C|z|^{ν} + C.

  Here x₀ ≍ |z| when z is near the band. When x₀ ≪ |z| (z away from the band), use the two-sided bound
  |z − x| ≥ c(|z| + |x − Re z|), for x ≥ 0 and arg z bounded away from 0. Then |q(x)| ≤ Cx^ν gives
  C|z|^{1/2}∫_0^η x^{ν−1/2}(|z| + x)^{−1}dx ≤ C|z|^ν.
- The half-line case is identical with the kernel 1/(y − z) − 1/(y − 1) and no square-root factor. ∎

*Consequence.*
- **log h_N is Hölder-ν on [0, η]** (re-check R3). log h_N = const − 2log D̃ − 2log B.
  - On (0, η], |(log D̃)′(x)| = |μ′(t)||t′(x)| ≤ C t^{−2}·N x^{−1/p−1}/p = O(x^{1/p−1}/N).
  - Likewise |(log B)′(x)| ≤ C∫_{−∞}^0 |ℓ̂(y)|/|y − x|²dy ≤ C x^{1/p−1}, using |ℓ̂(y)| ≤ C|y|^{1/p} near 0 and bounded
    far away.
  - Integrating gives Hölder-1/p, and the cap ν = min(1/p, ½) costs nothing.
- So log h_N = log h_N(0) + q with q Hölder-ν. So the Szegő function D_w of w₀ = C_N x^{α_x}(4c − x)h_N satisfies
  D_w(z)/((−z)^{α_x/2}(4c − z)^{1/2}h_N(z)^{1/2}) bounded above and below near 0. The constant part of log h_N gives an
  exact constant, and Q is bounded.
- This is exactly what KMVV's removability argument for E_N uses (§4.1).

**Lemma 3.5 (normalization at ∞, F3).** μ* has unbounded support, so g − log z ≍ z^{−1/p} and T = I + O(N|z|^{−1/p}),
not I + O(1/z). Put κ(z) := F(z)^{−1}e^{N(g(z) − log z)}. Then:
- on (N^p + δ′, ∞): g₊ − g₋ = 2πiμ*((x, ∞)) = 2iθ/N, so e^{N(g − log z)} jumps by e^{2iθ}, as does F (Lemma 3.3(ii));
- on (−∞, 0): g and log z both jump by 2πi, and F is jump-free.

So κ is analytic and bounded in |z| > N^p + δ′. Hence it is analytic at ∞: κ = κ_∞(1 + κ₁/z + …).

Since U z^{−Nσ₃} = I + O(1/z) and, for |z| large, V = C_∞e^{−Nlσ₃/2}(Uz^{−Nσ₃})e^{Nlσ₃/2}κ^{−σ₃}·const, the choice
C_∞ := (κ_∞ const)^{σ₃} gives **V = I + O(1/z)**. (Probe P1 confirms the 1/z rate: Fe^{−N(g−log z)} agrees in two
directions to 10^{−9} at |z| = 10⁹.)

**Band weight and global parametrix.**
- In the band lens the jump is [[0, w₀], [−1/w₀, 0]], with

    w₀(x) = W(x)(4c − x)/(D̃(x)²B(x)²) = C_N x^{α_x}(4c − x)h_N(x).

  Here h_N is Hölder at 0, analytic on (0, 4c + ε), and h_N/h_N(1) = 1 + O(1/N).
- Global parametrix: N := D_{w,∞}^{σ₃}N₀D_w^{−σ₃}, with N₀ built from a(z) = ((z − 4c)/z)^{1/4}.
  - The linear vanishing at 4c is WLXZ's (4 − z²)^{2α−1} at α = 1, cf. (5.9)–(5.11).
  - The band jump is exact. D_{w,∞} ∝ N^{(1+p−s)/2}, so all smallness statements are made in the
    D_{w,∞}-conjugated frame (F3).
- **Probe P1** (end to end, `checks/check_px_e2e.py`; `_p2s3`, `_p15s3`, `_p3s25.out`; from the Rule R review).
  - The true U comes from the discrete OPs: exact atoms k ≤ 4N, plus a Gauss rule built from exact Hurwitz-zeta tail
    moments.
  - Then V := C_∞e^{−Nlσ₃/2}Ue^{Nφσ₃}F^{σ₃} is compared with N at 9 points outside the discs, including the negative
    axis.
  - D_{w,∞}^{−σ₃}(VN^{−1} − I)D_{w,∞}^{σ₃} = C/N, with N·error stable for N = 10, 20, 40.
  - This holds at (p, s) = (2, 3), (1.5, 3) and (3, 2.5), i.e. α_x = 0, ⅓ and −½.
  - It validates l, D, B, K, w₀ and N at once.

**Gate 3: GO.** Outside the discs at 0 and 4c:
- the band jump is exact;
- the band lips are O(e^{−cN}) (Lemma 2.2);
- D/D̃ − 1 = O(e^{−2|Im θ|});
- the Σ^△ lips and (4c, N^p) are O(e^{−cN}) (Lemma 2.1(iii), Lemma 2.2);
- the top end is O(N^{−pN}poly) (§4.3);
- there is no jump on (−∞, 0) or on (N^p + δ′, ∞).

## 4. Local parametrices (Phase 4; Gate 4 GO after F1)

### 4.1 Hard edge x = 0: KMVV's **left-endpoint** construction (6.42)–(6.53) (F1)

**Conformal map.** f(z) := (φ(z) ± iπ)²/4 in ℂ±.

**Lemma 4.1.**
- f is analytic in U(0, δ), with f(0) = 0 and f′(0) < 0 (= −1/π² to 4 digits at p = 2, check [1] of
  `check_px_phase4.out`).
- The band (0, δ) maps to ζ < 0 and (−δ, 0) maps to ζ > 0. The ordering is **reversed**, exactly as at KMVV's
  endpoint −1: "the ordering is reversed … f̃(Σ₁ ∩ Ũδ) is part of the ray γ₃". So our upper lip maps to γ₃ (F10).
- The reversal is absorbed by the σ₃-conjugation (6.51) and the constant matrix of (6.53), **not** by f (F1(d)).
- Since Re φ < 0 on U(0, δ) off the band (Lemma 2.2), the principal root is f^{1/2} = −(φ ± iπ)/2 (F1(b)).

*Proof of analyticity:* as before. φ(0±) = ∓iπ; across the band φ₊ = −φ₋; across (−δ, 0), φ₊ − φ₋ = −2πi. ∎

**W.** W̃(z) := (C_N(−z)^{α_x}(4c − z)h_N(z))^{1/2}, with the **principal** (−z)^{α_x}, cut along [0, ∞) ∩ U (F1(c);
KMVV (6.44)–(6.46)). Then W̃₊W̃₋ = w₀ on the band.

**Parametrix** (the analogue of KMVV (6.47), (6.51)–(6.53), Bessel order α_x > −1):

  P₀ := (−1)^N·Ẽ_N(z)·σ₃Ψ(N²f(z))σ₃·W̃(z)^{−σ₃}·e^{+Nφ(z)σ₃},
  Ẽ_N := N(z)W̃(z)^{σ₃}(1/√2)[[1, i], [i, 1]]f(z)^{σ₃/4}(2πN)^{σ₃/2}.

Ψ is KMVV (6.23)–(6.25) with order α_x. The factor e^{+Nφσ₃}(−1)^{Nσ₃} is the analogue of KMVV's ϕ̃^{−nσ₃}, since
ϕ̃^{−2n} = e^{−4Nf^{1/2}} = e^{2Nφ} matches the lip entry e^{2Nφ}.

**Lemma 4.2.**
- (i) P₀ has the model jumps of V in U(0, δ), up to the (h2) jump of W̃ on (−δ, 0).
  - **Band jump of Ẽ_N, written out** (the analogue of KMVV (6.35)–(6.36)):
    - N₊W̃₊^{σ₃} = N₋W̃₋^{σ₃}[[0, 1], [−1, 0]], since W̃₊W̃₋ = w₀;
    - on the band f < 0 and, for the principal fourth root, f₊^{1/4} = −if₋^{1/4} (the opposite of KMVV's +i at +1);
    - so f₊^{σ₃/4} = diag(−i, i)f₋^{σ₃/4};
    - with M := [[1, i], [i, 1]]/√2, one checks J₀M = [[i, 1], [−1, −i]]/√2 = M·diag(i, −i), where
      J₀ := [[0, 1], [−1, 0]]; so M^{−1}J₀M = diag(i, −i);
    - hence Ẽ_{N,−}^{−1}Ẽ_{N,+} = f₋^{−σ₃/4}·diag(i, −i)·diag(−i, i)·f₋^{σ₃/4} = I.
  - Check [A] of `check_px_bessel.out`: E_−^{−1}E_+ = I to 1e−19 with M₊ = [[1, i], [i, 1]]. It equals −I with
    KMVV (6.31)'s [[1, −i], [−i, 1]], which was the F1(a) error.
- (ii) det P₀ ≡ 1 (as KMVV (6.33)).
- (iii) **Ẽ_N = (analytic in U(0, δ)) + O(e^{−c′N}), bounded with bounded inverse** (F4(a); heading per re-check R2).
  - Ẽ_N has no band jump by (i).
  - On (−δ₀, 0), with δ₀ > δ, it has the super-small jump J_E − I = O(exp(−cN|y|^{−1/p})), inherited from W̃ (Lemma 3.2(v)).
  - Write Ẽ_N = E^a + Φ with Φ := (1/2πi)∫_{−δ₀}^0 Ẽ_{N,−}(y)(J_E(y) − I)dy/(y − z).
    Integrating to −δ₀ keeps Φ's endpoint log singularity at −δ₀, off ∂U(0, δ). The density is
    O(|y|^{−1/2}e^{−cN|y|^{−1/p}}), so Φ is bounded, continuous and O(e^{−c′N}).
  - E^a is analytic in the punctured disc, and O(|z|^{−1/2}) at 0 by Lemma 3.4's consequence: KMVV's (6.37)–(6.38)
    pattern, "all entries of E_n(z) have at most a square-root singularity … Since we already know that E_n is
    analytic in a punctured neighborhood …, the isolated singularity … is removable". Hence E^a is analytic.
  - So Ẽ_N = analytic + O(e^{−c′N}), and det Ẽ_N = 1.
- (iv) P₀N^{−1} = I + O(1/N) on ∂U(0, δ) (KMVV (6.28) and the (6.53) analogue).
  - **Check [B]** of `check_px_bessel.out` (p = 2, s = 3; |z| = 0.4): the max entry of D_∞^{−σ₃}(P₀N^{−1} − I)D_∞^{σ₃}
    is 0.0492 → 0.0250 (arg ±π/2), 0.0655 → 0.0335 (arg ±0.8π) and, **inside the lens** (Hankel sectors (6.24)–(6.25)),
    0.0290 → 0.0142 (arg ±0.15π), for N = 20 → 40. So it is O(1/N) in all five KMVV sectors.
  - The previous construction gave 10⁵ → 10¹³.

**Lemma 4.3 (hard-edge mismatch).** With H := VP₀^{−1}, on Σ ∩ U(0, δ) and for every K, |J_H − I| ≤ C_K N^{−K}min(1, |z|^K).
- The (h1) entries (diag D/D̃ − I and the upper-right e^{−2Nφ̃} entries on the lips) and the (h2) jump on (−δ, 0) are
  ≤ exp(−cN|z|^{−1/p}). The lips leave 0 near the angles ±π/3 (upper lip ↦ γ₃), where sin(arg z/p) > 0.
- The amplification by P₀ is poly(N, |z|^{−1}) times e^{CN|z|^{1/2}}.
- σ₃-conjugation preserves KMVV's (6.4)–(6.6) bounds entrywise.
- Check [3] of `check_px_phase4.out`: log₁₀(mismatch × amplification) ≤ −84 at α = 3, N = 20, |z| = 0.1, and it
  decreases further.

**No Stirling truncation is needed.** The Binet non-analyticity is cancelled exactly by B (Lemma 3.2). Its residue in
h_N is Hölder and enters only through Lemma 3.4.

### 4.2 Soft edge 4c: Airy parametrix (WLXZ §6.1 in x)

- Near 4c the V-jumps are WLXZ (6.4) with D̃ ↦ F̃ = D̃BK and their w̃ ↦ −2iθ′w (re-check R1):
  - band (4c − ε, 4c) with weight w₀;
  - lower-triangular on (4c, 4c + ε) (the explicit entry of §3);
  - upper-triangular w̃e^{−2Nφ̃}/F̃² on the vertical segments 4c ± i(0, δ), where Re φ̃ > 0 because
    φ̃ ≈ −κ̃(iy)^{3/2}.
- K = (4c − z)^{−1/2} reproduces WLXZ (5.7) at α = 1.
- φ̃ = −κ̃(z − 4c)^{3/2}(1 + O(z − 4c)) (check [2]: −0.1720).
- WLXZ (6.5)–(6.21) need only that w̃ and D̃ are analytic and nonvanishing in U(4c, ε). That holds, since t ≈ N(4c)^{−1/p}.
  B is analytic there. This gives V_r with exact jumps and V_rN^{−1} = I + O(1/N).

### 4.3 Top end (F6)

- WLXZ (3.22) is the junction at 4c (§4.2), not the top. The top closing piece belongs to Σ^△, with J_R = (U^△_±)^{∓1}
  (WLXZ (3.20)–(3.21)).
- After Q and V, the jump on the Σ^△ lips and on the closing segment N^p + δ′ + i(0, ±δ) is

    J_V = I + (F F̃/W)·e^{2Nφ}·e₂₁,  W = 2iθ′w  (the lower-triangular Σ^△ entry of WLXZ (5.4) with our functions;
    θ′ power corrected per re-check R1).

- Bounds on that segment:
  - |D| ≤ CN^p/δ′, since |1 − e^{∓2iθ}| ≍ δ′/(pN^p);
  - |D̃|, |B|, |K| ≤ poly(N);
  - |1/W| = |1/(2θ′w)| ≤ poly(N);
  - |e^{2Nφ}| = |e^{2Nφ̃}||e^{∓2iθ}| ≤ e^{2N Re φ̃}e^{2|Im θ|}, with |Im θ| = O(1) there;
  - Re φ̃(x) = log c + p − U*(x) ≤ −½log x for x ≥ x₀, since U*(x) = log x + o(1).
- Hence |J_V − I| ≤ poly(N)·N^{−pN} on the top pieces, whose length is O(N^p).
- On the Σ^△ lips away from the top, Re φ̃ < 0 (Lemma 2.2), which gives O(e^{−cN}).
- Reliance (c) is closed.

**Gate 4: GO** (after F1, verified by check [B]).

## 5. Identification, small norm, extraction (Phase 5)

**(Y4)_x (F9; one-sided nodes).** For z → 0 with δ₀ ≤ |arg z| ≤ π, Y₁₂, Y₂₂ = O(1 + |z|^{α_x}ℓ(z)).

*Proof.*
- **Away from the band**: Σ_k k^{−s}/max(|z|, k^{−p}) = O(1 + |z|^{(s−1)/p−1}), and (s−1)/p − 1 = α_x.
- **In the lens sectors** 0 < arg z < δ₀ (and the mirror image): R₁₂ = U₁₂ − 𝒦₋(z) with 𝒦_±(s) := U₁₁(wθ′/ sin θ)e^{±iθ}.
  - 𝒦_± has residue μ_kU₁₁(X_k) at each node.
  - 𝒦₋ is O(e^{−cN|s|^{−1/p}}) in the upper right quadrant, since Im θ < 0 there.
  - 𝒦₋ − 𝒦₊ = −2iU₁₁wθ′ = O(|s|^{α_x}).
  - Integrate 𝒦₋/(s − z) over the boundary of G = {|arg s| < φ₀, η_j < |s| < b}, where η_j are midpoints between
    consecutive nodes. On the lower ray switch to 𝒦₊ + (𝒦₋ − 𝒦₊).
  - The η_j-arcs contribute O(η_j^{1+α_x}) → 0, since α_x > −1.
  - The lower-ray integral of −2iU₁₁wθ′/(s − z) is O(1 + |z|^{α_x}ℓ).
  - The remaining nodes in [b, N^p] are finitely many.
  - The left half-plane is node-free.
  - The strip δ₀ ≤ |arg z| < π/3 is covered by both arguments, and they agree up to O(e^{−cN|z|^{−1/p}}). ∎

**Identification** (the RH_p1_general.md §6 route, with KMVV's P̃ behaviour (6.41): "O(1, 1) outside the lens,
O(|z + 1|^{−β}, 1) inside", F10):
- O1: un-lensing for α_x ≥ 0 gives H = O(ℓ²); for α_x ∈ (−1, 0), H = O(|z|^{α_x}).
- X: an inverse-jump local solution X̃. Its δ is arbitrary by Lemma 4.3.
- Removability by circle integrals: ∫_{|z|=r}|HX̃| ≤ C_N r^{min(0,α_x)}ℓ²(r + r^{K+1/2}) → 0, since α_x > −1.
- H₋ ∈ E²_loc, and L² uniqueness.

**Small norm.**
- In the D_{w,∞}-conjugated frame, J_𝒵 − I is:
  - O(1/N) on ∂U(0, δ) and ∂U(4c, ε);
  - O(e^{−cN}) on the lips and saturated pieces;
  - O(N^{−K}) inside U(0, δ);
  - O(N^{−pN}poly) at the top.
- Its L¹ ∩ L² ∩ L^∞ norm is O(1/N); the top pieces of length O(N^p) are absorbed by N^{−pN}.
- So 𝒵 = I + O(1/N), with 𝒵₁, 𝒵₂ = O(1/N) in that frame.

**Extraction (F7).**
- **Convention:** b_N² = h_N/h_{N−1}. a_N is the coefficient in xπ_N = π_{N+1} + a_Nπ_N + b_N²π_{N−1} (toolkit `_fold`).
  Then (U₁)₁₂(U₁)₂₁ = N^{2p}b_N², checked by the reviewer against `_fold`, and a(U) := (U₂)₁₂/(U₁)₁₂ − (U₁)₂₂ = N^p a_N.
- **Invariance lemma.** For constant diagonal C and scalar k(z) = k_∞(1 + k₁/z + …) analytic at ∞, both
  (Y₁)₁₂(Y₁)₂₁ and a(Y) are unchanged under Y ↦ CYk^{σ₃}.
  - *Proof:* the 12-entries of Y₁ and Y₂/Y₁-ratios pick up −k₁ terms, and (Y₁)₂₂ picks up −k₁. These cancel in a(·),
    and the product is conjugation-invariant. ∎
- By Lemma 3.5, U = const·V·(const·κ)^{σ₃}z^{Nσ₃} for |z| large. So the functionals of U equal those of V = 𝒵N, which
  are those of N plus O(1/N).
- For N, (N₁)₁₂(N₁)₂₁ = c² and a(N) = a(N₀) = 2c, since Szegő conjugation is of the invariant form.
- Hence N^p b_N = c(p)(1 + O(1/N)) and N^p a_N = 2c(p)(1 + O(1/N)).
- Probe P1 also gives N^p b_N/c = 0.909, 0.952, 0.976 for N = 10, 20, 40 (p = 2, s = 3). These match
  1 + d₁/N with d₁ = −(s−1)/2 = −1.

## 6. Statement

**Theorem RH_p (PROVED-mod-cite, REVIEWED).** For p > 1 and s > 1, σ_{p,s} = Σ k^{−s}δ_{k^{−p}} satisfies

  n^p b_n = c(p)(1 + O(1/n))  and  a_n/(2b_n) = 1 + O(1/n).

- With RH₁(r) (p = 1, every r > 1), this gives the pointwise Law P with a rate for all pure powers with power weights,
  p ≥ 1, including the Haynes–Zudilin measures and Lommel (p = 2).
- **Open:** 0 < p < 1, where Γ's poles enter the slit plane (Lemma 1.1).
- **Cited:**
  - WLXZ v1 §§3–5 and §6.1 (transformations, V^△, the Airy construction);
  - KMVV §6, including (6.42)–(6.53) (the left-endpoint Bessel parametrix and its removability argument);
  - G2 PROOF.md (μ*, B*).
- **New:**
  - the one-sided x-formulation;
  - B (the exact Binet-cut scalar) and the monodromy count;
  - Lemma 3.4 (Hölder endpoint bound);
  - Lemma 3.5 (normalization with unbounded support);
  - the super-exponential hard-edge mismatch (no truncation);
  - the top-end bound;
  - (Y4)_x.
