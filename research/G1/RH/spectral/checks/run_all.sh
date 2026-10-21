#!/usr/bin/env bash
# Regenerate every spec_*.out from scratch (REVIEW_SPEC2_B F2/F9). Caches go to tmp/spectral_cache/<tag>__<hash>.txt.
# Usage: PY=/path/to/python bash run_all.sh   (two jobs at a time; about 1-2.5 min per new measure on 2 cores)
set -u
cd "$(dirname "$0")"
PY=${PY:-python3}
r() { local out=$1; shift; { for args in "$@"; do $PY -B $args; done; } > "$out" 2>&1; echo "$(date +%T) $out exit=$?"; }
pair() { r "${@:1:2}" & local a=$!; shift 2; r "$@" & local b=$!; wait $a $b; }
# stage 1: measures and self-contained checks
r spec_zeta_airy.out "spec_zeta_airy.py"
r spec_bouncer_closed.out "spec_bouncer_closed.py"
r spec_bouncer_heat.out "spec_bouncer_heat.py"
r spec_airy_index.out "spec_airy_index.py"
r spec_mobius.out "spec_mobius.py"
r spec_lommel.out "spec_lommel.py"
r spec_kernel.out "spec_kernel.py"
r m1_theoremQ.out "m1_theoremQ.py"
r m1_edge.out "m1_edge.py"
r spec_homog.out "spec_homog.py"
r spec_hurwitz_moments.out "spec_hurwitz_moments.py" & A=$!; r spec_hurwitz_moments_plt1.out "spec_hurwitz_moments_plt1.py" & B=$!; wait $A $B
r spec_hur.out "spec_hur.py 0.6 2.0 -0.5" "spec_hur.py 0.6 2.0 0.5" "spec_hur.py 0.6 2.0 1.0" "spec_hur.py 0.75 3.0 1.0" "spec_hur.py 1.5 2.0 0.5" "spec_hur.py 1.5 2.0 1.0" & A=$!
r spec_pert.out "spec_pert.py 0.6 2.0 2 0.5" "spec_pert.py 0.6 2.0 3 -0.4" & B=$!; wait $A $B
r spec_bouncer.out "spec_bouncer.py 2.0" "spec_bouncer.py 3.0" & A=$!; r spec_neumann.out "spec_neumann.py 2.0" & B=$!; wait $A $B
r spec_jitter.out "spec_jitter.py 0.3 2.0 0.3" "spec_jitter.py 0.6 2.0 0.3" "spec_rigid.py 0.6 2.0 0.3" & A=$!
r spec_window.out "spec_window.py 0.6 2.0 0.3 1 300" "spec_window.py 0.6 2.0 0.3 20000 320000" & B=$!; wait $A $B
r spec_remove.out "spec_remove.py 0.6 2.0 30" "spec_remove.py 0.6 2.0 300" & A=$!
r spec_kappa.out "spec_kappa.py 1.0 0.6" "spec_kappa.py 0.5 0.6" "spec_kappa.py 1.0 0.3" & B=$!; wait $A $B
r spec_turning.out "spec_turning.py 0.6 2.0 300 0.3" & A=$!
r spec_robin.out "spec_robin.py 1.0 2.0" "spec_robin.py 0.5 2.0" "spec_robin.py 2.0 2.0" & B=$!; wait $A $B
r spec_gamma.out "spec_gamma.py 0.6 2.0 0.5" "spec_gamma.py 1.5 2.0 0.5" "spec_gamma.py 1.5 2.0 1.0" & A=$!
r spec_gamma_b.out "spec_gamma.py 1.5 2.0 -0.5" "spec_gamma.py 1.5 3.0 0.5" "spec_gamma2.py 1.5 2.0 1.0 kmin 50" "spec_gamma2.py 1.5 2.0 1.0 pow 2" & B=$!; wait $A $B
r spec_pole.out "spec_pole.py 1.25 2.0 0.5 1" "spec_pole.py 1.8 2.0 0.5 1" "spec_pole.py 0.75 2.0 0.5 1" & A=$!
r spec_pole_b.out "spec_pole.py 0.8 2.0 0.5 1" "spec_pole.py 1.5 2.0 0.5 0.5" "spec_pole.py 1.25 2.0 0.5 0.5" & B=$!; wait $A $B
r spec_resonance.out "spec_resonance.py 0.5 2.0 0.5 0.5" & A=$!
r spec_hur_small.out "spec_hur_small.py 3 2.0 -0.5" "spec_hur_small.py 4 2.0 -0.5" & B=$!; wait $A $B
r spec_stats_seeds_a.out "spec_stats.py gue 7" "spec_stats.py gue 11" "spec_stats.py gue 13" "spec_stats.py gue 17" "spec_stats.py gue 19" & A=$!
r spec_stats_seeds_b.out "spec_stats.py poisson 7" "spec_stats.py poisson 11" "spec_stats.py poisson 13" "spec_stats.py poisson 17" "spec_stats.py poisson 19" & B=$!; wait $A $B
r spec_subpole.out "spec_subpole.py 2.0 2.2 2.5 3.0 4.0 3.0:2:2 1.8 1.8:3 1.5 1.25 2.5:2:2 3.0:3.0 2.5:3.0"
# stage 2: readers of stage-1 caches
cat spec_stats_seeds_a.out spec_stats_seeds_b.out > spec_stats_seeds.out; rm -f spec_stats_seeds_a.out spec_stats_seeds_b.out
cat spec_gamma_b.out >> spec_gamma.out; rm -f spec_gamma_b.out
cat spec_pole_b.out >> spec_pole.out; rm -f spec_pole_b.out
r spec_stats_summary.out "spec_stats_summary.py"
r spec_uvarov.out "spec_uvarov.py"
r spec_kappa_fit.out "spec_kappa_fit.py"
r spec_mobius_pred.out "spec_mobius_pred.py"
r spec_hur_d2.out "spec_hur_d2.py"
r spec_bouncer_d2.out "spec_bouncer_d2.py"
r spec_shift_hi.out "spec_shift_hi.py"
grep -L "PASSED" spec_*.out | sed 's/^/no PASSED line: /'
grep -l "FAIL\|Traceback" spec_*.out | sed 's/^/FAILURE in: /'
echo run_all done
