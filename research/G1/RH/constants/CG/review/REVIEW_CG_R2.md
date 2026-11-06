# REVIEW_CG_R2 — Rule R second reader for CG.md §9 (Theorem C) and §10

Reviewer: independent agent (Rule R), 2026-11-05, branch `g1-constants`. Scope: CG.md §9 (Theorem C, p = 1, every s > 1)
and §10 only (§§0–8 were reviewed in REVIEW_CG_R1.md). I re-derived G1–G8 from the note, from Paper II
(`papers/paperII/sec11_pone.tex` §`sec:pone-first`, `appH_pone.tex`) and from the quotes in `research/G1/RH/CITATIONS.md`,
and wrote my own numerics (`review/checks/r2_lambda.py` → `r2_lambda.out`). I did not edit CG.md and did not commit.

## Verdicts

| # | Step | Verdict |
|---|---|---|
| 1 | G3: ir ∈ Ω∞; u = 𝖬₀Ve₁e^{Ng−Nl/2}/(ED) | OK |
| 2 | G3: exact cancellation of e^{±N(l/2−g)} against e^{−Nφ^{KV}} | OK |
| 3 | G4(ii)–(iii): Van (4.27) in sector II, W = (−z)^a, cancellation of η^{±a}, r^{∓a} | OK |
| 4 | G4(iv), G5: E(0)² = π/2, D(ir) → 1, 𝔳₀(0) = 4e^L, e^L = √2ie/√π, f′(0) = πψ(0) = 1/3 | OK |
| 5 | G6–G7: det 𝒩 = 1, |B(ir)| ≤ C uniformly via the weighted Cauchy estimate | OK (needs `lem:pone-mismatch`, not only `prop:pone-first`(ii); see §5) |
| 6 | G1–G2, G8: N = 2m − 1, fold, normalisation κ, assembly | OK |
| 7 | Independence from Theorem B (Rule X) | OK |
| 8 | Independent numerics at s = 1.35, 4.2 | OK, lim r_m − 1 = 4e−42 and −7e−30 |
| 9 | Rule C (quotes and hypotheses) | OK |
| 10 | §10 vs E2_pgt1 Cor E2.7 / Rem E2.12–E2.13 | OK (wording nit N5) |

No ERROR, no SERIOUS GAP, no FIXABLE GAP. Only notation/wording nits N1–N5.

## 1. Ω∞ and the formula for u (G3)
Near 0, inside U(0,ε), Σ_X consists of the band and four lips which App. H takes as f-preimages of the rays
arg ζ = ±π/4, ±3π/4, so they lie in |arg(±z)| ∈ [π/4−η, π/4+η]; the Σ^△ contours belong to the saturated interval (2, k_n)
(nodes Z_k = N^{1/2}k^{−1/2} with k < N/4). So ir (0 < r ≤ ε/2) is in Ω∞. There (3.11) R = U, (4.12) Q = T, (4.1)
T = e^{−Nlσ₃/2}Re^{(−Ng+Nl/2)σ₃}, (5.1) V = N^{(α_W−½)σ₃}Q E^{σ₃}D^{σ₃}. Hence
Ve₁ = N^{½}e^{−Nl/2}·Ue₁·e^{−Ng+Nl/2}ED (first component scaled by the diagonal), i.e.
u = Ue₁ = e^{Nlσ₃/2}N^{−σ₃/2}Ve₁·e^{Ng−Nl/2}/(ED). This is G3 with α_W = 1. I checked that D (WLXZ (2.6)) is analytic in
ℂ₊: with −1/z² = e^{πi}/z², arg(−N/z²) ∈ (−π, π), and Γ(1 − N/z²) has poles only for real z. P₀ involves 𝔳₀ = e^L(4−z²)𝖰_{m_S}
(entire 𝖰), not e^{j(N/z²)}, so P₀ is analytic across iℝ; this is what makes the evaluation on iℝ legitimate even though
w and Π have zeros on iℝ (they do not enter in Ω∞). OK.

## 2. Cancellation of the exponentials
V = σ₃HP₀σ₃ gives Ve₁ = σ₃HP₀e₁ = σ₃H𝖡_NΨ^{FH}(ξ)e₁·W_𝔳^{−1}e^{−Nφ^{KV}}, and φ^{KV} = −φ = g − l/2, so
e^{−Nφ^{KV}} = e^{N(l/2−g)}. With the factor e^{Ng−Nl/2} from §1 the product is exactly 1 (same branch of g: both are the
ℂ₊ functions). OK.

## 3. Sector II and the singular powers
f is odd with real Taylor coefficients and f′(0) > 0, so f(ir) = iη(r), η real, η = Nf′(0)r(1+O(r²)); the right side of
iℝ near 0 is f^{−1}(II). KV (5.9): W = (−z)^a there, so W(ir⁺) = r^a e^{−iπa/2}. Van (4.27), first column:
e^{−aπi/2}√πξ^{1/2}(I_{a+½}(η), −iI_{a−½}(η)) with ξ^{1/2} = e^{iπ/4}η^{1/2}. Dividing by W the phases e^{∓iπa/2} cancel, and
with DLMF 10.25.2: η^{1/2}I_{a+½}(η)r^{−a} = (η/r)^a·2^{−a−½}ηβ_{a+½}(η²), η^{1/2}I_{a−½}(η)r^{−a} = (η/r)^a·2^{−a+½}β_{a−½}(η²).
This is G4(iii) (ν = a ± ½ > −1, so β_ν(0) = 1/Γ(ν+1) is finite). The left-sector check of Rule A item 2 is also correct:
z^a = e^{iπa}(−z)^a at ir and Van (4.28) carries e^{+aπi/2}. OK.

## 4. Scalars
E(z) = √(2π)(4−z²)^{−1/2} at α_W = 1, E(0)² = π/2. At z = ir, T := −N/z² = N/r² > 0 and
D = Γ(1+T)e^TT^{−T−½}/√(2π) = e^{j(T)} → 1 (r → 0, N fixed). 𝔳₀(0) = 4e^L (𝖰(0) = 1); e^L = √2ie/√π from L of the (5.9)
context at α = 1. τ² = iπ(η/r)^{2a}/(E²D²𝔳₀) → i(Nf′(0))^{2a}/(2e^L) = (√π/(2√2e))(Nf′(0))^{2a} > 0. The branch of 𝔳₀^{1/2}
does not matter (only 𝔳₀ and det 𝖡_N enter). G5: 4arcsin(x/2)/x³ = 2/x² + 1/12 + O(x²), √(4−x²)/x² = 2/x² − 1/4 + O(x²),
so ψ(0) = 1/(3π) and f′(0) = πψ(0) = 1/3 (f(x) = π∫₀^xψ from KV (5.6) and φ^{KV}_+(x) = πi∫_x^∞ψ). OK.

## 5. Determinant and the bound on B (the question asked)
det 𝖬₀σ₃ = −1; det V = det P₀ = det Ψ^{FH} = 1 (Van (4.53)), so det 𝖡_N = det H = det 𝒩 = 1. Scalars factor out of
det[(τw)′, τw] = τ²det[w′, w], and det[(𝒩v)_r, 𝒩v] = det[v_r, v] + det[Bv, v]. With d/dz = −i d/dr:
det[u_z,u] = iτ²(det[v_r,v] + det[Bv,v]); det[v_r,v] → −i2^{−2a}Nf′(0)/(Γ(a+½)Γ(a+3/2)). All as in G6.

G7. `prop:pone-first`(iv) supplies X = I + 𝒞(X₋(J−I)) off Σ_X and ‖X₋−I‖_{L²} ≤ C/N; (i)–(iii) give ‖J−I‖_{L¹∩L²} ≤ C/N.
**The sup bound of (ii) alone is not enough**: with only |J−I| ≤ CN^{−2m_S−1} on the band and lips, ∫|J−I||w−ir|^{−j}|dw|
diverges logarithmically (j = 1) or like 1/r (j = 2) as r → 0. What closes it is the structured bound of
`lem:pone-mismatch`, |J_H−I| ≤ CN^{−6m_S−3}(N|w|)^{δ_m} for N|w| ≤ 1 with δ_m = 4m_S+2−2|a| ≥ 2 (from m_S ≥ max(1,|a|/2)),
which G7 does use. I re-derived it from App. H: on the lips J_H − I = (𝖶_N^{−1}−1)𝖡_N(Ψ₊Ψ₋^{−1}−I)𝖡_N^{−1}, with
|𝖶_N−1| ≤ C(|z|²/N)^{2m_S+1} (Lemma `lem:pone-stirling`) and |Ψ₊Ψ₋^{−1}−I| ≤ Cρ^{−2|a|} (KV (5.21)–(5.22), det Ψ = 1);
writing |z| = ρ/N gives N^{−6m_S−3}ρ^{δ_m}. The discarded lip terms are O(e^{−cN/|z|²}·poly), below this bound. With
|w − ir| ≥ sin(π/4−η)·max(|w|, r) on band and lips, I get, for j ∈ {1,2},
∫|J−I||w−ir|^{−j} ≤ C(N^{−6m_S−4+j} + N^{−2m_S−1}(N^{j−1}+log N)) ≤ CN^{−2m_S}log N and
(∫|J−I|²|w−ir|^{−2j})^{1/2} ≤ CN^{−2m_S+½}, both ≤ C/N for m_S ≥ 1; the rest of Σ_X is at distance ≥ ε/2. So
|X(ir)−I| + |∂X(ir)| ≤ C/N uniformly in 0 < r ≤ ε/2. With |𝖡_N^{±1}| ≤ C (`lem:pone-fh`(ii)) and Cauchy's estimate on
U(0,ε/2), |B(ir)| ≤ C uniformly. v(0) is N-independent, so the error det[Bv,v] = O(1) against a main term ∝ N (relative
O(1/N)); det[Bv,v](ir) has a limit because every other term does. OK.

## 6. Index bookkeeping, fold, normalisation, assembly
Fold: ½(P(y)+P(−y)) keeps P(0) and does not increase ∫P²dν_s (convexity + symmetry); even polynomials of degree ≤ 2m−2 are
Q(y²), deg Q ≤ m−1, so λ_m(0;σ_{1,s}) = λ_{2m−1}(0;ν_s) = 1/K_{2m−1}(0,0;ν_s), and K_{2m} = K_{2m−1} since R_{2m−1} is odd.
Masses: ½k^{−s} = (√(2π)/(2e))w_d(y_k)e^{j(1/y_k²)}(y_k²)^a (w_d(±k^{−1/2}) = ev_k, k^{−3/2} = √(2π)e^{j(k)}v_k). After
z = N^{1/2}y with weight wF, w = N^{1/2}w_d (WLXZ (3.4)), (z²)^a = N^a(y²)^a, the y-problem is the residue problem of
μ_Y = κν_s, κ = 2eN^a/√(2π). Residue form: Y₂₁ = P_{N−1}/h_{N−1} (coefficient of z^{−N} in Y₂₂ is 1), so
K_N(0,0;μ_Y) = det[Y′e₁, Ye₁](0) by Christoffel–Darboux; (3.1) gives det[U′e₁,Ue₁] = N^{−1/2}K_N(μ_Y); K(ν_s) = κK(μ_Y).
Assembly: κN^{1/2}·(√π/(2√2e))(Nf′)^{2a}2^{−2a}Nf′/(Γ(a+½)Γ(a+3/2)) = N^{a+½}(Nf′/2)^{2a+1}/(ΓΓ) = (N³f′²/4)^ζ/(Γ(ζ)Γ(ζ+1)),
= (N³/36)^ζ/(Γ(ζ)Γ(ζ+1)) at f′ = 1/3. With N = 2m−1: λ_m = Γ(ζ)Γ(ζ+1)(36/8)^ζm^{−3ζ}(1+O(1/m)), and c(1) = ½
(I(1) = π/4) gives (c(1)·9)^ζ = (9/2)^ζ. At s = 3/2: 3π√2/4·m^{−3/2}, Theorem B's value. `prop:pone-first` is stated for all
N ≥ N₀ (no parity restriction), so odd N = 2m−1 is allowed. OK.

## 7. Circularity (Rule X)
§9 uses `prop:pone-first`, `lem:pone-weight`, `lem:pone-fh`, `lem:pone-mismatch` (App. H §§`app:pone-setup`–`app:pone-ident`),
none of which uses `cor:tc`, `lem:pone-tc` or the TC comparison of §`sec:pone-tc` (the Airy parametrix P^{(3/2)} is WLXZ's
model, not Theorem B). Theorem B is not used. OK.

## 8. Independent numerics (`review/checks/r2_lambda.py` → `r2_lambda.out`)
Own code, different from cglib: λ_m = 1/K_m(0,0), K_m = Σ_{k<m}(L^{−1}e₀)_k², L the Cholesky factor of the Hankel matrix
[ζ(s+i+j)] (exact moments), all in Arb ball arithmetic (python-flint), M = 120, 5000 and 10000 bits.
r_m := λ_m m^{3(s−1)}/(Γ(s−1)Γ(s)(9/2)^{s−1}).
- s = 1.35: r_120 − 1 = −1.52e−3; Neville/Richardson in 1/m, K = 4, 8, 12, 16, 20: lim − 1 = −3.4e−13, 5.6e−22, 4.8e−29,
  8.3e−36, 3.9e−42.
- s = 4.2: r_120 − 1 = −0.119; lim − 1 = −1.1e−6, −2.4e−12, −3.6e−18, −5.1e−24, −7.2e−30.
- Ball radii ≤ 1e−825 (5000 bits); the 5000- and 10000-bit runs agree in every printed digit. The limits are NUMERICAL
  (Rule N.2): extrapolation is not an error bound.
- Side result (F7 at p = 1): the 1/m coefficient of r_m (Richardson K = 12 of m(r_m−1)) is −0.18375000 and −15.360000, equal
  to −3ζ²/2, the value F7 predicts (λ = C(m+ζ/2)^{−3ζ}). This supports §10's F7 CONJECTURE at p = 1 for two more s.

## 9. Rule C
Every external formula used in §9 is quoted in CITATIONS.md with its hypothesis: WLXZ (2.1), (2.3), (2.6), (2.14), (2.15),
(3.1), (3.4), (3.11), (4.1), (4.12), (4.19), (5.1), L of the (5.9) context, (5.8), (6.34)–(6.37) ("α is a positive parameter",
α_W = 1); KV (5.6), (5.9), (5.21)–(5.22), (5.26)–(5.30); Van (4.27), (4.28), (4.53), "λ > −1/2" (λ = a > −½); DLMF 10.25.2,
5.5.1, 5.11.1. The CG §9 "Also used in" lines are present (KV, WLXZ Plan 53, WLXZ Plan 66, Van Plan 66, DLMF, DLMF-5). The
inherited dependence on WLXZ (5.8), (6.34) and the Cauchy bound after (6.35) is stated in CG §9 and in the status table. OK.

## 10. §10
Cor E2.7's λ_n is the same quantity (deg R ≤ n−1); its exponent −(p+2)(s−1)/p equals −E; C is unspecified there (C > 0);
Remark E2.13 gives O(n^{−θ}) with non-explicit C; Remark E2.12's CG reading matches. E2_pgt1 does not cover p ≤ 1. The
consistency numbers quoted match `checks/check_e2_consistency.out`. Nothing conflicts.

## Nits (no effect on the proof)
- **N1.** Notation clash: §9 writes 𝒩 := H𝖡_N, while Paper II's 𝒩 (WLXZ (5.11)) and 𝒩_s appear in the same section
  ("𝖡_N (which contains 𝒩_s, …)"). Rename (e.g. 𝖦 := H𝖡_N).
- **N2.** κ denotes both 2eN^a/√(2π) (G2) and sin(π/4−η) (G7); η denotes both the lip-angle tolerance and η(r). Rename one of each.
- **N3.** G3 "H = σ₃𝖷σ₃": Paper II says only "X = VP₀^{−1} in U(0,ε) after conjugation by σ₃"; say "H = 𝖷 up to conjugation by σ₃".
- **N4.** G7: state explicitly that the refined bound of `lem:pone-mismatch` (not `prop:pone-first`(ii)) is what makes the
  j = 1, 2 integrals uniform in r; the text does use it, but the header line "(from Paper II as in S6)" suggests (ii) suffices.
- **N5.** §10(ii): "the unshifted −E misses by 5.6e−3 … 7e−4" is the (1.5, 2) row only; over the four rows the range is
  1.4e−2 … 2.5e−4.

## Label recommendation
Theorem C: **PROVED-mod-cite + REVIEWED** (inheriting Paper II's stated dependence on WLXZ (5.8), (6.34) and the Cauchy bound
after (6.35)). N1–N5 are optional edits. §10: as written; F7 remains CONJECTURE (NUMERICAL), with the p = 1 evidence of §8 added.
