# JacobiAsym (Lean 4.34.1, Mathlib v4.34.1)

Sorry-free foundations for the deduction Theorem H (pure powers) ⇒ Theorem H_L (slowly varying atoms) of
math-pursuits item 11 (work/proof/PROOF.md §7b). D_n is represented by the Heine sum `heineK x w K n` (truncation to range K) and its supremum `heineD`. The
identities heineK = Hankel determinant of the truncation (`heineK_eq_det`, Andreief) and heineD = Hankel determinant
of the infinite measure (`heineD_eq_det`, K → ∞) are proved here. Only Theorem H for pure powers (`TheoremHPure`)
remains a named input. On paper, the input `TheoremHPure p κ_p s` (κ_p = 3p/2 + log c(p)) is supplied for all
p > 0, s > 1 by G2 Corollary H-input (research/G2/PROOF.md §3), citation-free since Plan 47 (was mod-cite (P); Rule R
ACCEPT WITH FIXES, research/G2/review/REVIEW_Plan47.md — REVIEWED), and for p ∈ {1, 2}, s ≥ s0(p) by item 11's
Theorem H (p = 2 citation-free; this covers the `TheoremHPure 2 κ 2` instance of Corollary H_L-ζ). Its `bdd` field is
already the sorry-free `heineK_bdd_of_summable`. Neither paper proof of `asymp` is formalized, so the Lean labels below
stay PROVED-mod-input.

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
| **`theoremHL`** | **Theorem H_L** | **PROVED-mod-input (TheoremHPure; input supplied on paper for all p > 0, s > 1 by G2 Cor. H-input, citation-free since Plan 47 (was mod-cite (P)); item 11 alone gave p ∈ {1,2}, s ≥ s0(p))** |
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
| `toeplitzTri`, `toeplitz_eigen`, `toeplitz_charpoly_roots` | (S4) | for B > 0, T_ℓ(A,B) has the simple eigenvalues A + 2B cos(πi/(ℓ+1)), sine eigenvectors (B = 0: `toeplitz_eigCount_zero`) |
| **`eigCount`, `toeplitz_count`** | **(S4) Toeplitz count** | **\|N(T_ℓ(A,B); μ) − (ℓ/π)θ\| ≤ 1, B ≥ 0; `eigCount` counts charpoly roots > μ with multiplicity (= spectral count for symmetric T)** |
| `chain_limit_core`, `chain_limit` | Paper 2 §3 Lemma `lem:chain-limit` (G1 §3.21 Lemma CS) | positive sequences with U_n + V_n → 2c and U_n V_{n+1} → c² converge: U_n, V_n → c; scale form: s_n a_n → 2c, s_n b_n → c, a_n = u_n + l_n, b_n² = u_{n−1} l_n ⇒ s_n u_n, s_n l_n → c (s_n > 0, s_n/s_{n+1} → 1, e.g. n^p) |
| `xw`, `christoffel_DMeasure`, `opoly_eval_zero`, **`christoffel_sign`** | Paper 2 Lemma `lem:zeros` (sign part) | for atoms x_k ≥ 0, x·σ (weights x_k w_k) is again a `DMeasure`; P_n(0) = (−1)ⁿ D_n(xσ)/D_n(σ), so (−1)ⁿ P_n(0) > 0 (the zero-location statement itself is not formalized) |
| `cg`, `ch`, `cg_pos`, `ch_pos`, `christoffel_ja_split`, `christoffel_jb2_split`, `opoly_recurrence_zero` | Paper 2 Lemma `lem:transfer`(i) | u_n = −P_{n+1}(0)/P_n(0) > 0, l_0 = 0, l_n = b_n²/u_{n−1} > 0; a_n = u_n + l_n, b_{n+1}² = u_n l_{n+1}; the k = 0 recurrence X P_0 = P_1 + a_0 P_0 |
| `christoffel_poly`, `christoffel_back`, **`christoffel_transfer`** | Paper 2 Lemma `lem:transfer`(ii), eq. `eq:transfer` | X·P̃_n = P_{n+1} + u_n P_n (P̃_n monic OPs of xσ), P_{n+1} = P̃_{n+1} + l_{n+1} P̃_n; ã_n = u_n + l_{n+1}, b̃_{n+1}² = u_{n+1} l_{n+1} |
| **`christoffel_shift_law`**, **`christoffel_shift_law_converse`**, **`christoffel_shift_law_pow`** | Paper 2 Theorem `thm:shift` (no rate) + Remark `rem:converse`; G1 §3.21 Theorem SH, §3.19 CT₁ "⟸" | s_n a_n → 2c and s_n b_n → c for σ ⇔ the same for xσ; `_pow`: the iff at scale n^p exactly as in Paper 2 |
| `RegularRate`, `RegularRate.not_summable`, `RegularRate.sqrt_sub_le`, **`chain_rate_core`** | Paper 2 Lemma `lem:chain-rate` (G1 §3.21 Lemma CS-r) | η regular (positive, non-increasing, nη_n non-decreasing, → 0); U_n + V_n − 2c = O(η), U_n V_{n+1} − c² = O(η) ⇒ U_n − c = O(√η_n) and U_{n+1} − U_n = O(η_n) |
| **`christoffel_shift_rate`**, `bigO_rpow_succ_iff`, **`christoffel_shift_rate_pow`** | Paper 2 Theorem `thm:shift` (rate part; G1 §3.21 Theorem SH-r) | s_n a_n − 2c = O(η_n), s_n b_n − c = O(η_n) (and s_n/s_{n+1} − 1 = O(η_n)) ⇒ the same for xσ; `_pow`: at scale n^p exactly as in Paper 2 |
| `hallLam`, `hallC`, `hallKappa`, `four_hallC_rpow` | Paper 1 (1.2) (Plan 60, S0) | Λ(p) = ∫₀¹ arccos(2s^p − 1) ds, c(p) = (π/Λ(p))^p/4, κ_p = 3p/2 + log c(p), so (4c)^{1/p} = π/Λ; the identification Λ(p) = 2I(p) (Gamma form) is stage S6, not yet formalized |
| `arcX`, `arcsine_pot`, `arcsine_pot_ge` | Paper 1 Lemma 3.2 (G2 Lemma B0) | ∫₀^π log\|β(1 − cos φ)/2 − y\| dφ = π log(β/4) for 0 ≤ y ≤ β, and ≥ for y ≥ β (via log-sin integrals, no Fourier series) |
| `muStar`, `starTail_add`, `muStar_Ioc_le`, `muStar_Ioc_eq`, `muStar_Iic_zero` | Paper 1 Theorem 1.3(i) (G2 B\*(i)) | μ\*_u = image of Leb(0,1] ⊗ dφ/π under (t,φ) ↦ (β_t(1 − cos φ)/2)^{−1/p}; μ\*_u(a,b] ≤ b − a, with equality on (0, Λ/π] |
| `Fp`, `Jp`, `muStar_energy_integrable`, **`muStar_energy`** | Paper 1 Theorem 1.3(iii), the value | 𝒥_p(μ\*_u) = ∬ log\|u^{−p} − v^{−p}\| dμ\*_u dμ\*_u = κ_p, absolutely convergent |
| `AdmissibleOn`, `qpt`, `kq`, `uq`, `quantile_sum_ge`, **`quantile_lower`** | Paper 1 Theorem 5.2, Steps 2–3 | quantile configuration of an admissible θ on (0,U]: eventually n²(𝒥_p(θ) − η) ≤ 2Σ_{i<j} F(u_i,u_j); proved by an exact monotone block comparison (far pairs), O(log n) per near pair, and absolute continuity on a set of θ⊗θ-measure ≤ 7/n |
| `scaleM`, `Jp_scaleM`, `thetaV`, `exists_good_theta` | Paper 1 Lemma 3.1, Theorem 5.2 Step 1 | scaling 𝒥(μ_τ) = τ²(𝒥(μ) − pm² log τ); truncated, rescaled μ\*_u is admissible with 𝒥 ≥ κ_p − η |
| `cfg`, `log_heineTerm_cfg`, **`hall_lower`** | **Paper 1 Theorem 5.2 (G2 Theorem A-L), pure powers** | **p > 0, s > 1: ∀ η > 0, eventually hnorm p κ_p (heineD (powSeq p) (powSeq s)) 0 n ≥ −η, i.e. liminf (log D_n + pn² log n)/n² ≥ κ_p — sorry-free, no named input** |

Not here: the true-zero measure (G3′) is research; the forward Weyl law (Theorem B) itself is not formalized.
Christoffel shift (Plan 56; ChainLimit.lean, Christoffel.lean, ChainRate.lean, ChristoffelRate.lean): stated for `DMeasure`
(positive summable weights, bounded strictly decreasing atoms) with atoms x_k ≥ 0, so Paper 2's general σ on [0, ∞) with
finite moments, and an atom at 0, are not covered; the location/simplicity of the zeros in Lemma `lem:zeros` (only the sign
of P_n(0) is used) and Remark `rem:sharp` are not formalized.

Plan 60 (lean/HALL_PLAN.md) formalizes Theorem H_all for pure powers in stages; the rows marked Paper 1 above are
sorry-free. Still missing for `TheoremHPure p κ_p s` as a theorem: the upper bound A-U (Lemma EP, optimality, Lemma 4.1,
Theorem 4.3) and the Gamma form of the constant.

Check: `./check.sh` (build + axioms audit + completeness list; prints AUDIT OK).
