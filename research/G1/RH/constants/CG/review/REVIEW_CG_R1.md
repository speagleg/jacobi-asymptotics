# REVIEW_CG_R1 — Rule R second reader for CG.md (Theorem A for p≠1, Lemma L, Theorem B)

Reviewer: independent agent (Rule R), 2026-11-05, branch `g1-constants`. Scope: CG.md §§0–5, 7–8 as they stand. The p=1
general-s section (GAP-1) was not reviewed. I re-derived the steps from the note and from Paper II's text
(sec4_frame, sec5_outer, sec8_classical, sec10_plt1, sec2_prelim, sec11_pone), and wrote my own checks in `review/checks/`.
I did not edit CG.md.

## Verdicts

| # | Step | Verdict |
|---|---|---|
| 1 | S1: K_n(0,0) = n^p det[u'(0),u(0)] | OK |
| 2 | S2–S3: first column through Q; F·W̃ = υ w_n^{1/2}(−z)^{α/2} | OK (wording nit F3) |
| 3 | S6: uniform bounds on 𝖱−I, 𝖱', Ǎ' along iy | OK (small gap F2 for p<1) |
| 4 | S4–S5, S8: Bessel Wronskian, \|f'(0)\| | OK |
| 5 | Lemma L | OK |
| 6 | Theorem B: kernels and constants | OK |
| 7 | Rule C | FIXABLE (F1) |
| 8 | Independent numerics (0.6,1.9), (2.5,5) | OK, limit −1 = 2e−8 and −4e−8 |

No ERROR and no SERIOUS GAP.

## 1. S1 (scaling, signs, z → 0)
Paper II eq:Y-solution has Y₁₁ = P_n and Y₂₁ = P_{n−1}/h_{n−1}, with no 2πi factor. eq:U gives
U(X) = n^{pnσ₃}Y(Xn^{−p}), so U₁₁(X)U₂₁(Y) = P_n(x)P_{n−1}(y)/h_{n−1}. With x − y = n^{−p}(X − Y), Christoffel–Darboux
gives K_n = n^p[u₁(X)u₂(Y) − u₂(X)u₁(Y)]/(X−Y), and the diagonal limit is n^p(u₁'u₂ − u₂'u₁), which is n^p det[u',u].
Here n = m, because K_m sums over k < m and Y is built from P_m and P_{m−1}. The poles accumulating at 0 are a red herring:
by lem:interp the poles sit in the second column of U only, and u = Ue₁ is a pair of polynomials. So det[u',u](iy) →
det[u',u](0) as y → 0, by plain continuity. Representation (3) holds on the open set Ω_∞ ∩ D(0,δ) ∩ ℂ₊ (∩ S_out when p<1),
which contains iy, so differentiating it there is legitimate. The left side has a limit; on the right, s², ζ' and
det[c',c] have limits; so det[Bc,c](iy) also has a limit, and only its bound O(n) is used. OK.

## 2. S2–S3 (scalar identity)
From eq:VM and eq:Q: U = 𝖬QD_W^{−σ₃}F^{−σ₃}e^{−nφσ₃} in Ω_∞, with 𝖬 = e^{nγ_pσ₃}C_∞^{−1}D_∞^{σ₃}, constant, diagonal,
det 1. Then Qe₁ = 𝖱P̌₀e₁ = 𝖱Ǎ(2πn)^{σ₃/2}σ₃Ψ_αe₁·e^{−2ζ^{1/2}}ρ_n^{−1} (eq:Pcheck), and ρ_nD_W = W̃. In ℂ₊,
e^{nφ} = (−1)^n e^{−2ζ^{1/2}} (lem:signs(iii)). This gives (2).

**p>1.** By lem:outer, F = υ₊D̃BK. By eq:G-def and eq:Wtilde, e^{−G} = e^{j}B^{−1} = (D̃B)^{−1}. Both square roots of
(4c−z) are principal with cut [4c,∞), so they cancel exactly. Result: FW̃ = υ₊w_n^{1/2}(−z)^{α/2}.

**p<1.** iy lies in S_out = {|arg z| > πp/2}. There F = B_out K e^χ (lem:outer), and eq:plt1-G gives
e^{−G} = (1−z/2πn)^{−1/2}e^{−χ}, with B_out = (1−z/2πn)^{1/2}. Result: FW̃ = w_n^{1/2}(−z)^{α/2}. W̃ is defined there
(eq:plt1-Wtilde: D(0,2δ) minus [0,2δ) and the seams).

iy is outside the lens: the lips stay in |arg| ≤ 5θ_lip/4 = 5π/12 for p>1 and 5πp/16 for p<1. It is in U₀ because
y ≤ δ/4. The formula used is exactly Paper II's own formula in the proof of prop:classical, Step 2 ("𝖱 = ±c_n U(FW̃)^{σ₃}…"),
read in reverse. **F3 (nit):** S3 calls B and χ "global n-dependent constants". They are functions; what happens is an
exact pointwise cancellation. Reword.

## 3. S6 (uniformity as y → 0)
- The hypothesis |J_𝖱−I| ≤ C_K n^{−K} min(1,|w|^K) on Σ_𝖱 ∩ U₀ is provided by Paper II. For p>1 it holds on the lips and
  on (−δ,0) (lem:mismatch-classical, prop:classical(ii)). For p<1 it holds on the lips and the seam segments
  (lem:plt1-param, prop:plt1-small).
- ‖𝖱₋−I‖_{L²} ≤ C/n and 𝖱 = I + 𝒞(𝖱₋(J−I)) off Σ_𝖱 come from (iii)–(iv) of those propositions.
- For w on any contour piece in U₀, the angle between w and iy is at least a fixed positive angle φ₀ (π/12 for the lips
  when p>1, ≥ 3π/16 for the lips when p<1, π(1−p)/2 for the seams, π/2 for (−δ,0)). Hence |w − iy| ≥ sin(φ₀)|w|, and
  ∫|w|^{K−j}|dw| < ∞ for K = 3, j ≤ 2. The z-derivative of a Cauchy integral at a point off the contour is the kernel
  (w−z)^{−2}, so nothing is needed "up to the endpoint 0": the bound is uniform in y because of the factor |w|^K.
- Circles and far arcs: |w − iy| ≥ 3δ/4. OK.
- Ǎ': for p>1 the split Ǎ = Ǎ^a + Ǎ^s (lem:classical-param(i)) gives |Ǎ^a'| ≤ C on D(0,δ/2), by Cauchy's estimate.
  The density of Ǎ^s is bounded by C|w|^{−1}|𝔢(w)|, from the crude bound |Ǎ| ≤ C|z|^{−1/2} and eq:A-jump.
- **F2 (fixable gap, p<1).** The note's (P5) asserts the same density bound on the seams. Paper II's proof of
  lem:plt1-param(i) only says "the rest … is that of lem:classical-param(i)" and never states |Ǎ| ≤ C|z|^{−1/2} for p<1.
  The bound does hold: |P^∞₀| ≤ C|z|^{−1/4} (eq:Pinf0-bound), |ρ_n^{±1}| ≤ C (eq:plt1-rho-mod) and |f^{±1/4}| ≤ C|z|^{±1/4}.
  Write this line out in (P5).
- With these, |B| = |Ǎ^{−1}𝖱^{−1}𝖱'Ǎ + Ǎ^{−1}Ǎ'| = O(1). Then |det[Bc,c]| = O(n): the worst term is B₂₁c₁², with
  c₁² ~ 2πnβ₁². The main term is O(n²), so the relative error is O(1/n). OK.

## 4. Constants (S4, S5, S8)
- **Symbolic.** β₁(0) = 1/Γ(α+1), β₁'(0) = 1/Γ(α+2), β₂(0) = −πiα/Γ(α+1), β₂'(0) = −πi(α+2)/Γ(α+2). These give
  W = 2πi/(Γ(α+1)Γ(α+2)). The series for β₂ is re-derived from ζ^{1/2}I_α'(2ζ^{1/2}) = ζ^{α/2}(α/2·β₁ + ζβ₁').
- **Normalisation.** 𝔞(0) = 2C_* and f = −(π²/4)z𝔞² give f'(0) = −π²C_*². From B(a_*,½) = 2I(p), p·a_* = (p+2)/2 and
  (4c)^{−1/p} = 2I/π: C_* = 1/(π(p+2)√c), so |f'(0)| = 1/(c(p+2)²).
- **Exponent and sign.** w_n^{−1}·2πi·f'(0) = p|f'(0)|n^{pα} > 0. The power of n is
  p + 2 + 2α + pα = (p+2)(α+1). This is (★).
- **Numerical** (`rev_identities.py` → `.out`).
  - The C_* closed form agrees with x^{1/2}ψ*(x), computed by quadrature of the incomplete-beta form, to 1e−14 at
    p = 0.3, 0.6, 2.5, 4.
  - The Wronskian computed from mpmath `besseli` (not from the series) matches 2πi/(ΓΓ) at α ∈ {−0.7, 0, 0.5, 0.6, 3}.
  - The branch identity (−X)^{−α/2}ζ^{α/2} = (n²F₁)^{α/2} holds at X = iy to 1e−42.

## 5. Lemma L
- The steps check out: P* = Σv_kp_k/S_m, ε_m = vᵀJ_mv/S_m, and the coefficient of v_k² is a_k + b_k + b_{k+1}. The
  Toeplitz step is correct, as are the two test-function inequalities. (g ≤ 1+η+(c₂/δ_η)x holds because g ≤ c₂ ≤ c₂x/δ_η
  for x > δ_η; the same argument gives the bound on 1/g.)
- An atom at 0 is excluded by λ_m(0;μ) → 0.
- The hypotheses are met in Theorem B. g(1/k) = e^{j(k)} lies in [1, e^{1/12}] and tends to 1. Both measures sit on {1/k};
  a_k, b_k = O(1/k) by lem:pone-tc and cor:tc. (The Remark is right: essential spectrum {0} makes J compact.)
- **F6 (Rule L).** Lemma L is a comparison/localisation principle for Christoffel functions of the Máté–Nevai–Totik type.
  Check the literature before calling it new; the label PROVED stands.

## 6. Theorem B (hand recomputation)
- **σ_TC.** P_k(0)²/h_k = (2k+1)!/(4^k k!²), and Σ_{k<m} = (2m+1)!!/(3(2m−2)!!). Spot checks: 1 at m=1, 5/2 at m=2.
  This is ~ 4m^{3/2}/(3√π).
- **xσ_TC.** Π_{i<k}u_i = (2k+3)/(3·2^k k!) and h_k = 1/(2k+2)!. Then P_k(0)²/h_k = (2k+2)(2k+3)²(2k+1)!/(9·4^k k!²),
  ~ 16k^{7/2}/(9√π), so the sum is ~ 32m^{9/2}/(81√π).
- **Mass and weights.** h₀ = Σv_j = 1 (Borel law), and k^{−3/2} = √(2π)e^{j(k)}v_k follows from Stirling with Binet's j.
  This gives 3π√2/4 and 81π/(16√2), and both equal the Conjecture-CG value at c(1) = ½. OK.

## 7. Rule C
KMVV (6.23), DLMF 10.25.2, WLXZ (1.3)–(1.9) and DLMF 5.5.1/5.11.1 are quoted in research/G1/RH/CITATIONS.md.
**F1:** DLMF 4.13.1, 4.13.2 and 4.13.5 (Lambert W), used for h₀ = 1, appear only paraphrased in CG.md §4, not in a
CITATIONS.md entry. Add the verbatim quotes. Optional: replace the Lambert-W argument by the elementary Borel-law
identity, or by an Abel-limit remark. The Paper II results are internal; their labels are inherited.

## 8. Independent numerics (`review/checks/rev_lambda.py`, `rev_fit.py`; outputs `rev_p06_s19.out`, `rev_p25_s5.out`, `rev_fit.out`)
- **Method.** This is a different method from cglib: λ_m = 1/(H_m^{−1})₀₀ with the Hankel matrix [ζ(s+(i+j)p)],
  solved in Arb ball arithmetic (python-flint).
  - (0.6, 1.9): m ≤ 160, 6000/12000 bits.
  - (2.5, 5): m ≤ 120, 10000/20000 bits.
- **Precision.** Ball radii are ≤ 1e−2546 relative. The prec-vs-2prec difference is ≤ 1e−749 at the largest m, and
  ≤ 1e−1385 for (2.5, 5).
- **(2.5, 5).** r_m = λ_m m^E/C. Richardson in 1/m gives limit − 1 = −1.5e−3, −4.4e−5, −1.3e−6, −3.8e−8 at orders 1–4.
- **(0.6, 1.9).** Integer-power Richardson stalls at ~1e−5, as expected from the m^{−1−p} terms. A fit in
  {1/m, m^{−1.6}, m^{−2}, m^{−2.2}, m^{−2.6}} gives limit − 1 = 2.5e−8.
- **Label.** NUMERICAL. Theorem A's constant is confirmed.
- **F7 (observation, NUMERICAL).** In both cases the 1/m coefficient equals −E(s−1)/(2p): −5.75998 against −5.76, and
  −2.92515 against −2.925. So λ_m = C·N^{−E}(1 + o(1/m)) with N = m + (s−1)/(2p). The author's (2,3.5) value −3.044 at
  m = 81 is consistent with the predicted −3.125. Worth recording as a conjecture.

## Other fixable items
- **F4.** S6(a)'s list "min(π/12, π(1−p)/2, π/2)" omits the p<1 lip angle π/2 − 5πp/16. That angle is ≥ 3π/16, so
  the argument is unaffected; correct the text.
- **F5 (Rule N.3).** `check_lambda_n80.out` reports a "precision-doubling diff" of O(1) for p ≥ 1.5. The quoted values
  come from a different run (check_stability). Regenerate the export at dps 800/1600 so the file itself shows stability.

## Label recommendation
- **Theorem A:** PROVED-mod-cite (as stated). Add **REVIEWED** once F1–F5 are applied. None of F1–F5 changes the
  statement.
- **Lemma L:** PROVED; novelty UNCHECKED.
- **Theorem B:** PROVED-mod-cite; REVIEWED after F1.
