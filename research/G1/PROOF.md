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
| Sat_p | saturation, p ≥ 1: 1 − ρ_n(k) ≤ (W/w_k)e^{−2n·g_p(k/n)} (§3.1) | PROVED (§3.1 header); REVIEWED |
| WC | concentration at speed n²: P_n(\|⟨φ, ν_S⟩ − ⟨φ, μ*_u⟩\| > δ) ≤ e^{−c(φ,δ)n² + o(n²)} (§3.1) | PROVED-mod-cite (P) (through G2 B*(iii)) (§3.1 header); REVIEWED |
| A4′ | unconditional tail-Cesàro a-law: x_k = k^{−p} (p > 1), Σw < ∞, w_k ≥ c₁k^{−s}: n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p − 1) (§3.1) | PROVED-mod-cite (P) (through G2 B*(iii)) (§3.1 header); REVIEWED |
| Sat_p⁺ | Sat_p for all p > 0, with the extra factor ((n+1)/k)^{2(1−p)₊} and g_p⁺ (§3.3); internal input of T3-conv, T3-sv, T3a, Thm R, L, T3-all, T3-log | no separate label in the §3.3 header (which labels T3-conv); the proof is that of Lemma Sat_p (PROVED) with two elementary changes; Rule R (review/REVIEW_Plan29.md) ACCEPT WITH FIXES, F1 applied — REVIEWED |
| G1-R | (T3) from the atoms alone; (CL) (proved for pure-power atoms with rough weights, p > 1: Theorem CL; open for general nodes or p ≤ 1) | (T3) half **REFUTED** for sandwiched weights (Theorem R, §3.6); PROVED-mod-cite for pure-power nodes with slowly varying Ψ: bounded Ψ (Theorem T3-all, §3.8; contains T3-conv, T3-sv/T3a, T3-avg) and log-type Ψ (Theorem T3-log, §3.9); open for slowly varying Ψ with D(γ) = ∞ and for nodes other than pure powers. (CL) half: proved for pure powers k^{−p}, p > 1 (Theorem CL); open for general nodes or p ≤ 1 (see §4). *(Row updated by Plan 37, 2026-10-14; previously "proved for polynomially slowly varying weights (T3-sv/T3a); (CL) half unchanged".)* |
| FV | first variation: d/dt log b_n²(v e^{tf}) = ⟨f, μ_n − μ_{n−1}⟩, μ_n := w p_n² (§3.2) | PROVED (standard; novelty not claimed); REVIEWED |
| Conj R | (T3) — hence the pointwise b-law — FAILS for some weights e^{−ε}k^{−2} ≤ w_k ≤ e^{ε}k^{−2} (p = s = 2; §3.2, Plan 28) | Proved in modified form as Theorem R (§3.6): ε ≤ ε₀, non-explicit η, windows [θN, N^{κ+1}]. The [0.6N, 1.6N]-window form remains NUMERICAL. *(Plan 39, 2026-10-14: window form, incl. [0.6N, 1.6N], proved for ε ≤ ε₀ explicit with N_{i+1}/N_i → ∞ — Theorem RW, §3.10, Rule R pending; every-ε/absolute-c and ×4 forms still NUMERICAL.)* |
| **Thm R** | Conjecture R proved in modified form (all p > 0, s > 1): there is ε₀ = η/16 such that for every ε ≤ ε₀ there is f with \|f\| ≤ ε such that w = k^{−s}e^{f} has limsup \|log(β_n²/β_{n−1}²)\| ≥ εη/2; so (T3) and the pointwise b-law fail for some weights in [e^{−ε}, e^{ε}]·k^{−s} (§3.6, Plan 33) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺, TL, §3.5 two-point formula); proves Conjecture R in modified form; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan33.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED. Sub-labels: R2 PROVED; R1 PROVED-mod-cite |
| **T3-conv** | pointwise b-law (hence (T3)) for x_k = k^{−p} (p > 0), w_k = k^{−s}ψ_k (s > 1) with **ψ_k → L ∈ (0, ∞)** (rough at finite scales, decaying roughness): n^p b_n → c(p) (§3.3, Plan 29) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV (REVIEWED), Lemma Sat_p⁺); REVIEWED; novelty UNCHECKED (comparison theorems of Máté–Nevai–Totik type may be classical) |
| TL | polynomial tail localization: for sandwiched weights c k^{−s} ≤ w_k ≤ C k^{−s} (s > 1), 𝔼_{n+1}#(S ∩ (T, ∞)) ≤ ε, hence μ_n((T, ∞)) ≤ ε, for T ≥ A·n^{κ}ε^{−1/(s−1)}, κ = (2 + 2/p)s/(s−1) (§3.4) | PROVED (textbook-standard Markov/Chebyshev inequalities, quoted); REVIEWED; novelty UNCHECKED (pointers: Ehlich–Zeller 1964, Coppersmith–Rivlin 1992, Rakhmanov 2007, Nevai, Máté–Nevai–Totik) |
| **T3-sv** | pointwise b-law for w = k^{−s}Ψ with Ψ bounded and *polynomially slowly varying*: sup_{n/M≤k≤n^γ}\|log Ψ(k) − log Ψ(n)\| → 0 for all M, γ (e.g. Ψ = 2 + sin√(log log k)) (§3.4, Plan 30) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV, Lemma Sat_p⁺, Lemma TL); REVIEWED; novelty UNCHECKED |
| FVa | first variation of a_n: d/dt a_n(v e^{tf}) = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩ (q_j = √w p_j) (§3.5) | PROVED (standard; novelty not claimed; self-contained via the proof of Lemma H and Christoffel–Darboux); Rule R ACCEPT WITH FIXES, re-check ACCEPT — REVIEWED |
| **T3a** | pointwise **a-law** n^p a_n → 2c(p) under T3-sv's hypotheses (Ψ bounded, polynomially slowly varying; includes ψ_k → L), all p > 0, s > 1 (§3.5, Plan 32) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FVa, Sat_p⁺, TL); REVIEWED; novelty UNCHECKED |
| TC | tail count: 𝔼_m#(S ∩ (Mm, ∞)) ≤ (2A/(p log M))·m + o(1) uniformly over sandwiched weights, every p > 0 (§3.7) | PROVED-mod-cite (P) (through G2 B*(iii); internal: G2 A1/A2, A-U, A-L) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **T3-avg** | for w = k^{−s}Ψ with Ψ bounded and **uniformly slowly varying** (δ_N(M, M′) → 0; e.g. 2 + sin(log log k)): (1/N)Σ_{n=N}^{2N}\|log b_n²(w) − log b_n²(v)\| → 0 and (1/N)Σ n^p\|a_n(w) − a_n(v)\| → 0; hence the full pointwise Law P along a set of n of density one (§3.7, Plan 34) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; (P) via TC) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **TV** | (d/dt)μ_m(A) = ⟨f1_Aq_m,q_m⟩ − 2⟨1_Aq_m, K_m(fq_m)⟩ − ⟨fq_m,q_m⟩μ_m(A) along w(t) = we^{tf} (§3.8, Plan 35) | PROVED (standard; novelty not claimed) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED |
| **LP** | pure power: μ_n((Mn, ∞)) → F_p(M) = (2/π)arcsin√(min(1, M^{−p}/(4c(p)))), M ≥ 1 (§3.8; min added by Plan 37 to match §3.8) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; textbook method of moments) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED; novelty not claimed |
| **Thm L** | localization at scale Mn: limsup sup_t μ_m^{(t)}((Mn, ∞)) ≤ e^{4G}F_p(M) for bounded slowly varying Ψ (§3.8) | PROVED-mod-cite (as LP; internal TV, Sat_p⁺) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **T3-all** | for w = k^{−s}Ψ with Ψ bounded and **slowly varying** (δ_n(λ) → 0): n^pb_n → c(p) and n^pa_n → 2c(p) for **all n** — the full pointwise Law P; contains T3-conv, T3-sv, T3-avg (§3.8, Plan 35) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, L) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **T3-log** | for w = k^{−s}Ψ with Ψ **log-type slowly varying** (slowly varying, and D(γ) < ∞; e.g. (log k)^α, any α ∈ ℝ): the full pointwise Law P, all n; contains T3-all (§3.9, Plan 36) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TL(w), L, T3-all) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **RW** | Conjecture R in window form (all p > 0, s > 1): for every window [aN, bN] with b > u_s(p) (e.g. [0.6N, 1.6N], admissible for every p), explicit η_W > 0 and ε₀ = η_W/16 such that for ε ≤ ε₀, f := ε·Σ_i sign(Δ²μ^v_{m_i})·1_{[aN_i, bN_i]} with N_{i+1}/N_i → ∞ (or > R_W fixed) gives limsup |log(β_n²/β_{n−1}²)| ≥ εη_W/2 (resp. /4); Lemma R1W: ‖Δ²μ^v_m\|_{[aN,bN]}‖₁ ≥ η_W for some m ∈ [N − J_W + 1, N] (§3.10, Plan 39) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, R2, LP, Sat_p⁺, G2 B*(i)); Rule R pending; novelty UNCHECKED. Not proved: every ε with absolute c; ×4 separation (NUMERICAL) |
| **RH₁** | pointwise Law P with O(1/n) rate for σ = Σ k^{−3/2}δ_{1/k} (p = 1, r = 3/2), via TC(α = 1) and WLXZ (`RH/RH_p1.md`) | PROVED-mod-cite (WLXZ v1 §§2–6) + REVIEWED |
| **RH_p** | the same for σ_{p,s} = Σ k^{−s}δ_{k^{−p}}, **every p > 1, s > 1**: n^p b_n = c(p)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n), via a one-sided x-variable RH analysis (exact Binet-cut scalar, KMVV left-endpoint Bessel at the hard edge, no truncation); validated end to end vs the true OPs (`RH/px/RH_px.md`) | PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6; G2 PROOF.md μ*, B* — only μ* and B*(i)–(ii), which do not use (P)) + REVIEWED |
| **RH₁(r)** | the same for σ_r = Σ k^{−r}δ_{1/k}, **every r > 1** (p = 1): Nβ_N = 1 + O(1/N), with a Bessel FH parametrix at 0, a = r − 3/2 (`RH/RH_p1_general.md`) | PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4, DLMF 5.11) + REVIEWED |
| **RH_ζ** | smooth-ζ model (x_j = 1/(γ_j²+¼), N₀(γ_j) = j−½, masses 2x_j): **b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log² n))**, κ = −2(log(π/2) − (1 − log 2)); b_N = (β_N/4)(1+O(1/N)), a_N/(2b_N) = 1+O(1/N). Finite-N edge equation (E1–E3), α = 5/8 shift, log-weight hard edge by a Conway–Deift comparison, Arb-certified far field (`RH/zeta/RH_zeta.md`, `RH/zeta/RH_zeta_close.md`) | PROVED-mod-cite (WLXZ v1 §§3–6.1; KMVV §6; C–D Thm 4.4; DLMF; G2 — optimality, for E1(iv) only, which RH_zeta.md §1 says is not needed for the RH analysis) + REVIEWED |
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
(limsup ≤ 1) is the remaining a_n gap; see §4. *(Plan 37 note, 2026-10-14: this was the Plan 9 status. For pure-power
nodes with slowly varying Ψ the full a-law n^pa_n → 2c(p) is now proved (T3a, T3-all, T3-log; §§3.5, 3.8, 3.9). For rough
weights only the tail-Cesàro form A4′ (§3.1) is known; a pointwise a_n statement is not proved (§4, "a_n side").)*

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

### 3.2 (T3) for rough weights: first variation and counter-evidence (Plan 28) — FV PROVED (standard); Conjecture R NUMERICAL (proved in modified form, §3.6); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan28.md), fixes applied, re-check ACCEPT — REVIEWED

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

**Conjecture R** (stated for p = s = 2, which is all the numerics test). **Proved for all p > 0, s > 1, in a modified form, as Theorem R (§3.6):** ε ≤ ε₀, non-explicit η, and windows [θN, N^{κ+1}] in place of [0.6N, 1.6N]. The [0.6N, 1.6N] form would need localization at scale Mn and remains NUMERICAL (F2). *(Plan 39, 2026-10-14: the window form, including [0.6N, 1.6N] for every p > 0, s > 1, is now proved for ε ≤ ε₀ (explicit) with separation N_{i+1}/N_i → ∞ or a fixed explicit ratio — Theorem RW, §3.10, PROVED-mod-cite, Rule R pending. The bound for every ε > 0 with absolute c, and ×4 separation, remain NUMERICAL.)* For every ε > 0 there is f with |f| ≤ ε,
supported on windows [0.6N_i, 1.6N_i] along a sufficiently sparse sequence N_i, such that w = k^{−2}e^{f} satisfies
limsup_n |β_n/β_{n−1} − 1| ≥ cε, with c > 0 absolute.
- Then β_n does not converge, so (T3) and the pointwise law n²b_n → c(2) fail.
- H_all (the averaged law) still holds, since the weights are sandwiched, and so does Theorem CL (the tail-Cesàro a-law) when p > 1 (F1).

**What a proof needs** (F10; ordered by importance).
- **(iii) Cross-scale independence.** Windows at larger scales perturb β_N only slightly. Numerically ×4 separation
  suffices; super-exponential separation plus a Christoffel tail bound is a plausible rigorous route.
- **(i) A lower bound ‖Δ²μ_N‖₁ ≥ c** restricted to the window, for the base measures that arise in the construction
  (not all of the sandwich class). This is pointwise asymptotics of p_N at the atoms.
- **(ii) Second-order control** of t ↦ log(b_N²/b_{N−1}²) along the perturbation path.
- None of these was done in Plan 28. All three are done in §3.6 (Theorem R): (iii) by Sat_p⁺ and Lemma TL, (i) by
  Lemma R1, (ii) by Lemma R2.

**Re-scoping G1-R (F6).**
- §4 posed (T3) from atom regularity under the one-sided weight conditions Σw < ∞, w_k ≥ c₁k^{−s}. Theorem R (§3.6)
  refutes this (T3) half directly (β_n does not converge); the (CL) half is unaffected (F3).
- The positive target becomes (T3) for *regular* weights.

**Localization reduction (F5).** Let w = vΨ with base v = k^{−s} (s > 1) and Ψ bounded above and below with
log Ψ slowly varying.
- The path vΨ^t stays in a fixed sandwich class. By Lemma FV,
  log b_n²(vΨ) − log b_n²(v) = ∫_0^1⟨g_n, μ_n^{(t)} − μ_{n−1}^{(t)}⟩dt, with g_n := log Ψ − log Ψ(n).
- On [n/M, Mn], |g_n| → 0 by slow variation.
- On the head, μ_n = ρ_{n+1} − ρ_n ≤ 1 − ρ_n is exponentially small by Lemma Sat_p (§3.1).
- So if a **localization lemma** holds, meaning μ_n^{(t)}((Mn, ∞)) + μ_{n−1}^{(t)}((Mn, ∞)) ≤ ε(M) uniformly along the path, then
  b_n(vΨ)/b_n(v) → 1. The pure-power laws (RH_p etc.) then give the pointwise law. That is more than (T3).
- The upper tail at scale Mn was a GAP; it is now PROVED (Theorem L, §3.8, Plan 35), giving the all-n law T3-all. (On average over n it is handled by Lemma TC, giving the density-one Theorem T3-avg, §3.7). (§3.4, Lemma TL, proves it at polynomial scale n^κ, giving Theorem T3-sv;
  F12.) Unbounded log-type Ψ (e.g. (log k)^α) is handled by truncation (Theorem T3-log, §3.9).
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
- RH_p for p > 1 (`RH/px/RH_px.md`);
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
  - *Non-decaying* roughness of size ε ≤ ε₀ can break it: Theorem R (§3.6; earlier Conjecture R, §3.2, numerical evidence
    only, p = s = 2).
  - The proof uses no localization of μ_n at large k. Only the saturated head matters, because g → 0 at ∞.
- **T3c2 (slowly varying Ψ; F2).** For ψ = Ψ slowly varying without a limit (e.g. Ψ(k) = 2 + sin(log log k)), the
  same argument needs the upper-tail localization μ_n((Mn, ∞)) + μ_{n−1}((Mn, ∞)) ≤ ε(M), uniformly along the path
  (the §3.2 localization reduction). Numerically 99% of the mass lies within 6.2n (§3.2 [2]). A pointwise-in-n proof
  was OPEN; it is now PROVED (Theorem T3-all, §3.8; density-one version T3-avg, §3.7). (Polynomial-scale localization is proved in §3.4, Lemma TL, giving T3-sv.)
  - *Averaged version:* SUPERSEDED by §3.7 (Lemma TC, Theorem T3-avg; all p > 0). Original sketch, kept for the record: Σ_{m=N}^{2N}μ_m(A) ≤ 𝔼#_{2N+1}(S ∩ A) with A = (MN, ∞).
  - A tail-count bound for the Heine ensemble would then give (1/N)Σ_{n=N}^{2N}|log b_n²(w) − log b_n²(v)| → 0. The
    bound needed: the number of points of S beyond Mn is O(n/log M), *uniformly along the path*. G2 A-U gives this
    (for every p > 0; the earlier "p > 1 only" was wrong), and G3′ §7 Lemma K for p = 2. (G1's own "Lemma K" is the kernel
    identity, not this.)
- **T3c3 (a_n).** Done in §3.5 (Lemma FVa, Theorem T3a; Plan 32).
- **NUMERICAL** (`checks/check_t3_conv.out`, p = 2, long double RKPW):
  - |β_n(ψ)/β_n(1) − 1| for ψ = 1 + ½(−1)^k/log(k+1) goes 3.9·10⁻³ → 8.2·10⁻⁴ (n = 250 → 3600).
  - For random ±½/√log and block-sign ±½/log variants it is ≤ 2.3·10⁻³, not monotone in n (F6). Only p = 2 is
    tested in the repo.
  - Control: non-decaying parity gives 2.8·10⁻² → 4.6·10⁻³ (it also decays; parity is not adversarial, cf. §3.2).

### 3.4 Lemma TL and Theorem T3-sv (Plan 30): polynomial tail localization, and (T3) for polynomially slowly varying weights — PROVED / PROVED-mod-cite; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan30.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED

Setting: x_k = k^{−p} (p > 0), weights c·k^{−s} ≤ w_k ≤ C·k^{−s} with s > 1 and 0 < c ≤ C. Notation ρ_m, μ_n as in
§3.2–3.3.

**Lemma TL (polynomial tail localization).** Let n ≥ 2 (F4). Put T′ := ⌈8p·n²⌉ and T″ := ⌈T′n^{2/p}⌉. For every k ≥ T″,

  ρ_{n+1}(k) ≤ 1156·(C/c)·(T″/k)^s.

Hence, for integer T ≥ T″,

  μ_n((T, ∞)) ≤ 𝔼_{n+1}#(S ∩ (T, ∞)) ≤ 1156·(C/c)·T″^sT^{1−s}/(s − 1).

(For non-integer T, use ⌊T⌋; F5.) This is ≤ ε (with 0 < ε ≤ 1) as soon as the integer T satisfies T ≥ A·n^κ·ε^{−1/(s−1)}, where
κ := (2 + 2/p)s/(s − 1) and A := (8p + 2)^{s/(s−1)}·max{1, 1156(C/c)/(s − 1)}^{1/(s−1)} (F3). In particular T ≥ T″.
The bound is uniform over the sandwich class. It holds also for μ_{n−1}, since μ_{n−1} ≤ ρ_n ≤ ρ_{n+1}.

*Standard inputs (F11; textbook-standard, as for Lemma FV, and not checked against a specific source).*
- **Markov:** for deg P ≤ n on [a, b], ‖P′‖_{[a,b]} ≤ (2n²/(b − a))‖P‖_{[a,b]}.
- **Chebyshev:** for deg P ≤ n and x outside [a, b], |P(x)| ≤ |T_n(y)|·‖P‖_{[a,b]}, with y the affine image of x
  under [a, b] → [−1, 1].

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
   - So ∫P²dμ ≥ min_{T′≤j≤T″}w_j/34² ≥ c·T″^{−s}/1156 (F6).
   - Hence 1/K_{n+1}(x_k, x_k) ≥ cT″^{−s}/1156, and ρ_{n+1}(k) = w_kK_{n+1}(x_k, x_k) ≤ 1156(C/c)(T″/k)^s.
4. **Sum.** Σ_{k>T}k^{−s} ≤ T^{1−s}/(s − 1). Also μ_n = ρ_{n+1} − ρ_n ≤ ρ_{n+1} pointwise. ∎

**Theorem T3-sv.** Let w = vΨ with v = k^{−s} (s > 1), and Ψ bounded with 0 < c ≤ Ψ ≤ C. Assume Ψ is
*polynomially slowly varying*: for all M, γ ≥ 1,

  δ_n(M, γ) := sup_{n/M ≤ k ≤ n^γ}|log Ψ(k) − log Ψ(n)| → 0  (n → ∞).

Then log b_n²(w) − log b_n²(v) → 0, so n^p b_n(w) → c(p) (the pure-power laws, as in T3-conv), and (T3) holds.

*Proof.* Take the path w(t) = vΨ^t. It is sandwiched by min(1, c)·v and max(1, C)·v, so Lemma TL applies along the
path with C′/c′ = max(1, C)/min(1, c) (F7). Put g_n := log Ψ − log Ψ(n), so |g_n| ≤ G := log(C/c) (F1). By Lemma FV
and centering,

  |log b_n²(w) − log b_n²(v)| ≤ sup_t Σ_k|g_n(k)|(μ_n^{(t)} + μ_{n−1}^{(t)})(k)
    ≤ 2δ_n(M, γ) + G·[(μ_n^{(t)} + μ_{n−1}^{(t)})(k < n/M) + (μ_n^{(t)} + μ_{n−1}^{(t)})(k > n^γ)].

- **Head (F2).** Fix M ≥ 4 (so 2/M ≤ ½, where g_p is decreasing, and k < n − 1) with g_p⁺ ≥ 1 on (0, 2/M]. Then for m ∈ {n−1, n} and k < n/M (so k/m ≤ 2/M), μ_m ≤ 1 − ρ_m and
  Lemma Sat_p⁺ give a total head mass ≤ C″n^{s+1}(n+1)²e^{−2(n−1)} → 0.
- **Tail.** Fix ε ∈ (0, 1] and take γ := κ + 1. Then n^γ ≥ A n^κ ε^{−1/(s−1)} for large n, so Lemma TL (for μ_n and μ_{n−1},
  along the path) gives ≤ 2ε. (Any γ > κ works, so the hypothesis is needed only for some γ > κ; F7.)
- Let n → ∞, then ε → 0. ∎

**Remarks.**
- **TL1 (examples).**
  - Ψ(k) = 2 + sin√(log log k) and Ψ(k) = 2 + sin(log log log k) (for k large enough to be defined, with any bounded
    positive values before that; F8) are polynomially slowly varying. On k ∈ [n/M, n^γ], log log k ranges over
    [log log n + log(1 − log M/log n), log log n + log γ], an interval of length O(1). Both functions are uniformly
    continuous in log log k with vanishing local oscillation as log log k → ∞.
  - Ψ(k) = 2 + sin(log log k) is slowly varying but *not* polynomially so (δ_n ≥ log 3 − o(1) infinitely often). The all-n law follows from localization at scale
    Mn, now PROVED (Theorem L, T3-all, §3.8).
  - T3-sv contains T3-conv: take Ψ = ψ, since ψ_k → L > 0 is bounded and polynomially slowly varying. Products
    Ψ·χ with χ_k → L are likewise a direct instance (F9).
- **TL2 (what is open).** Localization at scale Mn, μ_n((Mn, ∞)) ≤ ε(M), would suffice for the all-n law under full slow variation; now PROVED (Theorem L, §3.8; T3-all). (Density-one version: T3-avg, §3.7).
  - Lemma TL loses a polynomial factor. It comes from Markov's inequality (atoms must be n²-dense relative to the
    interval) and the n^{−2} relative extrapolation distance.
  - NUMERICAL (`checks/check_tail_loc.out`, small n, truncation K = 6T″; F10): μ_n has 4.5–9.3% of its mass beyond
    10n, and 0.002–0.14% beyond T″. The bound of Lemma TL holds with ratio ≤ 8·10⁻¹⁰, so it is very loose.
  - Doubling the truncation leaves the ratio unchanged and moves the mass beyond T″ by about 10% (reviewer's run).

### 3.5 Lemma FVa and Theorem T3a (Plan 32): the a_n half — PROVED / PROVED-mod-cite; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan32.md), fixes applied, re-check ACCEPT — REVIEWED

Notation as in §3.2–3.4. Put q_j := √w·p_j on the atoms, so μ_j = q_j², and write K_m(k, l) := Σ_{j<m}q_j(k)q_j(l)
(a projection matrix). Conventions: a_n = ⟨xq_n, q_n⟩ and b_n = ⟨xq_{n−1}, q_n⟩, so that b_n² = h_n/h_{n−1}.

**Lemma FVa (first variation of a_n).** For w(t) = v·e^{tf} with f bounded,

  (d/dt) a_n = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩.

The right side is unchanged when f is replaced by f + const.

*Proof.*
1. **a_n as an expectation difference.** a_n = ⟨x, μ_n⟩ = Σ_k x_k(ρ_{n+1} − ρ_n)(k) = 𝔼_{n+1}⟨x, X⟩ − 𝔼_n⟨x, X⟩, with
   X_k := 1[k ∈ S].
2. **Exponential tilting.** P_{m,t}(S) ∝ Π_{k∈S}w_k(t)V(S), so (d/dt)𝔼_{m,t}F = Cov_{m,t}(F, ⟨f, X⟩) for bounded F
   (dominated convergence, as in Lemma FV).
3. **Two-point function (F1, F2).** The Gram/Sylvester steps in the *proof* of Lemma H (G3′ §5.2), together with the
   Heine identification D_m(μ ∖ E′)/D_m(μ) = P(S ∩ E′ = ∅), give the equality P(k, l ∉ S) = det(I − K_{E′}) for
   E′ = {k, l}. (Lemma H's *statement* records only the inequality and the single-deletion case.) Inclusion–exclusion
   then gives P(k, l ∈ S) = K_m(k,k)K_m(l,l) − K_m(k,l)² for k ≠ l. Since K_m is a projection, Σ_lK_m(k,l)² = K_m(k,k),
   so Cov_m(⟨g,X⟩, ⟨f,X⟩) = ½Σ_{k,l}(g_k − g_l)(f_k − f_l)K_m(k,l)². (The diagonal term is
   Var X_k = K_m(k,k) − K_m(k,k)²; the double sums converge absolutely, since Σ_{k,l}K_m(k,l)² = m and g, f are
   bounded.)
4. **Rank-one update.** K_{n+1} = K_n + q_nq_nᵀ, so K_{n+1}² − K_n² = 2K_n(k,l)q_n(k)q_n(l) + q_n(k)²q_n(l)²
   entrywise. With g = x:
   - The second part contributes ½Σ(x_k − x_l)(f_k − f_l)q_n(k)²q_n(l)² = ⟨(x − a_n)f, μ_n⟩.
   - The first part is Σ_{k,l}(x_k − x_l)K_n(k,l)q_n(k)q_n(l)(f_k − f_l). By Christoffel–Darboux,
     (x_k − x_l)K_n(k,l) = b_n(q_n(k)q_{n−1}(l) − q_{n−1}(k)q_n(l)). This uses the recurrence
     xp_j = b_{j+1}p_{j+1} + a_jp_j + b_jp_{j−1} (F3).
   - **Algebra.** The first part equals b_n·Σ_{k,l}A_{kl}(f_k − f_l), with
     A_{kl} := q_n(k)²q_{n−1}(l)q_n(l) − q_{n−1}(k)q_n(k)q_n(l)².
     - Σ_{k,l}A_{kl}f_k = ⟨f, q_n²⟩⟨q_{n−1}, q_n⟩ − ⟨f, q_{n−1}q_n⟩·1 = −⟨f, q_{n−1}q_n⟩.
     - Σ_{k,l}A_{kl}f_l = 1·⟨f, q_{n−1}q_n⟩ − ⟨q_{n−1}, q_n⟩⟨f, q_n²⟩ = ⟨f, q_{n−1}q_n⟩.
     - So the first part is −2b_n⟨f, q_{n−1}q_n⟩.
   - For n = 0 (K_0 = 0) the first part vanishes, consistent with b_0 := 0.
5. **Invariance.** ⟨x − a_n, μ_n⟩ = 0 and ⟨q_{n−1}, q_n⟩ = 0, so constants drop out.
6. **Toda check.** f = x gives ‖xq_n‖² − a_n² − 2b_n² = b_{n+1}² − b_n², the Toda flow. ∎

NUMERICAL ([1] of `checks/check_alaw.out`):
- Central differences against the formula, for random f, agree to relative error ≤ 8·10⁻⁸ (n = 20, 60, 150; F6).
- For f = x the formula equals b_{n+1}² − b_n² (finite-difference error ≤ 2·10⁻⁴, at values of size 10⁻¹¹).

**Theorem T3a.** Under the hypotheses of Theorem T3-sv (x_k = k^{−p}, p > 0; w = k^{−s}Ψ, s > 1; Ψ bounded and
polynomially slowly varying, including ψ_k → L), n^p a_n(w) → 2c(p). Together with T3-sv, the full pointwise
Law P (b- and a-laws) holds for these weights.

*Proof.* Take the path w(t) = vΨ^t and g_n := log Ψ − log Ψ(n), with |g_n| ≤ G. Fix M ≥ 4 as in T3-sv (head margin),
ε ∈ (0, 1], and γ := κ + 1 (Lemma TL). All bounds below hold for n ≥ n₀(M, ε, p, s, sandwich) (F4). The constants are
generous: about 7 (middle) and 5 (tail) suffice, times (n/(n−1))^p.
1. **Uniform bounds along the path.** a_n^{(t)} = ⟨x, μ_n⟩ ≤ (M/n)^p + (head mass), since x_k ≤ (M/n)^p for
   k ≥ n/M and x_k ≤ 1. The head mass is exponentially small (Sat_p⁺), so a_n^{(t)} ≤ 2M^pn^{−p} for large n,
   uniformly in t. Also b_n = ⟨xq_{n−1}, q_n⟩ ≤ ½⟨x, μ_{n−1} + μ_n⟩ ≤ ½(a_{n−1} + a_n) ≤ 2M^p(n−1)^{−p}.
2. **First variation.** By Lemma FVa (centered),
   |(d/dt)a_n| ≤ Σ_k|g_n(k)|·[|x_k − a_n|μ_n(k) + b_n(μ_{n−1} + μ_n)(k)].
   - **Head** (k < n/M): bounded by (1 + 1)·G·(μ_n + μ_{n−1})(head) = O(n^{O(1)}e^{−2(n−1)}), using |x_k − a_n| ≤ 1
     and b_n ≤ 1.
   - **Middle** (n/M ≤ k ≤ n^γ): |x_k − a_n| ≤ 3M^pn^{−p} and |g_n| ≤ δ_n(M, γ), so the contribution is
     ≤ 14M^pn^{−p}δ_n.
   - **Tail** (k > n^γ): bounded by G·7M^pn^{−p}·(μ_n + μ_{n−1})(tail), which is ≤ 14GM^pεn^{−p} (Lemma TL for both,
     along the path).
3. **Conclude.** Integrate over t: n^p|a_n(w) − a_n(v)| ≤ 14M^pδ_n + 14GM^pε + o(1). Let n → ∞, then ε → 0.
   The pure-power a-law (a_n/(2b_n) = 1 + O(1/n) and n^p b_n → c(p), in RH_px, RH₁(r) and RH_plt1b) gives
   n^p a_n(v) → 2c(p). ∎

**Remarks.**
- **T3a1.** Lemma FVa is self-contained: the two-point formula comes from the proof of Lemma H, not from a cited
  determinantal theory. Novelty of the lemma: none claimed (the first variation of Jacobi parameters under weight tilting is
  classical; cf. the Toda flow).
- **T3a2 (NUMERICAL, [2]; F7).** The script reports (n+1)²a_n/(2c) − 1, the a_n index being 0-based, at
  n = 250, 500, 1000, 2000 and 3600, with K = 120000 and 240000.
  - For n ≤ 1000, the gap |A(ψ) − A(1)| for ψ_k = 1 + ½(−1)^k/log(k+1) (5.3·10⁻³, 8.6·10⁻⁴, 2.1·10⁻³) is 2–12×
    smaller than for non-decaying parity at each n. No rate is claimed.
  - For n ≥ 2000 none of the three runs is K-converged (K-doubling moves them by up to 3.5·10⁻³), so those columns are
    illustrative only (R1).

### 3.6 Theorem R (Plan 33): bounded rough weights can break the pointwise law — Conjecture R proved in modified form — PROVED-mod-cite (R2 PROVED; R1 PROVED-mod-cite); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan33.md), fixes applied, re-check ACCEPT — REVIEWED

Setting: x_k = k^{−p} (p > 0), v_k := k^{−s} (s > 1), and w = v·e^{f} with f bounded. Notation q_j = √w·p_j,
μ_j = q_j² and K_m are as in §3.5. Put F_N(w) := log(b_N²/b_{N−1}²) and Δ²μ_N := μ_N − 2μ_{N−1} + μ_{N−2}.

**Lemma R2 (second-order control).** Along w(t) = v·e^{tf}, |(d²/dt²)F_N| ≤ 16‖f‖²_∞, for every N and every v
(with finite moments).

*Proof.*
- (d²/dt²) log D_m = Var_m⟨f, X⟩ (exponential tilting, as in Lemma FV), and
  Var_m⟨f, X⟩ = ½Σ_{k,l}(f_k − f_l)²K_m(k,l)² (§3.5 step 3).
- By the rank-one update, Var_{m+1} − Var_m = A + B, with A := Σ_{k,l}(f_k − f_l)²K_m(k,l)q_m(k)q_m(l) and
  B := ½Σ_{k,l}(f_k − f_l)²q_m(k)²q_m(l)².
- **Bound on A.** K_m is the orthogonal projection onto span{q_0, …, q_{m−1}} in ℓ²(atoms), and q_m is orthogonal to
  it, so K_mq_m = 0. Hence the f_k² and f_l² parts of A vanish, and A = −2⟨fq_m, K_m(fq_m)⟩ ∈ [−2‖f‖²_∞, 0].
- **Bound on B.** 0 ≤ B ≤ 2‖f‖²_∞.
- **Combine.** F_N is the third difference L_{N+1} − 3L_N + 3L_{N−1} − L_{N−2} of L_m := log D_m. So F_N'' is a second
  difference of (Var_{m+1} − Var_m). Each |Var_{m+1} − Var_m| ≤ |A| + B ≤ 2‖f‖²_∞ (A ≤ 0 ≤ B, so |A + B| ≤
  max(|A|, B)), and the coefficients of the second difference sum in absolute value to 4. So |F_N''| ≤ 8‖f‖²_∞; the
  stated 16 is a valid weaker constant (F5). ∎

**Lemma R1 (the pure power keeps a non-degenerate second difference).** For the pure power v there are η > 0, an integer window length J
and N₀ such that every N ≥ N₀ has some m ∈ [N − J, N] with ‖Δ²μ_m^{(v)}‖₁ ≥ η.

*Proof (by contradiction).* Suppose that for some (arbitrarily large) N, ‖Δ²μ_m‖₁ < η for all m ∈ [N − J, N]. Put
D_m := μ_m − μ_{m−1}.
1. **First differences are small.** ‖D_m − D_N‖₁ ≤ Jη for m ∈ [N − J, N]. Since μ_N − μ_{N−J} = Σ_{m=N−J+1}^{N}D_m
   has ℓ¹-norm ≤ 2, we get ‖D_N‖₁ ≤ 2/J + Jη, and ‖D_{N−1}‖₁ ≤ 2/J + Jη + η (F6). With J := ⌈2/δ⌉ and η := δ/J², both are
   ≤ 2δ.
2. **Moduli nearly agree.** (|a| − |b|)² ≤ |a² − b²| gives ‖|q_m| − |q_{m′}|‖₂² ≤ ‖μ_m − μ_{m′}‖₁ ≤ 4δ for
   m, m′ ∈ {N, N−1, N−2}.
3. **The recurrence forces concentration.** The recurrence b_Nq_N = (x − a_{N−1})q_{N−1} − b_{N−1}q_{N−2} holds at
   every atom. Let σ_k := sign(q_{N−1}(k)q_{N−2}(k)) ∈ {±1}, choosing +1 where the product vanishes (F6), and write |q_{N−2}| = |q_{N−1}| + e and |q_N| = |q_{N−1}| + e′,
   with ‖e‖₂, ‖e′‖₂ ≤ 2√δ. Then
   |b_N|q_N(k)| − |x_k − a_{N−1} − b_{N−1}σ_k|·|q_{N−1}(k)|| ≤ b_{N−1}|e_k|.
   Hence Σ_kμ_{N−1}(k)(|x_k − a_{N−1} − b_{N−1}σ_k| − b_N)² ≤ 16b̄²δ, with b̄ := max(b_N, b_{N−1}).
   - In the variable y := (x − a_{N−1})/b̄, this says ⟨dist(y, Z)², μ_{N−1}⟩ ≤ 16δ, where
     Z := {±b_{N−1}/b̄ ± b_N/b̄}.
4. **Moments contradict concentration.** Let m_j := ⟨y^j, μ_{N−1}⟩ = b̄^{−j}((J − a_{N−1})^j)_{N−1,N−1}, an exact
   finite expression in a_{N−1±i} and b_{N±i} for i ≤ j/2.
   - By the pure-power ratio asymptotics (a_n/(2b_n) = 1 + O(1/n) and n^p b_n = c(p)(1 + O(1/n)); RH_px, RH₁(r),
     RH_plt1b), (J − a_{N−1})/b̄ tends locally to the free Jacobi matrix (zero diagonal, unit off-diagonals). So
     m₂ → 2, m₄ → 6 and m₆ → 20 (central binomial coefficients), and Z → {−2, 0, 2}.
   - Put P(y) := y²(y² − 4), which vanishes on {−2, 0, 2}. Then |P(y)| ≤ C(dist(y, Z) + o(1))(1 + |y|³).
   - Cauchy–Schwarz gives |m₄ − 4m₂| = |⟨P, μ_{N−1}⟩| ≤ C(4√δ + o(1))(2(1 + m₆))^{1/2}.
   - But m₄ − 4m₂ → 6 − 8 = −2. For δ small and N large this is a contradiction. ∎

**Theorem R.** For every ε ∈ (0, ε₀] (ε₀ := η/16) there is f with |f| ≤ ε such that w := v·e^{f}, which satisfies
e^{−ε}k^{−s} ≤ w_k ≤ e^{ε}k^{−s}, has

  limsup_n |log(β_n²/β_{n−1}²)| ≥ εη/2,  β_n := n^p b_n/c(p).

Hence (T3) fails for w, directly from its definition in §2, and so does the pointwise b-law. H_all still holds for w,
and so does Theorem CL when p > 1 (F1).

*Proof.*
1. **Scales.** Let θ ∈ (0, ½] with g_p⁺ ≥ 1 on (0, 2θ] (Sat_p⁺), and γ := κ + 1 (Lemma TL). Choose good scales
   N₁ < N₂ < … (Lemma R1: in every [N − J, N] there is one) with θN_{i+1} > N_i^{γ}·i and N_i → ∞ fast.
   - Windows W_i := [θN_i, N_i^{γ}] are disjoint.
   - Put f := Σ_i f_i with f_i := ε·sign(Δ²μ_{N_i}^{(v)}) on W_i. The signs are computed for the *pure power* v.
2. **Gain at scale N_i.** By Lemma FV, (d/dt)F_N = ⟨f, Δ²μ_N⟩. By Lemma R2,
   F_{N_i}(ve^{f_i}) − F_{N_i}(v) ≥ ε‖Δ²μ_{N_i}^{(v)}|_{W_i}‖₁ − 8ε².
   - Outside W_i, μ_{N_i}, μ_{N_i−1} and μ_{N_i−2} have mass → 0: the head by Sat_p⁺ (k/m ≤ 2θ for m = N, N−1, N−2 once
     N ≥ 4), and the tail by Lemma TL (with its own tolerance ε′, not the roughness ε, and μ_{N−2} ≤ ρ_{N−1} ≤ ρ_{N+1})
     (F7, F8). So
     ‖Δ²μ|_{W_i}‖₁ ≥ η − o(1).
3. **Cross-scale independence.** The other windows lie in the head (j < i: W_j ⊂ [1, N_{i−1}^γ] ⊂ [1, θN_i)) or in
   the tail (j > i: beyond θN_{i+1} > N_i^γ).
   - Along the path from ve^{f_i} to w, Lemma FV gives |F_{N_i}(w) − F_{N_i}(ve^{f_i})| ≤ ε·sup_t(μ_N + 2μ_{N−1} +
     μ_{N−2})(head ∪ tail) = o(1), uniformly by the sandwich [e^{−ε}, e^{ε}].
4. **Conclude.** F_{N_i}(v) = −2p log(N_i/(N_i − 1)) + O(1/N_i) → 0 (pure power). So
   |log(β_{N_i}²/β_{N_i−1}²)| ≥ εη − 8ε² − o(1) ≥ εη/2 − o(1) for ε ≤ ε₀ = η/16. Only F_N(v) → 0 is used here (F7). ∎

**Remarks.**
- **R-a (the dichotomy, now proved).**
  - Decaying roughness (ψ_k → L), and more generally polynomially slowly varying Ψ, preserves the full pointwise law:
    T3-sv and T3a.
  - Bounded roughness of any fixed size ε can destroy it: Theorem R.
  - Averaged laws survive all sandwiched roughness: H_all for all p > 0, and CL for p > 1.
  - The (T3) half of G1-R as posed in §4 (pointwise law from atom regularity and sandwiched weights) is therefore
    **refuted**. The (CL) half is unaffected (F3).
- **R-b.** The constants η and J are not explicit, because Lemma R1 is proved by contradiction. Numerically
  ‖Δ²μ_N‖₁ ≈ 1.2–1.35 at p = s = 2 (§3.2 [1]).
- **R-c.** The scale separation needed is polynomial (θN_{i+1} > N_i^{κ+1}). Numerically, ×4 suffices (§3.2 [3]).
- **R-d.** Novelty UNCHECKED. Possible prior art (reviewer's recollection, unverified): Lubinsky's counterexamples to
  Freud's conjecture for non-smooth weights; Máté–Nevai–Totik; Simon, *Szegő's Theorem and Its Descendants*. Instability of ratio asymptotics under non-decaying perturbations is consistent with the
  OPUC/OPRL literature (Rakhmanov-type theorems need the perturbation to be "small at infinity" in suitable senses).
  This is a recollection, not cited.

### 3.7 Lemma TC and Theorem T3-avg (Plan 34): density-one pointwise law for slowly varying weights — TC PROVED-mod-cite (P); T3-avg PROVED-mod-cite; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan34.md), fixes applied, re-check ACCEPT — REVIEWED

Setting: x_k = k^{−p} (p > 0), sandwiched weights c·k^{−s} ≤ w_k ≤ C·k^{−s} (s > 1); notation μ_n, ρ_m as in
§3.2–3.5.

**Lemma TC (tail count).** For each fixed M ≥ 2 and all m,

  𝔼_m#(S ∩ (Mm, ∞)) ≤ (2A/(p log M))·m + o(1),

with A := 4p + 2|κ_p| (G2 A-U, using E_p = κ_p from G2 B*(iii)). The o(1) depends on M, p and the sandwich constants
(c, C, s) only.

*Proof.* Let T_j denote the Heine mass of index sets with exactly j elements beyond Mm.
- G2 Theorem A-U (with its M, valid for every p > 0) gives log T_j ≤ −pm²log m + E_pm² + m²(At − pt²log M)
  + O_M(m log m), with t = j/m. The constants depend on the weights only through W = Σw.
- G2 B*(iii) gives E_p = κ_p (this is where the external citation (P) enters).
- G2 Theorem A-L gives log D_m ≥ −pm²log m + κ_pm² − o(m²); its constants depend on the weights only through c₁ and s.
- For t ≥ t₁ := 2A/(p log M), the bracket At − pt²log M is ≤ −At₁ (equality at t₁; concave and decreasing beyond
  t₁/2). So P_m(j ≥ t₁m) ≤ (m + 1)e^{−At₁m² + o(m²)}.
- Since j ≤ m, 𝔼#(beyond Mm) ≤ t₁m + m·P_m(j ≥ t₁m) = t₁m + o(1). (If t₁ ≥ 1 the lemma is trivial.) ∎

**Definition (uniformly slowly varying).** A bounded sequence Ψ with 0 < c ≤ Ψ ≤ C is *uniformly slowly varying* if
for all M, M′ ≥ 1

  δ_N(M, M′) := sup{|log Ψ(k) − log Ψ(n)| : n ∈ [N, 2N], k ∈ ℕ ∩ [n/M, M′N]} → 0  (N → ∞).

- Example: Ψ(k) = 2 + sin(log log k) (or log log(k + 2)). For n ∈ [N, 2N] and k ∈ [n/M, M′N],
  |log log k − log log n| ≤ max(log(log(M′N)/log N), −log(log(N/M)/log(2N))) → 0, sin is 1-Lipschitz and Ψ ≥ 1, so
  δ_N ≤ that quantity → 0.
- Every polynomially slowly varying Ψ (§3.4) is uniformly slowly varying. (Restrictions to ℕ of measurable slowly
  varying functions should also qualify, via the uniform convergence theorem; that source has not been read, so this is
  not used.)

**Theorem T3-avg.** Let w = vΨ with v = k^{−s} (s > 1) and Ψ bounded and uniformly slowly varying. Then

  (1/N)Σ_{n=N}^{2N}|log b_n²(w) − log b_n²(v)| → 0  and  (1/N)Σ_{n=N}^{2N}n^p|a_n(w) − a_n(v)| → 0.

Consequently there is a set J ⊂ ℕ of natural density one with n^p b_n(w) → c(p) and n^p a_n(w) → 2c(p) as n → ∞,
n ∈ J (by the pure-power laws RH₁(r), RH_p, RH_plt1b for v).

*Proof.* Take the path w(t) = vΨ^t, which stays in the sandwich [min(1, c), max(1, C)]·v. For n ∈ [N, 2N] put
g_n := log Ψ − log Ψ(n), with |g_n| ≤ G := log(C/c). Fix M ≥ 4 (the head margin of T3-sv) and M′ ≥ 6.
1. **Pointwise split.** By Lemma FV and centering (Σμ_n = Σμ_{n−1} = 1),
   |log b_n²(w) − log b_n²(v)| ≤ ∫_0^1 Σ_k|g_n(k)|(μ_n^{(t)} + μ_{n−1}^{(t)})(k)dt
     ≤ 2δ_N + G·∫_0^1[(μ_n^{(t)} + μ_{n−1}^{(t)})(head ∪ A_N)]dt,
   where head = {k < n/M}, A_N := (M′N, ∞) (the same set for every n in the block) and δ_N = δ_N(M, M′) → 0 by
   hypothesis.
2. **Head:** exponentially small, uniformly in t (Sat_p⁺, as in T3-sv).
3. **Tail, on average.** For each t, telescoping and μ_m = ρ_{m+1} − ρ_m ≥ 0 give
   Σ_{n=N}^{2N}(μ_n^{(t)} + μ_{n−1}^{(t)})(A_N) ≤ ρ_{2N+1}^{(t)}(A_N) + ρ_{2N}^{(t)}(A_N) ≤ 2𝔼_{2N+1}^{(t)}#(S ∩ A_N).
   - Since M′N ≥ (M′/3)(2N + 1), A_N ⊂ ((M′/3)(2N + 1), ∞). Lemma TC with m = 2N + 1 and the fixed M := M′/3 ≥ 2
     bounds this by (4A/(p log(M′/3)))(2N + 1) + o(1), uniformly in t (the path stays in one sandwich class).
   - Each t ↦ (μ_n^{(t)} + μ_{n−1}^{(t)})(A_N) is continuous (A_N^c is finite and each ρ_m^{(t)}(k) is continuous in
     t), so the finite sum over n and ∫_0^1dt may be interchanged.
4. **Combine.** (1/N)Σ_{n=N}^{2N}|log b_n²(w) − log b_n²(v)| ≤ 2δ_N(N + 1)/N + o(1) + 12AG/(p log(M′/3)) + o(1).
   Let N → ∞, then M′ → ∞.
5. **a_n.** The same argument applies with Lemma FVa (2|q_{n−1}q_n| ≤ μ_{n−1} + μ_n) and the bounds
   a_n^{(t)}, b_n^{(t)} ≤ 2M^p(n−1)^{−p} of T3a step 1, which use only the head mass (Sat_p⁺) and so hold here uniformly
   in t. Off the head |x_k − a_n| ≤ 2M^pn^{−p}. This gives (1/N)Σn^p|a_n(w) − a_n(v)| ≤ C′(M, p, A)(δ_N + G/log(M′/3))
   + o(1).
6. **Density one.** Let X_n := |log b_n²(w) − log b_n²(v)| + n^p|a_n(w) − a_n(v)|, so (1/N)Σ_{n=N}^{2N}X_n → 0.
   - *Blocks to Cesàro.* Given η > 0 pick N₀ with block averages ≤ η for N ≥ N₀. Splitting [1, Y] into dyadic blocks
     [N, 2N] with N ≥ N₀ plus [1, N₀) gives Σ_{n≤Y}X_n ≤ O_{N₀}(1) + 2ηY. Hence (1/Y)Σ_{n≤Y}X_n → 0, and for each
     ε > 0, E_ε := {n : X_n > ε} has density 0 (Chebyshev).
   - *Single set (diagonal argument).* Write E_j := E_{1/j}; these increase in j. Choose N_1 < N_2 < … with
     #(E_{j+1} ∩ [1, Y]) ≤ Y/j for all Y ≥ N_j, and put J := ℕ ∖ ([1, N_1) ∪ ∪_j(E_{j+1} ∩ [N_j, N_{j+1}))).
     For Y ∈ [N_j, N_{j+1}) every piece with index i ≤ j lies in E_{j+1} ∩ [1, Y] (monotonicity), so
     #(J^c ∩ [1, Y]) ≤ N_1 + Y/j; hence J has density one. For n ∈ J ∩ [N_j, N_{j+1}), X_n ≤ 1/(j + 1), so X_n → 0
     along J.
   - Then n^pb_n(w) = n^pb_n(v)·exp(½(log b_n²(w) − log b_n²(v))) → c(p) and n^pa_n(w) → 2c(p) along J. ∎

**Remarks.**
- **avg1.** T3-avg covers uniformly slowly varying Ψ, e.g. 2 + sin(log log k), which T3-sv does not.
  - It gives the pointwise law outside a density-zero set of n. Upgrading this to all n would follow from localization
    at scale Mn (§3.2 reduction; §3.4 TL2) — now PROVED (Theorem L, §3.8), so T3-all gives all n.
  - Theorem R (§3.6) gives bounded, not slowly varying, weights for which the pointwise law fails along a sparse
    sequence of n. T3-avg does not apply to them, and whether a density-one law holds for such weights is open.
- **avg2 (NUMERICAL, p = s = 2 only; `checks/check_sv_density.out`).** For Ψ = 2 + sin(log log(k+2)),
  |β_n(vΨ)/β_n(v) − 1| and |A_n(vΨ) − A_n(v)| are ≤ 1.8·10⁻⁵ and decreasing at n = 200 … 3200 (the a-row is
  printed at n = 3199). The values are K-converged (K = 1.2·10⁵ vs 2.4·10⁵).
  - This is consistent with the pointwise law and is weak evidence only, since Ψ varies slowly over the accessible
    range.

### 3.8 Lemma TV, Lemma LP, Theorem L and Theorem T3-all (Plan 35): localization at scale Mn and the all-n law for bounded slowly varying weights — TV PROVED; LP, L, T3-all PROVED-mod-cite; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED

Setting as in §3.7: x_k = k^{−p} (p > 0), v = k^{−s} (s > 1), sandwiched weights; q_j = √w p_j(x_·) ∈ ℓ²(ℕ) is
orthonormal, K_m := Σ_{j<m} q_jq_jᵀ is the orthogonal projection onto span{q_0, …, q_{m−1}}, μ_m = q_m², and
ν(A) := Σ_{k∈A}ν(k).

**Lemma TV (tail variation).** Let w(t) = w(0)e^{tf} with f bounded, and A ⊂ ℕ. Then t ↦ μ_m^{(t)}(A) is C¹ and

  (d/dt)μ_m(A) = ⟨f1_A q_m, q_m⟩ − 2⟨1_A q_m, K_m(fq_m)⟩ − ⟨fq_m, q_m⟩μ_m(A).

The right side is unchanged when f is replaced by f + const.

*Proof.* √w(t)x^j = √w(0)e^{tf/2}x^j is C^∞ in t as an ℓ²-valued map (f bounded, x_k ≤ 1), so q_0, …, q_m (Gram–Schmidt of
finitely many such vectors) are C^∞. Write q̇_m = ½fq_m + r with r ∈ span{q_0, …, q_m} (the derivative of the polynomial
factor has degree ≤ m). For j < m, differentiating ⟨q_m, q_j⟩ = 0 and using ⟨q_m, q̇_j⟩ = ½⟨fq_m, q_j⟩ (since
q̇_j − ½fq_j ∈ span{q_0..q_j} ⊥ q_m) gives ⟨r, q_j⟩ = −⟨fq_m, q_j⟩. Differentiating ⟨q_m, q_m⟩ = 1 gives ⟨r, q_m⟩ =
−½⟨fq_m, q_m⟩. Hence q̇_m = ½fq_m − K_m(fq_m) − ½⟨fq_m, q_m⟩q_m, and (d/dt)μ_m(A) = 2⟨1_Aq_m, q̇_m⟩ is the formula.
For f ↦ f + c the three terms change by cμ_m(A), −2c⟨1_Aq_m, K_mq_m⟩ = 0 and −cμ_m(A). ∎

**Lemma LP (localization for the pure power).** For v = k^{−s} and every M ≥ 1,

  μ_n^v((Mn, ∞)) → F_p(M) := (2/π)·arcsin√(min(1, M^{−p}/(4c(p))))  (n → ∞),

and the same holds for μ_{n−1}^v((Mn, ∞)). In particular F_p(M) ~ (1/π)c(p)^{−1/2}M^{−p/2} → 0 as M → ∞.

*Proof.* Let J be the Jacobi matrix of v. For fixed j and n > j, ∫(n^px)^j dμ_n^v = n^{pj}(J^j)_{nn} is a finite sum
over lattice paths from n to n of length j, which only use a_m, b_m with |m − n| ≤ j. By the pure-power laws
(RH₁(r), RH_p, RH_plt1b), n^pa_m → 2c(p) and n^pb_m → c(p) for each such m. So the j-th moment of the image ν_n of
μ_n^v under x ↦ n^px converges to (J_0^j)_{00}, where J_0 is the doubly infinite free Jacobi matrix with diagonal 2c(p)
and off-diagonal c(p). The spectral measure of e_0 for J_0 is the arcsine law on [0, 4c(p)], density
1/(π√(y(4c(p) − y))): J_0 = c(p)(2 + S + S*) with S the shift is diagonalized by Fourier series, with symbol
c(p)(2 + 2cos θ), so (J_0^j)_{00} = (1/2π)∫_0^{2π}(2c(p)(1 + cos θ))^j dθ, and the image of dθ/2π under
θ ↦ 2c(p)(1 + cos θ) is that arcsine law. It is compactly supported, hence determined by its moments, so ν_n
converges weakly to it (method of moments; textbook-standard, not separately cited: if probability measures ν_n have all moments finite and
these converge to the moments of a probability measure ν determined by its moments, e.g. compactly supported, then
ν_n → ν weakly). The
set {k > Mn} is {n^px_k < M^{−p}}, and the arcsine law has no atoms, so ν_n([0, M^{−p})) → F_p(M). For μ_{n−1}, rescale
by (n−1)^p; since ((n−1)/n)^p → 1 and F_p is continuous the limit is the same. ∎

**Definition (slowly varying, sequence form).** A bounded Ψ with 0 < c ≤ Ψ ≤ C is *slowly varying* if for every λ ≥ 1

  δ_n(λ) := max{|log Ψ(k) − log Ψ(n)| : k ∈ ℕ ∩ [n/λ, λn]} → 0  (n → ∞).

This is implied by ψ_k → L and by polynomial slow variation (§3.4), and it is equivalent to uniform slow variation
(§3.7).

**Theorem L (localization at scale Mn).** Let w = vΨ with Ψ bounded and slowly varying, G := log(C/c), and
w(t) = vΨ^t (t ∈ [0, 1]). For every M ≥ 4 and m ∈ {n − 1, n},

  limsup_{n→∞} sup_{t∈[0,1]} μ_m^{(t)}((Mn, ∞)) ≤ e^{4G}F_p(M).

*Proof.* Fix the head margin M₀ = M₀(p) ≥ 4 of T3-sv (g_p⁺ ≥ 1 on (0, 2/M₀]; F1: a fixed margin such as 4 does not
work for small p, since the saturated region u < u_s(p) can lie below 1/4). Fix n, m ∈ {n−1, n}, and put A := (Mn, ∞),
H := {k < n/M₀} (head), Mid := ℕ ∖ (H ∪ A) ⊂ [n/M₀, Mn]. Write M₁ := max(M, M₀).
Apply Lemma TV with f := g_n = log Ψ − log Ψ(n) (allowed: d/dt log w(t) = log Ψ differs from g_n by a constant).
- |g_n| ≤ G everywhere and |g_n| ≤ δ := δ_n(M₁) on Mid.
- The head mass η_n := sup_t μ_m^{(t)}(H) is exponentially small in n (Sat_p⁺; the path stays in the sandwich
  [min(1, c), max(1, C)]·v; as in the "Head" bullet of the T3-sv proof).
- Let y(t) := μ_m^{(t)}(A). The first and third terms of Lemma TV are each ≤ G·y in absolute value. For the second,
  ‖K_m‖ ≤ 1 and Cauchy–Schwarz give |2⟨1_Aq_m, K_m(g_nq_m)⟩| ≤ 2√y·‖g_nq_m‖, and
  ‖g_nq_m‖² = Σ_k g_n(k)²μ_m(k) ≤ δ² + G²η_n + G²y, so ‖g_nq_m‖ ≤ δ + G√η_n + G√y.
- Hence ẏ ≤ 4Gy + 2ε_n√y with ε_n := δ + G√η_n. For z := √(y + κ) (κ > 0), ż = ẏ/(2z) ≤ 2Gz + ε_n, so by Grönwall
  z(t) ≤ e^{2Gt}(z(0) + ε_n t). Letting κ → 0:

  √(μ_m^{(t)}(A)) ≤ e^{2G}(√(μ_m^v(A)) + δ_n(M₁) + G√η_n)  for all t ∈ [0, 1].

- As n → ∞, δ_n(M₁) → 0 (slow variation), η_n → 0, and μ_m^v(A) → F_p(M) (Lemma LP). ∎

**Theorem T3-all (pointwise Law P for bounded slowly varying weights).** Let w = k^{−s}Ψ (s > 1) with Ψ bounded and
slowly varying (sequence form). Then n^pb_n(w) → c(p) and n^pa_n(w) → 2c(p) as n → ∞ (all n, p > 0).

*Proof.* Fix M ≥ 4; M₀, M₁, H, Mid, A as in Theorem L.
1. **b_n.** By Lemma FV, |log b_n²(w) − log b_n²(v)| ≤ ∫_0^1Σ_k|g_n(k)|(μ_n^{(t)} + μ_{n−1}^{(t)})(k)dt
   ≤ 2δ_n(M₁) + 2Gη_n + G·sup_t(μ_n^{(t)} + μ_{n−1}^{(t)})(A). By Theorem L the limsup is ≤ 2Ge^{4G}F_p(M). Let M → ∞:
   b_n(w)/b_n(v) → 1, and n^pb_n(v) → c(p) by the pure-power laws.
2. **a_n.** By Lemma FVa (centered), |ȧ_n| ≤ Σ_k|g_n(k)|[|x_k − a_n|μ_n(k) + b_n(μ_{n−1} + μ_n)(k)]. T3a step 1 (which
   uses only Sat_p⁺, with head margin M₀) gives a_n^{(t)}, b_n^{(t)} ≤ 2M₀^p(n−1)^{−p} uniformly in t for n ≥ n₀. Off
   the head x_k ≤ (M₀/n)^p, so with C_p := 4M₀^p·2^p (≥ 2M₀^p(n/(n−1))^p + M₀^p for n ≥ 2) we have n^p|x_k − a_n| ≤ C_p
   and n^pb_n ≤ C_p there. Hence
   n^p|a_n(w) − a_n(v)| ≤ 3C_pδ_n(M₁) + 3C_pG·sup_t(μ_n^{(t)} + μ_{n−1}^{(t)})(A) + O(n^{p}Gη_n),
   with limsup ≤ 6C_pGe^{4G}F_p(M) → 0 as M → ∞. With n^pa_n(v) → 2c(p) this gives the a-law. ∎

**Remarks.**
- **L1 (what this closes).** T3-all contains T3-conv, T3-sv and (for all n) T3-avg. With Theorem R the dichotomy for
  bounded weights k^{−s}Ψ is: slowly varying Ψ ⇒ the full pointwise Law P; fixed-size roughness ⇒ it can fail.
  The (T3) target of G1-R is therefore settled (PROVED-mod-cite) for pure-power nodes k^{−p}, base k^{−s}, and bounded
  slowly varying Ψ. Lemma TC / T3-avg are no longer
  needed for this conclusion (they remain valid).
- **L2 (why it works).** Ensemble counts (TC, TL) bound ρ_{n+1} = Σ_{j≤n}μ_j, which is of order n at scale Mn; a single
  μ_n needs a gain of n. Lemma TV gets it from the projection structure: the only non-local term, ⟨1_Aq_m, K_m(fq_m)⟩,
  is controlled by √μ_m(A) times ‖fq_m‖, and ‖fq_m‖ is small where f is small. So localization is *transported* along
  the path from the pure power, whose localization is read off from its pointwise law (Lemma LP).
- **L2′ (lead, F9).** The same transport works for rough weights with |f| ≤ ε, giving localization up to O(ε) in √μ;
  whether this reaches the [0.6N, 1.6N]-window form of Conjecture R is not examined.
- **L3 (constants).** e^{4G} is crude (e.g. 81 for Ψ = 2 + sin(log log k)); numerically μ_n^w(A) ≈ μ_n^v(A).
- **L4 (open).** Unbounded slowly varying Ψ: G = ∞ and the Grönwall factor is lost. For log-type Ψ (e.g. (log k)^α)
  this is repaired by truncation (Theorem T3-log, §3.9); general unbounded slowly varying Ψ remains open. Other nodes
  x_k = f(k) need a substitute for the pure-power law in Lemma LP.
- **L5 (NUMERICAL, `checks/check_mn_loc.out`).**
  - [1] Lemma TV agrees with a central finite difference to 8 digits (p = s = 2, random f, n = 100).
  - [2] Pure power: μ_n((Mn, ∞)) vs F_p(M) for p = 2 (n ≤ 400), p = 1 (n ≤ 200), p = 0.5 (n ≤ 100), M = 2…16. E.g.
    p = 2, M = 4: 0.1025 (n = 400) vs 0.1018; p = 1, M = 16: 0.1114 vs 0.1131; p = 0.5 deviates by ≤ 0.006
    (small n, truncation at K = 4·10⁵).
  - [3] Ψ = 2 + sin(log log(k+2)): μ_n^w(A) agrees with μ_n^v(A) to 4 digits, and the Theorem L bound holds (loosely).

### 3.9 Theorem T3-log (Plan 36): unbounded log-type weights — TLw PROVED; T3-log PROVED-mod-cite; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan36.md), fixes applied, re-check ACCEPT — REVIEWED

Setting: x_k = k^{−p} (p > 0), v = k^{−s} (s > 1), w = vΨ with Ψ > 0 *not necessarily bounded*. Notation as in §3.8;
M₀ = M₀(p) ≥ 4 is the head margin of T3-sv (g_p⁺ ≥ 1 on (0, 2/M₀]), κ := (2 + 2/p)s/(s − 1) as in Lemma TL.

**Definition (log-type slowly varying).** Ψ > 0 on ℕ is *log-type slowly varying* if
- (i) it is slowly varying in the sequence form of §3.8 (δ_n(λ) → 0 for every λ ≥ 1), with the boundedness assumed there
  dropped; and
- (ii) for every γ > 1 (equivalently, by chaining, for γ = 2), D(γ) := sup_{n≥2} max{|log Ψ(k) − log Ψ(n)| : k ∈ ℕ ∩ [n, n^γ]} < ∞.

Examples: Ψ(k) = (log(k + e))^α (α ∈ ℝ; D(γ) ≤ |α|log γ), (log log(k + e^e))^α (D(γ) ≤ |α|log(1 + log γ)), products of these with bounded
slowly varying functions. Every bounded slowly varying Ψ qualifies (D(γ) ≤ G), so T3-log contains T3-all. Not
covered: e.g. exp(√log k), for which D(γ) = ∞.

**Polylog bound.** (ii) with γ = 2 and the chain n_0 = 2, n_{j+1} = n_j² give, for k ≥ 2,
|log Ψ(k)| ≤ |log Ψ(2)| + D(2)(1 + log₂ log₂ k) (log₂ := log base 2). Hence there are C_Ψ, β ≥ 0 with

  C_Ψ^{−1}(log(k + 2))^{−β} ≤ Ψ(k) ≤ C_Ψ(log(k + 2))^β  for all k ≥ 1.

**Lemma TLw (weight-explicit form of Lemma TL, step 3).** For n ≥ 2, any weight u > 0 with Σu < ∞, and k ≥ T″ (T′, T″ as in
Lemma TL), ρ_{n+1}^u(k) ≤ 1156·u_k/min_{T′≤j≤T″}u_j.

*Proof.* Lemma TL steps 1–3 verbatim: steps 1–2 do not involve the weight, and step 3 gives
∫P²du ≥ min_{T′≤j≤T″}u_j/34² for P with deg P ≤ n and P(x_k) = 1; then ρ_{n+1}^u(k) = u_kK_{n+1}^u(x_k, x_k). ∎

**Theorem T3-log.** Let w = k^{−s}Ψ (s > 1) with Ψ log-type slowly varying. Then n^pb_n(w) → c(p) and
n^pa_n(w) → 2c(p) (all n, p > 0).

*Proof.* Fix γ with γ(s − 1) > s(2 + 2/p) + p (this forces γ > 2 + 2/p). The largeness conditions used below are
M₁n ≤ n^γ (step 2) and T″ ≤ n^γ (step 3); both hold for n large. For n ≥ 2 let
π_n(k) := min(max(k, ⌈n/M₀⌉), ⌊n^γ⌋) and Ψ̃_n(k) := Ψ(π_n(k))/Ψ(n). Rescaling a weight by a constant does not change
(a_n, b_n), so w and w_n := vΨ/Ψ(n) have the same coefficients.
1. **Uniform sandwich for the truncation.** |log Ψ̃_n| ≤ D* :=
   sup_{n'}δ_{n'}(M₀) + D(γ) < ∞ (δ_n(M₀) → 0 and each δ_n(M₀) is finite). So every vΨ̃_n^t (t ∈ [0, 1]) lies in
   the fixed sandwich class [e^{−D*}, e^{D*}]·v.
2. **Bounded part (uniform version of Theorem L / T3-all).** The proofs of Theorem L and T3-all use the weight only
   through: (a) |g| ≤ G everywhere along the path; (b) |g_n| ≤ δ on Mid, with δ → 0; (c) the head bound (Sat_p⁺)
   uniformly over a fixed sandwich class; (d) Lemma LP for v. They therefore apply verbatim to the n-dependent family
   Ψ̃_n at index n, with G := 2D*, g_n := log Ψ̃_n (note Ψ̃_n(n) = 1), and δ := max_{k∈[n/M₁, M₁n]}|log Ψ(k) − log Ψ(n)|
   = δ_n(M₁) (for n large, M₁n ≤ n^γ, so Ψ̃_n = Ψ/Ψ(n) on [n/M₀, M₁n]). Hence
   log b_n²(vΨ̃_n) − log b_n²(v) → 0 and n^p(a_n(vΨ̃_n) − a_n(v)) → 0.
3. **Truncation error.** Take the path u(t) := vΨ̃_n e^{th_n}, h_n := log(Ψ/Ψ(n)) − log Ψ̃_n, from vΨ̃_n (t = 0) to w_n
   (t = 1). h_n vanishes on [⌈n/M₀⌉, ⌊n^γ⌋]; on H := {k < n/M₀} and T := {k > n^γ}, by the polylog bound,
   |h_n(k)| ≤ 4log C_Ψ + 2β(log log(k + 2) + log log(n^γ + 2)) =: ℓ_n(k), which is O(log log n) on H and
   O(log log k) on T. Along the path, u(t) = vΦ_t with Φ_t(k) between Ψ̃_n(k) and Ψ(k)/Ψ(n), so
   Φ_t(k)^{±1} ≤ C_Ψ²(log(k + 2))^β(log(n^γ + 2))^β·e^{D*} =: P_n(k), polylogarithmic in k and n.
   - *Head.* By Lemma Sat_p⁺ for the weight u(t), with W(t)/u_k(t) ≤ (Σ_jj^{−s}P_n(j))·k^sP_n(k) ≤ n^{O(1)} and
     k/m ≤ 2/M₀ for m ∈ {n − 1, n}: (μ_n + μ_{n−1})^{(t)}(H) ≤ n^{O(1)}e^{−2(n−1)}, uniformly in t.
   - *Tail.* By Lemma TLw (μ_m ≤ ρ_{n+1} for m ≤ n), for k > n^γ ≥ T″ (n large; T″ = O(n^{2+2/p})),
     μ_m^{(t)}(k) ≤ 1156(T″/k)^sP_n(k)·max_{T′≤j≤T″}P_n(j) ≤ C(log n)^{O(1)}n^{s(2+2/p)}k^{−s}(log(k + 2))^β.
   - *Cutoff (F1).* Lemmas FV and FVa are stated for bounded f, and h_n is unbounded on T. For K > n^γ put
     h_n^K := h_n·1_{k≤K} (bounded) and w_n^K := vΨ̃_ne^{h_n^K}. Every weight on the path vΨ̃_ne^{th_n^K} has the form
     vΦ_t with Φ_t(k) between Ψ̃_n(k) and Ψ(k)/Ψ(n), so the head and tail bounds above hold for it, uniformly in K and t,
     and |h_n^K| ≤ ℓ_n. The bounds below are therefore uniform in K. As K → ∞, w_n^K → w_n pointwise, dominated by
     vΨ̃_n + w_n (summable, with x_k ≤ 1), so every moment ∫x^jdw_n^K converges to ∫x^jdw_n; (a_n, b_n²) are continuous
     functions of the moments of order ≤ 2n + 1 (ratios of positive Hankel determinants), so the bounds pass to w_n.
   - *b_n.* By Lemma FV, |log b_n²(w_n^K) − log b_n²(vΨ̃_n)| ≤ sup_tΣ_{k∈H∪T}ℓ_n(k)(μ_n + μ_{n−1})^{(t)}(k)
     ≤ (log log n)·n^{O(1)}e^{−2(n−1)} + C(log n)^{O(1)}n^{s(2+2/p)}Σ_{k>n^γ}k^{−s}(log(k + 2))^{β+1}
     = o(1) + (log n)^{O(1)}n^{s(2+2/p) − γ(s−1)} → 0.
   - *a_n.* By Lemma FVa, |ȧ_n| ≤ Σ_k|h_n^K(k)|[|x_k − a_n|μ_n(k) + b_n(μ_{n−1} + μ_n)(k)] ≤ 3Σ_{k∈H∪T}ℓ_n(k)
     (μ_n + μ_{n−1})(k), using x_k, a_n, b_n ≤ 1. Multiplying by n^p, the same bounds give
     n^p|a_n(w_n^K) − a_n(vΨ̃_n)| ≤ o(1) + (log n)^{O(1)}n^{p + s(2+2/p) − γ(s−1)} → 0 by the choice of γ.
4. **Conclusion.** Letting K → ∞ in step 3 (uniform bounds, continuity in the moments), steps 2–3 give log b_n²(w) − log b_n²(v) → 0 and n^p(a_n(w) − a_n(v)) → 0; the pure-power laws
   (RH₁(r), RH_p, RH_plt1b) give n^pb_n(v) → c(p) and n^pa_n(v) → 2c(p). ∎

**Remarks.**
- **log1 (scope).** For pure-power nodes k^{−p} the full pointwise Law P now holds for every weight k^{−s}Ψ with Ψ
  log-type slowly varying, e.g. k^{−s}(log k)^α for every α ∈ ℝ. (A weight k^{−σ}L(k) with σ > 1 and L log-type slowly
  varying is the case s = σ; general slowly varying L, e.g. exp(√log k), is not covered.) Open: slowly varying Ψ with D(γ) = ∞, e.g.
  exp(√log k); here the truncated weight is not uniformly sandwiched and the Grönwall factor e^{4G} of Theorem L
  diverges.
- **log2 (why truncation is harmless).** b_n only sees the window [n/M₀, n^γ] up to errors that are exponentially small
  (head, Sat_p⁺) or polynomially small (tail, Lemma TLw); both survive polylogarithmic losses in the weight ratios.
- **log3 (NUMERICAL, `checks/check_log_weights.out`, p = s = 2 only).** For Ψ = log(k + e)^α, α ∈ {1, −2, 3},
  |β_n(vΨ)/β_n(v) − 1| and |A_n(vΨ) − A_n(v)| decrease from ≈ 10⁻³ (n = 100) to 2–6·10⁻⁵ (n = 3200),
  with halving ratios 2.16–2.25 per doubling (n·log n·deviation/|α| ≈ 0.46–0.49, consistent with |α|/(n log n)),
  in exact proportion 1 : 2 : 3 to |α|; K-converged (K = 1.2·10⁵ vs 2.4·10⁵).

### 3.10 Theorem RW (Plan 39): Conjecture R in window form — R1W PROVED-mod-cite; RW PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); Rule R pending; novelty UNCHECKED

Setting and notation as in §3.6 and §3.8: x_k = k^{−p} (p > 0), v_k := k^{−s} (s > 1), w = v·e^{f} with f bounded;
q_j = √w p_j, μ_j = q_j², D_m := μ_m − μ_{m−1}, Δ²μ_m := μ_m − 2μ_{m−1} + μ_{m−2}, F_m(w) := log(b_m²/b_{m−1}²). The
recurrence is b_Nq_N = (x − a_{N−1})q_{N−1} − b_{N−1}q_{N−2}, as in Lemma R1. c = c(p), u_s = u_s(p) := (4c(p))^{−1/p}
(G2 §1). For a measure-like sequence g and an index set S, g|_S := g·1_S and ‖g‖₁ := Σ_k|g(k)|. Superscript v means
"computed for the pure power v". Only R2, R1W, FV, LP and Sat_p⁺ are used. Lemma TL and Lemma TV are not needed (see
remark RW-c).

**Windows.** A *window* is a pair 0 < a < b < ∞, with W_N := ℕ ∩ [aN, bN]. It is *admissible* (for p) if b > u_s(p).
Put

  I_W := (b^{−p}, a^{−p}) ∩ (0, 4c),  Θ_W := {θ ∈ (0, π) : 2c(1 + cos θ) ∈ I_W},
  c_W := (1/π)∫_{Θ_W} dist(2cos θ, {−2, 0, 2})² dθ,
  δ_W := c_W/32,  J_W := ⌈2/δ_W⌉,  η_W := δ_W/J_W²,  ε₀(W) := η_W/16.

The window is admissible iff I_W ≠ ∅ (b^{−p} < 4c ⇔ b > u_s). Then c_W > 0: θ ↦ 2c(1 + cos θ) maps (0, π)
continuously onto (0, 4c), so Θ_W is a non-empty open set, and the integrand vanishes only where 2cos θ ∈ {−2, 0, 2},
i.e. at θ ∈ {0, π/2, π}. All of these constants depend only on (p, a, b), not on s. Their values (quadrature; `checks/check_rw.out` [1]): for W = [0.6, 1.6] and p = 2, c_W ≈ 0.2345,
J_W = 273, η_W ≈ 9.8·10⁻⁸, ε₀ ≈ 6.1·10⁻⁹. These are crude; see remark RW-b.

**Lemma u_s.** u_s(p) < 1 for every p > 0. Hence every window with b ≥ 1 is admissible; in particular [0.6, 1.6]
is admissible for every p > 0.

*Proof.* By G2 B*(i), μ*_u has density 1 on (0, u_s], so μ*_u((0, u_s]) = u_s. In the x-variable, u ≤ u_s is
x ≥ 4c. μ* is a probability measure, so u_s = 1 − μ*((0, 4c)). Finally μ*((0, 4c)) > 0: μ* = ∫_0^1ω_{β_t}dt, and
for t ∈ [½, 1] the arcsine law ω_{β_t} on [0, β_t] (distribution function (2/π)arcsin√(y/β_t), no atoms) gives
mass (2/π)arcsin√(4c/β_t) = (2/π)arcsin(t^{p/2}) ≥ (2/π)arcsin(2^{−p/2}) > 0 to [0, 4c) (β_t = 4ct^{−p}). So
μ*((0, 4c)) ≥ ½·(2/π)arcsin(2^{−p/2}) > 0. ∎ (Numerically u_s = 0.375, 0.5, 0.637, 0.763 for p = 0.5, 1, 2, 4; the formula
u_s = 2I(p)/π of G2 B*(i) is not needed.)

**Lemma LP-w (weak form of Lemma LP).** Let ν_n be the image of μ_n^v under x ↦ n^px. Then ν_n → ν weakly as
n → ∞, where ν is the arcsine law on [0, 4c(p)]: the image of dθ/π on (0, π) under θ ↦ 2c(1 + cos θ). Also
n^pa_n^v → 2c(p) and n^pb_n^v → c(p).

*Proof.* This is the content of the proof of Lemma LP (§3.8), which states "ν_n converges weakly to it" (method of
moments, from the pure-power laws RH_px for p > 1, RH₁(r) for p = 1, RH_plt1b for 0 < p < 1). The last two limits are
those pure-power laws. Index shifts by a bounded amount do not change them, since ((n + j)/n)^p → 1. ∎

**Lemma R1W (window non-degeneracy).** Let W be an admissible window. There is N₀ = N₀(p, s, W) such that for every
N ≥ N₀ some m ∈ [N − J_W + 1, N] has

  ‖Δ²μ_m^v|_{W_N}‖₁ ≥ η_W.

N₀ is not explicit (it depends on the rate in Lemma LP-w); δ_W, J_W, η_W are explicit.

*Proof.* Write S := W_N, δ := δ_W, J := J_W, η := η_W, and suppose ‖Δ²μ_m|_S‖₁ < η for every m ∈ [N − J + 1, N]
(all measures are those of v). We show that this fails for N ≥ N₀.
1. **First differences on S are small.** For m ∈ [N − J, N], D_N − D_m = Σ_{j=m+1}^{N}Δ²μ_j, so
   ‖(D_N − D_m)|_S‖₁ ≤ (N − m)η. Also μ_N − μ_{N−J} = Σ_{m=N−J+1}^{N}D_m, and ‖(μ_N − μ_{N−J})|_S‖₁ ≤ 2. So
   J‖D_N|_S‖₁ ≤ 2 + Σ_{m=N−J+1}^{N}(N − m)η = 2 + ηJ(J − 1)/2, i.e. ‖D_N|_S‖₁ ≤ 2/J + (J − 1)η/2. Since
   D_{N−1} = D_N − Δ²μ_N, ‖D_{N−1}|_S‖₁ ≤ 2/J + (J + 1)η/2. With 2/J ≤ δ and η = δ/J², both are ≤ 2δ (J ≥ 2).
2. **Moduli nearly agree on S.** Put e := |q_{N−2}| − |q_{N−1}| and e′ := |q_N| − |q_{N−1}|. Since
   (α − β)² ≤ |α² − β²| for α, β ≥ 0, Σ_{k∈S}e_k² ≤ ‖D_{N−1}|_S‖₁ ≤ 2δ and Σ_{k∈S}e′_k² ≤ ‖D_N|_S‖₁ ≤ 2δ.
3. **The recurrence on S.** Fix k ∈ S, let σ_k := sign(q_{N−1}(k)q_{N−2}(k)) (+1 if the product vanishes) and
   t_k := x_k − a_{N−1} − b_{N−1}σ_k. We claim
     |q_{N−1}(k)|·| |t_k| − b_N | ≤ b_{N−1}|e_k| + b_N|e′_k|.
   If q_{N−1}(k) = 0 the left side is 0. Otherwise q_{N−2}(k) = σ_k·sgn(q_{N−1}(k))·|q_{N−2}(k)|, so the recurrence
   gives b_N|q_N| = |(x_k − a_{N−1})|q_{N−1}| − b_{N−1}σ_k|q_{N−2}|| = |t_k|q_{N−1}| − b_{N−1}σ_ke_k|, hence
   |b_N|q_N| − |t_k||q_{N−1}|| ≤ b_{N−1}|e_k|; and b_N|q_N| = b_N|q_{N−1}| + b_Ne′_k. This proves the claim.
   - ||t| − b_N| = dist(t, {±b_N}) ≥ dist(x_k − a_{N−1}, Z̃) with Z̃ := {±b_{N−1} ± b_N}. Put b̄ := max(b_N, b_{N−1}),
     y_k := (x_k − a_{N−1})/b̄ and Z_N := Z̃/b̄. Squaring the claim ((α + β)² ≤ 2α² + 2β²) and summing over S, with
     step 2:
       Σ_{k∈S}μ_{N−1}(k)·dist(y_k, Z_N)² ≤ 2(‖e|_S‖₂² + ‖e′|_S‖₂²) ≤ 8δ = c_W/4.   (∗)
4. **Weak convergence contradicts (∗).** Put n := N − 1 and Y_k := n^px_k. Then y_k = φ_N(Y_k) with
   φ_N(Y) := (Y − n^pa_{N−1})/(n^pb̄). By Lemma LP-w, n^pa_{N−1} → 2c and n^pb̄ → c, so φ_N → φ(Y) := (Y − 2c)/c
   uniformly on compact sets, and Z_N → Z := {−2, 0, 2} in the Hausdorff distance d_H. Since dist(·, Z_N) is
   1-Lipschitz and |dist(y, Z_N) − dist(y, Z)| ≤ d_H(Z_N, Z), dist(φ_N, Z_N)² → dist(φ, Z)² uniformly on compact
   sets.
   - Choose a continuous h with 0 ≤ h ≤ 1, compact support in the open interval I_W, and
     ∫h·dist(φ, Z)²dν ≥ c_W/2. This is possible by monotone convergence (h_j ↑ 1_{I_W}). Note
     ∫_{I_W}dist(φ, Z)²dν = c_W, since φ(2c(1 + cos θ)) = 2cos θ.
   - k ∈ S ⇔ aN ≤ k ≤ bN ⇔ Y_k ∈ [(n/(bN))^p, (n/(aN))^p]. These endpoints tend to b^{−p} and a^{−p}, so for N
     large supp h lies inside this interval, and 1_S(k) ≥ h(Y_k) for all k.
   - Hence the left side of (∗) is ≥ ∫G_N dν_n with G_N := h·dist(φ_N, Z_N)². G_N → G := h·dist(φ, Z)²
     uniformly on [0, ∞) (both vanish off supp h), and G is bounded and continuous. So
     ∫G_Ndν_n = ∫Gdν_n + o(1) → ∫Gdν ≥ c_W/2 by Lemma LP-w.
   - So for N ≥ N₀ the left side of (∗) exceeds c_W/4, which contradicts (∗). ∎

**Theorem RW (Conjecture R in window form).** Let p > 0, s > 1, let W = (a, b) be an admissible window, and let
N₀, J_W, η_W, ε₀ := η_W/16 be as above. Let θ₁ = θ₁(p) ∈ (0, ½] be such that g_p⁺ ≥ 1 on (0, θ₁] (Sat_p⁺; it exists
because g_p⁺(θ) → +∞ as θ → 0). Let N₁ < N₂ < … be integers with N₁ ≥ max(N₀, 2J_W + 2) and bN_i < aN_{i+1}, and
satisfying either
- (A) N_{i+1}/N_i → ∞; or
- (B) N_{i+1} > R_W·N_i for every i, where R_W := max(b/a, 2b/θ₁, M_W/a) and
  M_W := max(1, (4c(p)·sin²(πη_W/32))^{−1/p}). Then M_W ≥ 1 and F_p(M_W) ≤ η_W/16 (F_p as in Lemma LP; F_p is
  nonincreasing, and F_p((4c sin²(πη_W/32))^{−1/p}) = (2/π)arcsin(sin(πη_W/32)) = η_W/16 since πη_W/32 < π/2).

For each i pick m_i ∈ [N_i − J_W + 1, N_i] as in Lemma R1W, put W_i := W_{N_i} = ℕ ∩ [aN_i, bN_i] and
s_i := sign(Δ²μ_{m_i}^v) (with sign 0 := +1), and set

  f := ε·Σ_i s_i·1_{W_i},  w := v·e^{f}.

Then for every ε ∈ (0, ε₀]: |f| ≤ ε, f is supported on ∪_iW_i, e^{−ε}k^{−s} ≤ w_k ≤ e^{ε}k^{−s}, and

  (A): liminf_i F_{m_i}(w) ≥ εη_W/2;  (B): liminf_i F_{m_i}(w) ≥ εη_W/4.

Consequently limsup_n |log(β_n²/β_{n−1}²)| ≥ εη_W/2 (resp. εη_W/4), with β_n := n^pb_n/c(p). So β_n does not
converge, (T3) fails for w (as in Theorem R), and so does the pointwise b-law. H_all still holds for w, and so does
Theorem CL when p > 1 (as in Theorem R).

*Proof.* The windows W_i are disjoint (bN_i < aN_{i+1}), so |f| ≤ ε and the sandwich holds. Fix i and m := m_i, and
put H_i := ∪_{j<i}W_j ⊂ [1, bN_{i−1}] and T_i := ∪_{j>i}W_j ⊂ [aN_{i+1}, ∞).
1. **Linearisation along the direct path.** Let u(t) := v·e^{tf}, t ∈ [0, 1]. By Lemma FV, (d/dt)F_m(u(t)) =
   ⟨f, Δ²μ_m^{(t)}⟩, and by Lemma R2 (valid along ve^{tf} for every bounded f and every m), |(d²/dt²)F_m| ≤ 16ε².
   Taylor's formula with integral remainder, F(1) = F(0) + F′(0) + ∫_0^1(1 − t)F″(t)dt, gives
     F_m(w) ≥ F_m(v) + ⟨f, Δ²μ_m^v⟩ − 8ε².
   (t ↦ F_m(u(t)) is C², as in the proofs of Lemma FV and T3-conv step 1.)
2. **Own window.** ⟨f, Δ²μ_m^v⟩ = ε‖Δ²μ_m^v|_{W_i}‖₁ + ⟨f1_{H_i∪T_i}, Δ²μ_m^v⟩, and the first term is ≥ εη_W by
   the choice of m (Lemma R1W). The second, the cross-window term, has absolute value
     E_i ≤ ε·Σ_{m′∈{m, m−1, m−2}} c_{m′}·μ_{m′}^v(H_i ∪ T_i),  (c_m, c_{m−1}, c_{m−2}) = (1, 2, 1).
3. **Head.** Let m′ ∈ {m, m − 1, m − 2}, so N_i − J_W − 1 ≤ m′ ≤ N_i and m′ ≥ N_i/2 (N_i ≥ 2J_W + 2). For
   k ∈ H_i, k ≤ bN_{i−1}. In case (A), k/m′ ≤ 2bN_{i−1}/N_i → 0, so k/m′ ≤ θ₁ for i large. In case (B),
   k/m′ < 2b/R_W ≤ θ₁. Then k < m′ (θ₁ ≤ ½), and μ_{m′} = ρ_{m′+1} − ρ_{m′} ≤ 1 − ρ_{m′} with Lemma Sat_p⁺ (W = ζ(s),
   w_k = k^{−s}, g_p⁺(k/m′) ≥ 1) give μ_{m′}^v(k) ≤ ζ(s)k^s((m′ + 1)/k)^{2(1−p)₊}e^{−2m′}
   ≤ ζ(s)(m′ + 1)^{s+2}e^{−2m′}. Summing over k ≤ m′:
     μ_{m′}^v(H_i) ≤ ζ(s)(m′ + 1)^{s+3}e^{−2m′} → 0  (i → ∞).
4. **Tail.** In case (A), fix M ≥ 1. For i large, aN_{i+1} > MN_i ≥ Mm′, so T_i ⊂ (Mm′, ∞) and, by Lemma LP (applied
   with n = m′ → ∞), limsup_i μ_{m′}^v(T_i) ≤ F_p(M). Since M is arbitrary and F_p(M) → 0, μ_{m′}^v(T_i) → 0. In
   case (B), aN_{i+1} > aR_WN_i ≥ M_Wm′, so limsup_i μ_{m′}^v(T_i) ≤ F_p(M_W) ≤ η_W/16.
5. **Conclusion.** By steps 3–4, limsup_iE_i = 0 in case (A) and ≤ 4ε·η_W/16 = εη_W/4 in case (B). F_m(v) → 0 by
   the pure-power b-law (n^pb_n^v → c(p); Lemma LP-w). With ε ≤ η_W/16, 8ε² ≤ εη_W/2. So
     (A) liminf_iF_{m_i}(w) ≥ εη_W − εη_W/2 = εη_W/2;  (B) liminf_iF_{m_i}(w) ≥ εη_W − εη_W/2 − εη_W/4 = εη_W/4.
   Finally log(β_m²/β_{m−1}²) = F_m(w) − 2p·log(m/(m − 1)) and the last term → 0. If β_n converged to a positive
   limit, then log(β_n²/β_{n−1}²) → 0, which is false; in particular β_n ↛ 1, i.e. the pointwise b-law fails. Let
   c′ := εη_W/2 in case (A) and εη_W/4 in case (B). Then |β_{n+1}/β_n − 1| ≥ 1 − e^{−c′/2} − o(1) for infinitely many
   n, and for n ≥ 1/δ the index n + 1 lies in [n, (1 + δ)n]. So ω(δ) ≥ 1 − e^{−c′/2} > 0 for every δ > 0, and (T3)
   fails. ∎

**Corollary RW′ (the [0.6N, 1.6N] form).** For every p > 0 and s > 1 the window [0.6N, 1.6N] is admissible (Lemma
u_s). So Theorem RW holds with W_i = ℕ ∩ [0.6N_i, 1.6N_i], spikes at m_i ∈ [N_i − J_W + 1, N_i], ε₀ = η_W/16 and
η_W = η_{[0.6,1.6]}(p), under either separation (A) N_{i+1}/N_i → ∞ or (B) N_{i+1} > R_WN_i. For p = s = 2 this is
Conjecture R (§3.2) restricted to ε ≤ ε₀ ≈ 6.1·10⁻⁹, with c = η_W/2 ≈ 4.9·10⁻⁸ in case (A).

**What is and is not proved (Conjecture R as stated in §3.2).**
- PROVED-mod-cite: the window form, for every admissible window (including [0.6N, 1.6N] for all p > 0, s > 1), with
  separation N_{i+1}/N_i → ∞ or a fixed explicit ratio R_W, for ε ≤ ε₀ (explicit), with an explicit c = η_W/2 that
  depends only on (p, a, b).
- For ε > ε₀ the qualitative failure still holds: the weight built with ε₀ lies in the [e^{−ε}, e^{ε}] sandwich, so
  for every ε > 0 some |f| ≤ ε breaks the pointwise b-law. The *linear* bound limsup ≥ cε with c independent of ε is
  not proved for ε > ε₀.
- NOT proved: (i) the bound for every ε > 0 with an absolute c (numerically the spike is Δ_m ≈ 1.2ε at p = 2 for
  ε ∈ {0.05, 0.2}, `check_rw.out` [3]); (ii) a realistic size of η_W (numerically ‖Δ²μ_m|_W‖₁ ≈ 1.06–1.09 against the proved
  η_W ≈ 10⁻⁷; the phase model predicts 1.144); (iii) small fixed ratios such as ×4 or ×8 (R_W ≈ 1.1·10⁸ for p = 2,
  W = [0.6, 1.6]). Items (ii) and (iii) are both limited by the size of η_W (R_W enters through F_p(M_W) ≤ η_W/16), and
  both would follow from a sharp R1W (outline target T6: η_W → (8/π)∫_{Θ_W}sin²θ dθ/π). These remain NUMERICAL.
- N₀ (from LP-w) is not explicit.

**Remarks.**
- **RW-a (relation to Theorem R).** Theorem R (§3.6) used windows [θN_i, N_i^{κ+1}] and polynomial separation, because
  at the time only Lemma TL localised the upper tail. RW uses Lemma LP (§3.8), so windows of bounded aspect ratio and
  separation N_{i+1}/N_i → ∞ suffice, and R1W makes η_W explicit (R1's η is not). Theorem R remains valid as stated.
  Its ε₀ is non-explicit and is not compared with RW's, so R is not marked SUPERSEDED.
- **RW-b (constants).** δ_W = c_W/32 and J_W = ⌈2/δ_W⌉ come from the crude contradiction in R1W, which loses a factor
  J_W² ≈ 7·10⁴. The value of c_W is a quadrature (`check_rw.out` [1]); the proof uses only c_W > 0.
- **RW-c (why no transport is needed).** outline_C_rough.md §2.1 proposed transporting tail localisation along
  ve^{f_i} → w by Lemma TV and Grönwall. That is unnecessary: Lemma R2 holds along the direct path ve^{tf} for every
  bounded f. So only the *linear* term needs localisation, and it is evaluated at the pure power v, where Lemma LP and
  Sat_p⁺ apply directly. The second-order term costs 8ε² regardless of where f lives.
- **RW-d (admissibility is necessary for this mechanism).** If b ≤ u_s then W_N lies in the saturated head of μ_m for
  m ≈ N, so ‖Δ²μ_m^v|_{W_N}‖₁ → 0 exponentially fast (Sat_p⁺), c_W = 0, and the first-order gain vanishes.
- **RW-e (Rule A pass).** Attempts: (1) sign(0) convention: irrelevant, since ⟨f_i, Δ²μ⟩ = ε‖Δ²μ|_W‖₁ either way.
  (2) The moving window in R1W step 4 is handled by h ≤ 1_S, with no continuity-set argument needed for the lower
  bound. (3) Distinctness of the m_i is not needed: each i is treated separately, and only m_i ≥ N_i − J_W + 1 → ∞ is
  used (for F_{m_i}(v) → 0, the head bound and Lemma LP). (4) Off-by-one in step 1 of R1W: Δ²μ_j is needed for j ∈ [N − J + 1, N] only, which is exactly
  the hypothesis. (5) Index convention of FV/F_m checked numerically against a finite difference (`check_rw.out` [0],
  9 digits). (6) R2 is used with its stated constant 16; its proof gives 8, which would allow ε₀ = η_W/8.
  (7) Degenerate windows a ↑ b: c_W → 0 and η_W → 0, so the statement degrades continuously; no false claim.
- **RW-f (NUMERICAL, `checks/check_rw.out`, float64 Lanczos with full reorthogonalisation).**
  - [2] The R1W mechanism, pure power, W = [0.6N, 1.6N]: Q_N := ⟨dist(y, Z_N)²1_S, μ_{N−1}⟩ = 0.2264, 0.2293, 0.2307
    (p = 2, N = 100, 200, 300) against its limit c_W = 0.2345; 0.1217, 0.1245 (p = 1, N = 50, 100) against
    c_W = 0.1268. min_{m∈[N−7,N]}‖Δ²μ_m|_{W_N}‖₁ = 1.06–1.09 (p = 2) and 0.70–0.76 (p = 1), against phase-model
    values 1.144 and 0.794 and the proved η_W ≈ 10⁻⁷ / 1.6·10⁻⁸.
  - [3] The construction, p = s = 2, W = [0.6N, 1.6N], scales (30, 240) and (15, 60, 240), ε = 0.05 and 0.2. The
    deviation Δ_m := F_m(w) − F_m(v) at each spike m_i equals the linear prediction ⟨f, Δ²μ_m^v⟩ to ≤ 2%
    (e.g. 0.2389 vs 0.2403 at N = 240, ε = 0.2). The cross-window part is ≤ 1.4·10⁻³ even at ratio 4. Every spike
    exceeds the off-spike maximum of |Δ_n| (0.020–0.026 vs ≥ 0.060 at ε = 0.05; 0.083–0.103 vs ≥ 0.239 at ε = 0.2). Doubling
    the truncation K changes the spikes by ≤ 10⁻³.
  - These runs use ε ≫ ε₀ and small, finitely many scales. They test the mechanism (linearisation, own-window gain,
    cross-window decoupling), not the proved constants.

## 4. G1-R: what remains (stop report)

**Where G1 stands after Plan 9 (updated by Plan 27).**
- *b_n side.* Pointwise b_n ⟺ (T3) slow oscillation of β_n, given H_all (G1-T). Unconditionally, the single
  geometric Cesàro mean converges under a one-sided bound (G1-L).
- *a_n side.* The lower half holds unconditionally in window average (A1). For p > 1, the upper half holds in
  tail-Cesàro form. This is unconditional for pure-power atoms with rough weights by Theorem CL (Plan 27). Block-Cesàro
  ratios and window-average density still need β_n → 1 (A4). Pointwise density is not proved.
- *Plans 29–32:* the full pointwise law (b and a) holds for weights k^{−s}Ψ with Ψ bounded and polynomially slowly
  varying (T3-conv, T3-sv, T3a). Fixed-size adversarial roughness (ε ≤ ε₀) breaks it (Theorem R, §3.6).
- *Plan 34:* for Ψ bounded and uniformly slowly varying the full pointwise law holds on a density-one set of n
  (Lemma TC, Theorem T3-avg, §3.7).
- *Plan 35:* localization at scale Mn holds (Theorem L), so the full pointwise law holds for **all n** for every
  bounded slowly varying Ψ (Theorem T3-all, §3.8). (T3) is settled (PROVED-mod-cite) for pure-power nodes k^{−p}, base
  k^{−s}, and bounded slowly varying Ψ.
- *Plan 36:* the same for unbounded log-type slowly varying Ψ, e.g. (log k)^α (Theorem T3-log, §3.9).
- G1-L needs a one-sided bound on β_n; it is not unconditional.

**Missing statements (precise).** (For *rough* sandwiched weights the (T3) half is refuted by Theorem R, §3.6.)
- ~~(T3) for β_n := n^p b_n/(c(p)C), from atom regularity (H-a) and weight conditions~~: REFUTED in this generality (Theorem R, §3.6). For bounded slowly varying weights (T3) and the full pointwise law are PROVED (Theorem T3-all, §3.8). Unbounded log-type Ψ (e.g. (log k)^α): PROVED-mod-cite (Theorem T3-log, §3.9). Open: slowly varying Ψ with D(γ) = ∞ (e.g. exp(√log k)), and nodes other than pure powers.
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

**Stop condition (Plan 9; updated through Plan 36).** (CL) is proved for pure-power atoms with rough weights
(Theorem CL). For pure-power nodes k^{−p} the Plan-9 missing step was supplied in two parts: the RH analyses of the pure
powers (RH₁(r), RH_p, RH_plt1b; Plans 10–15) and the transport to bounded slowly varying weights (Theorem T3-all,
Plan 35). For rough weights (T3) is refuted (Theorem R). Unbounded log-type Ψ is covered by T3-log (Plan 36). What remains open: slowly varying Ψ with D(γ) = ∞ (e.g. exp(√log k)),
nodes other than pure powers, and (CL) for general nodes or p ≤ 1.

*(Superseded, Plan 9 text, kept for the record.)* (T3) was "not reached by the methods developed here"; the "most
promising next step" named there, an RH analysis à la BKMM/WLXZ for x_k = k^{−p} with weights k^{−s}, was carried out
in Plans 10–15.
