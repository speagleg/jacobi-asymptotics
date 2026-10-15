import JacobiAsym.HallConst

/-! # Plan 60: the energy functional `𝒥_p` (Paper 1 (1.4), §3.1)

`Fp p u v = log |u^{-p} − v^{-p}|` and `Jp p μ = ∬ Fp p u v dμ(u) dμ(v)` (a Bochner integral over `μ ⊗ μ`;
meaningful when `Fp` is `μ ⊗ μ`-integrable). `AdmissibleOn U μ` is the class of probability measures on `(0, U]`
with `μ (a, b] ≤ b − a` (Paper 1's `𝒜`, restricted to bounded support). -/

open Real Set MeasureTheory Filter Topology
open scoped ENNReal

namespace JacobiAsym

/-- `F(u, v) = log |u^{-p} − v^{-p}|`. -/
noncomputable def Fp (p u v : ℝ) : ℝ := Real.log |u ^ (-p) - v ^ (-p)|

/-- `𝒥_p(μ) = ∬ log |u^{-p} − v^{-p}| dμ(u) dμ(v)`. -/
noncomputable def Jp (p : ℝ) (μ : Measure ℝ) : ℝ := ∫ z, Fp p z.1 z.2 ∂(μ.prod μ)

theorem measurable_Fp (p : ℝ) : Measurable (fun z : ℝ × ℝ => Fp p z.1 z.2) := by
  unfold Fp; fun_prop

theorem Fp_comm (p u v : ℝ) : Fp p u v = Fp p v u := by
  unfold Fp; rw [abs_sub_comm]

/-- Admissible measures with support in `(0, U]` (Paper 1 `𝒜`, `μ ≤ Leb` tested on intervals). -/
structure AdmissibleOn (U : ℝ) (μ : Measure ℝ) : Prop where
  prob : IsProbabilityMeasure μ
  le_zero : μ (Iic 0) = 0
  gt_U : μ (Ioi U) = 0
  lip : ∀ a b, 0 < a → a ≤ b → μ (Ioc a b) ≤ ENNReal.ofReal (b - a)

end JacobiAsym
