import JacobiAsym.Discretize
import JacobiAsym.Exponent

/-! # Plan 60, stage S3b: head bound and the upper bound A-U (Paper 1 Corollary 4.2, Theorem 4.3)

* `head_V_bound` (Corollary 4.2): for `S ⊆ {0,…,Mn−1}`, `|S| = N ≥ 1`,
  `log V(S) ≤ −p N² log N + κ_p N² + p N log n + N eDisc`, from Lemma 4.1, the scaling lemma and `Jp_le_kappa`.
* **`hall_upper`** (Theorem 4.3 for `w_k = k^{-s}`): for every `η > 0`, eventually `hnorm ≤ η`. -/

open Real Set MeasureTheory Filter Topology
open scoped ENNReal

namespace JacobiAsym

/-! ### The cell measure: mass, admissibility after scaling -/

theorem muBar_univ {n : ℕ} (hn : 1 ≤ n) (S : Finset ℕ) : muBar n S univ = ENNReal.ofReal (S.card / n) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [muBar, Measure.restrict_apply MeasurableSet.univ, univ_inter, cellU,
    measure_biUnion_finset (fun a _ b _ hab => cell_disjoint hn hab) (fun a _ => measurableSet_Ioc)]
  have : ∀ a ∈ S, volume (cell n a) = ENNReal.ofReal (1 / n) := fun a _ => by
    rw [cell, Real.volume_Ioc, show ((a : ℝ) + 1) / n - a / n = 1 / n by ring]
  rw [Finset.sum_congr rfl this, Finset.sum_const, nsmul_eq_mul, ← ENNReal.ofReal_natCast,
    ← ENNReal.ofReal_mul (by positivity)]
  congr 1; ring

instance muBar_sfinite (n : ℕ) (S : Finset ℕ) : SFinite (muBar n S) := by unfold muBar; infer_instance

theorem muBar_fin {n M : ℕ} (hn : 1 ≤ n) {S : Finset ℕ} (hS : S ⊆ Finset.range (M * n)) :
    IsFiniteMeasure (muBar n S) := by
  rw [muBar, isFiniteMeasure_restrict]
  exact ne_top_of_le_ne_top (by simp) (measure_mono (cellU_sub_box hn hS))

theorem muBar_scaleHyp {p : ℝ} (hp : 0 < p) {n M : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) {S : Finset ℕ}
    (hS : S ⊆ Finset.range (M * n)) : ScaleHyp p (muBar n S) where
  fin := muBar_fin hn hS
  le_zero := by
    rw [muBar, Measure.restrict_apply measurableSet_Iic]
    apply measure_mono_null _ (measure_empty (μ := volume))
    intro x hx
    exact absurd (cellU_sub_box hn hS hx.2).1 (not_lt.2 hx.1)
  diag := by
    apply diag_null2
    intro x
    rw [muBar, Measure.restrict_apply (measurableSet_singleton x)]
    exact measure_mono_null inter_subset_left Real.volume_singleton
  int := by
    have hM' : (0 : ℝ) < M := by exact_mod_cast hM
    exact (Fp_integrable_box hp hM').mono_measure
      (Measure.prod_mono (muBar_le_box hn hS) (muBar_le_box hn hS))

theorem muBar_real_univ {n : ℕ} (hn : 1 ≤ n) (S : Finset ℕ) : (muBar n S).real univ = S.card / n := by
  rw [Measure.real, muBar_univ hn S, ENNReal.toReal_ofReal (by positivity)]

theorem scaled_muBar_admissible {n M : ℕ} (hn : 1 ≤ n) {S : Finset ℕ} (hS : S ⊆ Finset.range (M * n))
    (hN : 1 ≤ S.card) :
    AdmissibleOn ((n : ℝ) / S.card * M) (scaleM ((n : ℝ) / S.card) (muBar n S)) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hN' : (0 : ℝ) < S.card := by exact_mod_cast hN
  have hτ : 0 < (n : ℝ) / S.card := by positivity
  constructor
  · constructor
    rw [scaleM_apply MeasurableSet.univ, preimage_univ, muBar_univ hn S, ← ENNReal.ofReal_mul hτ.le]
    rw [show (n : ℝ) / S.card * (S.card / n) = 1 by field_simp]; simp
  · rw [scaleM_apply measurableSet_Iic, preimage_mul_Iic hτ, zero_div, muBar, Measure.restrict_apply measurableSet_Iic]
    rw [show Iic (0 : ℝ) ∩ cellU n S = ∅ by
      ext x; simp only [mem_inter_iff, mem_Iic, mem_empty_iff_false, iff_false, not_and]
      intro hx hxU; exact absurd (cellU_sub_box hn hS hxU).1 (not_lt.2 hx)]
    simp
  · rw [scaleM_apply measurableSet_Ioi, preimage_mul_Ioi hτ, show (n : ℝ) / S.card * M / (n / S.card) = M by
      field_simp, muBar, Measure.restrict_apply measurableSet_Ioi]
    rw [show Ioi (M : ℝ) ∩ cellU n S = ∅ by
      ext x; simp only [mem_inter_iff, Set.mem_Ioi, mem_empty_iff_false, iff_false, not_and]
      intro hx hxU; exact absurd (cellU_sub_box hn hS hxU).2 (not_le.2 hx)]
    simp
  · intro a b ha hab
    rw [scaleM_apply measurableSet_Ioc, preimage_mul_Ioc hτ, muBar, Measure.restrict_apply measurableSet_Ioc]
    calc ENNReal.ofReal ((n : ℝ) / S.card) * volume (Ioc (a / (n / S.card)) (b / (n / S.card)) ∩ cellU n S)
        ≤ ENNReal.ofReal ((n : ℝ) / S.card) * volume (Ioc (a / (n / S.card)) (b / (n / S.card))) := by
          gcongr; exact inter_subset_left
      _ = ENNReal.ofReal (b - a) := by
          rw [Real.volume_Ioc, ← ENNReal.ofReal_mul hτ.le]; congr 1; field_simp

/-- `n² 𝒥(μ̄_S) ≤ N² (κ_p + p log (n/N))` (scaling + optimality). -/
theorem muBar_energy_le {p : ℝ} (hp : 0 < p) {n M : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) {S : Finset ℕ}
    (hS : S ⊆ Finset.range (M * n)) (hN : 1 ≤ S.card) :
    (n : ℝ) ^ 2 * Jp p (muBar n S) ≤
      (S.card : ℝ) ^ 2 * (hallKappa p + p * Real.log n - p * Real.log S.card) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hN' : (0 : ℝ) < S.card := by exact_mod_cast hN
  have hτ : 0 < (n : ℝ) / S.card := by positivity
  have hH := muBar_scaleHyp hp hn hM hS
  have hJ := Jp_scaleM hp hτ hH
  have hle := Jp_le_kappa hp (scaled_muBar_admissible hn hS hN) (scaleM_integrable hp hτ hH)
  rw [hJ, muBar_real_univ hn S, Real.log_div hn'.ne' hN'.ne'] at hle
  have e : ((n : ℝ) / S.card) ^ 2 = (n : ℝ) ^ 2 / (S.card : ℝ) ^ 2 := by ring
  rw [e] at hle
  have hpos : 0 < (n : ℝ) ^ 2 / (S.card : ℝ) ^ 2 := by positivity
  have key : Jp p (muBar n S) - p * (Real.log n - Real.log S.card) * ((S.card : ℝ) / n) ^ 2 ≤
      hallKappa p * ((S.card : ℝ) ^ 2 / (n : ℝ) ^ 2) := by
    rw [← le_div_iff₀' hpos] at hle; rw [div_div_eq_mul_div] at hle
    calc _ ≤ _ := hle
      _ = _ := by ring
  have : (n : ℝ) ^ 2 * (Jp p (muBar n S) - p * (Real.log n - Real.log S.card) * ((S.card : ℝ) / n) ^ 2) ≤
      (n : ℝ) ^ 2 * (hallKappa p * ((S.card : ℝ) ^ 2 / (n : ℝ) ^ 2)) := mul_le_mul_of_nonneg_left key (by positivity)
  have e2 : (n : ℝ) ^ 2 * (Jp p (muBar n S) - p * (Real.log n - Real.log S.card) * ((S.card : ℝ) / n) ^ 2) =
      (n : ℝ) ^ 2 * Jp p (muBar n S) - (S.card : ℝ) ^ 2 * (p * Real.log n - p * Real.log S.card) := by
    field_simp
  have e3 : (n : ℝ) ^ 2 * (hallKappa p * ((S.card : ℝ) ^ 2 / (n : ℝ) ^ 2)) = (S.card : ℝ) ^ 2 * hallKappa p := by
    field_simp
  rw [e2, e3] at this
  nlinarith

/-! ### Corollary 4.2: the head bound -/

theorem powSeq_eq_ucell {p : ℝ} {n : ℕ} (hn : 1 ≤ n) (a : ℕ) :
    powSeq p a = (n : ℝ) ^ (-p) * ucell n a ^ (-p) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  unfold powSeq ucell
  rw [← mul_rpow hn'.le (by positivity), mul_div_cancel₀ _ hn'.ne']

theorem log_pair_ucell {p : ℝ} (hp : 0 < p) {n a b : ℕ} (hn : 1 ≤ n) (hab : a < b) :
    0 < (powSeq p a - powSeq p b) ^ 2 ∧
      Real.log ((powSeq p a - powSeq p b) ^ 2) = 2 * Fp p (ucell n a) (ucell n b) - 2 * p * Real.log n := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hua : 0 < ucell n a := by unfold ucell; positivity
  have hlt : ucell n a < ucell n b := by
    unfold ucell; apply div_lt_div_of_pos_right _ hn'
    have : (a : ℝ) < b := by exact_mod_cast hab
    linarith
  have hd : 0 < ucell n a ^ (-p) - ucell n b ^ (-p) := sub_pos.2 (rpow_lt_rpow_of_neg hua hlt (by linarith))
  rw [powSeq_eq_ucell hn a, powSeq_eq_ucell hn b, ← mul_sub]
  have hnp := rpow_pos_of_pos hn' (-p)
  refine ⟨by positivity, ?_⟩
  rw [Real.log_pow, Real.log_mul hnp.ne' hd.ne', Real.log_rpow hn', Fp, abs_of_pos hd]
  push_cast; ring

/-- **Corollary 4.2 (head bound)**: for `S ⊆ {0,…,Mn−1}` with `N = |S| ≥ 1`,
`log V(S) ≤ −p N² log N + κ_p N² + p N log n + N · eDisc`. -/
theorem head_V_bound {p : ℝ} (hp : 0 < p) {n M : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) {S : Finset ℕ}
    (hS : S ⊆ Finset.range (M * n)) (hN : 1 ≤ S.card) :
    Real.log (∏ q ∈ pairs S, (powSeq p q.1 - powSeq p q.2) ^ 2) ≤
      -p * (S.card : ℝ) ^ 2 * Real.log S.card + hallKappa p * (S.card : ℝ) ^ 2 +
        p * S.card * Real.log n + S.card * eDisc p n M := by
  have hlt : ∀ q ∈ pairs S, q.1 < q.2 := fun q hq => by
    simp only [pairs, Finset.mem_filter] at hq; exact hq.2
  rw [Real.log_prod (fun q hq => (log_pair_ucell hp hn (hlt q hq)).1.ne'),
    Finset.sum_congr rfl (fun q hq => (log_pair_ucell hp hn (hlt q hq)).2), Finset.sum_sub_distrib,
    ← Finset.mul_sum, Finset.sum_const, nsmul_eq_mul]
  have hD := disc_upper hp hn hM hS (n := n)
  have hE := muBar_energy_le hp hn hM hS hN
  have hc : 2 * ((pairs S).card : ℝ) = S.card * (S.card - 1) := by
    have := two_mul_card_pairs S
    have h2 : ((2 * (pairs S).card : ℕ) : ℝ) = ((S.card * (S.card - 1) : ℕ) : ℝ) := by rw [this]
    push_cast [Nat.cast_sub hN] at h2; linarith
  have e1 : ((pairs S).card : ℝ) * (2 * p * Real.log n) = p * S.card * (S.card - 1) * Real.log n := by
    have : ((pairs S).card : ℝ) * (2 * p * Real.log n) = (2 * (pairs S).card) * (p * Real.log n) := by ring
    rw [this, hc]; ring
  rw [e1]
  nlinarith

/-- Head Heine sum: `heineK (powSeq p) w (Mn) N ≤ W^N exp(B_N)` with `B_N` the head bound, `W ≥ Σ_{k<Mn} w_k`. -/
theorem head_heineK_bound {p : ℝ} (hp : 0 < p) {w : ℕ → ℝ} (hw : ∀ k, 0 ≤ w k) {W : ℝ}
    {n M N : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (hN : 1 ≤ N) (hW : ∑ k ∈ Finset.range (M * n), w k ≤ W) :
    heineK (powSeq p) w (M * n) N ≤
      W ^ N * Real.exp (-p * (N : ℝ) ^ 2 * Real.log N + hallKappa p * (N : ℝ) ^ 2 +
        p * N * Real.log n + N * eDisc p n M) := by
  set B := -p * (N : ℝ) ^ 2 * Real.log N + hallKappa p * (N : ℝ) ^ 2 + p * N * Real.log n + N * eDisc p n M
  have hV : ∀ S ∈ (Finset.range (M * n)).powersetCard N,
      heineTerm (powSeq p) w S ≤ (∏ i ∈ S, w i) * Real.exp B := by
    intro S hS
    obtain ⟨hsub, hcard⟩ := Finset.mem_powersetCard.1 hS
    unfold heineTerm
    apply mul_le_mul_of_nonneg_left _ (Finset.prod_nonneg fun i _ => hw i)
    have hpos : 0 < ∏ q ∈ pairs S, (powSeq p q.1 - powSeq p q.2) ^ 2 :=
      Finset.prod_pos fun q hq => (log_pair_ucell hp hn (by
        simp only [pairs, Finset.mem_filter] at hq; exact hq.2)).1
    rw [← Real.exp_log hpos, Real.exp_le_exp]
    have := head_V_bound hp hn hM hsub (by rw [hcard]; exact hN)
    rw [hcard] at this; exact this
  calc heineK (powSeq p) w (M * n) N ≤ ∑ S ∈ (Finset.range (M * n)).powersetCard N, (∏ i ∈ S, w i) * Real.exp B :=
        Finset.sum_le_sum hV
    _ = (∑ S ∈ (Finset.range (M * n)).powersetCard N, ∏ i ∈ S, w i) * Real.exp B := by rw [Finset.sum_mul]
    _ ≤ (∑ k ∈ Finset.range (M * n), w k) ^ N * Real.exp B :=
        mul_le_mul_of_nonneg_right (sum_prod_powersetCard_le hw _ N) (Real.exp_pos _).le
    _ ≤ W ^ N * Real.exp B := by
        gcongr
        exact Finset.sum_nonneg fun k _ => hw k

/-! ### The `m`-th term of the head/tail split (Paper 1 Theorem 4.3) -/

/-- `log` of the `m`-th term (head `N = n − m` points, tail `m` points) given a head bound
`log D ≤ −p N² log N + κ N² + R`. Adapted from `log_upperTerm_le`. -/
theorem log_term_le {p κ W D R : ℝ} (hp : 0 < p) (hW : 0 < W) (hDpos : 0 < D) {M n m : ℕ} (hM : 2 ≤ M)
    (hn : 1 ≤ n) (hmn : m ≤ n)
    (hD : Real.log D ≤ -p * ((n : ℝ) - m) ^ 2 * Real.log ((n : ℝ) - m) + κ * ((n : ℝ) - m) ^ 2 + R) :
    Real.log (((n - m).factorial : ℝ) ^ (-(2 * p * m)) * D * W ^ m *
        (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1))) ≤
      -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2
        + (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) * (n : ℝ) ^ 2 + R
        + n * (|Real.log W| + p * Real.log (M * n)) := by
  have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hnpos : (0 : ℝ) < n := by linarith
  have hmr : (m : ℝ) ≤ n := by exact_mod_cast hmn
  have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
  have hMr : (2 : ℝ) ≤ M := by exact_mod_cast hM
  have hMpos : (0 : ℝ) < M := by linarith
  have hNr : ((n - m : ℕ) : ℝ) = (n : ℝ) - m := Nat.cast_sub hmn
  have hMn : ((M * n : ℕ) : ℝ) = (M : ℝ) * n := by push_cast; ring
  have hMn1 : (1 : ℝ) ≤ (M : ℝ) * n := by nlinarith
  have hlogMn : Real.log ((M : ℝ) * n) = Real.log M + Real.log n := Real.log_mul hMpos.ne' hnpos.ne'
  have hlogMn0 : 0 ≤ Real.log ((M : ℝ) * n) := Real.log_nonneg hMn1
  have hmm : (((m * (m - 1) : ℕ)) : ℝ) = (m : ℝ) ^ 2 - m := by
    rcases m with _ | m
    · simp
    · push_cast [Nat.succ_sub_one]; ring
  have hF : (0 : ℝ) < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
  have hX : (0 : ℝ) < ((M * n : ℕ) : ℝ) ^ (-p) := Real.rpow_pos_of_pos (by rw [hMn]; linarith) _
  set F := ((n - m).factorial : ℝ)
  set X := ((M * n : ℕ) : ℝ) ^ (-p)
  have hlog : Real.log (F ^ (-(2 * p * m)) * D * W ^ m * X ^ (m * (m - 1))) =
      -(2 * p * m) * Real.log F + Real.log D + m * Real.log W + (((m * (m - 1) : ℕ)) : ℝ) * Real.log X := by
    have h1 : F ^ (-(2 * p * m)) ≠ 0 := (Real.rpow_pos_of_pos hF _).ne'
    have h3 : W ^ m ≠ 0 := (pow_pos hW _).ne'
    have h4 : X ^ (m * (m - 1)) ≠ 0 := (pow_pos hX _).ne'
    rw [Real.log_mul (by positivity) h4, Real.log_mul (by positivity) h3, Real.log_mul h1 hDpos.ne',
      Real.log_rpow hF, Real.log_pow, Real.log_pow]
  have hlogX : Real.log X = -p * Real.log ((M : ℝ) * n) := by
    simp only [X]; rw [Real.log_rpow (by rw [hMn]; linarith), hMn]
  have hfact : -(2 * p * m) * Real.log F ≤ -(2 * p * m) * (((n : ℝ) - m) * Real.log ((n : ℝ) - m) - ((n : ℝ) - m)) := by
    have := log_factorial_ge (n - m)
    rw [hNr] at this
    exact mul_le_mul_of_nonpos_left this (by nlinarith)
  have hWb : (m : ℝ) * Real.log W ≤ n * |Real.log W| :=
    (mul_le_mul_of_nonneg_left (le_abs_self _) hm0).trans (mul_le_mul_of_nonneg_right hmr (abs_nonneg _))
  have hXb : (((m * (m - 1) : ℕ)) : ℝ) * Real.log X ≤
      -p * (m : ℝ) ^ 2 * (Real.log M + Real.log n) + n * (p * Real.log ((M : ℝ) * n)) := by
    rw [hmm, hlogX, ← hlogMn]
    have : (m : ℝ) * (p * Real.log ((M : ℝ) * n)) ≤ n * (p * Real.log ((M : ℝ) * n)) :=
      mul_le_mul_of_nonneg_right hmr (mul_nonneg hp.le hlogMn0)
    nlinarith
  have hid := exponent_identity (p := p) (κ := κ) (M := M) hnpos hm0 hmr hMpos
  have hphi := phi_bound (κ := κ) (M := M) (t := m / n) hp (by linarith) (div_nonneg hm0 hnpos.le)
    ((div_le_one hnpos).2 hmr)
  have hphin := mul_le_mul_of_nonneg_left hphi (sq_nonneg (n : ℝ))
  rw [hlog]
  set φ := -p * (1 - ((m : ℝ) / n) ^ 2) * Real.log (1 - (m : ℝ) / n) + 2 * p * ((m : ℝ) / n) * (1 - (m : ℝ) / n)
    - κ * ((m : ℝ) / n) * (2 - (m : ℝ) / n) - p * ((m : ℝ) / n) ^ 2 * Real.log M with hφ
  calc -(2 * p * m) * Real.log F + Real.log D + m * Real.log W + (((m * (m - 1) : ℕ)) : ℝ) * Real.log X
      ≤ -(2 * p * m) * (((n : ℝ) - m) * Real.log ((n : ℝ) - m) - ((n : ℝ) - m))
        + (-p * ((n : ℝ) - m) ^ 2 * Real.log ((n : ℝ) - m) + κ * ((n : ℝ) - m) ^ 2 + R)
        + n * |Real.log W|
        + (-p * (m : ℝ) ^ 2 * (Real.log M + Real.log n) + n * (p * Real.log ((M : ℝ) * n))) := by
        linarith [hfact, hWb, hXb, hD]
    _ = -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2 + (n : ℝ) ^ 2 * φ + R
        + n * (|Real.log W| + p * Real.log ((M : ℝ) * n)) := by
        linear_combination hid
    _ ≤ _ := by linear_combination hphin

/-! ### Theorem 4.3 (upper bound) for the pure powers -/

theorem powSeq_summable {s : ℝ} (hs : 1 < s) : Summable (powSeq s) := by
  have := (Real.summable_nat_rpow_inv.2 hs).comp_injective (add_left_injective 1)
  refine this.congr fun k => ?_
  simp [powSeq, rpow_neg (by positivity : (0 : ℝ) ≤ (k : ℝ) + 1)]

theorem powSeq_pos (s : ℝ) (k : ℕ) : 0 < powSeq s k := rpow_pos_of_pos (by positivity) _

theorem powSeq_strictAnti {p : ℝ} (hp : 0 < p) : StrictAnti (powSeq p) := by
  intro a b hab
  exact Real.rpow_lt_rpow_of_neg (by positivity) (by exact_mod_cast Nat.add_lt_add_right hab 1) (by linarith)

/-- The `m`-th term: `(N!)^{−2pm} heineK(Mn, N) W^m ((Mn)^{−p})^{m(m−1)}`, `N = n − m`. -/
noncomputable def hTerm (p s : ℝ) (M n m : ℕ) : ℝ :=
  ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * heineK (powSeq p) (powSeq s) (M * n) (n - m) *
    (∑' k, powSeq s k) ^ m * (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1))

/-- Head/tail split for the pure powers (item 11 H7 / Paper 1 Theorem 4.3). -/
theorem heineK_le_hTerm {p s : ℝ} (hp : 0 < p) (hs : 1 < s) {M n : ℕ} (hMn : 1 ≤ M * n) (K : ℕ) :
    heineK (powSeq p) (powSeq s) K n ≤ ∑ m ∈ Finset.range (n + 1), hTerm p s M n m := by
  have hw : ∀ i, 0 ≤ powSeq s i := fun i => (powSeq_pos s i).le
  have hMnr : (0 : ℝ) < ((M * n : ℕ) : ℝ) := by exact_mod_cast hMn
  have h0 := heineK_mono_K hw (le_max_left K (M * n)) n (x := powSeq p)
  have h2 := heineK_tail_split (y := powSeq p) (w := powSeq s) hw (le_max_right K (M * n)) (n := n)
    (X := ((M * n : ℕ) : ℝ) ^ (-p)) (powSeq_pos p)
    (fun b hb => rpow_le_rpow_of_nonpos hMnr (by
      have : ((M * n : ℕ) : ℝ) ≤ b := by exact_mod_cast hb
      linarith) (by linarith))
    (fun a b ha hb => ((powSeq_strictAnti hp).antitone (by omega)))
  refine h0.trans (h2.trans (Finset.sum_le_sum fun m _ => ?_))
  have hX : 0 ≤ (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) := pow_nonneg (rpow_pos_of_pos hMnr _).le _
  have hF : 0 < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
  have hhead : ∑ SH ∈ (Finset.range (M * n)).powersetCard (n - m),
        heineTerm (powSeq p) (powSeq s) SH * ∏ a ∈ SH, powSeq p a ^ (2 * m) ≤
      ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * heineK (powSeq p) (powSeq s) (M * n) (n - m) := by
    rw [heineK, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro SH hSH
    have hcard := (Finset.mem_powersetCard.1 hSH).2
    have hP : ∏ a ∈ SH, powSeq p a ^ (2 * m) ≤ ((n - m).factorial : ℝ) ^ (-(2 * p * m)) := by
      have e : ∏ a ∈ SH, powSeq p a ^ (2 * m) = (∏ a ∈ SH, ((a : ℝ) + 1)) ^ (-(2 * p * m)) := by
        rw [← Real.finsetProd_rpow _ _ (fun a _ => by positivity)]
        apply Finset.prod_congr rfl; intro a _
        rw [powSeq, ← Real.rpow_natCast, ← Real.rpow_mul (by positivity)]
        congr 1; push_cast; ring
      rw [e]
      have hf := factorial_le_prod_succ SH
      rw [hcard] at hf
      exact Real.rpow_le_rpow_of_nonpos hF hf (by have : (0 : ℝ) ≤ m := Nat.cast_nonneg m; nlinarith)
    rw [mul_comm (((n - m).factorial : ℝ) ^ (-(2 * p * m)))]
    exact mul_le_mul_of_nonneg_left hP (heineTerm_nonneg hw SH)
  have htail : (∑ b ∈ Finset.Ico (M * n) (max K (M * n)), powSeq s b) ^ m ≤ (∑' k, powSeq s k) ^ m :=
    pow_le_pow_left₀ (Finset.sum_nonneg fun b _ => hw b)
      (Summable.sum_le_tsum _ (fun b _ => hw b) (powSeq_summable hs)) m
  have hh0 : 0 ≤ ∑ SH ∈ (Finset.range (M * n)).powersetCard (n - m),
      heineTerm (powSeq p) (powSeq s) SH * ∏ a ∈ SH, powSeq p a ^ (2 * m) :=
    Finset.sum_nonneg fun SH _ => mul_nonneg (heineTerm_nonneg hw SH)
      (Finset.prod_nonneg fun a _ => pow_nonneg (powSeq_pos p a).le _)
  unfold hTerm
  calc _ ≤ (((n - m).factorial : ℝ) ^ (-(2 * p * m)) * heineK (powSeq p) (powSeq s) (M * n) (n - m)) *
        (∑' k, powSeq s k) ^ m * (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) := by
        apply mul_le_mul_of_nonneg_right _ hX
        exact mul_le_mul hhead htail (pow_nonneg (Finset.sum_nonneg fun b _ => hw b) _) (hh0.trans hhead)
    _ = _ := by ring

theorem eDisc_nonneg {p : ℝ} (hp : 0 < p) {n M : ℕ} (_hn : 1 ≤ n) (_hM : 1 ≤ M) : 0 ≤ eDisc p n M := by
  unfold eDisc
  have := Real.log_natCast_nonneg n
  have : 0 ≤ Real.log ((M * n : ℕ) : ℝ) := Real.log_natCast_nonneg _
  have := eAdj_nonneg hp n M
  positivity

/-- The head bound in the form needed by `log_term_le`. -/
theorem head_log_bound {p s : ℝ} (hp : 0 < p) (hs : 1 < s) {M n m : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) (hmn : m ≤ n) :
    0 < heineK (powSeq p) (powSeq s) (M * n) (n - m) ∧
    Real.log (heineK (powSeq p) (powSeq s) (M * n) (n - m)) ≤
      -p * ((n : ℝ) - m) ^ 2 * Real.log ((n : ℝ) - m) + hallKappa p * ((n : ℝ) - m) ^ 2 +
        n * (|Real.log (∑' k, powSeq s k)| + p * Real.log n + eDisc p n M) := by
  have hw : ∀ i, 0 ≤ powSeq s i := fun i => (powSeq_pos s i).le
  have hWpos : 0 < ∑' k, powSeq s k := (powSeq_summable hs).tsum_pos hw 0 (powSeq_pos s 0)
  have hNle : n - m ≤ M * n := (Nat.sub_le n m).trans (Nat.le_mul_of_pos_left n (by omega))
  have hpos := heineK_pos (powSeq_strictAnti hp) (powSeq_pos s) hNle
  refine ⟨hpos, ?_⟩
  have hNr : ((n - m : ℕ) : ℝ) = (n : ℝ) - m := Nat.cast_sub hmn
  have hE := eDisc_nonneg hp hn hM
  have hlogn := Real.log_natCast_nonneg n
  have hR0 : 0 ≤ (n : ℝ) * (|Real.log (∑' k, powSeq s k)| + p * Real.log n + eDisc p n M) := by positivity
  rcases Nat.eq_zero_or_pos (n - m) with h0 | hN
  · rw [h0, heineK_zero_card, Real.log_one]
    have : (n : ℝ) - m = 0 := by rw [← hNr, h0]; simp
    rw [this]; simp; linarith
  · have hb := head_heineK_bound hp hw hn hM hN (W := ∑' k, powSeq s k)
      (Summable.sum_le_tsum _ (fun b _ => hw b) (powSeq_summable hs))
    have hl := Real.log_le_log hpos hb
    rw [Real.log_mul (pow_pos hWpos _).ne' (Real.exp_pos _).ne', Real.log_pow, Real.log_exp, hNr] at hl
    have hmr : (m : ℝ) ≤ n := by exact_mod_cast hmn
    have hm0 : (0 : ℝ) ≤ m := Nat.cast_nonneg m
    have h1 : ((n : ℝ) - m) * Real.log (∑' k, powSeq s k) ≤ n * |Real.log (∑' k, powSeq s k)| :=
      (mul_le_mul_of_nonneg_left (le_abs_self _) (by linarith)).trans
        (mul_le_mul_of_nonneg_right (by linarith) (abs_nonneg _))
    have h2 : p * ((n : ℝ) - m) * Real.log n ≤ n * (p * Real.log n) := by
      have : p * ((n : ℝ) - m) * Real.log n = ((n : ℝ) - m) * (p * Real.log n) := by ring
      rw [this]; exact mul_le_mul_of_nonneg_right (by linarith) (by positivity)
    have h3 : ((n : ℝ) - m) * eDisc p n M ≤ n * eDisc p n M := by nlinarith
    linarith

theorem eDisc_le {p : ℝ} (_hp : 0 < p) {n M : ℕ} (hn : 1 ≤ n) (hM : 1 ≤ M) :
    eDisc p n M ≤ (3 * |Real.log (p * (M : ℝ) ^ (-p - 1))| + 11 + (2 + 4 * p) * |Real.log M|) +
      (5 + 4 * p) * Real.log n := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hM' : (0 : ℝ) < M := by exact_mod_cast hM
  unfold eDisc eAdj
  have e : Real.log ((M * n : ℕ) : ℝ) = Real.log M + Real.log n := by
    push_cast; exact Real.log_mul hM'.ne' hn'.ne'
  rw [e]
  have := le_abs_self (Real.log M)
  nlinarith [abs_nonneg (Real.log M)]

/-- **Theorem A-U** (Paper 1 Theorem 4.3 for `w_k = k^{-s}`): for every `η > 0`, eventually
`hnorm ≤ η`, i.e. `limsup (log D_n + p n² log n)/n² ≤ κ_p`. -/
theorem hall_upper {p s : ℝ} (hp : 0 < p) (hs : 1 < s) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop, hnorm p (hallKappa p) (heineD (powSeq p) (powSeq s)) (fun _ => 0) n ≤ η := by
  set κ := hallKappa p
  set A := 4 * p + 2 * |κ|
  have hA : 0 < A := by have := abs_nonneg κ; simp only [A]; linarith
  set X := A ^ 2 / (2 * p * η)
  set M : ℕ := ⌈Real.exp X⌉₊ + 2
  have hM2 : 2 ≤ M := by omega
  have hMgt : Real.exp X < M := by
    have := Nat.le_ceil (Real.exp X)
    have : ((⌈Real.exp X⌉₊ + 2 : ℕ) : ℝ) = (⌈Real.exp X⌉₊ : ℝ) + 2 := by push_cast; ring
    simp only [M]; rw [this]; linarith
  have hlogM : X < Real.log M := by
    rw [← Real.exp_lt_exp, Real.exp_log (by have := Real.exp_pos X; linarith)]; exact hMgt
  have hXpos : 0 < X := by positivity
  have hpen : A ^ 2 / (4 * p * Real.log M) < η / 2 := by
    have hlp : 0 < Real.log M := hXpos.trans hlogM
    rw [div_lt_iff₀ (by positivity)]
    have h1 : A ^ 2 = X * (2 * p * η) := by simp only [X]; field_simp
    rw [h1]
    nlinarith [mul_lt_mul_of_pos_right hlogM (by positivity : (0:ℝ) < 2 * p * η)]
  set W := ∑' k, powSeq s k
  set K1 := 3 * |Real.log (p * (M : ℝ) ^ (-p - 1))| + 11 + (2 + 4 * p) * |Real.log M|
  set K2 := 5 + 4 * p
  -- the error term
  set err : ℕ → ℝ := fun n => n * (|Real.log W| + p * Real.log n + (K1 + K2 * Real.log n)) +
    n * (|Real.log W| + p * (Real.log M + Real.log n)) + Real.log ((n : ℝ) + 1)
  have herr : Tendsto (fun n : ℕ => err n / (n : ℝ) ^ 2) atTop (𝓝 0) := by
    have h1 := tendsto_const_div_atTop_nhds_zero_nat (2 * |Real.log W| + K1 + p * Real.log M)
    have h2 := tendsto_log_div_nat.const_mul (2 * p + K2)
    have h3 := tendsto_log_succ_div_sq
    have := (h1.add h2).add h3
    simp only [mul_zero, add_zero] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hn' : (0 : ℝ) < n := by exact_mod_cast hn
    simp only [err]; field_simp; ring
  filter_upwards [herr.eventually (gt_mem_nhds (half_pos hη)), eventually_ge_atTop 1] with n hen hn
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hMn : 1 ≤ M * n := Nat.one_le_iff_ne_zero.2 (by positivity)
  have hbdd := heineK_bdd_of_summable (x := powSeq p) (w := powSeq s) (X := 1)
    (fun k => (powSeq_pos s k).le) (powSeq_summable hs)
    (fun k => by
      rw [abs_of_pos (powSeq_pos p k)]
      exact rpow_le_one_of_one_le_of_nonpos (by have := Nat.cast_nonneg (α := ℝ) k; linarith) (by linarith))
  have hDpos := heineD_pos (powSeq_strictAnti hp) (powSeq_pos s) (hbdd n)
  have hDle := heineD_le (fun K => heineK_le_hTerm hp hs hMn K (n := n))
  set Q := -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2 + A ^ 2 / (4 * p * Real.log M) * (n : ℝ) ^ 2 +
    n * (|Real.log W| + p * Real.log n + eDisc p n M) + n * (|Real.log W| + p * Real.log ((M : ℝ) * n))
  have hW : 0 < W := (powSeq_summable hs).tsum_pos (fun k => (powSeq_pos s k).le) 0 (powSeq_pos s 0)
  have hT : ∀ m ∈ Finset.range (n + 1), 0 < hTerm p s M n m ∧ Real.log (hTerm p s M n m) ≤ Q := by
    intro m hm
    have hmn : m ≤ n := Nat.lt_succ_iff.1 (Finset.mem_range.1 hm)
    obtain ⟨hDp, hDb⟩ := head_log_bound hp hs hn (by omega : 1 ≤ M) hmn (M := M)
    constructor
    · unfold hTerm
      have hF : (0 : ℝ) < ((n - m).factorial : ℝ) := by exact_mod_cast Nat.factorial_pos _
      have hX : (0 : ℝ) < ((M * n : ℕ) : ℝ) ^ (-p) := rpow_pos_of_pos (by exact_mod_cast hMn) _
      have := rpow_pos_of_pos hF (-(2 * p * m))
      positivity
    · exact log_term_le hp hW hDp hM2 hn hmn hDb
  have hsum := log_sum_le_of_log_le (fun m hm => (hT m hm).1) (fun m hm => (hT m hm).2)
  have hlogD : Real.log (heineD (powSeq p) (powSeq s) n) ≤ Real.log ((n : ℝ) + 1) + Q :=
    (Real.log_le_log hDpos hDle).trans hsum
  have hED := eDisc_le hp hn (by omega : 1 ≤ M) (n := n) (M := M)
  have hlogMn : Real.log ((M : ℝ) * n) = Real.log M + Real.log n :=
    Real.log_mul (by have : (2 : ℝ) ≤ M := by exact_mod_cast hM2
                     linarith) hn'.ne'
  have hQ : Q ≤ -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2 + A ^ 2 / (4 * p * Real.log M) * (n : ℝ) ^ 2 +
      (err n - Real.log ((n : ℝ) + 1)) := by
    simp only [Q, err]; rw [hlogMn]
    have := mul_le_mul_of_nonneg_left hED hn'.le
    nlinarith
  rw [div_lt_iff₀ (by positivity)] at hen
  unfold hnorm
  rw [div_le_iff₀ (by positivity)]
  have hpen' := mul_le_mul_of_nonneg_right hpen.le (sq_nonneg (n : ℝ))
  nlinarith

end JacobiAsym
