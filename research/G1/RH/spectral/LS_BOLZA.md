# LS BOLZA: hearing the closed geodesics of the Bolza surface in Lanczos coefficients (PRE-REGISTRATION, then results)

Status (2026-10-27): **PRE-REGISTRATION** (§§1–4) **+ RESULTS** (§5: B1–B3 FAIL, B4 PASS; post-hoc diagnostics labelled EXPLORATORY).
- §§1–4 were written and committed before any Bolza eigenvalue was read by this pipeline. The commit hash is the timestamp.
- §5 (results) is added in a later commit and may not change §§1–4. Any deviation is recorded there under Rule X.
- Labels per VERIFICATION_POLICY.md: the edge law (§2) is NUMERICAL on synthetic spectra (`checks/ls_synthetic.py`) and
  HEURISTIC as derived.
- Novelty: UNCHECKED.
- No claim about RH: for compact surfaces the Selberg zeta analogue is classical, and nothing here concerns ζ.

Branch: lanczos-selberg (from p1-continuation).

## 1. Question

**Can the closed geodesics of a hyperbolic surface be read off the recurrence coefficients b_n of the measure on its reciprocal
eigenvalues?**

The smooth part of b_n is the Paper IV dictionary at p = 1 (JZC_P1). This note asks whether the fluctuating part carries the
length spectrum through the trace formula.

## 2. The edge law (derived and calibrated on synthetic spectra before the Bolza data)

**Setting.** Node counting N(λ) = N̄(λ) + N_osc(λ), with N̄ = νλ − a − ½ (a Hurwitz lattice, nodes (k + a)/ν). Let y_n be the
measure Σλ^{−s}δ_{1/λ}'s n b_n/c_eff − 1, with c_eff = ν/2. Define

  D_n := n(y_n − y_n^lattice).

**Claim.** For an N_osc that varies slowly on the scale of the edge kernel (about 10 spacings),

  D_n ≈ E[N_osc](n) := −½ f.p.∫₀¹ (1 − u)^{−3/2} N_osc(u λ*) du,   λ* = N/(2ν),   N = n + α/2 − Z(0).

**Derivation (HEURISTIC).**
- The linear response of D_n to displacing one node outside the band is (p²/2k)u(1 − u)^{−3/2}. This is the derivative of
  Theorem S2′'s law; SPEC §3.18 measured it on τ ≥ 2 to 1–3%.
- A smooth displacement field is −N_osc/ν in λ.
- Summing over the outside nodes and taking the Hadamard finite part at the Airy-smoothed edge gives the formula.
- For N_osc = A sin(ℓr), r = √(λ − ¼), its stationary part is −√π·A·√(ℓr*/2)·sin(ℓr* + π/4):
  - an amplitude gain of order √(ℓr*);
  - a phase offset of π/4.

**Calibration.** Synthetic spectra (`ls_synthetic.out`; ν = 2/5, p = 1, s = 2, n ∈ [40, 300], explicit nodes below 998 and an exact
Hurwitz tail):
- **One line at ℓ₀ = 3.0571:**
  - the edge law holds with corr −0.96 and slope −0.91 to −0.92, and the slope rises slowly with n;
  - the best index shift is the predicted natural index N = n + 4/5;
  - CLEAN finds ℓ₀ first, with phase ≈ −π/4.
- **Two lines plus jitter:** corr −0.82; CLEAN recovers both lines.
- **Nonlinearity:** CLEAN's next component is a second harmonic at 2ℓ₀, about ¼ of the main line's amplitude.

**Rule X.** The first synthetic run used the naive law D_n ≈ N_osc(λ*). It found the line, but with amplitude 3.70 against 0.5.
The edge law was then derived from the S2′ kernel and checked, all before any Bolza data.

## 3. Data and measure (fixed in advance)

**Data.** Strohmaier–Uski (2013): the 1000 non-zero Laplace eigenvalues of the Bolza surface, with multiplicity. The ancillary
file is `eig-bolza-refined0-1000.txt` (arXiv:1110.2150v4), verified against bolzakit's pinned sha256 869f48bc….

**Nodes.**
- The *distinct* eigenvalues, clustered at relative tolerance 10⁻⁹ as bolzakit does.
- b_n of the spectral measure sees each degenerate eigenvalue as one atom (SPEC §3.16). The node-counting function is therefore
  N_dist(λ), not the multiplicity count.

**Measures.**
- **(M1) primary:** μ = Σ_{distinct λ_i < λ_cut} λ_i^{−2} δ_{1/λ_i}, with the exact Hurwitz tail (k + a)/ν beyond λ_cut = 900.
- **(M2) secondary:** the same with masses m_i λ_i^{−2} (multiplicity-weighted).

**Smooth parameters.** ν and a come from a least-squares fit of N_dist(λ) = νλ − a − ½ on λ ∈ [50, 900]. These are two smooth
parameters, and they also define the comparator lattice.

**Fit range.** n ∈ [40, n_max], with n_max = min(300, ⌊1.2ν·900⌋), so that λ* ≤ 0.6 λ_cut.

**N_osc.** N_osc := N_dist − N̄, taken from the same eigenvalue list. It is the edge law's input, not a fit.

## 4. Predictions (registered)

**(B1) Edge law on a real spectrum.** corr(D_n, E[N_osc](n)) ≤ −0.6 on the fit range, with slope in [−1.3, −0.6].
- The threshold is weaker than the synthetic one.
- Bolza is arithmetic, so its counting function has large, Poisson-like short-wavelength fluctuations. SPEC §3.18 found those
  respond nonlinearly, with low pointwise correlation.
- Failure of (B1) would mean the edge law does not survive real spectral fluctuations.

**(B2) The systole is heard.** CLEAN (k = 5, ℓ ∈ [1, 8], grow = ½, natural-index shift) applied to D_n of (M1) finds a component
within ±0.12 of ℓ_sys = 2 arccosh(1 + √2) = 3.0571.

**(B3) b_n's lines are N_dist's lines.**
- The first three CLEAN components of D_n match, within ±0.12, three of the first five CLEAN components of E[N_osc], computed
  from the eigenvalues with no b_n involved.
- (B2) and (B3) together say that b_n carries the trace-formula oscillations of the counting function.

**(B4) Masses are a tilt.** (M2) gives the same first three lines as (M1), within ±0.12.

**Interpretive expectation (stated, not a pass/fail test).**
- N_dist is a combination of twisted trace formulas over the isometry group G: N_dist = |G|⁻¹ Σ_g (Σ_ρ χ_ρ(g)) tr(g·1_{Δ≤λ}).
- The g = e term carries the Bolza length spectrum (3.057, 4.897, 5.828, …).
- The terms g ≠ e carry lengths of the extended triangle-group orbifold, which may include lines shorter than the systole.
- A line that matches neither list would need explanation.
- A line at 2ℓ_sys = 6.114 could be either the genuine repeated geodesic or the nonlinear second harmonic (§2), so it is not
  counted as evidence.

## 5. Results (2026-10-27; §§1–4 unchanged)

**Data.** The Strohmaier–Uski file arrived through the chat (arXiv is blocked from both machines). It was transcribed and its
sha256 matches bolzakit's pin 869f48bc… byte for byte.
- 1000 eigenvalues, 334 distinct, with multiplicities {1: 42, 2: 43, 3: 124, 4: 125}.
- Smooth fit: ν = 0.333378 and a = 0.0443, so the distinct-eigenvalue density is ≈ 1/3.
- n ∈ [40, 300), natural-index shift 1.0443. Bits left ≥ 4632 in every run.

**Rule X, deviation 1 (mechanical).** The first run crashed on `mp.mpf(repr(np.float64))`. The fix converts with float() first. No
analysis choice changed. The script's sha256 changed from 2b71b9… to eac3e5…, and the diff is that one line.

**Registered outcomes (`checks/ls_bolza.out`):**

| prediction | registered | result | verdict |
|---|---|---|---|
| (B1) edge law on the real spectrum | corr ≤ −0.6, slope ∈ [−1.3, −0.6] | corr = −0.006, slope = −0.004 | **FAIL** |
| (B2) systole within ±0.12 of 3.0571 | among CLEAN's 5 lines | nearest line 3.205 (Δ = 0.148); it is the strongest line | **FAIL** |
| (B3) b_n's top 3 lines among N_osc's top 5 | ±0.12 | D_n: 3.205, 1.21, 7.745; E[N_osc]: 7.995, 5.725, 3.005, 1.92, 4.46 | **FAIL** |
| (B4) multiplicity masses act as a tilt | same top 3 | M1 and M2 lines agree (3.205/3.21, 1.21/1.20, 7.745/7.77) | PASS |

So, as registered, **the Lanczos coefficients of the Bolza spectrum do not demonstrably hear the systole.**

**Post-hoc diagnostics (EXPLORATORY; they do not change any verdict above):**
- **The E[N_osc] estimator was ill-posed for real data.** The data's N_osc is a step function. Its finite-part edge transform is
  dominated by the nodes nearest the edge: rms E = 28 against rms D = 12. The synthetic calibration only ever used smooth N_osc.
  This was a design flaw of (B1).
- **Smoothing does not fix it.** With N_osc Gaussian-smoothed over σ = 1.5–12 in λ, corr rises only to −0.11 … −0.16. At σ = 12
  the slope is −0.92, the size the edge law predicts.
- **The long-wavelength parts agree.** A moving average over W = 11–31 consecutive n of both D_n and E_σ=12 gives corr −0.58 …
  −0.61, with the predicted sign, and rms D_lp ≈ 2–4.
- **D_n is dominated by short-scale noise.** Its rms is 12, the lag-1 autocorrelation 0.39 and the lag-5 autocorrelation 0.08.
  This is consistent with SPEC §3.18 (the noise has the variance of a linear statistic, not its realisation) and with the
  Poisson-like level statistics of an arithmetic surface. At these n the noise is larger than the geodesic signal.
- **The strongest CLEAN line, 3.205, is within the ℓ-resolution of the window (≈ 2π/Δr* ≈ 0.47) of the systole.** That is
  suggestive, not evidence, because no null distribution has been computed.

**Reading.**
- The coherent part of the edge law is plausibly present at long wavelength, with the right sign and size.
- On Bolza, with 1000 eigenvalues, it sits under a short-scale noise floor that the registered tests did not anticipate.
- The registered claim, "b_n hears the systole", is not supported by this run.

**What a fair next test needs (to be pre-registered afresh, not run on this data as if new):**
1. A null distribution for CLEAN's top line, from spectra with Bolza's smooth part and Poisson-like or GOE-like fluctuations but
   no injected lines.
2. A low-pass protocol fixed in advance (W, or a filter in r*).
3. Independent data: another surface, Bolza eigenvalues beyond 998, or a non-arithmetic genus-2 surface, whose GOE-like rigidity
   should lower the noise floor by the factor 3–4 of §3.6.
