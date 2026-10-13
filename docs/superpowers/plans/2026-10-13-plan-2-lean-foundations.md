# Plan 2: Lean foundations for Theorem H_L

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or
> superpowers:executing-plans to implement this plan task by task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a sorry-free Lean 4 library `JacobiAsym` containing every *finite* and *real-analysis* lemma that the
deduction "Theorem H (pure powers) ⇒ Theorem H_L (slowly varying atoms)" needs, with Hankel determinants represented
as Heine sums.

**Architecture:**
- **Defining D_n.** D_n is *defined* as the Heine sum Σ_{|S|=n} Π w · Π_{a<b}(x_a−x_b)² over n-subsets of
  `range K`, for finite K. Every inequality in item 11's proof of H_L (`PROOF.md` §7b) is termwise on configurations,
  so it is proved for finite K, uniformly in K.
- **No Hadamard inequality.** Mathlib v4.34.1 has neither Cauchy–Binet nor the Hadamard inequality. The tail bound
  of Lemma H7 therefore uses the elementary Heine-level bound (x_a−x_b)² ≤ X² together with
  Σ_{|T|=m} Π w ≤ (Σ w)^m, which yields the same estimate W^m X^{m(m−1)}.
- **Out of scope.** The asymptotic assembly (limits, sup over K, M → ∞, Theorem H as a named input) is Plan 3. The
  link from Heine sums to Hankel determinants and Jacobi coefficients (H1/H2, which needs Cauchy–Binet) is a later
  plan.

**Tech Stack:** Lean 4.34.1 and Mathlib v4.34.1, with `autoImplicit` off. The Mathlib build is reused from
`/root/.cache/math-pursuits-lake/packages` through a symlink.

**Spec:** `docs/superpowers/specs/2026-10-13-jacobi-asymptotics-design.md` §6 (Lean library, ambition level A) and
§11 step 3. Mathematical source: math-pursuits item 11 `work/proof/PROOF.md` §7b (Lemmas H5, H6, H7, Theorem H_L;
REVIEWED).

**Decomposition ruling (recorded here; spec §11 lists "Lean core" as one step).** The Lean core is split into three
plans:
- Plan 2 (this plan): foundations.
- Plan 3: assembly of H ⇒ H_L, plus Lemma P and the Toeplitz count.
- A later plan: the H1/H2 bridge to Hankel determinants and Jacobi coefficients.

Reason: each part ends in a sorry-free, independently checkable library, and the bridge needs Cauchy–Binet, which is
not in Mathlib.

**How TDD works in Lean here.** Each task's "failing test" is the exact theorem statement with a `sorry` proof:
`lake env lean <file>` must elaborate it and print `declaration uses 'sorry'`. That is RED: the statement is
well-typed but unproved. GREEN means the same command prints no warnings *and* `lean/check.sh` reports no `sorryAx`.
Every statement below was typechecked against Mathlib v4.34.1 on 2026-10-13, and each was checked by hand to be true
(edge cases noted). Proofs are given as strategies naming the Mathlib lemmas to use, because writing the tactic
script is the implementation work. If a named lemma has a different name or signature, find the replacement with
`exact?` or `#check` and record a ruling.

## Global Constraints

- Lean toolchain `leanprover/lean4:v4.34.1`; Mathlib `v4.34.1`. Do not edit the toolchain or Mathlib version.
- No `sorry`, `admit` or new `axiom` in any committed `.lean` file. `#print axioms` may show only `propext`,
  `Classical.choice` and `Quot.sound`.
- Use `export PATH=$HOME/.elan/bin:$PATH`. Never run `lake update`: it would re-resolve the shared Mathlib cache.
- Treat `/root/.cache/math-pursuits-lake/packages` as read-only. It is shared with math-pursuits. Only our own
  `lean/.lake/build` is written.
- Commit prefix `lean:`. Each commit ends with `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.
- Work on branch `plan-2-lean` (from `master`).
- Indexing convention: atoms are indexed by `ℕ` (index k ↔ the (k+1)-th atom of item 11). Configurations are
  `Finset ℕ`. Pairs are ordered by index, `a < b`.

## Review Focus

1. **Index off-by-one between Lean (0-based) and PROOF.md (1-based).** For example, "k_i ≥ i" becomes "the i-th
   smallest element (0-based) is ≥ i". Plan 3 depends on these exact forms. Each statement's docstring must state the
   convention.
2. **Natural-number subtraction** in `S.card - 1 - i`, `n - m` and `m * (m - 1)`. The statements are true with
   truncated subtraction, but proofs must not silently assume `≥`. Edge cases: n = 0, m = 0, m = n.
3. **`Real.log 0 = 0` in Mathlib.** `phi_bound` at t = 1 relies on it. The proof must handle t = 1 explicitly, not
   divide by 1 − t.
4. **The shared-cache symlink.** If `lake build` starts rebuilding Mathlib (hundreds of files), stop. The manifest or
   toolchain has drifted from math-pursuits. Do not let it overwrite the shared cache.
5. **Statements weaker than needed downstream.** Before proving, check that each statement is the form Plan 3 will
   apply: termwise and uniform in K, with explicit constants. Don't "simplify" a hypothesis away.

---

### Task 1: Lean project scaffold and audit script

**Files:**
- Create: `lean/lean-toolchain`, `lean/lakefile.lean`, `lean/lake-manifest.json` (copied and renamed),
  `lean/JacobiAsym.lean`, `lean/JacobiAsym/Basic.lean`, `lean/Audit.lean`, `lean/check.sh`
- Symlink: `lean/.lake/packages -> /root/.cache/math-pursuits-lake/packages`
- Modify: `PROVENANCE.md`, `AGENTS.md` (Lean section)

**Interfaces:**
- Produces: library `JacobiAsym` (root `lean/JacobiAsym.lean` imports every module) and `lean/check.sh`. The script
  exits 0 iff `lake build` succeeds and `Audit.lean`'s `#print axioms` output contains no `sorryAx`.

- [ ] **Step 1: Create the project**

```bash
cd /mnt/c/Users/gspea/source/repos/jacobi-asymptotics && git checkout -b plan-2-lean
mkdir -p lean/JacobiAsym lean/.lake
cp /mnt/c/Users/gspea/source/repos/math-pursuits/lean/lean-toolchain lean/
cp /mnt/c/Users/gspea/source/repos/math-pursuits/lean/lake-manifest.json lean/
sed -i 's/"name": "math_pursuits"/"name": "jacobi_asym"/' lean/lake-manifest.json
ln -sfn /root/.cache/math-pursuits-lake/packages lean/.lake/packages
```

`lean/lakefile.lean`:
```lean
import Lake
open Lake DSL

package «jacobi_asym» where
  leanOptions := #[⟨`autoImplicit, false⟩, ⟨`relaxedAutoImplicit, false⟩]

require "leanprover-community" / "mathlib" @ git "v4.34.1"

@[default_target]
lean_lib «JacobiAsym» where
```

`lean/JacobiAsym/Basic.lean`:
```lean
import Mathlib

/-! Conventions for the JacobiAsym library (see docs/superpowers/plans/2026-10-13-plan-2-lean-foundations.md).
Atoms `x k`, weights `w k` are indexed by `k : ℕ`; index `k` is the `(k+1)`-th atom of math-pursuits item 11.
Configurations are `Finset ℕ`; pairs `(a, b)` with `a < b`. -/

namespace JacobiAsym

theorem scaffold_ok : (1 : ℕ) + 1 = 2 := rfl

end JacobiAsym
```

`lean/JacobiAsym.lean`:
```lean
import JacobiAsym.Basic
```

`lean/Audit.lean`:
```lean
import JacobiAsym

#print axioms JacobiAsym.scaffold_ok
```

`lean/check.sh`:
```bash
#!/usr/bin/env bash
# Build the library and audit axioms: fails on any sorryAx or non-standard axiom.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/.elan/bin:$PATH"
lake build 2>&1 | tail -5
out=$(lake env lean Audit.lean 2>&1)
echo "$out"
if echo "$out" | grep -q "sorryAx"; then echo "FAIL: sorryAx present"; exit 1; fi
bad=$(echo "$out" | grep -o "depends on axioms: \[[^]]*\]" | tr -d '[]' | sed 's/depends on axioms: //' \
      | tr ',' '\n' | sed 's/ //g' | grep -v -E '^(propext|Classical.choice|Quot.sound)?$' || true)
if [ -n "$bad" ]; then echo "FAIL: non-standard axioms: $bad"; exit 1; fi
if echo "$out" | grep -qi "error"; then echo "FAIL: errors"; exit 1; fi
echo "AUDIT OK"
```

Run `chmod +x lean/check.sh`.

- [ ] **Step 2: Build and audit**

Run: `lean/check.sh`
Expected: the build completes in under ~2 minutes without compiling Mathlib, and the output ends with `AUDIT OK`.
`#print axioms JacobiAsym.scaffold_ok` prints "does not depend on any axioms".

If `lake build` starts compiling Mathlib files, stop: kill it and compare `lean/lake-manifest.json` with
math-pursuits' version (Review Focus #4).

- [ ] **Step 3: Docs and commit**

Append to `PROVENANCE.md`:
```
| lean/lean-toolchain, lean/lake-manifest.json | math-pursuits/lean/ | copied; package name changed to jacobi_asym |
```

In `AGENTS.md`, replace the line ``- Lean: `export PATH=$HOME/.elan/bin:$PATH`; Lean 4.34.1 and Mathlib v4.34.1
(Plan 2).`` with:
```
- Lean: `export PATH=$HOME/.elan/bin:$PATH`; Lean 4.34.1, Mathlib v4.34.1. `lean/.lake/packages` is a symlink to the
  shared read-only cache /root/.cache/math-pursuits-lake/packages; never run `lake update`. `lean/check.sh` = build +
  axioms audit (must print AUDIT OK). Check one file with `cd lean && lake env lean JacobiAsym/<File>.lean`.
```

```bash
git add lean/lean-toolchain lean/lakefile.lean lean/lake-manifest.json lean/JacobiAsym.lean lean/JacobiAsym lean/Audit.lean lean/check.sh PROVENANCE.md AGENTS.md
git commit -m "lean: project scaffold sharing the math-pursuits Mathlib cache, axioms audit script

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

(`lean/.lake` is gitignored, so the symlink is not committed. `scripts/setup_env.sh` gets the `ln -sfn` line in
Task 9.)

---

### Task 2: Heine sums: definitions and basic monotonicity

**Files:**
- Create: `lean/JacobiAsym/Heine.lean`
- Modify: `lean/JacobiAsym.lean` (import), `lean/Audit.lean` (print axioms)

**Interfaces:**
- Produces (namespace `JacobiAsym`):
  - `def pairs (S : Finset ℕ) : Finset (ℕ × ℕ)`
  - `noncomputable def heineTerm (x w : ℕ → ℝ) (S : Finset ℕ) : ℝ`
  - `noncomputable def heineK (x w : ℕ → ℝ) (K n : ℕ) : ℝ`
  - theorems `card_pairs`, `heineTerm_nonneg`, `heineK_mono_K`, `heineK_mono_w`, `heineK_smul_w` (statements below)

- [ ] **Step 1: Write the statements with `sorry`**

`lean/JacobiAsym/Heine.lean`:
```lean
import JacobiAsym.Basic

open Finset

namespace JacobiAsym

/-- Ordered pairs `(a, b)` of `S` with `a < b`. -/
def pairs (S : Finset ℕ) : Finset (ℕ × ℕ) := (S ×ˢ S).filter (fun p => p.1 < p.2)

/-- Heine term of configuration `S`: `(∏_{i∈S} w i) * ∏_{a<b in S} (x a - x b)^2`. -/
noncomputable def heineTerm (x w : ℕ → ℝ) (S : Finset ℕ) : ℝ :=
  (∏ i ∈ S, w i) * ∏ p ∈ pairs S, (x p.1 - x p.2) ^ 2

/-- Heine sum over `n`-subsets of `range K` (= the `n × n` Hankel determinant of `∑_{k<K} w k δ_{x k}`,
by Andreief; that identity is NOT used or proved here). -/
noncomputable def heineK (x w : ℕ → ℝ) (K n : ℕ) : ℝ :=
  ∑ S ∈ (range K).powersetCard n, heineTerm x w S

theorem card_pairs (S : Finset ℕ) : (pairs S).card = S.card * (S.card - 1) / 2 := by
  sorry

theorem heineTerm_nonneg {x w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) (S : Finset ℕ) : 0 ≤ heineTerm x w S := by
  sorry

theorem heineK_mono_K {x w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {K K' : ℕ} (hK : K ≤ K') (n : ℕ) :
    heineK x w K n ≤ heineK x w K' n := by
  sorry

theorem heineK_mono_w {x w w' : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) (hww : ∀ i, w i ≤ w' i) (K n : ℕ) :
    heineK x w K n ≤ heineK x w' K n := by
  sorry

theorem heineK_smul_w (x w : ℕ → ℝ) (c : ℝ) (K n : ℕ) :
    heineK x (fun i => c * w i) K n = c ^ n * heineK x w K n := by
  sorry

end JacobiAsym
```

Add `import JacobiAsym.Heine` to `lean/JacobiAsym.lean`. Append these lines to `lean/Audit.lean`:
```lean
#print axioms JacobiAsym.card_pairs
#print axioms JacobiAsym.heineTerm_nonneg
#print axioms JacobiAsym.heineK_mono_K
#print axioms JacobiAsym.heineK_mono_w
#print axioms JacobiAsym.heineK_smul_w
```

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/Heine.lean`
Expected: 5 warnings `declaration uses 'sorry'` and no errors. Then `lean/check.sh` must exit non-zero with
`FAIL: sorryAx present`.

- [ ] **Step 3: Prove**

Strategies:
- `card_pairs`: `pairs S` is in bijection with `S.powersetCard 2` (the map `p ↦ {p.1, p.2}`). Use
  `Finset.card_powersetCard` and `Nat.choose_two_right`. Alternatively, induct on `S` with `Finset.induction_on_max`:
  adding a new maximum `m` adds the pairs `(a, m)` for `a ∈ S`, and then check `n(n-1)/2 + n = (n+1)n/2` with
  `Nat.div_add_div_same`/`omega`-friendly rewriting via `Nat.succ_mul`.
- `heineTerm_nonneg`: `mul_nonneg (prod_nonneg fun i _ => hw i) (prod_nonneg fun p _ => sq_nonneg _)`.
- `heineK_mono_K`: `sum_le_sum_of_subset_of_nonneg (powersetCard_mono (range_subset.2 hK))` with
  `heineTerm_nonneg hw`.
- `heineK_mono_w`: `sum_le_sum` and then `mul_le_mul_of_nonneg_right (prod_le_prod (fun i _ => hw i) (fun i _ => hww i))`
  `(prod_nonneg fun _ _ => sq_nonneg _)`.
- `heineK_smul_w`: unfold, `mul_sum`. For `S ∈ powersetCard n`, `prod_mul_distrib` and `prod_const` give
  `c ^ S.card` with `(mem_powersetCard.1 hS).2`; finish with `ring`.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/Heine.lean && ./check.sh`
Expected: no warnings from the first command; `AUDIT OK` from the second.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/Heine.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: Heine sums (finite), card of pairs, nonnegativity, monotonicity in K and w, weight scaling

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Termwise comparison of Heine terms (constant and rank-dependent factors)

**Files:**
- Create: `lean/JacobiAsym/HeineCompare.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Consumes: `pairs`, `heineTerm`, `card_pairs` (Task 2).
- Produces:
  - `heineTerm_le_of_pair_le`: a uniform pair factor `lam` gives `lam ^ (n*(n-1))`. This is the upper bound of
    Theorem H_L, with `lam = B'·L(Mn)` in Plan 3.
  - `heineTerm_ge_of_pair_ge`: a monotone pair factor `ρ` evaluated at the *smaller* index gives
    `∏_{i<n} ρ i ^ (2(n-1-i))`. This is the lower bound of Theorem H_L: in item 11's 1-based language, k_i ≥ i and
    pair (i, j) contributes ρ(k_i)².
  - Helper `orderEmb_ge`: the i-th smallest element of `S` (0-based) is ≥ i.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.Heine

open Finset

namespace JacobiAsym

/-- The `i`-th smallest element (0-based) of a finset of naturals is at least `i`. -/
theorem orderEmb_ge (S : Finset ℕ) {n : ℕ} (h : S.card = n) (i : Fin n) : (i : ℕ) ≤ S.orderEmbOfFin h i := by
  sorry

/-- Uniform pair comparison: if every pair satisfies `(x a - x b)^2 ≤ lam^2 (y a - y b)^2`, then
`heineTerm x ≤ lam^(n(n-1)) heineTerm y`, `n = |S|`. -/
theorem heineTerm_le_of_pair_le {x y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {lam : ℝ} (hlam : 0 ≤ lam)
    {S : Finset ℕ} (h : ∀ a ∈ S, ∀ b ∈ S, a < b → (x a - x b) ^ 2 ≤ lam ^ 2 * (y a - y b) ^ 2) :
    heineTerm x w S ≤ lam ^ (S.card * (S.card - 1)) * heineTerm y w S := by
  sorry

/-- Rank-dependent lower comparison: if `ρ ≥ 0` is monotone and every pair `a < b` satisfies
`ρ a ^ 2 (y a - y b)^2 ≤ (x a - x b)^2`, then `(∏_{i<n} ρ i ^ (2(n-1-i))) heineTerm y ≤ heineTerm x`
(0-based ranks: the `i`-th smallest element is `≥ i` and is the smaller index of exactly `n-1-i` pairs). -/
theorem heineTerm_ge_of_pair_ge {x y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {ρ : ℕ → ℝ}
    (hρ0 : ∀ i, 0 ≤ ρ i) (hρ : Monotone ρ) {S : Finset ℕ}
    (h : ∀ a ∈ S, ∀ b ∈ S, a < b → ρ a ^ 2 * (y a - y b) ^ 2 ≤ (x a - x b) ^ 2) :
    (∏ i ∈ range S.card, ρ i ^ (2 * (S.card - 1 - i))) * heineTerm y w S ≤ heineTerm x w S := by
  sorry

end JacobiAsym
```

Add the import and three `#print axioms` lines.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/HeineCompare.lean`
Expected: 3 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `orderEmb_ge`: induct on `i`. Use `OrderEmbedding.strictMono` (`S.orderEmbOfFin h`), so `f i < f (i+1)` in ℕ, and
  `Nat.succ_le_of_lt`. The base case is `Nat.zero_le`. In practice, prove `∀ k (hk : k < n), k ≤ f ⟨k, hk⟩` by
  `Nat.rec` on `k`.
- `heineTerm_le_of_pair_le`:
  1. Unfold `heineTerm`. The weight factors coincide, so it suffices to show
     `∏_{p∈pairs S}(x..)^2 ≤ ∏_{p∈pairs S} lam^2 (y..)^2`. Use `prod_le_prod` with nonnegativity `sq_nonneg`; the
     pointwise hypothesis comes from `mem_filter` and `mem_product`.
  2. Then `prod_mul_distrib` and `prod_const` give `lam ^ (2 * (pairs S).card)`.
  3. `card_pairs`: `2 * (n*(n-1)/2) = n*(n-1)` holds because `n*(n-1)` is even. Use `Nat.even_mul_pred_self` with
     `Nat.two_mul_div_two_of_even`.
  4. Close the remaining reordering with `mul_le_mul_of_nonneg_left` and `ring_nf`.
- `heineTerm_ge_of_pair_ge`:
  1. Write `∏_{p∈pairs S} ρ(p.1)^2 = ∏_{a∈S} ρ a ^ (2 * #{b∈S | a<b})`. Use `prod_filter` and
     `prod_product`/`prod_sigma`-style regrouping (`Finset.prod_product` on `S ×ˢ S` with the filter moved inside as
     `if`), then `prod_pow_eq_pow_sum` and `prod_const`.
  2. Re-index `S` by `S.orderEmbOfFin h` (`Finset.prod_map`, or `prod_bij` with the embedding). The element of rank i
     has exactly `n-1-i` larger elements: `card_filter_lt` via the order embedding. Its value is `≥ i`
     (`orderEmb_ge`), so `ρ i ≤ ρ (f i)` by `hρ`.
  3. Combine with `prod_le_prod` and `pow_le_pow_left` (nonnegativity from `hρ0`). Multiply by the pointwise pair
     inequality, as in the previous lemma but reversed.

  The `range S.card` product in the statement is the re-indexed form; convert with `Fin.prod_univ_eq_prod_range`.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/HeineCompare.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/HeineCompare.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: termwise Heine comparisons (uniform factor; monotone rank-dependent factor) and rank lemma

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Combinatorial bounds (elementary symmetric sum and factorial)

**Files:**
- Create: `lean/JacobiAsym/Combinatorics.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Consumes: `orderEmb_ge` (Task 3).
- Produces:
  - `sum_prod_powersetCard_le`: e_m(w|_s) ≤ (Σ_s w)^m. Replaces the Hadamard bound in H7.
  - `factorial_le_prod_succ`: N! ≤ Π_{a∈S}(a+1) for |S| = N. This is the (N!)^{−2pm} step of H7.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.HeineCompare

open Finset

namespace JacobiAsym

/-- `e_m(w restricted to s) ≤ (∑_{b∈s} w b)^m` for nonnegative weights (true also for `m = 0`). -/
theorem sum_prod_powersetCard_le {w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) (s : Finset ℕ) (m : ℕ) :
    ∑ T ∈ s.powersetCard m, ∏ b ∈ T, w b ≤ (∑ b ∈ s, w b) ^ m := by
  sorry

/-- `N! ≤ ∏_{a∈S} (a+1)` when `|S| = N` (the `i`-th smallest element is `≥ i`). -/
theorem factorial_le_prod_succ (S : Finset ℕ) : ((S.card).factorial : ℝ) ≤ ∏ a ∈ S, ((a : ℝ) + 1) := by
  sorry

end JacobiAsym
```

Add the import and two `#print axioms` lines.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/Combinatorics.lean`
Expected: 2 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `sum_prod_powersetCard_le`: induct on `s` with `Finset.induction_on`.
  - Use `powersetCard_succ_insert` (or `Finset.powersetCard_insert`): for `a ∉ s`, the m-subsets of `insert a s`
    are the m-subsets of s together with `insert a` applied to the (m−1)-subsets of s.
  - So `e_m(insert a s) = e_m(s) + w a · e_{m-1}(s)`, while `(w a + W)^m ≥ W^m + w a · W^(m-1)` for m ≥ 1 by the
    binomial expansion with nonnegative terms (`add_pow_le_pow_mul_pow_of_sq_le_sq` is not needed; use
    `add_pow` and keep two terms with `single_le_sum`, or prove `W^m + a W^(m-1) ≤ (a+W)^m` by induction on m).
  - Handle m = 0 separately (`powersetCard_zero`, both sides 1). Alternatively, Mathlib's
    `Finset.prod_add`/`Finset.sum_pow` expansion with `Finset.sum_le_sum_of_subset_of_nonneg` may give it directly.
    Try `exact?` first.
- `factorial_le_prod_succ`:
  1. Re-index by `S.orderEmbOfFin rfl` (`Finset.prod_map` / `prod_bij`).
  2. `∏_{i<N} ((f i : ℝ) + 1) ≥ ∏_{i<N} ((i : ℝ) + 1) = N!`, using `orderEmb_ge` and `prod_le_prod`, cast with
     `Nat.cast_le`.
  3. `Finset.prod_range_add_one_eq_factorial` (`∏_{i<N}(i+1) = N!`) and `Nat.cast_prod`.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/Combinatorics.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/Combinatorics.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: elementary-symmetric bound e_m <= (sum w)^m and N! <= prod (a+1)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Tail-split bound (Lemma H7, finite combinatorial core)

**Files:**
- Create: `lean/JacobiAsym/TailCut.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Consumes: `heineTerm`, `heineK`, `pairs`, `card_pairs` (Task 2); `sum_prod_powersetCard_le` (Task 4).
- Produces: `heineK_tail_split`, the finite form of item 11's Lemma H7 steps 1–3. Head = indices `< K0`; tail =
  `Ico K0 K` with atoms in `(0, X]` below every head atom. Plan 3 combines it with `factorial_le_prod_succ` and
  Theorem H for the head.

- [ ] **Step 1: Write the statement with `sorry`**

```lean
import JacobiAsym.Combinatorics

open Finset

namespace JacobiAsym

/-- Lemma H7 core.  Split each `n`-subset `S ⊆ range K` into head `S ∩ range K0` (size `n - m`) and tail
`S ∩ Ico K0 K` (size `m`).  Cross pairs: `0 < y b ≤ y a` gives `(y a - y b)^2 ≤ (y a)^2`; tail pairs: `(y b - y b')^2 ≤ X^2`;
tail weights: `e_m ≤ (∑ w)^m`. -/
theorem heineK_tail_split {y w : ℕ → ℝ} (hw : ∀ i, 0 ≤ w i) {K0 K n : ℕ} (hK : K0 ≤ K) {X : ℝ}
    (hpos : ∀ i, 0 < y i) (htail : ∀ b, K0 ≤ b → y b ≤ X) (hord : ∀ a b, a < K0 → K0 ≤ b → y b ≤ y a) :
    heineK y w K n ≤ ∑ m ∈ range (n + 1),
      (∑ SH ∈ (range K0).powersetCard (n - m), heineTerm y w SH * ∏ a ∈ SH, y a ^ (2 * m)) *
      (∑ b ∈ Ico K0 K, w b) ^ m * X ^ (m * (m - 1)) := by
  sorry

end JacobiAsym
```

Add the import and `#print axioms JacobiAsym.heineK_tail_split`.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/TailCut.lean`
Expected: 1 `sorry` warning and no errors.

- [ ] **Step 3: Prove**

1. **Pointwise bound.** For `S ⊆ range K`, let `SH = S.filter (· < K0)` and `ST = S.filter (K0 ≤ ·)`, so
   `S = SH ∪ ST` (disjoint) and `m = ST.card`. Then

       heineTerm y w S ≤ heineTerm y w SH * (∏_{a∈SH} y a^(2m)) * (∏_{b∈ST} w b) * X^(m(m-1)).

   - `pairs S = pairs SH ∪ pairs ST ∪ cross`, where `cross = SH ×ˢ ST`. Every cross pair has its first index in the
     head, because a < K0 ≤ b.
   - Products split with `prod_union` (disjointness via `disjoint_filter`).
   - Cross factor: `(y a - y b)^2 ≤ (y a)^2`, because `0 ≤ y a - y b ≤ y a` (`hord`, `hpos`). So
     `∏_{cross} ≤ ∏_{a∈SH} (y a)^(2·|ST|)` (`prod_product`, `prod_const`).
   - Tail factor: `|y b - y b'| ≤ X` with both in `(0, X]` (`abs_sub_le_iff` and `htail`). So the factor is
     `≤ X^(2·#pairs ST) = X^(m(m-1))` by `card_pairs` and evenness, as in Task 3. If `ST` is empty then m = 0 and
     the factor is 1. If `ST` is nonempty then `X > 0` (from `hpos`, `htail`), so the powers are monotone.
2. **Sum.** Re-index `∑_{S ∈ powersetCard n (range K)}` as
   `∑_{m ≤ n} ∑_{SH ∈ powersetCard (n-m) (range K0)} ∑_{ST ∈ powersetCard m (Ico K0 K)}`. The map
   `S ↦ (SH, ST)` is a bijection onto these pairs, and `range K = range K0 ∪ Ico K0 K` (`range_eq_Ico`,
   `Ico_union_Ico_eq_Ico`). Use `Finset.sum_bij`/`sum_nbij'`, or prove `≤` directly with
   `sum_le_sum_of_subset_of_nonneg` after mapping. Only `≤` is needed, so an injection into the triple sum suffices.
3. Bound the inner `∑_{ST} ∏ w` by `(∑_{Ico K0 K} w)^m` with `sum_prod_powersetCard_le`.

This is the longest proof in the plan. Put helper lemmas (`pairs_union_split`, `cross_factor_le`,
`tail_factor_le`) in the same file, each with its own `#print axioms` line.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/TailCut.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/TailCut.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: Lemma H7 finite core — Heine tail split with cross-pair, tail-pair and e_m bounds

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Difference-ratio bounds (Lemma H5)

**Files:**
- Create: `lean/JacobiAsym/RatioBounds.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Produces:
  - `ratio_bounds_of_deriv`: Cauchy MVT in the two-sided form used by H4 and H5.
  - `diff_le_of_L_mono`: the algebraic upper bound of H5(i).
  - `diff_ge_of_deriv_lower`: the lower bound of H5(i) from a pointwise derivative bound.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
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
  sorry

/-- H5(i) upper bound: if `L a ≤ L b` then `a^{-p} L a - b^{-p} L b ≤ L a (a^{-p} - b^{-p})`. -/
theorem diff_le_of_L_mono {L : ℝ → ℝ} {a b p : ℝ} (ha : 0 < a) (hab : a < b) (hp : 0 < p)
    (hL : L a ≤ L b) :
    a ^ (-p) * L a - b ^ (-p) * L b ≤ L a * (a ^ (-p) - b ^ (-p)) := by
  sorry

end JacobiAsym
```

The lower bound of H5(i) is `ratio_bounds_of_deriv` applied with `lo = (1 - ε*(a)/p) L(a)`. Plan 3 instantiates it;
no separate lemma is needed (YAGNI).

Add the import and two `#print axioms` lines.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/RatioBounds.lean`
Expected: 2 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `ratio_bounds_of_deriv`:
  1. `exists_ratio_hasDerivAt_eq_ratio_slope f f' hab hf hf' g g' hg hg'` gives `c ∈ Ioo a b` with
     `(g b - g a) * f' c = (f b - f a) * g' c`.
  2. Let `d = -g' c > 0`, so `f a - f b = (g a - g b) * (-f' c) / d`.
  3. The bounds follow from `hlo c` and `hhi c` multiplied by `(g a - g b) / d ≥ 0`.
  4. Nonnegativity: `g a - g b > 0`, because `g` is strictly antitone on `[a,b]`
     (`strictAntiOn_of_deriv_neg` needs `deriv`; use instead the MVT `exists_hasDerivAt_eq_slope` on g:
     `g b - g a = g'(c')(b-a) < 0`).
  5. Finish with `div_le_iff₀`/`le_div_iff₀` and `nlinarith`.
- `diff_le_of_L_mono`: `L b * b^(-p) ≥ L a * b^(-p)`, because `b^(-p) > 0` (`Real.rpow_pos_of_pos`). Rearrange:
  `nlinarith [mul_le_mul_of_nonneg_right hL (le_of_lt (Real.rpow_pos_of_pos (ha.trans hab) (-p)))]`. The
  hypothesis `hp` is not needed; keep it for the call-site shape, or drop it and record a ruling.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/RatioBounds.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/RatioBounds.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: Lemma H5 — Cauchy-MVT ratio bounds and the monotone-L upper bound

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Slow variation (Lemma H6)

**Files:**
- Create: `lean/JacobiAsym/SlowVariation.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Produces:
  - `weighted_cesaro_slow`: H6(b),
    (2/n²) Σ_{1≤i<n} (n−i)(ℓ(i) − ℓ(n)) → 0.
  - `slow_shift`: H6(d), ℓ(Mn) − ℓ(n) → 0.

  Both take the abstract hypothesis |ℓ y − ℓ x| ≤ E(x)·log(y/x) for 1 ≤ x ≤ y, with E ≥ 0 antitone and E → 0.
  That hypothesis is H6(a), which Plan 3 derives from ε(ξ) = ξL′/L by the mean value theorem. Here ℓ stands for
  log L.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.Basic

open Finset Filter Topology

namespace JacobiAsym

/-- Lemma H6(b): `(2/n²) ∑_{1≤i<n} (n-i)(ℓ i - ℓ n) → 0` under `|ℓ y - ℓ x| ≤ E x · log (y/x)` (`1 ≤ x ≤ y`),
`E ≥ 0` antitone, `E → 0`. -/
theorem weighted_cesaro_slow {ℓ E : ℝ → ℝ} (hE0 : ∀ x, 0 ≤ E x) (hEanti : Antitone E)
    (hE : Tendsto E atTop (𝓝 0))
    (hℓ : ∀ x y : ℝ, 1 ≤ x → x ≤ y → |ℓ y - ℓ x| ≤ E x * Real.log (y / x)) :
    Tendsto (fun n : ℕ => (2 * ∑ i ∈ Ico 1 n, ((n : ℝ) - i) * (ℓ i - ℓ n)) / (n : ℝ) ^ 2) atTop (𝓝 0) := by
  sorry

/-- Lemma H6(d): `ℓ (M n) - ℓ n → 0` for fixed `M ≥ 1`. -/
theorem slow_shift {ℓ E : ℝ → ℝ} (hE : Tendsto E atTop (𝓝 0))
    (hℓ : ∀ x y : ℝ, 1 ≤ x → x ≤ y → |ℓ y - ℓ x| ≤ E x * Real.log (y / x)) (M : ℝ) (hM : 1 ≤ M) :
    Tendsto (fun n : ℕ => ℓ (M * n) - ℓ n) atTop (𝓝 0) := by
  sorry

end JacobiAsym
```

Add the import and two `#print axioms` lines.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/SlowVariation.lean`
Expected: 2 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `slow_shift`:
  - For `n ≥ 1`: `|ℓ(Mn) − ℓ(n)| ≤ E(n)·log M` (`hℓ n (M n)`, with `M n / n = M` by `field_simp`).
  - `E(n)·log M → 0` (`hE.comp tendsto_natCast_atTop_atTop`, `Tendsto.mul_const`).
  - Squeeze with `squeeze_zero_norm'` and `eventually_atTop`.
- `weighted_cesaro_slow`:
  1. Bound the absolute value by `(2/n)·Σ_{1≤i<n} E(i)·log(n/i)`, using `n − i ≤ n` and `hℓ i n`.
  2. Fix η > 0 and choose X with E ≤ η beyond X (and E(1) ≥ E(i) for i ≥ 1 by antitonicity).
  3. Split the sum at X: the head is ≤ X·E(1)·log n, and the tail is ≤ η·Σ_{i<n} log(n/i).
  4. Use `Σ_{1≤i<n} log(n/i) ≤ n`. This holds because Σ_{i=1}^{n} log(n/i) = n log n − log n! ≤ n, using
     `Real.log_factorial`-type bounds or Stirling's lower bound `n! ≥ (n/e)^n` (`Nat.factorial` with
     `Real.exp_one_lt_d9`; Mathlib has `Stirling.le_factorial`/`Nat.pow_div_exp_le_factorial`-style lemmas; check with
     `exact?` on `(n:ℝ)^n / Real.exp n ≤ n.factorial`).
  5. So limsup ≤ 2η, and `(log n)/n → 0` (`Real.tendsto_log_div...` or `isLittleO_log_id_atTop`) kills the head.
  6. Conclude with `Metric.tendsto_atTop` and the ε–N form.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/SlowVariation.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/SlowVariation.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: Lemma H6 — weighted Cesaro slow-variation limit and shift lemma

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 8: The Lemma H7 penalty φ_M

**Files:**
- Create: `lean/JacobiAsym/Penalty.lean`
- Modify: `lean/JacobiAsym.lean`, `lean/Audit.lean`

**Interfaces:**
- Produces:
  - `neg_mul_log_le`: −(1−t)·log(1−t) ≤ t on [0,1].
  - `phi_bound`: φ_M(t) ≤ A²/(4p log M) with A = 4p + 2|κ|. This is exactly the expression in item 11 Lemma H7 step 5,
    and Plan 3 consumes it.

- [ ] **Step 1: Write the statements with `sorry`**

```lean
import JacobiAsym.Basic

namespace JacobiAsym

/-- `-(1-t) log (1-t) ≤ t` on `[0,1]` (at `t = 1` both sides use `Real.log 0 = 0`). -/
theorem neg_mul_log_le {t : ℝ} (ht0 : 0 ≤ t) (ht1 : t ≤ 1) : -((1 - t) * Real.log (1 - t)) ≤ t := by
  sorry

/-- Lemma H7 penalty: `φ_M(t) ≤ A²/(4 p log M)`, `A = 4p + 2|κ|`, for `t ∈ [0,1]`, `p > 0`, `M > 1`. -/
theorem phi_bound {p κ M t : ℝ} (hp : 0 < p) (hM : 1 < M) (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    -p * (1 - t ^ 2) * Real.log (1 - t) + 2 * p * t * (1 - t) - κ * t * (2 - t) - p * t ^ 2 * Real.log M
      ≤ (4 * p + 2 * |κ|) ^ 2 / (4 * p * Real.log M) := by
  sorry

end JacobiAsym
```

Add the import and two `#print axioms` lines.

- [ ] **Step 2: Confirm RED**

Run: `cd lean && lake env lean JacobiAsym/Penalty.lean`
Expected: 2 `sorry` warnings and no errors.

- [ ] **Step 3: Prove**

- `neg_mul_log_le`: with u = 1 − t ∈ [0,1], prove `-(u * log u) ≤ 1 - u`.
  - At u = 0: `Real.log_zero`, so 0 ≤ 1.
  - At u > 0: `Real.log_le_sub_one_of_pos` applied to 1/u gives `log(1/u) ≤ 1/u − 1`. Multiply by u:
    `-u log u ≤ 1 − u`. Use `Real.log_inv` and `nlinarith`/`field_simp`.
- `phi_bound`: let `h(t) := -p(1-t²)log(1-t) + 2pt(1-t) - κt(2-t)` and `A := 4p+2|κ|`.
  1. `h(t) ≤ A t`, because:
     - `-p(1-t²)log(1-t) = p(1+t)·(-(1-t)log(1-t)) ≤ p(1+t)t ≤ 2pt`, by `neg_mul_log_le` and `t ≤ 1`;
     - `2pt(1-t) ≤ 2pt`;
     - `-κt(2-t) ≤ |κ|·2t`, by `neg_abs_le` and `0 ≤ t(2-t) ≤ 2t`.
  2. `A t - p t² log M ≤ A²/(4 p log M)`, which is `(2 p log M · t - A)² ≥ 0` divided by `4 p log M > 0`
     (`Real.log_pos hM`). Use `div_le_iff₀` plus `nlinarith [sq_nonneg (2*p*Real.log M*t - A)]`.

- [ ] **Step 4: Confirm GREEN**

Run: `cd lean && lake env lean JacobiAsym/Penalty.lean && ./check.sh`
Expected: no warnings; `AUDIT OK`.

- [ ] **Step 5: Commit**

```bash
git add lean/JacobiAsym/Penalty.lean lean/JacobiAsym.lean lean/Audit.lean
git commit -m "lean: Lemma H7 penalty bound phi_M(t) <= A^2/(4 p log M)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 9: Integration: environment script, documentation, full audit

**Files:**
- Modify: `scripts/setup_env.sh`, `README.md`, `lean/Audit.lean` (completeness check)
- Create: `lean/README.md`

**Interfaces:**
- Consumes: every theorem from Tasks 2–8.
- Produces: a documented Lean library. `lean/README.md` maps each Lean theorem to its item-11 lemma, so Plan 3 can
  start from it.

- [ ] **Step 1: Write the completeness check (RED)**

Append to `lean/check.sh`, before the final `echo "AUDIT OK"`:
```bash
need="card_pairs heineTerm_nonneg heineK_mono_K heineK_mono_w heineK_smul_w orderEmb_ge heineTerm_le_of_pair_le heineTerm_ge_of_pair_ge sum_prod_powersetCard_le factorial_le_prod_succ heineK_tail_split ratio_bounds_of_deriv diff_le_of_L_mono weighted_cesaro_slow slow_shift neg_mul_log_le phi_bound"
for t in $need; do
  echo "$out" | grep -q "JacobiAsym.$t" || { echo "FAIL: $t not audited"; exit 1; }
done
```

Run: `lean/check.sh`
Expected: PASS if Tasks 2–8 added every audit line. If one is missing, the script prints
`FAIL: <name> not audited`. Add the line and re-run.

(To see the check work, run it once with a deliberately misspelled name in `need` and confirm the FAIL line, then
revert.)

- [ ] **Step 2: Environment and docs**

Insert into `scripts/setup_env.sh`, after `make -C csrc`:
```bash
mkdir -p lean/.lake && ln -sfn /root/.cache/math-pursuits-lake/packages lean/.lake/packages
```

`lean/README.md`:
```markdown
# JacobiAsym (Lean 4.34.1, Mathlib v4.34.1)

Sorry-free foundations for the deduction Theorem H (pure powers) ⇒ Theorem H_L (slowly varying atoms) of
math-pursuits item 11 (work/proof/PROOF.md §7b). D_n is represented by the finite Heine sum `heineK x w K n`.

| Lean | Item 11 | Content |
|---|---|---|
| `heineK`, `heineTerm`, `pairs` | H1 (definition side) | Heine sum over n-subsets of range K |
| `heineK_mono_K`, `heineK_mono_w`, `heineK_smul_w` | H3 | monotone in atoms set and weights; weight scaling |
| `heineTerm_le_of_pair_le` | H_L upper bound | uniform pair factor λ ⇒ λ^{n(n-1)} |
| `heineTerm_ge_of_pair_ge`, `orderEmb_ge` | H_L lower bound | monotone factor at the smaller index, k_i ≥ i |
| `sum_prod_powersetCard_le`, `factorial_le_prod_succ` | H7 steps 2–3 | e_m ≤ (Σw)^m (replaces Hadamard); N! ≤ Π(a+1) |
| `heineK_tail_split` | H7 steps 1–3 | head/tail split of the Heine sum |
| `ratio_bounds_of_deriv`, `diff_le_of_L_mono` | H4, H5 | Cauchy-MVT ratio bounds; monotone-L upper bound |
| `weighted_cesaro_slow`, `slow_shift` | H6(b), H6(d) | slow-variation limits |
| `neg_mul_log_le`, `phi_bound` | H7 step 5–6 | the penalty φ_M ≤ A²/(4p log M) |

Not here (Plan 3): asymptotic assembly of Theorem H_L with Theorem H as a named input; Lemma P; Toeplitz count.
Not here (later): Andreief/Cauchy–Binet (heineK = Hankel determinant) and H2 (Hankel = Π b_j^{2(n-j)}).

Check: `./check.sh` (build + axioms audit; prints AUDIT OK).
```

In the top-level `README.md`, change the line `Status: toolkit under construction (Plan 1). Lean core: Plan 2.
Research: research/G3prime, G2, G1.` to:
```
Status: toolkit done (Plan 1). Lean foundations done (Plan 2, lean/README.md); Lean assembly of Theorem H_L: Plan 3.
Research: research/G3prime, G2, G1.
```

- [ ] **Step 3: Full verification**

Run: `lean/check.sh && .venv/bin/python -m pytest -q`
Expected: `AUDIT OK`, and the Python suite still green (61 passed, 2 deselected).

- [ ] **Step 4: Commit**

```bash
git add scripts/setup_env.sh README.md lean/README.md lean/check.sh lean/Audit.lean
git commit -m "lean: completeness audit, setup symlink, docs mapping Lean theorems to item-11 lemmas

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

## Later plans

- **Plan 3, Lean assembly.**
  - `Inputs.lean`: structure `TheoremHPure p` stating Theorem H for atoms (k+1)^{-p} and weights (k+1)^{-s} as
    `Tendsto` statements about `heineK`, uniformly in K via sup.
  - From these and Plan 2's lemmas: Theorem H_L. Also Lemma P and the Toeplitz count.
- **Plan 4, H1/H2 bridge.** Cauchy–Binet for rectangular matrices, Andreief (`heineK` = Hankel determinant of the
  truncated measure), and H2.
- **Plans 5–7:** research G3′, G2 and G1.
