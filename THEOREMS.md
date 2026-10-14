# THEOREMS — jacobi-asymptotics (consolidated index, DRAFT)

> Draft compiled 2026-10-14 from master at commit 38bfb3b. Read-only consolidation: every label below is copied
> from the source status table or section header named in the "Location" column. Nothing has been upgraded. Where two
> sources disagree, the disagreement is listed in §5, not resolved here. Novelty is UNCHECKED throughout unless a
> source says otherwise. Measures built from ζ-zeros take the ordinates as real numbers (AGENTS.md rule 3). RH occurs
> only as a labelled hypothesis of conditional results (G3′ §9, rhfree/).
>
> **Plan 36 note.** The brief for this draft said Plan 36 (Theorem T3-log, G1 §3.9) was in review on another branch.
> It was merged to master *while this draft was being written* (commits e2f563d → 99e0487 → 38bfb3b, 13:46–13:54
> 2026-10-14). G1 PROOF.md §0 and §3.9 and README now label it REVIEWED. It is listed below with that source label and
> flagged ⚑.

Label vocabulary (VERIFICATION_POLICY.md; G1 §0; G2 §0): PROVED; PROVED-mod-cite (X) = proved from external results X
quoted with hypotheses in a CITATIONS.md; PROVED-mod-input (X) = proved modulo a named input (Lean
`lean/JacobiAsym/Inputs.lean`, or a stated hypothesis); CONDITIONAL = proved under a stated hypothesis that is not a
named Lean input; NUMERICAL; GAP = precise unproved statement; REVIEWED = Rule R second reader done. "Certified" only
means Arb/ball arithmetic.

Notation: c(p) := ¼(π/(2I(p)))^p, I(p) := (√π/2)Γ(1/p + ½)/Γ(1/p + 1); κ_p := 3p/2 + log c(p); c(2) = π²/16.
σ_{p,s} := Σ_k k^{−s}δ_{k^{−p}}. β_n := n^p b_n/(c(p)C). Φ_n := −2n²log n + 2Σ_{j<n}(n−j)log L(j) + κn²,
κ = 3 + log(π²/16) (smooth-ζ normalization).

---

## 1. Overview and headline results

The repo studies Jacobi coefficients (a_n, b_n) and Hankel determinants D_n of σ = Σ w_kδ_{x_k}, x_k ↓ 0. "Law P" is
b_n/x_n → c(p) (and a_n ~ 2b_n) for x_k ~ Ck^{−p}. The averaged (n²) law is proved for every p > 0 by identifying the
n² constant as a constrained logarithmic equilibrium (G2). The pointwise law with an O(1/n) rate is proved for every
pure power σ_{p,s} (p > 0, s > 1) and for the smooth-ζ model, by Riemann–Hilbert analyses that perturb cited
constructions (G1/RH). The pure-power laws are transported to weights k^{−s}Ψ with Ψ slowly varying. For fixed-size
roughness of the weights the pointwise law can fail (G1). For the true ζ-zero measure (G3′) the averaged law holds up to
O(n²) unconditionally (mod (C1), (C5), Theorem H). It holds exactly iff a capped near-pair energy of the ordinates is
o(K²), and it holds under several stated pair-correlation / prime-variance hypotheses. Lean formalizes the reduction
Theorem H ⇒ Theorem H_L / Corollary H_L-ζ with Theorem H as a named input.

**H1. Theorem H_all (averaged Law P, every p > 0).** G2 PROOF.md §3.
"Let p > 0 and C > 0. Let x_k = f(k) with f ∈ C¹[1, ∞), ξ^{p+1}f′(ξ) → −pC, and ξ^{p+1}|f′(ξ)| bounded above and
below … Let the weights satisfy Σ_k w_k < ∞ and w_k ≥ c₁k^{−s}. Then log D_n(Σ_k w_kδ_{x_k}) = −pn²log n +
(3p/2 + log(c(p)C))n² + o(n²). Equivalently, (2/n²)Σ_{j<n}(n−j)log(j^p b_j) → log(c(p)C)."
Label: **PROVED-mod-cite (P)**; G2 REVIEWED. External input: **(P)** (Beckermann–Kalyagin–Matos–Wielonsky
arXiv:1105.3088v2 Lemma 2.1, itself resting on Saff–Totik I.1.8 and Cegrell–Kolodziej–Levenberg Thm 2.5, *not read*;
accepted under mod-cite (P)). (P) enters only through B*(iii) (E_p = κ_p, optimality/uniqueness). The lower bound A-L is
citation-free. Corollary **HZ**: log det_{1≤i,j≤n}ζ(a(i+j)+b) = −an²log n + (3a/2 + log c(a))n² + o(n²), real a > 0,
2a + b > 1 (PROVED-mod-cite (P)).

**H2. Pointwise Law P with rate for every pure power (p > 0, s > 1).** G1 §0 rows RH₁(r), RH_p, RH_p 0<p<1 (seam).
For σ_{p,s}: n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n).
- p = 1, every r > 1: **Theorem RH₁(r)** (RH/RH_p1_general.md). Label: PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4,
  DLMF 5.11) + REVIEWED. (r = 3/2: Theorem RH₁, RH/RH_p1.md, PROVED-mod-cite (WLXZ v1) + REVIEWED.)
- p > 1, s > 1: **Theorem RH_p** (RH/px/RH_px.md). Label: PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6) + REVIEWED.
- 0 < p < 1, s > 1: **RH_p (seam)** (RH/plt1/RH_plt1b.md). Label: PROVED-mod-cite (WLXZ, KMVV §6 incl. angle freedom,
  G2 μ*/B*, DLMF 5.11) + REVIEWED; no numerical caveat.
External inputs: **WLXZ v1** (arXiv:1410.3948v1), **KMVV** (math/0111252v2 §6), **KV** §5, **Van** (math/0212014 §4),
**DLMF** 5.11 (and 5.5.3). G2's μ*/B*(i)–(ii) are used, which are citation-free (RH_px §2 uses B*(ii) only).

**H3. Theorem RH_ζ (smooth-ζ model, pointwise with rate).** RH/zeta/RH_zeta_close.md §5; G1 §0.
x_j = 1/(γ_j² + ¼), N₀(γ_j) = j − ½, masses 2x_j: "b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log² n)),
κ = −2(log(π/2) − (1 − log 2)); b_N = (β_N/4)(1+O(1/N)), a_N/(2b_N) = 1+O(1/N)." (κ = −0.28946…)
Label: **PROVED-mod-cite (WLXZ v1 §§3–6.1; KMVV §6; C–D Thm 4.4; DLMF; G2), REVIEWED.** Lemma Z (far field) is PROVED
with an **Arb-certified** winding computation. External: WLXZ v1, KMVV §6, **C–D** (Conway–Deift arXiv:1711.01590v4
Thm 4.4), DLMF (§§1.14, 5.5, 5.11, 5.12, 10.27, 10.39).

**H4. Weight transport and the dichotomy for weights k^{−s}Ψ (pure-power nodes).** G1 §§3.1–3.9.
- **T3-all** (§3.8): "Let w = k^{−s}Ψ (s > 1) with Ψ bounded and slowly varying (sequence form). Then n^pb_n(w) → c(p)
  and n^pa_n(w) → 2c(p) as n → ∞ (all n, p > 0)." PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺,
  L) + REVIEWED.
- ⚑ **T3-log** (§3.9, Plan 36): same conclusion for Ψ "log-type slowly varying" (slowly varying, unbounded allowed, and
  D(γ) := sup_{n≥2}max{|log Ψ(k) − log Ψ(n)| : k ∈ [n, n^γ]} < ∞), e.g. (log k)^α, α ∈ ℝ. PROVED-mod-cite (RH_px,
  RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TL(w), L, T3-all) + REVIEWED (per master; see Plan 36 note).
- **Theorem R** (§3.6): for ε ∈ (0, ε₀], ε₀ = η/16, there is f with |f| ≤ ε such that w = k^{−s}e^{f} has
  limsup|log(β_n²/β_{n−1}²)| ≥ εη/2; so (T3) and the pointwise b-law fail (all p > 0, s > 1). PROVED-mod-cite (RH_px,
  RH₁(r), RH_plt1b; internal FV, Sat_p⁺, TL, §3.5 two-point formula) + REVIEWED. η, J non-explicit.
- **Theorem CL / Cor. A4′** (§3.1): x_k = k^{−p}, p > 1, Σw < ∞, w_k ≥ c₁k^{−s} (rough weights allowed):
  n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p − 1). PROVED-mod-cite (P) (through G2 B*(iii)) + REVIEWED.
External inputs: those of H2 (transitively), plus (P) for CL/TC/T3-avg only. T3-all and T3-log do **not** use (P).

**H5. G3′ (true ζ-zero measure, σ = Σ 2x_kδ_{x_k}, x_k = 1/(γ_k² + ¼), ordinates with multiplicity).** G3′ PROOF.md.
- **G3′-U** (§3): limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0. PROVED-mod-cite + mod-input Theorem H (Lean `TheoremHPure`) +
  REVIEWED. Inputs: (C1) via Z1/Z2; Theorem H (p = 2).
- **Theorem B** (§8.1): liminf ≥ −3 log C > −∞, so log D_n = Φ_n + O(n²) with no hypothesis on the zeros.
  PROVED-mod-cite (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED. C not explicit.
- **Theorem Ch** (§5.4): G3′ ⟺ 𝒞(K) = o(K²), 𝒞(K) := min_{T⊂[k₂,K]}[P(T) + K·|[k₂,K]∖T|] (capped near-pair energy).
  PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED.
- Conditional closures of G3′ (each ⇒ (SG) ⇒ G3′): **Theorem C** (PCC in GLSS form, no RH), **Theorem S** (SPC_ℂ⁺, no
  RH), **Theorem S′** (SPC_ℂ⁺(full)), **Theorem V⁺** (RH + (V⁺)), **Corollary P** (RH + (V)). Necessity: **N″**
  (G3′ ⇒ d(E) = 0) and **N‴** (G3′ ⇒ d(T_β) = 0 ∀β > 0).
External inputs: **(C1)** Trudgian arXiv:1208.5846v2 Cor. 1; **(C5)** GLSS arXiv:2503.15449v4 (6.1); **(C3)** BGST
arXiv:2501.14545v3; **(C6)** Lamzouri arXiv:2609.02882v2; **(C8)** Goldston arXiv:math/0412313; named input **Theorem H
(p = 2)**.

**H6. Lean (sorry-free per lean/README.md; `check.sh` audit not re-run for this draft).**
`theoremHL` (Theorem H_L): **PROVED-mod-input (TheoremHPure …)**. `smoothZeta_HL`, `smoothZeta_HL_det` (Corollary
H_L-ζ) and `smoothZeta_bLaw` ((2/n²)Σ(n−j)log(b_j/x_j) → log(π²/16)): **PROVED-mod-input (TheoremHPure 2 κ 2,
κ = 3 + log(π²/16))**. Unconditional Lean results: `heineK_eq_det`, `heineD_eq_det` (Andreief/Heine), `hankel_det_eq_prod`
(H2), `opoly_recurrence`, `lemmaP` (α ≥ 2β), `toeplitz_count` ((S4): |N(T_ℓ(A,B); μ) − (ℓ/π)θ| ≤ 1, B ≥ 0),
`det_mul_cauchyBinet`. Named input: `TheoremHPure p κ s` (Inputs.lean: bounded in K and log D_n = −pn²log n + κn² +
o(n²) for atoms (k+1)^{−p}, weights (k+1)^{−s}).

---

## 2. Tables by area

Columns: name | exact short statement | label (verbatim) | location | depends on. "SUPERSEDED" = still valid, contained
in a later result.

### 2.1 Lean (lean/README.md table; lean/JacobiAsym/)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| `heineK`, `heineTerm`, `pairs`, `card_pairs` | Heine sum over n-subsets of range K | (definitions) | README row H1 | — |
| `heineK_mono_K`, `_mono_w`, `_smul_w` | monotone in atom set, weights; weight scaling (H3) | sorry-free | README | — |
| `heineTerm_le_of_pair_le(_split)`, `heineTerm_ge_of_pair_ge`, `orderEmb_ge` | pair-factor comparisons (H_L upper/lower) | sorry-free | README | — |
| `sum_prod_powersetCard_le`, `factorial_le_prod_succ`, `heineK_tail_split`, `heineTerm_tail_pointwise` | H7 steps 1–3 | sorry-free | README | — |
| `ratio_bounds_of_deriv`, `diff_le_of_L_mono`, `weighted_cesaro_slow`, `slow_shift`, `sum_log_div_le`, `neg_mul_log_le`, `phi_bound` | MVT, slow-variation limits, φ_M ≤ A²/(4p log M) | sorry-free | README | — |
| `heineD`, **`TheoremHPure`**, `hnorm` | D_n = sup_K heineK; Theorem H for pure powers as hypothesis | NAMED INPUT | Inputs.lean | — |
| **`theoremHL`** | Theorem H_L (slowly varying atoms) | **PROVED-mod-input (TheoremHPure; input available for p ∈ {1,2}, s ≥ s0(p))** | TheoremHL.lean | TheoremHPure (two instances: s and s0) |
| `lemmaP` | Lemma P: α ≥ 2β | sorry-free | LemmaP.lean | — |
| `det_mul_cauchyBinet` | det(AB) = Σ_S det A_S det B_S | sorry-free | README | — |
| `hankelK`, `heineK_eq_det` | truncated Heine sum = Hankel det of truncation | sorry-free | README | Cauchy–Binet |
| `hankel`, `heineD_eq_det`, `heineK_bdd_of_summable` | heineD = det(Σ' w x^{i+j}) for summable w ≥ 0, bounded x | sorry-free | README | — |
| `N0`, `zetaGamma(_spec, _hasDerivAt)`, `zetaL`, `zetaL_eps_eq`, `zetaL_slowFactor` | smooth-ζ model; SlowFactor 2 instance | sorry-free | README | — |
| `DMeasure`, `dip`, `mom`, `hankel_det_pos`, `opoly…`, `jb2`, `ja`, `opoly_recurrence` | D_n > 0; monic OPs; three-term recurrence, b_k² = D_{k+1}D_{k−1}/D_k² | sorry-free | README | — |
| `hankel_det_eq_prod` | H2: D_n = m₀ⁿΠ_{j<n}(b_j²)^{n−j} | sorry-free | README | — |
| `sum_log_weighted_asymp` | Σ_{j<n}(n−j)log j = n²/2 log n − 3n²/4 + o(n²) | sorry-free | README | — |
| `smoothZeta_HL_sumForm` | log D_n = −2n²log n + 2Σ(n−j)log L(j) + κn² + o(n²) | PROVED-mod-input | README | TheoremHPure 2 κ 2 |
| **`smoothZeta_bLaw`** | (2/n²)Σ(n−j)log(b_j/x_j) → log(π²/16) | **PROVED-mod-input (TheoremHPure 2 κ 2, κ = 3 + log(π²/16))** | BLaw.lean | smoothZeta_HL_det, H2 |
| **`smoothZeta_HL`, `smoothZeta_HL_det`** | Corollary H_L-ζ, Hankel-det form | **PROVED-mod-input (TheoremHPure 2 κ 2)** | SmoothZetaHL.lean | theoremHL |
| `toeplitzTri`, `toeplitz_eigen`, `toeplitz_charpoly_roots` | T_ℓ(A,B), B > 0: eigenvalues A + 2B cos(πi/(ℓ+1)) | sorry-free | Toeplitz.lean | — |
| **`eigCount`, `toeplitz_count`** | (S4): \|N(T_ℓ(A,B); μ) − (ℓ/π)θ\| ≤ 1, B ≥ 0 | sorry-free | Toeplitz.lean | — |

Not formalized: the forward Weyl law (item 11 "Theorem B"), Theorem H itself, everything in research/.

### 2.2 G2 (research/G2/PROOF.md; REVIEWED 2026-10-13)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| B0 | ∫log\|x−y\|dω_{[0,β]} = log(β/4) on [0,β], ≥ on [β,∞) | PROVED | §1 | — |
| B* | E_p := sup_{μ∈𝒜}I(μ) = κ_p, uniquely attained at μ* = ∫_0^1 ω_{[0,4c(p)t^{−p}]}dt | PROVED-mod-cite (P); the value I(μ*) = κ_p is citation-free | §1 | B0, (P) for (iii) optimality |
| A1 | discretization: point energy ≤ n²·(smeared energy) + C_M n log n, subsets of [1, Mn] | PROVED | §2 | — |
| A2 (Cor.) | head bound log V(S) ≤ −pN²log N + E_pN² + C′_M n log n | (in proof; no separate label) | §2 | A1, scaling |
| A-U | limsup (1/n²)[log D_n + pn²log n] ≤ E_p | PROVED (uses A1, B*-scaling; algebra of item 11 H7) | §2 | A1, item 11 H7 |
| A-L | liminf ≥ κ_p (= I(μ*_u)) | PROVED (citation-free: uses B*(i) and the value in B*(iii)) | §2 | B*(i), value of I(μ*) |
| **H_all** | see H1 | PROVED-mod-cite (P) | §3 | A-U, A-L, B*, item 11 H3, H4 |
| HZ | log det ζ(a(i+j)+b) = −an²log n + (3a/2 + log c(a))n² + o(n²), a > 0, 2a+b > 1 | PROVED-mod-cite (P) | §3 | H_all |

Prior art recorded: Monien arXiv:0901.1883 (p = 1, heuristic, same optimizer) (M).

### 2.3 G1 — Tauberian reductions, a_n side, weight transport (research/G1/PROOF.md)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| K | second difference of G(n) = Σ(n−j)u_j over ±h = triangle-kernel sum, mass h² | PROVED | §1 | — |
| **G1-T** | H_all + (T3) slow oscillation of β_n ⇒ β_n → 1 | PROVED-mod-cite (G2 (P)) | §2 | H_all, K |
| **G1-L** | H_all + one-sided bound on β_n ⇒ (1/n)Σ_{j<n}log(j^pb_j) → log(c(p)C) | PROVED-mod-cite (G2 (P)) | §2 | H_all |
| A1 | J ≥ 0 ⇒ sine-weighted window averages of a_j ≥ 2cos(π/(L+1))·min b | PROVED | §3 | (S4) / Lean `toeplitz_eigen` |
| A2 | p > 1: Σ_{j>n}a_j = 𝔼_n[Σ_{k∉S}x_k] (Heine ensemble) | PROVED | §3 | — |
| A3 | Q_p := ∫x d(σ − μ*) = 2c(p)/(p−1) | PROVED (uses only G2 B*(i) and the definition of μ*, both citation-free) | §3 | G2 B*(i) |
| A4 | (CL) ⇒ tail-Cesàro a-law; with β_n → 1, block ratios → 1, window averages → 1 in b-weighted density | CONDITIONAL on (CL) … tail-Cesàro part unconditional for pure powers via CL; (i)–(ii) still need β_n → 1 | §3 | A2, A3, (CL) |
| Sat_p | 1 − ρ_n(k) ≤ (W/w_k)e^{−2n g_p(θ)}, θ = k/n, p ≥ 1 | PROVED | §3.1 | G3′ §5.2 Lemma Sat |
| WC | concentration at speed n² of ν_S to μ*_u | PROVED-mod-cite (P) (through G2 B*(iii)) | §3.1 header | G2 A1, A-U, A-L, B*(iii) |
| **CL** | x_k = k^{−p}, p > 1, rough weights: n^{p−1}𝔼_n[Σ_{k∉S}x_k] → Q_p | PROVED-mod-cite (P) (through G2 B*(iii); internal: G2 A1, A-U, A-L; G3′ §5.2 Lemma Sat); REVIEWED; novelty UNCHECKED | §3.1 | Sat_p, WC, A3 |
| A4′ | unconditional tail-Cesàro a-law n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p−1), p > 1, rough weights | PROVED-mod-cite (P) (§3.1 header) | §3.1 | A2, CL |
| FV | d/dt log b_n²(ve^{tf}) = ⟨f, μ_n − μ_{n−1}⟩ | PROVED (standard; novelty not claimed); REVIEWED | §3.2 | — |
| Conj R | (T3) fails for some e^{−ε}k^{−2} ≤ w_k ≤ e^{ε}k^{−2} on windows [0.6N, 1.6N] | Proved in modified form as Theorem R (§3.6) … The [0.6N, 1.6N]-window form remains NUMERICAL | §3.2 | — |
| Sat_p⁺ | Sat_p for all p > 0 with factor ((n+1)/k)^{2(1−p)₊}, g_p⁺ | (no separate row; used as internal input; §3.3 header PROVED-mod-cite for the section) | §3.3 | Sat_p |
| **T3-conv** | ψ_k → L ∈ (0,∞): n^pb_n → c(p) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺); REVIEWED; novelty UNCHECKED — **SUPERSEDED by T3-all** | §3.3 | FV, Sat_p⁺, H2 |
| TL | sandwiched weights: μ_n((T,∞)) ≤ ε for T ≥ A n^κ ε^{−1/(s−1)}, κ = (2+2/p)s/(s−1) | PROVED (textbook-standard Markov/Chebyshev inequalities, quoted); REVIEWED; novelty UNCHECKED | §3.4 | Markov, Chebyshev (not checked against a source) |
| **T3-sv** | Ψ bounded, polynomially slowly varying: n^pb_n → c(p) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺, TL); REVIEWED — **SUPERSEDED by T3-all** | §3.4 | FV, Sat_p⁺, TL, H2 |
| FVa | d/dt a_n = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩ | PROVED (standard; novelty not claimed; self-contained via the proof of Lemma H and Christoffel–Darboux); REVIEWED | §3.5 | G3′ Lemma H proof |
| **T3a** | under T3-sv hypotheses, n^pa_n → 2c(p) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FVa, Sat_p⁺, TL); REVIEWED — **SUPERSEDED by T3-all** | §3.5 | FVa, Sat_p⁺, TL, H2 |
| R2 | \|d²F_N/dt²\| ≤ 16‖f‖²_∞ | PROVED | §3.6 | §3.5 two-point formula |
| R1 | pure power: ∃η, J: every [N−J, N] has m with ‖Δ²μ_m‖₁ ≥ η | PROVED-mod-cite | §3.6 | H2 (pure-power ratio asymptotics) |
| **Thm R** | see H4 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺, TL, §3.5 two-point formula); … REVIEWED; novelty UNCHECKED. Sub-labels: R2 PROVED; R1 PROVED-mod-cite | §3.6 | R1, R2, FV, Sat_p⁺, TL |
| TC | 𝔼_m#(S ∩ (Mm,∞)) ≤ (2A/(p log M))m + o(1), sandwiched weights | PROVED-mod-cite (P) (through G2 B*(iii); internal: G2 A1/A2, A-U, A-L) + … REVIEWED | §3.7 | G2 A-U, A-L, B*(iii) |
| **T3-avg** | Ψ bounded, uniformly slowly varying: full pointwise law on a density-one set of n | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; (P) via TC) + … REVIEWED — **SUPERSEDED by T3-all** (all n) | §3.7 | FV, FVa, Sat_p⁺, TC |
| TV | (d/dt)μ_m(A) = ⟨f1_Aq_m,q_m⟩ − 2⟨1_Aq_m, K_m(fq_m)⟩ − ⟨fq_m,q_m⟩μ_m(A) | PROVED (standard; novelty not claimed) + … REVIEWED | §3.8 | — |
| LP | pure power: μ_n((Mn,∞)) → F_p(M) = (2/π)arcsin√(min(1, M^{−p}/(4c(p)))) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; textbook method of moments) + … REVIEWED; novelty not claimed | §3.8 | H2 |
| **Thm L** | limsup sup_t μ_m^{(t)}((Mn,∞)) ≤ e^{4G}F_p(M), Ψ bounded slowly varying | PROVED-mod-cite (as LP; internal TV, Sat_p⁺) + … REVIEWED; novelty UNCHECKED | §3.8 | TV, LP, Sat_p⁺ |
| **T3-all** | see H4 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, L) + … REVIEWED; novelty UNCHECKED | §3.8 | FV, FVa, Sat_p⁺, L |
| ⚑ TLw | ρ_{n+1}^u(k) ≤ 1156·u_k/min_{T′≤j≤T″}u_j, any summable u > 0 | PROVED (§3.9 header) | §3.9 | TL proof |
| ⚑ **T3-log** | see H4 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TL(w), L, T3-all) + … REVIEWED; novelty UNCHECKED | §3.9 | T3-all, TLw |
| G1-R | (T3) from atoms alone; (CL) | (T3) half **REFUTED** for sandwiched weights (Theorem R); proved for polynomially slowly varying weights (T3-sv/T3a); (CL) half unchanged | §0, §4 | — |

### 2.4 G1 — pointwise laws by Riemann–Hilbert (research/G1/RH/)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| Theorem RH (p = 2) | n²b_n = c(2)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n), any r > 1 | **DRAFT — NOT a proof**; "The PROVED-mod-cite label below is withdrawn; the status is PROOF SKETCH" — SUPERSEDED in content by RH_p (p = 2 > 1) | RH/RH_proof.md §0; RH/RH.md (PROOF SKETCH) | — |
| **RH₁** | σ = Σk^{−3/2}δ_{1/k}: a_n = a_n^{TC}(1+O(1/n)), b_n = b_n^{TC}(1+O(1/n)); nb_n = ½(1+O(1/n)) | PROVED-mod-cite (WLXZ v1) + REVIEWED (file: WLXZ v1 §§2–6) — special case r = 3/2 of RH₁(r) | RH/RH_p1.md §0 | WLXZ v1 |
| **RH₁(r)** | σ_r = Σk^{−r}δ_{1/k}, r > 1: Nβ_N = 1 + O(1/N) ⇒ nb_n = ½(1+O(1/n)), a_n/(2b_n) = 1+O(1/n) | PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4, DLMF 5.11) + REVIEWED | RH/RH_p1_general.md §0 | WLXZ v1, KV, Van, DLMF |
| **RH_p** | σ_{p,s}, p > 1, s > 1: n^pb_n = c(p)(1+O(1/n)), a_n/(2b_n) = 1+O(1/n) | PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6) + REVIEWED (file also lists G2 μ*, B*) | RH/px/RH_px.md | WLXZ v1, KMVV, G2 B*(i)–(ii) |
| RH_p, ½<p<1 | same, ½ < p < 1 | PROVED-mod-cite (+ DLMF 5.5.3, 5.11) mod NUMERICAL no-winding (F4) + REVIEWED — **SUPERSEDED by seam** (file header) | RH/plt1/RH_plt1.md | RH_px |
| **RH_p, 0<p<1 (seam)** | same, all 0 < p < 1, s > 1 | PROVED-mod-cite (WLXZ, KMVV §6 incl. angle freedom, G2 μ*/B*, DLMF 5.11) + REVIEWED; no numerical caveat | RH/plt1/RH_plt1b.md | RH_px, KMVV angle freedom |
| E1 | finite-N constrained equilibrium / edge equation (generalizing G2 B*) | PROVED-mod-G2 | RH/zeta/RH_zeta.md §1 | G2 |
| E2, E3 | (edge-equation lemmas) | PROVED | RH/zeta/RH_zeta.md | — |
| E4 | — | NUMERICAL (convention-dependent) | RH/zeta/RH_zeta.md | — |
| Lemma Z | far field | PROVED, with an Arb-certified winding | RH/zeta/RH_zeta_close.md §2 | Arb |
| hard edge (§1), uniform edges (§3), rate (§4) | — | §1 PROVED-mod-cite (KMVV §6; C–D Thm 4.4; DLMF); §3 PROVED-mod-cite (WLXZ §6.1); §4 PROVED | RH/zeta/RH_zeta_close.md | — |
| **RH_ζ** | see H3 | PROVED-mod-cite (WLXZ v1 §§3–6.1; KMVV §6; C–D Thm 4.4; DLMF; G2), REVIEWED | RH/zeta/RH_zeta_close.md §5 | E1–E3, Z, §§1–4 |

### 2.5 G3′ (research/G3prime/PROOF.md §0 and rhfree/)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| Z1 | \|γ_k − γ̃_k\| ≤ C₀ (k ≥ k₁), ≤ C₀′ all k; C₀ ≤ 2.7 | PROVED-mod-cite + REVIEWED | §2 | (C1) |
| Z2 | pair ratio bound (x_a−x_b)/(x̃_a−x̃_b) ≤ … | PROVED-mod-cite + REVIEWED | §3 | Z1 |
| **G3′-U** | limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0 | PROVED-mod-cite + mod-input Theorem H (Lean `TheoremHPure`) + REVIEWED | §3 | Z2, item 11 H5/H6/H7, Theorem H (p = 2) |
| S | index shift π(a)⁻² − π(b)⁻² ≥ (1+η)⁻³(a⁻² − b⁻²) | PROVED + REVIEWED | §4 | — |
| W | log D_n(Σk⁻ˢδ_{Ck⁻²}) ≥ Λ_n − (s−3)Kn log n, s ≥ 4 | PROVED (from item 11 §7) + REVIEWED | §4 | Theorem A refs, H3 |
| **G3′-L** | liminf ≥ 0 under (SG) | PROVED-mod-cite + mod-input (SG), Theorem H + REVIEWED | §4 | Z1, S, W, H5, H6 |
| L′ | (LG*) ⇒ G3′; contains (SG) and "d(E) = 0 + log-gap" | PROVED-mod-cite (C1) + mod-input (LG*), Theorem H; REVIEWED; novelty UNCHECKED | §4.1 | G3′-L, G3′-U, Tr, K, W |
| Tr | truncation at J ≥ (M/2)n costs O(n²/log M) | PROVED-mod-input Theorem H (via Lemma K / item 11 H7); REVIEWED | §4.1 | Lemma H, Lemma K |
| N | doubled-smooth sequences (same counting fn.) fail by 2log(1−1/m) | PROVED-mod-input Theorem H + REVIEWED | §5 | Theorem H_L, item 11 H6 |
| N′ | d_*(E) > 0 ⇒ limsup ≤ 2log(1 − d_*(E)) | PROVED-mod-cite + mod-input Theorem H + REVIEWED; residual case closed by N″ | §5 | G3′*-U proof, Z1, Z2, T, H6 |
| **N″** | d̄(E) = η > 0 ⇒ liminf ≤ −0.2397η; hence G3′ ⇒ d(E) = 0 | PROVED-mod-cite (C1) + mod-input Theorem H …; REVIEWED; novelty UNCHECKED | §5.2 | Hadamard, Christoffel, G3′-U |
| **N‴** | gaps g_k ≤ e^{−βk} at positive upper density ⇒ law fails; G3′ ⇒ d(T_β) = 0 | PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED; novelty UNCHECKED | §5.3 | N″, G3′-U, Z1, Z2 |
| **Ch** | G3′ ⟺ 𝒞(K) = o(K²); contains N″, N‴, L′ qualitatively | PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED; novelty UNCHECKED | §5.4 | Lemma H, Sat, Tr, K, W, S, Z1, Z2, G3′-U, G3′-L |
| Ch on ζ data | 𝒞(K)/K² ≤ 1.1·10⁻⁷ at K = 2·10⁶ (Odlyzko) | NUMERICAL | §5.5 | — |
| **B** | liminf ≥ −3log C > −∞; log D_n = Φ_n + O(n²) | PROVED-mod-cite (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED | §8.1 | GLSS (6.1), Caro–Wei, §4 proof |
| **C** | PCC (GLSS form, no RH) ⇒ (SG) ⇒ G3′ | PROVED-mod-cite (C1), (C5) + mod-input PCC, Theorem H; REVIEWED | §8.2 | GLSS, G3′-L |
| P (Corollary P) | RH + (V) ⇒ G3′ | PROVED-mod-cite (C8 Thm 7, C8 SPC⇔(9.3) secondary, C8 Thm 4, C5, C1) + mod-input RH, (V), Theorem H; REVIEWED; novelty UNCHECKED (RH + (V) ⇒ PCC is KNOWN) | §9.1 | §8.2 |
| Lemma PC | K² sum under SPC_ℂ⁺ | PROVED-mod-cite ((C3) (3.1)–(3.2); (C6) §3 algebra) + mod-input SPC_ℂ⁺; REVIEWED | rhfree/RHFREE.md §1 | (C3), (C6) |
| Lemma G | spectral small-gap lemma (deterministic) | PROVED, REVIEWED | rhfree/RHFREE.md §2 | — |
| **Thm S** | SPC_ℂ⁺ ⇒ 100% simple critical, small gaps ≪ δ³N, (SG) ⇒ G3′ | PROVED-mod-cite ((C3), (C6) (2.4), (C1)) + mod-input SPC_ℂ⁺, Theorem H; REVIEWED; novelty UNCHECKED | rhfree/RHFREE.md §3 | PC, G, G3′-L |
| **Thm S′** | RH + upper half of Montgomery's SPC ⇒ G3′; RH-free: SPC_ℂ⁺(full) ⇒ G3′ | PROVED-mod-cite ((C3) (3.5), (C6), (C1)) + mod-input SPC_ℂ⁺(full), Theorem H; REVIEWED; novelty UNCHECKED | rhfree/RHFREE2.md §1 | PC′, G |
| Lemma N (RHFREE2) | inertia bound E ≥ k + 4Σm_z dist(h_z, V)² | PROVED (deterministic); REVIEWED; novelty UNCHECKED | RHFREE2 §2 | — |
| Cor. N1 | Σm_z dist(h_z,V)² ≤ (D·N_T + o(N_T))/4 | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺; REVIEWED | RHFREE2 §2 | PC |
| Prop. Q | SPC_ℂ⁺ + (NA) ⇒ max_{T<γ≤2T}\|β − ½\| → 0 (quasi-RH, not RH) | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺, (NA); REVIEWED; novelty UNCHECKED | RHFREE2 §2 | PC, N, (NA) |
| Lemmas P1, P2, P3 | prime/zero transfer on RH | P1: PROVED-mod-cite (via RH99 …) + mod-input RH, (V⁺); P2: PROVED-mod-cite ((C8) (4.2)–(4.4), (C3) (3.5), (C1)) + mod-input RH; P3: PROVED-mod-cite ((C6) §3 algebra) + mod-input RH, (V⁺); all REVIEWED | rhfree/RHPRIME.md | RH99 |
| Lemmas 9.7*, 9.9* | self-contained (C8) (9.7), (9.9) | PROVED-mod-cite ((C8) Prop. 1 (3.11), (C1) / (C8) (3.4)) + mod-input RH; REVIEWED | rhfree/RH99.md | (C8) |
| **Thm V⁺** | RH + (V⁺) ⇒ (SG) with rate δ³ ⇒ G3′ | PROVED-mod-cite ((C8) Prop. 1 + (3.4) via RH99, (C3) (3.5), (C6), (C1)) + mod-input RH, (V⁺), Theorem H; REVIEWED; novelty UNCHECKED | rhfree/RHPRIME.md §4 | P1–P3 |
| R, K | pair factors under thinning; concentration (from H7) | PROVED-mod-input Theorem H + REVIEWED | §7 | H5, H7 |
| T | thinning of convergent density: own-normalized law survives | PROVED-mod-input Theorem H + REVIEWED | §7 | R, K, H6, H7 |
| T′ | robustness: density band ±η ⇒ error ω(η) → 0 | PROVED-mod-input Theorem H + REVIEWED | §7 | T |
| G3′*-U | own-normalized upper bound under (D∞) | PROVED-mod-cite + mod-input (D∞), Theorem H + REVIEWED | §7.1 | Z2, T |
| G3′*-L | own-normalized law under (D∞) + (SG*) | PROVED-mod-cite + mod-input (D∞), (SG*), Theorem H + REVIEWED | §7.1 | Z1, T′, K |

Hypotheses (not results): (SG), (LG*), PCC (GLSS form), SPC_ℂ⁺, SPC_ℂ⁺(full), (V), (V⁺) (with RH), (NA), (D∞)
"N_d(T)/N(T) → θ ∈ (0, 1]", (SG*).

---

## 3. Dependency summary

### 3.1 External citations → results

| Input | Source (CITATIONS file) | Enters |
|---|---|---|
| (P) Beckermann–Kalyagin–Matos–Wielonsky Lemma 2.1 (+ unread Saff–Totik I.1.8, Cegrell–Kolodziej–Levenberg 2.5) | G2/CITATIONS.md | G2 B*(iii) ⇒ H_all, HZ; G1-T, G1-L; WC, CL, A4′; TC ⇒ T3-avg. **Not** in RH₁(r), RH_p, seam, T3-conv/sv/a, Thm R, L, T3-all, T3-log. |
| WLXZ v1 (arXiv:1410.3948v1) | G1/RH/CITATIONS.md | RH₁, RH₁(r), RH_p, seam, RH_ζ ⇒ (transitively) T3-*, LP, L, Thm R |
| KMVV §6 (math/0111252v2) | G1/RH/CITATIONS.md | RH_p, seam (angle freedom), RH_ζ |
| KV §5; Van §4 (math/0212014) | G1/RH/CITATIONS.md | RH₁(r) |
| DLMF 5.11 (+5.5.3; §§1.14, 5.12, 10.27, 10.39) | G1/RH/CITATIONS.md | RH₁(r), seam, RH_p ½<p<1, RH_ζ |
| C–D Thm 4.4 (arXiv:1711.01590v4) | G1/RH/CITATIONS.md | RH_ζ (log-weight hard edge) |
| Markov, Chebyshev polynomial inequalities | quoted as textbook, not checked against a source | TL ⇒ T3-sv, T3a, Thm R, T3-log (TLw) |
| (C1) Trudgian Cor. 1 | G3prime/CITATIONS.md | Z1, Z2 ⇒ every G3′ result except S, W, Lemma G, Lemma N |
| (C5) GLSS (6.1), Thm 1 | G3prime/CITATIONS.md | B, C, P |
| (C3) BGST (3.1), (3.2), (3.5) | G3prime/CITATIONS.md | PC, S, S′, P2, V⁺ |
| (C6) Lamzouri (2.4), §3 | G3prime/CITATIONS.md | PC, S, S′, P3, V⁺ |
| (C8) Goldston Prop. 1, (3.4), Thms 4, 7 | G3prime/CITATIONS.md | P, RH99, P1, P2, V⁺ |
| item 11 H3, H4, H5, H6, H7, §7 (math-pursuits f5f6aef) | item 11 | H_all (H3, H4), G3′-U/L, N, T, W |
| **Theorem H (named input `TheoremHPure`)** | lean/JacobiAsym/Inputs.lean | theoremHL, Cor. H_L-ζ, smoothZeta_bLaw; every G3′ result labelled "mod-input Theorem H" |

Note on Theorem H: G2's H_all (PROVED-mod-cite (P)) states the pure-power case for every p > 0 with weights Σw < ∞,
w_k ≥ c₁k^{−s}, error o(n²), which is the form of `TheoremHPure.asymp`. The repo does **not** record that G2 discharges
the Lean/G3′ input; all Lean and G3′ labels still say "mod-input Theorem H". Not upgraded here (see §5, item 1).

### 3.2 Fully self-contained (PROVED, no external citation, no named input)

G2: B0, A1, A-U, A-L (A-L is "citation-free"; it uses only B*(i) and the computed value I(μ*) = κ_p).
G1: K, A1, A2, A3, Sat_p, FV, FVa, TV, R2, TLw (and TL modulo the quoted textbook inequalities).
G3′: S, W (from item 11 §7), Lemma G, Lemma N (RHFREE2).
Lean: all items except `theoremHL`, `smoothZeta_HL(_det, _sumForm)`, `smoothZeta_bLaw` (sorry-free per lean/README).
**No headline result (H1–H5) is fully self-contained.** Each rests on (P), the RH-analysis citations, (C1)/(C5), or the
named input Theorem H.

---

## 4. Open problems (as stated in the repo)

**G3′**
1. **G3′ unconditionally**, i.e. 𝒞(K) = o(K²) for the ζ ordinates (Theorem Ch). Known: (U) and Theorem B
   (O(n²)) unconditional mod (C1), (C5), Theorem H; G3′ under (SG), PCC, SPC_ℂ⁺, SPC_ℂ⁺(full), RH + (V⁺), RH + (V).
   By N″, G3′ ⇒ d(E) = 0 (proportion-one distinct ordinates). Best unconditional input read: (C3) N_d ≥ 0.4075N;
   Lamzouri (C6) 67.25% simple and on the line. Numerically 𝒞(K)/K² ≤ 1.1·10⁻⁷ at K = 2·10⁶ (§5.5). The repo says
   explicitly that "as hard as a known open problem" is *not* claimed (§5.5).
2. **Explicit constant in Theorem B.** Needs an explicit O-constant in Fujii's second moment (GLSS (6.1)); not in what
   was read (§8.1 Remark B3).
3. **(Q1)** Does (V) on a restricted range, or a one-sided variance bound, give (SG) without RH (§9.3)? RH-free route
   needs a **weighted Lemma G**, "Recorded as OPEN" (RHFREE2 §4; RHPRIME header).
4. **(NA)** non-approximation hypothesis: "HYPOTHESIS. It is not proved." … "**OPEN**" (RHFREE2 §2).
5. Does SPC_ℂ⁺ alone confine zeros near the line (quasi-RH)? "Open; no claim about RH is made" (RHFREE §4).
6. **G3′\*** unconditionally: "the inputs read do not supply (D∞) or (SG*)" (§6, NOT REVIEWED exploration).

**G1 (pointwise law)**
7. **Slowly varying Ψ with D(γ) = ∞** (e.g. exp(√log k)): "here the truncated weight is not uniformly sandwiched and the
   Grönwall factor e^{4G} of Theorem L diverges" (§3.9 log1; §4). Known: bounded slowly varying (T3-all), log-type
   (T3-log ⚑).
8. **Nodes other than pure powers.** "Other nodes x_k = f(k) need a substitute for the pure-power law in Lemma LP"
   (§3.8 L4; §4). The analytic families done are pure powers (all p > 0) and the smooth-ζ model (README). The literature
   read has no RH analysis for general nodes accumulating at 0 with merely sandwiched weights (§4 point 2).
9. **(CL) for general nodes or p ≤ 1** (§3.1 CL4; §4). For p ≤ 1, J is not trace class and A2 does not apply as stated.
10. **Conjecture R, window form**: (T3) failure on windows [0.6N, 1.6N] "remains NUMERICAL" (§3.2); Theorem R uses
    windows [θN, N^{κ+1}]. Lead: transport of localization for |f| ≤ ε, "not examined" (§3.8 L2′).
11. **Density-one law for rough (Theorem R-type) weights**: "whether a density-one law holds for such weights is open"
    (§3.7 avg1).

**Additional open items found that were not on the brief's list**
12. Pointwise a_n for rough weights: A4 gives only tail/block/b-weighted-density forms; "A pointwise density statement
    does NOT follow"; "The matching upper bound (limsup ≤ 1) is the remaining a_n gap" (§3, A1/A4 text).
13. Second-order constants for pure powers: RH₁ n²(b_n^σ/b_n^{TC} − 1) → −1/24 "conjecture, not proved"
    (RH_p1.md §0); d₁ = −(s−1)/2, e₁ = p/2 are NUMERICAL Phase-0 fits (RH.md §0, RH_px §0); RH_p proves only O(1/n).
14. Lemma R1's η, J are non-explicit (proof by contradiction) (§3.6 R-b).
15. Novelty searches (Rule L) not done for any result; prior-art pointers recorded but unread (G2 §3; G1 CL3, R-d, TL).
16. Lean: Theorem H (`TheoremHPure`) and the forward Weyl law are not formalized (lean/README).
17. In review: none on master. (Plan 36 / T3-log was "in review" per the brief but is merged and labelled REVIEWED.)

---

## 5. Inconsistencies noticed

1. **Theorem H input vs G2 (stale scope).** lean/README `theoremHL` row and `Inputs.lean` docstring: "input available
   for p ∈ {1,2}, s ≥ s0(p)" (item 11). G2 H_all supplies the pure-power Theorem H for every p > 0 and all s with
   Σw < ∞ (mod (P)), and drops s₀(p) (G2 §3). No file records that G2 discharges `TheoremHPure`. Lean, G3′ and README
   therefore still say "mod-input Theorem H" everywhere.
2. **README G3′ first bullet is stale:** "G3′ (true zeros, Plan 7; pending Rule R review)" and "Stop condition: an
   unconditional lower bound needs multiplicity/small-gap input beyond the literature read". G3′ PROOF.md is REVIEWED,
   and Theorem B (Plan 17) gives an unconditional bounded lower bound. The later README G3′ bullet says "all REVIEWED".
3. **README G1 bullet (Plan 9) is stale:** "Stop report: GAP, with missing statements (T3) and (CL)" and "for p > 1, a
   conditional upper bound". (CL) is proved for pure powers (Theorem CL), and (T3) is refuted for rough weights and
   proved for slowly varying ones.
4. **README "Status" open list is garbled and stale:** "G1-R: (T3) for general, rough (non-analytic) weights and nodes.
   Plan 28: for *rough* sandwiched weights (T3) is REFUTED for rough sandwiched weights (Theorem R …)". This lists as
   open something that has been refuted, and the sentence is duplicated.
5. **G1 §0 row G1-R** still says "proved for polynomially slowly varying weights (T3-sv/T3a)". It should reflect T3-all
   and T3-log, as §4 does.
6. **G1 §3 A1 text:** "The matching upper bound (limsup ≤ 1) is the remaining a_n gap; see §4". §4 no longer lists it.
7. **RH_p1_general.md §0:** "By G1-T and A4 it discharges (T3) and (CL) for this family". The family is p = 1, but
   G1 §3.1 CL4 and A2 say (CL)/A2 "do not apply as stated" for p ≤ 1. (Same claim in docs/…plan-10 spec.)
8. **Stale "Open" sections inside superseded files:** RH_px.md end, "Open: 0 < p < 1" (closed by RH_plt1b);
   RH_plt1.md §6, "Open: 0 < p ≤ ½ … being tested" (header says superseded, body not updated); RH_zeta.md §4,
   "Hard edge 0 — OPEN" (closed in RH_zeta_close §1; header notes it).
9. **RH.md / RH_proof.md** (Theorem RH p = 2, PROOF SKETCH / DRAFT, label withdrawn) are not marked as superseded by
   RH_p (p = 2 is in p > 1).
10. **Label lists differ between file header and G1 §0:** RH_px header lists "G2 PROOF.md μ*, B*" among the mod-cite
    inputs, but G1 §0 does not. Only citation-free B*(i)–(ii) are used. RH₁: §0 says "(WLXZ v1)", the file says
    "(WLXZ v1 §§2–6)". Same for RH_ζ, where "G2" is listed even though E1(iv), the only (P)-dependent part, "is not
    needed".
11. **Unlabelled internal lemmas:** Sat_p⁺ (used by Thm R, T3-*, L) has no row in G1 §0. G2 Corollary A2 has no label.
    The §3.1 header labels WC and A4′, but §0 has no rows for them.
12. **G3′ §8.3 table "after Plan 17"** omits N″, N‴, L′, Ch, S, S′, V⁺. It is a historical snapshot but is not marked
    as one. README calls (U) "unconditionally", while its label carries "mod-input Theorem H" and (C1).
13. **G3′ status table names "P"**, but the section is "Corollary P". With citation (P) (G2), Lean `lemmaP`, "Law P"
    and Lemmas P1–P3, the letter P is heavily overloaded.
14. **Name clashes across areas:** "Theorem B" (item 11 forward Weyl law, lean/README) vs G3′ Theorem B (bounded
    defect). "Lemma K" (G1 kernel identity) vs G3′ Lemma K (concentration). "TC" (Tricomi–Carlitz in the G1 §0 RH₁ row)
    vs Lemma TC (tail count, §3.7). "Lemma S" (index shift) vs Theorem S. "Lemma N" (RHFREE2) vs Prop. N (G3′). κ
    means TL's exponent, RH_ζ's 1/log coefficient, and the Lean/G3′ constant 3 + log(π²/16).
15. **README G2 bullet** gives no label for Theorem H (it is PROVED-mod-cite (P)) and says HZ holds "for all a ≥ 1";
    G2 HZ covers real a > 0.
16. **Label vocabulary:** VERIFICATION_POLICY.md's table has no PROVED-mod-cite, CONDITIONAL or GAP (only the
    PROVED-mod-input addendum). These are defined locally in the G1 and G2 headers.
17. **Plan 36 timing:** the brief assumed T3-log was off master. It is now on master at 38bfb3b, labelled REVIEWED in
    G1 §0, §3.9 and README.
