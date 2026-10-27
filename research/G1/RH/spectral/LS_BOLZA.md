# LS BOLZA: hearing the closed geodesics of the Bolza surface in Lanczos coefficients (PRE-REGISTRATION, then results)

Status (2026-10-27): **PRE-REGISTRATION**.
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

## 5. Results

(to be added after the data run; §§1–4 unchanged)
