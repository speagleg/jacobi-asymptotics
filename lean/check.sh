#!/usr/bin/env bash
# Build the library and audit axioms: fails on any sorryAx or non-standard axiom.
set -euo pipefail
cd "$(dirname "$0")"
export PATH="$HOME/.elan/bin:$PATH"
lake build 2>&1 | tail -5
out=$(lake env lean Audit.lean 2>&1)
echo "$out"
if grep -q "sorryAx" <<< "$out"; then echo "FAIL: sorryAx present"; exit 1; fi
bad=$(grep -o "depends on axioms: \[[^]]*\]" <<< "$out" | tr -d '[]' | sed 's/depends on axioms: //' \
      | tr ',' '\n' | sed 's/ //g' | grep -v -E '^(propext|Classical.choice|Quot.sound)?$' || true)
if [ -n "$bad" ]; then echo "FAIL: non-standard axioms: $bad"; exit 1; fi
if grep -qi "error" <<< "$out"; then echo "FAIL: errors"; exit 1; fi
need="card_pairs heineTerm_nonneg heineK_mono_K heineK_mono_w heineK_smul_w orderEmb_ge heineTerm_le_of_pair_le heineTerm_le_of_pair_le_split heineTerm_ge_of_pair_ge sum_prod_powersetCard_le factorial_le_prod_succ heineK_tail_split ratio_bounds_of_deriv diff_le_of_L_mono weighted_cesaro_slow slow_shift neg_mul_log_le phi_bound heineK_pos heineD_pos TheoremHPure.uniform_upper SlowFactor.logL_slow SlowFactor.exists_rhoMin SlowFactor.lower_pair SlowFactor.upper_pair heineK_slow_le slow_bdd exponent_identity log_upperTerm_le HL_upper rhoSeq_mono HL_lower theoremHL lemmaP det_mul_cauchyBinet heineK_eq_det heineK_bdd_of_summable heineD_eq_det zetaGamma_spec zetaGamma_hasDerivAt zetaL_slowFactor zetaL_monotoneOn smoothZeta_HL smoothZeta_HL_det dip_self_eq_zero hankel_det_pos dip_opoly_pow dip_opoly_pow_self opoly_monic opoly_recurrence hankel_det_eq_prod sum_log_weighted_asymp zeta_DMeasure smoothZeta_HL_sumForm smoothZeta_bLaw toeplitz_eigen toepVec_ne_zero toeplitz_charpoly_roots toeplitz_eigCount toeplitz_eigCount_zero cos_count toeplitz_count toeplitz_isRoot toepEig_injOn chain_limit_core chain_limit christoffel_DMeasure opoly_eval_zero christoffel_sign cg_pos ch_pos opoly_recurrence_zero christoffel_ja_split christoffel_jb2_split christoffel_poly christoffel_back christoffel_transfer christoffel_shift_law christoffel_shift_law_converse christoffel_shift_law_pow RegularRate.not_summable chain_rate_core christoffel_shift_rate bigO_rpow_succ_iff christoffel_shift_rate_pow hallLam_pos four_hallC_rpow arcsine_pot arcsine_pot_ge starTail_add muStar_Ioc_le muStar_Ioc_eq muStar_Iic_zero muStar_energy_integrable muStar_energy quantile_sum_ge quantile_lower Jp_scaleM exists_good_theta log_heineTerm_cfg hall_lower energy_pos gauss_pd frK_integral le_volume_of_lip starPot_ge starPot_eq starPot_compare Jp_le_kappa"
for t in $need; do
  grep -q "JacobiAsym.$t'" <<< "$out" || { echo "FAIL: $t not audited"; exit 1; }
done
echo "AUDIT OK"
