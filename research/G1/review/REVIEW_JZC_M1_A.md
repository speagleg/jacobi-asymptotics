# Rule R review, reviewer A: JZC_M1.md (Theorem Q, Corollary Q.1, Proposition M1.2)

Reviewer: independent second reader (Rule R), reviewer **A**. Remit:
1. Theorem Q (i)–(iv), line by line, and the sufficiency of (H1)–(H3).
2. Corollary Q.1 (a = 4c(p)).
3. Proposition M1.2: the Mellin–Barnes statement, residue signs, the "no oscillatory terms" claim, the first-order η, and the label.
4. Independent numerics (my own code, not reruns).
5. A sabotage test of m1_theoremQ.py.
6. Novelty (first pass, web only).

- **Target:** research/G1/RH/spectral/JZC_M1.md (2026-10-21, 170 lines), with checks/m1_theoremQ.py/.out and checks/m1_edge.py/.out.
- **Context read:** AGENTS.md, VERIFICATION_POLICY.md, SPEC.md §3.14 (Lemma K0, Theorem K, Lemma Q, Proposition E, Hypothesis G) and
  §3.16, spec_common.py (Checks, c_p_mp), REVIEW_SPEC2_A.md (format).
- I edited no repository file except this report. My scripts are in
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/review_m1/.
- Nothing here concerns RH or any other hypothesis on zeros. The "log law" density is used only as a test density.

## Overall verdict: **ACCEPT WITH FIXES**

The mathematics checks out. I re-derived every step of Theorem Q (i)–(iv), Corollary Q.1 and the residue/Mellin algebra of
Proposition M1.2, and found no sign error. Two independent computations confirm the results:
- **A discretised constrained energy minimisation** reproduces a and ν to discretisation accuracy, converging at O(h).
- **A linearised closed-form computation of the M1.2 pole term** agrees to 10⁻¹⁰–10⁻¹⁴, including a case not in m1_edge.py.

One finding is MAJOR, and it concerns the labels, not the truth of the statements:
- **F1:** both "PROVED-mod-cite" labels rest on inputs the note marks NOT QUOTED. VERIFICATION_POLICY defines PROVED-mod-cite as
  "proved from explicitly cited external results X, each read and quoted with its hypotheses". So neither label is compliant as
  written.
- All three gaps can be closed with short elementary arguments, given below:
  - (a) an inversion that reduces (iv) to the compact case;
  - (b) a Liouville argument that replaces the balayage citation;
  - (c) direct termwise integration for M1.2.
- With these, Theorem Q becomes PROVED-mod-cite with one quotable textbook lemma, and M1.2 becomes PROVED.

The other findings: a wrong sentence in the Remark about square-root vanishing (F3), a missing regularity hypothesis in (iii)
(F2), edge cases in the statement of M1.2 (F4), and weaknesses in the m1_theoremQ assertions that the sabotage test exposes (F5).

| Item | Verdict | Findings |
|---|---|---|
| 1. Theorem Q (i)–(iv) | ACCEPT WITH FIXES (all steps re-derived; label and two gaps) | F1(a,b), F2, F3, F6, F7 |
| 2. Corollary Q.1 | ACCEPT (re-derived; numerically 4c to 10⁻¹²) | F8 |
| 3. Proposition M1.2 | statement ACCEPT WITH FIXES; proof as written is a sketch | F1(c), F4 |
| 4. Checks m1_theoremQ / m1_edge | m1_edge ACCEPT; m1_theoremQ ACCEPT WITH FIXES | F5, F9 |
| 5. Novelty | NOT FOUND stands, but the endpoint equations and the monotonicity-criterion type are known; cite them | F10 |

## 1. Theorem Q, step by step

**(i) Monotonicity of F.** Substituting y = au gives F(a) = ∫_1^{Y/a}aσ(au)(1 − 1/u)^{−1/2}du.
- aσ(au) = (au·σ(au))/u is strictly decreasing in a by (H2), and Y/a decreases. So F is strictly decreasing. Correct.
- F is finite: near y = a the integrand is O((y − a)^{−1/2}); at ∞ the log-moment in (H3) gives ∫^∞σ < ∞.
- F is continuous (dominated convergence). The proof does not say so; it is trivial.
- **a → 0:** F(a) ≥ ∫_a^Yσ → ∞. Correct.
- **a → Y < ∞:** σ is bounded near Y, since σ(y) ≤ y₀σ(y₀)/y by (H2), so F → 0. Correct.
- **Y = ∞:** the split at 2a is right. The bound on [a, 2a] uses σ(y) ≤ aσ(a)/y ≤ σ(a) and ∫_a^{2a}(1 − a/y)^{−1/2}dy =
  a∫_1^2(1 − 1/u)^{−1/2}du. Correct.

**(ii) Balayage and Cauchy transform.**
- **Balayage density.** I re-derived it from the [−1, 1] formula √(t² − 1)/(π(t − u)√(1 − u²)) by the affine map:
  √(y(y − a))/(π(y − x)√(x(a − x))). Correct.
- **Boundary value of R.** With R(z) = z√(1 − a/z) (principal branch), on (0, a) we have 1 − a/(x + i0) = (1 − a/x) + i0⁺. So
  R(x + i0) = i√(x(a − x)).
- **C_y(z) = (1 − R(y)/R(z))/(z − y).** It is analytic off [0, a], removable at z = y, and ~ 1/z at ∞. Its density is
  −(1/π)Im C_y(x + i0) = R(y)/(π(y − x)√(x(a − x))) > 0. Correct, sign included.
- **Arcsine measure.** It has Cauchy transform 1/R, with density 1/(π√(x(a − x))). Correct.
- **The Cauchy transform G of μ.** With ω the arcsine measure, G = 1/R − ∫σC_y + ∫σ/(z − y) = (1/R)[1 + ∫σR(y)/(z − y)dy]. Correct. The
  integral converges at ∞ because σR ~ yσ and ∫σ < ∞.
- **(G).** Use σR(y) = s(y)(y − a) and 1 = ∫s:
  - 1 + ∫s(y − a)/(z − y) = ∫s·(z − a)/(z − y);
  - (z − a)/R(z) = √((z − a)/z), analytic off [0, a] and → 1 at ∞.
  Correct.
- **Branch on (0, a).** √((z − a)/z) at x + i0 is i√((a − x)/x), from the same computation as R. S(x) = ∫s/(x − y) < 0 is real.
  So ν = −(1/π)Im G(x + i0) = (1/π)√((a − x)/x)∫s/(y − x) > 0. Correct.
- **Balayage form.** (1/π)√((a − x)/x)∫s/(y − x)·π√(x(a − x)) = ∫s(a − x)/(y − x) = ∫s − ∫s(y − a)/(y − x) =
  1 − ∫σ√(y(y − a))/(y − x), using (Q). Correct.
- **ν < σ.** ∫_0^∞v^{−1/2}(v + c)^{−1}dv = π/√c, g(y) < g(a) for y > a, and g(a) < g(x) for x < a. Correct and strict. Note that
  only g = √y·σ decreasing is used here (F7).
- **Unit mass.** The mass of ν is 1 − ∫_a^Yσ, because balayage out of an unbounded domain preserves mass. So unit mass holds for
  **every** a, not only the root of (Q). Equivalently (F5), the mass of ν_explicit + σ is ∫s = F(a). (Q) is what makes the explicit
  form equal the balayage form.
- **Integrability.** ν ~ (1/π)√a·x^{−1/2}∫s/y near 0, which is integrable. As x → a⁻, ν(x) → g(a)/√a = σ(a), so ν is bounded,
  continuous, and meets σ at a (F3).

**(iii) Outer inequality.**
- **φ′ = −Re G(z ± i0) = −√((z − a)/z)·H(z).** Correct given differentiability (F2).
- **The decomposition of H.** The first integrand (g(y) − g(z))(y − a)^{−1/2}/(z − y) is ≥ 0 on both sides of z, so the sign is
  right. The integral is positive, possibly +∞ if g is not Lipschitz, which is harmless.
- **Y = ∞.** With y − a = v², z − a = c²: PV∫_a^∞(y − a)^{−1/2}(z − y)^{−1}dy = 2·PV∫_0^∞dv/(c² − v²) = 0. Correct.
- **Y < ∞.** 2·PV∫_0^Vdv/(c² − v²) = (1/c)log((V + c)/(V − c)), with V = √(Y − a). This is the stated
  (z − a)^{−1/2}log[(√(Y − a) + √(z − a))/(√(Y − a) − √(z − a))] > 0. It is consistent with
  −∫_Y^∞ = +∫_Y^∞(y − a)^{−1/2}/(y − z) > 0. The **sign is correct**, and "the cut helps" is right.
- **Endpoints.** φ(a) = 0 by continuity, and φ(Y) < 0 by monotonicity and continuity. Correct.
- **Direct confirmation** (thq_potential.py: plain quadrature of −∫log|z − x|dμ, no Cauchy transforms):
  - U^μ − ℓ = O(10⁻¹³) at five points of [0, a];
  - U^μ − ℓ < 0 at 6–8 points of (a, Y], down to z = 1.001a and z = Y;
  - near a, U^μ − ℓ scales like (z − a)^{3/2} (−7.0·10⁻⁵ at 1.001a, −2.2·10⁻³ at 1.01a).

**(iv) Minimality.**
- The identity I(μ′) − I(μ) = I(μ′ − μ) + 2∫(U^μ − ℓ)d(μ′ − μ) needs ∫|U^μ|dμ′ < ∞. This holds, because U^μ ~ −log y at ∞ and
  μ′ ≤ σ has a finite log-moment by (H3).
- The sign argument on (a, Y] is right: U^μ − ℓ < 0 and μ′ − σ ≤ 0.
- The remaining input, positivity of I(τ) for a zero-mass τ with non-compact support, can be reduced to the compact case (F1(a)).

**Hypotheses (H1)–(H3).**
- **Sufficient**, with these remarks:
  - (H3)'s first clause is implied by (H1)+(H2) (F6).
  - Differentiability in (iii) needs a little more than continuity (F2).
  - (H2) can be weakened (F7).
- **Integrability:**
  - s is integrable at y = a, with s ~ g(a)(y − a)^{−1/2};
  - μ has finite energy: x^{−1/2} at 0, bounded near a, and the log-moment at ∞;
  - ν is integrable at 0 and bounded at a.
  No missing hypothesis beyond F2.

## 2. Corollary Q.1

Substituting y = a/t gives F(a) = (1/p)a^{−1/p}∫_0^1t^{1/p−1}(1 − t)^{−1/2}dt = (1/p)a^{−1/p}B(1/p, ½). Then:
- a^{1/p} = √πΓ(1/p + 1)/Γ(1/p + ½);
- π/(2I) = πΓ(1/p + 1)/(√πΓ(1/p + ½)), which is the same;
- so a = (π/(2I))^p = 4c.
(H2) and (H3) hold for the power law.

Numerically (my code), a = 1.717810737111 and 2.265089372402 at p = 0.6 and 1.5. Both equal 4c and ((1/p)B(1/p, ½))^p to 12 digits.

## 3. Proposition M1.2

**Residues.** For a term c_ρλ^ρ of N:
- ∫_{λ₀}^∞λ^{−s}ρc_ρλ^{ρ−1}dλ = ρc_ρλ₀^{ρ−s}/(s − ρ), so the s-residue is ρc_ρ;
- in w = −s the residue is −ρc_ρ, at q = −ρ. Correct.
- Weyl pole: R = −1/p at q = −1/p, consistent with Prop. E.
- Drum: ρ = ½, c = −β, so R_{−1/2} = +β/2, consistent with §3.16.
- m1_edge: κ = λ^{1/p} − gλ^{−m/p}, so R = −mg/p. Correct.

**Mellin–Barnes orientation.**
- L(u) = (1/2πi)∫_{(c)}L̃(w)u^wdw, with c < −1/p so that Z_N(−w) converges.
- Shifting the line to the right gives −ΣRes:
  - poles of Z_N(−w) give −R_qL̃(q)A^q;
  - poles of L̃ give +C(2j, j)4^{−j}Z_N(−j)A^j.
  Correct.
- The Weyl term is (1/p)B(1/p, ½)A^{−1/p} = n(a/4c)^{−1/p}. Correct.
- (4c)^q(−L̃(q)) = W(q)π cot(πq), and C(2j, j)4^{−j}(4c)^j = W(j).

**First-order η.** Linearising n(1 + η)^{−1/p} gives −nη/p. Every cross term η × (correction) is O(nη²), including the
negative-q (growing) poles, for which η·n^{−pq} ~ nη². The formula is correct.

**Drum, nonlinear terms.** p = 1, c = ½, and 2/A − (πβ/2)A^{−1/2} + C₀ = n. With X = (1 + η)^{−1/2}:
- nX² − (πβ/(2√2))√n·X + C₀ − n = 0;
- nη = −(πβ/(2√2))√n + π²β²/16 + C₀ + O(n^{−1/2}).
This confirms the §3.16 coefficients.

**The proof as written (F1(c)).**
- **The contour shift is not justified by the stated reason.** On vertical lines |L̃(c + it)| ~ |t|^{−1/2}, because
  cot → ∓i and Γ(w + ½)/Γ(w + 1) ~ w^{−1/2}. So the shift needs decay of Z_N(−w) on vertical lines. "C¹ and termwise
  differentiable" does not provide this beyond the first strip.
- **"No oscillatory terms" is a heuristic.** The single integrable singularity of L at u = 1 explains it, but does not prove it.
- **An elementary proof exists.** Write N′ = Σ_{k<K}ρ_kc_kλ^{ρ_k−1} + r_K with r_K = O(λ^{ρ_K−1}). Then:
  - each power gives exactly ρc_ρ[A^{−ρ}B(ρ, ½) − Σ_jC(2j, j)4^{−j}A^jλ₀^{ρ+j}/(ρ + j)] = −R_qL̃(q)A^q + (integer powers), using
    B(ρ, ½) = L̃(−ρ);
  - for the remainder, split at λ = 1/(2A). Taylor-expand (1 − Aλ)^{−1/2} on [λ₀, 1/(2A)]. On [1/(2A), 1/A], bound
    |r_K| ≤ Cλ^{ρ_K−1}, which gives O(A^{−ρ_K});
  - the integer coefficients combine into the continued Z_N(−j) (take K large enough that ρ_K < −j).
  This gives the expansion with an explicit O(A^{−ρ_K}) remainder and no citation, i.e. PROVED.

**Independent numerics** (edge_lin.py; my implementation). I linearised the root exactly in g: n·dη/dg = −nG_g/(G_A·dA/dη),
with no finite differences. Both G and G_g are closed forms (A^{−r}B(r, ½) minus a convergent series), and I used 40 digits and
n = 10³…10¹⁰.

| (p, m) | fitted n^{−pq} coefficient | p R W(q) π cot(πq) | rel. diff |
|---|---|---|---|
| (1.5, 0.5) | −0.84940851465084 | −0.84940851465086 | 2·10⁻¹⁴ |
| (1.8, 0.75) | −0.61002613289057 | −0.61002613266680 | 4·10⁻¹⁰ |
| (0.6, 0.2), **not in m1_edge.py** | −0.30984174149816 | −0.30984174149598 | 7·10⁻¹² |

In every case the n⁰ coefficient is exactly p: the j = 0 term, since the g-part of Z_N(0) is 1. The two cases shared with
m1_edge.out agree with its fits (which reach 10⁻⁸ and 1.4·10⁻⁶).

## 4. Findings

**F1 (MAJOR): labels vs Rule C. Both PROVED-mod-cite labels rest on NOT-QUOTED inputs. All three gaps close with short arguments.**

- **(a) Theorem Q (iv), non-compact positivity.**
  - Map x ↦ x* := 1/(1 + x), which sends [0, Y] into (0, 1]. Then log(1/|x* − y*|) = log(1/|x − y|) + log(1 + x) + log(1 + y).
  - For atomless τ = μ′ − μ with τ(ℝ) = 0, finite energy, and ∫log(1 + x)d(μ + μ′) < ∞ (from (H3), since μ, μ′ ≤ σ), the extra
    terms integrate to 2τ(ℝ)∫log(1 + x)dτ = 0. So I(τ) = I(τ*), and also I(μ*) = I(μ) + 2∫log(1 + x)dμ < ∞.
  - τ* is compactly supported, has zero mass and finite energy, and τ* = 0 iff τ = 0. So I(τ) ≥ 0, with equality iff μ′ = μ,
    follows from the compact-support lemma alone.
  - Kernel identity checked numerically (inversion.py; for atoms the diagonal term −2Σw_i²log(1 + x_i) must be restored, and it
    agrees to 10⁻¹⁴).
  - That lemma (Saff–Totik, *Logarithmic Potentials with External Fields*, Lemma I.1.8 as usually cited; **I have not read it in
    this review**) must still be quoted in RH/CITATIONS.md. It is a far smaller ask than the non-compact statement.
- **(b) Theorem Q (ii)–(iii), the balayage citation.**
  - As usually stated, the balayage theorem for unbounded Ω (Saff–Totik Thm II.4.7, NOT READ here) concerns measures supported in
    Ω. Here σ|_{[a,Y]} touches ∂Ω = [0, a] at a, and is unbounded when Y = ∞. So a limiting argument would be needed in any case.
  - Simpler: define μ := ν_explicit dx + σ dy and show directly that its Cauchy transform is G̃ := √((z − a)/z)S(z). Both are
    analytic off [0, Y] and have the same jumps:
    - −2πiσ on (a, Y), from S(z ± i0) = H ∓ iπs and s = σ√(z/(z − a));
    - −2πiν on (0, a).
  - Both are o(1/|z − z₀|) at z₀ ∈ {0, a, Y} and → 0 at ∞. So by Riemann's removable-singularity theorem and Liouville they are
    equal.
  - Then Re G(x ± i0) = 0 on (0, a) (S is real there) gives U^μ = ℓ on [0, a], and G̃ ~ (∫s)/z gives unit mass. No balayage
    theorem is needed.
- **(c) Proposition M1.2.** Replace the Mellin–Barnes sketch with the termwise computation in §3 (PROVED). Otherwise relabel it
  CONDITIONAL / PROOF SKETCH.
- **Label change.** In the label table, change "PROVED-mod-cite (…NOT QUOTED)" to:
  - Theorem Q: PROVED-mod-cite (compact positivity lemma, to be quoted);
  - Prop. M1.2: PROVED.

**F2 (MINOR): differentiability in (iii).**
- φ′ = −Re G(z ± i0) needs the Hilbert transform of σ to exist at z, e.g. σ Dini- or Hölder-continuous. (H1) gives only continuity.
- Fix, either of:
  - add "σ locally Hölder on (0, Y)" to (H1); all SPEC densities are real-analytic there;
  - argue almost everywhere: U^μ is locally absolutely continuous, with derivative equal a.e. to the Hilbert transform of an
    L^p_loc density, so φ′ < 0 a.e. implies φ strictly decreasing.

**F3 (MINOR): the Remark on "square-root vanishing of the density at the soft edge a" is wrong.**
- ν(a⁻) = g(a)/√a = σ(a), so μ is continuous at a and does not vanish there. What vanishes is σ − ν ~ C√(a − x). Measured C:
  0.4713 (p = 0.6), 0.1245 (p = 1.5), 0.3239 (drum), stable over a − x = 10⁻²…10⁻⁵.
- (Q) is what removes the generic inverse-square-root (hard-edge) singularity of ν at a. Without (Q), ν has a ±(a − x)^{−1/2}
  term, which either violates ν ≤ σ or ν ≥ 0.
- Suggested text: "(Q) turns the generic 1/R(z) singularity at a into a bounded density meeting σ continuously; σ − ν vanishes like
  √(a − x)".

**F4 (MINOR): Proposition M1.2, statement edge cases.**
- (a) If some ρ ∈ {0, −1, −2, …} carries ρc_ρ ≠ 0, i.e. q ∈ ℤ_{≥1} (q = 0 has zero residue), the pole of Z_N(−w) meets a pole of L̃.
  That gives a double pole and an A^jlog A term: the §3.13 resonance. Exclude these q from the statement, or add the log term.
- (b) At q ∈ −½ − ℕ₀ the factor W(q)π cot(πq) is 0·∞. This includes the drum perimeter, q = −½. The first display, in terms of
  L̃(q) = B(−q, ½), is finite there (L̃(−½) = π). State the η formula with −(4c)^qL̃(q), or note that the limit is meant.
- (c) Expansions with log terms, like the log law used in m1_theoremQ, are outside M1.2 (double poles). Say so.

**F5 (MINOR): m1_theoremQ.py assertions are weaker than §4 suggests.**
- **(a) Two of the five checks per density are identities in F(a).**
  - ν_exp − ν_bal = (F(a) − 1)/(π√(x(a − x))) exactly.
  - The total mass of ν_exp + σ is ∫s = F(a), for every a (§1).
  - So "agree to 10⁻²¹" and "mass 1 to 10⁻¹¹" measure the accuracy of the root and the quadrature, not (G) or the balayage. The
    Rule A bullet "Is (G) consistent… agree to 10⁻²¹" should say so.
- **(b) The docstring overclaims.** It promises "(E) U^μ = const on [0, a] … and directly", but the script has no direct potential
  evaluation. The equilibrium on the band is not checked at all there. (SPEC's spec_kernel.out (Q) does check it, for the power
  laws only.)
- **(c) The outer-inequality check is only a sign test at 3 points.** Sabotage S1 (§6) flips the sign of the finite-Y PV term and
  passes all 20 assertions.
- **(d) The H2 check uses 4 points per decade.** Sabotage S4 inserts a narrow bump that violates H2; the grid check still prints
  True. The run failed only because one ν/σ sample point happened to fall where ν > σ.
- **Fixes:**
  - add a direct potential check (as in thq_potential.py);
  - compare Φ against an independent quantity, e.g. U(z) − ℓ = −∫_a^z√((t − a)/t)H(t)dt, or the closed-form finite-Y PV of the note;
  - verify (H2) analytically for each test density (all four are elementary; for the log law, yσ = log(T/2π)/(4π√y) is decreasing
    iff T > 2π/e, which the cut satisfies), or on a fine grid via the derivative.

**F6 (INFO): redundancies in (H3).**
- (H1)+(H2) give yσ(y) ≥ y₀σ(y₀) > 0 for y < y₀, so σ ≥ c/y and ∫_0σ = ∞ automatically.
- "yσ → 0" follows from (H2) and ∫^∞σ < ∞.
- So (H3) reduces to the log-moment when Y = ∞.
- If Y < 1, "∫_0^1σ" should read ∫_0^{min(1,Y)}σ.

**F7 (INFO; a strengthening).**
- Steps (ii)–(iv) use only "g = √y·σ decreasing". (i) needs existence only, F(0⁺) = ∫_0^Yσ > 1.
- Uniqueness of the root then follows from (iv): a is determined by μ as the left end of the saturation set, and the minimiser is
  unique. So (H2) can be replaced by "√y·σ(y) strictly decreasing and ∫_0^Yσ > 1".
- Numerical test (weakH2.py), σ = 0.2y^{−0.9} on (0, 10], where (H2) fails (yσ increasing) but g decreases:
  - one root, a = 0.29908;
  - ν/σ ∈ (0.20, 0.94);
  - U^μ − ℓ = O(10⁻¹⁵) on the band and < 0 outside.
- A density with g increasing (0.25y^{−0.4}) also satisfied the conclusions, with F non-monotone but one root. So neither
  condition is necessary.
- The Rule A bullet "(H2) is used three times" should become "(H2) is used once, in (i); (ii)–(iii) need only g decreasing".

**F8 (INFO): Corollary Q.1 label.** The computation a = 4c is PROVED. Its identification as the equilibrium edge inherits Theorem
Q's label. Write "PROVED (computation); equilibrium identification inherits Thm Q".

**F9 (INFO): provenance and text.**
- The m1_theoremQ docstring says the log law is "cut at T = 2 pi e"; the code and the note use 2πe^{1.5}.
- The m1_edge docstring's dN expression is garbled ("lam^{-(m+1)/p... ]"). The code is right: (1/p)λ^{1/p−1} + g(m/p)λ^{−m/p−1}.
- The m1_edge tolerance (2·10⁻³ relative) is 10³–10⁶ times looser than the accuracy achieved. Tighten it to 10⁻⁵.
- The note's per-case accuracies (1·10⁻⁹ … 1·10⁻⁶) match m1_edge.out.

**F10 (INFO): novelty (Rule L, first pass; see §7).** "NOT FOUND" is accurate for the exact statement. But closely related
structures are known, and the note should cite them:
- endpoint equations of the same Cauchy-integral type for the band/saturated transition, in Beckermann–Kuijlaars (2002), Thm 2.8;
- a monotonicity "ansatz criterion" guaranteeing the band/saturated structure, Thm 2.7 there: (x − A)Q′ and (B − x)Q̃′ increasing,
  Q̃ = −Q − U^σ, after Kuijlaars (Duke 2000) and Kuijlaars–McLaughlin.
Those are for compact supp σ = [A, B] with an external field and a void. JZC's setting is different: Q ≡ 0, a non-compact
constraint with infinite mass at 0, a hard edge at 0, and no void.

Suggested novelty: **POSSIBLY-NEW**, as a specialisation of the one-cut constrained framework to this configuration. Two parts
appear to be this project's: the explicit factorisation (G) and the criterion "yσ (or √yσ) decreasing". This is subject to reading
Kuijlaars 2000 (SIAM J. Matrix Anal. Appl., Q ≡ 0) and Dragnev–Saff 1997.

## 5. Independently verified

| Claim | My method (script) | Result |
|---|---|---|
| Thm Q (i): root a of (Q) | own substitution y = a/t, t = 1 − w², scipy brentq (thq_potential.py) | a = 1.717810737111, 2.265089372402, 1.671710534403 (p = 0.6, 1.5, drum): equal to m1_theoremQ.out |
| Cor Q.1: a = 4c | algebra; numerics as above | 4c and ((1/p)B)^p agree to 12 digits |
| Balayage density, C_y, arcsine, boundary values of R and √((z − a)/z) | by hand | correct, signs included |
| (G) and the balayage form | by hand | correct; (Q) used exactly once |
| ν > 0, ν < σ, ν(a⁻) = σ(a) | by hand; numerics | ν/σ ∈ (0, 1) at 5 points × 3 densities; ν(a⁻) = σ(a) |
| σ − ν ~ C√(a − x) | numerics | C stable to 4 digits over 10⁻³…10⁻⁵ (F3) |
| (iii) U^μ = ℓ on [0, a] | **direct log-potential quadrature**, no Cauchy transform | \|U − ℓ\| ≤ 1.3·10⁻¹³ |
| (iii) U^μ < ℓ on (a, Y] | same | < 0 at all tested points; ~ (z − a)^{3/2} near a |
| PV integrals (Y = ∞: 0; Y < ∞: log formula) | by hand | correct, sign positive |
| (iv) identity and sign argument | by hand | correct; positivity closed by inversion (F1(a)) |
| Inversion kernel identity | algebra + inversion.py | 10⁻¹⁴ |
| Constrained minimiser = Thm Q's μ | **discretised constrained energy minimisation** (P0 cells, exact cell log-kernel, BVLS; thq_qp.py, thq_qp_refine.py), p = 1.5 (truncated at 3000 with tail field) and drum | band density vs ν: 1–4·10⁻⁴ (1.2·10⁻³ at x = 0.1a), O(h) convergence (drum, x = 0.9a: 4.8·10⁻⁴ → 2.4·10⁻⁴ → 1.2·10⁻⁴); saturation edge within one cell of a; no unsaturated cell beyond a |
| Mass 1 | quadrature | 1 ± 4·10⁻¹² (but see F5(a)) |
| (H2) weakening | weakH2.py | F7 |
| M1.2 residues, MB orientation, W identities, first-order η | by hand | correct |
| M1.2 pole term (m1_edge) | **linearised closed form**, 40 digits, n ≤ 10¹⁰ (edge_lin.py) | 2·10⁻¹⁴, 4·10⁻¹⁰, 7·10⁻¹² (new case (0.6, 0.2)) |
| Drum nonlinear D (§3.16) | by hand | −(πβ/(2√2))√n + π²β²/16 confirmed |

## 6. Sabotage test (copies in my scratch directory; the repository script is untouched)

| Sabotage | Caught? |
|---|---|
| S1: sign of the finite-Y PV log term in Φ flipped | **No.** All 20 pass; Φ stays positive and in fact grows (F5(c)) |
| S2: root a multiplied by 1.01 | Yes: 8 failures ("ν formulas agree", "mass 1") |
| S3: sign of the PV main integrand flipped (both branches) | Yes: 4 failures (Φ ≥ 0) |
| S4: narrow bump 40·exp(−((y − 4)/0.12)²) in the p = 1.5 density, violating (H2) | Hypothesis check **missed it** (prints True); caught only incidentally by ν/σ = 1.21 at x = 0.8a (F5(d)) |

## 7. Adversarial pass (Rule A) and literature log

| Attempt | Result |
|---|---|
| Wrong root a | detected by the F(a)-identities; this is what they actually test (F5(a)) |
| Density violating (H2) but with √yσ decreasing | conclusions hold; (H2) can be weakened (F7) |
| Density with √yσ increasing | conclusions still hold in the example; the hypotheses are sufficient, not necessary |
| Behaviour of μ at the soft edge | continuous, ν(a) = σ(a); the Remark is wrong (F3) |
| Non-compact positivity | reduced to compact by inversion (F1(a)) |
| Mellin–Barnes absolute convergence | \|L̃\| ~ \|t\|^{−1/2}: the shift needs more than stated; a direct proof is available (F1(c)) |
| Pole meets an integer or a Γ pole | log terms / 0·∞ limits not covered by the statement (F4) |

**Literature (web only; MathSciNet/zbMATH unavailable).**
- B. Beckermann, A.B.J. Kuijlaars, *Superlinear CG convergence for special right-hand sides*, ETNA 14 (2002) 1–19,
  https://emis.dsd.sztaki.hu/journals/ETNA/vol.14.2002/pp1-19.dir/pp1-19.pdf.
  - **Read through a fetch-tool extraction of the PDF, not line by line by me.**
  - Def. 2.4 (left ansatz), Thm 2.7 (monotonicity criterion), Thm 2.8 (endpoint equations (2.24)–(2.25) with
    ∫dσ/√((β − λ)(α − λ))).
  - Remark: for Q ≡ 0, supp ν_t = supp σ.
  - It cites Kuijlaars, Duke Math. J. 104 (2000) 433–462; Kuijlaars–McLaughlin (manuscript, 2000); Deift–McLaughlin, Mem. AMS 624
    (1998). **Not read.**
- A.B.J. Kuijlaars, *Which eigenvalues are found by the Lanczos method?*, SIAM J. Matrix Anal. Appl. 22 (2000) 306–321,
  https://epubs.siam.org/doi/10.1137/S089547989935527X. **Abstract only** (Q ≡ 0 constrained problem; paywalled).
- D. Coroian, P. Dragnev, A. Legg, R. Orive, *On constrained Riesz minimum energy problems*, arXiv:2608.11987 (Aug 2026),
  https://arxiv.org/abs/2608.11987. **Abstract only**; Riesz kernels, the logarithmic case only as history.
- *Zero distribution of orthogonal polynomials on a q-lattice*, arXiv:1910.12518, https://arxiv.org/abs/1910.12518. **Abstract
  only.** It concerns a constrained problem with nodes accumulating at 0 (radial, circular-symmetric). Its relation to Theorem Q
  is worth checking.
- Rakhmanov 1996 (Sb. Math.), Dragnev–Saff 1997, Kuijlaars–Rakhmanov 1998: **not read** (search hits only).
- Saff–Totik Lemma I.1.8 and Thm II.4.7: **not read in this review**. The numbers are as usually cited and must be checked before
  quoting.

## 8. Log

**Re-derived by hand:**
- (i) in full;
- the balayage density;
- C_y, the arcsine transform, and the boundary values;
- (G), the balayage form and ν < σ;
- both PV integrals;
- φ′ and H;
- the (iv) identity;
- Cor Q.1;
- the M1.2 residues, the MB orientation, W(j) = C(2j, j)4^{−j}(4c)^j and (4c)^q(−L̃(q)) = Wπ cot;
- first-order η and its cross terms;
- the drum quadratic;
- the inversion identity;
- the Liouville replacement for balayage;
- the termwise proof of M1.2.

**Ran** (session venv; review_m1/):
- thq_potential.py (≈ 2 min);
- thq_qp.py, thq_qp_refine.py (≈ 1 min each);
- edge_lin.py (< 1 s);
- weakH2.py;
- inversion.py;
- sab1–sab4.py.

**Not done:**
- reading Saff–Totik, Kuijlaars 2000, Dragnev–Saff or Rakhmanov (Rule C);
- the log-law and p = 0.6 cases of the QP (power p = 1.5 and drum only);
- a rigorous (interval) check of anything. All numerics here are NUMERICAL.
