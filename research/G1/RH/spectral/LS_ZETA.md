# LS ZETA: are the primes heard in the Lanczos coefficients of the measure on reciprocal zeta ordinates? (PRE-REGISTRATION, then results)

Status (2026-10-27): **PRE-REGISTRATION + CALIBRATION FAILED (UNDERPOWERED)**; the registered run on the zeros was not performed (§3).
- §§1–4 were committed before `lz_zeta.py` read the zeros. The commit hash is the timestamp.
- §5 is added later and may not change §§1–4.
- Labels per VERIFICATION_POLICY.md: everything is NUMERICAL. The response mechanism is HEURISTIC (SPEC §3.18).
- Novelty: UNCHECKED.
- **No claim about RH, GRH or the zeros' location.** The ordinates are real-number inputs (item 11, E1). The prime-power
  oscillations of their counting function are classical (Riemann–von Mangoldt explicit formula). The question is only whether
  the Jacobi coefficients b_n of the measure on their reciprocals carry them.

Branch: lanczos-selberg. Scope: the follow-up recommended in LS_BOLZA §5.

## 1. Why this test (after LS_BOLZA)

LS_BOLZA failed as registered.
- On the arithmetic Bolza surface, b_n's residual was dominated by short-scale noise: rms 12, decorrelating within 5 n. That is
  consistent with Poisson-like level statistics (SPEC §§3.6, 3.18).
- Zeta ordinates have GUE statistics, which by §3.18 lowers the noise by a factor of 3–4.
- Their counting function has exactly known oscillations:

  N(T) = N̄(T) + S(T) + O(1/T),  S(T) ≈ −(1/π) Σ_{p^k} sin(kT log p)/(k p^{k/2}),

  with "lengths" log p^k: 0.693, 1.099, 1.386, 1.609, 1.946, 2.079, ….
- These oscillations are short-wavelength: about 2–5 zero spacings. So the slow-variation edge law of LS_BOLZA §2 does not
  apply. The relevant mechanism is the small-amplitude linear response of SPEC §3.18: a coherent sinusoidal displacement gives
  power ∝ n·κ(ω) at its own frequency. The positive control calibrates this.

## 2. Pipeline (`checks/lz_common.py`, `checks/lz_synthetic.py`)

- **Measure.** μ = Σ_{k≤4000} T_k^{−2} δ_{1/T_k}, plus a continuum tail beyond N̄ = 4000, shared by data and comparator. The
  tail is ρ̄(1/x)dx on (0, 1/T_end], by composite Gauss–Legendre on geometric panels.
- **Comparator.** The smooth nodes N̄(T_k) = k − ½, with N̄(T) = (T/2π)log(T/2π) − T/2π + 7/8.
- **Recurrence.** Lanczos with full reorthogonalisation, n < 2000.
- **Validation (V).** On a Hurwitz lattice, this pipeline reproduces the exact Arb pipeline (ls_common) to a relative 3.3·10⁻¹¹.
  The plain Stieltjes procedure was found unstable beyond n ≈ 15 and is not used.
- **Statistic.**
  - D_n = n(b_n/b_n^smooth − 1), normalised as D_n/√n.
  - CLEAN with k = 6 constant-amplitude sinusoids in T*(n), after a quadratic detrend.
  - T*(n) is the soft edge: ∫(1 − T/T*)^{−1/2} ρ̄ dT = n + ½.
  - n ∈ [40, 2000), so T* ∈ [69, 1325].
  - ℓ ∈ [0.3, 2.1] in steps of 0.002, below the Nyquist limit log(T*/2π) ≥ 2.4.
- **Null (N).** 200 GUE spectra (Dumitriu–Edelman β = 2, N = 8000, middle 60 %, unfolded, seeds 1–200), placed on the zero
  density. The detection thresholds A95 and A99 are the 95th and 99th percentiles of the first CLEAN amplitude.
- **Positive control (P).** 20 GUE spectra (seeds 1001–1020) with the truncated explicit formula (p ≤ 13, k ≤ 3) injected
  into the counting function.

## 3. Calibration (synthetic only; filled in from `lz_synthetic.out` before the real run)

From `checks/lz_synthetic.out`:
- **(V) passes.** Maximum relative error 3.3·10⁻¹¹ against Arb.
- **(N) null, 200 GUE spectra.** First-line amplitude: median 0.80, **A95 = 2.19, A99 = 2.97**. The first-line positions all fall in
  [1.168, 1.226], every one of the 200, which is not spread over [0.3, 2.1].
- **(P) positive control.** The first line is log 2 above A99 in **0/20**. On average 0.00 of the 5 registered lines are
  recovered. In every seed the CLEAN lines crowd into the same band, ℓ ≈ 1.16–1.22, whether or not the primes are injected.

**Diagnosis (post-calibration, before any real data).**
- For a single null spectrum, D_n/√n has rms 2.6, autocorrelation +0.50 at lag 10 and −0.37 at lag 2, and FFT peaks at 0.104
  cycles per step and its harmonic 0.208.
- This is the in-band ringing of the linear-response kernel, period ≈ 10 nodes (SPEC §3.18: "deeper in the band: O(3) per unit h,
  oscillating … period of about 2–3 in τ, i.e. about 10 nodes").
- It turns any displacement field into a quasi-periodic signal in n. In T*(n) that signal lands at ℓ ≈ 1.2, and it swamps the
  short-wavelength prime lines.
- A constant-amplitude sinusoid in T* is therefore the wrong model for the response to short-wavelength displacements. The
  readout of §2 cannot hear injected primes.

**Power: UNDERPOWERED** (0/20 < 15/20). Under §4 a FAIL would be uninformative.

**Registered decision (made now, before any real data).** `lz_zeta.py` is **not run** on the zeta ordinates. A test whose positive
control fails cannot inform. Running it anyway would invite post-hoc changes to the statistic on the real data.

## 4. Predictions (registered)

Let L = {log 2, log 3, log 4, log 5, log 7} and L⁺ = L ∪ {log 8}. Data: `tests/data/zeta_zeros_4000_dps60.txt`, sha256 pinned in
MANIFEST.sha256. Before use it is cross-checked against mpmath.zetazero at k = 1, 2, 3, 10, 100 and 1000.

- **(Z1)** CLEAN's first line on the real ordinates lies within ±0.02 of log 2, with amplitude > A99.
- **(Z2)** At least 3 of the 5 elements of L are recovered: some CLEAN line within ±0.02 of each, with amplitude > A99.
- **(Z3) Specificity.** Every CLEAN line with amplitude > A99 lies within ±0.02 of some element of L⁺.
- **Power statement.** If the positive control's first-line hit rate is < 15/20, the test is UNDERPOWERED. Then a FAIL of (Z1)
  or (Z2) is uninformative, and only a PASS would carry weight.

## 5. Results

**Not run (see §3).** The calibration showed that the registered statistic cannot recover injected explicit-formula lines.

**Reading, combined with LS_BOLZA.**
- *Long-wavelength* oscillations (Bolza geodesics) are carried coherently by b_n through the edge law, but on a real arithmetic
  spectrum they were buried in short-scale noise.
- *Short-wavelength* oscillations (primes at 2–5 zero spacings) excite the kernel's ≈ 10-node ringing and are not read out as
  lines.
- In both cases the information is in b_n, since b_n determines the measure, but not in a form that a direct local line search
  reads.

**What is consistent with the mechanism.** The variance-level statement of SPEC §3.18: Var D ≈ n∫κ(ω)S_h(ω)dω/π. Its natural
arithmetic version would compare the *power spectrum* of D_n for the zeros with the GUE null. The zeros' form factor departs from
GUE at a known, prime-dependent scale (Bogomolny–Keating). That would be a new pre-registration, not a rescue of this one.
