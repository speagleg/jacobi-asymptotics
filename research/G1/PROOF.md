# G1: the pointwise Law P — reductions and status

Status: draft, written 2026-10-13. NOT REVIEWED (Rule R is Task 5 of Plan 9).

## 0. Status

| Result | Statement | Label |
|---|---|---|
| K | second difference of G(n) := Σ_{j<n}(n−j)u_j over ±h = triangle-kernel sum of u, of total mass h² | PROVED |
| **G1-T** | H_all + (T3) slow oscillation of β_n ⇒ β_n → 1, i.e. n^p b_n → c(p)C | PROVED-mod-cite (G2 (P)) |
| **G1-L** | H_all + a one-sided bound (sup β_n < ∞ or inf β_n > 0) ⇒ (1/n)Σ_{j≤n} log(j^p b_j) → log(c(p)C) | PROVED-mod-cite (G2 (P)) |
| A1 | J ≥ 0 ⇒ sine-weighted window averages of a_j are ≥ 2cos(π/(L+1))·min b over the window. Hence, if b is regular, liminf of window averages of a_j/(2b_j) ≥ 1 | PROVED |
| A2 | p > 1: Σ_{j≥n} a_j = 𝔼_n[Σ_{k∉S} x_k] (Heine ensemble) | PROVED |
| A3 | Q_p := ∫ x d(σ − μ*) = 2c(p)/(p−1) | PROVED-mod-cite (G2 B*) |
| A4 | (CL) ⇒ tail-Cesàro a-law; with β_n → 1, a_j/(2b_j) → 1 in density | PROVED-mod-input (CL) |
| G1-R | (T3) from the atoms alone; (CL) | GAP (see §4) |

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

Then β_n → 1, i.e. n^p b_n → c(p)C. No bound on β_n, no a_n hypothesis and no monotonicity are assumed.

*Proof.*
1. **(T3) gives a two-sided additive modulus.** For m ∈ [(1−δ)n, n] we have n ≤ (1 + δ/(1−δ))m. So for all
   |m − n| ≤ δn, |u_m − u_n| ≤ ω̃(δ) + o(1), where ω̃(δ) := −log(1 − ω(δ/(1−δ))) → 0.
2. **Window average.** Fix δ ∈ (0, ½) and put h := ⌊δn⌋. By Lemma K,

     u_n = h⁻²[G(n+h) − 2G(n) + G(n−h)] − h⁻² Σ_j (h − |j−n|)⁺(u_j − u_n).

   The first term is o(n²)/(δn)² → 0, because G(m) = o(m²) and n ± h ≍ n. The second is at most ω̃(δ) + o(1) in
   absolute value, by step 1 and because the kernel has mass h².
3. **Conclusion.** limsup |u_n| ≤ ω̃(δ) for every δ. Let δ → 0. ∎

*Compared with item 11's Theorem C′.* C′ needed (T1)–(T4) and Wiener's Tauberian theorem, and gave β_n → 1 only under
monotonicity (T4). G1-T needs only (T3), because H_all (G2) already supplies the averaged statement for every p.
Numerically, (T4) fails for parity-oscillating weights (`check_regularity.out`) while (T3) appears to hold
asymptotically. So the reduction is a genuine improvement. The b_n half of G1 is now equivalent to (T3), given H_all.
Conversely, β_n → 1 implies (T3) trivially.

**Theorem G1-L (single Cesàro mean).** Assume H_all's hypotheses and sup_n β_n < ∞ (or inf_n β_n > 0). Then
(1/n)Σ_{j<n} u_j → 0, i.e. the geometric mean of j^p b_j/(c(p)C) over j < n tends to 1.

*Proof (Landau).* Assume u_j ≤ M; the case u_j ≥ −M is symmetric. Put A(n) := Σ_{j<n}u_j, so that
G(n+1) − G(n) = A(n+1).
- Since u ≤ M, we have A(n+i) ≤ A(n) + Mi. Summing over i = 1…h gives
  G(n+h+1) − G(n+1) ≤ hA(n) + Mh(h+1)/2. So
  A(n) ≥ [G(n+h+1) − G(n+1)]/h − M(h+1)/2.
- Similarly A(n−i) ≥ A(n) − Mi gives A(n) ≤ [G(n+1) − G(n−h+1)]/h + M(h+1)/2.
- Take h = ⌊δn⌋. Then G = o(n²) gives |A(n)|/n ≤ o(1)/δ + Mδ/2 + o(1). Let δ → 0. ∎

## 3. The a_n side

**Proposition A1 (positivity, windowed).** Let J ≥ 0. Let n ≥ 1 and L ≥ 2, and put s_j := sin(π(j − n + 1)/(L + 1))
for n ≤ j < n + L. Then

  Σ_{j=n}^{n+L−1} a_j s_j² ≥ 2cos(π/(L+1))·(min_{n≤j<n+L−1} b_j)·Σ_j s_j².

In particular, assume b is regular on windows: max_{n≤j<n+L_n}|b_j/b_n − 1| → 0 for some L_n → ∞. This holds when
β_n → 1 (G1-T) and L_n = o(n). Then liminf_n Σ_j (a_j/(2b_j)) s_j²/Σ_j s_j² ≥ 1.

*Proof.* Take v_j := (−1)^j s_j on the window and 0 elsewhere. Then
0 ≤ ⟨v, Jv⟩ = Σ a_j s_j² − 2Σ_j b_j s_j s_{j+1}. The sine vector satisfies s_{j−1} + s_{j+1} = 2cos(π/(L+1))s_j, with
zero boundary values (item 11 (S4); Lean `toeplitz_eigen`). So Σ_j s_j s_{j+1} = cos(π/(L+1))Σ s_j², and s ≥ 0
gives Σ b_j s_j s_{j+1} ≥ (min b)·cos(π/(L+1))Σ s_j². ∎

A1 is the windowed, limit-free form of item 11's Lemma P: a_n ≥ 2b_n on average. The matching upper bound
(limsup ≤ 1) is the remaining a_n gap; see §4.

**Proposition A2 (tail identity, p > 1).** Let p > 1, so that Σ_k x_k < ∞, J ≥ 0 is trace class, and
Σ_j a_j = Tr J = Σ_k x_k. Let ℙ_n be the Heine probability on n-subsets S ⊂ ℕ, with ℙ_n(S) ∝ Π_{k∈S} w_k·V(S). Then

  Σ_{j≥n} a_j = 𝔼_n[Σ_{k∉S} x_k].

*Proof.* Σ_{j<n} a_j = Tr J_n is the sum of the zeros of P_n. By Heine's formula, P_n(z) = 𝔼_n[Π_{k∈S}(z − x_k)]. The
coefficient of z^{n−1} is linear in the atoms, so the sum of the zeros is 𝔼_n[Σ_{k∈S} x_k]. Subtract this from
Tr J = Σ_k x_k. ∎

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
n^{p−1}Σ_{j≥n} a_j converge to Q_p: for p = 2, 1.2430 → 1.2363 → 1.2343 at n = 100, 400, 1600, against 1.2337.

**Theorem A4 (conditional a_n law, p > 1).** Assume H_all's hypotheses with exact pure-power atoms x_k = k^{−p} (C = 1),
and the concentration lemma

  (CL) n^{p−1}𝔼_n[Σ_{k∉S} x_k] → Q_p.

Then n^{p−1}Σ_{j≥n} a_j → 2c(p)/(p−1), which is the tail-Cesàro form of a_n ~ 2c(p)n^{−p}. If in addition β_n → 1
(e.g. under (T3), by G1-T), then:
- Σ_{j≥n}(a_j − 2b_j) = o(n^{1−p});
- with Prop A1, a_j/(2b_j) → 1 *in density*: for every η > 0, the set {j : |a_j/(2b_j) − 1| > η} has
  Σ_{j∈set, j≥n} j^{−p} = o(n^{1−p}), on the positive side directly and on the negative side in window average.

*Proof.* Combine A2, A3 and (CL). Then subtract Σ_{j≥n} 2b_j = (2c/(p−1))n^{1−p}(1 + o(1)), which holds when β_n → 1.
For the density statement:
- the positive part (a_j − 2b_j)⁺ is controlled by the tail equality together with A1's lower bound on window averages;
- the negative part is controlled by A1 directly. ∎

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

Written in Task 4.
