# Plan 14: close the smooth-ζ pointwise Law P (hard edge, far field, uniform Airy, rate)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans (native). Steps use checkbox syntax.
> Multi-session research plan with gates, like Plans 10–13.

**Goal.** Promote the §4 theorem of `research/G1/RH/zeta/RH_zeta.md` from PROOF SKETCH to PROVED-mod-cite:
for σ_ζ (atoms x_j = 1/(γ_j² + ¼), N₀(γ_j) = j − ½, weights 2x_j),
- (Z1) b_N = (β_N/4)(1 + O(1/N)) [fallback: (1 + O(1/log² N)), which still gives the rate below];
- (Z2) a_N/(2b_N) = 1 + O(1/N) [same fallback];
- (Z3) b_n/x_n = (π²/16)(1 + κ/log n + o(1/log n)), κ = −2(log(π/2) − (1 − log 2)).

The weakest acceptable closure is b_n/x_n → π²/16 with an O(1/log n) rate, proved.

**Context: the four closure items** (this plan does item 1; the others get their own plans).
1. **Smooth-ζ (this plan):** three open lemmas plus the E5 rate.
2. **0 < p < 1 pure powers (Plan 15):** Γ's poles enter the slit plane on the rays arg z = ±pπ (RH_px Lemma 1.1), and
   the Binet-cut scalar B stops being integrable at 0. This needs a sector decomposition with seams that reach the hard
   edge.
3. **G3′ unconditional lower bound (Plan 16):** Prop N proves that counting information is insufficient. Closure means
   turning the conditional result into an equivalence (prove GAP N′: (SG)-type input is necessary), because an
   unconditional proof would be a new theorem about the multiplicities of ζ's zeros.
4. **General (T3)/(CL) (Plan 17):** either a positive theorem for an explicit analytic class, via RH_p plus
   perturbation, or a counterexample within sandwiched weights. check_regularity shows that parity weights still obey
   the law.

**Spec.** RH_zeta.md §4 and §5; review/REVIEW_RHzeta.md (F1, the major finding); RH_px.md §§3–5; CITATIONS.md.

## Global Constraints
- AGENTS.md: no RH framing; Rule C (cite only what was read, with verbatim quotes in CITATIONS.md); Rule N; "certified"
  only with Arb (python-flint in .venv); Rule R before any PROVED/REVIEWED label.
- Commit prefix `G1:`. Branch `plan-14-zeta-closure`. Files under `research/G1/RH/zeta/` (new: `RH_zeta_close.md`,
  `checks/check_z_lw*.py`, `checks/check_z_cmp*.py`, `checks/check_z_Zcert.py`).
- `.venv` only; no pip installs.

## Review Focus
1. **The comparison measure is a real positive measure.** C–D Thm 4.5's proof uses positivity (a moment matrix). Our
   analog must use the Gram matrix of a genuine discrete measure, with every transformation unwound.
2. **L² bookkeeping near the hard edge.** α = −½ gives |ζ|^{−1/4} singularities. Check that every L² claim is
   integrable, especially on (−δ, 0) and the lips.
3. **Uniformity in N.** Λ = log(γ/2π) ≍ log N on the hard-edge disc. Every O(·) must be uniform in N. The disc
   radius is fixed in z-units.
4. **Far-field certification.** The winding computation must be N-independent: a scaling limit plus a uniform error,
   not a finite list of N.
5. **Gauge and index conventions** (t_c = 3/8; N vs N ± 1) in the extraction, against check_z_edge2.

---

### Phase A: the log-weight hard edge (Rule R F1)

**Strategy (Conway–Deift, SIGMA 14 (2018) 056 = C–D).**
- Do **not** build a local parametrix for the log weight. Instead compare the transformed problem Q (lenses opened,
  closing on (−δ, 0)) with the problem Q̃ of a comparison measure σ̃ whose hard-edge weight has no log.
- Their jumps differ only by G²/g-type factors times φ^{−2N}.
- Resolvent identity (C–D Thm 4.4), uniform invertibility of 1 − C_ṽ (C–D Thm 4.5, Prop 4.6, via positivity), and
  then a Neumann series (C–D Thm 4.7). The leading difference comes from a C–D Prop 5.1/5.5-type L² estimate.

- [ ] **A0 (Rule C).** Read C–D §§2–5 and Apps A–C (arXiv 1711.01590v4). Put verbatim quotes in CITATIONS.md: Thms 4.4,
  4.5 (and the structure of its proof), 4.7; Props 2.4, 4.6, 5.1, 5.5, A.1. Record what is general (Thm 4.4, Prop 4.6)
  and what is Legendre-specific (Thm 4.5).
- [ ] **A1 (local structure of w₀ at 0).** Write the band weight as w₀(z) = z^{−1/2}·Λ(z)·k_N(z), with Λ = log(γ/2π).
  Prove that k_N is analytic and nonvanishing on a fixed disc around 0 minus (−δ, 0], Hölder up to the cut, and that
  its jump on (−δ, 0) is exactly the pure-power one. So the log is the *only* non-RH_px feature. Numerically:
  `checks/check_z_lw0.py` (k_N on |z| = 10^{−k}, uniform in N = 10² … 10⁶).
- [ ] **A2 (Lemma LW1, the C–D Prop 2.4/A.1 analog).** For g := Λ/Λ(1) on the band, with G its Szegő function on
  [0, β̂], prove uniformly in N:
  - G²/g − 1 = ∓iπ/(2Λ) + O(Λ^{−2}) on the lips in the disc;
  - G²/g₊ + G²/g₋ − 2 = O(Λ^{−2}) on (−δ, 0).
  Since Λ ≥ log N − log log N − C there, both are O(1/log N) and O(1/log² N) in sup norm. Numerically:
  `checks/check_z_lw1.py`.
- [ ] **A3 (comparison measure).** σ̃ := Σ_j (2x_j/Λ(x_j)) δ_{x_j} (same nodes; the log removed from the masses).
  - Show that its RH analysis is RH_zeta §4 with h Hölder at 0, i.e. the RH_px §4.1 hard edge applies verbatim
    (A1 with Λ ≡ 1).
  - Numerically: `checks/check_z_cmp.py` computes b_N(σ̃) against its own β̃_N/4, expecting O(1/N), and also
    b_N(σ_ζ)/b_N(σ̃) against the edge-equation ratio.
- [ ] **A4 (Theorem C, uniform invertibility for σ̃; the C–D Thm 4.5 analog).** Show that the inhomogeneous RHP
  m₊ = m₋ṽ + f on Σ is uniquely solvable with ‖m±‖_{L²} ≤ c‖f‖_{L²}, c independent of N. The proof unwinds the
  transformations to a discrete orthogonality problem for σ̃ and uses positivity of its Gram matrix (cf. the moment
  matrix in C–D's proof), plus |φ₊| = 1 on the band and the exponential decay on Σ^△ and the saturated lips.
  - **GATE A4.** If positivity does not close the estimate in the discrete setting, record the obstruction precisely
    and fall back to A4′.
- [ ] **A4′ (fallback).** Small-norm in a weighted L² space adapted to the |ζ|^{−1/4} singularity. Target:
  b_N(σ_ζ) = b_N(σ̃)(1 + O(1/log² N)), using the first-order lip cancellation from A2.
- [ ] **A5 (Theorem C plus Neumann series ⇒ the hard edge).** Via Thm 4.4 plus a Prop 5.1-type bound:
  - ‖μ̃(v − ṽ)‖_{L²} = O(N^{−1/2} log^{−2} N), so Q₁ − Q̃₁ = O(1/(N log² N));
  - hence b_N(σ_ζ)/(β_N/4) = 1 + O(1/N), after accounting for β_N vs β̃_N (both from E1, the same nodes);
  - numerics against check_z_cmp.

### Phase B: Lemma Z (far field), certified
- [ ] **B1.** Prove log(F_out/F_in) on C (C fixed in x-units) = Φ₀(ζ) + O(1/log N) uniformly, where Φ₀ is an explicit
  N-independent function from the scaling limit (t ~ (γ/2π)log γ; X_e ≍ N²/log² N).
- [ ] **B2.** `checks/check_z_Zcert.py` (Arb): certify the winding of exp Φ₀ on C to be 0, and certify
  inf_C|·| > 0 and continuity at both crossings. Then the uniform O(1/log N) error closes Lemma Z for N ≥ N₀ with N₀
  explicit.
- [ ] **B3.** Ξ bound: Ξ(z) = Ξ(0)(1 + O(log^k N/N²)) near the band (RH_zeta §4.2, now proved).

### Phase C: uniform Airy with α_W = 5/8
- [ ] **C1.** Write the WLXZ §6.1 construction with general α (quote (5.7) and §6.1 for general α in CITATIONS) and the
  uniform conformal-map lemma: φ̃ = −κ̃_N(z − β̂)^{3/2}(1 + O(z − β̂)), with κ̃_N → κ̃_∞ > 0 at rate 1/log N and
  uniform disc radius.

### Phase D: (Z3) the rate, rigorously
- [ ] **D1.** Uniform regular-variation lemma for E3: β_N/(4x_N) = c(2)(1 + κ/log N + O(log log N/log² N)). Write the
  proof with explicit expansions of x(t) (Lambert W) and an Arb check of the constant κ.

### Phase E: assembly and review
- [ ] **E1.** Theorem RH_ζ in RH_zeta_close.md, with the label chain; update the RH_zeta.md status line, PROOF.md, README
  and LOG.
- [ ] **E2.** Rule R (opus, fresh context), apply the fixes, re-check, then label.
