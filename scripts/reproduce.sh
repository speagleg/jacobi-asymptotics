#!/usr/bin/env bash
# Reproduce the repository's checkable outputs (Plan 59). See REPRODUCIBILITY.md.
#
#   scripts/reproduce.sh            all stages (~5 min)
#   scripts/reproduce.sh --quick    certified suite + manifest only (~20 s)
#   scripts/reproduce.sh --extended all stages, plus 16 slower numerical checks (~11 min)
#
# Python: $PYTHON if set, else .venv/bin/python if present, else python3. The interpreter needs numpy, scipy, mpmath,
# sympy, python-flint 0.9.0 and pytest; the repository's src/ is put first on PYTHONPATH, so the code checked is the
# code in this tree. Each stage reports PASS/FAIL/SKIP; the script exits nonzero if any stage FAILs.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

QUICK=0
EXTENDED=0
for a in "$@"; do
  case "$a" in
    --quick) QUICK=1 ;;
    --extended) EXTENDED=1 ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown argument: $a" >&2; exit 2 ;;
  esac
done

if [ -z "${PYTHON:-}" ]; then
  if [ -x "$ROOT/.venv/bin/python" ]; then PYTHON="$ROOT/.venv/bin/python"; else PYTHON=python3; fi
fi
export PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}"
export PYTHONHASHSEED=0

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

STAGES=()
RESULTS=()
TIMES=()
record() { STAGES+=("$1"); RESULTS+=("$2"); TIMES+=("$3"); }
now() { date +%s; }

# compare <script> <committed .out> [args...]: run from the repo root and diff stdout byte-for-byte against the .out.
# If $NORMALIZE is set (a `sed -E` program), it is applied to both sides first (used only to blank wall-clock stamps).
NORMALIZE=""
compare() {
  local script="$1" ref="$2"; shift 2
  local got="$TMP/$(echo "$ref" | tr '/' '_')" t0 rc
  t0=$(now)
  "$PYTHON" "$script" "$@" > "$got" 2> "$got.err"; rc=$?
  local dt=$(( $(now) - t0 ))
  if [ $rc -ne 0 ]; then
    echo "  FAIL ${dt}s  $script${*:+ $*} (exit $rc)"; tail -5 "$got.err" | sed 's/^/        /'; return 1
  fi
  if [ -n "$NORMALIZE" ]; then
    if ! diff <(sed -E "$NORMALIZE" "$ref") <(sed -E "$NORMALIZE" "$got") > "$got.diff"; then
      echo "  FAIL ${dt}s  $script${*:+ $*}  (differs from $ref after sed -E '$NORMALIZE')"
      head -20 "$got.diff" | sed 's/^/        /'; return 1
    fi
    echo "  ok   ${dt}s  $script${*:+ $*}  (identical after sed -E '$NORMALIZE')"; return 0
  fi
  if ! cmp -s "$ref" "$got"; then
    echo "  FAIL ${dt}s  $script${*:+ $*}  (differs from $ref)"; diff "$ref" "$got" | head -20 | sed 's/^/        /'
    return 1
  fi
  echo "  ok   ${dt}s  $script${*:+ $*}"
  return 0
}

stage() {  # stage <name> <function>
  local name="$1" fn="$2" t0 rc
  echo; echo "=== $name"
  t0=$(now)
  "$fn"; rc=$?
  local dt=$(( $(now) - t0 ))
  if [ $rc -eq 0 ]; then record "$name" PASS "$dt"
  elif [ $rc -eq 77 ]; then record "$name" SKIP "$dt"
  else record "$name" FAIL "$dt"; fi
}

# ---------------------------------------------------------------------------------------------------------------
build_kernel() { make -C csrc; }

fast_tests() { "$PYTHON" -m pytest -q -rs; }

certified_suite() {
  local fail=0 s
  for s in certified/c*.py; do
    compare "$s" "${s%.py}.out" || fail=1
  done
  return $fail
}

# Curated fast, deterministic numerical checks: each reproduced its committed .out byte-for-byte here, both with the
# default BLAS threading and with OMP/OPENBLAS_NUM_THREADS=2, and takes < ~1 min (a few up to ~2 min under load).
# The selection and every exclusion are documented in REPRODUCIBILITY.md.
# Line format: "<script> [args...]" or "<script> ~ <sed -E program>" (normalization applied to both outputs).
STAMP='s/\[[0-9]+s\]/[Ns]/g'   # wall-clock stamps "[31s]" printed by table2.py and check_cb.py
FAST_CHECKS=(
  "papers/paper1/checks/bs_check.py"
  "papers/paper1/checks/monien_check.py"
  "papers/paper1/checks/positivity_sanity.py"
  "papers/paper2/checks/airy_check.py"
  "papers/paper2/checks/lommel_check.py"
  "papers/paper2/checks/table2.py ~ STAMP"
  "research/G1/RH/checks/check_P2.py"
  "research/G1/RH/checks/check_fine.py"
  "research/G1/RH/checks/check_general_r_parametrix.py"
  "research/G1/RH/checks/check_p1_general_r.py"
  "research/G1/RH/checks/check_p1_tc.py"
  "research/G1/RH/checks/check_phase2.py"
  "research/G1/RH/checks/check_phase3a.py"
  "research/G1/RH/checks/check_phase3b.py"
  "research/G1/RH/checks/check_phase4.py"
  "research/G1/RH/checks/check_phase5.py"
  "research/G1/RH/plt1/checks/check_plt1_phase0.py"
  "research/G1/RH/plt1/checks/check_plt1_phase0_small.py"
  "research/G1/RH/px/checks/check_px_phase1.py"
  "research/G1/RH/px/checks/check_px_phase2.py"
  "research/G1/RH/px/checks/check_px_phase3a.py"
  "research/G1/RH/px/checks/check_px_phase4.py"
  "research/G1/RH/route2/checks/check_bnd_fold.py"
  "research/G1/RH/route2/checks/check_r2_lw1.py"
  "research/G1/RH/route2/checks/check_r2_mellin.py"
  "research/G1/RH/route2/checks/check_r2p1_ct.py"
  "research/G1/RH/route2/checks/check_x1_frame.py"
  "research/G1/RH/zeta/checks/check_z_Zcert.py"
  "research/G1/checks/check_cb.py ~ STAMP"
  "research/G1/checks/check_lr.py"
  "research/G1/checks/check_qlp.py"
  "research/G1/checks/check_tail_loc.py"
  "research/G1/checks/check_tailsum.py"
  "research/G1/checks/check_tauberian.py"
  "research/G2/checks/check_averaged.py"
  "research/G2/checks/check_energy.py"
  "research/G2/checks/check_hz.py"
  "research/G2/checks/check_positivity.py"
  "research/G3prime/checks/check_clusters.py"
  "research/G3prime/checks/check_npp.py"
  "research/G3prime/checks/check_positioning.py"
  "research/G3prime/checks/check_shift.py"
  "research/G3prime/checks/check_trunc.py"
  "research/G3prime/checks/check_twins.py"
  "research/G3prime/rhfree/checks/check_99.py"
  "research/G3prime/rhfree/checks/check_dist_probe.py"
  "research/G3prime/rhfree/checks/check_pos_identity.py"
)
# --extended: also reproduced byte-for-byte (same conditions), but 1.5-4 min each.
SLOW_CHECKS=(
  "research/G1/RH/plt1/checks/check_plt1_lhat.py"
  "research/G1/RH/px/checks/check_px_phase3b.py"
  "research/G1/RH/route2/checks/check_r2_coeff.py"
  "research/G1/RH/route2/checks/check_r2_redA.py"
  "research/G1/RH/route2/checks/check_r2alpha_law.py"
  "research/G1/RH/route2/checks/check_r2p1_lw1.py"
  "research/G1/RH/zeta/checks/check_z_edge.py"
  "research/G1/RH/zeta/checks/check_z_lw1.py"
  "research/G1/RH/zeta/checks/check_z_phase0.py"
  "research/G1/checks/check_alaw.py"
  "research/G1/checks/check_cl_rough.py"
  "research/G1/checks/check_log_weights.py"
  "research/G1/checks/check_rl.py"
  "research/G1/checks/check_sv_density.py"
  "research/G1/checks/check_t3_conv.py"
  "research/G1/checks/check_t3_rough.py"
)

# Run the curated checks, $JOBS at a time (default 6; JOBS=1 for sequential); output is printed per check in list
# order once all have finished. BLAS/OpenMP threads default to 2 per job (every listed check was verified with 2
# threads and with the machine default; the 4 thread-sensitive checks are excluded, see REPRODUCIBILITY.md).
numerical_checks() {
  local fail=0 i=0 line script args jobs="${JOBS:-6}"
  local -a list=("${FAST_CHECKS[@]}")
  [ $EXTENDED -eq 1 ] && list+=("${SLOW_CHECKS[@]}")
  export OMP_NUM_THREADS="${OMP_NUM_THREADS:-2}" OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-2}" \
         MKL_NUM_THREADS="${MKL_NUM_THREADS:-2}"
  for line in "${list[@]}"; do
    (
      NORMALIZE=""
      if [[ "$line" == *" ~ "* ]]; then NORMALIZE="${line##* ~ }"; [ "$NORMALIZE" = STAMP ] && NORMALIZE="$STAMP"; line="${line% ~ *}"; fi
      read -r script args <<< "$line"
      # shellcheck disable=SC2086
      compare "$script" "${script%.py}.out" $args > "$TMP/log.$i" 2>&1
      echo $? > "$TMP/rc.$i"
    ) &
    i=$((i + 1))
    while [ "$(jobs -rp | wc -l)" -ge "$jobs" ]; do wait -n; done
  done
  wait
  for ((j = 0; j < i; j++)); do
    cat "$TMP/log.$j"
    [ "$(cat "$TMP/rc.$j" 2>/dev/null)" = 0 ] || fail=1
  done
  echo "  ${#list[@]} checks"
  return $fail
}

lean_check() {
  export PATH="$HOME/.elan/bin:$PATH"
  if ! command -v lake > /dev/null 2>&1; then
    echo "  lake not found: skipping the Lean build (install elan, see lean/README.md)"; return 77
  fi
  if [ ! -e lean/.lake/packages ] && [ "${LEAN_FETCH:-0}" != 1 ]; then
    echo "  lean/.lake/packages absent: skipping (lake would download Mathlib). Set JA_LAKE_PACKAGES for"
    echo "  scripts/setup_env.sh, or LEAN_FETCH=1 to let lake fetch the pinned Mathlib (lake-manifest.json)."
    return 77
  fi
  bash lean/check.sh | tail -3
  return "${PIPESTATUS[0]}"
}

manifest_check() { "$PYTHON" scripts/manifest.py --check; }

# ---------------------------------------------------------------------------------------------------------------
MODE=full; [ $EXTENDED -eq 1 ] && MODE=extended; [ $QUICK -eq 1 ] && MODE=quick
echo "jacobi-asymptotics reproduce ($MODE); python: $("$PYTHON" --version 2>&1)"
T0=$(now)
if [ $QUICK -eq 0 ]; then
  stage "build C kernel"            build_kernel
  stage "fast pytest suite"         fast_tests
fi
stage "certified suite (byte-for-byte)" certified_suite
if [ $QUICK -eq 0 ]; then
  stage "numerical checks (byte-for-byte)" numerical_checks
  stage "Lean build + axiom audit"  lean_check
fi
stage "integrity manifest"          manifest_check

echo; echo "=== summary"
status=0
for i in "${!STAGES[@]}"; do
  printf '  %-4s %5ss  %s\n' "${RESULTS[$i]}" "${TIMES[$i]}" "${STAGES[$i]}"
  [ "${RESULTS[$i]}" = FAIL ] && status=1
done
echo "  total $(( $(now) - T0 ))s: $([ $status -eq 0 ] && echo PASS || echo FAIL)"
exit $status
