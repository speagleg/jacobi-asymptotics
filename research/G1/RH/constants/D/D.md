# D — the constant of log D_n, the rate of Theorem C, and the N-centring of the CG constant

Lead session, 2026-11-06, branch `master` (uncommitted until reviewed). Checks in `checks/` and the files named below.
Labels per VERIFICATION_POLICY.md. **Rule R: one reader (R1, review/REVIEW_D_R1.md, a subagent of the same session); verdicts R ACCEPT,
F7 and FE ACCEPT WITH FIXES, Kp/K1/K2/MZ ACCEPT with the labels below; fixes F1–F8 applied 2026-11-06 (§5).** Novelty: Rule L not done for §§1–2;
§3.4 is checked against the one source that states the p = 1 constant (Monien, arXiv:0901.1883v1).

| # | Statement | Label |
|---|---|---|
| R | rate of Theorem C: log(h_n/H_n) = e/n − 2Σ_j ε_j n^{−jp}/(jp) + o(1/n), e = d₁ + d₁² − 2d₂ (p > 1; 0 < p < 1, 1/p ∉ ℕ) | PROVED-mod-cite (Thm C; E2.1, E3.1) + REVIEWED (R1, 1 reader); NUMERICAL check |
| F7 | λ_m(0; σ_{p,s}) = C N^{−E}(1 + O(N^{−2} + N^{−1−p} + N^{−3p})), N = m + (s−1)/(2p); for p > 1: 1 + e₂N^{−2} + O(N^{−min(4,1+p)}), e₂ explicit, no N^{−3} term | PROVED-mod-cite for p > 1/3, p ≠ 1 (Thm A; Thm N.6) + REVIEWED (R1, 1 reader); GAP for p ≤ 1/3 and p = 1; NUMERICAL check |
| FE | K(p, s + p) − K(p, s) = ½log(2π(p+2)) + (3/2)log c − ζ log(p+2) − log Γ(ζ) | PROVED-mod-cite for p > 1 and for 0 < p < 1 with 1/p ∉ ℕ (Thm A, Thm C, R; E2.1, E3.1; not F7) + REVIEWED (R1, 1 reader; range widened per R1 F2); NUMERICAL for p = 1 |
| Kp | the 1-periodic part Π(p) of K is constant in s | NUMERICAL (p = 1: three s, p = 2: five s, p = 3, 4: two s each; 19–22 digits) |
| K1, K2 | closed forms of Π(1), Π(2) | p = 2, s ∈ 2 + 2ℕ: PROVED-mod-cite (Krattenthaler's product, App. A of arXiv:math/0608372, read; 45 digits); otherwise CONJECTURE (PSLQ, 19–30 digits) |
| MZ | Monien–Zagier's constant: A⁽⁰⁾ = e^{1/12}2^{1/6}3^{1/8}/A³ = 0.66359780287358568799… (A = Glaisher) | CONJECTURE, verified to 2·10⁻³⁰ by a direct fit independent of R, F7, FE |
| Π(p), p ∉ {1, 2} | closed form | OPEN; numerical values Π(3), Π(4) recorded |

Notation: σ = σ_{p,s} = Σ_k k^{−s}δ_{k^{−p}}, h_n, b_n, D_n = det(ζ(p(i+j)+s))_{0≤i,j<n} = Π_{k<n}h_k, c = c(p), ζ = (s−1)/p,
α = ζ − 1, E = (p+2)ζ, natural index N_n = n + (s−1)/(2p). H_n := (2π/p)c^{2n+1}(c^{1/p}/n)^{s−1}Γ(n+1)^{−2p} (Theorem C:
h_n = H_n(1 + o(1))). d₁ = −(s−1)/2, d₂ = (p+1)(s−1)²/(8p) − (p+2)(s−1−p)²/(8p²) + (p+1)/12 (E2.1), ε_j = C(2j,j)pc^jζ(−jp) (E3.1).

## 1. The rate of Theorem C (R)

**Proposition R.** Let p > 1, s > 1. Then
  h_n = H_n·(1 + e/n − 4cζ(−p)n^{−p} + O(n^{−2})),  e = d₁ + d₁² − 2d₂ = −(s−1)/2 − (s−1)²/(4p) + (p+2)(s−1−p)²/(4p²) − (p+1)/6.
Let 0 < p < 1 with 1/p ∉ ℕ, K = ⌊1/p⌋. Then log(h_n/H_n) = e/n − 2Σ_{j≤K}ε_jn^{−jp}/(jp) + O(n^{−1−p} + n^{−(K+1)p}).

*Proof.* h_n = h_0Π_{j≤n}b_j², so log(h_n/H_n) = 2[S_n − (S_∞-form)], S_n = Σ_{j≤n}log(j^pb_j/c), where Theorem C says
S_n = −((s−1)/2)log n + κ + o(1) with κ explicit. Write f_j = log(j^pb_j/c) = d₁/j + (d₂ − d₁²/2)/j² + Σ_jε_jj^{−1−jp} + r_j with
r_j = O(j^{−min(3,1+p)}) for p > 1 after removing the ε₁ term (E3.1: remainder O(n^{−3})), and r_j = O(j^{−2−p} + j^{−1−(K+1)p})
plus cross terms d₁ε_jj^{−2−jp}, ε_jε_kj^{−2−(j+k)p} for p < 1 (E3.1; the cross terms come from log(1 + x) − x). Then
S_n − κ + ((s−1)/2)log n = −Σ_{j>n}f_j + d₁(H_n − log n − γ) − (correction absorbed in κ) and Σ_{j>n}j^{−2} = 1/n + O(n^{−2}),
H_n − log n − γ = 1/(2n) + O(n^{−2}), Σ_{j>n}j^{−1−q} = n^{−q}/q + O(n^{−1−q}). Collecting: 2[d₁/(2n) − (d₂ − d₁²/2)/n −
Σε_jn^{−jp}/(jp)] + tails, i.e. the claim (the constant is fixed by Theorem C, so no constant term appears). For p > 1, ε₁ = 2pcζ(−p)
gives −2ε₁/p = −4cζ(−p). ∎ (The simplification of e uses d₁ = −(s−1)/2.)

At p = 2, s = 2, 4, 6, e = −7/8, −23/8, −31/8 (generally e(2, s) = (s² − 14s + 17)/8), which is what Krattenthaler's exact products
give (C/NOVELTY_C.md §2.2a: n(h_n/H_n − 1) = −0.8748, −2.8736, −3.8731 at n = 4000). Check: `../C/checks/rate_C.py` → `rate_C.out`.
At p = 1 the same computation with d₂(1, s) − 1/12 (E_p1 Thm E1.6 at s ∈ {3/2, 5/2}; CONJECTURE otherwise) gives the rate;
for general s the 1/n coefficient at p = 1 is therefore CONJECTURE. p = 1/K (resonant): see E3.1; not written out here.

## 2. N-centring of the CG constant (F7)

**Theorem F7.** Let p > 1/3, p ≠ 1, s > 1, C = Γ(ζ)Γ(ζ+1)(c(p+2)²)^ζ/p. Then
  λ_m(0; σ_{p,s}) = C·N_m^{−E}·(1 + O(N_m^{−2} + N_m^{−1−p} + N_m^{−3p})).
(The N^{−3p} term matters only for 1/3 < p < 1/2; R1 F1.)
For p > 1, λ_m = C N_m^{−E}(1 + e₂N_m^{−2} + O(N_m^{−min(4,1+p)})) with
  e₂ = E·[(2p+1)(p+2)ζ² + p² − p − 1] / (24(3p+2)),
and the N^{−3} coefficient of the integer layer is 0. (e₂(2,2) = 1/16, e₂(2,3) = 7/16: the values fitted numerically in
research/program/CONNECTIONS.md §1.1 before this derivation.)

*Proof.* (1) *Local step identity.* λ_m = D_m(σ)/D_{m−1}(x²σ) (CG.md §0) and x²σ_{p,s} = σ_{p,s+2p}, so
log λ_{m+1} − log λ_m = log h_m(σ) − log h_{m−1}(σ′), σ′ = σ_{p,s+2p}. The Bessel order of σ′ is α + 2 and its natural index is
N′_n = n + 1 + (s−1)/(2p) = N_{n+1}.
(2) *Natural forms.* Theorem N.6(i)–(ii) (JZC_M4_proof.md, PROVED-mod-cite + REVIEWED, p ≠ 1): b_n(σ) = cN_n^{−p}F_α(N_n), where
F_α(N) = 1 + f₂(α)N^{−2} + f₄(α)N^{−4} + … + Σ_jε_jN^{−1−jp}(1 + g_j(α)N^{−2} + …) + ε₁²N^{−2−2p}((3p+1)/(2p) + O(N^{−2})) + (layers
of order ≥ 2 and weight ≥ 3) + O(N^{−K}); f₂ = −(p+2)α²/8 + (p+1)/12, f₄ = JZC_M4 §5. The leading constants ε_j, ε₁²(3p+1)/(2p)
do not depend on α and the brackets have no N^{−1} term.
(3) *Telescoping.* With h_m = h_0Π_{j≤m}b_j² for both measures, the factors N^{−p} cancel between σ at j and σ′ at j − 1 (same
N), and log λ_{m+1} − log λ_m = κ − 2Σ_{j>m}G(N_j), G := log F_α − log F_{α+2}; κ = 0 because both sides tend to 0 (Theorem A).
(4) *Size of G.* Integer layer: G = g₂N^{−2} + g₄N^{−4} + O(N^{−6}) with g₂ = f₂(α) − f₂(α+2) = (p+2)(α+1)/2 = E/2. Zeta layers: the
α-free leading terms cancel in G; what is left is O(N^{−3−p}) (from g_j and the cross term f₂ε_j) and, for second-order layers of
weight w, their leading constants, which N.6(ii) gives α-free only for μ₁² (and the first-order layers). A layer of order r ≥ 2 and
weight w ≥ 3 is O(N^{−r−wp}) ⊂ O(N^{−2−3p}), with unknown α-dependence (R1 F1: μ₁μ₂, μ₁³, …). So
G = (E/2)N^{−2} + g₄N^{−4} + O(N^{−3−p} + N^{−2−3p} + N^{−6}), and the two summations below turn N^{−2−3p} into N^{−3p}, which is
o(1/N) exactly when p > 1/3.
(5) *Summation.* Σ_{j>m}N_j^{−2} = ψ′(N_m + 1) = 1/N − 1/(2N²) + 1/(6N³) + O(N^{−5}), log(1 + 1/N) = 1/N − 1/(2N²) + 1/(3N³) − …,
so the step D(N) := log λ_{m+1} − log λ_m + E log(N_{m+1}/N_m) = −2Σ_{j>m}G(N_j) + E log(1 + 1/N) is O(N^{−3} + N^{−2−p} + N^{−1−3p}). By
Theorem A, log λ_m − log C + E log N_m → 0, hence log λ_m − log C + E log N_m = −Σ_{k≥m}D(N_k) = O(N^{−2} + N^{−1−p} + N^{−3p}). For p > 1,
expanding D to N^{−4} with g₄ = [f₄ − f₂²/2](α) − [f₄ − f₂²/2](α + 2) gives D = d₃N^{−3} + d₄N^{−4} + …, d₄ = −(3/2)d₃, and
Σ_{k≥0}(N+k)^{−3} = 1/(2N²) + 1/(2N³) + …, Σ(N+k)^{−4} = 1/(3N³) + …, so the N^{−2} coefficient is d₃/2 = e₂ (d₃ of −D, see below) and the N^{−3}
coefficient −(d₃/2 + d₄/3) vanishes. (Sign convention, R1 F4: here d₃ is the N^{−3} coefficient of −D, as in the
sympy script; with D as defined above the N^{−2} coefficient is −d₃(D)/2 = e₂.) (Exact algebra: `scratchpad e2.py`, reproduced in `checks/F7_algebra.py`.) ∎

*GAP F7-small.* For 0 < p ≤ 1/3: α-independence of the leading constants of the zeta layers of order r ≥ 2 and weight w ≥ 3 with
r + wp ≤ 3 (and, for the error term N^{−3p} when 1/3 < p < 1/2, with r + wp < 3 + p; R1 F1). *GAP F7-one.* p = 1 (N.6 excludes it). Both are NUMERICAL-true (CG.md, check_F7.out).
Check: `../CG/checks/check_F7.py` → `check_F7.out`.

## 3. The constant of log D_n

### 3.1 Definition
For p ≠ 1 (and at p = 1 with the conjectural rate), by Proposition R the sum Σ_{k<n}log h_k equals an explicit expression plus a
constant plus o(1):
  log D_n(σ_{p,s}) = A_n(s) + K(p,s) + o(1),
  A_n(s) = (n−1)[log(2π/p) + ζ log c] + (n² − 1)log c − pζ log Γ(n) − 2p log G(n+1) + e log n + L_n,
G = Barnes G-function, L_n = −(2ε₁/p)Σ_{k<n}k^{−p} for 1 < p < 2; for p ≥ 2 the ζ(−p) terms are summable and absorbed in K; for
p < 1 the layer sums of Proposition R are added the same way. *Convention (R1 F5):* Σk^{−p} converges for every p > 1, so L_n could
equally be absorbed for 1 < p < 2; the two conventions differ by the constant (2ε₁/p)ζ(p). All recorded values use the convention
stated here (no value with 1 < p < 2 is recorded). K is defined for p > 1 and for 0 < p < 1 with 1/p ∉ ℕ (and at p = 1 with the
conjectural rate); not at p = 1/K (R1 F3).

### 3.2 Functional equation (FE)
Two exact identities: (i) xσ_{p,s} = σ_{p,s+p}, hence P_n(0; σ) = (−1)^nD_n(s+p)/D_n(s); (ii) P_m(0)²/h_m = 1/λ_{m+1} − 1/λ_m.
1/λ_{m+1} − 1/λ_m = (1/λ_m)(e^{−(log λ_{m+1} − log λ_m)} − 1), and log λ_{m+1} − log λ_m = −E log(1 + 1/N_m) + D(N_m) with
D = o(1/N) (R1 F2): D = −2Σ_{j>m}G(N_j) + E log(1 + 1/N) needs only G = (E/2)N^{−2} + o(N^{−2}), which E2.1 (p > 1) and E3.1
(0 < p < 1, 1/p ∉ ℕ) give after re-centring n → N (the ε_j terms are s-independent and cancel; re-centring costs O(N^{−2−jp})). With
Theorem A this gives 1/λ_{m+1} − 1/λ_m = C^{−1}E N_m^{E−1}(1 + o(1)) without F7, so with Theorem C
  log|P_n(0)| = ½[log H_n + log E − log C + (E−1)log N_n] + o(1)
and FE follows by inserting A_n: the log n terms cancel exactly when e(s+p) − e(s) = ζ − p − ½, which is an identity for the e of
Proposition R (a consistency check of R), and what is left is
  **K(p, s+p) − K(p, s) = ½log(2π(p+2)) + (3/2)log c − ζ log(p+2) − log Γ(ζ).**
Since log G(ζ+1) − log G(ζ) = log Γ(ζ), the general solution is
  K(p,s) = Π_p(ζ) − log G(ζ) − ½ζ(ζ−1)log(p+2) + κ_pζ,  κ_p = ½log(2π(p+2)) + (3/2)log c,
with Π_p 1-periodic in ζ.

### 3.3 Numerics: Π is constant (Kp)
`checks/K_numeric.py` computes log D_n from the exact moments (Chebyshev algorithm, cglib, dps 1500, n ≤ 70–80), subtracts A_n and
extrapolates (exact linear solve on the last 10 points with the exponents of the remainder; at p = 1 on even n only). Π_p(ζ):

| p | s (ζ) | Π | file |
|---|---|---|---|
| 1 | 2 (1), 2.5 (1.5), 3 (2) | 0.0277892176632482727(3), …(2), …(8) | K_p1.out |
| 2 | 2 (½), 2.5 (¾), 3 (1), 4 (3/2), 4.5 (7/4) | −0.70112294215566899568 (all five to 10⁻²⁰–10⁻²²) | K_p2_quick.out |
| 3 | 2.5 (½), 4 (1) | −1.12209725218754456180 (both) | K_p3.out |
| 4 | 2.5 (3/8), 4.5 (7/8) | −1.38879411029830148621 | K_p4.out |

The values at non-half-integer ζ (¾, 7/4, 1.5, 3/8, 7/8) rule out a periodic part that is constant only on ζ ∈ ½ℤ.

### 3.4 Closed forms at p = 1, 2 (K1, K2)
PSLQ (bases {1, log A, log 2, log 3, log π}, coefficients ≤ 144, 19–20 digits):
  **Π(1) = 1/4 − 5 log A + log π + (5/12)log 2 − (3/8)log 3,  Π(2) = 1/2 − 6 log A + (5/2)log π − (89/24)log 2**
(A = Glaisher's constant, log A = 1/12 − ζ′(−1)). `checks/K_closed.py` → `K_closed.out`: all eight numerical K(p,s) agree with
the closed form to 10⁻¹⁹–10⁻²².
- *p = 2, s = 2 from Krattenthaler's product* (`checks/K_p2_exact.py` → `K_p2_exact.out`): Π(2) from the exact D_n (n ≤ 860,
  Richardson) agrees with the closed form to 6·10⁻⁴⁵. With FE (p = 2, proved-mod-cite) this proves K(2,s) for s ∈ 2 + 2ℕ (the
  Krattenthaler class); for the other classes mod 2 (e.g. s = 3, det ζ(2(i+j)+3), the Haynes–Zudilin odd-zeta case) it is CONJECTURE.
- *p = 1, Monien–Zagier.* In Monien's normalisation H_n⁽⁰⁾ = det_{1≤i,j≤n}ζ(i+j) = A⁽⁰⁾((2n+1)/e^{3/2})^{−(n+½)²}(1 + O(n^{−2})),
  the closed form gives, by the Barnes asymptotics (lim(A_n − MZ_n) = (3/4)log 2 − (3/2)log π − 2ζ′(−1) at (1, 2), e = −11/12),
    **A⁽⁰⁾ = e^{1/12}·2^{1/6}·3^{1/8}·A^{−3} = 0.663597802873585687992130374672…**
  *Independent check* (`checks/monien_direct.py` → `monien_direct.out`): direct det ζ(i+j) for n ≤ 90 at 600 digits, fitted as
  A⁽⁰⁾(1 + Σ_{k≤16}a_kx^k), x = 1/(2n+1), with no printed coefficient and nothing from §§1–3.2: A⁽⁰⁾ agrees to 2·10⁻³⁰, the fit
  returns a₁ = a₃ = 0 (to 10⁻²⁷, 10⁻²¹), a₂ = 1/24 and a₄ = −559/259200; and A⁽¹⁾ = (e^{9/8}/√6)A⁽⁰⁾ with Monien's second form
  agrees to 3·10⁻¹⁹.
- *Monien's printed constant.* arXiv:0901.1883v1 p. 1 prints A⁽⁰⁾ ≈ 0.351466738331 and the x⁴ coefficient −12319/259200 (page
  rendered and read, scratchpad). Both disagree with the direct computation, and the printed A⁽⁰⁾ also disagrees with Monien's own
  value H₁₀₀⁽⁰⁾ ≈ 4.9·10⁻¹⁶⁶⁸⁴ (it gives 2.6·10⁻¹⁶⁶⁸⁴; 0.66360 gives 4.8999·10⁻¹⁶⁶⁸⁴). His ratio A⁽¹⁾/A⁽⁰⁾ = e^{9/8}/√6 agrees.
  Finch (2014) quotes 0.351466738331 and states that no closed form is known. Recorded as a discrepancy to report, not as an
  error claim: a later version of Monien's paper was not checked. Second witness (R1 F8): Monien's H₁₀₀⁽¹⁾ ≈ 4.3·10⁻¹⁶⁸⁷¹ agrees with
  the closed form (4.26·10⁻¹⁶⁸⁷¹), not with the printed constant (2.26·10⁻¹⁶⁸⁷¹). R1 also fitted det ζ(i+j) independently (own LDL code,
  n ≤ 70) and matched A⁽⁰⁾ to 4·10⁻⁴⁵.

### 3.5 General p (OPEN)
Π(3) = −1.12209725218754456180 and Π(4) = −1.38879411029830148621 have no relation with small coefficients over {1, log A, log 2,
log 3, log 5, log π, log Γ(1/3)} resp. {…, log Γ(1/4)} at 20 digits (relations found have coefficients ~ 10²–10³, the size expected
by chance). *Heuristic:* the zeta layers ε_jn^{−1−jp} of b_n contribute constants of the form ε_jζ(jp) to K; the series in j
diverges factorially (ζ(−jp) grows like (jp)!), so for p not an even integer an elementary closed form is not expected, while at
even p all ζ(−jp) vanish. p = 4 does not fit the simplest elementary ansatz either, so derivative terms (ζ′(−jp) ∝ ζ(jp+1) at even
p) may enter. p = 1 and p = 2 are the two cases where the layers are absent or merge with the integer layer. Higher precision at p = 3
(n = 120, dps 2600, K_p3_hi.out): Π(3) = −1.122097252187544561816936 (n vs n − 10: 4·10⁻³²; the 20-digit value above agrees to
2·10⁻²⁰). PSLQ at 29 digits over {1, log A, log 2, log 3, log 5, log π, log Γ(1/3)}, alone and with ζ′(−3), ζ(3), ζ(3)/π² added: no
relation with coefficients ≤ 2000 except one 10-term relation with all coefficients 269–869, which is the size expected by chance.
So Π(3) is not an elementary combination of these constants (at this precision), consistent with the heuristic.

## 3.6 Status of the check runs
`../C/checks/rate_C.out` and `../CG/checks/check_F7.out` are **partial**: the runs were stopped (2026-11-06) after (2, 3) for the rate
(extrapolated e = −2.0, predicted −2) and after (2, 2), (2, 3), (3, 2.5) for F7 (e₂ extrapolated to 1·10⁻⁹, 7·10⁻⁸, 3·10⁻⁹ of the
prediction). The cases not reached are covered by R1's independent runs (review/checks/: rate at (3, 5/2) and (0.7, 2); centring at
p = 0.7; e₂ at (3, 2.5)), and by the earlier exploratory run of rate_C at n ≤ 100 (values consistent with e at (3, 2.5), (1.5, 2),
(2.5, 4), (0.4, 1.5), (0.7, 1.6)).

## 4. Rule A (self-check)
1. *R uses Theorem C's constant*: only to fix the constant; the n-dependence is from E2.1/E3.1. ✓ The p = 2 values match an exact
   formula, so a sign error would show. ✓
2. *F7, step (3)*: requires the expansions of b_j for both σ and σ′ to be summed from j = 1; finitely many j contribute only to κ,
   which is then forced to 0 by Theorem A. ✓ Uniformity in j is not needed (fixed (p,s), then (p,s+2p)).
3. *F7, step (4)*: the claim "no N^{−1} bracket term" is used for the first-order layers and for μ₁²; both are in N.6(ii). ✓ The
   second-order weight-≥3 layers are the only unproved ingredient and are excluded by p > 1/3. ✓
4. *FE*: uses 1/λ_{m+1} − 1/λ_m asymptotics. Originally derived from F7; R1 F2 showed the step bound D = o(1/N) suffices, which
   needs only E2.1/E3.1, so FE holds for every p ≠ 1 where K is defined. ✓ (Re-checked by the author before relabelling.)
5. *K1 at p = 1*: K is defined with the conjectural e(1, s); the independent Monien fit does not use it and agrees. ✓
6. *PSLQ*: K2 is confirmed to 45 digits at s = 2 by an exact formula; K1 by an independent fit at 30 digits. ✓ Π(3), Π(4): no
   claim.

## 5. Rule R log
R1 (review/REVIEW_D_R1.md; own code in review/checks/, no cglib): R ACCEPT; F7 ACCEPT WITH FIXES; FE ACCEPT WITH FIXES; Kp, K1, K2, MZ
ACCEPT as labelled; Monien misprint ACCEPT (PDF read). Applied: F1 (N^{−3p} term for 1/3 < p < 1/2, GAP F7-small widened), F2 (FE
from D = o(1/N), range widened to p > 1 and 0 < p < 1 with 1/p ∉ ℕ), F3 (K undefined at p = 1/K), F4 (sign convention of d₃), F5
(L_n convention stated), F8 (H₁₀₀⁽¹⁾ witness). F6, F7 (nits on notation in §1 and on where p ≠ 1 is used) noted; no change of
substance. One reader only.
