import Mathlib
import JacobiAsym.HallGamma

/-! # Paper IV spectral constants: the moment function `W`, Theorem D's constant, Lemma K0

Source: `papers/paperIV/p1_intro.tex` (eq. (W), Theorem D) and `papers/paperIV/p3_kernel.tex`
(Lemma K0, `lem:K0`).

* `Wq p q = (4c)^q Γ(q+½)/(√π Γ(q+1))` with `c = hallC p` (Paper IV eq. (W));
  `Wq_one_div : Wq p (1/p) = 1` ("`W(1/p) = 1` is the definition of `c`").
* `gamma_nat_add_half_ratio : Γ(j+½)/(√π Γ(j+1)) = C(2j,j)/4^j`, hence
  `Wq_nat : Wq p j = C(2j,j) c^j`, and the resonance `centralBinom_mul_hallC_pow_eq_one`:
  if `j p = 1` then `C(2j,j) c(p)^j = 1` (E3 Cor. E3.3, the case `p = 1/j`).
* `theoremD_constant`: for `p > 1`, `q = 1 − 1/p`, `R_q = −κ q/p`,
  `p R_q W(q) π cot(π q) = −2(2−p) c κ` (Theorem D).
* `lemmaK0_gamma` / `lemmaK0_integral`: for real `w < 0`, `w ∉ ℤ`, `w + ½ ∉ ℤ`,
  `B(−w, ½) = Γ(−w)Γ(½)/Γ(½−w) = −π cot(π w) Γ(w+½)/(√π Γ(w+1))` and
  `∫₀¹ u^{−w−1}(1−u)^{−1/2} du = B(−w, ½)` (Lemma K0, real slice). The extra hypothesis
  `w + ½ ∉ ℤ` excludes the removable points where `cot(πw) = 0` meets a pole of `Γ(w+½)`
  (Lean's `Γ` is `0` at poles, so the meromorphic identity cannot be read literally there). -/

open Real Set MeasureTheory

namespace JacobiAsym

/-- Paper IV eq. (W): `W(q) = (4c)^q Γ(q+½)/(√π Γ(q+1))`, `c = c(p) = hallC p`. -/
noncomputable def Wq (p q : ℝ) : ℝ :=
  (4 * hallC p) ^ q * Real.Gamma (q + 1 / 2) / (√π * Real.Gamma (q + 1))

/-- `(4c)^q Γ(q+½)/(√πΓ(q+1))` at `q = 1/p` equals `1`: the defining normalisation of `c(p)`
(Paper IV, after eq. (W)). -/
theorem Wq_one_div {p : ℝ} (hp : 0 < p) : Wq p (1 / p) = 1 := by
  have hL := hallLam_pos hp
  have hG := Real.Gamma_pos_of_pos (show 0 < 1 / p + 1 by positivity)
  have hG' := Real.Gamma_pos_of_pos (show 0 < 1 / p + 1 / 2 by positivity)
  have hs : 0 < √π := Real.sqrt_pos.2 pi_pos
  rw [Wq, four_hallC_rpow hp, hallLam_eq_gamma hp]
  field_simp
  rw [Real.sq_sqrt pi_pos.le]

/-- `Γ(j+½)/(√π Γ(j+1)) = C(2j,j)/4^j` for `j : ℕ`. -/
theorem gamma_nat_add_half_ratio (j : ℕ) :
    Real.Gamma (j + 1 / 2) / (√π * Real.Gamma (j + 1)) = (Nat.centralBinom j : ℝ) / 4 ^ j := by
  have hs : 0 < √π := Real.sqrt_pos.2 pi_pos
  induction j with
  | zero =>
    rw [Nat.cast_zero, zero_add, zero_add, Real.Gamma_one, Real.Gamma_one_half_eq]
    simp [hs.ne']
  | succ n ih =>
    have hG : 0 < Real.Gamma (n + 1) := Real.Gamma_pos_of_pos (by positivity)
    have h1 : Real.Gamma ((n + 1 : ℕ) + 1 / 2) = (n + 1 / 2) * Real.Gamma (n + 1 / 2) := by
      rw [show ((n + 1 : ℕ) : ℝ) + 1 / 2 = (n + 1 / 2) + 1 by push_cast; ring]
      exact Real.Gamma_add_one (by positivity)
    have h2 : Real.Gamma ((n + 1 : ℕ) + 1) = (n + 1) * Real.Gamma (n + 1) := by
      rw [show ((n + 1 : ℕ) : ℝ) + 1 = (n + 1) + 1 by push_cast; ring]
      exact Real.Gamma_add_one (by positivity)
    have hc : ((n + 1 : ℝ)) * (Nat.centralBinom (n + 1) : ℝ) = 2 * (2 * n + 1) * Nat.centralBinom n := by
      exact_mod_cast Nat.succ_mul_centralBinom_succ n
    have hc' : (Nat.centralBinom (n + 1) : ℝ) = 2 * (2 * n + 1) * Nat.centralBinom n / (n + 1) := by
      rw [← hc]; field_simp
    rw [h1, h2, hc', pow_succ]
    rw [div_eq_iff (by positivity)] at ih
    rw [div_eq_iff (by positivity), ih]
    field_simp
    ring

/-- `W(j) = C(2j,j) c^j` for `j : ℕ`. -/
theorem Wq_nat (p : ℝ) (j : ℕ) :
    Wq p j = (Nat.centralBinom j : ℝ) * hallC p ^ j := by
  have h4 : (0 : ℝ) < 4 ^ j := by positivity
  rw [Wq, Real.rpow_natCast, mul_div_assoc, gamma_nat_add_half_ratio, mul_pow]
  field_simp

/-- Resonance (E3 Cor. E3.3, `p = 1/j`; JZC_SHIFT): if `j p = 1` then `C(2j,j) c(p)^j = 1`. -/
theorem centralBinom_mul_hallC_pow_eq_one {p : ℝ} (hp : 0 < p) {j : ℕ} (hj : (j : ℝ) * p = 1) :
    (Nat.centralBinom j : ℝ) * hallC p ^ j = 1 := by
  have hjp : (j : ℝ) = 1 / p := by field_simp; linarith
  rw [← Wq_nat p, hjp, Wq_one_div hp]

/-- **Theorem D's constant** (Paper IV, Theorem D): for `p > 1`, `q = 1 − 1/p`,
`R_q = −κ q/p`: `p R_q W(q) π cot(π q) = −2(2−p) c κ`. At `p = 2` both sides vanish
(`cot(π/2) = 0`). -/
theorem theoremD_constant {p : ℝ} (hp : 1 < p) (κ : ℝ) :
    p * (-κ * (1 - 1 / p) / p) * Wq p (1 - 1 / p) * π * Real.cot (π * (1 - 1 / p)) =
      -2 * (2 - p) * hallC p * κ := by
  have hp0 : 0 < p := by linarith
  set s := 1 / p with hs_def
  have hs0 : 0 < s := by positivity
  have hs1 : s < 1 := by rw [hs_def, div_lt_one hp0]; exact hp
  have hpi := pi_pos
  have hcot : Real.cot (π * (1 - s)) = -(Real.cos (π * s) / Real.sin (π * s)) := by
    rw [Real.cot_eq_cos_div_sin, show π * (1 - s) = π - π * s by ring, cos_pi_sub, sin_pi_sub,
      neg_div]
  rw [hcot]
  rcases eq_or_ne p 2 with rfl | hp2
  · have : Real.cos (π * s) = 0 := by
      rw [hs_def, show π * (1 / 2) = π / 2 by ring, cos_pi_div_two]
    rw [this]; ring
  have hsin : 0 < Real.sin (π * s) := sin_pos_of_pos_of_lt_pi (by positivity) (by nlinarith)
  have hcos : Real.cos (π * s) ≠ 0 := by
    rcases lt_or_gt_of_ne hp2 with h | h
    · have : 1 / 2 < s := by rw [hs_def, lt_div_iff₀ hp0]; linarith
      exact (cos_neg_of_pi_div_two_lt_of_lt (by nlinarith) (by nlinarith)).ne
    · have : s < 1 / 2 := by rw [hs_def, div_lt_iff₀ hp0]; linarith
      exact (cos_pos_of_mem_Ioo ⟨by nlinarith, by nlinarith⟩).ne'
  have hhalf : (1 / 2 - s) ≠ 0 := by
    intro h; apply hcos; rw [show s = 1 / 2 by linarith, show π * (1 / 2) = π / 2 by ring,
      cos_pi_div_two]
  have hc := hallC_pos hp0
  have hL := hallLam_pos hp0
  have hrp : (4 * hallC p) ^ (1 - s) = 4 * hallC p * (hallLam p / π) := by
    rw [Real.rpow_sub (by positivity), Real.rpow_one, hs_def, four_hallC_rpow hp0]
    field_simp
  have hLam : hallLam p = √π * Real.Gamma (s + 1 / 2) / Real.Gamma (s + 1) := hallLam_eq_gamma hp0
  have hsqp : 0 < √π := Real.sqrt_pos.2 hpi
  have hG1 : 0 < Real.Gamma (s + 1 / 2) := Real.Gamma_pos_of_pos (by positivity)
  have hG3 : 0 < Real.Gamma (s + 1) := Real.Gamma_pos_of_pos (by positivity)
  have hG4 : 0 < Real.Gamma (1 - s + 1) := Real.Gamma_pos_of_pos (by linarith)
  -- reflection 1: Γ(s+½) Γ(½−s) = π/cos(πs), and Γ(3/2−s) = (½−s) Γ(½−s)
  have r1 := Real.Gamma_mul_Gamma_one_sub (s + 1 / 2)
  rw [show π * (s + 1 / 2) = π * s + π / 2 by ring, sin_add_pi_div_two] at r1
  have e1 : Real.Gamma (1 - s + 1 / 2) = (1 / 2 - s) * Real.Gamma (1 - (s + 1 / 2)) := by
    have hne : 1 - (s + 1 / 2) ≠ 0 := by rw [show 1 - (s + 1 / 2) = 1 / 2 - s by ring]; exact hhalf
    rw [show 1 - s + 1 / 2 = (1 - (s + 1 / 2)) + 1 by ring, Real.Gamma_add_one hne]
    ring
  -- reflection 2: Γ(s)Γ(1−s) = π/sin(πs), Γ(s+1) = sΓ(s), Γ(2−s) = (1−s)Γ(1−s)
  have r2 := Real.Gamma_mul_Gamma_one_sub s
  have e3 : Real.Gamma (s + 1) = s * Real.Gamma s := Real.Gamma_add_one hs0.ne'
  have e4 : Real.Gamma (1 - s + 1) = (1 - s) * Real.Gamma (1 - s) := Real.Gamma_add_one (by linarith)
  have hps : p = 1 / s := by rw [hs_def]; field_simp
  rw [Wq, hrp, hLam, e1, e3, e4]
  rw [e3] at hG3
  rw [e4] at hG4
  have hs1' : (0 : ℝ) < 1 - s := by linarith
  have hGs : Real.Gamma s ≠ 0 := fun h => by rw [h, mul_zero] at hG3; exact lt_irrefl _ hG3
  have hGs' : Real.Gamma (1 - s) ≠ 0 := fun h => by rw [h, mul_zero] at hG4; exact lt_irrefl _ hG4
  clear_value s
  subst hps
  generalize Real.cos (π * s) = C at *
  generalize Real.sin (π * s) = S at *
  generalize Real.Gamma (s + 1 / 2) = G1 at *
  generalize Real.Gamma (1 - (s + 1 / 2)) = G2 at *
  generalize Real.Gamma s = G3 at *
  generalize Real.Gamma (1 - s) = G4 at *
  generalize hallC (1 / s) = c at *
  generalize √π = r at *
  have hG2 : G2 = π / C / G1 := by field_simp at r1 ⊢; linarith
  have hG4' : G4 = π / S / G3 := by field_simp at r2 ⊢; linarith
  subst hG2 hG4'
  field_simp
  ring

/-- **Lemma K0** (Paper IV, `lem:K0`), Gamma form, real slice: for `w < 0`, `w ∉ ℤ`, `w+½ ∉ ℤ`,
`B(−w, ½) = Γ(−w)Γ(½)/Γ(½−w) = −π cot(πw) Γ(w+½)/(√π Γ(w+1))`. -/
theorem lemmaK0_gamma {w : ℝ} (hw : w < 0) (hwZ : ∀ n : ℤ, w ≠ n) (hwZ' : ∀ n : ℤ, w + 1 / 2 ≠ n) :
    Real.Gamma (-w) * Real.Gamma (1 / 2) / Real.Gamma (-w + 1 / 2) =
      -π * Real.cot (π * w) * Real.Gamma (w + 1 / 2) / (√π * Real.Gamma (w + 1)) := by
  have hpi := pi_pos
  have hsqp : 0 < √π := Real.sqrt_pos.2 hpi
  have hsq : √π * √π = π := Real.mul_self_sqrt hpi.le
  have hsin : Real.sin (π * w) ≠ 0 := by
    intro h
    obtain ⟨n, hn⟩ := Real.sin_eq_zero_iff.1 h
    exact hwZ n (by field_simp at hn; linarith)
  have hcos : Real.cos (π * w) ≠ 0 := by
    intro h
    obtain ⟨k, hk⟩ := Real.cos_eq_zero_iff.1 h
    apply hwZ' (k + 1)
    push_cast
    have : w = (2 * k + 1) / 2 := by field_simp at hk ⊢; linarith
    rw [this]; ring
  have hA : 0 < Real.Gamma (-w) := Real.Gamma_pos_of_pos (by linarith)
  have hD : 0 < Real.Gamma (-w + 1 / 2) := Real.Gamma_pos_of_pos (by linarith)
  have hB : Real.Gamma (w + 1) ≠ 0 := by
    apply Real.Gamma_ne_zero
    intro m hm
    apply hwZ (-(m : ℤ) - 1)
    push_cast; linarith
  have hC : Real.Gamma (w + 1 / 2) ≠ 0 := by
    apply Real.Gamma_ne_zero
    intro m hm
    exact hwZ' (-(m : ℤ)) (by push_cast; linarith)
  -- reflections
  have r1 : Real.Gamma (-w) * Real.Gamma (w + 1) * Real.sin (π * w) = -π := by
    have h := Real.Gamma_mul_Gamma_one_sub (-w)
    rw [show 1 - -w = w + 1 by ring, show π * -w = -(π * w) by ring, Real.sin_neg] at h
    rw [h]; field_simp
  have r2 : Real.Gamma (w + 1 / 2) * Real.Gamma (-w + 1 / 2) = π / Real.cos (π * w) := by
    have h := Real.Gamma_mul_Gamma_one_sub (w + 1 / 2)
    rwa [show π * (w + 1 / 2) = π * w + π / 2 by ring, sin_add_pi_div_two,
      show 1 - (w + 1 / 2) = -w + 1 / 2 by ring] at h
  rw [Real.Gamma_one_half_eq, Real.cot_eq_cos_div_sin]
  generalize Real.cos (π * w) = Cs at *
  generalize Real.sin (π * w) = S at *
  generalize Real.Gamma (-w) = A at *
  generalize Real.Gamma (w + 1) = B at *
  generalize Real.Gamma (w + 1 / 2) = C at *
  generalize Real.Gamma (-w + 1 / 2) = D at *
  have hA' : A = -π / (B * S) := by field_simp; linarith
  have hD' : D = π / (Cs * C) := by field_simp at r2 ⊢; linarith
  subst hA' hD'
  field_simp
  rw [Real.sq_sqrt hpi.le]

/-- **Lemma K0**, integral form (real slice): `∫₀¹ u^{−w−1}(1−u)^{−1/2} du = B(−w,½)
= −π cot(πw) Γ(w+½)/(√π Γ(w+1))` for `w < 0`, `w ∉ ℤ`, `w+½ ∉ ℤ`. -/
theorem lemmaK0_integral {w : ℝ} (hw : w < 0) (hwZ : ∀ n : ℤ, w ≠ n)
    (hwZ' : ∀ n : ℤ, w + 1 / 2 ≠ n) :
    ∫ u in Ioo (0 : ℝ) 1, u ^ (-w - 1) * (1 - u) ^ (-(1 / 2) : ℝ) =
      -π * Real.cot (π * w) * Real.Gamma (w + 1 / 2) / (√π * Real.Gamma (w + 1)) := by
  have h := (betaF_integral (α := -w) (β := 1 / 2) (by linarith) one_half_pos).2
  unfold betaF at h
  rw [show (1 / 2 : ℝ) - 1 = -(1 / 2) by norm_num] at h
  rw [h, lemmaK0_gamma hw hwZ hwZ']

end JacobiAsym
