# SPEC: Jacobi coefficients of measures on reciprocal spectra — the node-zeta law (exploration)

Status (2026-10-20): exploratory note from the Plan E3 session. Labels per VERIFICATION_POLICY.md.
- §§1–2 and §4: CONJECTURE / HEURISTIC / NUMERICAL (Rule N: fit half-ranges are spreads over fit choices, not error bounds).
- §3.2: Lemma U (PROVED) and Theorem S2′ (PROVED-mod-cite), **REVIEWED** (Rule R: REVIEW_SPEC_A.md, ACCEPT WITH FIXES; fixes
  applied, §6). A single second reader; the other parts were reviewed for labels only.
- §3.1: Lemma H is CONDITIONAL on Hurwitz's formula (unread under Rule C), with NUMERICAL confirmation.
- §3.3: Proposition B, PROVED-mod-cite pending Rule C (Hadamard factorisation of Ai; the Mellin correspondence), NOT REVIEWED;
  NUMERICAL confirmation. This note builds on E3.md (REVIEWED), in particular its Lemma E3.7. Novelty: first pass done, §3.9.
- §§3.3–3.13 (second round): **REVIEWED** for correctness of the stated evidence, derivations and labels (Rule R:
  REVIEW_SPEC2_A.md and REVIEW_SPEC2_B.md, two independent readers, both ACCEPT WITH FIXES; fixes applied 2026-10-21, §6).
  Review does not upgrade labels: S1′, S1″, S1‴, the pole law and the κ law remain CONJECTURE / NUMERICAL / HEURISTIC.
  The main correction is the sign of the pole law (§3.12) and its limitation to the leading power of each pole (F2).
- §3.18 (2026-10-21, NOT REVIEWED): noise mechanism — universal edge kernel; noise = linear statistic in variance, not in realisation.
- §3.17 (2026-10-21, NOT REVIEWED): quartic oscillator — pole law with cot ≠ 0 on a real operator, d₂ to 3·10⁻⁵ (NUMERICAL).
- §3.16 (2026-10-21, NOT REVIEWED): drums at p = 1 (NUMERICAL): perimeter via the W·cot = 0·∞ limit, corners via Z(0).
- §3.15 (2026-10-21, NOT REVIEWED): the subleading pole term, Conjecture S1⁗ (NUMERICAL; exact to fit precision for q₁ ≤ 1).
- §3.14 (2026-10-21, NOT REVIEWED): the π cot kernel derived. Theorem K (lattice, PROVED-mod-cite on E3), Lemma K0 (PROVED),
  Lemma Q (soft-edge condition, PROVED-mod-cite + NUMERICAL inequalities), Proposition E (PROVED as Mellin algebra). Principle
  E and Hypothesis G are CONJECTURE / HEURISTIC; S1″ itself stays CONJECTURE (NUMERICAL).

## 0. Setting

Λ = {λ_m}_{m≥1} is an increasing sequence with λ_m ~ m^p (p > 0, p ≠ 1). Λ is the *node set*. The measure on reciprocal
nodes is σ_Λ := Σ_m λ_m^{−s/p}δ_{1/λ_m}, with s > 1, α = (s−1−p)/p and c = c(p) as in E3. For Λ = {m^p} this is σ_{p,s}.

The *node zeta function* is Z_Λ(w) := Σ_m λ_m^{−w}, analytically continued. For Λ = {(m + a − 1)^p} it is Z_Λ(w) = ζ(pw, a).
For Λ with an asymptotic expansion λ_m = (m + a − 1)^pΣ_iγ_i(m + a − 1)^{−2i}, Z_Λ(−j) is the Hurwitz-regularised sum (the series
terms give ζ values, plus a convergent remainder). This is the regularisation used for the Airy zeros in `checks/spec_zeta_airy.py`.

Throughout, y_n := n^pb_n/c − 1. The "band" is [0, 4c] in the rescaled variable x = n^p·(node), so the node 1/λ lies outside
the band iff u := 4cλn^{−p} < 1.

## 1. Statements

**Conjecture S1 (node-zeta law).** If Λ is *regular* (λ_m^{1/p} has an asymptotic expansion in powers of 1/m, as for WKB
spectra, or Λ is a finite modification of such a set), then for 0 < p < 1, with K = ⌊1/p⌋,

  y_n = (1/n)·[ −pα/2 + p·Σ_{j=0}^{K} C(2j, j)c^jZ_Λ(−j)n^{−jp} ] + (n⁻²-order terms) + o(n^{−1−Kp}),

with the analogous statement for p > 1 (only j ≤ 1 above n⁻³ when 1 < p < 2).
- For Λ = {m^p} this is E3 Theorem E3.2 plus d₁ = −(s−1)/2: the j = 0 term is pζ(0) = −p/2 (PROVED there).
- The j = 0 term is the "lattice offset" heuristic of SECOND.md §4.1: j₀ − ½ = −ζ(0, j₀).

**Conjecture S2 (exact per-node contribution; for one deleted atom of σ_{p,s} away from the turning point this is Theorem S2′,
§3.2, PROVED-mod-cite, REVIEWED).** Let a single node λ (n-independent) be deleted from Λ. While the node is
outside the band (u < 1),

  n·(y_n(Λ∖{λ}) − y_n(Λ)) = −p(1 − u)^{−1/2} + O(n^{−1}),   u = 4cλn^{−p}

(with the error not uniform as u → 1). Adding a node gives the opposite sign. Expanding (1 − u)^{−1/2} = ΣC(2j, j)(cλn^{−p})^j
recovers S1 term by term, so S1 for finite modifications is S2 summed over the modified nodes.

*Proof sketch (HEURISTIC).* A node outside the band enters the RH problem like an analytic weight factor (1 − xλn^{−p})^{±2}
on a neighbourhood of [0, 4c], plus a unit change in the node count. Lemma E3.7 (exact for any analytic tilt, REVIEW_PlanE3_B F1)
gives the first-order response cp·M(4c). For P(x) = −2log(1 − xy), y = λn^{−p}: μ_k = 2y^k/k, M(4c) = Σμ_kQ_k(4c) =
(1/c)Σ_{k≥1}C(2k, k)(cy)^k = (1/c)[(1 − 4cy)^{−1/2} − 1], so the response is p[(1 − u)^{−1/2} − 1]. The unit change in the
node count is the index shift n ↦ n ± 1 (the j = 0 term, −p). Together: −p(1 − u)^{−1/2}.

What is not done:
- the precise form in which a saturated-region node enters the band factor (E_pgt1 Lemma E.2, E_plt1 Lemma F.1);
- uniformity of Lemmas E3.4–E3.6 as the singularity 1/y of the tilt approaches 4c;
- the index shift as a statement.

**Heuristic S3 (spectral determinant).** In E3 the band factor acts as the tilt μ_k = 2Z(−k)/(kn^{kp}). Formally
exp(−2Σ_kZ_Λ(−k)t^k/k) = Π_m(1 − tλ_m)², with t = x/n^p. So the discrete part of the problem is governed by the regularised
determinant det_ζ(1 − tA)², where A has spectrum Λ:
- its regular (Taylor) part gives the n^{−1−jp} terms;
- its singular (Weyl-law) part gives c(p) and the edge exponent.
At p = 1 this is consistent with the Gamma/Binet band factor of E_pgt1/E_p1 (the regularised product over ℕ is 1/Γ). Not
made precise.

**Observation S4 (limit of regularity; NUMERICAL; mechanism refined in §3.6).** If the node positions deviate from a smooth node function by a fixed
fraction of the spacing (iid jitter), y_n acquires an irregular component.
- Its RMS decays only like ≈ n^{−1/2}, so the 1/n expansion itself is destroyed.
- The noise is generated locally, while the soft-edge threshold λ ≈ n^p/(4c) sweeps through jittered nodes.
- Jitter confined to nodes deep inside the band is invisible (RMS ≤ 3·10⁻⁷).
- Jitter with bounded counting function (differences of iid) is no better. So the mechanism is local soft-edge sensitivity, not
  a long-range linear statistic.

Consequence (HEURISTIC): for chaotic spectra, e.g. Laplacians on negatively curved surfaces with O(spacing) deviations from
any smooth node function, no deterministic 1/n expansion of b_n is expected. Such surfaces also have p = 1, outside E3.

## 2. Evidence (NUMERICAL; Plan 62 pipeline, n ≤ 1600, quad precision, tails K = 100–200·n_max)

**Hurwitz lattices** (`checks/spec_hur.out`): Λ = {(m + δ)^p}, so Z(−j) = ζ(−jp, 1 + δ).

| p, s, a = 1+δ | d₁ fit / S1 | n^{−1−p} coefficient: fit / S1 | pure-lattice value |
|---|---|---|---|
| 0.6, 2, ½ | −0.19999996 / −0.2 | +0.0306156 (8·10⁻⁵) / +0.0306142 | −0.0899767 |
| 0.6, 2, 3/2 | −0.8000002 / −0.8 | −0.309374 (1.4·10⁻⁴) / −0.309386 | −0.0899767 |
| 0.6, 2, 2 | −1.1000006 / −1.1 | −0.605309 (3·10⁻⁴) / −0.605320 | −0.0899767 |
| 0.75, 3, 2 | −1.7500003 / −1.75 | −0.779282 (1.3·10⁻³) / −0.779293 | −0.0918692 |
| 1.5, 2, 3/2 | −1.25 / −1.25 | −0.57244 (5.5·10⁻³) / −0.57263 | −0.0432947 |
| 1.5, 2, 2 | −2.00 / −2.00 | −1.74157 (5.6·10⁻³) / −1.74211 | −0.0432947 |

The n^{−1−2p} coefficient at p = 0.6 agrees to ≤ 4·10⁻³ against half-ranges of 0.025–0.065 (weak).

**Single moved node** (`checks/spec_pert.out`; p = 0.6, s = 2): d₁ is unchanged to ≤ 4·10⁻⁷, and the n^{−1−p} coefficient
shifts by 2pc[(new)^p − (old)^p].

| Node move | n^{−1−p} coefficient: fit | S1 | difference |
|---|---|---|---|
| 2 → 2.5 | +0.021941 | +0.021928 | 1.3·10⁻⁵ |
| 3 → 2.6 | −0.171867 | −0.171946 | 7.9·10⁻⁵ |

**Exact per-node formula** (`checks/spec_remove.out`; p = 0.6, s = 2; no fitting). Values of n·(y_n(removed) − y_n(pure)):

| node k₀ | n | u | measured | −p(1−u)^{−1/2} | ratio | truncated S1 (j ≤ 1) |
|---|---|---|---|---|---|---|
| 30 | 200 | 0.550 | −0.87984 | −0.89476 | 0.983 | −0.765 |
| 30 | 1600 | 0.158 | −0.65295 | −0.65389 | 0.9986 | −0.647 |
| 300 | 800 | 0.954 | −2.6644 | −2.7873 | 0.956 | −0.886 |
| 300 | 1000 | 0.834 | −1.4613 | −1.4733 | 0.992 | −0.850 |
| 300 | 1600 | 0.629 | −0.98290 | −0.98531 | 0.998 | −0.789 |

The ratio tends to 1 like 1 − O(1/(n(1 − u))). Equivalently, R ≈ C(p)/(n(1 − u)^{3/2}) (REVIEW_SPEC_A F9), an O(n⁻¹) correction that grows near the edge. For
u > 1 (node inside the band) the difference is small and irregular. This is the regime of S4.

**A real operator: the quantum bouncer** −ψ″ + xψ = Eψ on (0, ∞), ψ(0) = 0 (`checks/spec_bouncer.out`, `checks/spec_zeta_airy.out`).
- **Spectrum.** E_k = −a_k (Airy zeros). Normalised, Λ = {−a_k/(3π/2)^{2/3}} = {(k − ¼)^{2/3}(1 + O(k⁻²))}, so p = 2/3.
- **Zeta values.** From DLMF 9.9.6 plus exact low zeros: Z(0) = ζ(0, ¾) = −¼. Z(−1) and Z(−2) vanish to ≤ 10⁻¹⁷, and so do
  Z(−4) and Z(−5) to ≤ 3·10⁻¹³. Z(−3) = 0.0105542899627. So Z(−j) = 0 unless 3 | j (NUMERICAL).
- **Heat-trace consistency (HEURISTIC).** This pattern fits a heat trace Tr e^{−tH} with powers t^{(3m−3)/2} only, and Z(0) = −¼
  is its constant term. Not checked against the literature; Voros's exact-WKB work on odd-degree potentials is the natural
  reference (Rule L).
- **S1 predictions.** d₁ = −pα/2 − p/4 = −(s−1)/2 + 1/6, and ε₁ = 2pcZ(−1) = 0. The "Hurwitz-only" guess, ignoring the WKB
  corrections, would be 2pcζ(−2/3, ¾) = −0.0113453.

| s | d₁ fit / S1 | n^{−5/3} coefficient: fit / S1 / Hurwitz-only |
|---|---|---|
| 2 | −0.33333333 (5·10⁻⁷) / −1/3 | +0.0000021 (5.9·10⁻⁵) / 0 / −0.0113 |
| 3 | −0.83333335 (1·10⁻⁵) / −5/6 | −0.0000295 (4.8·10⁻⁴) / 0 / −0.0113 |

The Hurwitz-only value is excluded by ≈ 200 half-ranges at s = 2. The WKB corrections to the Airy zeros cancel the Hurwitz term
exactly, as S1 requires.

**Jitter** (`checks/spec_jitter.out`, `checks/spec_window.out`; p ∈ {0.3, 0.6}, s = 2, A = 0.3). For iid jitter
λ_m = (m + ξ_m)^p, ξ ~ U(−A, A), the residual RMS after a smooth fit is:

| Model | n ∈ [100, 200) | n ∈ [800, 1600) |
|---|---|---|
| iid, p = 0.3 | 7.6·10⁻³ | 2.8·10⁻³ |
| iid, p = 0.6 | 1.3·10⁻² | 4.2·10⁻³ |
| difference jitter (ξ_k = A(η_k − η_{k−1})) | 9.9·10⁻³ | 3.6·10⁻³ |

The RMS slopes ≈ n^{−0.5}, and the fitted d₁ is meaningless. Localisation:
- **Jitter only on nodes 1–300.** The soft-edge threshold k ≈ 0.406n passes node 300 at n ≈ 740. The noise is
  5.3·10⁻³ on [400, 800) and drops to 1.4·10⁻⁴ on [800, 1600), once the threshold has passed all jittered nodes.
- **Jitter only on nodes ≥ 20000.** These stay deep in the band for all n ≤ 1600. The RMS is 10⁻⁹–3·10⁻⁷, and d₁ is correct
  to 5·10⁻⁵.

## 3. Proof-side progress

### 3.1 Lemma H: the shifted band-factor moments (p > 1; p < 1 analogue checked)

**Lemma H (CONDITIONAL on Hurwitz's formula, DLMF 25.11.9 / Apostol, *Introduction to Analytic Number Theory*, Thm 12.6: not
read under Rule C, since the DLMF fetch truncates before §25.11(iv) and the domain is blocked from the shell; the formula and the
lemma are confirmed NUMERICALLY to 10⁻²⁷–10⁻³⁰; REVIEW_SPEC_A F5).** Let p > 1, δ ∈ ℝ, and
𝔢_δ(y) := 2Im Log(1 − e^{−2πi(t₊(y) − δ)}), with t₊ = n(y + i0)^{−1/p} on y < 0. This is E3 Lemma F.1′'s density with the
interpolating phase of the lattice {(k + δ)^{−p}}_{k≥1} (the lattice reading needs δ > −1; the identity holds for every
δ ∈ ℝ). Then

  m_k(δ) := (1/2π)∫_{−∞}^0𝔢_δ(y)y^{−k−1}dy = ζ(−kp, a)/(kn^{kp}),   a := δ − ⌈δ⌉ + 1 ∈ (0, 1].

*Proof.* As in Lemma F.1′(i), with q^m replaced by q^me^{2πimδ}:
- ∫_0^∞𝔢_δ(−r)r^{−k−1}dr = 2(−1)^kpΓ(kp)(2πn)^{−kp}S, where S := Σ_m sin(πkp/2 − 2πmδ)/m^{1+kp}. The Fubini bound is unchanged,
  since |e^{2πimδ}| = 1.
- Hence m_k = −(1/π)pΓ(kp)(2πn)^{−kp}S.
- Hurwitz's formula, ζ(1−σ, a) = 2Γ(σ)(2π)^{−σ}Σ_m cos(πσ/2 − 2πma)/m^σ for Re σ > 1, 0 < a ≤ 1 (DLMF 25.11.9; not read), at
  σ = 1 + kp gives ζ(−kp, a) = −(kpΓ(kp)/π)(2π)^{−kp}S. Here S depends on δ only mod 1, and cos(π/2 + x) = −sin x. ∎

Check: `checks/spec_hurwitz_moments.out`; p ∈ {5/4, 3/2, 3}, δ ∈ {−½, 0.3, ¾, 1.4}, k ≤ 3; worst relative error 2·10⁻²⁷.

*What it gives.* The seam integral produces the Hurwitz values for the fractional part of the offset. The integer part of δ
(the lattice {(k + δ)^{−p}}_{k≥1} lacks the ⌈δ⌉ nodes a, a + 1, …, a + ⌈δ⌉ − 1 of {(j + a)^{−p}}_{j≥0}, none when −1 < δ ≤ 0) is
per-node: ζ(−kp, a + 1) = ζ(−kp, a) − a^{kp}, which is S2 expanded. To turn this into Conjecture S1 for Hurwitz lattices one still needs:
- that the shifted lattice's band factor has exactly this jump (the construction of E_pgt1 §1 / Paper 2 with Γ(t) ↦ Γ(t − δ +
  ⌈δ⌉) and sin πt ↦ sin π(t − δ));
- the index offset (d₁), SECOND §4.1.

Lemma E3.7 is unchanged.

*Reduction for −1 < δ ≤ 0 (HEURISTIC; the steps that change, after Paper 2 §§5–6 and E_pgt1 Lemma E.2).*
- **Interpolation.** The nodes sit at t ∈ 1 + δ + ℕ₀ (t = nz^{−1/p}), so in Paper 2 Lemma interp and §6 sin πt becomes
  sin π(t − δ), and the factor 1/Γ(t) carried by the node masses becomes 1/Γ(t − δ).
- **Outer scalar.** It becomes D̃_δ = e^{−j_δ(t)}, with j_δ(t) := LnΓ(t − δ) − (t − δ − ½)ln t + t − ½ln 2π. By DLMF 5.11.8
  (Stirling for Γ(t + a)), j_δ(t) → 0 as t → ∞, with Bernoulli-polynomial (Hurwitz) coefficients B_{k+1}(−δ).
- **Band factor (p > 1).** G_δ := −j_δ + log B_δ. Here B_δ is the Binet-cut scalar of the density
  𝔟_δ = 2Im(−j_δ(t₊) − Log(1 − e^{−2πi(t₊ − δ)})). Its jump on (−∞, 0) is i𝔢_δ: the j_δ parts cancel identically, as in E_pgt1
  Lemma E.2(a). K_δ := G_δ − G_δ(1) − (Cauchy integral of 𝔢_δ) is analytic on ℂ ∖ {0}, bounded near 0 (t → ∞), and O(log|z|) at ∞,
  so it is constant. Hence log H_n^δ(z) − log H_n^δ(1) = −2Σ_km_k(δ)(z^k − 1) + …, with Lemma H's m_k(δ) = ζ(−kp, 1 + δ)/(kn^{kp}).
  With Lemma E3.7 this gives ε_k = C(2k, k)pc^kζ(−kp, 1 + δ), which is S1.
- **What is not done: the index offset.** At t → 0 (z → ∞), j_δ behaves as (δ + ½)ln t + LnΓ(−δ) for δ ∈ (−1, 0), against −½ln t
  for δ = 0, where Γ(t) has its pole at t = 0. This changes the outer scalar's power of z at ∞, i.e. the normalisation
  U z^{−nσ₃} of Paper 2 Lemma interp. That is where d₁ = −(s−1)/2 − pδ must come from. The limit δ → 0⁻ is a crossover
  (the pole of Γ(t − δ) at t = δ approaches 0), so the bookkeeping has to be done with Paper 2's normalisation (O1)–(O5)
  redone, not read off from the exponent.
- For δ > 0 the fractional part enters through Lemma H, and the ⌈δ⌉ missing nodes enter through the zeros of 1/Γ(t − δ) at
  t = δ, δ − 1, … on the positive axis: phantom nodes beyond the top node, removed by rational factors (the S2 mechanism).

*p < 1.* The analogue is now checked too. In E_plt1 Lemma F.1(iii), with seams at θ = pπ/2 carrying the jumps
−Log(1 − e^{±2πiδ}e^{−2πnr^{−1/p}}), the two seam terms combine into Σ_m sin(2πmδ − πkp/2)/m^{1+kp}, the same Fourier sum. It
equals ζ(−kp, a)/(kn^{kp}); `checks/spec_hurwitz_moments_plt1.out`, p ∈ {0.3, 0.6, 0.75}, δ ∈ {0, −½, 0.3, 1.4}, k ≤ 3, relative
error ≤ 2·10⁻¹⁶, 10⁻³⁰ in most cases.

### 3.2 S2 from the Uvarov identity: Lemma U (PROVED) and Theorem S2′ (PROVED-mod-cite); REVIEWED

**Lemma U (PROVED, elementary).** Let σ = σ′ + w₀δ_{x₀} and F(m) := log D_m(σ) − log D_m(σ′), where D_m is the m×m Hankel
determinant. Then F(m) = log(1 + w₀K′_{m−1}(x₀, x₀)), with K′_{m−1}(x, x) = Σ_{j<m}p′_j(x)² the Christoffel–Darboux kernel of σ′
(orthonormal p′_j), and

  log b_n²(σ) − log b_n²(σ′) = F(n+1) − 2F(n) + F(n−1).

*Proof.* The moment matrix is a rank-one update, H_m(σ) = H_m(σ′) + w₀vvᵀ with v = (x₀^i)_{i<m}. So
det H_m(σ) = det H_m(σ′)(1 + w₀vᵀH_m(σ′)^{−1}v), and vᵀH_m(σ′)^{−1}v = K′_{m−1}(x₀, x₀). Finally b_n² = D_{n+1}D_{n−1}/D_n². ∎

**Theorem S2′ (deleting one atom of σ_{p,s}).** *Label: PROVED-mod-cite (inputs: the REVIEWED coefficient expansions below;
everything else is elementary and proved here), REVIEWED (REVIEW_SPEC_A.md).*

Let p > 0, s > 1, σ = σ_{p,s}, and ε := min(2p, 1) for 0 < p < 1, ε := 1 for p ≥ 1. Let x₀ = k₀^{−p} be an atom with mass w₀ = k₀^{−s}, and
σ′ := σ − w₀δ_{x₀}. Put u_n := 4c(k₀/n)^p and y_n := n^pb_n/c − 1. For every η ∈ (0, 1) there are C, n₀ (depending on p, s, η,
not on k₀) such that for all k₀ ≥ 1 and n ≥ n₀ with u_n ≤ 1 − η,

  n·(y_n(σ′) − y_n(σ)) = −p(1 − u_n)^{−1/2} + R,   |R| ≤ Cn^{−ε}.

So S2 holds outside a neighbourhood of the turning point. For fixed k₀ and n → ∞ only its u → 0 limit −p (the index shift) is
resolved by the statement; the first u-term, of size n^{−p}, is resolved only when ε > p, i.e. for p < 1 (ε = min(2p, 1) > p).
In the regime k₀ ∝ n the full function of u is resolved. Empirically R ≈ C(p)/(n(1 − u)^{3/2}), i.e. O(1/n) at every p tested
(REVIEW_SPEC_A F9: C ≈ 0.6–1.2 at p ∈ {0.3, 0.5, 0.6}, ≈ 2.95 at p = 1.5).

*Inputs (REVIEWED).* For σ_{p,s} and every p > 0:
- b_j = cj^{−p}(1 + d₁/j + κ_pj^{−1−p}·[p < 1] + O(j^{−1−ε}));
- α_j/(2b_j) = 1 − p/(2j) + O(j^{−1−ε}).
Sources (all in the α_n/(2b_n) pairing used here): E_pgt1 Theorem E.1 (p > 1, remainder O(j⁻²)); E_plt1 Theorem E′.1
(0 < p < 1, remainder O(j^{−1−2p} + j⁻²), the κ_p term explicit); E_p1 Theorem E1.10 (p = 1, remainder O(j⁻²)).
Hence, with β_j := α_j/(2b_j) − 1 and γ_j := b_{j+1}/b_j − 1:
- β_j, γ_j = O(1/j) and γ_j = −p/j + O(j^{−1−ε}) (the κ_p term contributes O(j^{−2−p}));
- Δβ_j, Δγ_j = O(j^{−1−ε}) (a first difference of an O(j^{−1−ε}) remainder is O(j^{−1−ε})).

*Proof.* Orthonormal polynomials P_j of σ satisfy b_{j+1}P_{j+1} = (x − α_j)P_j − b_jP_{j−1}.

(a) **Uvarov, reversed.** As in Lemma U with the roles exchanged, D_m(σ′) = D_m(σ)(1 − w₀K_{m−1}(x₀, x₀)), K_{m−1} = Σ_{j<m}P_j(x₀)².
Next, Σ_jP_j(x₀)² = 1/w₀ (no citation needed):
- *Extremal property.* For deg π < m with π(x₀) = 1, write π = Σ_{j<m}c_jP_j. Cauchy–Schwarz on 1 = Σc_jP_j(x₀) gives
  ∫π²dσ = Σc_j² ≥ 1/K_{m−1}(x₀, x₀), with equality for π = K_{m−1}(·, x₀)/K_{m−1}(x₀, x₀).
- *Lower bound.* Every such π has ∫π²dσ ≥ w₀π(x₀)² = w₀, so K_{m−1}(x₀, x₀) ≤ 1/w₀.
- *Upper bound.* x₀ is an isolated point of supp σ ⊂ [0, 1], since the atoms accumulate only at 0. Let d > 0 be its distance to
  the rest of the support, and T(x) := 1 − (x − x₀)²/2. Then T(x₀) = 1, and 0 < T ≤ θ := 1 − d²/2 < 1 on supp σ′. With π = T^N
  (deg 2N < m): ∫π²dσ ≤ w₀ + θ^{2N}σ′(ℝ) → w₀.
Hence K_{m−1}(x₀, x₀) ↑ 1/w₀, i.e. Σ_jP_j(x₀)² = 1/w₀. So 1 − w₀K_{m−1} = w₀T_m
with T_m := Σ_{j≥m}P_j(x₀)², and F(m) := log D_m(σ) − log D_m(σ′) = −log(w₀T_m). By b_n² = D_{n+1}D_{n−1}/D_n²,

  log b_n²(σ) − log b_n²(σ′) = F(n+1) − 2F(n) + F(n−1).

(b) **Contraction for the minimal ratio.** Write the recurrence at x₀ backwards in ratios: if Y_{j+1} = ρ_jY_j then
ρ_{j−1} = Φ_j(ρ_j), with Φ_j(ρ) := b_j/((x₀ − α_j) − b_{j+1}ρ).
- Put u_j := 4b_j/x₀; then u_j = u_n(n/j)^p(1 + O(1/n)) ≤ 1 − η/2 for j ≥ n − 1 ≥ n₀.
- On [0, 1], (x₀ − α_j) − b_{j+1}ρ ≥ x₀(1 − 3u_j/4)(1 + O(1/j)) > 0, so Φ_j maps [0, 1] into [0, 1] with Lipschitz constant
  ≤ (u_j/(4 − 3u_j))²(1 + O(1/j)) ≤ q < 1 (q = q(η)).
- Hence, for j ≥ n − 1, the backward iteration from any tail (equivalently, the contraction-mapping fixed point in ℓ^∞) defines
  ratios ρ̂_j ∈ [0, q^{1/2}], up to the O(1/j) factor. This gives a solution Ŷ with Ŷ_{j+1} = ρ̂_jŶ_j, decaying geometrically, so
  Ŷ ∈ ℓ².
- P(x₀) is also an ℓ² solution, by (a). The Casoratian b_j(P_jŶ_{j−1} − P_{j−1}Ŷ_j) is constant in j and tends to 0, so it is 0.
  Thus P_j(x₀) = κŶ_j for j ≥ n − 2, with κ ≠ 0 (P(x₀) ≢ 0 there, since T_m > 0). So P_{j+1}(x₀)/P_j(x₀) = ρ̂_j.

(c) **Frozen root.** Let σ_j be the small root of b_{j+1}σ² − (x₀ − α_j)σ + b_j = 0, i.e. the fixed point of the frozen map. In
terms of (u_j, β_j, γ_j), σ_j = S(u_j, β_j, γ_j) with S real-analytic near (u, 0, 0), u ≤ 1 − η/2, and
S(u, 0, 0) = (1 − u/2 − √(1−u))/(u/2) = 1/r(u) = u/4 + O(u²). So σ_j ≍ u_j, which may be small (a far node). All
estimates are therefore relative: write ρ̂_j = σ_j(1 + e_j). Since σ_j = Φ_j(σ_j),

  σ_{j−1}(1 + e_{j−1}) = Φ_j(σ_j(1 + e_j)) = σ_j + Φ_j′(ξ_j)σ_je_j,

i.e. e_{j−1} = θ_j e_j + D_j, with θ_j := Φ_j′(ξ_j)σ_j/σ_{j−1} and D_j := σ_j/σ_{j−1} − 1. Here:
- |θ_j| ≤ q′ < 1, since Φ_j′ ≤ (u_j/(4 − 3u_j))² and σ_j/σ_{j−1} = 1 + O(1/j);
- D_j = e^{Δlog σ_j} − 1 = Δlog σ_j + O(j⁻²). Solving the frozen quadratic (divided by x₀) exactly:
  σ_j = (u_j/2)/(A_j + √(A_j² − u_j²(1 + γ_j)/4)), with A_j := 1 − u_j(1 + β_j)/2.
  So log σ_j = log u_j + h(u_j, β_j, γ_j), with h(u, β, γ) := −log(2A + 2√(A² − u²(1 + γ)/4)). This h is real-analytic and bounded
  with all derivatives on u ∈ [0, 1 − η/2], |β|, |γ| ≤ δ₀; the discriminant at β = γ = 0 is 1 − u ≥ η/2.
- *No division by u.* Δu_j = u_{j−1}γ_{j−1} exactly, so Δlog u_j = log(1 + γ_{j−1}) = −p/j + O(j^{−1−ε}), and
  Δ²log u_j = O(|Δγ| + j⁻²) = O(j^{−1−ε}). Likewise Δ²u_j = Δu_{j−1}γ_{j−1} + u_{j−2}Δγ_{j−1} = O(j^{−1−ε}), and
  Δ²h_j = O(|Δ²u| + |Δ(u, β, γ)|² + |Δβ| + |Δγ|) = O(j^{−1−ε}).
- Hence D_j = O(1/j) and ΔD_j = O(j^{−1−ε}), uniformly in u_j ∈ (0, 1 − η/2].

Contraction gives e_j = O(1/j). The series e_{j−1} = Σ_{i≥j}D_iΠ_{l=j}^{i−1}θ_l converges: the a priori bound |e_J| ≤ 1/σ_J
grows only polynomially, while Πθ_l decays geometrically (θ_l ≤ Cu_l²), so the tail term vanishes. The same holds for ẽ. Put E_j := D_j/(1 − θ̄_j), with θ̄_j := Φ_j′(σ_j)σ_j/σ_{j−1}; θ_j − θ̄_j = O(e_j). Then
ẽ_j := e_j − E_j satisfies ẽ_{j−1} = θ_jẽ_j + O(|ΔE_j| + |e_j|²) = θ_jẽ_j + O(j^{−1−ε}), so ẽ_j = O(j^{−1−ε}). Also
ΔE_j = O(j^{−1−ε}), because E is built from slowly varying data. Hence Δlog(1 + e_j) = O(j^{−1−ε}).
Therefore Δlog ρ̂_j = Δlog σ_j + O(j^{−1−ε}) = (1 + u_jh_u(u_j, 0, 0))Δlog u_j + O(j^{−1−ε}). The β, γ dependence of h_u
contributes O(1/j)·Δu_j. Since 1 + uh_u(u, 0, 0) = u∂_u log S(u, 0, 0) = 1/√(1 − u),

  log ρ̂_j − log ρ̂_{j−1} = −p/(j√(1 − u_j)) + O(j^{−1−ε}),   and   Δ²log ρ̂_j = O(j^{−1−ε})

(the main term has differences O(j⁻²), since Δu_j = O(u_j/j)).

(d) **Tail sums.** T_m = P_m(x₀)²G_m with G_m = 1 + ρ̂_m²G_{m+1} = Σ_{i≥0}Π_{l<i}ρ̂_{m+l}². Claim: Δ²log G_m = O(m^{−1−ε}),
uniformly in u. (Argument from REVIEW_SPEC_A §2.4.)
- Put Ḡ_m := 1/(1 − ρ̂_m²) and f_m := G_m − Ḡ_m. Then f_m = ρ̂_m²f_{m+1} + ρ̂_m²(Ḡ_{m+1} − Ḡ_m), so
  f_m = Σ_{i≥0}π_{m,i}ΔḠ_{m+i+1}, with π_{m,i} := Π_{l=0}^{i}ρ̂²_{m+l} ≤ q^{i+1}.
- log Ḡ is a smooth function of log ρ̂ on ρ̂² ≤ q. So by (c), ΔḠ = O(1/m) and Δ²Ḡ = O(|Δ²log ρ̂| + |Δlog ρ̂|²) = O(m^{−1−ε}).
- Write f_m − f_{m−1} = Σ_i(π_{m,i} − π_{m−1,i})ΔḠ_{m+i+1} + Σ_iπ_{m−1,i}Δ²Ḡ_{m+i+1}. Since
  π_{m,i}/π_{m−1,i} = exp(2Σ_{l=m}^{m+i}Δlog ρ̂_l) = 1 + O((i + 1)/m)e^{C(i+1)/m}, the first sum is O(m⁻²) (for m ≥ n₀ with
  qe^{C/n₀} < 1) and the second is O(m^{−1−ε}). So Δf = O(m^{−1−ε}) and f = O(1/m).
- log G = log Ḡ + log(1 + f/Ḡ), with Ḡ ≥ 1. Then Δ²log Ḡ = O(m^{−1−ε}), and Δlog(1 + f/Ḡ) = O(|Δf| + |f||ΔḠ|) = O(m^{−1−ε}),
  so its second difference is O(m^{−1−ε}) as well.
Numerically this term is O(n⁻²)·(a function of u) (REVIEW_SPEC_A T2). Then

  F(m+1) − F(m) = −log(T_{m+1}/T_m) = −2 log ρ̂_m − log(G_{m+1}/G_m),

so F(n+1) − 2F(n) + F(n−1) = −2(log ρ̂_n − log ρ̂_{n−1}) + O(n^{−1−ε}) = 2p/(n√(1 − u_n)) + O(n^{−1−ε}).

(e) **Conclusion.** By (a), log b_n(σ′) − log b_n(σ) = −p/(n√(1 − u_n)) + O(n^{−1−ε}). Since 1 + y_n(σ) = 1 + O(1/n), we get
n(y_n(σ′) − y_n(σ)) = n(1 + y_n(σ))(b_n(σ′)/b_n(σ) − 1) = −p(1 − u_n)^{−1/2} + O(n^{−ε}). All constants depend only on (p, s, η)
through the input remainders and q(η). ∎

*Remarks.*
- Only leading-order smoothness of the coefficients enters, never the band factor or the gauge. So S2′ is independent of the RH
  tilt sketch under S2, and agrees with it.
- The proof breaks exactly at u → 1, where q(η) → 1 (the turning point; Airy scaling 1 − u ~ n^{−2/3}). That is where the measured
  ratio drops (0.956 at u = 0.954, §2), and where jittered nodes generate noise (S4). So S4 is a turning-point phenomenon:
  each node crossing u = 1 contributes an Airy-smoothed step, whose timing jitter scatters.
- *Adding* a node outside the band, or deleting finitely many nodes, is the same argument iterated: Lemma U applied repeatedly,
  each step an atom of the current measure. That needs the input expansions for the modified measure, which are not proved.
  S2′ itself is the only case proved here.

Check (`checks/spec_uvarov.out`; p = 0.6, s = 2, k₀ = 30). This uses the cached coefficients of σ and σ′ and the orthonormal
polynomials of σ′ at x₀.
- Lemma U holds to relative 6·10⁻¹² for n ∈ [100, 1500], limited by the cache precision.
- p′_n(x₀)/p′_{n−1}(x₀) = 22.3217 against r(u_n) = 22.3034 at n = 1500, and 2.468 against 2.374 at n = 100: a relative gap
  of O(1/n). This tests the dominant solution of σ′, not the proof's minimal solution of σ, whose ratio tends to the reciprocal
  1/r(u) = S(u, 0, 0) (the product of the frozen roots is b_j/b_{j+1} → 1).
- The proof's own chain (b)–(d) was tested by the reviewer (REVIEW_SPEC_A T2, script chain.py in the review scratch). It uses
  σ's coefficients alone (backward contraction, minimal ratios, tail sums) and reproduces the measured
  log b_n²(σ)/b_n²(σ′) to 10⁻¹²–10⁻¹⁶ at p ∈ {0.3, 0.5, 0.6, 1.5}. j·e_j stays bounded, and Δ²log G = O(n⁻²).

### 3.3 The bouncer zeta values in closed form (PROVED-mod-cite pending Rule C for two classical inputs; NOT REVIEWED)

H = −d²/dx² + x on (0, ∞), with Dirichlet condition at 0; its eigenvalues are E_k = −a_k (the Airy zeros). Let Z_E(w) := Σ_kE_k^{−w}.

**Proposition B.** For j = 0, 1, 2, …, Z_E(−j) = (−1)^j·[z^{−j−1}](Ai′/Ai)(z), the coefficient in the large-z asymptotic
expansion. In particular Z_E(−j) = 0 unless 3 | j, and

  Z_E(0) = −1/4,  Z_E(−3) = 15/64,  Z_E(−6) = −1695/1024,  Z_E(−9) = 59025/2048.

The heat trace is Θ(t) = Σe^{−tE_k} = (4π)^{−1/2}t^{−3/2}e^{t³/12} − 1/4 + β₁t^{3/2} + β₂t³ + β₃t^{9/2} + …, with boundary coefficients
β₁ = 1/(6√π), β₂ = −5/128 and β₃ = 25/(1512√π).

*Proof.*
- **Resolvent trace.** Ai is entire of order 3/2, with zeros exactly the a_k < 0. By Hadamard's factorisation (genus 1;
  NOT QUOTED, Rule C), Σ_k[1/(z + E_k) − 1/E_k] = Ai′(z)/Ai(z) − Ai′(0)/Ai(0).
- **Large-z expansion.** By DLMF 9.7.5–9.7.6 with u_k, v_k from 9.7.2 (quoted in RH/CITATIONS.md "(DLMF-9, Paper 2)",
  "(DLMF-9.7.2, Plan 65)"), Ai′/Ai = −z^{1/2}·[Σ(−1)^kv_kζ^{−k}]/[Σ(−1)^ku_kζ^{−k}], with ζ = (2/3)z^{3/2}, in |ph z| ≤ π − δ. The
  k-th term is ∝ z^{(1−3k)/2}, which is an integer power only for odd k, namely z^{−1}, z^{−4}, z^{−7}, ….
- **Mellin correspondence** (standard, NOT QUOTED). For 0 < Re w < 2, ∫_0^∞z^{1−w}(z + E)^{−2}dz = E^{−w}Γ(w)Γ(2 − w). So
  Z_E(w) = (sin πw/(π(1 − w)))∫_0^∞z^{1−w}R₂(z)dz, with R₂ = −(Ai′/Ai)′ = Σ(z + E_k)^{−2} (valid for 3/2 < Re w < 2).
  Continue analytically by subtracting the asymptotic terms of R₂ at ∞. At w = −j the zero of sin πw cancels the pole produced
  by the z^{−j−2} term of R₂, which gives Z_E(−j) = (−1)^j[z^{−j−1}](Ai′/Ai). Equivalently, a heat-trace term c_at^a corresponds
  to c_aΓ(a + 1)z^{−a−1}.
- **Coefficients.** These are exact sympy rational arithmetic (`checks/spec_bouncer_closed.py`). The half-integer coefficients
  minus those of the bulk term (4π)^{−1/2}t^{−3/2}e^{t³/12} give β₁, β₃. ∎

*Checks* (`checks/spec_bouncer_closed.out`, `checks/spec_bouncer_heat.out`; NUMERICAL, independent of the proof):
- The Hurwitz-regularised Airy-zero sums of §2 (WKB series plus exact low zeros, 40 digits) give Z_E(0), Z_E(−3) and Z_E(−6)
  to 0, 3·10⁻²⁴ and 7·10⁻¹⁸.
- The heat-trace fit gives β₁ = 0.094031587 (closed form 0.0940315973) and β₂ = −0.0390622 (closed form −0.0390625), and a fitted
  β₃ ≈ 0.00933 (closed form 0.0093285).
Z_E(−9) is not independently checked: the zero sums would need more WKB terms.

*Consequences for S1* (normalised eigenvalues λ′ = E/(3π/2)^{2/3}, Z_{λ′}(−j) = (3π/2)^{−2j/3}Z_E(−j)):
- d₁ = −pα/2 − p/4.
- ε₁ = ε₂ = 0, and ε₃ = 20pc³(3π/2)^{−2}·15/64.
The ε₃ term sits at n^{−1−3p} = n^{−3}, where it merges with the n⁻³ term, below the resolution of the §2 fits. *Correction
(REVIEW_SPEC2_A F2):* the n⁻³ coefficient is **not** predicted by ε₃ alone. The q = 3/2 pole of Z_E (from the z^{1/2} term of
Ai′/Ai) has its leading term killed by cot(3π/2) = 0, but its subleading term, also at n^{−2−pq} = n⁻³, is not (§3.12,
Limitation). The bouncer's n⁻³ coefficient is therefore an open prediction, not an exact one.

*Remaining proof gaps* (REVIEW_SPEC2_A F9): the continuation step needs the remainder bound of the large-z expansion (DLMF
§9.7(iv), or a sector-analyticity argument) and term-by-term differentiation of it (R₂ = −(Ai′/Ai)′); Hadamard needs order
3/2 < 2, genus 1. Both are classical and stay under "pending Rule C". The same expansions give the poles of Z_E exactly: a term
z^{−a−1} of F′/F with non-integer a is a pole at s = −a. Dirichlet: q ∈ {3/2, 9/2, …}; Robin (all orders in h) and Bessel:
q ∈ {½, 3/2, 5/2, …}. So "every pole sits at a half-integer" (§3.12) follows from these expansions, not only from WKB parity.

### 3.4 Direction 3: reading off the Maslov index (NUMERICAL; S1 test with an exact prediction)

For WKB-regular spectra λ_m ≈ (m + μ/4)^p (m ≥ 0), with μ the Maslov index, Z(0) = ζ(0, μ/4) = ½ − μ/4. So S1 gives

  d₁ = −pα/2 + p(½ − μ/4),

and the 1/n coefficient of b_n reads off μ. The test changes only the boundary condition of the bouncer: Dirichlet ψ(0) = 0,
E = −a_k, μ = 3; against Neumann ψ′(0) = 0, E = −a′_k, μ = 1 (`checks/spec_neumann.out`).
- **Zeros.** a′_k from the asymptotic series (DLMF 9.9-type, five terms), checked against mpmath.airyaizero(k, 1) for
  k ∈ [41, 200] to 4·10⁻¹⁶ relative.
- **Zeta values, exact.** As in Proposition B, with z·Ai/Ai′ in place of Ai′/Ai: Z_E(0) = +1/4, Z_E(−3) = −21/64,
  Z_E(−6) = 2121/1024, Z_E(−9) = −136479/4096, and all others vanish.
- **S1 at p = 2/3, s = 2.** Predicted d₁ = 0 (Neumann) against −1/3 (Dirichlet); fitted d₁ = 0.00000000 ± 1.2·10⁻⁷. Predicted
  ε₁ = 0; fitted n^{−5/3} coefficient 5·10⁻⁷ ± 8·10⁻⁵.

So b_n distinguishes the two boundary conditions exactly, through ζ(0, μ/4).

### 3.5 Where the regularity hypothesis matters: λ_k = k^p + κ (NUMERICAL)

A constant shift of every eigenvalue (adding the constant κ to the potential) gives λ^{1/p} = k + (κ/p)k^{1−p} + …, which is
not of the form m + a + O(1/m). S1 does not apply, and indeed the effect is of a different order (`checks/spec_kappa.out`,
`checks/spec_kappa_fit.out`; p = 0.6 and 0.3, s = 2): Δy_n = y_n(κ) − y_n(0) is of relative order n^{−p}, not n^{−1−p}.
- **Linear in κ.** The κ = ½ run gives half the κ = 1 value.
- **Leading coefficient.** Least-squares fits of n^pΔy_n = L + Σ_iA_in^{−e_i} give L = −1.2034, −0.6015 and −1.2231 at
  (p, κ) = (0.6, 1), (0.6, ½) and (0.3, 1). The candidate −2(2−p)cκ gives −1.2025, −0.6012 and −1.2226. The fit half-ranges are
  large: at p = 0.3 the half-range is 0.74 (60%), so the 0.1% agreement there is luck and not evidence (REVIEW_SPEC2_B F5);
  the real evidence at p = 0.3 is the convergent spec_mobius_pred ratio below. *Rule X:* the p = 0.6, κ = 1 row was the
  identification target for the candidate; only the other rows, the Möbius derivation and the out-of-sample p = 1.5 run
  (§3.12) test it.
- **It is a pole-law term** (REVIEW_SPEC2_A F3; §3.12). κ moves the Weyl pole of Z to q = 1 − 1/p, and the pole law reproduces
  −2(2−p)cκ exactly for all p. An out-of-sample run at p = 1.5, κ = 1 (reviewer A) gives L = −0.5662723 ± 1.3·10⁻⁶ against
  −0.5662723.
- **Exact identity (Proposition M; PROVED, elementary).** The shift is the Möbius map φ(y) = y/(1 + κy) on the nodes y = 1/λ.
  Since φ(a) − φ(b) = (a − b)/((1 + κa)(1 + κb)), Heine's formula gives

    D_m(σ_κ) = D_m((1 + κy)^{−2(m−1)}σ′),  σ′ := (1 + κy)^{−s/p}σ,

  so the shifted measure is the old nodes with a weight that varies with m. Checked at 50 digits on a random 9-atom measure,
  m ≤ 7 (`checks/spec_mobius.out`).
- **First-order derivation (HEURISTIC; checked).** For μ_N := (1 + κy)^{−2N}σ′, ∂_N log D_m(μ_N) = −2∫log(1 + κy)K_{m−1}(y, y)dμ_N
  (expectation of a linear statistic). To first order in κy this is −2κTr J_m = −2κT(m), with T(m) = Σ_{j<m}α_j. So
  log D_m(σ_κ) ≈ log D_m(σ′) − 2κ(m−1)T(m). Then:
  - log b_n² = Δ²log D at m = n gives log b_n²(σ_κ) − log b_n²(σ) ≈ Δ²_m[−2κ(m−1)T(m)];
  - with α_j ≈ 2cj^{−p}, this is −4(2−p)cκn^{−p}, i.e. Δy_n ≈ −2(2−p)cκn^{−p}, which is the numerical candidate;
  - neglected: the tilt (1 + κy)^{−s/p} (order n^{−1−p}), the O(κ²y²) term and the N-dependence of μ_N (order κ²n^{−2p}).
    For p < 1 the tilt (1 + κy)^{−2N} is not small in absolute terms (2Nκy ~ κn^{1−p} on the band); it is small per particle
    (relative n^{−p}), which is the sense the estimate uses (REVIEW_SPEC2_A F13).
  Check (`checks/spec_mobius_pred.out`): Δ²G built from the actual α_j of σ, against the measured log-ratio. The ratio
  measured/predicted is 0.955 → 0.995 (p = 0.6, κ = 1, n = 50 → 1500), 0.970 → 0.997 (κ = ½), and 0.859 → 0.947 (p = 0.3). The gap
  decays like κn^{−p} (0.0069 → 0.0047 from n = 800 to 1500, against (1500/800)^{0.6} = 1.46), i.e. it is the second-order term.
  A proof would need leading-order Law P for σ′ and a bound on ∂²_N log D_m (a variance of a linear statistic).

Lesson: S1's hypothesis is necessary. A smooth spectral deformation whose index drift grows (k^{1−p}) moves the leading
asymptotics, while one with bounded index offset (Hurwitz, WKB) only shifts the 1/n-order series.

### 3.6 Direction 4: the noise mechanism and spectral statistics (NUMERICAL; single realisations)

**Single-node kernel** (`checks/spec_turning.out`; p = 0.6, s = 2). Node 300 is moved by h = ±0.3, and D(n) := n(y_n(moved) − y_n(pure))
is followed as the edge threshold k* = 0.406n passes it (u = 1 at n* = 739):
- **Outside the band (u < 1, n ≥ 760).** D matches the differentiated S2′ formula p[(1 − u_a)^{−1/2} − (1 − u_l)^{−1/2}] to
  0.2–2% (ratio 0.998 at n = 1600, 0.976 at u = 0.968). It is linear: max|D(+h) + D(−h)| = 3·10⁻⁵ against |D| ~ 4·10⁻³ on [900, 1600].
- **Inside the band near the edge (1 < u ≲ 2, n ∈ [300, 740]).** |D| = O(0.1–1). D alternates in sign from one n to the next
  and is strongly nonlinear: D(+h) + D(−h) is as large as D. Deeper in the band (u ≳ 3, n ≤ 200), |D| ~ 10⁻⁴–10⁻².
So a node a fraction of a spacing off the lattice changes b_n by an oscillating O(1/n), wherever it sits in the outer band,
not only at the turning point. With ~n such nodes displaced independently this gives the n^{−1/2} relative noise of S4.
Because the kernel oscillates on the scale of one spacing, displacements with a rigid counting function (difference jitter)
do not cancel it, which is what S4 found.

**GUE-like against Poisson nodes** (`checks/spec_stats_seeds.out`, seed 7). The first M = 3000 nodes are replaced by unfolded CUE eigenphases
(max |x_k − k| = 3.3) or by a Poisson bridge (max |x_k − k| = 36); the lattice is kept beyond M.

Five seeds per ensemble (7, 11, 13, 17, 19; `checks/spec_stats_seeds.out`, summary `checks/spec_stats_summary.out`). Mean and
seed-to-seed standard deviation of RMS n(y − y_lat) per window:

| n-window | GUE-like | Poisson | ratio |
|---|---|---|---|
| [50, 100) | 2.67 ± 0.36 | 8.7 ± 2.5 | 3.3 |
| [100, 200) | 3.76 ± 0.34 | 15.0 ± 4.8 | 4.0 |
| [200, 400) | 5.38 ± 0.18 | 19.3 ± 3.4 | 3.6 |
| [400, 800) | 7.40 ± 0.33 | 26.3 ± 2.1 | 3.6 |
| [800, 1600) | 10.68 ± 0.50 | 39.8 ± 5.1 | 3.7 |

- **Growth.** The mean RMS grows like n^{0.50} (GUE-like) and n^{0.52} (Poisson), so the relative noise in y is ~ n^{−1/2} for both.
  This is the same exponent as iid jitter; the single-seed estimate n^{0.4} was a fluctuation.
- **Amplitude.** Poisson is larger by a stable factor of 3.3–4.0 (mean 3.6).
- **Self-averaging.** The GUE-like amplitude is nearly deterministic (seed-to-seed spread ≈ 5%, against 15–30% for Poisson):
  RMS ≈ 0.32·n^{1/2} for GUE-like, ≈ 1.2·n^{1/2} for Poisson, at p = 0.6, s = 2.
- **Predictors.** Neither the count predictor p·Δ(n) (node-count deviation below the threshold) nor the per-node S2′ sum
  explains the noise: correlations −0.3 to 0.66, typically 0.1–0.4, and residual RMS reduced by ≤ 25%. This is consistent with the
  kernel above, where the in-band oscillatory responses dominate.

So the fluctuations of b_n distinguish GUE-like from Poisson spectra by amplitude, reproducibly across seeds (NUMERICAL). Open:
- a theory for the amplitude constant, e.g. as an integral of the single-node kernel against the pair correlation of the
  spectrum. If such a formula holds, the GUE/Poisson ratio follows from the two pair correlations;
- the dependence on p and s;
- the autocorrelation in n.

### 3.7 Direction 2: the spectral determinant as the organising object (CONJECTURE / HEURISTIC; NOT REVIEWED)

**What is true already.** Let Δ_Λ(w) := Π_m(1 − w/λ_m) be the (zeta-regularised) spectral determinant.
- **Lattice.** For λ_m = m^p, the Mellin transform of log(1 + x/m^p) summed over m is ζ(−ps)·π/(s sin πs). The poles at
  s = 1, 2, … give the integer-power part of the large-x expansion of log Δ(−x): Σ_{k≥1}(−1)^{k+1}ζ(−kp)x^{−k}/k. Continuing to
  w = −x, the integer-power part of log Δ_Λ(w) is R_Λ(w) = −Σ_kZ_Λ(−k)w^{−k}/k.
- **Bouncer.** Δ ∝ Ai, and Proposition B is exactly this statement.
- **Consequence.** With w = n^p/z, 2R_Λ(n^p/z) = −2Σ_kZ_Λ(−k)z^k/(kn^{kp}) is precisely the band-factor law of E3 (Lemmas F.1/F.1′)
  and of S1. So the band factor is the regular part of the squared spectral determinant evaluated at the rescaled spectral
  variable: H_n(z) ∝ exp(2R_Λ(n^p/z)).

**What is not literally true.** For p ≠ 1, Paper 2's Γ(t) is not Δ_Λ. It is the mirror product Π(1 + t/k) in the index variable
t = nz^{−1/p} (w = t^p), and the construction uses the analytic index map t(z) (BKMM-style), with its cut on (−∞, 0).

**Conjecture S5 (determinant construction).** For a node set Λ whose determinant Δ_Λ satisfies
- (P1) Δ_Λ is entire, with simple zeros exactly at the λ_m > 0;
- (P2) uniform sectorial asymptotics of log Δ_Λ off the positive axis, with explicit error bounds (Stirling's role);
- (P3) a two-exponential decomposition on the node ray (the role of sin πt = (e^{iπt} − e^{−iπt})/2i);
- (P4) a Weyl term (the singular part of log Δ_Λ) of power type λ^{1/p}, matching the equilibrium constant c(p);
an interpolation/outer construction can be built in the w-plane directly from Δ_Λ, with no analytic index function. Its band
factor is exp(2R_Λ), and S1 follows with Lemma E3.7.

**The bouncer instance.** Here Δ ∝ Ai(−Cw), and the four properties are available from quoted sources:
- (P1) the zeros of Ai are real, negative and simple;
- (P2) DLMF 9.7.5–9.7.6 in |ph z| ≤ π − δ, with the error bounds of §9.7(iv) (not yet quoted);
- (P3) the connection formula 9.2.12, Ai(z) + e^{−2πi/3}Ai(ze^{−2πi/3}) + e^{2πi/3}Ai(ze^{2πi/3}) = 0, quoted in RH/CITATIONS.md.
  On the node ray it splits Ai(−x) into two terms ~ e^{±i(2/3)x^{3/2}};
- (P4) Proposition B's leading terms.
So a "Paper 2 for Airy nodes" is a concrete plan, with Airy sector lemmas replacing the Γ-sector lemmas (binetcut, seam).

**Why it matters.** (P1)–(P4) do not require λ_m = G(m) with G analytic. They hold for any spectrum whose determinant has
WKB-type sectorial asymptotics, which includes Robin and inhomogeneous potentials. For chaotic spectra, log Δ on the node ray
fluctuates at the scale of the spacing, so (P3) fails in the way S4 and §3.6 see.

### 3.8 The bouncer inside Paper 2's framework: an exact analytic index map (NUMERICAL check; plan)

Paper 2 builds the interpolation from an analytic index map t(z) with t = k at the nodes (t = nz^{−1/p} for the lattice). For the
bouncer such a map exists exactly, through the Airy modulus-phase form (DLMF §9.8; NOT QUOTED).
- **The map.** Let φ(x) := arg(Ai(−x) + iBi(−x)), continuous on x ≥ 0, with φ(0) = π/3 and φ′ = 1/(πM²) by the Wronskian
  W(Ai, Bi) = 1/π. Then t(x) := φ(x)/π − 1/6 satisfies t(−a_k) = k exactly: checked for k ≤ 60 to 20 digits
  (`checks/spec_airy_index.out`).
- **Asymptotics.** t(x) = (2/(3π))x^{3/2} + 1/4 + O(x^{−3/2}): the difference is 1.0·10⁻³, 3.3·10⁻⁵ and 1.0·10⁻⁶ at x = 10, 100
  and 1000.
- **In the rescaled variable.** With x = Cn^p/z (C = (3π/2)^{2/3}, p = 2/3): t(z) = nz^{−3/2}·(1 + corrections) + 1/4.

So the bouncer is Paper 2's lattice construction with three changes:
- **(i) Hurwitz offset.** The index is shifted by a = 3/4, which is §3.1's case δ = −1/4 (the index-offset step there is still
  open).
- **(ii) A deformed index map.** t(z) − (nz^{−1/p} + 1/4) = O(z^{3/2}/n), analytic, and small on compact z-sets.
- **(iii) Weights.** λ′^{−s/p} as a function of t, i.e. a smooth deformation of t^{−s}.
In the band (z bounded, t ~ n) the deformation (ii) has relative size O(n^{−2}). But for the far nodes (small t) it is O(1), and
there it produces the WKB part of Z(−j): the cancellation that makes the bouncer's ε₁ = ε₂ = 0.

**Plan (not done).**
1. Redo Paper 2 Lemma interp and the outer scalar with t(z) := φ(Cn^p/z)/π − 1/6. Node masses become smooth functions of t, and
   sin πt and 1/Γ(t) are unchanged as functions of t. The Binet scalar j(t) is then composed with a different t(z).
2. The band factor's jump on the cut is again Log(1 − e^{−2πit₊}), now with t₊ the boundary value of the deformed map. Its
   moments ∫ (…)y^{−k−1}dy should give Z_{λ′}(−k). This is the analogue of Lemma F.1′/H, provable from the moment integral in the
   variable t, where the integrand is the same and only the Jacobian dy/dt changes.
3. The (P1)–(P4) of §3.7 are this construction written invariantly. For spectra without an exact phase function, the
   determinant route of §3.7 is the general version.

### 3.10 The two-layer structure: Conjecture S1′ (NUMERICAL; refines S1)

**Conjecture S1′.** For a regular node set Λ (§1), write Z = Z_Λ, d_i⁰ = d_i(p, s) for the lattice coefficients (d₁⁰ = −(s−1)/2,
d₂⁰ = E2's closed form), and δ := −Z(0) − ½ (the constant term of the smoothed counting function, read as an index offset).
Then the expansion of n^pb_n/c separates into two layers:
- **(I) Integer layer.** The integer-order coefficients are those of the lattice with n ↦ n + δ:
  1 + Σ_id_i⁰(n + δ)^{−i}, multiplied by (n/(n + δ))^p, then re-expanded in 1/n. In particular d₁ = d₁⁰ − pδ, and
  d₂ = d₂⁰ + p(p+1)δ²/2 − (p+1)δd₁⁰.
- **(II) Zeta layer.** The n^{−1−jp} coefficients are ε_j = C(2j, j)pc^jZ(−j). These are new spectral data, not produced by an
  index shift.
- **Merging.** At p = 1/j the two layers merge at n⁻², and the coefficient is the sum d₂ + ε_j = d₂ + pZ(−j), using
  C(2j, j)c(1/j)^j = 1.
For Λ = {m^p}, δ = 0 and (I), (II) reduce to E2/E3 (PROVED, REVIEWED). S1 is (II) together with d₁ from (I).

**Evidence** (all predictions computed from the formula, nothing fitted to them):

| Test | Layer | Result |
|---|---|---|
| Hurwitz lattices, d₂ (`checks/spec_hur_d2.out`) | I | p = 0.6 (δ = −½, ½, 1), 0.75, 1.5: agreement to 2·10⁻⁶ … 3·10⁻⁵ (fit spreads 3·10⁻⁵ … 9·10⁻⁴); the d₂ shifts are 0.3 to 3 |
| Bouncer (Dirichlet δ = −¼, Neumann δ = −¾), d₂ (`checks/spec_bouncer_d2.out`) | I | 9·10⁻⁵, 2·10⁻⁵ (s = 2), 1.2·10⁻³ (s = 3, spread 1.5·10⁻²); the WKB corrections enter only at n⁻³ |
| Bessel zeros, p = s = 2 (`checks/spec_lommel.out`) | I, exact | closed form from the Lommel recurrence, n²b_n/c = 4n²/((2n+μ)√((2n+μ)² − 1)) = [n/(n+δ)]²G(n + δ), δ = μ/2 − ¼: an exact index shift of the p = 2 lattice to all orders; checked against Bessel-zero measures to 10⁻¹⁵ (μ = 0, 1.5). The exactness at n⁻³ arises by cancellation of a subleading pole term against ε₁ (§3.12, Limitation), not by absence |
| Hurwitz p = 1/3, δ = −½ (`checks/spec_hur_small.out`) | II and merged | ε₁, ε₂ = Hurwitz to 5·10⁻⁷, 3·10⁻⁵; merged n⁻² = d₂^shift + ⅓ζ(−1, ½) to 3.5·10⁻⁵ (spread 1.9·10⁻³; without the ζ term off by 1.4·10⁻², i.e. 7 spreads) |
| Hurwitz p = 1/4, δ = −½ | II and merged | ε₁, ε₂, ε₃ = Hurwitz to 4·10⁻⁷, 9·10⁻⁶, 3·10⁻⁴ (spreads 5·10⁻⁵, 5·10⁻⁴, 10⁻²); merged consistent (2·10⁻³, spread 9·10⁻³; weak) |
| Earlier: §2 (ε₁ for Hurwitz, moved nodes, bouncer), §3.4 (Maslov) | I, II | as reported |

**Reading.** The node set enters b_n through two independent channels:
- its counting function, in the integer layer. *Superseded* (REVIEW_SPEC2_A F7): "only Z(0) is needed" is false in general.
  Decaying index corrections γk^{−m} enter at n^{−1−m} through the pole law (§3.11(b), §3.12); they are invisible for the
  bouncer only because cot = 0 at its half-integer poles;
- its regularised power sums Z(−j), in the zeta layer.
The structural reason is visible in the proofs. The integer layer comes from the model weight and the index normalisation
(Paper 2's interpolation in t), while the zeta layer is the band factor (Lemmas F.1/F.1′/H) fed through the exact linear
response of Lemma E3.7.

**Open.**
- ~~Whether the zeta-layer terms are ε_j n^{−1−jp} or ε_j (n + δ)^{−1−jp}.~~ Answered by §3.11(a) for Hurwitz lattices: shifted,
  ε_j(n + δ)^{−1−jp} times (n/(n + δ))^p.
- The integer layer beyond Z(0): which spectral data (the Weyl-term coefficients of N̄) enter d₃ (bouncer).
- A proof of (I) for Hurwitz lattices. This is §3.1's open index-offset step, now with a sharper target: an exact index shift
  of the integer layer.

### 3.11 Probes of S1′: higher orders, and the first non-Z(0) integer datum (NUMERICAL)

**(a) Hurwitz lattices obey one exact rule to the orders tested** (`checks/spec_shift_hi.out`; p = 1.5, s = 2,
δ ∈ {−½, ½, 1}). The rule is hypothesis H:

  n^pb_n(a)/c = (n/(n+δ))^p·Φ(n + δ),

where Φ is the lattice expansion as a function of N, with every ζ(−jp) replaced by ζ(−jp, a). Two checks:
- **d₃ (integer layer, third order).** The rule built from d₁⁰, d₂⁰ and the fitted d₃⁰ predicts d₃(δ) to 9·10⁻⁷, 2·10⁻⁵ and
  7·10⁻⁵ in the reported fit configuration. The d₃ shifts are 0.37, 1.5 and 5.7. These are best-case medians: within
  same-configuration ranges the agreement is 1·10⁻⁴, 2·10⁻³ and 1.3·10⁻² (REVIEW_SPEC2_B F5), i.e. relative 3·10⁻⁴ to 2·10⁻³ of
  the shifts. The prediction uses the fitted d₃⁰, so it tests the δ-dependence only.
- **The n^{−3.5} coefficient (zeta layer under the shift).** H predicts f(δ) = ε₁(a)[f(0)/ε₁(1) − (1 + 2p)δ]; the fits agree to
  4.5·10⁻⁵, 1.1·10⁻³ and 5.4·10⁻³ (spreads ≈ 0.14). The alternative "zeta layer unshifted" is off by 0.056, 1.1 and 7.0, so
  δ = ½ and 1 discriminate; δ = −½ (0.056 against a spread of 0.14) does not. The prediction assumes that the lattice
  n^{−2−p} coefficient f(0) is ζ(−p) times a function of (p, s) (REVIEW_SPEC2_A F12).
So for Hurwitz lattices the whole expansion, both layers, is the lattice expansion at n + δ with Hurwitz zeta values.

**(b) Decaying index corrections** (`checks/spec_gamma.out`). Synthetic lattices λ_k = (k + γ/k^m)^p keep
the count, so Z(0) is unchanged.
- **Zeta layer.** ε₁ = 2pc·Z(−1) with the exact regularised Z(−1): agreement 3·10⁻⁶ (p = 0.6) and 9·10⁻⁴ (p = 1.5).
- **m = 2.** After the exact zeta-layer change is subtracted, Δd₂ = 0 to print precision.
- **m = 1.** Δd₂ = γ·1.81380, exactly linear in γ (γ = −½, ½, 1). It is the same at p = 0.6 and 1.5 and at s = 2 and 3, and the
  same when the correction acts only on k > 50 (1.8136, converging). *Correction (§3.12):* the constant is −π·cot(π/p). At
  p = 0.6 and 1.5 it equals π/√3 only because cot(5π/3) = cot(2π/3) = −1/√3. It is not p-independent: it is checked at
  p = 0.75, 0.8, 1.25 and 1.8 to 10⁻⁶.
- **Interpretation (HEURISTIC).** A γ/k index correction gives Z(s) = Σ(k + γ/k)^{−ps} a pole at s = −1/p, with residue γ/p.
  The generalised identity C(2q, q)c(p)^q = 1 at q = 1/p (a consequence of c(p)'s definition and the duplication formula;
  C(2j, j)c(1/j)^j = 1 is its integer case) makes the "j = 1/p" member of the zeta layer land at n^{−1−p·(1/p)} = n⁻². With the
  prefactor p cancelling the residue's 1/p, Δd₂ = γ·(an s-independent constant); §3.12 gives it as −γπcot(π/p). So the integer layer is the zeta
  layer's pole part. If this is right, S1′ becomes a single statement: all poles and zeta values of Z, each entering through
  C(2q, q)c^q with q the location.
- **Consequence for the bouncer** (corrected in §3.12). λ′ = (k − ¼)^{2/3}(1 + O(k⁻²)) gives λ′^{3/2} = (k − ¼) + γ₁/(k − ¼) + …, an
  m = 1 index correction. It is invisible in d₂ because cot(π/p) = cot(3π/2) = 0, not because it is O(k⁻²). Its subleading
  term at n⁻³ is not killed (§3.12, Limitation).

### 3.12 The pole law (NUMERICAL; HEURISTIC derivation; REVIEWED with fixes: REVIEW_SPEC2_A F1–F3, F8; REVIEW_SPEC2_B F1, F3, F5, F8)

**Statement.** Write the zeta layer as a Mellin–Barnes integral,

  (p/n)·Σ_jW(j)Z(−j)n^{−jp} = −(p/n)·(1/2πi)∫_↑W(w)Z(−w)·π cot(πw)·n^{−wp}dw,
  W(q) := C(2q, q)c^q = (4c)^qΓ(q + ½)/(√πΓ(q + 1)).

Here π cot(πw) has residue 1 at every integer, and closing the contour to the right gives +ΣRes, so the integer residues are the
terms on the left. A pole of w ↦ Z(−w) at a non-integer w = q, with w-residue R, then contributes, with the same orientation,

  **+p·R·W(q)·π cot(πq)·n^{−1−pq}**  (equivalently −p·Res_{s=−q}Z(s)·W(q)·π cot(πq)·n^{−1−pq})

to n^pb_n/c.
- **Correction.** The first version of this section stated the law with a minus sign, "calibrated once", while its table used
  the correct sign. Both reviewers found this (REVIEW_SPEC2_A F1, REVIEW_SPEC2_B F1). The sign is fixed by the integral itself,
  with three independent checks:
  - the cancellation of divergences at a resonance (§3.13);
  - the κ law (below);
  - the averaged-kernel representation of §3.13.
- **What was fitted.** What was identified from data is the kernel π cot(πw), from the m = 1 runs at p = 0.6 and 1.5 (§3.11(b))
  (Rule X). Those two rows are the identification point, not evidence.
- **Two identities.** W(1/p) = 1 for every p, directly from the definition of c(p): (4c)^{1/p} = π/(2I(p)), and C(2j, j)c(1/j)^j = 1
  is the case p = 1/j. And W(−1/p) = p·tan(π/p)/π, by the reflection formulas (REVIEW_SPEC2_A §4; checked to 10⁻³⁰).

**Test.** For λ_k = (k + γk^{−m})^p, Z(−w) = ζ(−pw) + pwγζ(m + 1 − pw) + O(γ²) has a pole at q = m/p with w-residue R = −mγ/p. The
prediction is a term −mγW(m/p)π cot(πm/p)·n^{−1−m} (m = 1: a shift of d₂). Measured (`checks/spec_pole.out`, regenerated with
hashed caches; s = 2, γ = ½; n(y − y_lat) after subtracting the exact first-order zeta layer). The predictions were committed
before the measures were generated (git: c554aa3 at 04:20, measures 04:21–04:27; REVIEW_SPEC2_B F10).

| p | m | W(m/p) | cot(πm/p) | predicted | fitted, n ≥ 200 / 400 / 800 | role |
|---|---|---|---|---|---|---|
| 0.6, 1.5 (§3.11(b)) | 1 | 1 | −0.5774 | +0.906900 per γ = ½ | +0.906900 | identification (Rule X), not evidence |
| 1.25 | 1 | 1 | −1.3764 | +2.162016 | +2.162016 / +2.162017 / +2.162022 | prediction |
| 1.8 | 1 | 1 | −0.1763 | +0.276974 | +0.276974 / +0.276974 / +0.276973 | prediction |
| 0.8 | 1 | 1 | +1 | −1.570796 | −1.570783 / −1.570792 / −1.570813 | prediction |
| 0.75 | 1 | 1 | +0.5774 | −0.906900 | −0.906866 / −0.906885 / −0.906954 | prediction |
| 1.5 | ½ | 0.9366 | +0.5774 | −0.424704 (new n^{−3/2} term) | −0.424703 / −0.424697 / −0.424630 | prediction, tests W |
| 1.25 | ½ | 0.9216 | +0.3249 | −0.235183 (new n^{−3/2} term) | −0.235177 / −0.235112 / −0.232695 | prediction, tests W |

The p = 0.8 row moved by ~10⁻⁵ against the first run: the regenerated script limits the subtracted zeta terms to jp < 2.5
(the fix that removed a spurious ζ(1) term at p = 0.75), and the regenerated output replaces a stale one (REVIEW_SPEC2_B F3). The latest windows (n ≥ 800) drift, most at m = ½, p = 1.25, where only 800 points remain.

Out-of-sample by reviewer B (fresh measures, own fits):
- p = 1.1, m = 1: +5.34969 ± 1.3·10⁻⁴ against +5.349641;
- p = 0.6, m = ½ (W = 0.841): +1.1453 ± 4·10⁻³ against +1.14367. The value without W (1.360) and the opposite sign are both excluded.
W ≠ 1 is tested only in the m = ½ rows and this case; at m = 1, W(1/p) = 1 identically. Honest precision (REVIEW_SPEC2_B F5):
±4·10⁻⁶ for p > 1, m = 1; 4–5·10⁻⁵ for p < 1; 4·10⁻⁵ to 3·10⁻⁴ for m = ½.

**The κ-shift law is a pole-law term, exactly** (REVIEW_SPEC2_A F3). For λ_k = k^p + κ, Z(−w) = ζ(−pw) + κwζ(p(1 − w)) + O(κ²) has a
pole at q = 1 − 1/p with w-residue R = −κq/p. The pole law gives

  p·R·W(q)·π cot(πq) = −2(2−p)cκ,  at n^{−1−pq} = n^{−p},

exactly for every p, using W(1 − 1/p) = 4c·W(−1/p)(p − 2)/(2(p − 1)) and W(−1/p) = p·tan(π/p)/π. This is §3.5's law. Reviewer A's
out-of-sample run at p = 1.5, κ = 1 gives L = −0.5662723 ± 1.3·10⁻⁶ against −0.5662723. The opposite sign would give +0.566.
So the κ deformation, which is outside S1, is inside S1″.

**Limitation: subleading pole terms** (REVIEW_SPEC2_A F2, MAJOR). The law gives the leading power n^{−1−pq} of each pole. The
same pole also contributes one order lower, at n^{−2−pq}, and cot(πq) = 0 does not remove that term. The datum:
- **Bessel zeros (p = s = 2).** Z_E(−1) = −(4μ² − 1)/16 for E = j²_{μ,k}, which is nonzero; reviewer A derived it from
  F = z^{−μ/2}I_μ(√z) and checked it numerically. S1′(II) would add 2pcZ_λ(−1) = −(4μ² − 1)/64 at n⁻³. Yet the exact Lommel
  formula is a pure index shift (§3.10); at μ = 0 its n⁻³ coefficient is 0, not 1/64.
- **Control.** A pure Hurwitz lattice with the same δ (p = s = 2, λ = (k − ¼)²) does carry the additive ε₁ = π²/256 to 10⁻⁷
  (reviewer A).
- **Reading.** The McMahon correction (m = 1, q = ½) has its leading term n^{−1−pq} = n⁻² killed by cot(π/2) = 0. Its subleading
  term at n⁻³ is not killed, and it cancels ε₁ exactly.
- **Consequences.**
  - S1′/S1″ hold only through orders below n^{−2−pq} for every pole q of Z − Z_lattice, half-integer q included.
  - The bouncer's ε₃ (at n⁻³, where its q = 3/2 pole has its subleading term) is NOT predicted exactly (§3.3 corrected).
  - Any future Robin ε₂ test at n^{−7/3} must include the subleading term of the q = ½ pole.
  - The "pure index shift" readings below hold at the leading power of each pole only.

**Consistency checks (not inputs; leading power of each pole only).**
- *Bouncer (p = 2/3).* The index corrections are odd powers 1/k^m (m = 1, 3, …); this can be made exact from the F′/F expansion
  (REVIEW_SPEC2_A F9). So q = 3m/2 is a half-integer, cot = 0, and the leading pole terms vanish. This is consistent with d₂ being
  the pure index-shift value (§3.10).
- *Bessel zeros (p = 2).* McMahon has odd powers only, so q = m/2 is a half-integer. Leading pole terms vanish. The exact all-orders
  index shift of the Lommel formula arises by cancellation of the subleading terms against the zeta layer (above), not by
  absence.
- *Robin.* hk^{−1/3} (q = ½) and h³k^{−1} (q = 3/2): reviewer B measured the n^{−4/3} coefficient as ≤ 3·10⁻⁶, where a
  non-vanishing kernel would give about 0.17h. This confirms cot(π/2) = 0 at leading power.
- *Resonance.* A pole meeting an integer gives n^{−1−jp}log n. Tested in §3.13 (weak test).

**Reading.** Conjecture S1″ (NUMERICAL; validity limited as above): the 1/n-order series of n^pb_n/c is the Mellin–Barnes integral
above, taken over the poles of Z − Z_lattice (the common Weyl pole excluded; §3.13), at the leading power of each pole.
- Its residues at integers are the zeta layer W(j)Z(−j).
- Its residues at the poles of Z are the index-correction and moved-Weyl data (κ), weighted by π cot(πq).
The Hurwitz shifts of §3.11(a), whose Z has no poles beyond the common Weyl pole, act through the exact index-shift rule. Its
terms linear in δ but one order lower (−(p+1)δd₁⁰ and −(1+2p)δε₁) are of the same subleading kind as the F2 terms, and are not
produced by this formula.

**Open.**
- A derivation of the π cot(πw) kernel from the RH analysis: done for the lattice's integer residues (§3.14, Theorem K); for
  the poles, derived from the soft-edge condition under Hypothesis G (§3.14). A full proof needs G.
- The subleading pole terms: a formula for the n^{−2−pq} coefficient. The Bessel family (exact) and the Hurwitz p = 2 control are
  the test data.
- Second-order (γ²) terms. For γ/k these are absent at d₂ (exactly linear; §3.11(b)).

### 3.13 Why π cot: one formula behind S2′, the zeta layer, the pole law and the in-band noise (HEURISTIC), plus two tests

**The formula (Conjecture S1‴, HEURISTIC; scope corrected per REVIEW_SPEC2_A F4, F5).** At leading order per node, the
1/n-order part of n^pb_n/c is the per-node law of S2′ summed over all nodes, taken as a Mellin pole part:

  (p/n)·Σ_m [(1 − u_m)^{−1/2}]_{av},   u_m := 4cλ_m/n^p,

where [·]_{av} is the average of the two boundary values for in-band nodes (u_m > 1, where (1 − u)^{−1/2} = ∓i|1 − u|^{−1/2}).
- **Definition of the sum** (F4). Literally, [(1 − u)^{−1/2}]_{av} = (1 − u)^{−1/2}1_{u<1}, and the truncated sum
  (p/n)Σ_{u_m<1}(1 − u_m)^{−1/2} equals the pole part below plus an O(n^{−1/2}) edge oscillation set by frac((n^p/4c)^{1/p})
  (reviewer A: (lit − pole)·√n ranges over −0.72 … +0.44 for the p = 0.6 lattice, n ∈ [100, 1602]). That oscillation is not in
  y_n for lattices. So S1‴ means **the sum of residues of the Mellin–Barnes integrand**, not a regularised value of the sum.
- **The Weyl pole is excluded** (F4). The common pole of Z at w = −1/p would contribute p·(−1/p)·W(−1/p)·π cot(−π/p) = +p, a
  constant that is not in y_n. Residues are taken of Z − Z_lattice. A *moved* Weyl pole (the κ deformation, §3.12) is included.
- **Mellin–Barnes form.** (1 − u)^{−1/2} = (1/2πi)∫Γ(−w)Γ(w + ½)/√π·(−u)^wdw, and Γ(w + ½)/(√πΓ(w + 1))·(4c)^w = W(w). So
  Σ_m(1 − u_m)^{−1/2} = (1/2πi)∫W(w)·Γ(−w)Γ(1 + w)(−1)^w·Z(−w)n^{−wp}dw.
- **Where π cot comes from.** The two continuations (−1)^w = e^{±iπw} correspond to the two boundary values. Their average turns
  Γ(−w)Γ(1 + w)(−1)^w = −π(−1)^w/sin πw into −π cot(πw). This is the kernel of §3.12.
- **Residues.** Integer residues give W(j)Z(−j) (the zeta layer, with W(0)Z(0) the Z(0) part of d₁). Residues at the poles of Z
  give the pole law, in particular the Weyl-scale index data with W(1/p) = 1.
- **Single nodes.** For one node outside the band this is S2′ (PROVED for one deleted atom).
- **In-band nodes.** For a node inside the band the averaged first-order contribution vanishes (the real part of ±i|·|^{−1/2}).
  This is why deep-band jitter was invisible (S4), and why in-band displacements act only nonlinearly, through the
  oscillating kernel of §3.6.
- **What is not covered** (F5). S1‴ is leading order *per node*, not first order in the perturbation. Terms one order in 1/n
  below each per-node contribution are not produced: the Hurwitz d₂ term −(p+1)δd₁⁰ and the f(δ) term −(1+2p)δε₁ (both linear in
  δ), the quadratic index-shift terms, and the subleading pole terms of §3.12 (F2). This parallels the O(1/n) remainder R of S2′.
None of this is proved. It organises every numerical result of §§2–3.12, and S2′ and E3 are its proved special cases.

**Test 1: the log resonance** (`checks/spec_resonance.out`; a **weak** test, REVIEW_SPEC2_A F6). When a pole of Z meets an integer j (q = m/p = j), the integer term
and the pole term each diverge, and their divergences cancel; the signs of §3.12 make them cancel. What remains in n(y − y_lat),
after the other zeta terms are removed, is

  p²jγW(j)·n^{−jp}log n + n^{−jp}·p[W(j)Z_fin − γW(j) − jγW′(j)],

where Z_fin is the full regularised ΔZ(−j), all orders in γ, with the divergent ζ(1) replaced by Euler's γ_E (its first-order
part is −0.166466; the γ^{≥2} part brings the bracket to the value below).
- **Derivation.** Both reviewers re-derived the formula, A as the double-pole residue of π cot(πw)W(w)ΔZ(−w)n^{−pw} at w = j
  (contour quadrature agrees to 10⁻²⁷), B as the ε → 0 limit of the two merging residues. The total finite part is independent
  of the regularisation family (the integrand is jointly analytic in (p, m)). Only the split between "Z_fin" and "−γW(j)" is
  a convention: the −γW(j) term can be read as coming from the prefactor m = p(j + ε) of the pole term, or as part of the
  w-Laurent finite part of ΔZ(−w).
- **Rule X.** The −γW(j) term was added *after* a mismatch with the fit; it is a derivation, not a fitted constant, and both
  reviewers confirm it. The pre-correction value +0.0232 is excluded by about 130 spreads. The log coefficient was predicted
  before the fit and is the a priori test.
At p = m = ½, γ = ½ (resonance at j = 1, a term n^{−3/2}log n in b_n), n ≥ 200:
- log coefficient: fit +0.10207 ± 1.4·10⁻⁴, predicted +0.102062;
- n^{−1/2} coefficient: fit −0.1809 ± 1.6·10⁻³, predicted −0.180893.
Agreement is at the 10⁻⁴ level, not 10⁻⁵. Later (higher-n) windows are less stable: at n ≥ 400 and n ≥ 800 the log coefficient
drifts to 0.1028 and 0.1080 and the constant to −0.190 and −0.249 (n^{−1/2}log n and n^{−1/2} are nearly degenerate on short
ranges). Hence "weak".

**Test 2: a real operator with a parameter, the Robin bouncer** ψ′(0) = hψ(0) on (0, ∞) with V = x (`checks/spec_robin.out`). The
eigenvalues are zeros of Ai′(−E) − hAi(−E), between the Neumann and Dirichlet ones; a vectorised bisection pins them to 10⁻¹⁶
relative. The exact zeta values, from F′/F with F = Ai′ − hAi, are

  Z_E(0) = 1/4,  Z_E(−1) = −h²/2,  Z_E(−2) = h(h + 1)(h² − h + 1)/2 = h(h³ + 1)/2,  Z_E(−3) = −(32h⁶ + 48h³ + 21)/64.

These are finite values, not finite parts: the coefficient of the would-be ζ(1) term vanishes (reviewer B, j = 0, 1, 2; B also
confirmed Z_E(−1) and Z_E(−2) from the eigenvalues, independently of the Hadamard and Mellin steps, which remain NOT QUOTED).

At h = 0 these reduce to the Neumann values (Z_E(−3) = −21/64). S1′ then predicts:
- d₁ = −pα/2 + p/4, independent of h;
- ε₁ = 2pcZ_{λ′}(−1) ∝ −h²;
- d₂ = the index-shift value with δ = −¾. Every Robin index correction (hk^{−1/3}: q = ½; h³k^{−1}: q = 3/2) and the Neumann WKB
  term (q = 3/2) sit at half-integers, where cot = 0.

| h | ε₁ predicted (= 2pcZ_{λ′}(−1)) | ε₁ fitted (spread) | d₁ fitted (pred 0) | d₂ fitted − index shift (spread) |
|---|---|---|---|---|
| ½ | −0.0262484 | −0.0262417 (8·10⁻⁴) | 2·10⁻⁸ | 6·10⁻⁵ (8·10⁻³) |
| 1 | −0.1049934 | −0.1049772 (1.7·10⁻³) | 9·10⁻⁸ | 1.2·10⁻⁴ (1.6·10⁻²) |
| 2 | −0.4199737 | −0.4198287 (3.3·10⁻³) | 1·10⁻⁶ | 5·10⁻⁵ (3.2·10⁻²) |

ε₁ scales as h² (ratios 1 : 4 : 16) with the predicted constant. So b_n reads off the Robin parameter through Z(−1) = −h²/2, and
the boundary condition's type (μ) through Z(0). (`checks/spec_robin.out`; s = 2, n ≤ 1600.) The Robin closed forms were
committed (3f13e62, 04:48) before the h = ½ and h = 2 runs (04:50).
- **Direct test of cot(π/2) = 0** (reviewer B, F7). With n^{−4/3} added to the fit pool (the exponent of the leading q = ½ pole
  term), its coefficient is ≤ 3·10⁻⁶, against about 0.17h if the kernel did not vanish there.
- **Caution for ε₂.** A future test of the Robin ε₂ at n^{−1−2p} = n^{−7/3} must include the subleading term of the q = ½ pole,
  which sits at n^{−2−pq} = n^{−7/3} as well (§3.12, Limitation).

### 3.14 Where the π cot kernel comes from (Theorem K: PROVED-mod-cite; Lemma K0: PROVED; Lemma Q: PROVED-mod-cite with NUMERICAL inequalities; Principle E: CONJECTURE; NOT REVIEWED)

Two mechanisms produce the same kernel:
- **The band factor (E3's lattice proof).** The whole 1/n-order zeta layer is one linear functional of the band factor.
  Theorem K writes it exactly as a Mellin–Barnes integral whose kernel contains −π cot(πw). Its residues at the integers are
  E3's ε_j.
- **The leading-order equilibrium.** The constant c(p) of Law P is fixed by a soft-edge condition that is literally a sum of
  the per-node law (1 − u)^{−1/2} over the saturated (out-of-band) nodes (Lemma Q). The Mellin transform of that *truncated* law
  is −π cot(πw)·W(w)(4c)^{−w} (Lemma K0). Perturbing the node set moves the edge, and the poles of Z enter with π cot(πq).
So the kernel of §3.12 is derived, not fitted. What is still missing for a proof of S1″ is stated as Hypothesis G below.

**Lemma K0 (PROVED).** Let L(u) := (1 − u)^{−1/2}1_{u<1}. For Re w < 0,

  L̃(w) := ∫_0^∞u^{−w−1}L(u)du = B(−w, ½) = −π cot(πw)·Γ(w + ½)/(√πΓ(w + 1)),

continued meromorphically to ℂ, with simple poles at w = 0, 1, 2, … where −Res L̃ = C(2j, j)4^{−j} (the Taylor coefficients of
L at 0). At a = 4c, (a/n^p)^w·Γ(w + ½)/(√πΓ(w + 1)) = W(w)n^{−pw}.

*Proof.* B(−w, ½) = Γ(−w)√π/Γ(½ − w). By the reflection formulas Γ(½ − w)Γ(½ + w) = π/cos πw and Γ(−w)Γ(1 + w) = −π/sin πw,
√πΓ(−w)/Γ(½ − w) = Γ(−w)Γ(w + ½)cos(πw)/√π = −π cot(πw)Γ(w + ½)/(√πΓ(w + 1)). ∎ (Checked: `checks/spec_kernel.out` (K0).)

The two analytic continuations of (1 − u)^{−1/2} into u > 1, ∓i|1 − u|^{−1/2}, have Mellin transforms with Γ(−w)Γ(1 + w)e^{±iπw}.
Their average is the truncated L, so K0 is §3.13's "averaging" made exact.

**Theorem K (p > 1, s > 1; PROVED-mod-cite: E3 Lemmas F.1′, E3.7; DLMF 5.9.1, 25.2.1, 25.4.1 as quoted in RH/CITATIONS.md; the
Mellin–Barnes integral for (1 + x)^{−3/2}, standard, NOT QUOTED).** Let 𝔢 = 𝔢_n be the jump density of Lemma F.1′ and

  e_n := (cp/π)∫_0^∞𝔢(−r)·r^{−1/2}(r + 4c)^{−3/2}dr.

(i) e_n = cp·Σ_kμ_{n,k}Q_k(4c) term by term: e_n is Lemma E3.7's functional evaluated on the full band factor rather than on its
  truncation P_n.
(ii) For 0 < c₀ < 1,

  e_n = (1/2πi)∫_{(c₀)} pW(w)ζ(−wp)n^{−wp}·π[cot(πwp/2) − cot(πw)] dw.

(iii) For every J ≥ 1, e_n = Σ_{j≤J} pW(j)ζ(−jp)n^{−jp} + O(n^{−(J+1)p}); the terms are E3's ε_j.

*Proof.*
- **(i).** Σ_kQ_k(4c)y^{−k−1} = y^{−2}(1 − 4c/y)^{−1/2}(1 − 4c/y)^{−1} for |y| > 4c (product of the generating functions of
  C(2j, j)c^j and (4c)^l). At y = −r this is r^{−1/2}(r + 4c)^{−3/2}. Insert m_k = (1/2π)∫𝔢y^{−k−1}dy (Lemma F.1′(i)); the
  interchange is justified because 𝔢 is exponentially small for |y| ≤ 2R₁ (E_pgt1 Lemma E.2(c)).
- **Mellin transform of 𝔢.** As in Lemma F.1′(i), with k replaced by complex w (the Fubini bound is the same with Re w):
  I(w) := ∫_0^∞𝔢(−r)r^{−w−1}dr = −2pΓ(wp)ζ(1 + wp)(2πn)^{−wp}sin(πw − πwp/2) for Re w > 0. The strip is set by 𝔢(−r) → π(1 − 2/p)
  as r → ∞ (t₊ → 0) and by its exponential decay as r → 0. By DLMF 25.4.1, I(w) = (2π/w)ζ(−wp)n^{−wp}[sin πw·cot(πwp/2) − cos πw].
- **(ii).** r^{−1/2}(r + 4c)^{−3/2} = (1/2πi)∫Γ(−s)Γ(3/2 + s)/Γ(3/2)·(4c)^sr^{−2−s}ds, with −3/2 < Re s < 0. Put w = s + 1 and
  exchange the integrals (absolute convergence on Re w = c₀ ∈ (0, 1)). Then Γ(1 − w)/w = π/(sin(πw)Γ(1 + w)) collects the
  factors into pW(w)·(π/sin πw)·(w/2π)n^{pw}I(w), which is the stated integrand.
- **(iii).** On vertical lines |cot(πwp/2) − cot(πw)| ≤ Ce^{−min(p, 2)π|Im w|}, while ζ(−wp) and W grow at most polynomially. So
  the contour moves right. The poles are those of −π cot(πw) at w = j, each giving −Res = pW(j)ζ(−jp)n^{−jp}. The poles of
  cot(πwp/2) at w = 2l/p (l ≥ 1) sit on the trivial zeros ζ(−2l) = 0 and are removable; where 2l/p = j is also an integer, the
  product is regular and the j-th term is 0. ∎
- **Check** (`checks/spec_kernel.out` (K)): quadrature of e_n against the Mellin–Barnes integral agrees to all 16 printed
  digits at (p, n) = (1.5, 10), (1.25, 20), (3, 10), and the residue sums converge to it (5 terms: 10⁻⁸ relative or better).

*What Theorem K adds to E3.* E3 controls e only through its truncated polynomial expansion. Theorem K gives the exact functional
and shows that S1‴ holds for the lattice, in the sense that S1‴ asserts:
- the kernel −π cot(πw) comes out of the RH functional itself;
- the Weyl pole w = −1/p lies to the left of the strip Re w > 0, so the exclusion REVIEW_SPEC2_A F4(i) asked for is automatic,
  as is w = 0 (the Z(0) term enters d₁ through the index normalisation, not through e_n);
- the second kernel π cot(πwp/2) contributes nothing. Its apparent poles are removable: they come from rewriting with
  ζ(−wp), and the original integrand has none (see the Structural reading);
- e_n is a smooth function of n with an asymptotic expansion in powers only. The n^{−1/2} edge oscillation of the literal
  truncated sum (F4(ii)) is an artefact of truncating at u = 1.
The lattice proof uses p > 1 (𝔢 on the negative axis). For p < 1 the seam version of Lemma F.1 has the same Fourier sum
(§3.1), and the same representation is expected but not written out.

**Proposition 3.14.4 (the band factor does not carry the pole term; computation PROVED, conclusion HEURISTIC).** Perturb the
lattice to λ_k = (k + γk^{−m})^p, keeping the interpolating phase of Lemma F.1′ but with t(z) = κ(n^p/z), κ the inverse of
k ↦ λ_k. To first order, δt₊ = −γn^{−m}(re^{iπ})^{m/p}, and δ𝔢 = 2Im[F′(t₊)δt₊] with F′(t) = 2πi/(e^{2πit} − 1). Then

  ∫_0^∞δ𝔢(−r)r^{−w−1}dr = −2πγp·n^{−pw}ζ(1 + m − pw)[cos πw + sin πw·tan(π(pw − m)/2)],  Re w > (m + 1)/p

(same Fubini/DLMF 5.9.1 argument, with Σ_{m′}m′^{m−pw} = ζ(pw − m) and the functional equation; checked to 10⁻¹³ at
w = 2.3, 3.1, `spec_kernel.out` (P)). With δZ(−w) = pwγζ(1 + m − pw), the contribution to e is

  (1/2πi)∫ pW(w)δZ(−w)n^{−pw}·π[−cot(πw) − tan(π(pw − m)/2)] dw,

taken on a line Re w > (m + 1)/p.
- **The integers** give pW(j)δZ(−j)n^{−pj}, the zeta layer of the perturbed set, exactly as for the lattice.
- **The pole at q = m/p lies to the left of the strip.** Equivalently: δ𝔢 = γΦ(r/n^p) is O(γ) only at r ~ n^p (t ~ 1), so for
  any admissible interpolant (bounded for t < 1) its contribution to e_n is O(n^{−p}). A term n^{−pq} = n^{−m} with m < p (all
  the m = 1, p > 1 rows of §3.12) cannot come from the band factor.
- **The Jacobian tilt.** The band weight changes by log|t′| → γmn^{−1−m}z^{(m+1)/p}, a branched tilt at the hard edge. By the
  Beta integral (1/π)∫_0^1(1 − v^q)(1 − v)^{−3/2}v^{−1/2}dv = 2Γ(q + ½)/(√πΓ(q)) (`spec_kernel.out` (B)), E3.7's functional maps
  a tilt +Az^q to −A·pqW(q)/2 (if E3.7 extends to branched tilts, which is not shown; the sign follows E3.4, where the tilt
  enters as −P). Both this and the tan pole at w = (m + 1)/p sit at n^{−2−m}, the order of the subleading pole terms of §3.12
  (F2). The Jacobian term is confirmed numerically in §3.15; the tan pole is not needed for q₁ ≤ 1.

**Lemma Q (the soft-edge condition; PROVED-mod-cite: balayage onto an interval, standard; the constrained-equilibrium
characterisation (Rakhmanov 1996, Dragnev–Saff 1997), NOT READ under Rule C; the variational inequalities NUMERICAL).**
Rescale the lattice nodes to z_k = (n/k)^p, so the normalised node density is σ(y) = (1/p)y^{−1/p−1} on (0, ∞). The
equilibrium measure of unit mass with upper constraint σ and no external field (the weights k^{−s} are subexponential) is
μ = ν|_{[0,a]} + σ|_{[a,∞)}, where

  ν(x) = [1 − ∫_a^∞σ(y)√(y(y − a))/(y − x)dy]/(π√(x(a − x))),

and the edge a is fixed by the soft-edge (continuity) condition

  ∫_a^∞σ(y)(1 − a/y)^{−1/2}dy = 1.     (Q)

For this σ, (Q) reads a^{−1/p}(1/p)B(1/p, ½) = 1, i.e. a^{1/p} = √πΓ(1/p + 1)/Γ(1/p + ½) = π/(2I(p)), i.e. **a = 4c(p)**. This is an
independent derivation of the constant of Law P.
- **Equilibrium on the band.** ν is (arcsine, mass 1) minus the balayage of σ|_{[a,∞)} onto [0, a], so U^μ is constant there.
- **Positivity.** √(y(y − a))/(y − x) < √(y/(y − a)) for x < a, so the bracket is positive on [0, a) and vanishes at x = a
  exactly under (Q).
- **Upper constraint and outer inequality (NUMERICAL, `spec_kernel.out` (Q), p = 0.6 and 1.5).** ν ≤ σ on the band, U^μ is
  constant there to 10⁻¹¹, and U^μ − ℓ < 0 on the saturated region; a = 4c to 10⁻¹².

In node language, (Q) is (1/n)Σ_{u_k<1}(1 − u_k)^{−1/2} ≈ 1 with u_k = 4cλ_k/n^p. The per-node law of S2′ is the derivative of this
condition: deleting one saturated node lowers the sum by (1 − u₀)^{−1/2}, and the edge must move to compensate (see Principle E).

**Proposition E (Mellin algebra; PROVED as an identity of asymptotic series).** Let Λ be regular (λ_k ~ k^p, so w ↦ Z(−w) has
the Weyl pole at w = −1/p with residue −1/p). Suppose its other poles are at points q with residues R_q, and Z(−j) is finite
for integers j ≥ 0. Define F_n(a) as the Mellin pole part of Σ_kL(aλ_k/n^p), i.e. (1/2πi)∫L̃(w)Z(−w)(a/n^p)^wdw with all poles
to the right. Then, by Lemma K0,

  F_n(a) = n(a/4c)^{−1/p} + Σ_{j≥0}C(2j, j)4^{−j}Z(−j)(a/n^p)^j + Σ_q R_qπcot(πq)Γ(q + ½)/(√πΓ(q + 1))·(a/n^p)^q,

and the solution of F_n(4c(1 + η)) = n is, to first order,

  η = (p/n)[Z(0) + Σ_{j≥1}W(j)Z(−j)n^{−jp} + Σ_q R_qW(q)π cot(πq)n^{−pq}] + O(nη²).

The four parts of S1 are exactly these terms:
- **j = 0.** pZ(0)/n is the Z(0) part of d₁ (S1).
- **j ≥ 1.** ε_j = pW(j)Z(−j) (S1′(II)).
- **The poles.** They give the pole law of §3.12, +pR_qW(q)π cot(πq)n^{−1−pq}, with the sign that the data require. This
  includes the κ pole (the moved Weyl pole) and the log resonance (a pole meeting an integer).
- **The Weyl pole.** It is the leading term n itself, not a correction, which explains its exclusion.

**Principle E (CONJECTURE; NUMERICAL support = all of §§2–3.13).** For a regular node set, the 1/n-order layer of n^pb_n/c, at
leading order per node, is η of Proposition E. Equivalently, the band edge is fixed by the discrete soft-edge condition
Σ_{u_k<1}(1 − u_k)^{−1/2} = n (Mellin pole part).
- **Proved instances.**
  - The lattice: its integer residues are E3's ε_j (Theorem K), and Lemma Q gives the leading order.
  - One deleted saturated atom: Principle E gives Δ(ny_n) = −p(1 − u₀)^{−1/2}, which is Theorem S2′ (§3.2, PROVED by an
    independent route via Uvarov). This consistency was not used in formulating E.
- **Not covered.**
  - The integer layer beyond Z(0) (the quadratic and one-order-lower index-shift terms; F5).
  - The −pα/2 part of d₁ (the weights).
  - The subleading pole terms (F2). Proposition 3.14.4 identifies candidates for these.

**Hypothesis G (what a proof of S1″ needs).** For λ_k = Λ(k) with Λ(t) = t^p(1 + O(t^{−1−m})), the RH analysis of Paper 2/E2/E3
goes through with:
- (G1) the g-function of the constrained equilibrium of the n-dependent continuum node density;
- (G2) the band factor given by the Cauchy integral of 𝔢_κ;
- (G3) parametrix corrections whose first-order dependence on the perturbation is O(n^{−2−m}).
Under G, the first-order change of n^pb_n/c at order n^{−1−m} is the edge shift of (Q) for the perturbed continuum density
(1/n)|dt_κ/dz|. Its Mellin-regularised value is, by Lemma K0 at w = q, pR_qW(q)π cot(πq)n^{−1−pq}. The integer residues come
from G2 (Proposition 3.14.4). Proving G is the plan-sized task: Paper 2 for non-lattice nodes. The pole law S1″ therefore
remains CONJECTURE (NUMERICAL), now with a derivation from Hypothesis G (HEURISTIC) and with its kernel no longer an input.

**Structural reading.**
- The poles of Z come from the smooth (continuum) node density and enter through the equilibrium (g-function). Their kernel is
  the Mellin transform of the truncated law: π cot(πq).
- The zeta values Z(−j) come from discreteness and enter through the band factor. Their kernel is the integer residues of
  −π cot(πw).
- Both are one Mellin–Barnes integral because both are the same soft-edge sum, read at its poles.
- *Correction (same day):* the second lattice kernel π cot(πwp/2) is an artefact of writing I(w) with ζ(−wp). In the original
  form −2pΓ(wp)ζ(1 + wp)(2πn)^{−wp}sin(πw − πwp/2) there are no poles at w = 2l/p at all. The same holds for Hurwitz lattices,
  where the Fourier sum Σ_m sin(πw − πwp/2 + 2πmδ)/m^{1+wp} is entire in w for δ ∉ ℤ. So the band factor of a Hurwitz lattice
  produces only the ζ(−jp, a) residues. The integer layer (the index shift) must come from the outer scalar j_δ (its
  Bernoulli-polynomial coefficients, §3.1) and from the normalisation, not from a hidden kernel. A speculation to the
  contrary, written earlier the same day, is withdrawn.

**Rule A.**
- *Is Theorem K just E3 re-summed?* Its expansion is E3's series (asymptotic only, since ζ(−jp) grows factorially). The
  content is the exact functional, its strip, and the two kernels.
- *Is Lemma Q circular with S2′?* No. (Q) comes from potential theory alone, and S2′ was proved from Uvarov's identity. Their
  agreement is a check.
- *Fitted inputs?* None. The kernel identification of §3.12 (Rule X) now has a derivation. The pole-law predictions predate it.
- *Why was the band factor not enough?* Proposition 3.14.4 shows that its pole contribution lies on the wrong side of the
  strip, at scale n^{−p}. Searching for the pole term there would have failed.

**Open.**
- Hypothesis G (the proof of S1″).
- The p < 1 version of Theorem K.
- The integer layer from the outer scalar j_δ (§3.1) for Hurwitz lattices.
- The subleading pole terms from the Jacobian tilt and the tan pole. This needs E3.7 for branched tilts, i.e. a hard-edge
  computation.

### 3.15 The subleading pole term (NUMERICAL; Conjecture S1⁗; NOT REVIEWED)

**Question** (REVIEW_SPEC2_A F2, §3.12 Limitation). The pole law gives the leading power n^{−1−pq} of each pole q of Z. The same
pole also contributes at n^{−2−pq}, where cot(πq) = 0 does not kill it. What is that coefficient?

**Method** (`checks/spec_subpole.py`, `checks/spec_subpole.out`).
- Lattices λ_k = (k + γ/k^m)^p with γ ∈ {±¼, ±½}.
- With D(γ) := n(y_γ − y_lat), antisymmetrise in γ and Richardson-extrapolate over γ = ¼, ½. This isolates the part linear in
  γ; the γ² and γ³ terms are removed exactly.
- Subtract the leading pole term and the first-order zeta layer pW(j)·pjγζ(1 + m − pj)n^{−jp}.
- Fit the n^{−1−m} coefficient S of what is left (n^{−2−m} in n^pb_n/c), over windows n ≥ 200, 400 and 4–6 nuisance exponents.

**Conjecture S1⁗ (NUMERICAL; precise for q₁ := (m + 1)/p ≤ 1, consistent at ~10⁻³ for q₁ > 1).** Per unit γ,

  S = −(mpq₁/2)·W(q₁) + L·(1 + m + p)·d₁⁰/p,   L := −mW(q)π cot(πq) (the leading pole coefficient), d₁⁰ = −(s − 1)/2.

The two terms have separate origins:
- **The Jacobian tilt.** The perturbed index function changes the node density on the band by log|t′| → γmn^{−1−m}z^{q₁}, a
  tilt branched at the hard edge z = 0. Lemma E3.7's functional, with the Beta integral of Proposition 3.14.4, maps a tilt
  +Az^{q₁} to −A·pq₁W(q₁)/2. (The tilt enters E3.4 as −P, which fixes the sign; Proposition 3.14.4's "(2q/4c)W(q)" is the
  modulus.) This term is confirmed exactly at p = 2, m = 1, where L = 0: S = −W(1) = −π²/8 to 10⁻⁶. So E3.7 extends to this
  branched tilt, numerically.
- **The shifted pole.** The leading pole term behaves as if evaluated at the shifted index n + δ_eff, multiplied by
  (n/(n + δ_eff))^p, with δ_eff := −d₁⁰/p = (s − 1)/(2p). That is the index shift which turns the lattice's own 1/n coefficient d₁⁰
  into a pure shift: rule H of §3.11(a), applied to the pole term. Its coefficient is −(1 + m + p)δ_eff·L. The s-dependence
  confirms this: at p = 1.8, S(s = 3) − S(s = 2) = −0.58464 against −(1 + m + p)L/(2p) = −0.58472.

| p | s | m | q₁ | S (fit, half-range) | prediction | S − pred |
|---|---|---|---|---|---|---|
| 2 | 2 | 1 | 1 | −1.233702 (1·10⁻⁶) | −1.233701 | −1·10⁻⁶ |
| 2.2 | 2 | 1 | 0.909 | −0.777016 (7·10⁻⁵) | −0.776976 | −4·10⁻⁵ |
| 2.5 | 2 | 1 | 0.8 | −0.258693 (2·10⁻⁵) | −0.258696 | +3·10⁻⁶ |
| 3 | 2 | 1 | 0.667 | +0.371552 (1·10⁻⁶) | +0.371551 | +2·10⁻⁶ |
| 4 | 2 | 1 | 0.5 | +1.261975 (4·10⁻⁷) | +1.261975 | +3·10⁻⁹ |
| 3 | 2 | 2 | 1 | −8.270517 (3·10⁻⁵) | −8.270552 | +4·10⁻⁵ |
| 1.8 | 2 | 1 | 1.111 | −1.847995 (3·10⁻⁴) | −1.849477 | +1.5·10⁻³ |
| 1.8 | 3 | 1 | 1.111 | −2.432630 (3·10⁻⁴) | −2.434200 | +1.6·10⁻³ |
| 1.5 | 2 | 1 | 1.333 | −3.39874 (1.4·10⁻²) | −3.44204 | +4.3·10⁻² |
| 1.25 | 2 | 1 | 1.6 | −6.54 (0.26) | −7.02 | +0.48 |
| 2.5 | 2 | 2 | 1.2 | −15.706 (1.8·10⁻²) | −15.649 | −5.7·10⁻² |

**Reading.**
- For q₁ ≤ 1 the formula holds to the fit precision in six cases (p = 2, 2.2, 2.5, 3, 4; m = 1, 2; all at s = 2). The
  s-dependence has so far been tested only at p = 1.8 (q₁ > 1), where the s = 3 − s = 2 difference matches the shift term to
  10⁻⁴.
- For q₁ > 1 the small-pool fits left a residual of 0.3% (p = 1.8) to 7% (p = 1.25) of S. *Resolved (same day): fit
  systematics.* Refitting the cached data with broad pools (20 fits: windows n ≥ 150–600 and 3–7 nuisance exponents i + jp + lm)
  gives the following medians minus prediction:
  - p = 1.5: −2·10⁻³ (it was +4·10⁻²; the prediction lies inside the interquartile range);
  - p = 1.8: +3·10⁻³ (the prediction is at the edge of the interquartile range);
  - p = 2.5, m = 2: −9·10⁻² (an unstable pool);
  - p = 3 and p = 2.2, for comparison: 2·10⁻⁶ and 6·10⁻⁴.
  The sign of the "residual" depends on the pool, so it is not a third mechanism. S1⁗ is consistent with every case tested.
  Its precision degrades from 10⁻⁶ (q₁ ≤ 1, clean exponents) to about 10⁻³ (q₁ > 1, crowded exponents near p = 1).
- **p = 2.** The synthetic family's first-order n⁻³ coefficient (zeta layer plus subleading) is −3.70γ ≠ 0. A decaying index
  correction is therefore visible at n⁻³ at p = 2 in general. The exact index shift of the Bessel-zero family (§3.10) is a
  special cancellation: there the correction γ ∝ (4μ² − 1) is tied to the index offset δ = μ/2 − ¼.
- **The integer layer, in hindsight.** Both mechanisms are integer-layer-type: a smooth density tilt, and an index shift
  by δ_eff. §3.13 called these "one order in 1/n below each per-node contribution" (F5), and Principle E does not produce
  them. Rule H and S1⁗ are the same statement for two different spectral terms. This suggests a single rule for the
  second-order structure: every first-order term of the 1/n layer is evaluated at n + δ_eff, plus the density tilt.

**Rule X / Rule A.**
- The two terms were identified from the data in this order:
  1. the Jacobian candidate, written in advance with the wrong sign;
  2. its sign fixed by redoing E3.4's convention, after the p = 2 value came in;
  3. the shift term guessed from the X ratios at p = 2.5 and 3 (5/6, 9/10);
  4. then tested on the s = 3 run, p = 4, p = 2.2 and m = 2, which were run or predicted after the guess.
  So p = 2, 2.5, 3 (m = 1, s = 2) are the identification set. The s = 3, p = 4, p = 2.2 and m = 2 rows are the tests: four
  rows, two of them inside q₁ ≤ 1 at precision.
- Nothing is fitted: both terms are closed forms in p, s, m.

**Open.**
- ~~The q₁ > 1 residual~~ (fit systematics; see Reading).
- A derivation of δ_eff from the outer scalar (the same open step as for rule H).
- E3.7 for branched tilts, proved rather than observed.
- The analogous subleading term for the κ pole and for half-integer poles (bouncer ε₃, Robin ε₂). The bouncer's n⁻³
  coefficient can now be predicted. It needs the bouncer's actual index correction and its Jacobian; a script to do this
  is open.

### 3.16 Hearing a drum's perimeter and corners in b_n (NUMERICAL; p = 1, outside the proved framework; NOT REVIEWED)

**Setting** (`checks/spec_corners.py`, `checks/spec_corners.out`). Dirichlet eigenvalues of planar drums are rescaled to unit
Weyl density, λ̃ = Aλ/4π, so that N(λ̃) = λ̃ − β√λ̃ + c₀ + (fluctuations). Here β = L/√(4πA) carries the perimeter and
c₀ = Z(0) the corners and curvature: 1/4 for any rectangle, 1/3 for the equilateral triangle, 1/6 for a smooth simply connected
domain. The measure is Σ λ̃^{−2}δ_{1/λ̃} (p = 1, s = 2). A "smoothed drum" is the regular node set N_s(λ_k) = k − ½ − c₀ with the
same β and c₀ and no counting fluctuations. Write D := n(y − y_lattice).

**Perimeter (a test of the pole law with W·cot = 0·∞).** The perimeter term is a pole of Z(−w) at q = −½ with residue β/2. The
pole law gives pR·W(q)π cot(πq)·n^{−1−pq}. Here cot(πq) = 0, but W(q) ∝ Γ(q + ½) has a pole at the same point, and the product
tends to −π(4c)^{−1/2} = −π/√2. So the prediction is

  D ⊃ −(π/(2√2))·β·n^{+1/2}.

| smoothed drum | β | fitted n^{1/2} coefficient (half-range) | −πβ/(2√2) |
|---|---|---|---|
| square perimeter | 1.128379 | −1.253317 (1·10⁻⁵) | −1.253314 |
| triangle | 1.286074 | −1.428473 (1·10⁻⁵) | −1.428469 |
| disk | 1 | −1.110722 (7·10⁻⁶) | −1.110721 |
| golden rectangle | 1.161199 | −1.289770 (1·10⁻⁵) | −1.289767 |

*Rule X.* Before the run I predicted "no n^{1/2} term (cot = 0)", forgetting W's pole. The formula itself, evaluated correctly,
was never adjusted: the value above is its 0·∞ limit, computed after seeing the data but with no free parameter.

**Corners.**
- **Isolated at fixed β** (square perimeter with c₀ = 1/4 against c₀ = 1/3). The n⁰ coefficient of the difference is 0.08335,
  stable to 2·10⁻⁵ over six fits, against Δc₀ = 1/12 = 0.08333. So b_n hears the corner term exactly, as S1's pZ(0) says,
  at p = 1.
- **Absolute n⁰ coefficient.** It is c₀ + ½ + (π²/16)β² in all five smoothed drums (0.617β² against π²/16 = 0.6169; the
  medians agree to 2·10⁻⁴, although single fits are unstable). The β² part is second order in the perimeter, outside
  Principle E as stated.
- **The β² term is derived (same day) from Lemma Q's continuum soft-edge condition, to all orders in β.** With
  dN = (1 − β/(2√λ))dλ and c = ½:
  - the condition ∫_0^{1/a}(1 − aλ)^{−1/2}dN = n reads 2/a − (πβ/2)a^{−1/2} = n;
  - with a = 2(1 + η)/n and v := (1 + η)^{−1/2}, this is v² − εv − 1 = 0, where ε := πβ/(2√(2n));
  - so 1 + η = 1/v² = 1 − ε + ε²/2 + O(ε³), and D = nη ⊃ −(πβ/(2√2))√n + (π²/16)β².
  The leading term is the pole-law value above, and the second is the fitted β² coefficient. So the continuum equilibrium,
  solved exactly rather than linearised, carries every smooth-density term (all orders in the perimeter). Principle E's first
  order is its linearisation. The discreteness terms (Z(0) and the Z(−j)) are what remains for the band factor.

**Actual drums.**
- **Generic (golden rectangle, simple spectrum).** D − D_smoothed has mean ≈ 0 (+0.3, +0.5, −0.2, +1.0 over the four
  octaves) but a standard deviation of 11 → 38 that grows like n^{0.55}. These are the counting fluctuations of an
  integrable billiard (S4, Poisson-like). The perimeter term (≈ −1.29√n) is above this noise, just. The corner term
  (≈ 0.08) is not resolvable from one spectrum at n ≤ 1600.
- **Degenerate spectra (square, triangle).** b_n sees *distinct* eigenvalues only, since multiplicities merge into masses.
  The square's distinct eigenvalues are the sums of two squares, with density ~ K·Q/√(log Q), where K = 0.7642 is the
  Landau–Ramanujan constant. The leading law then gives nb_n/c ≈ (4K/π)/√(log Q_edge): 0.438 against 0.443 at n = 100, and
  0.364 against 0.374 at n = 1000. A Jacobi matrix of a square drum hears the arithmetic of sums of two squares; this is
  heuristic at the leading-order level.

**Reading.** At p = 1, where nothing is proved, b_n reads the drum's heat-trace data in the order the kernel predicts:
- area as the leading law;
- perimeter at n^{−1/2}, through the 0·∞ limit of W·π cot;
- corners and curvature at n^{−1}, through Z(0).
For integrable drums this information sits below the Poisson counting noise, except the perimeter. For chaotic drums, with
GOE-like rigidity, S4 predicts noise smaller by a factor ~3–4; that is untested.

### 3.17 The quartic oscillator: the pole law with cot ≠ 0 on a real operator (NUMERICAL; NOT REVIEWED)

**Why it matters.** In every real operator tested before (bouncer, Bessel zeros, Robin), the poles of Z sit at half-integers,
where cot = 0. So the π cot kernel had been tested at a nonzero value only on synthetic lattices (§3.12, §3.15). The quartic
oscillator H = −d²/dq² + q⁴ (p = 4/3) is the first real operator where it is.

**Spectrum** (`checks/spec_quartic.py`, `checks/spec_quartic.out`).
- **Exact part.** E_K for K ≤ 1200 come from a harmonic-oscillator basis (frequency E_max^{1/4}, banded, sizes 4000 and 5000).
  They are converged to 3·10⁻¹⁶ relative, with E₁ = 1.0603620905.
- **WKB fit.** On 200 < K ≤ 900, K − ½ = A·E^{3/4} + B·E^{−3/4} + C·E^{−9/4}, with A = (1/π)∫_{−1}^1√(1 − t⁴)dt exact. The fit gives
  B = −0.0476724854, which equals **−1/(12πA)** = −0.04767248522 to 4·10⁻¹⁰.
- **Tail.** Beyond K = 1000 the series is used, solved by Newton.

**Nodes.** λ_K := A^{4/3}E_K satisfy λ^{3/4} = k′ + γ/k′ + O(k′^{−3}), with k′ = K − ½. This is a Hurwitz lattice with δ = −½ plus an
m = 1 index correction γ = −AB = 1/(12π). Its pole is at q = m/p = 3/4, where W(3/4) = W(1/p) = 1 and **cot(3π/4) = −1**.

**Predictions** (s = 2; no fitted constant):
- **d₁** = −(s − 1)/2 − pδ = +1/6. Equivalently, Z(0) = ζ(0, ½) = 0, which agrees with Voros (Z(0) = 0 for the quartic).
- **ε₁ = 0.** The heat-trace exponents of q⁴ are −3/4, 3/4, 9/4, … and none is an integer, so Z(−1) = 0.
- **d₂** = [Hurwitz shift, δ = −½] + pole term = 0.192708 + πγ = 0.192708 + **1/12** = 0.276042. The pole term is
  −mγW(q)π cot(πq) = +πγ.

| coefficient | fit (spread) | prediction | without pole term | sign flipped |
|---|---|---|---|---|
| d₁ | +0.16666667 (8·10⁻⁹) | +1/6 | — | — |
| ε₁ (n^{−7/3}) | +0.00001 (3·10⁻³) | 0 | — | — |
| d₂ | +0.276010 (1·10⁻⁵) | +0.276042 | +0.192708 | +0.109375 |

The pole term is confirmed on a real operator, with cot ≠ 0, to 3·10⁻⁵ against a size of 0.083. The alternatives are excluded
by about 8000 spreads. The d₂ test is a prediction. The γ bug in the first run (−A²B instead of −AB) changed the prediction, not
the measure. The corrected value follows from λ^{3/4} = A·E^{3/4} alone and was not tuned.

**A closed form for all homogeneous potentials** (`checks/spec_homog.py`, `checks/spec_homog.out`; NUMERICAL). For V = q^N
(N even), the same construction gives a Hurwitz lattice (δ = −½) plus γ/k′ with γ = −AB, and pole q = 1/p with p = 2N/(N + 2),
W = 1. The pole contribution to d₂ is A·B·π cot(π/p), with cot(π/p) = −tan(π/N). Fitting B from exact eigenvalues gives:

  pole term = **(N − 1)/(6(N + 2))**:  1/12, 5/48, 7/60, 1/8, 11/84 for N = 4, 6, 8, 10, 12,  to 10⁻⁹–5·10⁻⁸.

- The second-order WKB constant carries tan(π/N) times Gamma ratios, and the π cot kernel cancels it exactly, leaving a
  rational.
- N = 1 (V = |q|) gives 0, consistent with the cot = 0 behaviour of linear potentials (the bouncer, §3.12).
- The N = 2 limit is 1/24, where the harmonic oscillator's exact Bohr–Sommerfeld rule meets the resonance p = 1. The N → ∞
  limit is 1/6.
- N = 4 and N = 6 are tested against b_n itself (`checks/spec_qN.py`, `checks/spec_qN.out`):

  | N | d₁ fit (pred) | ε₁ fit (pred 0) | d₂ fit (spread) | shift + (N − 1)/(6(N + 2)) | without pole term |
  |---|---|---|---|---|---|
  | 4 | +0.16666667 (1/6) | 1·10⁻⁵ ± 3·10⁻³ | +0.276010 (1·10⁻⁵) | +0.276042 | +0.192708 |
  | 6 | +0.25000000 (1/4) | 5·10⁻⁵ ± 2·10⁻³ | +0.315918 (3·10⁻⁵) | +0.315972 | +0.211806 |

  For N = 8–12 the rational is the pole law's prediction, evaluated with an exact-eigenvalue B. (The scripts' regularised
  Z(−1), about 10⁻³–10⁻², is a truncation artefact. The heat-trace exponents −a + 2aj contain no 1 for N = 4, 6, so Z(−1) = 0,
  and the fits agree with 0.)
- **Derivation (same day; PROVED-mod-cite given the second-order Bohr–Sommerfeld/Dunham term, NOT QUOTED; conditional on
  the pole law).** The second-order quantisation reads

    (1/π)∫_{−q₊}^{q₊}√(E − V)dq − (1/(24π))·∂²_E∫_{−q₊}^{q₊}V′²(E − V)^{−1/2}dq = K − ½ + O(E^{−3a}),

  and the coefficient −1/(24π) is checked numerically at N = 4: B/(5·I₆) = −0.013263 = −1/(24π). For V = q^N, with x := 1/N
  and the substitutions q = E^{1/N}t, u = t^N:
  - A = (2/(πN))·B(x, 3/2);
  - B = −(N/(12π))·e(e − 1)·B(2 − x, ½), where e = 3/2 − x.
  The reflection formulas Γ(x)Γ(1 − x) = π/sin πx and Γ(½ + x)Γ(½ − x) = π/cos πx collapse the product to

    A·B = −(N − 1)·cot(π/N)/(6π(N + 2)).

  The pole term is A·B·π·cot(π/p), and π/p = π/2 + π/N, so cot(π/p) = −tan(π/N). It therefore equals **(N − 1)/(6(N + 2))**.
  The kernel's cot(π/p) cancels WKB's cot(π/N) identically. This explains why every homogeneous potential gives a rational
  d₂ shift, and N = 4 reproduces B = −1/(12πA).

### 3.18 The noise mechanism: an edge kernel and a variance-level linear statistic (NUMERICAL; single seeds; NOT REVIEWED)

**Single-node kernel** (`checks/spec_edgekernel.py`, `checks/spec_edgekernel.out`; p = 0.6, s = 2). Node k₀ ∈ {100, 200, 400, 600}
is moved by ±0.05. The linear response F(n; k₀) = [D(+h) − D(−h)]/2h, with D = n(y − y_lattice), is followed in τ = (n − n*)/n*^{1/3},
where n* = k₀(4c)^{1/p} is where the node crosses the edge. The quadratic part is about 0.1 of the linear one per unit h.
- **Outside the band (τ > 0): one universal curve, with no amplitude scaling.** At τ = 1, 2, 3 the four nodes give 0.79–0.88,
  0.32–0.36 and 0.18–0.19. For τ ≥ 2 this agrees with the derivative of S2′'s law, (p²/2k₀)u(1 − u)^{−3/2}, to 1–3%. Near τ = 0 it
  is finite (0.1–1.2) where S2′ diverges: the Airy smoothing of the edge.
- **Just inside (τ ∈ [−1, −½]): also universal.** F(−1) = −4.7 … −5.2 and F(−½) = −2.8 … −3.1.
- **Deeper in the band: O(3) per unit h, oscillating.** The sign flips with a period of about 2–3 in τ, i.e. about 10 nodes,
  and the response decays only as u grows to about 2 (§3.6). Its sums over n cancel almost completely (2–5, against a
  random-walk scale of 50–100). This is the precise sense in which "in-band nodes average to zero" (§3.13).

**Is the noise a linear statistic?** (`checks/spec_noiselin.py`, `checks/spec_noiselin.out`). Take the GUE and Poisson
realisations of §3.6 (seed 7), with displacements h_k = x_k − k, and compare the full noise N₁ with the linearised response
L = [N_ε − N_{−ε}]/2ε (ε = 0.05).
- **Point by point: no.** corr(N₁, L) = 0.23–0.43 (GUE, RMS h = 0.9) and −0.04–0.47 (Poisson). The curvature part is comparable.
  A displacement of about one node spacing is already nonlinear near the edge, consistent with the kernel's oscillation scale
  of about 10 nodes.
- **In amplitude: yes.** RMS(L) ≈ RMS(N₁) in every octave:

  | window | GUE: N₁ / L | Poisson: N₁ / L |
  |---|---|---|
  | [100, 200) | 3.79 / 3.67 | 10.3 / 9.3 |
  | [200, 400) | 5.38 / 5.48 | 20.8 / 23.1 |
  | [400, 800) | 7.46 / 7.02 | 28.3 / 24.4 |
  | [800, 1600) | 11.6 / 10.6 | 41.8 / 39.3 |

  The Poisson/GUE ratio of L (2.5–4.2) matches that of N₁ (the 3.3–4.0 of §3.6).

**Reading (HEURISTIC).** The noise has the variance of the linear statistic Σ_kF(n; k)h_k but not its realisation. A
displacement field of O(1) mostly re-phases the oscillating in-band kernel instead of adding to it. So its covariance, not
its pattern, survives. On that reading the noise amplitude is set by the displacement spectrum at the kernel's
wavelength:
- Var N ≈ Σ_{k,l}F(n; k)F(n; l)Cov(h_k, h_l);
- the GUE/Poisson ratio is √(K_GUE(ω₀)/K_Poisson(ω₀)) at ω₀ ≈ 2π/10, where K is the spectral form factor. That gives ≈ 3.5,
  against the 3.3–4.0 observed.
This is a concrete version of the Krylov-complexity hypothesis that Lanczos fluctuations are driven by spectral rigidity.
Untested parts:
- the form-factor formula itself, which needs the kernel row F(n; ·) at fixed n, not only the four columns measured here;
- more seeds;
- the √n growth of the amplitude, which in this picture comes from the slow in-band decay of F.

### 3.9 Novelty (Rule L, first pass, 2026-10-20) — summary of research/program/novelty_SPEC.md (local, gitignored)

The search was web-only: arXiv was read through WebFetch, and MathSciNet/zbMATH were unavailable. Quotes there are second-hand
and must be re-read before citing (Rule C). "Not found" describes the search, not a proof of novelty.

| Item | Verdict | Closest prior work |
|---|---|---|
| S1: ε_j = C(2j, j)pc^jZ(−j), j ≥ 1 | NOT FOUND | Monien 2006/2010; Haynes–Zudilin 2015 (leading order or experimental) |
| S1, j = 0: d₁ = −pα/2 + pZ(0) | exact special cases implicit in classical work | Lommel polynomials (Van Assche 1996 §3; Dickinson 1954), see below |
| Theorem S2′ (closed law −p(1−u)^{−1/2}) | PARTIALLY KNOWN: ingredients classical, closed scaled law not found | Uvarov 1969; Simon 2008 Thm 9.7 (Σ_jP_j(x₀)² = 1/w₀); Wong 2009; van der Sluis–van der Vorst 1986 |
| Prop. B values (Airy-zero zeta) | KNOWN | Naber 2022 (arXiv:2211.05808); Voros 1999 (Z^±(0) = ±¼) |
| Heat coefficients β₁, β₃ | follow from the known zeta values; not found written | — |
| Möbius identity (Prop. M) | elementary / PARTIALLY KNOWN | Vieira–Botta 2019 Thm 3 (degree-dependent weight) |
| κ-shift law −2(2−p)cκn^{−p} | NOT FOUND | — |
| GUE vs Poisson fluctuation law | qualitatively KNOWN in another setting | Krylov complexity: Rabinovici–Sánchez-Garrido–Shir–Sonner 2022 (Lanczos coefficients more disordered for integrable spectra) |
| Band factor = regular part of a spectral determinant | NOT FOUND | — |
| Airy index map | KNOWN | DLMF 9.9.1 (θ(a_k) = kπ); Fucci–Piorkowski–Stanfill 2025 Thm 3.7 |

Consequences for this note:
- **Sign conflict on the Dirichlet bouncer values: settled mathematically.** Naber's eqs. (74)–(75) give Z(−3) = −15/64 and
  Z(−6) = +1695/1024, the opposite signs to Proposition B. Proposition B is right (REVIEW_SPEC2_A §1): in Naber's own
  convention (eq. (52), as relayed) the series coefficients are b₁ = ¼, b₂ = 5/32, b₃ = 15/64, matching his eq. (53), and the
  correspondence rule gives Z(−3) = +b₃; so eq. (74) has a sign slip. An independent direct heat-trace computation from the
  zeros (no Riccati series, no regularised sums) tends to −5/128 = −Z_E(−3)/6. This settles the mathematics, not what the paper
  says: Naber has not been read under Rule C. Proposition B's novelty is downgraded to "known values; independent
  derivation and numerical confirmation".
- **Lommel / Bessel-zero family (exact check of the j = 0 term).** The measure on 1/j²_{μ,k} (p = 2, s = 2) has Lommel-polynomial
  recurrence coefficients (Van Assche 1996 §3; recurrence quoted in RH/CITATIONS.md as VA). The search report's computation
  from that recurrence gives n²b_n/c = 1 − μ/n + (3μ²/4 + 1/8)/n² + O(n⁻³). S1's j = 0 term predicts d₁ = ½ + 2ζ(0, μ/2 + ¾) = −μ,
  which matches for all μ. At μ = ½ the n⁻² coefficient 5/16 equals E3's d₂(2, 2). It does not test ε_j (p = 2). NOT yet
  re-derived in this repo.
- **Citations to add.** Simon 2008 Thm 9.7 for step (a) of S2′ (the self-contained proof stays); Uvarov 1969 for Lemma U;
  DLMF 9.9.1 for the Airy index map (§3.8, after aligning phase conventions); Rabinovici et al. 2022 in §3.6.
- **Still to search:** MathSciNet/zbMATH (Lommel asymptotics, varying point masses), Voros 1987 (Z(0) as a Maslov term),
  Branson–Gilkey (β₁), and FPS §5.2 (the sign of Z(−3)).

## 4. What this opens (HEURISTIC)

- **Jacobi matrices as spectral invariants.** For regular spectra, the asymptotic expansion of b_n for the measure on
  reciprocal eigenvalues reads off Z_Λ(0), Z_Λ(−1), …, i.e. heat-trace coefficients (for the bouncer: −¼, 0, 0, 0.01055…).
- **A closed form beyond series.** S2 is a resummed, per-node statement. If S2 holds, the full first-order correction from the
  nodes outside the band is p·Σ_{u_m<1}(1 − u_m)^{−1/2}, regularised by Z_Λ (made precise in §3.13 as a Mellin pole part; the
  literal sum carries an extra O(n^{−1/2}) edge oscillation). This is route 3 of the session (resummation)
  joined to route 1.
- **Irregular spectra.** By S4 the relevant object is not the zeta function but the local node statistics at the soft edge
  threshold. That is a different, probably harder question, and it is the one relevant to surfaces.

## 5. Next steps

1. **S1 for Hurwitz lattices.** Done: the moment identity for both p > 1 and p < 1 (Lemma H), and the band-factor reduction
   for −1 < δ ≤ 0 (§3.1). Remaining:
   - the index offset (d₁ = −(s−1)/2 − pδ) from Paper 2's normalisation at ∞ with Γ(t − δ), including the δ → 0⁻ crossover;
   - the p < 1 outer construction (seams, glue) with the shift;
   - a Rule C quote of Hurwitz's formula.
   This is a plan-sized task (a shifted copy of Paper 2 §§5–6 and E_pgt1/E_plt1), not a lemma.
2. **S2.** Theorem S2′ (§3.2) proves it for one deleted atom of σ_{p,s}, away from the turning point, with error O(n^{−ε}).
   Remaining:
   - the turning-point region u → 1 (Airy, the S4 mechanism);
   - for p ≥ 1, an error sharper than O(n⁻¹) to resolve the u-terms at fixed k₀ (numerically R = O(1/n) everywhere);
   - several nodes, or added nodes (needs coefficient expansions for modified measures).
3. **Bouncer.** Closed forms derived (Proposition B, §3.3). Remaining: quote Hadamard's factorisation and the Mellin
   correspondence (Rule C), the remainder bound and differentiation of the expansion (REVIEW_SPEC2_A F9). Reviewed (Rule R,
   REVIEW_SPEC2_A). The n⁻³ coefficient needs the subleading pole term (§3.12) as well as ε₃, and third-order fits.
4. **Directions 2–4 (§§3.4–3.7).**
   - Maslov readout: done for the bouncer. Next: an operator where μ is not fixed by a single wall.
   - λ + κ: first-order derivation done (§3.5), and the law is a pole-law term (§3.12). Remaining: the second-order bound.
   - Noise: ensembles over seeds, the amplitude as a function of local statistics, and the autocorrelation.
   - Determinant construction: carry out "Paper 2 for Airy nodes" (P1)–(P4).
5. **Quartic oscillator** (p = 4/3, the κ-regime of E3 Thm E3.1): compare 2pcZ(−1) with Voros's spectral zeta.
6. **Quantify S4**: the amplitude and law of the soft-edge noise.
7. **The pole law.** Kernel derived (§3.14): Theorem K for the lattice, and the soft-edge condition (Lemma Q, Proposition E)
   for the poles. Remaining: Hypothesis G, i.e. Paper 2's construction for non-lattice nodes; the p < 1 version of Theorem K;
   and E3.7 for branched hard-edge tilts. Then the subleading pole terms (§3.12,
   Limitation), with the exact Bessel family and the Hurwitz p = 2 control (ε₁ = π²/256) as test data.

## 6. Rule A / Rule X log

- *Provenance.* S1 was formulated from the pattern ε_j = C(2j, j)pc^jζ(−jp) of E3 and the d₁ = −(s−1)/2 − pδ data of
  check_so_lattice (Plan 62), before the Hurwitz runs. Every S1/S2 prediction in §2 was computed from the formula, not fitted.
  The exception is d₁ for the shifted lattices, which was already known (SECOND §4.1).
- *Could the bouncer agreement be trivial?* The Hurwitz-only value is nonzero (−0.0113). The vanishing comes from the WKB
  correction terms, and the fit sees it to 6·10⁻⁵. The d₁ shift from −½ to −⅓ at s = 2 is the ζ(0, ¾) offset, which is
  independent of the other check.
- *Fit artefacts in S4?* Deep-band jitter, fitted by the same code, gives RMS 10⁻⁹. So the n^{−1/2} noise is in the data, not
  the fit.
- *Lemma U / S2′ (after review).* Exact finite test: the reviewer's chain (b)–(d), run from σ's coefficients alone, reproduces
  the measured Δ²F to 10⁻¹²–10⁻¹⁶ (REVIEW_SPEC_A T2/T3). Far-node regime u → 0: all estimates in (c)–(d) are relative and
  avoid division by u (F2). k₀ = 1 (x₀ = 1, the largest atom, u_n = 4cn^{−p}): S2′ predicts −p + O(n^{−ε}), the index shift.
- *Lemma H.* An integer δ (a = 1) reduces to E3 Lemma F.1′(i). The check grids use δ ∈ {−½, 0.3, ¾, 1.4} (p > 1) and
  δ ∈ {0, −½, 0.3, 1.4} (p < 1).
- *Cache provenance.* The coefficient files are in `tmp/spectral_cache/` (gitignored), named `<tag>__<hash>.txt` with the
  hash taken over the node array and (p, s, tail δ, K), so a changed measure can never reuse a stale cache (REVIEW_SPEC2_B F2).
  The Hurwitz runs use the Plan 62 cache (`so_coeffs.coeffs(..., delta)`). `checks/run_all.sh` regenerates every .out from
  scratch in dependency order (readers of other scripts' caches run last); about 1–2.5 min per (measure, n_max = 1600) on 2
  cores. Every script now ends with assertions on its predictions (`ALL n CHECKS PASSED`). The output of spec_rigid.py is in
  spec_jitter.out (REVIEW_SPEC2_A provenance note).
- *Second review round (2026-10-21; REVIEW_SPEC2_A, REVIEW_SPEC2_B).* Both readers re-derived the formulas and re-ran the
  measures independently, with sabotage tests on the scripts. Fixes applied:
  - pole-law sign (A F1, B F1): text corrected to +p·R·W·π cot; the table always used the right sign;
  - subleading pole terms (A F2, MAJOR): limitation added to §3.12; §3.3's "ε₃ predicted exactly" withdrawn;
  - κ law as a pole-law term (A F3), with an out-of-sample p = 1.5 run;
  - S1‴ scope (A F4, F5): Weyl pole excluded, Mellin pole part, leading order per node;
  - resonance (A F6, B F6): weak test, all-orders Z_fin, post-mismatch correction recorded;
  - precision downgrades (B F5): pole table, Hurwitz d₃, κ at p = 0.3;
  - text (A F7, F12, F13), Proposition B gaps (A F9), Robin additions (B F7), hygiene (B F2, F9).
  - *Rule X, pole law.* The π cot kernel was identified from the m = 1 data at p = 0.6 and 1.5; those rows are not evidence. The
    predictions for the other rows were committed before the measures were generated (git timestamps, B F10).
