# Plan 3: Lean assembly of Theorem H_L and Lemma P

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prove in Lean, with no `sorry`, item 11's **Theorem H_L** (the averaged law for atoms k^{-p}L(k)) from
**Theorem H for pure powers**, which enters as a named input structure. Also prove **Lemma P**. The main result is
`theoremHL`.

**Architecture:**
- **D_n.** D_n of the infinite measure is `heineD x w n := ⨆ K, heineK x w K n`, the supremum of the Plan 2 finite
  Heine sums.
- **Named input.** Theorem H for atoms (k+1)^{-p} and weights (k+1)^{-s} is the structure `TheoremHPure p κ s`:
  boundedness in K and `log D_n = −p n² log n + κ n² + o(n²)`. It is proved in item 11 through the Lommel and
  Tricomi–Carlitz families and is not formalized here.
- **The slowly varying factor L.** Its hypotheses are bundled as `SlowFactor p L L' E a0`. This is the formal
  counterpart of item 11 (L1)–(L3), with E an antitone majorant of |ξL′/L|.
- **The proof.** It follows item 11 `PROOF.md` §7b exactly:
  - *Lower bound:* rank-dependent pair comparison with a monotone ρ (Plan 2 `heineTerm_ge_of_pair_ge`).
  - *Upper bound:* cut at K0 = Mn and rescale the tail (`cutAtom`), using the split pair comparison (Plan 2
    `heineTerm_le_of_pair_le_split`), the tail split (`heineK_tail_split`), N! ≤ Π(a+1), the uniform form of
    Theorem H, the exact exponent identity, and `phi_bound`.
  - *Limits:* M → ∞ after n → ∞.

**Tech Stack:** Lean 4.34.1, Mathlib v4.34.1, and the JacobiAsym library from Plan 2 (merged at `44af48e`).

**Spec:** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` §6, which carries a scope-update note.
Mathematical source: math-pursuits item 11 `work/proof/PROOF.md` §7b and §4 (Lemma P).

**Scope ruling.** The Toeplitz eigenvalue count (Theorem B's Toeplitz part) is moved out of Plan 3, because Mathlib
has no spectral theory of tridiagonal Toeplitz matrices. It joins the later bridge plan, alongside Andreief/H2. The
smooth-ζ corollary (Lambert-W facts) is also later: it is an instance of `SlowFactor`, and checking that instance is
separate work. Task 10 records both in spec §6.

**TDD in Lean** works as in Plan 2. RED is the statement with `sorry` elaborating, plus `check.sh` failing. GREEN is
no warnings plus `AUDIT OK`. Every statement below was typechecked against the merged library on 2026-10-13 and
checked by hand for truth. Notes:
- `exponent_identity` holds at m = n as well, because both sides use `Real.log 0 = 0`.
- Every constant (ρ₋, B, inf L) is derivable from `SlowFactor` by compactness on [1, a0].

## Global Constraints

- Lean 4.34.1 and Mathlib v4.34.1. Never run `lake update`. The shared cache `/root/.cache/math-pursuits-lake` is
  read-only.
- No `sorry`, `admit` or new `axiom`. Axioms are limited to propext, Classical.choice and Quot.sound. `lean/check.sh`
  must print `AUDIT OK`.
- Every new top-level theorem gets a `#print axioms` line in `lean/Audit.lean`. Headline theorems also go in the
  `need` list in `check.sh`.
- Commit prefix `lean:`. Each commit ends with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Branch `plan-3-lean-hl` from `master`.
- Indexing: atom index k : ℕ ↔ item-11 atom k+1. The atom function is `slowAtom p L t = t^(-p) * L t`, evaluated at
  t = k+1. Theorem H_L's main term uses `Real.log (L n)` at the *unshifted* n. The shift is absorbed by slow
  variation, so handle it explicitly (Review Focus #2).
- The lemma names follow Plan 2's actual names (`prod_le_prod₀`, `heineTerm_le_of_pair_le_split`, and so on).

## Review Focus

1. **Real `iSup` junk values.** `heineD` is a real `⨆`. Without `BddAbove` it is 0, and `log 0 = 0`. Every use of
   `le_ciSup` or `ciSup_le` must carry its `BddAbove`. In particular, `theoremHL` must not be *vacuously* about
   junk: Task 4 proves `BddAbove` for the f-measure.
2. **Index shifts.** Lower-bound ranks are 0-based (ρ i at index i ↔ atom i+1). The main term uses log L(n), while
   the sums naturally give log L(i+1). Each shift is an o(n²) correction that must be proved, not assumed.
3. **Uniformity in m (0 ≤ m ≤ n).** Every error term in the upper bound must be bounded independently of m before
   taking the max over m (`log (n+1)` for the sum).
4. **The order of limits.** Fix M and η, then take n → ∞, then let M → ∞ and η → 0. The final ε-argument must pick
   M with A²/(4p log M) < ε/3 *before* choosing N.
5. **Weight hypotheses on the head only.** Use `w k ≤ c2 (k+1)^{-s0} U(k+1)` only for k < Mn, and bound
   U(k+1) ≤ U(Mn) there. `heineK_mono_w` needs pointwise ≤ on all of ℕ, so use a piecewise w′ (equal to w off the
   head) or restrict the sum first (Plan 2 deferred note).

---

### Task 1: `Inputs.lean`: D_n, pure powers, the named input, and basic facts

**Files:**
- Create: `lean/JacobiAsym/Inputs.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh` (`need` list)

**Interfaces:**
- Produces:
  - Definitions `heineD`, `powSeq`, `hnorm`; structure `TheoremHPure`.
  - Theorems `heineK_zero_card`, `heineK_pos`, `heineK_le_heineD`, `heineD_le`, `heineD_pos`,
    `TheoremHPure.uniform_upper`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.TailCut

open Finset Filter Topology

namespace JacobiAsym

/-- `D_n` of the infinite measure `∑_k w k δ_{x k}`: supremum of the truncated Heine sums (meaningful only
under `BddAbove`; otherwise Lean's junk value 0). -/
noncomputable def heineD (x w : ℕ → ℝ) (n : ℕ) : ℝ := ⨆ K, heineK x w K n

/-- Pure-power sequence `(k+1)^{-p}` (0-based index `k` = item-11 atom `k+1`). -/
noncomputable def powSeq (p : ℝ) : ℕ → ℝ := fun k => ((k : ℝ) + 1) ^ (-p)

/-- `(log D n - (-p n² log n + n² ℓ n + κ n²)) / n²`. -/
noncomputable def hnorm (p κ : ℝ) (D ℓ : ℕ → ℝ) (n : ℕ) : ℝ :=
  (Real.log (D n) - (-p * (n : ℝ) ^ 2 * Real.log n + (n : ℝ) ^ 2 * ℓ n + κ * (n : ℝ) ^ 2)) / (n : ℝ) ^ 2

/-- NAMED INPUT — item 11 Theorem H for atoms `(k+1)^{-p}`, weights `(k+1)^{-s}` (PROVED in item 11 via the
Lommel / Tricomi–Carlitz families; NOT formalized): bounded in `K`, and `log D_n = -p n² log n + κ n² + o(n²)`. -/
structure TheoremHPure (p κ s : ℝ) : Prop where
  bdd : ∀ n, BddAbove (Set.range fun K => heineK (powSeq p) (powSeq s) K n)
  asymp : Tendsto (hnorm p κ (heineD (powSeq p) (powSeq s)) (fun _ => 0)) atTop (𝓝 0)

theorem heineK_zero_card (x w : ℕ → ℝ) (K : ℕ) : heineK x w K 0 = 1 := by
  sorry

theorem heineK_pos {x w : ℕ → ℝ} (hx : StrictAnti x) (hw : ∀ i, 0 < w i) {K n : ℕ} (hKn : n ≤ K) :
    0 < heineK x w K n := by
  sorry

theorem heineK_le_heineD {x w : ℕ → ℝ} {n : ℕ} (hb : BddAbove (Set.range fun K => heineK x w K n)) (K : ℕ) :
    heineK x w K n ≤ heineD x w n := by
  sorry

theorem heineD_le {x w : ℕ → ℝ} {n : ℕ} {C : ℝ} (h : ∀ K, heineK x w K n ≤ C) : heineD x w n ≤ C := by
  sorry

theorem heineD_pos {x w : ℕ → ℝ} (hx : StrictAnti x) (hw : ∀ i, 0 < w i) {n : ℕ}
    (hb : BddAbove (Set.range fun K => heineK x w K n)) : 0 < heineD x w n := by
  sorry

/-- Uniform-in-`N` upper form of the input. -/
theorem TheoremHPure.uniform_upper {p κ s : ℝ} (h : TheoremHPure p κ s) {η : ℝ} (hη : 0 < η) :
    ∃ C : ℝ, ∀ N : ℕ, Real.log (heineD (powSeq p) (powSeq s) N) ≤
      -p * (N : ℝ) ^ 2 * Real.log N + κ * (N : ℝ) ^ 2 + η * (N : ℝ) ^ 2 + C := by
  sorry

end JacobiAsym
```

Add `import JacobiAsym.Inputs` to `lean/JacobiAsym.lean`. Add the 6 `#print axioms` lines. Append `heineK_pos`,
`heineD_pos` and `TheoremHPure.uniform_upper` to `need` in `check.sh`; the audit line prints the name as
`JacobiAsym.TheoremHPure.uniform_upper`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/Inputs.lean`
Expected: 6 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `heineK_zero_card`: `powersetCard_zero` gives `{∅}`. Then `sum_singleton`; `heineTerm ∅ = 1` by `prod_empty`, and
  `pairs ∅ = ∅` by `simp [pairs]`.
- `heineK_pos`:
  - `single_le_sum` with `S = range n ∈ (range K).powersetCard n` (`powersetCard_mono`, `card_range`) and
    nonnegativity (`heineTerm_nonneg`).
  - `heineTerm x w (range n) > 0`: the weights are positive (`prod_pos`). Each pair (a, b) with a < b has
    x a ≠ x b (`hx.injective`, or `hx` directly gives x b < x a), so `(x a - x b)^2 > 0` (`pow_pos`/`sq_pos_of_ne_zero`).
- `heineK_le_heineD`: `le_ciSup hb K`.
- `heineD_le`: `ciSup_le h`; the index type ℕ is nonempty.
- `heineD_pos`: `(heineK_pos hx hw (le_refl n)).trans_le (heineK_le_heineD hb n)`.
- `TheoremHPure.uniform_upper`:
  1. From `h.asymp`: `∀ᶠ N in atTop, hnorm … N ≤ η` (`(h.asymp.eventually (gt_mem_nhds hη))`, then take ≤). Get N0,
     and also take N ≥ 1 so that `(N:ℝ)^2 > 0`.
  2. Unfold `hnorm` with ℓ = 0 and multiply by N² (`div_le_iff₀`).
  3. For N < N0, take C := max over `range N0` of `log D N - (-pN² log N + κN² + ηN²)`
     (`Finset.sup'`, or `∑` of positive parts as a crude bound). Use C' := max C 0.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/Inputs.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/Inputs.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: D_n as sup of Heine sums, named input TheoremHPure, positivity and uniform-input lemmas

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: `SlowFactor.lean`: hypotheses on L, slow variation, the lower constant ρ₋

**Files:**
- Create: `lean/JacobiAsym/SlowFactor.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Consumes: none (Mathlib only).
- Produces:
  - `slowAtom p L t := t^(-p) * L t`; structure `SlowFactor p L L' E a0`.
  - `SlowFactor.logL_slow`: H6(a), the form consumed by Plan 2's `weighted_cesaro_slow`/`slow_shift` with
    ℓ = log ∘ L.
  - `SlowFactor.exists_rhoMin`: ρ₋.
  - Helpers `SlowFactor.L_cont`, `SlowFactor.R_pos` (stated in Step 1).

- [ ] **Step 1: Write the statements with `sorry`**

```lean
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
    ContinuousOn L (Set.Ici 1) := by
  sorry

/-- `R t := L t - t L' t / p > 0` on `[1, ∞)` (equivalent to `f' < 0`). -/
theorem SlowFactor.R_pos {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∀ t, 1 ≤ t → 0 < L t - t * L' t / p := by
  sorry

/-- H6(a): `|log L y - log L x| ≤ E x · log (y/x)` for `1 ≤ x ≤ y`. -/
theorem SlowFactor.logL_slow {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∀ x y : ℝ, 1 ≤ x → x ≤ y → |Real.log (L y) - Real.log (L x)| ≤ E x * Real.log (y / x) := by
  sorry

/-- The lower constant `ρ₋` of item 11 Lemma H5(ii). -/
theorem SlowFactor.exists_rhoMin {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∃ ρm : ℝ, 0 < ρm ∧ ρm ≤ (1 - E a0 / p) * L a0 ∧ ∀ t, 1 ≤ t → ρm ≤ L t - t * L' t / p := by
  sorry

end JacobiAsym
```

Add the import, 4 audit lines, and `SlowFactor.logL_slow SlowFactor.exists_rhoMin` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/SlowFactor.lean`
Expected: 4 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `L_cont`: `fun t ht => (h.L_deriv t ht).continuousAt.continuousWithinAt`.
- `R_pos`: from `f_dec` and `p_pos`, `L t - t L' t / p = (p L t - t L' t)/p > 0` (`div_pos`, `sub_pos`), then
  `field_simp`.
- `logL_slow`:
  1. Apply the mean value theorem (`exists_hasDerivAt_eq_slope`) to `φ(u) := log (L (exp u))` on
     `[log x, log y]` (if x = y both sides are 0).
  2. `φ'(u) = exp u · L'(exp u) / L(exp u)`, by `HasDerivAt.log`, `HasDerivAt.comp` and `Real.hasDerivAt_exp`, with
     `L (exp u) > 0`.
  3. So `|φ(log y) − φ(log x)| = |ε(exp c)|·(log y − log x) ≤ E(exp c)·log(y/x) ≤ E x · log(y/x)`, because
     `exp c ≥ x` (`E_anti`) and `Real.log_div`.
- `exists_rhoMin`:
  1. Let `R t := L t - t * L' t / p`, which is continuous on `Icc 1 a0` (`L_cont`, `L'_cont`, `ContinuousOn.mul`,
     `.sub`).
  2. `isCompact_Icc.exists_isMinOn` (nonempty since `1 ≤ a0`) gives a minimum ρ1 = R t1 > 0 (`R_pos`).
  3. Put ρm := min ρ1 ((1 − E a0/p)·L a0), which is positive (`E_a0`, `L_pos`).
  4. For t ≥ a0: `R t = L t (1 − ε/p) ≥ L t (1 − E t/p) ≥ L a0 (1 − E a0/p)`, using `|ε| ≤ E t`, `E_anti`,
     `L_mono` and nonnegativity of the factors. Use `abs_le` and `nlinarith`.
  5. For 1 ≤ t ≤ a0, use the minimum.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/SlowFactor.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/SlowFactor.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: SlowFactor hypotheses (L1)-(L3), H6(a) slow variation from eps, lower constant rho_min

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: `PairBounds.lean`: Lemma H5 for `slowAtom`, and the cut comparison atoms

**Files:**
- Create: `lean/JacobiAsym/PairBounds.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: `SlowFactor`, `slowAtom`, `exists_rhoMin`, `R_pos`, `L_cont` (Task 2); `ratio_bounds_of_deriv`,
  `diff_le_of_L_mono` (Plan 2).
- Produces:
  - `slowAtom_hasDerivAt`.
  - `SlowFactor.lower_pair`: H5 lower bound, with ρm for a < a0 and (1−E a/p)L a otherwise.
  - `SlowFactor.upper_pair`: H5 upper bound, with B for a < a0 and 1 otherwise, times L T for any T ≥ c, T ≥ a0.
  - `cutAtom p L K0`: item 11's G, 0-based: pure power on k < K0, `slowAtom/L K0` on the tail.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.SlowFactor
import JacobiAsym.RatioBounds

namespace JacobiAsym

theorem slowAtom_hasDerivAt {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) {t : ℝ} (ht : 1 ≤ t) :
    HasDerivAt (slowAtom p L) (-p * t ^ (-p - 1) * L t + t ^ (-p) * L' t) t := by
  sorry

theorem SlowFactor.lower_pair {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) {ρm : ℝ}
    (hρm : ∀ t, 1 ≤ t → ρm ≤ L t - t * L' t / p) {a c : ℝ} (ha : 1 ≤ a) (hac : a < c) :
    (if a < a0 then ρm else (1 - E a / p) * L a) * (a ^ (-p) - c ^ (-p)) ≤ slowAtom p L a - slowAtom p L c := by
  sorry

theorem SlowFactor.upper_pair {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) :
    ∃ B : ℝ, 1 ≤ B ∧ ∀ a c T : ℝ, 1 ≤ a → a < c → c ≤ T → (a0 : ℝ) ≤ T →
      slowAtom p L a - slowAtom p L c ≤ (if a < a0 then B else 1) * L T * (a ^ (-p) - c ^ (-p)) := by
  sorry

/-- Item 11's comparison atoms `G` (0-based): pure power on the head `k < K0`, rescaled tail `f(k+1)/L(K0)`. -/
noncomputable def cutAtom (p : ℝ) (L : ℝ → ℝ) (K0 : ℕ) (k : ℕ) : ℝ :=
  if k < K0 then ((k : ℝ) + 1) ^ (-p) else slowAtom p L ((k : ℝ) + 1) / L K0

end JacobiAsym
```

Add the import, 3 audit lines, and `SlowFactor.lower_pair SlowFactor.upper_pair` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/PairBounds.lean`
Expected: 3 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `slowAtom_hasDerivAt`: `(Real.hasDerivAt_rpow_const (Or.inl (by linarith))).mul (h.L_deriv t ht)`. Normalize with
  `ring_nf`/`simp`: rpow's derivative is `-p * t^(-p-1)`.
- `lower_pair`:
  1. Apply `ratio_bounds_of_deriv` on `[a, c]` with `f = slowAtom p L`, `g = fun t => t^(-p)`,
     `g' t = -p t^(-p-1) < 0`, and `lo` the `if`-value. Only `.1` is needed.
  2. The pointwise condition `lo·(p t^(-p-1)) ≤ p t^(-p-1) L t − t^(-p) L' t` is equivalent, dividing by
     `p t^(-p-1) > 0` and using `t^(-p) = t · t^(-p-1)` (`Real.rpow_sub_one`/`rpow_add`), to `lo ≤ L t − t L' t / p`.
  3. Case a < a0: `hρm`.
  4. Case a ≥ a0: `L t (1 − E t/p) ≥ L a (1 − E a/p)` for t > a, as in `exists_rhoMin`; then `R t ≥ L t (1 − E t/p)`
     from `eps_le`.
  5. Continuity on `Icc a c` comes from the derivatives (`HasDerivAt.continuousAt`).
- `upper_pair`:
  1. Let B0 = the max of R on `Icc 1 a0` (compactness, as in Task 2), Lmin = the min of L on `Icc 1 a0` (> 0), and
     B := max 1 (max B0 (L a0) / Lmin). Note L t ≥ min(Lmin, L a0) for all t ≥ 1, and Lmin ≤ L a0, so
     L t ≥ Lmin for t ≥ 1.
  2. Case a ≥ a0: `diff_le_of_L_mono` (with `L_mono`: L a ≤ L c) gives `≤ L a (a^(-p) − c^(-p))`. Then
     L a ≤ L T (`L_mono`, a ≤ T) and `a^(-p) − c^(-p) ≥ 0`.
  3. Case a < a0 ≤ c: split at a0. Use `ratio_bounds_of_deriv` (`.2`, with hi = B0) on `[a, a0]`, and Case 2's
     algebra on `[a0, c]` with factor L a0 ≤ L T. Both factors are ≤ B·L T, because B0 ≤ B·Lmin ≤ B·L T and
     L a0 ≤ L T ≤ B·L T.
  4. Case c < a0: `ratio_bounds_of_deriv` `.2` with hi = B0 ≤ B·L T.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/PairBounds.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/PairBounds.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: Lemma H5 for slowAtom (lower with rho_min, upper with B split at a0), cut atoms G

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: `UpperChain.lean`: the per-n upper bound and BddAbove for the f-measure

**Files:**
- Create: `lean/JacobiAsym/UpperChain.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes:
  - `upper_pair`, `cutAtom` (Task 3).
  - `heineTerm_le_of_pair_le_split`, `heineK_tail_split`, `factorial_le_prod_succ`, `heineK_mono_w`,
    `heineK_smul_w` (Plan 2).
  - `heineD`, `heineK_le_heineD` (Task 1).
- Produces:
  - `upperTerm`, the explicit m-th term.
  - `heineK_slow_le`, the per-(n, M, K) bound.
  - `slow_bdd`: `BddAbove` of the f-measure's truncated sums. Item 11's tail mass is `W := ∑' k, w k`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.PairBounds
import JacobiAsym.Inputs

open Finset

namespace JacobiAsym

/-- The m-th term of item 11 Lemma H7 (head `N = n - m` points, tail `m` points), with `X = (Mn)^{-p}`. -/
noncomputable def upperTerm (p s0 c2 W : ℝ) (U : ℝ → ℝ) (Mn n m : ℕ) : ℝ :=
  ((n - m).factorial : ℝ) ^ (-(2 * p * m)) * (c2 * U Mn) ^ (n - m) *
    heineD (powSeq p) (powSeq s0) (n - m) * W ^ m * ((Mn : ℝ) ^ (-p)) ^ (m * (m - 1))

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
  sorry

theorem slow_bdd {p κ s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    (hHup : TheoremHPure p κ s0) (hc2 : 0 < c2)
    (hw0 : ∀ k, 0 < w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1)) (hUmono : Monotone U)
    (hwsum : Summable w) (n : ℕ) :
    BddAbove (Set.range fun K => heineK (fun k => slowAtom p L ((k : ℝ) + 1)) w K n) := by
  sorry

end JacobiAsym
```

Add the import, 2 audit lines, and `heineK_slow_le slow_bdd` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/UpperChain.lean`
Expected: 2 `sorry` warnings and no errors. If there are errors, fix the binder issue noted above.

- [ ] **Step 3: Prove**

`heineK_slow_le`, with `K0 := M*n`, `G := cutAtom p L K0`, `x := fun k => slowAtom p L (k+1)` and `lam := L K0`:
1. **Pair bound** for every configuration S (all k ∈ ℕ) and a < b:
   `(x a − x b)^2 ≤ (if a < a0 then B else 1)^2 · lam^2 · (G a − G b)^2`. Work with the unsquared form
   `0 ≤ x a − x b ≤ c·lam·(G a − G b)` (`pow_le_pow_left₀` on nonnegatives), using three cases as in item 11:
   - both indices in the head (b < K0): `hB` with T = K0, a ↦ a+1, c ↦ b+1, noting `(a+1 < a0) → (a < a0)` and B ≥ 1;
   - mixed (a < K0 ≤ b): split at the real point K0 =: T. `hB` on `[a+1, K0]`, plus the exact tail identity
     `x K0' − x b = lam·(G(K0−1) − G b)` with `G (K0-1) = K0^(-p) = slowAtom p L K0 / L K0`;
   - both in the tail: an exact identity, factor `lam`.

   Nonnegativity `x a − x b ≥ 0` comes from `lower_pair` (Task 3) with `exists_rhoMin`.
2. `heineTerm_le_of_pair_le_split` termwise, summed over `powersetCard n (range K)`, gives
   `heineK x w K n ≤ B^(2 a0 n) lam^(n(n-1)) heineK G w K n`.
3. `heineK_tail_split` on `G` with `K0`, `X := K0^(-p)`:
   - `hpos`: L > 0;
   - `htail`: `slowAtom` is decreasing (from `lower_pair`) and `slowAtom p L K0 / L K0 = K0^(-p)`;
   - `hord`: tail ≤ X ≤ head.

   If K < K0, first enlarge K to `max K K0` with `heineK_mono_K`.
4. **Head factor.** For SH ⊆ range K0 with |SH| = N:
   - `∏_{a∈SH} G a^(2m) = ∏ ((a+1)^(-p))^(2m) ≤ (N!)^(-2pm)`. Use `factorial_le_prod_succ` and
     `Real.rpow_le_rpow_of_nonpos`-style monotonicity, rewriting the product of rpow's as an rpow of the product
     (`Real.finset_prod_rpow`).
   - `heineTerm G w SH = heineTerm (powSeq p) w SH` (pointwise equality on SH, via `prod_congr`).
   - `∑_{SH} heineTerm (powSeq p) w SH ≤ (c2 U K0)^N heineK (powSeq p) (powSeq s0) K0 N` (Review Focus #5): bound
     termwise with `w a ≤ c2 · powSeq s0 a · U K0` for a < K0 (`hUmono`), `prod_le_prod₀` and `prod_const`.
   - Finally `≤ … heineD …` (`heineK_le_heineD hHup.bdd`).
5. **Tail mass.** `∑_{b ∈ Ico K0 K} w b ≤ ∑' w` (`sum_le_tsum` with `hwsum`, `hw0`).
6. Assemble with `gcongr`. All factors are nonnegative; the exponent `m(m-1)` is even (`Nat.even_mul_pred_self`).

`slow_bdd`: take M := a0 (so `a0 ≤ M*n` when n ≥ 1; the case n = 0 is trivial via `heineK_zero_card`). The
right-hand side of `heineK_slow_le` does not depend on K.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/UpperChain.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/UpperChain.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: H_L upper chain per (n, M, K) via split pairs, tail cut, factorial head bound; BddAbove of f-measure

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: `Exponent.lean`: logarithm of the m-th term, uniformly in m

**Files:**
- Create: `lean/JacobiAsym/Exponent.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: `upperTerm` (Task 4), `TheoremHPure.uniform_upper`, `heineD_pos` (Task 1), `phi_bound`,
  `sum_log_div_le`'s factorial bound (Plan 2; reuse `Real.pow_div_factorial_le_exp`).
- Produces:
  - `exponent_identity`: exact.
  - `log_factorial_ge`: log N! ≥ N log N − N.
  - `log_upperTerm_le`: an explicit bound, uniform in 0 ≤ m ≤ n.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.UpperChain
import JacobiAsym.Penalty

open Finset

namespace JacobiAsym

theorem log_factorial_ge (N : ℕ) : (N : ℝ) * Real.log N - N ≤ Real.log (N.factorial) := by
  sorry

/-- The exact exponent identity of item 11 Lemma H7 step 5 (`log 0 = 0` makes `m = n` work too). -/
theorem exponent_identity {p κ M n m : ℝ} (hn : 0 < n) (hm0 : 0 ≤ m) (hmn : m ≤ n) (hM : 0 < M) :
    -2 * p * m * ((n - m) * Real.log (n - m)) + 2 * p * m * (n - m) - p * (n - m) ^ 2 * Real.log (n - m)
      + κ * (n - m) ^ 2 - p * m ^ 2 * (Real.log M + Real.log n)
    = -p * n ^ 2 * Real.log n + κ * n ^ 2 + n ^ 2 * (-p * (1 - (m / n) ^ 2) * Real.log (1 - m / n)
      + 2 * p * (m / n) * (1 - m / n) - κ * (m / n) * (2 - m / n) - p * (m / n) ^ 2 * Real.log M) := by
  sorry

/-- Uniform bound on the m-th term: for `n ≥ 1`, `m ≤ n`, `M ≥ 2`, any `C` from `uniform_upper` at level `η`:
`log upperTerm ≤ -p n² log n + κ n² + (A²/(4p log M) + η) n² + C + n (|log (c2 U(Mn))| + |log W| + p log (Mn))`,
`A = 4p + 2|κ|`. -/
theorem log_upperTerm_le {p κ s0 c2 W η C : ℝ} {U : ℝ → ℝ} (hp : 0 < p) (hη : 0 < η)
    (hHup : TheoremHPure p κ s0)
    (hC : ∀ N : ℕ, Real.log (heineD (powSeq p) (powSeq s0) N) ≤
      -p * (N : ℝ) ^ 2 * Real.log N + κ * (N : ℝ) ^ 2 + η * (N : ℝ) ^ 2 + C)
    (hc2U : ∀ t, 0 < c2 * U t) (hW : 0 < W) {M n m : ℕ} (hM : 2 ≤ M) (hn : 1 ≤ n) (hmn : m ≤ n) :
    Real.log (upperTerm p s0 c2 W U (M * n) n m) ≤
      -p * (n : ℝ) ^ 2 * Real.log n + κ * (n : ℝ) ^ 2
        + ((4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) + η) * (n : ℝ) ^ 2 + C
        + n * (|Real.log (c2 * U (M * n))| + |Real.log W| + p * Real.log (M * n)) := by
  sorry

end JacobiAsym
```

Add the import, 3 audit lines, and `exponent_identity log_upperTerm_le` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/Exponent.lean`
Expected: 3 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `log_factorial_ge`: from `Real.pow_div_factorial_le_exp (N:ℝ) _ N`, take logs (`Real.log_le_iff_le_exp`),
  `Real.log_div`, `Real.log_pow`. Handle N = 0 by `simp`.
- `exponent_identity`:
  - Case m = n: `simp` (`sub_self`, `Real.log_zero`, `div_self`), then `ring`.
  - Case m < n: rewrite `Real.log (n - m) = Real.log n + Real.log (1 - m/n)` via
    `n - m = n * (1 - m/n)` and `Real.log_mul` (both factors positive). Then `field_simp` and `ring`.
- `log_upperTerm_le`:
  1. Positivity of each factor (`heineD_pos` with `StrictAnti (powSeq p)`, `Nat.factorial_pos`, `rpow_pos_of_pos`).
     Then `Real.log_mul`, `Real.log_rpow`, `Real.log_pow` expand the log into
     `−2pm·log N! + N log(c2U) + log D(N) + m log W + m(m−1)(−p log(Mn))`.
  2. Bound:
     - `−2pm log N! ≤ −2pm(N log N − N)` (`log_factorial_ge`, with −2pm ≤ 0);
     - `log D(N) ≤ hC N`;
     - `N log(c2U) ≤ n|·|`, `m log W ≤ n|log W|`, and `ηN² ≤ ηn²`;
     - `−p m(m−1) log(Mn) = −p m² log(Mn) + p m log(Mn) ≤ −p m²(log M + log n) + n·p log(Mn)`
       (`Real.log_mul`, cast).
  3. Rewrite the remaining main part with `exponent_identity` (cast m, n to ℝ, so 0 ≤ m ≤ n).
  4. Then `phi_bound hp (by exact_mod_cast …: (1:ℝ) < M) (m/n ≥ 0) (m/n ≤ 1)`, multiplied by n² ≥ 0.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/Exponent.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/Exponent.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: exact H7 exponent identity, log N! lower bound, uniform-in-m bound on log of the m-th term

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: `UpperBound.lean`: limsup ≤ A²/(4p log M) + η

**Files:**
- Create: `lean/JacobiAsym/UpperBound.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: Tasks 1–5; `slow_shift` (Plan 2) with ℓ = log ∘ L via `logL_slow` (Task 2).
- Produces: `HL_upper`: for every integer M ≥ 2 and η > 0, eventually
  `hnorm p κ D_f (log ∘ L ∘ cast) n ≤ A²/(4p log M) + η`.

- [ ] **Step 1: Write the statement with `sorry`**

```lean
import JacobiAsym.Exponent
import JacobiAsym.SlowVariation

open Finset Filter Topology

namespace JacobiAsym

theorem HL_upper {p κ s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    (hHup : TheoremHPure p κ s0) (hc2 : 0 < c2)
    (hw0 : ∀ k, 0 < w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hU1 : ∀ t, 1 ≤ U t) (hUmono : Monotone U)
    (hUsub : Tendsto (fun n : ℕ => Real.log (U n) / n) atTop (𝓝 0)) (hwsum : Summable w)
    {M : ℕ} (hM : 2 ≤ M) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop,
      hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)) n ≤
        (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) + η := by
  sorry

end JacobiAsym
```

Add the import, an audit line, and `HL_upper` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/UpperBound.lean`
Expected: 1 `sorry` warning and no errors.

- [ ] **Step 3: Prove**

1. Get B from `hL.upper_pair`, and C from `hHup.uniform_upper (η/2)`.
2. For n ≥ max(1, a0) (so `a0 ≤ M n`): `heineD_le` with `heineK_slow_le` gives
   `D_f(n) ≤ B^(2a0n) L(Mn)^(n(n−1)) ∑_{m≤n} upperTerm`.
3. `log ∑_{m≤n} T_m ≤ log(n+1) + max_m log T_m`, from `sum_le_card_nsmul` with `Finset.exists_max_image`, then
   `Real.log_le_log` and `Real.log_mul`.
4. Use `log_upperTerm_le` at level η/2 for the max.
5. `log D_f(n) − main(n)` over n² is then
   `≤ A²/(4p log M) + η/2 + [2a0 n log B + n(n−1) log L(Mn) − n² log L(n) + log(n+1) + C + n(…)]/n²`.
6. The bracket over n² tends to 0:
   - `(n(n−1) log L(Mn) − n² log L(n))/n² = (log L(Mn) − log L(n)) − log L(Mn)/n`;
   - the first part tends to 0 by `slow_shift` (ℓ = log ∘ L, hypothesis from `logL_slow`);
   - `log L(Mn)/n → 0`, since `|log L(Mn) − log L 1| ≤ E 1 · log(Mn)` by `logL_slow`;
   - `log(n+1)/n² → 0`, `C/n² → 0`, `2a0 log B / n → 0`;
   - `|log(c2 U(Mn))|/n → 0` by `hUsub` (composed with `n ↦ M n`, plus constant/n), and `p log(Mn)/n → 0`.

   Each piece follows from `Real.tendsto_pow_log_div_mul_add_atTop`, `tendsto_const_div_atTop_nhds_zero_nat` and
   `Tendsto.add`.
7. Eventually the bracket is ≤ η/2.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/UpperBound.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/UpperBound.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: Theorem H_L upper half — eventually hnorm <= A^2/(4p log M) + eta

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: `LowerBound.lean`: liminf ≥ 0

**Files:**
- Create: `lean/JacobiAsym/LowerBound.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: `lower_pair`, `exists_rhoMin`, `logL_slow` (Tasks 2–3); `slow_bdd` (Task 4); `heineTerm_ge_of_pair_ge`,
  `heineK_mono_w`, `heineK_smul_w`, `weighted_cesaro_slow` (Plan 2); Task 1.
- Produces:
  - `rhoSeq`, the monotone ρ in 0-based form, and `rhoSeq_mono`.
  - `HL_lower`: for every η > 0, eventually `hnorm … n ≥ −η`.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.UpperChain
import JacobiAsym.SlowVariation

open Finset Filter Topology

namespace JacobiAsym

/-- The monotone lower pair factor, 0-based: index `k` ↔ atom `k+1`. -/
noncomputable def rhoSeq (p : ℝ) (L E : ℝ → ℝ) (a0 : ℕ) (ρm : ℝ) (k : ℕ) : ℝ :=
  if (k : ℝ) + 1 < a0 then ρm else (1 - E ((k : ℝ) + 1) / p) * L ((k : ℝ) + 1)

theorem rhoSeq_mono {p : ℝ} {L L' E : ℝ → ℝ} {a0 : ℕ} (h : SlowFactor p L L' E a0) {ρm : ℝ}
    (hρm0 : 0 < ρm) (hρm : ρm ≤ (1 - E a0 / p) * L a0) :
    Monotone (rhoSeq p L E a0 ρm) ∧ ∀ k, 0 < rhoSeq p L E a0 ρm k := by
  sorry

theorem HL_lower {p κ s c1 s0 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ} (hL : SlowFactor p L L' E a0)
    (hHlo : TheoremHPure p κ s) (hHup : TheoremHPure p κ s0) (hc1 : 0 < c1) (hc2 : 0 < c2)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hUmono : Monotone U) (hwsum : Summable w) {η : ℝ} (hη : 0 < η) :
    ∀ᶠ n : ℕ in atTop,
      -η ≤ hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)) n := by
  sorry

end JacobiAsym
```

Add the import, 2 audit lines, and `rhoSeq_mono HL_lower` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/LowerBound.lean`
Expected: 2 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `rhoSeq_mono`:
  - Positivity: `L_pos` and `1 − E/p > 0` (`E_anti`, `E_a0`, a0 ≤ k+1 in that branch).
  - Monotone: within the head branch it is constant. Within the tail branch it is a product of two nonnegative
    nondecreasing factors (`L_mono`, `E_anti`). Across the boundary, use `hρm` and the tail branch value at a0 or
    later.
- `HL_lower`:
  1. Termwise, for every S: `ρ(a)²(g(a+1) − g(b+1))² ≤ (x a − x b)²`, by `lower_pair` with a ↦ a+1, then squaring
     nonnegatives. This needs `ρ ≥ 0` and `g(a+1) − g(b+1) ≥ 0`.
  2. So `(∏_{i<n} ρ_i^(2(n−1−i))) heineK (powSeq p) w K n ≤ heineK x w K n ≤ heineD x w n`, by `slow_bdd` and
     `heineTerm_ge_of_pair_ge`. Then `heineK (powSeq p) w ≥ c1^n heineK (powSeq p) (powSeq s)`, by
     `heineK_mono_w` and `heineK_smul_w`.
  3. Sup over K (`ciSup_le` on the left, `hHlo.bdd`) gives `Πρ · c1^n · D_g,s(n) ≤ D_f(n)`. Take logs (all factors
     positive):

         log D_f(n) ≥ ∑_{i<n} 2(n−1−i) log ρ_i + n log c1 + log D_g,s(n).

  4. Asymptotics:
     - `log D_g,s(n) ≥ main_g(n) − η/3·n²` eventually (`hHlo.asymp`).
     - `(n log c1)/n² → 0`.
     - **Key:** `(∑_{i<n} 2(n−1−i) log ρ_i − n² log L(n))/n² → 0`. For i+1 ≥ a0, write
       `log ρ_i = log L(i+1) + log(1 − E(i+1)/p)`.
       - `(2/n²)∑ (n−1−i) log(1 − E(i+1)/p) → 0` (Cesàro: `E → 0`, so `log(1 − E/p) → 0`; same ε–N pattern as
         `weighted_cesaro_slow`).
       - `(2/n²)∑ (n−1−i)(log L(i+1) − log L(n)) → 0` follows from `weighted_cesaro_slow` with ℓ = log ∘ L, after
         the shift j = i+1: the weights `(n−1−i) = (n − j)` match exactly. Use `Finset.sum_bij`/`sum_Ico_eq_sum_range`
         to re-index.
       - `(2/n²)∑_{i<n}(n−1−i) = (n−1)/n`, so the constant part gives `log L(n)·(n−1)/n − log L(n) = −log L(n)/n → 0`.
       - The finitely many i+1 < a0 contribute `O(n)·(|log ρm| + |log L(n)|)`, which is o(n²).

       Put this in a separate lemma `rho_sum_asymp`, with its own audit line.
  5. Combine: eventually `hnorm ≥ −η`.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/LowerBound.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/LowerBound.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: Theorem H_L lower half — monotone rank factor, sum asymptotics, eventually hnorm >= -eta

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 8: `TheoremHL.lean`: the theorem

**Files:**
- Create: `lean/JacobiAsym/TheoremHL.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Consumes: `HL_upper` (Task 6), `HL_lower` (Task 7).
- Produces: `theoremHL`, the headline.

- [ ] **Step 1: Write the statement with `sorry`**

```lean
import JacobiAsym.UpperBound
import JacobiAsym.LowerBound

open Filter Topology

namespace JacobiAsym

/-- **Item 11 Theorem H_L (PROVED-mod-input).**  Atoms `(k+1)^{-p} L(k+1)` with `L` slowly varying
(`SlowFactor`), weights sandwiched `c1 (k+1)^{-s} ≤ w k ≤ c2 (k+1)^{-s0} U(k+1)`; given the named input
Theorem H for the pure powers with exponents `s` and `s0` and constant `κ = 3p/2 + log c(p)`:
`log D_n = -p n² log n + n² log L(n) + κ n² + o(n²)`. -/
theorem theoremHL {p κ s s0 c1 c2 : ℝ} {L L' E U : ℝ → ℝ} {a0 : ℕ} {w : ℕ → ℝ}
    (hL : SlowFactor p L L' E a0) (hHlo : TheoremHPure p κ s) (hHup : TheoremHPure p κ s0)
    (hc1 : 0 < c1) (hc2 : 0 < c2)
    (hwlo : ∀ k, c1 * powSeq s k ≤ w k) (hwhi : ∀ k, w k ≤ c2 * powSeq s0 k * U ((k : ℝ) + 1))
    (hU1 : ∀ t, 1 ≤ U t) (hUmono : Monotone U)
    (hUsub : Tendsto (fun n : ℕ => Real.log (U n) / n) atTop (𝓝 0))
    (hwsum : Summable w) :
    Tendsto (hnorm p κ (heineD (fun k => slowAtom p L ((k : ℝ) + 1)) w) (fun n => Real.log (L n)))
      atTop (𝓝 0) := by
  sorry

end JacobiAsym
```

Add the import, an audit line, and `theoremHL` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/TheoremHL.lean`
Expected: 1 `sorry` warning and no errors.

- [ ] **Step 3: Prove**

`Metric.tendsto_atTop`. Given ε > 0:
1. Choose an integer M ≥ 2 with `A²/(4p log M) < ε/3`. Since `log M → ∞`, take M = ⌈exp(3A²/(4pε))⌉₊ + 2,
   using `Real.add_one_le_exp` or `Real.log_le_log`.
2. Apply `HL_upper` with η = ε/3 and `HL_lower` with η = ε/2, and combine the `eventually`s with `Filter.Eventually.and`.
3. Then `|hnorm| < ε` (`abs_lt`).

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/TheoremHL.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`. `#print axioms JacobiAsym.theoremHL` lists only the three standard axioms.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/TheoremHL.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: Theorem H_L (item 11) proved from the named input TheoremHPure

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 9: `LemmaP.lean`: item 11 Lemma P

**Files:**
- Create: `lean/JacobiAsym/LemmaP.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`, `lean/check.sh`

**Interfaces:**
- Produces: `lemmaP`. J ≥ 0 is stated as nonnegativity of the quadratic form of the truncations, written as the
  explicit sum. This is the exact content used in item 11.

- [ ] **Step 1: Write the statement with `sorry`**

```lean
import JacobiAsym.Basic

open Finset Filter Topology

namespace JacobiAsym

/-- Item 11 Lemma P: if the Jacobi form is nonnegative, `(n+1)^p a_n → α` and `(n+1)^p b_n → β`, then
`α ≥ 2β`.  (0-based: `a n`, `b n` are item 11's `a_{n+1}`, `b_{n+1}`; `b n` couples `v n` and `v (n+1)`.) -/
theorem lemmaP {a b : ℕ → ℝ} {p α β : ℝ} (hp : 0 < p)
    (hJ : ∀ v : ℕ → ℝ, ∀ N, (∀ n, N ≤ n → v n = 0) →
      0 ≤ ∑ n ∈ range N, a n * v n ^ 2 + 2 * ∑ n ∈ range N, b n * v n * v (n + 1))
    (ha : Tendsto (fun n : ℕ => ((n : ℝ) + 1) ^ p * a n) atTop (𝓝 α))
    (hb : Tendsto (fun n : ℕ => ((n : ℝ) + 1) ^ p * b n) atTop (𝓝 β)) : 2 * β ≤ α := by
  sorry

end JacobiAsym
```

Why `hJ` carries the support condition `∀ n ≥ N, v n = 0`: the sum then equals ⟨J v, v⟩ for the finitely supported
v, which is ≥ 0 when J ≥ 0. Without it, the boundary term `2 b_{N-1} v_{N-1} v_N` would make `hJ` strictly stronger
than J ≥ 0, so the lemma would assume more than item 11 does.

Add the import, an audit line, and `lemmaP` to `need`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/LemmaP.lean`
Expected: 1 `sorry` warning and no errors.

- [ ] **Step 3: Prove**

Item 11's proof:
1. Suppose α < 2β and put δ := 2β − α > 0.
2. Take `v n := (-1)^n` for `L ≤ n ≤ 2L` and 0 otherwise, with N = 2L+2.
3. The form equals `∑_{L}^{2L} a_n − 2∑_{L}^{2L−1} b_n`.
4. For large L, `a_n ≤ (α + δ/4)(n+1)^{-p}` and `b_n ≥ (β − δ/4)(n+1)^{-p}` on that range (from the limits, since
   n ≥ L).
5. So the form ≤ `(α − 2β + 3δ/4)·∑_{L}^{2L−1}(n+1)^{-p} + (α+δ/4)(2L+1)^{-p}`, which is
   `−(δ/4)∑ + O(L^{-p})`.
6. And `∑_{L}^{2L−1}(n+1)^{-p} ≥ L·(2L)^{-p}`, which dominates `(2L+1)^{-p}` for large L.
7. This contradicts `hJ`. The ε–N bookkeeping is in Mathlib style: `Metric.tendsto_atTop`, then pick L ≥ N0 large.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/LemmaP.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/LemmaP.lean lean/JacobiAsym.lean lean/Audit.lean lean/check.sh
git commit -m "lean: Lemma P (alpha >= 2 beta) from nonnegativity of the truncated Jacobi forms

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 10: Documentation and status

**Files:**
- Modify: `lean/README.md`, `README.md`, `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` (§6
  scope note)

- [ ] **Step 1: Verify the headline axioms**

Run: `cd lean && lake env lean Audit.lean 2>&1 | grep -A1 "theoremHL\|lemmaP"`
Expected: both show `[propext, Classical.choice, Quot.sound]` (or a subset).

- [ ] **Step 2: Update the docs**

1. In `lean/README.md`, add rows:

   ```
   | `heineD`, `TheoremHPure` (NAMED INPUT), `hnorm` | Thm H (input) | D_n = sup_K heineK; Theorem H for pure powers as hypothesis |
   | `SlowFactor`, `logL_slow`, `exists_rhoMin`, `lower_pair`, `upper_pair`, `cutAtom` | (L1)–(L3), H5, H6(a) | hypotheses on L and pair bounds |
   | `heineK_slow_le`, `slow_bdd`, `exponent_identity`, `log_upperTerm_le`, `HL_upper` | H7 + H_L upper | upper half |
   | `rhoSeq`, `rho_sum_asymp`, `HL_lower` | H_L lower | lower half |
   | **`theoremHL`** | **Theorem H_L** | **PROVED-mod-input (TheoremHPure)** |
   | `lemmaP` | Lemma P | α ≥ 2β |
   ```

2. In the "Not here" paragraph of `lean/README.md`, replace the Plan 3 line with:
   "Not here: Toeplitz eigenvalue count (Theorem B); Andreief/H2 and K → ∞ identification of heineD with the Hankel
   determinant of the infinite measure; the smooth-ζ instance of `SlowFactor`."
3. Top-level `README.md` status:
   "Lean: Theorem H_L proved from the named input Theorem H (Plans 2–3, lean/README.md)."
4. Spec §6 scope note: append "Plan 3 done: theoremHL, lemmaP. Toeplitz count and the ζ instance moved to the
   bridge plan."

- [ ] **Step 3: Full verification**

Run: `lean/check.sh && .venv/bin/python -m pytest -q`
Expected: `AUDIT OK`; Python green.

- [ ] **Step 4: Commit**

```bash
git add lean/README.md README.md docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md
git commit -m "docs: Theorem H_L formalized (mod named input Theorem H); Lemma P; scope notes

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

## After this plan

- **Bridge plan.**
  - Cauchy–Binet/Andreief: `heineK` equals the Hankel determinant of the truncation.
  - K → ∞ via moment convergence.
  - H2: the Hankel determinant is Π b_j^{2(n−j)}.
  - The Toeplitz count.
  - The smooth-ζ `SlowFactor` instance.
- **Research plans.** G3′, G2 and G1.
