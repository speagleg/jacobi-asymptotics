# RH_plt1: pointwise Law P for σ_{p,s}, ½ < p < 1 (Plan 15)

Status: **PROOF (delta to RH_px.md), pending Rule R.** It covers ½ < p < 1 and every s > 1. The range 0 < p ≤ ½ is
open (§6).

Everything not stated here is RH_px.md verbatim (Plan 12, REVIEWED): transformations, μ*, Lemmas 1.2, 2.1, 2.2, 3.3,
3.5, the Airy parametrix, the top end, and the small-norm extraction. The hard edge is RH_px §4.1 with a glued W̃ (§3). The only p > 1 input of RH_px is Lemma 1.1, which is replaced
by Lemma 1.1′ below.

## 0. Target and baseline

**Target.** n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n), for ½ < p < 1 and s > 1.

**Baseline** (NUMERICAL, `checks/check_plt1_phase0.out`; exact atoms plus a log-panel Euler–Maclaurin tail; K-stability
≤ 10⁻¹⁰ for n ≤ 200): n(n^p b_n/c(p) − 1) = −0.5000 (p = ¾, s = 2), −0.504 (p = ½, s = 2), −1.007 (p = ½, s = 3) at
n = 400. So d₁ = −(s − 1)/2, as for p > 1 (RH_px §0).

## 1. The continued D-function

The obstruction (RH_px Lemma 1.1) concerns D̃ = √(2π)t^{t−½}e^{−t}/Γ(t). For p < 1, 1/Γ(t) has zeros at
t = −1, −2, … on the rays arg z = ±πp. The combination that RH_px actually uses in Ω_∞ is D = D̃/(1 − e^{∓2πit}),
and that combination is better behaved.

**Lemma 1.1′.** Let ½ < p < 1. In ℂ₊ put log t := log N − (1/p)Log z, so that arg t ∈ (−π/p, 0) ⊂ (−2π, 0). Then

  D_up(z) := D̃/(1 − e^{−2πit}) = t^{t−½}e^{−t}e^{iπt}Γ(1 − t)/(i√(2π))

holds as an identity of meromorphic functions, and D_low(z) := conj D_up(z̄). Moreover:
- (i) D_up is analytic and zero-free in ℂ₊. Its only singularities in the closed half-plane are poles at the nodes
  X_k (t = k, on arg t = 0⁻), exactly as in RH_px.
- (ii) Uniformly on {z ∈ ℂ₊ : |t| ≥ 1, arg t ∈ [−π/p, −η]} for each η > 0, D_up = 1 + O(1/|t|).
- (iii) On (−∞, 0): D₊/D₋ = e^{iℓ̂}, with ℓ̂ = 2arg D₊ real and continuous. Near 0, ℓ̂(x) = O(|x|^{1/p}/N), and
  ℓ̂(−∞) = π/p − π.
- (iv) |D| ~ |t|^{−1/2}/√(2π) as z → ∞.

*Proof.*
- **Identity.** Use 1/Γ(t) = Γ(1 − t)sin(πt)/π (DLMF 5.5.3) and sin(πt)/(1 − e^{−2πit}) = e^{iπt}/(2i).
- **(i)** t^{t−½} = exp((t − ½)log t) is analytic and zero-free on the simply connected ℂ₊. Γ(1 − t) is zero-free,
  with poles only at t = 1, 2, …, i.e. at t real positive. Here arg t ∈ (−π/p, 0) with π/p < 2π, so t is real positive
  only on the boundary ray arg t = 0, i.e. at the nodes.
- **(ii)** Apply DLMF 5.11.1 (n = 1, with the sec² remainder bound) to Γ(1 − t).
  - Since arg t ∈ [−π/p, −η], the angle of 1 − t from the negative real axis is at least min(η, 2π − π/p) > 0, and
    the sector condition holds.
  - Use the continuous branch log(1 − t) = log t − iπ + log(1 − 1/t), valid because −t = te^{−iπ} has
    arg ∈ (−π/p + π, π) ⊂ (−π, π).
  - Then the exponent of D_up is
    (t − ½)log t − t + iπt + (½ − t)log(1 − t) + (t − 1) + ½log 2π − log(i√(2π)) + O(1/t)
    = (t − ½)log t − t + iπt + (½ − t)(log t − iπ) + (t − 1) − log i + O(1/t) + (½ − t)log(1 − 1/t).
  - The log t terms cancel, and iπt + (½ − t)(−iπ) = iπ/2. Also (½ − t)log(1 − 1/t) = 1 + O(1/t). So the exponent is
    iπ/2 − log i + O(1/t) = O(1/t).
- **(iii)** Conjugation symmetry gives D₋ = conj D₊ on (−∞, 0).
  - As x → 0⁻, |t| = N|x|^{−1/p} → ∞ with arg t = −π/p ∈ (−2π, −π) fixed, so (ii) gives D₊ = 1 + O(|x|^{1/p}/N).
  - The limit at −∞ is RH_px Lemma 3.1(iii) verbatim: small t, D₊ ~ −it₊^{−1/2}/√(2π).
- **(iv)** As in RH_px. ∎

**Consequences.**
- B (RH_px Lemma 3.2) exists:
  - ℓ̂ is Lipschitz at 0⁻ (1/p > 1), so the ν of Lemma 3.2(ii) is ½;
  - B ~ Cz^{½−1/(2p)} at ∞;
  - B/B(1) = 1 + O(1/N) on compacts.
- F := DBK has no jump on (−∞, 0) (Lemma 3.3), and Lemma 3.5 (normalization at ∞) is unchanged.

## 2. Where D̃ itself is used: thin lenses

D̃ (not D) enters:
- F̃ := D̃BK in the band lens and in Ω^△;
- the band weight w₀ = W(4c − x)/(D̃B)².

For p < 1, D̃ has zeros on arg z = ±πp. So:
- **Lens and Ω^△ geometry.** All lens lips and Σ^△ contours lie in |arg z| < πp/2.
  - There arg t ∈ (−½π, 0), D̃ = exp(−μ(t)) = 1 + O(1/|t|), and |e^{∓2πit}| ≤ exp(−2π sin(arg … )|t|) decays.
  - The (h1) entries D/D̃ − 1 = O(exp(−c|t|)) are super-small near 0, as in RH_px Lemma 4.3.
  - RH_px Lemma 2.2's signs are local to the axis, so they hold in thin lenses.
- **w₀ only on the band.** w₀ is used on (0, 4c), and in the lens through its continuation into |arg z| < πp/2 (no
  zeros of D̃ there). It is **not** continued around 0. §3 glues W̃ instead.

## 3. Hard edge: RH_px §4.1 with a glued W̃

RH_px §4.1 builds W̃ = (C(−z)^{α_x}(4c − z)h_N)^{1/2}, with h_N ∝ (D̃B)^{−2} continued to the punctured disc U(0, δ).
For p < 1, D̃ has zeros on arg z = ±πp accumulating at 0, so h_N cannot be continued that way. **Glue instead.**
- In S_lens := {|arg z| < πp/2} (which contains the lips and Σ^△ near 0, §2): W̃ := (C(−z)^{α_x}(4c − z)/(D̃B)²)^{1/2},
  exactly as in RH_px. So the lip jumps are reproduced exactly.
- In U(0, δ) ∖ S̄_lens: W̃ := (C(−z)^{α_x}(4c − z)/(DB)²)^{1/2}. D is analytic and zero-free there (Lemma 1.1′(i); no
  nodes off the positive axis), and DB is continuous across (−∞, 0) (§1). So this W̃ is analytic in that sector, with
  (−z)^{α_x} principal (cut on [0, ∞)).
- On the glue rays arg z = ±πp/2, W̃ jumps by (D/D̃)^{∓1} = (1 − e^{∓2πit})^{±1}.
  - On these rays arg t = ∓π/2, so |e^{∓2πit}| = e^{−2π|t|} = exp(−2πN|z|^{−1/p}). This jump is super-small.
  - It is of exactly the type that RH_px Lemma 4.2(iii) handles for its (h2) jump on (−δ, 0): split Ẽ_N = E^a + Φ,
    where Φ is the Cauchy integral of the super-small jump, with density O(|y|^{−1/2}exp(−cN|y|^{−1/p})), hence
    O(e^{−c′N}). E^a is analytic in the punctured disc with at most a square-root singularity (RH_px Lemma 3.4's
    consequence, h_N Hölder), so it is analytic.
  - In the error matrix the glue jumps are O(N^{−K}min(1, |z|^K)) after the polynomial amplification by P₀, as in
    RH_px Lemma 4.3.
- With this W̃, RH_px Lemmas 4.1–4.3 hold verbatim:
  - f is the same conformal map, since φ depends only on μ*;
  - the Bessel order is α_x = (s − 1 − p)/p > −1;
  - KMVV's left-endpoint construction (6.42)–(6.53) and the matching P₀N^{−1} = I + O(1/N) are unchanged.
- No comparison argument is needed: there is no log factor, and every mismatch is super-small. (The comparison method
  of RH_zeta_close.md §1 would also work for |α_x| < 1, but this route covers all s > 1.)

## 4. Assembly

**Theorem RH_p (½ < p < 1; pending Rule R).** For ½ < p < 1 and s > 1,

  n^p b_n = c(p)(1 + O(1/n)),  a_n/(2b_n) = 1 + O(1/n).

*Proof.* RH_px §§1–5 with Lemma 1.1′ (§1), thin lenses (§2), and the glued hard-edge W̃ (§3). ∎

## 5. Numerical validation (Gate G1; `checks/check_plt1_e2e.py`, adapted from the RH_px Rule R probe)

D is evaluated by the continued closed form of Lemma 1.1′, with guard digits ≈ 2log₁₀|t| for the cancellation. D̃ on
the band uses Binet's series for |t| > 10³. The test points include three beyond arg z = πp (where D̃ has zeros):
−1 + 0.5i, −0.4 + 0.3i, −0.3 − 0.05i.

The tables give N·max|D_∞^{−σ₃}(VN^{−1} − I)D_∞^{σ₃}|:

| (p, s) | N | 1.2+i | 0.5+0.8i | −1+0.5i | −1.5 | 2.5i | 4.5+1.5i | 3−1.2i | 15+8i | −6−3i | −0.4+0.3i | −0.3−0.05i |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| (0.75, 2) | 10 | 0.391 | 0.291 | 0.190 | 0.283 | 0.160 | 0.161 | 0.293 | 0.032 | 0.060 | 0.267 | 0.332 |
| (0.75, 2) | 20 | 0.395 | 0.294 | 0.196 | 0.280 | 0.165 | 0.169 | 0.309 | 0.034 | 0.063 | 0.276 | 0.346 |
| (0.75, 2) | 40 | 0.397 | 0.295 | 0.199 | 0.278 | 0.168 | 0.173 | 0.317 | 0.034 | 0.064 | 0.281 | 0.353 |
| (0.6, 2.5) | 10 | 0.677 | 0.700 | 0.575 | 0.734 | 0.309 | 0.230 | 0.380 | 0.054 | 0.119 | 1.148 | 1.815 |
| (0.6, 2.5) | 20 | 0.709 | 0.749 | 0.606 | 0.752 | 0.325 | 0.242 | 0.397 | 0.057 | 0.126 | 1.211 | 1.915 |
| (0.6, 2.5) | 40 | 0.724 | 0.775 | 0.623 | 0.761 | 0.333 | 0.247 | 0.405 | 0.058 | 0.129 | 1.245 | 1.970 |

- N·error is stable, so VN^{−1} − I = O(1/N) in Ω_∞, including near the negative axis close to 0.
- N^p b_N/c = 0.925, 0.962, 0.981 at (0.6, 2.5) and N = 10, 20, 40, consistent with d₁ = −(s − 1)/2 = −0.75.
- N^p b_N/c = 0.952, 0.975, 0.988 at (0.75, 2) and N = 10, 20, 40, consistent with d₁ = −0.5.
- (0.6, 2.5) has α_x = 1.5, so the glued construction is tested beyond |α_x| < 1.

## 6. Open: 0 < p ≤ ½

For p ≤ ½ the continued D_up has **phantom poles**: t = k (k ∈ ℕ) on the sheet arg t = −2π, i.e. on the rays
arg z = ±2πp (and further sheets for p < ¼). At p = ½ these rays are the negative axis.

Design (not yet carried out):
- Between consecutive phantom rays, use alternately D_up and D̃ (D̃ ≈ 1 near the sheet arg t ≈ −2π, where D_up has
  poles).
- Glue along the rays arg t = −π(2m + 1)/2·…, where the ratio (1 − e^{±2πit}) is super-small near 0.
- Close the glue rays at |t| ~ 1 (|z| ~ N^p) by a far-field curve with a Ξ-type scalar, as in Lemma Z.
- In the t-variable the configuration is p-independent except for the number of sheets. So a certified winding
  computation per sheet-count would close it.

The baseline numerics (p = ½, s = 2, 3) already show the law with d₁ = −(s − 1)/2.
