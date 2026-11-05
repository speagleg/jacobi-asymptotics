# JZC M3a, step H-a of Theorem H: the interpolation problem for the Hurwitz lattice

Rule R review A: ACCEPT WITH FIXES (research/G1/review/REVIEW_JZC_M3a_H_pgt1_chain_A.md); fixes applied 2026-10-21.
Status (2026-10-21): **REVIEWED** (Rule R: independent second reader A re-derived L Ha.1–P Ha.5 and the contour and re-ran
m3a_ha_interp.py, byte-identical output; fixes Ha-1–Ha-3 and C-1 applied). Labels per VERIFICATION_POLICY.md. Closes item 4 of
JZC_M3a_H.md §4, step H-a of its §2 table. Setting: −1 < δ ≤ 0, a := 1 + δ ∈ (0, 1], p > 0, p ≠ 1, 1 < s < 1 + 2p,
α := (s−1−p)/p ∈ (−1, 1), n ≥ 1 (n ≥ n₀ where stated). Both p > 1 and 0 < p < 1 are covered; δ = 0 is Paper 2 verbatim.
Check: `checks/m3a_ha_interp.py/.out` (298 assertions and 33 controls; every control fails as required; ALL 298 CHECKS PASSED).
Everything attributed to Paper 2 is quoted from papers/paper2/{sec_2,sec_5,sec_6,app_c}.tex as read for this note (read-only).
In Paper 2's numbering, Lemma interp is Lemma 5.1 and Lemma invariance is Lemma 5.2 (`\newtheorem{lemma}[theorem]`, numbered
within sections; they are the first two numbered statements of §5).

| # | Statement | Label |
|---|---|---|
| L Ha.1 | node set: in ℂ∖(−∞,0] the zeros of 1 − e^{2iθ_δ} are t ∈ δ + ℤ. The Hurwitz nodes are t = δ + k (k ≥ 1). The other zeros t = δ − m (m ≥ 0) do not occur for p > 1, and for p < 1 they lie on arg z = ±πp, outside 𝒵_n, the lens sector and S_in. Γ-factorisation of sin π(t−δ) | PROVED-mod-cite (DLMF 5.5.3 via Paper 2 T4) |
| L Ha.2 | interpolation lemma (Paper 2 L5.1) for σ^δ: poles X_k = (n/τ_k)^p, residues n^pτ_k^{−s}U_{j1}(X_k), expansion for \|z\| > X₁ = (n/a)^p, (eq:extractU), (eq:U-sum) | PROVED-mod-cite (Paper 2 T1(a), L5.1, L5.2 proofs; hypothesis x_k ≤ 1 removed) |
| L Ha.3 | uniqueness: the interpolation problem (Y1)–(Y3), (Y4′) for σ^δ has exactly one solution, (eq:Y-solution) | PROVED (elementary) |
| L Ha.4 | node masses: Res_{X_k} W/(e^{2iθ_δ} − 1) = Res_{X_k} we^{−iθ_δ}/Π_δ = w(X_k) = n^pτ_k^{−s}; no other poles in 𝒵_n | PROVED |
| P Ha.5 | Step 1 with κ_δ: R is continuous at every node ⇔ the residue conditions of L Ha.2. So the RH problem for R, which has jumps on Σ only, is equivalent to the interpolation problem, and by L Ha.3 to the OPs of σ^δ | PROVED |
| Contour | top segment at X₁ + δ′, c₀ := 1 + log(1/a), 𝒵_n ⊃ the closure of Ω_b ∪ Ω_sat for n ≥ n₀(p) | PROVED (bookkeeping) |
| Check | residues, node masses, Laurent radius X₁, extraction, zero counts, pole removal; controls | NUMERICAL |

Novelty: UNCHECKED (the content is a routine adaptation of Paper 2 §5 and is not claimed as new).

## 0. Setting, and what is quoted

σ^δ := Σ_{k≥1}τ_k^{−s}δ_{x_k}, τ_k := k + δ, x_k := τ_k^{−p} ∈ (0, a^{−p}], w_k := τ_k^{−s} > 0, Σw_k = Σ_k(k+δ)^{−s} < ∞ (s > 1), and
the x_k are distinct with infinitely many of them. Rescaled nodes X_k := n^px_k = (n/τ_k)^p, so **the top node is X₁ = (n/a)^p ≥ n^p**,
with equality only at δ = 0. Pure power: ℓ₁ ≡ 1, so Paper 2's hypothesis (A_ϑ) holds for every ϑ and c₀, and we fix c₀ := 1 + log(1/a)
(as in G12 §0).

Quoted from Paper 2 (verbatim or exact paraphrase):
- **T1(a)** (sec_2): "Let σ = Σ_{k≥1}w_kδ_{x_k} with distinct nodes x_k ∈ (0,1], w_k > 0 and Σ_kw_k < ∞, and fix n ≥ 1." Y := (eq:Y-solution)
  = [[P_n(z), Σ_k w_kP_n(x_k)/(z−x_k)], [h_{n−1}^{−1}P_{n−1}(z), h_{n−1}^{−1}Σ_k w_kP_{n−1}(x_k)/(z−x_k)]]. "Then Y is analytic in
  ℂ∖({x_k}_k ∪ {0}); at each node it has a simple pole with Res_{z=x_k}Y(z) = lim_{z→x_k}Y(z)(0 w_k; 0 0) …; and
  Y(z)z^{−nσ₃} = I + Y₁/z + Y₂/z² + O(z^{−3}) as z → ∞", with (eq:Y-extract) (Y₁)₁₂(Y₁)₂₁ = b_n², (Y₂)₁₂/(Y₁)₁₂ − (Y₁)₂₂ = a_n.
  The proof there is self-contained: "For |z| > 2, expanding (z−x)^{−1} gives Σ_kw_kP_m(x_k)/(z−x_k) = Σ_{i≥0}z^{−i−1}∫P_mx^i dσ".
- **Lemma interp (L5.1)**, (eq:U) U(z) := n^{pnσ₃}Y(zn^{−p}); "analytic off {X_k}_{k≥1} ∪ {0}, where X_k := n^px_k = (n/k)^p (k ≥ 1),
  X₁ = n^p (the top node); it has simple poles at the X_k in its second column only, with Res_{z=X_k}U_{j2} = n^pw_kU_{j1}(X_k)
  (j = 1, 2); and U(z)z^{−nσ₃} = I + U₁/z + U₂/z² + … for |z| > n^p", with (eq:extractU) 𝖻(Uz^{−nσ₃}) = n^{2p}b_n²,
  𝖺(Uz^{−nσ₃}) = n^pa_n. Its proof: det Y ≡ 1 by orthogonality; the rest "by the substitution z = n^pζ" and Lemma invariance.
- **Lemma invariance (L5.2)**: for scalar k = k_∞(1 + k₁/z + …), k_∞ ≠ 0, k_∞^{−σ₃}Xk^{σ₃} has the same 𝖺, 𝖻. (No measure enters.)
- (eq:t) t(z) := nz^{−1/p} (principal); "t(X_k) = k"; (eq:theta) θ := πt, Π := sin θ/θ′, θ′ = −(π/p)t/z; (eq:imtheta) "±Im θ(z) < 0 for
  0 < ±arg z < min(π, πp), |e^{∓2iθ(z)}| = exp(−2πn|z|^{−1/p}sin(|arg z|/p))"; (eq:w-rn) w(z) := n^pt(z)^{−s}ℓ₁(t(z)); "By Lemma interp,
  Res_{X_k}U_{j2} = w(X_k)U_{j1}(X_k)"; (eq:W) W := 2iθ′w; Lemma bandweight W = 𝗐_nz^αr_n.
- (eq:Zn) 𝒵_n := {0 < |z| < e^{pc₀}n^p, |arg z| < ϑ_w}; (eq:thetaw) ϑ_w = 7π/16 (p ≥ 1), 3πp/8 (p < 1) (default; times 𝗆 ≤ 1).
- (eq:kappa) κ_± := 1/(1 − e^{∓2iθ}), κ_± − 1 = e^{∓2iθ}κ_±; (eq:LA) L_± := (1, ∓We^{∓2iθ}κ_±; 0, 1), A^△_± := (1, 0; ∓1/(κ_±W), 1);
  (eq:R) R := U in Ω_∞, UL_± in Ω_b^±, UA^△_±κ_±^{σ₃} in Ω_sat±. Step 1: "near X_k all factors are meromorphic, and
  1 − e^{∓2iθ} = ±2iθ′(X_k)(z−X_k)(1 + O(z−X_k)) because e^{2iθ(X_k)} = 1 …".
- §frame-contour: "the saturated segment (4c, n^p+δ′) and the top segment Σ_top := {n^p+δ′+iy: 0 < |y| ≤ h₀}. The top node X₁ = n^p
  lies inside, and no node lies on [n^p+δ′, ∞)"; "|z| ≤ n^p+δ′+h₀ < e^{pc₀}n^p for n ≥ n₀".
- (eq:U-sum) (app_c) U_{j2}(z) = Σ_{k≥1}w(X_k)U_{j1}(X_k)/(z − X_k), w(X_k) = n^pw_k.
- Lemma lenssector's proof (app_c): "e^{2iθ} = 1 only where t ∈ ℤ, i.e. at the nodes (the points with t ∈ −ℕ have |arg s| = πp > ϑ_lip)".
- **T4** (sec_2), Gamma function: "(5.5.1) Γ(z+1) = zΓ(z); (5.5.3) Γ(z)Γ(1−z) = π/sin(πz), z ∉ ℤ". §6 intro: "The node masses carry
  the factor 1/Γ(t) through Π = sin θ/θ′", D̃ = e^{−j(t)} = √(2π)t^{t−1/2}e^{−t}/Γ(t).

Hurwitz data: θ_δ := π(t − δ), so θ_δ′ = θ′; κ_δ± := 1/(1 − e^{∓2iθ_δ}); Π_δ := sin θ_δ/θ′; L^δ_±, A^{△δ}_± := (eq:LA) with θ_δ, κ_δ;
w(z) := n^pt^{−s} (ℓ₁ ≡ 1, r_n ≡ 1), W := 2iθ′w = 𝗐_nz^α exactly (Lemma bandweight; δ does not enter W).

## 1. The node set (Lemma Ha.1)

**Lemma Ha.1.** Let p ≠ 1. On ℂ∖(−∞,0]:
(i) 1 − e^{2iθ_δ(z)} = 0 iff t(z) ∈ δ + ℤ. Every zero is simple, with d/dz(e^{2iθ_δ}) = 2iθ′e^{2iθ_δ} ≠ 0.
(ii) *Nodes.* The zeros with t ∈ δ + ℕ (t = τ_k, k ≥ 1) are exactly z = X_k ∈ (0, X₁]. The largest is X₁ = (n/a)^p. No zero lies on
  (X₁, ∞), because no point of δ + ℤ lies in (0, a). In particular t = δ (k = 0) is never a node: for δ < 0 it is negative, and for δ = 0 it
  is t = 0, which corresponds to z = ∞.
(iii) *Non-nodes t = δ − m, m ≥ 0 (t ≤ 0, t ≠ 0).*
  - p > 1: arg t = −arg z/p ∈ (−π/p, π/p) ⊂ (−π, π), so t ∉ (−∞, 0]. There are no non-nodes.
  - p < 1: t ∈ (−∞, 0) iff arg z = ±πp, and then |z| = (n/(m − δ))^p (m ≥ 0 for δ < 0, m ≥ 1 for δ = 0). The angle πp is larger than
    ϑ_w ≤ 3πp/8 (𝒵_n), than (5/4)ϑ_lip ≤ 5πp/16 (lens and the sectors near 0), and than πp/2 (S_in, where D̃_δ is used).
  So in 𝒵_n, and in every sector |arg z| < φ with φ < min(π, πp), the zero set of 1 − e^{2iθ_δ} is exactly {X_k}_{k≥1}.
(iv) *Γ-factorisation.* For t − δ ∉ ℤ, sin π(t − δ) = π/(Γ(t − δ)Γ(1 − t + δ)). So Π_δ = π/(θ′Γ(t−δ)Γ(1−(t−δ))). The nodes are the zeros of
  1/Γ(1 − (t−δ)) (t − δ = k ≥ 1). The non-nodes are the zeros of 1/Γ(t − δ) (t − δ = −m). The outer factor
  D̃_δ = e^{−j_δ(t)} = √(2π)t^{t−δ−½}e^{−t}/Γ(t − δ) (definition of j_δ, G12 §1) vanishes exactly at the non-nodes. It is used only where
  t − δ ∉ (−∞, 0]: for p > 1, everywhere (G12 L1.1); for p < 1, in S_in, where Re t > 0. There it is analytic and zero-free.

*Proof.* (i) e^{2iθ_δ} = e^{2πi(t−δ)} = 1 iff t − δ ∈ ℤ. (ii) t(z) > 0 iff z > 0, and t is a decreasing bijection (0, ∞) → (0, ∞) with
t(X_k) = nX_k^{−1/p} = τ_k. The positive points of δ + ℤ are δ + k, k ≥ 1, because δ ≤ 0 < 1 + δ. (iii) arg t = −arg z/p on ℂ∖(−∞,0]
((eq:imtheta) context), and |arg z| < π. The bounds on ϑ_w, ϑ_lip are (eq:thetaw)/(eq:angles) for p < 1 (𝗆 ≤ 1). (iv) DLMF 5.5.3 (T4)
with z = t − δ. The formula for D̃_δ is e^{−j_δ} written out. Re t > 0 on S_in = {|arg z| < πp/2} because |arg t| < π/2, and then
Re(t − δ) ≥ Re t > 0. ∎ (PROVED-mod-cite: DLMF 5.5.3 as quoted in Paper 2 T4. Numerical evidence: argument-principle counts, §5.) (fixed per Rule R review A of the p>1 chain, Ha-3)

This is the check asked for: the points t = δ − m, m ≥ 0, are not nodes, and they do not lie in any sector that the frame uses.
For p > 1 they do not exist at all. Paper 2's lattice remark ("the points with t ∈ −ℕ have |arg s| = πp > ϑ_lip") becomes "the points
with t ∈ δ − ℕ₀". The only new point is t = δ (m = 0). It lies on the same rays, at |z| = (n/|δ|)^p (which is > X₁ only for δ > −½; for δ ≤ −½ it
lies between n^p and X₁), on the rays arg z = ±πp, outside 𝒵_n, the lens and S_in; so it is in Ω_∞, where κ_δ is not used
(fixed per Rule R review A of the p>1 chain, Ha-1).

## 2. The interpolation lemma (Lemma Ha.2 = Paper 2 L5.1 for σ^δ)

**Lemma Ha.2.** Let n ≥ 1 and Y := (eq:Y-solution) for σ^δ. Then:
(a) det Y ≡ 1, and Y is analytic in ℂ∖({x_k} ∪ {0}). At each x_k it has a simple pole with Res_{x_k}Y = lim Y(z)(0 w_k; 0 0). Also
  Y(z)z^{−nσ₃} = I + Y₁/z + Y₂/z² + …, convergent for **|z| > x₁ = a^{−p}**, and (eq:Y-extract) holds.
(b) U := n^{pnσ₃}Y(zn^{−p}) is analytic off {X_k} ∪ {0}. Its first column is polynomial. It has simple poles at the X_k in its second
  column only, with
  Res_{z=X_k}U_{j2} = n^pw_kU_{j1}(X_k) = w(X_k)U_{j1}(X_k),  w(X_k) = n^pτ_k^{−s} (j = 1, 2),
  and U_{j2} = Σ_k w(X_k)U_{j1}(X_k)/(z − X_k) ((eq:U-sum)). Also U(z)z^{−nσ₃} = I + U₁/z + U₂/z² + … for **|z| > X₁ = (n/a)^p**, and
  𝖻(Uz^{−nσ₃}) = n^{2p}b_n², 𝖺(Uz^{−nσ₃}) = n^pa_n ((eq:extractU)), where a_n, b_n are the recurrence coefficients of σ^δ.

*Proof.* T1(a) requires x_k ∈ (0,1]. That fails for δ < 0, since x₁ = a^{−p} > 1. Its proof uses x_k ≤ 1 at exactly one point: the
expansion of (z − x)^{−1} for |z| > 2. With x_k ∈ (0, x₁] the same expansion holds for |z| > x₁. For fixed i, Σ_kw_k|P_m(x_k)|x_k^i ≤
x₁^i·max_{[0,x₁]}|P_m|·Σ_kw_k, so Σ_kw_kP_m(x_k)/(z−x_k) = Σ_{i≥0}z^{−i−1}∫P_mx^i dσ^δ converges absolutely and locally uniformly
on |z| > x₁. The rest of T1(a)'s proof uses only w_k > 0 and Σw_k < ∞: local uniform convergence of the sums off {x_k} ∪ {0}, the residues,
and the moment identities ∫P_mx^i dσ = 0 (i < m), h_m (i = m), −π_{m+1}h_m (i = m+1). So it holds verbatim. In particular h_m > 0
for all m, because σ^δ has infinitely many support points. The determinant argument of L5.1 uses only orthogonality. The statements for U
follow from the substitution z = n^pζ, which maps the circle |ζ| = x₁ to |z| = n^px₁ = X₁. The extraction identities follow by L5.2,
which does not involve the measure. (eq:U-sum) is the definition of Y₁₂, Y₂₂ rescaled: n^{±pn} and n^p (from 1/(ζ − x_k) = n^p/(z − X_k))
go into U_{j1}(X_k) and w(X_k). ∎ (PROVED-mod-cite: the proofs of Paper 2 T1(a), L5.1, L5.2, re-checked line by line with x_k ≤ x₁.)

*Top node.* The only change from Paper 2 is X₁ = (n/a)^p in place of n^p. This affects three things. (1) The Laurent expansion at ∞
holds for |z| > X₁, and not on n^p < |z| < X₁ when δ < 0: the pole X₁ lies there. (2) The top node's mass is w(X₁) = n^pa^{−s}. It is
large as δ → −1, but for fixed δ it is a constant times n^p, as for every node. (3) The contour must reach past X₁ (§4). Numerically
(§5), the Laurent coefficients of U₁₂z^n have ratio → X₁, not n^p. Extraction on |z| = 2X₁ reproduces n^{2p}b_n² and n^pa_n to 3·10⁻²⁵ relative.
The same extraction on the circle |z| = (n^p + X₁)/2, which lies outside the lattice top node but inside X₁, is off by O(1) (control).

## 3. Uniqueness (Lemma Ha.3): the interpolation problem determines the OPs

Paper 2 does not use uniqueness ("We never use that Y is the unique solution of an interpolation problem"), and nothing downstream
needs it. It is recorded here because H-a asks that "the RH problem for σ^δ" be equivalent to the interpolation problem. Near 0 the
nodes accumulate, so the usual growth condition at the poles cannot be imposed at 0. We replace it by the structural condition (Y4′).

**Interpolation problem IP^δ_n.** Find a 2×2 matrix function Y with:
(Y1) Y is analytic in ℂ∖({x_k} ∪ {0});
(Y2) Res_{x_k}Y = lim_{z→x_k}Y(z)(0 w_k; 0 0) for every k. That is, the first column is analytic at x_k, and the second column has at most a
  simple pole there, with residue w_kY_{j1}(x_k);
(Y3) Y(z)z^{−nσ₃} = I + O(1/z) as z → ∞;
(Y4′) Y_{j1} extends to an entire function, and there are numbers r_{jk} with Σ_k|r_{jk}| < ∞ such that Y_{j2}(z) − Σ_k r_{jk}/(z − x_k)
  extends to an entire function (j = 1, 2) (fixed per Rule R review A of the p>1 chain, Ha-2). (The former (Y4) had r_{jk} = w_kY_{j1}(x_k) built in, so it implied (Y2) and
  made the "Consequently" of P Ha.5 vacuous.)

**Lemma Ha.3.** For n ≥ 1, IP^δ_n has exactly one solution, namely (eq:Y-solution) built from the monic OPs of σ^δ.

*Proof.* Existence: Lemma Ha.2(a). (Y4′) holds with r_{jk} = w_kY_{j1}(x_k) and both differences ≡ 0. Uniqueness: let Y solve IP^δ_n.
By (Y2), r_{jk} = w_kY_{j1}(x_k) (fixed per Rule R review A of the p>1 chain, Ha-2). By (Y4′),
C_j(z) := Σ_kw_kY_{j1}(x_k)/(z − x_k) converges, is analytic off {x_k} ∪ {0} and is O(1/z). By (Y3), Y₁₁ = z^n(1 + O(1/z)) and
Y₂₁ = O(z^{n−1}). Since they are entire, Cauchy's estimates make Y₁₁ a monic polynomial of degree n and Y₂₁ a polynomial of degree
≤ n − 1. E_j := Y_{j2} − C_j is entire. By (Y3), Y₁₂ = O(z^{−n−1}) and Y₂₂ = O(z^{−n}), so E_j = O(1/z) (n ≥ 1), and E_j ≡ 0 by
Liouville. Hence Y_{j2} = C_j = Σ_{i≥0}z^{−i−1}∫Y_{j1}x^i dσ^δ for |z| > x₁ (§2). Y₁₂ = O(z^{−n−1}) means ∫Y₁₁x^i dσ^δ = 0 for i < n. So
Y₁₁ is the monic polynomial of degree n orthogonal to all lower degrees, which is P_n: the Gram matrix (∫x^{i+j}dσ^δ) is positive
definite since σ^δ has infinite support. Y₂₂z^n = 1 + O(1/z) means ∫Y₂₁x^i dσ^δ = 0 for i ≤ n − 2 and = 1 for i = n − 1. So
Y₂₁ = cP_{n−1} with c·h_{n−1} = 1. ∎ (PROVED, elementary.)

## 4. Node masses, residues, and the RH problem for R

**Lemma Ha.4 (node masses).** Let 𝒦^δ(z) := W(z)/(e^{2iθ_δ(z)} − 1) = W e^{−2iθ_δ}κ_δ+ (in ℂ₊). Then:
(a) 𝒦^δ = w e^{−iθ_δ}/Π_δ, and it is meromorphic on 𝒵_n (and on any sector |arg z| < φ < min(π, πp)). Its poles are exactly the X_k, all simple,
  with Res_{X_k}𝒦^δ = W(X_k)/(2iθ′(X_k)) = w(X_k) = n^pτ_k^{−s} = n^p·(mass of σ^δ at x_k).
(b) κ_δ± is analytic in ℂ_± ∩ {|arg z| < min(π, πp)} with |e^{∓2iθ_δ}| = |e^{∓2iθ}| < 1 there, and κ_δ± − 1 = e^{∓2iθ_δ}κ_δ±. At X_k,
  1 − e^{∓2iθ_δ} = ±2iθ′(X_k)(z − X_k)(1 + O(z − X_k)).
*Proof.* (a) W/(e^{2iθ_δ} − 1) = 2iθ′w/(2ie^{iθ_δ}sin θ_δ) = we^{−iθ_δ}θ′/sin θ_δ. The poles are the zeros of e^{2iθ_δ} − 1, which are the X_k by L Ha.1(iii).
At X_k, e^{2iθ_δ} − 1 = 2iθ′(X_k)(z−X_k)(1 + O(z − X_k)), since e^{2iθ_δ(X_k)} = 1 and θ_δ′ = θ′. Also W = 2iθ′w, θ′(X_k) ≠ 0, and
w(X_k) = n^pt(X_k)^{−s} = n^pτ_k^{−s}. (b) |e^{∓2iθ_δ}| = |e^{∓2iθ}|·|e^{±2πiδ}| = |e^{∓2iθ}| (δ real), then (eq:imtheta). The expansion
is as in (a). ∎ (PROVED.)

So the lattice identity "Res_{X_k}U_{j2} = w(X_k)U_{j1}(X_k)" (eq:w-rn) and "Res_{X_k}𝒦_j = w(X_k)U_{j1}(X_k)" (lenssector) hold for the
Hurwitz problem with the same w, W and with θ_δ only in the phase. With the lattice phase θ, 𝒦 has no pole at X_k when δ < 0, because
t(X_k) = k + δ ∉ ℤ. The residue is then 0, not the mass (control in §5). The phase must be θ_δ.

**Proposition Ha.5 (pole removal; RH ⇔ interpolation).** Fix the contour of Paper 2 §frame-contour with the saturated segment
(4c, X₁ + δ′), the top segment Σ_top := {X₁ + δ′ + iy: 0 < |y| ≤ h₀}, Ω_sat± := {4c < Re z < X₁ + δ′, 0 < ±Im z < h₀}, and the lens Ω_b^±
unchanged. Let U be any 2×2 function, analytic in ℂ∖({X_k} ∪ {0}), whose first column is analytic at each X_k and whose second
column has at most a simple pole at each X_k, with residue r_{jk}. Define R by (eq:R) with κ_δ, L^δ_±, A^{△δ}_±. Then, for each k:

  R restricted to each of Ω_b^±, Ω_sat± extends continuously to X_k  ⇔  r_{jk} = w(X_k)U_{j1}(X_k) (j = 1, 2).

Consequently, for U = n^{pnσ₃}Y(zn^{−p}) with Y in the class (Y1), (Y3), (Y4′) (fixed per Rule R review A of the p>1 chain, Ha-2), the following are equivalent:
- (Y2) holds, so that Y is (eq:Y-solution), by L Ha.3;
- R has no singularity at any node, i.e. R solves the RH problem whose jumps M₋^{−1}M₊ lie on Σ only (Paper 2 (eq:VM) context), with
  R = U for |z| > X₁ + δ′ + h₀.

Conversely, U is recovered from R by inverting the triangular factors region by region.

*Proof.* Every node lies in [0, X₁] ⊂ closure of Ω_b ∪ Ω_sat (L Ha.1(ii)): X_k ∈ (0, 4c] in the lens, X_k ∈ (4c, X₁] in Ω_sat. None lies in
Ω_∞, where R = U. *Lens* (Ω_b^+; Ω_b^− is the mirror image): R_{j2} = U_{j2} − U_{j1}𝒦^δ = [r_{jk} − w(X_k)U_{j1}(X_k)]/(z − X_k) + O(1)
by L Ha.4(a). R_{j1} = U_{j1} is regular. *Saturated region*: R = UA^{△δ}_±κ_δ±^{σ₃}. The second column is U_{j2}κ_δ±^{−1}, which is regular
because κ_δ±^{−1} vanishes simply at X_k (L Ha.4(b)). The first column is κ_δ±(U_{j1} ∓ U_{j2}/(κ_δ±W)). By L Ha.4(b),
κ_δ± = 1/(±2iθ′(X_k)(z − X_k)) + O(1), so U_{j2}/(κ_δ±W) = ±r_{jk}·2iθ′(X_k)/W(X_k) + O(z − X_k) = ±r_{jk}/w(X_k) + O(z − X_k). The bracket is
U_{j1}(X_k) − r_{jk}/w(X_k) + O(z − X_k). So the first column is regular iff r_{jk} = w(X_k)U_{j1}(X_k). In both regions the singular part is
a nonzero multiple of [r_{jk} − w(X_k)U_{j1}(X_k)]/(z − X_k), which proves ⇔. "Consequently": the residue conditions of U are (Y2)
rescaled (L Ha.2(b)). With them, R is analytic in each region and continuous up to the nodes, so its only jumps are on Σ. The
factors L^δ, A^{△δ}κ_δ^{σ₃} are invertible in their regions (det = 1, resp. det κ_δ^{σ₃} = 1). ∎ (PROVED. This is Paper 2 Step 1, run in
both directions, with κ_δ.)

*Contour bookkeeping (top node).* The top segment sits at Re z = X₁ + δ′ (0 < δ′ < 1). No node lies on [X₁ + δ′, ∞) (L Ha.1(ii)). The
closure of Ω_b ∪ Ω_sat minus {0} lies in 𝒵_n: arguments as in Paper 2, and |z| ≤ X₁ + δ′ + h₀ < e^{p}a^{−p}n^p = e^{pc₀}n^p as soon as
(e^p − 1)a^{−p}n^p > δ′ + h₀, e.g. for (e^p − 1)n^p > 2 (n ≥ n₀(p)). Lemma weightdomain holds verbatim. On 𝒵_n, Re ξ = log|t| > −c₀ holds
on the top node itself (t = a) and up to |z| < e^{pc₀}n^p. The lips, Σ_v and the band are unchanged (they depend only on the lattice g).
Every n^p + δ′ in Paper 2's contour (saturated segment, Σ^{△±}, Σ_top, the vertex n^p + δ′ ± ih₀, and the domain {|z| > n^p + δ′} of
Lemma normalisation and of (O5) at ∞) becomes X₁ + δ′. This agrees with JZC_M3a_H_G12.md §0 and with the corrected JZC_M3a_Hd.md §1.

*F5 on the moved arcs* (fixed per Rule R review A of the p>1 chain, G1u-1 = C-1). Paper 2's F5 argument (sec_6, 'Σ^{△±} and the top segment') holds verbatim for
x ≤ X₁ + δ′: Re φ ≤ −½log x for x ≥ x₀ (lattice g); |Im θ(x ± ih₀)| ≥ h₀nx^{−1−1/p}/C gives |κ_δ±| ≤ Ca^{−p−1}n^p (|e^{∓2iθ_δ}| = |e^{∓2iθ}|);
on the top segment |1 − e^{∓2iθ_δ}| ≥ a^{p+1}n^{−p}/C; log x ≤ C log n; the phase e^{±2πiδ} of these entries (H-d (ii)) has modulus 1. Hence
|v − I| ≤ C_ae^{−n/C} there, and ≤ C_an^{−pn/4} on the top segment.

*What changes vs Paper 2 (δ = 0 gives Paper 2 in every line).*
| object | Paper 2 (lattice) | Hurwitz (H-a) |
|---|---|---|
| nodes | X_k = (n/k)^p, t(X_k) = k | X_k = (n/(k+δ))^p, t(X_k) = k + δ |
| top node; Laurent region | X₁ = n^p; \|z\| > n^p | X₁ = (n/a)^p; \|z\| > X₁ |
| phase | θ = πt, sin πt, 1/Γ(t) | θ_δ = π(t−δ), sin π(t−δ), 1/Γ(t−δ) |
| non-nodes | t ∈ −ℕ (p < 1: arg z = ±πp) | t ∈ δ − ℕ₀ (p < 1: arg z = ±πp; p > 1: none) |
| residue weight | w(X_k) = n^pk^{−s} | w(X_k) = n^p(k+δ)^{−s}; W = 𝗐_nz^α unchanged |
| κ, L, A^△ | with θ | with θ_δ (\|e^{∓2iθ_δ}\| = \|e^{∓2iθ}\|) |
| contour top | n^p + δ′ | X₁ + δ′; c₀ = 1 + log(1/a) |
| T1(a) hypothesis | x_k ∈ (0, 1] | x_k ∈ (0, a^{−p}] (proof adapted, §2) |

G12 Lemma 2.2 (lens sectors, Hurwitz) uses L Ha.1(iii) and L Ha.4(a) in the form stated there: "the poles of 𝒦_j … in 𝒢 are where
t ∈ δ + ℤ, |arg t| < ϑ_lip/p, i.e. exactly the Hurwitz nodes (t = δ − m ≤ 0 lies off the sector), with residues w(X_k)U_{j1}(X_k)".

## 5. Numerical check (Rule N: NUMERICAL; finite samples; nothing fitted)

`checks/m3a_ha_interp.py` (mpmath, dps 60), n = 3, α = −0.3 (s = 1 + p + αp), (p, δ) ∈ {(1.5, 0), (1.5, −0.3), (1.5, −0.9), (3, −0.3),
(3, −0.9), (0.6, 0), (0.6, −0.3), (0.6, −0.9)}. The case δ = −0.9 has a = 0.1, so the top node X₁ = 10^p·n^p is far above n^p. Moments
ζ(s + jp, a) are computed as a direct sum (k ≤ 400) plus the script's own Euler–Maclaurin tail. That tail is checked against mp.zeta at
small b to 10⁻³⁰; mpmath's zeta(σ, b) is avoided at large b, cf. G12 §3. U_{j2} is evaluated by **direct summation over the nodes**
(k ≤ 400) plus an expanded tail, independently of the residue formula.
- Ha.1: argument-principle counts of zeros of 1 − e^{2iθ_δ} in {r₁ < |z| < r₂, |arg z| < φ} (|t| ∈ (½, 5.5)). The count is 5 = #nodes for
  φ = ϑ_w, and for p > 1 also for φ = 0.95π. *Control (must fail)*: p = 0.6, φ = 0.95π > πp gives 15 = 5 nodes + 10 non-nodes t = δ − m on
  the two rays arg z = ±πp. That count is asserted as well.
- Ha.2: Laurent ratio of U₁₂z^n at ∞ → X₁ to 10⁻⁶ at order 70 (e.g. 164.3168 = X₁ vs n^p = 5.196 at p = 1.5, δ = −0.9). Extraction on
  |z| = 2X₁: 𝖻 = n^{2p}b_n², 𝖺 = n^pa_n to ≤ 3·10⁻²⁵ relative (b_n², a_n from the three-term recurrence of the monic OPs). *Control (must fail,
  δ < 0)*: extraction on |z| = (n^p + X₁)/2 is off by O(1) (relative errors −1.0 to −3.3).
- Ha.4: Res_{X_k}U_{j2} (contour integral of the direct sum) = n^pτ_k^{−s}U_{j1}(X_k). Res_{X_k}W/(e^{2iθ_δ} − 1) = Res we^{−iθ_δ}/Π_δ =
  n^pτ_k^{−s} for k = 1, 2, 3, to 10⁻²⁵ relative; top-node masses up to 583 (p = 1.5, δ = −0.9). The reflection identity for sin π(t−δ)
  and D̃_δ = √(2π)t^{t−δ−½}e^{−t}/Γ(t−δ) hold to 10⁻³⁰. *Control (must fail, δ < 0)*: the lattice phase gives residue ≤ 10⁻¹⁷ at X₁ (no pole); asserted at X₁, X₂, X₃.
- Ha.5: R_{j2} (lens formula) and R_{j1} (saturated formula) at X_k + εe^{iφ}, ε ∈ {10⁻¹², 10⁻¹⁶}·X_k, φ ∈ {π/3, 2π/3}, agree to 10⁻⁸
  relative at X₁, X₂, X₃. *Control (must fail, δ < 0)*: with the lattice κ, ε|R|/|R_δ| = 0.15–2.6, a pole.

Result: ALL 298 CHECKS PASSED; all 33 controls failed as required. Runtime ≈ 2 min.

## 6. Rule A (adversarial pass) — log

1. *Top node, a → 0.* X₁ = (n/a)^p → ∞ and w(X₁) = n^pa^{−s} → ∞ as δ → −1, but every statement is for fixed δ. The Laurent radius is
   X₁ and not n^p: tested at a = 0.1, and the control on the circle between n^p and X₁ fails. T1(a)'s hypothesis x_k ≤ 1 really fails
   here (x₁ = 10^p), so a direct citation of T1(a) would be invalid; §2 re-proves the one step that used it.
2. *Is t = δ a node?* For δ ∈ (−1, 0) it is negative. For δ = 0 it is t = 0, i.e. z = ∞. For δ > 0 (excluded) t = δ > 0 would be a zero
   of 1 − e^{2iθ_δ} at z = (n/δ)^p > X₁ that carries no mass. P Ha.5 then shows that R has a pole there (r = 0 ≠ w·U_{j1} unless U_{j1}
   vanishes), so Step 1 fails. This is the "phantom node" obstruction behind JZC_M3a_H §4 "Not covered: δ > 0". It is consistent with
   H-d §4 (each deleted top node shifts β′ by 2). Logged as the reason for the restriction, not as a new claim.
3. *Non-nodes in the relevant sectors.* p > 1: impossible (|arg t| < π/p < π). p < 1: only on arg z = ±πp, beyond ϑ_w, (5/4)ϑ_lip and
   πp/2. The argument-principle control confirms that they appear exactly when the sector is widened past πp. p = 1 would put them on
   (−∞, 0), on the cut of t (not covered).
4. *Converse direction of P Ha.5.* Tested: a wrong residue (lattice phase) leaves a 1/(z − X_k) singularity in both the lens and the
   saturated formulas (control).
5. *Uniqueness without (Y4′).* Without a condition at the accumulation point 0, IP^δ_n need not determine Y: (Y1)–(Y3) do not exclude
   adding to Y_{j2} a function with an essential singularity at 0 that is O(z^{−n−1}) at ∞ (e.g. a multiple of
   e^{1/z} − Σ_{m≤n}z^{−m}/m!). So the class condition (Y4′) is needed for L Ha.3. Paper 2 never uses uniqueness, and neither does Theorem H.
6. *Nodes at vertices* (X_k = 4c for some k): as in Paper 2. R is continuous up to X_k from each region separately, so the statement is
   unchanged. Nothing new for δ.
7. *det of the factors*: det L^δ = det A^{△δ} = 1 and det κ_δ^{σ₃} = 1, so det R = det U = 1 (L Ha.2(a)).
8. *Rule N*: a first run at dps 40 lost the pole-removal check at p = 3 (ε = 10⁻¹⁶ absolute next to X₁ ≈ 79 cost about 18 digits). It was
   fixed with ε relative to X_k and dps 60. Every pass/fail is computed, and controls are asserted to fail.
9. *Rule X*: nothing is fitted. Moments, node sums and contour integrals are independent evaluations of the stated objects.

## 7. Outcome

H-a is written out for −1 < δ ≤ 0, p > 1 and p < 1 (PROVED / PROVED-mod-cite + REVIEWED: Rule R review A of the p>1 chain, fixes
applied 2026-10-21):
- the interpolation lemma for σ^δ (L Ha.2), with top node X₁ = (n/a)^p and Laurent region |z| > X₁;
- uniqueness in the class (Y4′) (L Ha.3);
- node masses and residues with θ_δ = π(t − δ), sin π(t − δ), 1/Γ(t − δ) (L Ha.1, L Ha.4);
- the equivalence of the RH problem for R with the interpolation problem, i.e. pole removal ⇔ residue conditions (P Ha.5);
- the contour with top vertex X₁ + δ′ and c₀ = 1 + log(1/a).

This closes item 4 of JZC_M3a_H.md §4 (Rule R review A done, fixes applied 2026-10-21; JZC_M3a_H.md §4 records it).
