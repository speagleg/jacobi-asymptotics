# JacobiAsym (Lean 4.34.1, Mathlib v4.34.1)

Sorry-free foundations for the deduction Theorem H (pure powers) ⇒ Theorem H_L (slowly varying atoms) of
math-pursuits item 11 (work/proof/PROOF.md §7b). D_n is represented by the Heine sum `heineK x w K n` (truncation to range K) and its supremum `heineD`. The
identities heineK = Hankel determinant of the truncation (`heineK_eq_det`, Andreief) and heineD = Hankel determinant
of the infinite measure (`heineD_eq_det`, K → ∞) are proved here. Only Theorem H for pure powers (`TheoremHPure`)
remains a named input.

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
| `heineD`, `TheoremHPure` (NAMED INPUT), `hnorm` | Thm H (input) | D_n = sup_K heineK; Theorem H for pure powers as hypothesis |
| `SlowFactor`, `logL_slow`, `exists_rhoMin`, `lower_pair`, `upper_pair`, `cutAtom` | (L1)–(L3), H5, H6(a) | hypotheses on L and pair bounds |
| `heineK_slow_le`, `slow_bdd`, `exponent_identity`, `log_upperTerm_le`, `HL_upper` | H7 + H_L upper | upper half |
| `rhoSeq`, `cesaro_weighted_zero`, `HL_lower` | H_L lower | lower half |
| **`theoremHL`** | **Theorem H_L** | **PROVED-mod-input (TheoremHPure; input available for p ∈ {1,2}, s ≥ s0(p))** |
| `lemmaP` | Lemma P | α ≥ 2β |
| `det_mul_cauchyBinet` | (Cauchy–Binet) | det(AB) = Σ_S det A_S det B_S for rectangular real matrices |
| `hankelK`, `heineK_eq_det` | H1 (Andreief/Heine) | truncated Heine sum = Hankel determinant of the truncated measure |
| `hankel`, `heineD_eq_det`, `heineK_bdd_of_summable` | H1, K → ∞ | heineD = det(∑' w x^{i+j}) for summable w ≥ 0, bounded x |
| `N0`, `zetaGamma`, `zetaGamma_spec`, `zetaGamma_hasDerivAt` | smooth ζ model | γ = N₀⁻¹(ξ − ½) without Lambert W; γ ≥ 9, derivative 2π/log(γ/2π) |
| `zetaL`, `zetaL_eps_eq`, `zetaL_slowFactor` | Cor. H_L-ζ hypotheses | exact ε = (ℓ/2 + 2γ² − (11π/2)γ)/(ℓ(γ²+¼)); SlowFactor 2 instance |
| `DMeasure`, `dip`, `mom`, `dip_self_eq_zero`, `hankel_det_pos` | (S1)–(S2) | discrete inner product, positive definiteness, D_n > 0 |
| `opoly`, `dip_opoly_pow`, `dip_opoly_pow_self`, `opoly_monic` | monic OPs | determinant formula; orthogonality; ⟨P_k, X^k⟩ = D_{k+1}/D_k |
| `jb2`, `ja`, `opoly_recurrence` | three-term recurrence | X P_k = P_{k+1} + a_k P_k + b_k² P_{k−1}, b_k² = D_{k+1}D_{k−1}/D_k² |
| `hankel_det_eq_prod` | H2 | D_n = m₀ⁿ Π_{j<n} (b_j²)^{n−j} |
| `sum_log_weighted_asymp` | (Stirling-type sum) | Σ_{j<n}(n−j) log j = n²/2 log n − 3n²/4 + o(n²) |
| `smoothZeta_HL_sumForm` | Cor. H_L-ζ, sum form | log D_n = −2n² log n + 2Σ_{j=1}^{n−1}(n−j) log L(j) + κn² + o(n²); PROVED-mod-input |
| **`smoothZeta_bLaw`** | **b_j form of Cor. H_L-ζ** | **(2/n²)Σ(n−j) log(b_j/x_j) → log(π²/16); PROVED-mod-input (TheoremHPure 2 κ 2, κ = 3 + log(π²/16))** |
| **`smoothZeta_HL`, `smoothZeta_HL_det`** | **Corollary H_L-ζ** | **smooth-ζ measure, Hankel-determinant form; PROVED-mod-input (TheoremHPure 2 κ 2)** |

Not here: the Toeplitz eigenvalue count (Plan 6). The true-zero measure (G3′) is research.

Check: `./check.sh` (build + axioms audit + completeness list; prints AUDIT OK).
