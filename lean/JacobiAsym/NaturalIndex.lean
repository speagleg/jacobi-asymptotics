import Mathlib

/-! # The natural index of Paper IV and the n-expansion of Thm E2.1

Notation (Paper IV, `papers/paperIV/p1_intro.tex` §1.2; `research/G1/RH/second_order/E2_pgt1.md` §0):
`p > 0`, `s` real, `α = (s − 1 − p)/p` (`alphaP`), natural index (Paper IV eq. (1.6), `eq:N`)
`N = n + α/2 + 1/2 = n + a` with `a = (α + 1)/2` (`natIndex`, `natShift`),
`f₂ = (p+1)/12 − (p+2)α²/8` (Theorem A(iii), `f2`),
`d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12` (Thm E2.1, `d2`).

The natural index absorbs the `1/n` term and the `(s−1)²` part of the `n⁻²` term of `n^p b_n / c`:
`(n/N)^p (1 + f₂/N²) = 1 − (s−1)/(2n) + d₂/n² + O(n⁻³)` (`natural_expansion`, coefficient identities
`neg_mul_natShift`, `natShift_sq_add_f2`). Hence the integer layer of Theorem A to order `N⁻²` (remainder
`O(N⁻³)`) is equivalent to the form of Thm E2.1 with remainder `O(n⁻³)` (`naturalForm_iff_E21`).
Only the elementary asymptotic bookkeeping is formalized here; `b_n` itself is an arbitrary sequence `y`. -/

open Filter Asymptotics Topology

namespace JacobiAsym

/-- Second-order binomial Taylor bound: `(1 + x)^q = 1 + qx + q(q−1)/2·x² + O(x³)` as `x → 0`
(the `(1 + a/n)^{−p}` expansion hinted in the task for the passage Paper IV Theorem A ⇒ E2_pgt1.md
Remark E2.8 / Thm E2.1; from Mathlib's binomial power series). -/
theorem one_add_rpow_taylor2 (q : ℝ) :
    (fun x : ℝ => (1 + x) ^ q - (1 + q * x + q * (q - 1) / 2 * x ^ 2)) =O[𝓝 0] fun x => x ^ 3 := by
  have h := (Real.one_add_rpow_hasFPowerSeriesAt_zero (a := q)).isBigO_sub_partialSum_pow 3
  have hc2 : Ring.choose q 2 = q * (q - 1) / 2 := by
    rw [Ring.choose_eq_smul]
    simp [descPochhammer_succ_right, Polynomial.smeval_mul, Polynomial.smeval_sub,
      Polynomial.smeval_X]
    ring
  simp only [FormalMultilinearSeries.partialSum, Finset.sum_range_succ, Finset.sum_range_zero,
    binomialSeries_apply, zero_add, List.ofFn_const, List.prod_replicate, smul_eq_mul,
    Ring.choose_zero_right, Ring.choose_one_right, hc2, Real.norm_eq_abs] at h
  have h' : (fun x : ℝ => (1 + x) ^ q - (1 + q * x + q * (q - 1) / 2 * x ^ 2)) =O[𝓝 0]
      fun x => |x ^ 3| := by
    simpa [abs_pow] using h
  exact h'.of_abs_right


/-- `x = 1/n` form of `natural_expansion`: `(1 + ax)^{−p}(1 + f x²/(1 + ax)²) =
1 − pa x + (p(p+1)/2·a² + f) x² + O(x³)` as `x → 0`, for all real `p, a, f`
(Paper IV `p1_intro.tex` eq. (1.6) and Theorem A(iii), integer layer). -/
theorem natural_expansion_x (p a f : ℝ) :
    (fun x : ℝ => (1 + a * x) ^ (-p) * (1 + f * x ^ 2 / (1 + a * x) ^ 2)
      - (1 - p * a * x + (p * (p + 1) / 2 * a ^ 2 + f) * x ^ 2)) =O[𝓝 0] fun x => x ^ 3 := by
  set T : ℝ → ℝ := fun x => 1 - p * a * x + p * (p + 1) / 2 * a ^ 2 * x ^ 2 with hT
  set B : ℝ → ℝ := fun x => 1 + f * x ^ 2 / (1 + a * x) ^ 2 with hB
  have hlin : Tendsto (fun x : ℝ => a * x) (𝓝 0) (𝓝 0) := by
    simpa using (tendsto_id (x := 𝓝 (0 : ℝ))).const_mul a
  have hden : ∀ᶠ x in 𝓝 (0 : ℝ), 1 + a * x ≠ 0 :=
    (continuous_const.add (continuous_const.mul continuous_id)).continuousAt.eventually_ne
      (by simp)
  -- E1 = (1 + a x)^{-p} - T x = O(x^3)
  have hE1 : (fun x : ℝ => (1 + a * x) ^ (-p) - T x) =O[𝓝 0] fun x => x ^ 3 := by
    have h1 := (one_add_rpow_taylor2 (-p)).comp_tendsto hlin
    have h2 : (fun x : ℝ => (a * x) ^ 3) =O[𝓝 0] fun x => x ^ 3 := by
      simp_rw [mul_pow]; exact (isBigO_refl _ _).const_mul_left _
    refine (h1.trans h2).congr_left (fun x => ?_)
    simp only [Function.comp, hT]; ring
  -- E2 = B x - 1 - f x^2 = O(x^3)
  have hE2 : (fun x : ℝ => B x - (1 + f * x ^ 2)) =O[𝓝 0] fun x => x ^ 3 := by
    have hc : ContinuousAt (fun x : ℝ => -(f * a) * (2 + a * x) / (1 + a * x) ^ 2) 0 :=
      ContinuousAt.div (by fun_prop) (by fun_prop) (by simp)
    have h1 := (isBigO_refl (fun x : ℝ => x ^ 3) (𝓝 0)).mul (hc.tendsto.isBigO_one ℝ)
    simp only [mul_one] at h1
    refine h1.congr' ?_ (Eventually.of_forall fun _ => rfl)
    filter_upwards [hden] with x hx
    show x ^ 3 * (-(f * a) * (2 + a * x) / (1 + a * x) ^ 2)
      = (1 + f * x ^ 2 / (1 + a * x) ^ 2) - (1 + f * x ^ 2)
    have hx2 : (1 + a * x) ^ 2 ≠ 0 := pow_ne_zero 2 hx
    rw [add_sub_add_left_eq_sub, mul_div_assoc', div_sub' hx2, div_left_inj' hx2]
    ring
  have hTb : T =O[𝓝 0] fun _ => (1 : ℝ) := by
    have : ContinuousAt T 0 := by simp only [hT]; fun_prop
    exact this.tendsto.isBigO_one ℝ
  have hBb : B =O[𝓝 0] fun _ => (1 : ℝ) := by
    have : ContinuousAt B 0 := by
      simp only [hB]
      exact continuousAt_const.add (ContinuousAt.div (by fun_prop) (by fun_prop) (by simp))
    exact this.tendsto.isBigO_one ℝ
  have hpoly : (fun x : ℝ => T x * (1 + f * x ^ 2)
      - (1 - p * a * x + (p * (p + 1) / 2 * a ^ 2 + f) * x ^ 2)) =O[𝓝 0] fun x => x ^ 3 := by
    have hc : ContinuousAt (fun x : ℝ => -(p * a * f) + p * (p + 1) / 2 * a ^ 2 * f * x) 0 := by
      fun_prop
    have h1 := (isBigO_refl (fun x : ℝ => x ^ 3) (𝓝 0)).mul (hc.tendsto.isBigO_one ℝ)
    simp only [mul_one] at h1
    refine h1.congr_left (fun x => ?_)
    simp only [hT]; ring
  have h3 := hTb.mul hE2
  have h4 := hE1.mul hBb
  simp only [one_mul, mul_one] at h3 h4
  have hsum := hpoly.add (h3.add h4)
  refine hsum.congr_left (fun x => ?_)
  simp only [hB]; ring

/-- **Natural-index expansion** (Paper IV `p1_intro.tex` eq. (1.6), Theorem A(iii) integer layer;
E2_pgt1.md Remark E2.8 "index-shift form"): for all real `p, a, f`,
`(n/(n+a))^p (1 + f/(n+a)²) − (1 − pa/n + (p(p+1)/2·a² + f)/n²) = O(n⁻³)` as `n → ∞` (real `n`). -/
theorem natural_expansion (p a f : ℝ) :
    (fun n : ℝ => (n / (n + a)) ^ p * (1 + f / (n + a) ^ 2)
      - (1 - p * a / n + (p * (p + 1) / 2 * a ^ 2 + f) / n ^ 2)) =O[atTop] fun n => 1 / n ^ 3 := by
  have h := (natural_expansion_x p a f).comp_tendsto tendsto_inv_atTop_zero
  refine h.congr' ?_ ?_
  · filter_upwards [eventually_gt_atTop (0 : ℝ), eventually_gt_atTop (-a)] with n hn hna
    have hna' : 0 < n + a := by linarith
    have hx : 1 + a * n⁻¹ = (n / (n + a))⁻¹ := by field_simp
    have hq : 0 ≤ n / (n + a) := (div_pos hn hna').le
    simp only [Function.comp]
    rw [hx, Real.rpow_neg (inv_nonneg.2 hq), Real.inv_rpow hq, inv_inv]
    field_simp
  · exact Eventually.of_forall fun n => by simp [Function.comp, one_div]

/-- `α = (s − 1 − p)/p` (E2_pgt1.md §0; Paper IV §1). -/
noncomputable def alphaP (p s : ℝ) : ℝ := (s - 1 - p) / p

/-- The shift `a = α/2 + 1/2 = α/2 − ζ(0)` of the natural index (Paper IV `p1_intro.tex` eq. (1.6)). -/
noncomputable def natShift (p s : ℝ) : ℝ := alphaP p s / 2 + 1 / 2

/-- The natural index `N = n + α/2 + 1/2` (Paper IV `p1_intro.tex` eq. (1.6), `eq:N`). -/
noncomputable def natIndex (p s n : ℝ) : ℝ := n + natShift p s

/-- `f₂ = (p+1)/12 − (p+2)α²/8` (Paper IV `p1_intro.tex` Theorem A(iii)). -/
noncomputable def f2 (p s : ℝ) : ℝ := (p + 1) / 12 - (p + 2) * alphaP p s ^ 2 / 8

/-- `d₂(p, s)` of Thm E2.1 (E2_pgt1.md; THEOREMS.md row "Thm E2.1"; same closed form in E3.md Cor E3.3(i)). -/
noncomputable def d2 (p s : ℝ) : ℝ :=
  (p + 1) * (s - 1) ^ 2 / (8 * p) - (p + 2) * (s - 1 - p) ^ 2 / (8 * p ^ 2) + (p + 1) / 12

/-- `a = (α + 1)/2 = (s − 1)/(2p)` (Paper IV eq. (1.6); E2_pgt1.md Remark E2.8 shift `(s−1)/(2p)`). -/
theorem natShift_eq {p : ℝ} (hp : p ≠ 0) (s : ℝ) : natShift p s = (s - 1) / (2 * p) := by
  unfold natShift alphaP; field_simp; ring

/-- Coefficient identity (i): `−p·a = −(s−1)/2`, the `1/n` coefficient `d₁` of Thm E2.1 / E2_pgt1.md
(`d₁ = −p(α+1)/2 = −(s−1)/2`), i.e. the natural index absorbs the `1/n` term (Paper IV eq. (1.6)). -/
theorem neg_mul_natShift {p : ℝ} (hp : p ≠ 0) (s : ℝ) : -p * natShift p s = -(s - 1) / 2 := by
  rw [natShift_eq hp]; field_simp

/-- Coefficient identity (ii): `p(p+1)/2·a² + f₂ = d₂`, the `n⁻²` coefficient of `(n/(n+a))^p(1 + f₂/(n+a)²)`
equals `d₂` of Thm E2.1 (E2_pgt1.md; Paper IV Theorem A(iii) `f₂`); `p(p+1)/2·a²` is the `(s−1)²` part
(E2_pgt1.md Remark E2.8). -/
theorem natShift_sq_add_f2 {p : ℝ} (hp : p ≠ 0) (s : ℝ) :
    p * (p + 1) / 2 * natShift p s ^ 2 + f2 p s = d2 p s := by
  rw [natShift_eq hp]; unfold f2 d2 alphaP; field_simp; ring

/-- The second closed form of `d₂` in Thm E2.1 (E2_pgt1.md):
`d₂ = −[p³ + 7p² + 12p + 6 − 12(p+1)s + (6 − 3p²)s²]/(24p²)`. -/
theorem d2_closed {p : ℝ} (hp : p ≠ 0) (s : ℝ) :
    d2 p s = -(p ^ 3 + 7 * p ^ 2 + 12 * p + 6 - 12 * (p + 1) * s + (6 - 3 * p ^ 2) * s ^ 2)
      / (24 * p ^ 2) := by
  unfold d2; field_simp; ring

/-- Coefficient identity (iii): `d₂(2, s) = (s² + 6s − 11)/16` for every `s` (E2_pgt1.md Thm E2.1, p = 2;
Remark E2.9). -/
theorem d2_two (s : ℝ) : d2 2 s = (s ^ 2 + 6 * s - 11) / 16 := by
  unfold d2; ring

/-- `N⁻³ ~ n⁻³` for `N = n + a` (bookkeeping for Paper IV Theorem A's remainder in `N` vs E2.1's in `n`). -/
theorem inv_cube_shift_isEquivalent (a : ℝ) :
    (fun n : ℝ => 1 / (n + a) ^ 3) ~[atTop] fun n => 1 / n ^ 3 := by
  have h : (fun n : ℝ => n + a) ~[atTop] id :=
    (IsEquivalent.refl (u := (id : ℝ → ℝ))).add_isLittleO (isLittleO_const_id_atTop a)
  have h3 := (h.pow 3).inv
  simpa [one_div, Pi.inv_def, Pi.pow_def] using h3

/-- **Paper IV natural form ⇔ Thm E2.1 form** (Paper IV `p1_intro.tex` Theorem A(ii)–(iii) with eq. (1.6);
E2_pgt1.md Thm E2.1; THEOREMS.md rows "Thm E2.1" and "Thm E3.1, E3.2"). For `p > 0`, any real `s` and
any real sequence `y` (standing for `n^p b_n / c`):
`y_n = (n/N)^p (1 + f₂/N² ) + O(N⁻³)` with `N = n + α/2 + 1/2`  iff
`y_n = 1 − (s−1)/(2n) + d₂/n² + O(n⁻³)`.

Scope: the left side is the *integer layer* of Theorem A truncated at `N⁻²`; Theorem A also has zeta layers
`(n/N)^p ε_j N^{−1−jp}`, which are `O(N⁻³)` only for `p ≥ 2` (for `1 < p < 2` E3.1 carries `κ_p n^{−1−p}`
separately, and for `0 < p < 1` E3.2 carries `ε_j n^{−1−jp}`). Likewise E2.1's remainder is `O(n^{−min(3,1+p)})`,
which is `O(n⁻³)` exactly when `p ≥ 2`. So this is the exact statement for `p ≥ 2` (in particular `p = 2`) and,
for other `p`, the statement about the integer layer after the zeta layers are subtracted. No `s > 1`,
`p ≠ 1` hypothesis is needed for this algebraic-asymptotic step. -/
theorem naturalForm_iff_E21 {p : ℝ} (hp : 0 < p) (s : ℝ) (y : ℕ → ℝ) :
    ((fun n : ℕ => y n - ((n : ℝ) / natIndex p s n) ^ p * (1 + f2 p s / natIndex p s n ^ 2))
        =O[atTop] fun n : ℕ => 1 / natIndex p s n ^ 3)
      ↔ ((fun n : ℕ => y n - (1 - (s - 1) / (2 * n) + d2 p s / (n : ℝ) ^ 2))
        =O[atTop] fun n : ℕ => 1 / (n : ℝ) ^ 3) := by
  set a := natShift p s with ha
  have e1 : p * a = (s - 1) / 2 := by
    have := neg_mul_natShift hp.ne' s; rw [← ha] at this; linarith
  have e2 := natShift_sq_add_f2 hp.ne' s
  rw [← ha] at e2
  have hD : (fun n : ℕ => ((n : ℝ) / natIndex p s n) ^ p * (1 + f2 p s / natIndex p s n ^ 2)
      - (1 - (s - 1) / (2 * n) + d2 p s / (n : ℝ) ^ 2)) =O[atTop] fun n : ℕ => 1 / (n : ℝ) ^ 3 := by
    refine ((natural_expansion p a (f2 p s)).comp_tendsto tendsto_natCast_atTop_atTop).congr_left
      (fun n => ?_)
    simp only [Function.comp, natIndex, ← ha, e1, e2, div_div]
  have hE := (inv_cube_shift_isEquivalent a).comp_tendsto tendsto_natCast_atTop_atTop
  have h1 : (fun n : ℕ => 1 / natIndex p s n ^ 3) =O[atTop] fun n : ℕ => 1 / (n : ℝ) ^ 3 :=
    hE.isBigO
  have h2 : (fun n : ℕ => 1 / (n : ℝ) ^ 3) =O[atTop] fun n : ℕ => 1 / natIndex p s n ^ 3 :=
    hE.symm.isBigO
  constructor
  · intro h
    exact ((h.trans h1).add hD).congr_left (fun n => by ring)
  · intro h
    exact ((h.sub hD).trans h2).congr_left (fun n => by ring)

end JacobiAsym
