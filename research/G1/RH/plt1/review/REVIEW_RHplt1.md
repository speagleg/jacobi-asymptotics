# Rule R review: RH_plt1.md (Plan 15, ½ < p < 1)

Reviewer: independent agent, fresh context (worktree `ja-plan15`, branch `plan-15-p-lt-1`, HEAD 28058bf). Read: AGENTS.md,
VERIFICATION_POLICY.md, the plan, RH_plt1.md, RH_px.md (in full), REVIEW_RHpx.md (targeted), CITATIONS.md (DLMF, DLMF-2),
G2 PROOF.md (range of μ*), both probes. Re-derived Lemma 1.1′ by hand; ran independent scratch computations (mpmath, not
committed) and re-ran `check_plt1_e2e.py 0.75 2 10`.

## Verdict: **ACCEPT WITH FIXES**

The strategy is sound and, I believe, correct: the continued D_up has no poles or zeros in ℂ₊ for p > ½, D_up = 1 + O(1/|t|)
off the positive t-axis, B exists, and a glued W̃ removes the only real obstruction (the non-small (h2) jump of D̃B on
(−δ, 0)). Two statements in the write-up are wrong as written, though. The proof of Lemma 1.1′(ii) has a branch sign error
and a compensating arithmetic error (F1). The lens sector |arg z| < πp/2 does not contain the KMVV lips for p ≤ 2/3,
including the tested p = 0.6 (F2). Both have short fixes that don't change the theorem. The claim that "everything else is
RH_px verbatim" needs an explicit amendment list (F5), and one stated consequence is false: B/B(1) = 1 + O(N^{−p}), not
O(1/N). It is unused for the rate (F3).

## Findings

### F1 (major: proof text wrong, conclusion right). Lemma 1.1′(ii), the branch of log(1 − t) and the exponent arithmetic
- **Location:** §1, proof of (ii), bullets 2–3.
- **The branch is wrong.** The text says log(1 − t) = log t − iπ + log(1 − 1/t), "because −t = te^{−iπ} has arg ∈
  (−π/p + π, π)". But te^{−iπ} has argument arg t − π ∈ [−π/p − π, −η − π], outside (−π, π). The range quoted,
  (π − π/p, π), is that of te^{+iπ}.
- **Principal Ln is required.** DLMF 5.11.1 is stated for the principal Ln Γ(z) and ln z. So with z = 1 − t you need the
  principal Ln(1 − t) = log t **+ iπ** + Ln(1 − 1/t), where log t is the continuous log N − (1/p)Log z.
- **Checked numerically:** at arg t = −π/2 and at arg t = −3π/2 (continuous), the principal Ln(1 − t) equals the +iπ
  formula to 60 digits. The −iπ formula is off by 2πi.
- **The branch matters.** A 2πik shift in log(1 − t) multiplies the exponent's (½ − t)·2πik, which is not in 2πiℤ for
  non-integer t.
- **The arithmetic is also wrong.** iπt + (½ − t)(−iπ) = 2πit − iπ/2, not iπ/2. With the correct +iπ,
  iπt + (½ − t)(iπ) = iπ/2, and the exponent is iπ/2 − log i + O(1/t) = O(1/t). So the conclusion holds.
- **Independent check:** |t|·|D_up − 1| → 1/12 (i.e. D_up = 1 − 1/(12t) + …) for |t| = 10…10⁴ on rays arg t ∈
  {−π/p + 10⁻⁹, −0.9π/p, −3π/2, −π, −π/2, −0.3, −0.05}, for p ∈ {0.55, 0.6, 0.75, 0.95}. The identity
  D_up = D̃/(1 − e^{−2πit}) holds to 10⁻⁶⁰.
- **Fix:** replace "−iπ" with "+iπ" and "te^{−iπ}" with "te^{iπ}". Write the step as
  iπt + (½ − t)(iπ) = iπ/2. Also state that the n = 1 remainder is ≤ sec²(½ph(1 − t))·|B₂|/(2|1 − t|), with
  |ph(1 − t)| ≤ π − min(η, 2π − π/p) + o(1). For |t| in a compact range ≥ 1, use boundedness: the distance to t = 1 is
  ≥ sin η.

### F2 (major: false as written for ½ < p ≤ 2/3; easy fix). Lens sector |arg z| < πp/2 versus the KMVV lip angle π/3
- **Location:** §2 ("All lens lips and Σ^△ contours lie in |arg z| < πp/2 … There arg t ∈ (−½π, 0)") and §3 (S_lens,
  the glue rays at ±πp/2, "lips inside S_lens").
- **The problem.** RH_px Lemma 4.1/4.3 (kept verbatim) has f conformal at 0 with f′(0) < 0. The lips are f⁻¹ of the KMVV
  rays arg ζ = ±2π/3, so they leave 0 at arg z = ±π/3 exactly. REVIEW_RHpx line 78 says the same. This is not a free
  parameter of the construction.
- **For p ≤ 2/3,** πp/2 ≤ π/3. So the lips leave S_lens, the glue rays lie inside the lens, and "the lip jumps are
  reproduced exactly" fails. This includes p = 0.6, one of the two e2e test cases; the probe does not see it (F9).
- **Nothing in the proof needs πp/2.** D̃ is zero-free and Stirling-valid (DLMF 5.11.1 for Γ(t)) on |arg t| ≤ π − δ, i.e.
  |arg z| ≤ p(π − δ). The super-smallness of e^{∓2πit}, e^{−2Nφ̃} and the glue jump needs only 0 < |arg z| < πp.
- **Fix:** take S_lens := {|arg z| < θ*} with θ* ∈ (π/3, πp), e.g. θ* = (π/3 + πp)/2. This is non-empty for p > 1/3.
  - On S_lens, |arg t| ≤ θ*/p < π, so D̃ = 1 + O(1/|t|).
  - The lips (arg z = ±π/3) and the band lens near 0 lie inside S_lens.
  - The glue jump is |e^{∓2πit}| = exp(−2π sin(θ*/p)·N|z|^{−1/p}), with sin(θ*/p) > 0. In Lemma 4.3 the lip constant is
    c = 2π sin(π/(3p)) > 0.
  - The outer sector is arg t ∈ [−π/p, −θ*/p], so Lemma 1.1′(ii) applies with η = θ*/p.
  - Replace "arg t ∈ (−½π, 0)" with "|arg t| < θ*/p < π". (Changing the Bessel ray angles would also work, but it needs a
    new citation.)

### F3 (minor; the false statement is unused for the rate). "B/B(1) = 1 + O(1/N) on compacts" (§1 Consequences)
- **Why it fails for p < 1.** |ℓ̂(y)| ≍ |y|^{1/p}/N for |y| ≲ N^p, and it is O(1) beyond. Against the kernel
  ~(1 + |y|)^{−2} this gives ∫_1^{N^p} y^{1/p−2}dy/N + ∫_{N^p}^∞ y^{−2}dy ≍ N^{−p}, because 1/p − 2 > −1 for p > ½.
- **Numerically:** log(B(2)/B(1)) = −3.1e−2, −1.6e−2, −7.4e−3, −3.4e−3 at N = 10, 40, 160, 640 for p = 0.6. The local
  slopes 0.50, 0.54, 0.56 tend to p. At p = 0.75 the slopes are 0.59–0.68. At p = 2 the slope is 1.000, as in RH_px.
- **Why the rate survives.** The global parametrix uses the exact w₀ (Szegő function), the extraction uses only N₀
  (invariance lemma), and Ẽ_N only needs N-uniform bounds. Those hold: ℓ̂ is a fixed bounded function of |t| with
  |ℓ̂| ≤ C|y|^{1/p}/N, so the Hölder constants of log B are N-uniform.
- **Consistent with the probe:** N·err shows no N^{1−p} drift.
- **Fix:** state B/B(1) = 1 + O(N^{−p}). Add "only N-uniform boundedness and Hölder bounds of B, h_N are used". Amend
  RH_px's "h_N/h_N(1) = 1 + O(1/N)" accordingly for p < 1.

### F4 (minor). ℓ̂(−∞) as a continuous determination (winding)
- **Location:** Lemma 1.1′(iii). The small-t argument gives ℓ̂(−∞) only mod 2π, but B's exponent at ∞ and the monodromy
  count (Lemma 3.3(iii)) need the continuous value π/p − π.
- **Key observation:** ℓ̂ is a function of |t| alone along arg t = −π/p, so it is **N-independent** in that variable, and
  one computation per p suffices.
- **Reviewer check (NUMERICAL):** the continuous 2arg D₊ along the whole ray ends at π/p − π exactly. Its range is
  [−0.56, 2.90] at p = 0.52, [−0.01, 2.57] at p = 0.55, [0, 2.09] at p = 0.6, [0, 1.05] at p = 0.75 and [0, 0.35] at
  p = 0.9, so there is no wrap. (The probe's principal `2*arg` is therefore safe.) The probe's F_∞ agrees in two
  directions to 10⁻⁸, which is consistent.
- **Fix:** add the sentence. Either cite a committed check, or prove |arg D₊| < π on the ray: Stirling for |t| ≥ T₀,
  small-t expansion for |t| ≤ t₀, and an Arb winding on the compact middle, as in Lemma Z. Flag it as NUMERICAL if it is
  not certified.

### F5 (minor; needed for "verbatim" to be literally true). The places where RH_px uses p > 1
Each item gives the place in RH_px, then the status for ½ < p < 1.
- **§1 "In ℂ₊, Im θ < 0":** false for πp < arg z < π. It is used only in the band lens and Ω^△ (arg z small) and in
  (Y4)_x, so it is fine but needs restating as "for 0 < arg z < πp".
- **Lemma 1.1, Lemma 3.1(i) (D̃ analytic and nonvanishing on the slit plane):** false. It is replaced by 1.1′, with D̃
  restricted to S_lens (F2).
- **Lemma 3.1(iii) (ℓ̂ asymptotics, "Binet"):** replaced by 1.1′(iii). OK, with F4.
- **Lemma 3.2(ii) (ν = min(1/p, ½)):** ν = ½; ℓ̂ is Lipschitz. OK.
- **Lemma 3.2(iii):** OK, given F4.
- **Lemma 3.2(iv):** false; it is O(N^{−p}) (F3).
- **Lemma 3.2(v):** fails, since sin(π/p) < 0. It is obsolete under the glue; say so.
- **Lemma 3.3(iii) monodromy:** OK, given F4.
- **Lemma 3.4 consequence (log h_N Hölder on the band):** OK; (log D̃)′ = O(x^{1/p−1}/N) is now bounded.
- **Lemma 3.5 "g − log z ≍ z^{−1/p}", "T = I + O(N|z|^{−1/p})":** for p < 1, μ* has a finite first moment, so it is
  ≍ 1/z. This is cosmetic, because the argument only needs κ to be bounded and jump-free in |z| > N^p + δ′, which holds.
- **Lemma 4.1:** p-free, since μ* is G2's for all p > 0 and the hard-edge density is x^{−1/2}·(analytic, |x| < 4c). OK.
- **Lemma 4.2(iii):** the (h2) jump on (−δ, 0) disappears (DB is continuous there). It is replaced by the glue-ray jumps
  (§3). Say so.
- **Lemma 4.3:** the lip constant is sin(π/(3p)) > 0 (p > 1/3). The (h2) item is replaced by the glue item. With F2: OK.
- **§4.2 Airy, §4.3 top end:** t is near the positive axis, so p-free. OK.
- **§5 (Y4)_x:** the sum bound is p-free. The lens-sector argument needs Im θ < 0 in the **whole upper-right quadrant**,
  i.e. π/2 < πp, i.e. **p > ½**: a second, independent use of p > ½ that the write-up should name. The δ₀ ≤ |arg z| < π/3
  overlap needs π/3 < πp. OK.
- **Identification, small norm, extraction:** p-free. OK.
- **Fix:** add a short amendments table to RH_plt1 §0 with the items above. The present claim, "the only p > 1 input of
  RH_px is Lemma 1.1", is not literally true.

### F6 (minor). §3: the square-root bound in the outer sector is not spelled out
- **Location:** §3. For removability, E^a = O(|z|^{−1/2}) needs D_w/W̃ bounded above and below near 0 **in every sector**.
  In the outer sector W̃ uses DB, not h_N.
- **Supply:**
  - D_w/((−z)^{α_x/2}(4c − z)^{1/2}) → h_N(0)^{1/2}·exp(bounded) by Lemma 3.4;
  - h_N(0) = const/B(0)², since D̃(0⁺) = 1;
  - in the outer sector D → 1 uniformly by 1.1′(ii) with η = θ*/p, and B → B(0) from each side by Lemma 3.2(ii);
  - so D_w/W̃ is bounded above and below.
- The rest of the transfer is correct (checked; see below).
- **Fix:** add these three lines, and note that (−z)^{α_x} is analytic across (−δ, 0).

### F7 (minor). Citation gate
- DLMF 5.5.3 **is** quoted in this worktree (CITATIONS.md, entry DLMF-2, line 275). DLMF 5.11.1 and its sec^{2n} remainder
  are quoted in the DLMF entry (lines 85–92).
- **Fix:**
  - add RH_plt1 (Lemma 1.1′) to the "Used in" lines of DLMF-2 and DLMF;
  - in Lemma 1.1′ cite "DLMF 5.11.1 + §5.11(ii) (n = 1)" applied to z = 1 − t with principal ln (F1);
  - also cite DLMF 5.11.1 for Γ(t) on S_lens (F2).
- No other new external input is used.

### F8 (minor, Rule N). Baseline probe `check_plt1_phase0`
- **No precision doubling.** It uses `prec='ld'` only, while Rule N's NUMERICAL label requires it.
- **Mismatched stability claim.** The quoted n = 400 values sit where the K-stability is 3.0e−5 (p = ½, s = 2) and 2.4e−5
  (p = ½, s = 3). The text claims stability ≤ 10⁻¹⁰ only "for n ≤ 200". The resulting uncertainty in n·dev at n = 400 is
  ≈ 0.01, the same size as the gaps −0.504 vs −0.5 and −1.007 vs −1.
- **Fix:** quote n = 200 (−0.5052, −1.0118, −0.4997) or add a dps run. This is the baseline only and affects no proof step.

### F9 (minor). Scope of the e2e probe
- **What it tests.** `check_plt1_e2e.py` tests V vs the outer parametrix N at Ω_∞ points only. It validates D's
  continuation beyond arg z = πp, B (including F4 implicitly), l, w₀/D_w and C_∞. It tests **none** of §2–§3: lens
  geometry, glued W̃, P₀, the glue-ray mismatch, Bessel matching on ∂U(0, δ).
- **Re-run.** `check_plt1_e2e.py 0.75 2 10` reproduced the committed N = 10 row (see "Re-run" below).
- **Masking risk is low.**
  - D_up is evaluated from the exact identity (exp makes the loggamma branch irrelevant). The guard digits ≈ 2log₁₀|t| + 10
    cover the |t|log|t| cancellation, and L is recomputed inside `workdps`.
  - The Binet tail for real t > 10³ has remainder < 1/(1680t⁷) < 10⁻²⁴ (correct coefficients).
  - It is not certified, and no dps-doubling is reported.
- **Fix (recommended, not blocking):** port `check_px_bessel.py` [B] (P₀N^{−1} − I on ∂U(0, δ), five KMVV sectors,
  N = 20 → 40) and `check_px_phase4.py` [3] (mismatch × amplification on the lip ray arg z = π/3 and on the glue ray
  arg z = θ*) to p = 0.6 with the glued W̃. State in §5 that the e2e gate covers Ω_∞ only.

### F10 (cosmetic)
- §6: "D̃ ≈ 1 near the sheet arg t ≈ −2π" is false for the *continued* t^{t−½}. There D̃_cont = −e^{−2πit}·D̃_principal.
  What is ≈ 1 is D̃ with the principal log t, i.e. a re-definition per sheet. Say so in the design note.
- §3: "W̃ jumps by (D/D̃)^{∓1}". The sign of the exponent depends on orientation; write W̃_out/W̃_in = D̃/D = 1 − e^{∓2πit}.
- Lemma 1.1′(ii): the bound "uniformly on |t| ≥ 1" has constants that blow up as p → ½⁺ (margin 2π − π/p). Fine for
  fixed p; say so.

## Checked and OK
1. **Identity of Lemma 1.1′.** 1/Γ(t) = Γ(1 − t)sin(πt)/π (DLMF 5.5.3) and sin(πt)/(1 − e^{−2πit}) = e^{iπt}/(2i) give
   D_up = t^{t−½}e^{−t}e^{iπt}Γ(1 − t)/(i√(2π)). Re-derived by hand, and checked to 10⁻⁶⁰ at five points including
   arg t = −5.5 and near −π/p.
2. **(i) Pole- and zero-freeness in ℂ₊ for ½ < p < 1.**
   - Γ(1 − t) has no zeros and has poles only at t ∈ {1, 2, …}.
   - arg t ∈ (−π/p, 0) ⊂ (−2π, 0) excludes the positive reals in the open half-plane.
   - On the negative axis arg t = −π/p ≠ 0, −2π, so D_up is regular and nonzero there. The nodes are the only
     singularities.
3. **(ii)** holds with the corrected branch (F1). Its restriction to arg t ≤ −η is all that is needed, because near
   arg t = 0 (the band, Ω^△ and their lips, outside U(0, δ)) one uses D = D̃/(1 − e^{−2πit}) with D̃'s own Stirling and
   |e^{−2πit}| = e^{2π Im t} small.
4. **(iii)**
   - ℓ̂(0⁻) = O(|x|^{1/p}/N): observed ~6e−20 at |x| = e^{−30}, p = 0.75, N = 10.
   - ℓ̂(−∞) = π/p − π: verified continuously, no winding (F4).
   - D₋ = conj D₊ on the negative axis.
5. **(iv), and F's exponents at ∞.** D ~ z^{1/(2p)}, B ~ z^{½−1/(2p)} and K ~ z^{−½} sum to 0. κ is analytic at ∞
   (Lemma 3.5's argument is p-free).
6. **Glue-ray jump (§3).** On arg z = ±θ, arg t = ∓θ/p and |e^{∓2πit}| = exp(−2π sin(θ/p)N|z|^{−1/p}). At θ = πp/2 this is
   exp(−2πN|z|^{−1/p}) as stated (with F2's θ*, the constant is sin(θ*/p)).
   - The jump of P₀ (both Ẽ_N and the right factor W̃^{−σ₃}) is I + O(ε·e^{CN|z|^{1/2}}·poly). This is super-small
     against ε = e^{−cN|z|^{−1/p}}.
   - The E^a + Φ split transfers verbatim: the density is O(|y|^{−1/2}e^{−cN|y|^{−1/p}}), and the endpoint singularities
     at δ₀e^{±iθ*} lie off ∂U(0, δ).
7. **W̃₊W̃₋ = w₀ on the band.**
   - The band lies in S_lens, so W̃ there is the RH_px W̃.
   - The principal (−z)^{α_x} phases cancel.
   - D̃B is continuous across (0, δ).
   - Outer W̃ is analytic: DB has no jump on (−∞, 0) by Lemma 3.2(i), and is zero-free.
8. **Large α_x (s ≥ 1 + 2p).** Nothing α-specific is introduced. KMVV covers α > −1, and the removability bound uses
   D_w/W̃ bounded, independent of α. The (Y4)_x/O1 parts are RH_px's.
9. **Lemma 4.3 lip bounds for p < 1.**
   - D/D̃ − 1 and e^{−2Nφ̃} are ≤ exp(−2π sin(π/(3p))N|z|^{−1/p}).
   - Re φ̃ ≈ π sin(π/(3p))|z|^{−1/p} > 0 on the lip near 0.
   - Positive for p > 1/3.
10. **μ*, Lemmas 2.1, 2.2 and 4.1 (f analytic, f′(0) < 0, Re φ < 0 off the band).** G2 B* is proved for every p > 0
    (PROOF.md line 1, B* row). The hard-edge density is x^{−1/2}·(1/π)∫₀¹(4cτ^{−p} − x)^{−1/2}dτ, analytic for |x| < 4c.
11. **§6 phantom poles.**
    - For p < ½, π/p > 2π, so the sheet arg t = −2π (arg z = ±2πp) enters ℂ±, and Γ(1 − t) has poles at t = k there.
    - For p = ½, these are the boundary values on the negative axis (arg z = π), at x = −(N/k)².
    - Further sheets arg t = −4π, … enter for p < ¼.
    - Characterization correct.
12. **Probe numerics.**
    - Committed outputs: N·err is stable at all 11 points for N = 10, 20, 40, at both parameter pairs.
    - The near-0 negative-axis points drift by +0.06 and then +0.03, so the increments halve: an O(1/N²) correction, and
      no N^{1−p} drift.
    - N^p b_N/c matches 1 + d₁/N with d₁ = −(s − 1)/2.
    - det V = 1 to 10⁻³¹.
13. **Rule C.** DLMF 5.5.3 is present here (DLMF-2). DLMF 5.11.1 and the §5.11(ii) remainder are quoted with the sector
    hypothesis, and that hypothesis holds: |ph(1 − t)| ≤ π − min(η, 2π − π/p) for large |t|.

## Re-run
`check_plt1_e2e.py 0.75 2 10` (reviewer, this worktree): reproduced the committed N = 10 block of `check_plt1_e2e_p075s2.out` digit for digit (all 11 points, F_inf, D_inf, N^p b_N/c = 0.9522058151), runtime 48 s.

## Recommended label
After F1–F2 (required) and F3–F7 (text), the label is:

**Theorem RH_p, ½ < p < 1: PROVED-mod-cite (RH_px's cites: WLXZ v1 §§3–5, §6.1; KMVV §6 incl. (6.42)–(6.53); G2 μ*/B*;
plus DLMF 5.5.3, 5.11.1/§5.11(ii)), REVIEWED.**

- F4: the ℓ̂ no-winding statement is NUMERICAL unless proved or certified. Either prove it or record it as a named
  NUMERICAL input. Until then: "PROVED-mod-cite, modulo the NUMERICAL no-winding fact F4".
- Novelty: UNCHECKED.
- F8–F9 are recommended, not blocking.
- 0 < p ≤ ½ stays OPEN, as stated.
