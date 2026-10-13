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
need="card_pairs heineTerm_nonneg heineK_mono_K heineK_mono_w heineK_smul_w orderEmb_ge heineTerm_le_of_pair_le heineTerm_le_of_pair_le_split heineTerm_ge_of_pair_ge sum_prod_powersetCard_le factorial_le_prod_succ heineK_tail_split ratio_bounds_of_deriv diff_le_of_L_mono weighted_cesaro_slow slow_shift neg_mul_log_le phi_bound heineK_pos heineD_pos TheoremHPure.uniform_upper SlowFactor.logL_slow SlowFactor.exists_rhoMin SlowFactor.lower_pair SlowFactor.upper_pair heineK_slow_le slow_bdd exponent_identity log_upperTerm_le HL_upper rhoSeq_mono HL_lower theoremHL lemmaP det_mul_cauchyBinet heineK_eq_det heineK_bdd_of_summable heineD_eq_det zetaGamma_spec zetaGamma_hasDerivAt zetaL_slowFactor zetaL_monotoneOn smoothZeta_HL smoothZeta_HL_det dip_self_eq_zero hankel_det_pos dip_opoly_pow dip_opoly_pow_self opoly_monic opoly_recurrence hankel_det_eq_prod sum_log_weighted_asymp"
for t in $need; do
  echo "$out" | grep -q "JacobiAsym.$t'" || { echo "FAIL: $t not audited"; exit 1; }
done
echo "AUDIT OK"
