# Second referee report: Paper 2, revision 1 (commit d844b18)

Reviewer: second AI referee, independent of the first (REFEREE_REPORT.md). This is not a human Rule R reading.

**Scope.** The text reviewed is the committed revision d844b18, read from `git show d844b18:...` where it mattered.

**Concurrent edits.** While this review was running, another agent made uncommitted edits in the same worktree. Up to 13
files were modified, among them sec_2–sec_8, sec_front and app_a. I checked the diffs of sec_5, sec_6 and sec_7. They
are editorial:
- renaming Θ, M to 𝔠, 𝔐 in Lemma 6.3;
- moving the DLMF Airy quotes into T4;
- deleting the `airy_check` sentence and Remark `rem:frame`;
- shortening §7 prose.

None of these edits changes a finding below. Line references are to d844b18.

**Numbering in the compiled PDF (main.aux).** Several numbers differ from those used in the task and in the first report:

| Object | Number in the PDF |
|---|---|
| Szegő lemma | Lemma 6.3 (the task's "Lemma 6.6(vi)(b)" is Lemma 6.3(vi)(b)) |
| Airy lemma | Lemma 6.6 |
| Lip lemma | Lemma 5.6 |
| Signs lemma | Lemma 5.5 |
| Lip mismatch | Lemma 7.3 |
| Remark on α ≥ 1 | Remark 7.8 |

The appendices print in the order of `\input`:

| Printed | Content | Source file |
|---|---|---|
| A | outer scalar | app_outer |
| B | a priori bound | app_c.tex |
| C | power-weighted Cauchy bounds | app_a.tex |
| D | uniform resolvent | app_b.tex |

So the task's "App. B" is printed **Appendix D**, its "App. C" is printed **Appendix B**, and "Cor C.4" is printed
Cor. B.4.

## Recommendation

**Minor revision.** I found no critical or major issue.

The first referee's MAJOR item F1, that the Airy parametrix was asserted only by reference, is now fully resolved. I
re-derived everything in Lemma 6.6 by hand and checked it independently with my own numerics:
- the model;
- the four sector matrices and their jump relations;
- the determinant;
- the large-ζ form in all four closed sectors, including the sector boundaries;
- N_r = M and the branch of (−ω)^{1/2};
- analyticity and removability of A_r;
- exactness of the (F1) jumps;
- the O(1/n) matching;
- the two-scale structure.

Appendix D (dense class, linearity from uniqueness, Lemma D.1(c)) and Appendix B were read in full and are correct.

The F3 sign claim agrees with the WLXZ v1 PDF: Fig. 3 and (4.12), checked by rendering the PDF text.

The findings below are bookkeeping gaps in parameter ranges and statement scopes, a lens-construction detail, and
repository hygiene. Each has a one-line fix.

## Numbered findings

### G1 (MINOR) — (O3) is posited on too small a disc for its uses
**Location.** §5.9 (O3)–(O4), "η₀ ∈ (0, δ] is fixed". It is used in (F2), in Lemma 6.3(ii) via (vi)(a), and in Lemma 7.3
("the factor H°_n").

**Issue.** (O3) gives the bounds |log H_n − log H_n(0⁺)| ≤ C|z|^{ν_p} and |(log H_n)′| ≤ C|z|^{ν_p−1} only for |z| ≤ η₀ ≤ δ.
Two places need more:
- Lemma 6.3(ii) is applied to q = H°_n with hypotheses on all of Z(η_*), where η_* = min(1, 2c) may exceed δ. These
  include the derivative bound, which Step "𝒰_z" uses on segments reaching |w| ≤ (3/2)|z|.
- (F2) asserts both bounds for |z| ≤ 1 and cites only (O2)–(O4).

For η₀ ≤ |z| ≤ 1 the value bound follows from (O4). The derivative bound does not follow from it. A Cauchy estimate
would also not give it up to the edge |arg z| = ϑ_w of Z_n, which has the same angle.

All three constructions in fact prove (O3) on |z| ≤ 1: Lemma 6.1 for p = 1, and App. A for p > 1 and for p < 1, each
stated as "for z ∈ Z_n, |z| ≤ 1". So nothing is false.

**Fix.** Replace "η₀ ∈ (0, δ]" by η₀ = 1. Equivalently, state (O3) for z ∈ Z_n with |z| ≤ 1.

### G2 (MINOR) — Missing constraint that U(4c, 4ε) ⊂ Z_n
**Location.** Lemma 6.3(vi)(b) and the parameter list after Lemma 5.6.

**Issue.**
- (vi)(b) is stated on U(4c, 2ε) and proved through (iv) with ε₁ = 2ε. That needs log q₁ = log(x^α H°_n r_n)
  analytic and bounded on U(4c, 4ε).
- H_n and r_n are only known to be analytic on Z_n = {|arg z| < ϑ_w, …}. So one needs 4ε < 4c·sin ϑ_w.
- The stated constraints are ε < h₀ ≤ ½δ tan ϑ_w and δ ≤ c/2. These give ε < (c/4)tan ϑ_w. For p ≥ 1
  (ϑ_w = 7π/16, tan ϑ_w ≈ 5.03) this does not imply ε < c·sin ϑ_w.
- The constraint holds only implicitly, if ε₀ (Lemma 5.5(iv)) happens to be small.

**Fix.** Add ε < c·sin ϑ_w (or "ε₀ ≤ ½c sin ϑ_w" in Lemma 5.5(iv)) to the parameter list.

### G3 (MINOR) — Lemma 5.6(a) versus corner rounding at z₁
**Location.** Proof of Lemma 5.6: "round the three corners inside G₊".

**Issue.**
- Statement (a) says that Σ_lip ∩ U(0, δ) is *exactly* the f-preimage of a ray segment.
- The first piece ends at z₁ on |z| = δ, where it meets the radial second piece at an angle.
- Rounding that corner in a neighbourhood of z₁ changes the lip inside U(0, δ), which breaks (a).
- (a) is what (F3) and the Bessel comparison use, so the rounding has to happen outside.

**Fix.** Take the first piece to be the preimage of the ray inside U(0, 2δ). Since δ ≤ δ₁ ≤ r_*/2, it still lies in S₀.
Join it to the second piece and round the corner in {δ < |z| < 2δ}. Two further nits:
- (F1) says Σ ∩ U(0, 2δ) is n-independent. That remains true.
- Choose r_* < δ₀ strictly, since eq:retvphi-zero (Lemma 5.5(iii)) is stated on the open disc U(0, δ₀).

A second nit in the same proof: the condition "arg(4c + ih₀) < ϑ_w" does not bound the maximal argument on the arc
{4c + h₀e^{iϑ}}. That maximum is arcsin(h₀/4c) > arctan(h₀/4c). The correct condition, arcsin(h₀/4c) < ϑ_w, also holds
for small h₀.

### G4 (MINOR) — `airy_check.py` is useful but partly tautological; its output is not committed
**Location.** papers/paper2/checks/airy_check.py; CITATIONS.md "(DLMF-9, Paper 2)" ("Numerical check: … (.out)").

**Assessment.** I re-ran the script with the jacobi-asymptotics venv in 3.6 s. The output is identical to the stored
`airy_check.out`:
- jump residuals ≤ 1.2·10⁻²⁴ on the band, the saturated segment and both vertical segments;
- det − 1 ≤ 2·10⁻³⁰;
- A_r band jump 5·10⁻²⁶;
- n·sup|P̂_r P₀^{−1} − I| converging to 3.05 for n = 10…2560.

What the script does test:
- the four explicit column formulas against the jump relations (eq:airy-relations);
- the four jumps of P̂_r with the paper's region labels and orientations;
- det ≡ 1;
- M J M⁻¹ = diag(−i, i);
- (−ω)^{1/2}₊(−ω)^{1/2}₋ = 1;
- no band jump of A_r;
- the O(1/n) matching.

What it does not test:
- (a) It sets φ̃ := −(2/3)f_r^{3/2} by fiat, so the identity (2/3)ζ^{3/2} = −nφ̃ that drives (iii) is tautological
  there. The real content of that identity is Lemma 5.5(iv), which is proved analytically and which I checked.
- (b) The model ω = (4c/Υ)e^{R·g} has the structure of Lemma 6.3(vi)(b) by construction. The check therefore says
  nothing about whether the true ω has that structure. That is (vi)(b), checked by hand below.
- (c) The large-ζ form (eq:airy-infty) uniformly in the closed sectors S_j, including the edges 5π/12, 7π/12 and ±π,
  is tested only through 13 points on one circle.
- (d) The two-scale bounds of part (iv) are not tested.

I covered (c) with my own script (scratchpad `airy2.py`, not committed). On all four sectors, at 9 angles including the
boundary rays and for R = 10, 40, 160, sup|ζ^{σ₃/4}Ψ^j e^{−(2/3)ζ^{3/2}σ₃} − M|·R^{3/2} → 0.103. This confirms the
O(|ζ|^{−3/2}) error with the stated M in every sector. Relations and determinants agree to 10⁻⁴⁰.

The script is adequate as a NUMERICAL sanity check of the algebra (Rule N). The analytic proof stands on its own.

**Repo hygiene.** `papers/paper2/.gitignore` contains `*.out`, which is meant for LaTeX. It also ignores
`checks/airy_check.out`, `checks/table2.out` and `checks/lommel_check.out`. CITATIONS.md and NOTES §5/§7 refer to these
files as artefacts to compare against from a clean checkout.

**Fix.** Un-ignore `checks/*.out` (`!checks/*.out`) and commit the outputs. If the `airy_check` sentence is restored
(the concurrent edit removed it), state (a) and (b) as limitations.

### G5 (MINOR) — Remark 7.8 (uses of |α| < 1): complete for the essential uses; two harmless uses are unlisted
**Location.** Remark 7.8 (`rem:alpha-ge-1`).

**Issue.** I traced every place where α appears: §§5–8, App. B, App. D and Lemma 7.1. The three listed uses are the
essential ones:
- (a) L² at the hard edge;
- (b) |β| = |α|/2 < ½ in Lemma C.1;
- (c) integrability of |ζ|^{−|α|}.

The following uses are not listed:
- App. D Step 1 and Step 5: the vertex condition ρ^{1−|α|/2} → 0. This needs only |α| < 2, so it is weaker than (a).
- Proof of Prop. 7.6, Δ₃ on the lips: the bound |Q̃₋^{±1}| ≤ Cn^{1/2}|z|^{−1/2} uses |α| ≤ 1. The super-exponentially
  small |E| makes any power harmless.
- Lemma 7.1 is stated for α ∈ (−1, 1). Its part (i) only needs α ∉ ℤ. This is a statement scope, not a use.
- App. B Lemmas B.1–B.2 use only α − η > −1, that is s > 1.

None of these is a hidden essential use. The sentence "nowhere else" is correct in substance.

**Fix (optional).** Change it to "…and nowhere else in an essential way (the vertex conditions in Appendix D need only
|α| < 2)".

### G6 (MINOR) — Stale numbering comments and appendix order
**Location.** main.tex line 11 and the header of sec_4.tex.

**Issue.**
- Both say "Corollary 1.4". The printed number is **Corollary 1.6**. These are comments only.
- Appendix B (Cor. B.4) depends on Lemma D.1(c) of Appendix D, a forward reference across appendices. Appendix D in turn
  uses Appendix C.
- The first report's "App. B/C" letters (and its "App. D") refer to the pre-revision order.

**Fix.** Update the comments. Consider the order A (outer), C→B (L² bounds), D→C (resolvent), B→D (a priori), or move
Lemma D.1 into its own short section. Tell readers of REFEREE_REPORT.md that its appendix letters are pre-revision.

### G7 (MINOR) — Abstract: "If ℓ extends analytically to a sector, the error is O(1/n)"
**Issue.** (A_ϑp) requires more than an analytic extension:
- boundedness near |t| = e^{−c₀};
- tℓ′(t)/ℓ(t) → 0 uniformly in the sector, i.e. ε_Λ → 0, which is slow variation inside the sector.

The sector half-width is also specific (π/p, or π/2). An analytic extension without these properties does not
qualify; for example, ℓ(t) = 2 + sin(log t) is analytic on a sector but tℓ′/ℓ does not tend to 0.

**Fix.** Write "If ℓ extends to a slowly varying analytic function on a sector (Definition 1.2), …".

### G8 (process) — Rule C: the WLXZ Fig. 3 check
The first report asked a human to confirm the region correspondence in WLXZ Fig. 3. I fetched arXiv:1410.3948v1, PDF,
24 pp, and extracted it with `pdftotext -layout`:
- Fig. 3 places Ω^△_{l,+} upper left, Ω^△_{r,+} upper right, Ω^△_{l,−} lower left and Ω^△_{r,−} lower right.
- (4.12) reads "−V^△₋(z), z ∈ Ω^△_{l,+} ∪ Ω^△_{r,−}", matching the corrected transcription in RH/CITATIONS.md.

**Fix.** Record in CITATIONS.md that Fig. 3 was read from the v1 PDF (text layer). A visual check of the figure is
still advisable, since the layout came from the text layer rather than the image.

## Verified steps (independent re-derivation)

### (1) Airy parametrix (§6 "The soft edge", Lemma 6.6)
- **DLMF quotes.** I fetched dlmf.nist.gov/9.2 and /9.7 on 2026-10-15. The quotes in CITATIONS "(DLMF-9, Paper 2)" match
  verbatim:
  - "All solutions are entire functions of z";
  - (9.2.8) 𝒲{Ai(z), Ai(ze^{∓2πi/3})} = e^{±πi/6}/(2π);
  - (9.2.12);
  - "Here δ denotes an arbitrary small positive constant";
  - "As z→∞ … valid uniformly in the stated sectors";
  - (9.7.1), (9.7.2) u₀ = v₀ = 1;
  - (9.7.5)–(9.7.6) with |ph z| ≤ π − δ.

  The DLMF states no branch convention beyond the sector condition. The registry's "(principal, by DLMF's general
  convention)" is an interpretation and is correct.
- **Relations.**
  - y₀ + q⁻¹y₊ + q y₋ = 0, from (9.2.12) and its derivative.
  - Hence y₊ + q y₀ = −q⁻¹y₋. All four relations in (eq:airy-relations) follow by hand: Ψ^{II} = Ψ^I U, Ψ^{II} = Ψ^{III}J,
    Ψ^{IV} = Ψ^{III}U and Ψ^I = Ψ^{IV}L, with U = [[1,1],[0,1]] and L = [[1,0],[−1,1]].
  - det Ψ^I = k²q·det(y₊, y₀) = −k²q·𝒲{Ai(ζ), Ai(q⁻¹ζ)} = −e^{iπ/3}e^{2πi/3} = 1.
- **Large ζ.**
  - On S_I ∪ S_II: (q⁻¹ζ)^{1/4} = e^{−iπ/6}ζ^{1/4} and (2/3)(q⁻¹ζ)^{3/2} = −ξ.
  - On S_II: (qζ)^{1/4} = e^{−iπ/3}ζ^{1/4} and (qζ)^{3/2} = ζ^{3/2}. This uses arg ζ ≥ π/3, which holds since S_II starts at
    5π/12.
  - The arguments used stay in |ph| ≤ 11π/12: S_I gives [0, 7π/12] and [−2π/3, −π/12]; S_II gives [−π/4, π/3] and
    [−11π/12, −π/3].
  - k_{Ai}e^{−iπσ₃/4}(2√π)⁻¹[[e^{iπ/6}, q], [e^{iπ/6}, −q]] = M.
  - The S_II column −q⁻¹y₋ has the same leading vector q(1, −1) as q y₀.
  - The error is O(|ζ|^{−3/2}) = O(ξ^{−1}), and on 1 ≤ |ζ| ≤ R₀ it holds by compactness.
- **Geometry.**
  - In U(4c, ε) the only arcs are the band, (4c, 4c+ε) and the straight segments Σ_v^±. This needs ε < h₀ (Lemma 5.6(c)).
  - So the components I–IV are the quarter discs, and |arg f_r − arg(z−4c)| ≤ π/12 gives ζ ∈ S_j.
  - f_r maps ℂ_± ∩ U into ℂ_± (univalent, real exactly on ℝ, f_r′ > 0).
- **Jumps.**
  - Σ_v^+ upward: + side II, − side I.
  - Σ_v^− downward: + side IV, − side III.
  - (4c, 4c+ε): + side I, − side IV.
  - Band: + side II, − side III.
  - h^{−σ₃}Uh^{σ₃} = [[1, h^{−2}], [0, 1]], with h^{−2} = −ω⁻¹e^{−2nφ̃}.
  - h^{−σ₃}[[1,0],[−1,1]]h^{σ₃} gives the (2,1) entry −h² = ωe^{2nφ̃}.
  - h₊^{σ₃}Jh₊^{σ₃} = J.
  - Since the Ψ^j are entire and ζ is analytic across the band, both sides evaluate at the same ζ. This is the advantage of
    sector matrices that are entire.
  - h has no jump off the band, because φ̃ has no jump on (4c, ∞) and (−ω)^{1/2} has a cut only on the band.
- **Branch (−ω)^{1/2} and Lemma 6.3(vi)(b).**
  - D_{4c−x}²/(4c−z) = −4c/Υ.
  - L₁ = 2E − log q₁(z), with E the Szegő exponent. Since E₊ + E₋ = log q₁ on the band (I₊ − I₋ = −2πi·density) and log
    q₁ is analytic near 4c, L₁₊ + L₁₋ = 0.
  - Hence (−ω)^{1/2}₊(−ω)^{1/2}₋ = 4c/((√x + i√(4c−x))(√x − i√(4c−x))) = 1. Also −ω(4c) = 1, so ω(4c) = −1, and the
    root is positive on (4c, 4c+2ε).
  - The paper's remark that a branch of ω^{1/2} continuous across (4c, 4c+ε) would give product −1 is correct.
- **A_r.**
  - f₊^{1/4}/f₋^{1/4} = i on the band.
  - M J M⁻¹ = diag(−i, i), computed by hand.
  - Using JD = D⁻¹J, the band jump cancels exactly as displayed.
  - |A_r| ≤ C|z−4c|^{−1/2}, so the singularity is removable.
  - det A_r = 1.
  - The maximum principle on |z−4c| = 3ε/2 applies, inside U(4c, 2ε₀).
- **Matching.** (n^{2/3}f_r)^{3/2} = n f_r^{3/2} and (n^{2/3}f_r)^{−1/4} = n^{−1/6}f_r^{−1/4} hold for principal powers
  (n^{2/3} > 0). Lemma 5.5(iv) gives φ̃ = −(2/3)f_r^{3/2}, fixed by negativity on (4c, ∞). Together these give
  P̂_r(P₀^∞)⁻¹ = I + O(1/n), uniformly in n via (vi)(b).
- **Two scales.**
  - Θ_∞ = ζ^{σ₃/4}Ψ_r e^{−(2/3)ζ^{3/2}σ₃}(−ω)^{σ₃/2}.
  - Θ₀ = S_j h^{σ₃}, with the S_j listed correctly.
  - |e^{±nφ̃}| ≤ e^{(2/3)·3^{3/2}} = e^{2√3}.

### (2) Lemma 5.5(iii) and Lemma 5.6
- **eq:retvphi-zero.**
  - φ̃ = −iπ + iπz^{1/2}𝔞(z) + iπz^{−1/p} in ℂ₊, so Re φ̃ = πr^{−1/p}sin(ϑ/p) − π Im(z^{1/2}𝔞).
  - |∂_ϑ(z^{1/2}𝔞)| = |z(z^{1/2}𝔞)′| ≤ Cr^{1/2}.
  - sin(ϑ/p) ≥ (2/π)ϑ/p needs ϑ_w/p ≤ π/2, which holds in all three geometries.
- **Lemma 5.6 construction.** The order δ → h₁(δ) → h₀ → ε is consistent. The dependence of h₁ on δ enters only through
  "ϑ < arg z₁".
  - First piece: angle ϑ_lip, and the ¾–5/4 band holds for small δ₁.
  - Second piece: lies in S₀.
  - Third piece:
    - on K it lies in G₊, since y₁ < h₀ ≤ y_K;
    - the near-4c part lies in U(4c, ε₀), since y₁ < h₀ ≤ ε₀/2;
    - arg(z−4c) ≥ 11π/12 follows from y₁/x′ ≤ tan(π/12), which gives arg f_r ≥ 5π/6.
  - Fourth piece: arg f_r ∈ [5π/12, π).
  - Property (c) holds.
  - (F5) "lips outside U(0, δ)": compactness applies, including the endpoint 4c + ih₀.
  - G3 is the only gap.
- Lemma 5.8 (Potter in the sector)(iii): the path argument with T = log n − (1/p)log R is correct.

### (3) Appendix D (resolvent; task's "App. B")
- **Lemma D.1.**
  - (a): shell sum.
  - (b): Cauchy–Pompeiu, with the orientation of ∂D₊ and the continuity of Ω.
  - (c): Cauchy's formula on U(0, R) minus Γ minus small discs. The + side is on the left, Γ is bounded for fixed n, and
    L² ⊂ L¹.
- **Lemma D.2 (block).**
  - Weights: for |ζ| ≥ 2, |t^{σ₃/4}ζ^{−σ₃/4}Θ| = |f₀^{−σ₃/4}Θ| ≤ C|f₀|^{−1/4}; the |ζ| < 2 case is also checked.
  - ∫𝔚² ≤ C uses the t^{−1/2} factor and 2|β| < 1.
  - Step 1: Cauchy estimates for 𝒜 on U(z₀, r₁) from bounds on U(z₀, r₀).
  - Step 2: the k₀ kernel.
  - The partition of (ζ′, ζ) pairs is a genuine partition. Overlap B≤3 × B≤3 ∩ B≥2 × B≥2 = B₂,₃ × B₂,₃ is subtracted
    once.
  - Separated parts: kernel bounds |ζ|^{−3/4} with ∫|ζ|^{−3/2} < ∞.
  - The soft-edge instance (t_n^{σ₃/4} = n^{σ₃/6}, P = I, Â = Ψ^I entire with det 1) satisfies (B1)–(B3) by Lemma 6.6(i),
    (iv). Distinct tangents at 4c hold (angles 0, ±π/2, π), and the circle ∂U(4c, ε) is excluded since U is open.
- **Proof of Prop. 7.4.**
  - Step 0: blocks; the distance from Σ ∖ Σ_loc to Σ_∘ is ≥ min(δ, ε).
  - Step 1 (fixed n): L² holds iff |α| < 1; the vertex condition holds; Q̃ = P₀^∞ = I + O(1/z).
  - Step 2: linearity follows from uniqueness. Two solutions of (R1) for the same 𝔤 differ by a homogeneous solution
    in ∂𝒞(L²), which is 0 by (R2). So 𝔣 ↦ μ is linear and bounded on 𝒟.
    - The right inverse by continuity is valid, since 1 − 𝒞_ṽ is bounded.
    - Injectivity holds: m := 𝒞(μ(ṽ−I)) gives m₋ = μ and m₊ = μṽ.
    - Step 3 uses only Step 1, so there is no circularity. The order fix requested in first-report F7 is implemented.
  - Step 4:
    - Σ_A ∪ Σ_B ∪ Σ_R covers Σ̂.
    - The third block is 1_R T 1_R − 1_{R∩A}T1_{R∩A} − 1_{R∩B}T1_{R∩B}, with R∩A and R∩B disjoint.
    - Remaining pairs are ≥ ¼min(δ, ε) apart. The Hilbert–Schmidt (HS) bound covers both cases: the other point on Σ_R
      (bounded Q̃, ∫|s−z|^{−2} ≤ 4C_Σ/t), or the other point in the other disc (product of L² norms).
    - Q̃ is bounded on Σ_R, including ½ε ≤ |z−4c| ≤ ε via (B2), since |f_r| ≥ ε/C.
  - Step 5: |m| ≤ C_n|Q̃| near the vertices.
  - Final bound: ‖ṽ − I‖_∞ is uniformly bounded.
- **Merged Cor. B.4.** It applies Lemma D.1(c) to Q − I correctly, with η = (1−|α|)/4 and (1+|α|)/4 < ½. The fixed-n
  boundedness of Γ = Σ is stated.

### (4) Appendix B (a priori bound; task's "App. C")
- **Lemma B.1.**
  - |z − X| ≥ sin φ₁·max(|z|, X) for |arg z| ≥ φ₁.
  - Both sums are checked, with t_z^{1+p−s} = n^{1+p−s}|z|^α and |z|⁻¹t_z^{1−s} = n^{1−s}|z|^α.
- **Lemma B.2.**
  - R_{j2} = U_{j2} − 𝒦_j, since e^{−2iθ}κ₊ = 1/(e^{2iθ} − 1).
  - Residues equal wU, from W = 2iθ′w.
  - The residue theorem gives (eq:R-contour) with the correct sign.
  - Upper ray: |e^{2iθ}| is large in ℂ₊.
  - Lower ray: the decomposition is −1 − e^{2iθ}/(1 − e^{2iθ}), and the integral bound holds for both signs of α − η.
  - Arcs with |t| ∈ ℕ + ½: if |v| < ¼ then |u| is at distance ≥ ⅜ from ℤ (|t| − |u| ≤ v²/|t| ≤ ⅛), and the |v| ≥ ¼ case
    holds.
  - r → 0 limits.
- **Prop. B.3.**
  - Outside the lens: column bounds and (1+|z|^α)|z|^{−α/2} ≤ 2|z|^{−|α|/2}.
  - In the lens: the e^{nφσ₃}A_± product and the three-η bookkeeping.
  - Near 4c: (F̃D_W)² = w_n z^α r_n ω.

### (5) The §7 restructure
- Lemma 7.3 uses Lemma 6.3(i)–(iii) correctly. With R = max(4c, 1), the path from x ∈ (0, 4c) to z′ ∈ Z(η_*) stays in
  Re ξ ≥ T_n = log n − (1/p)log max(4c, 1), since η_* ≤ 1. The same T_n appears in Lemma 6.3(vi)(a).
- ε′_n: t^{2ν}n^{−2ν}(log 2 + 2 log n − 2 log t)e^{−t/C} ≤ Cn^{−2ν}log n.
- The Bessel-localisation integrals check out.
- The circle term Q̃₋Δ₂Q̃₋⁻¹ = Q̃_in Q̃_out⁻¹ − I. Clockwise circles put the + side outside.

### (6) F3 (§5.7)
- WLXZ θ = nπ/z² and the paper's θ = πn x^{−1/p} at p = 1 correspond under x = z² (orientation preserving).
- Ω^△_{l,+} lies in the second quadrant and Ω^△_{r,−} in the fourth (Fig. 3, v1 PDF). Both map into ℂ₋.
- WLXZ (4.12) puts −V^△₋ exactly there, matching the paper's minus sign in Ω^△₋.
- The rewritten sentence is accurate.

### (7) Thin sectors for p < 1 (Lemma 7.1, T2(b))
- Rays at ±(π − πp/4). The central formula (6.23) is used on |arg ζ| < π − ϑ_lip.
  - |ph 2ζ^{1/2}| ≤ π/2 − ϑ_lip/2, inside (10.40.1)/(10.40.3) for I_α, I′_α (|ph| ≤ π/2 − δ) with δ = ϑ_lip/2.
  - It is also inside (10.40.2)/(10.40.4) for K, K′ (|ph| ≤ 3π/2 − δ).
- In the thin sectors the Hankel formulas use arg(−ζ) ∈ (−ϑ_lip, 0), well inside the sectors of validity of the H^{(1,2)}
  expansions.
- The relation between the central and thin-sector formulas is a global connection identity. Its constant jump matrix
  therefore does not depend on where the ray is drawn. This is KMVV's angle freedom, quoted in CITATIONS.
- No sectorial constant changes. The O(ζ^{−1/2}) constants depend on ϑ_lip, which is fixed for each p.

### (8) §1 statements vs §4 and §8 assembly
- Theorem 1(i)–(ii), Corollary 1.6, Theorem 2 (shift) and Theorem 3 (engine) as printed are exactly what §4.4 Steps 1–5
  and §8 prove.
  - Step 1: s₀ ∈ (1, 1+2p).
  - Steps 2–3 give Thm 1(ii) and the Corollary.
  - Steps 4–5 give (eq:main-rate) and Thm 1(i).
- §8 coefficients: a = 1 − c/z − (3/2)c²/z², a⁻¹ = 1 + c/z + (5/2)c²/z², so 𝖻 = c² and 𝖺 = 2c.
- c(1) = ½ and c(2) = π²/16.
- (eq:forms) equivalence.
- Remark 4.6: α = 0 is forced for s ∈ 1 + p + pℕ₀.
- main.log has no warnings and no undefined references.

## What a human expert should still check
1. **Lemma 6.6 against the literature.** The construction differs from WLXZ (6.12)'s σ₂-conjugated form and is built
   directly from DLMF. A specialist should confirm that the normalisation ζ^{−σ₃/4}M(I + O)e^{+(2/3)ζ^{3/2}σ₃}, with
   lower-triangular jumps on (4c, 4c+ε), is the intended "left-of-band" orientation. I verified internal consistency, not
   conventions in the literature.
2. **Lemma 5.6.** The corrected lens (G3), and the exact parameter list after G1–G2.
3. **Appendix C** (Lemma C.1 power weights on curved stars, and the curvature errors). It underlies Lemma D.2 for both
   edges. This report did not re-read it line by line.
4. **WLXZ Fig. 3 image.** The image itself, not the text layer (G8).
5. **Rule R.** This is a second *AI* reading. A human reading of §§5–7 and Appendices B and D is still required before
   REVIEWED.
6. **Commit state.** The concurrent uncommitted edits (13 files at the time of writing) need their own diff review before
   the next commit. In particular, they delete the `airy_check` sentence and Remark `rem:frame`. No dangling `\ref`
   remained when I grepped.
