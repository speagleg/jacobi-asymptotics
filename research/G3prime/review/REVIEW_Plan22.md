# Rule R review: Plan 22 (rhfree/RH99.md: Lemma 9.7*, Lemma 9.9*, Corollary 9.9′; relabelling of Theorem V⁺)

Reviewer: independent Rule R referee (adversarial). Target: branch plan-22-goldston-99, commit f911f6c.

Read:
- AGENTS.md;
- RH99.md (all);
- the RHPRIME.md diff, plus RHPRIME §0–§1 (Setting, (V⁺), Lemma P1) in full;
- the diffs of PROOF.md (row Thm V⁺), CITATIONS.md ((C8) Plan-22 addendum) and LOG.md;
- the plan doc docs/superpowers/plans/2026-10-14-plan-22-goldston-99.md;
- REVIEW_Plan21.md (F2, re-check);
- checks/check_99.py and check_99.out.

Sources checked:
- Goldston, arXiv:math/0412313, read from the PDF images (Read tool), pp. 4–7 and 19–20:
  - (3.3), (3.4) on p. 4;
  - Prop. 1 (3.11)–(3.12) and the proof via (3.13)–(3.14) on pp. 6–7;
  - (9.4)–(9.9) and the full-range remark on pp. 19–20.
- The definition (9.1) of I(X, δ) was checked in the text extraction (p. 18).

Numerics: I re-ran `.venv/bin/python research/G3prime/rhfree/checks/check_99.py`. The output is byte-identical to
`check_99.out`.

## Verdict: ACCEPT WITH FIXES

The mathematics is correct. I checked every step of (0.1)–(0.3), Lemma 9.7*, Lemma 9.9* and Corollary 9.9′ by hand
and found no error that affects a conclusion. The Plancherel normalization, the sign of ε(t), the symmetry argument,
the by-parts identity and the J/I offset all close exactly. Lemma P1 of RHPRIME now goes through with Corollary 9.9′
in place of the sketched full-range (9.9).

The fixes are:
- (i) One stated inequality in Lemma 9.9* has constants that the proof does not deliver (F1; harmless).
- (ii) RHPRIME's body still says the sketched claim "is used here as cited" (F2). Only the tables were relabelled.
- (iii) Framing and bookkeeping items (F3–F8).

No major findings. Medium: F2. Minor: F1, F3–F6. Info: F7–F9.

## Checked and OK

### §0 identities (Review focus 1)
- **(0.1).** Substitute v = xy/u, so v/y = x/u and dv/v = −du/u. The limits v: xe^{−κ} → x become u: ye^κ → y.
  - a_v(y) = min((x/u)^{1/2}, (u/x)^{3/2}) =: a_x(u).
  - x·a_x(u)/u = (u/x)^{1/2} = a_u(x) for u ≤ x, and (x/u)^{3/2} = a_u(x) for u ≥ x.
  - Hence x∫_{xe^{−κ}}^x a_v(y)dv/v = ∫_y^{ye^κ}a_u(x)du. ✔
  - The PDF confirms the subtracted term as "x∫_{xe^{−κ}}^{x} a_v(y) dv/v" (p. 19).
- **(0.2).** y + y/T = y(1 + δ) = ye^κ. Σ_{y<n≤ye^κ}Λ(n)a_n − ∫a_u du = ∫_{(y,ye^κ]}a_u d(ψ(u) − u). ✔
- **(0.3) Mellin.**
  - ∫_0^x(u/x)^{1/2}u^{−it}du = x^{1−it}/(3/2 − it).
  - ∫_x^∞(x/u)^{3/2}u^{−it}du = x^{1−it}/(½ + it).
  - The sum is 2x^{1−it}/((½ + it)(3/2 − it)). ✔
  - Absolute convergence: dψ has no mass on (0, 2), and Σ Λ(n)n^{−3/2} < ∞. ✔

### Lemma 9.7* (Review focus 2)
- **Fubini.** s ∈ [log u − κ/2, log u + κ/2) ⇔ e^{s−κ/2} < u ≤ e^{s+κ/2}. So
  ∫g(s)e^{−its}ds = κ^{−1}∫a_u u^{−it}dE(u)·∫_{−κ/2}^{κ/2}e^{−itv}dv = sinc·P(t).
  - The absolute double integral is ≤ ∫a_u(dψ + du) < ∞. ✔
- **g ∈ L¹ ∩ L².**
  - As s → +∞: |Δ(y)| ≪ y^{−3/2}x^{3/2}(κy + √y log²y) ≪_x y^{−1/2}, so g ≪ e^{−s/2}.
  - As s → −∞: for ye^κ < 2 there are no primes, so Δ(y) = −∫_y^{ye^κ}a_u du ≍ −κy^{3/2}x^{−1/2}, so g ≪ e^{3s/2}.
  - The stated "κy log y" is a harmless overestimate. ✔
- **Plancherel.** With ĝ(t) = ∫g e^{−its}ds, ∫|ĝ|² = 2π∫|g|². Under y = e^{s−κ/2}, ds = dy/y, so
  ∫|G_κ|² = (2π/κ²)L. ✔
- **ε(t).** From (3.11) as printed, P(t) = −2x^{1/2−it}S_x + x^{−1/2}(log(|t| + 2) + O(1)) + O(x^{−2}/(|t| + 2)).
  - The sign is right.
  - |ε| ≪ x^{−1/2}log(|t| + 2) for x ≥ 1, since x^{−2} ≤ x^{−1/2}. ✔
- **Symmetry.** S_x(−t) = Σ_γ x^{iγ}c(t + γ). With γ ↦ −γ (zeros are symmetric under ρ ↦ ρ̄; on RH that is γ ↦ −γ,
  with multiplicity) this is conj S_x(t). φ is even. ✔
- **|S_x| ≪ log(|t| + 2).** Σ_k log(|t| + |k| + 2)/(1 + k²) ≪ log(|t| + 2), via (C1)/(2.18). This uses |x^{iγ}| = 1,
  i.e. RH. ✔
- **∫φ log².** φ ≤ min(1, 4/(κt)²). This gives ≪ κ^{−1}log²(1/κ + 2) ≪ T log²T for T ≥ 2, since κ^{−1} ≤ T + 1. ✔
- **Collect.** ∫|G|² = 4x∫_ℝφ|S|² + O(T log²T) = 8x∫_0^∞φ|S|² + O(T log²T). Then
  L = (κ²/2π)·8x∫_0^∞φ|S|² + O(κ²T log²T) = (4xκ²/π)∫_0^∞φ|S|² + O(log²T/T).
  - This is exactly Goldston's displayed (9.7) (p. 19), coefficient included. ✔
- **Uniformity in x ≥ 1.** There is no hidden x-dependence. The cross term is x^{1/2}·x^{−1/2}, and the |ε|² term
  carries x^{−1} ≤ 1. The only input is that the O-terms of (3.11) are absolute (see F7). ✔

### Lemma 9.9* (Review focus 3)
- **Definitions.** D = ∫_{(y,ye^κ]}dE, since ye^κ − y = δy. I matches (C8) (9.1): "I(x, δ) := ∫_1^X(ψ((1 + δ)x) −
  ψ(x) − δx)²dx". ✔
- **R(y).** Stieltjes by parts with f(u) = a_u − a_y, which is continuous, piecewise C¹ and vanishes at u = y. E is
  right-continuous BV. This gives the stated formula. ✔
- **|R| bound.**
  - |∂_u a_u| ≤ (3/2)a_u/u.
  - a_u/a_y ∈ [e^{−3κ/2}, e^{κ/2}] on [y, ye^κ].
  - Both terms are ≤ (3/2)κe^{3κ/2}a_y·max|E|, total 3κe^{3κ/2}a_y·max|E|.
  - max_{[y,2y]}|E| ≪ √y log²(y + 2) + 1, by (3.4) for u ≥ 2 and E = −u on (0, 2). ✔
- **E-integral.**
  - (√y log² + 1)² ≤ 2(y log⁴ + 1).
  - ∫a_y²y^{−1}dy = 1 + 1/3 = 4/3 exactly.
  - ∫_0^x(y/x)log⁴ and ∫_x^∞(x/y)³log⁴ are each ≪ x log⁴(x + 2).
  - So E ≪ κ²x log⁴(x + 2) for x ≥ 2, and κ ≤ log(3/2) keeps e^{3κ} bounded. ✔
- **By-parts identity.**
  - a_y² = y/x on (0, x) and (x/y)³ on (x, ∞). Hence ∫a_y²D²dy/y = J(x)/x + x³∫_x^∞y^{−4}dJ.
  - x³[y^{−4}J]_x^∞ = −J(x)/x, and +4x³∫J y^{−5}.
  - So ∫a_y²D²dy/y = 4x³∫_x^∞J y^{−5}dy exactly.
  - Boundary at ∞: J(y) ≪ δ²y³ + y²log⁴y = o(y⁴). (The text's "J ≪ δ²y³log²y" holds only for y ≫ δ^{−2}log²; F6.) ✔
- **J vs I.**
  - For 0 < y < 1: ye^κ < 1 + δ ≤ 3/2 < 2. So ψ(ye^κ) = ψ(y) = 0 and D = −δy.
  - J(1) = δ²/3, so J = I + δ²/3 on [1, ∞).
  - 4x³·(δ²/3)∫_x^∞y^{−5} = δ²/(3x). ✔ (This uses x ≥ 2 > 1.)
- **Numerics [2].** Agreement is 1.9·10⁻⁵ to 8.1·10⁻⁵, consistent with trapezoid error on 4·10⁵ log-spaced nodes. ✔

### Corollary 9.9′ and Lemma P1 (Review focus 4)
- **Error.** √(ME) ≪ √(xδ log T·κ²x log⁴x) = xδ^{3/2}(log T)^{1/2}log²x, and δ²/x is negligible.
  - Divided by xδ log T, the first term is δ^{1/2}log²x/(log T)^{1/2} ≤ M₀²T^{−1/2}log^{3/2}T → 0.
  - The second is κ²x log⁴x/(xδ log T) ≪ M₀⁴δ log³T → 0. ✔
  - The proof needs x ≤ T^{M₀} only for log x ≪ log T. It does not use x ≥ T at all.
- **Hypothesis supplied in P1.** P1's first steps give M ≤ (1 + 2ε)xδ log T + O(x³δ²log²Y/Y), and the O-term is
  o(xδ log T). So M ≪ xδ log T on [T, T^M]. ✔
- **P1 then closes.**
  - L ≤ M(1 + o(1)).
  - Lemma 9.7* gives R = L + O(log²T/T), and log²T/T = o(xδ log T).
  - So R ≤ (1 + 2ε + o(1))xδ log T. ✔
  - Lemma 9.9* needs x ≥ 2 and T ≥ 2; P1 has x ≥ T. ✔
- **Comparison with Goldston.** The comparison claim holds as an upper bound (with a caveat, F4).
  - κ²x log⁴x ≪ x log⁴x/T² ≤ x log⁴x/T^{3/2}.
  - xT^{−3/2}(log T)^{1/2}log²x ≤ xT^{−3/2}log⁴x once log x ≥ 1.

### Rule C (Review focus 5)
Against the PDF images, the addendum quotes are verbatim up to typesetting:
- Prop. 1 with "For x ≥ 1" and (3.12) (p. 6);
- (3.4) (p. 4);
- (9.5) (p. 19);
- the (9.7) LHS (p. 19).

The RHS of (9.7) given in RH99's Sources list also matches p. 19. ✔

### Numerics vs .out
- [3]: |L − main|/main ∈ [1.67·10⁻⁴, 4.86·10⁻³], and the bound ratio ∈ [4.41·10⁻⁴, 1.35·10⁻²].
- E/(κ²x log⁴x) ≤ 4.60·10⁻⁶.
- The primes go up to 8·10⁶ (sieve size 2Ymax + 2).
- All match RH99's text. The exception is [1] (F5).

## Findings

**F1 (MINOR; RH99 Lemma 9.9* statement and step 4).**
- **Issue.** Cauchy–Schwarz is applied to L = ∫(a_yD + R)² with main term A := ∫a_y²D²dy/y = M + δ²/(3x), not M.
  - It gives |L − A| ≤ 2√(AE) + E, hence |L − M| ≤ 2√(AE) + E + δ²/(3x).
  - Replacing √(AE) by √(ME) costs 2√(δ²E/(3x)) ≤ δ²/(3x) + E.
  - So the proved inequality is |L − M| ≤ 2√(ME) + 2E + 2δ²/(3x), not the stated one with constants 1.
  - The O-form, Corollary 9.9′ and the numerics (which use A) are unaffected.
- **Fix.** State |L − M| ≤ 2√((M + δ²/(3x))E) + E + δ²/(3x), or use the weaker constants above.

**F2 (MEDIUM; RHPRIME.md P1 Inputs, P1 proof, V3, V5; consistency of the relabel).**
- **Issue.** Only the tables and the V3/V5 headings were changed. The body still contains stale text:
  - P1 Inputs: the full-range claim "is stated with a sketch … **It is used here as cited.**"
  - The P1 proof: "With (9.9) (full-range error) and (9.7): R(x, T) ≤ … + O(x(log x)⁴/T^{3/2})".
  - V3: after "superseded" it still says "The full-range error in (9.9) is cited from (C8), where it is stated with a
    sketch."
  - V5: after "DONE" it still says "… must be read from the PDF first. Not attempted."

  A reader of P1 cannot see that the proof now runs through RH99.
- **Fix.**
  - In P1 Inputs, replace the (9.7)/(9.9) bullets with: Lemma 9.7* (RH99) and Corollary 9.9′ (RH99). Keep the
    Goldston quotes as context, marked "superseded as an input".
  - In the proof, write "By Corollary 9.9′ (hypothesis M ≪ xδ log T supplied by the two previous bullets) and
    Lemma 9.7*: R ≤ (1 + 2ε)xδ log T + O(xδ^{3/2}(log T)^{1/2}log²x + κ²x log⁴x) + O(log²T/T)".
  - Strike or past-tense the stale V3/V5 sentences.

**F3 (MINOR; RH99 §3, last paragraph; framing).**
- **Issue.** "It no longer depends on any statement that is only sketched in (C8)" is accurate in the sense that
  matters: (C8) calls (3.11) a Proposition and gives a Proof. But that proof is itself short and cites two things:
  - Landau's formula (3.13), cited to "Landau's 1909 Handbuch [28]", which has not been read;
  - the estimate ζ′/ζ(−½ + it) = −log(|t| + 2) + O(1), described as "follows easily from the functional equation".

  Likewise, (3.4) is derived in (C8) from the truncated formula (3.3), which is quoted without proof (von Koch).
  These are classical results, and cite-as-stated is acceptable under the citation gate, since the exact hypotheses
  ("Assume the Riemann Hypothesis. For x ≥ 1") are quoted from a read source. The text should still say so precisely.
- **Fix.** Reword as: "It no longer depends on any step that (C8) itself presents only as a sketch. It depends on
  (C8) Proposition 1 (proved in (C8) §3 from Landau's formula (3.13) [28, not read] and a functional-equation
  estimate) and on (3.4) (von Koch; derived in (C8) from (3.3)). Both are cited as stated."

**F4 (MINOR; RH99 Corollary 9.9′, comparison bullet).**
- **Issue.** "It is the same order as Goldston's stated O(x(log x)⁴/T^{3/2})" has two problems:
  - The bound is smaller by a factor ≍ log^{3/2}x/(log T)^{1/2}, so "same order" is loose.
  - It holds only under the extra hypothesis M ≪ xδ log T, which Goldston's remark does not assume.

  So it is not literally "(C8)'s full-range claim". Also, (log T)^{1/2} ≤ log²x needs log x ≥ (log T)^{1/4}. That holds
  for x ≥ T ≥ e, not at x = T = 2.
- **Fix.** "Under M ≪ xδ log T this is at most Goldston's O(x(log x)⁴/T^{3/2}) for x ≥ T ≥ 3. Goldston states his
  error without that hypothesis; we prove only the conditional form, which is all P1 needs."
- **Optional.** For P1 only an upper bound is needed. √L ≤ √(M + δ²/(3x)) + √E holds with no hypothesis on M.

**F5 (MINOR; RH99 (0.3) NUMERICAL line).**
- **Issue.** "to 3·10⁻¹³" holds only for t ∈ {0, 1.7}. At t = 25 the .out gives 7.3·10⁻⁹ (flagged there as loose
  oscillatory quadrature).
- **Fix.** Write "to 3·10⁻¹³ (t ≤ 1.7) and 7·10⁻⁹ (t = 25)".

**F6 (MINOR; RH99 §2 step 3, and notation).**
- **Issue 1.** "J(y) ≪ δ²y³log²y" is not a valid bound for small y relative to δ. The correct statement is
  J(y) ≪ δ²y³ + y²log⁴y. The conclusion y^{−4}J → 0 is unaffected.
- **Issue 2.** The letter E denotes both ψ(u) − u and the error integral ∫R²dy/y.
- **Fix.** Correct the J bound, and rename the integral (e.g. 𝓔).

**F7 (INFO; Lemma 9.7* uniformity).**
- **Issue.** Uniformity in x ≥ 1 needs the O-terms of (3.11) to be absolute in x ≥ 1 and t. (C8) does not say so.
  The proof on p. 7 supports it:
  - the n-series difference is Σ x^{−2n}·2/|(2n + 3/2 + it)(2n − ½ + it)| ≪ x^{−2}/(|t| + 2) uniformly, including
    x = 1;
  - the O(1) comes from ζ′/ζ alone.
- **Fix.** Add one line saying that uniformity is read off from the proof in (C8) §3.

**F8 (MINOR; CITATIONS addendum, RH99 Sources, LOG; Rule C bookkeeping).**
- **Issue.** The pages are given as "pp. 5–7 and 19–20". But (3.4), quoted in the addendum, is on p. 4, and LOG lists
  (3.4) under "pp. 5–7".
- **Fix.** Write "pp. 4–7 and 19–20".

**F9 (INFO; PROOF.md row Thm V⁺).**
- **Issue.** The row keeps "REVIEWED" while its new dependency reads "Rule R pending". This is acceptable as a
  transitional state.
- **Fix.** After the re-check, write "(C8) Prop. 1 + (3.4) via RH99 (REVIEWED, review/REVIEW_Plan22.md)". Tick T6 in
  the plan.

## Recommended labels (after F1–F8; re-check required before REVIEWED)

| Item | Label |
|---|---|
| Lemma 9.7* | PROVED-mod-cite ((C8) Prop. 1 (3.11), (C1)) + mod-input RH — as proposed |
| Lemma 9.9* | PROVED-mod-cite ((C8) (3.4)) + mod-input RH — as proposed (with the F1 constants) |
| Corollary 9.9′ | PROVED-mod-cite ((C8) (3.4)) + mod-input RH, hypothesis M ≪ xδ log T — "the conditional form of (C8)'s full-range claim" (F4) |
| Lemma P1 | PROVED-mod-cite (RH99 Lemma 9.7*, Corollary 9.9′; (C8) Prop. 1, (3.4); (C1)) + mod-input RH, (V⁺) |
| Theorem V⁺ | PROVED-mod-cite ((C8) Prop. 1 and (3.4) via RH99; (C3) (3.5); (C6); (C1)) + mod-input RH, (V⁺), Theorem H; novelty UNCHECKED |

Each row becomes REVIEWED after the re-check. Novelty: none is claimed, which is appropriate.
