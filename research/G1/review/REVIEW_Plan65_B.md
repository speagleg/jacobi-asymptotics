# Rule R review: Plan 65, reviewer B (algebra and extraction), E_pgt1.md

Reviewer: independent second reader B (Rule R), focused on the explicit computation that produces the constants of
Theorem E.1 and Corollary E.6. Reviewer A checks the analytic estimates separately (Lemma E.2, the n-dependence part of
Lemma E.3, the small-norm bounds in Prop. E.5′, and the remainder in §7.2). I did not review those estimates and accept
none of them here.

Branch `plan-65-E-pgt1`, commit 78cfd1f. Targets:
- research/G1/RH/second_order/E_pgt1.md: §0, Lemma E.3 (matrix forms and prefactors), Lemma E.4, Lemma E.5,
  the extraction in Prop. E.5′ and §7.1, Cor E.6 / §7.2, and §8.1;
- checks/check_e_sym.py, check_e_num.py, check_e_grid.py and their .out files;
- research/G1/RH/CITATIONS.md entry "(DLMF-9.7.2, Plan 65)".

Internal inputs I re-read: RH_px.md §1 (α_x), §4.1 (Bessel parametrix P₀, Ẽ_N, Lemma 4.1 on f and φ); Paper 2 sec_6.tex
(eq. airy-model, airy-relations, airy-infty, omega-root, airy, Lemma airy, jumps-4c); SECOND.md Thm 2.3 and §1.1;
REVIEW_Plan62.md (for the format). External: the DLMF page for §9.7, fetched again today.

My scratch computations are in the session scratchpad (`review65B/`, not committed):
- m1_models.py: mpmath check of the Bessel and Airy model expansions, written from scratch;
- m2_sym.py: sympy re-derivation of E.4, E.5, the extraction and Cor E.6, written before I read check_e_sym.py;
- m3_p2.py: Stieltjes procedure for σ_{2,2};
- m4_k2chain.py: dependence of the chain coefficient on κ₂ and on f″(0).

## Overall verdict: **ACCEPT WITH FIXES** (algebra and extraction only)

I re-derived every constant independently and found no mathematical error. The constants checked are:
- Q₀ and X;
- f′(0), f″(0)/f′(0), κ and κ₂;
- A₀, A_r, B_r and C₀;
- P₁ and P₂;
- the 1/n coefficients of n^pb_n and n^pα_n;
- w⁽⁰⁾, w⁽¹⁾ and a;
- k₀ and k₁.

The final sign of d₁ is forced by two facts that do not use any data:
- the decay requirement of the lens jump on (4c, 4c+ε);
- the orientation of the circles.

The exact p = 2 formulas and the 80-cell grid then confirm it. All fixes below are minor or INFO: wording, script scope
and notation.

| Statement | Verdict (B's scope) | Notes |
|---|---|---|
| §0 conventions (α = α_x, a = α+½, c, B_p) | ACCEPT WITH FIXES (F5) | α_x = (s−1−p)/p as in RH_px §1, line 36 |
| Lemma E.3: Bessel Q₀, prefactor 1/(16f^{1/2}), ρ^{σ₃} conjugation | ACCEPT | numerically re-derived in all three sectors |
| Lemma E.3: Airy X, prefactor −1/φ̃, (−ω)^{∓σ₃/2} conjugation | ACCEPT | numerically re-derived in all four sectors |
| Lemma E.3: "depends on n only through H_n", Δ₁ = Δ₁^{mod} + O(n^{−p}) | not reviewed (reviewer A) | — |
| Lemma E.4 (i) f′(0), f″(0)/f′(0) | ACCEPT | independent sympy |
| Lemma E.4 (ii) κ, κ₂, sign of φ̃ | ACCEPT | independent sympy; sign forced by the lens decay |
| Lemma E.4 (iii) ω^{mod}, (−ω^{mod})^{1/2}, ρ^{mod} | ACCEPT | re-derived by hand from Paper 2 Lemma szego(i) |
| Lemma E.5 (A₀, A_r, B_r, C₀; meromorphy) | ACCEPT | independent sympy, exact match |
| Prop E.5′: R⁽¹⁾ = principal parts, R₁⁽¹⁾, R₂⁽¹⁾, R⁽¹⁾(0) (algebraic part) | ACCEPT | orientation re-derived; estimates are for reviewer A |
| §7.1 extraction and Thm E.1 constants | ACCEPT WITH FIXES (F1) | d₁ = −(s−1)/2 and n^pα_n/(2c) = 1 − (s−1+p)/(2n) confirmed; one sentence is inaccurate |
| §7.2 identity (E.6.1), w⁽⁰⁾, w⁽¹⁾, a, unfolding, k₀, k₁ | ACCEPT | independent sympy; RH.md Lemma 5.1 consistent |
| §8.1 comparisons | ACCEPT WITH FIXES (F4) | p = 2 exact ✓, grid 80/80 ✓ |
| §10 Rule A "sign of Δ₁^r" | ACCEPT | final sign confirmed by independent routes (§3 below) |
| check_e_sym / check_e_num / check_e_grid | ACCEPT WITH FIXES (F3, F4) | all reproduce; no hard-coded pass flags |
| CITATIONS "(DLMF-9.7.2, Plan 65)" | ACCEPT | matches the live page |
| CITATIONS "(DLMF-10.40, Paper 2)" as reused for α ≥ 1 | ACCEPT WITH FIXES (F6) | — |

## 1. Independent re-derivations

### 1.1 Lemma E.3: the model first corrections (m1_models.py, mpmath, written from scratch)

**Bessel.** I implemented KMVV (6.23)–(6.25) as recalled:
- I_α and K_α in |arg ζ| < 2π/3;
- ½H^{(1,2)}_α(2(−ζ)^{1/2}) with e^{±απiσ₃/2} in the two thin sectors.

I computed 16ζ^{1/2}(L⁻¹Ψ(ζ)e^{−2ζ^{1/2}σ₃} − I), where L = (2πζ^{1/2})^{−σ₃/2}M. The test points were:
- α ∈ {0.3, −0.6, 1.7};
- arg ζ ∈ {0.2, −1.0, 1.9, 2.5, −2.5, 3.0};
- |ζ| = 10³ and 10⁵, at 400 digits (the Hankel sectors need this to avoid cancellation).

The distance to [[−(1+4α²), −2i], [−2i, 1+4α²]] is 9.8·10⁻³ at |ζ| = 10³ and 9.7·10⁻⁴ at |ζ| = 10⁵ for α = 0.3. The
corresponding values are 7.2·10⁻³ and 7.2·10⁻⁴ for α = −0.6, and 0.28 and 0.028 for α = 1.7. In every sector the
decay is exactly ∝ |ζ|^{−1/2}, which is (E.3.1).

I also checked the hand algebra of the proof:
- the first-order entries of Ψe^{−wσ₃}, from 10.40.1–4 with a₁ = (4α²−1)/8 and b₁ = (4α²+3)/8, are
  (1/√2)[[−a₁, ia₁], [−ib₁, b₁]]/w;
- multiplying by M⁻¹ = [[1, −i], [−i, 1]]/√2 gives ½[[−(a₁+b₁), i(a₁−b₁)], [i(a₁−b₁), a₁+b₁]];
- with w = 2ζ^{1/2} this is the stated matrix over 16ζ^{1/2};
- σ₃(·)σ₃ turns the off-diagonal −2i into +2i, which gives Q₀;
- σ₃Mσ₃ = M⁻¹ (asserted in m2).

The left factor matches RH_px §4.1: Ẽ_N = NW̃^{σ₃}Mf^{σ₃/4}(2πN)^{σ₃/2}, so Ẽ_N(2πζ^{1/2})^{−σ₃/2}M⁻¹ = NW̃^{σ₃}. In the Q-frame,
D_∞^{−σ₃}NW̃^{σ₃} = P₀^∞(W̃/D_W)^{σ₃} = P₀^∞ρ^{σ₃}. This gives Δ₁⁰ = (1/(16f^{1/2}))P₀^∞ρ^{σ₃}Q₀ρ^{−σ₃}(P₀^∞)⁻¹, with ζ^{1/2} = nf^{1/2}.
The prefactor and its sign are confirmed.

**Airy.** From Paper 2 (eq. airy-model), I built Ψ^{I…IV} myself (k_Ai = √(2π)e^{iπ/12}, q = e^{2πi/3}) and computed
ξ(M⁻¹ζ^{σ₃/4}Ψ^jζe^{−ξσ₃} − I) for two angles in each of the four sectors, at |ζ| = 10² and 10⁴. The distance to
X = [[−1/72, −i/12], [−i/12, 1/72]] is 6.6·10⁻⁵ and then 6.6·10⁻⁸, i.e. O(ξ⁻¹), in all sectors. By hand,
(u₁+v₁)/2 = −1/72 and i(v₁−u₁)/2 = −i/12 = −i(u₁−v₁)/2.

With ξ = (2/3)ζ^{3/2} = −nφ̃ (Paper 2 Lemma airy (iii)), X/ξ = −X/(nφ̃), so the prefactor −1/φ̃ is right. The conjugation
is right too: A_r = P₀^∞(−ω)^{−σ₃/2}M⁻¹f_r^{σ₃/4}, so A_rn^{σ₃/6}ζ^{−σ₃/4}M = P₀^∞(−ω)^{−σ₃/2}.

### 1.2 Lemma E.4, derived independently (m2_sym.py)

First I re-derived the density formula itself. From μ* = ∫₀¹arc_{4cτ^{−p}}dτ, substituting τ = (4c/x)^{1/p}t and then y = t^p
gives:
- ψ*(x) = λ_p(x)I_{x/4c}(1/p+½, ½) on (0, 4c), using (4c)^{1/p} = π/B_p;
- ψ* = λ_p on (4c, ∞), i.e. saturation.

This checks the G2 input as quoted. From that representation, sympy gives:
- C₀ = 1/(π√c(p+2));
- f′(0) = −1/(c(p+2)²) and f″(0)/f′(0) = (p+2)/(6c(3p+2)), with f = −(π²/4)μ*((0, z])²;
- κ = 1/(6pc^{3/2}) and κ₂ = −(7p+4)/(40pc), from φ̃₊ = iπ∫_x^{4c}(λ_p − ψ*) expanded in v = 4c − x to v^{5/2}.

All four agree exactly with E.4.

The normalisation f = −(π²/4)μ*² (rather than −π²μ*²) is consistent with the convention "φ jumps by πi × mass, lens
entries e^{±2nφ}". That convention is fixed by e^{2Nf^{1/2}σ₃}e^{Nφσ₃}(−1)^N = I (RH_px §4.1) and by the e^{2nφ̃} in Paper 2
(eq. jumps-4c).

**Sign of φ̃ (the slip of §10).** It is forced without any data:
- on (4c, 4c+ε) the jump of Q is [[1, 0], [ωe^{2nφ̃}, 1]] (Paper 2 eq. jumps-4c) with ω bounded, so φ̃ < 0 there;
- φ̃ = −κu³(1 + O(u²)) with u > 0 there, so κ > 0;
- the band value φ̃₊ = iκv^{3/2} is the analytic continuation through ℂ₊ (u = iv^{1/2}), and it matches
  +iπ∫(λ_p − ψ*), which lies on the positive imaginary axis because λ_p > ψ* on the band.

So the code's original "+1/φ̃" was wrong, and the corrected −1/φ̃ with κ > 0 is right.

### 1.3 Lemma E.5 (m2_sym.py: full sympy series, no hand truncation)

The Airy part is expanded in u = (z−4c)^{1/2} and the Bessel part on z = −v². For the Bessel part I used:
- f^{1/2} > 0;
- a² = √(4c+v²)/v;
- ρ² = (v/(2√c) + √(1+v²/4c))^{2(1+α)}.

Results:
- the odd powers of u and v vanish identically;
- **B_r, A_r, A₀ and C₀ agree exactly with E.5** (the sympy differences simplify to 0).

The hand value K = lim z a²/f^{1/2} = −2c(p+2) checks.

### 1.4 Extraction (§0, Prop E.5′, §7.1)

**Functionals.** I re-derived the extraction formulas from the Fokas–Its–Kitaev (FIK) matrix Y of degree n
(Y₁₁ = π_n, Y₁₂ = Cauchy transform of π_nw, Y₂₁ = −(2πi/h_{n−1})π_{n−1}):
- (Y₁)₁₂(Y₁)₂₁ = h_n/h_{n−1} = b_n²;
- (Y₂)₁₂/(Y₁)₁₂ = α_n − e_n and (Y₁)₂₂ = −e_n, where e_n is the x^{n−1} coefficient of π_n; so the a-functional is α_n.

The scaling U = n^{pnσ₃}Y(z/n^p) multiplies both functionals by exactly n^{2p} and n^p. There is no n versus n±1 shift,
which matters because a shift would move the 1/n coefficient by p.

**Invariance.** Both functionals are invariant under left multiplication by a constant diagonal matrix. They are also
invariant under right multiplication by a diagonal I + F₁/z + …: (F₁)₂₂ enters (Q₂)₁₂/(Q₁)₁₂ and (Q₁)₂₂ equally and cancels.

**Global parametrix.** From (1 − 4cw)^{1/4} I get P₁ = [[0, ic], [−ic, 0]] and P₂ = [[c²/2, 2ic²], [−2ic², c²/2]]. Hence
(P₁)₁₂(P₁)₂₁ = c² and a(P) = 2ic²/(ic) − 0 = 2c exactly, as claimed.

**Orientation.** Write R_out = R_in·P̂(P₀^∞)⁻¹. With clockwise circles the + side (left) is the outside, so R₊ = R₋J. Then
(1/2πi)∮_cw Δ₁(s)ds/(s−z) = +Σ principal parts for z outside. This gives R₁⁽¹⁾ = A₀ + A_r and R₂⁽¹⁾ = 4cA_r + B_r (from
A/(z−4c) = A/z + 4cA/z² + …), and R⁽¹⁾(0) = −C₀ − A_r/(4c) + B_r/(16c²). All are confirmed.

**Constants (sympy, with α = (s−1−p)/p):**
- n^pb_n/c = 1 − (s−1)/(2n), from i(A₂₁ − A₁₂)/c = −p(α+1); the p cancels against α;
- n^pα_n/(2c) = 1 − p(α+2)/(2n) = 1 − (s−1+p)/(2n);
- e₁ˢ = −p/2 and e₁ = +p/2 (repo pairing).

I decomposed the result by source:
- **A₀ contributes exactly 0 to both functionals**. A₀ ∝ [[1, i], [i, −1]], and b needs A₂₁ − A₁₂ = 0, while a needs
  A₁₁ + 2iA₁₂ − A₂₂ = k(1 + 2i·i + 1) = 0 (with A₀ = k[[1, i], [i, −1]]). Also A₀/z has no 1/z² term.
- The Airy part alone gives −p(α+1)/2 for b_n and −p(α+2)/2 for α_n.
- The α² part of A_r, (cα²p/4)[[1, −i], [−i, −1]], cancels **within** the Airy contribution: +4k from R₁ against −4k from
  4cA_r in R₂. See F1.

**κ₂ drops out.** With κ₂ kept symbolic, A_r depends on κ₂, but both functionals have zero derivative in κ₂. m4 adds two
more facts: the chain coefficient a is independent of κ₂, and it is also independent of the f″(0) coefficient (which
enters C₀). See F2.

### 1.5 Cor E.6 (§7.2)

**(E.6.1).** g_{n−1} = −(Y₁)₂₁Y₁₁(0)/Y₂₁(0), because Y₂₁ = (Y₁)₂₁·π_{n−1} exactly. Under U this becomes n^pg_{n−1}. The
product (Q₁)₂₁·Q₁₁/Q₂₁ is invariant under constant left diagonals and under right diagonals normalised at ∞, so it is
unchanged in the Q-frame. Confirmed.

**First column.** From RH_px's P₀:
- the first column is ∝ P₀^∞ρ^{σ₃}M(f^{1/4}Ψ₁₁, −f^{−1/4}Ψ₂₁/(2πn))ᵀ;
- with Ψ₂₁/Ψ₁₁ = πi·xI′_α/I_α → πiα (10.25.2), this gives w⁽¹⁾ exactly as stated.

**Values (sympy):**
- w⁽⁰⁾ = (1, i)ᵀ/√(p+2) and w⁽¹⁾ = (α(α+2), iα²)ᵀ√(p+2)/4. The ρ-mixing term sh·a·f^{−1/4} = O(1) does contribute (it is
  the α² in w⁽¹⁾), and the computation includes it.
- n^pg_{n−1}/c = 1 + (α+½)/n, so a = (2s−2−p)/(2p).

**Unfolding.** I re-did it from scratch:
- the even sites give k₀ + k₁ = 2(2d₁ − a), and the odd sites give −p/2 + (k₀−k₁)/2 = a − p;
- so k₀ = −(s−1) − p/2 and k₁ = −(p+2)a;
- RH.md Lemma 5.1 holds: (p/2 + k₀)/2 = d₁.

## 2. Comparison with exact and fitted data (the independent route for the sign)

**p = 2.** I ran the Stieltjes procedure on the truncated σ_{2,2} (K = 4000, 50 digits; m3_p2.py). It reproduces
α_n = 2π²/((4n+1)(4n+5)), b_n² = π⁴/((4n+1)²(4n−1)(4n+3)) and α₀ = π²/15 to the truncation level (~10⁻⁴ relative). This
confirms the SECOND formulas and the indexing b_n² = h_n/h_{n−1}. From these:
- 16n²/((4n+1)(4n+5)) = 1 − 3/(2n) + O(n⁻²) = 1 − (s−1+p)/(2n);
- n²b_n/c = 1 − 1/(2n) + O(n⁻²);
- Thm 2.3's d₁ = −(s−1)/2, k₀ = −s, k₁ = −2(s−2) equal the E.1/E.6 values at p = 2 for all s.

A flipped orientation, or the old +1/φ̃, would give d₁ = +(s−1)/2. So would flipping both A_r and B_r. The exact p = 2
data exclude all of these.

**Grid.** I re-ran check_e_grid.py; the output is byte-identical. Its regex pairs "value (half-range)" columns in the order
d₁, e₁, e₁ˢ, k₀, k₁, which matches the check_so_grid.out header; the unfitted "conj" columns are not matched. The
predicted values are computed from (p, s) and are not typed in.

The result is 80/80 within tolerance, with a largest deviation of 5.3·10⁻⁸. The fits come from the actual coefficients of
Plan 62 (REVIEWED, cache re-verified in REVIEW_Plan62 §1). Rule X is satisfied: these are independent data.

## 3. The check scripts

| Script | Re-run | Identical to .out | Tests what E_pgt1 claims? |
|---|---|---|---|
| check_e_sym.py | 17 s | yes | Yes for E.5, §7.1 and §7.2 algebra. It takes Q₀, X and the closed forms of E.4 as **inputs** (as its docstring says), so it does not test E.3 or E.4; those rest on the hand proofs and on m1/m2 here. The asserts compare computed values with closed forms; nothing is hard-coded as a pass. k₀ is formed as 2d₁ − p/2, i.e. the unfolding identity, which I re-derived. |
| check_e_num.py | 2 min 57 s | yes | [1] and [2] test X and Q₀ in all sectors (I reproduced both independently). [3] builds g, φ, φ̃, f and ω by quadrature, so it is independent of E.4. It shares the Δ₁ structure of E.3, the orientation and the extraction with check_e_sym, so it is not independent of those. One reported value is partly hard-coded (F4). |
| check_e_grid.py | <1 s | yes | Yes (see §2). |

**check_e_num.py re-run.** I re-ran it in the background with the same venv and PYTHONPATH. It took 2 min 57 s, and the output is byte-identical to check_e_num.out.

## 4. Findings and required fixes

**F1 (minor, wording; §7.1, lines 301–302).** The text says "the α²-terms coming from A₀ and A_r cancel". That is
inaccurate. A₀ contributes **nothing** to either functional at order 1/n. The α² terms cancel inside the Airy
contribution, between R₁ ∋ A_r and R₂ ∋ 4cA_r.

*Required fix.* Replace the clause with: "A₀ is annihilated by both functionals (A₀ ∝ [[1, i], [i, −1]]: A₂₁ = A₁₂ and
A₁₁ + 2iA₁₂ − A₂₂ = 0), and the α²-part of A_r cancels between its R₁ and R₂ (4cA_r) contributions". Extend the §5 Remark
and the §1 mechanism paragraph from "does not contribute to b_n" to "does not contribute to b_n or α_n at order 1/n".

**F2 (INFO; Lemma E.4 / §7).** κ₂ and f″(0)/f′(0) affect A_r and C₀ but none of the five constants. I verified this
symbolically: d/dκ₂ and d/d(f″ coefficient) of the b-, α- and g-coefficients are 0. *Suggested:* state this after
Lemma E.5. It lowers the weight that Theorem E.1 and Cor E.6 put on E.4(ii)'s κ₂ and on the τ₁ part of E.4(i).

**F3 (minor, scope statement; §5 label, the Thm E.1 row of the summary table, §10).** Lemma E.5 says "PROVED; check_e_sym.py".
check_e_sym takes Q₀, X and the E.4 closed forms as inputs.

*Required fix.* Add one sentence to §5 "Method": "check_e_sym.py takes Q₀, X (Lemma E.3) and the closed forms of
Lemma E.4 as inputs; those are checked by check_e_num [1]–[2] (Q₀, X) and by the hand proof of E.4, and [3] uses no E.4
closed form".

**F4 (minor; check_e_num.py [3] and §8.1).** In [3], k1 = k0 + p − 2γ′ is computed with **k0 set to the closed form**
−(s−1) − p/2, not from the numerical d₁. So "[3] reproduces … k₁" is a check of γ′ only.

*Required fix (either one):*
- set k0 = 2·d1 − p/2 from the numerical d1 in check_e_num.py, regenerate the .out and update MANIFEST.sha256; or
- reword §8.1 and the header of [3] to "γ′ (= a), and k₁ given k₀ = 2d₁ − p/2".

Numerically nothing changes: d₁ agrees with the closed form to ≤ 7·10⁻⁸.

**F5 (INFO, notation; §0).** "a" denotes both ((z−4c)/z)^{1/4} (the global parametrix, §0, §5 "Method") and α + ½ (§0,
Cor E.6). *Suggested:* rename one of them, e.g. the parametrix function ϑ(z) or 𝔞_∞, and keep a = α + ½ to match SECOND.

**F6 (minor, Rule C; CITATIONS "(Plan 65 reuse)").** The reused entry "(DLMF-10.40, Paper 2)" records "Hypotheses: ν = α
fixed, real, |α| < 1". E_pgt1 applies 10.40.1–4 and 10.17.5–12 for every α > −1, including α ≥ 1 (§10 "Large α"). The
DLMF expansions hold for any fixed ν, so this is only a missing hypothesis check, not an error.

*Required fix.* In the "(Plan 65 reuse)" entry, add: "10.40.1–4 and 10.17.5, .6, .11, .12 are stated for fixed (complex)
ν with no restriction on |ν|. The |α| < 1 in the Paper 2 entry is Paper 2's standing assumption, not a DLMF hypothesis.
E_pgt1 uses them for α ∈ (−1, ∞)."

**F7 (INFO).** The DLMF 9.7.2 entry is accurate. I fetched dlmf.nist.gov/9.7 again (2026-10-15). The alttext gives
u_k = (2k+1)(2k+3)(2k+5)⋯(6k−1)/(216^k k!) = ((6k−5)(6k−3)(6k−1)/((2k−1)216k))u_{k−1} and v_k = ((6k+1)/(1−6k))u_k.
Also 9.7.5–9.7.6 hold with |ph z| ≤ π − δ. Hence u₁ = 15/216 = 5/72 and v₁ = −7/72. The application uses them in closed
subsectors |ph| ≤ 11π/12 (Paper 2's sector check), so the hypotheses hold.

**Not findings (checked, correct):**
- κ₂ = −(7+4/p)/(40c) in the body and −(7p+4)/(40pc) in the table agree;
- the §8.1 identity k₁ = −2(s−2) = −(2+2)(2s−4)/4 holds;
- the §0 claims T⁻¹M = diag(1, i) and σ₃Mσ₃ = M⁻¹ hold;
- E.4(iii) ρ^{mod} gives ρ² = (Υ̂/4c)^{1+α}, which I re-derived from ω = D²/W₀ with z^{−α} = |z|^{−α}e^{∓iπα};
- citing 10.25.2 for xI′_α/I_α → α is appropriate; the entry is in (DLMF-5).

## 5. Summary for the integrator

For the explicit computation behind Theorem E.1 and Corollary E.6 (all of d₁ = −(s−1)/2,
n^pα_n/(2c) = 1 − (s−1+p)/(2n), e₁ˢ = −p/2, a = (2s−2−p)/(2p), k₀ = −(s−1) − p/2 and k₁ = −(p+2)a), reviewer B finds:
- the constants are correct;
- the stated mechanism is correct, with F1's correction to which terms cancel;
- the extraction is correct, with no index shift.

F1, F3, F4 and F6 are required (all wording or scope). F2, F5 and F7 are INFO. REVIEWED status also needs reviewer A's
verdict on the estimates (Lemma E.2, Lemma E.3's n-dependence, Prop E.5′ bounds and the §7.2 remainder).
