# SECOND: the 1/n coefficient in the pointwise Law P for pure powers (Plan 62)

Status (2026-10-15): written by the Plan 62 agent; **REVIEWED 2026-10-15** (Rule R: research/G1/review/REVIEW_Plan62.md, ACCEPT WITH FIXES; fixes F1–F11, O1 applied in 5aa04e3 and diff-checked). Labels per VERIFICATION_POLICY.md; REVIEWED applies to the PROVED / PROVED-mod-cite / CONDITIONAL statements as labelled (NUMERICAL, CONJECTURE, HEURISTIC and GAP items keep those labels).
*Plan 64 update (2026-10-15, REVIEWED, REVIEW_Plan64.md):* Thm 3.8, Cor 3.9, Thm 3.10(d) and (UΛ) are upgraded by `UL.md` (same
directory); the rows and paragraphs marked "Plan 64" carry UL.md's labels (REVIEWED, REVIEW_Plan64.md).
*Plan 65 update (2026-10-15, **REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)**):* `E_pgt1.md` (same directory) proves (E) and all constants of Conj. P62 for
p > 1 by second-order RH analysis; the rows and paragraphs marked "Plan 65" carry its labels.
*Plan 66 update (2026-10-15, REVIEWED; Rule R REVIEW_Plan66_A.md, REVIEW_Plan66_B.md, fixes applied):* `E_p1.md` (same directory) proves (E) at p = 1 for every
s > 1 (remainder O(n⁻²)) and the −1/24 constant at s = 3/2 (and s = 5/2 vs x·TC); rows and paragraphs marked "Plan 66" carry its labels.
*Plan 67 update (2026-10-15, not REVIEWED; Rule R REVIEW_Plan67_A.md, REVIEW_Plan67_B.md, fixes applied):* `E_plt1.md` (same directory) proves (E) for
0 < p < 1 at every s > 1, with the sharp remainder: n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), κ_p = 2pc(p)ζ(−p), and all constants of Conj. P62; rows and paragraphs marked "Plan 67" carry its labels.
*Plan 69 (2026-10-15, REVIEWED, REVIEW_Plan69.md):* `TAIL.md` (same directory) proves the hard-edge tail bound used by UL.md in Paper 2's frame and reduces Thm 3.8 to the window by telescoping.
"RH" below means Riemann–Hilbert. Open item 13 of THEOREMS.md §4.

**Summary of labels.**

| # | Statement | Label |
|---|---|---|
| §1 | d₁(p, s) = −(s − 1)/2, e₁ = p/2 (repo pairing) = −p/2 (standard pairing), k₀ = −(s − 1) − p/2, k₁ = −(p + 2)a, on the grid p ∈ {½, 1, 3/2, 2, 3, 4}, s ∈ {3/2, 2, 3, 4} | NUMERICAL |
| Conj. P62 | the same closed forms for every p > 0, s > 1, with remainder O(n^{−1−min(1,p)}) | **PROVED-mod-cite for 0 < p < 1** (remainder O(n^{−1−p}), as conjectured, with the n^{−1−p} coefficient identified: κ_p = 2pc(p)ζ(−p) for b_n, α_n, g_{n−1}, h_n, 0 for α_n/(2b_n), 2^{1+p}κ_p for γ_N²; E_plt1 Thm E′.1, Cor E′.6) (Plan 67, E_plt1.md; not REVIEWED); **at p = 1 PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀** (E_p1 Thm E1.10, remainder O(n⁻²)) and for k₁ at s ∈ {3/2, 5/2} (E_p1 Thm E1.6); k₁ at other s GAP (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); **PROVED-mod-cite for p > 1** (remainder O(n⁻²); E_pgt1 Thm E.1, Cor E.6) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)) |
| Thm 2.3 | p = 2, s ∈ {2, 4, 6, 8, 10}: exact rational Jacobi coefficients; d₁ = −(s − 1)/2, e₁ = 1, e₁ˢ = −1, k₀ = −s, k₁ = −2(s − 2), d₂ = (s² + 6s − 11)/16 | PROVED-mod-cite (VA §3, DLMF-Lommel, via Paper 2 Remark rem:pure-lommel) + exact computer algebra |
| Prop 3.1 | Christoffel product identity Π_{m≤n}(b_m(s+p)/b_m(s))² = g_n/g_0 | PROVED (elementary; any σ on [0, ∞)) |
| Thm 3.2 | Σ_{m≤n} log(b_m(s+p)/b_m(s)) + (p/2)log n → ½log(c(p)ζ(s)/ζ(s+p)) | PROVED-mod-cite (pointwise Law P: Paper 2 Cor. thm:pure / RH_p, RH₁(r), RH_plt1b; G1 Lemma CS) |
| Cor 3.3 | (E) at s and s + p ⇒ d₁(s + p) = d₁(s) − p/2, and n(G_n − G_{n−1}) → 0 (the NUMERICAL hypothesis of G1 Remark SH-1/n) | CONDITIONAL on (E) at s, s + p + PROVED-mod-cite (Law P: Paper 2 Cor. thm:pure / RH_p, RH₁(r), RH_plt1b; G1 Lemma CS); **unconditional for p > 1** (E_pgt1 Thm E.1 gives (E₁)) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); **unconditional for p = 1** (E_p1 Thm E1.10) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); **unconditional for 0 < p < 1** (E_plt1 Thm E′.1 gives (E_p)) (Plan 67, E_plt1.md; not REVIEWED) |
| Thm 3.4 | (E_ε), ε > ½, at s and s + p ⇒ α_n/(2b_n) = 1 − p/(2n) + o(1/n) (e₁ˢ = −p/2; e₁ = +p/2 in the repo pairing) | CONDITIONAL on (E_ε), ε > ½, at s, s + p + PROVED-mod-cite (Law P: Paper 2 Cor. thm:pure / RH_p, RH₁(r), RH_plt1b; G1 Lemma CS); for p > 1 unconditional and **superseded** by E_pgt1 Thm E.1 (α_n/(2b_n) = 1 − p/(2n) + O(n⁻²)) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); for p = 1 unconditional and **superseded** by E_p1 Thm E1.10 (α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²)) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); for 0 < p < 1 its conclusion holds and is **superseded** by E_plt1 Thm E′.1 (α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−min(2p,1)})) (Plan 67, E_plt1.md; not REVIEWED) |
| Prop 3.5 | weights with \|log(w_k/v_k)\| ≤ C/k: log h_n(w) − log h_n(v) = O(1/n), so Σ_{j≤n} log(b_j(w)/b_j(v)) converges | PROVED (internal: G1 Lemma Sat_p⁺) |
| Cor 3.6 | p = 1, s = 3/2 vs Tricomi–Carlitz: Σ_{j≤n} log(b_j/b_j^{TC}) → −½log(ζ(3/2)/(√(2π)W_TC)); (E) at (1, 3/2) ⇒ d₁ = −1/4; with Cor 3.3, d₁(1, 3/2 + m) = −(1 + 2m)/4 | (i) PROVED-mod-cite (RH_p1 §1; DLMF 5.11); (ii)–(iii) CONDITIONAL on (E) + PROVED-mod-cite (as (i); Law P, Lemma CS); (ii)–(iii) **unconditional** (E_p1 Thm E1.10, or elementary E_p1 Thm E1.6 at s = 3/2, 5/2), and Remark (b) (the −1/24 constant) PROVED-mod-cite (E_p1 Thm E1.6) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) |
| Prop 3.7 | ∂_s log h_n(s) = −Σ_k log k·μ_n^{(s)}(k) | PROVED (elementary) |
| Thm 3.8 | Σ_{j≤n} log(b_j(s₁)/b_j(s₀)) = −((s₁ − s₀)/2)log n + ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) + o(1), every p > 0, s₀, s₁ > 1 | PROVED-mod-cite (UL.md Cor UL-3.8: (P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; Lemma CS) (Plan 64, UL.md; REVIEWED). Earlier route: CONDITIONAL on (UΛ) or (CVX) |
| Cor 3.9 | (E) at s₀, s₁ ⇒ d₁(s₁) − d₁(s₀) = −(s₁ − s₀)/2. Hence d₁(2, s) = −(s − 1)/2 and d₁(1, s) = −(s − 1)/2 for all s > 1, under (E) at s | CONDITIONAL on (E) only + PROVED-mod-cite (UL.md Cor UL-3.9; as Thm 3.8) (Plan 64, UL.md; REVIEWED); **unconditional for p > 1** (E_pgt1 Thm E.1 gives d₁ = −(s−1)/2 directly) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); **unconditional for p = 1** (E_p1 Thm E1.10), g(1) = 0 (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); **unconditional for 0 < p < 1** (E_plt1 Thm E′.1), g(p) = 0 (Plan 67, E_plt1.md; not REVIEWED) |
| Thm 3.10 | log-average form: Σ_{j≤n}log(j^pb_j/c) = −((s−1)/2)log n + O(1) for p = 2, s ∈ 2 + 2ℕ₀ and p = 1, s ∈ 3/2 + ℕ₀; equivalently log h_n of the zeta-value Hankel ratios to O(1) | (a)–(c) PROVED-mod-cite (Law P; Lemma CS; Lommel input; RH_p1 §1, DLMF 5.11); (d) every s > 1 for p ∈ {1, 2} (log-average coefficient −(s − 1)/2, convergent remainder) and (c) for all real shifts: PROVED-mod-cite (UL.md Cor UL-3.10: UF-lim; SECOND §2 Input (VA, DLMF-Lommel); Cor 3.6(i) (RH_p1 §1, DLMF 5.11)) (Plan 64, UL.md; REVIEWED); every p > 1, s > 1: log-average coefficient −(s − 1)/2 with O(1), PROVED-mod-cite (sum of E_pgt1 Thm E.1) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); every 0 < p < 1, s > 1: the same, PROVED-mod-cite (sum of E_plt1 Thm E′.1; Σj^{−1−p} < ∞) (Plan 67, E_plt1.md; not REVIEWED) |
| (CVX) | s ↦ log h_n(σ_{p,s}) convex (no longer needed for Thms 3.8–3.10; sufficient for sup_K\|Λ_n\| = O(1), UL.md Prop R; fails for finite truncations, UL.md Remark CVX-fin) | HYPOTHESIS; NUMERICAL support (n ≤ 8, 300-digit determinants; n ≤ 1600 grid: positive second divided differences at the grid points) |
| (UΛ) | sup_{s∈K}\|Λ_n(s)\| = o(log n), K ⊂ (1, ∞) compact | PROVED-mod-cite (UL.md Thm UΛ: Thm UP, Lemma LP's method, Lemma TL) (Plan 64, UL.md; REVIEWED); sup_K\|Λ_n\| = O(1): **GAP** (⇐ (RU) at PROOF SKETCH level, ⇐ (SCVX), ⇐ (CVX)) |
| UF-lim | h_n(s)/h_n(s₀) = c^{(s−s₀)/p}n^{−(s−s₀)}(1 + o(1)) uniformly on compacts | PROVED-mod-cite (UL.md Thm UF-lim: (P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; Lemma CS) (Plan 64, UL.md; REVIEWED) |
| UP | Law P uniform on compacts in s: sup_K\|n^pb_n − c\|, \|n^pg_n − c\|, \|n^pα_n − 2c\| → 0 | PROVED-mod-cite (UL.md Thm UP: Thm UF-lim, hence (P), (LP), (QLP-c) at fixed points; Lemma CT) (Plan 64, UL.md; REVIEWED) |
| Thm E.1, Cor E.6 | p > 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + O(n⁻²)), n^pα_n = 2c(1 − (s−1+p)/(2n) + O(n⁻²)), α_n/(2b_n) = 1 − p/(2n) + O(n⁻²); n^pg_{n−1} = c(1 + a/n + O(n⁻²)), k₀ = −(s−1) − p/2, k₁ = −(p+2)a | PROVED-mod-cite (RH_px; Paper 2 Lemmas binetcut, szego, airy, Frame Prop.; KMVV §6; DLMF 9.7.2, 9.7.5–6, 10.17, 10.25.2, 10.40.1–4) + exact computer algebra (E_pgt1.md) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)) |
| Thm E1.6, E1.10 | p = 1, every s > 1: nb_n = ½(1 − (s−1)/(2n) + O(n⁻²)), nα_n = 1 − s/(2n) + O(n⁻²), α_n/(2b_n) = 1 − 1/(2n) + O(n⁻²), Nβ_N = 1 + (½ − s + κ₁(−1)^N)/N + O(N⁻²); s = 3/2, 5/2: b_n, α_n, g_n, h̃_n = TC resp. x·TC values × (1 − 1/(24n²) + O(n⁻³)) | E1.10: PROVED-mod-cite (RH₁(r); WLXZ v1 (6.8), (6.10)–(6.21), (6.34)–(6.37); KV (5.23), (5.26)–(5.30); Vanlessen (4.26)–(4.33), (4.43)–(4.52); DLMF 5.11, 9.7.5–6, 10.17.5–6, 10.40.1–2; UL Cor UL-3.10); E1.6: PROVED-mod-cite (WLXZ v1 (1.4)–(1.9); DLMF 5.5.1, 5.11) + exact computer algebra (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) |
| Thm E′.1, Cor E′.6, Lemma F.1 | 0 < p < 1, s > 1: n^pb_n = c(1 − (s−1)/(2n) + κ_pn^{−1−p} + O(n^{−1−2p} + n^{−2})), n^pα_n = 2c(1 − (s−1+p)/(2n) + κ_pn^{−1−p} + O(·)), κ_p = 2pc(p)ζ(−p) < 0; α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−2p} + n^{−2}); n^pg_{n−1} = c(1 + a/n + κ_pn^{−1−p} + O(·)); γ_N² = c(N/2)^{−p}(1 + (k₀ + k₁(−1)^N)/N + 2^{1+p}κ_pN^{−1−p} + …), k₀ = −(s−1) − p/2, k₁ = −(p+2)a; seam band factor log H_n(z) − log H_n(1) ~ −2Σ_kζ(−kp)(z^k − 1)/(kn^{kp}) | PROVED-mod-cite (RH_plt1b; RH_px §5; Paper 2 Lemmas seam, corner, szego, airy, invariance, Frame Prop.; E_pgt1 Lemmas E.3–E.5; KMVV §6 incl. angle freedom; DLMF 5.2.1, 25.2.1, 25.4.1, 9.7.2, 9.7.5–6, 10.17, 10.25.2, 10.40.1–4) + exact computer algebra (Plan 67, E_plt1.md; not REVIEWED) |
| §4.1 | n_eff = n + α_x/2 + (j₀ − ½) (hard edge + lattice offset) | HEURISTIC; NUMERICAL (shifted lattices); at p = 1 the chain value d₁(TC(α)) = ¾ − α is exact for all α (the TC(α) masses are not checked) |
| §4 (E) | existence of the 1/n coefficient (with a remainder O(n^{−1−ε})) for pure powers | **PROVED-mod-cite for p > 1** with ε = 1 (E_pgt1 Thm E.1) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); **PROVED-mod-cite for p = 1** with ε = 1 (E_p1 Thm E1.10: symmetric frame of RH₁(r), second-order matching; value from UL Cor UL-3.10) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md); **PROVED-mod-cite for 0 < p < 1** with ε = p, sharp (E_plt1 Thm E′.1: seam band factor flat only to O(n^{−p}), log H_n(z) − log H_n(1) = −2ζ(−p)(z−1)n^{−p} + O(n^{−2p}) (Lemma F.1), entering at order n^{−1−p} through the Bessel/Airy corrections) (Plan 67, E_plt1.md; not REVIEWED). Hence (E) holds for **every p > 0** |
| §4 g(p) | the s-independent part g(p) := d₁(p, s) + (s − 1)/2 for p ∉ {1, 2} | g(p) = 0 for every p > 1: PROVED-mod-cite (E_pgt1 §8.2) (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)); **g(p) = 0 for every 0 < p < 1: PROVED-mod-cite** (E_plt1 Thm E′.1) (Plan 67, E_plt1.md; not REVIEWED) (earlier NUMERICAL: \|g\| ≤ 1.4·10⁻⁶ at p = ½); p = 1: g(1) = 0 PROVED-mod-cite (E_p1 Thm E1.10) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md) |

Novelty: UNCHECKED throughout. Prop 3.1 is the classical Christoffel / chain-sequence telescoping (novelty not
claimed; Lemma CS is KNOWN, Dai–Piao–Qiao Prop. 2.1). Rule L pointer for Theorem 3.10's Hankel form: compare with the
Monien/Zagier expansion and Haynes–Zudilin (Paper 2 Remark rem:pure-zeta).

Nothing here is REVIEWED. No external source was newly read for Plan 62: every citation is to an entry already in
`RH/CITATIONS.md` (see the Plan 62 entry there).

## 0. Setting and conventions

- σ = σ_{p,s} := Σ_{k≥1} k^{−s}δ_{x_k}, x_k := k^{−p}, p > 0, s > 1. Its total mass is ζ(s), and x·σ_{p,s} = σ_{p,s+p}.
- Monic OPs: xπ_n = π_{n+1} + α_nπ_n + b_n²π_{n−1} (n ≥ 0, b_0 := 0). So α_n (n ≥ 0) is the diagonal and b_n (n ≥ 1)
  the off-diagonal of the Jacobi matrix; h_n := ∫π_n²dσ = ζ(s)·b_1²⋯b_n².
- **Two pairings.** Item 11 / repo indexing writes a_n := α_{n−1}. The repo's "a_n/(2b_n) = 1 + e₁/n" is the pairing
  **α_{n−1}/(2b_n)**, with e₁ = +p/2. Paper 2 and the standard convention pair **α_n/(2b_n)**; its coefficient is
  written e₁ˢ here, and e₁ˢ = −p/2. In general e₁ = e₁ˢ + p whenever α_n has a 1/n expansion (α_{n−1}/α_n =
  1 + p/n + O(n⁻²)). Every statement below names the pairing.
- c = c(p) := ¼(π/(2I_p))^p, I_p := (√π/2)Γ(1/p + ½)/Γ(1/p + 1) (toolkit `laws.weyl.c_p`); c(1) = ½, c(2) = π²/16.
- **Chain** (G1 PROOF.md §3.21, Lemma CT, PROVED): g_n := −π_{n+1}(0)/π_n(0) > 0, h_0 := 0, h_n := b_n²/g_{n−1}; then
  α_n = g_n + h_n and b_n² = g_{n−1}h_n. In the symmetric variable of RH.md §1, g_n = γ_{2n+1}² and h_n = γ_{2n}².
  Lemma CS (ibid., PROVED): if Law P holds then G_n := n^pg_n → c and n^ph_n → c.
- **Targets.** d₁, e₁, e₁ˢ in n^pb_n/c = 1 + d₁/n + …, α_{n−1}/(2b_n) = 1 + e₁/n + …, α_n/(2b_n) = 1 + e₁ˢ/n + …,
  and k₀, k₁ in γ_N²/(c(N/2)^{−p}) = 1 + (k₀ + k₁(−1)^N)/N + … (RH.md §8.3).
- **Hypothesis (E_ε)(p, s)** (existence): there is d₁ ∈ ℝ with n^pb_n/c = 1 + d₁/n + O(n^{−1−ε}). (E) means (E_ε) for
  some ε > 0. Under (E), d₁ is unique. RH_p (RH_px.md), RH₁(r) and RH_plt1b prove only n^pb_n/c = 1 + O(1/n).
- a := (2s − 2 − p)/(2p) is the symmetric Fisher–Hartwig exponent (RH.md §5) and α_x := (s − 1 − p)/p = a − ½ the
  x-variable hard-edge (Bessel) order (RH_px Lemma 1.2).

## 1. Numerics (Goal 1) — NUMERICAL

**Method** (`checks/so_coeffs.py`). Atoms k ≤ K exactly, plus a Gauss–Jacobi rule with nmax + 8 nodes for the continuum
tail T_K(f) := ∫_{K+½}^∞ t^{−s}f(t^{−p})dt = (1/p)∫_0^X x^β f(x)dx, X := (K + ½)^{−p}, β := (s − 1)/p − 1 > −1. The rule is
exact on polynomials of degree ≤ 2nmax + 15, so the first nmax coefficients are exactly those of (atoms + T_K). The
remaining error is the midpoint Euler–Maclaurin defect of the tail, measured by K → 2K. Coefficients by the binary128
RKPW kernel (`csrc/rkpw.c`); atoms are stored in float64, a relative perturbation of 10⁻¹⁶ of the measure.

**Validation** (`checks/check_so_validate.py`, .out). Against the exact Lommel coefficients at (p, s) = (2, 2) (§2):
max relative error of b_n and α_n over n ≤ 400 is 6.6·10⁻¹⁵ at K = 4·10⁴ (2.2·10⁻¹³ at K = 2·10⁴).

**Fits** (`checks/so_fit.py`). Least squares in the exponents {1 + i + jp : i, j ≥ 0} (the first J of them), J = 4…7,
windows [f·nmax, nmax], f ∈ {0.1, 0.2, 0.3}, nmax = 1600; the chain fit adds (−1)^N terms with the same exponents. The
reported value is the median of the 12 estimates; "fit" is half their range; "dK" is |value(K) − value(2K)|. Both
are error **estimates** (Rule N), not bounds. K = 100·nmax for p ≥ 1, 200·nmax for p = ½.

**Non-integer exponents.** For p < 1 the remainder is not O(n⁻²): at p = ½, s = 2, n(n^{1/2}b_n/c − 1) + ½ =
−8.6·10⁻³, −6.9·10⁻³, −5.2·10⁻³, −3.9·10⁻³, −2.8·10⁻³, −2.0·10⁻³ at n = 50, 100, …, 1600 (ratio ≈ 0.72 per
doubling, i.e. a term ≍ n^{−1−p} in n^pb_n/c, up to slower drifts). This is why the fit basis contains n^{−1−jp}. A
heuristic source: the part of the node set above the band (k ≲ n) acts on the band, at scale n^{−p}, through a far field
whose first correction is of relative size n^{−1}·(n^{−p}/1) (HEURISTIC). For p ≥ 1 these terms are O(n⁻²).
*Plan 67 (Plan 67, E_plt1.md; not REVIEWED):* the n^{−1−p} term is identified: its coefficient in n^pb_n/c (and in n^pα_n/(2c), n^pg_{n−1}/c) is
κ_p = 2pc(p)ζ(−p) (κ_{1/2} = ζ(−½)/√6 = −0.0848692…), s-independent, absent in α_n/(2b_n); it comes from the seam band
factor H_n ∝ exp(−2ζ(−p)n^{−p}z + O(n^{−2p})) (E_plt1 Lemma F.1, Thm E′.1).

**Table** (`checks/check_so_grid.out`): §1.1.

### 1.1 Results

| p | s | d₁ (conj −(s−1)/2) | e₁ repo α_{n−1}/(2b_n) (conj p/2) | e₁ˢ std α_n/(2b_n) (conj −p/2) | k₀ (conj −(s−1)−p/2) | k₁ (conj −(p+2)a) |
|---|---|---|---|---|---|---|
| 0.5 | 1.5 | -0.249999998 (3.8e-07) [3e-09] (-0.250) | +0.249999991 (6.5e-08) [1e-08] | -0.250000021 (2.7e-07) [2e-08] | -0.750000002 (2.0e-06) [5e-08] (-0.750) | -1.249998846 (3.9e-06) [3e-07] (-1.250) |
| 0.5 | 2.0 | -0.500000014 (5.7e-07) [4e-09] (-0.500) | +0.250000027 (1.5e-06) [2e-08] | -0.249999950 (6.3e-06) [4e-08] | -1.249999907 (2.3e-05) [3e-08] (-1.250) | -3.749999315 (3.5e-05) [4e-07] (-3.750) |
| 0.5 | 3.0 | -1.000000247 (2.9e-05) [7e-09] (-1.000) | +0.250000403 (5.6e-05) [4e-09] | -0.249999294 (9.3e-05) [2e-08] | -2.249998765 (2.0e-04) [9e-09] (-2.250) | -8.749998621 (2.5e-04) [3e-07] (-8.750) |
| 0.5 | 4.0 | -1.500001361 (1.3e-04) [1e-07] (-1.500) | +0.250002580 (2.5e-04) [2e-07] | -0.249996155 (3.4e-04) [1e-07] | -3.249993811 (6.6e-04) [2e-07] (-3.250) | -13.749991980 (8.1e-04) [1e-06] (-13.750) |
| 1.0 | 1.5 | -0.250000000 (1.3e-10) [5e-11] (-0.250) | +0.500000000 (2.9e-10) [8e-11] | -0.500000000 (3.7e-10) [5e-11] | -1.000000000 (3.6e-10) [6e-11] (-1.000) | +0.000000026 (4.4e-08) [9e-09] (-0.000) |
| 1.0 | 2.0 | -0.500000000 (5.6e-10) [1e-10] (-0.500) | +0.500000000 (1.1e-09) [2e-10] | -0.500000000 (1.1e-09) [2e-10] | -1.500000000 (1.2e-09) [2e-10] (-1.500) | -1.500000000 (4.5e-09) [2e-09] (-1.500) |
| 1.0 | 3.0 | -1.000000000 (5.6e-10) [1e-10] (-1.000) | +0.500000000 (1.1e-09) [2e-10] | -0.500000000 (1.1e-09) [4e-10] | -2.500000000 (2.6e-09) [5e-10] (-2.500) | -4.500000000 (4.7e-09) [2e-09] (-4.500) |
| 1.0 | 4.0 | -1.500000000 (2.1e-09) [6e-11] (-1.500) | +0.500000000 (3.0e-09) [1e-10] | -0.500000000 (8.5e-09) [2e-10] | -3.500000000 (2.1e-08) [2e-10] (-3.500) | -7.499999999 (1.9e-08) [6e-09] (-7.500) |
| 1.5 | 1.5 | -0.250000000 (3.4e-09) [3e-10] (-0.250) | +0.750000000 (5.0e-09) [4e-10] | -0.750000000 (1.9e-08) [6e-10] | -1.250000000 (1.1e-08) [8e-11] (-1.250) | +0.583333361 (3.0e-07) [1e-08] (+0.583) |
| 1.5 | 2.0 | -0.500000000 (4.8e-09) [7e-10] (-0.500) | +0.750000000 (2.3e-09) [5e-10] | -0.750000000 (6.9e-09) [3e-10] | -1.750000000 (2.0e-08) [5e-10] (-1.750) | -0.583333316 (3.4e-08) [2e-08] (-0.583) |
| 1.5 | 3.0 | -1.000000000 (1.6e-08) [4e-10] (-1.000) | +0.750000000 (3.2e-09) [1e-10] | -0.750000000 (1.4e-08) [1e-09] | -2.750000000 (1.7e-07) [1e-09] (-2.750) | -2.916666661 (2.2e-07) [1e-08] (-2.917) |
| 1.5 | 4.0 | -1.500000000 (1.4e-08) [4e-12] (-1.500) | +0.750000000 (5.9e-09) [3e-11] | -0.750000000 (1.6e-07) [1e-10] | -3.750000000 (8.3e-07) [3e-10] (-3.750) | -5.250000011 (9.1e-07) [6e-08] (-5.250) |
| 2.0 | 1.5 | -0.250000000 (6.0e-10) [5e-11] (-0.250) | +1.000000000 (1.6e-09) [9e-11] | -1.000000000 (1.6e-09) [1e-10] | -1.500000000 (4.7e-09) [3e-11] (-1.500) | +1.000000053 (2.5e-06) [6e-09] (+1.000) |
| 2.0 | 2.0 | -0.500000000 (3.4e-11) [3e-12] (-0.500) | +1.000000000 (4.3e-11) [8e-12] | -1.000000000 (1.1e-10) [2e-11] | -2.000000000 (7.9e-11) [7e-12] (-2.000) | +0.000000002 (1.4e-08) [2e-09] (-0.000) |
| 2.0 | 3.0 | -1.000000000 (3.2e-11) [3e-13] (-1.000) | +1.000000000 (2.2e-12) [6e-13] | -1.000000000 (1.2e-11) [5e-13] | -3.000000000 (3.4e-10) [7e-12] (-3.000) | -2.000000000 (5.5e-09) [9e-10] (-2.000) |
| 2.0 | 4.0 | -1.500000000 (8.6e-11) [1e-11] (-1.500) | +1.000000000 (1.9e-11) [7e-12] | -1.000000000 (2.6e-10) [8e-12] | -4.000000000 (2.6e-09) [1e-11] (-4.000) | -4.000000000 (5.2e-09) [2e-11] (-4.000) |
| 3.0 | 1.5 | -0.250000000 (2.9e-12) [3e-12] (-0.250) | +1.500000000 (2.9e-10) [2e-12] | -1.500000000 (4.5e-10) [3e-12] | -2.000000000 (4.3e-11) [6e-11] (-2.000) | +1.666666664 (1.1e-08) [2e-08] (+1.667) |
| 3.0 | 2.0 | -0.500000000 (3.9e-12) [9e-13] (-0.500) | +1.500000000 (1.1e-10) [3e-12] | -1.500000000 (3.2e-10) [1e-12] | -2.500000000 (5.4e-11) [7e-12] (-2.500) | +0.833333334 (1.1e-09) [3e-09] (+0.833) |
| 3.0 | 3.0 | -1.000000000 (2.2e-11) [2e-14] (-1.000) | +1.500000000 (6.5e-12) [8e-14] | -1.500000000 (1.0e-10) [1e-13] | -3.500000000 (1.7e-10) [8e-14] (-3.500) | -0.833333333 (1.2e-10) [8e-12] (-0.833) |
| 3.0 | 4.0 | -1.500000000 (8.1e-11) [2e-14] (-1.500) | +1.500000000 (1.5e-12) [6e-15] | -1.500000000 (1.7e-11) [7e-15] | -4.500000000 (1.0e-09) [5e-14] (-4.500) | -2.500000000 (1.1e-09) [5e-11] (-2.500) |
| 4.0 | 1.5 | -0.250000000 (1.8e-12) [1e-12] (-0.250) | +2.000000000 (8.7e-10) [2e-12] | -2.000000000 (1.1e-09) [5e-12] | -2.500000000 (9.0e-11) [2e-11] (-2.500) | +2.250000000 (1.2e-09) [5e-09] (+2.250) |
| 4.0 | 2.0 | -0.500000000 (1.5e-12) [2e-14] (-0.500) | +2.000000000 (4.7e-10) [7e-14] | -2.000000000 (8.8e-10) [8e-14] | -3.000000000 (9.8e-11) [4e-13] (-3.000) | +1.500000000 (1.1e-10) [9e-11] (+1.500) |
| 4.0 | 3.0 | -1.000000000 (1.3e-11) [2e-15] (-1.000) | +2.000000000 (9.1e-11) [7e-16] | -2.000000000 (4.6e-10) [0e+00] | -4.000000000 (1.6e-10) [1e-14] (-4.000) | +0.000000000 (1.9e-12) [8e-12] (-0.000) |
| 4.0 | 4.0 | -1.500000000 (5.7e-11) [2e-15] (-1.500) | +2.000000000 (1.9e-12) [3e-15] | -2.000000000 (1.7e-10) [3e-15] | -5.000000000 (6.5e-10) [2e-14] (-5.000) | -1.500000000 (5.9e-10) [1e-11] (-1.500) |

Format: value (fit half-range) [|K − 2K|]; conjectured value in parentheses where it varies.

**Reading of the table.**
- d₁ = −(s − 1)/2: independent of p.
- e₁ = p/2 (repo pairing α_{n−1}/(2b_n)) and e₁ˢ = −p/2 (standard pairing α_n/(2b_n)): independent of s.
- k₀ = −(s − 1) − p/2, k₁ = −(p + 2)a, a = (2s − 2 − p)/(2p). For p = 2 these are the values found in RH.md §8.3
  (k₀ = −2, k₁ = 0 at s = 2; k₀ = −3, k₁ = −2 at s = 3).
- Consistency: Lemma 5.1 of RH.md (unfolding) gives d₁ = (p/2 + k₀)/2 = −(s − 1)/2 and e₁ = p/2 from (k₀, k₁).
- Linearity in s and the Christoffel constraint d₁(s + p) − d₁(s) = −p/2 (Cor 3.3) hold to the same accuracy
  (`checks/check_so_shift.out` [C]).
- An "effective index" form of the conjecture: b_n = c(p)(n + (s − 1)/(2p))^{−p}(1 + O(n^{−1−min(1,p)})), i.e. the shift
  is (α_x + 1)/2.

**Conjecture P62 (CONJECTURE; evidence: §1.1, §2, §3. Plan 65: PROVED-mod-cite for p > 1, with remainder O(n⁻²) for b_n, α_n and the chain — E_pgt1.md Thm E.1, Cor E.6, Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md). Plan 66: at p = 1 PROVED-mod-cite for d₁, e₁, e₁ˢ, k₀ with remainder O(n⁻²) — E_p1.md Thm E1.10 (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md). Plan 67: PROVED-mod-cite for 0 < p < 1, with the conjectured remainder O(n^{−1−p}) for b_n, α_n and the chain and the n^{−1−p} coefficient identified — E_plt1.md Thm E′.1, Cor E′.6 (Plan 67, E_plt1.md; not REVIEWED)).** For every p > 0 and s > 1,

  n^pb_n = c(p)(1 − (s − 1)/(2n) + O(n^{−1−min(1,p)})),  α_n/(2b_n) = 1 − p/(2n) + O(n^{−1−min(1,p)}),

equivalently α_{n−1}/(2b_n) = 1 + p/(2n) + O(·). Limits of the evidence: grid p ∈ [½, 4], s ∈ [3/2, 4], n ≤ 1600; the
error estimates are not bounds; the remainder exponent 1 + min(1, p) is read off p = ½ only.

## 2. Exact results at p = 2 — PROVED-mod-cite

**Lemma 2.1 (symmetric chain; PROVED, elementary).** Let σ be a positive measure on [0, ∞) with infinite support and
finite moments, and ν its symmetrization (∫f(t²)dν(t) = ∫f dσ, ν even). The monic OPs R_N of ν satisfy
tR_N = R_{N+1} + γ_N²R_{N−1}, R_{2m}(t) = π_m(t²), R_{2m+1}(t) = tπ_m^{(1)}(t²), where π^{(1)} are the monic OPs of xσ,
and α_m = γ_{2m}² + γ_{2m+1}², b_m² = γ_{2m−1}²γ_{2m}² (γ_0 := 0). With g_m := γ_{2m+1}², h_m := γ_{2m}² this is
Lemma CT's decomposition, and g_m = −π_{m+1}(0)/π_m(0).

*Proof.* ν is even, so its Jacobi matrix has zero diagonal. R_{2m}(t) := π_m(t²) is monic of degree 2m, even, hence
orthogonal to odd polynomials, and ∫R_{2m}(t)t^{2j}dν = ∫π_m x^j dσ = 0 for j < m. tπ_m^{(1)}(t²) is odd and
∫tπ_m^{(1)}(t²)t^{2j+1}dν = ∫π_m^{(1)}x^j·x dσ = 0 for j < m. Uniqueness of monic OPs gives the two formulas. Evaluate
tR_{2m+1} = R_{2m+2} + γ_{2m+1}²R_{2m} at t → 0 (with R_{2m+1}(t)/t bounded): 0 = π_{m+1}(0) + γ_{2m+1}²π_m(0). Two steps
of the t-recurrence give t²R_{2m} = R_{2m+2} + (γ_{2m}² + γ_{2m+1}²)R_{2m} + γ_{2m−1}²γ_{2m}²R_{2m−2}, i.e. the
recurrence of π_m. ∎

**Lemma 2.2 (Darboux step; PROVED; = Lemma CT of G1 §3.21).** xσ has α'_m = γ_{2m+1}² + γ_{2m+2}² and
b'_m² = γ_{2m}²γ_{2m+1}². *Proof.* Two steps of the t-recurrence on the odd R's: t²R_{2m+1} = R_{2m+3} +
(γ_{2m+1}² + γ_{2m+2}²)R_{2m+1} + γ_{2m}²γ_{2m+1}²R_{2m−1}; divide by t. ∎ Conversely, given (α, b) of a measure, the
chain with γ_0 = 0 is determined recursively (γ_1² = α_0, γ_{2m}² = b_m²/γ_{2m−1}², γ_{2m+1}² = α_m − γ_{2m}²), so any
positive sequence satisfying the three chain relations *is* the chain.

**Input (Paper 2 Remark rem:pure-lommel; VA §3, DLMF (10.2.2), (10.6.1), (10.16.1), (4.22.3); RH/CITATIONS.md entries
VA and DLMF-Lommel).** For σ_{2,2}, b_n = π²/((4n + 1)√((4n − 1)(4n + 3))) and α_n = 2π²/((4n + 1)(4n + 5)) (n ≥ 1; α₀ = π²/15). Equivalently
(Lemma 2.1, after x ↦ x/π², which makes c(2) = 1/16) γ_N² = 1/((2N + 1)(2N + 3)) (N ≥ 1, γ₀ = 0). The script checks
these against the chain (part (0) of `checks/check_so_exact_p2.out`).

**Theorem 2.3 (p = 2, s ∈ {2, 4, 6, 8, 10}; PROVED-mod-cite (input above) + exact computer algebra).** After
x ↦ x/π², the chains of σ_{2,4}, σ_{2,6}, σ_{2,8} are the rational functions listed in `checks/check_so_exact_p2.py`
(e.g. σ_{2,4}: h_m = m(2m+1)/((m+1)(2m+3)(4m+3)(4m+5)), g_m = (m+2)(2m+5)/((m+1)(2m+3)(4m+5)(4m+7))), and the
coefficients of σ_{2,s} have the exact expansions

  n²b_n/c(2) = 1 − (s − 1)/(2n) + (s² + 6s − 11)/(16n²) + O(n⁻³),
  α_{n−1}/(2b_n) = 1 + 1/n + O(n⁻²),  α_n/(2b_n) = 1 − 1/n + O(n⁻²),
  γ_N²·4N² = 1 + (−s − 2(s − 2)(−1)^N)/N + O(N⁻²)  (k₀ = −s, k₁ = −2(s − 2); s ≤ 8 for the chain).

*Proof.* s = 2 is the input. For s = 4, 6, 8, Lemma 2.2 gives (α', b'²) of σ_{2,s} = x·σ_{2,s−2} from the chain of
σ_{2,s−2}, and the script verifies **as identities of rational functions in m** (sympy `cancel`) that the listed
closed form satisfies γ_1² = α'_0, γ_{2m−1}²γ_{2m}² = b'_m², γ_{2m}² + γ_{2m+1}² = α'_m. The closed forms are finite at every
integer m ≥ 0 (checked: no denominator root at a non-negative integer), and the true chain has γ_{2m−1}² > 0, so by the
uniqueness remark in Lemma 2.2 the closed form is the chain. s = 10 uses Lemma 2.2 once more
on the s = 8 chain. The expansions are exact series of rational functions (with a square root for b_n) in 1/n. Output:
`checks/check_so_exact_p2.out` (all assertions pass, including d₁, d₂, e₁, e₁ˢ, k₀, k₁). ∎

The p = 2 values agree with Conjecture P62 (d₁, e₁, e₁ˢ, k₀, k₁). The closed forms for s = 6, 8 were found by rational
interpolation of exact rational data (≤ 60 points, degree ≤ 11) and then verified as identities; the interpolation step
is not part of the proof. The second-order coefficient d₂(2, s) = (s² + 6s − 11)/16 also matches the p = 2, s = 3
numerics (d₂ = 1.000; RH/checks/check_fine.out) — a by-product, not pursued further.

## 3. Soft identities

### 3.1 Christoffel shift s ↦ s + p

**Proposition 3.1 (product identity; PROVED).** For any positive σ on [0, ∞) with infinite support and finite
moments, with b'_m the off-diagonal coefficients of x·σ and g_m as in §0,

  Π_{m=1}^n (b'_m/b_m)² = g_n/g_0,  g_0 = α_0 = ∫x dσ/∫dσ.

*Proof.* Lemma CT (G1 §3.21) / Lemma 2.2: b_m² = g_{m−1}h_m and b'_m² = g_mh_m, so (b'_m/b_m)² = g_m/g_{m−1}; telescope. ∎

**Theorem 3.2 (Christoffel–Cesàro with exact constant; PROVED-mod-cite: pointwise Law P for σ_{p,s} (Paper 2
Cor. thm:pure; RH_p, RH₁(r), RH_plt1b) and G1 Lemma CS).** For p > 0, s > 1, with b_m(s) := b_m(σ_{p,s}):

  Σ_{m=1}^n log(b_m(s + p)/b_m(s)) + (p/2)log n → ½log(c(p)ζ(s)/ζ(s + p))  (n → ∞).

*Proof.* Prop 3.1 with σ = σ_{p,s}, x·σ = σ_{p,s+p}, g_0 = ζ(s + p)/ζ(s): 2Σ_{m≤n}log(b'_m/b_m) = log(n^pg_n) − p log n
− log g_0. Law P for σ_{p,s} and Lemma CS give n^pg_n → c. ∎

*Remark.* Only Law P without rate is used. Lemma CS-r with the O(1/n) rate gives n^pg_n − c = O(n^{−1/2}) (sharp in
general, G1 §3.21), so Theorem 3.2 has an O(n^{−1/2}) error a priori.

**Corollary 3.3 (CONDITIONAL on (E) at s and s + p + PROVED-mod-cite (Law P: Paper 2 Cor. thm:pure / RH_p, RH₁(r), RH_plt1b; G1 Lemma CS)).** If (E_ε) holds for σ_{p,s} and σ_{p,s+p} with coefficients
d₁(s), d₁(s + p), then d₁(s + p) = d₁(s) − p/2. Moreover then G_n := n^pg_n = c(1 + O(n^{−ε′})) and
n(G_n − G_{n−1}) → 0 (ε′ := min(ε, 1)), i.e. the hypothesis of G1 Remark SH-1/n holds.

*Proof.* Under (E_ε) at both points, log(b_m(s+p)/b_m(s)) = (d₁(s+p) − d₁(s))/m + O(m^{−1−ε′}) (the quadratic term of log(1 + x) is O(m⁻²)), so the left side of
Theorem 3.2 is (d₁(s+p) − d₁(s) + p/2)log n + O(1). Its convergence forces d₁(s+p) − d₁(s) = −p/2. Then
log(g_m/g_{m−1}) = 2log(b'_m/b_m) = −p/m + O(m^{−1−ε′}), so log(n^pg_n) = log c + O(n^{−ε′}) (the limit is log c by
Lemma CS), and G_n/G_{n−1} = (n/(n−1))^p·g_n/g_{n−1} = (1 + p/n + O(n⁻²))(1 − p/n + O(n^{−1−ε′})) = 1 + O(n^{−1−ε′}),
so n(G_n − G_{n−1}) = O(n^{−ε′}) → 0. ∎

**Theorem 3.4 (e₁ from the existence of d₁; CONDITIONAL on (E_ε) at s and s + p, ε > ½, + PROVED-mod-cite (Law P: Paper 2 Cor. thm:pure / RH_p, RH₁(r), RH_plt1b; G1 Lemma CS)).** Then

  α_n/(2b_n) = 1 − p/(2n) + O(n^{−2ε′}),  ε′ = min(ε, 1),

so e₁ˢ = −p/2 (standard pairing), and α_{n−1}/(2b_n) = 1 + p/(2n) + O(n^{−2ε′}) (repo pairing, e₁ = p/2). In particular
e₁ˢ = −p/2 whatever the values d₁(s), d₁(s + p); only their existence (with ε > ½) is used ("kinematic").

*Proof.* α_n = h_n + g_n = b_n²/g_{n−1} + g_n. Put X := b_n/g_{n−1}. Then α_n/(2b_n) = ½(X + g_n/b_n) =
½(X + (g_n/g_{n−1})/X). By Cor 3.3, g_n/g_{n−1} = 1 − p/n + O(n^{−1−ε′}) and g_{n−1} = c(n−1)^{−p}(1 + O(n^{−ε′})), while
b_n = cn^{−p}(1 + O(1/n)); so X = 1 + O(n^{−ε′}). Hence α_n/(2b_n) = ½(X + 1/X) − p/(2nX) + O(n^{−1−ε′}) =
1 + (X − 1)²/(2X) − p/(2n) + O(n^{−1−ε′}) = 1 − p/(2n) + O(n^{−2ε′}). For the repo pairing,
α_{n−1}/(2b_n) = (α_{n−1}/(2b_{n−1}))·(b_{n−1}/b_n), and b_{n−1}/b_n = 1 + p/n + O(n^{−1−ε′}) by (E), so
α_{n−1}/(2b_n) = (1 − p/(2n))(1 + p/n) + O(n^{−2ε′}) = 1 + p/(2n) + O(n^{−2ε′}). ∎

*Remark.* This is the exact version of RH.md Lemma 5.1's observation that "e₁ = p/2 for every weight": there it came from
assuming a γ-chain expansion; here it needs only (E) for b at s and s + p.

### 3.2 Weight perturbations of relative size O(1/k)

For weights w on the nodes x_k = k^{−p} write h_n(w), b_n(w), and μ_n^w(k) := w_kπ_n(x_k)²/h_n(w) (π_n = π_n^w).

**Proposition 3.5 (PROVED; internal input: G1 Lemma Sat_p⁺, §3.3).** Let v, w > 0 be weights on {k^{−p}} with
Σv_k < ∞, v_k ≥ c₁k^{−A} for some c₁ > 0, A and all k, and |log(w_k/v_k)| ≤ C/k for all k ≥ 1. Then log h_n(w) − log h_n(v) = O(1/n). Consequently

  Σ_{j=1}^n log(b_j(w)/b_j(v)) = −½log(Σ_kw_k/Σ_kv_k) + O(1/n).

*Proof.* Put f := log(w/v), w(t) := ve^{tf} (t ∈ [0, 1]); all w(t) lie in the sandwich e^{−C}v ≤ w(t) ≤ e^Cv.
- (Envelope.) h_n(t) = min over monic π of degree n of Σ_kw_k(t)π(x_k)², a ratio of Hankel determinants of the moments
  Σ_kw_k(t)x_k^j, which are C¹ in t (termwise differentiation; |f| ≤ C, x_k ≤ 1, Σv_k < ∞). As in G1 Lemma TV / Prop 3.7
  below, (d/dt)log h_n(t) = Σ_kf(k)μ_n^{(t)}(k), because the derivative of π_n^{(t)} has degree < n and is orthogonal to
  π_n^{(t)}.
- (Bound.) Fix the head margin M₀ = M₀(p) ≥ 4 with g_p⁺ ≥ 1 on (0, 1/M₀] (as in T3-sv/Theorem L, G1 §3.8). For
  k ≥ n/M₀, |f(k)| ≤ CM₀/n. For k < n/M₀, Lemma Sat_p⁺ gives μ_n(k) ≤ 1 − ρ_n(k) ≤ (W_t/w_k(t))((n+1)/k)^{2(1−p)₊}e^{−2n},
  with W_t ≤ e^CΣv and w_k(t) ≥ e^{−C}v_k ≥ e^{−C}c₁n^{−A}. So the head contributes at most
  C·n·(n+1)²·e^{2C}(Σv)n^A·e^{−2n}/c₁ = O(e^{−n}). Hence |(d/dt)log h_n(t)| ≤ CM₀/n + O(e^{−n}) uniformly in t.
- Integrate over t ∈ [0, 1]. For the sum: Σ_{j≤n}log b_j² = log h_n − log h_0 and h_0 = total mass. ∎

(The hypothesis v_k ≥ c₁k^{−A} is used only in the head bound.)

**Corollary 3.6 (Tricomi–Carlitz anchor at p = 1).** Let σ = σ_{1,3/2} and TC(α = 1) the Tricomi–Carlitz measure: the
same atoms 1/k with masses v_k = k^{k−1}e^{−k}/k! and b_n^{TC} = 1/√(2n(2n+1)) (RH_p1.md §0–§1, PROVED, REVIEWED;
item 11 §7). Put W_TC := Σ_kv_k.
- (i) (PROVED-mod-cite: RH_p1 §1, DLMF 5.11.1 + §5.11(ii).) Σ_{j=1}^n log(b_j(σ)/b_j^{TC}) =
  −½log(ζ(3/2)/(√(2π)W_TC)) + O(1/n).
- (ii) (CONDITIONAL on (E) at (1, 3/2) + PROVED-mod-cite as (i).) d₁(1, 3/2) = −1/4 = −(s − 1)/2.
- (iii) (CONDITIONAL on (E) at (1, 3/2 + j), 0 ≤ j ≤ m, + PROVED-mod-cite (Law P: Paper 2 Cor. thm:pure / RH_p, RH₁(r), RH_plt1b; G1 Lemma CS).) d₁(1, 3/2 + m) = −(1 + 2m)/4 = −(s − 1)/2.

*Proof.* (i) RH_p1 §1: k^{−3/2} = √(2π)H(k)v_k with H(t) = Γ(t + 1)e^t/(√(2π)t^{t+1/2}) = 1 + 1/(12t) + O(t⁻²) (DLMF 5.11.1
with the §5.11(ii) remainder bound on the real axis), and H(k) ∈ (0, ∞) for every k, so |log H(k)| ≤ C/k for all k ≥ 1.
Apply Prop 3.5 with w := σ's masses, v := √(2π)v_k (the constant does not change b^{TC}); v_k ≍ k^{−3/2}, so v_k ≥ c₁k^{−3/2} with c₁ > 0 (v₁ = √(2π)/e < 1, hence the constant c₁). (ii) TC: nb_n^{TC} =
½(1 + 1/(2n))^{−1/2} = ½(1 − 1/(4n) + O(n⁻²)). If (E) holds for σ, (i) forces d₁(σ) = −1/4 (as in Cor 3.3). (iii) Cor 3.3,
m times. ∎

*Remarks.* (a) W_TC = 1 numerically (`checks/check_so_shift.out` [D] tests the limit with W_TC := 1: T_n − limit = 2.6·10⁻⁵ at n = 1600, and n(T_n − limit) → 0.04165 ≈ 1/24, the second-order constant of RH_p1; the tree-function
identity Σk^{k−1}e^{−k}/k! = 1 is classical but not cited, and not used: (i) is stated with W_TC). (b) Numerically
b_n(σ)/b_n^{TC} = 1 − 1/(24n²) + … (RH_p1 §0: n²(b_n^σ/b_n^{TC} − 1) → −1/24, CONJECTURE), which is (E) at (1, 3/2) with
ε = 1 and d₁ = −1/4: (ii) is consistent with it. The −1/24 conjecture is a statement about the *second* order and is not
addressed here. (c) (HEURISTIC) Prop 3.5 suggests why the 1/k-correction of the TC masses (H(k) = 1 + 1/(12k) + …) does not
change d₁: a weight factor 1 + ε/k shifts log h_n by ε·E_n[1/k] = O(1/n) (proved), and log b_n² by the difference of two
such terms, which one expects to be O(1/n²) (not proved; only the Cesàro consequence (ii) is). *Plan 66:* (b) is E_p1 Thm E1.6
(b_n, α_n, g_n, h̃_n of σ_{3/2} = TC values × (1 − 1/(24n²) + O(n⁻³))); (c) is made precise by E_p1 Prop E1.4(iii) (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md).

### 3.3 The s-derivative identity

**Proposition 3.7 (PROVED, elementary).** For fixed p > 0 and n ≥ 0, s ↦ h_n(s) := h_n(σ_{p,s}) is real-analytic on
(1, ∞) and

  ∂_s log h_n(s) = −Σ_k (log k)·μ_n^{(s)}(k) =: −L_n(s),  μ_n^{(s)}(k) := k^{−s}π_n(x_k)²/h_n(s).

Hence Σ_{j=1}^n ∂_s log b_j(s)² = −L_n(s) + L_0(s), with L_0(s) = −ζ′(s)/ζ(s).

*Proof.* h_n = D_{n+1}/D_n with D_n = det(ζ(s + p(i + j)))_{0≤i,j<n} > 0, analytic in s > 1. The coefficients of
π_n^{(s)} are rational in the moments, hence C¹. d/ds Σ_kk^{−s}π_n(x_k)² = −Σ_k log k·k^{−s}π_n(x_k)² + 2Σ_kk^{−s}π_n(x_k)∂_sπ_n(x_k);
termwise differentiation is justified because |π_n(x_k)| ≤ max_{[0,1]}|π_n| and Σk^{−s}log k converges locally uniformly; the
second sum vanishes since ∂_sπ_n has degree < n. Sum over j using h_n = ζ(s)Π_{j≤n}b_j². ∎

So, with Λ_m(s) := L_m(s) − log m = Σ_k log(k/m)μ_m(k) (m ≥ 1): ∂_s log b_n² = −log(n/(n−1)) − (Λ_n(s) − Λ_{n−1}(s))
(n ≥ 2), and Σ_{j≤n}∂_s log b_j² = −log n − Λ_n(s) + L_0(s). The slope −½ of d₁ in s is the statement that the localized
measure μ_n (scale k ≍ n, Lemma LP) has a log-moment Λ_n(s) that is bounded and, pointwise, changes by o(1/n) from n − 1
to n (HEURISTIC reading; only the Cesàro form below is proved).

**Hypothesis (UΛ) on [s₀, s₁].** sup_{s∈[s₀,s₁]}|Λ_n(s)| = o(log n) as n → ∞. — *Plan 64:* PROVED-mod-cite, UL.md Theorem UΛ
(REVIEWED, REVIEW_Plan64.md).

*Status of (UΛ).* For each fixed s, Λ_n(s) = O(1): the part k ≥ n is Corollary QLP-Λ (G1 §3.16, PROVED-mod-cite, REVIEWED,
for each fixed σ); for k < n, 0 ≤ log(n/k) ≤ (1/p)(n/k)^p = (1/p)n^px_k, so Σ_{k<n}log(n/k)μ_n(k) ≤ (1/p)n^pΣ_kx_kμ_n(k) =
(1/p)n^pα_n → 2c/p (Law P). Uniformity in s on [s₀, s₁] is what (UΛ) adds: it holds under hypothesis (RU) of G1 §3.16
(σ-uniformity of the cited RH analyses; Audit U: PROOF SKETCH), which makes QLP-Λ uniform on compacts, and (for the k < n half) Law P's α-part n^pα_n → 2c uniform on [s₀, s₁],
also from the uniform small-norm bounds of (RU). So (UΛ) ⇐ (RU), an implication at PROOF SKETCH level (as Audit U).
*Plan 64 update:* (UΛ) holds (UL.md Thm UΛ, PROVED-mod-cite, REVIEWED), without (RU); the α-part of Law P uniform on
[s₀, s₁] required above (review F10) is UL.md Thm UP. Only the O(1) strengthening sup|Λ_n| = O(1) needs uniform
hard-edge control ((RU), or (SCVX)/(CVX): UL.md Prop R); it is a GAP.

**Hypothesis (CVX) on [s₀, s₁] (alternative to (UΛ)).** For all large n, s ↦ log h_n(σ_{p,s}) is convex on [s₀, s₁].

*Why it is natural.* log D_n(s) (D_n the n×n Hankel determinant) is convex, being the log of a positive combination of
exponentials e^{−sΣ_{k∈S}log k} over n-subsets S; its second derivative is Var_n(Σ_{k∈S}log k) in the n-point discrete
OP ensemble. So (log h_n)″ = Var_{n+1} − Var_n, and with the projection P_n onto span{q_0, …, q_{n−1}},
Var_n = ‖(I − P_n)fP_n‖²_HS = Σ_{i<n≤j}|f(J)_{ij}|² (f = log k as a function of the Jacobi operator J). For f = log k the
cross-cut flux is log-correlated (Toeplitz symbol log(2 + 2cos θ), Fourier coefficients ≍ 1/m), so it grows like log n and
its increments are positive asymptotically (HEURISTIC). (For f = x it is b_n², which decreases.) (Exact level-n form: UL.md Prop SV, ∂_s²log h_n = Σ_{j>n}f_{nj}² − Σ_{i<n}f_{in}²; (CVX) fails at the top level of finite
truncations, UL.md Remark CVX-fin.) Numerically consistent with (CVX)
(`checks/check_so_convex.out`): 300-digit Hankel determinants for n ≤ 8, p ∈ {½, 1, 2}, s ∈ [3/2, 4] (positive second
differences, step ½); and the grid data for n ≤ 1600 (positive second divided differences at the grid points s = 3/2, 2,
3, 4, roughly 1/(2p²n); dd ≈ (log h_n)″/2, so (log h_n)″ ≈ 1/(p²n)). Not proved.

*(CVX) suffices (no longer needed for Thms 3.8–3.10 after Plan 64: UL.md UF-lim).* If log h_n is convex on [s₀, s₁], then −L_n(s₀) ≤ (log h_n(s₁) − log h_n(s₀))/(s₁ − s₀) ≤ −L_n(s₁),
and L_n(s_i) = log n + O(1) at the two **fixed** endpoints (QLP-Λ + Law P, no uniformity). So Theorem 3.8 below holds with
o(log n) improved to O(1), under (CVX) instead of (UΛ).

**Theorem 3.8 (s-slope, Cesàro form; Plan 64: PROVED-mod-cite, UL.md Cor UL-3.8 ((P), (LP), (QLP-c) at fixed points only (finitely many for each grid, countably many in all); no uniformity in σ, (RU) not used; Lemma CS), REVIEWED. The
proof below is the earlier route, CONDITIONAL on (UΛ) or on (CVX), on [s₀, s₁], + PROVED-mod-cite (QLP-Λ, Law P)).**

  Σ_{j=1}^n log(b_j(s₁)/b_j(s₀)) = −((s₁ − s₀)/2)log n + o(log n)  (+ O(1) instead of o(log n) under (CVX)).

*Plan 64 (UL.md Cor UL-3.8):* unconditionally, for every p > 0 and s₀, s₁ > 1, the right side is
−((s₁ − s₀)/2)log n + ½log(c^{(s₁−s₀)/p}ζ(s₀)/ζ(s₁)) + o(1).

*Proof.* Integrate Prop 3.7 over s ∈ [s₀, s₁] (everything is continuous in s): 2Σ_{j≤n}log(b_j(s₁)/b_j(s₀)) =
−(s₁ − s₀)log n − ∫Λ_n ds + ∫L_0 ds, and |∫Λ_n ds| ≤ (s₁ − s₀)sup|Λ_n| = o(log n) under (UΛ). Under (CVX) use the
secant bound above: 2Σ_{j≤n}log(b_j(s₁)/b_j(s₀)) = log h_n(s₁) − log h_n(s₀) − log(ζ(s₁)/ζ(s₀)) = −(s₁ − s₀)log n + O(1). ∎

**Corollary 3.9 (CONDITIONAL on (E) at s₀, s₁ (+ PROVED-mod-cite: UL.md Cor UL-3.8; Plan 64, REVIEWED; earlier: also
on (UΛ) or (CVX) on [s₀, s₁])).** d₁(s₁) − d₁(s₀) = −(s₁ − s₀)/2. Combined with
the anchors:
- p = 2: d₁(2, s) = −(s − 1)/2 for every s > 1 (anchor s₀ = 2, Theorem 2.3), under (E) at s;
- p = 1: d₁(1, s) = −(s − 1)/2 for every s > 1 (anchor s₀ = 3/2), under (E) at s — (E) at 3/2 is not needed: Theorem 3.10(b),(d) give 𝒟_n(s) = −((s−1)/2)log n + O(1) directly (O1; UL.md Cor UL-3.10);
- every p: d₁(p, s) = −(s − 1)/2 + g(p) with g independent of s, under (E) at the points used. The value
  g(p) = 0 for p ∉ {1, 2} is **not** obtained by any soft argument here (GAP; NUMERICAL g = 0).
- *Plan 65:* for p > 1, (E) holds at every s (E_pgt1 Thm E.1), so the corollary is unconditional there, and Thm E.1 gives
  d₁ = −(s−1)/2 directly: g(p) = 0 for every p > 1 (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)).
- *Plan 66:* for p = 1, (E) holds at every s (E_p1 Thm E1.10), so the corollary is unconditional there and g(1) = 0 (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md).

*Proof.* As in Cor 3.3: under (E) the left side of Theorem 3.8 is (d₁(s₁) − d₁(s₀))log n + O(1). ∎

*Remark (tilt law).* The same computation with w(t) = k^{−s}Ψ(k)^t, Ψ = exp L₁(log k), gives Σ_{j≤n}log(b_j(vΨ)/b_j(v)) =
½L₁(log n) + o(L₁(log n))-type statements under a uniform log-moment hypothesis of the same kind (QL of G1 §3.14 along the
path). At the pointwise level this is the tilt law n^pb_n/c = 1 − (s − 1 − ϑ_n)/(2n) + o(ϑ_n/n), ϑ_n = L₁′(log n), of G1
§3.17 (CONJECTURE): the factor Ψ acts as a local change of s by −ϑ_n. Not pursued (HEURISTIC).

### 3.4 The 1/n coefficient in logarithmic-average form

Put 𝒟_n(p, s) := Σ_{j=1}^n log(j^pb_j/c(p)) = ½log h_n − ½log ζ(s) + p log n! − n log c(p). Under (E),
𝒟_n = d₁ log n + O(1). Without (E), say that σ_{p,s} has **log-average coefficient** d if 𝒟_n = d·log n + O(1).

**Theorem 3.10 ((a)–(c) PROVED-mod-cite: Paper 2 Cor. thm:pure (Law P), G1 Lemma CS, Theorem 2.3's input; RH_p1 §1, DLMF 5.11. (d) Plan 64: PROVED-mod-cite, UL.md Cor UL-3.10 (UF-lim; SECOND §2 Input (VA, DLMF-Lommel); Cor 3.6(i) (RH_p1 §1, DLMF 5.11)), REVIEWED).**
- (a) p = 2 and every even s = 2 + 2m (m ≥ 0): σ_{2,s} has log-average coefficient −(s − 1)/2.
- (b) p = 1 and every s = 3/2 + m (m ≥ 0): σ_{1,s} has log-average coefficient −(s − 1)/2.
- (c) For every p > 0, s > 1: σ_{p,s} has a log-average coefficient iff σ_{p,s+p} has, and the two differ by −p/2.
- (d) For every s > 1 (p = 2 resp. p = 1): log-average coefficient −(s − 1)/2, with 𝒟_n + ((s − 1)/2)log n convergent.
- (c′) (UL.md Cor UL-3.10) For every p > 0 and s, s₀ > 1: 𝒟_n(p, s) − 𝒟_n(p, s₀) + ((s − s₀)/2)log n →
  ((s − s₀)/(2p))log c − ½log(ζ(s)/ζ(s₀)); so (c) holds for all real shifts.

Equivalently, for the Hankel ratios of zeta values (Paper 2 Remark rem:pure-zeta): with h_n = D_{n+1}/D_n,
D_n = det(ζ(s + p(i + j)))_{0≤i,j<n}, log h_n = log ζ(s) − 2p log n! + 2n log c(p) − (s − 1)log n + O(1) in cases (a), (b), and (Plan 64, UL.md Cor UL-3.10(d′)) for every s > 1 at p ∈ {1, 2}, with O(1)
improvable to const + o(1).

*Proof.* (c) is Theorem 3.2. (a): at s = 2, 𝒟_n = −½log n + O(1) by the exact b_n (input of Theorem 2.3); then (c) m
times. (b): at s = 3/2, Cor 3.6(i) and nb_n^{TC} = ½(1 − 1/(4n) + O(n⁻²)) give 𝒟_n = −¼log n + O(1); then (c). (d) UL.md Cor UL-3.10 (earlier
route: Theorem 3.8 under (UΛ) or (CVX)). ∎

This is the only form in which the 1/n coefficient is proved here without (E): it identifies the coefficient on the
lattices s₀ + pℕ₀ (s₀ = 2 at p = 2, s₀ = 3/2 at p = 1), and by UL.md Cor UL-3.10 at every s > 1 for p ∈ {1, 2}. For p ∉ {1, 2} there is no anchor (§4).

## 4. Existence of the 1/n coefficient (p > 1: E_pgt1.md; p = 1: E_p1.md; 0 < p < 1: E_plt1.md)

*Plan 65 (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)):* for p > 1 the GAP below is closed by `E_pgt1.md` (Thm E.1, Cor E.6). Step 1 is as stated; step 3 is resolved by
E_pgt1 Lemma E.2 (H_n is constant to O(n^{−p}), so Δ₁^{(N)} = Δ₁^{(∞)} + O(N^{−p})); steps 2, 4, 5 are E_pgt1 Lemmas E.3–E.5 and
Prop. E.5′. The computed values are d₁ = −(s−1)/2, e₁ˢ = −p/2, k₀ = −(s−1) − p/2, k₁ = −(p+2)a, with remainder O(n⁻²). The
text below is the Plan 62 statement, kept as written; it remains the GAP statement for 0 < p ≤ 1.
*Plan 66 (Plan 66, E_p1.md; REVIEWED 2026-10-15, REVIEW_Plan66_A.md, REVIEW_Plan66_B.md):* for p = 1 the GAP is closed by `E_p1.md` (Thm E1.10): the obstruction of E_pgt1 §9 concerns the
x-frame; in the symmetric frame of RH₁(r) the second-order matching works (E_p1 §§3–4). The text below remains the GAP statement
for 0 < p < 1.
*Plan 67 (Plan 67, E_plt1.md; not REVIEWED):* for 0 < p < 1 the GAP is closed by `E_plt1.md` (Thm E′.1, Cor E′.6). Step 3 is replaced by
E_plt1 Lemma F.1: the seam band factor is flat only to O(n^{−p}), with the explicit linear part log H_n(z) − log H_n(1) =
−2ζ(−p)(z−1)n^{−p} + O(n^{−2p}); by the invariance of the global parametrix it enters only through the Bessel/Airy
corrections Δ₁/n, hence at order n^{−1−p} (coefficient κ_p = 2pc(p)ζ(−p)). (E_ε) holds with ε = p, sharp. The text below is
the Plan 62 statement, kept as written; with Plans 65–67 (E) is now proved for every p > 0.

**(E) for pure powers (GAP).** For which (p, s) does n^pb_n/c(p) = 1 + d₁/n + O(n^{−1−ε}) hold with some ε > 0?
Known: all (p, s) with an O(1/n) remainder (RH_p, RH₁(r), RH_plt1b; Paper 2 Cor. thm:pure); exactly p = 2, s ∈ {2, …, 10}
even (Theorem 2.3). With (E), §3 gives d₁ for p ∈ {1, 2} (UL.md: all s, given (E) at s) and the s-dependence for
all p; e₁ follows from d₁ (Theorem 3.4).

**What the O(1/n) proofs give, and what is missing (PROOF SKETCH for p > 1, RH_px frame).**
1. *Outer parametrix: no 1/n term.* In RH_px §5 the global parametrix N gives (N₁)₁₂(N₁)₂₁ = c² and a(N) = 2c
   **exactly**, for every N, because the Szegő conjugation D_{w,∞}^{σ₃}N₀D_w^{−σ₃} and the normalization κ are of the
   invariant form (RH_px §5, invariance lemma). The N-dependent band factor h_N (D̃ = 1 + O(1/N) by Stirling, B/B(1) =
   1 + O(1/N), RH_px Lemma 3.2(iv)) therefore does **not** produce a 1/n term in b_n at first order. So d₁ comes only
   from the local parametrices.
2. *Local parametrices.* All 1/N corrections come from J_𝒵 − I on ∂U(0, δ) (Bessel, order α_x, KMVV (6.42)–(6.53)) and
   on ∂U(4c, ε) (Airy, band–saturated form of WLXZ §6.1); the lens lips, the saturated region and the top are O(e^{−cN})
   or O(N^{−pN}) (RH_px §§3–4), and the hard-edge mismatch inside U(0, δ) is O(N^{−K}) (RH_px Lemma 4.3). The full
   large-argument expansions are available in sources already read: DLMF 10.40.1–10.40.5 (I_α, K_α; RH/CITATIONS
   "DLMF-10.40") for the Bessel model Ψ of KMVV (6.23), and DLMF 9.7.5–9.7.6 (RH/CITATIONS "DLMF-9") for the Airy model.
   They give J_𝒵 = I + Δ₁^{(N)}/N + O(N⁻²) on the two circles, with Δ₁^{(N)} explicit in terms of N(z), W̃(z), the
   conformal maps f (at 0) and f_r (at 4c), and the expansion coefficients a₁(α_x), u₁, v₁.
3. *N-dependence of Δ₁.* Δ₁^{(N)} depends on N through h_N (in D_w and W̃). One needs Δ₁^{(N)} = Δ₁^{(∞)} + O(N^{−ε})
   uniformly on the circles. Ingredients: D̃ = 1 + O(1/N) on the circles (DLMF 5.11 in |ph t| ≤ π/p < π, p > 1),
   B/B(1) = 1 + O(1/N) including the boundary values at the crossing with (−∞, 0) (RH_px Lemma 3.2(iv)–(v)), and a Cauchy-
   integral bound for the Szegő function of the O(1/N) perturbation log(h_N/h_N(1)) on the band at distance δ.
   Not written out.
4. *Second-order small norm.* With ‖J_𝒵 − I − Δ₁^{(N)}/N‖_{L¹∩L²∩L^∞} = O(N⁻²) and the N-uniform bound on the Cauchy
   operator already used in RH_px §5, the Neumann series gives 𝒵₁ = −(1/2πi N)∮Δ₁^{(N)} + O(N⁻²) (routine; not written).
5. *Extraction.* N^pb_N/c = 1 + ℓ(𝒵₁)/2 + O(N⁻²) with ℓ the linear functional (𝒵₁)₁₂/(N₁)₁₂ + (𝒵₁)₂₁/(N₁)₂₁ in the
   D_{w,∞}-frame. Then (E₁) holds with d₁ = ½lim_N Nℓ(𝒵₁).

Steps 1–5 would prove (E_1) for every p > 1, s > 1; with step 3's rate O(N^{−ε}) only (E_ε). This is a PROOF SKETCH:
none of steps 2–5 is written out symbol by symbol, and step 3 is the only non-routine one (the Hölder behaviour of B at 0,
ν = min(1/p, ½), must not spoil the rate on ∂U(0, δ)).

**Computing d₁ itself** from steps 2–5 needs the residues of Δ₁^{(∞)} at 0 and 4c, i.e. f′(0), the first two Taylor
coefficients of φ̃ at 4c, and the Szegő function of x^{α_x}(4c − x) near 0 and 4c; these are explicit but p-dependent
through μ* (G2 B*). Conjecture P62 predicts that the p-dependence cancels, leaving −(s − 1)/2. Given §3, it suffices to
do this at one s per p (g(p) := d₁ + (s − 1)/2 is s-independent under (E)); α_x = 0 (s = 1 + p) is the natural
choice (Bessel order 0, no Fisher–Hartwig factor). **GAP.** *Plan 65:* done for p > 1 at every s (E_pgt1 §§4–7): the
hard-edge residue is c(p+2)(4α²−1)/16·[[1, i], [i, −1]], annihilated by both extraction functionals, and d₁ comes from the
Airy simple-pole residue (Plan 65, E_pgt1.md; REVIEWED 2026-10-15 (REVIEW_Plan65_A.md, REVIEW_Plan65_B.md)).

**p ≤ 1.** p = 1: done (E_p1.md, Plan 66); 0 < p < 1: RH_plt1b's seam geometry. The same
steps apply, but (i) Stirling holds only in |ph t| ≤ π − δ, so the seam scalar's rate must be re-checked; (ii) the
numerics (§1) show remainders n^{−1−p}, so for p < 1 only (E_ε) with ε ≤ p can hold, and step 3 must produce exactly that
rate. **GAP.** *Plan 67 (Plan 67, E_plt1.md; not REVIEWED):* closed for 0 < p < 1 (E_plt1.md): the seam scalar's rate is O(n^{−p}) with an explicit
leading term (Lemma F.1), and (E_ε) holds with exactly ε = p.

### 4.1 A heuristic for g(p) = 0: hard edge + lattice offset (HEURISTIC; NUMERICAL test)

Write the conjecture as b_n ≈ c(p)·n_eff^{−p} with n_eff = n + α_x/2 + (j₀ − ½), where j₀ = 1 is the index of the first
node (x = j^{−p}, j ∈ j₀ + ℕ₀). The two shifts have separate sources:
- **hard edge**: α_x/2, as for Laguerre (b_n² = n(n + α) ⇒ shift α/2) and Meixner; this is the s-dependent part, and §3.3
  explains its slope;
- **lattice offset**: j₀ − ½, the Euler–Maclaurin midpoint offset of the node count #{j ≥ j₀ : j^{−p} > x} ≈
  x^{−1/p} − (j₀ − ½). Removing the top node (j₀ ↦ j₀ + 1) should make b_n(reduced) ≈ b_{n+1}(full), a shift of −p in d₁
  (the top node carries one pinned zero).
Then d₁ = −p(α_x/2 + j₀ − ½) = −(s − 1)/2 at j₀ = 1, i.e. g(p) = 0 is the statement that the lattice offset is exactly ½.
Support at p = 1: Tricomi–Carlitz(α) (atoms 1/(k + α), k ≥ 0, so j₀ = α; masses: not checked here — the repo
records them only for α = 1 (RH_p1 §1); that they are ∝ (k + α)^{−3/2}(1 + O(1/k)) is an unverified assumption on which
the comparison rests) has γ_N² = N/((N + α)(N + α − 1)) (toolkit `measures.reference.tc_coeffs`), whence d₁ = (½ + 1 − 2α)/2 = ¾ − α, which is
−p(α_x/2 + j₀ − ½) with p = 1, α_x = −½, j₀ = α — for every α > 0, not only integers. Only this chain computation is
exact; with the masses verified, Prop 3.5 (adapted to the shifted nodes) would make it a proved comparison. NUMERICAL test on shifted lattices
(nodes (k + δ)^{−p}, weights (k + δ)^{−s}, j₀ = 1 + δ; prediction d₁ = −(s − 1)/2 − pδ, e₁ unchanged):
`checks/check_so_lattice.out`. None of this is a proof; it locates what a proof of g(p) = 0 has to capture (the top of the
node set, i.e. the saturated region and its first node).

**Paper 2's engine** (Conway–Deift comparison at the hard edge, for general slowly varying factors) has a lip mismatch
that is "o(1) in the supremum norm but has no rate" (Paper 2 §1, "The hard edge"); it cannot give a second order. For pure
powers it is not needed: the weight is exactly x^{α_x} at the hard edge (RH_px Lemma 1.2) and the standard Bessel
parametrix applies.

**Soft routes tried.**
- Hankel determinants (Goal 2, last option): log D_n = Σ_{k<n}log h_k. A 1/n term in log b_n corresponds to a
  (d₁)·log n term in log h_n, i.e. an n log n term in log D_n beyond Theorem H's leading order. Paper 1's method gives the
  averaged law (o(n²)-level information on log D_n), not an O(log n)-accurate expansion of log h_n. Not available.
- Christoffel shift + averaged law (§3.1): gives the s ↦ s + p constraint exactly (Theorem 3.2), but no single value.
- s-derivative (§3.3): gives the slope in s (UL.md UF-lim; unconditional), but not the s-independent part g(p).
- The limit s → 1⁺: σ_{p,s}/ζ(s) → δ_0, and b_n(s) → b_{n−1}(σ_{p,1+2p}) shifted (the OPs of "∞·δ_0 + σ_{p,1}" are
  x·π_{n−1}^{x²σ_{p,1}}); this reproduces Cor 3.3 twice and gives no new constraint.

## 5. Rule A (adversarial pass) — log

- Prop 3.1: tested on finite measures (identity exact while n < number of atoms − 1) and numerically on independently
  computed σ_{p,s}, σ_{p,s+p} (check [A]: discrepancy ≤ 6·10⁻¹² at n ≤ 1600, the data precision).
- Theorem 3.2: the limit constant uses g_0 = ζ(s + p)/ζ(s) (first moment ratio), not a fitted value; check [B] tests it.
  An atom at 0 would not break anything: with infinite support in [0, ∞) the zeros of P_n lie in the open convex hull,
  so P_n(0) ≠ 0 still; the atom changes g₀ = α₀ only through the moments.
- Cor 3.3: needs (E) at **both** s and s + p; with (E) at one point only, Theorem 3.2 gives (E) at the other only in
  Cesàro form. Tested: d₁ differences in check [C].
- Theorem 3.4: ε > ½ is needed for (X − 1)² = o(1/n); at p = ½ the numerics give ε = ½ (n^{−3/2} terms), the borderline:
  then Theorem 3.4 gives only α_n/(2b_n) = 1 − p/(2n) + O(1/n), i.e. nothing. The numerics for e₁ at p = ½ show no
  n^{−3/2} term in α_n/(2b_n) (§1.1), consistent with cancellation in ½(X + 1/X) beyond what the proof uses.
  *Plan 67 (Plan 67, E_plt1.md; not REVIEWED):* explained — b_n and α_n carry the same relative n^{−1−p} correction κ_pn^{−1−p} (E_plt1 Thm E′.1).
- Prop 3.5: the head bound needs v_k ≥ c₁k^{−A}; for super-polynomially decaying weights it can fail (not used).
  "|log(w/v)| ≤ C/k" cannot be weakened to "→ 0" without losing the O(1/n) (a slowly varying factor gives the tilt).
- Cor 3.6: the constant √(2π) in k^{−3/2} = √(2π)H(k)v_k matters only for the limit constant, not for d₁.
- Prop 3.7: real-analyticity uses positivity of the Hankel determinants (infinite support). Termwise differentiation
  checked.
- Theorem 3.8: the converse (pointwise slope from Cesàro slope) is false in general; only Cor 3.9 under (E) is claimed.
- Conjecture P62 vs exact data: p = 2 even s (Theorem 2.3) — agrees, including k₀, k₁. Possible counterexample regime:
  p → 0 (the n^{−1−p} terms dominate for n ≤ 1600 and the d₁ estimate degrades: at p = ½ the fit spread is up to 1.3·10⁻⁴); not tested below ½.

## 6. Checks

- `checks/so_coeffs.py`, `checks/so_fit.py` — helpers (coefficients with Gauss–Jacobi tail; fits).
- `checks/check_so_grid.py` (.out) — Goal 1 table (NUMERICAL).
- `checks/check_so_exact_p2.py` (.out) — Theorem 2.3 (exact), incl. the Lommel base-chain check and the d₂ assert.
- `checks/check_so_validate.py` (.out) — §1 validation against Lommel (NUMERICAL).
- `checks/check_so_shift.py` (.out) — Prop 3.1, Thm 3.2, Cor 3.3, Cor 3.6(i) numerically.
- `checks/check_so_convex.py` (.out) — (CVX), exact small n and grid data (NUMERICAL).
- `checks/check_ul.py` (.out) — UL.md (Plan 64): Lemma V, Prop SV, Remark CVX-fin, Thms UF/UF-lim/UP (NUMERICAL).
- `checks/check_so_lattice.py` (.out) — §4.1 shifted lattices (NUMERICAL).
- `checks/check_e_sym.py`, `check_e_num.py`, `check_e_flat.py`, `check_e_rate.py`, `check_e_grid.py` (.out) — E_pgt1.md (Plan 65).
- `checks/check_e_plt1_sym.py`, `check_e_plt1_flat.py`, `check_e_plt1_num.py` (.out) — E_plt1.md (Plan 67).
- `checks/check_e1_exact.py`, `check_e1_tc.py`, `check_e1_rate.py`, `check_e1_models.py` (.out) — E_p1.md (Plan 66).

Run with `PYTHONPATH=src` and the repo `.venv`; the grid caches coefficients in `tmp/plan62_cache/` (gitignored).
