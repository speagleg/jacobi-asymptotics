# G2: Theorem H for every p > 0

Status: REVIEWED 2026-10-13 (Rule R: `review/REVIEW_G2.md`, ACCEPT WITH FIXES; fixes applied). No RH framing applies
here: the measures are explicit power laws.

**Labels.** "PROVED-mod-cite (X)" means proved from explicitly cited external results X that were read and quoted with
their hypotheses in CITATIONS.md (item 11's convention, which VERIFICATION_POLICY.md's PROVED-mod-input generalizes).
**Prior art:** for p = 1, Monien (arXiv:0901.1883 §3) set up the same constrained maximization heuristically and found
the same optimizer (CITATIONS.md (M)).

## 0. Status

| Result | Statement | Label |
|---|---|---|
| B0 | arcsine potential: ∫ log\|x−y\| dω_{[0,β]} = log(β/4) on [0,β], and ≥ log(β/4) on [β,∞) | PROVED |
| B* | E_p := sup_{μ∈𝒜} I(μ) = κ_p := 3p/2 + log c(p), uniquely attained at μ* = ∫_0^1 ω_{[0,4c(p)t^{−p}]} dt | PROVED-mod-cite (P); the value I(μ*) = κ_p is citation-free |
| A1 | discretization: point energy ≤ n²·(smeared energy) + C_M n log n, for subsets of [1, Mn] | PROVED |
| A-U | limsup (1/n²)[log D_n + p n² log n] ≤ E_p | PROVED (uses A1, B*-scaling; algebra of item 11 H7) |
| A-L | liminf ≥ κ_p (= I(μ*_u)) | PROVED (citation-free: uses B*(i) and the value in B*(iii)) |
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
log|2 sin(α/2)| = −Σ_{k≥1} cos(kα)/k. Integrating dθ/π over [0, π] kills every term. (The series converges in L²[0, π], hence in
L¹, which justifies termwise integration.) For x > β, U_β′(x) = ∫ dω_β(y)/(x − y) > 0. U_β is continuous at β: near
y = β the integrand is dominated by |log s|·s^{−1/2} (with s = β − y), so dominated convergence applies. ∎

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
  - *Closed form* (from the reviewer; substitute v = s^p): dμ*/dσ = I_{min(1, x/4c)}(1/p + ½, ½), the regularized
    incomplete beta function.

(ii) By Fubini: ∫|log|x − y|| dω_{β_t}(y) ≤ C(1 + |log x| + log β_t), an absolute-integrability bound that is
  integrable in t ∈ (0, 1]. So
  U*(x) = ∫_0^1 U_{β_t}(x) dt. For x ≤ 4c we have x ≤ β_t for every t, so by B0
  U* = ∫_0^1 log(c t^{−p}) dt = log c + p. For all x, B0 gives U_{β_t} ≥ log(β_t/4), so U* ≥ log c + p.

(iii) **Value.** For 0 < s ≤ t ≤ 1, supp ω_{β_t} ⊂ [0, β_t] ⊂ [0, β_s], so by B0
  ∬ log|x − y| dω_{β_s}dω_{β_t} = ∫ U_{β_s} dω_{β_t} = log(β_s/4) = log c − p log s. Hence

    I(μ*_u) = ∫_0^1∫_0^1 [log c − p log min(s,t)] ds dt = log c − p·∫_0^1 2(1−m) log m dm = log c + 3p/2 = κ_p,

  using E[log min] = −3/2. Fubini is justified because ∬|log|x − y|| dω_{β_s}dω_{β_t} ≤ C(1 + |log s| + |log t|), an
  absolute bound.

**Optimality.**
- **E_p is finite.** I(μ) < +∞ for every μ ∈ 𝒜, since log|x − y| ≤ log(1+x) + log(1+y) and μ^x ≤ σ has a finite log
  moment. The case I(μ) = −∞ is trivial.
- **Setup.** Let μ ∈ 𝒜 with I(μ) > −∞, and put μ^x := g_*μ ≤ σ. Then μ^x and μ* are positive, of mass 1, have finite
  energy in the sense of (P) (I_{(P)} = −I < ∞), and satisfy ∫ log(1+x) < ∞, both being ≤ σ near ∞. So both lie in
  M(ℂ) of (P).
- **Mutual energy.** It is finite by (P) §1 (the bound after (1.13), and 2I(μ̃,ν̃) ≤ I(μ̃) + I(ν̃)), so ∫U* dμ^x is
  finite and the bilinear expansion below is legitimate.

Expanding with ν := μ^x − μ*:

    I(μ) = I(μ*_u) + 2∫ U* dν + ∬ log|x − y| dν dν.

  - The last term is −I_{(P)}(ν) ≤ 0, by (P) Lemma 2.1, with equality iff ν = 0.
  - The middle term: ν has mass 0, so ∫ U* dν = ∫ (U* − log c − p) dν. The integrand is 0 on (0, 4c] and ≥ 0 on
    (4c, ∞), where μ* = σ ≥ μ^x, so ν ≤ 0 there. Hence ∫ U* dν ≤ 0.

  Therefore I(μ) ≤ κ_p, with equality iff μ^x = μ*. ∎

*Remarks.*
- **Prior art.** For p = 1, μ*_u is exactly Monien's density (arXiv:0901.1883, Theorem 3.1):
  (2/π)(arctan(1/√(2x−1)) − √(2x−1)/(2x)) for x > ½, saturated on [0, ½]. The reviewer checked numerically that it
  coincides with I_{1/(2x)}(3/2, ½). Monien's treatment is heuristic: existence is assumed, only stationarity is
  checked, and there is no upper bound or discretization argument. B* proves optimality and uniqueness for every p > 0.
- μ* is the average of the arcsine laws that the forward Weyl law (item 11 Theorem B) assigns to a Jacobi matrix with
  b_j = c(p)j^{−p} and a_j = 2b_j. The saturation identity (i) is exactly the defining equation of c(p). This explains
  why Law P's constant is the constrained-equilibrium constant.
- Numerics (`checks/check_energy.out`): density/σ and a Monte Carlo I(μ*) agree with (i) and (iii) for
  p ∈ {0.5, 1, 1.5, 2, 3, 4, 6}. Two caveats:
  - The value 0.9862 at p = 0.5, x = 1000·4c is quadrature error. The closed form gives exactly 1.
  - The U* rows are circular (Rule X): inside the support they plug B0's value into a t-quadrature. B0 itself was
    checked independently by direct quadrature in the reviewer's scratch run.
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
- *Summing.* The harmonic bound is one-sided: for fixed i, the partners to the right have distinct index distances,
  so their sum is ≤ 2 + log n. The factor 2 below accounts for ordered pairs. Collecting,
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

*The φ_M derivation* (item 11 H7 steps 5–6, written out with E_p in place of κ_p). Put t := m/n, so N = (1−t)n.
1. Use log N! ≥ N log N − N, together with log N = log n + log(1−t) and log(Mn) = log n + log M.
2. The log n terms combine to −p(2mN + N² + m²) log n = −pn² log n.
3. The remaining terms are
   n²[−2pt(1−t) log(1−t) + 2pt(1−t) − p(1−t)² log(1−t) + E_p((1−t)² − 1) − pt² log M] + O_M(n log n).
4. With −(1−t) log(1−t) ≤ t, this is ≤ n²[(p(1+t) + 2p + 2|E_p|)t − pt² log M] ≤ n²[At − pt² log M], with
   A := 4p + 2|E_p|.
5. For N = 0 (t = 1), (1−t)² log(1−t) → 0 and the bound is unchanged.

So log T_m + pn² log n − E_pn² ≤ n²φ_M(m/n) + O_M(n log n), with φ_M(t) ≤ At − pt² log M. Hence
limsup (1/n²)[log D_n + pn² log n] ≤ E_p + A²/(4p log M). Let M → ∞. ∎

The upper bound needs only W < ∞. It needs no polynomial upper bound on the weights, and no s₀.

**Theorem A-L.** liminf_n (1/n²)[log D_n + p n² log n] ≥ κ_p = I(μ*_u). The proof is citation-free.

*Proof.* Fix η > 0.
1. **A compact admissible approximant.** μ*_u has a continuous positive density ρ* on (0, ∞): it equals 1 on
   (0, u_s], and on (u_s, ∞) it is given by B*(i) pulled back.
   - Put μ_U := μ*_u|_{(0,U]}, of mass m_U. |log|g(u) − g(v)|| is μ*_u⊗μ*_u-integrable: the positive part by
     (1.12)-type log moments, and the negative part because I(μ*_u) is finite. So I(μ_U) → I(μ*_u) = κ_p and
     m_U → 1 as U → ∞, by dominated convergence.
   - Scale a mass-m measure by μ_τ(B) := τμ(B/τ), which gives I(μ_τ) = τ²(I(μ) − p m² log τ). With τ := 1/m_U, the
     measure ν := (μ_U)_τ has mass 1 and density ρ*(u m_U) ∈ [d_U, 1] on its support (0, U′], where U′ := U/m_U and
     d_U := min_{(0,U]} ρ* > 0. So ν ∈ 𝒜, and

       I(ν) = m_U⁻² I(μ_U) + p log m_U ≥ κ_p − η  for U large.

2. **Quantile configuration.** Let F be the distribution function of ν, with blocks B_i := [l_i, r_i] :=
   [F⁻¹((i−1)/n), F⁻¹(i/n)], q_i := F⁻¹((i − ½)/n) ∈ B_i, and k_i := ⌈n q_i⌉, u_i := k_i/n ∈ [q_i, q_i + 1/n].
   - Since ν ≤ Lebesgue: |B_i| ≥ 1/n, l_i ≥ (i−1)/n, r_i ≥ i/n, and r_i − q_i ≥ 1/(2n). Hence u_i ≤ r_{i+1}, and
     q_{i+1} − q_i ≥ 1/n, so the k_i are distinct, k_i ≥ 1, and u_j − u_i ≥ 1/n for i < j.
   - Since density ≥ d_U: |B_i| ≤ 1/(d_U n), so r_i ≤ i/(d_U n).
   - Put S* := {k_i} ⊂ [1, U′n + 1].
3. **Energy comparison.** Write n²I(ν) = Σ_{i≠j} n²∬_{B_i×B_j} + Σ_i n²∬_{B_i²} (all w.r.t. ν⊗ν, integrand
   log|g(u) − g(v)|). For i < j, u ∈ B_i and v ∈ B_j, write log(g(u) − g(v)) = −p log u + h(u/v), where
   h(r) := log(1 − r^p) is decreasing on (0, 1). We show that each point value is at least the block average minus
   err_{ij}, where Σ_{i<j} err_{ij} = O_U(n log n).
   - **(a) The −p log u part.** point − average = −p·avg_{B_i} log(u_i/u), and u_i ≤ r_{i+1}, u ≥ l_i.
     - For i ≥ 2: log(r_{i+1}/l_i) ≤ (r_{i+1} − l_i)/l_i ≤ (2/(d_U n))/((i−1)/n). So the cost is ≤ 2p/(d_U(i−1)).
     - For i = 1: avg_{B_1} log(1/u) ≤ n∫_0^{1/n} log(1/u) du = log n + 1, because ν ≤ Lebesgue and ν(B_1) = 1/n. Also
       log u_1 ≤ log r_2 ≤ log(2/(d_U n)). So the cost is ≤ p(log(2/d_U) + 1).
     - Summed over the partners j > i: ≤ n·C_U/i, and over i: O_U(n log n).
   - **(b) The h part, j ≥ i + 3.** The average is ≤ h(a) with a := l_i/r_j. The point value is ≥ h(b) with
     b := r_{i+1}/l_j < 1, because l_j ≥ r_{i+2} > r_{i+1}. Then h(a) − h(b) ≤ (b^p − a^p)/(1 − b^p).
     - *If b ≤ ½:* 1 − b^p ≥ 1 − 2^{−p}, and b^p − a^p ≤ 1 − (a/b)^p ≤ max(1,p)(1 − a/b). Also
       1 − a/b ≤ (r_{i+1} − l_i)/r_{i+1} + (r_j − l_j)/r_j ≤ 3/(d_U(i+1)). So err ≤ C_U/(i+1).
     - *If b > ½:* 1 − b^p ≥ min(1,p)(1 − b) ≥ min(1,p)(l_j − r_{i+1})/l_j ≥ min(1,p)(j − i − 2)/(n l_j), since
       there are j − i − 2 intermediate blocks, each of width ≥ 1/n. Also
       b^p − a^p ≤ max(1,p)(1 − a/b) ≤ 2 max(1,p)(b − a) and b − a ≤ 3/(d_U n l_j). So err ≤ C_U/(j − i − 2).
     - Summed: Σ_{i<j}[C_U/(i+1) + C_U/(j−i−2)] = O_U(n log n).
   - **(c) The h part, i < j ≤ i + 2.** The average is ≤ 0, since h ≤ 0. At the point,
     1 − (u_i/u_j)^p ≥ min(1,p)(u_j − u_i)/u_j ≥ min(1,p)·(1/n)/r_{j+1} ≥ min(1,p)d_U/(j+1). So
     err ≤ log(j + 1) + C_U. There are ≤ 2n such pairs, costing O_U(n log n).
   - **(d) Diagonal blocks** (upper bound). |g(u) − g(v)| ≤ g(min(u,v)), so
     n²∬_{B_i²} ≤ p·avg_{B_i} log(1/u) ≤ p log(n/(i−1)) for i ≥ 2, and ≤ p(log n + 1) for i = 1. The sum over i is
     p[(n−1) log n − log (n−1)!] + O(log n) = O(n).
   - Hence Σ_{i≠j} log|g(u_i) − g(u_j)| ≥ n²I(ν) − O_U(n log n).
4. **Weights.** Π_{k∈S*} w_k ≥ c₁^n (U′n + 1)^{−sn}.

So log D_n ≥ log(Π w) + log V(S*) ≥ −p n² log n + n²(κ_p − η) − O_U(n log n). Let n → ∞, then η → 0. ∎

*Rule A* (reviewer's scratch `al.py`, NUMERICAL). The quantile configuration of the untruncated μ*_u gives
Σ_{i≠j}/n² − κ_p = +0.0018, −0.0012 and −0.013 for p = 0.5, 1 and 3 at n = 1600, decaying like O(log n/n).

---

## 3. Main theorem and consequences

**Theorem H_all.** Let p > 0 and C > 0. Let x_k = f(k) with f ∈ C¹[1, ∞), ξ^{p+1}f′(ξ) → −pC, and ξ^{p+1}|f′(ξ)|
bounded above and below; this is item 11's (H-a) for arbitrary p. Let the weights satisfy Σ_k w_k < ∞ and
w_k ≥ c₁k^{−s}. Then

  log D_n(Σ_k w_k δ_{x_k}) = −p n² log n + (3p/2 + log(c(p)C)) n² + o(n²).

Equivalently, (2/n²)Σ_{j<n}(n−j) log(j^p b_j) → log(c(p)C).

*Proof.* Theorems A-U and A-L, with E_p = κ_p (Theorem B*), give the case f(ξ) = Cξ^{−p}, with constant κ_p + log C
(the C-scaling is item 11's H3). Note that f′ < 0 everywhere: f′ is continuous, never 0 (|f′|ξ^{p+1} is bounded
below), and has a negative limit. So H4 applies. Item 11's
Lemma H4 (PROVED for any p and any weights) transfers it to regularly spaced f. The b_j form follows from H2 and
2pΣ_{j<n}(n−j) log j = pn² log n − (3p/2)n² + O(n log n). ∎

*Compared with item 11's Theorem H* (the error term is now only o(n²); item 11 had O(n log n) for exact pure powers
with p ∈ {1, 2}, so for those cases this is a weakening):
- every p > 0 is covered, not only p ∈ {1, 2};
- the weight condition is now just Σw < ∞ plus a polynomial lower bound (the s₀(p) restriction is gone; item 11's
  numerics had suggested it was technical);
- no exactly solvable reference family (Lommel, Tricomi–Carlitz) is needed. The p = 1 case therefore no longer depends
  on the Carlitz citation (gap G4 in item 11).

**Corollary HZ.** Let a > 0 (in particular any integer a ≥ 1) and b real, with 2a + b > 1. Then

  log det_{1≤i,j≤n} ζ(a(i+j) + b) = −a n² log n + (3a/2 + log c(a)) n² + o(n²).

*Proof.* Reindex i, j ↦ i − 1, j − 1. This gives the Hankel determinant D_n of the moments
m_r = Σ_k k^{−(2a+b)}(k^{−a})^r, i.e. of Σ_k k^{−(2a+b)} δ_{k^{−a}}, with Σ_k k^{−(2a+b)} < ∞. Apply H_all with p = a,
C = 1. ∎

This proves the expectation quoted in (HZ) for all positive integers a, b, with an explicit n² constant. The proved
bound in (HZ) was the weaker upper bound −(a/2)n² log n + O(n²). Examples:
- a = 3: constant 4.5 + log c(3) = 4.12779…
- a = 1 (H_n^{(r)} = det ζ(i+j+r), any r > −1): −n² log n + (3/2 − log 2)n² + o(n²). Monien (CITATIONS.md (M))
  states the weak asymptotic log H_n^{(r)} ∼ −n²(log 2n − 3/2), derived heuristically for r = 0, 1. Per (HZ) he
  rigorously justified the leading-order asymptotics for r = 0 in later work. For a = 1, G2's contribution is a
  rigorous proof of the n² constant (this was already item 11 Theorem H, p = 1, mod Carlitz). For a ≥ 2 it is the
  general-p equilibrium.

*Novelty is UNCHECKED.* Known prior art: Monien's p = 1 equilibrium (heuristic). No literature search for the
general-p constrained-equilibrium identification has been done beyond item 11's `lit` report, which found general-p
Law P "not found in print". The search must be rerun before any claim beyond UNCHECKED.
