# RH_plt1b: pointwise Law P for σ_{p,s}, all 0 < p < 1 — the seam construction (Plan 15b)

Status: **REVIEWED** (Rule R: ACCEPT WITH FIXES, review/REVIEW_RHplt1b.md; F1–F9 applied and re-checked). There is **no
numerical caveat**: Lemma S(iii) is now proved (F2). This document covers every 0 < p < 1. For ½ < p < 1 it agrees
exactly with RH_plt1's B-construction (Liouville, §4), and it removes RH_plt1's NUMERICAL F4 dependence.

It is a delta to RH_px.md (p > 1, REVIEWED) and to RH_plt1.md's amendments table (§0 there), which is p-free once D̃
is confined to the inner sector.

## 0. Why the B-construction stops at ½

On the continued sheets, D_up has two defects (RH_plt1 §6):
- phantom poles at t = k ∈ ℕ on arg t = −2π, i.e. on arg z = 2πp ≤ π;
- beyond arg t = −2π it is exponentially small or large.

So for p ≤ ½ the Binet-cut scalar B on (−∞, 0) does not exist. The fix is to use D **only in an inner sector** and to
glue along two seam rays with an exact scalar.

## 1. The scalar F

**Angles** (Rule R F1). For every 0 < p < 1 put θ_L := πp/4 (the lip angle) and θ_s := πp/2 (the seam angle). Let
S_in := {|arg z| < θ_s} and S_out := ℂ ∖ (S̄_in ∪ {0}).
- In S_in, |arg t| = |arg z|/p < π/2. So D̃ = exp(−μ(t)) is given by the principal formula, is analytic and zero-free,
  and D̃ = 1 + O(1/|t|) (DLMF 5.11.1).
- D = D̃/(1 − e^{∓2πit}) has its poles at the nodes. On closed subsectors ε ≤ |arg z| < θ_s, D = 1 + O(1/|t|), with
  |e^{∓2πit}| ≤ exp(−2π sin(|arg t|)|t|) (Rule R F4).

**Factors.** Put c := ½ − 1/(2p) and:
- B_in(z) := (1 + z)^c, analytic off (−∞, −1] ⊂ S_out;
- B_out(z) := (1 − z/(2πN))^{1/2}, analytic off [2πN, ∞) ⊂ S̄_in;
- K := (4c(p) − z)^{−1/2}, as in RH_px.

**Lemma S.** On the seam rays Γ± := {re^{±iθ_s}}, put

  L± := −μ(t) − Log(1 − e^{∓2πit}) + c·Log(1 + z) − ½Log(1 − z/(2πN)),

with all logarithms principal, μ(t) := ½log 2π + (t − ½)Log t − t − LogΓ(t), and Log t := log N − Log z/p. Then
e^{L±} = D·B_in/B_out, and:
- **(i)** L± = O(|z|) as z → 0. Here D − 1 = O(|z|^{1/p}/N) = O(|z|), and B_in/B_out − 1 = O(|z|).
- **(ii)** As z → ∞, D·B_in/B_out = 1 + O(N|z|^{−1/p}log|z| + 1/|z| + N/|z|).
- **(iii)** L± is continuous on the open ray, tends to 0 at 0, and tends to 0 at ∞. So it is the continuous determination
  vanishing at 0, and it has **no winding**.

*Proof* (Rule R F2). On Γ₊, arg t = −θ_s/p = −π/2.
- **Continuity.** Each term is continuous on the open ray:
  - μ is analytic off (−∞, 0];
  - |e^{−2πit}| = e^{2π Im t} < 1, so 1 − e^{−2πit} stays in |w − 1| < 1;
  - 1 + z avoids (−∞, 0], since arg z = θ_s ∈ (0, π);
  - 1 − z/(2πN) has nonzero imaginary part.
- **At 0** (t → ∞): each term → 0, by DLMF 5.11.1 for μ.
- **At ∞** (t → 0):
  - −μ = ½log 2π + ½Log t + O(|t|log|t|), using LogΓ(t) = LogΓ(1 + t) − Log t;
  - Log(1 − e^{−2πit}) = log 2π + iπ/2 + Log t + O(t), since π/2 + arg t ∈ (−π/2, π/2);
  - c·Log(1 + z) = c·Log z + O(1/z);
  - Log(1 − z/(2πN)) = Log z − log 2πN − iπ + O(N/z), since arg(1 − z/2πN) → θ_s − π.
- Collecting terms, with Log t = log N − Log z/p:
  - the real part is (1/(2p) + c − ½)log|z| − ½log 2π − ½log N + ½log 2πN = 0;
  - the imaginary part is θ_s/(2p) − π/2 + cθ_s − ½(θ_s − π) = 0.
  The remainders give (ii). Γ₋ follows by conjugation. ∎

`checks/check_plt1_seam_winding.out` (57 values of (p, N); end values ≈ 10⁻³¹) is a consistency check of exactly this
sum of principal logs.

**The seam scalar.** X(z) := (1/2πi)[∫_{Γ₊}L₊(ζ)dζ/(ζ − z) − ∫_{Γ₋}L₋(ζ)dζ/(ζ − z)], with both rays oriented outward.
- Γ₊ has S_out on its left. So by Plemelj X_out − X_in = L₊ on Γ₊, and likewise X_out − X_in = L₋ on Γ₋.
- **Boundary behaviour** (Rule R F5).
  - The density is real-analytic on the open rays, Lipschitz at 0 with value 0, and O(1/|ζ|) at ∞.
  - Hence X is bounded and Hölder up to each ray, continuous at the corner 0, and X → 0 at ∞. This is RH_px Lemma 3.4's
    half-line case applied to each ray after rotation; at 0 the density vanishes, so there is no corner singularity.
  - X(0) = (1/2πi)Σ±(±)∫L±dζ/ζ, the same value from every sector.
- **N-dependence** (Rule R F3).
  - |X| = O(log N), because max|L| ≍ log N on the seams. A probe at p = 0.4 gives X(0) = −1.24, −1.93, −3.31, −4.70 for
    N = 10, 10², 10⁴, 10⁶.
  - X − X(0) has N-uniform Lipschitz bounds on compacts, since ∫|L(ζ)||ζ|^{−2}|dζ| is N-uniformly bounded.
  - Constants in X cancel between w₀'s Szegő function, D_{w,∞} and C_∞. The top end needs only poly(N) ≪ N^{pN}.
  - So only "h_N modulo constants is N-uniformly Hölder" is used. This is an amendment to RH_plt1 §0, in the same spirit
    as its F3.

**F := D·B_in·K·e^X on S_in, F := B_out·K·e^X on S_out.** Then:
- F is continuous, hence analytic, across Γ±;
- F has no jump on (−∞, 0); **no B is needed**;
- on the positive axis F has exactly D·K's jumps (RH_px Lemma 3.3(ii));
- F → F_∞ = (2πN)^{−1/2} at ∞, consistent in all directions. So RH_px Lemma 3.5 holds, with κ bounded and jump-free
  beyond N^p + δ′.

F̃ := D̃·B_in·K·e^X is used in the band lens and in Ω^△. The band weight is w₀ = W(4c − x)/(D̃B_ine^X)².

## 2. Geometry, hard edge, (Y4)_x

- **Containment** (Rule R F1, F9).
  - The KMVV rays are taken at angle π − θ_L, so the lips leave 0 at ±θ_L = ±πp/4. KMVV (§6, after (6.21)): "we have
    chosen the angle 2π/3 rather arbitrarily. It could be replaced by any angle in (0, π)". (6.23)–(6.25) are then used on
    the sectors |arg ζ| < π − θ_L etc., where the Bessel and Hankel asymptotics hold uniformly.
  - The band lens in U(0, δ) lies in S_in.
  - Outside U(0, δ), the lens and Σ^△ heights are chosen below δ·tan(θ_s)/2 at Re z ≥ δ (p-dependent, N-free). The top
    closing segment at N^p + δ′ ± iδ has arg ≈ δ/N^p.
  - So all of them lie in S_in. The Lemma 4.3 lip constant is c = 2π sin(θ_L/p) = 2π sin(π/4).
- **Hard edge** (Rule R F8). W̃ := (C(−z)^{α_x}(4c − z))^{1/2}/G̃, with one principal root and G̃ := D̃·B_in·e^X in S_in
  and G̃ := B_out·e^X in S_out ∩ U(0, δ), for δ < 1.
  - The lips are reproduced exactly in S_in.
  - On the seams, W̃_out/W̃_in = D̃B_ine^{X_in}/(B_oute^{X_out}) = D̃/D = 1 − e^{∓2πit}, with
    |e^{∓2πit}| = exp(−2πN|z|^{−1/p}) at θ_s = πp/2. This is super-small, and is handled by RH_px Lemma 4.2(iii)'s split
    Ẽ_N = E^a + Φ.
  - Removability: D_w/W̃ is bounded above and below near 0 in both sectors, since B_in, B_out, e^X are Hölder and nonzero
    at 0, and D̃(0⁺) = 1.
- **(Y4)_x.** The sum bound is p-free. The lens-sector argument needs Im θ < 0 on 0 < arg s < φ₀ (and the mirror image),
  i.e. only φ₀ < πp (Rule R F9). p > ½ is not needed.
- Everything else is as in RH_plt1's amendments table (p-free once D̃ is confined to S_in): μ* (G2, all p > 0),
  Lemmas 2.1–2.2, Airy, top end, small norm, extraction.

## 3. Theorem

**Theorem RH_p (0 < p < 1; PROVED-mod-cite (WLXZ; KMVV §6 including the angle-freedom remark; G2 μ*/B*; DLMF 5.11),
REVIEWED; no numerical caveat).** For 0 < p < 1 and s > 1:

  n^p b_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

With RH_px (p > 1) and RH₁(r) (p = 1), this gives **the pointwise Law P with an O(1/n) rate for all pure powers with
power weights**, with no numerical caveat.

## 4. Numerical validation (`checks/check_plt1_seam_e2e.py`; Ω_∞ points only)

N·max|D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}|:

| (p, s) | N | 1.2+i | 0.5+0.8i | −1+0.5i | −1.5 | 2.5i | 4.5+1.5i | 3−1.2i | 15+8i | −6−3i | −0.4+0.3i | −0.3−0.05i |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (0.4, 2) | 10 | 0.447 | 0.530 | 0.464 | 0.358 | 0.242 | 0.167 | 0.268 | 0.041 | 0.093 | 0.942 | 1.496 |
| (0.4, 2) | 20 | 0.461 | 0.561 | 0.485 | 0.375 | 0.253 | 0.173 | 0.277 | 0.042 | 0.097 | 0.987 | 1.570 |
| (0.4, 2) | 40 | 0.467 | 0.577 | 0.497 | 0.383 | 0.258 | 0.176 | 0.281 | 0.043 | 0.099 | 1.012 | 1.610 |

- N·error is stable. N^p b_N/c = 0.947, 0.974, 0.987 at p = 0.4, N = 10, 20, 40, consistent with d₁ = −½.
- `check_plt1_seam_e2e_p075s2.out`: the (0.75, 2) N = 20 seam run, for comparison with RH_plt1 §5.
- For p = 0.4, the points 4.5 + 1.5i, 3 − 1.2i and 15 + 8i lie in S_in, and the others in S_out.
- **Liouville identity** (Rule R F6). For ½ < p < 1 the seam F equals const·D·B (same jumps, same behaviour at 0 and ∞).
  So the seam and B-probes must agree exactly.
  - The reviewer's runs (not committed) at p = 0.75, N = 10 agree to all printed digits at 0.6 + 0.45i, 0.6 + 0.55i, −1.5 + 0.05i and
    −1.5 + 0.3i, and at the ten table points off the axis.
  - At −1.5 + 10⁻⁴⁰i the seam value 0.161 is the correct one. The B-probe's 0.283 is a quadrature artifact (its S(z)
    quadrature misses the half-residue). RH_plt1 §5's −1.5 column is corrected accordingly.
- **Scope** (Rule R F7). This gate does not test the glued W̃, the KMVV angle π − θ_L, or P₀N^{−1} on ∂U(0, δ). Porting
  `check_px_bessel.py` [B] to p = 0.4 is recommended.
