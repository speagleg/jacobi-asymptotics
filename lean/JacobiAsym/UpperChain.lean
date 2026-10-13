import JacobiAsym.PairBounds
import JacobiAsym.Inputs

open Finset

namespace JacobiAsym

/-- The m-th term of item 11 Lemma H7 (head `N = n - m` points, tail `m` points), with `X = (Mn)^{-p}`. -/
noncomputable def upperTerm (p s0 c2 W : ℝ) (U : ℝ → ℝ) (Mn n m : ℕ) : ℝ :=
  ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U Mn) ^ (n - m) *
    heineD (powSeq p) (powSeq s0) (n - m) * W ^ m * ((Mn : ℝ) ^ (-p)) ^ (m * (m - 1))

/-- `slowAtom` is antitone on `[1, ∞)`. -/
theorem SlowFactor.slowAtom_anti {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0)
    {u v : ℝ} (hu : 1 ≤ u) (huv : u < v) : slowAtom p L v ≤ slowAtom p L u := by
  obtain ⟨ρm, hρm0, _, hρm⟩ := h.exists_rhoMin
  have hlow := h.lower_pair hρm hu huv
  have hp := h.p_pos
  have hg : 0 ≤ u ^ (-p) - v ^ (-p) :=
    sub_nonneg.2 (Real.rpow_le_rpow_of_nonpos (by linarith) huv.le (by linarith))
  have hlo : 0 ≤ (if u < a0 then ρm else (1 - E u / p) * L u) := by
    split_ifs with hlt
    · exact hρm0.le
    · have ha0u : (a0 : ℝ) ≤ u := not_lt.1 hlt
      have : E u ≤ E a0 := h.E_anti ha0u
      have : E u / p < 1 := by rw [div_lt_one hp]; linarith [h.E_a0]
      exact mul_nonneg (by linarith) (h.L_pos u hu).le
  nlinarith [mul_nonneg hlo hg]

section Cut
variable {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ}

theorem cutAtom_head {K0 k : ℕ} (hk : k < K0) : cutAtom p L K0 k = powSeq p k := by
  simp [cutAtom, powSeq, hk]

theorem cutAtom_tail {K0 k : ℕ} (hk : K0 ≤ k) : cutAtom p L K0 k = slowAtom p L ((k : ℝ) + 1) / L K0 := by
  simp [cutAtom, not_lt.2 hk]

theorem SlowFactor.cutAtom_pos (h : SlowFactor p L L' E a0) {K0 : ℕ} (hK0 : 1 ≤ K0) (k : ℕ) :
    0 < cutAtom p L K0 k := by
  have hK0r : (1 : ℝ) ≤ K0 := by exact_mod_cast hK0
  unfold cutAtom
  split_ifs
  · exact Real.rpow_pos_of_pos (by positivity) _
  · unfold slowAtom
    exact div_pos (mul_pos (Real.rpow_pos_of_pos (by positivity) _) (h.L_pos _ (by
      have : (0 : ℝ) ≤ k := Nat.cast_nonneg k
      linarith))) (h.L_pos _ hK0r)

/-- `f(K0) / L(K0) = K0^{-p}`. -/
theorem SlowFactor.slowAtom_div_L (h : SlowFactor p L L' E a0) {K0 : ℕ} (hK0 : 1 ≤ K0) :
    slowAtom p L K0 / L K0 = (K0 : ℝ) ^ (-p) := by
  have hK0r : (1 : ℝ) ≤ K0 := by exact_mod_cast hK0
  unfold slowAtom
  field_simp [(h.L_pos _ hK0r).ne']

theorem SlowFactor.cutAtom_tail_le (h : SlowFactor p L L' E a0) {K0 : ℕ} (hK0 : 1 ≤ K0) {k : ℕ}
    (hk : K0 ≤ k) : cutAtom p L K0 k ≤ (K0 : ℝ) ^ (-p) := by
  have hK0r : (1 : ℝ) ≤ K0 := by exact_mod_cast hK0
  rw [cutAtom_tail hk, ← h.slowAtom_div_L hK0]
  apply div_le_div_of_nonneg_right _ (h.L_pos _ hK0r).le
  apply h.slowAtom_anti hK0r
  have : (K0 : ℝ) ≤ k := by exact_mod_cast hk
  linarith

theorem cutAtom_head_ge (hp : 0 < p) {K0 k : ℕ} (hk : k < K0) : (K0 : ℝ) ^ (-p) ≤ cutAtom p L K0 k := by
  rw [cutAtom_head hk, powSeq]
  apply Real.rpow_le_rpow_of_nonpos (by positivity) _ (by linarith)
  have : (k : ℝ) + 1 ≤ K0 := by exact_mod_cast hk
  exact this

/-- Pair bound of item 11's H_L upper bound for the cut atoms (all three cases). -/
theorem SlowFactor.cut_pair_bound (h : SlowFactor p L L' E a0) {B : ℝ} (hB1 : 1 ≤ B)
    (hB : ∀ a c T : ℝ, 1 ≤ a → a < c → c ≤ T → (a0 : ℝ) ≤ T →
      slowAtom p L a - slowAtom p L c ≤ (if a < a0 then B else 1) * L T * (a ^ (-p) - c ^ (-p)))
    {K0 : ℕ} (hK0 : a0 ≤ K0) {a b : ℕ} (hab : a < b) :
    (slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1)) ^ 2 ≤
      (if a < a0 then B else 1) ^ 2 * L K0 ^ 2 * (cutAtom p L K0 a - cutAtom p L K0 b) ^ 2 := by
  have hp := h.p_pos
  have hK01 : 1 ≤ K0 := h.a0_pos.trans hK0
  have hK0r : (1 : ℝ) ≤ K0 := by exact_mod_cast hK01
  have ha0K : (a0 : ℝ) ≤ K0 := by exact_mod_cast hK0
  have hLK : 0 < L K0 := h.L_pos _ hK0r
  have har : (1 : ℝ) ≤ (a : ℝ) + 1 := by have := Nat.cast_nonneg (α := ℝ) a; linarith
  have habr : (a : ℝ) + 1 < (b : ℝ) + 1 := by
    have : (a : ℝ) < b := by exact_mod_cast hab
    linarith
  set c : ℝ := if a < a0 then B else 1 with hc
  have hc1 : 1 ≤ c := by simp only [hc]; split_ifs <;> linarith
  -- unsquared bound
  have hnn : 0 ≤ slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1) :=
    sub_nonneg.2 (h.slowAtom_anti har habr)
  -- the `if` at a+1 is ≤ c
  have hite : ∀ (z : ℝ), 0 ≤ z → (if (a : ℝ) + 1 < a0 then B else 1) * z ≤ c * z := by
    intro z hz
    apply mul_le_mul_of_nonneg_right _ hz
    simp only [hc]
    split_ifs with h1 h2 h2
    · exact le_rfl
    · exfalso; apply h2; exact_mod_cast (by linarith : (a : ℝ) < a0)
    · exact hB1
    · exact le_rfl
  have hle : slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1) ≤
      c * L K0 * (cutAtom p L K0 a - cutAtom p L K0 b) := by
    rcases lt_or_ge b K0 with hbK | hbK
    · -- both in the head
      have hbr : (b : ℝ) + 1 ≤ K0 := by exact_mod_cast hbK
      have h1 := hB _ _ K0 har habr hbr ha0K
      rw [cutAtom_head (hab.trans hbK), cutAtom_head hbK, powSeq, powSeq]
      have hg : 0 ≤ ((a : ℝ) + 1) ^ (-p) - ((b : ℝ) + 1) ^ (-p) :=
        sub_nonneg.2 (Real.rpow_le_rpow_of_nonpos (by linarith) habr.le (by linarith))
      calc _ ≤ _ := h1
        _ = (if (a : ℝ) + 1 < a0 then B else 1) * (L K0 * (((a : ℝ) + 1) ^ (-p) - ((b : ℝ) + 1) ^ (-p))) := by ring
        _ ≤ c * (L K0 * (((a : ℝ) + 1) ^ (-p) - ((b : ℝ) + 1) ^ (-p))) := hite _ (mul_nonneg hLK.le hg)
        _ = _ := by ring
    · rcases lt_or_ge a K0 with haK | haK
      · -- mixed: split at the real point K0
        have hGb := h.cutAtom_tail_le hK01 hbK
        have htail : slowAtom p L K0 - slowAtom p L ((b : ℝ) + 1) =
            L K0 * ((K0 : ℝ) ^ (-p) - cutAtom p L K0 b) := by
          rw [cutAtom_tail hbK, ← h.slowAtom_div_L hK01]; field_simp
        have hG : 0 ≤ (K0 : ℝ) ^ (-p) - cutAtom p L K0 b := sub_nonneg.2 hGb
        have hhead : slowAtom p L ((a : ℝ) + 1) - slowAtom p L K0 ≤
            c * L K0 * (((a : ℝ) + 1) ^ (-p) - (K0 : ℝ) ^ (-p)) := by
          have haK' : (a : ℝ) + 1 ≤ K0 := by exact_mod_cast haK
          rcases eq_or_lt_of_le haK' with heq | hlt
          · rw [heq]; simp
          · have h1 := hB _ _ K0 har hlt le_rfl ha0K
            have hg : 0 ≤ ((a : ℝ) + 1) ^ (-p) - (K0 : ℝ) ^ (-p) :=
              sub_nonneg.2 (Real.rpow_le_rpow_of_nonpos (by linarith) hlt.le (by linarith))
            calc _ ≤ _ := h1
              _ = (if (a : ℝ) + 1 < a0 then B else 1) * (L K0 * (((a : ℝ) + 1) ^ (-p) - (K0 : ℝ) ^ (-p))) := by ring
              _ ≤ c * (L K0 * (((a : ℝ) + 1) ^ (-p) - (K0 : ℝ) ^ (-p))) := hite _ (mul_nonneg hLK.le hg)
              _ = _ := by ring
        rw [cutAtom_head haK, powSeq]
        calc slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1)
            = (slowAtom p L ((a : ℝ) + 1) - slowAtom p L K0) + (slowAtom p L K0 - slowAtom p L ((b : ℝ) + 1)) := by ring
          _ ≤ c * L K0 * (((a : ℝ) + 1) ^ (-p) - (K0 : ℝ) ^ (-p)) + c * L K0 * ((K0 : ℝ) ^ (-p) - cutAtom p L K0 b) := by
              rw [htail]
              gcongr
              nlinarith [mul_nonneg hLK.le hG]
          _ = _ := by ring
      · -- both in the tail: exact
        rw [cutAtom_tail haK, cutAtom_tail hbK]
        have : slowAtom p L ((a : ℝ) + 1) - slowAtom p L ((b : ℝ) + 1) =
            L K0 * (slowAtom p L ((a : ℝ) + 1) / L K0 - slowAtom p L ((b : ℝ) + 1) / L K0) := by
          field_simp
        rw [this]
        have hd : 0 ≤ slowAtom p L ((a : ℝ) + 1) / L K0 - slowAtom p L ((b : ℝ) + 1) / L K0 := by
          rw [← sub_div]; exact div_nonneg hnn hLK.le
        nlinarith [mul_nonneg hLK.le hd]
  have hsq := pow_le_pow_left₀ hnn hle 2
  calc _ ≤ (c * L K0 * (cutAtom p L K0 a - cutAtom p L K0 b)) ^ 2 := hsq
    _ = _ := by ring

end Cut

/-- `U K0 > 0` follows from `w > 0` and the weight upper bound. -/
theorem U_pos_of_w {s0 c2 : ℝ} {U : ℝ → ℝ} {w : ℕ → ℝ} (hc2 : 0 < c2) (hw0 : ∀ k, 0 < w k)
    (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1)) {K0 : ℕ} (hK0 : 1 ≤ K0) : 0 < U K0 := by
  have h1 := (hw0 (K0 - 1)).trans_le (hwhi (K0 - 1))
  have hcast : ((K0 - 1 : ℕ) : ℝ) + 1 = K0 := by
    rw [Nat.cast_sub hK0]; push_cast; ring
  rw [hcast] at h1
  have hps : 0 < c2 * powSeq s0 (K0 - 1) := mul_pos hc2 (Real.rpow_pos_of_pos (by positivity) _)
  exact pos_of_mul_pos_right h1 hps.le

/-- Head factor of Lemma H7: on `SH ⊆ range K0`, `|SH| = N`. -/
theorem head_term_bound {p s0 c2 : ℝ} {L U : ℝ → ℝ} {w : ℕ → ℝ} (hp : 0 < p) (hc2 : 0 < c2)
    (hw0 : ∀ k, 0 < w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1)) (hUmono : Monotone U)
    {K0 N m : ℕ} (hK0 : 1 ≤ K0) {SH : Finset ℕ} (hSH : SH ∈ (range K0).powersetCard N) :
    heineTerm (cutAtom p L K0) w SH * ∏ a ∈ SH, cutAtom p L K0 a ^ (2 * m) ≤
      (N.factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U K0) ^ N * heineTerm (powSeq p) (powSeq s0) SH := by
  obtain ⟨hsub, hcard⟩ := mem_powersetCard.1 hSH
  have hin : ∀ a ∈ SH, a < K0 := fun a ha => mem_range.1 (hsub ha)
  -- U K0 > 0 (from w > 0)
  have hUK : 0 < U K0 := by
    have h1 := (hw0 (K0 - 1)).trans_le (hwhi (K0 - 1))
    have hcast : ((K0 - 1 : ℕ) : ℝ) + 1 = K0 := by
      rw [Nat.cast_sub hK0]; push_cast; ring
    rw [hcast] at h1
    have hps : 0 < c2 * powSeq s0 (K0 - 1) := mul_pos hc2 (Real.rpow_pos_of_pos (by positivity) _)
    exact pos_of_mul_pos_right h1 hps.le
  -- (ii) head atoms are pure powers
  have hT : heineTerm (cutAtom p L K0) w SH = heineTerm (powSeq p) w SH := by
    unfold heineTerm; congr 1
    apply prod_congr rfl; intro q hq
    simp only [pairs, mem_filter, mem_product] at hq
    rw [cutAtom_head (hin _ hq.1.1), cutAtom_head (hin _ hq.1.2)]
  -- (i) the product of powers
  have hP : ∏ a ∈ SH, cutAtom p L K0 a ^ (2 * m) ≤ (N.factorial : ℝ) ^ (-(2 * p * m)) := by
    have e : ∏ a ∈ SH, cutAtom p L K0 a ^ (2 * m) = (∏ a ∈ SH, ((a : ℝ) + 1)) ^ (-(2 * p * m)) := by
      rw [← Real.finsetProd_rpow _ _ (fun a _ => by positivity)]
      apply prod_congr rfl; intro a ha
      rw [cutAtom_head (hin a ha), powSeq, ← Real.rpow_natCast, ← Real.rpow_mul (by positivity)]
      congr 1; push_cast; ring
    rw [e]
    have hf := factorial_le_prod_succ SH
    rw [hcard] at hf
    exact Real.rpow_le_rpow_of_nonpos (by exact_mod_cast Nat.factorial_pos N) hf
      (by have : (0 : ℝ) ≤ m := Nat.cast_nonneg m; nlinarith)
  -- (iii) weights
  have hW : heineTerm (powSeq p) w SH ≤ (c2 * U K0) ^ N * heineTerm (powSeq p) (powSeq s0) SH := by
    unfold heineTerm
    have hprod : ∏ i ∈ SH, w i ≤ ∏ i ∈ SH, (c2 * U K0 * powSeq s0 i) := by
      apply prod_le_prod₀ (fun i _ => (hw0 i).le)
      intro i hi
      have hU : U ((i : ℝ) + 1) ≤ U K0 := hUmono (by exact_mod_cast hin i hi)
      have hps : 0 ≤ c2 * powSeq s0 i := mul_nonneg hc2.le (Real.rpow_pos_of_pos (by positivity) _).le
      calc w i ≤ c2 * powSeq s0 i * U ((i : ℝ) + 1) := hwhi i
        _ ≤ c2 * powSeq s0 i * U K0 := mul_le_mul_of_nonneg_left hU hps
        _ = c2 * U K0 * powSeq s0 i := by ring
    rw [prod_mul_distrib, prod_const, hcard] at hprod
    have hpairs : 0 ≤ ∏ q ∈ pairs SH, (powSeq p q.1 - powSeq p q.2) ^ 2 := prod_nonneg fun _ _ => sq_nonneg _
    calc (∏ i ∈ SH, w i) * ∏ q ∈ pairs SH, (powSeq p q.1 - powSeq p q.2) ^ 2
        ≤ ((c2 * U K0) ^ N * ∏ i ∈ SH, powSeq s0 i) * ∏ q ∈ pairs SH, (powSeq p q.1 - powSeq p q.2) ^ 2 :=
          mul_le_mul_of_nonneg_right hprod hpairs
      _ = _ := by ring
  rw [hT]
  have h0 : 0 ≤ heineTerm (powSeq p) w SH := heineTerm_nonneg (fun i => (hw0 i).le) SH
  have hPnn : 0 ≤ ∏ a ∈ SH, cutAtom p L K0 a ^ (2 * m) := by
    apply prod_nonneg; intro a ha; rw [cutAtom_head (hin a ha), powSeq]; positivity
  calc heineTerm (powSeq p) w SH * ∏ a ∈ SH, cutAtom p L K0 a ^ (2 * m)
      ≤ ((c2 * U K0) ^ N * heineTerm (powSeq p) (powSeq s0) SH) * (N.factorial : ℝ) ^ (-(2 * p * m)) :=
        mul_le_mul hW hP hPnn (le_trans h0 hW)
    _ = _ := by ring

/-- Per-(n, M, K) upper bound: `heineK f ≤ B^(2 a0 n) L(Mn)^(n(n-1)) ∑_m upperTerm`. -/
theorem heineK_slow_le {p κ s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    {B : ℝ} (hB1 : 1 ≤ B)
    (hB : ∀ a c T : ℝ, 1 ≤ a → a < c → c ≤ T → (a0 : ℝ) ≤ T →
      slowAtom p L a - slowAtom p L c ≤ (if a < a0 then B else 1) * L T * (a ^ (-p) - c ^ (-p)))
    (hHup : TheoremHPure p κ s0) (hc2 : 0 < c2)
    (hw0 : ∀ k, 0 < w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1)) (hUmono : Monotone U)
    (hwsum : Summable w) {M n : ℕ} (hMn : a0 ≤ M * n) (K : ℕ) :
    heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w K n ≤
      B ^ (2 * a0 * n) * L (M * n) ^ (n * (n - 1)) *
        ∑ m ∈ range (n + 1), upperTerm p s0 c2 (∑' k, w k) U (M * n) n m := by
  have hp := hL.p_pos
  have hK01 : 1 ≤ M * n := hL.a0_pos.trans hMn
  have hw : ∀ i, 0 ≤ w i := fun i => (hw0 i).le
  have hUK : 0 < U ((M * n : ℕ) : ℝ) := U_pos_of_w hc2 hw0 hwhi hK01
  have hLK : 0 < L ((M * n : ℕ) : ℝ) := hL.L_pos _ (by exact_mod_cast hK01)
  -- step 0: enlarge K
  have h0 : heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w K n ≤
      heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w (max K (M * n)) n :=
    heineK_mono_K hw (le_max_left _ _) n
  -- step 1: split pair comparison
  have h1 : heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w (max K (M * n)) n ≤
      B ^ (2 * a0 * n) * L ((M * n : ℕ) : ℝ) ^ (n * (n - 1)) * heineK (cutAtom p L (M * n)) w (max K (M * n)) n := by
    unfold heineK; rw [mul_sum]
    apply sum_le_sum; intro S hS
    have hcard := (mem_powersetCard.1 hS).2
    have := heineTerm_le_of_pair_le_split (x := fun k => slowAtom p L ((k : ℝ) + 1))
      (y := cutAtom p L (M * n)) (w := w) (lam := L ((M * n : ℕ) : ℝ)) hw hB1 (a0 := a0) (S := S)
      (fun a _ b _ hab => hL.cut_pair_bound hB1 hB hMn hab)
    rwa [hcard] at this
  -- step 2: tail split
  have h2 := heineK_tail_split (y := cutAtom p L (M * n)) (w := w) hw
    (le_max_right K (M * n)) (n := n) (X := ((M * n : ℕ) : ℝ) ^ (-p))
    (hL.cutAtom_pos hK01) (fun b hb => hL.cutAtom_tail_le hK01 hb)
    (fun a b ha hb => (hL.cutAtom_tail_le hK01 hb).trans (cutAtom_head_ge hp ha))
  -- step 3: termwise in m
  have h3 : ∀ m ∈ range (n + 1),
      (∑ SH ∈ (range (M * n)).powersetCard (n - m),
          heineTerm (cutAtom p L (M * n)) w SH * ∏ a ∈ SH, cutAtom p L (M * n) a ^ (2 * m)) *
        (∑ b ∈ Ico (M * n) (max K (M * n)), w b) ^ m * (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) ≤
      upperTerm p s0 c2 (∑' k, w k) U (M * n) n m := by
    intro m _
    have hX : 0 ≤ (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) :=
      pow_nonneg (Real.rpow_pos_of_pos (by positivity) _).le _
    have hcoef : 0 ≤ ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U ((M * n : ℕ) : ℝ)) ^ (n - m) :=
      mul_nonneg (Real.rpow_pos_of_pos (by exact_mod_cast Nat.factorial_pos _) _).le
        (pow_nonneg (mul_pos hc2 hUK).le _)
    have hhead : ∑ SH ∈ (range (M * n)).powersetCard (n - m),
          heineTerm (cutAtom p L (M * n)) w SH * ∏ a ∈ SH, cutAtom p L (M * n) a ^ (2 * m) ≤
        ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U ((M * n : ℕ) : ℝ)) ^ (n - m) *
          heineD (powSeq p) (powSeq s0) (n - m) := by
      calc _ ≤ ∑ SH ∈ (range (M * n)).powersetCard (n - m),
            ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U ((M * n : ℕ) : ℝ)) ^ (n - m) *
              heineTerm (powSeq p) (powSeq s0) SH :=
            sum_le_sum fun SH hSH => head_term_bound hp hc2 hw0 hwhi hUmono hK01 hSH
        _ = ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U ((M * n : ℕ) : ℝ)) ^ (n - m) *
              heineK (powSeq p) (powSeq s0) (M * n) (n - m) := by rw [heineK, mul_sum]
        _ ≤ _ := mul_le_mul_of_nonneg_left (heineK_le_heineD (hHup.bdd _) _) hcoef
    have htail : (∑ b ∈ Ico (M * n) (max K (M * n)), w b) ^ m ≤ (∑' k, w k) ^ m :=
      pow_le_pow_left₀ (sum_nonneg fun b _ => hw b) (Summable.sum_le_tsum _ (fun b _ => hw b) hwsum) m
    have hh0 : 0 ≤ ∑ SH ∈ (range (M * n)).powersetCard (n - m),
        heineTerm (cutAtom p L (M * n)) w SH * ∏ a ∈ SH, cutAtom p L (M * n) a ^ (2 * m) :=
      sum_nonneg fun SH _ => mul_nonneg (heineTerm_nonneg hw SH)
        (prod_nonneg fun a _ => pow_nonneg (hL.cutAtom_pos hK01 a).le _)
    unfold upperTerm
    calc _ ≤ (((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U ((M * n : ℕ) : ℝ)) ^ (n - m) *
            heineD (powSeq p) (powSeq s0) (n - m)) * (∑' k, w k) ^ m *
            (((M * n : ℕ) : ℝ) ^ (-p)) ^ (m * (m - 1)) := by
          apply mul_le_mul_of_nonneg_right _ hX
          exact mul_le_mul hhead htail (pow_nonneg (sum_nonneg fun b _ => hw b) _) (hh0.trans hhead)
      _ = _ := by ring
  have hBL : 0 ≤ B ^ (2 * a0 * n) * L ((M * n : ℕ) : ℝ) ^ (n * (n - 1)) :=
    mul_nonneg (pow_nonneg (by linarith) _) (pow_nonneg hLK.le _)
  have hcast : ((M * n : ℕ) : ℝ) = (M : ℝ) * n := by push_cast; ring
  calc heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w K n
      ≤ B ^ (2 * a0 * n) * L ((M * n : ℕ) : ℝ) ^ (n * (n - 1)) *
          heineK (cutAtom p L (M * n)) w (max K (M * n)) n := h0.trans h1
    _ ≤ B ^ (2 * a0 * n) * L ((M * n : ℕ) : ℝ) ^ (n * (n - 1)) *
          ∑ m ∈ range (n + 1), upperTerm p s0 c2 (∑' k, w k) U (M * n) n m :=
        mul_le_mul_of_nonneg_left (h2.trans (sum_le_sum h3)) hBL
    _ = _ := by rw [hcast]

theorem slow_bdd {p κ s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    (hHup : TheoremHPure p κ s0) (hc2 : 0 < c2)
    (hw0 : ∀ k, 0 < w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1)) (hUmono : Monotone U)
    (hwsum : Summable w) (n : ℕ) :
    BddAbove (Set.range fun K => heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w K n) := by
  rcases Nat.eq_zero_or_pos n with rfl | hn
  · exact ⟨1, by rintro _ ⟨K, rfl⟩; simp [heineK_zero_card]⟩
  obtain ⟨B, hB1, hB⟩ := hL.upper_pair
  have hMn : a0 ≤ a0 * n := Nat.le_mul_of_pos_right a0 hn
  exact ⟨_, by rintro _ ⟨K, rfl⟩; exact heineK_slow_le hL hB1 hB hHup hc2 hw0 hwhi hUmono hwsum hMn K⟩

end JacobiAsym
