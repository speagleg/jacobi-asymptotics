# Rule R review — Plan 52 (Route II for s ≥ 1 + 2p: Christoffel transfer, GAP-α for the law)

Reviewer: independent second reader (Rule R). Branch `plan-52-r2alpha`, commit c2f1cb0 (`git diff master...HEAD`).
Scope: `research/G1/RH/route2/ROUTE2_alpha.md` (all of §§1–8), `research/G1/PROOF.md` §0 row "SH / B_all", §3.21, §4 note;
`research/G1/LOG.md` Plan 52 entry; `research/G1/RH/CITATIONS.md` entries "(Christoffel-attrib, Plan 52)", "(RII-inherited,
Plan 52)"; `research/G1/RH/route2/ROUTE2.md` GAP-α note; checks `check_r2alpha_christoffel.py/.out`, `check_r2alpha_law.py/.out`;
plan `docs/superpowers/plans/2026-10-14-plan-52-r2alpha.md` (Review focus followed item by item).

## Verdicts

| Item | Verdict | Label after review |
|---|---|---|
| Shift identity x·σ_s = σ_{s+p} | ACCEPT (exact, same Ψ, also truncated) | PROVED |
| Lemma CP | ACCEPT | PROVED (self-contained; classical) |
| Lemma CT | ACCEPT (all indices, β vs b², LU/UL checked; independent 400-digit check incl. mass at 0) | PROVED (self-contained; classical, novelty not claimed) |
| Lemma CS | ACCEPT (the crux is correct) | PROVED (self-contained); novelty: **very likely KNOWN** in chain-sequence form (F1) |
| Theorem SH | ACCEPT | PROVED (self-contained); novelty UNCHECKED |
| Lemma CS-r | ACCEPT (every inequality re-derived; the O(√r_n) bound is sharp in general, F4) | PROVED |
| Theorem SH-r | ACCEPT | PROVED |
| Corollary B_all | ACCEPT WITH FIXES (F2: the "both parts of Plan 48 are used" remark is wrong as a necessity; better base window) | PROVED-mod-cite (inherits RII / B_{p>1}) |
| Remark SH-1/n | ACCEPT WITH FIXES (F5: the tilt transfer is a proved implication, label understated) | identity + equivalence PROVED; hypothesis NUMERICAL; tilt transfer CONDITIONAL (implication PROVED) |
| Route (a) remarks | ACCEPT | HEURISTIC / OBSTRUCTION (scoped) |
| Numerics | ACCEPT WITH FIXES (F3: K-convergence scopes slightly overstated for e_n and for the s = 3, 4 bases) | NUMERICAL |
| GAP-α | closed **for the law**, p > 1 | as written |

**Overall: ACCEPT WITH FIXES.** No mathematical error found. All fixes are wording / scope / attribution; none changes a
PROVED label downward.

## Checks performed

1. **Lemma CP.** Re-derived. The odd-multiplicity-zero argument is standard; factors (x − y), y ≤ 0 (incl. y = 0) are > 0 on
   (0, ∞), P_nπ ≥ 0 on [0, ∞) by continuity, ∫P_nπ dσ > 0 by infinite support. Mass at 0 is harmless (P_nπ(0) ≥ 0 is all
   that is used). Conclusion (−1)^nP_n(0) > 0 ✓.
2. **Lemma CT, every index.** Convention xP_n = P_{n+1} + α_nP_n + β_nP_{n−1}, β_n couples P_{n−1}, P_n (β_n = b_n², repo
   1-based b_n; toolkit b2[n−1]) — consistent throughout ROUTE2_alpha and both scripts.
   (i) recurrence at 0 ÷ P_n(0): α_n = g_n − β_nP_{n−1}(0)/P_n(0) = g_n + β_n/g_{n−1} ✓; n = 0: α_0 = −P_1(0) = g_0 ✓.
   (ii) Q_n monic of degree n (numerator vanishes at 0 by definition of g_n) ✓; ∫Q_nx^jdσ̃ = ∫(P_{n+1} + g_nP_n)x^jdσ = 0,
   j ≤ n − 1 ✓; P_n − Q_n of degree ≤ n − 1, orthogonal (σ̃) to degree ≤ n − 2 ⇒ multiple of Q_{n−1} ✓; comparison gives
   h′_n = h_n ✓ (and h′_0 = 0 = h_0 since P_0 = Q_0); xQ_n = P_{n+1} + g_nP_n = Q_{n+1} + (g_n + h_{n+1})Q_n + g_nh_nQ_{n−1} ✓.
   So α̃_n = g_n + h_{n+1}, β̃_n = g_nh_n (n ≥ 1) ✓. Matrix form: with J_{n,n} = α_n, J_{n,n−1} = β_n, J_{n,n+1} = 1, L unit lower
   bidiagonal (L_{n,n−1} = h_n), U upper bidiagonal (U_{nn} = g_n, U_{n,n+1} = 1): (LU)_{nn} = g_n + h_n, (LU)_{n,n−1} = h_ng_{n−1},
   (LU)_{n,n+1} = 1; (UL)_{nn} = g_n + h_{n+1}, (UL)_{n,n−1} = g_nh_n ✓. "LU ↦ UL" is the correct direction.
3. **Independent numerical check of CT** (reviewer's own script, not in the repo): 400-digit discretized Stieltjes on a
   61-atom measure **with an atom at 0** (mass 0.3) plus k^{−3}e^{√log(k+e)} at k^{−2}, k ≤ 60, n ≤ 40, with g_n computed
   **directly as −P_{n+1}(0)/P_n(0)** (the repo scripts compute g_n by the recursion of CT(i), which makes (i) tautological
   there). Results: signs (−1)^nP_n(0) > 0 all n; |α_n − g_n − h_n|/α_n ≤ 2·10⁻⁴⁰¹; transfer vs direct coefficients of x·σ
   (atom at 0 dropped): 1.1·10⁻³⁸³ (α̃), 1.3·10⁻³⁸³ (β̃). Confirms CT(i), CT(ii) and Rule A (b).
4. **Lemma CS (crux).** Re-derived line by line.
   - G_{n−1}H_n = κ_nB_n²: n^ph_n·(n − 1)^pg_{n−1} = n^{2p}β_n((n − 1)/n)^p ✓ (the scaling with (n − 1)^p vs n^p is exactly κ_n).
   - A priori: G_n < A_n, H_n < A_n by positivity; G_{n−1} = κ_nB_n²/H_n > κ_nB_n²/A_n → c/2 ✓. So G ∈ [c/3, 3c] eventually.
     This lower barrier is **the** place where positivity (supp σ ⊂ [0, ∞)) enters, and it is what makes the neutral fixed
     point attracting from below.
   - F(G) − G = −(G − c)²/G, F(c + t) = c + ct/(c + t) ✓; d = δ²/(3c) ✓ on [c/3, 3c] ∖ (c − δ, c + δ).
   - Lower bound: once below c − δ, drift ≤ −d/2 per step, so G would leave [c/3, 3c] — contradiction ✓.
   - Upper band: from G_n < c + δ, G_{n+1} < F(c + δ) + δ < c + 2δ; from c + δ ≤ G_n < c + 2δ, G_{n+1} < G_n − d/2; cannot stay
     ≥ c + δ forever ✓. The o(1) perturbation is handled by fixing δ first, then n₂ with |η| < min(d/2, δ) ✓.
   - *Is convergence forced at a double fixed point with o(1) noise?* In general no (noise of fixed sign can hold a
     neutral orbit away from the fixed point at distance ≍ √|η|), but here the distance is ≤ 2δ for every δ once
     |η| < δ²/(6c), i.e. limsup|G − c| ≲ √(sup_{m≥n}|η_m|) → 0. The one-sidedness F(G) ≤ G plus the positivity barrier
     is exactly what is needed. ✓ c > 0 is used only for the a priori bound and the map F (Rule A (c)) ✓.
5. **Theorem SH.** n^pα̃_n = G_n + (n/(n + 1))^pH_{n+1}, n^{2p}β̃_n = G_nH_n ✓. Iteration: x^jσ again positive on [0, 1],
   infinite support ✓. Remark (1) (any scale s_n, s_{n−1}/s_n → 1): the proof only uses κ_n → 1 and s_n/s_{n+1} → 1 ✓.
   SH holds for every p > 0 (not only p > 1), as the text says (§5 remark, Rule A (h)); it is node-agnostic as well (any
   atoms x_k > 0: weights w_k ↦ x_kw_k).
6. **Lemma CS-r.** Re-derived: |κ_n − 1| ≤ p/(n − 1) holds for **all** p > 0 (for p < 1 via (1 − x)^p ≥ 1 + p log(1 − x) ≥
   1 − px/(1 − x)) ✓; λ² = 6cM₁ gives u²/G ≥ 2M₁r on the lower branch ✓; Λ condition ✓; step (α): u ↦ cu/(c + u) increasing on
   (−c, ∞) (|u| ≤ c/2 there) ✓, ct/(c + t) ≤ t − t²/(2c) for t ≤ c ✓, √r_n − √r_{n+1} ≤ √r_n(1 − √(n/(n + 1))) ≤ √r_n/(2n) (the
   last since 2n ≤ n + 1 + √(n(n + 1))) ✓, 1/n ≤ r_n/r_1 ≤ √(r_n/r_1) ✓; entry (β): decrease ≥ M₁r_n per step, Σr_n = ∞ ✓;
   increments |G_n − G_{n−1}| ≤ u_{n−1}²/G_{n−1} + |η_n| = O(r_{n−1}) = O(r_n) (r_{n−1} ≤ 2r_n) ✓. Regular-majorant
   construction ✓ (monotonicity of ρ is used; ρ(m) = sup_{k≥m}… is non-increasing, so 1/n + ρ(⌈n/M₀⌉) qualifies).
7. **Theorem SH-r.** Both formulas: √(G_nH_n) = B_n(κ_nG_n/G_{n−1})^{1/2} ✓; n^pα̃_n = A_{n+1} − (G_{n+1} − G_n) + O(1/n) ✓
   (H bounded). Only increments enter ✓. Index-shift invariance (§1): r_{n±1} ≍ r_n, (n/(n ± 1))^p = 1 + O(r_n) ✓; RII's form
   (n^pb_n = c(1 + O(1/n)), a_n/(2b_n) = 1 + O(1/n)) ⇔ |A_n − 2c| + |B_n − c| = O(1/n) under any ±1 pairing ✓.
8. **Corollary B_all.** α_x = (s − 1 − p)/p for atoms k^{−p} with weights k^{−s} (density ≍ x^{(s−1−p)/p}) ✓; RII and B_{p>1}
   (PROOF.md §3.17) cover exactly 1 < s < 1 + 2p ⇔ α_x ∈ (−1, 1), including α_x = 0 (Lemma W′) ✓. Choice of m: s₀ ∈ (1, 1 + 2p),
   and s₀ ≥ 1 + p when m ≥ 1 ✓. Shift with the same Ψ: x_kw_k = k^{−p}k^{−s}Ψ(k) exactly ✓; RedA's smoothing happens inside
   B_{p>1} at s₀ and does not interact with the shift ✓. Rate form of B_{p>1} ("n^pb_n → c, n^pa_n → 2c with rate
   O(1/n + ρ(n/M₀))") is the |A_n − 2c| + |B_n − c| form ✓.
9. **Remark SH-1/n.** Expansion re-derived: n(B̃_n/c − 1) − n(B_n/c − 1) = −p/2 + (n/2)(G_n/G_{n−1} − 1) + O(1/n) under an O(1/n)
   law ✓ (cross terms O(1/n) because G_n/G_{n−1} − 1 = O(1/n) by CS-r).
10. **Numerics re-run.** `check_r2alpha_christoffel.py` re-run from the jacobi-asymptotics root: part [1] reproduces the .out
    digit for digit, and part [2] (binary128, K = 4·10⁴) as well (runtime 2 min 21 s). Law numerics spot-checked with a reduced script (Ψ = 1,
    K = 1.2·10⁵, s = 3, 5, n = 100, 200, 400, long double): nB, E reproduce the .out to all printed digits (e.g. s = 5:
    −1.9728, −1.9863, −1.9936; E = 1.0036, 1.0018, 1.0018); direct long-double transfer s = 3 → 5 agrees with the directly
    computed coefficients to 1.5·10⁻¹⁵. All table values in ROUTE2_alpha §7 and §4.3 match the .out (K = 2.4·10⁵ column).

## Findings

**F1 (MEDIUM — novelty/attribution; no math change). Location: ROUTE2_alpha label table (Lemma CS "NEW-or-KNOWN:
UNCHECKED"), §3.1 "Why it works", PROOF.md §3.21, CITATIONS "(Christoffel-attrib)".**
Lemma CS is, after a change of variables, a statement about **chain sequences**: with a_n := β_n/(α_{n−1}α_n) and
m_n := h_n/α_n one has a_n = (1 − m_{n−1})m_n, m_0 = 0, i.e. (m_n) is the minimal parameter sequence of the chain sequence
(a_n) (Wall; Chihara, *An Introduction to Orthogonal Polynomials* (1978), Ch. III and the kernel-polynomial section of Ch. I;
Chihara's papers on chain sequences). Law P gives a_n = κ_nB_n²/(A_{n−1}A_n) → 1/4, and Lemma CS ⇔ m_n → 1/2 — the
"parabolic" chain-sequence limit (f(m) = 1/(4(1 − m)) has the double fixed point ½, f(m) ≥ m, and m_n < 1 is the barrier).
Convergence of parameter sequences of convergent chain sequences is a classical topic and the a = 1/4 case is very likely
in that literature. Not searched (no Rule L). Fix: (i) add the chain-sequence reformulation in one line to §3.1; (ii) change
the novelty note to "very likely KNOWN (chain sequences, a_n → 1/4 ⇒ parameter sequence → ½); not checked"; (iii) add
Chihara 1978 (Ch. I kernel polynomials, Ch. III chain sequences) to the CITATIONS "(Christoffel-attrib)" pointer list
(attribution only, not read). Theorem SH as a "law transfer" may likewise be a known consequence (ratio-asymptotic /
Nevai-class preservation under Christoffel modifications is classical for zeros outside the support; here the zero is at
the accumulation point and the scale is n^{−p}, which is less standard). Keep "novelty UNCHECKED" for SH; do not claim it new.

**F2 (LOW–MEDIUM — overclaim/robustness in a remark). Location: ROUTE2_alpha §5 Remarks, first bullet; PROOF.md §3.21
Corollary B_all last sentence; LOG ("Base s₀ ∈ (1, 1 + 2p) (… length p)").**
The text says the base window [1 + p, 1 + 2p) "has length exactly p, so both RII's α_x = 0 case (Lemma W′) and its
α_x ∈ (½, 1) part (UR′(b′), Plan 48 Rule R F1) are used", and that a window like α_x ∈ [0, ½] would leave gaps. The second
part is right, but the first is a property of the **chosen** reduction, not a necessity. Any half-open s-window of length p
inside (1, 1 + 2p) works; in particular s₀ ∈ (1 + p/2, 1 + 3p/2] (α_x ∈ (−½, ½]) reaches every s > 1 + p/2, and on that
window RII is covered by the **original** UR′ argument (REVIEW_Plan48 F1: without F1 the proof covered |α_x| ≤ ½). So:
for every s > 1 + p/2, Corollary B_all does not depend on UR′(b′)/F1 at all; F1 is needed only for 1 < s ≤ 1 + p/2, which is
already Corollary B_{p>1}'s own range. Lemma W′ (α_x = 0) cannot be avoided: every length-1 α-window in (−1, 1) contains 0,
and for s ∈ 1 + p + pℕ the chain passes through α_x = 0. Fix: replace the remark by this (and optionally use the base
s₀ := the unique point of s − pℕ₀ in (1 + p/2, 1 + 3p/2] when s > 1 + p/2), stating which Plan 48 ingredients each s-range
depends on. The proof as written is correct (RII is REVIEWED for all |α_x| < 1); this only reduces the dependency footprint.

**F3 (LOW — numerical scope). Location: ROUTE2_alpha §4.3 ("K-converged for n ≤ 200 only"), §7 parenthesis, PROOF.md §3.21
NUMERICAL, LOG ("K-doubling: n ≤ 400 stable to ≤ 10⁻³").**
(a) e_n is not K-converged at n = 200 for the base s = 3: n·e_n = 0.676, 0.543, 0.509 (K = 6, 12, 24·10⁴, Ψ = 1); 0.566,
0.404, 0.359 (exp √log). It is converged at n = 100 (0.507/0.498/0.496) and, for s ≥ 4, roughly at n = 200 (≤ 0.4%).
Say "K-converged at n = 100 (and n = 200 for s ≥ 4)". The inference "e_n = O(1/n) rather than O(n^{−1/2})" rests on n ≤ 200
(s ≥ 4) and n = 100 (s = 3); keep it NUMERICAL and say "consistent with".
(b) The "≤ 6·10⁻⁴ (nB), ≤ 10⁻³ (E)" K-stability statement is true for the s = 5, 6 rows of the §7 table but not for the bases
s = 3, 4 (e.g. Ψ = 1, s = 3, n = 400: nB −1.0002 vs −0.9982, E 1.0008 vs 0.9981, i.e. 2–3·10⁻³), which enter dB. dB itself is
K-stable to 1.6·10⁻³ as stated (2·10⁻³). The LOG's blanket "n ≤ 400 stable to ≤ 10⁻³" should be scoped to s = 5, 6.
(c) Nit: PROOF.md §3.21 "n(a_n/(2b_n) − 1) … (1.001–1.007 at n = 400)": the K = 2.4·10⁵ values are 1.0004–1.0065.

**F4 (INFO — Rule A addition; strengthens the write-up). Location: ROUTE2_alpha §4.1 / §8 (e).**
The bound |G_n − c| = O(√r_n) of Lemma CS-r is **sharp** for the hypotheses of the lemma, so the "only increments enter"
design of SH-r is essential, not an artefact. Example: pick G_n = c + a/√n (a > 0), B_n := c, and A_n := G_n + κ_nc²/G_{n−1};
then g_n, h_n > 0, so (Favard + LU-positivity) these are the coefficients of a positive measure on [0, ∞), A_n − 2c =
(a² /c − pc)/n + O(n^{−3/2}) = O(1/n), yet G_n − c ≍ n^{−1/2}. (Equivalently: a 1/n-perturbation η_n ≈ e/n, e > 0, in
u_{n+1} = u_n − u_n²/G + η_{n+1} produces u_n ≈ √(ce/n).) The pure-power data have e = 0 (u_n = O(1/n)). Suggest adding this
one-line example to §8 (e).

**F5 (LOW — label understated). Location: ROUTE2_alpha label table and §4.3; PROOF.md §3.21 Remark SH-1/n.**
"Tilt-law consistency HEURISTIC" can be upgraded: from the exact expansion of check 9, if the tilt law
n(n^pb_n/c − 1) = −(s − 1 − ϑ_n)/2 + o(ϑ_n) holds at s and n(G_n − G_{n−1}) = o(ϑ_n), and nϑ_n → ∞ (so that the O(1/n)
remainder is o(ϑ_n); true for exp √log, ϑ_n ≍ (log n)^{−1/2}), then the tilt law holds at s + p with the same ϑ_n (same Ψ).
That is a PROVED conditional implication (CONDITIONAL on the tilt law at s and on the G-increment hypothesis), not a
heuristic. Note also (F4's example) that under a regular two-term expansion of A_n, B_n one gets u_n ≍ n^{−1/2} at worst,
whence n(G_n − G_{n−1}) ≍ n^{−1/2} → 0; so the "iff" hypothesis is plausibly provable under expansion hypotheses, though
o(ϑ_n) is not automatic (n^{−1/2} vs (log n)^{−1/2} is fine, but the general case needs an argument). Optional.

**F6 (INFO — scope sentence). Location: ROUTE2_alpha "Result in one line", "for every measure on [0, ∞)".**
Add "with infinite support" (as in Theorem SH). Also worth one sentence in §5 Remarks: SH is node-agnostic (any atoms
x_k > 0: law for (x_k, w_k) ⇒ law for (x_k, x_kw_k)) and works for every p > 0 and every scale s_n with s_{n−1}/s_n → 1, so any
future base case at p ≤ 1 (or for other node families) propagates upward in s. (The §5 p ≤ 1 bullet already says the p
part; the remark "for pure powers and bounded / log-type Ψ the law is already known for all s > 1" was checked against
PROOF.md: T3-all is stated "all n, p > 0" ✓.)

**F7 (INFO — CITATIONS). Location: CITATIONS "(RII-inherited, Plan 52)".** Correct as written. If F2 is adopted, add that
for s > 1 + p/2 only the |α_x| ≤ ½ part of RII is needed.

No HIGH findings. Review-focus items not listed above were checked and found correct (see Checks 1–10): CP sign argument
with mass at 0; CT index conventions, the step P_n − Q_n = h_nQ_{n−1} and h′_n = h_n; CS a priori bounds, F increasing,
F(G) ≤ G, F(c + δ) < c + δ, the escape-below and the band argument, c > 0 used only where stated; CS-r choices of λ, Λ,
step (α), entry (β), regular majorant; SH-r both formulas and index-shift invariance; B_all choice of m, rate form, same Ψ.

## Recommended labels

- Lemma CP: PROVED (self-contained; classical).
- Lemma CT: PROVED (self-contained; classical, novelty not claimed).
- Lemma CS: PROVED (self-contained); novelty: very likely KNOWN (chain sequences; F1), not checked.
- Theorem SH, Lemma CS-r, Theorem SH-r: PROVED (self-contained); novelty UNCHECKED.
- Corollary B_all: PROVED-mod-cite (inherits Theorem RII / Corollary B_{p>1}); with F2, for s > 1 + p/2 only the
  |α_x| ≤ ½ part of RII (plus Lemma W′) is used.
- Remark SH-1/n: identity and equivalence PROVED; hypothesis n(G_n − G_{n−1}) → 0 NUMERICAL (p = 2); tilt-law transfer
  CONDITIONAL (implication PROVED, F5) — or keep HEURISTIC if the authors prefer the conservative label.
- Route (a): HEURISTIC; OBSTRUCTION (heuristic, scoped). GAP-α: closed for the law (p > 1).
- After fixes F1–F3 (F4–F7 optional): REVIEWED.
