# E_plt1: the 1/n coefficient (E) for pure powers, 0 < p < 1, and the n^{−1−p} term (Plan 67)

Status (2026-10-15): written by the Plan 67 agent. Rule R reviews A (analysis) and B (algebra) are in
(research/G1/review/REVIEW_Plan67_A.md, REVIEW_Plan67_B.md; both ACCEPT WITH FIXES, no mathematical error); fixes A1–A4,
I1, I3 and B1–B6 are applied (I2, optional near-seam sample points, not added; the reviewer's own probe covers them).
**REVIEWED 2026-10-15** (REVIEW_Plan67_A.md, REVIEW_Plan67_B.md; fixes diff-checked). Labels per VERIFICATION_POLICY.md.
"RH" means Riemann–Hilbert throughout. This file closes, for 0 < p < 1, the GAP "(E)" of SECOND.md §4 (and E_pgt1 §9,
second bullet), settles g(p) = 0 for 0 < p < 1, and identifies the n^{−1−p} term seen in SECOND §1. It does not touch
p = 1 (worked on separately). SECOND.md and THEOREMS.md are **not** edited; §12 lists the changes for integration.

**Summary of labels.**

| # | Statement | Label |
|---|---|---|
| Thm E′.1 | 0 < p < 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), n^pα_n = 2c(1 − (s−1+p)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), **κ_p := 2p c(p) ζ(−p) < 0**; hence α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−2p} + n^{−2}) (no n^{−1−p} term) | PROVED-mod-cite (RH_plt1b [REVIEWED], RH_px §5 [REVIEWED]; Paper 2 Lemmas seam, corner, szego, airy, invariance, Frame Prop.; E_pgt1 Lemmas E.3–E.5 [REVIEWED]; KMVV §6 incl. angle freedom; DLMF 5.2.1, 25.2.1, 25.4.1, 9.7.2, 9.7.5–6, 10.17, 10.40.1–4) + exact computer algebra (check_e_plt1_sym) |
| Cor E′.6 | 0 < p < 1: n^pg_{n−1} = c(1 + a/n + κ_p n^{−1−p} + O(n^{−1−2p} + n^{−2})) (the same relative correction as b_n, α_n); hence the symmetric chain γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + 2^{1+p}κ_pN^{−1−p} + O(N^{−1−2p} + N^{−2})), k₀ = −(s−1) − p/2, k₁ = −(p+2)a | PROVED-mod-cite (as Thm E′.1, + DLMF 10.25.2) + exact computer algebra (n^pg_{n−1}: check_e_plt1_sym [4]; unfolding to γ_N²: by hand (§7.2) and asserted in check_e_plt1_sym [5]) |
| Lemma F.1 | band factor of the seam geometry: log H_n(z) − log H_n(1) = −2ζ(−p)(z−1)n^{−p} + O(n^{−2p}) on \|z\| ≤ 4c + 2 (boundary values on the seams included); more precisely −2Σ_{k≤K}ζ(−kp)(z^k−1)/(k n^{kp}) + O(n^{−(K+1)p}) | PROVED-mod-cite (Paper 2 Lemmas seam, corner; (eq. binet-bound), (eq. binet-small); DLMF 5.2.1, 25.2.1, 25.4.1) |
| Lemma F.2 | Szegő function of e^{−λx} on [0, 4c]: D_q²/q = e^{λ𝓡}, 𝓡 = (z(z−4c))^{1/2} | PROVED (Paper 2 (eq. szego-repr)) |
| Lemma E′.3 | circle jumps I + Δ₁/n + O(n⁻²), Δ₁ = Δ₁^{mod} + λ_nΔ₁^{lin} + O(n^{−2p}), λ_n := 2ζ(−p)n^{−p} | PROVED-mod-cite (E_pgt1 Lemma E.3 transferred; RH_plt1b §2; KMVV angle freedom; DLMF as E_pgt1) |
| Lemma E′.5 | Δ₁^λ := Δ₁ for the weight x^α(4c−x)e^{−λx} is meromorphic in both discs (proof, not only series check); Laurent data of ∂_λΔ₁^λ: A_r^{lin} = c²p[[−(α+1), i(α+2)], [iα, α+1]], B_r^{lin} = 0, A₀^{lin} = 0, C₀^{lin} explicit | PROVED (structural argument + exact sympy series, check_e_plt1_sym.py) |
| Prop E′.5′ | R = I + R⁽¹⁾/n + O(n⁻² + n^{−1−2p}), R⁽¹⁾ = principal parts of Δ₁^{mod} + λ_nΔ₁^{lin} | PROVED-mod-cite (RH_px §5; RH_plt1b; Paper 2 Prop. frame F1, F5) |
| §2 | where the p > 1 proof breaks, and why the n^{−p} variation of H_n never reaches b_n at order n^{−p} | PROVED (bookkeeping on the above) |
| §9 | consequences: SECOND Cor 3.3, Cor 3.9, Thm 3.10(d) unconditional for 0 < p < 1; Thm 3.4 superseded; g(p) = 0 for 0 < p < 1; Conj. P62 PROVED-mod-cite for 0 < p < 1 (remainder O(n^{−1−p}), as conjectured) | PROVED-mod-cite (as Thm E′.1) |
| Remark F.3 | for p > 1 the same ζ(−kp) expansion of log H_n (n^{−1−p} term inside E_pgt1's O(n⁻²) for 1 < p < 2) | NUMERICAL (check_e_flat.out) + HEURISTIC |
| §10 | the n^{−1−2p} and n⁻² coefficients; p = 1; Rule L | GAP |

Numerical cross-checks (NUMERICAL, not used in the proofs): `checks/check_e_plt1_flat.out` (Lemma F.1 against the literal
seam construction of Paper 2, three terms of the ζ(−kp) expansion, p = 0.3, 0.5, 0.7; the seam moment identity at
p = 0.3, …, 0.9 to 10⁻⁴⁰), `checks/check_e_plt1_num.out` (the coefficients on the grid p ∈ {0.3, 0.5, 0.7, 0.9},
s ∈ {1.5, 2, 3}, n ≤ 1600: d₁, the n^{−1−p} coefficient κ_p of b_n and α_n, its absence in α_n/(2b_n), the chain),
and the Plan 62 data at p = ½ (raw sequence in SECOND §1; the fitted n^{−3/2} coefficient ≈ −0.0849 of n^pb_n/c at
s = 1.5, 2, 3 is in REVIEW_Plan62.md, bullet "Rule A claim on n^{−3/2} terms"): it is κ_{1/2} = ζ(−½)/√6 = −0.08487.

Novelty: UNCHECKED (Rule L not done; §10).

## 0. Setting and conventions

- σ = σ_{p,s} = Σ_{k≥1}k^{−s}δ_{k^{−p}}, **0 < p < 1**, s > 1; α := (s−1−p)/p > −1 (Bessel order at the hard edge),
  a := α + ½ = (2s−2−p)/(2p); c = c(p) as in E_pgt1 §0 (toolkit `laws.weyl.c_p`).
- Monic OPs, pairings, chain g_n, h_n: as in E_pgt1 §0 / SECOND §0. Standard pairing α_n/(2b_n) (coefficient e₁ˢ).
- **Frame.** The Q-frame of Paper 2 (papers/paper2 §§5–6, ℓ₁ ≡ 1) with the **seam outer scalar** of Paper 2 Lemma seam
  (app_outer.tex §"The case 0 < p < 1", = RH_plt1b §1): θ_s := πp/2, S_in := {|arg z| < θ_s}, S_out, seams Γ± :=
  {re^{±iθ_s}} oriented away from 0, ϖ := ½ − 1/(2p), B_in := (1+z)^ϖ, B_out := (1 − z/(2πn))^{1/2}, seam densities
  χ± (Paper 2 (eq. Lpm); Binet's function j, D̃ = e^{−j(t)}, t = nz^{−1/p}), seam scalar χ (eq. chi), F (eq. F-seam), and
  the band factor H_n = (D̃B_in e^χ)^{−2} on Z_n (Paper 2 Lemma seam(iv)), band weight W₀ = 𝗐_n z^α(4c−z)H_n (eq. W0;
  r_n ≡ 1 for pure powers). Lips at θ_lip = πp/4 (Paper 2 (eq. thetaw), default for p < 1; = RH_plt1b's θ_L), weight
  sector θ_w = 3πp/8 < θ_s. Szegő function D_W, ω := D_W²/W₀ (Paper 2 (eq. omega)), 𝓡(z) := (z(z−4c))^{1/2} ~ z,
  global parametrix P₀^∞ = T𝔞_∞^{σ₃}T^{−1}, extraction functionals b(Q) = (Q₁)₁₂(Q₁)₂₁ = n^{2p}b_n², a(Q) =
  (Q₂)₁₂/(Q₁)₁₂ − (Q₁)₂₂ = n^pα_n (Paper 2 F8): all as in E_pgt1 §0.
- **Hard edge.** The classical Bessel parametrix of RH_plt1b §2 (RH_px §4.1 / KMVV (6.42)–(6.53) with the KMVV rays at
  angle π − θ_L, and the **glued** W̃ := (C(−z)^α(4c−z))^{1/2}/G̃, G̃ := D̃B_in e^χ in S_in, G̃ := B_out e^χ in
  S_out ∩ U(0, δ)), written in the Q-frame as P̂₀ := D_∞^{−σ₃}P₀D_W^{σ₃}; ρ := W̃/D_W.
  RH_plt1b's seam scalar X is Paper 2's χ (same densities; RH_plt1b's *displayed* definition of μ has a sign slip,
  recorded in ROUTE2_plt1 §3.2 "Sign convention"; we use Paper 2 (eq. Lpm), with Binet's j).
- Range of s: Paper 2 states its lemmas for 1 < s < 1 + 2p; RH_plt1b (REVIEWED) covers every s > 1. The Paper 2 inputs used
  here (Lemmas seam, corner, szego (i), (vi)(a)–(c), signs, gfunction, airy; F1's contour and Cauchy bound; F5's arc-by-arc
  bounds) do not use α < 1 — the same check as E_pgt1 §10 "Large α", which applies verbatim (the seam scalar does not
  involve s at all).

## 1. Main results

**Theorem E′.1 (PROVED-mod-cite; inputs listed in the table).** Let 0 < p < 1, s > 1, and κ_p := 2p·c(p)·ζ(−p). Then

  n^pb_n = c(p)(1 − (s−1)/(2n) + κ_p n^{−1−p} + O(n^{−1−2p} + n^{−2})),
  n^pα_n = 2c(p)(1 − (s−1+p)/(2n) + κ_p n^{−1−p} + O(n^{−1−2p} + n^{−2})),

and consequently

  α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−2p} + n^{−2})  (e₁ˢ = −p/2; no n^{−1−p} term),
  α_{n−1}/(2b_n) = 1 + p/(2n) + O(n^{−1−2p} + n^{−2})  (e₁ = p/2).

In particular (E) of SECOND §4 holds for 0 < p < 1 with ε = p (that is, (E_p)), d₁ = −(s−1)/2, and the remainder O(n^{−1−p})
is sharp: κ_p < 0 for every p ∈ (0, 1) (by DLMF 25.4.1, ζ(−p) = −2(2π)^{−1−p}sin(πp/2)Γ(1+p)ζ(1+p), and every factor after
the sign is positive). At p = ½: κ_{1/2} = ζ(−½)·c(½) = ζ(−½)/√6 = −0.0848692… (c(½) = ¼√(8/3) = 1/√6).

**Corollary E′.6 (chain; PROVED-mod-cite).** For 0 < p < 1, s > 1:

  n^pg_{n−1} = c(1 + a/n + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})),

equivalently G_m := m^pg_m = c(1 + (a−p)/m + κ_pm^{−1−p} + O(m^{−1−2p} + m^{−2})) and H_m := m^ph_m =
c(1 − (s−1+a)/m + κ_pm^{−1−p} + O(m^{−1−2p} + m^{−2})); the symmetric chain satisfies

  γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + 2^{1+p}κ_pN^{−1−p} + O(N^{−1−2p} + N^{−2})),  k₀ = −(s−1) − p/2, k₁ = −(p+2)a,

the values of SECOND §1.1 (and of E_pgt1 Cor E.6). So to order n^{−1−p} the whole chain (g, h, hence b_n and α_n) carries
the same relative factor 1 + κ_pn^{−1−p}: the n^{−1−p} term acts as an n-dependent rescaling c ↦ c(1 + κ_pn^{−1−p}).

**Mechanism (one paragraph).** In the seam geometry the band factor H_n is *not* flat to o(1/n): Lemma F.1 shows that,
modulo constants, H_n(z) = exp(−λ_n z + O(n^{−2p})) with **λ_n = 2ζ(−p)n^{−p}** — in the original variable x = zn^{−p} this
is the n-independent factor exp(−2ζ(−p)x + O(x²)) — heuristically the zeta-regularised product over the nodes above the band (the
moments of the seam jump −Log(1 − e^{∓2πit}) are exactly ζ(−kp)/k · n^{−kp}). Such a variation **cannot** enter b_n or
α_n at order n^{−p}: the global parametrix is exactly invariant (its extraction functionals equal c², 2c for every band
weight, Paper 2 Lemma invariance / E_pgt1 §0), so the weight enters only through the 1/n corrections Δ₁ of the Bessel and
Airy models. There, the linear factor e^{−λz} perturbs ω by e^{λ𝓡} (Lemma F.2) and changes, among the residues that enter b_n and α_n, only the Airy residue A_r, by
λ_n c²p[[−(α+1), i(α+2)], [iα, α+1]], which moves both n^pb_n/c and n^pα_n/(2c) by the same amount cpλ_n/n = κ_pn^{−1−p}.
So the n^{−1−p} term is a product (1/n)·(n^{−p}), s-independent, and cancels in α_n/(2b_n). At p = 2, ζ(−2) = 0 and H_n is
exactly flat (E_pgt1 Lemma E.2, Remark (3)); at p = 1, −2ζ(−1)z/n = z/(6n) is exactly the 1/n term of E_pgt1 §9's
H_n = e^{2j(n/z)}.

## 2. Where the p > 1 proof breaks for p < 1, and what replaces it (Goal 1)

E_pgt1's proof has four ingredients: (a) Lemma E.2 (H_n flat to O(n^{−p}) through the Binet-cut scalar B), (b) Lemma E.3
(circle jumps to second order, Δ₁ depending on n only through H_n), (c) Lemmas E.4–E.5 (model data, residues), (d) Prop
E.5′ (second-order small norm), where the term "O(n^{−1−p}) ≤ O(n⁻²)" absorbed the non-flat part of H_n.

1. *(a) changes form.* For p < 1, Γ's poles lie on arg z = ±πp inside the slit plane and B does not exist (RH_plt1 §6,
   RH_plt1b §0); the band factor is the seam one, H_n = (D̃B_in e^χ)^{−2}. Its flatness statement is Lemma F.1 below: the
   proof of Lemma E.2 (Liouville + a Cauchy integral of a jump that is super-small near 0) goes through with the jump
   −Log(1 − e^{∓2πit}) on the seams, and gives again O(n^{−p}) — but now n^{−p} ≫ n^{−1}.
2. *The O(n^{−p}) is genuine*, not a lossy bound: its leading part is ζ(−p)(z−1)n^{−p} exactly, and ζ(−p) ≠ 0. (E_pgt1 §9
   guessed that the seam H_n is "not flat to o(1/n) near 0", quoting Paper 2's (O3) bound |z|(1 + log(1/|z|)); that bound
   is for χ alone, which varies at order 1, and loses the cancellation between −j(t), ϖLog(1+z) and χ — the same
   phenomenon as E_pgt1 Remark (1) for −j and log B.)
3. *Why no n^{−p} term in b_n.* By Paper 2 Lemma invariance and the exact form of P₀^∞ in the Q-frame (E_pgt1 §0:
   (P₁)₁₂(P₁)₂₁ = c², a(P₀^∞) = 2c for every n and every band weight), the weight enters the extraction only through
   R = Q(parametrix)^{−1}, whose jump is I + Δ₁/n + O(n⁻²) on the circles and super-small elsewhere. So any O(n^{−p})
   change of the weight costs a factor 1/n: it appears at order n^{−1−p} (Prop E′.5′). This is the mechanism; the
   n^{−p}-part of b_n cancels identically, not by a computation.
4. *(b) and (d) survive* with "Δ₁ = Δ₁^{mod} + O(n^{−p})" replaced by "Δ₁ = Δ₁^{mod} + λ_nΔ₁^{lin} + O(n^{−2p})"
   (Lemma E′.3), and the remainder O(n⁻²) of Prop E.5′ replaced by O(n⁻² + n^{−1−2p}). The hard edge is unproblematic for
   p < 1 (unlike p = 1): RH_plt1b's glued classical Bessel parametrix has only super-small extra jumps.
5. *(c)* is p-free (Lemma E.4's local data come from G2's μ*, valid for all p > 0), and one new residue computation is
   needed: the first-order variation of A_r, B_r, A₀, C₀ under e^{−λx} (Lemma E′.5).

## 3. Lemma F.1: the band factor of the seam geometry

Put, with the principal logarithm on each piece and log D̃ := −j(t),

  𝒢(z) := −j(t(z)) + ϖLog(1+z) + χ(z)  (z ∈ S_in),   𝒢(z) := ½Log(1 − z/(2πn)) + χ(z)  (z ∈ S_out),

so that H_n = e^{−2𝒢} on Z_n ⊂ S_in (Paper 2 Lemma seam(iv)) and, in U(0, δ), the glued W̃ of §0 is
(C(−z)^α(4c−z))^{1/2}e^{−𝒢} in both sectors. Let R₁ := 4c + 2 and ℓ(r) := −log(1 − e^{−2πnr^{−1/p}}) > 0 (r > 0).

**Lemma F.1 (PROVED-mod-cite: Paper 2 Lemma seam (i)–(iv), Lemma corner (i)–(iii), (eq. binet-bound), (eq. binet-small);
DLMF 5.2.1, 25.2.1, 25.4.1 as quoted in RH/CITATIONS.md "(DLMF-zeta, Plan 67)").** Let 0 < p < 1.
(i) 𝒢 is analytic in S_in and in S_out, has continuous boundary values on the open seams, is bounded near 0, and
  𝒢_out − 𝒢_in = ℓ(|ζ|) on Γ±.
(ii) For z ∉ Γ₊ ∪ Γ₋ ∪ {0}, with θ := θ_s and K(ζ, z) := (z − 1)/((ζ − z)(ζ − 1)),

  𝒢(z) − 𝒢(1) = (1/2πi)∫_0^∞ ℓ(r)[e^{iθ}K(re^{iθ}, z) − e^{−iθ}K(re^{−iθ}, z)]dr.   (F.1)

(iii) For k ≥ 1, m_k := (1/2πi)∫_0^∞ ℓ(r)[e^{iθ}(re^{iθ})^{−k−1} − e^{−iθ}(re^{−iθ})^{−k−1}]dr = ζ(−kp)/(k n^{kp}).
(iv) For every K ≥ 1 there are C = C(p, K) and n₀ such that for n ≥ n₀, |z| ≤ R₁ (boundary values on the seams included)

  |𝒢(z) − 𝒢(1) − Σ_{k=1}^K m_k(z^k − 1)| ≤ Cn^{−(K+1)p};

  and, for η ∈ (0, 1], the derivative of the left side is ≤ Cn^{−(K+1)p}/η for |z| ≤ R₁ − η with dist(z, Γ₊ ∪ Γ₋) ≥ η.
  In particular (K = 1), with **E_n(z) := 𝒢(z) − 𝒢(1) − ζ(−p)(z − 1)n^{−p}**: |E_n| ≤ Cn^{−2p} on {|z| ≤ R₁}, and
  |E_n′| ≤ Cn^{−2p}/η away from the seams. Moreover |E_n′(x)| ≤ Cn^{−2p} for real x with 0 < |x| ≤ R₁/2 (on (−R₁/2, 0) these are the S_out values, which
  are analytic there), and E_n extends continuously to 0 with the same value E_n(0) from every sector; hence
  |E_n(x) − E_n(0)| ≤ Cn^{−2p}|x| for 0 < |x| ≤ R₁/2.
Hence log H_n(z) − log H_n(1) = −2ζ(−p)(z−1)n^{−p} − 2E_n(z), i.e. H_n ∝ e^{−λ_nz}e^{−2E_n}, λ_n := 2ζ(−p)n^{−p}.

*Proof.* (i) Analyticity in each sector: in S_in, |arg t| < π/2 and −j(t) is analytic (Paper 2 Lemma seam(i)), Log(1+z) is
analytic off (−∞, −1] ⊂ S_out, χ is analytic off the seams (Lemma seam(iii)); in S_out, 1 − z/(2πn) ∉ (−∞, 0] (its cut
[2πn, ∞) lies in S_in). Boundary values: χ has continuous boundary values on the open seams (Lemma seam(iii)); the other
terms are continuous up to the seams. Jump: on Γ₊, by Lemma seam(iii) χ_out − χ_in = χ₊ = −j(t) − Log(1 − e^{−2πit}) +
ϖLog(1+ζ) − ½Log(1 − ζ/(2πn)) (eq. Lpm), so 𝒢_out − 𝒢_in = ½Log(1 − ζ/2πn) + χ₊ + j(t) − ϖLog(1+ζ) =
−Log(1 − e^{−2πit}); on Γ₊, t = −i|t|, |t| = n|ζ|^{−1/p}, so e^{−2πit} = e^{−2π|t|} ∈ (0, 1) and the jump is ℓ(|ζ|).
Γ₋ by conjugation (Lemma seam(ii): χ₋(ζ̄) = conj χ₊(ζ); there e^{2πit} = e^{−2π|t|}). Near 0: in S_in, |t| → ∞ with
|arg t| < π/2, so j(t) → 0 by (eq. binet-bound) (φ = π/2); B_in, B_out → 1; χ is bounded near 0 uniformly up to the seams
(Lemma corner(iii)).
(ii) Let 𝒥(z) be the right side of (F.1). The integral converges absolutely: ℓ(r) ≤ 2e^{−2πnr^{−1/p}} whenever e^{−2πnr^{−1/p}} ≤ ½ (as −log(1−q) ≤ 2q
for 0 ≤ q ≤ ½), and ℓ(r) ≤ log(1 + 1/y) ≤ log 2 + log⁺(r^{1/p}/(2πn)) for all r, y := 2πnr^{−1/p} (from
1 − e^{−y} ≥ y/(1+y)), so ℓ(r) = O_n(1 + log r); and |K(re^{±iθ}, z)| = O_z(r^{−2}) at ∞, O_z(1) near r = 0. With the orientation of Γ± (Γ₊ has
S_out on its left, Γ₋ has S_in on its left), the Sokhotski–Plemelj formula gives 𝒥_out − 𝒥_in = ℓ on both seams
(the density on Γ₊ is +ℓ; on Γ₋ it is −ℓ, with "left minus right" = in minus out), and 𝒥 has continuous boundary values
(ℓ is real-analytic on (0, ∞)). So K₀ := 𝒢 − 𝒢(1) − 𝒥 is continuous across the open seams and analytic on both sides,
hence analytic in ℂ ∖ {0} (Morera). K₀ is bounded near 0: 𝒢 is, by (i), and so is 𝒥 (|ℓ(r)| ≤ 2e^{−2πnr^{−1/p}} near 0,
and the Cauchy integral of a density that vanishes to all orders at the end point is bounded, also at the seam boundary
values). So K₀ is entire. Growth: on the circle |z| = ρ ≥ 2, the terms −j(t), ϖLog(1+z), ½Log(1 − z/2πn) are
O_n(1 + log ρ) up to the seams (for |t| < 1 by (eq. binet-small), for |t| ≥ 1 by (eq. binet-bound)); χ and 𝒥 are Cauchy
integrals over the two rays of densities bounded by C_n(1 + log|ζ|) (Lemma corner(i); and ℓ), whose modulus at z is
≤ C_n(1 + log ρ)²(1 + log(ρ/dist(z, Γ₊ ∪ Γ₋))) (split the ray at |ζ − z| ≤ ρ/2), an integrable function of arg z on the
circle with integral O_n((1 + log ρ)²). Hence ∫_0^{2π}|K₀(ρe^{iφ})|dφ ≤ C_n(1 + log ρ)², and the Taylor coefficients
a_k = (2πρ^k)^{−1}∫K₀(ρe^{iφ})e^{−ikφ}dφ (k ≥ 1) satisfy |a_k| ≤ C_n(1 + log ρ)²ρ^{−k} → 0. So K₀ is constant, and
K₀(1) = 0 (𝒥(1) = 0 since K(ζ, 1) = 0). This is (F.1).
(iii) On Γ₊, (re^{iθ})^{−k−1}e^{iθ} = r^{−k−1}e^{−ikθ}; on Γ₋ the conjugate. So m_k = −(sin(kθ)/π)∫_0^∞ℓ(r)r^{−k−1}dr.
Substitute u = 2πnr^{−1/p} (r = (2πn/u)^p, dr = −p(2πn)^pu^{−p−1}du): ∫_0^∞ℓ(r)r^{−k−1}dr =
p(2πn)^{−kp}∫_0^∞ −log(1 − e^{−u})u^{kp−1}du. By −log(1 − e^{−u}) = Σ_{m≥1}e^{−mu}/m (non-negative terms, Tonelli) and
DLMF 5.2.1 (∫_0^∞e^{−mu}u^{kp−1}du = Γ(kp)m^{−kp}, Re kp > 0), the last integral is Γ(kp)Σ_m m^{−1−kp} = Γ(kp)ζ(1+kp)
(DLMF 25.2.1, Re(1+kp) > 1). Hence m_k = −(sin(πkp/2)/π)·pΓ(kp)ζ(1+kp)(2πn)^{−kp}. DLMF 25.4.1 at s = 1 + kp
(≠ 0, 1): ζ(−kp) = 2(2π)^{−1−kp}cos(π(1+kp)/2)Γ(1+kp)ζ(1+kp) = −2(2π)^{−1−kp}sin(πkp/2)·kpΓ(kp)ζ(1+kp), i.e.
ζ(−kp)/k = −(2π)^{−kp}sin(πkp/2)pΓ(kp)ζ(1+kp)/π. So m_k = ζ(−kp)/(kn^{kp}).
(iv) For |ζ| ≥ 2R₁ and |z| ≤ R₁, K(ζ, z) = Σ_{k=1}^K(z^k − 1)ζ^{−k−1} + O(|ζ|^{−K−2}) (expand 1/(ζ−z) and 1/(ζ−1) in
geometric series; |z|, 1 ≤ |ζ|/2), uniformly. Split (F.1) and the m_k at r = 2R₁.
*Far part.* ∫_{2R₁}^∞ℓ(r)r^{−K−2}dr ≤ ∫_0^∞ℓ(r)r^{−K−2}dr = n^{−(K+1)p}·p(2π)^{−(K+1)p}Γ((K+1)p)ζ(1+(K+1)p) (as in (iii)).
*Near part.* On r ≤ 2R₁, ℓ(r) ≤ 2e^{−2πn(2R₁)^{−1/p}} once this is ≤ ½ (n ≥ n₀; small n are absorbed in C), and more precisely
ℓ(r) ≤ 2e^{−2πnr^{−1/p}}, which vanishes to all orders at 0; ℓ′(r) = O(nr^{−1−1/p}e^{−2πnr^{−1/p}}). The near parts of the
m_k (k ≤ K) are ≤ C∫_0^{2R₁}e^{−2πnr^{−1/p}}r^{−k−1}dr ≤ C′e^{−πn(2R₁)^{−1/p}}. The near part of (F.1): for z at distance
≥ η₀ from the seams, |K(ζ, z)| ≤ (R₁ + 1)/(η₀ sin θ) (ζ on a seam has |ζ − 1| ≥ sin θ), giving O(e^{−cn}); for z close to (or on) a seam, subtract ℓ(|z*|) on the window
|ζ − z*| ≤ |z*|/2 (z* the nearest seam point) and use |ℓ′| on the window, exactly as in Paper 2 Lemma corner(iii) or
E_pgt1 Lemma E.2(c); since ℓ and ℓ′ are O(e^{−cn}) on [r₀, 2R₁] for any fixed r₀ > 0 and super-small near 0 (where
|ζ − z| ≥ sin(θ)·|ζ| for |ζ| ≤ |z|/2), the near part is O(e^{−cn}), boundary values included. Collecting: the left side
of (iv) is O(n^{−(K+1)p} + e^{−cn}). The derivative bound away from the seams is Cauchy's estimate on the disc U(z, η)
(which avoids the seams and lies in {|w| ≤ R₁}). For real x with 0 < |x| ≤ R₁/2: differentiate (F.1) under the integral; the far
part gives ∫ℓ r^{−K−3}·C, O(n^{−(K+1)p}); the near part has |∂_zK(ζ, x)| ≤ C|ζ|^{−2} for ζ on the seams with |ζ| ≤ 2R₁,
since |ζ − x| ≥ sin θ·max(|ζ|, x) for x > 0, and |ζ − x| ≥ max(|ζ|, |x|) for x < 0 (the angle at 0 between the seam
and the negative axis is π − θ > π/2); times ℓ = O(e^{−2πn|ζ|^{−1/p}}) this is O(e^{−cn}). Continuity at 0: 𝒢 − 𝒢(1) = 𝒥
by (F.1), and 𝒥 is the Cauchy integral of a density vanishing to infinite order at the corner 0, so it has one limit
𝒥(0) from all sectors (dominated convergence: for |z| ≤ |ζ|/2 or |ζ| ≤ |z|/2, |K(ζ, z)| ≤ C(1 + |ζ|^{−1}), and near
|ζ| ≍ |z| the density is O(e^{−2πn(2|z|)^{−1/p}}), dominated as in Paper 2 Lemma corner(iii)). ∎

*Remarks.* (1) *What the constants are.* In the original variable x = zn^{−p}, Σ_k m_k z^k = Σ_k ζ(−kp)x^k/k. *Interpretation
(HEURISTIC; not used: the proof uses only the convergent moment integrals (iii), and no regularised product is defined):* this is
the zeta-regularised value of −Σ_{m≥1}log(1 − x m^p) (formally −Σ_m log(1 − x m^p) = Σ_k(x^k/k)Σ_m m^{kp}): H_n is,
modulo constants and to all orders in n^{−p}, the n-independent smooth factor exp(−2Σ_kζ(−kp)x^k/k) = 1 − 2ζ(−p)x + O(x²)
— the regularised square of the product over the nodes x_m = m^{−p} ≫ x. This is SECOND §1's heuristic "far field of the
nodes above the band", now exact. (2) *Checks.* `check_e_plt1_flat.out` [B] computes 𝒢 − 𝒢(1) from the literal
definitions of Paper 2 (χ by quadrature of χ±), at points in S_in and S_out, n = 10…640, p = ½, 0.3, 0.7: after
subtracting the k = 1 term, n^{2p}·residual matches the k = 2 term ζ(−2p)(z²−1)/2, and after subtracting it,
n^{3p}·residual matches the k = 3 term (e.g. p = ½, n = 160, z = 0.2: r₂ = 0.0084158 vs 0.0084271). [A] checks (iii) at
p = 0.3, 0.5, 0.7, 0.9 to 40 digits. (3) *p = 2, p = 1.* For p > 1 the same constants appear (Remark F.3). (4) The
expansion is asymptotic in n^{−p}, not convergent (the moments grow like Γ(kp)).

**Remark F.3 (p ≥ 1; NUMERICAL + HEURISTIC, not used).** For p > 1, E_pgt1 (E.2.1) has the same structure with the jump
𝔢 on (−∞, 0); `check_e_flat.out` gives n^p·max_z|G(z) − G(1)| = 0.022974 at p = 3 (n = 10, …, 80), which is
4c(3)·ζ(−3) = 2.7569/120 = 0.022974 (the maximum is at z = 4c + 1, |z − 1| = 4c), and 0.0565 → 0.0577 at p = 3/2, n = 10 → 80,
approaching 4c(3/2)|ζ(−3/2)| = 0.0577; at p = 2 it is 0 (ζ(−2) = 0). At p = 1, E_pgt1 §9's H_n = e^{2j(n/z)} has
log H_n = 2Σ_m B_{2m}(z/n)^{2m−1}/(2m(2m−1)) = −2Σ_kζ(−k)z^k/(kn^k) (ζ(−k) = −B_{k+1}/(k+1); the terms with even k ≥ 2 vanish on both sides).
So the ζ(−kp) law is p-uniform; for 1 < p < 2 it predicts that E_pgt1's O(n⁻²) remainder contains κ_pn^{−1−p} (the slow drift
in check_e_rate.out). Not claimed: proving it needs the moments of 𝔢, which is the same Mellin computation on a different
contour (not written).

## 4. Lemma F.2 and Lemma E′.3: the circle jumps to order n^{−1−2p}

**Lemma F.2 (PROVED: Paper 2 (eq. szego), (eq. szego-repr)).** For λ ∈ ℝ and q(x) := e^{−λx} on (0, 4c),
log D_q(z)² − log q(z) = λ𝓡(z), i.e. D_q²/q = e^{λ𝓡}, for z ∉ [0, 4c].

*Proof.* (eq. szego-repr) with 𝔠 = log q(z) = −λz: log D_q² + λz = (𝓡/π)∫_0^{4c}(−λx + λz)dx/(√(x(4c−x))(z−x)) =
λ𝓡·(1/π)∫_0^{4c}dx/√(x(4c−x)) = λ𝓡 (x = 4c sin²φ gives ∫ = π). ∎ (check_e_plt1_sym.py [0] also checks the equivalent
identity (1/π)∫x dx/(√(x(4c−x))(z−x)) = z/𝓡 − 1 numerically.)

Write ω^λ := ω^{mod}e^{λ𝓡}, ρ^λ := ρ^{mod}e^{−λ𝓡/2}, (−ω^λ)^{1/2} := (−ω^{mod})^{1/2}e^{λ𝓡/2}, where "mod" is E_pgt1
Lemma E.4(iii) (weight x^α(4c−x)); by Lemma F.2 and D_{q₁q₂} = D_{q₁}D_{q₂} these are the ω, ρ of the weight
x^α(4c−x)e^{−λx}. Let Δ₁^{⋄,λ} (⋄ ∈ {0, r}) be E_pgt1's formulas (Lemma E.3) with these data:

  Δ₁^{0,λ} = (1/(16f^{1/2}))P₀^∞(ρ^λ)^{σ₃}Q₀(ρ^λ)^{−σ₃}(P₀^∞)^{−1},  Δ₁^{r,λ} = −(1/φ̃)P₀^∞(−ω^λ)^{−σ₃/2}X(−ω^λ)^{σ₃/2}(P₀^∞)^{−1},

and Δ₁^{lin} := ∂_λΔ₁^λ|_{λ=0} (so Δ₁^{mod} = Δ₁^0).

**Lemma E′.3 (PROVED-mod-cite: E_pgt1 Lemma E.3 (KMVV (6.23)–(6.28); DLMF 10.40.1–4, 10.17; 9.7.2, 9.7.5–6; Paper 2 Lemma
airy); RH_plt1b §2; KMVV angle freedom; Lemma F.1).** For 0 < p < 1, uniformly on ∂U_0 (boundary values at the seams and
at (−δ, 0) included) and on ∂U_r,

  P̂₀(P₀^∞)^{−1} = I + Δ₁⁰/n + O(n⁻²),  P̂_r(P₀^∞)^{−1} = I + Δ₁^r/n + O(n⁻²),  Δ₁^⋄ = Δ₁^{⋄,mod} + λ_nΔ₁^{⋄,lin} + O(n^{−2p}).

*Proof.* *The expansions.* E_pgt1 Lemma E.3's computation is local: it uses the large-argument expansions of the Bessel
model Ψ and of the Airy model, the identities f^{1/2} = −(φ ± iπ)/2, φ̃ = −(2/3)f_r^{3/2}, and the bounds on P₀^∞, ρ^{±1},
(−ω)^{±1/2} on the circles; none depends on p > 1. The Airy part is Paper 2's parametrix (eq. airy), valid for all p
(Paper 2 F5). For the Bessel part with p < 1 the KMVV rays are at π − θ_L, θ_L = πp/4 (RH_plt1b §2; KMVV angle freedom, RH/CITATIONS
"(KMVV, angle freedom; Plan 15b)"): in the sector |arg ζ| < π − θ_L, w = 2ζ^{1/2} has |ph w| ≤ π/2 − θ_L/2, so DLMF
10.40.1–10.40.4 apply with δ = θ_L/2 (as recorded in "(DLMF-10.40, Paper 2)"); in π − θ_L < ±arg ζ < π,
ph 2(−ζ)^{1/2} ∈ (−θ_L/2, 0), resp. (0, θ_L/2), inside the sectors of DLMF 10.17.5–6, 10.17.11–12 ("(DLMF-10.17, Plan 55)").
So (E.3.1) holds in all three sectors, and the derivation of E_pgt1 Lemma E.3 gives the displayed expansions with Δ₁ given by
its formulas with the true ω, ρ. The glue of RH_plt1b §2 (W̃_out/W̃_in = 1 − e^{∓2πit} on the seams, |e^{∓2πit}| =
e^{−2πn|z|^{−1/p}}) changes the analytic prefactor by Φ = O(e^{−c′n}) (RH_plt1b §2: Ẽ_N = E^a + Φ, RH_px Lemma
4.2(iii)), which is inside O(n⁻²).
*The n-dependence.* By Lemma F.1, W₀ = 𝗐′_n·z^α(4c−z)e^{−λ_nz}q₂(z) with q₂ := e^{−2E_n} (on the band and on Z_n), and
in U(0, δ) W̃² = e^{∓iπα}·𝗐′_n z^α(4c−z)e^{−λ_nz}q₂(z) with the sector values of E_n. With Paper 2 (eq. omega) and Lemma F.2,
ω = ω^{λ_n}·(D²_{q₂}/q₂) and ρ² = (ρ^{λ_n})²·(q₂/D²_{q₂}). By (eq. szego-repr) with 𝔠 = log q₂(z) (any value is allowed),

  log D²_{q₂}(z) − log q₂(z) = (2𝓡(z)/π)∫_0^{4c}(E_n(z) − E_n(x))dx/(√(x(4c−x))(z − x)).

On both circles, away from the two points δ and 4c − ε where they meet [0, 4c], |z − x| ≥ d > 0 and |E_n| ≤ Cn^{−2p}
(Lemma F.1(iv), sup over |z| ≤ R₁, boundary values included) give O(n^{−2p}); near those two points (which are at
distance ≥ δ sin θ_s from the seams) split off the window |x − Re z| ≤ η₀ and use |E_n′| ≤ Cn^{−2p}/η₀ there, as in
E_pgt1 Lemma E.3 ("n-dependence"). So log(ω/ω^{λ_n}) = O(n^{−2p}) on both circles. Δ₁ depends analytically on
(ρ²)^{±1} and (−ω)^{±1/2}, which are bounded above and below uniformly: on ∂U_0 because ρ^{mod} is explicit and
bounded above and below on |z| = δ (Paper 2 Lemma szego(i): D²_{x^α} = (4cz/Υ)^α, D²_{4c−x} = 4c(z−4c)/Υ; E_pgt1 Lemma
E.4(iii)), e^{±λ_n𝓡/2} = 1 + O(n^{−p}), and log(D²_{q₂}/q₂) = O(n^{−2p}) as just shown; on ∂U_r by Paper 2 Lemma szego(vi)(b)
and the same two factors; so Δ₁ = Δ₁^{λ_n} + O(n^{−2p}) and Δ₁^{λ_n} = Δ₁^{mod} + λ_nΔ₁^{lin} + O(λ_n²). ∎

## 5. Lemma E′.5: meromorphy and the Laurent data of Δ₁^{lin}

**Lemma E′.5 (PROVED; structural argument + checks/check_e_plt1_sym.py, sympy, all assertions pass, output
check_e_plt1_sym.out).** For each real λ, Δ₁^{r,λ} is analytic in U_r ∖ {4c} with at most a double pole at 4c, and Δ₁^{0,λ}
is analytic in U_0 ∖ {0} with at most a simple pole at 0. Writing Δ₁^{r,λ} = B_r^λ/(z−4c)² + A_r^λ/(z−4c) + O(1) and
Δ₁^{0,λ} = A₀^λ/z + C₀^λ + O(z), the λ = 0 values are E_pgt1 Lemma E.5's B_r, A_r, A₀, C₀, and the λ-derivatives at 0 are

  B_r^{lin} = 0,  A_r^{lin} = c²p[[−(α+1), i(α+2)], [iα, α+1]],  A₀^{lin} = 0,  C₀^{lin} = (c(p+2)/4)[[α+1, i(α+2)], [iα, −(α+1)]].

*Proof (meromorphy).* Δ₁^{r,λ}: inside U_r the only possible jump is on (4c − ε, 4c) (P₀^∞, φ̃, (−ω)^{1/2} are analytic
on (4c, 4c + ε) and off the real axis). There P₀^∞₊ = P₀^∞₋J, J := [[0, 1], [−1, 0]] (Paper 2 F5), φ̃₊ = −φ̃₋ (φ̃/u³ is analytic
at 4c, u = (z−4c)^{1/2} principal: E_pgt1 Lemma E.4(ii) proof), and (−ω^λ)^{1/2}₊(−ω^λ)^{1/2}₋ = 1 — for λ = 0 this is the band relation of
Paper 2's root (eq. omega-root-band) (D_{W+}D_{W−} = W₀ gives ω₊ω₋ = 1), and the factor e^{λ𝓡/2} satisfies it because
𝓡₊ = −𝓡₋ on the band. Since Jd^{σ₃}J^{−1} = d^{−σ₃} and JXJ^{−1} = −X, Δ₁^{r,λ}₊ = −(1/φ̃₊)P₀^∞₋(−ω₋)^{−σ₃/2}(−X)(−ω₋)^{σ₃/2}(P₀^∞₋)^{−1} =
Δ₁^{r,λ}₋. So Δ₁^{r,λ} is analytic in U_r ∖ {4c}; |Δ₁^{r,λ}| ≤ C|z − 4c|^{−2} (|φ̃| ≍ |z−4c|^{3/2}, |P₀^∞|^{±1} ≤
C|z−4c|^{−1/4}, (−ω^λ)^{±1/2} bounded), so (z − 4c)²Δ₁^{r,λ} has a removable singularity (Riemann). Δ₁^{0,λ}: on (0, δ),
P₀^∞₊ = P₀^∞₋J, f^{1/2}₊ = −f^{1/2}₋ (f < 0 there), (ρ^λ)²₊(ρ^λ)²₋ = e^{−iπα}e^{iπα}/(ω₊ω₋) = 1 (and e^{−λ𝓡} also
satisfies it), JQ₀J^{−1} = −Q₀; on (−δ, 0), P₀^∞, f^{1/2}, 𝓡 are analytic and (ρ^λ)²₊/(ρ^λ)²₋ = e^{−2πiα}·ω₋/ω₊ = 1 (W₀ ∝ z^α
gives ω₊/ω₋ = e^{−2πiα}); Δ₁⁰ depends on ρ only through ρ². So Δ₁^{0,λ} is analytic in U_0 ∖ {0}, and |Δ₁^{0,λ}| ≤ C|z|^{−1}
(|f^{1/2}| ≍ |z|^{1/2}, |P₀^∞|^{±1} ≤ C|z|^{−1/4}): at most a simple pole. (This also supplies the structural reason for
the cancellation of half-integer powers that E_pgt1 Lemma E.5 verified by series.)
*(Coefficients.)* Given meromorphy with these pole orders, the Laurent coefficients are determined by finitely many
terms of the expansions in u = (z − 4c)^{1/2}, resp. z = −v², which check_e_plt1_sym.py computes exactly, keeping λ to
first order (ω → ω(1 + λ𝓡), 𝓡 = z^{1/2}u near 4c; ρ² → ρ²(1 − λ𝓡), 𝓡 = −v(4c + v²)^{1/2} on z = −v²), with the inputs
of check_e_sym.py (Q₀, X, Lemma E.4 closed forms). It asserts: odd powers of u (up to u³) and of v (v¹, v³) vanish,
including the λ-terms (a consistency check of the branches); the values above; A_r^{lin} does not depend on κ₂ and C₀^{lin}
not on the second Taylor coefficient of f. ∎

## 6. Proposition E′.5′: second-order small norm for p < 1

Let R := Q(P₀^∞)^{−1} outside Ū_0 ∪ Ū_r, QP̂₀^{−1} in U_0, QP̂_r^{−1} in U_r; circles clockwise.

**Proposition E′.5′ (PROVED-mod-cite: RH_px §5 (small norm, identification) as amended by RH_plt1, RH_plt1b; Paper 2 Prop.
frame F1 (no jump on the seams; uniform Cauchy bound; length O(n^p)), F4, F5; Lemmas E′.3, E′.5).** For 0 < p < 1, s > 1:
R = I + R⁽¹⁾(z)/n + O(n⁻² + n^{−1−2p}) uniformly at distance ≥ d from Σ_R, and R_k = R_k⁽¹⁾/n + O(n⁻² + n^{−1−2p}) (k = 1, 2)
for the moments at ∞, with

  R⁽¹⁾ = A₀/z + (A_r + λ_nA_r^{lin})/(z − 4c) + B_r/(z − 4c)²  (outside the discs),
  R_1⁽¹⁾ = A₀ + A_r + λ_nA_r^{lin},  R_2⁽¹⁾ = 4c(A_r + λ_nA_r^{lin}) + B_r,
  R⁽¹⁾(0) = −(C₀ + λ_nC₀^{lin}) − (A_r + λ_nA_r^{lin})/(4c) + B_r/(16c²).

*Proof.* E_pgt1 Prop. E.5′ verbatim, with three changes. (1) The jumps away from the circles: on the lips, Σ_v, the saturated
segment, Σ^△ and the top segment |J − I| ≤ Ce^{−n/C} resp. Cn^{−pn/4} (Paper 2 F5, all p); inside U_0 the pieces of
Σ_R are (a) the lips at ±θ_L, where the mismatch is O(n^{−K}min(1, |z|^K)) (RH_plt1b §2, RH_px Lemma 4.3 with the lip
constant 2π sin(θ_L/p) = 2π sin(π/4)), and (b) the two seam segments Γ± ∩ U_0, where Q has no jump (Paper 2 F1) but
P̂₀ carries the glue jump W̃_out/W̃_in = 1 − e^{∓2πit}, |e^{∓2πit}| = e^{−2πn|z|^{−1/p}}; after amplification by P̂₀
(|e^{±nφ}| ≤ e^{Cn|z|^{1/2}}, RH_plt1b §2 / RH_px Lemma 4.2(iii)) this gives |J − I| ≤ C exp(−n(2π|z|^{−1/p} − C|z|^{1/2}))
≤ C exp(−n(2πδ^{−1/p} − Cδ^{1/2})) (δ small), super-small uniformly and vanishing to all orders at 0. Hence
‖J − I‖_{L¹∩L²∩L^∞(Σ_R)} = O(1/n) on this (Q-frame) contour, and with the uniform Cauchy bound ‖𝒞₋‖_{L²→L²} ≤ C of Paper 2 F1
the equation R₋ = I + 𝒞₋(R₋(J − I)) gives ‖R₋ − I‖_{L²} = O(1/n) for n ≥ n₀. RH_px §5 / RH_plt1b are used only for the
identification of Q with this small-norm solution. (2) On the circles J − I = Δ₁/n + O(n⁻²) with Δ₁ =
Δ₁^{mod} + λ_nΔ₁^{lin} + O(n^{−2p}) (Lemma E′.3), so the circle contribution to (1/2πi)∫(J − I)ds/(s − z) is
(1/n)(1/2πi)∮_{cw}(Δ₁^{mod} + λ_nΔ₁^{lin})(s)ds/(s − z) + O(n⁻² + n^{−1−2p}). (3) Δ₁^{mod} + λΔ₁^{lin} is meromorphic in the discs
(Lemma E′.5, differentiate in λ: Δ₁^{lin} has the same analyticity and pole orders), so the clockwise circle integrals are
minus the residues: the principal parts for z outside, Σ Res Δ₁s^{k−1} for the moments, and the stated value at 0
(the point 0 is reached as in E_pgt1 Prop. E.5′: the super-small local jumps are dominated near 0, including the glue
jumps on the seam segments; for z on (−δ, 0) and s on a seam, |s − z| ≥ max(|s|, |z|), the angle at 0 being π − θ_s > π/2). The quadratic term ≤ ‖R₋ − I‖_{L²}‖J − I‖_{L²}/d = O(n⁻²). ∎

## 7. Proof of Theorem E′.1 and Corollary E′.6

### 7.1 b_n and α_n

As in E_pgt1 §7.1: Q₁ = P₁ + R_1, Q₂ = P₂ + R_1P₁ + R_2 (Paper 2 F8 and Lemma invariance), now with
R_1 = (A₀ + A_r + λ_nA_r^{lin})/n + O(n⁻² + n^{−1−2p}), R_2 = (4c(A_r + λ_nA_r^{lin}) + B_r)/n + O(·). The functionals are
linear in A at first order, so the λ_n-part adds to E_pgt1's result:
- b: n^{2p}b_n²/c² = 1 + i(A₂₁ − A₁₂)/(cn) + …; for A_r^{lin}, A₂₁ − A₁₂ = c²p(iα − i(α+2)) = −2ic²p, so the λ_n-part is
  i(−2ic²p)λ_n/(cn) = 2cpλ_n/n. Hence n^{2p}b_n²/c² = 1 − p(α+1)/n + 2cpλ_n/n + O(n⁻² + n^{−1−2p}) (λ_n² /n = O(n^{−1−2p})),
  and n^pb_n/c = 1 − (s−1)/(2n) + cpλ_n/n + O(·) = 1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2}).
- a: check_e_plt1_sym.py [3] (exact): n^pα_n/(2c) = 1 − p(α+2)/(2n) + cpλ_n/n + O(·), i.e. 1 − (s−1+p)/(2n) + κ_pn^{−1−p} +
  O(n^{−1−2p} + n^{−2}).
- Dividing: α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−2p} + n^{−2}) — the κ_p terms cancel. For the repo pairing,
  (n/(n−1))^p = 1 + p/n + O(n⁻²) gives α_{n−1}/(2b_n) = 1 + p/(2n) + O(n^{−1−2p} + n^{−2}) (the κ_p terms at n−1 and n differ by
  O(n^{−2−p}), so the n^{−1−p} parts cancel there too, and the remainder is O(n^{−1−2p} + n^{−2})). ∎

### 7.2 The chain

E_pgt1 §7.2 verbatim (identity (E.6.1), the Bessel column at 0 via DLMF 10.25.2 — on the negative axis near 0, which lies
in S_out for p < 1, ζ = n²f > 0 is in the I_α/K_α sector for the KMVV rays at π − θ_L as well), with three changes:
R⁽¹⁾(0) and (Q₁)₂₁ = −ic + A₂₁/n from Prop E′.5′ (λ_n-parts included); ρ = ρ^{λ_n}·(1 + O(n^{−2p})) near 0, where
ρ^λ = ρ^{mod}e^{−λ𝓡/2} and 𝓡(−v²) = −v(4c + v²)^{1/2}, so w⁽¹⁾ := lim_{z→0⁻}P₀^∞ρ^{σ₃}M(0, −iαf^{−1/4}/2)ᵀ acquires the
λ-part αcλ√(p+2)/2·(1, i)ᵀ (w⁽⁰⁾ is unchanged: it depends only on ρ(0) = 1); check_e_plt1_sym.py [4] evaluates (E.6.1)
exactly to first order in λ:

  n^pg_{n−1} = c(1 + (α + ½)/n + cpλ_n/n) + O(n⁻² + n^{−1−2p}) = c(1 + a/n + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})).

*Remainder.* The true ρ is ρ^{λ_n}(D²_{q₂}/q₂)^{−1/2}, q₂ = e^{−2E_n}; on z = −v², by (eq. szego-repr) and
|E_n(x) − E_n(0)| ≤ Cn^{−2p}|x| for 0 < |x| ≤ R₁/2 (Lemma F.1(iv), last clause) and |E_n| ≤ Cn^{−2p} on (0, 4c],
log(D²_{q₂}/q₂)(−v²) = vμ_n + o(v) as v → 0 (at fixed n) with |μ_n| ≤ Cn^{−2p} — only the v-linear coefficient
μ_n enters w⁽¹⁾ (the o(v) needs E_n(−v²) − E_n(0) = O(n^{−2p}v²), i.e. the negative-axis part of Lemma F.1(iv), last clause,
and the continuity of E_n at 0 from S_out); so w⁽¹⁾ changes by O(n^{−2p}) and n^pg_{n−1} by
O(n^{−1−2p}).
*Unfolding.* G_m = m^pg_m: n^pg_{n−1} = (1 + p/n + O(n⁻²))G_{n−1} and (n−1)^{−1−p} = n^{−1−p} + O(n^{−2−p}) give the G_m
formula; H_n = n^{2p}b_n²/(n^pg_{n−1}) = c(1 − (s−1)/n + 2κ_pn^{−1−p})(1 + a/n + κ_pn^{−1−p})^{−1} + O(·) gives the H_m
formula. In the symmetric variable (g_m = γ_{2m+1}², h_m = γ_{2m}²), m^{−1−p} = 2^{1+p}N^{−1−p}(1 + O(1/N)) for N = 2m and
N = 2m + 1, so the κ_p-terms of H_m and G_m both become 2^{1+p}κ_pN^{−1−p}, with no (−1)^N part; the 1/N terms are those of
E_pgt1 §7.2 (k₀, k₁ unchanged). ∎

## 8. Numerics (NUMERICAL; checks/check_e_plt1_num.py, .out)

Data: the Plan 62 machinery (SECOND §1: atoms k ≤ K exactly + a Gauss–Jacobi rule for the continuum tail; binary128 RKPW),
p ∈ {0.3, 0.5, 0.7, 0.9}, s ∈ {1.5, 2, 3}, n ≤ 1600, K = 3.2·10⁵ and 2K ("dK" = |K − 2K| difference, an estimate only).
Fits: least squares in the exponents {1 + i + jp} (SECOND §1), J = 4…7 terms, windows [f·1600, 1600], f = 0.1, 0.2, 0.3;
value = median, "fit" = half-range of the 12 estimates (estimates, not bounds; Rule N). Two kinds of rows: (a) the
coefficients of n^{−1} and n^{−1−p} from the free fit; (b) the n^{−1−p} coefficient after subtracting the proved 1/n term
(J = 3…6 exponents of {1 + i + jp} ∖ {1}), which removes the near-degeneracy of n^{−1} and n^{−1−p} for small p.

Results (`check_e_plt1_num.out`; "ok" is computed: |fit − prediction| ≤ max(fit half-range, dK, 10⁻⁸) — this tolerance
is itself an error *estimate*, not a bound): **131 of 132 rows ok**; the exception is the chain 1/n coefficient at
(p, s) = (0.9, 1.5), off by 5.9·10⁻⁸ (relative 1·10⁻⁶) against a half-range of 5.4·10⁻⁸. At p = 0.9 the fit basis contains
exponent pairs 0.1 apart, and that estimate moves by more than its half-range under changes of J and window and shrinks
with K (REVIEW_Plan67_A.md I3); it is not evidence against the theorem.
Highlights:
- d₁ = −(s−1)/2 at all twelve (p, s) (to ≤ 2.5·10⁻⁷ for p ≥ ½; to ≤ 8·10⁻⁵ at p = 0.3, s = 3, where the fit half-range is 4·10⁻³);
  the 1/n coefficients of n^pα_n/(2c) (−(s−1+p)/2), of α_n/(2b_n) (−p/2) and of n^pg_{n−1}/c (a) likewise.
- κ_p in b_n, α_n and the chain, rows (b): p = ½: −0.0848692 (prediction −0.0848692) for b at s = 1.5 (|diff| 5·10⁻⁹),
  2 (3·10⁻⁷), 3 (7·10⁻⁶); p = 0.7: |diff| ≤ 3·10⁻⁵ for b, a; p = 0.9: |diff| ≤ 1·10⁻⁴ for b, a; p = 0.3: |diff| ≤ 1.3·10⁻² with
  half-ranges up to 4·10⁻² (s = 3), and 1.4·10⁻⁵ at s = 1.5.
- No n^{−1−p} term in α_n/(2b_n): the fitted coefficient is ≤ 3.5·10⁻⁴ in modulus for p ≥ ½, and ≤ 10⁻⁴ except at (0.9, 3) (each within its half-range), as
  Theorem E′.1 says.
- The direct ratio n^{1+p}(y_n + (s−1)/(2n)) drifts towards κ_p as n^{−p} (its next term is n^{−1−2p}/n^{−1−p}), and, for
  p near 1, together with an n^{p−1} drift from the n⁻² term (e.g. p = 0.9, s = 3: 0.339 → 0.234 at n = 1600, consistent
  with a large d₂ > 0 term n^{p−1}d₂); the fits with the full exponent set separate the two.

Earlier data: the p = ½ fit "−0.0849 for s = 1.5, 2 and 3" of REVIEW_Plan62.md (bullet "Rule A claim on n^{−3/2} terms";
raw sequence in SECOND §1) is κ_{1/2} = −0.0848692…; the sharpness of the n^{−1−p}
remainder (an "ε = p" (E_ε) and no better) is visible at every p in the table.

## 9. Consequences (for 0 < p < 1)

Theorem E′.1 gives (E_ε) with ε = p at every (p, s), 0 < p < 1, s > 1. Hence, for 0 < p < 1:
- **SECOND Cor 3.3** (needs (E) at s and s + p): unconditional — d₁(s+p) = d₁(s) − p/2, and n(G_n − G_{n−1}) → 0 (also
  directly from Cor E′.6: n(G_n − G_{n−1}) = O(n^{−p})).
- **SECOND Thm 3.4** (needs (E_ε), ε > ½): its hypothesis holds only for p > ½, but its conclusion holds for all 0 < p < 1
  and is **superseded** by Theorem E′.1 (α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−min(2p,1)})). This also explains SECOND §5's
  remark that at p = ½ "the numerics for e₁ show no n^{−3/2} term in α_n/(2b_n)": b_n and α_n carry the same relative
  n^{−1−p} correction.
- **SECOND Cor 3.9**: unconditional for 0 < p < 1 (d₁ = −(s−1)/2 read off directly); **g(p) = 0 for every 0 < p < 1**.
- **SECOND Thm 3.10(d)**: the log-average form Σ_{j≤n}log(j^pb_j/c) = −((s−1)/2)log n + O(1) for every 0 < p < 1, s > 1
  (sum of Theorem E′.1; Σ j^{−1−p} converges).
- **Conjecture P62**: PROVED-mod-cite for 0 < p < 1, with the conjectured remainder O(n^{−1−min(1,p)}) = O(n^{−1−p}) for
  b_n, α_n and (by Cor E′.6) the chain; moreover the n^{−1−p} coefficient is identified (κ_p for b_n and α_n, 0 for
  α_n/(2b_n), κ_p for g_{n−1}, h_n and 2^{1+p}κ_p for γ_N²). With E_pgt1, P62 is now proved for every p ≠ 1.
- **SECOND §1 "Non-integer exponents"**: the observed n^{−1−p} term at p = ½ is κ_{1/2}n^{−3/2}: SECOND's sequence
  n(n^{1/2}b_n/c − 1) + ½ at s = 2 should be κ_{1/2}n^{−1/2} + O(n^{−1}): at n = 1600, κ_{1/2}/40 = −2.12·10⁻³ against the
  tabulated −2.0·10⁻³ (the ratio 0.72 per doubling there is 2^{−1/2} = 0.71 plus the O(n⁻¹) drift).
- **THEOREMS item 13**: (E) is now proved for every p ≠ 1; open only at p = 1 (and d₂ everywhere).

## 10. What remains open (GAP)

- **The next coefficients** (GAP): the n^{−1−2p} coefficient (needs the second-order λ-term of Δ₁ and the k = 2 term
  ζ(−2p)(z² − 1)/(2n^{2p}) of Lemma F.1 — both available in principle by the same method: it is the first-order
  response to the quadratic weight factor, plus the second-order response to the linear one) and the n⁻² coefficient d₂
  (needs Δ₂, the second Bessel/Airy corrections, and the second-order small-norm term). By Lemma F.1 the full asymptotic
  series of n^pb_n/c is plausibly in the exponents {1 + i + jp}, as SECOND §1's fit basis assumes (HEURISTIC).
- **p = 1** (not treated; E_pgt1 §9, worked on separately). Note only: at p = 1, λ_n = 2ζ(−1)/n = −1/(6n) is of the same
  order as 1/n, so the "n^{−1−p}" term becomes part of d₂; this is consistent with E_pgt1 §9's H_n = 1 + z/(6n).
- **Rule L** (novelty) not done. The ζ(−kp) constants are the Euler–Maclaurin/zeta-regularisation constants of the node
  set; second-order RH expansions with hard and soft edges are standard (KMVV §8 for fixed Jacobi weights).

## 11. Rule A (adversarial pass) — log

- *Is the n^{−p} variation of H_n real?* Yes: check_e_plt1_flat.out [B] recomputes 𝒢 − 𝒢(1) from Paper 2's literal
  definitions (no use of Lemma F.1) and finds ζ(−p)(z−1)n^{−p} + ζ(−2p)(z²−1)/(2n^{2p}) + ζ(−3p)(z³−1)/(3n^{3p}) to the
  expected accuracy, in S_in and in S_out, at p = 0.3, 0.5, 0.7.
- *Sign and orientation in (F.1).* Γ₊ has S_out on its left; Γ₋ has S_in on its left (Paper 2 Lemma seam(iii) proof). A sign
  error here would flip ζ(−p) to −ζ(−p) and κ_p to −κ_p; the flat check [B] and the coefficient fits (§8) both fix the sign.
- *Could the n^{−p} term enter b_n directly?* Only through the global parametrix, which is weight-invariant (Paper 2
  Lemma invariance; E_pgt1 §0: (P₁)₁₂(P₁)₂₁ = c², a(P₀^∞) = 2c exactly). The numerics confirm: the fitted coefficient of
  n^{−p} in n^pb_n/c − 1 (exponent p < 1, not in the fit basis) would show up as a non-convergent d₁ fit; it does not.
- *The choice ω → ωe^{λ𝓡} (not e^{−λ𝓡}).* Lemma F.2: D_q²/q = e^{+λ𝓡} for q = e^{−λx}; with H_n ∝ e^{−λ_nz}, λ_n =
  2ζ(−p)n^{−p} < 0. The first scratch computation in this plan extracted the λ-coefficient of a non-polynomial expression and
  produced spurious odd powers (v¹ terms at the hard edge); with the λ-expansion made polynomial before extraction the odd
  powers vanish, as Lemma E′.5's structural argument requires. Kept as a lesson: the odd-power assertions are a real test.
- *s-independence.* A_r^{lin} depends on α, but the b- and a-functionals of λA_r^{lin} are cpλ for every α: the s-dependence
  cancels, as the p = ½ grid (REVIEW_Plan62.md, bullet "Rule A claim on n^{−3/2} terms": n^{−3/2} coefficient −0.0849 at s = 1.5, 2, 3) suggested.
- *Hard-edge residue A₀ and the seams.* A₀^{lin} = 0: the factor e^{−λ𝓡/2} in ρ is 1 + O(|z|^{1/2}), which cannot change the
  simple-pole residue at 0; it changes only C₀ (and the chain). Seam crossings of ∂U_0: the glue jumps are super-small and the
  bounds of Lemma F.1(iv) include boundary values.
- *Uniformity in p near 0.* All constants depend on p; as p → 0⁺ the remainder O(n^{−1−2p}) degenerates (consistent with the
  slow convergence of the p = 0.3 fits, §8). Not claimed uniformly.
- *Converse / scope.* Lemma F.1 uses p < 1 only through the seam construction; its moment formula (iii) is valid for every
  p > 0 for the seam integral itself. The Bessel parametrix uses p < 1 only through θ_L < π.

## 12. Integration (applied after merging master dea41ef, i.e. after Plan 66; reconciled with the Plan 66 wording)

*Applied 2026-10-15:* the SECOND.md and THEOREMS.md changes below are made, tagged "Plan 67, E_plt1.md; not REVIEWED"
(SECOND: status line, rows P62/Cor 3.3/Thm 3.4/Cor 3.9/Thm 3.10/§4 (E)/§4 g(p), new row Thm E′.1, P62 heading, §1 note, §4 title
and Plan 67 paragraphs, §5 Thm 3.4 bullet, §6 checks; THEOREMS §2.10 heading and rows, new row, §4 item 13 update).

Labels to apply carry a "Plan 67" tag; until Rule R they read "not REVIEWED". Nothing here touches p = 1.

**RH/CITATIONS.md** (added in this plan, since Rule C requires the record): new entry "(DLMF-zeta, Plan 67)" — DLMF 5.2.1,
25.2.1, 25.4.1, quoted from the pages fetched 2026-10-15, with the hypothesis checks of Lemma F.1(iii); and a "(Plan 67 reuse)"
entry listing the entries reused (as E_pgt1's "(Plan 65 reuse)", plus "(KMVV, angle freedom; Plan 15b)").

**SECOND.md** (do not edit here; for the integrator):
- Status block: add a "*Plan 67 update*" line: E_plt1.md proves (E) and all constants of Conj. P62 for 0 < p < 1, with the
  n^{−1−p} term identified (κ_p = 2pc(p)ζ(−p)).
- Summary rows:
  - "Conj. P62": CONJECTURE only for p = 1; **PROVED-mod-cite for 0 < p < 1** (remainder O(n^{−1−p}) for b_n, α_n and the
    chain, as conjectured; E_plt1 Thm E′.1, Cor E′.6) (Plan 67).
  - "Cor 3.3": add "**unconditional for 0 < p < 1** (E_plt1 Thm E′.1 gives (E_p))" (Plan 67).
  - "Thm 3.4": add "for 0 < p < 1 superseded by E_plt1 Thm E′.1 (α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−min(2p,1)}))" (Plan 67).
  - "Cor 3.9": add "**unconditional for 0 < p < 1**" (Plan 67).
  - "Thm 3.10": add "every 0 < p < 1, s > 1: log-average coefficient −(s−1)/2 with O(1), PROVED-mod-cite (sum of E_plt1
    Thm E′.1)" (Plan 67).
  - "§4 (E)": "PROVED-mod-cite for p > 1 (ε = 1) and **for 0 < p < 1 with ε = p (sharp; E_plt1 Thm E′.1)**; GAP only for p = 1"
    (Plan 67).
  - "§4 g(p)": "g(p) = 0 for every p ≠ 1 … ; p = 1: CONDITIONAL on (E)" (Plan 67).
  - New row "Thm E′.1, Cor E′.6, Lemma F.1 (Plan 67)": statement as in E_plt1's summary table, label PROVED-mod-cite
    (RH_plt1b; RH_px §5; Paper 2 Lemmas seam/corner/szego/airy/invariance, Frame Prop.; E_pgt1 Lemmas E.3–E.5; KMVV §6 incl.
    angle freedom; DLMF 5.2.1, 25.2.1, 25.4.1, 9.7.2, 9.7.5–6, 10.17, 10.25.2, 10.40.1–4) + exact computer algebra.
- Conjecture P62 heading paragraph: add "Plan 67: PROVED-mod-cite for 0 < p < 1 (E_plt1.md)"; the conjecture is now open only
  at p = 1.
- §1 "Non-integer exponents": the heuristic sentence ("far field … first correction of relative size n^{−1}·(n^{−p}/1)") can
  point to E_plt1 Lemma F.1 / Thm E′.1: the n^{−1−p} coefficient is κ_p = 2pc(p)ζ(−p) (−0.08487 at p = ½), s-independent,
  equal for b_n and α_n, absent in α_n/(2b_n).
- §4 title "GAP for p ≤ 1" → "GAP for p = 1 (p > 1: E_pgt1.md; 0 < p < 1: E_plt1.md)"; a Plan 67 paragraph after the Plan 65 one;
  the "p ≤ 1" paragraph: the 0 < p < 1 half is closed (step 3 is replaced by Lemma F.1: H_n flat only to O(n^{−p}), with the
  explicit linear part, entering at n^{−1−p}; "(E_ε) with ε ≤ p" is attained with ε = p).
- §5 Rule A, Thm 3.4 bullet: the "no n^{−3/2} term in α_n/(2b_n)" observation is explained (E_plt1 §9).
- §6 Checks: add `checks/check_e_plt1_sym.py`, `check_e_plt1_flat.py`, `check_e_plt1_num.py` (.out) — E_plt1.md (Plan 67).

**THEOREMS.md §2.10:** heading: add "and Plan 67: (E) for 0 < p < 1 (research/G1/RH/second_order/E_plt1.md; not REVIEWED)".
Rows: "Conjecture P62" (PROVED-mod-cite for 0 < p < 1; CONJECTURE only at p = 1); "Cor 3.3, Thm 3.4" (unconditional for
0 < p < 1, Thm 3.4 superseded there); "Prop 3.7, Thm 3.8, Cor 3.9" (3.9 unconditional and g(p) = 0 for 0 < p < 1); "Thm 3.10"
(log-average form for every p ≠ 1); "(E), g(p)" ((E) PROVED-mod-cite for all p ≠ 1, ε = p for p < 1; GAP only at p = 1;
g(p) = 0 for p ≠ 1); new row "Thm E′.1, Cor E′.6 (Plan 67)" (0 < p < 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} +
O(n^{−1−2p} + n^{−2})), n^pα_n = 2c(1 − (s−1+p)/(2n) + κ_pn^{−1−p} + …), κ_p = 2pc(p)ζ(−p); α_n/(2b_n) = 1 − p/(2n) +
O(n^{−1−2p} + n^{−2}); n^pg_{n−1} = c(1 + a/n + κ_pn^{−1−p} + …); k₀, k₁ as for p > 1; location
research/G1/RH/second_order/E_plt1.md, checks/check_e_plt1_*.out). Optionally a row "Lemma F.1 (Plan 67)" (seam band factor:
log H_n(z) − log H_n(1) = −2Σ_kζ(−kp)(z^k − 1)/(kn^{kp}) asymptotically).
**§4 item 13:** append "*Update (Plan 67, not REVIEWED; E_plt1.md):* (E) is PROVED-mod-cite for 0 < p < 1 with the sharp
remainder: n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), κ_p = 2pc(p)ζ(−p), and the same for α_n and the
chain; all constants of Conjecture P62 for 0 < p < 1; g(p) = 0 for p < 1. Still open: (E) at p = 1; d₂ and the n^{−1−2p}
coefficient; the −1/24 conjecture." and change "Still open: (E) for 0 < p ≤ 1 and g(p) for 0 < p < 1 (GAP)" accordingly.
