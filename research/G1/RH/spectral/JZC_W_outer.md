# JZC W, first proof step: the general outer scalar for λ_k = (k + δ)^p + κ (Conjecture W, §5.1 item 1)

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_W_kappa_chain_A.md; it covers this note, JZC_W_kappa.md and
JZC_W_BT.md); fix B4 (the corrections listed in JZC_W_kappa §9 item 5) applied here 2026-10-22.
Status (2026-10-22): **REVIEWED** (Rule R: independent second reader A re-derived the key steps and re-ran w_outer_index, w_outer_scalar
and w_outer_e2e (twice: fresh caches, then on the caches), all identical to the stored outputs; fixes applied) for **L W-out.0–5,
P W-out.3, P W-out.5, P W-out.7, Remark 3.6 and P W-out.6 (i)**. P W-out.6 (ii), (iii) are now proved in JZC_W_kappa (P K.12 + Prop K.12′,
P K.11); §7 stays an OBSTRUCTION (heuristic, sharpened by JZC_W_kappa P K.14). Labels per VERIFICATION_POLICY.md; REVIEWED is combined
with, and does not upgrade, the labels below. Novelty: UNCHECKED (no Rule L pass).
**Status of Conjecture W for σ^{δ,κ}** (p > 1, −1 < δ ≤ 0, κ ≠ 0, κ > −a^p, |α| < 1; review A §3; JZC_W_kappa header and P K.12): at first
order in the poles, n^pb_n/c = 𝔅_n[M(α + 2δ, α); t] + Σ_m(continued pole layer at j = q_m) + O(n^{−2p}), and in W's displayed form (pole term
× (1 + O(N^{−1}))) with remainder O(n^{−1−p}): **PROVED-mod-cite + REVIEWED**, with one unreviewed input (JZC_W_exact WE.1, elementary).
Not covered: second order in the poles; p < 1 (OBSTRUCTION for this route); p = 1/m; α ∉ (−1, 1); non-coherent branched tilts ((F-br),
GAP, not needed here) (fixed per Rule R review A of the W chain, B4). No claim about RH: no measure built from zeta zeros is
used. Checks: `checks/w_outer_index.py/.out`, `checks/w_outer_scalar.py/.out`, `checks/w_outer_e2e.py/.out` (§8; caches in
`tmp/w_cache/`, gitignored). Everything attributed to Paper 2 is quoted from papers/paper2/{sec_5,sec_6}.tex as read for this note
(read-only); the H-chain notes (JZC_M3a_H_Ha, JZC_M3a_Hd, JZC_M3a_H_G12, JZC_M3a_H_Hc, JZC_M3a_H_G1u) are cited with their labels.

| # | Statement | Label |
|---|---|---|
| L W-out.0 | Z(0) = −½ − δ for every κ > −a^p when p > 1, and when p < 1 with 1/p ∉ ℕ; for p = 1/m: Z(0) = −½ − δ + (−κ)^m. Poles of w ↦ Z(−w) at q_m = m − 1/p, R_{q_m} = −binom(q_m, m)κ^m/p | PROVED (elementary) + NUMERICAL + REVIEWED |
| L W-out.1 | the index map is a Möbius change of variable: t_κ = t∘ζ, ζ(z) = z/(1 − κz/n^p); zeros of 1 − e^{2iθ_κ} off its cut are exactly the κ-nodes (p > 1) | PROVED (elementary) + REVIEWED |
| L W-out.2 | H-a for σ^{δ,κ}: W_κ = 𝗐_n z^α r_n, r_n := (1 − κz/n^p)^{1/p − 1}; residues = masses; top node X₁ = n^p/(a^p + κ); P Ha.5 verbatim | PROVED-mod-cite (JZC_M3a_H_Ha L Ha.2–P Ha.5, REVIEWED) + REVIEWED |
| L W-out.3 | the unnormalised scalar F_κ := Φ_δ∘ζ·K (Φ_δ = Hurwitz F_δ/K): jumps; F_κ/F_δ → 1 at the hard edge; \|F_κ\| ≍ \|z − z_*\|^{−δ−½} at z_* := n^p/κ; **F_κ ~ C(−z)^{−½} at z = ∞, not C(−z)^{−Z(0)−½}** | PROVED-mod-cite (G12 C1.5, P1.4 [REVIEWED]) + REVIEWED |
| **P W-out.3** | the gauge G_κ = (−z)^{−δ}E_κ, E_κ = exp 𝒞[ρ₁] (ρ₁ = minus the index offset): F♮_κ := F_κG_κ satisfies (O1) with the lattice θ, is bounded above and below at z_*, and **F♮_κ → C_κ ≠ 0 uniformly at ∞**; at the hard edge **G_κ = (−z)^{−δ}E_κ(0)(1 + O(n^{1−p}\|z\|^{1−1/p}))**: the outer exponent −Z(0) − ½ = δ sits at the hard edge, κ-free | PROVED-mod-cite (G12 C1.5; Paper 2 L normalisation) + REVIEWED |
| L W-out.4 | H-d for σ^{δ,κ}: the jumps are those of M(β′ = α + 2δ, ν = α) with band weight W₀^κ = 𝗐_n z^{β′}(4c − z)H_n^κ, except the factor e^{±2πiρ₁(z)} in the (2,1) entries of lips, Σ^△, top segment | PROVED (algebra, as JZC_M3a_Hd (ii)) + NUMERICAL + REVIEWED |
| L W-out.5 | PV lemma: ∫_0^L y^q dy/(y − z) = −π(−z)^q/sin(πq) + Σ_{j≥0} z^jL^{q−j}/(q − j) | PROVED (elementary) + NUMERICAL + REVIEWED |
| **P W-out.5** | structure of H_n^κ: log H_n^κ = (Hurwitz G_δ∘ζ) + log r_n − 2Ψ₀; the integer-power part gives **exactly W's Toda parameters μ_j = 2Z_κ(−j)/j − B_j** (the gauge supplies κ^jζ(0, a)), the branched part is the tilt Σ_m 2π cot(πq_m)a_m(z/n^p)^{q_m}, a_m = −R_{q_m}/q_m | PROVED-mod-cite (Hc.2; DLMF 5.12.1, 5.5.3 for κ < 0) — with ζ(−mp, a) in place of the Fourier sums by JZC_M3a_H Remark 3.3 (PROVED-mod-cite (CITATIONS (Hurwitz-DK)); NUMERICAL support) (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)); + REVIEWED |
| P W-out.7 | the first-order fractional-time response of W applied to that tilt is **exactly W's pole term** pR_qW(q)π cot(πq)(n/N)^pN^{−1−pq} | PROVED (algebra) + REVIEWED |
| **P W-out.6** | reduction: (i) the κ-problem is exactly the decoupled model M(α + 2δ, α) with band factor H_n^κ and the lip factor e^{±2πiρ₁}; (ii) Conjecture W holds for σ^{δ,κ} at first order in the poles (remainder O(n^{−2p}) with the continued pole dressing; O(n^{−1−p}) in W's displayed form); (iii) the n^{−k} coefficients, k < p, are those of M(α + 2δ, α) (κ-free) | (i) PROVED-mod-cite + REVIEWED; (ii) PROVED-mod-cite (W_kappa P K.12 + K.12′) + REVIEWED (input WE.1 NOT REVIEWED); (iii) PROVED-mod-cite (W_kappa P K.11) + REVIEWED; formerly CONDITIONAL (BT, BT₀) (fixed per Rule R review A of the W chain, B4) |
| Remark 3.6 | the literal reading of JZC_W §5.1 item 1 ("F_Λ ∼ C(−z)^{−Z(0)−½} at ∞") is false for κ ≠ 0 at fixed n; the exponent at z = ∞ of an unnormalised scalar is construction-dependent; the invariant is the exponent of the normalising gauge at the hard edge | PROVED (by L W-out.3) + NUMERICAL (exponent −½, not δ) + REVIEWED |
| §7 | p < 1: the gauge density is unbounded at the hard edge (ρ₁ ∼ n^{1−p}x^{1−1/p}, 1 − 1/p < 0) and O(n^{1−p}) ≫ 1 on the band: the lattice g cannot carry it | OBSTRUCTION (heuristic, for this route); sharpened by JZC_W_kappa P K.14 (exponent e(p) = (1 − p)(2 + p)/p on the Bessel scale) (fixed per Rule R review A of the W chain, B4) |
| §8 | 104 + 125 + 44 assertions incl. controls that must fail; end-to-end: d₁, d₂ of M(α + 2δ, α) to 10⁻¹⁰, 5·10⁻⁸ at κ = ±0.3; the n^{−p} pole term to 4·10⁻⁷ | NUMERICAL |

## 0. Setting, hypotheses, what is reused

**Setting (S).** p > 1 (p < 1 in §7 only); −1 < δ ≤ 0, a := 1 + δ ∈ (0, 1]; κ ∈ ℝ, κ ≠ 0, **κ > −a^p** (then λ_k := (k + δ)^p + κ > 0 and
strictly increasing in k ≥ 1, so the nodes are positive and ordered; κ = 0 is Theorem H); 1 < s < 1 + 2p, α := (s − 1 − p)/p ∈ (−1, 1);
β′ := α + 2δ; σ^{δ,κ} := Σ_{k≥1}λ_k^{−s/p}δ_{1/λ_k} (masses λ^{−s/p}, i.e. v ≡ 1 in JZC_W (W3)); n ≥ n₀(p, δ, κ). Scaled nodes X_k :=
n^p/λ_k; top node **X₁ = n^p/(a^p + κ)**. z_* := n^p/κ (on (X₁, ∞) for κ > 0, on (−∞, 0) for κ < 0); z′ := |z_*|; t_∞ := |κ|^{1/p}.

**Lattice and Hurwitz objects (reused).** t(z) = nz^{−1/p} (principal), θ = πt, lattice g, φ, φ̃ (Paper 2 (eq:t), (eq:theta),
Lemma gfunction (i): "g₊ − g₋ = 2iθ/n on (4c, ∞), φ₊ + φ₋ = 0 on (0, 4c)", as quoted in JZC_M3a_Hd §1). From JZC_M3a_H_G12 §1 (REVIEWED):
j_δ, D̃_δ = e^{−j_δ(t)}, κ_δ± = 1/(1 − e^{∓2iθ_δ}), θ_δ = π(t − δ), B_δ, and F_δ = κ_δD̃_δB_δK, K = (4c − z)^{−1/2}. Put
**Φ_δ := F_δ/K = κ_δD̃_δB_δ** (analytic, zero-free on ℂ∖[0, ∞); D̃_δB_δ extends analytically across (−∞, 0): P1.4(a)) and
G_δ := −j_δ(t) + log B_δ, so (D̃_δB_δ)^{−2} = e^{−2G_δ} = H_n^δ (Hc §0).
- G12 **C1.5** (quoted): "F♮ := F_δ(−z)^{−δ} … F♮(z) → C_δ := 1/ϰ_∞♮(∞) uniformly as z → ∞ (boundary values on ℝ included); i.e.
  F_δ(z) = C_δ(−z)^δ(1 + o(1)). Moreover C_δ = e^{L_δ} > 0."
- Hc **Lemma Hc.2(ii)** (quoted): "G_δ(z) − G_δ(1) = Σ_{k≤K}m_k(δ)(z^k − 1) + O(n^{−(K+1)p}) on |z| ≤ 4c + 2, boundary values included, with
  derivative bounds; C = C(p, K) independent of δ", m_k(δ) the Fourier sums of JZC_M3a_H §3.2; = ζ(−kp, a)/(kn^{kp}) by Remark 3.3
  (PROVED-mod-cite (CITATIONS (Hurwitz-DK)); NUMERICAL support; a = 1 + δ ∈ (0, 1] as Dixit–Kumar Thm 1.1 requires) (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)).
- Paper 2 **(O1)–(O5)** (sec_5 §frame-outer, quoted): "(O1) F is analytic and zero-free in ℂ∖[0,∞) (in particular, it has no jump on
  (−∞,0)), it has continuous boundary values on (0,∞)∖{X_k}, and F₊ = F₋e^{2iθ} on (4c,∞)∖{X_k}. … (O5) (For each fixed n.) |F|^{±1} is
  bounded on U(0,δ)∖(Ω̄_b ∪ [0,∞)), and F̃^{±1} is bounded on U(0,δ) ∩ Ω_b. There is N_n with |F(z)|^{±1} ≤ C_n|z|^{N_n} for
  |z| ≥ n^p+δ′, z ∉ ℝ, and F(iy) is bounded and bounded away from 0 as y → ±∞." (O3) is quoted below; (O2) fails here as in the Hurwitz case and is replaced by L W-out.4 (as in JZC_M3a_Hd (ii)); (O4) is not used.
- Paper 2 **Lemma normalisation** (sec_6, quoted): "Let ϰ_∞(z) := F(z)^{−1}e^{n(g(z)−Log z)} for |z| > n^p+δ′, z ∉ ℝ. Then ϰ_∞ extends to an
  analytic function on {|z| > n^p+δ′} ∪ {∞} with ϰ_∞(∞) ≠ 0." Its proof uses only (O1) on (n^p+δ′, ∞), no jump of F on (−∞, −n^p−δ′),
  the polynomial bound and the limit along iy of (O5), and Lemma gfunction. For σ^{δ,κ}, n^p + δ′ becomes X₁ + δ′ (as in H-a).
- Paper 2 **Lemma jumpsV** (sec_5, quoted): "(a) on the band (0,4c): v_V = [[0, W₀], [−1/W₀, 0]]; (b) on Σ^±_lip …
  [[1,0],[e^{2nφ}/W₀,1]] + [[ι_±(κ_±−1), W₀e^{−2nφ̃}], [(κ_±−1)e^{2nφ}/W₀, ι_∓(κ_±−1)]]; (c) on Σ_v^±: [[1, −W₀e^{−2nφ̃}], [0,1]]; (d) on the
  saturated segment (4c, n^p+δ′): [[1,0],[e^{2nφ̃}/W₀,1]]; (e) on Σ^{△±}: [[1,0],[κ_±e^{2nφ}/W₀,1]]; (f) on Σ_top ∩ ℂ_±: [[1,0],[∓κ_±e^{2nφ}/W₀,1]];
  (g) there is no jump on (−∞,0) or on (n^p+δ′,∞)", proved from "(eq:identities) e^{∓2iθ}e^{−2nφ} = e^{−2nφ̃}, F = κ_±F̃, W/F̃² = W₀ in ℂ_±"
  and, in (d), "the diagonal becomes (e^{n(φ₊−φ₋)}F₊/F₋)^{σ₃} = (e^{−2iθ}e^{2iθ})^{σ₃} = I by Lemma gfunction (i) and (O1)". Paper 2 **(O3)**:
  "For z ∈ 𝒵_n with |z| ≤ 1: |log H_n(z) − log H_n(0⁺)| ≤ C|z|^{ν_p} and |(log H_n)′(z)| ≤ C|z|^{ν_p−1}", ν_p := min(1/p, ½). And **(eq:VM)**: "V = C_∞e^{−nγ_pσ₃}UM, M := e^{nφσ₃}F^{σ₃} in Ω_∞, L_±e^{nφσ₃}A_±F̃^{σ₃}
  in Ω_b^±, A^△_±e^{nφσ₃}F^{σ₃} in Ω_sat±." Paper 2 **Lemma lips (c)**: the lips avoid U(4c, h₀) (as quoted in JZC_M3a_Hd §1).
- External (Rule C): only **(DLMF-2)** of RH/CITATIONS.md, read 2026-10-14: "(5.5.3) Γ(z)Γ(1−z) = π/sin(πz), z ≠ 0, ±1, …";
  "(5.12.1) B(a,b) = ∫₀¹t^{a−1}(1−t)^{b−1}dt = Γ(a)Γ(b)/Γ(a+b)"; "(5.12.3) ∫₀^∞ t^{a−1}/(1+t)^{a+b} dt = B(a,b)"; "In (5.12.1)–(5.12.4) it
  is assumed ℜa > 0 and ℜb > 0." Used only in P W-out.5 for κ < 0, with the hypotheses checked there (one use is by analytic
  continuation in a, stated as such). Hurwitz zeta facts are proved below (L W-out.0), not cited.

## 1. Spectral data (Lemma W-out.0)

**Lemma W-out.0.** Let Z(w) := Σ_kλ_k^{−w} (Re w > 1/p), λ_k = (k + δ)^p + κ, κ > −a^p, p > 0.
(a) Z extends meromorphically to ℂ. Its poles are at w = 1/p − m (m ≥ 0) only; in the variable w ↦ Z(−w) the non-Weyl poles are
  q_m := m − 1/p (m ≥ 1) with w-residues **R_{q_m} = −binom(q_m, m)κ^m/p** (those with q_m ∈ {0, …, m − 1} vanish).
(b) **Z(0) = −½ − δ** if 1/p ∉ ℕ (in particular for every p > 1); **Z(0) = −½ − δ + (−κ)^m** if p = 1/m, m ∈ ℕ.
(c) Z(−j) = Σ_{i=0}^{j}binom(j, i)κ^iζ(−p(j − i), a) (j ∈ ℕ; 1/p ∉ ℕ).

*Proof.* Hurwitz zeta, self-contained. For b > 0, Re s > 1, f(x) := (x + b)^{−s}: on each [k, k + 1], ∫P₁f′ = ½f(k) + ½f(k + 1) − ∫f
(integration by parts, P₁(x) := {x} − ½), so Σ_{k≥0}f(k) = ∫_0^∞f + ½f(0) + ∫_0^∞P₁f′. Integrating by parts once more with the periodic,
bounded antiderivative P₂ of P₁ (P₂(x) := ({x}² − {x} + ⅙)/2, P₂(0) = 1/12):
  ζ(s, b) = b^{1−s}/(s − 1) + ½b^{−s} + s[P₂(0)b^{−s−1} − (s + 1)∫_0^∞P₂(x)(x + b)^{−s−2}dx].   (1.1)
The bracket is analytic on Re s > −1, so ζ(s, b) is meromorphic there with a single simple pole at s = 1, residue 1, and
**ζ(0, b) = ½ − b** (the s-term vanishes at s = 0). Iterating the integration by parts continues ζ(·, b) to ℂ with no other pole. Also
ζ(s, b) = Σ_{k<K₀}(k + b)^{−s} + ζ(s, b + K₀) (for Re s > 1, hence everywhere). Choose K₀ ≥ 0 with |κ| < (K₀ + a)^p and put b := K₀ + a. For k > K₀,
λ_k^{−w} = (k + δ)^{−pw}(1 + κ(k + δ)^{−p})^{−w} = Σ_i binom(−w, i)κ^i(k + δ)^{−p(w+i)}, and Σ_{k>K₀}Σ_i|…| converges for Re w > 1/p
(|κ|/b^p < 1). Hence
  Z(w) = Σ_{k≤K₀}λ_k^{−w} + Σ_{i≥0}binom(−w, i)κ^iζ(p(w + i), b).   (1.2)
The i-th term is meromorphic with at most a simple pole at w = 1/p − i; the tail Σ_{i>I} converges uniformly on compact w-sets
(ζ(p(w+i), b) = O(b^{−p(Re w + i)}) once p(Re w + i) ≥ 2, and |binom(−w, i)| grows polynomially), so (1.2) is the continuation.
(a): Res_{w=1/p−i} = binom(−w, i)κ^i/p at w = 1/p − i; with w = −q (q = i − 1/p) the residue of q ↦ Z(−q) is −binom(q, i)κ^i/p.
(b): at w = 0 the head gives K₀, the i = 0 term gives ζ(0, b) = ½ − K₀ − a, so these give ½ − a = −½ − δ. For i ≥ 1, binom(−w, i) has a
simple zero at w = 0 (binom(−w, i) = (−1)^iw/i + O(w²)); the product vanishes unless ζ(p(w + i), b) has its pole at w = 0, i.e. pi = 1. That
happens iff 1/p = m ∈ ℕ, with ζ(1 + pw, b) = 1/(pw) + O(1), giving (−1)^mκ^m/(mp) = (−κ)^m. (c): at w = −j, binom(j, i) = 0 for i > j, and
no ζ(−p(j − i), b) is at its pole (−p(j − i) ≤ 0); so Z(−j) = Σ_{k≤K₀}λ_k^j + Σ_{i≤j}binom(j, i)κ^iζ(−p(j − i), b). Expanding λ_k^j binomially
and using ζ(s, a) = Σ_{k<K₀}(k + a)^{−s} + ζ(s, b) gives the stated sum. ∎ (PROVED, elementary. NUMERICAL: w_outer_index [Z0], 9 cases incl. κ = 2, 5 ≥ a^p (K₀ = 3, 4),
p = 0.6, and p = ½, ⅓ with the (−κ)^m term; the κ-free value fails at p = 1/m as required.)

So for p > 1, **β′ = α − 2Z(0) − 1 = α + 2δ, independent of κ** (JZC_W §5.3). The pole q₁ = 1 − 1/p is the "moved Weyl pole" of the κ law
(R_{q₁} = −κq₁/p, SPEC §3.5).

## 2. Index map and interpolation (H-a)

**Lemma W-out.1 (Möbius index map).** Let ζ(z) := z/(1 − z/z_*) = z/(1 − κz/n^p) and t_κ := t∘ζ, θ_κ := π(t_κ − δ) = θ_δ∘ζ,
κ_κ± := κ_δ±∘ζ.
(a) ζ is the real Möbius map with matrix [[1, 0], [−1/z_*, 1]] (det 1): it maps ℂ_± onto ℂ_±, ℝ ∪ {∞} onto itself, ζ(0) = 0, ζ′(0) = 1,
  ζ(z_*) = ∞, ζ(∞) = −z_*. On ℂ∖Γ_κ, Γ_κ := ζ^{−1}((−∞, 0]) = (−∞, 0] ∪ [z_*, ∞) (κ > 0), [−z′, 0] (κ < 0), t_κ is analytic and
  **t_κ(z) = (n^p/z − κ)^{1/p}** (principal).
(b) t_κ(X_k) = k + δ; ζ(X_k) = Ξ_k := (n/(k + δ))^p (the Hurwitz nodes).
(c) (p > 1) In ℂ∖Γ_κ the zeros of 1 − e^{2iθ_κ} are exactly the X_k, all simple; κ_κ± is analytic in ℂ_± with |e^{∓2iθ_κ}| < 1.
*Proof.* (a) ζ^{−1} = w ↦ w/(1 + w/z_*); a real Möbius map of positive determinant preserves ℂ_±. 1/ζ = 1/z − κ/n^p, so
nζ^{−1/p} = n(1/ζ)^{1/p} = (n^p/z − κ)^{1/p} for ζ ∉ (−∞, 0] (principal powers). The preimage of (−∞, 0] is read off from
ζ(x) = x/(1 − x/z_*). (b) λ_k = n^p/X_k, so n^p/X_k − κ = (k + δ)^p. (c) By (a), z ∉ Γ_κ ⇒ ζ ∉ (−∞, 0], so arg t_κ = −arg ζ/p ∈
(−π/p, π/p) ⊂ (−π, π): t_κ ∉ (−∞, 0]. A zero needs t_κ − δ ∈ ℤ, so t_κ > 0 real, ζ > 0, and t_κ = k + δ with k ≥ 1 (t_κ > 0 ≥ δ). For
κ < 0, the part ζ ∈ (z′, ∞) of the positive ζ-axis is the image of (−∞, −z′), where t_κ ∈ (0, t_∞) and t_∞ < a: no zeros. So
z = ζ^{−1}(Ξ_k) = X_k. Simplicity: d/dz e^{2iθ_κ} = 2iθ_κ′e^{2iθ_κ}, θ_κ′(X_k) = θ_δ′(Ξ_k)ζ′(X_k) ≠ 0. The last claim is L Ha.4(b) for θ_δ at ζ(z) ∈ ℂ_±. ∎
(PROVED. NUMERICAL: w_outer_index [I1], [I3]: argument principle counts 4 zeros = 4 κ-nodes in {r₁ < |z| < r₂, |arg z| < 0.95π}, 5 cases.)

**Lemma W-out.2 (H-a for σ^{δ,κ}).** Let w(z) := n^pt(z)^{−s} (lattice weight, unchanged: w(X_k) = n^pλ_k^{−s/p} since t(X_k)^p = λ_k), and
  **W_κ := 2iθ_κ′w = 𝗐_nz^αr_n(z),  r_n(z) := (1 − z/z_*)^{1/p − 1}**   (𝗐_n = −(2πi/p)n^{1+p−s}, Paper 2 Lemma bandweight).
(a) L Ha.2 holds with x₁ = 1/(a^p + κ), X₁ = n^p/(a^p + κ): Uz^{−nσ₃} = I + O(1/z) for |z| > X₁, (eq:extractU) gives b_n, a_n of σ^{δ,κ}.
(b) Res_{X_k}W_κ/(e^{2iθ_κ} − 1) = w(X_k) = n^pλ_k^{−s/p}; no other poles in 𝒵_n.
(c) P Ha.5 (pole removal ⇔ residue conditions) holds verbatim with κ_κ, L^κ_±, A^{△κ}_±; contour: top segment at X₁ + δ′, and
  𝒵_n := {0 < |z| < ρ_κn^p, |arg z| < ϑ_w} with ρ_κ ∈ (1/(a^p + κ), 1/κ) for κ > 0 (so z_* ∉ 𝒵̄_n and r_n is analytic on 𝒵_n), any
  ρ_κ > 1/(a^p + κ) for κ < 0 (r_n's cut (−∞, −z′] lies outside the sector).
*Proof.* θ_κ′ = θ_δ′(ζ)ζ′ = −(π/p)t_κζ/z², while θ′ = −(π/p)t/z; so W_κ/W = (t_κ/t)(ζ/z) = (1 − z/z_*)^{1/p}(1 − z/z_*)^{−1}, using
(t_κ/t)^p = 1 − z/z_* and positivity on (0, X₁] for the branch. (a) is L Ha.2's proof with x_k ∈ (0, x₁]. (b): W_κ/(2iθ_κ′) = w at the
simple zeros of L W-out.1(c). (c): P Ha.5's proof uses only (b) and L W-out.1(c). ∎ (PROVED-mod-cite: JZC_M3a_H_Ha (REVIEWED).
NUMERICAL: [I2], 15 residues to 10⁻²⁵ relative; controls: without r_n the residues are wrong, and the uncomposed phase π(t − δ) has
no pole at X_k — both fail as required.)

The density factor r_n is W's D(x) = (1 − κx)^{1/p − 1} (JZC_W Prop W.1, −pR_{q₁} = q₁κ) in the scaled variable: integer powers of x only.

## 3. The outer scalar and its normalisation (H-b)

**Definition.** F_κ(z) := Φ_δ(ζ(z))·K(z). Gauge density ρ₁ on (0, ∞) and, for κ < 0, ρ̃ on (−∞, −z′):
- κ > 0: ρ₁(y) := t(y) − t_κ(y) on (0, z_*);  ρ₁(y) := t(y) − δ − ½ on (z_*, ∞);
- κ < 0: ρ₁(y) := t(y) − t_κ(y) on (0, ∞);  ρ̃(y) := ½ + δ − t_κ(y) on (−∞, −z′) (there t_κ = (|κ| − n^p/|y|)^{1/p} ∈ (0, t_∞)).
𝒞[ρ](z) := ∫_0^∞ρ(y)[1/(y − z) − 1/(y + 1)]dy (+ ∫_{−∞}^{−z′}ρ̃(y)[1/(y − z) − 1/(y − 1)]dy for κ < 0); E_κ := e^{𝒞}; **G_κ := (−z)^{−δ}E_κ**;
**F♮_κ := F_κG_κ**, F̃♮_κ := F♮_κ/κ_κ = (D̃_δB_δ)(ζ)·K·G_κ.

On (0, z_*), ρ₁ = t − t_κ = −(index offset): with λ = n^p/y, t = λ^{1/p}, t_κ − δ = N̄(λ) + ½ is W's smoothed count, so
**ρ₁ = −(N̄(λ) + ½ − λ^{1/p} − κ₀) with κ₀ = −δ = Z(0) + ½**, and ρ₁(y) = Σ_{m≥1}a_m(y/n^p)^{q_m}, a_m := −binom(1/p, m)(−κ)^m (convergent for
y < z_*; ρ₁ = (κ/p)n^{1−p}y^{1−1/p}(1 + O(y/z_*))).

**Lemma W-out.3 (the unnormalised scalar).** Assume (S).
(a) F_κ is analytic and zero-free on ℂ∖([0, ∞) ∪ Γ_κ). Jumps: −e^{2iθ_κ} on (0, 4c), **e^{2iθ_κ} on (4c, z_*)** (κ > 0) resp. (4c, ∞)
  (κ < 0), off the nodes; **−1 on (z_*, ∞)** (κ > 0); J := −e^{2iθ_κ} on (−∞, −z′) (κ < 0, θ_κ real there); none on (−z′, 0) or (−∞, 0).
(b) (hard edge) F_κ(z)/F_δ(z) → 1 as z → 0 off the lens, and (D̃_δB_δ)(ζ(z))/(D̃_δB_δ)(z) → 1 in the lens: (O5) near 0 holds verbatim.
(c) (the moved Hurwitz infinity) as z → z_* (κ > 0) or −z′ (κ < 0), boundary values included,
  F_κ(z) = C_δ(−ζ(z))^{δ+½}K(z)(1 + o(1)),  |F_κ(z)| = C_δ|K(z_*)|z′^{2δ+1}|z − z_*|^{−δ−½}(1 + o(1)).
(d) (z = ∞, fixed n) κ > 0: F_κ(z) = Φ_δ(−z_*)(−z)^{−½}(1 + O(1/z)); κ < 0: F_κ = Φ_±(∞)(−z)^{−½}(1 + O(1/z)) in ℂ_±, with
  Φ_±(∞) := Φ_δ(z′ ± i0) and Φ₊(∞)/Φ₋(∞) = −e^{2πi(t_∞ − δ)}.
*Proof.* (a) Φ_δ is analytic and zero-free on ℂ∖[0, ∞), with Φ_δ₊/Φ_δ₋ = D_δ₊/D_δ₋ = −e^{2iθ_δ} on (0, ∞) off the nodes and no jump on
(−∞, 0) (P1.4(a); B_δ cancels D_δ's jump there). Pull back by ζ (L W-out.1(a), orientation preserved): ζ^{−1}((0, ∞)) = (0, z_*)
(κ > 0) resp. (0, ∞) ∪ (−∞, −z′) (κ < 0); ζ^{−1}((−∞, 0)) = (−∞, 0) ∪ (z_*, ∞) (κ > 0) resp. (−z′, 0). Multiply by K (jump −1 on (4c, ∞)).
(b) ζ(z) = z(1 + O(z/n^p)); D̃_δ(t(ζ)) → 1 (G12 L1.2(b)), κ_δ → 1 off the lens, B_δ continuous at 0 (L1.3(iii)). (c) C1.5 with ζ → ∞:
Φ_δ(ζ) = F_δ(ζ)/K(ζ) = C_δ(−ζ)^δ(4c − ζ)^{½}(1 + o(1)) = C_δ(−ζ)^{δ+½}(1 + o(1)) (ζ ∉ [0, ∞)), and −ζ = zz_*/(z − z_*). (d) ζ(∞) = −z_* is a
point of (−∞, 0), where Φ_δ is analytic (κ > 0); for κ < 0, ζ(∞) = z′ ∈ (Ξ₁, ∞) is not a node, Φ_δ has analytic continuations
Φ_± from ℂ_± across it, with ratio −e^{2iθ_δ(z′)} = −e^{2πi(t_∞ − δ)}; and K ~ (−z)^{−½}. ∎ (PROVED-mod-cite: G12 P1.4, C1.5 (REVIEWED).
NUMERICAL: w_outer_scalar [O1], [zs], [inf], [0].)

**Remark 3.6 (what the literal claim gets wrong).** JZC_W §5.1 item 1 asks for an outer scalar with "power at z = ∞ … −Z(0) − ½". By (d),
the interpolant-built scalar F_κ has exponent **−½** at z = ∞ for every κ ≠ 0 (fixed n), not δ = −Z(0) − ½; the alternative construction
κ_κe^{−j_δ(t_κ)}B̂K (Binet scalar composed with t_κ, cut on Γ_κ) has exponent δ − t_∞ for κ < 0 (index function at λ = 0, not at λ = ∞;
computed from the limit of its Binet-cut density, not checked numerically).
The exponent at fixed-n infinity is therefore not a spectral invariant: it sees the regime |z| ≳ n^p (λ ≲ 1), where t_κ − t is not small.
What is invariant is the exponent of the **normalising gauge at the hard edge** (P W-out.3(b)): G_κ ∼ (−z)^{−δ}E_κ(0), −δ = Z(0) + ½. For
Hurwitz lattices E ≡ 1 and the two readings coincide (C1.5), which is why §5.1 phrased it at ∞. The end-to-end data exclude the
"exponent at ∞" readings (A1 in §8: β = α − 1 for κ > 0, α + 2δ − 2t_∞ for κ < 0) by 3.7·10³–6·10⁵ tolerances.

**Proposition W-out.3 (normalised outer scalar).** Assume (S).
(a) **(O1) with the lattice phase:** F♮_κ is analytic and zero-free on ℂ∖[0, ∞) (no jump on (−∞, 0), across −z′ included), has
  continuous boundary values on (0, ∞)∖({X_k} ∪ {z_*}), and **F♮_κ₊ = F♮_κ₋e^{2iθ} on (4c, ∞)∖({X_k} ∪ {z_*})**.
(b) **(hard edge)** E_κ is continuous at 0 with E_κ(0) = exp∫_0^∞ρ₁(y)[1/y − 1/(y + 1)]dy (+ the ρ̃ term) ∈ (0, ∞), and
  |log E_κ(z) − log E_κ(0)| ≤ C n^{1−p}|z|^{1−1/p} for |z| ≤ 1 (C = C(p, δ, κ), n-free). So G_κ(−z)^{δ} → E_κ(0): the exponent of the gauge
  at 0 is **−δ = Z(0) + ½**, and F♮_κ = E_κ(0)F♮_δ(1 + o(1)) at 0 off the lens.
(c) **(regular at the moved infinity)** |F♮_κ|^{±1} is bounded near z_* (κ > 0) and near −z′ (κ < 0); −z′ is a removable point.
(d) **(O5) at ∞ and normalisation:** |F♮_κ(z)|^{±1} ≤ C_n|z|^{C_n} for |z| ≥ X₁ + δ′, and F♮_κ(iy) → e^{L_κ} ∈ ℂ∖{0} as y → ±∞. Hence
  Paper 2's Lemma normalisation holds for F♮_κ (with X₁ + δ′), **F♮_κ(z) → C_κ ≠ 0 uniformly as z → ∞**, and with (L W-out.2(a))
  Q = k_∞^{−σ₃}(Uz^{−nσ₃})k^{σ₃} near ∞ for the degree-n κ-problem: the extraction gives b_n, a_n of σ^{δ,κ}.
Equivalently: **F_κ(z) = C_κ(−z)^{δ}E_κ(z)^{−1}(1 + o(1))** as z → ∞ — the factor (−z)^{−Z(0)−½} with the κ-free exponent, times
E_κ^{−1}, which carries all κ-dependence, tends to the constant E_κ(0)^{−1} at the hard edge, and is ∼ (−z)^{−δ−½} at fixed-n infinity.

*Proof.* (a) Jumps on (0, ∞): (−z)^{−δ} jumps by e^{2πiδ}. 𝒞[ρ₁] has boundary values 𝒞_± = PV ± iπρ₁ wherever ρ₁ is real-analytic
(deform the integration path locally; ρ₁ is real-analytic on (0, z_*) and on (z_*, ∞) as a combination of t, t_κ), so E_κ jumps by
e^{2πiρ₁}. On (4c, z_*): F_κ (L W-out.3(a)) × (−z)^{−δ} × E_κ jumps by e^{2πi(t_κ − δ)}e^{2πiδ}e^{2πi(t − t_κ)} = e^{2πit} = e^{2iθ}. On (z_*, ∞)
(κ > 0): (−1)e^{2πiδ}e^{2πi(t − δ − ½)} = e^{2πit}. On (−∞, −z′) (κ < 0): F_κ jumps by J = −e^{2πi(t_κ − δ)}, E_κ by e^{2πiρ̃} = J^{−1},
(−z)^{−δ} and K not at all: no jump; on (−z′, 0) nothing jumps. Zero-free: each factor is. Continuity of boundary values off the
listed points: Φ_δ (P1.4(a)), and 𝒞 as above. (b) By the expansion proved in P W-out.5 (its proof does not use this item): for |z| < L < z′,
𝒞[ρ₁](z) − 𝒞[ρ₁](0) = Σ_{m≥1}a_mn^{−pq_m}(−π/sin(πq_m))(−z)^{q_m} + Σ_{j≥1}FP_jz^j, with |a_m|n^{−pq_m} = |a_m|n^{1−pm}, |sin(πq_m)| = sin(π/p) > 0,
Σ|a_m|L^m/z′^m < ∞ and FP_j = O((κ/n^p)^j); every term is continuous up to (0, L) from both sides. So |𝒞[ρ₁](z) − 𝒞[ρ₁](0)| ≤
C(n^{1−p}|z|^{q₁} + n^{−p}|z|) ≤ Cn^{1−p}|z|^{q₁} for |z| ≤ 1, boundary values included (q₁ := 1 − 1/p ∈ (0, 1)). L W-out.3(b) gives the rest. (c) Near z_* the density ρ₁ has one-sided limits ρ₁(z_*−) = t(z_*) = t_∞ and
ρ₁(z_*+) = t_∞ − δ − ½ and is Hölder on each side (t_κ is Hölder-1/p at z_*), so (splitting off the constants; the Hölder remainders give
bounded integrals) 𝒞[ρ₁](z) = (ρ₁(z_*−) − ρ₁(z_*+))log(z_* − z) + O(1) = (δ + ½)log(z_* − z) + O(1). So |G_κ| ≍ |z − z_*|^{δ+½}, which
cancels L W-out.3(c). For κ < 0, ρ̃(−z′) = ½ + δ (t_κ(−z′) = 0) is the end value of the support (−∞, −z′], so 𝒞 = (½ + δ)log(−z′ − z) +
O(1) there, cancelling |z + z′|^{−δ−½}; F♮_κ is analytic in a punctured neighbourhood of −z′ (by (a)) and bounded, hence analytic there.
(d) *Limits.* For y ≥ A (κ > 0, A > z_*): ρ₁ − ρ₁(∞) = t(y) = ny^{−1/p}, ρ₁(∞) = −δ − ½; and ∫_A^∞[1/(y − z) − 1/(y + 1)]dy =
−Log((A − z)/(A + 1)), so 𝒞[ρ₁](iY) = (δ + ½)Log(−iY) + const + o(1) by dominated convergence (|t(y)|/y integrable at ∞). Hence
G_κ(iY) = (−iY)^{½}e^{const + o(1)}, and with L W-out.3(d) F♮_κ(iY) → Φ_δ(−z_*)e^{const}. For κ < 0: ρ₁(∞) = −t_∞, ρ̃(−∞) = ½ + δ − t_∞, and
∫_{−∞}^{−A}[1/(y − z) − 1/(y − 1)]dy = Log((A + z)/(A + 1)) ⇒ 𝒞(z) = t_∞Log(−z) + (½ + δ − t_∞)Log z + const + o(1); in ℂ_±,
Log z = Log(−z) ± iπ, so G_κ = (−z)^{½}e^{±iπ(½ + δ − t_∞)}e^{const + o(1)}, and Φ_±(∞)e^{±iπ(½+δ−t_∞)} agree because
Φ₊(∞)/Φ₋(∞) = −e^{2πi(t_∞−δ)} = e^{−2πi(½ + δ − t_∞)} (L W-out.3(d)): the limit along ±iY is the same nonzero number. *Polynomial
bound.* |Φ_δ∘ζ|^{±1} is bounded for |z| ≥ X₁ + δ′ away from z_* (continuous, nonzero, with limits at ∞), (c) covers z_*, |K|, |(−z)^{−δ}|
are powers, and |𝒞(z)| ≤ C_n(1 + log|z|) up to the cuts by G12 P1.4(c)'s window argument, which needs only |ρ₁′(y)| ≤ C_n/|y| for large |y|
(true: t′ = O(y^{−1−1/p}), and t_κ′ likewise on (−∞, −z′)) and |ρ| ≤ C. *Normalisation.* Lemma normalisation's proof applies: ϰ_∞ :=
F♮_κ^{−1}e^{n(g − Log z)} has matching continuous boundary values on (X₁ + δ′, ∞)∖{z_*} ((a) and Lemma gfunction (i)) and on
(−∞, −X₁ − δ′) (both g and Log z jump by 2πi, F♮_κ not at all), hence is analytic in {|z| > X₁ + δ′}∖{z_*} (Morera) and bounded near z_* by
(c), so analytic there too; at ∞ it is polynomially bounded with a nonzero limit along iy, so ∞ is removable and ϰ_∞(∞) ≠ 0. The extraction
is then Paper 2's (eq:Q-at-infinity) with L W-out.2(a). ∎ (PROVED-mod-cite: G12 C1.5, P1.4; Paper 2 Lemma normalisation, Lemma gfunction.
NUMERICAL: w_outer_scalar.)

*Which integer branch.* ρ₁ on (z_*, ∞) is fixed by the jump only mod 1; ρ₁ ± 1 makes F♮_κ ∼ |z − z_*|^{∓1}·… at z_* and ∼ |z|^{±1} at ∞,
violating (O5)/normalisation (control in [zs], [inf]). On (0, z_*) the branch is fixed by (b) (ρ₁(0+) = 0, i.e. no change of the hard-edge
exponent beyond δ). Both are forced, so the global index is 0 and β′ = α + 2δ.

## 4. The jump algebra (H-d)

Run Paper 2's Steps 1–4 with κ_κ, L^κ_±, A^{△κ}_± (Step 1, L W-out.2), the **lattice** g, φ, φ̃ (Steps 2–3), and F♮_κ, F̃♮_κ (Step 4,
(eq:VM)); call the result V♮_κ. Let Ψ₀ be the analytic function on 𝒵_n∖{0} with Ψ₀ := 𝒞[ρ₁] − iπρ₁ in ℂ₊ and 𝒞[ρ₁] + iπρ₁ in ℂ₋
(ρ₁(z) := t(z) − t_κ(z), the analytic continuation; these agree across (0, ρ_κn^p) because 𝒞₊ − 𝒞₋ = 2πiρ₁ there), real on the axis
(Ψ₀ = PV𝒞[ρ₁]), and put
  **H_n^κ := r_n·(D̃_δB_δ∘ζ)^{−2}·e^{−2Ψ₀},  W₀^κ := 𝗐_nz^{α+2δ}(4c − z)H_n^κ(z)**   (z^{α+2δ} principal) on 𝒵_n.

**Lemma W-out.4.** Under (S), V♮_κ satisfies Lemma jumpsV with the following replacements:
- (a) band (0, 4c): [[0, W₀^κ], [−1/W₀^κ, 0]], because W_κ/(F̃♮₊F̃♮₋) = W₀^κ(x) (H_n^κ > 0 there);
- (d) saturated segment (4c, X₁ + δ′): diagonal I (P W-out.3(a) and Lemma gfunction (i)), entry e^{2nφ̃}/W₀^κ(x), because
  −F̃♮₊F̃♮₋ = W_κ/W₀^κ(x);
- (c) Σ_v and the (1,2) entries on the lips: the lattice formulas with W₀^κ, because e^{−2nφ}e^{∓2iθ_κ}W_κ/F̃♮² = e^{−2nφ̃}W₀^κ(z) in ℂ_±;
- (b), (e), (f) the (2,1) entries on the lips (main and super-small), Σ^△ and the top segment: κ_κ±e^{2nφ}**e^{±2πi(δ + ρ₁(z))}**/W₀^κ(z);
- (g) no jump on (−∞, 0) or (X₁ + δ′, ∞).
In the Q-frame (D_W := Szegő function of W₀^κ), the band limits of the lip data at 0 are e^{∓iπβ′}e^{±2πiδ}e^{±2πiρ₁(0)} = e^{∓iπα} (ρ₁(0) = 0):
the hard-edge model has **Bessel order α and Szegő exponent β′ = α + 2δ** (JZC_M3a_Hd (iii)), and the deviation of the lip factor from
the Hurwitz one is |e^{±2πiρ₁(z)} − 1| ≤ Cn^{1−p}|z|^{1−1/p} on the lips in U(0, δ_r). The lips avoid U(4c, h₀) (Paper 2 Lemma lips (c)), so
the Airy disc sees only (a), (c), (d), where the phases cancel exactly.

*Proof.* JZC_M3a_Hd (ii)'s algebra with θ_δ ↦ θ_κ and (−z)^{−δ} ↦ G_κ: it uses only L₋^{−1}L₊ = U(W) and κ_+^{−1} + κ_−^{−1} = κ_+^{−1}κ_−^{−1}
(any real phase), and the four identities, which we verify. On the band: (D̃_δB_δ)(ζ(x)) > 0 has no jump, K₊K₋ = (4c − x)^{−1},
G₊G₋ = x^{−2δ}E₊E₋ = x^{−2δ}e^{2PV𝒞[ρ₁](x)}, so W_κ/(F̃♮₊F̃♮₋) = 𝗐_nx^αr_n(4c − x)x^{2δ}(D̃_δB_δ)^{−2}(ζ)e^{−2Ψ₀(x)} = W₀^κ(x); on
(4c, X₁ + δ′) the same with K₊K₋ = −(4c − x)^{−1}. In ℂ_±: (−z)^{−2δ} = z^{−2δ}e^{±2πiδ} and E_κ² = e^{2Ψ₀}e^{±2πiρ₁}, so
W_κ/F̃♮² = W₀^κ(z)e^{∓2πiδ}e^{∓2πiρ₁(z)}, while e^{∓2iθ_κ} = e^{∓2iθ}e^{±2πiδ}e^{±2πiρ₁(z)} and e^{∓2iθ}e^{−2nφ} = e^{−2nφ̃} (Paper 2
(eq:identities)): this gives (c); inverting gives (b), (e), (f). (g) is P W-out.3(a). The Q-frame statement is Hd (iii) with the extra
factor, and |ρ₁(z)| ≤ Cn^{1−p}|z|^{q₁} in the sector (from the series for ρ₁). ∎ (PROVED, algebra. NUMERICAL: w_outer_scalar [W4]:
band weight real and equal to the formula to 10⁻⁸ (at η = 10⁻¹⁴), lip phase = e^{−2πiρ₁(x)} to 10⁻¹⁴, Σ_v cancellation to 10⁻³⁰.)

For F5 on Σ^△ and the top segment (Re z ≤ X₁ + δ′ < z_*, |Im z| ≤ h₀) the only change from Hd is the factor |e^{±2πiρ₁(z)}| = e^{∓2πIm ρ₁} ≤ C
(|ρ₁| ≤ C there), so |v − I| ≤ Ce^{−n/C} survives. For the Hölder conditions of Paper 2's (O3)/(F2) on 𝒵_n ∩ {|z| ≤ 1}: the new part of
log H_n^κ is −2Ψ₀ + log r_n, with |Ψ₀(z) − Ψ₀(0)| ≤ Cn^{1−p}|z|^{q₁} (P W-out.5), q₁ = 1 − 1/p. **For p ≥ 2, q₁ ≥ ½ ≥ ν_p and (O3) holds with
n-free constants; for 1 < p < 2 it holds with ν_p replaced by q₁ < ν_p** — for H_n^κ alone. This is no restriction: by JZC_W_kappa
P K.13, every use of ν_p in Paper 2 and G12/G1u/Hc concerns the lip coefficient, which carries the gauge only through X (exponent ½,
JZC_W_kappa L K.4), and G1u L3's lip mismatch bound |z|^{ν_p}log(2/|z|) holds for every p > 1 with the lip phase included (JZC_W_kappa
L K.6(v)) (fixed per Rule R review A of the W chain, B4).

## 5. The band factor (H-c): Toda times and pole tilts

**Lemma W-out.5 (PV lemma).** Let q > −1, q ∉ ℤ, L > 0. For |z| < L, z ∉ [0, L):
  ∫_0^Ly^q dy/(y − z) = −π(−z)^q/sin(πq) + Σ_{j≥0}z^jL^{q−j}/(q − j)   (principal (−z)^q).
On (0, L) the boundary values are PV ± iπx^q, with PV = −π cot(πq)x^q + Σ_jx^jL^{q−j}/(q − j).
*Proof.* f(z) := ∫_0^Ly^q/(y − z)dy + π(−z)^q/sin(πq) has no jump on (0, L): the integral jumps by 2πix^q, and ((−z)^q)₊ − ((−z)^q)₋ =
x^q(e^{−iπq} − e^{iπq}) = −2ix^q sin(πq). At 0, |f| ≤ C(1 + |z|^q + |z|^{0}log(1/|z|)) = o(1/|z|), so f is analytic on |z| < L. ∂_L of f is
L^q/(L − z) = Σ_jz^jL^{q−j−1}, so the Taylor coefficients satisfy c_j(L) = L^{q−j}/(q − j) + k_j; and f(λz; λL) = λ^qf(z; L) gives
c_j(λL) = λ^{q−j}c_j(L), so k_j = 0 (q ≠ j). ∎ (PROVED. NUMERICAL [PV], 6 cases to 10⁻²⁵.)

**Proposition W-out.5 (structure of H_n^κ).** Assume (S) and let J ≥ 1, n ≥ n₀. For z ∈ 𝒵_n with |z| ≤ 4c + 1 (z^{q} principal),
  log H_n^κ(z) = c_n − Σ_{j≤J}μ_{n,j}z^j + Σ_{m≥1}τ_m(z/n^p)^{q_m} + O(n^{−(J+1)p}),   c_n constant,
with
(i) **μ_{n,j} = (2Z_κ(−j)/j − B_j)n^{−jp}** (with Z_κ(−j) as in L W-out.0(c) and the Fourier sums m_k(δ) for ζ(−kp, a)/(kn^{kp})), B_j the
  Taylor coefficients of log D(x) = (1/p − 1)log(1 − κx): these are **exactly Conjecture W's Toda parameters** (JZC_W §1.2) for σ^{δ,κ};
(ii) the gauge's integer share is −2FP_jz^j with **FP_j := FP∫_0^∞ρ₁(y)y^{−j−1}dy (+ ∫ρ̃y^{−j−1}dy) = ζ(0, a)κ^jn^{−jp}/j**;
(iii) the branched part comes only from −2Ψ₀: **τ_m = 2π cot(πq_m)a_m = −2π cot(πq_m)R_{q_m}/q_m**. Equivalently, E_κ^{−2} ∋
  exp(Σ_m(2πa_m/sin(πq_m))(−z/n^p)^{q_m}): since (−z)^q = z^qe^{∓iπq} in ℂ_±, this splits into the tilt e^{Σ_mτ_m(z/n^p)^{q_m}} (the cot part, the
  analytic continuation of the band tilt) and the lip factor e^{±2πiΣ_ma_m(z/n^p)^{q_m}} = e^{±2πiρ₁(z)} (the sin part) of L W-out.4.
*Proof.* log H_n^κ = −2G_δ(ζ(z)) + log r_n − 2Ψ₀. *Hurwitz part.* ζ maps |z| ≤ 4c + 1 into |ζ| ≤ 4c + 2 (n ≥ n₀), so Hc.2(ii) applies:
−2G_δ(ζ) = const − Σ_{k≤K}μ^δ_{n,k}ζ^k + O(n^{−(K+1)p}), μ^δ_{n,k} = 2m_k(δ); ζ^k = z^kΣ_{l≥0}binom(k + l − 1, l)(z/z_*)^l, so the coefficient of
z^j is Σ_{k≤j}μ^δ_{n,k}binom(j − 1, k − 1)κ^{j−k}n^{−(j−k)p}; with m_k = ζ(−kp, a)/(kn^{kp}) this is n^{−jp}Σ_k(2/k)binom(j−1, k−1)κ^{j−k}ζ(−kp, a)
= n^{−jp}(2/j)Σ_{k=1}^{j}binom(j, k)κ^{j−k}ζ(−kp, a) = n^{−jp}[2Z_κ(−j)/j − 2κ^jζ(0, a)/j] ((1/k)binom(j−1, k−1) = (1/j)binom(j, k)).
*Density.* log r_n = (1/p − 1)log(1 − κz/n^p) = Σ_jB_j(z/n^p)^j. *Gauge.* For |z| < L < z′ split 𝒞[ρ₁] at L. On (0, L), ρ₁ = Σa_m(y/n^p)^{q_m}
converges uniformly (|binom(1/p, m)| summable and (L/z′)^m ≤ 1); apply L W-out.5 termwise: the (−z)^{q_m} terms give
Σ_ma_mn^{−pq_m}(−π/sin(πq_m))(−z)^{q_m}, and in ℂ₊ (−π/sin(πq))(−z)^q = (−π cot(πq) + iπ)z^q, so Ψ₀ = 𝒞 − iπρ₁ has branched part
Σ_ma_m(−π cot(πq_m))(z/n^p)^{q_m} (the same in ℂ₋): this is (iii). The z^j-coefficients Σ_ma_mn^{−pq_m}L^{q_m−j}/(q_m − j) + ∫_L^∞ρ₁y^{−j−1}dy
(+ ∫ρ̃y^{−j−1}dy) =: FP_j do not depend on L (the finite-part integral); the remaining Taylor tail of the convergent part is O(n^{−(J+1)p}). (ii), κ > 0: substitute y = z_*u:
FP_j = nz_*^{s}[FP∫_0^1u^{s−1}(1 − (1 − u)^{1/p})du + ∫_1^∞u^{s−1}du] − (δ + ½)z_*^{−j}/j, s := −1/p − j. FP∫_0^1u^{s−1}du = 1/s cancels
∫_1^∞u^{s−1}du = −1/s, and FP∫_0^1u^{s−1}(1 − u)^{1/p}du = Σ_mbinom(1/p, m)(−1)^m/(s + m) =: 𝔅(s) is the continuation of the Beta integral
B(s, 1 + 1/p) (equal for Re s > 0 termwise; both sides meromorphic). Integration by parts gives B(s + 1, r + 1) = sB(s, r + 1)/(s + r + 1)
(r := 1/p) for Re s > 0, so 𝔅(s) = ((s + r + 1)/s)𝔅(s + 1) on ℂ; at s = −r − 1 the prefactor vanishes and 𝔅(−r) is finite (−r ∉ −ℕ₀), so
𝔅(−r − 1) = 0, and by induction 𝔅(−r − j) = 0 for all j ≥ 1. So FP_j = −(δ + ½)κ^jn^{−jp}/j = ζ(0, a)κ^jn^{−jp}/j. *κ < 0* (z′ = n^p/|κ|, r := 1/p, s := −r − j):
- (0, ∞): ρ₁ = t(y)(1 − (1 + y/z′)^{r}); with y = z′u and FP∫_0^∞u^{s−1}du = 0, this piece is −nz′^{s}·FP∫_0^∞u^{s−1}(1 + u)^{r}du. For
  −r − 1 > ℜa > −r − j − 1 the finite part is the analytic continuation in a of ∫_0^∞u^{a−1}(1 + u)^{−(a+b)}du = B(a, b), b := −r − a (DLMF 5.12.3,
  stated for ℜa, ℜb > 0; both sides are meromorphic in a, and the finite part is the continuation, by subtracting the Taylor terms of
  (1 + u)^r at 0). At a = s, b = j: the piece is −nz′^{s}Γ(s)Γ(j)/Γ(−r) (5.12.1).
- (−∞, −z′): ρ̃ = ½ + δ − t_κ. The constant gives (½ + δ)∫_{−∞}^{−z′}y^{−j−1}dy = −(½ + δ)(−z′)^{−j}/j = −(½ + δ)κ^jn^{−jp}/j = ζ(0, a)κ^jn^{−jp}/j
  ((−z′)^{−j} = κ^jn^{−jp}). For t_κ(y) = |κ|^r(1 − z′/|y|)^r, y = −z′/w: −∫_{−∞}^{−z′}t_κy^{−j−1}dy = (−1)^jnz′^{s}∫_0^1w^{j−1}(1 − w)^rdw
  = (−1)^jnz′^{s}Γ(j)Γ(1 + r)/Γ(1 + r + j) (5.12.1 with ℜa = j > 0, ℜb = 1 + r > 0: hypotheses hold).
- By 5.5.3 (−r − j, −r ∉ ℤ), Γ(−r − j)/Γ(−r) = (−1)^jΓ(1 + r)/Γ(1 + r + j), so the two n-terms cancel, and FP_j = ζ(0, a)κ^jn^{−jp}/j again.
Then (i) = Hurwitz + density + gauge. ∎
(PROVED-mod-cite: Hc.2 (REVIEWED), DLMF-2 (5.12.1, 5.5.3) for κ < 0; the name ζ(−kp, a) for the Fourier-sum constants is Remark 3.3,
PROVED-mod-cite (CITATIONS (Hurwitz-DK)) (updated 2026-10-22: Hurwitz's formula quoted, CITATIONS (Hurwitz-DK)). NUMERICAL: [T] the identity (i) to 10⁻³⁰ for j ≤ 5 at 4 parameter sets (without the gauge share it fails); [A] a_m = −R_{q_m}/q_m;
[W5] FP₁, FP₂ extracted from 𝒞[ρ₁] near 0 at κ = 0.5, −0.3, 1, −0.02.)

**Proposition W-out.7 (pole terms = gauge tilt response).** Conjecture W's fractional-time response −(pρW(ρ)/2)t_ρ(n/N)^pN^{−1−pρ}
(JZC_W §1.3, third line), applied to the tilt t_{q_m} = τ_m = −2π cot(πq_m)R_{q_m}/q_m of P W-out.5(iii), equals
  pR_{q_m}W(q_m)π cot(πq_m)(n/N)^pN^{−1−pq_m},
which is W's pole term (second line) for every m. (PROVED, algebra; the identity a_m = −R_{q_m}/q_m is the binomial identity
(−1)^mbinom(1/p, m) = −binom(m − 1/p, m)/(p(m − 1/p)), both sides = −(1/p)Π_{i=1}^{m−1}(i − 1/p)/m!.)

So for this node set W's three ingredients have one source: the Szegő shift is the gauge's hard-edge exponent, the Toda times are the
integer moments (Binet-cut∘ζ + density + gauge FP), and the π cot pole terms are the gauge's PV band tilt. (W's "one linear response for
every time" extends to the poles: a pole is a fractional time of the gauge.)

## 6. The reduction (which steps of H-a…H-f change, and the resulting statement)

| step | Theorem H (Hurwitz) | κ ≠ 0 (this note) | status |
|---|---|---|---|
| H-a | sin π(t − δ), 1/Γ(t − δ), top node (n/a)^p | sin π(t_κ − δ), t_κ = t∘ζ; W_κ = W·r_n (density); X₁ = n^p/(a^p + κ); 𝒵_n radius < z_* | L W-out.1–2: PROVED-mod-cite |
| H-b | F_δ ∼ C_δ(−z)^δ at ∞; gauge (−z)^{−δ} | F_κ = Φ_δ∘ζ·K ∼ (−z)^{−½} at ∞; gauge G_κ = (−z)^{−δ}E_κ with variable density ρ₁ = −(index offset); hard-edge exponent −δ | P W-out.3: PROVED-mod-cite |
| H-b′ | G12 L2.1–P2.4 (a-priori bound, \|α\|/2) | column factorisation with G♮ := G_κD_{x^{2δ}}D_{e^{−2Ψ₀}}: \|E_κ\|^{±1} and the Szegő function of the Hölder factor e^{−2Ψ₀} are bounded near 0 (fixed n), so P2.4 should transfer; L2.1 needs the κ-node sum (node spacing 1 in t_κ, masses t^{−s}) | PROVED-mod-cite: JZC_W_kappa P K.5 (L K.2–K.4) (fixed per Rule R review A of the W chain, B4) |
| H-c | Hc.2–Hc.3: H_n^δ = e^{−Σμζ^k}(1 + O(n^{−(J+1)p})) | H_n^κ = (Hurwitz∘ζ)·r_n·e^{−2Ψ₀}: integer part = W's Toda times (P W-out.5(i)); **branched part τ_m(z/n^p)^{q_m} + lip factor** | integer part PROVED-mod-cite; the gauge Hc.3 on the circles for the branched part: PROVED-mod-cite, JZC_W_kappa L K.10 (fixed per Rule R review A of the W chain, B4) |
| H-d | jumps of M(α + 2δ, α); lip phases e^{±2πiδ} | same, plus e^{±2πiρ₁(z)} on lips/Σ^△/top; Bessel order α, Szegő β′ = α + 2δ | L W-out.4: PROVED |
| H-e | N.6a–c for M(β, ν), G1u in the α-frame | the circle jumps contain branched terms of size n^{1−p}\|z\|^{q₁}: N.6b's meromorphy fails — not for the coherent data of the κ-problem (JZC_W_kappa L K.9), and not needed for (iii) (JZC_W_kappa P K.11); G1u (A), (B) transfer for every p > 1 (JZC_W_kappa P K.8) | PROVED-mod-cite: JZC_W_kappa L K.9, P K.8, P K.11 (fixed per Rule R review A of the W chain, B4) |
| H-f | exact algebra of M(β, ν) | unchanged for the integer and Toda layers; for the branched layer: W's fractional-response formula (for the κ-family's coherent first-order branched layer: JZC_W_kappa Prop K.12′) | P W-out.7 (algebra) + PROVED-mod-cite (Prop K.12′) (fixed per Rule R review A of the W chain, B4) |

**Hypothesis BT (branched tilts; = JZC_W §5.1 item 4; GAP).** For p > 1, |ν| < 1, real β, the decoupled model M(β, ν) of JZC_M4 §7 in the
n^p frame with band factor exp(−Σ_{j≤J}μ_{n,j}z^j + Σ_{ρ∈𝓡}τ_ρ(z/n^p)^ρ) (𝓡 ⊂ (0, ∞)∖ℕ finite, μ_{n,j} = O(n^{−jp}), τ_ρ bounded; z^ρ principal,
continued from the band) and lip (2,1) factors exp(±iπΣ_ρσ_ρ(z/n^p)^ρ) (σ_ρ bounded) has
  n^pb_n/c = 𝔅_n[M(β, ν); μ] − Σ_ρ(pρW(ρ)/2)τ_ρ(n/N)^pN^{−1−pρ} + O(n^{−1−p·min𝓡−η}) for some η > 0,
N = n + (β + 1)/2: in particular the lip coefficients σ_ρ do not enter at order N^{−1−pρ}.
*Scope for the κ-family:* only **coherent** tilts (σ_ρ = (τ_ρ/π)tan(πρ)) occur here, and for them BT is JZC_W_kappa's BT_coh, proved there
(Prop K.12′, η = 1); for the non-coherent companion (independent σ_ρ, e.g. a genuine x^ρ tilt) see JZC_W_BT (Theorem BT, Cor BT.6; as
asymptotics CONDITIONAL on (F-br)) (fixed per Rule R review A of the W chain, B4).
**Hypothesis BT₀ (crude form).** The same model satisfies n^pb_n/c = 𝔅_n[M(β, ν); μ] + O(n^{−1−p·min𝓡}log n).

**Proposition W-out.6 (reduction).** Assume (S), p > 1.
(i) *(exact; PROVED-mod-cite)* The degree-n RH problem of σ^{δ,κ}, transformed by Paper 2's Steps 1–4 with t_κ (L W-out.2), the lattice g
  and F♮_κ (P W-out.3), is the decoupled problem **M(β′ = α + 2δ, ν = α)** with band weight W₀^κ (L W-out.4) and the lip factor
  e^{±2πiρ₁(z)}; Lemma normalisation and the extraction hold (P W-out.3(d)); and H_n^κ has the structure of P W-out.5: Toda parameters
  μ_{n,j} = (2Z_κ(−j)/j − B_j)n^{−jp} up to O(n^{−(J+1)p}), branched tilts τ_m = −2π cot(πq_m)R_{q_m}/q_m, lip coefficients σ_m = 2a_m
  (m = 1, …; q_m = m − 1/p), and products of these at higher order. **Z(0) = −½ − δ does not depend on κ** (L W-out.0), so β′ is κ-free.
(ii) *(PROVED-mod-cite (W_kappa P K.12 + K.12′); formerly CONDITIONAL on BT and on the transfer G1u/Hc.3 to the composite band factor,
  now W_kappa L K.10 + P K.8)* Conjecture W holds for σ^{δ,κ} at first order in the poles:
  n^pb_n/c = 𝔅_n[M(α + 2δ, α); t] + Σ_m pR_{q_m}W(q_m)π cot(πq_m)(n/N)^pN^{−1−pq_m}(1 + O(N^{−1})) + …,  t_j = −2Z_κ(−j)/j + B_j,
  precisely: with the continued pole dressing the remainder is O(n^{−2p}); in the displayed form, with (1 + O(N^{−1})), it is O(n^{−1−p})
  (W_kappa P K.12) (fixed per Rule R review A of the W chain, B4).
(iii) *(PROVED-mod-cite (W_kappa P K.11); formerly CONDITIONAL on BT₀ and the same transfer)* For every k < p, the coefficient of n^{−k} in n^pb_n/c equals that of M(α + 2δ, α): it does
  not depend on κ. In particular d₁ = −p(β′ + 1)/2 = −(s − 1)/2 − pδ, and d₂ = d₂(M(α + 2δ, α)) for p > 2.
*Proof.* (i) collects L W-out.0–W-out.4 and P W-out.3, W-out.5. (ii): JZC_W_kappa P K.12 with Prop K.12′ (BT_coh), P W-out.5 and P W-out.7
for the pole terms. (iii): JZC_W_kappa P K.11 (the non-model terms start at n^{−1−pq₁} = n^{−p}). ∎ (fixed per Rule R review A of the W chain, B4)

What (ii) adds to W for this family: W's three layers are *derived* from one exact transformation; what remains is a statement about the
decoupled model alone (BT_coh), with no node set in it, and that statement is JZC_W_kappa Prop K.12′. Numerically (§8) (ii) is consistent at
n^{−p} (pole term, 4·10⁻⁷) and (iii) at n^{−1}, n^{−2} (10⁻¹⁰, 5·10⁻⁸); both are now PROVED-mod-cite (JZC_W_kappa P K.12 + K.12′, P K.11) (fixed per Rule R review A of the W chain, B4).

## 7. p < 1: what changes

- **Spectral data.** Z(0) = −½ − δ unless p = 1/m, where Z(0) = −½ − δ + (−κ)^m (L W-out.0): then W predicts β = α + 2δ − 2(−κ)^m, a κ-dependent
  Szegő shift. In the gauge picture: q_m = m − 1/p = 0 for that m, and the term a_m(y/n^p)^0 = −(−κ)^m of ρ₁ is a constant: it adds to the
  hard-edge exponent of G_κ exactly the (−κ)^m of Z(0). Consistent, and a test case for W (not run).
- **The gauge density grows at the hard edge.** For p < 1, q_m < 0 for m < 1/p: ρ₁(y) ∼ (κ/p)n^{1−p}y^{1−1/p} is unbounded as y → 0 and is
  O(n^{1−p}) ≫ 1 on the band. Then ρ₁(0+) does not exist, E_κ is not continuous at 0, and the decomposition "M(β′, α) × small branched
  factor" fails: the κ shift changes the equilibrium at relative order n^{−p} but at absolute size n^{1−p} in nφ (SPEC §3.5's remark "small per
  particle, not in absolute terms"). **OBSTRUCTION (heuristic, for this route):** with the lattice g the gauge cannot carry the index
  offset for p < 1; one needs the n-dependent equilibrium (JZC_W §5.1 item 3, JZC_M1 Theorem Q): a g-function whose saturated-region
  density is the κ-node density. The Möbius map still exists (ζ maps the non-node rays arg ζ = ±πp to circular arcs through 0 and −z_*),
  and Φ_δ∘ζ with the seam scalar (G3) gives the unnormalised scalar, but its normalisation is the open step.
- Also: L W-out.1(c) needs the non-nodes t_κ = δ − m, which for p < 1 sit on ζ^{−1}(arg ζ = ±πp); 𝒵_n, the lens and S_in must avoid these
  arcs (true near 0, where ζ ≈ z; near |z| ∼ n^p the arcs bend: GAP-minor).

## 8. Checks (Rule N: NUMERICAL; finite samples; nothing fitted except the Jacobi-coefficient fits of w_outer_e2e)

- **`w_outer_index.py/.out` (ALL 104 CHECKS PASSED; dps 40):** [I1] Möbius identities (5 parameter sets incl. δ = 0); [I2] 15 residues =
  node masses to 10⁻²⁵, controls: no r_n (fails), uncomposed phase (no pole; fails); [I3] argument-principle zero counts = number of κ-nodes;
  [Z0] Z(0) = −½ − δ (6 cases incl. κ ≥ a^p via K₀ and p = 0.6), and Z(0) = −½ − δ + (−κ)^m at p = ½, ⅓ (κ-free value fails); [A] a_m = −R_{q_m}/q_m;
  [T] P W-out.5(i) for j ≤ 5 (without the gauge share: fails); [PV] L W-out.5; [FP] the vanishing Beta value.
- **`w_outer_scalar.py/.out` (n = 4, c = 1, dps 30; cases (p, δ, κ) = (1.5, −0.3, 0.5), (1.5, −0.3, −0.3), (3, −0.7, 1), (3, −0.7, −0.02)):**
  [O1] jump of F♮_κ = e^{2πit} on (4c, ∞) between nodes and beyond z_* (≤ 10⁻¹³); F_κ's jumps; F♮_κ continuous across (−∞, 0) (κ < 0);
  control: the Hurwitz gauge (−z)^{−δ} alone gives the wrong jump. [zs] F♮_κ converges at z_* (r = 10⁻⁶, 10⁻¹², 10⁻¹⁸), exponents of |F_κ|
  and |G_κ| = ∓(δ + ½); controls: the wrong integer branch on (z_*, ∞) gives exponent ±1. [inf] F♮_κ → C_κ on 4 rays (spread 1.5·10⁻⁹ at
  p = 1.5 between R = 10²⁰ and 10³⁰); exponent of |F_κ(iy)| = −½ (the literal δ fails), of |G_κ(iy)| = +½. [0] G_κ(−z)^δ → E_κ(0) with
  decay exponent 1 − 1/p (0.333333 at p = 1.5); F_κ/F_δ → 1 (10⁻²⁰). [W5] FP₁, FP₂ from 𝒞[ρ₁] near 0 (e.g. −0.01250001 vs −0.0125);
  control: dropping the (−z)^{q₁} term. [W4] band weight, lip phase, Σ_v cancellation. ALL 125 CHECKS PASSED (≈ 50 min on 2 shared cores).
- **`w_outer_e2e.py/.out` (ALL 44 CHECKS PASSED):** Plan 62 pipeline (binary128 RKPW), 120 000 atoms + Gauss–Jacobi tail, n ≤ 1200.
  Predictions written (09:41:13) before the three measures existed; the second run re-computes and compares them (to 10⁻³⁰), never rewrites.
  | case | coefficient | prediction | fit (half-range) | alternatives (miss in tolerances) |
  |---|---|---|---|---|
  | KO1 p = 2.5, δ = −0.3, κ = +0.3, s = 2 (β′ = −1.2) | n⁻¹ | +0.25 (M(β′, α)) | +0.250000000 (1.4·10⁻⁷), diff 10⁻¹⁰ | β = α: 3·10⁵; β from F_κ at ∞ (α − 1): 2·10⁵ |
  | | n⁻² | +0.1329166667 (M(β′, α), κ-free) | +0.132916618 (6.7·10⁻⁵) | β = α: 649 |
  | | n^{−2.5} | +0.1970441 (pole term = gauge tilt) | +0.1970439 (1.3·10⁻⁵) | no pole term: 5112 |
  | | n⁻³ | +0.0466875 (M(β′, α) d₃) | +0.0466873 (3.8·10⁻⁴) | |
  | | n^{−3.5} | −0.380944 (Toda + pole shift) | −0.38098 (1.1·10⁻²) | no gauge share in t₁: 5.8; no pole: 2.9 (weak) |
  | KO2 same, κ = −0.3 | n⁻¹, n⁻² | +0.25, +0.1329166667 | +0.250000000, +0.132916688 | β = α: 3·10⁵, 585; index-at-λ=0 β: 6·10⁵ |
  | | n^{−2.5}, n⁻³, n^{−3.5} | −0.1970441, +0.0466875, +0.407232 | −0.1970437, +0.0466828, +0.40719 | no pole 9722; no gauge share 9.0 (weak) |
  | KO3 p = 1.5, δ = −0.4, κ = +0.4, s = 2.5 (β′ = −0.8) | n⁻¹ | −0.15 | −0.149999987 (1.4·10⁻⁵) | β = α: 14785; α − 1: 3696 |
  | | n^{−1.5}, n⁻² | −0.2265089 (pole), +0.2270833 (d₂, κ-free) | −0.2265084, +0.2270844 | no pole: 2260 |
  Run history (Rule X, recorded in the script): run 1 used w_common's nuisance pool {i + jp, i ≥ 1}, which lacks the pole exponents jp;
  all its 37 checks passed but the n⁻² (p = 2.5) and n⁻¹ (p = 1.5) fits were contaminated by the n^{−p} term (residuals ±2·10⁻³, odd in κ).
  Run 2 adds {m + jp} as nuisance columns (a change of the fit method, not of any prediction) and the n^{−3.5} target with the control
  "Toda time without the gauge share 2κζ(0, a)" (chosen after run 1). At n^{−3.5} the fits are weak (half-ranges 10⁻²): the controls miss
  by 3–9 tolerances, so they are asserted at the pass criterion only, and this row is weak evidence.

## 9. Rule A log

1. *Is t_κ = t∘ζ the right branch everywhere it is used?* Checked identically on sample points of ℂ₊ incl. Re z < 0 and |z| = 10⁵ ([I1]).
   The cut of t_κ is Γ_κ; for κ > 0 it meets (4c, ∞) at [z_*, ∞), beyond the contour (X₁ + δ′ + h₀ < z_* for n ≥ n₀) — the only place the
   interpolant is used. Beyond z_* only F♮_κ is needed, and its jump there is fixed by (O1), not by the interpolant.
2. *Counterexample hunt for "exponent −Z(0) − ½ at ∞".* Found: F_κ ∼ (−z)^{−½} for every κ ≠ 0 (L W-out.3(d)), and a second natural construction
   gives δ − t_∞ (κ < 0). Recorded as Remark 3.6; the data exclude both readings (§8, A1). This is the main correction to JZC_W §5.1.
3. *Could another gauge give a different hard-edge exponent?* The gauge's jump is prescribed on (4c, ∞) (by (O1)) only mod integers; on
   (0, 4c) it is free. Moving the δ-part of the density off the band creates an exponent at the soft edge 4c (destroying the Airy model);
   the √(z − 4c)-trick instead creates a constant lip phase at 0 (changing the Bessel order). The integer branches are forced by (O5) at z_*
   and the hard-edge continuity. So within Paper 2's frame (Airy at 4c, Bessel order α at 0) the hard-edge Szegő exponent is forced to be
   α + 2δ; the data (KO1–KO3) confirm. (Argument at the level of the frame; not a uniqueness theorem.)
4. *Signs and conventions of the pole identity.* P W-out.7 was derived symbolically and then checked against w_common.predict's pole terms:
   for KO1 the gauge-tilt response −(pq₁W(q₁)/2)τ₁ reproduces +0.1970441 (the "pole q = 0.6" term) — sign flip would give −0.197, excluded by
   10⁴ tolerances (KO1 vs KO2 are mirror images in κ, and the fits flip sign accordingly).
5. *κ → 0.* z_* → ∞, ρ₁ → 0 on compacts, and F♮_κ → F♮_δ locally uniformly; the limit at ∞ is non-uniform (the (z_*, ∞) piece of ρ₁ is
   t − δ − ½, not small), as is C1.5's in δ → 0 (G12 Rule A 3). Fixed-n statements only; no n-uniform input lives at |z| ≳ n^p.
6. *Large κ (κ ≥ a^p).* The binomial series for Z fails; L W-out.0 splits off K₀ nodes (checked at κ = 2, 5). The scalar construction never
   uses the series (only ρ₁'s expansion for y < z_*, which converges for all κ since |y/z_*| < 1).
7. *κ < 0 near −a^p.* t_∞ = |κ|^{1/p} → a: the non-node check of L W-out.1(c) uses t_∞ < a strictly (κ > −a^p). At equality the first node
   would sit at λ₁ = 0 (excluded).
8. *Half-integer q.* q_m = ½ (p = 2/(2m − 1); p = 2 for m = 1): τ_m = 0, so the gauge has no first-order band tilt and only the lip factor —
   exactly where JZC_W found the W′ term (K2p/K2m at p = 2, n^{−3−p/2}). Consistent with BT's claim that lip coefficients enter only beyond
   N^{−1−pρ}; the heuristic order of §10 item 4, n^{−2−(p+2)/2} = n^{−3−p/2}, is W′'s order. (Heuristic consistency, not a proof.)
9. *Precision (Rule N).* Boundary values are evaluated at η = 10⁻¹⁴|x| with quadrature breakpoints at the near-singular point; the jump
   checks are at 10⁻¹³–10⁻¹⁶, the exponent fits at r = 10⁻¹², 10⁻¹⁸ (Hölder rate r^{1/p}, so the C1.5 o(1) is ≤ 10⁻⁴·C at p = 3). A first
   version measured the z_* exponents at r = 10⁻⁵, 10⁻⁷, where the p = 3 rate (r^{1/3}) would have been too slow; changed before any run
   completed. The residue control "uncomposed phase has no pole" first used a circle that contained the Hurwitz node Ξ_k (spurious pass of
   the true residue in the control): the control circle now excludes Ξ_k, and the true residue circle excludes z_* (one true residue at
   p = 3, κ = 1 had failed because the circle contained z_*).
10. *Rule X.* Predictions of w_outer_e2e from spectral data and the model engine only, written before the measures; the second run's changes
   are listed in §8 and in the script header. The fit-method change could only make the agreement worse if the pole exponents were absent.

## 10. What remains

1. **Hypothesis BT** (= JZC_W §5.1 item 4): N.6/E3.7 for the decoupled model with branched band tilts and lip factors vanishing at 0.
   This was the *only* gap between Theorem H's machinery and Conjecture W(i) at first order for this family; it is now closed for the
   κ-family by JZC_W_kappa Prop K.12′ (BT_coh, the coherent case, which is all this family needs) (fixed per Rule R review A of the W chain, B4); for general (non-coherent)
   branched tilts it stays open as (F-br) (JZC_W_BT §3.3). Originally: it is a statement about a model problem with no node set in it. A test without measures: run the exact/float engine with a z^ρ tilt (JZC_W §5.3); here P W-out.7
   fixes the expected answer.
2. **The transfer of Hc.3/G1u to the composite factor** (Hurwitz∘ζ · r_n · e^{−2Ψ₀}) for the analytic part (routine: ζ is analytic on the
   circles, Hc.2 applies), and H-b′ (G12 §2) for the κ-nodes (sum bound with node spacing 1 in t_κ; column factorisation with E_κ). Done:
   JZC_W_kappa L K.10, P K.8 and P K.5 (fixed per Rule R review A of the W chain, B4).
3. **1 < p < 2:** the Hölder exponent of the gauge at 0 is q₁ = 1 − 1/p < ν_p = ½; no restriction is needed: JZC_W_kappa P K.13 (the lip
   coefficient carries the gauge only through X, exponent ½) (fixed per Rule R review A of the W chain, B4).
4. **Lip factors (HEURISTIC prediction, not tested):** a lip factor of size n^{−pρ}|z|^ρ acts through the Bessel region |z| ≍ n^{−2}, where the
   Bessel order enters b_n at relative n^{−2}; so the lip coefficients σ_ρ = 2a_m should first act at n^{−2−(p+2)ρ} (ρ = 0, a constant lip phase,
   gives the Bessel-order shift at n^{−2}, as for δ); at ρ = ½ this is W′'s n^{−3−p/2}. For ρ ≠ ½ this predicts a term at n^{−2−(p+2)q_m}, not at W′'s n^{−3−pq_m} (they agree only at q = ½).
   Testable at p = 1.5 (q₁ = ⅓: n^{−3.17}) with a longer measure.
5. **p < 1:** the n-dependent equilibrium (§7); the case p = 1/m with κ-dependent Z(0) as a test of W.
6. **General node sets:** the construction uses the Möbius structure only to reuse G12/Hc; the gauge ρ₁ = −(index offset), the Toda share
   FP_j and the pole tilt τ = −2π cot(πq)R_q/q are written invariantly, so the next case is a node set with an analytic index map and no
   Möbius structure (JZC_M3_scope M3b, SPEC §3.8's bouncer), where Φ_δ∘ζ must be replaced by the Binet scalar composed with the index map.
7. Rule R for this note: done (review A of the W chain). Rule L before any novelty claim (UNCHECKED). Still open for W on this family:
   second order in the poles; p < 1 (item 5; OBSTRUCTION for this route, JZC_W_kappa P K.14); p = 1/m; α ∉ (−1, 1); Rule R of
   JZC_W_exact WE.1 (fixed per Rule R review A of the W chain, B4).
