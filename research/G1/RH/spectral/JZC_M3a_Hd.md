# JZC M3a, lemma H-d: the Hurwitz index transfer is a Szegő shift β′ = α + 2δ at fixed Bessel order α; relation to Σ

Status (2026-10-21): NOT REVIEWED (Rule R pending). Labels per VERIFICATION_POLICY.md. Scope: JZC_M3_scope §3.1, lemma H-d, for
Hurwitz lattices λ_k = (k + δ)^p, k ≥ 1, −1 < δ ≤ 0 (a := 1 + δ), p > 1 for the outer scalar (§2; p < 1: §7 gap G3), s > 1,
α := (s−1−p)/p. Checks: `checks/m3a_hd_outer.py/.out` (34 assertions), `checks/m3a_hd_model.py/.out` (42 assertions).
External results not read under Rule C are marked NOT QUOTED. Everything quoted from Paper 2 is from papers/paper2/*.tex.

| # | Statement | Label |
|---|---|---|
| Prop 2.1 | outer scalar at ∞: F_δ = D_δB_δK ~ C_δ(−z)^δ, C_δ ≠ 0; at 0 unchanged (j_δ = O(1/t)) | PROOF SKETCH (§2) + NUMERICAL (m3a_hd_outer) |
| Lemma H-d | with F♮ := F_δ(−z)^{−δ}, Paper 2's frame (degree n, lattice g, n^p scaling) turns the Hurwitz problem into the decoupled model M(β′, ν) of JZC_M4 §7 with β′ = α + 2δ, ν = α, band factor H_n^δ | PROVED for the jump algebra (§3, NOT REVIEWED); the analytic inputs are §7 gaps G1–G4 |
| Test | M(α+2δ, α) with Hurwitz μ reproduces all 36 Hurwitz fit data; the three alternatives are excluded | NUMERICAL (§4) |
| Relation to Σ | H-d is the exact gauge Y ↦ Y(−z)^{γσ₃} with γ = −δ (p-free); rule H's form (n/(n+δ))^pΦ(n+δ) is Σ at γ = δ, not part of H-d | PROVED (algebra) / reduction (§5) |

## 0. Answer

(i), and only (i), in the frame where Paper 2's normalisation stays U z^{−nσ₃}: the Hurwitz problem at degree n is the lattice-type
problem with **Szegő exponent β′ = α + 2δ** (= α − 2Z(0) − 1, Z(0) = ζ(0, a) = −½ − δ), **Bessel order unchanged (ν = α)**, the same
g-function, the same n^p scaling, and band factor H_n^δ (Lemma H moments ζ(−kp, a)). By the exact gauge (−z)^{δσ₃} this is the same
problem as (ii) "Szegő α, normalisation z^{(n+δ)σ₃}" in the n^p frame (no rescaling). Not (iii). Natural index
N = n + (β′+1)/2 = n + α/2 + ½ + δ, as rule H requires. Identifying the result with "the lattice at degree n + δ" (the form
(n/(n+δ))^pΦ(n+δ) of rule H) is Conjecture Σ, which H-d does not need and does not prove.

## 1. Inputs quoted from Paper 2

- Lemma interp, (eq:U): U(z) := n^{pnσ₃}Y(zn^{−p}); "U(z)z^{−nσ₃} = I + U₁/z + U₂/z² + … for |z| > n^p", (eq:extractU):
  𝖻(Uz^{−nσ₃}) = n^{2p}b_n², 𝖺(Uz^{−nσ₃}) = n^pa_n. Lemma invariance: k_∞^{−σ₃}Xk^{σ₃} has the same 𝖺, 𝖻.
- (eq:t)/(eq:theta): t = nz^{−1/p}, θ = πt; (eq:W), (eq:Wformula): W = 2iθ′w = 𝗐_n z^α r_n; (eq:kappa): κ_± = 1/(1 − e^{∓2iθ}).
- Step 2: T := e^{−nγ_pσ₃}Re^{nφσ₃}; φ̃ := φ ± iθ/n; Lemma gfunction (i): g₊ − g₋ = 2iθ/n on (4c, ∞), φ₊ + φ₋ = 0 on (0, 4c).
- (O1): "F is analytic and zero-free in ℂ∖[0,∞) (in particular, it has no jump on (−∞,0)), … and F₊ = F₋e^{2iθ} on (4c,∞)∖{X_k}."
  (O2): F̃ := (1 − e^{∓2iθ})F = F/κ_±, "F̃₊ = −F̃₋ on (4c, e^{pc₀}n^p)"; (eq:Hn) H_n := 1/((4c − z)F̃²); (eq:W0) W₀ := W/F̃².
  (O5) "(For each fixed n.) |F|^{±1} is bounded on U(0,δ)∖(Ω̄_b ∪ [0,∞)) … |F(z)|^{±1} ≤ C_n|z|^{N_n} for |z| ≥ n^p+δ′, and F(iy) is
  bounded and bounded away from 0 as y → ±∞."
- Lemma jumpsV (a) band [[0, W₀], [−1/W₀, 0]]; (b) lips [[1,0],[e^{2nφ}/W₀,1]] + super-small entries ∝ W₀e^{−2nφ̃}, κ_± − 1;
  (c) Σ_v: [[1, −W₀e^{−2nφ̃}],[0,1]]; (d) saturated [[1,0],[e^{2nφ̃}/W₀,1]]; (g) "On (−∞,0): … e^{nφ} jumps by e^{−2πin} = 1".
- (eq:D) D := κ_±D̃, D̃ = e^{−j(t)}; (eq:binet-small) j(t) = −½ln t − ½ln(2π) + O(|t|log(2/|t|)); Lemma binetcut (ii) 𝔟(y) → π/p − π,
  (eq:B) B := exp(−(1/2π)∫_{−∞}^0 𝔟(y)[1/(y−z) − 1/(y−1)]dy); proof of (iv): "|B(iy)| ≍ |y|^{½−1/(2p)}, and |F(iy)| ≍ 1".
- Lemma normalisation: ϰ_∞ := F^{−1}e^{n(g − Log z)} "extends to an analytic function on {|z| > n^p+δ′} ∪ {∞} with ϰ_∞(∞) ≠ 0";
  (eq:Q-at-infinity) Q = k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃}. (eq:Q) Q := D_∞^{−σ₃}VD_W^{σ₃}; (eq:Pinf0) P₀^∞; (eq:omega) ω := D_W²/W₀.
- Lemma szego (i): D_{x^α}(z)² = (4cz/Υ(z))^α, Υ = (z^{1/2} + (z−4c)^{1/2})², Υ(0) = −4c. Notation table: c_± = e^{∓iπα}.
- Prop apriori (App C) (i): |Q(z)| ≤ C_{n,η}|z|^{−|α|/2−η}, proved from "|F|^{±1} ≤ C outside the lens … (O5); |D_W(z)|^{±1} ≤ C|z|^{±α/2−η}".
- Lemma lips (c): the lips avoid U(4c, h₀); Remark angles: ε (the Airy radius) is chosen after h₀.

## 2. (a) The outer scalar: what δ changes at ∞ and at 0

Hurwitz nodes sit at t ∈ 1 + δ + ℕ₀; the weight is still w = n^pt^{−s} (masses (k+δ)^{−s} = t^{−s} at the node), so **W, W's power
z^α and the Bessel order are unchanged**; only the phase changes, θ ↦ θ_δ := π(t − δ), κ_δ± := 1/(1 − e^{∓2iθ_δ}). Following SPEC §3.1
(H-b): D̃_δ := e^{−j_δ(t)}, j_δ(t) := LnΓ(t−δ) − (t−δ−½)ln t + t − ½ln 2π, D_δ := κ_δD̃_δ, 𝔟_δ := 2Im(−j_δ(t₊) − Log(1 − e^{−2iθ_δ+})),
B_δ by (eq:B), F_δ := D_δB_δK. As in Lemma binetcut, F_δ is analytic and zero-free in ℂ∖[0,∞), no jump on (−∞, 0), and
F_δ₊ = F_δ₋e^{2iθ_δ} on (4c, ∞) off the nodes: (O1) with θ_δ in place of θ. Note e^{2iθ_δ} = e^{2iθ}e^{−2πiδ}.

**Prop 2.1.** Fix n, p > 1, −1 < δ < 0.
- (2.1) *Hard edge, t → ∞:* j_δ(t) = B₂(−δ)/(2t) + O(t⁻²), B₂(−δ) = δ² + δ + ⅙ (DLMF 5.11.8, NOT QUOTED; checked to 10⁻⁷ at |t| = 10⁸).
  So D̃_δ → 1, κ_δ → 1 off the axis, H_n^δ := (D̃_δB_δ)^{−2} keeps the Hölder bound |z|^{1/p} of (O3): nothing changes at z = 0.
- (2.2) *t → 0:* LnΓ(t − δ) → LnΓ(−δ) (Γ is analytic and positive at −δ ∈ (0, 1); elementary), so j_δ(t) = (δ+½)ln t + LnΓ(−δ) − ½ln 2π
  + O(|t|log(1/|t|)), and κ_δ± → 1/(1 − e^{±2πiδ}) (finite: e^{2πiδ} ≠ 1). Hence |D_δ| = Γ(1+δ)(2π)^{−1/2}|t|^{−δ−½}(1 + o(1)),
  against the lattice |D| = (2π)^{−1/2}|t|^{−1/2}, where κ ~ 1/(±2πit) contributes t^{−1}: the lattice's "pole of Γ at t = 0".
- (2.3) 𝔟_δ(y) → 𝔟_∞(δ) := 2[(δ+½)π/p − π/2 − πδ] = (π/p − π) + 2πδ(1/p − 1) as y → −∞ (arg t₊ = −π/p; arg(1 − e^{2πiδ}) = π/2 + πδ),
  with 𝔟_δ − 𝔟_∞ = O(|t₊|log) integrable against |y|^{−1}dy; so, as in the proof of binetcut (iv), |B_δ(iy)| ≍ |y|^{−𝔟_∞/(2π)}.
- (2.4) Exponents add up: (δ+½)/p + [½ − 1/(2p) + δ − δ/p] − ½ = δ. With the monodromy of F_δ at ∞ (jump e^{2iθ_δ} → e^{−2πiδ} on
  (R, ∞), none on (−∞, 0)) this gives **F_δ(z) = C_δ(−z)^δ(1 + o(1)) as z → ∞, C_δ ≠ 0**; δ = 0 is Paper 2's |F(iy)| ≍ 1.

*Status.* (2.1)–(2.3) are limits of explicit functions; (2.4)'s B_δ step is binetcut (iv)'s argument verbatim with 𝔟_∞(δ): PROOF
SKETCH. NUMERICAL (m3a_hd_outer.out, n = 4, p ∈ {3/2, 3}, δ ∈ {0, −0.3, −0.7}, dps 30): 𝔟_δ(−10⁴⁰) = 𝔟_∞ to 10⁻⁹;
log F_δ − δ log(−z) is the same constant on arg z ∈ {π/4, π/2, 3π/4} at |z| = 10²⁴ to 8·10⁻¹⁶ (p = 3/2), 4·10⁻⁸ (p = 3), drifts
3·10⁻¹⁰ / 7·10⁻⁵ from |z| = 10¹⁶; the fitted exponent of |F_δ(iy)| is δ to 10⁻¹¹ / 3·10⁻⁶ (the p = 3 residue is δ-independent:
it is the lattice's O(|z|^{−1/p}) tail). Exploratory: δ = +½ gives exponent +½ as well.

So the offset's whole effect on the outer scalar is the power (−z)^δ at infinity, independent of p. Paper 2's construction then
fails verbatim in exactly two places: ϰ_∞ = F_δ^{−1}e^{n(g−Log z)} ~ (−z)^{−δ} is not analytic at ∞ (Lemma normalisation), and on
(4c, ∞) the diagonal of jumpsV (d) is e^{n(φ₊−φ₋)}F_δ₊/F_δ₋ = e^{−2iθ}e^{2iθ_δ} = e^{−2πiδ} ≠ 1. Both are the same defect: the
lattice g counts nodes from t = 0, the Hurwitz interpolant from t = δ.

## 3. Lemma H-d (frame 1: degree n, lattice g, Szegő shift)

Put F♮ := F_δ·(−z)^{−δ} (principal power, cut [0, ∞)) and F̃♮ := F♮/κ_δ = D̃_δB_δK(−z)^{−δ}; run Paper 2 §5 Steps 1–4 with
κ_δ, θ_δ in Step 1 (L_±, A^△_±; this is H-a), the **lattice** g, φ, φ̃ in Steps 2–3, and F♮ in Step 4. Call the result V♮.

**Lemma H-d.** (i) F♮ satisfies (O1) with the lattice θ: F♮₊/F♮₋ = e^{2iθ_δ}e^{2πiδ} = e^{2iθ} on (4c, ∞); no jump on (−∞, 0); and
F♮ → C_δ ≠ 0 at ∞ (Prop 2.1), so Lemma normalisation holds verbatim: ϰ_∞ is analytic at ∞, ϰ_∞(∞) ≠ 0, and
Q♮ = k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃} near ∞ with U the **degree-n** Hurwitz matrix; (eq:extractU) gives the Hurwitz b_n, a_n.
(ii) Jumps of V♮ (recomputing jumpsV with θ_δ, θ and F♮; W₀^{(β′)} := 𝗐_n z^{α+2δ}(4c − z)H_n^δ, principal power):
- band (a): W/(F̃♮₊F̃♮₋) = W₀^{(β′)}(x), since ((−z)^{−δ})₊((−z)^{−δ})₋ = x^{−2δ} (F̃♮ jumps on the band; only the product enters);
- saturated (d): diagonal e^{−2iθ}·e^{2iθ} = I; entry e^{2nφ̃}/W₀^{(β′)}(x) (−F̃♮₊F̃♮₋ = (D̃_δB_δ)²x^{−2δ}/(4c − x));
- Σ_v (c), lip super-small entries, Σ^△, top: the entries carry e^{−2nφ}e^{∓2iθ_δ} = e^{−2nφ̃}e^{±2πiδ}, and W/F̃♮² = W₀^{(β′)}e^{∓2πiδ} in
  ℂ_±; the phases cancel: all are the lattice formulas with W₀^{(β′)} (principal);
- lips, main entries (b): e^{2nφ}/(W/F̃♮²) = e^{2nφ}e^{±2πiδ}/W₀^{(β′)} in ℂ_± (no θ here, so the phase stays);
- none on (−∞, 0) (n is an integer; F♮ has no jump there).
(iii) Q-frame. D_W := Szegő function of W₀^{(β′)} = D_W^{(α)}·D_{x^{2δ}}, D_{x^{2δ}}² = (4cz/Υ)^{2δ}. The global parametrix is P₀^∞
(weight-free). In the Airy disc (which the lips avoid) every jump is the β′-lattice one: Szegő data φ^{−2(β′+1)} at 4c. On the lips
near 0, ω♮ = ω^{(β′)}e^{±2πiδ}, whose band limits are e^{∓iπβ′}e^{±2πiδ} = e^{∓iπα} = c_±: the hard-edge model is Paper 2's
order-α Bessel model, glued with the Szegő function of x^{β′}. This is JZC_M4 §7's decoupled problem **M(β′ = α + 2δ, ν = α)**,
with band factor H_n^δ = e^{−P_n^δ}(1 + O(n^{−(K+1)p})), μ_{n,k} = 2ζ(−kp, a)/(kn^{kp}) (Lemma H, CONDITIONAL on Hurwitz's formula).
(iv) A priori bound: F♮D_W = F_δD_W^{(α)}·[(−z)^{−δ}D_{x^{2δ}}] and [·] = (4c/Υ)^δe^{±iπδ} is bounded above and below near 0
(Υ(0) = −4c); the δ-powers cancel in each column of Prop apriori's proof, so (F7) holds with the same exponent |α|/2.

*Proof of (i)–(iii).* Algebra of jumpsV's proof with θ_δ/θ kept apart: (a) uses only L₋^{−1}L₊ = U(W), true for any phase
(−W(e^{−2iθ_δ}κ_δ+ + e^{2iθ_δ}κ_δ−) = W); (c): (A^△₊)^{−1}L₊ conjugated by e^{nφσ₃} times A₊ has (1,1) = κ_δ+, (2,1) = 0 and
(1,2) = −Wκ_δ+e^{−2nφ}e^{−2iθ_δ}; (d): κ_δ+^{−1} + κ_δ−^{−1} = κ_δ+^{−1}κ_δ−^{−1} for any real phase. The rest is the bookkeeping above. ∎
(PROVED, NOT REVIEWED; Rule A in §6.)

*Frame 2.* V₂ := V♮(−z)^{δσ₃} uses F_δ itself: Szegő α, the lip phases gone, but a constant diagonal jump e^{−2πiδσ₃} on (4c, ∞),
extra phases e^{±2πiδ} on Σ_v, and normalisation Q₂ ~ (−z)^{δσ₃}, i.e. U at "degree n + δ". This is (ii); it is equivalent to frame 1
and less convenient (the soft edge is twisted).

*The crossover δ → 0⁻.* Prop 2.1's limit at ∞ is non-uniform in δ (it needs |t| ≪ |δ|, i.e. |z| ≫ (n/|δ|)^p), but Lemma normalisation
and (O5) are fixed-n statements, and the extraction does not see ϰ_∞(∞) (Lemma invariance). Every n-uniform input (H_n^δ, the discs,
the lips) lives at |z| ≤ n^p·const, where δ enters only through κ_δ and H_n^δ. So the crossover feared in JZC_M3_scope §3.1, risk 1,
does not reach the asymptotics. At δ = 0, F♮ = F and frame 1 is Paper 2.

## 4. (b) Test: which M(β, ν) reproduces the Hurwitz data (m3a_hd_model.out; NUMERICAL)

Model: m4_rh4.run(p, β, nu=ν, c=c(p), mu=…), KORD = 4, dps 40; μ-responses by central differences; the coefficient of n^{−k−jp} is
(2ζ(−jp, a)/j)·∂d_k/∂μ_j (the n^p frame of Lemma H-d, no (n+δ)^p). Data: the fits in spec_hur.out, spec_hur_d2.out,
spec_shift_hi.out, spec_hur_small.out (36 numbers; Rule X: Jacobi coefficients of the actual Hurwitz measures, fitted by earlier
scripts; nothing is fitted here). Tolerance max(3 × fit half-range, floor) as in those scripts.

| Candidate | (β, ν) | worst deviation | decided by |
|---|---|---|---|
| H1 = H-d | (α + 2δ, α) | **0.07 tol** (all 36 pass) | — |
| H2 (lattice with s′ = s + 2pδ) | (α + 2δ, α + 2δ) | 11 667 tol | n^{−2} (58–11 667 tol), d₃ (129–1 512 tol) |
| H3 (Bessel order shift) | (α, α + 2δ) | 150 000 tol | d₁ |
| H4 (half shift) | (α + δ, α) | 75 000 tol | d₁ |

Highlights for H1: d₁ = −(s−1)/2 − pδ (6 data); n^{−2} at p ∈ {0.6, 0.75, 1.5}, δ ∈ {−½, ½, 1}: e.g. +1.461806 vs fit +1.461804 (tol 10⁻⁴);
d₃ at p = 1.5 now **predicted outright** (the earlier probe used a fitted d₃⁰): −0.267361, +0.103299, −1.731771, −5.930556 vs fits
−0.26736, +0.10330, −1.73179, −5.93062 for δ = 0, −½, ½, 1 (half-ranges ~10⁻³); ε₁, ε₂, ε₃ (β-free at this order, so not
discriminating) and the merged n^{−2} at p = ⅓, ¼ (d₂ + pζ(−1, a)); the n^{−2−p} coefficient 2ζ(−p,a)∂d₂/∂μ₁ = −pc(2p+1)(β′+1)ζ(−p,a)
(c = c(p); weak, half-ranges 0.13–0.15). Exact (sympy): d₁, d₂ of M(α+2δ, α) equal rule H's d₁⁰ − pδ and d₂⁰ + p(p+1)δ²/2 − (p+1)δd₁⁰.
Caveat: spec_shift_hi's d₃ fit subtracted rule H's d₂, which equals H1's (exact) and is itself confirmed by spec_hur_d2.
The δ = ½, 1 data lie outside −1 < δ ≤ 0; they fit the same β′ = α + 2δ (consistent with S2: each deleted top node shifts β′ by 2).

## 5. (c) Relation to Σ

- **H-d is exactly the transformation of JZC_M4 §8 with γ = −δ, independent of p.** Frame 2 → frame 1 is Y ↦ Y(−z)^{γσ₃}: degree
  n + δ → n, weight × z^{−2γ} (β: α → α + 2δ), R unchanged, Bessel order unchanged. The "diagonal jump e^{2πiγσ₃} along the cut" is
  placed on (0, ∞), where it is not an artefact: it is precisely the phase mismatch e^{2πiδ} between the Hurwitz interpolant (zeros
  at t ∈ δ + ℤ) and the lattice g (which counts from t = 0). It is absorbed: on the band into the geometric mean x^{2δ}, on Σ_v and
  the saturated region by θ_δ − θ, and it survives only as the lip phases e^{±2πiδ}, which set the Bessel order back to α.
- **What H-d gives without Σ.** Hurwitz b_n(n; α, δ) = b(n; α + 2δ, α; μ^δ) in the n^p frame: no change of scaling frame is needed,
  because the lattice g at degree n is used unchanged (G1 of the scope: σ_n = σ). With Theorem N.6 extended to M(β, ν) (gap G5)
  this proves the Hurwitz expansion to N.6's orders in the form b(n; α+2δ, α).
- **What needs Σ.** Rule H's form (n/(n+δ))^pΦ(n+δ) is b(n; β′, α) = (n/(n+δ))^p b(n+δ; α, α) — Σ at γ = δ. At finite order this
  is Prop S (JZC_M4 §7: identically in (p, ν, β) for k ≤ 4 by exact algebra, NUMERICAL to k = 8; the run m4_shift_exact.out in the
  tree currently reports orders ≤ 3 only) plus the μ-layers (m4_shift_zeta.out, NUMERICAL). So rule H to the orders of N.6(iii)
  = H-d + N.6 for M(β, ν) + Prop S at those orders (exact for the integer layer to order 4).
- **What remains for Σ itself** (all orders). The gauge relates the degree-n problem to the "(n+γ)-normalised" one **in the n^p frame
  with phase e^{2nφ}**; Σ asserts equality with the problem at degree n + γ **in the (n+γ)^p frame with phase e^{2(n+γ)φ}**. Their
  phases differ by (n+γ)Φ(((n+γ)/n)^pz) − nΦ(z) = −2∫_n^{n+γ}log φ(z(m/n)^p)dm (Lemma BR integrated), which is not a constant multiple
  of log φ, and the local maps f, f_r rescale with it. So the gauge supplies the (β, n)-bookkeeping exactly, and Lemma BR the
  infinitesimal generator, but the finite-γ identity must still absorb the Bessel/Airy corrections (JZC_M4 §7 caveat (c)); H-d
  contributes nothing to that step. Corollary: the scope's planned order "do H-d and Σ together" can be split; H-d is independent.

## 6. Rule A (adversarial pass) — log

1. *Soft-edge twist?* First pass (frame 1): lips and Σ_v both seemed to carry e^{∓2πiδ}, which would make the Airy disc's jump
   product e^{∓2πiδσ₃} ≠ I (impossible for an honest V♮). Error found: Σ_v's entry contains e^{−2iθ_δ} = e^{−2iθ}e^{2πiδ} (from L_±),
   which cancels the phase. Only the lips (θ-free entries) keep it, and the lips avoid U(4c, h₀). Recorded in §3 (ii).
2. *Alternatives to (i):* H2–H4 (§4) and "degree shift without (n/(n+δ))^p" (d₁ would be −(s−1)/2, wrong) are excluded by data.
3. *δ = 0:* F♮ = F, β′ = α; the lattice limit is continuous in every formula of §3 (Prop 2.1's constant is not uniform, see §3).
4. *β′ < −1* (e.g. α = −½, δ = −0.8): D_{x^{β′}} is explicit and only enters through F♮D_W (§3 (iv)), so no integrability of x^{β′} is
   used. The model (m4_rh4) is polynomial/analytic in β; nothing special at β′ = −1. Not tested numerically below β′ = −1.
5. *Is ν really α?* (2.1): the hard-edge Stirling term is O(1/t) for every δ, so W₀'s local power is z^α·(−z)^{2δ}; data exclude H3.
6. *Top node:* X₁ = (n/(1+δ))^p > n^p; the contour must reach X₁ + δ′ (routine, H-a); with ℓ₁ ≡ 1 the bound e^{pc₀}n^p is free.

## 7. What remains (precise gaps)

For H-d (frame 1), p > 1:
- G1. Prop 2.1 (2.4) written as a proof: the B_δ asymptotics (binetcut (iv)'s window argument with 𝔟_∞(δ)) and (O5) at ∞ for F♮.
- G2. Paper 2 App C (Prop apriori) and Lemma sumbound for the Hurwitz U, with the column bookkeeping of §3 (iv).
- G3. p < 1: the seam construction (Lemma seam) with j_δ; Γ(t − δ) has its poles at t = δ − m on arg z = ±πp, inside S_out where D is
  not used. Expected: the seam densities grow like (δ/p)log ζ, so χ produces the same (−z)^δ at ∞ (the monodromy argument of §2 is
  geometry-free and fixes the exponent mod 1; continuity in δ fixes it). Not computed.
- G4. Hurwitz's formula (Lemma H, DLMF 25.11.9 / Apostol Thm 12.6) and DLMF 5.11.8: NOT QUOTED (Rule C).
- G5. Theorem N.6 for the decoupled model M(β, ν): its proof enters β only through ρ² = φ^{2(β+1)} (bounded, analytic on the circles);
  expected routine, not written.
For rule H as stated (n/(n+δ))^pΦ(n+δ): G1–G5 plus Prop S at the orders of N.6(iii) (exact for the integer layer to order 4; orders
5–6 and the μ-layers NUMERICAL). For Σ at all orders: the finite-γ change of frame of §5 (string equation / Bleher–Its route).

*Correction to JZC_M3_scope §3.1 (H-d heuristic).* "After rescaling by ν^p, all jumps are the lattice's at the real parameter ν" is not
what happens: rescaling cannot move the node offset (it sits in θ_δ), and none is needed. The z^{O(δ)} power is exactly (−z)^δ (p-free,
not z^{δ/p}); it is absorbed as a Szegő shift at the hard edge with the degree and the scaling unchanged; the (n/ν)^p factor is Σ's.
