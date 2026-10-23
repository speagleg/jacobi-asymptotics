# REFIT: audit of the deep-fit results against the measure-generator defects found in JZC_W2

Status (2026-10-23): **NOT REVIEWED** (no Rule R reader). Every result here is **NUMERICAL** (Rule N: fit medians and half-ranges are
spreads over fit choices, not error bounds; agreement between two generators is not an enclosure). No claim about RH: no measure built from
zeta zeros is used. No memo, paper, existing script or existing `.out` was edited. The label recommendations in §5 are for the owners of the
notes to apply.

**Scope.** JZC_W2 Rule A items 5–7 found two defects in the measure generators used before it, at the 10⁻¹³–10⁻¹⁶ level in y_n = n^pb_n/c − 1:
**(a)** the measure beyond the last atom is a pure power (any correction to λ_k ∼ k^p is dropped there: κ, ak^{p−1}, McMahon's terms, the
multiplicity's +1), cut sharply at K + ½ (midpoint Euler–Maclaurin defect); **(b)** float64 atoms, masses and scipy float64 Gauss–Jacobi rules
are fed to the binary128 RKPW kernel. This note asks which earlier results depend on fits deep enough for that to matter, re-runs them on
corrected data, and compares old and new fitted values and verdicts.

**Result in one line.** Re-running gave **no verdict changes**: no pass became a fail, no fail became a pass, and every
alternative that was excluded is still excluded. Several results got much sharper (half-ranges down 10–10⁴×). Four rows that the notes call
"weak" or "not informative" are now decisive. One explanation in JZC_M4 §3 holds only in part: the p = 3 N⁻³ residual is not data noise.
The SPEC §3.5 κ-caches at p < 1 carry large defect-(a) errors (up to 3·10⁻⁴ in y). Those errors stay below the tolerances that were
claimed, and the p = 0.3 row now discriminates.

## 1. The corrected generator (`checks/refit_data.py`) and its validation

`refit_data.py` extends `w2_data.py` (imported, not modified) to the general weighted node sets of JZC_W / SPEC / JZC_M4. It uses:
- atoms 1/λ(k) and masses m(k) at mpmath dps 40, handed to w2_data's binary128 RKPW copy as double-double pairs;
- w2_data's C^∞ partition of unity on [K, 2K], with the complement integrated by Newton-refined Gauss–Legendre (1600 nodes);
- **new:** the continuum beyond 2K, integrated in u = 2K/t on geometric panels [4^{−j−1}, 4^{−j}] with Gauss–Legendre (64 nodes per
  panel for p > 1, 512 for p < 1) at the exact node positions 1/λ(t). This needs no expansion of λ(t) in t, so it applies to the families
  A, B and M as well as to κ. w2_data's Gauss–Jacobi-in-x tail is exact only when the density is x^β times a function analytic in x.

Families: κ-lattice, A (k^p + ak^{p−1}), M1 (l(l+1), multiplicity 2l + 1), M2, Bessel zeros (300 zeros from besseljzero at dps 45, then
McMahon), Hurwitz. The old runs' K is kept; nmax is 1600 (1200 for W_outer).

Validation (`refit_validate.out`, `refit_lommel.out`, `refit_mpcheck.out`):
- **Against w2_data (independent far-tail method), JZC_W2 case P15a.** max |Δy| = 1.1·10⁻³² over n ≤ 1200.
- **K-independence, family A (p = 1.5, a = −¾).** K = 50·nmax against 100·nmax: max |Δy| = 8·10⁻³², and n⁴|Δy| ≤ 3·10⁻¹⁹.
- **Exact closed form (Lommel, SPEC §3.10), Bessel zeros at P = 2, μ = 0 and 1.5, n ≤ 40, K = 4000 and 40000.**
  |n²b_n/c − 4n²/((2n+μ)√((2n+μ)² − 1))| ≤ 2·10⁻³¹. spec_lommel's float64 run gave 1.6·10⁻¹⁵.
- **p < 1 tail panels, A06 (640 000 atoms).** 512 against 768 nodes per panel: max |Δy| = 5·10⁻³².

Rule A log for the generator. Two bugs were found in run 1 (`refit_w_test.out`, rows M1 and A06; the old outputs are kept in
`tmp/refit/stale/`), and both were fixed before any comparison was used:
1. M1's λ(k) = k(k+1) was a Python int, so 1/λ was float64. The new σ_y equalled the old one, 9·10⁻¹⁶, which gave it away.
2. At p < 1, 64 nodes per panel do not resolve the far tail. For p < 1 about 10² zeros of p_n lie beyond 2K, against about 20 for
   p > 1. Run 1's A06 data were wrong at 5·10⁻⁸, which gave it away.

The final M1/A06 rows are in `refit_w_test2.out`. `refit_m4.out` printed the sha256 of the pre-fix `refit_data.py`. The fix does not touch
the Hurwitz family at p > 1 (same cache keys, same records).

## 2. Size of the defect (old minus new data, same atoms)

| pipeline / family | \|y_old − y_new\| at n = 200 / 800 / 1600 | old σ_y (6th differences) | new σ_y |
|---|---|---|---|
| run_measure, p ≥ 1.5 (A, B, M, κ at p = 2, 2.5) | 10⁻¹⁷–10⁻¹⁵ / 10⁻¹⁶–6·10⁻¹⁵ / 10⁻¹⁵–2.5·10⁻¹⁴ | 0.9–4.6·10⁻¹⁵ | ≤ 7·10⁻²⁰ |
| run_measure, KO3 (p = 1.5, κ = 0.4: (a) relative κT₀^{−p} = 10⁻⁸) | 8·10⁻¹⁴ / 1.4·10⁻¹² / – | 1.1·10⁻¹⁵ | 8·10⁻²¹ |
| run_measure, A06 (p = 0.6) | 1.5·10⁻¹⁴ / 2·10⁻¹³ / 6·10⁻¹⁴ (5·10⁻¹³ at 1200) | 1.7·10⁻¹⁵ | 7·10⁻²¹ |
| Plan 62 lattices (so_coeffs), p ≥ 1.5 | ≤ 10⁻¹⁵ / ≤ 5·10⁻¹⁵ / ≤ 4·10⁻¹⁴; p = 1.25: 1.7·10⁻¹³ at 1600 | – | – |
| Plan 62 lattices, p = 0.6, 0.3 | ≤ 4·10⁻¹⁴ (n = 200), 2–7·10⁻¹³ (800) | – | – |
| spec_common.run, λ = k^p + κ, **p = 0.6, κ = 1** (spec_kappa) | **1.2·10⁻⁷ / 3.1·10⁻⁶** / 4·10⁻⁸ (n = 1500) | – | – |
| spec_common.run, λ = k^p + κ, **p = 0.3, κ = 1** | **3.4·10⁻⁴ / 7.2·10⁻⁵** / 5.5·10⁻⁵ | – | – |

So defect (b) together with the midpoint cut gives white noise of about 10⁻¹⁵ plus a smooth drift up to about 2·10⁻¹⁴ at n = 1600. This
holds for every pipeline (run_measure, spec_common.run, so_coeffs) at p > 1. Defect (a) matters only when the dropped tail correction is
large: κ at p < 1, where the relative node error is κ/K^p = 5·10⁻⁴ at p = 0.6 and 2·10⁻² at p = 0.3, and to a lesser degree KO3. Translated
into fitted coefficients at p > 1, new minus old is ≤ 10⁻⁹ at n⁻¹, ≤ 5·10⁻⁷ at n⁻², ≤ 2·10⁻⁶ at n^{−2.5}, ≤ 3.4·10⁻⁵ at n⁻³ (A15p),
≤ 4·10⁻⁴ at n^{−3.5} (B1_15) and ≤ 2·10⁻⁵ at n⁻⁴ (p = 2). At p = 0.6 (A06) it is ≤ 3·10⁻⁵ through n^{−2.2} and 6·10⁻³ at n^{−2.8}. These
bounds are used in §4 for the results not re-run.

## 3. Re-runs (old → new; the original fit routines, pass rules and stored predictions; nothing re-registered)

Outputs: `checks/refit_w_test.out` (+ `refit_w_test2.out` for M1, A06), `refit_w_probe.out`, `refit_w_outer.out`, `refit_m4.out`,
`refit_spec.out`, `refit_subpole.out`. "tol" = max(3 half-ranges, floor) as in the original script.

**JZC_W §2.3 (w_test; 9 measures, 41 targets): all 41 verdicts unchanged.** Deepest rows:

| case | coefficient | W | old fit (half-range) | new fit (half-range) | new − W |
|---|---|---|---|---|---|
| A15m | n⁻³ | +0.0699377 | +0.0699393 (1.1·10⁻³) | +0.06993774 (3.2·10⁻⁵) | 7·10⁻⁹ |
| A15m | n^{−3.5} | +0.147717200 | +0.14775 (2.9·10⁻²) | +0.147717200 (3.1·10⁻⁵) | 2·10⁻¹⁰; alternatives now 1597–4791 tol (were "weak: 2–5") |
| A15p | n⁻³ | −1.0077315 | −1.0077655 (1.1·10⁻³) | −1.0077316 (3.6·10⁻⁴) | −1·10⁻⁸ |
| A15p | n^{−3.5} | +0.748561 | +0.748569 (3·10⁻²) | +0.748558 (5.4·10⁻⁵) | −2·10⁻⁶; alternatives 2535–4647 tol |
| A3 | n⁻³ | +0.0452648 | +0.0452649 (2.7·10⁻⁶) | +0.04526476 (5.5·10⁻⁸) | −4·10⁻⁹ |
| B0_15 | n⁻³ | −0.0713449 | −0.071360 (1.8·10⁻²) | −0.07134492 (1.3·10⁻⁶) | 5·10⁻⁹ |
| B0_15 | n^{−3.5} | +0.0011834 | +0.00093 (0.94) | +0.00118336 (1.0·10⁻⁵) | −7·10⁻⁸; β = α 113 tol, no Z(−j) 38 tol |
| B1_15 | n⁻³ | −0.5692249 | −0.569239 (1.7·10⁻²) | −0.5692251 (4.5·10⁻⁵) | −2.5·10⁻⁷ |
| B1_15 | n^{−3.5} | +0.155152 | +0.15477 (0.91) | +0.155157 (1.3·10⁻⁴) | 5·10⁻⁶; alternatives 167–389 tol |
| B0_3 | n⁻³ | +0.0049259 | +0.0049264 (1.2·10⁻⁵) | +0.00492588 (4.6·10⁻⁸) | −6·10⁻⁹ |
| M2 | n⁻³, n^{−3.5} | +0.1900476, +0.0577263 | +0.1900481 (1.1·10⁻³), +0.05779 (2.9·10⁻²) | +0.1900485 (1.2·10⁻⁵), +0.0577755 (7.7·10⁻⁵) | 9·10⁻⁷ (0.03 tol), 4.9·10⁻⁵ (0.21 tol) |
| M1 | n⁻⁴ (W: M(1, 0)) | +7.5449219 | +7.776241 (3.3·10⁻⁴) FAIL | +7.7762407 (7.9·10⁻⁶) FAIL | +0.2313188 (9795 tol; same verdict) |
| A06 (p = 0.6) | n⁻², n^{−2.6}, n^{−2.8} | +0.1329122, −0.062675, −0.234633 | −2.0·10⁻⁴ (1.1·10⁻³), +3·10⁻³ (2.8·10⁻²), +6.6·10⁻³ (9.3·10⁻²) off W | −2.1·10⁻⁴ (1.1·10⁻³), +4·10⁻⁴ (1.8·10⁻²), +1.2·10⁻⁴ (1.6·10⁻²) off W | half-ranges at p < 1 come from model truncation, not data |

**JZC_W §2.4 (w_probe, w_probe2): all verdicts unchanged.** W′ is confirmed far more sharply.

| measure | n⁻⁴: W′ | old fit (half-range), Δ to W′ | new fit (half-range), Δ to W′ | W (unrefined), new |
|---|---|---|---|---|
| M1 sphere (post hoc) | +7.7762407 | +7.7762408 (3.3·10⁻⁴), +2.5·10⁻⁸ | +7.7762407 (7.9·10⁻⁶), −3·10⁻⁸ | fails, 9795 tol |
| K2p (s = 3) | +1.9076973 | +1.9077102 (6.8·10⁻⁴), +1.3·10⁻⁵ | +1.9076973 (1.5·10⁻⁶), −2.9·10⁻⁸ | fails, 36846 tol |
| K2m (s = 3) | +0.0571465 | +0.0571455 (5.0·10⁻⁴) | +0.0571464 (1.2·10⁻⁶), −2.6·10⁻⁸ | fails, 67006 tol |
| K2p, s = 2 (pre-registered; W′ = W) | +0.6993909 | +0.6994095 (1.6·10⁻³), +1.9·10⁻⁵ | +0.6993909 (6.7·10⁻⁷), −2.1·10⁻⁸ | (same) |
| **K2p, s = 3.5 (pre-registered)** | **+2.9296023** | +2.9296226 (3.6·10⁻³), +2.0·10⁻⁵; W off by 16 tol | **+2.9296023 (2.6·10⁻⁶), −5.4·10⁻⁸** | **fails, 22075 tol** |
| H2, L2 (controls) | = W | pass | pass (Δ ≤ 10⁻⁷) | – |

The κ-even part (K2p + K2m)/2 − L2 has no n⁻⁴ term: −1.2·10⁻⁶ ± 2.7·10⁻⁴ (old), −2.2·10⁻⁸ ± 1.1·10⁻⁶ (new). The identification
0.23132 = 3π²/128 now holds to 1·10⁻⁷ (new fit − M(1, 0) = 0.2313188, 3π²/128 = 0.2313189). It was 1·10⁻⁵ before. **The common
Δ ≈ +2·10⁻⁵ of the old probe-2 fits was the data defect.** W′ remains a CONJECTURE, and its general-q part is still untested (JZC_W §2.4).

**JZC_W_outer §8 (w_outer_e2e; KO1–KO3): all 13 verdicts unchanged.** The weak n^{−3.5} row becomes decisive:

| case | n^{−3.5}: W | old fit (half-range) | new fit (half-range) | control "no gauge share in t₁": old → new | "no pole": new |
|---|---|---|---|---|---|
| KO1 | −0.3809443 | −0.380983 (1.1·10⁻²) | −0.3809443 (2.7·10⁻⁵) | 5.8 → **2449 tol** | 1225 tol |
| KO2 | +0.4072321 | +0.407190 (7.3·10⁻³) | +0.4072319 (9.6·10⁻⁵) | 9.0 → **684 tol** | 342 tol |

The other rows are unchanged within their half-ranges, for example KO2 n⁻³: +0.0466828 (2.4·10⁻⁴) → +0.0466871 (6·10⁻⁶) against
+0.0466875. KO3 had the largest defect (a) of the p > 1 runs (1.4·10⁻¹² in y), yet its fits moved by ≤ 1.2·10⁻⁶.

**JZC_M4 §3 (m4_natural_index; 7 Plan 62 lattices): verdicts unchanged; the "resolved" explanation is confirmed except at p = 3.**

| p, s | N⁻³ residual: old (spread) | new (spread) | sd of N⁴R on n ≥ 600: old → new |
|---|---|---|---|
| 1.5, 2 | −3.0·10⁻⁴ (2·10⁻⁴) | −2.1·10⁻⁷ (1·10⁻⁵) | 6.1·10⁻² → 3.7·10⁻⁴ |
| 1.5, 3 | +3.2·10⁻⁴ (2·10⁻⁴) | −1.3·10⁻⁵ (1·10⁻⁵) | 5.8·10⁻² → 4.4·10⁻⁴ |
| 1.25, 2 | +5.2·10⁻⁴ (4·10⁻⁴) | −3.0·10⁻⁵ (3·10⁻⁵) | 2.8·10⁻¹ → 5.2·10⁻⁴ |
| 2.5, 2 | −6.0·10⁻⁵ (6·10⁻⁵) | +2.5·10⁻⁶ (3·10⁻⁶) | 4.0·10⁻³ → 5.2·10⁻⁴ |
| **3, 2** | **+2.3·10⁻⁶ (5·10⁻⁷)** | **+1.66·10⁻⁶ (1·10⁻⁷)** | 2.7·10⁻³ → 6.5·10⁻⁴ |
| 1.5, 2.5 | +1.3·10⁻⁵ (2·10⁻⁵) | −6.7·10⁻⁶ (3·10⁻⁶) | 5.9·10⁻² → 3.7·10⁻⁴ |
| 2, 3 | −3·10⁻⁷ (3·10⁻⁷) | −1.7·10⁻⁸ (8·10⁻⁸) | 4.1·10⁻³ → 4.3·10⁻⁴ |

The N⁻¹ and N⁻² residuals shrink by 10–100× (for example 1.5·10⁻⁷ → 4·10⁻¹⁰). The sign flip in α and the large-n wander were data
defects. Exception: **at p = 3 the 2·10⁻⁶ residual persists on corrected data** (1.66·10⁻⁶ at about 16 spreads). So it is not "fit noise
from the data" as JZC_M4 §3 says. It is a systematic of this fit design: the truncated subtraction and the nuisance set (4, 5, 2 + jp,
3 + jp) on the windows n ≥ 200, 400. Its size, 2·10⁻⁶, is still well under the check's floor of 10⁻⁵, and the mid-window fits of
m4_f4_lattice give ≤ 4·10⁻⁸. The conclusion f₃ = 0 does not depend on it: it is PROVED-mod-cite by JZC_SIGMA Cor Σ.1. Not investigated
further.

**JZC_M3a_H_G1u §5a (m3a_g1u_endtoend; the two β′ = −2.1 cases at K = 160 000): unchanged, much sharper.**
- p = 1.5: d₂ dev −1.1·10⁻⁶ → −4.7·10⁻⁹; ε₁ dev −6.4·10⁻⁶ (half-range 1.1·10⁻³) → +1.4·10⁻⁸ (2·10⁻⁷).
- p = 3: d₃ dev −4.8·10⁻⁷ (1.3·10⁻⁵) → +6.7·10⁻¹² (1.8·10⁻⁹).

**SPEC §3.5 (spec_kappa_fit, spec_mobius_pred; the worst defect (a)): unchanged verdicts, one weak row becomes evidence.**

| p, κ | L: old (half-range) | L: new (half-range) | candidate −2(2−p)cκ | Möbius ratio at n = 50 / 1500: old → new |
|---|---|---|---|---|
| 0.6, 1 | −1.20342 (0.13) | **−1.202472 (1.4·10⁻⁵)** | −1.20247 | 0.95451 / 0.99526 → 0.95451 / 0.99527 |
| 0.3, 1 | −1.22311 (0.74) | **−1.22264 (4.0·10⁻⁴)** | −1.22262 | 0.85860 / 0.94742 → 0.85986 / 0.94697 |

The old κ-measures were wrong by up to 3·10⁻⁶ (p = 0.6) and 3.4·10⁻⁴ (p = 0.3) in y. Their pure-power tail drops the κ-shift of the far
nodes, which W_plt1 Rule A item 5 had already noted for run_measure. The claims had tolerances of 10⁻³ and 3κn^{−p}, and those still hold.
At p = 0.3, SPEC §3.5 calls the 0.04 % agreement "luck, not evidence" (half-range 74 %). On corrected data the half-range is 0.03 % and the
agreement is 2·10⁻⁵, so the row is now real evidence, though it was the identification target only at p = 0.6. The κ = ½ row was not
re-run; at p = 0.6 its defect is half that of κ = 1.

**SPEC §3.15 (spec_subpole, the row p = 2, s = 2, m = 1, "S = −W(1) = −π²/8 to 10⁻⁶"): unchanged, much sharper.**
S = −1.233701646 (half-range 9.6·10⁻⁷), off by −1.1·10⁻⁶ → **−1.233700550 (3.7·10⁻¹⁰), off by +3.7·10⁻¹⁰.** The other rows (q₁ ≤ 1 at
2·10⁻⁶–4·10⁻⁵) have the tolerance floor 2·10⁻⁴|S| and were not re-run.

## 4. Inventory

Pipelines:
- **RM** = w_common.run_measure: float64 atoms; scipy Gauss–Jacobi pure-power tail at the midpoint T₀; quad RKPW.
- **P62** = so_coeffs.coeffs: Hurwitz lattices; float64; the pure power is exact; midpoint cut at K + ½ + δ.
- **SC** = spec_common.run: as RM, with a pure-power tail of (k + δ_tail)^p.
- **own** = script-specific generator.

Affected: (a) means a non-trivial tail correction is dropped; (b) means float64 data. "Margin" compares the claim's tolerance or
precision with the measured defect (§2 bounds).

| result (memo, check) | pipeline | affected | claimed precision / tolerance | margin vs defect | re-run? old → new | verdict |
|---|---|---|---|---|---|---|
| JZC_W §2.3, families A, M1, M2, B (w_test, w_resid) | RM | A, M1: (a) relative ~10⁻⁶ and (b); B: (a) relative 10⁻¹² and (b); M2: (b) and midpoint | n⁻¹–n⁻²: 10⁻⁷–10⁻¹⁰; n⁻³–n^{−3.5}: half-ranges 10⁻³–0.9 ("weak") | deep rows not safely above | **yes** (§3) | unchanged; n^{−3.5} rows now decisive |
| JZC_W §2.4 M1 n⁻⁴ fail; W′ probes (w_probe, w_probe2) | RM (famK: κ dropped in the tail) | (a) and (b) | n⁻⁴ half-ranges 10⁻³; W′ Δ 2·10⁻⁵ | not safely above | **yes** | unchanged (M1 W fails, W′ passes); Δ 2·10⁻⁵ → 5·10⁻⁸ |
| JZC_W §2.2 Lommel anchor; Obs W.3 | exact (no measure) | – | 2·10⁻²¹ | – | no | unaffected |
| JZC_W_outer §8 (w_outer_e2e) | RM (famK tail) | (a) (KO3: 10⁻⁸ relative) and (b) | d₁ 10⁻¹⁰, d₂ 5·10⁻⁸, pole 4·10⁻⁷; n^{−3.5} weak | n^{−3.5} not safely above | **yes** | unchanged; n^{−3.5} controls 5.8/9 → 2449/684 tol |
| JZC_W_outer §3–§7 (index, scalar) | none (function evaluations) | – | – | – | no | unaffected |
| JZC_W_exact (all), JZC_W_BT (all) | exact engine / quadrature, **no measure data** | – | – | – | no | unaffected |
| JZC_W_kappa (checks), JZC_W2 | none / w2_data (already corrected) | – | – | – | no | unaffected |
| JZC_W_plt1 §5 (w_plt1_test) | own: exact κ-tail, float64 Gauss–Jacobi, midpoint cut | (b) only | targets ≤ n^{−2.25}; tol ≥ 3·1.6·10⁻⁴ | A06 bound ≤ 3·10⁻⁵ through n^{−2.2}; K → 2K tested there | no | unaffected in substance |
| JZC_M4 §3 natural index (m4_natural_index) | P62 | (b) and midpoint | N⁻³ ≤ 5·10⁻⁴ ("fit noise") | not above | **yes** | unchanged; explanation confirmed except p = 3 (§3) |
| JZC_M4 §5 lattice cross-check (m4_f4_lattice) | P62, mid-window n ≤ 400 | (b) | 3·10⁻¹⁰–5·10⁻⁵ | windows n ≤ 400, where Δy ≤ 10⁻¹⁵ (§2): n⁴Δy ≤ 3·10⁻⁵ at n = 400, below the coarsest claim's spread 10⁻⁴; the 3·10⁻¹⁰ row (p = 4) is the most exposed | no | unaffected in substance (p = 4 row: re-run if its 3·10⁻¹⁰ is cited as a precision) |
| JZC_M4 §5–§8, JZC_M4_proof, JZC_SIGMA | exact engine | – | – | – | no | unaffected |
| JZC_M3a_H_G1u §5a (m3a_g1u_endtoend) | P62 | (b) and midpoint | floors 10⁻⁵–10⁻³ | ≥ 30× | yes (β′ = −2.1) | unchanged; d₃ dev 5·10⁻⁷ → 7·10⁻¹² |
| JZC_M3a_H_G1u_plt1 §5b (m3a_g1up_endtoend) | P62, p < 1 | (b) and midpoint | floors 10⁻⁴; ε₂ half-ranges 0.08 | ≥ 30× (p < 1 bound) | no | unaffected |
| JZC_M3a_Hd §4 (m3a_hd_model; reads spec_hur, spec_hur_d2, spec_shift_hi, spec_hur_small) | P62 | (b) and midpoint | half-ranges ≥ 3.9·10⁻⁵ (n^{−2−p}: 0.4) | ≥ 10× | no | unaffected |
| JZC_M3a_H_G1u hardedge, G12, G23, G3, Ha, Hc, Hd outer (m3a_*_apriori/outer/seam/gauge/interp) | function evaluations, no Jacobi data | – | – | – | no | unaffected |
| SPEC §2 Hurwitz, moved node, removed node, bouncer, jitter (spec_hur, spec_pert, spec_remove, spec_bouncer, spec_zeta_airy, spec_jitter, spec_window) | P62 / SC | (b); bouncer (a) with WKB O(k⁻²) | ≥ 10⁻⁵ (n^{−1−p} half-ranges 10⁻⁴–10⁻³; jitter RMS ≥ 10⁻⁹) | ≥ 10³× | no | unaffected |
| SPEC §3.2 Lemma U "to 6·10⁻¹², limited by cache precision" (spec_uvarov) | P62 caches | (b) | 6·10⁻¹² | consistent with (b) (the limit is that defect) | no | unaffected (precision statement only) |
| SPEC §3.4 Maslov, §3.10 (spec_hur_d2, spec_bouncer_d2, spec_hur_small) | P62 / SC | (b) | 2·10⁻⁶–3·10⁻⁴ with spreads ≥ 3·10⁻⁵ | ≥ 10² | no | unaffected |
| SPEC §3.10 Lommel row "checked to 10⁻¹⁵" (spec_lommel) | own (float64 McMahon zeros, pure-power tail) | (a) and (b); the claim sits at the defect level | 10⁻¹⁵ (asserted < 10⁻⁷) | not above | **yes** (refit_lommel) | unchanged; 1.6·10⁻¹⁵ → 2·10⁻³¹ |
| SPEC §3.5 κ (spec_kappa, spec_kappa_fit, spec_mobius_pred) | SC with κ dropped in the tail, **p < 1** | **(a) large: 5·10⁻⁴ / 2·10⁻² relative node error in the tail; Δy up to 3·10⁻⁶ / 3.4·10⁻⁴** | L half-ranges 0.04–0.74; ratio tol 3κn^{−p} | the data were wrong at 10⁻⁶–10⁻⁴, still below the claims | **yes** | unchanged; p = 0.3 row now evidence (§3) |
| SPEC §3.11(a) shift_hi (d₃, n^{−3.5}) | P62 | (b) | d₃ ranges 10⁻⁴–10⁻²; n^{−3.5} spreads 0.14 | ≥ 3× (n^{−3.5} shift ≤ 4·10⁻⁴) | no | unaffected |
| SPEC §3.11(b) gamma, §3.12 pole law (spec_gamma, spec_gamma2, spec_pole, spec_resonance) | SC (tail drops γ/k^m: relative ≤ 10⁻¹¹) and P62 | (b) | 10⁻⁶–10⁻³ at n⁻² | ≥ 10³ | no | unaffected |
| SPEC §3.13, §3.14 (spec_robin, spec_neumann, spec_mobius, spec_kernel*, spec_qN) | SC / exact | (b) | ≥ 10⁻⁶ at n ≤ n⁻² | ≥ 10² | no | unaffected |
| SPEC §3.15 subleading pole (spec_subpole) | SC and P62 | (b) | 10⁻⁶ stated (tol floor 2·10⁻⁴\|S\|); n⁻³ in y, Richardson ×8 | stated precision not above | **yes** (p = 2, s = 2) | unchanged; S − (−π²/8): −1.1·10⁻⁶ → 3.7·10⁻¹⁰ |
| SPEC §3.16 drum corners (spec_corners) | own RKPW, p = 1 | (b) | ≥ 10⁻⁴ | ≥ 10³ | no | unaffected |
| SPEC §3.17 quartic (spec_quartic, spec_homog) | SC; eigenvalues to 3·10⁻¹⁶ | (b); the eigenvalue error is of the same size | d₂ to 3·10⁻⁵ (spread 10⁻⁵); B to 4·10⁻¹⁰ is an eigenvalue fit, not b_n | ≥ 10² | no | unaffected |
| SPEC §3.18 noise, edge kernel (spec_edgekernel, spec_noiselin, spec_stats, spec_turning, spec_rigid) | SC − P62 differences of noise ≥ 10⁻⁹ | (b) | RMS 10⁻⁹–10⁻² | ≥ 10⁶ | no | unaffected |
| SPEC §3.1 Lemma H, §3.3 bouncer zeta, §3.7–§3.9 | moments / closed forms / heuristic | – | – | – | no | unaffected |

## 5. Recommended label and text changes (for the notes' owners; no labels move between categories)

All labels stay as they are (NUMERICAL / CONJECTURE / PASS). The re-runs change numbers and qualifiers only:
1. **JZC_W §2.3–§2.4, §3 item 8.** The "noise floor" and the n ≥ 1200 "wander" (≈ 3·10⁻¹⁴) came from the data generator (REFIT §2), so the
   n^{−3.5} rows of A15m, A15p, B0_15 and B1_15 are no longer "weak / not informative". With corrected data W passes at ≤ 0.01 tol, with
   half-ranges 10⁻⁵–10⁻⁴, and the alternatives are excluded by 38–4791 tol. Suggested: add a REFIT note. Keep NUMERICAL; the probe-1 and
   M1 parts stay post hoc (Rule X).
2. **JZC_W §2.4 W′.** Probe 2 (pre-registered): W′ − fit = −5·10⁻⁸ (half-range 2.6·10⁻⁶) at s = 3.5, and unrefined W fails by 22075 tol
   instead of 16. The M1 identification 3π²/128 now holds to 10⁻⁷. W′ stays a **CONJECTURE**: one pre-registered confirmation, now at high
   precision, and the general-q part is untested.
3. **JZC_W_outer §8.** The n^{−3.5} row of KO1/KO2 can drop "weak evidence": the "no gauge share" control misses by 2449 and 684 tol on
   corrected data. This is a re-run of the same registered predictions on new data, not a new registration; say so.
4. **JZC_M4 §3, "Resolved".** For p ≤ 2.5 the N⁻³ residual was data noise; the corrected data give ≤ 3·10⁻⁵ at the original fit settings,
   and the α-odd pattern is gone. **At p = 3 the 2·10⁻⁶ residual is not data noise:** it persists at 1.7·10⁻⁶, about 16 spreads, on
   corrected data. Reword to "a systematic of the tail-window fit (nuisance set), below the 10⁻⁵ floor; mid-window fits ≤ 4·10⁻⁸; f₃ = 0 is
   proved (JZC_SIGMA Cor Σ.1)". This is the only explanation in the audited notes that the data correction contradicts, in part.
5. **SPEC §3.5.** Note that spec_kappa's caches carry a defect-(a) measure error of 3·10⁻⁶ (p = 0.6) and 3.4·10⁻⁴ (p = 0.3) in y. On
   corrected data: L = −1.202472 (1.4·10⁻⁵) and −1.22264 (4·10⁻⁴) against −1.20247 and −1.22262. The p = 0.3 caveat ("luck, not evidence")
   can be replaced by this out-of-identification-set agreement. The Möbius ratios move by ≤ 1.7·10⁻³, and their reading (a gap that decays
   like κn^{−p}) is unchanged.
6. **SPEC §3.10 Lommel row.** "checked against Bessel-zero measures to 10⁻¹⁵" → 2·10⁻³¹ (refit_lommel.out; the old figure was the float64
   floor).
7. **SPEC §3.15.** p = 2: S = −π²/8 to 4·10⁻¹⁰ (was 10⁻⁶).
8. **JZC_M3a_H_G1u §5a.** Optional: the β′ = −2.1 rows sharpen (d₃ to 7·10⁻¹², ε₁ to 1.4·10⁻⁸).
9. **JZC_W2 §6 item 6.** Done by this note: the floor affected precision, not any verdict.

## 6. Rule A log

1. *Rule X.* No prediction was recomputed and used in place of a stored one. W′ (probe 2, M1) was recomputed with
   `w_common.predict(variant={'dressing'})` and asserted equal to the stored `predictions_probe2.json` to 10⁻²⁵. The outer run's control
   fields X and gauge1 are not in the stored file, so they were recomputed as w_outer_e2e does. Fit routines and pass rules were copied
   verbatim. The only change is the measure.
2. *Is the new generator right, or merely different?* Four independent checks (§1), including an exact closed form at 2·10⁻³¹ and an
   independent far-tail method at 10⁻³². The p < 1 panel resolution was checked separately (512 against 768 nodes).
3. *Generator bugs found during the audit.* Two (§1), both caught by their own signatures (σ_y unchanged; a 5·10⁻⁸ jump at p < 1) before
   any conclusion was drawn. The run-1 rows are void and kept in tmp/refit/stale/.
4. *Could corrected data only look better because the half-ranges shrank?* Every target was re-checked against its prediction under the
   original pass rule: with smaller half-ranges a wrong prediction would now fail more easily. None did. The deviations that remain at
   p < 1 (A06 n⁻²: −2.1·10⁻⁴; M2 n^{−3.5}: 4.9·10⁻⁵) are inside the new tolerances and the same as before, so they are not data.
5. *Not re-run* (bounded via §2 instead): W_plt1 (it uses an exact κ tail already), G1u_plt1, Hd model, SPEC §2, §3.10–§3.14, §3.16–§3.18, and
   the SPEC §3.15 rows other than p = 2. The §2 bounds come from the re-run families at the same n range and the same pipelines.
   Families with a tail correction larger than those re-run would need their own check; spec_kappa at p < 1 was the only one found.
6. *pkill.* A `pkill -f` pattern matched its own shell once; no data were affected. Two queued shell watchers deadlocked because each
   matched its own `pgrep -f` pattern. They were killed and the runs started by hand.

## 7. Files

`checks/refit_data.py`, `refit_validate.py/.out`, `refit_lommel.py/.out`, `refit_mpcheck.out`, `refit_w.py` → `refit_w_test.out`
(run 1; M1/A06 rows void), `refit_w_test2.out`, `refit_w_probe.out`, `refit_w_outer.out`; `refit_m4.py/.out`; `refit_spec.py/.out`;
`refit_subpole.py/.out`. Caches are in `tmp/refit/`. Old caches were read, never rewritten. Each `.out` prints the sha256 of its script and
of refit_data.py / w2_data.py.
