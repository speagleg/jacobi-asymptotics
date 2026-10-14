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

*(Plan 47 note, 2026-10-14: G2's citation (P) was replaced by G2 Lemma EP (self-contained). Rows G1-T, G1-L, CL, WC,
A4′ and TC are relabelled PROVED, and "(P) via TC" is dropped from T3-avg. RH_ζ (G2 optimality for its E1(iv), a
different measure) is not changed. Each changed label says "Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED". Table: research/G2/LOG.md
"Plan 47".)*

| Result | Statement | Label |
|---|---|---|
| K | second difference of G(n) := Σ_{j<n}(n−j)u_j over ±h = triangle-kernel sum of u, of total mass h² | PROVED |
| **G1-T** | H_all + (T3) slow oscillation of β_n ⇒ β_n → 1, i.e. n^p b_n → c(p)C | PROVED (Plan 47; was PROVED-mod-cite (G2 (P)); only input H_all, now PROVED via G2 Lemma EP); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| **G1-L** | H_all + a one-sided bound (sup β_n < ∞ or inf β_n > 0) ⇒ (1/n)Σ_{j<n} log(j^p b_j) → log(c(p)C) | PROVED (Plan 47; was PROVED-mod-cite (G2 (P)); only input H_all, now PROVED via G2 Lemma EP); Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| A1 | J ≥ 0 ⇒ sine-weighted window averages of a_j are ≥ 2cos(π/(L+1))·min b over the window. Hence, if b is regular, liminf of window averages of a_j/(2b_j) ≥ 1 | PROVED |
| A2 | p > 1: Σ_{j>n} a_j = 𝔼_n[Σ_{k∉S} x_k] (Heine ensemble) | PROVED |
| A3 | Q_p := ∫ x d(σ − μ*) = 2c(p)/(p−1) | PROVED (uses only G2 B*(i) and the definition of μ*, both citation-free) |
| A4 | (CL) ⇒ tail-Cesàro a-law; with β_n → 1, block-Cesàro ratios Σa/Σ2b → 1 and window averages → 1 in b-weighted density (pointwise density NOT proved) | CONDITIONAL on (CL). (CL) is proved for pure-power atoms by Theorem CL (§3.1, REVIEWED), so the tail-Cesàro part is unconditional there; (i)–(ii) still need β_n → 1 |
| **CL** | (CL) for pure-power atoms k^{−p}, p > 1, and ROUGH weights (Σw < ∞, w_k ≥ c₁k^{−s}): n^{p−1}𝔼_n[Σ_{k∉S}x_k] → Q_p. Hence n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p−1) unconditionally (§3.1, Plan 27) | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii), which now uses G2 Lemma EP; internal inputs: G2 A1, A-U, A-L, B*; G3′ §5.2 Lemma Sat); REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED; novelty UNCHECKED |
| Sat_p | saturation, p ≥ 1: 1 − ρ_n(k) ≤ (W/w_k)e^{−2n·g_p(k/n)} (§3.1) | PROVED (§3.1 header); REVIEWED |
| WC | concentration at speed n²: P_n(\|⟨φ, ν_S⟩ − ⟨φ, μ*_u⟩\| > δ) ≤ e^{−c(φ,δ)n² + o(n²)} (§3.1) | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii), which now uses G2 Lemma EP) (§3.1 header); REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| A4′ | unconditional tail-Cesàro a-law: x_k = k^{−p} (p > 1), Σw < ∞, w_k ≥ c₁k^{−s}: n^{p−1}Σ_{j≥n}a_j → 2c(p)/(p − 1) (§3.1) | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii), which now uses G2 Lemma EP) (§3.1 header); REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED |
| Sat_p⁺ | Sat_p for all p > 0, with the extra factor ((n+1)/k)^{2(1−p)₊} and g_p⁺ (§3.3); internal input of T3-conv, T3-sv, T3a, Thm R, L, T3-all, T3-log | no separate label in the §3.3 header (which labels T3-conv); the proof is that of Lemma Sat_p (PROVED) with two elementary changes; Rule R (review/REVIEW_Plan29.md) ACCEPT WITH FIXES, F1 applied — REVIEWED |
| G1-R | (T3) from the atoms alone; (CL) (proved for pure-power atoms with rough weights, p > 1: Theorem CL; open for general nodes or p ≤ 1) | (T3) half **REFUTED** for sandwiched weights (Theorem R, §3.6); PROVED-mod-cite for pure-power nodes with slowly varying Ψ: bounded Ψ (Theorem T3-all, §3.8; contains T3-conv, T3-sv/T3a, T3-avg) and log-type Ψ (Theorem T3-log, §3.9); open for slowly varying Ψ with D(γ) = ∞ and for nodes other than pure powers. (CL) half: proved for pure powers k^{−p}, p > 1 (Theorem CL); open for general nodes or p ≤ 1 (see §4). *(Row updated by Plan 37, 2026-10-14; previously "proved for polynomially slowly varying weights (T3-sv/T3a); (CL) half unchanged".)* |
| FV | first variation: d/dt log b_n²(v e^{tf}) = ⟨f, μ_n − μ_{n−1}⟩, μ_n := w p_n² (§3.2) | PROVED (standard; novelty not claimed); REVIEWED |
| Conj R | (T3) — hence the pointwise b-law — FAILS for some weights e^{−ε}k^{−2} ≤ w_k ≤ e^{ε}k^{−2} (p = s = 2; §3.2, Plan 28) | Proved in modified form as Theorem R (§3.6): ε ≤ ε₀, non-explicit η, windows [θN, N^{κ+1}]. The [0.6N, 1.6N]-window form remains NUMERICAL (as of Plan 33). *(Plan 39, 2026-10-14: window form, incl. [0.6N, 1.6N], proved for ε ≤ ε₀ explicit with N_{i+1}/N_i → ∞ — Theorem RW, §3.10, Rule R ACCEPT WITH FIXES, re-check ACCEPT — REVIEWED; every-ε/absolute-c and ×4 forms still NUMERICAL.)* |
| **Thm R** | Conjecture R proved in modified form (all p > 0, s > 1): there is ε₀ = η/16 such that for every ε ≤ ε₀ there is f with \|f\| ≤ ε such that w = k^{−s}e^{f} has limsup \|log(β_n²/β_{n−1}²)\| ≥ εη/2; so (T3) and the pointwise b-law fail for some weights in [e^{−ε}, e^{ε}]·k^{−s} (§3.6, Plan 33) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FV, Sat_p⁺, TL, §3.5 two-point formula); proves Conjecture R in modified form; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan33.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED. Sub-labels: R2 PROVED; R1 PROVED-mod-cite |
| **T3-conv** | pointwise b-law (hence (T3)) for x_k = k^{−p} (p > 0), w_k = k^{−s}ψ_k (s > 1) with **ψ_k → L ∈ (0, ∞)** (rough at finite scales, decaying roughness): n^p b_n → c(p) (§3.3, Plan 29) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV (REVIEWED), Lemma Sat_p⁺); REVIEWED; novelty UNCHECKED (comparison theorems of Máté–Nevai–Totik type may be classical) |
| TL | polynomial tail localization: for sandwiched weights c k^{−s} ≤ w_k ≤ C k^{−s} (s > 1), 𝔼_{n+1}#(S ∩ (T, ∞)) ≤ ε, hence μ_n((T, ∞)) ≤ ε, for T ≥ A·n^{κ}ε^{−1/(s−1)}, κ = (2 + 2/p)s/(s−1) (§3.4) | PROVED (textbook-standard Markov/Chebyshev inequalities, quoted); REVIEWED; novelty UNCHECKED (pointers: Ehlich–Zeller 1964, Coppersmith–Rivlin 1992, Rakhmanov 2007, Nevai, Máté–Nevai–Totik) |
| **T3-sv** | pointwise b-law for w = k^{−s}Ψ with Ψ bounded and *polynomially slowly varying*: sup_{n/M≤k≤n^γ}\|log Ψ(k) − log Ψ(n)\| → 0 for all M, γ (e.g. Ψ = 2 + sin√(log log k)) (§3.4, Plan 30) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: Lemma FV, Lemma Sat_p⁺, Lemma TL); REVIEWED; novelty UNCHECKED |
| FVa | first variation of a_n: d/dt a_n(v e^{tf}) = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩ (q_j = √w p_j) (§3.5) | PROVED (standard; novelty not claimed; self-contained via the proof of Lemma H and Christoffel–Darboux); Rule R ACCEPT WITH FIXES, re-check ACCEPT — REVIEWED |
| **T3a** | pointwise **a-law** n^p a_n → 2c(p) under T3-sv's hypotheses (Ψ bounded, polynomially slowly varying; includes ψ_k → L), all p > 0, s > 1 (§3.5, Plan 32) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal: FVa, Sat_p⁺, TL); REVIEWED; novelty UNCHECKED |
| TC | tail count: 𝔼_m#(S ∩ (Mm, ∞)) ≤ (2A/(p log M))·m + o(1) uniformly over sandwiched weights, every p > 0 (§3.7) | PROVED (Plan 47; was PROVED-mod-cite (P) through G2 B*(iii), which now uses G2 Lemma EP; internal: G2 A1/A2, A-U, A-L, B*) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT — REVIEWED (proof unchanged); relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED; novelty UNCHECKED |
| **T3-avg** | for w = k^{−s}Ψ with Ψ bounded and **uniformly slowly varying** (δ_N(M, M′) → 0; e.g. 2 + sin(log log k)): (1/N)Σ_{n=N}^{2N}\|log b_n²(w) − log b_n²(v)\| → 0 and (1/N)Σ n^p\|a_n(w) − a_n(v)\| → 0; hence the full pointwise Law P along a set of n of density one (§3.7, Plan 34) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) (Plan 47: "(P) via TC" removed, TC is now PROVED; Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **TV** | (d/dt)μ_m(A) = ⟨f1_Aq_m,q_m⟩ − 2⟨1_Aq_m, K_m(fq_m)⟩ − ⟨fq_m,q_m⟩μ_m(A) along w(t) = we^{tf} (§3.8, Plan 35) | PROVED (standard; novelty not claimed) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED |
| **LP** | pure power: μ_n((Mn, ∞)) → F_p(M) = (2/π)arcsin√(min(1, M^{−p}/(4c(p)))), M ≥ 1 (§3.8; min added by Plan 37 to match §3.8) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; textbook method of moments) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED; novelty not claimed |
| **Thm L** | localization at scale Mn: limsup sup_t μ_m^{(t)}((Mn, ∞)) ≤ e^{4G}F_p(M) for bounded slowly varying Ψ (§3.8) | PROVED-mod-cite (as LP; internal TV, Sat_p⁺) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **T3-all** | for w = k^{−s}Ψ with Ψ bounded and **slowly varying** (δ_n(λ) → 0): n^pb_n → c(p) and n^pa_n → 2c(p) for **all n** — the full pointwise Law P; contains T3-conv, T3-sv, T3-avg (§3.8, Plan 35) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, L) + Rule R ACCEPT WITH FIXES (review/REVIEW_Plan35.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **T3-log** | for w = k^{−s}Ψ with Ψ **log-type slowly varying** (slowly varying, and D(γ) < ∞; e.g. (log k)^α, any α ∈ ℝ): the full pointwise Law P, all n; contains T3-all (§3.9, Plan 36) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, Sat_p⁺, TL(w), L, T3-all) + Rule R ACCEPT WITH FIXES, fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **RW** | Conjecture R in window form (all p > 0, s > 1): for every window [aN, bN] with b > u_s(p) (e.g. [0.6N, 1.6N], admissible for every p), explicit η_W > 0 and ε₀ = η_W/16 such that for ε ≤ ε₀, f(k) := ε·Σ_i sign(Δ²μ^v_{m_i}(k))·1_{[aN_i, bN_i]}(k) (pointwise signs) with N_{i+1}/N_i → ∞ (or > R_W fixed) gives limsup log(β_n²/β_{n−1}²) ≥ εη_W/2 (resp. /4), i.e. limsup (β_n/β_{n−1} − 1) ≥ εη_W/4 (resp. /8); Lemma R1W: for N ≥ N₀, ‖Δ²μ^v_m\|_{[aN,bN]}‖₁ ≥ η_W for some m ∈ [N − J_W + 1, N] (§3.10, Plan 39) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, R2, LP, Sat_p⁺, G2 B*(i) ((P)-free)); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan39.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED. Not proved: every ε with absolute c; ×4 separation (NUMERICAL) |
| **LR / LRa** | linear response with explicit ε² remainder, any finite-moment base v, ε := ½ osc f: \|log b_n²(ve^f) − log b_n²(v) − ⟨f, μ_n^v − μ_{n−1}^v⟩\| ≤ ε²; ratio form ≤ 2ε²; \|a_n(ve^f) − a_n(v) − L_n^{a,v}(f)\| ≤ (e^ε − 1 − ε)(b_n + b_{n+1})(v); constants independent of n, p, s, v. Corollary LR-law (pure power): limsup\|log β_n²(w)\| and limsup\|L_n^v(f)\| differ by ≤ ε²; L_n^v(f) → 0 iff the b-law defect of ve^{τf} is o(τ), τ ↓ 0 (§3.11, Plan 40) | LR, LR′, LRa PROVED (internal FV, FVa, TV); LR-law PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); constants numerically sharp (NUMERICAL); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan40.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **Ra** | fixed-size rough weights break the pointwise **a-law**: for all p > 0, s > 1 and ε ∈ (0, ε₀], ε₀ = I/16, some \|f\| ≤ ε gives w = k^{−s}e^{f} with limsup (n^pa_n − 2c(p)) ≥ εη_a/2 and liminf ≤ −εη_a/2, η_a = c(p)I/2, I = (1/π)∫min(1, H(2cos θ))dθ > 0 (≈ 0.314, NUMERICAL). Ingredients: Toda form ȧ_n = ⟨f, b_{n+1}q_nq_{n+1} − b_nq_{n−1}q_n⟩; R2a \|ä_n\| ≤ 2(b_n + b_{n+1})‖f‖²; R1a (explicit, window 2) (§3.12, Plan 41) | PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal FV, FVa, TV, LP/LP′, Sat_p⁺, TL). Sub-labels: Toda form, R2a PROVED; R1a PROVED-mod-cite (via LP′). Rule R ACCEPT WITH FIXES (review/REVIEW_Plan41.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **RL** | Lemma RL: for any σ with infinite support (any nodes x_k ↓ 0) and scales s_n (s_{n+1}/s_n → 1, e.g. n^p): s_na_n → α, s_nb_n → β ⟺ the 1st, 2nd, 4th moments of ν_n := (x ↦ s_nx)_*μ_n tend to those of arcsine on [α−2β, α+2β] ⟺ ν_n → that law weakly + an a priori bound sup s_n(\|a_n\| + b_n) < ∞ (or UI of y⁴). Law P (constant c) ⟺ ν_n → arcsine on [0, 4c] weakly **with sup n^p(a_n + b_n) < ∞** (equivalently: moments ℓ = 1, 2, 4 converge to 2c, 6c², 70c⁴). RL-loc: indices n−1, n, n+1 suffice for right limits; RL-n: index n alone does not (explicit J_t); RL-n2: {n, n+1} does not for moments 1, 2, 4 (general measures); RL-b: the b-law alone is not enough (§3.13, Plan 42) | RL, RL-loc PROVED (self-contained; method of Simon 2004 Thm 3.2, read and quoted, CITATIONS.md (Simon), attribution only); RL-n, RL-b, RL-n2 PROVED (spectral theorem for compact self-adjoint operators: textbook-standard, not checked against a specific source); RL2 PROVED-mod-cite (inherits Theorem R); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan42.md), fixes applied, re-check ACCEPT — REVIEWED; novelty not claimed (RL, RL-b), UNCHECKED (RL-loc, RL-n, RL-n2). Open: weak convergence without the bound (RL-UI) |
| **B-cond** | for x_k = k^{−p} (p > 0), w = k^{−s}Ψ (s > 1) with Ψ **slowly varying in sequence form only** (no boundedness, no D(γ) < ∞; e.g. exp(√log k)): explicit bounds (the displayed bounds are unconditional) \|log b_n²(w) − log b_n²(v)\| ≤ 2δ_n(M₀) + Q_n + o(1), n^p\|a_n(w) − a_n(v)\| ≤ 4M₀^p(2δ_n(M₀) + Q_n) + o(1); hence **QL** (ε_nΛ_n → 0, Λ_n := sup_t max_{m∈{n−1,n}}Σ_{n≤k≤n^γ}log(k/n)μ_m^{(t)}(k), γ > κ) ⇒ n^pb_n → c(p), n^pa_n → 2c(p) along the full sequence. Internal: L0 (dyadic chaining/Potter), FV⁺ (FV/FVa for unbounded f), QLb (power tail ⇒ QL) — PROVED (§3.14, Plan 44) | CONDITIONAL (QL₀, implied by QL; both HYPOTHESIS) + PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b; internal L0, FV⁺, Sat_p⁺, TLw); L0, QLb PROVED; FV⁺ PROVED (standard extension; novelty not claimed); QL proved only in cases already covered (ε_n log n → 0 ⊂ T3-log; bounded Ψ); no new case of the law; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan44.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED |
| **CB / QL-CB** | Route I′ (outline_B_sv §5): boundary-flux identities X_A = Σ_{A×A^c}q_mK_mq_m(f(l)−f(k)) and d/dt μ_m(A) = flux of K_m+K_{m+1} (BF), X_A = ∫_A R_m dμ_m with R_m = P_m/p_m (RF); TV for unbounded f (TV⁺); free (Toeplitz) model: commutator = ½ covariance exactly, X/μ(A) = (ε/p)Cl₂(φ)/φ (FM; log M in CB sharp in the free model, HEURISTIC for μ_m^{(t)}, NUMERICAL support); dyadic block bound (DB); Nishida–Ovsyannikov lemma (NO); **Theorem QL-CB**: CB with a small constant η ≤ η₀(p,s,α,a) along vΨ^t ⇒ QL-b (any α < min(p/2, s−1)) ⇒ QL ⇒ full pointwise Law P for every sequence-form slowly varying Ψ; **Theorem B-OD**: two block bounds (OD-E, OD-F) ⇒ CB ⇒ law. CB itself NOT proved (§3.18, Plan 49) | TV⁺ PROVED (standard extension); BF, RF, DB, NO PROVED; FM (i)–(iii) PROVED, model reading HEURISTIC; QL-CB CONDITIONAL (CB(η, a), η ≤ η₀(p,s,α,a)) + PROVED-mod-cite (inherits QLP §3.16: RH_px, RH₁(r), RH_plt1b, KMVV (6.23), Vanlessen (4.27), DLMF 10.25.2/10.32.4/10.32.9 via Lemma BK; B-cond: RH_px, RH₁(r), RH_plt1b); B-OD CONDITIONAL (OD-E, OD-F); CB-ob HEURISTIC/OBSTRUCTION; numerics NUMERICAL; no new case of the law (cross-ref. Plan 48, §3.17, in review: law for p > 1, 1 < s < 1 + 2p without QL); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan49.md), fixes applied — REVIEWED; novelty UNCHECKED |
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

*(Plan 47 note, 2026-10-14: G2 B*(iii) now uses G2 Lemma EP instead of (P), so Lemma WC, Theorem CL and A4′ are PROVED
(no external citation); proofs unchanged; relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED. Header kept as history; §0 carries the current labels.)*

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

### 3.2 (T3) for rough weights: first variation and counter-evidence (Plan 28) — FV PROVED (standard); Conjecture R NUMERICAL (modified forms proved: §3.6, §3.10); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan28.md), fixes applied, re-check ACCEPT — REVIEWED

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

**Conjecture R** (stated for p = s = 2, which is all the numerics test). **Proved for all p > 0, s > 1, in a modified form, as Theorem R (§3.6):** ε ≤ ε₀, non-explicit η, and windows [θN, N^{κ+1}] in place of [0.6N, 1.6N]. The [0.6N, 1.6N] form would need localization at scale Mn and remains NUMERICAL (F2) (as of Plan 33; superseded by Plan 39 for ε ≤ ε₀). *(Plan 39, 2026-10-14: the window form, including [0.6N, 1.6N] for every p > 0, s > 1, is now proved for ε ≤ ε₀ (explicit) with separation N_{i+1}/N_i → ∞ or a fixed explicit ratio — Theorem RW, §3.10, PROVED-mod-cite, Rule R ACCEPT WITH FIXES, re-check ACCEPT — REVIEWED. The bound for every ε > 0 with absolute c, and ×4 separation, remain NUMERICAL.)* For every ε > 0 there is f with |f| ≤ ε,
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

*(Plan 47 note, 2026-10-14: G2 B*(iii) now uses G2 Lemma EP instead of (P), so Lemma TC is PROVED (no external
citation) and T3-avg is PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b) without (P); proofs unchanged; relabel Rule R ACCEPT WITH FIXES (research/G2/review/REVIEW_Plan47.md), fixes applied — REVIEWED.)*

Setting: x_k = k^{−p} (p > 0), sandwiched weights c·k^{−s} ≤ w_k ≤ C·k^{−s} (s > 1); notation μ_n, ρ_m as in
§3.2–3.5.

**Lemma TC (tail count).** For each fixed M ≥ 2 and all m,

  𝔼_m#(S ∩ (Mm, ∞)) ≤ (2A/(p log M))·m + o(1),

with A := 4p + 2|κ_p| (G2 A-U, using E_p = κ_p from G2 B*(iii)). The o(1) depends on M, p and the sandwich constants
(c, C, s) only.

*Proof.* Let T_j denote the Heine mass of index sets with exactly j elements beyond Mm.
- G2 Theorem A-U (with its M, valid for every p > 0) gives log T_j ≤ −pm²log m + E_pm² + m²(At − pt²log M)
  + O_M(m log m), with t = j/m. The constants depend on the weights only through W = Σw.
- G2 B*(iii) gives E_p = κ_p (this is where the external citation (P) entered; since Plan 47, 2026-10-14, B*(iii) uses
  G2 Lemma EP and no citation).
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

### 3.10 Theorem RW (Plan 39): Conjecture R in window form, for ε ≤ ε₀ — Lemma u_s PROVED; LP-w, R1W PROVED-mod-cite; RW PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan39.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED

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

**Lemma u_s (PROVED; internal input G2 B*(i), whose proof is a direct density computation and does not use (P)).** u_s(p) < 1 for every p > 0. Hence every window with b ≥ 1 is admissible; in particular [0.6, 1.6]
is admissible for every p > 0.

*Proof.* By G2 B*(i), μ*_u has density 1 on (0, u_s], so μ*_u((0, u_s]) = u_s. In the x-variable, u ≤ u_s is
x ≥ 4c. μ* is a probability measure, so u_s = 1 − μ*((0, 4c)). Finally μ*((0, 4c)) > 0: μ* = ∫_0^1ω_{β_t}dt, and
for t ∈ [½, 1] the arcsine law ω_{β_t} on [0, β_t] (distribution function (2/π)arcsin√(y/β_t), no atoms) gives
mass (2/π)arcsin√(4c/β_t) = (2/π)arcsin(t^{p/2}) ≥ (2/π)arcsin(2^{−p/2}) > 0 to [0, 4c) (β_t = 4ct^{−p}). So
μ*((0, 4c)) ≥ ½·(2/π)arcsin(2^{−p/2}) > 0. ∎ (Numerically u_s = 0.375, 0.5, 0.637, 0.763 for p = 0.5, 1, 2, 4; the formula
u_s = 2I(p)/π of G2 B*(i) is not needed.)

**Lemma LP-w (weak form of Lemma LP; PROVED-mod-cite, as Lemma LP: RH_px, RH₁(r), RH_plt1b).** Let ν_n be the image of μ_n^v under x ↦ n^px. Then ν_n → ν weakly as
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
let s_i be the pointwise sign function s_i(k) := sign(Δ²μ_{m_i}^v(k)) ∈ {±1} (with sign 0 := +1), and set

  f(k) := ε·Σ_i s_i(k)·1_{W_i}(k),  w := v·e^{f}.

Then for every ε ∈ (0, ε₀]: |f| ≤ ε, f is supported on ∪_iW_i, e^{−ε}k^{−s} ≤ w_k ≤ e^{ε}k^{−s}, and

  (A): liminf_i F_{m_i}(w) ≥ εη_W/2;  (B): liminf_i F_{m_i}(w) ≥ εη_W/4.

Consequently, with β_n := n^pb_n/c(p), limsup_n log(β_n²/β_{n−1}²) ≥ εη_W/2 (resp. εη_W/4), and in the
normalisation of Conjecture R (§3.2)

  limsup_n (β_n/β_{n−1} − 1) ≥ e^{εη_W/4} − 1 ≥ εη_W/4  (A);  ≥ e^{εη_W/8} − 1 ≥ εη_W/8  (B).

(The spikes are one-signed, F_{m_i}(w) > 0, so no 1 − e^{−x} loss occurs; review F1.) So β_n does not converge, (T3) fails for w (as in Theorem R), and so does the pointwise b-law. H_all still holds for w, and so does
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
   Finally log(β_m²/β_{m−1}²) = F_m(w) + 2p·log(m/(m − 1)) and the last term → 0 (sign corrected, review F2). Hence
   liminf_i log(β_{m_i}/β_{m_i−1}) ≥ c′/2 with c′ as below, i.e. β_{m_i}/β_{m_i−1} − 1 ≥ e^{c′/2} − 1 − o(1) ≥ c′/2 − o(1),
   which is the Conjecture-R normalisation stated in the theorem. If β_n converged to a positive
   limit, then log(β_n²/β_{n−1}²) → 0, which is false; in particular β_n ↛ 1, i.e. the pointwise b-law fails. Let
   c′ := εη_W/2 in case (A) and εη_W/4 in case (B). Then |β_{n+1}/β_n − 1| ≥ 1 − e^{−c′/2} − o(1) for infinitely many
   n, and for n ≥ 1/δ the index n + 1 lies in [n, (1 + δ)n]. So ω(δ) ≥ 1 − e^{−c′/2} > 0 for every δ > 0, and (T3)
   fails. ∎

**Corollary RW′ (the [0.6N, 1.6N] form).** For every p > 0 and s > 1 the window [0.6N, 1.6N] is admissible (Lemma
u_s). So Theorem RW holds with W_i = ℕ ∩ [0.6N_i, 1.6N_i], spikes at m_i ∈ [N_i − J_W + 1, N_i], ε₀ = η_W/16 and
η_W = η_{[0.6,1.6]}(p), under either separation (A) N_{i+1}/N_i → ∞ or (B) N_{i+1} > R_WN_i. For p = s = 2 this is
Conjecture R (§3.2) restricted to ε ≤ ε₀ ≈ 6.1·10⁻⁹: limsup_n |β_n/β_{n−1} − 1| ≥ cε with c = η_W/4 ≈ 2.5·10⁻⁸ in
case (A) and c = η_W/8 ≈ 1.2·10⁻⁸ in case (B) (Conjecture R's normalisation); the constant for |log(β_n²/β_{n−1}²)|
is η_W/2 (A), η_W/4 (B). *(Corrected by review F1; the first version quoted η_W/2 as Conjecture R's c.)*

**What is and is not proved (Conjecture R as stated in §3.2).**
- PROVED-mod-cite: the window form, for every admissible window (including [0.6N, 1.6N] for all p > 0, s > 1), with
  separation N_{i+1}/N_i → ∞ or a fixed explicit ratio R_W, for ε ≤ ε₀ (explicit), with an explicit c that
  depends only on (p, a, b): η_W/2 (A) / η_W/4 (B) for log(β_n²/β_{n−1}²), and η_W/4 (A) / η_W/8 (B) for
  |β_n/β_{n−1} − 1| (Conjecture R's normalisation).
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
- **RW-d (admissibility is necessary for this mechanism).** If b ≤ u_s then μ_m^v(W_N) → 0 for m − N = O(1): by
  LP-w, since the arcsine law ν has no mass beyond 4c and no atom at 4c, and the image of W_N lies in
  [(m/(bN))^p, ∞) with (m/(bN))^p → b^{−p} ≥ 4c. This is exponentially fast only when b < θ₀(p), the zero of g_p⁺
  (Sat_p⁺; θ₀ ≈ 0.056, 0.218, 0.315, 0.427 for p = 0.5, 1, 2, 4, strictly below u_s); for θ₀ ≤ b ≤ u_s it is only
  o(1). Either way ‖Δ²μ_m^v|_{W_N}‖₁ ≤ 4 max_{m′∈{m,m−1,m−2}} μ_{m′}^v(W_N) → 0, c_W = 0, and the first-order gain
  vanishes. *(Corrected by review F3; the first version claimed exponential decay for all b ≤ u_s.)*
- **RW-e (Rule A pass).** Attempts: (1) sign(0) convention: irrelevant, since ⟨f_i, Δ²μ⟩ = ε‖Δ²μ|_W‖₁ either way.
  (2) The moving window in R1W step 4 is handled by h ≤ 1_S, with no continuity-set argument needed for the lower
  bound. (3) Distinctness of the m_i is not needed: each i is treated separately, and only m_i ≥ N_i − J_W + 1 → ∞ is
  used (for F_{m_i}(v) → 0, the head bound and Lemma LP). (4) Off-by-one in step 1 of R1W: Δ²μ_j is needed for j ∈ [N − J + 1, N] only, which is exactly
  the hypothesis. (5) Index convention of FV/F_m checked numerically against a finite difference (`check_rw.out` [0],
  9 digits). (6) R2 is used with its stated constant 16; its proof gives 8, which would allow ε₀ = η_W/8 (review F7: no change made).
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

### 3.11 Lemma LR (Plan 40): linear response of log b_n² and a_n with an explicit ε² remainder — LR, LR′, LRa PROVED (self-contained; internal: FV, FVa, TV; §3.5 step 3 only as a cross-check); Corollary LR-law PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); sharpness of the constants NUMERICAL; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan40.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED

Setting (general, no pure-power hypothesis). The atoms x_k (k in a countable index set) are distinct reals, v_k > 0,
and v has finite moments, Σ_k v_k|x_k|^j < ∞ for all j. f is a bounded real sequence on the atoms, and
w(t) := v·e^{tf} (t ∈ [0, 1]), w := w(1). Put

  ε := ½ osc f = ½(sup f − inf f),  c := ½(sup f + inf f),  g := f − c,  so |g| ≤ ε (and ε ≤ ‖f‖_∞).

Notation as in §3.5–3.8: q_j = √w p_j ∈ ℓ²(atoms) (orthonormal), μ_j = q_j², K_m = Σ_{j<m}q_jq_jᵀ (orthogonal
projection onto span{q_0, …, q_{m−1}}), a_n = ⟨xq_n, q_n⟩, b_n = ⟨xq_{n−1}, q_n⟩ (b_0 := 0), all at the weight w(t)
unless a superscript says otherwise. For the indices used, the measure has at least n + 2 atoms (so D_{n+2} > 0 and
q_0, …, q_{n+1} exist). Define the **linear responses at the base v**

  L_n^v(f) := ⟨f, μ_n^v − μ_{n−1}^v⟩ (n ≥ 1),  L_n^{a,v}(f) := ⟨(x − a_n^v)f, μ_n^v⟩ − 2b_n^v⟨f, q_{n−1}^vq_n^v⟩ (n ≥ 0),

i.e. the t-derivatives at t = 0 of log b_n² and a_n (Lemmas FV, FVa). Both are linear in f and vanish on constants.

**Lemma LR (linear response).** For every n ≥ 1, every v and f as above,

  |log b_n²(w) − log b_n²(v) − L_n^v(f)| ≤ ∫_0^1(1 − t)[Var_{μ_n^{(t)}}(f) + Var_{μ_{n−1}^{(t)}}(f)] dt ≤ ε².

More precisely, |(d²/dt²) log b_n²(w(t))| ≤ Var_{μ_n^{(t)}}(f) + Var_{μ_{n−1}^{(t)}}(f) ≤ 2ε² for every t ∈ [0, 1].

**Lemma LR′ (ratio form; sharpens R2).** For N ≥ 2, with F_N := log(b_N²/b_{N−1}²) and Δ²μ_N := μ_N − 2μ_{N−1} + μ_{N−2},
|(d²/dt²)F_N| ≤ 4ε² and |F_N(w) − F_N(v) − ⟨f, Δ²μ_N^v⟩| ≤ 2ε².

**Lemma LRa (a_n version).** For every n ≥ 0, |(d²/dt²) a_n(w(t))| ≤ ε²(b_n^{(t)} + b_{n+1}^{(t)}) for every t, and

  |a_n(w) − a_n(v) − L_n^{a,v}(f)| ≤ (e^{ε} − 1 − ε)(b_n(v) + b_{n+1}(v)) ≤ ½ε²e^{ε}(b_n(v) + b_{n+1}(v)).

**The constants.** C = 1 in LR (in units of ε = ½ osc f; the outline's 2 is also valid), 2 in LR′, and the factor in
LRa, are absolute: they do not depend on n, on p or s, on the nodes, or on v (only finite moments are used). For pure
powers x_k = k^{−p}, LRa's bound is ≤ (e^ε − 1 − ε)·2c(p)n^{−p}(1 + o(1)) ≤ (1 + o(1))ε²e^{ε}c(p)n^{−p}, the natural
scale of a_n (F5).

*Proof.* **0. Reductions and regularity.**
- Multiplying a weight by a positive constant does not change q_j, μ_j, a_j, b_j. Since ve^{tf} = e^{tc}·ve^{tg},
  all these quantities are the same along the paths ve^{tf} and ve^{tg}; also L_n^v(f) = L_n^v(g) and
  L_n^{a,v}(f) = L_n^{a,v}(g) (both vanish on constants: Σμ_n = Σμ_{n−1} = 1; FVa's invariance). So assume f = g,
  |f| ≤ ε.
- **Uniformity in t.** w(t + h) = w(t)e^{hf}, and w(t) is again a weight with finite moments (w(t) ≤ e^{ε}v after the
  reduction). So every derivative bound proved below "at t = 0 for an arbitrary finite-moment base v" holds at every
  t ∈ [0, 1] with the same ε. All bounds below are of this form; nothing depends on t except through the base.
- **Smoothness.** D_m(t) = Σ_{|S|=m}Π_{k∈S}w_k(t)V(S) (Heine, as in Lemma FV) is C^∞: the r-th t-derivative of the
  S-term is ≤ (m‖f‖_∞)^r e^{m‖f‖_∞}Π_{k∈S}v_kV(S), uniformly in t ∈ [0, 1], so dominated convergence applies (F5). Likewise
  √w(t)x^j = √v e^{tf/2}x^j is C^∞ as an ℓ²-valued map (its r-th derivative is (f/2)^r√w(t)x^j, of ℓ²-norm
  ≤ (‖f‖_∞/2)^r e^{‖f‖_∞}m_{2j}(v)^{1/2}), so q_0, …, q_{n+1} (Gram–Schmidt of finitely many such vectors) are C^∞, as
  in the proof of Lemma TV, which used x_k ≤ 1 only for this step. Hence log b_n², a_n, μ_m and γ_m below are C^∞ in t.
- **Taylor.** For a C² function φ on [0, 1], φ(1) − φ(0) − φ′(0) = ∫_0^1(1 − t)φ″(t)dt.

**1. First and second derivatives (FV + TV; F2).** Put α_m := ⟨f, μ_m⟩ = ⟨fq_m, q_m⟩. By Lemma FV,
(log b_n²)′ = α_n − α_{n−1}. By step 0, Lemma TV's formula q̇_m = ½fq_m − K_m(fq_m) − ½α_mq_m holds in the present
general setting (its proof uses only orthonormality and the C¹ property of step 0). Hence

  ΔV_m := α_m′ = 2⟨fq_m, q̇_m⟩ = ‖fq_m‖² − 2⟨fq_m, K_m(fq_m)⟩ − α_m² = A_m + B_m,  (d²/dt²)log b_n² = ΔV_n − ΔV_{n−1},

with

  A_m := −2⟨fq_m, K_m(fq_m)⟩ = −2‖K_m(fq_m)‖²,  B_m := ‖fq_m‖² − α_m² = Var_{μ_m}(f)

(K_m is an orthogonal projection, so ⟨u, K_mu⟩ = ‖K_mu‖²). This is the main proof of the formula for ΔV_m; it does not
use the Heine two-point function.

*Cross-check (Heine route, as in Lemma R2).* With L_m := log D_m and the Heine ensemble P_m (Lemma FV),
L_m′ = ⟨f, ρ_m⟩ and L_m″ = Var_m⟨f, X⟩ =: V_m (differentiate the normalised tilted sum once more; same domination), and
since ρ_{m+1} − ρ_m = μ_m, ΔV_m = V_{m+1} − V_m. By §3.5 step 3, V_m = ½Σ_{k,l}(f_k − f_l)²K_m(k,l)², and the rank-one
update K_{m+1} = K_m + q_mq_mᵀ gives the same A_m + B_m (the f_k² and f_l² parts of A_m vanish because K_mq_m = 0;
B_m = ½Σ(f_k − f_l)²μ_m(k)μ_m(l)). §3.5 step 3 is stated in the pure-power setting, but its input — the Gram/Sylvester
proof of G3′ Lemma H with the Heine identification — uses only the Gram form of D_m, so it holds for any finite-moment
measure on distinct real atoms.

**2. Bessel's inequality in place of R2's crude bounds.**
- **Bessel.** q_m is orthogonal to the range of K_m, so fq_m = K_m(fq_m) + α_mq_m + r with the three terms pairwise
  orthogonal. Hence ‖K_m(fq_m)‖² ≤ ‖fq_m‖² − α_m² = B_m. (Only Bessel, not Parseval, is used: completeness of
  {q_j} in ℓ² is not assumed.)
- So ΔV_m = B_m − 2‖K_m(fq_m)‖² ∈ [−B_m, B_m], i.e. **|ΔV_m| ≤ Var_{μ_m}(f) ≤ ‖fq_m‖² = Σ_kf_k²μ_m(k) ≤ ε².**
- Hence |(d²/dt²)log b_n²| ≤ B_n + B_{n−1} ≤ 2ε², and |F_N″| = |ΔV_N − 2ΔV_{N−1} + ΔV_{N−2}| ≤ 4ε².

**3. LR and LR′.** By Lemma FV, (d/dt)log b_n²|_{t=0} = L_n^v(f) and (d/dt)F_N|_{t=0} = ⟨f, Δ²μ_N^v⟩. Taylor (step 0)
and step 2 at every t (uniformity, step 0) give LR, since ∫_0^1(1 − t)·2ε² dt = ε², and LR′, since
∫_0^1(1 − t)·4ε² dt = 2ε².

**4. LRa: the first derivative in Lax form.** Put γ_m := ⟨fq_m, q_{m+1}⟩. The recurrence
xq_n = b_{n+1}q_{n+1} + a_nq_n + b_nq_{n−1} holds at every atom, so ⟨(x − a_n)f, μ_n⟩ = ⟨fq_n, (x − a_n)q_n⟩ =
b_{n+1}γ_n + b_nγ_{n−1}, and Lemma FVa becomes

  a_n′ = b_{n+1}γ_n − b_nγ_{n−1}  (the term b_nγ_{n−1} is absent for n = 0).

(For f = x this is the Toda form b_{n+1}² − b_n².) Also, by Lemma FV, b_m′ = ½(α_m − α_{m−1})b_m, so
**|(d/dt)log b_m| ≤ ε** and b_m(t) ≤ e^{εt}b_m(0).

**5. LRa: the derivative of γ_n.** Lemma TV's proof gives q̇_m = ½fq_m − K_m(fq_m) − ½α_mq_m (valid for f = g as well:
the c-terms cancel). Put u := fq_n, u′ := fq_{n+1}, P := I − K_{n+2}, S_n := ⟨K_nu, K_nu′⟩, R_n := ⟨Pu, Pu′⟩.
- ⟨fq̇_n, q_{n+1}⟩ = ⟨q̇_n, u′⟩ = ½⟨u, u′⟩ − S_n − ½α_nγ_n (using ⟨K_nu, u′⟩ = ⟨K_nu, K_nu′⟩ and ⟨q_n, u′⟩ = γ_n).
- ⟨fq_n, q̇_{n+1}⟩ = ⟨u, q̇_{n+1}⟩ = ½⟨u, u′⟩ − ⟨u, K_{n+1}u′⟩ − ½α_{n+1}γ_n, and
  ⟨u, K_{n+1}u′⟩ = S_n + ⟨u, q_n⟩⟨q_n, u′⟩ = S_n + α_nγ_n.
- Decomposing along range K_n, q_n, q_{n+1} and range P (pairwise orthogonal; ⟨u, q_n⟩ = α_n, ⟨u, q_{n+1}⟩ = γ_n,
  ⟨u′, q_n⟩ = γ_n, ⟨u′, q_{n+1}⟩ = α_{n+1}): ⟨u, u′⟩ = S_n + α_nγ_n + γ_nα_{n+1} + R_n.
- Adding: **γ_n′ = R_n − S_n + ½(α_{n+1} − α_n)γ_n.**

**6. LRa: the bound.** By steps 4–5,

  a_n″ = b_{n+1}Γ_n − b_nΓ_{n−1},  Γ_m := γ_m′ + ½(α_{m+1} − α_m)γ_m = R_m − S_m + (α_{m+1} − α_m)γ_m.

Claim: |Γ_m| ≤ ε². By Cauchy–Schwarz twice (in ℓ², then in ℝ²),
|R_m − S_m| ≤ ‖Pu‖‖Pu′‖ + ‖K_mu‖‖K_mu′‖ ≤ (‖Pu‖² + ‖K_mu‖²)^{1/2}(‖Pu′‖² + ‖K_mu′‖²)^{1/2}. By the orthogonal
decomposition of step 5 (with m in place of n), ‖Pu‖² + ‖K_mu‖² = ‖u‖² − α_m² − γ_m² ≤ ε² − α_m² − γ_m² (as
‖u‖² = Σf²μ_m ≤ ε²), and likewise ‖Pu′‖² + ‖K_mu′‖² ≤ ε² − α_{m+1}² − γ_m². By AM–GM,
|R_m − S_m| ≤ ε² − γ_m² − ½(α_m² + α_{m+1}²). Also |(α_{m+1} − α_m)γ_m| ≤ |γ_m|(|α_m| + |α_{m+1}|) ≤
γ_m² + ¼(|α_m| + |α_{m+1}|)² ≤ γ_m² + ½(α_m² + α_{m+1}²). Adding, |Γ_m| ≤ ε². Hence
|a_n″(t)| ≤ ε²(b_n^{(t)} + b_{n+1}^{(t)}) ≤ ε²e^{εt}(b_n(v) + b_{n+1}(v)) (step 4), and Taylor gives
|a_n(w) − a_n(v) − L_n^{a,v}(f)| ≤ ε²(b_n + b_{n+1})(v)∫_0^1(1 − t)e^{εt}dt = (e^ε − 1 − ε)(b_n + b_{n+1})(v),
with a_n′(0) = L_n^{a,v}(f) by Lemma FVa. Finally e^ε − 1 − ε = Σ_{r≥2}ε^r/r! ≤ ½ε²e^ε. ∎

**Corollary LR-law (the b- and a-laws to accuracy ε²).** Let x_k = k^{−p} (p > 0), v = k^{−s} (s > 1), f bounded with
ε = ½ osc f (e.g. |f| ≤ ε), w = ve^{f}, β_n(w) := n^pb_n(w)/c(p). Then for all n ≥ 1

  log β_n²(w) = L_n^v(f) + r_n + δ_n,  |r_n| ≤ ε²,  δ_n := log β_n²(v) → 0 (independent of f),

  n^pa_n(w)/(2c(p)) − 1 = n^pL_n^{a,v}(f)/(2c(p)) + r_n^a + δ_n^a,  |r_n^a| ≤ (e^ε − 1 − ε)n^p(b_n + b_{n+1})(v)/(2c(p)),
  δ_n^a := n^pa_n(v)/(2c(p)) − 1 → 0, and limsup_n |r_n^a| ≤ e^ε − 1 − ε ≤ ½ε²e^ε.

Consequently:
- (i) |limsup_n |log β_n²(w)| − limsup_n |L_n^v(f)|| ≤ ε². In particular, if L_n^v(f) → 0 then
  limsup_n |log β_n²(w)| ≤ ε²; and if the b-law n^pb_n(w) → c(p) holds then limsup_n |L_n^v(f)| ≤ ε².
- (ii) **Exact form along rays.** Put E(f) := limsup_n |log β_n²(ve^{f})| and Λ(f) := limsup_n |L_n^v(f)| (a
  seminorm, by linearity of L_n^v; finite, since |L_n^v(f)| = |⟨f − c, μ_n − μ_{n−1}⟩| ≤ 2ε, so Λ(f) ≤ 2ε; F3). For every τ > 0, |E(τf) − τΛ(f)| ≤ τ²ε². Hence Λ(f) = lim_{τ↓0}E(τf)/τ, and
  **L_n^v(f) → 0 if and only if the b-law defect of ve^{τf} is o(τ) as τ ↓ 0** (then E(τf) ≤ τ²ε² for every τ > 0).
- (iii) **The a-analogue (F3).** Put E^a(f) := limsup_n |n^pa_n(ve^{f})/(2c(p)) − 1| and
  Λ^a(f) := limsup_n n^p|L_n^{a,v}(f)|/(2c(p)). By step 4, L_n^{a,v}(f) = b_{n+1}γ_n − b_nγ_{n−1} with |γ_m| ≤ ε, so
  n^p|L_n^{a,v}(f)|/(2c(p)) ≤ ε·n^p(b_n + b_{n+1})(v)/(2c(p)) → ε, and Λ^a(f) ≤ ε. Then
  |E^a(f) − Λ^a(f)| ≤ e^ε − 1 − ε ≤ ½ε²e^ε, and along rays |E^a(τf) − τΛ^a(f)| ≤ e^{τε} − 1 − τε = O(τ²); so
  L_n^{a,v}(f)n^p → 0 iff E^a(τf) = o(τ) as τ ↓ 0.
- The same statements hold for any base v for which the b-law (resp. a-law) is known, with δ_n, δ_n^a the base's
  defects: e.g. v = k^{−s}Ψ under the hypotheses of T3-all or T3-log.

*Proof.* Apply LR and LRa with base v. δ_n → 0 and δ_n^a → 0 are the pure-power laws n^pb_n(v) → c(p) and
n^pa_n(v) → 2c(p) (RH_px for p > 1, RH₁(r) for p = 1, RH_plt1b for 0 < p < 1; via a_n/(2b_n) = 1 + O(1/n)); they
also give n^p(b_n + b_{n+1})(v) → 2c(p), whence limsup|r_n^a| ≤ e^ε − 1 − ε. (i): |log β_n²(w) − L_n^v(f)| ≤ ε² + |δ_n|;
take limsups. (ii): apply (i) to τf, whose osc-radius is τε, and use L_n^v(τf) = τL_n^v(f). (iii): the same with LRa. ∎

**What LR does not give (gaps, stated precisely).**
- **No exact characterisation for a fixed f.** (ii) is exact only along rays τf, τ ↓ 0. For a fixed f with
  ε > 0, LR leaves an ε²-band: L_n^v(f) → 0 gives only limsup|log β_n²(w)| ≤ ε², and conversely. The statement
  "for |f| ≤ ε ≤ ε₁, the b-law holds iff L_n^v(f) → 0" is **not proved** (it would need the second-order term
  ∫(1 − t)(ΔV_n − ΔV_{n−1})dt to tend to 0 whenever the first-order one does; outline_C_rough §2.5 T7b).
- **Sharpness of the constants (NUMERICAL; F1).** C = 1 in LR, 2 in LR′ and the factor (e^ε − 1 − ε)(b_n + b_{n+1})
  in LRa are numerically sharp in the general finite-moment class: the Rule R reviewer's adversarial hill-climb on 2–5-atom
  measures reaches ratio 1.0000 (LR, n = 1, 3 atoms), 0.993 (LR′, n = 2, 5 atoms) and 0.9999 (LRa, n = 0, 2 atoms), and
  the pointwise inequality |(log b_n²)″| ≤ Var_{μ_n}(f) + Var_{μ_{n−1}}(f) to 0.9995 (review/REVIEW_Plan40.md); our own
  exhaustive sign search ([3]) reaches 0.986 (LR), 1.889/2 (LR′, n ≥ 2) and 0.887 (LRa). No proof of optimality
  of the integrated constants is given.
  - *Pointwise LRa constant attained (proved).* Two atoms ±1, n = 0, weights ∝ (e^{θ}, e^{−θ}): a_0 = tanh θ,
    b_1 = sech θ, and f = ±ε on the two atoms moves θ at rate ε, so |a_0″| = 2ε²|tanh θ|sech²θ = ε²b_1·(2|sinh θ|/cosh²θ),
    which equals ε²(b_0 + b_1) at sinh θ = ±1. So the constant 1 in |a_n″| ≤ ε²(b_n + b_{n+1}) cannot be lowered.
  - For the pure powers the observed ratios are smaller: ≤ 0.53 (LR), 0.61 (LR′), 0.19 (LRa) (p = s = 2 and p = 1, s = 2,
    n ≤ 200).
- **The pure-power linear response L_n^v itself is not analysed here** (its locality, size and oscillation; outline
  SOC/FJ). LR only reduces the law for |f| ≤ ε to that linear functional, up to ε².

**Rule A (adversarial pass, logged).**
- *Small cases.* Exhaustive sign patterns f ∈ {±ε}^K on random measures with K = 4–6 atoms (random nodes in [−1, 1],
  weights in [0.05, 1]), every n ≤ K − 3, ε ∈ {1, 0.05}: 13000 cases (0 skipped), max |R_b|/ε² = 0.986 ≤ 1,
  max |R_F|/ε² = 1.889 ≤ 2 (n ≥ 2) and max |R_a|/bound = 0.887 ≤ 1 ([3]). No counterexample.
- *Degenerate parameters.* m = 0 in step 2: K_0 = 0, so A_0 = 0 and ΔV_0 = B_0 ∈ [0, ε²]; consistent. n = 0 in LRa:
  b_0 = 0, so only Γ_0 enters. Constant f: ε = 0 and both sides vanish (scale invariance, step 0).
- *"The cross term vanishes."* A_m's f_k² terms vanish by K_mq_m = 0 (q_m ⊥ range K_m), not by symmetry; checked.
  In step 5 every inner product was expanded along the orthogonal decomposition range K_m ⊕ ⟨q_m⟩ ⊕ ⟨q_{m+1}⟩ ⊕ range P,
  with no completeness assumption (non-dense polynomials only enlarge range P).
- *Converse.* Not used.
- *Formula checks.* The Var-difference formula for g″(t) agrees with a central second difference to 5 digits at
  t = 0, 0.5, 1 ([2]); this also tests the uniformity of step 0 along the path (max_t |g″(t)|/ε² = 0.43 ≤ 2).

**Numerics** (NUMERICAL; `checks/check_lr.py` / `.out`; float64 Lanczos with full reorthogonalization, K = 20n atoms;
the lemma is exact for the truncated measure, so truncation does not enter the inequality tested).
- [1] p = s = 2 (n = 50, 100, 200) and p = 1, s = 2 (n = 50, 100); random f (uniform, random signs) and adversarial f
  (sign(μ_n − μ_{n−1}), its restriction to [0.6n, 1.6n], and sign power iteration on the Hessian of log b_n²), at
  ε = 0.4, 0.2, 0.1, 0.05, 0.025. Worst ratios: |R_b|/ε² = 0.53 (≤ 1), |R_F|/ε² = 0.61 (≤ 2), |R_a|/bound = 0.19 (≤ 1).
  The ratios R_b/ε² are nearly constant in ε (≈ ½g″(0)/ε², as Taylor predicts) and do not grow with n.
- [4] Rule N: float64 vs longdouble Lanczos (n = 40, K = 800) agree on R_b/ε² to 1·10⁻¹².

**Remarks.**
- **LR-a (relation to R2).** LR′ sharpens Lemma R2's |F_N″| ≤ 16‖f‖²_∞ (8 after F5) to 4ε² ≤ 4‖f‖²_∞, by using Bessel's
  inequality (ΔV_m ≥ −B_m) in place of A ∈ [−2‖f‖², 0], B ∈ [0, 2‖f‖²]. In Theorem R step 2 the loss 8ε² could
  therefore be 2ε² (ε₀ = η/4); §3.6 is left unchanged.
- **LR-b.** LR holds for every finite-moment base, so the outline's continuity method (outline_C_rough §2.4, step (3))
  can apply it at each intermediate weight w(t_i) with remainder h²ε² per step (the outline wrote 2h²G²).
- **LR-c (novelty).** UNCHECKED. Second-order control of Jacobi parameters under weight tilting is close in spirit to
  Toda-flow / perturbation-determinant estimates; no source was read for this plan and none is cited.

### 3.12 Theorem Ra (Plan 41): fixed-size rough weights also break the pointwise a-law — Toda form, R2a PROVED; R1a, Ra PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan41.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED

Setting and notation as in §3.5–3.6 and §3.8: x_k = k^{−p} (p > 0), v_k := k^{−s} (s > 1), w(t) = v·e^{tf} with f
bounded, q_j = √w·p_j ∈ ℓ²(atoms) orthonormal, μ_j = q_j², K_m = Σ_{j<m}q_jq_jᵀ, b_0 := 0, q_{−1} := 0. Conventions of
§3.5: a_n = ⟨xq_n, q_n⟩, b_n = ⟨xq_{n−1}, q_n⟩, and the recurrence holds at every atom:

  x_k q_n(k) = b_{n+1}q_{n+1}(k) + a_n q_n(k) + b_n q_{n−1}(k).   (Rec)

Put E_n := b_{n+1}q_nq_{n+1} (a vector on the atoms; E_{−1} := 0) and ΔE_n := E_n − E_{n−1}. c := c(p), and ν is
the arcsine law on [0, 4c] (Lemma LP), parametrised by y = 2c(1 + cos θ), θ uniform on (0, π).

**Lemma Toda (Toda form of FVa; PROVED, standard, novelty not claimed).** Along w(t) = v·e^{tf},

  (d/dt) a_n = ⟨f, ΔE_n⟩ = ⟨f, b_{n+1}q_nq_{n+1} − b_nq_{n−1}q_n⟩,

and at every atom ΔE_n = (x − a_n)μ_n − 2b_nq_{n−1}q_n = 2E_n − (x − a_n)μ_n.

*Proof.* Multiply (Rec) by q_n(k): (x_k − a_n)μ_n(k) = b_{n+1}q_nq_{n+1}(k) + b_nq_{n−1}q_n(k) = E_n(k) + E_{n−1}(k).
Hence (x − a_n)μ_n − 2b_nq_{n−1}q_n = E_n + E_{n−1} − 2E_{n−1} = ΔE_n, and also = 2E_n − (x − a_n)μ_n. Pairing the first
form with f and comparing with Lemma FVa, (d/dt)a_n = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩ = ⟨f, ΔE_n⟩. ∎
- *Checks.* ⟨1, E_m⟩ = b_{m+1}⟨q_m, q_{m+1}⟩ = 0, so the formula is unchanged by f ↦ f + const (as FVa). For f = x,
  ⟨x, E_m⟩ = b_{m+1}⟨xq_m, q_{m+1}⟩ = b_{m+1}², so ȧ_n = b_{n+1}² − b_n², the Toda flow (FVa step 6).
- *Independent derivation (not used).* T_m := Σ_{j<m}a_j = Tr(XK_m), X := multiplication by x. Range K_m(t) =
  e^{tf/2}·Range K_m(0), so K̇_m = ½[(1 − K_m)fK_m + K_mf(1 − K_m)] and Ṫ_m = Tr(f(1 − K_m)XK_m) = b_m⟨f, q_mq_{m−1}⟩,
  because (1 − K_m)XK_m = b_mq_mq_{m−1}ᵀ by (Rec). Then ȧ_n = Ṫ_{n+1} − Ṫ_n = ⟨f, E_n − E_{n−1}⟩.

NUMERICAL ([1] of `checks/check_ra.out`; p = s = 2, K = 20n, float64): central differences (h = 10⁻⁵) agree with
⟨f, ΔE_n⟩ to relative error ≤ 1.2·10⁻⁸ (n = 20, 60, 150, random f); ⟨f, ΔE_n⟩ and the FVa formula agree to 10⁻²⁰;
the atomwise identity holds to 10⁻¹⁹.

*Cross-reference (F1 of review/REVIEW_Plan41.md).* §3.11 Lemma LRa (Plan 40, REVIEWED and merged before this section; in review on a parallel branch at the time
of writing) contains the same Toda form (its step 4) and the sharper bound |ä_n| ≤ ε²(b_n + b_{n+1}), ε = ½ osc f =
inf_c‖f − c‖_∞, i.e. Lemma R2a below with constant 1 instead of 2; with it, Theorem Ra's step 7 would allow ε₀ = I/8.
This section does not rely on §3.11: R2a and ε₀ = I/16 are proved here independently.

**Lemma R2a (second-order control of a_n; PROVED).** Along w(t) = v·e^{tf}, for every n ≥ 0, every t and every v with
finite moments,

  |(d²/dt²) a_n| ≤ 2(b_n + b_{n+1})·inf_{c∈ℝ}‖f − c‖²_∞,

with b_n, b_{n+1} evaluated at w(t).

*Proof.* Replacing f by f − c multiplies w(t) by e^{−ct}, which leaves q_j, a_j, b_j unchanged; so assume ‖f‖_∞ is
already the infimum. By Lemma Toda, ȧ_n = Φ_n − Φ_{n−1} with Φ_m := ⟨f, E_m⟩ = b_{m+1}⟨q_{m+1}, fq_m⟩ (Φ_{−1} = 0).
All q_j are C^∞ ℓ²-valued in t (proof of Lemma TV), so Φ_m is C¹ and

  Φ̇_m = ḃ_{m+1}⟨q_{m+1}, fq_m⟩ + b_{m+1}(⟨q̇_{m+1}, fq_m⟩ + ⟨q_{m+1}, fq̇_m⟩).

- *ḃ.* Lemma FV: (d/dt) log b_{m+1}² = ⟨f, μ_{m+1} − μ_m⟩, so |ḃ_{m+1}| = ½b_{m+1}|⟨f, μ_{m+1} − μ_m⟩| ≤ b_{m+1}‖f‖_∞.
- *q̇.* By the proof of Lemma TV, q̇_j = ½fq_j − K_j(fq_j) − ½⟨fq_j, q_j⟩q_j. Decompose fq_j = K_j(fq_j) +
  ⟨fq_j, q_j⟩q_j + (1 − K_{j+1})(fq_j) (K_{j+1} = K_j + q_jq_jᵀ). Then q̇_j = ½(1 − K_{j+1})(fq_j) − ½K_j(fq_j), a sum
  of two orthogonal vectors, so ‖q̇_j‖² = ¼(‖(1 − K_{j+1})fq_j‖² + ‖K_jfq_j‖²) ≤ ¼‖fq_j‖² ≤ ¼‖f‖²_∞.
- *Combine.* |⟨q_{m+1}, fq_m⟩| ≤ ‖f‖_∞ and |⟨q̇_{m+1}, fq_m⟩|, |⟨q_{m+1}, fq̇_m⟩| ≤ ½‖f‖²_∞, so
  |Φ̇_m| ≤ b_{m+1}‖f‖²_∞ + b_{m+1}‖f‖²_∞ = 2b_{m+1}‖f‖²_∞. Hence |ä_n| ≤ |Φ̇_n| + |Φ̇_{n−1}| ≤ 2(b_{n+1} + b_n)‖f‖²_∞. ∎

NUMERICAL ([2]): second central differences give |ä_n|/(2(b_n + b_{n+1})‖f‖²_∞) between 0.005 and 0.10 (n = 20, 60,
150; f random ±1, sign(ΔE_n), sign(q_nq_{n+1})); the bound holds with room.

**Definition (the a-kernel constant).** For z ∈ ℝ put

  H(z) := min_{φ∈[0,π]} (|sin 2φ − z cos²φ| + |z sin²φ − sin 2φ|),  I := (1/π)∫_0^π min(1, H(2cos θ)) dθ.

- **H is 1-Lipschitz** (the two terms change by ≤ |z − z′|cos²φ and ≤ |z − z′|sin²φ, uniformly in φ), hence
  continuous, and H ≥ 0.
- **H(z) = 0 iff z ∈ {−2, 0, 2}.** Write u = cos φ, v = sin φ, so the two terms are |u(2v − zu)| and |v(zv − 2u)|. Both
  vanish iff: u = 0 (then v = ±1 and the second term is |z|, so z = 0); or v = 0 (then the first term is |z|, so z = 0);
  or uv ≠ 0, 2v = zu and zv = 2u, whence z²u = 4u, z = ±2 (and φ = ±π/4 mod π gives zero). The minimum over the compact
  φ-interval is attained, so H(z) = 0 iff z ∈ {−2, 0, 2}.
- Hence **I > 0**: θ ↦ min(1, H(2cos θ)) is continuous and ≥ 0 on [0, π], and vanishes only where 2cos θ ∈ {−2, 0, 2},
  i.e. at θ ∈ {0, π/2, π}. (I ≤ 1 trivially.)
- NUMERICAL ([3]): I ≈ 0.3140 (grid quadrature, not certified; the proofs below use only 0 < I ≤ 1).

**Lemma LP′ (weak form of Lemma LP; PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b)).** For the pure power v and each fixed
i ∈ ℤ, the image of μ_{N+i}^v under x ↦ N^px converges weakly (as N → ∞) to the arcsine law ν on [0, 4c(p)].

*Proof (the moment argument of Lemma LP's proof, §3.8).* For fixed j, ∫(N^px)^j dμ_{N+i}^v = N^{pj}(J^j)_{N+i,N+i} is a
finite sum over lattice paths of length j from N + i to N + i, which use only a_m, b_m with |m − N − i| ≤ j. By the
pure-power laws (RH₁(r), RH_p, RH_plt1b), N^pa_m → 2c(p) and N^pb_m → c(p) for each such m (since (m/N)^p → 1). Hence
the j-th moment converges to (J_0^j)_{00}, the j-th moment of ν (LP's proof). ν is compactly supported, hence
determined by its moments, so the method of moments (as quoted in LP's proof) gives weak convergence. ∎

**Lemma R1a (non-degeneracy of the a-response kernel; PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b), via Lemma LP′).** For the
pure power v,

  liminf_{N→∞} (‖N^pΔE_N^v‖₁ + ‖N^pΔE_{N+1}^v‖₁) ≥ 2c(p)·I.

Consequently, with η_a := c(p)I/2, there is N₀ such that every N ≥ N₀ has some m ∈ {N, N + 1} with
‖m^pΔE_m^v‖₁ ≥ η_a.

*Proof.* Fix N and write u := q_N, v′ := q_{N+1} (vectors on the atoms), B := b_{N+1}.
1. **Both differences in the variables (q_N, q_{N+1}).** By Lemma Toda, ΔE_N = 2E_N − (x − a_N)μ_N = 2Buv′ −
   (x − a_N)u². By Lemma Toda at index N + 1, ΔE_{N+1} = (x − a_{N+1})v′² − 2Buv′ (atomwise). Both are exact.
2. **Free comparison.** Put y_k := N^px_k and z_k := (y_k − 2c)/c. Then, atomwise,
   N^pΔE_N = c(2uv′ − zu²) + r_N, N^pΔE_{N+1} = c(zv′² − 2uv′) + r_N′, with
   |r_N| + |r_N′| ≤ τ_N(u² + v′²), τ_N := 2|N^pb_{N+1} − c| + |N^pa_N − 2c| + |N^pa_{N+1} − 2c|
   (using 2|uv′| ≤ u² + v′²). By the pure-power laws (n^pb_n → c(p) and a_n/(2b_n) → 1, hence n^pa_n → 2c(p); RH_px,
   RH₁(r), RH_plt1b) τ_N → 0.
3. **Pointwise lower bound.** |2uv′ − zu²| + |zv′² − 2uv′| is homogeneous of degree 2 in (u, v′), so it is
   ≥ H(z)(u² + v′²) at every atom. Summing, with Σ_k(u_k² + v′_k²) = 2:
   ‖N^pΔE_N‖₁ + ‖N^pΔE_{N+1}‖₁ ≥ c·⟨H(z), μ_N + μ_{N+1}⟩ − 2τ_N ≥ c·⟨min(1, H(z)), μ_N + μ_{N+1}⟩ − 2τ_N.
4. **Weak convergence (Lemma LP′ with i = 0, 1).** The images of μ_N^v and μ_{N+1}^v under x ↦ N^px both converge
   weakly to ν. The test function y ↦ min(1, H((y − 2c)/c)) is bounded and continuous on [0, ∞), so
   ⟨min(1, H(z)), μ_N + μ_{N+1}⟩ → 2∫min(1, H((y − 2c)/c)) dν(y) = 2I (substitute y = 2c(1 + cos θ), so
   (y − 2c)/c = 2cos θ).
5. Steps 3–4 and τ_N → 0 give the liminf ≥ 2cI. So there is N₀ with sum ≥ cI for N ≥ N₀; then one of the two terms
   is ≥ cI/2 = η_a, and ‖m^pΔE_m‖₁ ≥ ‖N^pΔE_m‖₁ for m ≥ N. ∎

*Remarks on R1a.* (i) Unlike Lemma R1 (contradiction, non-explicit η and window J), R1a is direct, with window 2 and an
explicit constant η_a = c(p)I/2 ≈ 0.157c(p) (I NUMERICAL; N₀ not explicit, it comes from the rates in the pure-power
laws). (i′) No information on the joint law of (q_N, q_{N+1}) at the atoms, or on phases, is needed: step 3 is a
deterministic inequality at each atom that depends only on u_k² + v′_k², so only the marginal μ_N + μ_{N+1} enters, and
LP′ (with a bounded continuous test function) controls it. Positivity comes from I > 0, not from an atom-free argument. (ii) The three points {−2, 0, 2} are the same set Z as in
R1 step 3. (iii) HEURISTIC (phase model of `research/program/outline_C_rough.md` §0): ΔE_n ≈ bR_k² sin θ_k sin(2nθ_k +
2φ_k), which predicts ‖n^pΔE_n^v‖₁ → 8c(p)/π² ≈ 0.81c(p) on average; observed ([3]) 0.77–0.87·c(p) for p = 2, 1, 0.5.

**Theorem Ra.** Let p > 0, s > 1, v = k^{−s}, and let I, η_a = c(p)I/2 be as above. Put ε₀ := I/16 (≤ 1/16). For every
ε ∈ (0, ε₀] there is f with |f| ≤ ε such that w := v·e^{f} (so e^{−ε}k^{−s} ≤ w_k ≤ e^{ε}k^{−s}) satisfies

  limsup_{n→∞} (n^pa_n(w) − 2c(p)) ≥ εη_a/2  and  liminf_{n→∞} (n^pa_n(w) − 2c(p)) ≤ −εη_a/2,

with εη_a/2 = εc(p)I/4. In particular n^pa_n(w) does not converge, and the pointwise a-law n^pa_n → 2c(p) fails for
some weights in [e^{−ε}, e^{ε}]·k^{−s}, for every ε ∈ (0, ε₀].

*Proof.* Fix ε ∈ (0, ε₀]. Let 𝒮 := {u : e^{−ε}v ≤ u ≤ e^{ε}v} (the sandwich class).
1. **Uniform bound on b along paths in 𝒮.** For any g with ‖g‖_∞ ≤ ε and the path ve^{tg}, Lemma FV gives
   |(d/dt) log b_m| ≤ ½‖g‖_∞‖μ_m − μ_{m−1}‖₁ ≤ ε, so b_m(ve^{g}) ≤ e^{ε}b_m(v). Since m^pb_m(v) → c(p) and
   e^{ε} ≤ e^{1/16}, there is n₁ = n₁(p, s) with n^pb_m(u) ≤ 2c for m ∈ {n, n + 1}, n ≥ n₁, and every u = ve^{g} ∈ 𝒮.
2. **Linear response with error (R2a).** For n ≥ n₁ and any g with ‖g‖_∞ ≤ ε, Taylor's formula along ve^{tg}
   (a_n is C² in t, proof of R2a), Lemma Toda at t = 0, and Lemma R2a with step 1 give
   n^p|a_n(ve^{g}) − a_n(v) − ⟨g, ΔE_n^v⟩| ≤ ½·sup_t n^p|ä_n| ≤ ½·2(2c + 2c)ε² = 4c(p)ε².
3. **Off-window mass is negligible.** Let θ ∈ (0, ½] with g_p⁺ ≥ 1 on (0, 2θ] (Sat_p⁺) and γ := κ + 1 (Lemma TL,
   κ = (2 + 2/p)s/(s − 1)). For a set A ⊂ ℕ, atomwise |ΔE_n(k)| ≤ b_{n+1}|q_nq_{n+1}| + b_n|q_{n−1}q_n| ≤
   ½b̄(μ_{n−1} + 2μ_n + μ_{n+1})(k), b̄ := max(b_n, b_{n+1}); so for u ∈ 𝒮 and n ≥ n₁,
   n^p‖ΔE_n^{u}|_A‖₁ ≤ c·(μ_{n−1}^u + 2μ_n^u + μ_{n+1}^u)(A).
   With A_n := [1, θn) ∪ (n^γ, ∞) this tends to 0 as n → ∞, **uniformly over u ∈ 𝒮**:
   - head [1, θn): μ_m ≤ 1 − ρ_m for m ∈ {n − 1, n, n + 1}, and Sat_p⁺ (k/m ≤ 2θ for n ≥ 2) makes the head mass
     exponentially small, uniformly over 𝒮, exactly as in Theorem R step 2 and the "Head" bullet of T3-sv;
   - tail (n^γ, ∞): Lemma TL (uniform over the sandwich class) applied at n + 1 bounds μ_{n−1}, μ_n, μ_{n+1} ≤ ρ_{n+2}
     tail masses by any fixed ε′ > 0 once n^γ ≥ A(n + 1)^κε′^{−1/(s−1)}, which holds for n large since γ > κ.
   Write ω(n) := sup_{u∈𝒮} c(μ_{n−1}^u + 2μ_n^u + μ_{n+1}^u)(A_n) → 0.
4. **Scales and the weight.** By Lemma R1a choose good indices n_1 < n_2 < … with ‖n_i^pΔE_{n_i}^v‖₁ ≥ η_a,
   n_1 ≥ max(N₀, n₁), and θn_{i+1} > i·n_i^γ (possible because every pair {N, N + 1}, N ≥ N₀, contains a good index).
   Put W_i := [θn_i, n_i^γ]; these are pairwise disjoint, and for j < i, W_j ⊂ [1, n_{i−1}^γ] ⊂ [1, θn_i), while for
   j > i, W_j ⊂ [θn_{i+1}, ∞) ⊂ (n_i^γ, ∞); i.e. ∪_{j≠i}W_j ⊂ A_{n_i}. Define
   f_i := (−1)^iε·sign(ΔE_{n_i}^v)·1_{W_i} (sign 0 := +1),  f := Σ_if_i,  |f| ≤ ε.
   The signs are computed for the pure power v.
5. **Gain at n_i.** By step 2 with g = f_i, and ⟨f_i, ΔE_{n_i}^v⟩ = (−1)^iε‖ΔE_{n_i}^v|_{W_i}‖₁,
   (−1)^i n_i^p(a_{n_i}(ve^{f_i}) − a_{n_i}(v)) ≥ ε(n_i^p‖ΔE_{n_i}^v‖₁ − n_i^p‖ΔE_{n_i}^v|_{W_i^c}‖₁) − 4cε²
   ≥ εη_a − εω(n_i) − 4cε²,
   where W_i^c ⊂ [1, θn_i) ∪ (n_i^γ, ∞) = A_{n_i}, so by step 3 (with u = v) the middle term is ≤ εω(n_i) → 0.
6. **Cross-scale independence.** Along u(t) := v·e^{f_i + t(f − f_i)}, t ∈ [0, 1] (in 𝒮 for all t), Lemma Toda gives
   n_i^p|(d/dt)a_{n_i}| = n_i^p|⟨f − f_i, ΔE_{n_i}^{u(t)}⟩| ≤ ε·n_i^p‖ΔE_{n_i}^{u(t)}|_{A_{n_i}}‖₁ ≤ εω(n_i),
   since f − f_i is supported in ∪_{j≠i}W_j ⊂ A_{n_i}. So n_i^p|a_{n_i}(w) − a_{n_i}(ve^{f_i})| ≤ εω(n_i) → 0.
7. **Conclude.** Steps 5–6 give (−1)^i(n_i^pa_{n_i}(w) − n_i^pa_{n_i}(v)) ≥ εη_a − 4c(p)ε² − 2εω(n_i). Since
   ε ≤ I/16, 4c(p)ε² ≤ εc(p)I/4 = εη_a/2. The pure-power a-law (n^pa_n(v) → 2c(p); RH_px, RH₁(r), RH_plt1b) then gives
   n_i^pa_{n_i}(w) − 2c(p) ≥ εη_a/2 − o(1) for even i and ≤ −εη_a/2 + o(1) for odd i. ∎

**Remarks.**
- **Ra-a (what is and is not claimed).** Ra shows that the a-law, like the b-law (Theorem R), is not stable under
  fixed-size sandwiched roughness. It does **not** say whether the b-law also fails for the same w, nor whether
  a_n/(2b_n) → 1 fails: the construction controls a_n only. (HEURISTIC, not proved: running R and Ra on interleaved
  scales should break both at once.) For p > 1, w still satisfies the hypotheses of Theorem CL (Σw < ∞, w_k ≥ e^{−ε}k^{−s}), so the
  **tail-Cesàro a-law** A4′ (PROVED-mod-cite (P), through G2 B*(iii); PROVED since Plan 47, REVIEWED), n^{p−1}Σ_{j≥n}a_j(w) → 2c(p)/(p − 1), holds for this w while the pointwise a-law fails
  — a concrete instance of the A4 remark that the tail-Cesàro form does not imply the pointwise one.
- **Ra-b (comparison with Theorem R).** R1a is explicit and direct; Theorem R's R1 is by contradiction. The scale
  separation and the head/tail bookkeeping (Sat_p⁺, TL) are copied from Theorem R; step 1 replaces T3a step 1 by FV,
  which avoids head-margin constants. ε₀ = I/16 ≈ 0.0196 (I NUMERICAL) does not depend on p or s; N₀, n₁ and the scale
  sequence are not explicit (they come from the rates in the pure-power laws, Sat_p⁺ and TL).
- **Ra-c (constants are crude).** The guaranteed jump εη_a/2 ≈ 0.078εc(p) is about 10× smaller than the first-order
  value ε‖n^pΔE_n|_W‖₁ ≈ 0.8εc(p) seen numerically ([4]).
- **Ra-d (novelty).** UNCHECKED (Rule L not run). The Toda form of the first variation of a_n is classical in spirit
  (Toda/Kac–van Moerbeke flows); the same unverified pointers as Theorem R's remark R-d apply.
- **Ra-e (NUMERICAL, `checks/check_ra.out`; float64 Lanczos, truncated at K atoms; not certified).**
  - [4] p = s = 2, K = 20n, one window W = [n/4, K], f = ±ε·sign(ΔE_n^v): n^p(a_n(w) − a_n(v)) = ±0.0250…0.0269 at
    ε = 0.05 and ±0.0985…0.1069 at ε = 0.2 (n = 100, 200), matching the first-order value ±ε‖n^pΔE_n|_W‖₁ to ≤ 2%,
    against the guaranteed εη_a/2 = 0.0024 and 0.0097. The pure-power deviation n^pa_n(v)/(2c) − 1 is ≈ −1.4·10⁻²
    (n = 100) and −7·10⁻³ (n = 200), i.e. O(1/n).
  - [3] and [4] were not K-checked (no K-doubling run; §3.2 [2] shows a polynomial tail beyond 6n), so these numbers
    are illustrative only; nothing in the proofs depends on them.
  - [4b] Two scales on one measure (K = 8000, ε = 0.1, n₁ = 40 on [10, 99] with sign +, n₂ = 400 on [100, K] with sign
    −; far below the polynomial separation of the proof): n^p(a_n(w) − a_n(v))/c(p) = +0.080 at n = 40 and −0.083 at
    n = 400, with median 0.004 over n ∈ [10, 401]. Both spikes survive the other window.

### 3.13 Lemma RL (Plan 42): Law P ⟺ the rescaled μ_n converge to the arcsine law with sup n^p(a_n + b_n) < ∞ (equivalently, in moments ℓ = 1, 2, 4) — RL, RL-loc PROVED (self-contained; the method is Simon 2004 Thm 3.2's, read and quoted in CITATIONS.md (Simon)); Remarks RL-b, RL-n, RL-n2 PROVED (spectral theorem for compact self-adjoint operators: textbook-standard, stated precisely, not checked against a specific source); RL2 PROVED-mod-cite (inherits Theorem R); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan42.md), fixes applied, re-check ACCEPT — REVIEWED; novelty not claimed for RL and RL-b (scaled transcription of Simon's argument), UNCHECKED for RL-loc, RL-n and RL-n2

Target T0′ of `research/program/outline_A_nodes.md`. Lemma LP (§3.8) is a special case of the forward direction for the pure power. Here
both directions are proved for **any** measure, in particular any discrete σ = Σ w_kδ_{x_k} with x_k ↓ 0 (any nodes),
and the outline's statement is refined: the hypothesis "every fixed j" is redundant for the full sequence, the
neighbours are needed for right limits (RL-loc, RL-n), the bound-free case is open (RL-UI), and the b-law alone fails
(RL-b).

**Setting and notation.** σ is a positive Borel measure on ℝ with infinite support and ∫|x|^ℓdσ < ∞ for all ℓ (e.g.
σ = Σw_kδ_{x_k}, x_k ↓ 0, Σw_k < ∞). p_n are its orthonormal polynomials (positive leading coefficients), with the
recurrence of this file

  x p_n = b_{n+1}p_{n+1} + a_np_n + b_np_{n−1}  (n ≥ 0, b_0p_{−1} := 0, b_n > 0 for n ≥ 1),

so a_n is the diagonal and b_n the off-diagonal Jacobi parameter (note: Simon's convention is the reverse, see
CITATIONS.md). μ_n := p_n²dσ is a probability measure (in the discrete case μ_n(k) = w_kp_n(x_k)² = q_n(k)²). Fix
scales s_n > 0 with s_{n+1}/s_n → 1 (here s_n = ⟨n⟩^p, ⟨n⟩ := max(n, 1), written n^p below; for regularly varying
nodes x_k = f(k), s_n = 1/f(n), see RL3). Put

  ν_n := (x ↦ s_nx)_*μ_n,  u_m := (s_mb_m)² (m ≥ 1).

For α ∈ ℝ, β > 0, ρ_{α,β} is the arcsine law on [α − 2β, α + 2β], density 1/(π√(4β² − (y − α)²)). As in Lemma LP's
proof, ∫y^ℓdρ_{α,β} = (1/2π)∫_0^{2π}(α + 2βcos θ)^ℓdθ = (J_{α,β}^ℓ)_{00}, where J_{α,β} is the doubly infinite Jacobi
matrix with diagonal α and off-diagonal β. Its centred moments are ∫(y − α)²dρ_{α,β} = 2β² and ∫(y − α)⁴dρ_{α,β} = 6β⁴
(odd ones vanish), so ∫y⁴dρ_{α,β} = α⁴ + 12α²β² + 6β⁴. **Law P with constant c > 0** (n^pb_n → c, n^pa_n → 2c) is the
case α = 2c, β = c, and ρ_{2c,c} is the arcsine law on [0, 4c], with moments c^ℓ·binom(2ℓ, ℓ).

**(M) Moment formula.** For ℓ ≥ 0, ∫y^ℓdν_n = s_n^ℓ⟨p_n, x^ℓp_n⟩_σ = ((s_nJ)^ℓ)_{nn} = Σ_π W_n(π), the sum over the
(at most 3^ℓ) paths π = (π_0, …, π_ℓ) in ℤ_{≥0} with π_0 = π_ℓ = n and |π_{i+1} − π_i| ≤ 1, where W_n(π) is the product
over steps of s_na_m (a stay at m) and s_nb_{max(m, m′)} (a step between m and m′).
*Proof.* By the recurrence, multiplication by x maps p_m to Σ_{m′}J_{m′m}p_{m′}; iterate ℓ times and take the inner
product with p_n (orthonormality). A closed path of length ℓ stays within distance ⌊ℓ/2⌋ of n. ∎ (This is Simon's
Proposition 3.3 in our notation; the proof above is complete.)

**Lemma RL.** Let α ∈ ℝ and β > 0. The following are equivalent.
- (a) s_na_n → α and s_nb_n → β.
- (b) ∫y^ℓdν_n → ∫y^ℓdρ_{α,β} for ℓ = 1, 2 and 4.
- (c) ν_n → ρ_{α,β} weakly, and y⁴ is uniformly integrable: lim_{R→∞} sup_n ∫_{|y|>R}y⁴dν_n = 0.
- (c′) ν_n → ρ_{α,β} weakly, and sup_n s_n(|a_n| + b_n) < ∞ (an a priori bound).

If they hold, ∫y^ℓdν_n → ∫y^ℓdρ_{α,β} for every ℓ ≥ 0. In particular, for any nodes and any c > 0, **Law P with
constant c holds iff ν_n → arcsine on [0, 4c] weakly together with the a priori bound sup_n n^p(a_n + b_n) < ∞**
(for x_k > 0, a_n > 0); and iff the three moments ℓ = 1, 2, 4 of ν_n converge to 2c, 6c², 70c⁴.

*Proof.* Throughout, s_n/s_{n+i} → 1 for each fixed i.

**(a) ⇒ all moments, hence (b).** Fix ℓ and let n ≥ ℓ, so the paths in (M) are exactly the closed paths of length ℓ
on ℤ at n. For |m − n| ≤ ℓ, s_na_m = (s_n/s_m)(s_ma_m) → α and s_nb_m → β. So each of the finitely many W_n(π)
converges to the weight of the translated path for J_{α,β}, and ∫y^ℓdν_n → (J_{α,β}^ℓ)_{00} = ∫y^ℓdρ_{α,β}.

**(b) ⇒ (a).**
1. *ℓ = 1.* ∫y dν_n = s_na_n, so s_na_n → α.
2. *ℓ = 2.* By (M), ∫y²dν_n = s_n²(a_n² + b_n² + b_{n+1}²). A convergent sequence is bounded, so sup_n s_n²b_n² and
   sup_n s_n²b_{n+1}² are finite; hence U := sup_m u_m < ∞ (u_m = s_m²b_m² ≤ ∫y²dν_m). Then
   s_n²b_{n+1}² = (s_n/s_{n+1})²u_{n+1} = u_{n+1} + o(1), and with step 1:

     u_n + u_{n+1} → (α² + 2β²) − α² = 2β².  (∗)

3. *ℓ = 4.* Let K^{(n)} := s_nJ − αI: diagonal D_m := s_na_m − α, off-diagonal E_m := s_nb_m. Since αI commutes
   with K^{(n)}, ∫y⁴dν_n = Σ_{j=0}^{4}binom(4, j)α^{4−j}((K^{(n)})^j)_{nn}, and each ((K^{(n)})^j)_{nn} is a path sum
   as in (M) with stay weights D_m and step weights E_m. For |m − n| ≤ 1, D_m = (s_n/s_m)(s_ma_m) − α → 0 by step 1
   at index m. For n − 1 ≤ m ≤ n + 2, E_m² = (s_n/s_m)²u_m = u_m + o(1) ≤ 2U eventually.
   - j = 1: (K)_{nn} = D_n → 0.
   - j = 2: (K²)_{nn} = D_n² + E_n² + E_{n+1}² = u_n + u_{n+1} + o(1) → 2β² by (∗).
   - j = 3: a closed path has as many up-steps as down-steps, so a closed path of length 3 has an odd number (≥ 1)
     of stays. It stays within distance 1 of n, so it contains a factor D_m with |m − n| ≤ 1 (→ 0); its other two
     factors are bounded. Hence (K³)_{nn} → 0.
   - j = 4: paths with at least one stay have 0 or 2 non-stay steps, stay within distance 1 of n and contain a factor
     D_m → 0. The six paths with four ±1 steps (++−−, +−+−, +−−+, −++−, −+−+, −−++) give
     (E_n² + E_{n+1}²)² + E_{n+1}²E_{n+2}² + E_{n−1}²E_n².
   Hence ∫y⁴dν_n = α⁴ + 12α²β² + (u_n + u_{n+1})² + u_{n+1}u_{n+2} + u_{n−1}u_n + o(1). Comparing with
   ∫y⁴dρ_{α,β} = α⁴ + 12α²β² + 6β⁴ and using (∗):

     u_{n+1}u_{n+2} + u_{n−1}u_n → 6β⁴ − 4β⁴ = 2β⁴.  (∗∗)

4. *Limit points.* (u_n) is bounded. Let γ be a limit point, u_{n_j} → γ. By (∗) at n_j − 1, n_j and n_j + 1:
   u_{n_j−1} → 2β² − γ, u_{n_j+1} → 2β² − γ, u_{n_j+2} → γ. By (∗∗) at n_j: 2γ(2β² − γ) = 2β⁴, i.e. (γ − β²)² = 0.
   So β² is the only limit point, u_n → β², and s_nb_n → β (b_n > 0). With step 1 this is (a). ∎(b ⇒ a)

**(a) ⇒ (c′).** Convergent sequences are bounded. Weak convergence (method of moments, proved here to keep RL
self-contained): all moments converge (first part). By Chebyshev with ℓ = 2, (ν_n) is tight. Let ν be a subsequential
weak limit. Since sup_n∫y^{2ℓ+2}dν_n < ∞, y^ℓ is uniformly integrable, so ∫y^ℓdν = ∫y^ℓdρ_{α,β} for all ℓ (as in
(c) ⇒ (b) below). With R := |α| + 2β, ∫y^{2ℓ}dν ≤ R^{2ℓ}, so ν(|y| > R + δ) ≤ (R/(R + δ))^{2ℓ} → 0 (ℓ → ∞); ν lives on
[−R, R], where polynomials are uniformly dense in C[−R, R] (Weierstrass), so ν = ρ_{α,β}. All subsequential limits
agree, so ν_n → ρ_{α,β}.

**(c′) ⇒ (c).** Let L := sup_n s_n(|a_n| + b_n). For n ≥ n₀ with s_n/s_m ≤ 2 whenever |m − n| ≤ 3, (M) with ℓ = 6 gives
∫y⁶dν_n ≤ 3⁶(2L)⁶; the finitely many n < n₀ have finite moments. So M₆ := sup_n∫y⁶dν_n < ∞ and
∫_{|y|>R}y⁴dν_n ≤ M₆/R².

**(c) ⇒ (b).** Let g(y) = y^ℓ (ℓ ≤ 4), so |g| ≤ 1 + y⁴. Fix R ≥ max(1, |α| + 2β) and a continuous φ_R with 0 ≤ φ_R ≤ 1,
φ_R = 1 on [−R, R], φ_R = 0 off [−R − 1, R + 1]. Then |∫g dν_n − ∫g dρ_{α,β}| ≤ |∫gφ_R dν_n − ∫gφ_R dρ_{α,β}| +
2∫_{|y|>R}y⁴dν_n (the ρ-tail is 0). The first term → 0 (gφ_R is bounded and continuous), and the second is small
uniformly in n for R large. ∎

**Lemma RL-loc (right limits: which neighbours are needed).** Let N₀ ⊂ ℕ be infinite and suppose that, as n → ∞ in
N₀, ∫y^ℓdν_n → ∫y^ℓdρ_{α,β} for ℓ = 1, 2, 4 and ∫y^ℓdν_{n±1} → ∫y^ℓdρ_{α,β} for ℓ = 1, 2 (the 4th moment is used
only at n). Then s_na_n → α, s_nb_n → β and
s_nb_{n+1} → β as n → ∞ in N₀. (The same holds under weak convergence of ν_{n+i}, i ∈ {−1, 0, 1}, along N₀ plus
uniform integrability of y⁴ there, by (c) ⇒ (b).)

*Proof.* Steps 1–4 above, run along N₀. Step 1 at n + i (i = −1, 0, 1) gives D_m → 0 for |m − n| ≤ 1. Step 2 at n + i
(i = −1, 0, 1; at i = 1 it uses s_{n+1}²b_{n+2}² ≤ ∫y²dν_{n+1}) gives
boundedness of u_{n−1}, …, u_{n+2} and u_{n−1} + u_n, u_n + u_{n+1}, u_{n+1} + u_{n+2} → 2β². Step 3 at n uses only
these (D_m with |m − n| ≤ 1, E_m with n − 1 ≤ m ≤ n + 2) and gives (∗∗) at n. Step 4 along subsequences of N₀ gives
u_n → β², and then u_{n+1} → β² by (∗). ∎

So the outline's hypothesis "for every fixed j ∈ ℤ, μ_{n+j} rescaled by f(n)" is redundant for the full sequence (it
follows from the hypothesis at index n + j, since s_{n+j}/s_n → 1), and for right limits the three indices
n − 1, n, n + 1 suffice. The middle index alone does not:

**Remark RL-n (the neighbours cannot be dropped; PROVED (spectral theorem for compact self-adjoint operators: textbook-standard, stated precisely, not checked against a specific source); novelty UNCHECKED).** Weak convergence of ν_n along a
sparse N₀ — even convergence of *all* moments — does not force the parameters at n ∈ N₀, already for positive
discrete measures with x_k ↓ 0 and α = 2β (Law P's case).
- *Doubly infinite model.* For t ∈ (0, 1) let J_t be the doubly infinite Jacobi matrix with diagonal α, bonds
  B_m (between m − 1 and m) equal to β for m ∉ {0, 1}, B_0² = 2tβ², B_1² = 2(1 − t)β². Then (J_t^ℓ)_{00} = (J_{α,β}^ℓ)_{00}
  for every ℓ. *Proof.* A closed path at 0 splits uniquely into stays at 0 (weight α) and excursions (maximal segments
  off 0). A right excursion of length L + 2 is 0 → 1, a closed path at 1 of length L inside {1, 2, …}, 1 → 0, with
  weight B_1²·W₊; a left one has weight B_0²·W₋, and reflection m ↦ −m is a weight-preserving bijection between left
  and right inner paths (both half-lines are free, with entries α, β). Summing each excursion over left/right gives
  (B_0² + B_1²)W₊ = 2β²W₊, the same as for t = ½, i.e. for J_{α,β}. ∎ So the e_0-spectral measure of J_t is ρ_{α,β}
  although J_t is not free for t ≠ ½: the outline's step "the e_j-spectral measure of J_∞ is arcsine ⇒ J_∞ free" needs
  every j (it is the full-sequence hypothesis).
- *Realization.* Let α = 2β, p > 0, ⟨m⟩ := max(m, 1), N₀ = {n_1 < n_2 < …} with n_1 ≥ 2 and n_{j+1} − n_j → ∞,
  θ_m := π/4 for m ∉ N₀ and θ_m := θ* := arcsin√t for m ∈ N₀. Put ℓ_m := √(2β)⟨m⟩^{−p/2}cos θ_m,
  k_m := √(2β)⟨m⟩^{−p/2}sin θ_m, and

    a_m := ℓ_m² + k_m² = 2β⟨m⟩^{−p},  b_m := ℓ_{m−1}k_m (m ≥ 1).

  With L the lower-bidiagonal matrix with diagonal ℓ_m and subdiagonal k_m (m ≥ 1), J = LLᵀ + k_0²e_0e_0ᵀ, so J ≥ 0.
  J is injective: Ju = 0 gives ‖Lᵀu‖² + k_0²u_0² = 0, so u_0 = 0 and ℓ_mu_m + k_{m+1}u_{m+1} = 0 with all ℓ, k > 0,
  so u = 0. Its entries tend to 0, so J is compact (a norm limit of its finite truncations). Let σ be the spectral
  measure of e_0 for J. By the spectral theorem for compact self-adjoint operators (Hilbert–Schmidt;
  textbook-standard, stated precisely, not checked against a specific source — as for TL's Markov/Chebyshev and LP's
  method of moments): a compact self-adjoint operator on a separable Hilbert space has an orthonormal eigenbasis of
  (ker J)^⊥ with real eigenvalues λ_k → 0. Hence σ = Σ_k|⟨e_0, φ_k⟩|²δ_{λ_k} over an orthonormal eigenbasis
  (J is injective), with eigenvalues λ_k > 0 (J ≥ 0, injective) accumulating only at 0. After that only polynomial
  functional calculus on the eigenbasis is used. With P_m defined by the recurrence with these
  a_m, b_m, induction on the recurrence gives P_m(J)e_0 = e_m, so ∫P_mP_{m′}dσ = ⟨e_m, e_{m′}⟩ = δ_{mm′}: the P_m are
  σ's orthonormal polynomials (σ has infinite support) and its Jacobi parameters are exactly a_m, b_m. So σ is a
  discrete measure with atoms x_k ↓ 0.
- *Conclusion.* Fix ℓ. For n = n_j, the entries within distance ℓ of n, multiplied by s_n = n^p, converge to those of
  J_t translated to n (diagonal → 2β = α; s_nb_{n+i} → 2βcos θ_{n+i−1}sin θ_{n+i}, which is β√(2t) for i = 0,
  β√(2(1 − t)) for i = 1 and β otherwise, since the other θ's near n_j are π/4 for large j). So by (M) every moment of
  ν_{n_j} converges to (J_t^ℓ)_{00} = ∫y^ℓdρ_{2β,β}, and ν_{n_j} → arcsine on [0, 4β] weakly (as in (a) ⇒ (c′)). But
  n_j^pb_{n_j} → β√(2t) ≠ β for t ≠ ½. (By RL-loc, ν_{n_j−1} and ν_{n_j+1} cannot both have arcsine 1st/2nd moments in
  the limit; indeed the 2nd moment of ν_{n_j−1} tends to α² + (1 + 2t)β².)

**Remark RL-b (the b-law alone is not enough; PROVED (spectral theorem for compact self-adjoint operators: textbook-standard, stated precisely, not checked against a specific source; realization as in RL-n); novelty not claimed).** Law P needs both halves: there are positive discrete measures
with x_k ↓ 0, n^pb_n → c, and ν_n → arcsine on [c, 5c] (not [0, 4c]). Take a_m := 3c⟨m⟩^{−p}, b_m := cm^{−p}. Then
⟨u, Ju⟩ ≥ Σ_m(a_m − b_m − b_{m+1})u_m² ≥ cΣ⟨m⟩^{−p}u_m² (2|b_mu_{m−1}u_m| ≤ b_m(u_{m−1}² + u_m²); b_m + b_{m+1} ≤ 2c⟨m⟩^{−p}),
so J is positive definite and compact, and as in RL-n its e_0-spectral measure is discrete with atoms x_k ↓ 0 and has
these parameters. By RL ((a) with α = 3c, β = c), ν_n → ρ_{3c,c}. Since a_n = ∫x dμ_n, the a-law is the first moment
of ν_n; positivity of the atoms forces α ≥ 2β for any limit ρ_{α,β}, since ρ_{α,β} must live on [0, ∞).

**Remark RL-UI (open).** The proof of (c) ⇒ (a) uses uniform integrability of y⁴ (or the a priori bound in (c′)).
Whether weak convergence of the full sequence ν_n alone implies (a) is not decided here. For pure-power nodes and
sandwiched weights c₁k^{−s} ≤ w_k ≤ C₁k^{−s} the question does not arise: T3a's proof, step 1 (§3.5), which uses only
Sat_p⁺, gives a_n, b_n ≤ 2M^p(n − 1)^{−p} for large n (M the head margin there; M₀(p) in §3.8), which is the bound in
(c′).

**Corollaries (for G1).**
- **RL1 (localization ⟺ Law P).** For x_k = k^{−p} and sandwiched weights, the full pointwise Law P holds iff
  ν_n → arcsine on [0, 4c(p)] weakly (RL with (c′) and RL-UI's bound). Label: PROVED (internal: RL, T3a step 1 /
  Sat_p⁺). Lemma LP (§3.8) is a special case of the forward direction for v = k^{−s} (its CDF form for y ≤ 1, i.e.
  M ≥ 1); the full forward direction is RL (a) ⇒ (c′) applied to the pure-power Law P (RH_px, RH₁(r), RH_plt1b). Any proof of the weak limit, e.g. by Christoffel-function or universality methods (outline A, Route W),
  therefore gives the full law.
- **RL2 (Theorem R; PROVED-mod-cite, inherits Theorem R: RH_px, RH₁(r), RH_plt1b).** For the weights of Theorem R
  (§3.6; sandwiched, |f| ≤ ε), limsup|log(β_n²/β_{n−1}²)| > 0, so β_n ↛ 1 (indeed β_n has no positive limit). Hence (a)
  fails, so at least one of the moments ℓ = 1, 2, 4 of ν_n does not converge to its arcsine value (this half needs no
  bound). Since the a priori bound of (c′) holds by T3a step 1 (§3.5; sandwiched weights, Sat_p⁺), ν_n also does
  **not** converge weakly to arcsine on [0, 4c(p)]. By RL-loc this failure is visible near any subsequence along which
  β_n stays away from 1.
- **RL3 (any nodes).** RL needs nothing about the nodes beyond s_{n+1}/s_n → 1. Let x_k = f(k) with f regularly
  varying with index −p and constant C as in the Setting of this file (item 11 (H-a)), f decreasing on [1, ∞), and
  s_n = 1/f(n). Then s_{n+1}/s_n → 1: for λ > 1 and n ≥ 1/(λ − 1), f(λn)/f(n) ≤ f(n + 1)/f(n) ≤ 1, whence
  λ^{−p} ≤ liminf f(n + 1)/f(n) ≤ 1; let λ ↓ 1. So "Law P (constant c(p)C)" ⟺ "ν_n (rescaling by 1/f(n)) → arcsine on
  [0, 4c(p)C], with the a priori bound". The a priori bound for nodes other than pure powers needs a substitute for Sat_p⁺ (outline A, T0).

**Literature (Rule C; source READ).** Simon, "Ratio asymptotics and weak asymptotic measures for orthogonal
polynomials on the real line", J. Approx. Theory 126 (2004); mp_arc 03-341, TeX source read 2026-10-14 (quotes in
`CITATIONS.md`, entry (Simon)). His Theorem 3.2 is the unscaled case s_n ≡ 1 of (b) ⇒ (a), with general limits A_1,
A_2, A_4 (then the off-diagonal limits may alternate, a_{2n} → a, a_{2n+1} → c in his notation); Theorem 3.1 is the
unscaled (a) ⇒ all moments. Simon's statements do not apply verbatim: ν_n is a moment problem for the n-dependent
matrix s_nJ, not for a fixed J. The proof above transcribes his argument (path sums, his (3.10)–(3.11) = our (∗),
(∗∗)) to the scaled setting. For the arcsine values the discriminant 3A_2² − 2A_4 of his (3.13) vanishes, which is
why the limit is a single value and his Lemma 3.4 is not needed. RL does not depend on the citation, which is given
for attribution. Label: **PROVED** (self-contained); novelty not claimed (RL, RL-b). RL-loc, RL-n: novelty UNCHECKED (Simon's
Remark 2 after Thm 3.1 — ρ_{b;a,c} determines b and the unordered pair (a, c) — concerns the full sequence; a
single-index counterexample like J_t was not seen in the sources read).

**Rule A (adversarial pass).**
- *Two-point / degenerate measures:* excluded (infinite support is needed for μ_n at every n). For finite support
  everything holds up to the last index, which is irrelevant for limits.
- *Converse of (∗):* (∗) alone allows period-2 oscillation u_{2n} → γ, u_{2n+1} → 2β² − γ; (∗∗) kills it only because
  the arcsine 4th moment has zero discriminant. Checked: other targets (A_4 < 3A_2²/2) give Simon's alternating
  limits, so the arcsine identification is essential.
- *Only ℓ = 1, 2 (no 4th moment):* insufficient — the spectral measure of e_0 (as in RL-n; positivity is not needed
  for RL) of the period-2 Jacobi matrix with a_m = α⟨m⟩^{−p}, b_m alternating
  between β_1m^{−p} and β_2m^{−p} (β_1² + β_2² = 2β²) has the right 1st and 2nd moments in the limit (Simon Thm 3.1
  scaled), and 4th moment α⁴ + 12α²β² + 4β⁴ + 2β_1²β_2² ≠ α⁴ + 12α²β² + 6β⁴ unless β_1 = β_2.
- *Neighbours:* RL-n shows that the index set {n} alone fails; {n − 1, n, n + 1} suffices (RL-loc).
  **Remark RL-n2 (the pair {n, n + 1} does not suffice for moments 1, 2, 4; reviewer's construction, Rule R F7;
  PROVED for general measures (spectral theorem for compact self-adjoint operators: textbook-standard, stated precisely, not checked against a specific source), positivity open; novelty UNCHECKED; check_rl [4] NUMERICAL).** Take β = 1, α = 2 and at a sparse N₀ the
  scaled bond values u_n = u_{n+2} = γ, u_{n+1} = 2 − γ, u_{n−1} = u_{n+3} = ((γ − 1)² + 1)/γ (0 < γ < 2, so that all b > 0), all other
  u = 1, and diagonal α (scaled as in RL-n: a_m = α⟨m⟩^{−p}, b_m = √u·m^{−p}). Then (∗) and (∗∗) hold exactly at n
  and at n + 1: u_n + u_{n+1} = u_{n+1} + u_{n+2} = 2, and u_{n+1}u_{n+2} + u_{n−1}u_n = u_{n+2}u_{n+3} + u_nu_{n+1}
  = γ(2 − γ) + (γ − 1)² + 1 = 2. So the scaled moments ℓ = 1, 2, 4 of ν_n and ν_{n+1} tend to 2, 6, 70 (step 3's
  expansion), while u_n → γ ≠ 1 for γ ≠ 1. RL does not need positivity, so the e_0-spectral measure of this bounded
  Jacobi matrix (as in RL-n, via the spectral theorem) is an admissible σ. Whether a version with
  x_k > 0 exists is **not claimed**: the reviewer found the local model's smallest truncated eigenvalue +5.6e−5 at
  γ = 1.3 (consistent with the free edge) but −0.016 at γ = 0.8.
- *Scale ratios:* every use of s_n/s_m → 1 is for |m − n| bounded by a constant depending only on ℓ (≤ ℓ/2 in
  "(a) ⇒ all moments", ≤ 3 in (c′) ⇒ (c), ≤ 2 in steps 1–4).
- *b_n alone:* RL-b.
- *Weak convergence without moments:* RL-UI (open, stated as such).

**Numerics (NUMERICAL, `checks/check_rl.out`; float64 Lanczos with full reorthogonalization, p = s = 2).**
- [1] (M) agrees with quadrature over the atoms to 10 digits (ℓ ≤ 4, n = 100), and so does the step-3 expansion
  α⁴ + 4α³(K) + 6α²(K²) + 4α(K³) + (K⁴).
- [2] dev_n := max(|n^pb_n/c − 1|, |n^pa_n/2c − 1|) and mom_n := max_{ℓ=1,2,4}|∫y^ℓdν_n/m_ℓ − 1|. rdev, rmom are the
  same quantities relative to the pure power at the same n and K, which removes the common O(1/n) error.
  - Pure power: dev_n = 2.9e−2 → 3.7e−3 and mom_n = 1.1e−1 → 1.5e−2 (n = 50 → 400), both O(1/n).
  - Ψ = 2 + sin(log log(k + 2)): rdev, rmom ≤ 5.4e−4; for n ≥ 100, rdev ≈ 1e−5 and rmom = 2.8e−5, 6.9e−5, 6.3e−5.
  - Theorem-R-type weight (ε = 0.2, windows at N = 60, 240): rdev ≈ 6e−2 at n = N − 1, N. rmom = 9.6e−2, 6.8e−3,
    4.0e−2 at n = N − 2, N − 1, N for N = 60 and 7.9e−2, 8.2e−3, 3.9e−2 for N = 240; the peak is at N − 2, since the
    4th moment at n sees u_{n−1}, …, u_{n+2}. The N − 1 rows (rdev ≈ 6e−2, rmom < 1e−2) are a numerical instance of
    RL-n: the single-index moments are near arcsine while the parameters are off. At n = 20, 110, 130, 389,
    rdev ≤ 8e−3 and rmom ≤ 3e−2.
  - iid U[½, 3/2] weights: rdev = 2.6e−2, 8.3e−3, 1.6e−2, 5.6e−3 and rmom = 6.1e−2, 1.3e−2, 1.7e−2, 2.2e−2
    (n = 50…400): of order 1e−2, not monotone at these n (check_t3_rough [4] finds slowly decaying jumps for such
    weights).
  - K-doubling for Ψ at n = 200 changes dev and mom in the 4th digit.
  - A finite computation cannot show (non)convergence. It shows that the two order parameters move together, as RL
    predicts.
- [3] RL-b: moments of ν_n → 3c, 11c², 195c⁴ (arcsine on [c, 5c]). RL-n (t = ¼, n_j = 10², 10³, 10⁴): n_j^pb_{n_j}/β →
  0.707 = √(2t), while the moments ℓ = 1…8 of ν_{n_j} tend to the arcsine moments (ratios 0.99955–1 at n_j = 10⁴).
  At n_j ± 1 the 2nd-moment ratio is 0.9167 = (5 + 2t)/6 and 1.0833. The leading 3000×3000 block of J has smallest
  eigenvalue 1.75e−13 > 0.
- [4] RL-n2 (γ = 0.5, 0.8, 1.3; n_j = 1000, 9995): the moments ℓ = 1, 2, 4 of ν_{n_j} and ν_{n_j+1} are within 3e−4
  (relative) of 2, 6, 70 at n_j = 9995 (3e−3 at n_j = 1000; O(1/n)), while n_j^pb_{n_j} = √γ exactly.

### 3.14 Theorem B-cond (Plan 44): the pointwise Law P for every slowly varying weight, conditional on a log-moment localization hypothesis (QL) — Lemmas L0, QLb PROVED; FV⁺ PROVED (standard extension; novelty not claimed); QL, QL₀ HYPOTHESIS; Theorem B-cond CONDITIONAL (QL₀, implied by QL) + PROVED-mod-cite (RH_px, RH₁(r), RH_plt1b); Rule R ACCEPT WITH FIXES (review/REVIEW_Plan44.md), fixes applied, re-check ACCEPT — REVIEWED; novelty UNCHECKED

Source: `research/program/outline_B_sv.md` §2 (Problem B, "B-cond"). Setting: x_k = k^{−p} (p > 0), v = k^{−s} (s > 1),
w = vΨ with Ψ > 0 on ℕ **slowly varying in the sequence form of §3.8/§3.9(i)**: δ_n(λ) := max{|log Ψ(k) − log Ψ(n)| :
k ∈ ℕ ∩ [n/λ, λn]} → 0 for every λ ≥ 1. Nothing else is assumed: no boundedness, no D(γ) < ∞ (so e.g. Ψ = exp(√log k)
and exp((log k)^θ), θ < 1, are allowed), no measurability or smoothness of an interpolating function. Notation as in
§3.8–3.9: path w(t) = vΨ^t (t ∈ [0, 1]), q_j = √(w(t))p_j^{(t)}, μ_m^{(t)} = q_m², ρ_m^{(t)} = Σ_{j<m}μ_j^{(t)};
M₀ = M₀(p) ≥ 4 is the head margin of T3-sv (g_p⁺ ≥ 1 on (0, 2/M₀]); κ := (2 + 2/p)s/(s − 1) as in Lemma TL;
g_n := log Ψ − log Ψ(n); log₂ is log base 2.

**Lemma L0 (dyadic chaining and Potter bounds, sequence form).** Put ε_n := sup_{m≥n} δ_m(2). Then ε_n < ∞, ε_n is
nonincreasing and ε_n → 0, and
- (i) |g_n(k)| ≤ ε_n(1 + log₂(k/n)) for all n ≥ 1 and all integers k ≥ n;
- (ii) for every η > 0 there is A_η < ∞ with |log Ψ(k)| ≤ A_η + η log k for all k ≥ 1; i.e.
  e^{−A_η}k^{−η} ≤ Ψ(k) ≤ e^{A_η}k^{η}.

*Proof.* Each δ_m(2) is a maximum of finitely many finite numbers, and δ_m(2) → 0; so the tail suprema ε_n are finite,
nonincreasing and tend to 0.
- (i) Let k ≥ n and j := ⌊log₂(k/n)⌋ ≥ 0, so 2^jn ≤ k < 2^{j+1}n. For 0 ≤ i < j, 2^{i+1}n ∈ [2^in/2, 2·2^in], so
  |log Ψ(2^{i+1}n) − log Ψ(2^in)| ≤ δ_{2^in}(2) ≤ ε_n (as 2^in ≥ n). Also k ∈ [2^jn, 2·2^jn], so
  |log Ψ(k) − log Ψ(2^jn)| ≤ δ_{2^jn}(2) ≤ ε_n. Summing the j + 1 steps: |g_n(k)| ≤ (j + 1)ε_n ≤ ε_n(1 + log₂(k/n)).
- (ii) Fix η > 0 and choose N with ε_N ≤ η log 2. For k ≥ N, (i) at n = N gives
  |log Ψ(k)| ≤ |log Ψ(N)| + ε_N + (ε_N/log 2)log(k/N) ≤ |log Ψ(N)| + ε_N + η log k. For k < N there are finitely many
  values. Take A_η := max(|log Ψ(N)| + ε_N, max_{k<N}|log Ψ(k)|). ∎

*Remarks on L0.* Only the upward chain is proved and used; below n the proof of B-cond uses δ_n(M₀) and (ii). Only λ = 2
enters (λ = 2 implies all λ by the same chaining; the downward half k ∈ [n/λ, n) needs ε at the lower index:
|g_n(k)| ≤ ε_k(1 + log₂(n/k)) ≤ ε_{⌈n/λ⌉}(1 + log₂λ)), so "sequence-form slow variation" is used exactly as defined, and no
uniform convergence theorem (Bingham–Goldie–Teugels) is used or cited.

**Lemma FV⁺ (Lemmas FV and FVa for unbounded perturbations; PROVED, standard extension, novelty not claimed).** Let x_k ∈ (0, 1] be distinct (k ∈ ℕ), v_k > 0 and f_k ∈ ℝ,
and assume

  Σ_k U_k < ∞,  U_k := v_k·max(1, e^{f_k})·(1 + |f_k|).

Put w(t) := v·e^{tf} (t ∈ [0, 1]). Then for every n ≥ 1: Σ_k|f_k|μ_m^{(t)}(k) < ∞ for every m, uniformly bounded in
t ∈ [0, 1]; t ↦ log b_n²(t) and t ↦ a_n(t) are C¹ on [0, 1]; and the formulas of Lemma FV and Lemma FVa hold,

  (d/dt)log b_n² = ⟨f, μ_n − μ_{n−1}⟩,  (d/dt)a_n = ⟨(x − a_n)f, μ_n⟩ − 2b_n⟨f, q_{n−1}q_n⟩,

with every series absolutely convergent. Both right sides are unchanged under f ↦ f + c.

*Proof.* Only two uses of "f bounded" occur in the proofs of FV (§3.2) and FVa (§3.5): (A) differentiating the Heine sums
term by term, and (B) absolute convergence of the series. We redo both.
- **(A) Heine sums.** D_m(t) = Σ_{|S|=m}T_S(t), T_S(t) := Π_{k∈S}w_k(t)·V(S), V(S) := Π_{i<j in S}(x_i − x_j)² ≤ 1 (all
  x_k ∈ (0, 1]). Since ∂_tT_S = (Σ_{k∈S}f_k)T_S, 1 + |Σ_{k∈S}f_k| ≤ Π_{k∈S}(1 + |f_k|) and w_k(t) ≤ v_k max(1, e^{f_k}),
  we get |T_S(t)| + |∂_tT_S(t)| ≤ Π_{k∈S}U_k on [0, 1], and Σ_{|S|=m}Π_{k∈S}U_k ≤ (ΣU)^m < ∞. By the Weierstrass M-test,
  D_m ∈ C¹[0, 1] with D_m′ = Σ_S(Σ_{k∈S}f_k)T_S, and D_m > 0 (infinitely many atoms). The same holds for
  N_F(t) := Σ_SF(S)T_S(t) with F(S) := Σ_{k∈S}x_k (|F| ≤ m).
- **(B) Absolute convergence.** By Tonelli and (A), Σ_k|f_k|ρ_m^{(t)}(k) = Σ_S(Σ_{k∈S}|f_k|)T_S/D_m ≤ (ΣU)^m/D_m(t),
  which is bounded on [0, 1] (D_m continuous and positive). As μ_j ≤ ρ_m for j < m (Lemma H, weight-general), every
  Σ_k|f_k|μ_j(k) is finite; also |q_{n−1}q_n| ≤ ½(μ_{n−1} + μ_n), so ⟨|f|, |q_{n−1}q_n|⟩ < ∞.
- **FV.** (d/dt)log D_m = D_m′/D_m = Σ_S(Σ_{k∈S}f_k)P_{m,t}(S) = Σ_kf_kρ_m(k), the interchange by (B). Then
  log b_n² = log D_{n+1} − 2log D_n + log D_{n−1} gives the formula as in §3.2.
- **FVa.** Step 1 of §3.5 is weight-independent. Step 2: 𝔼_{m,t}F = N_F/D_m is C¹ with derivative
  𝔼[F⟨f, X⟩] − 𝔼F·𝔼⟨f, X⟩, finite since |F⟨f, X⟩| ≤ mΣ_{k∈S}|f_k|. Step 3: 𝔼[F⟨f, X⟩] = Σ_{k,l}x_kf_lP(k, l ∈ S) by
  Fubini, since Σ_{k,l}x_k|f_l|P(k, l ∈ S) ≤ Σ_l|f_l|𝔼[|S|X_l] = mΣ_l|f_l|ρ_m(l) < ∞. The two-point formula
  P(k, l ∈ S) = K_m(k,k)K_m(l,l) − K_m(k,l)² (k ≠ l) does not involve f. Every double sum in the covariance identity
  Cov = ½Σ_{k,l}(x_k − x_l)(f_k − f_l)K_m(k,l)² is dominated by a multiple of Σ_{k,l}|f_l|K_m(k,l)² = Σ_l|f_l|K_m(l,l) < ∞
  (projection: Σ_kK_m(k,l)² = K_m(l,l)). Step 4: the rank-one update is a termwise identity between absolutely convergent
  series (m = n + 1 and m = n); for the cross piece, Cauchy–Schwarz gives
  Σ_{k,l}|f_k||K_n(k,l)q_n(k)q_n(l)| ≤ ½Σ_{k,l}|f_k|(K_n(k,l)² + q_n(k)²q_n(l)²) = ½Σ_k|f_k|(K_n(k,k) + μ_n(k)) < ∞
  (and symmetrically for f_l; |x_k − x_l| ≤ 1). After Christoffel–Darboux the cross part is b_nΣ_{k,l}A_{kl}(f_k − f_l), with
  Σ_{k,l}|A_{kl}||f_k| ≤ ⟨|f|, μ_n + |q_{n−1}q_n|⟩ < ∞ (Σ_l|q_{n−1}(l)q_n(l)| ≤ 1, Σ_lq_n(l)² = 1), and likewise for f_l.
  The algebra of §3.5 step 4 then applies verbatim. C¹: a_n = 𝔼_{n+1}F − 𝔼_nF.
- **Invariance.** μ_n, μ_{n−1} are probability vectors and Σ|f|μ < ∞, so f ↦ f + c changes nothing (as in §3.5 step 5). ∎

*Why not the K-cutoff of T3-log step 3 (F1 of Plan 36).* The cutoff replaces the path vΨ^t by vΨ^t·1_{k≤K} + v·1_{k>K},
which is not on the path vΨ^t. Hypothesis QL below would then have to be assumed for these cut paths as well (uniformly
in K). FV⁺ keeps the hypothesis on the single path vΨ^t.

**Application of FV⁺.** f := log Ψ, v = k^{−s}. By L0(ii) with η ≤ (s − 1)/2,
U_k ≤ k^{−s}e^{A_η}k^{η}(1 + A_η + η log k), which is summable. So FV⁺ applies to the path w(t) = vΨ^t.

**Hypothesis QL (log-moment localization along the path; HYPOTHESIS — QL and QL₀ below are both HYPOTHESIS).** Fix γ > κ. Put

  Λ_n := sup_{t∈[0,1]} max_{m∈{n−1,n}} Σ_{k∈ℕ, n≤k≤n^γ} log(k/n)·μ_m^{(t)}(k).

**QL** is the statement ε_nΛ_n → 0 (n → ∞), with ε_n from Lemma L0. (Λ_n increases with γ, so QL for one γ > κ implies
it for every γ′ ∈ (κ, γ]; the weakest form takes γ just above κ.) The proof below uses only the weaker

  **QL₀:** Q_n := sup_{t∈[0,1]} Σ_{k∈ℕ, n≤k≤n^γ}|g_n(k)|·(μ_n^{(t)} + μ_{n−1}^{(t)})(k) → 0,

and even only its t-average ∫_0^1(…)dt in place of sup_t (t ↦ μ_m^{(t)}(k) is continuous). QL₀ is precisely the range
part of the first-variation bound; B-cond shows that everything outside [n, n^γ] is controlled unconditionally, for every
sequence-form slowly varying Ψ (no boundedness), and reduces QL₀ to the log-moment localization statement QL (free of g_n, but still a statement about μ^{(t)} along vΨ^t) via L0. QL ⇒ QL₀, because by
L0(i), with log₂ = log/log 2,

  Q_n ≤ 2ε_n + (2ε_n/log 2)·Λ_n.

**Theorem B-cond.** Let x_k = k^{−p} (p > 0) and w = k^{−s}Ψ (s > 1) with Ψ > 0 slowly varying in sequence form. Fix
γ > κ. Then, with no further hypothesis, there are r_n, r′_n → 0 (depending on p, s, γ, Ψ, not on t) such that for
n ≥ n₀:

  |log b_n²(w) − log b_n²(v)| ≤ 2δ_n(M₀) + Q_n + r_n,
  n^p|a_n(w) − a_n(v)| ≤ 4M₀^p(2δ_n(M₀) + Q_n) + r′_n.

Consequently, **if QL (or QL₀) holds, then n^pb_n(w) → c(p) and n^pa_n(w) → 2c(p)**, along the full sequence of n (not a density-one subsequence), for every p > 0 and s > 1.

*Proof.* Fix η ∈ (0, (s − 1)/2] so small that γ(s − 1 − η) > (2 + 2/p)(s + η) (possible since γ(s − 1) > (2 + 2/p)s,
i.e. γ > κ), and let A := A_η from L0(ii). Then for all t ∈ [0, 1] and k ≥ 1:
e^{−A}k^{−η} ≤ min(1, Ψ(k)) ≤ Ψ(k)^t ≤ max(1, Ψ(k)) ≤ e^{A}k^{η}, so

  W(t) := Σ_jw_j(t) ≤ e^{A}ζ(s − η),  w_k(t) ≥ e^{−A}k^{−s−η},  |g_n(k)| ≤ 2A + 2η log max(k, n).   (∗)

Split ℕ into H := {k < n/M₀} (head), B := [n/M₀, n) (lower bulk), R := [n, n^γ] (range) and T := (n^γ, ∞) (far tail).
1. **FV⁺ and centering.** By FV⁺ and invariance under constants,
   |log b_n²(w) − log b_n²(v)| ≤ ∫_0^1|⟨g_n, μ_n^{(t)} − μ_{n−1}^{(t)}⟩|dt ≤ sup_tΣ_k|g_n(k)|(μ_n + μ_{n−1})^{(t)}(k).
2. **Head (Sat_p⁺).** Let n ≥ 2, m ∈ {n − 1, n}, k ∈ H. Then 1 ≤ k < n/4 < m and k/m ≤ n/(M₀(n − 1)) ≤ 2/M₀, so
   g_p⁺(k/m) ≥ 1. Lemma Sat_p⁺ (which uses only W < ∞ and w_k > 0) and μ_m = ρ_{m+1} − ρ_m ≤ 1 − ρ_m give, by (∗),
   μ_m^{(t)}(k) ≤ (W(t)/w_k(t))·(n + 1)²·e^{−2(n−1)} ≤ e^{2A}ζ(s − η)·n^{s+η}(n + 1)²e^{−2(n−1)}.
   Summing over the < n points of H, with |g_n| ≤ 2A + 2η log n there:
   h_n := sup_tΣ_{k∈H}(1 + |g_n(k)|)(μ_n + μ_{n−1})^{(t)}(k) ≤ 4n(1 + 2A + 2η log n)e^{2A}ζ(s − η)n^{s+η}(n + 1)²e^{−2(n−1)},
   so n^ph_n → 0.
3. **Lower bulk.** On B, |g_n| ≤ δ_n(M₀); contribution ≤ 2δ_n(M₀).
4. **Range.** The contribution of R is ≤ Q_n by definition.
5. **Far tail (Lemma TLw).** T″ = ⌈⌈8pn²⌉n^{2/p}⌉ ≤ (8p + 3)n^{2+2/p} for n ≥ 1, and γ > κ > 2 + 2/p, so n^γ ≥ T″ for
   n ≥ n₁. For k ∈ T and m ≤ n, μ_m ≤ ρ_{m+1} ≤ ρ_{n+1}, and Lemma TLw with u := w(t) and (∗) gives
   μ_m^{(t)}(k) ≤ 1156·w_k(t)/min_{T′≤j≤T″}w_j(t) ≤ 1156e^{2A}T″^{s+η}k^{−s+η}. With |g_n(k)| ≤ 2A + 2η log k there
   (k > n), and using Σ_{k>X}(1 + log k)k^{−(s−η)} ≤ C′X^{1−(s−η)}(1 + log X) for X ≥ e (s − η > 1; compare with the
   integral, the summand being eventually decreasing),
   τ_n := sup_tΣ_{k∈T}(1 + |g_n(k)|)(μ_n + μ_{n−1})^{(t)}(k) ≤ 2·1156e^{2A}(1 + 2A + 2η)·T″^{s+η}·C′n^{−γ(s−1−η)}(1 + γ log n)
   ≤ C″(1 + log n)n^{(2+2/p)(s+η) − γ(s−1−η)} → 0 by the choice of η.
6. **b_n.** Steps 1–5: |log b_n²(w) − log b_n²(v)| ≤ h_n + 2δ_n(M₀) + Q_n + τ_n. Put r_n := h_n + τ_n.
7. **a_n.** Uniform bounds (T3a step 1, which uses only the head bound): x_k ≤ (M₀/n)^p for k ∉ H and x_k ≤ 1, so
   a_n^{(t)} = ⟨x, μ_n⟩ ≤ (M₀/n)^p + h_n, a_{n−1}^{(t)} ≤ (M₀/n)^p + h_n, and b_n^{(t)} = ⟨xq_{n−1}, q_n⟩ ≤
   ½⟨x, μ_{n−1} + μ_n⟩ ≤ (M₀/n)^p + h_n. For n ≥ n₂ (h_n ≤ (M₀/n)^p) these are ≤ 2M₀^pn^{−p}, uniformly in t, and
   off H, |x_k − a_n| ≤ max(x_k, a_n) ≤ 2M₀^pn^{−p}. On H use |x_k − a_n| ≤ 1 and b_n ≤ 1. By FV⁺ (FVa, centered),
   n^p|ȧ_n| ≤ Σ_k|g_n(k)|n^p[|x_k − a_n|μ_n(k) + b_n(μ_{n−1} + μ_n)(k)]
   ≤ 2M₀^p·2Σ_{k∉H}|g_n(k)|(μ_n + μ_{n−1})(k) + 2n^ph_n ≤ 4M₀^p(2δ_n(M₀) + Q_n + τ_n) + 2n^ph_n.
   Integrate over t; r′_n := 4M₀^pτ_n + 2n^ph_n → 0.
8. **Conclusion under QL₀.** δ_n(M₀) → 0 (slow variation), Q_n → 0 (QL₀), r_n, r′_n → 0. So
   log b_n²(w) − log b_n²(v) → 0 and n^p(a_n(w) − a_n(v)) → 0. The pure-power laws (RH_p for p > 1, `RH/px/RH_px.md`;
   RH₁(r) for p = 1; RH_plt1b for 0 < p < 1) give n^pb_n(v) → c(p) and n^pa_n(v) → 2c(p). ∎

*Where each input is used (regularity audit).* Sequence-form slow variation enters only through δ_n(M₀) (step 3) and
L0 (ε_n in QL ⇒ QL₀; the Potter bounds (∗) in FV⁺, steps 2, 5, 7). Sat_p⁺ needs only W(t) < ∞ and the ratio W/w_k;
TLw needs only Σu < ∞; FV⁺ needs ΣU < ∞. The pure-power laws are used for v only. **No smoothing reduction (RedA of the
outline) is needed, and none is proved here**: no interpolating function, no derivative L′ and no measurability enter
the proof. The only hypothesis beyond sequence-form slow variation is QL₀.

**Lemma QLb (power-tail localization ⇒ QL; PROVED).** Suppose there are α > 0, C ≥ 1 and n₀ such that for n ≥ n₀,
m ∈ {n − 1, n} and all real 1 ≤ M ≤ n^{γ−1}: sup_tμ_m^{(t)}(ℕ ∩ (Mn, ∞)) ≤ CM^{−α} (outline's QL-b). Then
Λ_n ≤ (1 + log C)/α for n ≥ n₀, so QL holds (ε_n → 0), and hence the law, for this Ψ.

*Proof.* For fixed t and m, Σ_{n≤k≤n^γ}log(k/n)μ_m(k) = ∫_0^{(γ−1)log n}μ_m({k ≤ n^γ : log(k/n) > u})du (layer cake)
≤ ∫_0^∞min(1, Ce^{−αu})du = (log C)/α + 1/α. ∎

**What is proved about QL (and what is not).**
- *Trivial range.* Λ_n ≤ (γ − 1)log n always (μ_m is a probability vector), so QL holds whenever ε_n log n → 0. This is
  nothing new: then sup_n ε_n(1 + (γ − 1)log₂ n) < ∞, so by L0(i) D(γ) < ∞, and Theorem T3-log (§3.9) already applies.
  With Λ_n ≤ (γ − 1)log n the bound of Theorem B-cond is O(ε_n log n), i.e. B-cond's elementary part reaches exactly
  log-type weights (the outline's "T3-log is the trivial case").
- *Bounded Ψ.* QL₀ holds: the proof of T3-all (§3.8, step 1, via Theorem L) bounds the full sum
  sup_tΣ_k|g_n|(μ_n + μ_{n−1})^{(t)}, which contains Q_n, by a quantity with limsup ≤ 2Ge^{4G}F_p(M) for every M. Theorem L
  does *not* give QL (it is a limit for each fixed M, not uniform up to M = n^{γ−1}), and for bounded Ψ B-cond adds
  nothing to T3-all.
- *Log-type unbounded Ψ (D(γ) < ∞).* The law holds (T3-log), but T3-log's proof runs along a truncated path, so QL₀ along
  vΨ^t itself is not established by it.
- *D(γ) = ∞* (the new case, e.g. exp(√log k)): no case of QL is proved. For Ψ = exp((log k)^θ), ε_n ≍ (log n)^{θ−1}, so
  QL asks for Λ_n = o((log n)^{1−θ}), while the trivial bound is (γ − 1)log n. Numerically Λ_n ≈ 0.4 (below).
- No further case of QL is obtained cheaply from Theorem L, Lemma LP or Lemma TL: the deep range [Mn, n^γ] with M → ∞
  needs localization uniform in M (the outline's QLP for v, L6) *and* its transport along a path whose weights are not
  uniformly sandwiched; the latter is where the elementary methods stop (next remark).

**Remarks.**
- **Bc1 (why the elementary methods stop at log-type; HEURISTIC / OBSTRUCTION, not a theorem about all methods).**
  Summary of `research/program/outline_B_sv.md` §4; none of this is proved here.
  - *Truncation + Grönwall (as in T3-log/Theorem L).* With Ψ truncated to [n/M₀, nR_n], the Grönwall factor is e^{4H_n},
    H_n := osc_{[nR_n, n^γ]}log Ψ, which → ∞ exactly when D(γ) = ∞. Every available transport (TV + Cauchy–Schwarz) leaves
    an additive floor ≥ δ_n(R_n), at best polynomial in 1/log n, and floor²·e^{4H_n} → ∞ for exp((log k)^θ), every θ ∈ (0, 1).
  - *Layered Grönwall on (2^jn, ∞).* The Cauchy–Schwarz bound for ⟨1_Aq_m, K_m(fq_m)⟩ feeds a non-decaying forcing into
    every layer; the resulting bound on Σ_jε·μ((2^jn, ∞)) is ≍ ε³J³ with J ≍ log n, bounded only when ε ≍ 1/log n.
  - *Tilt comparison with v_{σ_n}.* Removes the leading log-singular part of g_n, but the residual has oscillation of order
    τ²|L₁″(τ)| on [n, n^γ] (τ = log n), bounded only for log-type L₁ (up to an exact power k^ρ).
  - *Structural reason.* QL is a statement about μ_m deep in the hard-edge region, which the o(1) pointwise law of v does
    not see; it is 1/n-order information (the 1/n coefficients of the pure-power expansion fix the Bessel order), which is
    why a Riemann–Hilbert analysis (outline Route II) is the natural route to QL or to Theorem B directly.
- **Bc2 (rate; NUMERICAL, p = s = 2 only; `checks/check_sv_general.out`).** Write ϑ_n := L′(log n) for Ψ = exp(L(log k))
  (the outline calls this ε_n; it is not L0's ε_n — numerically ε_n/ϑ_n ≈ 0.68–0.71 ≈ log 2 for the examples).
  For Ψ = exp(√log(k + e)) and exp((log(k + e))^{0.8}), n = 100 … 1600:
  - n·(β_n(w)/β_n(v) − 1)/ϑ_n = 0.470, 0.481, 0.487, 0.490, 0.491 and 0.475, 0.486, 0.492, 0.494, 0.494 (K = 2.4·10⁵);
    the a_n analogue n·(A_n(w)/A_n(v) − 1)/ϑ_n is 0.479–0.495. K = 1.2·10⁵ vs 2.4·10⁵ agree to ≤ 2·10⁻³ in these ratios (the K-gap grows
    with n: 0, 0, 3·10⁻⁴, 8·10⁻⁴, 1.9·10⁻³ for θ = 0.8, b_n; 2.0·10⁻³ for a_n at n = 1600, so n = 1600 is truncation-limited
    at the 0.2% level),
    and quad vs long double agree to all printed digits (n ≤ 400). So the observed deviation is ≈ ϑ_n/(2n) (the outline's
    "tilt law"; CONJECTURE, not proved).
  - The QL log-moment along the path (t ∈ {0, ¼, ½, ¾, 1}, m ∈ {n − 1, n}, n = 100 … 800, sum truncated at k ≤ K since
    n^γ ≫ K; μ_m(k) for k ≥ m/2 by the three-term recurrence from the RKPW coefficients, which agrees with a fully
    reorthogonalized Lanczos run to 4·10⁻¹³ at n = 100, K = 2·10⁴): sup_tΛ_n = 0.423, 0.419, 0.417, 0.415 (n = 100, 200, 400, 800; K = 4.8·10⁵) flat in t
    (variation ≤ 1.2·10⁻³ at K = 4.8·10⁵, ≤ 1.8·10⁻³ at K = 1.2·10⁵); K = 1.2·10⁵ gives values smaller by ≤ 3.3·10⁻³. In every
    row the sup over t is attained at t = 0, i.e. at the pure power v (so the two weights share it trivially); the t = 1 values
    are smaller by ≤ 1.2·10⁻³ at K = 4.8·10⁵ (1.8·10⁻³ at K = 1.2·10⁵). The slow decrease in n is the approach to the Lemma LP constant ∫_0^∞F_p(e^u)du = 0.4156
    (p = 2; reviewer's computation, REVIEW_Plan44.md). At t = 0, QL with Λ_n = O(1) is a uniform-in-M form of Lemma LP (the
    outline's QLP): supported by these numerics, not proved.
    So ε_n·sup_tΛ_n ≈ 0.068 → 0.057 (√log) and 0.169 → 0.158 (θ = 0.8), decreasing like ε_n, consistent with QL in the
    natural form Λ_n = O(1) (outline QL-a). The trivial bound (γ − 1)log n is 25–37 here. This is a truncated, finite-n
    computation (k ≤ K ≪ n^γ) and is not evidence about the range [K, n^γ] beyond the tail decay it shows.
  - Compared with the observed ϑ_n/(2n), Theorem B-cond's bound O(δ_n(M₀) + ε_n(1 + Λ_n)) is weaker by a factor ≍ n:
    the first-variation bound |⟨g_n, μ_n − μ_{n−1}⟩| ≤ ⟨|g_n|, μ_n + μ_{n−1}⟩ discards the cancellation between μ_n and
    μ_{n−1}. B-cond is a convergence statement, not a rate.
- **Bc3 (scope).** Under QL: every Ψ slowly varying in sequence form, hence (renaming s) every w = k^{−σ}k^{ρ}Ψ with
  σ − ρ > 1 (QL then for the path with s := σ − ρ). The outline's Corollary B1 for a measurable slowly varying ℓ would
  need the Uniform Convergence Theorem to pass to the sequence form; it is not cited (Rule C) and not claimed.
- **Bc4 (Rule A, adversarial pass; logged in LOG.md).** (a) Ψ eventually constant: ε_n = 0 eventually, QL trivial,
  B-cond reduces to T3-conv. (b) L0(i) downward: available only with ε at the lower index (|g_n(k)| ≤ ε_{⌈n/λ⌉}(1 + log₂λ) for
  k ∈ [n/λ, n); see the remark on L0), not with ε_n; the proof never uses it. (c) Is sup_t needed in QL? No: step 1 and step 7 integrate over t, so the
  t-average suffices. (d) Does QL depend on γ? Only through n^γ ≥ T″ and the tail exponent; any γ > κ works, the
  smaller the weaker. (e) Does any step need Ψ bounded? Head: W/w_k ≤ n^{s+2η}·const (Potter); tail: TLw's ratio
  ≤ T″^{s+η}k^{η}·const; FVa off-head constants use only Sat_p⁺ — none needs boundedness. (f) m = n − 1 in QL: the sum
  still starts at k = n with log(k/n), matching L0(i) centred at n.

### 3.18 Commutator lemma CB (Plan 49): boundary-flux identities, a dyadic block bound, and CB ⇒ QL ⇒ law — TV⁺ PROVED (standard extension; novelty not claimed); BF, RF, DB, NO PROVED (NO: attribution only, novelty not claimed); FM (i)–(iii) PROVED, model reading and sharpness of log M for μ_m^{(t)} HEURISTIC (NUMERICAL support); Theorem QL-CB CONDITIONAL (CB(η, a), η ≤ η₀(p, s, α, a)) + PROVED-mod-cite (inherits QLP §3.16: RH_px, RH₁(r), RH_plt1b, KMVV (6.23), Vanlessen (4.27), DLMF 10.25.2/10.32.4/10.32.9 via Lemma BK; B-cond: RH_px, RH₁(r), RH_plt1b); Theorem B-OD CONDITIONAL (OD-E, OD-F); CB itself NOT proved; Remark CB-ob HEURISTIC/OBSTRUCTION (scoped to the routes tried); numerics NUMERICAL; no new case of the law; Rule R ACCEPT WITH FIXES (review/REVIEW_Plan49.md), fixes applied — REVIEWED; novelty UNCHECKED

Source: `research/program/outline_B_sv.md` §5, Route I′. Setting and notation as in §3.14: x_k = k^{−p} (p > 0), v = k^{−s}
(s > 1), w = vΨ with Ψ > 0 slowly varying in sequence form, path w(t) = vΨ^t (t ∈ [0, 1]), f := log Ψ, g := g_n = f − f(n),
ε_n of Lemma L0, q_j = q_j^{(t)}, μ_j = q_j², K_m := Σ_{j<m}q_jq_jᵀ, M₀ the head margin, h_n the head quantity of B-cond
step 2. For real M > 0 put A_M := ℕ ∩ (Mn, ∞), y_M = y_M(t) := μ_m^{(t)}(A_M) (so y_M ≤ 1, nonincreasing in M), and

  X_M = X_{A_M} := ⟨1_{A_M}q_m, K_m(gq_m)⟩,  K_m(gq_m) := Σ_{j<m}⟨gq_m, q_j⟩q_j,  m ∈ {n − 1, n}.

ϑ = ϑ(p, s) := min(p/2, s − 1) is the exponent of Lemma QLP(c) (§3.16, Plan 46, merged to master; used here only at t = 0,
i.e. for the single pure power v = v_σ with σ = s, so hypothesis (RU) of §3.16 is not needed).

**Summary.** (1) The commutator term has exact "boundary-flux" forms (Lemma BF), and the TV derivative is a flux of the
kernel K_m + K_{m+1} across ∂A (BF(ii)); for deep A it is the μ_m-average over A of one rational function R_m = P_m/p_m
(Lemma RF). (2) In the Toeplitz (free) model the commutator term is exactly half the covariance, so the TV derivative
vanishes identically, and X/μ(A) = (ε/p)(1 + log(1/φ)) + O(φ²) (Proposition FM): the factor 1 + log M in CB is sharp in the free model (PROVED there; relevance to μ_m^{(t)} HEURISTIC;
NUMERICAL agreement, `check_cb.out` [3]).
(3) A dyadic block bound (Lemma DB) splits X into row-blocks of the spectral-projection matrix and of g; numerically it
loses at most a factor 1.3 (`check_cb.out` [4]). (4) **CB ⇒ QL ⇒ law** (Theorem QL-CB): a Grönwall argument in a scale of
power moments Y_β (Nishida–Ovsyannikov, Lemma NO), started from QLP at t = 0. It needs CB only with a *small* constant
η ≤ η₀(p, s, α, a), not necessarily with η ∝ ε_n. Together with DB: two concrete block bounds (OD-E, OD-F) along the path ⇒ Law P
(Theorem B-OD). (5) **CB is not proved.** The obstruction (Remark CB-ob) is that the block bounds need the sharp
hard-edge *density*, not tails, and tail transport loses a factor M^{Cε} which feeds back into the commutator rate; the
loop closes only when ε_n log n = O(1), i.e. for log-type Ψ (already covered by T3-log). **No new case of the law is
proved.** (Cross-reference: Plan 48 (§3.17, Route II, branch plan-48-route2; in review at the time of writing) claims the law directly, without QL, for p > 1, 1 < s < 1 + 2p and every sequence-form Ψ (including D(γ) = ∞). If that review accepts it, the prospective new content of QL-CB/B-OD is (i) the regimes p ≤ 1 and s ≥ 1 + 2p and (ii) QL itself along the path, which Plan 48 does not give.)

**Lemma TV⁺ (TV for unbounded f; PROVED, standard extension of §3.8, novelty not claimed).** Let x_k ∈ (0, 1] be distinct,
v_k > 0, f_k real with Σ_kU_k < ∞, U_k := v_k max(1, e^{f_k})(1 + |f_k|) (the hypothesis of FV⁺), and w(t) := ve^{tf}.
Then for every m ≥ 0 and A ⊂ ℕ, t ↦ μ_m^{(t)}(A) is C¹ on [0, 1], every ⟨fq_m, q_j⟩ converges absolutely, and

  (d/dt)μ_m(A) = ⟨f1_A, μ_m⟩ − 2⟨1_Aq_m, K_m(fq_m)⟩ − ⟨f, μ_m⟩μ_m(A).

*Proof.* The moments m_i(t) = Σ_kw_k(t)x_k^i (i ≤ 2m + 2) are C¹ by the M-test (|∂_tw_k(t)x_k^i| ≤ U_k). The coefficients of
p_m^{(t)} are rational in the m_i with denominators √(D_mD_{m+1}) > 0 (infinitely many atoms), hence C¹; so on [0, 1]
C_m := sup_t sup_{x∈[0,1]}(|p_m| + |ṗ_m|) < ∞ for each m. Then |∂_t(w_k(t)p_m^{(t)}(x_k)p_j^{(t)}(x_k))| ≤ 3C_mC_jU_k, so
μ_m^{(t)}(A) = Σ_{k∈A}w_kp_m(x_k)² and ⟨q_m, q_j⟩ = Σ_kw_kp_mp_j can be differentiated termwise, and Σ_k|f_k|w_k|p_mp_j| ≤
C_mC_jΣU < ∞. Write q̇_m = ½fq_m + √w ṗ_m (pointwise), deg ṗ_m ≤ m. Differentiating ⟨q_m, q_j⟩ = δ_{mj}:
⟨fq_m, q_j⟩ + ⟨√wṗ_m, q_j⟩ + ⟨q_m, √wṗ_j⟩ = 0 (each a finite or absolutely convergent sum). For j < m the last term is 0
(deg ṗ_j < m), and for j = m the second and third are equal; so √wṗ_m = −Σ_{j<m}⟨fq_m, q_j⟩q_j − ½⟨f, μ_m⟩q_m (the
coefficients of the polynomial ṗ_m in the basis p_0, …, p_m). Hence (d/dt)μ_m(A) = Σ_{k∈A}(f_kμ_m(k) + 2q_m(k)(√wṗ_m)(k))
is the formula. ∎ *Application:* f = log Ψ, v = k^{−s}: ΣU < ∞ by L0(ii) (§3.14, "Application of FV⁺").

**Lemma BF (boundary-flux identities; PROVED, elementary).** Let σ = Σ_kw_kδ_{x_k} be any measure on distinct atoms with finite
moments, f real with Σ_k|f_k|w_k(1 + |x_k|)^{2m+2} < ∞, A any set of atoms, A^c its complement, and μ = μ_m, K_m as above
(so K_m(k, l) = Σ_{j<m}q_j(k)q_j(l)). Then, with absolutely convergent double sums,

- (i) X_A := ⟨1_Aq_m, K_m(fq_m)⟩ = Σ_{k∈A, l∈A^c} q_m(k)K_m(k, l)q_m(l)·(f(l) − f(k));
- (ii) Cov_μ(f, 1_A) − 2X_A = Σ_{k∈A, l∈A^c} q_m(k)(K_m + K_{m+1})(k, l)q_m(l)·(f(k) − f(l)); so, under TV⁺, this flux is
  (d/dt)μ_m(A);
- (iii) (Christoffel–Darboux form of (ii)) with ψ := b_{m+1}q_mq_{m+1} − b_mq_{m−1}q_m (the Toda density of FVa, §3.12):
  Cov_μ(f, 1_A) − 2X_A = Σ_{k∈A, l∈A^c}[μ(l)ψ(k) − μ(k)ψ(l)]·(f(k) − f(l))/(x_k − x_l).

*Proof.* Absolute convergence: |q_j(k)| = √w_k|p_j(x_k)| ≤ C_j√w_k(1 + |x_k|)^j, so every summand is ≤ C w_kw_l(1 + |x_k|)^{2m+2}(1 + |x_l|)^{2m+2}(|f_k| + |f_l|).
(i) Σ_lK_m(k, l)q_m(l) = Σ_{j<m}q_j(k)⟨q_j, q_m⟩ = 0, so X_A = Σ_{k∈A}Σ_l q_m(k)K_m(k, l)q_m(l)(f(l) − f(k)); the part
l ∈ A is antisymmetric under k ↔ l (K_m symmetric) and vanishes. (ii) K_{m+1} = K_m + q_mq_mᵀ; the q_mq_mᵀ part of the
flux is Σ_{k∈A, l∉A}μ(k)μ(l)(f(k) − f(l)) = μ(A^c)⟨f1_A, μ⟩ − μ(A)⟨f1_{A^c}, μ⟩ = Cov_μ(f, 1_A), and the 2K_m part is
−2X_A by (i). (iii) Christoffel–Darboux for K_m and K_{m+1} (k ≠ l): q_m(k)K_m(k, l)q_m(l) = b_m[μ(k)π₋(l) − π₋(k)μ(l)]/(x_k − x_l)
with π₋ := q_{m−1}q_m, and q_m(k)K_{m+1}(k, l)q_m(l) = b_{m+1}[π₊(k)μ(l) − μ(k)π₊(l)]/(x_k − x_l) with π₊ := q_mq_{m+1}; add. ∎

*Reading.* By (i) X_A only sees pairs straddling ∂A, weighted by the jump f(l) − f(k); by L0(i) this jump is
≤ ε_n(1 + log₂(k/l)) for n ≤ l < k, without any smoothness of Ψ. So CB is the statement that the "flux" of the kernel
K_m across ∂A_M, weighted by log₂(k/l), is ≲ μ_m(A_M) up to log M. (ii)–(iii) show that the full TV derivative is a flux of
the averaged kernel ½(K_m + K_{m+1}) and, in CD form, of the oscillating Toda density ψ (Σψ = 0; for f = x, (iii) is the Toda
flow μ̇_m = ψ). (The double sum in (iii) converges absolutely as a whole, being a termwise rewriting of (ii); it must not be
split into the μ(l)ψ(k) and μ(k)ψ(l) parts, since 1/(x_k − x_l) is unbounded at the accumulation point. Conventions:
q_{−1} := 0, K_0 := 0, b_0 := 0; RF and z₁(m) are for m ≥ 1.) The absolute-value bound of (iii) with |ψ| ≲ n^{−p}(μ_{m−1} + μ_m + μ_{m+1}) loses a factor M^{p/2}
(the hard-edge mass weighted by b_m/x_l); any useful bound must use the cancellation inside ψ (or inside
μ(k)π(l) − π(k)μ(l)), i.e. the phase structure of (q_{m−1}, q_m, q_{m+1}) at the hard edge.

**Lemma RF (the commutator term as one rational function; PROVED).** In the setting of BF, put P_m := Σ_{j<m}⟨fq_m, q_j⟩p_j
(a polynomial of degree < m, so K_m(fq_m) = √w P_m) and R_m := P_m/p_m. Then X_A = Σ_{k∈A, p_m(x_k)≠0} μ_m(k)R_m(x_k) (atoms
with p_m(x_k) = 0 have μ_m(k) = 0). Hence |X_A| ≤ μ_m(A)·sup_{k∈A, p_m(x_k)≠0}|R_m(x_k)|, and if A ⊂ {x < τ} with τ below the
smallest zero z₁(m) of p_m (> 0, as σ lives on (0, 1]), then X_A/μ_m(A) lies in the range of the rational function R_m on [0, τ]
(no poles there); for deep A (τ ↓ 0) X_A/μ_m(A) → R_m(0) = P_m(0)/p_m(0).

*Proof.* q_m(k)·√w_kP_m(x_k) = w_kp_m(x_k)P_m(x_k) = μ_m(k)P_m(x_k)/p_m(x_k). ∎

*Use.* This makes exact the observation of the Plan 45 review (REVIEW_Plan45.md): beyond the Bessel (hard-edge) scale
X_M/y_M → R_m(0) for any f, so the saturation of X/μ(A) there is structural and is **not** evidence for the multiplicative
form of CB in the arcsine range. What the deep-tail data *do* test is a different, sharper statement: by RF, CB for all
A ⊂ {x < z₁(m)/2} is implied by sup_{[0, z₁(m)/2]}|R_m| ≲ ε_n log n, i.e. |P_m| ≲ ε_n log n·|p_m| on the zero-free hard-edge
interval (there log M ≳ (2/p)log n − C, z₁ being at the Bessel scale). The converse fails: CB carries the factor 1 + log M,
unbounded as M → ∞, so it constrains only log M-weighted tail averages of R_m and gives no bound on R_m(0); |R_m(0)| ≲ ε_n log n
is a separate, sharper statement that CB does not contain. Numerically R_m(0) = (0.63–0.74)·ε_n log n (p = 2) and (0.93–1.00)·ε_n log n (p = 1)
(`check_cb.out` [5]), while Cauchy–Schwarz would only give |R_m(0)| ≤ ‖gq_m‖/√μ_m(A) → ∞.

**Proposition FM (free model: exact cancellation; PROVED, Fourier computation; relevance HEURISTIC).** For 0 < φ < π let
h := 1_{(π−φ, π+φ)} and F(θ) := −2log|cos(θ/2)| on 𝕋 = ℝ/2πℤ, with Fourier coefficients ĥ(0) = φ/π, ĥ(d) = (−1)^d sin(dφ)/(πd),
F̂(d) = (−1)^d/|d| (d ≠ 0). Then
- (i) S(φ) := Σ_{d≥1}ĥ(d)F̂(d) = Cl₂(φ)/π, where Cl₂(φ) := Σ_{d≥1}sin(dφ)/d² = −∫_0^φlog(2sin(u/2))du;
- (ii) Cov_{dθ/2π}(F, h) = 2S(φ);
- (iii) Cl₂(φ)/φ = 1 + log(1/φ) + r(φ), 0 ≤ r(φ) ≤ φ²/60.

*Model reading.* On ℓ²(ℤ), J₀ := c(2 + S + S*) (S the shift, c = c(p)) is unitarily equivalent (e_j ↦ e^{ijθ}) to
multiplication by y(θ) = 2c(1 + cos θ); the spectral measure of e₀ is dθ/2π, i.e. the arcsine law of Lemma LP. Take m = 0,
K := the projection onto span{e_j : j < 0} (the model of K_m), A := {y < τ} (the arc |θ − π| < φ, 1 − cos φ = τ/(2c);
τ = M^{−p} models A_M, since n^px_k = (k/n)^{−p}), and f := −(ε/p)log(y/(4c)) = (ε/p)F (the model of
g_n ≈ ε log(k/n) + const). Then X := ⟨1_Ae₀, Kfe₀⟩ = Σ_{j<0}ĥ(j)(ε/p)F̂(j) = (ε/p)S(φ), and by (ii)
**Cov(f, 1_A) − 2X = 0**: in the model the TV derivative vanishes identically (the upward and downward neighbours of e₀
cancel: by BF(ii) the flux kernel is the reflection-symmetric K + K₊), and by (iii)

  X/μ(A) = (ε/p)(1 + log(1/φ)) + O(εφ²),  log(1/φ) = (p/2)log M + ½log c(p) + O(M^{−p}).

So R = X/μ(A) ≈ (ε/2)log M: in the model the log M in CB is necessary (no o(log M) form holds there; for μ_m^{(t)} this is
HEURISTIC, with NUMERICAL agreement below) and the constant is ½ in units
of the local tilt; with ε ≈ ϑ_n (the tilt L′(log n)) and L0's ε_n ≈ ϑ_n log 2 this predicts R/(ε_n(1 + log M)) ≈ 0.72 for large
M, the size seen in Plan 45 and in `check_cb.out` [3] (0.55–0.74; R/R_FM = 0.86–0.93 at p = 2 and 0.69–0.88 at p = 1 on the
printed rows with M ≤ n^{2/p}/4).

*Proof.* (i) ĥ(d)F̂(d) = sin(dφ)/(πd²). For 0 < u < 2π, Σ_{d≥1}cos(du)/d = −log(2sin(u/2)) (real part of −log(1 − e^{iu}) =
Σe^{idu}/d, Abel's theorem; the series converges by Dirichlet's test), uniformly on compacts of (0, 2π); integrating from 0
(the series Σsin(dφ)/d² converges uniformly on 𝕋) gives the integral form. The same expansion at u = θ + π gives
log|cos(θ/2)| = −log 2 − Σ_{d≥1}(−1)^dcos(dθ)/d, hence F = 2log 2 + Σ_{d≠0}(−1)^de^{idθ}/|d| in L²(𝕋), which is F̂.
(ii) Parseval: ∫Fh dθ/2π = Σ_{d∈ℤ}F̂(d)ĥ(−d) = F̂(0)ĥ(0) + 2S (both sequences real and even), and ∫F dθ/2π·∫h dθ/2π =
F̂(0)ĥ(0). (iii) Cl₂(φ) = −∫_0^φlog u du − ∫_0^φlog(2sin(u/2)/u)du = φ − φlog φ + ∫_0^φ|log(sin(u/2)/(u/2))|du, and for
0 < x ≤ π/2, 0 ≤ −log(sin x/x) ≤ x²/5: indeed −log(sin x/x) = Σ_{k≥1}−log(1 − x²/(k²π²)) has nonnegative Taylor
coefficients in x², so −log(sin x/x)/x² is nondecreasing on (0, π), and at x = π/2 it equals log(π/2)/(π²/4) = 0.1830 ≤ 1/5.
So 0 ≤ r ≤ φ²/60. ∎

**Lemma DB (dyadic block bound; PROVED, elementary).** In the setting of BF with additionally Σ_kf_k²μ_m(k) < ∞, put, for
1 ≤ d ≤ m, E_d := ⟨1_Aq_m, q_{m−d}⟩ and G_d := ⟨fq_m, q_{m−d}⟩, so that X_A = Σ_{d=1}^mE_dG_d. For i ≥ 0 let
B_i := [2^i, 2^{i+1}) ∩ [1, m], a_i := (Σ_{d∈B_i}E_d²)^{1/2}, e_i := (Σ_{d∈B_i}G_d²)^{1/2}. Then:
- (a) |X_A| ≤ Σ_ia_ie_i.
- (b) a_i ≤ (|B_i|·μ_m(A)·max_{d∈B_i}μ_{m−d}(A))^{1/2} and Σ_ia_i² = ‖K_m(1_Aq_m)‖² ≤ μ_m(A)(1 − μ_m(A)) (Bessel, as in §3.11).
- (c) (Jackson form) for every polynomial P with deg P ≤ D: Σ_{d>D}G_d² ≤ Σ_k(f_k − P(x_k))²μ_m(k), and the same for E with
  1_A in place of f. So e_i ≤ ℰ_{2^i−1}(f; μ_m) and a_i ≤ ℰ_{2^i−1}(1_A; μ_m), ℰ_D(φ; μ) := inf_{deg P≤D}‖φ − P‖_{L²(μ)}.
- (d) If, for all i with 2^i ≤ m, (OD-E) a_i ≤ C_E min(2^{i/2}y, 2^{−i/2}) and (OD-F) e_i ≤ C_Fε2^{−i/2}, with y := μ_m(A), then
  |X_A| ≤ C_EC_Fε·y(3 + log₂(1/y)); and for any a > 0, y log₂(1/y) ≤ (a/log 2)y log M + M^{−a}/(e log 2) for every M ≥ 1.

*Proof.* (a) Cauchy–Schwarz in each block. (b) |E_d| ≤ ‖1_Aq_m‖‖1_Aq_{m−d}‖; Σ_dE_d² = Σ_{j<m}⟨1_Aq_m, q_j⟩² =
‖K_m(1_Aq_m)‖², and 1_Aq_m = K_m(1_Aq_m) + μ_m(A)q_m + (rest), pairwise orthogonal. (c) Pq_m = √w·Pp_m and
⟨Pp_m, p_j⟩_σ = ⟨p_m, Pp_j⟩_σ = 0 for j + D < m, so ⟨Pq_m, q_{m−d}⟩ = 0 for d > D and G_d = ⟨(f − P)q_m, q_{m−d}⟩ there; Bessel.
(d) Σ_{i≥0}min(y, 2^{−i}) ≤ y·(1 + log₂(1/y)) + 2y. For the last claim write y log(1/y) = ay log M + M^{−a}·u log(1/u) with
u := yM^a, and u log(1/u) ≤ 1/e for u ≤ 1, < 0 for u > 1. ∎

*Numerics (`check_cb.out` [4]).* DB is nearly lossless: Σ_ia_ie_i/|X_M| ≤ 1.26 over p ∈ {2, 1}, n ∈ {50, …, 400} (p = 2),
n ∈ {50, 100, 200} (p = 1), t ∈ {0, ½, 1}, all tested M (down to μ_m(A) ≈ 10^{−11}). (OD-E) and (OD-F) hold on the same data
with C_E ≤ 1.03 and C_F ≤ 0.68 (p = 2), 1.26 (p = 1), flat in n and t (OD-F does not depend on A; OD-E's maximum is the d = 1
block, |E_1| ≈ y, i.e. row coherence μ_{m−1}(A) ≈ μ_m(A)). So the content of CB is carried, with a loss ≤ 1.26, by the
two block bounds.

**Lemma NO (comparison in a scale; PROVED; the name Nishida–Ovsyannikov is attribution only, the proof is self-contained,
novelty not claimed).** Let 0 < α < α₂, κ > 0, T₀ > 0, a ≥ 0, and let u: [α, α₂] × [0, T₀] → [0, ∞) be jointly continuous
(monotonicity in β is not needed), with

  u_β(t) ≤ a + ∫_0^tκ·u_{β′(r)}(r)/(β′(r) − β) dr

for every β ∈ [α, α₂), t ∈ [0, T₀] and every continuous β′: [0, t] → (β, α₂]. Then u_β(t) ≤ 2a/(1 − 8κt/(α₂ − β)) whenever
8κt < α₂ − β.

*Proof.* Put T := 1/(8κ), c_β := α₂ − β, D := {(β, t): t < Tc_β} and N := sup_Du_β(t)(1 − t/(Tc_β)) ≤ sup u < ∞. For
(β, t) ∈ D take β′(r) := β + (c_β − r/T)/2 (r ≤ t). Then β′ − β = (c_β − r/T)/2 > 0, c_{β′} = (c_β + r/T)/2 and r < Tc_{β′}, so
u_{β′(r)}(r) ≤ N·c_{β′}/(c_{β′} − r/T) = N(c_β + r/T)/(c_β − r/T). Hence the integrand is ≤ 4κNc_β/(c_β − r/T)², and
u_β(t) ≤ a + 4κNc_βT(1/(c_β − t/T) − 1/c_β) ≤ a + 4κTN·c_β/(c_β − t/T). Multiplying by (c_β − t/T)/c_β ≤ 1:
u_β(t)(1 − t/(Tc_β)) ≤ a + N/2. Taking the sup, N ≤ 2a. ∎

**Hypothesis CB(η, a) (for the given Ψ; HYPOTHESIS).** There is n₀ such that for n ≥ n₀, m ∈ {n − 1, n}, t ∈ [0, 1] and all
real M ≥ 1:

  |X_M(t)| ≤ η[(1 + log M)y_{M/2}(t) + ∫_M^∞y_{M′}(t)dM′/M′ + M^{−a}].

The outline's form "|X| ≤ Cε_nμ_m(A)(1 + log M) + (head/far-tail terms)" is CB(Cε_n, a) when the error terms are ≤ Cε_nM^{−a};
the deeper-layer integral and the enlargement y_{M/2} are allowed because every proof route through DB produces them. In the
free model (FM) |X| ≤ (ε/p)(1 + log(1/φ) + φ²)μ(A).

**Theorem QL-CB (CB ⇒ QL-b ⇒ QL ⇒ Law P; CONDITIONAL (CB(η, a), η ≤ η₀(p, s, α, a)) + PROVED-mod-cite (inherits QLP at t = 0,
§3.16: RH_px, RH₁(r), RH_plt1b, KMVV (6.23), Vanlessen (4.27), DLMF 10.25.2/10.32.4/10.32.9 via Lemma BK; B-cond: RH_px, RH₁(r), RH_plt1b)).** Let x_k = k^{−p} (p > 0), w = k^{−s}Ψ (s > 1) with Ψ slowly varying in sequence form. Fix 0 < α < ϑ(p, s) and
a > α. There is η₀ = η₀(p, s, α, a) > 0 such that, if CB(η, a) holds with η ≤ η₀, then there are C, n₁ with

  sup_{t∈[0,1]}μ_m^{(t)}((Mn, ∞)) ≤ C·M^{−α}  for all M ≥ 1, n ≥ n₁, m ∈ {n − 1, n}  (QL-b),

hence (Lemma QLb) Λ_n ≤ (1 + log C)/α, QL holds, and (Theorem B-cond) n^pb_n(w) → c(p), n^pa_n(w) → 2c(p). In particular
CB(C_Bε_n, a) with any constant C_B suffices (η = C_Bε_n → 0).

*Proof.* Constants: α₂ := (α + min(ϑ, a))/2, ϑ′ := (α₂ + min(ϑ, a))/2 < ϑ, L := α₂ − α.
0. **Start (t = 0).** w(0) = v = v_s. By QLP(c) (fixed σ = s), y_M(0) ≤ C_{ϑ′}M^{−ϑ′} for n ≥ n₀, m ∈ {n − 1, n}, M ≥ 1. Put
   Y_β(t) := Σ_kmax(1, k/n)^βμ_m^{(t)}(k) = 1 + β∫_1^∞M^{β−1}y_M(t)dM (layer cake). Then Y_β(0) ≤ a₀ := 1 + α₂C_{ϑ′}/(ϑ′ − α₂)
   for β ≤ α₂.
1. **A priori finiteness and continuity.** Fix n. Choose η₁ > 0 with α₂ < s − 1 − 2η₁ (α₂ < ϑ ≤ s − 1). By B-cond step 5 (TLw with
   Potter), μ_m^{(t)}(k) ≤ C_nk^{−s+η₁} for k > T″, uniformly in t (C_n depends on n). So the series for Y_β, β ≤ α₂, converge
   uniformly in (β, t); each term is continuous in (β, t) (TV⁺); hence (β, t) ↦ Y_β(t) is jointly continuous and bounded on
   [α, α₂] × [0, 1], and nondecreasing in β.
2. **Integrated TV⁺.** For each M, y_M(t) − y_M(0) = ∫_0^tẏ_M(r)dr with ẏ_M = ⟨g1_{A_M}, μ⟩ − ⟨g, μ⟩y_M − 2X_M (TV⁺ with f
   replaced by g, allowed by invariance under constants). The same tail bound gives |ẏ_M(r)| ≤ C′_nM^{1−s+2η₁} for M large
   (|X_M| ≤ Σ_{j<m}√(y_Mμ_j(A_M))|⟨gq_m, q_j⟩| and μ_j ≤ ρ_{n+1}), so by Fubini Y_β(t) − Y_β(0) = ∫_0^tR_β(r)dr with
   R_β := β∫_1^∞M^{β−1}ẏ_MdM. We bound R_β(r) at a fixed r; let β < β′ ≤ α₂, δ := β′ − β.
   - (I) β∫M^{β−1}⟨g1_{A_M}, μ⟩dM = Σ_kg(k)μ(k)(max(1, k/n)^β − 1) (Tonelli). Only k > n contribute, where |g(k)| ≤
     ε_n(1 + log₂(k/n)) (L0(i)); with log₂u ≤ u^δ/(eδ log 2) (u ≥ 1): |(I)| ≤ ε_n(1 + 1/(eδ log 2))Y_{β′}.
   - (II) β∫M^{β−1}⟨g, μ⟩y_MdM = ⟨g, μ⟩(Y_β − 1), and |⟨g, μ⟩| ≤ h_n + δ_n(M₀) + ε_nΣ_{k≥n}(1 + log₂(k/n))μ(k) ≤
     ω_n + ε_nY_α/(eα log 2), ω_n := h_n + δ_n(M₀) + ε_n → 0 (head: B-cond step 2; lower bulk: δ_n(M₀); log u ≤ u^α/(eα)).
   - (III) By CB(η, a), 2β∫_1^∞M^{β−1}|X_M|dM ≤ 2βη[I₁ + I₂ + I₃] with, substituting M = 2u and using y_u ≤ 1 for u ≤ 1 and
     1 + log 2 + log u ≤ (1 + log 2) + u^δ/(eδ) for u ≥ 1:
     I₁ = ∫_1^∞M^{β−1}(1 + log M)y_{M/2}dM ≤ 2^β[(1 + log 2)/β + (1 + log 2)(Y_β − 1)/β + (Y_{β′} − 1)/(eδβ′)];
     I₂ = ∫_1^∞M^{β−1}∫_M^∞y_{M′}dM′/M′ dM = ∫_1^∞y_{M′}(M′^β − 1)/(βM′)dM′ ≤ (Y_β − 1)/β²;
     I₃ = ∫_1^∞M^{β−1−a}dM = 1/(a − β).
     Since α ≤ β ≤ β′ ≤ α₂ < a, 1 ≤ Y_β ≤ Y_{β′} and δ ≤ L: |(III)| ≤ ηC₃(1 + 1/δ)Y_{β′} with C₃ = C₃(α, α₂, a)
     (C₃ := 2^{α₂+1}(1 + log 2) + 2/α + 2α₂/(a − α₂) works).
   Altogether, using Y_β ≤ Y_{β′} and 1 + 1/δ ≤ (L + 1)/δ:

     R_β(r) ≤ κ(r)·Y_{β′}(r)/(β′ − β),  κ(r) := (L + 1)[ε_n(1 + 1/(e log 2)) + ω_n + ε_nY_α(r)/(eα log 2) + C₃η].

3. **Bootstrap and Lemma NO.** Let T* := sup{t ≤ 1: Y_α(r) ≤ 8a₀ for r ≤ t} (> 0 by continuity, Y_α(0) ≤ a₀). On [0, T*],
   κ(r) ≤ κ* := (L + 1)[ε_n(2 + 8a₀/(eα log 2)) + ω_n + C₃η]. Lemma NO (u = Y on [α, α₂] × [0, T*], with the inequality of step 2
   applied at each r with β′ = β′(r)) gives Y_β(t) ≤ 2a₀/(1 − 8κ*t/(α₂ − β)). If 16κ* ≤ L, then at β = α, Y_α(t) ≤ 4a₀ < 8a₀
   on [0, T*], so T* = 1 by continuity. The condition 16κ* ≤ L holds for n ≥ n₁ if η ≤ η₀ := L/(32(L + 1)C₃), since ε_n, ω_n → 0.
4. **Conclusion.** For n ≥ n₁, t ∈ [0, 1], m ∈ {n − 1, n}: Y_α(t) ≤ 4a₀, so y_M(t) ≤ Y_α(t)M^{−α} ≤ 4a₀M^{−α} (Markov). This is
   QL-b with C = 4a₀; Lemma QLb and Theorem B-cond finish. ∎

*Remarks on QL-CB.* (1) The Grönwall is multiplicative but in *moments*, not in y_M: the rate ε_n log M of the pointwise
Grönwall (which would give the factor M^{Cε_n}, unbounded on M ≤ n^γ when ε_n log n → ∞) becomes a loss δ in the moment
order, which Lemma NO absorbs for every α < ϑ — this is why no "additive floor" (Bc1) appears. (2) The proof uses CB only
through (III), so the hypothesis can be replaced by the same bound on the transport defect T_M := ẏ_M = Cov(g, 1_{A_M}) − 2X_M
(then (I)–(II) and the bootstrap are not needed); in the free model T ≡ 0 (FM). Numerically |T_M| ≤ 0.58·ε_ny_M(1 + log M),
small (≤ 0.05 at p = 2, ≤ 0.10 at p = 1 on the printed rows with M ≤ n^{2/p}/4) in the arcsine range and ≈ ½ε_ny_M(1 + log M) beyond the Bessel scale, where the far tail genuinely tilts
(slope −(s − 1) → −(s − 1) + O(ε), Plan 45 N2). (3) CB is needed with a small *absolute* constant η₀, not with η ∝ ε_n; so
CB "with a constant ≤ η₀(p, s, α, a)" for M in the whole range is a sufficient condition (no necessity is shown); the
outline's form CB(C_Bε_n, a) meets the smallness automatically for n large, since ε_n → 0. (4) Only QLP at t = 0 for σ = s is
used: no uniformity in σ, no (RU).

**Theorem B-OD (block bounds ⇒ Law P; CONDITIONAL on (OD-E), (OD-F) along the path).** Let Ψ be as in QL-CB. Suppose there
are C_E, C_F, n₀ such that for n ≥ n₀, m ∈ {n − 1, n}, t ∈ [0, 1], M ≥ 1 and all i with 2^i ≤ m, the block norms of Lemma DB for
A = A_M, f = g_n satisfy (OD-E) a_i ≤ C_E min(2^{i/2}y_M, 2^{−i/2}) and (OD-F) e_i ≤ C_Fε_n2^{−i/2}. Then n^pb_n(w) → c(p) and
n^pa_n(w) → 2c(p).

*Proof.* By DB(d) with a := ϑ: |X_M| ≤ C_EC_Fε_n[(3 + a/log 2)(1 + log M)y_M + M^{−a}/(e log 2)], and
y_M ≤ y_{M/2}; this is CB(η_n, a) with η_n := C_EC_F(3 + a/log 2)ε_n → 0. Apply Theorem QL-CB with α := a/2. ∎

**What is not proved, and why (Remark CB-ob; OBSTRUCTION, HEURISTIC — about the routes tried here, not about all routes).**
- *The missing statements* are (OD-E) and (OD-F) (or CB itself) along the path, uniformly in t, M and n. (OD-F) is a weighted
  polynomial-approximation statement: by DB(c), e_i ≤ ℰ_{2^i−1}(g_n; μ_m^{(t)}), and a Jackson-kernel argument in the arcsine
  angle θ (x = a(1 + cos θ)/2 on a window [0, a] ⊃ supp of the bulk) gives ℰ_D(g_n; μ_m) ≲ ε_nD^{−1/2} **if** g_n is smooth in
  log x (|∂_{log x}g_n| ≲ ε_n; e.g. Ψ₁ of the outline's RedA; after merge, Plan 48's Lemma RedA, §3.17) **and** μ_m has bounded density in θ near the hard edge, μ_m(|θ − π| < r) ≲ r
  for r ≥ 1/D (ED). It also needs control of the polynomial outside [0, a] against the head (Sat_p⁺), which caps D at θ₀n.
  (OD-E) additionally needs the 1/d decay |E_d| ≲ min(y, 1/d) of the spectral-projection row, i.e. a phase coherence between
  rows m and m − d at the hard edge (in the free model E_d = ĥ(d) = O(1/d) because 1_A has bounded variation in θ).
  None of this is written here as a proof.
- *Why tail transport does not supply them (exponent feedback).* Every bound available along the path (Theorem L-type
  transport, the moment Grönwall above) propagates **tails** with a loss M^{Cε}: from y_M(0) ≲ M^{−p/2} it gives y_M(t) ≲
  M^{−p/2+Cε}, i.e. a near-edge density ≲ r^{−2Cε/p} instead of ≲ 1. Fed into DB(c) this gives e_i ≲ ε2^{−i(1/2 − Cε/p)}, and
  DB then gives |X_M| ≲ εy_M log M·M^{O(ε)} — a commutator rate inflated by M^{O(ε)}, which over M ≤ n^{2/p} (and the block range
  D ≤ θ₀n) is n^{O(ε_n)}, unbounded exactly when ε_n log n → ∞, i.e. when D(γ) = ∞. Feeding the inflated rate back into the
  Grönwall loses more exponent; the loop closes only if ε_n log n = O(1) (log-type Ψ, already T3-log). With only moment
  information of order β < p/2 the estimate is not even linear in the moments: the small blocks give
  Σ_{2^i<1/y}√(2^iy·y)·2^{−iβ/p} ≈ y^{1/2+β/p} ≫ y. This is the same 1/n-level ("density, not tail") phenomenon as Bc1's
  structural remark; the free model shows that the truth is benign (X ≈ (ε/p)y log(1/φ) even for distorted edges, and the
  TV derivative cancels), but the cancellation is a statement about the oscillatory structure of q_m, q_{m±1} at the hard edge.
- *The CS bound* |X_M| ≤ √y_M‖K_m(gq_m)‖ ≤ √y_M·Var_μ(g)^{1/2} (§3.8) is far from the truth in the deep range: X/(√y‖gq_m‖)
  falls from 0.36 to 10^{−5} over the tested range, but this is the structural RF limit (`check_cb.out` [3]); in the arcsine window alone (M ≲ n^{2/p}) the data do not separate the
  CB scale from the CS scale (window too short at n ≤ 400), so the arcsine-range evidence for CB is the agreement with the free
  model (R/R_FM = 0.86–1.03 at p = 2 for M ≤ n^{2/p}; 0.86–0.93 for M ≤ n^{2/p}/4), and the deep-range evidence is the RF statement |R_m(0)| ≈ 0.7ε_n log n (structural form,
  REVIEW_Plan45.md).
- *Route-II information would close it.* (ED) and the row phases are exactly what a hard-edge Bessel parametrix along the path
  provides (outline Route II; QLP's Lemma ST-type bounds give tails only, which is why §3.16 stops at t = 0). Plan 48 (§3.17, Route II, branch plan-48-route2; in review at the time of writing) claims the law directly, without QL, for p > 1, 1 < s < 1 + 2p and every sequence-form Ψ (including D(γ) = ∞). If that review accepts it, the prospective new content of QL-CB/B-OD is (i) the regimes p ≤ 1 and s ≥ 1 + 2p and (ii) QL itself along the path, which Plan 48 does not give.

**Rule A (adversarial pass).** (a) f constant, or A = ∅, or A = all atoms: X_A = 0 in BF(i), and the CB right side ≥ 0. ✓
(b) Invariance f ↦ f + c: BF(i), (ii) and RF unchanged (P_m unchanged since ⟨q_m, q_j⟩ = 0, j < m). ✓ (c) Is the log M in CB
removable? Not in the free model: FM gives X/μ(A) = (ε/p)(1 + log(1/φ)) + O(φ²) exactly there (for μ_m^{(t)}: HEURISTIC, NUMERICAL
support `check_cb.out` [3]). (d) Is the small constant in QL-CB
necessary? The argument needs 16κ* ≤ L; with a large η the moment rate exceeds the scale width and Lemma NO gives nothing
(no claim that the conclusion fails). (e) Sign of X: positive in every tested case (as in Plan 45) and in FM (Cl₂ > 0 on
(0, π)); not used. (f) Rough f (Theorem R): for |f| ≤ ε with fixed-size roughness at scale n, the G_d do not decay (e_i ≍ ε for
all i), so (OD-F) fails, consistent with the failure of the law there; QL-CB itself is stated only for slowly varying Ψ ((I),
(II) use L0). (g) Deep tail with p_m(0) small: RF needs p_m(x_k) ≠ 0 only on A; z₁(m) > 0 always; R_m(0) is finite. (h) The
substitution M = 2u in I₁ covers u ∈ [½, 1] where y_u ≤ 1. ✓ (i) Fubini in step 2: the M-integrand is O(M^{β+1−s+2η₁−1})
with β + 1 − s + 2η₁ < 0 for η₁ small (α₂ < s − 1). ✓ No counterexample found.

**Numerics (NUMERICAL; `checks/check_cb.py/.out`, s = 2, Ψ = exp(√log(k + e)), float64 Lanczos with full reorthogonalization
on atoms k ≤ 6·10⁴ plus a Gauss–Legendre log-panel tail to 10^{16} as in Plan 45).** Following REVIEW_Plan45.md, p = 2
(discriminates best) and p = 1 are used and p = ½ is omitted. All rows use m = n only (not m = n − 1).
- [1] BF(i), BF(ii), RF and TV agree with direct computation and with a central finite difference in t to 9–10 digits
  (K = 3000, p = 2, n = 30, t = ½).
- [2] FM: S(φ) = Cl₂(φ)/π and Cov = 2S to 10 digits (φ = 0.5, 0.1, 0.01); S/μ(A) − (1 + log(1/φ)) = 3.5·10⁻³, 1.4·10⁻⁴, 2·10⁻⁶.
- [3] max over t, M of R/(ε_n(1 + log M)): 0.67–0.74 (p = 2), 0.70–0.72 (p = 1); R/R_FM 0.86–0.93 (p = 2), 0.69–0.88 (p = 1)
  for M ≤ n^{2/p}/4; |T|/(ε_ny(1 + log M)) ≤ 0.58 (≤ 0.05 resp. 0.10 for M ≤ n^{2/p}/4).
- [4] DB/|X| ≤ 1.26; C_E ≤ 1.03; C_F ≤ 0.68 (p = 2), 1.26 (p = 1), the same for every n and t tested.
- [5] X_M/y_M at the deepest M equals R_m at the deepest node to all printed digits (Lemma RF); |R_m(0)|/(ε_n log n) =
  0.63–0.74 (p = 2, decreasing in n), 0.93–1.00 (p = 1).
- [6] Y_β(1)/Y_β(0) for β = (¼, ½, ¾)·p/2: ≤ 1.003, ≤ 1.03, ≤ 1.36 (p = 2; 1.0004, 1.009, 1.18 at n = 400), ≤ 1.002, ≤ 1.009, ≤ 1.034 (p = 1), decreasing in n;
  the growth at β near ϑ is the far-tail tilt of remark (2).
- Limits: n ≤ 400 (p = 2), n ≤ 200 (p = 1), one Ψ, s = 2, a continuum tail model beyond k = 6·10⁴; finite checks of
  universally quantified statements (Rule N2).

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
