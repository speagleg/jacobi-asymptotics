import JacobiAsym.Basic

namespace JacobiAsym

/-- Cauchy mean value theorem, ratio form: if `g' < 0` and `lo·(-g') ≤ -f' ≤ hi·(-g')` on `(a,b)` then
`lo (g a - g b) ≤ f a - f b ≤ hi (g a - g b)`.  (Item 11 Lemmas H4/H5.) -/
theorem ratio_bounds_of_deriv {f g f' g' : ℝ → ℝ} {a b lo hi : ℝ} (hab : a < b)
    (hf : ContinuousOn f (Set.Icc a b)) (hg : ContinuousOn g (Set.Icc a b))
    (hf' : ∀ t ∈ Set.Ioo a b, HasDerivAt f (f' t) t) (hg' : ∀ t ∈ Set.Ioo a b, HasDerivAt g (g' t) t)
    (hgneg : ∀ t ∈ Set.Ioo a b, g' t < 0)
    (hlo : ∀ t ∈ Set.Ioo a b, lo * (-g' t) ≤ -f' t) (hhi : ∀ t ∈ Set.Ioo a b, -f' t ≤ hi * (-g' t)) :
    lo * (g a - g b) ≤ f a - f b ∧ f a - f b ≤ hi * (g a - g b) := by
  obtain ⟨c, hc, hEq⟩ := exists_ratio_hasDerivAt_eq_ratio_slope f f' hab hf hf' g g' hg hg'
  obtain ⟨c', hc', hslope⟩ := exists_hasDerivAt_eq_slope g g' hab hg hg'
  have hba : 0 < b - a := sub_pos.2 hab
  have hD : 0 < g a - g b := by
    have h1 := hgneg c' hc'
    rw [hslope, div_neg_iff] at h1
    rcases h1 with ⟨_, h⟩ | ⟨h, _⟩
    · linarith
    · linarith
  have hd : 0 < -g' c := neg_pos.2 (hgneg c hc)
  -- (f a - f b) * (-g' c) = (g a - g b) * (-f' c)
  have hkey : (f a - f b) * (-g' c) = (g a - g b) * (-f' c) := by linarith
  constructor
  · have h := mul_le_mul_of_nonneg_left (hlo c hc) hD.le
    have : lo * (g a - g b) * (-g' c) ≤ (f a - f b) * (-g' c) := by nlinarith
    exact le_of_mul_le_mul_right this hd
  · have h := mul_le_mul_of_nonneg_left (hhi c hc) hD.le
    have : (f a - f b) * (-g' c) ≤ hi * (g a - g b) * (-g' c) := by nlinarith
    exact le_of_mul_le_mul_right this hd

/-- H5(i) upper bound: if `L a ≤ L b` then `a^{-p} L a - b^{-p} L b ≤ L a (a^{-p} - b^{-p})`. -/
theorem diff_le_of_L_mono {L : ℝ → ℝ} {a b p : ℝ} (ha : 0 < a) (hab : a < b) (_hp : 0 < p)
    (hL : L a ≤ L b) :
    a ^ (-p) * L a - b ^ (-p) * L b ≤ L a * (a ^ (-p) - b ^ (-p)) := by
  have hb : 0 < b ^ (-p) := Real.rpow_pos_of_pos (ha.trans hab) (-p)
  nlinarith [mul_le_mul_of_nonneg_left hL hb.le]

end JacobiAsym
