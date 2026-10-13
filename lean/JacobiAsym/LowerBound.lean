import JacobiAsym.UpperBound
import JacobiAsym.SlowVariation

open Finset Filter Topology

namespace JacobiAsym

/-- The monotone lower pair factor, 0-based: index `k` ↔ atom `k+1`. -/
noncomputable def rhoSeq (p : ℝ) (L E : ℝ → ℝ) (a0 : ℕ) (ρm : ℝ) (k : ℕ) : ℝ :=
  if (k : ℝ) + 1 < a0 then ρm else (1 - E ((k : ℝ) + 1) / p) * L ((k : ℝ) + 1)

theorem rhoSeq_mono {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) {ρm : ℝ}
    (hρm0 : 0 < ρm) (hρm : ρm ≤ (1 - E a0 / p) * L a0) :
    Monotone (rhoSeq p L E a0 ρm) ∧ ∀ k, 0 < rhoSeq p L E a0 ρm k := by
  have hp := h.p_pos
  have ha0 : (1 : ℝ) ≤ a0 := by exact_mod_cast h.a0_pos
  -- tail value is positive and monotone
  have htail_pos : ∀ t : ℝ, (a0 : ℝ) ≤ t → 0 < (1 - E t / p) * L t := by
    intro t ht
    have : E t ≤ E a0 := h.E_anti ht
    have : E t / p < 1 := by rw [div_lt_one hp]; linarith [h.E_a0]
    exact mul_pos (by linarith) (h.L_pos t (ha0.trans ht))
  have htail_mono : ∀ t u : ℝ, (a0 : ℝ) ≤ t → t ≤ u → (1 - E t / p) * L t ≤ (1 - E u / p) * L u := by
    intro t u ht htu
    have hEu : E u ≤ E t := h.E_anti htu
    have hLt : L t ≤ L u := h.L_mono (Set.mem_Ici.2 ht) (Set.mem_Ici.2 (ht.trans htu)) htu
    have : E u / p < 1 := by rw [div_lt_one hp]; linarith [h.E_anti (ht.trans htu), h.E_a0]
    apply mul_le_mul _ hLt (h.L_pos t (ha0.trans ht)).le (by linarith)
    have := div_le_div_of_nonneg_right hEu hp.le
    linarith
  have hk : ∀ k : ℕ, (1 : ℝ) ≤ (k : ℝ) + 1 := fun k => by have := Nat.cast_nonneg (α := ℝ) k; linarith
  refine ⟨fun k l hkl => ?_, fun k => ?_⟩
  · have hkl' : (k : ℝ) + 1 ≤ (l : ℝ) + 1 := by have : (k : ℝ) ≤ l := by exact_mod_cast hkl
                                                linarith
    unfold rhoSeq
    split_ifs with h1 h2 h2
    · exact le_rfl
    · exact hρm.trans (htail_mono _ _ le_rfl (not_lt.1 h2))
    · exact absurd (lt_of_le_of_lt hkl' h2) h1
    · exact htail_mono _ _ (not_lt.1 h1) hkl'
  · unfold rhoSeq
    split_ifs with h1
    · exact hρm0
    · exact htail_pos _ (not_lt.1 h1)

/-- Weighted Cesàro: if `a i → 0` then `(2/n²) ∑_{i<n} (n-1-i) a i → 0`. -/
theorem cesaro_weighted_zero {a : ℕ → ℝ} (ha : Tendsto a atTop (𝓝 0)) :
    Tendsto (fun n : ℕ => (2 * ∑ i ∈ range n, ((n : ℝ) - 1 - i) * a i) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  rw [Metric.tendsto_atTop]
  intro ε hε
  obtain ⟨N0, hN0⟩ := (Metric.tendsto_atTop.1 ha) (ε / 4) (by positivity)
  set C0 := ∑ i ∈ range N0, |a i| with hC0
  have hC0nn : 0 ≤ C0 := sum_nonneg fun _ _ => abs_nonneg _
  refine ⟨max N0 (⌈4 * C0 / ε⌉₊ + 1), fun n hn => ?_⟩
  have hnN0 : N0 ≤ n := le_of_max_le_left hn
  have hn1 : ⌈4 * C0 / ε⌉₊ + 1 ≤ n := le_of_max_le_right hn
  have hnpos : (0 : ℝ) < n := by
    have : (1 : ℝ) ≤ n := by exact_mod_cast (Nat.le_add_left 1 _).trans hn1
    linarith
  have hnC : 4 * C0 / ε < n := by
    have := Nat.le_ceil (4 * C0 / ε)
    have : ((⌈4 * C0 / ε⌉₊ + 1 : ℕ) : ℝ) ≤ n := by exact_mod_cast hn1
    push_cast at this; linarith
  -- termwise bound
  have hterm : ∀ i ∈ range n, |((n : ℝ) - 1 - i) * a i| ≤
      (if i < N0 then (n : ℝ) * |a i| else 0) + (n : ℝ) * (ε / 4) := by
    intro i hi
    have hin : (i : ℝ) + 1 ≤ n := by have := mem_range.1 hi; exact_mod_cast this
    have hw0 : 0 ≤ (n : ℝ) - 1 - i := by linarith
    have hwn : (n : ℝ) - 1 - i ≤ n := by have := Nat.cast_nonneg (α := ℝ) i; linarith
    rw [abs_mul, abs_of_nonneg hw0]
    split_ifs with hiN
    · have := mul_le_mul_of_nonneg_right hwn (abs_nonneg (a i))
      have : 0 ≤ (n : ℝ) * (ε / 4) := by positivity
      linarith
    · have hai := hN0 i (not_lt.1 hiN)
      rw [Real.dist_eq, sub_zero] at hai
      have := mul_le_mul hwn hai.le (abs_nonneg _) hnpos.le
      linarith
  have hsum : |∑ i ∈ range n, ((n : ℝ) - 1 - i) * a i| ≤ (n : ℝ) * C0 + (n : ℝ) ^ 2 * (ε / 4) := by
    calc _ ≤ ∑ i ∈ range n, |((n : ℝ) - 1 - i) * a i| := abs_sum_le_sum_abs _ _
      _ ≤ ∑ i ∈ range n, ((if i < N0 then (n : ℝ) * |a i| else 0) + (n : ℝ) * (ε / 4)) := sum_le_sum hterm
      _ = (n : ℝ) * ∑ i ∈ (range n).filter (· < N0), |a i| + (n : ℝ) ^ 2 * (ε / 4) := by
          rw [sum_add_distrib, sum_ite, sum_const_zero, add_zero, sum_const, card_range, nsmul_eq_mul, ← mul_sum]
          ring
      _ ≤ (n : ℝ) * C0 + (n : ℝ) ^ 2 * (ε / 4) := by
          gcongr
          apply sum_le_sum_of_subset_of_nonneg
          · intro i hi; exact mem_range.2 (mem_filter.1 hi).2
          · intro _ _ _; exact abs_nonneg _
  rw [Real.dist_eq, sub_zero, abs_div, abs_mul, abs_two, abs_of_pos (by positivity : (0:ℝ) < (n:ℝ)^2)]
  rw [div_lt_iff₀ (by positivity)]
  have h4 : 4 * C0 < ε * n := by
    have h := hnC
    rw [div_lt_iff₀ hε] at h
    linarith
  nlinarith [hsum]

theorem HL_lower {p κ s c1 s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    (hHlo : TheoremHPure p κ s) (hHup : TheoremHPure p κ s0) (hc1 : 0 < c1) (hc2 : 0 < c2)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hUmono : Monotone U) (hwsum : Summable w) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop,
      -η ≤ hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)) n := by
  have hp := hL.p_pos
  have hw0 : ∀ k, 0 < w k := fun k =>
    (mul_pos hc1 (Real.rpow_pos_of_pos (by positivity : (0:ℝ) < (k:ℝ) + 1) (-s))).trans_le (hwlo k)
  have hw : ∀ i, 0 ≤ w i := fun i => (hw0 i).le
  obtain ⟨ρm, hρm0, hρma0, hρm⟩ := hL.exists_rhoMin
  obtain ⟨hmono, hρpos⟩ := rhoSeq_mono hL hρm0 hρma0
  set ρ := rhoSeq p L E a0 ρm with hρdef
  have hanti : StrictAnti (powSeq p) := by
    intro a b hab
    exact Real.rpow_lt_rpow_of_neg (by positivity) (by exact_mod_cast Nat.add_lt_add_right hab 1) (by linarith)
  -- (1) pair bound
  have hpair : ∀ a b : ℕ, a < b →
      ρ a ^ 2 * (powSeq p a - powSeq p b) ^ 2 ≤
        (slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1)) ^ 2 := by
    intro a b hab
    have har : (1 : ℝ) ≤ (a : ℝ) + 1 := by have := Nat.cast_nonneg (α := ℝ) a; linarith
    have habr : (a : ℝ) + 1 < (b : ℝ) + 1 := by
      have : (a : ℝ) < b := by exact_mod_cast hab
      linarith
    have hlow := hL.lower_pair hρm har habr
    have hd : 0 ≤ powSeq p a - powSeq p b := sub_nonneg.2 (hanti hab).le
    have heq : ρ a = (if (a : ℝ) + 1 < a0 then ρm else (1 - E ((a : ℝ) + 1) / p) * L ((a : ℝ) + 1)) := rfl
    have h1 : ρ a * (powSeq p a - powSeq p b) ≤ slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1) := by
      rw [heq]; exact hlow
    have h0 : 0 ≤ ρ a * (powSeq p a - powSeq p b) := mul_nonneg (hρpos a).le hd
    have := pow_le_pow_left₀ h0 h1 2
    rwa [mul_pow] at this
  -- (2) per n: P c1^n D_g ≤ D_f
  have hDg_pos : ∀ n, 0 < heineD (powSeq p) (powSeq s) n := fun n =>
    heineD_pos hanti (fun i => Real.rpow_pos_of_pos (by positivity) _) (hHlo.bdd n)
  have hDf_pos : ∀ n, 0 < heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w n := fun n =>
    heineD_pos hL.slowAtom_strictAnti hw0 (slow_bdd hL hHup hc2 hw0 hwhi hUmono hwsum n)
  have hP_pos : ∀ n, 0 < ∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i)) := fun n =>
    prod_pos fun i _ => pow_pos (hρpos i) _
  have hkey : ∀ n, (∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * c1 ^ n * heineD (powSeq p) (powSeq s) n ≤
      heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w n := by
    intro n
    have hPc : 0 < (∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * c1 ^ n := mul_pos (hP_pos n) (pow_pos hc1 n)
    have hK : ∀ K, heineK (powSeq p) (powSeq s) K n ≤
        heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w n / ((∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * c1 ^ n) := by
      intro K
      rw [le_div_iff₀ hPc]
      have hsw : c1 ^ n * heineK (powSeq p) (powSeq s) K n ≤ heineK (powSeq p) w K n := by
        rw [← heineK_smul_w]
        exact heineK_mono_w (fun i => mul_nonneg hc1.le (Real.rpow_pos_of_pos (by positivity) _).le) hwlo K n
      have hcmp : (∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * heineK (powSeq p) w K n ≤
          heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w K n := by
        unfold heineK; rw [mul_sum]
        apply sum_le_sum; intro S hS
        have hcard := (mem_powersetCard.1 hS).2
        have := heineTerm_ge_of_pair_ge (x := fun k => slowAtom p L ((k : ℝ) + 1)) (y := powSeq p) hw
          (fun i => (hρpos i).le) hmono (S := S) (fun a _ b _ hab => hpair a b hab)
        rwa [hcard] at this
      have hle := heineK_le_heineD (slow_bdd hL hHup hc2 hw0 hwhi hUmono hwsum n) K
      calc heineK (powSeq p) (powSeq s) K n * ((∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * c1 ^ n)
          = (∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * (c1 ^ n * heineK (powSeq p) (powSeq s) K n) := by ring
        _ ≤ (∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) * heineK (powSeq p) w K n :=
            mul_le_mul_of_nonneg_left hsw (hP_pos n).le
        _ ≤ _ := hcmp.trans hle
    have := heineD_le hK
    rwa [le_div_iff₀ hPc, mul_comm] at this
  -- (3) logarithmic form
  have hlogP : ∀ n, 1 ≤ n → Real.log (∏ i ∈ range n, ρ i ^ (2 * (n - 1 - i))) =
      ∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) := by
    intro n hn
    rw [Real.log_prod (fun i _ => (pow_pos (hρpos i) _).ne')]
    apply sum_congr rfl; intro i hi
    rw [Real.log_pow]
    have hi' : i + 1 ≤ n := mem_range.1 hi
    congr 1
    rw [Nat.cast_mul, Nat.cast_sub (by omega), Nat.cast_sub (by omega)]
    push_cast; ring
  -- (4) the sequence a_i = log ρ_i - log L(i+1) tends to 0
  set a : ℕ → ℝ := fun i => Real.log (ρ i) - Real.log (L ((i : ℝ) + 1)) with ha
  have ha0 : Tendsto a atTop (𝓝 0) := by
    have hE1 : Tendsto (fun i : ℕ => E ((i : ℝ) + 1)) atTop (𝓝 0) :=
      hL.E_lim.comp (tendsto_atTop_add_const_right _ 1 tendsto_natCast_atTop_atTop)
    have h1 : Tendsto (fun i : ℕ => 1 - E ((i : ℝ) + 1) / p) atTop (𝓝 1) := by
      have := (hE1.div_const p).const_sub 1
      simpa using this
    have hlog := h1.log one_ne_zero
    rw [Real.log_one] at hlog
    refine hlog.congr' ?_
    filter_upwards [eventually_ge_atTop a0] with i hi
    have hia : ¬ ((i : ℝ) + 1 < a0) := by
      have : (a0 : ℝ) ≤ i := by exact_mod_cast hi
      linarith
    have hE : E ((i : ℝ) + 1) / p < 1 := by
      rw [div_lt_one hp]
      have : (a0 : ℝ) ≤ (i : ℝ) + 1 := by have : (a0 : ℝ) ≤ i := by exact_mod_cast hi
                                          linarith
      linarith [hL.E_anti this, hL.E_a0]
    have hL1 : 0 < L ((i : ℝ) + 1) := hL.L_pos _ (by have := Nat.cast_nonneg (α := ℝ) i; linarith)
    simp only [ha, hρdef, rhoSeq, hia, ite_false]
    rw [Real.log_mul (by linarith) hL1.ne']
    ring
  -- (5) Q(n) → 0
  have hlogL := hL.logL_slow
  have hW := weighted_cesaro_slow hL.E_nonneg hL.E_anti hL.E_lim hlogL
  have hLn : Tendsto (fun n : ℕ => Real.log (L n) / n) atTop (𝓝 0) := by
    have hb : Tendsto (fun n : ℕ => (|Real.log (L 1)| + E 1 * Real.log n) / n) atTop (𝓝 0) := by
      have := (tendsto_const_div_atTop_nhds_zero_nat |Real.log (L 1)|).add (tendsto_log_div_nat.const_mul (E 1))
      simp only [mul_zero, add_zero] at this
      refine this.congr' ?_
      filter_upwards [eventually_ge_atTop 1] with n hn
      field_simp
    apply squeeze_zero_norm' _ hb
    filter_upwards [eventually_ge_atTop 1] with n hn
    have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
    have h := hlogL 1 n le_rfl hnr
    rw [div_one] at h
    rw [Real.norm_eq_abs, abs_div, abs_of_pos (by positivity : (0:ℝ) < n)]
    apply div_le_div_of_nonneg_right _ (by positivity)
    have := abs_sub_abs_le_abs_sub (Real.log (L n)) (Real.log (L 1))
    linarith
  have hC := cesaro_weighted_zero ha0
  -- reindexing identity for the main sum
  have hreidx : ∀ n : ℕ, 1 ≤ n →
      ∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) - (n : ℝ) ^ 2 * Real.log (L n) =
        2 * ∑ j ∈ Ico 1 n, ((n : ℝ) - j) * (Real.log (L j) - Real.log (L n)) - (n : ℝ) * Real.log (L n)
          + 2 * ∑ i ∈ range n, ((n : ℝ) - 1 - i) * a i := by
    intro n hn
    -- ∑_{i<n} (n-1-i) f(i+1) = ∑_{j ∈ Ico 1 n} (n-j) f j
    have hsh : ∀ f : ℝ → ℝ, ∑ i ∈ range n, ((n : ℝ) - 1 - i) * f ((i : ℝ) + 1) =
        ∑ j ∈ Ico 1 n, ((n : ℝ) - j) * f j := by
      intro f
      have h1 : ∑ j ∈ Ico 1 (n + 1), ((n : ℝ) - j) * f j = ∑ i ∈ range n, ((n : ℝ) - 1 - i) * f ((i : ℝ) + 1) := by
        rw [sum_Ico_eq_sum_range, show n + 1 - 1 = n by omega]
        apply sum_congr rfl; intro i _; push_cast; ring_nf
      rw [← h1, sum_Ico_succ_top hn]
      simp
    have hcount : ∑ i ∈ range n, ((n : ℝ) - 1 - i) = (n : ℝ) * ((n : ℝ) - 1) / 2 := by
      have h2 := Finset.sum_range_id_mul_two n
      have h3 : ∑ i ∈ range n, ((n : ℝ) - 1 - i) = ∑ i ∈ range n, (i : ℝ) := by
        rw [← sum_range_reflect]
        apply sum_congr rfl; intro i hi
        have : i < n := mem_range.1 hi
        rw [Nat.cast_sub (by omega), Nat.cast_sub (by omega)]; push_cast; ring
      rw [h3]
      have h4 : (∑ i ∈ range n, (i : ℝ)) * 2 = (n : ℝ) * ((n : ℝ) - 1) := by
        have := congrArg (fun z : ℕ => (z : ℝ)) h2
        push_cast at this
        rw [this, Nat.cast_sub hn]; push_cast; ring
      linarith
    have hsplit : ∀ i, Real.log (ρ i) = (Real.log (L ((i : ℝ) + 1)) - Real.log (L n)) + Real.log (L n) + a i := by
      intro i; simp only [ha]; ring
    have e1 : ∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) =
        2 * ∑ i ∈ range n, ((n : ℝ) - 1 - i) * (Real.log (L ((i : ℝ) + 1)) - Real.log (L n))
          + 2 * Real.log (L n) * ∑ i ∈ range n, ((n : ℝ) - 1 - i)
          + 2 * ∑ i ∈ range n, ((n : ℝ) - 1 - i) * a i := by
      simp_rw [hsplit, mul_sum, ← sum_add_distrib]
      apply sum_congr rfl; intro i _; ring
    rw [e1, hcount, hsh (fun t => Real.log (L t) - Real.log (L n))]
    ring
  have hQ : Tendsto (fun n : ℕ => (∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i)
      - (n : ℝ) ^ 2 * Real.log (L n)) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
    have := (hW.sub hLn).add hC
    simp only [sub_zero, add_zero] at this
    refine this.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with n hn
    rw [hreidx n hn]
    have : (n : ℝ) ≠ 0 := by have : (1 : ℝ) ≤ n := by exact_mod_cast hn
                             linarith
    field_simp
  -- (6) assemble
  have hc1n : Tendsto (fun n : ℕ => Real.log c1 / n) atTop (𝓝 0) := tendsto_const_div_atTop_nhds_zero_nat _
  have hg := hHlo.asymp
  have hall := (hQ.add hc1n).add hg
  simp only [add_zero] at hall
  have hev := hall.eventually (lt_mem_nhds (neg_lt_zero.2 hη))
  filter_upwards [hev, eventually_ge_atTop 1] with n hlt hn
  have hnr : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hn2 : (0 : ℝ) < (n : ℝ) ^ 2 := by positivity
  have hlogD : Real.log (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w n) ≥
      ∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) + n * Real.log c1 +
        Real.log (heineD (powSeq p) (powSeq s) n) := by
    have h := Real.log_le_log (mul_pos (mul_pos (hP_pos n) (pow_pos hc1 n)) (hDg_pos n)) (hkey n)
    rw [Real.log_mul (mul_pos (hP_pos n) (pow_pos hc1 n)).ne' (hDg_pos n).ne',
      Real.log_mul (hP_pos n).ne' (pow_pos hc1 n).ne', Real.log_pow, hlogP n hn] at h
    linarith
  unfold hnorm at hlt ⊢
  have e2 : ((∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) - (n : ℝ) ^ 2 * Real.log (L n)) / (n : ℝ) ^ 2
      + Real.log c1 / n + (Real.log (heineD (powSeq p) (powSeq s) n) -
        (-p * (n : ℝ) ^ 2 * Real.log n + (n : ℝ) ^ 2 * 0 + κ * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2) =
      (∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) + n * Real.log c1 +
        Real.log (heineD (powSeq p) (powSeq s) n) -
        (-p * (n : ℝ) ^ 2 * Real.log n + (n : ℝ) ^ 2 * Real.log (L n) + κ * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2 := by
    field_simp; ring
  rw [e2] at hlt
  have : (∑ i ∈ range n, 2 * ((n : ℝ) - 1 - i) * Real.log (ρ i) + n * Real.log c1 +
        Real.log (heineD (powSeq p) (powSeq s) n) -
        (-p * (n : ℝ) ^ 2 * Real.log n + (n : ℝ) ^ 2 * Real.log (L n) + κ * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2 ≤
      (Real.log (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w n) -
        (-p * (n : ℝ) ^ 2 * Real.log n + (n : ℝ) ^ 2 * Real.log (L n) + κ * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2 :=
    div_le_div_of_nonneg_right (by linarith) hn2.le
  linarith

end JacobiAsym
