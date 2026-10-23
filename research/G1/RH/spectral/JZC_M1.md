# JZC M1: the equilibrium layer — Theorem Q and the soft-edge expansion (Plan JZC, milestone M1)

Status (2026-10-21; updated 2026-10-23): written in the SPEC exploration session. Rule R: REVIEW_JZC_M1_A.md (ACCEPT WITH FIXES;
fixes applied, §7) and REVIEW_JZC_M1_B.md (reviewer B: re-derived every step, re-ran the checks byte-identically, independent
energy-minimisation numerics; ACCEPT WITH FIXES B1–B7; fixes applied 2026-10-23, §7). **REVIEWED.** Labels per VERIFICATION_POLICY.md. This note is
milestone M1 of the Jacobi–zeta correspondence (the plan is local). It proves the potential-theory layer of SPEC §3.14 Lemma Q
for general constraint densities. It also proves that the continuum soft-edge root carries the pole terms of Z with the
π cot kernel. It says nothing about b_n directly: the link between b_n and the root a_n is part of Hypothesis G (SPEC §3.14).

| # | Statement | Label |
|---|---|---|
| Thm Q | For a locally Hölder constraint σ on (0, Y] with yσ(y) strictly decreasing (and H3), the constrained equilibrium of unit mass with no external field is ν\|_{[0,a]} + σ\|_{[a,Y]}, where a is the unique root of the soft-edge condition (Q). Explicit ν; 0 < ν < σ; strict outer inequality | (i)–(iv) **PROVED + REVIEWED** (no external input: energy positivity is Paper I Lemma 3.3 = research/G2/PROOF.md Lemma EP, PROVED + REVIEWED; (ii) by the elementary per-point balayage argument; fixed per Rule R review B, B1, B2). Was PROVED-mod-cite (Saff–Totik Lemma I.1.8, NOT QUOTED) |
| Cor Q.1 | lattice: a = 4c(p) | PROVED + REVIEWED (the computation; its identification as the equilibrium edge is Thm Q) |
| Prop M1.2 | soft-edge root a_n for a counting function with a power expansion: first-order terms −R·L̃(q)(a/n^p)^q at the poles of Z_N with π cot kernel (Lemma K0), plus integer terms; higher orders by reversion (resonant q ∈ ℕ and log laws excluded) | PROVED + REVIEWED (termwise integration, explicit remainder; REVIEW_JZC_M1_A F1(c); re-derived in REVIEW_JZC_M1_B §1) |
| Checks | m1_theoremQ.out (4 densities, 32 assertions), m1_edge.out (continuum pole term to ≤ 10⁻⁸ (printed digits)–10⁻⁶, 4 assertions) | NUMERICAL |
| Novelty | Thm Q (explicit ν, the criterion "yσ (or √yσ) decreasing", infinite-mass constraint with a hard edge and no void) | POSSIBLY-NEW (§6; pending Beckermann–Kuijlaars 2001, Kuijlaars 2000, Dragnev–Saff §4; B6 caveats) |

## 1. Setting

The constraint σ is a density on (0, Y], with 0 < Y ≤ ∞. It is the continuum density of the nodes in the edge variable,
normalised so that n nodes have mass 1. For the lattice σ_{p,s}, σ(y) = (1/p)y^{−1/p−1} on (0, ∞).

Hypotheses:
- (H1) σ is positive and locally Hölder continuous on (0, Y). The Hölder condition is needed only for the Hilbert transform
  in (iii) (not in (ii), after the per-point argument of review B, B2; review A F2 gives an a.e. alternative in (iii)); every
  density in SPEC is real-analytic.
- (H2) y ↦ yσ(y) is strictly decreasing on (0, Y).
- (H3) If Y = ∞: ∫_1^∞σ(y)log y dy < ∞.

(H2) implies:
- g(y) := √y·σ(y) = yσ(y)/√y is strictly decreasing;
- σ(y) ≥ y₀σ(y₀)/y for y < y₀, so ∫_0σ = ∞;
- yσ(y) → 0 at ∞ once ∫^∞σ < ∞.
So (H3) only asks for the log-moment (REVIEW_JZC_M1_A F6).

*Weaker hypothesis* (F7). Steps (ii)–(iv) use only "g strictly decreasing". Step (i) needs only existence, F(0⁺) = ∫_0^Yσ > 1.
Uniqueness of the root then follows from (iv): a is the left end of the saturation set of the unique minimiser. So (H2) may be
replaced by "√y·σ(y) strictly decreasing and ∫_0^Yσ > 1". The reviewer checked this numerically on σ = 0.2y^{−0.9} on (0, 10],
where (H2) fails. Neither condition is necessary. The problem is to minimise
I(μ) = ∫∫log(1/|x − y|)dμ(x)dμ(y) over positive μ on [0, Y] with μ([0, Y]) = 1 and μ ≤ σ.

Soft-edge condition:

  F(a) := ∫_a^Y σ(y)(1 − a/y)^{−1/2}dy = 1.     (Q)

## 2. Theorem Q

**Theorem Q.** Assume (H1)–(H3).
- (i) (Q) has exactly one root a ∈ (0, Y).
- (ii) Put s(y) := σ(y)√(y/(y − a)) on (a, Y), and

    ν(x) := (1/π)·√((a − x)/x)·∫_a^Y s(y)/(y − x) dy,   0 < x < a.

  Then μ := ν dx|_{[0,a]} + σ dy|_{[a,Y]} has unit mass, 0 < ν(x) < σ(x) on (0, a), and ν(x)√(x(a − x))·π equals
  1 − ∫_a^Yσ(y)√(y(y − a))/(y − x)dy (the balayage form).
- (iii) There is a constant ℓ with U^μ = ℓ on [0, a] and U^μ < ℓ on (a, Y]. (Wording fixed per Rule R review B, D4.)
- (iv) μ is the unique solution of the constrained equilibrium problem. (Wording matched to Paper IV, review B D3: no
  competitor has I = −∞, so no finite-energy restriction is needed.)

*Proof.*
- **(i).** F(a) = ∫_1^{Y/a}aσ(au)(1 − 1/u)^{−1/2}du. For fixed u, aσ(au) = (au·σ(au))/u is strictly decreasing in a (H2), and the
  upper limit Y/a decreases. So F is strictly decreasing. F is continuous on (0, Y) by dominated convergence (on [a₀, a₁],
  aσ(au) ≤ a₀σ(a₀u) by (H2)) (fixed per Rule R review B, B4), so the intermediate value theorem applies.
  - As a → 0: F(a) ≥ ∫_a^Yσ → ∞ by (H2): yσ decreasing gives σ(y) ≥ σ(1)/y on (0, 1], so ∫_0σ = ∞ (Paper IV draft note;
    previously attributed to (H3)).
  - As a → Y (Y < ∞), F → 0. If Y = ∞, split at 2a: ∫_{2a}^∞ ≤ √2∫_{2a}^∞σ → 0, and ∫_a^{2a} ≤ σ(a)·a·∫_1^2(1 − 1/u)^{−1/2}du → 0,
    since yσ(y) → 0 and σ(y) ≤ aσ(a)/y on [a, 2a].
- **(ii), Cauchy transform, by per-point balayage** (REVIEW_JZC_M1_A F1(b); fixed per Rule R review B, B2: the earlier
  Liouville argument, "G − G̃ entire and → 0 at ∞", did not control G − G̃ near the positive axis when Y = ∞, and its Morera
  step needed the Plemelj–Privalov theorem, NOT QUOTED). Put S(z) := ∫_a^Y s(y)/(z − y)dy and

      G̃(z) := √((z − a)/z)·S(z)     (G)

  (principal branch, analytic off [0, Y]). Let μ := ν dx|_{[0,a]} + σ dy|_{[a,Y]} with ν as stated, and G(z) := ∫dμ(x)/(z − x).
  - **One saturated point.** For fixed y ∈ (a, Y) put k_y(z) := (√((z − a)/z) − √((y − a)/y))/(z − y). It is analytic off
    [0, a] (the singularity at z = y is removable), O(|z|^{−1/2}) at 0, bounded at a, ~ (1 − √((y − a)/y))/z at ∞, and its jump
    on (0, a) is −2πiρ_y, with ρ_y(x) := (1/π)√((a − x)/x)/(y − x) > 0 (the branch values ±i√((a − x)/x) from above and below).
    The support [0, a] is compact, so plain Liouville gives k_y(z) = ∫_0^aρ_y(x)dx/(z − x), and ρ_y has mass 1 − √((y − a)/y).
  - **Superposition.** Since σ = s·√((y − a)/y),

      G̃(z) = ∫_a^Y s(y)[√((y − a)/y)/(z − y) + k_y(z)]dy = ∫_a^Y σ(y)dy/(z − y) + ∫_0^a ν(x)dx/(z − x) = G(z),

    by Fubini (everything is positive, |1/(z − x)| ≤ 1/|Im z|, and ∫s(y)(1 − √((y − a)/y))dy ≤ F(a) < ∞); here
    ν(x) = ∫s(y)ρ_y(x)dy is exactly the ν of the statement. So G̃ is the Cauchy transform of μ, of total mass
    ∫_a^Yσ + ∫s(1 − √((y − a)/y)) = ∫s = F(a). The boundary values on (0, a) need only the real-analyticity of S there.
    (Checked numerically by review B, kyB.py: |k_y − C[ρ_y]| ≤ 1.2·10⁻¹⁵ at 12 points, mass to 2·10⁻¹⁶.)
  Consequences:
  - μ has mass F(a) = 1 by (Q).
  - Re G(x ± i0) = 0 on (0, a), so U^μ is constant on [0, a].
  - ν = −(1/π)Im G(x + i0) is positive, because S(x) < 0 there.
  - The balayage form of ν follows from the identity R(y)σ(y) = s(y)(y − a), which gives
    G̃ = (1/R(z))[F(a) + ∫σR/(z − y)dy]. ν_explicit − ν_balayage = (F(a) − 1)/(π√(x(a − x))), which vanishes exactly under (Q).
  This is (G); no balayage theorem is used.
- **(ii), ν < σ.** Write s(y) = g(y)(y − a)^{−1/2} with g decreasing, and use ∫_a^∞(y − a)^{−1/2}(y − x)^{−1}dy = π/√(a − x):

    ν(x) < (1/π)√((a − x)/x)·g(a⁺)·π/√(a − x) = g(a⁺)/√x ≤ g(x)/√x = σ(x),   0 < x < a.

- **(iii).** On (0, a) equilibrium holds by (ii). For z ∈ (a, Y), φ(z) := U^μ(z) − ℓ has φ(a) = 0 by continuity, and
  φ′(z) = −Re G(z ± i0) = −√((z − a)/z)·H(z), where H(z) := PV∫_a^Y s(y)/(z − y)dy. Writing s = g·(y − a)^{−1/2},

    H(z) = ∫_a^Y (g(y) − g(z))(y − a)^{−1/2}/(z − y) dy + g(z)·PV∫_a^Y (y − a)^{−1/2}/(z − y) dy.

  - The first integrand is positive for every y ≠ z, because g is decreasing.
  - The second PV integral is 0 if Y = ∞ (it is the cot(π/2) = 0 of Lemma K0), and
    (z − a)^{−1/2}log[(√(Y − a) + √(z − a))/(√(Y − a) − √(z − a))] > 0 if Y < ∞.
  So H > 0, φ′ < 0 on (a, Y), and φ < 0 there. The Hilbert transform exists pointwise because σ is locally Hölder (H1); this
  is the only use of the Hölder condition (review B, B2).
- **(iv).** Let μ′ ≤ σ have unit mass and I(μ′) < ∞ (competitors with I(μ′) = +∞ are trivially worse, and I(μ′) > −∞ always,
  since log⁺|x − y| ≤ log(1 + x) + log(1 + y) and (H3) gives the log-moment). Then

    I(μ′) − I(μ) = I(μ′ − μ) + 2∫(U^μ − ℓ)d(μ′ − μ).

  - On [0, a], U^μ = ℓ at every point (U^μ is continuous: the density of μ is ≤ g(a)x^{−1/2} on (0, a) and bounded on [a, Y]),
    so this part contributes 0.
  - On (a, Y], μ = σ ≥ μ′ and U^μ − ℓ < 0, so (U^μ − ℓ)(μ′ − μ) ≥ 0 there.
  - **I(μ′ − μ) ≥ 0, with equality iff μ′ = μ.** τ := μ′ − μ is a finite signed measure with τ(ℝ) = 0. It satisfies
    ∬|log|x − y|| d|τ| d|τ| < ∞: the log⁺ part by the log-moments (H3), the log⁻ part because μ has density ≤ g(a)·max(x^{−1/2},
    a^{−1/2}) (so its log⁻-potential is bounded) and I(μ′) < ∞. Paper I Lemma 3.3 (= G2 PROOF.md Lemma EP, REVIEWED) applies.
    (Fixed per Rule R review B, B1. In detail: |τ| ≤ μ + μ′, of mass 2, so it suffices that ∬|log|x − y|| dα dβ < ∞ for
    α, β ∈ {μ, μ′}. log⁺|x − y| ≤ log(1 + x) + log(1 + y), and the log-moments of μ, μ′ are finite: on bounded sets log(1 + x)
    is bounded and the masses are 1, at ∞ μ, μ′ ≤ σ and (H3). The log⁻ part with μ: sup_x∫log⁺(1/|x − t|)dμ(t) ≤
    g(a)·sup_x∫_{|x−t|<1}log(1/|x − t|)(t^{−1/2} + a^{−1/2})dt < ∞, which bounds the (μ, μ) and (μ, μ′) terms; the (μ′, μ′) term
    by I(μ′) < ∞ and the log⁺ bound. Lemma EP, verbatim in research/G2/PROOF.md §1 and papers/paper1/main.tex `lem:positivity`:
    "Let ν be a finite signed Borel measure on ℝ with ν(ℝ) = 0 and ∬|log|x − y|| d|ν|(x) d|ν|(y) < ∞. Then
    −∬log|x − y| dν dν = ∫_0^∞|ν̂(ξ)|²/ξ dξ ≥ 0, with equality iff ν = 0." No compact support is assumed, so the earlier
    inversion x ↦ 1/(1 + x) and the NOT QUOTED Saff–Totik Lemma I.1.8 are no longer used.)
  Hence μ minimises, and it is unique. ∎

**Corollary Q.1 (lattice).** For σ = (1/p)y^{−1/p−1}, yσ = (1/p)y^{−1/p} is strictly decreasing and (H3) holds. (Q) gives
a^{−1/p}(1/p)B(1/p, ½) = 1, i.e. a^{1/p} = √πΓ(1/p + 1)/Γ(1/p + ½) = π/(2I(p)), so **a = 4c(p)**. This is the constant of Law P,
obtained here without Riemann–Hilbert analysis.

*Remarks.*
- (G) is the structural formula. Without (Q), ν has a ±(a − x)^{−1/2} term at a, which violates either ν ≥ 0 or ν ≤ σ. The
  soft-edge condition removes it: ν(a⁻) = g(a)/√a = σ(a), so μ is continuous at a. If σ is Hölder of order > ½ near a
  (e.g. C¹), σ − ν = C√(a − x)(1 + o(1)) with C = −h(a)/(π√a) > 0,
  h(a) := ∫_a^Y(g(y) − g(a))(y − a)^{−3/2}dy − 2g(a)(Y − a)^{−1/2}[Y < ∞]. (The integral can diverge when g is only Hölder of
  order ≤ ½ at a. Fixed per Rule R review B, B3; this is the same h as in JZC_W_plt1 Prop 2(vi).)
  (Corrected per REVIEW_JZC_M1_A F3. An earlier version said the density vanishes at a; it does not. The reviewer measured C =
  0.4713, 0.1245 and 0.3239 for p = 0.6, p = 1.5 and the drum; review B's 30-digit −h(a)/(π√a) gives 0.47126578 and
  0.12449756 for p = 0.6 and 1.5.)
- (H2) is a natural condition: "fewer nodes per logarithmic scale as y grows". It holds for every regular spectrum in SPEC,
  including drums cut at the first node and log-modified laws (§4).

## 3. Proposition M1.2: the soft-edge root carries the poles of Z with the π cot kernel

Let N(λ) be a C¹ counting function on [λ₀, ∞) with N′ > 0 and asymptotic expansion N(λ) ~ Σ_ρc_ρλ^ρ as λ → ∞ (exponents ρ
decreasing from ρ_max = 1/p, with c_{1/p} = 1, and termwise differentiable). Put Z_N(s) := ∫λ^{−s}dN(λ), continued
meromorphically: it has simple poles at s = ρ with residue ρc_ρ. In the variable w = −s, w ↦ Z_N(−w) has poles at q = −ρ with
residue R_q = −ρc_ρ. Take L(u) := (1 − u)^{−1/2}1_{u<1} and its Mellin transform L̃(w) = −π cot(πw)Γ(w + ½)/(√πΓ(w + 1)) (SPEC
Lemma K0).

**Proposition M1.2.** Assume N′ = Σ_{k<K}ρ_kc_kλ^{ρ_k−1} + r_K with r_K = O(λ^{ρ_K−1}) for every K. Assume also that no
exponent ρ ∈ {−1, −2, …} has ρc_ρ ≠ 0, i.e. no resonance q ∈ ℕ (resonances give A^j log A terms, SPEC §3.13; log laws are excluded
too). Then as A → 0⁺,

  ∫L(Aλ)dN(λ) ~ −Σ_q R_q·L̃(q)·A^q + Σ_{j≥0} C(2j, j)4^{−j}Z_N(−j)A^j,

where Z_N(−j) are the continued values (which depend on λ₀). With A = 4c(1 + η)/n^p, the root of ∫L(Aλ)dN = n is

  η = (p/n)·[Σ_{q ≠ Weyl}R_qW(q)π cot(πq)n^{−pq} + Σ_{j≥0}W(j)Z_N(−j)n^{−jp}] + O(η²),

and the higher orders follow by series reversion. (Remainder written per Rule R review B, B7: the earlier "+ O(nη²)" is the
error in nη, not in η.) The Weyl pole q = −1/p gives the leading term n(a/4c)^{−1/p}, i.e. the
equation itself. At q ∈ −½ − ℕ₀ (for example the drum perimeter, q = −½), W(q)π cot(πq) is the finite limit 0·∞; there,
−(4c)^qL̃(q) is meant, and L̃(−½) = π (REVIEW_JZC_M1_A F4).

*Proof (termwise; REVIEW_JZC_M1_A F1(c)).*
- **Each power.** For dN = ρc_ρλ^{ρ−1}dλ on [λ₀, ∞), substitute u = Aλ:

    ∫_{λ₀}^{1/A}(1 − Aλ)^{−1/2}ρc_ρλ^{ρ−1}dλ = ρc_ρ[A^{−ρ}B(ρ, ½) − Σ_jC(2j, j)4^{−j}A^jλ₀^{ρ+j}/(ρ + j)].

  Here B(ρ, ½) means L̃(−ρ), continued for ρ ≤ 0. The first term is −R_qL̃(q)A^q, with q = −ρ and R_q = −ρc_ρ.
- **The remainder r_K.** Split at λ = 1/(2A). On [λ₀, 1/(2A)], Taylor-expand (1 − Aλ)^{−1/2}. On [1/(2A), 1/A], bound
  |r_K| ≤ Cλ^{ρ_K−1}, which gives O(A^{−ρ_K}).
- **Integer coefficients.** They combine into the continued Z_N(−j), taking K so large that ρ_K < −j.
- **Result.** The expansion holds with an explicit O(A^{−ρ_K}) remainder. The root follows by the implicit function theorem
  around η = 0. Every cross term η × (correction) is O(nη²) in the equation, i.e. O(η²) in η after division by n/p (B7).
- **Note.** The Mellin–Barnes form (1/2πi)∫L̃(w)Z_N(−w)A^wdw is the same statement, but shifting its contour needs decay of
  Z_N(−w) on vertical lines, since |L̃| ~ |t|^{−1/2} there. The termwise proof avoids this. ∎

**Consequences.**
- **Pole law.** The continuum equilibrium alone already contains the pole law of SPEC §3.12, +pR_qW(q)π cot(πq)n^{−1−pq} in
  n^pb_n/c, provided Hypothesis G1 (the Riemann–Hilbert g-function is this equilibrium). Check: m1_edge.out. The first-order
  γ-part of n·η for N = κ(λ) of λ_k = (k + γk^{−m})^p, at (p, m) = (1.5, ½), (0.75, ¼), (1.25, ½), (1.8, ¾), matches
  pRW(q)π cot(πq) to ≤ 10⁻⁸ (printed digits), 1·10⁻⁶, 1·10⁻⁷ and 1·10⁻⁶ (review B: the first value cannot be read below the
  8 printed digits; review A measured 2·10⁻¹⁴ independently).
- **Nonlinear terms, exactly.** For drums (p = 1, N = λ − β√λ), the root is quadratic in (1 + η)^{−1/2}, and
  D ⊃ −(πβ/(2√2))√n + (π²/16)β² exactly (SPEC §3.16).
- **What M1 does not give.**
  - The discreteness values Z(−j) of the actual node set. These enter through the band factor (M2), not the continuum.
    The continuum Z_N(−j) here are cutoff-dependent and are not the spectral ones.
  - The second-order layer (M4).

## 4. Checks (NUMERICAL)

`checks/m1_theoremQ.py`, `checks/m1_theoremQ.out`: 32 assertions on four densities, two of them not power laws.
- Power laws: p = 0.6 and 1.5 (a = 4c to 10⁻¹²).
- A drum: p = 1, N = λ − β√λ, cut at the first node.
- A log law: N(T) = (T/2π)log(T/2πe), λ = T², cut at T = 2πe^{1.5}.
For each density:
- (H2) holds on a grid;
- the explicit and balayage forms of ν agree to 10⁻²¹;
- 0 < ν/σ < 1 at five points;
- the total mass is 1 to 10⁻¹¹;
- Φ(z) = (z − a)H(z) > 0 at three points of (a, Y);
- −√((z − a)/z)Φ(z)/(z − a) equals U′(z) (central difference of the direct potential) at z = 1.5a, to ≤ 10⁻⁴ relative (added
  per Rule R review B, B5; measured 3.9·10⁻⁷–6.3·10⁻⁷).

`checks/m1_edge.py`, `checks/m1_edge.out`: Proposition M1.2's pole term, from the first-order γ-part of the continuum root over
n = 100–6400, with the cross terms (n⁰, n^{−1}, n^{−1−pq}, n^{−pq−jp}, n^{−1−jp}) in the fit. Four cases agree to ≤ 10⁻⁸ (printed
digits)–10⁻⁶;
the tolerance is now 10⁻⁵ relative (F9). The m = 1 cases are excluded, because there pq = 1 coincides with the n^{−1} cross
term, the continuum analogue of the d₂ merge. The reviewer's independent exact linearisation in g (closed forms, 40 digits,
n up to 10¹⁰) gives 2·10⁻¹⁴ and 4·10⁻¹⁰ on two of these cases, and 7·10⁻¹² on a new case, (p, m) = (0.6, 0.2).

What m1_theoremQ tests (REVIEW_JZC_M1_A F5):
- "ν formulas agree" and "mass 1" are identities in F(a). They test the accuracy of the root and the quadrature, not (G).
- The outer inequality is tested twice: via Φ, and by a direct potential evaluation (U − ℓ on the band and on (a, Y]).
- (H2) is verified analytically for each test density, as listed in the script, and on a fine grid of the derivative of yσ.
- The reviewer's sabotage of the finite-Y PV sign passed the old assertions. (Fixed per Rule R review B, B5: the direct
  potential check alone did *not* catch it — review B re-ran sabotage S1, the sign of `logpart` in Φ flipped, and got ALL 28
  CHECKS PASSED, because no assertion compared Φ with anything.) The assertion "Φ matches direct U′" now ties Φ to the direct
  potential; with S1 applied to the new script the drum and log-law assertions fail (2 of 32), and the unsabotaged script
  passes all 32.

## 5. Rule A

- *Is (G) consistent with Lemma Q's numerics in SPEC §3.14?* Yes. The outer inequality is now proved, where §3.14 only had
  numerics. (The agreement of the two ν forms to 10⁻²¹ is an identity once (Q) holds; F5.)
- *Is (H2) needed?* It is used once, in (i) (monotonicity of F). Steps (ii)–(iii) need only g decreasing. A density with g
  increasing somewhere could, in principle, open a second band or a saturated island (review B). Theorem Q is then silent.
  Review B's independent discretised energy minimisation (REVIEW_JZC_M1_B §2.5, NUMERICAL) found: (H2) and the weaker
  hypothesis F7 are sufficient but not necessary (several densities with g non-monotone still give band | saturated with the
  formula's edge); but they cannot simply be dropped: a density with a dip gives three roots of (Q) and a minimiser with two
  bands (band | sat | band | sat), and a shallower dip gives a single root but a saturated island inside the band. At the three
  roots, (ii) (ν < σ) or (iii) (H > 0) or both fail, so the two uses of monotone g (on (0, a) and on (a, Y)) are distinct.
- *The finite-Y case.* Drums and zeros are cut at the first node. The extra PV term in H is positive, so the cut helps.
  Beyond Y there is no condition, since μ = σ = 0 there.
- *Non-compactness.* I(μ′ − μ) ≥ 0 for non-compactly supported zero-mass signed measures is Paper I Lemma 3.3 (= G2 Lemma
  EP, PROVED + REVIEWED), which needs no compact support; its integrability hypothesis is checked in (iv). No external input
  remains (fixed per Rule R review B, B1).

## 6. Novelty (first pass)

- Constrained equilibrium problems for discrete orthogonal polynomials: Rakhmanov 1996, Dragnev–Saff 1997, Kuijlaars–
  Rakhmanov 1998. Their Riemann–Hilbert use: Baik–Kriecherbauer–McLaughlin–Miller (arXiv math/0310278).
- (Fixed per Rule R review B, B6.) Rakhmanov 1996 Thm 3, Dragnev–Saff 1997 Thms 2.1, 2.6 and Van Assche–Van Baelen are
  quoted with hypotheses in research/G2/CITATIONS.md, entries (R96), (DS97), (VAVB). None is an input of Theorem Q, and their
  hypotheses are not met here: Rakhmanov assumes σ on [−1, 1] with continuous potential, and Dragnev–Saff (Def 1.2) a *finite*
  constraint, whereas σ here has infinite mass at 0. Existence and uniqueness of the constrained minimiser come from (iv)
  directly.
- In the excerpts read, BKMM characterise the minimiser variationally, assume square-root behaviour at the edges, and state no
  general explicit formula. Explicit formulas exist for classical weights (Krawtchouk, Hahn).
- Closely related structures are known, and are now cited (REVIEW_JZC_M1_A F10). According to Beckermann–Kuijlaars (ETNA
  2002; NOT QUOTED in any CITATIONS.md, read only through a tool extraction, B6(c)), there are endpoint equations of the same Cauchy-integral type for a band/saturated transition (their
  Thm 2.8). They also have a monotonicity "ansatz criterion" guaranteeing the band/saturated structure (Thm 2.7: (x − A)Q′ and
  (B − x)Q̃′ increasing, after Kuijlaars, Duke 2000, and Kuijlaars–McLaughlin). Both are for compact support with an external
  field and a void.
- The present setting is different: no external field, a non-compact constraint with infinite mass at 0, a hard edge at 0, and
  no void. The explicit factorisation (G) and the criterion "yσ (or √yσ) decreasing" appear to be this project's.
- **Verdict: POSSIBLY-NEW** as a specialisation of the one-cut constrained framework, pending a reading of Kuijlaars 2000 (SIAM
  J. Matrix Anal. Appl., Q ≡ 0; abstract only), Beckermann–Kuijlaars 2001 (NOT READ) and Dragnev–Saff 1997 §4. The identification of (Q) with Law P's constant and with the per-node
  law of S2′ is this project's.

## 7. Review log

REVIEW_JZC_M1_A.md (ACCEPT WITH FIXES), applied 2026-10-21:
- F1 (MAJOR): (a) inversion to compact support (one remaining citation, Saff–Totik Lemma I.1.8); (b) balayage replaced by the
  Liouville argument; (c) termwise proof of M1.2, relabelled PROVED.
- F2: Hölder continuity added to (H1).
- F3: the edge remark corrected.
- F4: the M1.2 statement excludes resonances and log laws, and covers the 0·∞ points.
- F5: direct potential check and analytic (H2) checks added to m1_theoremQ.
- F6/F7: (H3) simplified; the weaker hypothesis noted.
- F8: Cor Q.1 label.
- F9: docstrings; m1_edge tolerance 10⁻⁵.
- F10: novelty, POSSIBLY-NEW with citations.

REVIEW_JZC_M1_B.md (reviewer B, ACCEPT WITH FIXES), applied 2026-10-23:
- B1 (MAJOR for the label): (iv) uses Paper I Lemma 3.3 = G2 Lemma EP (statement and hypotheses checked against
  research/G2/PROOF.md §1 and papers/paper1/main.tex `lem:positivity`; Lemma 3.3 is its number in papers/paper1/main.pdf),
  with the integrability check for τ = μ′ − μ. Inversion and Saff–Totik dropped. Thm Q PROVED (no external input).
- B2: (ii) by the per-point balayage argument (k_y); Hölder needed only in (iii). JZC_W_plt1 Prop 2 (κ < 0) has the same gap;
  a note there points here.
- B3: soft-edge remark qualified (Hölder > ½ at a), constant C = −h(a)/(π√a).
- B4: continuity of F stated.
- B5: m1_theoremQ.py gains "Φ matches direct U′" (4 assertions, 32 in all); re-run ALL 32 CHECKS PASSED; sabotage S1 on a copy
  of the new script now FAILS (drum and log law); §4 sentence corrected.
- B6: §6 points to G2/CITATIONS.md (R96), (DS97), (VAVB) with the hypothesis caveats; BK2002 as "according to".
- B7: η remainder O(η²).
- Discrepancies D3 (wording of (iv)), D4 (ℓ), D10 (Rule A numerics) adopted; Paper IV sec3.tex updated in parallel.
Labels: Thm Q (i)–(iv), Cor Q.1, Prop M1.2 PROVED + REVIEWED; checks NUMERICAL; novelty POSSIBLY-NEW.
