# Rule R review: Plan E2, reviewer B (algebra and computation), E2_pgt1.md

Reviewer: independent second reader B (Rule R). My scope is the explicit computation behind Theorem E2.1:
- the second-order model data (X₂, Ξ₂);
- the conjugations and branches;
- the series of Lemma E2.4 as they are used;
- the Laurent and residue bookkeeping of Lemma E2.6(c);
- the extraction of d₂;
- the numerical cross-checks;
- the p = 2 and p = 1 remarks;
- the algebra of Cor E2.7.

I did not review the analytic estimates and accept none of them here. These are Lemma E2.3's uniformity and n-dependence,
the small-norm bounds of Prop. E2.5, and the remainder O(n^{−min(3,1+p)}). They belong to reviewer A.

Date 2026-10-20. Targets:
- research/G1/RH/second_order/E2_pgt1.md;
- checks/check_e2_sym.py, check_e2_num.py, check_e2_grid.py and their .out files;
- for the standard, E_pgt1.md, check_e_sym.py, check_e_num.py and REVIEW_Plan65_B.md.

No repository file other than this report was modified. My scratch work is in the session scratchpad `reviewB/`, which is
not committed:

| File | Purpose |
|---|---|
| orig.py | byte copy of check_e2_sym.py |
| dump.py | the same plus one line that pickles the intermediate matrices |
| tamper.py | sabotage tests on the residue bookkeeping, using the pickled matrices |
| trunc3.py, trunc4.py | truncation-order tests |
| pertS.py, pertS3.py, pertA.py, pertA1.py | sensitivity to individual series coefficients |
| sym_parity.py | exact, untruncated proof of meromorphy |
| num_d2.py | independent quadrature route to d₂ |
| misc.py | closed-form identities, p = 2 Lommel, p = 1, my own Ξ₂/X₂ extraction |

## Overall verdict: **ACCEPT WITH FIXES** (computation only)

The value d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12 is what the second-order Riemann–Hilbert data produce. I
confirmed this by three routes that share only the DLMF inputs and the structure of the Δ's from Lemma E2.3:
1. **Re-run of the script.** check_e2_sym.py reproduces check_e2_sym.out exactly and all assertions pass (3 min 55 s).
2. **Line-by-line audit.** The bookkeeping in the script matches Lemma E2.6. All 11 sabotaged bookkeeping variants in tamper.py break the final
   assertion. One further whole-function substitution, R_out for R_in, is equivalent to the script by construction (§2, F4).
3. **Independent numerical route.** There are no series and no Laurent bookkeeping. The ingredients g, φ, φ̃, f and ω are
   built by quadrature, R⁽¹⁾_in comes from Cauchy integrals, and Res F comes from contour integrals. This reproduces d₂ at
   8 values of (p, s) with α ∈ [−0.875, 1.4], to 3·10⁻⁸ … 6·10⁻⁷. The effects of sabotage are at least 3.6·10⁻².

I found no mathematical error. The findings concern three things: wording that overclaims what two checks show (c-independence
and truncation), stale references in the script, and missing provenance (Rule X) for the "conjectured" closed form.

| Item | Verdict (B's scope) | Notes |
|---|---|---|
| Lemma E2.3: X₂, Ξ₂, u₂, v₂, a₂, b₂, prefactors 1/φ̃², 1/(4f) | ACCEPT | re-derived; my own mpmath models with Richardson extrapolation (§1.1) |
| Lemma E2.4 as used (κ, κ₂, f′(0); full series) | ACCEPT | asserted in the script; sensitivity in §3 |
| Lemma E2.6(a) meromorphy | ACCEPT (INFO F5) | proved exactly to all orders (§1.3) |
| Lemma E2.6(b) first-order reproduction | ACCEPT | B_r, A_r, A₀ asserted; I also checked C₀ against E.5 (difference 0) |
| Lemma E2.6(c) residue bookkeeping | ACCEPT | §1.2 and the sabotage tests of §2 |
| Lemma E2.6(d) extraction, d₁, d₂ | ACCEPT WITH FIXES (F1, F2) | value confirmed; the c-independence claim is overstated |
| Truncation orders | ACCEPT WITH FIXES (F3) | sufficient (trunc4 passes, trunc3 fails); "shown in the script" is not accurate |
| Thm E2.1 closed form; p = 2 reduction | ACCEPT | §4 |
| Cor E2.7 algebra (δ′, γ) | ACCEPT | re-derived by hand (§4) |
| Rem E2.8, E2.10, E2.11 numbers | ACCEPT (INFO F7) | §4 |
| check_e2_grid.out | ACCEPT WITH FIXES (F1, Rule X) | byte-identical re-run; numbers recomputed exactly |
| check_e2_num.out | ACCEPT (INFO F8) | independently re-derived |

## 1. Audit of check_e2_sym.py against E2_pgt1.md

### 1.1 Model inputs (lines 60–66, 111–117)

**DLMF coefficients.**
- u₂ = 5·7·9·11/(216²·2!) = 385/10368 and v₂ = (13/(−11))u₂ = −455/10368, from DLMF 9.7.2 at k = 2.
- a₂ = (4α²−1)(4α²−9)/128 (10.17.1) and b₂ = (4α²−1)(4α²+15)/128 (10.17.8).

**Ξ₂ from the text's recipe.** I recomputed Ξ₂ = M⁻¹(M∘C₂) with C₂ = [[a₂, a₂], [b₂, b₂]]:
- M∘C₂ = (1/√2)[[a₂, ia₂], [ib₂, b₂]];
- M⁻¹(M∘C₂) = ½[[a₂+b₂, i(a₂−b₂)], [−i(a₂−b₂), a₂+b₂]], which is the script's Xi2.

**X₂.** The X₂ pattern [[(u₂+v₂)/2, i(u₂−v₂)/2], [−i(u₂−v₂)/2, (u₂+v₂)/2]] is the k = 2 analogue of X₁. The sign of the second
term changes because of the (−1)^k of y₀ in 9.7.5–6.

**Trace identities (asserted in the script).**
- tr X₂ = −35/5184 = −det X₁.
- a₂ + b₂ = a₁b₁ = (4α²−1)(4α²+3)/64.

**Independent numerics (misc.py (d)).** I wrote my own I_α/K_α model with K_α′ = −(K_{α−1} + K_{α+1})/2 and Richardson
extrapolation in 1/w over w ≈ 400, 800, 1600. Then |w²(G − I − Ξ₁/w) − Ξ₂| was:

| α | Richardson value | with −Ξ₂ | with the transposed sign pattern |
|---|---|---|---|
| 0.3 | 6.9·10⁻⁸ | 0.154 | 0.12 |
| 1.7 | 2.2·10⁻⁷ | 4.4 | 2.0 |
| −0.6 | 4.0·10⁻⁸ | 0.113 | 0.083 |

For Airy (sectors I and IV, |ζ| = 400), the distance to X₂ is 8.0·10⁻⁶ against 0.088 for −X₂. This decays like 1/ξ, as in
check_e2_num.out [1].

**Prefactors.**
- Soft edge. ξ = −nφ̃ gives X₂/ξ² = X₂/(n²φ̃²). In the code, φ̃ = −κu³·phit_over and conj_soft returns u·P(…)P⁻¹. So
  Δ₂^r = conj_soft(X₂)·inv2/(κ²u⁷), which is the script's D2r_u7/u⁷. The sign is (−1)², with no leftover minus.
- Hard edge. w = 2nf^{1/2} gives Ξ₂/w² = Ξ₂/(4n²f), so D20 = conj_hard(σ₃Ξ₂σ₃)/(4 fh²). The first-order normalisation
  Q₀/16 = 8σ₃Ξ₁σ₃ is asserted (line 117).

### 1.2 Branches and bookkeeping

**Branches.** All branches are those of check_e_sym.py (Plan 65, REVIEWED):
- 𝔞_∞² = u/z^{1/2};
- (−ω)^{1/2} = (2√c/(z^{1/2}+u))^{1+α} (h2 = (−ω), ih2 = (−ω)⁻¹);
- on z = −v²: 𝔞_∞² = √(4c+v²)/v > 0, ρ = ((v + √(4c+v²))/(2√c))^{1+α} = (Υ̂/4c)^{(1+α)/2}, and f^{1/2} = v·(positive
  series)/(√c(p+2)) > 0.

The only change from Plan 65 is that f^{1/2} is now built from the full series of Lemma E2.4(i) rather than from (f₁, F₂).
The A₀ assertion (line 136) pins its normalisation, including the √((p+2)²) issue mentioned in §10.

**Residue at 4c.** For clockwise circles, the O(n⁻²) jump relation is R⁽²⁾₊ = R⁽²⁾₋ + R⁽¹⁾₋Δ₁ + Δ₂, with the minus side
inside. So F = R⁽¹⁾_inΔ₁ + Δ₂ with R_in on the **left**, as in the code. In U_r, R⁽¹⁾_in = A₀/z − Δ₁^{reg}, because the
principal parts cancel. The pieces are:
- A₀/z = A₀/(4c) − A₀w/(16c²) + …, with w = z − 4c;
- reg0 and reg1 are the u⁴ and u⁶ coefficients of u⁴Δ₁^r, i.e. the (z−4c)⁰ and (z−4c)¹ terms;
- Res_{4c}(R_inΔ₁) = r₀A_r + r₁B_r, since Δ₁^r = B_r/w² + A_r/w + …;
- Res_{4c}Δ₂^r is the u⁻² coefficient of Δ₂, i.e. the u⁵ coefficient of u⁷Δ₂ (line 94).

All of this is correct.

**Residue at 0.** The pieces are:
- Δ₁⁰ = A₀/z + C₀ + … has a simple pole. So Res₀(R_inΔ₁⁰) = R_in(0)A₀ with R_in(0) = −A_r/(4c) + B_r/(16c²) − C₀. This is
  correct; C₀ is the v² coefficient of v²Δ₁ = −zΔ₁ = −A₀ + C₀v² − ….
- Res₀Δ₂⁰: v⁴Δ₂ = z²Δ₂ = E₂ − E₁v² + …, so E₁ = −coeff(v²), as in line 138.
- I also computed E₂ = 0, so Δ₂⁰ has only a simple pole (INFO F6). C₀ agrees exactly with E_pgt1 Lemma E.5 (c0check.out).

**Extraction.** Q = RP₀^∞ gives Q₁ = P₁ + R_1 exactly. With R_1 = A/n + R_1⁽²⁾/n², √((Q₁)₁₂(Q₁)₂₁)/c is expanded in ε = 1/n,
taking the branch with value 1 at ε = 0. Both are correct. The second-order b-coefficient decomposes as:

  d₂ = i((R₁⁽²⁾)₂₁ − (R₁⁽²⁾)₁₂)/(2c) + A₁₂A₂₁/(2c²) − b₁²/8,  b₁ = i(A₂₁ − A₁₂)/c.

The individual source terms are printed in tamper.out. They are high-degree rational functions of (p, s), and only their sum
collapses to the quadratic closed form. So the closed form is not an artefact of any single term.

### 1.3 Meromorphy, exactly (sym_parity.py)

Near 4c the parities in u are:
- z^{1/2} is even;
- 𝔞_∞² is odd;
- φ̃ is odd;
- H := (−ω)^{1/2} satisfies H(−u) = 1/H(u), because (z^{1/2}+u)(z^{1/2}−u) = 4c.

Near 0 on z = −v², the parities in v are: f^{1/2} and 𝔞_∞² are odd, and ρ(−v) = 1/ρ(v).

So Δ_k is single-valued if and only if its matrix formula is invariant under (𝔞², H, Φ) ↦ (−𝔞², 1/H, −Φ). I checked this
with free symbols, exactly and to all orders, for Δ₁^r, Δ₂^r, Δ₁⁰ and Δ₂⁰. All four pass.

For a generic matrix G, invariance holds exactly when G has the pattern g₁₁ = (−1)^{k+1}g₂₂ and g₂₁ = (−1)^{k+1}g₁₂. So
Lemma E2.6(a) tests the sign pattern of X₂ and Ξ₂: an X₂ with the k = 1 pattern fails. It does not test their size or sign
(see F5).

## 2. Making it fail (tamper.py, num_d2.py modes)

The pickled intermediates come from an unmodified copy (dump.py). Each variant recomputes d₂ exactly and compares it with
the closed form. In the table, "same as above" means the variant is algebraically the same error as the row above it.

| Variant | Exact symbolic d₂ − closed form | Quadrature route, (3/2, 2) |
|---|---|---|
| as in the script | **0** (passes) | 8.5·10⁻⁸ |
| X₂ → −X₂ | −(213p⁴ + … + 350)/(2880p²) ≠ 0, fails | −1.04 |
| u₂ ↔ v₂ (X₂ with transposed off-diagonal) | not run symbolically | −1.04 |
| Ξ₂ → −Ξ₂ | 3(p+2)²(p−2s+2)(3p−2s+2)/(64p²), fails | −0.319 |
| a₂ ↔ b₂ | not run symbolically | −0.319 |
| drop R_inΔ₁ at both edges | ≠ 0, fails | +0.042 |
| drop R_inΔ₁ at 0 only | −(p+2)(p−2s+2)(3p−2s+2)(…)/(384p⁴), fails | — |
| drop R_inΔ₁ at 4c only | ≠ 0, fails | — |
| Δ₁R_in instead of R_inΔ₁ | ≠ 0 (twice the "drop both" error), fails | +0.084 |
| drop r₁B_r | ≠ 0, fails | — |
| drop C₀ in R_in(0) | ≠ 0, fails | — |
| Res₀Δ₂⁰ with the wrong z = ±v² sign (E₁ ↦ −E₁) | same as Ξ₂ → −Ξ₂, fails | — |
| omit the −Δ₁^{reg} terms of R_in | ≠ 0, fails | — |
| flip the sign of R_in = R_out − Δ₁ | ≠ 0, fails | — |
| R⁽¹⁾_out·Δ₁ instead of R⁽¹⁾_in·Δ₁ (whole function) | equivalent by construction, see F4 | 8.5·10⁻⁸ (**invisible**) |
| truncation K = 4, O = 7 (trunc4) | 0 (passes) | — |
| truncation K = 3, O = 5 (trunc3) | −(171p⁴ + …)/(4608p²), fails | — |
| perturb S's e² coefficient by 10⁻³ (κ₃) | −7p²/51200, fails (**c-independent**, see F2) | — |
| perturb S's e³ coefficient (κ₄) | 0 (passes) | — |
| perturb 𝔞's z¹ or z² coefficient (f″(0), f‴(0)) | 0 (passes) | — |

Notes on the table:
- At (3, 5/2), α = −½. There a₂ = b₂ = 0 and every Δ₂⁰ residue carries a factor (4α²−1), so flipping Ξ₂ is invisible. This
  is a correct degeneracy, not a blind spot of the check.
- The quadrature column for "R_out·Δ₁" makes the point of F4: the whole-function substitution changes nothing at all.

Conclusions:
- The final assertion has teeth against every bookkeeping error I could think of except one. The exception is "R_out
  versus R_in" for the whole function, which is equivalent by construction (F4).
- The trace identities catch sign flips of X₂ and Ξ₂ but not the u₂ ↔ v₂ or a₂ ↔ b₂ swaps. The swaps are caught by
  check_e2_num and by the final d₂ (F5).
- d₂ depends on the soft-edge series through κ₂ and κ₃ only. It depends on the hard-edge map only through f′(0); f″(0) and
  f‴(0) drop out, as F₂ did at first order (REVIEW_Plan65_B F2).

## 3. Independent route (num_d2.py; NUMERICAL)

**Construction.** g, φ, φ̃ = φ ± iπz^{−1/p}, f^{1/2} = −(φ ± iπ)/2 and ω = D_W²/W₀ are built exactly as in check_e_num.py [3]:
mpmath quadrature of the arcsine mixture and of the Szegő integral of x^α(4c−x). No closed form or series from
Lemma E.4 / E2.4 is used. Δ₁ and Δ₂ are formed pointwise from the Lemma E2.3 formulas, with X₁, X₂, Ξ₁, Ξ₂ as the only
symbolic inputs.

**Cauchy step.** R⁽¹⁾_out(z) = Σ_e (1/2πi)∮_{|s−e|=0.2, ccw}Δ₁(s)ds/(z−s) is evaluated at points of larger circles, |z−e| = 0.35.
Then R⁽¹⁾_in = R⁽¹⁾_out − Δ₁ there, and R₁⁽²⁾ = Σ_e(1/2πi)∮_{0.35}(R_inΔ₁ + Δ₂)dz. All circles use a K-point midpoint
trapezoid. The b-functional is expanded to second order. This uses none of the Laurent coefficients A₀, A_r, B_r, C₀, Δ^{reg}
or E₁, and none of the u- and v-series.

**Results (K = 48, dps 20).**

| (p, s) | α | d₁ | d₂ (quadrature) | closed form | diff |
|---|---|---|---|---|---|
| (2, 3) | 0 | −1.00000007 | 0.99999988 | 1 | 1.2·10⁻⁷ |
| (3/2, 2) | −1/3 | −0.50000017 | 0.36805547 | 0.36805556 | 8.5·10⁻⁸ |
| (3, 5/2) | −1/2 | −0.74999940 | 0.55208369 | 0.55208333 | 3.6·10⁻⁷ |
| (5/4, 4) | 1.4 | −1.50000000 | 1.41624989 | 1.41625 | 1.1·10⁻⁷ |
| (5/2, 9/2) | 0.4 | −1.75000013 | 2.34541609 | 2.34541667 | 5.8·10⁻⁷ |
| (2, 2) | −1/2 | −0.50000010 | 0.31249995 | 0.3125 | 5.0·10⁻⁸ |
| (4, 3/2) | −0.875 | −0.24999723 | −0.11848909 | −0.11848958 | 5.0·10⁻⁷ |
| (1.1, 3) | 0.818 | −0.99999999 | 0.87014466 | 0.87014463 | 3.0·10⁻⁸ |

**Accuracy.** At (3/2, 2) the error is:

| K | radii | dps | error |
|---|---|---|---|
| 32 | 0.2 / 0.35 | — | 1.4·10⁻¹⁰ |
| 64 | 0.2 / 0.35 | 30 | 1.8·10⁻⁶ |
| 64 | 0.15 / 0.4 | — | 5.5·10⁻⁶ |

More nodes do not help. The limit is the accuracy of the g quadrature at nodes close to the band or cut, not the
trapezoid. These are differences, not error bounds (Rule N). The discrimination against the sabotaged variants
(≥ 3.6·10⁻²) is five orders of magnitude.

**Independence.** This route shares with check_e2_sym only:
- the DLMF matrices;
- the conjugation structure of Lemma E2.3;
- the orientation convention.

It shares neither the series of Lemma E2.4, nor the closed forms of E.4(iii), nor any of the Laurent or residue bookkeeping.

## 4. Numbers, p = 2, p = 1, Cor E2.7, remarks

**Grid.** check_e2_grid.py re-runs in 5.8 s from the Plan 62 cache, and the output is byte-identical. I recomputed every
closed-form value as an exact rational, e.g. 19/288, 53/144, −91/768, 341/192. All 25 printed values match to the 8 printed
digits. The largest |fit − cf|/half-range is 0.60, at (4, 2).

At p = 1, fit − d₂(1, s) = −0.083333 at all five s. The deviations from d₂ − 1/12 are at most 1.3·10⁻⁶, as stated in
Remark E2.10.

**Closed forms.**
- The two forms of d₂ in Thm E2.1 agree (sympy).
- At p = 2 the formula reduces to (s² + 6s − 11)/16.
- **Independent p = 2 check.** For s = 2, the exact Lommel b_n² = π⁴/((4n+1)²(4n−1)(4n+3)) with c(2) = π²/16 (numerically
  equal to c_p(2)) gives n²b_n/c = 1 − 1/(2n) + (5/16)/n² + …, and d₂(2, 2) = 5/16.
- **p = 1.** c(1) = 1/2 and 2p c(p)ζ(−p)|_{p=1} = −1/12 (mpmath).

**Remark E2.8.** The n⁻² term of (1 + (s−1)/(2pn))^{−p} is (p+1)(s−1)²/(8p) (sympy). 𝖤 at s = 1+p equals (p+1)/12, so its
s-dependent part vanishes there, as stated.

**Remark E2.11.**
- The s² coefficient is (p²−2)/(8p²).
- 2(1/4 − ∂²_s d₂) = 1/p².
- The check_so_convex.out values at n = 1600 are 1.3885e-4 (p = 3/2), 7.8127e-5 (p = 2) and 3.4740e-5 (p = 3). These equal
  1/(2p²n) to 4 digits, and the same holds for p = 1/2 and p = 1.
- These are the standard second divided differences f[s₀, s₁, s₂] ≈ ½f″, which is why the factor ½ appears (F7).

**Cor E2.7, by hand.**
- d₁ − d₁″ = p.
- δ′ = d₂ − d₂″ − (d₁² − d₁″²)/2 = (s−1)/p − p/2. This agrees with the script's −(p² − 2s + 2)/(2p).
- The 1/j coefficient of log h_j(s) − log h_j(s+2p) is 2[p·½ − δ′] = p − 2δ′. This uses Σ1/i = log j + γ + 1/(2j) and
  Σ1/i² = ζ(2) − 1/j.
- K = −2 log c follows from UL with s − s₀ = −2p.
- The n log c terms cancel and leave 2 log c. The factorials leave −2p log n. So γ = −2p + 2d₁ + p − 2δ′ = −(p+2)(s−1)/p.

## 5. Findings and required fixes

**F1 (MINOR; Rule X and provenance; check_e2_sym.py docstring, lines 9 and 13, and the "conjectured closed form" prints).**
1. The docstring cites "check_e2_coef", which does not exist; it should be check_e2_num.
2. The script calls the target the "conjectured closed form", but E2_pgt1 does not say where the conjecture came from. If it
   was fitted from the Plan 62 grid, then check_e2_grid.out is a consistency check of that fit, not independent evidence
   for the formula (Rule X). The independent evidence is the Riemann–Hilbert computation together with §3 here.

*Required fix.*
- Change the docstring reference to check_e2_num.
- Add one sentence in E2_pgt1 §1 or §10 stating how the closed form was first obtained (fit or guess) and that
  check_e2_sym derives d₂ without using it, the comparison being only the final assert.
- Rename "conjectured closed form" to "closed form of Thm E2.1" in the prints, and regenerate the .out.

**F2 (MINOR, overclaim; E2_pgt1 §1, last sentence of the mechanism paragraph, and §10 "c-independence").** The c-independence
of d₂ is automatic. In the model data, φ̃, f, 𝔞_∞, ω and ρ are all functions of z/c alone, through S(−u²/(4c)), 𝔞(z/4c),
v/√c and (4c)^{−3/2}u³. So every residue is homogeneous of degree 1 in c, as are P₁ and the products R_inΔ₁, and d₂ cannot
depend on c whatever p-dependent normalisation is used.

Demonstration: pertS.py changes κ₃ and gives a wrong d₂ (−7p²/51200 off) that is still c-independent ("depends on c?
False"). The check only catches errors that break the homogeneity in c, such as a wrong power of 4c.

*Required fix.* Replace "which is a non-trivial internal check since c(p) is transcendental" with "a consistency check of the
c-homogeneity of the inputs (it catches a wrong power of c, not a wrong p-dependent constant)", and adjust the §10 bullet to
match.

**F3 (MINOR; Lemma E2.6 statement, "series truncated at orders shown in the script to be sufficient", and the §10
"Truncation orders" bullet).** The script does not show sufficiency. It uses one fixed, generous truncation (K = 6 terms of S
and 𝔞, u-powers < 11, v-series to v⁵). I checked sufficiency:
- K = 4, O = 7 still passes, and K = 3, O = 5 fails;
- d₂ depends on κ₂ and κ₃ but not on κ₄, and not on f″(0) or f‴(0).

So the §10 list ("κ up to κ₄", "f up to its z³ coefficient") is an upper bound on what the Laurent coefficients use, not
what d₂ uses.

*Required fix (either one).*
- Add to check_e2_sym.py a second pass at a lower truncation (e.g. K = 4, O = 7), asserting the same d₂; or
- reword Lemma E2.6 to "(series truncated at orders that exceed the order count of §10)".

*Suggested.* Following Plan 65 F2, keep κ₄ and the z², z³ coefficients of 𝔞 as free symbols and assert that d₂ does not
depend on them. This reduces the weight Theorem E2.1 puts on Lemma E2.4 to κ₂, κ₃ and f′(0).

**F4 (INFO; Prop. E2.5 and Lemma E2.6(c)).** Δ₁² is a scalar multiple of I on both circles:
- on the soft circle, X₁² = −(35/5184)I, so Δ₁^r² = −(35/5184)φ̃⁻²I;
- on the hard circle, Ξ₁² = −det(Ξ₁)I, because tr Ξ₁ = 0.

So replacing R⁽¹⁾_in by R⁽¹⁾_out = R⁽¹⁾_in + Δ₁ in F changes R₁⁽²⁾ by a multiple of I. That change is invisible to the
b-functional, which reads only the off-diagonal entries; num_d2 "outer" mode gives an identical d₂.

The in/out distinction is therefore not tested by d₂. It would matter for the second-order α_n coefficient (the "Open"
bullet in §9), whose a-functional reads (Q₁)₂₂. The left-versus-right order is tested: Δ₁R_in fails.

*Suggested.* One sentence in §6(c), so that a future α_n computation does not assume this ordering was checked.

**F5 (INFO; §10 "Branches" and "Sign and normalisation").**
- The meromorphy assertion of Lemma E2.6(a) is invariant under X₂ → −X₂, u₂ ↔ v₂, Ξ₂ → −Ξ₂ and a₂ ↔ b₂ (§1.3). It tests
  the branches and the sign pattern, not the values.
- The trace identities catch the sign flips but not the swaps.
- The swaps are caught by check_e2_num and by the final d₂: in §2 the quadrature route shifts d₂ by −1.04 and −0.32.

The §10 text is correct as written. *Suggested:* note in §10 which check covers which error.

**F6 (INFO).**
- Δ₂^{0,mod} has a simple pole only (E₂ = 0).
- Res₀Δ₂⁰ and A₀ carry the factor (4α²−1), so at α = ±½ (s = 1 + p/2 or s = 1 + 3p/2) the hard edge contributes nothing at
  second order. This matches the elementary Bessel model there.
- The script does not need E₂ = 0, because Δ₁⁰'s pole is simple.

*Suggested:* assert E₂ = 0 and note it in §6(c).

**F7 (INFO; Remark E2.11).** "(step-1 divided differences)" is unclear. check_so_convex computes standard second divided
differences f[s₀, s₁, s₂] ≈ ½∂²_s f, which is why the measured value is 1/(2p²n) against the predicted ∂²_s log h_n ≈
1/(p²n). The agreement holds at 4 digits at n = 1600 for all p ∈ {½, 1, 3/2, 2, 3, 4}, including p ≤ 1, where Theorem E2.1
does not apply. The remark stays HEURISTIC.

*Suggested wording:* "matches the measured second divided differences f[s₀, s₁, s₂] ≈ ½∂²_s log h_n ≈ 1/(2p²n)".

**F8 (INFO; check_e2_num.py [1]).** The per-sector print label reads "|X(zeta) − X|", copied from check_e_num, although the
quantity is the X₂ error. This is cosmetic.

**Not findings (checked, correct):**
- Lemma E2.4(ii): S(0) = 4/3, and the e¹ coefficient 14/15 + 8/(15p) gives κ₂ (both asserted).
- The −(z−4c)/(16c²) Taylor term of A₀/z.
- The u⁵ ↔ (z−4c)⁻¹ and v² ↔ z⁻¹ index conversions, with the sign from z = −v².
- The branch of √(bb) at ε = 0.
- check_e2_sym.out reproduces exactly (the timing lines are my addition).
- check_e2_grid.out is byte-identical on re-run.
- The DLMF k = 2 coefficients.

## 6. Log of what I ran (venv python; scratchpad `reviewB/`)

| Run | Time | Result |
|---|---|---|
| orig.py (copy of check_e2_sym.py) | 3 min 55 s | output identical to check_e2_sym.out; ALL ASSERTIONS PASSED |
| dump.py (copy + pickle) | ~4 min | same output; pieces.pkl |
| tamper.py | 49 s | the script's bookkeeping plus 11 sabotaged variants (table §2) |
| trunc4.py / trunc3.py | — | pass / fail |
| pertS.py, pertS3.py, pertA.py, pertA1.py | — | fail (−7p²/51200, c-free) / pass / pass / pass |
| sym_parity.py | 15 s | exact meromorphy of Δ₁, Δ₂ at both edges; generic-pattern conditions |
| num_d2.py ok, 8 (p, s) | ~30 s each | §3 table |
| num_d2.py flipX2, flipXi2, noRD, rightorder, outer, swapuv, swapab | — | §2 table |
| convergence: K = 32, 64; radii (0.15, 0.4); dps 30 | — | §3 |
| misc.py | 2 s | closed-form identities, p = 2 Lommel (5/16), c(2), c(1), κ₁ = −1/12; own Ξ₂, X₂ extraction |
| c0check | — | C₀ = E.5's C₀; X₁² = −(35/5184)I |
| check_e2_grid.py | 5.8 s | byte-identical; exact rational recomputation of the closed-form column |

## 7. Summary for the integrator

On the computation:
- d₂(p, s) = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12 is the correct output of the second-order Riemann–Hilbert
  data for p > 1, s > 1.
- I confirmed it exactly (re-run and sabotage tests) and NUMERICALLY by an independent quadrature route that uses no
  series and no Laurent bookkeeping.
- The p = 2 reduction, the p = 1 constant and the Cor E2.7 exponent are correct.

F1, F2 and F3 are required; they cover wording, provenance and a scope statement. F4–F8 are INFO.

REVIEWED status also needs reviewer A's verdict on the estimates: Lemma E2.3's uniformity and n-dependence, Prop. E2.5,
and the remainder exponent ν = min(3, 1+p).
