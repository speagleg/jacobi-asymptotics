# Plan 13: pointwise Law P for the smooth-ζ model, via a finite-N equilibrium and the RH_p machinery

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native). Steps use checkbox syntax. This
> is a multi-session research plan with gates, like Plans 10–12.

**Goal.** For the smooth-ζ model σ_ζ, prove:
- (Z1) b_N = (β_N/4)(1 + O(1/N)), where β_N is the band edge of the finite-N constrained equilibrium, given by the
  **edge equation**

    ∫_{β}^{∞} √(x/(x − β)) ρ_N(x) dx = 1,  ρ_N := |t′|/N;

- (Z2) a_N/(2b_N) = 1 + O(1/N);
- (Z3) β_N/(4x_N) = c(2)(1 + κ/log N + O(log^{−2}N)) with κ explicit.

Here σ_ζ is the toolkit `smooth_zeta`: atoms x_j = 1/(γ_j² + ¼), γ_j = N₀^{−1}(j − ½), weights 2x_j. This is the measure
of Lean Corollary H_L-ζ.

Together these give the **pointwise Law P with rate for the smooth-ζ model**: b_n/x_n = π²/16 + O(1/log n).

**Baseline** (NUMERICAL, `research/G1/RH/zeta/checks/`):
- check_z_phase0.out: b_n/x_n − c(2) ≈ −0.226/log n, and a_n/(2b_n) − 1 ≈ 0.7/n–0.84/n (n ≤ 3200, stable under
  J-halving).
- check_z_edge.out:
  - the edge equation reproduces 4c(p) exactly for pure powers (p = 1.5, 2, 3; 11 digits);
  - for σ_ζ, b_N/(β_N/4) − 1 = −1.09/N … −1.41/N (N = 50…3200).
  - So the slow 1/log term is entirely the finite-N equilibrium, and the remainder is O(1/N) up to a slowly drifting
    constant.

**Spec.** §7 G1; G1 PROOF.md §4; RH_px.md (the p > 1 machinery); G2 PROOF.md B* (the structure being generalized);
lean/README (Corollary H_L-ζ).

## Global Constraints

- AGENTS.md rules: no RH framing (the ordinates are model numbers, smooth N₀ only); Rule C; Rule N; Rule R before
  PROVED.
- Commit prefix `G1:`. Branch `plan-13-smooth-zeta`. Directory `research/G1/RH/zeta/` (RH_zeta.md, checks/,
  review/).
- .venv only; no pip installs.

## Review Focus

1. **Finite-N equilibrium.** Do the variational relations and the strict inequalities hold for a general decreasing
   density with √x ρ decreasing? The edge equation (Abel inversion) and its uniqueness and existence for σ_ζ.
2. **Index function topology.** t(x) = N₀(γ(x)) + ½ tends to 11/8 (not 0) at x = 4 and branches there. The far-end
   bookkeeping (μ* mass beyond the top node, the monodromy of F) must close, as B did in RH_px.
3. **Uniformity in N.** Rescaled data converge to the p = 2 model only at rate 1/log N. Every local construction
   (conformal maps, the Airy and Bessel parametrices, Lemma 3.4-type Hölder bounds) must hold uniformly.
4. **Extraction.** The global parametrix gives β_N/4 exactly; check the index convention (N vs N ± 1) against
   check_z_edge.
5. **(Z3) asymptotics.** The κ/log N term from the edge equation, versus Phase 0's −0.226/log n.

---

### Phase 0: baseline — DONE (numerics above).

### Phase 1: finite-N constrained equilibrium (generalizing G2 B*)
- [ ] Lemma E1. Let ρ be a density on (0, ∞) with √x ρ strictly decreasing, and A(u) := ∫_u^∞ √x ρ(x)(x − u)^{−1/2}dx.
  Let β solve A(β) = 1 (the edge equation). Put m := −A′ ≥ 0 on [β, ∞), τ(u) := ∫_u^∞ m, and
  μ := ∫ ω_{[0,β(τ)]}dτ. Then:
  - (i) μ = ρ on [β, ∞), and μ < ρ strictly on (0, β);
  - (ii) U^μ = const = ∫ log(β(τ)/4)dτ on [0, β];
  - (iii) Re g′ > 0 on (β, ∞), so U^μ > const there.
  - Proof: Abel inversion, plus the B* argument. Optimality is optional (not needed for RH).
- [ ] Apply to ρ_N of σ_ζ: verify √x ρ_N is decreasing on (0, 4). Existence and uniqueness of β_N. Asymptotics of β_N,
  i.e. (Z3) with κ.
- [ ] Check: the edge solution vs check_z_edge; the predicted κ vs −0.226.
- [ ] **Gate 1.**

### Phase 2: RH in x for σ_ζ (RH_px template)
- [ ] Rescale by x ↦ x/s_N (band edge → fixed). Index t_N, θ, Π, weights, the R and T transformations.
- [ ] g from Lemma E1. The far end: t → 11/8 at x = 4, and the branch at x = 4. Define D, B and K and do the monodromy
  bookkeeping (the RH_px Lemma 3.3 analogue). Global parametrix (Jacobi-type with an N-dependent Szegő function).
- [ ] Check: an end-to-end probe (check_px_e2e pattern) for σ_ζ: V N^{−1} − I = O(1/N).
- [ ] **Gate 2.**

### Phase 3: local parametrices, uniform in N
- [ ] Hard edge 0 (the KMVV left endpoint, as RH_px §4.1). Soft edge β (Airy). Top end. Uniformity lemmas.
- [ ] **Gate 3.**

### Phase 4: small norm, extraction, (Z1)–(Z3)
- [ ] b_N = (β_N/4)(1 + O(1/N)) and a_N/(2b_N) = 1 + O(1/N). Combine with (Z3).

### Phase 5: Rule R (opus), fixes, re-check; update G1 PROOF.md, README, spec, memory.
