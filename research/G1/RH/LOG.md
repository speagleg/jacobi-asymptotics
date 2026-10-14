# Plan 10 (RH) log

## Phase 0: fine numerics (`checks/check_fine.out`, NUMERICAL)

- **Method.** Atoms beyond K are replaced by an Euler–Maclaurin Gauss–Legendre tail. Without the tail, the fits are
  truncation-dominated: d₁ moves from −1.27 to −0.70 between K and 2K, because about n²/K zeros of P_n lie below
  K^{−p}. With the tail, every case is stable to 4 digits under K-doubling.
- **Exact anchor.** Lommel ν = ½ is exactly σ_{2,2} up to scale, since j_{½,k} = kπ. Its fit gives d = (−0.5, 0.3125)
  and e = (1, 0.625), which the closed forms confirm.
- **Fitted first-order corrections**, for (p, s) ∈ {(2, 2), (2, 3), (2, 4), (2, 6), (3, 3), (3, 4), (3, 6),
  (1.5, 1.5), (1.5, 3)}:

    n^p b_n/c(p) = 1 − (s−1)/(2n) + O(n⁻²),   a_n/(2b_n) = 1 + p/(2n) + O(n⁻²).

  So d₁ = −(s−1)/2 is independent of p, and e₁ = p/2 is independent of s, to 4 digits in all 9 cases. The O(n⁻²)
  coefficients depend on both p and s.
- **Gate 0: GO.** The corrections have the form 1 + c/n + O(n⁻²), with no log terms and no oscillation. The RH analysis
  must reproduce d₁ = −(s−1)/2 and e₁ = p/2. Equivalently, b_n ≈ c(p)(n + (s−1)/(2p))^{−p}.

## Phase 1: interpolation problem → RHP (RH.md §1–3)

- **Option (i), symmetrization, chosen.** WLXZ's origin parametrix is elementary when the accumulation point is
  interior to the band (their (6.24)–(6.28), read).
- **Lemma 1.1, checked to 30 digits** (`checks/check_phase1.out`): θ(±Z_k) = πk; Π′(±Z_k) = (−1)^k; residues cancel;
  the nodes are the only zeros of sin θ off the cut (argument principle 280.000 = 280 for p = 1, 2, 3); the decay
  sectors match WLXZ.
- **Band.** r* = 2^{1+q}√c(p) reproduces WLXZ's (−2, 2) at p = 1, a consistency check of the scaling.
- **Gate 1: GO for p ≥ 1.** For p < 1, θ is real on extra rays, which is deferred. Open for Phase 2: the
  saturated-region sign conventions.

## Phase 2: g-function and signs (RH.md §4)

- **Density.** ψ matches WLXZ (2.1) at p = 1 to 10 digits, and g′ matches WLXZ (4.2) in the right half-plane.
- **Variational conditions.** Equality on the band to 7e−13; strict inequality on the saturated part.
- **Lens signs.** Re φ < 0 over the band, by an exact identity. Re φ̃ < 0 on the saturated part (checked for
  p = 1, 2, 3).
- **Bug found and fixed.** The node-density normalization in the check was off by a factor 2: (1/q)|x|^{−1−1/q}, not
  half of it. The ratio ψ/constraint is now exactly 1 on the saturated part.
- **Gate 2: GO.**
- **Structural finding (RH.md §5).** The origin is regular iff r = 1 + p/2 (α = 0); otherwise there is a Fisher–Hartwig
  |z|^{2α} singularity at 0, which needs a Bessel parametrix. Ruling: Phases 3–5 are done first on the regular family
  r = 1 + p/2, then extended.

## Phase 3: R-jumps, D-functions, global parametrix (RH.md §6)

- **End-to-end check** (actual OPs, N = 24): the poles are removed (|U₁₂| ~ 1/dist; R bounded). The band weight is
  exactly the constant −2πi/p on the regular family (Lemma 3.1).
- **D-functions for p = 2.** The jump identity holds to 1e−26 on the right; normalization |DE| → 1/√(2πN); D̃ − 1 = O(1/N).
  The left side needs mirrored functions (as WLXZ).
- **Scope finding.** The WLXZ D-function construction needs t(z) single-valued in ℂ±. In the symmetric variable that
  holds iff 2/p ∈ ℤ (p = 1, 2). General p needs option (ii) (x-variable, edge parametrix) or a sectorial D.
- **Gate 3: GO for p ∈ {1, 2}**; general p deferred. The new content for p ∈ {1, 2} is the pointwise law for weights
  r ≠ 1 + p/2, which needs the Bessel/Fisher–Hartwig origin parametrix. This covers Haynes–Zudilin a = 2 and
  Monien a = 1.

## Phase 4: local parametrices (RH.md §7)

- **Airy edges.** Square-root vanishing proved, with an explicit constant √(r*² − x²)/(πq r*²) (numerics match for
  p = 1, 2, 3).
- **Origin.** A regular interior point, ψ(0) = 1/(πr*(q+1)). KV §5 (read) is the local problem, with Fisher–Hartwig
  exponent α = (2r − 2 − p)/(2p): structure verified, prefactor bookkeeping pending.
- **Top end.** The saturated jump is exponentially small uniformly up to k_N (raw entry 3e−14 at N = 160), so no
  parametrix is needed.
- **First run of the top-end check (recorded honestly).** Taking the sup over [1.05r*, k_N] grew with N, because the
  sup sat inside the would-be Airy disc and the raw entry carries polynomial N-factors. Restricting to a fixed disc
  complement gives clean exponential decay.
- **Gate 4: GO for p ∈ {1, 2}.** Phase 5 (bookkeeping, small norm, extraction, acceptance test against Phase 0's
  d₁ and e₁) is next.

## Phase 5: assembly and acceptance (RH.md §8)

- **Test A (outer strong asymptotics, p = 2, r = 2 and 3, N up to 240).** No exponential drift; the ratios converge
  at O(1/N); |T₁₁| ∝ 1/N. The g-function and RH structure are confirmed.
- **Test B (extraction).** The leading γ_N² = c(N/2)^{−p} is confirmed. The corrections are (k₀ + k₁(−1)^N)/N with
  k₁ = 0 iff α = 0 (the Bessel/Fisher–Hartwig signature).
- **Lemma 5.1 (unfolding).** e₁ = p/2 for every weight, and d₁ = (p/2 + k₀)/2. This explains Phase 0 exactly.
- **Status.** Theorem RH for p ∈ {1, 2} is a PROOF SKETCH, numerically validated. To reach PROVED it still needs
  symbol-by-symbol jump bookkeeping, explicit small-norm uniformity, and Rule R.
- **Housekeeping.** check_fine.py now has a `__main__` guard, because importing it from check_phase5 re-ran Phase 0.

## Rule R (review/REVIEW_RH.md)

- **Verdict.** ACCEPT WITH FIXES at the PROOF SKETCH level. §6.2–6.3 are REJECTED for p = 2.
- **Withdrawn.** RH_proof.md's PROVED-mod-cite label.
- **Key findings:**
  - the D/E normalization for p = 2 is wrong: D is one-sided and E has a cut on iℝ. Test A's N^{−1} scaling is the
    square of the predicted N^{−1/2}, consistent with a needed two-sided D;
  - the φ̃ sign was wrong;
  - Re φ̃ > 0 on the lens contours is missing;
  - behaviour at 0, the origin perturbation estimate and test B's circularity, plus six more missing steps.
- **Positive.** p = 1 test A matches WLXZ's N^{−1/2} scaling exactly. WLXZ's D works for p = 1 because n/z² is even.

## Option 1: p = 1, r = 3/2 via Tricomi–Carlitz (RH_p1.md)

- **Identification (exact).** σ_{1,3/2} = TC(α = 1) with masses multiplied by √(2π)H(k), where
  H(t) = Γ(t+1)e^t/(√(2π)t^{t+½}) = 1 + 1/(12t) + O(t⁻²).
- **Numerics** (`checks/check_p1_tc.out`). b_n/b_n^{TC} − 1 and a_n/a_n^{TC} − 1 are O(n⁻²): −1.65e−5 at n = 50,
  −2.5e−8 at n = 1500. K-stable to 6e−12.
- **Lemma W1.** The weight perturbation by H_n = H(n/z²) passes through WLXZ's analysis via one extra Szegő
  conjugation D_H. All errors are unchanged: O(1/n) and O(e^{−cn}).
- **Theorem RH₁ (pointwise Law P for σ_{1,3/2}, with O(1/n) rate):** PROVED-mod-cite (WLXZ §§2–6), pending Rule R.
- **Ruling.** The p = 1 full proof is done by perturbing WLXZ's TC analysis rather than re-deriving it. Our nodes are
  TC's with α = 1, and the weights differ by the analytic factor H → 1. This avoids the review's missing steps 2, 3 and
  5 entirely. Cost if wrong: it depends on WLXZ's analysis being correct, which is a published proof that we cite.
- **Rule R on RH₁** (review/REVIEW_RH1.md): ACCEPT WITH FIXES.
  - Fixes applied: D_H dropped (WLXZ run verbatim with weight wH_n); Airy parametrices built from σ's own weight;
    extraction notation and the L¹ bound; WLXZ v1 and DLMF quotes; same-pipeline numerics with exact-TC validation
    (n²·dev → −0.0417, plausibly −1/24).
  - **Rule A pass for W1:**
    - every place the weight enters WLXZ was enumerated (R and V factors, residual weights, local parametrices);
    - degenerate regions checked: the top node (t ≈ 1; H(1) = e/√(2π), bounded); z → 0 (H → 1 in the sectors only,
      and WLXZ's lips approach 0 inside sectors); iℝ (cut, never crossed);
    - risk: D-functions designed around the TC Gamma structure. Resolved: D̃ ≡ 1/H_n, so the residual weight changes
      only by H_n² = 1 + O(z²/n).

## Plan 11 (2026-10-13): RH₁ for general r (p = 1)

- **Numerics** (`checks/check_p1_general_r.out`). Nβ_N − 1 = (k₀ + k₁(−1)^N)/N + O(N⁻²), stable under K-doubling.
  - k₀ = ½ − r (conjecture).
  - k₁ ≈ −3a with a = r − 3/2. The p = 2 fits gave ≈ −4a, suggesting the conjecture k₁ = −(p+2)a.
  - The (−1)^N term is the FH-at-band-centre signature.
- **Proof** (RH_p1_general.md). σ_r = TC(1)·F with F = H_n(z²)^a.
  - Global N_r carries the Szegő function (z/Φ)^a·D_Q.
  - The Airy discs reduce to RH₁ via A = Ng^{σ₃}N^{−1}.
  - The origin gets a KV/Vanlessen Bessel parametrix with h₀ = e^L(4 − z²)Q_m. Q_m is the Stirling truncation of
    H_n² (H_n has poles on iℝ accumulating at 0, so it cannot go into W).
  - Lemma M: the mismatch is structured (diagonal on the band, ∝ J_Ψ − I on the lips) with amplification ≤ ρ^{−2|a|}.
    m ≥ (|a| − 1)/2 makes it O(1/n) uniformly.
- **Checks** (`checks/check_general_r_parametrix.out`):
  - Szegő product to 1e−16;
  - κ_n remainder constants 1/6, 1/180, 1/630, independent of n;
  - Ψ amplification ≈ ρ^{−2|a|} for a ∈ {−0.4, …, 2.5}.
- **Ruling.** The identification step (Lemma O / (Y4)_r) is done at WLXZ's level of rigour, as in RH₁, and is flagged
  for Rule R. Cost if wrong: the label drops to PROVED-mod-(Y4)_r.
- **Rule R** (review/REVIEW_RH1r.md): ACCEPT WITH FIXES, with F1 blocking (§6 identification for |a| ≥ 1/4).
- **Fixes:**
  - **F1.** §6 rewritten:
    - (Y4)_r proved in all sectors (F3, F4);
    - Lemma O1 (un-lensing for a ≥ 0 gives H = O(ℓ²); for a < 0, H = O(|z|^{2a}));
    - Lemma X (a local small-norm solution X̃ of the *inverse* jump, so G = HX̃ is jump-free and no X^{−1} is needed;
      det X̃ is controlled by area means);
    - removability by circle integrals; H₋ ∈ L²; L² uniqueness.
  - **F2.** m := ⌈|a|/2⌉, so δ ≥ 2: δ > 0 for Lemma M and δ > 1/2 for Lemma X.
  - **F5–F9.** Wording, frames, and renaming f → q in §4.
  - **F10.** Numerics caveats; the script docstring notes the −4a "pred" is rejected.
  - **F11.** KV, Vanlessen and DLMF verbatim quotes.
- **Ruling.** Lemma X uses the inverse-jump problem rather than the reviewer's X with X^{−1}. Reason: the circle
  integral of |X^{−1}| = |adj X|/|det X| needs det X control, and the inverse jump avoids that. Cost if wrong: the
  re-check flags it, with no effect on Lemmas S, G, B or M.
- **Re-check: CONFIRMED** subject to R1–R5, which are applied:
  - R1: X̃ → a constant at 0, not I; the near-0 bound corrected;
  - R2: the sub-mean-value argument run on |det X̃ − 1|^{1/2}, since dist^{−1/2} is area-integrable and dist^{−1} is not;
  - R3: midpoint arcs at the tip of G;
  - R4: Vanlessen (4.27)–(4.34) cited for the continuation of Ψ;
  - R5: the Remark range corrected to 1 < r < 9/4.
- **Theorem RH₁(r): PROVED-mod-cite + REVIEWED.**

## Plan 12 (2026-10-13): RH in the x-variable, p > 1 (research/G1/RH/px/)

- **Phase 0.** Reused Plan 10's numerics: d₁ = −(s−1)/2 and e₁ = p/2 for p ∈ {1.5, 2, 3}.
- **Phase 1, Gate 1 GO.**
  - The IP is rescaled with nodes X_k = (N/k)^p and t = N z^{−1/p}. For p > 1, |arg t| < π on the slit plane.
  - Pole removal is checked at a band node and at a saturated node (p = 2, s = 3, N = 12).
  - The band weight is |W| = (2π/p)N^{1+p−s}x^{α_x}, so x = 0 is a hard edge with exponent α_x = (s−1−p)/p.
- **Phase 2, Gate 2 GO.**
  - g, φ = l/2 − g and φ̃ = φ ± iθ/N, with l = 2(log c + p).
  - Strictness on the saturated region comes from Re g′ > 0 there (closes REVIEW_RH Lemma 2.2's fix).
  - Lip signs: ∂_y Re φ = −πψ and ∂_y Re φ̃ = π(ρ − ψ). This gives the REVIEW_RH item-4 condition Re φ̃ > 0 on the
    band lips.
  - Checked for p ∈ {1.5, 2, 3}.
- **Phase 3, Gate 3 GO.**
  - D on the slit plane: D₊/D₋ is unimodular on (−∞, 0), with arg running 0 → π/(2p) − π/2.
  - A scalar S cancels D's (−∞, 0) jump exactly, and S ~ z^{½−1/(2p)}.
  - F = D·S·(4c − z)^{−1/2} → const at ∞. This needs S: D alone has monodromy e^{iπ/p}, which E cannot cancel unless
    1/p ∈ ℤ.
  - The band jump is exact, with weight x^{α_x}(4c − x)h_N.
  - Near the hard edge, D̃S jumps only super-exponentially, so the Binet non-analyticity is absorbed with **no Stirling
    truncation**.
  - Checks: check_px_phase3a.out and check_px_phase3b.out.
- **Phase 4, Gate 4 GO** (`checks/check_px_phase4.out`).
  - **Hard edge.** f := (φ ± iπ)²/4 is analytic at 0, with f′(0) = −0.10132 ≈ −1/π² at p = 2. The KMVV Bessel
    parametrix uses W := (C x^{α_x}(4c − x)h_N)^{1/2}.
  - **Mismatch.** Every mismatch is super-exponentially small (exp(−cN|z|^{−1/p})). It beats the Bessel amplification
    (log₁₀ ≤ −84 at α = 3, N = 20), so **no truncation is needed**.
  - **Soft edge.** φ̃/(z − 4c)^{3/2} → −0.172. WLXZ §6.1 transfers, with E = (4c − z)^{−1/2} playing WLXZ's α = 1 role.
  - **Top end.** Explicit bound: Re φ̃ ≤ −½log x, so the jumps there are N^{−pN}·poly.
- **Phase 5.** Identification via the RH₁(r) §6 route; small norm; extraction in x.
  - Theorem RH_p is claimed: for p > 1, s > 1, n^p b_n = c(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n). Pending Rule R.
- **Rule R** (px/review/REVIEW_RHpx.md): ACCEPT WITH FIXES.
  - End-to-end probe P1 (true OPs vs the global parametrix): error C/N with N·error stable, at three (p, s) pairs.
    This validates Phases 1–3.
  - F1 (blocking): the hard edge is KMVV's *left* endpoint (the old P₀ matching error was 10⁵ → 10¹³).
  - F2: the saturated-region bookkeeping.
  - F3–F10.
- **Fixes applied.** The left-endpoint P₀ matches at O(1/N) in all five sectors (check_px_bessel.out, lens points
  0.029 → 0.014). Lemma 3.4 (the Hölder endpoint bound) is self-contained. Re-check of F1 and F2 dispatched.
- **Re-check: CONFIRMED** subject to R1–R4, which are applied:
  - R1: the θ′ power in the saturated and top entries;
  - R2: the Φ endpoint;
  - R3: the Hölder proof for log h_N;
  - R4: a rename.
- **Theorem RH_p** (every p > 1, s > 1): PROVED-mod-cite + REVIEWED.
- **Deferred minor:** R5, a numerical test of the Ψ phases at α_x ≠ 0.

## Plan 13 (2026-10-13): smooth-ζ model, pointwise (research/G1/RH/zeta/)

- **Phase 0** (check_z_phase0.out):
  - b_n/x_n − π²/16 ≈ −0.226/log n (slow);
  - a_n/(2b_n) − 1 ≈ 0.7/n–0.84/n;
  - stable under J-halving.
- **Edge equation** (check_z_edge.out): ∫_β^∞ √(x/(x − β))ρ_N = 1, from the Abel inversion of G2's arcsine
  superposition.
  - It reproduces 4c(p) for pure powers.
  - For σ_ζ, b_N/(β_N/4) − 1 = O(1/N), with N·dev ≈ −1.1 … −1.4.
  - The 1/log term is entirely the finite-N equilibrium.
- **Canonical edge equation** (constraint only on the monotone branch x ≤ x_e = 1/(4π² + ¼)): b_N = (β_N/4)(1 + 0.27/N)
  (check_z_edge2.out).
- **κ derivation** (regular variation): κ = −2(2J′(2)/J(2) + log J(2)) = −0.2895. The edge equation alone gives a
  log N-coefficient converging slowly (−0.38 → −0.32 for N = 10² … 10¹⁵; the extrapolated a + b/log N fit gives
  ≈ −0.300). Check: check_z_kappa.out.
- **Phase 1 write-up:** RH_zeta.md, Lemma E1, the Abel-inversion generalization of G2 B*.
- **Phase 2 obstruction found.** t(x) is non-monotone beyond x_e (N₀'s minimum at γ = 2π), which puts a spurious
  pole of D at x_s. A fix is proposed: split Ω_∞, plus a far-field scalar Ξ.
- **Phase 2, Gate 2 GO** (check_z_e2e_zeta.out). The end-to-end probe on the true smooth-ζ OPs vs the RH global
  parametrix gives N·error ≈ 0.15–0.36, stable for N = 10, 20, 40. Two corrections were needed:
  - (a) the WLXZ α-shift: the constraint ends at t = 3/8, so α = 5/8 and K = (β̂ − z)^{−1/8};
  - (b) D̃ continued analytically along (−∞, 0) past the t-axis crossing at |γ| = 2πe.
- **Pipeline validation:** MODEL=pp2 reproduces the reviewer's RH_px probe to 4 digits.
- **Rule R** (zeta/review/REVIEW_RHzeta.md): ACCEPT WITH FIXES for Phases 1–2.
  - The headline is confirmed by the absolute test with Ξ explicit (N·err 0.07–0.34, stable for N = 10, 20, 40).
  - The α-shift, E1, E2, E3 and the extraction are verified.
  - F1 (major, open): the hard edge carries a log weight, so RH_px §4.1 does not transfer verbatim.
  - F2: a probe bug, fixed.
  - F5: t_c is a gauge.
  - F6: the κ closed form is corrected; a fit to 10⁶⁰ agrees to 1e−5.
- **Status:** E1–E3 PROVED(-mod-G2); E4 and E5 NUMERICAL; the §4 theorem is a PROOF SKETCH (conditional on the
  log-weight hard-edge lemma, Lemma Z and uniform Airy).

## 2026-10-14 — Item closed
- Plan 13 merged to master with the labels above; no further plans. Open problems carried forward: the log-weight
  hard-edge lemma (candidate routes: D_w-based local parametrix with a lens-boundary mismatch bound, or
  Conway–Deift SIGMA 2018, unread), a certified Lemma Z, uniform Airy; 0 < p < 1 pure powers.
