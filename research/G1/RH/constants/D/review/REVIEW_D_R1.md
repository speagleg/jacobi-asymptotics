# REVIEW_D_R1 — Rule R referee pass on constants/D/D.md

Reviewer: independent second agent (Rule R), 2026-11-06. Read: VERIFICATION_POLICY.md; D/D.md; C/C.md §0; E2_pgt1.md (Thm E2.1);
E3.md (Thms E3.1, E3.2); spectral/JZC_M4_proof.md §1 (Thm N.6 and its bookkeeping); JZC_M4.md §5 (f₄); CG/CG.md §0 (Thm A, Thm C);
JZC_SIGMA.md (header: weight ≥ 3 layers open); Monien arXiv:0901.1883v1 pp. 1–2 (PDF fetched and read by the reviewer).
No existing file edited, nothing committed. The reviewer did **not** run or read the author's scripts in D/checks; all checks below
are the reviewer's own code (no cglib) in `review/checks/`:

| script → output | what |
|---|---|
| `e2_indep.py` → `e2_indep.out` | sympy re-derivation of F7 step (4)–(5) for p > 1 (g₂, D's coefficients, e₂, N⁻³ coefficient) |
| `hank.py` | LDLᵀ of the Hankel matrix (ζ(s + pk)) in mpmath: pivots h_k, P_k(0) from L⁻¹, λ_m = 1/Σ_{k<m}P_k(0)²/h_k |
| `checkA_e2.py` → `checkA_e2.out` | e₂ at (p, s) = (3, 5/2); F7 centring at (0.7, 2) |
| `checkA2_plow.py` → `checkA2_plow.out` | precision confirmation at p = 0.7; exploratory p = 0.4 (see F1) |
| `checkR_rate.py` → `checkR_rate.out` | Proposition R at (3, 5/2) and (0.7, 2) |
| `checkB_Pi2.py` → `checkB_Pi2.out` | Π₂ at the new s = 3.3 (ζ = 1.15), FE directly at (2, 3.3)→(2, 5.3), control s = 2 |
| `checkC_monien.py` → `checkC_monien.out` | A⁽⁰⁾ by a direct fit of det ζ(i+j), n ≤ 70; H₁₀₀⁽⁰⁾ from both candidate constants |
| `checkC2_bridge.py` → `checkC2_bridge.out` | the Barnes bridge lim(A_n − MZ_n) of §3.4 and K(1,2) + bridge = log A⁽⁰⁾ |
| `checkD_H1.py` → `checkD_H1.out` | Monien's second printed value H₁₀₀⁽¹⁾ from both candidates |

All mpmath runs were repeated at two precisions (dps given in the outputs) with identical printed digits, except where noted.
These are NUMERICAL (Rule N), not CERTIFIED.

## Verdicts

| Claim | Verdict |
|---|---|
| R (Proposition R) | **ACCEPT** (nits F6) |
| F7 | **ACCEPT WITH FIXES** (F1 rate over-claimed for 1/3 < p < 1/2; F4 sign typo; F7 GAP wording) |
| FE (+ Barnes solution) | **ACCEPT WITH FIXES** (F3: p = 1/2 is outside the range where K is defined; F2: the hypothesis p > 1/3 is not needed — optional strengthening) |
| Kp (Π constant in s) | **ACCEPT as NUMERICAL** (new s = 3.3 at p = 2 confirms to 3·10⁻⁴³, see §3(b)) |
| K1, K2 | **ACCEPT** with the stated labels (K2 at s ∈ 2 + 2ℕ PROVED-mod-cite rests on FE at p = 2, which is unaffected by F1–F3) |
| MZ (A⁽⁰⁾ closed form) | **ACCEPT as CONJECTURE** (independently confirmed to 4·10⁻⁴⁵) |
| Monien misprint remark | **ACCEPT** (confirmed from the PDF and by a second printed value, F8) |

No error was found that changes a stated value. The findings are one over-claimed error term (F1), one range slip (F3), one sign typo
(F4), definitional/expository points (F5–F7), and one possible strengthening (F2).

## 1. Re-derivations (from the write-up alone)

### Proposition R
h_n = h₀Π_{j≤n}b_j² and log H_n = log(2π/p) + (2n+1)log c + ζ log c − (s−1)log n − 2p log n!, so
log(h_n/H_n) = 2[S_n − d₁ log n] + const with S_n = Σ_{j≤n}f_j, f_j = log(j^pb_j/c), d₁ = −(s−1)/2; Theorem C (all p > 0) fixes the
constant so that the limit is 0. Writing S_n = d₁H_n + T − Σ_{j>n}(f_j − d₁/j) gives
log(h_n/H_n) = 2[d₁(H_n − log n − γ) − Σ_{j>n}(f_j − d₁/j)]. With log(1+x) = x − x²/2 + O(x³) applied to E3.1/E3.2,
f_j − d₁/j = (d₂ − d₁²/2)j⁻² + Σ_kε_kj^{−1−kp} + (cross terms) + r_j; the tails give d₁/(2n) − (d₂ − d₁²/2)/n − Σε_kn^{−kp}/(kp), hence
**e = d₁ + d₁² − 2d₂** and the ε-terms as stated. I re-did the simplification: e = −(s−1)/2 − (s−1)²/(4p) + (p+2)(s−1−p)²/(4p²) − (p+1)/6,
and e(2, s) = (s² − 14s + 17)/8 (e(2,2) = −7/8 ✓).
Error terms. p > 1: E3.1 remainder O(j⁻³) → O(n⁻²); the cross term d₁ε₁j^{−2−p} → O(n^{−1−p}); ε₁²j^{−2−2p} → O(n^{−1−2p});
Euler–Maclaurin corrections of the ε₁ tail O(n^{−1−p}); after exponentiation x² = O(n⁻² + n^{−2p}); all ⊂ O(n⁻²) for p > 1 ✓.
p < 1, 1/p ∉ ℕ: E3.2 remainder O(j^{−2−p} + j^{−ν_K}) sums to O(n^{−1−p} + n^{−(K+1)p}); cross terms d₁ε_kj^{−2−kp} → O(n^{−1−kp}) ⊂ O(n^{−1−p}),
ε_iε_kj^{−2−(i+k)p} → o(n^{−1−p}); the j⁻²-tails' second terms O(n⁻²) ⊂ O(n^{−1−p}) ✓; and (K+1)p > 1 so e/n is not swamped ✓.
The exclusion 1/p ∈ ℕ is right: there ε_K j^{−1−Kp} = ε_K j⁻² merges with d₂ (E2 Remark E2.10 / E3) and −2ε_K n^{−Kp}/(Kp) is a 1/n term.
Numerical (own pivots, `checkR_rate.out`): (3, 5/2): fitted 1/n coefficient −1.29166666667 = e = −31/24; (0.7, 2): fitted n^{−p}
coefficient 0.26266053 vs −2ε₁/p = 0.26266025 and 1/n coefficient −1.016507 vs e = −1.016497 ✓.

### F7
(1) λ_m = D_m(σ)/D_{m−1}(x²σ), x²σ_{p,s} = σ_{p,s+2p}, so λ_{m+1}/λ_m = h_m(σ)/h_{m−1}(σ′) ✓. Natural index of σ′:
N′_n = n + (s + 2p − 1)/(2p) = n + 1 + (s−1)/(2p) = N_{n+1} ✓; Bessel order α′ = (s+2p−1)/p − 1 = α + 2 ✓.
(2) N.6 (JZC_M4_proof §1) uses α = (s−1)/p − 1 and N = n + α/2 + ½ = n + (s−1)/(2p): the same N ✓. N.6(ii) does give α-free leading
constants ε_j (all j ≥ 1) and (3p+1)/(2p)ε₁² for μ₁², with no N⁻¹ bracket term; ε_j is s-independent (E3) ✓. For |β| ≥ 2 other than 2e₁,
N.6 only gives 𝔇_β = O(n⁻²) (and JZC_SIGMA Cor Σ.2 stops at weight 2) ✓.
(3) Telescoping: log λ_{m+1} − log λ_m = const + 2Σ_{j≤m}G_j with G_j := log b_j(σ) − log b_{j−1}(σ′) = G(N_j) + O(N_j^{−K′}), and the
constant is forced by Theorem A (CG §0: p ≠ 1, every s > 1, applied at s and s + 2p) to make the step tend to 0 ✓. Legitimate use: Theorem A
is a REVIEWED input, used only for the limit and for C, not for any rate. No uniformity in s is needed (two fixed measures) ✓.
(4) g₂ = f₂(α) − f₂(α+2) = (p+2)(α+1)/2 = E/2 ✓ (sympy, `e2_indep.out`). The integer layer is even in N, so G has no N⁻³ ✓.
First-order zeta layers: leading terms cancel; remainder O(N^{−3−jp}) from (g_j(α) − g_j(α+2)) and the f₂ε_j cross term ✓.
**But see F1** for the weight-3 second-order (and third-order) layers.
(5) ψ′(N+1) = 1/N − 1/(2N²) + 1/(6N³) − … ✓; D = O(N⁻³ + N^{−2−p}) and the second summation gives O(N⁻² + N^{−1−p}) ✓ (for the layers
covered). Note the **double** summation: a term N^{−a} in G contributes N^{2−a} to log λ_m − log C + E log N_m.
e₂, p > 1: my own sympy derivation (`e2_indep.py`, Hurwitz/Euler–Maclaurin tails, f₄ from JZC_M4 §5) gives
D = d₃N⁻³ + d₄N⁻⁴ + …, d₃ = −E[(2p+1)(p+2)ζ² + p² − p − 1]/(12(3p+2)), d₄ = −(3/2)d₃, final N⁻¹ coefficient 0, N⁻² coefficient
**e₂ = E[(2p+1)(p+2)ζ² + p² − p − 1]/(24(3p+2))** (difference from the claim: 0, symbolically), N⁻³ coefficient 0 ✓. e₂(2,2) = 1/16,
e₂(2,3) = 7/16, e₂(3, 5/2) = 25/192, e₂(5/2, 4) = 37467/38000. (The sign of "d₃/2 = e₂" in the note is wrong: F4.)
The error O(N^{−min(4,1+p)}) for p > 1 ✓ (zeta first-order: N^{−3−p} → N^{−1−p}; second-order O(N^{−2−2p}) → N^{−2p} ⊂ N^{−1−p}; integer N⁻⁶ → N⁻⁴).

### FE
(i) xσ_{p,s} = σ_{p,s+p}; expanding the moment determinant of P_n along its last row (1, 0, …, 0) gives P_n(0) = (−1)ⁿD_n(xσ)/D_n(σ)
(sign (−1)^{n+2}) ✓, so |P_n(0)| = D_n(s+p)/D_n(s) > 0 ✓. (ii) 1/λ_m = K_m(0,0) = Σ_{k<m}P_k(0)²/h_k, so P_m(0)²/h_m = 1/λ_{m+1} − 1/λ_m ✓.
With F7, 1/λ_{m+1} − 1/λ_m = C⁻¹E N^{E−1}(1 + o(1)) ✓. I redid the bookkeeping by hand: the log Γ(n) terms match (−p log Γ(n+1) =
−p log Γ(n) − p log n), the n log c terms match, the log n coefficient on the right is ½[−(s−1) − 2p + E − 1] = ζ − p − ½, and
e(ζ+1) − e(ζ) = ζ − p − ½ identically (with s − 1 = pζ) ✓. The constant: ½log(2π/p) + ½(ζ+1)log c + log c + ½log E − ½log C, which with
log C = log Γ(ζ) + log Γ(ζ+1) + ζ log c + 2ζ log(p+2) − log p and log Γ(ζ+1) = log ζ + log Γ(ζ) is
**½log(2π(p+2)) + (3/2)log c − ζ log(p+2) − log Γ(ζ)** ✓. The Barnes solution satisfies it (G(ζ+1) = Γ(ζ)G(ζ);
½[(ζ+1)ζ − ζ(ζ−1)] = ζ) ✓; the general solution is that plus a 1-periodic function of ζ ✓. A_n of §3.1 = Σ_{k=1}^{n−1}log H_k + e log n + L_n
(Σ_{k=1}^{n−1}(2k+1) = n² − 1; Σ_{k<n}log k! = log G(n+1)) ✓.

### §3.4 bridge
`checkC2_bridge.out`: A_n(1,2) − MZ_n − [(3/4)log 2 − (3/2)log π − 2ζ′(−1)] = −4.17·10⁻⁵, −4.17·10⁻⁶, −4.17·10⁻⁷ at n = 10³, 10⁴, 10⁵ (→ 0 like 1/n) ✓,
and K(1,2) (from the Π(1) closed form and the Barnes form) + bridge − log(e^{1/12}2^{1/6}3^{1/8}A⁻³) = −5·10⁻⁴¹ ✓.

## 2. Findings

**F1 (moderate; F7 statement and step (4), range 1/3 < p < 1/2).** Step (4) correctly notes that weight-w ≥ 3 layers of order ≥ 2
(μ₁μ₂, and also the third-order μ₁³, both only O(n⁻²)·μ^β by N.6(i)) have unknown α-dependence, so their difference between σ and σ′ is
O(N^{−2−3p}) in G with no cancellation. The display "G = (E/2)N⁻² + g₄N⁻⁴ + O(N^{−3−p} + N⁻⁶)" drops this term. After the two summations it
contributes O(N^{−3p}) to log λ_m − log C + E log N_m, and 3p < 1 + p for p < 1/2. So the proof gives
λ_m = C N^{−E}(1 + O(N⁻² + N^{−1−p} + N^{−3p})): the stated O(N⁻² + N^{−1−p}) is proved for 1/2 ≤ p < 1 and p > 1, but for 1/3 < p < 1/2 only
O(N^{−3p}) = o(N⁻¹) is proved. (p > 1/3 is exactly the condition for o(1/N), which is what FE uses, so FE is unaffected.)
Fix: add N^{−3p} to the error in the F7 statement (or state the rate for p ≥ 1/2 and o(N⁻¹) for 1/3 < p < 1/2), add O(N^{−2−3p}) to the
G display, and rewrite GAP F7-small as "α-independence of the leading constants of the layers μ^β, |β| ≥ 2, of weight w with
wp < 1 + p (other than μ₁²)", which also names the third-order layers. Numerics cannot settle it at n ≤ 70: at p = 0.4 the local exponent of
the residual is 1.49 (s = 2) and 1.64 (s = 3) at m = 70 and still decreasing (`checkA2_plow.out`), consistent with either 1.2 or 1.4.

**F2 (minor, strengthening; FE range and §4 item 4).** FE does not need F7's rate, only the *step*:
1/λ_{m+1} − 1/λ_m = (1/λ_m)(λ_m/λ_{m+1} − 1) and λ_m/λ_{m+1} = exp(E log(1 + 1/N) − D(N)), so FE needs Theorem A plus D = o(1/N). With
D = −2Σ_{j>m}G_j + E log(1 + 1/N), it suffices that G − (E/2)N⁻² = O(N^{−2−δ}). That holds for **every** p > 0, p ≠ 1: first-order layers
cancel at leading order (α-free ε_j, N.6(ii)), leaving O(N^{−3−jp}); every layer of order ≥ 2 is O(N^{−2−2p}) whether or not it is α-free.
So D = O(N⁻² + N^{−1−2p}) = o(1/N), and FE is PROVED-mod-cite (R, N.6, Thm A, Thm C) wherever K is defined: p > 1, and 0 < p < 1 with
1/p ∉ ℕ. §4 item 4 ("needs the o(1/m) form F7") is too pessimistic. The author should re-check this argument before relabelling.

**F3 (minor; FE label range).** The FE row says "p > 1/3, p ≠ 1", which includes p = 1/2, but §3.1 defines K through Proposition R, which
excludes 1/p ∈ ℕ. Either exclude p = 1/2 or write R at p = 1/K (there −2ε_K n^{−Kp}/(Kp) and the tail of ε_Kj⁻² both land on 1/n; since
ε_K is s-independent this shifts e by an s-independent constant, so the log n cancellation and FE are unchanged — but E3's merged
n⁻² coefficient at p = 1/K must be quoted, Rule C).

**F4 (minor; sign typo, F7 step (5)).** "the N⁻² coefficient is d₃/2 = e₂" should read −d₃/2 = e₂, since
log λ_m − log C + E log N_m = −Σ_{k≥m}D(N_k) and Σ_{k≥0}(N+k)⁻³ = 1/(2N²) + …. With D as defined, d₃ = −2e₂ < 0 (`e2_indep.out`). The
N⁻³ statement (d₃/2 + d₄/3 = 0) is sign-independent and correct.

**F5 (minor; §3.1 definition of K).** "L_n … for 1 < p < 2 (for p ≥ 2 the ζ(−p) terms are summable …)": Σk^{−p} converges for every p > 1,
so L_n is a convergence accelerator, not a necessity. Including it for 1 < p < 2 and not for p ≥ 2 shifts K by the constant
(2ε₁/p)ζ(p) on one side of p = 2, i.e. K(p,s) is defined by two conventions. FE is unaffected (ε₁ is s-independent) and no recorded Π
(p ∈ {1,2,3,4}) is affected, but a closed form for Π(p), 1 < p < 2, would depend on the convention. Fix: define K without L_n for all
p > 1 and use L_n only in the extrapolation, or state the convention explicitly in the table.

**F6 (nit; Proposition R proof).** The letter j is used both as the summation index of f_j and as the layer index in Σ_jε_jj^{−1−jp};
"S_∞-form" and "correction absorbed in κ" are undefined — write S_n = d₁H_n + T − Σ_{j>n}(f_j − d₁/j), κ = T + d₁γ explicitly. The p < 1
remainder should also list the x³ terms of log(1+x) and the Euler–Maclaurin corrections (all inside the stated error). In the table
"o(1/n)" for R is fine for p ≠ 1, 1/p ∉ ℕ only — say so.

**F7 (nit; labels).** F7's table row (p > 1/3) should carry F1's rate qualification. The "PROVED-mod-cite (Thm A; Thm N.6)" input list is
complete: no other place in F7's proof uses p ≠ 1 (Theorem A covers p ≠ 1; CG Theorem C would cover p = 1, so GAP F7-one is exactly
N.6's exclusion, as stated). Resonant p = 1/j (e.g. p = 1/2) is not a problem for F7: N.6(ii) is stated as layer identities for every p.

**F8 (confirmation; §3.4 Monien).** I fetched arXiv:0901.1883v1 and read pp. 1–2: it prints H₁₀₀⁽⁰⁾ ≈ 4.9·10⁻¹⁶⁶⁸⁴, H₁₀₀⁽¹⁾ ≈ 4.3·10⁻¹⁶⁸⁷¹,
the x⁴ coefficient −12319/259200, A⁽⁰⁾ ≈ 0.351466738331 and A⁽¹⁾ = (e^{9/8}/√6)A⁽⁰⁾ — as the note says. From the asymptotic forms:
H₁₀₀⁽⁰⁾ = 4.8999·10⁻¹⁶⁶⁸⁴ (closed form) vs 2.5952·10⁻¹⁶⁶⁸⁴ (printed A⁽⁰⁾); H₁₀₀⁽¹⁾ = 4.261·10⁻¹⁶⁸⁷¹ vs 2.257·10⁻¹⁶⁸⁷¹. So *both* of Monien's
own printed determinant values contradict his printed A⁽⁰⁾ and agree with the closed form; worth adding H₁₀₀⁽¹⁾ as a second witness.
My direct fit (`checkC_monien.out`, own LDL, n ≤ 60/70, dps 500/700/900, 24–32 terms in x = 1/(2n+1)) gives
A⁽⁰⁾ = 0.66359780287358568799213037467200037, closed form − fit = 5·10⁻³⁸, −4·10⁻⁴², 4·10⁻⁴⁵; log-series c₁, c₃ ≤ 10⁻²⁸; c₂ = 1/24;
c₄ = −0.00302469135802, i.e. a₄ = c₄ + a₂²/2 = −559/259200 (not −12319/259200) ✓. The ratio closed/printed = 1.88808137585 (not identified).
The note's cautious wording ("discrepancy to report", later versions unchecked) is appropriate.

## 3. Independent numerics (summary)

(a) **e₂ at (3, 5/2)** (`checkA_e2.out`, own λ_m, n ≤ 44, dps 500 and 700 identical): N²(λN^E/C − 1) = 0.13018, …, 0.130203 at m = 20…44;
the fit with exponents {2, 4, 5, …} gives e₂ = 0.130208333333333 = 25/192; with N⁻³ free, e₃ = 1.1·10⁻¹² ✓.
**F7 centring at p = 0.7, s = 2** (n ≤ 70, dps 250 and 350 identical; dps 150 breaks down for m ≥ 60): λN^E/C − 1 = 4.6·10⁻⁴ at m = 70,
N^{1.7}·residual = 0.755, 0.704, …, 0.641 (bounded, consistent with O(N^{−1−p})), while m·(λm^E/C − 1) → −2.66 (the uncentred error is
O(1/m)) ✓.
(b) **Π₂ at s = 3.3** (ζ = 1.15, a value not used in the note; `checkB_Pi2.out`, own LDL, A_n of §3.1, exact linear solve in
powers of 1/n on the last 20/24/28 points, n ≤ 60/70/70, dps 700/900/1100): K(2, 3.3) = 0.15300009205863578769327, Π₂ = −0.70112294215566899568052,
Π₂ − closed form = −2.5·10⁻³³, −2.7·10⁻³⁹, −2.6·10⁻⁴³ ✓ (control s = 2: −1.6·10⁻³³). FE directly (no Barnes form):
K(2, 5.3) − K(2, 3.3) − RHS = 6·10⁻³⁴ ✓. This also extends the PSLQ evidence for the Π(2) closed form to 42 digits at a non-Krattenthaler s.
(c) **A⁽⁰⁾**: confirmed to 4·10⁻⁴⁵ (F8).
(d) **Monien's H₁₀₀**: F8.

## 4. Rule A log (reviewer)
- Tried p → 1/K in R (exclusion justified), p = 1/2 in FE (F3), 1/3 < p < 1/2 in F7 (F1), p ≥ 2 vs 1 < p < 2 in K (F5).
- Checked "the cross term vanishes"-type claims: N⁻³ coefficient of F7 for p > 1 (symbolically 0); log n cancellation in FE (identity);
  κ = 0 in F7 (forced by Theorem A, legitimate).
- Checked whether N.6's error terms suffice: yes, with B, J chosen large; the only missing ingredient is F1's α-dependence of weight-≥ 3
  layers of order ≥ 2, which affects only F7's rate for p < 1/2.
- Rule X: e₂ was derived symbolically here without the author's script; the numerical e₂ fit at (3, 5/2) is a new point not used in the
  note. The A⁽⁰⁾ fit uses only det ζ(i+j) and Monien's normalisation.
