# G3′: averaged Law P for the true-zero measure

Status: draft, written 2026-10-13. Nothing in this file is REVIEWED yet (Rule R is Task 7 of Plan 7).
Framing (AGENTS.md rule 3): the ordinates are inputs. They are taken as real numbers, listed with multiplicity, and
nothing here is evidence about where the zeros lie.

## 0. Status

| Result | Statement (short) | Label | Depends on |
|---|---|---|---|
| Z1 | \|γ_k − γ̃_k\| ≤ C₀ for k ≥ k₁ | PROVED-mod-cite | (C1) |
| Z2 | pair ratio (x_a − x_b)/(x̃_a − x̃_b) ≤ (1 + C₀ log(γ̃_b/2π)/(π(b−a)))(1 + 2C₀/γ̃_a)⁵ | PROVED-mod-cite | Z1 |
| G3′-U | limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0 | PROVED-mod-cite | Z2, item 11 H5/H6/H7, Theorem H (p = 2) |
| S | index shift: π(a)⁻² − π(b)⁻² ≥ (1+η)⁻³(a⁻² − b⁻²) | PROVED | — |
| W | log D_n(Σ k⁻ˢ δ_{Ck⁻²}) ≥ Λ_n − (s−3)K n log n, uniformly in s ≥ 4 | PROVED (from item 11 §7) | Theorem A refs, H3 |
| G3′-L | liminf (1/n²)[log D_n(σ) − Φ_n] ≥ 0 under (SG) | PROVED-mod-cite + mod-input (SG) | Z1, S, W, H5, H6 |
| N | doubled-smooth sequences: same counting function, law fails by 2 log(1−1/m) | PROVED-mod-input | Theorem H_L, item 11 H6 |
| N′ | positive density of repeats ⇒ the law fails (general deletion lemma) | GAP | — |

Here Φ_n := −2n² log n + 2Σ_{j<n}(n−j) log L(j) + κn², with L(j) := j² x̃_j and κ := 3 + log(π²/16). This is the
right-hand side of the sum form of Corollary H_L-ζ (Lean: `smoothZeta_HL_sumForm`).

## 1. Setting

- **Ordinates.** γ_1 ≤ γ_2 ≤ … are the ordinates Im ρ > 0 of the nontrivial zeros of ζ, counted with multiplicity
  as in N(T) (CITATIONS.md (C1)). A value can repeat: for a multiple zero, or for distinct zeros with the same
  ordinate.
- **Measure.** x_k := 1/(γ_k² + ¼), w_k := 2x_k, and σ := Σ_k w_k δ_{x_k}. Equal atoms are simply summed. The Heine
  formula (item 11 H1; Lean `heineD_eq_det`) is indexed by subsets of ℕ, and stays valid with repeated atoms: a subset
  containing two indices with the same atom contributes 0.
- **Smooth model.** N₀(T) := (T/2π) log(T/2πe) + 7/8, γ̃_k := N₀⁻¹(k − ½) (on T > 2π), x̃_k := 1/(γ̃_k² + ¼) and
  L(k) := k² x̃_k. Corollary H_L-ζ (item 11 §7b; Lean `smoothZeta_HL_sumForm`, PROVED-mod-input Theorem H) says that
  σ̃ := Σ 2x̃_k δ_{x̃_k} satisfies log D_n(σ̃) = Φ_n + o(n²). Its hypothesis check gives (L1)–(L3) with a₀ = 1, so L is
  nondecreasing and ε* < 2.
- **Goal (G3′).** log D_n(σ) = Φ_n + o(n²). With the true normalization x_j in place of x̃_j, this is equivalent,
  because x_j/x̃_j → 1 by Z1 and Cesàro averaging. In b_j form, by H2, it reads
  (2/n²)Σ(n−j) log(b_j/x_j) → log(π²/16).
- **Facts about N₀** (elementary). N₀′(T) = (1/2π) log(T/2π) > 0 for T > 2π, so N₀ is increasing there and γ̃ is
  increasing. (N₀⁻¹)′ = 2π/log(T/2π) is decreasing, so k ↦ γ̃_k is concave in this sense: γ̃_b − γ̃_a lies between
  2π(b−a)/log(γ̃_b/2π) and 2π(b−a)/log(γ̃_a/2π).

## 2. Lemma Z1 (ordinate comparison) — PROVED-mod-cite (C1)

**Lemma Z1.** Let E(T) := 0.111 log T + 0.275 log log T + 2.524. There is k₁ such that for all k ≥ k₁,

  |γ_k − γ̃_k| ≤ 2π E(γ_k)/log(γ_k/(4π)) ≤ C₀,  where C₀ := sup_{T ≥ 10⁶} 2πE(T)/log(T/4π) ≤ 2.7

(the numerical value is from `checks/check_ratio.out` [1]). Also γ_k → ∞, and for each k the number of indices sharing
the value γ_k is at most 2E(γ_k) + 1.

*Proof.*
1. By (C1), N(T ± 0) ≤ N₀(T) + E(T) < ∞ for every T ≥ e, so only finitely many γ_k lie below any T. Hence γ_k → ∞.
   Pick k₁ with γ_k ≥ 10⁶ for k ≥ k₁.
2. Fix k ≥ k₁ and put T := γ_k. Counting with multiplicity, N(T − 0) ≤ k − 1 and N(T + 0) ≥ k. By (C1), applied to
   the one-sided limits (CITATIONS.md), N₀(T) ≤ N(T − 0) + E(T) ≤ k − 1 + E(T), and N₀(T) ≥ N(T + 0) − E(T) ≥ k − E(T).
   So |N₀(γ_k) − N₀(γ̃_k)| = |N₀(T) − (k − ½)| ≤ E(T) − ½.
3. *γ̃_k ≥ T/2.* Otherwise N₀(T) − N₀(γ̃_k) ≥ N₀(T) − N₀(T/2) ≥ (T/2)·N₀′(T/2) = (T/4π) log(T/4π) > E(T) for T ≥ 10⁶,
   which contradicts step 2.
4. *Mean value theorem.* Between γ_k and γ̃_k, N₀′ ≥ (1/2π) log(min(γ_k, γ̃_k)/2π) ≥ (1/2π) log(T/4π). Hence
   |γ_k − γ̃_k| ≤ 2π(E(T) − ½)/log(T/4π) ≤ 2πE(T)/log(T/4π) ≤ C₀.
5. *Multiplicity.* #{j : γ_j = T} ≤ N(T + 0) − N(T − 0) ≤ 2E(T). ∎

*Cross-check* (NUMERICAL, `check_merge.out` [3]): for k ≤ 2·10⁶, max |γ_k − γ̃_k| from the Odlyzko table.

**Corollary Z1′.** x_k/x̃_k → 1, and there is c ≥ 1 with c⁻¹ ≤ x_k/x̃_k ≤ c for all k. This is from Z1 for k ≥ k₁;
the finitely many k < k₁ have positive finite ratios.

## 3. Lemma Z2 and Theorem G3′-U (upper bound) — PROVED-mod-cite

**Lemma Z2 (pair ratios, upper).** Let k₂ ≥ k₁ be such that γ̃_k ≥ 2C₀ for k ≥ k₂. For k₂ ≤ a < b:

  x_a − x_b ≤ ρ(a,b)·(x̃_a − x̃_b),  ρ(a,b) := (1 + C₀ log(γ̃_b/2π)/(π(b − a)))·(1 + 2C₀/γ̃_a)⁵.

*Proof.* Write x_a − x_b = (γ_b − γ_a)(γ_b + γ_a)/((γ_a² + ¼)(γ_b² + ¼)), and the same for x̃. If γ_b = γ_a, the left
side is 0. Otherwise compare the three factors:
- **Difference.** γ_b − γ_a ≤ γ̃_b − γ̃_a + 2C₀, by Z1. Also γ̃_b − γ̃_a ≥ 2π(b−a)/log(γ̃_b/2π), by §1. So the ratio
  is ≤ 1 + C₀ log(γ̃_b/2π)/(π(b−a)).
- **Sum.** (γ_b + γ_a)/(γ̃_b + γ̃_a) ≤ 1 + 2C₀/(γ̃_a + γ̃_b) ≤ 1 + 2C₀/γ̃_a.
- **Denominators.** For each of a, b, (γ̃² + ¼)/(γ² + ¼) ≤ (γ̃/(γ̃ − C₀))² ≤ (1 + 2C₀/γ̃)², using γ ≥ γ̃ − C₀ > 0 and
  γ̃ ≥ 2C₀. Since γ̃_b ≥ γ̃_a, the two together are ≤ (1 + 2C₀/γ̃_a)⁴. ∎

Small indices. For a < k₂ < b there is B ≥ 1 with x_a − x_b ≤ x_a ≤ B(x̃_a − x̃_{a+1}) ≤ B(x̃_a − x̃_b), so put
ρ := B for such pairs. B exists because finitely many a are involved and x̃ is strictly decreasing.

**Theorem G3′-U.** limsup_n (1/n²)[log D_n(σ) − Φ_n] ≤ 0.

*Proof.* Fix an integer M ≥ 2. Let n be large, so that Mn > k₂.
1. **Comparison function.** Put λ := (Mn)² x_{Mn}. Define G(k) := k⁻² for k ≤ Mn and G(k) := x_k/λ for k > Mn. Since
   x is nonincreasing, 0 < G(k) ≤ x_{Mn}/λ = (Mn)⁻² on the tail. Ties are possible there, and item 11's Lemma H7 needs
   only 0 < G ≤ (Mn)⁻² on the tail. Put Λ := max(L(Mn), λ). For the smooth model, item 11 Lemma H5(i) with a₀ = 1
   gives x̃_a − x̃_b ≤ L(a)(a⁻² − b⁻²) ≤ L(Mn)(a⁻² − b⁻²) for a < b ≤ Mn, since L is nondecreasing.
2. **Pairwise bounds.** In a Heine term with indices k_1 < … < k_n, take a pair a = k_i < b = k_j.
   - *Head pair* (b ≤ Mn): x_a − x_b ≤ ρ(a,b)·L(Mn)·(G(a) − G(b)) ≤ ρ(a,b)·Λ·(G(a) − G(b)).
   - *Cross pair* (a ≤ Mn < b):
     x_a − x_b = (x_a − x_{Mn}) + (x_{Mn} − x_b) ≤ ρ(a,Mn)·L(Mn)·(G(a) − G(Mn)) + λ(G(Mn) − G(b)).
     This is ≤ max(ρ(a,Mn), 1)·Λ·(G(a) − G(b)). For a = Mn the first bracket is 0.
   - *Tail pair* (a > Mn): x_a − x_b = λ(G(a) − G(b)) exactly.
3. **Cost of the factors.** Write ρ* for max(ρ, 1). For a fixed element a = k_i of S:
   - The b > a in S that form head pairs are distinct, with b − a ≥ 1, 2, …. So
     Σ_b log ρ(a,b) ≤ (C₀/π) log(γ̃_{Mn}/2π)(1 + log n) + 10C₀ n/γ̃_a.
   - The cross pairs (a, b) all use the same factor log ρ*(a, Mn), so they contribute
     ≤ n[C₀ log(γ̃_{Mn}/2π)/(π(Mn − a)) + 10C₀/γ̃_a]. Summed over the distinct head elements a < Mn, the first part is
     ≤ n(C₀/π) log(γ̃_{Mn}/2π)(1 + log(Mn)).
   - Pairs with a < k₂ cost ≤ log B each, and there are at most k₂n of them.
   - Using k_i ≥ i and γ̃ increasing, the total of 2 log ρ* over all pairs is
     ≤ O(n log² n) + 20C₀ n Σ_{i≤n} 1/γ̃_i + O(n) = O(n log² n), since γ̃_i ≍ i/log i.
4. **Heine comparison.** Let w_k = 2x_k ≤ 2c x̃_k ≤ 2cL(k) k⁻² by Z1′. Every term of the Heine sum of σ is then at most
   e^{O(n log² n)} Λ^{n(n−1)} times the corresponding term of the Heine sum of ν := Σ_k w_k δ_{G(k)}. Hence
   log D_n(σ) ≤ n(n−1) log Λ + log D_n(ν) + O(n log² n).
5. **Lemma H7** (item 11 §7b; p = 2). ν satisfies its hypotheses: (Hw) holds with s = s₀ = 2, c₁ = 2 min_k(x_k k²) > 0,
   U = L/L(1) nondecreasing and log U = O(log log k). So
   log D_n(ν) ≤ −2n² log n + κn² + (A₂²/(8 log M)) n² + o(n²).
6. **The constant Λ.** λ/L(Mn) = x_{Mn}/x̃_{Mn} → 1, by Z1′. So log Λ = log L(Mn) + o(1). By item 11 Lemma H6(d),
   log L(Mn) − log L(n) → 0. By H6(b), n² log L(n) = 2Σ_{j<n}(n−j) log L(j) + o(n²).
7. Combining: limsup (1/n²)[log D_n(σ) − Φ_n] ≤ A₂²/(8 log M). Let M → ∞. ∎

*Remark.* No lower bound on any gap γ_b − γ_a is used anywhere (Review Focus 3). Tail pairs are rescaled exactly and
never compared pair by pair; the factor log γ̃_b in Z2 appears only for b ≤ Mn.

## 4. Theorem G3′-L (lower bound, under (SG)) — PROVED-mod-cite + mod-input (SG)

**Hypothesis (SG) (small gaps are rare).** Write g_k := (γ_{k+1} − γ_k)·log(γ_k/2π)/2π for the normalized gap. For
every η > 0 there are δ > 0 and K₀ such that #{k ≤ K : g_k < δ} ≤ ηK for all K ≥ K₀.

(SG) makes the repeated indices (g_k = 0) a set of density 0. It is not available unconditionally: see §5 and
CITATIONS.md (C3)/(C4).

**Lemma S (index shift) — PROVED.** Let π: ℕ → ℕ be strictly increasing with π(a) ≤ (1+η)a for some a. Then for every
b > a,

  π(a)⁻² − π(b)⁻² ≥ (1+η)⁻³ (a⁻² − b⁻²).

*Proof.* π(b) ≥ π(a) + (b − a). For s ≥ 0, π(a) + s ≤ (1+η)a + s ≤ (1+η)(a + s). So

  π(a)⁻² − π(b)⁻² ≥ ∫_0^{b−a} 2(π(a) + s)⁻³ ds ≥ (1+η)⁻³ ∫_0^{b−a} 2(a + s)⁻³ ds = (1+η)⁻³(a⁻² − b⁻²). ∎

The constant does not depend on a, b or n (Review Focus 4). Numerical check: `checks/check_shift.out`.

**Lemma W (uniform weight lower bound) — PROVED from item 11 §7.** Let Λ_n := −2n² log n + (3 + log(c(2)C))n². There
is K such that for all s ≥ 4 and n ≥ 2,

  log D_n(Σ_k k⁻ˢ δ_{Ck⁻²}) ≥ Λ_n − (s − 3) K n log n.

*Proof.* Item 11 §7 (p = 2, "References") gives log D_n(Σ k⁻⁴δ_{Ck⁻²}) = Λ_n + O(n log n), and the same with weights
k⁻² (the reference there has weights equal to k⁻² up to a bounded factor, which changes log D_n by O(n)). Let K bound
both O(n log n) terms. For s > 4 put θ := (s−4)/(s−2), so that k⁻⁴ = (k⁻²)^θ (k⁻ˢ)^{1−θ}. Log-convexity (item 11 H3)
gives

  log D_n(k⁻ˢ) ≥ [log D_n(k⁻⁴) − θ log D_n(k⁻²)]/(1 − θ) ≥ Λ_n − ((1+θ)/(1−θ)) K n log n,

and (1+θ)/(1−θ) = s − 3. For s = 4 the bound is the reference itself. ∎

**Theorem G3′-L.** Assume (SG). Then liminf_n (1/n²)[log D_n(σ) − Φ_n] ≥ 0.

*Proof.* Fix η ∈ (0, ¼), take δ and K₀ from (SG), and let k₂ be as in Z2.
1. **Good set.** E := {k ≥ k₂ : g_k ≥ δ}, enumerated increasingly by π. By (SG), #(E ∩ [1, K]) ≥ (1−η)K − k₂ for
   K ≥ K₀. Hence there is j₀ with π(j) ≤ (1+2η)j for all j ≥ j₀.
2. **Restriction.** All Heine terms are ≥ 0, so D_n(σ) ≥ Σ_{S ⊂ E, |S| = n} term_σ(S).
3. **Pair ratios on E (lower).** Let a < b be in E.
   - b > a and g_a ≥ δ give γ_b − γ_a ≥ γ_{a+1} − γ_a ≥ 2πδ/log(γ_a/2π).
   - By Z1, γ_b − γ_a ≥ γ̃_b − γ̃_a − 2C₀.
   - The sum and denominator factors are ≥ (1 + 2C₀/γ̃_a)⁻⁵, as in Z2.
   - *Far pair* (γ̃_b − γ̃_a ≥ 4C₀): the difference ratio is ≥ 1 − 2C₀/(γ̃_b − γ̃_a) ≥ ½, so its log is
     ≥ −4C₀/(γ̃_b − γ̃_a).
   - *Near pair* (γ̃_b − γ̃_a < 4C₀): the difference ratio is ≥ (2πδ/log(γ_a/2π))/(4C₀). For fixed a there are at most
     1 + (2C₀/π) log((γ̃_a + 4C₀)/2π) = O(log γ̃_a) such b, by §1.
4. **Per-element cost.** For a ∈ S, the m-th far partner b > a has b ≥ a + m, so
   γ̃_b − γ̃_a ≥ 2πm/log(γ̃_{a+n}/2π). Also log γ̃_{a+n} ≤ log γ̃_a + log(n+1) + O(1), because γ̃_k ≍ k/log k. So the
   pairs (a, ·) cost at most

     ℓ_n(a) := C[(log γ̃_a + log n)(1 + log n) + log γ̃_a · log(log γ̃_a/δ) + n/γ̃_a]  (in log, doubled for squares),

   with C depending only on C₀. In particular ℓ_n(a) ≤ C′(1 + log a)(1 + log n) + 2Cn/γ̃_a for a ≥ k₂, with C′
   depending on δ.
5. **Comparison with the smooth atoms.** By Z1′, w_a ≥ c⁻¹·2x̃_a. Hence
   D_n(σ) ≥ c^{−n} D_n(Σ_{a∈E} 2x̃_a e^{−ℓ_n(a)} δ_{x̃_a}), dropping the n/γ̃_a part into a global
   e^{−O(n log² n)}. That part sums to ≤ 2Cn Σ_{i≤n} 1/γ̃_i over S, since the i-th element of S is ≥ i.
6. **Reindex by π and compare with the pure power.** Put y_j := x̃_{π(j)}. For j ≥ j₀ and every i > j:
   - y_j − y_i ≥ (1 − ε*(π(j))/2)·L(π(j))·(π(j)⁻² − π(i)⁻²), by item 11 H5(i) with a₀ = 1;
   - this is ≥ (1 − ε*(j)/2)·L(j)·(1+2η)⁻³·(j⁻² − i⁻²), by L nondecreasing, ε* nonincreasing and Lemma S.

   For j < j₀ the ratio (y_j − y_i)/(j⁻² − i⁻²) is bounded below by a positive constant (finitely many j). The weights
   satisfy 2x̃_{π(j)} e^{−ℓ_n(π(j))} ≥ c₃ n^{−C″} j^{−s_n}, with s_n := 4 + C″(1 + log n), using
   π(j) ≤ (1+2η)j + j₀. Hence

     log D_n(σ) ≥ log D_n(Σ_j j^{−s_n} δ_{j⁻²}) + 2Σ_{j<n}(n−j)[log L(j) + log(1 − ε*(j)/2)]
                  − 3n² log(1+2η) − O(n log² n).

7. **Lemma W** with s = s_n gives log D_n(Σ j^{−s_n}δ_{j⁻²}) ≥ Λ_n − O(n log² n), where Λ_n = −2n² log n + κn² for C = 1.
   The ε* sum is o(n²), since ε* → 0. So liminf (1/n²)[log D_n(σ) − Φ_n] ≥ −3 log(1+2η). Let η → 0. ∎

**Corollary G3′-UL.** Under (SG), log D_n(σ) = Φ_n + o(n²), i.e. (2/n²)Σ(n−j) log(b_j/x_j) → log(π²/16) for the
true-zero measure.

## 5. Proposition N (counting information does not decide G3′) — PROVED-mod-input (Theorem H, p = 2)

Every input to G3′-U is a statement about the counting function: Z1 comes from |N − N₀| = O(log T). The next
proposition shows that no argument using only such information can give the lower bound. Sequences with the same
counting function, and repeated values spread at positive density, violate the law.

**Construction.** Fix an integer m ≥ 2 and put φ := 1/m. Define γ^{(m)} from the smooth ordinates by making every m-th
one a double value: γ^{(m)}_{km+2} := γ̃_{km+1} for k ≥ 0, and γ^{(m)}_i := γ̃_i otherwise. This is `merge_repeats`
with idx = 0, m, 2m, … (0-based). Let σ^{(m)} := Σ_i 2x^{(m)}_i δ_{x^{(m)}_i}, with x^{(m)}_i := 1/((γ^{(m)}_i)² + ¼),
indexed with multiplicity as in §1.

**Proposition N.** For every m ≥ 2:
- (i) **Same counting information.** |γ^{(m)}_i − γ̃_i| ≤ max_k(γ̃_{k+1} − γ̃_k) ≤ 2π/log(γ̃_1/2π) for all i, and
  N^{(m)}(T ± 0) differs from #{i : γ̃_i < T (resp. ≤ T)} by at most 1. So Z1 holds with a better constant, and
  every step of G3′-U applies to σ^{(m)}.
- (ii) **The law fails.** log D_n(σ^{(m)}) = Φ_n + 2n² log(1 − φ) + o(n²). Equivalently,
  (2/n²)Σ_{j<n}(n−j) log(b_j/x^{(m)}_j) → log(π²/16) + 2 log(1 − 1/m).

*Proof.*
- (i) Each γ^{(m)}_i is γ̃_i or γ̃_{i−1}. Moving one value down by one place changes counts by at most 1.
- (ii) **Distinct atoms.** The distinct atoms are y_j := x̃_{π(j)}, where π enumerates the 1-based index set
  E := ℕ ∖ {km + 2 : k ≥ 0}. Their weights are 2x̃_{π(j)} or 4x̃_{π(j)}, by the Heine convention of §1. With
  ψ(ξ) := ξm/(m−1), we have |π(j) − ψ(j)| ≤ 2 for all j.
- (ii-a) **Smooth comparison measure.** Let f(ξ) := 1/(γ(ξ)² + ¼), with γ(ξ) = N₀⁻¹(ξ − ½), so x̃_k = f(k). Put
  z_j := f(ψ(j)) = j⁻²L_z(j), with L_z(ξ) := (1−φ)²L(ψ(ξ)).
  - L_z satisfies (L1)–(L3). The map ψ is linear, ξL_z′/L_z = ε(ψ(ξ)) → 0, and L_z is nondecreasing.
  - The weights 2x̃_{π(j)} or 4x̃_{π(j)} satisfy (Hw) with s = s₀ = 2.
  - Theorem H_L (item 11 §7b) therefore gives
    log D_n(Σ w_j δ_{z_j}) = −2n² log n + 2Σ(n−j) log L_z(j) + κn² + o(n²).
  - Now 2Σ_{j<n}(n−j) log L_z(j) = 2n(n−1) log(1−φ) + 2Σ(n−j) log L(ψ(j)). By H6(a),
    |log L(ψ(j)) − log L(j)| ≤ ε*(j) log(m/(m−1)) → 0, so the last sum is 2Σ(n−j) log L(j) + o(n²). Hence
    log D_n(Σ w_jδ_{z_j}) = Φ_n + 2n² log(1−φ) + o(n²).
- (ii-b) **y against z.** Write h := −f′ > 0. On [1, ∞), h(ξ) ≍ ξ⁻³L(ξ) and (log h)′ = O(1/ξ), from the expansion in
  the hypothesis check of Corollary H_L-ζ. Put u = π(a), v = π(b), u′ = ψ(a), v′ = ψ(b) for a < b, so that
  |u − u′|, |v − v′| ≤ 2. Then
  - |∫_{u′}^{v′} h − ∫_u^v h| ≤ 2 sup_{|t−u|≤2} h(t) + 2 sup_{|t−v|≤2} h(t) ≤ C h(u);
  - ∫_u^v h ≥ min(v − u, u)·h(2u) ≥ c·min(b − a, a)·h(u).

  So (y_a − y_b)/(z_a − z_b) = 1 + O(1/(b − a) + 1/a), and it is bounded above and below for all pairs. In a Heine
  term with elements k_1 < … < k_n, summing |log ratio| over the partners of k_i gives O(log n + n/i). The total is
  O(n log n), so log D_n(σ^{(m)}) = log D_n(Σ w_jδ_{z_j}) + O(n log n). ∎

**Consequence (stop condition, written up in LOG.md).** G3′-U holds for σ (unconditional) and for every σ^{(m)}. The
lower bound holds for σ under (SG), and fails for σ^{(m)}. So the lower bound for the true ordinates depends on how
often repeated (or nearly repeated) ordinates occur, which the counting function cannot see. Any proof must use
multiplicity or small-gap information about the actual zeros, at least something like the density-zero part of (SG).
- (SG) implies that almost all ordinates are simple values. The results surveyed in CITATIONS.md (C3) reach only
  "more than 40.75%" of zeros simple (and on the line) unconditionally, and about 70% under RH. No surveyed result
  reaches proportion one.
- The unconditional lower bound is therefore not reachable with the inputs available here. G3′ stops at:
  **U (unconditional) + L (mod (SG)) + N (counting information is insufficient)**.

**Not proved (GAP N′, general deletion).** A converse would read: "if the repeated indices of the true ordinates have
positive lower density, the law fails". That would make G3′ equivalent to a density-one simplicity statement. It needs
a deletion lemma for arbitrary index sets E of positive lower co-density: limsup (1/n²)[log D_n(σ̃|_E) − Φ_n] < 0. Prop
N proves this only for evenly spread E. For clustered E the pairwise comparison used in (ii-b) fails, because
π(b) − π(a) is not comparable to b − a. The numerics in `check_merge.out` [1] cover evenly spread E only; [2] (a
localized defect) shows the shift appears once n exceeds the defect's index scale. This is NUMERICAL only.
