# G1: the pointwise Law P — reductions and status

Status: REVIEWED 2026-10-13 (Rule R: `review/REVIEW_G1.md`, ACCEPT WITH FIXES; fixes applied). §3.1 (Plan 27, Theorem CL)
has its own status: Rule R ACCEPT WITH FIXES (`review/REVIEW_Plan27.md`), fixes applied, re-check ACCEPT — REVIEWED. Time-boxed per spec
§7; stop report in §4.

**Labels.** GAP means a precise unproved statement, with no claim about its difficulty. CONDITIONAL means proved
assuming a stated hypothesis that is not a named Lean input.

**Notation.** σ is the spectral measure here, but G2's constraint measure in A3. β_j is n^p b_n here, but G2's β_t
in A3. ω is the oscillation modulus here, but an arcsine law in A3. Each use is local.

**Novelty: UNCHECKED.** G1-T and G1-L are discrete versions of the classical Landau / Hardy–Littlewood Tauberian
lemmas: F = o(x²) together with slow oscillation of F″ gives F″ → 0, and a one-sided bound gives F′. The technique is
known; its application here to Law P is what is new.

## 0. Status

| Result | Statement | Label |
|---|---|---|
| K | second difference of G(n) := Σ_{j<n}(n−j)u_j over ±h = triangle-kernel sum of u, of total mass h² | PROVED |
| **G1-T** | H_all + (T3) slow oscillation of β_n ⇒ β_n → 1, i.e. n^p b_n → c(p)C | PROVED-mod-cite (G2 (P)) |
| **G1-L** | H_all + a one-sided bound (sup β_n < ∞ or inf β_n > 0) ⇒ (1/n)Σ_{j<n} log(j^p b_j) → log(c(p)C) | PROVED-mod-cite (G2 (P)) |
| A1 | J ≥ 0 ⇒ sine-weighted window averages of a_j are ≥ 2cos(π/(L+1))·min b over the window. Hence, if b is regular, liminf of window averages of a_j/(2b_j) ≥ 1 | PROVED |
| A2 | p > 1: Σ_{j>n} a_j = 𝔼_n[Σ_{k∉S} x_k] (Heine ensemble) | PROVED |
| A3 | Q_p := ∫ x d(σ − μ*) = 2c(p)/(p−1) | PROVED (uses only G2 B*(i) and the definition of μ*, both citation-free) |
| A4 | (CL) ⇒ tail-Cesàro a-law; with β_n → 1, block-Cesàro ratios Σa/Σ2b → 1 and window averages → 1 in b-weighted density (pointwise density NOT proved) | CONDITIONAL on (CL). (CL) is proved for pure-power atoms by Theorem CL (§3.1, REVIEWED), so the tail-Cesàro part is unconditional there; (i)–(ii) still need β_n → 1 |
| **CL** | (CL) for pure-power atoms k^{−p}, p > 1, and ROUGH weights (Σw < ∞, w_k ≥ c₁k^{−s}): n^{p−1}𝔼_n[Σ_{k∉S}x_k] → Q_p. Hence n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p−1) unconditionally (§3.1, Plan 27) | PROVED-mod-cite (P) (through G2 B*(iii); internal inputs: G2 A1, A-U, A-L; G3′ §5.2 Lemma Sat); REVIEWED; novelty UNCHECKED |
| G1-R | (T3) from the atoms alone; (CL) (proved for pure-power atoms with rough weights, p > 1: Theorem CL; open for general nodes or p ≤ 1) | GAP for (T3) (see §4) |
| FV | first variation: d/dt log b_n²(v e^{tf}) = ⟨f, μ_n − μ_{n−1}⟩, μ_n := w p_n² (§3.2) | PROVED (standard; novelty not claimed); REVIEWED |
| Conj R | (T3) — hence the pointwise b-law — FAILS for some weights e^{−ε}k^{−2} ≤ w_k ≤ e^{ε}k^{−2} (p = s = 2; §3.2, Plan 28) | CONJECTURE; NUMERICAL (p = s = 2; committed checks: two scales, n ≤ 400, Rule N; reviewer runs in REVIEW_Plan28: three scales, n ≤ 1000, 400-digit mpmath); REVIEWED as a conjecture |
| **T3-conv** | pointwise b-law (hence (T3)) for x_k = k^{−p} (p > 0), w_k = k^{−s}ψ_k (s > 1) with **ψ_k → L ∈ (0, ∞)** (rough at finite scales, decaying roughness): n^p b_n → c(p) (§3.3, Plan 29) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV (REVIEWED), Lemma Sat_p⁺); REVIEWED; novelty UNCHECKED (comparison theorems of Máté–Nevai–Totik type may be classical) |
| TL | polynomial tail localization: for sandwiched weights c k^{−s} ≤ w_k ≤ C k^{−s} (s > 1), 𝔼_{n+1}#(S ∩ (T, ∞)) ≤ ε, hence μ_n((T, ∞)) ≤ ε, for T ≥ A·n^{κ}ε^{−1/(s−1)}, κ = (2 + 2/p)s/(s−1) (§3.4) | PROVED; Rule R pending |
| **T3-sv** | pointwise b-law for w = k^{−s}Ψ with Ψ bounded and *polynomially slowly varying*: sup_{n/M≤k≤n^γ}\|log Ψ(k) − log Ψ(n)\| → 0 for all M, γ (e.g. Ψ = 2 + sin√(log log k)) (§3.4, Plan 30) | PROVED-mod-cite (as T3-conv); Rule R pending; novelty UNCHECKED |
| **RH₁** | pointwise Law P with O(1/n) rate for σ = Σ k^{−3/2}δ_{1/k} (p = 1, r = 3/2), via TC(α = 1) and WLXZ (`RH/RH_p1.md`) | PROVED-mod-cite (WLXZ v1) + REVIEWED |
| **RH_p** | the same for σ_{p,s} = Σ k^{−s}δ_{k^{−p}}, **every p > 1, s > 1**: n^p b_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n), via a one-sided x-variable RH analysis (exact Binet-cut scalar, KMVV left-endpoint Bessel at the hard edge, no truncation); validated end to end vs the true OPs (`RH/px/RH_px.md`) | PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6) + REVIEWED |
| **RH₁(r)** | the same for σ_r = Σ k^{−r}δ_{1/k}, **every r > 1** (p = 1): Nβ_N = 1 + O(1/N), with a Bessel FH parametrix at 0, a = r − 3/2 (`RH/RH_p1_general.md`) | PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4, DLMF 5.11) + REVIEWED |
| **RH_ζ** | smooth-ζ model (x_j = 1/(γ_j²+¼), N₀(γ_j) = j−½, masses 2x_j): **b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log² n))**, κ = −2(log(π/2) − (1 − log 2)); b_N = (β_N/4)(1+O(1/N)), a_N/(2b_N) = 1+O(1/N). Finite-N edge equation (E1–E3), α = 5/8 shift, log-weight hard edge by a Conway–Deift comparison, Arb-certified far field (`RH/zeta/RH_zeta.md`, `RH/zeta/RH_zeta_close.md`) | PROVED-mod-cite (WLXZ v1, KMVV §6, C–D Thm 4.4, DLMF, G2) + REVIEWED |
| **RH_p, ½<p<1** | σ_{p,s}, ½ < p < 1, all s > 1: n^p b_n = c(p)(1+O(1/n)), a_n/(2b_n) = 1+O(1/n). Continued D = t^{t−½}e^{−t}e^{iπt}Γ(1−t)/(i√2π), thin lenses, glued hard-edge W̃ (`RH/plt1/RH_plt1.md`) | PROVED-mod-cite (+ DLMF 5.5.3, 5.11) mod NUMERICAL no-winding (F4) + REVIEWED |
| **RH_p, 0<p<1 (seam)** | the same for all 0 < p < 1 via the seam construction (no Binet-cut B; `RH/plt1/RH_plt1b.md`) | PROVED-mod-cite (WLXZ, KMVV §6 incl. angle freedom, G2 μ*/B*, DLMF 5.11) + REVIEWED; no numerical caveat |

Setting:
- J > 0 is the Jacobi matrix of σ = Σ w_k δ_{x_k}, with x_k = f(k) regularly spaced with index −p and constant C
  (item 11 (H-a)).
- The weights satisfy Σw < ∞ and w_k ≥ c₁k^{−s}. These are the hypotheses of G2's Theorem H_all, so H_all applies.
- Put β_j := j^p b_j/(c(p)C), u_j := log β_j and G(n) := Σ_{j=1}^{n−1}(n−j)u_j.
- H_all is equivalent to G(n) = o(n²) (G2 PROOF.md §3: its b_j form, with the Stirling-type identity).

## 1. The kernel identity

**Lemma K.** For integers n > h ≥ 1, G(n+h) − 2G(n) + G(n−h) = Σ_j (h − |j − n|)⁺ u_j, and Σ_{m∈ℤ}(h − |m|)⁺ = h².

*Proof.* G(n) = Σ_j (n − j)⁺u_j. For fixed j, the second difference in n of (n − j)⁺ with step h is the triangle
(h − |n − j|)⁺. This is checked by cases on the sign of n − j ± h. ∎

## 2. Tauberian reductions

**Theorem G1-T.** Assume H_all's hypotheses and

  (T3) ω(δ) := limsup_{n→∞} sup_{n≤m≤(1+δ)n} |β_m/β_n − 1| → 0 as δ ↓ 0.

Here (T3) means only the slow-oscillation part of item 11's (T3), which also includes two-sided bounds. Then
β_n → 1, i.e. n^p b_n → c(p)C. No bound on β_n, no a_n hypothesis and no monotonicity are assumed: boundedness of u
comes out of the identity itself.

*Proof.*
1. **(T3) gives a two-sided additive modulus.** For m ∈ [(1−δ)n, n] we have n ≤ (1 + δ/(1−δ))m. So for all
   |m − n| ≤ δn, |u_m − u_n| ≤ ω̃(δ) + o(1), where ω̃(δ) := −log(1 − ω(δ/(1−δ))) → 0. This needs
   ω(δ/(1−δ)) < 1, i.e. δ small, and uses that ω is nondecreasing.
2. **Window average.** Fix δ ∈ (0, ½) and put h := ⌊δn⌋. By Lemma K,

     u_n = h⁻²[G(n+h) − 2G(n) + G(n−h)] − h⁻² Σ_j (h − |j−n|)⁺(u_j − u_n).

   The first term is o(n²)/(δn)² → 0, because G(m) = o(m²) and n ± h ≍ n. The second is at most ω̃(δ) + o(1) in
   absolute value, by step 1 and because the kernel has mass h².
3. **Conclusion.** limsup |u_n| ≤ ω̃(δ) for every δ. Let δ → 0. ∎

*Compared with item 11's Theorem C′.* C′ needed:
- (T2) a_n ~ 2b_n;
- the two-sided bounds of (T3);
- Wiener's Tauberian theorem;
- (T4), a δn-scale monotonicity: b_m < b_n eventually for m ≥ (1+δ)n.

G1-T needs only slow oscillation, because H_all (G2) already supplies the averaged statement for every p. (T4) then
becomes a consequence, holding automatically once β_n → 1. (The step-to-step non-monotonicity seen for parity weights
in `check_regularity.out` is not a failure of (T4), which is a δn-scale condition.) The b_n half of G1 is now equivalent to (T3), given H_all.
Conversely, β_n → 1 implies (T3) trivially.

**Theorem G1-L (single Cesàro mean).** Assume H_all's hypotheses and sup_n β_n < ∞ (or inf_n β_n > 0). Then
(1/n)Σ_{j<n} u_j → 0, i.e. the geometric mean of j^p b_j/(c(p)C) over j < n tends to 1.

*Proof (Landau).* Assume u_j ≤ M; the case u_j ≥ −M is symmetric. Put A(n) := Σ_{j<n}u_j, so that
G(n+1) − G(n) = A(n+1).
- Since u ≤ M, A(n+i) ≤ A(n) + Mi. Also Σ_{i=1}^{h} A(n+i) = G(n+h) − G(n). So
  G(n+h) − G(n) ≤ hA(n) + Mh(h+1)/2, i.e. A(n) ≥ [G(n+h) − G(n)]/h − M(h+1)/2.
- Similarly A(n−i) ≥ A(n) − Mi, and G(n) − G(n−h) = Σ_{i=0}^{h−1} A(n−i) ≥ hA(n) − Mh(h−1)/2. So
  A(n) ≤ [G(n) − G(n−h)]/h + M(h−1)/2.
- Take h = ⌊δn⌋. Then G = o(n²) gives |A(n)|/n ≤ o(1)/δ + Mδ/2 + o(1). Let δ → 0. ∎

## 3. The a_n side

**Proposition A1 (positivity, windowed).** Let J ≥ 0. Let n ≥ 1 and L ≥ 2, and put s_j := sin(π(j − n + 1)/(L + 1))
for n ≤ j < n + L. Then

  Σ_{j=n}^{n+L−1} a_j s_j² ≥ 2cos(π/(L+1))·(min_{n≤j<n+L−1} b_j)·Σ_j s_j².

In particular, assume b is regular on windows: max_{n≤j<n+L_n}|b_j/b_n − 1| → 0 for some L_n → ∞. This holds when
β_n → 1 (G1-T) and L_n = o(n). Then liminf_n Σ_j (a_j/(2b_j)) s_j²/Σ_j s_j² ≥ 1. This uses a_j ≥ 0 (from J ≥ 0) to
pass to Σ_j(a_j/2b_j)s_j² ≥ Σ_j a_j s_j²/(2 max b), and min b/max b → 1 over the window.

*Proof.* Take v_j := (−1)^j s_j on the window and 0 elsewhere. Then
0 ≤ ⟨v, Jv⟩ = Σ a_j s_j² − 2Σ_j b_j s_j s_{j+1}. The sine vector satisfies s_{j−1} + s_{j+1} = 2cos(π/(L+1))s_j, with
zero boundary values (item 11 (S4); Lean `toeplitz_eigen`). So Σ_j s_j s_{j+1} = cos(π/(L+1))Σ s_j², and s ≥ 0
gives Σ b_j s_j s_{j+1} ≥ (min b)·cos(π/(L+1))Σ s_j². ∎

A1 is the windowed, limit-free form of item 11's Lemma P: a_n ≥ 2b_n on average. The matching upper bound
(limsup ≤ 1) is the remaining a_n gap; see §4.

**Proposition A2 (tail identity, p > 1).** Let p > 1, so that Σ_k x_k < ∞, J ≥ 0 is trace class, and
Σ_j a_j = Tr J = Σ_k x_k. Let ℙ_n be the Heine probability on n-subsets S ⊂ ℕ, with ℙ_n(S) ∝ Π_{k∈S} w_k·V(S) and
V(S) := Π_{i<j}(x_{k_i} − x_{k_j})². Then, in item 11's indexing (a_1 is the first diagonal entry),

  Σ_{j>n} a_j = 𝔼_n[Σ_{k∉S} x_k].

*Proof.* Σ_{j≤n} a_j = Tr J_n is the sum of the zeros of P_n.
- *Heine's formula*, P_n(z) = 𝔼_n[Π_{k∈S}(z − x_k)]. P_n(z) is the bordered Hankel determinant
  det[m_{i+j} | z^i]/D_n. Expanding it by multilinearity over atoms, as in item 11's H1 (Andreief), and symmetrising
  gives D_n⁻¹ Σ_{ordered n-tuples} Π w·Δ(x)²·Π(z − x_k). Tuples with a repeated atom vanish, which leaves n-subsets.
  (The reviewer checked this by brute force: 9 atoms, dps 40, n ≤ 4.) The
coefficient of z^{n−1} is linear in the atoms, so the sum of the zeros is 𝔼_n[Σ_{k∈S} x_k]. Subtract this from
Tr J = Σ_k x_k. ∎ (The tail Σ_{j≥n} a_j used below is the same identity with 𝔼_{n−1}; the shift is immaterial for
asymptotics.)

**Proposition A3 (the equilibrium value).** Let p > 1 and C = 1. With μ*, σ and c = c(p) as in G2 §1,

  Q_p := ∫ x d(σ − μ*)(x) = ∫_0^∞ u^{−p}(1 − ρ*(u)) du = 2c(p)/(p − 1).

This is the value the tail sums must take if a_j ~ 2c(p)j^{−p}, since n^{p−1}Σ_{j≥n} 2c j^{−p} → 2c/(p−1).

*Proof.* σ − μ* vanishes on [4c, ∞) (G2 B*(i)), so F(R) := ∫_0^R x d(σ − μ*) is constant for R ≥ 4c. Compute the two
parts for R ≥ 4c.
- ∫_0^R xσ(dx) = R^{1−1/p}/(p−1).
- Write μ* = ∫_0^1 ω_{β_t}dt and put t_R := (4c/R)^{1/p}.
  - For t ≥ t_R (β_t ≤ R), ∫ x dω_{β_t} = β_t/2 = 2c t^{−p}. These t contribute 2c(t_R^{1−p} − 1)/(p−1).
  - For t < t_R, the substitution t = t_R s gives β_t = R s^{−p}, and these t contribute R t_R M_p with
    M_p := ∫_0^1∫_0^1 y dω_{[0,s^{−p}]}(y) ds < ∞.
  - Both t-ranges give terms proportional to R^{1−1/p}, plus the constant −2c/(p−1).
- So F(R) = κ′R^{1−1/p} + 2c/(p−1) for some constant κ′. Since F is constant in R, κ′ = 0 and F ≡ 2c/(p−1). ∎

Numerically (`checks/check_tailsum.out`), Q_p − 2c/(p−1) = 0 to 8 digits for p ∈ {1.5, 2, 3, 4}. The actual tail sums
n^{p−1}Σ_{j≥n} a_j converge to Q_p: for p = 2, 1.2430 → 1.2360 → 1.2343 at n = 100, 400, 1600, against 1.2337.

**Theorem A4 (conditional a_n law, p > 1).** Assume H_all's hypotheses with exact pure-power atoms x_k = k^{−p} (C = 1),
and the concentration lemma

  (CL) n^{p−1}𝔼_n[Σ_{k∉S} x_k] → Q_p.

Then n^{p−1}Σ_{j≥n} a_j → 2c(p)/(p−1), which is the tail-Cesàro form of a_n ~ 2c(p)n^{−p}. If in addition β_n → 1
(e.g. under (T3), by G1-T), then:
- (i) Σ_{j≥n}(a_j − 2b_j) = o(n^{1−p}), and for every δ > 0 the block ratio
  Σ_{n≤j<(1+δ)n} a_j / Σ_{n≤j<(1+δ)n} 2b_j → 1;
- (ii) the sine-weighted window averages of a_j/(2b_j), over windows of length L_n → ∞ with L_n = o(n), tend to 1 in
  b-weighted density.

*A pointwise density statement does NOT follow.* The reviewer's counterexample is b_j = j^{−2},
a_j = 2b_j(1 + 0.3(−1)^j). It satisfies A1 (the alternating part is invisible to sine windows) and the tail equality,
yet |a_j/(2b_j) − 1| = 0.3 for every j. Full J ≥ 0 excludes this example, so a variational argument might do better,
but none is given.

*Proof.* Combine A2, A3 and (CL). Then subtract Σ_{j≥n} 2b_j = (2c/(p−1))n^{1−p}(1 + o(1)), which holds when β_n → 1.
- (i) The block ratio follows by differencing the tail asymptotics at n and (1+δ)n.
- (ii) The tail equality bounds the total positive excess of the window averages, and A1 bounds them below. ∎

*Status of (CL) (Plan 9 text; superseded by Theorem CL, §3.1, Plan 27: (CL) is proved for pure-power atoms
k^{−p}, p > 1, with rough weights).* (CL) is the statement that the Heine ensemble's complement measure (1/n)Σ_{k∉S}δ_{k/n} converges to
(1 − ρ*(u))du, tested against u^{−p}. The integrand is singular at u = 0, inside the saturated region.
- On u ≥ θ the test function is bounded. There, (CL) would follow from concentration of the empirical measure at speed
  n² (an LDP upper bound). That bound is plausibly provable from G2 Part A and the energy-distance form of B*(iii), but
  it is not written here.
- On u < θ < u_s (saturated), (CL) needs E[(1/n)Σ_{k≤θn, k∉S}(k/n)^{−p}] → 0: a *saturation-exactness* statement. The
  n²-speed bound cannot see single-atom exclusions, which cost only O(n) in log V. Heuristically each exclusion costs
  e^{−2n(U*(x_k) − ℓ)} (swap a saturated atom for a free one), and U* − ℓ > 0 on the saturated region. A proof needs
  mesoscopic control of the empirical potential.
- **(CL) is the precise missing lemma for the a_n side (p > 1).** For p ≤ 1, J is not trace class and A2 does not apply
  as stated.

### 3.1 Theorem CL (Plan 27): saturation exactness and concentration — (CL) holds for rough weights — Lemma Sat_p PROVED; Lemma WC, Theorem CL, A4′ PROVED-mod-cite (P) (through G2 B*(iii)); Rule R ACCEPT WITH FIXES, re-check ACCEPT — REVIEWED; novelty UNCHECKED

Setting: x_k = k^{−p} with p > 1, weights w_k > 0 with W := Σw_k < ∞ and w_k ≥ c₁k^{−s}. P_n is the Heine measure
on n-subsets S (item 11 H1), with ρ_n(k) := P_n(k ∈ S) = w_kK_n(x_k, x_k). Put
- m_n := (1/n)Σ_kρ_n(k)δ_{k/n} = 𝔼_n[ν_S], where ν_S := (1/n)Σ_{k∈S}δ_{k/n};
- λ_n := (1/n)Σ_{k≥1}δ_{k/n}.
Then 0 ≤ m_n ≤ λ_n. Notation 𝒜, I, μ*_u, ρ*, u_s := (4c(p))^{−1/p} and κ_p is G2's (§1).

**Lemma Sat_p (saturation, any p ≥ 1).** For 1 ≤ k < n, with θ := k/n,

  1 − ρ_n(k) ≤ (W/w_k)·e^{−2n·g_p(θ)},  g_p(θ) := (p − θ)log(1/θ) + (1 − θ)log(1 − θ) − p + (p − 1)θ.

g_p is decreasing on (0, ½) and g_p(θ) → ∞ as θ → 0. (For p = 2 this is G3′ §5.2's g.)

*Proof.* G3′ §5.2 Lemma Sat (Christoffel + Lagrange) gives 1 − ρ_n(k) ≤ (W_{>n}/w_k)·Π_{j≤n,j≠k}(x_j/|x_j − x_k|)².
Here x_j/|x_j − x_k| = k^p/|k^p − j^p|.
- For p ≥ 1, j^p − k^p ≥ j^{p−1}(j − k) (j > k) and k^p − j^p ≥ k^{p−1}(k − j) (j < k).
- So the j < k part of the product is ≤ k^{k−1}/(k−1)! ≤ e^k, and the j > k part is
  ≤ k^{p(n−k)}/((n−k)!·(n!/k!)^{p−1}).
- Use log m! ≥ m log m − m and Σ_{k<j≤n}log j ≥ ∫_k^n log t dt. The log n terms cancel (coefficient
  (p−θ) − (1−θ) − (p−1) = 0), leaving log Π ≤ −n·g_p(θ).
- Since W_{>n} ≤ W, the stated bound follows (F7).
- Monotonicity: g_p′(θ) = log(θ/(1−θ)) − p/θ + p − 1 < 0 on (0, ½). Only θ ≤ ½ is used. ∎

**Lemma WC (concentration at speed n²).** For every φ ∈ C_c((0, ∞)) and δ > 0,
P_n(|⟨φ, ν_S⟩ − ⟨φ, μ*_u⟩| > δ) ≤ e^{−c(φ,δ)n² + o(n²)}. In particular, ⟨φ, m_n⟩ → ⟨φ, μ*_u⟩.

*Proof (rewritten after Rule R F1; the gap constant no longer depends on any cutoff).*
1. **Uniform energy gap.** Let B := {μ ∈ 𝒜 : |⟨φ, μ⟩ − ⟨φ, μ*_u⟩| ≥ δ/4}. **Claim:** sup_B I < κ_p.
   - Suppose μ_k ∈ B with I(μ_k) → κ_p. Pass to the x-variable, μ_k^x := g_*μ_k ≤ σ.
   - These are probability measures on [0, ∞), tight at ∞, since μ_k^x([X, ∞)) ≤ σ([X, ∞)) = X^{−1/p}. Mass may
     accumulate at x = 0, which corresponds to u = ∞.
   - Take a weak limit ν on [0, ∞) along a subsequence.
   - **Upper semicontinuity.** Write k(x, y) := log|x − y| = min(k, L) + (k − L)⁺.
     - min(k, L) is u.s.c. and bounded above, so ∬min(k, L)dμ_kdμ_k has limsup ≤ ∬min(k, L)dνdν ≤ I(ν). This is the
       Portmanteau theorem for μ_k ⊗ μ_k → ν ⊗ ν.
     - (k − L)⁺ ≤ (log(1+x) + log(1+y) − L)⁺, and ∫_X^∞log(1+x)σ(dx) → 0. So ∬(k − L)⁺dμ_kdμ_k ≤ ε(L) → 0 uniformly
       in k.
     - Hence I(ν) ≥ limsup I(μ_k) = κ_p > −∞.
   - So ν has no atom at 0, since an atom would give I(ν) = −∞. Also ν ≤ σ on (0, ∞), as the inequality is
     preserved on open sets.
   - Hence ν = g_*μ with μ ∈ 𝒜, and I(μ) ≥ κ_p, so μ = μ*_u by G2 B*(iii).
   - But φ∘g^{−1} ∈ C_c((0, ∞)), so ⟨φ, μ_k⟩ → ⟨φ, μ*_u⟩, contradicting μ_k ∈ B.
   - Put c′ := min(1, (κ_p − sup_B I)/2) > 0 (B may be empty, or have sup −∞). The u.s.c. integrals above are against
     the x-measures μ_k^x. (This replaces the earlier 𝒜^R u.s.c. step and its corner issue, F2.)
2. **Constants, in order.** Let R_φ ≥ 1 with supp φ ⊂ (0, R_φ].
   - Choose t₀ ∈ (0, 1 − 1/√2] (so τ² ≥ ½) with At₀ ≤ c′/2 and (1 − τ)‖φ‖_∞ + ω_φ(2R_φ(1 − τ)) ≤ δ/4 for all τ ∈ [1 − t₀, 1].
     Here A = 4p + 2|κ_p| is G2 A-U's constant.
   - Then choose M ≥ max(2, R_φ) with p·t₀·log M ≥ 2A.
3. **Splitting** (G2 Theorem A-U with this M). Write S = H ∪ T with T := S ∩ (Mn, ∞), m := |T|, N := n − m and
   t := m/n.
   - For t ≥ t₀, A-U's bound log T_m ≤ −pn²log n + κ_pn² + n²(At − pt²log M) + O_M(n log n) applies, with bracket
     ≤ t(A − pt₀log M) ≤ −At₀.
   - For t < t₀, ⟨φ, ν_S⟩ = ⟨φ, ν_H⟩ (T lies beyond Mn ≥ R_φn). Also |⟨φ, ν_H⟩ − ⟨φ, μ̄_H⟩| ≤ ω_φ(1/n), with μ̄_H ∈ 𝒜_τ
     the smeared measure of G2 Lemma A1, τ = N/n.
4. **Bad heads.** Write μ̄_H = (μ′)_τ with μ′ ∈ 𝒜 (G2 scaling).
   - ⟨φ, μ̄_H⟩ = τ⟨φ(τ·), μ′⟩, and |φ(τu) − φ(u)| ≤ ω_φ(2R_φ(1 − τ)) wherever either side is nonzero (u ≤ R_φ/τ). So
     |⟨φ, μ′⟩ − ⟨φ, μ̄_H⟩| ≤ δ/4. So on the bad event μ′ ∈ B, for n ≥ n₀(φ, δ) (so that ω_φ(1/n) ≤ δ/4).
   - Hence I(μ̄_H) = τ²(I(μ′) − p log τ) ≤ τ²(κ_p − p log τ) − 2τ²c′ ≤ τ²(κ_p − p log τ) − c′ (τ² ≥ ½, since
     t₀ ≤ 1 − 1/√2).
   - Inserting this into G2 Lemma A1 and the A-U chain lowers the head bound by c′n². So
     Σ_{bad, t<t₀}T_m ≤ exp(−pn²log n + κ_pn² + (At₀ − c′)n² + o(n²)) ≤ exp(… − (c′/2)n²).
5. **Compare with A-L,** D_n ≥ exp(−pn²log n + κ_pn² − o(n²)). Then P_n(bad) ≤ e^{−min(c′/2, At₀)n² + o(n²)}.
   Since φ is bounded, 𝔼|⟨φ, ν_S⟩ − ⟨φ, μ*_u⟩| → 0. ∎

**Theorem CL.** In the setting above, n^{p−1}𝔼_n[Σ_{k∉S}x_k] → Q_p = 2c(p)/(p − 1) (A3).

*Proof (split rewritten, F3).* n^{p−1}Σ_k k^{−p}(1 − ρ_n(k)) = ∫u^{−p}d(λ_n − m_n). Fix θ ≤ min(u_s, ½) with
g_p(θ) ≥ 1, R ≥ 1, and χ ∈ C_c((0, ∞)) with 0 ≤ χ ≤ 1, χ = 1 on [θ, R] and supp χ ⊂ [θ/2, R + 1]. Split
u^{−p} = u^{−p}χ + u^{−p}(1 − χ).
- (a) **Middle.** By vague convergence (Lemma WC, and λ_n → du), ∫u^{−p}χ d(λ_n − m_n) → ∫u^{−p}χ(1 − ρ*)du.
- (b) **Near 0.** u^{−p}(1 − χ) on (0, θ) is supported where k < θn. There Lemma Sat_p gives
  n^{p−1}Σ_{k<θn}k^{−p}(1 − ρ_n(k)) ≤ (W/c₁)n^{p−1}Σ_{k<θn}k^{s−p}e^{−2n} ≤ Cn^{p+s}e^{−2n} → 0. In the limit,
  ρ* = 1 on (0, u_s) ⊃ (0, θ) (G2 B*(i)), so that part is 0.
- (c) **Tail.** On (R, ∞), 0 ≤ ∫u^{−p}(1−χ)d(λ_n − m_n) ≤ ∫_{(R,∞)}u^{−p}dλ_n ≤ R^{1−p}/(p−1) + o(1), since
  0 ≤ m_n ≤ λ_n. The limit side has the same bound.
- Let n → ∞, then R → ∞. ∎

**Corollary A4′ (unconditional tail-Cesàro a-law).** For x_k = k^{−p} (p > 1), weights with Σw < ∞ and
w_k ≥ c₁k^{−s} (no regularity), n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p − 1). This is A4's first conclusion, now without (CL).
A4 (i)–(ii) still need β_n → 1, i.e. (T3) via G1-T.

**Remarks.**
- **CL1 (why this was out of reach in Plan 9).** Saturation is needed only near u = 0 (F5). The §4 stop report noted that single-atom exclusions cost only O(n) in
  log V, below n² resolution. Lemma Sat_p controls them directly through the Christoffel function, with a Lagrange test
  polynomial. It is not an n² energy argument, so this is the missing mesoscopic input.
- **CL2.** Rough weights enter only through Σw < ∞, w_k ≥ c₁k^{−s} and log(W/w_k) = O(log k), so parity or random
  weights are fine.
  - NUMERICAL (`checks/check_cl_rough.out`, long double RKPW as in `check_tailsum`, p = 2, n ≤ 3200): n·Σ_{j≥n}a_j
    tends to 2c/(p−1) = 1.233701. For example 1.233924 (smooth), 1.233941 (parity weights k^{−2}(1 + ½(−1)^k)) and
    1.233929 (random U[½, 3/2] factors) at n = 3200.
  - Meanwhile the pointwise ratio a_n/(2b_n) for parity weights oscillates (correctly indexed, F6: see the .out). This
    is consistent with A4 claiming only the tail-Cesàro form.
- **CL3.** Novelty UNCHECKED. The weak-convergence step (Lemma WC) is the standard large-deviation pattern for
  Coulomb gases, made explicit for G2's constrained functional. Unverified pointers for a literature search (from the
  reviewer): Johansson; Féral; Dragnev–Saff; Kuijlaars–Rakhmanov.
- **CL4 (scope, F5).** (CL) is proved here for exact pure-power atoms k^{−p} with p > 1 only. It is not proved for
  general regularly spaced nodes f(k), and for p ≤ 1 (CL)/A2 do not apply as stated.

### 3.2 (T3) for rough weights: first variation and counter-evidence (Plan 28) — FV PROVED (standard); Conjecture R NUMERICAL; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan28.md), fixes applied, re-check ACCEPT — REVIEWED

**Lemma FV (first variation; standard, novelty not claimed).** Let w(t) := v·e^{tf}, where v is a weight sequence
with finite moments and f is bounded, on fixed atoms x_k. Let p_j = p_j^{(t)} be the orthonormal polynomials of w(t),
and put μ_n(k) := w_k(t)p_n(x_k)² (a probability vector). Then, with b_n² = h_n/h_{n−1}:

  (d/dt) log b_n²(t) = ⟨f, μ_n − μ_{n−1}⟩,  and  (d/dt) log(b_n²/b_{n−1}²) = ⟨f, μ_n − 2μ_{n−1} + μ_{n−2}⟩.

*Proof.*
- **Heine.** D_m = Σ_{|S|=m}Π_{k∈S}w_k·V(S). Differentiating term by term is justified by dominated convergence,
  since |f| is bounded and D_m(t) is a convergent sum of terms Π w_k(t)V(S) with |∂_t| ≤ m‖f‖_∞·(term). This gives
  (d/dt) log D_m = Σ_k f_kρ_m(k), with ρ_m(k) = P_m(k ∈ S) = w_kΣ_{j<m}p_j(x_k)² (G3′ §5.2 Lemma H).
- h_n = D_{n+1}/D_n gives log b_n² = log D_{n+1} − 2 log D_n + log D_{n−1}. Hence
  (d/dt) log b_n² = Σ_k f_k(ρ_{n+1} − 2ρ_n + ρ_{n−1})(k) = ⟨f, μ_n − μ_{n−1}⟩.
- Differencing in n gives the second formula.
- Sanity check (Toda): f = x gives (d/dt) log b_n² = a_n − a_{n−1}. ∎

**Numerics** (NUMERICAL; `checks/check_t3_rough.out`; full-reorthogonalized Lanczos in float64, with Lanczos vector
Q[j] = √w·p_j and b[n]² = h_n/h_{n−1}; truncated pure power x_k = k^{−2}, w = k^{−2}, K = 20n; p = s = 2 only).
- **[1] Adversarial jumps.** Take f = ε·sign(μ_n − 2μ_{n−1} + μ_{n−2}), with weights in [e^{−ε}, e^{ε}]·k^{−2}.
  - It moves |β_n/β_{n−1} − 1| from about 10⁻⁵ to 0.031–0.034 at ε = 0.05, and to 0.128–0.141 at ε = 0.2, for
    n = 100, 200 and 400. The effect does not shrink with n.
  - Lemma FV is confirmed to first order. Δlog b_n² matches ⟨f, μ_n − μ_{n−1}⟩ to within 2% at ε = 0.05 and 11% at
    ε = 0.2. Δlog(b_n²/b_{n−1}²) matches ⟨f, Δ²μ⟩ to within 3% (F1 of the review: the earlier text paired the wrong
    quantities).
  - The supremum over |f| ≤ ε of the first-order ratio change is ε‖Δ²μ‖₁ ≈ 1.2–1.35ε.
- **[1b] Rule N.** K = 20n vs 40n gives the same jump (0.128 at n = 200, ε = 0.2), with the pattern recomputed on each
  measure. The pattern must be computed on the measure it perturbs (F8): transplanted onto a much longer truncation it
  is weaker.
- **[2] Locality.** |μ_n − μ_{n−1}| lives at index scale n: quantiles 0.65n (5%), 0.92n (50%), 2.86n (95%), 6.17n
  (99%). About 6.5% of the mass lies beyond 6n, with a polynomially decaying tail.
- **[3] One sequence, repeated spikes.** One weight sequence has adversarial windows [0.6N, 1.6N] at N = 60 and 240
  (ε = 0.2).
  - Each window produces an isolated spike: |β_N/β_{N−1} − 1| = 0.127 and 0.123, with 0.077 and 0.069 at N + 1.
  - The maximum over every other n ∈ [10, 390] is 0.030. Smooth weights give a maximum of 5·10⁻³.
  - The reviewer's independent runs confirm the pattern:
    - three windows (N = 60, 240, 960) give 0.112, 0.110 and 0.104;
    - the 960 window moves jumps at n ≤ 400 by ≤ 3·10⁻⁴;
    - the jumps persist at n = 800;
    - a 400-digit mpmath Stieltjes check at n = 60 reproduces them.
- **[4] Generic rough weights** (long double RKPW, K vs 2K). For parity and random weights, mean |β_{m+1}/β_m − 1| over
  [n, 1.1n] decays like n^{−1/2}:
  - parity: 3.5·10⁻² → 8.7·10⁻³;
  - random: 1.3·10⁻² → 3.2·10⁻³;

  over n = 250 → 3600. (At n = 3600 the K and 2K values differ by 5–8%, so that column is at the edge of truncation.)

**What the evidence is, and what it is not (F2).** Non-decaying TV(μ_n, μ_{n−1}) is *not* by itself evidence against
(T3). The Chebyshev weight on [−1, 1] has TV(μ_n, μ_{n−1}) → 4/π² ≈ 0.405, yet b_n converges under every bounded
perturbation there (Rakhmanov-type theorems; recollection, not cited). The evidence against (T3) here is:
- the locality of |μ_n − μ_{n−1}| at index scale n ([2]);
- the cross-scale independence of adversarial windows ([3]).

Together these allow a single bounded sequence to keep spiking at sparse scales.

**Conjecture R** (stated for p = s = 2, which is all the numerics test). For every ε > 0 there is f with |f| ≤ ε,
supported on windows [0.6N_i, 1.6N_i] along a sufficiently sparse sequence N_i, such that w = k^{−2}e^{f} satisfies
limsup_n |β_n/β_{n−1} − 1| ≥ cε, with c > 0 absolute.
- Then β_n does not converge, so (T3) and the pointwise law n²b_n → c(2) fail.
- H_all (the averaged law) and Theorem CL (the tail-Cesàro a-law) still hold, since the weights are sandwiched.

**What a proof needs** (F10; ordered by importance).
- **(iii) Cross-scale independence.** Windows at larger scales perturb β_N only slightly. Numerically ×4 separation
  suffices; super-exponential separation plus a Christoffel tail bound is a plausible rigorous route.
- **(i) A lower bound ‖Δ²μ_N‖₁ ≥ c** restricted to the window, for the base measures that arise in the construction
  (not all of the sandwich class). This is pointwise asymptotics of p_N at the atoms.
- **(ii) Second-order control** of t ↦ log(b_N²/b_{N−1}²) along the perturbation path.
- None of these is done here.

**Re-scoping G1-R (F6).**
- §4 posed (T3) from atom regularity under the one-sided weight conditions Σw < ∞, w_k ≥ c₁k^{−s}. If Conjecture R
  holds, it is false a fortiori: Conjecture R refutes β_n → 1 directly.
- The positive target becomes (T3) for *regular* weights.

**Localization reduction (F5).** Let w = vΨ with base v = k^{−s} (s > 1) and Ψ bounded above and below with
log Ψ slowly varying.
- The path vΨ^t stays in a fixed sandwich class. By Lemma FV,
  log b_n²(vΨ) − log b_n²(v) = ∫_0^1⟨g_n, μ_n^{(t)} − μ_{n−1}^{(t)}⟩dt, with g_n := log Ψ − log Ψ(n).
- On [n/M, Mn], |g_n| → 0 by slow variation.
- On the head, μ_n = ρ_{n+1} − ρ_n ≤ 1 − ρ_n is exponentially small by Lemma Sat_p (§3.1).
- So if a **localization lemma** holds, meaning μ_n^{(t)}((Mn, ∞)) + μ_{n−1}^{(t)}((Mn, ∞)) ≤ ε(M) uniformly along the path, then
  b_n(vΨ)/b_n(v) → 1. The pure-power laws (RH_p etc.) then give the pointwise law. That is more than (T3).
- The upper tail is a GAP. Unbounded slowly varying Ψ (e.g. log k) would need additional quantitative tail control.
- The case Ψ_k → L, where the tail is not needed, is Theorem T3-conv (§3.3, Plan 29).

### 3.3 Theorem T3-conv (Plan 29): decaying roughness does not break the pointwise law — PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan29.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED

**Lemma Sat_p⁺ (all p > 0).** For 1 ≤ k < n and θ := k/n:
  1 − ρ_n(k) ≤ (W/w_k)·((n+1)/k)^{2(1−p)₊}·e^{−2n·g_p⁺(θ)},
where g_p⁺ := g_p for p ≥ 1 and g_p⁺ := g_p − log(1/p) for 0 < p < 1. In all cases g_p⁺(θ) → +∞ as θ → 0 (since
g_p(θ) ≥ p·log(1/θ) − O(1)).

*Proof.* As for Lemma Sat_p (§3.1), with two changes for p < 1 (F1).
1. Concavity gives j^p − k^p ≥ p·j^{p−1}(j − k) for j > k, and k^p − j^p ≥ p·k^{p−1}(k − j) for j < k. Each of the
   n − 1 factors therefore gains at most 1/p, so the product bound is multiplied by at most p^{−(n−1)}.
2. The j > k product becomes k^{p(n−k)}(n!/k!)^{1−p}/(p^{n−k}(n−k)!). The factor (n!/k!)^{1−p} is now in the
   numerator, so it needs an *upper* bound. For the increasing function log:
   Σ_{j=k+1}^n log j ≤ ∫_{k+1}^{n+1}log t dt ≤ ∫_k^n log t dt + log((n+1)/k).
   - The integral term reproduces the p ≥ 1 computation.
   - The excess contributes at most ((n+1)/k)^{1−p} to the product, i.e. ((n+1)/k)^{2(1−p)} after squaring.
∎

**Theorem T3-conv.** Let x_k = k^{−p} (p > 0) and w_k = k^{−s}ψ_k with s > 1, where ψ_k > 0 and ψ_k → L ∈ (0, ∞).
Then, with v_k := k^{−s},

  log b_n²(w) − log b_n²(v) → 0,  hence n^p b_n(w) → c(p),

by the pointwise law for the pure power v:
- RH_p for p > 1 (`RH/RH_px.md`);
- RH₁(r) for p = 1 (r = s);
- the RH_p seam construction for 0 < p < 1 (`RH/plt1/RH_plt1b.md`).

In particular β_n → 1, so (T3) holds.

*Proof.*
1. **Path.** w(t) := v·ψ^t for t ∈ [0, 1]. Since ψ is bounded above and below (it converges to L > 0 and is positive),
   every w(t) lies in a fixed sandwich c·k^{−s} ≤ w_k(t) ≤ C·k^{−s}, with W(t) ≤ C·ζ(s).
   - b_n²(t) is smooth in t: each Heine term Π_{k∈S}w_k(t)V(S) has t-derivatives bounded by (m‖log ψ‖_∞)^j times
     itself, so the series for D_m(t) and its derivatives converge uniformly (F4).
   - Lemma FV gives log b_n²(1) − log b_n²(0) = ∫_0^1⟨f, μ_n^{(t)} − μ_{n−1}^{(t)}⟩dt, with f := log ψ.
2. **Centering.** Σ_kμ_n^{(t)}(k) = Σ_kμ_{n−1}^{(t)}(k) = 1, so f may be replaced by g := log ψ − log L. Then
   |g| ≤ G everywhere, and for every ε > 0 there is k_ε with |g_k| ≤ ε for k ≥ k_ε.
3. **Head.** μ_m^{(t)}(k) = ρ_{m+1}^{(t)}(k) − ρ_m^{(t)}(k) ≤ 1 − ρ_m^{(t)}(k). Take k < k_ε and m large, so that
   k < m and k/m ≤ θ₁, where g_p⁺ ≥ 1 on (0, θ₁]. Then Lemma Sat_p⁺ gives
   μ_m^{(t)}(k) ≤ (Cζ(s)/c)k^s(m+1)²·e^{−2m}, uniformly in t (F4: factor ζ(s), using W(t) ≤ Cζ(s)).
4. **Estimate.** |⟨g, μ_n^{(t)} − μ_{n−1}^{(t)}⟩| ≤ ε·Σ_{k≥k_ε}(μ_n + μ_{n−1})(k) + G·Σ_{k<k_ε}(μ_n + μ_{n−1})(k)
   ≤ 2ε + 2G(Cζ(s)/c)k_ε^{s+1}(n+1)²e^{−2(n−1)}. Integrate over t, let n → ∞, then ε → 0. ∎

**Remarks.**
- **T3c1 (the dichotomy).**
  - *Decaying* roughness (ψ_k → L, arbitrarily rough at finite scales, e.g. ψ_k = 1 + ½(−1)^k/log(k+1)) preserves
    the pointwise b-law: Theorem T3-conv.
  - *Non-decaying* roughness of size ε *conjecturally* can break it (F3): Conjecture R (§3.2, numerical evidence
    only, p = s = 2).
  - The proof uses no localization of μ_n at large k. Only the saturated head matters, because g → 0 at ∞.
- **T3c2 (slowly varying Ψ; F2).** For ψ = Ψ slowly varying without a limit (e.g. Ψ(k) = 2 + sin(log log k)), the
  same argument needs the upper-tail localization μ_n((Mn, ∞)) + μ_{n−1}((Mn, ∞)) ≤ ε(M), uniformly along the path
  (the §3.2 localization reduction). Numerically 99% of the mass lies within 6.2n (§3.2 [2]). A pointwise-in-n proof
  is OPEN. (Polynomial-scale localization is proved in §3.4, Lemma TL, giving T3-sv.)
  - *Averaged version (SKETCH):* Σ_{m=N}^{2N}μ_m(A) ≤ 𝔼#_{2N+1}(S ∩ A) with A = (MN, ∞).
  - A tail-count bound for the Heine ensemble would then give (1/N)Σ_{n=N}^{2N}|log b_n²(w) − log b_n²(v)| → 0. The
    bound needed: the number of points of S beyond Mn is O(n/log M), *uniformly along the path*. G2 A-U gives this
    for p > 1, and G3′ §7 Lemma K for p = 2; nothing is stated for p ≤ 1. (G1's own "Lemma K" is the kernel
    identity, not this.)
- **T3c3 (a_n).** The a_n half would need the first variation of a_n = ⟨xp_n, p_n⟩, a covariance-type expression.
  Not done.
- **NUMERICAL** (`checks/check_t3_conv.out`, p = 2, long double RKPW):
  - |β_n(ψ)/β_n(1) − 1| for ψ = 1 + ½(−1)^k/log(k+1) goes 3.9·10⁻³ → 8.2·10⁻⁴ (n = 250 → 3600).
  - For random ±½/√log and block-sign ±½/log variants it is ≤ 2.3·10⁻³, not monotone in n (F6). Only p = 2 is
    tested in the repo.
  - Control: non-decaying parity gives 2.8·10⁻² → 4.6·10⁻³ (it also decays; parity is not adversarial, cf. §3.2).

### 3.4 Lemma TL and Theorem T3-sv (Plan 30): polynomial tail localization, and (T3) for polynomially slowly varying weights — PROVED / PROVED-mod-cite; Rule R pending

Setting: x_k = k^{−p} (p > 0), weights c·k^{−s} ≤ w_k ≤ C·k^{−s} with s > 1 and 0 < c ≤ C. Notation ρ_m, μ_n as in
§3.2–3.3.

**Lemma TL (polynomial tail localization).** Put T′ := ⌈8p·n²⌉ and T″ := ⌈T′n^{2/p}⌉. For every k ≥ T″,

  ρ_{n+1}(k) ≤ 1156·(C/c)·(T″/k)^s.

Hence, for T ≥ T″,

  μ_n((T, ∞)) ≤ 𝔼_{n+1}#(S ∩ (T, ∞)) ≤ 1156·(C/c)·T″^sT^{1−s}/(s − 1).

This is ≤ ε as soon as T ≥ A·n^κ·ε^{−1/(s−1)}, with κ := (2 + 2/p)s/(s − 1) and A = A(p, s, C/c). The bound is
uniform over the sandwich class, and the same holds for μ_{n−1}.

*Proof.* Put a := x_{T″} and b := x_{T′}, so a/b ≤ n^{−2} ≤ ½ (n ≥ 2).
1. **Norming set.** Let deg P ≤ n.
   - Consecutive atoms in [a, b] are at distance x_j − x_{j+1} ≤ p·j^{−p−1} ≤ p·b/T′, by the mean value theorem
     (any p > 0).
   - Markov's inequality on [a, b], with b − a ≥ b/2, gives |P′| ≤ (4n²/b)‖P‖_{[a,b]}.
   - So every point of [a, b] is within p·b/T′ of an atom, and ‖P‖_{[a,b]} ≤ max_{atoms}|P| + (4pn²/T′)‖P‖_{[a,b]}.
     Since T′ ≥ 8pn², this gives ‖P‖_{[a,b]} ≤ 2·max_{T′≤j≤T″}|P(x_j)|.
2. **Extrapolation to [0, a].** For x ∈ [0, a], |P(x)| ≤ T_n((a + b − 2x)/(b − a))·‖P‖_{[a,b]} ≤ T_n(1 + 4a/b)‖P‖.
   With cosh θ = 1 + η, θ ≤ √(2η), we get T_n(1 + η) = cosh(nθ) ≤ e^{n√(2η)} ≤ e^{√8} ≤ 17 (η = 4a/b ≤ 4n^{−2}).
3. **Christoffel.** For k ≥ T″ (x_k ≤ a) and P with P(x_k) = 1, steps 1–2 give 1 ≤ 34·max_{T′≤j≤T″}|P(x_j)|.
   - So ∫P²dμ ≥ min_{j≤T″}w_j/34² ≥ c·T″^{−s}/1156.
   - Hence 1/K_{n+1}(x_k, x_k) ≥ cT″^{−s}/1156, and ρ_{n+1}(k) = w_kK_{n+1}(x_k, x_k) ≤ 1156(C/c)(T″/k)^s.
4. **Sum.** Σ_{k>T}k^{−s} ≤ T^{1−s}/(s − 1). Also μ_n = ρ_{n+1} − ρ_n ≤ ρ_{n+1} pointwise. ∎

**Theorem T3-sv.** Let w = vΨ with v = k^{−s} (s > 1), and Ψ bounded with 0 < c ≤ Ψ ≤ C. Assume Ψ is
*polynomially slowly varying*: for all M, γ ≥ 1,

  δ_n(M, γ) := sup_{n/M ≤ k ≤ n^γ}|log Ψ(k) − log Ψ(n)| → 0  (n → ∞).

Then log b_n²(w) − log b_n²(v) → 0, so n^p b_n(w) → c(p) (the pure-power laws, as in T3-conv), and (T3) holds.

*Proof.* Take the path w(t) = vΨ^t (sandwiched by min(1, c) and max(1, C)) and g_n := log Ψ − log Ψ(n), with
|g_n| ≤ G := log(C/c) + |log Ψ(n)|-type constant ≤ 2 max|log Ψ|. By Lemma FV and centering,

  |log b_n²(w) − log b_n²(v)| ≤ sup_t Σ_k|g_n(k)|(μ_n^{(t)} + μ_{n−1}^{(t)})(k)
    ≤ 2δ_n(M, γ) + G·[(μ_n^{(t)} + μ_{n−1}^{(t)})(k < n/M) + (μ_n^{(t)} + μ_{n−1}^{(t)})(k > n^γ)].

- **Head.** μ_m ≤ 1 − ρ_m and Lemma Sat_p⁺ give e^{−2n·g_p⁺(1/M)}·n^{O(1)} → 0 once g_p⁺(1/M) ≥ 1.
- **Tail.** Fix ε > 0 and take γ := κ + 1. Then n^γ ≥ A n^κ ε^{−1/(s−1)} for large n, so Lemma TL gives ≤ 2ε.
- Let n → ∞, then ε → 0. ∎

**Remarks.**
- **TL1 (examples).**
  - Ψ(k) = 2 + sin√(log log k) and Ψ(k) = 2 + sin(log log log k) are polynomially slowly varying: log log(k^γ) =
    log log k + log γ.
  - Ψ(k) = 2 + sin(log log k) is slowly varying but *not* polynomially so. It still needs localization at scale
    Mn (OPEN).
  - Combining with T3-conv: products Ψ·χ with χ_k → L are also covered (same proof, with g = log Ψ + log χ −
    log Ψ(n) − log L).
- **TL2 (what is open).** Localization at scale Mn, μ_n((Mn, ∞)) ≤ ε(M), is what full slow variation needs.
  - Lemma TL loses a polynomial factor. It comes from Markov's inequality (atoms must be n²-dense relative to the
    interval) and the n^{−2} relative extrapolation distance.
  - NUMERICAL (`checks/check_tail_loc.out`, small n): μ_n has 5–9% of its mass beyond 10n, and 0.002–0.14% beyond
    T″. The bound of Lemma TL holds with ratio ≤ 8·10⁻¹⁰, so it is very loose.

## 4. G1-R: what remains (stop report)

**Where G1 stands after Plan 9 (updated by Plan 27).**
- *b_n side.* Pointwise b_n ⟺ (T3) slow oscillation of β_n, given H_all (G1-T). Unconditionally, the single
  geometric Cesàro mean converges under a one-sided bound (G1-L).
- *a_n side.* The lower half holds unconditionally in window average (A1). For p > 1, the upper half holds in
  tail-Cesàro form. This is unconditional for pure-power atoms with rough weights by Theorem CL (Plan 27). Block-Cesàro
  ratios and window-average density still need β_n → 1 (A4). Pointwise density is not proved.
- G1-L needs a one-sided bound on β_n; it is not unconditional.

**Missing statements (precise).** (See §3.2: for *rough* weights, (T3) is conjecturally FALSE, Conjecture R.)
- (T3) for β_n := n^p b_n/(c(p)C), from atom regularity (H-a) and weight conditions.
- ~~(CL) for p > 1~~: now PROVED for pure-power atoms with rough weights (Theorem CL, §3.1, Plan 27).

**Why the tools here stop short** (methodological explanations, heuristic; not theorems about all such methods).
1. *Energy / large-deviation methods* (G2 Part A, H7, Lemma K) control log D_n to o(n²). Second differences over
   windows of width h therefore control only *window averages* of log b_j, with error o(n²)/h². That is exactly
   G1-T's input. (T3) is a statement about the variation of b_j *inside* windows. Through
   2 log b_n = Δ² log D_n, it needs log D_n to o(1) precision in second differences, far beyond any n²-speed method.
   (CL) likewise needed single-atom exclusion probabilities, which cost O(n) in log V, below n² resolution. Plan 27
   supplies them through Christoffel–Lagrange bounds (Lemma Sat_p), which are not n²-speed arguments.
2. *Riemann–Hilbert steepest descent* gives pointwise asymptotics of discrete orthogonal polynomials, including
   saturated regions, for finite node sets with analytic data (BKMM). Infinite nodes with an accumulation point are
   handled only for the explicit Tricomi–Carlitz family (WLXZ; nodes ±(k+α)^{−1/2}, i.e. p = 1 in the squared
   variable), within the literature read. The literature read has no RH analysis for general
   nodes x_k = f(k) accumulating at 0 with merely polynomially sandwiched (non-analytic) weights. Weight regularity
   genuinely matters: item 11's Prop D (exponentially small weights break the law) and test A3 (parity weights give
   power-rate coefficient oscillations; also `checks/check_regularity.out`).
3. *Tauberian methods* (item 11's C′, and G1-T) need an a priori regularity input. Neither the atoms nor the
   averaged law supplies it.

**Stop condition (Plan 9; updated).** (CL) is now proved (pure-power atoms, rough weights; Theorem CL). The remaining
statement (T3) is not reached by the methods developed here. The
only route found in the literature read (RH for discrete OPs) is established only for finite node sets (BKMM) and for
one explicit accumulating family (WLXZ). Adapting it to general accumulating nodes with analytic weights is a
plausible but substantial project, far outside this time box. For non-analytic sandwiched weights, no method is known
to us. This is recorded as **GAP**: "as hard as an open problem" is *not* claimed, because no source states the
general problem as open. The precise missing statement is (T3) above (and (CL) for general nodes or p ≤ 1).

**Most promising next step (not attempted).** An RH analysis à la BKMM/WLXZ for x_k = k^{−p} with weights k^{−s}.
Analytic node density and analytic weights put it in the regime where the steepest-descent machinery should apply.
The saturated region (u < u_s) and the explicit equilibrium μ* of G2 give the needed g-function. A result for this
model family would prove the pointwise law for pure powers with power weights, the case of Haynes–Zudilin and
item 11's references.
