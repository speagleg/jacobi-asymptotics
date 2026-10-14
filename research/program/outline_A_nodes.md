# Research program outline: Problem A — pointwise Law P for non-pure-power nodes

Scope: jacobi-asymptotics (read-only), THEOREMS.md §4 items 8 (nodes other than pure powers) and 9 (CL for general
nodes), with the true ζ-zero measure as the far horizon. Everything in this file is a PLAN. Labels on new statements
are *proposed* (GAP / conjecture / NUMERICAL); nothing here is proved. Numerical results below are NUMERICAL (long-double
RKPW via `jacobi_asym`, K vs 2K truncation checks) and were produced by the scripts in this directory
(`expA_*.py`, outputs `expA_*.out`).

---

## 0. Executive summary

1. **New structural finding (NUMERICAL + heuristic): the "local-exponent law".** For nodes x_k = f(k) = k^{−p}ℓ(k)
   with ℓ smoothly slowly varying, b_n/f(n) ≈ c(p_f(n)), where p_f(n) := −n f′(n)/f(n) is the *local exponent*. It
   reproduces RH_ζ's coefficient exactly: for the smooth-ζ model p_f(n) = 2 − 2/log n + …, so
   b_n/x_n = c(2)(1 − 2(log c)′(2)/log n + …), and (log c)′(2) = log(π/2) − (1 − log 2) = 0.14473, i.e.
   κ = −0.28946, which is RH_ζ's κ. Numerically (E1, E1b, E2) the prediction holds for ℓ = log^α (α = 1, −2; p = 1, 2),
   ℓ = exp(√log), ℓ = 2 + sin log log, with residuals that decay like a power of n. The node first-variation kernel also
   reproduces −2(log c)′(p) to O(1/n) (E2). This turns the qualitative Law P into a sharper, checkable target.
2. **Most tractable positive target:** a direct Riemann–Hilbert (RH) theorem for *analytic* regularly varying nodes
   (class 𝒜 below). It generalizes RH_px/seam and RH_ζ, which is itself such a node family. Estimated 3–5 plans,
   P ≈ 0.55. A power-decaying sub-case (T1′) takes 1–2 plans, P ≈ 0.75.
3. **Node transport (the proposed Lemma TV/Theorem L analogue) is well posed but ill-conditioned at the lattice
   scale.** The first variation in atom positions is exact and elementary (Lemma NFV). Constant log-dilations give
   exactly 2. Smoothed in log k, the kernel is O(1), n-independent and localized at k ∈ [n/4, 1.5n] (E2). For
   displacements that are rough at the lattice scale, it has per-atom size O(1) (total variation ~ n), so moving
   C¹-only nodes needs summation by parts and a bound on an integrated kernel U_j (Lemma NK). Numerically
   B_n := Σ_j |U_j|/j ≈ 1.55, 1.61, 1.67 at n = 50, 100, 200 (bounded or ~log n; E3b). B_n is dominated by the soft
   edge, where single-gap responses grow like n^{0.4}. **Lemma NK uniformly along a non-analytic path is the hardest
   missing step.** No self-improving inequality like Theorem L's Grönwall is available for it.
4. **Negative half (tractable):** sub-spacing rough node displacements of fixed relative size should break Law P
   (Theorem R_node). Numerically, lattice-rough displacements give O(0.1–0.4)·ε responses (E2), and parity-rough
   spacings oscillate at ~n^{−0.4} decay (E1). 1–2 plans, P ≈ 0.55.
5. **True ζ ordinates: a barrier, not a target.** Pointwise Law P for σ_ζ^{true} implies averaged Law P (G3′), which
   implies d(E) = 0 (Theorem N″): 100% of ordinates distinct. That is open, so stop condition 1 applies. Numerically the
   pointwise law looks true: |log(b_n^{true}/b_n^{smooth})| has mean 0.033 → 0.0115 for n from 50–100 to 800–1200,
   decaying ≈ n^{−0.4} (E4).
6. **Cheap rigorous wins:** (i) the Cesàro law (1/n)Σ log(b_j/f(j)) → log c(p) for (H-a) nodes via a Sat-type bound +
   G1-L, 1 plan, P ≈ 0.8; (ii) Lemma RL, a right-limit reduction (pointwise law ⇔ rescaled μ_n → arcsine), 0.5 plan,
   P ≈ 0.9, possibly known (Simon 2004).

---

## 1. Setting, notation, what is already known

- σ = Σ_k w_kδ_{x_k}, x_k = f(k) ↓ 0, Jacobi coefficients (a_n, b_n), orthonormal p_n, q_j := √w p_j(x_·),
  μ_m := q_m² (prob. vector), ρ_m := Σ_{j<m}μ_j, K_m := Σ_{j<m}q_jq_jᵀ, c(p) as in THEOREMS.
- **Law P(f, w):** b_n/f(n) → c(p) and a_n/(2b_n) → 1, where p is the regular-variation index of f. Under (H-a) with
  constant C this is n^pb_n → c(p)C.
- **Local exponent:** p_f(ξ) := −ξf′(ξ)/f(ξ). For f = ξ^{−p}ℓ, p_f = p − ε_ℓ with ε_ℓ := ξℓ′/ℓ → 0.
- Node classes, from strongest to weakest:
  - **𝒜 (analytic regularly varying).** λ(u) := log ℓ(e^u) extends analytically to a strip/sector large enough for the
    RH index function (see L-RH1), with symbol bounds |λ^{(j)}(u)| ≤ C_j ε(Re u)(Re u)^{1−j} (j ≥ 1), ε ↓ 0.
    Examples: (log ξ)^α, log log, exp(√log ξ) (with ε = 1/(2√u)), the smooth-ζ model (p = 2, ℓ ≈ (log ξ/2π)²).
    - Sub-class 𝒜₀: ℓ = C(1 + O(ξ^{−δ})) analytic. Examples: (k + a)^{−p}, (k² + a)^{−p/2}, the "integer-ordinate"
      model 1/(k² + ¼).
  - **ℋ¹ ((H-a), G2's hypothesis):** f ∈ C¹, ξ^{p+1}f′(ξ) → −pC. Equivalently g := log(f/(Cξ^{−p})) has g → 0 and
    ξg′ → 0. Regularly varying C¹ version: ℓ C¹ with ξℓ′/ℓ → 0.
  - **Rough:** x_k = k^{−p} + δ_k with |δ_k| ≤ ε·(spacing), sign pattern arbitrary.

**Known (reused):**
- Pure powers, all p > 0, s > 1, pointwise with O(1/n): RH_p (RH_px), RH₁(r), seam (RH_plt1b).
- Smooth-ζ model, pointwise with κ/log n: RH_ζ (RH_zeta, RH_zeta_close: E1–E3 finite-N edge equation, C–D
  log-weight hard edge, Lemma Z far field (Arb), uniform edges, rate).
- Averaged law: G2 H_all (ℋ¹ nodes, Σw < ∞, w ≥ c₁k^{−s}); item 11 Theorem H_L (slowly varying atoms L,
  hypotheses (L1)–(L3)); Lean `theoremHL`.
- Tauberian: G1-T (H_all + (T3) ⇒ pointwise), G1-L (H_all + one-sided bound ⇒ Cesàro).
- Weight transport (pure-power nodes): FV, FVa, TV, Sat_p⁺, TL/TLw, LP, Theorem L, T3-all, T3-log, Theorem R
  (R1, R2).

---

## 2. Target theorems, ranked from most to least tractable

### T0. Cesàro law for ℋ¹ nodes (rigorous, cheap)
*Statement.* Let f ∈ ℋ¹ (constant C), Σw < ∞, c₁k^{−s} ≤ w_k ≤ c₂k^{−s}. Then
sup_n n^pb_n < ∞ and (1/n)Σ_{j<n}log(j^pb_j) → log(c(p)C).
*Chain.* Lemma Sat(ℋ¹) (Sat_p⁺ for ℋ¹ nodes; its proof is Christoffel–Lagrange plus node spacing, which only needs
spacing bounds ≍ k^{−p−1}). Then T3a step 1 gives sup n^pb_n < ∞, and G1-L + H_all conclude.
Regularly varying version: H_L (item 11) replaces H_all.
*Proposed label:* PROVED-mod-cite (P) (through H_all).
*Effort:* 1 plan. *P:* 0.8.

### T0′. Lemma RL (right-limit reduction; rigorous, cheap, possibly known)
*Statement.* Suppose sup_n a_n/f(n) and sup_n b_n/f(n) are finite. Then Law P(f, w) holds iff, for every fixed j ∈ ℤ,
the image of μ_{n+j} under x ↦ x/f(n) converges weakly to the arcsine law on [0, 4c(p)].
*Proof sketch.*
- (⇒) is Lemma LP's moment argument.
- (⇐): take any subsequence along which all rescaled coefficients (a_{n+j}/f(n), b_{n+j}/f(n)) converge to (A_j, B_j);
  this gives a doubly infinite J_∞.
- Weak convergence plus uniformly bounded moments make the e_j-spectral measure of every J_∞ arcsine.
- 1st moments: A_j = 2c.
- 2nd moments: B_j² + B_{j+1}² = 2c² for all j, so B² alternates between β and 2c² − β.
- 4th central moments: (B_j² + B_{j+1}²)² + B_j²B_{j−1}² + B_{j+1}²B_{j+2}² = 6c⁴ forces β(2c² − β) = c⁴, so β = c².
  Hence J_∞ is free.

*Use.* It turns every route into "identify the local density of μ_n", gives a cheap numerical order parameter, and is
the natural interface to Christoffel/universality methods. *Effort:* ½ plan. *P:* 0.9. Check Simon (2004) first.

### T1′. Analytic power-decaying perturbations (class 𝒜₀), p > 1 first
*Statement.* For f ∈ 𝒜₀ and weights W(k) with W(ξ) = ξ^{−s}(analytic, 1 + O(ξ^{−δ})), s > 1:
n^pb_n = c(p)C(1 + O(n^{−δ′})) and a_n/(2b_n) = 1 + O(n^{−δ′}).
*Chain.* RH_px §§1–5 with the index function t_N(z) = N·f^{−1}(z/N^p)/N (RH_ζ's α-shift is the prototype). The
finite-N equilibrium is an O(N^{−δ}) perturbation of G2's μ*. Hard edge: KMVV as in RH_px §4.1, since the band factor
is bounded and Hölder. Far field: perturbative from the pure power (L-RH7a).
*Effort:* 1–2 plans. *P:* 0.75. *Value:* modest, but it is the testbed for T1.

### T1. Local-exponent Law P for analytic regularly varying nodes (class 𝒜), p > 1, then all p > 0
*Statement (target).* For f ∈ 𝒜 with index p > 1, weights W ∈ 𝒜 with index s > 1, and (A4) the far-field sign
condition (to be discharged by L-RH7):

  b_n = c(p_f(n))·f(n)·(1 + O(η(n))),  a_n/(2b_n) = 1 + O(η(n)),

where η(n) := ε(log n)²log(1/ε(log n)) + |λ″(log n)| + 1/n. This is the error form that RH_ζ attains:
ε ≍ 1/log n gives log log n/log²n.
- Corollary: Law P for every f ∈ 𝒜, including ℓ = exp(√log k). For weights, that is the analogue of THEOREMS §4 item 7,
  which is open (D(γ) = ∞).
- RH_ζ is the instance p = 2, ℓ ≈ (log/2π)², with κ = −2(log c)′(2).

*Effort:* p > 1 needs 2–3 plans after T1′; p = 1 and 0 < p < 1 (seam) need +2 plans. *P:* 0.55 for p > 1, 0.5 for all
p.

### T2. Theorem R_node (rough sub-spacing displacements break the pointwise law)
*Statement.* For all p > 0, s > 1 there is ε₀ > 0 such that for every ε ∈ (0, ε₀] there are nodes
x_k = k^{−p} + δ_k with |δ_k| ≤ ε·pk^{−p−1} (so x_k ~ k^{−p} and spacings in [1 − 2ε, 1 + 2ε]·pk^{−p−1}), weights
exactly k^{−s}, and limsup|log(β_n²/β_{n−1}²)| ≥ c₀ε (c₀ > 0 non-explicit). This mirrors Theorem R. Together with
T1/T3 it gives the node dichotomy: smooth spacings preserve Law P, fixed-size rough spacings can destroy it.
*Effort:* 1–2 plans. *P:* 0.55.

### T3. Law P for ℋ¹ (C¹) nodes, then C¹ regularly varying nodes
*Statement.* For f ∈ ℋ¹ and w = k^{−s}Ψ (Ψ bounded, slowly varying): n^pb_n → c(p)C and n^pa_n → 2c(p)C. Regularly
varying C¹ version: b_n/f(n) → c(p).
*Chain.* Route NT (§3.3) on top of T1. *Effort:* 4–8 plans after T1. *P:* 0.2.
A C^∞/symbol-class version through ∂̄-RH: 4–6 plans, P ≈ 0.3. The second-order local-exponent refinement for C¹ nodes
is out of reach: C¹ does not control ε_ℓ′.

### T4. True ζ ordinates (horizon; NOT a target)
Pointwise Law P for x_k = 1/(γ_k² + ¼) ⇒ G3′ (Cesàro, with x_j^{true}/x̃_j → 1 by Z1) ⇒ d(E) = 0 (Theorem N″).
That is "100% of ordinates distinct", open even on RH as far as the repo's reading goes. This is stop condition 1 in
the implication sense. Even conditionally, transport from the smooth model is a rough node perturbation:
kΔg_k equals the relative gap fluctuation, which is O(1). It would need statistical cancellation (smoothed sums of gap
fluctuations telescope to γ_k − γ̃_k = O(1) by Z1), which no current lemma can exploit. Record the barrier and the
E4 numerics; P(unconditional) < 0.02.

---

## 3. Lemma chains

### 3.1 Conjecture LE (local-exponent law) — the organizing statement

**Conjecture LE.** For f = ξ^{−p}ℓ with ℓ smoothly slowly varying (ε_ℓ → 0, ξε_ℓ′ = o(ε_ℓ)) and regular weights:
b_n/f(n) = c(p_f(n))(1 + o(ε_ℓ(n)) + O(1/n)), and a_n/(2b_n) → 1.

**Heuristic.** b_n depends only on nodes at index scale n (E2: the smoothed node kernel lives on k/n ∈ [1/4, 3/2]).
On that window f(k) = f(n)(k/n)^{−p_f(n)}(1 + O(ε′ log²M)). So locally the nodes are a pure power with exponent p_f(n)
and constant f(n)n^{p_f(n)}, and the pure-power law gives c(p_f(n))f(n).

**First-order check.** g_k = log(k/n) turns k^{−p} into n^{−ε}k^{−(p−ε)}, so d log b_n²/dε = −2(log c)′(p). The E2 kernel
gives −0.2506, −0.2704, −0.2802, −0.2849 at n = 50, 100, 200, 400 against −0.2895, with an O(1/n) defect that halves
per doubling.

**Where it would be proved.** L-RH3 below: the finite-N edge equation should give β̂_N = 4c(p_f(N))(1 + O(η)). It is
also a potential-theory computation that could be done on its own (E10).

### 3.2 Route RH (targets T1′, T1). Reused: RH_px §§1–5, RH_plt1b (seam), RH₁(r), RH_zeta E1–E3 and §4.1, RH_zeta_close §§1–5, G2 μ*/B*(i)–(ii)

- **L-RH1 (index function).** t_N(z) := f^{−1}(z/s_N)/f^{−1}(1/s_N)·N, normalized so t_N(X_k) = k at the rescaled
  nodes X_k := s_Nx_k, with s_N := 1/f(N). It is analytic and univalent on ℂ ∖ (−∞, 0], and |arg t_N| ≤ π − δ there
  (Stirling/Binet valid; Lemma 1.1 analogue). For p > 1 this needs λ analytic in |Im u| < π/p + δ′. For p ≤ 1 it
  needs the seam/angle-freedom construction of RH_plt1b instead.
- **L-RH2 (band weight).** W := 2iθ′w = (hard-edge factor z^{α_x})·Λ_N(z)·(bounded Hölder), with α_x = (s − 1 − p)/p
  and Λ_N analytic, slowly varying, built from ℓ, ℓ_w and t′. This is Lemma A1's analogue; RH_ζ has Λ = log(γ/2π).
- **L-RH3 (finite-N constrained equilibrium; the heart of LE).** For the N-dependent node density ρ_N (upper
  constraint): there is a band [0, β̂_N] with an edge equation as in RH_zeta E1–E3, β̂_N = 4c(p_f(N))(1 + O(η(N))),
  and the strict inequalities of Lemma 2.1(iii) and 2.2 (signs off the axis) hold uniformly in N.
  *Can be done first and alone; it predicts the LE constant without RH.*
- **L-RH4 (global parametrix).** D̃ = exp(−μ(t_N)) (Binet), the Binet-cut B as in RH_px §3, and the Szegő function of
  the band weight with slowly varying Λ_N. Normalization as in RH_px.
- **L-RH5 (hard edge 0).**
  - (a) Λ_N bounded, Hölder (class 𝒜₀): KMVV §6 left-endpoint Bessel, as in RH_px §4.1.
  - (b) Λ_N unbounded slowly varying: Conway–Deift comparison as in RH_zeta_close §1 (H1, LW1, UR, Theorem C,
    Proposition D), with |Λ_N| ≥ c·(scale) and uniform Hölder bounds for log k_N.
  - Risk: RH_zeta's Λ is exactly log; general λ needs the lip-mismatch bound LW1 in terms of ε(log N).
- **L-RH6 (soft edge).** Airy, uniform in N (WLXZ §6.1; RH_zeta_close §3) with the N-dependent edge β̂_N.
- **L-RH7 (far field / top end).**
  - (a) For 𝒜₀ and for small ε: perturbation from the pure power. The sign/winding is a continuous integer-valued
    quantity along ℓ_τ = ℓ^τ, τ ∈ [0, 1], so it suffices to show non-vanishing along the homotopy.
  - (b) For general 𝒜: a structural argument (monotonicity of arg) or per-instance Arb certification as in Lemma Z.
  - *This is T1's main risk.*
- **L-RH8 (small norm, extraction, rate).** RH_px §5 verbatim, and RH_zeta_close §4 (Lemma D1) for the
  slowly varying rate.
- **Theorem T1** = assembly. p = 1: RH₁(r)'s Bessel FH at 0. 0 < p < 1: seam.

### 3.3 Route NT (node transport; target T3, and the first-order part of LE)

- **Lemma NFV (node first variation; standard, Jacobi's formula / Hellmann–Feynman).** Let x_k(t) be C¹ in t with
  dominated derivatives (e.g. ẋ_k = x_kg_k, g bounded). Then:
  - d/dt log D_m = Σ_k w_kẋ_k ∂_xK_m(x, x)|_{x=x_k}. In Heine form it is 𝔼_m[Σ_{i∈S}ẋ_iΣ_{j∈S∖i}2/(x_i − x_j)].
  - d/dt log b_n² = Σ_k w_kẋ_k ∂_x(p_n² − p_{n−1}²)(x_k) =: ⟨g, D^{(n)}⟩, where D^{(n)}_k := w_kx_k∂_x(p_n² − p_{n−1}²)(x_k).
  - Exact scaling identity: Σ_k w_kx_k∂_x(p_m²)(x_k) = 2⟨xp_m′, p_m⟩ = 2m, so ⟨1, D^{(n)}⟩ = 2.

  *Proof:* d log det H = tr(H^{−1}dH), with dH_{ij} = Σ_k w_kẋ_k∂_x(x^{i+j})(x_k). (Checked numerically: constant g
  gives 2.000000; E2.)
- **Lemma NFVa.** The a_n analogue: d/dt a_n = Σ_k w_kẋ_k∂_x(x p_n²)(x_k) + (polynomial-variation terms). Derive as in
  FVa (Lemma H proof + Christoffel–Darboux). Needed for the a-law.
- **Lemma SBP (summation by parts; elementary).**
  d/dt log b_n² = 2g_n + Σ_j (jΔg_j)·(U_j/j), where U_j := Σ_{k>j}D_k for j ≥ n and U_j := −Σ_{k≤j}D_k for j < n.
  Equivalently, U_j = (response to dilating all atoms beyond j) − 2·1_{j<n}.
  *Hence for ℋ¹ deformations (sup|kΔg| small on the window) the error is ≤ sup_window|kΔg|·B_n,
  B_n := Σ_j|U_j|/j.*
- **Lemma Head-ν (saturated region; GAP, plausible).** sup_t Σ_{j<n/M}|U_j^{(t)}|/j ≤ C·M^{−ϑ}, uniformly along paths in
  a fixed ℋ¹-sandwich.
  - Idea: for i in the saturated head, 1 − ρ_m(i) is exponentially small (Sat). The multipole expansion
    2x_i/(x_i − x_j) = 2Σ_r(x_j/x_i)^r over j at scale n converts the head contribution into Σ_{i∈H}g_i·x_i^{−r}
    times second differences of the moments 𝔼_m[Σ_{j∈S}x_j^r]. Those are local in J, as in Lemma LP.
  - Numerically the smoothed head kernel decays like (k/n)^{≈3.4} (E2).
  - Unlike μ_n it is only *polynomially* small: saturated nodes pin zeros.
- **Lemma Tail-ν (hard-edge region; GAP, plausible).** sup_t Σ_{j>Mn}|U_j^{(t)}|/j ≤ ε(M).
  - Idea: for k ≫ n the node set is a continuum at scale n, so a smooth node motion is a weight change
    −[(α + 1)g + xg′] against μ_n − μ_{n−1}, whose tail is O(1/n) (LP + TL/TLw).
  - Numerically negligible beyond 2n (E2, E3).
- **Lemma NK (window kernel bound; THE HARDEST STEP).** sup_{t∈[0,1]} Σ_{n/M≤j≤Mn}|U_j^{(t)}|/j ≤ B, with B independent of
  n, t, M, for paths x(t) = f_ae^{tg} with f_a ∈ 𝒜 and |g| + |kΔg| ≤ δ₀.
  - At t = 0 it should follow from T1's RH solution: uniform asymptotics of p_n, p_n′ at the nodes in all regions,
    including the Airy window, extracted from Y. That costs 1–2 plans *beyond* T1, P ≈ 0.6.
  - For t > 0 it is open; §4 explains why.
- **Lemma MOL (analytic mollification; elementary, PROVED-level likely).** For f ∈ ℋ¹ there is f_a ∈ 𝒜₀ ∪ 𝒜 (Gaussian
  mollification of u ↦ log(e^{pu}f(e^u)) at width h) with g := log(f/f_a) satisfying g_k → 0 and kΔg_k → 0. The
  mollified λ_a is entire in u with the symbol bounds of 𝒜 (bounds ∝ h^{−j}sup|λ′| on |Im u| ≤ θ₀).
  - Caveat: T1 must then cover f_a whose ε(u) decays at an *unspecified* rate. So T1's proof must be uniform in ε, not
    tied to log-type.
- **Theorem NT-conv (node analogue of T3-conv).** If T1 holds for f_a, and NK, Head-ν and Tail-ν hold along
  f_ae^{tg}, then Law P holds for f.
  - Proof: integrate SBP over t ∈ [0, 1]. The window contributes ≤ B·sup_{k≥n/M}(|g_k| + |kΔg_k|) → 0; the head and
    tail contribute ≤ ‖g‖_∞(CM^{−ϑ} + ε(M)); then let M → ∞.
  - The a-law follows the same way through NFVa.
  - Since g_n → 0 and p_f − p_{f_a} → 0, the constant is c(p).
- **Theorem T3** = MOL + T1 (for f_a) + NT-conv, with weights handled afterwards by T3-all's weight transport. That
  requires Theorem L/LP to be re-proved for 𝒜 ∪ ℋ¹ nodes: LP for f_a comes from T1 by the same moment argument; Sat and
  TL hold for ℋ¹ spacings.

### 3.4 Route R_node (target T2). Reused: Theorem R's architecture, Sat_p⁺, TL, LP

- **R1-node.** For the pure power there are η, J: every [N − J, N] has m with ‖Δ_m D̃^{(m)}‖₁ ≥ η, where
  D̃^{(m)}_k := (pk^{−1})·D^{(m)}_k is the response per unit sub-spacing displacement.
  - Contradiction proof as in R1 (moments of μ_{N−1} + pure-power ratio asymptotics) has to be redone for the
    derivative kernel; alternatively take it from NK's RH extraction.
  - Numerically the rough-bump responses are 0.1–0.4 (E2), so non-degeneracy is very likely.
- **R2-node (second-order control).** |d²F_N/dt²| ≤ C·ε² along x_k + tδ_k with |δ_k| ≤ ε·spacing_k.
  - Heine form: d² log D_m = Var_m[Σ_{i∈S}δ_i∂_i log V] + 𝔼_m[Σ_{pairs}−2(δ_i − δ_j)²/(x_i − x_j)²]. Pair terms are
    O(ε²) per particle, since Σ_j(spacing/|x_i − x_j|)² < ∞.
  - The third difference in m needs a rank-one/projection argument like R2's (K_mq_m = 0). *This is the risk: for
    nodes the analogue of A ≤ 0 ≤ B is not obvious.* Fallback: a cruder bound O(ε²·polylog n) is enough if the
    windows are chosen sparser.
- **Cross-scale independence.** The node kernel's head is only polynomially small (Head-ν), so windows need
  super-polynomial separation. Lemma TL handles the tail.

### 3.5 Route W (weak limits / Christoffel; alternative for T3, via T0′)
By Lemma RL it suffices to show that μ_n rescaled converges to arcsine. Candidate inputs:
- bulk universality for varying measures (Lubinsky), which is robust to C⁰ density perturbations;
- Christoffel-function asymptotics (Totik), with the discrete saturated region handled by Sat.

Obstacle: universality controls K_n near the diagonal, not p_n² itself, and μ_n = ρ_{n+1} − ρ_n needs relative
precision o(1/n) in ρ (the "gain of n" problem of G1 §4). It is probably not sufficient alone. Read it for ideas, do not
plan on it.

---

## 4. The hardest missing step, and why

**For T3: Lemma NK along a non-analytic path.**
1. *Amplification.* Node motion is generated by g·x∂_x. On degree-n polynomials ‖x∂_x‖ ~ n, so lattice-rough
   displacements of relative size O(1/n) already move log b_n² by O(1). E2's rough row: 0.10–0.39 at n = 50…400, for
   displacements of one spacing-fraction. Any estimate has to sum by parts and so needs the integrated kernel U.
2. *Concentration at the soft edge.* U_j is large exactly where the saturated region meets the band
   (j/n ≈ (4c(p))^{−1/p} = 0.637 for p = 2). There max_j|U_j| = 4.0, 5.5, 7.3 at n = 50, 100, 200 (~n^{0.4}), and the
   window [0.6n, 0.7n] carries Σ|U_j|/j = 0.45, 0.49, 0.53 (E3b). Whether B_n stays bounded or grows like log n is
   numerically undecided (increments 0.063, 0.056 per doubling). A log n growth would force sup|kΔg| = o(1/log n),
   which is *not* implied by ℋ¹.
3. *No closure.*
   - Theorem L closed because Lemma TV's non-local term is a projection (‖K_m‖ ≤ 1, K_mq_m = 0), giving
     ẏ ≤ 4Gy + 2ε√y.
   - The time derivative of U^{(t)} instead contains three-point terms with p_n″ and the same O(n) amplification. To
     bound it one has to sum by parts again, and that produces a new kernel. There is no finite hierarchy in sight.
   - RH, which gives NK at analytic points, is unavailable along C¹ paths unless one develops a discrete ∂̄-RH, which
     is a research project in itself.
4. *What would break the impasse:* either (a) an a-priori ("soft") proof that B_n ≤ B for every node set in an
   ℋ¹-neighbourhood of 𝒜 (e.g. via a variational/Heine characterisation of U_j as a cross-field functional, with the
   soft-edge window handled by an Airy-scale comparison), or (b) a ∂̄ extension that runs the whole RH analysis
   for C^{2+}-symbol nodes. Either would give T3 for that regularity class.

**For T1: L-RH7 (far field for a class) and L-RH5(b) (unbounded slowly varying hard-edge factor).** Both have
working templates (Lemma Z certified; C–D comparison), but RH_ζ needed an Arb certificate for *one* model. A class
statement needs a homotopy/perturbation argument. L-RH3's uniform strict inequalities are routine but long.

---

## 5. Candidate methods

| Method | Pros | Cons | Verdict |
|---|---|---|---|
| **M1 Direct RH for analytic f (class 𝒜)** | Templates exist (RH_px, seam, RH₁(r), RH_ζ, which is already a non-pure-power node family). Gives rates and the LE constant. Pointwise asymptotics of p_n come for free (feeds NK at t = 0, R1-node, LP). | Needs analyticity of f and w in a sector. Far-field winding for a class is not routine. p ≤ 1 needs the seam again. Long and citation-heavy (WLXZ, KMVV, C–D). | **Primary route** (T1′ → T1) |
| **M2 Node transport (NFV + SBP + NK + Head/Tail-ν)** | Exact first-variation formula and scaling identity. The smoothed kernel is O(1), n-independent and localized (E2), and reproduces −2(log c)′(p). It is the only route to C¹ nodes and mirrors the successful weight program. | Lattice-scale ill-conditioning (TV ~ n). The soft-edge concentration of U. No Grönwall closure. The head kernel is only polynomially small. | Use for first-order statements (LE heuristics, R_node, decaying perturbations of analytic nodes *if* NK can be proved). Not the primary route. |
| **M3 ∂̄-steepest descent (McLaughlin–Miller)** | Handles non-analytic weights with finite smoothness, so it could cover C^{2+} nodes directly, with rates. | No discrete-OP ∂̄ theory in the literature read. The interpolation step uses sin(πt(z)) with analytic t. Needs C² at least, not C¹. | Second-phase option for T3 at C^{2+} |
| **M4 Comparison / interlacing** (Heine pair-ratio comparisons, Christoffel monotonicity λ_n(μ) ≤ λ_n(ν) for μ ≤ ν, Markov–Stieltjes) | Robust, elementary. Gives one-sided bounds (feeds G1-L, giving T0) and the averaged law (H5/H6 → H_L). | b_n is not monotone in nodes or weights. Pair-ratio comparisons control log D_n only to o(n²), and pointwise b_n needs O(1) precision in Δ² log D_n (G1 §4 point 1). | Only for T0 / a-priori bounds |
| **M5 Right limits / weak limits (Lemma RL) + universality** | Clean equivalence. A cheap numerical diagnostic. Connects to OPRL literature (Simon, Last–Simon, Lubinsky). | Identifying the weak limit of μ_n is as hard as the law (gain-of-n problem). | Reduction lemma only |
| **M6 Tauberian (G1-T)** | H_all is already known for ℋ¹ nodes, so only (T3) slow oscillation is needed. | (T3) needs the same local-regularity input as the law itself. | Bookkeeping only |

---

## 6. Literature to read (all recollections; verify per the citation gate)

1. **Baik–Kriecherbauer–McLaughlin–Miller, *Discrete Orthogonal Polynomials* (Ann. Math. Stud. 164, 2007).**
   - Their node model is quantiles of an analytic density ρ⁰ on a finite interval.
   - Look for: exact analyticity hypotheses on ρ⁰ and the weight; how saturated regions and band/saturated transitions
     are handled; whether nodes from a *non-analytic* density or an accumulation point are discussed; the uniform
     asymptotics of p_n at nodes (needed for NK at t = 0).
2. **WLXZ (arXiv:1410.3948), KMVV §6, Conway–Deift (arXiv:1711.01590).** Already in the citations. Re-read for uniformity
   in parameters (p, s, and the slowly varying factor), since T1's proof must be uniform over ε.
3. **McLaughlin–Miller, ∂̄ steepest descent** (IMRP 2006 for OPUC; IMRN 2008 for OPRL with varying weights).
   - Look for: the minimal smoothness (C², W^{2,∞}?) and the error rates; whether the method survives an
     interpolation problem with non-analytic t(z) (discrete OPs).
4. **Lubinsky–Mhaskar–Saff, "A proof of Freud's conjecture for exponential weights" (Constr. Approx. 1988)**, the
   **Levin–Lubinsky monograph *Orthogonal Polynomials for Exponential Weights* (2001)**, and
   **Knopfmacher–Lubinsky–Nevai (1988), counterexamples.**
   - This is the closest classical analogue: a pointwise law (b_n/a_n^{MRS} → ½) proved from regularity of Q, and false
     without it (cf. Theorem R/R_node).
   - Look for: what smoothness of Q is used and where (Freud's identity n/b_n = ⟨p_n′, p_{n−1}⟩, the analogue of our
     scaling identity); infinite–finite range inequalities; whether the proof transports regularity or uses it once.
5. **Simon, "Ratio asymptotics and weak asymptotic measures for OPRL" (J. Approx. Theory 126, 2004)**, and **Last–Simon
   on right limits.**
   - Look for: whether Lemma RL (weak limits of p_n²dμ ⇔ coefficient limits) is already there; the varying-measure
     versions.
6. **Rakhmanov (1996), Dragnev–Saff (1997), Kuijlaars–Rakhmanov (1998), Kuijlaars–Van Assche (J. Approx. Theory
   1999, varying recurrence coefficients).**
   - Look for: constrained equilibrium with N-dependent constraints (L-RH3), and the converse direction (regularly
     varying coefficients ⇒ zero distribution) as a consistency check of LE.
7. **Bingham–Goldie–Teugels, *Regular Variation* (§1.8 smooth variation; de Haan second-order theory).**
   - Look for: the Smooth Variation Theorem (for MOL); second-order regular variation for the o(ε_ℓ) remainder in LE.
8. **Ismail, *Classical and Quantum OPs in One Variable* (Hellmann–Feynman for zeros, parameter derivatives).**
   - Look for: prior statements of NFV (to cite instead of claiming).
9. **Lubinsky, bulk universality for varying measures; Totik on Christoffel functions.** For route W only: what local
   hypotheses suffice, and whether any gives μ_n (not just K_n) asymptotics.
10. **True ζ (T4 only).** Selberg's CLT for S(t), Fujii's moments (already C5), and the GUE gap statistics literature,
    to model the E4 fluctuations. No theorem planned.

---

## 7. Numerical experiments

### Done (this outline; all NUMERICAL, long double, p = 2, s = 2 unless stated; K vs 2K agree to ≤ 2·10⁻⁴ for n ≤ 800)

**E1 `expA_law.py` → `expA_law_*.out`.** R_n := b_n/(c(2)f(n)), w_k = k^{−2}, n = 50…1600.
- **Smooth families converge** (with the leading term predicted by LE):
  - ℓ = 2 + sin log log: R_800 = 0.9997;
  - ℋ¹ f = k^{−2}(1 + 1/log k): 0.9991;
  - ℓ = log k: 0.977 (slow, ~κ/log n);
  - ℓ = log^{−2}: 1.033 (from above).
  - |log(R_n/R_{n−1})| ≤ 7·10⁻⁶ at n = 800.
  - A_n = a_n/(2b_n) → 1 in all of them.
- **Parity-rough spacings** (Δx_k = 2k^{−3}(1 ± ε)):
  - R_n and A_n oscillate with period 2;
  - the jump |log(R_n/R_{n−1})| decays slowly: ε = 0.3 gives 0.069 → 0.019; ε = 0.6 gives 0.11 → 0.018
    (n = 50…1600, ≈ n^{−0.4});
  - like the parity-weight numerics of G1 §3.2 [4]. Periodic roughness averages out; adversarial roughness should not
    (T2).

**E1′ `expA_ploc.py`.** The LE prediction c(p_f(n))/c(2)·(1 − 1/(2n)) against E1:
- ℓ = log: obs − pred = −0.029, −0.013, −0.0056, −0.0019, −0.0002 (n = 50…800), while pred − 1 = −0.023 at n = 800;
- ℓ = log^{−2}: residual −0.0066 at n = 800 against pred − 1 = +0.040, decaying ~n^{−0.7};
- sinll and ℋ¹ residuals ≈ −2/n. These are 1/n normalization terms (f(n) vs f(n + a)).

**E1b `expA_le2.py` → `expA_le2.out`.** (R/R_pure)/pred, which removes the pure-power 1/n terms:
- p = 1, ℓ = log: 1.0121 → 1.0034 (n = 25…400; K-sensitive at 10⁻³), while the raw deviation is 5–9%;
- p = 2, ℓ = exp(√log): 1.0056 → 1.0015 (n = 50…800), while the raw deviation is ~3%.
- So LE holds beyond log-type ℓ, where the weight analogue of THEOREMS §4 item 7 is open.

**E2 `expA_kernel.py` → `expA_kernel_*.out`.** Node-transport response R(λ) = d log b_n²/dε for Gaussian bumps in log k
(width 0.25) centred at k = λn:
- Scaling identity: exactly 2.000000.
- Shape is n-independent (n = 50…400): peak +2.90 at λ = 0.71, −0.45 at λ = 0.35, ≤ 10⁻³ beyond λ = 2, head decay
  ~λ^{3.4}. Σ|R|·norm ≈ 2.65, so the smoothed TV is O(1).
- The first moment against log λ → −0.2895 = −2(log c)′(2) at rate O(1/n).
- Rough bumps (±1 spacing-fraction, alternating) give 0.10–0.39, not decaying in n, so the lattice-scale sensitivity is
  O(1).

**E3 `expA_step.py`, E3b `expA_stepfine.py` → outputs.** Integrated kernel U_j (step dilations) for every j ∈ [n/4, 3n]:
- B_n = Σ|U_j|/j = 1.549, 1.612, 1.668 (n = 50, 100, 200);
- the share from j/n ∈ [0.6, 1.0) is 1.16, 1.21, 1.25;
- max|U_j| = 4.0, 5.5, 7.3 at j/n ≈ 0.64, the soft edge (4c)^{−1/2} = 0.637.
- Head ([n/4, n/2)) ≈ 0.09 and tail ([1.5n, 3n]) ≈ 0.06, both stable.

**E4 `expA_zeta.py` → `expA_zeta.out`.** True ζ (Odlyzko, M = 10⁵ and 2·10⁵ identical, + smooth tail) vs the smooth model,
n ≤ 1200:
- Mean R agrees to 4 digits per dyadic block.
- |log(R^{true}/R^{smooth})| has mean 0.033, 0.025, 0.018, 0.0146, 0.0115 and max 0.097 → 0.036.
- The jump |log(R_n/R_{n−1})| has max 0.128 → 0.048.
- A_n^{true} ∈ [0.945, 1.10] → [0.974, 1.037].
- Consistent with a pointwise law with ≈ n^{−0.4} fluctuations. This is not evidence about the zeros (AGENTS rule 3).

### Proposed (de-risking, in priority order)

- **E5 (NK class-uniformity; decides T3's viability).** B_n for f_ae^{g} with (i) smooth random g with
  |g| + |kΔg| ≤ δ, (ii) ℋ¹-but-not-C² g (e.g. kΔg = δ·sign-blocks of length √k), (iii) n up to 800 with a
  K-check. Fit B_n against log n. If B_n grows under (ii) faster than under the pure power, abandon T3 at C¹ and target
  C^{2+} via M3.
- **E10 (L-RH3 standalone).** Solve the finite-N constrained equilibrium edge equation for ℓ = log^α, exp(√log),
  p ∈ {0.5, 1, 2, 3}, and compare β̂_N/(4f(N)·s-scaling) with c(p_f(N)). That confirms LE's mechanism before any RH
  work.
- **E6 (T2 viability).** Adversarial sub-spacing displacements δ_k = ε·spacing·sign(D̃-pattern) on windows
  [θN_i, CN_i], with N_i ×4 apart (as in G1 §3.2 [3]). Expect non-decaying spikes ≈ c₀ε. Also measure the second-order
  remainder (supports R2-node).
- **E7 (LE error form).** Residual (R/R_pure)/pred − 1 against ε², λ″ and 1/n for p ∈ {0.5, 1.5, 3}, ℓ ∈ {log^α,
  exp(√log), 2 + sin log log}. It fixes η(n) in T1's statement.
- **E8 (Lemma RL diagnostic).** KS distance of rescaled μ_n to arcsine[0, 4c] for the E1/E4 families; a cheap order
  parameter.
- **E9 (ζ).** Push E4 to n ≈ 5000 (M = 2·10⁶). Compare with synthetic nodes (smooth model + i.i.d. or GUE-like
  gap noise; + synthetic merges via `merge_repeats`) to separate gap-fluctuation from near-pair effects.

---

## 8. Effort and probability (plans of the repo's size: one theorem + Rule A + Rule R)

| Item | Plans | P(success) | Depends on |
|---|---|---|---|
| T0 Cesàro law for ℋ¹ (+ regularly varying via H_L) | 1 | 0.8 | Sat(ℋ¹), G1-L, H_all / H_L |
| T0′ Lemma RL | 0.5 | 0.9 (may be known) | LP method |
| E10 + LE note (heuristic + numerics) | 1 | 0.9 | — |
| T1′ (𝒜₀, p > 1) | 1–2 | 0.75 | RH_px, RH_ζ shift |
| L-RH3 (finite-N equilibrium, LE constant), rigorous | 1 | 0.7 | RH_zeta E1–E3, G2 |
| T1 (𝒜, p > 1) | +2–3 after T1′ | 0.55 | L-RH1–8; main risks L-RH7, L-RH5(b) |
| T1 for p = 1 and 0 < p < 1 | +2 | 0.5 | RH₁(r), seam |
| T2 Theorem R_node | 1–2 | 0.55 | R1-node, R2-node, Sat, TL |
| NK at t = 0 (RH extraction of p_n, p_n′ at the nodes) | 1–2 after T1 | 0.6 | T1 / RH_px |
| T3 (ℋ¹ nodes) | 4–8 after T1 | 0.2 | NK along paths (open), Head/Tail-ν, MOL, NFVa |
| T3 at C^{2+} via ∂̄ | 4–6 | 0.3 | new discrete ∂̄ theory |
| T4 (true ζ) | — | < 0.02 | implies d(E) = 0 (open) |

**Suggested order:**
1. E10 + E5 (numerics, ~½ plan);
2. T0′ and T0 (quick rigorous wins);
3. L-RH3;
4. T1′;
5. T2 in parallel;
6. T1;
7. reassess T3 using E5. If B_n is not class-uniform, stop T3 and record it in G1 LOG as a GAP with the E3/E5 evidence.

---

## 9. Publishable partial results along the way

1. **"Local-exponent law" note.** Conjecture LE, its derivation from the scaling/first-variation identity, the exact
   explanation of RH_ζ's κ = −2(log c)′(2), and E1/E1b/E2/E10 numerics. Short and self-contained. It should be checked
   against de Haan/Freud-type literature for novelty (Rule L).
2. **Theorem T1′/T1.** "Pointwise asymptotics of Jacobi coefficients for discrete measures with regularly varying nodes
   accumulating at a hard edge". A real paper; RH_ζ becomes a corollary.
3. **Node dichotomy.** T1/T3 (smooth spacings ⇒ Law P) together with Theorem R_node (fixed-size rough spacings can break
   it), paralleling the weight dichotomy T3-all/Theorem R. Publishable together with the existing weight results.
4. **Lemma NFV + SBP + kernel numerics** (localization, soft-edge concentration, n^{0.4} single-gap growth), as a
   technical section or a note on "Hellmann–Feynman for discrete OPs with moving nodes".
5. **T0/T0′** as lemmas inside items 2–3, not separately.
6. **ζ numerics (E4/E9)** only as a remark, framed per AGENTS rule 3 (ordinates as real inputs; no RH claims).
