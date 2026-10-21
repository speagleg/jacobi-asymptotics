# JZC M1: the equilibrium layer — Theorem Q and the soft-edge expansion (Plan JZC, milestone M1)

Status (2026-10-21): written in the SPEC exploration session; NOT REVIEWED. Labels per VERIFICATION_POLICY.md. This note is
milestone M1 of the Jacobi–zeta correspondence (the plan is local). It proves the potential-theory layer of SPEC §3.14 Lemma Q
for general constraint densities. It also proves that the continuum soft-edge root carries the pole terms of Z with the
π cot kernel. It says nothing about b_n directly: the link between b_n and the root a_n is part of Hypothesis G (SPEC §3.14).

| # | Statement | Label |
|---|---|---|
| Thm Q | For a constraint σ on (0, Y] with yσ(y) strictly decreasing (and H3), the constrained equilibrium of unit mass with no external field is ν\|_{[0,a]} + σ\|_{[a,Y]}, where a is the unique root of the soft-edge condition (Q). Explicit ν; 0 < ν < σ; strict outer inequality | PROVED-mod-cite (balayage onto an interval, Saff–Totik; sufficiency of the variational inequalities — proved here — needs positivity of log energy for zero-mass signed measures with non-compact support, NOT QUOTED) |
| Cor Q.1 | lattice: a = 4c(p) | PROVED (from Thm Q) |
| Prop M1.2 | soft-edge root a_n for a counting function with an asymptotic expansion: first-order terms −R·L̃(q)(a/n^p)^q at the poles of Z_N with π cot kernel (Lemma K0), plus integer terms; higher orders by reversion | PROVED-mod-cite (Mellin asymptotics of ∫L(Aλ)dN, standard, NOT QUOTED) |
| Checks | m1_theoremQ.out (4 densities, 20 assertions), m1_edge.out (continuum pole term to 10⁻⁹–10⁻⁶, 4 assertions) | NUMERICAL |

## 1. Setting

The constraint σ is a density on (0, Y], with 0 < Y ≤ ∞. It is the continuum density of the nodes in the edge variable,
normalised so that n nodes have mass 1. For the lattice σ_{p,s}, σ(y) = (1/p)y^{−1/p−1} on (0, ∞).

Hypotheses:
- (H1) σ is continuous and positive on (0, Y).
- (H2) y ↦ yσ(y) is strictly decreasing on (0, Y).
- (H3) ∫_0^1σ = ∞. If Y = ∞: ∫_1^∞σ(y)log y dy < ∞ and yσ(y) → 0.

(H2) implies that g(y) := √y·σ(y) = yσ(y)/√y is strictly decreasing. The problem is to minimise
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
- (iii) U^μ = ℓ on [0, a], and U^μ < ℓ on (a, Y].
- (iv) μ is the constrained equilibrium measure.

*Proof.*
- **(i).** F(a) = ∫_1^{Y/a}aσ(au)(1 − 1/u)^{−1/2}du. For fixed u, aσ(au) = (au·σ(au))/u is strictly decreasing in a (H2), and the
  upper limit Y/a decreases. So F is strictly decreasing.
  - As a → 0: F(a) ≥ ∫_a^Yσ → ∞ (H3).
  - As a → Y (Y < ∞), F → 0. If Y = ∞, split at 2a: ∫_{2a}^∞ ≤ √2∫_{2a}^∞σ → 0, and ∫_a^{2a} ≤ σ(a)·a·∫_1^2(1 − 1/u)^{−1/2}du → 0,
    since yσ(y) → 0 and σ(y) ≤ aσ(a)/y on [a, 2a].
- **(ii), Cauchy transform.** Let R(z) := √(z(z − a)), analytic off [0, a], with R(z) ~ z at ∞.
  - The balayage of δ_y (y > a) onto [0, a] has Cauchy transform C_y(z) = (1 − R(y)/R(z))/(z − y). It is analytic off [0, a]
    (removable at z = y) and ~ 1/z at ∞, and its boundary values give the density √(y(y − a))/(π(y − x)√(x(a − x))).
  - With ω the arcsine measure (Cauchy transform 1/R), ν := ω − Bal(σ|_{[a,Y]}) has U^ν + U^{σ|[a,Y]} constant on [0, a]
    (Saff–Totik, balayage onto an interval), and total mass 1 − ∫_a^Yσ. So μ has unit mass.
  - Its Cauchy transform is G(z) = ∫dμ(x)/(z − x) = (1/R(z))[1 + ∫_a^Yσ(y)R(y)/(z − y)dy].
  - By (Q), 1 = ∫_a^Y s, and R(y)σ(y) = s(y)(y − a). So

      G(z) = ((z − a)/R(z))·∫_a^Y s(y)dy/(z − y) = √((z − a)/z)·S(z),   S(z) := ∫_a^Y s(y)/(z − y)dy.     (G)

  - On (0, a), √((z − a)/z) has boundary value i√((a − x)/x) from above, so ν(x) = −(1/π)Im G(x + i0) is the stated formula.
    It is positive, because S(x) < 0 there.
- **(ii), ν < σ.** Write s(y) = g(y)(y − a)^{−1/2} with g decreasing, and use ∫_a^∞(y − a)^{−1/2}(y − x)^{−1}dy = π/√(a − x):

    ν(x) < (1/π)√((a − x)/x)·g(a⁺)·π/√(a − x) = g(a⁺)/√x ≤ g(x)/√x = σ(x),   0 < x < a.

- **(iii).** On (0, a) equilibrium holds by balayage. For z ∈ (a, Y), φ(z) := U^μ(z) − ℓ has φ(a) = 0 by continuity, and
  φ′(z) = −Re G(z ± i0) = −√((z − a)/z)·H(z), where H(z) := PV∫_a^Y s(y)/(z − y)dy. Writing s = g·(y − a)^{−1/2},

    H(z) = ∫_a^Y (g(y) − g(z))(y − a)^{−1/2}/(z − y) dy + g(z)·PV∫_a^Y (y − a)^{−1/2}/(z − y) dy.

  - The first integrand is positive for every y ≠ z, because g is decreasing.
  - The second PV integral is 0 if Y = ∞ (it is the cot(π/2) = 0 of Lemma K0), and
    (z − a)^{−1/2}log[(√(Y − a) + √(z − a))/(√(Y − a) − √(z − a))] > 0 if Y < ∞.
  So H > 0, φ′ < 0 on (a, Y), and φ < 0 there.
- **(iv).** Let μ′ ≤ σ have unit mass and finite energy. Then

    I(μ′) − I(μ) = I(μ′ − μ) + 2∫(U^μ − ℓ)d(μ′ − μ).

  - On [0, a], U^μ = ℓ, so this part contributes 0.
  - On (a, Y], μ = σ ≥ μ′ and U^μ − ℓ < 0, so (U^μ − ℓ)(μ′ − μ) ≥ 0 there.
  - I(μ′ − μ) ≥ 0 for signed measures of zero total mass and finite logarithmic energy. This is classical for compact
    support; for our non-compact support with the tail of (H3) it is NOT QUOTED (Rule C).
  Hence μ minimises, and it is unique by strict positivity. ∎

**Corollary Q.1 (lattice).** For σ = (1/p)y^{−1/p−1}, yσ = (1/p)y^{−1/p} is strictly decreasing and (H3) holds. (Q) gives
a^{−1/p}(1/p)B(1/p, ½) = 1, i.e. a^{1/p} = √πΓ(1/p + 1)/Γ(1/p + ½) = π/(2I(p)), so **a = 4c(p)**. This is the constant of Law P,
obtained here without Riemann–Hilbert analysis.

*Remarks.*
- (G) is the structural formula. The soft-edge condition is exactly what turns the generic 1/R(z) behaviour into
  √((z − a)/z), i.e. square-root vanishing of the density at the soft edge a.
- (H2) is a natural condition: "fewer nodes per logarithmic scale as y grows". It holds for every regular spectrum in SPEC,
  including drums cut at the first node and log-modified laws (§4).

## 3. Proposition M1.2: the soft-edge root carries the poles of Z with the π cot kernel

Let N(λ) be a C¹ counting function on [λ₀, ∞) with N′ > 0 and asymptotic expansion N(λ) ~ Σ_ρc_ρλ^ρ as λ → ∞ (exponents ρ
decreasing from ρ_max = 1/p, with c_{1/p} = 1, and termwise differentiable). Put Z_N(s) := ∫λ^{−s}dN(λ), continued
meromorphically: it has simple poles at s = ρ with residue ρc_ρ. In the variable w = −s, w ↦ Z_N(−w) has poles at q = −ρ with
residue R_q = −ρc_ρ. Take L(u) := (1 − u)^{−1/2}1_{u<1} and its Mellin transform L̃(w) = −π cot(πw)Γ(w + ½)/(√πΓ(w + 1)) (SPEC
Lemma K0).

**Proposition M1.2.** As A → 0⁺,

  ∫L(Aλ)dN(λ) ~ −Σ_q R_q·L̃(q)·A^q + Σ_{j≥0} C(2j, j)4^{−j}Z_N(−j)A^j,

where Z_N(−j) are the continued values (which depend on λ₀). With A = 4c(1 + η)/n^p, the root of ∫L(Aλ)dN = n is

  η = (p/n)·[Σ_{q ≠ Weyl}R_qW(q)π cot(πq)n^{−pq} + Σ_{j≥0}W(j)Z_N(−j)n^{−jp}] + O(nη²),

and the higher orders follow by series reversion. The Weyl pole q = −1/p gives the leading term n(a/4c)^{−1/p}, i.e. the
equation itself.

*Proof (mod-cite).* This is the Mellin–Barnes representation ∫L(Aλ)dN = (1/2πi)∫L̃(w)Z_N(−w)A^wdw, with the contour shifted
right. The poles of L̃ at w = j give the Taylor terms of L (C(2j, j)4^{−j}). The poles of Z_N(−w) give −R_qL̃(q)A^q, and
(4c)^qΓ(q + ½)/(√πΓ(q + 1)) = W(q). The shift is justified because L has a single integrable singularity at u = 1 and N is
smooth near λ = 1/A, so there are no oscillatory terms; the standard Mellin asymptotic theorem (Flajolet–Gourdon–Dumas) is
NOT QUOTED. The root follows from the implicit function theorem around η = 0. ∎

**Consequences.**
- **Pole law.** The continuum equilibrium alone already contains the pole law of SPEC §3.12, +pR_qW(q)π cot(πq)n^{−1−pq} in
  n^pb_n/c, provided Hypothesis G1 (the Riemann–Hilbert g-function is this equilibrium). Check: m1_edge.out. The first-order
  γ-part of n·η for N = κ(λ) of λ_k = (k + γk^{−m})^p, at (p, m) = (1.5, ½), (0.75, ¼), (1.25, ½), (1.8, ¾), matches
  pRW(q)π cot(πq) to 1·10⁻⁹, 1·10⁻⁶, 1·10⁻⁷ and 1·10⁻⁶.
- **Nonlinear terms, exactly.** For drums (p = 1, N = λ − β√λ), the root is quadratic in (1 + η)^{−1/2}, and
  D ⊃ −(πβ/(2√2))√n + (π²/16)β² exactly (SPEC §3.16).
- **What M1 does not give.**
  - The discreteness values Z(−j) of the actual node set. These enter through the band factor (M2), not the continuum.
    The continuum Z_N(−j) here are cutoff-dependent and are not the spectral ones.
  - The second-order layer (M4).

## 4. Checks (NUMERICAL)

`checks/m1_theoremQ.py`, `checks/m1_theoremQ.out`: 20 assertions on four densities, two of them not power laws.
- Power laws: p = 0.6 and 1.5 (a = 4c to 10⁻¹²).
- A drum: p = 1, N = λ − β√λ, cut at the first node.
- A log law: N(T) = (T/2π)log(T/2πe), λ = T², cut at T = 2πe^{1.5}.
For each density:
- (H2) holds on a grid;
- the explicit and balayage forms of ν agree to 10⁻²¹;
- 0 < ν/σ < 1 at five points;
- the total mass is 1 to 10⁻¹¹;
- Φ(z) = (z − a)H(z) > 0 at three points of (a, Y).

`checks/m1_edge.py`, `checks/m1_edge.out`: Proposition M1.2's pole term, from the first-order γ-part of the continuum root
over n = 100–6400, with the cross terms (n⁰, n^{−1}, n^{−1−pq}, n^{−pq−jp}, n^{−1−jp}) in the fit. Four cases, all within
2·10⁻³ relative (actually 10⁻⁹–10⁻⁶). The m = 1 cases are excluded, because there pq = 1 coincides with the n^{−1} cross term,
the continuum analogue of the d₂ merge.

## 5. Rule A

- *Is (G) consistent with Lemma Q's numerics in SPEC §3.14?* Yes. The balayage and explicit forms of ν agree to 10⁻²¹. The
  outer inequality is now proved, where §3.14 only had numerics.
- *Is (H2) needed?* It is used three times: monotonicity of F, ν < σ, and H > 0. A density with yσ increasing somewhere
  could, in principle, open a gap (a second band). Theorem Q is then silent.
- *The finite-Y case.* Drums and zeros are cut at the first node. The extra PV term in H is positive, so the cut helps.
  Beyond Y there is no condition, since μ = σ = 0 there.
- *Non-compactness.* The only non-elementary input is I(μ′ − μ) ≥ 0 for non-compactly supported zero-mass signed measures.
  This is standard under finite energy and the log-integrability in (H3), but it is NOT QUOTED.

## 6. Novelty (first pass)

- Constrained equilibrium problems for discrete orthogonal polynomials: Rakhmanov 1996, Dragnev–Saff 1997, Kuijlaars–
  Rakhmanov 1998. Their Riemann–Hilbert use: Baik–Kriecherbauer–McLaughlin–Miller (arXiv math/0310278).
- In the excerpts read, BKMM characterise the minimiser variationally, assume square-root behaviour at the edges, and state no
  general explicit formula. Explicit formulas exist for classical weights (Krawtchouk, Hahn).
- An explicit one-cut solution on a half-line with infinite constraint mass near 0, with the single sufficient condition "yσ
  decreasing", and with the factorisation (G): NOT FOUND (web-only search; MathSciNet/zbMATH unavailable). The ingredients
  are classical. The identification of (Q) with Law P's constant and with the per-node law of S2′ is this project's.
