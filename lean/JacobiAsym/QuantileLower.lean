import JacobiAsym.Energy

/-! # Plan 60, stage S1a: the quantile configuration (Paper 1 Theorem 5.2, Steps 2–3)

For an admissible `θ` on `(0, U]` (`AdmissibleOn U θ`) we choose points `t_m` with `θ(0, t_m] = m/2n`
(`qpt`), the quantiles `q_i = t_{2i+1}`, the integers `k_i = ⌈n q_i⌉` and `u_i = k_i/n`. Then (`far_le`)
for `j ≥ i + 4` and `(u, v) ∈ B_{i+2} × B_{j−1}`, `B_a = (t_{2a}, t_{2a+2}]`, one has `u_i ≤ u < v ≤ u_j`, so
`F(u, v) ≤ F(u_i, u_j)` by monotonicity of `F(u,v) = log (u^{-p} − v^{-p})` — an exact comparison which replaces
the error analysis (a)–(d) of the paper; near pairs cost `O(log n)` each (`near_ge`); the uncovered region has
`θ ⊗ θ`-measure `≤ 7/n` (`measure_bad_le`). -/

open Real Set MeasureTheory Filter Topology Finset
open scoped ENNReal

namespace JacobiAsym

variable {U : ℝ} {θ : Measure ℝ}

/-! ### Interval bound for all `a ≤ b` -/

/-- Interval bound on `(0, b]` from the bound on `(a, b]`, `a > 0` (continuity from below). -/
theorem Ioc_zero_le_of_lip {μ : Measure ℝ}
    (hlip : ∀ a b, 0 < a → a ≤ b → μ (Ioc a b) ≤ ENNReal.ofReal (b - a)) (b : ℝ) :
    μ (Ioc 0 b) ≤ ENNReal.ofReal b := by
  rcases le_or_gt b 0 with hb | hb
  · rw [Ioc_eq_empty (not_lt.2 hb)]; simp
  have hU : Ioc 0 b = ⋃ k : ℕ, Ioc (b / (k + 2)) b := by
    ext x; simp only [Set.mem_Ioc, mem_iUnion]; constructor
    · rintro ⟨hx0, hxb⟩
      obtain ⟨k, hk⟩ := exists_nat_gt (b / x)
      refine ⟨k, ?_, hxb⟩
      rw [div_lt_iff₀ (by positivity)]
      rw [div_lt_iff₀ hx0] at hk
      nlinarith
    · rintro ⟨k, hk, hxb⟩; exact ⟨lt_of_le_of_lt (by positivity) hk, hxb⟩
  have hmono : Monotone fun k : ℕ => Ioc (b / (k + 2)) b := by
    intro k l hkl
    apply Set.Ioc_subset_Ioc_left
    apply div_le_div_of_nonneg_left hb.le (by positivity)
    have : (k : ℝ) ≤ l := by exact_mod_cast hkl
    linarith
  rw [hU, hmono.measure_iUnion]
  apply iSup_le; intro k
  refine (hlip _ _ (by positivity) (div_le_self hb.le (by linarith [(Nat.cast_nonneg k : (0:ℝ) ≤ k)]))).trans ?_
  apply ENNReal.ofReal_le_ofReal
  have : 0 < b / (k + 2) := by positivity
  linarith

/-- Interval bound for all `a ≤ b`. -/
theorem Ioc_le_of_lip {μ : Measure ℝ} (h0 : μ (Iic 0) = 0)
    (hlip : ∀ a b, 0 < a → a ≤ b → μ (Ioc a b) ≤ ENNReal.ofReal (b - a)) {a b : ℝ} (hab : a ≤ b) :
    μ (Ioc a b) ≤ ENNReal.ofReal (b - a) := by
  rcases lt_or_ge 0 a with ha | ha
  · exact hlip a b ha hab
  have hsub : Ioc a b ⊆ Iic 0 ∪ Ioc 0 b := by
    intro x hx
    by_cases hx0 : x ≤ 0
    · exact Or.inl hx0
    · exact Or.inr ⟨lt_of_not_ge hx0, hx.2⟩
  calc μ (Ioc a b) ≤ μ (Iic 0 ∪ Ioc 0 b) := measure_mono hsub
    _ ≤ μ (Iic 0) + μ (Ioc 0 b) := measure_union_le _ _
    _ ≤ 0 + ENNReal.ofReal b := by rw [h0]; exact add_le_add le_rfl (Ioc_zero_le_of_lip hlip b)
    _ ≤ ENNReal.ofReal (b - a) := by rw [zero_add]; exact ENNReal.ofReal_le_ofReal (by linarith)

theorem AdmissibleOn.Ioc_le (h : AdmissibleOn U θ) {a b : ℝ} (hab : a ≤ b) :
    θ (Ioc a b) ≤ ENNReal.ofReal (b - a) :=
  Ioc_le_of_lip h.le_zero h.lip hab

/-! ### The distribution function -/

/-- `F_θ(x) = θ(−∞, x]`. -/
noncomputable def cdfR (θ : Measure ℝ) (x : ℝ) : ℝ := (θ (Iic x)).toReal

theorem AdmissibleOn.cdf_sub (h : AdmissibleOn U θ) {a b : ℝ} (hab : a ≤ b) :
    cdfR θ b - cdfR θ a = (θ (Ioc a b)).toReal := by
  have := h.prob
  unfold cdfR
  rw [← Iic_union_Ioc_eq_Iic hab, measure_union (Iic_disjoint_Ioc le_rfl) measurableSet_Ioc,
    ENNReal.toReal_add (measure_ne_top _ _) (measure_ne_top _ _)]
  ring

theorem AdmissibleOn.cdf_mono (h : AdmissibleOn U θ) : Monotone (cdfR θ) := by
  intro a b hab
  have := h.cdf_sub hab
  have : 0 ≤ (θ (Ioc a b)).toReal := ENNReal.toReal_nonneg
  linarith

theorem AdmissibleOn.cdf_sub_le (h : AdmissibleOn U θ) {a b : ℝ} (hab : a ≤ b) :
    cdfR θ b - cdfR θ a ≤ b - a := by
  rw [h.cdf_sub hab]
  exact ENNReal.toReal_le_of_le_ofReal (by linarith) (h.Ioc_le hab)

theorem AdmissibleOn.cdf_continuous (h : AdmissibleOn U θ) : Continuous (cdfR θ) := by
  apply LipschitzWith.continuous (K := 1)
  apply LipschitzWith.of_dist_le_mul
  intro a b
  simp only [NNReal.coe_one, one_mul, Real.dist_eq]
  rcases le_total a b with hab | hab
  · rw [abs_sub_comm, abs_of_nonneg (by linarith [h.cdf_mono hab]), abs_sub_comm,
      abs_of_nonneg (by linarith)]
    exact h.cdf_sub_le hab
  · rw [abs_of_nonneg (by linarith [h.cdf_mono hab]), abs_of_nonneg (by linarith)]
    exact h.cdf_sub_le hab

theorem AdmissibleOn.cdf_zero (h : AdmissibleOn U θ) : cdfR θ 0 = 0 := by
  simp [cdfR, h.le_zero]

theorem AdmissibleOn.cdf_U (h : AdmissibleOn U θ) : cdfR θ U = 1 := by
  have := h.prob
  unfold cdfR
  rw [← compl_Ioi, prob_compl_eq_one_sub measurableSet_Ioi, h.gt_U]; simp

theorem AdmissibleOn.U_pos (h : AdmissibleOn U θ) : 0 < U := by
  by_contra hU
  push Not at hU
  have h1 := h.cdf_U
  have h2 := h.cdf_mono hU
  rw [h.cdf_zero, h1] at h2
  linarith

theorem AdmissibleOn.exists_quantile (h : AdmissibleOn U θ) {v : ℝ} (hv0 : 0 ≤ v) (hv1 : v ≤ 1) :
    ∃ x ∈ Icc 0 U, cdfR θ x = v := by
  have := intermediate_value_Icc h.U_pos.le h.cdf_continuous.continuousOn
  rw [h.cdf_zero, h.cdf_U] at this
  exact this ⟨hv0, hv1⟩

/-- Quantile points `t_m` with `θ(0, t_m] = m/2n` (for `m ≤ 2n`). -/
noncomputable def qpt (h : AdmissibleOn U θ) (n m : ℕ) : ℝ :=
  Classical.choose (h.exists_quantile (v := min ((m : ℝ) / (2 * n)) 1)
    (le_min (by positivity) zero_le_one) (min_le_right _ _))

theorem qpt_mem (h : AdmissibleOn U θ) (n m : ℕ) : qpt h n m ∈ Icc 0 U :=
  (Classical.choose_spec (h.exists_quantile (v := min ((m : ℝ) / (2 * n)) 1)
    (le_min (by positivity) zero_le_one) (min_le_right _ _))).1

theorem cdf_qpt (h : AdmissibleOn U θ) {n m : ℕ} (hn : 1 ≤ n) (hm : m ≤ 2 * n) :
    cdfR θ (qpt h n m) = (m : ℝ) / (2 * n) := by
  have := (Classical.choose_spec (h.exists_quantile (v := min ((m : ℝ) / (2 * n)) 1)
    (le_min (by positivity) zero_le_one) (min_le_right _ _))).2
  rw [qpt, this, min_eq_left]
  rw [div_le_one (by positivity)]; exact_mod_cast hm

/-- Gaps: `t_m + (m' − m)/2n ≤ t_{m'}`. -/
theorem qpt_gap (h : AdmissibleOn U θ) {n m m' : ℕ} (hn : 1 ≤ n) (hmm : m ≤ m') (hm' : m' ≤ 2 * n) :
    qpt h n m + ((m' : ℝ) - m) / (2 * n) ≤ qpt h n m' := by
  have e1 := cdf_qpt h hn (hmm.trans hm')
  have e2 := cdf_qpt h hn hm'
  have hdiff : ((m' : ℝ) - m) / (2 * n) = cdfR θ (qpt h n m') - cdfR θ (qpt h n m) := by
    rw [e1, e2]; ring
  rcases le_or_gt (qpt h n m) (qpt h n m') with hle | hlt
  · have := h.cdf_sub_le hle
    linarith
  · have := h.cdf_mono hlt.le
    have hz : ((m' : ℝ) - m) / (2 * n) ≤ 0 := by linarith
    have : (m : ℝ) ≤ m' := by exact_mod_cast hmm
    have : 0 ≤ ((m' : ℝ) - m) / (2 * n) := div_nonneg (by linarith) (by positivity)
    have h0 : ((m' : ℝ) - m) / (2 * n) = 0 := by linarith
    rw [div_eq_zero_iff] at h0
    rcases h0 with h0 | h0
    · have : m' = m := by exact_mod_cast (sub_eq_zero.1 h0)
      subst this; exact absurd hlt (lt_irrefl _)
    · have : (0 : ℝ) < 2 * n := by positivity
      linarith

theorem qpt_mono (h : AdmissibleOn U θ) {n m m' : ℕ} (hn : 1 ≤ n) (hmm : m ≤ m') (hm' : m' ≤ 2 * n) :
    qpt h n m ≤ qpt h n m' := by
  have := qpt_gap h hn hmm hm'
  have : (m : ℝ) ≤ m' := by exact_mod_cast hmm
  have : 0 ≤ ((m' : ℝ) - m) / (2 * n) := div_nonneg (by linarith) (by positivity)
  linarith

theorem qpt_mass (h : AdmissibleOn U θ) {n m m' : ℕ} (hn : 1 ≤ n) (hmm : m ≤ m') (hm' : m' ≤ 2 * n) :
    θ (Ioc (qpt h n m) (qpt h n m')) = ENNReal.ofReal (((m' : ℝ) - m) / (2 * n)) := by
  have := h.prob
  have := h.cdf_sub (qpt_mono h hn hmm hm')
  rw [cdf_qpt h hn hm', cdf_qpt h hn (hmm.trans hm')] at this
  rw [← ENNReal.ofReal_toReal (measure_ne_top θ _), ← this]
  ring_nf

theorem qpt_full (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) :
    θ (Ioc (qpt h n 0) (qpt h n (2 * n)))ᶜ = 0 := by
  have := h.prob
  rw [prob_compl_eq_zero_iff measurableSet_Ioc, qpt_mass h hn (Nat.zero_le _) le_rfl]
  have : ((((2 * n : ℕ) : ℝ) - ((0 : ℕ) : ℝ)) / (2 * n)) = 1 := by
    push_cast; rw [sub_zero]; field_simp
  rw [this, ENNReal.ofReal_one]

/-! ### The configuration `k_i = ⌈n t_{2i+1}⌉` -/

/-- The quantile `q_i = t_{2i+1}`. -/
noncomputable def qq (h : AdmissibleOn U θ) (n i : ℕ) : ℝ := qpt h n (2 * i + 1)

/-- `k_i = ⌈n q_i⌉`. -/
noncomputable def kq (h : AdmissibleOn U θ) (n i : ℕ) : ℕ := ⌈(n : ℝ) * qq h n i⌉₊

/-- `u_i = k_i / n`. -/
noncomputable def uq (h : AdmissibleOn U θ) (n i : ℕ) : ℝ := (kq h n i : ℝ) / n

theorem qq_pos (h : AdmissibleOn U θ) {n i : ℕ} (hn : 1 ≤ n) (hi : i < n) : 0 < qq h n i := by
  have := qpt_gap h hn (Nat.zero_le (2 * i + 1)) (by omega)
  have h0 := (qpt_mem h n 0).1
  have : 0 < (((2 * i + 1 : ℕ) : ℝ) - ((0 : ℕ) : ℝ)) / (2 * n) := by push_cast; rw [sub_zero]; positivity
  unfold qq; linarith

theorem qq_gap (h : AdmissibleOn U θ) {n i j : ℕ} (hn : 1 ≤ n) (hij : i ≤ j) (hj : j < n) :
    qq h n i + ((j : ℝ) - i) / n ≤ qq h n j := by
  have := qpt_gap h hn (show 2 * i + 1 ≤ 2 * j + 1 by omega) (by omega)
  have e : (((2 * j + 1 : ℕ) : ℝ) - ((2 * i + 1 : ℕ) : ℝ)) / (2 * n) = ((j : ℝ) - i) / n := by
    push_cast; field_simp; ring
  unfold qq; linarith

theorem uq_ge (h : AdmissibleOn U θ) {n i : ℕ} (hn : 1 ≤ n) : qq h n i ≤ uq h n i := by
  unfold uq kq
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [le_div_iff₀ hn', mul_comm]; exact Nat.le_ceil _

theorem uq_lt (h : AdmissibleOn U θ) {n i : ℕ} (hn : 1 ≤ n) (hi : i < n) :
    uq h n i < qq h n i + 1 / n := by
  unfold uq kq
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have := Nat.ceil_lt_add_one (mul_nonneg hn'.le (qq_pos h hn hi).le)
  rw [div_lt_iff₀ hn']
  calc (⌈(n : ℝ) * qq h n i⌉₊ : ℝ) < n * qq h n i + 1 := this
    _ = (qq h n i + 1 / n) * n := by field_simp

theorem kq_add_le (h : AdmissibleOn U θ) {n i j : ℕ} (hn : 1 ≤ n) (hij : i ≤ j) (hj : j < n) :
    kq h n i + (j - i) ≤ kq h n j := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hg := qq_gap h hn hij hj
  unfold kq
  have h1 : (n : ℝ) * qq h n i + ((j - i : ℕ) : ℝ) ≤ n * qq h n j := by
    rw [Nat.cast_sub hij]
    have : (n : ℝ) * (((j : ℝ) - i) / n) = (j : ℝ) - i := by field_simp
    nlinarith
  calc ⌈(n : ℝ) * qq h n i⌉₊ + (j - i) = ⌈(n : ℝ) * qq h n i + ((j - i : ℕ) : ℝ)⌉₊ :=
        (Nat.ceil_add_natCast (mul_nonneg hn'.le (qq_pos h hn (lt_of_le_of_lt hij hj)).le) _).symm
    _ ≤ _ := Nat.ceil_mono h1

theorem kq_pos (h : AdmissibleOn U θ) {n i : ℕ} (hn : 1 ≤ n) (hi : i < n) : 1 ≤ kq h n i := by
  unfold kq
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  exact Nat.one_le_iff_ne_zero.2 (by
    rw [Ne, Nat.ceil_eq_zero, not_le]; exact mul_pos hn' (qq_pos h hn hi))

theorem kq_le (h : AdmissibleOn U θ) {n i : ℕ} : kq h n i ≤ n * ⌈U⌉₊ := by
  unfold kq
  have : (n : ℝ) * qq h n i ≤ ((n * ⌈U⌉₊ : ℕ) : ℝ) := by
    push_cast
    exact mul_le_mul_of_nonneg_left ((qpt_mem h n _).2.trans (Nat.le_ceil U)) (Nat.cast_nonneg n)
  exact (Nat.ceil_mono this).trans (by rw [Nat.ceil_natCast])

theorem uq_pos (h : AdmissibleOn U θ) {n i : ℕ} (hn : 1 ≤ n) (hi : i < n) : 0 < uq h n i :=
  (qq_pos h hn hi).trans_le (uq_ge h hn)

theorem uq_le (h : AdmissibleOn U θ) {n i : ℕ} (hn : 1 ≤ n) (hi : i < n) : uq h n i ≤ U + 1 := by
  have := uq_lt h hn hi
  have := (qpt_mem h n (2 * i + 1)).2
  have : 1 / (n : ℝ) ≤ 1 := by rw [div_le_one (by exact_mod_cast hn)]; exact_mod_cast hn
  unfold qq at *; linarith

theorem uq_gap (h : AdmissibleOn U θ) {n i j : ℕ} (hn : 1 ≤ n) (hij : i < j) (hj : j < n) :
    uq h n i + 1 / n ≤ uq h n j := by
  have := kq_add_le h hn hij.le hj
  have hk : (kq h n i : ℝ) + 1 ≤ kq h n j := by
    have : kq h n i + 1 ≤ kq h n j := by omega
    exact_mod_cast this
  unfold uq
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [← add_div]; exact div_le_div_of_nonneg_right hk hn'.le

/-! ### Pointwise comparisons -/

/-- Monotonicity of `F`: `0 < a ≤ u < v ≤ b ⇒ F(u,v) ≤ F(a,b)`. -/
theorem Fp_le_of {p a u v b : ℝ} (hp : 0 < p) (ha : 0 < a) (hau : a ≤ u) (huv : u < v) (hvb : v ≤ b) :
    Fp p u v ≤ Fp p a b := by
  have hu : 0 < u := ha.trans_le hau
  have hv : 0 < v := hu.trans huv
  have h1 : v ^ (-p) < u ^ (-p) := rpow_lt_rpow_of_neg hu huv (by linarith)
  have h2 : u ^ (-p) ≤ a ^ (-p) := rpow_le_rpow_of_nonpos ha hau (by linarith)
  have h3 : b ^ (-p) ≤ v ^ (-p) := rpow_le_rpow_of_nonpos hv hvb (by linarith)
  unfold Fp
  rw [abs_of_pos (by linarith), abs_of_pos (by linarith)]
  exact Real.log_le_log (by linarith) (by linarith)

/-- Mean value bound: `p b^{-p-1} (b − a) ≤ a^{-p} − b^{-p}` for `0 < a ≤ b`. -/
theorem rpow_neg_sub_ge {p a b : ℝ} (hp : 0 < p) (ha : 0 < a) (hab : a ≤ b) :
    p * b ^ (-p - 1) * (b - a) ≤ a ^ (-p) - b ^ (-p) := by
  rcases hab.eq_or_lt with rfl | hab
  · simp
  have hcont : ContinuousOn (fun x : ℝ => x ^ (-p)) (Icc a b) := fun x hx =>
    (continuousAt_rpow_const x (-p) (Or.inl (ha.trans_le hx.1).ne')).continuousWithinAt
  have hder : ∀ x ∈ Ioo a b, HasDerivAt (fun x : ℝ => x ^ (-p)) (-p * x ^ (-p - 1)) x := fun x hx =>
    Real.hasDerivAt_rpow_const (Or.inl (ha.trans hx.1).ne')
  obtain ⟨c, hc, hcd⟩ := exists_hasDerivAt_eq_slope (fun x : ℝ => x ^ (-p)) (fun x => -p * x ^ (-p - 1))
    hab hcont hder
  have hc0 : 0 < c := ha.trans hc.1
  have hcb : b ^ (-p - 1) ≤ c ^ (-p - 1) := rpow_le_rpow_of_nonpos hc0 hc.2.le (by linarith)
  have hba : 0 < b - a := by linarith
  rw [eq_div_iff hba.ne'] at hcd
  nlinarith [mul_le_mul_of_nonneg_right hcb (mul_nonneg hp.le hba.le)]

/-- Near pairs: `F(u_i, u_j) ≥ log (p (U+1)^{-p-1}) − log n`. -/
theorem near_ge (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p) {n i j : ℕ} (hn : 1 ≤ n) (hij : i < j)
    (hj : j < n) : Real.log (p * (U + 1) ^ (-p - 1)) - Real.log n ≤ Fp p (uq h n i) (uq h n j) := by
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  have hi := uq_pos h hn (hij.trans hj)
  have hg := uq_gap h hn hij hj
  have hle := uq_le h hn hj
  have hU := h.U_pos
  have hn1 : 0 < 1 / (n : ℝ) := by positivity
  have hij' : uq h n i ≤ uq h n j := by linarith
  have hj0 : 0 < uq h n j := hi.trans_le hij'
  have hmv := rpow_neg_sub_ge hp hi hij'
  have hb : (U + 1) ^ (-p - 1) ≤ uq h n j ^ (-p - 1) := rpow_le_rpow_of_nonpos hj0 hle (by linarith)
  have hpos : 0 < p * (U + 1) ^ (-p - 1) := mul_pos hp (rpow_pos_of_pos (by linarith) _)
  have key : p * (U + 1) ^ (-p - 1) / n ≤ uq h n i ^ (-p) - uq h n j ^ (-p) := by
    calc p * (U + 1) ^ (-p - 1) / n = p * (U + 1) ^ (-p - 1) * (1 / n) := by ring
      _ ≤ p * uq h n j ^ (-p - 1) * (uq h n j - uq h n i) := by
          apply mul_le_mul (mul_le_mul_of_nonneg_left hb hp.le) (by linarith) (by positivity)
          exact mul_nonneg hp.le (rpow_pos_of_pos hj0 _).le
      _ ≤ _ := hmv
  rw [← Real.log_div hpos.ne' hn'.ne', Fp]
  exact Real.log_le_log (by positivity) (key.trans (le_abs_self _))

/-! ### Blocks and the far-pair comparison -/

/-- Block `B_a = (t_{2a}, t_{2a+2}]`. -/
noncomputable def blk (h : AdmissibleOn U θ) (n a : ℕ) : Set ℝ := Ioc (qpt h n (2 * a)) (qpt h n (2 * a + 2))

theorem blk_mass (h : AdmissibleOn U θ) {n a : ℕ} (hn : 1 ≤ n) (ha : a < n) :
    θ (blk h n a) = ENNReal.ofReal (1 / n) := by
  rw [blk, qpt_mass h hn (by omega) (by omega)]
  congr 1; push_cast; field_simp; ring

theorem blk_real (h : AdmissibleOn U θ) {n a : ℕ} (hn : 1 ≤ n) (ha : a < n) :
    θ.real (blk h n a) = 1 / n := by
  rw [Measure.real, blk_mass h hn ha, ENNReal.toReal_ofReal (by positivity)]

theorem blk_disjoint (h : AdmissibleOn U θ) {n a b : ℕ} (hn : 1 ≤ n) (hab : a ≠ b) (ha : a < n) (hb : b < n) :
    Disjoint (blk h n a) (blk h n b) := by
  wlog hlt : a < b generalizing a b
  · exact (this hab.symm hb ha (lt_of_le_of_ne (not_lt.1 hlt) hab.symm)).symm
  rw [Set.disjoint_left]
  intro x hxa hxb
  have := qpt_mono h hn (show 2 * a + 2 ≤ 2 * b by omega) (by omega)
  exact absurd (hxa.2.trans this) (not_le.2 hxb.1)

theorem far_pointwise (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p) {n i j : ℕ} (hn : 1 ≤ n)
    (hij : i + 4 ≤ j) (hj : j < n) {u v : ℝ} (hu : u ∈ blk h n (i + 2)) (hv : v ∈ blk h n (j - 1)) :
    u < v ∧ Fp p u v ≤ Fp p (uq h n i) (uq h n j) := by
  have e1 : 2 * (j - 1) + 2 = 2 * j := by omega
  rw [blk, e1] at hv
  rw [blk] at hu
  have g1 := qpt_gap h hn (show 2 * i + 1 ≤ 2 * i + 3 by omega) (by omega)
  have e2 : (((2 * i + 3 : ℕ) : ℝ) - ((2 * i + 1 : ℕ) : ℝ)) / (2 * n) = 1 / n := by
    push_cast; field_simp; ring
  rw [e2] at g1
  have m1 := qpt_mono h hn (show 2 * i + 3 ≤ 2 * (i + 2) by omega) (by omega)
  have m2 := qpt_mono h hn (show 2 * (i + 2) + 2 ≤ 2 * (j - 1) by omega) (by omega)
  have m3 := qpt_mono h hn (show 2 * (j - 1) ≤ 2 * j by omega) (by omega)
  have m4 := qpt_mono h hn (show 2 * j ≤ 2 * j + 1 by omega) (by omega)
  have hui := uq_lt h hn (show i < n by omega)
  have huj := uq_ge h hn (θ := θ) (n := n) (i := j)
  have hi0 := uq_pos h hn (show i < n by omega)
  unfold qq at hui huj
  have hlt : u < v := by
    have : qpt h n (2 * (j - 1)) < v := by
      have := hv.1
      have e3 : 2 * (j - 1) = 2 * j - 2 := by omega
      linarith [qpt_mono h hn (show 2 * (j - 1) ≤ 2 * (j - 1) by omega) (by omega)]
    linarith [hu.2]
  refine ⟨hlt, Fp_le_of hp hi0 (by linarith [hu.1]) hlt (by linarith [hv.2])⟩

/-! ### The decomposition of `𝒥_p(θ)` -/

/-- The far pairs `i + 4 ≤ j < n`. -/
def farS (n : ℕ) : Finset (ℕ × ℕ) := ((range n) ×ˢ (range n)).filter (fun ij => ij.1 + 4 ≤ ij.2)

/-- The rectangle `B_{i+2} × B_{j−1}`. -/
noncomputable def rect (h : AdmissibleOn U θ) (n : ℕ) (ij : ℕ × ℕ) : Set (ℝ × ℝ) :=
  blk h n (ij.1 + 2) ×ˢ blk h n (ij.2 - 1)

/-- `D = ⋃_{far} B_{i+2} × B_{j−1}`. -/
noncomputable def Dset (h : AdmissibleOn U θ) (n : ℕ) : Set (ℝ × ℝ) := ⋃ ij ∈ farS n, rect h n ij

theorem mem_farS {n : ℕ} {ij : ℕ × ℕ} : ij ∈ farS n ↔ ij.1 + 4 ≤ ij.2 ∧ ij.2 < n := by
  simp only [farS, Finset.mem_filter, Finset.mem_product, Finset.mem_range]; omega

theorem measurableSet_rect (h : AdmissibleOn U θ) (n : ℕ) (ij : ℕ × ℕ) : MeasurableSet (rect h n ij) :=
  measurableSet_Ioc.prod measurableSet_Ioc

theorem measurableSet_Dset (h : AdmissibleOn U θ) (n : ℕ) : MeasurableSet (Dset h n) :=
  Finset.measurableSet_biUnion _ fun ij _ => measurableSet_rect h n ij

theorem rect_disjoint (h : AdmissibleOn U θ) {n : ℕ} (hn : 1 ≤ n) :
    Set.Pairwise (↑(farS n) : Set (ℕ × ℕ)) (Function.onFun Disjoint (rect h n)) := by
  intro ij hij kl hkl hne
  rw [Finset.mem_coe, mem_farS] at hij hkl
  simp only [Function.onFun, rect]
  rw [Set.disjoint_prod]
  by_cases h1 : ij.1 = kl.1
  · right
    have h2 : ij.2 ≠ kl.2 := fun h2 => hne (Prod.ext h1 h2)
    exact blk_disjoint h hn (by omega) (by omega) (by omega)
  · left; exact blk_disjoint h hn (by omega) (by omega) (by omega)

theorem Dset_lt (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p) {n : ℕ} (hn : 1 ≤ n) {z : ℝ × ℝ}
    (hz : z ∈ Dset h n) : z.1 < z.2 := by
  simp only [Dset, mem_iUnion] at hz
  obtain ⟨ij, hij, hz⟩ := hz
  rw [mem_farS] at hij
  exact (far_pointwise h hp hn hij.1 hij.2 hz.1 hz.2).1

theorem integral_Dset_le (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p) {n : ℕ} (hn : 1 ≤ n)
    (hint : Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) (θ.prod θ)) :
    (n : ℝ) ^ 2 * ∫ z in Dset h n, Fp p z.1 z.2 ∂(θ.prod θ) ≤
      ∑ ij ∈ farS n, Fp p (uq h n ij.1) (uq h n ij.2) := by
  have := h.prob
  have hn' : (0 : ℝ) < n := by exact_mod_cast hn
  rw [Dset, integral_biUnion_finset _ (fun ij _ => measurableSet_rect h n ij) (rect_disjoint h hn)
    (fun ij _ => hint.integrableOn), Finset.mul_sum]
  apply Finset.sum_le_sum
  intro ij hij
  rw [mem_farS] at hij
  have hle : ∫ z in rect h n ij, Fp p z.1 z.2 ∂(θ.prod θ) ≤
      ∫ z in rect h n ij, Fp p (uq h n ij.1) (uq h n ij.2) ∂(θ.prod θ) :=
    setIntegral_mono_on hint.integrableOn (integrableOn_const (by simp) (by simp))
      (measurableSet_rect h n ij) (fun z hz => (far_pointwise h hp hn hij.1 hij.2 hz.1 hz.2).2)
  rw [setIntegral_const, smul_eq_mul, rect, Measure.real, Measure.prod_prod, ENNReal.toReal_mul] at hle
  rw [← Measure.real, ← Measure.real, blk_real h hn (by omega), blk_real h hn (by omega)] at hle
  calc (n : ℝ) ^ 2 * ∫ z in rect h n ij, Fp p z.1 z.2 ∂(θ.prod θ)
      ≤ (n : ℝ) ^ 2 * (1 / n * (1 / n) * Fp p (uq h n ij.1) (uq h n ij.2)) :=
        mul_le_mul_of_nonneg_left hle (by positivity)
    _ = _ := by field_simp

/-- The swapped set `D' = swap⁻¹ D` carries the same integral. -/
theorem integral_Dswap (h : AdmissibleOn U θ) {p : ℝ} (n : ℕ) :
    ∫ z in Prod.swap ⁻¹' Dset h n, Fp p z.1 z.2 ∂(θ.prod θ) = ∫ z in Dset h n, Fp p z.1 z.2 ∂(θ.prod θ) := by
  have := h.prob
  have hD := measurableSet_Dset h n
  rw [← integral_indicator (measurable_swap hD), ← integral_indicator hD]
  have e : (Prod.swap ⁻¹' Dset h n).indicator (fun z : ℝ × ℝ => Fp p z.1 z.2) =
      fun z => (Dset h n).indicator (fun z : ℝ × ℝ => Fp p z.1 z.2) z.swap := by
    funext z
    by_cases hz : z.swap ∈ Dset h n
    · rw [indicator_of_mem (show z ∈ Prod.swap ⁻¹' Dset h n from hz), indicator_of_mem hz]
      exact Fp_comm p _ _
    · rw [indicator_of_notMem (show z ∉ Prod.swap ⁻¹' Dset h n from hz), indicator_of_notMem hz]
  rw [e]
  exact integral_prod_swap (μ := θ) (ν := θ) ((Dset h n).indicator fun z : ℝ × ℝ => Fp p z.1 z.2)

/-- The bad set: outside the support square, diagonal blocks, and the strips of `B_0, B_1, B_{n−1}`. -/
noncomputable def Ebad (h : AdmissibleOn U θ) (n : ℕ) : Set (ℝ × ℝ) :=
  (Ioc (qpt h n 0) (qpt h n (2 * n)) ×ˢ Ioc (qpt h n 0) (qpt h n (2 * n)))ᶜ ∪
    (⋃ a ∈ range n, blk h n a ×ˢ blk h n a) ∪
    (⋃ a ∈ ({0, 1, n - 1} : Finset ℕ), (blk h n a ×ˢ univ ∪ univ ×ˢ blk h n a))

theorem measurableSet_Ebad (h : AdmissibleOn U θ) (n : ℕ) : MeasurableSet (Ebad h n) := by
  unfold Ebad
  refine ((measurableSet_Ioc.prod measurableSet_Ioc).compl.union ?_).union ?_
  · exact Finset.measurableSet_biUnion _ fun a _ => measurableSet_Ioc.prod measurableSet_Ioc
  · exact Finset.measurableSet_biUnion _ fun a _ =>
      (measurableSet_Ioc.prod MeasurableSet.univ).union (MeasurableSet.univ.prod measurableSet_Ioc)

theorem exists_blk (h : AdmissibleOn U θ) {n : ℕ} {x : ℝ} (hx : x ∈ Ioc (qpt h n 0) (qpt h n (2 * n))) :
    ∃ a < n, x ∈ blk h n a := by
  classical
  have hex : ∃ m, x ≤ qpt h n (2 * m) := ⟨n, hx.2⟩
  set m0 := Nat.find hex with hm0
  have hspec : x ≤ qpt h n (2 * m0) := Nat.find_spec hex
  have hm0n : m0 ≤ n := Nat.find_min' hex hx.2
  have hm00 : m0 ≠ 0 := by
    intro h0; rw [h0] at hspec; simp at hspec; exact absurd hspec (not_le.2 hx.1)
  refine ⟨m0 - 1, by omega, ?_, ?_⟩
  · have := Nat.find_min hex (show m0 - 1 < m0 by omega)
    exact lt_of_not_ge this
  · rw [show 2 * (m0 - 1) + 2 = 2 * m0 by omega]; exact hspec

theorem cover (h : AdmissibleOn U θ) {n : ℕ} (hn : 2 ≤ n) :
    (Dset h n ∪ Prod.swap ⁻¹' Dset h n)ᶜ ⊆ Ebad h n := by
  intro z hz
  by_contra hE
  apply hz
  simp only [Ebad, mem_union, mem_compl_iff, not_or, not_not, mem_iUnion, Finset.mem_range, exists_prop,
    not_exists, not_and, Finset.mem_insert, Finset.mem_singleton] at hE
  obtain ⟨⟨hsq, hdiag⟩, hstrip⟩ := hE
  obtain ⟨a, ha, hza⟩ := exists_blk h hsq.1
  obtain ⟨b, hb, hzb⟩ := exists_blk h hsq.2
  have hab : a ≠ b := fun e => hdiag a ha (by rw [e] at hza ⊢; exact ⟨hza, hzb⟩)
  have hA : a ≠ 0 ∧ a ≠ 1 ∧ a ≠ n - 1 := by
    refine ⟨fun e => ?_, fun e => ?_, fun e => ?_⟩ <;>
    exact (hstrip a (by omega)).1 ⟨hza, mem_univ _⟩
  have hB : b ≠ 0 ∧ b ≠ 1 ∧ b ≠ n - 1 := by
    refine ⟨fun e => ?_, fun e => ?_, fun e => ?_⟩ <;>
    exact (hstrip b (by omega)).2 ⟨mem_univ _, hzb⟩
  rcases lt_or_gt_of_ne hab with hlt | hlt
  · left
    simp only [Dset, mem_iUnion]
    refine ⟨(a - 2, b + 1), mem_farS.2 ⟨by simp only; omega, by simp only; omega⟩, ?_, ?_⟩
    · simp only; rw [show a - 2 + 2 = a by omega]; exact hza
    · simp only; rw [show b + 1 - 1 = b by omega]; exact hzb
  · right
    simp only [Dset, mem_iUnion, Set.mem_preimage]
    refine ⟨(b - 2, a + 1), mem_farS.2 ⟨by simp only; omega, by simp only; omega⟩, ?_, ?_⟩
    · simp only; rw [show b - 2 + 2 = b by omega]; exact hzb
    · simp only; rw [show a + 1 - 1 = a by omega]; exact hza

theorem measure_Ebad_le (h : AdmissibleOn U θ) {n : ℕ} (hn : 2 ≤ n) :
    (θ.prod θ) (Ebad h n) ≤ ENNReal.ofReal (7 / n) := by
  have := h.prob
  have hn1 : 1 ≤ n := by omega
  set A := Ioc (qpt h n 0) (qpt h n (2 * n))
  have hA : θ Aᶜ = 0 := qpt_full h hn1
  have h1 : (θ.prod θ) (A ×ˢ A)ᶜ = 0 := by
    apply measure_mono_null (t := Aᶜ ×ˢ Set.univ ∪ Set.univ ×ˢ Aᶜ)
    · intro z hz
      simp only [mem_compl_iff, mem_prod, not_and_or] at hz
      rcases hz with hz | hz
      · exact Or.inl ⟨hz, mem_univ _⟩
      · exact Or.inr ⟨mem_univ _, hz⟩
    · apply measure_union_null <;> rw [Measure.prod_prod] <;> simp [hA]
  have h2 : (θ.prod θ) (⋃ a ∈ range n, blk h n a ×ˢ blk h n a) ≤ ENNReal.ofReal (1 / n) := by
    refine (measure_biUnion_finset_le _ _).trans (le_of_eq ?_)
    calc ∑ a ∈ range n, (θ.prod θ) (blk h n a ×ˢ blk h n a)
        = ∑ a ∈ range n, ENNReal.ofReal (1 / n) * ENNReal.ofReal (1 / n) := by
          apply Finset.sum_congr rfl; intro a ha
          rw [Measure.prod_prod, blk_mass h hn1 (Finset.mem_range.1 ha)]
      _ = ENNReal.ofReal (1 / n) := by
          rw [Finset.sum_const, Finset.card_range, ← ENNReal.ofReal_mul (by positivity), nsmul_eq_mul,
            ← ENNReal.ofReal_natCast, ← ENNReal.ofReal_mul (by positivity)]
          congr 1; field_simp
  have h3 : (θ.prod θ) (⋃ a ∈ ({0, 1, n - 1} : Finset ℕ), (blk h n a ×ˢ Set.univ ∪ Set.univ ×ˢ blk h n a)) ≤
      ENNReal.ofReal (6 / n) := by
    refine (measure_biUnion_finset_le _ _).trans ?_
    have hterm : ∀ a ∈ ({0, 1, n - 1} : Finset ℕ),
        (θ.prod θ) (blk h n a ×ˢ Set.univ ∪ Set.univ ×ˢ blk h n a) ≤ ENNReal.ofReal (2 / n) := by
      intro a ha
      have han : a < n := by simp only [Finset.mem_insert, Finset.mem_singleton] at ha; omega
      refine (measure_union_le _ _).trans ?_
      rw [Measure.prod_prod, Measure.prod_prod, blk_mass h hn1 han, measure_univ, mul_one, one_mul,
        ← ENNReal.ofReal_add (by positivity) (by positivity)]
      apply ENNReal.ofReal_le_ofReal; rw [← add_div]; norm_num
    calc ∑ a ∈ ({0, 1, n - 1} : Finset ℕ), (θ.prod θ) (blk h n a ×ˢ Set.univ ∪ Set.univ ×ˢ blk h n a)
        ≤ ∑ a ∈ ({0, 1, n - 1} : Finset ℕ), ENNReal.ofReal (2 / n) := Finset.sum_le_sum hterm
      _ = (({0, 1, n - 1} : Finset ℕ).card : ℝ≥0∞) * ENNReal.ofReal (2 / n) := by
          rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ 3 * ENNReal.ofReal (2 / n) := by
          gcongr
          exact_mod_cast Finset.card_le_three
      _ = ENNReal.ofReal (6 / n) := by
          rw [show (3 : ℝ≥0∞) = ENNReal.ofReal 3 by simp, ← ENNReal.ofReal_mul (by norm_num)]
          congr 1; ring
  calc (θ.prod θ) (Ebad h n) ≤ (θ.prod θ) (A ×ˢ A)ᶜ + (θ.prod θ) (⋃ a ∈ range n, blk h n a ×ˢ blk h n a) +
        (θ.prod θ) (⋃ a ∈ ({0, 1, n - 1} : Finset ℕ), (blk h n a ×ˢ Set.univ ∪ Set.univ ×ˢ blk h n a)) :=
        (measure_union_le _ _).trans (add_le_add_left (measure_union_le _ _) _)
    _ ≤ 0 + ENNReal.ofReal (1 / n) + ENNReal.ofReal (6 / n) := by rw [h1]; gcongr
    _ = ENNReal.ofReal (7 / n) := by
        rw [zero_add, ← ENNReal.ofReal_add (by positivity) (by positivity)]; congr 1; ring

/-! ### Conclusion of Step 3 -/

/-- The pairs `i < j < n`. -/
def ltS (n : ℕ) : Finset (ℕ × ℕ) := ((range n) ×ˢ (range n)).filter (fun ij => ij.1 < ij.2)

theorem farS_eq (n : ℕ) : farS n = (ltS n).filter (fun ij => ij.1 + 4 ≤ ij.2) := by
  ext ij; simp only [farS, ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_range]; omega

theorem card_near_le (n : ℕ) : ((ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2)).card ≤ 3 * n := by
  have hsub : (ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2) ⊆
      ((range n) ×ˢ (range 3)).image (fun id => (id.1, id.1 + id.2 + 1)) := by
    intro ij hij
    simp only [ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_range] at hij
    simp only [Finset.mem_image, Finset.mem_product, Finset.mem_range]
    exact ⟨(ij.1, ij.2 - ij.1 - 1), ⟨by omega, by simp only; omega⟩, by ext <;> simp only <;> omega⟩
  calc _ ≤ _ := Finset.card_le_card hsub
    _ ≤ ((range n) ×ˢ (range 3)).card := Finset.card_image_le
    _ = 3 * n := by rw [Finset.card_product, Finset.card_range, Finset.card_range, mul_comm]

/-- **Step 3 (deterministic form)**: `n² 𝒥(θ) ≤ 2 Σ_{i<j} F(u_i, u_j) + n² ∫_{Ebad} |F| + 6n (log n + |c_U|)`. -/
theorem quantile_sum_ge (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p)
    (hint : Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) (θ.prod θ)) {n : ℕ} (hn : 2 ≤ n) :
    (n : ℝ) ^ 2 * Jp p θ ≤ 2 * ∑ ij ∈ ltS n, Fp p (uq h n ij.1) (uq h n ij.2) +
      (n : ℝ) ^ 2 * ∫ z in Ebad h n, |Fp p z.1 z.2| ∂(θ.prod θ) +
      6 * n * (Real.log n + |Real.log (p * (U + 1) ^ (-p - 1))|) := by
  have := h.prob
  have hn1 : 1 ≤ n := by omega
  set G : ℝ × ℝ → ℝ := fun z => Fp p z.1 z.2 with hG
  set D := Dset h n
  have hDm := measurableSet_Dset h n
  have hD'm : MeasurableSet (Prod.swap ⁻¹' D) := measurable_swap hDm
  have hdisj : Disjoint D (Prod.swap ⁻¹' D) := by
    rw [Set.disjoint_left]
    intro z hz hz'
    have h1 := Dset_lt h hp hn1 hz
    have h2 := Dset_lt h hp hn1 (show z.swap ∈ D from hz')
    simp only [Prod.fst_swap, Prod.snd_swap] at h2
    linarith
  -- J = 2 ∫_D G + ∫_{(D ∪ D')ᶜ} G
  have hsplit : Jp p θ = 2 * ∫ z in D, G z ∂(θ.prod θ) + ∫ z in (D ∪ Prod.swap ⁻¹' D)ᶜ, G z ∂(θ.prod θ) := by
    rw [Jp, ← integral_add_compl (hDm.union hD'm) hint,
      setIntegral_union hdisj hD'm hint.integrableOn hint.integrableOn, integral_Dswap h n]
    ring
  have hrest : ∫ z in (D ∪ Prod.swap ⁻¹' D)ᶜ, G z ∂(θ.prod θ) ≤ ∫ z in Ebad h n, |G z| ∂(θ.prod θ) := by
    calc ∫ z in (D ∪ Prod.swap ⁻¹' D)ᶜ, G z ∂(θ.prod θ) ≤ ∫ z in (D ∪ Prod.swap ⁻¹' D)ᶜ, |G z| ∂(θ.prod θ) :=
          setIntegral_mono hint.integrableOn hint.abs.integrableOn (fun z => le_abs_self _)
      _ ≤ _ := setIntegral_mono_set hint.abs.integrableOn (Eventually.of_forall fun z => abs_nonneg _)
          (Eventually.of_forall (cover h hn))
  have hfar := integral_Dset_le h hp hn1 hint
  -- near pairs
  set c := Real.log (p * (U + 1) ^ (-p - 1))
  have hlogn : 0 ≤ Real.log n := Real.log_natCast_nonneg n
  have hnear : -(3 * n * (Real.log n + |c|)) ≤
      ∑ ij ∈ (ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2), Fp p (uq h n ij.1) (uq h n ij.2) := by
    have hterm : ∀ ij ∈ (ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2),
        -(Real.log n + |c|) ≤ Fp p (uq h n ij.1) (uq h n ij.2) := by
      intro ij hij
      simp only [ltS, Finset.mem_filter, Finset.mem_product, Finset.mem_range] at hij
      have := near_ge h hp hn1 hij.1.2 hij.1.1.2
      have := neg_abs_le c
      linarith
    have hcard := card_near_le n
    calc -(3 * n * (Real.log n + |c|)) ≤ -(((ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2)).card *
          (Real.log n + |c|)) := by
          have : (((ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2)).card : ℝ) ≤ 3 * n := by exact_mod_cast hcard
          have : 0 ≤ Real.log n + |c| := by positivity
          nlinarith
      _ = ∑ ij ∈ (ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2), -(Real.log n + |c|) := by
          rw [Finset.sum_const, nsmul_eq_mul]; ring
      _ ≤ _ := Finset.sum_le_sum hterm
  have hsum : ∑ ij ∈ ltS n, Fp p (uq h n ij.1) (uq h n ij.2) =
      ∑ ij ∈ farS n, Fp p (uq h n ij.1) (uq h n ij.2) +
      ∑ ij ∈ (ltS n).filter (fun ij => ¬ ij.1 + 4 ≤ ij.2), Fp p (uq h n ij.1) (uq h n ij.2) := by
    rw [farS_eq, Finset.sum_filter_add_sum_filter_not]
  have hn2 : (0 : ℝ) ≤ (n : ℝ) ^ 2 := by positivity
  rw [hsplit, mul_add]
  have := mul_le_mul_of_nonneg_left hrest hn2
  nlinarith [hfar]

/-- **Step 3 (asymptotic form)**: for every `η > 0`, eventually
`n² (𝒥(θ) − η) ≤ 2 Σ_{i<j} F(u_i, u_j)`. -/
theorem quantile_lower (h : AdmissibleOn U θ) {p : ℝ} (hp : 0 < p)
    (hint : Integrable (fun z : ℝ × ℝ => Fp p z.1 z.2) (θ.prod θ)) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop, (n : ℝ) ^ 2 * (Jp p θ - η) ≤ 2 * ∑ ij ∈ ltS n, Fp p (uq h n ij.1) (uq h n ij.2) := by
  have := h.prob
  set G : ℝ × ℝ → ℝ := fun z => Fp p z.1 z.2
  -- absolute continuity of `∫ |G|`
  obtain ⟨δ, hδ, hδs⟩ := exists_pos_setLIntegral_lt_of_measure_lt (μ := θ.prod θ)
    (f := fun z => ‖G z‖ₑ) hint.2.ne (ε := ENNReal.ofReal (η / 2)) (by simp [hη])
  have hsmall : ∀ᶠ n : ℕ in atTop, ENNReal.ofReal (7 / n) < δ := by
    have : Tendsto (fun n : ℕ => ENNReal.ofReal (7 / n)) atTop (𝓝 0) := by
      rw [← ENNReal.ofReal_zero]
      exact ENNReal.tendsto_ofReal (tendsto_const_div_atTop_nhds_zero_nat 7)
    exact this.eventually (gt_mem_nhds hδ)
  set c := Real.log (p * (U + 1) ^ (-p - 1))
  have hlog : Tendsto (fun n : ℕ => 6 * (Real.log n + |c|) / n) atTop (𝓝 0) := by
    have h1 : Tendsto (fun n : ℕ => Real.log n / n) atTop (𝓝 0) := by
      have := (Real.tendsto_pow_log_div_mul_add_atTop 1 0 1 one_ne_zero).comp tendsto_natCast_atTop_atTop
      simpa [Function.comp_def] using this
    have := ((h1.add (tendsto_const_div_atTop_nhds_zero_nat |c|)).const_mul 6)
    simp only [add_zero, mul_zero] at this
    refine this.congr' (Eventually.of_forall fun n => ?_)
    simp only; ring
  filter_upwards [hsmall, hlog.eventually (gt_mem_nhds (half_pos hη)), eventually_ge_atTop 2] with n hn hn' hn2
  have hn0 : (0 : ℝ) < n := by exact_mod_cast (show 0 < n by omega)
  have hE := (measure_Ebad_le h hn2).trans_lt hn
  have hint_E : ∫ z in Ebad h n, |G z| ∂(θ.prod θ) < η / 2 := by
    have h1 := hδs _ hE
    rw [← ofReal_integral_norm_eq_lintegral_enorm hint.integrableOn] at h1
    have := (ENNReal.ofReal_lt_ofReal_iff (half_pos hη)).1 h1
    simpa [Real.norm_eq_abs] using this
  have key := quantile_sum_ge h hp hint hn2
  have h6 : 6 * n * (Real.log n + |c|) ≤ (n : ℝ) ^ 2 * (η / 2) := by
    have := hn'.le
    rw [div_le_iff₀ hn0] at this
    nlinarith
  have h7 : (n : ℝ) ^ 2 * ∫ z in Ebad h n, |G z| ∂(θ.prod θ) ≤ (n : ℝ) ^ 2 * (η / 2) :=
    mul_le_mul_of_nonneg_left hint_E.le (by positivity)
  nlinarith

end JacobiAsym
