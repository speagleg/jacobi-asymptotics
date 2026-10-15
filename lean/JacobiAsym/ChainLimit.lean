import JacobiAsym.Basic

/-!
# Chain limit (Paper 2 §3, Lemma `lem:chain-limit`)

Pure real analysis on sequences. If `U, V > 0`, `U n + V n → 2c` and `U n · V (n+1) → c²` (`c > 0`), then
`U n → c` and `V n → c`. The limiting map `t ↦ 2c − c²/t` has the double fixed point `c` and `2c − c²/t ≤ t`
for `t > 0`; both `limsup U` and `liminf U` satisfy `K ≤ 2c − c²/K`, which forces `K = c`.

`chain_limit` is the form used in Paper 2 (scale `s_n`, e.g. `s_n = n^p`): `a_n = u_n + l_n`,
`b_n² = u_{n−1} l_n`, `s_n a_n → 2c`, `s_n √(b_n²) → c` ⇒ `s_n u_n → c`, `s_n l_n → c`.
-/

open Filter Topology

namespace JacobiAsym

theorem eventually_of_eventually_succ {P : ℕ → Prop} (h : ∀ᶠ n in atTop, P (n + 1)) :
    ∀ᶠ n in atTop, P n := by
  obtain ⟨N, hN⟩ := eventually_atTop.1 h
  refine eventually_atTop.2 ⟨N + 1, fun n hn => ?_⟩
  obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
  exact hN m (by omega)

theorem frequently_of_frequently_succ {P : ℕ → Prop} (h : ∃ᶠ n in atTop, P (n + 1)) :
    ∃ᶠ n in atTop, P n := by
  rw [frequently_atTop] at h ⊢
  intro a
  obtain ⟨b, hb, hP⟩ := h a
  exact ⟨b + 1, by omega, hP⟩

/-- One step of the chain recursion `U_{n+1} = (U_{n+1} + V_{n+1}) − U_n V_{n+1} / U_n`. -/
theorem chain_step {c ε K u u' v' : ℝ} (hu : 0 < u) (hε : ε < c ^ 2)
    (h1 : u < K + ε) (h2 : u' + v' < 2 * c + ε) (h3 : c ^ 2 - ε < u * v') :
    u' ≤ 2 * c + ε - (c ^ 2 - ε) / (K + ε) := by
  have hv : (c ^ 2 - ε) / u < v' := by rw [div_lt_iff₀ hu]; linarith
  have : (c ^ 2 - ε) / (K + ε) ≤ (c ^ 2 - ε) / u :=
    div_le_div_of_nonneg_left (by linarith) hu h1.le
  linarith

/-- The double fixed point: `K ≤ 2c − c²/K` (approximately) forces `K = c`. -/
theorem eq_of_le_chainMap {c K : ℝ} (hc : 0 < c) (hK : 0 < K)
    (h : ∀ ε, 0 < ε → ε < c ^ 2 → K ≤ 2 * c + ε - (c ^ 2 - ε) / (K + ε)) : K = c := by
  have hφ : Tendsto (fun ε : ℝ => 2 * c + ε - (c ^ 2 - ε) / (K + ε)) (𝓝[>] 0)
      (𝓝 (2 * c + 0 - (c ^ 2 - 0) / (K + 0))) := by
    apply Tendsto.mono_left _ nhdsWithin_le_nhds
    exact (tendsto_const_nhds.add tendsto_id).sub
      ((tendsto_const_nhds.sub tendsto_id).div (tendsto_const_nhds.add tendsto_id) (by simp; exact hK.ne'))
  have hc2 : (0 : ℝ) < c ^ 2 := by positivity
  have hle : K ≤ 2 * c + 0 - (c ^ 2 - 0) / (K + 0) := by
    apply ge_of_tendsto hφ
    filter_upwards [Ioo_mem_nhdsGT hc2] with ε hε
    exact h ε hε.1 hε.2
  simp only [add_zero, sub_zero] at hle
  have e : c ^ 2 / K * K = c ^ 2 := div_mul_cancel₀ _ hK.ne'
  have hsq : (K - c) ^ 2 = 0 := le_antisymm (by nlinarith) (sq_nonneg _)
  have := pow_eq_zero_iff (n := 2) (by norm_num) |>.1 hsq
  linarith

/-- **Chain limit, core form.** `U n > 0`, `V (n+1) > 0`, `U n + V n → 2c`, `U n · V (n+1) → c²` ⇒
`U → c`, `V → c`. -/
theorem chain_limit_core {c : ℝ} (hc : 0 < c) {U V : ℕ → ℝ} (hU : ∀ n, 0 < U n) (hV : ∀ n, 0 < V (n + 1))
    (hA : Tendsto (fun n => U n + V n) atTop (𝓝 (2 * c)))
    (hQ : Tendsto (fun n => U n * V (n + 1)) atTop (𝓝 (c ^ 2))) :
    Tendsto U atTop (𝓝 c) ∧ Tendsto V atTop (𝓝 c) := by
  have hc2 : (0 : ℝ) < c ^ 2 := by positivity
  have hA3 : ∀ᶠ n in atTop, U n + V n < 3 * c := hA.eventually (gt_mem_nhds (by linarith))
  have hQ2 : ∀ᶠ n in atTop, c ^ 2 / 2 < U n * V (n + 1) := hQ.eventually (lt_mem_nhds (by linarith))
  have hup : ∀ᶠ n in atTop, U n ≤ 3 * c := by
    filter_upwards [hA3, eventually_ge_atTop 1] with n h1 h2
    obtain ⟨m, rfl⟩ : ∃ m, n = m + 1 := ⟨n - 1, by omega⟩
    linarith [hV m]
  have hlow : ∀ᶠ n in atTop, c / 6 ≤ U n := by
    filter_upwards [hQ2, (tendsto_add_atTop_nat 1).eventually hA3] with n h1 h2
    have hv : V (n + 1) < 3 * c := by linarith [hU (n + 1)]
    have := mul_lt_mul_of_pos_left hv (hU n)
    nlinarith
  have hb1 : IsBoundedUnder (· ≤ ·) atTop U := isBoundedUnder_of_eventually_le hup
  have hb2 : IsBoundedUnder (· ≥ ·) atTop U := isBoundedUnder_of_eventually_ge hlow
  set M := limsup U atTop with hM
  set L := liminf U atTop with hL
  have hLlow : c / 6 ≤ L := le_liminf_of_le hb1.isCoboundedUnder_ge hlow
  have hLM : L ≤ M := liminf_le_limsup hb1 hb2
  -- eventual input bounds at level ε
  have hin : ∀ ε, 0 < ε → ∀ᶠ n in atTop, U (n + 1) + V (n + 1) < 2 * c + ε ∧ c ^ 2 - ε < U n * V (n + 1) :=
    fun ε hε => ((tendsto_add_atTop_nat 1).eventually (hA.eventually (gt_mem_nhds (by linarith)))).and
      (hQ.eventually (lt_mem_nhds (by linarith)))
  have hMc : M = c := by
    apply eq_of_le_chainMap hc (by linarith)
    intro ε hε hεc
    apply limsup_le_of_le hb2.isCoboundedUnder_le
    apply eventually_of_eventually_succ
    filter_upwards [eventually_lt_of_limsup_lt (lt_add_of_pos_right M hε) hb1, hin ε hε] with n h1 h2
    exact chain_step (hU n) hεc h1 h2.1 h2.2
  have hLc : L = c := by
    apply eq_of_le_chainMap hc (by linarith)
    intro ε hε hεc
    apply liminf_le_of_frequently_le _ hb2
    apply frequently_of_frequently_succ
    have hf := frequently_lt_of_liminf_lt hb1.isCoboundedUnder_ge (lt_add_of_pos_right L hε)
    refine (hf.and_eventually (hin ε hε)).mono ?_
    rintro n ⟨h1, h2⟩
    exact chain_step (hU n) hεc h1 h2.1 h2.2
  have hUt : Tendsto U atTop (𝓝 c) := tendsto_of_liminf_eq_limsup hLc hMc hb1 hb2
  refine ⟨hUt, ?_⟩
  have h2 := hA.sub hUt
  rw [show 2 * c - c = c by ring] at h2
  simpa using h2

/-- **Chain limit** (Paper 2 §3, Lemma `lem:chain-limit`, scale `s_n`). With `s_n > 0`, `s_n / s_{n+1} → 1`,
`u_n > 0`, `l_n > 0` (`n ≥ 1`), `a_n = u_n + l_n` and `b_n² = u_{n−1} l_n` (`n ≥ 1`):
if `s_n a_n → 2c` and `s_n √(b_n²) → c` (`c > 0`), then `s_n u_n → c` and `s_n l_n → c`. -/
theorem chain_limit {c : ℝ} (hc : 0 < c) {s u l a b2 : ℕ → ℝ} (hs : ∀ n, 0 < s n)
    (hs1 : Tendsto (fun n => s n / s (n + 1)) atTop (𝓝 1))
    (hu : ∀ n, 0 < u n) (hl : ∀ n, 0 < l (n + 1))
    (ha : ∀ n, a (n + 1) = u (n + 1) + l (n + 1)) (hb : ∀ n, b2 (n + 1) = u n * l (n + 1))
    (hA : Tendsto (fun n => s n * a n) atTop (𝓝 (2 * c)))
    (hB : Tendsto (fun n => s n * Real.sqrt (b2 n)) atTop (𝓝 c)) :
    Tendsto (fun n => s n * u n) atTop (𝓝 c) ∧ Tendsto (fun n => s n * l n) atTop (𝓝 c) := by
  apply chain_limit_core hc (fun n => mul_pos (hs n) (hu n)) (fun n => mul_pos (hs _) (hl n))
  · apply (tendsto_add_atTop_iff_nat 1).1
    refine hA.comp (tendsto_add_atTop_nat 1) |>.congr fun n => ?_
    simp only [Function.comp, ha]; ring
  · have hB1 := (hB.comp (tendsto_add_atTop_nat 1)).pow 2
    have := hs1.mul hB1
    rw [one_mul] at this
    refine this.congr fun n => ?_
    simp only [Function.comp]
    have hb0 : 0 ≤ b2 (n + 1) := by rw [hb]; exact (mul_pos (hu n) (hl n)).le
    rw [mul_pow, Real.sq_sqrt hb0, hb]
    field_simp [(hs (n + 1)).ne']

end JacobiAsym
