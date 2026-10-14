# G3′: averaged Law P for the true-zero measure

Status: REVIEWED 2026-10-13 (Rule R: `review/REVIEW_G3prime.md`, ACCEPT WITH FIXES; fixes applied) for Z1, Z2, G3′-U,
S, W, G3′-L and N. N′ is proved for d_*(E) > 0 (Plan 16, REVIEWED); the residual case is GAP.
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
| N′ | repeated indices containing a positive-density subset (d_*(E) > 0) ⇒ the law fails, limsup ≤ 2 log(1 − d_*(E)) | PROVED-mod-cite + mod-input Theorem H + REVIEWED; residual GAP: positive lower density with d_*(E) = 0 | G3′*-U proof, Z1, Z2, T (P1), H6 |
| B | unconditional: liminf (1/n²)[log D_n − Φ_n] ≥ −3 log C > −∞, i.e. log D_n = Φ_n + O(n²) (§8.1) | PROVED-mod-cite (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED | GLSS (6.1), Caro–Wei, §4 proof |
| C | PCC (GLSS form, no RH) ⇒ (SG) ⇒ G3′ (§8.2) | PROVED-mod-cite (C1), (C5) + mod-input PCC, Theorem H; REVIEWED | GLSS, G3′-L |
| P | RH + prime short-interval variance (V) ⇒ G3′ (§9.1; corollary of KNOWN (C8) + Theorem C) | PROVED-mod-cite (C8 Thm 7, C8 SPC⇔(9.3) secondary, C8 Thm 4, C5, C1) + mod-input RH, (V), Theorem H; re-check pending | §8.2 |
| R, K | pair factors under thinning; concentration (from H7) | PROVED-mod-input Theorem H + REVIEWED | H5, H7 |
| T | thinning of convergent density: the own-normalized law survives | PROVED-mod-input Theorem H + REVIEWED | R, K, H6, H7 |
| T′ | robustness: density band ±η gives error ω(η) → 0 | PROVED-mod-input Theorem H + REVIEWED | T |
| G3′*-U | own-normalized upper bound under (D∞) | PROVED-mod-cite + mod-input (D∞), Theorem H + REVIEWED | Z2, T |
| G3′*-L | own-normalized law under (D∞) + (SG*) | PROVED-mod-cite + mod-input (D∞), (SG*), Theorem H + REVIEWED | Z1, T′, K |

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
  no result surveyed in (C3) reaches. Theorem N′ below shows that excluding positive-density repeats is necessary, in the sense d_*(E) = 0. G3′ (multiplicity normalization) stops
  at:
  **U (unconditional) + L (mod (SG)) + N (counting information is insufficient) + N′ (d_*(E) = 0 is necessary)**.

**Theorem N′ (positive-density repeats break the law; Plan 16) — PROVED-mod-cite + mod-input Theorem H + REVIEWED
(review/REVIEW_Nprime.md, ACCEPT WITH FIXES, F1–F8 applied).**

*Setting.* Let E := {k ≥ 2 : γ_k = γ_{k−1}} be the set of **repeated indices** of the true ordinates (listed with
multiplicity, §1). For a set A ⊂ ℕ write d(A) := lim |A ∩ [1, K]|/K when the limit exists, and put

  d_*(E) := sup{d(E′) : E′ ⊂ E, d(E′) exists}.

**Theorem N′.** If d_*(E) > 0, then

  limsup_n (1/n²)[log D_n(σ) − Φ_n] ≤ 2 log(1 − d_*(E)) < 0.

So the multiplicity-normalized averaged law (G3′) fails.

*Proof.*
1. **Enlarge.** Fix E′ ⊂ E with 0 < d(E′) = δ′ < 1 (Rule R F5). A set of density δ ∈ (0, 1] contains subsets of
   every density in [0, δ], by the greedy rule of the Remarks. For each k ∈ E ∖ E′, add an atom at γ⁺_k := γ_k + η_k with weight
   2/(γ⁺_k² + ¼).
   - Explicitly (Rule R F4): η_k := min(1, g/2)·i/(m + 1) for the i-th re-added repeat in a block of multiplicity m
     whose forward gap to the next distinct ordinate is g. So 0 < η_k ≤ 1, all atoms are distinct, and their order
     agrees with the index order.
   - Call the result σ⁺. Every atom of σ, with its merged weight, is an atom of σ⁺, so σ ≤ σ⁺ as measures.
   - Every Heine term is nonnegative, so D_n(σ) ≤ D_n(σ⁺).
2. **σ⁺ is a Z1-thinning of convergent density.** The atoms of σ⁺ sit at positions γ⁺_k (γ⁺_k := γ_k for k ∉ E), for
   k in the index set K⁺ := ℕ ∖ E′, with d(K⁺) = 1 − δ′.
   - Z1 holds for these positions with C₀ + 1 (and C₀′ + 1 for all k). Z2 is derived from Z1 alone, so it holds with
     the same change of constant, after re-choosing k₂ so that γ̃_k ≥ 2(C₀ + 1).
   - Weights (Rule R F8): each first-occurrence atom keeps its full merged weight 2m_jy_j, so the re-added mass is
     counted twice. This is harmless. The upper half of (Hw) is weight ≤ 4E(γ)·cx̃_{π(j)} ≤ C log(j+2)·L(Cj)·j⁻²,
     using j ≤ π(j) ≤ Cj. The lower half is weight ≥ 2c⁻¹x̃_{π(j)} ≥ c′j⁻². This is the U(j) of G3′*-U.
3. **G3′*-U for σ⁺.** The proof of Theorem G3′*-U (§7.1) uses only the following:
   - the enumeration k(j) of the atom indices, here K⁺;
   - the convergence of its density, here 1 − δ′ directly, in place of "(D∞) gives d → θ";
   - Z1, Z1′ and Z2 for the atom positions;
   - (Hw).
   So it applies verbatim to σ⁺:

     limsup (1/n²)[log D_n(σ⁺) − Φ*_n(σ⁺)] ≤ 0,  Φ*_n(σ⁺) = −2n² log n + 2Σ_{j<n}(n−j) log L⁺(j) + κn²,

   with L⁺(j) := j²·(j-th atom of σ⁺).
4. **Compare normalizations.**
   - Let π enumerate K⁺. Then π(j)/j → 1/(1 − δ′) (Theorem T (P1)), and L⁺(j) = L(π(j))(j/π(j))²(1 + o(1)) by Z1′.
   - Since π(j) ≤ Cj and L is slowly varying (H6(a)), log L(π(j)) − log L(j) → 0.
   - So log L⁺(j) − log L(j) → 2 log(1 − δ′), and Φ*_n(σ⁺) − Φ_n = 2n² log(1 − δ′) + o(n²).
5. Combining 1–4: limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 2 log(1 − δ′). Let δ′ ↑ d_*(E), with log 0 := −∞. ∎

**Remarks.**
- **Relation to Prop N** (Rule R F3). The proof of N′ uses only three inputs: Z1 for the positions, a multiplicity bound
  m_j = O(log γ), and convergence of d(E′).
  - σ^{(m)} of Prop N has all three: Prop N(i), and multiplicity ≤ 2. Its repeated-index set {km + 2} (written
    ℕ ∖ E in Prop N's notation) has density 1/m.
  - So the same argument gives Prop N's upper half, limsup ≤ 2 log(1 − 1/m). Prop N also gives equality.
  - N′ therefore holds for any ordinate list with Z1 and that multiplicity bound.
- **When is d_*(E) > 0?** For example, when E has positive *window lower density*: there is δ > 0 with
  |E ∩ (K′, K]| ≥ δ(K − K′) − o(K) for all K′ < K.
  - Then the greedy rule "add k ∈ E iff |E′ ∩ [1, k)| < δ′k" with δ′ < δ yields d(E′) = δ′.
  - Plain positive lower density is not enough. Let E := ⋃_m[a_m, 2a_m) with a_{m+1} ≥ 4a_m (Rule R F7), so
    E ∩ [2a_m, 4a_m) = ∅. If E′ ⊂ E had density δ′, then |E′ ∩ [1, 4a_m)| = |E′ ∩ [1, 2a_m)|, which forces
    δ′ = δ′/2. So d_*(E) = 0, although liminf |E ∩ [1, K]|/K > 0.
  - This residual case (positive lower density but d_*(E) = 0) is the only part of the former GAP N′ left open.
    Whether the law fails there is not known either way. *(Heuristic:* it would need a thinning law for oscillating
    densities, which Theorem T excludes; cf. the log-periodic rows of §6.)

**G3′ status after N′ (the sandwich).**
- **(U)** limsup ≤ 0, unconditionally (G3′-U).
- **(L)** liminf ≥ 0 under (SG) (G3′-L).
- **(N′)** If the law holds, then d_*(E) = 0: no positive-density family of repeated ordinates.

A repeated ordinate comes from a multiple zero or from two distinct zeros on one horizontal line.
- The unconditional input surveyed in (C3) gives only N_d(T) ≥ 0.4075·N(T)(1 + o(1)) ((C3), PRZD20 via the survey).
  This uses two steps: simple zeros on the line have pairwise distinct ordinates, so N_d ≥ #(simple, on the line); and
  K ≤ N(γ_K + 0) ≤ K + 2E(γ_K).
- Hence |E ∩ [1, K]| ≤ K − N_d(γ_K) + 1 ≤ 0.5925K(1 + o(1)), which does not exclude d_*(E) > 0.

So an unconditional proof of G3′ must exclude positive-density repeated ordinates, a statement about the fine
structure of the ordinates that no surveyed result reaches. **G3′ closes as: U unconditional; L under (SG); necessity
of d_*(E) = 0 by N′.** "As hard as a known open problem" is still *not* claimed: no surveyed source states "d_*(E) = 0"
as open in this form.

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

| Perturbation of the smooth model | Own-normalized shift | Density d(K) |
|---|---|---|
| random thinning, keep 50% (one seed) | +0.029, +0.022, +0.006 at n = 250–500, then within ±0.01; +0.0045 to +0.0064 for n ≥ 4000, no visible decay | converges (½) |
| every 2nd index removed in [2^k, 1.5·2^k) | +0.013 early, then alternating, with the negative branch −0.004 → −0.008 | oscillates between 2/3 and 3/4 |
| **all** indices removed in [2^k, 1.5·2^k) (log-periodic holes) | −0.03 → −0.08 over n = 250–16000, **not decaying** | oscillates |
| **all** indices removed in [2^k, 1.8·2^k) | −0.12 → −0.25 over n = 250–16000, **not decaying** | oscillates |
| near-duplicate atom beside every 4th, gap 0.5 → 10⁻⁵ of the spacing (n = 250–4000) | −0.013 → −0.002, decaying roughly like n^{−0.3} to n^{−0.6} | converges |

Rule N caveat: check_thinning has no precision or truncation doubling. check_neardouble has d vs ld, which agree.

**Reading.**
- *Convergent density* (random thinning, near-duplicates down to 10⁻⁵ of the spacing): the shift is small, consistent
  with Theorem T (§7), which proves the law in this case.
- *Log-periodically oscillating density*: the shift does not decay. It is small when the oscillation is small (the
  every-2nd row, consistent with the ω(η) of Remark T′) and large for full holes. Such a density is not slowly varying,
  so (L2) of H_L fails, and Theorem T excludes it. (NUMERICAL.)
- Theory suggests near-duplicates matter only when log(1/gap) is comparable to n, i.e. gaps of size e^{−cn}. Below
  that, including both atoms costs less than dropping one. This is a heuristic; the numerics are consistent with it.

**Consequence for an unconditional proof (heuristic and NUMERICAL for the own normalization; for the multiplicity normalization, necessity of d_*(E) = 0 is Theorem N′).** In either
normalization, the law for the true zeros appears to depend on how repeated (or super-close) ordinates are
distributed:
- *Multiplicity normalization:* repeats would need d_*(E) = 0 (Prop N; necessity proved by Theorem N′ in §5).
- *Own normalization:* the proportion of distinct ordinates, N_d(T)/N(T), would need to vary slowly (no macroscopic
  oscillation; smooth-model numerics above), and super-close distinct pairs (gaps ≈ e^{−cN}) would need to be rare.

Unconditionally, (C3) gives only N_d(T) ≥ 0.4075·N(T)(1 + o(1)), since distinct zeros that are simple and on the line
have distinct ordinates. Nothing read controls the regularity of N_d/N or the separation of distinct zeros. (C1) gives the
local count N(t + h) − N(t) only up to O(log t), so the inputs read do not show that zeros are spread at the scale of the
mean spacing. **An unconditional proof of G3′* is not obtained here: the inputs read do not supply (D∞) or (SG*)** (§7). The obstruction moves from
"density-one simplicity" to "regularity of the repeated-ordinate density plus sparse super-close pairs". Both are
statements about the fine distribution of zeros that no surveyed result reaches.

**Thinning.** The deterministic thinning question is settled for index sets with convergent density by Theorem T in
§7. The log-periodic rows of the table above have non-convergent density, which Theorem T excludes. The conditional
results for the true zeros are G3′*-U and G3′*-L in §7.

## 7. Theorem T (thinning) and G3′* for the true zeros — PROVED-mod-input Theorem H (via item 11 H5, H6, H7)

Rule R: `review/REVIEW_T.md`. Theorem T, Lemmas R and K, Remark T′ and G3′*-U are ACCEPT WITH FIXES, fixes applied, so
REVIEWED. G3′*-L was REJECTED as first written (order-of-limits gap). It was repaired by a two-scale split, then
re-reviewed: ACCEPT WITH FIXES, fixes applied, so REVIEWED.

Notation as in §1. Write f(ξ) := 1/(γ(ξ)² + ¼), so that x̃_k = f(k) = k⁻²L(k), and use item 11's H5(i) with a₀ = 1:

  (1 − ε*(u)/2) L(u) ≤ r(u,v) := (f(u) − f(v))/(u⁻² − v⁻²) ≤ L(u)  for 1 ≤ u < v.

Put c₀ := 1 − sup ε/2 > 0, which holds because sup ε < 2. Theorem T is stated for this specific f: (L1)–(L3) with
a₀ = 1 and sup ε < 2. Let A := A₂ be the constant of item 11's Lemma H7, so that
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
  |log L(π(n)) − log L(π(j))| ≤ ε*(π(j)) log(π(n)/π(j)), and π(n)/π(j) ≤ C′n/j, using π(j) ≥ j and π(n) ≤ C′n from (P1).
- (P4) L_E(Mn)/L_E(n) → 1 for fixed M, by H6(a) with π(Mn)/π(n) → M, and by (P1).

**Lemma R (pair factors).** Define F(a,b) := (y_a − y_b)/(L_E(a)(a⁻² − b⁻²)). For ε ∈ (0, ½) there is a_ε such that
for all a_ε ≤ a < b:
- (far, b ≥ (1+ε)a): (1 − ε*(π(a))/2)(1 − ε) ≤ F(a,b) ≤ 1 + ε;
- (near, b < (1+ε)a): F(a,b) ≥ 3c₀θ/16, and F(a,b) ≤ 5εa/(b − a).

*Proof.* Write t := π(b)/π(a) and s := b/a. Then
F = [r(π(a),π(b))/L(π(a))]·[(1 − t⁻²)/(1 − s⁻²)], and the first bracket lies in [1 − ε*(π(a))/2, 1].
- Choose a_ε ≥ 2/ε so that |θπ(j)/j − 1| ≤ ε³/8 for j ≥ a_ε. Then t/s ∈ [1 − ε³/3, 1 + ε³/3]. The condition
  a_ε ≥ 2/ε absorbs the ceiling and the additive (1+ε³/8)/θ term in the near-upper step.
- *Far.* |t⁻² − s⁻²| ≤ s⁻²·ε³ and 1 − s⁻² ≥ 1 − (1+ε)⁻² ≥ ε. So the second bracket is 1 ± ε².
- *Near, upper.* 1 − t⁻² ≤ 2(t − 1) = 2(π(b) − π(a))/π(a). Also π(b) − π(a) ≤ π(⌈(1+ε)a⌉) − π(a) ≤ 2εa/θ for
  a ≥ a_ε, and 1 − s⁻² ≥ (s − 1)(s + 1)/s² ≥ (8/9)(b − a)/a. So the second bracket is
  ≤ (9/2)·(εa/(b − a))·(a/(θπ(a))) ≤ 5εa/(b − a).
- *Near, lower.* π is strictly increasing and integer-valued, so t − 1 ≥ (b − a)/π(a). Since t ≤ 2,
  1 − t⁻² ≥ (3/4)(t − 1). Also 1 − s⁻² ≤ 2(b − a)/a. So the second bracket is ≥ (3/8)·a/π(a) ≥ 3θ/16. ∎

**Lemma K (concentration, from H7).** Assume both halves of (Hw), since this is H7. Fix M ≥ 2 and put
t₀ := A/log M. (When t₀ ≥ 1 the statement is vacuous; this is harmless because M → ∞ later.) The Heine terms of ν over index sets S with
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

By Lemma R, the far factors cost ≤ log(1 + ε) per pair, doubled for squares. For a head element a, the near partners
have distinct m = b − a < εa, so they cost Σ_{m<εa} log⁺(5εa/m) ≤ (1 + log 5)εa ≤ 3εa ≤ 3εMn. For a fixed tail element
b, its cross partners a are distinct, with distinct Mn − a, and F(a,Mn) ≤ 5εMn/(Mn − a). So they cost the same. Hence

  log D_n(y) ≤ n(n−1) log((1+ε)²λ) + C(ε + εM)n² + O(n) + log D_n(Σ v_j δ_{G(j)}).

Item 11's H7 bounds the last term by −2n² log n + κn² + (A²/(8 log M))n² + o(n²), since (Hw) holds. By (P4) and
(P3), n² log λ = 2Σ(n−j) log L_E(j) + o(n²), and n log λ = o(n²). Let ε → 0, then M → ∞. ∎

*Proof of Theorem T, lower bound.* Fix M and ε. By Lemma K, D_n(y) ≥ Σ_{S ∈ 𝒮} term_y(S), where 𝒮 is the family of
index sets with fewer than t₀n elements beyond Mn, and Σ_𝒮 term_ν(S) ≥ (1 − o(1))D_n(ν). For S = {k_1 < … < k_n} ∈ 𝒮:

  term_y(S) = term_ν(S)·Π_{i<j}[F(k_i, k_j)·L_E(k_i)]².

- **Far pairs.** log F ≥ log(1 − ε*(π(k_i))/2) + log(1 − ε). Since π(k_i) ≥ i and ε* is nonincreasing, these sum to
  ≥ 2Σ(n−i) log(1 − ε*(i)/2) − n² log(1/(1−ε)), which is −o(n²) − O(ε)n².
- **Near pairs.** log F ≥ −C_θ with C_θ := log(16/(3c₀θ)).
  - Pairs whose smaller element is in the head: ≤ Σ_{a∈S, a≤Mn} min(n, εa) ≤ n·min(n, εMn) ≤ εMn².
  - Pairs with both elements beyond Mn: ≤ (t₀n)².
- **The L_E factors.** L_E(k_i) ≥ (1 − 3ε)L_E(i) for i ≥ a_ε. This uses k_i ≥ i, L∘π nondecreasing and (P1).
- **Small a < a_ε.** inf_{b>a} F(a,b) ≥ (y_a − y_{a+1})a²/L_E(a) > 0, and L_E(k_i) ≥ inf L_E > 0 for i < a_ε. So
  these cost O(n).

Hence log D_n(y) ≥ log D_n(ν) + 2Σ(n−i) log L_E(i) − [O(ε) + 2C_θ(εM + A²/log² M)]n² − o(n²). Theorem H (lower half)
gives log D_n(ν) ≥ −2n² log n + κn² − o(n²). Let ε → 0, then M → ∞. ∎

**Remark T′ (robustness).** Suppose d(K) ∈ [θ(1−η), θ(1+η)] for all large K, instead of d → θ. Write
RHS_E := −2n² log n + 2Σ_{j<n}(n−j) log L_E(j) + κn². Then

  limsup |log D_n(y) − RHS_E|/n² ≤ ω(η) := inf_M [C(η^{1/3}M + A²/log² M)(1 + C_θ) + Cη],

which tends to 0 as η → 0.

*Proof.* Lemma R uses only |θπ(j)/j − 1| ≤ ε³/8 for j ≥ a_ε. Under the band hypothesis this holds with
ε := (8η/(1−η))^{1/3} ≍ 2η^{1/3}, so Lemma R holds verbatim. Three things change:
1. (P1) becomes the two-sided bound π(j)/j ∈ [1/(θ(1+η)), 1/(θ(1−η))] for large j.
2. (P3) and (P4) hold up to ±O(η)n², because log(j/π(j))² oscillates within ±2 log((1+η)/(1−η)). H6(a) still gives
   L(π(Mn))/L(π(n)) → 1.
3. In both bounds, ε is now tied to η.

What makes ω(η) → 0 is that C_θ does not depend on η. Any use of Remark T′ in which the per-pair near loss depends on η
must re-check this.

### 7.1 G3′* for the true zeros

- **Setting.** γ*_1 < γ*_2 < … are the distinct ordinates, with multiplicity m_j in the ordinate list of §1.
  k(j) is the index of the first occurrence, so γ*_j = γ_{k(j)}.
- **Atoms and weights.** y_j := 1/(γ*_j² + ¼), with weights 2m_j y_j (the merged measure σ). Then L_y(j) := j²y_j.
- **Counting.** N_d(T) := #{j : γ*_j ≤ T}.

**Hypotheses.**
- **(D∞)** N_d(T)/N(T) → θ ∈ (0, 1].

  Unconditionally liminf N_d/N ≥ 0.4075, because distinct zeros that are simple and on the line have distinct
  ordinates ((C3), PRZD20). The proportion is meant in the usual liminf_T N*(T)/N(T) sense; that convention comes from
  the secondary source.
- **(SG\*)** For every η > 0 there is δ > 0 such that the upper density in j of
  B_δ := {j : (γ*_{j+1} − γ*_j)·log(γ*_j/2π)/2π < δ} is at most η.

  Unlike (SG), this concerns gaps between distinct ordinates only. Multiple zeros and repeated ordinates are allowed at
  any density.

**Theorem G3′*-U.** Under (D∞): limsup (1/n²)[log D_n(σ) − Φ*_n] ≤ 0, where
Φ*_n := −2n² log n + 2Σ_{j<n}(n−j) log L_y(j) + κn².

*Proof.* Compare y_j with the smooth thinned atoms ỹ_j := x̃_{k(j)}.
- **Density of E.** E := {k(j)} has density exactly d(K) = N_d(γ_K)/K. Since K ≤ N(γ_K) ≤ K + 2E(γ_K) (the Z1
  multiplicity bound), (D∞) gives d → θ.
- **Z2 factors.** Z2 at indices k(a) < k(b), with k(b) − k(a) ≥ b − a and k(j) ≤ Cj, gives
  y_a − y_b ≤ ρ(k(a),k(b))(ỹ_a − ỹ_b).
  - Head pairs (b ≤ Mn): the factors cost O(n log² n), exactly as in G3′-U step 3.
  - Cross pairs (a ≤ Mn < b): the factor ρ(k(a), k(Mn)) is shared over the tail partners and costed as in G3′-U
    step 3, bullet 2.
- **Theorem T step.** Run the upper-bound proof of Theorem T for ỹ, with the tail of G built from the true atoms:
  G(j) := y_j/λ_y for j > Mn, with λ_y := L_y(Mn). Tail pairs are then exact. Head and cross pairs take the Z2 factor
  times the Theorem T factor, against Λ := max((1+ε)L̃_E(Mn), λ_y). Also λ_y/L̃_E(Mn) = y_{Mn}/ỹ_{Mn} → 1 by Z1′.
- **Weights (Hw).** The multiplicity m_j is not monotone, so take U(j) := C log(j+2)·L(Cj). This is nondecreasing,
  with log U = O(log log j). Use m_j ≤ 2E(γ*_j) for γ*_j ≥ e (finitely many small j only change constants), and
  L_y(j) ≤ cL̃_E(j) ≤ c′L(Cj). Both halves of (Hw) hold, which Lemma K also needs.
- **Right-hand sides.** L_y(j)/L̃_E(j) → 1 by Z1′, so the right-hand sides agree up to o(n²). ∎

**Theorem G3′*-L.** Under (D∞) and (SG*): liminf (1/n²)[log D_n(σ) − Φ*_n] ≥ 0. Hence, under (D∞) and (SG*), the
own-normalized law (2/n²)Σ_{j<n}(n−j) log(b_j/y_j) → log(π²/16) holds. *(Repaired after the first Rule R pass;
ACCEPT WITH FIXES on re-review; REVIEWED.)*

*Proof.*
1. **Delete the bad set.** Fix η, take δ = δ(η) from (SG*), and delete B_δ. The remaining distinct indices J′ have
   density in J within [1 − η − o(1), 1]. So E′ := k(J′) has density in [θ(1−η), θ] up to o(1). This is the band
   hypothesis of Remark T′, centred at θ(1 − η/2), with ε ≍ η^{1/3} forced. Let π′ enumerate E′, and let y′ be the
   true atoms of σ|_{J′}, indexed by J′-rank.
2. **Restriction.** D_n(σ) ≥ D_n(σ|_{J′}), since all Heine terms are ≥ 0. Fix M₁ < M₂. By Lemma K applied at both M₁
   and M₂ (a union bound), the reference sum over 𝒮 := {S : |S ∩ (M₁n, ∞)| < t₀(M₁)n and
   |S ∩ (M₂n, ∞)| < t₀(M₂)n} is ≥ (1 − o(1))D_n(ν). Both halves of (Hw) hold, by the weights bullet of G3′*-U.
3. **Pair factors against the pure power at the J′-rank.**
   - *Far pairs* (b ≥ (1+ε)a). The atoms are within 1 + O(1/γ̃). The ratio is controlled by the lower analogue of Z2
     (§4 step 3): the difference factor 1 − 2C₀/(γ̃_{π′(b)} − γ̃_{π′(a)}) ≥ 1 − O(1/(εγ̃_{π′(a)})), together with the
     sum and denominator factors ≥ (1 + 2C₀/γ̃)⁻⁵. The far bounds of Lemma R (from Remark T′) thus hold up to these
     factors, whose total is O_ε(n log² n).
   - *Near pairs* (b < (1+ε)a) are split by the smooth ordinate distance.
     - *Near-long* (γ̃_{π′(b)} − γ̃_{π′(a)} ≥ 4C₀): by Z1 the true difference is ≥ ½ the smooth one. With the lower-Z2
       factors, F_true ≥ ½(1 − o(1))·3c₀θ′/16. This is a **δ-free** bounded loss. These pairs are counted as in
       Theorem T at scale M₁: ≤ ε M₁n² + (t₀(M₁)n)².
     - *Near-short* (γ̃_{π′(b)} − γ̃_{π′(a)} < 4C₀): these have b − a ≤ C log π′(a). Write γ_A := γ*_{π_J(a)} = γ_{π′(a)} and
       γ_B := γ*_{π_J(b)} = γ_{π′(b)}, since a and b are J′-ranks. Consecutive J′-elements are separated by at least the forward gap of the earlier one, so
       γ_B − γ_A ≥ (b − a)·2πδ/log(γ_B/2π). Then:
       - y′_a − y′_b ≥ (γ_B − γ_A)·2γ_A/(γ_B² + ¼)², with γ_B/γ_A ≤ 2;
       - a⁻² − b⁻² ≤ 2(b − a)/a³;
       - a ≍ θ′N(γ_A) ≍ θ′γ_A log(γ_A/2π)/2π, with θ′ ∈ [θ(1−η), θ];
       - L_{y′}(a) = a²y′_a ≍ a²/γ_A².

       So F ≥ c·θ′δ, and the loss is ≤ log(1/(cθ′δ)) per pair. (π′(a) ≥ N(γ_A − 0) ≍ γ_A log(γ_A/2π)/2π by Z1/(C1),
       and a ≥ θ(1−η)(1−o(1))π′(a).)
       - Pairs with a ≤ M₂n: at most C log(M₂n) such pairs per element, so ≤ n·C log(M₂n) = o(n²) in total.
       - Pairs with a > M₂n: both elements lie beyond M₂n, so there are ≤ (t₀(M₂)n)² on 𝒮.
   - *Weights.* 2m_j y_j ≥ 2y_j ≥ c j⁻², the lower half of (Hw).
   - *Normalization.* F_true is normalised by L_{y′}(a), whereas Lemma R uses L_{E′}(a) = a²x̃_{π′(a)}. Their ratio is
     x̃_{π′(a)}/x_{π′(a)} → 1 by Z1′. It is absorbed in the (1 − o(1)) factors and in the o(n²) of step 4.
4. **Collect the losses.**

     log D_n(σ|_{J′}) ≥ −2n² log n + 2Σ(n−j) log L_{y′}(j) + κn²
                        − [ω₁(η, M₁) + log(1/(cθδ))·t₀(M₂)²] n² − o(n²),

   with ω₁(η, M₁) := C(η^{1/3}M₁ + A²/log² M₁)(1 + C_θ) + Cη. Here C_θ := log(32/(3c₀θ′)), using θ′ ≥ θ/2, is the
   near-long constant (with the extra ½). It depends on neither η nor δ, so ω₁ is δ-free. **Order of limits:** n → ∞; then
   M₂ → ∞, which kills the δ-dependent term for fixed η; then minimise over M₁; then η → 0.
5. **Back to the full sequence.** Only the "≥" direction is needed. y′_j = y_{π_J(j)} with π_J(j) ≤ (1 + 2η)j
   eventually. So log(j²y′_j) ≥ log L_y(π_J(j)) − 2 log(1+2η). Also L_y(π_J(j))/L_y(j) ≥ 1 − o(1), because L∘k is
   nondecreasing, j/k(j) → θ, and Z1′. Let η → 0. ∎

**Status of G3′ after §7.**

| Form | Unconditional | Conditional |
|---|---|---|
| multiplicity-normalized (Φ_n) | upper bound (G3′-U), REVIEWED | lower bound under (SG) (G3′-L), REVIEWED |
| own-normalized (Φ*_n) | — | upper under (D∞) (G3′*-U), REVIEWED; law under (D∞) + (SG*) (G3′*-L), REVIEWED |

The log-periodic numerics of §6 suggest (NUMERICAL, smooth model) that some regularity hypothesis such as (D∞) is
needed for the own-normalized law. Neither (D∞) nor (SG*) is reached by the literature read in CITATIONS.md: (C3) gives
only liminf N_d/N ≥ 0.4075.

## 8. Plan 17: an unconditional bounded defect, and the pair-correlation conditional — REVIEWED (review/REVIEW_Plan17.md: ACCEPT WITH FIXES, then re-check ACCEPT; F1 via Fix A, F2–F9, N1–N2 applied)

Inputs: GLSS (C5) and, for context, Lamzouri (C6), both read 2026-10-14. Notation is as in §§1–7. L(T) := (1/2π)log T.
"Normalized distance" between ordinates γ, γ′ ∈ (T, 2T] means |γ − γ′|L(2T). Zeros are counted with multiplicity
(the multiset Z), and H(γ) is the horizontal multiplicity of GLSS (7.1).

### 8.1 Theorem B (unconditional): the averaged law holds up to a bounded constant

**Theorem B.** There is a constant C ≥ 1 with

  liminf_n (1/n²)[log D_n(σ) − Φ_n] ≥ −3 log C.

Equivalently, liminf ≥ 2 log θ₀ with θ₀ := C^{−3/2} ∈ (0, 1]. Together with G3′-U, log D_n(σ) = Φ_n + O(n²)
**unconditionally**. In b_j-form, (2/n²)Σ_{j<n}(n−j)log(b_j/x̃_j) stays within a bounded distance of log(π²/16) for all
large n.

C = 2/c₀ + 1, where c₀ comes from the O-constant of GLSS (6.1) (Fujii's second moment). That constant is not explicit,
so C is not computed here (Remark B3).

*Proof.*
1. **Pairs on a dyadic block** (Rule R F2). Apply GLSS (6.1) with λ := 2 at height 2T only.
   - Pairs with γ, γ′ ∈ (T, 2T] are among the pairs counted there.
   - A pair with |γ′ − γ|L(2T) ≤ 1 has weight ≥ ½.
   - So the number P_T of ordered pairs (ρ, ρ′) with γ, γ′ ∈ (T, 2T] and |γ − γ′|L(2T) ≤ 1 satisfies
     P_T ≤ 2·2TL(2T)(2 + log 4/(2π²) + O(1)) ≤ A·M_T for large T.
   - Here M_T := N(2T) − N(T) ~ TL(2T) (C1), and A is an absolute constant.
   - P_T includes ρ = ρ′, pairs on one horizontal line, and off-line pairs.
2. **Many distinct ordinates.** Let V_T be the set of distinct ordinates in (T, 2T], with horizontal multiplicities H(v)
   (GLSS (7.1)). Then Σ_v H(v) = M_T and Σ_v H(v)² ≤ P_T, since pairs on one horizontal line have distance 0. By
   Cauchy–Schwarz, |V_T| ≥ M_T²/Σ H² ≥ M_T/A.
3. **A separated subset.** Let G_T be the graph on V_T with an edge between distinct ordinates at distance ≤ 1/L(2T).
   - Each edge accounts for ≥ 2 ordered zero-pairs counted in P_T, so |E(G_T)| ≤ P_T/2.
   - Caro–Wei: G_T has an independent set I_T with |I_T| ≥ Σ_v 1/(1 + deg v) ≥ |V_T|²/(|V_T| + 2|E|) ≥ M_T/(A²(A + 1)).
   - Delete from I_T the elements within 1/L(2T) of T or 2T; by (C1) there are O(log T) of them.
   - S := ⋃_{dyadic T} I_T is a set of distinct ordinates with |S ∩ (T, 2T]| ≥ 2c₀M_T for large T, where
     c₀ := 1/(4A²(A + 1)).
   - Two elements of S at heights in [T, 4T] are more than 1/L(4T) apart. So for γ < γ′ in S,
     γ′ − γ ≥ (½ + o(1))·2π/log(γ/2π).
4. **Index bound** (Rule R F1, Fix A). Index the zeros with multiplicity, k = 1, 2, … (§1). Let E be the set of
   first-occurrence indices of the ordinates in S, enumerated increasingly by π.
   - Let K be large, and let 2^m T₀ be the largest dyadic level with N(2^mT₀) ≤ K. Then |E ∩ [1, K]| ≥ 2c₀(N(2^mT₀) − N(2^{m−1}T₀))(1 + o(1)).
     By (C1), N(2^mT₀) − N(2^{m−1}T₀) ≥ (½ − o(1))N(2^mT₀), and N(2^{m+1}T₀) ≤ (2 + o(1))N(2^mT₀), so N(2^mT₀) ≥ (½ − o(1))K.
   - Hence |E ∩ [1, K]| ≥ (c₀/2 − o(1))K, i.e. there is j₀ with π(j) ≤ Cj for all j ≥ j₀, with C := 2/c₀ + 1.
   - This is only a *lower density* bound. No convergence is claimed; Rule R F1 shows that a Caro–Wei set need not have
     a convergent density.
5. **Run the proof of Theorem G3′-L (§4) on E**, with these changes:
   - **Step 1:** the good set is E (not {g_k ≥ δ}), with π(j) ≤ Cj in place of π(j) ≤ (1+2η)j.
   - **Step 3 (near pairs):** first drop the finitely many elements of E below k₂, or where the o(1) of Step 3
     exceeds ¼ (Rule R N1). Then for a < b in E, γ_b − γ_a ≥ ¼·2π/log(γ_a/2π). This is §4's bound with the fixed
     δ := ¼, so the near-pair ratio and the count O(log γ̃_a) of near partners are unchanged. Far pairs are unchanged.
   - **Steps 4–5** are unchanged.
   - **Step 6:** Lemma S with 1 + η := C gives π(j)⁻² − π(i)⁻² ≥ C⁻³(j⁻² − i⁻²) for i > j ≥ j₀. Also L(π(j)) ≥ L(j)
     (L nondecreasing, π(j) ≥ j), and the weight bound uses π(j) ≤ C_E j for all j (C_E := max(C, π(j₀))). So the term
     −3n²log(1+2η) becomes −3n²log C.
   - **Step 7** is unchanged (Lemma W, ε* → 0).

   Hence liminf (1/n²)[log D_n(σ) − Φ_n] ≥ −3 log C. Monotonicity is built in (§4 Step 2: D_n(σ) ≥ Σ_{S⊂E} term).
   This reuses the reviewed §4 proof with one constant changed. ∎

**Remarks.**
- **B1 (what is new).** Before Plan 17 the lower bound for the true zeros was only conditional (G3′-L under (SG);
  G3′*-L under (D∞) + (SG*)). Theorem B uses only unconditional inputs: GLSS (6.1), i.e. Gallagher–Mueller plus
  Fujii's second moment of S(t + U) − S(t) (Selberg's method; secondary statement, (C5)), and (C1).
- **B2 (defect interval).** Let D := liminf (1/n²)[log D_n − Φ_n]. Unconditionally, D ∈ [−3 log C, 0] = [2 log θ₀, 0].
  - N′ forces D ≤ 2 log(1 − d_*(E_rep)) < 0 if repeats contain a positive-density family.
  - G3′ is the statement D = 0, together with the limsup, which is ≤ 0 by G3′-U.
- **B3 (the constant).**
  - An explicit C needs an explicit O-constant in Fujii's second moment, which is not in what we read.
  - The −3 log C comes from Lemma S's crude index-shift bound. The thinning argument of §7 would give 2 log(density)
    instead, but it needs a convergent density, which Caro–Wei does not provide (F1).
  - Lamzouri's (C6) proportions (≥ 0.6725 simple and on the line) control repeats, not close-but-distinct pairs. A
    sharper B would combine them with a convergent-density selection. (Optional.)

### 8.2 Theorem C (conditional, no RH): pair correlation implies G3′

**Theorem C.** Assume Montgomery's pair-correlation conjecture in the form of GLSS (C5), which concerns vertical
distances only and assumes no RH. Then (SG) of §4 holds, and hence (G3′-L and G3′-U) log D_n(σ) = Φ_n + o(n²): the
multiplicity-normalized averaged law holds for the true zeros.

*Proof.* Let g_k be the normalized gaps of §4 (consecutive ordinates with multiplicity; g_k = 0 at repeats). Fix
δ ∈ (0, 1).
- **Repeats.** GLSS Theorem 1's proof shows that PCC implies N^⊛(T) = TL + o(TL), i.e. HMH. Then
  #{k ≤ N(T) : g_k = 0} = Σ_{distinct lines}(H − 1) ≤ Σ_ρ(H(γ) − 1) = N^⊛(T) − N(T) = o(TL), using N(T) = TL + o(TL)
  (GLSS (3.7)). So repeats have density 0.
- **Small positive gaps** (Rule R F5). Fix R > 1. Indices k with γ_k ≤ T/R number ≤ N(T/R) ≤ (1/R + o(1))N(T).
  - For γ_k ∈ (T/R, T], log(γ_k/2π)/2π ≥ L(T)(1 − log R/log T − o(1)). So 0 < g_k < δ implies
    0 < (γ_{k+1} − γ_k)L(T) ≤ 2δ for large T.
  - These pairs (ρ_k, ρ_{k+1}) are distinct for distinct k. So #{k ≤ N(T) : 0 < g_k < δ, γ_k > T/R} ≤ N(2δ).
  - PCC at the fixed λ = 2δ gives N(2δ) = TL∫_0^{2δ}(1 − (sin πα/πα)²)dα + o(TL) ≤ (8π²/9)δ³TL + o(TL), since
    1 − (sin x/x)² ≤ x²/3.
- With K = N(T) (indices and heights correspond via (C1)), #{k ≤ K : g_k < δ} ≤ (1/R + (8π²/9)δ³ + o(1))K.
  Given η > 0, take R := 3/η and δ := (3η/(8π²))^{1/3}, so that the bound is ≤ (2η/3 + o(1))K ≤ ηK for K ≥ K₀.
  This is (SG) (Rule R N2). ∎

**Remarks.**
- **C1.** By GLSS Theorem 1, PCC also gives 100% simple and critical zeros, consistent with N′'s necessary condition
  (d_*(E) = 0).
- **C2 (framing, AGENTS.md).** Theorem C is an implication from a stated conjecture about the vertical distribution of
  zeros. It assumes nothing about their horizontal location, and it is not evidence for or against any conjecture.

### 8.3 G3′ status after Plan 17

| Statement | Status |
|---|---|
| limsup (1/n²)[log D_n − Φ_n] ≤ 0 | unconditional (G3′-U), REVIEWED |
| liminf ≥ −3 log C > −∞ | **unconditional (Theorem B)**, mod-input Theorem H; REVIEWED |
| liminf ≥ 0, i.e. G3′ | under (SG) (G3′-L), REVIEWED; under PCC (Theorem C, no RH), mod-input Theorem H; REVIEWED |
| G3′ ⇒ d_*(E) = 0 | N′, REVIEWED |
| G3′ under RH + prime variance (V) | Corollary P (§9.1), re-check pending |

## 9. Plan 18: from prime pairs to Law P (the primes–zeros duality) — Rule R ACCEPT WITH FIXES (review/REVIEW_Plan18.md); F1–F12 applied, re-check pending

Inputs: (C7) Montgomery–Soundararajan, (C8) Goldston's notes, (C9) MRT, together with §8 (Theorem C). RH enters
**only as a stated hypothesis** of conditional results (AGENTS.md rule 3).

### 9.1 Corollary P (prime variance ⇒ Law P for the true zeros)

**Corollary P.** Assume RH and

  (V) ∫_1^X(ψ(x + h) − ψ(x) − h)²dx ∼ hX log(X/h), uniformly for 1 ≤ h ≤ X^{1−ε}, for every ε > 0.

Then log D_n(σ) = Φ_n + o(n²). Equivalently, (2/n²)Σ_{j<n}(n−j)log(b_j/x̃_j) → log(π²/16) for the true-zero measure.

- (C8, footnote 6, a secondary claim about how the hypotheses relate: "If (9.3) holds for this range of h it implies
  RH." So RH is formally redundant beside (V). It is kept because the cited equivalences are stated on RH.)
- **Novelty.** RH + (V) ⇒ PCC is KNOWN: Goldston–Montgomery with Goldston's Theorem 4 (C8, also cited in C7). The only
  new step is composing it with Theorem C. Label: corollary; novelty UNCHECKED.

*Proof.*
1. **(V) ⇒ SPC.** Goldston–Montgomery (C8 Theorem 7, converse direction, RH assumed): (9.1) for
   X^{−1/A₁}(log x)^{−3} ≤ δ ≤ X^{−1/A₂}(log x)³ gives F(x, T) ∼ (T/2π)log T for T^{A₁} ≤ X ≤ T^{A₂}.
   - With A₁ = 1 and A₂ = M, the δ-range is covered by (V) once ε < 1/M.
   - The passage between the h-form (9.3) = (V) and the δ-form (9.1) (Saffari–Vaughan) is **only stated** in C8, so it
     is a secondary step (Rule R F5).
   - Hence F(α) = 1 + o(1) on 1 ≤ α ≤ M for every M: this is SPC.
2. **SPC ⇒ PCC** by (C8) Theorem 4. Goldston's PCC (fixed β, forward pairs 0 < γ′ − γ ≤ 2πβ/log T = β/L, normalization
   T log T/2π = TL, with multiplicity) is GLSS's N(β) = TL∫_0^β(1 − sinc²) + o(TL). On RH the zero sets coincide.
   - **Uniformity on [β₀, β₁]** (written out, Rule R F6). N(T, ·)/TL is nondecreasing, and the limit P(β) is continuous
     and nondecreasing.
   - Given ε, take a grid β₀ = t₀ < … < t_m = β₁ with P(t_{i+1}) − P(t_i) < ε, and T large so that every grid point
     is within ε.
   - For β ∈ [t_i, t_{i+1}]: N(β)/TL − P(β) ≤ N(t_{i+1})/TL − P(t_i) < 2ε, and symmetrically ≥ −2ε.
3. **PCC ⇒ (SG) ⇒ G3′:** Theorem C (§8.2), then G3′-L and G3′-U. ∎

### 9.2 Remarks P′ (prime-pair inputs: what the known routes give)

**(a) Pointwise Hardy–Littlewood pairs (KNOWN, with a remark).** Assume RH and the pair conjecture
Σ_{n≤N}Λ(n)Λ(n + k) = S(k)N + O(N^{1/2+ε}), uniformly in 0 < k ≤ N. (Both C8 §9 and C7 Theorem 3 use RH, which is
C7's k = 1 case.)
- The known route (C8 §9) then gives (V) for h ≤ X^{1/2−ε}, hence SPC on 1 ≤ α ≤ 2 − ε. Compare C7 Theorem 3 with
  K = 2, whose effective range is H ≤ N^{1/2−ε}.
- *Remark (route, not impossibility; Rule R F2).* The standard kernel method (Goldston Thm 4) uses F(α) on every
  bounded α-range to get PCC. With F known only on [0, 2 − ε], it does not give N(T, β) → 0 as β → 0, and so does not
  give (SG). Whether some other method could is not addressed.
- F on [0, 2 − ε] would give *conditional* improvements of simple-zero proportions and a conditional analogue of
  Theorem B's constant. These are not carried out (Rule R F10).

**(b) Averaged prime pairs: heuristic bookkeeping (HEURISTIC, Rule R F4).**
- In M_2(X; H) = Σ_n(ψ(n + H) − ψ(n) − H)², the pair errors enter as Σ_{0<|d|<H}(H − |d|)E_2(X; {0, d}). The main terms
  combine through C7 (16), R_2(h) = Σ_{0<|d|<h}(h − |d|)(S(d) − 1) = −h log h + Ah + O(h^{1/2+ε}), to H·X log(X/H).
- So (V) at H needs the weighted error average to be o(HX log(X/H)), i.e. an average error o(X log X/H) per shift.
  For H = X^η that is a power saving.
- MRT (C9) save an arbitrary power of log X on average over h, for X^{8/33+ε} ≤ H ≤ X^{1−ε}. So, *by this bookkeeping*,
  the best unconditional averaged prime-pair results fall short of (V) by a power of X.

**(c) The duality (HEURISTIC, Rule R F4, F11).**
- Small gaps between zeros, the content of (SG), are controlled by F(α) at large α.
- F(α) at large α is in turn controlled by prime-pair errors cancelling on average over shifts up to X^{1−ε}.
- Repulsion of zeros corresponds to the negative secondary term in R_2(h) = Σ_{0<|d|<h}(h − |d|)(S(d) − 1) = −h log h +
  Ah + … (C7 (16)).
- Existence results for prime clusters (bounded gaps) have no bearing on (V) in the needed range.

### 9.3 Open: can the prime input be weakened? (Rule R F1)

By C8 footnote 6, (V) on the full range already implies RH. So "remove RH from Corollary P" is not the right
question. The open questions are:
- **(Q1)** Does (V) on a *restricted* range (for example h ≤ X^{θ} with θ < 1, which is not known to imply RH), or a
  one-sided variance bound, still give (SG)?
- **(Q2)** A hypothesis-free formulation on the zero side: does the strong pair correlation in the unconditional
  complex-weighted form, F(x, T) := Σ x^{ρ−ρ′}W(ρ − ρ′) (BGST arXiv:2501.14545v3 (3.1); W(u) = 4/(4 − u²)), imply (SG)
  without RH?
  - Its weights are complex-valued, so the positivity of individual terms used on RH is unavailable (BGST, proof of
    Lemma 4: "Since W(ρ−ρ′) is complex-valued we need to remove this weight").
  - This is pursued in Plan 19 (research/G3prime/rhfree/).

### 9.4 Numerical sanity (NUMERICAL; `checks/check_pc_numerics.py` → `.out`; Odlyzko's first 2,001,052 zeros)

These are statements about a finite sample, not evidence about the asymptotics (AGENTS.md rule 3). The script needs
`data/raw` (Odlyzko zeros) and the compiled toolkit (main checkout).

**[1] Repulsion: the content of (SG).** Normalized gaps g_k (§4) for k ≤ 2·10⁶ (γ ≤ 1.13·10⁶). The mean is 1.00000
and the minimum is 0.0055.
- The comparison columns are the Wigner-surmise CDF, an *approximation* to the GUE nearest-neighbour spacing law, and
  the PCC integral.
- Only **17** gaps are below δ = 0.02, so that row carries roughly ±25% statistical uncertainty (Rule R F7).
- The pair count uses forward pairs among the next 7 neighbours, which is adequate for β ≤ 0.5 (offset 2 adds 44 pairs
  at β = 0.5, offset 3 adds none).

| δ | #{g_k < δ}/K | Wigner-surmise CDF | PCC ∫_0^δ(1 − sinc²) |
|---|---|---|---|
| 0.02 | 8.50e−6 | 8.64e−6 | 8.77e−6 |
| 0.05 | 1.27e−4 | 1.35e−4 | 1.37e−4 |
| 0.10 | 9.12e−4 | 1.07e−3 | 1.09e−3 |
| 0.20 | 7.14e−3 | 8.39e−3 | 8.50e−3 |
| 0.50 | 1.02e−1 | 1.12e−1 | 1.13e−1 |

- The small-gap fraction follows the δ³ shape.
- The 10–15% shortfall at moderate δ is **not analysed**. The reviewer's split by height shows it shrinking with
  height (internal evidence only).

**[2] G3′ defect, true zeros against the smooth model.** D(n) := (2/n²)Σ_{j<n}(n−j)log(b_j/x̃_j) − log(π²/16):

| n | 100 | 200 | 400 | 800 | 1600 | 3200 |
|---|---|---|---|---|---|---|
| D_true | −0.12664 | −0.10701 | −0.09097 | −0.07817 | −0.06801 | −0.05991 |
| D_smooth | −0.12627 | −0.10674 | −0.09080 | −0.07807 | −0.06796 | −0.05988 |
| difference | −3.7e−4 | −2.6e−4 | −1.7e−4 | −1.0e−4 | −5.8e−5 | −3.2e−5 |

- **Stability** (Rule N; the reviewer's runs, now built into the script as part [3]): J = 1, 2, 4·10⁵ in double, and
  J = 2·10⁵ in long double, reproduce every printed digit.
- Both D's drift to 0 like the smooth model's slow 1/log term (the κ of Theorem RH_ζ, G1).
- The true-minus-smooth difference shrinks, with local exponents rising from 0.49 to 0.86 over this range. This is
  consistent with G3′, i.e. a defect of 0.
