# Rule R review, reviewer A (second round): SPEC.md §3.3–§3.5, §3.10–§3.13, labels

Reviewer: independent second reader (Rule R), reviewer **A**, analysis side. Remit:
1. §3.3 Proposition B; §3.4 Neumann; §3.13 Robin formulas; heat-trace coefficients; the Naber sign conflict (§3.9).
2. §3.5 Proposition M and the first-order derivation of −2(2−p)cκn^{−p}.
3. §3.10–3.11: Conjecture S1′, hypothesis H, the index-shift algebra, the Lommel closed form.
4. §3.12: the pole law.
5. §3.13: S1‴, the π cot kernel, the resonance formula.
6. Labels, Rule N and Rule X; adversarial pass.

- **Target:** research/G1/RH/spectral/SPEC.md (2026-10-20 state, 780 lines). §3.1–3.2 were not redone (REVIEW_SPEC_A.md).
- **Context read:** AGENTS.md, VERIFICATION_POLICY.md, E3.md (label table, Lemma E3.7), E2_pgt1.md (Thm E2.1), novelty_SPEC.md §3,
  REVIEW_SPEC_A.md (style), and the check scripts spec_resonance.py, spec_kappa_fit.py, spec_robin.py, spec_common.py.
- I edited no repository file except this report. My scripts, and a coefficient cache redirected away from tmp/, are in
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/reviewSPEC2A/.

## Overall verdict: **ACCEPT WITH FIXES**

Everything I re-derived is correct:
- the closed forms of §3.3/§3.4/§3.13 (Proposition B, Neumann, Robin, heat coefficients);
- the correspondence rule and Proposition B's sign. Naber's eq. (74) has the wrong sign; derivation below;
- Proposition M and the first-order κ computation;
- the index-shift algebra (d₁, d₂, f(δ));
- the Lommel closed form, including the even/odd contraction and c(2) = π²/16;
- W(1/p) = 1;
- the resonance formula.

Two findings are MAJOR. Both are fixable in the text, but they change what the conjectures claim:
- **F1 (sign of the pole law).** The displayed law −p·R·W(q)·π cot(πq)·n^{−1−pq} has the wrong sign for the R it defines (the
  residue of w ↦ Z(−w), quoted as R = −mγ/p). The §3.12 table, the Mellin–Barnes integral that §3.12 itself writes down, the
  divergence cancellation at resonance (§3.13) and the κ data of §3.5 all agree with **+p·R·W(q)·π cot(πq)**. The tabulated numbers
  are right; only the boxed formula and the "calibrated once" remark are wrong.
- **F2 (subleading pole terms are not killed by cot).** The exact Lommel formula contradicts S1′ at n⁻³ (p = 2). For μ ≠ ±½ the
  Bessel-zero zeta value Z(−1) is nonzero. I derived it and confirmed it numerically: Z_E(−1) = −(4μ²−1)/16. So (II) predicts an
  extra n⁻³ term 2pcZ_λ(−1) = −(4μ²−1)/64, which the exact formula does not have. A pure Hurwitz lattice with the same δ (my new
  run) does show the additive ε₁ at n⁻³, to 10⁻⁷. So the McMahon index correction contributes at n⁻³, one order below its cot-killed
  leading term n⁻². This removes the "predicted exactly" status of the bouncer's ε₃ (also at n⁻³). It also limits the "pure index
  shift to all orders" readings of §3.12.

A positive finding (F3): with the corrected sign, the pole law reproduces the κ-shift law of §3.5 **exactly, for every p**. This
is an algebraic identity, below. I confirmed it out of sample at p = 1.5 (a new run): L = −0.5662723 against −0.5662723, half-range
1.3·10⁻⁶. So the "outside S1" deformation of §3.5 is inside S1″/S1‴.

| Item | Verdict | Findings |
|---|---|---|
| 1. Prop. B, Neumann, Robin, heat coefficients, Naber sign | ACCEPT WITH FIXES (all values re-derived; minor proof gaps) | F9, F10 |
| 2. Prop. M, first-order κ derivation | ACCEPT (re-derived) | F3 (text), F13 |
| 3. S1′ algebra, H, f(δ), Lommel | algebra ACCEPT; S1′ scope ACCEPT WITH FIXES | F2, F7, F12 |
| 4. Pole law (§3.12) | ACCEPT WITH FIXES | F1, F3, F8, F11 |
| 5. §3.13 S1‴, kernel, resonance | ACCEPT WITH FIXES | F4, F5, F6 |
| 6. Labels, Rule N/X | ACCEPT WITH FIXES | F3, F6, F8, F14 |

## 1. Proposition B, Neumann, Robin, heat trace (§3.3, §3.4, §3.13)

**Correspondence and sign.** Large z: 1/(z + E) = Σ_j(−1)^jE^jz^{−j−1}. So, formally, Σ_k1/(z + E_k) has the coefficient
(−1)^jZ_E(−j) at z^{−j−1}, i.e. Z_E(−j) = (−1)^j[z^{−j−1}](F′/F). I re-derived the Mellin step:
- ∫_0^∞z^{1−w}(z+E)^{−2}dz = E^{−w}Γ(w)Γ(2−w) and Γ(w)Γ(2−w) = (1−w)π/sin πw, so the prefactor sin πw/(π(1−w)) is right;
- the strip 3/2 < Re w < 2 is right (R₂ ~ ½z^{−1/2} at ∞; R₂ is bounded at 0 since Ai(0) ≠ 0);
- a term rz^{−j−2} of R₂, integrated over [1, ∞), gives r/(w + j), and sin πw ≈ (−1)^jπ(w + j). With r = (j+1)A this returns (−1)^jA.

Control on the lattice: −ψ(z+1) gives Z(0) = −½, Z(−1) = −1/12 and Z(−3) = +1/120, the values ζ(0), ζ(−1), ζ(−3). The rule is right.

**Values** (propB.py: an exact Riccati recursion for w = Ai′/Ai in x = z^{1/2}, independent of spec_bouncer_closed.py):

| | SPEC | mine |
|---|---|---|
| Dirichlet Z_E(0), (−3), (−6), (−9) | −1/4, 15/64, −1695/1024, 59025/2048 | same; all others 0 |
| Neumann (z·Ai/Ai′ = Ai″/Ai′) Z_E(0), (−3), (−6), (−9) | 1/4, −21/64, 2121/1024, −136479/4096 | same; all others 0 |
| Robin F = Ai′ − hAi, F′/F = (z − hw)/(w − h) | 1/4, −h²/2, h(h³+1)/2, −(32h⁶+48h³+21)/64 | same; also Z_E(−4) = h²(h⁶+2h³+2)/2 |
| heat β₁, β₂, β₃ | 1/(6√π), −5/128, 25/(1512√π) | same (c_{3/2} = 5/(24√π), bulk 1/(24√π); c_{9/2} = 221/(12096√π), bulk 1/(288√π)); leading c_{−3/2} = (4π)^{−1/2} |

The Robin condition is right: ψ = Ai(x − E) gives Ai′(−E) = hAi(−E). For h > 0 there are no E ≤ 0 roots, since Ai′/Ai < 0 on
[0, ∞).

**Naber sign (§3.9).** Use Naber's own convention (eq. (52) as relayed): Ai′/Ai = √x(Σ(−1)^nb_nx^{−3n/2} − 1). My series gives
b₁ = 1/4, b₂ = 5/32, b₃ = 15/64, matching his eq. (53). So [z⁻⁴]Ai′/Ai = −b₃, and the rule gives Z(−3) = (−1)³(−b₃) = **+b₃ = +15/64**.
Proposition B is right, and eq. (74) "f(−3) = −b₃" has a sign slip.

An independent check, heat.py, uses neither the Riccati series nor regularised sums:
- Θ(t) is computed directly from the zeros (30 exact plus 3970 from DLMF 9.9.18);
- [Θ − bulk + ¼ − β₁t^{3/2} − β₃t^{9/2}]/t³ = −0.039123, −0.039332, −0.039775 at t = 0.3, 0.5, 0.7;
- this tends to −5/128 = −0.0390625 = −Z_E(−3)/6. Naber's sign would give +0.039.

(Naber has not been read under Rule C. This settles the mathematics, not what the paper says.)

**Proof of Prop. B: remaining gaps** (F9). (i) Differentiating the asymptotic expansion, and the remainder bound used in the
continuation (DLMF §9.7(iv), or the sector-analyticity argument), must be stated. (ii) Hadamard needs order 3/2 < 2 with genus 1.
The label PROVED-mod-cite pending Rule C is appropriate.

**Pole locations from the same expansions (upgrade, F9).** The non-integer powers of F′/F are the poles of Z_E:
z^{−a−1} ↔ heat t^a ↔ a pole of Z_E(s) at s = −a, i.e. q = a.
- Dirichlet: z^{1/2}, z^{−5/2}, z^{−11/2}, …, so q ∈ {3/2, 9/2, …}.
- Robin, exactly and to all orders in h (robinpoles.py): z^{−3/2}, z^{−5/2}, … with nonzero coefficients, so q ∈ {½, 3/2, 5/2, …}.
- Bessel (bessel.py, the Hankel expansion of I_μ′/I_μ): z^{−k−1/2}, so q ∈ {½, 3/2, …}.

So "every pole sits at a half-integer q" is a consequence of the same expansions as Prop. B. It is not a WKB parity heuristic.
I also checked the WKB parity argument to all orders: T(t) is even in t^{−1}, McMahon is odd in 1/β, and for Robin the condition is
odd in (hx^{−1/2}, δ). Both routes agree.

## 2. Proposition M and the κ derivation (§3.5)

- **Heine.** y ↦ y/(1+κy) maps the old nodes to the new ones, and the masses become λ^{−s/p}(1+κy)^{−s/p}. In Π_{i<j}, each index
  occurs m−1 times, so D_m(σ_κ) = D_m((1+κy)^{−2(m−1)}σ′). Correct.
- **Hellmann–Feynman.** ∂_Nlog D_m(μ_N) = E_{OPE}[Σ_i −2log(1+κy_i)] = −2∫log(1+κy)K_{m−1}(y,y)dμ_N. Correct (one-point density
  K(y,y)dμ_N).
- **Second difference.** With G(m) = (m−1)T(m), Δ²G(n) = nα_n − (n−2)α_{n−1} exactly: the T(n) terms cancel. With α_j ≈ 2cj^{−p},
  this is 2c(2−p)n^{−p}. So Δlog b_n = −2(2−p)cκn^{−p}, and Δy_n equals it to this order. Correct.
- **Neglected terms** (F13). The O(κ²y²) term gives Tr J² ~ mn^{−2p}, i.e. κ²n^{−2p} after Δ². The N-dependence enters through the
  covariance of Σy_i, which is O(b_m²) ~ m^{−2p} per unit tilt. That gives κ²m^{2−2p}, so κ²n^{−2p} after Δ². Both are as stated.
  For p < 1 the tilt (1+κy)^{−2N} is not small in absolute terms (2Nκy ~ κn^{1−p} on the band). It is small per particle (relative
  n^{−p}), which is the sense the estimate needs. Worth one sentence.

## 3. S1′, H and Lommel (§3.10–3.11)

**Index-shift algebra.** Re-expanding (1+δ/n)^{−p}[1 + d₁⁰/(n+δ) + d₂⁰/(n+δ)²]:
- d₁ = d₁⁰ − pδ;
- d₂ = d₂⁰ + p(p+1)δ²/2 − (p+1)δd₁⁰. Correct.

f(δ): under H, (1+δ/n)^{−p}·ε₁(a)(n+δ)^{−1−p} contributes −(1+2p)δε₁(a)n^{−2−p}, and the lattice n^{−2−p} term contributes f₀(a). This
gives f(δ) = ε₁(a)[f(0)/ε₁(1) − (1+2p)δ], *provided* the lattice n^{−2−p} coefficient f(0) is ζ(−p) times a (p, s)-function. H
assumes this implicitly (F12).

**Lommel.** From xP_n = P_{n+1} + β_n²P_{n−1}, β_n² = 1/(4(n+ν−1)(n+ν)), the measure is symmetric with masses 1/j²_{ν−1,k} at
±1/j_{ν−1,k}. This is the Mittag-Leffler expansion J_ν(1/x)/J_{ν−1}(1/x) = Σ_k j_k^{−2}[(x − 1/j_k)^{−1} + (x + 1/j_k)^{−1}].
- Writing P_{2n}(x) = P̃_n(x²) gives the contracted recurrence, with off-diagonal B_n² = β²_{2n−1}β²_{2n}. So b_n^{(y)} = β_{2n−1}β_{2n},
  on y = 1/j² with masses 2/j². This is σ_{2,2} up to the scaling y ↦ π²y, with nodes π²/j² = 1/λ and masses ∝ λ^{−1}.
- With μ = ν − 1: β_{2n−1}β_{2n} = 1/(4(2n+μ)√((2n+μ)²−1)).
- c(2) = ¼(π/(2I(2)))² with I(2) = 1, so c(2) = π²/16, and n²b_n/c = 4n²/((2n+μ)√((2n+μ)²−1)).
- The shift identity with δ = μ/2 − ¼ is exact. It matches δ = −Z(0) − ½, since Z(0) = ζ(0, μ/2+¾) = −μ/2 − ¼.
- d₁ = −μ, and d₂ = 5/16 + 3δ² + 3δ/2 = 3μ²/4 + 1/8, as in §3.9.

**F2 (MAJOR): the n⁻³ order at p = 2.**
- **Bessel-zero zeta values.** I derived Z_E(−1) = −(4μ²−1)/16 for E = j²_{μ,k} from the Hankel expansion: F = z^{−μ/2}I_μ(√z) is
  genus 0, so F′/F = Σ1/(z + j²) exactly (bessel.py). Numerical check (besselZ.py; exact low zeros plus Hurwitz-regularised McMahon
  series): 0.0625000000010, −0.49999999999932 and −0.18750000000085 at μ = 0, 1.5, 1, against 1/16, −1/2 and −3/16.
- **What S1′ predicts.** At p = 2 the zeta-layer term ε₁n^{−1−p} sits at n⁻³, an integer order. With additive merging (as at
  p = 1/j), S1′ predicts d₃ = d₃^{shift} + 2pcZ_λ(−1) = d₃^{shift} − (4μ²−1)/64.
- **What the exact formula gives.** d₃ = d₃^{shift}. At μ = 0 the formula is n²b_n/c = (1 − 1/(4n²))^{−1/2}, whose n⁻³ coefficient
  is 0, against the predicted +1/64. At μ = 1.5 (a case SPEC checked against Bessel measures) the predicted extra term is −1/8.
- **Control** (new run, hur2.py). The pure Hurwitz lattice λ = (k − ¼)², p = s = 2, has the same δ as Bessel μ = 0, and the p = 2
  lattice is exact (Lommel μ = ½). After subtracting the exact shift (n/(n+δ))²G(n+δ), the residual's n⁻³ coefficient is 0.0385532
  (fits n ≥ 100/200/400 with 2–4 terms agree to 10⁻⁶). This equals 2pcζ(−2, ¾) = π²/256 = 0.0385531. So **H with additive merging
  holds for Hurwitz lattices at p = 2**, a new datum.
- **Reading.** The difference between Bessel μ = 0 and Hurwitz a = ¾ is the McMahon correction j/π = K − (4μ²−1)/(8π²K) + …,
  i.e. m = 1, q = ½. Its leading pole term n^{−1−pq} = n⁻² is killed by cot(π/2) = 0. Its next term, at n^{−2−pq} = n⁻³, is not:
  it equals (4μ²−1)/64 and cancels ε₁ exactly. S1‴ (§3.13), which is linear in Z, predicts the Bessel-minus-Hurwitz n⁻³ difference
  as 2pcΔZ(−1) = 1/64 − π²/256 = −0.0229. The truth is −π²/256 = −0.0386.
- **Consequences:**
  - (a) §3.3's "ε₃ is predicted exactly" for the bouncer is unsupported. Its WKB correction (q = 3/2) has its subleading term at
    n^{−2−1} = n⁻³, exactly where ε₃ sits.
  - (b) The §3.12 bullets "the integer layer is a pure index shift" (bouncer) and "consistent with the Lommel formula being an exact
    index shift to all orders" (Bessel) hold only at the leading power of each pole. For Bessel, "exact shift to all orders" is
    true, but by cancellation against (II), not by absence of pole terms.
  - (c) For Robin, the q = ½ correction hk^{−1/3} has its subleading term at n^{−7/3} = n^{−1−2p}, where ε₂ sits. ε₂ was not tested,
    but any future test must account for this.
  - (d) The §3.10 bouncer row "the WKB corrections enter only at n⁻³" is consistent with this, but §3.12 then calls the bouncer
    integer layer a pure shift. The two are in tension.
- **Required fix.**
  - State S1′/S1″ only through orders below n^{−2−pq} for every pole q of Z − Z_lattice, including half-integer q.
  - Record the Bessel n⁻³ cancellation as a datum (μ-family, exact), and the Hurwitz p = 2 additive result as a datum.
  - Withdraw "predicted exactly" for the bouncer ε₃, and for the (still unmeasured) Robin ε₂.
  - Add "the integer layer beyond Z(0)", i.e. the subleading pole terms, to "Open".

## 4. The pole law (§3.12)

**W(q).** C(2q, q) = Γ(2q+1)/Γ(q+1)² = 4^qΓ(q+½)/(√πΓ(q+1)), by duplication. W(1/p) = (4c)^{1/p}Γ(1/p+½)/(√πΓ(1/p+1)) =
(π/(2I))·(2I/π) = 1. This follows from the definition of c alone, with no duplication step (F11). I also get
**W(−1/p) = p·tan(π/p)/π**, from the reflection formulas; checked numerically to 10⁻³⁰ (pole.py, checks2.py).

**Residue.** Z(s) = Σ(k + γk^{−m})^{−ps} = ζ(ps) − psγζ(ps+m+1) + O(γ²). So Z(−w) = ζ(−pw) + pwγζ(m+1−pw). Its w-residue at
q = m/p is pq·γ·(−1/p) = **−mγ/p**, as stated. The s-residue of Z(s) at s = −q is +mγ/p; this is §3.11(b)'s "residue γ/p" for m = 1.

**F1 (MAJOR): sign.** With R = −mγ/p, the displayed −p·R·W·π cot = +mγW(q)π cot(πq). The §3.12 "Test" sentence and the table use
−mγW(q)π cot(πq). checks2.py recomputes all seven rows: the table equals +p·R·W·π cot, with the opposite sign to the boxed formula.
Four independent arguments fix the sign without any calibration:
1. **The Mellin–Barnes integral §3.12 writes down.** Closing −(1/2πi)∫_↑ to the right gives +ΣRes. The integer residues are
   +W(j)Z(−j)n^{−jp}, so a pole of Z(−w) at q contributes +R·W(q)π cot(πq)n^{−pq}, with the same sign.
2. **The S1‴ representation.** The averaged kernel is the Mellin transform of (1−u)^{−1/2}·1_{u<1}. Its transform B(s, ½), at s = −w
   and times (4c)^w, equals −π cot(πw)W(w) identically (reflection formulas). Shifting the contour gives the same +R sign.
3. **Resonance.** The integer term pW(j)·pjγζ(m+1−pj) ≈ +p²jγW/(m−pj) cancels the pole term only with −mγWπ cot (π cot ≈ p/(m−pj)).
   With the boxed sign the divergences would add.
4. **The κ law** (F3) has the observed sign only with +p·R.

Fix: write the law as **+p·R·W(q)·π cot(πq)·n^{−1−pq}, R the residue of w ↦ Z(−w)** (equivalently −p·Res_{s=−q}Z(s)·W·π cot). Replace
"the sign is calibrated once" with "the sign is fixed by the Mellin–Barnes integral", citing arguments 1–4 as checks.

**F3 (positive; required text): the κ law is a pole-law term, exactly.** For λ_k = k^p + κ, Z(−w) = ζ(−pw) + κwζ(p(1−w)) + O(κ²),
with a pole at q = 1 − 1/p and w-residue R = −κq/p. Then
  +p·R·W(q)π cot(πq) = −κq·W(1−1/p)·(−π cot(π/p)),
with W(1−1/p) = 4c·W(−1/p)(p−2)/(2(p−1)) and W(−1/p) = p tan(π/p)/π. This simplifies to **−2(2−p)cκ**, exactly, for every p. It
lands at n^{−1−pq} = n^{−p}.

Evidence:
- §3.5's measured L = −1.2034, −0.6015 and −1.2231.
- My new out-of-sample run at p = 1.5, κ = 1 (kappa15.py, n ≤ 1600, K = 160000; fits of n^pΔy with 3–6 correction terms, n ≥ 100–400)
  gives **L = −0.5662723 (half-range 1.3·10⁻⁶) against −2(2−p)cκ = −0.5662723**.
- The opposite (boxed) sign would give +0.566.

Consequences:
- §3.5's "S1 does not apply … effect of a different order" and the "Lesson" are right for S1, but S1″/S1‴ cover the κ deformation.
  The sentence "Hurwitz shifts … outside this first-order formula" should be balanced by "κ-shifts are inside it".
- Rule X: spec_kappa_fit.py's docstring says the candidate was "identified from p = 0.6, kappa = 1". That row is the fit target,
  not evidence. §3.5 should say so. The p = 1.5 run and the pole-law identity are genuine out-of-sample support.

**Half-integer claims.** Correct, and provable from F′/F (§1 above). One caveat, per F2: cot = 0 kills only the leading power of each
pole term.

**F8 (MINOR): the header "NUMERICAL, to 10⁻⁶" is too strong for the m = ½ rows.** At p = 1.25, the n ≥ 800 fit gives −0.232695
against −0.235183, 1% off; at n ≥ 200 the agreement is 5·10⁻⁶. The p = 0.6, m = 1 row is the calibration/identification point
(Rule X), so mark it as such.

## 5. §3.13: S1‴, kernel, resonance

- **Mellin–Barnes form.** (1−u)^{−a} = (1/2πi)∫Γ(−w)Γ(a+w)/Γ(a)·(−u)^wdw at a = ½, and Γ(w+½)(4c)^w/(√πΓ(w+1)) = W(w). The
  averaging of e^{±iπw} is correct and gives −π cot(πw).
- **F4 (MINOR): the literal statement.** [(1−u)^{−1/2}]_av = (1−u)^{−1/2}1_{u<1}, so S1‴ is (p/n)Σ_{u_m<1}(1−u_m)^{−1/2}, the §4
  sum. Two corrections are needed (literal.py, p = 0.6, lattice):
  - (i) The Weyl pole w = −1/p contributes +p·(−1/p)·W(−1/p)π cot(−π/p) = **+p**, an O(1) constant that is not in y_n. The
    formula must take residues of Z − Z_lattice, i.e. exclude the common Weyl pole. (The κ pole is a *moved* Weyl pole and is
    included.)
  - (ii) The literal truncated sum equals the pole part plus an O(n^{−1/2}) oscillation, set by frac((n^p/4c)^{1/p}): (lit − pole)·√n
    ranges over −0.72 … +0.44 for n ∈ [100, 1602]. This edge term is not seen in y_n for lattices. So "zeta regularisation" must
    be defined as "the Mellin pole part", not as a regularised value of the sum.
- **F5 (MINOR): scope wording.** S1‴ is leading order *per node*. It is not "first order in the perturbation".
  - The Hurwitz d₂ shift contains −(p+1)δd₁⁰, and f(δ) contains −(1+2p)δε₁. Both are linear in δ but one order down, like S2′'s O(1/n)
    remainder R. Neither is produced.
  - Replace "second-order effects of a change of count" (§3.13) and "second order in δ" (§3.12 Reading) with "terms one order in 1/n
    below each per-node contribution". F2 is the same phenomenon for poles.
- **F6 (MINOR): resonance.** The re-derivation from the double-pole residue of π cot(πw)W(w)ΔZ(−w)n^{−pw} at w = j, with
  ζ(1−pε) = −1/(pε) + γ_E, gives exactly p²jγW(j)n^{−jp}log n + n^{−jp}[p²jγγ_EW(j) − pγW(j) − pjγW′(j)]. A contour quadrature agrees
  to 10⁻²⁷ (checks2.py).
  - **Family independence.** The total finite part is independent of the regularisation family. The integrand is jointly analytic
    in (p, m), so the sum of the two merging residues converges to the double-pole residue along any path: varying m, varying p,
    or both.
  - **The split is a convention.** The attribution of −γW(j) "to the prefactor m = p(j+ε)" is conventional. With the w-Laurent
    finite part of ΔZ(−w) at w = j, which is pjγγ_E − γ, the same term sits inside Z_fin.
  - **Z_fin is all orders in γ.** spec_resonance.py uses the **full** ΔZ(−j), all orders in γ, for Z_fin. The first-order value is
    −0.166466; the γ^{≥2} part brings it to −0.180893. The text should say "the full regularised ΔZ(−j)".
  - **Weak test.** The fit discriminates between the two values (diff 7.6·10⁻⁵ against a gap of 1.4·10⁻²), but only for n ≥ 200.
    At n ≥ 400 and n ≥ 800 the log coefficient drifts to 0.1028 and 0.1080, and the constant to −0.190 and −0.249. "Larger windows
    are less stable" should read "later (higher-n) windows". Label the test weak.

## 6. Further findings

**F7 (MINOR): §3.10 text.**
- "the coefficient is the sum d₂ + ε_j = d₂ + pZ(−1)" should be pZ(−j). The script and the data use ε_j(a).
- The Open item "ε_jn^{−1−jp} or ε_j(n+δ)^{−1−jp}" is answered by §3.11(a): shifted.
- "Only Z(0) is needed … higher Weyl corrections appear later" is superseded by §3.11(b)/§3.12: m = 1 corrections enter d₂ through
  cot(π/p).

**F9 (MINOR): Proposition B.** See §1 (remainder and differentiation of the expansion). Optionally replace the WKB parity arguments
in §3.12/§3.13 with the exact F′/F pole lists.

**F10 (INFO).** All Prop. B / Neumann / Robin / heat values were confirmed independently, and the Naber sign was settled (§1).

**F11 (INFO).** W(1/p) = 1 is definitional. The new identity W(−1/p) = p tan(π/p)/π drives F3 and F4(i).

**F12 (INFO).** H's f(δ) prediction assumes f(0) ∝ ζ(−p). State it.

**F13 (INFO).** Prop. M's neglected terms were re-estimated (§2). Add one sentence on the size of the tilt for p < 1.

**F14 (INFO): provenance.**
- spec_robin_summary.out is a verbatim subset of spec_robin.out. Say so; it has no generating script.
- spec_rigid.py has no .out. It is presumably the "difference jitter" row of §2, attributed there to spec_jitter.out/spec_window.out.
  Check the attribution.
- Every other NUMERICAL claim in §3.3–3.13 cites an existing .out.
- The "consistency checks (not inputs)" of §3.12 are not inputs, apart from the p = 0.6, m = 1 row (F8). The bouncer and Bessel
  checks are derived, but see F2 on their scope.

## 7. Adversarial pass (Rule A)

| Attempt | Result |
|---|---|
| Pole law on the κ-shift (a deformation SPEC places outside S1) | exact agreement with sign +pR (F3); new p = 1.5 run confirms to 10⁻⁷ |
| Pole law on the Weyl pole itself | gives a constant +p: must be excluded (F4) |
| Boxed sign vs table vs MB integral vs resonance cancellation | boxed sign inconsistent with the other three (F1) |
| Bessel/Lommel at n⁻³ vs S1′ (II) | contradiction unless subleading pole terms are included (F2); Hurwitz p = 2 control satisfies H |
| Literal per-node sum vs pole part | O(n^{−1/2}) edge oscillation; S1‴ only as a Mellin pole part (F4) |
| S1‴ vs Hurwitz index shift | gives d₁ only; misses the linear-in-δ subleading terms (F5) |
| Robin/bouncer/Bessel poles beyond first order | all at half-integers, to all orders (exact expansions) |
| Naber sign | Prop. B right (rule checked on ζ; direct heat trace) |
| Resonance regularisation dependence | total intrinsic; split conventional (F6) |

## 8. Log

**Re-derived by hand:**
- the correspondence rule and the Mellin step;
- the Riccati structure and the vanishing unless 3 | j;
- the Robin condition;
- Heine/Möbius, Hellmann–Feynman, Δ²G = nα_n − (n−2)α_{n−1}, the neglected-term orders;
- the index-shift expansions, f(δ), the even/odd contraction, the Lommel normalisation, c(2);
- W(1/p), W(−1/p), the κ identity, the residue signs, the MB orientation;
- B(−w, ½)(4c)^w = −π cot(πw)W(w);
- the resonance residue and family independence.

**Ran** (session venv; /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/reviewSPEC2A/):
- propB.py: Dirichlet, Neumann, Robin, heat coefficients;
- robinpoles.py;
- heat.py: Θ(t) from the zeros;
- pole.py, checks2.py: the identities, the pole table, the resonance contour residue;
- bessel.py, besselZ.py: Z_E(−1) for Bessel zeros;
- literal.py;
- kappa15.py: **new run** p = 1.5, s = 2, κ = 1, K = 160000, n ≤ 1600, about 3 min;
- hur2.py: **new run** p = s = 2, λ = (k − ¼)², K = 160000, n ≤ 1600, about 3 min.

The new caches are in cache/ there. The repository's tmp/plan62_cache was only read.

**Not done:**
- re-running the authors' long fits (reviewer B);
- reading Naber, Voros or the DLMF bounds (Rule C);
- the subleading pole-term formula behind F2;
- a Robin ε₂ test.
