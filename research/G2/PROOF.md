# G2: Theorem H for every p > 0

Status: draft, written 2026-10-13. NOT REVIEWED (Rule R is Task 6 of Plan 8). No RH framing applies here: the measures
are explicit power laws.

## 0. Status

| Result | Statement | Label |
|---|---|---|
| B0 | arcsine potential: ∫ log\|x−y\| dω_{[0,β]} = log(β/4) on [0,β], and ≥ log(β/4) on [β,∞) | PROVED |
| B* | E_p := sup_{μ∈𝒜} I(μ) = κ_p := 3p/2 + log c(p), uniquely attained at μ* = ∫_0^1 ω_{[0,4c(p)t^{−p}]} dt | PROVED-mod-cite (P) |
| A1 | discretization: point energy ≤ n²·(smeared energy) + C_M n log n, for subsets of [1, Mn] | PROVED |
| A-U | limsup (1/n²)[log D_n + p n² log n] ≤ E_p | PROVED (uses A1, B*-scaling; algebra of item 11 H7) |
| A-L | liminf ≥ E_p | PROVED (uses B*) |
| **H_all** | **for every p > 0, C > 0, regularly spaced atoms, and weights with Σw < ∞ and w_k ≥ c₁k^{−s}: log D_n = −pn² log n + (κ_p + log C)n² + o(n²)** | PROVED-mod-cite (P) |
| HZ | log det_{1≤i,j≤n} ζ(a(i+j)+b) = −an² log n + (3a/2 + log c(a))n² + o(n²), for integer a ≥ 1 and real b > 1 − 2a | PROVED-mod-cite (P) |

Notation:
- p > 0 is fixed. g(u) := u^{−p} on (0, ∞).
- c(p) := ¼(π/(2I(p)))^p, with I(p) := (√π/2)Γ(1/p + ½)/Γ(1/p + 1), as in item 11 and `jacobi_asym.laws.weyl`.
- κ_p := 3p/2 + log c(p).
- 𝒜_τ is the set of positive Borel measures on (0, ∞) of mass τ with μ ≤ du (Lebesgue), and 𝒜 := 𝒜_1.
- I(μ) := ∬ log|g(u) − g(v)| dμ(u)dμ(v) ∈ [−∞, ∞). This is the *negative* of the energy convention in (P).
- In the variable x = g(u), μ ↦ μ^x := g_*μ, and the constraint becomes μ^x ≤ σ(dx) := (1/p)x^{−1−1/p}dx on (0, ∞).
  Then I(μ) = ∬ log|x − y| dμ^x dμ^x.

**Why E_p.** For S = {k_1 < … < k_n} ⊂ ℕ, the Heine term (item 11 H1) is Π_{k∈S} w_k · V(S), with
V(S) := Π_{i<j}(k_i^{−p} − k_j^{−p})². With u_i := k_i/n, we have k^{−p} = n^{−p}g(u), so

  log V(S) = −p n(n−1) log n + Σ_{i≠j} log|g(u_i) − g(u_j)|.

The empirical measure (1/n)Σδ_{u_i} has at most one atom per 1/n, which is a discrete version of μ ≤ du.

**Scaling.** For μ ∈ 𝒜 and τ > 0, define μ_τ(B) := τ·μ(B/τ). It has mass τ and density ρ(u/τ) ≤ 1, so μ_τ ∈ 𝒜_τ,
and μ ↦ μ_τ is a bijection 𝒜 → 𝒜_τ. Also I(μ_τ) = τ²(I(μ) − p log τ), because g(τu) = τ^{−p}g(u). Hence
sup_{𝒜_τ} I = τ²(E_p − p log τ).

---

## 1. Part B: the constrained equilibrium is explicit

**Lemma B0 (arcsine potential).** Let ω_β be the arcsine probability measure on [0, β], with density
1/(π√(y(β−y))). Then U_β(x) := ∫ log|x − y| dω_β(y) = log(β/4) for x ∈ [0, β]. U_β is increasing on [β, ∞), so
U_β ≥ log(β/4) on [0, ∞).

*Proof.* Write x = (β/2)(1 − cos φ) and y = (β/2)(1 − cos θ). Then dω_β = dθ/π on [0, π], and
log|x − y| = log(β/4) + log|2(cos θ − cos φ)|. Also
log|2(cos θ − cos φ)| = log|2 sin((θ+φ)/2)| + log|2 sin((θ−φ)/2)| = −Σ_{k≥1}(2/k) cos kθ cos kφ, using
log|2 sin(α/2)| = −Σ_{k≥1} cos(kα)/k. Integrating dθ/π over [0, π] kills every term. (The series converges in L¹,
which justifies termwise integration.) For x > β, U_β′(x) = ∫ dω_β(y)/(x − y) > 0, and U_β is continuous at β. ∎

**Definition.** Put β_t := 4c(p) t^{−p} for t ∈ (0, 1], and μ* := ∫_0^1 ω_{β_t} dt, a probability measure in the x
variable. Write μ*_u := (g⁻¹)_*μ* for the same measure in u.

**Theorem B\*.** (i) μ*_u ∈ 𝒜, with μ* = σ on [4c(p), ∞) and μ* < σ on (0, 4c(p)). Equivalently, μ*_u has density 1
on (0, u_s] with u_s := (4c(p))^{−1/p}, and density < 1 on (u_s, ∞).
(ii) U*(x) := ∫ log|x − y| dμ*(y) = log c(p) + p on (0, 4c(p)], and U* ≥ log c(p) + p on (0, ∞).
(iii) I(μ*_u) = κ_p. For every μ ∈ 𝒜, I(μ) ≤ κ_p, with equality only if μ = μ*_u. So E_p = κ_p.

*Proof.*
(i) Fix x > 0 and put t_x := (4c/x)^{1/p}. Then x ≤ β_t iff t ≤ t_x, and

  dμ*/dx = (1/π)∫_0^{min(1,t_x)} dt/√(x(β_t − x)) = (1/π)(t_x/x)∫_0^{min(1, 1/t_x)} (s^{−p} − 1)^{−1/2} ds,

  using the substitution t = t_x s.
  - Put J(p) := ∫_0^1 (s^{−p} − 1)^{−1/2} ds. The substitution v = s^p gives
    J(p) = (1/p)B(1/p + ½, ½) = (2/p)I(p).
  - For x ≥ 4c (t_x ≤ 1), dμ*/dx = (1/π)(4c)^{1/p}(2/p)I(p)·x^{−1−1/p}. This equals σ(x) exactly when
    (4c)^{1/p} = π/(2I(p)), i.e. c = c(p).
  - For x < 4c (t_x > 1), the s-integral stops at 1/t_x < 1, so dμ*/dx < σ(x).
  - The total mass is ∫_0^1 dt = 1.
  - Also ∫ log(1 + x) dμ* < ∞, since σ(x) log x is integrable at ∞.

(ii) By Fubini (U_{β_t}(x) is bounded by C(1 + |log x| + log β_t), which is integrable in t),
  U*(x) = ∫_0^1 U_{β_t}(x) dt. For x ≤ 4c we have x ≤ β_t for every t, so by B0
  U* = ∫_0^1 log(c t^{−p}) dt = log c + p. For all x, B0 gives U_{β_t} ≥ log(β_t/4), so U* ≥ log c + p.

(iii) **Value.** For 0 < s ≤ t ≤ 1, supp ω_{β_t} ⊂ [0, β_t] ⊂ [0, β_s], so by B0
  ∬ log|x − y| dω_{β_s}dω_{β_t} = ∫ U_{β_s} dω_{β_t} = log(β_s/4) = log c − p log s. Hence

    I(μ*_u) = ∫_0^1∫_0^1 [log c − p log min(s,t)] ds dt = log c − p·∫_0^1 2(1−m) log m dm = log c + 3p/2 = κ_p,

  using E[log min] = −3/2. Fubini is justified because every term is bounded by C(1 + |log s| + |log t|).

**Optimality.** Let μ ∈ 𝒜 with I(μ) > −∞, and put μ^x := g_*μ ≤ σ. Then μ^x and μ* are positive, of mass 1, have finite
energy, and satisfy ∫ log(1+x) < ∞ (both are ≤ σ near ∞). So both lie in M(ℂ) of (P). Expanding with ν := μ^x − μ*:

    I(μ) = I(μ*_u) + 2∫ U* dν + ∬ log|x − y| dν dν.

  - The last term is −I_{(P)}(ν) ≤ 0, by (P) Lemma 2.1, with equality iff ν = 0.
  - The middle term: ν has mass 0, so ∫ U* dν = ∫ (U* − log c − p) dν. The integrand is 0 on (0, 4c] and ≥ 0 on
    (4c, ∞), where μ* = σ ≥ μ^x, so ν ≤ 0 there. Hence ∫ U* dν ≤ 0.

  Therefore I(μ) ≤ κ_p, with equality iff μ^x = μ*. ∎

*Remarks.*
- μ* is the average of the arcsine laws that the forward Weyl law (item 11 Theorem B) assigns to a Jacobi matrix with
  b_j = c(p)j^{−p} and a_j = 2b_j. The saturation identity (i) is exactly the defining equation of c(p). This explains
  why Law P's constant is the constrained-equilibrium constant.
- Numerics (`checks/check_energy.out`): density/σ, the potential, and a Monte Carlo I(μ*) agree with (i)–(iii) for
  p ∈ {0.5, 1, 1.5, 2, 3, 4, 6}.
- For C ≠ 1 (atoms Ck^{−p}), I gains log C.

---

## 2. Part A: the variational limit

Weights: assume W := Σ_k w_k < ∞ (for the upper bound) and w_k ≥ c₁k^{−s} for some s (for the lower bound). Put
D_n := D_n(Σ_k w_k δ_{k^{−p}}).

**Lemma A1 (discretization).** For M ≥ 1 there is C_M such that, for all n ≥ 2 and every S ⊂ ℕ ∩ [1, Mn] with
|S| = N ≤ n,

  Σ_{i≠j} log|g(u_i) − g(u_j)| ≤ n² I(μ̄_S) + C_M n log n,

where u_i = k_i/n and μ̄_S ∈ 𝒜_{N/n} has density 1 on ∪_{k∈S} A_k, with A_k := [(k−1)/n, k/n].

*Proof.* Write n²I(μ̄_S) = Σ_{i≠j} n²∬_{A_{k_i}×A_{k_j}} log|g(u) − g(v)| + Σ_i n²∬_{A_{k_i}²} log|g(u) − g(v)|.
- *Pairs k < l with l ≥ k + 2.* On A_k × A_l, g(u) − g(v) ≥ g(k/n) − g((l−1)/n). Then
  log(g(k/n) − g(l/n)) − log(g(k/n) − g((l−1)/n)) = log(1 + Δ/D) with Δ := g((l−1)/n) − g(l/n) ≤ |g′((l−1)/n)|/n
  and D ≥ ((l−1−k)/n)|g′((l−1)/n)|, since |g′| is decreasing. So the point value exceeds the cell average by at most
  1/(l − k − 1).
- *Adjacent pairs* (l = k + 1). The point value is ≤ log(|g′(k/n)|/n). On A_k × A_l,
  g(u) − g(v) ≥ |g′((k+1)/n)|(v − u), so the cell average is ≥ log|g′((k+1)/n)| − log n + c₀, with
  c₀ := ∫_0^1∫_1^2 log(v − u) du dv. The excess is ≤ (p+1) log 2 − c₀.
- *Diagonal.* On A_k², |g(u) − g(v)| ≥ |g′(k/n)||u − v|, so n²∬_{A_k²} log|g(u) − g(v)| ≥ log|g′(k/n)| − log n − 3/2.
  For k ≤ Mn this is ≥ log p − (p+1) log M − log n − 3/2.
- *Summing.* For fixed i, the partners have distinct index distances, so Σ_j 1/(l − k − 1) ≤ 2 + log n. Collecting,
  Σ_{i≠j} log|g(u_i) − g(u_j)| ≤ n²I(μ̄_S) + 2n(2 + log n + (p+1) log 2 − c₀) + N((p+1) log M + log n + 3/2 − log p).
  ∎

The diagonal is the only place where k ≤ Mn is used. Without the cap, an isolated far point at k ≫ n makes
n²I(μ̄_S) → −∞ while the point sum stays bounded. This is why the tail is handled separately below (Review Focus 1).

**Corollary A2 (head bound).** For S ⊂ [1, Mn] with |S| = N:
log V(S) ≤ −p N² log N + E_p N² + C′_M n log n.

*Proof.* Lemma A1 and the scaling sup_{𝒜_τ} I = τ²(E_p − p log τ) with τ = N/n give
log V(S) = −pN(N−1) log n + Σ_{i≠j} ≤ −pN(N−1) log n + N²(E_p − p log(N/n)) + C_M n log n. Then
−pN(N−1) log n − pN² log(N/n) = −pN² log N + pN log n. ∎

**Theorem A-U.** limsup_n (1/n²)[log D_n + p n² log n] ≤ E_p.

*Proof.* This follows item 11's Lemma H7 verbatim, with its head input (Theorem H) replaced by Corollary A2. Fix
M ≥ 2. Split S = H ∪ T with T := S ∩ (Mn, ∞), m := |T| and N := n − m.
- *Cross pairs.* (x_a − x_b)² ≤ a^{−2p}, and H consists of distinct positive integers, so they contribute
  ≤ (N!)^{−2pm}.
- *Tail.* Σ_T Π_T w·V(T) = D_m(tail) ≤ W^m(Mn)^{−pm(m−1)}, by Hadamard's inequality as in H7 step 3.
- *Head.* Σ_H Π_H w·V(H) ≤ W^N sup_H V(H), which Corollary A2 bounds.

So D_n ≤ Σ_{m=0}^n T_m with

  log T_m ≤ n log W − 2pm log N! − pN² log N + E_pN² − pm(m−1) log(Mn) + C′_M n log n.

The algebra of H7 steps 5–6, with κ_p replaced by E_p, gives log T_m + pn² log n − E_pn² ≤ n²φ_M(m/n) + O_M(n log n),
where φ_M(t) ≤ A t − p t² log M and A := 4p + 2|E_p|. Hence
limsup (1/n²)[log D_n + pn² log n] ≤ E_p + A²/(4p log M). Let M → ∞. ∎

The upper bound needs only W < ∞. It needs no polynomial upper bound on the weights, and no s₀.

**Theorem A-L.** liminf_n (1/n²)[log D_n + p n² log n] ≥ E_p.

*Proof.* Fix ε > 0.
1. **A compact admissible approximant.** μ*_u has a continuous positive density on (0, ∞): it equals 1 on (0, u_s],
   and on (u_s, ∞) it is the formula of B*(i) pulled back. Choose U with I(μ*_u|_{(0,U]}) ≥ κ_p − ε and mass m_U ≥ 1 − ε,
   which is possible by dominated convergence, since I(μ*_u) is finite. Apply the scaling map with τ := 1/m_U to
   μ_U := μ*_u|_{(0,U]}: ν(B) := τ·μ_U(B/τ). Then ν has mass 1 and density ρ*(u m_U) ∈ [d_U, 1] on its support
   (0, U′], with U′ := U/m_U, where d_U := min_{(0,U]} ρ* > 0. So ν ∈ 𝒜, and
   I(ν) = m_U⁻²(I(μ_U) + p log m_U) ≥ κ_p − 3ε for small ε.
2. **Quantile configuration.** Let q_i := F_ν⁻¹((i − ½)/n) and k_i := ⌈n q_i⌉. The density is ≤ 1, so
   q_{i+1} − q_i ≥ 1/n and the k_i are distinct. The density is ≥ d_U, so q_{i+1} − q_i ≤ 1/(d_U n).
   Put S* := {k_i} ⊂ [1, U′n + 1].
3. **Energy comparison.** Let B_i be the ν-quantile blocks of mass 1/n, of u-width in [1/n, 1/(d_U n)], and note
   k_i/n ∈ B_i + [0, 1/n].
   - *Pairs with |i − j| ≥ 3.* The perturbation argument of A1, with widths ≤ C_U/n, bounds the point value from below
     by n²∬_{B_i×B_j} log|g − g| dν dν − C_U(1/(|i − j| − 2) + 1/min(i,j)).
   - *Pairs with |i − j| ≤ 2.* The point value is ≥ log(|g′(k_j/n)|/n) and the block average is
     ≤ log(|g′(q_{i−½})|·3/(d_U n)). The difference is bounded by C_U, because q_j/q_i is bounded for neighbouring
     blocks: q_i ≥ (i − ½)/n.
   - *Diagonal blocks.* n²∬_{B_i²} log|g(u) − g(v)| dν dν ≤ log(|g′(q_{i−½})|/(d_U n)), and
     Σ_i[(p+1) log(n/(i − ½)) − log n] = O(n).
   - Summing, Σ_{i≠j} log|g(u_i) − g(u_j)| ≥ n²I(ν) − C_U n log n.
4. **Weights.** Π_{k∈S*} w_k ≥ c₁^n (U′n + 1)^{−sn}.

So log D_n ≥ log(Π w) + log V(S*) ≥ −p n² log n + n²(κ_p − 3ε) − O_U(n log n). Let n → ∞, then ε → 0. ∎

---

## 3. Main theorem and consequences

**Theorem H_all.** Let p > 0 and C > 0. Let x_k = f(k) with f ∈ C¹[1, ∞), ξ^{p+1}f′(ξ) → −pC, and ξ^{p+1}|f′(ξ)|
bounded above and below; this is item 11's (H-a) for arbitrary p. Let the weights satisfy Σ_k w_k < ∞ and
w_k ≥ c₁k^{−s}. Then

  log D_n(Σ_k w_k δ_{x_k}) = −p n² log n + (3p/2 + log(c(p)C)) n² + o(n²).

Equivalently, (2/n²)Σ_{j<n}(n−j) log(j^p b_j) → log(c(p)C).

*Proof.* Theorem A gives the case f(ξ) = Cξ^{−p}, with the constant E_p + log C = κ_p + log C by Theorem B*. Item 11's
Lemma H4 (PROVED for any p and any weights) transfers it to regularly spaced f. The b_j form follows from H2 and
2pΣ_{j<n}(n−j) log j = pn² log n − (3p/2)n² + O(n log n). ∎

*Compared with item 11's Theorem H:*
- every p > 0 is covered, not only p ∈ {1, 2};
- the weight condition is now just Σw < ∞ plus a polynomial lower bound (the s₀(p) restriction is gone; item 11's
  numerics had suggested it was technical);
- no exactly solvable reference family (Lommel, Tricomi–Carlitz) is needed. The p = 1 case therefore no longer depends
  on the Carlitz citation (gap G4 in item 11).

**Corollary HZ.** Let a ≥ 1 be an integer and b real with 2a + b > 1. Then

  log det_{1≤i,j≤n} ζ(a(i+j) + b) = −a n² log n + (3a/2 + log c(a)) n² + o(n²).

*Proof.* Reindex i, j ↦ i − 1, j − 1. This gives the Hankel determinant D_n of the moments
m_r = Σ_k k^{−(2a+b)}(k^{−a})^r, i.e. of Σ_k k^{−(2a+b)} δ_{k^{−a}}, with Σ_k k^{−(2a+b)} < ∞. Apply H_all with p = a,
C = 1. ∎

This confirms the expectation quoted in (HZ) for all positive integers a, b, with the explicit n² constant. The proved
bound in (HZ) was the weaker upper bound −(a/2)n² log n + O(n²). Examples:
- a = 3: constant 4.5 + log c(3) = 4.12779…
- a = 1 (Monien, any r > −1): −n² log n + (3/2 − log 2)n² + o(n²).

*Novelty is UNCHECKED*: no literature search for the general-p constrained-equilibrium identification has been done
beyond item 11's `lit` report, which found general-p Law P "not found in print".
