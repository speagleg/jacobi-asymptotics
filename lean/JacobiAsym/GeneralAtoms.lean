import JacobiAsym.Spacing
import JacobiAsym.HallGamma

/-! # Plan 61, stage G3: Paper 1 Theorem 1.1 for general atoms `x_k = f(k)`

Hypotheses on `f` (Paper 1 (1.4)), with `f'` given explicitly:
* `f ∈ C¹[1,∞)`: `∀ ξ ∈ Ici 1, HasDerivWithinAt f (f' ξ) (Ici 1) ξ` and `ContinuousOn f' (Ici 1)`;
* `ξ^{p+1} f'(ξ) → −pC` as `ξ → ∞`;
* `0 < inf_{ξ≥1} ξ^{p+1}|f'(ξ)| ≤ sup_{ξ≥1} ξ^{p+1}|f'(ξ)| < ∞`, stated as
  `∃ m M, 0 < m ∧ ∀ ξ ≥ 1, m ≤ ξ^{p+1}|f' ξ| ∧ ξ^{p+1}|f' ξ| ≤ M`.

Proof (Paper 1 §6): `f' < 0` (continuity + IVT), Cauchy's mean value theorem against `h(ξ) = Cξ^{−p}` gives
`PairRatio (f(k+1)) (C (k+1)^{−p})`, then `hnorm_transfer` (Lemma 2.3), `scaled_law` (Lemma 2.2(iii)) and
`pure_law_w` (Theorems 4.3, 5.2, 1.3(iii)). -/

open Real Set Filter Topology Finset

namespace JacobiAsym

section Atoms

variable {p C : ℝ} {f f' : ℝ → ℝ}

/-- `f' < 0` on `[1, ∞)`: `f'` is continuous, never `0`, and eventually negative. -/
theorem deriv_neg_of_hyp (hp : 0 < p) (hC : 0 < C) (hf'c : ContinuousOn f' (Ici 1))
    (hlim : Tendsto (fun ξ => ξ ^ (p + 1) * f' ξ) atTop (𝓝 (-p * C)))
    (hbd : ∃ m M : ℝ, 0 < m ∧ ∀ ξ, 1 ≤ ξ → m ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ M) :
    ∀ ξ, 1 ≤ ξ → f' ξ < 0 := by
  obtain ⟨m, M, hm, hb⟩ := hbd
  have hne : ∀ ξ, 1 ≤ ξ → f' ξ ≠ 0 := by
    intro ξ hξ h0
    have := (hb ξ hξ).1
    rw [h0, abs_zero, mul_zero] at this
    linarith
  have hev : ∀ᶠ ξ in atTop, ξ ^ (p + 1) * f' ξ < 0 :=
    hlim.eventually (gt_mem_nhds (by nlinarith))
  intro ξ0 hξ0
  by_contra hcon
  have hpos : 0 < f' ξ0 := lt_of_le_of_ne (not_lt.1 hcon) (hne ξ0 hξ0).symm
  obtain ⟨T, hT⟩ := eventually_atTop.1 hev
  set ξ1 := max ξ0 (max T 1)
  have h11 : 1 ≤ ξ1 := le_trans (le_max_right _ _) (le_max_right _ _)
  have hneg : f' ξ1 < 0 := by
    have h := hT ξ1 (le_trans (le_max_left _ _) (le_max_right _ _))
    have : 0 < ξ1 ^ (p + 1) := rpow_pos_of_pos (by linarith) _
    by_contra h'
    push Not at h'
    nlinarith
  have hcont : ContinuousOn f' (Icc ξ0 ξ1) := hf'c.mono fun t ht => le_trans hξ0 ht.1
  obtain ⟨c, hc, hc0⟩ := intermediate_value_Icc' (le_max_left _ _) hcont ⟨hneg.le, hpos.le⟩
  exact hne c (le_trans hξ0 hc.1) hc0

/-- Mean value step: if `lo·pC ≤ ξ^{p+1}|f'(ξ)| ≤ hi·pC` for all `ξ ≥ T` (`T ≥ 1`), then for `T ≤ u < v`,
`lo (h(u) − h(v)) ≤ f(u) − f(v) ≤ hi (h(u) − h(v))`, `h(ξ) = C ξ^{−p}`. -/
theorem gap_bounds (hp : 0 < p) (hC : 0 < C) (hf : ∀ ξ ∈ Ici (1 : ℝ), HasDerivWithinAt f (f' ξ) (Ici 1) ξ)
    (hneg : ∀ ξ, 1 ≤ ξ → f' ξ < 0) {T lo hi : ℝ} (hT : 1 ≤ T)
    (hr : ∀ ξ, T ≤ ξ → lo * (p * C) ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ hi * (p * C))
    {u v : ℝ} (hu : T ≤ u) (huv : u < v) :
    lo * (C * u ^ (-p) - C * v ^ (-p)) ≤ f u - f v ∧ f u - f v ≤ hi * (C * u ^ (-p) - C * v ^ (-p)) := by
  have hcf : ContinuousOn f (Icc u v) := fun t ht =>
    ((hf t (le_trans (le_trans hT hu) ht.1)).continuousWithinAt).mono fun s hs =>
      le_trans (le_trans hT hu) hs.1
  have hg' : ∀ t, 0 < t → HasDerivAt (fun t => C * t ^ (-p)) (C * (-p * t ^ (-p - 1))) t := fun t ht =>
    (hasDerivAt_rpow_const (Or.inl ht.ne')).const_mul C
  have hcg : ContinuousOn (fun t => C * t ^ (-p)) (Icc u v) := fun t ht =>
    (hg' t (by linarith [ht.1])).continuousAt.continuousWithinAt
  have hkey : ∀ t, T < t → -f' t = t ^ (-p - 1) * (t ^ (p + 1) * |f' t|) := by
    intro t ht
    have ht0 : 0 < t := by linarith
    rw [abs_of_neg (hneg t (by linarith)), ← mul_assoc, ← rpow_add ht0]
    have : -p - 1 + (p + 1) = 0 := by ring
    rw [this, rpow_zero]; ring
  apply ratio_bounds_of_deriv huv hcf hcg
  · intro t ht
    exact (hf t (show (1 : ℝ) ≤ t by linarith [ht.1])).hasDerivAt (Ici_mem_nhds (by linarith [ht.1]))
  · intro t ht; exact hg' t (by linarith [ht.1])
  · intro t ht
    have : 0 < t ^ (-p - 1) := rpow_pos_of_pos (by linarith [ht.1]) _
    have : 0 < C * p := mul_pos hC hp
    nlinarith
  · intro t ht
    have ht' : T < t := by linarith [ht.1]
    rw [hkey t ht']
    have h1 := (hr t ht'.le).1
    have : 0 < t ^ (-p - 1) := rpow_pos_of_pos (by linarith) _
    nlinarith
  · intro t ht
    have ht' : T < t := by linarith [ht.1]
    rw [hkey t ht']
    have h1 := (hr t ht'.le).2
    have : 0 < t ^ (-p - 1) := rpow_pos_of_pos (by linarith) _
    nlinarith

/-- `u ≤ k v`, `0 ≤ u`, `k ≤ K` (with `0 ≤ v`) give `u² ≤ K² v²`. -/
theorem sq_le_of_le_mul {u v k K : ℝ} (hu : 0 ≤ u) (hv : 0 ≤ v) (huv : u ≤ k * v) (hkK : k ≤ K) :
    u ^ 2 ≤ K ^ 2 * v ^ 2 := by
  have h1 : u ≤ K * v := huv.trans (mul_le_mul_of_nonneg_right hkK hv)
  have h2 : 0 ≤ K * v := hu.trans h1
  rw [← mul_pow]
  exact pow_le_pow_left₀ hu h1 2

/-- The atoms `x_k = f(k+1)` and `y_k = C (k+1)^{−p}` satisfy `PairRatio` (Cauchy MVT step of Lemma 2.3), and the
global gap bounds `x_a − x_b ≤ (M/(pC)) (y_a − y_b)`, `(m/(pC)) (y_a − y_b) ≤ x_a − x_b`. -/
theorem pairRatio_of_hyp (hp : 0 < p) (hC : 0 < C)
    (hf : ∀ ξ ∈ Ici (1 : ℝ), HasDerivWithinAt f (f' ξ) (Ici 1) ξ) (hf'c : ContinuousOn f' (Ici 1))
    (hlim : Tendsto (fun ξ => ξ ^ (p + 1) * f' ξ) atTop (𝓝 (-p * C)))
    (hbd : ∃ m M : ℝ, 0 < m ∧ ∀ ξ, 1 ≤ ξ → m ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ M) :
    PairRatio (fun k : ℕ => f ((k : ℝ) + 1)) (fun k => C * powSeq p k) ∧
    ∃ lo hi : ℝ, 0 < lo ∧ ∀ a b : ℕ, a < b →
      lo * (C * powSeq p a - C * powSeq p b) ≤ f ((a : ℝ) + 1) - f ((b : ℝ) + 1) ∧
      f ((a : ℝ) + 1) - f ((b : ℝ) + 1) ≤ hi * (C * powSeq p a - C * powSeq p b) := by
  have hneg := deriv_neg_of_hyp hp hC hf'c hlim hbd
  obtain ⟨m, M, hm, hb⟩ := hbd
  have hpC : 0 < p * C := mul_pos hp hC
  set lo := m / (p * C)
  set hi := M / (p * C)
  have hlo : 0 < lo := div_pos hm hpC
  have hglob : ∀ ξ, 1 ≤ ξ → lo * (p * C) ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ hi * (p * C) := by
    intro ξ hξ
    simp only [lo, hi, div_mul_cancel₀ _ hpC.ne']
    exact hb ξ hξ
  have hcast : ∀ a : ℕ, (1 : ℝ) ≤ (a : ℝ) + 1 := fun a => by have := Nat.cast_nonneg (α := ℝ) a; linarith
  have hylt : ∀ a b : ℕ, a < b → 0 < C * powSeq p a - C * powSeq p b := fun a b hab => by
    have := powSeq_strictAnti hp hab; nlinarith
  have hgap : ∀ a b : ℕ, a < b → (a : ℝ) + 1 < (b : ℝ) + 1 := fun a b hab => by
    have : (a : ℝ) < b := by exact_mod_cast hab
    linarith
  have hglobal : ∀ a b : ℕ, a < b →
      lo * (C * powSeq p a - C * powSeq p b) ≤ f ((a : ℝ) + 1) - f ((b : ℝ) + 1) ∧
      f ((a : ℝ) + 1) - f ((b : ℝ) + 1) ≤ hi * (C * powSeq p a - C * powSeq p b) := fun a b hab =>
    gap_bounds hp hC hf hneg le_rfl hglob (hcast a) (hgap a b hab)
  refine ⟨?_, lo, hi, hlo, hglobal⟩
  intro ε hε
  -- eventually `e^{−ε} pC ≤ ξ^{p+1}|f'| ≤ e^{ε} pC`
  have hlim' : Tendsto (fun ξ => ξ ^ (p + 1) * |f' ξ|) atTop (𝓝 (p * C)) := by
    have h := hlim.neg
    rw [neg_mul, neg_neg] at h
    refine h.congr' ?_
    filter_upwards [eventually_ge_atTop 1] with ξ hξ
    rw [abs_of_neg (hneg ξ hξ)]; ring
  have hin : p * C ∈ Ioo (Real.exp (-ε) * (p * C)) (Real.exp ε * (p * C)) := by
    constructor
    · have : Real.exp (-ε) < 1 := Real.exp_lt_one_iff.2 (by linarith)
      nlinarith
    · have : 1 < Real.exp ε := Real.one_lt_exp_iff.2 hε
      nlinarith
  obtain ⟨T0, hT0⟩ := eventually_atTop.1 (hlim'.eventually (Ioo_mem_nhds hin.1 hin.2))
  set T := max T0 1
  set a0 := ⌈T⌉₊
  set B := max (max hi lo⁻¹) 1
  refine ⟨a0, B, le_max_right _ _, fun a b hab => ?_⟩
  have hD := hylt a b hab
  have hex : 1 ≤ Real.exp ε := Real.one_le_exp hε.le
  by_cases ha : a < a0
  · simp only [ha, ↓reduceIte]
    obtain ⟨h1, h2⟩ := hglobal a b hab
    have hx0 : 0 ≤ f ((a : ℝ) + 1) - f ((b : ℝ) + 1) := le_trans (by positivity) h1
    have hhiB : hi ≤ B * Real.exp ε :=
      (le_trans (le_max_left _ _) (le_max_left _ _)).trans (le_mul_of_one_le_right (by positivity) hex)
    have hloB : lo⁻¹ ≤ B * Real.exp ε :=
      (le_trans (le_max_right _ _) (le_max_left _ _)).trans (le_mul_of_one_le_right (by positivity) hex)
    constructor
    · rw [← mul_pow]; exact sq_le_of_le_mul hx0 hD.le h2 hhiB
    · rw [← mul_pow]
      refine sq_le_of_le_mul hD.le hx0 ?_ hloB
      rw [inv_mul_eq_div, le_div_iff₀ hlo]; linarith
  · simp only [ha, ↓reduceIte, one_pow, one_mul]
    have hTa : T ≤ (a : ℝ) + 1 := by
      have : T ≤ (a0 : ℝ) := Nat.le_ceil T
      have : (a0 : ℝ) ≤ a := by exact_mod_cast not_lt.1 ha
      linarith
    have hr : ∀ ξ, T ≤ ξ → Real.exp (-ε) * (p * C) ≤ ξ ^ (p + 1) * |f' ξ| ∧
        ξ ^ (p + 1) * |f' ξ| ≤ Real.exp ε * (p * C) := fun ξ hξ => by
      have := hT0 ξ (le_trans (le_max_left _ _) hξ)
      exact ⟨this.1.le, this.2.le⟩
    obtain ⟨h1, h2⟩ := gap_bounds hp hC hf hneg (le_max_right _ _) hr hTa (hgap a b hab)
    have hx0 : 0 ≤ f ((a : ℝ) + 1) - f ((b : ℝ) + 1) := le_trans (by positivity) h1
    simp only [powSeq] at hD ⊢
    constructor
    · exact sq_le_of_le_mul hx0 hD.le h2 le_rfl
    · refine sq_le_of_le_mul hD.le hx0 ?_ le_rfl
      have : Real.exp ε * Real.exp (-ε) = 1 := by rw [← Real.exp_add]; simp
      nlinarith [Real.exp_pos ε]

end Atoms

/-- Atoms `f(k+1)` are strictly decreasing and bounded under the hypotheses of Theorem 1.1. -/
theorem atoms_of_hyp {p C : ℝ} {f f' : ℝ → ℝ} (hp : 0 < p) (hC : 0 < C)
    (hf : ∀ ξ ∈ Ici (1 : ℝ), HasDerivWithinAt f (f' ξ) (Ici 1) ξ) (hf'c : ContinuousOn f' (Ici 1))
    (hlim : Tendsto (fun ξ => ξ ^ (p + 1) * f' ξ) atTop (𝓝 (-p * C)))
    (hbd : ∃ m M : ℝ, 0 < m ∧ ∀ ξ, 1 ≤ ξ → m ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ M) :
    PairRatio (fun k : ℕ => f ((k : ℝ) + 1)) (fun k => C * powSeq p k) ∧
    StrictAnti (fun k : ℕ => f ((k : ℝ) + 1)) ∧ ∃ X, ∀ k : ℕ, |f ((k : ℝ) + 1)| ≤ X := by
  obtain ⟨hPR, lo, hi, hlo, hgl⟩ := pairRatio_of_hyp hp hC hf hf'c hlim hbd
  have hylt : ∀ a b : ℕ, a < b → 0 < C * powSeq p a - C * powSeq p b := fun a b hab => by
    have := powSeq_strictAnti hp hab; nlinarith
  refine ⟨hPR, fun a b hab => ?_, |f 1| + |hi| * C, fun k => ?_⟩
  · have := (hgl a b hab).1
    have := hylt a b hab
    have : 0 < lo * (C * powSeq p a - C * powSeq p b) := mul_pos hlo this
    linarith
  · rcases Nat.eq_zero_or_pos k with hk | hk
    · subst hk; simp only [Nat.cast_zero, zero_add]
      have := abs_nonneg hi; nlinarith
    · obtain ⟨h1, h2⟩ := hgl 0 k hk
      have hD := hylt 0 k hk
      have hp0 : powSeq p 0 = 1 := by simp [powSeq]
      have hpk := powSeq_pos p k
      simp only [Nat.cast_zero, zero_add] at h1 h2
      rw [hp0] at h1 h2 hD
      have hx0 : 0 ≤ f 1 - f ((k : ℝ) + 1) := le_trans (mul_pos hlo hD).le h1
      have h3 : hi * (C * 1 - C * powSeq p k) ≤ |hi| * C := by
        calc hi * (C * 1 - C * powSeq p k) ≤ |hi| * (C * 1 - C * powSeq p k) :=
              mul_le_mul_of_nonneg_right (le_abs_self hi) hD.le
          _ ≤ |hi| * C := mul_le_mul_of_nonneg_left (by nlinarith) (abs_nonneg hi)
      rw [abs_le]
      constructor
      · have := neg_abs_le (f 1); linarith
      · have := le_abs_self (f 1); have := abs_nonneg hi; nlinarith

/-- **Paper 1 Theorem 1.1, Heine form, `κ_p` as `hallKappa p`.** -/
theorem paper1_thm11_heine {p C s c1 : ℝ} {f f' : ℝ → ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hC : 0 < C)
    (hf : ∀ ξ ∈ Ici (1 : ℝ), HasDerivWithinAt f (f' ξ) (Ici 1) ξ) (hf'c : ContinuousOn f' (Ici 1))
    (hlim : Tendsto (fun ξ => ξ ^ (p + 1) * f' ξ) atTop (𝓝 (-p * C)))
    (hbd : ∃ m M : ℝ, 0 < m ∧ ∀ ξ, 1 ≤ ξ → m ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ M)
    (hw0 : ∀ k, 0 ≤ w k) (hws : Summable w) (hc1 : 0 < c1)
    (hwlo : ∀ k : ℕ, c1 * ((k : ℝ) + 1) ^ (-s) ≤ w k) :
    Tendsto (hnorm p (hallKappa p + Real.log C) (heineD (fun k : ℕ => f ((k : ℝ) + 1)) w) (fun _ => 0))
      atTop (𝓝 0) := by
  obtain ⟨hPR, hxa, X, hX⟩ := atoms_of_hyp hp hC hf hf'c hlim hbd
  have hwp : ∀ k, 0 < w k := fun k => (mul_pos hc1 (powSeq_pos s k)).trans_le (hwlo k)
  have hbp := heineK_bdd_of_summable hw0 hws (powSeq_abs_le_one hp)
  have hy0 := pure_law_w hp hc1 hw0 hws (s := s) hwlo
  have hy := scaled_law hC (fun n => heineD_pos (powSeq_strictAnti hp) hwp (hbp n)) hy0
  have hyabs : ∀ k, |C * powSeq p k| ≤ C := fun k => by
    rw [abs_mul, abs_of_pos hC]
    exact mul_le_of_le_one_right hC.le (powSeq_abs_le_one hp k)
  have hya : StrictAnti (fun k => C * powSeq p k) := fun a b hab => by
    have := powSeq_strictAnti hp hab; nlinarith
  have hby := heineK_bdd_of_summable hw0 hws hyabs
  have hbx := heineK_bdd_of_summable hw0 hws hX
  exact hnorm_transfer hPR hw0 hbx hby (fun n => heineD_pos hxa hwp (hbx n))
    (fun n => heineD_pos hya hwp (hby n)) hy

/-- **Paper 1 Theorem 1.1 (general atoms), as stated.** Let `p > 0`, `C > 0`, and `f ∈ C¹[1,∞)` with derivative `f'`
(one-sided at `1`; `f'` continuous on `[1,∞)`) such that `ξ^{p+1} f'(ξ) → −pC` and
`0 < inf_{ξ≥1} ξ^{p+1}|f'(ξ)| ≤ sup_{ξ≥1} ξ^{p+1}|f'(ξ)| < ∞`. Let `w ≥ 0` with `Σ w < ∞` and `w_k ≥ c₁ k^{−s}`
(`c₁ > 0`, `s ∈ ℝ` arbitrary). Then for `σ = Σ_{k≥1} w_k δ_{f(k)}` and `D_n = det(m_{i+j})_{i,j<n}`,
`log D_n = −p n² log n + (κ_p + log C) n² + o(n²)`, `κ_p = 3p/2 + log c(p)`, `c(p) = ¼ (π/(2I(p)))^p`,
`I(p) = (√π/2) Γ(1/p+1/2)/Γ(1/p+1)` (`hallI p`).

Lean indexing is 0-based: atom `k` is `f(k+1)` and weight `w k` is the paper's `w_{k+1}`. No hypothesis is
strengthened. -/
theorem paper1_thm11 {p C s c1 : ℝ} {f f' : ℝ → ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hC : 0 < C)
    (hf : ∀ ξ ∈ Ici (1 : ℝ), HasDerivWithinAt f (f' ξ) (Ici 1) ξ) (hf'c : ContinuousOn f' (Ici 1))
    (hlim : Tendsto (fun ξ => ξ ^ (p + 1) * f' ξ) atTop (𝓝 (-p * C)))
    (hbd : ∃ m M : ℝ, 0 < m ∧ ∀ ξ, 1 ≤ ξ → m ≤ ξ ^ (p + 1) * |f' ξ| ∧ ξ ^ (p + 1) * |f' ξ| ≤ M)
    (hw0 : ∀ k, 0 ≤ w k) (hws : Summable w) (hc1 : 0 < c1)
    (hwlo : ∀ k : ℕ, c1 * ((k : ℝ) + 1) ^ (-s) ≤ w k) :
    Tendsto (fun n : ℕ => (Real.log (hankel (fun k : ℕ => f ((k : ℝ) + 1)) w n).det -
        (-p * (n : ℝ) ^ 2 * Real.log n +
          (3 * p / 2 + Real.log ((π / (2 * hallI p)) ^ p / 4) + Real.log C) * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2)
      atTop (𝓝 0) := by
  obtain ⟨-, -, X, hX⟩ := atoms_of_hyp hp hC hf hf'c hlim hbd
  have h := paper1_thm11_heine hp hC hf hf'c hlim hbd hw0 hws hc1 hwlo
  rw [hallKappa_eq hp] at h
  refine h.congr fun n => ?_
  unfold hnorm
  rw [heineD_eq_det hw0 hws hX]
  ring

end JacobiAsym
