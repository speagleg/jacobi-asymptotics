import JacobiAsym.Basic

open Filter Topology

namespace JacobiAsym

/-- Atom function `t^{-p} L t` (item 11: `f(ξ) = ξ^{-p} L(ξ)`). -/
noncomputable def slowAtom (p : ℝ) (L : ℝ → ℝ) (t : ℝ) : ℝ := t ^ (-p) * L t

/-- Item 11 hypotheses (L1)–(L3) on `[1, ∞)`. `E` is an antitone majorant of `|ε|`, `ε(t) = t L'(t)/L(t)`
(so `E ≥ ε*`). `f_dec` is `f' < 0`. -/
structure SlowFactor (p : ℝ) (L L' E : ℝ → ℝ) (a0 : ℕ) : Prop where
  p_pos : 0 < p
  L_pos : ∀ t, 1 ≤ t → 0 < L t
  L_deriv : ∀ t, 1 ≤ t → HasDerivAt L (L' t) t
  L'_cont : ContinuousOn L' (Set.Ici 1)
  E_nonneg : ∀ t, 0 ≤ E t
  E_anti : Antitone E
  E_lim : Tendsto E atTop (𝓝 0)
  eps_le : ∀ t, 1 ≤ t → |t * L' t / L t| ≤ E t
  a0_pos : 1 ≤ a0
  E_a0 : E a0 < p
  L_mono : MonotoneOn L (Set.Ici (a0 : ℝ))
  f_dec : ∀ t, 1 ≤ t → t * L' t < p * L t

theorem SlowFactor.L_cont {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ContinuousOn L (Set.Ici 1) :=
  fun t ht => (h.L_deriv t ht).continuousAt.continuousWithinAt

/-- `R t := L t - t L' t / p > 0` on `[1, ∞)` (equivalent to `f' < 0`). -/
theorem SlowFactor.R_pos {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∀ t, 1 ≤ t → 0 < L t - t * L' t / p := by
  intro t ht
  have h1 := h.f_dec t ht
  have hp := h.p_pos
  have : t * L' t / p < L t := by rw [div_lt_iff₀ hp]; linarith
  linarith

/-- H6(a): `|log L y - log L x| ≤ E x · log (y/x)` for `1 ≤ x ≤ y`. -/
theorem SlowFactor.logL_slow {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∀ x y : ℝ, 1 ≤ x → x ≤ y → |Real.log (L y) - Real.log (L x)| ≤ E x * Real.log (y / x) := by
  intro x y hx hxy
  have hx0 : 0 < x := by linarith
  rcases eq_or_lt_of_le hxy with rfl | hlt
  · simp
  set φ : ℝ → ℝ := fun u => Real.log (L (Real.exp u)) with hφ
  set φ' : ℝ → ℝ := fun u => Real.exp u * L' (Real.exp u) / L (Real.exp u) with hφ'
  have hderiv : ∀ u, Real.log x ≤ u → HasDerivAt φ (φ' u) u := by
    intro u hu
    have he : 1 ≤ Real.exp u := by
      have := Real.exp_le_exp.2 hu
      rw [Real.exp_log hx0] at this; linarith
    have hL := (h.L_deriv _ he).comp u (Real.hasDerivAt_exp u)
    have hlog := hL.log (h.L_pos _ he).ne'
    have e : φ' u = L' (Real.exp u) * Real.exp u / (L ∘ Real.exp) u := by
      simp only [hφ', Function.comp_apply]; ring
    rw [e]; exact hlog
  have hab : Real.log x < Real.log y := Real.log_lt_log hx0 hlt
  obtain ⟨c, hc, hcs⟩ := exists_hasDerivAt_eq_slope φ φ' hab
    (fun u hu => (hderiv u hu.1).continuousAt.continuousWithinAt)
    (fun u hu => hderiv u hu.1.le)
  have hc1 : x ≤ Real.exp c := by
    have := Real.exp_le_exp.2 hc.1.le
    rwa [Real.exp_log hx0] at this
  have he1 : 1 ≤ Real.exp c := hx.trans hc1
  have hbound : |φ' c| ≤ E x := (h.eps_le _ he1).trans (h.E_anti hc1)
  have hpos : 0 < Real.log y - Real.log x := sub_pos.2 hab
  have hdiff : φ (Real.log y) - φ (Real.log x) = φ' c * (Real.log y - Real.log x) := by
    rw [hcs]; field_simp
  simp only [hφ, Real.exp_log hx0, Real.exp_log (hx0.trans hlt)] at hdiff
  rw [hdiff, abs_mul, abs_of_pos hpos, Real.log_div (by linarith) hx0.ne']
  exact mul_le_mul_of_nonneg_right hbound hpos.le

/-- The lower constant `ρ₋` of item 11 Lemma H5(ii). -/
theorem SlowFactor.exists_rhoMin {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∃ ρm : ℝ, 0 < ρm ∧ ρm ≤ (1 - E a0 / p) * L a0 ∧ ∀ t, 1 ≤ t → ρm ≤ L t - t * L' t / p := by
  have hp := h.p_pos
  have ha0 : (1 : ℝ) ≤ a0 := by exact_mod_cast h.a0_pos
  set R : ℝ → ℝ := fun t => L t - t * L' t / p with hR
  have hRc : ContinuousOn R (Set.Icc 1 a0) := by
    have hL : ContinuousOn L (Set.Icc 1 (a0 : ℝ)) := h.L_cont.mono Set.Icc_subset_Ici_self
    have hL' : ContinuousOn L' (Set.Icc 1 (a0 : ℝ)) := h.L'_cont.mono Set.Icc_subset_Ici_self
    exact hL.sub ((continuousOn_id.mul hL').div_const p)
  obtain ⟨t1, ht1, hmin⟩ := isCompact_Icc.exists_isMinOn ⟨1, le_refl _, ha0⟩ hRc
  have hρ1 : 0 < R t1 := h.R_pos t1 ht1.1
  have hEa0 : E a0 / p < 1 := by rw [div_lt_one hp]; exact h.E_a0
  have hq : 0 < (1 - E a0 / p) * L a0 := mul_pos (by linarith) (h.L_pos _ ha0)
  refine ⟨min (R t1) ((1 - E a0 / p) * L a0), lt_min hρ1 hq, min_le_right _ _, fun t ht => ?_⟩
  rcases le_or_gt t a0 with hta | hta
  · exact (min_le_left _ _).trans (hmin ⟨ht, hta⟩)
  · refine (min_le_right _ _).trans ?_
    have hEt : E t ≤ E a0 := h.E_anti hta.le
    have hLt : L a0 ≤ L t := h.L_mono (Set.mem_Ici.2 le_rfl) (Set.mem_Ici.2 hta.le) hta.le
    have hLpos : 0 < L t := h.L_pos t ht
    have h1 : (1 - E a0 / p) * L a0 ≤ (1 - E t / p) * L t := by
      apply mul_le_mul _ hLt (h.L_pos _ ha0).le
      · have : E t / p ≤ E a0 / p := div_le_div_of_nonneg_right hEt hp.le
        linarith
      · have : E t / p ≤ E a0 / p := div_le_div_of_nonneg_right hEt hp.le
        linarith
    have heps : t * L' t / L t ≤ E t := (le_abs_self _).trans (h.eps_le t ht)
    have h2 : t * L' t ≤ E t * L t := by rwa [div_le_iff₀ hLpos] at heps
    have h3 : (1 - E t / p) * L t ≤ L t - t * L' t / p := by
      have : t * L' t / p ≤ E t * L t / p := div_le_div_of_nonneg_right h2 hp.le
      have e : (1 - E t / p) * L t = L t - E t * L t / p := by ring
      rw [e]; linarith
    exact h1.trans h3

end JacobiAsym
