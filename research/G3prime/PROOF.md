# G3′: averaged Law P for the true-zero measure

Status: REVIEWED 2026-10-13 (Rule R: `review/REVIEW_G3prime.md`, ACCEPT WITH FIXES; fixes applied) for Z1, Z2, G3′-U,
S, W, G3′-L and N. N′ remains GAP.
Framing (AGENTS.md rule 3): the ordinates are inputs. They are taken as real numbers, listed with multiplicity, and
nothing here is evidence about where the zeros lie.

## 0. Status

| Result | Statement (short) | Label | Depends on |
|---|---|---|---|
| Z1 | \|γ_k − γ̃_k\| ≤ C₀ for k ≥ k₁ (≤ C₀′ for all k) | PROVED-mod-cite + REVIEWED | (C1) |
| Z2 | pair ratio (x_a − x_b)/(x̃_a − x̃_b) ≤ (1 + C₀ log(γ̃_b/2π)/(π(b−a)))(1 + 2C₀/γ̃_a)⁵ | PROVED-mod-cite + REVIEWED | Z1 |
| G3′-U | limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0 | PROVED-mod-cite + mod-input Theorem H (Lean `TheoremHPure`) + REVIEWED | Z2, item 11 H5/H6/H7, Theorem H (p = 2) |
| S | index shift: π(a)⁻² − π(b)⁻² ≥ (1+η)⁻³(a⁻² − b⁻²) | PROVED + REVIEWED | — |
| W | log D_n(Σ k⁻ˢ δ_{Ck⁻²}) ≥ Λ_n − (s−3)K n log n, uniformly in s ≥ 4 | PROVED (from item 11 §7) + REVIEWED | Theorem A refs, H3 |
| G3′-L | liminf (1/n²)[log D_n(σ) − Φ_n] ≥ 0 under (SG) | PROVED-mod-cite + mod-input (SG), Theorem H + REVIEWED | Z1, S, W, H5, H6 |
| N | doubled-smooth sequences: same counting function, law fails by 2 log(1−1/m) | PROVED-mod-input Theorem H + REVIEWED | Theorem H_L, item 11 H6 |
| N′ | positive density of repeated ordinates ⇒ the law fails (general deletion lemma) | GAP | — |

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
  increasing. (N₀⁻¹)′(y) = 2π/log(N₀⁻¹(y)/2π) is decreasing, so k ↦ γ̃_k is concave in this sense: γ̃_b − γ̃_a lies between
  2π(b−a)/log(γ̃_b/2π) and 2π(b−a)/log(γ̃_a/2π).

## 2. Lemma Z1 (ordinate comparison) — PROVED-mod-cite (C1)

**Lemma Z1.** Let E(T) := 0.111 log T + 0.275 log log T + 2.524. There is k₁ such that for all k ≥ k₁,

  |γ_k − γ̃_k| ≤ 2π E(γ_k)/log(γ_k/(4π)) ≤ C₀,  where C₀ := sup_{T ≥ 10⁶} 2πE(T)/log(T/4π) = 2.6613… ≤ 2.7.

The ratio is decreasing in T, so the sup is its value at T = 10⁶. To see this, put u = log T and c = log 4π. Then
d/du[E/(u − c)] has the sign of E′(u)(u − c) − E(u) = −0.111c − 0.275c/u − 0.275 log u − 2.524 + 0.275 < 0.
`checks/check_ratio.out` [1] is a numerical cross-check only.

Also γ_k → ∞, and for each k the number of indices sharing the value γ_k is at most 2E(γ_k). For all k ≥ 1,
|γ_k − γ̃_k| ≤ C₀′ := max(C₀, max_{k<k₁}|γ_k − γ̃_k|) < ∞. Only the finiteness of C₀′ is used for small k (Review
Focus 2).

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

Small indices. For a < k₂ and every b > a, there is B ≥ 1 with x_a − x_b ≤ x_a ≤ B(x̃_a − x̃_{a+1}) ≤ B(x̃_a − x̃_b),
so put ρ := B for such pairs. This covers head pairs with b ≤ k₂ and the cross pairs alike. B exists because finitely many a are involved and x̃ is strictly decreasing.

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
5. **Lemma H7** (item 11 §7b; p = 2). ν satisfies its hypotheses: (Hw) holds with s = s₀ = 2, c₁ = 2 min_k(x_k k²) > 0 (attained, since k²x_k → ∞), c₂ = 2cL(1),
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
k⁻². After rescaling the atoms by π²C, the reference weights are exactly π⁻²k⁻² and π⁻⁴k⁻⁴, which changes log D_n by
2n log π or 4n log π. The uniformity is the point of this lemma. The reference coefficients b_j = π²C c_{2j−2}c_{2j−1}
are explicit and positive, with |log(j²b_j) − log(c(2)C)| ≤ K′/j for all j ≥ 1. With H2 and
4Σ_{j<n}(n−j) log j = 2n² log n − 3n² + O(n log n), this gives |log D_n − Λ_n| ≤ K n log n for all n ≥ 2, with one K
for both references. For s > 4 put θ := (s−4)/(s−2), so that k⁻⁴ = (k⁻²)^θ (k⁻ˢ)^{1−θ}. Log-convexity (item 11 H3)
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
   - The sum and denominator factors are ≥ (1 + 2C₀/γ̃_a)⁻⁵, by the following lower analogue of Z2:
     - *Sum.* γ̃_a + γ̃_b ≥ 2γ̃_a gives (γ_a + γ_b)/(γ̃_a + γ̃_b) ≥ 1 − C₀/γ̃_a ≥ (1 + 2C₀/γ̃_a)⁻¹, using
       1 − u/2 ≥ 1/(1+u) for u = 2C₀/γ̃_a ≤ 1.
     - *Denominators.* (γ̃² + ¼)/(γ² + ¼) ≥ (γ̃/(γ̃ + C₀))² ≥ (1 + 2C₀/γ̃)⁻².
   - *Far pair* (γ̃_b − γ̃_a ≥ 4C₀): the difference ratio is ≥ 1 − 2C₀/(γ̃_b − γ̃_a) ≥ ½, so its log is
     ≥ −4C₀/(γ̃_b − γ̃_a).
   - *Near pair* (γ̃_b − γ̃_a < 4C₀): the difference ratio is ≥ (2πδ/log(γ_a/2π))/(4C₀). For fixed a there are at most
     1 + (2C₀/π) log((γ̃_a + 4C₀)/2π) = O(log γ̃_a) such b, by §1.
4. **Per-element cost.** Fix a ∈ S and let b be its m-th far partner.
   - If b ≤ a + n, then b − a ≥ m, and concavity gives γ̃_b − γ̃_a ≥ 2πm/log(γ̃_{a+n}/2π).
   - If b > a + n, then γ̃_b − γ̃_a ≥ γ̃_{a+n} − γ̃_a ≥ 2πn/log(γ̃_{a+n}/2π) ≥ 2πm/log(γ̃_{a+n}/2π).

   Also log γ̃_{a+n} ≤ log γ̃_a + log(n+1) + O(1), because γ̃_k ≍ k/log k. The number of near partners of a inside an
   n-subset is ≤ t_a := min(n − 1, 1 + (2C₀/π) log((γ̃_a + 4C₀)/2π)), and each costs ≤ log(C log γ̃_a/δ). Put
   t ≍ log a. If t ≤ n, the near cost is ≤ C t(log(C/δ) + log n). If t > n, it is ≤ n(log(C/δ) + log t)
   ≤ t log(C/δ) + t log n, since log t/t ≤ log n/n for t ≥ n ≥ 3. So the pairs (a, ·) cost at most

     ℓ_n(a) ≤ C′(1 + log a)(1 + log n) + C′(1 + log n)² + 2Cn/γ̃_a  (in log, doubled for squares),

   for a ≥ k₂, with C′ depending on C₀ and δ. The term C′(1 + log n)² comes from the far partners of small a.
5. **Comparison with the smooth atoms.** By Z1′, w_a ≥ c⁻¹·2x̃_a. Hence
   D_n(σ) ≥ c^{−n} D_n(Σ_{a∈E} 2x̃_a e^{−ℓ_n(a)} δ_{x̃_a}), dropping the n/γ̃_a part into a global
   e^{−O(n log² n)}. That part sums to ≤ 2Cn Σ_{i≤n} 1/γ̃_i over S, since the i-th element of S is ≥ i.
6. **Reindex by π and compare with the pure power.** Put y_j := x̃_{π(j)}. For j ≥ j₀ and every i > j:
   - y_j − y_i ≥ (1 − ε*(π(j))/2)·L(π(j))·(π(j)⁻² − π(i)⁻²), by item 11 H5(i) with a₀ = 1;
   - this is ≥ (1 − ε*(j)/2)·L(j)·(1+2η)⁻³·(j⁻² − i⁻²), by L nondecreasing, ε* nonincreasing and Lemma S.

   For j < j₀ the ratio (y_j − y_i)/(j⁻² − i⁻²) is bounded below by a positive constant (finitely many j). The weights
   satisfy 2x̃_{π(j)} e^{−ℓ_n(π(j))} ≥ c₃ e^{−C″(1+log n)²} j^{−s_n}, with s_n := 4 + C″(1 + log n), using
   π(j) ≤ C_η j for all j. (This holds because π(j) ≤ (1+2η)j for j ≥ j₀, and π(j) ≤ π(j₀) for j < j₀.) The global
   factor costs n·C″(1 + log n)² = O(n log² n). For j < j₀, the positive constant is (y_j − y_{j+1}) j² > 0. Hence

     log D_n(σ) ≥ log D_n(Σ_j j^{−s_n} δ_{j⁻²}) + 2Σ_{j<n}(n−j)[log L(j) + log(1 − ε*(j)/2)]
                  − 3n² log(1+2η) − O(n log² n).

7. **Lemma W** with s = s_n gives log D_n(Σ j^{−s_n}δ_{j⁻²}) ≥ Λ_n − O(n log² n), where Λ_n = −2n² log n + κn² for C = 1.
   The ε* sum is o(n²), since ε* → 0. So liminf (1/n²)[log D_n(σ) − Φ_n] ≥ −3 log(1+2η). Let η → 0. ∎

**Corollary G3′-UL.** Under (SG), log D_n(σ) = Φ_n + o(n²), i.e. (2/n²)Σ(n−j) log(b_j/x_j) → log(π²/16) for the
true-zero measure.

## 5. Proposition N (counting information does not decide G3′) — PROVED-mod-input (Theorem H, p = 2)

Every input to G3′-U is a statement about the counting function: Z1 comes from |N − N₀| = O(log T). The next
proposition shows that no argument using only such information can give the lower bound. Sequences with the same
counting function up to O(1), and repeated values spread at positive density, violate the law.

**Construction.** Fix an integer m ≥ 2 and put φ := 1/m. Define γ^{(m)} from the smooth ordinates by making every m-th
one a double value: γ^{(m)}_{km+2} := γ̃_{km+1} for k ≥ 0, and γ^{(m)}_i := γ̃_i otherwise. This is `merge_repeats`
with idx = 0, m, 2m, … (0-based). Let σ^{(m)} := Σ_i 2x^{(m)}_i δ_{x^{(m)}_i}, with x^{(m)}_i := 1/((γ^{(m)}_i)² + ¼),
indexed with multiplicity as in §1.

**Proposition N.** For every m ≥ 2:
- (i) **Same counting information.** |γ^{(m)}_i − γ̃_i| ≤ γ̃_i − γ̃_{i−1} ≤ 2π/log(γ̃_{i−1}/2π), which tends to 0.
  N^{(m)}(T ± 0) differs from #{i : γ̃_i < T (resp. ≤ T)} by at most 1. So Z1 holds for σ^{(m)} for k ≥ k₁ (with any
  constant > 0 for large k), and every step of G3′-U applies to σ^{(m)}.
- (ii) **The law fails.** log D_n(σ^{(m)}) = Φ_n + 2n² log(1 − φ) + o(n²). Equivalently,
  (2/n²)Σ_{j<n}(n−j) log(b_j/x^{(m)}_j) → log(π²/16) + 2 log(1 − 1/m).

*Proof.*
- (i) Each γ^{(m)}_i is γ̃_i or γ̃_{i−1}. Moving one value down by one place changes counts by at most 1.
- (ii) **Distinct atoms.** The distinct atoms are y_j := x̃_{π(j)}, where π enumerates the 1-based index set
  E := ℕ ∖ {km + 2 : k ≥ 0}. Their weights are 2x̃_{π(j)} or 4x̃_{π(j)}, by the Heine convention of §1. With
  ψ(ξ) := ξm/(m−1), we have |π(j) − ψ(j)| ≤ 1 for all j. Indeed #(E ∩ [1, K]) = K − ⌊(K−2)/m⌋ − 1 for K ≥ 2, so
π(j) − jm/(m−1) lies in [−1, 1].
- (ii-a) **Smooth comparison measure.** Let f(ξ) := 1/(γ(ξ)² + ¼), with γ(ξ) = N₀⁻¹(ξ − ½), so x̃_k = f(k). Put
  z_j := f(ψ(j)) = j⁻²L_z(j), with L_z(ξ) := (1−φ)²L(ψ(ξ)).
  - L_z satisfies (L1)–(L3). The map ψ is linear, ξL_z′/L_z = ε(ψ(ξ)) → 0, and L_z is nondecreasing.
  - The weights 2x̃_{π(j)} or 4x̃_{π(j)} satisfy (Hw) with s = s₀ = 2.
  - Theorem H_L (item 11 §7b) therefore gives
    log D_n(Σ w_j δ_{z_j}) = −2n² log n + 2Σ(n−j) log L_z(j) + κn² + o(n²).
  - Now 2Σ_{j<n}(n−j) log L_z(j) = 2n(n−1) log(1−φ) + 2Σ(n−j) log L(ψ(j)). By H6(a),
    |log L(ψ(j)) − log L(j)| ≤ ε*(j) log(m/(m−1)) → 0, so the last sum is 2Σ(n−j) log L(j) + o(n²). Hence
    log D_n(Σ w_jδ_{z_j}) = Φ_n + 2n² log(1−φ) + o(n²).
- (ii-b) **y against z.** Write h := −f′ > 0. On [1, ∞), h(ξ) ≍ ξ⁻³L(ξ) and (log h)′ = O(1/ξ). For the second
  claim, differentiate directly. With γ = γ(ξ), γ′ = 2π/ℓ and ℓ = log(γ/2π),
  h = 2γγ′/(γ² + ¼)², so (log h)′ = γ′/γ − (γ′/γ)/ℓ − 4γγ′/(γ² + ¼).
  Each term is O(γ′/γ) = O(1/(γℓ)) = O(1/ξ), because ξ = N₀(γ) + ½ ≤ γℓ/2π + O(1) on γ ≥ γ̃_1 > 2π. (The reviewer
  measured ξ(log h)′ ∈ [−2.94, −1.96] on [1, 10¹⁵].) Put u = π(a), v = π(b), u′ = ψ(a), v′ = ψ(b) for a < b, so that
  |u − u′|, |v − v′| ≤ 1. Taking sups over the interval I_u between u and u′ (respectively I_v between v and v′), both of
  which lie in [1, ∞),
  - |∫_{u′}^{v′} h − ∫_u^v h| ≤ sup_{I_u} h + sup_{I_v} h ≤ C h(u);
  - ∫_u^v h ≥ min(v − u, u)·h(2u) ≥ c·min(b − a, a)·h(u).

  So (y_a − y_b)/(z_a − z_b) = 1 + O(1/(b − a) + 1/a), and it is bounded above and below for all pairs. In a Heine
  term with elements k_1 < … < k_n, summing |log ratio| over the partners of k_i gives O(log n + n/i). The total is
  O(n log n), so log D_n(σ^{(m)}) = log D_n(Σ w_jδ_{z_j}) + O(n log n). ∎

**Consequence (stop condition, written up in LOG.md).** G3′-U holds for σ (unconditional) and for every σ^{(m)}. The
lower bound holds for σ under (SG), and fails for σ^{(m)}. Any proof of the lower bound must therefore use information
beyond (C1), for example multiplicity or small-gap information about the actual zeros. *(Heuristic, not proved:* the
lower bound depends on how often repeated or nearly repeated ordinates occur, which the counting function cannot
see.)
- (SG) implies that almost all ordinates are simple values: almost all zeros have horizontal multiplicity H(γ) = 1 in
  the sense of (C3) §1.3, so in particular almost all zeros are simple. A repeated ordinate is not the same as a
  multiple zero, because distinct zeros on one horizontal line also repeat an ordinate. The results surveyed in CITATIONS.md (C3) reach only
  "more than 40.75%" of zeros simple (and on the line) unconditionally, and about 70% under RH. No surveyed result
  reaches proportion one.
- The unconditional lower bound needs inputs beyond (C1) (Prop N). The sufficient input (SG) implies a statement that
  no result surveyed in (C3) reaches. Hardness is not established (GAP N′). G3′ (multiplicity normalization) stops
  at:
  **U (unconditional) + L (mod (SG)) + N (counting information is insufficient)**.

**Not proved (GAP N′, general deletion).** A converse would read: "if the repeated indices of the true ordinates have
positive lower density, the law fails". N′ would show that density-zero repeated ordinates (almost all zeros of
horizontal multiplicity 1, in the sense of (C3) §1.3) is necessary, while G3′-L shows that (SG) is sufficient. This
sandwiches G3′; it is not an equivalence. It needs
a deletion lemma for arbitrary index sets E of positive lower co-density: limsup (1/n²)[log D_n(σ̃|_E) − Φ_n] < 0. Prop
N proves this only for evenly spread E. For clustered E the pairwise comparison used in (ii-b) fails, because
π(b) − π(a) is not comparable to b − a. The numerics in `check_merge.out` [1] cover evenly spread E only; [2] (a
localized defect) shows the shift appears once n exceeds the defect's index scale. This is NUMERICAL only.

## 6. Own-atom normalization (G3′*): exploration, 2026-10-13 — NOT REVIEWED

**Question.** Item 11's Law P is a statement about the atoms of a spectral measure, and those are distinct points.
Normalizing by the measure's own distinct atoms y_1 > y_2 > … (merged weights) gives

  (G3′*)  log D_n(σ) = −2n² log n + 2Σ_{j<n}(n−j) log(j² y_j) + κn² + o(n²).

Exact repeats, whether multiple zeros or symmetric pairs off the line, then become a single atom. Does this remove the
obstruction of §5?

**What is proved.** For the doubled sequences σ^{(m)} of §5, G3′* holds. This is Prop N (ii-a, ii-b) read in own
normalization: z_j = j⁻²L_z(j) with y_j/z_j → 1. So the specific counterexamples of Prop N are artefacts of the
multiplicity normalization. (PROVED-mod-input Theorem H; follows directly from the reviewed proof of N.)

**What the numerics show** (NUMERICAL, `star/check_thinning.out` and `star/check_neardouble.out`):

| Perturbation of the smooth model | Own-normalized shift, n = 250 → 16000 |
|---|---|
| random thinning, keep 50% | ±0.006, near 0 |
| every 2nd index removed in [2^k, 1.5·2^k) | ±0.008, oscillating, small |
| **all** indices removed in [2^k, 1.5·2^k) (log-periodic holes) | −0.03 → −0.08, **not decaying** |
| **all** indices removed in [2^k, 1.8·2^k) | −0.12 → −0.25, **not decaying** |
| near-duplicate atom beside every 4th, gap 0.5 → 10⁻⁵ of the spacing | −0.013 → −0.002, decaying like 1/n |

**Reading.**
- *Microscopic* irregularity is harmless in own normalization: random or interleaved thinning, and near-duplicates
  down to 10⁻⁵ of the spacing.
- *Macroscopic* irregularity breaks the law: an atom density that oscillates log-periodically is not slowly varying, so
  (L2) of H_L fails. The n² constant is then not the linear functional Σ(n−j) log L_y(j).
- Theory suggests near-duplicates matter only when log(1/gap) is comparable to n, i.e. gaps of size e^{−cn}. Below
  that, including both atoms costs less than dropping one. This is a heuristic; the numerics are consistent with it.

**Consequence for an unconditional proof.** In either normalization, the law for the true zeros depends on how
repeated (or super-close) ordinates are distributed:
- *Multiplicity normalization:* repeats must have density 0 (Prop N; necessity would follow from GAP N′).
- *Own normalization:* the proportion of distinct ordinates, N_d(T)/N(T), must vary slowly (no macroscopic
  oscillation). Also, super-close distinct pairs (gaps ≈ e^{−cN}) must not have positive density.

Unconditionally, (C3) gives only N_d(T) ≥ 0.4075·N(T)(1 + o(1)), since distinct zeros that are simple and on the line
have distinct ordinates. Nothing read controls the regularity of N_d/N or the separation of distinct zeros. Even the
local count N(t + h) − N(t) is known only up to O(log t), so zeros are not known to be spread at the scale of the mean
spacing. So **G3′* is not provable unconditionally with the inputs available.** The obstruction moves from
"density-one simplicity" to "regularity of the repeated-ordinate density plus sparse super-close pairs". Both are
statements about the fine distribution of zeros that no surveyed result reaches.

**Thinning.** The deterministic thinning question is settled for index sets with convergent density by Theorem T in
§7. The log-periodic rows of the table above have non-convergent density, which Theorem T excludes. The conditional
results for the true zeros are G3′*-U and G3′*-L in §7.

## 7. Theorem T (thinning) and G3′* for the true zeros — PROVED-mod-input Theorem H, NOT REVIEWED

Notation as in §1. Write f(ξ) := 1/(γ(ξ)² + ¼), so that x̃_k = f(k) = k⁻²L(k), and use item 11's H5(i) with a₀ = 1:

  (1 − ε*(u)/2) L(u) ≤ r(u,v) := (f(u) − f(v))/(u⁻² − v⁻²) ≤ L(u)  for 1 ≤ u < v.

Put c₀ := 1 − sup ε/2 > 0, which holds because sup ε < 2. Let A := A₂ be the constant of item 11's Lemma H7, so that
φ_M(t) ≤ At − 2t² log M.

**Setting T.** Let E ⊂ ℕ be infinite, with increasing enumeration π, and let d(K) := |E ∩ [1, K]|/K.
- Assume d(K) → θ ∈ (0, 1].
- Put y_j := f(π(j)) and L_E(j) := j²y_j = L(π(j))(j/π(j))².
- Let the weights v_j > 0 satisfy (Hw) in the index j: c₁j⁻ˢ ≤ v_j ≤ c₂j⁻²U(j), with U nondecreasing,
  log U = o(j) and Σv_j < ∞.
- Let ν := Σ_j v_j δ_{j⁻²} be the comparison pure power.

**Theorem T.** Under Setting T,

  log D_n(Σ_j v_j δ_{y_j}) = −2n² log n + 2Σ_{j<n}(n−j) log L_E(j) + κn² + o(n²).

That is, own-normalized Law P survives any thinning of convergent density.

**Preliminaries.**
- (P1) π(j)/j → 1/θ, since d(π(j)) = j/π(j).
- (P2) log L_E(j) = log L(π(j)) + 2 log θ + o(1).
- (P3) 2Σ_{j<n}(n−j) log L_E(j) = n² log L_E(n) + o(n²). The proof is as for H6(b): by H6(a),
  |log L(π(n)) − log L(π(j))| ≤ ε*(π(j)) log(π(n)/π(j)), and π(n)/π(j) ≤ Cn/j by (P1).
- (P4) L_E(Mn)/L_E(n) → 1 for fixed M, by H6(a) with π(Mn)/π(n) → M, and by (P1).

**Lemma R (pair factors).** Define F(a,b) := (y_a − y_b)/(L_E(a)(a⁻² − b⁻²)). For ε ∈ (0, ½) there is a_ε such that
for all a_ε ≤ a < b:
- (far, b ≥ (1+ε)a): (1 − ε*(π(a))/2)(1 − ε) ≤ F(a,b) ≤ 1 + ε;
- (near, b < (1+ε)a): F(a,b) ≥ 3c₀θ/16, and F(a,b) ≤ 5εa/(b − a).

*Proof.* Write t := π(b)/π(a) and s := b/a. Then
F = [r(π(a),π(b))/L(π(a))]·[(1 − t⁻²)/(1 − s⁻²)], and the first bracket lies in [1 − ε*(π(a))/2, 1].
- Choose a_ε so that |θπ(j)/j − 1| ≤ ε³/8 for j ≥ a_ε. Then t/s ∈ [1 − ε³/3, 1 + ε³/3].
- *Far.* |t⁻² − s⁻²| ≤ s⁻²·ε³ and 1 − s⁻² ≥ 1 − (1+ε)⁻² ≥ ε. So the second bracket is 1 ± ε².
- *Near, upper.* 1 − t⁻² ≤ 2(t − 1) = 2(π(b) − π(a))/π(a). Also π(b) − π(a) ≤ π(⌈(1+ε)a⌉) − π(a) ≤ 2εa/θ for
  a ≥ a_ε, and 1 − s⁻² ≥ (s − 1)(s + 1)/s² ≥ (8/9)(b − a)/a. So the second bracket is
  ≤ (9/2)·(εa/(b − a))·(a/(θπ(a))) ≤ 5εa/(b − a).
- *Near, lower.* π is strictly increasing and integer-valued, so t − 1 ≥ (b − a)/π(a). Since t ≤ 2,
  1 − t⁻² ≥ (3/4)(t − 1). Also 1 − s⁻² ≤ 2(b − a)/a. So the second bracket is ≥ (3/8)·a/π(a) ≥ 3θ/16. ∎

**Lemma K (concentration, from H7).** Fix M ≥ 2 and put t₀ := A/log M. The Heine terms of ν over index sets S with
|S ∩ (Mn, ∞)| ≥ t₀n sum to ≤ exp(−2n² log n + κn² − (A²/log M)n² + o(n²)). This is a fraction o(1) of D_n(ν).

*Proof.* Item 11's H7 proof, steps 1–6, bounds the sum over S with exactly m tail elements by T_m. With t = m/n it
gives log T_m ≤ −2n² log n + κn² + n²φ_M(t) + o(n²), uniformly in m. For t ≥ t₀,
φ_M(t) ≤ At − 2t² log M ≤ −At ≤ −A²/log M. Summing over the n + 1 values of m costs log(n+1). Theorem H (lower half,
weights ≥ c₁j⁻ˢ) gives log D_n(ν) ≥ −2n² log n + κn² − o(n²). ∎

*Proof of Theorem T, upper bound.* Fix M ≥ 2 and ε. Put λ := L_E(Mn). Define G(j) := j⁻² for j ≤ Mn and G(j) := y_j/λ
for j > Mn. For a_ε ≤ a ≤ Mn, (P1) gives L_E(a) ≤ (1 + ε)λ. Then in a Heine term:
- *Head pair* (b ≤ Mn): y_a − y_b ≤ max(F, 1)(1+ε)λ(G(a) − G(b)).
- *Cross pair* (a ≤ Mn < b): y_a − y_b = (y_a − y_{Mn}) + λ(G(Mn) − G(b)) ≤ max(F(a,Mn), 1)(1+ε)λ(G(a) − G(b)).
- *Tail pair:* exact.
- *a < a_ε:* y_a − y_b ≤ y_a ≤ Bλ(a⁻² − b⁻²), with B depending on a_ε. These cost O(n).

By Lemma R, the far factors cost ≤ log(1 + ε) per pair. For a head element a, the near factors cost
Σ_{m=1}^{⌈εa⌉} log⁺(5εa/m) ≤ 3εa ≤ 3εMn. The cross factors cost the same per tail element. So

  log D_n(y) ≤ n(n−1) log((1+ε)²λ) + C(ε + εM)n² + O(n) + log D_n(Σ v_j δ_{G(j)}).

Item 11's H7 bounds the last term by −2n² log n + κn² + (A²/(8 log M))n² + o(n²), since (Hw) holds. By (P4) and
(P3), n² log λ = 2Σ(n−j) log L_E(j) + o(n²). Let ε → 0, then M → ∞. ∎

*Proof of Theorem T, lower bound.* Fix M and ε. By Lemma K, D_n(y) ≥ Σ_{S ∈ 𝒮} term_y(S), where 𝒮 is the family of
index sets with fewer than t₀n elements beyond Mn, and Σ_𝒮 term_ν(S) ≥ (1 − o(1))D_n(ν). For S = {k_1 < … < k_n} ∈ 𝒮:

  term_y(S) = term_ν(S)·Π_{i<j}[F(k_i, k_j)·L_E(k_i)]².

- **Far pairs.** log F ≥ log(1 − ε*(π(k_i))/2) + log(1 − ε). Since π(k_i) ≥ i and ε* is nonincreasing, these sum to
  ≥ 2Σ(n−i) log(1 − ε*(i)/2) − n² log(1/(1−ε)), which is −o(n²) − O(ε)n².
- **Near pairs.** log F ≥ −C_θ with C_θ := log(16/(3c₀θ)).
  - Pairs whose smaller element is in the head: ≤ Σ_{a ≤ Mn} min(n, εa) ≤ εMn².
  - Pairs with both elements beyond Mn: ≤ (t₀n)².
- **The L_E factors.** L_E(k_i) ≥ (1 − 3ε)L_E(i) for i ≥ a_ε. This uses k_i ≥ i, L∘π nondecreasing and (P1).
- **Small a < a_ε.** inf_{b>a} F(a,b) ≥ (y_a − y_{a+1})a²/L_E(a) > 0, so these cost O(n).

Hence log D_n(y) ≥ log D_n(ν) + 2Σ(n−i) log L_E(i) − [O(ε) + C_θ(εM + A²/log² M)]n² − o(n²). Theorem H (lower half)
gives log D_n(ν) ≥ −2n² log n + κn² − o(n²). Let ε → 0, then M → ∞. ∎

**Remark T′ (robustness).** Suppose d(K) ∈ [θ(1−η), θ(1+η)] for all large K, instead of d → θ. The same proof gives
limsup |log D_n(y) − RHS_E|/n² ≤ ω(η) with ω(η) → 0 as η → 0. Take ε = η^{1/3} in Lemma R: t/s is then within 1 ± 3η,
and the far bracket within 1 ± 3η/ε. Then let M → ∞ slowly as η → 0.

### 7.1 G3′* for the true zeros

- **Setting.** γ*_1 < γ*_2 < … are the distinct ordinates, with multiplicity m_j in the ordinate list of §1.
  k(j) is the index of the first occurrence, so γ*_j = γ_{k(j)}.
- **Atoms and weights.** y_j := 1/(γ*_j² + ¼), with weights 2m_j y_j (the merged measure σ). Then L_y(j) := j²y_j.
- **Counting.** N_d(T) := #{j : γ*_j ≤ T}.

**Hypotheses.**
- **(D∞)** N_d(T)/N(T) → θ ∈ (0, 1].

  Unconditionally liminf N_d/N ≥ 0.4075, because distinct zeros that are simple and on the line have distinct
  ordinates ((C3), PRZD20).
- **(SG\*)** For every η > 0 there is δ > 0 such that the upper density in j of
  B_δ := {j : (γ*_{j+1} − γ*_j)·log(γ*_j/2π)/2π < δ} is at most η.

  Unlike (SG), this concerns gaps between distinct ordinates only. Multiple zeros and repeated ordinates are allowed at
  any density.

**Theorem G3′*-U.** Under (D∞): limsup (1/n²)[log D_n(σ) − Φ*_n] ≤ 0, where
Φ*_n := −2n² log n + 2Σ_{j<n}(n−j) log L_y(j) + κn².

*Proof.* Compare y_j with the smooth thinned atoms ỹ_j := x̃_{k(j)}. The set E := {k(j)} has density
d(K) = N_d(γ_K)/K → θ. This uses (D∞) and K = N(γ_K) + O(log γ_K), from Z1/(C2).
- Z2 at indices k(a) < k(b), with k(b) − k(a) ≥ b − a, gives y_a − y_b ≤ ρ(k(a),k(b))(ỹ_a − ỹ_b). Over head pairs
  (b ≤ Mn) the factors cost O(n log² n), exactly as in G3′-U step 3, because γ̃_{k(Mn)} ≤ γ̃_{CMn}.
- Run the upper-bound proof of Theorem T for ỹ, with the tail of G built from the true atoms: G(j) := y_j/λ_y for
  j > Mn, λ_y := L_y(Mn). Tail pairs are then exact.
- Head and cross pairs take the Z2 factor times the Theorem T factor. λ_y/L̃_E(Mn) = y_{Mn}/ỹ_{Mn} → 1 by Z1′.
- The weights satisfy (Hw): m_j ≤ 2E(γ*_j) = O(log j), which is absorbed into U.
- Finally L_y(j)/L̃_E(j) → 1 by Z1′, so the right-hand sides agree up to o(n²). ∎

**Theorem G3′*-L.** Under (D∞) and (SG*): liminf (1/n²)[log D_n(σ) − Φ*_n] ≥ 0. Hence, under (D∞) and (SG*), the
own-normalized law (2/n²)Σ_{j<n}(n−j) log(b_j/y_j) → log(π²/16) holds.

*Proof.*
1. **Delete the bad set.** Fix η, take δ from (SG*), and delete B_δ. The remaining distinct indices J′ have density in
   J within [1 − η − o(1), 1]. So the index set E′ := k(J′) has density in [θ(1 − η), θ] up to o(1), which is the
   setting of Remark T′.
2. **Restriction.** D_n(σ) ≥ D_n(σ|_{J′}), since all Heine terms are ≥ 0.
3. **Own-atom comparison.** Run the lower-bound proof of Theorem T directly on the true atoms y′ of σ|_{J′}, against
   the pure power, with π′ the enumeration of E′.
   - *Far pairs.* γ*_j = γ_{k(j)} = γ̃_{k(j)} + O(1) by Z1, so y′ = f∘π′·(1 + O(1/γ̃)) in the far-pair ratios. The far
     bounds of Lemma R hold with an extra factor 1 + O(1/γ̃_{π′(a)}). These sum to O(n log² n), as in G3′-U.
   - *Near pairs.* Consecutive elements of J′ are separated by at least the forward gap of the earlier one, which is
     ≥ 2πδ/log(γ/2π). So for near pairs (b < (1+ε)a, in J′-index), γ*_b − γ*_a ≥ (b − a)·2πδ/log(γ*_b/2π). The mean
     spacing of J′-ordinates at height γ is 2π/(θ′ log(γ/2π)) with θ′ ∈ [θ(1−η), θ]. Hence F(a,b) ≥ c(θ)·δ for
     a ≥ a_ε, which is again a bounded loss per near pair. The counting of near pairs (head: ≤ εMn²; deep: ≤ (t₀n)²)
     and Lemma K are unchanged.
   - *Weights.* 2m_j y_j ≥ 2y_j ≥ c j⁻² satisfies the lower half of (Hw).
4. **Back to the full sequence.** This gives log D_n(σ|_{J′}) ≥ −2n² log n + 2Σ(n−j) log(j²y′_j) + κn² − ω(η)n² − o(n²).
   Now y′_j = y_{π_J(j)}, with π_J(j) ≤ (1 + 2η)j eventually. So log(j²y′_j) ≥ log L_y(j) − 2 log(1+2η) − o(1),
   because L_y is slowly varying, by Z1′ and Theorem T's (P2) applied to E. Let η → 0. ∎

**Status of G3′ after §7.**

| Form | Unconditional | Conditional |
|---|---|---|
| multiplicity-normalized (Φ_n) | upper bound (G3′-U) | lower bound under (SG) (G3′-L) |
| own-normalized (Φ*_n) | — | upper under (D∞) (G3′*-U); law under (D∞) + (SG*) (G3′*-L) |

The log-periodic numerics of §6 show that some regularity hypothesis such as (D∞) is genuinely needed for the
own-normalized law (NUMERICAL). Neither (D∞) nor (SG*) is reached by the literature read in CITATIONS.md: (C3) gives
only liminf N_d/N ≥ 0.4075.
