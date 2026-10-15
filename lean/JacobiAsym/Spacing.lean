import JacobiAsym.GenWeights

/-! # Plan 61, stage G2: scaling and the regular-spacing comparison (Paper 1 Lemma 2.2(iii), Lemma 2.3)

* `heineD_scale`: `D_n(Σ w_k δ_{C y_k}) = C^{n(n−1)} D_n(Σ w_k δ_{y_k})` (`C > 0`), and `scaled_law`: the constant
  `κ` of a law `log D_n = −p n² log n + n² ℓ(n) + κ n² + o(n²)` becomes `κ + log C`.
* `PairRatio x y`: the conclusion of the Cauchy mean value step of Lemma 2.3 — for every `ε > 0` the squared gaps
  of `x` and `y` agree up to the factor `e^{±2ε}` on all pairs whose smaller index is `≥ a₀`, and up to a fixed
  factor `B^{±2} e^{±2ε}` on the others.
* `hnorm_transfer` (Lemma 2.3): under `PairRatio x y`, `x` and `y` with the same weights have the same law
  (`|log D_n(x) − log D_n(y)| ≤ 2a₀ n log B + ε n(n−1)`). Translation invariance (Lemma 2.2(ii)) is built in:
  only differences of atoms occur. -/

open Real Set Filter Topology Finset

namespace JacobiAsym

/-! ### Scaling (Lemma 2.2(iii)) -/

theorem heineTerm_scale (y w : ℕ → ℝ) (C : ℝ) (S : Finset ℕ) :
    heineTerm (fun k => C * y k) w S = C ^ (S.card * (S.card - 1)) * heineTerm y w S := by
  unfold heineTerm
  have e : ∀ q ∈ pairs S, (C * y q.1 - C * y q.2) ^ 2 = C ^ 2 * (y q.1 - y q.2) ^ 2 := fun q _ => by ring
  rw [prod_congr rfl e, prod_mul_distrib, prod_const, ← pow_mul, two_mul_card_pairs]
  ring

theorem heineK_scale (y w : ℕ → ℝ) (C : ℝ) (K n : ℕ) :
    heineK (fun k => C * y k) w K n = C ^ (n * (n - 1)) * heineK y w K n := by
  unfold heineK
  rw [mul_sum]
  apply sum_congr rfl
  intro S hS
  rw [heineTerm_scale, (mem_powersetCard.1 hS).2]

theorem heineD_scale {y w : ℕ → ℝ} {C : ℝ} (hC : 0 < C) (n : ℕ) :
    heineD (fun k => C * y k) w n = C ^ (n * (n - 1)) * heineD y w n := by
  unfold heineD
  simp_rw [heineK_scale]
  exact (Real.mul_iSup_of_nonneg (pow_nonneg hC.le _) _).symm

/-- Scaling the atoms by `C > 0` adds `log C` to the constant (Paper 1 §6, "pure powers"). -/
theorem scaled_law {p κ C : ℝ} {y w : ℕ → ℝ} {ℓ : ℕ → ℝ} (hC : 0 < C) (hpy : ∀ n, 0 < heineD y w n)
    (hy : Tendsto (hnorm p κ (heineD y w) ℓ) atTop (𝓝 0)) :
    Tendsto (hnorm p (κ + Real.log C) (heineD (fun k => C * y k) w) ℓ) atTop (𝓝 0) := by
  have h2 : Tendsto (fun n : ℕ => -Real.log C / n) atTop (𝓝 0) := tendsto_const_div_atTop_nhds_zero_nat _
  have := hy.add h2
  rw [add_zero] at this
  refine this.congr' ?_
  filter_upwards [eventually_ge_atTop 1] with n hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hCn : 0 < C ^ (n * (n - 1)) := pow_pos hC _
  unfold hnorm
  rw [heineD_scale hC, Real.log_mul hCn.ne' (hpy n).ne', Real.log_pow]
  have : ((n * (n - 1) : ℕ) : ℝ) = (n : ℝ) ^ 2 - n := by
    rw [Nat.cast_mul, Nat.cast_sub hn]; push_cast; ring
  rw [this]
  field_simp
  ring

/-! ### Regular-spacing comparison (Lemma 2.3) -/

/-- Pair-gap comparison between two atom sequences (the output of the Cauchy mean value step in Paper 1
Lemma 2.3): for every `ε > 0` there are `a₀` and `B ≥ 1` such that for all `a < b`, with
`β = (if a < a₀ then B else 1)`, `(x_a − x_b)² ≤ β² e^{2ε} (y_a − y_b)²` and `(y_a − y_b)² ≤ β² e^{2ε} (x_a − x_b)²`. -/
def PairRatio (x y : ℕ → ℝ) : Prop :=
  ∀ ε > 0, ∃ a0 : ℕ, ∃ B : ℝ, 1 ≤ B ∧ ∀ a b : ℕ, a < b →
    (x a - x b) ^ 2 ≤ (if a < a0 then B else 1) ^ 2 * Real.exp ε ^ 2 * (y a - y b) ^ 2 ∧
    (y a - y b) ^ 2 ≤ (if a < a0 then B else 1) ^ 2 * Real.exp ε ^ 2 * (x a - x b) ^ 2

theorem PairRatio.symm {x y : ℕ → ℝ} (h : PairRatio x y) : PairRatio y x := by
  intro ε hε
  obtain ⟨a0, B, hB, hab⟩ := h ε hε
  exact ⟨a0, B, hB, fun a b hlt => ⟨(hab a b hlt).2, (hab a b hlt).1⟩⟩

/-- One direction of Lemma 2.3 at the level of `log heineD`. -/
theorem log_heineD_le_of_pair {x y w : ℕ → ℝ} (hw : ∀ k, 0 ≤ w k) {a0 : ℕ} {B ε : ℝ} (hB : 1 ≤ B) (hε : 0 ≤ ε)
    (hpair : ∀ a b : ℕ, a < b →
      (x a - x b) ^ 2 ≤ (if a < a0 then B else 1) ^ 2 * Real.exp ε ^ 2 * (y a - y b) ^ 2)
    {n : ℕ} (hby : BddAbove (Set.range fun K => heineK y w K n)) (hpx : 0 < heineD x w n)
    (hpy : 0 < heineD y w n) :
    Real.log (heineD x w n) ≤ Real.log (heineD y w n) + 2 * a0 * n * Real.log B + (n : ℝ) ^ 2 * ε := by
  set c : ℝ := B ^ (2 * a0 * n) * Real.exp ε ^ (n * (n - 1))
  have hc : 0 < c := by positivity
  have hK : ∀ K, heineK x w K n ≤ c * heineD y w n := by
    intro K
    unfold heineK
    calc ∑ S ∈ (range K).powersetCard n, heineTerm x w S
        ≤ ∑ S ∈ (range K).powersetCard n, c * heineTerm y w S := by
          apply sum_le_sum
          intro S hS
          have hcard := (mem_powersetCard.1 hS).2
          have := heineTerm_le_of_pair_le_split hw hB (lam := Real.exp ε) (a0 := a0) (S := S)
            (fun a _ b _ hab => hpair a b hab)
          rw [hcard] at this
          exact this
      _ = c * heineK y w K n := by rw [← mul_sum]; rfl
      _ ≤ c * heineD y w n := mul_le_mul_of_nonneg_left (heineK_le_heineD hby K) hc.le
  have hD := heineD_le hK
  have hl := Real.log_le_log hpx hD
  rw [Real.log_mul hc.ne' hpy.ne', Real.log_mul (by positivity) (by positivity), Real.log_pow, Real.log_pow,
    Real.log_exp] at hl
  have hlogB : 0 ≤ Real.log B := Real.log_nonneg hB
  have hnn : ((n * (n - 1) : ℕ) : ℝ) ≤ (n : ℝ) ^ 2 := by
    have : n * (n - 1) ≤ n ^ 2 := by rw [sq]; exact Nat.mul_le_mul_left n (Nat.sub_le n 1)
    exact_mod_cast this
  have h3 : ((n * (n - 1) : ℕ) : ℝ) * ε ≤ (n : ℝ) ^ 2 * ε := mul_le_mul_of_nonneg_right hnn hε
  push_cast at hl h3 ⊢
  linarith

/-- **Lemma 2.3 (regular spacing comparison), asymptotic form**: if the atom sequences `x`, `y` satisfy
`PairRatio x y`, then with the same nonnegative weights `log D_n(x) − log D_n(y) = o(n²)`, so a law for `y` holds for
`x` with the same `κ`, `ℓ`. -/
theorem hnorm_transfer {p κ : ℝ} {x y w : ℕ → ℝ} {ℓ : ℕ → ℝ} (h : PairRatio x y) (hw : ∀ k, 0 ≤ w k)
    (hbx : ∀ n, BddAbove (Set.range fun K => heineK x w K n))
    (hby : ∀ n, BddAbove (Set.range fun K => heineK y w K n))
    (hpx : ∀ n, 0 < heineD x w n) (hpy : ∀ n, 0 < heineD y w n)
    (hy : Tendsto (hnorm p κ (heineD y w) ℓ) atTop (𝓝 0)) :
    Tendsto (hnorm p κ (heineD x w) ℓ) atTop (𝓝 0) := by
  have hd : Tendsto (fun n => hnorm p κ (heineD x w) ℓ n - hnorm p κ (heineD y w) ℓ n) atTop (𝓝 0) := by
    rw [Metric.tendsto_atTop]
    intro δ hδ
    obtain ⟨a0, B, hB, hab⟩ := h (δ / 2) (half_pos hδ)
    have hlogB : 0 ≤ Real.log B := Real.log_nonneg hB
    have ht : Tendsto (fun n : ℕ => 2 * a0 * Real.log B / n) atTop (𝓝 0) :=
      tendsto_const_div_atTop_nhds_zero_nat _
    obtain ⟨N, hN⟩ := eventually_atTop.1 ((ht.eventually (gt_mem_nhds (half_pos hδ))).and
      (eventually_ge_atTop 1))
    refine ⟨N, fun n hn => ?_⟩
    obtain ⟨h1, hn1⟩ := hN n hn
    have hn' : (0 : ℝ) < n := by exact_mod_cast hn1
    have u1 := log_heineD_le_of_pair hw hB (half_pos hδ).le (fun a b hlt => (hab a b hlt).1) (hby n) (hpx n)
      (hpy n)
    have u2 := log_heineD_le_of_pair hw hB (half_pos hδ).le (fun a b hlt => (hab a b hlt).2) (hbx n) (hpy n)
      (hpx n)
    rw [div_lt_iff₀ hn'] at h1
    rw [Real.dist_eq, sub_zero]
    have e : hnorm p κ (heineD x w) ℓ n - hnorm p κ (heineD y w) ℓ n =
        (Real.log (heineD x w n) - Real.log (heineD y w n)) / (n : ℝ) ^ 2 := by
      unfold hnorm; field_simp; ring
    rw [e, abs_div, abs_of_pos (by positivity : (0 : ℝ) < (n : ℝ) ^ 2), div_lt_iff₀ (by positivity), abs_lt]
    constructor <;> nlinarith
  have := hd.add hy
  rw [add_zero] at this
  exact this.congr fun n => by ring

end JacobiAsym
