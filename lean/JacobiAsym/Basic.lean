import Mathlib

/-! Conventions for the JacobiAsym library (see docs/superpowers/plans/2026-10-13-plan-2-lean-foundations.md).
Atoms `x k`, weights `w k` are indexed by `k : ℕ`; index `k` is the `(k+1)`-th atom of math-pursuits item 11.
Configurations are `Finset ℕ`; pairs `(a, b)` with `a < b`. -/

namespace JacobiAsym

theorem scaffold_ok : (1 : ℕ) + 1 = 2 := rfl

end JacobiAsym
