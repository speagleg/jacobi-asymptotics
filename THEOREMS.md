# THEOREMS — jacobi-asymptotics (consolidated index)

> Compiled 2026-10-14 from master 38bfb3b + Plan 37 edits (branch plan-37-consolidate). Every label below is copied
> verbatim from the status table or section header named in the "Location" column, as corrected by Plan 37 (§5). (Plan 37:)
> Nothing has been upgraded — see the Plan 47 note below for the label upgrades of 2026-10-14; the only label change is the appended note on G3′ results "Theorem H input (p = 2, s ≥ 2) supplied
> by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (mod-cite (P))" (or, for G3′-L, "uses no
> Theorem H instance"); see §3.3. Revised after Rule R (research/G2/review/REVIEW_Plan37.md, F1–F9). Novelty is UNCHECKED throughout unless a source says
> otherwise. Measures built from ζ-zeros take the ordinates as real numbers (AGENTS.md rule 3). The Riemann Hypothesis
> occurs only as a labelled hypothesis of conditional results (G3′ §9, rhfree/); "RH" in G1/RH file names means
> Riemann–Hilbert.
>
> *Plan 47 (2026-10-14):* G2's only external citation (P) was replaced by the self-contained G2 Lemma EP (energy
> positivity, ported from Paper 1 Lemma 3.3). Results whose only external input was (P) are relabelled PROVED (G2 B*,
> H_all, HZ, Cor. H-input; G1 G1-T, G1-L, WC, CL, A4′, TC), T3-avg drops "(P) via TC", and the G3′ discharge note now
> reads "(PROVED since Plan 47; was mod-cite (P))". Every changed label is marked "Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED". Log: §5
> (Plan 47 block) and research/G2/LOG.md.

Label vocabulary (VERIFICATION_POLICY.md, which since Plan 37 also defines the repo's local labels): PROVED;
PROVED-mod-cite (X) = proved from external results X quoted with hypotheses in a CITATIONS.md; PROVED-mod-input (X) =
proved modulo a named input (Lean `lean/JacobiAsym/Inputs.lean`; G3′ also uses it for stated hypotheses on the zeros);
CONDITIONAL = proved under a stated hypothesis that is not a named Lean input; NUMERICAL; GAP = precise unproved
statement; REVIEWED = Rule R second reader done. "Certified" only means Arb/ball arithmetic. Names that mean different
things in different places are listed in §6.

Notation: c(p) := ¼(π/(2I(p)))^p, I(p) := (√π/2)Γ(1/p + ½)/Γ(1/p + 1); κ_p := 3p/2 + log c(p); c(2) = π²/16.
σ_{p,s} := Σ_k k^{−s}δ_{k^{−p}}. β_n := n^p b_n/(c(p)C). Φ_n := −2n²log n + 2Σ_{j<n}(n−j)log L(j) + κn²,
κ = 3 + log(π²/16) (smooth-ζ normalization).
The numerical values of c(p), u_s, κ_p (Paper 1 Table), κ = −0.28946… (RH_ζ) and the identity κ = −2(log c)′(2) are
CERTIFIED (Arb) in `certified/c01_constants.py`; the Lommel closed form (p = s = 2) is CERTIFIED for n < 300 and the
Baricz–Štampach closed forms for n ≤ 30 (`certified/`). No theorem label changes.

---

## 1. Overview and headline results

The repo studies Jacobi coefficients (a_n, b_n) and Hankel determinants D_n of σ = Σ w_kδ_{x_k}, x_k ↓ 0. "Law P" is
b_n/x_n → c(p) (and a_n ~ 2b_n) for x_k ~ Ck^{−p}. The averaged (n²) law is proved for every p > 0 by identifying the
n² constant as a constrained logarithmic equilibrium (G2). The pointwise law with an O(1/n) rate is proved for every
pure power σ_{p,s} (p > 0, s > 1); for the smooth-ζ model the pointwise law is proved with a κ/log n correction,
b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log²n)) (only b_N/(β_N/4) and a_N/(2b_N) are 1 + O(1/N)). Both come from
Riemann–Hilbert analyses that perturb cited constructions (G1/RH). The pure-power laws are transported to weights k^{−s}Ψ with Ψ slowly varying. For fixed-size
roughness of the weights the pointwise law can fail (G1). For the true ζ-zero measure (G3′) the averaged law holds up to
O(n²) with no hypothesis on the zeros (mod (C1), (C5), Theorem H). It holds exactly iff a capped near-pair energy of the ordinates is
o(K²), and it holds under several stated pair-correlation / prime-variance hypotheses. Lean formalizes the reduction
Theorem H ⇒ Theorem H_L / Corollary H_L-ζ with Theorem H as a named input.

**H1. Theorem H_all (averaged Law P, every p > 0).** G2 PROOF.md §3.
"Let p > 0 and C > 0. Let x_k = f(k) with f ∈ C¹[1, ∞), ξ^{p+1}f′(ξ) → −pC, and ξ^{p+1}|f′(ξ)| bounded above and
below … Let the weights satisfy Σ_k w_k < ∞ and w_k ≥ c₁k^{−s}. Then log D_n(Σ_k w_kδ_{x_k}) = −pn²log n +
(3p/2 + log(c(p)C))n² + o(n²). Equivalently, (2/n²)Σ_{j<n}(n−j)log(j^p b_j) → log(c(p)C)."
Label: **PROVED** (Plan 47, 2026-10-14; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED); G2 REVIEWED (pre-Plan-47 text). No external citation: B*(iii)
now uses **G2 Lemma EP** (a Fourier proof that −∬log|x−y|dνdν ≥ 0 for zero-mass ν with log-integrable |ν|, ported from
Paper 1 Lemma 3.3). *Pre-Plan-47 label (history):* PROVED-mod-cite (P). External input: **(P)** (Beckermann–Kalyagin–Matos–Wielonsky
arXiv:1105.3088v2 Lemma 2.1, itself resting on Saff–Totik I.1.8 and Cegrell–Kolodziej–Levenberg Thm 2.5, *not read*;
accepted under mod-cite (P)). (P) enters only through B*(iii) (E_p = κ_p, optimality/uniqueness). The lower bound A-L is
citation-free. Corollary **HZ**: log det_{1≤i,j≤n}ζ(a(i+j)+b) = −an²log n + (3a/2 + log c(a))n² + o(n²), real a > 0,
2a + b > 1 (PROVED since Plan 47; was PROVED-mod-cite (P); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED). **Corollary H-input** (§3, Plan 37): for every p > 0, s > 1 the Lean named input
`TheoremHPure p κ_p s` holds on paper (C = 1, w_k = k^{−s}); label PROVED, as H_all (Plan 47; was PROVED-mod-cite (P); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED). The `bdd` field
is already the sorry-free Lean theorem `heineK_bdd_of_summable`; only `asymp` is paper-only. (P) is needed only where
G2 is the sole route (outside item 11's Theorem H range: p ∉ {1, 2}, p = 1 with s < 3/2, p = 2 with s < 2). See §3.3.
*(Plan 47: the previous sentence is pre-Plan-47 history; (P) is now needed nowhere.)*

**H2. Pointwise Law P with rate for every pure power (p > 0, s > 1).** G1 §0 rows RH₁(r), RH_p, RH_p 0<p<1 (seam).
For σ_{p,s}: n^p b_n = c(p)(1 + O(1/n)) and a_n/(2b_n) = 1 + O(1/n).
- p = 1, every r > 1: **Theorem RH₁(r)** (RH/RH_p1_general.md). Label: PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4,
  DLMF 5.11) + REVIEWED. (r = 3/2: Theorem RH₁, RH/RH_p1.md, PROVED-mod-cite (WLXZ v1) + REVIEWED.)
- p > 1, s > 1: **Theorem RH_p** (RH/px/RH_px.md). Label: PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6; G2 μ*, B*(i)–(ii),
  citation-free) + REVIEWED.
- 0 < p < 1, s > 1: **RH_p (seam)** (RH/plt1/RH_plt1b.md). Label: PROVED-mod-cite (WLXZ, KMVV §6 incl. angle freedom,
  G2 μ*/B*, DLMF 5.11) + REVIEWED; no numerical caveat.
External inputs: **WLXZ v1** (arXiv:1410.3948v1), **KMVV** (math/0111252v2 §6), **KV** §5, **Van** (math/0212014 §4),
**DLMF** 5.11 (and 5.5.3). G2's μ*/B*(i)–(ii) are used, which are citation-free (RH_px §2 uses B*(ii) only).

**H3. Theorem RH_ζ (smooth-ζ model, pointwise with rate).** RH/zeta/RH_zeta_close.md §5; G1 §0.
x_j = 1/(γ_j² + ¼), N₀(γ_j) = j − ½, masses 2x_j: "b_n/x_n = (π²/16)(1 + κ/log n + O(log log n/log² n)),
κ = −2(log(π/2) − (1 − log 2)); b_N = (β_N/4)(1+O(1/N)), a_N/(2b_N) = 1+O(1/N)." (κ = −0.28946…)
Label (as in G1 §0): **PROVED-mod-cite (WLXZ v1 §§3–6.1; KMVV §6; C–D Thm 4.4; DLMF; G2 — optimality, for E1(iv) only), REVIEWED.** Lemma Z (far field) is PROVED
with an **Arb-certified** winding computation. External: WLXZ v1, KMVV §6, **C–D** (Conway–Deift arXiv:1711.01590v4
Thm 4.4), DLMF (§§1.14, 5.5, 5.11, 5.12, 10.27, 10.39).

**H4. Weight transport and the dichotomy for weights k^{−s}Ψ (pure-power nodes).** G1 §§3.1–3.9.
- **T3-all** (§3.8): "Let w = k^{−s}Ψ (s > 1) with Ψ bounded and slowly varying (sequence form). Then n^pb_n(w) → c(p)
  and n^pa_n(w) → 2c(p) as n → ∞ (all n, p > 0)." PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺,
  L) + REVIEWED.
- **T3-log** (§3.9, Plan 36): same conclusion for Ψ "log-type slowly varying" (slowly varying, unbounded allowed, and
  D(γ) := sup_{n≥2}max{|log Ψ(k) − log Ψ(n)| : k ∈ [n, n^γ]} < ∞), e.g. (log k)^α, α ∈ ℝ. PROVED-mod-cite (RH_px,
  RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TL(w), L, T3-all) + REVIEWED.
- **Theorem R** (§3.6): for ε ∈ (0, ε₀], ε₀ = η/16, there is f with |f| ≤ ε such that w = k^{−s}e^{f} has
  limsup|log(β_n²/β_{n−1}²)| ≥ εη/2; so (T3) and the pointwise b-law fail (all p > 0, s > 1). PROVED-mod-cite (RH_px,
  RH₁(r), RH_plt1b; internal FV, Sat_p⁺, TL, §3.5 two-point formula) + REVIEWED. η, J non-explicit.
- **Theorem CL / Cor. A4′** (§3.1): x_k = k^{−p}, p > 1, Σw < ∞, w_k ≥ c₁k^{−s} (rough weights allowed):
  n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p − 1). PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii)) + REVIEWED (proof
  unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED.
External inputs: those of H2 (transitively). *(Pre-Plan-47: "plus (P) for CL/TC/T3-avg only. T3-all and T3-log do
**not** use (P)." Since Plan 47, CL, A4′ and TC use no external citation, and T3-avg only those of H2.)*

**H5. G3′ (true ζ-zero measure, σ = Σ 2x_kδ_{x_k}, x_k = 1/(γ_k² + ¼), ordinates with multiplicity).** G3′ PROOF.md.
- **G3′-U** (§3): limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0. PROVED-mod-cite + mod-input Theorem H (Lean `TheoremHPure`) +
  REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)). Inputs: (C1) via Z1/Z2; Theorem H (p = 2, via item 11 H7).
- **Theorem B** (§8.1): liminf ≥ −3 log C > −∞, so log D_n = Φ_n + O(n²) with no hypothesis on the zeros.
  PROVED-mod-cite (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)). C not explicit.
- **Theorem Ch** (§5.4): G3′ ⟺ 𝒞(K) = o(K²), 𝒞(K) := min_{T⊂[k₂,K]}[P(T) + K·|[k₂,K]∖T|] (capped near-pair energy).
  PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)).
- Conditional closures of G3′ (each ⇒ (SG) ⇒ G3′): **Theorem C** (PCC in GLSS form, no RH), **Theorem S** (SPC_ℂ⁺, no
  RH), **Theorem S′** (SPC_ℂ⁺(full)), **Theorem V⁺** (RH + (V⁺)), **Corollary P** (RH + (V)). Necessity: **N″**
  (G3′ ⇒ d(E) = 0) and **N‴** (G3′ ⇒ d(T_β) = 0 ∀β > 0). All carry the Theorem H note in G3′ §0 (§2.5 below).
External inputs: **(C1)** Trudgian arXiv:1208.5846v2 Cor. 1; **(C5)** GLSS arXiv:2503.15449v4 (6.1); **(C3)** BGST
arXiv:2501.14545v3; **(C6)** Lamzouri arXiv:2609.02882v2; **(C8)** Goldston arXiv:math/0412313; named input **Theorem H
(p = 2, s ≥ 2)**, supplied citation-free by item 11 Theorem H (p = 2, PROVED + REVIEWED there) and also by G2 Cor.
H-input (PROVED since Plan 47; was mod-cite (P)); no G3′ result depends on (P) — §3.3.

**H6. Lean (sorry-free; `lean/check.sh` re-run on the Plan 37 branch 2026-10-14: AUDIT OK, only propext, Classical.choice, Quot.sound).**
`theoremHL` (Theorem H_L): **PROVED-mod-input (TheoremHPure; input supplied on paper for all p > 0, s > 1 by G2 Cor.
H-input, PROVED since Plan 47 (was mod-cite (P)); item 11 alone gave p ∈ {1,2}, s ≥ s0(p))**. `smoothZeta_HL`, `smoothZeta_HL_det` (Corollary
H_L-ζ) and `smoothZeta_bLaw` ((2/n²)Σ(n−j)log(b_j/x_j) → log(π²/16)): **PROVED-mod-input (TheoremHPure 2 κ 2,
κ = 3 + log(π²/16))**. Unconditional Lean results: `heineK_eq_det`, `heineD_eq_det` (Andreief/Heine), `hankel_det_eq_prod`
(H2), `opoly_recurrence`, `lemmaP` (α ≥ 2β), `toeplitz_count` ((S4): |N(T_ℓ(A,B); μ) − (ℓ/π)θ| ≤ 1, B ≥ 0),
`det_mul_cauchyBinet`. Named input: `TheoremHPure p κ s` (Inputs.lean: bounded in K and log D_n = −pn²log n + κn² +
o(n²) for atoms (k+1)^{−p}, weights (k+1)^{−s}). Lean labels stay PROVED-mod-input: Theorem H_all is not formalized.

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
| **`theoremHL`** | Theorem H_L (slowly varying atoms) | **PROVED-mod-input (TheoremHPure; input supplied on paper for all p > 0, s > 1 by G2 Cor. H-input, PROVED since Plan 47 (was mod-cite (P)); item 11 alone gave p ∈ {1,2}, s ≥ s0(p))** | TheoremHL.lean | TheoremHPure (two instances: s and s0) |
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
| `chain_limit_core`, `chain_limit` | U_n + V_n → 2c, U_nV_{n+1} → c², U, V > 0 ⇒ U_n, V_n → c (Paper 2 Lemma `lem:chain-limit`; G1 §3.21 Lemma CS) | sorry-free (Plan 56) | ChainLimit.lean | — |
| **`christoffel_sign`**, `opoly_eval_zero` | x_k ≥ 0: P_n(0) = (−1)ⁿD_n(xσ)/D_n(σ), (−1)ⁿP_n(0) > 0 (Paper 2 Lemma `lem:zeros`, sign part) | sorry-free (Plan 56) | Christoffel.lean | hankel_det_pos |
| **`christoffel_transfer`**, `christoffel_poly`, `christoffel_ja_split`, `christoffel_jb2_split` | a_n = u_n + l_n, b_{n+1}² = u_nl_{n+1}; XP̃_n = P_{n+1} + u_nP_n; ã_n = u_n + l_{n+1}, b̃_{n+1}² = u_{n+1}l_{n+1} (Paper 2 Lemma `lem:transfer`) | sorry-free (Plan 56) | Christoffel.lean | opoly_recurrence, eq_zero_of_orth |
| **`christoffel_shift_law(_converse, _pow)`** | s_na_n → 2c, s_nb_n → c for σ ⇔ for xσ (s_n/s_{n+1} → 1; `_pow`: s_n = n^p) (Paper 2 Thm `thm:shift` no rate, Remark `rem:converse`; G1 §3.21 SH, §3.19 CT₁ "⟸") | sorry-free (Plan 56) | Christoffel.lean | chain_limit_core |
| **`chain_rate_core`** | regular η: O(η) inputs ⇒ U_n − c = O(√η_n), U_{n+1} − U_n = O(η_n) (Paper 2 Lemma `lem:chain-rate`; G1 §3.21 CS-r) | sorry-free (Plan 56) | ChainRate.lean | chain_limit_core |
| **`christoffel_shift_rate(_pow)`** | s_na_n − 2c, s_nb_n − c = O(η_n) for σ ⇒ the same for xσ (`_pow`: s_n = n^p) (Paper 2 Thm `thm:shift`, rate; G1 §3.21 SH-r) | sorry-free (Plan 56) | ChristoffelRate.lean | chain_rate_core, christoffel_transfer |
| `hallLam`, `hallC`, `hallKappa`, `four_hallC_rpow` | Λ(p) = ∫₀¹ arccos(2s^p − 1), c(p) = (π/Λ)^p/4, κ_p = 3p/2 + log c(p) (Paper 1 (1.2); Λ = 2I(p) not yet formalized) | (definitions) sorry-free (Plan 60) | HallConst.lean | — |
| `arcsine_pot`, `arcsine_pot_ge` | ∫₀^π log\|β(1−cos φ)/2 − y\| dφ = π log(β/4) (0 ≤ y ≤ β), ≥ for y ≥ β (Paper 1 Lemma 3.2; G2 B0) | sorry-free (Plan 60) | Arcsine.lean | Mathlib `integral_log_sin_zero_pi` |
| `muStar`, `muStar_Ioc_le`, `muStar_Ioc_eq` | μ\*_u admissible: μ\*_u(a,b] ≤ b − a, = on (0, Λ/π] (Paper 1 Thm 1.3(i); G2 B\*(i)) | sorry-free (Plan 60) | Equilibrium.lean | — |
| **`muStar_energy`** | 𝒥_p(μ\*_u) = κ_p, absolutely convergent (Paper 1 Thm 1.3(iii), value) | sorry-free (Plan 60) | StarEnergy.lean | arcsine_pot |
| **`quantile_lower`**, `quantile_sum_ge` | admissible θ on (0,U], F integrable: eventually n²(𝒥(θ) − η) ≤ 2Σ_{i<j}F(u_i,u_j) (Paper 1 Thm 5.2 Steps 2–3) | sorry-free (Plan 60) | QuantileLower.lean | — |
| `Jp_scaleM`, `exists_good_theta` | scaling (Paper 1 Lemma 3.1); admissible θ with 𝒥 ≥ κ_p − η (Thm 5.2 Step 1) | sorry-free (Plan 60) | HallLower.lean | muStar_energy |
| **`hall_lower`** | p > 0, s > 1: ∀η > 0 eventually hnorm p κ_p (heineD (powSeq p) (powSeq s)) 0 n ≥ −η (Paper 1 Thm 5.2 = G2 A-L, pure powers) | **sorry-free (Plan 60)** — the lower half of `TheoremHPure p κ_p s` | HallLower.lean | quantile_lower, exists_good_theta |
| **`energy_pos`**, `gauss_pd`, `frK_integral` | 𝓛(A,A) + 𝓛(B,B) ≤ 2𝓛(A,B) for finite A, B of equal mass (Paper 1 Lemma 3.3 inequality; G2 Lemma EP), via Frullani + Gaussian kernel | sorry-free (Plan 60) | EnergyPos.lean | Mathlib `Frullani.integral_Ioi_eq` |
| `starPot_eq`, `starPot_ge`, `le_volume_of_lip` | U\* = log c + p on [0,4c], ≥ on [0,∞) (Paper 1 Thm 1.3(ii)) | sorry-free (Plan 60) | Optimality.lean | arcsine_pot |
| **`Jp_le_kappa`** | admissible μ on (0,U], F_p integrable ⇒ 𝒥_p(μ) ≤ κ_p (Paper 1 Thm 1.3(iii) optimality; G2 B\*(iii)) | sorry-free (Plan 60) | Optimality.lean | energy_pos, starPot_compare, muStar_energy |
| **`disc_upper`**, `Fp_integrable_box`, `far_cell`, `any_cell` | 2Σ_{a<b}F(u_a,u_b) ≤ n²𝒥(μ̄_S) + \|S\|·eDisc (Paper 1 Lemma 4.1; G2 A1) | sorry-free (Plan 60) | Discretize.lean | — |
| **`head_V_bound`**, `muBar_energy_le` | log V(S) ≤ −pN² log N + κ_pN² + pN log n + N·eDisc (Paper 1 Cor 4.2; G2 A2) | sorry-free (Plan 60) | HallUpper.lean | disc_upper, Jp_scaleM, Jp_le_kappa |
| **`hall_upper`** | p > 0, s > 1: ∀η > 0 eventually hnorm p κ_p (heineD (powSeq p) (powSeq s)) 0 n ≤ η (Paper 1 Thm 4.3 = G2 A-U, pure powers) | **sorry-free (Plan 60)** | HallUpper.lean | head_V_bound, heineK_tail_split, phi_bound |
| **`theoremHPure_all`** | `TheoremHPure p (hallKappa p) s` for all p > 0, s > 1 (Paper 1 Thm 1.1 pure powers; G2 Cor H-input) | **sorry-free (Plan 60)** — named input discharged, κ in Λ(p) form | TheoremHall.lean | hall_lower, hall_upper |
| **`theoremHL_all`** | Theorem H_L with no named input, κ = hallKappa p | **sorry-free (Plan 60)** | TheoremHall.lean | theoremHL, theoremHPure_all |
| **`hallLam_eq_gamma`**, `hallKappa_eq`, `hallKappa_one`, `hallKappa_two` | Λ(p) = √π Γ(1/p+1/2)/Γ(1/p+1) = 2I(p); Lean κ = Paper 1's κ_p; κ₁ = 3/2 − log 2, κ₂ = 3 + log(π²/16) | sorry-free (Plan 60) | HallGamma.lean | Mathlib beta distribution |
| **`theoremHPure_kappa`**, `theoremHPure_two` | `TheoremHPure p κ_p s`, κ_p = 3p/2 + log(¼(π/(2I(p)))^p), all p > 0, s > 1 (G2 Cor H-input) | **sorry-free (Plan 60) — the named input is a theorem** | HallCorollaries.lean | theoremHPure_all, hallLam_eq_gamma |
| **`smoothZeta_HL_uncond`, `smoothZeta_HL_det_uncond`, `smoothZeta_bLaw_uncond`** | Corollary H_L-ζ (Heine, Hankel-det, b_j forms) with no named input | **sorry-free (Plan 60)** | HallCorollaries.lean | smoothZeta_HL(_det), smoothZeta_bLaw, theoremHPure_two |
| `hall_upper_w`, `hall_lower_w`, **`pure_law_w`** | atoms (k+1)^{−p}, general weights: upper bound for any positive summable w; lower bound for w ≥ c₁(k+1)^{−s}, **any real s** (by weight monotonicity from `hall_lower`) (Paper 1 Thms 4.3, 5.2 as stated) | **sorry-free (Plan 61)** | GenWeights.lean | hall_upper, hall_lower |
| `heineD_scale`, `scaled_law`, `PairRatio`, **`hnorm_transfer`** | D_n(Cy) = C^{n(n−1)} D_n(y) (Lemma 2.2(iii)); regular-spacing comparison (Lemma 2.3): pair-gap ratio → 1 ⇒ same law | **sorry-free (Plan 61)** | Spacing.lean | heineTerm_le_of_pair_le_split |
| **`paper1_thm11`**, `paper1_thm11_heine`, `pairRatio_of_hyp`, `deriv_neg_of_hyp` | **Paper 1 Theorem 1.1 in full**: f ∈ C¹[1,∞) (HasDerivWithinAt on Ici 1, f′ continuous), ξ^{p+1}f′ → −pC, 0 < inf ≤ sup ξ^{p+1}\|f′\| < ∞; w ≥ 0, Σw < ∞, w_k ≥ c₁k^{−s}, any real s ⇒ log det(m_{i+j}) = −pn² log n + (κ_p + log C)n² + o(n²), κ_p in Gamma form; no hypothesis strengthened | **sorry-free (Plan 61)** | GeneralAtoms.lean | pure_law_w, scaled_law, hnorm_transfer, ratio_bounds_of_deriv |
| **`paper1_cor12`** | Paper 1 Corollary 1.2: (2/n²)Σ_{j<n}(n−j) log(j^p b_j) → log(c(p)C), b_j = √(jb2) | **sorry-free (Plan 61)** | Paper1Corollaries.lean | paper1_thm11, hankel_det_eq_prod, sum_log_weighted_asymp |
| **`paper1_cor14`**, `paper1_cor14_one`, `paper1_cor14_two`, `zetaHankel_eq` | Paper 1 Corollary 1.4 (= G2 HZ): log det_{1≤i,j≤n} ζ(a(i+j)+b) = −an² log n + (3a/2 + log c(a))n² + o(n²), real a > 0, 2a + b > 1 (Mathlib `riemannZeta`, real parts); a = 1 (b > −1), a = 2 (b > −3) | **sorry-free (Plan 61)** | Paper1Corollaries.lean | theoremHPure_kappa, heineD_eq_det |

Not formalized: the forward Weyl law (item 11 "Theorem B"; not G3′ Theorem B, see §6), the uniqueness of the maximiser
and the equality case of Lemma 3.3 (Plan 60, lean/HALL_PLAN.md; Theorem H_all for general atoms f(k) is formalized since
Plan 61, `paper1_thm11`, lean/GENF_PLAN.md), everything in
research/ except the Christoffel shift of G1 §3.21 / Paper 2 §3 (Plan 56 rows above; for `DMeasure` σ with atoms x_k ≥ 0 —
no atom at 0, general σ with finite moments not covered; zero location in `lem:zeros` and Remark `rem:sharp` not formalized).

### 2.2 G2 (research/G2/PROOF.md; REVIEWED 2026-10-13)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| B0 | ∫log\|x−y\|dω_{[0,β]} = log(β/4) on [0,β], ≥ on [β,∞) | PROVED | §1 | — |
| EP | energy positivity: ν signed, ν(ℝ) = 0, ∬\|log\|x−y\|\|d\|ν\|d\|ν\| < ∞ ⇒ −∬log\|x−y\|dνdν = ∫_0^∞\|ν̂\|²/ξ dξ ≥ 0, = 0 iff ν = 0 | PROVED (Plan 47; ported from Paper 1 Lemma 3.3, refereed CORRECT); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §1 | — (Fubini, dominated/monotone convergence, Gaussian Fourier transform) |
| B* | E_p := sup_{μ∈𝒜}I(μ) = κ_p, uniquely attained at μ* = ∫_0^1 ω_{[0,4c(p)t^{−p}]}dt | PROVED (Plan 47; was PROVED-mod-cite (P)); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED; the value I(μ*) = κ_p is citation-free | §1 | B0, EP for (iii) optimality (formerly (P)) |
| A1 | discretization: point energy ≤ n²·(smeared energy) + C_M n log n, subsets of [1, Mn] | PROVED | §2 | — |
| A2 (Cor.) | head bound log V(S) ≤ −pN²log N + E_pN² + C′_M n log n | PROVED (uses A1 and the Scaling identity of §0; E_p enters only as the sup, not its value) — label added by Plan 37 | §0, §2 | A1, scaling |
| A-U | limsup (1/n²)[log D_n + pn²log n] ≤ E_p | PROVED (uses A1, B*-scaling; algebra of item 11 H7) | §2 | A1, item 11 H7 |
| A-L | liminf ≥ κ_p (= I(μ*_u)) | PROVED (citation-free: uses B*(i) and the value in B*(iii)) | §2 | B*(i), value of I(μ*) |
| **H_all** | see H1 | PROVED (Plan 47; was PROVED-mod-cite (P)); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED. Lean: sorry-free in full generality (Paper 1 Thm 1.1, `paper1_thm11`, Plan 61) | §3 | A-U, A-L, B*, item 11 H3, H4 |
| HZ | log det ζ(a(i+j)+b) = −an²log n + (3a/2 + log c(a))n² + o(n²), a > 0, 2a+b > 1 | PROVED (Plan 47; was PROVED-mod-cite (P)); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED. Lean: sorry-free (`paper1_cor14`, Plan 61) | §3 | H_all |
| **H-input** (Cor.) | `TheoremHPure p κ_p s` holds on paper for every p > 0, s > 1 (bdd: heineK ≤ (Σ(k+1)^{−s})^n; asymp: H_all with f = ξ^{−p}, C = 1, w = k^{−s}, via `heineD_eq_det`) | PROVED, as H_all (Plan 47; was PROVED-mod-cite (P)); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §3 (before Novelty) | H_all, Lean `heineD_eq_det` |

Prior art recorded: Monien arXiv:0901.1883 (p = 1, heuristic, same optimizer) (M).

### 2.3 G1 — Tauberian reductions, a_n side, weight transport (research/G1/PROOF.md)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| K | second difference of G(n) = Σ(n−j)u_j over ±h = triangle-kernel sum, mass h² | PROVED | §1 | — |
| **G1-T** | H_all + (T3) slow oscillation of β_n ⇒ β_n → 1 | PROVED (Plan 47; was PROVED-mod-cite (G2 (P))); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §2 | H_all, K |
| **G1-L** | H_all + one-sided bound on β_n ⇒ (1/n)Σ_{j<n}log(j^pb_j) → log(c(p)C) | PROVED (Plan 47; was PROVED-mod-cite (G2 (P))); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §2 | H_all |
| A1 | J ≥ 0 ⇒ sine-weighted window averages of a_j ≥ 2cos(π/(L+1))·min b | PROVED | §3 | (S4) / Lean `toeplitz_eigen` |
| A2 | p > 1: Σ_{j>n}a_j = 𝔼_n[Σ_{k∉S}x_k] (Heine ensemble) | PROVED | §3 | — |
| A3 | Q_p := ∫x d(σ − μ*) = 2c(p)/(p−1) | PROVED (uses only G2 B*(i) and the definition of μ*, both citation-free) | §3 | G2 B*(i) |
| A4 | (CL) ⇒ tail-Cesàro a-law; with β_n → 1, block ratios → 1, window averages → 1 in b-weighted density | CONDITIONAL on (CL) … tail-Cesàro part unconditional for pure powers via CL; (i)–(ii) still need β_n → 1 | §3 | A2, A3, (CL) |
| Sat_p | 1 − ρ_n(k) ≤ (W/w_k)e^{−2n g_p(θ)}, θ = k/n, p ≥ 1 | PROVED (§3.1 header); REVIEWED | §0, §3.1 | G3′ §5.2 Lemma Sat |
| WC | concentration at speed n² of ν_S to μ*_u | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii)); REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §0, §3.1 | G2 A1, A-U, A-L, B*(iii) |
| **CL** | x_k = k^{−p}, p > 1, rough weights: n^{p−1}𝔼_n[Σ_{k∉S}x_k] → Q_p | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii); internal: G2 A1, A-U, A-L; G3′ §5.2 Lemma Sat); REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED; novelty UNCHECKED | §3.1 | Sat_p, WC, A3 |
| A4′ | unconditional tail-Cesàro a-law n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p−1), p > 1, rough weights | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii)); REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §0, §3.1 | A2, CL |
| FV | d/dt log b_n²(ve^{tf}) = ⟨f, μ_n − μ_{n−1}⟩ | PROVED (standard; novelty not claimed); REVIEWED | §3.2 | — |
| Conj R | (T3) fails for some e^{−ε}k^{−2} ≤ w_k ≤ e^{ε}k^{−2} on windows [0.6N, 1.6N] | Proved in modified form as Theorem R (§3.6) … The [0.6N, 1.6N]-window form remains NUMERICAL | §3.2 | — |
| Sat_p⁺ | Sat_p for all p > 0 with factor ((n+1)/k)^{2(1−p)₊}, g_p⁺ | no separate label in the §3.3 header (which labels T3-conv); the proof is that of Lemma Sat_p (PROVED) with two elementary changes; Rule R (review/REVIEW_Plan29.md) ACCEPT WITH FIXES, F1 applied — REVIEWED | §0, §3.3 | Sat_p |
| **T3-conv** | ψ_k → L ∈ (0,∞): n^pb_n → c(p) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺); REVIEWED; novelty UNCHECKED — **SUPERSEDED by T3-all** | §3.3 | FV, Sat_p⁺, H2 |
| TL | sandwiched weights: μ_n((T,∞)) ≤ ε for T ≥ A n^κ ε^{−1/(s−1)}, κ = (2+2/p)s/(s−1) | PROVED (textbook-standard Markov/Chebyshev inequalities, quoted); REVIEWED; novelty UNCHECKED | §3.4 | Markov, Chebyshev (not checked against a source) |
| **T3-sv** | Ψ bounded, polynomially slowly varying: n^pb_n → c(p) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺, TL); REVIEWED — **SUPERSEDED by T3-all** | §3.4 | FV, Sat_p⁺, TL, H2 |
| FVa | d/dt a_n = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩ | PROVED (standard; novelty not claimed; self-contained via the proof of Lemma H and Christoffel–Darboux); REVIEWED | §3.5 | G3′ Lemma H proof |
| **T3a** | under T3-sv hypotheses, n^pa_n → 2c(p) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FVa, Sat_p⁺, TL); REVIEWED — **SUPERSEDED by T3-all** | §3.5 | FVa, Sat_p⁺, TL, H2 |
| R2 | \|d²F_N/dt²\| ≤ 16‖f‖²_∞ | PROVED | §3.6 | §3.5 two-point formula |
| R1 | pure power: ∃η, J: every [N−J, N] has m with ‖Δ²μ_m‖₁ ≥ η | PROVED-mod-cite | §3.6 | H2 (pure-power ratio asymptotics) |
| **Thm R** | see H4 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺, TL, §3.5 two-point formula); … REVIEWED; novelty UNCHECKED. Sub-labels: R2 PROVED; R1 PROVED-mod-cite | §3.6 | R1, R2, FV, Sat_p⁺, TL |
| TC | 𝔼_m#(S ∩ (Mm,∞)) ≤ (2A/(p log M))m + o(1), sandwiched weights | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii); internal: G2 A1/A2, A-U, A-L) + … REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED | §3.7 | G2 A-U, A-L, B*(iii) |
| **T3-avg** | Ψ bounded, uniformly slowly varying: full pointwise law on a density-one set of n | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) (Plan 47: "(P) via TC" dropped; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED) + … REVIEWED — **SUPERSEDED by T3-all** (all n) | §3.7 | FV, FVa, Sat_p⁺, TC |
| TV | (d/dt)μ_m(A) = ⟨f1_Aq_m,q_m⟩ − 2⟨1_Aq_m, K_m(fq_m)⟩ − ⟨fq_m,q_m⟩μ_m(A) | PROVED (standard; novelty not claimed) + … REVIEWED | §3.8 | — |
| LP | pure power: μ_n((Mn,∞)) → F_p(M) = (2/π)arcsin√(min(1, M^{−p}/(4c(p)))) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; textbook method of moments) + … REVIEWED; novelty not claimed | §3.8 | H2 |
| **Thm L** | limsup sup_t μ_m^{(t)}((Mn,∞)) ≤ e^{4G}F_p(M), Ψ bounded slowly varying | PROVED-mod-cite (as LP; internal TV, Sat_p⁺) + … REVIEWED; novelty UNCHECKED | §3.8 | TV, LP, Sat_p⁺ |
| **T3-all** | see H4 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, L) + … REVIEWED; novelty UNCHECKED | §3.8 | FV, FVa, Sat_p⁺, L |
| TLw | ρ_{n+1}^u(k) ≤ 1156·u_k/min_{T′≤j≤T″}u_j, any summable u > 0 | PROVED (§3.9 header) | §3.9 | TL proof |
| **T3-log** | see H4 | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TL(w), L, T3-all) + … REVIEWED; novelty UNCHECKED | §3.9 | T3-all, TLw |
| G1-R | (T3) from atoms alone; (CL) | (T3) half **REFUTED** for sandwiched weights (Theorem R, §3.6); PROVED-mod-cite for pure-power nodes with slowly varying Ψ: bounded Ψ (Theorem T3-all, §3.8; contains T3-conv, T3-sv/T3a, T3-avg) and log-type Ψ (Theorem T3-log, §3.9); open for slowly varying Ψ with D(γ) = ∞ and for nodes other than pure powers. (CL) half: proved for pure powers k^{−p}, p > 1 (Theorem CL); open for general nodes or p ≤ 1 (see §4) | §0 (updated by Plan 37), §4 | — |

### 2.4 G1 — pointwise laws by Riemann–Hilbert (research/G1/RH/)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| Theorem RH (p = 2) | n²b_n = c(2)(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n), any r > 1 | **DRAFT — NOT a proof**; "The PROVED-mod-cite label below is withdrawn; the status is PROOF SKETCH" — SUPERSEDED by RH_p (p = 2 > 1); both files now carry a "Superseded (Plan 37)" note | RH/RH_proof.md §0; RH/RH.md (PROOF SKETCH) | — |
| **RH₁** | σ = Σk^{−3/2}δ_{1/k}: a_n = a_n^{TC}(1+O(1/n)), b_n = b_n^{TC}(1+O(1/n)); nb_n = ½(1+O(1/n)) | PROVED-mod-cite (WLXZ v1 §§2–6) + REVIEWED — special case r = 3/2 of RH₁(r); sharpened (E_p1 Thm E1.6, elementary): b_n = b_n^{TC}(1 − 1/(24n²) + O(n⁻³)), same for a_n, PROVED-mod-cite (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) | RH/RH_p1.md §0; E_p1.md | WLXZ v1 |
| **RH₁(r)** | σ_r = Σk^{−r}δ_{1/k}, r > 1: Nβ_N = 1 + O(1/N) ⇒ nb_n = ½(1+O(1/n)), a_n/(2b_n) = 1+O(1/n) | PROVED-mod-cite (WLXZ v1, KV §5, Vanlessen §4, DLMF 5.11) + REVIEWED | RH/RH_p1_general.md §0 | WLXZ v1, KV, Van, DLMF |
| **RH_p** | σ_{p,s}, p > 1, s > 1: n^pb_n = c(p)(1+O(1/n)), a_n/(2b_n) = 1+O(1/n) | PROVED-mod-cite (WLXZ v1 §§3–5, §6.1; KMVV §6; G2 PROOF.md μ*, B* — only μ* and B*(i)–(ii), which do not use (P)) + REVIEWED | RH/px/RH_px.md | WLXZ v1, KMVV, G2 B*(i)–(ii) |
| RH_p, ½<p<1 | same, ½ < p < 1 | PROVED-mod-cite (+ DLMF 5.5.3, 5.11) mod NUMERICAL no-winding (F4) + REVIEWED — **SUPERSEDED by seam** (file header) | RH/plt1/RH_plt1.md | RH_px |
| **RH_p, 0<p<1 (seam)** | same, all 0 < p < 1, s > 1 | PROVED-mod-cite (WLXZ, KMVV §6 incl. angle freedom, G2 μ*/B*, DLMF 5.11) + REVIEWED; no numerical caveat | RH/plt1/RH_plt1b.md | RH_px, KMVV angle freedom |
| E1 | finite-N constrained equilibrium / edge equation (generalizing G2 B*) | PROVED-mod-G2 | RH/zeta/RH_zeta.md §1 | G2 |
| E2, E3 | (edge-equation lemmas) | PROVED | RH/zeta/RH_zeta.md | — |
| E4 | — | NUMERICAL (convention-dependent) | RH/zeta/RH_zeta.md | — |
| Lemma Z | far field | PROVED, with an Arb-certified winding | RH/zeta/RH_zeta_close.md §2 | Arb |
| hard edge (§1), uniform edges (§3), rate (§4) | — | §1 PROVED-mod-cite (KMVV §6; C–D Thm 4.4; DLMF); §3 PROVED-mod-cite (WLXZ §6.1); §4 PROVED | RH/zeta/RH_zeta_close.md | — |
| **RH_ζ** | see H3 | PROVED-mod-cite (WLXZ v1 §§3–6.1; KMVV §6; C–D Thm 4.4; DLMF; G2 — optimality, for E1(iv) only, which RH_zeta.md §1 says is not needed for the RH analysis), REVIEWED | label as in G1 §0 (Plan 37 annotation); RH/zeta/RH_zeta_close.md §5 (its header "(…; DLMF; G2)" now carries the same annotation as a dated note) | E1–E3, Z, §§1–4 |

### 2.5 G3′ (research/G3prime/PROOF.md §0 and rhfree/)

| Name | Statement | Label | Location | Depends on |
|---|---|---|---|---|
| Z1 | \|γ_k − γ̃_k\| ≤ C₀ (k ≥ k₁), ≤ C₀′ all k; C₀ ≤ 2.7 | PROVED-mod-cite + REVIEWED | §2 | (C1) |
| Z2 | pair ratio bound (x_a−x_b)/(x̃_a−x̃_b) ≤ … | PROVED-mod-cite + REVIEWED | §3 | Z1 |
| **G3′-U** | limsup (1/n²)[log D_n(σ) − Φ_n] ≤ 0 | PROVED-mod-cite + mod-input Theorem H (Lean `TheoremHPure`) + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §3 | Z2, item 11 H5/H6/H7, Theorem H (p = 2) |
| S | index shift π(a)⁻² − π(b)⁻² ≥ (1+η)⁻³(a⁻² − b⁻²) | PROVED + REVIEWED | §4 | — |
| W | log D_n(Σk⁻ˢδ_{Ck⁻²}) ≥ Λ_n − (s−3)Kn log n, uniformly in s ≥ 4 | PROVED (from item 11 §7) + REVIEWED | §4 | Theorem A refs, H3 |
| **G3′-L** | liminf ≥ 0 under (SG) | PROVED-mod-cite + mod-input (SG), Theorem H + REVIEWED; uses no Theorem H instance (THEOREMS §3.3) | §4 | Z1, S, W, H5, H6 |
| L′ | (LG*) ⇒ G3′; contains (SG) and "d(E) = 0 + log-gap" | PROVED-mod-cite (C1) + mod-input (LG*), Theorem H; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §4.1 | G3′-L, G3′-U, Tr, K, W |
| Tr | truncation at J ≥ (M/2)n costs O(n²/log M) | PROVED-mod-input Theorem H (via Lemma K / item 11 H7); REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §4.1 | Lemma H, Lemma K |
| N | doubled-smooth sequences (same counting fn.) fail by 2log(1−1/m) | PROVED-mod-input Theorem H + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §5 | Theorem H_L, item 11 H6 |
| N′ | d_*(E) > 0 ⇒ limsup ≤ 2log(1 − d_*(E)) | PROVED-mod-cite + mod-input Theorem H + REVIEWED; residual case closed by N″; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §5 | G3′*-U proof, Z1, Z2, T, H6 |
| **N″** | d̄(E) = η > 0 ⇒ liminf ≤ −0.2397η; hence G3′ ⇒ d(E) = 0 | PROVED-mod-cite (C1) + mod-input Theorem H …; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §5.2 | Hadamard, Christoffel, G3′-U |
| **N‴** | gaps g_k ≤ e^{−βk} at positive upper density ⇒ law fails; G3′ ⇒ d(T_β) = 0 | PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §5.3 | N″, G3′-U, Z1, Z2 |
| **Ch** | G3′ ⟺ 𝒞(K) = o(K²); contains N″, N‴, L′ qualitatively | PROVED-mod-cite (C1) + mod-input Theorem H; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §5.4 | Lemma H, Sat, Tr, K, W, S, Z1, Z2, G3′-U, G3′-L |
| Ch on ζ data | 𝒞(K)/K² ≤ 1.1·10⁻⁷ at K = 2·10⁶ (Odlyzko) | NUMERICAL | §5.5 | — |
| **B** | liminf ≥ −3log C > −∞; log D_n = Φ_n + O(n²) | PROVED-mod-cite (C1), (C5, Fujii's Prop. 2 secondary) + mod-input Theorem H; REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §8.1 | GLSS (6.1), Caro–Wei, §4 proof |
| **C** | PCC (GLSS form, no RH) ⇒ (SG) ⇒ G3′ | PROVED-mod-cite (C1), (C5) + mod-input PCC, Theorem H; REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §8.2 | GLSS, G3′-L |
| P (Corollary P) | RH + (V) ⇒ G3′ | PROVED-mod-cite (C8 Thm 7, C8 SPC⇔(9.3) secondary, C8 Thm 4, C5, C1) + mod-input RH, (V), Theorem H; REVIEWED; novelty UNCHECKED (RH + (V) ⇒ PCC is KNOWN); Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §9.1 | §8.2 |
| Lemma PC | K² sum under SPC_ℂ⁺ | PROVED-mod-cite ((C3) (3.1)–(3.2); (C6) §3 algebra) + mod-input SPC_ℂ⁺; REVIEWED | rhfree/RHFREE.md §1 | (C3), (C6) |
| Lemma G | spectral small-gap lemma (deterministic) | PROVED, REVIEWED | rhfree/RHFREE.md §2 | — |
| **Thm S** | SPC_ℂ⁺ ⇒ 100% simple critical, small gaps ≪ δ³N, (SG) ⇒ G3′ | PROVED-mod-cite ((C3), (C6) (2.4), (C1)) + mod-input SPC_ℂ⁺, Theorem H; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | label as in G3′ §0; proof rhfree/RHFREE.md §3 (header lists (C3) (3.1)–(3.2), (C6) Prop 2.1 (2.4) and §3 algebra, (C1)) | PC, G, G3′-L |
| **Thm S′** | RH + upper half of Montgomery's SPC ⇒ G3′; RH-free: SPC_ℂ⁺(full) ⇒ G3′ | PROVED-mod-cite ((C3) (3.5), (C6), (C1)) + mod-input SPC_ℂ⁺(full), Theorem H; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | label as in G3′ §0; proof rhfree/RHFREE2.md §1 | PC′, G |
| Lemma N (RHFREE2) | inertia bound E ≥ k + 4Σm_z dist(h_z, V)² | PROVED (deterministic); REVIEWED; novelty UNCHECKED | RHFREE2 §2 | — |
| Cor. N1 | Σm_z dist(h_z,V)² ≤ (D·N_T + o(N_T))/4 | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺; REVIEWED | RHFREE2 §2 | PC |
| Prop. Q | SPC_ℂ⁺ + (NA) ⇒ max_{T<γ≤2T}\|β − ½\| → 0 (quasi-RH, not RH) | PROVED-mod-cite (via Lemma PC) + mod-input SPC_ℂ⁺, (NA); REVIEWED; novelty UNCHECKED | RHFREE2 §2 | PC, N, (NA) |
| Lemmas P1, P2, P3 | prime/zero transfer on RH | P1: PROVED-mod-cite (via RH99 …) + mod-input RH, (V⁺); P2: PROVED-mod-cite ((C8) (4.2)–(4.4), (C3) (3.5), (C1)) + mod-input RH; P3: PROVED-mod-cite ((C6) §3 algebra) + mod-input RH, (V⁺); all REVIEWED | rhfree/RHPRIME.md | RH99 |
| Lemmas 9.7*, 9.9* | self-contained (C8) (9.7), (9.9) | PROVED-mod-cite ((C8) Prop. 1 (3.11), (C1) / (C8) (3.4)) + mod-input RH; REVIEWED | rhfree/RH99.md | (C8) |
| **Thm V⁺** | RH + (V⁺) ⇒ (SG) with rate δ³ ⇒ G3′ | PROVED-mod-cite ((C8) Prop. 1 + (3.4) via RH99, (C3) (3.5), (C6), (C1)) + mod-input RH, (V⁺), Theorem H; REVIEWED; novelty UNCHECKED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | label as in G3′ §0; proof rhfree/RHPRIME.md §4 | P1–P3 |
| R, K | pair factors under thinning; concentration (from H7) | PROVED-mod-input Theorem H + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §7 | H5, H7 |
| T | thinning of convergent density: own-normalized law survives | PROVED-mod-input Theorem H + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §7 | R, K, H6, H7 |
| T′ | robustness: density band ±η ⇒ error ω(η) → 0 | PROVED-mod-input Theorem H + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §7 | T |
| G3′*-U | own-normalized upper bound under (D∞) | PROVED-mod-cite + mod-input (D∞), Theorem H + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §7.1 | Z2, T |
| G3′*-L | own-normalized law under (D∞) + (SG*) | PROVED-mod-cite + mod-input (D∞), (SG*), Theorem H + REVIEWED; Theorem H input (p = 2, s ≥ 2) supplied by item 11 Theorem H (PROVED + REVIEWED there), and also by G2 Cor. H-input (PROVED since Plan 47; was mod-cite (P)) | §7.1 | Z1, T′, K |

Hypotheses (not results): (SG), (LG*), PCC (GLSS form), SPC_ℂ⁺, SPC_ℂ⁺(full), (V), (V⁺) (with RH), (NA), (D∞)
"N_d(T)/N(T) → θ ∈ (0, 1]", (SG*).

---

### 2.6 Additions after Plan 37 (Plans 39–44, all REVIEWED 2026-10-14)

Labels abbreviated; the verbatim labels are in the §0 rows of research/G1/PROOF.md (RW, LR / LRa, Ra, RL, B-cond) and
research/G3prime/PROOF.md (Pos). Novelty UNCHECKED unless stated.

| Name | Short statement | Label | Location |
|---|---|---|---|
| Thm RW | Conjecture R in window form: for every window [aN, bN] with b > u_s(p) (incl. [0.6N, 1.6N], all p > 0), explicit η_W, ε₀ = η_W/16; for ε ≤ ε₀ a pointwise-sign f with \|f\| ≤ ε gives limsup (β_n/β_{n−1} − 1) ≥ εη_W/4 (separation → ∞) or εη_W/8 (fixed ratio R_W) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) | G1 §3.10 |
| Lemma LR / LR′ / LRa | linear response with remainder ε² (ratio form 2ε²; a_n form (e^ε − 1 − ε)(b_n + b_{n+1})), ε = ½ osc f, any finite-moment base; constants absolute and numerically sharp; Cor LR-law | PROVED; LR-law PROVED-mod-cite | G1 §3.11 |
| Thm Ra | fixed-size rough weights break the pointwise **a-law**, explicit η_a = c(p)I/2, ε₀ = I/16 (Toda form, R2a, R1a, LP′) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) | G1 §3.12 |
| Lemma RL | for any nodes: s_na_n → α, s_nb_n → β ⟺ moments 1, 2, 4 of ν_n → arcsine moments ⟺ ν_n → arcsine weakly + a priori bound; Law P ⟺ arcsine limit with sup n^p(a_n + b_n) < ∞; RL-n/RL-n2: one index (or two, moments 1,2,4) do not suffice | PROVED (spectral theorem textbook-standard); RL2 PROVED-mod-cite | G1 §3.13 |
| Thm B-cond | pure-power nodes, any slowly varying Ψ (sequence form): unconditional head/bulk/tail bounds; QL ⇒ full pointwise Law P | CONDITIONAL (QL₀, implied by QL) + PROVED-mod-cite; no new case of the law | G1 §3.14 |
| Pos (Plan 43) | d(E) = 0 ⟺ 100% of zeros simple and on the critical line; G3′ ⇒ that (G3′ at least as hard); d̄(E) ≤ 1 − C_Lz ≈ 0.3275 unconditionally (Lamzouri, arXiv preprint); G3′ ⟺ d(E) = 0 ∧ 𝒞_dist = o(K²); G3′ ⇒ HMH not established | PROVED-mod-cite (C1), (C5), (C6) + mod-input Theorem H | G3′ §5.6 |

### 2.7 Additions (Plans 45–49, all REVIEWED 2026-10-14)

| Name | Short statement | Label | Location |
|---|---|---|---|
| **Thm RII / Cor B_{p>1}** | **pointwise Law P (b and a, rate O(1/n) + smoothing error) for x_k = k^{−p}, p > 1, w = k^{−s}Ψ, 1 < s < 1 + 2p, Ψ any slowly varying function (sequence form; incl. D(γ) = ∞, e.g. exp(√log k))**, via Lemma RedA (Gaussian smoothing to an entire L₁) and a Riemann–Hilbert analysis perturbing RH_px with a Conway–Deift comparison at the hard edge; bypasses QL | RedA PROVED; RII, B_{p>1} PROVED-mod-cite (WLXZ v1, KMVV §6, C–D Thm 4.4, DLMF, G2) | G1 §3.17; RH/route2/ROUTE2.md |
| Thm QLP | pure powers, every fixed σ > 1, all M ≥ 1: μ_m((Mn,∞)) ≤ CM^{−p/2} up to the Bessel scale M ≍ n^{2/p}, faster below; QL at t = 0 (log-moment bounded); via a Stieltjes-transform bound in the non-oscillatory RH region | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b, KMVV, Vanlessen, DLMF); uniform in σ CONDITIONAL (RU) (Law P itself is uniform on compacts in σ without (RU): UL.md Thm UP, Plan 64, REVIEWED) | G1 §3.16 |
| QL-CB, BF, RF, FM, DB | commutator lemma CB ⇒ QL ⇒ law (all p); exact boundary-flux identities; free-model computation (log M sharp there); CB itself OPEN (obstruction: hard-edge density/phase along the path) | QL-CB CONDITIONAL (CB) + PROVED-mod-cite; identities PROVED; CB-ob HEURISTIC | G1 §3.18 |
| QL numerics | tilt law at p = 1, ½; QL-b slopes, crossover M ≍ n^{2/p}; commutator ratio ≤ 0.93ε_n(1 + log M) (saturation beyond the hard edge is structural) | NUMERICAL | G1 §3.15 |
| Lemma EP (Plan 47) | energy positivity for zero-mass signed measures (self-contained Fourier proof); removes citation (P): H_all, B*, HZ, Cor H-input, G1-T, G1-L, WC, CL, A4′, TC now PROVED | PROVED | G2 §1 |

*(Plan 55 note, 2026-10-15: in Thm RII / Cor B_{p>1} the rate hypothesis (H_an) — L₁ analytic on |Im u| ≤ π/p — can be weakened to (A_ϑ), analyticity on |Im u| ≤ ϑ for **some** ϑ > 0 (Theorem AS, G1 §3.24: PROVED-mod-cite, Rule R ACCEPT WITH FIXES (review/REVIEW_Plan55.md), fixes applied — REVIEWED). The row above is unchanged.)*



### 2.8 Line B completed (Plans 50–52, 54, all REVIEWED 2026-10-14)

**Pointwise Law P for weights k^{−s}Ψ, Ψ any slowly varying function (sequence form, incl. D(γ) = ∞, e.g. exp(√log k)),
nodes x_k = k^{−p}:** n^pb_n → c(p), n^pa_n → 2c(p), with rate O(1/n) when Ψ satisfies the analyticity hypothesis
(otherwise O(1/n) + smoothing error), in the following ranges:

| Range | Result | Label | Location |
|---|---|---|---|
| p > 1, every s > 1 | RII (1 < s < 1 + 2p) + Christoffel shift SH (s ↦ s + p) = Corollary B_all | PROVED-mod-cite | G1 §3.17, §3.21 |
| 0 < p < 1, every s > 1 | RII_{<1} (seam geometry; strip half-width π/2 suffices) + shift = Corollary B_{p<1} | PROVED-mod-cite | G1 §3.20 |
| p = 1, every non-integer r > 1 | RII₁ (1 < r < 2) + shift = Corollary B_{p=1}⁺ | PROVED-mod-cite | G1 §3.19 |
| p = 1, every r > 1 incl. integer r ≥ 2 | x-frame Route II at p = 1 (RII_x1, 1 < r < 3, incl. r = 2 at α_x = 0) + shift = Corollaries GAP-int (closed), B_{p=1}^{all} — **closes GAP-int** (Plan 54) | PROVED-mod-cite | G1 §3.23 |
| every p > 0, every s > 1 (rate clause) | Plan 55, Theorem AS: the O(1/n) rate needs Ψ = exp L₁(log k) with L₁ analytic only on **some** strip \|Im u\| ≤ ϑ, ϑ > 0 arbitrary (was π/p for p > 1, π/2 for p ≤ 1; (H_an₁)'s π at p = 1); lens angle → 0 by KMVV angle freedom, weight used only in \|arg z\| < ϑ_w ≤ pϑ | PROVED-mod-cite; proof of record papers/paper2 rev. 3 (§§5–7, App. A–D) + G1 §3.24 audit; ROUTE2*.md do not prove AS as written; same external citations; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan55.md), fixes applied — REVIEWED | G1 §3.24; papers/paper2 Remark 5.8 |

Supporting results: Theorem SH (Law P(c) for σ ⇒ for x·σ, any positive σ on [0, ∞) with infinite support, any p > 0;
rates carried by SH-r) PROVED; CT₁ converse (law for x·σ ⇒ for σ) PROVED; Lemma CS PROVED, "very likely KNOWN" (chain
sequences). **With Plan 54 the pointwise Law P holds for every p > 0, every s > 1 and every sequence-form slowly varying Ψ.**
Open: the 1/n coefficient (tilt law, CONJECTURE) and the true ζ-zero measure (barrier).
*(Plan 55 note, 2026-10-15: "the analyticity hypothesis" in the rate clauses above can be taken to be (A_ϑ) for any ϑ > 0 — see the last row and G1 §3.24; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan55.md), fixes applied — REVIEWED.)*

### 2.9 Novelty relabels from the second Rule L pass (2026-10-14; research/program/RESEARCH_PROGRAM.md §6)

Proof labels are unchanged; only novelty status changes.
- **Lemma CS** (§3.21): KNOWN — Dai–Piao–Qiao arXiv:2508.07653 Prop. 2.1 (chain sequences; earlier classical origin
  unconfirmed). **Theorem SH and CT₁'s converse without rates**: a short corollary of that proposition + the classical
  Christoffel formulas; present as such. **SH-r / CS-r (rate transfer)**: NOT FOUND.
- **Lemma GS** (§3.16): KNOWN (Teschl, Jacobi Operators (1.99)–(1.100), (2.122)).
- **Lemma RedA** (§3.17): very likely KNOWN in substance (smooth variation theorem, BGT; Vuilleumier 1976) — novelty not
  claimed; full texts still to be read.
- **Route II technique**: credit Conway–Deift Thm 4.7 explicitly as the mechanism; new: arbitrary slowly varying factor,
  |α| < 1, discrete accumulating nodes.
- **Lemma LR**: first-order part KNOWN (Fischer 1998); sharp ε² bounds NOT FOUND. **Lemma RL**: Simon 2004 Thm 3.2 in
  rescaled form; RL-loc, RL-n/RL-n2 and the a-priori-bound clause NOT FOUND.
- **Headline pointwise law (all slowly varying Ψ), Theorems R/RW/Ra, QLP, B-cond/CB**: NOT FOUND (Knopfmacher–Lubinsky–
  Nevai 1988 still unread; its review indicates a sufficient-condition result).

### 2.10 Plan 62: the 1/n coefficient for pure powers (research/G1/RH/second_order/SECOND.md; REVIEWED 2026-10-15, REVIEW_Plan62.md) and Plan 64: uniformity in s (research/G1/RH/second_order/UL.md; REVIEWED 2026-10-15, REVIEW_Plan64.md) and Plan 65: (E) for p > 1 (research/G1/RH/second_order/E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)) and Plan 66: (E) at p = 1 (research/G1/RH/second_order/E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) and Plan 67: (E) for 0 < p < 1 (research/G1/RH/second_order/E_plt1.md; REVIEWED 2026-10-15)

Pairings: repo a_n = α_{n−1}, so "a_n/(2b_n)" = α_{n−1}/(2b_n) (coefficient e₁ = +p/2); standard/Paper 2 α_n/(2b_n)
(coefficient e₁ˢ = −p/2). (E) = existence of d₁ in n^pb_n/c(p) = 1 + d₁/n + O(n^{−1−ε}).

| Name | Statement | Label | Location |
|---|---|---|---|
| Grid numerics | d₁ = −(s−1)/2, e₁ = p/2, e₁ˢ = −p/2, k₀ = −(s−1) − p/2, k₁ = −(p+2)(2s−2−p)/(2p); maximal fit half-ranges, p ≥ 1 / p = ½ (remainders n^{−1−p}): d₁ 1.6·10⁻⁸ / 1.3·10⁻⁴, e₁ 5.9·10⁻⁹ / 2.5·10⁻⁴, e₁ˢ 1.6·10⁻⁷ / 3.4·10⁻⁴, k₀ 8.3·10⁻⁷ / 6.6·10⁻⁴, k₁ 2.5·10⁻⁶ / 8.1·10⁻⁴ | NUMERICAL | SECOND §1, checks/check_so_grid.out |
| Conjecture P62 | the same for all p > 0, s > 1, remainder O(n^{−1−min(1,p)}) | PROVED-mod-cite for 0 < p < 1 (remainder O(n^{−1−p}) as conjectured; n^{−1−p} coefficient κ_p = 2pc(p)ζ(−p) identified; E_plt1.md Thm E′.1, Cor E′.6) (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md); p = 1: PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀ (E_p1 Thm E1.10) and k₁ at s ∈ {3/2, 5/2} (E_p1 Thm E1.6), k₁ at other s GAP (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); PROVED-mod-cite for p > 1 (E_pgt1.md Thm E.1, Cor E.6) (Plan 65, REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)) | SECOND §1; E_pgt1.md; E_plt1.md |
| Thm 2.3 | p = 2, s ∈ {2,4,6,8,10}: exact rational chains / coefficients; d₁ = −(s−1)/2, e₁ = 1, k₀ = −s, k₁ = −2(s−2), d₂ = (s²+6s−11)/16 | PROVED-mod-cite (VA §3, DLMF-Lommel via Paper 2 Remark rem:pure-lommel) + exact computer algebra | SECOND §2, checks/check_so_exact_p2.out |
| Prop 3.1, Thm 3.2 | Π_{m≤n}(b_m(s+p)/b_m(s))² = g_n/g_0; Σ_{m≤n}log(b_m(s+p)/b_m(s)) + (p/2)log n → ½log(c(p)ζ(s)/ζ(s+p)) | 3.1 PROVED; 3.2 PROVED-mod-cite (Law P; G1 Lemma CS) | SECOND §3.1 |
| Cor 3.3, Thm 3.4 | (E) at s, s+p ⇒ d₁(s+p) = d₁(s) − p/2 and n(G_n − G_{n−1}) → 0; (E_ε), ε > ½ ⇒ e₁ˢ = −p/2, e₁ = p/2 | CONDITIONAL on (E) at s, s+p (Cor 3.3); (E_ε), ε > ½ (Thm 3.4); + PROVED-mod-cite (Law P; Lemma CS); unconditional for p > 1, Thm 3.4 superseded there by E_pgt1 Thm E.1 (Plan 65, REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); unconditional for p = 1, Thm 3.4 superseded there by E_p1 Thm E1.10 (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); unconditional for 0 < p < 1, Thm 3.4 superseded there by E_plt1 Thm E′.1 (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md) | SECOND §3.1 |
| Prop 3.5, Cor 3.6 | weight factors 1 + O(1/k) change Σ_{j≤n}log b_j by a convergent amount; TC anchor: d₁(1, 3/2 + m) = −(1+2m)/4 under (E) | 3.5 PROVED (internal Sat_p⁺); 3.6(i) PROVED-mod-cite (RH_p1 §1, DLMF 5.11); (ii)–(iii) CONDITIONAL on (E) + PROVED-mod-cite, now unconditional, and the −1/24 constant of Remark (b) PROVED-mod-cite (E_p1 Thms E1.6, E1.10) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) | SECOND §3.2 |
| Prop 3.7, Thm 3.8, Cor 3.9 | ∂_s log h_n = −Σ log k·μ_n(k); Cesàro s-slope −½; d₁(p,s) = −(s−1)/2 + g(p), g(1) = g(2) = 0 | 3.7 PROVED; 3.8 PROVED-mod-cite (UL.md Cor UL-3.8: (P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; Lemma CS; with the constant ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) + o(1)); 3.9 CONDITIONAL on (E) only + PROVED-mod-cite (Plan 64 labels, REVIEWED); for p > 1 3.9 unconditional and g(p) = 0 (E_pgt1 §8.2) (Plan 65, REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); for p = 1 3.9 unconditional, g(1) = 0 (E_p1 Thm E1.10) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); for 0 < p < 1 3.9 unconditional, g(p) = 0 (E_plt1 Thm E′.1) (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md) | SECOND §3.3; UL.md §3 |
| Thm 3.10 | log-average d₁ = −(s−1)/2 for p = 2, s ∈ 2+2ℕ₀ and p = 1, s ∈ 3/2+ℕ₀ (⇔ log h_n of the zeta-value Hankel ratios to O(1)) | (a)–(c) PROVED-mod-cite; (d) every s > 1 for p ∈ {1, 2} (convergent remainder) and (c) for all real shifts: PROVED-mod-cite (UL.md Cor UL-3.10: UF-lim; SECOND §2 Input (VA, DLMF-Lommel); Cor 3.6(i) (RH_p1 §1, DLMF 5.11); Plan 64, REVIEWED); every 0 < p < 1, s > 1: log-average coefficient −(s−1)/2 with O(1), PROVED-mod-cite (sum of E_plt1 Thm E′.1) (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md) | SECOND §3.4; UL.md §3 |
| UF-lim (Plan 64) | h_n(s)/h_n(s₀) = c(p)^{(s−s₀)/p}n^{−(s−s₀)}(1 + o(1)), uniformly for s, s₀ in compacts of (1, ∞), every p > 0 (via a minimum/duality sandwich, Lemma V) | PROVED-mod-cite ((P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; Lemma CS); Lemma V PROVED | UL.md §§1–2 |
| UP (Plan 64) | Law P uniform on compacts in s: sup_K\|n^pb_n − c\|, \|n^pg_n − c\|, \|n^pα_n − 2c\| → 0 (removes the (RU) dependence of SECOND's (UΛ)-status α-part, review F10) | PROVED-mod-cite (Thm UF-lim, hence (P), (LP), (QLP-c) at fixed points; Lemma CT) | UL.md §3 |
| UΛ (Plan 64) | sup_{s∈K}\|Λ_n(s)\| = o(log n); Λ_n → −(log c)/p pointwise and in L¹(K) | PROVED-mod-cite (Thm UP, Lemma LP's method, Lemma TL; Lemma W, Scheffé); sup_K\|Λ_n\| = O(1) GAP (⇐ (RU) at PROOF SKETCH level, ⇐ (SCVX), ⇐ (CVX)) | UL.md §4 |
| SV, CVX (Plan 64) | ∂_s²log h_n = Σ_{j>n}f_{nj}² − Σ_{i<n}f_{in}²; (CVX) fails at the top level of finite truncations | SV PROVED; CVX-fin PROVED; (CVX) for σ_{p,s} HYPOTHESIS, NUMERICAL | UL.md §5 |
| (E), g(p) | existence of d₁; its s-independent part for p ∉ {1, 2} | (E): PROVED-mod-cite for p > 1 (E_pgt1.md: second-order RH; Lemma E.2, H_n flat to O(n^{−p})) (Plan 65, REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)), PROVED-mod-cite for p = 1 (E_p1.md Thm E1.10) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md), PROVED-mod-cite for 0 < p < 1 with ε = p, sharp (E_plt1.md Thm E′.1; Lemma F.1, seam H_n flat only to O(n^{−p}) with explicit linear part) (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md) — so (E) holds for every p > 0; g(p) = 0 for p > 1 PROVED-mod-cite (Plan 65, REVIEWED), g(1) = 0 (Plan 66, REVIEWED), g(p) = 0 for 0 < p < 1 PROVED-mod-cite (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md) | SECOND §4; E_pgt1.md; E_p1.md; E_plt1.md |
| Thm E.1, Cor E.6 (Plan 65) | p > 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)), n^pα_n = 2c(1 − (s−1+p)/(2n) + O(n⁻²)), α_n/(2b_n) = 1 − p/(2n) + O(n⁻²); n^pg_{n−1} = c(1 + a/n + O(n⁻²)), k₀ = −(s−1) − p/2, k₁ = −(p+2)a, a = (2s−2−p)/(2p) | PROVED-mod-cite (RH_px; Paper 2 Lemmas binetcut/szego/airy, Frame Prop.; KMVV §6; DLMF 9.7.2, 9.7.5–6, 10.17, 10.25.2, 10.40.1–4) + exact computer algebra (Plan 65, REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)) | research/G1/RH/second_order/E_pgt1.md, checks/check_e_*.out |
| Thm E1.6, E1.10 (Plan 66) | p = 1, every s > 1: nb_n = ½(1 − (s−1)/(2n) + O(n⁻²)), nα_n = 1 − s/(2n) + O(n⁻²), α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²), Nβ_N = 1 + (½ − s + κ₁(−1)^N)/N + O(N⁻²); s = 3/2, 5/2: b_n, α_n, g_n, h̃_n = TC resp. x·TC values × (1 − 1/(24n²) + O(n⁻³)) | E1.10: PROVED-mod-cite (RH₁(r); WLXZ v1 (6.8), (6.10)–(6.21), (6.34)–(6.37); KV (5.23), (5.26)–(5.30); Vanlessen (4.26)–(4.33), (4.43)–(4.52); DLMF 5.11, 9.7.5–6, 10.17.5–6, 10.40.1–2; UL Cor UL-3.10); E1.6: PROVED-mod-cite (WLXZ v1 (1.4)–(1.9); DLMF 5.5.1, 5.11) + exact computer algebra (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) | research/G1/RH/second_order/E_p1.md, checks/check_e1_*.out |
| Thm E′.1, Cor E′.6, Lemma F.1 (Plan 67) | 0 < p < 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), n^pα_n = 2c(1 − (s−1+p)/(2n) + κ_pn^{−1−p} + O(·)), κ_p = 2pc(p)ζ(−p); α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−2p} + n^{−2}); n^pg_{n−1} = c(1 + a/n + κ_pn^{−1−p} + O(·)); k₀ = −(s−1) − p/2, k₁ = −(p+2)a, chain N^{−1−p} coefficient 2^{1+p}κ_p; seam band factor log H_n(z) − log H_n(1) ~ −2Σ_kζ(−kp)(z^k−1)/(kn^{kp}) | PROVED-mod-cite (RH_plt1b; RH_px §5; Paper 2 Lemmas seam/corner/szego/airy/invariance, Frame Prop.; E_pgt1 Lemmas E.3–E.5; KMVV §6 incl. angle freedom; DLMF 5.2.1, 25.2.1, 25.4.1, 9.7.2, 9.7.5–6, 10.17, 10.25.2, 10.40.1–4) + exact computer algebra (Plan 67, E_plt1.md; REVIEWED 2026-10-15, REVIEW_Plan67_A.md, REVIEW_Plan67_B.md) | research/G1/RH/second_order/E_plt1.md, checks/check_e_plt1_*.out |
| Thm TS, Lemma TS (Plan 69) | telescoping with Thm 3.2: the Cesàro s-law (Cor UL-3.8) for every p > 0 and all s₀, s₁ > 1 with the tail bound used only in the window 1 < s < 1 + 2p; uniform on window compacts (all p) | PROVED-mod-cite (UF-lim restricted to the window; Cor TB-C; SECOND Thm 3.2); Plan 69, REVIEWED (REVIEW_Plan69.md ACCEPT WITH FIXES, fixes applied) | research/G1/RH/second_order/TAIL.md §2, checks/check_tail.out |
| Prop UP-w (Plan 69) | uniform b-law on window compacts; uniform a-law on window compacts avoiding s = 1 + p; sup n^pα_n bounded on every window compact | PROVED-mod-cite; GAP UP-1+p: uniform a-*limit* near 1 + p for p ≤ 1 (limit only); Plan 69, REVIEWED | TAIL.md §2 |
| Prop TB-Q, TB-A, Cor TB-C (Plan 69) | Paper 2's comparison frame, p > 0, 1 < s < 1 + 2p: μ_m((Mn, ∞)) ≤ CM^{−p/2} for M ≤ c₁n^{2/p}; ≤ CM^{−ϑ_*} for all M, ϑ_* = (s−1)/(s(1+2/p)+2) | PROVED-mod-cite (Paper 2 §§5–7, App. A–D; C–D Thm 4.4 via T3(b); TC: + Lemma TL); GAP TB-opt (optimal exponent below the Bessel scale in II's frame, p ≤ 1); Plan 69, REVIEWED | TAIL.md §3 |
| Prop TB-P (Plan 69) | p > 1, every s > 1: QLP (a)–(c) | PROVED-mod-cite (= G1 §3.16 Thm QLP for p > 1, REVIEWED); Q-frame dictionary = presentation note; Plan 69, REVIEWED | TAIL.md §3.5 |

Novelty UNCHECKED (Prop 3.1 classical, not claimed; UL.md Lemma V and Prop SV elementary, not claimed).

## 3. Dependency summary

### 3.1 External citations → results

| Input | Source (CITATIONS file) | Enters |
|---|---|---|
| (P) Beckermann–Kalyagin–Matos–Wielonsky Lemma 2.1 (+ unread Saff–Totik I.1.8, Cegrell–Kolodziej–Levenberg 2.5) | G2/CITATIONS.md | **Nothing since Plan 47** (2026-10-14): G2 B*(iii) now uses G2 Lemma EP; (P) is kept only as an alternative route (G2 PROOF.md remark after B*). *Pre-Plan-47:* G2 B*(iii) ⇒ H_all, HZ; G1-T, G1-L; WC, CL, A4′; TC ⇒ T3-avg. **Not** in RH₁(r), RH_p, seam, T3-conv/sv/a, Thm R, L, T3-all, T3-log. (RH_ζ's E1(iv) also invokes (P) via G2's argument; not needed for RH_ζ, unchanged.) |
| WLXZ v1 (arXiv:1410.3948v1) | G1/RH/CITATIONS.md | RH₁, RH₁(r), RH_p, seam, RH_ζ ⇒ (transitively) T3-*, LP, L, Thm R |
| KMVV §6 (math/0111252v2) | G1/RH/CITATIONS.md | RH_p, seam (angle freedom), RH_ζ |
| KV §5; Van §4 (math/0212014) | G1/RH/CITATIONS.md | RH₁(r) |
| DLMF 5.11 (+5.5.3; §§1.14, 5.12, 10.27, 10.39) | G1/RH/CITATIONS.md | RH₁(r), seam, RH_p ½<p<1, RH_ζ |
| C–D Thm 4.4 (arXiv:1711.01590v4) | G1/RH/CITATIONS.md | RH_ζ (log-weight hard edge) |
| Markov, Chebyshev polynomial inequalities | quoted as textbook, not checked against a source | TL ⇒ T3-sv, T3a, Thm R, T3-log (TLw) |
| (C1) Trudgian Cor. 1 | G3prime/CITATIONS.md | Z1, Z2 and every result built on them: G3′-U, G3′-L, N′, N″, N‴, B, L′, Ch, C, P, Thm S, S′, V⁺, P2, G3′*-U, G3′*-L, Lemma P1, Lemma 9.7*. Not: S, W, Prop N, Lemmas R, K, Theorem T, T′, Lemma G, Lemma N, Lemma PC, Cor. N1, Prop. Q, Lemma P3, Lemma 9.9* |
| (C5) GLSS (6.1), Thm 1 | G3prime/CITATIONS.md | B, C, P |
| (C3) BGST (3.1), (3.2), (3.5) | G3prime/CITATIONS.md | PC, S, S′, P2, V⁺ |
| (C6) Lamzouri (2.4), §3 | G3prime/CITATIONS.md | PC, S, S′, P3, V⁺ |
| (C8) Goldston Prop. 1, (3.4), Thms 4, 7 | G3prime/CITATIONS.md | P, RH99, P1, P2, V⁺ |
| item 11 H3, H4, H5, H6, H7, §7 (math-pursuits f5f6aef) | item 11 | H_all (H3, H4), G3′-U/L, N, T, W |
| **Theorem H (named input `TheoremHPure`)** | lean/JacobiAsym/Inputs.lean; supplied on paper by item 11 Theorem H (p ∈ {1, 2}, s ≥ s₀(p); p = 2 citation-free) and by G2 Cor. H-input (all p > 0, s > 1; PROVED since Plan 47, was mod-cite (P)) | theoremHL, Cor. H_L-ζ, smoothZeta_bLaw; every G3′ result labelled "mod-input Theorem H" (all (2, s ≥ 2), item 11 route; §3.3) |

### 3.2 Fully self-contained (PROVED, no external citation, no named input)

G2: B0, A1, Cor. A2, A-U, A-L (A-L is "citation-free"; it uses only B*(i) and the computed value I(μ*) = κ_p).
*Plan 47 (Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED):* also G2 EP, B*, H_all, HZ, Cor. H-input.
G1: K, A1, A2, A3, Sat_p, FV, FVa, TV, R2, TLw (and TL modulo the quoted textbook inequalities).
*Plan 47 (Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED):* also G1-T, G1-L, WC, CL, A4′, TC (G1-T and G1-L are implications from a stated
hypothesis on β_n). These, and G2 H_all, HZ, Cor. H-input, are self-contained in the repo's sense: no external
citation, with internal item 11 inputs (H2–H4, H7) and textbook Prokhorov/Portmanteau (WC), as for A-U.
G3′: S, W (from item 11 §7), Lemma G, Lemma N (RHFREE2).
Lean: all items except `theoremHL`, `smoothZeta_HL(_det, _sumForm)`, `smoothZeta_bLaw` (sorry-free per lean/README).
**No headline result (H1–H5) is fully self-contained.** Each rests on (P), the RH-analysis citations, (C1)/(C5), or the
named input Theorem H (supplied on paper: for G3′ and Cor. H_L-ζ, i.e. p = 2, s ≥ 2, citation-free by item 11 Theorem H;
for general p only by G2, mod-cite (P); §3.3). *(Pre-Plan-47 text. Since Plan 47, H1 (Theorem H_all) and Corollary HZ
are fully self-contained (PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED), and G2 supplies Theorem H on paper citation-free for all p > 0,
s > 1. H2–H5 are unchanged.)*

### 3.3 Theorem H input: uses and discharge

Two sources supply `TheoremHPure p κ_p s` (atoms (k+1)^{−p}, weights (k+1)^{−s}, C = 1, κ_p = 3p/2 + log c(p)) on paper:
- **item 11 Theorem H** (math-pursuits, §7): p = 2, s ≥ 2: PROVED + REVIEWED, citation-free (Lommel references); p = 1,
  s ≥ 3/2: PROVED-mod-cite (Tricomi–Carlitz, citation read). Exact k^{−s} weights satisfy its (H-b) with c₁ = c₂ = 1.
  Inputs.lean recorded this range before Plan 37.
- **G2 Corollary H-input** (G2 PROOF.md §3): every p > 0, s > 1, PROVED (Plan 47; was PROVED-mod-cite (P)); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED.

(P) is needed only where G2 is the sole route: p ∉ {1, 2}, p = 1 with s < 3/2, p = 2 with s < 2. Every G3′ instance is
(2, s, 1) with s ≥ 2, so the primary route for G3′ is item 11, citation-free, and **no G3′ result depends on (P)**.
*(Plan 47, 2026-10-14: the previous paragraph is pre-Plan-47 history. G2 Cor. H-input is now PROVED with no citation,
so both routes are citation-free and (P) is needed nowhere, including Lean `theoremHL` at general p (on paper). Lean
labels are unchanged: Theorem H_all is not formalized.)*

How item 11 (math-pursuits f5f6aef, items/11-zero-measure-jacobi-asymptotics/work/proof/PROOF.md §§7, 7b; read
read-only for this table) builds the lemmas G3′ uses:
- **H5** (difference ratios) and **H6** (slow variation): "PROVED", from the mean value theorem and (L1)–(L3) only. No
  Theorem H.
- **H7** (tail cut): "PROVED from Theorem H for the pure power". Theorem H enters only in step 4 (head factor) as an
  upper bound log D_N(Σ k^{−s₀}δ_{k^{−p}}) ≤ −pN²log N + κ_pN² + error, uniformly in N ≤ n. The o(N²) form supplies this
  (Lean `TheoremHPure.uniform_upper` derives exactly this uniform bound from `asymp`), so H7 needs only the instance
  (p, s₀, 1).
- **Theorem H_L**: "PROVED-mod-H", from the two instances (p, s, 1) and (p, s₀, 1) (Lean `theoremHL` takes exactly
  these two hypotheses).
- **Lemma W** (G3′ §4) and the explicit references of item 11 §7 (Theorem A, Lommel, p = 2): PROVED there without
  Theorem H as a black box.
- **Lemma K** (G3′ §7, from H7): H7's steps 1–6 (instance (2, 2, 1)) plus "Theorem H (lower half, weights ≥ c₁j^{−s})"
  (instance (2, s, 1)).

| Result | Use of Theorem H | Instance (p, s, C) | Supplied by (item 11 Thm H / G2 Cor. H-input)? |
|---|---|---|---|
| Lean `theoremHL` | hypotheses `hHlo : TheoremHPure p κ s`, `hHup : TheoremHPure p κ s0` (direct) | (p, s, 1), (p, s₀, 1), any p > 0 | item 11 for p ∈ {1, 2}, s, s₀ ≥ s₀(p); otherwise G2 only (mod-cite (P); PROVED since Plan 47), for s, s₀ > 1. Lean label unchanged (neither proof is formalized) |
| Lean `smoothZeta_HL(_det, _sumForm)`, `smoothZeta_bLaw` | via `theoremHL` (direct) | (2, 2, 1) | yes: item 11 (citation-free), also G2; Lean label unchanged |
| G3′-U | via item 11 H7 (step 5, (Hw) with s = s₀ = 2); H5(i), H6(b, d) do not use Theorem H | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| G3′-L | none: the pure-power comparison is Lemma W (item 11 §7 references) plus H5(i), Lemma S | — | no instance used: Lemma W's s = s_n = 4 + C″(1 + log n) grows with n, which no fixed-s instance covers; Lemma W is proved uniformly in s ≥ 4 from item 11's Lommel references instead |
| N (Prop N) | Theorem H_L at p = 2, s = s₀ = 2 (direct, through H_L) | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| N′ | G3′*-U proof (Theorem T upper bound ⇒ H7) | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| N″ | G3′-U steps 1–5 and H7 for D_n(ν) | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| N‴ | through G3′-U (as N″) | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| B | liminf half: G3′-L proof (Lemma W), no instance; "log D_n = Φ_n + O(n²)" uses G3′-U | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| L′ | Lemma Tr (s = 4), Lemma W, G3′-U | (2, 2, 1), (2, 4, 1) | yes: item 11 (citation-free); also G2 |
| Tr | Lemma K (H7 head + lower half), weights with fixed s | (2, 2, 1), (2, s, 1); s = 4 in L′, Ch | yes: item 11 (citation-free); also G2 |
| Ch | Lemmas Tr, K, W; G3′-U, G3′-L | (2, 2, 1), (2, 4, 1) | yes: item 11 (citation-free); also G2 |
| C, P, Thm S, Thm S′, Thm V⁺ | (SG) ⇒ G3′-L, plus G3′-U for the equality | (2, 2, 1) | yes: item 11 (citation-free); also G2 |
| R, K | R: H5(i) only; K: H7 + lower half | (2, 2, 1), (2, s, 1) | yes: item 11 (citation-free); also G2 |
| T, T′ | H7 (upper bound) and the lower half for ν = Σ v_jδ_{j^{−2}}, c₁j^{−s} ≤ v_j ≤ c₂j^{−2}U(j) | (2, 2, 1), (2, s, 1) | yes: item 11 (citation-free); also G2 |
| G3′*-U, G3′*-L | through T, T′, K | (2, 2, 1), (2, s, 1) | yes: item 11 (citation-free); also G2 |

No "partial" or "no" case was found: every use is an instance (p, s, 1) with s > 1 (in G3′, p = 2 and s ≥ 2), or no
instance at all. The note was appended to the labels in G3′ PROOF.md §0 and README.md, and to §2.5 above. Section
headers inside G3′ PROOF.md and the rhfree/ status tables keep their original wording.

**Resolution (Rule R F1).** The first Plan 37 version credited the G3′ discharge only to G2, mod-cite (P), with a remark
that item 11 already covers p = 2. The review confirmed the remark (every G3′ instance lies in item 11's (H-b) range)
and asked for item 11 to be named as the primary route. That changes no label; it removes a false (P) dependency.

---

*Novelty (first pass, Plan 38) and the research program built on these open problems: `research/program/RESEARCH_PROGRAM.md`.*

## 4. Open problems (as stated in the repo)

**G3′**
1. **G3′ unconditionally**, i.e. 𝒞(K) = o(K²) for the ζ ordinates (Theorem Ch). Known: (U) and Theorem B
   (O(n²)) with no hypothesis on the zeros, mod (C1), (C5), Theorem H (p = 2 input supplied citation-free by item 11, §3.3); G3′ under (SG), PCC, SPC_ℂ⁺, SPC_ℂ⁺(full), RH + (V⁺), RH + (V).
   By N″, G3′ ⇒ d(E) = 0 (proportion-one distinct ordinates). Best unconditional input read: (C3) N_d ≥ 0.4075N;
   Lamzouri (C6) 67.25% simple and on the line. Numerically 𝒞(K)/K² ≤ 1.1·10⁻⁷ at K = 2·10⁶ (§5.5). The repo says
   explicitly that "as hard as a known open problem" is *not* claimed (§5.5). *Update (Plan 43, §5.6):* G3′ ⇒ 100% of
   zeros simple and on the critical line, so G3′ is at least as hard as that statement; d̄(E) ≤ 0.3275 unconditionally.
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
   (T3-log). *Update (Plan 48, §3.17): PROVED-mod-cite for p > 1, 1 < s < 1 + 2p (Corollary B_{p>1}), bypassing QL.
   Plans 50–52 and 54 extend this to every p > 0 and every s > 1 — §2.8. **CLOSED.** Still open: the 1/n coefficient
   (tilt law, CONJECTURE).* *Update (Plan 44, §3.14):* reduced to the single hypothesis **QL** (log-moment localization along vΨ^t);
   QL is open for D(γ) = ∞ (at t = 0 it is a uniform-in-M form of Lemma LP).
8. **Nodes other than pure powers.** "Other nodes x_k = f(k) need a substitute for the pure-power law in Lemma LP"
   (§3.8 L4; §4). The analytic families done are pure powers (all p > 0) and the smooth-ζ model (README). The literature
   read has no RH analysis for general nodes accumulating at 0 with merely sandwiched weights (§4 point 2).
9. **(CL) for general nodes or p ≤ 1** (§3.1 CL4; §4). For p ≤ 1, J is not trace class and A2 does not apply as stated.
10. ~~**Conjecture R, window form**~~: PROVED for ε ≤ ε₀ (Theorem RW, §3.10, Plan 39). Still NUMERICAL: the every-ε /
    absolute-constant form, and small fixed scale ratios (e.g. ×4); proved constants are tiny (η_W ≈ 10⁻⁷ at p = 2).
11. **Density-one law for rough (Theorem R-type) weights**: "whether a density-one law holds for such weights is open"
    (§3.7 avg1).

**Additional open items**
12. Pointwise a_n for rough weights: *now REFUTED in general* (Theorem Ra, §3.12, Plan 41: fixed-size rough weights
    break the pointwise a-law). Earlier text: A4/A4′ give only tail/block/b-weighted-density forms; "A pointwise density
    statement does NOT follow" (§3, A4 text). For slowly varying Ψ the a-law is proved (T3a, T3-all, T3-log; A1 note).
13. Second-order constants for pure powers: RH₁ n²(b_n^σ/b_n^{TC} − 1) → −1/24 "conjecture, not proved"
    (RH_p1.md §0); d₁ = −(s−1)/2, e₁ = p/2 are NUMERICAL Phase-0 fits (RH.md §0, RH_px §0); RH_p proves only O(1/n).
    *Update (Plan 62, 2026-10-15, REVIEWED; research/G1/RH/second_order/SECOND.md, §2.10 above):* NUMERICAL on
    p ∈ {½, 1, 3/2, 2, 3, 4}, s ∈ {3/2, 2, 3, 4} (n ≤ 1600): d₁ = −(s−1)/2, e₁ = p/2 (repo pairing α_{n−1}/(2b_n)) =
    e₁ˢ + p with e₁ˢ = −p/2 (standard pairing α_n/(2b_n)), chain k₀ = −(s−1) − p/2, k₁ = −(p+2)(2s−2−p)/(2p) (Conjecture P62).
    PROVED(-mod-cite): exact p = 2, s ∈ {2, 4, 6, 8, 10}; the log-average form of d₁ on the lattices s ∈ 2 + 2ℕ₀
    (p = 2) and s ∈ 3/2 + ℕ₀ (p = 1). CONDITIONAL on (E) at s and s + p (+ mod-cite): the Christoffel constraint
    d₁(s+p) = d₁(s) − p/2 (Cor 3.3); CONDITIONAL on (E_ε), ε > ½, at s and s + p: e₁ˢ = −p/2 (Thm 3.4). *Update (Plan 64, REVIEWED; UL.md):* the (UΛ)/(CVX) dependencies are removed — the Cesàro s-slope
    (Thm 3.8, with constant) and the log-average form at every s > 1 for p ∈ {1, 2} (Thm 3.10(d)) are PROVED-mod-cite, Cor 3.9
    needs (E) only; (UΛ) holds in its o(log n) form. Open: sup_K|Λ_n| = O(1) (uniform hard edge); (CVX) for σ_{p,s}. *Update (Plan 65, REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md); E_pgt1.md):* (E) is PROVED-mod-cite for p > 1 — n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)) and
    all five constants of Conjecture P62 (d₁, e₁, e₁ˢ, k₀, k₁), with remainder O(n⁻²); hence g(p) = 0 for p > 1 and Cor 3.3, 3.9
    unconditional there. Still open: (E) for 0 < p ≤ 1 and g(p) for 0 < p < 1 (GAP). The −1/24 (second-order) conjecture is not addressed.
    *Update (Plan 66, REVIEWED; E_p1.md):* (E) is PROVED-mod-cite at p = 1 for every s > 1 (remainder O(n⁻²); d₁, e₁, e₁ˢ, k₀
    of P62), and the −1/24 conjecture is PROVED-mod-cite (elementary comparison with Tricomi–Carlitz; also at s = 5/2 vs x·TC).
    Still open: k₁ at p = 1 for s ∉ {3/2, 5/2} (NUMERICAL −3(s − 3/2) to 10 digits); (E) and g(p) for 0 < p < 1.
    *Update (Plan 67, REVIEWED; E_plt1.md):* (E) is PROVED-mod-cite for 0 < p < 1 with the sharp remainder:
    n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), κ_p = 2pc(p)ζ(−p), the same κ_p for α_n and the chain
    (none in α_n/(2b_n)); all constants of Conjecture P62 for 0 < p < 1; g(p) = 0 for p < 1. With Plans 65–66, (E) now holds
    for every p > 0. Still open: k₁ at p = 1 for s ∉ {3/2, 5/2}; the n^{−1−2p} coefficient and d₂ (p ≠ 1, 2).
14. Lemma R1's η, J are non-explicit (proof by contradiction) (§3.6 R-b). *Update:* explicit (but tiny) constants in the
    window version R1W (§3.10) and for the a-law R1a (§3.12); sharp constants (phase model 4/π, 8/π²) open.
15. Novelty searches (Rule L): first pass done 2026-10-14 (research/program/novelty_*.md; summary in
    research/program/RESEARCH_PROGRAM.md §1); gating unread items listed there. Earlier text: not done for any result; prior-art pointers recorded but unread (G2 §3; G1 CL3, R-d, TL).
16. ~~Lean: Theorem H / H_all~~: **CLOSED** (Plans 60–61). `theoremHPure_all` (all p > 0, s > 1) and Paper 1
    Theorem 1.1 / Cor. 1.2 / Cor. 1.4 in full (`paper1_thm11`, `paper1_cor12`, `paper1_cor14`) are sorry-free in Lean.
    Still not formalized: uniqueness of the maximiser, the forward Weyl law (lean/README).
17. In review: none on master. New (Plan 42): **RL-UI** — whether weak convergence ν_n → arcsine *without* the a priori
    bound implies Law P (§3.13).

---

## 5. Consolidation log (Plan 37)

Items 1–17 are the inconsistencies listed in the draft of this file (master 38bfb3b). "Fixed" means a text or label
change; no statement or proof was changed.

1. **Theorem H input vs G2.** Fixed. G2 PROOF.md §3 gained Corollary H-input. §3.3 above records how each result uses
   Theorem H; every use is covered. The note (first version "; Theorem H input discharged by G2 Cor. H-input
   (mod-cite (P))"; revised by Rule R F1/F2, see below) was
   appended to the 20 Theorem-H labels in G3′ PROOF.md §0 and to the README G3′ labels; G3′ §0 gained a paragraph
   pointing here. lean/README.md: one sentence in the intro, and the `theoremHL` row now says the input is supplied on
   paper for all p > 0, s > 1 (item 11 alone gave p ∈ {1,2}, s ≥ s0(p)). Docstrings of `TheoremHPure`
   (Inputs.lean) and `theoremHL` (TheoremHL.lean) updated the same way (comments only). Lean labels unchanged.
   G3′ section headers and rhfree/ tables not edited.
2. **README G3′ "pending Rule R review" / old stop condition.** Fixed by the README rewrite (E): one G3′ block with
   current labels.
3. **README Plan 9 G1 bullet ("Stop report: GAP …").** Fixed (removed by the rewrite; G1 now described by T3-all,
   T3-log, Theorem R, Theorem CL).
4. **README Status open list garbled.** Fixed (rewritten; points to §4 here).
5. **G1 §0 G1-R row.** Fixed: it now cites Theorem R, T3-all, T3-log and the remaining open cases, with a dated note
   giving the previous text.
6. **G1 §3 A1 "remaining a_n gap; see §4".** Fixed with a dated Plan 37 note after the sentence (original kept).
7. **RH_p1_general.md §0 "(CL)" for p = 1.** Fixed in place: the sentence is struck through and a dated "Corrected"
   note says (T3) holds for the family directly, and (CL)/A2/A4 are p > 1 statements (G1 §3.1 CL4). The plan-10 spec
   (docs/superpowers/plans/2026-10-13-plan-10-RH-pure-power.md) got a dated correction note after the same claim; its
   Phase-5 checklist line was left as history.
8. **Stale "Open" sections.** Fixed with dated notes: RH_px.md §6 "Open: 0 < p < 1" (closed by RH_plt1b),
   RH_plt1.md §6 (closed by RH_plt1b), RH_zeta.md §4.3 "Hard edge 0 — OPEN" (closed in RH_zeta_close §1).
9. **RH.md / RH_proof.md.** Fixed: each now opens with a dated "Superseded" note pointing to RH₁, RH₁(r), RH_p and the
   seam (RH.md) or RH_p (RH_proof.md).
10. **Label lists between headers and G1 §0.** Fixed without upgrading: G1 §0 RH₁ now reads "(WLXZ v1 §§2–6)" as in
    RH_p1.md; G1 §0 RH_p now lists "G2 PROOF.md μ*, B*" (only μ*, B*(i)–(ii), which do not use (P)), and RH_px.md's
    header got the same clarification; G1 §0 RH_ζ now lists the file's section numbers and "G2 — optimality, for E1(iv)
    only, which RH_zeta.md §1 says is not needed". G2 was kept in both lists.
11. **Unlabelled internal lemmas.** Fixed: G1 §0 gained rows Sat_p (PROVED), WC and A4′ (PROVED-mod-cite (P), from the
    §3.1 header) and Sat_p⁺ (no separate label in its header; the row says so and records its Rule R review). G2
    Corollary A2 is now labelled PROVED (its proof uses Lemma A1 and the scaling identity only; no citation) in the
    section and in a new §0 row.
12. **G3′ §8.3 snapshot; README "(U) unconditionally".** Fixed: §8.3 is marked "Historical snapshot … after Plan 17"
    with a pointer to §0. The README gives (U) its full label (PROVED-mod-cite + mod-input Theorem H + REVIEWED,
    discharge note) and says "with no hypothesis on the zeros".
13. **"P" overloaded.** Not renamed (brief). Listed in the glossary §6.
14. **Name clashes.** Not renamed (brief). Listed in the glossary §6.
15. **README G2 bullet.** Fixed: Theorem H_all is labelled PROVED-mod-cite (P), REVIEWED; HZ range is real a > 0,
    2a + b > 1, as in G2 §0.
16. **Label vocabulary.** Fixed: VERIFICATION_POLICY.md gained a table defining PROVED-mod-cite, PROVED-mod-input
    (with G3′'s usage for hypotheses), CONDITIONAL, GAP and REVIEWED, copied from the G1/G2 headers.
17. **Plan 36 timing.** Resolved: the "Plan 36 note" and ⚑ flags were removed; T3-log is REVIEWED on master (G1 §0,
    §3.9).

Not done: Lean was not rebuilt for the docstring edits (the worktree has no `lean/.lake/packages` symlink; a `lake env`
attempt started cloning Mathlib and was stopped, and the partial `lean/.lake` it created was deleted). The edits are
inside `/-- … -/` docstrings only.


**Rule R review (research/G2/review/REVIEW_Plan37.md, ACCEPT WITH FIXES) — fixes applied 2026-10-14:**
- **F1 (major).** The G3′ discharge is now credited first to item 11's Theorem H (p = 2, s ≥ 2: PROVED + REVIEWED,
  citation-free), with G2 Cor. H-input (mod-cite (P)) as an alternative route. The 19 G3′ §0 notes (all except G3′-L),
  the G3′ §0 paragraph, G2 Cor. H-input's "Consequence" sentence ((P) only where G2 is the sole route: p ∉ {1, 2},
  p = 1 with s < 3/2, p = 2 with s < 2, in practice Lean `theoremHL` at general p), THEOREMS header, §1 (H1, H5),
  §§3.1–3.3, §4 item 1, README (G3′ bullets) and lean/README intro were updated. The §3.3 remark became the recorded
  resolution. No label upgraded; a false (P) dependency was removed.
- **F2.** G3′-L's note now reads "; uses no Theorem H instance (THEOREMS §3.3)" (G3′ §0 and §2.5).
- **F3.** Cor. H-input: the `bdd` field cites the sorry-free Lean theorem `heineK_bdd_of_summable`; "Lean
  `heineD_eq_det`, PROVED" → "sorry-free". The optional Inputs.lean docstring note was *not* made: a Lean build was
  running in this worktree and lean/*.lean files were off limits.
- **F4.** §1 overview: the smooth-ζ pointwise law is stated with its κ/log n correction; "unconditionally" → "with no
  hypothesis on the zeros".
- **F5.** §3.1 (C1) row now lists the results that use (C1) and those that do not.
- **F6.** §2.5 Lemma W row restores "uniformly in s ≥ 4"; §3.3's G3′-L row says s_n grows with n, so no fixed-s
  instance covers it, and Lemma W is proved from item 11's Lommel references.
- **F7.** (a) RH_zeta_close.md's header got a dated note with the same G2/E1(iv) annotation; THEOREMS says "label as in
  G1 §0". (b) Thm S, S′, V⁺ rows in §2.5 now say "label as in G3′ §0; proof <rhfree file>" (with RHFREE.md §3's longer
  citation list). (c) G1 §0 LP row now has min(1, ·) as in §3.8.
- **F8.** VERIFICATION_POLICY.md: attributions corrected per label; one-line definitions added for PROVED-mod-G2,
  PROOF SKETCH / DRAFT, REFUTED (vs RETRACTED), SUPERSEDED, HYPOTHESIS, OBSTRUCTION, HEURISTIC, sorry-free; dated note
  on the stale "Lean is not installed yet". G2 header got a dated note that "generalizes" is no longer accurate.
- **F9.** README Lean bullet names both routes (item 11 for p ∈ {1, 2}, s ≥ s₀(p); G2 for all p > 0, s > 1).
- **F10 (info).** Lean rebuild: `lean/check.sh` run by the coordinator on this branch (after the docstring edits), 2026-10-14: AUDIT OK (no sorryAx; only propext, Classical.choice, Quot.sound).
- **F11 (info).** Confirmations; nothing to change.


**Plan 47 (2026-10-14, branch plan-47-noP): removing the citation (P).** G2 PROOF.md §1 gained Lemma EP (energy
positivity with Fourier identity; papers/paper1/main.tex Lemma 3.3 and proof, refereed CORRECT), and B*(iii)'s
optimality now uses it, with (EP-int) checked via |ν| ≤ μ^x + μ*; the (P)-based text is kept as a remark. Relabels
(each verified by reading the dependency chain; full table with inputs in research/G2/LOG.md "Plan 47"):

| Result | Old label | New label |
|---|---|---|
| G2 Lemma EP (new) | — | PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| G2 B* | PROVED-mod-cite (P) | PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| G2 H_all (H1) | PROVED-mod-cite (P) | PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| G2 HZ | PROVED-mod-cite (P) | PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| G2 Cor. H-input | PROVED-mod-cite (P), as H_all | PROVED, as H_all; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| G1-T, G1-L | PROVED-mod-cite (G2 (P)) | PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| WC, CL, A4′, TC | PROVED-mod-cite (P) (through G2 B*(iii)) + REVIEWED | PROVED + REVIEWED (proofs unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| T3-avg | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; (P) via TC) + REVIEWED | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) + REVIEWED; relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| G3′ §0 notes (19 rows), Lean `theoremHL` | "… G2 Cor. H-input (mod-cite (P))" | "… (PROVED since Plan 47; was mod-cite (P))"; labels unchanged |

Edited: G2 PROOF.md (header note, §0, Lemma EP, B*(iii), Cor. H-input), G2 CITATIONS.md, G2 LOG.md, checks/
check_positivity.py (+ .out), G1 PROOF.md (§0 note and rows, §3.1/§3.7 header notes, TC proof bullet, Ra-a remark), G3′
PROOF.md (§0 notes, Theorem H paragraph note), README.md, lean/README.md, this file (header, H1, H4, H5, H6, §2.1–2.3,
§3.1–3.3, glossary), research/program/RESEARCH_PROGRAM.md and outline_A_nodes.md (dated notes). Not changed: RH_ζ (its
E1(iv) applies G2's argument to a different measure; (EP-int) there not re-checked; E1(iv) is not needed for RH_ζ),
Lean docstrings in Inputs.lean / TheoremHL.lean (still "mod-cite (P)"; .lean files not edited), review files, logs and
§5 Plan 37 items (history), novelty_G2.md. Pre-Plan-47 sentences about where "(P) enters" are kept with dated notes.
Plan: docs/superpowers/plans/2026-10-14-plan-47-noP.md.

**Plan 47 Rule R (research/G2/review/REVIEW_Plan47.md, ACCEPT WITH FIXES, all minor) — fixes applied 2026-10-14:** F1
Rule A δ_0 − δ_1 example reworded (both sides +∞); F2 derivations of the B*(ii) and Value absolute bounds added in G2
§1; F3 Lean docstrings of `TheoremHPure` (Inputs.lean) and `theoremHL` (TheoremHL.lean) updated (comments only) and
`lean/check.sh` re-run on branch plan-47-noP (2026-10-14, after the docstring edits): build completed (8955 jobs), AUDIT OK (only propext, Classical.choice, Quot.sound); F4 dated note at RH_zeta.md E1(iv); F5 check_positivity.py
tail constant corrected to (3/(2π))/cut; F6 header wording; F7 §3.2 "self-contained" qualified (internal item 11
inputs); F8 dated note at novelty_G2.md. All "Rule R pending (Plan 47)" markers replaced by the REVIEWED marker, as the
reviewer recommended. The G3′, Lean and RH_ζ labels stay unchanged.

---

## 6. Glossary / name disambiguation

No name was changed. Where a name means different things, the meaning is fixed by the area.

| Name | Meanings and locations |
|---|---|
| **Theorem B** | (1) item 11 Theorem B, the forward Weyl law (lean/README "Not here"; not formalized). (2) G3′ Theorem B, the unconditional bounded defect liminf ≥ −3 log C (G3′ §8.1). (3) Unrelated: G2 B0, B* (equilibrium lemmas); the scalar function B in RH_px §3 and RH_plt1 ("Binet-cut B", B_in, B_out). |
| **Theorem A** | item 11 Theorem A (Lommel family, exact; cited in G3′ Lemma W as "Theorem A refs"). Not G1 A1–A4 or G2 A1, A2, A-U, A-L. |
| **A1, A2** | G1 Prop. A1 (windowed positivity) and Prop. A2 (Heine tail identity, p > 1); G2 Lemma A1 (discretization) and Cor. A2 (head bound). Also A3, A4, A4′ (G1) and A-U, A-L (G2). |
| **Theorem C** | item 11 Theorem C (conditional inverse) and C′ (Tauberian inverse); G3′ Theorem C (PCC ⇒ (SG) ⇒ G3′, §8.2). Citation labels (C1)–(C8) are G3′ CITATIONS entries. |
| **Lemma K** | G1 Lemma K (kernel identity for second differences, §1); G3′ Lemma K (concentration, from item 11 H7, §7). |
| **TC** | (1) Tricomi–Carlitz measure/fact (item 11 §7; G1 §0 RH₁ row "via TC(α = 1)"; RH_p1.md b_n^{TC}). (2) G1 Lemma TC, tail count (§3.7). |
| **TL, TLw / TL(w)** | G1 Lemma TL (polynomial tail localization, §3.4) and its weight-general form TLw = TL(w) (§3.9). |
| **Lemma S vs Theorem S** | G3′ Lemma S (index shift, §4); G3′ Theorem S (SPC_ℂ⁺ ⇒ G3′, rhfree/RHFREE.md §3) and S′ (RHFREE2); RH_plt1b Lemma S(iii) (seam); Lemma Sat (G3′ §5.2), Sat_p, Sat_p⁺ (G1). |
| **N** | G3′ Proposition N (counting information does not decide G3′, §5) and Theorems N′, N″, N‴; Lemma N and Cor. N1 (inertia bound, rhfree/RHFREE2 §2); N₀ (smooth counting function); N(T) (zero counting). |
| **P** | (1) "Law P" (the target law). (2) citation **(P)** = Beckermann–Kalyagin–Matos–Wielonsky Lemma 2.1 (G2 CITATIONS), as in "PROVED-mod-cite (P)". (3) item 11 Lemma P (α ≥ 2β), Lean `lemmaP`. (4) G3′ Corollary P (RH + (V) ⇒ G3′, §9.1; the G3′ §0 row is named "P"). (5) Lemmas P1–P3 (rhfree/RHPRIME). (6) Lemma PC, PC′ (rhfree). (7) RH_zeta.md E1(iv) "the positivity lemma (P)" = the same citation (P) (G2 CITATIONS: "Positivity of logarithmic energy"). Since Plan 47 (P) is replaced in G2 by **Lemma EP** (energy positivity, G2 §1). (8) G1 §3.1 P_n = Heine measure; p = the exponent. |
| **H** | item 11 Theorem H (p ∈ {1,2}); G2 Theorem H_all; Lean named input `TheoremHPure`; Theorem H_L and Corollary H_L-ζ; item 11 Lemmas H1–H7; G3′ Lemma H (determinantal deletion, §5.2); G2 Cor. H-input. |
| **R** | Rule R (review); G1 Conjecture R and Theorem R (§§3.2, 3.6) with Lemmas R1, R2; G3′ Lemma R (pair factors under thinning, §7). |
| **L** | G1 Theorem L (localization at scale Mn, §3.8) and Lemma LP; G3′ Theorem L′ (log-gap condition, §4.1) and G3′-L (lower bound); L(j) = j²x̃_j (slow factor of the smooth ζ model, G3′ §1) and item 11's L in H_L. |
| **T** | G3′ Theorem T, T′ (thinning, §7); G1 hypothesis (T3) and Theorems T3-conv, T3-sv, T3a, T3-avg, T3-all, T3-log; Lemma Tr (G3′ §4.1). |
| **W** | G3′ Lemma W (uniform weight lower bound, §4); W := Σ_k w_k (total mass, G1 §3.1, item 11 H7). |
| **G** | G3′ Lemma G (spectral small-gap lemma, rhfree/RHFREE §2); G(n) := Σ(n−j)u_j (G1 §1); G(k) comparison atoms (G3′ §3, item 11 H7); the g-function of RH analyses; G1-T, G1-L, G1-R, G2, G3′ as problem names. |
| **D** | D_n (Hankel determinant); item 11 Prop D (weight hypothesis cannot be dropped); RH_zeta_close Proposition D (transfer to σ_ζ) and Lemma D1; D(γ) (T3-log's log-type modulus); D-functions in RH_px §3; (D∞) hypothesis (G3′*). |
| **E1–E5** | G2 Lemma EP (energy positivity, Plan 47; replaces citation (P)). RH_zeta Lemmas E1–E5 (finite-N edge equation); item 11 E1 (zero-built measures take ordinates as real numbers, AGENTS.md) and Lemma E (tunnelling); E = repeated-index set (G3′ §5); E(T) (Trudgian bound, Z1). |
| **Z** | G3′ Lemmas Z1, Z2 (ordinate comparison); RH_zeta_close Lemma Z (far field, Arb-certified). |
| **κ** | (1) κ_p := 3p/2 + log c(p) (G2, item 11). (2) κ := 3 + log(π²/16) = κ_2 (Lean `TheoremHPure 2 κ 2`, G3′ Φ_n). (3) RH_ζ's coefficient κ = −2(log(π/2) − (1 − log 2)) = −0.28946… of 1/log n. (4) G1 Lemma TL's exponent κ = (2 + 2/p)s/(s−1) (and Theorem R's windows [θN, N^{κ+1}]). (5) κ′ (a constant in G1 A3's proof). |
| **β** | β_n := n^pb_n/(c(p)C) (G1); G2's β_t = 4c(p)t^{−p} (arcsine edges); RH₁(r) β_N (squared recurrence coefficients of the symmetrization); β in N‴ (gap exponent e^{−βk}). |
| **σ, ω, s** | σ: spectral measure (G1), G2's constraint measure (G1 A3), σ_{p,s} pure power. ω: oscillation modulus (G1), arcsine law ω_{[0,β]} (G2), ω(η) (G3′ T′). s: weight exponent; RH.md uses r for it (RH₁(r)). (G1 header notes these as local.) |
| **RH** | Riemann–Hilbert in research/G1/RH/ and "RH analyses"; Riemann Hypothesis only as a labelled hypothesis in G3′ §9 and rhfree/ (RH + (V), RH + (V⁺)); rhfree/RH99.md = self-contained proofs of Goldston's (C8) (9.7), (9.9) under RH. |
