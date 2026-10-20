# SPEC: Jacobi coefficients of measures on reciprocal spectra — the node-zeta law (exploration)

Status (2026-10-20): exploratory note from the Plan E3 session. Labels per VERIFICATION_POLICY.md.
- §§1–2 and §4: CONJECTURE / HEURISTIC / NUMERICAL (Rule N: fit half-ranges are spreads over fit choices, not error bounds).
- §3.2: Lemma U (PROVED) and Theorem S2′ (PROVED-mod-cite), **REVIEWED** (Rule R: REVIEW_SPEC_A.md, ACCEPT WITH FIXES; fixes
  applied, §6). A single second reader; the other parts were reviewed for labels only.
- §3.1: Lemma H is CONDITIONAL on Hurwitz's formula (unread under Rule C), with NUMERICAL confirmation.
- §3.3: Proposition B, PROVED-mod-cite pending Rule C (Hadamard factorisation of Ai; the Mellin correspondence), NOT REVIEWED;
  NUMERICAL confirmation. This note builds on E3.md (REVIEWED), in particular its Lemma E3.7. Novelty: UNCHECKED
(Rule L not done).

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
The ε₃ term sits at n^{−1−3p} = n^{−3}, where it merges with the n⁻³ term, below the resolution of the §2 fits. So the bouncer's first nonzero spectral correction
beyond d₁ is predicted exactly but not yet observed.

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
  (p, κ) = (0.6, 1), (0.6, ½) and (0.3, 1). The candidate −2(2−p)cκ gives −1.2025, −0.6012 and −1.2226; all agree within 0.1%.
  The fit half-ranges are large (0.04–0.7), so this is a NUMERICAL candidate, not an identification.
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

**GUE-like against Poisson nodes** (`checks/spec_stats.out`). The first M = 3000 nodes are replaced by unfolded CUE eigenphases
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

## 4. What this opens (HEURISTIC)

- **Jacobi matrices as spectral invariants.** For regular spectra, the asymptotic expansion of b_n for the measure on
  reciprocal eigenvalues reads off Z_Λ(0), Z_Λ(−1), …, i.e. heat-trace coefficients (for the bouncer: −¼, 0, 0, 0.01055…).
- **A closed form beyond series.** S2 is a resummed, per-node statement. If S2 holds, the full first-order correction from the
  nodes outside the band is p·Σ_{u_m<1}(1 − u_m)^{−1/2}, regularised by Z_Λ. This is route 3 of the session (resummation)
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
   correspondence (Rule C), and a Rule R review. Observing ε₃ at n⁻³ would need third-order fits.
4. **Directions 2–4 (§§3.4–3.7).**
   - Maslov readout: done for the bouncer. Next: an operator where μ is not fixed by a single wall.
   - λ + κ: derive −2(2−p)cκ from the varying-weight (Möbius) picture.
   - Noise: ensembles over seeds, the amplitude as a function of local statistics, and the autocorrelation.
   - Determinant construction: carry out "Paper 2 for Airy nodes" (P1)–(P4).
5. **Quartic oscillator** (p = 4/3, the κ-regime of E3 Thm E3.1): compare 2pcZ(−1) with Voros's spectral zeta.
6. **Quantify S4**: the amplitude and law of the soft-edge noise.

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
- *Cache provenance.* The coefficient files are in `tmp/spectral_cache/` (gitignored). The Hurwitz runs use the Plan 62 cache
  (`so_coeffs.coeffs(..., delta)`). The scripts regenerate everything from scratch; at 2 cores this takes about 3 min per
  (measure, n_max = 1600).
