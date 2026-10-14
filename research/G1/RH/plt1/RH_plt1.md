# RH_plt1: pointwise Law P for σ_{p,s}, ½ < p < 1 (Plan 15)

Status: **REVIEWED** (Rule R: ACCEPT WITH FIXES, review/REVIEW_RHplt1.md; F1–F10 applied and re-checked). It
covers ½ < p < 1 and every s > 1, modulo the NUMERICAL no-winding fact of Lemma 1.1′(iii) (F4). The range 0 < p ≤ ½
is open (§6).

Everything not stated here is RH_px.md verbatim (Plan 12, REVIEWED): transformations, μ*, Lemmas 1.2, 2.1, 2.2, 3.3,
3.5, the Airy parametrix, the top end, and the small-norm extraction. The hard edge is RH_px §4.1 with a glued W̃
(§3).

**Amendments to RH_px for ½ < p < 1** (Rule R F5). Each entry gives the place in RH_px, then the change.
- **§1, "in ℂ₊, Im θ < 0":** holds for 0 < arg z < πp. It is used only in the band lens and Ω^△ (arg z small) and in
  (Y4)_x.
- **Lemma 1.1 and Lemma 3.1(i) (D̃ on the slit plane):** replaced by Lemma 1.1′. D̃ is used only on
  S_lens = {|arg z| < θ*} (§2).
- **Lemma 3.1(iii):** replaced by Lemma 1.1′(iii).
- **Lemma 3.2(ii):** ν = ½; ℓ̂ is Lipschitz at 0⁻.
- **Lemma 3.2(iii):** holds, given 1.1′(iii).
- **Lemma 3.2(iv):** becomes B/B(1) = 1 + O(N^{−p}) (F3). Only N-uniform bounds and Hölder bounds of B and h_N are used
  (global parametrix with the exact w₀; extraction via N₀). Correspondingly, h_N/h_N(1) = 1 + O(N^{−p}).
- **Lemma 3.2(v):** obsolete; it is replaced by the glue-ray jumps (§3).
- **Lemma 3.3(iii) (monodromy):** holds, given 1.1′(iii).
- **Lemma 3.4's consequence:** (log D̃)′ = O(x^{1/p−1}/N) is now bounded. It holds.
- **Lemma 3.5:** for p < 1, μ* has a finite first moment, so g − log z ≍ 1/z. Only "κ bounded and jump-free in
  |z| > N^p + δ′" is used, and that holds.
- **Lemma 4.1:** p-free.
- **Lemma 4.2(iii):** the (h2) jump on (−δ, 0) is absent (DB is continuous there). It is replaced by the glue-ray jumps
  (§3).
- **Lemma 4.3:** the lip constant is c = 2π sin(π/(3p)) > 0, since the lips sit at arg z = ±π/3 and π/(3p) < π. The
  (h2) item is replaced by the glue item.
- **§§4.2–4.3:** p-free.
- **§5 (Y4)_x:** the sum bound is p-free. The lens-sector argument needs Im θ < 0 in the whole upper-right quadrant,
  i.e. π/2 < πp. **This is a second, independent use of p > ½.** The δ₀ ≤ |arg z| < π/3 overlap needs π/3 < πp.
- **Identification, small norm and extraction:** p-free.

## 0. Target and baseline

**Target.** n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n), for ½ < p < 1 and s > 1.

**Baseline** (NUMERICAL, `checks/check_plt1_phase0.out`; exact atoms plus a log-panel Euler–Maclaurin tail; K-stability
≤ 10⁻¹⁰ for n ≤ 200, extended precision only, with no dps-doubling; Rule R F8). At n = 200, n(n^p b_n/c(p) − 1) is:
- −0.4997 (p = ¾, s = 2);
- −0.5052 (p = ½, s = 2);
- −1.0118 (p = ½, s = 3).

This is consistent with d₁ = −(s − 1)/2, as for p > 1 (RH_px §0). `check_plt1_phase0_small.out` shows the same pattern
for p = 0.4, 0.3 and 0.25.

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
- **(ii)** Apply DLMF 5.11.1 together with §5.11(ii) (n = 1) to Γ(1 − t), with the *principal* Ln (Rule R F1).
  - Since arg t ∈ [−π/p, −η], the angle of 1 − t from the negative real axis is at least min(η, 2π − π/p) − o(1) > 0.
  - So the remainder is ≤ sec²(½ph(1 − t))·|B₂|/(2|1 − t|) = O(1/|t|), with a constant that blows up as p → ½⁺ or
    η → 0 (fine for fixed p).
  - On compact |t|-ranges with |t| ≥ 1, the distance to the pole t = 1 is ≥ sin η, so everything is bounded.
  - The principal logarithm is Ln(1 − t) = log t **+ iπ** + Ln(1 − 1/t), because te^{iπ} has
    arg ∈ (π − π/p, π) ⊂ (−π, π). Here log t = log N − (1/p)Log z is the continuous branch.
  - Then the exponent of D_up is
    (t − ½)log t − t + iπt + (½ − t)Ln(1 − t) + (t − 1) + ½log 2π − log(i√(2π)) + O(1/t)
    = iπt + (½ − t)(iπ) − 1 − log i + (½ − t)Ln(1 − 1/t) + O(1/t).
  - Here iπt + (½ − t)iπ = iπ/2 and (½ − t)Ln(1 − 1/t) = 1 + O(1/t). So the exponent is iπ/2 − log i + O(1/t) = O(1/t).
  - *Check:* |t|·|D_up − 1| → 1/12 on rays arg t ∈ [−π/p, −0.05] for p ∈ {0.55, …, 0.95} (Rule R probe).
- **(iii)** Conjugation symmetry gives D₋ = conj D₊ on (−∞, 0).
  - As x → 0⁻, |t| = N|x|^{−1/p} → ∞ with arg t = −π/p ∈ (−2π, −π) fixed, so (ii) gives D₊ = 1 + O(|x|^{1/p}/N).
  - At −∞, small t gives D₊ ~ −it₊^{−1/2}/√(2π) (RH_px Lemma 3.1(iii)). That fixes ℓ̂(−∞) only mod 2π.
  - The continuous value π/p − π (needed for B's exponent and Lemma 3.3's monodromy) holds if arg D₊ does not wind along
    (−∞, 0).
    - On arg z = π one has arg t = −π/p, so D₊ is a function of |t| alone, and this is **N-independent**.
    - **NUMERICAL** (`checks/check_plt1_lhat.out`; Rule R F4): for p = 0.51, 0.52, …, 0.99 (49 values), tracking
      |t| ∈ [10⁻¹², 10¹²] continuously, max|arg D₊| < π, and the end value equals (π/p − π)/2 to 3·10⁻¹¹.
    - Not certified: an Arb certificate on (|t|, p) boxes, as in Lemma Z, would close it.
- **(iv)** As in RH_px. ∎

**Consequences.**
- B (RH_px Lemma 3.2) exists:
  - ℓ̂ is Lipschitz at 0⁻ (1/p > 1), so the ν of Lemma 3.2(ii) is ½;
  - B ~ Cz^{½−1/(2p)} at ∞;
  - B/B(1) = 1 + O(N^{−p}) on compacts (Rule R F3). Only N-uniform boundedness and Hölder bounds are used: ℓ̂ is a
    fixed function of |t| with |ℓ̂| ≤ C|y|^{1/p}/N.
- F := DBK has no jump on (−∞, 0) (Lemma 3.3), and Lemma 3.5 (normalization at ∞) is unchanged.

## 2. Where D̃ itself is used: thin lenses

D̃ (not D) enters:
- F̃ := D̃BK in the band lens and in Ω^△;
- the band weight w₀ = W(4c − x)/(D̃B)².

For p < 1, D̃ has zeros on arg z = ±πp. So:
- **Lens and Ω^△ geometry** (Rule R F2).
  - The KMVV lips are f⁻¹ of the rays arg ζ = ±2π/3. Since f is conformal at 0 with f′(0) < 0, they leave 0 at
    arg z = ±π/3.
  - So put S_lens := {|arg z| < θ*} with θ* := (π/3 + πp)/2 ∈ (π/3, πp). It contains the lips, the band lens near 0
    and Σ^△.
  - On S_lens, |arg t| ≤ θ*/p < π. So D̃ = exp(−μ(t)) = 1 + O(1/|t|) (DLMF 5.11.1 for Γ(t)), and
    |e^{∓2πit}| ≤ exp(−2π sin(|arg t|)|t|) decays away from the axis.
  - The (h1) entries D/D̃ − 1 = O(exp(−c|t|)) are super-small near 0, as in RH_px Lemma 4.3.
  - RH_px Lemma 2.2's signs are local to the axis, so they hold in thin lenses.
- **w₀ only on the band.** w₀ is used on (0, 4c), and in the lens through its continuation into S_lens (no zeros of
  D̃ there). It is **not** continued around 0. §3 glues W̃ instead.

## 3. Hard edge: RH_px §4.1 with a glued W̃

RH_px §4.1 builds W̃ = (C(−z)^{α_x}(4c − z)h_N)^{1/2}, with h_N ∝ (D̃B)^{−2} continued to the punctured disc U(0, δ).
For p < 1, D̃ has zeros on arg z = ±πp accumulating at 0, so h_N cannot be continued that way. **Glue instead.**
- In S_lens = {|arg z| < θ*} (§2; it contains the lips and Σ^△ near 0): W̃ := (C(−z)^{α_x}(4c − z)/(D̃B)²)^{1/2},
  exactly as in RH_px. So the lip jumps are reproduced exactly.
- In U(0, δ) ∖ S̄_lens: W̃ := (C(−z)^{α_x}(4c − z)/(DB)²)^{1/2}. D is analytic and zero-free there (Lemma 1.1′(i); no
  nodes off the positive axis), and DB is continuous across (−∞, 0) (§1). So this W̃ is analytic in that sector, with
  (−z)^{α_x} principal (cut on [0, ∞)).
- On the glue rays arg z = ±θ*, W̃_out/W̃_in = D̃/D = 1 − e^{∓2πit} (Rule R F10).
  - There |e^{∓2πit}| = exp(−2π sin(θ*/p)N|z|^{−1/p}), with sin(θ*/p) > 0. This jump is super-small.
  - It is of exactly the type that RH_px Lemma 4.2(iii) handles for its (h2) jump on (−δ, 0): split Ẽ_N = E^a + Φ,
    where Φ is the Cauchy integral of the super-small jump, with density O(|y|^{−1/2}exp(−cN|y|^{−1/p})), hence
    O(e^{−c′N}). E^a is analytic in the punctured disc with at most a square-root singularity, so it is analytic.
  - The square-root bound needs D_w/W̃ bounded above and below near 0 **in every sector** (Rule R F6):
    - D_w/((−z)^{α_x/2}(4c − z)^{1/2}) → h_N(0)^{1/2}·exp(bounded) by RH_px Lemma 3.4;
    - h_N(0) = const/B(0)², since D̃(0⁺) = 1;
    - in the outer sector, D → 1 uniformly (Lemma 1.1′(ii) with η = θ*/p), and B → B(0) from each side (Lemma 3.2(ii));
    - (−z)^{α_x} is analytic across (−δ, 0).
  - In the error matrix the glue jumps are O(N^{−K}min(1, |z|^K)) after the polynomial amplification by P₀, as in
    RH_px Lemma 4.3.
- With this W̃, RH_px Lemmas 4.1–4.3 hold verbatim:
  - f is the same conformal map, since φ depends only on μ*;
  - the Bessel order is α_x = (s − 1 − p)/p > −1;
  - KMVV's left-endpoint construction (6.42)–(6.53) and the matching P₀N^{−1} = I + O(1/N) are unchanged.
- No comparison argument is needed: there is no log factor, and every mismatch is super-small. (The comparison method
  of RH_zeta_close.md §1 would also work for |α_x| < 1, but this route covers all s > 1.)

## 4. Assembly

**Theorem RH_p (½ < p < 1; PROVED-mod-cite (WLXZ, KMVV §6, G2 μ*/B*, DLMF 5.5.3, 5.11), modulo the NUMERICAL no-winding
fact of 1.1′(iii); REVIEWED).** For ½ < p < 1 and s > 1,

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
- **Scope** (Rule R F9). This gate tests Ω_∞ only: D's continuation, B, l, w₀/D_w and C_∞. It does **not** test §§2–3
  (lens geometry, glued W̃, P₀, Bessel matching). Porting `check_px_bessel.py` [B] and `check_px_phase4.py` [3] to
  p = 0.6 with θ* is recommended.

## 6. Open: 0 < p ≤ ½

For p ≤ ½ the continued D_up has **phantom poles**: t = k (k ∈ ℕ) on the sheet arg t = −2π, i.e. on the rays
arg z = ±2πp (and further sheets for p < ¼). At p = ½ these rays are the negative axis.

Design (not yet carried out):
- Beyond arg t = −2π the continued D_up is exponentially small or large, so B fails on the negative axis.
  - D̃ with the *continued* t^{t−½} is not ≈ 1 there: D̃_cont = −e^{−2πit}D̃_principal (Rule R F10).
- **Seam construction (Plan 15b, being tested; `checks/check_plt1_seam_e2e.py`).**
  - Use D only in an inner sector |arg z| < θ_s < πp, with F = D·B_in·K and B_in := (1 + z)^{½−1/(2p)}.
  - In the outer sector put F = B_out·K, with B_out := (1 − z/(2πN))^{1/2}.
  - X is the Cauchy integral over the two seam rays of log(D·B_in/B_out). Its density decays at both ends: O(|z|^{min(1,1/p)})
    at 0 and O(|z|^{−1/p}log|z|) at ∞. With F := (…)e^X, F is continuous across the seams.
  - No B is needed, and there are no phantom poles. The outer power ½ makes the seam phases match exactly.
  - Open points: the lip angle versus θ_s for p ≤ ⅓ (KMVV: the angle 2π/3 "could be replaced by any angle in (0, π)"),
    and the (Y4)_x lens-sector argument for p ≤ ½.

The baseline numerics (p = ½, s = 2, 3) already show the law with d₁ = −(s − 1)/2.
