# Rule R review: Plan 66, reviewer A (Route C and the main theorem): E_p1.md, (E) at p = 1

Reviewer: independent second reader (Rule R), reviewer **A**. Reviewer B checks Route A (Lemmas E1.1–E1.6) separately.
- Branch `plan-66-E-p1`, commit 52e5980 (worktree ja-plan66).
- **Scope:** research/G1/RH/second_order/E_p1.md §3 (Lemmas E1.7a, E1.7b, E1.7, Prop E1.8, Thm E1.9), §3.5 (Thm E1.10),
  the Route C parts of §§4, 6, 7. Checks: check_e1_rate, check_e1_models. CITATIONS.md entries "(WLXZ-v1, Plan 66)",
  "(Van, Plan 66)" and "(Plan 66 reuse)".
- **Internal inputs re-read:**
  - RH_p1_general.md (Theorem RH₁(r), REVIEWED) §§1–7;
  - RH/review/REVIEW_RH1r.md, for the reliance it records: WLXZ's uniform O(e^{−cn}) up to k_n and their small-norm
    step;
  - UL.md Cor UL-3.9 and UL-3.10 (REVIEWED);
  - SECOND.md §0 conventions.
- **External sources, fetched by me on 2026-10-15:**
  - arXiv:1410.3948v1 (WLXZ) and arXiv:math/0212014 (Vanlessen), by curl + pdftotext;
  - dlmf.nist.gov/9.7, /10.17 and /10.40, reading the TeX alttext of the sector conditions.

I did not edit E_p1.md.

## Overall verdict: **ACCEPT WITH FIXES** (Route C and Thm E1.10)

I found **no critical or major gap**. The Route C argument is a correct second-order extension of RH₁(r). Every
non-circle jump is O(N^{−2m−1}) ≤ O(N⁻³) or super-polynomially small. The three circle jumps are I + Δ₁/N + O(N⁻²), and
the only non-smooth N-dependence is the factor (−1)^N from φ₊(0) = −iπ/2. The second-order small-norm step uses nothing
beyond the first-order output of RH₁(r)/WLXZ. The fold cancels κ₁ exactly at order 1/n. The value of d₁ (hence of κ₀
and of the α_n coefficient −s/2) is forced by UL Cor UL-3.10 without any unproved input.

Fixes A1–A5 below are minor (presentation, one mis-stated equivalence, one unjustified side remark, and a weak numerical
check). A6 is an INFO note: an opportunity to close the k₁ GAP.

| Statement | Verdict | Fixes |
|---|---|---|
| Lemma E1.7a (Airy model, two terms) | ACCEPT | A5 (check only) |
| Lemma E1.7b (Bessel/FH model, two terms) | ACCEPT | A5 (check only), A6 (INFO) |
| Lemma E1.7 (jumps of S to second order) | ACCEPT WITH FIXES | A1, A3, A4 |
| Prop E1.8 (S₁ = (Σᵉ + (−1)^NΣᵒ)/N + O(N⁻²)) | ACCEPT WITH FIXES | A2 |
| Thm E1.9 (Nβ_N = 1 + (κ₀ + κ₁(−1)^N)/N + O(N⁻²)) | ACCEPT | — |
| Thm E1.10 (main) | ACCEPT; PROVED-mod-cite as labelled | — |
| §3.1 summary of RH₁(r) inputs | ACCEPT WITH FIXES | A2 |
| §7 Rule A log (Route C bullets) | ACCEPT WITH FIXES | A7 |
| Rule C (citations used by Route C) | ACCEPT (equation numbers and sector conditions verified) | — |
| Numerics check_e1_rate, check_e1_models | ACCEPT (byte-identical reproduction; supports O(n⁻²)) | A5 |

## 1. Re-runs (Rule N)

I used `/mnt/c/Users/gspea/source/repos/jacobi-asymptotics/.venv/bin/python` with `PYTHONPATH=<worktree>/src`
(csrc already built).
- **check_e1_models.py**: the output is **byte-identical** to checks/check_e1_models.out.
- **check_e1_rate.py**: the output is **byte-identical** to checks/check_e1_rate.out.
  - The script reads coefficients from `tmp/plan62_cache`, whose files were written by the author before the commit.
    So I also **recomputed from scratch** into a fresh cache (binary128 RKPW, K = 8·10⁴, nmax = 800) the cases s = 2 and
    s = 4.5.
  - All α_n, b_n agree with the cached files to ≤ 5·10⁻³⁷ (the 36-digit print rounding).

**Rate assessment.** In every column (rb, ra, rc(2n), rc(2n−1)) and at all five s, the increments per doubling of n
shrink by a factor ≈ 0.5. Examples:
- rb, s = 4.5: −0.056, −0.030, −0.016, −0.008;
- ra, s = 4.5: 0.37, 0.20, 0.10, 0.05;
- rc(2n), s = 3: 0.74, 0.38, 0.19, 0.10.

So n²·(error) = const + O(1/n). This means a remainder exactly of order n⁻², with an n⁻³ correction, and not
n⁻²log n, which would give constant increments. The "slow drift" of rb at s = 4.5 noted in §6 is just this 1/n
approach (the extrapolated limit is ≈ 0.802).

At s = 3/2, rb extrapolates to ≈ 0.052081, against the proved d₂ = 5/96 = 0.052083.

The period-4 test reproduces:
- classes 0 vs 2 and 1 vs 3 agree to ≤ 1.6·10⁻⁴;
- even vs odd classes differ by O(10⁻²), the next-order parity term.

No i^N term. **Consistent with Thm E1.9/E1.10.** NUMERICAL only; not used in the proof.

## 2. Analytic verification, item by item

### 2.1 Lemma E1.7(iii)–(iv): every non-circle jump is O(N⁻³) or super-polynomially small

**Band pieces (S1).**
- On (−2+ε, −ε) ∪ (ε, 2−ε), J_S − I = N_{r,−}diag(κ_N^{−1} − 1, κ_N − 1)N_{r,−}^{−1}.
- N_r is bounded there (away from 0 and ±2).
- |κ_N − 1| ≤ C(|z|²/N)^{2m+1} by RH₁(r) Lemma S, which is uniform in |arg(±z)| ≤ π/3. I re-derived Lemma S from
  DLMF 5.11.1 with the §5.11(ii) bound.
- With |z| ≤ 2 and m ≥ 1 this is O(N⁻³). ✓

**Exactness of the band jump.** This is the point most at risk at second order. If the band jump of V contained a
unimodular lattice phase e^{±2πiN/x²}, the mismatch would not be smooth in N. I checked WLXZ (5.3) directly:
- on (0, 2) the jump is [[0, w₀/D̃²], [−D̃²/w₀, 0]];
- D̃ (4.15) = 1/H(N/z²) at α_W = 1, which is analytic on ℂ ∖ (−∞, 0] with no lattice phase;
- w₀ = 2iγw/E² with γ = −2nπ/z³ (3.7), which is smooth.

So m_σ = e^L(4 − x²)H_N²|x|^{2a} exactly, and κ_N = H_N²/Q_m exactly. ✓

**Σ ∩ U(0, ε) (S2), RH₁(r) Lemma M.**
- (J1), band and lips:
  - for ρ = N|f| ≥ 1 the amplification is bounded, so |J_H − I| ≤ C(ε²/N)^{2m+1};
  - for ρ ≤ 1 the bound is C(|z|²/N)^{2m+1}ρ^{−2|a|}(1 + |log ρ|)² = CN^{−6m−3}·ρ^{δ}(1 + |log ρ|)², with
    δ = 4m + 2 − 2|a| ≥ 2 > 0. This is ≤ C′N^{−6m−3} uniformly (see A3 for the wording).
- The lips lie at angle ≈ π/4, inside Lemma S's |arg(±z)| ≤ π/3. ✓
- (J2): O(e^{−cN/|z|²})·poly, which is O(N^{−K}). ✓

**Lips and saturated pieces outside the discs (S3).** These are O(e^{−cN}) on total length O(√N), as in RH₁(r)
Lemma W1(r). This inherits the RH₁/RH₁(r) reliance on WLXZ's uniform O(e^{−cn}) up to k_n, which is already recorded
in REVIEW_RH1r.md. Nothing new. ✓

**Interior Fisher–Hartwig point / interpolation.**
- The discrete-to-continuous interpolation (WLXZ (3.6), (3.11), (4.13)) puts the lattice phases e^{±iθ},
  θ = πN/z² − πα_W, only into:
  - lens/lip jumps, where they are exponentially small: (J2) near 0, and (S3) outside;
  - D-function ratios, which are removed exactly in the Airy discs.
- At α_W = 1, e^{2iθ} = e^{2πiN/z²}, an analytic function of z that carries no N mod k structure.
- I confirm the Rule A bullet "Hidden N-dependence". ✓

**The choice m ≥ max(1, ⌈|a|/2⌉).**
- RH₁(r) §3 says "Any larger m also works", and all its uses need only δ ≥ 2 (F2: δ > 0; §6: δ > 1/2; Lemma X: δ ≥ 2).
  So the change m ≥ 1 is legitimate.
- At a = 0 this means running RH₁(r) with Q₁ instead of Q₀ ≡ 1. That is covered by the same statement. ✓

### 2.2 Lemma E1.7(i): the Airy circles

**N-dependence only through H_N.** The key fact is that WLXZ's Airy phase vanishes at the endpoint:
- (4.29): φ̃ = φ ± πi/z² in ℂ±;
- (4.34): this uses g₊(2) = l/2 + πi/4, so φ₊(2) = −πi/4 but φ̃(2) = 0, as in (6.11) φ̃ = −(2/3)(z−2)^{3/2} + O((z−2)²);
- likewise φ̂ = φ ∓ (1/z² − 1)πi (4.30) gives φ̂(−2) = −3πi/4 + 3πi/4 = 0, since g₊(−2) = l/2 + 3πi/4.

So the Airy parametrices carry **no** constant phase e^{Nφ₊(±2)} = e^{∓iπN/4}. Such a phase would produce an i^N
dependence on ∂U(±2, ε). I checked this explicitly because it is the one way a period-4 term could enter (see A4).

**The algebra.** With (6.12), (6.15), (F1) G_σ = G₀H_N^{−2} and (F2) m_rM₀^{−1} = G₀^{σ₃/2}NG₀^{−σ₃/2}, I re-derived

  P^{(3/2)}N^{−1} = H_N^{σ₃}·N·G₀^{−σ₃/2}(I + X_j/ξ + O(ξ⁻²))G₀^{σ₃/2}·H_N^{−σ₃}·N^{−1},  ξ = −Nφ̃.

The order of the last two factors in E_p1's display is swapped (A1). The bracketed 1/N coefficient that E_p1 states,
including (z²/12)(σ₃ − Nσ₃N^{−1}), is the one that follows from the correct order. So only the display is wrong.

**Inputs.**
- (F1): from (4.15) at α_W = 1, D̃ = √(2π)t^{t+1/2}/(Γ(t+1)e^t) = 1/H(t). ✓
- (F2) is checked to 9·10⁻⁴¹ (my re-run). ✓

**The disc factors.**
- A = A_∞ + O(1/N), since g = (qQ_m)^{1/2}/D_aD_Q and Q_m, D_Q = 1 + O(1/N).
- N Q_m^{σ₃/2}N^{−1} = I + (z²/(12N))Nσ₃N^{−1} + O(N⁻²), using log Q_m = z²/(6N) + O(N⁻³), B₂ = 1/6.
- D_{Q,∞}^{σ₃} conjugation contributes only at O(N⁻²) to the 1/N term.

**Szegő step (c).**
- log Q_m − z²/(6N) is entire and O(N⁻³) on compacts, so its z-derivative is O(N⁻³) on compacts (Cauchy estimates).
- RH₁(r) Lemma G(iii)'s difference-quotient representation then bounds 𝒮 of it by O(N⁻³) uniformly, including boundary
  values on (−2, 2) where the circles cross the band. ✓

**Δ^± and the model expansion.**
- Δ^± is N-independent: A_∞, N, G₀, φ̃ and X_j are all N-independent.
- f̃₁ is conformal, so sector arcs on the circle are fixed.
- |φ̃| is bounded below on ∂U(2, ε). ✓

### 2.3 Lemma E1.7(ii): the origin circle and φ₊(0) = −iπ/2

**Matching identity.**
- E_N = E e^{Nφ_{KV,+}(0)σ₃}e^{−πiσ₃/4}B^{−1}, with B^{−1} = (1/√2)[[1, i], [i, 1]].
- Vanlessen (4.43): Ψ = B(I + O(1/ζ))e^{πiσ₃/4}e^{−iζσ₃}C₁. In ℂ₊, ζ = Nf = N(iφ_KV − iφ_{KV,+}(0)), so
  −iζ = N(φ_KV − φ_{KV,+}(0)).
- Hence e^{−iζσ₃}C₁W_h^{−σ₃}e^{−Nφ_KVσ₃}(P^∞)^{−1} = e^{−Nφ_{KV,+}(0)σ₃}E^{−1}.
- In ℂ₋, f = −iφ_KV − iφ_{KV,+}(0) and C_q contains [[0, −1], [1, 0]]. The anti-diagonal factor turns e^{iζσ₃} into
  e^{−iζσ₃}, and I get the same conjugation structure, with e^{Nφ_{KV,+}(0)σ₃} the same in every sector.

So P₀(P^∞)^{−1} = E e^{Nφ₊σ₃}e^{−πiσ₃/4}(I + Ψ₁/(Nf) + O(N⁻²))e^{πiσ₃/4}e^{−Nφ₊σ₃}E^{−1}, as stated.
- The leading term is exactly I.
- Replacing E by E_∞ in the 1/N term costs O(N⁻²). ✓

**The phase.**
- WLXZ (2.1) gives ψ = 2/|x|³ on |x| > 2, so ∫_2^∞ψ = 1/4.
- This is also the lattice constraint mass #{k : N/k ≥ z²}/N = 1/z² at z = 2.
- ψ is even with total mass 1, so ∫_0^2ψ = 1/2 − 1/4 = 1/4.
- With (4.3) and g₊(2) = l/2 + πi/4 (proof of Prop 4.2), φ₊(x) = −πiμ([x, ∞)) on the band, so φ₊(0) = −iπ/2 exactly.
- Conjugation by e^{Nφ_{KV,+}(0)σ₃} = diag(i^N, i^{−N}) multiplies both off-diagonal entries by i^{±2N} = (−1)^N and
  fixes the diagonal. ✓
- This is the same structure as Vanlessen Remark 4.4 (ϕ₊(x_ν)^{nσ₃}, which is i^{nσ₃} at x_ν = 0).

### 2.4 Lemmas E1.7a, E1.7b (Rule C, DLMF sectors)

**Airy (E1.7a).**
- (6.8) is read in the PDF: four quadrant formulas, ω = e^{2πi/3}.
- The phases of the Airy arguments on the closed sectors are as stated: ph ω²ζ ∈ [−2π/3, −π/6] on [0, π/2];
  ph ωζ ∈ [−5π/6, −π/3] and ph ω²ζ ∈ [−π/6, π/3] on [π/2, π].
- DLMF 9.7.5–6 hold for |ph z| ≤ π − δ (verified alttext), with δ = π/6. ✓

**Bessel (E1.7b).**
- Vanlessen (4.26)–(4.33), (4.43)–(4.46), (4.47)–(4.52) and Remark 4.4: the equation numbers match the PDF.
- On the closed sectors the arguments ζ, −ζ and ζe^{∓πi/2} have phase in [−π/4, π/4].
- DLMF ranges (verified alttext):
  - 10.17.5: −π + δ ≤ ph ≤ 2π − δ;
  - 10.17.6: −2π + δ ≤ ph ≤ π − δ;
  - 10.40.1: |ph| ≤ π/2 − δ;
  - 10.40.2: |ph| ≤ 3π/2 − δ.

  All of these contain [−π/4, π/4] with δ = π/4. ✓

Two-term Poincaré expansions in closed sectors give uniform O(ζ⁻²) remainders. ✓

### 2.5 Prop E1.8: second-order small norm

S₁ = −(1/2πi)∫Δ_S − (1/2πi)∫u_SΔ_S, with u_S = S₋ − I (WLXZ (6.36)). The bound
|∫u_SΔ_S| ≤ ‖u_S‖_{L²}‖Δ_S‖_{L²} = O(1/N)·O(1/N) is correct.

‖u_S‖_{L²} = O(1/N) is exactly the first-order output. It needs C₋ bounded on L²(Σ_S) uniformly in N. WLXZ obtain this
by "the standard procedure of norm estimation of Cauchy operators" on a contour whose long pieces grow like k_n ≍ √n.
That is the **same inherited reliance** as RH₁/RH₁(r) §7. Prop E1.8 assumes nothing new.

The parenthetical "equivalently … sup|S_± − I| = O(1/N)" in §3.1 (SN) is not an equivalence on a contour of length
O(√N) (A2). It also does not follow from WLXZ (6.37) as stated. That statement is "S(z) = I + O(1/n) uniformly for
z ∈ ℂ"; boundary values need the contour-deformation remark. The proof does not use it, so this is a wording fix.

Circle contributions: (1/N)∮Δ + O(N⁻²) by Lemma E1.7(i)–(ii), uniform remainders on bounded-length circles. ✓

### 2.6 Thm E1.9 and the extraction

V₁ = N_{r,1} + S₁ (V = SN_r near ∞). Since N_{r,1} = D_{Q,∞}^{σ₃}(N₁ − d₁σ₃)D_{Q,∞}^{−σ₃}, the off-diagonal entries are
D_{Q,∞}^{±2}(N₁)₁₂, ₂₁, with D_{Q,∞}^{±2} = 1 + O(1/N). Expanding the product:

  Nβ_N = 1 − ie^L(S₁)₂₁ + ie^{−L}(S₁)₁₂ + O(N⁻²).

I re-derived this. Reality of κ₀ ± κ₁ from the reality of Nβ_N along each parity class is correct. ✓

### 2.7 Thm E1.10: the fold and the values

**Fold.** I recomputed it:
- b_m² = β_{2m−1}β_{2m} = (4m²)^{−1}(1 + (½ + κ₀)/m + O(m⁻²));
- mα_m = 1 + (κ₀ − ½)/(2m) + O(m⁻²);
- κ₁ enters only through (κ₁/(2m) − κ₁/(2m±1)) = O(m⁻²), so it cancels at order 1/m. ✓

**Value of d₁.**
- Under the now-proved (E) with an O(j⁻²) remainder, Σ_{j≤n}log(2jb_j) = d₁log n + O(1).
- UL Cor UL-3.10(d′) at p = 1 (REVIEWED) gives −((s − 1)/2)log n + O(1). So d₁ = −(s − 1)/2.
- UL-3.10 is anchored at s₀ = 3/2 through SECOND Cor 3.6(i) / RH₁. It does not use E_p1, so there is no circularity
  (Rule X). ✓

**The α_n coefficient −s/2 is derived, not assumed.** Both 1/n coefficients depend only on κ₀:
- d₁ = (κ₀ + ½)/2;
- the α_n coefficient is (κ₀ − ½)/2.

So fixing d₁ fixes κ₀ = ½ − s and hence −s/2. **No unproved k₁ value is used anywhere in Thm E1.10.** κ₁ appears only
in the stated ng_{n−1} formula, where it is left symbolic. ✓

**Pairings and chain.** Re-derived:
- α_n/(2b_n) = 1 − 1/(2n);
- b_{n−1}/b_n = 1 + 1/n + O(n⁻²), so α_{n−1}/(2b_n) = 1 + 1/(2n);
- ng_{n−1} = nβ_{2n−1} = ½(1 + (1 + κ₀ − κ₁)/(2n)) + O(n⁻²).

With κ₁ = −3a this gives ½(1 + a/n). ✓

## 3. Additional finding (INFO): the model corrections are sector-independent

I estimated X_j and Ψ₁^{(j)} at |ζ| = 3000 on 5 (Airy) and 4 (Bessel) rays per sector (scratch script; not committed).
- **Airy:** the spread within each sector is ≤ 7·10⁻⁷, and all four sectors give the same matrix
  X = [[−1/72, i/12], [i/12, 1/72]] (= the standard (u₁ ± v₁)/2 combinations).
- **Bessel:** the spread is O(1/|ζ|), consistent with the O(ζ⁻²) remainder. All eight sectors give the same
  Ψ₁ = (a/2)σ₁ − (ia²/2)σ₃ (λ = a ∈ {−0.25, 1.5}; consistent with DLMF a₁(a ± ½) = (a² ± a)/2).

So E1.7a/b hold in the stronger form "one constant for all sectors". This has a consequence (A6): Δ^{0,o}(z) =
E_∞(z)Ŷᵒᶠᶠ E_∞(z)^{−1}/f(z) is a single meromorphic function in U(0, ε), with E_∞ analytic and f having a simple zero
at 0. So Σᵒ is a residue at z = 0, and κ₁ reduces to evaluating E_∞(0) and f′(0) = πψ(0). Note that Ψ₁ᵒᶠᶠ ∝ a,
consistent with κ₁ ∝ a and κ₁(3/2) = 0.

## 4. Fixes (exact wording)

**A1 (minor, typo; Lemma E1.7(i) proof).** In the first line of the display, replace

  `P^{(3/2)}N^{−1} = H_N^{σ₃}·N G₀^{−σ₃/2}(I − X_j/(Nφ̃) + O(N⁻²))G₀^{σ₃/2}N^{−1}·H_N^{−σ₃}`

by

  `P^{(3/2)}N^{−1} = H_N^{σ₃}·N G₀^{−σ₃/2}(I − X_j/(Nφ̃) + O(N⁻²))G₀^{σ₃/2}·H_N^{−σ₃}·N^{−1}`.

The second line is unchanged; it is the expansion of the corrected first line.

**A2 (minor; §3.1 (SN) and Prop E1.8).**
- In (SN), replace "(equivalently for our purpose, sup|S_± − I| = O(1/N), WLXZ (6.37))" by: "(this uses that C₋ is
  bounded on L²(Σ_S) uniformly in N, which is WLXZ's 'standard procedure' after (6.35) and the same reliance as RH₁ and
  RH₁(r) §7; alternatively, a uniform bound sup_{Σ_S}|S₋ − I| = O(1/N) together with ‖J_S − I‖_{L¹(Σ_S)} = O(1/N)
  would give the same O(N⁻²) bound in Prop E1.8)".
- In the Rule A bullet "Second-order small norm without a new operator bound", replace "(equivalently the uniform bound
  of WLXZ (6.37))" by "(which already contains the uniform L² boundedness of the Cauchy operator inherited from
  WLXZ/RH₁(r))".

**A3 (minor; Lemma E1.7(iii)).** Replace "|J_H − I| ≤ CN^{−2m−1−2|a|}|z|^{4m+2−2|a|}log²(2/(N|z|)) ≤ CN^{−6m−3}log²" by
"|J_H − I| ≤ CN^{−2m−1−2|a|}|z|^{4m+2−2|a|}(1 + |log(N|z|)|)² = CN^{−6m−3}ρ^{δ}(1 + |log ρ|)² ≤ C′N^{−6m−3}
(ρ ≍ N|z| ≤ 1, δ = 4m + 2 − 2|a| > 0)". The present text leaves an unbounded log² factor in the final bound.

**A4 (minor, clarity; Lemma E1.7(i)).** After "so that the Airy variable has ξ = (2/3)f̃_N^{3/2} = −Nφ̃", add: "Here
φ̃ = φ ± πi/z² (WLXZ (4.29)) vanishes at 2 (6.11), although φ₊(2) = −πi/4; likewise φ̂ (4.30) vanishes at −2. So no
constant phase e^{Nφ₊(±2)σ₃} (which would give an i^N dependence) enters the Airy matching. The only lattice phase,
e^{2iθ} = e^{2πiN/z²} (α_W = 1), is an analytic function of z absorbed in φ̃, φ̂."

**A5 (minor, numerics; check_e1_models [3], [4] and §§3.2, 6).**
- The script estimates X_j (resp. Ψ₁^{(j)}) **separately on each ray** at |z| = 400 (`Xj = (Rb − I2)*xib` inside the
  ray loop). So it tests the two-term structure ray by ray, not that the 1/ξ coefficient is constant on a sector.
- Either estimate one X_j per sector (e.g. at the sector's middle ray) and test all rays against it, or add a printed
  spread across rays. Then add to §6: "the 1/ξ and 1/ζ coefficients are the same constant on all rays and in all
  sectors: X = [[−1/72, i/12], [i/12, 1/72]], Ψ₁ = (a/2)σ₁ − (ia²/2)σ₃ (NUMERICAL)".
- Regenerate the .out file.

**A6 (INFO; §8 GAP k₁).** By §3 above, Δ^{0,o} is meromorphic in U(0, ε) with a simple pole at 0, so Σᵒ is (up to the
orientation sign) E_∞(0)ŶᵒᶠᶠE_∞(0)^{−1}/f′(0). The k₁ GAP therefore looks like a finite residue computation (E_∞(0)
from P^∞, W_h and D_a near 0, f′(0) = πψ(0)) rather than a new analytic problem. Suggest recording this in §8 as the
route. Not required for acceptance.

**A7 (minor; §7 Rule A bullet "Choice m ≥ 1").** The claim that with m = 0 the argument is "still compatible with
Theorem E1.9" is not justified in the file:
- inside U(0, ε) the m = 0 mismatch J_H − I is O(|z|²/N) amplified by Ψ_a(Nf);
- its 1/ζ correction and the ρ ≤ 1 region would have to be shown to contribute O(N⁻²), not O(N⁻²log N).

Also, RH₁(r) allows m = 0 only for |a| < 3/4 in the first place. Replace the bullet's middle sentence by: "With m = 0
the band mismatch κ_N − 1 = z²/(6N) + … is only O(1/N), and inside U(0, ε) it is amplified by Ψ_a(Nf); whether this
still gives Theorem E1.9 was not checked. m ≥ 1 makes all non-circle jumps O(N⁻³) uniformly, which is what §3.4 uses."

## 5. Points checked and found correct (no action)

- **No new assumption beyond RH₁(r).** The Route C inputs are RH₁(r) §§2–7 (REVIEWED, with its recorded WLXZ reliance),
  WLXZ formulas actually present in v1 (I located (2.1)–(2.5), (3.6)–(3.7), (4.3), (4.13)–(4.30), (4.34)–(4.35), (5.3),
  (6.8)–(6.21), (6.29)–(6.37) in the PDF), Vanlessen §4.2–4.3, and DLMF. The (WLXZ-v1, Plan 66) and (Van, Plan 66)
  quotes match the PDFs.
- **Orientation conventions:** the σ₃-conjugation between the KV and WLXZ frames changes the signs of (S₁)₁₂ and (S₁)₂₁
  together. It does not affect existence of κ₀, κ₁, which is all Thm E1.9 claims.
- **(Ex) exactness** (constant diagonal conjugations and scalar right factors preserve (·)₁₂(·)₂₁): ✓ as in RH₁(r) §7.
- **§4 (why p = 1 works)** is a correct HEURISTIC explanation. The symmetric-frame claims in it are those verified above.

## 6. Recommendation

Apply A1–A5 and A7 (all wording, plus the A5 check strengthening and regenerating its .out). After that, Lemma E1.7,
Prop E1.8, Thm E1.9 and Thm E1.10 are **PROVED-mod-cite + REVIEWED (reviewer A)**, with labels as in the E_p1 summary
table, pending reviewer B on Route A. A6 is optional follow-up work.
