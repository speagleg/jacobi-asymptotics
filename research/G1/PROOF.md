# G1: the pointwise Law P — reductions and status

Status: REVIEWED 2026-10-13 (Rule R: `review/REVIEW_G1.md`, ACCEPT WITH FIXES; fixes applied). Time-boxed per spec
§7; stop report in §4.

**Labels.** GAP means a precise unproved statement, with no claim about its difficulty. CONDITIONAL means proved
assuming a stated hypothesis that is not a named Lean input.

**Notation.** σ is the spectral measure here, but G2's constraint measure in A3. β_j is n^p b_n here, but G2's β_t
in A3. ω is the oscillation modulus here, but an arcsine law in A3. Each use is local.

**Novelty: UNCHECKED.** G1-T and G1-L are discrete versions of the classical Landau / Hardy–Littlewood Tauberian
lemmas: F = o(x²) together with slow oscillation of F″ gives F″ → 0, and a one-sided bound gives F′. The technique is
known; its application here to Law P is what is new.

## 0. Status

| Result | Statement | Label |
|---|---|---|
| K | second difference of G(n) := Σ_{j<n}(n−j)u_j over ±h = triangle-kernel sum of u, of total mass h² | PROVED |
| **G1-T** | H_all + (T3) slow oscillation of β_n ⇒ β_n → 1, i.e. n^p b_n → c(p)C | PROVED-mod-cite (G2 (P)) |
| **G1-L** | H_all + a one-sided bound (sup β_n < ∞ or inf β_n > 0) ⇒ (1/n)Σ_{j<n} log(j^p b_j) → log(c(p)C) | PROVED-mod-cite (G2 (P)) |
| A1 | J ≥ 0 ⇒ sine-weighted window averages of a_j are ≥ 2cos(π/(L+1))·min b over the window. Hence, if b is regular, liminf of window averages of a_j/(2b_j) ≥ 1 | PROVED |
| A2 | p > 1: Σ_{j>n} a_j = 𝔼_n[Σ_{k∉S} x_k] (Heine ensemble) | PROVED |
| A3 | Q_p := ∫ x d(σ − μ*) = 2c(p)/(p−1) | PROVED (uses only G2 B*(i) and the definition of μ*, both citation-free) |
| A4 | (CL) ⇒ tail-Cesàro a-law; with β_n → 1, block-Cesàro ratios Σa/Σ2b → 1 and window averages → 1 in b-weighted density (pointwise density NOT proved) | CONDITIONAL on (CL) |
| G1-R | (T3) from the atoms alone; (CL) | GAP in general (see §4) |
| **RH₁** | pointwise Law P with O(1/n) rate for σ = Σ k^{−3/2}δ_{1/k} (p = 1, r = 3/2), via TC(α = 1) and WLXZ (`RH/RH_p1.md`) | PROVED-mod-cite (WLXZ v1) + REVIEWED |
| **RH_p** | the same for σ_{p,s} = Σ k^{−s}δ_{k^{−p}}, **every p > 1, s > 1**: n^p b_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n), via a one-sided x-variable RH analysis (exact Binet-cut scalar, KMVV left-endpoint Bessel at the hard edge, no truncation); validated end to end vs the true OPs (`RH/px/RH_px.md`) | PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6) + REVIEWED |
| **RH₁(r)** | the same for σ_r = Σ k^{−r}δ_{1/k}, **every r > 1** (p = 1): Nβ_N = 1 + O(1/N), with a Bessel FH parametrix at 0, a = r − 3/2 (`RH/RH_p1_general.md`) | PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4, DLMF 5.11) + REVIEWED |
| **RH_ζ** | smooth-ζ model (x_j = 1/(γ_j²+¼), N₀(γ_j) = j−½, masses 2x_j): **b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log² n))**, κ = −2(log(π/2) − (1 − log 2)); b_N = (β_N/4)(1+O(1/N)), a_N/(2b_N) = 1+O(1/N). Finite-N edge equation (E1–E3), α = 5/8 shift, log-weight hard edge by a Conway–Deift comparison, Arb-certified far field (`RH/zeta/RH_zeta.md`, `RH/zeta/RH_zeta_close.md`) | PROVED-mod-cite (WLXZ v1, KMVV §6, C–D Thm 4.4, DLMF, G2) + REVIEWED |
| **RH_p, ½<p<1** | σ_{p,s}, ½ < p < 1, all s > 1: n^p b_n = c(p)(1+O(1/n)), a_n/(2b_n) = 1+O(1/n). Continued D = t^{t−½}e^{−t}e^{iπt}Γ(1−t)/(i√2π), thin lenses, glued hard-edge W̃ (`RH/plt1/RH_plt1.md`) | PROVED-mod-cite (+ DLMF 5.5.3, 5.11) mod NUMERICAL no-winding (F4) + REVIEWED |
| **RH_p, 0<p<1 (seam)** | the same for all 0 < p < 1 via the seam construction (no Binet-cut B; `RH/plt1/RH_plt1b.md`) | PROOF mod NUMERICAL no-winding (Lemma S(iii)); Rule R pending |

Setting:
- J > 0 is the Jacobi matrix of σ = Σ w_k δ_{x_k}, with x_k = f(k) regularly spaced with index −p and constant C
  (item 11 (H-a)).
- The weights satisfy Σw < ∞ and w_k ≥ c₁k^{−s}. These are the hypotheses of G2's Theorem H_all, so H_all applies.
- Put β_j := j^p b_j/(c(p)C), u_j := log β_j and G(n) := Σ_{j=1}^{n−1}(n−j)u_j.
- H_all is equivalent to G(n) = o(n²) (G2 PROOF.md §3: its b_j form, with the Stirling-type identity).

## 1. The kernel identity

**Lemma K.** For integers n > h ≥ 1, G(n+h) − 2G(n) + G(n−h) = Σ_j (h − |j − n|)⁺ u_j, and Σ_{m∈ℤ}(h − |m|)⁺ = h².

*Proof.* G(n) = Σ_j (n − j)⁺u_j. For fixed j, the second difference in n of (n − j)⁺ with step h is the triangle
(h − |n − j|)⁺. This is checked by cases on the sign of n − j ± h. ∎

## 2. Tauberian reductions

**Theorem G1-T.** Assume H_all's hypotheses and

  (T3) ω(δ) := limsup_{n→∞} sup_{n≤m≤(1+δ)n} |β_m/β_n − 1| → 0 as δ ↓ 0.

Here (T3) means only the slow-oscillation part of item 11's (T3), which also includes two-sided bounds. Then
β_n → 1, i.e. n^p b_n → c(p)C. No bound on β_n, no a_n hypothesis and no monotonicity are assumed: boundedness of u
comes out of the identity itself.

*Proof.*
1. **(T3) gives a two-sided additive modulus.** For m ∈ [(1−δ)n, n] we have n ≤ (1 + δ/(1−δ))m. So for all
   |m − n| ≤ δn, |u_m − u_n| ≤ ω̃(δ) + o(1), where ω̃(δ) := −log(1 − ω(δ/(1−δ))) → 0. This needs
   ω(δ/(1−δ)) < 1, i.e. δ small, and uses that ω is nondecreasing.
2. **Window average.** Fix δ ∈ (0, ½) and put h := ⌊δn⌋. By Lemma K,

     u_n = h⁻²[G(n+h) − 2G(n) + G(n−h)] − h⁻² Σ_j (h − |j−n|)⁺(u_j − u_n).

   The first term is o(n²)/(δn)² → 0, because G(m) = o(m²) and n ± h ≍ n. The second is at most ω̃(δ) + o(1) in
   absolute value, by step 1 and because the kernel has mass h².
3. **Conclusion.** limsup |u_n| ≤ ω̃(δ) for every δ. Let δ → 0. ∎

*Compared with item 11's Theorem C′.* C′ needed:
- (T2) a_n ~ 2b_n;
- the two-sided bounds of (T3);
- Wiener's Tauberian theorem;
- (T4), a δn-scale monotonicity: b_m < b_n eventually for m ≥ (1+δ)n.

G1-T needs only slow oscillation, because H_all (G2) already supplies the averaged statement for every p. (T4) then
becomes a consequence, holding automatically once β_n → 1. (The step-to-step non-monotonicity seen for parity weights
in `check_regularity.out` is not a failure of (T4), which is a δn-scale condition.) The b_n half of G1 is now equivalent to (T3), given H_all.
Conversely, β_n → 1 implies (T3) trivially.

**Theorem G1-L (single Cesàro mean).** Assume H_all's hypotheses and sup_n β_n < ∞ (or inf_n β_n > 0). Then
(1/n)Σ_{j<n} u_j → 0, i.e. the geometric mean of j^p b_j/(c(p)C) over j < n tends to 1.

*Proof (Landau).* Assume u_j ≤ M; the case u_j ≥ −M is symmetric. Put A(n) := Σ_{j<n}u_j, so that
G(n+1) − G(n) = A(n+1).
- Since u ≤ M, A(n+i) ≤ A(n) + Mi. Also Σ_{i=1}^{h} A(n+i) = G(n+h) − G(n). So
  G(n+h) − G(n) ≤ hA(n) + Mh(h+1)/2, i.e. A(n) ≥ [G(n+h) − G(n)]/h − M(h+1)/2.
- Similarly A(n−i) ≥ A(n) − Mi, and G(n) − G(n−h) = Σ_{i=0}^{h−1} A(n−i) ≥ hA(n) − Mh(h−1)/2. So
  A(n) ≤ [G(n) − G(n−h)]/h + M(h−1)/2.
- Take h = ⌊δn⌋. Then G = o(n²) gives |A(n)|/n ≤ o(1)/δ + Mδ/2 + o(1). Let δ → 0. ∎

## 3. The a_n side

**Proposition A1 (positivity, windowed).** Let J ≥ 0. Let n ≥ 1 and L ≥ 2, and put s_j := sin(π(j − n + 1)/(L + 1))
for n ≤ j < n + L. Then

  Σ_{j=n}^{n+L−1} a_j s_j² ≥ 2cos(π/(L+1))·(min_{n≤j<n+L−1} b_j)·Σ_j s_j².

In particular, assume b is regular on windows: max_{n≤j<n+L_n}|b_j/b_n − 1| → 0 for some L_n → ∞. This holds when
β_n → 1 (G1-T) and L_n = o(n). Then liminf_n Σ_j (a_j/(2b_j)) s_j²/Σ_j s_j² ≥ 1. This uses a_j ≥ 0 (from J ≥ 0) to
pass to Σ_j(a_j/2b_j)s_j² ≥ Σ_j a_j s_j²/(2 max b), and min b/max b → 1 over the window.

*Proof.* Take v_j := (−1)^j s_j on the window and 0 elsewhere. Then
0 ≤ ⟨v, Jv⟩ = Σ a_j s_j² − 2Σ_j b_j s_j s_{j+1}. The sine vector satisfies s_{j−1} + s_{j+1} = 2cos(π/(L+1))s_j, with
zero boundary values (item 11 (S4); Lean `toeplitz_eigen`). So Σ_j s_j s_{j+1} = cos(π/(L+1))Σ s_j², and s ≥ 0
gives Σ b_j s_j s_{j+1} ≥ (min b)·cos(π/(L+1))Σ s_j². ∎

A1 is the windowed, limit-free form of item 11's Lemma P: a_n ≥ 2b_n on average. The matching upper bound
(limsup ≤ 1) is the remaining a_n gap; see §4.

**Proposition A2 (tail identity, p > 1).** Let p > 1, so that Σ_k x_k < ∞, J ≥ 0 is trace class, and
Σ_j a_j = Tr J = Σ_k x_k. Let ℙ_n be the Heine probability on n-subsets S ⊂ ℕ, with ℙ_n(S) ∝ Π_{k∈S} w_k·V(S) and
V(S) := Π_{i<j}(x_{k_i} − x_{k_j})². Then, in item 11's indexing (a_1 is the first diagonal entry),

  Σ_{j>n} a_j = 𝔼_n[Σ_{k∉S} x_k].

*Proof.* Σ_{j≤n} a_j = Tr J_n is the sum of the zeros of P_n.
- *Heine's formula*, P_n(z) = 𝔼_n[Π_{k∈S}(z − x_k)]. P_n(z) is the bordered Hankel determinant
  det[m_{i+j} | z^i]/D_n. Expanding it by multilinearity over atoms, as in item 11's H1 (Andreief), and symmetrising
  gives D_n⁻¹ Σ_{ordered n-tuples} Π w·Δ(x)²·Π(z − x_k). Tuples with a repeated atom vanish, which leaves n-subsets.
  (The reviewer checked this by brute force: 9 atoms, dps 40, n ≤ 4.) The
coefficient of z^{n−1} is linear in the atoms, so the sum of the zeros is 𝔼_n[Σ_{k∈S} x_k]. Subtract this from
Tr J = Σ_k x_k. ∎ (The tail Σ_{j≥n} a_j used below is the same identity with 𝔼_{n−1}; the shift is immaterial for
asymptotics.)

**Proposition A3 (the equilibrium value).** Let p > 1 and C = 1. With μ*, σ and c = c(p) as in G2 §1,

  Q_p := ∫ x d(σ − μ*)(x) = ∫_0^∞ u^{−p}(1 − ρ*(u)) du = 2c(p)/(p − 1).

This is the value the tail sums must take if a_j ~ 2c(p)j^{−p}, since n^{p−1}Σ_{j≥n} 2c j^{−p} → 2c/(p−1).

*Proof.* σ − μ* vanishes on [4c, ∞) (G2 B*(i)), so F(R) := ∫_0^R x d(σ − μ*) is constant for R ≥ 4c. Compute the two
parts for R ≥ 4c.
- ∫_0^R xσ(dx) = R^{1−1/p}/(p−1).
- Write μ* = ∫_0^1 ω_{β_t}dt and put t_R := (4c/R)^{1/p}.
  - For t ≥ t_R (β_t ≤ R), ∫ x dω_{β_t} = β_t/2 = 2c t^{−p}. These t contribute 2c(t_R^{1−p} − 1)/(p−1).
  - For t < t_R, the substitution t = t_R s gives β_t = R s^{−p}, and these t contribute R t_R M_p with
    M_p := ∫_0^1∫_0^1 y dω_{[0,s^{−p}]}(y) ds < ∞.
  - Both t-ranges give terms proportional to R^{1−1/p}, plus the constant −2c/(p−1).
- So F(R) = κ′R^{1−1/p} + 2c/(p−1) for some constant κ′. Since F is constant in R, κ′ = 0 and F ≡ 2c/(p−1). ∎

Numerically (`checks/check_tailsum.out`), Q_p − 2c/(p−1) = 0 to 8 digits for p ∈ {1.5, 2, 3, 4}. The actual tail sums
n^{p−1}Σ_{j≥n} a_j converge to Q_p: for p = 2, 1.2430 → 1.2360 → 1.2343 at n = 100, 400, 1600, against 1.2337.

**Theorem A4 (conditional a_n law, p > 1).** Assume H_all's hypotheses with exact pure-power atoms x_k = k^{−p} (C = 1),
and the concentration lemma

  (CL) n^{p−1}𝔼_n[Σ_{k∉S} x_k] → Q_p.

Then n^{p−1}Σ_{j≥n} a_j → 2c(p)/(p−1), which is the tail-Cesàro form of a_n ~ 2c(p)n^{−p}. If in addition β_n → 1
(e.g. under (T3), by G1-T), then:
- (i) Σ_{j≥n}(a_j − 2b_j) = o(n^{1−p}), and for every δ > 0 the block ratio
  Σ_{n≤j<(1+δ)n} a_j / Σ_{n≤j<(1+δ)n} 2b_j → 1;
- (ii) the sine-weighted window averages of a_j/(2b_j), over windows of length L_n → ∞ with L_n = o(n), tend to 1 in
  b-weighted density.

*A pointwise density statement does NOT follow.* The reviewer's counterexample is b_j = j^{−2},
a_j = 2b_j(1 + 0.3(−1)^j). It satisfies A1 (the alternating part is invisible to sine windows) and the tail equality,
yet |a_j/(2b_j) − 1| = 0.3 for every j. Full J ≥ 0 excludes this example, so a variational argument might do better,
but none is given.

*Proof.* Combine A2, A3 and (CL). Then subtract Σ_{j≥n} 2b_j = (2c/(p−1))n^{1−p}(1 + o(1)), which holds when β_n → 1.
- (i) The block ratio follows by differencing the tail asymptotics at n and (1+δ)n.
- (ii) The tail equality bounds the total positive excess of the window averages, and A1 bounds them below. ∎

*Status of (CL).* (CL) is the statement that the Heine ensemble's complement measure (1/n)Σ_{k∉S}δ_{k/n} converges to
(1 − ρ*(u))du, tested against u^{−p}. The integrand is singular at u = 0, inside the saturated region.
- On u ≥ θ the test function is bounded. There, (CL) would follow from concentration of the empirical measure at speed
  n² (an LDP upper bound). That bound is plausibly provable from G2 Part A and the energy-distance form of B*(iii), but
  it is not written here.
- On u < θ < u_s (saturated), (CL) needs E[(1/n)Σ_{k≤θn, k∉S}(k/n)^{−p}] → 0: a *saturation-exactness* statement. The
  n²-speed bound cannot see single-atom exclusions, which cost only O(n) in log V. Heuristically each exclusion costs
  e^{−2n(U*(x_k) − ℓ)} (swap a saturated atom for a free one), and U* − ℓ > 0 on the saturated region. A proof needs
  mesoscopic control of the empirical potential.
- **(CL) is the precise missing lemma for the a_n side (p > 1).** For p ≤ 1, J is not trace class and A2 does not apply
  as stated.

## 4. G1-R: what remains (stop report)

**Where G1 stands after Plan 9.**
- *b_n side.* Pointwise b_n ⟺ (T3) slow oscillation of β_n, given H_all (G1-T). Unconditionally, the single
  geometric Cesàro mean converges under a one-sided bound (G1-L).
- *a_n side.* The lower half holds unconditionally in window average (A1). For p > 1, the upper half holds in
  tail-Cesàro form, with block-Cesàro ratios and window-average density, conditional on (CL) (A4). Pointwise density
  is not proved.
- G1-L needs a one-sided bound on β_n; it is not unconditional.

**Missing statements (precise).**
- (T3) for β_n := n^p b_n/(c(p)C), from atom regularity (H-a) and weight conditions.
- (CL) for p > 1: n^{p−1}𝔼_n[Σ_{k∉S} x_k] → Q_p, i.e. saturation exactness of the Heine ensemble against u^{−p}.

**Why the tools here stop short** (methodological explanations, heuristic; not theorems about all such methods).
1. *Energy / large-deviation methods* (G2 Part A, H7, Lemma K) control log D_n to o(n²). Second differences over
   windows of width h therefore control only *window averages* of log b_j, with error o(n²)/h². That is exactly
   G1-T's input. (T3) is a statement about the variation of b_j *inside* windows. Through
   2 log b_n = Δ² log D_n, it needs log D_n to o(1) precision in second differences, far beyond any n²-speed method.
   (CL) likewise needs single-atom exclusion probabilities. Those cost O(n) in log V, below n² resolution.
2. *Riemann–Hilbert steepest descent* gives pointwise asymptotics of discrete orthogonal polynomials, including
   saturated regions, for finite node sets with analytic data (BKMM). Infinite nodes with an accumulation point are
   handled only for the explicit Tricomi–Carlitz family (WLXZ; nodes ±(k+α)^{−1/2}, i.e. p = 1 in the squared
   variable), within the literature read. The literature read has no RH analysis for general
   nodes x_k = f(k) accumulating at 0 with merely polynomially sandwiched (non-analytic) weights. Weight regularity
   genuinely matters: item 11's Prop D (exponentially small weights break the law) and test A3 (parity weights give
   power-rate coefficient oscillations; also `checks/check_regularity.out`).
3. *Tauberian methods* (item 11's C′, and G1-T) need an a priori regularity input. Neither the atoms nor the
   averaged law supplies it.

**Stop condition.** The remaining G1 statements (T3) and (CL) are not reached by the methods developed here. The
only route found in the literature read (RH for discrete OPs) is established only for finite node sets (BKMM) and for
one explicit accumulating family (WLXZ). Adapting it to general accumulating nodes with analytic weights is a
plausible but substantial project, far outside this time box. For non-analytic sandwiched weights, no method is known
to us. This is recorded as **GAP**: "as hard as an open problem" is *not* claimed, because no source states the
general problem as open. The precise missing statements are (T3) and (CL) above.

**Most promising next step (not attempted).** An RH analysis à la BKMM/WLXZ for x_k = k^{−p} with weights k^{−s}.
Analytic node density and analytic weights put it in the regime where the steepest-descent machinery should apply.
The saturated region (u < u_s) and the explicit equilibrium μ* of G2 give the needed g-function. A result for this
model family would prove the pointwise law for pure powers with power weights, the case of Haynes–Zudilin and
item 11's references.
