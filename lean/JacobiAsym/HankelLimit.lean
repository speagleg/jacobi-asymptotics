import JacobiAsym.Andreief
import JacobiAsym.Inputs

open Finset Filter Topology Matrix

namespace JacobiAsym

/-- Hankel moment matrix of the infinite measure. -/
noncomputable def hankel (x w : ℕ → ℝ) (n : ℕ) : Matrix (Fin n) (Fin n) ℝ :=
  Matrix.of fun i j => ∑' k, w k * x k ^ ((i : ℕ) + j)

theorem moment_summable {x w : ℕ → ℝ} {X : ℝ} (hw : ∀ k, 0 ≤ w k) (hws : Summable w)
    (hx : ∀ k, |x k| ≤ X) (r : ℕ) : Summable (fun k => w k * x k ^ r) := by
  have hX : 0 ≤ X := (abs_nonneg _).trans (hx 0)
  refine Summable.of_norm_bounded (hws.mul_left (X ^ r)) (fun k => ?_)
  rw [Real.norm_eq_abs, abs_mul, abs_of_nonneg (hw k), abs_pow, mul_comm]
  exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (abs_nonneg _) (hx k) r) (hw k)

theorem heineK_tendsto_det {x w : ℕ → ℝ} {X : ℝ} (hw : ∀ k, 0 ≤ w k) (hws : Summable w)
    (hx : ∀ k, |x k| ≤ X) (n : ℕ) :
    Tendsto (fun K => heineK x w K n) atTop (𝓝 (hankel x w n).det) := by
  have hmat : Tendsto (fun K => hankelK x w K n) atTop (𝓝 (hankel x w n)) := by
    refine tendsto_pi_nhds.2 fun i => tendsto_pi_nhds.2 fun j => ?_
    exact (moment_summable hw hws hx ((i : ℕ) + j)).hasSum.tendsto_sum_nat
  have hdet := ((continuous_id.matrix_det).tendsto (hankel x w n)).comp hmat
  simpa [Function.comp_def, heineK_eq_det] using hdet

theorem heineK_bdd_of_summable {x w : ℕ → ℝ} {X : ℝ} (hw : ∀ k, 0 ≤ w k) (hws : Summable w)
    (hx : ∀ k, |x k| ≤ X) (n : ℕ) : BddAbove (Set.range fun K => heineK x w K n) := by
  have hmono : Monotone (fun K => heineK x w K n) := fun K K' h => heineK_mono_K hw h n
  refine ⟨(hankel x w n).det, ?_⟩
  rintro _ ⟨K, rfl⟩
  exact hmono.ge_of_tendsto (heineK_tendsto_det hw hws hx n) K

theorem heineD_eq_det {x w : ℕ → ℝ} {X : ℝ} (hw : ∀ k, 0 ≤ w k) (hws : Summable w) (hx : ∀ k, |x k| ≤ X)
    (n : ℕ) : heineD x w n = (hankel x w n).det := by
  have hmono : Monotone (fun K => heineK x w K n) := fun K K' h => heineK_mono_K hw h n
  exact tendsto_nhds_unique (tendsto_atTop_ciSup hmono (heineK_bdd_of_summable hw hws hx n))
    (heineK_tendsto_det hw hws hx n)

end JacobiAsym
