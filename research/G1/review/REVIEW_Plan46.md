# Rule R review — Plan 46 (Lemma / Theorem QLP, PROOF.md §3.16)

Reviewer: independent second reader (Rule R). Branch `plan-46-qlp`, commit 43cfcca, `git diff master...HEAD`
(PROOF.md §0 row + §3.16, CITATIONS.md (DLMF-3), LOG.md, plan doc, `checks/check_qlp.py/.out`). Sources read:
RH/px/RH_px.md (§§1–6), RH/RH_p1_general.md (§§1–3, 5–6), RH/plt1/RH_plt1b.md (all), RH/CITATIONS.md ((KV), (Van),
(KMVV) quotes), PROOF.md §3.14 (QL, QLb). DLMF pages 10.25, 10.27, 10.32, 10.34 and 10.40 fetched on 2026-10-14.

## Verdict

**ACCEPT WITH FIXES.** I found no error in the main line of proof. Lemmas ST, GS and BK are correct, and so are
Theorem QLP (a), (b), (c) (for ϑ < ϑ(p, σ)) and Corollary QLP-Λ, for each fixed σ, modulo the cited RH analyses.
Required fixes:
- a citation misattribution: "WLXZ (4.27)" is Vanlessen math/0212014 (4.27) (F1);
- one sub-claim that is not proved as written: the endpoint ϑ = p/2 in (c) for p = 1 (F2);
- a domain slip in Lemma Z (F3);
- a script/label inconsistency at p = 1 (F4);
- polish (F5–F9).

(RU) is correctly kept CONDITIONAL. Audit U is correctly labelled PROOF SKETCH, and it has one more soft spot than it
admits (F6).

## Checks performed

**Lemma ST.**
- (i) z = τe^{iθ}, π/2 < θ ≤ π. For X ≥ 0, Re 1/(X − z) = (X + τ|cos θ|)/|X − z|² ≥ 0.
- For 0 ≤ X ≤ τ, |X − z|² = X² + 2Xτ|cos θ| + τ² ≤ 2τ²(1 + |cos θ|) ≤ 4τ².
- So Re 1/(X − z) ≥ |cos θ|/(4τ), and ν([0, τ]) ≤ (4τ/|cos θ|)Re S ≤ (4τ/|cos θ|)|S|.
- At θ = 5π/6: 4/(√3/2) = 8/√3 ≈ 4.62 ≤ 5, the constant used later. OK.
- Positivity needs supp ν ⊂ [0, ∞). In the X variable the nodes are X_k = (N/k)^p > 0. OK.
- (ii) Im 1/(X − z) = η sin θ/|X − z|² ≥ 0 on ℝ, and |X − z| ≤ 2η for |X| ≤ η. At θ = 3π/8: 4/sin(3π/8) ≈ 4.33 ≤ 5. OK.
- The angle choice is outside every contour (see Lemma Z below). The constant is irrelevant beyond being finite.

**Lemma GS.**
- Convention: Y₁₁ = π_N monic, and Y₁₂ = Σ_k w_kπ_N(X_k)/(z − X_k) (residue convention of RH_px §1).
- Expansion: Y₁₂ = Σ_j z^{−j−1}Σ_k w_kπ_N(X_k)X_k^j. Orthogonality kills j < N, so (Y₁)₁₂ = Σw_kπ_N(X_k)X_k^N = h_N.
- Splitting π_N(z) = π_N(X_k) + (z − X_k)q_z(X_k), with deg q_z = N − 1, gives Y₁₁Y₁₂ = Σw_kπ_N(X_k)²/(z − X_k) = −h_NS_N.
- Dimensions: Y₁₁Y₁₂ ~ h/z and S ~ −1/z. Consistent.
- This is the Stieltjes transform of μ_N = w π_N²/h (the Christoffel–Darboux/Green's-function diagonal), not of σ. Correct.
- V = CYk^{σ₃}: k cancels in V₁₁V₁₂ at z, and (V₁)₁₂ = C₁²(Y₁)₁₂ because C₁m(z) → 1. The analyticity of m at ∞ is not
  even needed: only C₁/m → C₁² is used.
- The rescaling U = N^{pNσ₃}Y(·/N^p) multiplies all weights by one constant, so ν_N is unchanged.
- **Independent check** (mpmath, 60 digits, p = 2, s = 2, 200 atoms, N = 6, z = 0.01e^{5πi/6}):
  - Σμ_N(k)/(X_k − z) = −Y₁₁Y₁₂/(Y₁)₁₂ = 38.02516067300 + 11.95937695836i, both ways;
  - (Y₁)₁₂/h = 1;
  - Lemma ST's bound ≥ the true mass at τ = 10⁻¹ … 10⁻⁷.
- Application in RH_px: on Ω_∞, R = U, Q = T and V = C_∞TF^{σ₃}. So V = CUk^{σ₃}, with C = C_∞e^{−Nlσ₃/2} the same
  constant at z and near ∞, and V = I + O(1/z) (Lemma 3.5). OK.
- RH_plt1b keeps this chain (F has no jump on (−∞, 0), and Lemma 3.5 holds). RH₁(r) has R = U on Ω_∞, which contains iℝ
  near 0 (RH_p1_general §5, "iℝ lies in Ω_∞"). OK.
- The use of invariances on the factorization V = 𝒵P₀ is legitimate, because only the row product at z is rewritten (F8,
  wording).

**The evaluation point is in Ω_∞, with only non-oscillatory parametrices.**
- p > 1:
  - The lips are preimages of ph ζ = ±2π/3 under ζ = N²f, with f′(0) < 0. So they leave 0 at ±π/3 (RH_px Lemma 4.3;
    (Y4)_x uses the same "δ₀ ≤ |arg z| < π/3" strip).
  - The R-transformation region is the lens (the D/D̃ jump sits on the lips).
  - The left half-plane is node-free, and the only jump there is (h2) on (−δ, 0).
  - So z = τe^{5πi/6} is in Ω_∞ for every τ ∈ (0, δ₁], uniformly in N, at angular distance ≥ π/6 from every contour.
- 0 < p < 1:
  - The lips are at ±πp/4 and the seams at ±πp/2 < π/2 (RH_plt1b §2), so z is in S_out ∩ Ω_∞.
  - KMVV's angle freedom (quoted, RH/CITATIONS.md) makes (6.23) valid on |ph ζ| < π − θ_L ⊇ |ph ζ| ≤ π/6 + π/24. OK.
- Sector check: ζ = N²f(z) ≈ N²f′(0)τe^{5πi/6} gives ph ζ ≈ −π/6. That is in KMVV (6.23)'s |arg ζ| < 2π/3 (quoted
  verbatim in RH/CITATIONS.md), with u = 2ζ^{1/2} and |ph u| ≤ π/12 + π/48 < π/3. Only I_α, K_α enter, with no Hankel
  functions. OK.
- p = 1:
  - f′(0) = πψ(0) > 0 (KV (5.7)–(5.8)), so ph ζ ≈ 3π/8 ∈ (π/4, π/2) = KV/Vanlessen sector II.
  - Lips at ±π/4, ±3π/4; iℝ is not a jump (RH_p1_general §5).
  - w = ζe^{−πi/2} has ph ≈ −π/8. OK.
- Scales:
  - τ = M^{−p} ↔ X_k < τ ⇔ k > MN.
  - |u| = 2N|f|^{1/2} ≍ N√τ, which is ≍ 1 at M ≍ N^{2/p}.
  - p = 1: Z_k = √(n/k) (t = n/Z²), ρ_M ≍ M^{−1/2}, |ζ| ≍ nη ≍ 1 at M ≍ n².
  - The crossover M_B = n^{2/p} is right in both cases.

**Row product (p ≠ 1).**
- Ê = D_{w,∞}^{−σ₃}Ẽ_N = N₀(W̃/D_w)^{σ₃}Mf^{σ₃/4}(2πN)^{σ₃/2}. This uses N = D_{w,∞}^{σ₃}N₀D_w^{−σ₃}. OK.
- (2πN)^{σ₃/2}σ₃Ψσ₃ written out gives exactly the displayed two entries:
  - √(2πN)[r₁I_α − r₂(i/2N)uI′_α];
  - √(2πN)[−r₁(i/π)K_α − r₂uK′_α/(2πN)].
- So |S_N| ≤ CN·P_α(u; 1/N). OK.
- Denominator:
  - (N₀)₁₂ = (a − a^{−1})/(2i), with a = (1 − 4c/z)^{1/4}, so a − a^{−1} = −2c/z + … and (N₀,₁)₁₂ = ic. The Szegő diagonal
    factor is I + O(1/z), so (Ñ₁)₁₂ = ic.
  - With (𝒵₁)₁₂ = O(1/N) (RH_px §5), |(Ṽ₁)₁₂| ≥ c/2. OK.
- p = 1: (N₁)₁₂(N₁)₂₁ = (i)(−i) = 1 for the band [−2, 2], and the Szegő conjugation preserves the product. OK.

**Lemma Z.**
- Representation: 𝒵 = I + C(𝒵₋(J − I)), with ‖J − I‖_{L¹∩L²∩L^∞} and ‖𝒵₋ − I‖_{L²} = O(1/N). This is RH_px §5, RH₁(r)
  §7 and RH_plt1b "everything else".
- Near part: Cauchy–Schwarz with |s − z| ≳ |s| + |z| (angular separation ≥ π/8).
- p ≠ 1:
  - Lemma 4.3 gives |J_H − I| ≤ C_KN^{−K}min(1, |s|^K). I re-derived that exp(−cN|s|^{−1/p})·poly(N, |s|^{−1})e^{CN|s|^{1/2}}
    is ≤ C_KN^{−K}|s|^K. Put t = N|s|^{−1/p} ≥ cN; super-exponential decay beats every power of |s|^{−1} and N.
  - The D_{w,∞} conjugation costs only poly(N). OK.
- p = 1:
  - With Lemma M's n^{−1}min(1, (n|s|)^δ), ‖(J − I)/|s|‖²_{L²} = n^{−2}[n/(2δ − 1) + n] = O(1/n). OK.
  - (J2) terms are e^{−cn/|s|²}·poly, harmless.
  - Only |𝒵 − I| ≤ ½ is used later. OK.
- Domain slip: F3.

**Lemma A.**
- Maximum principle:
  - Ẽ_N = E^a + Φ, with Φ = O(e^{−c′N}) on the whole disc, so A = A^a + O(N^{1/2}e^{−c′N}).
  - Bounding A on |z| = δ needs N₀ (bounded away from 0 and 4c, with boundary values at z = δ), f^{±1/4} (N, σ-free) and
    (W̃/D_w)^{±1}.
- Decomposition: the constants C_N^{1/2}h_N(0)^{1/2} cancel against the Szegő function of a constant. That leaves Q_x,
  Q_{4c} (N-free) and Q_{h,N}.
- N-uniform Hölder bound for log h_N − log h_N(0):
  - I re-derived (log B)′(x) ≤ C(x^{1/p−1}/N + N^{−p}) by splitting y ≤ N^p (where |ℓ̂(y)| ≤ C|y|^{1/p}/N, since ℓ̂ is a
    function of t = N|y|^{−1/p} that is O(1/t)) and y ≥ N^p.
  - This is a genuine improvement on RH_px Lemma 3.4's consequence, whose constant was not tracked in N. Correct.
- p < 1: the cited "X − X(0) N-uniform Lipschitz on compacts" (RH_plt1b §1) plus |ζ − x| ≳ |ζ| + x between the seams and
  the band gives N-uniform Lipschitz on [0, 4c]. D̃ and B_in are fine. OK.
- p = 1: Lemma B(iii) of RH₁(r) states exactly the boundedness of E_n and E_n^{−1}. OK.
- Minor: F9.

**Lemma BK** (every constant re-derived).
- Γ ≥ 0.8856 on (0, ∞), so 1/Γ ≤ 1.13. OK.
- The K small-argument integral uses the substitution v = re^t/2, giving (2/r)^{|ν|}∫_{r/2}^∞e^{−v}v^{|ν|−1}dv. Its bound
  log(2/r) + const is right, uniform for |ν| ≤ max(A, 1).
- K′: the bound (2/r)^{1+|ν|}Γ(|ν| + 1) is right.
- Large K: cosh t ≥ 1 + t²/2 gives e^{−r}√(2π/r)e^{A²/(2r)}. OK.
- Large I via 10.32.4: 1 − cos θ ≥ 2θ²/π² gives (1/π)e^r(π/2)(π/(2r))^{1/2} = e^r(π/(8r))^{1/2}. OK. The second integral is
  O(1) for r ≥ 1.
- Products:
  - small |u|: |u|^{ν−|ν|}(1 + log);
  - large |u|: 2C(1 + Λ|u|)²/r ≤ 4C(1 + Λ|u|)²/|u|, using r ≥ |u|/2 from |ph u| ≤ π/3. OK.
- Cosmetic: in the K bounds, "A" should be max(A, 1), since |ν| < 1 is possible for ν < 0. This is harmless.

**DLMF quotes (Rule C)**, checked against the live pages.
- 10.25.2: matches, including "corresponds to the principal value of (½z)^ν, is analytic in ℂ∖(−∞,0]" and the
  principal-value convention sentence.
- 10.32.4 and 10.32.9: match, both with |ph z| < ½π.
- 10.34.2: matches; m ∈ ℤ, with limiting values for integer ν.
- 10.27.8: matches, with both ph ranges.
- 10.40.10–12 match:
  - the variational-operator sentence is quoted correctly;
  - "π ≤ |ph z| < 3π/2" uses the corrected "<" (v1.0.11);
  - χ(ℓ) is correct;
  - no ν restriction.
- The 10.34.2 ⇒ I_ν identity in U5 (m = ±1) re-derived: I_ν(z) = ±(e^{∓νπi}K_ν(z) − K_ν(ze^{±πi}))/(πi). OK.
- The hypotheses as used are satisfied: |ph u| ≤ π/12 + π/48 (p ≠ 1) and ≤ π/8 + small (p = 1), both < π/3 < π/2.

**Derivation of (a), (b), (c), β.**
- p ≠ 1:
  - With y = N²τ = (N^{2/p}/M)^p and p(1 + α) = σ − 1:
    - |u| ≥ 2 ⇒ C√τ = CM^{−p/2};
    - |u| ≤ 2 ⇒ CN^{−1}y^{1+min(α,0)}(1 + log) = CN^{−1}(M/M_B)^{−min(p, σ−1)}(1 + log).
  - The overlap regions (|u| ≤ 2 with M < M_B, and |u| ≥ 2 with M > M_B) have M ≍ M_B, where both forms agree up to
    constants. This is implicit in the text, and fine.
- p = 1:
  - Vanlessen (4.27)'s rows have orders a + ½ (row 1) and a − ½ (row 2).
  - The worst cross term ζ^{1/2}I_{a−½}·ζ^{1/2}K_{a+½} (or K_{a−½} if a < 0) has exponent 1 + (a − ½) − max|a ± ½| = 2min(0, a).
  - So β = ½ + min(0, a) = min(½, σ − 1), with a = σ − 3/2 (RH_px Lemma 1.2 / RH_p1_general §1). OK.
- (c) for ϑ < ϑ(p, σ): n^{−1} ≤ n^{−2ϑ/p} because 2ϑ/p < 2β/p ≤ 1. Also n^{−2ϑ/p}(M/M_B)^{−ϑ} = M^{−ϑ}. OK in all cases.
- The endpoint ϑ = p/2: see F2.
- m = n − 1 via M′ = Mn/(n − 1): OK.
- τ > δ₁ (finitely many M): trivial bound. OK.

**Corollary QLP-Λ.** Σ_{k>n}log(k/n)μ(k) = Σμ(k)∫_1^{k/n}dM/M = ∫_1^∞μ((Mn, ∞))dM/M (Tonelli, indicator k > Mn)
≤ C_ϑ/ϑ. OK. This is Lemma QLb of §3.14 at t = 0 (QLb would give (1 + log C)/ϑ); cross-referencing it is optional. The
text correctly says this is the t = 0 slice only, and that QL along vΨ^t (t > 0) is not obtained.

**Fixed σ vs (RU).**
- Every constant (N₀, δ, δ₁, C_K, C_A, the BK constant via ν₀ = α or a − ½) is taken from the cited analyses at fixed
  (p, σ). The theorem's "C, C_ϑ, n₀ depend on (p, σ)" is honest.
- The outline's "uniformly in σ" is correctly downgraded to CONDITIONAL on (RU).
- U1–U4 and U7 are fine as a sketch. U5 is supported by the quoted 10.40.10–12.
- U6 has a gap: F6.

**Numerics.**
- Re-ran `check_qlp.py` from jacobi-asymptotics/.venv. The output is **byte-identical** to the committed `check_qlp.out`.
- All 18 runs: tail ≤ ST bound in every row; sup_{M≤M_B} tail·M^{p/2} ∈ [0.48, 0.71], flat in n.
- The deep slopes quoted in QLP4 match the output.

## Findings

**F1 (moderate; citation gate). Location:** §3.16 heading, §0 QLP row, LOG.md entry, "Proof, p = 1" ("WLXZ (4.27)
(quoted in RH/CITATIONS.md …)").
- **Issue:** the sector-II I/K formula is **Vanlessen math/0212014 (4.27)**, quoted under "(Van)" in RH/CITATIONS.md.
  WLXZ (4.27) is a different equation of a different paper. The labels therefore cite a non-existent dependency.
- **Fix:** replace "WLXZ (4.27)" by "Vanlessen (4.27)" everywhere (heading, §0, LOG, proof). Keep WLXZ only where WLXZ's
  chain (3.11)/(4.1) is meant (the Application paragraph).

**F2 (moderate; overclaim in a sub-statement). Location:** Theorem QLP (c), "if σ − 1 > p/2 this holds with ϑ = p/2
itself", and the proof of (c) ("(c) as before" for p = 1).
- **Issue:**
  - For p ≠ 1, σ − 1 > p/2 gives β = min(p, σ − 1) > p/2 strictly, which absorbs the log. Correct.
  - For p = 1, β = min(½, σ − 1) = ½ = p/2 exactly when σ > 3/2. Then (b) gives only CM^{−1/2}(1 + log(M/n²)) beyond the
    Bessel scale. The log is **not** absorbed, so ϑ = p/2 is not proved for p = 1.
  - It is very likely true: for a ∉ {±½} the log in Lemma BK is unnecessary, and for a = ½ the K₀ factor never meets the
    worst-exponent term. But that refinement is not in the text.
- **Fix:** either restrict the endpoint clause to p ≠ 1, or add the order-by-order refinement (for fixed σ, the log is
  needed only for a K-order equal to 0, and the term with exponent 2min(0, a) = 0 is I_{a−½}K_{a+½} with a + ½ > 1).
  Corollary QLP-Λ is unaffected (it uses ϑ < ϑ(p, σ)).

**F3 (minor; domain slip). Location:** Lemma Z, statement vs "Far part".
- **Issue:** the statement is for 0 < |z| ≤ δ₁, but the far-part estimate assumes |z| ≤ δ₁/2.
- **Fix:** state Lemma Z for |z| ≤ δ₁/2 (and use τ ∈ (0, δ₁/2] in the proof of QLP, trivial bound above). Or note that
  the angular separation makes |s − z| ≳ |s| + |z| also for s ∈ Σ ∩ (U(0, δ) ∖ U(0, δ₁)).

**F4 (minor; numerics labelling). Location:** `checks/check_qlp.py`, function `run` (beta = min(p, s − 1) for every p),
and hence the p = 1 lines of `check_qlp.out`.
- **Issue:**
  - For p = 1 the theorem's exponent is β = min(½, σ − 1). The script prints "proved bound exponent −β = −1.000" for
    p = 1, σ ∈ {2, 3}; the proved value is −0.5.
  - The r2 column at p = 1 also uses the wrong β.
  - The quoted numbers in QLP4 are unaffected, but the .out file mislabels the theorem.
- **Fix:** `beta = min(0.5, s-1) if p == 1 else min(p, s-1)`, and regenerate the .out.

**F5 (minor; numerical evidence overstated). Location:** QLP3(ii), "tail·n·(M/M_B)^{1/2} grows slowly, 0.38 → 1.16 over
M ∈ [2⁸, 2¹⁷], consistent with the log factor in (b)".
- **Issue:**
  - At n = 6, M_B = 1296, so the first three grid points (256, 512, 1024) are below the Bessel scale.
  - Beyond M_B the ratio goes 0.79 → 1.16 over 6 doublings while log(M/M_B) goes from 0.5 to 4.6. That looks more like
    pre-asymptotic saturation than a log.
  - Also, p = 2, σ = 3 has α = 0 too and shows a clean slope −2.000 with no visible log.
- **Fix:** reword to "not inconsistent with (b); the log is a proof artefact at α = 0 and is not resolved by these runs".
  Drop "consistent with the log factor".

**F6 (minor; Audit U). Location:** Audit U, U6.
- **Issue:**
  - U6 claims the RH₁(r) Lemma M amplification constant is a-uniform "by Lemma BK (ρ ≤ 1)".
  - Lemma BK covers only |ph u| ≤ π/3. Lemma M needs the amplification on the band rays (ph ζ = 0, π; sector I uses Hankel
    functions of ζ, or equivalently w = ζe^{−πi/2} with |ph w| = π/2) and on the lips.
  - Small-argument bounds there need the connection formulas (10.27.8, 10.34.2), uniform in order. Plausible, but not
    what BK proves.
- **Fix:** say so in U6 (BK's small-argument part extends to |ph u| ≤ π via the series for I and 10.34.2 for K; not written
  out). (RU) stays CONDITIONAL, so this is a disclosure fix.

**F7 (minor; wording). Location:** Lemma Z, p = 1 bullet.
- **Issue:** it cites Lemma M's bound n^{−1}min(1, (n|s|)^δ). That is the "(J1)" part. The (J2) lip terms are separately
  O(n^{−K}) with e^{−cn/|s|²} decay at 0.
- **Fix:** add "(J2) terms are O(n^{−K}e^{−cn/|s|²}·poly), harmless" for completeness.

**F8 (polish). Location:** Lemma GS, last paragraph, and "Application".
- **Issue:**
  - "analyticity of V₁₁ at ∞ makes m analytic there" is unnecessary; only C₁/m(z) → C₁² as z → ∞ is used.
  - The "invariances" are applied to a factorization V = 𝒵P₀ at the single point z, with the denominator always taken from
    the true V.
- **Fix:** state that explicitly to avoid the reading that P₀ itself is normalized at ∞.

**F9 (polish). Location:** Lemma A proof.
- **Issue:** the maximum principle needs A^a continuous on the closed disc |z| ≤ δ. Ẽ_N's band-jump cancellation holds
  where f is defined (a disc slightly larger than U(0, δ)).
- **Fix:** run the argument on |z| = δ′ < δ, or say "f is analytic on a neighbourhood of the closed disc". In Lemma BK, use
  max(A, 1) in the K bounds.

## Recommended labels (after fixes)

- **Lemma ST, Lemma GS:** PROVED.
- **Lemma BK:** PROVED-mod-cite (DLMF 10.25.2, 10.32.4, 10.32.9; quotes verified verbatim, Rule C satisfied).
- **Lemmas Z, A:** PROVED-mod-cite (RH_px Lemmas 4.2–4.3 and §5; RH₁(r) Lemmas B, M and §7; RH_plt1b §§1–2).
- **Theorem QLP (a), (b), and (c) for ϑ < min(p/2, σ − 1); Corollary QLP-Λ:** PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b;
  KMVV (6.23); **Vanlessen (4.27)**; KV (5.21)–(5.22) as a consistency check only) for each fixed σ.
  - The endpoint ϑ = p/2 is PROVED for p ≠ 1 only, unless F2's refinement is added.
- **Uniformity in σ on compacts:** CONDITIONAL on (RU). Audit U: PROOF SKETCH (with the F6 disclosure).
- **QL for t > 0:** still HYPOTHESIS; no new case of the law. Correctly stated.
- **Novelty:** UNCHECKED.
- Once F1–F4 are applied (F5–F9 optional), §3.16 may be marked "Rule R ACCEPT WITH FIXES (review/REVIEW_Plan46.md) —
  REVIEWED".
