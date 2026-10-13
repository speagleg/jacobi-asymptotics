# JacobiAsym (Lean 4.34.1, Mathlib v4.34.1)

Sorry-free foundations for the deduction Theorem H (pure powers) ⇒ Theorem H_L (slowly varying atoms) of
math-pursuits item 11 (work/proof/PROOF.md §7b). The Hankel determinant of the truncation Σ_{k<K} w_k δ_{x_k} is
represented by the finite Heine sum `heineK x w K n`; the identity heineK = Hankel determinant (Andreief) and the
passage K → ∞ to D_n of the infinite measure are NOT proved here.

| Lean | Item 11 | Content |
|---|---|---|
| `heineK`, `heineTerm`, `pairs`, `card_pairs` | H1 (definition side) | Heine sum over n-subsets of range K |
| `heineK_mono_K`, `heineK_mono_w`, `heineK_smul_w` | H3 | monotone in atoms set and weights; weight scaling |
| `heineTerm_le_of_pair_le` | (uniform comparison) | uniform pair factor λ ⇒ λ^{n(n-1)} |
| `heineTerm_le_of_pair_le_split` | H_L upper bound | factor B·λ only on pairs with smaller index < a₀ ⇒ B^{2a₀n} λ^{n(n-1)} (O(n) cost, as in item 11) |
| `heineTerm_ge_of_pair_ge`, `orderEmb_ge` | H_L lower bound | monotone factor at the smaller index, k_i ≥ i |
| `sum_prod_powersetCard_le`, `factorial_le_prod_succ` | H7 steps 2–3 | e_m ≤ (Σw)^m (replaces Hadamard); N! ≤ Π(a+1) |
| `heineK_tail_split`, `heineTerm_tail_pointwise` | H7 steps 1–3 | head/tail split of the Heine sum |
| `ratio_bounds_of_deriv`, `diff_le_of_L_mono` | MVT step of H4/H5(i) | Cauchy-MVT ratio bounds; monotone-L upper bound (the Heine-level H4 comparison and the H5(ii) split at a₀ are Plan 3) |
| `weighted_cesaro_slow`, `slow_shift`, `sum_log_div_le` | H6(b), H6(d) | slow-variation limits |
| `neg_mul_log_le`, `phi_bound` | H7 steps 5–6 | the penalty φ_M ≤ A²/(4p log M) |

Not here (Plan 3): asymptotic assembly of Theorem H_L with Theorem H as a named input; Lemma P; Toeplitz count.
Not here (later): Andreief/Cauchy–Binet (heineK = Hankel determinant) and H2 (Hankel = Π b_j^{2(n-j)}).

Check: `./check.sh` (build + axioms audit + completeness list; prints AUDIT OK).
