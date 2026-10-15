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
| `hallLam`, `hallC`, `hallKappa`, `four_hallC_rpow` | Paper 1 (1.2) (Plan 60, S0) | Λ(p) = ∫₀¹ arccos(2s^p − 1) ds, c(p) = (π/Λ(p))^p/4, κ_p = 3p/2 + log c(p), so (4c)^{1/p} = π/Λ; Λ(p) = 2I(p) is `hallLam_eq_gamma` (S6) |
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
| `frK`, `frK_integral`, `two_logEnergy_eq`, `gauss_conv`, `gauss_pd`, **`energy_pos`** | Paper 1 Lemma 3.3 (inequality part; G2 Lemma EP) | finite A, B of equal mass, log\|x−y\| integrable, null diagonals ⇒ 𝓛(A,A) + 𝓛(B,B) ≤ 2𝓛(A,B); proved with Frullani's integral (Mathlib) and the Gaussian kernel, not the Fourier transform; the equality case is not formalized |
| `le_volume_of_lip`, `starPot`, `starPot_ge`, `starPot_eq`, `muStar_restrict_us` | Paper 1 Theorem 1.3(ii) (G2 B\*(ii)) | μ(a,b] ≤ b − a ⇒ μ ≤ Leb; U\*(x) = log c + p on [0, 4c], ≥ log c + p on [0, ∞); μ\*_u = Leb on (0, Λ/π] |
| `starPot_compare`, **`Jp_le_kappa`** | Paper 1 Theorem 1.3(iii), optimality (G2 B\*(iii)) | every admissible μ on (0,U] with F_p integrable has 𝒥_p(μ) ≤ κ_p (uniqueness not formalized) |
| `Fp_integrable_box`, `integral_log_abs_sub_ge`, `cell_F_ge`, `far_cell`, `any_cell`, `muBar`, **`disc_upper`** | Paper 1 Lemma 4.1 (G2 Lemma A1) | for S ⊆ {0,…,Mn−1}: 2Σ_{a<b∈S} F(u_a,u_b) ≤ n²𝒥_p(μ̄_S) + \|S\|·eDisc, eDisc = O(log n) for fixed M (u_a = (a+1)/n, μ̄_S = Leb on the cells) |
| `muBar_energy_le`, **`head_V_bound`**, `head_heineK_bound` | Paper 1 Corollary 4.2 (G2 Corollary A2) | log V(S) ≤ −pN² log N + κ_pN² + pN log n + N·eDisc for S ⊆ {0,…,Mn−1}, \|S\| = N ≥ 1 (scaling + `Jp_le_kappa`) |
| `hTerm`, `heineK_le_hTerm`, `log_term_le`, **`hall_upper`** | **Paper 1 Theorem 4.3 (G2 Theorem A-U), pure powers** | **p > 0, s > 1: ∀ η > 0, eventually hnorm p κ_p (heineD (powSeq p) (powSeq s)) 0 n ≤ η — sorry-free** |
| **`theoremHPure_all`** | **Paper 1 Theorem 1.1, pure powers; G2 Corollary H-input** | **`TheoremHPure p (hallKappa p) s` for all p > 0, s > 1 — the named input is now a theorem (with κ_p in the Λ(p) form; Gamma form = stage S6)** |
| **`theoremHL_all`** | **Theorem H_L, no named input** | **`theoremHL` with both `TheoremHPure` instances discharged: log D_n = −pn² log n + n² log L(n) + κ_pn² + o(n²) for p > 0, s, s0 > 1 — sorry-free** |
| `betaF_integral`, `arccos_eq_integral`, **`hallLam_eq_gamma`**, `hallI`, `hallC_eq`, `hallKappa_eq`, `hallKappa_one`, `hallKappa_two` | Paper 1 (1.2) (Plan 60, S6) | Λ(p) = B(1/p+1/2, 1/2) = √π Γ(1/p+1/2)/Γ(1/p+1) = 2I(p), so `hallKappa p` = 3p/2 + log(¼(π/(2I(p)))^p) = κ_p; κ₁ = 3/2 − log 2, κ₂ = 3 + log(π²/16) |
| **`theoremHPure_kappa`**, `theoremHPure_two` | **G2 Corollary H-input, in the paper's normalisation** | **`TheoremHPure p κ_p s` for all p > 0, s > 1 with κ_p = 3p/2 + log(¼(π/(2I(p)))^p) — sorry-free** |
| **`smoothZeta_HL_uncond`, `smoothZeta_HL_det_uncond`, `smoothZeta_bLaw_uncond`** | **Corollary H_L-ζ (all three forms), no named input** | **the smooth-ζ corollaries with `TheoremHPure 2 (3 + log(π²/16)) 2` discharged — sorry-free** |
| `heineK_le_hTermW`, `head_log_bound_w`, `hall_upper_w`, `heineD_weight_ge`, `hall_lower_w`, **`pure_law_w`** | Paper 1 Theorems 4.3, 5.2 as stated (Plan 61, G1) | atoms (k+1)^{−p}: upper bound for any positive summable w (proof of `hall_upper` re-run with W = Σ'w); lower bound for w ≥ c₁(k+1)^{−s}, **any real s** (from `hall_lower` with s' = max s 2 by weight monotonicity) |
| `heineTerm_scale`, `heineD_scale`, `scaled_law` | Paper 1 Lemma 2.2(iii) (G2) | D_n(Σ w δ_{C y_k}) = C^{n(n−1)} D_n(Σ w δ_{y_k}); the constant becomes κ + log C |
| `PairRatio`, `log_heineD_le_of_pair`, **`hnorm_transfer`** | Paper 1 Lemma 2.3 (G2) | pair-gap ratios → 1 (≤ fixed B on pairs with smaller index < a₀) ⇒ \|log D_n(x) − log D_n(y)\| ≤ 2a₀n log B + εn², same law; translation invariance is built in (only differences occur) |
| `deriv_neg_of_hyp`, `gap_bounds`, `pairRatio_of_hyp`, `atoms_of_hyp` | Paper 1 §6, "general atoms" | f′ < 0 (IVT), Cauchy MVT against h(ξ) = Cξ^{−p}: `PairRatio (f(k+1)) (C(k+1)^{−p})`, atoms strictly decreasing and bounded |
| **`paper1_thm11`**, `paper1_thm11_heine` | **Paper 1 Theorem 1.1 in full** | **p > 0, C > 0, f ∈ C¹[1,∞) (`HasDerivWithinAt f (f' ξ) (Ici 1) ξ` for ξ ≥ 1, `ContinuousOn f' (Ici 1)`), ξ^{p+1}f′(ξ) → −pC, ∃ 0 < m ≤ ξ^{p+1}\|f′\| ≤ M on [1,∞); w ≥ 0, Σw < ∞, w_k ≥ c₁k^{−s}, c₁ > 0, s ∈ ℝ: (log det(m_{i+j})_{i,j<n} − (−pn² log n + (κ_p + log C)n²))/n² → 0, κ_p = 3p/2 + log(¼(π/(2I(p)))^p) — sorry-free, no hypothesis strengthened (0-based: atom k is f(k+1))** |
| **`paper1_cor12`** | **Paper 1 Corollary 1.2** | **(2/n²)Σ_{j=1}^{n−1}(n−j) log(j^p √(jb2 j)) → log(c(p)C) — sorry-free** |
| `zetaHankel`, `zeta_re_eq_tsum`, `zetaHankel_eq`, **`paper1_cor14`**, `paper1_cor14_one`, `paper1_cor14_two` | **Paper 1 Corollary 1.4 (G2 HZ)** | **log det_{1≤i,j≤n} ζ(a(i+j)+b) = −an² log n + (3a/2 + log c(a))n² + o(n²) for real a > 0, 2a + b > 1 (Mathlib `riemannZeta`, real parts); special cases a = 1 (3/2 − log 2, b > −1), a = 2 (3 + log(π²/16), b > −3) — sorry-free** |

Plan 60 (lean/HALL_PLAN.md) formalizes Theorem H_all for pure powers: `theoremHPure_all` / `theoremHPure_kappa` prove
the named input `TheoremHPure p κ_p s` for every p > 0, s > 1, sorry-free, with κ_p in the paper's Gamma form (rows marked
Paper 1 above). Consequently `theoremHL_all` (Theorem H_L) and `smoothZeta_HL_uncond`, `smoothZeta_HL_det_uncond`,
`smoothZeta_bLaw_uncond` (Corollary H_L-ζ) are sorry-free with no named input. The older PROVED-mod-input statements are
kept unchanged (they take `TheoremHPure` as a hypothesis). Plan 61 (lean/GENF_PLAN.md) formalizes Paper 1 Theorem 1.1 in
full (`paper1_thm11`: general atoms f(k), general weights, any real s), Corollary 1.2 (`paper1_cor12`) and Corollary 1.4
(`paper1_cor14`), sorry-free with no named input and no strengthened hypothesis. Not formalized: the uniqueness of the
maximiser and the equality case of Lemma 3.3 (neither is used by Theorem 1.1).

Check: `./check.sh` (build + axioms audit + completeness list; prints AUDIT OK).
