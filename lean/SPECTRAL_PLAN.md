# Plan L1 — formalizing the spectral-dictionary work (Paper IV, research/G1/RH/spectral) in Lean

Goal (2026-11-05): formalize everything in the Paper IV / G1 spectral work that is within reach of Lean 4.34.1 + Mathlib v4.34.1
without formalizing Riemann–Hilbert steepest descent or logarithmic potential theory. Existing modules are not modified; every
statement is in a new module, sorry-free, and audited by `check.sh` (axioms `propext`, `Classical.choice`, `Quot.sound` only).

## 1. What is formalized

| Module | Source statement | Lean | Coverage |
|---|---|---|---|
| `NaturalIndex` | Paper IV Thm A (integer layer, natural index N = n + α/2 + ½) vs E2 Thm E2.1 | `naturalForm_iff_E21`, `natural_expansion`, `natShift_sq_add_f2`, `neg_mul_natShift`, `d2_two`, `d2_closed` | Full equivalence of the two forms to O(n⁻³) for any sequence. It is the statement of both forms only where the zeta layers and E2.1's remainder are O(n⁻³), i.e. p ≥ 2; for other p it is a statement about the integer layer. The analytic content (that b_n has either form) is not formalized. |
| `PathCounts` | JZC_SHIFT Lemma R; Paper IV Q_k(4c) | `pathH_two_mul`, `pathG_two_mul`, `deriv_pathG_two_mul`, `freeJacobi_pow_coeff_zero/one`, `tiltQ_four_mul`, `resW_succ` | Full. H_j, G_j are also identified with the diagonal / first off-diagonal entries of (a + bT + bT⁻¹)^j. The derivative identity is the one-variable (∂_b on the line a = 2b) form of the note's ∂_n statement. |
| `SpectralConstants` | Paper IV W(q), W(1/p) = 1; E3 Cor E3.3 resonance; Thm D pole constant; Lemma K0 | `Wq_one_div`, `Wq_nat`, `centralBinom_mul_hallC_pow_eq_one`, `theoremD_constant`, `lemmaK0_gamma`, `lemmaK0_integral` | Full for the identities. Lemma K0 carries the extra hypothesis w + ½ ∉ ℤ (Lean's Γ is 0 at its poles, so the paper's removable points cannot be stated as written). Theorem D itself (an asymptotic statement) is not formalized, only its constant. |
| `SoftEdge` | JZC_M1 condition (Q), Corollary Q.1; Paper IV "a = 4c" | `softF_integral`, `softF_eq_one_iff`, `softF_strictAntiOn`, `softF_existsUnique_root` | Full for the computation: F(a) = (4c/a)^{1/p}, unique root a = 4c(p). That this root is the edge of the constrained equilibrium measure is Theorem Q, not formalized. |
| `Uvarov` | SPEC §3.2 Lemma U | `det_momHankel_add_atom`, `log_jb2_sub`, `hankel_det_add_atom`, `logDetDiff_add_atom`, `hankelQuad_eq_kernel`, `logDetDiff_add_atom_kernel` | Full, including the Christoffel–Darboux identification vᵀH⁻¹v = Σ_{j<m} p_j(x₀)². Stated for the library's `DMeasure` (infinite discrete measures); the atom is added at the level of moments. Theorem S2′ (which feeds the RH expansions into Lemma U) is not formalized. |
| `TodaTilt` | JZC_TODA Lemma T.1 (finite support M, one time t, tilt e^{tx^j}; multi-time follows by Remark (b)) | `hasDerivAt_th`, `hasDerivAt_log_th`, `hasDerivAt_log_tb2`, `tpi_deriv_expansion`, `tpi_recurrence`, `toda_log_b2`, `toda_a` | Items (1)–(3) for every j; item (4) for j = 1 only (the Toda lattice); n ≥ 1. π_n is defined by Cramer's rule from the Hankel matrix; (J^j)_{nn} is defined as ∫x^jπ_n²dμ_t/h_n (its identification with the matrix entry is not proved); (1) and the recurrence hold at the atoms (in L²(μ_t)). Not covered: item (4) for j ≥ 2, real-analyticity, infinite or compactly supported measures. |

## 2. What is not formalized, and why

| Result | Label in the notes | Reason |
|---|---|---|
| E_pgt1, E_plt1, E_p1, E2, E3 (the 1/n, n⁻², n^{−1−jp} coefficients) | PROVED-mod-cite + REVIEWED | Rest on the Riemann–Hilbert analysis of Paper II (steepest descent, local Bessel/Airy parametrices, small-norm estimates). Mathlib has none of this infrastructure. |
| Thm N.6, Σ, H [JZC], T.A, T.B, Thm T, T_H, SH, DR, the κ-family | PROVED-mod-cite + REVIEWED | Same RH chain (via Lemma T.A's transfer); the exact-algebra parts are computer-algebra outputs of an engine, not short identities. |
| Theorem Q (constrained equilibrium) | PROVED + REVIEWED | Logarithmic potential theory with an unbounded constraint (balayage, Plemelj boundary values, energy uniqueness). Paper I Lemma 3.3 (`energy_pos`) exists here, but the rest is a large project. The computational corollary is `SoftEdge`. |
| Thm K / K′ (Mellin–Barnes form of e_n) | PROVED-mod-cite, NOT REVIEWED | Needs Mellin inversion and contour shifting for a meromorphic kernel; Mathlib's Mellin inversion is not at that level. Lemma K0's closed form is in `SpectralConstants`. |
| Theorem 5.1(iii) (separation of layers) | PROVED | Uses irrationality / linear independence arguments about ζ(−jp) values not in Mathlib. |
| Conjecture W, W′, W_<1, the numerical tables | CONJECTURE / NUMERICAL | Not theorems. |
| JZC_W_plt1 Prop 2 (κ < 0) | GAP | Open on paper. |
