# Research program after the consolidation (Plan 38, 2026-10-14)

Synthesis of eight parallel reports (four Rule-L novelty searches, four research outlines), all in this folder:
`novelty_G2.md`, `novelty_G1RH.md`, `novelty_G1transport.md`, `novelty_G3p.md`, `outline_A_nodes.md`,
`outline_B_sv.md`, `outline_C_rough.md`, `outline_D_G3p.md`; their scripts and outputs are in `scripts/`.

Status of this document: PLANNING. The reports are agent output, not reviewed. Statements marked "derived here" in the
outlines are new deductions that need Rule A/R before use. Literature items marked "[recollection]" or "seen only in
search results" have not passed the citation gate (AGENTS.md Rule C) and must not be cited until read. "NOT FOUND" means
"not found in one search session" (no MathSciNet; paywalled papers listed as unread), not "proved new". Nothing here
bears on RH.

## 1. Novelty (Rule L, first pass)

| Result | Verdict | Closest prior work (report) |
|---|---|---|
| G2 Theorem H_all, general p | NOT FOUND | Monien 0901.1883 (p = 1, heuristic); Haynes–Zudilin 1510.01901 (expect −an²log n + O(n²); prove ≤ −(a/2)n²log n); Coons–Sutherland 1404.2699 (log H_n < −cn²) |
| G2 explicit constrained equilibrium B* | PARTIALLY KNOWN | framework: Rakhmanov 1996, Dragnev–Saff 1997, Kuijlaars–Van Assche 1999 (abstracts only); general-p solution, c(p), κ_p, optimality NOT FOUND |
| G2 Cor. HZ | a = 1: constant in Monien (heuristic); a = 2, b ∈ {−2, 0, 2}: implicit in Baricz–Štampach 1708.07729 closed forms (agent checked numerically: their constants → κ₂ ≈ 2.51687); all other cases NOT FOUND |
| G1 RH₁, RH₁(r), RH_p, seam, RH_ζ | NOT FOUND (method known) | WLXZ 1410.3948 is the only RH analysis with accumulating nodes (Dai–Yao 2104.03563 say so). (p, s) = (2, 2) is the classical Lommel ν = 3/2 family (exact b_n; free exact check). p = 1, r = 2: Monien–Zagier numerical expansion, unproved |
| G1 FV, FVa, LP, TL | KNOWN / standard (already labelled so) | Basor–Chen–Ehrhardt 0905.2620; Breuer–Duits 1309.6224; Van Assche math/9401209; Simon JAT 2004 |
| G1 TV transport, Theorem L, T3-all, T3-log | NOT FOUND | nearest: Lubinsky Annals 2009 (kernel comparison), Denisov–Rakhmanov (needs a.c. spectrum) |
| G1 Theorem R, dichotomy | NOT FOUND as stated; "expected in spirit" | **must read** Knopfmacher–Lubinsky–Nevai, Constr. Approx. 4 (1988) 9–20 (paywalled, unread) |
| G1 CL, TC/T3-avg | NOT FOUND (methods standard) | BKMM math/0212149 (analytic data only) |
| G3′-U, Theorem B, Ch, N″, N‴, V⁺, numerics | NOT FOUND | moments of σ are Voros's superzeta values Z∗(σ) (1403.4558), linked to Keiper–Li; no Hankel/OP study found |
| G3′ Theorem C, Cor. P, Thm S/S′ | PARTIALLY KNOWN | PCC ⇒ (SG) is in Goldston math/0412313 (6.10)–(6.11); only (SG) ⇒ G3′ is new |

**Framing suggestions from the searches.** Law P as a *Freud-type theorem for compact Jacobi operators* (spectral data ⇒
entry asymptotics via an equilibrium problem, cf. Lubinsky–Mhaskar–Saff), stable under slowly varying weights and not
under rough ones. For G3′: the Hankel determinants of the superzeta values.

**Citations to add (after reading):** Haynes–Zudilin (SIGMA 11 (2015) 101), Monien, Baricz–Štampach, Dai–Yao, Van Assche
(Lommel/Stieltjes survey math/9510214), Voros superzeta, Goldston (6.10)–(6.11), Hejhal's spacing hypothesis (via
Hiary–Odlyzko 1105.4312), Fauzan 2026 / Lai 2610.06838 (ζ(5), Hankel; different functional — cite and distinguish).

**Unread items that gate novelty claims:** Knopfmacher–Lubinsky–Nevai 1988 (Theorem R) — first priority;
Lubinsky–Mhaskar–Saff 1988; Máté–Nevai–Totik II/III; Rakhmanov 1996; Dragnev–Saff 1997; Kuijlaars–Van Assche PLMS 1999;
Ou–Wong 2010; BKMM monograph.

## 2. A structural observation checked here (local-exponent law)

Outline A observes that for nodes f(k) = k^{−p}ℓ(k) with ℓ smoothly slowly varying, b_n/f(n) ≈ c(p_f(n)) with the local
exponent p_f(n) := −nf′(n)/f(n). For the smooth-ζ model p_f(n) = 2 − 2/log n + …, which predicts
b_n/x_n = c(2)(1 + κ/log n + …) with κ = −2(log c)′(2). Checked (mpmath, 30 digits):
−2(log c)′(2) = −0.289459771698800348… = −2(log(π/2) − (1 − log 2)), RH_ζ's κ exactly. Outline B finds the analogous
weight-side effect: for Ψ with D(γ) = ∞ the deviation is ≈ ε_n/(2n), ε_n = (log Ψ)′ in log k, i.e. the pure-power 1/n
coefficient at the local weight exponent. Status: NUMERICAL + heuristic; the κ identity is an exact numerical
coincidence check, not a proof that the mechanism is right in general.

## 3. Research projects

Probabilities and plan counts are the outline agents' estimates (one "plan" ≈ one repo Plan of the size of Plans 33–36).

### C. Rough weights — most tractable, strongest near-term payoff (`outline_C_rough.md`)
- New heuristic (NUMERICAL): phase model q_n(k) ≈ R_k sin(nθ_k + φ_k), predicting universal constants
  ‖Δμ_N‖₁ → 8/π², ‖Δ²μ_N‖₁ → 4/π (observed 0.78–0.86 vs 0.811; 1.275–1.286 vs 1.273). Worst-case Σ_{n∈[N,2N]}L_n² is
  O(1) (≈ 1.9–2.1): at most O(1) bad n per dyadic block.
- Targets: **RW** (Conjecture R window form; 1 plan, ~90%); **LR** linear response |log b_n²(w) − log b_n²(v) − L_n^v(f)|
  ≤ 2ε² (≈ one paragraph); **Ra** pointwise a-law also fails (1 plan, ~85%); **D1** density-one law up to 2ε² for
  |f| ≤ ε (2 plans, ~70%); **Theorem D** density-one law for *every* bounded rough f (3–4 plans, ~50%) — would make the
  dichotomy "pointwise can fail, density-one always holds"; explicit η (C4).
- Hardest step: propagating "local freeness" along t ↦ ve^{tf} in Theorem D.

### B. Slowly varying weights beyond log-type (`outline_B_sv.md`)
- Target: law for every slowly varying Ψ (no boundedness, no D(γ)). Reductions (head, far tail, smoothing) routine.
- Exact gap: one lemma **QL** (single-n hard-edge log-moment localization, o(1/ε_n), uniformly on the path). Theorem
  B-cond (QL ⇒ law) provable now (1 plan, ~95%). The suggested elementary ideas provably stop at log-type.
- Full route: RH analysis with an N-dependent Bessel order (3–4 plans p > 1, ~45%; all p ~30–35% in ~8 plans).
- Numerics: deviation ≈ ε_n/(2n) for exp(√log k), exp((log k)^0.8), oscillating L.

### A. Nodes other than pure powers (`outline_A_nodes.md`)
- Local-exponent law (§2). Node first variation is exact: d/dt log b_n² = Σ_k w_kẋ_k ∂_x(p_n² − p_{n−1}²)(x_k).
- Targets: **T0′** Law P ⟺ rescaled μ_n → arcsine (½ plan, ~90%; check Simon 2004 first); **T0** Cesàro law for (H-a)
  nodes (1 plan, ~80%); **T1′/T1** RH for analytic regularly varying nodes, RH_ζ as a corollary (1–2 plans ~75%, then
  2–5 more ~50%); **T2** rough node displacements break the law (1–2 plans, ~55%); **T3** C¹ nodes by node transport
  (4–8 plans after T1, ~20%; missing Lemma NK, no closing Grönwall found).
- True ζ ordinates: a barrier, not a target (pointwise law ⇒ G3′ ⇒ 100% distinct ordinates).

### D. G3′ for ζ (`outline_D_G3p.md`)
- Unconditional G3′ is out of reach (<1%): G3′ ⇒ d(E) = 0 ⟺ (derived here) 100% of zeros simple and on the line
  (GLSS's HMH); open even on RH. Exact split (derived here): G3′ ⟺ HMH + capped energy over distinct ordinates o(K²).
  *(Correction, Plan 43, 2026-10-14; see research/G3prime/PROOF.md §5.6 and review/REVIEW_Plan43.md: only HMH ⇒ d(E) = 0 holds. d(E) = 0 ⟺ "100% of zeros simple and on the critical line" (Prop I) is NOT HMH. The split is G3′ ⟺ d(E) = 0 ∧ 𝒞_dist(K) = o(K²) (Thm Sp). G3′ ⇒ HMH is NOT established.)*
- Realistic targets: **D1** HMH positioning (≤ 1 week, ~95%); **D2** quantitative two-sided Ch (~70%); **D3** law
  provably fails for Dedekind zeta of non-abelian Galois fields (repeated ordinates from L(ρ₂)²; ~80%); **D4** law holds
  a.s. for the sine process (~75%); **D5** function-field zeta: law ⟺ distinct Frobenius angles (~70%); **D6** explicit
  constant in Theorem B (20–35%).
- Deprioritized: (Q1), (NA), G3′* unconditionally, weighted Lemma G.

## 4. Shareable now (after the pre-sharing checklist)

1. **Paper 1 — averaged Law P (G2) + Hankel determinants of zeta values.** Strongest novelty case, one citation (P) *(Plan 47, 2026-10-14: now none; G2 Lemma EP = Paper 1 Lemma 3.3)*,
   shortest proof. Add the Baricz–Štampach cross-check.
2. **Paper 2 — Law P for compact Jacobi operators: pure powers (RH) + weight transport + dichotomy** (G1). Needs an expert
   read of the RH analyses (suggested readers: Zhao/Lin/Xu, Dai, Kuijlaars, Van Assche, Bleher–Liechty) and the
   Knopfmacher–Lubinsky–Nevai check. Project C's RW/LR/Ra would strengthen it cheaply.
3. **Note 3 — Hankel determinants of the zeta-zero measure (superzeta values): Theorem Ch, Theorem B, N″/N‴,
   numerics,** plus project D's D1–D5 as decided examples.

**Pre-sharing checklist:** read the gating unread papers (§1); add the citations; human expert read; write standalone
papers (the PROOF.md files are working documents).

## 5. Recommended sequencing

1. Quick wins (≈ 3–4 plans): C-RW, C-LR, C-Ra; A-T0′; D1; B-cond. Each is ≥ 85% and directly strengthens Papers 2–3.
2. In parallel: the reading list in §1 and drafting Paper 1.
3. Then choose one major line: **C-Theorem D** (~50%, clean dichotomy) or **A-T1** (regularly varying nodes by RH,
   ~50%, explains RH_ζ structurally) or **D3–D5** (decided examples for the zeta-zero note, 70–80% each).
