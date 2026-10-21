# JZC M3a, gap G3: the Hurwitz outer scalar for 0 < p < 1 (seams with j_δ), and Lemma H-d for p < 1

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_M3a_H_G3_A.md); fixes applied 2026-10-21.

Status (2026-10-21): NOT REVIEWED. Rule R needs the second reader to re-run the checks (VERIFICATION_POLICY.md Rule R); review A
did spot checks of its own but did not re-run the repo scripts, and the repo's practice (JZC_M4_proof.md, JZC_M1.md) is a second
reader before REVIEWED. Labels per VERIFICATION_POLICY.md. Closes (modulo review) gap G3 of
JZC_M3a_Hd.md §7. Setting: Hurwitz lattice λ_k = (k + δ)^p, k ≥ 1, **0 < p < 1, −1 < δ < 0** (δ = 0 is Paper 2), 1 < s < 1 + 2p
(fixed per Rule R review A, F8),
α = (s−1−p)/p, t = nz^{−1/p}, θ_δ := π(t − δ), κ_δ± := 1/(1 − e^{∓2iθ_δ}), j_δ(t) := LnΓ(t−δ) − (t−δ−½)ln t + t − ½ln 2π,
D̃_δ := e^{−j_δ(t)}, D_δ := κ_δ±D̃_δ. Everything quoted from Paper 2 is from papers/paper2/{sec_5,sec_6,app_outer}.tex.
External inputs (Paper 2 (eq. binet-bound), the reflection formula): primary quotes in RH/CITATIONS.md (DLMF) §5.11 and
(DLMF-5.5/5.11, Plan 54) (fixed per Rule R review A, F9).
Checks: `checks/m3a_g3_seam.py/.out` (81 assertions), `checks/m3a_g3_model.py/.out` (25 assertions).

| # | Statement | Label |
|---|---|---|
| Lemma 1 (uniqueness) | two outer scalars with the same (O1)_δ jump, (O2), (O5) near 0 and polynomial bounds at ∞ differ by a constant | PROVED (elementary) |
| Lemma 2 (monodromy) | any such F_δ is C(−z)^{δ+m}(1 + o(1)) at ∞ for some m ∈ ℤ, C ≠ 0, uniformly in arg z | PROVED (elementary) |
| Lemma 3 (seam_δ) | Paper 2 Lemma seam with j_δ and modified B_in, B_out: χ_δ exists, F_δ satisfies (O1)_δ–(O4), (O5) near 0 | PROVED-mod-cite (Paper 2), NOT REVIEWED |
| Prop 4 (= Prop 2.1 for p < 1) | F_δ = (2πn)^{−½−δ}(−z)^δ(1 + o(1)) at ∞; at 0 nothing new | PROVED-mod-cite (Paper 2), NOT REVIEWED; NUMERICAL (m3a_g3_seam) |
| Cor 5 (Lemma H-d, p < 1) | F♮ := F_δ(−z)^{−δ} gives M(β′ = α + 2δ, ν = α), band factor the seam H_n^δ | PROVED for the jump algebra (as H-d §3; H-d (i)–(iii) only, (iv) open: §7) (fixed per Rule R review A, F1), NOT REVIEWED; band-factor moments = the Fourier sums of H.md §3.2 (unconditional, via E_plt1 Lemma F.1 (ii)); their identification with ζ(−kp, 1+δ)/(kn^{kp}) is H.md Remark 3.3 (NOT QUOTED) (fixed per Rule R review A, F7) |
| Test | M(α+2δ, α) with Hurwitz μ reproduces all 22 stored p < 1 Hurwitz fit data; H2–H4 excluded | NUMERICAL (m3a_g3_model) |

## 0. Answer

Yes, with one modification. The H-d memo's expectation is literally right — with Paper 2's lattice B_in = (1+z)^ϖ,
B_out = (1 − z/2πn)^{1/2} the seam densities are χ^{lat}_± = (δ/p)Log ζ + c_± + o(1), c_± = lnΓ(1+δ) − δ ln n ∓ iπδ (§2, checked to
10⁻²⁴) — but then **Paper 2's seam integral (eq. chi) diverges** (log ζ/ζ is not integrable), so Lemma seam does not carry over
verbatim (OBSTRUCTION to the verbatim route). Re-balancing the two elementary factors (§2: exponents ϖ_δ, ½ + δ and a Möbius
factor fixing the constant) makes the densities decay at both ends as in Paper 2; then Lemma seam (iii), Lemma corner and all of
(O1)–(O4) go through verbatim, (O5) holds near 0 verbatim, and at ∞ the outer scalar is exactly (2πn)^{−½−δ}(−z)^δ(1 + o(1)).
The power is forced: by Lemma 1 every admissible outer scalar is this one up to a constant, so "the seam scalar and the full outer
scalar produce the same (−z)^δ" is a theorem, not a gauge choice. The exponent δ is p-free and equals the p > 1 one (H-d Prop 2.1).
Hence F♮ = F_δ(−z)^{−δ} satisfies (O1) with the lattice θ and (O5) at ∞, while (O2)–(O4) and (O5) near 0 hold for F_δ with κ_δ
(Lemma 3 (iii)), as in G12 P1.4; and Lemma H-d (i)–(iii) holds for p < 1 with the same proof (H-d (iv), the a-priori bound, is
open for p < 1: §7) (fixed per Rule R review A, F5, F1): the Hurwitz problem is M(β′ = α + 2δ, ν = α) in the n^p frame, band factor the seam H_n^δ.

## 1. Two structural lemmas (p-free)

(O1)_δ := (O1) with θ_δ: F analytic, zero-free in ℂ∖[0, ∞), continuous boundary values on (0, ∞)∖{X_k}, F₊ = F₋e^{2iθ_δ} on
(4c, ∞)∖{X_k}. Take the outer radius e^{pc₀}n^p > X₁ = (n/(1+δ))^p (H-d §6 item 6), so all nodes lie in 𝒵_n.

**Lemma 1 (uniqueness).** Let F₁, F₂ satisfy (O1)_δ, (O2) and the fixed-n bounds of (O5) near 0, and |F_i|^{±1} ≤ C|z|^N at ∞.
Then F₁/F₂ is a nonzero constant.
*Proof.* G := F₁/F₂ is analytic, zero-free on ℂ∖[0, ∞) and has no jump on (4c, ∞)∖{X_k} (equal jumps). On 𝒵_n, G² = F̃₁²/F̃₂² with
F̃_i² analytic and zero-free on 𝒵_n (O2), so G² extends analytically across (0, 4c], the nodes and (4c, e^{pc₀}n^p); beyond, there
are no nodes. So G² is analytic in ℂ∖{0}. Near 0, |G|^{±1} is bounded off the lens (O5) and G = F̃₁/F̃₂ is bounded above and below
in the lens (O5): 0 is removable and G²(0) ≠ 0. At ∞, |G²|^{±1} ≤ C|z|^{4N}, and the same for G^{−2} (fixed per Rule R review A, F3): G² is a polynomial without zeros, a
constant. ∎

**Lemma 2 (monodromy).** If F satisfies (O1)_δ and |F|^{±1} ≤ C|z|^N for large |z|, then F(z) = C_F(−z)^{δ+m}(1 + O(|z|^{−min(1,1/p)}log|z|) +
O(|z|^{−1})) (fixed per Rule R review A, F4) as z → ∞, uniformly in arg z, for some m ∈ ℤ and C_F ≠ 0 (principal power, cut [0, ∞)).
*Proof.* Fix R > X₁. On (R, ∞), t ∈ (0, 1+δ) is real, e^{2iθ_δ} = e^{2πit}e^{−2πiδ}, and ((−z)^{−δ})₊/((−z)^{−δ})₋ = e^{2πiδ}. Put
h(z) := ∫_R^∞ t(x)dx/(x − z) (t(x) = nx^{−1/p}, integrable against dx/x as 1/p > 0); by Sokhotski–Plemelj (t real-analytic),
h₊ − h₋ = 2πit. Then G := F(−z)^{−δ}e^{−h} has no jump on (R, ∞), none on (−∞, 0), and is analytic, zero-free and polynomially
bounded on |z| > R: an isolated singularity at ∞ that is a pole or removable, and zero-free, so G = C z^{m}(1 + O(1/z)) for some
m ∈ ℤ. Finally h = O(|z|^{−min(1,1/p)}log|z|) and z^m = (−z)^m(−1)^m. ∎

So the exponent of any admissible F_δ is δ mod 1 for every p > 0 (the H-d memo's "monodromy fixes it mod 1"); the integer m is
read off one explicit construction (§3) — no continuity in δ is needed.

## 2. The seam construction with j_δ (Lemma 3)

Paper 2's θ_seam = πp/2, S_in, S_out, Σ^s_± are unchanged. Put
  ϖ_δ := (1 − 1/p)(½ + δ),  λ_δ := (2π)^{1+δ}/(2|sin πδ|Γ(−δ)) = Γ(1+δ)(2π)^δ > 0  (second form: reflection formula, cosmetic),
  B_in^δ(z) := (1+z)^{ϖ_δ}·(1+z)/(1+λ_δz),  B_out^δ(z) := (1 − z/(2πn))^{½+δ}  (principal powers);
  χ_±^δ(ζ) := −j_δ(t) − Log(1 − e^{∓2πi(t−δ)}) + (ϖ_δ+1)Log(1+ζ) − Log(1+λ_δζ) − (½+δ)Log(1 − ζ/2πn) on Σ^s_±;
χ_δ by Paper 2 (eq. chi) with χ_±^δ, and F_δ := D_δB_in^δKe^{χ_δ} in S_in, B_out^δKe^{χ_δ} in S_out. At δ = 0: ϖ₀ = ϖ, λ₀ = 1, so
B_in^0, B_out^0, χ_±^0, F₀ are Paper 2's.

**Lemma 3.** Let 0 < p < 1, −1 < δ < 0. (i) D̃_δ is analytic and zero-free on S_in, D_δ on S_in ∩ ℂ_±. (ii) χ_±^δ is
real-analytic on the open seam, e^{χ_±^δ} = D_δB_in^δ/B_out^δ there, χ_−^δ(ζ̄) = conj χ_+^δ(ζ), and, with C = C(p, δ),
|χ_±^δ(ζ)| ≤ C|ζ| (|ζ| ≤ 1), χ_±^δ(ζ) = O(n|ζ|^{−1/p}log|ζ| + n|ζ|^{−1}) (ζ → ∞), |χ_±^δ| ≤ C(1 + log|ζ|) (|ζ| ≥ 1), |χ_±^δ′| ≤ C
(|ζ| ≤ 2). (iii) Paper 2 Lemma seam (iii), (iv) [(O1) with θ_δ; (O2)–(O4); (O5) near 0 and the polynomial bound at ∞] and Lemma
corner (ii), (iii) hold for χ_δ, F_δ (the polynomial bound at ∞ near the seams: (iii′) below); H_n^δ := (D̃_δB_in^δe^{χ_δ})^{−2}, H_n^δ(0⁺) = e^{−2χ_δ(0)}.

*Proof.* (i) Poles of Γ(t−δ): t = δ − m < 0, m ∈ ℕ₀, i.e. arg t = π, arg z = ∓πp ∉ S̄_in; on S_in |arg t| < π/2 and Re(t−δ) > 0.
|e^{∓2iθ_δ}| = |e^{∓2iθ}| < 1 in S_in ∩ ℂ_± (δ real; Paper 2 (eq. imtheta)).
(ii) Write j_δ(t) = j(t−δ) + r_δ(t), r_δ(t) := (t−δ−½)Log(1 − δ/t) + δ (identity of definitions). On Σ^s_+, t = −i|t|, and t−δ =
|δ| − i|t| has |arg(t−δ)| < π/2, |t−δ| ≥ |t|. *ζ → 0 (|t| → ∞):* Paper 2 (eq. binet-bound) at φ = π/2 gives |j(t−δ)| ≤ 1/(6|t|);
expanding Log(1 − δ/t) gives |r_δ(t)| ≤ C_δ/|t| for |t| ≥ 2; |e^{−2πi(t−δ)}| = e^{−2π|t|}; the elementary Logs are O(|ζ|). Hence
|χ_+^δ| ≤ C|ζ|^{1/p}/n + C|ζ| — Paper 2's bound. *ζ → ∞ (t → 0):* j(t−δ) is analytic at t = 0 (Re(−δ) > 0) and
r_δ(t) = (δ+½)Log t + (−δ−½)Log(−δ) + δ + O(|t|log(1/|t|)); together −j_δ(t) = −(δ+½)Log t − LnΓ(−δ) + ½ln 2π + O(|t|log(1/|t|))
(definition of j at −δ). Next 1 − e^{2πiδ} = 2|sin πδ|e^{i(π/2+πδ)} with π/2 + πδ ∈ (−π/2, π/2), so −Log(1 − e^{−2πi(t−δ)}) =
−ln(2|sin πδ|) − i(π/2 + πδ) + O_δ(|t|) (the Log is continuous on the seam: |e^{−2πi(t−δ)}| < 1). With Log t = ln n − (1/p)Log ζ,
Log(1+ζ) = Log ζ + O(1/ζ), Log(1+λζ) = ln λ + Log ζ + O(1/ζ), Log(1 − ζ/2πn) = Log ζ − ln 2πn − iπ + O(n/ζ) (arg(−ζ/2πn) =
πp/2 − π): coefficient of Log ζ: (δ+½)/p + ϖ_δ + 1 − 1 − (½+δ) = 0; constant: −LnΓ(−δ) + ½ln 2π − (δ+½)ln n − ln(2|sin πδ|)
− i(π/2+πδ) − ln λ_δ + (½+δ)(ln 2πn + iπ) = −LnΓ(−δ) + (1+δ)ln 2π − ln(2|sin πδ|) − ln λ_δ = 0. Hence the decay. The bound for
|ζ| ≥ 1 and the derivative bound: Paper 2 Lemma corner (i)'s argument verbatim, with j_δ = j(t−δ) + r_δ and |1 − qe^{2πiδ}| ≥
s_δ > 0 for q ∈ [0, 1] (better than Paper 2's log). Symmetry: t(ζ̄) = conj t(ζ), j_δ real on (0, ∞).
(iii) Paper 2's proofs of Lemma seam (iii), (iv) and Lemma corner (ii), (iii) use only the bounds in (ii), the analyticity in (i),
and of B_in, B_out: analytic, zero-free in S_in resp. S_out, → 1 at 0 with |log| ≤ C|z|, |log| ≤ C(1 + log|z|) at ∞ (B_in^δ: zero −1
and pole −1/λ_δ lie in S_out; Re(λ_δz) > 0 on S_in so |1 + λ_δz| ≥ 1; positive on (0, ∞)). These hold. Only (O5) "F(iy) bounded and
bounded away from 0" is replaced, by Prop 4. ∎

*Addendum to Lemma 3 (ii), (iii) (fixed per Rule R review A, F2).* Paper 2's proof of Lemma seam (iv) only asserts that e^χ is
bounded above and below by powers of |z| in S_in ∩ {|z| ≥ n^p+δ′}; Lemma 2 needs this on a full neighbourhood of ∞, including
points near the seams.
- (ii′) For |ζ| ≥ 1, |χ_±^δ′(ζ)| ≤ C_n/|ζ|. Proof: dt/dζ = −t/(pζ); d/dt[j_δ + Log(1 − e^{−2πi(t−δ)})] = O(1/|t|) for |t| ≤ 2
  (L1.2(c) type: j_δ′ = (δ+½)/t + O(1 + |ln|t||)) and O(|t|^{−2}) for |t| ≥ 2; the elementary terms have derivatives O(1/|ζ|).
- (iii′) For fixed n, χ_δ is bounded on {|z| ≥ 2} uniformly up to the seams. Proof: for z near Σ^s_+ with nearest point z*,
  r = |z*|, split the Σ^s_+ integral at |ζ − z*| ≤ r/2. On the window, χ_+(ζ) = χ_+(z*) + O(|ζ − z*|C_n/r) by (ii′). The
  constant part times a logarithm with end points at comparable distances is bounded, since χ_+(z*) → 0. The Lipschitz part is
  O(C_n). Off the window, |ζ − z| ≥ (|ζ| + r)/C, and χ_+(ζ)/ζ is integrable. Σ^s_− is at distance ≥ |z|/C. Hence
  |F_δ|^{±1} ≤ C_n|z|^{N_n} for |z| ≥ X₁ + δ′.

*Reused verbatim:* Lemma seam (iii), (iv)[(O1)–(O4), (O5) near 0], Lemma corner (ii), (iii), E_plt1 Lemma F.1 (i), (ii) (with
ℓ_± := −Log(1 − e^{±2πiδ}e^{−2πnr^{−1/p}}), as in SPEC §3.1 p < 1). *Modified (proved above):* Lemma seam (i), (ii), Lemma corner
(i) (constants depend on δ), the elementary factors, and (O5) at ∞.

## 3. Prop 4 (the p < 1 Prop 2.1)

**Prop 4.** F_δ(z) = (2πn)^{−½−δ}(−z)^δ(1 + o(1)) as z → ∞, uniformly in arg z; F_δ satisfies (O5) near 0, and F_δ(z) →
(4c)^{−1/2}e^{χ_δ(0)} as z → 0 off the lens (as Paper 2's F) (near the seams: boundedness by Lemma corner (iii), and the limit
by Lindelöf's theorem on the sector between two rays at distance τ₀|z| from Σ^s_±) (fixed per Rule R review A, F6).
*Proof.* χ_±^δ/ζ is integrable on the seams (Lemma 3 (ii)), so χ_δ(z) → 0 as z → ∞ with dist(z, seams) ≥ τ|z| (dominated
convergence). In S_out, B_out^δK = (−z/2πn)^{½+δ}(−z)^{−½}(1 + O(1/z)) with consistent principal branches (arg(−z) ∈ (−π + πp/2,
π − πp/2)), giving the claim along every ray in S_out. F_δ satisfies (O1)_δ and polynomial bounds (Lemma 3 (iii), (iii′); fixed per Rule R review A, F2), so by Lemma 2
F_δ = C_F(−z)^{δ+m}(1 + o(1)) uniformly; comparing on one S_out ray, m = 0, C_F = (2πn)^{−½−δ}. Near 0: Lemma 3 (iii). ∎

So the seam scalar χ_δ itself produces no power at ∞ (χ_δ → 0): with the re-balanced elementary factors the whole (−z)^δ sits in
B_out^δK. In Paper 2's lattice gauge it would sit in the seam densities as (δ/p)log ζ (§0), which the Cauchy integral cannot carry.
Uniqueness (Lemma 1) makes the two descriptions the same function wherever both are defined; the constant C_δ is construction-
dependent but enters only through 𝗐_nH_n(0⁺), which cancels in ω (Paper 2, remark after Lemma seam).

## 4. Cor 5: Lemma H-d for p < 1, and the band factor

**Cor 5.** For 0 < p < 1, −1 < δ < 0, Lemma H-d (i)–(iii) of JZC_M3a_Hd.md §3 holds with F_δ of §2 (fixed per Rule R review
A, F1: H-d (iv), the a-priori bound, is not proved here for p < 1; see §7).
*Proof.* H-d §3's proof uses: (O1)_δ; F_δ ~ C_δ(−z)^δ at ∞ (now Prop 4); no jump on (−∞, 0) (Lemma 3 (iii)); Paper 2's
jumpsV algebra (geometry-free); Lemma normalisation (ϰ_∞ = F♮^{−1}e^{n(g − Log z)} has no jump on (R, ∞) or (−∞, 0), n ∈ ℤ, and
tends to C_δ^{−1}: removable at ∞, nonzero); lips, saturated regions and Σ_v inside 𝒵_n ⊂ S_in (θ_w = 3πp/8 < πp/2), where F_δ =
D_δB_in^δKe^{χ_δ} has the same κ_δ structure as for p > 1. ∎ (The former "(iv) …" clause is deleted, fixed per Rule R review A, F1.)
*Band factor.* By E_plt1 Lemma F.1 (ii) (verbatim, densities ℓ_±), 𝒢_δ(z) − 𝒢_δ(1) is the Cauchy integral of the pure jump, with
moments = the Fourier sums of H.md §3.2 (unconditional, via E_plt1 Lemma F.1 (ii)); their identification with
ζ(−kp, 1+δ)/(kn^{kp}) is H.md Remark 3.3 (NOT QUOTED; NUMERICAL to 2·10⁻¹⁶) (fixed per Rule R review A, F7); μ_{n,k} = 2m_k(δ)
as for p > 1; F.1 (iv)'s remainder bound was not re-derived for complex ℓ_± (expected verbatim: |ℓ_±| is
bounded at ∞ and super-small at 0).

## 5. Numerical evidence (NUMERICAL)

`checks/m3a_g3_seam.out` (dps 25 + extra digits in j_δ for |t| ≫ 1; n = 4, c = 1; p ∈ {0.3, 0.6, 0.75} × δ ∈ {−0.25, −0.5, −0.8}):
- (B) densities: |χ_+^δ(10⁻⁶e^{iπp/2})| ≤ 6·10⁻⁷, |χ_+^δ(10⁴⁰e^{iπp/2})| ≤ 2·10⁻²⁴ (working-precision floor); lattice-B densities:
  |χ^{lat}_+ − (δ/p)Log ζ − c_+| ≤ 5·10⁻²⁴ at |ζ| = 10⁴⁰ (the §0 constant c_+ = lnΓ(1+δ) − δ ln n − iπδ); λ_δ's two forms agree.
- (C) gluing across Σ^s_+ at |ζ| = 2, 2000: |F_in/F_out − 1| ≤ 2.2ε for ε = 10⁻⁴, 10⁻⁶ (O(ε), as for a continuous function).
- (D) ∞, five rays arg z ∈ {±πp/4 (S_in), π/2, 3π/4, −0.95π (S_out)}: |F_δ(z)(−z)^{−δ}/(2πn)^{−½−δ} − 1| ≤ 7·10⁻¹⁴ at |z| = 10¹⁴;
  exponent of |F_δ| fitted between 10¹⁰ and 10¹⁴: δ to ≤ 7·10⁻¹¹ (all 9 (p, δ); asserted 10⁻⁸).
- (E) 0: |F_δ(10⁻⁸e^{iφ})/((4c)^{−½}e^{χ_δ(0)}) − 1| ≤ 2·10⁻⁹ for φ = 0.45πp (S_in, off the lens) and π/2 (S_out).
- (F) Lemma F.1 (ii)_δ: 𝒢_δ(z) − 𝒢_δ(1) = pure-jump Cauchy integral at 4 points (S_in, (0, 1), S_out, ℂ₋) to ≤ 6·10⁻²⁶.
81 assertions, all pass. Exploratory (not asserted): χ_δ(0) at δ = −½ equals (p/2)ln 2 to the printed digits (p = 0.3, 0.6, 0.75).

`checks/m3a_g3_model.out` (m4_rh4, KORD = 4, dps 40; data provenance as in m3a_hd_model, Rule X: fits of the actual Hurwitz
measures by spec_hur.py, spec_hur_d2.py, spec_hur_small.py; nothing fitted here). All 22 stored p < 1 data (11 with −1 < δ ≤ 0:
p = 0.6, ⅓, ¼ at δ = −½; 11 at δ = ½, 1, outside the range) are reproduced by M(α+2δ, α) within max(3·half-range, floor),
worst 0.07 tol (d₁ exact; e.g. n^{−2} at p = 0.6, δ = −½: +0.042222 vs fit +0.042227 ± 6·10⁻⁴; merged n^{−2} at p = ⅓:
−0.819444 vs −0.819479). Alternatives on p < 1 data: H2 (α+2δ, α+2δ) 3 009 tol, H3 (α, α+2δ) 53 192 tol, H4 (α+δ, α) 26 596 tol.
These rows were already among H-d's 36 (no new p < 1 Hurwitz fit data exist in checks/spec_hur*.out); the new content is that the
p < 1 band factor they test is now the seam one of §2. p = 0.3, 0.75 at δ < 0 have no stored fits.

## 6. Rule A (adversarial pass) — log

1. *Verbatim reuse of Lemma seam with j_δ.* Fails: densities ~ (δ/p)log ζ, Paper 2's χ integral diverges (checked: §0 constant to
   10⁻²⁴). A regularised kernel 1/(ζ−z) − 1/(ζ+1) would converge but produces log² terms per ray; re-balancing B_in, B_out is cleaner.
2. *Constant at ∞ vs at 0.* A pure power rescaling cannot kill c_δ when ϖ_δ = 0 (δ = −½: B_out^δ ≡ 1, ϖ_δ = 0, c_{−½} = −½ln 2 ≠ 0);
   hence the Möbius factor. δ = −½ is in the numerics.
3. *δ → −1⁺:* λ_δ → ∞, pole −1/λ_δ → 0⁻ (still in S_out); constants of Lemma 3 grow like λ_δ; fixed δ fine (δ = −0.8: λ ≈ 1.06).
4. *δ → 0⁻:* O_δ(|t|) remainders carry 1/|sin πδ| (the p > 1 crossover, H-d §3); λ_δ → 1, C_δ → (2πn)^{−1/2}: continuous limit.
5. *Could m ≠ 0 with another construction?* No: Lemma 1. *Converse of Lemma 2:* not used.
6. *Sign of the power:* monodromy e^{−2πiδ} on (R, ∞) matches (−z)^δ (cut [0, ∞)), not z^δ (cut (−∞, 0], where F has no jump).
7. *Hidden jumps:* B_out^δ's cut [2πn, ∞) ⊂ S_in and B_in^δ's singularities ⊂ S_out are never used; the seam Logs are continuous
   (|e^{∓2πi(t−δ)}| < 1). Gluing checked numerically (§5).
8. *Is H_n^δ changed by the Möbius factor?* Only through χ_δ, which compensates: (F) in §5 shows 𝒢_δ − 𝒢_δ(1) equals the pure-jump
   Cauchy integral, independent of the choice of B's (Lemma 1).
9. *Paper 2 wording gap, Lemma seam (iv), (O5) at ∞* (from Rule R review A, F2): app_outer.tex, last lines of (O5), says "In
   S_in ∩ {|z| ≥ n^p+δ′} … D, B_in, K and e^χ are bounded above and below by powers of |z|"; for e^χ this is not justified there
   (Lemma corner (ii) gives only |χ − χ(0)| ≤ C(1 + log|z|)², and only at distance ≥ τ|z| from the seams). The claim is true
   (Lemma 3 (ii′), (iii′)); Paper 2's result is unaffected. Record for math-pursuits FIXES via a human (AGENTS.md Rule 1).

## 7. What remains

- Rule R second reader for Lemmas 1–3, Prop 4, Cor 5 (review A applied, see header). E_plt1 Lemma F.1 (iv) with complex ℓ_±
  (expected verbatim).
- H-d (iv) (a-priori bound) for p < 1: open (expected from G12 L2.1 (p-free), L2.2, L2.3 and P2.4 with Lemma 3 (iii) for (O3)–(O5)
  near 0 and Prop 4 at ∞) (fixed per Rule R review A, F1). This is gap 2 of JZC_M3a_H.md §4, being worked on in
  JZC_M3a_H_G23plt1.md (in progress).
- Inherited from H-d: G2 (App C, Lemma sumbound for the Hurwitz U), G4 (Hurwitz's formula, DLMF 5.11.8 — the latter is no longer
  used here: Lemma 3 uses only Paper 2's (eq. binet-bound) via j_δ = j(t−δ) + r_δ), G5 (Theorem N.6 for M(β, ν)).
- δ > 0 (phantom nodes) and p = 1 with δ ≠ 0 are not treated. No stored p < 1 fits at p = 0.3, 0.75 for δ < 0; d₃-level p < 1 data none.
