# CAUER: Cauer-ladder coefficients of a tapered RC line from the Paper IV dictionary

Status (2026-10-28): **NOT REVIEWED**. Labels per VERIFICATION_POLICY.md: NUMERICAL (`checks/cauer_taper.py` → `.out`, ALL PASSED).
The closed forms Z(−j) = −γ^{2j}/2 and d₅ are CONJECTURE: they are supported to 10⁻²²/10⁻¹⁵ and to 4–5 digits respectively, but
not proved. Novelty: UNCHECKED. The Lambert continued fraction for tanh is KNOWN, and so is the Cauer synthesis of RC impedances.

## 1. Why

The Stieltjes (S-) fraction of a sum of simple poles is a Cauer RC ladder:

  Z(s) = c₀/(1 + c₁s/(1 + c₂s/(1 + …))).

Its coefficients are exactly the "β_j" of the Carlitz recurrence. For the measure μ = Σ μ_k δ_{x_k} on reciprocal poles:
- b_n² = c_{2n−1}c_{2n};
- a_n = c_{2n} + c_{2n+1}.

So Paper IV's asymptotics of b_n, a_n are statements about ladder element values. The uniform diffusion line is the exact anchor:
- Z = tanh√s/√s;
- poles ((k−½)π)², i.e. p = 2 with the Hurwitz shift ½;
- c_k = 1/((2k−1)(2k+1)), which is Lambert's fraction and Paper IV's Bessel/Lommel case at μ = −½.

## 2. The tapered line (exact model)

**The line.** On x ∈ [0, 1] take series resistance e^{−2γx} and shunt capacitance e^{2γx} per unit length, with the far end
shorted. Then:
- the input impedance is Z(s) = 1/(γ + κ coth κ), with κ = √(s + γ²);
- the poles are λ_k = q_k² + γ², where tan q = −q/γ;
- the residues are ρ_k = 2(λ − γ²)/(λ + γ), an exact analytic mass tilt;
- the measure is μ_k = ρ_k/λ_k at x_k = 1/λ_k (p = 2, s = 2, α = −½);
- Z(0) = 0, so the natural index is N = n − ¼.

**Spectral data.**
- **Z(−j) = −γ^{2j}/2.** Hurwitz-regularised through the expansion of λ_k in (k − ½)⁻². Measured for j = 1, 2 at
  γ = ½, 1, 2: to 10⁻²² for j = 1 and 10⁻¹⁵ for j = 2. CONJECTURE for all j.
- **Mass tilt:** B_j = [−γ^{2j} + (−γ)^j]/j.
- **Density ("Jacobian") tilt of Conjecture W:** log D(x), with D = (dN̄/dλ)/(½λ^{−1/2}), from the exact counting function. To
  leading order this is the κ-family shift κ = (2γ + γ²)/π² (JZC_W_kappa), with B₁ = κ/2.

## 3. Results (NUMERICAL)

| check | result |
|---|---|
| (L) Lambert, γ = 0 | c_k(4k² − 1) = 1 to 2·10⁻¹² for k ≤ 300 (Lanczos with full reorthogonalisation + Gauss–Jacobi tail) |
| (K) κ-family (k − ½)² + κ | N⁻³ = −cκ to 4·10⁻⁷ for κ = 0.1, 0.25, −0.1; the Toda-time layer alone predicts 0, and the density tilt supplies −cκ |
| (T) N⁻³ | ε₁ = −γ²/16 exactly (t₁ = γ²/(2π²): zeta and mass tilt cancel at γ², and the density tilt restores γ²/2) |
| (T) N⁻⁵ | ε₂ + ε₁g₁ (g₁ = 9/8) = −75/4096, −21/256, −15/32 for γ = ½, 1, 2; measured within the float64 fit resolution (≤ 2.8·10⁻⁴) |
| (C) Cauer law | **c_k(4k² − 1) = 1 − γ²/(2k³) + 0·k⁻⁴ − (5γ²/4 + 3γ⁴/8)/k⁵ + O(k⁻⁶)**, the same for both parities; k⁻³ to 10⁻⁴, k⁻⁵ to 4–5 digits |

The k⁻⁵ coefficient is *derived*, not fitted. The dictionary's N⁻⁵ value is converted through b_n² = c_{2n−1}c_{2n}, and the three
values −43/128, −13/8 and −11 fix the closed form.

**Rule X.** The first comparison omitted the density tilt and got N⁻³ wrong: +γ/8 against the measured −γ²/16. Separating the
node effect from the residue effect located the missing term. The repo's own Conjecture W predictor (w_common.predict) already
contains it; the omission was mine.

## 4. Reading (engineering)

- **Element values carry the geometry.** The high-order Cauer element values of the line's impedance carry its taper:
  γ² = −2 lim k³[c_k(4k² − 1) − 1]. The correction is a k⁻³ effect on top of Lambert's ladder, with no k⁻² or k⁻⁴ term.
- **The general rule.** For a distributed RC line (a 1-D diffusion problem, p = 2) with poles λ_k and residues ρ_k, the ladder
  asymptotics are fixed by:
  - the regularised power sums Z(−j) of the poles;
  - the residue tilt;
  - the density tilt of the pole counting function.
- **This is the network-theory form of Paper IV's dictionary.**

## 5. Open

- N⁻⁶ and k⁻⁶, which need extended precision; the float64 fit cannot resolve them.
- A proof of Z(−j) = −γ^{2j}/2. It would follow if Z_q(−i) = 0 for i ≥ 1 and Z_q(0) = −½ for the roots of γ sin q + q cos q.
- Other tapers, open-circuited ends, and a measured thermal impedance (Foster → Cauer) as an applied test.
