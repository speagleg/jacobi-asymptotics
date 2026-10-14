# REVIEW_RHzeta_close: Rule R second reading of RH_zeta_close.md (Plan 14), 2026-10-14

- **Reviewer.** An independent second-reader agent (opus, fresh context). No repo file was edited except this one, and
  nothing was committed. HEAD at review time: 8c79d5d (Plan 14 commits 379e0c5 … 72d40d1).
- **Read:**
  - RH_zeta_close.md in full; RH_zeta.md; review/REVIEW_RHzeta.md (F1 and the probes); RH_px.md §§1–6;
  - CITATIONS.md; the Plan 14 file;
  - checks/check_z_Zcert.py, check_z_cmp.py, check_z_lw1.py and their .out files; check_z_kappa.out;
  - **primary sources** (fresh downloads in scratch dirs, pdftotext): Conway–Deift arXiv 1711.01590v4 §4 (Thm 4.4,
    Thm 4.5 statement, Prop 4.6, Thm 4.7, Prop 4.9, (4.14)–(4.15)); KMVV arXiv math/0111252v2 §6 ((6.16)–(6.28)).
- **Re-runs:**
  - `check_z_Zcert.py` reproduces `check_z_Zcert.out` byte for byte (3.5 s);
  - `check_z_lw1.py` reproduces `check_z_lw1.out` byte for byte.
  - check_z_cmp.py was not re-run (J = 8·10⁵; its .out is internally consistent: J = 4·10⁵ and 8·10⁵ agree to all digits).
- **Own probes** (scratchpad `rr14/`):
  - `cpm.py`: the x^{−1/2} factor of LW1. With the same Szegő representation as check_z_lw1, on [0, π²/4] and at
    z = re^{iθ}, the ratio D_q(z)²/z^{−1/2} for q = x^{−1/2} is:
    - +i(1 + 0.031), +i(1 + 0.0032), +i(1 + 0.0003), +i(1 + 0.00003) at θ = π/3 and r = 10⁻², 10⁻⁴, 10⁻⁶, 10⁻⁸;
    - the complex conjugate (→ −i) at θ = −π/3;
    - → +i at θ = 2π/3.
  - So D_q²/q → c_± = ±i with an O(|z|^{1/2}) error. This independently confirms the constant in H1(ii) and LW1, and its
    consistency with KMVV (6.45) (W̃² = e^{−βπi}w in ℂ₊, with β = −½).
  - A hand re-derivation of every algebraic identity in §§1–4, listed under "Checked and OK" below.

## Verdict: **ACCEPT WITH FIXES**

The three closure items are correct in substance, and I found no error that invalidates the main theorem.

- **§1 (hard edge, comparison with W̃ := D_w).** The comparison problem has exactly the right structure.
  - The prefactor Ẽ_N = D_∞^{σ₃}N₀Mf^{σ₃/4}(2πN)^{σ₃/2} is *weight-independent*. So Q̃ = A₀(2πN)^{σ₃/2}Φ(N²f), where:
    - D_w cancels exactly;
    - A₀ is analytic and bounded with bounded inverse;
    - Φ is N-free.
  - The only mismatch is the lip entry δ = (D_w²/w₀ − c_±)e^{2Nφ}, of size O(1/log N).
  - Every size estimate in Lemma UR, Theorem C and Proposition D re-derives with the claimed powers of N:
    - the K-term: N^{σ₃/2}ζ^{−σ₃/4} = f^{−σ₃/4}, so it is N-free for |ζ| ≥ 2;
    - the small-ζ Hilbert–Schmidt norms: O(N^{−2}) and O(N^{−1});
    - the cancellation of e^{2Nφ} against e^{Nφσ₃}, which leaves e^{−4ζ^{1/2}};
    - the inner-region bound N|ζ|^{−1/2};
    - the correction term: O(1/(N log²N)).
- **Lemma UR** is the Deift–Zhou "explicit solution" argument with A₂ power weights |ζ|^{±1/4}. The argument is valid.
  But several technical steps are asserted rather than proved (F1). They are routine, and they must be written before
  the PROVED label.
- **§2 (Lemma Z).** The jump bookkeeping is exact, and I re-derived it sign by sign. The maximum-principle argument is
  correct. The Arb certificate is sound (F7(c) has details: ball coverage, the determination switch, the tail).
- **§§3–4** are correct; F5 asks for a few lines on the non-compact ρ-range.
- **Rule C** has a few gaps (F2): the explicit local form of the order-−½ Bessel matrix, Hurwitz, and Mellin/PV facts.

**Labels after the fixes:**
- §2: PROVED, with a CERTIFIED winding computation.
- §§1, 3, 4: PROVED-mod-cite.
- Theorem RH_ζ: **PROVED-mod-cite** (WLXZ v1 §§3–6.1; KMVV §6; C–D Thm 4.4; DLMF 5.11 and 10.x; G2), and REVIEWED
  once F1–F5 are applied and re-checked.
- Until then, the status "PROOF complete, pending Rule R" is accurate.

## Findings

### F1 (minor; a write-up gap that must be closed before PROVED): Lemma UR, technical steps asserted

The architecture is right:
- the explicit solution m = C(gQ̃₊^{−1})Q̃;
- the factorization Q̃ = A₀N^{σ₃/2}Φ;
- the commutator split A₀^{−1}(s)A₀(z) = I + (s − z)K;
- Lemma W with a = ±¼ for the core.

I re-derived all the N-power bookkeeping and it holds. The following points are not justified as written.

- **(a) Removability in the uniqueness step** (§1.4(a)).
  - *Problem.* The bound |m| = O(|z − z₀|^{−1/2}) holds only in closed sectors away from Σ. An analytic function with
    an |z|^{−3/4} bound in sectors only is not automatically removable.
  - *Fix.* Use the area estimate. Since m = C(h) with h ∈ L²(Σ), ‖m‖_{L²(dA, |z−z₀|<ε)} ≤ Cε^{1/2}‖h‖ (Poisson/Cauchy
    extension on each ray). Together with |Q̃^{−1}| ≲ |z|^{−1/4}, this gives ∬_{ε<|z|<2ε}|mQ̃^{−1}|dA = O(ε^{5/4}). So
    every negative Laurent coefficient is O(ε^{1/4}) → 0.
  - Equivalently, cite the E²-class argument of RH_px §5 ("removability by circle integrals") and check its
    hypotheses here.
- **(b) m ∈ ∂C(L²)** (§1.4(b)).
  - *Problem.* gQ̃₊^{−1} ∉ L² in general (the doc itself notes it is only in L¹_loc). So "m₊ − m₋ṽ = g" does not yet
    show that m is the Cauchy integral of its jump, which is what (a) and Prop. 4.6's direction require.
  - *Fix.* Two lines:
    - (c)–(e) give m± ∈ L²;
    - m − C(m₊ − m₋) has no jump, is O(1/z) at ∞, and has at most |z|^{−3/4} local singularities, which are
      removable as in (a). Hence m = C(m₊ − m₋).
- **(c) Domain of the factorization** (§1.4(c)–(d)).
  - *Problem.* The partition uses U(0, 2δ), but A₀ = 𝒵̃′N₀Mf^{σ₃/4} is analytic only in U(0, δ): 𝒵̃ jumps on
    ∂U(0, δ), and in the annulus 𝒵̃_out·N carries the e^{−cN} lip jumps. The commutator K(s, z) is then not bounded
    across ∂U.
  - *Fix.* Use U(0, δ/2) for the hard-edge piece. On δ/2 ≤ |z| ≤ δ, Q̃^{±1} is bounded, since
    N^{σ₃/2}Φ ≈ f^{−σ₃/4}·(const)·Θ there. So the annulus belongs to "the rest". Do the same at β̂.
- **(d) Two factorizations of Φ** (§1.4(d)).
  - *Problem.* "B = (2π)^{−σ₃/2}const for |ζ| ≥ 2 and B = Ψ̂ for |ζ| ≤ 3" defines two different factorizations Φ = Bζ^{−σ₃/4}Θ
    on an overlap.
  - *Fix.* Add a ζ-plane partition χ_{≤3} + χ_{≥2} and treat the blocks separately:
    - small–small: the Ψ̂-commutator is bounded on |ζ| ≤ 3, with Hilbert–Schmidt norm N-free;
    - large–large: B is a constant diagonal, so there is no commutator;
    - overlap annulus: Φ^{±1} is bounded, so the plain Cauchy bound applies;
    - separated cross blocks: Hilbert–Schmidt, with ∫_{|ζ|≥3}|ζ|^{1/2}|ζ|^{−2}|dζ| < ∞.
  - I checked that each block is uniformly bounded.
- **(e) Soft-edge piece** (§1.4(e)).
  - *Problem.* "Q̃ = A_rN^{σ₃/6}Φ_Ai(ζ)" omits the right-most scalar factor. Since α_W = 5/8, the local behaviour is
    V = O(1)(z − β̂)^{−σ₃/8} (WLXZ (5.7)). So Q̃ = A_r N^{σ₃/6}Φ_Ai(ζ)e^{Nφ̃σ₃}(D_w/W_r)^{σ₃}, with W_r the local
    continuation of w₀^{1/2}.
  - *Fix.* State that D_w/W_r is bounded with bounded inverse on U(β̂, ε), uniformly. This is the Hölder-endpoint
    argument of RH_px Lemma 3.4 at a (β̂ − x)^{1/4} endpoint. Note that it enters only as a multiplication operator
    (on the input through Q̃^{−1}, on the output through Q̃), so it needs no commutator.
- **(f) Cosmetic, inside UR.**
  - (a) states |Q̃^{−1}| = O(N|z − z₀|^{−1/4}), but (d) gives CN^{1/2}|ζ|^{−1/4} = C|z|^{−1/4}.
  - In the K-term, all four sign combinations |s|^{±1/4}|z|^{±1/4} occur, not only "±/∓". The Hilbert–Schmidt norm is
    still O(1), since ∬|s|^{−1/2}|z|^{−1/2} < ∞.
- **Missing numerical evidence.** Nothing tests UR directly. That is acceptable for an analytic lemma, but a short probe
  would be cheap insurance. For example, discretize 1 − C_ṽ on Σ ∩ U(0, δ) in the ζ-variable, with Nyström on the
  3-ray star, and watch the smallest singular value for N = 10², 10³, 10⁴.

### F2 (minor; Rule C): local Bessel structure and three standard facts are used but not quoted

- **Bessel factorization near 0** (§1.4(d), §1.6, Prop. D inner bounds).
  - *Problem.* Two facts are used:
    - the factorization Ψ(ζ) = Ψ̂(ζ)ζ^{−σ₃/4}S_j for α = −½, with Ψ̂ entire and S_j constant per sector;
    - the bounds |Ψ^{±1}| ≲ |ζ|^{−1/4} near 0.
  - CITATIONS.md only says "the behaviour (6.19)–(6.21) at 0". It quotes neither (6.19) nor (6.23)–(6.25) verbatim.
  - I read KMVV: (6.19) gives only O(|ζ|^{α/2}) entrywise. That is enough for Prop. D, but not for the factorization
    UR needs.
  - The factorization is true. I checked it: for α = −½ the entries are elementary.
    - I_{−1/2}(x) = (2/(πx))^{1/2}cosh x and K_{−1/2} = K_{1/2} = (π/(2x))^{1/2}e^{−x}.
    - Since K_{−1/2} = (π/2)(I_{−1/2} − I_{1/2}), column 1 of (6.23) is ζ^{−1/4}·(entire), and column 2 is that plus
      ζ^{1/4}·(entire).
    - So Ψ = Ψ̂ζ^{−σ₃/4}S with S constant upper-triangular.
  - *Fix.* Do two things:
    - quote KMVV (6.19) and (6.23)–(6.25) verbatim;
    - add the DLMF half-order formulas (§10.39 for I_{±1/2}, K_{1/2}; §10.27 for K_ν = π(I_{−ν} − I_ν)/(2sin νπ)), or
      write the 3-line explicit derivation above.
- **Hurwitz's theorem** (Lemma U(iii), uniform univalence). Not quoted. Quote a textbook statement (e.g. Ahlfors,
  *Complex Analysis*, Ch. 5), or give the argument directly: f_N(z) − f_N(w) = (z − w)·F_N(z, w) with
  F_N → F_∞ ≠ 0 uniformly.
- **Lemma W.** The Mellin–Plancherel theorem and PV∫₀^∞u^{s−1}du/(u − 1) = −π cot(πs) on 0 < Re s < 1 are textbook facts.
  "Standard" is not a citation (Rule C.3). Quote a source (Titchmarsh, *Fourier Integrals*, Mellin Plancherel;
  Gradshteyn–Ryzhik 3.222.2), or derive them in a footnote.
- The A₂ / weighted-Hilbert facts are *not* needed as citations, because Lemma W proves them.

### F3 (minor): Proposition D, the second-moment formula is misstated

- *Problem.* "Q₂ − Q̃₂ is the same with an extra factor z" is not the expansion. Write h := Q₋(v − ṽ)ṽ^{−1}Q̃₋^{−1}. From
  QQ̃^{−1} = I + C(h):

    Q₂ − Q̃₂ = −(1/2πi)∫_Σ s·h(s)ds + (Q₁ − Q̃₁)Q̃₁.

- The conclusion survives, because Q̃₁ = O(1) in the D_∞-frame and h is supported in U(0, δ) (plus super-small (h1)
  parts).
- *Fix.* Write the correct formula. A related remark: C–D's (4.14) is written without the ṽ^{−1}. Their jump structure
  makes (v − ṽ)ṽ^{−1} = v − ṽ, which is true here too (e₁ᵀ[[1, 0], [−c, 1]] = e₁ᵀ). The doc's version with ṽ^{−1} is the
  one that follows from Thm 4.4, and it is correct.

### F4 (minor): §1.6, the hypotheses of C–D Thm 4.4 for the *true* Q are asserted, not checked

- *Problem.* "Q = O(|z|^{−1/4}Λ^{1/2}) at 0 … this is (Y4)_x of RH_px §5 with the extra Λ factor."
  - (Y4)_x was proved for σ_{p,s}. For σ_ζ the weights and the node density differ (masses 2x_j,
    x_j ≍ j^{−2}log²j).
  - Q ∈ I + ∂C(L²) also needs L²-boundedness at the other contour vertices: β̂, the far-end corners, the junction with
    the Σ^△ top pieces.
- *Fix.*
  - **At 0.** Redo the (Y4)_x sum: Σ_j 2x_j/max(|z|, x_j) = O(|z|^{−1/2}·log(1/|z|)·(1/log s)) in rescaled units,
    together with the lens-sector argument verbatim. Then Q = O(|z|^{−1/4}polylog), which is in L²_loc.
  - **At β̂.** V = O(1)(z − β̂)^{−σ₃/8} (WLXZ (5.7)), so Q = O(1) after the D_w^{σ₃} conjugation.
  - **Corners.** All jumps are bounded and the solution is bounded.
  - This is about 6 lines.

### F5 (minor): §3 Lemma U(i) and §4 Lemma D1, the non-compact ρ-range

- *Problem.* The key approximation is stated "for ρ in compacts":

    ℓ(Nρ)/ℓ(N) = ρ^{ε(N)}(1 + O(ε²log²ρ)),

  But 𝒜_N integrates over ρ ∈ [3/(8N), ρ_b]. For ρ ≲ N^{−1/2} one has ε|log ρ| ≳ 1, so the relative expansion fails;
  near ρ ~ 1/N, ℓ is not slowly varying at all.
- The conclusion holds, because the integrand deviation is weighted by u = bρ²ℓ(N)/ℓ(Nρ) ≲ ρ². So
  ∫₀^{ρ₀}O(ρ²ε²log²ρ)dρ = O(ε²) and ∫₀^{N^{−1/2}}O(ρ²)dρ = O(N^{−3/2}).
- *Fix.* Add these two lines. Also write the second-order step: ε(r) − ε(N) = O(log(r/N)/Λ²), since
  ε′(r) = O(1/(rΛ(r)²)) + O(1/(rγ)). Integrated, it gives the O(ε²log²ρ).
- Similarly, for complex b in Lemma U(i), say that the substitution v = m(ρ) := ρ²ℓ(N)/ℓ(Nρ) is real and monotone, so
  𝒜_N(b) = ∫₀^{v_max}(1 − bv)^{−1/2}(dρ/dv)dv extends analytically off the real b-axis.

### F6 (minor; numerics interpretation): check_z_cmp does not test Proposition D, and one number is misreported

- **What check_z_cmp compares.** It compares the OPs of σ_ζ with those of σ̃ (masses 2x_j/Λ). σ̃'s RH problem is *not*
  Q̃:
  - Q̃ is σ_ζ's own problem with W̃ := D_w;
  - σ̃ has a different band weight, so a different D_w, Airy factor and 𝒵̃.
- **Why the 1/N coefficients differ.** Both b_N(σ_ζ) and b_N(σ̃) are (β_N/4)(1 + c/N + …). The constant c depends on
  the weight's local data at both edges, as in RH_px, where d₁ = −(s − 1)/2. Λ varies by a relative O(1/log N) across
  the rescaled band, so the two constants differ by O(1/log N) through the *global* 1/N terms.
- **Conclusion.** The measured ≈ 0.5/(N log N) is consistent with Prop. D but does not isolate it.
  - Prop. D is an upper bound and is probably not sharp. The first-order lip mismatches ∓iπ/(2Λ) have opposite signs
    on the two lips, which is the mechanism that gives C–D's 1/(n log²n).
  - The phrase "the order of Proposition D" (§1.7) should read "consistent with".
- **Misreported number.** "The a_N/(2b_N) difference is ~10⁻⁴/N" is wrong. The .out column N·(e − ẽ) = 0.00317, 0.00143,
  0.00065, …, 0.00003 halves with each doubling of N. So e − ẽ ≈ 0.16/N².
- **Docstring.** check_z_cmp.py says the σ·Λ control should differ "with the opposite sign". As computed (bsq/b vs
  b/bt), both ratios multiply by Λ in the same direction and are positive, as they should be. Reword the docstring.

### F7 (minor/cosmetic): §2 Lemma Z, small corrections (the substance is verified)

- **(a) Numbers.**
  - x_e = 1/(4π² + ¼) = **0.025171**, not 0.02527.
  - Checked: x₁ = 0.004736 (y log(y/e) = −3/8, y = γ/2π ≈ 2.311) and x_cross = 0.003431. C's distance to 0 is
    Rad − c₀ = r. ✓
- **(b) "Near 0, Im t → −∞".** This is not true along directions tangent to the positive axis, where Im t → 0. What
  the maximum principle needs (Im t ≤ 0 near 0 in Ω) holds, and the one-line reason should replace the sentence:

    2π Im t = Im γ·log|γ/2πe| + Re γ·arg γ < 0,  since arg γ ∈ (−π/2, 0) and |γ| > 2πe.

- **(c) Certificate details I checked.** These could be stated in the doc.
  - *Arc balls.* The rectangle half-width Rad(hi − lo)/2·(1 + 10⁻⁶) bounds the chord, so it covers the arc piece.
    The midpoint's own 2^{−128} radius is dominated by the 10⁻⁶ margin down to depth 40.
  - *The "rotated" determination of γ at π/2.* −i(−u)^{1/2} and u^{1/2} agree on the whole open lower half-plane in u,
    and z on the upper arc gives Im u < 0. So the switch is harmless everywhere, not only at π/2.
  - *Rectangles straddling ℝ near θ = 0 and π.* They stay on the continuous side of both square roots and of
    log(γ/2πe).
  - *Poles.* Poles of D_up at integer t make the ball test fail, which forces subdivision.
  - *Tail monotonicity.* d/dη of |Im t|/|Re t| = (2/π)log(η/2πe)·η/(η − 5.5) is positive iff
    η − 5.5 > 5.5·log(η/2πe), which holds for η ≥ η₀ = 3162. So ph t → −π/2 monotonically, |t| and −Im t increase,
    and the DLMF n = 1 bound decreases.
  - *Branch.* μ computed from the principal lgamma is Binet's function, since t avoids (−∞, 0].
- **(d) The 10⁻²⁸ value.** ℓ̂_arc(−r) = ℓ̂_axis(−r) to 10⁻²⁸ is not a coincidence: the winding is an integer, so
  certifying |W| < ½ forces equality. Worth one sentence.

### F8 (minor): Lemma A1(ii) cites a numerical print for an analytic input

- *Problem.* "ℓ̂(y) = O(|y|^{1/2}) as y → 0⁻ (checks/check_z_e2e_xi.out prints … ≤ 2·10⁻⁸)". A printed value is not a
  proof (Rule N.2), and Lemma 3.4's consequence needs a *derivative* bound.
- *Fix.* Use Binet/DLMF 5.11 as in §2's tail:
  - |μ(t)| ≤ sec²(½ph t)/(12|t|), with |t| ≍ |y|^{−1/2}log(1/|y|) and ph t → −π/2. So
    ℓ̂(y) = O(|y|^{1/2}/log(1/|y|));
  - the derivative is |μ′(t)t′(y)| = O(|y|^{−1/2}/log), and e^{−2πit} is super-small.
- Note also that log B is evaluated in z-units: log B_z(z) = log B_x(z/s) + const. Its Hölder-½ constant therefore
  improves by s^{−1/2}, which is what makes A1(ii) uniform in N.

### F9 (cosmetic): attribution and plan bookkeeping

- **κ fit.** §4: "This matches checks/check_z_kappa.out: the reviewer's fit to N = 10⁶⁰ gives −0.289472". The 10⁶⁰ fit
  is REVIEW_RHzeta.md probe P6, which was never committed; check_z_kappa.out stops at 10¹⁵ and contains no fit.
  - *Fix.* Cite the review, or commit the fit script.
- **Plan deviation.** Plan 14 A3/A4 (positivity of σ̃'s Gram matrix, GATE A4, fallback A4′) was replaced by the
  W̃ := D_w comparison and Lemma UR. A1's `check_z_lw0.py` was not produced. Record the deviation and the reason in
  LOG.md and the plan: the D_w route makes positivity unnecessary, and A1 is proved analytically.
- **Status lines.** RH_zeta.md's status line should point to this review once the fixes are in.

### F10 (minor; make an implicit geometric assumption explicit): v = ṽ inside U(β̂, ε)

- *Problem.* §1.2 asserts ṽ = v outside U(0, δ), "since the Airy parametrix uses σ_ζ's own weight". That is exact only
  with RH_px §4.2's geometry:
  - inside U(β̂, ε) the only contours are the band, (β̂, β̂ + ε) and the vertical segments;
  - the outer lips of the band lens and of Ω^△, where F̃ meets F and the (h1) diagonal factors D/D̃ live, lie outside
    U(β̂, ε).
- **Why it matters.** If those lips entered U(β̂, ε), v − ṽ would contain entries of size e^{−cN|z−β̂|}. Against
  |μ̃|² ≲ N^{1/3}, Prop. D would then give only O(N^{−2/3}).
- *Fix.* State the geometry: the lips sit at height > ε near β̂, as in WLXZ (6.4). Note that in U(0, δ) the (h1)
  entries are exp(−cN|z|^{−1/2}), so they are harmless there.

## Checked and OK (re-derived)

**§1.0 / H1.**
- The Q-frame jumps:
  - the band jump D_w^{−σ₃}[[0, w₀], [−1/w₀, 0]]D_w^{σ₃} = J₀;
  - the lip entry D_w²e^{2Nφ}/w₀.
- The comparison problem:
  - Ẽ_N = D_∞^{σ₃}N₀Mf^{σ₃/4}(2πN)^{σ₃/2} has no band jump, since M^{−1}J₀M = diag(i, −i) and
    f₊^{σ₃/4} = diag(−i, i)f₋^{σ₃/4};
  - its singularity at 0 is O(|z|^{−1/2}), hence removable, and det = 1.
- The lip entries of P̃₀: σ₃-conjugation and D_w^{σ₃} give −(Ψ-jump)/D_w², and e^{−Nφσ₃}(·)e^{Nφσ₃} gives the factor
  e^{2Nφ}. So c_± = e^{∓iπα} = ±i, consistent with KMVV (6.45) and confirmed numerically (cpm.py).
- Matching on ∂U: Ẽσ₃Ψσ₃e^{Nφσ₃}N₀^{−1} = N₀Mf^{σ₃/4}f^{−σ₃/4}(σ₃Mσ₃)(I + O(ζ^{−1/2}))N₀^{−1} = I + O(1/N), using
  σ₃Mσ₃ = M^{−1} and e^{Nφ} = (−1)^Ne^{−2ζ^{1/2}}.
- Q̃ → I at ∞.

**A1 and LW1.**
- 4πz|t′| = Λs^{1/2}z^{−1/2}(1 − z/4s)^{−1/2}.
- t′/t² ≍ |z|^{−1/2}/(s^{1/2}Λ) = O(|z|^{−1/2}/N).
- The Szegő representation constant: (R/2π)∫dx/(√(x(β̂ − x))(z − x)) = ½.
- The Λ-factor scaling integral, ∫(|log u| + π)u^{−1/2}(1 + u)^{−1}du < ∞, with sup|d log Λ/d log z| ≤ 1/(c log N).
- check_z_lw1: sup|G²/Λ − 1|·log N → 1.56 ≈ π/2, which matches the first-order term ∓iπ/(2Λ). The sup norm of v − ṽ is
  ≤ C/log N, since the |z|^{1/3} part is killed by e^{−cN|z|^{1/2}}.

**Lemma W.**
- Off-diagonal Mellin symbol: absolutely convergent iff −½ < a < ½, and bounded in τ (L¹ bound).
- Diagonal symbol: −π cot(πs), bounded on Re s ∈ (0, 1), plus the constant ±½ from C±.
- Flattening C² arcs: with the complex measure ds, the kernel difference is O(h″) = O(1), and with weights it is
  Hilbert–Schmidt for |a| < ½.
- In UR the lips are exact preimages of rays, so no flattening is needed in the ζ-plane.

**UR core.**
- The explicit solution: m₊ − m₋ṽ = (C₊ − C₋)(gQ̃₊^{−1})Q̃₊ = g.
- The reduction μ = m₋ + f gives μ − C₋(μ(ṽ − I)) = f, and injectivity plus a bounded right inverse gives the inverse.
- Factorization: Q̃ = A₀(2πN)^{σ₃/2}Φ, with D_w cancelling.
- The I-term: N^{∓σ₃/2} cancel, and the core is two Lemma-W columns with a = −¼ and +¼.
- The K-term: N^{σ₃/2}ζ^{−σ₃/4} = f^{−σ₃/4}. Its Hilbert–Schmidt norms are:
  - O(1) (large–large);
  - O(N^{−1}) (mixed);
  - O(N^{−2}) (small–small).
- The change of variables ζ = N²f: the kernel difference is bounded, with weight ratio |s/z|^{±1/4} N-free.
- Soft edge: small-ζ Hilbert–Schmidt O(N^{2/3}·N^{−4/3}).
- Separated pieces: Hilbert–Schmidt against ∫|s − z|^{−2} over the long straight pieces, which is length-independent.
- The third piece: L^∞ multipliers times a Carleson Cauchy operator.

**Theorem C.** ‖C_v − C_ṽ‖ ≤ ‖C₋‖‖v − ṽ‖_∞, followed by the Neumann series. These are exactly C–D (4.12)–(4.13) as
quoted and as checked against the PDF.

**Prop. D.**
- The formula, from C–D Thm 4.4 (verbatim in the PDF).
- (v − ṽ)ṽ^{−1} = δe₂e₁ᵀ.
- μ̃e₂e₁ᵀμ̃^{−1}e^{2Nφ} = A₀N^{σ₃/2}σ₃Ψ(σ₃e₂e₁ᵀσ₃)Ψ^{−1}σ₃N^{−σ₃/2}A₀^{−1}.
- e^{−4ζ^{1/2}} with Re ζ^{1/2} = ½|ζ|^{1/2} on γ₁ and γ₃.
- The main-term integrals:
  - (1/log N)∫r^{−1/2}e^{−cN√r}dr = O(1/(N log N));
  - N∫₀^{N^{−2}}(N²r)^{−1/2}dr = O(1/N);
  - the |z|^{1/3} part is O(N^{−5/3}).
- The correction: μ − μ̃ = (1 − C_v)^{−1}C₋(μ̃(v − ṽ)), with both L² factors O(N^{−1/2}/log N).
- μ = (1 − C_v)^{−1}I makes sense, as I + (1 − C_v)^{−1}C₋(v − I). v − I is O(1) only on the bounded band, and
  e^{−cN} on the length-O(N²) pieces.

**§1.7.**
- Invariance: Q = D_∞^{−σ₃}VD_w^{σ₃} is of the form CYk^{σ₃} with Ck_∞^{σ₃} = I.
- (N₀,₁)₁₂(N₀,₁)₂₁ = (β̂/4)² with nonzero entries, so the absolute O(1/(N log N)) is relative.
- a(N₀) = β̂/2.

**§2.**
- The parametrization and the jump-sum formula: winding = −(J(x_m) + J(−r))/2πi, with J = after − before
  counterclockwise.
- At x_m: H₊ − H₋ = 2πit̂ (H = 2πi·C(t̂)); Log(1 − e^{2πit}) − Log(1 − e^{−2πit}) = i(2πt − π) for t ∈ (3/8, 1), where
  arg(1 − e^{2πit}) = πt − π/2 is principal; log K₊ − log K₋ = iπ/4. Hence J(x_m) = 0, and 3πi/4 without the shift.
- At −r: log B₋ − log B₊ = iℓ̂_axis (log B = −C(iℓ̂)); log D_up − log D_low = iℓ̂_arc by conjugation symmetry with conjugate
  starting values.
- The maximum principle (with F7(b)).
- (iii): L is Lipschitz, because the boundary values of the Cauchy integrals with smooth densities are smooth up to the
  crossings. The Ξ estimate is O(β_N).
- N-independence: H and K are continuous at −r, J(x_m) = 0 for every β < x_m, and D, B, t are N-free in x-units.
- Re-run: byte-identical.

**§3.**
- ε(r) = 2/Λ + O(1/γ), via d log γ/d log r = 1 − 1/Λ + O(1/γ).
- Λ(N) = log N − log log N + O(1).
- G(z; b) − G(0; b) = z^{1/2}·(analytic).
- The tail integrability ∫b^{−1/2}b^{−3/2}db.
- −𝒜_∞′(β̂) = π/(4β̂^{3/2}).

**§4.**
- J(p) = (1/p)B(1/p, ½), the exact approximate integral, and log β̂ = 2log J(2) − ε(log J(2) + 2J′(2)/J(2)) + O(ε²).
- (log J)′(2) = −(1 − log 2)/2 and ψ(3/2) − ψ(1) = 2 − 2log 2.
- κ = −2(0.451583 − 0.306853) = −0.289460, matching check_z_kappa's predicted −0.2894597717.
- The O(log log N/log²N) error is inherited from ε(N).

**Citations.** The C–D quotes of Thm 4.4, Prop. 4.6 and Prop. 4.9 match the arXiv v4 text. The doc's use of only the
easy direction of Prop. 4.6 (re-proved) is accurate. Thm 4.5 is correctly *not* used.

## Label table (recommended)

| Item | Label after fixes | Blocking findings |
|---|---|---|
| §1 H1, LW1 | PROVED-mod-cite (KMVV §6) | F2 |
| §1 Lemma W | PROVED | F2 (Mellin/PV source) |
| §1 Lemma UR | PROVED | **F1 (a)–(e)** |
| §1 Theorem C, Prop. D, §1.7 | PROVED-mod-cite (C–D Thm 4.4) | F3, F4, F10 |
| §2 Lemma Z | PROVED; winding CERTIFIED | F7(b) (wording) |
| §3 Lemma U | PROVED-mod-cite (Hurwitz, WLXZ §6.1) | F2, F5 |
| §4 Lemma D1 | PROVED | F5 |
| Theorem RH_ζ | **PROVED-mod-cite** (WLXZ v1, KMVV §6, C–D Thm 4.4, DLMF, G2), REVIEWED after the fixes are re-checked | F1–F5, F10 |
| check_z_cmp interpretation | NUMERICAL corroboration (not a test of Prop. D) | F6 |
