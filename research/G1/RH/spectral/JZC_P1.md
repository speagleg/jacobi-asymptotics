# JZC P1: the Paper IV expansion continued to p = 1 (lattices, Hurwitz shifts, polynomial tilts)

Status (2026-10-26): **NOT REVIEWED**. Labels per VERIFICATION_POLICY.md.
- Everything below is NUMERICAL: Arb ball arithmetic data against exact algebra, with no fitted parameter in any prediction.
- The one exception is the Tricomi–Carlitz comparison, which is exact computer algebra given the Carlitz recurrence (KNOWN).
- Novelty: UNCHECKED (no Rule L search).
- No claim about RH. The "zeta times" are Hurwitz values ζ(−j, d) at rational d, or free tilt parameters; no measure built from
  zeros is used.

Branch: p1-continuation (from plan-e2-d2).

Checks (`checks/`, `-B`; caches in `tmp/p1/`; every `.out` prints the sha256 of its scripts):
- `p1_arb.py` → `p1_arb.out`: the data. These are Arb Jacobi coefficients, n ≤ 89 at 4500 bits (6000 at p = 2), with ≥ 2967
  bits left. The script generates three families:
  - pure p = 1 Hurwitz lattices, from exact Hurwitz-zeta moments;
  - time-controlled tilts exp(Σ_{j≤8} τ_j y^j), with τ_j = t_j + 2ζ(−jp, d)/j, so that the Toda times are exactly the prescribed
    t_j;
  - the p = 2 control.
- `p1_continuation.py` → `p1_continuation.out`: all comparisons and controls.

## 1. Question

At p = 1 the zeta exponents 1 + jp are integers, the Weyl pole is an integer, and Theorem N.6 is not available. The
construction of [23] switches between the seam and the negative axis there.

JZC_W §1.6 and §5.2 record two expectations at p = 1:
- generic resonances, with log n terms;
- Toda times to be read as finite parts.

They also record that "the order-k engine m4_rh4 and the natural-form algebra … have no p = 1 specialisation checked". Paper IV
Problem 7.4(c) leaves p = 1 open.

**Question.** Does the natural-form expansion (1.7), with every coefficient continued from p ≠ 1, describe b_n at p = 1?

## 2. Prediction (registered before the comparisons; Rule X)

**Integer layers.** These are the p → 1 values of the closed forms:
- F: f₂, f₄ and f₆, from m4_rh4.f4_closed and f6_closed;
- the diagonal: a₂ and a₄, from Prop T.4.

**Zeta layers.** Every zeta layer is the formal Toda flow of these integer layers. This is Theorem T: Lemma T.1 is exact for every
measure and every exponential tilt, so it holds at p = 1. The flow is computed with the engine FT of shift_common at p = 1, in the
natural index N = n + α/2 − Z(0). For Hurwitz shifts, Theorem 6.1's index transfer is continued to p = 1.

## 3. Result (NUMERICAL)

| test | data | result |
|---|---|---|
| (B) base, all t = 0 | C₁…C₇ of N b_n/c | = f₂, f₄, f₆ at (1, −½); odd terms vanish (|Δ| ≤ 1.3·10⁻²⁶) |
| (B) diagonal | (M/n)A, M = N + ½ | a₂ = 5/48, a₄ = 53/2304; odd terms vanish |
| (T) tilts | 32 datasets: single t_j (j ≤ 6) at ±¼, ±½ (t₁ also ¾, 1); (t₁, t₂) pairs | C_k = FT(p = 1) for k ≤ 7; each |Δ| within 3× its own two-window fit spread (2·10⁻²⁶ for t₁ = 1 … 1.2·10⁻²⁰ for t₆ = −½) |
| (H) Hurwitz lattices | 11 shifts d ∈ [1/10, 21/10] at α = −½; d = 1/5, 3/10 at α = ½, 3/2 | C_k = FT(p = 1), times −2ζ(−j, d)/j; |Δ| ≤ 2·10⁻²⁹ |
| (C) Tricomi–Carlitz | exact b_n | = FT(p = 1) identically in a through N⁻⁶ (times −ζ(−j, a)/j) |
| (P2) p = 2 control | t₂ layer, s = 3 | lead −pW(2); g₂ = 11/4 = A₂(2) |

Further facts, from the same data:
- **No log n terms through N⁻⁷.** A pure-power fit reproduces every dataset to the precision above. For lattices and polynomial
  tilts at p = 1, the resonance expected by JZC_W §5.2 is absent through N⁻⁷. The Weyl pole sits entirely in the integer layer,
  and the times are the plain Hurwitz values, with no finite-part prescription needed.
- **FT at p = 1 reproduces the continued closed forms:**
  - g_j(1, −½) for j ≤ 6, and h₂;
  - the Pochhammer leading coefficients (p+1+S)_{m−1}/(r! p^{m−1}) of Theorem 5.4;
  - for one time, the Catalan numbers 1, 2, 5, as Lagrange inversion of x = n − ε/x gives.
- **New p = 1 values (FT, confirmed by the data; ε-units of (1.7), α = −½):**
  - the ε₂ layer in ε-units is N⁻³[1 + (139/96)N⁻² + (40915/18432)N⁻⁴ + …]. The N⁻⁴ dressing is new, and the Arb data
    confirm it.
  - the ε₁ε₂ layer is N⁻⁵[5 + (1661/96)N⁻² + …], whose lead is the Pochhammer value (5)₁. The ε₁³ layer is
    N⁻⁶[5 + (683/32)N⁻² + …].
  - `p1_continuation.out` prints the full p = 1 layers to N⁻⁷ for ε₂, ε₁ε₂, ε₁³, ε₁²ε₂ and ε₁ε₃.
- **Numerical values with no closed form at hand:**
  - a₆(1, −½) = 0.006085431134259259259259259 = 673/110592 by rational recognition, agreeing to 3·10⁻²⁸. The denominator is
    2¹²·3³, the same 2–3 shape as a₄ = 53/2304.
  - f₈(1, −½) = 0.00072228202113398799190. The candidate 817957/1132462080 (denominator 2²³·3³·5) agrees only to 3·10⁻²⁴,
    which is the fit-noise level of C₈, so it is not claimed.

**Reading.**
- For lattices, Hurwitz shifts and polynomial tilts, p = 1 is not a singular point of the dictionary. Every coefficient through N⁻⁷
  is the continuation of the p ≠ 1 formula.
- What fails at p = 1 is the proof (Theorem N.6 and the seam/negative-axis construction of [23]), not the expansion.
- The genuinely new p = 1 features of real drums are the extra poles of Z. At the perimeter pole the factor W(q)·π cot(πq) is a
  0·∞ limit (SPEC §3.16). The second-order perimeter term β² also lands on n⁻¹. Those are separate from this note.

## 4. Rule X record

The first comparison (same session, before this note) reported "p = 1 defects". For example:
- −(2/3)ε₂ at N⁻⁵;
- a power law (p+1+S)^{m−1} in place of the Pochhammer symbol for cubic terms.

Both were transcription errors in the comparison, not properties of the measures:
1. A_j's numerator: j² multiplies only the p³ term, but j had been factored out of the whole numerator.
2. The Pochhammer subscript of Theorem 5.4: the PDF text extraction dropped it, and it was read as a power.

The closed forms are now taken from repository code (m4_rh4, shift_dressing). Both mistranscriptions are kept as must-fail
controls in `p1_continuation.py`, and they fail.

## 5. Consequences for other notes (suggested, not applied)

- **JZC_W §1.6 and §5.2.** "Resonances (log n terms) are generic" and "Toda times … must be read as finite parts" are not borne out
  for lattices, Hurwitz shifts and polynomial tilts through N⁻⁷. They may still hold for node sets with extra poles of Z (drums).
- **Paper IV, p3_kernel.tex l.142 and p7_weyl.tex l.138** ("at p = 1 the two cotangents coincide / merge").
  - The kernel cot(πwp/2) − cot(πw) equals 1/sin(πw) at p = 1, which is not zero. It vanishes identically at p = 2.
  - What happens at p = 1 is that the poles of cot(πwp/2), at w = 2l, fall on the integers, where ζ(−2l) = 0 removes them.
  - Suggested wording: "at p = 1 the poles of cot(πwp/2) fall on the integers".
- **Paper IV Problem 7.4(c).** The p = 1 case of the expansion is now supported numerically through N⁻⁷. The open part is the
  proof.

## 6. Open

- **A proof at p = 1.** The E_p1 frame has the Γ/Binet band factor, and N.6 would need a p = 1 specialisation. The data say the
  continued N.6 coefficients are right.
- **Pole terms at p = 1** on a node set with a non-Weyl pole whose cot(πq) ≠ 0 (SPEC §3.16 has only the 0·∞ perimeter case).
- **Closed forms** for f₈ and a₆ at general p, to place the printed p = 1 values.
