# LS ZETA2: targeted per-frequency test for prime lines, and why b_n cannot hear them (CALIBRATION; real run not performed)

Status (2026-10-28): **CALIBRATION FAILED (UNDERPOWERED), MECHANISM QUANTIFIED**.
- The registered run on the zeta ordinates (`checks/lz2_zeta.py`) was **not performed**, under the same power rule as LS_ZETA
  §4.
- Everything here is NUMERICAL, on synthetic spectra only. The zeros were never read by this pipeline.
- **No claim about RH.** Novelty: UNCHECKED.

This follows LS_ZETA §3, whose global CLEAN threshold was set by the kernel's ringing band.

## 1. Mechanism experiments (synthetic; `checks/lz2_diag_*.py`)

**(R1) Single-node response, unit p = 1 lattice** (s = 2, node k₀ = 200, edge crossing at n* = 400.6).
- With the node inside the band (n < n*), the response rings: 123 sign changes for 61 zeros of P_n sweeping past the node, on
  n ∈ [200, 380). That is 2 sign changes per zero passage.
- With the node outside the band, there is no ringing: a smooth, decaying response, the S2′ regime.
- The kernel's in-band phase is therefore 2π × (number of zeros of P_n above the node).

**(R2) Sinusoidal displacement h_k = 0.02 sin(ωk).** The instantaneous frequency of D_n is ω/2 per n: 0.290, 0.472 and 0.741 for
ω = 0.6, 1.0 and 1.6.
- Since dλ*/dn = ½, the read-out is **edge-local**: D_n ≈ G(ω)·h(λ*(n)).
- The in-band stationary-phase root predicted the wrong frequency (median 2.7–3.8), so it is not the read-out point.
- So prime lines are sinusoids in T*(n), as LS_ZETA assumed.

**(LI) Linearity and background.** A log 2 sinusoid of amplitude ε is injected on the smooth zero lattice and on a GUE spectrum
(seed 7):
- The response is linear in ε up to ≈ 0.1–0.2: corr ≥ 0.98 at ε = 0.1 and 0.90 at ε = 0.2, against the ε = 0.005 response.
- **The coherent log 2 line per unit ε is 0.198 on the lattice but 0.059 on the GUE background, a loss of 3.4×.** The total
  response rms is comparable (0.73 and 0.99).
- The GUE configuration near the edge randomises the gain and the phase of the edge read-out. The response is spread over
  frequencies instead of sitting at log 2.

**(PA) Paired positive control** (same GUE seed with and without the injected explicit formula; seeds 1001–1020).
- The response per seed has rms ≈ 0.5, but it is dominated by seed-to-seed scatter (0.46).
- The coherent mean has rms 0.19, and its correlation with S_P(T*) is |corr| < 0.04 at every lag in [−3, 3].

## 2. Calibration of the targeted statistic (`checks/lz2_synthetic.py`, `lz2_synthetic.out`)

**Statistic.** The least-squares amplitude at fixed ℓ in y_n = D_n/√n versus T*(n), n ∈ [40, 2000), after a quadratic detrend.
The null is 200 GUE spectra, giving per-ℓ thresholds Q99(ℓ).

| ℓ | null median | Q99 | positive control median | positive above Q99 |
|---|---|---|---|---|
| log 2 | 0.0241 | 0.0567 | 0.0276 | 1/20 |
| log 3 | 0.0696 | 0.2880 | 0.0837 | 0/20 |
| log 4 | 0.0465 | 0.1612 | 0.0736 | 0/20 |
| log 5 | 0.0235 | 0.0844 | 0.0310 | 0/20 |
| log 7 | 0.0229 | 0.0549 | 0.0314 | 1/20 |
| controls 0.80–1.75 | 0.018–0.165 | 0.047–0.576 | — | 0.20 per seed (false-positive scale) |

**Power: UNDERPOWERED.** log 2 is detected in 1/20 seeds, and ≥ 3 of 5 lines in 0/20.

**Quantitative explanation.** The expected log 2 line is A₂ × G_GUE = 0.225 × 0.059 ≈ 0.013. The null median at log 2 is 0.024
and its Q99 is 0.057. With 4000 ordinates and n < 2000 the signal sits below the noise floor, consistent with the calibration.

## 3. Conclusion of the direct-readout programme (LS_BOLZA, LS_ZETA, LS_ZETA2)

- The fluctuations of b_n are **edge-local and linear** in small displacements of the spectrum. On realistic spectra,
  arithmetic-Poisson for Bolza and GUE for zeta, the configuration near the edge **scatters the coherent read-out** of any
  trace-formula oscillation.
- Long-wavelength geodesic oscillations survive in low-passed form (LS_BOLZA §5, post hoc: corr ≈ −0.6). Short-wavelength
  prime oscillations lose ≈ 3.4× coherence and fall below the noise.
- So b_n determines the measure, but trace-formula data is **not readable locally** from b_n at accessible n. The robust
  content of the Jacobi–zeta correspondence remains the smooth dictionary (Paper IV, JZC_P1) and the variance law (SPEC §3.18).
- **Open, not attempted:**
  - a configuration-conditioned read-out that estimates the edge gain and phase from the local node configuration (essentially
    re-deriving the spectrum, i.e. the inverse problem);
  - far larger n with Odlyzko's tables, where the coherent line (constant) and the per-frequency noise (∝ N_points^{−1/2})
    would cross at roughly 10× more points than here. That is beyond O(M n²) Lanczos.
