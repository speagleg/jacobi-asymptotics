# SPEC: Jacobi coefficients of measures on reciprocal spectra — the node-zeta law (exploration)

Status (2026-10-20): exploratory note from the Plan E3 session; **NOT REVIEWED**. Labels per VERIFICATION_POLICY.md. Nothing
here is PROVED. The numerics are NUMERICAL (Rule N: fit half-ranges are spreads over fit choices, not error bounds). The
statements are CONJECTURE or HEURISTIC. This note builds on E3.md (REVIEWED), in particular its Lemma E3.7. Novelty: UNCHECKED
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

**Conjecture S2 (exact per-node contribution).** Let a single node λ (n-independent) be deleted from Λ. While the node is
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

**Observation S4 (limit of regularity; NUMERICAL).** If the node positions deviate from a smooth node function by a fixed
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

The ratio tends to 1 like 1 − O(1/(n(1 − u))), which is consistent with an O(n⁻¹) correction that grows near the edge. For
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

## 3. What this opens (HEURISTIC)

- **Jacobi matrices as spectral invariants.** For regular spectra, the asymptotic expansion of b_n for the measure on
  reciprocal eigenvalues reads off Z_Λ(0), Z_Λ(−1), …, i.e. heat-trace coefficients (for the bouncer: −¼, 0, 0, 0.01055…).
- **A closed form beyond series.** S2 is a resummed, per-node statement. If S2 holds, the full first-order correction from the
  nodes outside the band is p·Σ_{u_m<1}(1 − u_m)^{−1/2}, regularised by Z_Λ. This is route 3 of the session (resummation)
  joined to route 1.
- **Irregular spectra.** By S4 the relevant object is not the zeta function but the local node statistics at the soft edge
  threshold. That is a different, probably harder question, and it is the one relevant to surfaces.

## 4. Next steps

1. **Prove S1 for Hurwitz lattices.** Lemma F.1(iii)/F.1′(i) with the jump phase e^{±2πiδ}: the moment integral gives
   Σ_m cos(πs/2 − 2πmδ)/m^s, and DLMF 25.11.9 (Hurwitz's formula) turns it into ζ(−kp, a). Lemma E3.7 is unchanged. The d₁ shift
   needs the index count (SECOND §4.1).
2. **Prove S2** via Lemma E3.7 applied to the tilt (1 − xλ/n^p)^{±2}, including the uniformity issue as u → 1.
3. **Bouncer.** Prove Z(−j) = 0 for 3 ∤ j from the heat trace, or find it in the literature; then the bouncer row is
   S1 plus a known identity.
4. **Quartic oscillator** (p = 4/3, the κ-regime of E3 Thm E3.1): compare 2pcZ(−1) with Voros's spectral zeta.
5. **Quantify S4**: the amplitude and law of the soft-edge noise.

## 5. Rule A / Rule X log

- *Provenance.* S1 was formulated from the pattern ε_j = C(2j, j)pc^jζ(−jp) of E3 and the d₁ = −(s−1)/2 − pδ data of
  check_so_lattice (Plan 62), before the Hurwitz runs. Every S1/S2 prediction in §2 was computed from the formula, not fitted.
  The exception is d₁ for the shifted lattices, which was already known (SECOND §4.1).
- *Could the bouncer agreement be trivial?* The Hurwitz-only value is nonzero (−0.0113). The vanishing comes from the WKB
  correction terms, and the fit sees it to 6·10⁻⁵. The d₁ shift from −½ to −⅓ at s = 2 is the ζ(0, ¾) offset, which is
  independent of the other check.
- *Fit artefacts in S4?* Deep-band jitter, fitted by the same code, gives RMS 10⁻⁹. So the n^{−1/2} noise is in the data, not
  the fit.
- *Cache provenance.* The coefficient files are in `tmp/spectral_cache/` (gitignored). The Hurwitz runs use the Plan 62 cache
  (`so_coeffs.coeffs(..., delta)`). The scripts regenerate everything from scratch; at 2 cores this takes about 3 min per
  (measure, n_max = 1600).
