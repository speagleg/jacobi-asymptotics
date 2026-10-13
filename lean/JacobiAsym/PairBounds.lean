import JacobiAsym.SlowFactor
import JacobiAsym.RatioBounds

namespace JacobiAsym

/-- One-sided Cauchy MVT (lower). -/
theorem ratio_lower_of_deriv {f g f' g' : ℝ → ℝ} {a b lo : ℝ} (hab : a < b)
    (hf : ContinuousOn f (Set.Icc a b)) (hg : ContinuousOn g (Set.Icc a b))
    (hf' : ∀ t ∈ Set.Ioo a b, HasDerivAt f (f' t) t) (hg' : ∀ t ∈ Set.Ioo a b, HasDerivAt g (g' t) t)
    (hgneg : ∀ t ∈ Set.Ioo a b, g' t < 0) (hlo : ∀ t ∈ Set.Ioo a b, lo * (-g' t) ≤ -f' t) :
    lo * (g a - g b) ≤ f a - f b := by
  obtain ⟨c, hc, hEq⟩ := exists_ratio_hasDerivAt_eq_ratio_slope f f' hab hf hf' g g' hg hg'
  obtain ⟨c', hc', hslope⟩ := exists_hasDerivAt_eq_slope g g' hab hg hg'
  have hba : 0 < b - a := sub_pos.2 hab
  have hD : 0 < g a - g b := by
    have h1 := hgneg c' hc'
    rw [hslope, div_neg_iff] at h1
    rcases h1 with ⟨_, h⟩ | ⟨h, _⟩ <;> linarith
  have hd : 0 < -g' c := neg_pos.2 (hgneg c hc)
  have h := mul_le_mul_of_nonneg_left (hlo c hc) hD.le
  have : lo * (g a - g b) * (-g' c) ≤ (f a - f b) * (-g' c) := by nlinarith
  exact le_of_mul_le_mul_right this hd

/-- One-sided Cauchy MVT (upper). -/
theorem ratio_upper_of_deriv {f g f' g' : ℝ → ℝ} {a b hi : ℝ} (hab : a < b)
    (hf : ContinuousOn f (Set.Icc a b)) (hg : ContinuousOn g (Set.Icc a b))
    (hf' : ∀ t ∈ Set.Ioo a b, HasDerivAt f (f' t) t) (hg' : ∀ t ∈ Set.Ioo a b, HasDerivAt g (g' t) t)
    (hgneg : ∀ t ∈ Set.Ioo a b, g' t < 0) (hhi : ∀ t ∈ Set.Ioo a b, -f' t ≤ hi * (-g' t)) :
    f a - f b ≤ hi * (g a - g b) := by
  obtain ⟨c, hc, hEq⟩ := exists_ratio_hasDerivAt_eq_ratio_slope f f' hab hf hf' g g' hg hg'
  obtain ⟨c', hc', hslope⟩ := exists_hasDerivAt_eq_slope g g' hab hg hg'
  have hba : 0 < b - a := sub_pos.2 hab
  have hD : 0 < g a - g b := by
    have h1 := hgneg c' hc'
    rw [hslope, div_neg_iff] at h1
    rcases h1 with ⟨_, h⟩ | ⟨h, _⟩ <;> linarith
  have hd : 0 < -g' c := neg_pos.2 (hgneg c hc)
  have h := mul_le_mul_of_nonneg_left (hhi c hc) hD.le
  have : (f a - f b) * (-g' c) ≤ hi * (g a - g b) * (-g' c) := by nlinarith
  exact le_of_mul_le_mul_right this hd

theorem rpow_neg_hasDerivAt {p t : ℝ} (ht : 0 < t) :
    HasDerivAt (fun t : ℝ => t ^ (-p)) (-p * t ^ (-p - 1)) t :=
  Real.hasDerivAt_rpow_const (Or.inl ht.ne')

/-- `-f'(t) = p t^{-p-1} (L t - t L' t / p)` for `f = slowAtom`. -/
theorem neg_slowAtom_deriv {p t : ℝ} {L L' : ℝ → ℝ} (hp : 0 < p) (ht : 0 < t) :
    -(-p * t ^ (-p - 1) * L t + t ^ (-p) * L' t) = (p * t ^ (-p - 1)) * (L t - t * L' t / p) := by
  have e : t ^ (-p) = t ^ (-p - 1) * t := by
    rw [← Real.rpow_add_one ht.ne']; norm_num
  rw [e]; field_simp; ring

theorem slowAtom_hasDerivAt {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) {t : ℝ} (ht : 1 ≤ t) :
    HasDerivAt (slowAtom p L) (-p * t ^ (-p - 1) * L t + t ^ (-p) * L' t) t :=
  (rpow_neg_hasDerivAt (by linarith : (0 : ℝ) < t)).mul (h.L_deriv t ht)

theorem SlowFactor.lower_pair {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) {ρm : ℝ}
    (hρm : ∀ t, 1 ≤ t → ρm ≤ L t - t * L' t / p) {a c : ℝ} (ha : 1 ≤ a) (hac : a < c) :
    (if a < a0 then ρm else (1 - E a / p) * L a) * (a ^ (-p) - c ^ (-p)) ≤ slowAtom p L a - slowAtom p L c := by
  have hp := h.p_pos
  have hd : ∀ t ∈ Set.Icc a c, HasDerivAt (slowAtom p L) (-p * t ^ (-p - 1) * L t + t ^ (-p) * L' t) t :=
    fun t ht => slowAtom_hasDerivAt h (ha.trans ht.1)
  have hg : ∀ t ∈ Set.Icc a c, HasDerivAt (fun t : ℝ => t ^ (-p)) (-p * t ^ (-p - 1)) t :=
    fun t ht => rpow_neg_hasDerivAt (by linarith [ht.1])
  apply ratio_lower_of_deriv hac
    (fun t ht => (hd t ht).continuousAt.continuousWithinAt)
    (fun t ht => (hg t ht).continuousAt.continuousWithinAt)
    (fun t ht => hd t (Set.Ioo_subset_Icc_self ht)) (fun t ht => hg t (Set.Ioo_subset_Icc_self ht))
  · intro t ht
    have : 0 < t := by linarith [ht.1]
    have : 0 < t ^ (-p - 1) := Real.rpow_pos_of_pos this _
    nlinarith
  · intro t ht
    have ht1 : 1 ≤ t := ha.trans ht.1.le
    have htpos : 0 < t := by linarith
    have hpow : 0 < p * t ^ (-p - 1) := mul_pos hp (Real.rpow_pos_of_pos htpos _)
    rw [neg_slowAtom_deriv hp htpos, neg_mul, neg_neg, mul_comm _ (p * t ^ (-p - 1))]
    apply mul_le_mul_of_nonneg_left _ hpow.le
    split_ifs with hlt
    · exact hρm t ht1
    · have ha0 : (a0 : ℝ) ≤ a := not_lt.1 hlt
      have hEt : E t ≤ E a := h.E_anti ht.1.le
      have hEa : E a ≤ E a0 := h.E_anti ha0
      have hEa0 := h.E_a0
      have hLa : L a ≤ L t := h.L_mono (Set.mem_Ici.2 ha0) (Set.mem_Ici.2 (ha0.trans ht.1.le)) ht.1.le
      have hLpos : 0 < L t := h.L_pos t ht1
      have h1 : (1 - E a / p) * L a ≤ (1 - E t / p) * L t := by
        have : E t / p ≤ E a / p := div_le_div_of_nonneg_right hEt hp.le
        have : E a / p < 1 := by rw [div_lt_one hp]; linarith
        apply mul_le_mul (by linarith) hLa (h.L_pos a ha).le
        have : E t / p ≤ E a0 / p := div_le_div_of_nonneg_right (hEt.trans hEa) hp.le
        have : E a0 / p < 1 := by rw [div_lt_one hp]; linarith
        linarith
      have heps : t * L' t / L t ≤ E t := (le_abs_self _).trans (h.eps_le t ht1)
      have h2 : t * L' t ≤ E t * L t := by rwa [div_le_iff₀ hLpos] at heps
      have h3 : (1 - E t / p) * L t ≤ L t - t * L' t / p := by
        have : t * L' t / p ≤ E t * L t / p := div_le_div_of_nonneg_right h2 hp.le
        have e : (1 - E t / p) * L t = L t - E t * L t / p := by ring
        rw [e]; linarith
      exact h1.trans h3

theorem SlowFactor.upper_pair {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∃ B : ℝ, 1 ≤ B ∧ ∀ a c T : ℝ, 1 ≤ a → a < c → c ≤ T → (a0 : ℝ) ≤ T →
      slowAtom p L a - slowAtom p L c ≤ (if a < a0 then B else 1) * L T * (a ^ (-p) - c ^ (-p)) := by
  have hp := h.p_pos
  have ha0 : (1 : ℝ) ≤ a0 := by exact_mod_cast h.a0_pos
  set R : ℝ → ℝ := fun t => L t - t * L' t / p with hR
  have hL : ContinuousOn L (Set.Icc 1 (a0 : ℝ)) := h.L_cont.mono Set.Icc_subset_Ici_self
  have hL' : ContinuousOn L' (Set.Icc 1 (a0 : ℝ)) := h.L'_cont.mono Set.Icc_subset_Ici_self
  have hRc : ContinuousOn R (Set.Icc 1 a0) := hL.sub ((continuousOn_id.mul hL').div_const p)
  obtain ⟨t1, ht1, hmax⟩ := isCompact_Icc.exists_isMaxOn ⟨1, le_refl _, ha0⟩ hRc
  obtain ⟨t2, ht2, hmin⟩ := isCompact_Icc.exists_isMinOn ⟨1, le_refl _, ha0⟩ hL
  set B0 := R t1
  set Lmin := L t2
  have hLmin : 0 < Lmin := h.L_pos t2 ht2.1
  have hLge : ∀ t, 1 ≤ t → Lmin ≤ L t := by
    intro t ht
    rcases le_or_gt t a0 with hta | hta
    · exact hmin ⟨ht, hta⟩
    · exact (hmin ⟨ha0, le_rfl⟩).trans (h.L_mono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 hta.le) hta.le)
  set B := max 1 (max B0 (L a0) / Lmin)
  have hB1 : 1 ≤ B := le_max_left _ _
  have hBL : max B0 (L a0) ≤ B * Lmin := by
    have := le_max_right 1 (max B0 (L a0) / Lmin)
    rwa [div_le_iff₀ hLmin] at this
  refine ⟨B, hB1, fun a c T ha hac hcT ha0T => ?_⟩
  have hapos : 0 < a := by linarith
  have hgac : 0 ≤ a ^ (-p) - c ^ (-p) :=
    sub_nonneg.2 (Real.rpow_le_rpow_of_nonpos hapos hac.le (by linarith))
  have hLT : Lmin ≤ L T := hLge T (ha0.trans ha0T)
  -- derivative data on any [u, v] ⊆ [1, ∞)
  have hd : ∀ t, 1 ≤ t → HasDerivAt (slowAtom p L) (-p * t ^ (-p - 1) * L t + t ^ (-p) * L' t) t :=
    fun t ht => slowAtom_hasDerivAt h ht
  have hg : ∀ t, 1 ≤ t → HasDerivAt (fun t : ℝ => t ^ (-p)) (-p * t ^ (-p - 1)) t :=
    fun t ht => rpow_neg_hasDerivAt (by linarith)
  -- ratio bound by B0 on [u, v] ⊆ [1, a0]
  have hseg : ∀ u v : ℝ, 1 ≤ u → u < v → v ≤ (a0 : ℝ) →
      slowAtom p L u - slowAtom p L v ≤ B0 * (u ^ (-p) - v ^ (-p)) := by
    intro u v hu huv hva
    apply ratio_upper_of_deriv huv
      (fun t ht => (hd t (hu.trans ht.1)).continuousAt.continuousWithinAt)
      (fun t ht => (hg t (hu.trans ht.1)).continuousAt.continuousWithinAt)
      (fun t ht => hd t (hu.trans ht.1.le)) (fun t ht => hg t (hu.trans ht.1.le))
    · intro t ht
      have : 0 < t ^ (-p - 1) := Real.rpow_pos_of_pos (by linarith [ht.1]) _
      nlinarith
    · intro t ht
      have ht1 : 1 ≤ t := hu.trans ht.1.le
      have htpos : 0 < t := by linarith
      have hpow : 0 < p * t ^ (-p - 1) := mul_pos hp (Real.rpow_pos_of_pos htpos _)
      rw [neg_slowAtom_deriv hp htpos, neg_mul, neg_neg, mul_comm B0]
      exact mul_le_mul_of_nonneg_left (hmax ⟨ht1, ht.2.le.trans hva⟩) hpow.le
  -- the monotone-L algebraic bound on [u, v] ⊆ [a0, ∞)
  have hmono : ∀ u v : ℝ, (a0 : ℝ) ≤ u → u < v →
      slowAtom p L u - slowAtom p L v ≤ L u * (u ^ (-p) - v ^ (-p)) := by
    intro u v hu huv
    exact diff_le_of_L_mono (by linarith) huv hp
      (h.L_mono (Set.mem_Ici.2 hu) (Set.mem_Ici.2 (hu.trans huv.le)) huv.le)
  split_ifs with hlt
  · rcases le_or_gt c a0 with hca | hca
    · calc slowAtom p L a - slowAtom p L c ≤ B0 * (a ^ (-p) - c ^ (-p)) := hseg a c ha hac hca
        _ ≤ (B * L T) * (a ^ (-p) - c ^ (-p)) := by
            apply mul_le_mul_of_nonneg_right _ hgac
            calc B0 ≤ max B0 (L a0) := le_max_left _ _
              _ ≤ B * Lmin := hBL
              _ ≤ B * L T := mul_le_mul_of_nonneg_left hLT (by linarith)
    · have h1 := hseg a a0 ha hlt le_rfl
      have h2 := hmono a0 c le_rfl hca
      have hg1 : 0 ≤ a ^ (-p) - (a0 : ℝ) ^ (-p) :=
        sub_nonneg.2 (Real.rpow_le_rpow_of_nonpos hapos hlt.le (by linarith))
      have hg2 : 0 ≤ (a0 : ℝ) ^ (-p) - c ^ (-p) :=
        sub_nonneg.2 (Real.rpow_le_rpow_of_nonpos (by linarith) hca.le (by linarith))
      have hB0 : B0 ≤ B * L T := (le_max_left _ _).trans (hBL.trans (mul_le_mul_of_nonneg_left hLT (by linarith)))
      have hLa0 : L a0 ≤ B * L T := by
        have : L a0 ≤ L T := h.L_mono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 ha0T) ha0T
        nlinarith [hLmin, hLT]
      calc slowAtom p L a - slowAtom p L c
          = (slowAtom p L a - slowAtom p L a0) + (slowAtom p L a0 - slowAtom p L c) := by ring
        _ ≤ B0 * (a ^ (-p) - (a0 : ℝ) ^ (-p)) + L a0 * ((a0 : ℝ) ^ (-p) - c ^ (-p)) := add_le_add h1 h2
        _ ≤ (B * L T) * (a ^ (-p) - (a0 : ℝ) ^ (-p)) + (B * L T) * ((a0 : ℝ) ^ (-p) - c ^ (-p)) := by
            gcongr
        _ = (B * L T) * (a ^ (-p) - c ^ (-p)) := by ring
  · have ha0a : (a0 : ℝ) ≤ a := not_lt.1 hlt
    calc slowAtom p L a - slowAtom p L c ≤ L a * (a ^ (-p) - c ^ (-p)) := hmono a c ha0a hac
      _ ≤ (1 * L T) * (a ^ (-p) - c ^ (-p)) := by
          rw [one_mul]
          exact mul_le_mul_of_nonneg_right
            (h.L_mono (Set.mem_Ici.2 ha0a) (Set.mem_Ici.2 ha0T) (hac.le.trans hcT)) hgac

/-- Item 11's comparison atoms `G` (0-based): pure power on the head `k < K0`, rescaled tail `f(k+1)/L(K0)`. -/
noncomputable def cutAtom (p : ℝ) (L : ℝ → ℝ) (K0 : ℕ) (k : ℕ) : ℝ :=
  if k < K0 then ((k : ℝ) + 1) ^ (-p) else slowAtom p L ((k : ℝ) + 1) / L K0

end JacobiAsym
