import JacobiAsym.Basic

namespace JacobiAsym

/-- `-(1-t) log (1-t) ≤ t` on `[0,1]` (at `t = 1` both sides use `Real.log 0 = 0`). -/
theorem neg_mul_log_le {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t ≤ 1) : -((1 - t) * Real.log (1 - t)) ≤ t := by
  rcases eq_or_lt_of_le ht1 with rfl | ht1'
  · simp
  have hu : 0 < 1 - t := by linarith
  have h := Real.log_le_sub_one_of_pos (inv_pos.2 hu)
  rw [Real.log_inv] at h
  have hinv : (1 - t) * (1 - t)⁻¹ = 1 := mul_inv_cancel₀ hu.ne'
  nlinarith [mul_le_mul_of_nonneg_left h hu.le]

/-- Lemma H7 penalty: `φ_M(t) ≤ A²/(4 p log M)`, `A = 4p + 2|κ|`, for `t ∈ [0,1]`, `p > 0`, `M > 1`. -/
theorem phi_bound {p κ M t : ℝ} (hp : 0 < p) (hM : 1 < M) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    -p * (1 - t ^ 2) * Real.log (1 - t) + 2 * p * t * (1 - t) - κ * t * (2 - t) - p * t ^ 2 * Real.log M
      ≤ (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) := by
  have hL : 0 < Real.log M := Real.log_pos hM
  have hnl := neg_mul_log_le ht0 ht1
  have h1 : -p * (1 - t ^ 2) * Real.log (1 - t) ≤ 2 * p * t := by
    have e : -p * (1 - t ^ 2) * Real.log (1 - t) = p * (1 + t) * (-((1 - t) * Real.log (1 - t))) := by ring
    rw [e]
    calc p * (1 + t) * (-((1 - t) * Real.log (1 - t))) ≤ p * (1 + t) * t := by
          apply mul_le_mul_of_nonneg_left hnl; positivity
      _ ≤ 2 * p * t := by nlinarith [mul_nonneg (mul_nonneg hp.le ht0) (sub_nonneg.2 ht1)]
  have h2 : 2 * p * t * (1 - t) ≤ 2 * p * t := by nlinarith
  have h3 : -κ * t * (2 - t) ≤ 2 * |κ| * t := by
    have ht2 : 0 ≤ t * (2 - t) := by nlinarith
    have : -κ * t * (2 - t) ≤ |κ| * (t * (2 - t)) := by
      have := neg_abs_le κ
      nlinarith [abs_nonneg κ]
    nlinarith [abs_nonneg κ]
  set A := 4 * p + 2 * |κ| with hA
  have hAt : -p * (1 - t ^ 2) * Real.log (1 - t) + 2 * p * t * (1 - t) - κ * t * (2 - t) ≤ A * t := by
    rw [hA]; linarith
  rw [le_div_iff₀ (by positivity)]
  nlinarith [sq_nonneg (2 * p * Real.log M * t - A), mul_pos hp hL]

end JacobiAsym
