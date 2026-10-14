# RH_plt1b: pointwise Law P for σ_{p,s}, 0 < p ≤ ½ — the seam construction (Plan 15b)

Status: **PROOF (delta to RH_px.md and RH_plt1.md), pending Rule R.** It holds modulo one NUMERICAL no-winding fact
(Lemma S(iii)), which is the analogue of RH_plt1's F4. The construction also works for ½ < p < 1, which gives a second
proof there that needs no Binet-cut scalar B.

## 0. Why RH_plt1 stops at ½

On the continued sheets (RH_plt1 §6) D_up has two defects:
- phantom poles at t = k ∈ ℕ on arg t = −2π, i.e. on arg z = 2πp ≤ π;
- beyond arg t = −2π it is exponentially small or large.

So D cannot be used near the negative axis, and B (built from ℓ̂ = 2arg D₊ on (−∞, 0)) does not exist. The fix is to
use D **only in an inner sector** and to glue along two seam rays with an exact scalar.

## 1. The scalar F

Fix θ_s ∈ (0, πp), for instance θ_s := πp/2, and let S_in := {|arg z| < θ_s}, S_out := ℂ ∖ (S̄_in ∪ {0}).
- In S_in: |arg t| = |arg z|/p < π/2. So D̃ = exp(−μ(t)) and D = D̃/(1 − e^{∓2πit}) are given by the principal formulas.
  They are analytic and zero-free off the positive axis, with D = 1 + O(1/|t|) (DLMF 5.11.1 for Γ(t)) and
  |e^{∓2πit}| ≤ exp(−2π sin(|arg t|)|t|).
- Put
  - B_in(z) := (1 + z)^{c}, with c := ½ − 1/(2p) (analytic off (−∞, −1], which is in S_out);
  - B_out(z) := (1 − z/(2πN))^{1/2} (analytic off [2πN, ∞), which is in S̄_in);
  - K := (4c(p) − z)^{−1/2}, as in RH_px.
- **Lemma S.** On the seam rays Γ± := {re^{±iθ_s}}, put L±(z) := log(D(z)B_in(z)/B_out(z)), with the continuous
  determination along Γ± that vanishes at 0. Then:
  - (i) L±(z) = O(|z|^{min(1,1/p)}/N + |z|) as z → 0. More precisely, D − 1 = O(|z|^{1/p}/N) and
    B_in/B_out − 1 = O(|z|).
  - (ii) At ∞, D ~ ∓it^{−1/2}/√(2π) (small t; RH_px Lemma 3.1(iv)). Hence
    D·B_in ~ ∓iN^{−1/2}z^{1/2}/√(2π) = N^{−1/2}(−z)^{1/2}/√(2π) on Γ± (the phases agree exactly because the total
    power is ½: −iz^{1/2} = (−z)^{1/2} on Γ₊, and +iz^{1/2} = (−z)^{1/2} on Γ₋), while B_out ~ (2πN)^{−1/2}(−z)^{1/2}.
    So D·B_in/B_out → 1 + O(N|z|^{−1/p}log|z| + 1/|z|).
  - (iii) **No winding:** the continuous L± tends to 0 (not 2πik) at ∞.
    - In the variable t (arg t = ∓θ_s/p fixed), D is N-free and B_in/B_out = √(2π)t^{1/2}(1 + O(1/z)) up to the phase. So
      the condition is N-independent as N → ∞.
    - **NUMERICAL** (`checks/check_plt1_seam_winding.out`): for p = 0.05, 0.10, …, 0.95 and N = 10, 10², 10⁴ (57
      cases), tracking |z| ∈ [10⁻⁴⁰, 10⁴⁰], every step is < 0.5 rad and the end value is |L| < 2·10⁻³¹. So there is no
      winding. The probe's F_∞ also agrees in two directions to 10⁻⁸ at p = 0.4. A Lemma Z-type Arb certificate is not yet
      done.
- **The seam scalar.** X(z) := (1/2πi)[∫_{Γ₊}L₊(ζ)dζ/(ζ − z) − ∫_{Γ₋}L₋(ζ)dζ/(ζ − z)], with both rays oriented outward.
  - The densities are O(|ζ|^{min(1,1/p)}) at 0 and O(|ζ|^{−1}) at ∞ by (i)–(ii), so X is bounded and Hölder up to the
    seams, X → 0 at ∞, and X is Hölder at 0.
  - By Plemelj, X_out − X_in = L± on Γ±.
- **F := D·B_in·K·e^X on S_in, and F := B_out·K·e^X on S_out.** Then:
  - F is continuous, hence analytic, across Γ±;
  - F has no jump on (−∞, 0), since B_out, K and e^X are analytic there. **No Binet-cut scalar is needed.**
  - On the positive axis F has exactly D's jumps (RH_px Lemma 3.3(ii)) times K's;
  - F → F_∞ ≠ 0 at ∞ (F ~ (−z)^{1/2}(−z)^{−1/2}·const in S_out). So RH_px Lemma 3.5's normalization holds with κ bounded
    and jump-free beyond N^p + δ′.
- F̃ := D̃·B_in·K·e^X is used in the band lens and Ω^△ (all inside S_in). The band weight is
  w₀ = W(4c − x)/(D̃B_ine^X)², and h_N is Hölder at 0 (B_in, e^X Hölder; D̃ as in RH_px Lemma 3.4's consequence).

## 2. Geometry, hard edge, (Y4)_x

- **Lens angle.** The KMVV lips leave 0 at arg z = ±(π − ray angle). With KMVV's choice 2π/3 they are at ±π/3 ("we
  have chosen the angle 2π/3 rather arbitrarily. It could be replaced by any angle in (0, π)", KMVV §6, CITATIONS).
  - For p ≤ ⅓, take the Ψ-rays at angle π − θ_L with θ_L < θ_s, so that the lips lie in S_in.
  - Σ^△ and the band lens near 0 are thin, so they also lie in S_in.
- **Hard edge.** Glue W̃ as in RH_plt1 §3:
  - (C(−z)^{α_x}(4c − z)/(D̃B_ine^X)²)^{1/2} in S_in;
  - (C(−z)^{α_x}(4c − z)/(B_out e^X)²)^{1/2} in S_out ∩ U(0, δ). Here B_out e^X = F/K is the outer counterpart of
    D̃B_ine^X. It is analytic and nonzero in S_out ∩ U(0, δ) for δ < 1, with no cut on (−δ, 0).
  - The seam jump: W̃_out/W̃_in = D̃B_ine^{X_in}/(B_oute^{X_out}) = D̃B_in/(B_out·e^{L±}) = D̃/D = 1 − e^{∓2πit}
    = 1 + O(exp(−2π sin(θ_s/p)N|z|^{−1/p})). This is super-small, exactly as in RH_plt1 §3.
  - The removability bound holds because B_in, B_out and e^X are all Hölder and nonzero at 0.
- **(Y4)_x.** The sum bound is p-free. The lens-sector argument (RH_px §5) uses the sector G = {|arg s| < φ₀}, with Im θ < 0
  needed only there. Choose φ₀ < θ_s < πp. The overlap with the "away from the band" argument (δ₀ ≤ |arg z| ≤ π) needs
  only δ₀ < φ₀. So p > ½ is **not** needed.
- Everything else (μ*, Lemmas 2.1–2.2, Airy, top end, small norm, extraction) is as in RH_plt1's amendments table,
  which is p-free once D̃ is confined to S_in.

## 3. Theorem

**Theorem RH_p (0 < p < 1; pending Rule R).** For 0 < p < 1 and s > 1, modulo the NUMERICAL Lemma S(iii):

  n^p b_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

With RH_px (p > 1) and RH₁(r) (p = 1), this gives the pointwise Law P with an O(1/n) rate for **all pure powers with
power weights**.

## 4. Numerical validation (`checks/check_plt1_seam_e2e.py`; Ω_∞ points only, as in RH_plt1 §5)

N·max|D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}|:

| (p, s) | N | 1.2+i | 0.5+0.8i | −1+0.5i | −1.5 | 2.5i | 4.5+1.5i | 3−1.2i | 15+8i | −6−3i | −0.4+0.3i | −0.3−0.05i |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (0.4, 2) | 10 | 0.447 | 0.530 | 0.464 | 0.358 | 0.242 | 0.167 | 0.268 | 0.041 | 0.093 | 0.942 | 1.496 |
| (0.4, 2) | 20 | 0.461 | 0.561 | 0.485 | 0.375 | 0.253 | 0.173 | 0.277 | 0.042 | 0.097 | 0.987 | 1.570 |
| (0.75, 2) | 10 | 0.391 | 0.291 | 0.190 | 0.161 | 0.160 | 0.161 | 0.293 | 0.032 | 0.060 | 0.267 | 0.332 |

- N·error is stable, and N^p b_N/c = 0.947, 0.974 at p = 0.4, N = 10, 20, consistent with d₁ = −½.
- At p = 0.75 the seam construction reproduces the B-construction at the ten points away from the negative axis, and
  stays O(1/N) at −1.5.
- (N = 40 at p = 0.4 is running; results are appended to check_plt1_seam_e2e_p04s2.out.)
