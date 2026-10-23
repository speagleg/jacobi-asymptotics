# Rule R review, reviewer B: JZC_M1.md (Theorem Q, Corollary Q.1, Proposition M1.2) and Paper IV §3 (Theorem C)

Reviewer: independent second reader (Rule R), reviewer **B** (2026-10-23, branch plan-e2-d2). I read REVIEW_JZC_M1_A.md only after
my own pass through the memo, and used it to check that its fixes were applied.

- **Targets:** research/G1/RH/spectral/JZC_M1.md (230 lines, status 2026-10-21) and papers/paperIV/sec3.tex (Theorem `thm:Q`,
  Lemma `lem:energy`, Remark `rem:Q`, Corollary `cor:Q1`, Proposition `prop:M12`).
- **Context read:** AGENTS.md; VERIFICATION_POLICY.md; REVIEW_JZC_M1_A.md; research/G1/RH/CITATIONS.md (all 909 lines searched);
  research/G2/CITATIONS.md (entries P, R96, DS97, KVA, Be00, VAVB); research/G2/PROOF.md Lemma EP; papers/paper1/main.tex Lemma
  `lem:positivity`; papers/paperIV/sec8.tex, NOTES.md, refs.bib; JZC_W_plt1.md Prop 2 (the part that uses Theorem Q).
- I edited no repository file except this report. My scripts and outputs are in
  /tmp/claude-0/-home-claude/952b5a15-5d15-5ecb-b1af-4a09f25589a5/scratchpad/reviewB_m1/ (qpB.py, outerB.py, edgeC.py, kyB.py,
  sab/).
- Nothing here concerns RH or any hypothesis on zeros. The log-law density is only a test density.

## Overall verdict: **ACCEPT WITH FIXES**

Theorem Q is true as stated, and I re-derived every step. My independent discretised energy minimisation reproduces the edge
and the density for densities that satisfy (H2) and for densities where (H2) fails but g = √y·σ is decreasing. It also shows
that the hypotheses cannot simply be dropped: for a density with a dip, (Q) has three roots and the true minimiser has two
bands.

Two findings change what the proof should say:

- **B1 (MAJOR for the label, good news): the one external input is already proved in this project.** Paper I Lemma 3.3
  (`lem:positivity`, papers/paper1/main.tex) = G2 PROOF.md Lemma EP (Plan 47, REVIEWED) proves I(τ) ≥ 0, with equality iff τ = 0,
  for *every finite signed Borel measure on ℝ* with τ(ℝ) = 0 and ∬|log|x − y|| d|τ| d|τ| < ∞. Compact support is not assumed.
  So the NOT QUOTED Saff–Totik Lemma I.1.8 and the inversion x ↦ 1/(1 + x) can both be dropped. Theorem Q then becomes
  **PROVED** (with no external citation), once the integrability hypothesis is checked for τ = μ′ − μ. Neither the memo nor
  Paper IV checks it now; it is checked below.
- **B2 (MINOR, a real gap for Y = ∞): the Liouville step in (ii) is incomplete as written.** "→ 0 at ∞" does not control
  G − G̃ near the positive real axis when the support [0, ∞) is unbounded. The step also relies on the Plemelj–Privalov
  theorem, which is NOT QUOTED. A per-point argument avoids both problems, and it also makes the Hölder condition in (H1)
  unnecessary for (ii). Fix text is given below.

The other findings are minor. The soft-edge remark needs a regularity qualifier (B3). F is never said to be continuous (B4).
A claim about sabotage S1 in §4 is inaccurate (B5). Some literature attributions are not quoted (B6). The memo and Paper IV
differ in a few places (§3).

| # | Item | Verdict |
|---|---|---|
| 1 | Thm Q (i): uniqueness and existence of the root | ACCEPT WITH FIXES (B4) |
| 2 | Thm Q (ii): Cauchy transform (G), mass, ν > 0, balayage form, ν < σ | ACCEPT WITH FIXES (B2) |
| 3 | Thm Q (iii): equilibrium on [0, a], strict outer inequality | ACCEPT |
| 4 | Thm Q (iv): minimality and uniqueness | ACCEPT WITH FIXES (B1; label upgrade to PROVED) |
| 5 | Role of (H1)–(H3), the weaker hypothesis (F7), infinite mass at 0, hard edge | ACCEPT (Rule A record added, §2.5) |
| 6 | Soft-edge remark (σ − ν ~ C√(a − x)) | ACCEPT WITH FIXES (B3) |
| 7 | Cor Q.1 (a = 4c) | ACCEPT |
| 8 | Prop M1.2 (soft-edge expansion, root η) | ACCEPT (B7 INFO) |
| 9 | Checks m1_theoremQ, m1_edge (re-run) | ACCEPT; re-runs are byte-identical; B5 |
| 10 | Citations (Rule 4 / Rule C) | ACCEPT WITH FIXES (B1, B2, B6) |
| 11 | Paper IV sec3 Theorem C vs memo | ACCEPT WITH FIXES (§3) |
| 12 | Review A fixes applied | all applied; F3 and F5(c) need a follow-up (B3, B5) |

## 1. Re-derivation (from the write-up alone)

**(i).**
- Monotonicity of F holds as stated. With y = au, aσ(au) = (au·σ(au))/u, which is strictly decreasing in a by (H2), and the
  upper limit Y/a decreases while the integrand is positive.
- F is finite: σ is bounded near Y < ∞ since σ ≤ y₀σ(y₀)/y; ∫_1^∞σ < ∞ from (H3) (∫_1^2σ < ∞ by continuity, and ∫_2^∞σ ≤
  ∫σlog y/log 2).
- **Continuity** (not stated, B4). On [a₀, a₁] ⊂ (0, Y) we have aσ(au) ≤ a₀σ(a₀u), because auσ(au) ≤ a₀uσ(a₀u) by (H2). So
  dominated convergence applies with the integrand of F(a₀) as the dominating function.
- Limits:
  - F(0⁺) = ∞, since F(a) ≥ ∫_a^Yσ and σ ≥ y₀σ(y₀)/y.
  - Y < ∞: F(a) ≤ (sup_{[a,Y]}σ)·√Y·2√(Y − a) → 0.
  - Y = ∞: the split at 2a is right; yσ → 0 because yσ decreases to some L, and L > 0 would contradict ∫^∞σ < ∞.
- Correct.

**(ii).** I checked each part by hand.
- **Sokhotski:** S(x ± i0) = H(x) ∓ iπs(x).
- **The branch on (0, a):** at x + i0, 1 − a/z has real part 1 − a/x < 0 and imaginary part aε/|z|² > 0. So √((z − a)/z) →
  +i√((a − x)/x), and −i√ from below.
- **Jumps:**
  - on (a, Y): √((x − a)/x)·(−2πis) = −2πiσ;
  - on (0, a): 2i√((a − x)/x)·S(x) = −2πiν, since S(x) = −∫s/(y − x) < 0.
- **Endpoints:** both functions are O(|z|^{−1/2}) at 0, bounded at a, and O(log) at Y < ∞.
- **Balayage form:** (z − a)/(z − y) = 1 + (y − a)/(z − y) and s(y)(y − a) = σ(y)√(y(y − a)) give
  G̃ = R(z)^{−1}[F(a) + ∫σR/(z − y)]. With R(x + i0) = i√(x(a − x)), the difference of the two ν forms is
  (F(a) − 1)/(π√(x(a − x))).
- **ν < σ:** ∫_0^∞v^{−1/2}(v + c)^{−1}dv = π/√c. The bound is strict because g is strictly decreasing and continuous. Extending
  ∫_a^Y to ∫_a^∞ only enlarges the bound, so the finite-Y case is covered.
- All correct. The gap is in the identification G = G̃ (B2).

**(iii).**
- φ′ = −Re G(z ± i0) = −√((z − a)/z)·H(z).
- In the split of H, the first integrand (g(y) − g(z))(y − a)^{−1/2}/(z − y) is > 0 on both sides of z, and it is O(y^{−3/2})
  at ∞.
- The PV integrals, with y = a + v² and z = a + c²:
  - Y = ∞: 2·PV∫_0^∞dv/(c² − v²) = 0;
  - Y < ∞: (1/c)log((V + c)/(V − c)) > 0, V = √(Y − a), from 1/(c² − v²) = (1/2c)[1/(c − v) + 1/(c + v)].
- φ(a) = 0 by continuity of U^μ, so φ < 0 on (a, Y]. The sign is the right one for a constrained minimiser, with
  U = ∫log(1/|·|): equality where μ < σ, and U ≤ ℓ where μ = σ.
- Correct.

**(iv).**
- The identity I(μ′) − I(μ) = I(τ) + 2∫(U^μ − ℓ)dτ uses τ(ℝ) = 0 and finiteness of the mutual energy I(μ, μ′) (shown in B1).
- The sign argument on (a, Y] is right: τ = μ′ − σ ≤ 0 there, and U^μ − ℓ < 0.
- U^μ = ℓ holds at *every* point of [0, a], not just quasi-everywhere. The density of μ is ≤ g(a)x^{−1/2} on (0, a) and bounded
  on [a, Y], so U^μ is continuous. No capacity argument is needed.
- No competitor has I(μ′) = −∞: log⁺|x − y| ≤ log(1 + x) + log(1 + y), and (H3) gives the log-moment.
- The inversion identity log(1/|x* − y*|) = log(1/|x − y|) + log(1 + x) + log(1 + y) is correct, but B1 makes it unnecessary.
- **Existence and uniqueness need no external theorem.** μ is explicit and is shown to beat every competitor, and the equality
  case gives uniqueness. So Rakhmanov, Dragnev–Saff and Beckermann–Kuijlaars are *not* inputs; they are cited only in §6
  (novelty) and in Paper IV §8. That matters, because their hypotheses exclude this setting (B6).

**Cor Q.1.** With y = a/t, F(a) = (1/p)a^{−1/p}B(1/p, ½). Then a^{1/p} = √πΓ(1/p + 1)/Γ(1/p + ½) = π/(2I). Correct. My edgeC.py
gives a = 1.717810737111 (p = 0.6) and 2.265089372402 (p = 1.5), equal to m1_theoremQ.out.

**Prop M1.2.**
- **Per-power formula:** u = Aλ, Taylor expansion of (1 − u)^{−1/2} on [0, Aλ₀], then analytic continuation in ρ ∉ −ℕ₀. Correct.
- **L̃(w) = B(−w, ½) = −π cot(πw)Γ(w + ½)/(√πΓ(w + 1)):** by reflection, Γ(−w) = −π/(sin(πw)Γ(w + 1)) and
  Γ(½ − w) = π/(cos(πw)Γ(w + ½)). Correct.
- **The remainder r_K:** on [λ₀, 1/(2A)], expand to order J > −ρ_K. The tail ∫_{1/(2A)}^∞λ^jr_K gives O(A^{−ρ_K−j})·A^j for
  j < −ρ_K. The piece on [1/(2A), 1/A] is O(A^{−ρ_K}). Correct.
- **The A^j coefficient equals C(2j, j)4^{−j}Z_N(−j):** Z_N(s) = Σρ_kc_kλ₀^{ρ_k−s}/(s − ρ_k) + ∫λ^{−s}r_K, evaluated at s = −j.
  Correct.
- **The Weyl term:** (1/p)B(1/p, ½)(4c)^{−1/p}(1 + η)^{−1/p}n = n(1 + η)^{−1/p} by Cor Q.1. Correct.
- B7 (INFO): with the equation divided by n/p, the error in η itself is O(η²). "η = … + O(nη²)" is true but loose; the O(nη²) is
  the error in nη.

## 2. Findings and fix texts

### B1 (MAJOR for the label; removes the only external input). Theorem Q (iv): use Paper I Lemma 3.3 / G2 Lemma EP

Paper I Lemma 3.3 (`lem:positivity`) is quoted in G2 PROOF.md as Lemma EP, which is REVIEWED (Plan 47; review/REVIEW_Plan47.md):

> Let ν be a finite signed Borel measure on ℝ with ν(ℝ) = 0 and ∬|log|x − y|| d|ν|(x) d|ν|(y) < ∞. Then
> −∬log|x − y| dν dν = ∫_0^∞|ν̂(ξ)|²/ξ dξ ≥ 0, with equality iff ν = 0.

This needs no compact support. Its proof (Fubini, a uniform bound on a truncated cosine kernel, Fourier uniqueness) is in Paper I.
So Theorem Q (iv) needs neither Saff–Totik Lemma I.1.8 (NOT QUOTED, and not in any CITATIONS.md) nor the inversion.

**Check of the hypothesis for τ = μ′ − μ** (missing from both the memo and Paper IV, which say only "finite energy"):
- τ is finite: |τ| ≤ μ + μ′, of mass 2.
- It is enough to show ∬|log|x − y|| dα dβ < ∞ for α, β ∈ {μ, μ′}.
- **log⁺ part:** log⁺|x − y| ≤ log(1 + x) + log(1 + y). The log-moments of μ and μ′ are finite: on bounded sets log(1 + x) is
  bounded and both have mass 1; at ∞, μ, μ′ ≤ σ and (H3) applies.
- **log⁻ part with μ:** the density of μ is < g(a)x^{−1/2} on (0, a) (proof of (ii)) and ≤ g(a)a^{−1/2} on [a, Y]. So
  sup_x∫log⁺(1/|x − t|)dμ(t) ≤ g(a)·sup_x∫_{|x−t|<1}log(1/|x − t|)(t^{−1/2} + a^{−1/2})dt < ∞. That bounds the (μ, μ) and
  (μ, μ′) terms.
- **log⁻ part of (μ′, μ′):** I(μ′) < ∞ plus the log⁺ bound.

**Fix text, memo §2 (iv)**, replacing the third bullet:
> **I(μ′ − μ) ≥ 0, with equality iff μ′ = μ.** τ := μ′ − μ is a finite signed measure with τ(ℝ) = 0. It satisfies
> ∬|log|x − y|| d|τ| d|τ| < ∞: the log⁺ part by the log-moments (H3), the log⁻ part because μ has density ≤ g(a)·max(x^{−1/2},
> a^{−1/2}) (so its log⁻-potential is bounded) and I(μ′) < ∞. Paper I Lemma 3.3 (= G2 PROOF.md Lemma EP, REVIEWED) applies.

**Label:** Theorem Q becomes PROVED (no external input); see B2 for (ii). Update the label table, the §5 "Non-compactness"
bullet and the §7 log to match.

**Fix text, Paper IV sec3.tex:**
- Delete Lemma `lem:energy` and the TODO, and the sentence "The proof of optimality uses one fact that we do not prove."
- In (iv), replace the inversion with: "… For $I(\tau)$: $\tau$ is a finite signed measure with $\tau(\R)=0$, and
  $\iint|\log|x-y||\diff|\tau|\diff|\tau|<\infty$ (the positive part of the logarithm by (H3), the negative part because $\mu$
  has density at most $g(a)\max(x^{-1/2},a^{-1/2})$ and $I(\mu')<\infty$). So $I(\tau)\ge0$, with equality only if $\tau=0$,
  by \cite[Lemma~3.3]{PaperI}."
- Update NOTES.md lines 39 and 83 to match.

### B2 (MINOR, real gap when Y = ∞). The identification G = G̃ in (ii)

As written ("both o(1/|z − z₀|) at 0, a, Y and → 0 at ∞, so G − G̃ is entire and vanishes at ∞"), there are two problems:
- For Y = ∞ the support reaches ∞. "→ 0 at ∞" is not uniform near the positive real axis, so Liouville does not apply directly.
- Morera across (a, Y) needs continuous boundary values of the Cauchy transform of σ, i.e. the Plemelj–Privalov theorem for
  Hölder densities. That is a "classical" fact which is NOT QUOTED (Rule C.3), and it is the only reason (H1) needs Hölder in (ii).

The same sentence appears in sec3.tex and in JZC_W_plt1 Prop 2 (κ < 0, Y = ∞). The latter is not my target, but it inherits this.

**Preferred fix (per-point balayage; elementary, and needs no Hölder condition in (ii)).** For fixed y > a put
k_y(z) := (√((z − a)/z) − √((y − a)/y))/(z − y). It is analytic off [0, a], since the singularity at z = y is removable. It is
O(|z|^{−1/2}) at 0, bounded at a, ~ (1 − √((y − a)/y))/z at ∞, and its jump on (0, a) is −2πiρ_y, with
ρ_y(x) := (1/π)√((a − x)/x)/(y − x) > 0. The support [0, a] is compact, so plain Liouville gives k_y = ∫ρ_y(x)dx/(z − x), and
ρ_y has mass 1 − √((y − a)/y). Since σ = s·√((y − a)/y),

  G̃(z) = ∫_a^Y s(y)[√((y − a)/y)/(z − y) + k_y(z)]dy = ∫_a^Y σ(y)dy/(z − y) + ∫_0^a ν(x)dx/(z − x),

by Fubini: everything is positive, |1/(z − x)| ≤ 1/|Im z|, and ∫s(y)(1 − √((y − a)/y))dy ≤ F(a) < ∞. Here
ν(x) = ∫s(y)ρ_y(x)dy is exactly the explicit ν. So G̃ is the Cauchy transform of μ, with total mass
∫_a^Yσ + ∫s(1 − √((y − a)/y)) = ∫s = F(a). The boundary-value statements on (0, a) need only real-analyticity of S there.
Checked numerically (kyB.py): |k_y − C[ρ_y]| ≤ 1.2·10⁻¹⁵ at 12 points (y = 1.31, 2, 50; a = 1.3), and mass to 2·10⁻¹⁶.

**Minimal alternative.** Keep the current argument and replace "→ 0 at ∞" with: "both satisfy |·| ≤ C/|Im z| on ℂ∖ℝ (for G̃,
split into |z| < a/2, a/2 ≤ |z| ≤ 2a and |z| > 2a). An entire f with |f(z)| ≤ C/|Im z| vanishes: for real x₀ and every r,
f(x₀) = (1/2π)∫f(x₀ + re^{iθ})(1 − e^{2iθ})dθ, since (z − x₀)f(z)/r² integrates to 0. As |1 − e^{2iθ}| = 2|sin θ|, this gives
|f(x₀)| ≤ 2C/r → 0, so f = 0 on ℝ and hence everywhere." Plemelj–Privalov must then be quoted in RH/CITATIONS.md
(e.g. Muskhelishvili, *Singular Integral Equations*, §§16–17), or replaced by the per-point argument.

After either fix, Hölder continuity in (H1) is used only in (iii), for φ′ = −Re G pointwise. Review A's F2 already gives the
a.e. alternative there.

### B3 (MINOR). Soft-edge remark (memo §2 Remarks; Paper IV Remark `rem:Q`(b))

"σ − ν vanishes like a constant times √(a − x)" needs more regularity of g at a than (H1) gives. With x = a − η,
π(ν − σ)(x) = √(a − x)x^{−1/2}·(h(a) + o(1)), where

  h(a) = ∫_a^Y(g(y) − g(a))(y − a)^{−3/2}dy − 2g(a)(Y − a)^{−1/2}·[Y < ∞]  (< 0).

The integral diverges when g is only Hölder of order ≤ ½ at a.
- Checked (edgeC.py, 30 digits): C = −h(a)/(π√a) = 0.47126578 (p = 0.6) and 0.12449756 (p = 1.5). The direct ratio
  (σ − ν)/√(a − x) reaches these values to 6·10⁻⁸ at a − x = 10⁻⁷. They agree with review A's measured 0.4713 and 0.1245.
- **Fix text:** "… If σ is Hölder of order > ½ near a (e.g. C¹), σ − ν = C√(a − x)(1 + o(1)) with
  C = −h(a)/(π√a) > 0, h(a) := ∫_a^Y(g(y) − g(a))(y − a)^{−3/2}dy − 2g(a)(Y − a)^{−1/2}[Y < ∞]."
- This is the same h as in JZC_W_plt1 Prop 2(vi), so the memo and that note become consistent.

### B4 (MINOR). Continuity of F in (i)

Both the memo and Paper IV use the intermediate value theorem without saying that F is continuous. Add: "F is continuous on
(0, Y) by dominated convergence (on [a₀, a₁], aσ(au) ≤ a₀σ(a₀u) by (H2))."

### B5 (MINOR). §4 claim about sabotage S1

The memo says "The reviewer's sabotage of the finite-Y PV sign passed the old assertions. The direct potential check now catches
it." I re-ran S1 on a copy (sab/m1_theoremQ_S1.py: the sign of `logpart` in Φ flipped) and got **ALL 28 CHECKS PASSED**. Φ changes
(drum: 0.1029 → 1.422; log: 0.0762 → 1.069) but stays positive. The direct potential check is an *independent* test of the outer
inequality, which is what F5 asked for. It cannot catch an error in the Φ code, because no assertion compares Φ with anything.
- **Fix,** either of:
  - change the sentence to "The direct potential check now tests the outer inequality independently of Φ; a sign error in Φ's
    finite-Y PV term would still pass";
  - or add the assertion Φ(z)·√((z − a)/z)/(z − a) ≈ −dU/dz (finite difference of the direct U) at one z per finite-Y density.

### B6 (MINOR). Citations (Rule 4 / Rule C)

| Source | Where cited | Quoted with hypotheses? | Hypotheses met in Theorem Q's setting? |
|---|---|---|---|
| Saff–Totik Lemma I.1.8 | memo label, (iv); sec3 Lemma `lem:energy` (TODO) | **NOT QUOTED** in any CITATIONS.md (G2 (P) cites it second-hand) | moot after B1 |
| Cegrell–Kolodziej–Levenberg Thm 2.5 (non-compact positivity) | not cited by M1; G2 (P) only | NOT READ | moot after B1 |
| Rakhmanov 1996 Thm 3 | memo §6; Paper IV §8 ("classical") | READ, in **research/G2/CITATIONS.md (R96)**, not RH/CITATIONS.md | **No**: σ on [−1, 1] with continuous potential. Not an input |
| Dragnev–Saff 1997 Thm 2.1, 2.6 | memo §6; Paper IV §8 | READ, G2/CITATIONS.md (DS97) | **No**: Def 1.2 requires a *finite* constraint (σ here has infinite mass at 0). Not an input |
| Beckermann–Kuijlaars 2002 Thms 2.7, 2.8 | memo §6; Paper IV §8 | **NOT QUOTED**: read by review A only through a tool extraction; no CITATIONS.md entry | compact support, external field; not an input |
| Beckermann–Kuijlaars 2001 | Paper IV §8; NOTES.md says "decisive for novelty" | **NOT READ** | — |
| Kuijlaars 2000 (SIAM J. Matrix Anal. Appl.) | memo §6 | abstract only | — |
| Van Assche–Van Baelen (q-lattice) | Paper IV §8 | READ, G2/CITATIONS.md (VAVB) | context only |
| Plemelj–Privalov (Sokhotski for Hölder densities) | implicit in (ii)/(iii) | **NOT QUOTED** | (H1) gives Hölder; see B2 |

No cited theorem is used as a proof input (after B1/B2). The existence and uniqueness of the constrained minimiser come from
(iv) directly.

**Fixes:**
- (a) Point memo §6 and sec8.tex to the G2/CITATIONS.md entries R96, DS97 and VAVB, or copy them into RH/CITATIONS.md.
- (b) Add a sentence to sec8.tex: "these results assume a finite constraint (Dragnev–Saff) or a compact interval
  (Rakhmanov) and are not used in the proof of Theorem C".
- (c) Add a CITATIONS entry for Beckermann–Kuijlaars 2002 Thms 2.7/2.8 from a direct reading, or weaken §8's sentence to
  "according to [BK2002]". POSSIBLY-NEW stays pending BK2001, Kuijlaars 2000 and Dragnev–Saff §4 (memo §6 already says so).

### B7 (INFO). Prop M1.2 remainder notation

See §1: "η = (p/n)[…] + O(nη²)" is correct but loose. Either write "+ O(η²)", or put the O(nη²) on nη. This applies to the memo
and to sec3 (eq:M12b) alike.

## 2.5 Independent numerics and Rule A (my code: qpB.py, outerB.py)

**Method.**
- Piecewise-constant density on cells.
- Exact cell–cell log-kernel integrals: Φ(t) = t²log|t|/2 − 3t²/4, Φ″ = log|t|.
- Box constraint 0 ≤ m_i ≤ ∫_{cell}σ, with an infinite cap on the first cell, where σ is not integrable.
- A primal–dual active-set QP that solves the KKT system exactly; it converges in 4–10 iterations.
- Graded mesh near 0, refined around the formula root. The refinement nodes are deliberately offset, so the root is *not* a
  mesh node.
- None of the code is from the repo or from review A (A used BVLS).
- Theorem Q side: (Q) is scanned for *all* roots on a 400-point grid, and ν comes from formula (ii) by scipy quadrature. The
  H-sign in outerB.py uses Cauchy-weight quadrature.

| density | (H2) | g = √yσ decr. | roots of (Q) | QP structure | QP edge vs a | band density vs ν (cell avg) |
|---|---|---|---|---|---|---|
| log law (repo's, Y = 2.0178) | yes | yes | 1: 0.2097256026 (= m1_theoremQ.out) | band \| saturated | within 1 cell | 6·10⁻⁵–4.5·10⁻⁴ (N = 200) |
| σ = 0.4(1 + 0.3 sin(1.2 log y))/y, Y = 4 | **no** | yes (εk = 0.36 < ½) | 1: 1.6490887885 | band \| saturated | 7.4·10⁻⁴ → 3.7·10⁻⁴ → 1.9·10⁻⁴ (N = 200, 400, 800; O(h)) | at 0.9a: 1.1·10⁻⁴ → 2.9·10⁻⁵ → 7.4·10⁻⁶ (O(h²)) |
| same, k = 2 (εk = 0.6) | no | **no** | 1 | band \| saturated | within 1 cell | ≤ 3·10⁻⁵ |
| same, k = 3 (εk = 0.9) | no | no | 1 | band \| saturated | within 1 cell | ≤ 4·10⁻⁵ |
| ε = 0.45, k = 4 and k = 6 | no | no | 1 (F not monotone) | band \| saturated | within 1 cell | ≤ 8·10⁻⁵; max ν/σ = 0.994, 0.898 |
| **dip**: 0.4/y·(1 − 0.9e^{−(log(y/0.8)/0.1)²}) | no | no | **3**: 0.7063, 0.8346, 1.1217 | **band \| sat \| band \| sat** (sat on [0.698, 0.941] and [1.101, 4]) | none of the roots | 1–6 % off |
| dip depth 0.5 at y = 0.8 | no | no | 1: 1.12166 | band \| **sat island [0.757, 0.865]** \| band \| sat | final edge within 1 cell | 12 % off at the island; ν/σ up to 1.18 |
| dip depth 0.9 at y = 2.5 (inside the saturated region) | no | no | 1 | band \| saturated | within 1 cell | ≤ 5·10⁻⁵ |

**Rule A conclusions.**
- (1) **Theorem Q holds where claimed, and also beyond (H2).** Formula and minimiser agree, with O(h) edge and O(h²) density
  convergence, whenever g is decreasing (this confirms F7 / Remark (a)). It also holds for several densities with g
  non-monotone, so (H2) and F7 are sufficient, not necessary.
- (2) **The hypotheses cannot be dropped.**
  - For the three-root dip, outerB.py shows what fails at each root:
    - at a = 0.7063, ν < σ on the band but H(z) < 0 at z = a + 0.05(Y − a), so (iii) fails;
    - at a = 1.1217, H > 0 on (a, Y) but ν/σ reaches 5.85, so (ii) fails;
    - at a = 0.8346, both fail.
  - So the two uses of monotone g are distinct, as the memo says: g decreasing on (0, a) gives ν < σ, and g decreasing on (a, Y)
    gives H > 0.
  - For the single-root dip, uniqueness of the root does **not** give the theorem: the true minimiser has a saturated island
    inside the band. The memo's Rule A guess was "a gap (a second band)". I found a second *saturated* run, i.e. two bands with
    no void. Suggest "a second band or a saturated island".
- (3) A dip *inside* the saturated region is harmless, as expected: ν depends only on σ|_{(a,Y)} through s, and H > 0 still holds.

**Re-runs** (session venv, `-B`):
- checks/m1_theoremQ.py → **byte-identical** to m1_theoremQ.out (ALL 28 CHECKS PASSED);
- checks/m1_edge.py → **byte-identical** to m1_edge.out (ALL 4 CHECKS PASSED).
- From the .out:
  - the four relative accuracies are ≤ 1·10⁻⁸ (8 printed digits), 1.0·10⁻⁶, 1.3·10⁻⁷ and 1.4·10⁻⁶;
  - the memo's "1·10⁻⁹" for (1.5, ½) cannot be read off the printed digits; review A measured 2·10⁻¹⁴ independently. INFO:
    say "≤ 10⁻⁸ (printed digits)".

## 3. Paper IV sec3.tex (Theorem C) vs JZC_M1.md

| # | Point | Memo | sec3.tex | Action |
|---|---|---|---|---|
| D1 | Energy positivity | Saff–Totik I.1.8 via inversion, NOT QUOTED | Lemma `lem:energy` "we do not prove", compact support + ∬\|log\| hypothesis, TODO | both: use \cite[Lemma 3.3]{PaperI} (B1) |
| D2 | Hypothesis check for τ | "finite energy" asserted | only the log-moment is checked ("finite by (H3)") | add the B1 check |
| D3 | Statement (iv) | "μ is the constrained equilibrium measure" | "the unique solution … among measures of finite energy" | memo should match the paper; "finite energy" can be dropped (no competitor has I = −∞) |
| D4 | ℓ in (iii) | used without introduction | "There is a constant ℓ" | memo: add "for a constant ℓ" |
| D5 | G = G̃ | Liouville, "→ 0 at ∞" | same | B2, both |
| D6 | Continuity of F | missing | missing | B4, both |
| D7 | Edge remark | general | general (Remark (b)) | B3 qualifier, both |
| D8 | (H1)–(H3) | identical | identical | — |
| D9 | Conclusions (i)–(iii) | identical in content (the paper gives ν > 0 "because s > 0", the memo "S(x) < 0"; same) | — | — |
| D10 | Remark (a) / F7 | same weaker hypothesis | same | add the B-numerics note: not necessary, but cannot be dropped (§2.5) |
| D11 | Remark (c) node-language | absent | present | fine (interpretation only) |
| D12 | Checks remark | 28 assertions, direct potential | names the checks, says the ν agreement tests the root | consistent; B5 also affects the memo only |
| D13 | M1.2 hypotheses | "resonant q ∈ ℕ and log laws excluded" | resonance excluded; log laws excluded implicitly by eq:Nexp | fine |
| D14 | M1.2 error term | O(nη²) | O(nη²) | B7 (INFO) |
| D15 | §8 attributions | — | "classical [Rakhmanov, DragnevSaff]"; BK2002, BK2001 | B6 |

No discrepancy in hypotheses or conclusions of the theorem itself. Paper IV's statement is slightly more precise in (iii)–(iv).

## 4. Review A's fixes

| A's finding | Applied? | Comment |
|---|---|---|
| F1(a) inversion | yes | correct, but superseded by B1 |
| F1(b) Liouville instead of balayage | yes | incomplete for Y = ∞ (B2) |
| F1(c) termwise M1.2 | yes | re-derived, correct |
| F2 Hölder | yes | after B2 needed only in (iii) |
| F3 edge remark | yes | needs a regularity qualifier (B3) |
| F4 M1.2 edge cases | yes | both texts |
| F5 checks | yes (direct potential, analytic (H2), fine grid) | the S1 claim is inaccurate (B5) |
| F6, F7, F8, F9, F10 | yes | F9 tolerance 10⁻⁵ is in m1_edge.py; docstrings fixed |

## 5. Consequences for JZC_W_plt1.md (not my target; flagged)

- It uses Theorem Q (i)–(iii) only. These never used the positivity lemma, so B1 does not affect it, and its statement that
  "Theorem Q (i)–(iii) uses no external input" is right.
- For κ > 0 (Y = z_* < ∞) the Liouville step is sound as written.
- For κ < 0 (Y = ∞ with S₋ added), its own "G − G̃ is entire and → 0" has the B2 gap. The per-point k_y argument or the
  |Im z|-bound lemma closes it there too. S₋ lies on the negative axis, where k_y is still analytic off [0, a].

## 6. Labels after fixes

- **Theorem Q:** PROVED (B1, B2 applied); REVIEWED once B1–B4 are in. Until then, PROVED-mod-cite with the input re-pointed to
  Paper I Lemma 3.3.
- **Cor Q.1:** PROVED (inherits Thm Q for the equilibrium identification).
- **Prop M1.2:** PROVED.
- **Checks:** NUMERICAL.
- **Novelty:** POSSIBLY-NEW (unchanged; BK2001 unread).

## 7. Log

**Read:** the files listed at the top.

**Re-derived by hand:**
- (i) with continuity;
- jumps, branches, endpoint orders, the balayage form, ν < σ;
- both PV integrals, the H-split and its sign;
- the (iv) identity and sign, and the inversion identity;
- the B1 integrability check;
- the per-point k_y identity (B2) and the |Im z|-lemma;
- Cor Q.1;
- the M1.2 per-power formula, L̃ by reflection, the remainder split, the Z_N(−j) collection, the Weyl term and the η
  linearisation;
- the soft-edge constant h(a).

**Ran:**
- the repo checks (identical);
- qpB.py on 10 densities (N = 200–800);
- outerB.py;
- edgeC.py;
- kyB.py;
- sabotage S1 copy (passes all 28).

**Not done:**
- reading Saff–Totik, Cegrell–Kolodziej–Levenberg, BK2001/2002, Kuijlaars 2000 or Muskhelishvili;
- a Y = ∞ QP (review A did p = 1.5 with a tail field);
- any interval/ball computation. All numerics here are NUMERICAL.
