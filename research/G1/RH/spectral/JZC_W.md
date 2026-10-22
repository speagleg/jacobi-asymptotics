# JZC W: the general statement — Jacobi coefficients of measures on reciprocal Weyl-type spectra (Conjecture W)

Status (2026-10-22): NOT REVIEWED. Labels per VERIFICATION_POLICY.md. Conjecture W itself is a **CONJECTURE (NUMERICAL)**; its
special cases carry their own labels (§1.4). **For the family λ_k = (k + δ)^p + κ** (p > 1, −1 < δ ≤ 0, κ > −a^p, |α| < 1) W is
**PROVED-mod-cite + REVIEWED at first order in the poles** (remainder O(n^{−2p}); O(n^{−1−p}) in W's displayed form), with one unreviewed
input (JZC_W_exact WE.1): JZC_W_outer.md + JZC_W_kappa.md (P K.11, P K.12, Prop K.12′) + JZC_W_BT.md (BT.1, BT.5); §1.5 (updated 2026-10-22 after Rule R review A of the W chain, research/G1/review/REVIEW_JZC_W_kappa_chain_A.md). Novelty: UNCHECKED (no Rule L pass for this note; NOVELTY_JZC.md covers the
ingredients). Checks: `checks/w_common.py`, `w_spectra.py`, `w_predict.py/.out`, `w_test.py` → `w_test.out`; caches in
`tmp/w_cache/` (gitignored). No claim about RH: no measure built from zeta zeros is used anywhere in this note.

| # | Statement | Label |
|---|---|---|
| Conj W | n^pb_n/c for a weighted Weyl-type node set = decoupled model M(β, ν) (ν = α, β = α − 2Z(0) − 1), flowed along the (fractional) Toda hierarchy with times read off from Z(−j), the density factor and the mass factor, plus the π cot pole terms of the non-Weyl poles of Z, all in the natural index N = n + (β+1)/2 | CONJECTURE (NUMERICAL: §2; 9 pre-registered measures, all 40 claimed coefficients pass; exact Lommel anchor) |
| Refinement W′ | pole and fractional terms carry the zeta layer's dressing g(w) = A(w) + B(w)ν² continued to w = q; at q = ½ this is a finite 0·∞ term R_{1/2}W(½)π²(p+2)²(p+4)(1−4ν²)/256·n^{−3−p/2} | CONJECTURE (identified after the M1 n⁻⁴ failure; explains M1, K2p, K2m and the Lommel zero; then 2 pre-registered measures pass, §2.4) |
| Prop W.1 | the density factor D(x) = 1 − pΣ_qR_qx^{q+1/p} is exact (linear in the residues) | PROVED (elementary, §1.2) |
| Prop W.2 | special cases: Theorem N.6, Theorem H, the pole law (leading), S1⁗, the κ law, S1′, rule H, Prop N.2 | reduction PROVED (algebra, §1.4); the cases keep their own labels |
| Obs W.3 | Bessel zeros at P = 2: all Toda times vanish (t₁, t₂ to 10⁻²¹, 10⁻¹⁶); the Lommel exactness is "t ≡ 0" | NUMERICAL (j = 1, 2); consistent with Prop N.2 |
| Obs W.4 | sphere-like spectrum l(l+1) with multiplicity 2l+1: Z(−j) = 0 for all j ≥ 1 and mass × density factor ≡ 1, so b_n is the bare model M(1, 0) at p = 2 through n⁻³, plus the W′ term at n⁻⁴ | Z(−j) = 0: PROVED (elementary, §2.4); the b_n statement NUMERICAL (n⁻⁴ to 2·10⁻⁸ with W′) |
| Finding | for spectra with multiplicities, Z must be the zeta function of the **distinct** nodes; multiplicity enters as a mass tilt. The "spectral zeta with multiplicities" reading is false at leading order | NUMERICAL (M1, M2: alternatives excluded by 10²–10⁴ tolerances) |

## 1. Conjecture W

### 1.1 Setting and hypotheses

Λ = {λ_k}_{k≥1} (nodes) and masses w_k > 0; the measure is σ := Σ_k w_kδ_{1/λ_k}. Hypotheses:
- **(W1) Nodes.** 0 < λ₁ < λ₂ < … → ∞, distinct. Repeated eigenvalues of an operator are merged into one node; the multiplicity goes
  into the mass (b_n sees distinct nodes only; SPEC §3.16).
- **(W2) Weyl-type regularity.** There is an index function κ with κ(λ_k) = k exactly and an asymptotic expansion, differentiable
  termwise,
    κ(λ) = λ^{1/p} + Σ_{r∈𝓡}A_rλ^r + κ₀ + O(λ^{−M}),  λ → ∞,
  with p > 0, 𝓡 ⊂ (−∞, 1/p)∖{0} finite (for each M). The smoothed counting function is N̄(λ) = κ(λ) − ½. Equivalently, λ_k^{1/p} has
  an expansion in powers of k of the S1 type (SPEC §1), allowing the shifted Weyl exponents of the κ law (r = 1/p − 1). (W2) excludes
  counting fluctuations (SPEC S4 / §3.6 / §3.18: chaotic, integrable-billiard and jittered spectra).
- **(W3) Masses.** w_k = λ_k^{−s/p}v(λ_k) with v(λ) = v₀λ^τ(1 + Σ_ρb_ρλ^{−ρ}) asymptotically (ρ > 0); v ≡ 1 is the program's
  normalisation σ_Λ = Σλ^{−s/p}δ_{1/λ} (SPEC §0); v(λ_k) = multiplicity for an operator spectrum with multiplicities. Put
  s_eff := s − pτ and **α := (s_eff − 1 − p)/p**; require s_eff > 1 (proved special cases: N.6 for all s > 1; Theorem H for
  s ∈ (1, 1 + 2p)).
- **(W4) p ≠ 1.** p = 1 is Remark 1.6.
- **(W5) Non-resonance (for the coefficients claimed).** For a pole q (below) with q ∈ ℕ, the integer term and the pole term
  merge into n^{−1−pq}log n (SPEC §3.13); W then makes no claim at n^{−1−pq} and beyond for that family of terms.

### 1.2 The spectral data

All of the following are read from (Λ, v); none is fitted.
- **Node zeta** Z(w) := Σ_kλ_k^{−w}, Re w > 1/p, continued meromorphically by (W2) (Hurwitz regularisation, SPEC §0). Its poles are
  w = 1/p (Weyl) and w = r ∈ 𝓡 with residue rA_r. In the variable of the pole law (w ↦ Z(−w)): poles at **q := −r** with w-residue
  **R_q = qA_{−q}**; the Weyl pole is q = −1/p and is excluded.
- **Z(0) = κ₀ − ½** (the constant term of N̄; Hurwitz: ζ(0, a) = ½ − a). **Z(−j)**, j ≥ 1: values (finite parts at a resonance).
- **Density factor** D(x) := (dN̄/dλ)/((1/p)λ^{1/p−1}), x = 1/λ.
  **Prop W.1 (PROVED).** D(x) = 1 − pΣ_qR_qx^{q+1/p} + O(x^{M+1/p}), exactly linear in the residues.
  *Proof.* dN̄/dλ = (1/p)λ^{1/p−1} + Σ_r rA_rλ^{r−1}; divide; rA_r = −qA_{−q} = −R_q and λ^{r−1/p} = x^{q+1/p}. ∎
  The first-order part −pR_qx^{q₁}, q₁ := q + 1/p, is SPEC §3.15's Jacobian tilt (log|t′| → γmn^{−1−m}z^{q₁}: with R = −mγ/p,
  −pR = mγ, and x^{q₁} = n^{−1−m}z^{q₁}).
- **Mass factor** V(x) := v(1/x)x^τ/v₀ = 1 + Σ_ρb_ρx^ρ.
- **Band tilt** T(x) := log V(x) + log D(x) =: Σ_ρB_ρx^ρ (a finite set of exponents ρ > 0 up to any order).
- **Toda times** (integer ρ = j and the discreteness of the nodes): **t_j := −2Z(−j)/j + B_j**; **fractional times** t_ρ := B_ρ (ρ ∉ ℕ).

Lattice: Z(0) = −½, Z(−j) = ζ(−jp), no poles, D = V = 1, t_j = −2ζ(−jp)/j (JZC_M4 §8).

### 1.3 Statement

**Conjecture W.** Under (W1)–(W5), with c = c(p), W(q) := (4c)^qΓ(q + ½)/(√πΓ(q + 1)), **β := α − 2Z(0) − 1**, **ν := α** and the
natural index **N := n + (β + 1)/2 = n + α/2 − Z(0)**:

  n^pb_n/c ≃ 𝔅_n[M(β, ν); (t_j)_{j∈ℕ}]
           + Σ_{q∉ℕ} pR_qW(q)π cot(πq)·(n/N)^pN^{−1−pq}
           − Σ_{ρ∉ℕ} (pρW(ρ)/2)·t_ρ·(n/N)^pN^{−1−pρ},

where
- (a) 𝔅_n[M(β, ν); 0] is the formal expansion of the decoupled model M(β, ν) of JZC_M4 §7 (Bessel order ν at the hard edge,
  Szegő exponent β, lattice g-function, n^p frame) — the integer layer;
- (b) 𝔅_n[M(β, ν); t] is that model flowed along the Toda hierarchy (JZC_M4 §8, Theorem T) for the fixed times t_j, i.e. with
  E3's band factor exp(−Σ_jμ_{n,j}z^j), μ_{n,j} = −t_jn^{−jp}, to all orders in t (Theorem N.6(i)'s double series);
- (c) the second line: the pole terms (SPEC §3.12) at their leading power and with the natural-index shift; the third line: the
  fractional Toda times, entering through E3.7's functional at first order. For ρ = j ∈ ℕ the same formula is the first-order
  Toda response, since ε_j = pW(j)Z(−j) = −(pjW(j)/2)t_j at B_j = 0: **one linear response −(pρW(ρ)/2)t_ρ for every time,
  integer or not**.

Claimed precision (as registered before the tests): the integer and Toda layers to every order (as in Theorem N.6(i)); each
pole/fractional term to relative O(N⁻²) (i.e. through n^{−2−pq}, n^{−2−pρ}); products of two pole/fractional terms, and of such a
term with a Toda time, are not claimed (they start at n^{−2−p(q+q′)}, n^{−2−p(q+j)} and include the drum's β² term, SPEC §3.16).

**Refinement W′ (identified after the sphere's n⁻⁴ failure, §2.4; one pre-registered confirmation; CONJECTURE).** Each pole and
fractional term carries the zeta layer's natural-form dressing continued in the index:

  pR_qW(q)π cot(πq)·(n/N)^pN^{−1−pq}·[1 + g(q)N⁻² + O(N⁻⁴)],  g(w) := A(w) + B(w)ν²,

with A_j, B_j of Theorem N.6(ii) (JZC_M4 §6) read as functions of w (similarly −(pρW(ρ)/2)t_ρ(n/N)^pN^{−1−pρ}[1 + g(ρ)N⁻²]). g has a
simple pole at w = ½ (the 1/(2j − 1) factor), where cot(πw) vanishes: **at q = ½ the dressed pole term is finite and nonzero
although the pole term itself vanishes**. From the closed forms, Res_{w=½}g(w) = −(p+2)²(p+4)(1 − 4ν²)/(256p) (sympy:
the A- and B-numerators at j = ½ are −3(p+2)²(p+4)/16 and (p+2)²(p+4)/4, with the factors 1/(48p) and ν²/(16p) from
1/(24(2w−1)p) = 1/(48p(w−½)) and 1/(8(2w−1)p)), and
lim_{w→½}cot(πw)g(w) = −π·Res g, so the term is

  **R_{1/2}·W(½)·π²(p+2)²(p+4)(1 − 4ν²)/256 · n^{−3−p/2}**   (p = 2: (3π²/8)(1 − 4ν²)R_{1/2}).

JZC_M4 §6 had anticipated this 0·∞ ("at w = ½, cot(πw) vanishes, so the product W·cot·g stays finite"). It vanishes for ν = ±½
at every p, which is why the Lommel family (ν = α = −½) shows nothing at n⁻⁴. The second-order natural-index shift of the pole term
is ∝ cot(πq) and adds nothing at half-integers.

### 1.4 Special cases (Prop W.2; each reduction is algebra, the cases keep their labels)

| case | data | W gives | label of the case |
|---|---|---|---|
| lattice λ_k = k^p (v = 1) | Z(0) = −½, t_j = −2ζ(−jp)/j, no poles | M(α, α) + Toda: Theorem N.6(i)–(iii), Theorem T | PROVED-mod-cite (JZC_M4_proof), Theorem T PROVED-mod-cite |
| Hurwitz (k + δ)^p | κ = λ^{1/p} − δ: Z(0) = −½ − δ, Z(−j) = ζ(−jp, 1+δ), D = 1 | β = α + 2δ: Theorem H(i) (M(α + 2δ, α) with Hurwitz μ); rule H = H(ii) | PROVED-mod-cite for −1 < δ ≤ 0 (JZC_M3a_H §4; (ii): integer layer to all orders and zeta layers of weight ≤ 2 PROVED-mod-cite + REVIEWED via Theorem Σ, JZC_SIGMA.md; weight ≥ 3 beyond Prop S's orders CONDITIONAL) (updated 2026-10-22 after Theorem Σ, JZC_SIGMA.md) |
| (k + γk^{−m})^p | q = m/p, R = −mγ/p, Z(0) = −½ | leading: −mγW(m/p)π cot(πm/p)n^{−1−m} (pole law); next order: shift −(1+m+p)(s−1)/(2p)·L and tilt −(mpq₁/2)W(q₁)γ | S1″ and S1⁗: CONJECTURE (NUMERICAL), SPEC §3.12, §3.15 |
| k^p + κ | moved Weyl pole q = 1 − 1/p, R = −κq/p | −2(2−p)cκn^{−p} | κ law, NUMERICAL (SPEC §3.5, §3.12) |
| bouncer, Robin, quartic | WKB index corrections | S1′ values, cot = 0 at half-integers, quartic d₂ | NUMERICAL (SPEC §3.3–3.4, §3.13, §3.17) |
| Bessel zeros, P = 2, s = 2 | Z(0) = −ν/2 − ¼, poles at half-integers, D from McMahon | β = ν − 1, N = n + ν/2, **all t_j = 0** (Obs W.3), so W = M(ν − 1, −½) | Prop N.2 (exact closed form): PROVED-mod-cite |

Notes on the reductions.
- *S1⁗ in W.* The "Jacobian" term is the first-order fractional time t_{q₁} = −pR_q (Prop W.1); the "shifted pole" term is the
  expansion of (n/N)^pN^{−1−pq} with N − n = (β+1)/2 = (s−1)/(2p) (the lattice's Z(0) = −½). W generalises the shift to
  N − n = α/2 − Z(0): tested in §2 (A15p, A3, B*: Z(0) ≠ −½).
- *The Bessel "cancellation" (SPEC §3.12 Limitation, F2) reinterpreted.* SPEC read the exact Lommel index shift as a subleading
  pole term cancelling ε₁ at n⁻³. In W both are parts of one Toda time, t₁ = −2Z(−1) + B₁, and **t₁ = 0** (the density coefficient
  of x¹ equals 2Z(−1)). The same holds for t₂ (Obs W.3). If t_j = 0 for every j, Lommel = M(ν − 1, −½) exactly, which is what
  Prop N.2 says through order N⁻⁶. W thus *predicts* the Bessel/Lommel exactness from spectral data alone (§2.1).
- *Integer q₁.* When q + 1/p ∈ ℕ (Bessel and sphere at p = 2, family A at p = 3 for q = 2/3), the density tilt is analytic and is a
  genuine Toda time; it is dressed by the engine like ε_j.

**Mismatches with earlier statements (findings).**
1. *Multiplicities.* SPEC/JZC_M3_scope phrase everything through "the spectral zeta function". For an operator spectrum with
   multiplicities that is wrong at leading order: the Weyl exponent of b_n is that of the distinct nodes (p_nodes = 2 for the
   sphere, against p_spec = 1), Z must be the distinct-node zeta, and the multiplicity is a mass tilt (it shifts s and adds
   fractional or integer Toda times). Tested in §2.4 (M1, M2).
2. *Scope of S1⁗.* SPEC §3.15 calls S1⁗ precise only for q₁ ≤ 1. In W the same term at q₁ = 4/3 (A15m, A15p, B0_15, B1_15)
   agrees to 2·10⁻⁶–3·10⁻⁵ in the median, against half-ranges 10⁻³–2·10⁻² (§2): consistent, at the precision those fits allow; the
   q₁ > 1 limitation looks like fit systematics, as SPEC's broad-pool refit suggested. The precise tests remain q₁ < 1 (A3, B0_3).
3. *Second order in the poles.* W is first order in each pole. The drum's β² term (SPEC §3.16, derived there from the exact
   continuum soft-edge condition) is the first known second-order pole term; for p ≠ 1 such terms sit at n^{−2−2pq} and were below
   the tested orders in every case of §2.
4. *Half-integer poles one order further down (found here).* "cot(πq) = 0 kills the pole term" (SPEC §3.12, used for the bouncer,
   Robin and Bessel) is true for the leading term and its natural-index shift, but not for the N⁻²-dressing at q = ½: W′ (§1.3,
   §2.4). This is a first-order term at n^{−3−p/2}, ∝ (1 − 4ν²)R_{1/2}.

### 1.5 What is proved, what is numerical, what is new

- **PROVED / PROVED-mod-cite (special cases):** Theorem N.6 (lattice), Theorem T (Toda structure), Theorem H (Hurwitz, −1 < δ ≤ 0,
  p ≠ 1), Prop N.2 (Bessel P = 2), Prop W.1 (the density factor), the reductions of §1.4, and Z(−j) = 0 for l(l+1) (§2.4).
- **PROVED-mod-cite + REVIEWED (the κ-family)** (updated 2026-10-22 after Rule R review A of the W chain, research/G1/review/REVIEW_JZC_W_kappa_chain_A.md): for σ^{δ,κ} (λ_k = (k + δ)^p + κ, p > 1, −1 < δ ≤ 0, κ ≠ 0, κ > −a^p,
  1 < s < 1 + 2p, i.e. |α| < 1), W holds at first order in the poles:
  n^pb_n/c = 𝔅_n[M(α + 2δ, α); t] + Σ_m(the continued symbolic-j layer at j = q_m, μ = −τ_mn^{−pq_m}; leading term
  pR_{q_m}W(q_m)π cot(πq_m)(n/N)^pN^{−1−pq_m}) + **O(n^{−2p})**; in W's displayed form (pole term × (1 + O(N^{−1}))) the remainder is
  **O(n^{−1−p})**: κ-free Szegő shift β′ = α + 2δ (Z(0) = −½ − δ), every n^{−k} coefficient with k < p that of M(α + 2δ, α), and the
  single pole term at n^{−p} with W's exact coefficient (JZC_W_kappa P K.11, P K.12 + Prop K.12′; JZC_W_outer P W-out.5, W-out.7;
  JZC_W_BT BT.1, BT.5). No hypothesis (BT, BT₀, BT_coh, (F-br)) is used. Rule R review A covered the chain; its one input not REVIEWED
  is JZC_W_exact Lemma WE.1 (elementary; WE.1(ii) independently spot-checked). **Not covered:** second order in the poles (products,
  the O(n^{−2p}) remainder); p < 1 (OBSTRUCTION for the lattice-g route, JZC_W_kappa P K.14); p = 1/m (κ-dependent Z(0)); α ∉ (−1, 1);
  non-coherent branched tilts ((F-br) for general branched band factors, a GAP; not needed for this family); W′ and the pole dressing
  beyond first order as separate statements. Novelty UNCHECKED (no Rule L pass).
- **NUMERICAL:** the pole law (SPEC), S1⁗ (SPEC), and Conjecture W on the nine measures of §2 and the Lommel anchor.
- **New in W (CONJECTURE):** (i) β = α − 2Z(0) − 1 beyond Hurwitz lattices, i.e. for node sets with poles (the Szegő shift and the
  pole terms coexist, and the pole terms live at the same natural index); (ii) the unification of the Jacobian tilt, the mass
  (multiplicity) tilt and the zeta layer as Toda times, integer and fractional, with one linear response −(pρW(ρ)/2)t_ρ;
  (iii) the multiplicity rule (finding 1); (iv) Obs W.3 and W.4; (v) W′ (post hoc, one pre-registered confirmation).

### 1.6 Remark: p = 1

At p = 1 (2-D drums, λ_k ~ k; 1-D and 3-D Laplacians have p = 2 and p = 2/3 and are covered) the statement degenerates:
- the zeta exponents 1 + jp are integers, so every Toda time lands on the integer layer, and the Weyl pole q = −1 is an integer:
  cot(πq) is singular at the Weyl pole itself, and resonances (log n terms) are generic;
- Theorem N.6 is not available (E_p1 is a separate construction with the Binet/Γ band factor; JZC_M4_proof excludes p = 1);
- the drum data of SPEC §3.16 are nevertheless what W predicts formally: the perimeter is the pole q = −½ with the 0·∞ limit
  W(q)π cot(πq) → −π(4c)^{−1/2}, the corners/curvature enter through Z(0) in β, i.e. pZ(0)/n in d₁; but the β² term is a
  second-order pole term outside W, and at p = 1 it lands on n⁻¹, the same order as the corner term. So a p = 1 version must
  include the continuum equilibrium to second order (SPEC §3.16's exact soft-edge solution) — that is the precise p = 1 obstacle
  on the conjecture side (§5.2 for the proof side).

## 2. Tests (predictions before fits)

### 2.1 Protocol (Rule X)

- **Predictions first.** `w_predict.py` computes every predicted coefficient from the spectral data of `w_spectra.py` (exact or
  Hurwitz-regularised Z(0), Z(−j); residues; mass factor) and the engine m4_rh4 (KORD = 4; Toda responses by central differences
  at 40 digits). It wrote `tmp/w_cache/predictions.json` at 08:09:00; `w_test.py` asserts that every measure cache is newer
  (all 9 were generated 08:24–08:50). Nothing in W is fitted: the alternatives are W with one piece switched off. `w_test.out` is
  the consolidated re-run from the caches (50 checks: 9 Rule X + 41 coefficients; one failure, M1 n⁻⁴, beyond W's claimed order,
  §2.4).
- **Internal checks (w_predict.out, 37 checks, all pass).** Z(0) by the regularised sum against the closed form (≤ 10⁻²⁶);
  each residue R_q against hZ(−(q+h)) (≤ 10⁻¹⁰ relative); McMahon (five terms) against mpmath.besseljzero for k = 150–300
  (4.8·10⁻²⁶ relative).
- **Measures.** Plan 62 pipeline (binary128 RKPW), n ≤ 1600; 160 000 atoms (320 000 for p < 1), Gauss–Jacobi continuum tail for
  the rest, with the multiplicity's exact tail density for M1/M2. 7–9 min per measure on 2 cores.
- **Fits.** For a target exponent e: subtract W's terms of order < e, fit n^{−e} with the next 2–5 exponents of {i + jp} as
  nuisance (plus n^{−e′}log n at a resonance e′ ≥ e), windows n ≥ 100, 200, 400: median and half-range over the 12 fits.
  Pass: |fit − W| ≤ max(3 half-ranges, 2·10⁻⁶(1 + |W|)). Half-ranges are spreads over fit choices, not error bounds (Rule N).
- **Fit-free cross-check (`w_resid.py`, declared after w_test).** S_n := n^e(y_n − Σ_{e′<e}W_{e′}n^{−e′}) − W_e at n = 200, 400,
  800, 1600 must decay to 0.

### 2.2 The anchor: Bessel zeros at P = 2 (W1; exact, no measure)

For λ_k = (j_{ν,k}/π)², s = 2 (α = −½): Z(0) = −ν/2 − ¼ gives β = ν − 1, N = n + ν/2. The total Toda parameters
μ_j = 2Z(−j)/j − B_j (Z from Hurwitz-regularised zero sums, B from McMahon's density factor) are
- ν = 0: μ₁ = −7·10⁻²², μ₂ = −9·10⁻¹⁷; ν = 1: μ₁ = 7·10⁻²², μ₂ = 9·10⁻¹⁷ (the limit is the regularisation's precision);
- the half-integer poles have cot = 0, so W = M(ν − 1, −½), and its coefficients of n⁻¹…n⁻⁴ equal those of the exact
  (n/N)²(1 − 1/(4N²))^{−1/2} to ≤ 2·10⁻²¹ (ν = 0: 0, ⅛, 0, 3/128; ν = 1: −1, ⅞, −¾, 83/128).
This is a prediction of an exact closed form from spectral data, at the order (n⁻³) where SPEC §3.12 had to invoke a cancellation.

### 2.3 Results (`w_test.out`; the fit, its half-range, W, and the alternatives' misses in tolerances)

**A: perturbed lattices λ_k = k^p + ak^{p−1}** (s = 2). Here λ^{1/p} = k + a/p + O(1/k): a Hurwitz offset δ = a/p plus decaying
index corrections; Z(0) = −½ − a/p; poles q_i = (i−1)/p (leading power n^{−i}, so every pole lands on an integer power).

| case | coefficient | W (components) | fit (half-range) | fit − W | alternatives excluded by |
|---|---|---|---|---|---|
| p = 1.5, a = −¾ (δ = −½) | n⁻¹ | +0.25 (model) | +0.25000000 (3·10⁻⁷) | −6·10⁻¹¹ | β = α: 3·10⁵ tol |
| | n⁻² | +0.0984431 = 0.211806 (model) − 0.113362 (pole q = ⅔) | +0.0984431 (3·10⁻⁵) | −3·10⁻⁹ | no pole: 1392; β = α: 1919 |
| | n^{−2.5} | +0.2215758 (Toda μ₁) | +0.2215749 (4·10⁻⁵) | −9·10⁻⁷ | no Z(−j): 1912 |
| | n⁻³ | +0.0699377 = 0.103299 (model) − 0.066128 (pole shift) − 0.050104 (pole q = 4/3) + 0.082871 (tilt ρ = 4/3) | +0.0699393 (1.1·10⁻³) | +1.6·10⁻⁶ | β = α 53, no pole 36, no tilt 25, no shift 20 |
| | n^{−3.5} | +0.147717 (Toda μ₁ dressing) | +0.14775 (2.9·10⁻²) | +3·10⁻⁵ | (weak: 2–5) |
| p = 1.5, a = 0.6 (δ = +0.4, outside Thm H) | n⁻¹ | −1.1 | −1.10000001 (2·10⁻⁶) | −8·10⁻⁹ | β = α: 95069 |
| | n⁻² | +1.0955036 (pole −0.072552) | +1.0955031 (1.6·10⁻⁴) | −5·10⁻⁷ | no pole 150; β = α 1652 |
| | n^{−2.5} | −0.2551911 | −0.2551896 (1.5·10⁻⁴) | +1.5·10⁻⁶ | no Z(−j) 577 |
| | n⁻³ | −1.0077315 (shift +0.186217, tilt +0.053037) | −1.0077655 (1.1·10⁻³) | −3.4·10⁻⁵ | β = α 269, no pole 63, no shift 55, no tilt 16 |
| | n^{−3.5} | +0.748561 | +0.748569 (3·10⁻²) | +9·10⁻⁶ | (weak) |
| p = 3, a = −0.6 (δ = −0.2) | n⁻¹ | +0.1 | +0.1 (2·10⁻⁹) | +6·10⁻¹³ | β = α 272727 |
| | n⁻² | +0.1347742 = 0.062222 + 0.072552 (pole q = ⅓) | +0.1347742 (5·10⁻⁹) | +5·10⁻¹⁰ | no pole 31968 |
| | n⁻³ | +0.0452648 = 0.009630 + 0.012092 (shift) − 0.022055 (pole q = ⅔) + 0.045598 (tilt ρ = ⅔) | +0.0452649 (2.7·10⁻⁶) | +1.0·10⁻⁷ | no tilt 5529, no shift 1466, no pole 1208 |
| p = 0.6, a = −0.3 (δ = −½) | n⁻¹ | −0.2 | −0.20000001 (3·10⁻⁵) | −1·10⁻⁸ | β = α 3225 |
| | n^{−1.6} | +0.0854664 (ε₁) | +0.0854637 (3.7·10⁻⁴) | −3·10⁻⁶ | no Z(−j) 77 |
| | n⁻² | +0.1329122 (pole q = 5/3: +0.090690) | +0.1327116 (1.1·10⁻³) | −2.0·10⁻⁴ | no pole 27, β = α 83 |
| | n^{−2.2} | −0.1622467 (ε₂) | −0.1621566 (1.5·10⁻³) | +9·10⁻⁵ | no Z(−j) 36 |
| | n^{−2.6}, n^{−2.8} | −0.062675, −0.234633 | −0.0597 (2.8·10⁻²), −0.228 (9·10⁻²) | | (weak) |

**B: Bessel zeros λ_k = (j_{ν,k}/π)^P** (s = 2; McMahon NOT QUOTED, checked numerically). Z(0) = −ν/2 − ¼; non-Weyl poles
q = (2i−1)/P; at P = 1.5, q = 2 meets j = 2 (log resonance at n⁻⁴, a nuisance column).

| case | coefficient | W (components) | fit (half-range) | fit − W | alternatives |
|---|---|---|---|---|---|
| ν = 0, P = 1.5 | n⁻¹, n⁻² | −0.125; +0.1957151 (pole q = ⅔: +0.022972) | −0.12500000; +0.1957150 (1.4·10⁻⁵) | −3·10⁻¹⁰; −1.3·10⁻⁷ | no pole 562; β = α 4776 |
| | n^{−2.5}, n⁻³ | −0.0035503; −0.0713449 | −0.0035510 (4.5·10⁻⁴); −0.071360 (1.8·10⁻²) | −7·10⁻⁷; −1.5·10⁻⁵ | weak (log column) |
| ν = 1, P = 1.5 | n⁻¹, n⁻² | −0.875; +0.7288269 (pole −0.068916) | −0.87500000; +0.7288264 (5.8·10⁻⁵) | −4·10⁻⁹; −5·10⁻⁷ | no pole 396; β = α 2469 |
| | n^{−2.5}, n⁻³ | −0.0664936; −0.5692249 | −0.0664957 (5·10⁻⁴); −0.569239 (1.7·10⁻²) | −2·10⁻⁶; −1.4·10⁻⁵ | no Z(−j) 42; n⁻³ weak |
| ν = 0, P = 3 | n⁻¹, n⁻² | +0.25; +0.0742502 (pole q = ⅓: −0.022972) | +0.25; +0.0742502 (3·10⁻⁹) | −1·10⁻¹²; +5·10⁻¹⁰ | no pole 10692; β = α 58180 |
| | n⁻³ | +0.0049259 = 0.028935 − 0.009572 (shift) − 0.014438 (tilt ρ = ⅔) | +0.0049264 (1.2·10⁻⁵) | +4.8·10⁻⁷ | no tilt 416, no shift 276, no pole 276 |

The n^{−3.5} rows (P = 1.5) agree to 3·10⁻⁴ against half-ranges near 1 (not informative). The fit-free S_n of `w_resid.out`
decays at every Bessel target through n = 800, which is where the half-range test is weak (e.g. B0_15 n⁻³: S_n = 1.5·10⁻⁴,
8·10⁻⁵, 5·10⁻⁵ at n = 200, 400, 800, against −6.8·10⁻³ for "no shift" and −1.7·10⁻² for "no tilt").

**M: multiplicities.**

| case | coefficient | W | fit (half-range) | fit − W | alternatives |
|---|---|---|---|---|---|
| M2: nodes l^{3/2}, mult 2l+1, s = 3 (s_eff = 2) | n⁻¹ | −0.5 | −0.50000000 (5·10⁻⁷) | −2·10⁻¹⁰ | |
| | n⁻² | +0.1180556 = 0.368056 (model) − ¼ (fractional time ρ = ⅔, B = ½) | +0.1180558 (3.8·10⁻⁶) | +2.7·10⁻⁷ | no mass tilt: 21830 tol |
| | n^{−2.5} | −0.0432947 | −0.0432967 (5·10⁻⁵) | −2·10⁻⁶ | no Z(−j) 275 |
| | n⁻³ | +0.1900476 = −0.267361 + 0.291667 (shift of the ρ = ⅔ term) + 0.165742 (ρ = 4/3) | +0.1900481 (1.1·10⁻³) | +4.8·10⁻⁷ | no mass tilt 141, no shift 90 |
| M1: l(l+1), mult 2l+1, s = 4 (s_eff = 3, α = 0, p = 2) | n⁻¹, n⁻², n⁻³ | −2, +3.25, −5 (pure M(1, 0): all t_j = 0) | −2.00000000, +3.25000000, −4.99999992 (≤ 3·10⁻⁶) | ≤ 8·10⁻⁸ | n⁻³: "density tilt only" or "mass tilt only" off by ∓0.154 = 12851 tol |
| | **n⁻⁴** | +7.5449219 (model) | **+7.776241 (3.3·10⁻⁴)** | **+0.23132** | **FAIL** (beyond W's claimed order; §2.4) |

The "spectral zeta with multiplicities" reading is not even at the right order: Z_spec(w) = Σ(2l+1)(l(l+1))^{−w} has Weyl exponent 1
(p_spec = 1), while b_n follows the distinct-node law n^{−2}b_n → c(2) (fit d₁ = −2.00000000 with c = c(2)).

### 2.4 The sphere at n⁻⁴ (the one failure)

- *What W claims.* For M1 the only non-Weyl poles are q = i − ½ (the κ-type shift l(l+1) = (l+½)² − ¼), with cot(πq) = 0, and the
  density and mass factors cancel exactly (the mass per unit λ is λ^{−s/2}dλ). Also **Z(−j) = 0 for all j ≥ 1** (PROVED,
  elementary). *Proof.* With t = l + ½ ∈ 3/2 + ℕ₀, write (t² − ¼)^j = Σ_mc_mt^{2m}, so Z(−j) = Σ_mc_mζ(−2m, 3/2). Since
  ζ(s, ½) = (2^s − 1)ζ(s) (from the definition) and ζ(−2m) = 0 for m ≥ 1, ζ(0, ½) = 0, we get ζ(−2m, 3/2) = ζ(−2m, ½) − (½)^{2m}
  = −(½)^{2m} for every m ≥ 0. Hence Z(−j) = −((½)² − ¼)^j = 0. ∎ (Checked to 40 digits.) So every term W claims at n⁻¹…n⁻³ is the
  bare model M(1, 0), and those three coefficients pass at 10⁻⁷–10⁻¹⁰.
- *What fails.* At n⁻⁴ the fit exceeds M(1, 0) by +0.23132 ± 3·10⁻⁴; the fit-free S_n is 0.17, 0.20, 0.22, 0.21 (n = 200…1600):
  a real term. Numerically 0.23132 = 3π²/128 = 0.231309 (to 1·10⁻⁵, inside the half-range; an identification, not a prediction).
- *Why it is outside W's claim.* n⁻⁴ = n^{−2−2pq} for q = ½, p = 2: the order where products of two pole terms start (§1.3), and
  n^{−3−pq}, one order beyond the natural-index term of the q = ½ pole. W does not claim it. But W's own Lommel anchor (§2.2) has
  the same pole structure and **no** such term (W reproduces the exact n⁻⁴ coefficient), so the term cannot be a function of the
  residue R_{1/2} alone. That was the mismatch; the probes below resolve it (the term is first order in R_{1/2} and carries a
  factor 1 − 4ν² that vanishes for Lommel, where ν = −½).
- *Probe 1* (`w_probe.py/.out`, exploratory, designed after the failure; p = 2, s = 3, α = 0):
  - H2 = (k + ½)² (Hurwitz δ = +½, no poles): n⁻¹…n⁻⁴ all pass (n⁻⁴: fit 10.629177 vs W 10.629173, 3·10⁻⁶). **Not a δ > 0
    (phantom-node) effect.**
  - K2p = k² + ¼, K2m = k² − ¼ (moved Weyl pole q = ½, R = ∓1/16; density tilt (1 − κx)^{−1/2} as a Toda time): n⁻¹…n⁻³ pass
    (≤ 1.6·10⁻⁷), and n⁻⁴ misses by **−0.23131 and +0.23131**: odd in κ, so **first order** in the pole, not second order.
    The κ-even part (y(K2p) + y(K2m))/2 − y(k²) has no n⁻⁴ term (−1·10⁻⁶ ± 3·10⁻⁴).
  - So the missing term is the next order, n^{−3−pq}, of the q = ½ pole, with coefficient −0.2313/R_{1/2}·R = (3π²/8)R at p = 2,
    α = 0, the same for M1 (R = +1/16, β = 1) and K2m (R = +1/16, β = 0): independent of β.
- *Identification (post hoc; no fitted constant).* This is W′ (§1.3): the continued dressing g(w) of JZC_M4 §6 has a pole at w = ½,
  and cot(πw)g(w) → −π·Res g = −π·(−(p+2)²(p+4)(1−4ν²)/(256p)). At p = 2, ν = 0 the term is (3π²/8)R_{1/2} = ∓0.2313188 for
  R = ∓1/16: K2p fit −0.2313059 (Δ = 1.3·10⁻⁵, half-range 7·10⁻⁴), sphere fit (n⁻⁴ coefficient) 7.7762408 against W′ 7.7762407
  (Δ = 2·10⁻⁸). At ν = −½ (Bessel P = 2, α = −½) the residue vanishes, so W′ = W there, consistent with the exact Lommel form.
- *Probe 2* (`w_probe2.py/.out`, **pre-registered**: predictions saved 09:04:12 before the two measures were generated):
  K2p at s = 2 (α = −½: W′ predicts no extra term) and at s = 3.5 (α = ¼: W′ predicts an extra −0.1734891 = (3π²/8)(1 − ¼)R).

  | measure | n⁻³: fit / W′ | n⁻⁴: fit (half-range) | W′ | W (unrefined) |
  |---|---|---|---|---|
  | k² + ¼, s = 2 | −0.6501377 / −0.6501377 | +0.6994095 (1.6·10⁻³) | +0.6993909 (Δ 1.9·10⁻⁵) | same (W′ = W at α = −½) |
  | k² + ¼, s = 3.5 | −1.9860749 / −1.9860752 | +2.9296226 (3.6·10⁻³) | **+2.9296023 (Δ 2.0·10⁻⁵)** | +3.1030915 (off by 16 tol) |

  Both pass; the (1 − 4ν²) dependence is confirmed at two new values of ν. **Status: the M1 failure is resolved by W′; W′ is a
  CONJECTURE with one pre-registered confirmation, and its general-q part (q ≠ ½, where g(q) is an ordinary relative N⁻² dressing)
  is untested.**

## 3. Rule A log

1. *Circularity (Rule X).* The predictions were written (08:09:00) before any of the nine measures existed (08:24–08:50), and
   w_test asserts the mtimes. W has no fitted constant: β, the Toda times, the residues, the tilts are spectral data; the engine
   is the order-k Riemann–Hilbert computation of JZC_M4. The probe of §2.4 was designed after the M1 failure and is labelled so.
2. *Is each piece tested independently?* Yes, by the alternatives: the Szegő shift (β = α misses by 10³–10⁵ tol in every case
   with Z(0) ≠ −½), the pole terms (27–31968 tol), the Toda/zeta times (36–1912 tol), the density tilt (16–5529 tol), the mass
   tilt (141–21830 tol), the natural-index shift of the pole and tilt terms (20–1466 tol). The weakest is p = 0.6 (27–83 tol).
3. *Could the n⁻³ agreement at q₁ = 4/3 (A15m, A15p) be luck?* The medians agree to 2·10⁻⁶ and 3·10⁻⁵ while the half-ranges are
   10⁻³; the fit-free S_n decays (A15m: 1.0·10⁻², 7·10⁻³, 5·10⁻³, 3.6·10⁻³). Consistent, not precise; the precise q₁ < 1 tests are
   A3 and B0_3 (10⁻⁷).
4. *δ > 0.* A15p (δ = 0.4) and M1 (δ = ½) lie outside Theorem H's −1 < δ ≤ 0. Both pass every claimed coefficient (A15p to n^{−3.5},
   M1 to n⁻³), as the earlier Hurwitz data at δ = ½, 1 did. The probe's H2 = (k + ½)² checks n⁻⁴ at δ = ½ separately.
5. *Degenerate parameters.* a = 0 (lattice) and Hurwitz are the special cases of §1.4 (reduction is algebra). Resonance: j = 5
   at p = 0.6 and j = 2 for Bessel P = 1.5 are excluded by (W5), with log columns in the fits.
6. *Sign conventions.* The fractional-time response −(pρW(ρ)/2)t_ρ has the sign of the integer case (ε_j = −(pjW(j)/2)t_j);
   the M2 mass tilt (B = +½ at ρ = ⅔) is predicted at −¼ and measured at −0.2499997; the flipped sign would be off by 0.5.
7. *Tails.* The continuum tail is the pure power beyond 160 000 atoms; it drops the index corrections there. SPEC §3.11(b) showed
   the pole term converges as the corrected range grows; the agreement to 10⁻⁷–10⁻¹⁰ at n⁻² (A3, B0_3) bounds this effect at
   that level for these runs (NUMERICAL, not a bound).
8. *Noise floor.* y_n carries ≈ 10⁻¹⁵ white noise from the float64 atoms (w_resid.out prints σ_y from 6th differences) and a
   larger, correlated wander beyond n ≈ 1200 (n^{3.5}-scaled residuals wander by ±5·10⁻³ for n ∈ [1400, 1600] in A15m and B0_15,
   i.e. ≈ 3·10⁻¹⁴ in y; JZC_M4 §3 saw the same at the N⁻³/N⁻⁴ scale). This explains the two "no decay" flags of w_resid at
   n^{−3.5}: those residuals decay through n = 1200 (A15m: −6.9·10⁻⁴, −6.3·10⁻⁴, −3.0·10⁻⁴ at n = 800, 1000, 1200). The third flag
   (M1 n⁻⁴) is the real term of §2.4.
9. *W′ is post hoc.* It was identified after the M1 failure from K2p/K2m/M1 and the Lommel zero; the formula is JZC_M4 §6's closed
   form with no adjustable constant, but its choice (continue g in the index; take the symmetric 0·∞ limit) was made knowing the
   target. Evidence for it is probe 2 only: the α = ¼ measure discriminates (W off by 16 tol; W′ off by Δ = 2·10⁻⁵ against a half-range 3.6·10⁻³); the α = −½ measure tests only the predicted zero. The sign and size at α = 0 were fixed by data
   before the formula was written down (an mpmath.limit evaluation first gave −0.2107; the symmetric-average value −0.2313 is the
   correct limit of the same expression, checked to 30 digits against 3π²/128). Rule A on W′ itself: at ν = ±½ it vanishes for
   every p (algebra, sympy), at other half-integers g has no pole, so the bouncer (q = 3/2, 9/2) and Robin's q = 3/2 are unaffected,
   and Robin's q = ½ (the hk^{−1/3} correction, p = 2/3) sits at n^{−10/3} with factor 1 − 4ν², where ν = α = ½ at SPEC §3.13's
   s = 2: it vanishes there as well (at other s it would not).

## 4. What is new relative to SPEC and JZC_M4

- **One statement instead of four.** SPEC's S1/S1′/S1″/S1⁗, the κ law, rule H, JZC_M4's S1-N/S1-N′/Theorem T and Theorem H become
  one conjecture with three ingredients: the Szegő-shifted model M(α − 2Z(0) − 1, α), a Toda flow with integer and fractional times
  t_ρ, and the π cot pole terms, all at N = n + α/2 − Z(0).
- **Fractional Toda times.** The S1⁗ Jacobian term, the multiplicity weight and the zeta layer are one object: a band tilt
  exp(Σt_ρx^ρ), with the single first-order response −(pρW(ρ)/2)t_ρ (integer ρ: E3.7 / Theorem T; non-integer: SPEC §3.15's
  branched E3.7, now tested at ρ = ⅔, 4/3 on four further spectra).
- **The natural index for pole terms with Z(0) ≠ −½** (A15p, A3, B*, M2): S1⁗'s shift (s − 1)/(2p) generalises to α/2 − Z(0).
- **Multiplicities** (finding 1), with the sphere-like and multiplicity-lattice tests.
- **Bessel exactness from spectral data** (Obs W.3): the Lommel closed form is W with all Toda times zero; SPEC's "cancellation"
  at n⁻³ is t₁ = 0.
- **W′: the dressing of pole terms** and its 0·∞ value at q = ½, a term on half-integer poles that SPEC's "cot = 0" reading misses
  one order further down (it answers part of SPEC §3.12's open "subleading pole terms" for half-integer q, e.g. the Robin and bouncer
  cases, where q = ½, 3/2 occur; only q = ½ has the pole of g). Every earlier real-operator test with a q = ½ pole happened to sit
  at ν = α = ±½ (bouncer and Robin at p = 2/3, s = 2: α = ½; Bessel at p = s = 2: α = −½), where the factor 1 − 4ν² vanishes; the
  sphere (α = 0) is the first case where the term shows.
- **Not new:** the pieces (SPEC, JZC_M4, Theorem H). Novelty of the combination: UNCHECKED (Rule L not run for this note).
- **Proof status after this note** (updated 2026-10-22 after Rule R review A of the W chain, research/G1/review/REVIEW_JZC_W_kappa_chain_A.md): for the κ-family (λ_k = (k + δ)^p + κ, p > 1, |α| < 1) W is PROVED-mod-cite + REVIEWED at
  first order in the poles, remainder O(n^{−2p}) with the continued pole dressing and O(n^{−1−p}) in W's displayed form (§1.5; one input,
  JZC_W_exact WE.1, NOT REVIEWED). §5.1 items 1 and 4 are thereby settled for this family (item 1 in the corrected form of JZC_W_outer
  Remark 3.6: the invariant is the gauge exponent at the hard edge, not the exponent at ∞; item 4 for coherent branched tilts, JZC_W_kappa
  Prop K.12′). Still open: second order in the poles, p < 1 (§5.1 item 3, OBSTRUCTION for the lattice-g route), p = 1/m, α ∉ (−1, 1),
  non-coherent branched tilts ((F-br)), general node sets, p = 1, and novelty (UNCHECKED).

## 5. The main obstacles to a proof

### 5.1 p ≠ 1: the general outer scalar (the α-frame of Theorem H as template)

Theorem H proves W for Hurwitz lattices by four moves: interpolate with sin π(t − δ) and 1/Γ(t − δ) (H-a); build the outer scalar
F_δ = D_δB_δK and show F_δ ~ C_δ(−z)^δ at ∞ (H-b, G12 C1.5); absorb (−z)^δ as the Szegő shift β′ = α + 2δ at fixed Bessel order α
(H-d, the α-frame: the lip phases e^{±2πiδ} restore c_± = e^{∓iπα}); and run N.6 for M(β′, α) (G1u, Hc). For a general Weyl-type
node set the template is the same, and the missing pieces are:
1. **The general outer scalar.** Replace 1/Γ(t − δ) by an entire function of the index variable with zeros exactly at the
   nodes, i.e. the (Weyl-subtracted) zeta-regularised determinant of Λ composed with an analytic index map t_κ(z) (JZC_M3_scope
   hypothesis (A); SPEC §3.7 (P1)–(P4)). What W needs from it is **its power at z = ∞ (t → 0)**: the exponent must be
   −Z(0) − ½ (Hurwitz: δ = −Z(0) − ½), so that the α-frame gauge (−z)^{−(Z(0)+½)σ₃} produces β = α − 2Z(0) − 1. HEURISTIC reason:
   the large-x expansion of log det_ζ(1 + x/Λ) has the log x coefficient −Z(0) (Voros-type, NOT QUOTED), independent of the low
   nodes; the Hurwitz case is LnΓ's (½ − a)ln. This must be proved with sectorial bounds (Paper 2 (O1)–(O5)), which for a
   non-lattice node set is the content of hypothesis (A).
2. **The band factor with Z(−j).** The Binet-cut (p > 1) / seam (p < 1) moments must come out as Z(−j)/(jn^{jp}) (JZC_M3_scope
   "Lemma AP", a rotated Abel–Plana formula). For Hurwitz this is the Fourier-sum computation (JZC_M3a_H §3.2).
3. **The n-dependent equilibrium** (G1: JZC_M1 Theorem Q for σ_n): this is where the π cot pole terms come from (SPEC Prop E,
   JZC_M1 Prop M1.2). Its global sign conditions on the saturated region are new.
4. **E3.7 for branched tilts** z^ρ, ρ ∉ ℕ (the fractional Toda times): only observed (SPEC §3.15 and §2 here), not proved. It is a
   hard-edge computation: the tilt is not analytic at z = 0, so N.6b's meromorphy argument does not apply as it stands.
Items 1 and 4 are the genuinely new analysis; 2 and 3 have worked templates. Theorem H's α-frame (Bessel order fixed, Szegő
exponent free, G1u's n-uniform comparison valid for every real β′) is exactly what item 1 needs downstream: once F_Λ ~ C(−z)^{−Z(0)−½}
is established, the rest of H-d and G1u transfer verbatim.

### 5.2 p = 1: 2-D drums

- **Frame.** Theorem N.6 excludes p = 1. E_p1 handles the lattice at p = 1 with its own Γ/Binet band factor; the order-k engine
  m4_rh4 and the natural-form algebra (denominators (2k+1)p + 2) have no p = 1 specialisation checked.
- **Resonance everywhere.** The zeta exponents 1 + j merge with the integer layer at every order, and the Weyl pole w = −1 is an
  integer, so the decomposition "integer layer + Toda times + pole terms" is not unique; generically log n terms appear
  (SPEC §3.13's resonance mechanism), and the Toda times t_j must be read as finite parts.
- **The perimeter pole q = −½ is the leading correction**, n^{+1/2} relative to the 1/n layer (W(q)π cot(πq) → −π(4c)^{−1/2}), so
  its second-order term (π²/16)β² lands at n⁻¹, the order of the corner term Z(0). A p = 1 statement must therefore include the
  continuum equilibrium to all orders in the perimeter (SPEC §3.16's exact solution of the soft-edge condition), not W's first
  order.
- **Counting fluctuations.** Real drums violate (W2): integrable drums have Poisson-like fluctuations whose noise
  (∝ n^{1/2} in n·y) exceeds the corner term (SPEC §3.16); degenerate drums need the multiplicity rule (§1.4 finding 1) with
  arithmetic node densities. W applies only to "smoothed drums".

### 5.3 Recommended next proof step

Prove the outer-scalar exponent (§5.1 item 1) for the simplest non-Hurwitz class with poles, **λ_k = (k + δ)^p + κ** (family K:
an exact Möbius image of the Hurwitz nodes, SPEC Prop M) or the analytically perturbed lattices of JZC_M3_scope M3b. There the
index map is explicit, Z(0) = −½ − δ is unchanged by κ, and the claim to prove is: F_Λ ~ C(−z)^δ at ∞ with δ-only exponent, so
that Theorem H's α-frame applies verbatim and W(i) reduces to N.6 for M(α + 2δ, α) plus the equilibrium (pole) and density-tilt
corrections. In parallel, settle E3.7 for branched tilts (§5.1 item 4) by the exact engine with a z^ρ term in the hard-edge
jump (the decoupled exact algebra of m3a_e37_decoupled is the template). The same engine run with a z^ρ tilt continued in ρ would
also test W′'s g(q) for q ≠ ½ without measures (the dressing of a tilt term is computable in the model, by Theorem N.6's
structure, once branched jumps are admitted).

## 6. Files

- `checks/w_common.py` (prediction assembly, measures, fits), `checks/w_spectra.py` (spectra and their Z data),
  `checks/w_predict.py` → `w_predict.out` (predictions; 37 internal checks), `checks/w_test.py` → `w_test.out` (fits vs W),
  `checks/w_resid.py` → `w_resid.out` (fit-free residuals), `checks/w_probe.py` → `w_probe.out` (§2.4 probe 1, exploratory),
  `checks/w_probe2.py` → `w_probe2.out` (§2.4 probe 2, pre-registered test of W′).
- Caches: `tmp/w_cache/` (measures `<tag>__<sha256>.txt`, model responses `model_*.json`, Bessel zeros, predictions.json).
